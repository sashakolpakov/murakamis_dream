# The complete terminal profile envelope over every real outside color

Research deduction, 6 November 2026. The complete-color terminal
profile envelope is also a valid upper envelope for the literal
terminal polynomial at every real ordinary color. This statement
holds on the whole incoming tube used by that envelope, not only
at an unselected reference height. It transfers the new selected
terminal-window gap to the entire real outside-color period.
No additional scalar or source evaluation is needed.

## 1. A color-independent upper envelope for the original source

Keep the original terminal polynomial
\[
 \mathcal V_{\epsilon,N}(w,X)
 =\sum_{i=0}^{N-1}\frac{X^{-i}(rX;r)_i}{(r;r)_i^{1+\epsilon}}
             \mathcal U_{\epsilon,N}(w,r^i),
 \quad r=e^{-2\pi i/N},\quad X=e^{-2\pi ia},
 \tag{1}
\]
for \(\epsilon=0,1\). Its complete terminal diagonal, Newton
polynomial, ordinary-color normals, support walls and both level
parities remain those of the original source. Put
\[
 \mathcal A=[.22,.45]+i[-.12,.12].
 \tag{2}
\]
Use exactly the 25 regular profiles \(F_{\epsilon,\sigma}\),
the physical entropy profile \(R_\epsilon\), and constant
\(C=879/1000\) from
[the terminal profile envelope](research_mixed_terminal_concave_profile_envelope.md),
equations (2)--(8). The index products are
\[
 \begin{array}{c|c|c}
 &t&\text{private index}\\ \hline
 \epsilon=0&[.15,.5]+i[-.12,.12]&[.1,.4]+i[-.12,.12]\\
 \epsilon=1&[.15,.5]+i[-.12,.12]&[.27,.49]+i[-.055,.04].
 \end{array}
 \tag{3}
\]
Choose the main heights as in that theorem. Real cuts, alias
penalties and unused coordinates keep their original meanings.
All phases defining these profiles are the complete-color phases.
Define
\[
 \mathcal E_\epsilon(a)=
 \max\left\{\frac{879}{1000},\
       \sup_yR_\epsilon(a;y),\
       \max_\sigma\sup_xF_{\epsilon,\sigma}(a;x)\right\}.
 \tag{4}
\]
The suprema retain the full original real index intervals and
closed entropy domains.

**Theorem 1.** For every prescribed \(\eta>0\), there are
constants \(C_\eta,A_\eta,N_\eta\) such that
\[
 \left|\mathcal V_{\epsilon,N}(-2\cos\theta,e^{-2\pi ia})\right|
 \le C_\eta N^{A_\eta}
             e^{N\{\mathcal E_\epsilon(a)+\eta\}},
 \qquad a\in\mathcal A,\quad -\pi\le\theta\le\pi.
 \tag{5}
\]
This is a bound for the unchanged signed polynomial (1). It does
not assert that its value or the modulus of a canceled subsum is
maximal at \(w=-2\). In particular, (5) compares to the profile
envelope, not to \(|\mathcal V_{\epsilon,N}(-2,X)|\).

*Proof: regular currents.* In type three the sole color-dependent
factor in the exact two-index interpolation is the original Newton
interpolant \(\mathcal E_N(u,\theta)\). Equations (2)--(4) of
[endpoint real-color decay](research_mixed_endpoint_real_color_decay.md)
give, on the entire private product in (3),
\[
 |\mathcal E_N(u,\theta)|
 \le C N^A e^{N\{\Re V_0(u)-c_0(1-\cos\theta)\}},
 \quad V_0(u)=-2J(1/2-u)-2J(u),\quad c_0>0.
 \tag{6}
\]
The relevant compact real interval is \([.1,.4]\), strictly
inside \((0,1/2)\), and the index height is at most \(.12\).
The reflected reciprocal factorial retains both exponential terms;
(6) includes moving zeros and both signs of the index height.
Every other density and residue-kernel factor is color independent.

