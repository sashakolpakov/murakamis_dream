# The Newton crossing on the actual Conway meridian flags

Research note, 2 November 2026. The Newton crossing phase has a
two-tetrahedron Bloch expression. Here we identify its four
parabolic meridians with the original Conway white-transition
matrices and exhibit the tetrahedra using their actual fixed
points. This gives a marked representation calculation and an
oriented local chain. It does not yet identify that chain with
the entire boundary of a crossing mapping cylinder.

## 1. Coordinates and the crossing convention

The original Newton crossing has the canonical equations
\[
 X=Y+\frac{Y-1}{V},\qquad U=-Y(1+V).
 \tag{1}
\]
Here \((Y,V)\) are input clock and momentum, and \((X,U)\)
are output clock and momentum for the original lower triangular
crossing matrix. They are fixed by its exact finite difference
equations in
[the original canonical-graph calculation](actual_newton_twist_canonical_graph.md),
Sections 1--4. In particular, they are not inferred from an
unmarked four-punctured-sphere character variety.

Its trace functions are
\[
 \begin{aligned}
 A&=Y+Y^{-1}+(Y+Y^{-1}-2)V^{-1},\\
 B&=Y+Y^{-1}+(Y+Y^{-1}-2)V,\\
 C&=2-(Y-1)^2(V+1)^2/V.
 \end{aligned}
 \tag{2}
\]
The active crossing sends
\[
                 (A,B,C)\longmapsto(A,C,8-AC-B).
 \tag{3}
\]
The transpose used when a crossing acts on a turned boundary
leg reverses input and output. Thus for the phase
\[
 F(x,y)=J(x)-J(y)-J(x-y)+i\pi(xy+x+1/2)
\]
with \(x\) incoming and \(y\) outgoing in that transpose,
the incoming and outgoing momenta are respectively
\(e^{-F_x}\) and \(e^{F_y}\). Formula (1) uses the original
matrix convention, with \(x\) outgoing and \(y\) incoming.
Both conventions refer to the same exact matrix and must
not be interchanged silently.

All calculations below take place on the regular open set
where the displayed denominators and the tetrahedron
shape differences are nonzero. They are rational identities
there and extend wherever their matrix representatives are
regular.

## 2. An explicit parabolic quadruple

Set
\[
 z=\frac{(V+1)(Y-1)^2}{VY},\qquad
 p=\frac{V}{(V+1)(Y-1)},\qquad d=\frac1{Y-1},
 \qquad h=\frac{(V+1)^2(Y-1)^2}{V}.
 \tag{4}
\]
The letter \(d\) denotes a fixed point in this note, not
the quantum degree \(N-1\).
Define the determinant-one, trace-two matrices
\[
 a=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
 b=\begin{pmatrix}1&0\\z&1\end{pmatrix},\quad
 c=\begin{pmatrix}1-hp&hp^2\\-h&1+hp\end{pmatrix},\quad
 d_{\rm mat}=(cba)^{-1}.
 \tag{5}
\]
Their fixed points, in the same order, are
\[
                            \infty,\quad0,\quad p,\quad d.
 \tag{6}
\]
For the last assertion, direct multiplication gives
\[
 d_{\rm mat}=
 \begin{pmatrix}
 1+(V+1)(Y-1)/Y&-(V+1)/Y\\
 (V+1)(Y-1)^2/Y&1-(V+1)(Y-1)/Y
 \end{pmatrix}.
 \tag{7}
\]
Substitution of \(d=(Y-1)^{-1}\) verifies its fixed-point
equation. Thus
\[
 d_{\rm mat}cba=I,\qquad
 \operatorname{tr}(ab)=A,\quad
 \operatorname{tr}(bc)=B,\quad
 \operatorname{tr}(ac)=C.
 \tag{8}
\]
Every lift and product order in (5)--(8) is specified.

The positive Hurwitz move in these conventions is
\[
 (a,b,c,d_{\rm mat})
       \longmapsto(a^{-1}ba,\ a,\ c,\ d_{\rm mat}).
 \tag{9}
\]
It preserves the reverse product relation in (8).
The first fixed point moves from \(0\) to \(-1\);
the four new fixed points are
\[
                             -1,\quad\infty,\quad p,\quad d.
 \tag{10}
\]
This is the convention \(c_{\rm under}=a^{-1}ba\) used
by the actual crossing in
[the fundamental-chain calculation](crossing_fundamental_cycle.md).
It also induces exactly (3), fixing its sign relative
to the original Newton matrix.

