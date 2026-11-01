# Appendix N: exact functional audit and a formalization skeleton

This is a read-only proof audit of the public manuscript at commit
c5d9c851c672b941bdbbec51da50d8f1a5c2cf12. It covers
manuscript/sections/N-uniform-filling-bound.tex and the literal finite
source dependencies listed below. No public source was edited. No
Appendix N reproduction program was run for this read. The separate
new coupled-moment checker was executed, but is not evidence for any
input of Appendix N.

## 1. Findings and exact scope

I found no mathematical defect in the scalar functional inequalities,
their two parity cases, their tensor extensions, or the stated
conditional transfer to a volume limit.

The proof is not a proof of a geometric estimate for the complementary
source. That missing premise remains explicit at lines 338–341,
label uf:eq-26. The nonzero central asymptotic and strict comparison of
its rate remain separate premises at lines 352–357, uf:eq-28.
Geometric identification is separately required at lines 362–365.
There is no promotion of node vanishing or a finite reproduction into
one of those premises.

For the actual invariant, the appendix imports the all-level local
matrix/face adapter and the original marked coefficient identity. The
norm proof alone does not establish them. The division is explicit in
lines 71–120, especially uf:eq-5 through uf:eq-7. I read the relevant
source derivations rather than using their finite-check reports.

One minor source-text precision lies outside this manuscript file:
notes/actual_uniform_filling_supremum_bound.md, lines 33–39, states the
joint-grid bound without repeating that the new polynomial has degree
at most \(N-1\) in every coordinate. The preceding source context may
suggest it, but the standalone formulation needs this hypothesis.
The manuscript already states it explicitly at lines 50–54.
No manuscript correction is needed for that issue.

## 2. Repeated roots and the exact operator functional

The relevant manuscript locations are lines 125–159, uf:eq-8 through
uf:eq-12. Let
\[
 \chi(z)=2T_N(z/2)+2,\qquad d=N-1.
\]
There are \(\lfloor N/2\rfloor\) distinct double roots
\(c_a=2\cos((2a+1)\pi/N)\), indexed by
\(0\le a<\lfloor N/2\rfloor\). At odd level there is one additional
simple root \(-2\). This is exactly \(N\) roots counted with
multiplicity. The full grid of \(N\) odd angles counts each double
root twice and the odd simple root once.

