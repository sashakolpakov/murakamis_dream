# Partial cone charges on positive paths

Research note, 3 November 2026.

For a finite original path with every crossing power at least
eight, the stationary equations have a unique solution in one
fixed complex box for every vector of cone charges between zero
and one. The proof is a contraction of the exact return map.
It does not require a variational existence theorem at each
intermediate charge.

The imaginary part of each angle is bounded by its own charge
times an explicit constant of order \(d_v/n_v^2\). Integrating
these bounds gives a change-of-action estimate supported only
on the vertices whose charges change. The constants do not
depend on path length or on the charges at other vertices.

These are statements about the original analytic phase and
its marked period equations. No finite quantum invariant
at a nonintegral cone charge is assumed, and no coefficient
of the original quantum integration cycle is inferred.

## 1. Exact equations and their common domain

Let \(I\) be the selected vertices of a finite original path.
At least one endpoint meets a complete outside vertex.
All original degrees, including complete outside incidences,
satisfy \(1\le d_v\le2\). Fix integers \(n_v\ge8\).
Outside angles are zero.

For an oriented incidence \((v,e)\), with \(e=\{v,w\}\), put
\[
 r_{v,e}(t)=\operatorname{arsinh}
       \bigl(\tan(t_v/2)\cos(t_w/2)\bigr).
 \tag{1}
\]
The branches are those continued from zero. The phase is
\[
 \Phi_\lambda(t)=\sum_{e=\{v,w\}}\psi(t_v,t_w)
       +\sum_{v\in I}\frac{i n_vt_v^2}{4\pi}
       -i\sum_{v\in I}\lambda_vt_v.
 \tag{2}
\]
Every original edge incident to \(I\) is included once.
Extra complete edges, if retained, add a constant only.
Since \(\psi_{t_v}=-r_{v,e}/\pi\), the exact stationary
equations are
\[
 n_vt_v+2i\sum_{e\ni v}r_{v,e}(t)=2\pi\lambda_v.
 \tag{3}
\]
These use the original powers and full logarithmic charges.

Use the box
\[
 \mathcal B=\{z:|\Re z|\le1,\ |\Im z|\le1/3\}.
 \tag{4}
\]
Section 7 of
[the edge-response note](research_edge_hessian_and_phase_response.md)
proves the elementary estimates
\[
 |\tan(z/2)|<3/5,\qquad |\Im\tan(z/2)|<1/4,
 \qquad \Re[-2\pi\psi''(z,u)]\succeq\tfrac15 I
 \tag{5}
\]
for \(z,u\in\mathcal B\). These are analytic edge estimates,
not an assumed quantum asymptotic on this larger box.

Write the normalized edge Hessian as
\[
 K(z,u)=\frac1s
 \begin{pmatrix}1+w^2&-wv\\-wv&1+v^2\end{pmatrix},
 \quad w=\tan(z/2),\quad v=\tan(u/2),\quad
 s=\sqrt{1+w^2+v^2}.
 \tag{6}
\]
On the box, \(\Re(s^2)>7/8\). Hence
\(|s|,\Re s>9/10\), and the square root is on the
complete sheet throughout.

## 2. The exact return map is a contraction

**Theorem 1.** For every real charge vector
\(\lambda\in[-1,1]^I\), equations (3) have exactly one
solution \(t(\lambda)\) in \(\mathcal B^I\). The solution
is in its interior and extends holomorphically to a
neighborhood of this charge cube of width independent
of the path and its powers.

For \(\lambda\in[0,1]^I\), each coordinate has
\[
 \lambda_v=0\ \Longrightarrow\ t_v=0,\qquad
 \lambda_v>0\ \Longrightarrow\
                    \Re t_v>0,\quad \Im t_v<0.
 \tag{7}
\]
The edge configurations are positive. At \(\lambda=\mathbf1\)
this is the selected marked geometric solution already
established for the original filling.

