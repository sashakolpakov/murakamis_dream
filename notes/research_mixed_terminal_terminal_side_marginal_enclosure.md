# Enclosing the terminal marginal from its terminal-side variables

Research deduction, 6 November 2026.

The original allocated terminal marginal has an existing representation
using only the terminal transform index and the shared retained leg.
This note applies a whole-family Taylor enclosure to that representation.
Its posterior error uses the transform-index radius instead of the
ordinary-index radius. Both radii and every required analytic value are
already certified. No smaller error or new comparison sign is assumed,
and the frozen source-cell protocol is unchanged.

## 1. The existing identity and its original lift

Fix either terminal type \(\epsilon=0,1\), the preceding own-four
ordinary block, and its canonical reference \(q_*(b)\) on \(D_4\).
Use the notation and original stationary branches of
[the joint-main theorem](research_mixed_terminal_joint_main_budget.md).
The allocated terminal marginal is
\[
 p_T=(P_\epsilon-g/2)'(a_*).
 \tag{1}
\]
The terminal phase depends explicitly on its incoming leg through
\(g(a+t)-g(a)+2\pi iat\). Its internal derivatives vanish on the
original terminal critical branch. Differentiation before elimination
therefore gives
\[
 \begin{split}
 P_\epsilon'(a_*)&=g'(a_*+t_*)-g'(a_*)+2\pi it_*,\\
 p_T&=g'(a_*+t_*)-\tfrac32g'(a_*)+2\pi it_*.
 \end{split}
 \tag{2}
\]
This is already proved in
[the terminal tail theorem, equation (11)](research_mixed_terminal_transform_tails.md)
and [the terminal height-sign theorem, equation (3)](research_mixed_terminal_height_tangent_sign.md).
It was also used by the
[original canonical diagnostic, equation (11)](research_mixed_terminal_horizontal_envelope_diagnostic.md).
No transposition of localized finite currents is involved.

Define two explicit holomorphic functions, without imposing stationarity
on their arguments:
\[
 \begin{split}
 P^{\mathrm T}(t,a)&=g'(t+a)-\tfrac32g'(a)+2\pi it,\\
 P^{\mathrm O}(s,a)&=\tfrac32g'(a)-g'(s+a).
 \end{split}
 \tag{3}
\]
The second is the representation used in the completed
[joined-plane estimate](research_mixed_terminal_uniform_joined_plane.md).
Their exact difference is the original shared-leg residual:
\[
 P^{\mathrm T}(t,a)-P^{\mathrm O}(s,a)
   =g'(t+a)+g'(s+a)-3g'(a)+2\pi it=f_a(q;b).
 \tag{4}
\]
Consequently both equal \(p_T\) on the canonical family.
They need not agree at an enclosing midpoint or an arbitrary point
of a containing product. In particular \(f_a(q^0;b^0)\) is not
silently set to zero.

