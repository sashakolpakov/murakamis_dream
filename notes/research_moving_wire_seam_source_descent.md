# Exact source descent with moving wire seams

Private written proof, 15 November 2026; uniform-domain addition,
16 November 2026.

The factorial joint source can be transported with wire seams that
depend on the angular variables. The necessary currents are explicit
differences of the angular primitives in the adopted joint-lens
theorem. They satisfy a strict corner compatibility identity, so the
descent requires only bulk and codimension-one seam terms.

This extends the allowed exact contour deformations. It gives no
exponential bound on the seam currents and does not turn them into
scalar Ward deletions.

## 1. Fixed original forms and admissible lifted charts

Fix \(N\ge2\) and \(D=N-1\). Use the entire original compiled source,
with its signed crossing
powers, optional canonical charge coupons, and unreduced free
boundary polynomial. Retain the notation and normalization of
the pinned joint-lens theorem:
\[
 d=|E|+|V|,\qquad C_{N,n}=e^{\pi i n(N-1)^2/(4N)},\qquad
 a_N=\pi-\frac{\pi}{2N},\qquad
 b_N=-\frac1{2N},\qquad I_N=[b_N,b_N+1],
 \tag{1}
\]
\[
 \Omega_{\rm fac}-\Omega_{\rm car}=d\Theta,\qquad
 \Theta=\sum_{v\in V}\Theta_v,\qquad
 \mathfrak c_N=N^{|E|}
       \prod_{v\in V}\left(-\frac{N^2C_{N,n_v}}{\pi i}\right).
 \tag{2}
\]
Here \(\Omega_{\rm fac}\) uses the exact factorial halfwires at
traced vertices. The cardinal representative remains at every
free spectral endpoint. The form \(\Omega_{\rm car}\) uses it
also at traced vertices. Both retain the factors
\[
 \sin t_v\,W_N(t_v)e^{in_vNt_v^2/(4\pi)}
                    \cos(N(1-\chi_v)t_v),\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-(-1)^{N-1}e^{-iNt})^2}.
 \tag{3}
\]
Neither the full trace kernel nor a coupon exponential is truncated.

Each \(\Theta_v\) is the specified primitive in \(t_v\), starting
at \(-a_N\), of the \(v\)-th representative defect after
\[
                 P_N(-2\cos t_v)W_N(t_v)=(-1)^N
 \tag{4}
\]
has canceled its trace poles. It omits \(dt_v\), is holomorphic
in that angular variable, and vanishes at both \(t_v=\pm a_N\).
It may retain the other original trace kernels. It contains every
wire differential \(dx_e\). All these assertions include the
odd ramified angular node and every first normal.

The factorial factors and these primitives are used only on
admissible lifted charts. In particular, the common domain
\[
       \Re x_e\in I_N,\qquad |\Re t_v|\le a_N
 \tag{5}
\]
and neighborhoods of its compact subsets are admissible at every
fixed finite height. The angular primitive paths in (2) lie in
the full corresponding vertical strip; their own trace poles
were canceled in (4). All other physical angular poles must be
avoided by the chains and their homotopies.

Let \(\tau_e\) translate \(x_e\) by one, leaving the other variables
unchanged. Near a lower wire face, both its lifted chart and the
translated upper chart are included. On a corner, all required
combinations of these translations are included. This is satisfied
by the explicit class in Section 4. No continuation through an
unrecorded factorial pole is assumed.

The cardinal top form is pointwise periodic:
\[
                       \tau_e^*\Omega_{\rm car}=\Omega_{\rm car}.
 \tag{6}
\]
Indeed each wire occurs in exactly two halfwires. Each cardinal
halfwire, direct or reflected, has multiplier
\(\eta=(-1)^{N-1}\), so their product has multiplier one.
This remains true at free polynomial endpoints.

## 2. Explicit bulk and seam currents

Define the \((d-1)\)-form on the lower seam chart by
\[
                       J_e=\tau_e^*\Theta-\Theta .
 \tag{7}
\]
It is a sum of at most \(|V|\) explicitly specified differences
of single-angular primitives. No unknown closing scalar is used.

