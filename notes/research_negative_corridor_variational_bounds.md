# Variational bounds for a corridor with negative powers

The uniform-sign rational normal form reduces every fixed rational
corridor to a negative chain, with its end twists and physical rotations
retained. This note studies the convex geometric problem for such a chain.
It proves strict feasibility, bounds on the real angle coordinates and
dual lengths, and a precise description of the possible remaining corners.
Its main conclusion, Theorem 15, proves interiority whenever every
selected crossing magnitude is an integer at least three, independently of the
length of the path. The proof first confines a possible corner to
an adjacent pair of magnitudes three and four or five. It then
excludes those two cases by a finite exact rational interval
certificate using both endpoints' real and imaginary period equations.
The earlier theorems record the intermediate bounds and their
elementary proofs.
Interiority for all magnitudes at least two remains unproved.
The [pointwise marked completion](research_positive_point_marked_completion.md)
now identifies that explicit positive class with the actual original
hyperbolic fillings and supplies the absolute volume through
[the positive-edge volume identity](research_positive_edge_volume_identity.md).
No quantum asymptotic is inferred.

In particular, a tempting stronger sign assertion is false: a positive
negative-power corridor can have a positive internal incidence. Section 7
gives an explicit asymptotic counterexample to that assertion.

## 1. The path and the convex problem

Let the selected vertices form a nonempty finite path. Their original
degrees are at most two. At least one end of the path has an edge to a
complete outside vertex. Thus the setup includes a corridor with two
outside ends and a pendant path with one outside end. It excludes a
closed component with no outside end.

At each selected vertex \(v\), take the original integer power
\(n_v=-b_v\), where \(b_v\in\mathbb Z\), \(b_v\ge2\), and unit filling charge.
Every outside angle is zero. Use the coordinates of the
[convex filling variation](research_positive_filling_convex_variation.md):
\(s_v\) is the real part of the boundary angle, and \(g_{v,e}\)
is the imaginary part of the return at the incidence \((v,e)\).
At a corner these are still primal variables, but the lengths and
real returns obtained below are only dual variables until an actual
shape interpretation is established.

The filling constraints and closed edge inequalities are
\[
 \sum_{e\ni v}g_{v,e}+\frac{b_v}{2}s_v=-\pi,\qquad
 |s_v|+2|g_{w,e}|\le\pi,\quad
 |s_w|+2|g_{v,e}|\le\pi
 \quad(e=\{v,w\}).
 \tag{1}
\]
An outside \(s_w\) is zero. The incidence at the outside endpoint
is retained as a variable; its prescribed imaginary angle is zero.

For an oriented edge \(e=(v,w)\), set
\[
 \begin{split}
 A_P&=s_v/4-g_{w,e}/2,& A_Q&=s_v/4+g_{w,e}/2,\\
 y_P&=g_{v,e}/2+s_w/4,& y_Q&=g_{v,e}/2-s_w/4.
 \end{split}
 \tag{2}
\]
Each pair \((A,y)\) lies in the closed square
\([-\pi/4,\pi/4]^2\).
The square energy \(E\) is normalized by \(E(0,0)=0\), with
\[
 E_A=x=\frac12\operatorname{arsinh}(\tan(2A)\cos(2y)),
 \qquad
 E_y=B=\frac12\operatorname{arsinh}(\tan(2y)\cos(2A)).
 \tag{3}
\]
It is even in each coordinate, strictly convex in the open square,
and continuous on the closed square. The total energy is
\[
                   \mathcal E=4\sum_e(E_P+E_Q).
 \tag{4}
\]

We use the proved
[corner optimality criterion](research_positive_filling_corner_kkt.md).
At a minimum with a strictly feasible comparison point, no square
can lie on an open side. An interior square uses (3); a corner
\((\epsilon_A\pi/4,\epsilon_y\pi/4)\) has a finite subgradient
\((x,B)\) exactly when
\[
 U=\epsilon_Ax>0,\qquad V=\epsilon_yB>0,\qquad
                         \sinh(2U)\sinh(2V)\ge1.
 \tag{5}
\]
For the two square covectors of an edge, define
\[
 \begin{split}
 h_{v,e}&=2(B_P+B_Q),&h_{w,e}&=-2(x_P-x_Q),\\
 k_{v,e}&=x_P+x_Q,&k_{w,e}&=B_P-B_Q.
 \end{split}
 \tag{6}
\]
At a minimum one can choose these covectors so that
\[
 h_{v,e}=h_v,\qquad h_{w,e}=0\ \text{at an outside endpoint},
 \qquad
                 \sum_{e\ni v}k_{v,e}=\frac{b_v}{2}h_v.
 \tag{7}
\]
Strict inequality in (5) is not the limit of an ordinary geometric
gradient along a fixed inward ray. None of the assertions about
dual variables below changes that distinction.

## 2. Strict feasibility

**Proposition 1.** The constraints (1) have a strictly feasible point.
Consequently their closed convex problem has a unique minimum and
the corner conditions (5)--(7) apply there.

**Proof.** Let \(Q\) be the matrix with diagonal entries \(b_v\) and
off-diagonal entries minus one along the selected path. The exact
sum-of-squares identity in
[the rational normal form](research_definite_rational_corridor_normal_form.md),
equation (30), proves that \(Q\) is positive definite.
Its inverse has strictly positive entries. One elementary proof
is the discrete maximum principle: a negative minimum of a solution
of \(Qz\ge0\) propagates through every row with equality in diagonal
dominance and reaches an endpoint row, where the inequality is
strict. This is impossible. Applying the same propagation to a
zero entry of \(Q^{-1}e_j\) proves strict positivity.

Write \(d_v\) for the original degree, including outside edges,
and put \(c_v=2-d_v\). Thus \(c_v\ge0\).
Define
\[
                       a^0=\pi Q^{-1}c.
 \tag{8}
\]
If \(d_v^{\rm out}\) counts the outside incidences, then
\[
               (Q\mathbf1-c)_v=b_v-2+d_v^{\rm out}\ge0,
 \tag{9}
\]
with a strict inequality somewhere because an outside edge exists.
Strict positivity of \(Q^{-1}\) gives
\[
                       0\le a^0_v<\pi.
 \tag{10}
\]
The equation \(Qa^0=\pi c\) also gives \(b_va^0_v<2\pi\).
Indeed
\[
 b_va^0_v=\sum_{w\text{ selected},\,w\sim v}a^0_w+\pi(2-d_v)
       <2\pi
 \tag{11}
\]
whenever the right side is nonzero; the zero case satisfies the same
strict bound. The number of selected neighbors plus \(2-d_v\)
is at most two.

Choose a sufficiently small \(\epsilon>0\) and set
\[
                  a=a^0+\epsilon Q^{-1}\mathbf1,\qquad s=-a.
 \tag{12}
\]
Then \(0<a_v<\pi\), \(b_va_v<2\pi\), and
\[
       b_va_v-\sum_{w\text{ selected},\,w\sim v}a_w
                                      >\pi(2-d_v).
 \tag{13}
\]
For a fixed \(s\), each \(g_{v,e}\) ranges independently over
\[
       -\frac{\pi-|s_w|}{2}<g_{v,e}
                                  <\frac{\pi-|s_w|}{2}.
 \tag{14}
\]
Their possible sums form the corresponding open interval.
Since the required sum is \(-\pi+b_va_v/2<0\), condition (13)
is exactly the assertion that it lies in this interval.
Choose these incidences independently at each selected vertex,
and choose every outside incidence to be zero.
All inequalities are strict. Existence and uniqueness of the
minimum now follow from the proved convex theorem. \(\square\)

