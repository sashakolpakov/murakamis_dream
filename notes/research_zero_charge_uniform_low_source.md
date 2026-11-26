# The zero-charge transition of the original low Newton source

Private written proof, 16 November 2026.

The original all-low zero-power source has a uniform nonzero formula
down to the first nonzero lattice charge. Its endpoint prefactor is
the product of the charges. This comes from the antisymmetric Fourier
differences in the full Hermite trace, not from replacing those
differences by Fourier coefficients. The proof also allows some
charges to stay in the interior while others tend to zero.

The archived regular low-source theorem gives the local edge symbol
and the interior Gaussian. The additional points here are compact
control on partially zero-charge faces, a fixed gap for higher aliases
without a positive lower bound on the heights, and analytic division
of the principal Fourier remainder. The interpolants used for the
last step agree with the actual source only on its lattice; they do
not assert an off-lattice cosine initializer.

## 1. Source, uniform formula, and endpoint coefficient

Keep a fixed finite tree and a nonempty connected proper selected set
\(S\), with every original selected degree \(d_v\ge3\). Every
selected crossing power is zero. Include every incident edge once,
and write
\[
 k=|S|,\qquad e=|E_S|,\qquad b=|\partial S|,
 \qquad p=\frac{3(b-1)}2,\qquad e=k-1+b.
 \tag{1}
\]
Every outside incidence remains an ordinary independent spectral
variable \(z_w=-2\cos u_w\). No reduction is made there.
Use the original Newton polynomials and full closing functional
\[
 e_a(z)=S_a^{-2}\prod_{j<a}(c_j-z),\quad
 S_a=\prod_{j=1}^a2\sin(\pi j/N),\quad
 c_j=2\cos((2j+1)\pi/N),
\]
\[
 D=N-1,\quad \eta=(-1)^D,\quad
 P_N(z)=2T_N(z/2)+2,\quad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f.
 \tag{2}
\]
All repeated-root first normals are retained. Put
\[
 K_N^{\rm low}(t,u)=\sum_{2a<N}e_a(-2\cos t)e_a(-2\cos u),
 \qquad
 F_N(\mathbf t;\mathbf u)=\prod_{vw\in E_S}K_N^{\rm low}(t_v,t_w).
 \tag{3}
\]
For \(\chi_v=J_v/N\), \(1\le J_v\le N\), the actual coupon is
\(\mathcal C_{N,\chi_v}=T_{N-J_v}(-z_v/2)\). Define
\[
 Z_N^{\rm low}(\boldsymbol\chi;\mathbf u)=
  \left(\prod_{v\in S}\phi_N^{(v)}\right)
       \left[F_N\prod_{v\in S}\mathcal C_{N,\chi_v}\right].
 \tag{4}
\]

Fix \(0<c_*<1\). Let \(\mathbf H(\boldsymbol\chi)\) minimize
\[
 M(\boldsymbol\chi)=\min_{\mathbf H\ge0}
 \left\{\sum_{vw\in E_S}V(H_v,H_w)
                 -\sum_{v\in S}\chi_vH_v\right\},\qquad H_w=0
 \quad(w\notin S),
 \tag{5}
\]
where, with continuous endpoint values,
\[
 J(x)=\int_0^x\log(2\sin\pi s)\,ds,
 \quad B(x,h)=\int_0^x\log(2\cos2\pi s+2\cosh h)\,ds-2J(x),
\]
\[
 V(h,g)=\max_{0\le x\le1/2}\{B(x,h)+B(x,g)\},
 \qquad V(0,0)=M_\infty=4G/\pi.
 \tag{6}
\]
All complete-edge constants in (5) are retained.

