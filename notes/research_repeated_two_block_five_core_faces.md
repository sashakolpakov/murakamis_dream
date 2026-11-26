# The five-cell core: exact faces, edge products and a doubled angle structure

Research deduction, 8 November 2026. All finite lists below are read
from an existing saved face table and traced by hand. No checker,
subdivision replay, numerical evaluation or new certificate arithmetic
is used.

The [five-shape dictionary](research_repeated_two_block_five_shape_layer_dictionary.md)
proves the actual capped representation and its sharp source
regulator. This companion extracts a concrete relative five-cell
complex from the already proved augmented mixed-word subdivision.
It gives every core face, both internal edge equations, all six
boundary products, and an explicit complete ten-cell double with
positive shapes and edge angles exactly \(2\pi\). A literal
annular loop has nontrivial parabolic holonomy, which proves
completeness of the doubled cusp.

The double is not yet identified with the original marked \(29/17\)
knot exterior. The remaining marking obligations are stated
separately in Section 7.

## 1. An exact subcomplex of the saved diagram triangulation

Use the original nine-cell complex in
[the positive subdivision theorem, Sections 2 and 9](research_mixed_two_crossing_positive_subdivision.md),
with its fixed
[face fixture](../repro/fixtures/research-mixed-two-crossing-subdivision.json),
field nine_gluing. Its four outside collar tetrahedra are
\(0,1,3,5\). Delete their interiors and retain
\[
                 A=2,\quad B=4,\quad C=6,\quad D=7,\quad E=8.
 \tag{1}
\]
Faces are numbered by their omitted vertex in the saved order
\((0,1,2,3)\). A permutation in the following table sends each
source vertex to the target vertex. Each reverse pairing is its
inverse.

| Source face | Target face | Vertex permutation |
|---|---|---|
| \(A0\) | \(C2\) | \((02)\) |
| \(A1\) | \(B1\) | \((23)\) |
| \(B0\) | \(E3\) | \((03)\) |
| \(B2\) | \(D0\) | \((02)\) |
| \(C0\) | \(D3\) | \((03)\) |
| \(C1\) | \(E1\) | \((23)\) |
| \(D1\) | \(E2\) | \((0123)\) |
| \(D2\) | \(E0\) | \((02)\) |

The four unpaired faces are precisely
\[
                         A2,\quad A3,\quad B3,\quad C3.
 \tag{2}
\]
In the full saved complex they meet, respectively, \(0\,3\),
\(1\,2\), \(3\,0\), and \(5\,0\). Thus (1)--(2) are an
actual subcomplex extraction, not a proposed retriangulation
based on a shape multiset. Every internal permutation above
is odd, so all five saved vertex orders have the same
consistent orientation.

Removing the four-cell subcomplex alone does not say that
its interface is the original specified Conway sphere under
the preceding diagram move list. This marked identification
is not assumed below.

## 2. Edge and link inventory

Write \(Aij\) for the edge with endpoints \(i,j\) in \(A\),
and similarly for the other cells. Tracing the eight face
pairings gives exactly the following eight edge classes:
\[
\begin{array}{c|l}
r&A12,\ C01\\
s&A13,\ C13,\ D01,\ E12,\ B12\\
\iota&A23,\ C03,\ B23,\ E02\\
u_0&A02,\ B03,\ D23,\ E03,\ C02\\
v&A03,\ B02\\
\jmath&B13,\ E01,\ D03,\ E23,\ C23,\ D02,\ E13,\ D13\\
x&B01,\ D12,\ C12\\
y&A01 .
\end{array}
 \tag{3}
\]
The classes \(\iota,\jmath\) have circular links; the other
six have interval links ending in (2). In particular all
thirty tetrahedral edges occur in (3). The two circular
paths, with their endpoints retained individually, are
\[
\begin{split}
&A23\to C03\to E02\to B23\to A23,\\
&B13\to E01\to D03\to E23\to C23\to D02
                                      \to E13\to D13\to B13 .
\end{split}
 \tag{4}
\]
Both return maps fix each endpoint; neither is an edge
reversal. This can also be read directly from the indicated
vertex permutations.

To describe the boundary before identifying the annular
ends, use four puncture labels \(a,b,c,d\):
\[
\begin{array}{c|c|c}
\text{face}&\text{ordered punctures}&\text{edge classes}\\ \hline
A2&(a,b,c)&(y,v,s)\\
A3&(a,b,d)&(y,u_0,r)\\
B3&(a,b,c)&(x,v,s)\\
C3&(d,b,a)&(r,u_0,x).
\end{array}
 \tag{5}
\]
Here, for example, \(A0=a,A1=b,A3=c,A2=d\) on the
boundary; these are puncture labels rather than four
distinct global ideal-vertex classes.
The boundary has the two distinct \(a b\) edges \(x,y\).
It is a sphere with four punctures.

