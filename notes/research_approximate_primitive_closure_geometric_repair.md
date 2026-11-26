# Repair of approximate primitive closure in the actual peripheral chart

Research note, 18 November 2026.

A small error in the full primitive filling word determines nonzero
centered integer charges and can be corrected to an exact filled
representation. The correction is uniform over independently long
slopes. It also bounds the classical eigenframes on the filled cusps.
The input is an actual representation in the positive gluing chart;
arbitrary approximate source configurations are not assumed to be
representations.

## 1. Complete directs and fixed chart

The complete proof directs are:

* **R**, [The regular peripheral factor for a primitive filling](
  research_regular_primitive_filling_factor.md).
* **G**, [A quantitative volume gap for actual long-filled groups](
  research_long_filled_group_representation_volume_gap.md).
* **F**, [A finite positive certificate supplies every sufficiently
  long filling branch](
  finite_geometric_certificate_uniform_filling_existence.md).

Fix their marked hyperbolic core, positive complete certificate and
actual peripheral bases, and a nonempty subset \(I\) of selected cusps.
All selected-cusp indices below lie in \(I\).
The holomorphic positive gluing family
\(\rho(U)\) consists of actual representations. On each selected cusp,
in its fixed bounded affine frame,
\[
 \mu_i(w)=e^{U_i}w+B_i(U),\qquad
 \lambda_i(w)=e^{V_i(U)}w+D_i(U),\qquad
 V_i=U_i\tau_i(U).
 \tag{1}
\]
Choose a fixed closed polydisk with a larger holomorphic buffer on which
\[
 |B_i|\ge B_0>0,\quad
 \Im\tau_i\ge m>0,\quad |\tau_i|\le T,\quad
 \sum_j|\partial_j\tau_i|\le L.
 \tag{2}
\]
All unfilled coordinates are fixed to zero. Thus their peripheral
groups remain the actual complete parabolic groups in this chart.
We shall restrict the input to a smaller concentric polydisk.
Every constant below depends on these fixed choices, not on the slopes.

For primitive selected slopes \((a_i,b_i)\), put
\[
 \ell_i=(a_i^2+b_i^2)^{1/2},\quad
 d_i(U)=a_i+b_i\tau_i(U),\quad
 s_i=U_i d_i(U).
 \tag{3}
\]
As in F, \(|d_i|\ge c_0\ell_i\) with
\(c_0=m/\sqrt{1+T^2}\), while
\(|d_i|\le C_0\ell_i\), \(C_0=\sqrt{1+T^2}\).
Write the full primitive word as
\[
 \mu_i^{a_i}\lambda_i^{b_i}(w)
       =e^{s_i}w+B_i t_i,\qquad
 e^{s_i}-1=(e^{U_i}-1)t_i.
 \tag{4}
\]
These are R's whole-word identities, including negative powers and
the removable value at \(U_i=0\).
Measure its translation residual by
\[
                         \varepsilon=\max_i|B_i t_i|.
 \tag{5}
\]
In this fixed bounded frame, small translation residual also bounds the
multiplier residual by (4). No unbounded conjugation is allowed in (5).

## 2. Integer charges without a zero-charge ambiguity

There are a fixed input polydisk and \(\varepsilon_0>0\) such that
every input with \(\varepsilon\le\varepsilon_0\) has unique integers
\(q_i\) and errors \(\omega_i\) satisfying
\[
 s_i=2\pi i q_i+\omega_i,\qquad
 |\omega_i|\le C\varepsilon|U_i|,\qquad q_i\ne0 .
 \tag{6}
\]
These are centered geometric charges, not labels of a Fourier sum.

Indeed the divided exponential \(\psi(U)=(e^U-1)/U\) is bounded on
the fixed chart. Equation (4) gives
\[
 |e^{s_i}-1|
 \le B_0^{-1}\sup|\psi(U_i)|\,\varepsilon|U_i|.
 \tag{7}
\]
Choose \(\varepsilon_0\) so the right side is less than \(1/2\).
The principal logarithm on \(|z-1|<1/2\) defines
\(\omega_i=\log(e^{s_i})\), with the bound in (6), since
\(|\log(1+x)|\le2|x|\) there. The kernel of the complex exponential
then gives the unique integer \(q_i\).

