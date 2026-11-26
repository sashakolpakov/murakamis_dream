# A relative edge-sector estimate and the network source at radius thirty-two

22 November 2026. Written research proof. Earlier final notes and public
manuscripts remain unchanged.

The original same-index graph source has its nonzero geometric expansion
when every selected vertex satisfies \(n_v^2+d_v^2\ge1024\). The previous
general network theorem required \(4096\). The improvement uses a relative
bound for the imaginary part of the exact edge Hessian, rather than a
separate absolute bound followed by Young's inequality. All original
physical rows, mixed currents, first normals and level parities remain.
This does not cover arbitrary fixed short fillings or prove finite exceptions.

## 1. The exact source and statement

Use the complete source, Newton normalization and edge amplitudes of
[N]. Let \(\Gamma=(V,E)\) be a fixed finite undirected graph, allowing
loops and repeated edges, and let \(I\ne\varnothing\) be its selected
vertices. Every selected vertex is incident to an edge. Its actual
incidence degree is \(d_v\), with a loop counted twice, and its original
signed integer crossing power is \(n_v\). Put
\[
 R_v=\sqrt{n_v^2+d_v^2},\qquad m=|I|,\qquad e=|E|,
 \qquad w_v=-2\cos t_v .
\]
Unselected angles are initially zero. The full original source is
\[
 Z_{\Gamma,I,N}
 =\left(\prod_{v\in I}\phi_N^{(w_v)}\right)
   \left[\prod_{v\in I}R(w_v)^{n_v}
          \prod_{\{v,w\}\in E}K_N(t_v,t_w)\right],
 \qquad
 K_N(t,u)=\sum_{j=0}^{N-1}e_j(-2\cos t)e_j(-2\cos u).
 \tag{1}
\]
Each product is formed before its full Hermite trace. A loop contributes
its kernel once. No incidence or edge is duplicated.

For real charges \(\boldsymbol\chi\in[0,1]^I\), used only to compare
stationary actions, set
\[
 \Phi_{\boldsymbol\chi}(\mathbf t)
 =\sum_{\{v,w\}\in E}\psi(t_v,t_w)
   +\sum_{v\in I}\left(\frac{in_vt_v^2}{4\pi}-i\chi_vt_v\right),
 \quad
 \psi(0,0)=\frac{4G_{\rm Cat}}{\pi},\quad
 \psi_t=-\frac1\pi\operatorname{arsinh}
                   \{\tan(t/2)\cos(u/2)\}.
 \tag{2}
\]
All branches continue from completeness.

**Theorem 1.** Suppose \(R_v\ge32\) for every selected vertex.
The entire charge cube has a unique critical point in
\(|t_v|\le1/5\), holomorphic locally in all charges and continuing
from zero. Its original edge shapes are positive. At unit charge put
\(t^*=\mathbf t(\mathbf1)\), \(\Phi=\Phi_{\mathbf1}\),
\(M=\Re\Phi(t^*)\), and \(\mathcal H=-\Phi''(t^*)\).
Through all sufficiently large integer levels,
\[
 Z_{\Gamma,I,N}
 =\varepsilon_N N^{3(m-e)/2}\mathcal A
                 e^{N\Phi(t^*)}(1+O(N^{-1})),
 \qquad
 \varepsilon_N=\prod_{v\in I}
       \exp\!\left(\frac{\pi i n_v(N-1)^2}{4N}\right),
 \tag{3}
\]
\[
 \mathcal A=
 \left(\frac{i}{\pi}\right)^m(2\pi)^{m/2}
 \frac{\prod_{v\in I}\sin t_v^*
             \prod_{\{v,w\}\in E}a_e(t_v^*,t_w^*)}
      {\sqrt{\det\mathcal H}}\ne0 .
 \tag{4}
\]
The square root is the branch on matrices with positive definite
real part. The expansion has every fixed inverse-power order.
It holds on a fixed small complex neighborhood of all complete
outside colors, with all fixed ordinary spectral derivatives.
Constants may depend on the fixed graph and its powers.

