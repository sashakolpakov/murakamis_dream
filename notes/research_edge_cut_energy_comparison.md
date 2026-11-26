# The convex energy and the cost of joining two path pieces

Research note, 3 November 2026. Frozen manuscripts are unchanged.

The convex square energy already used to solve the marked filling
equations determines the absolute stationary action. Its vertex
symmetries give explicit feasible comparisons as the filling powers
increase. Combined with a uniform geometric height bound, they prove
the edge comparison for positive integer-power paths whenever either
endpoint has power at least \(562\) and all powers are at least three.
The threshold is independent of the path length and the other powers.
More generally, Section 7 gives an explicit energy budget for any
set of activated vertices, including the endpoints of a radical
matching. The comparison for arbitrary adjacent small powers remains
open. The final section states separately the whole-boundary source
estimates needed to turn this geometric budget into a bound on a
quantum remainder.

Put
\[
 G=\sum_{j=0}^{\infty}\frac{(-1)^j}{(2j+1)^2},
 \qquad M_\infty=\psi(0,0)=\frac{4G}{\pi}.
 \tag{1}
\]
All edge phases and logarithms have the original normalization.
The geometric coordinates and the square energy are those of
[the convex filling variation](research_positive_filling_convex_variation.md).
For an endpoint of an edge, write
\[
 t_v=s_v+i h_v,\qquad r_{v,e}=k_{v,e}+i g_{v,e},
 \qquad \psi_{t_v}=-r_{v,e}/\pi.
 \tag{2}
\]
In particular \(h_v\) is negative on the positive-power geometric
branch. It is not the positive height magnitude used in some contour
estimates.

## 1. The absolute identity on one edge

Each original positive edge has two squares, with coordinates
\((A_P,y_P)\) and \((A_Q,y_Q)\). Their energy satisfies
\[
 4\,d(E_P+E_Q)
   =k_{v,e}\,ds_v+k_{w,e}\,ds_w
        +h_v\,dg_{v,e}+h_w\,dg_{w,e}.
 \tag{3}
\]
It vanishes at the complete edge. The square energy is an ordinary
real function; its differential and its value at completeness fix
the normalization.

**Lemma 1.** On the original positive edge branch,
\[
 \boxed{\;
 4(E_P+E_Q)
   =\pi\{M_\infty-\Re\psi(t_v,t_w)\}
                      +h_vg_{v,e}+h_wg_{w,e}.
 \;}
 \tag{4}
\]

**Proof.** Equation (2) gives
\[
 -\pi\,d\Re\psi
   =k_{v,e}\,ds_v-g_{v,e}\,dh_v
           +k_{w,e}\,ds_w-g_{w,e}\,dh_w.
 \tag{5}
\]
Adding \(d(h_vg_{v,e}+h_wg_{w,e})\) gives (3).
Thus the difference between the two sides of (4) is constant.
The original positive strip coordinates connect this branch to
the complete edge, where both sides vanish. This proves the
identity with its absolute constant. No logarithmic branch is
reset during this continuation. \(\square\)

## 2. The convex minimum and the stationary action

Let \(\Gamma\) be a finite original path, with complete outside
vertices. Retain every original edge, including an edge whose two
endpoints happen to be complete. Write \(e=|E(\Gamma)|\). At the
selected vertices prescribe real powers \(n_v\) and charges
\(\lambda_v\). The angle constraints are
\[
 \sum_{a\ni v}g_{v,a}-\frac{n_v}{2}s_v=-\pi\lambda_v.
 \tag{6}
\]
The real energy is
\[
 \mathcal E_\Gamma=4\sum_{a\in E(\Gamma)}(E_{P,a}+E_{Q,a}).
 \tag{7}
\]
The linear boundary term in the general variational problem is
zero here, since the outside angles are complete.

Suppose the original marked stationary solution is positive.
The strict convexity theorem identifies its real angle coordinates
with the unique minimum of (7) under (6) and the edge inequalities.
Denote this minimum by \(F_\Gamma(\lambda)\). Define
\[
 \begin{split}
 \Phi_\lambda(t)
   &=\sum_{\{v,w\}}\psi(t_v,t_w)
       +\sum_{v}\frac{i n_vt_v^2}{4\pi}
                        -i\sum_v\lambda_vt_v,\\
 M_\Gamma(\lambda)&=\Re\Phi_\lambda(t(\lambda)).
 \end{split}
 \tag{8}
\]