There are exactly two ideal-vertex classes in the core:
\[
\begin{array}{c|l}
\mathfrak a&
A0,A2,B0,B3,C0,C2,D2,D3,E0,E3\\
\mathfrak b&
A1,A3,B1,B2,C1,C3,D0,D1,E1,E2 .
\end{array}
 \tag{6}
\]
Their links are connected and orientable. Each has ten
triangles, eighteen edges and eight vertices, hence Euler
characteristic zero. The boundary cycles of the first link
have puncture labels \(a,d\), and those of the second have
labels \(b,c\). There are two boundary cycles in each case,
so both links are annuli. Thus (1) is a manifold core with
the indicated four-punctured boundary and two annular ends,
not an ideal pseudomanifold with singular vertex links.

These link conclusions use only (1)--(6). They neither
identify its marked rational-tangle slope nor transport a
preferred longitude through the saved diagram moves.

## 3. Shapes and all eight edge products

At the selected maximum of the actual coefficient packet, use
the notation of the five-shape dictionary:
\[
 w=u(1-u),\quad d=1-u+u^2,\quad
 V=\frac{u^3(1-u)}{d^2},\quad
 p=\frac{1-2u+3u^2-u^3}{u^2},\qquad |p|=|V|=1.
 \tag{7}
\]
The parameter \(u_0\) in (3) is only an edge name; it is
unrelated to the complex number \(u\).
Assign the five saved vertex orders the shapes
\[
 z_A=-V,\qquad z_B=\frac{w-1}{w},\qquad
 z_C=w,\qquad z_D=u,\qquad z_E=\frac1{1-u}.
 \tag{8}
\]
Every shape is positive by Section 4 of the dictionary;
the changes from \(w,u\) are even tetrahedral permutations.
In the original augmented subdivision, (8) specializes to
the shapes of its cells \(2,4,6,7,8\): its notation has
\(a=1-u^{-1}\), \(b=w\), and \(c=-V\), and those cells have
shapes \(c,(b-1)/b,b,1/(1-a),(a-1)/a\).
The present general assignment (8) will be checked directly;
it is not inferred by continuing a numerical shape solution.

On edge pairs \(01/23,02/13,03/12\), respectively, put
\[
                     z,\qquad z'=\frac1{1-z},
                       \qquad z''=\frac{z-1}{z}.
 \tag{9}
\]
The five rows of edge parameters are consequently
\[
\begin{array}{c|ccc}
 &01/23&02/13&03/12\\ \hline
A&-V&(1+V)^{-1}&(1+V)/V\\
B&-d/w&w&1/d\\
C&w&1/d&-d/w\\
D&u&(1-u)^{-1}&-(1-u)/u\\
E&(1-u)^{-1}&-(1-u)/u&u .
\end{array}
 \tag{10}
\]
Their products on the two internal edges are
\[
\begin{split}
P_{\iota}
 &=(-V)\frac{-d}{w}\frac{-d}{w}\frac{-(1-u)}u
   =\frac{Vd^2(1-u)}{uw^2}=1,\\
P_{\jmath}
 &=w^2(1-u)^{-4}\frac{(1-u)^2}{u^2}=1.
\end{split}
 \tag{11}
\]
These are rational identities, independent of the outer
stationarity \(|p|=|V|=1\).

The six boundary-edge products, retaining every incident
tetrahedron, are
\[
\begin{array}{c|c}
\text{edge}&\text{product}\\ \hline
r,\ v&(1+V)w/V=p\\
s,\ u_0&u^2/[d^2(1+V)]=p^{-1}\\
x&-V^{-1}\\
y&-V .
\end{array}
 \tag{12}
\]
For example \(1+V=(1-2u+3u^2-u^3)/d^2\), which proves
both occurrences of \(p\). These formulas are the full
relative edge data, not just the wedge boundary of a
regulator sum.

## 4. An explicit doubled face complex

Take a second copy \(\overline{\mathcal C}\) of (1), with
the same face permutations and complex-conjugate developed
shapes in the saved vertex orders. Give it the opposite
orientation. Equivalently, after any odd vertex relabelling,
its tetrahedra have positive shapes.