## 2. The relative sector of the original edge Hessian

The exact formula from [N, (14)] is
\[
 K=-2\pi\psi''(t,u)
   =s^{-1}\begin{pmatrix}1+w^2&-wz\\-wz&1+z^2\end{pmatrix},
 \qquad w=\tan(t/2),\quad z=\tan(u/2),\quad
 s^2=1+w^2+z^2,\quad \Re s>0 .
 \tag{5}
\]
Write \(K=H+iJ\), with real symmetric \(H,J\), and
\[
 X=\Re(w,-z),\quad Y=\Im(w,-z),\quad
 x=\|X\|^2,\quad y=\|Y\|^2,\quad c=X\cdot Y,\quad
 p=(\Re s)^2,\quad d_0=|s|^2=p+c^2/p .
\]

**Lemma 2.** If \(y<1\), then \(H>0\), and
\[
 \det H\ge1-y,\qquad
 \big\|H^{-1/2}JH^{-1/2}\big\|^2
     =\frac1{\det H}-1\le\frac{y}{1-y}.
 \tag{6}
\]

**Proof.** The real part of \(s^2\) is \(1+x-y>0\), so its
principal root has positive real part and \(p\ge1+x-y\).
Writing \(s=\alpha+i\beta\), direct expansion of (5) gives
\[
 H=\frac{\alpha}{d_0}(I+XX^T-YY^T)
       +\frac{\beta}{d_0}(XY^T+YX^T),\quad
 \operatorname{tr}H=\sqrt p(1+d_0^{-1}),\quad
 \det H=\frac{p-xy+c^2}{d_0}.
 \tag{7}
\]
Consequently
\[
 \det H-(1-y)
 =\frac{y(p-x)+c^2(p-1+y)/p}{d_0}\ge0 .
 \tag{8}
\]
Both terms are nonnegative, since \(p-x\ge1-y>0\) and
\(p-1+y\ge x\). The trace in (7) is positive, proving \(H>0\).
The matrix determinant lemma applied to (5) gives \(\det K=1\).
For the real symmetric matrix \(S=H^{-1/2}JH^{-1/2}\),
\[
 1=\det H\,\det(I+iS)
   =\det H\{1+i\operatorname{tr}S-\det S\}.
\]
Thus \(\operatorname{tr}S=0\); its eigenvalues are \(\kappa,-\kappa\).
The real identity is \(\det H(1+\kappa^2)=1\), proving (6).
\(\square\)

On the wide rectangle
\[
 |\Re t|,|\Re u|\le\pi/2,\qquad
 |\Im t|,|\Im u|\le1/5,
 \tag{9}
\]
one has \(|w|,|z|\le1\) and
\(|\Im w|,|\Im z|\le\tanh(1/5)<1/5\). Hence \(x\le2\),
\(y<2/25\), and \(\det H>23/25\). Moreover
\[
 \operatorname{tr}H
 \le\sqrt{1+x}\left(1+\frac1{1+x-y}\right)<\frac73 .
 \tag{10}
\]
For the last bound, fix \(y\le2/25\). The displayed function of
\(1+x\in[1,3]\) has no interior maximum, so its maximum is at
an endpoint. The endpoint bounds are \(48/23<7/3\) and
\(98\sqrt3/73<7/3\), the latter using \(\sqrt3<26/15\).
The characteristic polynomial at \(1/2\) is greater than \(1/300\),
and at \(2\) greater than \(19/75\); its trace excludes both roots
on the wrong side. Therefore
\[
 \frac12I<H<2I,\qquad
 |a^TJb|\le\frac3{10}
          \sqrt{(a^THa)(b^THb)}
 \tag{11}
\]
for real vectors \(a,b\). This relative inequality also survives
positive averaging and summing embedded edge incidences, by
Cauchy--Schwarz. A loop uses its literal two-coordinate pullback.

