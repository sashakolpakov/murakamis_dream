# A positive subdivision for a mixed rational crossing word

The marked-germ comparison left open in Sections 8–9 is completed in [the subsequent original collar proof](research_mixed_word_collar_representation.md), which also proves the long odd-filling corollary.

Consider the original pendant word
\[
                         T(R^{-2}T(R^2)).
                         \tag{1}
\]
Keep one crossing circle at its remaining boundary, with carrier \(+1\).
Its augmented link has two components: the main component and the retained
circle. This note constructs a complete positive ideal triangulation of
its complement. An explicit five-term identity identifies its volume
with the real critical value of the original mixed Newton source.

The complete volume statement is separate from the deformed peripheral
statement. Section 8 specifies the further marked-germ comparison needed
for a long-filling application. It is not inferred from the complete
volume or the shape multiset.

## 1. The original diagram

The original through tangle is vertical. Its pillowcase fraction is
reciprocal to the convention assigning zero to the horizontal through
tangle. Word (1) has pillowcase slope \(2/5\) in our convention.

Its actual planar-diagram code is
\[
\begin{split}
 &(12,5,13,6),\ (6,13,7,0),\ (4,7,5,8),\\
 &(8,3,9,4),\ (2,11,3,12),\ (1,16,2,17),\\
 &(10,15,11,16),\ (14,9,15,10),\ (17,0,14,1).
\end{split}                                                     \tag{2}
\]
Numbers label strand segments; each row lists the four incident
segments in cyclic order. The first four crossings are the two
signed boxes in (1), the fifth is the \(+1\) carrier, and the last
four draw the crossing-circle oval.

Here is a direct specification of the oval. Call its crossings
\(c_0,c_1,c_2,c_3\), with half-edges numbered cyclically, and join
\[
\begin{array}{c|c}
(c_3,3)&(c_0,0)\\
(c_2,3)&(c_1,0)\\
(c_0,3)&(c_3,0)\\
(c_0,1)&(c_1,3)\\
(c_1,1)&(c_2,2)\\
(c_2,0)&(c_3,2).
\end{array}                                                     \tag{3}
\]
The external ends, in bottom-left, bottom-right, top-left, top-right
order, are \((c_3,1),(c_2,1),(c_0,2),(c_1,2)\).
The oval passes over both strands along its top arc and under both
along its bottom arc. Insert the carrier and word (1), then take the
original cylindrical closure.

The verifier builds precisely this tangle from individual crossings.
Spherogram multiplication puts the first factor above the second;
the manuscript's written stack puts it below. Accordingly the pendant
is constructed as
~~~python
turn(turn(crossing_word(2)) * crossing_word(-2))
~~~
with a clockwise turn, and then closed as
~~~python
(pendant * crossing_word(1) * augmented_circle_block).braid_closure()
~~~
Its PD code, including signs, is checked against (2). No census name
is used to identify the exterior.

## 2. A finite topological certificate

Use the four-tetrahedron crossing ball in
[the diagram fundamental-cycle proof](crossing_fundamental_cycle.md).
Joining the strand-end triangles gives thirty-six tetrahedra and
two finite projection poles.

There is a direct formula for every raw face. Number the tetrahedra
at crossing \(c\) as \(4c+j\), \(0\le j<4\), and number faces by
opposite vertices. Every vertex permutation is \((0,1,3,2)\).
The internal pairings are
\[
\begin{split}
(4c+j,0)&\longleftrightarrow(4c+3-j,0),\\
(4c+j,1)&\longleftrightarrow(4c+(j\mathbin{\mathrm{xor}}1),1).
\end{split}                                                     \tag{4}
\]
An arc from half-edge \(j\) at crossing \(c\) to half-edge \(k\)
at crossing \(d\) gives the exterior pairings
\[
\begin{split}
(4c+(j+1\bmod4),2)&\longleftrightarrow(4d+(k+2\bmod4),3),\\
(4c+(j+2\bmod4),3)&\longleftrightarrow(4d+(k+1\bmod4),2).
\end{split}                                                     \tag{5}
\]
These formulas independently regenerate all raw faces from (2).
The crossing-ball construction explains why their quotient is the
diagram exterior with two ordinary interior vertices.