**Theorem 1.** On the closed charge cube \([0,c_*]^S\), the
minimizer in (5) is unique, all edges are regular, and the minimizing
configuration has a uniform regular neighborhood. There are a fixed
complex boundary polydisk \(U\) about \(\mathbf u=0\), a critical
action \(W(\boldsymbol\chi,\mathbf u)\), and a nonvanishing
coefficient \(\beta(\boldsymbol\chi,\mathbf u)\), locally
holomorphic in charges across every face of that cube, such that
\[
 W(\boldsymbol\chi,\mathbf0)=M(\boldsymbol\chi),\qquad
 \beta(\boldsymbol\chi,\mathbf0)>0,
 \tag{7}
\]
and, uniformly at both parities and at every nonzero lattice tuple
\(1\le J_v\le c_*N\),
\[
 \boxed{\quad
 Z_N^{\rm low}(\boldsymbol\chi;\mathbf u)
 =N^{-p}\left(\prod_v\chi_v\right)
     e^{NW(\boldsymbol\chi,\mathbf u)}
       \bigl(\beta(\boldsymbol\chi,\mathbf u)+O_{\rm hol}(N^{-1})\bigr).
 \quad}
 \tag{8}
\]
Here the error is holomorphic in the ordinary boundary variables,
uniform on a slightly larger polydisk than the one on which fixed
derivatives are taken. Thus (8) is a uniform relative estimate after
shrinking \(U\), and includes every fixed ordinary spectral boundary
derivative. No assertion is made that the error is the restriction
of one common off-lattice charged-source remainder.

At the completely zero charge corner,
\[
 \beta(\mathbf0,\mathbf0)
       =(2\pi)^k4^{-e}\prod_{v\in S}d_v^{-3/2}.
 \tag{9}
\]
Consequently, for each fixed \(C<\infty\), uniformly for
\(1\le J_v\le C\sqrt N\),
\[
 Z_N^{\rm low}(\mathbf J/N;\mathbf0)
 =N^{-p-k}\left(\prod_vJ_v\right)
       (2\pi)^k4^{-e}\prod_vd_v^{-3/2}
 \exp\left\{NeM_\infty-\frac\pi N\sum_v\frac{J_v^2}{d_v}\right\}
       (1+O_C(N^{-1})).
 \tag{10}
\]
This is the central Gaussian transition, with its original trace
normalization. In particular it includes every fixed positive
integer tuple \(\mathbf J\).

## 2. Geometry on all partially zero faces

The convex potential source proves continuity and convexity of
\(V\), its regular positive Hessian, and \(V(h,g)\ge(h+g)/2\).
Thus the functional in (5) is uniformly coercive on the closed cube:
\[
 \mathcal L_{\boldsymbol\chi}(\mathbf H)
       \ge\sum_v(d_v/2-\chi_v)H_v
       \ge(3/2-c_*)\sum_vH_v.
 \tag{11}
\]
If \(\chi_v=0\), a minimum has \(H_v=0\): every incident
potential is strictly increasing in its own positive height, whereas
there is no linear reward at that coordinate. The remaining positive
coordinates separate into selected components with the zero-height
vertices treated as complete ends. Their original degrees are
unchanged. The charge-cube theorem applies to each such component.
Its only exceptional saturated component requires two charges equal
to one, which is excluded by \(c_*<1\). Therefore every edge is
regular, including edges between two zero-height vertices.

The minimizer is unique: the positive components have their unique
minima, and the other heights have just been forced to zero. Uniform
coercivity and uniqueness imply continuity on the closed cube by
the convergent-subsequence argument for minimizers. Compactness now
gives a uniform strict regularity margin and uniform interior wire
indices \(0<x_e<1/2\).

On this compact regular set the edge potential extends analytically
and evenly in each signed height. Its Hessian is positive definite
after assembly, including at zero heights. The analytic implicit
function theorem therefore gives the continued minimizing branch
near every charge vector on the closed cube. The branches agree
on their real overlaps and hence on sufficiently small complex
overlaps. Reflection of one charge changes the sign of its own
height and leaves the other heights unchanged. In particular
\[
 H_v=0\ \Longleftrightarrow\ \chi_v=0,
 \qquad H_v/\chi_v\text{ extends to a positive analytic unit.}
 \tag{12}
\]
For the last assertion at a zero coordinate, the off-diagonal
entries in its Hessian row vanish by separate evenness. Its positive
diagonal entry gives \(\partial H_v/\partial\chi_v>0\).

