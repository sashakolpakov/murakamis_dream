# The original cells at square-corner degenerations

Research note, 2 November 2026. The square coordinates in
[the convex variational formulation](research_positive_filling_convex_variation.md)
describe positive original edge geometry. Their boundary minima
need not describe a limit of that geometry with the dual lengths
chosen by the constrained optimization problem.

This note classifies the finite geometric corner limits, including
an edge with only one corner square. It then records two
obstructions to treating every corner as an existing zero or
unit-power tangle reduction. The exact powers \((2,-2)\) already
give a corner minimum whose dual lengths are not original
geometric periods.

## 1. Each square controls four of the original tetrahedra

Keep the original ordered tetrahedron shapes

\[
        (A,B,-1/A,-1/B),\qquad(C,D,-1/C,-1/D).
 \tag{1}
\]

Use the strip coordinates \(P,Q\), disk coordinates
\(\zeta=\tanh P,\xi=\tanh Q\), and
\(f(P)=\arctan(\tanh P)\) from
[the positive-period theorem](research_positive_edge_global_monotonicity.md).
The shape formulas simplify to

\[
 \begin{aligned}
 C&=i e^{-2P},&
 B&=i e^{2if(P)}=\frac{C-1}{C+1},\\
 A&=i e^{2Q},&
 D&=i e^{2if(Q)}=\frac{A+1}{1-A}.
 \end{aligned}
 \tag{2}
\]

For example, substituting
\[
 q=\frac{1+\zeta\xi}{1-\zeta\xi},\quad
 a=\frac{\zeta+\xi}{1-\zeta\xi},\quad
 b=\frac{\zeta-\xi}{i(1-\zeta\xi)}
\]
in \(C=(q-a)/(b-i)\) gives \(i(1-\zeta)/(1+\zeta)\).
Substitution in \(B=-(q-b)/(a+i)\) gives
\(i(1+i\zeta)/(1-i\zeta)\). Eliminating \(\zeta\)
between these two expressions gives the first real Möbius
relation in (2). The calculation with \(\xi\) gives the
second.

Thus the \(P\) square controls \(B,C,-1/B,-1/C\), and the
\(Q\) square controls \(A,D,-1/A,-1/D\). These groups are
interleaved between the two original octahedra. They are
not the two original octahedra taken separately.

## 2. Finite geometric limits at one corner

Write

\[
 P=x+iy,\qquad f(P)=\alpha+i\beta.
 \tag{3}
\]

A corner of the square has

\[
        \alpha=\epsilon_\alpha\frac{\pi}{4},\qquad
        y=\epsilon_y\frac{\pi}{4},\qquad
        \epsilon_\alpha,\epsilon_y\in\{-1,1\}.
 \tag{4}
\]

Consider a finite geometric limit in which
\(\zeta\) tends to the unit circle away from
\(1,-1,i,-i\). Both \(x\) and \(\beta\) then have finite
nonzero limits. The square inverse gives

\[
 \epsilon_\alpha x=X>0,\qquad
 \epsilon_y\beta=Y>0,\qquad
                  \sinh(2X)\sinh(2Y)=1.
 \tag{5}
\]

Equivalently, for a unique \(r>0\),

\[
                   X=\frac12\operatorname{arsinh}r,\qquad
                   Y=\frac12\operatorname{arsinh}(1/r).
 \tag{6}
\]

One proof is to approach the corner along
\(\alpha=\epsilon_\alpha(\pi/4-as)\),
\(y=\epsilon_y(\pi/4-bs)\), \(a,b>0\), and use the
square inverse: \(r=b/a\). Conversely, (6) gives
\[
 \zeta=\tanh(2x)+i\epsilon_y\operatorname{sech}(2x),
\]
which lies on the unit circle away from the four excluded
points and has exactly the stated corner values and
complementary coordinate \(\beta\). Thus (5) is the
entire finite geometric boundary, not just one chosen path.

At this limit the two basic shapes are real:

\[
                   C=\epsilon_y e^{-2x},\qquad
                   B=-\epsilon_\alpha e^{-2\beta}.
 \tag{7}
\]

Their possible intervals are:

| \((\epsilon_\alpha,\epsilon_y)\) | \(C\) | \(B\) |
|---|---|---|
| \((+,+)\) | \((0,1)\) | \((-1,0)\) |
| \((+,-)\) | \((-1,0)\) | \((-\infty,-1)\) |
| \((-,+)\) | \((1,\infty)\) | \((0,1)\) |
| \((-,-)\) | \((-\infty,-1)\) | \((1,\infty)\) |

