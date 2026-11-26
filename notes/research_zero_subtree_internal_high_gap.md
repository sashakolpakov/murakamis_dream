# Internal high indices in a regular zero-power subtree

Research note, 2 November 2026. The positive Newton variational theorem
already controls the internal high indices of the zero-power source,
provided its minimizing imaginary-angle configuration is regular. The
argument uses concavity and the uniqueness of the old Newton optimizer.
It leaves high indices on the open boundary as a separate question.

The [high-boundary comparison](research_zero_subtree_high_boundary_gap.md)
settles that question. The subsequent
[Newton-coordinate theorem](research_all_zero_subtree_newton_packet.md)
also removes the regular imaginary-angle hypothesis, by estimating the
original positive product sum directly.

## 1. Which polynomial is estimated

Let \(S\) be a nonempty connected proper subtree of the original
finite tree, with all selected powers zero and all original selected
degrees at least three. Use the original kernel and closing functional
\(K_N,\phi_N\) from
[the convex-potential note](research_zero_power_subtree_convex_potential.md).
Define
\[
 K_N^{\mathrm{low}}(t,u)=
       \sum_{2a<N}e_a(-2\cos t)e_a(-2\cos u).
 \tag{1}
\]
In this note only the kernels on the open boundary are restricted:
\[
 Y_{S,N}(\mathbf u)=
 \left(\prod_{v\in S}\phi_N^{(v)}\right)
 \left[
  \prod_{vw\subset S}K_N(t_v,t_w)
  \prod_{\substack{e=vw\in\partial S\\v\in S}}
                         K_N^{\mathrm{low}}(t_v,u_e)
 \right].
 \tag{2}
\]
Every internal index in (2) retains its full range \(0,\ldots,N-1\),
and all original trace multiplicities are retained. The all-low source
\(Z^{\mathrm{low}}_{S,N}\) restricts the internal indices as well.

Let \(\mathbf h_*\) be the unique positive minimizing height vector
of the convex note. Suppose
\[
 \sinh(h_v/2)\sinh(h_w/2)<1\qquad(vw\subset S).
 \tag{3}
\]
Let \(x_e^*\in(0,1/2)\) be its real edge-index maxima and let
\(M=\mathcal L_S(\mathbf h_*)\). Condition (3) holds, in
particular, when every selected degree is at least four. The stronger
edgewise criterion \(\tan(\pi/d_v)\tan(\pi/d_w)\le1\) also
suffices, as proved in the convex note.

**Theorem.** There are constants \(C,a,\delta>0\) such that
\[
 \sup_{\mathbf u\text{ real}}
 |Y_{S,N}(\mathbf u)-Z^{\mathrm{low}}_{S,N}(\mathbf u)|
                  \le C N^a e^{N(M-\delta)}.
 \tag{4}
\]
Consequently \(Y_{S,N}\) has the same nonzero holomorphic asymptotic,
boundary Hessian, and global boundary-strip bound as the all-low source
in [the regular-subtree theorem](research_regular_zero_subtree_low_source.md).
This conclusion includes every internal high-index matching. It does
not yet include a high index on a boundary edge.

## 2. The exact positive Newton expression

Put \(D=N-1\). The exact pairing is
\[
 \phi_N(e_i e_j)=\mathbf1_{i+j=D}.
 \tag{5}
\]
If \(f=\sum_jf_j e_j\), contraction of one internal kernel gives
\[
 \phi_N^{(t)}\{K_N(t,u)f(t)\}
                    =\sum_{i=0}^{D} f_{D-i}e_i(-2\cos u).
 \tag{6}
\]
Thus an internal tree edge is exactly the coefficient reversal
\(\mathsf T(e_j)=e_{D-j}\). At complete boundary angles, the
boundary factor is the positive polynomial
\[
 B_N^{\mathrm{low}}(t)=
     \sum_{2a<N}b_{N,a}e_a(-2\cos t),
 \qquad b_{N,a}=e_a(-2)>0\quad(2a<N).
 \tag{7}
\]
Rooting the selected tree and applying (6) compiles (2) at zero into
ordinary Newton products, genuine coefficient reversals, and the final
closing functional. There is no quotient taken after forgetting double
roots.