Let \(\psi(t,u)\) and \(a_e(t,u)\) be the actual regular
low-edge phase and density, calibrated positively at imaginary
angles as in the regular low-source theorem. Define
\[
 \mathcal F(\mathbf t;\boldsymbol\chi,\mathbf u)
       =\sum_e\psi(t_v,t_w)-i\sum_v\chi_vt_v.
 \tag{13}
\]
Its critical point \(\mathbf t(\boldsymbol\chi,\mathbf u)\)
continues \(-i\mathbf H\); put \(W=\mathcal F(\mathbf t;\cdot)\)
and \(K=-\mathcal F_{\mathbf t\mathbf t}\) there. The square
root of \(\det K\) continues its positive value at real charges
and complete outside angles. Separate evenness shows that \(W\)
is even in a charge reflected across a zero face, and that
\(\sin t_v/\chi_v\) extends holomorphically. The coefficient in
(8) is
\[
 \beta(\boldsymbol\chi,\mathbf u)
 =\left(\frac{i}{\sqrt{2\pi}}\right)^k
   \frac{\displaystyle\prod_v\frac{\sin t_v}{\chi_v}
                        \prod_e a_e(t_v,t_w)}{\sqrt{\det K}}.
 \tag{14}
\]
It is positive on the real closed charge cube at \(\mathbf u=0\).
Compactness permits one common smaller \(U\) on which it is a unit.

## 3. Exact principal Fourier block and the other aliases

Write \(F_N=\sum_{\mathbf r}a_{N,\mathbf r}e^{i\mathbf r\cdot\mathbf t}\).
The coefficients are separately symmetric; at complete outside
angles they are nonnegative. For real outside angles their absolute
values have the coefficientwise majorant at complete outside angles.
Define the tensor antisymmetric difference
\[
 \Delta_{\mathbf q}a_N
 =\sum_{\boldsymbol\epsilon\in\{-1,1\}^S}
       \left(\prod_v(-\epsilon_v)\right)
                  a_{N,\mathbf q+\boldsymbol\epsilon}.
 \tag{15}
\]
The exact charged full-normal identity from the half-charge note is
the tensor product of
\[
 \phi_N(f\mathcal C_{N,J/N})
 =\frac{N^2}{2}\sum_{\ell\ge1}\ell\eta^{\ell+1}
 \left[
 a_{(\ell-1)N+J-1}-a_{(\ell-1)N+J+1}
 +a_{(\ell+1)N-J-1}-a_{(\ell+1)N-J+1}\right].
 \tag{16}
\]
It includes the original normal multiplier \(\ell N\), the odd
simple node, and the parity signs. The principal block is exactly
\[
             \mathcal P_N(\boldsymbol\chi;\mathbf u)
                   =(N^2/2)^k\Delta_{\mathbf J}a_N.
 \tag{17}
\]
Every other block has effective nonnegative charges
\(\lambda_v=(\ell_v-1)+\chi_v\) or
\(\lambda_v=(\ell_v+1)-\chi_v\). They satisfy
\(\boldsymbol\lambda\ge\boldsymbol\chi\), with at least one
excess at least
\[
                         a_*:=\min(1,2-2c_*)>0.
 \tag{18}
\]
Only a bounded number of these blocks can occur: the Laurent degree
at \(v\) is at most \(d_v(N-1)/2\), so their \(\ell_v\)'s are
bounded in terms of the fixed original degrees, independently of
\(N\).

Here is a uniform bound even when some minimizing heights vanish.
For any nonnegative \(\mathbf h\), coefficient positivity gives
\[
 |\Delta_{N\boldsymbol\lambda}a_N(\mathbf u)|
 \le\prod_v2\cosh h_v\,
       e^{-N\boldsymbol\lambda\cdot\mathbf h}
                       F_N(-i\mathbf h;\mathbf0)
 \quad(\mathbf u\text{ real}).
 \tag{19}
\]
The uniform endpoint factorial estimate in the half-charge note gives
\[
 F_N(-i\mathbf h;\mathbf0)
       \le C N^A\exp\left(N\sum_eV(h_v,h_w)\right)
 \tag{20}
\]
on every bounded nonnegative height box, including height zero.

