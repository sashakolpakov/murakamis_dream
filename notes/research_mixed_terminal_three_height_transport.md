# Attenuating a type-three input of the complete terminal transform

Research deduction, 5 November 2026. The complete type-three terminal
transform admits the same external-height allowance as the original
type-three conditional source. This is a pointwise transport of its
proved contour decomposition, not continuation of a target critical
point. It applies at the end of any word with a type-three retained
neighbor. In particular it removes the missing terminal-edge step
from the first-collar comparison for the length-three words with first
two types \((3,3)\) or \((4,3)\). No new numerical check is used.

## 1. Actual reference and claimed allowance

Let \(a_*=A+ic\) be an actual type-three input of a type-three
terminal block. Both ordinary and attached inputs are allowed, with
their original coupled endpoint root. In particular
\[
 -.072<c<.068,\qquad
 y\in I_3=[.267,.433],\qquad
 a_k=y+ik,\quad k\in[\min(c,0),\max(c,0)].
 \tag{1}
\]
Use the original terminal action \(\mathcal P_0\), and write
\[
\begin{split}
 B_0(a_*;y)&=\Re\mathcal P_0(a_*)+
       \Re\mathcal P_0'(a_*)(y-A)-\kappa_*(y-A)^2,
       \quad\kappa_*=1/2500000,\\
 a_c(k)&=\begin{cases}
 0,&c\le0,\quad c\le k\le0,\\
 \pi(c-k),&c\ge0,\quad0\le k\le c.
 \end{cases}
\end{split}
 \tag{2}
\]
No neighboring Fourier halfweight occurs because this retained input
has type three. All terminal rows and terminal alternatives remain
inside the exact \(\mathcal V_{0,N}\).

**Theorem 1.** For every \(\tau>0\), on a sufficiently small fixed
ordinary-color disk and for all sufficiently large integer levels of
either parity,
\[
 |\mathcal V_{0,N}(w,e^{-2\pi ia_k})|
 \le C_\tau N^{A_\tau}
                 \exp N\{B_0(a_*;y)+a_c(k)+\tau\}.
 \tag{3}
\]
All fixed ordinary-color derivatives have the same upper rate on
smaller disks, with their polynomial prefactors. The original
reference is fixed throughout; no critical point at \(a_k\) is
asserted or needed.

## 2. All complex transform-index currents have the same marginal

The simultaneous original phase in
[the joint terminal theorem](research_mixed_terminal_three_joint_zero_mode.md)
depends on the incoming variable through
\(g(a+t)-g(a)+2\pi iat\). Hence, at every fixed \((t,u)\),
\[
 \mathcal T_a=g'(a+t)-g'(a)+2\pi it
             =\log_{\rm R}(C+P)-\log_{\rm R}(C-i),
 \qquad C=\cot\pi t,\quad P=\cot\pi a.
 \tag{4}
\]
This is exactly the fixed-index identity in
[type-three finite transport](research_mixed_three_first_source_transport.md),
equation (7). It is independent of the Newton index and of its height.
The original logarithmic lift is retained.

Every complex transform-index current used in the completed terminal
proof lies in
\[
             K_t=[.15,.5]+i[-.12,.12].
 \tag{5}
\]
Write \(P=p+i\beta\), \(C=u_0+iv_0\). On (1),
\(0<p<1\) and \(\beta>-.37\). The latter lower bound only
uses the possible positive heights \(k\le.068\); the extra
negative attached height allowed in (1) is favorable. For
\(\Re t<.5\), one has \(u_0>0\), and the imaginary numerator
of the ratio in (4) is
\[
                       u_0(1+\beta)+p(1-v_0).
 \tag{6}
\]
It is positive when \(v_0\le1\). Otherwise the original
cotangent calculation, even on the larger rectangle with lower
height \(-.2\), gives
\[
 \frac{v_0-1}{u_0}
 \le\frac{\cos(.3\pi)-e^{-.4\pi}}{\sin(.3\pi)}
 <\frac7{16}<\frac{63}{100}.
 \tag{7}
\]
Thus (6) stays positive. At \(\Re t=.5\),
\(u_0=0\) and \(|v_0|<1\); the same positivity follows
from \(p(1-v_0)>0\). The right-half-plane logarithms in (4)
have their continuous boundary values there and never encounter zero.
Their difference therefore satisfies
\[
 0<\Im\mathcal T_a<\pi,\qquad
 \Re\mathcal T(a_k;t,u)
       \le\Re\mathcal T(y+ic;t,u)+a_c(k).
 \tag{8}
\]
All summed primitive arguments remain in their original regular
strips. The residue penalties depend only on the index coordinates,
so the same inequality holds after each alias penalty is subtracted.

## 3. Physical transform rows transport exactly

For \(X=e^{-2\pi i(y+ik)}\), the entire dependence of a
physical outer row on the incoming parameter is
\[
                         X^{-i}p_i(X).
 \tag{9}
\]
This remains an exact factor if its Newton sum is kept coherent,
if it is written as a positive double-row majorant, or if a residue
contour is used only for its Newton index.

