# The complete first-cap contour envelope on the early taper

Research deduction, 7 November 2026. The early-taper real-row theorem
can be strengthened to the original five-current envelope with any
fixed private main height in the original rectangle. The new step is
private vertical convexity at all complex private indices, proved from
the exact endpoint curvature. This permits retaining the actual private
reference height; it does not supply a calibrated mixed-boundary sign
or a transport inequality for every complex-private main profile.
No numerical evaluation or certificate replay is used.

## 1. The original finite source and domain

Keep the literal cap and its prescribed row interpolation from
[the complete-current criterion](research_mixed_cap_outer_contour_reduction.md),
equations (1)--(7):
\[
\begin{split}
 U_{\alpha,N}(w,X)
 &=\sum_{j=0}^{N-1}
       \frac{H_N(w,r^{-j})p_j(X)}{P_j^{1+\alpha}},
       \qquad X=e^{-2\pi iz},\\
 A_{\alpha,N}(e,z,w)
 &=D_N(e)^{-1}C_N(e,w)
       \frac{\widehat P_N(N(e+z))}
            {\widehat P_N(Nz)\widehat P_N(Ne)^\alpha},
       \qquad \alpha\in\{0,1\}.
\end{split}                                                     \tag{1}
\]
At each physical private index the second line is precisely its
summand in the first. In particular the whole coherent endpoint
coefficient is retained before any outer contour decomposition.

Let
\[
\begin{split}
 E_c&=[27/100,49/100]+i[-11/200,1/25],\\
 Z_{\rm early}&=\left\{x+ih:\quad
       \frac1{10}\le x\le\frac{11}{50},\quad
       -\frac{27}{250}\le h\le\frac7{40}(x-1/10)\right\}.
\end{split}                                                     \tag{2}
\]
The actual first-coordinate taper, including additional attenuation,
is contained in this set. The positive height bound retains its
correlation with the real coordinate. The original endpoint packet is
holomorphic on a fixed neighborhood of \(E_c\). The row (1) is regular
on a fixed neighborhood of \(E_c\times Z_{\rm early}\): the real parts
of \(e,z,e+z\) are respectively in
\([.27,.49],[.1,.22],[.37,.71]\).

At complete color its original phase is
\[
 \Psi_\alpha(e,z)=S(e)+J(e+z)-J(z)-i\pi ez-\alpha g(e),
 \qquad g(e)=J(e)+\frac{\pi i}{2}(e-e^2).
                                                               \tag{3}
\]
No additive constant, allocation, or logarithmic lift is changed.

## 2. Complex private curvature on the whole original rectangle

**Lemma 1.** Throughout \(E_c\), the actual endpoint action satisfies
\[
 -\frac{S''(e)}\pi
 =\cot\pi e+
       \frac{2}{\sin\pi e\,\sqrt{2-e^{-2\pi ie}}},
 \qquad
 -\Re S''(e)>\pi\Re\cot\pi e>0.                       \tag{4}
\]
The square root is the principal root with positive real part.

*Proof.* The exact endpoint identity and its original branch matching
on \(0<e<1/2\) are proved in Section 2 of
[the early real-row theorem](research_mixed_cap_early_taper_real_rows.md).
The identities there give the first formula in (4) before taking a
real part. On \(E_c\),
\[
 \Re(2-e^{-2\pi ie})>2,\qquad
 \Im(2-e^{-2\pi ie})>0.
\]
Consequently its indicated square root is a single holomorphic branch
on a neighborhood of this rectangle. The original endpoint action is
holomorphic there as well. The identity theorem extends the real-line
formula to the entire connected rectangle, with boundary values by
continuity. This fixes the branch rather than choosing a new root.

Write \(e=u+iv\). Since \(1/4<u<1/2\),
\[
 \left|\tan\arg\sin\pi e\right|
   =|\tanh\pi v|\cot\pi u<1.
\]
The real part of \(\sin\pi e\) is positive, hence
\(|\arg\sin\pi e|<\pi/4\). Meanwhile
\(0<\arg(2-e^{-2\pi ie})<\pi/2\). The argument of the
second reciprocal product in (4) therefore belongs to
\((-\pi/2,\pi/4)\), so its real part is strictly positive.
The last inequality of (4) follows from the standard cotangent
formula on \(0<\Re e<1/2\). \(\square\)

