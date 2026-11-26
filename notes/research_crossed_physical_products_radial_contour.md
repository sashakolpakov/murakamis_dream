# An original radial contour for crossed physical-row products

Private written proof, 17 November 2026.

A product of arbitrary macroscopic physical rows admits a complete
one-vertex crossing asymptotic at every fixed signed power of magnitude
at least four. The contour is constructed from the actual row action.
Its entire reflected half, both outer angular portions, the two endpoint
connectors, and every original Fourier alias are estimated. No spectral
cut current is dropped: the proof uses the exact full-grid angular lens.

The leading coefficient below uses the logarithm of the actual finite
row polynomials. This supplies a nonzero relative asymptotic without
postulating a level-independent row amplitude on a complex chart.
External derivative rows and subsequent observations are not covered.

## 1. Source, phase, and statement

Put
\[
 N\ge3,\quad D=N-1,\quad q=e^{\pi i/N},\quad
 \eta=(-1)^D,\quad c_j=2\cos((2j+1)\pi/N),\quad
 J=\lfloor D/2\rfloor,
\]
\[
 P_N(C)=2T_N(C/2)+2,\qquad
 \phi_N(f)=\eta N^2[C^D]\operatorname{rem}_{P_N}f,
 \qquad F_{j,N}(C)=K_N(c_j,C).
 \tag{1}
\]
Fix an integer \(m\ge3\), a positive \(\epsilon\), and an integer
\(p\ge4\). The physical indices may depend on \(N\), subject to
\[
 0\le j_i\le J,\qquad \sum_i j_i-D\ge\epsilon N.
 \tag{2}
\]
The scalar under consideration is exactly
\[
 Z_{p,N}(\mathbf j)=
 \phi_N\!\left(R^p\prod_{i=1}^mF_{j_i,N}\right).
 \tag{3}
\]
The ordinary product is taken before the original canonical trace.
In particular (3) retains all closing first normals and the odd simple
node. No normal in an external index \(j_i\) is asserted below.

For \(0\le x\le1/2\) define the source-normalized slit profile
\[
 \Psi_x(C)=2\int_0^x
  \operatorname{arsinh}\!\left(\tfrac12\sqrt{2-C}\cot(\pi u)\right)du,
 \qquad C\in\mathbb C\setminus[2,\infty),
 \tag{4}
\]
with the branches positive on \(C<2\), and set
\[
 S_{\mathbf x}(t)=\sum_i\Psi_{x_i}(-2\cos t),\qquad
 \Phi_{p,\mathbf x}(t)=S_{\mathbf x}(t)
                  +\frac{ip t^2}{4\pi}-it.
 \tag{5}
\]
The angular branch is the original one on \(|\Re t|<\pi\).
At \(x_i=0\) its corresponding summand is zero.

**Theorem 1.** Uniformly over (2), there is a unique critical point
selected by the contour constructed below,
\[
 t_p(\mathbf x)=s_p(\mathbf x)-ih_p(\mathbf x),\qquad
 0<s_p<2\pi/p,\quad h_p>0,\qquad \mathbf x=\mathbf j/N.
 \tag{6}
\]
Its real action
\[
 M_p(\mathbf x)=\Re\Phi_{p,\mathbf x}(t_p(\mathbf x))
 \tag{7}
\]
is positive. The point, its depth, and its distance from both ends
of the interval in (6) have uniform positive buffers on the support
compact in (2). Moreover \(\Re\Phi_{p,\mathbf x}''(t_p)<0\),
uniformly away from zero.

Let \(\mathscr L_{j,N}(C)=\log F_{j,N}(C)\) be the original
logarithm real on \(C< c_0\). In a fixed neighborhood of the
selected point put
\[
 \Phi_{p,N}(t)=\frac1N\sum_i\mathscr L_{j_i,N}(-2\cos t)
                    +\frac{ip t^2}{4\pi}-it.
 \tag{8}
\]
It has a unique nearby actual critical point
\[
 t_{p,N}=t_p(\mathbf j/N)+O(\log N/N).
 \tag{9}
\]
With the square root having positive real part,
\[
 \boxed{\quad
 Z_{p,N}(\mathbf j)=
 \frac{iN^{3/2}}{\pi}\,q^{pD^2/4}
 \sin(t_{p,N})
 \sqrt{\frac{2\pi}{-\Phi_{p,N}''(t_{p,N})}}
 e^{N\Phi_{p,N}(t_{p,N})}
 \bigl(1+O(N^{-1})\bigr).
 \quad}
 \tag{10}
\]
All errors are uniform in (2); constants may depend on the fixed
\(m,\epsilon,p\). The displayed coefficient is nonzero. In particular
\[
 \log|Z_{p,N}(\mathbf j)|
           =N M_p(\mathbf j/N)+O(\log N).
 \tag{11}
\]
For fixed \(p\le-4\) use the exact conjugacy
\(Z_{p,N}=\overline{Z_{-p,N}}\). Thus (10) also specifies its
original phase and scalar by conjugation. There is no assertion here
for powers of magnitude one, two, or three, or for further graph
contractions of (3).