Resolve each selected vertex into binary products. The exact positive
structure coefficient at a product is
\[
 \mu_{ijr}=
 \frac{S_{i+j}S_r}
 {S_iS_jS_{r-i}S_{r-j}S_{i+j-r}}
 \quad\text{if}\quad
 \max(i,j)\le r\le i+j\le D.
 \tag{8}
\]
An inadmissible product is zero. The forced final closing product has
coefficient one on its complementary support, so it can be removed
from the action while retaining its exact linear constraint.
The resulting positive state sum has the same rational polytope \(P\)
as the complete Newton expression with ordinary low leaves. In the
reduced-junction description its junctions are precisely the selected
vertices, all internal edges have a reversal, and every external leaf
is unflagged. Since every selected degree is at least three, the reduced
junction criterion supplies a strict state.

The needed finite and variational results are proved in
[the strict Newton syntax](../papers/strict-newton-profiles/syntax.tex)
and [its variational proof](../papers/strict-newton-profiles/variation.tex).
They are also included in the current [Newton calculus manuscript](../papers/newton-calculus/README.md).
Only their algebraic and variational conclusions are used here, not
their geometric interpretation or any signed-source estimate.

## 3. The action is unchanged by the boundary coefficients

For a state scaled by \(D\), give an ordinary leaf its coordinate
\(a\in[0,1/2]\), and give a product its coordinates \((x,y,z)\)
with \(\max(x,y)\le z\le x+y\le1\). Set
\[
 g(a)=J(2a)-4J(a),
 \tag{9}
\]
\[
 m(x,y,z)=J(x+y)+J(z)-J(x)-J(y)
          -J(z-x)-J(z-y)-J(x+y-z).
 \tag{10}
\]
The action \(\mathcal A\) on \(P\) is the sum of \(g\) over
boundary leaves and \(m\) over retained binary products.

The boundary weights in (7) have exactly this profile. Indeed the
uniform Newton product estimate gives
\[
 \log b_{N,a}=N B(a/N,0)+O(\log N)
             =N g(a/D)+O(\log N),\qquad 2a<N.
 \tag{11}
\]
The equality \(B(x,0)=g(x)\) follows by integrating
\(\log(2\sin2\pi s)=\log(2\sin\pi s)+
\log(2\cos\pi s)\). The errors in (11) are uniform, including
the endpoints. Changing the scale from \(N\) to \(D\) changes
\(NJ\) by \(O(\log N)\), using its endpoint modulus of
continuity. The same uniform factorial estimate applied to (8) yields
\[
 \log w_N(\mathbf r)=
        N\mathcal A(\mathbf r/D)+O(\log N)
 \tag{12}
\]
for every positive state of (2). There are only polynomially many
states, since the selected tree is fixed.

The old complete-circle leaf coefficients have the same uniform
\(g\) profile. Thus they and \(b_{N,a}\) differ by bounded powers
of \(N\), uniformly on their common low support. More directly,
(11) and (12) show why the same action applies without any finite
identification of these two kinds of leaf.

The strict Newton variational theorem proves that \(\mathcal A\)
is concave on \(P\), has a unique maximizer, and that this maximizer
is strict. Its proof writes \(\pi g\) and \(\pi m\) as sums
of ideal-tetrahedron volume functions with affine arguments. Their
negative Hessians give strictness at an interior maximum. The inward
logarithmic boundary derivative excludes every nonstrict state of a
strict expression. These facts concern the action and polytope, so
the change of coefficients in (11) does not change them.

## 4. The low constraints are inactive at the optimum

Every original internal edge index is a particular affine wire
coordinate on \(P\); depending on the orientation used in (6), it
is a product output or one minus that output. Denote it by \(q_e\).
The polytope for all-low assignments is
\[
 P_{\mathrm{low}}=
   \{y\in P:q_e(y)\le1/2\text{ for every internal edge }e\}.
 \tag{13}
\]
Boundary leaf coordinates already lie in \([0,1/2]\).

