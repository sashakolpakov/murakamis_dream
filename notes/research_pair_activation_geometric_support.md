# A uniform adjacent activation budget from the actual cosine domain

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The neighboring cosines in a positive path lie inside the unit disk,
as well as their height ellipses. Retaining this constraint reduces
the adjacent-pair support problem to two explicit boundary arcs.
The resulting outward certificates establish the required activation
budget independently of the larger, still unverified support tests
in the [earlier reduction](research_positive_path_pair_activation_gap.md).
This is a geometric comparison and an induction estimate for radical
remainders; it is not a proof of the remaining joint low-cycle coefficient.

## 1. The actual neighboring domain

Use the original positive path and charge family of
[the fractional-charge theorem](research_positive_path_fractional_charge_cube.md).
All selected powers are integers at least three, original degrees
are at most two, and a complete outside endpoint is retained.
At an active vertex write \(t=a-iH\). The proved inputs are
\[
 \begin{gathered}
 0<a<\pi,\qquad 0<H<B:=23/20,\qquad
 \sinh H<\sqrt3\sin a,\\
 |\cos(t/2)|<1,\qquad
 0\le\arg\cos(t/2)<\beta_*:=\arctan(1/\sqrt2),\\
 a\le\frac{2\pi\chi}{n}+\kappa\sin a,
 \qquad \kappa=5-2\sqrt6<11/108.
 \end{gathered}
 \tag{1}
\]
The unit-disk inequality is Lemma 1 of
[the real wire-order proof](research_positive_path_real_wire_order.md).
The phase bound is Theorem 5 of
[the phase maximum principle](research_geometric_phase_maximum_principle.md);
the resulting charge-angle bound is equation (8) of
[the horizontal-concavity proof](research_positive_path_horizontal_concavity.md).
These results hold on the full charge cube and do not depend on
an adjacent activation estimate. At a complete neighbor the cosine
is exactly one.

Activate two adjacent vertices of powers three with equal charge
\(\chi\in(0,1]\), holding all other charges fixed in \([0,1]\).
Choose the endpoint of greater height, write its data as \((a,H)\),
and put \(A=\tan((a-iH)/2)\). Its partner has height at most
\(H\); its other neighbor has height at most \(B\). The actual
returns therefore obey
\[
 r_1+r_2=\frac32H+i\left(\frac32a-\pi\chi\right),\qquad
 r_j=\operatorname{asinh}(Ac_j),\qquad
 c_1\in\Omega_B,\quad c_2\in\Omega_H,
 \tag{2}
\]
where, for \(0<C\le B\),
\[
 \Omega_C=\left\{c:\ |c|\le1,\quad
       0\le\arg c\le\beta_*,\quad
       \frac{(\Re c)^2}{\cosh^2(C/2)}+
       \frac{(\Im c)^2}{\sinh^2(C/2)}\le1\right\}\cup\{0\}.
 \tag{3}
\]
If an incidence is absent, take its cosine to be zero, hence its
return to be zero. No edge is added or duplicated. The ellipse
follows directly by writing the cosine of half a neighboring angle;
the other two restrictions are the independent geometric inputs (1).

All returns use the original right-half-plane branch of asinh.
Indeed \(\Re A>0\), \(\Im A<0\), and every nonzero point of
\(\Omega_C\) has positive real and nonnegative imaginary parts,
so \(\Re(Ac)>0\). The branch extends continuously to \(c=0\).

## 2. The two arcs suffice for every nonpositive support slope

For \(s\le0\), put \(L_s(r)=\Re r-s\Im r\).
Write \(U=\cosh(C/2)\), \(V=\sinh(C/2)\). The outer radial
boundary of (3) consists of the following two arcs, with \(0\le p\le1\):
\[
 \begin{split}
 c_{\rm circ}(C,p)&=e^{i p\arcsin(V^2)},\\
 \theta(C,p)&=\arcsin V+
       p\left\{\arctan\frac{U}{\sqrt2 V}-\arcsin V\right\},\\
 c_{\rm ell}(C,p)&=U\cos\theta(C,p)+iV\sin\theta(C,p).
 \end{split}
 \tag{4}
\]
Here \(V^2<3/8<1/\sqrt3=\sin\beta_*\), using the already
proved \(\cosh B<7/4\). Thus the circle/ellipse intersection
precedes the phase-wedge boundary. At that intersection the
ellipse parameter is \(\arcsin V\), and the cosine phase is
\(\arcsin(V^2)\), which proves (4).