## 3. The whole charge cube and its action cost

Let \(f(t,u)=2\operatorname{arsinh}\{\tan(t/2)\cos(u/2)\}/t-1\),
with its removable value at \(t=0\). On \(|t|,|u|\le2/5\),
\[
 |\tan(t/2)-t/2|\le|t|^3/16,\quad
 |\tan(t/2)|\le(51/100)|t|,\quad
 |\cos(u/2)-1|\le|u|^2/7,\quad |\cos(u/2)|\le41/40 .
 \tag{12}
\]
Indeed \(|\tan z|\le(21/20)|z|\) on \(|z|\le1/5\) follows
from \(\sinh|z|/(2-\cosh|z|)\): the positive series give
\(\sinh(1/5)/(1/5)<101/100\) and \(\cosh(1/5)<41/40\),
whose quotient bound is \(202/195<21/20\). Integrating \(\tan^2z\)
gives the first estimate, which then improves the linear bound.
The cosine estimates follow from its absolute cosh series.
The asinh argument has magnitude at most \(2091/10000<21/100\).
Integrating its binomial derivative gives
\(|\operatorname{arsinh}\xi-\xi|\le|\xi|^3/5\) there. Thus
\[
 |f(t,u)|\le
 \left[\frac18+\frac25\left(\frac{51}{100}\frac{41}{40}\right)^3\right]|t|^2
        +\frac{51}{350}|u|^2
 <\frac13\max(|t|,|u|)^2 .
 \tag{13}
\]

On \(|t_v|\le r=1/5\) put
\(C_v=\sum_{w\sim v}(1+f(t_v,t_w))\), one term per incidence.
Cauchy's estimate from the doubled disk gives
\[
 |C_v-d_v|\le d_v/75,\qquad
 \sum_w|\partial_{t_w}C_v|\le(8/15)d_v.
 \tag{14}
\]
The original stationary equations are exactly
\[
 t_v=\mathcal T_v(\mathbf t)
       =\frac{2\pi\chi_v}{n_v+iC_v}.
\]
Since \(d_v\le R_v\) and \(R_v\ge32\),
\[
 |\mathcal T_v|\le\frac{75\pi}{1184}\chi_v<\chi_v/5,\qquad
 \|D\mathcal T\|_\infty
 \le\frac{\pi}{30}\left(\frac{75}{74}\right)^2<\frac18 .
 \tag{15}
\]
This proves the asserted unique small branch and its holomorphic
dependence. If \(C_v=A_v+iB_v\), then \(A_v\ge74d_v/75>0\) and
\[
 h_v:=-\Im t_v
 =\frac{2\pi\chi_v A_v}{(n_v-B_v)^2+A_v^2},
 \qquad
 0<h_v\le\frac{2850\pi}{1369}
                 \frac{\chi_vd_v}{R_v^2}
       <7\frac{\chi_vd_v}{R_v^2}\quad(\chi_v>0).
 \tag{16}
\]
At zero charge \(t_v=0\). For \(\boldsymbol\chi^S\) obtained by
setting charges on \(S\) to zero, the exact stationary derivative
\(\partial_{\chi_v}\Re\Phi_{\boldsymbol\chi}=\Im t_v=-h_v\) yields
\[
 0\le M(\boldsymbol\chi^S)-M(\boldsymbol\chi)
 \le\frac72\sum_{v\in S}\frac{d_v\chi_v^2}{R_v^2}
 \le\frac7{2048}\sum_{v\in S}d_v.
 \tag{17}
\]

For positivity, every critical tangent has modulus less than
\(51/500\). The principal square root in (5) has real part
greater than \(9/10\), whereas the norm of its two real tangent
parts is less than \(1/5\). The exact shape criterion of [P]
therefore makes every original edge positive. Charge continuation
from zero fixes the full original logarithmic lift.