We first establish
\[
 \max_{P_{\mathrm{low}}}\mathcal A=M.
 \tag{14}
\]
The upper estimate in (12), the polynomial state count, and the
all-low asymptotic with positive leading coefficient imply
\(\max_{P_{\mathrm{low}}}\mathcal A\ge M\).
For the reverse inequality, choose any rational point of
\(P_{\mathrm{low}}\). Along an infinite sequence of even positive
integers \(D\) divisible by all its denominators, its scaled labels
are exact integer states. The corresponding levels \(N=D+1\) are
odd, and \(q_e\le1/2\) becomes \(2a_e\le D<N\), exactly
the low condition. All product support constraints are homogeneous
with scale \(D\), so no rounding or congruence issue arises.
Its positive weight, by (12), cannot exceed an all-low sum whose
rate is \(M\). Hence its action is at most \(M\). Rational
points are dense in the rational polytope, and the action is
continuous. This proves (14). The subsequence is used only to
identify a continuous maximum; the finite estimates below hold at
both level parities.

Every maximizer in (14) has all its original physical edge coordinates
equal to \(x_e^*\). To prove this, suppose one differs from
\(x_e^*\), and choose a small closed interval around each
\(x_e^*\) so that the proposed coordinate lies outside its
interval, with positive separation. The exact all-low Fourier bound
gives a strict gap for all states with that property. Applying the
same rational-state argument to nearby rational points yields a
strictly smaller action, a contradiction. Boundary leaf coordinates
are included in this argument, because they too are original low
edge indices in the all-low theorem.

Under (3), every \(x_e^*\) is strictly smaller than \(1/2\).
Thus all the extra inequalities in (13) are inactive at a maximizer
\(y_*\) of the restricted problem. A relative neighborhood of
\(y_*\) in \(P\) is contained in \(P_{\mathrm{low}}\), so
\(y_*\) is a local maximum of \(\mathcal A\) on \(P\).
A local maximum of a concave function on a convex set is global:
if another point had a larger value, the segment toward it would
increase the function immediately. Therefore
\[
 \max_P\mathcal A=M.
 \tag{15}
\]
The unique-optimizer theorem for the strict Newton expression implies
that \(y_*\) is also the unique global maximizer. Compactness now
gives a strict gap
\[
 \max_{\substack{y\in P\\q_e(y)\ge1/2\text{ for some internal }e}}
                    \mathcal A(y)<M.
 \tag{16}
\]
If there is no internal edge, the set in (16) is empty and the claimed
internal-high estimate is immediate.

## 5. The original real and complex boundary variables

At finite level an internal high index satisfies
\(2a_e\ge N=D+1\), so its scaled coordinate lies strictly above
\(1/2\) and is covered by (16). Equations (12), (16), and the
polynomial state count give (4) at zero boundary angles.

For each assignment, every selected Newton trace is nonnegative.
Every boundary index in (2) is low, so its Laurent coefficients are
positive and
\[
 |e_a(-2\cos u_e)|\le e_a(-2)
                  \qquad(u_e\text{ real},\ 2a<N).
 \tag{17}
\]
Taking absolute values term by term proves the same bound uniformly
for real boundary angles. Since each boundary spectral degree is at
most \(N-1\), the gap persists on a sufficiently small complex
polydisk. It follows that the difference in (4) cannot change the
nonzero local packet, its phase, or its amplitude.

For the global boundary-strip bound, combine (4) with the angular
loss for the all-low part. On the real torus, decrease the angular
constant so that its bounded sum is smaller than the gap in (4).
Near the complete boundary use the holomorphic packet and its negative
real Hessian. Away from it use polynomial continuation of the strict
real gap on a finite cover by products of spectral intervals. This is
the same argument as in the all-low theorem and supplies its stated
quadratic dependence on the imaginary boundary angles.

The full original polynomial differs from (2) by assignments with at
least one high boundary index. Those assignments are not in the
polytope \(P\), whose leaves are low by definition. The present
concavity argument therefore does not estimate them. At odd levels
their complete-boundary coefficients vanish, while at even levels
they need not; neither observation controls the full boundary
polynomial by itself. Their real-boundary estimates and their
continuation must be supplied before (2) can be replaced by the full
source in a further-filling theorem.