Choose a coordinate \(v\) with \(\lambda_v-\chi_v\ge a_*\).
The compact regularity from Section 2 allows a fixed \(\epsilon>0\)
such that \(\mathbf H(\boldsymbol\chi)+\epsilon\mathbf e_v\)
remains in a regular bounded neighborhood for all charges in the
closed cube. If \(L\) bounds the height Hessians there, stationarity
gives
\[
 \mathcal L_{\boldsymbol\chi}(\mathbf H+\epsilon\mathbf e_v)
             \le M(\boldsymbol\chi)+L\epsilon^2/2.
\]
Since all heights and all excess charges are nonnegative,
\[
 \mathcal L_{\boldsymbol\lambda}(\mathbf H+\epsilon\mathbf e_v)
       \le M(\boldsymbol\chi)+L\epsilon^2/2-a_*\epsilon
       \le M(\boldsymbol\chi)-\delta
 \tag{21}
\]
after fixing a sufficiently small \(\epsilon\), with \(\delta>0\).
Equations (16)--(21) prove
\[
 |Z_N^{\rm low}-\mathcal P_N|
          \le C N^A e^{N(M(\boldsymbol\chi)-\delta)}
 \tag{22}
\]
on the real outside torus, uniformly on the whole nonzero lattice
cube. Polynomial continuation preserves a smaller gap on a fixed
complex boundary polydisk: each boundary degree is less than \(N\),
so its cost is a polynomial times \(e^{N\sum|\Im u_e|}\).
Continuity of \(W\) preserves the relative gap after that polydisk
is shrunk. No small-height geometric-series denominator is used.

## 4. Fixed face contours and division of the vanishing amplitude

Fix a base charge vector \(\boldsymbol\chi^0\) in the closed cube,
and let \(A=\{v:\chi_v^0=0\}\). Keep the product contours
\[
            C_v^0=[-\pi,\pi]-iH_v(\boldsymbol\chi^0)
 \tag{23}
\]
fixed while varying the charges near that base. In particular the
contours for \(v\in A\) are real. Define the holomorphic interpolant
\[
 \mathcal P_N^0(\boldsymbol\chi;\mathbf u)
 =\left(\frac{iN^2}{2\pi}\right)^k
   \int_{\prod C_v^0}
       \prod_v\sin t_v\,F_N(\mathbf t;\mathbf u)
                       e^{-iN\boldsymbol\chi\cdot\mathbf t}\,d\mathbf t.
 \tag{24}
\]
At integer \(N\boldsymbol\chi\), separate periodicity and Cauchy's
theorem give (17) exactly. Away from those integers it is the stated
fixed-contour interpolation, not the original cosine trace. For each
\(v\in A\), reflection of its real integration interval shows that
\(\mathcal P_N^0\) is exactly odd in \(\chi_v\).

For completeness, all estimates used to deform (24) are uniform
through a zero height. At the base, every real wire maximum is
strict and in \((0,1/2)\). Choose compact index intervals around
the maximizing indices. The complement has a fixed index-phase gap
by strict concavity and compactness, using (20). On the retained
indices, the local exact factorial expansion is
\[
 e_a(-2\cos t)e_a(-2\cos u)
 =\frac{e^{NQ(x;t,u)}}{4N^2\sin^2\pi x}(1+O_{\rm hol}(N^{-1})),
 \quad Q=b(x,t)+b(x,u),\quad x=a/N,
 \tag{25}
\]
where
\(b(x,t)=\int_0^x\log(2\cos2\pi s+2\cos t)\,ds-2J(x)\)
uses the branch positive at the imaginary base angles.
The exact index cotangent contour gives
\[
 K_{N,I_e}(t,u)=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}
                       (1+O_{\rm hol}(N^{-1})),
 \qquad
 a_e=\frac{\sqrt{2\pi}}{4\sin^2(\pi x_e)\sqrt{-Q_{xx}(x_e)}}.
 \tag{26}
