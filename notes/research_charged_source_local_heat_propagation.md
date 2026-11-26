# Local propagation of an actual charged source by a signed heat step

Private written analysis, 16 November 2026.

The entire charged-source heat identity gives a local asymptotic
transport theorem with an estimated exterior integral. A sufficiently
small real power step preserves a known nonzero geometric expansion on
a smaller complex charge domain. This uses the whole initial source,
including its physical first normals and its global exponential
growth, rather than an assumed coefficient of a formal saddle.

The domain loss is essential. The output is the characteristic image
of an eroded initial domain. Iteration transports the same initial
set of classical angle labels; it does not supply a fresh complex
neighborhood at every step. No continuation to arbitrary short
fillings or to charge one is claimed.

## 1. Exact source and a global envelope

For \(N\ge2\), use the full algebra and original trace
\[
 \mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2),\qquad
 \phi_N=\eta N^2[z^{N-1}]\operatorname{rem},\qquad
 \eta=(-1)^{N-1}.
 \tag{1}
\]
The entire charged source, canonical real powers and carriers are
those of the exact heat reduction:
\[
 C_{N,b}=\exp\!\left(\frac{\pi i b(N-1)^2}{4N}\right),\qquad
 \widetilde Z_N=\left(\prod_v C_{N,b_v}^{-1}\right)Z_N .
 \tag{2}
\]
At each double physical node \(c=-2\cos\tau\), its charge coupon
has value \(\cos(N(1-\chi)\tau)\) and spectral first derivative
\[
 -\frac{N(1-\chi)\sin(N(1-\chi)\tau)}{2\sin\tau}.
 \tag{3}
\]
The odd simple node has value one. Thus all normal directions are
retained. No free boundary polynomial is reduced.

In one power coordinate the exact evolution is
\[
 \partial_b\widetilde Z_N=-\frac{i}{4\pi N}\partial_\chi^2
                                      \widetilde Z_N .
 \tag{4}
\]
For a nonzero real step \(\delta\), put
\[
 v_\delta=e^{-i\,\operatorname{sgn}(\delta)\pi/4},\qquad
 \mathcal H_\delta f(\chi)=
 \sqrt{\frac N{|\delta|}}\int_{\mathbb R}
              e^{-\pi Nr^2/|\delta|}f(\chi+v_\delta r)\,dr .
 \tag{5}
\]
This equals the actual carrier-removed source at power \(b+\delta\)
when \(f\) is that source at power \(b\). Its line may be translated
by any finite complex amount. The exact identity applies
coefficientwise to ordinary free boundaries and to mixed normal
observations. At zero step \(\mathcal H_0\) is the identity.

For the fixed finite same-index graph sources of the small-charge
theorem, there are constants \(C,p,A\), uniform for powers in a
fixed bounded real box, such that
\[
 |\widetilde Z_N(\mathbf b,\mathbf y;\mathbf u)|
 \le A N^p\prod_v(1+|y_v|)
       \exp N\!\left(C+\pi\sum_v|\Im y_v|\right).
 \tag{6}
\]
Here ordinary free spectral variables range over a fixed compact
set. A fixed number of their derivatives obeys the same kind of
bound. Constants depend on the fixed graph and compact set; (6)
is not a filled-action estimate.

Here is an elementary verification of the finite exponential constant
in (6). Put \(c_a=2\cos((2a+1)\pi/N)\), with the repeated nodes
retained, and write
\[
 S_j=\prod_{r=1}^j2\sin(\pi r/N),\qquad
 e_j(z)=S_j^{-2}\prod_{a<j}(c_a-z).
 \tag{7}
\]
For \(j\le N/2\), the sine chord inequality and
\(j!\ge(j/e)^j\) give
\[
 S_j\ge(4/N)^j j!\ge e^{-N/4}.
 \tag{8}
\]
The last bound follows by minimizing
\(x\log(4x/e)\) for \(0\le x\le1/2\).
For \(j>N/2\), the full sine product and reflection give
\(S_jS_{N-1-j}=N\), hence \(S_j\ge N2^{-N/2}\).
In particular \(S_j\ge e^{-N}\) for every \(0\le j<N\).
On \(|z|\le M_0\), with \(M_0\ge2\), every fixed derivative of
\(e_j\) is bounded by a polynomial in \(N\) times
\[
                    \exp N[\,2+\log(2+M_0)\,].
 \tag{9}
\]
The same conclusion holds for a kernel
\(K_N(z,w)=\sum_{j<N}e_j(z)e_j(w)\), its diagonal restriction
at a loop, and fixed products of kernels.

