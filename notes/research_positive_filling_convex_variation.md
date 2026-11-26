# A convex variational problem for the primitive filling equations

Research note, 2 November 2026. Positive edge geometry admits bounded
real coordinates in which matching the angles and prescribing the
imaginary parts of the filling periods are linear conditions. A
strictly convex function then supplies the remaining equations:
matching the imaginary parts of the boundary coordinates and
vanishing of the real parts of the primitive filling periods.

This gives an exact variational formulation for arbitrary real
signed filling powers. It also identifies the remaining existence
issue. Even when the linear conditions have strictly positive angle
solutions, the minimum can occur at a corner of the closed angle
domain. Section 6 gives an explicit example in the original
circle-tree construction.

## 1. One square of positive coordinates

Use the canonical strip coordinates of
[the global monotonicity theorem](research_positive_edge_global_monotonicity.md).
For one strip variable write

\[
 P=x+iy,\qquad f(P)=\arctan(\tanh P)=A+iB,
 \qquad |\Im P|<\pi/4.
 \tag{1}
\]

The map \(P\mapsto(A,y)\) is a bijection onto the open square

\[
                         -\pi/4<A,y<\pi/4.
 \tag{2}
\]

Indeed, for fixed \(y\), the derivative
\(\partial A/\partial x=\Re\{\operatorname{sech}(2P)\}\)
is positive, while \(A\) tends to \(-\pi/4\) and \(\pi/4\)
as \(x\) tends to the two ends of the real line.

The inverse and the remaining imaginary coordinate are explicit:

\[
 \begin{aligned}
 x(A,y)&=\frac12\operatorname{arsinh}
                         \bigl(\tan(2A)\cos(2y)\bigr),\\
 B(A,y)&=\frac12\operatorname{arsinh}
                         \bigl(\tan(2y)\cos(2A)\bigr).
 \end{aligned}
 \tag{3}
\]

To verify these identities, put \(z=\tanh(x+iy)\).
Since \(f(P)=\arctan z\),

\[
 \tan(2A)=\frac{2\Re z}{1-|z|^2}
          =\frac{\sinh(2x)}{\cos(2y)},\qquad
 \tanh(2B)=\frac{2\Im z}{1+|z|^2}
          =\frac{\sin(2y)}{\cosh(2x)}.
\]

The first identity gives \(x\). Substituting it into the second
gives
\(\sinh(2B)=\tan(2y)\cos(2A)\), proving (3).
All inverse functions here are real and single valued.

Define

\[
 E(A,y)=\frac{\pi}{8}\{\psi(0,0)-\psi(4A,4y)\},
                         \qquad E(0,0)=0,
 \tag{4}
\]

where \(\psi\) is the original edge phase on its real branch.
Its derivatives in the square are

\[
                          dE=x\,dA+B\,dy.
 \tag{5}
\]

If
\(\Delta=\sqrt{1-\sin^2(2A)\sin^2(2y)}>0\), direct
differentiation gives

\[
 E''(A,y)=\frac1\Delta
 \begin{pmatrix}
  \cos(2y)/\cos(2A)&-\sin(2A)\sin(2y)\\
  -\sin(2A)\sin(2y)&\cos(2A)/\cos(2y)
 \end{pmatrix}.
 \tag{6}
\]

Both diagonal entries are positive and the determinant is one.
Thus \(E\) is strictly convex throughout the square.
This proof uses the explicit original phase; no existence theorem
for a different circle-pattern problem is being imported.

## 2. Angle and length coordinates at an original edge

For an oriented original edge \(e=(v,w)\), use two copies of the
square, with strip variables \(P,Q\). Write their coordinates as
\((A_P,y_P)\), \((A_Q,y_Q)\), and their complementary coordinates
as \(x_P,B_P,x_Q,B_Q\) from (3).

Write

\[
 \begin{aligned}
 s_v&=\Re t_v,& h_{v,e}&=\Im t_{v,e},&
 g_{v,e}&=\Im r_{v,e},& k_{v,e}&=\Re r_{v,e}.
 \end{aligned}
\]

The subscript \(e\) on \(h\) is retained until imaginary matching
has been imposed. The exact period identities are

\[
 \begin{array}{ll}
 s_v=2(A_P+A_Q),&s_w=2(y_P-y_Q),\\
 g_{v,e}=y_P+y_Q,&g_{w,e}=A_Q-A_P,\\
 h_{v,e}=2(B_P+B_Q),&h_{w,e}=-2(x_P-x_Q),\\
 k_{v,e}=x_P+x_Q,&k_{w,e}=B_P-B_Q.
 \end{array}
 \tag{7}
\]

