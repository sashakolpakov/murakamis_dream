# One geometric chamber for every homogeneous three-crossing chain

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The estimates needed for a joint contour argument must hold at the
geometric critical point of every chain under consideration. A list
of numerical solutions for short chains would not establish this.
Here the explicit contraction of the geometric equations reduces
the all-length assertion to a finite, rigorous calculation. The
remaining vertices are controlled by a discrete comparison principle.

The result places all internal wires and their selected algebraic
index coordinates in fixed rectangles. It also places the two actual
end attachments in the already established cap domain. We then verify
the logarithmic critical equations of the original local source at
these points. No complementary-contour estimate or quantum lower
bound is inferred.

## 1. Coordinates and the uniform assertion

Take a path of \(m\ge3\) selected vertices, with crossing power three
at each vertex and a complete outside vertex at each end. Its
positive geometric angles are denoted by
\[
 t_v=a_v-iH_v,\qquad 1\le v\le m,\qquad t_0=t_{m+1}=0.
 \tag{1}
\]
They solve the full logarithmic equations in
[the geometric contraction theorem](research_homogeneous_three_geometric_contraction.md).
For the edge between vertices \(v\) and \(v+1\), define its original
Fourier coordinate by
\[
 x_v=\frac1{2\pi}\arccos
       \frac{1-\cos t_v\cos t_{v+1}}{2+\cos t_v+\cos t_{v+1}},
          \qquad 1\le v<m.
 \tag{2}
\]
The selected branch has positive imaginary part and real part in
\((0,1/4)\), as proved by
[the original wire-order theorem](research_positive_path_real_wire_order.md).
At the homogeneous angle \(t_*\),
\[
 \cos t_*=-\frac14+\frac{3\sqrt3}{4}i,\qquad
          x_*=\frac16+\frac{i\log2}{2\pi}.
 \tag{3}
\]

For an internal retained vertex, its two adjacent wire coordinates
are \(x=x_{v-1}\) and \(y=x_v\). The selected index branch is
\[
 \begin{split}
 X=e^{2\pi ix},\quad Y=e^{2\pi iy},\quad
 \alpha=X^{-1}-1,\quad\beta=Y^{-1}-1,\\
 \Delta=1-2(\alpha+\beta)+(\alpha-\beta)^2,\\
 U=(1+\alpha-\beta-\sqrt\Delta)/2,\qquad
 V=(1-\alpha+\beta-\sqrt\Delta)/2,\\
 s=\frac{i\Log U}{2\pi},\qquad
 t=\frac{i\Log V}{2\pi}.
 \end{split}
 \tag{4}
\]
In (4), the symbol \(t\) is the second index coordinate; the
geometric angles continue to carry subscripts as in (1). The
square root and logarithms are the branches in the
[central-index theorem](research_three_vertex_central_index_chart.md).

**Theorem 1.** For every \(m\ge3\), all the internal wires satisfy
\[
       \frac7{50}<\Re x_v<\frac15,\qquad
       \frac9{100}<\Im x_v<\frac3{25}.
 \tag{5}
\]
At each internal retained vertex \(2\le v\le m-1\), the branch
(4) satisfies
\[
       \frac14<\Re s,\Re t<\frac9{20},\qquad
                     |\Im s|,|\Im t|<\frac1{50}.
 \tag{6}
\]
The two end angles satisfy
\[
       \frac{38}{25}<a_1,a_m<\frac{\pi}{2},\qquad
                     \frac{97}{100}<H_1,H_m<1.
 \tag{7}
\]
Finally the first and last internal wires lie strictly in the
directed cap domain:
\[
 \begin{split}
 x_v&=x_*+r+i(-4r/5+z),\\
 0<r&<\frac{13}{1000},\qquad
          -\frac3{2000}<z<\frac1{1000},
                      \qquad v=1,\ m-1.
 \end{split}
 \tag{8}
\]
Thus the actual end attachments belong to the uniform source
domain of
[the complete-cap theorem](research_homogeneous_wire_complete_cap.md),
not merely to its unspecified local neighborhood.
The calculation also verifies \(|\cos(t_1/2)|,|\cos(t_m/2)|<1\);
the full local edge amplitude at the ends is therefore covered by
that theorem's original packet conditions.