\]
These are the actual symbols of the pinned regular low-source proof.
Their factorial arguments have a fixed bulk margin even when either
angle is zero.

The real angular tail estimate also remains uniform for bounded
heights including zero. For a compact index interval \(I\), the
root-product proof gives
\[
 |e_a(-2\cos(\tau-ih))|
 \le C N^A e_a(-2\cosh h)
                       e^{-cN(1-\cos\tau)},
       \qquad a/N\in I,\quad 0\le h\le H_*.
 \tag{27}
\]
One can see the endpoint uniformity directly in that proof: compare
the midpoint sum of \(\log|1+e^{h+is}|\) with its integral. Remove
the mesh intervals nearest its possible zero at \(h=0\); the upper
error there is \(O(\log N)\), and the remaining variation has the
same bound uniformly in \(h\). At a vanishing product the upper
bound is automatic. The integrated derivative inequality has the
uniform positive coefficient
\(\min_{x\in I}\sin(2\pi x)/(2\pi(\cosh H_*+1))\).
Thus the only angular maximum at the base is \(\Re\mathbf t=0\),
and the endpoints of every interval (23) have a fixed strict gap.

For sufficiently small complex changes of charges and outside
variables, deform only a small neighborhood of that maximum through
its continued saddle. Endpoint connectors require only a small
motion from the fixed base contours; their existing gaps persist.
The discarded index and angular pieces also retain their gaps:
on the fixed compact contours the change of the charge exponential
costs at most \(e^{CN|\boldsymbol\chi-\boldsymbol\chi^0|}\), and
ordinary boundary polynomial continuation has the analogous cost.
No deformation from a real full circle to a distant height at a
nonlattice charge is invoked.

The selected angular Hessian is the negative of the positive height
Hessian at the base. The analytic Gaussian calculation in (24)--(26)
therefore gives, on a fixed complex neighborhood,
\[
 N^p e^{-NW}\mathcal P_N^0
      =A_0(\boldsymbol\chi,\mathbf u)+R_N(\boldsymbol\chi,\mathbf u),
 \qquad |R_N|\le C/N,
 \tag{28}
\]
where \(A_0=(\prod_v\chi_v)\beta\) with (14). The power of \(N\)
is \(2k-3e/2-k/2=-p\). This is an additive Gaussian expansion;
it does not assume that the amplitude is nonzero at a zero charge.

Both sides of (28) are odd in every \(\chi_v\), \(v\in A\):
the integral has that exact parity, \(W\) is even, and \(A_0\)
is odd. Hence \(R_N\) is divisible by \(\prod_{v\in A}\chi_v\).
Cauchy's estimate on a slightly larger complex polydisk gives
\[
 \left|\frac{R_N}{\prod_{v\in A}\chi_v}\right|\le C'/N
 \tag{29}
\]
on a smaller one, including its coordinate hyperplanes. For example,
divide successively using the integral of the first derivative on
the segment from zero to the given coordinate. The coordinates not
in \(A\) are bounded away from zero on this patch, so (29) yields
division by their factors as well. This proves the required uniform
relative principal estimate locally.

A finite collection of these face-centered and interior patches
covers the closed cube. Their interpolants need not agree away
from the lattice; at its points each equals the same principal
Fourier block. Taking the finite minimum of their boundary radii
and the finite maximum of their error constants proves the uniform
principal formula everywhere on the nonzero lattice cube. Finally
\(\prod_v\chi_v\ge N^{-k}\), so the alias error (22), divided
by that prefactor, is still exponentially smaller. This proves (8).

Separate evenness in every outside angle holds for the exact source,
the critical action, and all the displayed coefficients and errors.
An even holomorphic function of \(u_e\) descends holomorphically to
\(z_e=-2\cos u_e\) near \(-2\). Cauchy's estimate on a smaller
spectral polydisk therefore proves the ordinary derivative assertion
in Theorem 1, including the angular ramification at completeness.