On the original regular strip put \(j(z)=\Log(2\sin\pi z)\). The
prescribed lifts give \(g'(z)=j(z)+i\pi(1/2-z)\). Thus
\[
 P^{\mathrm T}(t,a)
       =j(t+a)-\tfrac32j(a)+i\pi(t+a/2-1/4).
 \tag{5}
\]
This retains the chirp in (2), including its absolute linear term.
There is no logarithmic lift change or recovery of a lift from an
exponentiated equation.

## 2. A full affine-tube enclosure

Suppose a certified canonical family satisfies
\[
 t_*=t^0+u_t\delta+\zeta_t,\qquad
 a_*=a^0+u_a\delta+\zeta_a,\qquad
 |\delta|\le r=8/125,\qquad |\zeta_j|\le\eta_j.
 \tag{6}
\]
The centers and responses are exact Gaussian rationals. No stationarity
of \((t^0,a^0)\) is required. The
[whole-input affine theorem](research_mixed_terminal_all_input_affine_enclosures.md)
and its [quadratic refinement](research_mixed_terminal_quadratic_residual_refinement.md)
supply (6) for the two \(D_4\) families.

Assume the disks about \(a^0\) and \(t^0+a^0\), with radii
\[
 w_a=r|u_a|+\eta_a,\qquad
 w_{ta}=r|u_t+u_a|+\eta_t+\eta_a,
 \tag{7}
\]
are contained in saved regular disks on which
\(|g'''|\le m_a,m_{ta}\), respectively. In a saved-only
implementation the left sides may use outward modulus upper bounds;
their resulting radii must still be no larger than the saved disk
radii. This is a whole-tube containment check, before any restriction
of the actual root image to a source cell. It ensures every Taylor
segment stays on the original logarithmic branch.

With \(k=g''=j'-i\pi\), define
\[
 \begin{split}
 P^0_{\mathrm T}
   &=g'(t^0+a^0)-\tfrac32g'(a^0)+2\pi it^0,\\
 D_t&=k(t^0+a^0)+2\pi i=j'(t^0+a^0)+i\pi,\\
 D_a&=k(t^0+a^0)-\tfrac32k(a^0)
       =j'(t^0+a^0)-\tfrac32j'(a^0)+i\pi/2,\\
 L_{\mathrm T}&=D_tu_t+D_au_a,\\
 R_{\mathrm T}&=\tfrac12\{m_{ta}w_{ta}^2+\tfrac32m_aw_a^2\}.
 \end{split}
 \tag{8}
\]
The common coefficients \(u_t+u_a\) and \(D_tu_t+D_au_a\) are
formed before taking moduli.

Taylor's formula for the two \(g'\) terms, while the chirp is exactly
linear, gives the complex enclosure
\[
 P^{\mathrm T}(t_*,a_*)
 =P^0_{\mathrm T}+L_{\mathrm T}\delta
                     +D_t\zeta_t+D_a\zeta_a+\mathcal R,
 \qquad |\mathcal R|\le R_{\mathrm T}.
 \tag{9}
\]
It is valid at the nonstationary center because it expands the explicit
function (3); only its value at the actual canonical endpoint is
identified with \(p_T\).

Choose an exact real \(p_0\) and exact complex \(L_0\), with outward
bounds
\[
 |\Im P^0_{\mathrm T}-p_0|\le\rho_0,\qquad
 |L_{\mathrm T}-L_0|\le\rho_L.
\]
For example use the midpoints of their saved component enclosures,
with the corresponding certified component radius and modulus radius.
Then
\[
 \begin{split}
 |\Im p_T-p_0-\Im(L_0\delta)|&\le\rho_{\mathrm T},\\
 \rho_{\mathrm T}
   &=\rho_0+r\rho_L+\eta_t|D_t|^+
                          +\eta_a|D_a|^++R_{\mathrm T}.
 \end{split}
 \tag{10}
\]
The superscript \(+\) denotes a proved outward modulus upper.
The existing affine record already contains the center values of \(j\)
and \(j'\), and the full-curvature disks for the named primitive terms
\(t+a\) and \(a\). Since \(g'''=j''\), those are precisely the
analytic inputs in (5), (7)--(10). Their use requires no new logarithm,
cotangent, private action, derivative inverse or source evaluation.

## 3. Whole-disk and original-cell vertical supports

Let \(H=.01\), \(c=\Im a_*<0\),
\(\Delta=H-c\), \(\Delta_0=H-\Im a^0\), and let \(\Delta^+\)
be a certified upper bound for \(\Delta\).
The same exact disk calculation as in the old joined-plane proof
applies to (10):
\[
 \begin{split}
 \Delta\Im p_T\le U_{\mathrm T}:={}&
 \Delta_0p_0+r|\Delta_0L_0-p_0u_a|\\
 &+\frac{r^2}{2}\{|u_a||L_0|-\Re(u_a\overline{L_0})\}\\
 &+\Delta^+\rho_{\mathrm T}
              +\eta_a\{|p_0|+r|L_0|\}.
 \end{split}
 \tag{11}
\]
Indeed the quadratic term maximizes
\(-\Im(u_a\delta)\Im(L_0\delta)\) over the disk.
Its largest eigenvalue is the displayed nonnegative half-difference.
The last line pays the error in (10) and the posterior height error;
no independence of those errors is assumed.

If \(u_a\ne0\), define the exact coefficient \(\lambda=L_0/u_a\).
Substitution of (6) in (9) yields the useful alternative enclosure
\[
 \begin{split}
 \Im p_T&=p_0+\Im\{\lambda(a_*-a^0)\}+\widetilde e,\\
 |\widetilde e|&\le\rho_{\mathrm T}^*,\\
 \rho_{\mathrm T}^*
  &=\min\left\{
       \rho_{\mathrm T}+\eta_a|\lambda|^+,\quad
       \rho_0+r\rho_L+\eta_t|D_t|^+
                 +\eta_a|D_a-\lambda|^++R_{\mathrm T}
          \right\}.
 \end{split}
 \tag{12}
\]
For the sharper second bound, \(D_a\zeta_a-\lambda\zeta_a\)
is combined before its modulus is taken. The \(r\rho_L\) term
still pays \(L_{\mathrm T}-L_0\); it is not replaced by a derivative
evaluated on a clipped root image. The first bound follows directly
from (10), so taking their minimum is valid.

For an original source-cell intersection
\(J_C=[A_-,A_+]\times[c_-,c_+]\), put
\(a^0=A^0+ic^0\), \(\lambda=\lambda_R+i\lambda_I\). Then
\[
 \Delta\Im p_T\le
 U_{\mathrm T,C}:=
 \max_{(A,c)\in J_C}
 (H-c)\{p_0+\lambda_R(c-c^0)+\lambda_I(A-A^0)\}
                    +(H-c_-)\rho_{\mathrm T}^* .
 \tag{13}
\]
As in the [source-cell proof](research_mixed_terminal_source_cell_joined_plane.md),
this maximum uses only the two endpoints in \(A\).
For either endpoint define
\[
 b_A=p_0-\lambda_Rc^0+\lambda_I(A-A^0),\qquad
 f_A(c)=Hb_A+(H\lambda_R-b_A)c-\lambda_Rc^2.
 \tag{14}
\]
For \(\lambda_R>0\), evaluate at the clipped vertex
\((H\lambda_R-b_A)/(2\lambda_R)\).
For \(\lambda_R\le0\), take the larger endpoint value.
This remains exact for zero-width intersections.

The old ordinary-side and new terminal-side formulas enclose the same
actual marginal on the same canonical family. Therefore the minimum
of their separately proved whole-disk uppers, or their separately
proved cell uppers, is again valid. Their centers and linear coefficients
must not be interchanged: each bound must retain its own \(p_0,L_0\)
and full error. Neither an equality of their midpoint values nor an
improvement of the resulting upper is implied by stationarity.

## 4. Unchanged joined phase and evidence scope

Only the enclosure of \(\Delta\Im p_T\) changes. The joined-plane
value identities, cotangent-integral intervals, both selected-weight
alternatives, scalar costs, source-cell association and independent
target products remain exactly those of the old proof. In particular
the target variables are not restricted by (13); only the original
reference belongs to its source cell.

A future saved-only comparison could use (11) or (13) in the existing
trial-value formula and retain every other valid term. It would bind
the affine record, its exact posterior chain, original full-curvature
disks and the old integral/plane records; verify (7), \(u_a\ne0\) when
needed, and all case associations; then form only exact rational and
outward square-root bounds. No such calculation is made by this note.
It neither modifies the frozen pending protocol nor asserts a sign.

The marginal identities and affine enclosures apply on the canonical
whole \(D_4\). A finite-source application still uses the
[actual \(K_4\) source-domain theorem](research_mixed_terminal_canonical_source_domain.md).
The original action, lifts, chirp, incoming tangent and complete selected
weight are unchanged. A smaller posterior radius for \(t\) can help
(10)--(12), but the derivative coefficients and Taylor remainders
must also be paid. This deduction does not establish a full kernel
comparison or a new knot theorem.