If \(q_i=0\) and \(U_i\ne0\), (3) and (6) imply
\[
                  c_0\ell_i\le|d_i|\le C\varepsilon,
 \tag{8}
\]
which is impossible for a fixed sufficiently small
\(\varepsilon_0\), since every primitive slope has \(\ell_i\ge1\).
If \(U_i=0\), R's regular factor instead gives
\[
       |B_i t_i|=|B_i(a_i+b_i\tau_i)|\ge B_0c_0\ell_i,
 \tag{9}
\]
again impossible. This proves (6) without dividing a zero by a zero.

Also,
\[
 \frac{|q_i|}{\ell_i}
       \le \frac{C_0+C\varepsilon_0}{2\pi}|U_i|.
 \tag{10}
\]
Shrinking the input polydisk makes these charges lie in a fixed box
\(|q_i|\le\rho_*\ell_i\), where \(\rho_*>0\) is as small as needed
for the following correction.

## 3. Correction to an actual filled representation

Define on the larger fixed polydisk
\[
       \mathcal T_{q,i}(Z)=\frac{2\pi iq_i}
                                    {a_i+b_i\tau_i(Z)}.
 \tag{11}
\]
The estimates
\[
 \|\mathcal T_q\|_\infty\le2\pi\rho_*/c_0,\qquad
 \|D\mathcal T_q\|\le2\pi L\rho_*/c_0^2
 \tag{12}
\]
follow directly from (2)--(3).
Choose \(\rho_*\) so the image lies in the interior half-polydisk
and the derivative bound is at most \(1/2\).
Iteration gives the unique fixed point \(U(q)\) there.

The residual of the input under this contraction is exactly
\[
       U_i-\mathcal T_{q,i}(U)=\frac{\omega_i}{d_i(U)}.
 \tag{13}
\]
Consequently
\[
 \boxed{\quad
 \|U-U(q)\|_\infty
       \le C\varepsilon\max_i\frac{|U_i|}{\ell_i}
       \le \frac{C\varepsilon}{\ell_{\min}} .
 \quad}
 \tag{14}
\]
For the first inequality, use
\(\|U-U(q)\|\le\|U-\mathcal T_q(U)\|+\frac12\|U-U(q)\|\).
The second merely absorbs the fixed input radius.
All selected charges are nonzero by (6). R's exact equivalence between
the regular word factor and \(s_i=2\pi iq_i\ne0\) therefore shows
that \(\rho(U(q))\) satisfies every primitive slope relation as a
projective matrix. It is an actual representation of the filled group.
Unfilled peripheral groups remain complete.

The actual normalized matrix of every fixed group word is holomorphic
on the chart. Its difference between \(U\) and \(U(q)\) is thus bounded
by a constant times (14). This is a correction in a fixed regular
representation frame, not an estimate for an arbitrary source frame.

## 4. Quantitative frame control on the filled cusps

The same argument excludes collapsed eigenvalue separation at any
selected filled cusp. From (3) and (6), with \(|q_i|\ge1\),
\[
 2\pi\le |s_i|+|\omega_i|
       \le(C_0\ell_i+C\varepsilon_0)|U_i|.
 \tag{15}
\]
Since \(\psi(U_i)\) is a unit on the chart, this implies
\[
             |U_i|\ge c/\ell_i,\qquad
             |e^{U_i}-1|\ge c/\ell_i .
 \tag{16}
\]
Choose a regular local determinant-one lift of the actual meridian
matrix, and retain its central sign. Its selected eigenvalue is
\(M_i=\pm e^{U_i/2}\). The fundamental eigenprojector is
\[
       E_i=\frac{\rho(\mu_i)-M_i^{-1}I}{M_i-M_i^{-1}}.
 \tag{17}
\]
All numerator entries are bounded in the fixed regular frame, while
\(|M_i-M_i^{-1}|\ge c/\ell_i\) by (16). Hence
\[
       \|E_i\|\le C\ell_i,\qquad
       \|\partial_U^\alpha E_i\|
                        \le C_\alpha\ell_i^{|\alpha|+1}.
 \tag{18}
\]
The derivative estimate is obtained by differentiating (17): numerator
derivatives are bounded on the fixed buffer, and each differentiated
reciprocal contributes at most one additional inverse eigenvalue gap.
It is a fixed-order classical jet estimate.

