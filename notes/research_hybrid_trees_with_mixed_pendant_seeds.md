# Hybrid tree fillings with mixed pendant pieces

The hybrid tree theorem remains valid when any number of its terminal
pieces are replaced by the proved mixed tangle
\(T(R^{-2}T(R^2))\), or its mirror. The two short powers inside such a
piece are kept together. Each piece has one free interface and counts
as one child at the next vertex.

The analytic step is a finite enlargement of the initial family in
[the hybrid tree theorem](research_hybrid_tree_filling_closure.md).
Its geometric justification also needs the original embedded
punctured-disk interface. That requirement is supplied by
[the pure mixed geometry](research_mixed_pure_carrier_geometry.md)
and [the relative seam theorem](research_marked_pants_seam_isotopy.md).
We spell out the common constants, the source normalization and the
scope of the resulting knot theorem.

## 1. The initial pieces and the exact construction

Work in the original algebra
\[
 \mathcal A_N=\mathbb C[z]/P_N(z),\qquad
 P_N(z)=2T_N(z/2)+2,
\]
with the original crossing \(R\), Newton reversal \(T\), full
functional \(\phi_N\), and complete kernel
\[
 K_N(t,u)=\sum_{j=0}^{N-1}e_j(-2\cos t)e_j(-2\cos u).
 \tag{1}
\]
Here \(T_N\) is the standard Chebyshev polynomial. A boundary source
means the canonical representative of degree at most \(N-1\),
evaluated at \(z=-2\cos u\). In particular, it specifies both values
and first normals at the repeated roots of \(P_N\).

The allowed initial one-boundary pieces are
\[
\begin{split}
 H_{p,N}(u)&=\phi_N^{(t)}[R^pK_N(t,u)],\qquad |p|\ge2,\\
 Z_{+,N}(u)&=\operatorname{can}\bigl(T(R^{-2}T(R^2))\bigr)(-2\cos u),\\
 Z_{-,N}(u)&=\operatorname{can}\bigl(T(R^2T(R^{-2}))\bigr)(-2\cos u).
\end{split}
 \tag{2}
\]
Use each \(Z_\pm\) with its original pure reference interface:
there is no extra crossing at its free circle. Its two internal
powers and all its original markings belong to the piece.

Take a finite ordered rooted tree whose leaves are pieces from (2).
At each nonroot vertex above those leaves, include every child and
one outgoing bare edge, with the exact source
\[
 F_{\mathrm{new},N}(u)=
 \phi_N^{(t)}\!\left[
       R^n K_N(t,u)\prod_{\nu=1}^m F_{\nu,N}(t)\right],
                         \qquad m\ge1.
 \tag{3}
\]
At the final root omit the outgoing edge:
\[
 \mathcal Z_N=
 \phi_N^{(t)}\!\left[R^{n_{\mathrm{root}}}
                       \prod_{\nu=1}^mF_{\nu,N}(t)\right],
                         \qquad m\ge1.
 \tag{4}
\]
Products in these formulas are the original products before
applying the full trace. Reducing them for an exact algebra
calculation is legitimate, but their estimates use the raw
products and retain all first normals.

This is a tree of specified pieces. Expanding a mixed leaf restores
its original two adjacent filled vertices. They are not new
vertices to which the eligibility rule below must be applied.
The attaching vertex sees that whole leaf as one child.

**Theorem 1.** There are finite integers \(M_{\mathrm{mix}}\ge3\)
and \(B_{\mathrm{mix}}\ge2\) such that the following holds.
At every vertex in (3), and at the root in (4), require
\[
             m\ge M_{\mathrm{mix}}
                 \quad\hbox{or}\quad |n|\ge B_{\mathrm{mix}}.
 \tag{5}
\]
The high-valence alternative permits every fixed signed integer
\(n\), including \(0,\pm1\). The terminal powers in (2) may be any
fixed integers of magnitude at least two. The number, placement
and signs of mixed leaves are arbitrary.