## 3. The real coordinates and the weak length sign

**Proposition 2.** At the unique minimum,
\[
                            -\pi<s_v<0
 \tag{15}
\]
for every selected vertex. Every set of optimal corner covectors
satisfying (7) has \(h_v\le0\).

**Proof.** First, (1) gives
\[
        -b_vs_v\ge(2-d_v)\pi+\sum_{w\sim v}|s_w|.
 \tag{16}
\]
Since \(d_v\le2\), this implies \(s_v\le0\).

To obtain the weak length sign, fix one selected vertex and negate
both its \(s_v\) and all its \(g_{v,e}\), leaving every other
variable fixed. Formula (2) shows that, on each incident edge,
this either swaps the two squares or swaps and negates both square
coordinates. Hence the unconstrained energy (4) is unchanged.
The transformed point need not obey the filling equation; that is
irrelevant to the subgradient inequality for the unconstrained
energy on its product-square domain.

The energy subgradient paired with the vertex variables is
\[
 s_v\sum_{e\ni v}k_{v,e}+h_v\sum_{e\ni v}g_{v,e}
 =h_v\left(\frac{b_v}{2}s_v+\sum_{e\ni v}g_{v,e}\right)
 =-\pi h_v.
 \tag{17}
\]
Comparing the point with its negation in these variables implies
that this pairing is nonnegative. Thus \(h_v\le0\).

Put \(a_v=-s_v\). If some \(a_v=0\), (16) propagates zero to
every selected neighbor and hence to the whole path.
A vertex of original degree one would then contradict (16).
Otherwise all original selected degrees are two, and (1) forces
every selected incidence to be \(-\pi/2\).
At an outside end, orient the edge from selected \(v\) to outside
\(w\). We then have \(s_v=s_w=0\) and
\(y_P=y_Q=-\pi/4\).
No open side is permitted, so both \(A_P,A_Q\) are corners.
They are opposite because \(A_P=-A_Q\).
Their covectors \(x_P,x_Q\) consequently have opposite nonzero
signs by (5), contradicting
\(h_w=-2(x_P-x_Q)=0\). Thus every \(a_v>0\).

Suppose next that some \(a_v=\pi\).
On an edge to a selected neighbor \(w\), inequality (1) forces
\(g_{w,e}=0\), so \(A_P=A_Q=-\pi/4\).
Both \(y_P,y_Q\) must be corners. Their difference is
\(-a_w/2\); because \(0<a_w\le\pi\), this is possible only
if \(a_w=\pi\) and \(g_{v,e}=0\).
The same conclusion propagates to the whole path.
Every selected incidence on an internal edge is therefore zero.

At an outside end, the outside incidence is again forced to zero.
The selected incidence must be \(\pm\pi/2\), since both squares
have \(A=-\pi/4\) and cannot lie on an open side.
It cannot be \(+\pi/2\): both square covectors would then have
\(B>0\), giving \(h_v>0\). Thus every selected incidence on an
outside edge is \(-\pi/2\).
At a selected endpoint having at least one outside edge, the
filling equation reads
\[
              \sum_{e\text{ outside at }v}g_{v,e}
                                  =(b_v/2-1)\pi\ge0.
 \tag{18}
\]
Its left side is strictly negative, a contradiction. This also
handles a singleton selected path with two outside edges.
It proves (15). \(\square\)

## 4. The remaining corner patterns and strict length signs

**Proposition 3.** An outside edge has two interior squares.
On an internal oriented edge \(e=(v,w)\), at most one square can
be a corner. If a corner occurs, it is one of these two patterns:
\[
 \begin{array}{c|c|c|c}
 &\text{corner}&g_{v,e}&g_{w,e}\\ \hline
 P&(-\pi/4,-\pi/4)&-(\pi-a_w)/2&+(\pi-a_v)/2\\
 Q&(-\pi/4,+\pi/4)&+(\pi-a_w)/2&-(\pi-a_v)/2 .
 \end{array}
 \tag{19}
\]
Every selected real return and every selected dual length is
strictly negative:
\[
                            k_{v,e}<0,\qquad h_v<0.
 \tag{20}
\]

**Proof.** For an outside edge, \(y_P=y_Q=g_{v,e}/2\).
If one square were a corner, both \(y\)'s would be endpoints.
The other square could not lie on an open side, so both \(A\)'s
would also be endpoints. But their sum is
\(-a_v/2\in(-\pi/2,0)\), which is not a possible sum of
two numbers in \(\{-\pi/4,\pi/4\}\). Thus both squares are interior.

For an internal edge, use \(0<a_v,a_w<\pi\) in (2).
An \(A\)-corner can only have value \(-\pi/4\).
For \(P\), the corresponding \(y\)-corner can only be \(-\pi/4\);
for \(Q\), it can only be \(+\pi/4\).
Solving these equalities gives (19).
The other square is strictly interior. For a \(P\)-corner,
its coordinates are
\[
                  A_Q=\pi/4-a_v/2,\qquad
                  y_Q=-\pi/4+a_w/2.
 \tag{21}
\]
For a \(Q\)-corner, they are
\[
                  A_P=\pi/4-a_v/2,\qquad
                  y_P=\pi/4-a_w/2.
 \tag{22}
\]

Consider first an edge with two interior squares.
They reconstruct an actual positive edge with
\[
 t_v=-a_v-2iu_v,\quad t_w=-a_w-2iu_w,\qquad
                           u_v,u_w\ge0,
 \tag{23}
\]
where \(u=-h/2\); at an outside endpoint \(a=u=0\).
The original selected return is
\[
            r_{v,e}=\operatorname{arsinh}
                    \bigl(\tan(t_v/2)\cos(t_w/2)\bigr).
 \tag{24}
\]
Its branch has imaginary part between \(-\pi/2\) and \(\pi/2\).
The real part of its argument is
\[
 -\frac{
  \sin a_v\cos(a_w/2)\cosh u_w+
  \sinh(2u_v)\sin(a_w/2)\sinh u_w}
 {\cos a_v+\cosh(2u_v)}<0.
 \tag{25}
\]
The strict inequality uses \(0<a_v<\pi\) and \(0\le a_w<\pi\).
On the branch in (24), the sign of the real part of
\(\operatorname{arsinh}z\) is the sign of \(\Re z\).
Consequently \(k_{v,e}<0\) at every selected end of an interior edge.

Now suppose \(P\) is the corner in (19).
Then \(x_P<0,B_P<0\).
Since \(h_w=-2(x_P-x_Q)\le0\), we have
\(x_Q\le x_P<0\), and hence \(k_{v,e}<0\).
If \(B_Q\ge0\), then \(k_{w,e}=B_P-B_Q<0\) as well.
If \(B_Q<0\), put
\[
 X=-x_Q>0,\quad Y=-B_Q>0,\quad
 U=-x_P>0,\quad V=-B_P>0.
 \tag{26}
\]
Here \(U\le X\). Formula (21) and the interior gradient (3) give
\[
             \sinh(2X)\sinh(2Y)
                         =(-\cos a_v)\cos a_w<1.
 \tag{27}
\]
The signs \(x_Q,B_Q<0\) give \(a_v>\pi/2\), \(a_w<\pi/2\),
so the displayed product is positive.
The corner condition gives \(\sinh(2U)\sinh(2V)\ge1\).
Together with \(U\le X\), this forces \(V>Y\).
Thus \(k_{w,e}=-V+Y<0\).