Glue the four first-copy boundary faces to the second copy by
\[
\begin{array}{c|c|c}
\text{source}&\text{target}&\text{vertex permutation}\\ \hline
A2&\overline B3&(01)(23)\\
B3&\overline A2&(01)(23)\\
A3&\overline C3&(012)\\
C3&\overline A3&(021).
\end{array}
 \tag{13}
\]
All four permutations are even. They are therefore
orientation-reversing boundary identifications between the
two oppositely oriented cores. On (5), the map swaps
\(a,b\), fixes \(c,d\), and exchanges \(x,y\). Its action
on the six boundary edges is
\[
                   r\leftrightarrow u_0,\qquad
                   s\leftrightarrow v,\qquad
                   x\leftrightarrow y.
 \tag{14}
\]
The table respects all boundary edge incidences, so it is a
homeomorphism of the four-punctured boundaries.

The result has ten tetrahedra and ten edge classes: the two
internal edges from each copy and the six glued boundary
edges. The interval links in (3) glue to circles. The two
annular ends of each core are joined into one connected
closed orientable vertex link, because (13) takes the
puncture pair \((a,d)\) to \((b,d)\) and \((b,c)\) to
\((a,c)\). Gluing the four annuli along their boundary
circles preserves Euler characteristic zero. Hence this
single vertex link is a torus. In particular (13) defines
an oriented ideal three-manifold, not merely formal edge
equations.

For an oppositely oriented conjugate tetrahedron, the
positive complex edge parameter is the reciprocal of the
conjugate of the corresponding first-copy parameter.
Thus the product at a glued boundary edge \(e\) is
\[
            P_e\,\overline{P_{\tau(e)}}^{-1}=|P_e|^2,
 \tag{15}
\]
using the reciprocal pairing (12),(14).
At (7) all six products in (15) are one. The four internal
products are one by (11). This proves every multiplicative
edge equation of the doubled complex without an evaluation.

## 5. Angle lifts

All ten oriented shapes are positive. Each total edge
angle is therefore a strictly positive multiple \(2\pi n_e\)
of \(2\pi\), by its product equation, with \(n_e\ge1\).
The angle triangulation on the torus link has at each end
of an edge angle \(2\pi n_e\). Its combinatorial
Gauss--Bonnet sum is
\[
                  \sum_{\text{link vertices}}2\pi(1-n_e)
                              =2\pi\chi(T^2)=0.
 \tag{16}
\]
Every summand is nonpositive, so every \(n_e=1\).
This fixes the actual edge-angle lifts. It uses the proved
torus link and positivity; product equations alone would
not suffice.

The angle assertion (16) alone does not prove that the cusp
similarity holonomy has trivial linear part. The following
explicit peripheral loop supplies the additional input.

The sum of the oriented tetrahedral regulators of this
double is exactly
\[
       2\{2\mathcal D(u)+2\mathcal D(w)+\mathcal D(-V)\},
 \tag{17}
\]
the sharp source rate from the dictionary. Conjugation
reverses \(\mathcal D\), and the second core's orientation
reversal supplies the compensating sign. Equation (17)
is not yet the hyperbolic volume of the original knot.

## 6. A literal peripheral translation and completeness of the double

Set
\[
             h=1-u,\qquad k=1-2u+2u^2,\qquad \ell=2u-1.
 \tag{18}
\]
These denominators do not vanish at the selected point.
For \(k\), its upper zero is \(1/2+i/2\), whereas the
selected \(u\) has \(\Re u<1/2\). The other exclusions
follow from \(u\) being strictly in the upper half-plane.

Develop the core tetrahedra in one frame along the dual
tree \(A-C,A-B,B-E,B-D\), using their saved vertex orders:
\[
\begin{array}{c|cccc}
 &0&1&2&3\\ \hline
D&\infty&0&1&u\\
B&1&0&-u^2/h&u\\
E&u&0&-u^2/h&u^2/\ell\\
A&1&-u^2h/k&u&-u^2/h\\
C&u&-u^2h/k&u^2/\ell&-u^2/h .
\end{array}
 \tag{19}
\]
Use the vertex cross-ratio
\((v_0-v_2)(v_1-v_3)/[(v_0-v_3)(v_1-v_2)]\),
with its usual limits at infinity. Direct substitution
gives exactly (8), with edge parameters (9).
Every tree face identification is the
identity Möbius map with the listed vertex permutation.
The pairing \(C1\to E1\) is also the identity in this
development: its three vertices are sent by \((23)\).
The face pairing \(D1\to E2\) has Möbius map
\[
                  Z(t)=-\frac{u^2}{t-2u}.
 \tag{20}
\]
Indeed its permutation \((0123)\) requires
\[
                     Z(\infty)=0,\qquad
                     Z(1)=u^2/\ell,\qquad Z(u)=u,
 \]