## 4. Every retained mixed current

Take the largest physical trace midpoint \(T_N\le\pi/2\); for
large \(N\), \(T_N\ge3/2\). Use the exact full-Hermite rectangles
of [N], at the actual depths \(h_v<1/5\). For a vertical coordinate
use side \(\operatorname{sgn}(n_v)T_N\), or \(+T_N\) when \(n_v=0\),
with its original side-reflection orientation.

For a nonempty vertical set \(S\), write \(t-t^*=a+ib\).
Then \(b_v=0\) outside \(S\), and on \(S\)
\[
 |a_v|>13/10,\qquad 0\le b_v<2/5,\qquad n_va_vb_v\ge0 .
 \tag{18}
\]
The segment from \(t^*\) to \(t\) lies in (9). Average the
embedded matrices \(H,J\) on this segment with weight
\(2(1-\theta)\), and denote the resulting graph matrices by
\(\bar H,\bar J\). Put \(U=a^T\bar Ha\), \(V=b^T\bar Hb\).
Equation (11), including its incidence-sum version, gives
\[
 U\ge\tfrac12\sum_vd_va_v^2,\quad
 V\le2\sum_vd_vb_v^2,\quad
 |a^T\bar Jb|\le\tfrac3{10}\sqrt{UV},\quad
 \frac VU\le\frac{64}{169}.
 \tag{19}
\]
The actual vertical trace penalty is \(-|\Im t_v|\), so its
exponential modulus \(\mathcal E_S\) is at most \(\Re\Phi(t)\).
Taylor's formula, with the crossing chirp retained exactly, now gives
\[
 \begin{split}
 \mathcal E_S-M
 &\le-\frac{U-V-2a^T\bar Jb}{4\pi}
           -\frac1{2\pi}\sum_vn_va_vb_v\\
 &\le-\frac1{4\pi}\frac{213}{845}U
 \le-\frac{213}{4000\pi}\sum_{v\in S}d_v
 <-\frac1{60}\sum_{v\in S}d_v .
 \end{split}
 \tag{20}
\]
Here \(1-64/169-(3/5)(8/13)=213/845\).
This is a bound on each actual mixed current, not a deletion
or replacement of that current.

## 5. Removed rows and the full original coefficient

We use exactly the two source estimates retained in [N, Sections
4--6 and 8]: the full kernel expansion on
\(|\Re t|,|\Re u|\le\pi/2\), heights at most \(3/10\), and
the centered loss \(21/200\) per removed incidence on that same
box, including two removed endpoints and every fixed ordinary normal.
The new contours have heights at most \(1/5\), strictly inside it.

Partition the exact derivative samples by their nonempty set \(S\)
of removed vertices. Keep their actual crossing values and first
normals, and deform only the retained traces at
\(\mathbf t(\boldsymbol\chi^S)\). Degrees still count all original
incidences, including those to newly complete vertices.
Equations (17) and the centered estimate give
\[
 \operatorname{rate}(S)
 \le M-\left(\frac{21}{200}-\frac7{2048}\right)
                   \sum_{v\in S}d_v
 <M-\frac1{10}\sum_{v\in S}d_v .
 \tag{21}
\]
Loops count twice in this loss; no edge is counted twice as a kernel.
Actual crossing values have modulus one on physical nodes, and
their fixed-power first normals have polynomial cost.