**Theorem 2.** At every such positive stationary solution,
\[
 \boxed{\quad
 F_\Gamma(\lambda)
        =\pi\{eM_\infty-M_\Gamma(\lambda)\}.
 \quad}
 \tag{9}
\]

**Proof.** Sum (4) over the original edges. The terms containing
the matched imaginary coordinates give, by (6),
\[
 \sum_v h_v\sum_{a\ni v}g_{v,a}
       =\sum_v\left(\frac{n_vs_vh_v}{2}
                                      -\pi\lambda_vh_v\right).
 \tag{10}
\]
Outside vertices contribute zero. On the other hand,
\[
 \Re\!\left(\frac{i n_vt_v^2}{4\pi}-i\lambda_vt_v\right)
           =-\frac{n_vs_vh_v}{2\pi}+\lambda_vh_v.
 \tag{11}
\]
Substitution gives (9), and the convex minimum theorem gives the
asserted interpretation of its left side. \(\square\)

This proof is pointwise. It does not assume that every intermediate
fractional charge has an interior geometric solution. Such an
assumption would be unnecessary when comparing two already proved
positive endpoints. The identity is not asserted here for a minimum
at a corner without its positive geometric interpretation.

## 3. Zeroing the charges at the ends of one edge

Assume now that all selected powers are positive integers at least
three, and that the selected path has complete outside endpoints.
The
[positive-path existence theorem, after mirroring](research_negative_corridor_variational_bounds.md)
supplies its positive unit-charge solution.

Choose an edge \(a=\{v,w\}\) joining two selected vertices. Let
\(\lambda^a\) equal zero at \(v,w\) and one at the other selected
vertices. Delete \(a\), make \(v,w\) complete boundary vertices, and
retain the two resulting path pieces, denoted \(L\) and \(R\).
All other powers and all original edge constants are retained.
If a piece has no selected vertices, its edges are complete and
its minimum energy is zero.

Each piece has its positive solution by the same existence theorem.
Joining those two solutions by the complete edge \((t_v,t_w)=(0,0)\)
gives a positive stationary solution for \(\lambda^a\).
Indeed \(r_{v,b}(0,t)=0\) at every incidence of a zero-angle
vertex, so its zero-charge equation holds exactly. Strict convexity
then identifies this joined solution with the relevant minimum.
The complete connecting edge has zero square energy, hence
\[
                 F_\Gamma(\lambda^a)=F_L+F_R.
 \tag{12}
\]

**Corollary 3.** The exact action cost of activating the two
charges is
\[
 M_\Gamma(\lambda^a)-M_\Gamma(\mathbf1)
       =\frac{F_\Gamma(\mathbf1)-F_L-F_R}{\pi}.
 \tag{13}
\]
Consequently the proposed edge comparison
\[
           M_\Gamma(\lambda^a)-M_\Gamma(\mathbf1)<M_\infty
 \tag{14}
\]
is equivalent to the following inequality for convex minima:
\[
 \boxed{\qquad
                F_\Gamma(\mathbf1)<F_L+F_R+4G.
 \qquad}
 \tag{15}
\]
Equivalently, since the complete connecting edge contributes
\(M_\infty\) to the stationary action,
\[
                   M_\Gamma(\mathbf1)>M_L+M_R.
 \tag{16}
\]

Equations (13), (15) and (16) are exact reformulations. The strict
inequality in (14)--(16) remains unproved for all such paths.
Convexity by itself does not compare these three minima: activating
the two charges changes the constraints and the angles on their
other incident edges.

There is a useful reduction for several disjoint edges. If (14)
holds for every positive path piece with complete endpoints, it
can be applied successively to a matching \(\mathscr S\). Its edges
do not share endpoints, so at each step the two new zero charges
belong to one remaining selected path component. The resulting
costs telescope:
\[
 M_\Gamma(\lambda^{\mathscr S})-M_\Gamma(\mathbf1)
                             <|\mathscr S|M_\infty.
 \tag{17}
\]
A uniform improvement \(M_\infty-\delta\) in (14) would give the
same improvement \(|\mathscr S|\delta\) in (17). This is a deduction
from the stated single-edge inequality, not a proof of that
inequality.

## 4. The remaining quantum estimate

The proposed application separates high Newton indices before
deforming the remaining kernel. Even a proof of (15) would still
need an exact estimate for those original finite sectors. One must
show how their full Hermite traces, including the first normal
derivatives, are controlled by the corresponding path with the
edge deleted and its endpoint charges zero. An action comparison
alone does not identify that finite trace or bound it.

