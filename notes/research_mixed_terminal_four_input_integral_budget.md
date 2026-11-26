# Whole-disk terminal main budgets from correlated height integrals

Research deduction and fixed evaluation protocol, 6 November 2026.
The two canonical families on the whole type-four input disk are now
enclosed by saved affine functions and certified posterior errors.
This note turns those enclosures into four uniform main-profile scalar
tests. It keeps the common complex parameter when forming every
height-shifted argument, cancels all first-order action terms before
enclosure, and uses the larger symmetric pair costs. It needs no new
root, parameter subdivision, private action or dilogarithm evaluation.
The four scalar signs have not yet been evaluated.

## 1. Reference data and the exact normalized height integrals

The outside flag is \(\beta=1\); the terminal flag is
\(\epsilon=0,1\). The parameter domain is the entire closed disk
\[
 |b-b_0|\le r,\qquad b_0=.30-.052i,\quad r=8/125.
 \tag{1}
\]
Use the original canonical family and exact saved data from
[the complete affine-family theorem](research_mixed_terminal_all_input_affine_enclosures.md)
and its
[posterior record](../repro/results/research-mixed-terminal-split-taylor-completion.json),
SHA256 e04521450e1973658cbd602aa0a8f54d4c7d40c968b4b90d65374d570981c617.
For each of the coordinates \(q_i\in\{s,a,t\}\), these give
\[
 q_i=q_i^0+u_i\delta+\zeta_i,\qquad
 |\delta|\le r,\quad |\zeta_i|\le\eta_i,\quad \delta=b-b_0.
 \tag{2}
\]
Select exactly its two entries with \(\beta=1\), one for each
\(\epsilon\), in `posterior_enclosures`. The fields `center_exact`,
`response_exact`, and `posterior_radii_rational` give
\(q^0,u,\eta\) in the original order \((e,\xi,t,a,s)\).
The exact rational \(\eta_i\) come from the error-cost posterior
bound on the multiplier-one certified tube. They are not new
proposal radii or a claim of a smaller contraction tube. The
enclosures (2) hold simultaneously for every parameter in (1).
Every original height, coordinate, regularity and
optimizer-localization premise is checked from these saved images.

Put \(a=A+ic\), fix \(H=1/100\), and write
\[
 \Delta=H-c>0,\qquad
 a_\theta=A+i\{(1-\theta)c+\theta H\},\qquad 0\le\theta\le1.
 \tag{3}
\]
Define \(z_a=a_\theta,\ z_s=s+a_\theta,\ z_t=t+a_\theta\), and
\[
 C_j(\theta)=\Re\cot(\pi z_j),\qquad
 I_j(\theta)=\Im\cot(\pi z_j),\qquad j=a,s,t.
 \tag{4}
\]
The original lifted trial and its three nonzero real forces satisfy
\[
 \begin{split}
 W&=\pi\Delta^2\int_0^1(1-\theta)(3C_a-C_s-C_t)\,d\theta,\\
 A_s&=\pi\Delta\int_0^1(1-I_s)\,d\theta,\\
 A_t&=-\pi\Delta\int_0^1(1+I_t)\,d\theta,\\
 A_{a,1}&=\pi\Delta\int_0^1(3I_a-I_s-I_t-1)\,d\theta,\\
 A_{a,0}&=A_{a,1}+\Re g'(A+iH),\\
 T_1&=W-2\pi H,\qquad T_0=W+\Re g(A+iH).
 \end{split}
 \tag{5}
\]
These follow by integrating \(g''=\pi\cot(\pi z)-i\pi\) in
the exact formulas (16) of
[one-parameter transport](research_mixed_terminal_one_parameter_transport.md).
The original shared-leg equation cancels the first-order action
term. The original terminal chirp is the extra \(-2\pi\Delta\)
in \(A_t\), producing \(1+I_t\) in (5). Thus the factorial
trial cost begins at \(\Delta^2\), before any interval arithmetic.

Equations (5) define regular scalar functions on containing reference
boxes. Their identification with the literal lifted value and forces
uses stationarity only at the actual canonical reference. No
off-stationary box center is declared to solve an original equation.
The private action and incoming boundary response do not occur in (5).
The original incoming affine tangent is nevertheless retained: it is
why the omitted incoming horizontal force is exactly zero.

## 2. Sharp argument rectangles with the shared parameter retained

The following support formulas use only (2). Write
\(q_i^0=x_i^0+ih_i^0\), with \(a^0=A^0+ic^0\).
For \(j=s,t\), the real part of \(z_j\) lies in
\[
 x_j^0+A^0\ \pm\
       \{r|u_j+u_a|+\eta_j+\eta_a\}.
 \tag{6}
\]
The sum \(u_j+u_a\) is formed exactly before its modulus is bounded.
For a fixed \(\theta\), its imaginary part lies between
\[
 h_j^0+(1-\theta)c^0+\theta H
       \ \pm\ \{r|u_j+(1-\theta)u_a|
                        +\eta_j+(1-\theta)\eta_a\}.
 \tag{7}
\]
For \(z_a\), the real interval is
\(A^0\pm(r|u_a|+\eta_a)\), and the imaginary interval is
\[
 (1-\theta)c^0+\theta H
                 \ \pm\ (1-\theta)(r|u_a|+\eta_a).
 \tag{8}
\]
These formulas follow by taking real and imaginary parts of the
same complex linear form in \(\delta\). They do not replace that
single parameter by independent perturbations of \(s,a,t\).