For bounded real powers the crossing values have modulus one and
their first normals are \(O(N^2)\). Formula (3) contributes at most
a polynomial times
\((1+|\chi|)e^{\pi N|\Im\chi|}\); nonzero physical sines have
polynomial reciprocals. Expanding the finitely many mixed
first-normal terms in the original traces and summing their
polynomially many physical labels proves (6). The odd simple node
requires no derivative and satisfies the same bound. This argument
also retains fixed additional polynomial coupons with comparable
finite exponential bounds. For a more general compiled exterior,
the local theorem below requires its actual bound (6), rather than
assuming one from a geometric phase.

## 2. A quantitative one-coordinate theorem

Let \(D_R=\{z:|z-z_0|<R\}\). Other charge coordinates or ordinary
boundary parameters may range over a fixed compact holomorphic
parameter set; all assumptions and estimates below are uniform
there. Suppose the actual initial functions \(f_N\) are entire in
the charge variable and satisfy
\[
 |f_N(z)|\le A_N(1+|z|)^p
                           e^{N(C+\pi|\Im z|)},\qquad
                \log A_N=o(N),
 \tag{10}
\]
and, on a neighborhood of \(\overline D_R\),
\[
 f_N(z)=N^\alpha e^{NS(z)}
                    \{a_0(z)+O_{\rm hol}(N^{-1})\},\qquad
                  |a_0(z)|\ge a_*>0 .
 \tag{11}
\]
In (11) the error is a uniformly bounded holomorphic function
times \(N^{-1}\). Suppose \(S,a_0\) are holomorphic there. Put
\[
 M=\sup_{\overline D_R}|S'|,\qquad
 L=\sup_{\overline D_R}|S''|,\qquad
 B=\frac{M^2+(M+\pi)^2}{2\pi},
 \tag{12}
\]
\[
 E_{\max}=\sup_{\overline D_R}
            \{C+\pi|\Im z|-\Re S(z)\},\qquad
 E_*=1+\max(0,E_{\max})+B.
 \tag{13}
\]
The positive part makes the estimates valid without a sign convention
for a nonoptimal chosen envelope.

**Theorem 1.** Fix \(0<\rho<R\). If
\[
 0<|\delta|\le
 \min\left\{1,\frac{\pi}{L+1},
                         \frac{\pi\rho^2}{4E_*}\right\},
 \tag{14}
\]
then
\[
 \Phi_\delta(z)=z+\frac{i\delta}{2\pi}S'(z)
 \tag{15}
\]
is injective on \(D_R\). On the output domain
\(\Phi_\delta(D_{R-\rho})\), set
\[
 z=\Phi_\delta^{-1}(\chi),\qquad
 S_\delta(\chi)=S(z)+\frac{i\delta}{4\pi}S'(z)^2 .
 \tag{16}
\]
The actual heat evolution obeys
\[
 \boxed{\quad
 \mathcal H_\delta f_N(\chi)=
 N^\alpha e^{NS_\delta(\chi)}
 \left\{\frac{a_0(z)}
 {\sqrt{\,1+i\delta S''(z)/(2\pi)\,}}
                         +O_{\rm hol}(N^{-1})\right\}.
 \quad}
 \tag{17}
\]
The square root is the holomorphic branch tending to one at
\(\delta=0\). Its argument lies in \(|w-1|\le1/2\).
The leading coefficient is nonzero. Uniformity holds for the
displayed steps, and ordinary derivatives are uniform on smaller
output domains. If (11) has an expansion to every fixed order,
so does (17).

This theorem estimates the discarded part of the actual integral.
It does not assume its relative cycle already has a geometric
coefficient. Applied to (4), the original crossing carrier is restored
by the exact ratio \(C_{N,b+\delta}/C_{N,b}=C_{N,\delta}\).

### Exact contour, local phase and exterior estimate