They follow directly from equation (19) of the global monotonicity
note. In particular, the angle coordinates are related by an
invertible real linear transformation:

\[
 \begin{aligned}
 A_P&=s_v/4-g_{w,e}/2,&
 A_Q&=s_v/4+g_{w,e}/2,\\
 y_P&=g_{v,e}/2+s_w/4,&
 y_Q&=g_{v,e}/2-s_w/4.
 \end{aligned}
 \tag{8}
\]

The open square conditions are therefore exactly

\[
             |s_v|+2|g_{w,e}|<\pi,\qquad
             |s_w|+2|g_{v,e}|<\pi.
 \tag{9}
\]

These are strict linear inequalities after resolving the absolute
values into their finitely many sign choices.

For the edge energy \(E_e=E(A_P,y_P)+E(A_Q,y_Q)\), equations
(5), (7), and (8) give

\[
 4\,dE_e=
       k_{v,e}\,ds_v+k_{w,e}\,ds_w
       +h_{v,e}\,dg_{v,e}+h_{w,e}\,dg_{w,e}.
 \tag{10}
\]

For example, the coefficient of \(dg_{w,e}\) is
\(2(x_Q-x_P)=h_{w,e}\). This fixes both signs and the
factor four in the variational principle.

## 3. The linear feasible set and its energy

Let \(S\) be the selected vertices of an original circle tree,
and let \(B\) be its outside vertices incident to the included
edges. At a boundary vertex prescribe the full complex angle

\[
                              t_b=s_b+i h_b.
 \tag{11}
\]

At each selected vertex prescribe its real signed power \(n_v\)
and real cone charge \(c_v\).

Use a single real variable \(s_v\) for the real angle at each
selected vertex, and one real variable \(g_{v,e}\) for each
endpoint incidence of an included edge. The boundary \(s_b\)
are fixed. The open feasible set consists of these variables
subject to (9) at every edge and

\[
          \sum_{e\ni v}g_{v,e}-\frac{n_v}{2}s_v
                                      =-\pi c_v
                         \qquad(v\in S).
 \tag{12}
\]

The equations are affine and the inequalities are linear, so
this is a convex open polytope relative to its affine subspace.
All sums count endpoint incidences; if the same edge-block
formulas are used in a more general network, a loop contributes
both endpoints. Every included vertex is assumed incident to
an edge.

Define

\[
 \mathcal E
    =4\sum_e E_e
       -\sum_{b\in B}h_b\sum_{e\ni b}g_{b,e}.
 \tag{13}
\]

The second term records the prescribed imaginary boundary angles.
It is linear. The map from all endpoint angle variables to the
square coordinates in (8) is injective: recovering every endpoint
in an edge recovers each vertex variable, since each vertex is
incident to an edge. Equation (6) therefore makes \(\mathcal E\)
strictly convex on the open feasible set.

Let \(\overline{\mathcal P}\) denote its closure. When the open
feasible set is nonempty, this closure is the set obtained by
replacing (9) with weak inequalities and retaining (12). Indeed
the segment from any point satisfying the weak conditions to a
strictly feasible point is strictly feasible except at its weak
endpoint. The set is compact because (9) bounds every \(s_v\)
and every \(g_{v,e}\).

### Eliminating the incidence variables from strict feasibility

There is a direct finite system of inequalities for feasibility.
Normalize the real angles by \(\sigma_v=s_v/\pi\), and retain
the prescribed boundary values \(\sigma_b\).

**Proposition 1.** Suppose \(|\sigma_b|<1\) at every boundary
vertex. The open feasible set is nonempty if and only if
there are selected values \(|\sigma_v|<1\) such that

\[
       |n_v\sigma_v-2c_v|
           +\sum_{e=(v,w)}|\sigma_w|<d_v
                       \qquad(v\in S).
 \tag{23}
\]

The sum counts the opposite endpoint at each incidence.
For unit charges and complete boundary angles, this is
equivalent to the strict linear feasibility problem

\[
 \begin{gathered}
 0\le\tau_v<1,\qquad |n_v|\tau_v\le2,\\
 d_v-2+|n_v|\tau_v
        -\sum_{\substack{e=(v,w)\\w\in S}}\tau_w>0
                            \qquad(v\in S).
 \end{gathered}
 \tag{24}
\]