For a \(Q\)-corner, \(x_Q<0,B_Q>0\).
The inequality \(h_v\le0\) gives \(B_P\le-B_Q<0\), so
\(k_{w,e}<0\). If \(x_P\le0\), then \(k_{v,e}<0\) immediately.
Otherwise put \(X=x_P>0\), \(Y=-B_P>0\),
\(U=-x_Q>0\), \(V=B_Q>0\).
Now \(V\le Y\), and (22) gives
\[
             \sinh(2X)\sinh(2Y)
                         =\cos a_v(-\cos a_w)<1.
 \tag{28}
\]
The corner condition forces \(U>X\), proving
\(k_{v,e}=X-U<0\).
This covers every possible edge. Finally (7), with \(b_v>0\),
implies \(h_v<0\). \(\square\)

For an outside edge, (6) also gives \(x_P=x_Q\).
Its two squares have the same \(y\), and (3) is strictly increasing
in \(A\) with \(y\) fixed. Thus the outside incidence is zero.
The selected incidence on that edge is strictly negative,
because its sign is the sign of \(B_P=B_Q=h_v/4\).

The possible corners in (19) have one positive internal incidence.
That fact is a classification of the remaining obstruction,
not a proof that the obstruction is absent.

## 5. An explicit sufficient condition for interiority

This first criterion is an intermediate step. The directed-incidence
argument in Sections 8--9 reduces its uniform threshold to four
at every selected vertex.

**Corollary 4.** Every corner has a negative-incidence endpoint \(v\)
with \(a_v>\pi/2\). If \(v\) has original degree two, then \(b_v\le5\).
If \(v\) is an original terminal, then \(b_v\le3\).
The same bound \(b_v\le3\) holds when \(v\) has degree two and
its other neighbor is outside the selected path.
Consequently the minimum is interior whenever
\[
 b_v\ge6\quad(d_v=2),\qquad
 b_v\ge4\quad(d_v=1).
 \tag{29}
\]
For this class, the original positive primitive period equations
have their unique positive solution at unit charges and complete
outside angles.

**Proof.** In the \(P\)-corner calculation, \(x_Q\le x_P<0\).
Equation (21) therefore forces \(a_v>\pi/2\).
This is exactly the endpoint with negative incidence in (19).
For a \(Q\)-corner, \(B_P\le-B_Q<0\), so (22) forces
\(a_w>\pi/2\), again at the negative-incidence endpoint.

Call that endpoint \(v\), and the other endpoint of the corner
edge \(w\). If \(v\) has degree two, let \(z\) denote its other
neighbor, with \(a_z=0\) when that neighbor is outside. Equations
(1) and (19) give
\[
 \begin{split}
 b_va_v
   &=2\pi+2g_{v,e}+2g_{v,\{v,z\}}\\
   &\le2\pi-(\pi-a_w)+(\pi-a_z)
     =2\pi+a_w-a_z<3\pi.
 \end{split}
 \tag{30}
\]
Since \(a_v>\pi/2\), this implies \(b_v<6\).
At a terminal, there is no other incidence, and instead
\[
                         b_va_v=\pi+a_w<2\pi.
 \tag{31}
\]
Hence \(b_v<4\). The magnitudes are integers, proving the bounds.
If the other neighbor of a degree-two vertex is outside, its
incidence is strictly negative by Proposition 3. The first line
of (30) then gives \(b_va_v<\pi+a_w<2\pi\), and again \(b_v<4\).
Under (29), no corner is possible. Open sides were already excluded,
so every square is interior. The established variational theorem
then identifies the minimum with the unique positive solution
of the original logarithmic period equations. \(\square\)

The criterion is uniform in the length of the selected path.
It is a statement at the indicated filling charges.
The [marked-completion theorem](research_positive_point_marked_completion.md)
uses the positive tangent-radial contraction to fix the full
original peripheral periods, then completes the actual primitive
filling at this endpoint. Together with the pointwise volume
identity it gives the original hyperbolic filling and its absolute
action-volume equality for this class. That argument does not
require a path of solutions with fixed slopes. It also does not
assert that the corresponding quantum contribution has a nonzero
coefficient.

Thus the sufficient threshold six can be reduced to four at a
selected degree-two end adjacent to a complete outside vertex.
A singleton selected path has no internal edge and hence no
possible corner at all under the standing hypothesis \(b_v\ge2\).

## 6. What remains unproved

The propositions show that a negative chain has a unique constrained
minimum, with no endpoint angle degeneration and no outside-edge
fold. They leave only the mixed-incidence internal patterns (19).
The positivity of the tridiagonal matrix \(Q\) was enough for strict
feasibility; by itself it has not been shown to exclude these
patterns when the small powers allowed by Corollary 4 occur.
Theorem 6 narrows those possible negative endpoints to magnitudes
two and three. The final Theorem 15 excludes every magnitude-three
case, leaving magnitude two as the geometric question not settled
by this note.

In particular, this note does not prove a positive geometric solution
for every negative chain. If the minimum is interior, the established
convex variation theorem identifies it with the unique positive
solution of the original primitive period equations.
The strict dual signs above then allow the marked-completion theorem
to identify its actual geometric filling. These geometric conclusions
still do not prove that the corresponding saddle survives in the
original signed quantum sum.

## 7. A positive internal incidence on an interior solution

The following calculation rules out a proposed shortcut to
interiority. Consider two adjacent selected vertices \(v,w\),
each with one complete outside neighbor, and powers
\((-B,-2)\). Take \(B\) to be a sufficiently large positive integer.
Let
\[
 r(t,u)=\operatorname{arsinh}(\tan(t/2)\cos(u/2)).
 \tag{32}
\]
The exact marked equations are
\[
 \begin{split}
 r(t_v,0)+r(t_v,t_w)+iBt_v/2&=-\pi i,\\
 r(t_w,0)+r(t_w,t_v)+it_w&=-\pi i.
 \end{split}
 \tag{33}
\]

Set \(\epsilon=1/B\) and \(t_v=\epsilon\zeta\).
At \(\epsilon=0\), the first equation has \(\zeta=-2\pi\).
The second has the positive isolated solution
\[
 t_*=-\pi/2-iH,\qquad H=\operatorname{arcosh}2
                             =\operatorname{arsinh}\sqrt3.
 \tag{34}
\]
Indeed
\[
 \cos(t_*/2)=\frac{\sqrt3-i}{2},\qquad
 r(t_*,0)=-H/2-i\pi/4,
 \tag{35}
\]
which verifies \(2r(t_*,0)+it_*=-\pi i\).
The positive-edge criterion is strict at \((t_*,0)\):
with \(a=\tan(t_*/2)=-(1+i\sqrt3)/2\) and \(b=0\), its
selected square root is \(q=e^{i\pi/6}\), so
\(\Re q=\sqrt3/2>|\Re a|=1/2\).
The complete edge \((0,0)\) is also positive.

The Jacobian of the rescaled equations in \((\zeta,t_w)\)
is triangular at this point. Its diagonal entries are
\[
                  i/2,\qquad
       2r_t(t_*,0)+i=\sec(t_*/2)+i
                              =\sqrt3/2+3i/2,
 \tag{36}
\]
both nonzero. The holomorphic implicit function theorem therefore
gives an actual positive solution for all sufficiently small real
\(\epsilon>0\), with
\[
                 t_v=-2\pi/B+O(B^{-2}),\qquad
                 t_w=t_*+O(B^{-1}).
 \tag{37}
\]
Positivity follows from openness at the three limiting edge pairs;
the equations, branches and primitive charges are unchanged.

