# A uniform full charge-grid theorem for zero-power subtrees

Private written proof, 16 November 2026.

For original selected degrees at least twelve, the complete nonzero
\(N^s\) charge grid has one uniform full-source asymptotic. It retains
the vanishing charge factors at zero faces and both Fourier companions
at unit faces, simultaneously. In particular it includes mixed corners
such as \(J_v=1\), \(J_w=N\), every level parity, and the ordinary
free-boundary polynomial with its derivatives.

This is a fixed-order theorem for the actual finite source. It supplies
the whole sample array used by the canonical finite charge
reconstruction, with an explicit error scale. It does not convert that
scale into an exponentially accurate complex-charge asymptotic.

## 1. Source and statement

Let \(T\) be a fixed finite tree and \(S\) a nonempty connected proper
selected set. Every selected crossing power is zero and every original
selected degree satisfies
\[
                             d_v\ge12.
 \tag{1}
\]
Let \(E_S\) contain all edges incident to \(S\), each once, and write
\[
 s=|S|,\qquad e=|E_S|,\qquad b=|\partial S|,\qquad
 e=s-1+b,\qquad p=\frac{3(b-1)}2.
 \tag{2}
\]
Each outside incidence remains an independent ordinary spectral
variable \(z_w=-2\cos u_w\).

Use the full original Newton algebra and closing:
\[
 D=N-1,\quad\eta=(-1)^D,\quad P_N(z)=2T_N(z/2)+2,
 \qquad\phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f,
\]
\[
 e_a(z)=S_a^{-2}\prod_{j<a}(c_j-z),\quad
 S_a=\prod_{j=1}^a2\sin(\pi j/N),\quad
 c_j=2\cos((2j+1)\pi/N),
\]
\[
 K_N(t,u)=\sum_{a=0}^{D}e_a(-2\cos t)e_a(-2\cos u).
 \tag{3}
\]
All repeated-root first normals are retained. For
\[
           c_v=J_v/N,\qquad 1\le J_v\le N,
 \tag{4}
\]
the literal charge coupon is
\(\mathcal C_{N,c_v}=T_{N-J_v}(-z_v/2)\), including its normal
data. Define
\[
 Z_N(\mathbf c;\mathbf u)=
 \left(\prod_{v\in S}\phi_N^{(v)}\right)
 \left[\prod_{v\in S}\mathcal C_{N,c_v}(z_v)
                         \prod_{vw\in E_S}K_N(t_v,t_w)\right].
 \tag{5}
\]
Outside angles in (5) equal their corresponding \(u_w\).
Write \(Z_N^{\rm low}\) for the same expression with every original
edge index restricted by \(2a<N\).

For an effective charge vector \(\boldsymbol\lambda\in[0,2]^S\),
let \(\mathbf H(\boldsymbol\lambda)\ge0\) be the minimizer of
\[
 \mathcal L_{\boldsymbol\lambda}(\mathbf H)
    =\sum_{vw\in E_S}V(H_v,H_w)-\sum_{v\in S}\lambda_vH_v,
                    \qquad H_w=0\quad(w\notin S),
\]
\[
 V(H,G)=\max_{0\le x\le1/2}\{B(x,H)+B(x,G)\},
\]
\[
 B(x,H)=\int_0^x\log(2\cos2\pi t+2\cosh H)\,dt-2J(x),
 \qquad J(x)=\int_0^x\log(2\sin\pi t)\,dt .
 \tag{6}
\]
Write \(M_\infty=V(0,0)=4G/\pi\), where \(G\) is Catalan's
constant. The minimum in (6) is \(M(\boldsymbol\lambda)\).
Section 2 proves compact regularity on this entire doubled cube.
Use the original regular edge phase \(\psi\) to define
\[
 F_{\boldsymbol\lambda}(\mathbf t,\mathbf u)
     =\sum_{vw\in E_S}\psi(t_v,t_w)
                         -i\sum_{v\in S}\lambda_vt_v,
\]
\[
 \mathbf t^*(\boldsymbol\lambda,\mathbf0)=-i\mathbf H(\boldsymbol\lambda),
 \qquad W(\boldsymbol\lambda,\mathbf u)
           =F_{\boldsymbol\lambda}(\mathbf t^*,\mathbf u).
 \tag{7}
\]
The complete constants and height-continuation branches are retained;
\(W(\boldsymbol\lambda,\mathbf0)=M(\boldsymbol\lambda)\).

