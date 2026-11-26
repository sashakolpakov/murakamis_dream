# The coupled central currents for three original power-three vertices

Research proof, 4 November 2026. Completed source artifacts and frozen
manuscripts are unchanged.

The two actual complete caps and the retained middle vertex have a
coercive six-variable phase. A simultaneous height deformation controls
the central wire joins without estimating the cap and vertex separately.
The assertions concern the central source after the real-index and
angular complements have been separated. They do not remove those
complements or the outer wire periods.

## 1. The original phase and its critical point

Use the actual cap phase \(\mathcal F_3\) and retained phase \(F\)
from [joint concavity](research_three_vertex_joint_concavity.md), retaining
the affine cardinal factor. In the order \(z=(x,\tau,s,t,y,\sigma)\), put
\[
 \mathcal G_3(z)=\mathcal F_3(x,\tau)
       +F(s,t;x,y)-\pi i(x+y)+\mathcal F_3(y,\sigma).
 \tag{1}
\]
This is the principal phase of the literal source
\(N^2\iint W_N(x,w_L)\widetilde V_N^{(40)}(x,y)W_N(y,w_R)\,dx\,dy\)
at complete ordinary outside colors. Here \(W_N\) is the original
one-vertex cap, and the middle vertex deletes precisely
\(i,j\le\lfloor N/40\rfloor\). No further boundary change is made.

The [all-length geometric/source theorem](research_three_chain_geometric_chamber.md)
supplies the actual length-three critical point, including its exact
unexponentiated logarithmic lifts. It lies in the following small boxes:
\[
 \begin{split}
 x_*=y_*&\in(.1796561796584\mathbin\pm10^{-12})
                 +i(.0988146969420\mathbin\pm10^{-12}),\\
 \tau_* =\sigma_*&\in(1.5262658094748\mathbin\pm10^{-12})
                 -i(.9744144200478\mathbin\pm10^{-12}),\\
 s_*=t_*&\in(.3453470138444\mathbin\pm10^{-12})
                 -i(.0045768576124\mathbin\pm10^{-12}).
 \end{split}
 \tag{2}
\]
Equality of the paired coordinates follows from reflection symmetry and
the established uniqueness, not rounded centers. The new checker uses
the old exact rational centers as proposals for a fresh original
three-variable period self-map, with complex disk radius \(10^{-23}\).
It recomputes a rational preconditioner and certifies every contraction
and self-map margin. The old proved coordinate error
\(8/(3\cdot10^{25})\) puts the known positive geometric root strictly
inside these disks; uniqueness identifies it with the fresh root.
The original positive-edge inequalities are also checked directly.
The checker verifies the source domains and evaluates the original phase to give
\[
                 M_3:=\Re\mathcal G_3(z_*)>3.17595.
 \tag{3}
\]
The [open action calibration](research_three_chain_action_volume_calibration.md)
fixes this real value as the original marked action; no homogeneous
constant is substituted for it.

Let
\[
 \mathcal R=[.14,.20]\times[0,1.8]\times B\times B
                    \times[.14,.20]\times[0,1.8],
 \quad B=[1/4,9/20],\quad Y_h=\frac{\log2}{2\pi},
 \tag{4}
\]
and choose the initial height vector
\[
        h^0=(Y_h,-H_0,0,0,Y_h,-H_0),
                 \qquad H_0=24961509/25000000=.99846036.
 \tag{5}
\]
Every height on the segment from (5) to \(h^*=\Im z_*\)
belongs to the regular joint chamber. Both cap factorial strips stay
strictly positive, and all original retained denominator radii stay
below one.

## 2. Coercivity and all final faces

**Lemma 1.** Throughout this chamber, including index heights
\(|\Im s|,|\Im t|\le.01\),
\[
 -\Re d^2\mathcal G_3\succeq
 (3/4+\pi/5)(dx^2+dy^2)+\tfrac34(ds^2+dt^2)
                 +\frac{d\tau^2+d\sigma^2}{20\pi}.
 \tag{6}
\]
At the actual critical heights every real face of \(\mathcal R\)
has phase at most \(M_3-1/4000\).

