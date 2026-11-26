# The volume conjecture for the original reflected even closures

Research theorem, 3 November 2026.

The original reflected pair of even crossing blocks satisfies the
Kashaev volume conjecture at every fixed crossing power covered below.
The proof estimates the complete quantum sum and identifies its rate
with the volume of the knot complement. In particular, its conclusion
does not depend on discarding low colors, restricting the parity of the
quantum level, or choosing an undetermined constant in a classical action.

## 1. The knot, the invariant, and the assertion

Let \(R\) be the original positive crossing of two strands. A negative
power means the corresponding number of negative crossings. Let \(T\)
be the physical quarter-turn of a two-strand tangle, with the original
cyclic order of its four endpoints. Let \(C\) be the cylindrical closure
that joins the two top endpoints to the corresponding bottom endpoints
outside the tangle. Products are stacked in the original diagram order.

For an integer \(k\ge2\), consider the explicit diagram
\[
                 \mathcal K_k=C\bigl(R^{-2k}T(R^{2k})\bigr).
 \tag{1}
\]
Both crossing blocks have even power. The turned inner block has the
horizontal endpoint pairing, which the outer even block preserves.
Joining it to the vertical outside pairing gives one component. Thus
(1) is a knot. This description fixes the diagram without relying on
a convention for a knot-table name or for continued fractions.

Write \(K_N(\mathcal K_k)\) for its reduced, zero-framed Kashaev
invariant at \(q=e^{2\pi i/N}\), normalized to be one on the unknot.
The integer \(N\) is the quantum level. The crossing parameter \(k\)
is fixed before taking the limit in \(N\).

**Theorem 1.** Every knot (1) is hyperbolic, and
\[
 \boxed{\qquad
  \lim_{N\to\infty}\frac{2\pi}{N}
       \log|K_N(\mathcal K_k)|
       =\operatorname{Vol}(S^3\setminus\mathcal K_k).
 \qquad}
 \tag{2}
\]
The limit is through all integer levels. The conclusion also holds
after reversing the two crossing signs.

## 2. The quantum rate and the geometric action

We record the quantities used to connect the two sides of (2).
This also specifies which earlier results the theorem uses.

Let \(M_N\) be the matrix of multiplication by the original crossing
in the normalized Newton basis \(e_0,\ldots,e_{N-1}\) of the finite
tangle algebra. Let \(\phi_N\) be its original reduced closing
functional. The exact reflected pairing gives
\[
 \mathcal E_{k,N}
   :=\phi_N(R^{-2k}T(R^{2k}))
    =\sum_{j=0}^{N-1}|(M_N^{2k}e_0)_j|^2,
 \qquad |K_N(\mathcal K_k)|=\mathcal E_{k,N}.
 \tag{3}
\]
The second equality uses the original reduced invariant normalization.
In particular, no factor equal to a quantum dimension has been added.
The diagram and normalization checks are in Sections 2 and 4 of
[the original geometric-point calculation](research_even_reflected_run_geometric_point.md).

For a fixed integer \(k\), let \(T_k\) be the adjacency matrix of
the path with \(k\) vertices and let \(E_{ab}\) be the corresponding
matrix units. Define
\[
 H_k(\theta)=2\cos\theta\,I-T_k-e^{-i\theta}E_{11}-E_{kk},
 \qquad \delta(\theta)=2-2\cos\theta.
 \tag{4}
\]
Let \(\lambda_*(\theta)\) be the simple eigenvalue branch starting
at \(4\cos^2(\pi/(2k))\). The
[sharp reflected-growth theorem](research_even_run_sharp_reflected_growth.md)
proves that there is a unique \(\theta_k\in(0,\pi/2)\) with
\(|\lambda_*(\theta_k)|=\delta(\theta_k)\), and that
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log\mathcal E_{k,N}
  =2\int_0^{\theta_k}
                \log\left|\frac{\lambda_*(\theta)}{\delta(\theta)}\right|
                  \,d\theta=:\mathcal V(k).
 \tag{5}