which determine (20). Its determinant-one representative is
\[
                 \begin{pmatrix}0&-u\\u^{-1}&-2\end{pmatrix}.
 \tag{21}
\]
It has trace \(-2\), is not the identity projectively, and
fixes \(u\) with derivative one. Thus it is a nontrivial
parabolic transformation.

We verify that this transformation is a peripheral
holonomy, rather than merely a dual-face generator.
In the link of \(\mathfrak a\), the boundary component
labelled \(d\) in (5) meets the triangles at \((A,2)\)
and \((C,0)\). Its two corners are the boundary edge
classes \(r\) and \(u_0\). The fan at \(r\) is the
single face pairing \(A0\to C2\). The fan at \(u_0\)
is
\[
 (A,2)\ \xrightarrow{A1\to B1}\ (B,3)\
 \xrightarrow{B2\to D0}\ (D,3)\
 \xrightarrow{D1\to E2}\ (E,0)\
 \xrightarrow{E1\to C1}\ (C,0).
 \tag{22}
\]
Following (22) and returning by \(C2\to A0\) is therefore
a boundary-parallel loop in that annulus. Here pairs
\((A,2)\) denote tetrahedron vertices, whereas \(A1\)
denotes a face; all vertex images in (22) can be checked
in the table of Section 1. Every map along this loop
is the identity in (19), except \(D1\to E2\), whose
map is (20). Its holonomy is precisely \(Z\).

After (13), this annular loop is an actual loop in the
single torus cusp link. The edge equations and (16)
make the developed holonomy single-valued on the
manifold, so its peripheral image is an abelian subgroup
of \(\mathrm{PSL}_2(\mathbb C)\) fixing the cusp point.
It contains the nonidentity parabolic \(Z\). In a frame
that sends its fixed point to infinity and writes it
as \(t\mapsto t+c\), \(c\ne0\), a commuting affine map
\(t\mapsto at+b\) must have \(ac=c\), hence \(a=1\).
Thus every peripheral similarity has linear part one.

It follows that cusp-triangle Euclidean scales transport
consistently around every cycle. They give a compact
flat torus with translation holonomy. Its usual ideal
tetrahedral cusp extension is a complete hyperbolic cusp.
Together with the exact \(2\pi\) edge angles and positive
tetrahedra, this proves that the double (13) is a complete
finite-volume oriented hyperbolic three-manifold
\(\mathcal M_{\rm dbl}\). Equivalently, these are the
metric hypotheses of the
[marked positive-gluing theorem](general_marked_positive_gluing_certificate.md),
applied here to the explicitly defined double itself.

In particular
\[
 \operatorname{Vol}(\mathcal M_{\rm dbl})
    =2\{2\mathcal D(u)+2\mathcal D(w)+\mathcal D(-V)\}
    =\lim_{N\to\infty}\frac{2\pi}{N}\log|Z_{2,2,N}|.
 \tag{23}
\]
The last equality is the independently proved source
regulator. It does not identify \(\mathcal M_{\rm dbl}\)
with the source's original knot exterior.

## 7. Exact remaining marking obligations

The saved original diagram subdivision establishes the topology
of the full augmented nine-cell complex. The extracted core
and the newly defined double have the finite topological
properties proved above. A complete identification with the
original capped word must still establish the following.

1. The four-face interface (2), with its two annular ends,
   must be carried through the original subdivision moves
   as the specified rational-tangle boundary, including its
   four endpoint labels and inverse-pair cap marking.
   An identification of the complete augmented holonomy
   germ does not itself supply this relative homeomorphism.
2. Under that marking, the explicit gluing (13) must be the
   original Hermitian closing turn in
   \(\phi[J K_2^2\mathbf e_0]\), rather than a different
   mapping class with the same reduced trace action.
3. The original torus generators must be tracked under that
   identification. Section 6 proves completeness on the
   explicit double, but it does not rename its loop (22)
   as the original meridian or choose a preferred longitude.

The face and edge identities here are concrete inputs to those
checks. They neither invoke an unrecorded move sequence nor
replace them by positivity, a polynomial match or a numerical
recognition of the resulting three-manifold.