In type four the complete coherent coefficient
\(C_N(e,w)\) is kept before moving either remaining contour.
Theorem 1, equation (6), of the same endpoint note gives
\[
 |C_N(e,-2\cos\theta)|
 \le C N^A e^{N\{\Re S(e)-c_E(1-\cos\theta)\}},
 \quad e\in[.27,.49]+i[-.055,.04],\quad c_E>0.
 \tag{7}
\]
This is the entire finite coefficient, including revived Newton
rows. It is not its leading saddle term. The other factors in the
terminal double interpolation are again color independent.

Insert (6) or (7) before estimating each current of the exact
double-cycle identity. Dropping the favorable angular loss gives
precisely the old complete-color density upper. Apply the same
height-convexity and sign-half kernel inequalities to that upper
function. Thus every horizontal current, ordinary vertical join,
single or double alias, and half-grid cut sliver is bounded by the
same profile appearing in (4). No far-color critical point or
far-color phase concavity is needed. Both the constant residue
coefficients and every side orientation are retained before taking
absolute values.

*Proof: physical complements.* Here the necessary real-color
statements precede any calibrated supporting-plane comparison.
They are supplied explicitly by Sections 2--4 of
[terminal real-color decay](research_mixed_terminal_real_color_decay.md):

* Its Lemma 2 retains the coherent cap seams and the full transform
  end-row ceiling \(217/250<879/1000\), for all
  \(a\in\mathcal A\) and real colors. Each removed outer row
  retains the entire private and Newton sums.
* For type three, physical Newton rows below one half satisfy
  \(V_\theta(u)\le V_0(u)\). The low-Newton and near-half
  positive majorants therefore keep their old ceilings. Above
  one half only \(V_\theta(u)\le0\) is used: equations
  (11)--(13) of that note prove the same uniform ceiling below
  \(.878\), hence the finite ceiling \(.879\). The negative
  complete-color upper-half entropy is not asserted to dominate
  all other colors.
* The remaining type-three physical strips retain the same
  complete-color upper phases. Their original real-index
  monotonicity transports these upper phases to \(t=.15\) or
  the private cuts \(.1,.4\), including their real corners.
  The subsequent regular currents are those already covered
  above. This transports an upper bound, not the derivative of
  a new color-dependent phase.
* For type four, remove the whole small outer-index sector first.
  The exact support then permits deletion of the entire columns
  that vanish for every retained physical outer row. Every
  remaining physical private index has \(e<1-\delta\) for a
  fixed \(\delta>0\). Equation (8) of the terminal real-color
  note gives its whole \(H_N\) upper with the same rate
  \(h(e)\), an arbitrarily small tolerance, and all real
  colors. The original coherent private-tail and left-strip
  upper phases consequently transport to the same real anchors
  \(e=.27,.49\) and \(t=.15\). Within retained columns the
  polynomial \(p_j(e^{-2\pi it})\) stays literal when \(t\)
  moves: its revived off-grid values are not deleted by a
  row-dependent triangular support rule.
* In either right physical triangle the support forces every
  Newton index below one half. The inequality
  \(V_\theta\le V_0\) therefore preserves the positive
  majorant and its original half-period reduction. Its upper
  is exactly the entropy profile in (4), with its full closed
  interval or triangle. The even half row remains included.

These arguments use the domains (2)--(3); they do not use the
unselected target height or the favorable final supporting-plane
gaps in the old real-color theorem. Its contour arguments and
physical inequalities can therefore be used at every target in
(2). Every transported anchor remains an original regular profile,
and every absolute ceiling is bounded by the constant in (4).
Finitely many currents, source rows and tolerance allocations give
(5), with polynomial prefactors. \(\square\)

No common angular loss is assigned to (4). Regular densities before
physical restoration have the losses (6)--(7), but some transported
tails are used only with no-loss upper bounds at real-cut anchors.
The entropy and constant profiles likewise remain unmodified.

## 2. The selected terminal window over the full real period

