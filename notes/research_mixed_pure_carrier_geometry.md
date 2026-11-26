# The pure collar of the mixed rational block

The rational tangle \(T(R^{-2}T(R^2))\) also has a geometric boundary
chart with no carrier crossing at its remaining reference circle.
This is the chart needed when the tangle is used as a piece of a larger
diagram. Its complete closure has three cusps, rather than the two
cusps of the positive-carrier closure.

We prove this using the literal pure diagram. A recorded sequence of
local triangulation moves gives a complete positive subdivision. The
shape field then selects the actual complete cap representation, and
the original oval crossing relations fix the meridian and disk
longitude. This proves the whole local geometric phase, not only its
value at the complete point.

The quantum boundary polynomial and its asymptotic expansion are those
already proved in [the mixed boundary theorem](research_mixed_two_crossing_boundary_theorem.md).
No new contour estimate is needed here.

## 1. Removing the carrier in the original diagram

Let \(F=T(R^{-2}T(R^2))\), with the same through tangle and clockwise
turn as in [the original collar proof](research_mixed_word_collar_representation.md).
Use the same four-crossing oval that surrounds the two vertical
strands. The only change to that diagram is to omit its additional
positive carrier crossing. In the tangle convention used by the
verifier the closure is
~~~python
(pendant * augmented_circle_block).braid_closure()
~~~
Its planar-diagram code is
\[
\begin{split}
 &(2,15,3,8),\ (8,3,9,0),\ (14,9,15,10),\ (10,13,11,14),\\
 &(1,6,2,7),\ (12,5,13,6),\ (4,11,5,12),\ (7,0,4,1).
\end{split}                                                     \tag{1}
\]
The first four rows are the rational word and the last four are the
oval. The two main components and the auxiliary circle are distinct
components in this particular closure. The rational tangle itself has
two strands and no internal closed component.
Tracing opposite strand ends in (1) gives the three arc sets
\[
 \{0,1,2,3\},\qquad \{8,9,10,11,12,13,14,15\},\qquad
 \{4,5,6,7\}.
\]
The last is the oval. Thus the two punctures of its disk and
its outside boundary lie on three distinct cusp tori.

Write \(g_j\) for the meridian of diagram arc \(j\), with the same
directions as in the odd-carrier proof. The complete relative
Wirtinger table for the oval is
\[
\begin{array}{c|c|c}
&\text{PD row}&\text{relation}\\ \hline
c_0&(1,6,2,7)&p=h^{-1}lh\\
c_1&(12,5,13,6)&q=h^{-1}rh\\
c_2&(4,11,5,12)&g_4=r^{-1}hr\\
c_3&(7,0,4,1)&h=l^{-1}g_4l,
\end{array}                                                     \tag{2}
\]
where
\[
l=g_0=g_1,\qquad r=g_{11}=g_{12},\qquad
p=g_2,\quad q=g_{13},\quad h=g_7=g_6=g_5.
\]
The ordered tangle corners, lower left, lower right, upper right,
upper left, are the arcs \((2,13,11,0)\). Their outward meridians are
\[
             (a,b,c,d)=(p,q,r^{-1},l^{-1}).
\]
Eliminating \(g_4\) gives \([h,rl]=1\). Hence the source-oriented
primitive meridian and disk longitude are
\[
        \mu_0=h^{-1},\qquad L=ba=rl,
\]
and the full relative presentation is
\[
 dcba=1,\qquad [\mu_0,L]=1,\qquad
                   \mu_0c\mu_0^{-1}=b^{-1}.                    \tag{3}
\]
All eliminations are reversible. There is no other crossing in the
open outside piece. The curve \(h\) is an ordinary meridian of the
original oval; \(rl\) runs once around each puncture of its spanning
disk. Thus (3) includes the original primitive marking. It does not
replace either curve by a multiple or add a framing twist.

In the original leaf maps put \(W_0=1\), by a change of chart, and set
\[
 a=W_1^{-1},\quad b=W_2^{-1}W_1,\quad
 c=W_3^{-1}W_2,\quad d=W_3,\quad
 L=W_2^{-1},\quad \mu_0=S^{-1}.
\]
The pure identities
\[
                 W_0S=S^\#W_0,\quad W_2S=S^\#W_2,\quad
                                      W_3S=S^\#W_1              \tag{4}
\]
give exactly (3). This compares full ordered matrices with the
literal relative presentation. It does not infer the presentation
from a hypothetical open face complex.