*Proof.* Add the retained four-variable bound (8a) to the two actual
cap bounds (11) in the joint-concavity note. These are identities and
inequalities for the unsummed source. Integrate the negative Hessian
along the real segment from the critical point to any point of the
rectangle. The minimum distance to a wire face exceeds \(.0203\),
to an index face exceeds \(.0953\), and to a cap-angle face exceeds
\(.273\). Consequently the three possible lower losses are greater
than
\[
 \tfrac12(3/4+\pi/5)(.0203)^2,\qquad
 \tfrac38(.0953)^2,\qquad \frac{(.273)^2}{40\pi},
 \tag{7}
\]
each greater than \(1/4000\). All comparisons are outward checked.
Holomorphy also makes the real phase convex along every joint imaginary
direction inside this chamber. \(\square\)

## 3. The original index currents and initial faces

Put both original index rectangles at
\(B+i[-1/100,1/100]\), with their real sides at the original
half-grid cuts within \(O(N^{-1})\) of the ends of \(B\).
Keep both wire heights at \(Y_h\) and both cap heights at \(-H_0\).

**Lemma 2.** The following upper bounds hold on the entire indicated
real domains:
\[
 \begin{array}{ll}
 \Re\mathcal G_3<3.17,
   &\text{if either index lies on a vertical side},\\
 \Re\mathcal G_3<3.182,
   &\text{on every product of horizontal index sides},\\
 \Re\mathcal G_3<3.174,
   &\text{on all initial wire or cap-angle faces of }\mathcal R.
 \end{array}
 \tag{8}
\]
The first bound includes both-vertical products and every height on
their sides. In the last line the index heights are zero, as in (5).

*Proof.* At fixed heights the full six-real-variable phase is concave
by (6). At any rational supporting point \(p\) in a real rectangle
\(\prod[a_j,b_j]\),
\[
 \Re\mathcal G_3(z)
 \le \Re\mathcal G_3(p)
       +\sum_j\max\{\partial_j\Re\mathcal G_3(p)(a_j-p_j),
                         \partial_j\Re\mathcal G_3(p)(b_j-p_j)\}.
 \tag{9}
\]
Both the value and each term on the right are evaluated outward.
Convexity in the two imaginary index coordinates reduces a vertical
side to the four height corners. Four real index faces therefore
require 16 supporting planes. Four additional planes cover the
horizontal products. The eight remaining planes cover both wire
and both cap-angle faces at (5). The exact domain list has 28 entries,
including every real boundary and every index-height corner.

The certificate accepts the bounds (8) only after freshly evaluating
each original value and gradient at its rational supporting point.
The stored points are proposals, not numerical acceptance tests.
The independent replay uses negative-frequency retained primitives,
the reflected real cap primitive and real logarithmic derivatives.
It reconstructs all domains and accepts no optimizer or author module.
This proves (8) on the full rectangles, not only at the supporting
points. \(\square\)

Each nonconstant original cotangent factor on a horizontal index side
has exponential loss at least \(2\pi N/100\). Since
\(3.182-2\pi/100<3.17\), all such aliases are below the first
rate in (8). On half-grid vertical sides the cotangent is uniformly
bounded. The exact two-index residue identity thus bounds all 12
vertical-containing products and every alias, while the four constant
products retain their original coefficient \(+N^2\).
The strict margins absorb finite-cut rounding and every fixed source
derivative. No physical first normal or parity factor is discarded.

## 4. A simultaneous central height deformation

**Proposition 3.** For the principal central rectangle left after the
index-current extraction, simultaneous translation from (5) to
\(h^*\) introduces only boundary currents with upper rate
\[
                         \max\{3.174,M_3-1/4000\}<M_3.
 \tag{10}
\]
At its final heights the principal phase has a unique nondegenerate
maximum at \(z_*\). A localized principal contribution has the
original normalization
\[
                   C_{N,3}^2\kappa N^{-3/2}
                       A_3e^{N\mathcal G_3(z_*)}(1+O(N^{-1})),
                         \qquad A_3\ne0.
 \tag{11}
\]
This does not identify the complete two-wire integral with (11).