In every row the relation \(B=(C-1)/(C+1)\) is retained.
None of these finite shapes is \(0,1,\infty\).
The four tetrahedra belonging to \(P\) are flat, while
their distinct vertices remain distinct within each
tetrahedron.

If \(Q\) remains interior, its four tetrahedra remain
positive. Moreover the full original face chart remains
regular. Indeed \(|\xi|<1\), \(|\zeta|=1\), with
\(\zeta\notin\{1,-1,i,-i\}\), imply
\(|\zeta\xi|<1\) and \(\Re q>0\).
The factors \(1\pm\zeta,1\pm i\zeta\) and their \(\xi\)
counterparts are nonzero. Hence \(a\pm i,b\pm i,q\pm a,
q\pm b,q,q\pm i\) are nonzero. The apex denominator
factorizations in Section 3 of the positive-period note
then show that no additional singularity has appeared.

The description for a \(Q\)-corner is the same after
interchanging the roles of the two squares. With
\(Q=x+iy\), its real shapes are
\[
                    A=-\epsilon_y e^{2x},\qquad
                    D=-\epsilon_\alpha e^{-2\beta},
\]
and still satisfy \(D=(A+1)/(1-A)\).

## 3. Two corners and the original chart boundary

If both squares have finite geometric corner limits, all
eight shapes in (1) are real. Put \(w=\zeta\xi\), so
\(|w|=1\).

If \(w\ne1\), then
\[
                         q=\frac{1+w}{1-w}
\]
is purely imaginary, and the same is true of \(a,b\).
The canonical real parts of \(t,u\) can be \(0\) or
\(\pm\pi\), as follows directly from the two corner signs
in their strip formulas. Some special products require
separate treatment:

- \(w=-1\) gives \(q=0\), the ramification locus of the
  original square root.
- \(w=i\) or \(-i\) gives \(q=i\) or \(-i\); the original
  equatorial and apex denominators \(q^2+1\) or \(q\mp i\)
  vanish.
- \(w=1\) makes (15) of the positive-period note singular;
  the original tangent coordinates diverge.

These are singularities of the original chart even when
the individual limiting shape expressions (2) are finite.
They cannot be dismissed by checking only those expressions.

The regular imaginary fold is the particular case
\(\xi=-1/\zeta=-\overline\zeta\). Then
\[
 P=x+i\epsilon_y\pi/4,\qquad
 Q=-x+i\epsilon_y\pi/4,\qquad
 f(P)=\epsilon_\alpha\pi/4+i\beta,\qquad
 f(Q)=-\epsilon_\alpha\pi/4+i\beta,
\]
and therefore
\[
                    t=4i\beta,\qquad u=-4ix,\qquad q=0.
 \tag{8}
\]

For \(\epsilon_\alpha=1,\epsilon_y=-1\), both core
coordinates have negative imaginary parts. Their positive
heights \(h=-\Im t\), \(g=-\Im u\) obey
\[
                         \sinh(h/2)\sinh(g/2)=1.
 \tag{9}
\]

This is the regular-edge boundary in the zero-subtree
geometry. The trivalent zero-pair example is one instance.
General one-corner limits are different: four tetrahedra
can remain positive and the full face chart can remain
regular.

## 4. A convex subgradient need not be a geometric limit

The full corner subdifferential is proved in
[the corner KKT note](research_positive_filling_corner_kkt.md).
At the corner (4), its finite vectors \((x,\beta)\) satisfy

\[
 \epsilon_\alpha x=X>0,\qquad
 \epsilon_y\beta=Y>0,\qquad
                       \sinh(2X)\sinh(2Y)\ge1.
 \tag{10}
\]

Equality is the geometric boundary (5). Strict inequality
does not describe any finite boundary point of the original
disk factor. For instance, inserting such \(x,\beta\) into
(7) fails the exact original relation
\(B=(C-1)/(C+1)\).

This is a local algebraic obstruction, not merely a failure
of a positivity estimate. The imaginary matching and real
filling multipliers at a corner minimum may use (10) with
strict inequality. In that case their values must not be
reported as the periods of the original degenerate shapes.

### The original signed pair \((2,-2)\)

