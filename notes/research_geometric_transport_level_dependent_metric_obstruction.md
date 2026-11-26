# A fixed geometric loop forces exponential transport cost in every positive metric

Private written proof, 17 November 2026. No mathematical programs,
tests or numerical evidence are used. Frozen notes are unchanged.

The earlier coherent gluing note excludes exactly nonexpansive
positive metrics around a nontrivial parabolic loop. A single
parabolic can nevertheless approach norm one in degenerating metrics.
Two distinct parabolic flags give the stronger conclusion below:
even arbitrary level-dependent positive metrics on the full
symmetric-power fibers cannot make all geometric transports cost
\(\exp(o(N))\). This tests a geometric frame strategy, not a quantum
crossing identity or a volume theorem.

## 1. A fixed loxodromic word from complete cusp holonomy

Let \(\Gamma<\mathrm{PSL}_2(\mathbb C)\) be discrete, torsion-free
and of finite hyperbolic covolume, and suppose it contains a nontrivial
parabolic \(P\). These hypotheses apply to the complete holonomy of a
hyperbolic knot complement. Some conjugate of \(P\) has a different
fixed flag.

Indeed, put the flag of \(P\) at infinity. If every conjugate fixed
infinity, then \(gPg^{-1}\) has flag \(g\infty=\infty\) for every
\(g\in\Gamma\). Thus all of \(\Gamma\) fixes infinity and acts on the
boundary by \(z\mapsto az+b\). Write \(P(z)=z+c\), \(c\ne0\).
If \(|a|\ne1\), conjugation by positive or negative powers of \(g\)
produces nonidentity translations with lengths tending to zero,
contrary to discreteness. If \(|a|=1\) and \(a\ne1\), translate its
other fixed point to zero. The map becomes \(z\mapsto az\):
it has finite order when \(a\) is a root of unity, contradicting
torsion-freeness, and otherwise a sequence of powers tends to the
identity, contradicting discreteness. Hence every \(g\) is a
translation.

A discrete translation subgroup has rank at most two. Its horizontal
quotient has infinite area in rank at most one and positive finite
area in rank two. The needed volume contradiction can also be seen
without this lattice classification: discreteness supplies a
Euclidean disk \(B\), of area \(A>0\), whose distinct translates are
disjoint. The image of \(B\times(0,1)\) in the quotient is injective
and has upper-half-space volume
\[
                    A\int_0^1 h^{-3}\,dh=\infty.       \tag{1}
\]
In either case the hyperbolic quotient has infinite volume, a
contradiction.

Send the two distinct flags to infinity and zero and choose
trace-two lifts of the two parabolics. They have the form
\[
 P=\begin{pmatrix}1&a\\0&1\end{pmatrix},\qquad
 Q=\begin{pmatrix}1&0\\b&1\end{pmatrix},\qquad ab\ne0.
                                                               \tag{2}
\]
Choose a fixed positive integer \(n\) with \(n|ab|>4\), and set
\[
 L=P^nQ,\qquad \operatorname{tr}L=2+nab,\qquad
                       |\operatorname{tr}L|>2.        \tag{3}
\]
Since \(\det L=1\), its eigenvalues are \(\lambda,\lambda^{-1}\).
They cannot both have modulus one, since that would give
\(|\operatorname{tr}L|\le2\). Choose \(|\lambda|>1\), and put
\(\gamma=\log|\lambda|>0\). Thus the projective word is
loxodromic. Changing either lift or the lift of the resulting
word changes only central signs, which do not change \(\gamma\).
This argument also applies to any representation already supplied
with two such distinct-flag parabolics, without discreteness or
a finite-volume assumption.

## 2. Arbitrary positive metrics at every level

Realize this fixed geometric word by a closed transport path of
\(\ell\) oriented edge occurrences. Let its determinant-one geometric
transport matrices be \(g_1,\ldots,g_\ell\), with ordered product
conjugate to \(L\) or \(-L\). The same statement holds for any fixed
path with such holonomy. Use the actual matrices, with their allowed
central signs; arbitrary scalar renormalizations are not permitted.