At the shared edge,
\[
 \begin{split}
 r(t_v,t_w)
   &=-\frac{\pi}{B}\cos(t_*/2)+O(B^{-2})\\
   &=-\frac{\pi\sqrt3}{2B}
                       +\frac{\pi i}{2B}+O(B^{-2}).
 \end{split}
 \tag{38}
\]
Thus \(g_{v,e}>0\) for every sufficiently large integer \(B\).
This is an interior positive configuration, not a corner covector.
It disproves the general assertion that all incidences in an
all-negative corridor are negative. It does not disprove
interiority of the minimum or any volume conjecture.

## 8. A strict direction for the nonnegative incidences

There is nevertheless a useful sign principle that accommodates
the example above. Put
\[
 a_v=-s_v,\qquad u_v=-h_v/2,\qquad
                \mathcal R_v=\frac{\sinh(2u_v)}{\sin a_v}>0.
 \tag{39}
\]
All quantities are finite and positive by Propositions 2 and 3.

**Proposition 5.** If \(e=\{v,w\}\) is an internal edge and
\(g_{v,e}\ge0\), then
\[
 \mathcal R_v\le\tan(a_w/2)\tanh u_w<\mathcal R_w.
 \tag{40}
\]
The first inequality is strict when \(g_{v,e}>0\).
This holds both for an interior edge and for the allowed
corner covectors in (19).
Consequently orienting an edge from \(v\) to \(w\) whenever
\(g_{v,e}\ge0\) gives no edge with both orientations and no
directed cycle.

**Proof for an interior edge.** The imaginary part of the
argument of the original return (24) is
\[
 \frac{
 \sin a_v\sin(a_w/2)\sinh u_w
       -\sinh(2u_v)\cos(a_w/2)\cosh u_w}
 {\cos a_v+\cosh(2u_v)}.
 \tag{41}
\]
For the canonical return with \(|\Im r|<\pi/2\), this has
the same sign as \(g_{v,e}\).
Thus nonnegativity implies
\[
 \mathcal R_v\le\tan(a_w/2)\tanh u_w
             <\frac{\sinh(2u_w)}{\sin a_w}
              =\mathcal R_w.
 \tag{42}
\]
The strict inequality follows from
\[
 \frac{\sinh(2u_w)/\sin a_w}
      {\tan(a_w/2)\tanh u_w}
                  =\frac{\cosh^2u_w}{\sin^2(a_w/2)}>1.
 \tag{43}
\]

**Proof at a corner.** It suffices to consider the \(P\)-corner,
where \(g_{w,e}>0\) and \(g_{v,e}<0\). In the notation of
(26), allow \(Y=-B_Q\) to have either sign. The other square
is interior, \(X=-x_Q>0\), and
\[
       U=-x_P>0,\quad V=-B_P>0,\qquad
       u_w=X-U>0,\quad u_v=V+Y>0.
 \tag{44}
\]
In particular \(U<X\).
Replace \(V\) temporarily by
\[
                    V_0=\tfrac12\operatorname{arsinh}
                                  (\operatorname{csch}(2U)).
 \tag{45}
\]
The corner inequality gives \(V\ge V_0\).
This replacement puts the corner covector on the geometric
equality boundary \(\sinh(2U)\sinh(2V_0)=1\), without
changing the two square angle coordinates, the other square,
or \(u_w\).

We check that \(u_v^0=V_0+Y>0\).
If \(Y\ge0\), this is immediate.
If \(Y<0\), the interior square formula (21) gives
\[
              \sinh(2X)\sinh(-2Y)
                                =\cos a_v\cos a_w<1;
 \tag{46}
\]
both cosines are negative in this case.
Since \(U<X\), equation (46) implies \(V_0>-Y\).

The resulting equality covector is an actual finite flat
boundary of the original positive edge, with the other
four tetrahedra still positive. The precise shape statement
is proved in
[the corner geometry note](research_square_corner_flat_geometry.md),
Section 2. Its full face chart is regular, so the original
return formula (24) continues there.
The same calculation (41)--(43), now using the unchanged
strictly positive \(g_{w,e}\), gives
\[
 \mathcal R_w<\tan(a_v/2)\tanh u_v^0
                    <\frac{\sinh(2u_v^0)}{\sin a_v}.
 \tag{47}
\]
Increasing \(V_0\) back to \(V\) only increases \(u_v\);
both right-hand expressions increase.
This proves the stronger chain (40) for the positive incidence
at \(w\).
Interchanging the endpoints sends a \(Q\)-corner to this
\(P\)-corner calculation and proves the remaining case.
Strict increase of \(\mathcal R\) proves the directed-graph
assertions. \(\square\)

Every such directed path terminates at a vertex whose incident
values are all strictly negative. At that vertex the filling
equation gives \(b_va_v<2\pi\).
This supplies a scalar direction for following nonnegative
incidences through a long corridor. It does not show that a
path beginning at a corner must end at another corner.
Thus acyclicity alone does not exclude all corner patterns.
The next section uses the stronger quantitative inequality
in (40) to exclude negative corner endpoints of magnitude
at least four.

## 9. Reducing the possible corner coefficients to two and three

The stronger inequality in (40) does give a further exclusion.

**Theorem 6.** Every corner has a negative-incidence endpoint whose
crossing magnitude is either two or three.
Consequently, if every selected magnitude satisfies \(b_v\ge4\),
the unique minimum is interior, regardless of the length of the
selected path. It gives the actual marked hyperbolic filling
and its absolutely normalized action-volume identity through
the pointwise marked-completion theorem.

**Proof.** Let \(v\) be the negative-incidence endpoint of a
corner, and put \(\theta=a_v\), \(\phi=a_w\) for its other
endpoint. We know \(\pi/2<\theta<\pi\).
We first sharpen the height bound at this endpoint:
\[
                   \mathcal R_v>
                       \frac{\sin\theta}{-2\cos\theta}.
 \tag{48}
\]
Orient the edge so that it is the \(P\)-corner in (19).
Use \(X,U,V,Y\) as in (44), with \(Y\) allowed either sign.
The unchanged interior square gives
\[
 \sinh(2X)=-\cot\theta\sin\phi,\qquad
 \sinh(2Y)=\cot\phi\sin\theta.
 \tag{49}
\]
Since \(0<U<X\), and the function
\(V_0(U)=\tfrac12\operatorname{arsinh}(\operatorname{csch}(2U))\)
is strictly decreasing,
\[
                  u_v=V+Y>V_0(X)+Y.
 \tag{50}
\]
Set \(A=-\cos\theta>0\), \(B=\cos\phi\), and
\(\Delta=\sqrt{1-A^2B^2}\).
The hyperbolic addition formula applied to (49) gives exactly
\[
       \frac{\sinh(2[V_0(X)+Y])}{\sin\theta}
                                  =\frac{\Delta}{A(1-B)}.
 \tag{51}
\]
For example, the two sinh terms are
\(\sin\theta/(A\sin\phi)\) and
\(B\sin\theta/\sin\phi\); their cosh terms are
\(\Delta/(A\sin\phi)\) and \(\Delta/\sin\phi\).
Their sum simplifies to (51).
Now \(\Delta\ge\sin\theta\) and \(1-B<2\), so (50)--(51)
give (48). Interchanging endpoints covers a \(Q\)-corner.