**Lemma 2.** Both own types satisfy
\[
             -\Re\Psi_{\alpha,ee}(e,z)>0
             \quad(e\in E_c,\ z\in Z_{\rm early}).       \tag{5}
\]
There is a uniform positive lower bound on this compact product.
Thus each private horizontal restriction is strictly concave and
each private vertical restriction is strictly convex.

*Proof.* Put \(C(w)=\Re\cot\pi w\). Differentiating (3) gives
\[
 -\Re\Psi_{\alpha,ee}
       =-\Re S''+\alpha\pi C(e)-\pi C(e+z).             \tag{6}
\]
If \(\Re(e+z)\ge1/2\), then \(C(e+z)\le0\), and (4)
proves the claim directly.

Otherwise write \(u=\Re e\) and \(x=\Re z\). The original
height bound and an elementary hyperbolic-cosine bound give
\[
 \cosh(2\pi\Im e)<\frac{16}{15},\qquad
 C(e)>\frac{15}{16}\cot\pi u.                           \tag{7}
\]
For the first inequality, use \(.11\pi<7/20\) and
\[
 \cosh t\le1+\frac{t^2}{2(1-t^2/12)},\qquad
 1+\frac{(7/20)^2}{2(1-(7/20)^2/12)}<\frac{16}{15}.
\]
For the second, \(\cos(2\pi u)<0\), and
\[
 \frac{C(e)}{\cot\pi u}
  =\frac{1-\cos(2\pi u)}
         {\cosh(2\pi\Im e)-\cos(2\pi u)}>
    \frac{15}{16}.
\]
For every finite shifted height,
\(C(e+z)\le\cot\pi(u+x)\). On the real interval from
\(u\) to \(u+x<1/2\),
\[
 \frac{d}{dv}\log\cot\pi v
       =-\frac{2\pi}{\sin2\pi v}\le-2\pi.
\]
As \(x\ge1/10\), this proves
\[
 C(e+z)\le\cot\pi(u+x)
       \le e^{-2\pi x}\cot\pi u
       <\frac23\cot\pi u.                              \tag{8}
\]
The last strict inequality follows already from
\(e^{\pi/5}>1+\pi/5>8/5>3/2\).
Equations (4), (6)--(8) leave more than
\((13\pi/48)\cot\pi u>0\). All functions are regular on
the full compact product, so continuity supplies a positive uniform
lower bound in (5). \(\square\)

This proof applies to the bare cap. An outgoing halfweight does not
enter its private second derivative, but no finite halfweight
division or selected-source conclusion is needed here.

## 3. The complete early-taper five-profile theorem

Choose any private main height \(h_e\in(-.055,.04)\). Define
\[
\begin{split}
 A_{\alpha,0}(z;h_e)
   &=\max_{.27\le u\le.49}\Re\Psi_\alpha(u+ih_e,z),\\
 A_{\alpha,L}(z)&=\Re\Psi_\alpha(.27,z),\\
 A_{\alpha,R}(z)&=\Re\Psi_\alpha(.49,z),\\
 A_{\alpha,-}(z)
   &=\max_{.27\le u\le.49}\Re\Psi_\alpha(u-.055i,z)-.11\pi,\\
 A_{\alpha,+}(z)
   &=\max_{.27\le u\le.49}\Re\Psi_\alpha(u+.04i,z)-.08\pi,\\
 A_\alpha(z;h_e)&=\max\{A_{\alpha,0},A_{\alpha,L},A_{\alpha,R},
                                    A_{\alpha,-},A_{\alpha,+}\},\\
 E_{\rm end}(h)&=\frac35+2\pi h_++\frac1{100}\log4.
\end{split}                                                     \tag{9}
\]
In particular the two cut profiles keep height zero, whatever main
height is chosen.