The exact finite Poisson identity from the same type-three transport
proof gives
\[
 \partial_k\log|X^{-i}p_i(X)|=
 \begin{cases}
 -\pi i-\pi\displaystyle\sum_{j=1}^{i}
                  P_{e^{2\pi k}}(y+j/N),&k<0,\\
 -\pi i+\pi\displaystyle\sum_{j=1}^{i}
                  P_{e^{-2\pi k}}(y+j/N),&k>0,
 \end{cases}
 \quad P_r(x)=\frac{1-r^2}{1+r^2-2r\cos2\pi x}>0.
 \tag{10}
\]
Integration in the attenuation direction, using \(0\le i<N\),
yields the literal inequality
\[
 |X_k^{-i}p_i(X_k)|
          \le e^{Na_c(k)}|X_c^{-i}p_i(X_c)|.
 \tag{11}
\]
It extends by continuity to \(k=0\), including any new physical
zero. At \(i=0\) it is immediate. No division by a vanishing
factor or approximation of a logarithmic product is used.

## 4. Transport the completed decomposition, not just its sum

Keep all cuts, shifted horizontal paths and alias contours from
[whole terminal completion](research_mixed_terminal_three_full_completion.md)
at their original reference values. Its proof first splits the
physical outer half, removes the coherent end-index sector before
any Newton restriction, and then treats the retained rectangle and
its complement exactly. At the horizontal baseline \(y+ic\),
each central zero-mode current has upper rate \(B_0\); its
noncentral currents and real sectors have strict bare gaps below it.

Every part of this finite decomposition is covered by one of the
following two alternatives:

* If the transform index is complex, it lies in (5). This includes
  the central double-residue currents and the transform contours for
  the Newton exterior strips. Equation (8) applies to each phase,
  with all zero-mode, join and alias penalties unchanged.
* If the transform index is physical, (9) is an exact factor.
  This includes the whole coherent lower end sector, positive
  low/high/near-half Newton bounds, left strips with a Newton contour,
  the upper-cut column, real corner regions, and the complete right
  triangle. Equation (11) transports the existing per-row or
  positive-majorant estimates. It does not require an absolute bound
  for a partial Newton sum whose proof used cancellation.

The old finite interpolants are still valid at the changed incoming
parameter, on the same regular compact sets. Their symbols have the
same leading phases and polynomial prefactors. Combining (8), (11)
with those baseline bounds proves (3), after one total source and
color tolerance. There is no assumption that an error small before
the outer sum stays small after it: every exact current or sector
has been transported separately. Cauchy on a smaller fixed color
disk proves the derivative statement.

## 5. The three-vertex first collar with a second type-three block

Consider a length-three word \((3+\alpha,3,3)\),
\(\alpha=0,1\). The exact contracted integrand is
\[
 U_{\alpha,N}(w_L,X_1)C_{0,N}(X_1,X_2)
 \mathcal V_{0,N}(w_R,X_2)
                 d_N(X_1)^\alpha X_1^{-N\sigma_1},
 \qquad \sigma_1\in\{0,\alpha\}.
 \tag{12}
\]
Use the full first collar \(x_1\in[0,\rho]\), the physical
unselected second attenuation \(k\) between \(c_2\) and zero,
and any \(y_2\in I_3\). The second coordinate is ordinary,
so the original pair geometry has \(-.065<c_2<.068\).

The first-pair tangent proof in
[horizontal tangent cancellation](research_mixed_first_collar_horizontal_tangent.md),
Sections 2--4, applies verbatim to this actual ordinary second
coordinate. Its argument uses only the first cap and first
conditional pair; the former restriction to a cut \(h\ge3\)
ensured that coordinate two was ordinary, which is also true here.
If \(M_{12}\) is its allocated reference action and
\(p=\Re P_2\) its second marginal, it gives
\[
 U_{\alpha0}(k)+a_{c_2}(k)
 < M_{12}+p(y_2-a_2)-\delta_{\alpha0},
 \qquad\delta_{00}=3/100,\quad\delta_{10}=3/125.
 \tag{13}
\]
The full first Fourier weight, all first-cap private rows and the
entire first conditional sum are included in this ceiling.

Multiplying (3) and this first-pair bound cancels the actual second
tangent, since
\(P_2+\mathcal P_0'(r_2)=0\), and adds the reference actions
to \(M_{\rm open}\). Thus (12) has upper rate
\[
 M_{\rm open}-\delta_{\alpha0}+\tau
                -\kappa_*(y_2-a_2)^2+O(\log N/N).
 \tag{14}
\]
Taking one total \(\tau<1/250\) leaves common loss \(1/50\).
Both first selections, the whole terminal transform, both level
parities, fixed ordinary-color neighborhoods at both ends, and all
fixed ordinary derivatives are retained. This is the full source
on this collar sector, with no missing terminal-index condition.

The transport theorem itself is independent of word length, but this
last corollary treats only the two specified length-three collars.
A type-four retained input needs its actual Fourier halfweight and
selected-path budget; neither is inferred from the bare type-three
argument. For length two a first collar places the sole retained
real coordinate near zero, outside the input interval (1), so this
deduction makes no corresponding length-two collar claim. General
selected or nonplateau boundary configurations remain separate.