Exploratory calculations support (14) but are not certificates.
For a path with twenty-four selected vertices, all of power three,
zeroing its central adjacent pair gives a calculated cost about
\(1.11212826\), compared with \(M_\infty\approx1.16624362\).
They also warn against a simple monotonicity argument: for the
twelve-vertex pattern consisting of five powers \(n\), the pair
\(3,3\), and five further powers \(n\), the calculated costs at
\(n=8,16,64\) are approximately \(0.970123,0.968733,0.970915\).
These observations neither prove (15) nor establish a monotonicity
counterexample without rigorous error enclosures.

## 5. The two new vertices cannot be the only variables changed

A local gluing construction must allow some of the old angle
coordinates to move. Merely optimizing the new two vertices while
keeping the old halves fixed can cost more than \(4G\). This
limitation already occurs in a path with four selected vertices,
all of power three, and two complete outside endpoints.

Zero the charges at the two middle vertices. Each old half then
has one selected power-three vertex between two complete endpoints.
Its selected angle \(t=S-iH\) is specified exactly as follows.
Let \(k\) be the unique root of
\[
 4k^4-4k^3+k^2-2k+2=0,\qquad
 .84<\Re k<.85,\quad .29<\Im k<.30,
 \qquad t=2\arccos k.
 \tag{18}
\]
The inverse cosine is on the branch with \(0<\Re t<\pi\) and
\(\Im t<0\). The original return and its imaginary part are
\[
 r=\operatorname{arsinh}(\tan(t/2))
           =\frac{3it}{4}-\frac{\pi i}{2},\qquad
                  G_0=\Im r=\frac{3S}{4}-\frac\pi2.
 \tag{19}
\]
In particular \(3t+4ir=2\pi\), the full original stationary
equation. Numerically \(S\approx1.381983397\) and
\(G_0\approx-.534308779\); the proof below uses the algebraic
root enclosure, not these decimal approximations.

To check (19), write \(a=t/2=\arccos k\). Multiplying the
polynomial in (18) by \(k+1\) gives
\(4k^5-3k^3-k^2+2=0\), and hence
\(\cos^2(3a/2)+\tan^2a=0\). The root enclosure excludes
\(\cos(3a/2)+i\tan a=0\), so
\(\cos(3a/2)=i\tan a\). The number
\(i(3a-\pi)/2\) has positive real part and imaginary part
strictly between \(-\pi/2\) and \(\pi/2\).
It is therefore the specified inverse hyperbolic sine.
The angle and return lie in the positive edge domain.
The unique-minimum theorem identifies this solution with
the old half-path minimum.

**Proposition 4.** Freeze all the angle and incidence coordinates
in these two old halves, including the old endpoints of their
edges to the two middle vertices. Allow arbitrary feasible changes
at the two middle vertices, and activate both their unit charges.
Every such change increases the energy by more than
\[
                             4G+\frac9{250}.
 \tag{20}
\]
Thus this restricted construction cannot prove (15).
The proposition is not a counterexample to (15), whose minimum
allows all the old coordinates to relax.

**Proof.** The allowed set is a closed convex polytope: its
constraints are the original affine filling equations and square
inequalities. Its energy is convex. Reflection of the path exchanges
the two new vertices and preserves both the frozen data and the
energy. Averaging a feasible point with its reflection cannot
increase energy. It is consequently enough to give a lower bound
on the symmetric feasible configurations.

Let \(s\) be their common real angle and \(g\) their common
incidence value on the edge toward an old half. The incidence
value on the new middle edge is then
\(g_c=3s/2-\pi-g\). Put
\[
 x=-G_0/2,\quad y=S/4,\qquad
 A=\frac{\pi+g-s}{2},\quad Y=s-\frac{\pi+g}{2}.
 \tag{21}
\]
The new middle edge has energy \(8E(A,Y)\). The change on
each attachment edge is
\[
 4\{E(x+s/4,y+g/2)+E(x-s/4,y-g/2)-2E(x,y)\}.
\]
Here separate evenness of \(E\) has been used to express both
old squares at the same coordinates. Thus the total change is
the convex function
\[
 C(s,g)=8E(A,Y)+8\{E(x+s/4,y+g/2)
                    +E(x-s/4,y-g/2)-2E(x,y)\}.
 \tag{22}
\]
This is the energy change of the literal three affected edges.
The old edges farther from the middle pair cancel exactly.

