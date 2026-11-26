# Actual region coordinates and the global marked source equations

Private written proof, 17 November 2026. This gives the integral planar
region presentation of the **reduced original physical source**, including
both crossing signs, its summed first cut, and every logarithmic parity
constant. Integral flow--face duality is already covered by [M, Section 7].
The additional calculation here is the literal signed crossing dictionary
and its global source-row assembly. No simplicial sewing of octahedra or
triangulation edge interpretation is assumed.

## 1. The actual mark does not fix the first color

At the complete root let \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\),
\(Q=q^2\), \(x=-q^{-1}\), \(\eta=q^{-d^2}\), and let \(W\) be the original complete signed braid word
on \(b\) heads. The precise scalar used by the singleton compiler is

\[
K_N=\frac{\chi_N}{N}
 \operatorname{Tr}[(I\otimes g^{\otimes(b-1)})W],
\qquad g_a=\eta Q^{-a}.
\tag{1}
\]

This is [C, (1)]. Every crossing preserves total integer head degree,
so tracing the other heads makes the first-head partial matrix diagonal.
On that already assembled matrix the original averaged marked row has
the same scalar pairing as \(I/N\). This proves (1) without changing
the mark on individual sectors or on an inserted current.

Consequently **all** closing colors \(a_1,\ldots,a_b\) are summed.
The first has no pivot phase; the others retain \(Q^{-a_i}\) and
\(\eta\). In the full clock exponent this is the term
\(-2\sum_{i>1}a_i\). The factor \(\chi_N/N\) and every crossing
Cartan/framing scalar remain. A fixed-first-color matrix coefficient
would have a different index domain; it is not substituted for (1).

## 2. Integral region potentials for the literal physical indices

Form the plane directed physical wire graph \(D\) of the closed braid.
Its crossing vertices have two incoming and two outgoing edges. Retain
degree-two closure vertices until their equality of transmitted colors
has been imposed, and then suppress them. Use one dummy degree-two
vertex on a crossing-free circle if necessary. Loops, repeated face
occurrences and disconnected projection components are allowed.

At a crossing the compiler's ports carry

\[
\text{over-in}=u+v,\quad \text{over-out}=v,\qquad
\text{under-in}=J,\quad \text{under-out}=J+u.
\tag{2}
\]

Thus conservation is literal integer divergence zero. Conversely an
integer divergence-free edge assignment determines
\(u=\text{over-in}-\text{over-out}\),
\(v=\text{over-out}\), and \(J=\text{under-in}\), as well as every
closure color. This identifies the homogeneous physical lattice
\(\Lambda=\ker_{\mathbb Z}\partial_D\), using the same indices as [L].

Let \(\mathcal F\) be the complementary faces on the sphere. Give each
face an integer potential \(p_f\). Fix the orientation convention

\[
\text{head on a directed edge }e=p_{\mathrm{left}(e)}
                                      -p_{\mathrm{right}(e)}.
\tag{3}
\]

Then, integrally and with no index or parity loss,

\[
\mathbb Z^{\mathcal F}/\mathbb Z\mathbf1
       \ \cong\ \ker_{\mathbb Z}\partial_D.
\tag{4}
\]

Here is a proof that also covers loops and disconnected graphs. Face
differences telescope around every vertex, so give a circulation.
Conversely orient each edge according to the sign of an integral
circulation and use its absolute value as a multiplicity. At every
vertex the resulting incoming and outgoing multiplicities balance.
Successively following a nonzero edge therefore decomposes the flow
into directed cycles; splitting at repeated vertices makes them simple
embedded cycles, including embedded loop edges. Each simple cycle is
the oriented boundary of its disk in the sphere, and hence the face
difference of the indicator of that disk, with the appropriate sign.
Their sum is an integral potential. Finally the dual adjacency graph
of the faces is connected: a path between interior points of any two
faces can cross finitely many edge interiors and avoid the vertices.
Thus the kernel of (3) consists exactly of constant potentials.

If \(D\) has \(c\) crossing vertices and \(k\) connected components,
Euler's formula, including the dummy degree-two vertices, gives

\[
\operatorname{rank}\ker\partial_D=c+k=|\mathcal F|-1.
\tag{5}
\]

In particular a connected diagram has \(c+1\) independent potentials.
Fixing one face potential to zero chooses a primitive integral basis.
The actual finite index set is exactly the subset of these integer
potentials for which every head lies in \([0,d]\) and every transfer
\(u\) in (2) is nonnegative. These inequalities, not just conservation
modulo \(N\), are retained. They can force additional support faces;
(5) does not assert that the finite feasible set has full affine span
or that there is a global real interior point. No independent reduction
of the potentials modulo \(N\) is made in (4).