The output normalization is the Möbius transformation
\[
                N_{\rm out}(w)=\frac1{z(w+1)},\qquad
                N_{\rm out}=
                     \begin{pmatrix}0&1\\z&z\end{pmatrix}.
 \tag{11}
\]
It sends the new first two flags to \(\infty,0\) and
conjugates their matrices to \(a,b\) in the same
normalization. More precisely,
\[
 N_{\rm out}(a^{-1}ba,\ a,\ c,\ d_{\rm mat})
        N_{\rm out}^{-1}
          =(a,b,c,d_{\rm mat})\big|_{(Y,V)=(X,U)}.
 \tag{12}
\]
This includes all four matrices, not just their traces.
For their last two flags it says explicitly
\[
 \frac1{z(p+1)}
       =\frac{U}{(U+1)(X-1)},\qquad
 \frac1{z(d+1)}=\frac1{X-1}.
 \tag{13}
\]
Equations (12)--(13) follow by substitution of (1).

## 3. Identification with the original white matrices

The marked Conway deformation uses the four projective
white or completion transitions
\[
 \begin{aligned}
 W_0&=\begin{pmatrix}1&0\\0&E\end{pmatrix},&
 W_1&=\begin{pmatrix}1&E-1\\0&E\end{pmatrix},\\
 W_2&=\begin{pmatrix}E-R&R(1-E)\\E-1&1-ER\end{pmatrix},&
 W_3&=\begin{pmatrix}R&0\\1-E&ER\end{pmatrix}.
 \end{aligned}
 \tag{14}
\]
These are the actual matrices in
[the geometric deformation proof](../papers/strict-conway-geometry/deformation.tex).
After the expression is assembled, every completion
matrix is supplied by the adjacent actual white face.
The main meridian at the \(j\)-th corner is
\(W_{j-1}^{-1}W_j\), or its inverse according to its
orientation.

Normalize these quotients to trace two, and call them
\(P_j\), with cyclic indices. Direct calculation gives
\[
 \begin{aligned}
 P_0&=\begin{pmatrix}1&0\\(E-1)/(ER)&1\end{pmatrix},&
 P_1&=\begin{pmatrix}1&E-1\\0&1\end{pmatrix},\\
 P_2&=\frac1{E(R-1)}
       \begin{pmatrix}ER-2E+1&E-1\\1-E&ER-1\end{pmatrix},&
 P_3&=\begin{pmatrix}
 (E+R-2)/(R-1)&-R(E-1)/(R-1)\\
 (E-1)/(R(R-1))&(R-E)/(R-1)
 \end{pmatrix}.
 \end{aligned}
 \tag{15}
\]
Their fixed points are \(0,\infty,1,R\), respectively,
and \(P_0P_1P_2P_3=I\). In particular the based tuple
\[
 (a_{\rm geo},b_{\rm geo},c_{\rm geo},d_{\rm geo})
             =(P_1^{-1},P_2^{-1},P_3^{-1},P_0^{-1})
 \tag{16}
\]
has the reverse product relation of (8) and fixed flags
\((\infty,1,R,0)\).

**Proposition 1.** The actual geometric tuple (16) is
the tuple (5) in the coordinates
\[
                     Y=E,\qquad V=\frac{1-R}{R}.
 \tag{17}
\]
The full conjugating map is
\[
                    N_{\rm in}(w)=\frac{w-1}{1-E}.
 \tag{18}
\]

**Proof.** The map (18) sends the four geometric flags
to
\[
 \left(\infty,0,\frac{1-R}{E-1},\frac1{E-1}\right),
\]
which are exactly (6) after (17). It sends
\(a_{\rm geo}\) to the translation \(w\mapsto w+1\);
it sends \(b_{\rm geo}\) to the lower unipotent with
entry
\[
                 \frac{(E-1)^2}{E(1-R)}
                      =\frac{(V+1)(Y-1)^2}{VY}=z.
\]
Multiplying the remaining matrices in (15) gives
exactly \(c,d_{\rm mat}\) in (5),(7). Thus the fixed
flags and the parabolic translation scales agree
simultaneously. \(\square\)

This is also the dictionary supplied by the original
boundary phase. For
\[
 g(a_0,\chi)=J(2a_0)-2J(a_0)
              -J(a_0-\chi)-J(a_0+\chi),
\]
the geometric parameters satisfy
\[
 E=e^{2\pi ia_0},\qquad
 R=\frac{\cos^2(\pi a_0)}{\cos^2(\pi\chi)}.
 \tag{19}
\]
Differentiating \(g\) gives
\[
 e^{-g_{a_0}}
 =\frac{\sin\pi(a_0-\chi)\sin\pi(a_0+\chi)}
        {\cos^2(\pi a_0)}
 =\frac{1-R}{R}.
 \tag{20}
\]
The Newton leaf action is the stationary value of
\(g+i\chi u\), so its \(a_0\)-derivative is \(g_{a_0}\).
Therefore (17) is the actual incoming clock and
momentum, including the minus sign in the incoming
momentum derivative.