For each \(\omega\in\{0,1\}^S\), put
\[
 \lambda_v^\omega=
 \begin{cases}c_v,&\omega_v=0,\\2-c_v,&\omega_v=1,\end{cases}
 \qquad
 R_\omega(\mathbf c)=\prod_{v\in S}\frac{\lambda_v^\omega}{c_v}.
 \tag{8}
\]
The ratios are used only on the nonzero lattice (4).

**Theorem 1.** There are a fixed complex outside polydisk \(U\),
holomorphic coefficient functions
\(\beta_r(\boldsymbol\lambda,\mathbf u)\) on a neighborhood of
\([0,2]^S\times U\), and \(\delta>0\) with the following property.
For every fixed \(L\ge1\), constants \(C_L,N_L\) give, at both
parities and every grid tuple (4) with \(N\ge N_L\),
\[
 \begin{split}
 Z_N(\mathbf c;\mathbf u)
  ={}&N^{-p}\left(\prod_vc_v\right)e^{NW(\mathbf c,\mathbf u)}
       \left\{\sum_{r=0}^{L-1}\frac{\mathcal B_{N,r}(\mathbf c,\mathbf u)}
                                          {N^r}
                        +\mathcal R_{N,L}(\mathbf c,\mathbf u)\right\},\\
 \mathcal B_{N,r}(\mathbf c,\mathbf u)
  ={}&\sum_{\omega\in\{0,1\}^S}
       R_\omega(\mathbf c)\,
       \beta_r(\boldsymbol\lambda^\omega,\mathbf u)
       e^{N\{W(\boldsymbol\lambda^\omega,\mathbf u)
                         -W(\mathbf c,\mathbf u)\}},\\
 |\mathcal R_{N,L}|
  \le{}&C_L\{N^{-L}+e^{-\delta N}\}.
 \end{split}
 \tag{9}
\]
All bounds are uniform on \(U\). On smaller spectral polydisks they
hold with every fixed ordinary boundary derivative after extracting
the displayed reference exponential and charge product.

For each fixed \(r\), \(\mathcal B_{N,r}\) is uniformly bounded.
There are constants \(b_-,b_+>0\) such that
\[
                b_-\le|\mathcal B_{N,0}|\le b_+
 \tag{10}
\]
on a common smaller \(U\), independently of every \(J_v\) and \(N\).
In particular (9) is an actual uniform nonzero full-source formula
on the entire \(N^s\) nonzero charge grid.

The normalization of its positive coefficient is
\[
 \beta_0(\boldsymbol\lambda,\mathbf u)
 =\left(\frac{i}{\sqrt{2\pi}}\right)^s
 \frac{\displaystyle
       \prod_v\frac{\sin t_v^*}{\lambda_v}
                       \prod_{vw\in E_S}a_e(t_v^*,t_w^*)}
      {\sqrt{\det(-F_{\mathbf t\mathbf t})}},
 \tag{11}
\]
with each quotient continued holomorphically across \(\lambda_v=0\).
The square root is positive at real effective charges and complete
outside angles, so \(\beta_0(\boldsymbol\lambda,\mathbf0)>0\).
The factor \(2^{-s}\) from the cosine expansion is already included
in (11); it must not be multiplied into (9) again.

## 2. Compact regular geometry on the doubled cube

The original potential is convex and continuous, and
\(V(H,G)\ge(H+G)/2\). Therefore
\[
 \mathcal L_{\boldsymbol\lambda}(\mathbf H)
       \ge\sum_v(d_v/2-\lambda_v)H_v
       \ge4\sum_vH_v,\qquad 0\le\lambda_v\le2.
 \tag{12}
\]
Every minimum exists in a uniform compact box. If \(\lambda_v=0\),
strict increase of every incident potential in its own positive
height forces \(H_v=0\). If \(\lambda_v>0\), the derivative at
\(H_v=0\) is \(-\lambda_v<0\), so its minimizing height is positive.