Consider the original path
\[
                        b-v-w-b',
\]
with complete outside vertices \(b,b'\). The two selected
vertices have degree two, unit charges, and powers \(2,-2\).
Put
\[
                    u_0=\frac12\operatorname{arsinh}\sqrt3.
\]

The KKT note proves that the unique closed-polytope minimum
has one internal corner square
\((\alpha_P,y_P)=(\pi/4,-\pi/4)\), the other square at
\((0,0)\), and corner subgradient \((u_0,-u_0)\).
Its subgradient inequality is strict:
\[
                       \sinh(2u_0)^2=3>1.
 \tag{11}
\]

The resulting dual angle coordinates are
\[
         t_v=\pi/2-2iu_0,\qquad t_w=-\pi/2-2iu_0.
 \tag{12}
\]

Here is a direct check of what happens if one attempts to
interpret (12) as original edge geometry. The actual
tangents and square root satisfy
\[
 a=\frac{1-i\sqrt3}{2},\qquad
 b=\frac{-1-i\sqrt3}{2},\qquad
                           1+a^2+b^2=0.
 \tag{13}
\]

At \(q=0\), the rational shape expressions give
\[
 \begin{aligned}
 A&=\frac{\sqrt3-1}{2}(1+i),& C&=-A,\\
 B&=-\frac{\sqrt3+1}{2}(1+i),& D&=-B.
 \end{aligned}
 \tag{14}
\]

Thus the shapes have opposite orientations in pairs.
They are not the four-flat, four-positive shapes of a
finite one-corner geometric limit. The original square-root
chart is singular as well. Equations (13)--(14) exhibit
the distinction between the convex dual variables and
actual continued original periods.

Neither selected power in this example is \(0,1,-1\).
The established literal zero and unit-power vertex moves
therefore do not apply directly at either selected vertex.
This does not rule out a longer marked rational-tangle
identity or a different geometric subdivision.

## 5. A limitation of collapsing the pair by integral shifts

There is also a precise obstruction to a particularly
simple marked replacement. Use the pillowcase lifts in
[the degree-two tangle-move proof](research_marked_degree_two_tangle_moves.md).
On the homology of the double cover their linear parts are
\[
 T=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
 A_n=\begin{pmatrix}1&n\\0&1\end{pmatrix}.
 \tag{15}
\]

Affine translations retain endpoint markings but do not
alter these matrices. The two selected vertices occur
between their outside attachments with word
\[
                  W=T A_2 T A_{-2}T
                    =\begin{pmatrix}2&1\\-5&-2\end{pmatrix}.
 \tag{16}
\]

A one-middle-vertex replacement with integral changes at
the two outside attachments would have linear word
\[
 A_r T A_m T A_s
   =\begin{pmatrix}
      rm-1&s(rm-1)-r\\
      m&ms-1
     \end{pmatrix},\qquad r,m,s\in\mathbb Z.
 \tag{17}
\]

The proper half-turns retained in the existing moves have
projectively trivial linear parts, so they do not affect
this comparison. Equality of the marked boundary
operations would require (17) to equal \(W\) or \(-W\).
In the first case \(m=-5\) and \(rm=3\), which has no
integer solution. In the second case \(m=5\) and \(rm=-1\),
also impossible.

A replacement with no middle vertex has linear word
\(A_r T A_s\), whose lower-left entry is \(1\), or \(-1\)
after the deck involution, and is also excluded.
These matrix obstructions apply to universal substitutions
with arbitrary attached tangles: rational test tangles
detect different actions on the slopes of the double cover.

Thus this pair cannot be collapsed by the same kind of
integral outside shifts and retained half-turns that remove
a single zero or unit-power vertex. Allowing a more general
boundary mapping class changes the problem and requires
its own marking and peripheral calculation.

## 6. Two positive shapes supplied by the exact crossing phase

The crossing expansion gives a possible interface to a new
subdivision, but its geometric normalization must be kept
straight. Use the exact turned crossing phase from
[the Newton source-transport note](research_corner_newton_source_transport.md):
\[
 F_\sigma(x,y)=J(x)-J(y)-J(x-y)
             +\sigma i\pi(1/2+x+xy),\qquad 0<y<x<1.
 \tag{18}
\]
Here \(\sigma=\pm1\), \(x\) is its incoming Newton index,
and \(y\) its outgoing index. Define
\[
 X=e^{2\pi ix},\qquad Y=e^{2\pi iy},\qquad
 U_\sigma=e^{(F_\sigma)_x},\qquad
 V_\sigma=e^{-(F_\sigma)_y}.
\]

For the positive sign these rational functions are
\[
 U_+=\frac{Y(1-X)}{X-Y},\qquad
 V_+=\frac{Y-1}{X-Y},
 \tag{19}
\]
with \(XV_++U_++1=0\) and \(Y(V_++1)+U_+=0\).
The negative sign gives
\[
                   U_-=U_+/Y,\qquad V_-=XV_+.
\]

These derivative conventions agree with the symbols in
Section 7 of
[the original Newton canonical-graph note](actual_newton_twist_canonical_graph.md).
There is an important transpose in applying them here.
That note treats \(x\) as the output index of the original
crossing matrix. The turned operator used in (18) is its
transpose. With \(x\) incoming and \(y\) outgoing, its
input momentum is \(U_\sigma^{-1}\) and its output
momentum is \(V_\sigma^{-1}\). A geometric boundary
identification must retain this reversal.

The rational pre-Bloch symbol of the phase is
\[
                     \beta=-[X]+[Y]+[X/Y].
 \tag{20}
\]

**Proposition 1.** In the rational pre-Bloch group, at
regular values of these arguments,
\[
 \beta=[-U_+]+[-V_+]
      =[-1/U_-]+[-1/V_-].
 \tag{21}
\]

**Proof.** The five-term relation gives
\[
 [X]-[Y]+[Y/X]
 -\left[\frac{1-X^{-1}}{1-Y^{-1}}\right]
 +\left[\frac{1-X}{1-Y}\right]=0.
\]
Using \([z^{-1}]=-[z]\), put
\[
 a_0=\frac{1-X^{-1}}{1-Y^{-1}}
                    =\frac{U_+}{U_++1},\qquad
 b_0=\frac{1-X}{1-Y}=1+\frac1{V_+}.
\]
Then \(\beta=-[a_0]+[b_0]\).
The usual oriented tetrahedron relations
\([z/(z-1)]=-[z]\) and \([1-1/z]=[z]\)
give the first equality in (21).

Substitution of \(X^{-1},Y^{-1}\) in (19) gives
\(U_-,V_-\). The corresponding symbol is \(-\beta\),
again by the inversion relation. Applying the first
equality there and then inverting its two arguments
gives the second equality. \(\square\)

On the strict real triangle both shapes in the first
expression are positive:
\[
 \begin{aligned}
 -U_+&=
   e^{i\pi y}\frac{\sin\pi x}{\sin\pi(x-y)},\\
 -V_+&=
   e^{i\pi(1-x)}\frac{\sin\pi y}{\sin\pi(x-y)}.
 \end{aligned}
 \tag{22}
\]
Their arguments lie in \((0,\pi)\). Also
\(-U_+=1-\overline{(-V_+)}\).
The tetrahedron with shape \(-V_+\) has angles
\(\pi(1-x),\pi y,\pi(x-y)\), hence volume
\(\pi\{J(x)-J(y)-J(x-y)\}\). The other tetrahedron
has the same volume. For the negative sign,
\(U_-=\overline{U_+}\) and
\(V_-=\overline{V_+}\) on this triangle; the reciprocal
conjugate shapes in (21) are positive and have the
same respective volumes.

Consequently the crossing regulator has a positive
two-tetrahedron expression on this real triangle, with
total volume \(2\pi\Re F_\sigma\). Using only the single
tetrahedron whose volume is \(\pi\Re F_\sigma\) would
miss a factor of two.

This calculation shows that either crossing sign can
supply locally positive oriented shapes. Mixed signs
alone are therefore not a local orientation obstruction.
It does not yet show that these two tetrahedra form
the required marked layer, attach to the original
zero-subtree faces, or remain positive at the stationary
point of an assembled complex source.

The identity (21) is rational and forgets possible
torsion, flattenings, and logarithmic constants. The
finite crossing scalar, imaginary quadratic phase,
first normal derivatives, and original boundary
markings remain those of the exact source. A rational
Bloch identity does not replace their verification.

## 7. What a replacement still has to establish

The classification separates three situations:

1. A finite one-corner geometric limit has four flat and
   four positive original tetrahedra, with a regular
   original face chart.
2. A finite two-corner limit has eight flat tetrahedra,
   and can also reach singular equatorial, apex, or
   square-root coordinates.
3. A strict corner subgradient is not a limit of its
   original disk factor with the claimed complementary
   lengths. It cannot be repaired by merely relabeling
   those shapes.

A geometric replacement must retain the original external
boundary data and specify its face maps and primitive
curves. If it uses a new decomposition, its internal
variables must be solved again; the old corner multipliers
are not automatically its geometric periods. An exact
finite source transformation likewise needs a separate
argument before its coherent asymptotic contribution is
identified.

The already proved zero-subtree replacement meets these
requirements in its stated class. No universal replacement
for the mixed one-corner configurations or the \((2,-2)\)
pair is proved here. The companion
[Newton source-transport note](research_corner_newton_source_transport.md)
records exact algebraic changes of boundary representation;
those identities alone do not supply the missing positive
geometry or asymptotic contribution.
