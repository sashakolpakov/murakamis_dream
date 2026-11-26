# Crossed physical products below the positive-coefficient support wall

Private written proof, 17 November 2026.

The crossed radial contour does not require a positive uncrossed
coefficient. Constraining the radial minimization to one explicit
bounded height gives a unique interior saddle whenever the total
physical degree is bounded below by a positive multiple of the level.
The complete original scalar asymptotic, every mixed first-normal
upper bound, the bulk normal coefficient, and the exact-jet local
packet extend to this larger domain.

The excluded boundary is now only total degree \(o(N)\). This is a
one-vertex source theorem. No subsequent shared trace, general tree
closure, or manifold-volume conclusion is inferred.

## 1. Original source and the enlarged domain

Use
\[
 N\ge3,\quad D=N-1,\quad q=e^{\pi i/N},\quad
 \eta=(-1)^D,\quad J=\lfloor D/2\rfloor,
\]
\[
 c_j=2\cos((2j+1)\pi/N),\quad P_N(C)=2T_N(C/2)+2,
 \quad \phi_N(f)=\eta N^2[C^D]\operatorname{rem}_{P_N}f,
\]
\[
 F_j(C)=K_N(c_j,C),\qquad
 G_j(C)=\left.\partial_wK_N(w,C)\right|_{w=c_j}.
 \tag{1}
\]
The prescribed \(G_j\) exists only at a double physical node.
At the odd simple node only the value is used.

Fix an integer \(m\ge1\), a number \(\delta>0\), and an integer
\(p\ge4\). The indices may depend on the level and obey
\[
          0\le j_i\le J,\qquad \sum_{i=1}^m j_i\ge\delta N.
 \tag{2}
\]
There is no condition involving \(\sum_i j_i-D\). In particular
the uncrossed trace of their ordinary product may vanish identically.
For any subset \(I\) of double-node positions define
\[
 Z_{p,N,I}(\mathbf j)=
  \phi_N\!\left(R^p\prod_{i\in I}G_{j_i}
                         \prod_{i\notin I}F_{j_i}\right),
 \qquad Z_{p,N}=Z_{p,N,\varnothing}.
 \tag{3}
\]
All factors are multiplied before the original canonical trace.
The closing first normals and the odd simple value remain literal.

For \(0\le x\le1/2\) retain the original normalized profile
\[
 \Psi_x(C)=2\int_0^x
  \operatorname{arsinh}\!\left(\tfrac12\sqrt{2-C}\cot(\pi u)\right)du,
                  \qquad C\in\mathbb C\setminus[2,\infty),
 \tag{4}
\]
and put
\[
 S_{\mathbf x}(t)=\sum_i\Psi_{x_i}(-2\cos t),\qquad
 \Phi_{p,\mathbf x}(t)=S_{\mathbf x}(t)+\frac{ip t^2}{4\pi}-it.
 \tag{5}
\]
All branches and crossing scalars are those of the pinned radial
source. The relevant closed parameter set is
\[
 \mathcal X_\delta=
 \{\mathbf x\in[0,1/2]^m:\ \sum_i x_i\ge\delta\}.
 \tag{6}
\]
An empty parameter set makes the assertions vacuous.

**Theorem 1.** Uniformly on (2), the phase (5) has one saddle
selected by the bounded contour below,
\[
 t_p(\mathbf x)=s_p-ih_p,\quad
 0<s_p<a:=2\pi/p,\quad 0<h_p<H:=1+2m/p,
 \qquad \mathbf x=\mathbf j/N.
 \tag{7}
\]
The distances from all four sides in (7), its nonzero Hessian,
and its positive real action
\[
                M_p(\mathbf x)=\Re\Phi_{p,\mathbf x}(t_p)
 \tag{8}
\]
have uniform buffers depending only on \(m,\delta,p\).

Use the actual finite logarithms, real on \(C<c_0\), to define
\[
 \Phi_{p,N}(t)=N^{-1}\sum_i\log F_{j_i}(-2\cos t)
                            +\frac{ip t^2}{4\pi}-it.
 \tag{9}
\]
Its unique nearby critical point is
\(t_{p,N}=t_p(\mathbf j/N)+O(\log N/N)\). With the square
root having positive real part, the complete original scalar is
\[
 \boxed{\quad
 Z_{p,N}(\mathbf j)=
  \frac{iN^{3/2}}\pi q^{pD^2/4}\sin(t_{p,N})
  \sqrt{\frac{2\pi}{-\Phi_{p,N}''(t_{p,N})}}
  e^{N\Phi_{p,N}(t_{p,N})}\bigl(1+O(N^{-1})\bigr).
 \quad}
 \tag{10}
\]
In particular it is nonzero for all sufficiently large levels,
uniformly in (2), and
\[
             \log|Z_{p,N}|=N M_p(\mathbf j/N)+O(\log N).
 \tag{11}
\]

