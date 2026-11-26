# The braid cut, the literal empty cap, and global nine-cell sewing

Private written proof, 17 November 2026. Starting with a supplied braid
presentation of a knot, we assemble the literal charged tetrahedral
sources into a closed triangulated pair. Its normalized source is the
original fixed-zero planar source times a specified scalar of modulus
one on injective real decorations. All vertex measures, wire clocks,
sector phases, and the actual empty closing ball remain in the formula.
No state-invariance theorem or printed nine-cell comparison is used.

## 1. The planar source and its open diagonal

Fix odd \(N>2\), \(q=\exp(2\pi i/N)\), \(d=N-1\), and
\(\epsilon=1/2\in\mathbb Z/N\). Let a braid on \(b\ge2\) strands have
one-component closure and \(c>0\) crossings. Draw its strands upward
in a rectangle, and its disjoint nested closing arcs on the right.
Cut the outermost closing arc, on strand 1. The two free ends are on
the unbounded face. A crossing has four distinct *corner occurrences*,
even when some of its regions coincide.

For an admissible sector assignment \(\chi\), let
\[
 O_\chi(i,j)=\sum_{\text{internal colors}}
       \prod_v R_v(\,\cdot\mid\chi_v)
       \prod_{e\text{ internal}}q^{j_e}.                       \tag{1}
\]
Here \(R\) is exactly [K,(2.7),(2.8)]. The two end-edge factors are
omitted in (1). Admissibility means that every crossing and bounded
face has charge sum 1, and every unbounded-face corner has charge 0.
At \(i=j=0\), (1) is the original fixed-cut source [K,(3.6)].
The array \(F_\chi(i,j)\) of [G] includes both end factors, so
\(F_\chi(i,j)=q^{i+j}O_\chi(i,j)\); the two conventions will not
be interchanged in the cap contraction.

**Open diagonal identity.** For every such assignment,
\[
             O_\chi(i,j)=q^{-i}\delta_{ij}O_\chi(0,0).          \tag{2}
\]
This does not assert that the last scalar is nonzero.

We give the complete passage from the enhanced braid to (2).
Write \(R^o\) for [K,(2.12)] and \(B_+=P(R^o)^t\). By [P],
\[
 B_-=B_+^{-1},\qquad \mu=q^\epsilon S,\qquad
 S|j\rangle=|j+1\rangle,
\]
and the weighted partial trace of a one-component braid over strands
2 through \(b\) is a scalar operator. This follows there from the
explicit Fourier and diagonal comparison with the simple highest-weight
module, including all conjugations and the writhe phase; it is not an
invariance assertion imported from [K].

For precision the negative planar convention can also be checked
without assuming the printed inverse. Put
\(p_r=\prod_{t=1}^r(1-q^t)\). The Fourier matrix \(A\) in [P,(1.1)]
has inverse
\[
 (A^{-1})_{a-k,b+k;a,b}
 =(-1)^kq^{-1-a(b+1)-ak+k(k+1)/2}
       \frac{p_a p_{b+k}}{p_{a-k}p_b p_k},                       \tag{3}
\]
with the same ordinary triangular index range. In the product \(AA^{-1}\),
the entry of total displacement \(r>0\), after its common nonzero
factor, is
\[
 \sum_{k=0}^r
 \frac{(-1)^kq^{k(k-1)/2+(1-r)k}}{p_kp_{r-k}}
       =\frac{(q^{1-r};q)_r}{p_r}=0.
\]
The diagonal is 1. Reflection \(j\mapsto d-j\) and
\(\overline p_k=(-1)^kq^{-k(k+1)/2}p_k\) give
\(A^{-1}=J_dP\overline A PJ_d\), with tensor factors understood.
Since \(B_+=\mathcal F^{-1}PA^t\mathcal F\),
\(\mathcal F=F\otimes F\), and
\(F^{-1}J_dF^{-1}=Z\), this is
\[
       B_-=(Z\otimes Z)\overline{B_+}(Z^{-1}\otimes Z^{-1}),
       \qquad Z|j\rangle=q^j|j\rangle.                         \tag{4}
\]
Substitution in [K,(2.8),(2.15)] shows that the printed negative
matrix is \(qB_-\). Thus no signed inverse phase is discarded.

