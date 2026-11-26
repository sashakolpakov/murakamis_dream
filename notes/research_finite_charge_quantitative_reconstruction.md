# Quantitative reconstruction of the canonical finite charge source

Private written proof, 16 November 2026.

Two consecutive blocks of lattice charge observations recover the
canonical polarized charge function, including its first-normal
blocks. For the actual cosine source, its exact charge reflection
reduces this to one full block of \(N\) samples. The recovery has
polynomial cost on bounded real charge
sets and an explicit, sharp exponential cost in a complex direction.
It is different from reconstructing a contour-polarized family.
The known small-charge initializer does not provide this full unit
charge block with the required uniform error.

The signed period difference and its discrete Fourier transform
already occur in
[the actual charge equation, §§12–13](research_current_free_aw_crossing_transport.md#12-the-physical-charge-equation-has-two-channels).
The [Fourier–Hermite Gram](actual_filling_fourier_hermite_gram.md)
gives polynomially conditioned physical-jet coordinates, and the
[one-sided angular projection](research_one_sided_hermite_projection.md)
changes angular representatives. The additional result below is a
continuous-charge reconstruction with quantitative error bounds,
using the canonical finite charge normal form.

## 1. The actual charge space and its two sample blocks

Fix \(N\ge2\), \(D=N-1\), \(\eta=(-1)^D\), and \(m=\lfloor N/2\rfloor\).
Use \(y=1-\chi\) and
\[
 \lambda_a=\pi(D-2a),\qquad 0\le a\le D.
 \tag{1}
\]
The canonical polarized observation of an original boundary class
\(f\in\mathcal A_N\) is
\[
 F_\sigma(y)=\phi_N\!\left(f\exp_{\mathcal A_N}
                                  (\sigma iNyL_N)\right),
 \qquad \sigma\in\{+1,-1\}.
 \tag{2}
\]
The complete finite normal form proved in the polarization source is
\[
 F_\sigma(y)=
 \sum_{a=0}^{m-1}(u_a+yv_a)e^{\sigma i\lambda_a y}
       +\mathbf1_{N\ {\rm odd}}u_*.
 \tag{3}
\]
All coefficients depend linearly on the full original values and
first normals of \(f\). No normal is omitted: the coefficients of
\(y e^{\sigma i\lambda_a y}\) recover the values, and the other
coefficients then recover the first normals. The odd simple node
contributes only \(u_*\).

For the cosine observation
\[
 F(y)=\phi_N(f\mathcal C_{N,1-y}),
 \tag{4}
\]
its positive and negative generalized frequencies give exactly
\[
 F_\sigma=(2\Pi_\sigma+\Pi_0)F.
 \tag{5}
\]
Here \(\Pi_\sigma\) retains the frequencies
\(\sigma\lambda_a\), \(0\le a<m\), together with their linear
polynomial factors, and \(\Pi_0\) retains the odd constant.
This is the actual canonical coupon projection.

Both (3) and (4) belong to the larger space
\[
 \mathcal B_N=
 \left\{\sum_{a=0}^{D}(U_a+yV_a)e^{i\lambda_a y}\right\}.
 \tag{6}
\]
Its dimension is \(2N\). Every \(F\in\mathcal B_N\) obeys
\[
 B(y):=\eta F(y+1)-F(y)=\sum_aV_a e^{i\lambda_a y},
 \qquad
 A(y):=F(y)-yB(y)=\sum_aU_a e^{i\lambda_a y}.
 \tag{7}
\]
Indeed \(e^{i\lambda_a}=\eta\). Thus the first difference in (7)
retains the normal channel; replacing it by signed periodicity
would lose that channel.

Set \(y_j=j/N\), \(0\le j<N\), and retain the \(2N\) samples
\[
 d_j=F(y_j),\qquad d_{j+N}=F(y_j+1).
 \tag{8}
\]
They are the original charge lattice \(\chi=1-j/N\), over two
consecutive blocks. Define
\[
 B_j=\eta d_{j+N}-d_j,\qquad A_j=d_j-y_jB_j.
 \tag{9}
\]
Ordinary finite Fourier orthogonality gives the explicit inverse
\[
 V_a=\frac1N\sum_{j=0}^{N-1}e^{-i\lambda_a y_j}B_j,
 \qquad
 U_a=\frac1N\sum_{j=0}^{N-1}e^{-i\lambda_a y_j}A_j.
 \tag{10}
\]
For example, \(e^{-i\pi Dy}B(y)=\sum_aV_ae^{-2\pi iay}\);
the \(N\) frequencies are distinct modulo \(N\). This proves
(10), and also proves that (8) determines the whole of (6).
There is no division by an unknown source scalar.

For the actual cosine source there is a stronger reconstruction.
Its normal form is even in \(y\), and (7) gives the exact relation
\[
 F(y+1)+F(y-1)=2\eta F(y).
 \tag{10a}
\]
Consequently the first block alone determines the second:
\[
 d_N=\eta d_0,\qquad
 d_{N+j}=2\eta d_j-d_{N-j}\quad(1\le j<N).
 \tag{10b}
\]
Equivalently these are the full-quotient Chebyshev relations
\(T_{N+j}(-z/2)+T_{N-j}(-z/2)=2\eta T_j(-z/2)\),
since \(T_N(-z/2)=\eta\) in \(\mathcal A_N\).
They preserve the first normals. Substitution into (9) gives
\[
 \begin{aligned}
 &B_0=0,\qquad A_0=d_0,\\
 &B_j=d_j-\eta d_{N-j},\qquad
 A_j=(1-y_j)d_j+\eta y_jd_{N-j}\quad(1\le j<N).
 \end{aligned}
 \tag{10c}
\]
Equations (10), (10c), and (5) reconstruct the canonical polarized
observation from the \(N\) original cosine observations at
\(\chi=1-j/N\), \(0\le j<N\). Charge zero is already determined
by charge one. This does not assert a signed-period law for the
normal blocks: the nonzero difference \(B_j\) is still retained.

## 2. Exact interpolation and its complex error bound

Define the finite kernels
\[
 K_{\sigma,N}(z)=
 2\sum_{a=0}^{m-1}e^{\sigma i\lambda_a z}
                  +\mathbf1_{N\ {\rm odd}}.
 \tag{11}
\]
Their total coefficient weight is \(2m+\mathbf1_{N\ {\rm odd}}=N\).
Substituting (9) into (10) and applying (5) proves
\[
 \boxed{\quad
 F_\sigma(y)=\frac1N\sum_{j=0}^{N-1}K_{\sigma,N}(y-y_j)
       \bigl[(1+y_j-y)d_j+\eta(y-y_j)d_{j+N}\bigr]
 -\mathbf1_{N\ {\rm odd}}\frac yN\sum_{j=0}^{N-1}B_j.
 \quad}
 \tag{12}
\]
This formula reconstructs the polarized observation from the
cosine observations (8), not merely from already polarized data.
The factor two in (11) is absent at the odd simple frequency.
The final term projects away the linear zero-frequency coefficient.
It is zero for the exact cosine data, since their odd zero-frequency
block is constant. Keeping it in (12) makes the reconstruction land
in the canonical space even for noisy data.
If the supplied data are instead those of (3), the analogous
direct reconstruction replaces the factor two by one; it retains
the odd constant once.

Let \(\widehat d\) be arbitrary approximate samples with
\[
             \max_{0\le j<2N}|\widehat d_j-d_j|\le\delta_N.
 \tag{13}
\]
Apply the right side of (12) to these data and call its output
\(\widehat F_\sigma\). Since \(0\le y_j<1\) and
\(0<\lambda_a\le\pi D\) for \(a<m\),
\[
 |K_{\sigma,N}(y-y_j)|
       \le N e^{\pi D(-\sigma\Im y)_+},
 \qquad
 |1+y_j-y|+|y-y_j|\le3+2|y|.
 \tag{14}
\]
Here \(r_+=\max(r,0)\). At even levels these inequalities immediately
bound the reconstruction. At odd levels separate the nonzero
frequencies, of total weight \(N-1\), from the corrected constant.
The latter is \(N^{-1}\sum_j A_j\), whose error is at most
\(3\delta_N\). Thus at either parity
\[
 \boxed{\quad
 |\widehat F_\sigma(y)-F_\sigma(y)|
 \le N(3+2|y|)\delta_N
                  e^{\pi D(-\sigma\Im y)_+}.
 \quad}
 \tag{15}
\]
The same bound holds for the direct reconstruction from polarized
samples. Equations (9)–(10) also give the separate coefficient bounds
\[
 |\Delta V_a|\le2\delta_N,\qquad
 |\Delta U_a|\le3\delta_N.
 \tag{16}
\]
All formulas hold at both parities, including \(N=2\).
They hold with coefficients in any normed vector space, by the
same triangle inequalities; in particular ordinary free-boundary
parameters and fixed derivatives may be retained.

For the actual cosine source, suppose instead that only its first
block is approximated, with error at most \(\delta_N\). Construct
\(A_j,B_j\) by (10c) before applying (10) and (5). Their errors
satisfy
\[
 |\Delta B_j|\le2\delta_N,\qquad |\Delta A_j|\le\delta_N,
 \tag{16a}
\]
because the two coefficients of \(A_j\) have absolute values
\(1-y_j,y_j\). The Fourier coefficients have the same bounds.
The projection in (5) has total coefficient weight \(N\), so
\[
 \boxed{\quad
 |\Delta F_\sigma(y)|\le
       N(1+2|y|)\delta_N e^{\pi D(-\sigma\Im y)_+}.
 \quad}
 \tag{16b}
\]
At odd levels \(\eta=1\) and \(\sum_jB_j=0\) follows from
\(j\leftrightarrow N-j\), even for the approximate first block.
Thus no artificial linear zero-frequency term enters this
single-block reconstruction.

The real sample block may start at any real \(y_0\): apply the
same argument to \(F(y_0+z)\). This translation preserves the
frequency subspaces and their projection, so (15) then has
\(3+2|y-y_0|\) in place of \(3+2|y|\). Only the location, not
the length, of the required doubled block has changed. This
translated assertion uses two blocks; the one-block reduction
(10c) uses the original reflection center \(y=0\).

For \(s\) selected variables, use the tensor product of (12).
It reconstructs the original \(s\)-variable canonical polarized
observation from \((2N)^s\) cosine lattice samples, retaining all
mixed normal data. If their uniform error is \(\delta_N\), then
\[
 |\Delta F_{\boldsymbol\sigma}(\mathbf y)|
 \le N^s\delta_N\prod_{v=1}^s(3+2|y_v|)
       \exp\!\left[\pi D\sum_{v=1}^s(-\sigma_v\Im y_v)_+\right].
 \tag{17}
\]
This follows either by multiplying the exact interpolation weights
and summing their absolute values, or by successive operator norms
from (15). It does not assume independent physical contractions.
In charge variables the exponential cost is
\(\pi D\sum_v(\sigma_v\Im\chi_v)_+\).
For the actual tensor cosine source, its separate charge reflection
permits (10c) in every coordinate. Only \(N^s\) samples in
\(\{\chi_v=1-j_v/N:0\le j_v<N\}\) are then required, and (17)
improves to
\[
 |\Delta F_{\boldsymbol\sigma}(\mathbf y)|
 \le N^s\delta_N\prod_{v=1}^s(1+2|y_v|)
       \exp\!\left[\pi D\sum_v(-\sigma_v\Im y_v)_+\right].
 \tag{17a}
\]
This estimate retains every mixed first normal. The first block
in this assertion is the full unit-charge cube, not a fixed small
subinterval of it.

## 3. What the bounds transfer, and what they cost

On a fixed compact target set, suppose the approximate samples
have the actual uniform error
\[
             \delta_N\le C N^p e^{N(M-\gamma)}.
 \tag{18}
\]
Then (17) proves the concrete reconstruction error estimate
\[
 |\Delta F_{\boldsymbol\sigma}(\mathbf y)|
 \le C' N^{p+s}
  \exp N\left[M-\gamma+
                 \pi\sum_v(-\sigma_v\Im y_v)_+\right].
 \tag{19}
\]
Thus comparison with a proposed target action \(S(\mathbf y)\)
has a strict relative error gap whenever
\[
 \gamma>M+\pi\sum_v(-\sigma_v\Im y_v)_+
                              -\Re S(\mathbf y)
 \tag{20}
\]
uniformly on that set. The reconstructed approximate function is
specified by (12); identifying its asymptotic action is a separate
calculation. Formula (19) does not assume that interpolating a
lattice leading term automatically produces \(e^{NS}\).
Nor does it supply the sample error (18).

For an actual heat preimage with real base power \(b_v\), target
power \(n_v\), and target angle \(t_v^*\), substitute
\[
 \chi_{0,v}=1-\frac{(n_v-b_v)t_v^*}{2\pi},\qquad
 y_{0,v}=\frac{(n_v-b_v)t_v^*}{2\pi}
 \tag{21}
\]
into (19). Formula (21) follows also by subtracting the original
primitive equations at powers \(\mathbf b\) and \(\mathbf n\),
at the same angle: \(P_{\mathbf b}=P_{\mathbf n}
+i(\mathbf n-\mathbf b)\mathbf t^*/2\), coordinatewise.
Its explicit directional cost is
\[
 \pi\sum_v(-\sigma_v\Im y_{0,v})_+
       =\pi\sum_v(\sigma_v\Im\chi_{0,v})_+
       =\frac12\sum_v[-\sigma_v(n_v-b_v)\Im t_v^*]_+.
 \tag{22}
\]
For instance a uniform absolute sample error \(e^{-N\gamma}\)
is still exponentially small after this reconstruction if
\(\gamma\) exceeds (22). Any subsequent heat integral retains
its own marked Gaussian and tail estimates; these are not
included in (22). This is a quantitative prerequisite, not
coverage of the preimages by the known small-charge samples.

The exponential factor in (15) cannot be removed from a uniform
reconstruction theorem. Take the actual cosine-space element
\(F(y)=\cos(\pi Dy)\). Its real lattice samples have modulus at
most one, whereas (5) gives
\[
 F_\sigma(y)=e^{\sigma i\pi Dy},\qquad
 |F_\sigma(y)|=e^{\pi D(-\sigma\Im y)}
                      \quad\hbox{if }-\sigma\Im y>0.
 \tag{23}
\]
This is a member of the faithful finite source space, so the
exponential rate in (15) is sharp. It is not an assertion that
this particular boundary class is a prescribed knot numerator.
The polynomial factor in (15) is not claimed optimal.

There is also exponential instability when only a short real
charge interval is supplied. Let \(N\ge4\), \(0<L<1\), and
\(I=[y_c-L/2,y_c+L/2]\). The function
\[
 G_N(y)=e^{\sigma i\pi Dy}
             \bigl(1-e^{-\sigma2\pi i(y-y_c)}\bigr)^{m-1}
 \tag{24}
\]
lies in the span of pure exponentials in (3): its binomial expansion uses
precisely the allowed frequencies \(\sigma\lambda_a\),
\(0\le a<m\). For a real target \(y_*\) with
\[
       |\sin\pi(y_*-y_c)|>\sin(\pi L/2),
 \qquad
       r=\frac{\sin(\pi L/2)}
                    {|\sin\pi(y_*-y_c)|}<1,
 \tag{25}
\]
one has
\[
 \sup_{y\in I}\left|\frac{G_N(y)}{G_N(y_*)}\right|
                         \le r^{m-1},
 \qquad
 \frac{G_N(y_*)}{G_N(y_*)}=1.
 \tag{26}
\]
Indeed \(|1-e^{i\theta}|=2|\sin(\theta/2)|\), and the carrier
has modulus one on the real line. Thus even samples at every
lattice point of \(I\) cannot give a uniform polynomial-cost
extrapolation to \(y_*\) on this exact finite space: the norm of
any exact linear reconstruction is at least \(r^{-(m-1)}\).
The same two-data-set uncertainty applies to reconstruction from
inexact samples. This is an observation-operator estimate, not an
actual-knot cancellation example.

## 4. The finite-space restriction and the height-current distinction

The canonical functions (3) have at most linear growth on the
real \(y\)-axis. Their frequencies are one-sided and their maximal
frequency is \(\pi(N-1)\), strictly below the lattice Nyquist
frequency \(\pi N\). Reconstruction above uses the exact physical
frequency set and its size-two normal blocks, not an unsupported
claim that exponential type alone characterizes those functions.

For comparison, the exact full-midpoint zero-power height current
from the height-transport note is
\[
 J_{\sigma,0,1-y}^{h}[A]
 =\frac{\sigma\eta N^2}{2\pi}A^\sharp(2\cosh h)
       \frac{\sinh h\cosh(Nyh)}{\cosh^2(Nh/2)}
                              \sin(\pi Ny).
 \tag{27}
\]
It vanishes at every sample \(y=j/N\). When \(h>0\) and its
displayed spectator value is nonzero, it is not in (3) or (6):
along real \(y\), the factor \(\cosh(Nyh)\) has exponential
growth on subsequences with \(|\sin(\pi Ny)|=1\).
It also contains the excluded Nyquist sine factor.
Thus (12) does not identify different contour heights off the
lattice. A restriction to the canonical finite charge space
distinguishes this exact current, but does not prove that the
contour-polarized initializer belongs to that space.

The existing local small-charge asymptotic supplies neither the
full unit block in (10c) nor the action-relative error required by
(20). The positive zero-subtree theorem at fixed selected charge
one supplies a different boundary-angle family. None of these
facts is replaced by (12). What is established here is a stable
full-normal finite reconstruction and its explicit continuation
cost, available if the required actual charge samples are controlled.

## Direct sources and coverage

The author read the complete final proof and all three complete direct
sources at the versions below; all used implications were checked.

- [Canonical finite charge polarization](research_polarized_charge_heat_source.md),
  SHA256 860801dedc3f1093d58c0413f580599512bd2566c00f4a94d0ebf99636343db1:
  actual full-normal spaces (3)–(5), faithful observations and source
  placement.
- [Exact polarized height current](research_polarized_height_current_transport.md),
  SHA256 63273441891ce682acf46495e2707a8a72c28d2b74b3d4bed2d6861d568014fb:
  formula (27), its literal polynomial spectator and lattice scope.
- [Entire original-source heat reduction](research_entire_charged_source_heat_reduction.md),
  SHA256 33213425be9cac699860a48b23830399c82cd89bea3140cc776274aafe115fba:
  the original heat-characteristic convention used in (21).

For prior-coverage comparison, the full Fourier–Hermite Gram and
one-sided angular-projection notes were read, and §§12–13 of the
current-free charge equation were read. Their coordinate/period
constructions are credited above; no additional conclusion from
them is needed in this proof. No mathematical computation or
numerical experiment is used.