**Theorem 3.** There is \(c_0>0\) such that for each tolerance
\(\tau>0\), both parities and both \(\alpha\),
\[
 |U_{\alpha,N}(-2\cos\theta,e^{-2\pi iz})|
 \le C_\tau N^{b_\tau}
 \left[e^{N\{A_\alpha(z;h_e)-c_0(1-\cos\theta)+\tau\}}
            +e^{N\{E_{\rm end}(\Im z)+\tau\}}\right]
                                                               \tag{10}
\]
uniformly for \(z\in Z_{\rm early}\), \(-\pi\le\theta\le\pi\),
and \(h_e\) in any fixed compact subinterval of \((-.055,.04)\).
Each fixed ordinary-color derivative has the same two exponents
with an appropriate polynomial prefactor.

*Proof.* Repeat the exact retained-index decomposition in
[the full boundary-window envelope](research_mixed_boundary_window_real_color_envelopes.md),
Theorem 1, using the unchanged interpolant (1). The real-color
endpoint estimate on \(E_c\) bounds its complete coherent coefficient
by \(\Re S(e)-c_E(1-\cos\theta)\), with \(c_E>0\).
All other factors are color independent and have their original
uniform regular symbols.

The exact residue identity retains its constant coefficient \(+N\),
the shifted main segment at \(h_e\), both unpenalized joins, both
horizontal aliases and every vertical alias side. Lemma 2 bounds each
join by its real-cut and main-height endpoints. On each sign half of a
vertical alias the real phase minus its original \(2\pi|\Im e|\)
penalty remains convex, hence is bounded by its real-cut or horizontal
endpoint. These are exactly the five profiles (9). No complete current
has been discarded.

For compact physical private tails in \([.01,.99]\),
[the early real-row theorem](research_mixed_cap_early_taper_real_rows.md),
Corollary 2 and Lemma 3, transports their full coefficient upper rates
to the same real cuts \(.27,.49\). Its proof retains the actual
positive-height restriction in (2), including the own-three upper
tail. The original physical-index coefficient estimate supplies a
common positive angular loss on this compact interval. These physical
tail bounds therefore also enter the first exponent in (10).

At the two true private-index ends use precisely Section 4 of that
theorem: the complete finite Newton estimate, the literal full-product
identity and the uniform denominator-angle bound give the second
exponent \(E_{\rm end}(h)\). These bounds retain every product zero;
no angular loss is required there. Notice that
\(E_{\rm end}<373/500\) on (2).

Take \(c_0\le\min(c_E,c_I)\), where \(c_I>0\) is the compact
physical-index angular constant. Summing the physical rows and all
current bounds costs only polynomial factors. Place each finite cut
between its two adjacent physical indices; its discrepancy from the
limiting cuts is \(O(N^{-1})\). Regularity on a fixed neighborhood
and the strict tail directions justify those shifts after transport
to the cuts. Allocate all symbol and product errors within \(\tau\).
The same coefficient estimates for fixed ordinary derivatives, or
their original polynomial-degree/Cauchy consequence, give the stated
derivative scope. This proves (10). \(\square\)

## 4. What this adds to the ordinary three-four comparison

The main height in (10) may be the actual original private height of
the first type-three cap. The theorem also permits a continuous choice
of that height inside a fixed compact subinterval: it is uniform and
does not require a new critical point at the moving outgoing target.
At the endpoint \(x=.22\), with the original outgoing and private
heights, the five profiles are exactly those of the already completed
cap supporting-plane theorem. Thus the source representation itself
no longer requires resetting the private main profile to height zero.

This does not establish the necessary mixed transport inequality.
The earlier real-private derivative estimates do not automatically
hold after replacing that real private coordinate by a complex one,
and a varying private height contributes its own derivative term.
Both real cuts, both private aliases, and the explicit true-end
profile in (9) remain present. A coupled argument must control those
profiles together with the adjoining literal terminal source and the
original stationary marginals. No calibrated whole-circle estimate,
outside-color theorem, or new knot-family conclusion follows here.
