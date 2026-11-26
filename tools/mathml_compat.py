"""Presentation-only compatibility for Pandoc's parsed Math nodes.

The source documents are unchanged. A balanced-group parser expands only
legacy notation supported by this corpus. Ambiguous primitive-fraction or
font scopes are rejected rather than guessed. Prose and code are untouched.
"""
from __future__ import annotations

from collections import Counter
from decimal import Decimal, localcontext
import re

FONT_COMMANDS = {
    r'\rm': r'\mathrm', r'\it': r'\mathit', r'\bf': r'\mathbf',
    r'\cal': r'\mathcal', r'\sf': r'\mathsf', r'\tt': r'\mathtt',
}
OPERATORS = {r'\Log': 'Log', r'\Arg': 'Arg'}
IMPLICIT_SCOPES = {r'\begin', r'\end', r'\left', r'\right', '&', r'\\'}


def _groups(text: str) -> list:
    """Tokenize commands and explicit groups, respecting escapes/comments."""
    stack = [[]]
    i = 0
    while i < len(text):
        c = text[i]
        if c == '\\':
            match = re.match(r'\\(?:[A-Za-z]+|.)', text[i:], re.S)
            token = match[0] if match else '\\'
            stack[-1].append(token); i += len(token)
        elif c == '%':
            end = text.find('\n', i)
            end = len(text) if end < 0 else end + 1
            stack[-1].append(text[i:end]); i = end
        elif c == '{':
            group = []; stack[-1].append(group); stack.append(group); i += 1
        elif c == '}':
            if len(stack) == 1:
                raise ValueError('Unmatched closing brace in TeX math.')
            stack.pop(); i += 1
        elif c == '&':
            stack[-1].append(c); i += 1
        else:
            end = i + 1
            while end < len(text) and text[end] not in '\\{}%&':end += 1
            stack[-1].append(text[i:end]); i = end
    if len(stack) != 1:
        raise ValueError('Unmatched opening brace in TeX math.')
    return stack[0]


def _render(items: list, counts: Counter, explicit_group=False) -> str:
    commands = {x for x in items if isinstance(x, str)}
    overs = [i for i, x in enumerate(items) if isinstance(x, str) and x == r'\over']
    if overs:
        # TeX's infix fraction consumes the WHOLE current group. Font
        # declarations before it can affect its denominator too. The actual
        # corpus uses only explicit, unmixed groups; do not guess beyond it.
        if (not explicit_group or len(overs) != 1 or
                commands & (set(FONT_COMMANDS) | IMPLICIT_SCOPES)):
            raise ValueError('Unsupported primitive fraction scope: use an explicit \\frac numerator and denominator.')
        i = overs[0]; counts['primitive_fraction'] += 1
        return r'\frac{' + _render(items[:i], counts) + '}{' + _render(items[i+1:], counts) + '}'
    for i, item in enumerate(items):
        if not isinstance(item, str) or item not in FONT_COMMANDS:continue
        # Alignment/fence/environment groups have extra scope rules. The
        # retained formulas place these declarations in explicit labels.
        if commands & IMPLICIT_SCOPES:
            raise ValueError('Unsupported legacy font scope: use an explicit math font argument.')
        end = next((j for j in range(i+1, len(items))
                    if isinstance(items[j], str) and items[j] in FONT_COMMANDS), len(items))
        counts['legacy_font_declaration'] += 1
        return (_render(items[:i], counts) + FONT_COMMANDS[item] + '{'
                + _render(items[i+1:end], counts) + '}' + _render(items[end:], counts))
    result = []
    for i, item in enumerate(items):
        if isinstance(item, list):
            dimension = ''.join(item) if all(isinstance(x, str) for x in item) else ''
            metric = re.fullmatch(r'\s*([+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+))\s*mm\s*', dimension)
            if i and isinstance(items[i-1], str) and items[i-1] in {r'\hspace', r'\vspace'} and metric:
                with localcontext() as ctx:
                    ctx.prec = max(28, len(metric[1]) + 2)
                    cm = format(Decimal(metric[1]) / Decimal(10), 'f')
                result.append('{' + cm + 'cm}')
                counts['metric_spacing_unit'] += 1
            else:
                result.append('{' + _render(item, counts, True) + '}')
        elif item in OPERATORS:
            counts['named_operator'] += 1
            result.append(r'\operatorname{' + OPERATORS[item] + '}')
        elif item == r'\hbox':
            counts['text_box'] += 1; result.append(r'\text')
        elif item == r'\Bbb':
            # AMS \Bbb is a unary alias, not a rest-of-group declaration.
            counts['unary_font_alias'] += 1; result.append(r'\mathbb')
        else:
            result.append(item)
    return ''.join(result)



def _visible_labels(items: list, counts: Counter, top_level=True) -> list:
    """Keep row labels visible; Pandoc otherwise drops AMS tags from MathML.

    The retained source labels are all unstarred alphanumeric strings.
    Preserve their position in the equation/row and reject other grammars.
    """
    result = []; i = 0
    while i < len(items):
        item = items[i]
        if isinstance(item, list):
            result.append(_visible_labels(item, counts, False)); i += 1
        elif item == r'\tag':
            if not top_level:
                raise ValueError('Unsupported equation tag inside a TeX group.')
            j = i + 1
            while j < len(items) and isinstance(items[j], str) and items[j].isspace():
                j += 1
            if j == len(items) or not isinstance(items[j], list):
                raise ValueError('Unsupported equation tag: expected an unstarred alphanumeric label.')
            group = items[j]
            label = ''.join(group) if all(isinstance(x, str) for x in group) else ''
            if not re.fullmatch(r'[A-Za-z0-9]+', label):
                raise ValueError('Unsupported equation label: use an alphanumeric tag.')
            after = j + 1
            while after < len(items) and isinstance(items[after], str) and (items[after].isspace() or items[after].startswith('%')):
                after += 1
            if after < len(items) and items[after] not in [r'\\', r'\end']:
                raise ValueError('Unsupported nonterminal equation tag.')
            result.extend([r'\qquad', r'\text', ['(' + label + ')']])
            counts['visible_equation_label'] += 1
            i = j + 1
        else:
            result.append(item); i += 1
    return result


def normalize_math(tex: str, display: bool) -> tuple[str, dict]:
    counts = Counter()
    rendered = _render(_visible_labels(_groups(tex), counts), counts)
    return rendered, dict(counts)


def normalize_document(document: dict) -> tuple[dict, dict]:
    counts = Counter()
    def walk(node):
        if isinstance(node, dict):
            if node.get('t') == 'Math':
                mode, source = node['c']
                rendered, changes = normalize_math(source, mode['t'] == 'DisplayMath')
                node['c'][1] = rendered; counts.update(changes)
            else:
                for value in node.values():walk(value)
        elif isinstance(node, list):
            for value in node:walk(value)
    walk(document)
    return document, dict(counts)
