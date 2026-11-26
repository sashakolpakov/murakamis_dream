"""Exact internal-reference repairs for Appendix I; no writes on import.
Apply after converting the public note to TeX.
External source-note section numbers deliberately remain unchanged.
"""
from pathlib import Path
import json
REPLACEMENTS = {
    "retained in section 5.": r"retained in Section~\ref{gi:the-complete-anchor-and-the-primitive-filling-equations}.",
    "calculation in section 10.": r"calculation in Section~\ref{gi:the-determinant-one-sign-at-the-complete-filled-knot}.",
    "as established in subsection 2.2.": r"as established in Section~\ref{gi:the-auxiliary-longitude-equations-and-the-local-gluing-locus}.",
    "in section 4 below.": r"in Section~\ref{gi:ordered-pages-and-the-half-twist-collar} below.",
    "The face construction in section 2 supplies": r"The face construction in Section~\ref{gi:the-local-face-maps} supplies",
    "returns. Section 4 then": r"returns. Section~\ref{gi:ordered-pages-and-the-half-twist-collar} then",
    "Sections 4 and 9 retain": r"Sections~\ref{gi:ordered-pages-and-the-half-twist-collar} and~\ref{gi:determining-the-monomial-and-the-preferred-framing} retain",
    "pure tree. Sections 6--9 identify": r"pure tree. Sections~\ref{gi:boundary-isotropy-and-the-edge-differential}--\ref{gi:determining-the-monomial-and-the-preferred-framing} identify",
    "determined in sections 6--9 using": r"determined in Sections~\ref{gi:boundary-isotropy-and-the-edge-differential}--\ref{gi:determining-the-monomial-and-the-preferred-framing} using",
    "Sections 2--4 have assembled": r"Sections~\ref{gi:the-local-face-maps}--\ref{gi:ordered-pages-and-the-half-twist-collar} have assembled",
    "the separate check in section 8.": r"the separate check in Section~\ref{gi:regular-reconstruction-at-every-nonzero-main-value}.",
    "By section 7 the discrepancy": r"By Section~\ref{gi:the-constant-field-of-the-source-equations} the discrepancy",
    "By section 8 its pullback": r"By Section~\ref{gi:regular-reconstruction-at-every-nonzero-main-value} its pullback",
    "knot qualifications of section 1.": r"knot qualifications of Section~\ref{gi:the-diagram-and-the-longitude-identity}.",
    "stated in subsection 11.4.": r"stated in Section~\ref{gi:the-irreducible-factor-and-its-field-of-definition}.",
    "same branch. Section 5 identifies": r"same branch. Section~\ref{gi:the-complete-anchor-and-the-primitive-filling-equations} identifies",
    "germ. Section 10 fixes": r"germ. Section~\ref{gi:the-determinant-one-sign-at-the-complete-filled-knot} fixes",
    "representation identification in section 5": r"representation identification in Section~\ref{gi:the-complete-anchor-and-the-primitive-filling-equations}",
}
EXTERNAL_REFERENCES_UNCHANGED = [
    "section 5. In particular the preserved product",
    r"meridian, by section 6 of",
]
def repair(text):
    counts = {old: text.count(old) for old in REPLACEMENTS}
    if any(v != 1 for v in counts.values()):
        raise ValueError(counts)
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    return text
if __name__ == "__main__":
    import argparse, re
    p=argparse.ArgumentParser()
    p.add_argument("input",type=Path)
    p.add_argument("--output",type=Path)
    args=p.parse_args()
    original=args.input.read_text()
    fixed=repair(original)
    report={
        "input":str(args.input),
        "replacements":len(REPLACEMENTS),
        "all_exact_matches":True,
        "external_references_preserved":all(x in original and x in fixed for x in EXTERNAL_REFERENCES_UNCHANGED),
        "remaining_numeric_section_references":re.findall(r".{0,35}\b(?:[Ss]ections?|[Ss]ubsections?)\s+[0-9][^\n]*",fixed),
        "missing_target_labels":[m for m in re.findall(r"\\ref\{(gi:[^}]+)\}",fixed) if r"\label{"+m+"}" not in fixed],
    }
    if args.output:
        args.output.write_text(fixed)
        report["output"]=str(args.output)
    print(json.dumps(report,indent=2))