Writing \(h(z)=\chi(z)/(z-c)^2\), the Chebyshev equation and its
derivative give
\[
 h(c)=\frac{N^2}{4-c^2},\qquad
 \frac{h'(c)}{h(c)}=\frac{c}{4-c^2}.
\]
The derivative computation uses
\(\chi''(c)=2h(c)\) and \(\chi'''(c)=6h'(c)\); there is no missing
factor of two or three. For odd \(N\), \(\chi'(-2)=N^2\).

For \(\chi(\Omega)=0\), the local principal resolvent terms are
\(P_c/(z-c)+Q_c/(z-c)^2\). Thus
\[
 V(c)=h(c)Q_c,\qquad
 V'(c)=h(c)P_c+h'(c)Q_c .
\]
Solving these equations and substituting into
\(f(c)P_c+f'(c)Q_c\) proves exactly uf:eq-10, including its
nilpotent term. At the odd simple root the remaining term is
\(f(-2)V(-2)/N^2\).

An especially useful route for formalization avoids resolvent
notation altogether. Work in the finite algebra
\(\mathbb C[w]/(\chi(w))\). Let \(F\) be the unique degree-\(<N\)
polynomial with the prescribed values and first derivatives at the
double roots, and the prescribed value at the odd simple root.
Define
\[
 \tau(P)=[z^{N-1}]\,\operatorname{rem}_{\chi(z)}P,\qquad
 V(z,w)=\frac{\chi(z)-\chi(w)}{z-w},\qquad
 \mathcal L^f(H)=\tau(FH).
 \tag{A}
\]
The two-variable quotient defining \(V\) is a polynomial. Since
\[
 (F(z)-F(w))V(z,w)
       =\chi(z)\frac{F(z)-F(w)}{z-w}
       \quad\text{modulo }\chi(w),
 \tag{B}
\]
and \(V\) is monic of degree \(N-1\) in \(z\), reduction modulo
\(\chi(z)\) gives
\[
                    \mathcal L^f(V)=F(w).
 \tag{C}
\]
The partial-fraction coefficient of \(z^{-1}\) in \(FH/\chi\), or
equivalently polynomial Chinese remaindering, gives uf:eq-10 from
(A). This is a finite algebra identity and is valid even when
\(\Omega\) is not semisimple. Evaluation at the actual \(\Omega\)
then gives \(f(\Omega)\).

The angular check is also exact. Differentiating
\(2\sin\phi\,f(2\cos\phi)H(2\cos\phi)/N^2\), with the prefactor
\(-1/2\), gives half the double-root expression at each of its two
angles. At the single odd angle \(\phi=\pi\), the sine term
vanishes and the differentiated cosine contributes
\(f(-2)H(-2)/N^2\). This verifies the signs and multiplicities in
uf:eq-12 without discarding a derivative.

## 3. Actual signed crossing powers and the scalar norm

Manuscript lines 161–181, uf:eq-13 through uf:eq-15, use the actual
fixed-root Gaussian, not a Gaussian reconstructed from values alone.
The required source input is
notes/actual_direct_long_power_source.md, lines 127–152.
Its paired-node data are the original crossing value and logarithmic
derivative, lines 70–78:
\[
 r_N(c_a)=(-1)^a q^{a(a+1)},\qquad
 \frac{r_N'(c_a)}{r_N(c_a)}
  =-\frac{N-(2a+1)}{2(q^{2a+1}-q^{-2a-1})}.
 \tag{D}
\]
The displayed Gaussian matches both entries in (D), after retaining
the scalar \(q^{nd^2/2}\). Raising unit values to negative integral
powers multiplies the logarithmic derivative by the same signed
integer \(n\), so the argument covers all \(n\in\mathbb Z\).
For \(n=0\), it gives the identity functional.

At the odd simple root, symmetry about \(\phi=\pi\) makes the
Gaussian analytic in \(z+2\); only its value is used. The branch
endpoint \(z=2\) is not a spectral node. The finite norm argument
requires only its bounded angular values and derivative, not
holomorphic extension across that endpoint.

The finite Riesz formula at manuscript lines 187–209,
uf:eq-16 through uf:eq-19, acts on
\(P(\phi)=H(2\cos\phi)\), which has trigonometric degree at most \(d\).
It is not applied to the nonpolynomial Gaussian times \(P\).
Checking the Fourier modes \(-d+1,\ldots,d\), and then the aliased
mode \(-d\), proves the identity at every degree. The sum of the
absolute weights is exactly \(d\), so complex coefficients cause no
problem. This supplies a direct finite proof of
\(\|P'\|_\infty\le d\|P\|_\infty\).

In uf:eq-15 the evaluation coefficient is bounded by
\(1+|n|N/2\), the coefficient of \(P'\) by one, and there are exactly
\(N\) terms with common factor \(N^{-2}\). This gives
\[
 \frac1N+\frac{|n|}{2}+\frac dN=1+\frac{|n|}{2}.
 \tag{E}
\]
If all node values of \(H\) vanish, the entire evaluation term
vanishes, including the derivative of the crossing phase; the
remaining \(P'\) term gives \(d/N\). It does not vanish in general.
These are uf:eq-1 and uf:eq-2, proved at lines 220–231.

## 4. One-sided support and the unsplit tensor cancellation

For actual source use, manuscript lines 233–255 and 277–287 import
the one-sided divisibility of the original central-cut decomposition.
The relevant cutoff is the input row
\[
               0\le j\le \lfloor N/2\rfloor-1 .
 \tag{F}
\]
The original face operator lowers polynomial degree. Its restriction
to this block is triangular with the distinct diagonal entries
\(c_0,\ldots,c_{\lfloor N/2\rfloor-1}\), and is therefore
annihilated by
\(D_-(z)=\prod_a(z-c_a)\). Multiplying its block resolvent by
\(\chi(z)\) leaves the polynomial factor
\[
 \chi(z)/D_-(z)=
 \begin{cases}
  D_-(z),&N\text{ even},\\
  (z+2)D_-(z),&N\text{ odd}.
 \end{cases}
 \tag{G}
\]
The reflected upper block has the same spectrum. At odd level the
central row is excluded from both one-sided pieces and retained in
the central piece. Thus both one-sided polynomials vanish at every
full spectral node, including the odd simple node. This is value
vanishing only; it does not discard their first normal data.

For the tensor estimate, let the polynomial have multidegree at most
\(d\). In each coordinate write uf:eq-15 as an evaluation operator
plus a numerator-derivative operator. Iterated Riesz interpolation
bounds every mixed angular derivative by \(d^{|A|}\) times the
original cube supremum. The coefficient cost for the differentiated
coordinate is \(d/N\); for an evaluation coordinate it is
\[
                         b_e=1/N+|n_e|/2.
 \tag{H}
\]
If the polynomial vanishes only on the product node grid, then
only the term with no differentiated variables is forced to vanish.
It vanishes pointwise before any grid summation. Adding all other
subsets gives
\[
 \sum_{\varnothing\ne A\subseteq\{1,\ldots,r\}}
       \prod_{e\in A}\frac dN\prod_{e\notin A}b_e
   =\prod_e(1+|n_e|/2)-\prod_e b_e .
 \tag{I}
\]
This proves uf:eq-4 at lines 265–275. It does not assume vanishing
on coordinate hyperplanes and does not infer vanishing of mixed
derivatives at the grid.

When a coordinate hyperplane does vanish identically for all other
variables, the finite functionals in those other variables preserve
that property, including their derivative terms. This separately
justifies iteration of the stronger estimate in uf:eq-3.

Finally, (G) gives local polynomial equality
\(H_V(c)=H_C(c)\), with all four face variables still formal.
Products of these equalities, followed by the single original shared
coefficient extraction, prove uf:eq-25 for the full-minus-central
source. No absolute decomposition into local source terms occurs.
Its spectral multidegree is at most \(d\), since each spectral
variable occurs at only its own coupon before extraction.

## 5. Exact source normalization: the additional adapter

The necessary all-level input for uf:eq-6 and uf:eq-7 is the local
homogeneous adapter followed by the original marked Morse compiler.
I checked these specific steps:

* notes/actual_homogeneous_casimir_face_source.md, lines 55–86:
  the inverse finite Fourier transform of the literal Casimir step
  words gives the \(N^{-1}\) local polynomial factor. Wrong
  unwrapped physical totals have zero coefficient before a modular
  face-grid interpretation.
* The same note, lines 99–168: coherent lifted face potentials and
  original cup, cap and mark entries cancel the half-index factors.
  Whole-source conservation, rather than an early truncation of
  the mark, forces its two surviving heads to be complementary.
* notes/research_matched_sphere_morse_source.md, lines 177–248:
  the face turning identity is proved on the actual spherical Morse
  diagram; it is not transported from a presumed flat plat.
  The summand has factor \(N^{-R-1}\); its \(R+1\) primitive face
  grids cancel this exactly.
* The homogeneous total face degree is \(dR\). The \(R\) ordinary
  targets have minimum nonnegative residue representative \(d\);
  they already exhaust that degree. Thus there is only the
  prescribed alias, both protected exponents are zero, and the
  even-level coset character is one at that target.
* The Morse note, lines 250–307: insertion of the independent
  signed local matrix functionals is justified by multilinearity
  of the ordered contraction. Neighboring Casimirs need not
  commute. The reduced ribbon scalar and the specified
  zero-framed/enhanced or full one-cut conventions remain
  distinguished.

Thus the absence of an extra \(N^R\) in uf:eq-7 is supported by the
actual source proof. It is not a consequence of the scalar norm
inequality. The abstract scalar theorem applies at \(N\ge2\);
the physical compiler is explicitly invoked at \(N\ge3\).

## 6. Dependency skeleton for formalization

The following modules separate finite algebra, elementary analysis,
and the diagram adapter. Each arrow below means a theorem dependency,
not a finite numerical test.

1. **Chebyshev polynomial and roots.** Define \(T_N\), prove its
   recurrence, factorization of \(\chi\), root multiplicities,
   derivative identities, and odd-angle grid multiplicities.
2. **Finite quotient and coefficient trace.** Define
   \(\mathbb C[z]/(\chi)\), the top-coefficient functional \(\tau\),
   Hermite interpolation by the Chinese remainder theorem, and
   prove (A)–(C). This proves the full resolvent functional without
   assuming a diagonalizable Casimir.
3. **Actual crossing jets.** From the literal signed braid/Casimir
   matrices prove their value and first-derivative data (D),
   including the scalar lift and the odd simple value. Match these
   jets with the displayed Gaussian. This module is independent
   of global topology.
4. **Midpoint functional.** Combine modules 1–3 and the elementary
   chain rule to obtain uf:eq-12 and uf:eq-15.
5. **Finite trigonometric interpolation.** Prove Riesz interpolation
   on a basis of Fourier monomials, sum its absolute weights by the
   sine product, and extend to finite-dimensional normed spaces.
6. **One-variable functional bound.** Combine modules 4–5 with
   the two Gaussian modulus estimates; prove (E), the
   vanishing-value variant, and uf:eq-1/uf:eq-2.
7. **Multivariable polynomial norm.** Prove preservation of
   hyperplane vanishing, mixed derivative bounds, and the
   nonempty-subset identity (I). This proves uf:eq-3/uf:eq-4 for
   arbitrary polynomials of the stated multidegree.
8. **Actual source adapter.** Define the ordered physical tensors,
   homogeneous face kernel, mark and target; prove the local
   Fourier identity, true support, face winding, primitive grid,
   parity coset and total-degree alias exclusion. This proves
   uf:eq-6/uf:eq-7 independently of source positivity.
9. **Actual central-cut support.** Prove the triangular block
   restriction (F), factor (G), reflected block, and odd central
   row assignment. Then local node equality and module 8 prove
   uf:eq-25.
10. **Conditional rate transfer.** For a fixed diagram and fixed
    signed powers, modules 7–9 turn uf:eq-26 into uf:eq-27.
    Given the separate nonzero asymptotic uf:eq-28 with its strict
    real-action inequality, the reverse triangle inequality proves
    uf:eq-29. Geometric identification is a further theorem,
    not an output of modules 1–9.

Modules 1,2,3,5,8,9 contain finite sums or polynomial identities well
suited to formal algebra. Modules 4–7 require only elementary
differentiation and norm inequalities. Module 10 uses a genuine
asymptotic premise. None is certified for all levels merely because
the reproduction checks finitely many cases. This audit supplies a
proof dependency plan, not a machine-checked formal proof.