**Proposition 1.** On every admissible overlap,
\[
 \boxed{\quad
  \tau_e^*\Omega_{\rm fac}-\Omega_{\rm fac}=dJ_e,\qquad
  (\tau_f^*-1)J_e=(\tau_e^*-1)J_f .
 \quad}
 \tag{8}
\]
The second identity holds as an equality of forms.

**Proof.** Apply \(\tau_e^*-1\) to (2), use (6), and commute
pullback with exterior differentiation. The second identity
is
\((\tau_f^*-1)(\tau_e^*-1)\Theta
 =(\tau_e^*-1)(\tau_f^*-1)\Theta\).
The deck translations commute. \(\square\)

Thus the bulk failure of periodicity is exactly the differential
of the seam current, and the alternating seam defect at a
codimension-two corner is zero. Higher descent forms may all be
set to zero. This is a finite descent representative of the
original form on the wire torus, relative to the angular endpoint
faces. The number of primitive summands is at most \(|E||V|\),
independent of \(N\); their coefficients and sizes are not
claimed independent of \(N\).

## 3. The corrected period on an angle-dependent cut

Let \(C\) be an oriented, compact, piecewise smooth joint chain
cut along every wire circle. Its upper and lower \(e\)-faces
must be paired by \(\tau_e\), with the induced opposite boundary
orientations. Denote by \(F_e\) the lower-face chain equipped
with the orientation pulled back from the upper face, so that
\[
                  \partial C=\sum_e(\tau_e F_e-F_e)+A.
 \tag{9}
\]
The chain \(A\) is the signed sum of angular faces. Each of these
keeps its relevant coordinate \(t_v=\pm a_N\). Wire-face
coordinates may depend on the angles and other wire variables;
they need not be constant. All corner pairings must agree.
The chain lies in the admissible charts of Section 1.

Set
\[
 \boxed{\quad
 \mathcal I_N(C)
      =\int_C\Omega_{\rm fac}-\sum_{e\in E}\int_{F_e}J_e .
 \quad}
 \tag{10}
\]

**Theorem 2.** The following exact identity holds:
\[
                         \mathcal I_N(C)=\int_C\Omega_{\rm car}.
 \tag{11}
\]
If \(C\) is connected to the original product wire/lens chain
by an admissible joint homotopy with paired wire faces and
coordinate-fixed angular endpoint faces, then
\[
                              Z_N=\mathfrak c_N\,\mathcal I_N(C).
 \tag{12}
\]
The result is coefficientwise in every unreduced free boundary
polynomial and remains true after its derivatives.

**Proof.** Apply Stokes to (2) on \(C\). The angular-face
pullback of \(\Theta\) is zero: its own primitive is zero there,
and every other summand contains that fixed angular differential.
The paired wire faces in (9) contribute exactly
\(\int_{F_e}(\tau_e^*\Theta-\Theta)=\int_{F_e}J_e\).
This proves (11), including its sign.

The cardinal form descends pointwise to the wire torus by (6).
It is closed away from the retained angular poles. Stokes on
the admissible homotopy therefore has cancelling paired wire
faces. The angular side faces contribute zero because their
fixed differential occurs in the top form. Thus its period
equals that on the original product chain, which is exactly
\(Z_N/\mathfrak c_N\) by the joint-lens theorem. This proves
(12). All operations are linear on the retained polynomial
coefficients. \(\square\)

In particular, the source can be transported through such a
homotopy without evaluating the angular traces first. The
currents in (10) supply the terms missing from a bulk-only
factorial calculation. The compatibility in (8) ensures that
moving several seams together creates no further uncancelled
corner descent term.

## 4. A concrete family inside the known factorial domain

The chart hypothesis admits genuinely angle-dependent seams
without any new analytic continuation. Parametrize each wire
by \(r_e\in[0,1]\), and the angular chains by real parameters
\(\mathbf s\). For bounded smooth real functions \(H_e\), put
\[
 x_e=b_N+r_e+iH_e(\mathbf r,\mathbf s),
 \tag{13}
\]
where each \(H_e\) is periodic in every wire parameter at the
paired faces, including its own. Let the angular coordinates
also depend periodically on \(\mathbf r\), stay in their
admissible lower strips, and retain their endpoint values
\(\pm a_N\) on the corresponding angular faces.
Then opposite wire faces differ exactly by \(\tau_e\).
Their heights may depend on all angular parameters.

