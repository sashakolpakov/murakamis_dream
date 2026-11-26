# Paying the outgoing last row with both first coordinates selected

Research deduction, 6 November 2026. The completed first-selection
comparison supplies the baseline missing from the earlier simultaneous
selection reduction. Moving only the second height then pays every
remaining outgoing last-row term. This removes eight terms without a
new parameter cover, root or primitive evaluation. The other profile
signs remain open.

## 1. The original profiles and a completed first-selection baseline

Fix an actual mixed open critical reference of length \(m\ge4\),
with first three flags \((1,1,\beta)\), \(\beta\in\{0,1\}\).
Write its retained coordinates as \(a_*,z_*,b_*\), its ordinary
indices as \(u_*,v_*\), and its first private coordinate as \(e_*\).
Put
\[
 P=[11/50,9/20],\quad H=1/100,\quad c=\Im z_*<0,\quad
 a=x+iH,\quad z_k=y+ik,\quad b=t+i\Im b_*,
 \qquad x,y,t\in P.
 \tag{1}
\]
Use the original cap phase \(\Psi\), bare ordinary phases
\(Q_1,Q_\beta\), cap profiles \(A_0,A_L\), and original
logarithmic lifts of the
[simultaneous-selection reduction](research_mixed_second_selected_four_profile_reduction.md),
Section 4. Write
\[
 \begin{split}
 L^k&=\max_{1/8\le q\le1/2}
        \Re Q_1(q+i\Im u_*;a,z_k),\\
 T^k&=2\pi(-k)_++2\pi(\Im b_*)_+,\qquad
 G_k(y)=\Re g(y+ik),\\
 W_1^1(x)&=-\Re g(a)-2\pi H,\quad W_1^0(x)=0,\\
 W_2^1(y)&=-G_H(y)-2\pi H,\quad W_2^0(y)=0.
 \end{split}
 \tag{2}
\]
The superscripts 1 and 0 denote the factorial and forced alternatives.
The full periodic last row is \(T^k\); it is not the value of a
central-strip logarithmic branch at an index of one.

The original allocated phases are
\[
 \begin{split}
 F_{12}&=\Psi(e,a)+Q_1(u;a,z)-g(a)-\tfrac12g(z),\\
 F_3&=Q_\beta(v;z,b)-\tfrac12g(z)-\tfrac\beta2g(b),\\
 F_{123}&=F_{12}+F_3,\qquad
 \Lambda_{123}=\Re F_{123,*}+\Re\{p_R(b-b_*)\},\\
 p_R&=g'(v_*+b_*)-(1+\beta/2)g'(b_*).
 \end{split}
 \tag{3}
\]
The two original marginals at \(z_*\) cancel:
\(\partial_zF_{12,*}+\partial_zF_{3,*}=0\). The outgoing
halfweight in (3) is retained, including when the next factor is
terminal at length four.

The [completed first-four/next-four profile comparisons](research_mixed_selected_four_four_full_product.md),
Sections 2--3, prove for \(j\in\{0,L\}\) and \(\nu_1\in\{0,1\}\),
\[
 A_j(x)+L^c+W_1^{\nu_1}(x)-\tfrac12G_c(y)
 <\Re F_{12,*}
  +\Re\{\partial_zF_{12,*}(z_c-z_*)\}-\frac1{2000}.
 \tag{4}
\]
This invokes its individual main/main and left-cap/main phase bounds,
not an inference from the modulus of a cancelling finite sum. All
present first-two references are within that theorem's actual family;
its length-three theorem already permits any later types.

The unselected last-row plane for the ordinary third factor gives
\[
 T^c-\tfrac12G_c(y)-\tfrac\beta2\Re g(b)
 \le\Re F_{3,*}
  +\Re\{\partial_zF_{3,*}(z_c-z_*)+p_R(b-b_*)\}.
 \tag{5}
\]
The source is the individual ordinary-current comparison used in
[the second-selection last-row proof](research_mixed_second_selected_outgoing_last_rows.md),
Section 1. It applies to the actual ordinary third factor also at
\(m=4\). Its nonpositive quadratic remainder may be discarded.
Adding (4)--(5) cancels the original internal tangent and proves
\[
 A_j+L^c+T^c+W_1^{\nu_1}-G_c
       -\tfrac\beta2\Re g(b)
 <\Lambda_{123}-\frac1{2000}.
 \tag{6}
\]
The first coordinate in (6) is already at its selected height \(H\).
No unselected cap plane at this changed height has been assumed.

## 2. The second-height transport does not depend on the first height

