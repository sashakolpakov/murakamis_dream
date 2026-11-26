# The marked edge and peripheral lattice of the original five-cell assembly

Private written proof, 17 November 2026. The five-cell ball replacement
in [T] permits an integral comparison with the actual complete source
rows of [R] and [L]. This note records the edge windings, their parity,
the one extra meridian row, and the original longitude convention.
The comparison is on the continued complete source lift. It does not
transport the finite state or its relative cycle to new quantum tensors.

## 1. Diagram, source and logarithmic conventions

Fix the original closed signed physical source diagram of [R], closing
to one knot, with \(c>0\) crossings, its original cut, and writhe
\(w=\sum_j\sigma_j\). Retain its literal crossing and closure
conventions. At every crossing the heads are
\[
 h_{\mathrm{over,in}}=u+v,\quad h_{\mathrm{over,out}}=v,\qquad
 h_{\mathrm{under,in}}=J,\quad h_{\mathrm{under,out}}=J+u.
 \tag{1}
\]
Degree-two closure vertices can be suppressed in this equation: their
equal heads, their original summed degrees, and their finite pivot
weights remain. The first cut degree is summed as in [R], not fixed.

Set \(U=u/N,V=v/N\), and likewise scale \(J\). Use the complete source
primitive \(G_\sigma\) and its branches from [L]. In local coordinate
order
\[
 \alpha=(U+V,J+U,V,J,U),\qquad
 \lambda_a=2\pi i\alpha_a,\quad z_a=e^{\lambda_a},\quad
 \mu_a=\Log(1-z_a),
 \tag{2}
\]
the logarithms start on the sine strip of [L] and then continue on the
same marked regular clock graph. In particular they are not reset to
principal values. The complete derivative table is
\[
\begin{array}{c|ccc}
 &G_U&G_V&G_J\\ \hline
 +&
 \mu_1+\mu_2-\mu_5&
 \lambda_4+\mu_1-\mu_3-\pi i&
 \lambda_3+\mu_2-\mu_4-\pi i\\
 -&
 -\lambda_1-\lambda_4+\mu_1+\mu_2-\mu_5+\pi i&
 -\lambda_2+\mu_1-\mu_3+\pi i&
 -\lambda_1+\mu_2-\mu_4+\pi i .
\end{array}
\tag{3}
\]

Write the coupon regions in literal order \((W,S,N,E)\), with \(S\)
between the two inputs and \(N\) between the outputs. If
\(\rho_f=2\pi i y_f\) are the region potentials of [R], then
\[
\begin{array}{c|ccc}
 &U&V&J\\ \hline
 +&y_W+y_E-y_S-y_N&y_N-y_E&y_S-y_E\\
 -&y_S+y_N-y_W-y_E&y_W-y_N&y_W-y_S .
\end{array}
\tag{4}
\]
These are occurrence formulas even when region labels repeat. The
integral region lattice modulo constants is the actual physical flow
lattice. Its character is therefore a tuple
\(\xi=(\xi_f)\in\mathbb Z^{c+2}\) with \(\sum_f\xi_f=0\), and its
stationary rows are
\[
 \partial_{y_f}\sum_jG_{\sigma_j}=2\pi i\xi_f.
 \tag{5}
\]
The finite capacities, clock endpoints, pivots, and the original mark
are retained by [R,L]; (5) describes their leading logarithmic rows.

## 2. The actual cells and all local edge logs