There is a corresponding finite classical frame cover. For each of the
two eigenlines, choose a nonzero coordinate of largest modulus and
normalize it to one. The remaining coordinate then has modulus at most
one; allowing a factor two makes open charts. There are four choices
for an ordered pair of lines. If \(S_i\) has these vectors as columns,
the projector norm is the inverse sine of their angle. Thus (18) gives
\[
                       \|S_i\|\le C,\qquad
                       \|S_i^{-1}\|\le C\ell_i .
 \tag{19}
\]
These are holomorphic frame charts with their actual overlap maps.
Conjugating any fixed bounded holonomy word by such a frame has norm
at most \(C\ell_i\).

No statement here identifies that classical conjugation with a quantum
\(\mathrm{SL}_2\) action. An ordinary finite-dimensional change of basis
would still have to conjugate every crossing and pivot and retain the
transformed cut insertion. Moreover (16)--(19) concern the selected
filled cusps. They do not separate the eigenvalues at an unfilled
complete physical highest-cut meridian.

## 5. High-volume approximate closure corrects to geometric holonomy

On the fixed convex chart the exact volume differential F(10),
\[
 d\operatorname{Vol}
 =\frac12\sum_i
    [\Re V_i\,d\Im U_i-\Re U_i\,d\Im V_i],
 \tag{20}
\]
has bounded coefficients, by (1)--(2) and the holomorphic buffer.
Integration along the segment from \(U\) to \(U(q)\), which remains
in the chart, proves
\[
 \left|\operatorname{Vol}(\rho(U))-
               \operatorname{Vol}(\rho(U(q)))\right|
                         \le C_V\varepsilon/\ell_{\min}.
 \tag{21}
\]

Take independently long slopes as in G, and let
\[
 g_\sigma=\min\{\delta/2,\,3c_1/\ell_{\max}^2\}
 \tag{22}
\]
be its gap for every other admitted filled-group representation.
If
\[
 \varepsilon\le
       \min\{\varepsilon_0,\,
                     g_\sigma\ell_{\min}/(4C_V)\},
 \qquad
 \operatorname{Vol}(\rho(U))
             >\operatorname{Vol}(M(\sigma))-g_\sigma/2,
 \tag{23}
\]
then the corrected representation is conjugate to the oriented geometric
holonomy of \(M(\sigma)\). Otherwise G and (21) would give
\[
 \operatorname{Vol}(\rho(U))
 \le \operatorname{Vol}(M(\sigma))
                         -g_\sigma+g_\sigma/4,
 \tag{24}
\]
contradicting (23). Estimate (14) consequently places the input within
the stated quantitative distance of a decorated geometric
representative. The volume in (21) is the normalized core volume;
for the exact correction it equals the filled volume by G.

## 6. Source boundary scope

This gives an explicit exclusion and correction for approximate
primitive closure on the actual positive representation chart.
It does not assume that small scalar eigenvalue residuals imply
small translations: the whole word residual (5) is retained.

To use it for a source current, that current must first be mapped to
this actual representation chart with a bound on its full word residual.
An escaping highest-cut configuration need not satisfy those
requirements even when its character converges. The classical frame
cover (19) retains the filled peripheral data but is not a finite atlas
for the full quantum source, its unfilled parabolic cut, or its
relative boundary currents. No such current is discarded, and no
physical-cycle coefficient or scalar lower bound is inferred.

## Frozen proof-source pins

* R: research_regular_primitive_filling_factor.md,
  SHA256 ac4a336eac370bb45aec59b7a95de9e2884448d861a10b3f021f5d45d2bf76c4.
* G: research_long_filled_group_representation_volume_gap.md,
  SHA256 977d61c32e9610dc5e3bd1750b50614c88473f28683ca5dcea5f23a8a88becc0.
* F: finite_geometric_certificate_uniform_filling_existence.md,
  SHA256 f3f78212e1f42f501593412a71c21590f24f8838f4add8abeb2f12534ad2b39b.
