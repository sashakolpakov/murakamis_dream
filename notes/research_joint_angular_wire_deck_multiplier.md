# Exact angular deck multipliers at joint wire ends

Private written proof, 16 November 2026.

The original factorial halfwire has an explicit Möbius multiplier under
an angular deck turn. Multiplying these factors gives the exact defect
at a vertex of arbitrary degree, including a specified subset of
escaping wires. Its leading bulk defect can cancel in a precisely stated
resonance. That cancellation does not remove the original relative
current: the retained angular primitive carries the difference from
the cardinal source, whose wire residue still contains the original
edge kernels.

The statements are on supplied common continuation charts. They do not
construct a global angular deck homotopy, bound its exterior, or select
the regular lattice alias as the original relative cycle.

## 1. One actual halfwire

Fix \(N\ge2\), \(D=N-1\), \(\eta=(-1)^D\), and
\[
 B_N(x,t)=
 \frac{N}{G_N(D/2-Nx+Nt/(2\pi))
          G_N(D/2-Nx-Nt/(2\pi))G_N(Nx)^2}.
 \tag{1}
\]
This is the original canonical factorial, with its fixed gamma-product
normalization. Its one-step recurrence implies
\[
 G_N(z+N)=-2\sin(\pi z)G_N(z).
 \tag{2}
\]
Indeed the product of the \(N\) sine factors is
\(\prod_{j=1}^N2\sin(\pi(z+j)/N)=2\sin(\pi(z+1))\).
Both identities are meromorphic identities of the specified function.

Put
\[
 w=e^{-2\pi ix},\qquad y=e^{-iNt},\qquad
 d_N(w,t)=\frac{w^N-\eta y}{1-\eta y w^N},\qquad
 \mathcal D_\epsilon t=t-2\pi\epsilon,\quad \epsilon=\pm1 .
 \tag{3}
\]
Then exactly
\[
 \boxed{\quad
 B_N(x,t-2\pi\epsilon)=d_N(w,t)^\epsilon B_N(x,t).
 \quad}
 \tag{4}
\]
For \(\epsilon=1\), set
\(A=D/2-Nx+Nt/(2\pi)\), \(B=D/2-Nx-Nt/(2\pi)\).
The two arguments become \(A-N,B+N\). Equation (2) gives the
ratio \((-1)^N\sin(\pi A)/\sin(\pi B)\), which is (3).
The multiplier is \(2\pi\)-periodic in \(t\); reversing the shift
proves the other sign. The displayed quotient is used on a regular
chart, or after clearing its denominator. It does not remove zeros
or poles of the actual factors.