Every nonroot source has a nonzero holomorphic expansion
\[
 F_N(u)=\epsilon_N A(u)e^{NW(u)}
                  (1+O_F(N^{-1})),\qquad |\epsilon_N|=1,
 \tag{6}
\]
on one common complex disk. It has the common phase curvature
and whole-period Gaussian bounds in Section 2. The final source
has
\[
 \mathcal Z_N=\Omega_N N^{3/2}D_0e^{N\mathcal S}
                    (1+O_{\mathrm{tree}}(N^{-1})),
           \qquad |\Omega_N|=1,\quad D_0\ne0.
 \tag{7}
\]
These assertions include both level parities. The two thresholds
and the invariant domains are independent of tree size, depth,
the number of mixed leaves and all allowed seed powers. The
entire finite tree and its powers are fixed before \(N\) tends
to infinity. Amplitude sizes, error constants and starting
levels may depend on that fixed tree.

For the original marked attachments satisfying the knot component
test in Section 4, the action in (7) satisfies
\[
                  2\pi\Re\mathcal S
                         =\operatorname{Vol}(S^3\setminus K).
 \tag{8}
\]

## 2. A common class for all initial pieces

The [uniform terminal theorem](research_uniform_terminal_family_and_star_fillings.md)
provides a common disk, a common disk without amplitude zeros,
uniform bounds on \(W_p-W_p(0)\), positive real curvature,
and constants \(c_T,C_T,h_T>0\) for the whole-period strip.
Its geometric charts are also uniform over \(|p|\ge2\).
The terminal scalar \(\epsilon_{p,N}\) remains the one in that
theorem; it is not absorbed into a new power at an attaching
vertex.

The [mixed boundary theorem](research_mixed_two_crossing_boundary_theorem.md)
gives
\[
 Z_{\pm,N}(u)=A_\pm(u)e^{NS_\pm(u)}(1+O(N^{-1})).
 \tag{9}
\]
Its power of \(N\) is zero and its unit scalar is exactly one.
The amplitudes are nonzero on fixed disks. The mirror germs are
\[
 A_-(u)=\overline{A_+(\overline u)},\qquad
 S_-(u)=\overline{S_+(\overline u)}.
\]
Both satisfy the same whole-period bound with constants
\(c_Z,C_Z,h_Z>0\). Moreover,
\[
 S_+''(0)=-\frac{\tan(\pi y_*)}{2\pi},\qquad
                         \Re\tan(\pi y_*)>0.
 \tag{10}
\]
Continuity therefore supplies a positive curvature bound on
one smaller closed disk for both signs.

Here is a choice of constants that makes the enlargement
independent of all later trees. First choose \(R>0\) so that
the closed disk \(|u|\le2R\) lies strictly inside all the
following domains:

* the common terminal source, nonzero amplitude and geometric
  charts;
* the two mixed source, nonzero amplitude and pure geometric
  charts, including the original relative seam;
* the bare-edge charts and centered kernel domain used in
  equations (7)--(8) of the hybrid theorem.

All are fixed positive domains; there are only two new pieces.
Shrink \(R\) once so that
\[
 -\Re S_\pm''(u)\ge a_Z>0,\qquad
 \Re[-\psi''(t,u)]\ge a_e^* I>0,\qquad
 \left|-\frac{2\pi\psi_t(t,u)}t-1\right|\le\frac1{100}
 \tag{11}
\]
on the respective closed disks. The quotient at \(t=0\) is
removable. Retain the terminal lower bound \(a_T>0\) there.
Set
\[
\begin{split}
 a_0&=\min(a_T,a_Z,a_e^*),\\
 H_{\mathrm{seed}}&=
 \max\left\{
  \sup_{\substack{|p|\ge2\\|u|\le2R}}|W_p(u)-W_p(0)|,\
  \max_{\sigma=\pm}\sup_{|u|\le2R}|S_\sigma(u)-S_\sigma(0)|
                         \right\},\\
 H&\ge\max\left\{H_{\mathrm{seed}},\
            2R^2\sup_{|t|,|u|\le2R}|\psi_u(t,u)/u|\right\}.
\end{split}
 \tag{12}
\]
Only the normalized phases are bounded. Their growing complete
values are not part of \(H\).

