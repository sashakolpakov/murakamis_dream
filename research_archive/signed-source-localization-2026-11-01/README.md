# Bounds and finite transfer for the complementary contribution

This archive records the research following public commit
[`d8e0449`](https://github.com/sashakolpakov/murakamis_dream/commit/d8e0449891654ab1178b4f8e5b960045e04ba737).
It contains two quantitative bounds, an exact transfer reduction, and a
check of a possible geometric route. These results reduce parts of the
remaining problem. They do not establish the volume conjecture for a new
family of knots.

The published manuscript and guide are unchanged by this archive. The
[guide's methods chapter](https://sashakolpakov.github.io/murakamis_dream/guide/methods.html)
explains the existing approaches, and its
[notation chapter](https://sashakolpakov.github.io/murakamis_dream/guide/notation.html)
defines their objects. The former Sphinx pages redirect to the guide.

## The quantity that still needs to be bounded

Fix one of the marked diagrams to which the exact homogeneous source
formula applies. Let \(r\) be its number of crossing regions and let
\(N\) be the quantum level. Its spectral variables are
\(\boldsymbol{\sigma}=(\sigma_1,\ldots,\sigma_r)\in[-2,2]^r\).
The source polynomial \(S_N(\boldsymbol{\sigma})\) is obtained by
multiplying the local four-variable polynomials and extracting their
prescribed shared face coefficient. A face has one coefficient target,
even when it belongs to several local factors.

Set \(d=N-1\) and \(h=\lfloor d/2\rfloor\). Each local polynomial has
two distinguished middle exponents, denoted \(a\) and \(c\). Retaining
only monomials with \(a,c\le h\) in every factor gives a second shared
coefficient \(C_N\). This is the contribution called **CROSS** in the
existing formulas. The letters name a precise projection of the original
source; they do not define a second knot invariant. Write
\[
D_N=S_N-C_N.
\]

The published geometric-contribution theorem identifies the exponential
rate of the selected contribution after the original filling operations
with the volume of the resulting knot complement. It also proves that
this contribution is nonzero. To infer the same rate for the whole
invariant, the contribution of \(D_N\) must still be controlled.
For the broader class of unchanged matched-sphere diagrams, that estimate
is open.

One sufficient estimate would be
\[
\sup_{\boldsymbol{\sigma}\in[-2,2]^r}|D_N(\boldsymbol{\sigma})|
\le \exp\!\bigl(N(\Phi-\eta+o(1))\bigr),
\qquad
\Phi=\frac{\operatorname{Vol}(Y)}{2\pi},\quad \eta>0,
\]
where \(Y\) is the augmented complement before the crossing circles are
filled. The previously proved filling bound would then transfer this
strict gap to independently sufficiently long, fixed signed twists.
The strict gap matters: the volume of the filled knot complement is
smaller than the limiting augmented volume. An estimate merely at rate
\(\Phi\) does not suffice.

## A fixed interval near the positive spectral endpoint

The first result replaces an estimate at the single endpoint \(+2\) by
an estimate on an interval whose width is independent of \(N\). Put
\[
I_\delta=[2-\delta,2],\qquad
A_\delta=1+\delta^{-1/2},\qquad
\omega(\delta)=\sqrt{\delta}\bigl(2+\log(1+2/\sqrt{\delta})\bigr),
\]
where \(0<\delta\le1\). Every coefficient of an original local
numerator satisfies
\[
\sup_{\sigma\in I_\delta}|\text{coefficient}|
\le A_\delta N^3 e^{N\omega(\delta)}
\qquad\text{for }N\ge\pi/\sqrt{\delta}.
\]
The useful feature is \(\omega(\delta)\to0\) as \(\delta\to0\).

The proof first combines the signed one-step and two-step paths in the
local recurrence. An exact Green formula expresses the resulting
polynomial in nonnegative perturbation parameters. A weighted norm then
bounds its growth. Taking absolute values before combining those paths
would lose the small rate. The proof retains the unused spectral factors,
so it also applies at coincident roots.

The corresponding part of the filling functional includes both values
and derivatives at repeated roots. Markov's polynomial inequality on
\(I_\delta\) bounds these derivatives with only a polynomial cost in \(N\).
Consequently, the part of the original filling sum with all its spectral
coordinates in \(I_\delta\) is exponentially smaller than the geometric
contribution when \(\delta\) is sufficiently small and the fixed twists
are sufficiently long.

The [complete interval proof](proofs/md-fixed-spectrum-positive-end-continuant-and-source-corner.md)
also shows why a polynomial bound on a fixed interval would be false:
some individual local coefficients grow exponentially at
\(\sigma=2-\delta\). The theorem proves a small exponential rate, not a
polynomial bound.

## Mixed spectral regions

The same argument works when only some coordinates are near \(+2\).
An elementary estimate bounds every local coefficient on the entire
interval \([-2,2]\) by \(B^{N-1}\), where
\[
B=4(1+\sqrt2).
\]
Combining this bound with the interval estimate gives, for any specified
set \(J\) of \(k\) coordinates,
\[
\sup_{\substack{\sigma_e\in I_\delta\ (e\in J)\\
                 \sigma_e\in[-2,2]\ (e\notin J)}}|D_N|
\le
2A_\delta^kN^{3r+3k}
\exp\!\left(N\bigl[k\omega(\delta)+(r-k)\log B\bigr]\right).
\]

The finite filling sum can be partitioned according to which root
coordinates belong to \(I_\delta\). The same exponential rate bounds
each specified part, including all its mixed derivatives. Thus, if
\[
(r-k)\log B<\Phi,
\]
one can choose \(\delta\) so that the part with at least \(k\) coordinates
near \(+2\) is strictly smaller than the geometric contribution after
sufficiently long fixed fillings. The
[mixed-region proof](proofs/md-fixed-spectrum-mixed-region-bound.md)
gives the constants and the original filling formula.

This removes a union of regions from the remaining problem. Tuples with
fewer than \(k\) coordinates in the interval remain uncontrolled by this
argument.

## A finite transfer reduction for even bipyramids

The second approach preserves the signs and shared face constraints in
a cyclic matrix product. Here the diagram is an opposite-offset
bipyramid with an even equator of size \(m\ge6\). The construction is
specific to that class; it has not yet been extended to all matched
spheres.

A transfer state records two partial face loads \(u,v\), each between
zero and \(d\), together with the current position around the equator.
The matrix \(L\) advances this position by one. Let \(P\) project onto
the states that enforce the local conditions defining \(C_N\), and put
\(Q=I-P\). The new support theorem is
\[
(QLQ)^{3m}=0.
\]
The exponent depends on the diagram and is independent of the quantum
level and the spectral parameters.

The reason is a capacity constraint. A monomial outside the selected
local range has exactly one middle exponent greater than \(h\).
Two such high exponents cannot enter the same ordinary face, whose
target is \(d\). The protected face has target zero and accepts none.
A complete run through the north factors therefore contains a factor
in the selected range. Repeating the run forces more such factors
than a path confined to \(Q\) can accommodate. This proves nilpotence
before evaluating any coefficients.

Writing
\[
L=\begin{pmatrix}A&B_1\\ C_1&D\end{pmatrix}
\]
relative to the \(P\) and \(Q\) spaces, and using a formal variable
\(z\) to count transfer steps, the matrix
\[
z^2B_1(I-zD)^{-1}C_1
=z^2B_1\left(\sum_{j=0}^{3m-1}z^jD^j\right)C_1
\]
records a passage from \(P\) through \(Q\) and back. A Schur complement
expresses the original \(D_N\) as a coefficient of a finite sum of these
passages and the \(P\)-transfer \(A\). The
[transfer proof](proofs/md-shifted-cyclic-excursion-and-clock-reduction.md)
gives the exact formula, phases, and coefficient targets.

The Schur identity itself is general algebra. The additional theorem
is the level-independent nilpotence of this particular projected
transfer. Neither fact bounds the size of its entries. The next analytic
step is to estimate the coupled passages at the geometric exponential
rate, retaining their signs.

The same note records a necessary correction to shifted
integration-by-parts identities: shifted face targets require the
larger range \(0\le u\le2d\), and the common south-face coefficient
must still be extracted. The original nilpotence argument cannot be
reused after changing a face's capacity without checking it again.

## What representation rigidity does give

For one fixed complete hyperbolic knot complement \(X\), boundary-parabolic
representations have only finitely many signed volumes. The volume
bound and its equality case therefore give a strict gap below
\(\operatorname{Vol}(X)\) away from the geometric representation and
its orientation reversal. These geometric facts are established in the
literature. The
[representation note](proofs/md-filled-complement-representation-gap.md)
spells out the finite-type and continuity argument, including trivial
peripheral images, and records the relevant hypotheses.

The primary coverage is
[Garoufalidis–D. Thurston–Zickert, §1 and Theorem 1.8](https://arxiv.org/pdf/1111.2828v2),
[Zickert, Definition 4.3 and Theorem 6.10](https://arxiv.org/pdf/0710.2049v2),
and
[Francaviglia, Theorems 5.1 and 7.2](https://arxiv.org/pdf/math/0305275).
The note distinguishes the signed volume from the real and imaginary
parts of the complex regulator.

The existing full critical-point equations of the original marked
source produce representations of the knot group and the correct
fundamental-class volume. The gap therefore applies to their
nongeometric regular critical points. A maximum obtained by restricting
some local exponents need not satisfy those full equations. This is the
remaining limitation of using representation rigidity directly on
separated parts of the source.

The [half-charge calculation](proofs/md-filled-complement-half-charge-obstruction.md)
makes that limitation concrete. Keeping the exact omitted spectral
factors changes a local Fourier charge from an integer \(\ell\) to
\(\ell\pm\tfrac12\). It does not change the original prefactor, parity
rule, or summation convention. The resulting equation cannot be
identified with the original primitive filling relation merely by
choosing another logarithm branch. No geometric interpretation or
negligibility estimate for these isolated modes is asserted.

## Reproduction and preserved evidence

Run the finite checks from this directory with

~~~sh
python3 reproduce.py
~~~

The continuant check requires NumPy and SymPy; the other two checks use
the standard library. The runner writes to reproduction-output/ and
compares the results with the saved records. It checks local matrix
identities, direct shared coefficient extraction, transfer and Schur
formulas, finite support graphs, shifted targets, and the exact
half-charge products. These finite calculations do not replace the
all-level proofs or prove an asymptotic gap.

The evidence/originals/ directory preserves the original drafts, result
files, and review records. Earlier versions of the representation and
half-charge notes are retained there. The dependencies/ directory
contains the preceding private algebraic notes, and
evidence/public-inputs/ records the exact published dependencies.
The readable copies under proofs/ change only local links.
The manifest records file hashes.

The obstruction examples remain part of the evidence. In particular,
the previously proposed unshifted sewn current does not vanish, and
the remainder at the all-\(-2\) corner is positive at even levels.
The latter has a polynomial lower witness; it does not contradict
the desired exponential gap.

The unresolved task is still quantitative: bound the rest of the
original complementary contribution, either throughout the spectral
cube or directly after the original filling operations. The results
above provide exact objects and some controlled regions for that task.