## 2. The actual row facts used in the proof

The source Jacobi matrix gives real roots \(\lambda_{j,b}>c_0\) and
\[
 F_{j,N}(C)=\prod_{b=1}^j
                \frac{\lambda_{j,b}-C}{\lambda_{j,b}-c_0},
 \qquad F_{0,N}=1.
 \tag{12}
\]
Consequently the logarithm in (8) is well defined on
\(\mathbb C\setminus[c_0,\infty)\), with its prescribed real
normalization, and for every fixed \(r\ge1\)
\[
 |\partial_C^r\mathscr L_{j,N}(C)|
 \le (r-1)!\,j\,
       \operatorname{dist}(C,[c_0,\infty))^{-r}.
 \tag{13}
\]
The pinned slit theorem proves, uniformly in all physical rows,
\[
 N^{-1}\mathscr L_{j,N}(C)=\Psi_{j/N}(C)+o(1)
 \tag{14}
\]
on fixed slit compacts, with all fixed derivatives. On compact
subsets of \(\Re C<2\), the error before division by \(N\) is
\(O(\log N)\). The statements include the zero and last rows.

A separate elementary bound will cover the spectral endpoint, where
a fixed slit compact is unavailable. Formula (12) gives
\[
 |F_{j,N}(C)|\le F_{j,N}(c_0-|C-c_0|).
 \tag{15}
\]
For a fixed small \(d>0\), all \(|C-2|\le d\) and sufficiently
large \(N\) therefore satisfy
\[
 |F_{j,N}(C)|\le F_{j,N}(2-3d)
       \le N^B\exp\{N\Psi_{1/2}(2-3d)\}.
 \tag{16}
\]
Indeed \(c_0-|C-c_0|\ge2-3d\) and a real row decreases on
\(( -\infty,c_0]\); use (14) on the negative side of the cut.
Also \(\Psi_x(C)\le\Psi_{1/2}(C)\) for real \(C<2\), directly
from (4). Dominated convergence in (4), with the integrable bound
\(C(1+|\log u|)\), proves
\[
                 \Psi_{1/2}(2-3d)\longrightarrow0
                              \quad(d\downarrow0).
 \tag{17}
\]
No root lower bound beyond \(\lambda_{j,b}>c_0\) is needed in
(15)--(17).

## 3. A radial minimum and its positive geometry

All sufficiently large levels in (2) lie in the fixed compact
\[
 \mathcal X=\{\mathbf x\in[0,1/2]^m:
                          \sum_i x_i\ge1+\epsilon/2\}.
 \tag{18}
\]
If this set is empty there is no assertion to prove. Write
\(k_i=\sin(\pi x_i)\), \(a=2\pi/p\le\pi/2\), and
\[
 A(s,h)=\Re S_{\mathbf x}(s-ih)+\frac{p s h}{2\pi}-h,
                   \qquad 0\le s\le a,\ h\ge0.
 \tag{19}
\]
Differentiating (4), or substituting \(\sin(\pi u)\) in its
derivative integral, gives exactly
\[
 S_{\mathbf x}'(t)=-\frac1\pi\sum_i r_i(t),\qquad
 r_i(t)=\operatorname{arsinh}(k_i\tan(t/2)).
 \tag{20}
\]
Thus
\[
 A_h=-\frac1\pi\sum_i\Im r_i(s-ih)+\frac{p s}{2\pi}-1,
 \qquad
 A_s=-\frac1\pi\sum_i\Re r_i(s-ih)+\frac{p h}{2\pi}.
 \tag{21}
\]

