# Carrying the Casimir mark through the finite conditional contraction

Research deduction, 5 November 2026. The mark in the
[ordinary-boundary trace identity](research_mixed_ordinary_boundary_casimir_mark.md)
can be contracted before taking absolute values. It changes one vertex,
and admits an exact expansion in ordinary endpoint values and first
normals. Existing Newton color estimates then give a uniform bound
for the twisted family and an explicit loss away from the complete
physical color. These upper bounds are not shown below the open
geometric action and do not prove whole-source noncancellation.

## 1. One modified finite vertex

Fix \(N\ge2\), \(q=e^{\pi i/N}\), \(r=q^{-2}\), \(D=N-1\), and
\(\kappa=q^{D^2/2}\). Write \(C\) for the original Casimir multiplication,
\(M=R(C)\) for the crossing, \(J\) for reversal, and \(A_n=JM^n\).
Retain the original full Newton vector \(v(w)\).
Use \(S,B_3,B_4,\Gamma\) from
[the exact Fourier contraction](research_mixed_wire_exact_contraction.md):
\[
 S=\operatorname{diag}\left(
       \frac{\kappa^{-1}(-q)^{-a}}{P_a}\right)M,\quad
 P_a=(r;r)_a,\quad
 \Gamma=SS^T,\quad A_n=S^TB_nS,\quad b(w)=Sv(w).
 \tag{1}
\]
All matrices are \(N\) by \(N\). For any polynomial \(f\), put
\[
 T=SCS^{-1},\qquad B_3^{[f]}=B_3f(T).
 \tag{2}
\]
Since \(C\) commutes with \(M\), \(T\) is lower bidiagonal:
\[
 T_{aa}=q r^{-a}+q^{-1}r^a,\qquad
 T_{a,a-1}=q^{-1}(1-r^{-a})\quad(1\le a<N).
 \tag{3}
\]
Indeed its diagonal is \(c_a=2\cos((2a+1)\pi/N)\).
The quotient of consecutive diagonal factors in (1) is
\(-q^{-1}/(1-r^a)\); multiplying by the original subdiagonal
\(-4\sin^2(\pi a/N)\) gives (3).
Thus, without a change of finite source,
\[
 A_3f(C)=J(R^3f)(C)=S^TB_3^{[f]}S.
 \tag{4}
\]
In particular a marked cyclic product has the same original
conditional contractions at every other vertex. The modified vertex
is symmetric, since multiplication is self-adjoint for the original
Frobenius pairing. Equations (2)--(4) retain the complete matrices,
including repeated-root first normals.

For odd \(N\), take the exact idempotent
\(\pi_N(z)=(2T_N(z/2)+2)/(N^2(z+2))\), and let
\(\rho_N=R(-2)\). The proved identity
\(A_3\pi_N(C)=\rho_N^3v(-2)v(-2)^T\) gives
\[
             \boxed{\ \Gamma B_3^{[\pi_N]}\Gamma
                  =\rho_N^3 b(-2)b(-2)^T.\ }             \tag{5}
\]
The two adjacent Gram joins therefore collapse exactly to the two
original ordinary endpoint vectors. This identifies the same open
source; it is not a new asymptotic for it. The finite conversion of
these vectors to the endpoint polynomials \(H_N,U_{\epsilon,N}\)
and the unchanged conditional kernels \(C_{\epsilon,N}\) is precisely
[torus composition, equations (16)--(20)](research_mixed_conditional_torus_composition.md).
It retains the factors \(d_N(X)(1+X^{-N})\) and all original
normalizations. There is no need to estimate separate Fejér modes
before applying (5).

## 2. The general mark changes only endpoint values and normals