On the all-horizontal contour (11) gives
\[
 \Re[-\Phi''(t)]>\frac1{4\pi}\operatorname{diag}(d_v)>0 .
 \tag{22}
\]
Thus \(t^*\) is its unique maximum, with a strict gap on every
fixed complement. The wide-kernel theorem supplies the actual
nonzero \(a_e\). The exact horizontal trace factor is
\[
 \frac{iN^2}{\pi}
 e^{\pi i n_v(N-1)^2/(4N)}
 \frac{e^{-iNt_v}}{(1-(-1)^{N-1}e^{-iNt_v})^2}.
 \tag{23}
\]
Every unit-charge depth is positive for the fixed graph.
Its leading trace charge has coefficient one; all higher
charges are exponentially smaller on this contour.
Neither \(\sin t_v^*\) nor the Gaussian determinant vanishes.
The original Gaussian calculation of [N, Section 6] therefore gives
(3)--(4), including the powers \(N^{2m-3e/2-m/2}\).
The actual-source gaps (20)--(21) prevent cancellation by the rest.
The same local holomorphic expansion gives every fixed order.

Allow sufficiently small independent complex outside angles.
All estimates above persist directly: the map (15) has a strict
interior margin, \(\Re C_v>0\), and the two adopted source estimates
hold on complex parameter neighborhoods. The fixed positive
unit-charge depths persist. Hence the phase, amplitude and normalized
error are holomorphic there. Separate evenness of the original source
and uniqueness give descent to ordinary outside colors near \(-2\).
Cauchy's formula retains every fixed ordinary spectral derivative,
including all required first and mixed normals. No derivative of
a nonzero amplitude is asserted nonzero.

## 6. The original marked consequence and scope

For an original ordered circle-tree exterior retain its page order,
disk frames, carriers \(\eta_v\), and primitive curves, and put
\(n_v=\eta_v-2p_v\). The new positive unit-charge solution satisfies
\[
 \sum_{e\ni v}r_{v,e}=\frac{in_vt_v^*}{2}-\pi i,\qquad
 \Im t_v^*<0 .
 \tag{24}
\]
The marked completion theorem [M] applies to these full logarithms
and original slopes \(\mu_v+p_v\lambda_v^{\rm disk}\). Its absolute
volume is \(2\pi M\), with every original complete edge included.
Consequently [N, Corollary 2] holds with \(R_v\ge32\) in place
of \(64\): if all auxiliary vertices are filled and literal strand
tracing gives one main component and no internal closed component,
the resulting knot satisfies the original full-level Kashaev volume
identity, with eventual nonzero leading coefficient (4).

An arbitrary same-index graph is not thereby a knot presentation.
Other edge kernels are not silently replaced. The powers and graph
are fixed before \(N\) tends to infinity. No assignment with
\(R_v<32\) is asserted covered by this proof, and no theorem for
arbitrary fixed short partial fillings or finitely many exceptions follows.

## Complete proof sources and coverage

All three complete direct texts were read at these matching pins.
The new matrix bound, constants and source comparisons are proved
above; no mathematical programs or saved numerical results are used.

| Direct | Entire source | SHA-256 |
|---|---|---|
| N | [Original network source](research_network_degree_power_source.md) | a7f61d2565232b2195b3c660f0a4dbb329e8c8156d690005ed058ba8c693fbd1 |
| P | [Original positive edge geometry](research_positive_edge_global_monotonicity.md) | da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500 |
| M | [Original marked completion](research_positive_point_marked_completion.md) | 28de22f081e24629ea6d26ad05213301a9bcf5d17d3ae7d00cc9c675a8218887 |

The entire [edge-Hessian note](research_edge_hessian_and_phase_response.md)
and [isolated coverage theorem](research_isolated_vertex_coverage_and_assembly.md)
were read for coverage. The former contains the determinant/trace
framework, but not (6)'s relative bound or this source improvement.
The isolated theorem already covers every \(d+|n|>2\) when the other
ends remain near complete; it does not assemble arbitrary adjacent
short vertices. No novelty is claimed for sector bounds, contraction
mapping or stationary phase as general methods.

Only written mathematics, text reads, hashes and this new-file write
were used. Earlier final notes, manuscripts and public documents
remain unchanged. The complete exact author-final and all three
complete matching proof directs were read before freezing.
Independent entire-final and entire-direct reviews are required
before adoption.