Use the ordered cells
\[
 0123,\quad0134,\quad0142,\quad2315,\quad2350.
 \tag{6}
\]
At a positive crossing their vertices are
\((s_0,s_P,p,a^{-1}p,c,a)\). Their literal shape dictionary is
\[
\begin{array}{c|c|c}
 \sigma&\zeta=(\Log r_0,\ldots,\Log r_4)&
               \nu=(\Log(1-r_0),\ldots,\Log(1-r_4))\\ \hline
 +&(\lambda_5,\lambda_4,-\lambda_2,\lambda_3,-\lambda_1)&
 (\mu_5,\mu_4,\mu_2-\lambda_2+\pi i,\mu_3,
                         \mu_1-\lambda_1+\pi i)\\
 -&(\lambda_5,\lambda_4,-\lambda_2,-\lambda_1,\lambda_3)&
 (\mu_5,\mu_4,\mu_2-\lambda_2+\pi i,
                         \mu_1-\lambda_1+\pi i,\mu_3).
\end{array}
\tag{7}
\]
The negative row is the reversed marked block with its auxiliary
vertices \(2,3\) exchanged. The positive row uses the literal assignment
\((A,B,C)=(z_1,z_4,z_5)\); the negative uses
\((A,B,C)=(z_4,z_1,z_5)\). The scalar symmetry \(J\leftrightarrow V\)
cannot be used while leaving the original ports fixed.

For each ordered tetrahedron assign the triad
\((\zeta,-\nu,\nu-\zeta+\pi i)\) to opposite edge pairs
\((01,23),(02,13),(03,12)\), respectively. Thus this is a specified
logarithmic lift with triad sum \(\pi i\). Let \(b_{ab}\) be the sum
at an octahedron boundary edge. Direct incidence in (6) gives
\[
\begin{array}{c|l@{\qquad}c|l}
02&-\nu_0+\nu_2+\nu_4-\zeta_2-\zeta_4+2\pi i&
03&\nu_0-\zeta_0-\nu_1-\nu_4+\pi i\\
12&\nu_0-\zeta_0-\nu_2-\nu_3+\pi i&
13&-\nu_0+\nu_1+\nu_3-\zeta_1-\zeta_3+2\pi i\\
04&\nu_1-\zeta_1-\nu_2+\pi i&
14&-\nu_1+\nu_2-\zeta_2+\pi i\\
25&\nu_3-\zeta_3-\nu_4+\pi i&
35&-\nu_3+\nu_4-\zeta_4+\pi i\\
05&\zeta_4&15&\zeta_3\\
24&\zeta_2&34&\zeta_1 .
\end{array}
\tag{8}
\]
The two internal edges have logs
\[
 I_{01}=\zeta_0+\zeta_1+\zeta_2=0,\qquad
 I_{23}=\zeta_0+\zeta_3+\zeta_4=0.
 \tag{9}
\]
These are exactly the two local monomial relations from (2), with no
division. Their zero lift is part of the source convention. It is not
a positive angle sum or an assertion about the shifted finite charges.

In both signs (8)--(9) imply
\[
 b_{04}+b_{14}=\lambda_5+2\pi i,\qquad
 b_{25}+b_{35}=\lambda_5+2\pi i,\qquad
 b_{24}=-\lambda_2,\quad b_{34}=\lambda_4.
 \tag{10}
\]
At \(+\), \(b_{05}=-\lambda_1,b_{15}=\lambda_3\); at \(-\),
\(b_{15}=-\lambda_1,b_{05}=\lambda_3\). Thus these terms correspond
to the same actual heads in (1) for either sign.

## 3. Region edges, including the even correction

The \(P\)-to-\(S\) edges of [T] are the diagram regions. The local
region derivative rows, in order \((W,S,N,E)\), are
\[
\begin{array}{c|c|c}
 \sigma&\partial_\rho(2\pi iG_\sigma)&
                      \text{correction in units of }\pi i\\ \hline
 +&(b_{02}-4\pi i,\ b_{03}-\pi i,
                         b_{12}-\pi i,\ b_{13})&(4,1,1,0)\\
 -&(b_{03},\ b_{13}-3\pi i,
                         b_{02}-3\pi i,\ b_{12})&(0,3,3,0).
\end{array}
\tag{11}
\]
Here \(\partial_\rho(2\pi iG)=\partial_yG\), so no \(2\pi i\)
factor is lost. One verifies (11) by (3), (4), and (8).
For example the negative first entry is
\(-G_U+G_V+G_J=b_{03}\), and its next two are
\(G_U-G_J=b_{13}-3\pi i\), \(G_U-G_V=b_{02}-3\pi i\).

