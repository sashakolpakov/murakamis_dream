# Finite real-period image boundaries and their source contours

Private written proof, 16 November 2026.

The original positive period image already has an exact description
by tilted minima of the compact angle energy. This note strengthens
its finite-boundary conclusion: on every bounded real-period set,
all angular heights, returns and square covectors are uniformly
bounded. Every boundary approach therefore has finite sharp corner
data. For a proper selected subset of a connected original tree,
complete outside vertices also prevent vanishing half-angle
observation factors.

These statements do not make the inverse image a whole quantum
contour. A general real family in that image meets genuine trace
poles at infinitely many levels. That fact diagnoses a required
detour problem, not an impossibility of transporting the original
cycle. The component containing the geometric center is not assumed
to contain this real family.

## 1. The fixed original tilted problem

Fix a finite connected original ordered circle tree, a nonempty
selected set \(S\), and all edges incident to \(S\), counted once.
Let \(m\) be the number of included edges. Outside angles are complete:
\(t_b=0\). Retain the original real signed powers \(n_v\), and a
fixed charge vector \(c_v>0\). The original integral marking
\(n_v=\eta_v-2p_v\), when present, is unchanged.

Use the canonical positive branches and write
\[
 t_v=s_v+ih_v,\qquad r_{v,e}=k_{v,e}+ig_{v,e},\qquad
 P_v(t)=\sum_{e\ni v}r_{v,e}-\frac{i n_v}{2}t_v.
 \tag{1}
\]
Every selected vertex has an incidence. The ambient angle body \(X\)
has coordinates \(s_v\) and all endpoint incidence variables \(g\),
with outside \(s_b=0\), and inequalities
\[
 |s_v|+2|g_{w,e}|<\pi,\qquad
 |s_w|+2|g_{v,e}|<\pi.
 \tag{2}
\]
Its compact closure uses the weak inequalities. Put
\[
 \rho_v=\sum_{e\ni v}g_{v,e}-n_vs_v/2,\qquad
 \overline{\mathcal P}_c
       =\{z\in\overline X:\rho_v(z)=-\pi c_v\}.
 \tag{3}
\]
Assume a strictly feasible assignment \(\bar z\in X\) with these
rows is supplied. A positive original solution supplies one.

For an oriented edge the two square coordinates are
\[
 A_P=s_v/4-g_{w,e}/2,\quad A_Q=s_v/4+g_{w,e}/2,\qquad
 y_P=g_{v,e}/2+s_w/4,\quad y_Q=g_{v,e}/2-s_w/4.
 \tag{4}
\]
Let \(E_\square\) be the original square energy and
\[
 \mathcal E=4\sum_e(E_{P,e}+E_{Q,e}),\qquad
 E_{\max}=4mG_{\rm Cat},\qquad 0\le\mathcal E\le E_{\max}.
 \tag{5}
\]
There is no outside imaginary-work term. Set
\[
 \alpha=\min_{\text{square coordinates at }\bar z}
                    (\pi/4-|\text{coordinate}|)>0.
 \tag{6}
\]

For \(u\in\mathbb R^S\), let
\[
 z_u=\operatorname*{argmin}_{\overline{\mathcal P}_c}
                      \{\mathcal E(z)-u\cdot s(z)\},\qquad
 \Xi_c=\{u:z_u\in X\}.
 \tag{7}
\]
The pinned inverse-period theorem proves uniqueness and continuity
of these closed minimizers. Its proof applies unchanged to the
fixed rows (3): only their constant right sides change. It also
identifies \(\Xi_c\) exactly with the real parameters for which
the original positive equations
\[
                            P(t)=u-\pi i c
 \tag{8}
\]
have a solution. That solution is unique and analytic on \(\Xi_c\).
No convexity or connectedness of \(\Xi_c\) is assumed.

At an interior minimizer the exact ambient gradient is
\[
                     d\mathcal E=u\cdot ds+\sum_{v\in S}h_v\,d\rho_v.
 \tag{9}
\]
Indeed the incidence gradients match the imaginary angles, including
zero at outside ends, while the real rows are
\[
                \sum_{e\ni v}k_{v,e}+n_vh_v/2=u_v.
 \tag{10}
\]
Equations (3), (10) are the two parts of (8).