For every integer \(N\ge2\), put
\[
 V_{v,N}=\operatorname{Sym}^{N-1}\mathbb C^2,\qquad
 G_{j,N}=\operatorname{Sym}^{N-1}g_j.
                                                               \tag{4}
\]
Assign any positive definite Hermitian form \(H_{v,N}\) to each
visited fiber, with the returning form equal to the initial form.
The forms may depend arbitrarily on \(N\), may be arbitrarily
ill-conditioned, and need not be induced from two-dimensional forms.
Even independent forms at repeated intermediate visits are allowed.
Denote the corresponding operator norm of \(G_{j,N}\) by \(b_{j,N}\).

**Theorem.** For every such choice, at every level,
\[
 \prod_{j=1}^{\ell}b_{j,N}\ \ge
       \rho\bigl(\operatorname{Sym}^{N-1}L\bigr)
       =e^{(N-1)\gamma}.                                \tag{5}
\]
Consequently
\[
       \max_{1\le j\le\ell}\frac{\log b_{j,N}}{N-1}
                           \ge\frac{\gamma}{\ell}>0.     \tag{6}
\]
In particular one fixed edge occurrence has, along an infinite
subsequence of levels, logarithmic norm divided by \(N\) at least
\(\gamma/\ell-o(1)\). There is no choice of these metrics making
every transport on the fixed path have an upper bound \(\exp(o(N))\).

**Proof.** Submultiplicativity of operator norms between the
successive metric spaces bounds the loop norm by the left side
of (5). The returning metric is the initial metric, so this loop
norm is at least its spectral radius: apply it to an eigenvector.
The symmetric-power eigenvalues are
\(\lambda^{N-1-2j}\), \(0\le j<N\), up to a common sign.
Their largest modulus is \(|\lambda|^{N-1}\), proving (5).
Equation (6) and the infinite pigeonhole principle prove the
remaining assertions. No metric comparison constants enter.

Fixed changes of geometric frames merely conjugate the loop;
arbitrary level-dependent changes of head bases can likewise be
absorbed into the allowed forms. They do not change (5).
This concerns norms of actual flat transports. It does not assign
a norm to an independently rescaled transport with different
closed holonomy.

## 3. Every finite cover retains the obstruction

Let \(\Gamma'\le\Gamma\) have finite index \(d\), without a
normality assumption. Right multiplication by the projective
word \(L\) permutes the \(d\) right cosets \(\Gamma'\backslash\Gamma\).
The orbit of the base coset has some length \(1\le k\le d\);
hence \(L^k\in\Gamma'\). The repeated original path lifts to a
closed path of \(k\ell\) edge occurrences in this cover, with
spectral radius \(|\lambda|^k\). Thus (5) on the lifted path is
\[
        \prod_{j=1}^{k\ell}\widetilde b_{j,N}
                              \ge e^{k(N-1)\gamma}.      \tag{7}
\]
Using this literal repeated path, the lower rate per edge in
(6) remains \(\gamma/\ell\). Neither normality of the cover nor
its being a knot complement is required.

## 4. Exact scope for the original source

The direct coherent sources identify symmetric powers as geometric
frame changes and record their exact cancellation inside the full
finite tensor contraction. They do not identify a quantum crossing
or turn with \(\operatorname{Sym}^{N-1}\) of a meridian transport.
No such identity is used or asserted here.

The new obstruction is to making those flat geometric frame
transports simultaneously subexponential by allowing the positive
metrics to vary with the level, even after a finite cover. It does
not exclude cancellation of frame factors in the original scalar.
Nor does it exclude a negative assembled phase Hessian on an adapted
contour: the local phase inequalities in the gluing source need
not arise from flat transport of positive metrics. A nonflat
choice of Hessian gauges is outside (5). The original source's
geometric coefficient, exterior currents and volume asymptotic
remain undecided by this norm obstruction.

## Direct written source versions

Both complete direct texts were read at the following pins.
They supply the preceding coherent-frame context and the precise
scope being strengthened; Sections 1--3 above are proved directly.

| Source | SHA-256 | Direct use |
| --- | --- | --- |
| research_actual_coherent_polarization_transport.md | 10423fbb5c38b162a68173c1aa3fd2ec7af0f0433878b77390cb7b659e8db2af | Exact adapted coherent spheres, symmetric-power frame changes and their cancellation; Sections 3--5. |
| research_actual_coherent_gluing_hessian.md | 86fdd6c3bcb1eabefd733b24e63fcc8c62b1fb5411e73239f9b4ab9caefcb217 | Local phase versus metric distinction and prior single-parabolic obstruction; Sections 4--6. |