The negative edge order in (11) is also the actual geometric one.
Reverse the positive block: its region labels
\((0,M,P,R)\) become \((W,N,S,E)\). Exchange auxiliary vertices
\(2,3\). Its four corner edges then become
\((03,13,02,12)\) in order \((W,S,N,E)\), as displayed.
This avoids inferring a face map from the symmetry of the coefficient.

Let \(k_f\) be the sum of the integer corrections in (11) over all
occurrences of region \(f\). Then
\[
 k_f\in2\mathbb Z,\qquad
 H_{PS,f}=2\pi i\left(\xi_f+\frac{k_f}{2}\right),\qquad
 \sum_f\frac{k_f}{2}=3c.
 \tag{12}
\]
To prove the parity, traverse the closed boundary of the region,
counting repeated sides and corners as occurrences. Record whether the
directed strand agrees with this traversal on each side. That sign
changes precisely at an in--in or out--out corner, namely \(S,N\).
It changes an even number of times on a closed walk. These are exactly
the odd entries of both correction tables. Each crossing contributes
six to the sum of corrections. Summing (11) and using (5) proves (12).

Thus the actual integer region-edge winding is
\(\xi_f+k_f/2\), not \(\xi_f\) with its parity constants suppressed.

## 4. The two arc families and the remaining mismatch

Write \(AP\) for the knot-to-\(P\) edges: they correspond to Wirtinger
intervals cut at undercrossings. Write \(AS\) for the knot-to-\(S\)
edges, cut at overcrossings. This follows from the actual interval
disks of [T], including an interval containing no encounter of the
opposite type.

First impose literal head matching. For an \(AP\) interval \(\gamma\),
each over encounter contributes \(\lambda_U+2\pi i\) by (10).
Its under-output start contributes minus its head log, and its
under-input end contributes plus its head log. Along it
\(h_{\rm end}=h_{\rm start}-\sum_{\gamma,O}u\). Similarly an \(AS\)
interval has under contributions \(\lambda_U+2\pi i\), plus its
over-output start head and minus its over-input end head. Therefore
\[
 H_{AP,\gamma}=2\pi i\,n_O(\gamma),\qquad
 H_{AS,\gamma}=2\pi i\,n_U(\gamma),
 \tag{13}
\]
where \(n_O,n_U\) are the actual encounter counts. In particular neither
is asserted to be one. Their respective total windings are \(c,c\).
Together with (9) and (12), the total winding is \(5c\), consistent
with the triad sums of the \(5c\) cells. The two spherical ends are
retained; this is not an acute ideal triangulation.

The converse is integral. After (9), allow independent local log
coordinates \((\lambda_U,\lambda_V,\lambda_J)\) at each crossing.
For every directed knot segment \(e\) define
\[
 \delta_e=\lambda_{h,\mathrm{out}(e)}
                    -\lambda_{h,\mathrm{in}(e)}.
 \tag{14}
\]
Local conservation implies \(\sum_e\delta_e=0\). Equations (10) give,
without assuming the individual matches,
\[
\begin{split}
 H_{AP,\gamma}-2\pi i n_O(\gamma)&=-\sum_{e\subset\gamma}\delta_e,\\
 H_{AS,\gamma}-2\pi i n_U(\gamma)&=\phantom{-}\sum_{e\subset\gamma}\delta_e .
\end{split}
\tag{15}
\]
Consequently their simultaneous vanishing leaves exactly
\[
 \delta_e=k\left(\mathbf1_{\mathrm{next}(e)=O}
                       -\mathbf1_{\mathrm{previous}(e)=O}\right).
 \tag{16}
\]
Indeed integrate \(\delta\) once around the cyclic knot. Its primitive
is constant on all under encounters by the \(AP\) equations and on all
over encounters by the \(AS\) equations. Their difference is \(k\).
Conversely (16) telescopes on both sorts of interval.