The actual end angle is the cap theorem's selected critical branch.
To check this directly, write \(v=\tan(t_1/2)\),
\(w=\tan(t_2/2)\), and \(q=\cot(\pi x_1)\). Equation (2), or
the equivalent sine-square wire formula, gives
\[
                         q^2=1+v^2+w^2.
\]
On the positive edge branch one has
\[
 \operatorname{atanh}(v/q)
       =\operatorname{asinh}(v\cos(t_2/2)).
\]
Both sides continue from the same real branch; positivity keeps
the logarithms of \(q+v\) and \(q-v\) in their original
right half-plane. Substitution into the end vertex equation gives
exactly the cap critical equation. Bound (7) places its root
in the cap theorem's common rectangle, where that root is unique.
The same argument applies at the right end.

## 2. Comparing arbitrary lengths with one fixed reference path

Use the norm
\[
       |z|_\square=\max(|\Re z|,|\Im z|).
 \tag{9}
\]
The geometric contraction theorem places every selected angle in
\[
 \Omega=\{a-iH:1.3\le a\le1.82,\ .82\le H\le1.21\}.
 \tag{10}
\]
The one-vertex map \(T\), with neighbors fixed, satisfies
\[
 |T(u,w)-T(u',w')|_\square
       \le\frac5{16}\bigl(
          |u-u'|_\square+|w-w'|_\square\bigr).
 \tag{11}
\]
It also proves
\[
 |t_v-t_*|_\square
       \le q^{\,\min(v,m+1-v)-1},\qquad
       q=\frac{8-\sqrt{39}}5<\frac9{25}.
 \tag{12}
\]

**Lemma 2.** If \(m\ge M\), the solutions for lengths \(m\) and
\(M\), compared from their left ends, satisfy
\[
       |t_j^{(m)}-t_j^{(M)}|_\square
             \le\frac{13}{25}q^{M-j},
                       \qquad 1\le j\le M.
 \tag{13}
\]

*Proof.* Both left outside angles are zero. At \(j=M\), the
difference of two points of (10) is at most its diameter in
(9), which is \(13/25\). At every \(1\le j<M\), both solutions
satisfy the same vertex equation with the same neighbor types.
Equation (11) gives
\[
       e_j\le\frac5{16}(e_{j-1}+e_{j+1}),\qquad e_0=0.
 \tag{14}
\]
The comparison sequence \((13/25)q^{M-j}\) satisfies equality
in (14), because \(q+q^{-1}=16/5\), and dominates both endpoint
errors. A positive maximum of the difference of the two sequences
would occur in the interior and be at most \(5/8\) of itself.
This is impossible. \(\square\)

The geometric solution is invariant under reversal of the path,
by uniqueness. Thus the same comparison holds from the right end.
No comparison between distinct knot invariants is involved.

## 3. Certifying the finite reference solutions

The calculation uses reference lengths \(3\le m\le24\). Numerical
root solving supplies only rational centers \(c^{(m)}_v\).
It does not supply an existence assertion or an error estimate.

For each center, keep its two neighboring centers fixed, using zero
at an outside endpoint. The original one-vertex equation is
\[
 G(t;u,w)=3t+2i\left\{
   \operatorname{asinh}(\tan(t/2)\cos(u/2))
  +\operatorname{asinh}(\tan(t/2)\cos(w/2))\right\}-2\pi .
 \tag{15}
\]
The checker proves, with \(R=10^{-25}\),
\[
 |G_t(c;u,w)|R>
 |G(c;u,w)|+\frac{R^2}{2}
             \sup_{|t-c|\le R}|G_{tt}(t;u,w)|.
 \tag{16}
\]
It verifies that the disk lies strictly in \(\Omega\). Every term
in (16) is enclosed by outward arithmetic, with the actual
holomorphic branches. Rouché's theorem gives exactly one zero
in the disk.

This zero is the root used by \(T\). Indeed the existing derivative
certificate gives \(\Re G_t>0\) throughout the convex rectangle
\(\Omega\) for these neighbors. Integrating \(G_t\) on a line
segment shows that \(G\) is injective there. Thus the local root
cannot be a different branch from the one defining \(T\).

Consequently the center vector has simultaneous-update residual
at most \(R\) in the maximum real-coordinate norm. The proved
\(5/8\) contraction bounds its distance to the whole geometric
solution by
\[
       \max_v|t_v^{(m)}-c_v^{(m)}|_\square
                       \le\varepsilon:=\frac{8}{3\cdot10^{25}}.
 \tag{17}
\]
This controls the coupled system; separate small scalar residuals
would not suffice without that contraction argument.

Applying (2) and (4) to these enclosing rectangles verifies
(5)--(8) for each of the reference lengths. The branch checks
include that the argument of \(\arccos\) in (2) is in the lower
half-plane, that \(\Im\Delta>0\), and that \(U,V\) are both in
the lower-left quadrant. They identify the selected branches
throughout each enclosure.

