# Twelve phase families for the original terminal double residue cycle

Research criterion, 5 November 2026. This note reduces every alias of
the retained rectangular part of the type-three terminal Newton sum to
twelve explicit phase families. It uses the original simultaneous
interpolant and includes the vertical half-grid sides at height zero.
The twelve comparisons are hypotheses here, not completed estimates.
Eight single-alias families retain either zero or the actual height
of the unaliased index; four double-alias families complete the list.
The previously proved mixed-face comparisons control the remaining
height-zero endpoints. No new raw face with an independently free
unshifted index is required. If the twelve tests have a strict uniform
gap, the rectangular finite sum has the nonzero packet of its completed
zero mode. The real triangular complement is a separate obligation.

## 1. Source and the proposed comparisons

Use the original phase \(\mathcal T(a;t,u)\), interpolant
\(\mathcal I_N(a;t,u,w)\), and nonzero amplitude
\(\mathcal A(a,t,u)\) from
[the joint zero-mode theorem](research_mixed_terminal_three_joint_zero_mode.md),
equations (1), (15a)--(15e). In particular the positive logarithmic
lift of \((-q)^{-l}\), the chirp, and the literal factor \(N\)
in the exact Newton identity remain in \(\mathcal I_N\). Put
\[
 P=[11/50,9/20],\qquad I_t=[3/20,1/2],\qquad
 I_u=[1/10,2/5],\qquad \eta=3/25.
 \tag{1}
\]
At \(w=-2\), uniformly on the product with all three heights
in \([-\eta,\eta]\),
\[
 \mathcal I_N(a;t,u,-2)
 =N^{-2}\mathcal A(a,t,u)e^{N\mathcal T(a;t,u)}
       (1+O(N^{-1})).
 \tag{2}
\]
The same exact interpolation supplies a holomorphic, uniformly small
phase perturbation on a fixed ordinary-color disk near \(-2\).
All summed factorial arguments stay in compact regular strips;
their heights may reach \(2\eta\). This is the full double
summand, not an inner asymptotic inserted into an outer sum.