This statement is over \(\mathbb Z\), not just over \(\mathbb C\).
For an explicit elimination, make the bipartite multigraph whose
vertices are the \(c\) \(AP\) intervals and \(c\) \(AS\) intervals,
and whose \(2c\) edges are the segments belonging to both. Consecutive
segments share one interval, so the graph is connected. It has one
cycle. The arc sums are its incidence rows, after reversing one
vertex type. Its unique integral cycle has coefficients given by
(16), with zero on the attached trees. Any \(U\)-to-\(O\) transition
edge belongs to that cycle and has coefficient \(1\).
Remove it. Leaf elimination on the resulting tree expresses every
\(\delta_e\) as an integer combination of the arc sums and that one
transition coordinate. There are no integer divisors. Thus
\[
 \{\text{internal rows},\ AP/AS\text{ rows},\ k=0\}
 \quad\Longleftrightarrow_{\mathbb Z}\quad
 \{\text{all source monomial and head-matching rows}\}.
 \tag{17}
\]
The symbol \(k\) off the arc constraint locus can be represented by
that transition coordinate; different choices differ by arc rows.

## 5. Index one and the complete marked stationary lattice

Let \(\mathscr L_{\rm src}\) be the primitive rank-\(5c\) lattice of
[L], in its \((\lambda,\mu)\) row coordinates. Let
\(\mathscr L_{\rm edge+\!k}\) be generated by the literal edge rows
(8)--(9) after global face assembly, together with the transition row
in (17). Constants are temporarily omitted when naming a row lattice.
Then the affine coordinate change (7) gives
\[
 \boxed{\ \mathscr L_{\rm edge+\!k}=\mathscr L_{\rm src}
                 \quad\text{over }\mathbb Z.\ }
 \tag{18}
\]

Here are the integral steps. The two internal equations eliminate
two shape variables at every crossing with coefficients \(1\).
The remaining head-match equations generate the full annihilator of
the physical embedding. One can also see their saturation directly:
the local four-head conservation lattices have coordinates \((u,v,J)\);
the map to mismatches has image
\(\{(\delta_e)\in\mathbb Z^{2c}:\sum_e\delta_e=0\}\).
To solve for heads with any such mismatch, first choose outgoing
segment heads. The local conservation equations become a graph
divergence problem with total right side zero, which is solved
integrally along a spanning tree of the connected diagram. Its kernel
is exactly the physical flow lattice of [R]. Thus the head rows give
its integral annihilator. Equation (17) identifies this lattice with
the internal, arc, and \(k\) rows without saturation.

Modulo these monomial rows, (11) identifies every \(PS\) edge row
with the corresponding region stationary row. Conversely these are
all stationary rows because the integral region map in [R] is an
isomorphism modulo constants. This proves (18) in both directions.

For clarity, inversion in (7) acts by
\((\lambda,\mu)\mapsto(-\lambda,\mu-\lambda+\pi i)\). Its linear
part is unimodular. The sum of the ordinary five-cell shape forms
pulls back to minus the signed form \(E\) of [L]. Hence its global
sign does not change isotropy or saturation. Equation (18) is an
index-one equality of primitive Lagrangian lattices, not a claim
obtained by passing to their rational spans or their \(2\)-saturations.

Restoring all constants, the source stationary system is exactly the
edge system with
\[
 I_{01}=I_{23}=0,\quad
 H_{AP}=2\pi i n_O,\quad H_{AS}=2\pi i n_U,\quad
 H_{PS,f}=2\pi i(\xi_f+k_f/2),\quad k=0 .
 \tag{19}
\]
This specifies a particular marked lift. Arbitrary integer edge
windings are not identified with arbitrary finite carries.

## 6. The geometric meridian and its separate eigenvalue sign