For \(k_i>0\), the original branches give
\[
 r_i'(t)=
 \frac{k_i}{2\cos(t/2)
       \sqrt{\cos^2(t/2)+k_i^2\sin^2(t/2)}}.
 \tag{22}
\]
For \(t=s-ih\), \(0\le s\le\pi/2\), both
\(\cos^2(t/2)\) and
\(\cos^2(t/2)+k_i^2\sin^2(t/2)\) have arguments between
zero and \(s\), strictly inside the right half-plane at finite
\(h\). This follows by writing them respectively as
\((1+\cos t)/2\) and
\((1+k_i^2+(1-k_i^2)\cos t)/2\).
Their original square roots have arguments between zero and
\(s/2\). The denominator in (22) therefore has argument strictly
between \(-\pi/2\) and \(\pi/2\), including when \(s=\pi/2\).
It follows that
\[
                 A_{hh}=\frac1\pi\sum_i\Re r_i'(s-ih)>0.
 \tag{23}
\]
Zero rows contribute zero and do not affect strictness on (18).

At the lower boundary and at infinity,
\[
 A_h(s,0)=ps/(2\pi)-1,\qquad
 \lim_{h\to\infty}A_h(s,h)=\sum_i x_i+ps/(2\pi)-1.
 \tag{24}
\]
The second limit is uniform in (18) and \(0\le s\le a\):
\(\tan((s-ih)/2)\to-i\), and the continued inverse sine
is uniformly continuous at \(k_i\in[0,1]\). Hence, for
\(0\le s<a\), there is exactly one \(h(s)>0\) with
\(A_h(s,h(s))=0\). At \(s=a\) it is \(h(a)=0\).
These roots lie in a uniform bounded height interval. Equation
(23) gives their continuous dependence on all parameters and
their smooth dependence in \(s\), including at \(a\).

Set \(b(s)=A(s,h(s))\). Harmonicity of the holomorphic phase
gives \(A_{ss}=-A_{hh}\), while implicit differentiation gives
\[
 b''(s)=-A_{hh}-\frac{A_{sh}^2}{A_{hh}}<0.
 \tag{25}
\]
At its two ends,
\[
 b'(0)=\frac{p h(0)}{2\pi}>0,
 \qquad
 b'(a)=-\frac1\pi\sum_i
                       \operatorname{arsinh}(k_i\tan(\pi/p))<0.
 \tag{26}
\]
Thus there is a unique maximum \(s_p\in(0,a)\), and both
real equations in (21) vanish there. This proves (6).
Compactness of (18), (23)--(26) gives all stated uniform buffers
and \(-\Re\Phi''=A_{hh}>0\) at the saddle.

Its action is positive. At \(s=0\), (19) is
\(\sum_i\Psi_{x_i}(-2\cosh h)-h\). For every finite \(h\ge0\),
\(\operatorname{arsinh}z>\log(2z)\), \(z>0\), implies
\[
 \Psi_x(-2\cosh h)\ge
 xh+2x\log(1+e^{-h})+2\int_0^x\log\cot(\pi u)\,du.
 \tag{27}
\]
The last integral is nonnegative for \(0\le x\le1/2\): it
increases up to \(1/4\), then decreases to zero by the
substitution \(u\mapsto1/2-u\). Hence \(b(0)>0\), uniformly
on (18), since \(h(0)\) is uniformly bounded. The maximum is
strictly larger than \(b(0)\).

For the geometric interpretation, put \(\alpha_i=\pi-2\pi x_i\).
On strict outside angles \(\alpha_i<\pi\), the original edge
phase is exactly \(\psi(\alpha_i,t)=\Psi_{x_i}(-2\cos t)\):
(20) gives its original return and (4) fixes its normalization.
Every point of the radial graph has positive original edge angles.
Indeed write \(\tan(t/2)=A-iB\). On \(0\le s\le\pi/2\),
\[
 B=\frac{\sinh h}{\cosh h+\cos s}<1.
\]
With real \(b_i=\tan(\alpha_i/2)\),
\(q_i^2=1+(A-iB)^2+b_i^2\) has
\(\Re q_i^2=A^2+b_i^2+1-B^2>A^2+b_i^2\).
The original square root therefore satisfies
\(\Re q_i>\sqrt{A^2+b_i^2}\), the exact positive-edge
criterion. The saddle equation is the original unit-charge
equation \(\sum_i\psi_t+ipt/(2\pi)=i\).
If \(x_i=0\), the finite row is exactly one; the source theorem
continues to hold, but that limiting incidence is not called a
strict positive edge. No filled-manifold volume identification is
being inferred from these equations.

