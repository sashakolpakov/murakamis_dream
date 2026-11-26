# Simultaneous clamping of the high boundaries of an old region

Independent geometric and variational derivation, 1 November 2026.

This report checks the argument in
/private/tmp/md-trivalent-bare-component-simultaneous-clamp.md against the
original tetrahedron barrier and the exact product response equations.
The conclusion is restricted to a trivalent tree whose internal edges
are physical quarter-turns. It does not apply unchanged to binary
resolutions of higher-valence multiplication junctions.

## 1. The constrained problem

Put
\[
 J(u)=\int_0^u\log(2\sin\pi t)\,dt,\qquad
 g(u)=J(2u)-4J(u),\quad 0\le u\le\tfrac12,
\]
and define the old covariant cubic action by
\[
 t(x,y,z)=J(x+y)+J(x+z)+J(y+z)-J(x)-J(y)-J(z)
                         -J(x+y+z-1).
 \tag{1}
\]
Its closed support is
\[
 x,y,z\ge0,\qquad x+y,x+z,y+z\le1,\qquad x+y+z\ge1.
 \tag{2}
\]
Replacing the outgoing covariant coordinate by \(z=1-b\) gives the
original product action \(m(x,y,b)\). Consequently (1) is concave and
continuous on (2), and has a negative definite Hessian in the strict
domain. This is the three-tetrahedron decomposition used in
notes/actual_positive_conway_hyperbolic_volume.md, Section 2.

Consider a finite tree of these vertices. At each unmarked external
incidence put the action \(g(a)\), with \(0\le a\le1/2\). A marked
external incidence has a fixed label \(z_i\) and contributes no action.
Assume that at most one marked incidence meets any vertex. Internal
edges identify equal covariant labels. Additive boundary constants may
be kept throughout; they do not affect any derivative or gap below.

Let \(\Psi(\mathbf z)\) be the constrained maximum. The joint feasible
set is a compact convex polytope, and the sum of the actions is
concave. Taking convex combinations of maximizing states proves that
\(\Psi\) is concave on its feasible boundary domain.

The assertion to prove is
\[
 \Psi(\mathbf z)\le\Psi(\tfrac12\mathbf1)
 \qquad(z_i\ge\tfrac12\text{ for every }i).
 \tag{3}
\]
The boundary data in (3) must be feasible. It is a joint comparison.
No monotonicity in one coordinate with all
other coordinates fixed above half is asserted.

## 2. Why the all-half optimizer is strict

There is an explicit strict comparison state. Set the marked labels
to half and every other label to \(3/8\). An unmarked vertex has triple
\((3/8,3/8,3/8)\); a marked vertex has triple
\((1/2,3/8,3/8)\). Their totals exceed one and all pair sums are less
than one. The same assignment remains strict for sufficiently small
independent perturbations of the marked labels.

Root the tree at one marked incidence. Every vertex becomes an
ordinary binary product, with outgoing ordinary coordinate equal to
one minus its outgoing covariant coordinate. Every internal edge is
the physical turn. Other marked terminals are fixed at half and have
no tetrahedron attached to them. All remaining terminals have the
original leaf action \(g\).

The boundary-barrier proof survives this change of terminal data.
Along the segment toward the strict comparison state, an ideal atom
with angles \((0,a,1-a)\), \(0<a<1\), has derivative \(+\infty\).
A vertex-flat atom has a finite derivative: its small-angle logarithmic
terms cancel. Positive atoms also have finite derivatives. Thus no
other atom can cancel the positive infinite contribution.

If a variable product output is zero, both inputs are zero. If it is
one, either the two inputs are interior and sum to one, giving a
nonvertex-flat atom immediately, or an input is an endpoint. A turn
exchanges zero and one. Following endpoint children strictly descends
the finite rooted tree. It cannot end at a fixed half terminal and
cannot end at the root, whose output is half. It therefore reaches an
ordinary leaf at zero, or an interior pair summing to one. Either
alternative has a nonvertex-flat atom. Hence no variable wire is zero
or one at a maximum. An ordinary leaf at half is excluded by its own
nonvertex-flat atom. The fixed half terminals are not excluded and are
not assigned artificial leaf atoms.

With every variable wire interior, a remaining saturated product
inequality again gives a nonvertex-flat atom. In the notation
\(p=b-x,q=b-y,r=x+y-b,w=1-x-y\), the cases are
\[
\begin{array}{c|c}
w=0&(y,x,0)\\
r=0&(b,0,1-b)\\
p=0<q&(0,q,1-q)\\
q=0<p&(p,0,1-p)\\
p=q=0&(0,x,1-x).
\end{array}
 \tag{4}
\]
All relevant nonzero angles lie strictly between zero and one. This
proves strictness of every retained gate and every ordinary leaf.