We identify the primitive residual coordinate with the actual cusp,
not merely with a missing row count. Work on a regular marked geometric
chart of the assembly in [T], and choose the same eigenflag at every
knot-vertex occurrence. Let the eigenvalue of its actual oriented
meridian on that flag be \(m\). This auxiliary uniform-flag calculation
identifies geometric holonomy; it does not identify an off-complete
quantum state.

The free \(P,S\) vertices admit equivariant vector decorations; their
stabilizers are trivial. Equivalently develop their spherical links
and fix their vectors once. Thus the region determinants
\(w_f=\det(p,s_f)\) have the actual globally consistent region labels.
Use the original marked \(\mathrm{SL}_2\) lift near the complete chart.
At a positive crossing,
\[
 s_M=a s_0,\qquad s_P=c s_0,\qquad s_R=a s_P .
 \tag{20}
\]
Normalize the over flag to infinity, \(p=0,a^{-1}p=-1\). Then
\[
 a(z)=m^2(z+1),\quad
 a=\begin{pmatrix}m&m\\0&m^{-1}\end{pmatrix},\quad
 s_0=\alpha(S,1)^t,\quad s_P=\beta(T,1)^t .
 \tag{21}
\]
In the over cusp coordinate the ratio of its two input edge vectors is
\(S/(S+1)\), and the output ratio is \(T/(T+1)\).
These are the over-head monomials from (7)--(10). They equal
\[
 r_{O,\mathrm{in}}=m\,w_0/w_M,\qquad
 r_{O,\mathrm{out}}=m\,w_P/w_R .
 \tag{22}
\]

Let \(C\) be the under fixed point and use its cusp coordinate
\(z\mapsto1/(z-C)\). Since \(c(C,1)^t=m(C,1)^t\),
determinant preservation in \(c s_0=s_P\) gives
\[
 \beta(T-C)=m^{-1}\alpha(S-C).
 \tag{23}
\]
The under input/output edge-vector ratios are respectively
\[
 \frac{S+1}{T+1}\frac{T-C}{S-C},\qquad
 \frac S T\frac{T-C}{S-C}.
\]
They therefore give
\[
 r_{U,\mathrm{in}}=m^{-1}w_M/w_R,\qquad
 r_{U,\mathrm{out}}=m^{-1}w_0/w_P .
 \tag{24}
\]
These are actual cusp edge-vector ratios, so their transport uses the
individual face maps of [T].

For the negative block the reversed region order is
\((0,M,P,R)=(W,N,S,E)\), and \(2,3\) are exchanged. The over input
and output become \(T/(T+1)\), \(S/(S+1)\); the under input and
output become the second and first ratios above. Thus in both signs,
in the directed region convention of [R],
\[
 r_O=m\,w_{\rm left}/w_{\rm right},\qquad
 r_U=m^{-1}w_{\rm left}/w_{\rm right}.
 \tag{25}
\]
On a shared segment the region ratio agrees at its two ends.
Its mismatch is consequently
\[
 \delta_e=-2\Log m\,
  (\mathbf1_{\mathrm{next}=O}-\mathbf1_{\mathrm{previous}=O}),
 \qquad k=-2\Log m.
 \tag{26}
\]
The logarithms in this calculation continue from the complete marked
lift, where the source has \(k=0\). This fixes the additive integer
carry in (26); resetting either logarithm would lose that datum.

The meridional transition in [T] is one actual meridian, not a power.
The selected source cut flag has eigenvalue \(m=M^{-1}\) by [P].
Hence
\[
 k=2\Log M=\Log(M^2).
 \tag{27}
\]
The uniform cut flag has the inverse squared multiplier; the marked
\(M\)-flag convention of [P] gives (27). The equation \(k=0\) is
the complete *full* meridian row. The choice \(M=1\), rather than the
other lift of \(M^2=1\), is supplied by the original marked
\(\mathrm{SL}_2\) source. It is not an additional division within the
integer row lattice (18).