A terminal negative endpoint already has \(b_v\le3\) by
Corollary 4. Suppose instead that \(v\) has degree two and
assume for contradiction that its magnitude \(m=b_v\) is at
least four. Let \(z\) be its other neighbor.
The corner incidence and the filling equation give
\[
                      m\theta=\pi+\phi+2g_{v,\{v,z\}}.
 \tag{52}
\]
Because \(m\theta>2\pi\) and \(\phi<\pi\), this other
incidence is strictly positive. It cannot be an outside
incidence, so \(z\) is selected.
The strong inequality (40), valid whether this second edge
is interior or itself a corner, implies
\[
                         a_z>2\arctan\mathcal R_v.
 \tag{53}
\]
The edge angle bound and (52) give
\[
 m\theta\le2\pi+\phi-a_z<3\pi-a_z
     <3\pi-2\arctan\frac{\sin\theta}{-2\cos\theta}.
 \tag{54}
\]
Write \(\delta=\theta-\pi/2\in(0,\pi/2)\).
The last expression equals
\[
                         2\pi+2\arctan(2\tan\delta).
 \tag{55}
\]
For \(0<\delta<\pi/4\),
\(\tan(2\delta)>2\tan\delta\), so
\(\arctan(2\tan\delta)<2\delta\).
For \(\delta\ge\pi/4\), the same strict inequality follows
from \(\arctan(2\tan\delta)<\pi/2\le2\delta\).
Thus (54) is strictly less than
\(2\pi+4\delta=4\theta\), contradicting \(m\ge4\).

Every corner therefore has a negative endpoint of magnitude
two or three. If all magnitudes are at least four, there
are no corners; open sides have already been excluded.
The minimum is interior, and Propositions 2--3 give its
strict core signs. The marked-completion theorem applies
with the original integer slopes and carriers. \(\square\)

The theorem strengthens the sufficient criterion of Section 5.
It does not dispose of patterns containing coefficients two or
three, and it gives no quantum coefficient or cancellation estimate.
The directed-incidence argument is developed further below:
Section 14 excludes the magnitude-three cases.

## 10. Exact rational transport of the primitive edge equations

There is a second way to formulate the remaining existence problem.
It applies to genuine positive edge configurations, not to a strict
corner subgradient treated as if it were such a configuration.
The fixed integer turns give explicit rational transformations of
the original edge square roots.

At a selected vertex put
\[
 a=\tan(t/2),\qquad
 q_{\rm in}^2=1+a^2+a_{\rm in}^2,\qquad
 q_{\rm out}^2=1+a^2+a_{\rm out}^2.
 \tag{56}
\]
For either incident original edge, its canonical return satisfies
\[
              \sinh r=a\cos(u/2),\qquad
              \cosh r=q\cos(u/2),\qquad
                         \coth r=q/a.
 \tag{57}
\]
Here \(a\ne0\), since the selected angle has strictly negative
imaginary part. For the negative integer power \(-b\), the full
primitive equation at a degree-two vertex is
\[
                r_{\rm in}+r_{\rm out}
                            =-i b\arctan a-\pi i.
 \tag{58}
\]

Define real-coefficient polynomials \(C_b,H_b\) by
\[
                  (1+ia)^b=C_b(a)+iaH_b(a).
 \tag{59}
\]
Thus \(C_b\) is the even part of the binomial expansion and
\(iaH_b\) is its odd part. Comparing with \(1-ia\) gives
\[
               C_b(a)^2+a^2H_b(a)^2=(1+a^2)^b.
 \tag{60}
\]
Where the cotangent expression is defined,
\[
                   B_b(a):=\frac{iC_b(a)}{H_b(a)}
                              =ia\cot(b\arctan a).
 \tag{61}
\]

**Proposition 7.** Every positive solution of (58) obeys the
homogeneous rational relation
\[
       \{H_b(a)q_{\rm in}-iC_b(a)\}\,q_{\rm out}
                          =iC_b(a)q_{\rm in}-a^2H_b(a).
 \tag{62}
\]
Its projective matrix
\[
 \mathcal M_b^{\rm per}(a)
       =\begin{pmatrix}
          iC_b(a)&-a^2H_b(a)\\
          H_b(a)&-iC_b(a)
        \end{pmatrix}
 \tag{63}
\]
satisfies
\[
 \det\mathcal M_b^{\rm per}(a)=(1+a^2)^b,\qquad
 \{\mathcal M_b^{\rm per}(a)\}^2=-(1+a^2)^b I.
 \tag{64}
\]
Consequently it is an invertible projective involution on the
positive domain, where \(a\ne\pm i\).

**Proof.** Let \(A=-ib\arctan a\). The identity
\[
       \coth(A-r)=\frac{\coth A\,\coth r-1}
                            {\coth r-\coth A}
 \tag{65}
\]
and the period \(i\pi\) of coth transform (58), using (57),
into
\[
                    q_{\rm out}
                  =\frac{B_b(a)q_{\rm in}-a^2}
                               {q_{\rm in}-B_b(a)}.
 \tag{66}
\]
Multiplication by \(H_b(a)\) gives (62).
This equality also holds at a zero of that polynomial,
by the homogeneous formula or analytic continuation.
The determinant and square of (63) follow directly from
(60). \(\square\)

The two remaining small coefficients have particularly short maps:
\[
 \begin{array}{c|c|c|c}
 b&C_b(a)&H_b(a)&B_b(a)\\ \hline
 2&1-a^2&2&i(1-a^2)/2\\
 3&1-3a^2&3-a^2&i(1-3a^2)/(3-a^2).
 \end{array}
 \tag{67}
\]
In fact \(C_b,H_b\) are both nonzero when \(\Im a<0\):
their vanishing would make
\(\{(1+ia)/(1-ia)\}^b\) equal to \(-1\) or \(1\),
whereas this quotient has modulus strictly greater than one.
The excluded point \(a=-i\) is already absent from the positive
edge domain. The homogeneous form (62) nevertheless retains the
full polynomial factors and does not require canceling them.

The possible pole \(H_bq_{\rm in}-iC_b=0\) cannot be an
indeterminate expression: (64) is nonzero.
At that pole the projective output is infinity, which is not
a regular positive edge square root. Thus the pole is a genuine
boundary to be tracked, not a removable factor declared harmless.

For a pendant path, the degree-one initial equation gives
\[
                           H_{b_1}(a_1)q_1=iC_{b_1}(a_1).
 \tag{68}
\]
Subsequently use (62) at each degree-two vertex and
\[
                         a_{j+1}^2=q_j^2-1-a_j^2.
 \tag{69}
\]
At a complete outside end the final equation is
\(q_k^2=1+a_k^2\).
For a corridor with both ends retained, keep their tangent
variables in (56) and (69) instead.
These are exact algebraic equations for the original boundary
data; no knot-by-knot shape list is required.

There are essential qualifications. Equation (62) is a consequence
of the full primitive equation, but the converse retains an
integer ambiguity because coth has period \(i\pi\).
One must impose the original value \(-\pi i\) in (58),
the original square-root branches, and positivity at every edge.
The derivation also uses \(a\ne0\); the point \(a=0\) of the
exponentiated equations must not be reintroduced as a solution
of a unit-charge filling. Thus neither the projective involution
nor the algebraic closure (69) proves that the required positive
branch exists for every finite word.

The matrix (63) transports classical primitive periods. It is
not the finite quantum crossing matrix, and its involutivity
does not constitute a quantum source identity or a topological
tangle reduction.

## 11. A further restriction on a corner of magnitude three

The directed estimate also restricts the other endpoint of a
corner whose negative incidence has magnitude three. This is a
local necessary condition; it does not yet exclude that corner.

**Proposition 8.** Suppose the negative endpoint \(v\) of a corner
has \(b_v=3\), and write \(\theta=a_v\), \(\phi=a_w\) for its two
endpoint angles. Then \(\phi>\pi/2\). The magnitude at \(w\) is at
most six. It is at most four if \(w\) is a terminal, or if its other
neighbor is a complete outside vertex.