Use exactly the canonical actual domain \(K_4\), original action
\(M_*\), incoming marginal \(p_*\), and allocated kernel of
[the uniform terminal completion](research_mixed_terminal_uniform_kernel_completion.md).
The incoming leg is unselected, the preceding ordinary factor has
type four, and
\[
 b_R,a_R\in P=[.22,.45],\quad
 \Im b=\Im b_*,\quad \Im a=H=1/100.
 \tag{8}
\]
The two real parts are independent. The complete selected weight
\(d_N(X_a)X_a^{-N}\) and incoming modulus halfweight remain
unchanged. The complete-color reference is used at every outside
color; no new real-color reference action is introduced.

**Corollary 2.** For every fixed \(\eta>0\), uniformly on this
canonical actual family and (8), for both terminal types and both
level parities,
\[
 \begin{split}
 &\left|C_{1,N}(X_b,X_a)
   \mathcal V_{\epsilon,N}(-2\cos\theta,X_a)
                      d_N(X_a)X_a^{-N}\right|\,|d_N(X_b)|^{1/2}\\
 &\qquad\le C N^A
       \exp N\left\{\Re[M_*+p_*(b-b_*)]-\frac1{2600}+\eta\right\},
       \qquad -\pi\le\theta\le\pi,
 \end{split}
 \tag{9}
\]
for all sufficiently large \(N\), with the constants and threshold
allowed to depend on \(\eta\). In particular, choosing
\(0<\eta<1/5200\) gives
\[
 \left|C_{1,N}(X_b,X_a)
   \mathcal V_{\epsilon,N}(-2\cos\theta,X_a)
                 d_N(X_a)X_a^{-N}\right|\,|d_N(X_b)|^{1/2}
 \le C N^A\exp N\left\{
       \Re[M_*+p_*(b-b_*)]-\frac1{5200}\right\}.
 \tag{10}
\]

Indeed the completed ordinary-label reduction and both Fourier
alternatives are color independent. Theorem 1 gives exactly the
same 27 terminal upper profiles at every real color. Every joint
profile comparison in the completion therefore applies unchanged,
with raw gap \(1/2600\). Allocate all finite-source tolerances
within \(\eta\), proving (9). The strict spare tolerance in (10)
also allows polynomial absorption when required by an assembly.
Neither conclusion modifies any source coefficient or asserts its
positivity.

Every fixed ordinary-color derivative obeys (9) and (10) with a larger
polynomial prefactor. Apply the degree-\((N-1)\) Laurent maximum
principle to the original holomorphic integer-weighted source,
then Cauchy's formula on ordinary-color circles of radius
\(N^{-2}\). The inverse-angle height is \(O(N^{-1})\), uniformly
also at the two ramification points, so the added exponential
factor is bounded independently of \(N\). Allocate the
color-independent modulus halfweight only after differentiation.

## 3. What this propagates and what remains

The right outside color occurs only in the literal terminal
factor. Any exact assembly in which the other factors and contours
are independent of that color may consequently carry (9) or (10) through
its original sums and integrals, retaining the same incoming
complex affine marginal and halfweight. The available calibrated
bound for that remaining contraction still has to be proved and
matched; replacing it by a norm ceiling is not part of this result.

In particular the present deduction removes the need for a new
real-period color test for this selected terminal window. It does
not cover a selected incoming leg, type-three incoming references,
length-two endpoint compositions, or target coordinates outside
the specified outer plateau. It does not control the nonplateau
part of an arbitrary mixed word or all other boundary selections.

The exact whole-source obligation remains the complement estimates
(9) and (3) of
[open-source stability](research_mixed_open_source_stability_reduction.md):
a local exponentially small remainder on a fixed complex color
neighborhood and a calibrated real outside-period gap for the
entire original polynomial. The localized Fourier energy criterion
still needs its exterior energy bound for that entire polynomial;
the local window estimate is not such an energy bound. No
nonzero whole-word coefficient, short-filling stability theorem or
new knot-family theorem is asserted here.