## 2. Uniform finite-period bounds

Fix \(R\ge0\), put \(c_{\max}=\max_v c_v\), and define
\[
 \begin{aligned}
 H_R&=\frac{E_{\max}+2\pi R}{\alpha},\\
 K_R&=\max\left\{2R+(2c_{\max}+1)H_R,
                   \operatorname{arsinh}\bigl(\cosh(H_R/2)\bigr)\right\},\\
 L_R&=K_R/2+H_R/4 .
 \end{aligned}
 \tag{11}
\]

**Theorem 1.** At every positive solution with
\(u\in\Xi_c\), \(\|u\|_1\le R\),
\[
 \sum_{v\in S}|h_v|\le H_R,\qquad
 |k_{v,e}|\le K_R,\qquad
 |x_P|,|x_Q|,|B_P|,|B_Q|\le L_R.
 \tag{12}
\]
Outside heights and returns are zero. The bounds are independent
of the component of \(\Xi_c\).

**Proof.** At the solution choose one incidence at each selected
vertex. Starting at \(\bar z\), change its chosen incidence by
\(\alpha\operatorname{sgn}(h_v)\), and change no selected real
angle. Denote the result by \(y\); use sign zero when \(h_v=0\).
Each square coordinate changes by at most \(\alpha/2\).
Opposite endpoint changes affect its \(A\) and \(y\) coordinates
separately. Thus \(y\in X\), with square margin at least
\(\alpha/2\), and
\[
                   \rho_v(y)-\rho_v(z_u)=\alpha\operatorname{sgn}(h_v).
 \tag{13}
\]
This is an ambient comparison; \(y\) need not lie in
\(\overline{\mathcal P}_c\).

The supporting inequality for \(\mathcal E\), (9), and
\(|s_v(\bar z)-s_v(z_u)|<2\pi\) give
\[
 \alpha\sum_v|h_v|
 \le\mathcal E(y)-\mathcal E(z_u)
                   -u\cdot(s(\bar z)-s(z_u))
 \le E_{\max}+2\pi R.
 \tag{14}
\]
This proves the first estimate without assuming any sign of \(h_v\).

The original positive-prefix inequality is
\[
 \ell_{v,e}:=\Re(r_{v,e}\overline{t_v})>0
                                      \quad\text{when }t_v\ne0 .
 \tag{15}
\]
Here \(t_v=0\) is impossible: the canonical return identity
\[
             \sinh r_{v,e}=\tan(t_v/2)\cos(t_w/2),
                    \qquad |\Im r_{v,e}|<\pi/2
 \tag{16}
\]
would make all its returns zero, contradicting \(c_v>0\) in (8).
Pairing (8) with \(\overline{t_v}\) yields
\[
       0<\sum_{e\ni v}\ell_{v,e}
                =u_vs_v-\pi c_vh_v
                \le\pi|u_v|+\pi c_v|h_v|.
 \tag{17}
\]
Since \(s_vk_{v,e}=\ell_{v,e}-h_vg_{v,e}\) and
\(|g_{v,e}|<\pi/2\), for \(|s_v|\ge\pi/2\) we obtain
\[
               |k_{v,e}|
                  \le2|u_v|+(2c_v+1)|h_v|
                  \le2R+(2c_{\max}+1)H_R.
 \tag{18}
\]

If \(|s_v|\le\pi/2\), direct trigonometry gives
\[
 |\tan(t_v/2)|^2
   =\frac{\cosh h_v-\cos s_v}{\cosh h_v+\cos s_v}\le1,\qquad
 |\cos(t_w/2)|\le\cosh(H_R/2).
 \tag{19}
\]
Use (16) and
\(|\sinh(k+ig)|^2=\sinh^2k+\sin^2g\) to obtain
the other bound defining \(K_R\). At a complete outside end,
(16) gives its zero canonical return.

Finally the original square identities are
\[
 x_P=k_{v,e}/2-h_w/4,\quad x_Q=k_{v,e}/2+h_w/4,\qquad
 B_P=h_v/4+k_{w,e}/2,\quad B_Q=h_v/4-k_{w,e}/2.
 \tag{20}
\]
They give the last estimate. \(\square\)