## 2. A positive subdivision of the pure complement

Put
\[
 X^3+2X^2+1=0,\qquad \Im X>0,\qquad Y=1+2X+2X^2.                \tag{5}
\]
Use the same nine shapes, in the same tetrahedron order, as in
[the positive subdivision of the odd closure](research_mixed_two_crossing_positive_subdivision.md):
\[
\begin{array}{c|c}
0,1&(X^2+3X-1)/2\\
2&(2X^2+3X-1)/4\\
3&(X^2+3X+1)/2\\
4&(3X^2+5X+1)/4\\
5&X^2+X+1\\
6&X-X^2\\
7&X\\
8&(X^2+3X+3)/4.
\end{array}                                                     \tag{6}
\]
Keep every face pairing except the following two pairs, including
their inverses:
\[
\begin{array}{c|c|c}
\text{source tetrahedron, face}&\text{target tetrahedron, face}
   &\text{vertex permutation}\\ \hline
(3,1)&(5,2)&(0,2,1,3)\\
(0,1)&(1,0)&(3,0,1,2).
\end{array}                                                     \tag{7}
\]
Faces are numbered by opposite vertices.

These are the pure shaded pairings. To see this directly, develop
the four collar tetrahedra in the orders
\[
\begin{array}{c|c}
3&(\infty,1,Y,-1)\\
5&(\infty,1,-1,-Y)\\
0&(-1,1,Y^{-1},\infty)\\
1&(-1,1,\infty,-Y^{-1}).
\end{array}
\]
Set \(\rho=(Y+1)^2/(4Y)\). The two leaf coordinates are
\[
 f_+(z)=\frac{(Y+1)(z-1)}{2(z-Y)},\qquad
 f_-(z)=\frac{(Y+1)(z-1)}{2Y(z-Y^{-1})}.
\]
In these coordinates the pure maps are
\[
 S=\begin{pmatrix}0&-Y\rho\\1&-1-Y\end{pmatrix},\qquad
 S^\#=\begin{pmatrix}0&-\rho/Y\\1&-1-Y^{-1}\end{pmatrix}.
\]
Conjugating back gives, respectively,
\[
                  z\longmapsto z+1-Y,\qquad
                  z\longmapsto z+1-Y^{-1}.
\]
They identify exactly the ordered vertices in (7). All other
collar faces, and in particular its four faces adjoining the
rational tangle, remain unchanged.

We also certify the topology directly from (1). Its crossing-ball
triangulation has thirty-two tetrahedra and two finite vertices.
The fixed certificate contracts a finite–finite edge, then a
finite–ideal edge. It follows these contractions by fifteen local
moves: valence-two pillow removals, \(3\to2\) moves and one \(4\to4\)
move. Eight tetrahedra remain. An explicit relabelling and a final
\(2\to3\) move give (7). Every face of both relabellings is checked.

Before each contraction the verifier checks distinct endpoints and
an embedded edge star; the endpoint genera are \(0,0\), then \(0,1\).
Before each later move it checks the incident tetrahedra and edge
valence. A pillow consists of two distinct tetrahedra sharing exactly
its two internal faces, with distinct opposite edges. These are
local ball replacements preserving the outside boundary, not a
recognition by census name or numerical volume. The crossing-ball
orientation calibration is the same for both crossing signs as in
the odd certificate; it reverses the convention of the older signed
shadow-block table uniformly.

**Proposition 1.** Equations (5)–(7) give the literal pure complement
of (1) a complete positive ideal triangulation.