**Proof.** Rewrite (3) as the fixed-point equation
\[
 \mathcal T_v(t)=\frac{2\pi\lambda_v}{n_v}
                  -\frac{2i}{n_v}\sum_{e\ni v}r_{v,e}(t).
 \tag{8}
\]
First we verify that \(\mathcal T\) preserves the box.
For \(z,u\in\mathcal B\), elementary trigonometric bounds give
\[
 |\cos(u/2)|<41/40,\qquad
 |\Im\cos(u/2)|<
       (12/25)(17/100)=51/625.
 \tag{9}
\]
Here \(\sin(1/2)<12/25\), \(\sinh(1/6)<17/100\)
and \(\cosh(1/6)<41/40\); their Taylor bounds were
recorded in the edge-response note.
If \(Z=\tan(z/2)\cos(u/2)\), then
\[
 |Z|<123/200,\qquad
 |\Im Z|<
       \frac35\frac{51}{625}+\frac14\frac{41}{40}
       <\frac13.
 \tag{10}
\]
In particular \(|Z|<1\), so the branch of
\(\operatorname{arsinh}Z\) is regular on the entire box.
For \(r=\operatorname{arsinh}Z=A+iB\), its principal
branch has \(|B|<\pi/2\), and
\[
 |\Re r|\le\operatorname{arsinh}|Z|<123/200,\qquad
 |\Im r|<\arcsin(1/3)<7/20.
 \tag{11}
\]
Indeed \(|Z|^2=\sinh^2 A+\sin^2 B\) and
\(\Im Z=\cosh A\sin B\). The last numerical inequality
follows from
\(\sin(7/20)>7/20-(7/20)^3/6>1/3\).

Since \(d_v/n_v\le1/4\), equations (8)--(11) imply
\[
 |\Re\mathcal T_v|<
                 \pi/4+7/40<1,\qquad
 |\Im\mathcal T_v|<123/400<1/3.
 \tag{12}
\]
These are strict bounds independent of the number of
vertices.

For contraction, differentiate the returns:
\[
 \partial_{t_v}r_{v,e}=\tfrac12K_{vv},\qquad
 \partial_{t_w}r_{v,e}=\tfrac12K_{vw}.
 \tag{13}
\]
From (5)--(6),
\[
 |K_{vv}|+|K_{vw}|
 <\frac{1+9/25+9/25}{9/10}=\frac{86}{45}.
 \tag{14}
\]
The maximum row sum of the complex Jacobian of
\(\mathcal T\) is therefore at most
\[
                    \frac{d_v}{n_v}\frac{86}{45}
                         \le\frac{43}{90}<\frac12.
 \tag{15}
\]
Complete outside variables are fixed and add no Jacobian
columns. Integrating the derivative on a straight segment
in the convex box proves this Lipschitz bound for the
complex supremum norm. The closed finite product box is
complete, so Banach's theorem gives a unique fixed point.

The estimates also give holomorphic dependence uniformly
in path length. For example, allow each \(\lambda_v\)
to have distance less than \(1/100\) from \([-1,1]\).
The two right sides of (12) then increase by at most
\(\pi/400\), and still lie strictly inside the box.
The derivative bound (15) is unchanged. Iteration from
zero consists of holomorphic functions of the charges,
and converges uniformly on compact subsets. Its limit
is therefore holomorphic on this neighborhood.

For the signs, define the removable quotient
\[
 Q_v(t)=\sum_{e\ni v}\frac{r_{v,e}(t)}{t_v}
       =\frac12\sum_{e\ni v}
                    \int_0^1K_{vv}(\sigma t_v,t_w)\,d\sigma .
 \tag{16}
\]
The last equality is the complex fundamental theorem
of calculus, since \(r_{v,e}(0,t_w)=0\).
The segment stays in the same box. We will use the
slightly stronger centered estimate
\[
                    |K_{vv}-1|<2/5.
 \tag{17}
\]
To verify it, the exact expression (6) gives
\[
 K_{vv}-1=\frac{s w^2-v^2}{s(s+1)}.
\]
Using \(|w|,|v|<3/5\), \(|s|>9/10\) and
\(|s+1|\ge1+\Re s>19/10\) gives
\[
 |K_{vv}-1|
 <\frac{9}{25}\frac{1+10/9}{19/10}=\frac25.
\]
Consequently
\[
                  |Q_v-d_v/2|<d_v/5.
 \tag{18}
\]
In particular \(\Re Q_v>3d_v/10>0\) and
\(|\Im Q_v|<d_v/5\).
The stationary equation factors exactly as
\[
                    t_v=\frac{2\pi\lambda_v}{n_v+2iQ_v}.
 \tag{19}
\]
The denominator has positive real and positive imaginary
parts. Formula (7) follows, including the exact zero
coordinate when \(\lambda_v=0\).