**Theorem 2.** Every allowed mixed normal satisfies
\[
 |Z_{p,N,I}|\le C N^B e^{NM_p(\mathbf j/N)}
                       \le C N^{B'}|Z_{p,N}|.
 \tag{12}
\]
If each selected \(j_i/N\), \(i\in I\), stays in a fixed compact
subinterval of \((0,1/2)\), then, with \(C_{p,N}=-2\cos t_{p,N}\),
\[
 \frac{Z_{p,N,I}}{Z_{p,N}}
   =N^{|I|}\left\{\prod_{i\in I}g(j_i/N,C_{p,N})
                                      +O(\log N/N)\right\},
 \tag{13}
\]
\[
 g(x,C)=-\frac{2\operatorname{arsinh}
       (\tfrac12\sqrt{2-C}\cot(\pi x))}{4\pi\sin(2\pi x)}.
 \tag{14}
\]
Every selected factor is a uniform unit. Unselected rows may
approach zero or the last physical row.

**Theorem 3.** Every compact subset of \((0,1/2)^m\) has a finite
cover by real product neighborhoods with fixed thin complex
neighborhoods on which one holomorphic scalar \(\mathcal W_{p,N}\)
has, at all physical tuples in the product, every mixed first
spectral jet equal to \(Z_{p,N,I}\) up to
\[
                   C N^B e^{-\gamma N}|Z_{p,N}|.
 \tag{15}
\]
Here the external coordinates are \(w_i=C_N(x_i)\),
\(C_N(x)=2\cos(2\pi x+\pi/N)\), and the spectral derivative is
\(C_N'(x_i)^{-1}\partial_{x_i}\). A support margin for (2) is
chosen from the positive minimum of \(\sum x_i\) on the compact.
The physical error is exactly the omitted part of a fixed
saddle-arc lens. No off-grid canonical polynomial approximation
is asserted on that complex neighborhood.

All statements hold for fixed \(p\le-4\) by exact conjugation of
the positive-power source and coefficient. The powers and the
positive number \(\delta\) are fixed before \(N\to\infty\).

## 2. The bounded minimax construction

Let \(k_i=\sin(\pi x_i)\), and for \(0\le s\le a\), \(0\le h\le H\)
write
\[
 A(s,h)=\Re S_{\mathbf x}(s-ih)+\frac{p s h}{2\pi}-h,
 \qquad r_i(t)=\operatorname{arsinh}(k_i\tan(t/2)).
 \tag{16}
\]
The original return identity and its derivative are
\[
 S_{\mathbf x}'(t)=-\pi^{-1}\sum_i r_i(t),\qquad
 r_i'(t)=\frac{k_i}{2\cos(t/2)
                \sqrt{\cos^2(t/2)+k_i^2\sin^2(t/2)}}.
 \tag{17}
\]
The first pinned proof establishes these formulas on the original
branches and proves, for \(0\le s\le\pi/2\) and finite \(h\ge0\),
\[
 A_{hh}=\pi^{-1}\sum_i\Re r_i'(s-ih)>0,
               \qquad A_{ss}=-A_{hh}<0
 \tag{18}
\]
whenever some \(x_i>0\). The argument is the positive real part
of the two denominator factors in (17), not an asymptotic root
selection. It holds on the entire closed rectangle here. On (6),
compactness strengthens it to uniform constants
\[
                         c\le A_{hh}\le C.
 \tag{19}
\]
All derivatives in \(s,h\) needed below are uniformly bounded.
The zero rows have \(k_i=0\) and contribute zero; they introduce
no singularity into (17).

There is an explicit reason for the choice of \(H\). Throughout
this rectangle,
\[
 \left|\tan\frac{s-ih}{2}\right|^2
       =\frac{\cosh h-\cos s}{\cosh h+\cos s}\le1.
 \tag{20}
\]
For \(w=u+iv=\operatorname{arsinh}z\),
\(|\sinh w|^2=\sinh^2u+\sin^2v\), so
\(|\Re\operatorname{arsinh}z|\le\operatorname{arsinh}|z|\).
It follows that \(\Re r_i\le\operatorname{arsinh}1<1\).
Consequently
\[
 A_s(s,H)=-\pi^{-1}\sum_i\Re r_i(s-iH)+\frac{pH}{2\pi}
 \ge\frac p{2\pi}+\frac m\pi(1-\operatorname{arsinh}1)>0.
 \tag{21}
\]
This is uniform in all parameters, including zero and fold limits.

For each \(s\), let \(h_*(s)\) be the unique minimum of \(A(s,h)\)
on the compact interval \([0,H]\), and put
\[
                         b_H(s)=A(s,h_*(s)).
 \tag{22}
\]
Strict convexity in (19) gives uniqueness and continuous dependence
of \(h_*\) on \(s,\mathbf x\). The elementary envelope theorem gives
\(b_H'(s)=A_s(s,h_*(s))\), including the transitions at which the
minimum meets \(h=H\) or \(h=0\). One can check this without a
regularity theorem: compare the two minima at \(s\) and \(s+u\),
divide the resulting two inequalities by \(u\), and use continuity
of the unique minimizer.
The minimizer is uniformly Lipschitz in \(s\). Subtract its two
one-dimensional variational inequalities and use (19) and the bound
on \(A_{sh}\) to obtain
\(c|h_*(s)-h_*(r)|\le C|s-r|\). Thus all the graph contours below
have uniformly bounded lengths, including their constraint switches.

The function \(b_H\) is uniformly strongly concave. Indeed
\(A(s,h)+cs^2/2\) is concave in \(s\) for every \(h\), by (19),
and the infimum of concave functions is concave. Thus
\(b_H(s)+cs^2/2\) is concave even at an active-constraint transition.
On an interval where \(0<h_*<H\), its explicit second derivative is
\[
                 b_H''=-A_{hh}-A_{sh}^2/A_{hh}<0.
 \tag{23}
\]

The boundary signs are exact:
\[
 A_h(s,0)=ps/(2\pi)-1,
 \quad h_*(0)>0,
 \quad h_*(a)=0,
\]
\[
 b_H'(0)=p h_*(0)/(2\pi)>0,
 \qquad
 b_H'(a)=-\pi^{-1}\sum_i
                  \operatorname{arsinh}(k_i\tan(\pi/p))<0.
 \tag{24}
\]
They are uniformly separated from zero on (6). For the first,
(19) and \(A_h(0,0)=-1\) give a uniform positive lower bound for
\(h_*(0)\). For the second use \(\sum_i k_i\ge2\sum_i x_i\ge2\delta\)
and continuity on the compact parameter set.

It follows that \(b_H\) has one maximum at \(s_p\in(0,a)\).
It cannot have \(h_*(s_p)=H\), by (21) and the envelope derivative.
It cannot have \(h_*(s_p)=0\), because \(A_h(s_p,0)<0\).
Thus both real derivatives of the holomorphic phase vanish at
\(t_p=s_p-ih_*(s_p)\), proving an actual interior saddle.
All parameters vary continuously; compactness and the strict
boundary signs give uniform positive distances from the four sides.
Equation (19) also gives \(-\Re\Phi''(t_p)\ge c\).

Positivity no longer uses the uncharged coefficient saddle.
At \(s=a\), the minimum is \(h=0\), so
\[
 M_p=b_H(s_p)>b_H(a)=S_{\mathbf x}(a)
          =\sum_i\Psi_{x_i}(-2\cos a)>0.
 \tag{25}
\]
The last function has a strictly positive minimum on (6), by (4)
and \(\sum x_i\ge\delta\). This proves all geometric and compactness
claims in Theorem 1. Where the outside angles are strict, the
same original positive-edge criterion as in the pinned radial
proof applies because \(s\le a\le\pi/2\) and \(h\le H\).
It supplies positive original edge shapes, but no new topological
or volume interpretation is needed here.

## 3. The entire original source contour is still paid

The exact full-grid lens for \(f_N=\prod_iF_{j_i}\) is
\[
 Z_{p,N}=-\frac{N^2q^{pD^2/4}}{\pi i}
 \int_\Gamma \sin t\,f_N(-2\cos t)e^{ipNt^2/(4\pi)}W_N(t)dt,
 \qquad W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}.
 \tag{26}
\]
Its validity is independent of the degree of \(f_N\) relative to
\(D\). In particular a vanishing uncharged trace when the degree is
small does not remove (26) or its crossing. Both parities, every
closing normal, and the odd simple value are included once by this
identity.

Use the height \(h_*(s)\) on \([0,a]\) and its even reflection on
\([-a,0]\). The positive half has its sole strict maximum at \(s_p\).
On the reflected half the action is exactly
\[
       b_H(s)-p s h_*(s)/\pi,\qquad 0\le s\le a,
 \tag{27}
\]
and hence has a uniform strict gap below \(M_p\). Equality would
force \(s=s_p\), where the subtracted term is positive. The real
outer intervals \(a\le|s|\le\pi\) have decreasing action
\(S_{\mathbf x}(s)\le S_{\mathbf x}(a)<M_p\), by (17).

Give the graph a small fixed minimum depth \(v>0\), by replacing
\(h_*\) with \(\max(h_*,v)\), and use depth \(v\) on both outer
intervals. The new constrained-height corners cause no difficulty:
on the whole fixed rectangle all functions are uniformly continuous,
and the changes occur away from the selected saddle if \(v\) is
chosen sufficiently small. The strict gaps persist. The graph is
piecewise smooth; its constraint transitions may also be rounded
within these strict-gap neighborhoods. One can alternatively use
the Lipschitz graph given by the uniformly strongly convex minimizer.

At \(t=\pm\pi-iy\), \(0\le y\le v\), keep the original vertical
endpoint connectors. The source bounds used in the first pinned
proof remain uniform in every physical row and do not use a support
margin:
\[
 |F_j(C)|\le F_j(c_0-|C-c_0|),
 \qquad
 \sup_{|C-2|\le d}|F_j(C)|
      \le N^B e^{N\Psi_{1/2}(2-3d)},
 \tag{28}
\]
where \(\Psi_{1/2}(2-3d)\to0\) as \(d\downarrow0\). Also exactly
\[
 |W_N(\pm\pi-iy)|=
       \frac{e^{-Ny}}{(1+e^{-Ny})^2}\le e^{-Ny}.
 \tag{29}
\]
The Gaussian there costs at most \(e^{Np y/2}\). Choose \(d\)
and then \(v\) using the uniform positive lower bound (25).
This pays all endpoint neighborhoods and the full connectors.
On the remaining slit compacts the actual row logarithms obey
\(\log F_j=N\Psi_{j/N}+o(N)\) uniformly over all rows. Near the
favorable saddle their error is \(O(\log N)\), because its spectral
image lies in a compact subset of \(\Re C<2\). None of these
source facts uses \(\sum j_i-D>0\).

All portions at depth at least \(v\) retain
\[
                    W_N(t)=e^{-iNt}(1+O(e^{-Nv})).
 \tag{30}
\]
Thus every nonleading alias is paid there, while (29) retains the
whole denominator at the endpoints. The complete complement of a
fixed small saddle neighborhood has size
\(O(N^B e^{N(M_p-\gamma_0)})\), for a uniform positive \(\gamma_0\).

The actual finite phase (9) and all its fixed derivatives differ
from (5) by \(O(\log N/N)\) near the saddle. Its nearby critical
point has a nonzero second derivative with negative real part.
Exactly the oriented finite-phase Gaussian argument of the pinned
radial proof applies. It gives (10), including the original scalar
\(q^{pD^2/4}\), the sign \(i/\pi\), and the square-root orientation.
The leading coefficient is uniformly nonzero; the paid complement
is exponentially smaller even after the polynomial change between
the actual and limiting actions. This proves (11).

## 4. Original mixed normals and the exact-jet packet

The second pinned source supplies, independently of any degree-sum
condition, the exact representative
\[
 \widehat G_j(C)=
  \frac{c'(0)F_j(C)\widetilde Q_N(C)+R_j(C)}{c'(j)},
 \qquad c'(j)=-\frac{4\pi}{N}\sin((2j+1)\pi/N),
 \tag{31}
\]
with \(\widehat G_0=\widetilde Q_N\). Here \(R_j\) is the actual
common-shift determinant derivative, and \(\widetilde Q_N\) is the
even Ward representative. At every inner physical color it matches
the value and required first normal of the original \(G_j\). Thus
its products preserve (3), including the derivative of \(R^p\) and
all mixed product-rule terms.

Its angular lift is even, holomorphic in the canonical strip and
bounded up to fixed-height endpoint rectangles. The residue and
reflection proof of (26) therefore applies to every such product,
by the fixed-level endpoint limit already proved in the pinned
full-normal theorem. It is not a free off-grid polynomial equality.

On slit compacts \(\widehat G_j/F_j\) has a uniform polynomial
bound. On \(|C-2|\le d\), the exact cofactor proof gives instead
\[
                 |\widehat G_j(C)|\le C_dN^B F_j(2-3d),
 \tag{32}
\]
with the original angular branch understood on endpoint caps.
To recall the crucial bound, for every Jacobi root \(\lambda>c_0\),
\(|\lambda-C|\le\lambda-(2-3d)\) and
\(\lambda-(2-3d)\ge2d\), for sufficiently large \(N\).
Omitting a determinant factor therefore costs only \(1/(2d)\).
The Ward term and all original derivative coefficients are
polynomially bounded. This includes the zero row and even last
normal; the odd simple node carries only its value.

Consequently all complement estimates in Section 3 survive every
fixed mixed first-normal insertion. The local integral has only a
polynomial loss, proving (12) by the nonzero scalar estimate (10).
For selected bulk indices the actual scalar normal connection gives
\[
       \frac{\widehat G_j(C)}{N F_j(C)}
             =g(j/N,C)+O(\log N/N)
 \tag{33}
\]
with all fixed spectral derivatives on the favorable half-plane
compact. Since \(\cos(t_p/2)\cot(\pi x)\) has positive real part,
the inverse hyperbolic sine in (14) is nonzero; compactness gives
a uniform unit. The same actual finite-phase Gaussian calculation
with this analytic amplitude proves (13).

Finally take a strict bulk external product neighborhood. The exact
scalar correction in the second pinned proof supplies a holomorphic
function \(\mathfrak F_N(x,C)\) on a thin fixed degree neighborhood
times the favorable spectral compact, with exact identities
\[
 \mathfrak F_N(j/N,C)=F_j(C),\qquad
 \partial_x\mathfrak F_N(j/N,C)=C_N'(j/N)\widehat G_j(C).
 \tag{34}
\]
This is a rowwise source construction; it has no restriction on
the sum of the external degrees. Fix one reference radial lens and
a small subarc \(\gamma_0\) containing its saddle. On a sufficiently
small real product neighborhood, the entire complement retains its
strict gap, by continuity, (28), and (32). Define
\[
 \mathcal W_{p,N}(\mathbf x)=
 -\frac{N^2q^{pD^2/4}}{\pi i}
 \int_{\gamma_0}\sin t\,e^{ipNt^2/(4\pi)}W_N(t)
               \prod_i\mathfrak F_N(x_i,-2\cos t)\,dt.
 \tag{35}
\]
The arc is fixed in the external variables. At every physical tuple,
each mixed first spectral jet of its integrand is exactly the
corresponding product in (3), by (34). Its physical error is precisely
the complementary lens. The positive gap, divided by the nonzero
value lower bound (10), proves (15). The scalar-connection exponent
only limits the available complex thickness; it does not enter this
physical comparison error. A finite cover proves Theorem 3.

## 5. Exact scope and complete sources

The new content is the bounded minimax in Section 2 and its use on
the complete source: it removes both the condition \(m\ge3\) and
the positive-uncrossed-support condition \(\sum j_i-D\ge\epsilon N\).
All original phases, full closing jets and endpoint currents are
retained. The threshold \(|p|\ge4\) is unchanged.

The excluded domain \(\sum j_i=o(N)\), a further original shared
trace, and arbitrary finite-tree closure are not conclusions here.
The local packet is not a whole-grid off-real equality with the
canonical multivariate polynomial. The geometric Schur-complement
closure on a supplied positive domain does not by itself supply
those remaining source estimates.

Both complete direct texts were read at the following pins, with
their used implications checked:

* [Original crossed radial contour](research_crossed_physical_products_radial_contour.md),
  SHA256 db63d7bf100a6d35647b6c9b4832d16c6f5520a7a9c38c0fd322f87659c9d50e:
  actual row logarithms and return, exact full-grid lens and carrier,
  endpoint/alias estimates, and oriented finite-phase Gaussian.
* [Crossed full-normal source and scalar packet](research_crossed_physical_products_full_normal_packet.md),
  SHA256 84388316d1b6122e940832201b5a9b181d330bc6ea6094a22aafff9007076a53:
  original Ward--Jacobi representatives, exact even full-lens trace,
  all-row cofactor estimates, bulk normal multiplier, and exact
  rowwise scalar correction on the favorable half-plane chart.

Only written mathematics, complete source reads and metadata hashes
were used. No mathematical programs, tests, numerical evaluations,
or builds were run. Frozen notes and public manuscripts are unchanged.