Crossing-free components retain their original finite closing factors.
Their potential directions are present in (4), while the crossing
action below is constant in those directions. Those factors may vanish.

## 3. The literal signed local dictionary

Draw a crossing coupon with inputs below and outputs above, as in the
original ordered matrix. Denote its four regions by \(W,S,N,E\): west,
south between the inputs, north between the outputs, and east. Draw
the directed wires upwards. Equation (3) then says

\[
a=p_W-p_S,\quad b=p_S-p_E,\qquad
c=p_W-p_N,\quad d'=p_N-p_E,
\tag{6}
\]

where \((a,b)\) are the left/right inputs and \((c,d')\) the
left/right outputs. The local symbol \(d'\) is a head, not \(N-1\).
Each equation is an occurrence equation if some region labels coincide.

The original signed port table [S, Section 1] has over pair \((0,7)\)
for \(+\) and \((1,6)\) for \(-\). Therefore the actual assignments are

\[
\begin{array}{c|cc|cc}
\sigma&a&b&c&d'\\\hline
+&u+v&J&J+u&v\\
-&J&u+v&v&J+u.
\end{array}
\tag{7}
\]

Although the complete scalar crossing coefficient is symmetric in
\(J,v\), using that symmetry without changing the ports would change
the dictionary. Equation (7) fixes the literal one.

Write \(y_f=p_f/N\). In region order \((W,S,N,E)\), the matrices
which send a region tangent to \((\dot U,\dot V,\dot J)\) are

\[
D_+=\begin{pmatrix}1&0&0\\-1&0&1\\-1&1&0\\1&-1&-1\end{pmatrix},
\qquad
D_-=\begin{pmatrix}-1&1&1\\1&0&-1\\1&-1&0\\-1&0&0\end{pmatrix}.
\tag{8}
\]

For example \(+\) gives
\(U=y_W+y_E-y_S-y_N,V=y_N-y_E,J=y_S-y_E\), while \(-\) gives
\(U=y_S+y_N-y_W-y_E,V=y_W-y_N,J=y_W-y_S\).
These follow by solving (6)--(7), with no branch choices or halves.

## 4. Both logarithmic row tables, including constants

Use the five source arguments and lifted logarithms of [L]:

\[
\alpha=(U+V,J+U,V,J,U),\quad
\lambda_a=2\pi i\alpha_a,\quad
\mu_a=\Log(1-e^{\lambda_a}).
\tag{9}
\]

They start with the canonical sine branches and continue on the same
marked regular clock graph. In particular \(\lambda\) is unwrapped.
Let \(G_\sigma\) be the calibrated physical action in [L, (2)].
The region derivatives have the form

\[
\partial_{y_f}G_\sigma
    =a_{\sigma,f}\lambda+b_{\sigma,f}\mu+\pi i n_{\sigma,f}.
\tag{10}
\]

Here are all rows, in the five-column order (9):

| Sign | Region | \(a_{\sigma,f}\) | \(b_{\sigma,f}\) | \(n_{\sigma,f}\) |
| --- | --- | --- | --- | --- |
| + | W | \((0,0,0,0,0)\) | \((1,1,0,0,-1)\) | 0 |
| + | S | \((0,0,1,0,0)\) | \((-1,0,0,-1,1)\) | -1 |
| + | N | \((0,0,0,1,0)\) | \((0,-1,-1,0,1)\) | -1 |
| + | E | \((0,0,-1,-1,0)\) | \((0,0,1,1,-1)\) | 2 |
| - | W | \((0,-1,0,1,0)\) | \((0,0,-1,-1,1)\) | 1 |
| - | S | \((0,0,0,-1,0)\) | \((1,0,0,1,-1)\) | 0 |
| - | N | \((-1,1,0,-1,0)\) | \((0,1,1,0,-1)\) | 0 |
| - | E | \((1,0,0,1,0)\) | \((-1,-1,0,0,1)\) | -1 |

To verify the table directly, [L, (7)] gives the column of physical
derivatives \(A_\sigma\lambda+B_0\mu+\pi i\nu_\sigma\). Multiplying
by (8) gives exactly (10). In particular the constant columns are
\((0,-1,-1,2)\) and \((1,0,0,-1)\). The sum of the four rows is
zero, including its logarithmic and constant parts. This is the common
face-potential invariance, not a dropped equation.

Equivalently put \(\rho_f=2\pi i y_f\) and \(\mathscr S=2\pi i G\).
Then (10) is \(\partial_{\rho_f}\mathscr S\). This convention prevents
an extra \(2\pi i\) when comparing with holonomy logarithms.

## 5. Exact integral assembly and the marked residual character

At each crossing insert its four rows (10) at its four actual face
occurrences. Add rows with the same global face label, including repeated
occurrences at one crossing. Concatenate the five columns of every
crossing to define global integral matrices \(\mathcal A,\mathcal B\)
and an integer column \(n\), with one row per face. Thus

\[
\partial_y G=\mathcal A\lambda+\mathcal B\mu+\pi i n,
\qquad \mathbf1^{\mathsf T}\mathcal A
 =\mathbf1^{\mathsf T}\mathcal B=0,
\quad \sum_f n_f=0.
\tag{11}
\]

All anchor histories and closure degrees are included because (4)
parametrizes their literal full path lattice. The residual character
\(\bar\chi\in\Lambda^*\) of [L] pulls back uniquely to an integer
face vector \(\xi\) with \(\sum_f\xi_f=0\). The complete marked
source stationary equations in these coordinates are

\[
\boxed{\quad
\mathcal A\lambda+\mathcal B\mu
       =\pi i(2\xi-n).
\quad}
\tag{12}
\]

One face row is redundant. Fixing its potential leaves exactly the
equations on an integral basis of the physical lattice. In particular
the exponential equations are
\(\prod z_a^{\mathcal A_{fa}}(1-z_a)^{\mathcal B_{fa}}
=(-1)^{n_f}\), with the integer lift (12) retained.
For the part of the graph meeting crossings, this is a unimodular
change of physical basis in [L]. Adjoining the same monomial shape
relations therefore preserves its primitive signed-Lagrangian lattice.
Directions belonging to separated crossing-free factors are handled
as in Section 2, rather than asserted to supply independent shape rows.

At every actual integer path and its integer potential lift,

\[
\bar\chi(p_{\rm path})=\sum_f\xi_f p_f\in\mathbb Z,
\qquad \exp(-2\pi i\sum_f\xi_f p_f)=1.
\tag{13}
\]

Thus the residual Fourier correction changes no finite coefficient.
It is independent of the constant choice of potential. The canonical
clock correction, original pivots, external scalars, finite inequalities
and endpoints remain exactly as in [L]; no new quantum recurrence is
inferred from (12). These statements are at the complete fixed root,
not an off-root or generic-meridian normal transport.

For comparison only, imposing a fixed color on one specified edge in
a different presentation would add the corresponding affine equation
in (3), and its homogeneous variations would satisfy equality of those
two face potentials. That would reduce the circulation rank by one:
the directed all-ones circulation shows the edge functional is primitive.
No such equation is imposed on the summed first edge of (1).

## 6. Scope and the next compatibility

This theorem is an exact assembly of the original logarithmic **source**
rows. It does not identify them with all edge equations of a simplicially
glued five-tetrahedron decomposition. The local five-atom boundary can
be compared with an octahedron, but individual configuration-face
cancellation does not by itself prove that differently triangulated
over/under port disks have been sewn with the required topology and
logarithmic marks. Such a comparison must supply the actual face maps,
edge orbits and peripheral/mark transport. No missing endpoint or
relative-source current is declared zero here.

The integral flow--face isomorphism is prior coverage [M, Section 7].
The additional content is (7)--(13): both literal crossing assignments,
their complete logarithmic and parity rows, and the global integer
character in the actual averaged-cut source. Linear rank does not imply
a nondegenerate saddle, a selected cycle or scalar noncancellation.

## Direct source versions

The four complete texts were read at these versions. Only written
proofs are used; no program, test or numerical calculation was run.

| Label | Source | SHA-256 |
| --- | --- | --- |
| L | [Reduced physical logarithmic lattice](research_reduced_physical_marked_logarithmic_lattice.md) | f0c2d09d9f36b176a0a593db9723db55325737a39d9bfebc087583a875cffa79 |
| C | [Whole charged bridge source](actual_global_charged_bridge_flow.md) | b444e487eab3ec0a56c40b22584837cefcbe374a137b0beeaa185116c2a81d8c |
| S | [Signed overbridge unwinding](actual_signed_overbridge_unwinding.md) | 0a875f4feb3a1eecb8dbb77a5a7ec170ef95884746f5babd8b54659bc2e0078a |
| M | [Original MAIN-edge mark transport](research_arbitrary_main_edge_mark_transport.md) | 7a7c9efdca1e9f7907dc5baf5dfe8ba12e2345ee5f2df2ed94240e95ee69112a |