Let \(c_a\) run over distinct physical roots, let
\(v_a=v(c_a)\), \(v'_a=v'(c_a)\), and write
\(\eta=(-1)^{N-1}\). All these roots are double except \(-2\)
at odd levels. For \(g=R^3f\), interpreted through its original
physical values and first normals, the exact matrix identity is
\[
 \begin{split}
 A_3f(C)={}&
 \eta\sum_{\text{double }a}
 \bigl[
 (4-c_a^2)g(c_a)(v'_av_a^T+v_av_a'^T)\\
 &\hspace{23mm}
 +\{(4-c_a^2)g'(c_a)-c_ag(c_a)\}v_av_a^T
 \bigr]\\
 &+\boldsymbol1_{\{N\ {\rm odd}\}}g(-2)v(-2)v(-2)^T .
 \end{split}                                             \tag{6}
\]
To prove it, pair both sides by trace with an arbitrary matrix \(W\).
The left side is
\(\phi_N(g(z)v(z)^TWv(z))\), by the exact Frobenius identity.
Apply the full physical trace formula in
[the normal-defect theorem, equation (4)](research_trace_normal_defect_positive_form.md),
including the derivative of the product. Nondegeneracy of the
matrix trace pairing proves (6).

After the two Gram joins, (6) has the same form with
\(v_a,v'_a\) replaced by \(b(c_a),b'(c_a)\). Thus it is a finite
linear combination of the existing open conditional sources with
both ordinary colors equal to a physical \(c_a\), and with either
zero or one ordinary endpoint derivative. The coefficients retain
the original phases of \(R^3\), and the first-normal terms are not
discarded. This is an explicit modified-endpoint description of the
twisted trace, not a positivity statement.

## 3. A uniform bound with an explicit far-color loss

For a real ordinary color \(w=-2\cos\theta\), \(0\le\theta\le\pi\),
let \(m(\theta)\) be the maximum Newton row entropy. Write
\[
 b_2=\frac{2G_{\rm Cat}}{\pi},\quad M_\infty=2b_2,\quad
 c=2\int_0^{5/6}\log(2\sin\pi t)\,dt.
 \tag{7}
\]
Here \(G_{\rm Cat}\) is Catalan's constant.
The [real-period entropy theorem, Lemma 3](research_three_crossing_real_period_newton_bound.md)
and [Newton color tubes, Corollary 2](research_mixed_newton_color_tubes.md)
give, for every fixed derivative order \(j\),
\[
 \|v^{(j)}(w)\|_2
   \le C_jN^{a_j}e^{Nm(\theta)},\qquad
 m(\theta)\le b_2-\frac{w+2}{4\pi}.
 \tag{8}
\]
This estimate includes zeros and both level parities. At a physical
value and its permitted first normal, the exact inverse-multiplication
identity gives the further bound
\[
 \left\|\partial_w^j\{v(w)^TM^{-1}\}\big|_{w=c_a}\right\|
       \le CN^A e^{Nm(\theta_a)},\qquad j=0,1.
 \tag{9}
\]
The \(j=1\) assertion is needed only at double roots. It follows
by differentiating the physical product \(R^{-1}v^T\) in its local
algebra. The actual physical values of \(R^{-1}\) have modulus one,
and its first normals have polynomial size, as in
[positive-three boundary estimates, equations (42)--(44)](research_positive_three_crossing_cycle.md).
No off-grid eigenvector equation is used.

For a word \(W=A_{n_1}\cdots A_{n_m}\) let
\(k_4=\#\{j:n_j=4\}\). Its exact similarity and the one-crossing norm
bound yield
\(\|MWM^{-1}\|\le C\exp N(2m+k_4)c\).
Using (8)--(9) at the two ends therefore proves
\[
 \left|\partial_z^\alpha\partial_w^\beta
                   \{v(z)^TWv(w)\}\big|_{z=w=c_a}\right|
 \le CN^A
 e^{N\{(2m+k_4+1)c+2m(\theta_a)\}},
 \quad \alpha+\beta\le1.
 \tag{10}
\]
The extra factor \(e^{Nc}\) is from \(Mv^{(\beta)}\); the left
inverse-multiplication factor was handled by (9).

Now take the exact twisted mark
\[
 f_{\vartheta,N}(z)
     =1+2\sum_{k=1}^{N-1}\cos(k\vartheta)T_k(-z/2),\qquad
 Z_N(\vartheta;W)=\operatorname{tr}(f_{\vartheta,N}(C)WA_3).
 \tag{11}
\]
For a fixed strip \(|\Im\vartheta|\le h\), its physical values
and first ordinary derivatives are bounded by
\(CN^3e^{(N-1)h}\). This uses
\(|T_k(x)|\le1\) and \(|T'_k(x)|\le k^2\) on \([-1,1]\).
Multiplication by the physical values and normals of \(R^3\)
changes only a polynomial factor.

Let \(Z_N^{\rm far,\delta}\) be the part of the exact sum (6)
whose physical colors satisfy \(c_a\ge-2+\delta\), with
\(0<\delta<4\). Combining (6), (8), and (10) proves the uniform bound
\[
 \boxed{\quad
 |Z_N^{\rm far,\delta}(\vartheta;W)|
 \le CN^A\exp N\left\{
      (2m+k_4+1)c+M_\infty-\frac{\delta}{2\pi}+h
                      \right\}.\quad}                  \tag{12}
\]
With \(\delta=0\) and every physical node included, the same proof
bounds the whole \(Z_N\), omitting the loss term.
The constants may depend on the fixed word and strip.
This is a bound for the complete twisted family, not a collection
of unproved individual Fourier-mode estimates.

At odd levels, integration against the exact Fejér mark annihilates
the far-color sum, including its first normals, identically:
\[
 \int_{-\pi}^{\pi}
       F_N^{\rm Fej}(\vartheta)
              Z_N^{\rm far,\delta}(\vartheta;W)\,d\vartheta=0.
 \tag{13}
\]
This follows from the values and double zeros of \(\pi_N\), or
directly from (5). It is an exact cancellation, not a claim that
its separate absolute terms are small.

## 4. The corresponding part of the even resolvent

At even levels set \(G=(C+2I)^{-1}\). Let \(I_\delta\) be the
unique algebra idempotent with value one and derivative zero at
each physical color \(c_a\ge-2+\delta\), and value and derivative
zero at the other physical colors. Put
\[
 G_{\rm far}=I_\delta(C)G,\qquad
 v_{\rm far}=\frac4{N^2}JG_{\rm far}\mathbf e_0,\qquad
 v_{\rm near}=v(-2)-v_{\rm far}.
 \tag{14}
\]
This is an exact decomposition of the original forced resolvent,
with no omitted normal. The vector \(G_{\rm far}\mathbf e_0\)
is the coefficient vector of the algebra element
\(I_\delta(z)/(z+2)\). Its coefficient of \(e_j\) is
\(\phi_N(I_\delta(z)e_{D-j}(z)/(z+2))\).
On the retained physical colors the multiplier and its derivative
are bounded by constants depending only on \(\delta\).
The full trace formula and (8) imply
\[
 \|v_{\rm far}\|+
 \|v_{\rm far}^TM^{-1}\|
       \le CN^A e^{N(b_2-\delta/(4\pi))}.               \tag{15}
\]
For the second term use
\(v_{\rm far}^T=(4/N^2)\mathbf e_D^TG_{\rm far}\);
right multiplication by \(M^{-1}\) changes the multiplier to
\(I_\delta R^{-1}/(z+2)\), whose physical values and first normals
still have polynomial bounds. This proves (15) directly on the
original quotient.

Consequently either one-far-end observation is bounded by
\[
 |v_{\rm far}^TWv(-2)|+|v(-2)^TWv_{\rm far}|
 \le CN^A
   e^{N\{(2m+k_4+1)c+M_\infty-\delta/(4\pi)\}},
 \tag{16}
\]
and the two-far-end observation has loss \(\delta/(2\pi)\).
The unfiltered complete endpoint satisfies the all-parity physical
Hermite bound of the marked-observation note, equation (17).

The near part of (14), and the near-complete ordinary endpoint factors
in (6), remain the unresolved global observation. Their local packets
on the actual outgoing images are already supplied by the
[complete first-cap theorem](research_mixed_complete_first_cap_packet.md)
and the endpoint packet theorems. Equations (12) and (16) are not
asserted to lie below the local open action; they establish an explicit
loss within a known upper envelope. Identifying this source and
bounding its far physical colors does not control the full outgoing
Fourier period or promote a local packet to the whole open source.