*Proof.* Translate the entire six-dimensional rectangle by the common
homotopy \(h^0+\theta(h^*-h^0)\), \(0\le\theta\le1\).
The exact original factorial/root-product interpolants are holomorphic
throughout the swept chamber. The cap trace heights remain strictly
negative; after constant-cotangent extraction the principal index
integrand has no lattice pole. Stokes' formula retains the 12 swept
real faces, with their actual orientations and Jacobians. It does
not create an independent-height box of currents.

On each face, convexity along this joint imaginary segment bounds the
phase by its two endpoint values. Lemmas 1--2 give (10); the initial
index faces are included in the first line of (8). Compactness and the
strict original interpolation estimates turn these phase inequalities
into polynomial-times-exponential bounds for the finite currents.

At the final heights (6) supplies a nondegenerate complex Gaussian
with positive definite negative real Hessian. The original cap symbols
and retained symbol are nonzero at the actual critical point. The two
cap-angle integrands carry \(C_{N,3}^2N^{-1}\); the retained summand
carries \(\kappa N^{-3/2}\), and its exact index extraction contributes
\(N^2\). The two original wire measures contribute another \(N^2\).
The six-variable Gaussian contributes \(N^{-3}\). Their product is
exactly the power and carrier in (11). All square-root and trace
orientations are the original ones; positive Gaussian accretivity
prevents its local coefficient from vanishing.

Full source closure still requires the real indices outside \(B^2\),
the remaining angular/physical cap currents, the outer wire periods
and any chosen corner restoration. Those terms are not included in
(10). No lower bound is inferred from an absolute matrix norm.
\(\square\)

## 5. A coherent upper estimate for an angular remainder

There is a further useful upper estimate at the initial heights (5).
Leave one cap untraced, retain the other cap's positive bottom, and keep
the middle indices real in \(B^2\). The remaining coherent phase is
\[
 \mathcal G_{\rm one}(x,\tau,s,t,y)
    =\mathcal F_3(x,\tau)+F(s,t;x,y)-\pi i(x+y),
 \tag{12}
\]
with \(x,y\) at height \(Y_h\), \(\tau\) at height \(-H_0\),
and all five real coordinates in their intervals (4). It is concave
by the same positive Hessian decomposition, including the untraced
wire. One additional rational supporting plane proves
\[
                         \Re\mathcal G_{\rm one}<1.914.
 \tag{13}
\]
The bound applies with the two caps exchanged.

Consequently, if an actual grouped angular remainder of each cap has
uniform rate below \(1.26\) on this initial wire segment, its product
with the other positive cap and the central real-index vertex has rate
below \(1.26+1.914=3.174<M_3\). If both cap factors are remainders,
the [global homogeneous-height retained bound](research_three_vertex_global_wire_bound.md)
gives rate at most \(2(1.26)+2c<3.167<M_3\). The smaller
\(L_{40}\)-retained set preserves that absolute summand bound.
These are bounds for the coherently grouped actual source before
taking absolute values; they require the indicated separate cap
remainder estimate. No such estimate is inferred from (13).

## 6. Reproduction

Run

```sh
python3 experiments/check_three_chain_three_central_currents.py --precision 192
python3 experiments/replay_three_chain_three_central_currents.py --precision 256
```

The [author checker](../experiments/check_three_chain_three_central_currents.py)
and [record](../repro/results/research-three-chain-three-central-currents.json),
and the [independent replayer](../experiments/replay_three_chain_three_central_currents.py)
and [record](../repro/results/research-three-chain-three-central-currents-replay.json),
retain the exact 28 central domains, the additional plane (13),
geometric-source provenance and all margins.