For the fixed ordinary point \(s=q+i\Im u_*\), the derivative
of \(\Re Q_1(s;a,z_k)\) with respect to \(k\) is
\[
 \frac{d}{dk}\Re Q_1(s;a,z_k)
    =\mathcal A(y,k)-\mathcal A(q+y,\Im u_*+k),\qquad
 \mathcal A(t,k)=\arg(1-e^{2\pi k-2\pi it}).
 \tag{7}
\]
It is independent of the incoming target \(a\), including its
height: the asymmetric chirp is \(2\pi ias\). Thus the argument
bounds and the full height-transport table of the cited last-row
proof apply unchanged at the present \(\Im a=H\). Taking the
maximum over the fixed original main line preserves the inequalities.
They give
\[
 \begin{split}
 L^H-G_H-2\pi H-(L^c-G_c)
       &\le-\pi c-\frac{11\pi}{25}H,\\
 L^H-L^c&\le-\frac{19\pi}{20}c+\pi H,\qquad
 T^H-T^c=2\pi c.
 \end{split}
 \tag{8}
\]
All arguments remain in their original regular strips. The cap
profile and its selected-weight alternative are constant during
this transport.

**Theorem 1.** All eight outgoing last-row terms satisfy
\[
 A_j+L^H+T^H+W_1^{\nu_1}+W_2^{\nu_2}
       -\tfrac\beta2\Re g(b)
 <\Lambda_{123}-\frac3{1000},
 \quad j\in\{0,L\},\quad \nu_1,\nu_2\in\{0,1\}.
 \tag{9}
\]

*Proof.* Relative to the left side of (6), the factorial second
alternative changes by at most
\[
                 \pi c-\frac{11\pi}{2500}
                      <-\frac{11\pi}{2500}<-\frac1{400}.
 \tag{10}
\]
The forced second alternative changes by at most
\[
 \frac{21\pi}{20}c+\pi H+G_c(y)
 \le\pi H+J(y)+\pi(11/20+y)c
 <\pi H+J(9/20)<-\frac9{3500}<-\frac1{400}.
 \tag{11}
\]
Here \(G_c(y)\le J(y)-\pi(1/2-y)c\), and the exact elementary
witness \(J(9/20)<-17/500\) is proved in equations (21)--(25)
of the cited last-row proof. These use only \(c<0\), \(y\in P\)
and \(H=1/100\). Adding either strict improvement to (6), and
using \(1/2000+1/400=3/1000\), proves (9). \(\square\)

## 3. The resulting complete finite-current reduction

For \(\beta=0\), let \(\mathcal J_0=\{0,R\}\); for
\(\beta=1\), let \(\mathcal J_1=\{0\}\). Define
\[
 \mathcal D_\beta=
 \max_{\substack{j\in\{0,L\},\ k\in\mathcal J_\beta\\
                  \nu_1,\nu_2\in\{0,1\}}}
 \left\{A_j+R_0^2+R_k^3-\tfrac\beta2\Re g(b)
            +W_1^{\nu_1}+W_2^{\nu_2}-\Lambda_{123}\right\}.
 \tag{12}
\]
There are sixteen alternatives for prefix \(443\) and eight for
\(444\). In the latter case the
[completed outgoing-four half-row domination](research_mixed_second_selected_outgoing_four_half_row_completion.md)
replaces \(R_R^3\) by \(R_0^3-1/20\), independently of the cap,
the first ordinary factor and both selected weights.

**Corollary 2.** The literal weighted finite product of equation (8)
of the simultaneous-selection reduction satisfies, for every
\(\tau>0\) and every fixed ordinary-color derivative order,
\[
 \mathcal B_{123,N}^{(k)}
 \le C_{\tau,k}N^{A_{\tau,k}}
 \exp N\left\{\Lambda_{123}
              +\max\left(-\frac3{1000},\mathcal D_\beta\right)+\tau\right\}.
 \tag{13}
\]
It includes all original finite currents and both level parities.

*Proof.* Start with the complete twenty-four-term bound. Apply (9)
to its right-last-row terms. For \(\beta=1\) use the stated
pointwise half-row comparison on the remaining right-half-row terms.
All terms share the same reference, outer targets, original outgoing
halfweight and tangent. The earlier alias and left-cut reductions
remain unchanged. Their finite-current and color estimates spend
one arbitrary total tolerance, giving (13). No finite Fourier factor
is divided out. \(\square\)

Neither (12) nor the remaining joint main/main or main/half-row signs
are proved here. In particular this corollary supplies no completed
simultaneous-selection or whole-invariant theorem.

## 4. An exact shared-index cancellation for the remaining main profiles