\]
This theorem treats every original coefficient in (3). Its lower
bound uses the nonzero projection of the actual endpoint vector onto
the dominant mode. Its upper bound combines the exact low-color
estimate, middle-color contraction, and a spectral comparison on the
remaining quarter. Positivity of (3) is essential to this assembly.

The same critical point is described by a unique pair
\(\eta_k,\varphi_k\) satisfying
\[
 \begin{gathered}
  \eta_k>0,\qquad
  \frac{2\pi}{2k+1}<\varphi_k<\frac{\pi}{k},\\
  \cosh(2k\eta_k)-\cos(2k\varphi_k)
                        -\cosh\eta_k+\cos\varphi_k=0,\\
  \sinh(2k\eta_k)\sinh\eta_k
                        +\sin(2k\varphi_k)\sin\varphi_k=0.
 \end{gathered}
 \tag{6}
\]
Put \(t_k=\varphi_k-i\eta_k\) and
\(u_k=-\varphi_k-i\eta_k=-\overline{t_k}\). The original
geometric-point calculation proves the full primitive equations
\[
 \operatorname{arsinh}\!\left(\tan(t_k/2)\cos(u_k/2)\right)
                    =ik t_k-\pi i,
 \qquad
 \operatorname{arsinh}\!\left(\tan(u_k/2)\cos(t_k/2)\right)
                    =-ik u_k-\pi i .
 \tag{7}
\]
The logarithmic branches in these equations are fixed, not merely
specified after exponentiation. All eight original tetrahedra are
positive. The original marked-completion theorem therefore supplies
the hyperbolic metric on the complement of the actual knot (1).

Let \(\psi(t,u)\) denote the holomorphic original edge phase,
normalized by \(\psi(0,0)=4G/\pi\), where
\(G=\int_0^1\arctan(x)\,dx/x\) is Catalan's constant. Its
differential is
\[
 d\psi=-\frac1\pi(r_t\,dt+r_u\,du),
 \quad r_t=\operatorname{arsinh}(\tan(t/2)\cos(u/2)),
 \quad r_u=\operatorname{arsinh}(\tan(u/2)\cos(t/2)).
 \tag{8}
\]
On the selected positive branch the volume is
\[
 \operatorname{Vol}(S^3\setminus\mathcal K_k)=2\pi\mathcal G(k),
 \quad
 \mathcal G(k)=\psi(t_k,u_k)
       +\frac{ik}{2\pi}(t_k^2-u_k^2)-i(t_k+u_k)\in\mathbb R.
 \tag{9}
\]
The quadratic and linear filling terms in (9) are part of the
absolute volume formula.

## 3. Proof of the volume identity

The critical equations (6) have the same unique smooth solution
for every real \(k\ge2\). The stationary action \(\mathcal G(k)\)
therefore has a real-parameter continuation. Equations (7)--(8)
make its derivatives with respect to \(t,u\) vanish. Differentiating
only its explicit dependence on \(k\) gives
\[
        \frac{d}{dk}\{2\pi\mathcal G(k)\}
                      =4\eta_k\varphi_k,
 \qquad \lim_{k\to\infty}2\pi\mathcal G(k)=8G.
 \tag{10}
\]
For noninteger \(k\), this is an action, with no claim that it is
the volume of an integer filling.