The edge Hessians have positive real part by (5).
The original positive-edge theorem identifies this with
positivity of the eight original tetrahedra on the
continued branch. At unit charges, Proposition 5 of the
edge-response note places the already selected geometric
solution inside the same box. Uniqueness of the fixed
point identifies the two solutions, retaining their
original full logarithmic periods. \(\square\)

The theorem also provides a path to a partial-charge
solution by scaling its charges from zero. This path is
defined by (3), not by silently rescaling the powers.
Coordinates of zero charge stay exactly zero along it.

## 3. Componentwise heights and action loss

For positive charges write \(t_v=\theta_v-iH_v\).
For \(n\ge8\) and \(d\in\{1,2\}\), define
\[
 L_{n,d}=
 \frac{6\pi d/5}{(n+2d/5)^2+(3d/5)^2},
 \qquad
 U_{n,d}=
 \frac{14\pi d/5}{(n-2d/5)^2+(7d/5)^2}.
 \tag{20}
\]

**Theorem 2.** Throughout \([0,1]^I\),
\[
       L_{n_v,d_v}\lambda_v\le H_v(\lambda)
                              \le U_{n_v,d_v}\lambda_v.
 \tag{21}
\]
For \(\lambda_v>0\), both estimates may be made strict.
In particular
\[
 U_{n,d}\le\frac{35\pi}{373}<\frac3{10},
 \qquad
 U_{n,d}\le\frac{280\pi}{81}\frac{d}{n^2}.
 \tag{22}
\]

Let \(S(\lambda)=\Phi_\lambda(t(\lambda))\) and
\(M(\lambda)=\Re S(\lambda)\). If \(0\le\lambda\le\mu\le1\)
coordinatewise, then
\[
 \boxed{\displaystyle
 \frac12\sum_v L_{n_v,d_v}(\mu_v^2-\lambda_v^2)
 \ \le M(\lambda)-M(\mu)\le\
 \frac12\sum_v U_{n_v,d_v}(\mu_v^2-\lambda_v^2).}
 \tag{23}
\]
Only changed charges contribute. For arbitrary
\(\lambda,\mu\in[0,1]^I\), one has
\[
 |M(\lambda)-M(\mu)|
 \le\frac12\sum_v U_{n_v,d_v}|\mu_v^2-\lambda_v^2|.
 \tag{24}
\]

**Proof.** Write \(Q_v=A+iB\). Equation (19) gives
\[
 H_v=\frac{4\pi\lambda_v A}{(n_v-2B)^2+4A^2},
 \qquad
 3d_v/10<A<7d_v/10,\quad |B|<d_v/5.
 \tag{25}
\]
On this rectangle, the displayed expression increases
with both \(A\) and \(B\): for the first monotonicity
one uses \(2A<n_v-2B\), which follows from
\(n_v>9d_v/5\). Its opposite corners give precisely
(20)--(21).

The maximum of \(U_{n,d}\) for \(n\ge8\), \(d=1,2\)
is \(U_{8,2}=35\pi/373<3/10\).
Also \(n-2d/5\ge9n/10\), which proves the second
bound in (22) after dropping the other positive
denominator term.

Differentiating the stationary action introduces no
derivative of \(t(\lambda)\), because its full gradient
vanishes. Thus
\[
                \partial_{\lambda_v}S=-it_v,\qquad
                \partial_{\lambda_v}M=-H_v .
 \tag{26}
\]
Integrate (21) along the straight segment from \(\lambda\)
to \(\mu\). At each coordinate,
\(\int_0^1[\lambda_v+s(\mu_v-\lambda_v)]
(\mu_v-\lambda_v)\,ds=(\mu_v^2-\lambda_v^2)/2\).
This proves (23). Varying coordinates one at a time and
using the triangle inequality gives (24). \(\square\)

For example, turning a set \(A\) of unit charges down to
zero increases the real stationary action by an amount
between \(\frac12\sum_{v\in A}L_{n_v,d_v}\) and
\(\frac12\sum_{v\in A}U_{n_v,d_v}\), whatever the charges
at the other vertices. The latter is at most
\(35\pi|A|/746<3|A|/20\).
At the all-zero vector every angle is zero, so the action
there is the sum of the complete edge phases. No change
of peripheral basis or of the original powers occurs.

## 4. Signed powers and filling every auxiliary vertex

The contraction does not use a complete outside endpoint, nor
the positivity of the powers. These restrictions in the initial
statement can be removed without changing its constants.