When \(n_v=0\), one may take \(\tau_v=0\).
In particular, all selected degrees at least three imply
strict feasibility for every choice of signed powers.

**Proof.** Once the \(\sigma\)'s are fixed, (9) says that
each normalized incidence value \(g_{v,e}/\pi\) varies
independently in
\[
 \left(-\frac{1-|\sigma_w|}{2},
          \frac{1-|\sigma_w|}{2}\right).
\]
Their sum must be \((n_v\sigma_v-2c_v)/2\).
The sum of finitely many open intervals is the open
interval whose endpoints are the sums of their endpoints.
This proves exactly (23). Incidences at different vertices
are independent after the real angles have been fixed;
outside incidences have no sum constraint.

For \(c_v=1\) and \(\sigma_b=0\), changing the sign of
\(\sigma_v\) to agree with \(n_v\) cannot increase
\(|n_v\sigma_v-2|\), and leaves all neighbor bounds
unchanged. If \(|n_v||\sigma_v|>2\), decreasing
\(|\sigma_v|\) to \(2/|n_v|\) improves its own inequality
and every neighbor inequality. At zero power one may
decrease it to zero. Thus one may assume
\(\sigma_v=\operatorname{sgn}(n_v)\tau_v\) and
\(|n_v|\tau_v\le2\). Substitution in (23) gives (24);
the converse is immediate. Taking every \(\tau_v=0\)
proves the last assertion. \(\square\)

The strict conditions in (24) can be checked by a linear
program with a common positive slack. This criterion
guarantees a unique minimum of the closed variational
problem below. It does not guarantee that the minimum is
interior.

## 4. The exact variational theorem

**Theorem 1.** Interior critical points of \(\mathcal E\) are
exactly the positive solutions of the original primitive filling
equations with boundary data (11):

\[
 R_v-\frac{i n_v}{2}t_v=-\pi i c_v,\qquad
 R_v=\sum_{e\ni v}r_{v,e}.
 \tag{14}
\]

An interior critical point is the unique global minimum on
\(\overline{\mathcal P}\). In particular the following two
conditions are equivalent:

1. The original equations admit a solution with every original
   edge tetrahedron positive on the complete logarithmic branches.
2. The minimum of (13) on \(\overline{\mathcal P}\) is interior.

Here the equivalence presupposes strict feasibility; a positive
solution itself implies that feasibility.

**Proof.** The equations (12) are linearly independent.
Each has its own incidence variables \(g_{v,e}\), with
coefficient one, and those variables occur in no other
selected-vertex equation. Attach real multipliers \(h_v\)
to (12), with Lagrangian

\[
 \mathcal L=\mathcal E-
   \sum_{v\in S}h_v
    \left(\sum_{e\ni v}g_{v,e}-\frac{n_v}{2}s_v+\pi c_v\right).
 \tag{15}
\]

Equation (10) shows that stationarity in each \(g_{v,e}\)
is precisely

\[
                    h_{v,e}=h_v\quad(v\in S),\qquad
                    h_{b,e}=h_b\quad(b\in B).
 \tag{16}
\]

Thus all endpoint imaginary angles match the same original
vertex coordinate. Stationarity in \(s_v\) is

\[
                       \sum_{e\ni v}k_{v,e}
                                     +\frac{n_v}{2}h_v=0.
 \tag{17}
\]

Together, (12) and (17) are exactly the imaginary and real
parts of (14). The square construction gives the canonical
positive edge shapes and their full period branches.
Conversely any such solution supplies the multipliers \(h_v\)
and satisfies all equations (15)--(17).

Strict convexity gives uniqueness of an interior critical
point and makes it a global minimum. The continuous extension
proved in Section 5 extends the comparison to the boundary.
It is still a strict comparison: the segment from an interior
critical point to a distinct boundary point is interior before
its endpoint and has positive second derivative. Hence a
boundary point cannot have the same value. Compactness gives
existence of a minimum on the closure. \(\square\)

The original carriers and slopes are unchanged:
\(n_v=\eta_v-2p_v\),
\(U_v=2R_v-i\eta_vt_v\), and \(V_v=2it_v\).
Equation (14) is therefore
\(U_v+p_vV_v=-2\pi i c_v\), with the original primitive basis.