Interpolate the functions \(H_e\) from constant heights by
\[
              H_e^\lambda=(1-\lambda)h_e+\lambda H_e .
 \tag{14}
\]
Its real wire coordinates remain in \(I_N\), and its imaginary
coordinates stay bounded on the compact parameter domain.
For fixed product angular chains this is an admissible homotopy using
only the compiler's domain (5). Theorem 2 therefore applies.
Further angular or interior wire deformations are allowed by
the same theorem when their stated domain and face conditions
are retained. This last allowance does not assert the existence
of a particular global steepest-descent deformation.

On a fixed wire face the pullback of every \(\Theta_v\) used
to vanish because it contained \(dx_e=0\). In (13),
the seam instead has \(dx_e=i\,dH_e\), so the current in
(10) is generally nonzero. This is the precise additional
term that allows the larger family of contours.

## 5. An even holomorphic class with zero integrated seam current

There is a narrower symmetry class in which the currents in (10)
vanish after their angular integrations. Its domain requirement
is stronger than smooth admissibility.

**Proposition 3.** Suppose every seam \(F_e\) is parametrized by
the other real wire parameters \(\mathbf r'\) and the full product
of angular lenses \(\prod_v\Gamma_v\). Write its wire coordinates
as \(X_f(\mathbf r',\mathbf t)\). Require that every \(X_f\)
is holomorphic and even in each angular variable on a product
of symmetric simply connected angular rectangles containing the
lenses, their reflections, and the intervals \([-a_N,a_N]\).
Require all substituted factorial factors, spectral quotients
and their angular primitive paths to remain in admissible
holomorphic charts on this product. Then
\[
                   \int_{F_e}J_e=0\qquad\hbox{for every }e.
 \tag{15}
\]
For chains satisfying the homotopy hypothesis of Theorem 2,
the bulk factorial integral alone therefore gives (12).

**Proof.** For fixed wire coordinates, the primitive coefficient
\(Q_v\) defining \(\Theta_v\) is even in \(t_v\): its derivative
is odd and its two symmetric endpoint values are zero.
Substituting the even functions \(X_f\) preserves that parity.
All \(dt_w\), \(w\ne v\), already occur in \(\Theta_v\).
Thus its seam pullback has, up to its fixed orientation sign,
coefficient
\[
 Q_v(X,\mathbf t)\,
 \det\left[
    \frac{\partial X}{\partial r'_1},\ldots,
    \frac{\partial X}{\partial r'_{|E|-1}},
    \frac{\partial X}{\partial t_v}\right].
 \tag{16}
\]
The first columns are even in \(t_v\), and the last is odd.
The coefficient is therefore odd in \(t_v\). It is holomorphic
through the physical \(t_v\)-nodes, since that trace kernel
was canceled before \(Q_v\) was formed. Its other trace
kernels remain at the fixed other angular arguments.
The integral of this odd holomorphic coefficient over the
full lens from \(-a_N\) to \(a_N\) is zero. Fubini gives
\(\int_{F_e}\Theta_v=0\). Translating one wire coordinate
by one preserves the same parity and argument, proving
\(\int_{F_e}\tau_e^*\Theta_v=0\) as well. Sum over \(v\)
to obtain (15). \(\square\)

The class is nonempty at every fixed level. Choose compact
symmetric angular rectangles as above and standard constant
wire cuts. The compiler gives an open holomorphic neighborhood
of that compact product, including all paired face lifts.
For bounded nonconstant even holomorphic functions \(f_e\),
set
\[
           X_e=b_N+r_e+ih_e+\varepsilon_N f_e(\mathbf t).
 \tag{17}
\]
Choose \(\varepsilon_N\ne0\) sufficiently small to keep the
entire compact product, and its straight homotopy from zero,
inside that neighborhood. These are compatible nonconstant
holomorphic seam embeddings, and Proposition 3 applies.

The open neighborhood matters. Requiring both ends of a
nonconstant holomorphic seam to stay in the exact closed
real-width-one strip would force its real part to be constant
and hence the seam itself to be constant on a connected
angular domain. Formula (17) instead uses the available
neighborhood margin. This neighborhood argument alone gives no
level-independent lower bound on \(|\varepsilon_N|\).

### A level-independent domain at sufficiently large wire height

The actual canonical factorial supplies a larger admissible domain.
It permits perturbations of fixed nonzero size, independent of \(N\).

**Corollary 4.** Fix \(T,\delta>0\), and use full product angular
lenses contained in
\[
             \mathcal R_T=\{t:|\Re t|<\pi,\ |\Im t|<T\}.
 \tag{17a}
\]
Their endpoints are still \(\pm a_N\). Choose fixed wire heights
\[
                         h_e>\frac{T}{2\pi}+\delta .
 \tag{17b}
\]
Let \(f_e(\mathbf t)\) be bounded holomorphic functions on
\(\mathcal R_T^{\,|V|}\), even in each angular variable, and
choose a fixed complex \(\varepsilon\) such that
\[
               |\varepsilon|\sup_e\|f_e\|_\infty<\delta/2 .
 \tag{17c}
\]
Set, for \(0\le\lambda\le1\),
\[
 X_e^\lambda=b_N+r_e+ih_e+\lambda\varepsilon f_e(\mathbf t),
                       \qquad 0\le r_e\le1 .
 \tag{17d}
\]
For every \(N\ge2\), these chains and all their paired seam lifts
are admissible. They satisfy the homotopy hypothesis of Theorem 2
and the zero-current conclusion of Proposition 3. Consequently
the full original source equals its bulk factorial integral on
each of these chains, with the unchanged prefactor \(\mathfrak c_N\).
The permitted perturbation size in (17c) is independent of \(N\).

**Proof.** The pinned canonical factorial is the original gamma
product, not a new solution of its recurrence. That product gives
\[
 G_N(\overline z)=\overline{G_N(z)}
 \tag{17e}
\]
on its initial strip: all bases of its complex powers are positive
real numbers, and the gamma function has this conjugation identity.
Its exact recurrence
\(G_N(z+1)=2\sin(\pi(z+1)/N)G_N(z)\) continues it as a nonzero
holomorphic function throughout the lower half-plane.
Conjugation gives the same assertion in the upper half-plane.
Equivalently, any nonreal point can be shifted horizontally by an
integer into the original strip; all sine factors used in that
finite continuation are nonzero. Thus there are no nonreal
zeros or poles and no additional periodic factor to choose.

Write \(H_e'=\Im X_e^\lambda\). Equations (17b)--(17d) give
\[
                     H_e'>T/(2\pi)+\delta/2 .
 \tag{17f}
\]
For a direct halfwire with argument \(y=X_e^\lambda\), the three
factorial arguments therefore satisfy
\[
 \begin{aligned}
 \Im(Ny)&>N\delta/2,\\
 \Im\{D/2-Ny+Nt_v/(2\pi)\}&<-N\delta/2,\\
 \Im\{D/2-Ny-Nt_v/(2\pi)\}&<-N\delta/2 .
 \end{aligned}
 \tag{17g}
\]
For a reflected halfwire \(y=D/N-X_e^\lambda\), all three
signs reverse, with the same strict bounds. The offset \(D/2\)
is real. Real translations of any wire, including every paired
face or corner lift, do not change these inequalities.
All denominator factorials are consequently holomorphic units
on an open neighborhood of every compact piece of this domain.
Their real parts need not lie in the old width-one strip.

The same check applies to the full angular primitive paths:
hold the wire coordinates frozen at the substituted values
\(X^\lambda(\mathbf t)\), and vary the integrated angle within
\(\mathcal R_T\). Inequality (17f) remains available, and (17g)
still holds. The full-Hermite identity between the factorial and
cardinal representatives holds for every complex index. Thus
their quotient by \(P_N(-2\cos t_v)\) has removable singularities
at every physical node in this rectangle, including the
odd ramified node. There are no other zeros of that polynomial
in \(|\Re t_v|<\pi\). This constructs the same holomorphic
primitive \(\Theta_v\) on the enlarged domain, with its original
normalization at \(-a_N\).

At \(\lambda=0\) the chain is the original constant-height
wire-period representation, which is exact at every height.
The homotopy (17d) remains pole-free, fixes all angular endpoint
faces, and pairs each wire face by its actual unit translation.
Its embeddings are even and holomorphic on the whole angular
product. Theorems 2 and Proposition 3 now give the assertions.
\(\square\)

This class is explicitly nonconstant when a wire and an angular
variable are present. For example,
\[
       f_e(\mathbf t)=\frac{t_v^2}{1+\pi^2+T^2},
                  \qquad \varepsilon=\delta/4
 \tag{17h}
\]
for at least one wire, with any of the remaining \(f_e\) set to
zero, obeys (17c) for all levels. The functions, heights and
nonzero perturbation size are fixed before \(N\) varies.
The real strip may enlarge by a fixed bounded amount; the
nonreal factorial bounds, not the old real-width constraint,
justify that enlargement.

The assertion is uniform in the allowed deformation size only.
It is not a uniform upper bound on the factorials, the bulk
integral or their exponential rates. The high-height source
representation is exact, but no deformation from it to a
geometric contour with controlled complement has been proved.

Nor does Proposition 3 apply to an arbitrary coupled angular
collar: it uses full angular product lenses, not only a
geometric patch with different boundary. A local even
stationary wire function is not asserted to extend to the
entire required product domain.

## 6. Removed trace kernels do not give nilpotent deck transport

Every summand of \(J_e\) has its designated \(v\)-th trace
kernel canceled before angular integration. A deck translation
does not reintroduce that kernel. This makes the currents
explicit members of the actual source complex; it does not
make them scalar graph deletions.

Nor does iteration necessarily cancel more trace kernels.
For one direct halfwire set
\[
 \eta=(-1)^{N-1},\qquad
 d_N(x)=\frac{(-1)^N}{4\sin^2(\pi Nx)} .
 \tag{18}
\]
The literal factorial period law is
\[
 \tau^*B_N=(\eta+P_N(-2\cos t)d_N(x))B_N,\qquad
                         d_N(x+1)=d_N(x).
 \tag{19}
\]
Consequently, for every integer \(k\ge1\),
\[
 \boxed{\quad
   (\tau^*-\eta)^kB_N
       =P_N(-2\cos t)^k d_N(x)^k B_N .
 \quad}
 \tag{20}
\]
This follows inductively because the multiplier in (19)
is itself periodic. It is not identically zero off the
physical spectrum. The equalities are meromorphic identities
and are used only on the admitted regular charts.

Thus powers of the spectral relation are not nilpotent in
the analytic integrand. Once one \(P_N\) has canceled a
\(W_N\), its further powers retain the same removed-kernel
set; they do not force a triangular sequence of new vertex
deletions. The finite length of (8) comes instead from the
explicit common primitive and commuting translations.

The descent theorem supplies an exact finite transport law
for the whole source, including moving seams. It does not
bound the integrals of \(J_e\), their local patch boundaries,
or the remaining joint bulk. In particular, it provides no
automatic geometric coefficient, action gap, or comparison
with the scalar Ward-deletion currents.

## Direct sources

The complete source proofs were read and their directly used
implications checked at these versions.

* [Joint factorial lens source](research_joint_factorial_lens_relative_source.md),
  SHA256 a14ca148bd55b36b1eea9de8be8a63025532c3bbbb928482b0d7cb8edae56e54:
  original normalization, explicit \(\Theta\), all parity and
  ramification conditions, common domain and factorial period law.
* [Arbitrary-power compiler](research_arbitrary_power_source_compilation.md),
  SHA256 55e2de84870cfd20dac5922791dbc2bed54909439dfbf4663f17c70a1089445f:
  actual paired-wire topology, direct/reflected halfwires, free
  polynomial boundaries and the joint holomorphic domain.
* [Finite Fourier band](research_newton_interpolation_finite_fourier_band.md),
  SHA256 2e2d95184081ba6440b56268cb597624d97a5f1931e8c0df886fa754e6684304:
  full-Hermite cardinal interpolation and its exact paired
  periodicity.
* [Exact canonical factorial](research_exact_cyclotomic_factorial.md),
  SHA256 0f989261f53747266ac62dba40ca7548138012b266521e98a03bd94b450c657b:
  the fixed gamma product, its exact shift continuation and the
  zero-free nonreal half-planes used in Corollary 4.

Only written proofs, source-text reads and file hashes were used.
No mathematical code, numerical evaluation, test or compilation
was run. Frozen notes, manuscripts and public files were unchanged.