For a closed height slab \([\ell,u]\), evaluating both signs of
(7) at its two endpoints encloses the entire slab: its upper
endpoint function is convex in \(\theta\), because the modulus of
an affine complex function is convex; its lower endpoint function is
concave. Their maximum and minimum therefore occur at slab endpoints.
Equation (8) is affine in \(\theta\), so has the same property.
All moduli here are square roots of exact nonnegative rational
numbers and may be enclosed by integer-square-root bounds.

This correlation can materially improve the argument ranges. For
example the \(t+a_\theta\) real width uses \(r|u_t+u_a|\),
not \(r(|u_t|+|u_a|)\). The proof uses the former expression even
though the eventual cotangent enclosure is rectangular.

## 3. A finite interval integral, with no quadrature remainder

Use precisely the sixteen slabs
\[
 J_j=[j/16,(j+1)/16],\qquad j=0,\ldots,15.
 \tag{9}
\]
On each slab construct the three full rectangles from (6)--(8),
check \(0<\Re z<1\), and enclose their original cotangents.
Let \(\mathcal C_{ij},\mathcal I_{ij}\) be outward real
intervals containing (4) throughout the slab and the entire disk.
Set
\[
 \lambda_j=\frac1{16},\qquad
 \omega_j=\int_{j/16}^{(j+1)/16}(1-\theta)\,d\theta
                         =\frac{31-2j}{512}.
 \tag{10}
\]
Then \(\sum_j\lambda_j=1\) and \(\sum_j\omega_j=1/2\).
An interval enclosure of the normalized four integrals in (5) is
\[
 \begin{split}
 \mathcal V&=\sum_j\omega_j(3\mathcal C_{aj}
                                  -\mathcal C_{sj}-\mathcal C_{tj}),\\
 \mathcal S&=\sum_j\lambda_j(1-\mathcal I_{sj}),\\
 \mathcal T&=-\sum_j\lambda_j(1+\mathcal I_{tj}),\\
 \mathcal A&=\sum_j\lambda_j(3\mathcal I_{aj}
                                  -\mathcal I_{sj}-\mathcal I_{tj}-1).
 \end{split}
 \tag{11}
\]
Multiply by the saved enclosing interval for \(\pi\Delta^2\)
or \(\pi\Delta\) as appropriate. These are integral range
inclusions on whole slabs, not a midpoint quadrature approximation;
there is no omitted quadrature error. Dependence lost in the final
interval products can widen a bound, but cannot improve it falsely.