## 4. Why the finite calculation covers every longer chain

Fix \(M=24\). For \(m\ge24\), the first ten angles are enclosed
by the following rectangles around the certified reference centers:
\[
       |t_j^{(m)}-c_j^{(24)}|_\square
          \le\varepsilon+
             \frac{13}{25}\left(\frac9{25}\right)^{24-j},
                            \qquad 1\le j\le10.
 \tag{18}
\]
This follows from Lemma 2 and (17). Interval evaluation of (2)
on consecutive rectangles in (18) verifies (5) for the first
nine wires. Evaluation of (4) verifies (6) for the retained
vertices \(2,\ldots,9\). The same rectangles verify the end-angle
bound (7) and the first attachment bound (8). Reversal gives
the corresponding statements at the other end.

Every angle at distance at least nine from both complete ends
satisfies the common bound
\[
       |t_v-t_*|_\square
                     \le\left(\frac9{25}\right)^8.
 \tag{19}
\]
Interval evaluation of (2) on two independent copies of this box
verifies (5). Evaluation of (4) on two copies of the resulting
wire box verifies (6). The two copies are treated independently;
equality of adjacent angles or wires is not assumed.

Every wire is now covered: it either lies among the first or last
eight wires, or both its endpoint angles have distance at least
nine from the ends. Every retained vertex is covered as well:
it either has distance at most nine from an end, or its two
adjacent wires depend only on angles covered by (19). The extra
near-end wires included in (18) cause no difficulty. This proves
Theorem 1 for all \(m\ge24\); Section 3 supplies the remaining
lengths. \(\square\)

## 5. The original logarithmic critical equations

Let \(\Phi(x,y)\) be the critical value of the exact retained
index phase, including its cardinal factors:
\[
       \Phi(x,y)=F(s_c,t_c;X,Y)-\pi i(x+y).
 \tag{20}
\]
This is a holomorphic local phase at each pair covered by (5)--(6).
The present definition uses the exact local interpolated summands;
it does not assume a full-vertex asymptotic on the entire rectangle
(5). Let \(S_{\rm cap}(x)\) be the actual complete-cap phase on
its proved domain (8).

**Proposition 3.** The geometric wires of Theorem 1 are a stationary
point of
\[
 \mathcal S_m(x_1,\ldots,x_{m-1})
 =S_{\rm cap}(x_1)+
   \sum_{v=2}^{m-1}\Phi(x_{v-1},x_v)
                 +S_{\rm cap}(x_{m-1}).
 \tag{21}
\]
All equalities are for the stated logarithmic branches, not just
for their exponentials.

*Proof.* At an internal vertex put \(z=e^{it_v}\), and let \(X,Y\)
be the exponentials of its adjacent wires. The relation between a
wire and its two angles proved after Theorem 1 identifies each
geometric return with its \(\operatorname{atanh}\) expression.
Exponentiating the original vertex period therefore gives
\[
 z^3=\frac{(X+z)(Y+z)}{(1+Xz)(1+Yz)}.
 \tag{22}
\]
The identity follows directly from
\((q+\tan(t_v/2))/(q-\tan(t_v/2))=(X+z)/(1+Xz)\).
Since \(H_v>0\), one has \(|z|>1\), so \(z\ne1\).
Factoring the numerator of (22) by \((z-1)z^2\), and writing
\(W=z+z^{-1}=2\cos t_v\), gives
\[
       XYW^2+(XY+X+Y)W+1+X+Y-XY=0.
 \tag{23}
\]
Consequently
\[
 U_{\rm geom}=\frac{1-X}{1+X+XW},\qquad
 V_{\rm geom}=\frac{1-Y}{1+Y+YW}
 \tag{24}
\]
satisfy the exact index equations
\(\alpha=U_{\rm geom}(1-V_{\rm geom})\) and
\(\beta=V_{\rm geom}(1-U_{\rm geom})\).

The finite and all-length enclosing rectangles of Sections 3--4
also verify that both expressions in (24) lie in the lower-left
quadrant. There is exactly one such branch of the index equations:
the other branch is \((1-V,1-U)\), in the upper-right quadrant.
Thus (24) equals the selected branch (4). This identifies the
geometric vertex with the actual retained critical branch.