## 4. Paying the complete original lens

The pinned full-grid identity applied to the literal polynomial
\(f_N=\prod_i F_{j_i,N}\) states that for every lower arc
\(\Gamma\) from \(-\pi\) to \(\pi\),
\[
 Z_{p,N}=-\frac{N^2q^{pD^2/4}}{\pi i}
 \int_\Gamma
  \sin t\,f_N(-2\cos t)e^{ipNt^2/(4\pi)}W_N(t)\,dt,
 \qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}.
 \tag{28}
\]
This identity includes every closing first normal. At odd \(N\)
the simple node is already the single value contribution in the
full-grid residue calculation; there is no extra term to append.
The two spectral cut banks are encoded by this exact angular
chain, not replaced by one off-grid Gaussian branch on a circle.

Before giving it a positive minimum depth, reflect the radial
height evenly, \(h(-s)=h(s)\). The action on its negative half is
\[
 \Re\Phi_{p,\mathbf x}(-s-ih(s))
       =b(s)-\frac{p s h(s)}\pi,\qquad 0\le s\le a.
 \tag{29}
\]
Its maximum is strictly below \(M_p\). Equality would first force
\(s=s_p\) by the strict maximum of \(b\), but then the subtracted
term is positive. Compactness makes this a uniform strict gap.
On the positive half, outside any fixed small saddle neighborhood,
strict concavity gives another uniform gap.

On the real outer intervals \(a\le |s|\le\pi\), the action is
\(S_{\mathbf x}(s)\). Equation (20) shows that it decreases
strictly with \(|s|\), so it is at most
\(S_{\mathbf x}(a)=b(a)<M_p\), uniformly. Choose a small fixed
depth \(v>0\), replace \(h(s)\) by \(\max(h(s),v)\) on
\([-a,a]\), and use depth \(v\) on the outer intervals.
Choose \(v\) after the preceding strict gaps. The saddle
neighborhood is unchanged. Uniform continuity preserves all gaps
on angular compact subsets away from \(\pm\pi\).

Here is the missing endpoint estimate explicitly. Choose a small
fixed endpoint neighborhood and then \(v\) so that throughout
it \(|-2\cos t-2|\le d\), with \(d\) as small as desired.
Equations (16)--(17) bound the product there by
\(N^B\exp\{Nm\Psi_{1/2}(2-3d)\}\). The Gaussian contributes
at most \(\exp(Np v/2)\). On the horizontal part,
\(|W_N|\le C e^{-Nv}\); on the two vertical segments
\(t=\pm\pi-iy\), \(0\le y\le v\), exactly
\[
 |W_N(\pm\pi-iy)|
       =\frac{e^{-Ny}}{(1+e^{-Ny})^2}\le e^{-Ny}.
 \tag{30}
\]
The Gaussian there costs at most \(e^{Np y/2}\).
Since \(\inf_{\mathcal X}M_p>0\), first choosing \(d\)
and then \(v\) small pays these entire endpoint portions with
a fixed strict gap. In particular no limiting slit estimate is
being used at \(C=2\), and no near-real pole is encountered.

Append those two vertical segments to the graph to obtain the
complete lower arc in (28). It is piecewise smooth; any corners
may be kept or rounded inside the proved strict-gap neighborhoods.
On the remaining compact parts, (14) makes the limiting action
gaps into actual finite-source gaps. All graph points have depth
at least \(v\), so there
\[
 W_N(t)=e^{-iNt}\bigl(1+O(e^{-Nv})\bigr).
 \tag{31}
\]
Every nonleading Fourier alias is included in this estimate.
Together with (30), it accounts for the full denominator even at
the angular endpoints. Thus the complete contribution outside a
fixed local saddle neighborhood is
\[
                  O\!\left(N^B e^{N(M_p-\delta)}\right)
 \tag{32}
\]
for some uniform \(\delta>0\).

## 5. Actual finite-phase stationary integration