**Proof.** We already know \(\theta>\pi/2\). Put
\(\delta=\theta-\pi/2\). Suppose \(\phi\le\pi/2\).
In (51), \(B=\cos\phi\ge0\), \(\Delta\ge\sin\theta\), and
\(1-B\le1\). Consequently the stronger form of (48) gives
\[
                 \mathcal R_v>
                 \frac{\sin\theta}{-\cos\theta}
                               =\cot\delta.             \tag{70}
\]
If \(v\) were terminal, its imaginary filling equation would give
\(3\theta=\pi+\phi\le3\pi/2\), already a contradiction.
Otherwise its other incidence is
\[
             g=\frac{3\theta-\pi-\phi}{2}
                                  \ge\frac32\delta>0.    \tag{71}
\]
Its other neighbor \(z\) must therefore be selected. Proposition 5
and the original edge angle bound imply
\[
 \mathcal R_v<\tan(a_z/2),\qquad
 g\le\frac{\pi-a_z}{2}
                  <\arctan(1/\mathcal R_v)<\delta.        \tag{72}
\]
This argument applies even when the second edge is itself a
corner: Proposition 5 was proved for its full subdifferential.
Equations (71)--(72) contradict one another, proving
\(\phi>\pi/2\).

At \(w\), the corner incidence is \((\pi-\theta)/2\). If \(w\)
has degree two, its other incidence \(g_w\) gives
\[
                  b_w\phi=3\pi-\theta+2g_w
                                      <4\pi-\theta
                                      <7\pi/2.           \tag{73}
\]
Since \(\phi>\pi/2\), this forces the integer \(b_w<7\).
For a terminal the same equation has \(g_w=0\); for a complete
outside neighbor it has \(g_w<0\). In either case
\(b_w\phi\le3\pi-\theta<5\pi/2\), hence \(b_w<5\).
\(\square\)

Thus a corner of magnitude three cannot border an arbitrarily
large coefficient. Its positive endpoint has magnitude in
\(\{2,3,4,5,6\}\), with the smaller list \(\{2,3,4\}\) at a
complete end. Corners of magnitude two remain unrestricted by
this proposition. The result narrows the remaining local
configurations; it does not prove that the finite lists occur,
or that they cannot occur, in a minimizing finite path.

**Proposition 9.** A negative corner endpoint of magnitude three
has \(\theta>2\pi/3\). Its other incidence is strictly positive.
In particular, it is neither an original terminal nor a vertex
adjacent to a complete outside end.

**Proof.** Use Proposition 8 and orient the corner as in (49).
Since \(\phi>\pi/2\), write \(Y=-H\) with \(H>0\). The companion
square and the corner covector give
\[
 \sinh(2X)=(-\cot\theta)\sin\phi,\quad
 u_w=X-U>0,\quad -k_{w,e}=V+H,\quad
 V\ge V_0(U):=\tfrac12\operatorname{arsinh}(\operatorname{csch}(2U)).
                                                               \tag{74}
\]
All returns at \(w\) have negative real part. Its real filling
equation, with \(n=b_w\le6\), therefore gives
\[
             V+H\le n(X-U)\le6(X-U).
                                                               \tag{75}
\]
The first inequality is strict when \(w\) has another incidence;
equality is allowed at a terminal and does not affect the argument.
Because \(H>0\), (75) implies
\[
 6X>6U+V_0(U)\ge
 C_6:=\frac{6\operatorname{arsinh}(1/6)+\operatorname{arsinh}6}{2}.
                                                               \tag{76}
\]
The minimum in (76) follows by differentiation; it occurs at
\(\sinh(2U)=1/6\).

Suppose \(\theta\le2\pi/3\). Then (74) gives
\[
 X\le\tfrac12\operatorname{arsinh}(1/\sqrt3)
                                      =\tfrac14\log3.
                                                               \tag{77}
\]
On the other hand, \(\operatorname{arsinh}6>\log12\) and
\(6\operatorname{arsinh}(1/6)>6/7>5/6\).
The elementary inequality
\(\log x\le(x-1)/\sqrt{x}\), for \(x\ge1\), gives
\(\log(9/4)\le5/6\). It follows that
\(C_6>\tfrac12\log27=\tfrac32\log3\), contradicting
(76)--(77). This proves \(\theta>2\pi/3\).

A terminal would have \(3\theta=\pi+\phi<2\pi\), so it is
impossible. At a degree-two vertex, the other incidence is
\[
           g_{v,\mathrm{other}}
              =\frac{3\theta-\pi-\phi}{2}
                      >\frac{\pi-\phi}{2}>0.              \tag{78}
\]
An incidence against a complete outside vertex is strictly negative,
so that alternative is also impossible. \(\square\)

**Corollary 10.** The positive geometric conclusion of Theorem 6
continues to hold if magnitudes three are allowed at original
terminals and at selected vertices adjacent to complete outside
ends, while every other selected magnitude is at least four.
More generally, a magnitude-three vertex anywhere in the path
cannot be the negative endpoint of a corner if all its selected
neighbors have magnitude at least seven.

Indeed Theorem 6 excludes negative corner endpoints of magnitude
at least four, Proposition 9 excludes the specified end vertices,
and Proposition 8 excludes a magnitude-three negative endpoint
next to a magnitude at least seven. As before, these statements
give actual positive marked fillings through the completion theorem;
they make no assertion about a surviving quantum contribution.

## 12. Three necessary corner inequalities do not yet exclude the case

For a magnitude-three negative endpoint whose positive endpoint
also has degree two, Propositions 8--9 and the latter endpoint's
real equation imply
\[
 \begin{split}
 3\theta&<\pi+\phi+2\arctan(1/R_0),\\
 n\phi&<4\pi-\theta,\\
 nX&>C_n+H,
 \end{split}                                                   \tag{79}
\]
where \(n\in\{3,4,5,6\}\) when all selected magnitudes are at least
three, and
\[
 \begin{split}
 X&=\tfrac12\operatorname{arsinh}(-\cot\theta\sin\phi),&
 H&=\tfrac12\operatorname{arsinh}(-\cot\phi\sin\theta),\\
 R_0&=\frac{\sqrt{1-\cos^2\theta\cos^2\phi}}
                  {(-\cos\theta)(1-\cos\phi)},&
 C_n&=\frac{n\operatorname{arsinh}(1/n)+\operatorname{arsinh}n}{2}.
 \end{split}                                                   \tag{80}
\]
Here \(2\pi/3<\theta<\pi\) and \(\pi/2<\phi<\pi\).
The last inequality follows by minimizing \(nU+V_0(U)\), exactly
as in (76). If the positive endpoint is terminal, the last
inequality need only be non-strict. Even the stronger three
strict inequalities displayed here are consistent.

**Proposition 11.** For \(n=4\), every point of the rectangle
\[
 \left|\frac{\theta}{\pi}-\frac56\right|\le\frac1{100000},
 \qquad
 \left|\frac{\phi}{\pi}-\frac{79}{100}\right|\le\frac1{100000}
                                                               \tag{81}
\]
satisfies (79).