Write
\[
 b_x(x,t_v)=
  \log\cos(\pi x+t_v/2)+\log\cos(\pi x-t_v/2)
                           -2\log\sin(\pi x).
 \tag{25}
\]
Direct substitution of (24) into the retained derivative gives
\[
 \begin{split}
 \Phi_x&=-\Log U+\log(1-XU)-\log(1-X)-\pi i,\\
 e^{\Phi_x}
   &=\frac{XU-1}{U(1-X)}
     =\frac{\cos(2\pi x)+\cos t_v}{1-\cos(2\pi x)}
     =e^{b_x(x,t_v)}.
 \end{split}
 \tag{26}
\]
The enclosure checks retain the logarithmic lifts: each cosine
and sine in (25) has positive real part, and both
\(\Im b_x\) and \(\Im\Phi_x\) lie strictly between \(-\pi\)
and \(\pi\). Their difference is an integer multiple of \(2\pi i\)
by (26), so it is zero. The same argument applies to \(\Phi_y\).
At either end the established cap theorem gives
\(S_{\rm cap}'(x)=b_x(x,t_{\rm end})\), with the same lifts.

Finally put \(C=\cos(2\pi x_v)\). The wire equation (2) is
equivalent to
\[
             (C+\cos t_v)(C+\cos t_{v+1})=(1-C)^2.
 \tag{27}
\]
Thus the exponentials of the two incident derivatives in (26)
have product one. The two imaginary parts each belong to
\((-\pi,\pi)\), including those at the caps; hence their sum
belongs to \((-2\pi,2\pi)\) and must be zero. This is precisely
the derivative of (21) at each wire. The index equations themselves
already have their original logarithmic lifts by the central-index
theorem. \(\square\)

**Corollary 4.** Keep the two end angles and every retained index
uneliminated, and put
\[
 \begin{split}
 \mathcal G_m={}&
 \mathcal F_3(x_1,\tau_L)+
 \sum_{v=2}^{m-1}
    \{F(s_v,t_v;x_{v-1},x_v)-\pi i(x_{v-1}+x_v)\}\\
 &+\mathcal F_3(x_{m-1},\tau_R),
 \end{split}
 \tag{28}
\]
where \(\mathcal F_3\) is the actual complete-cap angular phase.
Fix the imaginary parts at the geometric critical point \(z_c\)
specified above. On the real product of the wire, index, and
cap-angle intervals
\[
 [7/50,1/5]^{m-1}\times
     ([1/4,9/20]^2)^{m-2}\times[0,9/5]^2
 \tag{29}
\]
one has
\[
       \Re\mathcal G_m(z)\le
       \Re\mathcal G_m(z_c)-\frac1{40\pi}|z-z_c|^2.
 \tag{30}
\]
The constant does not depend on \(m\).

*Proof.* Theorem 1 puts the actual critical point in the interior
of (29), with the required imaginary heights. Proposition 3
and the original index and cap equations make every first
derivative vanish there. The
[joint Hessian theorem](research_three_vertex_joint_concavity.md)
gives \(-\Re F''\succ(\pi/50)I\) on each retained block and
the cap bound
\((\pi/5)\,dx^2+(1/(20\pi))\,d\tau^2\).
Every wire belongs to at least one retained block, and every
index remains distinct. Summing the forms gives
\(-\Re\mathcal G_m''\succeq(1/(20\pi))I\).
Integrate twice along the segment from \(z_c\) to \(z\);
the product (29) is convex. This proves (30). \(\square\)

In particular, the geometric critical point is nondegenerate for
every fixed chain length, and the principal horizontal density
has no competing maximum in this whole central region. The exact
local interpolants have nonzero symbols at this point: their
factorial arguments are regular, their denominator products are
nonzero, and the two cap angles satisfy the full local edge-packet
conditions established above. A sufficiently small restricted
Gaussian integral through the point therefore has a nonzero
leading coefficient.

This is a statement about the central contribution in a contour
decomposition. It does not bound the remaining index sides,
nonconstant cotangent terms, angular currents, or complementary
wire periods. No lower bound for the full quantum sum, or absolute
phase-volume normalization, follows from this statement alone.

## 6. Reproduction and the remaining source problem

Run

    python3 experiments/check_three_chain_geometric_chamber.py

The [record](../repro/results/research-three-chain-geometric-chamber.json)
contains the exact rational centers, Rouché comparisons, full
reference wire and index boxes, and the common boxes used in
(18)--(19). It also checks the five rational identities behind
(22)--(27), the geometric index branch, and every logarithmic
lift bound used above. Its finite checks are the premises of the all-length
comparison proof, not evidence extrapolated from short paths.

The conclusion is a geometric domain statement. In particular,
it does not say that the original integration cycle can be moved
through this whole domain, or that the contribution near the
critical point dominates its complement. Those are analytic
requirements on the original finite source. The present theorem
supplies uniform locations at which such an argument can be made.