The four generating tetrahedron moduli and their negative
reciprocals also remain in the fixed annulus
\[
       e^{-(K_R+H_R/2)}\le |Z|\le e^{K_R+H_R/2},
 \tag{21}
\]
by their original exponential formulas. This annulus does not
exclude real shapes or the value one.

## 3. Every finite image-boundary approach

**Corollary 2.** Suppose \(u_j\in\Xi_c\) tends to a finite
\(u_*\). The primal assignments tend to the unique closed
minimizer \(z_{u_*}\). Heights, returns and square covectors have
a jointly convergent subsequence, with (12). If \(z_{u_*}\)
is on the angle boundary, every noninterior square is a corner,
and at each such square
\[
 (A,y)=(\varepsilon_A\pi/4,\varepsilon_y\pi/4),\qquad
 U=\varepsilon_Ax>0,\quad V=\varepsilon_yB>0,\qquad
                         \sinh(2U)\sinh(2V)=1.
 \tag{22}
\]
The original charge, real-period and matching rows pass to the
limit without resetting their branches.

**Proof.** Continuity in (7) gives the primal convergence;
Theorem 1 and the bounded real coordinates give subsequential
compactness of all remaining quantities. An open-side square
would make one of
\[
 x=\tfrac12\operatorname{arsinh}(\tan(2A)\cos(2y)),\qquad
 B=\tfrac12\operatorname{arsinh}(\tan(2y)\cos(2A))
 \tag{23}
\]
diverge, contrary to (12). At a corner, pass to the exact identity
\[
                  \sinh(2x)\sinh(2B)=\sin(2A)\sin(2y).
 \tag{24}
\]
The signs of \(x,B\) are those of \(A,y\); bounded limits in
(24) therefore give exactly (22). All period and matching rows
are finite linear identities in these coordinates. \(\square\)

This strengthens the finite-boundary statement in the earlier
inverse-image theorem for complete outside data. It does not
assert uniqueness of the reconstructed corner covectors when
only the closed primal minimizer has been specified.

**Corollary 3 (proper-selection observation units).** If \(S\)
is proper in the connected original tree, then for each \(R\)
there is \(\delta_R>0\) such that, at every solution covered by
Theorem 1 and every selected vertex,
\[
 |\cos(t_v/2)|,\quad |\sin(t_v/2)|,\quad|\sin t_v|\ \ge\delta_R.
 \tag{25}
\]
No nonzero lower bound on \(|h_v|\) is asserted.

**Proof.** If the cosine bound failed, choose a sequence of
solutions with that cosine tending to zero. Theorem 1 and the
compact real-angle ranges give a joint subsequential limit.
The limiting angle at this vertex is \(t_v=\pi\) or \(-\pi\).
Use the division-free original identity
\[
 \sinh r_{v,e}\cos(t_v/2)
                  =\sin(t_v/2)\cos(t_w/2).
 \tag{26}
\]
Its bounded factors pass to the limit. Since the limiting sine
is \(1\) or \(-1\), every neighbor has \(\cos(t_w/2)=0\).
This propagates along the selected component to a complete
outside neighbor, where the cosine equals one. Every selected
component has such a neighbor because the original tree is
connected and \(S\) is proper. This is a contradiction.

If a half-angle sine tends to zero, its limiting angle must
be \(t_v=0\). Equation (26) makes every incident
\(\sinh r_{v,e}=0\). The closed range
\(|\Im r_{v,e}|\le\pi/2\) forces \(r_{v,e}=0\).
The limit of (8) would have imaginary part \(0=-\pi c_v\),
again impossible. The only additional zeros of \(\sin t_v\)
in the closed angular range are \(t_v=\pm\pi\), already excluded.
Compactness and finiteness of the vertices prove uniformity.
\(\square\)

