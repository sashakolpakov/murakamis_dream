# The actual endpoint normal defect and its coherent bulk sine primitive

Private written proof, 16 November 2026.

The full first normal of a microscopic endpoint kernel is not obtained
by differentiating an arbitrary interpolation of its physical values.
This note gives the exact difference, including its original trace
current. The difference is a sum of the derivative of the physical-value
interpolant and a sine transform of the actual high Fourier coefficients.
The checkerboard cancels inside this transform. On a fixed bulk frequency
interval, the transform has an explicit discrete primitive with
exponentially small remainder. Its two terminal terms remain.

The separate value/normal interpolation theorem supplies polynomially
bounded analytic representatives of both channels. It does not make
their difference zero. No filled-action estimate, contour cancellation,
or source nonvanishing follows here.

## 1. Original values, normals, and the exact radical Fourier split

Put
\[
 N\ge2,\quad D=N-1,\quad \eta=(-1)^D,\quad \theta=\pi/N,
 \quad m=\lfloor N/2\rfloor,\quad J=\lfloor(N-1)/2\rfloor,
\]
\[
 c(j)=2\cos((2j+1)\theta),\quad
 \nu_j=(2j+1)\theta,\quad \tau_j=\pi-\nu_j,\quad x_j=j/N,
\]
\[
 c'(j)=-4\theta\sin\nu_j,\qquad
 w=2\cosh(\alpha/N),\qquad
 B_N(Z)=K_N(w,Z).
 \tag{1}
\]
The prime on \(c\) is the derivative in its unscaled index. Explicitly,
the original normalization is
\[
 c_0=c(0),\quad s_r=2\sin(r\theta),\quad
 S_j=\prod_{r=1}^j s_r,\quad S_0=1,\quad
 e_j(Z)=S_j^{-2}\prod_{r<j}(c(r)-Z),\quad
 K_N(w,Z)=\sum_{j=0}^{D}e_j(w)e_j(Z),\quad
 P_N(Z)=2T_N(Z/2)+2.
\]
Define
\[
 F_j=B_N(c(j)),\qquad G_j=B_N'(c(j)),\qquad
 B(t)=B_N(-2\cos t)
     =b_0+\sum_{k=1}^{D}b_k(e^{ikt}+e^{-ikt}).
 \tag{2}
\]
All identities in this section are ordinary polynomial identities in
\(w\). In particular they retain every other free variable and normal.

Let \(L_N(Z)\) be the unique polynomial of degree at most \(J\) taking
the values \(F_j\) at the distinct physical nodes \(c(0),\ldots,c(J)\).
Write \(L(t)=L_N(-2\cos t)\). For \(1\le s<N/2\), set
\[
 \mathcal R_s(t)=2\cos((N-s)t)-2\eta\cos(st).
 \tag{3}
\]
At every physical angle, \(e^{iN\tau_j}=\eta\), so these polynomials
vanish at every distinct physical node. For even \(N=2m\), the
polynomial \(2\cos(mt)\) also vanishes there. Consequently
\[
 \boxed{
 B(t)=L(t)+
       \sum_{1\le s<N/2}b_{N-s}\mathcal R_s(t)
       +\mathbf1_{N\ {\rm even}}\,2b_m\cos(mt).
 }
 \tag{4}
\]
Indeed subtract the displayed terms from \(B\). Every frequency above
\(J\) has been removed, and the resulting degree-\(J\) spectral
polynomial has precisely the original values. Uniqueness of ordinary
interpolation proves (4). At odd levels the simple node \(-2\) is
among these values. At \(N=2\), \(J=0\) and only the middle term occurs.

Direct differentiation gives
\[
 \mathcal R_s'(\tau_j)=2N\eta\sin(s\tau_j).
 \tag{5}
\]
Use a prime on a sum over \(1\le s\le m\) to mean weight one, except
weight \(1/2\) at \(s=m\) when \(N\) is even. Then (4)--(5) imply
\[
 B_t(\tau_j)=L_t(\tau_j)
                  +2N\eta\sum_{s=1}^{m}{}'b_{N-s}\sin(s\tau_j).
 \tag{6}
\]
The half weight gives exactly the derivative
\(-Nb_m\sin(m\tau_j)\) of the even middle term.