The two forced additions need only elementary scalar functions.
Writing \(R=e^{2\pi H}\),
\[
 \Re g'(A+iH)=\frac12
       \log\{1+R^2-2R\cos(2\pi A)\}.
 \tag{12}
\]
For a value upper bound, the positive original argument of
\(g'(A+ik)\) on \(0<A<.5,\ k\ge0\) gives
\(\Re g(A+iH)\le J(A)\). The function
\(\log(2\sin\pi x)\) is concave on \((0,1)\). Therefore
\[
 J(A)=-\int_A^{1/2}\log(2\sin\pi x)\,dx
 \le-\frac{1/2-A}{2}
            \{\log(2\sin\pi A)+\log2\}.
 \tag{13}
\]
If \(A\in[A_-,A_+]\subset(1/6,.5)\), then
\(J'(A)=\log(2\sin\pi A)>0\). Consequently a uniform upper
bound is the right side of (13) evaluated at \(A_+\), with its
positive logarithmic bracket enclosed from below. This follows from
\(J(A)\le J(A_+)\), and does not assume monotonicity of the
trapezoid expression itself. No dilogarithm or private primitive is
required.

## 4. Uniform cubic gains when the reference center is an interval

Use the stronger allocation from
[symmetric pair costs](research_mixed_terminal_symmetric_pair_costs.md).
Both alternatives keep their full real selected target interval \(P\)
in this protocol. The three target intervals and cubic coefficients are
\[
 \begin{array}{c|c|c}
 \text{node}&I=[L,R]&K\\ \hline
 s&[.22,.5]&88/5\\
 a&[.22,.45]&(\nu+1)49/5\\
 t&[.22,.4]&(3+\epsilon)22/5 .
 \end{array}
 \tag{14}
\]
The saved images must verify \(|h_s|,|h_t|\le.108\), all reference
real centers inside these intervals, and the original endpoint
private-height hypotheses. The full-input ordinary barrier applies
to the external heights in (1). The terminal localization supplies
the stated \(t\)-interval for both branches.

Here is an explicit safe gain enclosure requiring no optimization
over moving roots or reference parameters. Suppose
\(x_*\in[c_-,c_+]\subset I\subset[.18,.5]\) and
the force belongs to \([q_-,q_+]\). Put
\[
 d=.5-c_+>0,\quad
 p=\max(0,-q_-),\quad q=\max(0,q_+),\quad
 U_-=c_+-L,\quad U_+=R-c_- .
 \tag{15}
\]
For a negative displacement \(-v\), its gain is bounded above by
\[
 p v-Kd v^2/2-Kv^3/6,\qquad 0\le v\le U_-.
 \tag{16}
\]
Its maximum is at
\(\operatorname{clip}(\sqrt{d^2+2p/K}-d,0,U_-)\).
For a nonnegative displacement \(v\le d\), an upper polynomial is
\[
 qv-Kd v^2/2+Kv^3/6,\qquad 0\le v\le\min(U_+,d).
 \tag{17}
\]
It is concave there. If \(q\ge Kd^2/2\), its maximum is at
the right endpoint. Otherwise it is at the clipped point
\(d-\sqrt{d^2-2q/K}\).

When \(U_+>d\), the remaining displacements satisfy
the actual \(.5-x_*\ge v\), since the target is at most \(.5\).
Their gain is therefore bounded by
\[
 qv-Kv^3/3,\qquad d\le v\le U_+,
 \tag{18}
\]
whose maximum is at the projection of \(\sqrt{q/K}\) onto that
interval. Take the maximum of (16), (17), and, when present, (18).
It bounds the original cubic conjugate for every admissible force
and reference center. It is deliberately at least zero, because
the center belongs to the full target interval in this protocol.
No such zero truncation is authorized for a different protocol with
the forced target restricted to an interval excluding its center.

All quantities in (15)--(18), except square roots, are exact rational
endpoints after the interval integrals have been serialized.
Outward dyadic square-root bounds, monotone clipping, and rational
polynomial interval evaluation enclose the stated maxima. No formal
square root with a negative radicand is evaluated; the branch
condition in (17) is an exact rational comparison.

## 5. Four whole-disk tests and the bounded protocol

For each \(\epsilon=0,1\), enclose (5) by (6)--(13), then use
the gain upper bounds from Section 4. Let the resulting rational
upper bounds be \(W^+,G_H^+\), and \(G_s^+,G_{a,\nu}^+,G_t^+\).
The four sufficient inequalities are
\[
 \begin{split}
 B_{\epsilon,1}
   &=W^+-2\pi_{\rm lower}H+
                   G_s^++G_{a,1}^++G_t^+<0,\\
 B_{\epsilon,0}
   &=W^++G_H^++G_s^++G_{a,0}^++G_t^+<0.
 \end{split}
 \tag{19}
\]
Each bounds the supremum of the same original defect, at every
parameter in the entire disk and every original main target.
This is a direct all-domain comparison, so no boundary compensation
is needed. If all four tests pass, their exact smallest margin is a
uniform main-profile gap. If any fails or is arithmetically
inconclusive, no whole-disk sign is inferred from this protocol.

The prescribed first evaluation uses 256-bit outward interval
arithmetic and exactly two reference-data cases,
sixteen fixed height slabs per case, and three cotangent boxes per
slab: 96 cotangent enclosures. Equation (12) uses one positive scalar
logarithm enclosure per case; (13) uses one log-sine per case and
one shared \(\log2\). Outside the 96 cotangent calls, the maximum
elementary call counts are one \(\pi\), one exponential, two cosine,
two sine, and five logarithm enclosures. The remaining interval
operations are addition, multiplication and division; the support
and conjugate calculations use exact rational arithmetic and
outward integer square roots. There are no original \(g\) evaluations, new references,
roots, inverses, optimizers, external-parameter cells or subdivisions.

Before execution, the implementation must bind this protocol, the
saved affine record and complete audit, both prior coordinate proofs,
the original main identities, and the strengthened curvature proofs.
All inherited bindings are verified before and after. The result saves
both parameter cases, all 32 height slabs, common-affine argument
supports and coefficient moduli, the 96 original cotangent enclosures,
exact integral weights and sums, force/value bounds, every cubic
branch and clipped optimizer enclosure, and all four final budgets.
All planned cases are retained regardless of their signs. There is no
automatic refinement, alternate height, new radius, or retry.
The fallback is none. An undefined elementary interval or failed
domain guard is saved as inconclusive; it does not authorize a
replacement case or extra evaluation.

The scalar comparison is a phase theorem on the full \(D_4\) canonical
families. A finite source consequence still needs its original
actual-reference hypotheses and the remaining terminal-profile
comparisons. It is not a whole-word or knot-volume conclusion, and
it makes no assertion about the type-three external disk.