Let \(r_v=\sinh(H_v/2)\). Each original incidence angle satisfies
\[
 \alpha_{v,e}=\pi V_{H_v}\ge\arctan r_v.
 \tag{13}
\]
This holds also on a saturated edge, whose angle is \(\pi/2\).
At a positive coordinate the stationary row is
\(\sum_{e\ni v}\alpha_{v,e}=\pi\lambda_v\). Thus
\[
 d_v\arctan r_v\le2\pi,\qquad
 r_v\le\tan(2\pi/d_v)\le1/\sqrt3.
 \tag{14}
\]
It follows that every internal edge has
\[
             r_vr_w\le1/3<1,\qquad 0\le H_v\le\log3.
 \tag{15}
\]
Every outside edge is regular too. In particular all minimizing
wire indices have a uniform interior margin.

The regular edge Hessians are positive definite, with their
one-variable versions on outside edges. Their sum is positive
definite on all selected coordinates, including zero heights.
Local strict convexity at a minimum and global convexity imply
uniqueness. Uniform coercivity then implies continuity of the
minimum on the entire closed cube. The same Hessian argument and
the analytic implicit function theorem provide a common regular
analytic neighborhood of the compact minimizing family.

The edge potential extends evenly in each signed height on this
neighborhood. Reflection of \(\lambda_v\) therefore changes only
the sign of \(H_v\). At a zero coordinate its off-diagonal Hessian
row vanishes by separate evenness, and its diagonal entry is
strictly positive. Consequently
\[
 H_v/\lambda_v
 \text{ extends to a positive analytic unit on }[0,2]^S.
 \tag{16}
\]
It has uniform positive lower and finite upper bounds. The same
reflection and divisibility hold for the original critical angles
with small complex outside data:
\[
 t_v^*/\lambda_v\text{ is holomorphic},\qquad
 W\text{ is even in every effective charge across its zero face.}
 \tag{17}
\]
Height contraction fixes the original phase branch: all products
in (15) stay strictly below one along that contraction. No geometric
completion with an auxiliary cone angle greater than \(2\pi\) is
claimed; the doubled cube is the domain of the regular Fourier
stationary problems needed here.

## 3. Exact Fourier blocks and a uniform higher-alias gap

Write the original low product before tracing as
\[
 F_N(\mathbf t;\mathbf u)
       =\prod_{vw\in E_S}K_N^{\rm low}(t_v,t_w)
       =\sum_{\mathbf r}a_{N,\mathbf r}(\mathbf u)
                                    e^{i\mathbf r\cdot\mathbf t}.
 \tag{18}
\]
At complete outside angles its Laurent coefficients are nonnegative
and separately symmetric. For real outside angles their absolute
values have the coefficientwise complete-boundary majorant.
Put
\[
 \Delta_{\mathbf q}a_N
 =\sum_{\boldsymbol\epsilon\in\{-1,1\}^S}
        \left(\prod_v(-\epsilon_v)\right)
                         a_{N,\mathbf q+\boldsymbol\epsilon}.
 \tag{19}
\]
The exact full-normal trace is the tensor product of
\[
 \begin{split}
 \phi_N(f\mathcal C_{N,J/N})
 =\frac{N^2}{2}\sum_{\ell\ge1}\ell\eta^{\ell+1}
 \big[&a_{(\ell-1)N+J-1}-a_{(\ell-1)N+J+1}\\
      &+a_{(\ell+1)N-J-1}-a_{(\ell+1)N-J+1}\big].
 \end{split}
 \tag{20}
\]
In particular every original normal multiplier is \(\ell N\), not
\(J\).

Retaining both terms with \(\ell_v=1\) in every coordinate gives
exactly
\[
 \sum_{\omega\in\{0,1\}^S}\mathcal P_N(\boldsymbol\lambda^\omega;\mathbf u),
 \qquad
 \mathcal P_N(\boldsymbol\lambda;\mathbf u)
                  =(N^2/2)^s\Delta_{N\boldsymbol\lambda}a_N.
 \tag{21}
\]
There is no parity sign at \(\ell=1\). At \(c_v=1\), the two terms
are identical and both remain: this is exactly the original cosine
multiplicity.

Every omitted block has effective charges
\(\mu_v=(\ell_v-1)+c_v\) or \((\ell_v+1)-c_v\).
They satisfy \(\boldsymbol\mu\ge\mathbf c\), and at least one
coordinate has excess at least one. Only boundedly many such blocks
are nonzero: the Laurent degree at \(v\) is at most
\(d_v\lfloor(N-1)/2\rfloor\), so the possible \(\ell_v\)'s are
bounded in terms of the original degrees.