The [spectral transgression theorem](research_reflected_even_spectral_volume_transgression.md)
continues (5) to the same real interval. In the coordinate
\(a=\eta-i\varphi\), it uses
\[
 X=-\frac{\sinh((k+1/2)a)}{\sinh((k-1/2)a)},
 \qquad L=-\frac{\sinh^2(a/2)}{\sinh^2(ka)},
 \qquad \mathcal V(k)=2\Im\int_{-i\pi/k}^{\eta_k-i\varphi_k}
                                        \log L\,d\log X.
 \tag{11}
\]
The logarithms are normalized at the lower endpoint on a simply
connected strip. The differential identity
\[
 (\log L)_k(\log X)_a-(\log L)_a(\log X)_k=-2a
 \tag{12}
\]
gives
\[
                   \mathcal V'(k)=4\eta_k\varphi_k,
        \qquad \lim_{k\to\infty}\mathcal V(k)=8G.
 \tag{13}
\]
The cited proof retains the motion of the singular lower endpoint
when differentiating. It also proves uniform convergence of a
regularized integrand for the limit in (13). Thus neither assertion
comes from a formal substitution in a divergent integral.

Equations (10) and (13) show that
\(\mathcal V(k)-2\pi\mathcal G(k)\) has zero derivative and tends
to zero. It is therefore identically zero on \([2,\infty)\).
For integer \(k\), equations (3), (5), and (9) now prove (2).
Reversing both signs conjugates the invariant and reflects the
hyperbolic metric, preserving its absolute invariant and volume.
This proves Theorem 1.

The classical continuation also gives the exact formula
\[
 \operatorname{Vol}(S^3\setminus\mathcal K_k)
      =8G-4\int_k^\infty\eta_s\varphi_s\,ds
      =8G-\frac{\pi^2}{k^2}+O(k^{-4}).
 \tag{14}
\]
The volumes strictly increase with \(k\). This separate classical
limit provides no uniform error estimate when the crossing power
is allowed to grow with the quantum level.

## 4. Infinite families of original assignments with a zero twist

The result treats some infinite fibers of the original parameter
space, which must be retained in a finite-exception theorem.
For the four-vertex path, write
\[
 K_4(a,v,b,c)=C\bigl(R^aT(R^vT(R^bT(R^c)))\bigr).
 \tag{15}
\]
The exact marked zero-power reduction proves
\[
                       K_4(a,0,b,c)\simeq C(R^{a+b}T(R^c)).
 \tag{16}
\]
Its proof retains the reversal of multiplication under the physical
half-turn; see Section 2 of
[the finite-exception scope calculation](research_finite_exception_scope_audit.md).

**Corollary 2.** For every integer \(k\ge2\) and every integer
\(m\), the original assignment
\[
                         (a,v,b,c)=(m,0,-2k-m,2k)
 \tag{17}
\]
produces a hyperbolic knot satisfying (2).

Indeed (16) identifies it with \(\mathcal K_k\). To make the
original filling coefficients explicit, fix a parity
\(\epsilon\in\{0,1\}\), write \(m=\epsilon+2r\), and use
the fixed half-twist carriers \((\epsilon,0,\epsilon,0)\).
In the original convention \(n_j=\eta_j-2p_j\), the integer
filling coefficients are
\[
                       (p_1,p_2,p_3,p_4)
                             =(-r,0,k+\epsilon+r,-k).
 \tag{18}
\]
For each fixed \(k,\epsilon\), these are infinitely many distinct
assignments as \(r\) varies. The conclusion covers every one of
them. No parameter fiber has been replaced by a single exception.

## 5. Scope and reproducibility

Theorem 1 concerns an exactly reflected closed pair. Its positive
sum (3) is the original invariant for that diagram. Different powers
on the two sides, or further turns and joins, generally produce a
coherent complex contraction. The present proof does not establish
its noncancellation or a boundary estimate suitable for arbitrary
additional fillings. Those are still needed for finitely many
exceptions on every admissible template.

The [period checker](../experiments/check_even_reflected_volume_period.py)
compares the spectral integral on two paths, the classical matrix
equation, the original primitive returns, all eight positive
Bloch--Wigner volumes, and the complete stationary action. Its saved
results at [100 digits](../repro/results/research-even-reflected-volume-period-root.json)
and [140 digits](../repro/results/research-even-reflected-volume-period-review.json)
include noninteger parameters to check the continued action.
These finite comparisons supplement the written proofs above;
the limit through all levels is supplied by the sharp source theorem.