At either signed braid crossing, put charge 1 in the south sector
(between its two inputs) and 0 in the other sectors. The matrix
\(B_+\) is that raw \(R\) times \(q^{\text{sum of output colors}}\).
For \(B_-\) there is additionally \(q^{-1}\). For example, positive
input/output labels \((a,b)\to(c,d')\) give cyclic planar labels
\((a,b,d',c)\); the negative crossing uses
\((b,d',c,a)\). These substitutions fix the overpassing pair and
the south sector, rather than reversing a corner by convention.

In each traced closing arc, \(\mu\) makes the next input color equal
to the previous output color plus 1 and contributes \(q^\epsilon\).
Use the output color as the color of the whole corresponding planar
edge. At each local port let \(x=1\) if it is the first crossing input
after one of the closing arcs \(2,\ldots,b\), and \(x=0\) otherwise.
The first cut has no shift. At a crossing replace its south-sector
assignment \(a^0\) by
\[
                  a^*_{(e,e')}=a^0_{(e,e')}-(x_{e'}-x_e).
                                                                    \tag{5}
\]
All four \(W\) arguments agree. The change in its explicit prefactor
is \(q^{-x_{\rm under,1}-x_{\rm under,2}}\).
Let \(U\) denote the sum of these local under-port shifts, and let
\(n_-\) count negative crossings. The unnormalized enhanced open
operator \(T\) therefore satisfies
\[
 T_{ij}=q^{\epsilon(b-1)-n_- -U}\,q^i O_{a^*}(i,j).           \tag{6}
\]
Every internal wire has exactly one output factor. The remaining
output factor is precisely \(q^i\) at the free output; neither end
has been given a new mark.

Here is the face check in (5). In the braid rectangle a crossing
terminates the gap below it and starts the gap above it. Every finite
gap region receives its one south-sector charge. Each of the \(b-1\)
initial gap regions also terminates once, while the terminal gap
regions have no south charge. Every adjacent braid generator must
occur: otherwise the closure permutation preserves a proper initial
set of strands and the closure is not one component. The nested
outside band \(R_j\), \(1\le j<b\), joins the initial and terminal
gap \(j\); initially its charge is 1. The innermost band \(R_b\),
touching the right exterior gap, initially has charge 0. The cut
merges \(R_1\) with the outside region \(R_0\).

The input shift from closing arc \(j\ge2\) transfers one charge from
the region on the left of that initial strand, \(R_{j-1}\), to the
one on its right, \(R_j\). This holds whether its first crossing
uses that strand as the left or right input: substitution in (5)
subtracts 1 from its left corner and adds 1 to its right corner.
Consequently every bounded region has total 1 and the outer region
has total 0. These statements count occurrences, so repeated boundary
walks cause no change.

Individual outer corners of \(a^*\) need not vanish. We compare it
directly with any admissible \(\chi\), whose existence is proved in
Section 2. The corner difference \(\delta=\chi-a^*\) has zero sum
at every crossing and around every bounded face. The expanded-circle
proof in [G, Section 2] therefore integrates it to edge potentials
\(z_e\): existence uses these bounded-face sums, not the individual
outer-corner condition. Explicitly, give the old edges increment zero
and the circle corners increment \(\delta\); the bounded-face
boundaries generate the integral cycle group, so path integration is
single-valued, including repeated edges and bridges.

On the old \(R_0\) side of the outermost cut, all corners of \(a^*\)
are individually zero. Indeed this is the outside of the outermost
closing arc, meeting only the left exterior gap and no shifted
closing input. The corners of \(\chi\) there are also zero. This
one boundary path from one free end to the other has increment zero,
so the two end potentials agree. Subtract their common value to
make both zero. Thus \(\delta=z_{e'}-z_e\) with the original end
colors fixed; no consistency of separately assigned repeated-edge
values is assumed.

The literal color substitution gives
\(O_\chi=q^{\Omega(z)}O_{a^*}\), where
\[
 \Omega(z)=\sum_{e\text{ internal}}z_e-
              \sum_v(z_{\rm under,1}+z_{\rm under,2}).          \tag{7}
\]
The scalarity of \(T\) in (6) proves (2), by evaluating the same
formula at \(i=j=0\). All phases are retained, even if this value is
zero. Explicitly, if \(w\) is the braid writhe and \(J_N\) is the
normalized enhanced period of [P], then
\[
 O_\chi(0,0)=q^\Gamma J_N,\qquad
 \Gamma=\Omega(z)-\epsilon(b-1)+n_-+U+\epsilon w.
                                                                    \tag{8}
\]
No assertion of independence from a new off-root lift is made.

## 2. A global integral sector assignment

There is an explicit level-independent 0/1 admissible assignment.
Checkerboard-color the regions of the closed shadow. Its black and
white Tait graphs are dual, have \(c\) edges, and their vertex counts
sum to \(c+2\). The cut edge is adjacent to one black and one white
root region. Choose a spanning tree \(T\) of the black graph.
Its complementary dual edges form a spanning tree \(T^*\) of the
white graph: a dual cycle would separate the primal tree, and the
edge count is exactly the number of dual vertices minus one.

For a crossing whose black edge is in \(T\), give charge 1 to the
black corner farther from the black root along \(T\). Otherwise
give charge 1 to the white corner farther from the white root in
\(T^*\). Give all other corners zero. Each crossing has exactly
one 1. Each nonroot region receives exactly one, at its parent
tree edge, and both roots receive zero. After cutting, those roots
form the outer region. A loop is never chosen as a tree edge;
the dual of a primal bridge is not in the complementary dual tree.
Thus the construction also covers repeated regions and multiple edges.
The selected child endpoint of a tree edge is a particular corner
occurrence, not a possibly repeated region name.

This proves the hypotheses used in Section 1 without solving a
level-dependent linear system. We use this \(\chi\) below.

## 3. The actual three-ball and one global vertex order

The closed shadow has a dual quadrilateral cellulation of \(S^2\),
with \(c\) cells, \(2c\) sides, and \(c+2\) region vertices.
Cut its side dual to the chosen knot edge. The result is a disk \(Q\)
with \(2c-1\) paired interior sides and two free boundary sides.
It has \(c\) interior region vertices and the two root vertices on
its boundary. This remains an incidence description when cell
boundaries repeat. The knot edge separates two distinct checkerboard
regions, so the cut is along an embedded side, not a loop in the
dual surface.

Suspend \(Q\) between poles \(\mathsf P,\mathsf S\). Each region
vertex sweeps an arc from \(\mathsf P\) to \(\mathsf S\), designated
as one edge; its midpoint is not an additional vertex of the chosen
cell structure. The suspension of a side is a bigon disk between
two such pole edges. Subdivide it by its material midpoint \(m\)
into the two triangles \(\mathsf Pm\mathsf S\).
The boundary of each suspended quadrilateral is consequently the
four paired port disks of the nine-cell ball [S]. Replace that ball
by its literal nine tetrahedra, preserving all eight individual
boundary triangles and their orders. This is a replacement of a
ball by a ball relative to its boundary. The assembled space is
the suspension of a disk, hence a three-ball. The description of a
region arc as one edge is only a choice of PL cell structure;
subdividing that arc recovers the usual suspension coordinates.

The nine-ball link edges \(13,24\) give exactly the two original
crossing strands with their overpassing data. For an explicit local
model place its central tetrahedral vertices at
\(1=(1,0,-t),2=(0,1,t),3=(-1,0,-t),4=(0,-1,t)\), \(t>0\).
Their oriented determinant is \(8t>0\); edge \(24\) is above edge
\(13\) in the planar projection. The other cells attach around this
central tetrahedron as in [S] and retain these two arcs and the
four cyclic boundary ports. Use the indicated individual boundary
triangles when identifying its ball with the suspended quadrilateral,
without adding a boundary twist. Side gluing gives
the original cut knot. Its remaining boundary is the four-triangle
sphere
\[
       \mathsf Pa\mathsf S^\pm,\qquad
       \mathsf Pb\mathsf S^\pm,                                 \tag{9}
\]
with two distinct \(\mathsf P\mathsf S\) edges and no boundary edge
\(ab\). Its four vertices are \(\mathsf P,\mathsf S,a,b\).

To meet the primary's actual total vertex order and injective
decoration requirement, insert the two-cell collar [I] on **every**
internal wire. Topologically, inflate the corresponding side of \(Q\)
to a bigon between parallel copies with the same two region endpoints.
This refines the same disk. Suspending that bigon is the collar ball:
its side midpoints are the two material vertices, and its core edge
subdivides the original strand. Thus no new region vertex or extra
pole detour is introduced. Every crossing port is a distinct global material
vertex. Order the poles first and last, and order the blocks in any
sequence, with the four material vertices inside each block in its
required cyclic order \(1<2<3<4\). This is one total order on all
vertices, not an arbitrary collection of local branchings.
Each collar uses the appropriate one of the two recipes [I,(2)],
so its order is also the restriction of this same global order.
Self-adjacent wires are handled in exactly this way: the two ports
of the same crossing remain distinct vertices connected by a collar.

Give \(h=1\) to incoming crossing ports and \(h=0\) to outgoing ports.
Each crossing has two of each, so \(\sum h_m=2\). On a wire the
charges are complementary; [I] supplies \(h=1\to0\) in either
order relative to its two material vertices. Its port ordering is
literal: at one end the positive/negative face labels are
\((\alpha,\alpha')\), and at the other they are \((B',B)\).
Thus its difference coordinates are
\(\alpha'-\alpha+h_L\) and \(B-B'+h_R\), as in [I,(14)].
They glue to the opposite ordered port of [S], not to an independently
chosen Fourier transform. All old side and region occurrences remain.

Choose distinct real numbers on all these global vertices, and choose
each odd root \(s_{uv}\) real, with \(s_{vu}=-s_{uv}\). Use positive
square roots of the real divided-difference brackets. Every local
tetrahedron has distinct vertices; all of its Fermat factors and
normalizations are regular. The real decoration need not be increasing
in the global vertex order. This is the common branch on which [C]
gives its exact modulus for every block.
For the closing calculation name the two free material vertices
\(a<b\) in this global order. If \(a\) is the input rather than the
output, the array in (13) is the transpose of (1). Identity (2)
is unchanged by this transpose, and its \(00\) value is unchanged.
Thus the cap below uses the same global total order, with no
unproved endpoint permutation.

## 4. The entire open tetrahedral source

Let \(C_v=C_N(\mathbf s_v)\) be exactly [C,(4)]. For the local sector
\(\chi_v=(x,y,\zeta,w)\), put
\[
 \phi_v=3(h_1-1)/2+d_{\chi_v}+\zeta+w,
\]
\[
 d_\chi=\zeta-2y+w/2-\tfrac32(\zeta+w)h_1
                     +\tfrac32y h_2-\tfrac32\zeta h_4.          \tag{10}
\]
The complete local identity [C,(38)] is
\[
 B_v=C_v q^{\phi_v}s_{\mathsf P\mathsf S}^{d}
      \sum_{i_1,\ldots,i_4}R_v(\mathbf i\mid\chi_v)
                          \prod_{m=1}^4\mathcal A_{v,m}(i_m).
                                                                    \tag{11}
\]
It includes the original six internal sums and all ordinary local
edge weights. The adapter is
\[
 \mathcal A_h(i)=q^{ik}f(k),\qquad
 k=\alpha_- -\alpha_+ +h,\qquad
 f(k)=s_{\mathsf Pm}^{[k-1]}s_{m\mathsf S}^{[-k]}.              \tag{12}
\]
The bar on an opposite tetrahedron denotes its literal dual tensor,
never a Hermitian adjoint.

One oppositely ordered port identification has raw pairing
\(N^2(s_{\mathsf Pm}s_{m\mathsf S})^d Z\). Its two new ordinary
edges contribute the inverse decoration power, and its one newly
interior material vertex contributes \(N^{-1}\). The normalized
joining tensor is therefore \(S=NZ\). The collar has tensor
\(K=Z^{-1}/N\), and \(SKS=S\), with no phase [I,(16)--(20)].
It commutes with the literal \(E_{00}\) cut. Thus inserting the
collars changes neither the physical wire nor its original pointing.

There are \(2c-1\) effective internal wires. There are exactly \(c\)
interior region edges \(\mathsf P\mathsf S\), each ordinary because
its sector charges sum to 1. Their weights cancel the \(c\) factors
\(s_{\mathsf P\mathsf S}^d\) in (11), even though the edges have the
same endpoints. Hence the actual open source is
\[
 \boxed{\quad
 B_Q=K_{\rm open}\sum_{i,j}O_\chi(i,j)\,
                    \mathcal A_a(i)\mathcal A_b(j),\qquad
 K_{\rm open}=N^{2c-1}\prod_v C_v q^{\phi_v}.
 \quad}                                                        \tag{13}
\]
On the common real branch,
\[
                            |K_{\rm open}|=N^{-1}.              \tag{14}
\]
This is a boundary tensor identity, not a count substituted for a
contraction. With collars expanded there are \(4c-2\) actual joins
and \(2c-1\) collar tensors; their product is exactly the same
\(N^{2c-1}\) and the same original wire clocks. Every tetrahedron,
edge, vertex and face sum has been included.

## 5. The literal empty cap and its Hamiltonian route

Fill (9) with two oppositely oriented tetrahedra
\((0,a,b,5)=(\mathsf P,a,b,\mathsf S)\), glued across
\(0ab\) and \(ab5\), namely faces 3 and 0. Their sole interior edge
is \(ab\); the remaining faces are the two copies of \(0a5\) and
\(0b5\). Declare \(ab\) ordinary. Close the material knot along the
boundary path
\[
                             a-0-5-b,                           \tag{15}
\]
using one of the two distinct \(05\) edges. This simple boundary
path is pushed into the cap ball and is boundary-parallel there.
The cap and open source have the same four boundary triangles,
four pole-to-material edges and two \(05\) edges. Their individual
face matching is a homeomorphism of the boundary spheres. Its
radial extension identifies the two-ball union with \(S^3\).
The remaining tangle meets that sphere only at \(a,b\); the
simple arc (15), pushed into a collar, is the usual boundary-parallel
closing arc up to isotopy relative to that tangle. Thus the pair is the
original knot in \(S^3\). It visits both poles once, and every
material vertex now has exactly two incident link edges.

Let \(h_a+h_b=1\) be the two incoming open port charges. In the
opposite-pair convention \(0a|b5,0b|a5,05|ab\), choose cap triples
\[
 (\lambda,\epsilon-\lambda,0),\qquad
 (-h_b-\lambda,h_b-\epsilon+\lambda,1).                         \tag{16}
\]
Each sums to \(\epsilon\). Together with the old port charges,
the totals on \(0a,b5\) are 0, and those on \(0b,a5\) are 1.
The selected \(05\) edge has total 0, the other total 1, and the
interior \(ab\) has total 1. Thus (15) is the actual admissible
Hamiltonian route. We henceforth take \(\lambda=-h_b\).

We compute the cap instead of replacing it by \(E_{00}\). Write
\(X=s_{05}s_{ab}\), \(Y=s_{0a}s_{b5}\), \(Z=s_{0b}s_{a5}\),
so \(X^N+Y^N=Z^N\). The literal kernels [S,(3)] give
\[
 \sum_{x,y}T(\lambda,0)_{xB}^{Ay}
       \bar T(-h_b-\lambda,1)_{A'y}^{xB'}
  =X^d q^{3(h_b+\lambda)/2}
      \delta_{A'-A,h_b}\delta_{B'-B,h_b}.                       \tag{17}
\]
Here is an endpoint-inclusive proof. The two conservation deltas
give \(\Delta=A'-A=B'-B\). Put \(n=A-\lambda-x\) and
\(L=\Delta-h_b\). The remaining phase is
\(q^{n+\Delta+\lambda+(h_b+\lambda)/2}\), and its ratio is
\(W(n)/\bar W(n+L)\), with Fermat triple \((X,Y,Z)\).
For \(1\le L<N\),
\[
 \frac{W(n)}{\bar W(n+L)}
   =(Z-X)Y^{-L}\prod_{j=1}^{L-1}(Z-Xq^{n+j}).
\]
After multiplication by \(q^n\), all its frequencies are between
1 and \(N-1\), so its cyclic sum is zero. For \(L=0\),
\[
 \sum_n q^n\frac{W(n)}{\bar W(n)}
       =\frac{N X^d(Z-X)}{Y^N}.
\]
This follows by completing \(1/(Z-Xq^n)\) to the full cyclic
product. Multiplication by the independently proved
\(\rho\bar\rho=Y^N/[N(Z-X)]\) gives (17), including the
case \(L=0\) and every cyclic carry.

The face orders in this gluing are also fixed. On the source side
they give \(k_a=A'-A+h_a=1\), and
\(k_b=B-B'+h_b=0\). Hence its physical row is proportional to
\(q^i f_a(1)f_b(0)\), where
\[
                    f_a(1)=s_{a5}^d,\qquad f_b(0)=s_{0b}^d.
\]
The two unconstrained common indices \(A,B\) supply \(N^2\).
The cap's new ordinary edge weights are precisely those of
\(ab,a5,0b\) and the ordinary \(05\) copy; they cancel
\(X^d f_a(1)f_b(0)\). All **four** vertices \(0,5,a,b\) of the
open boundary now become interior, contributing \(N^{-4}\).
Thus the normalized cap row, for the source convention [K,(4.19)], is
\[
                      N^{-2}q^{3(h_b+\lambda)/2}q^i
                              =N^{-2}q^i.                       \tag{18}
\]
It is not a local \(E_{00}\) tensor and is not asserted equal to
one on arbitrary exterior states. Its action on this whole open
source is determined by (2).

## 6. Exact closed comparison and its scope

Let \(Z_{\rm lit}\) be the literal closed source with its factor
\(N^{-\#\mathrm{vertices}}\), as in [K,(4.19)]. Equations
(2),(13),(18) give
\[
 Z_{\rm lit}
   =N^{-2}K_{\rm open}\sum_{i,j}q^iO_\chi(i,j)
   =N^{-1}K_{\rm open}O_\chi(0,0).                              \tag{19}
\]
The primary's closed normalization is \(N^2Z_{\rm lit}\).
Consequently the full exact formula is
\[
 \boxed{\quad
 N^2 Z_{\rm lit}
    =\left(\prod_{v=1}^c N^2 C_N(\mathbf s_v)q^{\phi_v}\right)
                         O_\chi(0,0).
 \quad}                                                        \tag{20}
\]
Every phase in (20) is specified by (4) of [C] and (10) above.
For distinct real decorations the multiplier has modulus exactly 1.
Together with (8), this also gives the normalized enhanced period
with its recorded root phase, rather than an unidentified scalar.
The equality holds even at a level where that period vanishes.

The construction uses a supplied one-component braid presentation;
it makes no separate claim about transporting the sector adapter
through every arbitrary Morse presentation. Repeated face occurrences
are retained explicitly. If the primary notation identifies sectors
merely by the pair \((v,f)\), its literal applicability is restricted
to diagrams without such repetitions; our finite source specifies the
corner extension throughout, with the same proved local tensors.

The proof assigns the actual link, charges, total vertex order,
injective decorations, and fixed cut. It is not an invariance theorem
for all triangulations, a positive geometric development, an off-root
meridian family, or a transport of a selected integration cycle.
In particular it supplies no nonvanishing or volume lower bound.

## Complete direct sources

- [K] Kashaev, *A Link Invariant from Quantum Dilogarithm*,
  q-alg/9504020v1, complete primary definitions.
  Local PDF: research_archive/finite-source-identification-2026-11-01/md-kashaev-normalization-critical-audit/kashaev1995.pdf.
  SHA256 0baef40fa9934c9119af2c67252f8032e288c884da72eeaecf405bf91569cda9.
- [P] [Specified crossing and period pairing](kashaev_crossing_and_period_lattice.md).
  SHA256 71e67223742fe905af47d0475435f3a13acc877695bd0cdc321798cf2e608037.
- [G] [Planar sector gauge and open cut](research_planar_sector_gauge_and_open_cut.md).
  SHA256 d7bd5537da441891b5eea4c2e1f341d4c7e46799649b4c279fffed14a468d163.
- [C] [Exact nine-cell crossing evaluation](research_nine_cell_canonical_crossing_evaluation.md).
  SHA256 332062e67d64ab4a0767637c0fdd96f186d62c430ad38042aef35ad857d8d7c9.
- [S] [Literal nine-cell boundary source](research_nine_tetrahedron_boundary_source_reduction.md).
  SHA256 5aeecb0c174f33baa1264bc34c7419d4ccae007e84f4410b3dcb47c6c81c554c.
- [B] [Literal charged tetrahedron bubble](research_literal_charged_tetrahedron_bubble.md).
  SHA256 1dfe35f26137572235b1c3af66dcf410e0af758836baddaa8dd6d958c0f61d9b.
- [A] [Paired-face boundary adapter](research_kashaev_paired_face_boundary_adapter.md).
  SHA256 c430fd2714acdc7588003e1c18c60453e1ebe123bd7c0155d20a0eef639ec8ed.
- [I] [Literal Hamiltonian wire subdivision](research_literal_hamiltonian_wire_subdivision.md).
  SHA256 73e0f2f1804f47cf9d9273733b0596ffc4784d7596b645ce7e14427eebe13853.

The entire direct texts were read and the used implications checked.
No mathematical program, numerical experiment, or printed global
state-invariance assertion was used.