**Lemma 1.** For every \(A\) with \(\Re A>0,\Im A<0\),
\[
 \max_{c\in\Omega_C}L_s(\operatorname{asinh}(Ac))
 =\max\left\{0,
    \max_{0\le p\le1}L_s(\operatorname{asinh}(Ac_{\rm circ}(C,p))),
    \max_{0\le p\le1}L_s(\operatorname{asinh}(Ac_{\rm ell}(C,p)))
                                                        \right\}.
 \tag{5}
\]

*Proof.* Fix a radial direction and write \(z=Ae^{i\beta}\),
\(\varphi=\arg z\in(-\pi/2,\pi/2)\). The derivative along
that ray is
\[
 \frac d{d\rho}L_s(\operatorname{asinh}(\rho z))
   =\Re\frac{(1+is)z}{\sqrt{1+\rho^2z^2}}.
 \tag{6}
\]
The square root is the branch with positive real part. If
\(\varphi\ge0\), the argument of \(z/\sqrt{1+\rho^2z^2}\)
lies between zero and \(\varphi\). After adding
\(\arg(1+is)\in(-\pi/2,0]\), its real part is positive.
If \(\varphi<0\), that argument increases from \(\varphi\)
toward zero: its derivative is
\(-\rho\Im(z^2)/|1+\rho^2z^2|^2>0\).
The total argument in (6) lies in \((-\pi,0)\) and increases.
Thus the derivative can change sign only from negative to positive.
There is no radial interior maximum. The maximum on each closed
radial interval is therefore at zero or its outer endpoint.
The outer endpoints are exactly (4). The branch stays in the
open right half-plane away from zero, and the value at zero is
zero, so all radial and arc endpoints are included. \(\square\)

## 3. The certified inequalities on normalized rectangles

The following two height bounds are sufficient for the energy budget:
\[
 H<\frac{59}{50}\chi\quad(0<\chi\le1),\qquad
 H<\frac{37}{200}+\frac{37}{40}\chi\quad(4/5\le\chi\le1).
 \tag{7}
\]
The [small-height theorem](research_pair_activation_small_height.md),
Theorem 2, already proves the first when \(H\le3/100\).
For the remainder, assume a bound in (7) fails and put \(z=a/H\).
The actual geometry lies in one of two exact rational rectangles:
\[
 \begin{array}{c|c|c|c}
  \text{mode}&z&H&\chi\le\chi_*(H)\\ \hline
  \mathrm{scaled}&[1,2]&[3/100,23/20]&50H/59\\
  \mathrm{affine}&[1,17/8]&[37/40,23/20]&
            \min\{1,(40/37)(H-37/200)\}.
 \end{array}
 \tag{8}
\]
For the lower endpoint \(z>1\), note that the unit-disk bound
implies \(\cosh H+\cos a<2\), whereas
\(\cosh H+\cos a\ge2+(H^2-a^2)/2\).
For the upper endpoints use (1) and \(\sin a\le a\).
In scaled mode this gives
\(z<3600\pi/5723<2\).
In affine mode \(\chi_*(H)/H\le100/111\), so
\(z<2400\pi/3589<17/8\). Both final comparisons follow from
\(\pi<22/7\). The kink of the affine charge bound is the
rational height \(111/100\), and every verification box lies
on one side of it.

A parameter box may first be excluded by one of the following
necessary geometric inequalities, with \(a=zH\):
\[
 \begin{split}
 &\cosh H+\cos a<2,\qquad \sinh H<\sqrt3\sin a,\\
 &a-\frac{11}{108}\sin a\le\frac{2\pi}{3}\chi_*(H),\\
 &\frac32a+\arctan\left(d\tanh\frac32H\right)
       \le\pi\chi_*(H),
 \quad d=\frac{\sinh H-b\sin a}{\sin a+b\sinh H},\quad b=1/\sqrt2,
 \quad\text{when }\sinh H\ge b\sin a.
 \end{split}
 \tag{9}
\]
The last inequality is the negative-return estimate (11) of
[the horizontal-concavity proof](research_positive_path_horizontal_concavity.md).
It uses both original period equations and concavity of
\(\arctan(d\tanh k)\); it is not an additional assumption.