For any bounded nonnegative height vector, the positive majorant gives
\[
 |\Delta_{N\boldsymbol\mu}a_N(\mathbf u)|
 \le\prod_v2\cosh h_v\,
    e^{-N\boldsymbol\mu\cdot\mathbf h}F_N(-i\mathbf h;\mathbf0),
 \qquad
 F_N(-i\mathbf h;\mathbf0)
 \le C N^A e^{N\sum_eV(h_v,h_w)}.
 \tag{22}
\]
These estimates include zero heights and retain all shared indices.
Choose a coordinate with \(\mu_v-c_v\ge1\), and evaluate (22) at
\(\mathbf h=\mathbf H(\mathbf c)+\epsilon\mathbf e_v\).
Compact regularity on the original cube permits a fixed sufficiently
small \(\epsilon>0\) and a uniform Hessian upper bound \(L_0\).
Stationarity at the base, including its zero coordinates, gives
\[
 \mathcal L_{\boldsymbol\mu}
       (\mathbf H(\mathbf c)+\epsilon\mathbf e_v)
 \le M(\mathbf c)+L_0\epsilon^2/2-\epsilon
 \le M(\mathbf c)-\delta_0.
 \tag{23}
\]
All other excess charges are nonnegative and only improve the bound.
Thus, uniformly on the full grid and the real outside torus,
\[
 \left|Z_N^{\rm low}
       -\sum_\omega\mathcal P_N(\boldsymbol\lambda^\omega)\right|
           \le C N^A e^{N(M(\mathbf c)-\delta_0)}.
 \tag{24}
\]
A small complex outside polydisk preserves a smaller relative gap,
using the actual boundary degree \(D\) and continuity of \(W\).
This proof never divides by a small-height angular geometric-series
denominator.

## 4. Uniform principal blocks through every zero face

The following application of the zero-face proof is made on the
doubled cube, whose regularity was established separately in Section 2.
For every fixed \(L\),
\[
 \mathcal P_N(\boldsymbol\lambda;\mathbf u)
 =N^{-p}\left(\prod_v\lambda_v\right)e^{NW(\boldsymbol\lambda,\mathbf u)}
   \left\{\sum_{r=0}^{L-1}\frac{\beta_r(\boldsymbol\lambda,\mathbf u)}{N^r}
                         +O_{\rm hol,L}(N^{-L})\right\}
 \tag{25}
\]
uniformly for integer \(N\boldsymbol\lambda\) in \([0,2N]^S\).
At a coordinate \(\lambda_v=0\), both the exact block and the
displayed expression vanish. This is a Fourier-block assertion,
not an assertion about the full cosine source at exact zero charge.

Here are the parity and interpolation details needed for (25).
Fix a face point \(\boldsymbol\lambda^0\), and let
\(A=\{v:\lambda_v^0=0\}\). Keep the product circles
\[
                  C_v^0=[-\pi,\pi]-iH_v(\boldsymbol\lambda^0)
 \tag{26}
\]
fixed as the charges vary near that point. At \(v\in A\) this is
the real circle. Define the holomorphic local interpolant
\[
 \mathcal P_N^0(\boldsymbol\lambda;\mathbf u)
 =\left(\frac{iN^2}{2\pi}\right)^s
   \int_{\prod C_v^0}
       \prod_v\sin t_v\,F_N(\mathbf t;\mathbf u)
                       e^{-iN\boldsymbol\lambda\cdot\mathbf t}
                                            d\mathbf t .
 \tag{27}
\]
At integer \(N\boldsymbol\lambda\), periodicity and Cauchy's theorem
identify it exactly with (21). No off-lattice identification with
the cosine source is made. Reflection of a real circle makes (27)
exactly odd in each \(\lambda_v\), \(v\in A\).

All regular wire maxima and factorial arguments have common interior
margins on the compact doubled cube. The fixed-circle angular
decrease is uniform even at height zero. Therefore the local index
cotangent and angular Gaussian proof applies uniformly on a fixed
complex neighborhood of each face point: the complementary indices,
circle endpoints and local connectors retain strict losses. The
fixed-order factorial symbols and Taylor remainders give
\[
 N^p e^{-NW}\mathcal P_N^0
       =\sum_{r=0}^{L-1}\frac{\mathfrak a_r}{N^r}
                                      +O_{\rm hol,L}(N^{-L}).
 \tag{28}
\]
The coefficients are the canonical local saddle coefficients of the
same phase and density. They do not depend on the endpoint choice
in (26); changes there affect only the exponentially small complement.
They therefore agree on overlapping regular charts.