Fix an actual terminal reference \(a_*=A+iH\), with its original
critical point \((t_*,u_*)=(T+ih_t,U+ih_u)\) and calibrated action
\(\mathcal P_0\). The
[critical-curve identification](research_mixed_terminal_three_critical_curve.md)
gives \(\mathcal T_t=\mathcal T_u=0\),
\(\mathcal T=\mathcal P_0\), and
\(\mathcal T_a=\mathcal P_0'\) at that point. Write
\[
 B_0(a_*;y)=\Re\mathcal P_0(a_*)+
       \Re\mathcal P_0'(a_*)(y-A)-\kappa(y-A)^2,
 \qquad \kappa=1/2500000.
 \tag{3}
\]
The actual external reference may belong to either type. The actual
index ranges and their separation from all cuts are those in
[zero-mode completion, equations (4)--(5)](research_mixed_terminal_three_zero_mode_completion.md).
The reference enters the tests through \(H\), (3), and whichever
actual index height is retained. In **every** family all three real
targets \((y,x,z)\) range independently over \(P\times I_t\times I_u\).
The penalty belongs only to the index carrying a residue alias.

| Families | Tested phase | Subtracted penalty |
|---|---|---|
| Four transform-index single aliases | \(\Re\mathcal T(y+iH;x+i\epsilon\eta,z+i\sigma h_u)\), \(\epsilon=\pm1,\ \sigma=0,1\) | \(2\pi\eta\) |
| Four Newton-index single aliases | \(\Re\mathcal T(y+iH;x+i\sigma h_t,z+i\epsilon\eta)\), \(\epsilon=\pm1,\ \sigma=0,1\) | \(2\pi\eta\) |
| Four double aliases | \(\Re\mathcal T(y+iH;x+i\epsilon\eta,z+i\epsilon'\eta)\), \(\epsilon,\epsilon'=\pm1\) | \(4\pi\eta\) |

**Twelve-family hypothesis.** For some \(\delta>0\), every tested
phase minus its penalty is at most
\[
                         B_0(a_*;y)-\delta.
 \tag{4}
\]
When a uniform conclusion is desired, (4) is uniform over the stated
compact family of actual references. A stronger test over the original
auxiliary reference disks is permitted, but is not presumed to have
passed. In addition we use the already completed eight mixed-face
comparisons in [zero-mode completion, equation (7)](research_mixed_terminal_three_zero_mode_completion.md):
the two flattened transform faces \((c_t,z+ih_u)\), the two
flattened Newton faces \((x+ih_t,c_u)\), and four real-real
corners \((c_t,c_u)\). Their common strict gap is \(1/2000\).
These are not new hypotheses or additional alias families.

For an external type-four halfweight, set
\(\mathcal T_\nu=\mathcal T-\nu g(a)/2\) and
\(\Pi_{0,\nu}=\mathcal P_0-\nu g/2\), where \(\nu=0,1\).
Replace (3) by the corresponding plane \(B_\nu\).
Since \(\Re g(y+iH)\) is horizontally convex, subtracting this
halfweight changes the defect in (4) by a nonpositive Bregman
remainder. Thus the bare tests imply the allocated tests. Interpretation
as the physical Fourier halfweight for \(\nu=1\) uses the actual
negative type-four height, exactly as in the cited zero-mode theorem.
No Fourier factor is divided out, and no positive-height branch is
asserted on an auxiliary reference disk.

## 2. Exact one-variable splitting, including the zero-height sides

Let \(J_N=[c_N,d_N]\) have half-grid endpoints and let
\(\Gamma_N\) be its counterclockwise rectangle of heights
\(\pm\eta\). Its lower part \(\Gamma_N^-\) comprises the lower
horizontal side and the two vertical portions below height zero,
with their inherited orientations. Its upper part \(\Gamma_N^+\)
comprises the other three portions. For a holomorphic function \(f\),
define
\[
\begin{split}
 I_{J_N}f&=\int_{c_N}^{d_N}f(v)\,dv,\\
 A_{J_N}f&=\int_{\Gamma_N^-}(K_N(v)-1)f(v)\,dv
            +\int_{\Gamma_N^+}K_N(v)f(v)\,dv,\\
 K_N(v)&=(1-e^{-2\pi iNv})^{-1}.
\end{split}
 \tag{5}
\]
The residue of \(K_N\) is \(1/(2\pi iN)\), and Cauchy's
theorem on the lower half-rectangle gives
\(\int_{\Gamma_N^-}f=\int_{c_N}^{d_N}f\). Consequently the
literal finite summation functional is
\[
 \sum_{j/N\in(c_N,d_N)} f(j/N)
                  =N\bigl(I_{J_N}+A_{J_N}\bigr)f.
 \tag{6}
\]
This fixes the positive constant-mode coefficient and every side
orientation without an infinite alias expansion. It is the same
marked residue cycle as
[the original coefficient proof, equations (16)--(18)](research_complete_boundary_coefficient_asymptotic.md#4-exact-summation-aliases-and-the-nonzero-coefficient).

On horizontal sides, for all sufficiently large \(N\), the respective
kernels are bounded by \(2e^{-2\pi N\eta}\). On a half-grid
vertical side, \(c_N\in(\mathbb Z+1/2)/N\), the exact formula is
\[
 K_N(c_N+ih)=\frac1{1+e^{2\pi Nh}}.
 \tag{7}
\]
It follows that \(|K_N|\le e^{-2\pi Nh}\) for \(h\ge0\),
and \(|K_N-1|\le e^{-2\pi N|h|}\) for \(h\le0\).
At \(h=0\) both relevant absolute values are \(1/2\).
There is no pole, small-denominator loss, or omitted interval near
zero height. The value assigned at the one joining point does not
affect its contour integral.

Apply (6) successively to the original holomorphic double interpolant.
Let \(I_t,I_u,A_t,A_u\) now denote these functionals on the inward
half-grid intervals, not the limiting sets in (1). The rectangular
finite sub-sum is exactly
\[
 S_N^{\rm rect}(a,w)=N^2
   \{I_tI_u+A_tI_u+I_tA_u+A_tA_u\}\mathcal I_N(a;\cdot,\cdot,w).
 \tag{8}
\]
All enclosed lattice pairs satisfy \(i+l<N\), so the physical
support wall causes no extra term here. There are six oriented pieces
in each \(A\). Thus (8) retains twelve one-index alias currents and
thirty-six two-index alias currents, as well as the constant mode.
The twelve *phase families* above are not a count of these currents.
The coefficient \(+N^2\) in (8) is additional to the literal
factor \(N\) already contained in \(\mathcal I_N\).

## 3. Completeness after deforming the unaliased coordinate

The enlarged joint Hessian theorem gives
\[
 -\Re\mathcal T''\succ\frac{\pi}{100}I_3
 \quad\hbox{on }(P+i[-\eta,\eta])\times
       (I_t+i[-\eta,\eta])\times(I_u+i[-\eta,\eta]).
 \tag{9}
\]
In particular the real part is convex in each imaginary index
coordinate separately. On either sign half of an alias vertical side,
the kernel penalty \(2\pi|h|\) is affine. Hence the weighted
phase is still convex in that height and is bounded by its values at
height zero and height \(\pm\eta\).

For each constant-mode interval, deform its path to its actual
critical height, with its two oriented vertical joins:
\[
             I_t=H_t+J_t,\qquad I_u=H_u+J_u.
 \tag{10}
\]
Here \(J_t\) and \(J_u\) each denote the signed sum of the
left and right joins; their heights range between zero and the actual
height, of either sign. Only the **unaliased** coordinate is deformed
in each one-index alias term. Thus the exact alias part of (8) is
\[
 N^2\{A_tH_u+A_tJ_u+H_tA_u+J_tA_u+A_tA_u\}\mathcal I_N.
 \tag{11}
\]
The entire product remains in the original regular strips. The
residue kernel depends only on its own alias coordinate, so this
Cauchy deformation neither crosses a kernel pole nor creates a new
residue. It retains all contour terms. With six pieces in each
\(A\), one horizontal and two joins in each \(H+J\), the
formal count is \(18+18+36=72\) alias currents.

For \(A_tH_u\), an alias horizontal side has heights
\((\pm\eta,h_u)\), a tested single alias. On an alias vertical
side, convexity reduces to that family or \((0,h_u)\) with
\(t\) at a cut. The latter is a completed flattened transform
face, not a raw face with the other height released to zero.

For \(A_tJ_u\), convexity in the join height first reduces it
to \(u\)-height \(0\) or \(h_u\), with \(u\) at a cut.
An alias horizontal side is then a tested single alias with that
other height. If the alias side is vertical, its own endpoints add
only \((0,h_u)\) at two cuts or a real-real corner. Those are
contained in the completed flattened transform faces or corner
families. This argument includes negative or vanishing \(h_t,h_u\).
The terms \(H_tA_u+J_tA_u\) have exactly the reversed argument.

For \(A_tA_u\), two horizontal sides give a double alias.
One horizontal and one vertical side reduce to a double alias or
a single alias with the other height zero. Two vertical sides,
using convexity on each sign pair, reduce to those same families
or a real-real corner. This exhausts all endpoint combinations in
(11). In particular no raw face \((c_t,z)\) with free real
\(z\), or \((x,c_u)\) with free real \(x\), is needed.
The geometric-height single aliases have penalty \(2\pi\eta\),
not \(2\pi(\eta+|h_u|)\) or \(2\pi(\eta+|h_t|)\):
the retained geometric-height coordinate has no alias kernel.

For the inward half-grid cuts, the same argument is exact at their
actual values. A vertical cut differs from its limiting cut by at
most \(1/N\). Uniformly bounded phase derivatives on the regular
compact product give a rate change \(O(N^{-1})\). Horizontal
segments already lie in the tested intervals. The interpolant (2),
small ordinary-color perturbations, and bounded contour lengths now
prove the following.

**Proposition 1.** Assume (4), and put
\(\delta_0=\min(\delta,1/2000)\). For every
\(0<\delta'<\delta_0\), there is a fixed small ordinary-color
disk and an \(N_0\) such that the sum of all aliases in (8),
with the original allocation, has absolute value at most
\[
                   \exp\{N(B_\nu(a_*;y)-\delta')\}
 \tag{12}
\]
for \(N\ge N_0\), uniformly on the stated actual reference and
real-target family. Fixed ordinary-color derivatives satisfy the same
conclusion after choosing a smaller disk and reserving part of the gap.
The finite number seventy-two and all powers of \(N\) are absorbed
once. This does not assert transverse target-derivative bounds from
the real-target inequality alone.

## 4. Reference derivatives for a saved-cell comparison

The geometric-height variants require their original implicit
reference derivatives. They cannot be treated as fixed-height aliases
when the reference moves. The following formulas specify this dependence
without prescribing a numerical acceptance method.

Write \(d=y-A\). Use retention flags \(\sigma_t,\sigma_u\)
which equal one exactly when that coordinate retains its actual height.
A transform single alias has \(\sigma_t=0\), a Newton single
has \(\sigma_u=0\), and both flags vanish for a double alias.
At fixed real targets and fixed alias heights, define the bare defect
\(D=\Re\mathcal T-B_0-\text{penalty}\). With all phase
partials evaluated at the tested point, its real reference derivatives
are exactly
\[
\begin{split}
 D_A={}&-d\Re\mathcal P_0''-2\kappa d
 -\sigma_t\Im\mathcal T_t\,\Im t_*'
 -\sigma_u\Im\mathcal T_u\,\Im u_*',\\
 D_H={}&\Im(\mathcal P_0'-\mathcal T_a)
       +d\Im\mathcal P_0''
 -\sigma_t\Im\mathcal T_t\,\Re t_*'
 -\sigma_u\Im\mathcal T_u\,\Re u_*'.
\end{split}
 \tag{13}
\]
These follow from the original holomorphic reference branch:
\(\partial_A\Im t_* =\Im t_*'\),
\(\partial_H\Im t_* =\Re t_*'\), and likewise for \(u_*\).
The derivative of \(\Re\mathcal P_0\) cancels the derivative
of the supporting-plane displacement in the first line. The penalty
is constant in every family and contributes no response term.

At fixed reference, the real-target Hessian of \(D\) is the
entrywise real Hessian of \(\mathcal T\), plus \(2\kappa\)
in the external coordinate. By (9), its negative is bounded below by
\((\pi/100-2\kappa)I\), strictly greater than \((3/100)I\).
Thus a fixed-trial strict-concavity upper bound with curvature
\(3/100\) is legitimate for all three free real targets. This
algebra supplies an acceptance rule; it establishes no uniform sign
of the twelve defects by itself.

## 5. Conditional full rectangular packet and the remaining complement

**Theorem 2.** Assume (4). Then the *entire retained rectangular finite
sub-sum* (8), including all residue aliases, has the supporting-plane
upper rate
\[
 |\text{allocated }S_N^{\rm rect}(y+iH,w)|
       \le \exp\{N(B_\nu(a_*;y)+\varepsilon)\}
 \tag{14}
\]
for every fixed \(\varepsilon>0\), a sufficiently small fixed
ordinary-color disk, and sufficiently large \(N\). At the actual
target and complete color, before external allocation,
\[
 S_N^{\rm rect}(a_*,-2)=
 \frac{2\pi}{N}
 \frac{\mathcal A(a_*,t_*,u_*)}{\sqrt{\det H_*}}
 e^{N\mathcal P_0(a_*)}(1+O(N^{-1})),
 \qquad H_*=-\mathcal T''_{t,u}(a_*;t_*,u_*).
 \tag{15}
\]
The square root is the Gaussian branch on the accretive complex
symmetric matrices, and the leading coefficient is nonzero.

Indeed the constant mode in (8) has the packet proved in zero-mode
completion, including all of its joining currents.
The source factor \(N^{-2}\), residue coefficient \(+N^2\),
and two-dimensional Gaussian factor \(2\pi/N\) give exactly
(15). Proposition 1 makes every alias exponentially smaller at
\(y=A\). The proof works for both level parities. At independent
real targets only (14) is asserted; no new critical point there is
required.

The holomorphic ordinary-color continuation and fixed jets of the
completed zero mode transfer to (15), since the aliases remain
exponentially smaller on a fixed disk. In particular for every fixed
\(j\ge0\),
\[
 \left.\partial_w^jS_N^{\rm rect}(a_*,w)\right|_{w=-2}
 =2\pi N^{j-1}\frac{\mathcal A(a_*,t_*,u_*)}{\sqrt{\det H_*}}
 \left(-\frac{\tan\pi u_*}{4\pi}\right)^j
 e^{N\mathcal P_0(a_*)}(1+O(N^{-1})).
 \tag{16}
\]
The derivative coefficient is nonzero on the actual index range.
It follows from the literal ordinary Newton factor, not from a
derivative in either lattice index. No differentiation through a
Fourier square-root zero is involved.

The twelve uniform comparisons have not been established in this
note. Even after they are proved, (15) concerns the rectangular
sub-sum only. The retained physical triangle outside its inward cuts
still has to be combined with the separately controlled end-index
and low/high-Newton sectors. A nonzero rectangular packet alone does
not prove a nonzero leading coefficient for the full terminal
transform or the projected invariant.