The favorable saddle lies in a compact subset of
\(0<\Re t<\pi/2\), \(\Im t<0\). Its spectral image has
\(\Re C<2\) with a uniform buffer. Equations (13)--(14) imply
on a larger fixed neighborhood
\[
 \Phi_{p,N}-\Phi_{p,\mathbf j/N}=O(\log N/N)
 \tag{33}
\]
with every fixed derivative. The nonzero second derivative and
the holomorphic inverse function theorem give the unique nearby
critical point (9). A small local deformation of the exact lens
through it is legitimate; all endpoints of that deformation stay
in the original lower strip and its connecting portions remain
inside the already controlled saddle neighborhood.

For precision, the real-height minimum of the actual phase exists
near the limiting graph by (23),(33). Its real maximum is precisely
\(t_{p,N}\). On this graph let
\(a_N=-\Re\Phi_{p,N}''>0\), \(b_N=\Im\Phi_{p,N}''\).
Its oriented tangent at the saddle is
\(T_N=1+i b_N/a_N\), and
\[
       \Phi_{p,N}''T_N=-(a_N^2+b_N^2)/a_N<0.
 \tag{34}
\]
This fixes the Gaussian orientation. It is the same branch as
the square root of \(-\Phi_{p,N}''\) with positive real part;
the tangent factor cancels against the corresponding square root
of its square. Uniform analytic derivative bounds in (13) give
the usual one-dimensional stationary integral, here with the
literal amplitude \(\sin t\):
\[
 \int_{\rm local}\sin t\,e^{N\Phi_{p,N}(t)}dt
 =\frac{\sin(t_{p,N})}{\sqrt N}
       \sqrt{\frac{2\pi}{-\Phi_{p,N}''(t_{p,N})}}
       e^{N\Phi_{p,N}(t_{p,N})}
       \bigl(1+O(N^{-1})\bigr).
 \tag{35}
\]
One may prove the stated uniform error by a local analytic Morse
coordinate: expand its analytic amplitude through the linear
term on a symmetric real interval, whose odd term integrates to
zero; the quadratic remainder has relative size \(O(N^{-1})\).
All needed radii and derivatives are uniform on the compact family.
The amplitude is uniformly nonzero because \(t_{p,N}\) stays away
from every zero of \(\sin t\).

Equation (31) supplies only an exponentially small relative error
on this local piece. Multiplying (35) by the original factor
\(-N^2q^{pD^2/4}/(\pi i)\) gives (10). Equations (32)--(33)
show that the complete complement is exponentially smaller than
this nonzero term, even after the possible \(N^{O(1)}\) change
between its actual and limiting actions. This proves (11).
Conjugacy follows directly from the real original rows and trace
and the full physical jets of \(R^{-p}=\overline{R^p}\).

## 6. Scope and complete direct sources

This is a full one-vertex scalar theorem for the actual physical-row
inputs (2), with unrestricted fixed number \(m\ge3\) and fixed
\(|p|\ge4\). It differs from the degree-two boundary theorem,
which concerns two full free kernels near complete output, and from
the recursive high-valence theorem, which requires sufficiently
many previously transformed packets with a common boundary disk.
The rows here may occupy any macroscopic positions in the support
compact, including the zero and last rows.

The theorem does not provide an external normal estimate, an
invariant class under a further turn, or a lower bound for a graph
obtained by closing its external labels. Its positive local edge
geometry has been identified on strict outside angles, but no
manifold volume formula is asserted. The range \(|p|<4\) requires
a separate contour argument; no failure there is claimed.

The complete direct texts were read at the following pins, and
their used implications were checked:

* [Original full-grid lens](research_full_grid_lens_source_continuation.md),
  SHA256 d141e6e8c23572bb13484807a2359395a0371d6a3d699198826a105b6dad5649:
  exact scalar and crossing carrier, both-parity full trace,
  entire endpoint chain, and complete Fourier denominator.
* [All physical rows on the slit plane](research_mixed_next_first_short_edge_slit_plane_bound.md),
  SHA256 efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b:
  original Jacobi root product and logarithm, all-row profile,
  half-plane \(O(\log N)\) error, and fixed derivative bounds.
* [Original positive product chart](research_positive_wire_product_contour.md),
  SHA256 5646f2d6b2a8dfa2d8c49662d17f19f3743fc4efcaf3c3685c6a899975a4c230:
  original positive-edge criterion and its branch convention.

Only written mathematics, complete source reads and metadata hashes
were used. No mathematical programs, tests, numerical evaluations,
or builds were run. Frozen notes and public manuscripts are unchanged.