**Certified support lemma.** Every point in either rectangle (8)
either violates (9), or lies in a rational box on which there are
fixed rational numbers \(s\le0\) and \(o\) such that, with
\[
 T(z,H)=\frac32H-s\left(\frac32zH-\pi\chi_*(H)\right),
 \tag{10}
\]
one has throughout the box
\[
 \begin{split}
 &0<T/2+o,\qquad 0<T/2-o,\\
 &L_s(\operatorname{asinh}(Ac_k(B,p)))<T/2+o,\\
 &L_s(\operatorname{asinh}(Ac_k(H,p)))<T/2-o
       \quad(k=\mathrm{circ},\mathrm{ell},\ 0\le p\le1).
 \end{split}
 \tag{11}
\]

Here are the complete verification rules. The
[generator](../experiments/certify_pair_activation_geometric_support.py)
subdivides (8) into rational rectangles. Floating-point minimization
only proposes the rational slope and offset; it never accepts a
box. Exclusions (9), positivity of the two budgets, and the four
arc inequalities (11) are all checked by outward Arb arithmetic
at 128 bits. Failure to verify a box causes its bisection. A result
is saved only when the queue is empty.

For transparency, the mean-value enclosure used for (11) is explicit.
Write \(F=L_s(r)-T/2\mp o\). For the box center \((z_0,H_0)\)
and radii \(q_z,q_H\), an upper enclosure is
\[
 F(z_0,H_0,p)+q_z\sup|F_z|+q_H\sup|F_H|.
 \tag{12}
\]
The two derivatives are bounded on the entire box and the entire
current arc interval in \(p\). With \(r=\operatorname{asinh}(Ac)\),
\[
 \begin{split}
 A_z&=\tfrac H2(1+A^2),& A_H&=\tfrac{z-i}{2}(1+A^2),\\
 r_z&=A_zc/\sqrt{1+A^2c^2},&
 r_H&=(A_Hc+A c_H)/\sqrt{1+A^2c^2},\\
 T_z&=-3sH/2,& T_H&=3/2-s(3z/2-\pi\chi_*'(H)).
 \end{split}
 \tag{13}
\]
For the fixed outer-neighbor cap, \(c_H=0\). For the partner cap
it is the exact derivative of (4). In circle coordinates this uses
\((\arcsin V^2)'=UV/\sqrt{1-V^4}\); in ellipse coordinates
it uses
\[
 (\arcsin V)'=\frac{U}{2\sqrt{1-V^2}},\qquad
 \left(\arctan\frac{U}{\sqrt2V}\right)'
     =-\frac{1/\sqrt2}{2(V^2+U^2/2)}.
 \tag{14}
\]
All values and roots remain on the right-half-plane branch established
in §1. The generator uses the holomorphic asinh directly.
The independent replay instead evaluates its real and imaginary
parts from
\[
 \Re\operatorname{asinh}(x+iy)=
 \operatorname{arcosh}\frac{|x+i(y+1)|+|x+i(y-1)|}{2},\qquad
 \Im\operatorname{asinh}(x+iy)=
 \arcsin\frac{|x+i(y+1)|-|x+i(y-1)|}{2}.
 \tag{15}
\]
It intersects these real arguments with their known ranges
\([1,\infty)\), \([-1,1]\) before applying the monotone functions.
The derivatives in (13) use the same uniquely determined analytic
square root, not numerical differentiation.

The [scaled certificate](../repro/results/research-pair-activation-geometric-support-scaled.json)
and [affine certificate](../repro/results/research-pair-activation-geometric-support-affine.json)
record every rational parameter rectangle, its exclusion or its
slope and offset, and its outward strict margin. The
[independent replayer](../experiments/replay_pair_activation_geometric_support.py)
imports no generator or optimizer. It checks the outer rectangles
by an exact rational sweep with multiplicity one, and verifies
all stored inequalities at 160 bits. If its different interval
formulas are wider, it bisects the same box using the stored
slope and offset; no new optimization, missing point, or new
support assumption is allowed. Arc and parameter bisections must
finish before a replay result is saved.

**Theorem 2.** Both height bounds (7) hold for the actual adjacent
pair, uniformly in the length, the old powers, and all other charges.

*Proof.* A failure belongs to (8). Its actual point satisfies (9),
so the certified support lemma applies. By Lemma 1 and (11),
\(L_s(r_1)+L_s(r_2)<T\). Since \(s\le0\) and
\(\chi\le\chi_*(H)\), applying \(L_s\) to the actual equation
(2) gives a quantity at least \(T\), a contradiction.
The existing small-height theorem supplies the remaining range of
the scaled bound. \(\square\)

## 4. The adjacent energy budget and its exact scope

Let \(F_\Gamma\) denote the original convex energy minimum, and
let \(\lambda^e\) make the two endpoints of a selected edge
complete while retaining every other charge. For endpoint powers
\(n,p\ge3\), the feasible contraction argument in
[the energy comparison](research_edge_cut_energy_comparison.md),
Corollary 7, reduces the activation cost to new powers three;
all old powers remain fixed. Along simultaneous activation,
\(\partial_{\chi_v}F=\pi H_v\). Theorem 2 therefore gives
\[
 \begin{split}
 \frac{F_\Gamma(\mathbf1)-F_\Gamma(\lambda^e)}{\pi}
 &<2\int_0^{4/5}\frac{59}{50}\chi\,d\chi
   +2\int_{4/5}^1\left(\frac{37}{200}+\frac{37}{40}\chi\right)d\chi\\
 &=\frac{5811}{5000}<M_\infty-\frac1{1000},
       \qquad M_\infty=\frac{4G}{\pi}.
 \end{split}
 \tag{16}
\]
The strict final inequality follows from the eight-term alternating
lower sum for \(G\) and \(\pi<22/7\), with exact margin
\(712208857/637702065000>1/1000\), as in equation (16) of
[the earlier reduction](research_positive_path_pair_activation_gap.md).
No outcome of its older support tests (9) and (11) is used.

Consequently a nonempty matching of \(q\) selected edges has
geometric removal margin greater than \(q/1000\). The action
identity and successive activation are exactly those of
[the radical-sector comparison](research_radical_path_sector_gap.md).
If the remaining smaller original source components have their
whole-boundary geometric upper bounds, the exact radical matching
contraction gives a quantum remainder below the full geometric
rate by this margin. The strict observation gains of
[the radical and midpoint theorem](research_radical_observation_boundary_decay.md)
may be added when its separated boundary hypotheses hold, but
are unnecessary for (16).

This establishes the general geometric inequality needed for that
induction step. It does not prove a nonzero coefficient or a
whole-boundary upper bound for an arbitrary new joint low-sector
source. Those remain the separate quantum inputs.

## 5. Reproduction and scope of the records

The saved 128-bit author certificates contain 1,673 scaled boxes
and 1,327 affine boxes. The independent 160-bit replays verified
their exact covers, with areas \(28/25\) and \(81/320\),
respectively. They visited 552,239 and 946,633 boundary intervals;
the alternative interval formulas required 78 and 173 additional
binary parameter refinements, always with the stored slope and
offset. Both queues finished and both replay records passed:
[scaled replay](../repro/results/research-pair-activation-geometric-support-scaled-replay.json)
and [affine replay](../repro/results/research-pair-activation-geometric-support-affine-replay.json).

From the repository root, regenerate and independently replay with
Python, NumPy, SciPy, and python-flint installed:

~~~sh
python3 experiments/certify_pair_activation_geometric_support.py --mode scaled --precision 128 --maximum-segments 512
python3 experiments/certify_pair_activation_geometric_support.py --mode affine --precision 128 --maximum-segments 4096
python3 experiments/replay_pair_activation_geometric_support.py repro/results/research-pair-activation-geometric-support-scaled.json --precision 160
python3 experiments/replay_pair_activation_geometric_support.py repro/results/research-pair-activation-geometric-support-affine.json --precision 160
~~~

The arc budgets change only when an unresolved box is subdivided,
not any acceptance inequality. The replay uses
only python-flint and the standard library. Its exact sweep checks
the parameter cover before any support calculation. Failed support
or exhausted subdivisions cannot produce a successful result.
The [provenance snapshot](../repro/results/research-pair-activation-geometric-support-provenance.json)
records the final written proof, both programs, four completed
records, and the geometric inputs. Adding that snapshot does not
claim another numerical run.

These computations verify the scalar geometric inequalities (11),
not a finite-level quantum asymptotic or a source coefficient.
Their use of every actual neighbor is justified by (1)--(6);
their implication for energy is the separate written argument
(7)--(16). The source dependence remaining in §4 is unchanged.