This marking argument is deliberately separate from a generic-meridian
source comparison. The archived generic crossing certificate retains
different over/under eigenflags and its nonzero correction away from
completeness. Equations (20)--(27) do not discard that correction or
identify the original generic ADO family with this uniform-flag chart.

## 7. The original longitude, including its writhe

Use the exact peripheral insertion and its marking from [P]. At the
complete color \(x=-1\), take its prescribed \(\Log x=\pi i\).
Its local factors are
\[
 t_+=\frac{BC}{x}\frac{1-1/A}{1-C/A},\qquad
 t_-=\frac{x}{A}\frac{1-1/B}{1-C/B},\qquad
 \ell_{\rm intr}=x^{-w}\prod_j t_{\sigma_j}^{-1}.
 \tag{28}
\]
Substitute the literal assignments following (7), and use
\(\Log(1-z_a^{-1})=\mu_a-\lambda_a+\pi i\) on the specified lift.
The entire logarithmic calculation is
\[
\begin{split}
 \Log t_+&=\mu_1-\mu_3+\lambda_4-\pi i=G_{V,+},\\
 \Log t_-&=\mu_1-\mu_3-\lambda_2+\pi i=G_{V,-}.
\end{split}
\tag{29}
\]
Thus no transfer \(U\), integer carry, or local sign is suppressed:
\[
 \boxed{\ \Log\ell_{\rm intr}=-\sum_jG_{V,j}-\pi i w.\ }
 \tag{30}
\]
The original cut carries the inverse longitude eigenvalue. The full
geometric peripheral convention of [P] is
\((M^2,\ell_{\rm intr}^2)\), so its longitude row is twice (30).
In particular a complete eigenvalue \(\ell_{\rm intr}=-1\) is not
silently replaced by \(+1\).

There is an integral-coordinate check on (30). After the arc rows,
replace every local \(V\) by \(V-k/(2\pi i)\), leaving \(U,J\)
fixed. This changes the over heads only and realizes exactly the
residual mismatch (16). Therefore, for
\(\mathcal S=2\pi i\sum_jG_{\sigma_j}\),
\[
 \partial_k\mathcal S=-\sum_jG_{V,j}.
 \tag{31}
\]
The writhe correction in (30) is the preferred-longitude correction
to that row. This calculation concerns the stated classical
coordinates; it is not a continuation of the original finite source
in a new independent meridian variable.

## 8. Scope and complete direct sources

The result identifies the actual complete source's primitive marked
stationary lattice with the edge lattice of its proved five-cell face
assembly, augmented by one primitive full-meridian row. It supplies
all local parity constants, the region and arc windings, and the
original peripheral conventions. It neither makes the five developed
cells positive nor removes the two framing directions or any
nonlinear degeneracy.

No finite quantum tensor, endpoint current, cyclic pole, normal jet,
or relative cycle is replaced. In particular the internal logarithms
in (9) are not substituted for the shifted finite factorial charges.
No source-free Pachner move, source-independent generic flattening,
geometric coefficient, or noncancellation theorem follows.

All four complete direct texts were read at the versions below.
The proof uses written mathematics only.

| Label | Source | SHA-256 |
|---|---|---|
| T | [Actual crossing-tunnel face assembly](research_crossing_tunnel_shadow_cellulation.md) | e836e8f4bb4fc0c67eeee286d3ad39e372546b369517ef903df8806551841154 |
| R | [Original region logarithmic rows](research_physical_region_logarithmic_assembly.md) | efebbe8bd0e59beac8c6803117e7979177f73638005aa695efd0be08e4e01147 |
| L | [Primitive reduced source lattice](research_reduced_physical_marked_logarithmic_lattice.md) | f0c2d09d9f36b176a0a593db9723db55325737a39d9bfebc087583a875cffa79 |
| P | [Original longitude and regulator action](quantum_longitude_and_regulator_action.md) | e8ac5dc6bab05be0dad3810311dc3a8b169ad810b898aa3db75582087dbe8aa7 |