## 5. The transition and its quantitative scope

At \(\boldsymbol\chi=\mathbf0\), every height is zero, every wire
maximum is \(x_e=1/4\), and direct differentiation of (25) gives
\[
 Q_{xx}=-8\pi,\quad a_e=1/4,\quad
 K=\operatorname{diag}(d_v/(2\pi)),\quad
 H_v/\chi_v=2\pi/d_v.
 \tag{30}
\]
Substitution in (14) proves (9). Since \(\partial_{\chi_v}M=-H_v\)
and \(M\) is separately even,
\[
 M(\boldsymbol\chi)=eM_\infty
                    -\pi\sum_v\chi_v^2/d_v+O(|\boldsymbol\chi|^4),
 \qquad
 \beta(\boldsymbol\chi,\mathbf0)=\beta(\mathbf0,\mathbf0)
                                      (1+O(|\boldsymbol\chi|^2)).
 \tag{31}
\]
Equations (8) and (31) give (10), including its uniform error on
the stated \(\sqrt N\) scale. For mixed faces, (8) instead retains
the exact action of the remaining interior charges and the analytic
coefficient (14); no simultaneous smallness of those charges is needed.

The nonzero lattice qualification is essential. At \(J_v=0\) the
principal difference in that coordinate is exactly zero. Moreover
\(\mathcal C_{N,0}=\eta\,1\) in the full physical algebra: its
values are \(\eta\) and all double-node normals vanish. Thus the
actual zero-charge trace in that coordinate is \(\eta\) times the
uncharged trace, supplied by the remaining aliases. Formula (8) is
not asserted at that exact endpoint for the full low source.

On the whole nonzero lower half-charge block, combine (8) with the
adopted uniform high-sector gap to obtain the same formula for the
full original zero-power source, with unchanged coefficient and
ordinary boundary derivatives. On larger charge sets this additional
step requires the corresponding actual high-sector estimate; none
is inferred from the low calculation alone.

The quantitative error proved here is relative \(O(N^{-1})\), with
the explicitly retained factor \(\prod\chi_v\). Repeating the local
factorial and Gaussian expansions to any fixed order and the same
odd division gives the corresponding fixed-order version whenever
those fixed-order symbols are retained. No uniform optimal-truncation
or exponentially accurate sampling theorem is claimed. In particular,
this relative estimate alone does not meet an exponentially amplified
finite-reconstruction error budget. Nor does it supply a common
off-lattice complex-charge initializer, a heat-path coverage theorem,
or a nonzero coefficient after arbitrary further fillings.

## Direct sources and author readback

The complete proof and directly used implications are read before
the final version is frozen. Only written mathematics, text reads,
and file hashes are used; no mathematical programs or numerical
tests are run.

* [Charge-cube positivity](research_zero_power_charge_cube_positivity.md),
  SHA256 91b0a03a677c9139bbfd04f9ef6b06b23e6c3fab435c1a974a2d243189925faf:
  regular positive components and the unique exceptional unit corner.
  Section 2 above supplies the additional compact partially zero-face
  conclusion instead of assuming it from that source.
* [Convex height potential](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_zero_power_subtree_convex_potential.md),
  SHA256 c0ab73c2869ed3db7a0152634cbf3a315c573eed2f5fc99e437dacadcceb8eb8:
  coercivity, regular edge Hessians, edge maxima and phase calibration.
* [Regular low source](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_regular_zero_subtree_low_source.md),
  SHA256 06e4b7c14e3a61616dea61642103e2d2803709fcd465ae9860258119db3299d1:
  exact local edge density, cotangent comparison, angular decrease,
  original trace normalization and holomorphic Gaussian proof.
* [Lower half-charge source](research_zero_power_half_charge_high_gap.md),
  SHA256 fb2ffd3cfe32848d490bc866c70fb96505760cbe48344981a97c5abce131a0cd:
  exact charged Fourier differences, uniform bounded-height factorial
  estimate, and the separate whole-grid high-sector gap.
