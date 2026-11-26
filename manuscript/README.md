# Volume limits from planar tangles

[Read the reference manuscript](build/main.pdf) ·
[Current papers](../papers/README.md) ·
[Illustrated reading guide](../book/chapters/manuscript.md)

The current reference has 210 pages. The
[revision report](../repro/MANUSCRIPT_AND_LOGIC_AUDIT_2026-11-25.md) records
its mathematical corrections and the comparison of its statements with Lean.

The reference begins with the strict Conway theorem, proved through
its pure auxiliary source. It includes the same proof files as the
[19-page Conway paper](../papers/conway-asymptotics/README.md).

The reference also retains the independent circle-tree and planar
volume families. Moving-meridian expansions, preferred-longitude
identifications and conditional recurrence-symbol results remain
available in their separate [subject papers](../papers/README.md);
they are not extra premises of the volume theorem.

The current edition incorporates the [first-edition corrections](ERRATA.md).
Earlier tracked sources remain in Git history.

## The strict Conway theorem and its hypotheses

Fix a finite ordered Conway expression with at least two elementary
crossing circles. Its strict-state test requires leaf labels in
\((0,1/2)\), complemented turn labels, product labels
\(\max(x,y)<z<x+y<1\), and complementary closing outputs.
An elementary closing child is allowed. Choose retained crossing
parities whose strand connections form one knot, including no component
closed inside a box.

Theorem `ca:main` proves the whole reduced-invariant asymptotic and
volume limit when every auxiliary integer filling is independently
sufficiently long in absolute value. The diagram and fillings are fixed
before \(N\) tends to infinity through all integers. There is no common
sign or ratio condition. The main knot cusp stays complete.

For a fixed construction this covers a natural-density-one subset of
the integer assignment lattice. It is not a density statement about
distinct knots, and it leaves infinitely many assignments outside the
sufficient condition.

The proof has five distinct inputs:

1. Exact finite Newton algebra and a primitive wire lattice.
2. A strict positive optimizer and exact factorial interpolation.
3. A pure source expansion, the physical remainder bound, and both local
   and global Fourier estimates.
4. A whole oscillatory-filling theorem with a nonzero leading coefficient.
5. The marked primitive metric and absolute action-volume comparison.

The shared source files are
[introduction.tex](../papers/conway-asymptotics/introduction.tex),
[factorial.tex](../papers/conway-asymptotics/factorial.tex),
[lattice.tex](../papers/conway-asymptotics/lattice.tex),
[packet.tex](../papers/conway-asymptotics/packet.tex),
[pure-window.tex](../papers/conway-asymptotics/pure-window.tex) and
[filling.tex](../papers/conway-asymptotics/filling.tex).
This keeps the book and standalone proof aligned.

## The conceptual chapters

[Exact operations, orthogonality and stationary elimination](sections/02-exact-concepts.tex)
proves the Gram form \(G=B^*B\) for finite synthesis, shifted Fourier
Parseval, the bound
\(2\sqrt N(1+|n|/\sqrt{12})\) for the full Hermite coefficient vector,
and the stationary Schur-complement formula. It explains what each
operation preserves and which lower bounds it does not provide.

[From complex asymptotics to volume limits](sections/09-reproduction.tex)
proves the final scalar implication in full:
\(K_N=u_N(N^\rho a_Ne^{NS_N}+E_N)\), with \(|u_N|=1\),
\(a_N\to a\ne0\), \(S_N\to S\), and a strict upper exponential gap
for the entire remainder. These hypotheses give eventual nonvanishing
and the ordinary logarithmic limit. A separate nonnegative-cost lemma
transfers source upper rates through level-dependent polynomial costs,
including zero values.

## Independent volume families

| Family | Required extra condition |
| --- | --- |
| Ordered circle trees | A summed or directed degree-and-twist test. The directed sufficient test allows \(d_v\ge2^{28}\) or \(|n_v|\ge2^{27}\) at each vertex. |
| Terminally decorated matched spheres | A specified finite decoration gives strict shared packing inequalities; all final auxiliary powers are sufficiently long. The decoration can change the knot. |
| Unchanged matched spheres | Weak balance, including the stated quantified defect variant. |
| Protected triangular sums | A certificate for every locally allowed noncentral sector in each input. |
| Ordinary triangular insertion | Certified inputs and small boundary ratios at every required witness. |

These results keep their separate finite-sum and geometric proofs.
High degree can permit a fixed short or zero power in a circle tree;
that does not relax the strict Conway theorem's long-filling hypothesis.
The local ratio test \(\max_v d_v/(d_v^2+n_v^2)\le2^{-120}\) now follows
directly from the directed theorem, by the lemma in the
[local criterion](sections/08b-local-circle-messages.tex);
there is no independent local quantum induction. The summed argument
retains its explicit first meridian correction. The separate geometric
criterion \(L_v=\sqrt{d_v^2+n_v^2}\ge630\) constructs the metric but
does not prove a quantum asymptotic.

Two supporting results have narrower conclusions. The uniform filling
appendix is a finite norm estimate and needs a source bound for a volume
application. The general matched-sphere geometric contribution has a
nonzero asymptotic, but does not bound its entire complement for every
unchanged diagram.

## Reading and reproduction

Start with the [scope table](sections/01-introduction.tex), then the
conceptual chapter and shared Conway proof. For another family, read its
own theorem and follow its stated finite-sum and metric dependencies.
The [dependency graph](../docs/papers/dependencies.html) records named
uses; it does not verify their mathematics.

From the repository root, build the reference with:

```sh
python3 tools/build_manuscript.py
```

This writes `manuscript/build/main.pdf`, figure previews and a manifest.
The build checks typesetting, references and inputs; it does not prove
the mathematical arguments.

The Conway finite identities and rational certificates can be replayed
separately:

```sh
python3 -I papers/conway-asymptotics/check.py
python3 repro/verify.py --output repro/results
```

For all registered paper checks:

```sh
python3 repro/check_paper_algebra.py --output repro/results/paper-algebra
```

The [reproduction guide](../repro/README.md) gives requirements and
individual commands. Finite samples do not prove uniform asymptotics.
The [formal code](../formal-real/README.md) proves the retained Gram and
complex bilinear Schur block identities, actual shifted Parseval and
Fourier–Hermite mass bounds, and ordinary complex rate transfer.
[ConwayAssembly](../formal-real/ConwayAssembly.lean) derives the entire
filled-remainder estimate from the actual coherent color sum and proved
crossing coefficient bound. That bound holds at \(N\ge2\); the
physical source identity is required only at \(N\ge3\). The source contour, nonzero
whole packet and primitive geometric comparison remain written inputs. The
[coverage map](../formal/coverage.json) and
[cleanup record](../repro/PROOF_PATH_CLEANUP_2026-11-25.md) identify its
manuscript statements and replay command.

To rebuild the manuscript page in the guide after the PDFs are ready:

```sh
python3 tools/build_manuscript_guide.py
```

The complete guide build is `python3 tools/build_book.py`, followed by
`python3 tools/check_book.py`. The guide's methods chapters retain
historical and exploratory approaches separately from this current
proof path.