**Proof.** Put \(g=(3\theta-\pi-\phi)/2\). On (81),
\(0<g<\pi/2\), so the first inequality of (79) is equivalent to
\(\cos g-R_0\sin g>0\).
Outward rational interval evaluation on the whole rectangle gives
\[
 \cos g-R_0\sin g>\frac1{100},\qquad
 4\pi-\theta-4\phi>\frac1{50},\qquad
 4X-C_4-H>\frac1{400}.                                    \tag{82}
\]
The [finite verifier](../experiments/check_negative_three_corner_necessary_conditions.py)
records the complete rational bounds in
[its saved output](../repro/results/research-negative-three-corner-necessary-conditions.json).
It uses Machin's formula with alternating-series remainder bounds
for \(\pi\), Taylor remainder bounds for sine, integer-square-root
enclosures, and
\(\operatorname{arsinh}x=\log(x+\sqrt{1+x^2})\).
The logarithm is bounded by its convergent series in
\((x-1)/(x+1)\). All rounding is outward and rational; no
floating-point test decides (82). \(\square\)

This is a witness for the necessary inequalities only. In fact,
the additional outgoing incidence at the positive endpoint
excludes this entire rectangle from the full KKT system.

To see this, put
\[
 \lambda=4\pi-\theta-n\phi
                 =\pi-2g_{w,\mathrm{other}}.
                                                               \tag{83}
\]
Whenever \(g_{w,\mathrm{other}}>0\), Proposition 5 and the edge
angle bound give \(\mathcal R_w<\tan(\lambda/2)\).
The real equation at \(w\), on the other hand, gives
\(n(X-U)\ge V+H>H\). Consequently
\[
 \mathcal R_w=\frac{\sinh(2(X-U))}{\sin\phi}
                 >\frac{2H}{n\sin\phi},\qquad
                 \frac{2H}{n}<\sin\phi\tan(\lambda/2).
                                                               \tag{84}
\]
This remains valid if the other edge is itself a corner, because
Proposition 5 includes its full corner subdifferential.

On (81), \(\theta<7\pi/8\) and \(\phi>3\pi/4\), so
\[
 H>\tfrac12\operatorname{arsinh}(1/3)>\tfrac18.
                                                               \tag{85}
\]
Here \(\sin\theta>\sin(\pi/8)>1/3\), \(-\cot\phi>1\), and
\(\operatorname{arsinh}(1/3)>1/\sqrt{10}>1/4\).
Also \(0<\lambda/2<1/50\); the upper bound follows directly
from (81) and \(\pi<4\). Thus \(g_{w,\mathrm{other}}>0\), and
\[
 \sin\phi\tan(\lambda/2)
       <\frac{1/50}{1-1/5000}
       =\frac{100}{4999}<\frac1{40}.
                                                               \tag{86}
\]
For \(n=4\), (85) gives \(2H/n>1/16\), contradicting (84).
Therefore the open witness for (79) is not a possible corner
minimum.

This calculation isolates a missing condition in the
three-inequality test. Sections 13--14 use that condition to settle
the remaining angles when every magnitude is at least three.
The original quantum contribution is a separate question.

## 13. A magnitude-three corner must meet magnitude four or five

The outgoing inequality has a useful consequence independent of the
other endpoint's real equation. It will exclude two more magnitudes
from Proposition 8 and, in particular, settle arbitrary paths whose
selected magnitudes are all three.

**Lemma 12.** Suppose \(0<x<\pi/3\), \(0<y<\pi/2\), \(3x-y>0\), and
\[
 R(x,y):=\frac{\sqrt{1-\cos^2x\cos^2y}}{\cos x(1+\cos y)}
                               <\tan\frac{3x-y}{2}.
                                                               \tag{87}
\]
Then \(y<4x/3\).

**Proof.** We have
\[
 R(x,y)^2=\tan^2(y/2)+\tfrac14\tan^2x\sec^4(y/2).
                                                               \tag{88}
\]
For fixed \(x\), this is strictly increasing in \(y\), whereas the
right side of (87) is strictly decreasing while \(0<3x-y<\pi\).
It is therefore enough to show
\(R(x,4x/3)>\tan(5x/6)\).

Here is an exact polynomial verification of that last inequality.
Put \(a=\tan(x/6)\), and write
\[
 c_j(a)=\Re(1+ia)^j,\qquad s_j(a)=\Im(1+ia)^j.
\]
The real and imaginary parts here mean their real-coefficient
binomial polynomials. Since \(0<x/6<\pi/18\), we have \(0<a<1/5\);
for example this follows from \(\pi<22/7\),
\(\sin t<t\), and \(\cos t>1-t^2/2\).
All of \(c_4,c_5,c_6\) are positive. Substituting
\(\tan(jx/6)=s_j/c_j\) in (88) gives the identity
\[
 R(x,4x/3)^2-\tan^2(5x/6)
   =\frac{a^4(3-a^2)(1+a^2)^4 P(a^2)}
                 {c_4(a)^4c_5(a)^2c_6(a)^2},              \tag{89}
\]
where
\[
 \begin{split}
 P(z)={}&z^{12}-75z^{11}+1841z^{10}-26525z^9+188184z^8\\
       &-674158z^7+1223346z^6-1195674z^5+652257z^4\\
       &-197015z^3+32461z^2-2681z+86.
 \end{split}                                                   \tag{90}
\]
For \(0\le z\le1/25\), group each positive even-degree term with
the following negative odd-degree term. All groups of degree at
least four are nonnegative, and
\(32461-197015z>24580\). Thus
\[
 P(z)\ge86-2681z+24580z^2
                \ge\frac{11305}{625}>18.                  \tag{91}
\]
The quadratic is decreasing on this interval, giving its stated
lower bound at \(z=1/25\). Every factor in (89) is positive.
This proves the lemma. The
[exact symbolic verifier](../experiments/check_negative_three_corner_angle_bound.py)
checks (89), the grouping in (91), and all rational inequalities;
its [saved output](../repro/results/research-negative-three-corner-angle-bound.json)
records zero polynomial residual. \(\square\)

**Theorem 13.** Suppose all selected magnitudes are at least three.
If the minimum has a corner, its negative endpoint has magnitude
three and its positive endpoint has magnitude four or five.
Consequently the minimum is interior whenever the path contains
no edge joining magnitude three to magnitude four or five.
In particular, every finite path with magnitudes in
\(\{3\}\cup\{6,7,8,\ldots\}\) has a positive marked filling,
independently of its length.

**Proof.** Theorem 6 and Propositions 8--9 reduce a possible corner
to a negative endpoint of magnitude three, with
\(2\pi/3<\theta<\pi\), and a positive endpoint of magnitude
\(n\in\{3,4,5,6\}\), with \(\pi/2<\phi<\pi\).
Put
\[
                       x=\pi-\theta,\qquad y=\pi-\phi .
\]
The other incidence at the negative endpoint is positive.
Its outgoing inequality is exactly (87), so Lemma 12 gives
\(y<4x/3\).

At a degree-two positive endpoint, (73) gives
\[
                         ny>(n-3)\pi-x.                  \tag{92}
\]
The same strict inequality also holds for a terminal, whose
imaginary equation is stronger. If \(n=6\), combining (92) with
\(y<4x/3\) gives \(x>\pi/3\), a contradiction.

It remains to exclude \(n=3\). In these coordinates the real
equation requires
\[
 F_n(x,y):=
 \frac{n\operatorname{arsinh}(\cot x\sin y)
                   -\operatorname{arsinh}(\cot y\sin x)}{2}
                              \ge C_n.                    \tag{93}
\]
At a degree-two positive endpoint the inequality is strict;
allowing equality also covers a terminal. We prove a strict
upper bound contradicting (93) for \(n=3\).