Combining (12) and Proposition 1 gives explicit
conjugacies for every step of an arbitrary rational
crossing word on its regular representation chart.
One must retain the known transpose when the word
acts on a turned boundary leg. The calculation
does not replace the original finite matrix or its
first normal derivatives.

## 4. Two tetrahedra on these actual flags

Use the geometric shape convention
\[
 w(v_0,v_1,v_2,v_3)
   =\frac{(v_3-v_0)(v_2-v_1)}
          {(v_3-v_1)(v_2-v_0)},\qquad
 w(0,\infty,1,z)=z.
 \tag{21}
\]
The reciprocal convention in the fundamental-chain
note uses the opposite order of the first two
vertices. This order is relevant to the following
orientation calculation.

Consider the ordered tetrahedra
\[
       T_{\rm in}=(p,\infty,d,0),\qquad
       T_{\rm out}=(p,-1,d,\infty).
 \tag{22}
\]
Their shapes are
\[
 w(T_{\rm in})=-\frac{p}{d-p}=-V,\qquad
 w(T_{\rm out})=\frac{d+1}{d-p}=-U.
 \tag{23}
\]
Thus the earlier two-shape Bloch expression uses
the actual meridian flags on the two sides of
the Hurwitz crossing.

The common face has opposite boundary orientations.
Indeed
\[
 \begin{aligned}
 \partial T_{\rm in}
   &=(\infty,d,0)-(p,d,0)+(p,\infty,0)-(p,\infty,d),\\
 \partial T_{\rm out}
   &=(-1,d,\infty)-(p,d,\infty)
                        +(p,-1,\infty)-(p,-1,d).
 \end{aligned}
 \tag{24}
\]
Since \(-(p,\infty,d)=(p,d,\infty)\), these two
terms cancel. The abstract union is an oriented
two-tetrahedron ball with five vertices and the
six remaining boundary faces in (24). Its
developing data are the five explicit flags
\(\{p,\infty,d,0,-1\}\).

On the real Newton triangle \(0<y<x<1\), both
shapes in (23) have positive imaginary part:
\[
 -U=e^{i\pi y}\frac{\sin\pi x}{\sin\pi(x-y)},\qquad
 -V=e^{i\pi(1-x)}\frac{\sin\pi y}{\sin\pi(x-y)}.
 \tag{25}
\]
Their total volume is
\[
            D(-U)+D(-V)
                =2\pi\{J(x)-J(y)-J(x-y)\}.
 \tag{26}
\]
Here \(D\) is the Bloch--Wigner function.
The angle and five-term proof of (26), including
the negative-crossing inverse-conjugate shapes,
is in Section 6 of
[the corner geometry note](research_square_corner_flat_geometry.md).
The present calculation adds the actual ordered
fixed points and their parabolic matrices.

## 5. The attachment still required

The subsequent
[two-flip attachment](research_newton_crossing_two_flip_attachment.md)
provides the face table and auxiliary peripheral transport
when the interface has four actual white sides. The
qualification is essential: the original geometric
paper does not identify a general intermediate
quadrilateral with a physical four-punctured boundary.
Masked outputs still require an additional construction.
The statements in this section describe the scope of
the flag calculation by itself.

The identities prove three concrete facts:

1. The Newton canonical crossing and the original
   Conway main meridians agree at the level of all
   four matrices and their fixed flags.
2. Its two Bloch shapes are developed on those
   flags and join along an explicitly cancelling
   triangular face.
3. The exact input and output normalizations are
   the maps (18) and (11), so this comparison can
   be propagated through a regular crossing word.

They do not yet prove that the six remaining faces
in (24) are the required faces of the entire
crossing mapping cylinder. In particular, the
calculation does not specify every additional
face identification with a zero-subtree cell,
or the transport of an auxiliary disk longitude
and its transverse primitive meridian through
that identification. The main-meridian flags
alone do not determine those auxiliary curves.

Consequently this note does not assert a positive
triangulation of an arbitrary signed crossing
chain or of the folded \((2,-2)\) example. That
would require a full attachment table and a
solution of its geometric gluing equations.
The finite source, its normal derivatives and
its logarithmic constants likewise remain the
original ones; the rational Bloch relation
does not certify their asymptotic contribution.

The rational matrix identities and the face cancellation
can be replayed with

~~~sh
python3 experiments/verify_newton_crossing_marked_flags.py
~~~

The script uses exact rational simplification over
\(\mathbb Q(E,R,Y,V)\). Its
[saved result](../repro/results/research-newton-crossing-marked-flags.json)
records the identities checked and the six exterior
triangles. These checks have the same local scope
as the rational propositions. The extended script
also checks all four white transitions in the
two-flip table; it does not test a masked-interface
replacement or a geometric stationary point.