By (17) the phase is even in each charge in \(A\). Exact oddness of
(27) then implies oddness of every \(\mathfrak a_r\) and of its
normalized remainder in those coordinates. This can also be read
directly from the local saddle density. Divide successively by these
coordinates. Cauchy's estimate on a slightly larger face polydisk
shows that the divided remainder is still \(O_L(N^{-L})\).
The other charges are bounded away from zero on that patch and
may be divided out directly. Hence
\(\beta_r=\mathfrak a_r/\prod_v\lambda_v\) is holomorphic with
the remainder in (25).

A finite face/interior cover of \([0,2]^S\) supplies common constants
and one outside polydisk. The off-lattice interpolants need not
agree on overlaps, but at lattice points they equal the same
Fourier block, and their canonical saddle coefficients agree.
This proves (25), including arbitrary mixtures of small and order-one
effective charges. The leading coefficient calculation gives (11).
Its positivity and uniform nonvanishing follow from (16), the
positive edge densities and the positive height Hessian.

## 5. Combining the charge factors without losing uniformity

For small complex outside data the stationary-value identity and
(16)--(17) give
\[
 \partial_{\lambda_v}W=-it_v^*,\qquad
 \Re\left(\frac{it_v^*}{\lambda_v}\right)\ge h_0>0
                        \quad(\boldsymbol\lambda\in[0,2]^S).
 \tag{29}
\]
The quotient is its holomorphic extension at zero. Integrate one
reflected coordinate from \(c_v\) to \(2-c_v\), keeping the other
coordinates in the doubled cube, and then repeat for all reflected
coordinates. Since those coordinates are real and nonnegative,
\[
 \Re\{W(\boldsymbol\lambda^\omega,\mathbf u)-W(\mathbf c,\mathbf u)\}
       \le-2h_0\sum_{\omega_v=1}(1-c_v).
 \tag{30}
\]

The only apparently singular factor after extracting \(\prod c_v\)
is \(R_\omega\). For each reflected coordinate,
\[
 \frac{2-c_v}{c_v}
 e^{-2h_0N(1-c_v)}
 \le
 \begin{cases}
 3,&c_v\ge1/2,\\
 2N e^{-h_0N},&1/N\le c_v<1/2.
 \end{cases}
 \tag{31}
\]
Both right sides are uniformly bounded. Thus (30)--(31) show that
every normalized branch and every fixed-order remainder in (25)
is bounded uniformly relative to
\(N^{-p}(\prod c_v)e^{NW(\mathbf c,\mathbf u)}\).
There is no division of a reflected zero-face branch off the
nonzero lattice: its possible \(N\)-factor is controlled by its
actual exponential action gap.

At complete outside angles every leading branch is positive, and the
unreflected branch alone gives
\[
 \mathcal B_{N,0}(\mathbf c,\mathbf0)
          \ge\inf_{\boldsymbol\lambda\in[0,2]^S}
                         \beta_0(\boldsymbol\lambda,\mathbf0)>0.
 \tag{32}
\]
Equations (30)--(31) bound this holomorphic sum uniformly on a
common complex outside polydisk. Cauchy's estimate bounds its
derivatives on a smaller one, independently of \(N\) and all charges.
A final uniform shrink preserves half the positive lower bound in
(32). This proves (10).

The higher-alias error (24), after extracting the same reference, is
still exponentially small: \(\prod c_v\ge N^{-s}\), so only a
fixed polynomial is lost. The adopted degree-twelve high-sector
theorem gives
\[
 \sup_{\mathbf u\text{ real}}|Z_N-Z_N^{\rm low}|
       \le C N^A e^{N(M(\mathbf c)-\gamma)},\qquad
 \gamma=M_\infty-4\operatorname{arsinh}(2-\sqrt3)>4/99
 \tag{33}
\]
uniformly for every tuple (4). Boundary continuation and the same
polynomial absorption preserve a smaller exponential gap on \(U\).
Combining (24), (25), and (30)--(33) proves (9) for the full
original source.