For \(0<x,y<\pi/2\), put
\[
 r=\frac{\sin y}{\sin x},\qquad c=\cos x\cos y,\qquad
 \Delta=\sqrt{1-c^2}.
\]
Direct differentiation gives
\[
 2\Delta(F_n)_x=-nr-c,\qquad
 2\Delta(F_n)_y=nc+1/r>0.                                  \tag{94}
\]
Along a ray \(y=kx\), with \(1\le k<n\), it follows that
\[
 2\Delta\frac{d}{dx}F_n(x,kx)
                           =-n(r-kc)+k/r-c<0.             \tag{95}
\]
For completeness, let \(T=\tan(kx)/\tan x\ge k\), using the
convexity of tangent on \((0,\pi/2)\).
Then \(r/c=T/\cos^2x>k\), and
\[
 \frac{r-1/r}{c}=T-1/T\ge k-1/k.
\]
Thus \(k/r-c\le k(r-kc)\), while \(r-kc>0\) and \(n>k\).
This proves the strict sign in (95).

By (94), \(y<4x/3\), and (95) with \(k=4/3\),
\[
 F_3(x,y)<F_3(x,4x/3)
       <\frac{3\operatorname{arsinh}(4/3)
                       -\operatorname{arsinh}(3/4)}{2}
        =\frac12\log(27/2).                               \tag{96}
\]
But \(\operatorname{arsinh}3>\log6\) and
\(3\operatorname{arsinh}(1/3)>3/\sqrt{10}>5/6
\ge\log(9/4)\). Therefore
\[
                              C_3>\tfrac12\log(27/2),
\]
contradicting (93). Only \(n=4,5\) remain.

If the two specified adjacent pairs are absent, no corner is
possible. The earlier variational result already excludes open
sides, so the minimum is interior, with every selected
\(\Im t_v<0\). The pointwise marked-completion theorem gives the
original hyperbolic filling and the absolute action-volume
identity. Its primitive slopes, carrier markings, and complete
outside cusps are retained. \(\square\)

The theorem is a geometric statement. Adjacent pairs \(3,4\) and
\(3,5\) are the remaining possibilities under these estimates;
Section 14 excludes them using both endpoints' conditions.
Magnitude two remains outside this theorem. No estimate of the
original signed quantum sum, or nonzero quantum contribution,
follows from it.

## 14. Excluding the last two neighboring magnitudes

The two outgoing-incidence conditions can be imposed simultaneously.
The remaining domain is compact and stays away from every trigonometric
or logarithmic singularity. A finite rational interval certificate
then excludes both remaining magnitudes.

**Lemma 14.** The necessary corner conditions have no solution with
negative endpoint magnitude three and positive endpoint magnitude
\(n=4\) or \(n=5\).

**Proof.** Continue to use \(x=\pi-\theta\), \(y=\pi-\phi\).
Theorem 13 and its proof give
\[
 0<x<\pi/3,\qquad 0<y<4x/3,\qquad
 \lambda=x+ny-(n-3)\pi>0.
                                                               \tag{97}
\]
Combining these inequalities places \((x/\pi,y/\pi)\) in the interior
of one of the following closed rectangles:
\[
 \begin{array}{c|c|c}
 n&x/\pi&y/\pi\\ \hline
 4&[3/19,\,1/3]&[1/6,\,4/9]\\
 5&[6/23,\,1/3]&[1/3,\,4/9].
 \end{array}                                                   \tag{98}
\]
Indeed \(\lambda>0\) and \(y<4x/3\) give
\(x>3(n-3)\pi/(4n+3)\); using \(x<\pi/3\) in \(\lambda>0\)
gives the lower bound for \(y\).

On these rectangles define
\[
 X=\tfrac12\operatorname{arsinh}(\cot x\sin y),\quad
 H=\tfrac12\operatorname{arsinh}(\cot y\sin x),\quad
 R=\frac{\sqrt{1-\cos^2x\cos^2y}}{\cos x(1+\cos y)}.
                                                               \tag{99}
\]
Every corner would have to satisfy all the following conditions:
\[
 \begin{gathered}
 y<4x/3,\qquad \lambda>0,\qquad nX-H\ge C_n,\\
 R<\tan((3x-y)/2),\\
 \lambda<\pi\quad\Longrightarrow\quad
                 2H/n<\sin y\tan(\lambda/2).
 \end{gathered}                                                \tag{100}
\]
The first line is the angle and real-period information already
proved. The second line is the negative endpoint's outgoing bound.
The last line is (84), using the outgoing incidence at the positive
endpoint. If that endpoint is terminal, its equation gives exactly
\(\lambda=\pi\), so the last line is not invoked. In particular,
the weak inequality in the first line correctly retains the terminal
case.

The
[rational interval verifier](../experiments/verify_negative_three_corner_exclusion.py)
bisects each rectangle (98) at rational midpoints until every
resulting rectangle violates a condition in (100). There are 94
terminal rectangles for \(n=4\), and 10 for \(n=5\).
The [saved certificate](../repro/results/research-negative-three-corner-exclusion.json)
lists their exact rational endpoints, the condition violated, and
a rational lower bound for that violation.

Here are the bounds used at each rectangle, so that the scope of
the finite verification is explicit. Sine and cosine are enclosed
on the full coordinate intervals. Positive square roots use integer
square-root bounds; inverse hyperbolic sines use their monotonicity
and the logarithmic formula from Proposition 11. All arithmetic
rounds outward. The tests reject a rectangle if
\(C_n-nX+H\) is strictly positive throughout it, or if
\(R-\tan((3x-y)/2)\) is nonnegative throughout it.
The first requires strict positivity because the real-period
condition in (100) is weak.

For the last condition, let \(\lambda_{\max}\) be the upper interval
endpoint. This test is used only when
\(0<\lambda_{\max}<\pi\). On the portion where \(\lambda>0\),
\[
 \sin y\tan(\lambda/2)
   \le (\sin y)_{\max}\tan(\lambda_{\max}/2).
                                                               \tag{101}
\]
If this upper bound is at most the interval lower bound for \(2H/n\),
the rectangle cannot contain a corner. Its portion with
\(\lambda\le0\), if any, already violates (97).
No outgoing bound is applied to a rectangle reaching
\(\lambda\ge\pi\); such rectangles are excluded by the other
conditions.

The remaining tests are the linear inequalities
\(y<4x/3\) and \(\lambda>0\).
Each bisection replaces a rectangle by two rectangles whose union
is the original one, including their common boundary.
The finite list therefore covers the whole of (98).
Every listed rectangle has a proved exclusion, so (100) has no
solution. This proves the lemma. \(\square\)

**Theorem 15.** In the setup of Section 1, every finite selected
path with integer negative magnitudes \(b_v\ge3\) has an interior variational
minimum. Its positive solution has every selected
\(\Im t_v<0\), realizes the original marked hyperbolic filling,
and satisfies the absolute action-volume identity.

**Proof.** Theorem 6 excludes a negative corner endpoint of
magnitude at least four. Theorem 13 leaves only a negative endpoint
of magnitude three next to magnitude four or five; Lemma 14
excludes both cases. Thus there are no corners. Open sides were
already excluded by strict feasibility, so the unique minimum is
interior. Propositions 2--3 give the strict signs, and the pointwise
marked-completion theorem supplies the original filling and its
volume. All original topological hypotheses, primitive slopes,
carrier parities, and complete outside ends are retained.
\(\square\)

The threshold three is independent of path length. This is a
geometric theorem proved using a finite exact interval certificate.
The reduction to the remaining corner magnitudes three, four
and five uses the integer-power hypothesis. The theorem does
not assert interiority for an interpolation through arbitrary
real magnitudes between three and four.
Magnitude two remains unresolved by this argument. The theorem
does not establish the asymptotic of the original quantum source
or a nonzero coefficient of its geometric contribution.
