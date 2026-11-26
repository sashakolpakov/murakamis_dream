# Positive path solutions throughout the fractional-charge cube

Research note, 3 November 2026.

Fix a finite path and its original integer crossing powers, all at
least three. The unit-charge positive solution extends uniquely when
each filling charge is allowed to vary independently between zero
and one. A zero charge makes that vertex complete and separates the
positive-charge components. No lower bound on a nonzero charge is
required in the statement.

The proof has two inputs already established in the repository.
The [integer corridor theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_negative_corridor_variational_bounds.md),
Theorem 15 and its mirror, supplies the unit-charge solutions.
The [fractional-charge height bound](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_positive_path_height_bound.md#5-the-same-bound-during-a-positive-fractional-charge-deformation)
bounds every positive solution which already exists. That bound alone
does not give existence. Here we prove the missing closedness argument:
no angle endpoint, zero height, open square side, or square corner can
be reached while all charges stay positive.

The integer-power hypothesis is retained. The proof does not
interpolate the crossing powers through nonintegers, and it does
not assert a quantum asymptotic.

## 1. The path, equations and conclusion

Let the selected vertices form a nonempty finite path, with original
degrees at most two. At least one end is attached to a complete
outside vertex. Retain every original edge, including its prescribed
carrier and primitive marking. At a selected vertex fix an integer
\(n_v\ge3\), and let its charge be \(\lambda_v\in[0,1]\).
At an outside vertex set \(t=0\).

The sought angles and their original edge returns are
\[
 t_v=a_v-iH_v,\qquad
 r_{v,e}=k_{v,e}+ig_{v,e}
       =\operatorname{arsinh}\!
          \left(\tan(t_v/2)\cos(t_w/2)\right)
       \quad(e=\{v,w\}).
 \tag{1}
\]
The branch is the original positive branch, with
\(-\pi/2<\Im r<\pi/2\) in its interior. The full logarithmic
equations, rather than just their exponentials, are
\[
 \sum_{e\ni v}r_{v,e}=\frac{in_v}{2}t_v-\pi i\lambda_v.
 \tag{2}
\]
Their real and imaginary parts are
\[
 \sum_{e\ni v}k_{v,e}=\frac{n_vH_v}{2},\qquad
 \sum_{e\ni v}g_{v,e}-\frac{n_v a_v}{2}=-\pi\lambda_v.
 \tag{3}
\]

For clarity, positivity can be stated in either of the equivalent
coordinate systems proved in
[the positive-edge theorem](research_positive_edge_global_monotonicity.md)
and [the convex variation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_positive_filling_convex_variation.md).
In tangent coordinates \(z_v=\tan(t_v/2)\), it is
\[
 \Re\sqrt{1+z_v^2+z_w^2}>
           \sqrt{(\Re z_v)^2+(\Re z_w)^2}.
 \tag{4}
\]
In real angle coordinates, the two squares on an oriented edge
have coordinates
\[
 \begin{split}
 A_P=a_v/4-g_{w,e}/2,&\qquad
 A_Q=a_v/4+g_{w,e}/2,\\
 y_P=g_{v,e}/2+a_w/4,&\qquad
 y_Q=g_{v,e}/2-a_w/4.
 \end{split}
 \tag{5}
\]
They lie in the open square \((-\pi/4,\pi/4)^2\).
The equivalent edge inequalities are
\[
 |a_v|+2|g_{w,e}|<\pi,\qquad
 |a_w|+2|g_{v,e}|<\pi.
 \tag{6}
\]
The square energy \(E\), with \(E(0,0)=0\), has derivatives
\[
 E_A=\frac12\operatorname{arsinh}(\tan(2A)\cos(2y)),
 \qquad
 E_y=\frac12\operatorname{arsinh}(\tan(2y)\cos(2A)).
 \tag{7}
\]
The total energy is
\(\mathcal E=4\sum_e(E_{P,e}+E_{Q,e})\).
Outside incidences are retained as variables; their stationarity
equations impose complete outside angles.

**Theorem 1.** For every charge vector
\(\lambda\in(0,1]^{V}\), equations (1)--(2) have a unique
positive solution in the original variational domain. It satisfies
\[
                  0<a_v<\pi,\qquad 0<H_v<23/20
                    \quad(v\in V).
 \tag{8}
\]
It is the unique closed constrained minimum of \(\mathcal E\).
The minimum and its real angle coordinates depend continuously
on the entire cube \([0,1]^V\), and real analytically wherever
all charges are positive.

At a zero charge the unique solution has \(t_v=0\) and
\(r_{v,e}=0\) at every incidence of that vertex. The remaining
positive-charge components have the solutions just described,
with these zero-charge vertices treated as complete boundaries.
Every original edge remains present.

This theorem concerns the positive logarithmic equations and their
convex minima. At unit charges, or at a Boolean face where every
nonzero charge is one, the existing
[pointwise marked-completion theorem](research_positive_point_marked_completion.md)
applies. No additional topological completion statement for
fractional charges is needed or claimed here.

## 2. Strict feasibility and local continuation

For every Boolean vector \(\epsilon\in\{0,1\}^{V}\), make its
zero-charge vertices complete. Each remaining selected component
is a path with a complete outside end. Solve it by the unit-charge
corridor theorem and its mirror. Joining these solutions retains
every original edge. At a zero-charge vertex,
\(\operatorname{arsinh}(\tan(0)\cos(t_w/2))=0\), so both equations
in (3) hold there. A complete edge has two interior squares.
Thus these finitely many assignments \(X^\epsilon\) are strictly
feasible in the common real angle domain.

Their convex combination with weights
\[
 p_\epsilon(\lambda)=
       \prod_v\lambda_v^{\epsilon_v}(1-\lambda_v)^{1-\epsilon_v}
 \tag{9}
\]
is strictly feasible at the charge \(\lambda\). Indeed the
constraints in (3) are affine in the real coordinates and in
\(\lambda\), and the marginal mean of \(\epsilon_v\) is
\(\lambda_v\). The edge inequalities define a convex domain.
Since the finite list \(X^\epsilon\) lies in its interior, all
these convex combinations stay a fixed positive distance from
every square side. The closed feasible sets are compact and
nonempty, so a constrained minimum exists at every charge.

At an interior critical point this minimum is unique and locally
real analytic in \(\lambda\). One can see the required
nondegeneracy directly from (7). With
\(\Delta=1-\sin^2(2A)\sin^2(2y)>0\), the square Hessian is
\[
 \nabla^2E=
 \frac1{\sqrt\Delta}
 \begin{pmatrix}
 \cos(2y)/\cos(2A)&-\sin(2A)\sin(2y)\\
 -\sin(2A)\sin(2y)&\cos(2A)/\cos(2y)
 \end{pmatrix}.
 \tag{10}
\]
It has determinant one and positive diagonal entries.
The map from vertex/incidence coordinates to all square
coordinates is injective. Therefore the total Hessian is
positive definite on the real variable space, and in particular
on the tangent space of the constraints. Those constraints have
independent rows: the variable \(a_v\) has coefficient
\(-n_v/2\) in its own row and occurs in no other constraint.
The bordered critical-point system is consequently invertible.
The implicit function theorem gives local analytic continuation.

The unit-charge solution has the signs in (8). They persist
locally. To prove existence for an arbitrary positive target
charge it remains to show that this positive solution cannot
reach a boundary along the segment joining the unit vector
to that target.

## 3. Compact limits have bounded returns and square gradients

Consider a convergent sequence of charge vectors whose entries
lie in a fixed interval \([\lambda_0,1]\), \(\lambda_0>0\),
and positive solutions with \(0<a_v<\pi\), \(H_v>0\).
The fractional-charge height theorem gives \(H_v<23/20\).
After passage to a subsequence, all \(a_v,H_v\) converge in
\([0,\pi]\times[0,23/20]\).

For every selected incidence the argument of the inverse
hyperbolic sine in (1) has positive real part. Explicitly, write
\[
 \tan(t_v/2)=
       \frac{\sin a_v-i\sinh H_v}{\cos a_v+\cosh H_v}.
 \tag{11}
\]
Both real summands in the product with
\(\cos(t_w/2)=\cos(a_w/2)\cosh(H_w/2)
                 +i\sin(a_w/2)\sinh(H_w/2)\)
are nonnegative, and the first is strictly positive.
Consequently \(k_{v,e}>0\). Equation (3) gives
\[
             0<k_{v,e}\le n_vH_v/2\le23n_v/40.
 \tag{12}
\]
Also \(|g_{v,e}|<\pi/2\). The returns therefore remain bounded.

The four square gradients on an edge are linear combinations
of its two returns and two imaginary angles, by equations
(3) and (6) of the corridor note. Hence all square gradients
remain bounded as well. A square cannot converge to an open
side: in (7), the derivative normal to that side diverges if
the other coordinate stays in the open interval.

At a square corner, a convergent gradient is a finite
subgradient of the closed convex energy. To check this without
a compactness theorem for minimizers, take the limit in
\[
 E(Y)\ge E(X_j)+\nabla E(X_j)\cdot(Y-X_j)
 \tag{13}
\]
for any fixed point \(Y\) of the closed square.
Thus a corner limit satisfies precisely the finite corner
subgradient conditions already used in the corridor theorem.
The constraints and the linear stationarity equations also
pass to the limit.

## 4. Neither an angle endpoint nor a zero height can occur

The arguments in this section concern a possible limit from
Section 3. The complete outside vertices remain fixed.

First, the pair \((a_v,H_v)=(\pi,0)\) is impossible.
If it occurred, \(|\tan(t_v/2)|\) would tend to infinity.
The bounded return (12) implies that
\(\tan(t_v/2)\cos(t_w/2)=\sinh r_{v,e}\) stays bounded on
each incident edge. Therefore \(\cos(t_w/2)\) tends to zero.
In the closed parameter rectangle this means
\((a_w,H_w)=(\pi,0)\). This conclusion propagates along the
finite selected path to a complete outside vertex, where
\(\cos(0)=1\), a contradiction.

The pair \((a_v,H_v)=(0,0)\) is also impossible.
Here \(\tan(t_v/2)\) tends to zero and every neighboring
cosine is bounded. All its returns tend to zero. Equation
(3) would then give \(\lambda_v=0\), contrary to
\(\lambda_v\ge\lambda_0\).

Suppose next that \(a_v=0\) and \(H_v>0\). Put
\(B=23/40\). On an incident edge the argument in (1) is
\(z=x-iy\), where
\[
 0\le x\le\frac{H_v}{2}\sinh B,\qquad
 0\le y\le\sinh B.
 \tag{14}
\]
For \(y<1\), integration of the derivative of
\(\operatorname{arsinh}\) along the horizontal segment from
\(-iy\) to \(x-iy\) gives
\[
 0\le\Re\operatorname{arsinh}(x-iy)
                         \le\frac{x}{\sqrt{1-y^2}}.
 \tag{15}
\]
Indeed
\(\Re(1+(s-iy)^2)=1+s^2-y^2\ge1-y^2\), so the
derivative's modulus is at most \(1/\sqrt{1-y^2}\).
The rational Taylor estimate
\(\cosh(23/20)<7/4\), written in
[the energy comparison](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_edge_cut_energy_comparison.md), §7,
gives \(\sinh^2B<3/8\). Since the degree is at most two,
(14)--(15) imply
\[
 \sum_{e\ni v}k_{v,e}
     \le H_v\frac{\sinh B}{\sqrt{1-\sinh^2B}}
     <H_v\sqrt{3/5}<\frac32H_v.
 \tag{16}
\]
This contradicts (3), because \(n_v\ge3\).

Now suppose \(H_v=0\) with \(0<a_v<\pi\). Every incidence
has \(k_{v,e}=0\), by (3) and nonnegativity of the limiting
real returns. If a neighbor had \(a_w<\pi\), the argument
\(\tan(a_v/2)\cos(t_w/2)\) would have positive real part,
so \(k_{v,e}>0\). Thus every neighbor would have \(a_w=\pi\).
The case \((\pi,0)\) has already been excluded, so \(H_w>0\).
Then \(\cos(t_w/2)=i\sinh(H_w/2)\), and the selected return
has strictly positive imaginary part. But the closed edge
inequality \(a_w+2|g_{v,e}|\le\pi\) forces \(g_{v,e}=0\).
This is a contradiction.

It remains to exclude \(a_v=\pi,\ H_v>0\). If a selected
neighbor had \(0<a_w<\pi\), then
\(\cos(t_v/2)=i\sinh(H_v/2)\) and
\(\Re\tan(t_w/2)>0\). The argument defining \(r_{w,e}\)
would have positive imaginary part, hence \(g_{w,e}>0\).
The closed edge inequality at \(v\) instead forces
\(g_{w,e}=0\). Every selected neighbor must therefore also
have angle \(\pi\); angle zero has already been excluded.
On an edge to such a selected neighbor,
\(\tan(t_v/2)\cos(t_w/2)\) is positive real, so \(g_{v,e}=0\).
On an edge to a complete outside vertex its limiting argument is
\(-i\coth(H_v/2)\), whose right-half-plane inverse-sine limit
has imaginary part \(-\pi/2\). Thus every incidence at \(v\)
has \(g_{v,e}\le0\). On the other hand, (3) requires
\[
 \sum_{e\ni v}g_{v,e}
       =n_v\pi/2-\pi\lambda_v\ge\pi/2>0,
 \tag{17}
\]
again a contradiction.

All selected limit angles consequently satisfy
\(0<a_v<\pi\) and \(H_v>0\). Their return arguments have
positive real part, so the original branches remain regular.

## 5. Every unit-charge corner test remains necessary

Only square corners could still prevent an interior limit.
We give the charge comparison explicitly, since feasibility
alone would not exclude them.

Mirror the positive-power configuration to the negative-power
convention of the corridor note. This sends \(t\) to
\(-\overline t\) and \(r\) to \(-\overline r\), leaving the
imaginary returns \(g\) and positive angle magnitudes unchanged.
Orient a corner from its negative-incidence endpoint \(v\)
to its positive-incidence endpoint \(w\), and put
\(\theta=a_v,\ \phi=a_w\), \(m=n_v,\ p=n_w\).
The corner incidences are
\[
 g_{v,e}=-(\pi-\phi)/2,\qquad
 g_{w,e}=+(\pi-\theta)/2.
 \tag{18}
\]
If the endpoint has another incidence, its value is
\[
 \begin{split}
 g_{v,\mathrm{other}}
   &=\frac{m\theta-\pi-\phi}{2}+\pi(1-\lambda_v),\\
 g_{w,\mathrm{other}}
   &=\frac{p\phi-3\pi+\theta}{2}+\pi(1-\lambda_w).
 \end{split}
 \tag{19}
\]
At a terminal the corresponding expression is zero.
Thus each other incidence is at least its value in the
unit-charge formula with the same corner angles. The real
stationarity equations, and all the directed-incidence
inequalities involving the heights, are unchanged.

Here is the complete list of necessary reductions used in the
unit proof. Equation references in the first column refer to
the [corridor note](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_negative_corridor_variational_bounds.md).

| Step of the unit proof | Conditions still necessary at the fractional-charge limit | Reason |
| --- | --- | --- |
| Proposition 3 and Corollary 4 | The two patterns (19) of that note; \(0<\theta,\phi<\pi\); the negative endpoint has \(\theta>\pi/2\). | These use the square corner subgradient, strict negative mirrored heights and the unchanged companion square. |
| Theorem 6, equations (48)--(55) | A negative endpoint of magnitude \(m\ge4\) is impossible. | Its other incidence is at least \((m\theta-\pi-\phi)/2>0\). The old upper bound \(m\theta\le\pi+\phi+2g_{v,\mathrm{other}}\), followed by the unchanged outgoing estimate, gives the same contradiction \(m\theta<4\theta\). |
| Proposition 8, equations (70)--(73) | For the remaining negative magnitude three, \(\phi>\pi/2\), and the positive magnitude is \(p\le6\). | When \(\phi\le\pi/2\), (19) gives the same lower bound \(g_{v,\mathrm{other}}\ge3(\theta-\pi/2)/2\). At the positive endpoint \(p\phi\le3\pi-\theta+2g_{w,\mathrm{other}}<4\pi-\theta\). Terminal bounds only become stronger. |
| Proposition 9, equations (74)--(78) | \(\theta>2\pi/3\), and the negative endpoint has a strictly positive other incidence. | The real-period estimate \(6X>C_6\) does not contain a charge. Formula (19) gives the same positive lower bound afterward; a terminal or complete outside incidence is excluded as before. |
| Theorem 13, equations (87)--(96) | Put \(x=\pi-\theta,\ y=\pi-\phi\). Then \(0<x<\pi/3\), \(0<y<4x/3\), \(p y>(p-3)\pi-x\), and \(pX-H_c\ge C_p\). Only \(p=4,5\) remain. | The negative outgoing bound is still \(R<\tan((3x-y)/2)\), because the actual other incidence is larger. The positive angle bound is weaker than the fractional equation, and the real-period condition is identical. The same algebra excludes \(p=3,6\). |

For the last step define, exactly as in the corner certificate,
\[
 \begin{split}
 X&=\tfrac12\operatorname{arsinh}(\cot x\sin y),&
 H_c&=\tfrac12\operatorname{arsinh}(\cot y\sin x),\\
 R&=\frac{\sqrt{1-\cos^2x\cos^2y}}{\cos x(1+\cos y)},&
 \Lambda&=x+py-(p-3)\pi,\\
 C_p&=\tfrac12\{p\operatorname{arsinh}(1/p)
                                  +\operatorname{arsinh}p\}.
 \end{split}
 \tag{20}
\]
The letter \(H_c\) here is the companion-square quantity, not
a vertex height. The surviving conditions are exactly
\[
 \begin{gathered}
 y<4x/3,\qquad \Lambda>0,\qquad pX-H_c\ge C_p,\\
 R<\tan((3x-y)/2),\\
 \Lambda<\pi\ \Longrightarrow\
                2H_c/p<\sin y\,\tan(\Lambda/2).
 \end{gathered}
 \tag{21}
\]
Only the last implication needs a further charge check.
Equation (19) at the positive endpoint reads
\[
 g_{w,\mathrm{other}}
       =(\pi-\Lambda)/2+\pi(1-\lambda_w).
 \tag{22}
\]
If \(\Lambda<\pi\), this incidence is positive. The other
neighbor's angle is at most
\(\pi-2g_{w,\mathrm{other}}
   =\Lambda-2\pi(1-\lambda_w)\le\Lambda\).
The unchanged outgoing and real-period inequalities therefore
imply the last line of (21). If the endpoint is terminal,
equation (22) instead gives
\(\Lambda=\pi+2\pi(1-\lambda_w)\ge\pi\); that conditional
test is correctly not invoked.

The angle bounds place \((x/\pi,y/\pi)\) in the same two closed
rectangles:
\[
 \begin{array}{c|cc}
 p&x/\pi&y/\pi\\ \hline
 4&[3/19,1/3]&[1/6,4/9]\\
 5&[6/23,1/3]&[1/3,4/9].
 \end{array}
 \tag{23}
\]
The existing
[rational corner verifier](../experiments/verify_negative_three_corner_exclusion.py)
and its [saved certificate](../repro/results/research-negative-three-corner-exclusion.json)
exclude (21) on all of these rectangles. Its 94 terminal
rectangles for \(p=4\) and 10 for \(p=5\) are unchanged:
the fractional equations have only strengthened the necessary
conditions. Therefore the limiting configuration has no corner.

## 6. Completing the continuation and adding zero charges

Fix a target vector with every charge positive, and join it to the
unit vector by a straight segment. Let \(\mathcal U\) be the set
of segment parameters admitting a positive solution with the
strict signs in (8). It contains the unit endpoint. Section 2
makes it relatively open.

Take any convergent sequence of parameters in \(\mathcal U\).
All their charges have a common positive lower bound. Section 3
gives a compact limiting assignment with bounded square
subgradients. Section 4 excludes every angle endpoint and zero
height. There are no open square sides, and Section 5 excludes
all corners. Thus the limit is interior and has the required
strict signs. Its stationarity equations pass to the limit, so it
is a positive solution at the limiting parameter. The height
theorem applies again and gives the strict bound \(H_v<23/20\).
Hence \(\mathcal U\) is also relatively closed. Connectedness
of the segment proves existence at its target.

The interior stationary solution is the global constrained
minimum by convexity. It is unique: any distinct closed feasible
point can be joined to it by a segment whose interior is in the
open angle domain, where the energy is strictly convex. The
stationary first variation is zero along that segment, so the
other point cannot have the same minimum energy. This also
proves uniqueness of the continued branch.

Now allow zero charges. Make every zero-charge vertex complete
and solve each remaining positive-charge component by the result
just proved. Each component has at least one complete boundary
vertex. Join them with the original edges. At a zero-charge
vertex all its returns are zero, so (2), the matching conditions,
and the stationarity equations are exact. Every square is
interior, including squares on complete edges. The same convex
argument identifies this assignment as the unique closed minimum.

Finally, continuity at the cube faces follows directly from the
variational problem. For a sequence \(\lambda_j\to\lambda\),
take a convergent subsequence of its minimizing real coordinates.
Its limit is feasible at \(\lambda\). If \(Z\) is any feasible
point there and \(Y\) is the strictly feasible point from (9),
then \(Z_\epsilon=(1-\epsilon)Z+\epsilon Y\) is interior.
The coordinate correction
\[
 \delta a_v=\frac{2\pi}{n_v}
                       (\lambda_{j,v}-\lambda_v),
 \qquad \delta g_{v,e}=0
 \tag{24}
\]
makes its constraints exactly those at \(\lambda_j\).
For fixed \(\epsilon>0\) this correction stays in the open
angle domain for all sufficiently large \(j\).
The minimum at \(\lambda_j\) has no larger energy than this
competitor. Pass first to the limit in \(j\), then let
\(\epsilon\downarrow0\). The limiting point minimizes at
\(\lambda\), and hence equals its unique minimum. Every
subsequence has that limit, proving continuity on the full cube.
The interior analytic dependence was established in Section 2.
This completes the proof of Theorem 1.

The result supplies a genuine family of positive stationary
solutions for varying charges, with the original powers fixed.
It does not prove that a corresponding quantum saddle has a
nonzero coefficient. That remains an analytic question about the
original finite source.

## 7. Differentiating the energy along the actual charge family

Let \(F(\lambda)\) be the minimum in Theorem 1. The new existence
statement justifies integration along actual stationary solutions,
without assuming that intermediate charges remain geometric.
That assumption has now been proved.

**Corollary 2.** The minimum is differentiable on the charge cube,
with one-sided derivatives on its faces, and
\[
                  \frac{\partial F}{\partial\lambda_v}
                                  =\pi H_v(\lambda).
 \tag{25}
\]
For any piecewise continuously differentiable path
\(\lambda(s)\) in the cube,
\[
 F(\lambda(1))-F(\lambda(0))
       =\pi\int_0^1\sum_v H_v(\lambda(s))\lambda'_v(s)\,ds.
 \tag{26}
\]
In particular the simultaneous activation of a fixed pair \(v,w\),
with all other charges fixed at one, has the exact cost
\[
 \frac{F(\mathbf1)-F(\lambda^{v=w=0})}{\pi}
       =\int_0^1\bigl(H_v(\lambda_v=\lambda_w=s)
                         +H_w(\lambda_v=\lambda_w=s)\bigr)\,ds.
 \tag{27}
\]
The unchanged entries of the charge vector are suppressed in
the notation on the right.

*Proof.* All cube minima are interior square assignments.
Continuity on the compact cube and the nondegeneracy in (10)
therefore allow the critical-point equations to be solved in an
open neighborhood of any one of its points, even when some
charges are zero. The real angle coordinates and the energy have
analytic local extensions there; positivity signs need not persist
outside the cube.

Write the \(v\)-th real constraint as
\(C_v=\sum g_{v,e}-n_v a_v/2=-\pi\lambda_v\).
The energy differential at a stationary point is
\(\sum_v h_v\,dC_v\), where \(h_v=-H_v\).
This follows directly from the edge differential: its coefficient
of \(da_v\) is \(\sum k_{v,e}=-n_vh_v/2\), and its
coefficient of each \(dg_{v,e}\) is \(h_v\).
Hence \(dF=-\pi\sum_vh_v\,d\lambda_v\), proving (25).
The chain rule proves (26), and the straight activation path
gives (27). \(\square\)

The height bound also gives monotonicity in each charge and
\[
 |F(\lambda')-F(\lambda)|
                 \le\frac{23\pi}{20}\|\lambda'-\lambda\|_1.
 \tag{28}
\]
The single-activation budget and the resulting large-power
edge comparison were already proved by endpoint supporting planes
in [the energy comparison](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_edge_cut_energy_comparison.md),
§7; they are not new consequences being claimed here. What is
newly available is the exact integral (27) through the entire
stationary family. The remaining uniform \(3,3\) insertion
comparison asks whether that integral is always less than
\(4G/\pi\). The separate upper bound \(23/20\) for each
height does not establish this two-vertex inequality.

## 8. A uniform relation between angle and height

The height bound can be strengthened by retaining the real angle.
This is useful when estimating an old path component attached to
an activated pair: its boundary angle and height cannot range
independently over the full height rectangle.

**Theorem 3.** At every vertex with positive charge in Theorem 1,
\[
       \frac{\sinh H_v}{\sin a_v}<\sqrt3,\qquad
       H_v<\operatorname{arsinh}(\sqrt3\sin a_v).
 \tag{29}
\]
Equivalently, the original tangent coordinate satisfies
\[
                 -\frac{\pi}{3}
                   <\arg\tan(t_v/2)<0.
 \tag{30}
\]
Complete vertices are excluded from the ratio in (29), since
their numerator and denominator both vanish.

*Proof.* For each positive-charge vertex put
\(R_v=\sinh H_v/\sin a_v\), and choose a vertex where \(R_v\)
is largest. Write its angle and height as \(a,H\).
If one of its incidences has \(g_{v,e}>0\), its neighbor must
have positive charge. Formula (11) and the sign of the imaginary
part of the principal inverse hyperbolic sine give
\[
 R_v<\tan(a_w/2)\tanh(H_w/2)
       =R_w\,\frac{1-\cos a_w}{1+\cosh H_w}<R_w.
 \tag{31}
\]
This contradicts the choice of \(v\). A complete neighbor instead
has a strictly negative return imaginary part at \(v\).
Thus every incidence at the maximizing vertex is nonpositive,
and its charge equation yields
\[
                         a\le\frac{2\pi\lambda_v}{n_v}
                                     \le\frac{2\pi}{3}.
 \tag{32}
\]

Suppose \(R_v\ge\sqrt3\). Set \(C=\cosh H\).
The height bound and the rational estimate in Section 4 give
\(1<C<7/4\), and
\[
              \sin^2a\le\frac{\sinh^2H}{3}<\frac{11}{16}.
 \tag{33}
\]
On the interval \([\pi/2,2\pi/3]\), however,
\(\sin^2a\ge3/4\). Hence (32)--(33) imply \(a<\pi/2\).
It follows that
\[
 \cos a\ge\sqrt{\frac{4-C^2}{3}},\qquad
 C+\cos a\ge C+\sqrt{\frac{4-C^2}{3}}\ge2.
 \tag{34}
\]
The last inequality holds for \(1\le C\le2\): after squaring
its nonnegative sides it is equivalent to
\((C-1)(C-2)\le0\). Therefore
\[
 |\tan(t_v/2)|^2
    =\frac{\sin^2a+\sinh^2H}{(C+\cos a)^2}
                        \le\frac{\sinh^2H}{3}.
 \tag{35}
\]
Every neighbor, including a complete one, satisfies
\[
 |\cos(t_w/2)|^2
       =\frac{\cosh H_w+\cos a_w}{2}<\frac{11}{8}.
 \]
Since \(|\sinh(k+ig)|^2=\sinh^2k+\sin^2g\), each real return
at \(v\) is at most
\(\operatorname{arsinh}(\sqrt{11/24}\sinh H)\).
The real period equation and the degree bound would consequently
require
\[
          \frac{3H}{4}
             \le\operatorname{arsinh}
                         \left(\sqrt{\frac{11}{24}}\sinh H\right).
 \tag{36}
\]

This is impossible for \(0<H\le23/20\). Indeed the function
\(\sinh(3H/4)/\sinh H\) is strictly decreasing.
Its logarithmic derivative is
\((3/4)\coth(3H/4)-\coth H<0\), because
\(u\coth u\) is strictly increasing for \(u>0\).
At the upper endpoint,
\[
                24\sinh^2(69/80)>11\sinh^2(23/20).
 \tag{37}
\]
For an entirely rational verification, put \(x=69/80\),
\(y=23/20\). The positive Taylor series give
\[
 \sinh x>x+\frac{x^3}{6},\qquad
 \sinh y\le y+\frac{y^3}{6(1-y^2/20)}<\frac{10}{7}.
 \]
The geometric bound on the latter tail uses the fact that the
successive ratios after \(y^3/6\) are at most \(y^2/20<1\).
Finally,
\[
 24\left(x+\frac{x^3}{6}\right)^2
       -11\left(\frac{10}{7}\right)^2
             =\frac{683309192723}{6422528000000}>0.
 \tag{38}
\]
Thus (37) holds, contradicting (36). The maximizing ratio is
less than \(\sqrt3\), proving (29) at every active vertex.
Formula (11) gives
\(-\Im\tan(t_v/2)/\Re\tan(t_v/2)=R_v\), which proves (30).
\(\square\)

The rational comparisons in (37)--(38) are reproduced by
[the tangent-sector checker](../experiments/check_positive_path_tangent_sector.py);
its [saved results](../repro/results/research-positive-path-tangent-sector.json)
use exact fractions throughout. This theorem constrains the
geometric deformation. It does not assert a bound on an original
quantum sum or settle the simultaneous-pair integral in (27).