**Corollary 3.** Let \(Y\) be an original ordered circle-tree
exterior whose underlying graph is a nontrivial finite path.
Select any nonempty set \(I\) of its auxiliary vertices,
possibly every vertex. At each selected vertex choose its
original power
\[
 n_v=\eta_v-2p_v,\qquad p_v\in\mathbb Z,\qquad |n_v|\ge8,
 \tag{27}
\]
with its fixed carrier \(\eta_v\). Unselected angles are zero.
There is a unique solution in \(\mathcal B^I\) for every
\(\lambda\in[-1,1]^I\), with the same uniform holomorphic
extension as in Theorem 1. For nonnegative charges,
\[
 \lambda_v=0\Longrightarrow t_v=0,\qquad
 \lambda_v>0\Longrightarrow
       \operatorname{sgn}(\Re t_v)=\operatorname{sgn}(n_v),
       \quad\Im t_v<0.
 \tag{28}
\]
The height and action bounds (20)--(24) hold with \(n_v\)
replaced by \(|n_v|\).

At unit charges, these positive original cells determine the
smooth Dehn filling along the original slopes
\(\mu_v+p_v\lambda_v^{\rm disk}\). Here
\(\lambda_v^{\rm disk}\) denotes the original disk longitude,
to distinguish it from the cone charge. Every main cusp and
every unselected auxiliary cusp remains complete. If all
constant edge terms of \(Y\) are included in (2), its absolute
volume is \(2\pi M(\mathbf1)\). The original component test
still determines whether the main link is a knot.

**Proof.** The box estimates (12) and the contraction estimate
(15) use only \(d_v/|n_v|\). They do not use the existence of
a boundary vertex. Hence they apply verbatim to this graph.
In (19), the denominator still has positive imaginary part,
while its real part \(n_v-2\Im Q_v\) has the sign of \(n_v\).
This proves (28). Its real-part magnitude lies between
\(|n_v|-2d_v/5\) and \(|n_v|+2d_v/5\), so the same maximization
and minimization in (25) prove the unchanged bounds.

The continuation from zero charges stays on the same box
chart, and every original edge remains positive by (5).
At unit charges, (3) is exactly
\[
             \sum_{e\ni v}r_{v,e}
                   =\frac{i n_v}{2}t_v-\pi i.
\]
Together with \(\Im t_v<0\), these are precisely the
hypotheses of Theorem 1 in
[the marked completion theorem](research_positive_point_marked_completion.md).
That theorem allows any selected set, including all
auxiliary vertices; it does not require a complete outside
end. It supplies the original primitive filling and its
absolute action-volume identity, with every carrier and
marked disk retained. This proves the geometric assertions
directly, without using the earlier positive-path existence
theorem. \(\square\)

For later estimates one also has, for \(\lambda_v\ge0\),
\[
 |t_v|\le\frac{2\pi\lambda_v}{|n_v|-2d_v/5}.
 \tag{29}
\]
When \(|n_v|\ge64\), the loss from increasing a unit charge
at that vertex is bounded by
\[
 \frac12U_{|n_v|,d_v}
 <\frac{35\pi d_v}{99856}<\frac{d_v}{800}.
 \tag{30}
\]
Indeed \(|n_v|-2d_v/5\ge64-4/5=316/5\), and dropping
the other denominator term in (20) gives the first bound.
The second follows, for example, from \(\pi<22/7\).
In this range (29)--(30) also give
\[
                      |\Re t_v|<\frac1{10},\qquad
                         0<H_v<\frac1{200}
 \tag{31}
\]
at unit charges. These bounds remain independent of path
length and of all other powers.

## 5. What the charge estimate does not distinguish

The edge phase is even separately in each angle on this
complete chart. Flipping \(\lambda_v\) and \(t_v\)
simultaneously therefore preserves (3), leaves every
other angle unchanged, and preserves the stationary
action. Uniqueness in Theorem 1 proves that these are
the corresponding selected solutions. Consequently
\(S(\lambda)\) is even in each charge separately.

Thus (23) compares charge magnitudes and zeroed charges;
it does not supply a strict gap between the different
choices of signs of unit charges. Those contributions
still require the original finite trace, with its
orientations and coefficients.

Likewise, the bounds above do not estimate a high
Newton-index tail or a mixed boundary current of the
finite quantum source. They supply the marked phase
and an explicit action budget for such a comparison.
An upper bound for another contour piece must still
be proved from its own exact finite-source expression.