For a reversed halfwire \(x'=D/N-x\), its \(N\)-th wire exponential
is \(w^{-N}\), and
\[
                        d_N(w^{-1},t)=d_N(w,t)^{-1}.
 \tag{5}
\]
Thus original wire orientations are retained explicitly.

There is a useful warning at the physical angular nodes
\(\tau_j=\pi(D-2j)/N\). For \(w^N\ne1\), \(y(\tau_j)=\eta\), and
\[
 d_N(w,\tau_j)=-1,\qquad
 \partial_t d_N(w,\tau_j)
       =iN\,\frac{1+w^N}{1-w^N}.
 \tag{6}
\]
At an unramified preimage the corresponding spectral derivative is
the second expression divided by \(2\sin\tau_j\). The derivative of
\(d_N^\epsilon\) is \(\epsilon\partial_t d_N\) there. Thus an angular
deck turn of the factorial is not its unchanged polynomial spectral
representative. At the odd ramified node only its original value
enters the trace; no spectral derivative is imposed there. The
exceptional simultaneous specialization \(w^N=1,y=\eta\) is not
evaluated by (6): at the physical wire indices (1) is its original
polynomial and the cancelled whole expression must be used.

## 2. Composition at an arbitrary vertex

At one traced vertex retain its signed integer Gaussian power \(n\),
its actual polynomial coupon \(C_c(z)\), and every other polynomial
spectator, with \(z=-2\cos t\). Denote by \(\Omega_{\rm mix}\) a
literal mixed joint form: a specified list \(\mathcal J\) of its
incidences uses (1), while every other incidence at this vertex uses
the cardinal polynomial. This is an allowed representative change
only with the corresponding original relative primitive retained.
All free spectral endpoints remain cardinal.

For \(j\in\mathcal J\), let its argument be
\(x_j'=x_{e(j)}\) or \(D/N-x_{e(j)}\), with sign
\(\delta_j=1\) or \(-1\), respectively. Set
\[
 M_{n,\epsilon}(t)=(-1)^{nN}e^{-inN\epsilon t}.
 \tag{7}
\]
On a common chart for the form and its deck pullback,
\[
 \boxed{\quad
 \mathcal D_\epsilon^*\Omega_{\rm mix}
   =M_{n,\epsilon}(t)
      \prod_{j\in\mathcal J}
           d_N(e^{-2\pi ix_{e(j)}},t)^{\epsilon\delta_j}
          \Omega_{\rm mix}.
 \quad}
 \tag{8}
\]
The sine differential and original trace kernel are periodic. The
Gaussian contributes (7), and every polynomial spectator is periodic.
Equation (4) supplies the remaining factors. Loops and repeated
incidences are counted literally; opposite orientations of the same
wire cancel their multipliers by (5).

If instead the unwrapped representative
\(\cos(N(1-c)t)\) is used, remove that cosine from
\(\Omega_{\rm mix}\) and multiply the resulting form by the additive
defect
\[
 M_{n,\epsilon}\prod_{j\in\mathcal J}d_j^{\epsilon\delta_j}
       \cos(N(1-c)(t-2\pi\epsilon))
                    -\cos(N(1-c)t).
 \tag{9}
\]
No quotient by a cosine is used. Equality of full physical Hermite
data does not identify these two continuations on a partial deck face.

## 3. A prescribed set of wire ends

Choose a subset \(\mathcal E_\infty\) of the incident wires and a
direction \(\sigma_e=\pm1\) for each, and put
\[
 v_e=e^{-2\pi i\sigma_e x_e}\longrightarrow0 .
 \tag{10}
\]
This includes the lower and upper escaping ends. Let
\(\mathcal J_\infty\) be the factorial incidences in
\(\mathcal J\) belonging to these wires. For each such incidence set
\[
 p_j=\sigma_{e(j)}\delta_j,\qquad
 a=n+\sum_{j\in\mathcal J_\infty}p_j,\qquad
 \rho_j=
 \frac{1-\eta e^{ip_jNt}v_{e(j)}^N}
      {1-\eta e^{-ip_jNt}v_{e(j)}^N}.
 \tag{11}
\]
The original reversed-wire offset has \(N\)-th exponential one, so
no omitted offset remains in (11). Direct substitution in (3) gives
\[
 d_N(e^{-2\pi ix_e},t)^{\delta_j}
       =(-1)^N e^{-ip_jNt}\rho_j .
 \tag{12}
\]
Since the number of these incidences and \(\sum p_j\) have the same
parity, their signs combine with (7) to give the exact formula
\[
 \boxed{\quad
 \mathcal D_\epsilon^*\Omega_{\rm mix}-\Omega_{\rm mix}
   =\left[A_\epsilon
                   \prod_{j\in\mathcal J_\infty}\rho_j^\epsilon-1\right]
                      \Omega_{\rm mix},\qquad
 A_\epsilon=M_{a,\epsilon}
       \prod_{j\in\mathcal J\setminus\mathcal J_\infty}
                    d_j^{\epsilon\delta_j}.
 \quad}
 \tag{13}
\]
Here the remaining wire variables and \(t\) are retained, rather than
specialized to stationary values.

On a compact regular chart the rational product in (13) is holomorphic
at \(\mathbf v=0\), with value one. In the ring of holomorphic germs
there,
\[
 \prod_j\rho_j^\epsilon-1
                  \in (v_e^N:e\in\mathcal E_\infty).
 \tag{14}
\]
Consequently the multiplier defect in (13) belongs to this ideal
if and only if \(A_\epsilon-1\) is identically zero on the retained
boundary chart. Its vanishing at a single stationary point does not
give this germ identity.

In particular, if all factorial incidences at this vertex are among
the specified ends, \(A_\epsilon=M_{a,\epsilon}\). On an open angular
chart its value is identically one exactly when \(a=0\). At that
resonance (14) gives regular lattice-alias powers, at least one
escaping wire in every term; it does not assert divisibility by
their product. For example, when \(\epsilon=1\) the telescoping
product uses
\[
 \rho_j-1=
 \frac{\eta(e^{-ip_jNt}-e^{ip_jNt})v_{e(j)}^N}
      {1-\eta e^{-ip_jNt}v_{e(j)}^N}.
 \tag{15}
\]
The inverse factors for \(\epsilon=-1\) have the same order.
These are exact statements about the multiplier. The covering factors
\(x_e\log R_{N,t}\) in the factorial itself remain present.

For a useful uniform estimate, suppose
\[
       |\Im t|\le T,\qquad
       e^T\max_e|v_e|\le r<1.
 \tag{16}
\]
Then, for a fixed incidence list and all \(N\ge2\),
\[
 \left|\prod_j\rho_j^\epsilon-1\right|\le C_{\mathcal J,r}r^N .
 \tag{17}
\]
Each numerator or denominator correction has modulus at most \(r^N\);
its inverse is bounded by \((1-r^N)^{-1}\).
Telescoping a fixed product proves (17). Fixed angular derivatives
have the same estimate with an additional fixed power of \(N\),
by differentiating these explicit rational factors.
This bounds the multiplier defect, not the remaining density.

## 4. What choosing the decaying deck multiplier does

When \(A_\epsilon=M_{a,\epsilon}\), take
\[
                  t=\epsilon\pi+\xi/N+ih,
 \tag{18}
\]
with real bounded \(\xi\), bounded \(h\), and \(|h|\ge h_0>0\).
Exactly
\[
              M_{a,\epsilon}(t)
                  =e^{aN\epsilon h-ia\epsilon\xi}.
 \tag{19}
\]
If \(a\ne0\), (17) implies that the multiplier defect in (13) has
exponential rate \(\max(0,a\epsilon h)\), uniformly on compact
sets where these assumptions hold. More explicitly its magnitude
is bounded above and below by fixed positive multiples of
\(\exp(N\max(0,a\epsilon h))\) for all sufficiently large \(N\).
If \(a=0\), only the exponentially small multiplier bound (17)
is supplied; the whole source factor has not been estimated.

An oriented paired face can be written using either side. For any
nonzero multiplier \(A\),
\[
                   (A-1)\omega=(1-A^{-1})(A\omega).
 \tag{20}
\]
Thus choosing the decaying inverse multiplier does not reduce the
rate of the defect: the growth is in the transported density
\(A\omega\). This is an exact identity, not a claim that further
coherent cancellation or a different relative-chain estimate is
impossible.

## 5. The saturated geometric row restricts the bulk resonance

This section concerns the original direct same-index circle-tree
chart. Assume the finite-real-period hypotheses of the pinned
compactness theorem: a proper selected subset of a connected tree,
complete outside angles, fixed positive charges, a supplied strict
feasible angle point, and a positive approach with bounded real
periods. Keep its actual limiting returns
\(r_{ve}=k_{ve}+ig_{ve}\) and angles \(t_v=s_v+ih_v\).
At a saturated selected vertex write \(s_v=\epsilon\pi\).
The half-angle cosine is a unit, so \(h_v\ne0\). Put
\(\tau=\operatorname{sign}h_v\).

Every incidence satisfies
\[
 |s_v|+2|g_{we}|\le\pi,\qquad
 |s_w|+2|g_{ve}|\le\pi .
 \tag{21}
\]
Hence \(g_{we}=0\). The two square coordinates with real coordinate
\(s_v/4=\epsilon\pi/4\) cannot lie on an open side, by finite
square-covector compactness. Their other coordinates
\(g_{ve}/2\pm s_w/4\) must each have modulus \(\pi/4\).
It follows that either
\[
 (s_w,g_{ve})=(0,\ \pm\pi/2)
       \quad\hbox{or}\quad
 (s_w,g_{ve})=(\pm\pi,\ 0).
 \tag{22}
\]
For a zero-real-angle neighbor write
\[
 a_v=iC,\ C=\coth(h_v/2),\qquad
 a_w=iB,\ B=\tanh(h_w/2).
 \tag{23}
\]
Here \(|C|>1\), \(|B|<1\).
The limiting square root is \(q_e=iQ\), where
\(Q^2=C^2+B^2-1<C^2\). Thus \(Q+C\) has the sign of \(h_v\).
The actual half-return identity
\[
                 e^{r_{ve}}=\cos(t_w/2)(q_e+a_v)
 \tag{24}
\]
and its retained range \(|g_{ve}|\le\pi/2\) now force
\(g_{ve}=\tau\pi/2\). This also covers a complete outside neighbor,
where \(h_w=B=0\).

Let \(d_0(v)\) count the zero-real-angle neighbors. The imaginary
part of the original primitive equation is therefore exactly
\[
                     \epsilon n_v-2c_v=\tau d_0(v).
 \tag{25}
\]
For any nonempty subset of \(m\) escaping incidences
\(q_e=\sigma_e i\), the pinned escape classification gives
\(\sigma_e=\epsilon\tau\); in particular \(m\le d_0(v)\).
For the mixed representative using factorials on precisely this
subset, its effective exponent in (11) is
\[
              a=\epsilon\{2c_v+\tau(d_0(v)+m)\}.
 \tag{26}
\]
Resonance \(a=0\) is impossible when \(h_v>0\). When \(h_v<0\)
it requires \(2c_v=d_0(v)+m\). If \(0<c_v\le1\), this requires
\[
                     c_v=1,\qquad d_0(v)=m=1.
 \tag{27}
\]
Other neighbors may still have real angle \(\pm\pi\); (27) is not
an exclusion of every partial-star resonance.

Strict feasibility gives an additional general restriction. Under
resonance, (25)--(26) give \(n_v=\epsilon m\) and
\(2c_v=d_0(v)+m\). At the supplied strict feasible point,
\[
 \pi c_v=\left|n_vs_v/2-\sum_e g_{ve}\right|
                 <\frac{\pi}{2}(|n_v|+d_v).
 \tag{28}
\]
Consequently \(d_v>d_0(v)\): a resonating vertex must have a
neighbor whose real angle is also saturated. In particular an
isolated saturated star cannot resonate, even if only some of its
cut edges escape. If every incidence escapes, all its neighbors
have real angle zero, so this excludes that case as well.
This conclusion uses strict feasibility only for (28); it does not
assert that a classified escape actually occurs in the inverse-period
component of the geometric center.

## 6. The original relative current is still present

Keep the canonical polynomial charge coupon in this section. On any
supplied common admitted chart, the same telescope used in the
joint-lens theorem gives for the chosen mixed representative
\[
                    \Omega_{\rm mix}-\Omega_{\rm car}=d\Theta_{\rm mix}.
 \tag{29}
\]
It retains the specified primitive paths and every original angular
pole, wire seam, and free boundary coefficient. This is not an
assertion that such a chart exists along an arbitrary deck homotopy.
Applying the actual deck pullback gives the exact identity
\[
 \boxed{\quad
 \mathcal D_\epsilon^*\Omega_{\rm mix}-\Omega_{\rm mix}
   =(M_{n,\epsilon}-1)\Omega_{\rm car}
       +d(\mathcal D_\epsilon^*\Theta_{\rm mix}-\Theta_{\rm mix}).
 \quad}
 \tag{30}
\]
The first multiplier in (30) has the original power \(n\), not the
effective bulk power \(a\). Equation (30) is a direct consequence of
(29) and periodicity of every cardinal spectral factor; it includes
all first normals and the odd simple node.

For each direct cardinal wire, with its other endpoint retained,
\[
 F_{e,N}\,dx_e
       =-\frac{K_T}{2\pi iN}\frac{dw_e}{w_e}+d_{w_e}V_{e,N},
 \qquad
 V_{e,N}=\sum_{m\ne0}\frac{A_{e,m}w_e^{-m}}{2\pi i m}.
 \tag{31}
\]
For a reversed pairing retain its actual \(K_I\) version.
Angular deck transport acts coefficientwise in (31), so the
compactification residue of the cardinal term in (30) is still the original kernel
multiplied by \(M_{n,\epsilon}-1\), with the unchanged orientation
and \(N\)-normalization. Iterated complete wire residues retain the
product of the original kernels. They do not extract the extreme
crossing-power coefficient.

The remaining terms in this exact relative decomposition contain
both \(V_{e,N}\) and \(\mathcal D_\epsilon^*\Theta_{\rm mix}
-\Theta_{\rm mix}\), together with their recorded wire seam
differences. On a partial angular face or incomplete wire cap these
terms need not vanish. In particular (14) at a resonant bulk end
does not prove that the corrected source has become the regular
\(v_e^N\) lattice alias. Equation (30) explicitly retains the
original-kernel angular current that such an inference would omit.
This remains true if the geometric effective-power cancellation is
proved before any estimate.

The finite-real-period energy gap bounds the specified retained
classical action away from its center. Equations (13), (20), and (30)
do not identify every density on these sides with that action. A
useful further theorem must control or pair the full relative terms
in (30)--(31), with the same exterior, and exhibit the actual chain
that selects completed regular alias caps. No lower bound, geometric
cycle multiplicity, or global obstruction to such a theorem is
deduced here.

## Direct sources and proof scope

* Canonical factorial:
  research_exact_cyclotomic_factorial.md,
  SHA256 0f989261f53747266ac62dba40ca7548138012b266521e98a03bd94b450c657b.
  Fixed function, recurrence, and half-plane continuation.
* Stationary wire current:
  research_stationary_wire_escape_current.md,
  SHA256 03f902ea70818cf8432dd3d947822b49d1f762487552b20dac7e431b8222aa4e.
  Exact end covering factors, Laurent primitive, original kernel,
  carriers, and the constrained escape signs.
* Joint factorial source:
  research_joint_factorial_lens_relative_source.md,
  SHA256 a14ca148bd55b36b1eea9de8be8a63025532c3bbbb928482b0d7cb8edae56e54.
  Exact mixed representatives, full normals, original primitive paths
  and angular factors.
* Moving seams:
  research_moving_wire_seam_source_descent.md,
  SHA256 2b632735243fc450e2ce0f276f339c9fad0b5524724364b83f15690b4896f33d.
  Admitted-chart and wire seam requirements.
* Angular face identities:
  research_joint_angular_face_source_identities.md,
  SHA256 1870769e1684fc9fdd9e4491c24e658eb1aed135ae18fcc6c1f583a1c8ba2848.
  Original polynomial-coupon deck law, residue placement, and the
  distinction from its unwrapped cosine representative.
* Finite real-period compactness:
  research_real_period_image_compactness.md,
  SHA256 8ecdecc2c71e8a47a83fe60986ed618abaa926937920f376abebed779fb0c37e.
  Original square coordinates, bounded sharp-corner limits,
  half-angle units, strict feasible point, and retained period rows.

Only written proofs, source-text reads, and hashes are used.
No mathematical code, numerical evaluation, test, or compilation
was performed. Frozen notes and public documents are unchanged.