Every feasible point has \(|s|\le\pi\) and \(|g|\le\pi/2\).
Choose the rational, strictly feasible point
\[
                 s_0=1.59335955,\qquad g_0=-.39124668.
 \tag{23}
\]
The supporting-plane inequality for the convex function (22)
therefore gives, on its entire feasible domain,
\[
 \begin{split}
 C(s,g)&\ge C(s_0,g_0)
       -2\pi|C_s(s_0,g_0)|-\pi|C_g(s_0,g_0)|\\
       &>\frac{37}{10},\qquad
                         4G<\frac{458}{125}.
 \end{split}
 \tag{24}
\]
The first line uses \(|s-s_0|<2\pi\) and
\(|g-g_0|<\pi\). Convexity and continuity extend the inequality
to boundary squares as well.

The strict bounds in (24) are certified by
[the supporting-plane checker](../experiments/check_frozen_collar_energy_obstruction.py)
using real and complex ball arithmetic. It isolates the four
roots of the exact polynomial (18), selects its stipulated
root, checks the logarithmic branch and strict feasibility of
(23), and evaluates \(E\) and its derivatives with outward
error bounds. The derivative formulas are exactly (3) of the
convex filling variation. No minimum is assumed at (23).
For orientation, the resulting lower endpoint in (24) exceeds
\(3.70150265\). The
[saved certificate](../repro/results/research-frozen-collar-energy.json)
records its full enclosure.
Since \(37/10-458/125=9/250\), this proves (20). \(\square\)

The next constructive problem is therefore a collar adjustment:
the old first vertices or further old incidences must be allowed
to change. Neither this proposition nor the isolated two-vertex
trial supplies a uniform bound for that larger adjustment.

## 6. It suffices to insert two vertices of power three

There is a useful reduction of the powers at the two vertices being
activated. It is a comparison of explicit feasible angle assignments,
so it does not require interiority along a fractional-charge or
fractional-power deformation.

For a selected vertex \(v\), call
\[
                   X_v=(s_v,(g_{v,e})_{e\ni v})
 \tag{25}
\]
its vertex block. The constraints at complete outside boundaries are
\[
 \sum_{e\ni v}g_{v,e}-\frac{n_v}{2}s_v=-\pi,\qquad
 |s_v|+2|g_{w,e}|<\pi,\quad
 |s_w|+2|g_{v,e}|<\pi.
 \tag{26}
\]
In this section all original selected powers are positive integers
at least three. Their positive minimum has \(s_v>0\), by the
mirrored corridor theorem.

**Lemma 5.** Negating any one vertex block preserves the total
square energy. Consequently, for \(0\le\tau\le1\), multiplying
that block by \(\tau\), while holding all other blocks fixed,
cannot increase the energy. It preserves every closed or open
edge inequality in (26).

**Proof.** Orient an incident edge from \(v\) to \(w\). Its square
coordinates are
\[
 \begin{split}
 A_P=s_v/4-g_{w,e}/2,\quad&A_Q=s_v/4+g_{w,e}/2,\\
 y_P=g_{v,e}/2+s_w/4,\quad&y_Q=g_{v,e}/2-s_w/4.
 \end{split}
 \tag{27}
\]
Negating \(X_v\) sends the two pairs to
\((-A_Q,-y_Q)\) and \((-A_P,-y_P)\). Negating \(X_w\)
instead exchanges the two pairs. The square energy is even in
each coordinate, so either operation preserves their sum.
This proves independent evenness in every vertex block.

The assignment with block \(\tau X_v\) is the convex combination
of the assignments with blocks \(X_v\) and \(-X_v\), with
weights \((1+\tau)/2\) and \((1-\tau)/2\). Convexity of the
energy proves its nonincrease. The edge inequalities depend only
on the absolute values of the individual block entries and are
preserved as those decrease. If the initial assignment is in the
open angle domain, \(X_v\ne0\), and \(\tau<1\), strict convexity
there gives a strict energy decrease. \(\square\)