The sum of the gate Hessians is negative definite on the free-variable
space: each gate Hessian is negative definite in its three labels and
every free variable occurs in a gate. The leaf Hessians can only
strengthen that conclusion. Thus the constrained maximum is unique.
The implicit-function theorem supplies its analytic continuation for
marked labels near half. Compactness and uniqueness show that this
continued critical point remains the constrained maximum.

This proof uses no geometric completion of a fixed terminal. The
strictness is a consequence of the original action and its linear
constraints.

## 3. The supporting gradient at half

For a boundary response with ordinary coordinate \(b\), use
\[
 B=\cot\pi b,\qquad
 X^2=\frac{1+B^2}{1+\kappa},\qquad Y^2=\kappa X^2,
 \qquad \kappa=e^{-f'(b)}.
 \tag{5}
\]
At a fixed half terminal there is no profile derivative. Instead
define the response from its incident strict prism: in an input
coordinate \(\kappa=e^{m_x}>0\). This is precisely the response needed
to match the prism there. Its cotangent is zero, so it satisfies
\(-Y<B<X\) for every positive response. An ordinary leaf satisfies
\(B=X>0,Y=1\).

At a product, differentiation of the original action and stationarity
at its variable input wires give a common \(X>0\), and
\[
 B=\frac{B_1B_2+X^2-1}{B_1+B_2},\qquad
 Y=\frac{Y_1Y_2}{B_1+B_2},\qquad B_1+B_2>0.
 \tag{6}
\]
A turn sends \((B,X,Y)\) to \((-B,Y,X)\). The induction must be
phrased precisely: ordinary leaf inputs have the leaf condition;
fixed half inputs have the proper condition; every strict product
output has the proper condition; internal turns act on these proper
product outputs. One does not claim that turning an ordinary leaf
preserves its leaf condition.

Here is the product verification. The inputs satisfy
\(-Y_i<B_i\le X\) and \(Y_i^2=1+B_i^2-X^2\). If \(X\ge1\), then
\(B_i>0\) and \(B_i\ge\sqrt{X^2-1}\), with strict inequality for a
proper input. Moreover
\[
 B-X=\frac{(X-B_1)(X-B_2)-1}{B_1+B_2}<0.
 \tag{7}
\]
For a leaf input one factor in the numerator product is zero. For
proper inputs each factor is smaller than
\(X-\sqrt{X^2-1}\le1\). Also \(B>0\), so the lower proper inequality
is immediate. If \(X<1\), set \(h=\sqrt{1-X^2}\) and write
\(B_i=h\cot\alpha_i,Y_i=h\csc\alpha_i\), where
\(0<\alpha_i<\pi\). Then
\(\alpha_i\ge\arccos X\) and the positive denominator in (6) gives
\(\alpha_1+\alpha_2<\pi\). Formula (6) becomes
\[
 B=h\cot(\alpha_1+\alpha_2),\qquad
 Y=h\csc(\alpha_1+\alpha_2),
\]
which gives \(-Y<B<X\). Turns preserve these two strict inequalities.

Now choose marked incidence \(i\) as the root. Its ordinary output
is \(b=1-z_i=1/2\). Strict support makes both root inputs less than
half, so \(B_1,B_2>0\). Equations (5)–(6) give
\[
 Y^2=1-X^2=B_1B_2\le X^2.
\]
The envelope theorem therefore yields
\[
 \partial_{z_i}\Psi(\tfrac12\mathbf1)
       =-\log(X^2/Y^2)\le0.
 \tag{8}
\]
This argument can root the same constrained state at every marked
incidence, so it proves every component of the required gradient.

The supporting-plane inequality for the concave pressure proves (3).
There is no endpoint regularity assumption hidden here. For a feasible
boundary point \(\mathbf z\), concavity on the segment from
\(\mathbf z_0=\tfrac12\mathbf1\) gives
\[
 \Psi(\mathbf z)-\Psi(\mathbf z_0)
 \le \frac{\Psi(\mathbf z_0+t(\mathbf z-\mathbf z_0))
                    -\Psi(\mathbf z_0)}t.
\]
Letting \(t\downarrow0\) bounds the left side by the gradient at
\(\mathbf z_0\), paired with the nonnegative vector
\(\mathbf z-\mathbf z_0\). This proves the inequality even at a
degenerate endpoint of the feasible boundary domain.

## 4. All returns can be replaced with the same old action budget

The exact six-type table in
notes/actual_main_meridian_turn_comparison.md, Section 3, makes a
moving equal-color vertex adjacent only to a constant opposite-color
vertex across a physical quarter-turn. Thus return vertices are
nonadjacent in the trivalent tree. The old support allows at most one
high incidence per vertex, and return support requires at least two.

Fix a returned sector, recording its finite high/low choices even when
limiting labels equal half. Delete the return vertices. Every
remaining connected old region has at most one marked high incidence
at each vertex. Mark both high interfaces with deleted returns and
original high external boundaries.

A return with exactly two high arms has one low arm of label
\(x\in[0,1/2]\). Assign a new \(g(x)\) to the old region reached by
this arm. At the original state this increases the action because
\(g\ge0\), while discarding the return action also increases it because
the return action is nonpositive. This new leaf is only a term in the
comparison functional. Reassembly will replace it by the action of an
old vertex, using the exact identity
\[
                        t(1/2,1/2,x)=g(x).
 \tag{9}
\]
It follows directly from the duplication identity for \(J\), and
holds at both endpoints. In particular
\(t(1/2,1/2,1/2)=0\).

Apply (3) to each old region with these additional low-arm profiles.
Each region jointly reoptimizes all its variables while its marked
boundaries are moved to half. No one-coordinate monotonicity is used.
The regions have disjoint free variables. Each new low-arm term
belongs to exactly one region and one removed return vertex.

Reinsert a removed vertex as \((1/2,1/2,x)\), or as the all-half
triple if it had three high arms. Its contribution is exactly the
newly assigned profile, so that profile is not counted a second time.
If the low arm instead ended directly at an original low boundary,
the new contribution is \(2g(x)+c\), at least the former
\(g(x)+c\). A high original boundary is changed to half, preserving
its constant contribution because \(g(1/2)=0\). All original boundary
constants remain present.

The resulting state belongs to the original coupled old polytope and
has action at least the returned sector. Every replacement has a
saturated pair sum. If \(F_0\) is the original strict maximum and
\(\mathcal B\) is the union of these old pair-sum boundary faces, then
\[
                  \delta=F_0-\max_{\mathcal B}\mathcal A_0>0.
 \tag{10}
\]
The positivity follows from compactness and the unique strict old
optimizer. Hence every nonempty return sector has action at most
\(F_0-\delta\). There is no sum of independent probe or cap budgets:
the comparison state is in the same original old polytope.

## 5. Exact finite endpoints and scope

For exact finite supports it is cleanest to normalize labels by
\(d=N-1\), not by \(N\). The old inequalities then become (2) exactly.
For a return, the inequalities
\(i+j,i+k,j+k\ge N=d+1\) and
\(i+j+k\ge2N-1=2d+1\) imply that the complementary labels
\[
                 a=1-i/d,\quad b=1-j/d,\quad c=1-k/d
\]
are nonnegative and satisfy \(a+b+c\le1-1/d\). The real return rate
\[
 J(a)+J(b)+J(c)+J(a+b+c)-J(a+b)-J(a+c)-J(b+c)\le0
 \tag{11}
\]
is therefore evaluated in its proper real domain. Using \(N\) in
place of \(d\) would give total \(1+1/N\) at the lowest return total
and should not be used literally inside that real formula. The uniform
modulus of continuity of \(J\) makes the coordinate change cost
\(O(\log N/N)\), hence only \(O(\log N)\) in the logarithm of a
coefficient. The finitely many smallest levels do not enter the
asymptotic gap.

Recorded finite high labels normalize above half; recorded low labels
normalize at most half. The combinatorial counts persist in their
closures, including ties. Uniform closed factorial estimates, bounded
paired-edge factors, the finite number of tensor choices and the
polynomial number of index states therefore preserve any smaller
positive gap from (10). Old sectors with a high original boundary
still use the separate original positive-component gap from
notes/actual_conway_unflagged_core_probe_bound.md. No internal
bare–bare edge is cut off at half.

The result is a component estimate, with the original complete action
budget. Its insertion into a whole moving-meridian or filled theorem
still requires the already established source, primitive-window and
joint-contour interfaces to be stated for this enlarged component
class. Nothing in the clamping argument identifies an absolute return
stationary state with a geometric representation.

For a higher-valence product, artificial binary edges are unturned
and identify complementary rather than equal labels. The return
independent-set property and the unique-low-arm assignment used above
need not hold there. This proof makes no higher-valence extension.