Use the full edge constants \(c_e,C_e',h_e,\gamma_e,\gamma_w\)
from the hybrid theorem, and put
\[
 \gamma=\min(c_e/2,a_e^*,\gamma_w),\qquad
 \Delta=\gamma(1-\cos(R/4)),\qquad L_2=2H/R^2.
\]
Choose
\[
\begin{split}
 0<c&\le\min(c_T,c_Z,c_e,\gamma/2,\Delta/8,a_0/4),\\
 C&\ge\max(C_T,C_Z,C_e',L_2^2/a_0+L_2/2).
\end{split}
 \tag{13}
\]
Finally choose \(0<h<\min(h_T,h_Z,h_e,R/2)\) sufficiently
small for the fixed interval Green-function inequality (13)
of the hybrid theorem. These choices give the common class
\[
\begin{split}
 |W(u)-W(0)|&\le H,\qquad -\Re W''(u)\ge a_0
                                     &&(|u|\le2R),\\
 |F_N(x+iy)|&\le C_FN^{d_F}
   e^{N\{\Re W(0)-c(1-\cos x)+Cy^2\}}
                                     &&(|x|\le\pi,\ |y|\le h).
\end{split}
 \tag{14}
\]
Each member also has (6) on a neighborhood of the closed disk,
with nonzero amplitude there. There is no uniform lower bound
on amplitude magnitudes, and none is needed.

For a fully specified threshold choice, insert precisely
\(R,H,a_0,c,C,h\) from (11)--(14) into equations (15)--(17)
of the hybrid theorem. Choose \(r,L_Q\) by its Taylor
majorant and let \(M_{\mathrm{mix}}\) be any integer satisfying
all its inequalities (17). After that choice, form \(L_b,C_b\)
and \(\delta_b\) from its equations (20)--(21), with
\(M=M_{\mathrm{mix}}\), and let \(B_{\mathrm{mix}}\) satisfy
all its inequalities (22). These are explicit inequalities in
the fixed constants just selected. Their left and right sides
have the same eventual ordering as in that proof, so both
thresholds are finite. No constant is chosen by examining a
particular tree or by iterating a radius reduction.

## 3. Why the same induction and normalization apply

The two closure proofs in the hybrid theorem use only (6),
(14), canonical boundary degree \(N-1\), and the marked
one-boundary interface. They do not use the internal formula
for a child. For high valence, the summed positive real
curvature supplies the central mass. For bounded valence and
a long power, the fixed raw-product degree bound supplies
the first-normal estimate at polynomial cost. Equations
(9)--(14) verify every one of those inputs for the new leaves.

In particular, inserting \(Z_\pm\) means inserting their whole
original boundary polynomials into (3). Their contour tails
have already been included in (9) and (14). The induction
uses the same complete physical trace, its outer nodes,
endpoint currents and all its charges. It does not apply a
turn to an unestimated remainder or replace \(Z_\pm\) by a
local critical contribution.

For clarity, write \(a_e\) for the leading edge amplitude.
At a vertex in (3), the selected critical point gives
\[
\begin{split}
 W_{\mathrm{new}}(u)
   &=\operatorname{stat}_t\left[
       \sum_\nu W_\nu(t)+\psi(t,u)
                      +\frac{in}{4\pi}t^2-it\right],\\
 A_{\mathrm{new}}(u)
   &=i\sqrt{\frac2\pi}\,
    \frac{\sin t_*(u)\,a_e(t_*(u),u)
                         \prod_\nu A_\nu(t_*(u))}
    {\sqrt{-\sum_\nu W_\nu''(t_*(u))
                    -\psi_{tt}(t_*(u),u)-in/(2\pi)}}.
\end{split}
 \tag{15}
\]
The square root has the original Gaussian continuation.
The selected point remains in the fixed inner child disk;
the numerator and denominator in (15) are nonzero.
Its unit is
\[
 \epsilon_{\mathrm{new},N}
       =C_{N,n}\prod_\nu\epsilon_{\nu,N},\qquad
 C_{N,n}=\exp\!\left(\frac{\pi i n(N-1)^2}{4N}\right).
 \tag{16}
\]
Use this explicit exponential, rather than an ambiguous
fractional power of a numerically evaluated root of unity.

Every child, including either mixed piece, has power \(N^0\).
The outgoing edge contributes \(N^{-3/2}\), the full trace
contributes \(N^2\), and its one-dimensional Gaussian
contributes \(N^{-1/2}\). Thus (15) again has power \(N^0\).
The envelope equation
\(W_{\mathrm{new}}'(u)=\psi_u(t_*(u),u)\) and the accretive
Schur complement restore (12), while the full edge estimates
restore (14) on the same disk and strip. None of these bounds
counts the number of descendants inside a mixed child.

At the final root let \(V(t)=\sum_\nu W_\nu(t)\). The same
selected trace, now without an outgoing edge, gives
\[
\begin{split}
 \mathcal S&=V(t_*)+\frac{in_{\mathrm{root}}}{4\pi}t_*^2-it_*,\\
 D_0&=i\sqrt{\frac2\pi}\,
     \frac{\sin t_*\prod_\nu A_\nu(t_*)}
          {\sqrt{-V''(t_*)-in_{\mathrm{root}}/(2\pi)}}\ne0.
\end{split}
 \tag{17}
\]
The remaining power is \(N^2N^{-1/2}=N^{3/2}\).
The final unit is obtained by applying (16) at the root as
well. Mixed leaves introduce no additional parity scalar.
All original terminal units remain. This proves (6)--(7)
through both parities, with the fixed-tree quantifiers stated
in Theorem 1.

## 4. Original markings and the knot conclusion

For a mixed leaf, the pure geometric result gives
\[
 U_0=-2\pi S_\pm'(u),\qquad V=2iu,
       \qquad \operatorname{Vol}(M_{\pm,0})
                         =2\pi\Re S_\pm(0).
 \tag{18}
\]
The relative seam theorem identifies its ordered triangle
maps with the original oval's embedded twice-punctured disk,
preserving the labelled primitive curves and the framing.
This is the geometric input needed for attachment. A
matching boundary character alone would not supply it.

Apply [the recursive marked construction](research_recursive_marked_block_geometry.md)
to the finite tree of pieces. Both alternatives in (5)
place the whole new charge path in the inner child charts
on the unchanged outside disk. Thus every older filled
slope remains fixed and every previously positive geometric
piece is used in its proved deformation domain. At a new
vertex the original carrier occurs once, with
\[
                    n_v=\eta_v-2p_v.
 \tag{19}
\]
Its primitive disk longitude also occurs once; it is not
multiplied by the number of children. There is no extra
carrier at a mixed leaf's free interface and no compensating
shift of the parent's power.

The complete child volumes and the complete outgoing edge
volume give the initial value for each new Schläfli
integration. The outgoing edge term is absent at the final
root. Equations (18)--(19) and that integration identify
the real part of (17) with the volume of the original
filled complement. They prove (8), with all the original
primitive slopes.

Retain the literal strand tracing for the assembled ordered
tangles: it must give one main knot component and no internal
closed component. A pure mixed piece itself has no internal
closed strand component; this does not remove the global
test. Under that test and the original framing convention,
the reduced zero-framed Kashaev invariant is (4) times its
prescribed writhe unit. Hence
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|\langle K\rangle_N|
                         =\operatorname{Vol}(S^3\setminus K).
 \tag{20}
\]

The extension permits arbitrarily many mixed pendant pieces,
even when the two short internal powers in every one of them
have opposite signs. It supplies no two-boundary kernel for
putting that mixed word at an arbitrary internal position.
Vertices outside the specified pieces must still satisfy
(5). Consequently infinitely many short low-valence
assignments on a fixed template can remain outside this
theorem. Arbitrary adjacent short components and cofinite
coverage are not consequences of this enlargement.
