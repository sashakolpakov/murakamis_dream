from pathlib import Path
import re, subprocess, hashlib, json

source = Path('/private/tmp/md-balanced-simple-sphere-volume.md')
target = Path('/private/tmp/md-balanced-fans-appendix.tex')
original = source.read_text()
text = original
tags = re.findall(r'\\tag\{([^}]+)\}', text)
assert len(tags) == len(set(tags))
math_pattern = re.compile(r'(\\\(.*?\\\)|\\\[.*?\\\]|\$\$.*?\$\$|(?<!\$)\$(?!\$)[^\n]*?(?<!\$)\$(?!\$))', re.S)
parts = math_pattern.split(text)
for i in range(0, len(parts), 2):
    for tag in sorted(tags, key=len, reverse=True):
        parts[i] = parts[i].replace('(' + tag + ')', r'\eqref{bl:' + tag + '}')
    # Terminology changes are prose-only; mathematical strings are untouched.
    parts[i] = re.sub(r'\bMAIN\b', 'strand', parts[i])
    parts[i] = re.sub(r'\bports\b', 'crossing circles', parts[i])
    parts[i] = re.sub(r'\bport\b', 'crossing circle', parts[i])
    parts[i] = parts[i].replace('finite LOCAL charge sector', 'finite local charge sector')
text = ''.join(parts)
text = text.replace('# Balanced terminal decorations and volume limits beyond tangle-operation trees',
                    '# Proof of balanced terminal decoration', 1)
text = text.replace('Let \\(D\\) be a fixed connected augmented link diagram with the following data.',
    'A strand edge is an edge of the white triangulation not used in its crossing-disk matching. '
    'Let \\(D\\) be a fixed connected augmented link diagram with the following data.', 1)
text = text.replace(', meaning a nonmatching side in the white triangulation and called strand in the source formulas', '')

display_pattern = re.compile(r'\\\[(.*?)\\\]|\$\$(.*?)\$\$', re.S)
def display(m):
    body = m.group(1) if m.group(1) is not None else m.group(2)
    tag = re.search(r'\\tag\{([^}]+)\}', body)
    if tag:
        body = re.sub(r'\\tag\{[^}]+\}', '', body).strip()
        return '\n\\begin{equation}\\label{bl:' + tag.group(1) + '}\n' + body + '\n\\end{equation}\n'
    return '\n\\[\n' + body.strip() + '\n\\]\n'
text = display_pattern.sub(display, text)
text = re.sub(r'^(#{2,6})\s+\d+(?:\.\d+)*\.\s+', r'\1 ', text, flags=re.M)

def link(m):
    label, path = m.group(1), m.group(2)
    if label.endswith('.md'):
        label = re.sub(r'^(actual|general|research)_', '', Path(label).stem).replace('_', ' ')
    if '.md' in path:
        stem, sep, anchor = path.partition('#')
        path = 'https://sashakolpakov.github.io/murakamis_dream/notes/' + Path(stem).stem + '.html' + (sep + anchor if sep else '')
    elif path.startswith('../experiments/'):
        path = 'https://github.com/sashakolpakov/murakamis_dream/blob/main/experiments/' + Path(path).name
    return '[' + label + '](' + path + ')'
text = re.sub(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)', link, text)
input_path = Path('/private/tmp/md-balanced-fans-appendix-input.md')
input_path.write_text(text)
result = subprocess.run(['pandoc', str(input_path), '-f', 'markdown+tex_math_single_backslash+raw_tex',
    '-t', 'latex', '--top-level-division=chapter', '--wrap=preserve'], capture_output=True, text=True, check=True)
tex = result.stdout.replace(r'\tightlist', '')
for label in sorted(set(re.findall(r'\\label\{([^}]+)\}', tex)), key=len, reverse=True):
    if label.startswith('bl:'):
        continue
    tex = tex.replace(r'\label{' + label + '}', r'\label{bl:' + label + '}')
    tex = tex.replace(r'\hyperref[' + label + ']', r'\hyperref[bl:' + label + ']')
tex = re.sub(r'(\\chapter\{[^}]+\})', lambda m: m.group(1) + '\n\\label{app:balanced-terminal-fans}', tex, count=1)
target.write_text(tex)

def normalize(s):
    return re.sub(r'\s+', '', re.sub(r'\\(?:label|tag)\{[^}]*\}', '', s))
source_displays = [normalize(a if a is not None else b) for a, b in
    [(m.group(1), m.group(2)) for m in display_pattern.finditer(original)]]
target_displays = [normalize(m.group(1) if m.group(1) is not None else m.group(2)) for m in
    re.finditer(r'\\\[(.*?)\\\]|\\begin\{equation\}(.*?)\\end\{equation\}', tex, re.S)]
# Inline mathematics is checked independently after removing all displays.
def inline(s):
    s = re.sub(r'\\begin\{equation\}.*?\\end\{equation\}', '', s, flags=re.S)
    s = display_pattern.sub('', s)
    return [normalize(m.group(1) if m.group(1) is not None else m.group(2)) for m in
        re.finditer(r'\\\((.*?)\\\)|(?<!\$)\$(?!\$)([^\n]*?)(?<!\$)\$(?!\$)', s, re.S)]
source_inline, target_inline = inline(original), inline(tex)
labels = re.findall(r'\\label\{([^}]+)\}', tex)
refs = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', tex)
report = {
    'source': str(source), 'target': str(target),
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'target_sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
    'display_count': len(source_displays), 'converted_display_count': len(target_displays),
    'ordered_displays_identical': source_displays == target_displays,
    'inline_count': len(source_inline), 'converted_inline_count': len(target_inline),
    'ordered_inline_identical': source_inline == target_inline,
    'duplicate_labels': [label for label in set(labels) if labels.count(label) > 1],
    'unresolved_internal_refs': sorted(set(refs) - set(labels)),
    'numeric_section_refs': re.findall(r'\b[Ss]ections?\s+\d[^\n]*', tex),
    'private_path_hits': re.findall(r'/private/\S+|/Users/\S+', tex),
    'control_bytes': [(i, ord(c)) for i,c in enumerate(tex) if ord(c)<32 and c not in '\n\r\t'],
    'pandoc_stderr': result.stderr,
}
Path('/private/tmp/md-balanced-fans-appendix-fidelity.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
assert source_displays == target_displays
assert source_inline == target_inline
assert not report['duplicate_labels']
assert not report['unresolved_internal_refs']