For clarity, the numbering in (4)--(5) differs from the signed
crossing-ball table in the cited proof. The exact relabelling is
\[
\begin{array}{c|c|c}
\text{old tetrahedron}&\text{new tetrahedron}&
   \text{images of old vertices }(0,1,2,3)\\ \hline
0&0&(1,3,2,0)\\
1&3&(1,2,3,0)\\
2&1&(1,2,3,0)\\
3&2&(1,3,2,0).
\end{array}
\]
It sends the old strand ends (over in, over out, under in,
under out) to the PD slots \((3,1,0,2)\), respectively.
It reproduces both the internal face pairings and the endpoint
pairs used in (5). The verifier checks these correspondences.

There is an orientation calibration here. Multiplying the old
signed orientations by these permutation signs gives \(-1\)
for all four tetrahedra. Thus this raw numbering reverses the
orientation used in that signed crossing-block proof. This
does not alter the complement or its positive, unsigned
hyperbolic volume. It must be retained when comparing oriented
peripheral periods; it is not silently absorbed into a carrier
change in Section 8.


For a negative crossing the old tetrahedra map instead to
\((1,2,0,3)\); the vertex maps are \((1,2,3,0)\) on old
tetrahedra \(0,3\) and \((1,3,2,0)\) on old tetrahedra
\(1,2\). Reading the old block backwards gives PD strand-end
slots (over in, over out, under in, under out) equal to
\((1,3,0,2)\). The reversed signed orientations again become
\(-1\) on all four new tetrahedra. Thus the same global
orientation reversal applies to both crossing signs.
At an arc strip, the auxiliary and region vertices map to new
vertices \(1\) and \(0\); preserving those and the arc vertex
gives exactly the swap \((2,3)\) in (5).

The fixed
[subdivision data](../repro/fixtures/research-mixed-two-crossing-subdivision.json)
contain all face tables and the complete move list. First collapse
an edge between the two finite vertices. Then collapse an edge from
the resulting finite vertex to a cusp. At each step the endpoints
are distinct and the edge has an embedded open star. These are
contractions of tame arcs, first between interior points and then
from an interior point to the deleted ideal vertex. No two cusps
are identified.

Next perform twenty-eight recorded local moves: valence-two pillow
removals, \(3\to2\) moves and \(4\to4\) moves. A pillow removal deletes
the two tetrahedra around its edge and joins the exposed sides.
A \(3\to2\) move changes the subdivision of a triangular bipyramid;
a \(4\to4\) move changes an octahedral ball's internal diagonal.
Each is the identity on its local exterior boundary. The replay
checks its incident tetrahedra and local admissibility before
performing it, rather than only comparing its endpoints.

Eight tetrahedra remain. An explicit tetrahedron-and-vertex
relabelling to the saved eight-tetrahedron table is checked on
all thirty-two faces. A final \(2\to3\) move at tetrahedron zero,
face one, gives the nine-tetrahedron complex below. The final
relabelling has tetrahedron images
\[
                         (3,4,5,6,7,8,0,2,1)
\]
and the identity vertex permutation on every tetrahedron.

The replay contains no search, numerical isometry calculation or
census lookup. It uses the inspectable t3mlite local move routines.
Their local-ball interpretation is the topological justification.

The original meridian and disk longitude are carried by these
literal homeomorphisms. On a truncated cusp the moves change
subdivisions inside disks; the finite-to-cusp collapse also changes
a disk. Curves can be displaced off these disks and carried through.
There is therefore no multiplication of a primitive curve or
unrecorded framing twist. Exported peripheral arrays use a package's
basis and are not substituted for the original disk basis.

## 3. The positive algebraic structure

Let \(X\) be the unique root in the upper half-plane of
\[
                       X^3+2X^2+1=0,\qquad Y=1+2X+2X^2.
                                                               \tag{6}
\]
The cubic has one real root below \(-2\), and one nonreal conjugate
pair. Writing \(X=\alpha+i\beta\), \(\beta>0\), gives
\[
8\alpha(1+\alpha)^2=1,\qquad
\beta^2=4\alpha+3\alpha^2,\qquad 0<\alpha<1/8.          \tag{7}
\]
Define
\[
a=1-X^{-1},\quad b=X(1-X),\quad
c=\left(\frac{Y-1}{Y+1}\right)^2,\quad
l=\frac{Y+1}{2},\quad k=\frac{2Y}{Y+1}.               \tag{8}
\]
The nine oriented shape classes are
\[
                            (a,a,b,b,c,l,l,k,k).
                                                               \tag{9}
\]
The three parameters \(z,1/(1-z),(z-1)/z\) describe the same
oriented shape. In the saved tetrahedron order they are:

| Tetrahedron | Shape |
| --- | --- |
| \(0,1\) | \((X^2+3X-1)/2\) |
| \(2\) | \((2X^2+3X-1)/4\) |
| \(3\) | \((X^2+3X+1)/2\) |
| \(4\) | \((3X^2+5X+1)/4\) |
| \(5\) | \(X^2+X+1\) |
| \(6\) | \(X-X^2\) |
| \(7\) | \(X\) |
| \(8\) | \((X^2+3X+3)/4\) |

All shapes are positive. We have \(\Im a>0\),
\(\Im b=\beta(1-2\alpha)>0\), and
\(\Im Y=2\beta(1+2\alpha)>0\). Also
\[
 |Y|^2-1=4\alpha(16\alpha^3+40\alpha^2+26\alpha+1)>0. \tag{10}
\]
Thus \((Y-1)/(Y+1)\) has positive real and imaginary parts, so
\(c\) has positive imaginary part. The real Möbius maps defining
\(l,k\) preserve the upper half-plane.

**Proposition 1.** These shapes give the complex of Section 2 a
complete positively oriented ideal triangulation.

**Proof with finite certificate.** Reconstruct the nine edge
equations from the face pairings, with \(z,z',z''\) on the edge
pairs \(01/23,02/13,03/12\). Their products reduce exactly to one
modulo (6). To exclude extra winding, isolate \(\alpha,\beta\)
in rational intervals using (7). Alternating rational arctangent
bounds put every edge's total angle in \((6,7)\). Its exact
product equation then forces total angle \(2\pi\). The bound
for \(\pi\) is itself certified by Machin's arctangent identity.

The vertex links are two tori. Completeness is checked on every
cycle of their cusp-triangle adjacency graphs. Normalize a
tetrahedron's vertices to \((\infty,0,1,z)\). Use coordinate
\(w\) at infinity and \(1/(w-v)\) at a finite vertex \(v\).
A face pairing gives its linear cusp-similarity ratio by comparing
the two common finite coordinates. Propagation gives seventy-four
exact return checks, all equal to one in the cubic field. Thus
the triangles have consistent Euclidean scales and translation
holonomy. Their compact Euclidean tori are complete. Together
with the edge-angle check, this proves the proposition.
\(\square\)

The complement's volume is therefore
\[
                         2D(a)+2D(b)+D(c)+2D(l)+2D(k),            \tag{11}
\]
where \(D\) is the Bloch--Wigner dilogarithm. Its approximate value
is \(7.70691180281012665\); that decimal is not used in the proof.

## 4. The actual rational-word character

The original ordered Fricke coordinates satisfy
\[
\begin{split}
R(A,B,C)&=(A,C,8-AC-B),\\
R^{-1}(A,B,C)&=(A,8-AB-C,B),\\
T(A,B,C)&=(B,A,8-AB-C).
\end{split}                                                     \tag{12}
\]
The complete meridian intertwiners were proved in
[the Newton canonical-graph calculation](actual_newton_twist_canonical_graph.md).
The actual through cap is \((A,B,C)=(z,2,4-z)\).
Resolving its Newton clock by \(q\to1\) with
\[
                         V=\frac{(q-1)^2}{zq-q^2-1}
\]
gives the actual meridian matrices
\[
\begin{pmatrix}1&1\\0&1\end{pmatrix},\
\begin{pmatrix}1&0\\z-2&1\end{pmatrix},\
\begin{pmatrix}1&0\\2-z&1\end{pmatrix},\
\begin{pmatrix}1&-1\\0&1\end{pmatrix}.                 \tag{13}
\]
Their inverse pairs are the literal two through arcs.

Applying \(TR^{-2}TR^2\), rightmost first, gives
\[
 A_{\rm out}+2=(z^2-5z+7)(z^3-3z^2+5z-2).
                                                               \tag{14}
\]
At \(z=1+X^{-1}\), all three ordered output traces are
\[
-2,\quad
\frac{2(3Y^2-2Y+3)}{(Y+1)^2},\quad
\frac{2(9Y^2+2Y+1)}{(Y+1)^2}.                         \tag{15}
\]
These match the complete parent leaf at clock \(Y\) and momentum
\(-(Y-1)^2/(Y+1)^2\). The verifier checks all three identities.

The crossing layers explain the positive shape list. The first
two positive crossings have limiting parameters \(0,1,1,a\);
the two negative crossings give \(a,b,b,c\). The five nonflat
crossing parameters are \(a,a,b,b,c\), and the parent leaf
gives \(l,l,k,k\), up to oriented shape permutations.
This explanation alone does not authorize discarding the three
flat cap tetrahedra. The independent diagram move certificate
of Section 2 supplies the topology for Proposition 1.

## 5. An exact five-term regulator comparison

Use
\[
D(u)+D(v)=D(uv)+
D\left(\frac{u(1-v)}{1-uv}\right)+
D\left(\frac{v(1-u)}{1-uv}\right).                    \tag{16}
\]
Put \(Z=X^2/(1-b)\) and \(w_0=(1-X)^2/(1-b)\).
The pairs \((X,1-X)\), \((b,1-Z)\), and \((X,w_0)\) give
\[
\begin{split}
0&=D(b)+D(Z)+D(w_0),\\
D(b)-D(Z)&=D(Xw_0)-D(c)+D(Y),\\
D(X)+D(w_0)&=D(Xw_0)-D(Y)+D(XY).
\end{split}                                                     \tag{17}
\]
For instance the second line uses
\[
\frac{bZ}{1-b+bZ}=\frac{c}{c-1},\qquad
\frac{(1-Z)(1-b)}{1-b+bZ}=\frac{Y-1}{Y}.
\]
Elimination gives
\[
                    2D(b)+D(c)=D(X)+2D(Y)-D(XY).      \tag{18}
\]
Next use the pairs \((l,k)\) and \((Y,Y)\), with \(lk=Y\).
The remaining real argument is \(1/2\), whose value is zero:
\[
                        2D(l)+2D(k)=4D(Y)-D(Y^2).     \tag{19}
\]
All fifteen rational arguments of these five applications are
checked exactly. Since \(D(a)=D(X)\), equations (11), (18),
and (19) prove
\[
\boxed{\operatorname{Vol}(M)=3D(X)+6D(Y)-D(XY)-D(Y^2).}            \tag{20}
\]
This is a real regulator identity. It does not assert an integral
flattening or a complete complex Chern--Simons identity.

## 6. The source's complete real action

Use the original branches in
[the mixed source calculation](research_mixed_two_crossing_horizontal_dominance.md).
For \(J(z)=\int_0^z\log(2\sin\pi t)\,dt\), its phase is
\[
W(x,y;0)=J(x+y)-3J(x)-6J(y)+J(2y)
                    +i\pi(xy-y^2/2-y/2).             \tag{21}
\]
At the selected point \(x=\log X/(2\pi i)\),
\(y=\log Y/(2\pi i)\), the literal unexponentiated critical
equations hold on the bulk branches.

On these branches,
\[
2\pi\Re J(z)=-D(e^{2\pi iz})+
     \log|e^{2\pi iz}|\,\arg(2\sin\pi z).             \tag{22}
\]
Write \(x=a_0+ih\), \(y=b_0+ik_0\), and let \(A,B,C,D_2\)
be the arguments of \(2\sin\pi x,2\sin\pi y,
2\sin\pi(x+y),2\sin2\pi y\), respectively. The imaginary
critical equations give
\[
C-3A=-\pi b_0,\qquad
C-6B+2D_2=-\pi(a_0-b_0-1/2).                         \tag{23}
\]
The logarithmic corrections in the four \(J\) terms consequently
sum to \(2\pi^2\{hb_0+k_0(a_0-b_0-1/2)\}\). The quadratic
term in (21) cancels this number exactly. Hence
\[
\boxed{2\pi\Re W(x,y;0)=\operatorname{Vol}(M).}        \tag{24}
\]
No numerical calibration is used.


**Corollary 2 (the original boundary polynomial).** Let \(Z_N(u)\)
be the original canonical boundary polynomial
\[
Z_N(u)=\operatorname{can}\!\left(T(R^{-2}T(R^2))\right)(-2\cos u).
\]
For the two-cusped augmented complement \(M\) specified by (2),
\[
                 \lim_{N\to\infty}\frac{2\pi}{N}
                     \log|Z_N(0)|=\operatorname{Vol}(M).
\]
Indeed the mixed boundary theorem gives a nonzero leading
coefficient times a fixed power of \(N\) times \(e^{NS(0)}\).
Equation (24) supplies its absolute volume normalization.
Here \(Z_N(0)\) is the original boundary-polynomial evaluation;
it is not being renamed as a closed-knot invariant.

## 7. Reproduction

Run
~~~sh
.venv/bin/python experiments/verify_mixed_two_crossing_positive_subdivision.py
~~~
Its fixed face tables, moves and algebraic coefficients are in the
fixture above. The result is saved in
[the subdivision verification report](../repro/results/research-mixed-two-crossing-positive-subdivision.json).
The diagram construction, local move replay, cubic-field checks
and rational angle bounds are separate parts of the verifier.

The original boundary source asymptotic is proved separately in
[the mixed boundary theorem](research_mixed_two_crossing_boundary_theorem.md).
This geometric certificate does not supply that analytic proof.

## 8. What remains for deformed primitive periods

For the full critical boundary phase \(S(u)\), set \(w=e^{iu}\).
Its equations are
\[
X^2Y-X=(1-X)^3,\qquad
(1-XY)(Y+w)(Y+w^{-1})=(1-Y)^4.                       \tag{25}
\]
The original leaf polarization gives
\[
e^{-2\pi S'(u)}=\frac{Y+w}{1+wY}.                    \tag{26}
\]
For carrier \(\eta\), the candidate marked primitive periods are
\[
U=-2\pi S'(u)-i\eta u,\qquad V=2iu,\qquad
e^U=w^{-\eta}\frac{Y+w}{1+wY}.                       \tag{27}
\]
The carrier term occurs once. The original leaf's meridian and
disk longitude are computed in
[the deformed collar proof](../papers/strict-conway-geometry/deformation.tex);
the Newton Legendre conversion is proved in
[the zero-subtree geometry note](research_zero_subtree_conway_geometry.md).

For a long-filling application one must still identify the
representation germ defined by the actual word, (25), and the
original leaf maps with the geometric deformation germ of
Proposition 1, carrying the original curves through Section 2.
An explicit transport of decorated face maps, or a complete
layered-cap comparison of those maps, would prove this.

The complete trace match, shape multiset, and complete volume
identity do not bypass that step. Until it is supplied, (27)
is an exact marked source/leaf formula, while the long-filling
application remains conditional on the geometric-germ comparison.

## 9. A complete collar comparison that can help with Section 8

The four tetrahedra incident to the auxiliary cusp are \(0,1,3,5\).
Their two pyramid subdivisions admit the following developed orders:
\[
\begin{array}{c|c}
3&(\infty,1,Y,-1)\\
5&(\infty,1,-1,-Y)\\
0&(-1,1,Y^{-1},\infty)\\
1&(-1,1,\infty,-Y^{-1}).
\end{array}
\]
The two internal diagonal faces agree with the saved pairings.
The remaining four side pairings, read from the second pyramid
to the first, are
\[
f_j(z)=-Yz+c_j,\qquad
(c_0,c_1,c_2,c_3)=(1+Y,\,1-Y,\,Y-1,\,-1-Y).
\]
They arise respectively at faces \(0,0;\ 0,1;\ 1,0;\ 1,1\).
Two are white pairings and two are the odd shaded pairings;
calling all four white would be incorrect.

Put
\[
M_+(z)=\frac{Y+1}{2}\frac{z-1}{z-Y},\qquad
M_-(z)=\frac{Y+1}{2Y}\frac{z-1}{z-Y^{-1}}.
\]
With \(E=Y\), \(R=(Y+1)^2/(4Y)\), direct projective matrix
multiplication gives
\[
\begin{array}{c|c}
j&M_- f_j^{-1}M_+^{-1}\\ \hline
0&W_0\\
1&B\\
2&A\\
3&W_2 .
\end{array}
\]
Here \(W_0,W_2,A,B\) are exactly the original white and odd
shaded matrices in the deformed collar proof. The verifier checks
these four projective identities. Thus, in this local labelling,
the original collar words have translations
\[
W_0^{-1}B=f_0f_1^{-1}:z\mapsto z+2Y,\qquad
W_2^{-1}W_0=f_3f_0^{-1}:z\mapsto z-2(Y+1).
\]
Their ratio is \(-1-Y^{-1}\), agreeing with \(V'(0)/U'(0)\)
from (27) at \(\eta=1\).

What remains is the identification of these locally labelled
disk paths with the original paths in (2) through the recorded
moves, followed by the full rational-tangle representation
comparison. The exact four-map calculation does not silently
supply that topological marking.

A displayed software cusp shape should not be used to settle
this sign. The package's upper-half-plane cusp-shape convention
can conjugate a literal translation ratio. In addition, an
SL(2) peripheral matrix of trace \(-2\) must be normalized before
taking its off-diagonal ratio with a trace-\(+2\) matrix. Such
ratios are diagnostics until the original oriented disk curves
have been fixed. No carrier sign has been changed to make a
numerical cusp shape agree.