**Proposition 6.** Let \(F_\Gamma(\mathbf n)\) denote the closed
convex minimum at unit charges and complete outside boundaries.
If \(\mathbf n\) consists of integers at least three and
\(n'_v\ge n_v\) at every selected vertex, then
\[
                         F_\Gamma(\mathbf n')
                                  \le F_\Gamma(\mathbf n).
 \tag{28}
\]
The new powers may be real. If at least one power is strictly
increased, the inequality is strict. This assertion about the
closed minimum does not assert geometric interiority at the new
real powers.

**Proof.** Start at the proved positive minimum for \(\mathbf n\).
For every changed vertex set
\[
 \tau_v=
   \frac{\pi}{\pi+(n'_v-n_v)s_v/2},\qquad
          s'_v=\tau_vs_v,\quad g'_{v,e}=\tau_vg_{v,e}.
 \tag{29}
\]
Since \(s_v>0\), one has \(0<\tau_v\le1\).
The new constraint is exactly
\[
 \begin{split}
 \sum_{e\ni v}g'_{v,e}-\frac{n'_v}{2}s'_v
 &=\tau_v\left[-\pi-\frac{(n'_v-n_v)s_v}{2}\right]\\
 &=-\pi.
 \end{split}
 \tag{30}
\]
Each vertex constraint uses only its own block. Thus these
scalings commute, do not alter any other vertex constraint, and
produce a strictly feasible assignment for \(\mathbf n'\).
Lemma 5 bounds its energy by the old minimum. A changed power
has \(\tau_v<1\) and a nonzero block, so that step strictly
decreases energy. Taking the new minimum proves (28).
\(\square\)

**Corollary 7.** In the desired single-edge comparison (15), it
suffices to prove the case in which the two activated vertices
have powers \(3,3\). The powers on both old pieces remain arbitrary
positive integers at least three.

**Proof.** Fix the old pieces and all their powers. The quantity
\(F_L+F_R\) does not depend on the powers assigned to the two
zero-angle vertices. Replace those powers by three in the full
path. Its positive unit-charge minimum exists by the integer
corridor theorem. Proposition 6 then gives, for any assigned
endpoint powers \(n,p\ge3\),
\[
 F_\Gamma(\ldots,n,p,\ldots)-F_L-F_R
 \le
 F_\Gamma(\ldots,3,3,\ldots)-F_L-F_R.
 \tag{31}
\]
Thus a strict upper bound \(4G\) for the right side gives the
same strict bound for every \(n,p\ge3\). \(\square\)

This reduction concerns the two newly activated powers only.
Changing a power inside an old piece changes both the full
minimum and \(F_L+F_R\); Proposition 6 does not order their
difference. In particular it does not reduce the old pieces to
all-three paths. The remaining problem is the uniform insertion
of a \(3,3\) pair into arbitrary old positive paths, allowing
their collar coordinates to relax. Inequality (31) reduces that
problem's power dependence but does not prove its \(4G\) bound.

There is also a quantitative trial that relaxes all old coordinates.
Fix the old pieces as above and write
\[
       \mathcal C(n,p)=
          F_\Gamma(\ldots,n,p,\ldots)-F_L-F_R.
 \tag{32}
\]
Let \(X^*\) be the full minimum with new powers \(3,3\), and let
\(s_v^*,s_w^*>0\) be its two new real angles.

**Corollary 8.** For every \(n,p\ge3\), put
\[
 \begin{split}
 \tau_v&=\frac{\pi}{\pi+(n-3)s_v^*/2},&
 \tau_w&=\frac{\pi}{\pi+(p-3)s_w^*/2},\\
 \tau&=\max(\tau_v,\tau_w).
 \end{split}
 \qquad
                  \mathcal C(n,p)\le\tau\,\mathcal C(3,3).
 \tag{33}
\]
The target minimum in this inequality may again be the closed
minimum at real powers. The input \(X^*\) is the already-proved
positive integer-power geometry.

**Proof.** Let \(X^0\) be the two old minima joined by the
complete central edge. Its new vertex blocks are zero,
its old constraints have charge one, and
\(\mathcal E(X^0)=F_L+F_R\).
The assignment
\(\widetilde X=\tau X^*+(1-\tau)X^0\)
is strictly positive and preserves every old unit constraint.
Its new vertex blocks are \(\tau X_v^*,\tau X_w^*\).
Contract those blocks by the additional factors
\(\tau_v/\tau,\tau_w/\tau\), respectively.
Equation (30) verifies the desired unit constraints at powers
\(n,p\), and Lemma 5 preserves positivity and decreases energy.
The final feasible assignment therefore has energy at most
\[
       \tau F_\Gamma(\ldots,3,3,\ldots)
                       +(1-\tau)(F_L+F_R).
 \]
Taking its minimum and subtracting \(F_L+F_R\) proves (33).
\(\square\)

The trial in Corollary 8 changes the old pieces by a convex
interpolation; it is not a path of stationary geometric solutions.
It shows that their relaxed insertion cost contracts explicitly
when both new powers increase. It supplies no uniform bound for
the still-unknown reference cost \(\mathcal C(3,3)\).

One can also retain the cases where only one new vertex is active.
Keep the two reference powers equal to three. For
\((a,b)\in\{0,1\}^2\), let \(X^{ab}\) be the positive minimum
whose two new charges are \(a,b\), with all old charges one,
and write \(F_{ab}=\mathcal E(X^{ab})\).
These four points exist without a fractional-charge theorem:
make every zero-charge vertex complete, solve each remaining
integer-power path component, and join them along the complete
vertices. At a complete vertex both its angle and every return
are zero, so its zero-charge equation holds exactly. Strict
convexity identifies the joined positive solution with the
minimum. In particular \(F_{00}=F_L+F_R\) and \(F_{11}\) is
the full \(3,3\) minimum.

Let the two positive conditional angle minima be
\[
       m_v=\min(s_v^{10},s_v^{11})>0,\qquad
       m_w=\min(s_w^{01},s_w^{11})>0.
 \tag{34}
\]

**Corollary 9.** For target powers \(n,p\ge3\), define
\[
 \alpha=\frac1{1+(n-3)m_v/(2\pi)},\qquad
 \beta =\frac1{1+(p-3)m_w/(2\pi)}.
 \tag{35}
\]
Then the following explicit bound holds:
\[
 \begin{split}
 F_\Gamma(\ldots,n,p,\ldots)\le{}&
 (1-\alpha)(1-\beta)F_{00}
       +\alpha(1-\beta)F_{10}\\
 &+(1-\alpha)\beta F_{01}+\alpha\beta F_{11}.
 \end{split}
 \tag{36}
\]

**Proof.** Take the convex combination \(\overline X\) of the
four positive assignments with the four weights in (36).
All old unit constraints remain exact. The new vertex \(v\)
has charge \(\alpha\) for the reference power three and has
real angle
\[
       \overline s_v=
          \alpha\{(1-\beta)s_v^{10}+\beta s_v^{11}\}.
 \]
At the target power \(n\), its constraint value is consequently
\[
 -\pi\alpha\left[
    1+\frac{n-3}{2\pi}
                   \{(1-\beta)s_v^{10}+\beta s_v^{11}\}\right]
                  \le-\pi.
 \tag{37}
\]
The inequality is exactly the choice of \(m_v,\alpha\).
Contract the entire \(v\)-block by \(-\pi\) divided by this
negative constraint value. The factor belongs to \((0,1]\)
and makes its constraint equal to \(-\pi\).
Do the same at \(w\), using \(m_w,\beta\).
Neither contraction changes any other vertex constraint;
Lemma 5 preserves the open angle domain and decreases energy.
Convexity bounds the energy before contraction by the right side
of (36). Taking the new minimum proves the claim. \(\square\)

For example, with \(p=3\), this gives the one-sided estimate
\[
 \mathcal C(n,3)\le
      (1-\alpha)(F_{01}-F_{00})
                      +\alpha(F_{11}-F_{00}).
 \tag{38}
\]
Thus a strict bound \(F_{01}-F_{00}<4G\) for that particular
single activation implies the desired edge comparison for all
sufficiently large \(n\), with the other new power still three.
Formula (38) gives a threshold directly from the two energy
differences and \(m_v\). Section 7 supplies a uniform
single-activation bound and a uniform lower bound for \(m_v\).

The construction extends to any fixed set \(T\) of increased
powers. Use reference power three at these vertices and the
positive minima \(X^\epsilon\), \(\epsilon\in\{0,1\}^T\),
obtained by completing their zero-charge vertices. Set
\[
 m_v=\min_{\epsilon_v=1}s_v^\epsilon>0,\qquad
 \alpha_v=\frac1{1+(n_v-3)m_v/(2\pi)}.
 \]
Their convex combination with independent Bernoulli weights
\(\prod_v\alpha_v^{\epsilon_v}(1-\alpha_v)^{1-\epsilon_v}\)
has every target constraint at most \(-\pi\).
Contracting the corresponding blocks makes all constraints exact,
with no energy increase. Hence the same weighted average of the
energies \(F_\epsilon\) is an upper bound for the target minimum.
This uses only finitely many completed integer-power geometries
and explicit feasible assignments; it does not assume the
fractional-charge cube consists of geometric minima.

## 7. Consequences of a uniform height bound

The
[uniform height theorem](research_positive_path_height_bound.md)
proves the following geometric estimate:
\[
 \begin{gathered}
 0<H_v=-\Im t_v<\overline H,\qquad \overline H=\frac{23}{20},
 \\
 \text{for every active vertex of every positive integer-power
 path with all active powers at least three.}
 \end{gathered}
 \tag{39}
\]
The same theorem applies after any collection of vertices is made
complete. Those configurations are the positive path components
already used in Corollary 9. Its proof uses a maximum principle for
the original returns and an outward interval certificate for a
compact support inequality. The following consequences use only
the bound (39), the positive integer-power geometry, and the convex
comparisons of Section 6.

**Lemma 10.** Activating one charge, while keeping every
other charge zero or one, increases the minimum energy by less than
\[
                         B=\frac{23\pi}{20}.
 \tag{40}
\]
The power at the activated vertex may be any integer at least three.

**Proof.** Let \(X^1\) be the positive minimum with the charge one,
and \(X^0\) the minimum with that charge zero. At \(X^1\), the
geometric differential (3) and the real stationary equation give
\[
 d\mathcal E=\sum_j h_j\,dL_j,\qquad
           L_j=\sum_{e\ni j}g_{j,e}-\frac{n_j}{2}s_j.
 \]
Indeed the coefficient of \(ds_j\) is
\(\sum_e k_{j,e}=-n_jh_j/2\).
All constraint values agree at the two points except
\(L_v(X^0)-L_v(X^1)=\pi\). The supporting-plane inequality
for the convex energy therefore gives
\[
 F(X^0)\ge F(X^1)+\pi h_v,\qquad
                F(X^1)-F(X^0)\le\pi H_v<B.
 \tag{41}
\]
This uses the geometric gradient only at the unit-charge endpoint.
It requires no stationary solution at an intermediate charge.
\(\square\)

**Lemma 11.** Every active vertex of power three has
\[
                              s_v>\frac{\pi}{4}.
 \tag{42}
\]

**Proof.** Write \(t_v=a-iH\), and suppose \(a\le\pi/4\).
The positive-path theorem gives \(0<a<\pi\). For each neighbor
write \(t_w=b-ih\), allowing \(b=h=0\) at a complete endpoint.
The return is
\[
 r_{v,e}=\operatorname{arsinh}
             \bigl(\tan(t_v/2)\cos(t_w/2)\bigr)=k_{v,e}+ig_{v,e}
 \]
on the branch with \(k_{v,e}>0\) and
\(-\pi/2<g_{v,e}<\pi/2\). Formula (39) implies
\[
 \begin{split}
 |\tan(t_v/2)\cos(t_w/2)|^2
 &\le
 \cosh^2(\overline H/2)
 \frac{\cosh\overline H-1/\sqrt2}
      {\cosh\overline H+1/\sqrt2}\\
 &<\frac{33}{56}<\frac58
                  <\sin^2(5\pi/16).
 \end{split}
 \tag{43}
\]
For the middle bound, use
\(\cosh(23/20)<7/4\) and \(1/\sqrt2>7/10\).
For the last bound,
\(\cos(3\pi/8)>1/4\) gives
\(\sin^2(5\pi/16)=(1+\cos(3\pi/8))/2>5/8\).
Since
\[
 |\sinh(k+ig)|^2=\sinh^2k+\sin^2g,
 \]
we obtain \(|g_{v,e}|<5\pi/16\).
There are at most two incidences. Their sum is consequently greater
than \(-5\pi/8\), whereas the unit constraint at power three says
\[
                  \sum_{e\ni v}g_{v,e}
                         =\frac32a-\pi\le-\frac{5\pi}{8}.
 \]
This contradiction proves (42). \(\square\)

The bound on the hyperbolic cosine in (43) follows from positive
rational series bounds. With \(x=23/20\),
\[
 \cosh x\le
 1+\frac{x^2}{2!}+\frac{x^4}{4!}+\frac{x^6}{6!}
             +\frac{60}{59}\frac{x^8}{8!}<\frac74:
 \]
the ratios between successive terms after \(x^8/8!\) are less
than \(1/60\).

**Corollary 12.** For every fixed finite path, every
choice of old integer powers at least three, and all new powers
\(n,p\ge3\), the insertion cost in (32) satisfies
\[
 \boxed{\qquad
 \mathcal C(n,p)<
       \frac{23\pi}{20}
       \left(\frac8{n+5}+\frac8{p+5}\right).
 \qquad}
 \tag{44}
\]
For real target powers, the left side is the closed variational
minimum. For integer target powers, it is the positive geometric
energy already identified in Theorem 2.
In particular, the desired comparison (15) holds whenever
\[
                         \max(n,p)\ge562.
 \tag{45}
\]
The threshold is independent of the old powers and of the number
of vertices.

**Proof.** Lemma 10, applied to the four reference configurations,
gives
\[
 F_{10}-F_{00}<B,\quad F_{01}-F_{00}<B,\quad
                         F_{11}-F_{00}<2B.
 \]
Lemma 11 gives \(m_v,m_w>\pi/4\), hence the weights (35) obey
\[
                    \alpha\le\frac8{n+5},\qquad
                    \beta\le\frac8{p+5}.
 \]
Subtracting \(F_{00}\) from (36) therefore gives
\[
 \mathcal C(n,p)<
       B\{\alpha(1-\beta)+(1-\alpha)\beta+2\alpha\beta\}
                    =B(\alpha+\beta),
 \]
which proves (44).
If \(n\ge562\) and \(p\ge3\), the right side is at most
\[
 B\left(1+\frac8{567}\right)=\frac{2645\pi}{2268}<4G.
 \tag{46}
\]
The last strict inequality follows entirely from rational bounds:
\[
 4\sum_{j=0}^{99}\frac{(-1)^j}{(2j+1)^2}
                 >\frac{2645}{2268}\frac{355}{113},
 \]
the alternating sum is below \(G\), and \(\pi<355/113\).
The case \(p\ge562\) is symmetric. \(\square\)

The estimate also has a form that does not single out one edge.
For a set \(T\) of selected vertices, let \(\lambda^T\) be zero
on \(T\) and one at every other selected vertex.

**Corollary 13.** For every nonempty \(T\),
\[
 F_\Gamma(\mathbf1)-F_\Gamma(\lambda^T)
             <B\sum_{v\in T}\frac8{n_v+5}.
 \tag{47}
\]

**Proof.** Use reference power three at the vertices of \(T\).
Each of the Boolean minima in the final construction of Section 6
has energy at most \(F_\Gamma(\lambda^T)+B|\epsilon|\),
strictly less when \(\epsilon\ne0\): activate its nonzero charges
one at a time and apply Lemma 10.
All endpoints in this argument are the already-proved positive
integer-power configurations. Lemma 11 bounds every conditional
angle below by \(\pi/4\), so each Bernoulli parameter is at most
\(8/(n_v+5)\). The expected value of \(|\epsilon|\) is the sum of
these parameters. Since \(T\ne\varnothing\) and every Bernoulli
parameter is positive, a nonzero Boolean assignment has positive
weight. The energy bound for the explicit feasible assignment from
Section 6 is therefore strict and proves (47). \(\square\)

For a matching \(M\) of selected edges, take \(T=V(M)\).
The action identity (9) turns (47) into
\[
 M_\Gamma(\lambda^T)-M_\Gamma(\mathbf1)
              <\frac{23}{20}\sum_{v\in V(M)}\frac8{n_v+5}.
 \tag{48}
\]
If every edge of \(M\) has at least one endpoint of power at
least \(562\), the right side is at most
\(|M|\,2645/2268\), strictly below \(|M|M_\infty\).
Thus the geometric comparison for this entire matching has a
uniform gap of at least
\[
              |M|\delta,\qquad
              \delta=\frac{4G}{\pi}-\frac{2645}{2268}>0.
 \tag{49}
\]

This is the geometric input in
[the exact radical contraction estimate](research_radical_path_sector_gap.md),
Theorem 2. To obtain an upper bound on the original contracted
quantum term, one must also have its hypothesis (4): a uniform
bound over the whole real boundary period for every remaining
path component. That hypothesis is available for the established
components, but not for every cluster of short powers. Even when
it is available, this argument controls the radical contribution;
the low-sector cycle and its nonzero coefficient remain separate
questions.

Thus the uniform height estimate gives a uniform comparison for
an edge with at least one sufficiently large power, even when its
other endpoint has power three. It does not settle the comparison
for every adjacent pair of powers in \(\{3,\ldots,561\}\), and it
does not by itself prove a coefficient or a lower bound for a
finite quantum period.

The elementary constants in this section are checked with exact
rational arithmetic by
[the scalar checker](../experiments/check_positive_path_energy_height_consequences.py);
its [saved output](../repro/results/research-positive-path-energy-height-consequences.json)
records all eight positive margins. It also verifies
\(\pi<355/113\) from rational alternating bounds in Machin's
arctangent identity. This checker is separate from the
maximum-height certificate proving (39).