The tangent variables are consequently bounded, and the original
relations
\[
             e^{\pm r_{v,e}}=\cos(t_w/2)(q_e\pm a_v)
 \tag{27}
\]
bound \(q_e\pm a_v\) away from zero. These conclusions do
**not** exclude \(q_e=\pm i\) at a general tilted corner.
Thus they do not prove boundedness of
\[
               x_e=\frac1{2\pi i}\log\frac{q_e+i}{q_e-i}.
 \tag{28}
\]
In particular the radial endpoint exclusion and two-square
matching theorem cannot be imported into this tilted image.
The estimates do not exclude finite tilted limits with
\(\Re t_v=\pm\pi\) and \(\Im t_v\ne0\). The remaining statement is compactness
of angles, returns and square covectors, with (22), rather
than properness of every face or stationary-wire chart.

## 4. A classical gap away from the center

Suppose in addition that \(0\in\Xi_c\), so the original charged
positive solution \(t^0\) is supplied. Retain the exact action
\[
 \Phi_c(t)=\sum_e\psi(t_v,t_w)
            +\frac{i}{4\pi}\sum_{v\in S}n_vt_v^2
            -i\sum_{v\in S}c_vt_v.
 \tag{29}
\]
The original edge identity of the inverse-descent theorem gives,
with \(M_\infty=\psi(0,0)=4G_{\rm Cat}/\pi\), on the entire
positive inverse slice,
\[
                \Re\Phi_c(t(u))
                   =mM_\infty-\frac{\mathcal E(z_u)}{\pi}.
 \tag{30}
\]
Indeed summing
\(\pi\Re\psi+4E_e-g_vh_v-g_wh_w=\pi M_\infty\)
and using \(\sum g_v=n_vs_v/2-\pi c_v\) gives (30).
This checks the charge normalization directly.

For every \(0<r\le R<\infty\),
\[
 \Delta_{r,R}
     :=\min_{r\le\|u\|_1\le R}
                    \{\mathcal E(z_u)-\mathcal E(z_0)\}>0.
 \tag{31}
\]
To prove it, use continuity of the closed minimizers and
compactness of the parameter annulus. Equality of energies
would force \(z_u=z_0\), the unique minimum of \(\mathcal E\).
Since \(z_0\) is interior, it could also minimize
\(\mathcal E-u\cdot s\) only if \(u\cdot ds=0\) on every
feasible tangent. The projection to selected \(s\) is
surjective: change one incidence per selected vertex to
restore its row. Hence \(u=0\), excluded in (31).

Thus finite image-boundary approaches away from the center
retain a strict calibrated classical action gap. At a regular
single-square image boundary satisfying the already proved
proper-selected-set Jacobian criterion, the inverse equations
continue locally through the wall. The continued cells need
not be positive, so the original convex argument does not
control an unrestricted continuation beyond that neighborhood.
At more general finite corners, (22) alone supplies no such
continuation. No conclusion about the quantum source follows
from the classical gap without its actual contour estimates.

## 5. The real slice and actual trace poles

The full positive image is not generally confined to lower
angular heights. This is an exact general statement:

**Proposition 4.** Suppose \(n_v\ne0\) and
\(|n_v|>2c_v\) for every selected vertex. Then the real
configuration
\[
                         s_v=\frac{2\pi c_v}{n_v},\qquad t_v=s_v,
 \tag{32}
\]
with complete outside angles, lies on the positive inverse slice
for the real parameter \(u_v=\sum_{e\ni v}r_{v,e}(s)\).
Near that parameter the heights \(h_v\), as functions of the
real period coordinates, attain a neighborhood of zero.

At unit charge, if all \(|n_v|\ge3\) are odd, every odd level
\(N\) divisible by all \(|n_v|\) makes (32) an original angular
grid point at every selected vertex. The literal unit-coupon
factorial density has genuine trace double poles there.

**Proof.** The angles in (32) lie in \((-\pi,\pi)\).
All tangents \(a_v\) are real, and
\(q_e=\sqrt{1+a_v^2+a_w^2}>\sqrt{a_v^2+a_w^2}\);
thus every original edge is positive and its returns are real.
The imaginary part of \(P_v\) is
\(-n_vs_v/2=-\pi c_v\), proving (8).