Every function and error in the outside angles is separately even.
Near completeness, an even holomorphic function of \(u_w\) descends
holomorphically through \(z_w=-2\cos u_w\). Shrinking the common
spectral polydisk and applying Cauchy's estimates proves the stated
ordinary boundary derivative bounds, including the angular
ramification at \(u_w=0\).

## 6. Endpoints and the full sample array

When all \(c_v=1\), every effective vector in (8) is \(\mathbf1\).
The \(2^s\) equal terms in (9) cancel the cosine factor already
included in (11), giving the original unit-charge amplitude.
When some \(J_v\) stay fixed while others equal \(N\), (31)
suppresses reflected small-charge coordinates and retains both equal
unit companions. Thus the same formula covers mixed zero/unit
corners without imposing a positive lower bound on the small
heights.

Exact zero charges \(J_v=0\) are excluded. The principal Fourier
block then vanishes in that coordinate, whereas the full coupon is
\(\mathcal C_{N,0}=\eta\,1\) and its source is supplied by other
aliases. The reconstruction samples are \(J_v=1,\ldots,N\), so no
zero sample is required.

For each fixed \(L\), let \(\mathscr S_{N,L}\) be the finite branch
sum in (9), truncated before order \(N^{-L}\). Since \(M\) is
nonincreasing in each nonnegative charge,
\[
                  M(\mathbf c)\le M(\mathbf0)=eM_\infty.
 \tag{34}
\]
At complete outside angles the whole \(N^s\)-sample array consequently
has the actual uniform absolute error
\[
 \max_{\mathbf J\in\{1,\ldots,N\}^S}
       |Z_N(\mathbf J/N;\mathbf0)-\mathscr S_{N,L}(\mathbf J/N;\mathbf0)|
             \le C_L N^{-p-L}e^{NeM_\infty}.
 \tag{35}
\]
For the canonical polarized observation at \(y_v=1-\chi_v\), the
exact finite reconstruction therefore has error at most
\[
 C_L N^{s-p-L}\prod_v(1+2|y_v|)
 \exp\left\{NeM_\infty+
            \pi D\sum_v(-\sigma_v\Im y_v)_+\right\}.
 \tag{36}
\]
This is a quantitative consequence of having all the samples, not
just an interior subarray. It is still only a fixed-order estimate.
To dominate a target exponential of real action \(A_{\rm target}\),
an exponentially improved sample error would need to pay both the
deficit \(eM_\infty-A_{\rm target}\) and the directional cost in
(36). No such improvement follows from fixing a larger \(L\).

The theorem is a whole finite-source charge-grid result for the
stated original zero-power subtrees. It is not an off-lattice
complex-charge initializer, an arbitrary short-filling theorem, or
a proof of the volume conjecture for a larger knot class.

## Direct sources

Only written mathematics, source-text reads and hashes are used.
Complete author proof and source readbacks are checked before freeze.

- [Zero-charge uniform low source](research_zero_charge_uniform_low_source.md),
  SHA256 d4412c67ca520894840b80e390058ce2438af906ea13f719abb5def5c252496d:
  face-centered Fourier interpolation, exact normal differences,
  fixed-height alias gap, odd division and spectral boundary descent.
- [Unit-charge companion theorem](research_unit_charge_companion_uniformity.md),
  SHA256 e54bf679e69e70305019b8bb24e820e8388823818fbe53101b754b402fc3cac3:
  retained companion normalization, fixed-order saddle coefficients,
  holomorphic noncancellation and source-level contour scope.
- [Half-charge and whole-grid high bound](research_zero_power_half_charge_high_gap.md),
  SHA256 fb2ffd3cfe32848d490bc866c70fb96505760cbe48344981a97c5abce131a0cd:
  exact alias formula, bounded-height kernel profiles and uniform
  degree-twelve high-complement estimate.
- [Convex height potential](research_zero_power_subtree_convex_potential.md),
  SHA256 c0ab73c2869ed3db7a0152634cbf3a315c573eed2f5fc99e437dacadcceb8eb8:
  incidence derivative bounds, regular Hessians, convexity and the
  absolute edge constants used in the doubled-cube proof.
- [Finite quantitative charge reconstruction](research_finite_charge_quantitative_reconstruction.md),
  SHA256 5d13994e8b6d2dc3c54d1fcf15d1f9435efc2d26921046bca14b90d22e75bf23:
  exact full-normal tensor reconstruction and directional error norm.