The bound on \(S''\) and convexity of \(D_R\) give
\[
 |(\Phi_\delta(z)-\Phi_\delta(w))-(z-w)|
                \le\frac{|\delta|L}{2\pi}|z-w|
                \le\frac12|z-w|.
 \tag{18}
\]
Thus (15) is injective with a regular inverse. Write
\(b=z-\chi=-i\delta S'(z)/(2\pi)\). Translate the exact line in
(5) to \(y=z+v_\delta r\). The translated formula is
\[
 \mathcal H_\delta f_N(\chi)=
 e^{i\,\operatorname{sgn}(\delta)\pi/4}
       \sqrt{\frac N{|\delta|}}
 \int_{z+v_\delta\mathbb R}
                    e^{-i\pi N(y-\chi)^2/\delta}f_N(y)\,dy .
 \tag{19}
\]
For fixed \(N,\delta\), the connectors at \(r=\pm R_1\) have a
negative quadratic Gaussian exponent and only linear exponential
growth from (10); they tend to zero as \(R_1\to\infty\).
This proves the equality before any asymptotic estimate.
There are no hidden factorial or physical-grid poles.

The phase on the local segment is
\[
 T(y)=S(y)-\frac{i\pi}{\delta}(y-\chi)^2,\qquad T'(z)=0 .
 \tag{20}
\]
For \(|r|\le\rho\), its whole segment stays in \(D_R\), and
\[
 \Re\{T(z+v_\delta r)-T(z)\}
 \le-\frac{\pi}{|\delta|}r^2+\frac L2r^2
 \le-\frac{\pi}{2|\delta|}r^2 .
 \tag{21}
\]
Also \(T(z)=S_\delta(\chi)\).

For \(|r|\ge\rho\), use the global initial bound (10).
The quadratic kernel, its shifted linear term, and the source type
give the following exponential upper bound, before polynomial
factors:
\[
 C+\pi|\Im z|+\frac{|\delta|M^2}{4\pi}
           +(M+\pi)|r|-\frac{\pi r^2}{|\delta|}.
 \tag{22}
\]
In particular the growth of the source on the Fresnel ray has not
been dropped: \(\pi|\Im(v_\delta r)|\le\pi|r|\).
Young's inequality bounds the linear term by
\[
 (M+\pi)|r|\le
       \frac{\pi r^2}{2|\delta|}
                 +\frac{|\delta|(M+\pi)^2}{2\pi}.
 \tag{23}
\]
Since
\(\left|\Re\{-i\pi b^2/\delta\}\right|
 \le|\delta|M^2/(4\pi)\),
the tail exponent relative to \(\Re S_\delta(\chi)\) is at most
\[
 \boxed{\quad
 E_{\max}+|\delta|B-\frac{\pi r^2}{2|\delta|}.
 \quad}
 \tag{24}
\]
At \(|r|\ge\rho\), (14) makes this less than \(-1\).
Integrating the polynomial factors preserves a strict gap:
for fixed \(\rho>0\), the elementary Gaussian tail inequality
gives a polynomial prefactor, uniformly for \(0<|\delta|\le1\).
For example, write \(|r|=\rho+s\), use
\(r^2\ge\rho^2+2\rho s\), and integrate each fixed polynomial
in \(s\). The factor \(\sqrt{N/|\delta|}\) in (19) is absorbed
by the resulting factors \(|\delta|/N\). The \(A_N=e^{o(N)}\)
factor in (10) is harmless. Hence the exterior is
\[
        N^\alpha e^{N\Re S_\delta(\chi)}O(e^{-N/2}),
 \tag{25}
\]
after enlarging the threshold in \(N\). The constants can depend
on \(\rho\) and the fixed parameter set, but not on the sign
of \(\delta\).

On the local segment insert (11), use (21), and rescale
\(r=\sqrt{|\delta|/N}\,u\). The oriented factors in (19) satisfy
\(e^{i\,\operatorname{sgn}(\delta)\pi/4}v_\delta=1\).
The Gaussian multiplier is exactly
\[
 \left(1-\frac{|\delta|v_\delta^2}{2\pi}S''(z)\right)^{-1/2}
       =\left(1+\frac{i\delta}{2\pi}S''(z)\right)^{-1/2}.
 \tag{26}
\]
On the inner segment \(|r|\le\rho/2\), Cauchy's estimates on the
reserved \(\rho\)-discs bound the required derivatives uniformly.
The remaining local annulus has the strict quadratic gap (21).
The odd Taylor terms integrate to zero on the symmetric inner
segment; the remaining Taylor errors have relative order \(N^{-1}\),
uniformly for the steps in (14). Analyticity on a neighborhood
of the closed initial disc supplies all needed bounded derivatives.
The holomorphic initial remainder contributes the same error order.
Further Taylor terms give the all-order assertion. Cauchy's formula
on smaller output domains gives the derivative statement. This
proves Theorem 1.

For several charge coordinates, apply the theorem successively in
the changed coordinates, treating the others as compact holomorphic
parameters. Every step is the exact original source, and every
discarded tail has its own bound (24). This covers mixed signs and
unchanged zero-step coordinates. It is not an instruction to replace
the full source by a product of scalar observations.

## 3. The small-charge initializer has a complex neighborhood

The frozen small-charge source theorem is stated on the physical
charge lattice in the compact real box
\[
             [1/4000,1/2000]^I .
 \tag{27}
\]
For its specified fixed graph, fixed signed powers and complete
outside angles, its proof also gives a uniform holomorphic
initializer for the entire coupon family (3) on a sufficiently
small fixed complex neighborhood of (27).

This assertion does not follow merely from agreement on increasingly
fine lattices. The exact even-coupon trace identity continues to
complex \(\chi\) by the full physical jets, as proved in the
dominant-saddle source note, Section 9. In the small-charge proof
retain its physical-row decomposition and its actual mixed
horizontal/vertical contours. At a fixed real charge in (27),
all noncentral terms have uniform strict gaps, and every retained
angular contour is bounded. Moving the charges by at most
\(\varepsilon\) changes each coupon exponential bound by at most
\(e^{C_1N\varepsilon}\), with a fixed constant for this finite graph.
The required normal derivatives cost polynomial factors.
The same bound applies to removed physical rows; their angles
lie in \([-\pi,\pi]\). Explicitly,
\[
 |\cos(N(1-\chi)\tau)|\le e^{\pi N|\Im\chi|},
 \qquad
 |\partial_\tau\cos(N(1-\chi)\tau)|
 \le N|1-\chi|e^{\pi N|\Im\chi|}.
\]
The first spectral normals add only the already retained
polynomial reciprocal of \(\sin\tau\); the odd simple node
remains a value term.

Choose \(\varepsilon>0\) below the finitely many gap margins divided
by the resulting constants. The mixed-current and removed-row
gaps then remain strict relative to the continued selected action.
The central saddle moves holomorphically and stays in the same
pole-free thin rectangle. A small contour displacement through
it is legitimate there, with the connecting faces still in the
strict-gap region. The nonzero sine factors, edge amplitudes and
Gaussian determinant remain nonzero after one further shrinkage.
The exact companion and alias estimates also persist because the
real box is separated from both charge endpoints and its heights
are uniformly positive.

Compactness of (27) supplies one fixed complex neighborhood.
The original proof's Taylor expansion on these contours gives
uniform holomorphic errors to every fixed order there, through
both level parities. Thus this is an actual initializer for
Theorem 1. Its radius may depend on the fixed graph and powers.
No lower bound independent of that data or extension to charge
one is asserted.

The same local conclusion holds uniformly on a fixed bounded
real-power box after using the canonical real powers. The physical
values and normals have the uniform bounds used in (6); the
small-charge fixed-point denominators obey
\(|n_v+iC_v|\ge\sqrt{n_v^2+d_v^2}-d_v/30000\)
for real \(n_v\) as well. The signed vertical-side estimates use
only \(n_v\operatorname{sgn}(n_v)=|n_v|\), not integrality.
One may retain either side at zero power. The full real-power trace
identity keeps its endpoint currents. These observations give the
same compactness argument without assigning noninteger powers
an additional topological meaning.

## 4. Domain accounting under iteration

The local theorem is an effective propagation result, but it has
two explicit restrictions.

First, suppose a regular phase has initial derivative
\(t_0(\zeta)=iS_0'(\zeta)\). The classical heat characteristic is
\[
            \chi_s=\Phi_s(\zeta)
                   =\zeta+\frac{s}{2\pi}t_0(\zeta).
 \tag{28}
\]
Indeed differentiating (16) gives
\(S_{\delta,\chi}(\Phi_\delta(\zeta))=S'(\zeta)\).
Thus the angle is constant along the characteristic. The maps
for successive steps compose to (28) with the total power change.
In several coordinates the corresponding formula is
\[
 \boldsymbol\chi_{\mathbf n}
   =\boldsymbol\zeta+
        \frac1{2\pi}\operatorname{diag}(\mathbf n-\mathbf b)
                                      \mathbf t_0(\boldsymbol\zeta).
 \tag{29}
\]
The coordinate flows commute wherever these charts are regular.

Each use of Theorem 1 requires the input saddle to lie inside
the previously certified complex domain with a reserved margin.
Consequently this procedure transports a subset of the initial
angle labels. Recentring overlapping output discs does not add
initial labels that were not already certified. This statement
concerns the present local procedure, not an impossibility theorem
for analytic continuation by other source estimates.

Second, the explicit envelope recipe (14) spends a quadratic
time budget. For a one-coordinate nested-disc certificate, suppose
the characteristic charts extend injectively to neighborhoods of
the closed initial-label discs and their inverses have a common
Lipschitz bound \(K\ge1\). If these discs have radii
\(R_j\), reserve a charge margin
\(\rho_j=(R_j-R_{j+1})/K\). It lies inside the preceding charge
image: the inverse Lipschitz bound gives that lower bound on the
distance to its boundary. With a common chosen
\(E_*\), the sufficient steps in (14) obey
\[
 \sum_j|\delta_j|
 \le\frac{\pi}{4E_*}\sum_j\rho_j^2
 \le\frac{\pi}{4E_*K^2}(R_0-R_{\rm final})^2 .
 \tag{30}
\]
This is the limitation of that stated conservative certificate,
not a necessary inequality for the actual source or for all
possible contour estimates. Subdivision into more steps does not
increase its guaranteed total time. If one has sharper exterior
information than (10), a better domain estimate may be possible.
Neither positivity of a local Hessian nor a fixed global envelope
alone supplies that sharper information.

For a fixed unit-charge positive point
\(t^*=s-iH\), \(H>0\), the initial charge at any real base power
\(b\) is
\[
                  y_b=1-\frac{(n-b)t^*}{2\pi}.
 \tag{31}
\]
Successive real-power steps give the same initial label (31).
It is real only if \(b=n\), in which case it is one.
For a real initializer interval \([\alpha,\beta]\), \(\beta<1\),
orthogonal projection onto this line gives exactly
\[
 \inf_{\substack{b\in\mathbb R\\x\in[\alpha,\beta]}}|y_b-x|
                      =(1-\beta)\frac{H}{|t^*|}>0 .
 \tag{32}
\]
The complex neighborhood of Section 3 must actually contain
the required label; its existence alone does not establish this.
Formula (32) does not rule out containment in a sufficiently large
proved neighborhood, nor does it rule out a different continuation.

The new conclusion is therefore local and quantitative: a known
actual complex initializer admits a nonzero signed heat step with
an explicitly bounded whole-source exterior. Establishing enough
initial-label coverage or replenishing the complex domain to reach
every arbitrary short partial filling remains a separate problem.

## Direct sources and author readback

- [Exact entire charged-source heat reduction](research_entire_charged_source_heat_reduction.md):
  faithful charge space, all physical normals, exact Gaussian
  identity and finite translated contours. SHA256
  33213425be9cac699860a48b23830399c82cd89bea3140cc776274aafe115fba.
- [Actual small-charge initializer](research_small_charge_path_source.md):
  complete original graph source, strict alias/current/removed-row
  estimates, nonzero local amplitude and all-order expansion.
  SHA256
  c6d0ce2a4ecf1412aa3752cb8a94c6933bb47acab5d96d879c6f1b17b2db2a90.
- [Canonical real-power source](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_real_power_source_transport.md):
  real physical value/normal bounds, full trace and endpoint
  currents for noninteger powers. SHA256
  7dac43d1a5fac6b4602a3aab12bfe977cb42a61b36d40a2fb8517e29566df8ea.
- [Entire coupons and continuation scope](research_dominant_saddle_transport.md):
  Section 9, exact complex coupon trace family and its original
  current scope. SHA256
  413940497a23e884d726b91f9c0ebc01994fef8216811ed2c6fb0838fc80bb04.

Only written mathematics and text/hash inspection are used. No
mathematical code, numerical computation, tests or compilation
were run. The author read the entire final proof. The small-charge
source was read in full in this sequence; matching complete reads
of the other three sources were retained, their used implications
reread, and all four pinned versions verified. Independent peer
and root review are required before adoption.