The following identities specify a useful trial for a future joint
comparison; they assert no sign for the remaining maximum. Keep all
unselected index heights and take the original real trial, with
\[
 a_H=\Re a_*+iH,\quad z_H=\Re z_*+iH,\quad
 \Delta_a=H-\Im a_*,\quad\Delta_z=H-\Im z_*.
 \tag{14}
\]
For the cap main profile and outgoing main profile, the target phase is
\[
 \Phi_{\nu_1,\nu_2}=F_{123}
    +(1-\nu_1)g(a)+(1-\nu_2)g(z)+2\pi i(\nu_1a+\nu_2z).
 \tag{15}
\]
At the real reference trial \((e_*,u_*;a_H,z_H,v_*,b_*)\),
its defect against the original action and outgoing tangent is exactly
\[
 \begin{split}
 \mathcal T_{\nu_1,\nu_2}
  =V_a+V_z+(1-\nu_1)\Re g(a_H)+(1-\nu_2)\Re g(z_H)
                         -2\pi H(\nu_1+\nu_2),\\
 V_a=\Re\{g(e_*+a_H)-g(e_*+a_*)
        +g(u_*+a_H)-g(u_*+a_*)-3g(a_H)+3g(a_*)
                                      +2\pi iu_*(a_H-a_*)\},\\
 V_z=\Re\{g(u_*+z_H)-g(u_*+z_*)
        +g(v_*+z_H)-g(v_*+z_*)-3g(z_H)+3g(z_*)
                                      +2\pi iv_*(z_H-z_*)\}.
 \end{split}
 \tag{16}
\]
The vertical costs add exactly because \(\partial_a\partial_zF_{123}=0\).
The unchanged private action cancels in this main-profile trial.
In particular it need not be reconstructed by a new cap root.

Put \(E=e^{-2\pi ie_*},A=e^{-2\pi ia_*},U=e^{-2\pi iu_*},
Z=e^{-2\pi iz_*},V=e^{-2\pi iv_*}\),
\(\lambda_a=e^{2\pi\Delta_a}\), \(\lambda_z=e^{2\pi\Delta_z}\),
\(\ell_a=2\pi\Delta_a\), \(\ell_z=2\pi\Delta_z\), and define
\[
 \begin{gathered}
 A_{ea}=\log\left|\frac{1-\lambda_aEA}{1-EA}\right|,\quad
 A_{ua}=\log\left|\frac{1-\lambda_aUA}{1-UA}\right|,\quad
 A_{uz}=\log\left|\frac{1-\lambda_zUZ}{1-UZ}\right|,\quad
 A_{vz}=\log\left|\frac{1-\lambda_zVZ}{1-VZ}\right|,\\
 C_a=\log\left|\frac{1-\lambda_aA}{1-A}\right|,\quad
 C_z=\log\left|\frac{1-\lambda_zZ}{1-Z}\right|,\quad
 d_a=\ell_a-A_{ua},\quad d_z=\ell_z-A_{vz},\\
 D_a^{\nu_1}=A_{ea}+A_{ua}-3C_a
                         +(1-\nu_1)\log|1-\lambda_a A|,\\
 D_z^{\nu_2}=A_{uz}+A_{vz}-3C_z
                         +(1-\nu_2)\log|1-\lambda_z Z|.
 \end{gathered}
 \tag{17}
\]
In coordinate order \((e,a,u,z,v,b)\), the exact real target gradient,
after subtracting the original outgoing affine term, is
\[
 \boxed{\quad
 (A_{ea},D_a^{\nu_1},A_{uz}-d_a,D_z^{\nu_2},-d_z,0).
 \quad}
 \tag{18}
\]
Indeed all internal derivatives of \(F_{123}\) vanish at the
original reference. The incoming chirp changes the \(u\) derivative
by \(-\ell_a\); the outgoing chirp changes the \(v\) derivative
by \(-\ell_z\). The boundary derivative still equals the original
\(p_R\), so its target gradient cancels exactly.

The first-selected increment contributes \(-d_a\) to the shared
index force and the second-selected increment contributes \(A_{uz}\).
One has \(d_a>0\): the actual sum
\(\Re(a_*+u_*)\in(.545,.71)\) implies \(\Re(UA)<0\),
and \(\lambda_a>1\) gives
\(1<|1-\lambda_a UA|/|1-UA|<\lambda_a\), with its logarithm
strictly positive. The same elementary negative-real-part argument
gives \(A_{uz}>0\), since
\(\Re(u_*+z_*)\in(.48,.72)\subset(.25,.75)\).
The original correlated increment bound in the
[directional budget](research_mixed_second_selected_directional_budget.md)
gives \(d_z>0\). Thus the shared force in (18) must be kept as
one signed difference. Replacing it by \(A_{uz}+d_a\) discards
this proved opposition of forces. Equations (16)--(18) preserve all
four Fourier pairs; no separate marginal optimization or moving
reference is used.