The bulk Fourier source proves, for real \(\alpha\),
\[
 b_{N-s}=\eta(-1)^{s-1}\beta_{s,N}(\alpha),\qquad
 \beta_{s,N}(\alpha)>0,\qquad 1\le s\le m.
 \tag{7}
\]
Define \(\beta_{s,N}\) by the same algebraic relation for any other
parameter where an exact identity is wanted. Positivity is asserted
only for real \(\alpha\). Since
\(\sin(s\tau_j)=(-1)^{s+1}\sin(s\nu_j)\), the actual checkerboard
cancels, with no parity sign left:
\[
 \boxed{
 B_t(\tau_j)=L_t(\tau_j)
                         +2N\sum_{s=1}^{m}{}'
                                      \beta_{s,N}\sin(s\nu_j).
 }
 \tag{8}
\]
This cancellation is within one coherent transform. It does not permit
replacing the transform by a sum of absolute coefficient values.

## 2. The true derivative defect and its original trace

Let \(I\) be a fixed compact interval in \((0,1/2)\), and let
\(f_N(x,\alpha)\) be any holomorphic function on a neighborhood of \(I\)
such that
\[
                         f_N(x_j,\alpha)=F_j(\alpha)
                         \quad(x_j\in I).
 \tag{9}
\]
No difference equation or relation to \(G_j\) is assumed. Its
derivative-compatible spectral normal at these nodes would be
\[
                    G_j^{\,f}=\frac{\partial_x f_N(x_j)}{N c'(j)}.
 \tag{10}
\]
The denominator is a unit on this fixed bulk interval. Define the
true scaled defect
\[
                  \Delta_j=Nc'(j)G_j-\partial_xf_N(x_j).
 \tag{11}
\]
As \(Nc'(j)=-4\pi\sin\nu_j\) and
\(B_t(\tau_j)=2\sin\nu_j\,G_j\), equation (8) yields
\[
 \boxed{
 \Delta_j=-2\pi L_t(\tau_j)
          -4\pi N\sum_{s=1}^{m}{}'\beta_{s,N}\sin(s\nu_j)
          -\partial_xf_N(x_j).
 }
 \tag{12}
\]
This formula compares the actual normal to the derivative of the
specified value interpolation. The common-index derivative of a
Jacobi determinant with fixed initial data is a different object;
its homogeneous remainder is not automatically (11).

Here is the exact source effect. Let \(A_N(Z;\mathbf u)\) denote the
actual remaining spectator, including any original crossing, coupon,
kernel, shared trace variable, and ordinary outside parameter. At the
double nodes the original trace is
\[
 \phi_N(B_NA_N)=
 \eta\sum_{\rm double\ j}
 \big\{(4-c(j)^2)[G_jA_N(c(j))+F_jA_N'(c(j))]
                    -c(j)F_jA_N(c(j))\big\}
 +\mathbf1_{N\ {\rm odd}}B_N(-2)A_N(-2).
 \tag{13}
\]
Replace only \(G_j\), for \(x_j\in I\), by (10), keeping all values
and every other row unchanged. If \(\mathcal T_N^f\) is the resulting
finite expression, then
\[
 \boxed{
 \phi_N(B_NA_N)-\mathcal T_N^f
   =-\frac{\eta}{\pi}\sum_{x_j\in I}
                         \sin\nu_j\,\Delta_j A_N(c(j);\mathbf u).
 }
 \tag{14}
\]
Indeed \(G_j-G_j^f=-\Delta_j/(4\pi\sin\nu_j)\).
The spectator derivative disappears only from this difference,
because the values have not changed. It remains in \(\mathcal T_N^f\).
The odd simple-node contribution in (13) is unchanged.
If \(A_N=R^n\widetilde A_N\), the exact original factor \(R(c(j))^n\)
remains in (14), together with its original carrier. No Gaussian sheet
or crossing phase has been changed.

Equation (14) is a consumed-normal physical-value current. It is not
asserted to vanish. It is coefficientwise in all uncontracted variables,
so their fixed normal operators and subsequent original traces commute
with the identity.

For finitely many endpoint factors, choose exact value interpolants
\(f_i\) separately and write
\[
 F_{\rm prod,j}=\prod_iF_{i,j},\qquad
 G_{\rm prod,j}=\sum_iG_{i,j}\prod_{\ell\ne i}F_{\ell,j}.
\]
The true product defect is exactly
\[
 \boxed{
 \Delta_{\rm prod,j}
 =Nc'(j)G_{\rm prod,j}
                -\partial_x\!\left(\prod_i f_i\right)(x_j)
 =\sum_i\Delta_{i,j}\prod_{\ell\ne i}F_{\ell,j}.
 }
 \tag{15}
\]
No value is divided out. Thus zeros of physical rows cause no exception.
Every occurrence of one shared physical color remains the same color
in all incident factors.

## 3. A controlled primitive for the actual analytic bulk transform

Fix a frequency interval \(J_0=[a,b]\Subset(0,1/2)\), a real
parameter bound \(|\alpha|\le A\), and use the exact interpolant from
the pinned bulk Fourier theorem on a slightly larger interval. After
reserving its fixed buffer, there are \(d>0\) and \(C\) such that
\[
 \mathfrak b_N(s/N,\alpha)=\beta_{s,N}(\alpha),\qquad
 \|\mathfrak b_N\|_{\Omega_d(J_0)}\le C/N,\qquad
 \Omega_d(J_0)=\{x:\operatorname{dist}(x,J_0)<d\}.
 \tag{16}
\]
Take \(d\) smaller if necessary so that this tube is inside the source
rectangle. The exact equality is required at every frequency node
used below. All constants are uniform for the real parameter interval.

Let the physical row angle \(\nu\) range over a fixed compact interval
\(\mathcal V_0\Subset(0,\pi)\). Choose a small complex neighborhood
\(\mathcal V\) of it and constants \(\mu>0,\Lambda\ge1\) such that, for
both signs,
\[
 z_\pm=e^{\pm i\nu},\qquad
 |1-z_\pm|\ge\mu,\qquad
 \left|\frac{z_\pm}{1-z_\pm}\right|\le\Lambda
                      \quad(\nu\in\mathcal V).
 \tag{17}
\]
Put \(h=1/N\), \(T_hg(x)=g(x+h)\), and
\[
 P_\pm=\frac{z_\pm}{1-z_\pm}(T_h-I),\qquad
 0<a_*<\min\{d/4,d/(16\Lambda)\},\qquad
 K_N=\lfloor a_*N\rfloor .
 \tag{18}
\]
For sufficiently large \(N\), define
\[
 \mathcal A_{\pm,N}(x,\nu,\alpha)
       =\frac1{1-z_\pm}\sum_{r=0}^{K_N-1}
                                      P_\pm^r\mathfrak b_N(x,\alpha).
 \tag{19}
\]
This is a finite holomorphic formula. It keeps the actual frequency
sampling, rather than replacing that sampling by an integral.

The exact operator identity is
\[
 (I-z_\pm T_h)\mathcal A_{\pm,N}
                  =\mathfrak b_N-P_\pm^{K_N}\mathfrak b_N.
 \tag{20}
\]
It follows from
\(I-z_\pm T_h=(1-z_\pm)(I-P_\pm)\) and the finite geometric sum.
In particular, for \(p=\lceil Na\rceil\), \(q=\lfloor Nb\rfloor\),
\[
 \begin{split}
 \sum_{s=p}^{q}\beta_{s,N}e^{\pm is\nu}
 ={}&e^{\pm ip\nu}\mathcal A_{\pm,N}(p/N,\nu,\alpha)\\
 &-e^{\pm i(q+1)\nu}
                 \mathcal A_{\pm,N}((q+1)/N,\nu,\alpha)\\
 &+\sum_{s=p}^{q}e^{\pm is\nu}
                  (P_\pm^{K_N}\mathfrak b_N)(s/N,\alpha).
 \end{split}
 \tag{21}
\]
There is no omitted endpoint term in this summation by parts.

For completeness, the exponential estimate follows from a fixed
analytic buffer. Use \(K_N\) nested tubes losing radius
\(\delta=d/(2K_N)\) at each step, from \(\Omega_d(J_0)\) to
\(\Omega_{d/2}(J_0)\). If \(g\) is bounded on the larger tube, a
segment of length \(h\) from a point in the next tube leaves Cauchy
radius at least \(\delta/2\), since \(h\le\delta/2\) for large \(N\).
Therefore
\[
 \|(T_h-I)g\|\le\frac{2h}{\delta}\|g\|
                       =\frac{4K_N}{Nd}\|g\|.
 \tag{22}
\]
The choices in (18) imply \(4\Lambda K_N/(Nd)\le1/4\). Iterating
on the nested domains and using (16) gives
\[
 \|\mathcal A_{\pm,N}\|_{\Omega_{d/2}(J_0)}
          \le\frac{4C}{3\mu N},\qquad
 \|P_\pm^{K_N}\mathfrak b_N\|_{\Omega_{d/2}(J_0)}
          \le \frac{C}{N}4^{-K_N}.
 \tag{23}
\]
The point \((q+1)/N\) is within this tube for large \(N\).
For real \(\nu\), the final sum in (21) is thus at most
\(C4^{-K_N}\). For an explicit common smaller exponent put
\[
                       \kappa=a_*\log2/4.
 \tag{24}
\]
Since \(K_N\ge a_*N/2\) eventually, (21)'s remainder is
\(O(e^{-4\kappa N})\) on the real angle interval, after increasing
a constant. On a smaller fixed complex neighborhood, it is
\(O(e^{-2\kappa N})\) provided
\[
                     b|\Im\nu|\le\kappa
 \tag{25}
\]
and that neighborhood stays inside \(\mathcal V\).
The extra factor \(N\) in the actual normal transform still leaves
an \(O(e^{-\kappa N})\) error. Fixed derivatives in \(x\) or \(\nu\)
have the same type of estimate on smaller domains, by Cauchy.

Taking the difference of the two signs divided by \(2i\) gives the
analytic sine identity
\[
 \begin{split}
 \sum_{s=p}^{q}\beta_{s,N}\sin(s\nu)
 =\frac1{2i}\big[&
 e^{ip\nu}\mathcal A_{+,N}(p/N,\nu,\alpha)
 -e^{i(q+1)\nu}\mathcal A_{+,N}((q+1)/N,\nu,\alpha)\\
 &-e^{-ip\nu}\mathcal A_{-,N}(p/N,\nu,\alpha)
 +e^{-i(q+1)\nu}\mathcal A_{-,N}((q+1)/N,\nu,\alpha)\big]
 +\mathcal E_N(\nu,\alpha),
 \end{split}
 \tag{26}
\]
where \(\mathcal E_N\) has the just-stated exponential bounds.
Using a difference, rather than complex conjugation, preserves
holomorphic spectator and parameter identities wherever the same
uniform input domain is available.

The terms in square brackets are unremoved terminal primitives.
They have size \(O(N^{-1})\) on the real angle interval; multiplying
by the normal factor \(N\) in (12) need not make them small. If the
frequency interval is subdivided and the same function (19) is used,
adjacent terminal terms cancel exactly, with their phases. The two
external terminal terms remain. The frequency bands near \(s=0\)
and \(s=N/2\), the even middle term, and the separate \(L_t\) term
in (12) have not been estimated or discarded by this argument.

All estimates here are for the amplitude itself. Multiplying (21)
or (26) by an unestimated graph spectator does not provide a bound
for that spectator or for its subsequent coherent trace.

## 4. Two bounded channels and the remaining compatibility equation

The pinned two-channel theorem gives, on each fixed bulk interval,
jointly holomorphic functions \(\mathcal F_N(x,\alpha)\) and
\(\mathcal G_N(x,\alpha)\), exact at the original value and normal
nodes, with polynomial bounds on a fixed strip. It permits every
bounded complex \(\alpha\)-disk and fixed parameter derivatives on
smaller disks. Therefore
\[
 \mathcal D_N(x,\alpha)
       =Nc'(Nx)\mathcal G_N(x,\alpha)
                         -\partial_x\mathcal F_N(x,\alpha)
 \tag{27}
\]
is a polynomially bounded analytic representative of the true
defect (11), when \(f_N=\mathcal F_N\). This statement does not
divide by \(\mathcal F_N\), and it does not assert \(\mathcal D_N=0\).
The exact identities (12)--(15) apply to its nodal values.

The precise recurrence adapter is also useful. Use
\[
 A(r)=\frac{s_{r+1}^4}{s_{2r+1}s_{2r+2}},\qquad
 C(r)=\frac{s_r^4}{s_{2r}s_{2r+1}},\qquad C(0)=0,
\]
\[
 q_N(x)=\frac{C(Nx)}{A(Nx)},\quad
 d_N(x)=\frac{c_0-w}{A(Nx)},\quad
 T_N(x)=\begin{pmatrix}1+d_N(x)&q_N(x)/N\\
                         Nd_N(x)&q_N(x)\end{pmatrix}.
\]
Write the original bulk transfer as
\[
 X_{j+1}=T_N(x_j)X_j,\qquad
 Y_{j+1}=T_N(x_j)Y_j+T_N'(x_j)X_j,
\]
\[
 X_j=\binom{F_j}{N(F_j-F_{j-1})},\qquad
 Y_j=\binom{Nc'(j)G_j}
 {N^2[c'(j)G_j-c'(j-1)G_{j-1}]}.
 \tag{28}
\]
The derivative \(T_N'\) is in normalized degree \(x\). For any scalar
value interpolant \(f_N\), on a buffered interval where the preceding
node is also included, define
\[
 X_f(x)=\binom{f_N(x)}{N[f_N(x)-f_N(x-h)]},\qquad
 E_f(x)=X_f(x+h)-T_N(x)X_f(x).
 \tag{29}
\]
At every indicated grid point, \(X_f=X_j\) and \(E_f=0\).
Differentiating the off-grid definition (29), then subtracting (28),
gives the exact defect recurrence
\[
 \boxed{
 D_{j+1}=T_N(x_j)D_j-E_f'(x_j),\qquad
                    D_j=Y_j-X_f'(x_j).
 }
 \tag{30}
\]
Its first component is (11). A separately bounded interpolation of
\(Y_j\) does not remove the initial \(D_j\).

For \(f_N=\mathcal F_N\), the residual \(E_f\) and its derivatives
are polynomially bounded on a slightly smaller fixed strip.
The residual \(E_f\) vanishes at every interior grid node. The disk Blaschke
estimate proved in the two-channel source consequently gives, after
reducing the strip height and real interval by fixed buffers,
\[
                         E_f,\ E_f'=O(N^p e^{-cN})
 \tag{31}
\]
for some \(p,c>0\). To check this implication directly, choose fixed
concentric disks around each point of the smaller real interval.
The larger disk lies in the analytic strip; a fixed central real
subinterval contains \(c_1N\) grid zeros. On the smaller disk every
associated Blaschke factor is at most some \(q<1\). Their product
is at most \(q^{c_1N}\); Cauchy on another smaller disk controls
the derivative. A finite cover gives (31).
Thus the true defect is homogeneous up to exponentially small
forcing in the buffered bulk. This does not set its actual initial
coefficient to zero.

Those initial normals are part of the original source. For example,
put \(Q_N(w)=G_0(w)\), and use the just-defined unscaled coefficients.
At the first regular step,
\[
 U_0=c'(0)Q_N(w),\qquad U_j=c'(j)G_j,
\]
\[
 U_1=F_1U_0
       -\frac{(c_0-w)A'(0)}{A(0)^2}
       +\frac{c'(0)P_N(w)}{N^2s_1^2A(0)}.
 \tag{32}
\]
This formula is used only where that step is regular, in particular
for \(N\ge3\). It follows by differentiating the original off-grid
kernel equation at zero, using \(C(0)=C'(0)=0\) and
\(e_D'(c_0)=\eta/s_1^2\). The last term is the literal endpoint
source. For a microscopic real endpoint,
\(P_N(w)=4\cosh^2(\alpha/2)\), so it cannot be dropped.
Equation (32), or its propagation to a chosen bulk anchor, supplies
actual normal data; it is not a choice of integration constant.
Neither (32) nor the common-index Jacobi decomposition alone decides
whether (27) is small for the chosen global value interpolant.

## 5. Scope and direct-source readbacks

The note isolates the exact scalar compatibility question. It adds
no claim that a polynomially bounded pair of channels is a single
moderate scalar Hermite representative. The bulk sine primitive
removes no external connector, physical endpoint, fold band, odd
simple value, original crossing, or spectator. In particular it
does not give a filled-action estimate for the joined endpoint current.

All complete direct sources were read at the displayed versions,
with their used implications checked:

* [Original endpoint kernel and physical-value interpolation](research_full_period_endpoint_kernel_reduction.md),
  SHA256 a1d67ac803c0160bbfdacaa96a6fde9dc1ffae06fc39eb94f0416dcf2ecef76e:
  the ordinary low interpolant, full kernel, both parities, and
  original trace values and normals.
* [Actual high Fourier coefficients](research_endpoint_bulk_fourier_interpolation.md),
  SHA256 4f92c6081bf67646a14181bb753a903cf615d16adcd8d56d1534842303adb7eb:
  exact checkerboard coefficients and the bounded exact analytic
  bulk interpolant used in (16).
* [Microscopic two-channel interpolation](research_microscopic_endpoint_two_channel_interpolation.md),
  SHA256 44f6db0f8afdf1205ab8b0935b95b8a4fd9fa16c6414be2467b8b40a123c0ffe:
  exact prolonged transfer, polynomial analytic value and normal
  channels, and the quantitative dense-zero estimate.
* [Original all-color normal equation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_all_color_path_normal_bound.md),
  SHA256 08f8932c2cdee4c7afadbb4db3cd85480603f8adb4c936ce29a5517b2d4799c7:
  the endpoint source in (32) and its distinction from a chosen
  scalar degree interpolation.

Only written proofs, source-text reads and hashes were used.
No mathematical program, numerical experiment, test or build was run.
Frozen notes and public manuscripts were not changed.