At this real point the complex period Jacobian is
\[
                 J=A-iD,\qquad A=A^{\mathsf T}>0,\qquad
                              D=\operatorname{diag}(n_v/2).
 \tag{33}
\]
The real return matrix \(A\) is positive definite by original
edge monotonicity. The inverse-period height derivative is
the real symmetric matrix
\[
          \frac{\partial h}{\partial u}
                 =\Im(J^{-1})=J^{-*}D J^{-1}.
 \tag{34}
\]
It is invertible since \(D\) is. The real inverse-function
theorem proves the local height assertion.

For the stated odd common-multiple levels, the integers
\[
                        2j_v+1=N-\frac{2N}{n_v}
 \tag{35}
\]
are positive, odd and less than \(2N\). Thus (32) equals
\(\tau_{j_v}=\pi-(2j_v+1)\pi/N\), the actual physical
angular grid. The factor
\[
                 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2},
                          \qquad \eta=(-1)^{N-1},
 \tag{36}
\]
has a double pole there.

There is no cancellation of these poles by the literal local
factorials. At the real stationary wire,
\[
 \frac{\pi}{2}-\pi x_e=\arctan q_e>|s_v|/2,
 \qquad
             0<\tfrac12-x_e\pm\frac{s_v}{2\pi}<1.
 \tag{37}
\]
Consequently every shifted factorial argument
\(N(1/2-x_e\pm s_v/(2\pi))-1/2\) lies in \((-1,N)\),
and \(Nx_e\in(0,N)\). All the original \(B_N\)'s are
exact units. Also \(\sin s_v\ne0\), the unit coupon is one,
and the crossing Gaussian is a unit. This proves the last
assertion about the specified density. \(\square\)

Proposition 4 does not show that this real point belongs to the
component of \(\Xi_c\) containing \(u=0\). Nor does the presence
of poles forbid a valid cycle: it requires prescribed detours
and retention of their residue or endpoint currents. On a
compact regular phase chart, displacements of size \(O(1/N)\)
change its exponential phase by only \(O(1)\); this observation
is not an estimate for the entire original factorial network.
Competing modes and the actual meromorphic factors still require
their own coherent bounds.

For the original source the allowed relative boundary remains
the one in the joint-lens theorem: fixed angular endpoint faces
and fixed wire seams, with free cardinal ends unchanged. A finite
corner image is not one of those prescribed source faces merely
because the classical positive cells degenerate there. The
compactness and gap proved above therefore leave a precise
global task: construct the connecting relative chain, including
all necessary pole detours and wire faces, and control its
complete source. No such homology or remainder statement is
inferred in this note. A literal factorial density is deployed
as the original source only under its traced-end convention
or a separately proved boundary adapter.

## Direct sources and author readback

* [Positive inverse-period descent](research_positive_period_inverse_descent.md),
  SHA256 b9b5c3d61c704700e9431315cf50591c921ebeb95becdf6a52877606bdbc4565:
  the exact tilted image, continuous unique minimizers, action
  calibration and already proved compact collars. Complete text read.
* [Radial compactness and sharp corners](research_radial_charge_compactness_and_corners.md),
  SHA256 744d36368876f255df6e2b1f2ca15dd23e805d5d5a39b009f6983fec2c6243ec:
  original square identities, positive prefix pairing, ambient energy
  bound and sharp-corner argument. Complete text reread.
* [Positive wire product domain](research_positive_wire_product_contour.md),
  SHA256 5646f2d6b2a8dfa2d8c49662d17f19f3743fc4efcaf3c3685c6a899975a4c230:
  real positive-edge criterion, original stationary wire and exact
  factorial unit strip. Complete read retained at the unchanged hash.
* [Joint factorial-lens source](research_joint_factorial_lens_relative_source.md),
  SHA256 a14ca148bd55b36b1eea9de8be8a63025532c3bbbb928482b0d7cb8edae56e54:
  actual grid, trace poles, normalization, fixed relative faces and
  traced-versus-free endpoint convention. Complete read retained.
* [Regular-corner period assembly](research_regular_corner_period_assembly.md),
  SHA256 7d551e90d04b7c45232074109581bf2a807569259f98ad81e00855bec7f51ce5:
  the limited local continuation statement used after (31).
  The complete prior peer readback is retained.

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical calculation, test or compilation
was run. Frozen notes, manuscripts and public documents were unchanged.