If the powers \(n_v\) and charges \(c_v\) are integers and
the boundary tangents are algebraic, any interior solution
also has algebraic tangents \(a_v=\tan(t_v/2)\) and edge
coordinates \(q_e\). Indeed, exponentiating twice (14)
gives the rational algebraic system
\[
 \left(\prod_{e\ni v}\frac{q_e+a_v}{q_e-a_v}\right)
       \left(\frac{1-i a_v}{1+i a_v}\right)^{n_v}=1,
 \qquad q_e^2=1+a_v^2+a_w^2.
 \tag{25}
\]
Every denominator is nonzero on the positive domain.
The nonzero \(q_e\)'s allow the square equations to be
solved locally for the edge variables; the nonsingular
period Jacobian and
\(dt_v/da_v=2/(1+a_v^2)\ne0\) then make this an isolated
solution of (25). An isolated solution of polynomial
equations over the algebraic numbers is algebraic: its
zero-dimensional component has algebraic coordinate
residues, equivalently elimination gives algebraic
equations for each coordinate.
The original logarithmic equations still select the
correct branches among the solutions of (25). This
recovers the usual gluing-equation algebraicity; it is
not a statement about the quantum leading coefficient.

## 5. What a boundary minimum can look like

The function \(E\) extends continuously to the closed square.
To see this, (3) gives the uniform bounds

\[
 |E_A(A,y)|\le\frac12\operatorname{arsinh}|\tan(2A)|,\qquad
 |E_y(A,y)|\le\frac12\operatorname{arsinh}|\tan(2y)|.
 \tag{18}
\]

The functions on the right have only integrable logarithmic
singularities at the interval endpoints. Integrating along
coordinate segments proves uniform continuity up to the
closed square. This also proves the continuous extension
used in Theorem 1.

The open sides and the corners behave differently. Suppose
that a line enters the square through the side \(A=\pi/4\),
with

\[
 A(s)=\pi/4-\alpha s,\qquad
 y(s)=y_0+\beta s,\qquad
 \alpha>0,\quad |y_0|<\pi/4.
\]

Equation (3) gives
\(x(A(s),y(s))=\tfrac12\log(1/s)+O(1)\) and
\(B(A(s),y(s))\to0\). Thus

\[
                  \frac{d}{ds}E(A(s),y(s))\longrightarrow-\infty.
 \tag{19}
\]

The other three open sides have the same conclusion.

At a corner, write an inward line as

\[
 A(s)=\epsilon_A(\pi/4-\alpha s),\qquad
 y(s)=\epsilon_y(\pi/4-\beta s),\qquad
 \alpha,\beta>0,\quad \epsilon_A,\epsilon_y\in\{-1,1\}.
\]

In this case (3) gives finite limits

\[
 x\longrightarrow
       \frac{\epsilon_A}{2}\operatorname{arsinh}(\beta/\alpha),
 \qquad
 B\longrightarrow
       \frac{\epsilon_y}{2}\operatorname{arsinh}(\alpha/\beta),
\]

and hence

\[
 \frac{dE}{ds}\longrightarrow
 -\frac12\left[
   \alpha\operatorname{arsinh}(\beta/\alpha)
  +\beta\operatorname{arsinh}(\alpha/\beta)\right].
 \tag{20}
\]

This limit is finite. Consequently a corner contribution
does not supply the infinite inward decrease available at
an open side.

**Proposition 2.** Assume strict feasibility. At any minimum of
\(\mathcal E\) on \(\overline{\mathcal P}\), each square factor
is either interior or at a corner. No factor lies on an open side.

**Proof.** Join the putative minimum by a segment to a strictly
feasible point. The affine equations remain satisfied and every
square becomes strictly interior along the segment. Each
open-side factor contributes a derivative tending to
\(-\infty\) by (19). Interior factors have finite derivatives;
corner factors have finite derivatives by (20); and the boundary
term in (13) is linear. Thus if an open-side factor were present,
the total energy would strictly decrease along this segment
near its initial point. This contradicts minimality. \(\square\)

Therefore strict feasibility reduces the existence problem to
excluding corner minima. It does not exclude them automatically.

**Corollary 3.** Under strict feasibility, \(\mathcal E\) has a
unique minimum on \(\overline{\mathcal P}\), including when the
minimum has corner factors.

**Proof.** A minimum exists by compactness and continuity.
Suppose two different minima existed. Convexity makes their
entire segment a segment of minima. The square-coordinate
map (8) is injective, so at least one square factor differs
between the endpoints.