**Proof.** The recorded moves give its topology. The final vertex
links are three tori. Reconstruct the edge equations from the face
pairings, placing \(z,z',z''\) on \(01/23,02/13,03/12\). All nine
edge products equal one in \(\mathbb Q(X)\). Rational bounds for
the real and imaginary parts of \(X\), followed by rational
arctangent bounds, prove positivity of every shape and place each
edge-angle sum in \((6,7)\). Its exact product equation therefore
forces the sum to be \(2\pi\).

The same calculation checks every return of the linear similarity
cocycle on all three triangulated cusp links: all seventy-five
return products are one. Hence the compact links carry consistent
Euclidean triangle metrics and translation holonomy. They are
complete tori. This proves completeness of the positive hyperbolic
structure. All arithmetic and topology checks are reproduced by
the verifier linked below. \(\square\)

The oriented shape multiset is unchanged. Consequently the
five-term identity already proved for (6) gives
\[
 \operatorname{Vol}(M_0)
  =3D(X)+6D(Y)-D(XY)-D(Y^2)=2\pi\Re S(0),                       \tag{8}
\]
where \(M_0\) is this pure complement, \(D\) is the Bloch–Wigner
dilogarithm, and \(S\) is the selected phase of the original mixed
boundary polynomial. The verifier repeats the five rational
argument identities; (8) uses the previously proved logarithmic
normalization of that phase.

Combining (8) with the nonzero full-source expansion gives the
polynomial-volume identity
\[
        \lim_{N\to\infty}\frac{2\pi}{N}\log|Z_N(0)|
                           =\operatorname{Vol}(M_0).
\]
Here \(Z_N\) is the original mixed boundary polynomial, evaluated
at its complete free angle. It is not being renamed a closed-knot
invariant.

## 3. Selecting a geometric character by its field of definition

The following observation is useful beyond this example.

**Lemma 2.** Suppose a specified ideal triangulation of an actual
augmented rational tangle complement has a complete positive shape
solution in a fixed embedded number field \(K\subset\mathbb C\).
Suppose its original main meridians and an auxiliary meridian
generate the group through the rational-cap and outside-piece
presentations. If the complete cap equation has exactly one regular
irreducible root in \(K\), then that root is the actual complete cap
character. If its ordered boundary representation determines the
auxiliary generator uniquely, the full complete representation is
also determined.

**Proof.** Develop one tetrahedron with vertices
\((\infty,0,1,z)\). All neighboring vertices and face maps are
obtained by rational Möbius operations over \(K\). Thus the
holonomy lies in \(\mathrm{PGL}_2(K)\), after one conjugation.

Let \(A\in\mathrm{GL}_2(K)\) represent a nonidentity parabolic.
Its discriminant satisfies \((\operatorname{tr}A)^2=4\det A\),
so its trace is nonzero. Multiplication by
\(2/\operatorname{tr}A\) gives its unique trace-\(2\) lift in
\(\mathrm{SL}_2(K)\). Therefore the trace of an ordered product
of original main meridians, including the cap parameter, lies in
\(K\). The exhaustive cap equation and the assumed uniqueness
select that parameter. The actual rational-word Hurwitz maps
then determine the whole boundary quadruple up to conjugacy.
The last hypothesis fixes the auxiliary generator. \(\square\)

This is a field-of-definition criterion, not an existence theorem
for positive triangulations or a statement about quantum
coefficients.

Apply it to \(K=\mathbb Q(X)\) from (5). The cap family and
the rational word are exactly those in Sections 1–2 of the
original collar proof. At the complete point its exhaustive
equation is
\[
            (z^2-5z+7)(z^3-3z^2+5z-2)=0.                     \tag{9}
\]
For completeness, the cap pair cannot share a fixed point:
otherwise all its rational-word images would share that point;
the nonidentity disk longitude and the auxiliary meridian
commuting with it would preserve it too. The whole complete
holonomy would be elementary. Likewise the output product
\(ba\) has trace \(-2\), not \(+2\): trace \(+2\) for two
trace-\(2\) parabolics forces a common fixed point, and (3)
would again make the complete group elementary. These facts
justify using the full equation (9).

The field \(K\) has degree three, so it cannot contain a root of
the irreducible quadratic factor. The cubic factor is irreducible
by the rational-root test and has discriminant \(-59\).
Its splitting field has degree six. If its degree-three root
field contained a second root, it would contain the third and
hence the splitting field, which is impossible. Its only root
in \(K\) is
\[
                             z=1+X^{-1}.                       \tag{10}
\]
The inverse relation \(X=(z-1)^{-1}\) proves that this is exactly
the same root field. The regularity checks in the original collar
proof apply unchanged to every displayed Newton denominator.

Finally, a solution \(\mu_0\) of (3) is unique near the complete
point. The quotient of two solutions centralizes both \(L\)
and \(c\). At completeness these are noncommuting parabolics;
their common projective centralizer is trivial. Noncommutation
persists nearby. The full actual complete pure holonomy therefore
is the source representation selected by (5) and (10).
No numerical cusp modulus or choice of a package peripheral basis
enters this selection.

## 4. The original pure geometric germ

Let \(u\) be the original free circle angle and \(w=e^{iu}\).
The rational word and leaf matching equations are unchanged:
\[
\begin{split}
 X^2Y-X&=(1-X)^3,\\
 (1-XY)(Y+w)(Y+w^{-1})&=(Y-1)^4.
\end{split}                                                     \tag{11}
\]
Here \(X,Y\) now denote their holomorphic values near the
selected complete solution. The marked leaf has
\[
 E=Y,\qquad T=\frac{wY+1}{Y+w},\qquad
 R=\frac{(Y+w)(wY+1)}{Y(w+1)^2}.
\]
The original pure peripheral words are \(\mu_0=S^{-1}\) and
\(L=W_2^{-1}W_0\). Their similarity multipliers are
\[
 e^{U_0}=T^{-1}=\frac{Y+w}{1+wY},\qquad e^V=w^2.                \tag{12}
\]
They are the same meridian and disk longitude derived in (2)–(3).
The logarithms vanish at completeness, so their continuous
branches satisfy
\[
                         U_0=-2\pi S'(u),\qquad V=2iu.          \tag{13}
\]
These are similarity logarithms, twice the selected eigenvalue
logarithms.

**Theorem 3.** The phase \(S(u)\) of the original mixed boundary
polynomial is the marked pure boundary potential of \(M_0\).
It has the original primitive periods (13), a compatible positive
ideal fundamental chain on a small disk about \(u=0\), and complete
main cusps. Its absolute complete value is (8).

**Proof.** The full rational-word matrices and (3) construct a
representation of the literal diagram for every nearby solution
of (11). Lemma 2 identifies its complete basepoint with
Proposition 1. The marked gluing-germ theorem therefore identifies
the family with the actual decorated geometric deformation.
Transport the finitely many complete flags and face maps of
(6)–(7): positivity and nondegeneracy persist on a sufficiently
small disk. The original main meridians remain parabolic, so their
commuting peripheral maps remain translations. Equations
(12)–(13) give the actual primitive logs, with zero constants.
Equation (8) supplies the absolute anchor. \(\square\)

The pure leaf still carries the original ordered two-triangle
reference interfaces. Their ratios are
\[
                  (-Q^{-1},-Q,-Q^{-1}),\qquad
                  (-Q,-Q^{-1},-Q),\qquad Q=e^{iu}.
\]
These are the leaf's complete triangle-map tables, not only
trace data. They persist in the marked deformation just
constructed. There is one further topological requirement for
using them in [the annular composition theorem](research_amplified_marked_block_geometry.md):
the two triangles must be identified with the original oval's
embedded twice-punctured disk, with its labelled sides.
The move certificate identifies the whole complements and their
complete geometry; it does not yet carry this particular embedded
disk through the moves. Matching its holonomy and primitive
boundary classes does not by itself prove that relative
identification.

This relative requirement is proved by
[straightening the original marked disk](research_marked_pants_seam_isotopy.md).
The argument constructs an embedded geodesic pants surface from
the disk's own based group, then uses Waldhausen's relative
surface theorem to obtain an ambient isotopy fixed on the cusp
boundary. Its two labelled triangles give the actual interface;
they need not be a specified pair of faces in the saved
triangulation. The isotopy preserves the original primitive
curves and their framing.

The mixed boundary theorem supplies its even phase, nonzero
holomorphic amplitude, whole-source bounds and
\[
                       S''(0)=-\frac{\tan(\pi y_*)}{2\pi},
                       \qquad \Re\tan(\pi y_*)>0.
\]
Together with the relative disk theorem, these establish all
the required properties for including this block and its mirror
in a fixed finite library of pendant pieces. Its outside circle
keeps one primitive longitude and receives its original carrier
only once. The resulting compositions still have to satisfy
the applicable analytic closure hypotheses and the original
component test. This does not supply a new asymptotic theorem
for an arbitrary rational word or make this one-boundary
pendant polynomial into a two-boundary internal kernel.

## 5. Reproduction

Run
~~~bash
.venv/bin/python experiments/verify_mixed_pure_carrier_subdivision.py
~~~
The [fixed data](../repro/fixtures/research-mixed-pure-carrier-subdivision.json)
contain the literal PD code, every intermediate move, both final
relabellings and the nine shape coefficients. The
[verifier](../experiments/verify_mixed_pure_carrier_subdivision.py)
contains no search or numerical hyperbolic solve. Its
[result](../repro/results/research-mixed-pure-carrier-subdivision.json)
records hashes of the verifier and fixture; use
\(\texttt{--output path}\) to save an independent replay separately.
A separate [replay output](../repro/results/research-mixed-pure-carrier-subdivision-root.json)
records the same verifier and fixture hashes.