By Proposition 2 each endpoint factor is either interior or
a corner. If the differing factor has an interior endpoint,
or if it joins opposite corners, its segment passes through
the square interior. There its second derivative in that
nonzero direction is positive by (6). The other factors
are convex and the boundary term is linear, so the total
energy cannot be constant along the segment.

The remaining possibility is a pair of distinct adjacent
corners. Their midpoint lies on an open side. The midpoint
of the full segment would then be a minimum with an
open-side factor, contradicting Proposition 2. Thus the
minimum is unique. \(\square\)

## 6. A strictly feasible example with no positive solution

Consider two adjacent selected vertices \(v,w\), each of original
degree three. Each has two other neighbors, whose angles are fixed
at zero. Set \(n_v=n_w=0\) and \(c_v=c_w=1\). This is an original
circle tree with six vertices, not a modification of its
incidence rules.

The linear conditions are strictly feasible. Set every real
angle \(s\) to zero, put \(g_{v,e}=g_{w,e}=-\pi/3\) at every
selected incidence, and set the incidence values at the four
outside endpoints to zero. Each selected sum is \(-\pi\),
and every inequality in (9) is strict.

Nevertheless there is no positive solution of (14) in the
original two-octahedron edge decomposition.

**Proof.** The global uniqueness theorem applies if a positive
solution exists. Complex reflection
\(\mathbf t\mapsto-\overline{\mathbf t}\) preserves the
positive domain and, at zero powers and these real charges,
preserves the equations. The increments transform as
\(r\mapsto-\overline r\) on the canonical branches.
Uniqueness therefore forces all selected angles to be purely
imaginary. Interchanging the two selected vertices and their
identical complete neighbors is another symmetry, so

\[
                              t_v=t_w=-ih
\]

for a real \(h\). Positivity of the internal edge requires
\(|\sinh(h/2)|<1\), by the regular-edge condition. The
selected equation becomes

\[
         2\arcsin\bigl(\tanh(h/2)\bigr)
             +\arcsin\bigl(\sinh(h/2)\bigr)=\pi.
 \tag{21}
\]

If \(h\le0\), its left side is nonpositive. For
\(0<h<2\operatorname{arsinh}1\), both terms increase strictly,
and their sum is strictly less than its endpoint value

\[
                    2\arcsin(1/\sqrt2)+\arcsin(1)=\pi.
 \tag{22}
\]

Thus (21) has no positive regular solution. \(\square\)

At the limiting value \(h=2\operatorname{arsinh}1\), the internal
incidences have \(g=-\pi/2\), and the incidences towards the
complete neighbors have \(g=-\pi/4\). The selected sums are
still \(-\pi\). The two square factors of the internal edge
are corners; the four outside edges remain strictly positive.
The internal edge has \(q=0\), a degeneration of this
particular subdivision.

For charges \(c_v=c_w=\lambda<1\), equation (21) with
right-hand side \(\pi\lambda\) has a unique solution in the
regular interval. These solutions are interior minima by
Theorem 1 and converge to the displayed corner assignment.
It is a minimum at \(\lambda=1\): any feasible assignment
at unit charge can be scaled by \(\lambda\) in the angle
variables to give one at charge \(\lambda\); continuity of
the energy then permits passage to the minimum inequality
as \(\lambda\uparrow1\).

This does not imply that the corresponding partially filled
manifold is nonhyperbolic. The
[zero-subtree Conway construction](research_zero_subtree_conway_geometry.md)
uses a different positive cell decomposition after literal
zero-box deletion. The example shows that strict feasibility
of the original angle constraints does not ensure an interior
minimum for the original edge subdivision.

## 7. Scope of the variational reformulation

For arbitrary signed powers and fixed boundary coordinates,
the positive primitive problem is now one strictly convex
minimization problem on an explicit finite-dimensional
polytope. Under strict feasibility the closed problem always
has a unique minimizer; that minimizer can have corner factors.
Its interior Euler--Lagrange equations retain the
original slopes, carriers, and full logarithmic periods.
The possible boundary obstruction is restricted by
Proposition 2 to corner degenerations.

The minimum value of \(\mathcal E\), especially at a corner
configuration, is not identified here with hyperbolic volume.
The volume normalization of an interior geometric solution
still uses its original primitive periods and the separately
proved Schläfli calibration.

To obtain existence for a wider geometric class one must
exclude those corner minima, or replace their degenerate
cells by a compatible positive decomposition and prove
the transition. The example above requires precisely such
a replacement. None of these variational statements
controls the nonpositive critical points, boundary cycles,
or leading coefficient of the original quantum period.
