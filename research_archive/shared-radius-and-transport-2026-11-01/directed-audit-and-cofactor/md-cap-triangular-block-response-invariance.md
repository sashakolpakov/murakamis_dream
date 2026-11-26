# Triangular blocks preserve the original cap response and its spectral gap

This note gives a geometric decomposition criterion for the actual one-cap source. The other crossing regions remain central at spectrum -2, and levels are odd. It does not estimate several noncentral regions or a full filling period.

The new comparison is a classical elimination identity for an arbitrary simple triangulated triangular disk, not merely a stellar subdivision. It keeps all boundary loads, all original ordinary demands, and the original protected zeros. It implies that the exterior pressure curve, complete action, and every residual boundary capacity change by the same additive constant. Consequently a proved original-target cap estimate applies to a fixed larger diagram whenever these triangular blocks reduce its cap exterior to a certified one. One applies the finite stable-section theorem separately to the actual larger source; no finite signed-polynomial replacement is claimed.

## 1. An arbitrary triangular packing block

Let P be a finite triangulated disk with boundary triangle abc, all three boundary vertices distinct, and k interior vertices. Assume adjoining the outer face abc gives a simple triangulated sphere. The trivial disk k=0 is also allowed. No restriction is imposed on separating triangles or cycles inside P.

Write Q for the actual half-triangle potential from the cap response note. Thus each triangle supplies 1/2, every interior ordinary face has demand one, and
\[
 Q(a,b,c)=\max_{\alpha_i\ge0,\ \sum\alpha_i=1/2}
 \left[\sum_i f(\alpha_i)+\sum_i\alpha_i\log a_i\right],
\qquad f'(s)=\log\cot(\pi s).
\tag{1}
\]
Zero weights mean that their corresponding loads are zero. Initially all boundary weights are positive. Define the block pressure
\[
 \mathcal Q_P(a,b,c)=\inf_{\ell_i>0,\ i\in I_P}
 \left[\sum_{t\in P}Q_t(\ell)-\sum_{i\in I_P}\log\ell_i\right].
\tag{2}
\]
The proposed comparison is
\[
                \mathcal Q_P(a,b,c)=Q(a,b,c)+C_P,
\tag{3}
\]
where C_P depends only on the labeled triangular block, not on its boundary weights. For a one-vertex stellar block this is the previously proved identity with C_P=v_oct/pi. Here the disk can have arbitrary triangulation.

## 2. Why the pressure difference is constant

The fixed-boundary packing proof in `actual_smoothed_source_capacity_blocks.md` §4, also reproduced in `actual_balanced_terminal_fan_volume.md` §2, applies to exactly this disk. It gives the following facts for every three prescribed positive boundary radii r_a=1/a, r_b=1/b, r_c=1/c.

The disk has 2k+1 triangles. A strict Hall allocation supplies total angle 2pi at every interior vertex and leaves total angle pi at the three boundary vertices. Maximizing the strictly concave entropy, with the prescribed boundary log weights, gives an interior maximizer: the derivative toward a strict allocation excludes a zero supported corner. Its radius multipliers are positive and finite. The Euclidean center triangles have side lengths r_i+r_j; their development is single-valued because every interior angle sum is 2pi. Its boundary is the prescribed center triangle, traversed once. The degree argument makes this development embedded, so its three total boundary angles are exactly the angles of that center triangle. This includes disks with separating triangles.

Those are precisely the minimizers of (2), by the entropy/radius duality. If Theta_a is the total center angle at a, the envelope derivative is
\[
 \frac{\partial\mathcal Q_P}{\partial\log a}
       =\frac{\Theta_a}{2\pi}.
\tag{4}
\]
For the unrefined boundary center triangle, tangent-circle trigonometry gives
\[
 \frac{\Theta_a}{2\pi}
   =\frac1\pi\arctan\frac{a}{\sqrt{ab+bc+ca}}
   =\frac{\partial Q(a,b,c)}{\partial\log a},
\tag{5}
\]
and likewise at b,c. Hence all three derivatives of the difference in (3) vanish. The positive octant is connected, proving (3). An absolute definition of its constant is
\[
 C_P=\mathcal Q_P(1,1,1)-Q(1,1,1).
\tag{6}
\]
There is no undetermined perimeter term. Homogeneity is also consistent: P has half-supply k+1/2 and k interior demands, so both sides have degree 1/2 under common boundary scaling.

No knot interpretation of this elimination was used. It is a statement about the original triangle packing and source normalization.

## 3. Every closed boundary load and protected zero is preserved

Let alpha=(alpha_a,alpha_b,alpha_c) be a nonnegative boundary load of total 1/2. Let E_P(alpha) be the maximum entropy over the original triangles of P with each interior demand one and these exact aggregate boundary loads. Give it value -infinity when that fiber is empty. Its feasible set is compact; its value is concave and upper semicontinuous on its compact domain. Finite concave duality gives
\[
 \mathcal Q_P(e^q)=\max_\alpha\{E_P(\alpha)+\alpha\cdot q\}.
\tag{7}
\]
The identical conjugate (3) is that of the single-triangle entropy plus C_P. Closed concave biconjugacy therefore gives
\[
       E_P(\alpha)=\sum_i f(\alpha_i)+C_P
       \quad\text{on the entire closed half-simplex}.
\tag{8}
\]
In particular every such boundary fiber is feasible. This argument does not require finite boundary multipliers at an endpoint.

If an old boundary vertex is protected, its aggregate load is zero. Nonnegativity forces every corner at that vertex to remain zero in P. Every other old face retains its original aggregate boundary load; the added interior demands are exactly one each. Thus (8) can be inserted before any optimization over surrounding triangles. It does not allow a change of mark or an independent reweighting of an incidence.

The usual strict supported problem is also available after one or two boundary vertices are protected. Here is the finite feasibility check, rather than an assumption of a nondegenerate zero-weight limit. Pool the positive boundary corners into one destination of demand 1/2. Interior demands remain one. An interior subset S touches at least 2|S|+1 triangles, by the same punctured-sphere count. For a proper subset containing the pooled boundary, its complement consists of interior vertices T and at most two protected vertices. If T is nonempty, at most 2|T|-1 disk triangles are wholly supported on that complement, by the bounded-face count of the simple planar graph on T and those at most two vertices. For T empty no triangle is supported solely on at most two protected vertices. These are strict Hall inequalities. Every row has a surviving corner. Subtracting a sufficiently small positive amount at every allowed corner preserves feasibility; singleton rows are interpreted relatively.

The entropy boundary argument gives positivity on all allowed nonfixed corners. The supported ordinary graph is connected after deleting at most two boundary vertices, as follows by capping P and using the simple-sphere link rerouting argument. Grounding any positive boundary weight removes the sole scaling kernel. Therefore (2) has a finite unique interior minimizer also for these supported boundary data, and the corresponding Hessians are nondegenerate. This verifies the local positive-packet hypotheses needed when a block touches the original protected mark.

## 4. The entire original exterior response is unchanged

Now fix an actual simple matched sphere with its original protected nonmatching edge and selected cap e*. Its source order is (C,0,A,0), with A the overloaded ordinary middle. Keep the cap's two triangles unchanged. Suppose an exterior triangle is replaced by P, with its three original vertices and orders retained and every new vertex ordinary.

Use a tilde for the resulting actual diagram. At every finite real tilt A=e^z,C=1, joint minimization over all original exterior variables can be done first inside P. Equation (3) gives
\[
 \widetilde F(z)=F(z)+C_P,
 \qquad \widetilde\nu(z)=\nu(z),\qquad
 \widetilde\kappa(z)=\kappa(z).
\tag{9}
\]
No saddle approximation is used in this identity. Alternatively (8) proves it by first holding every surrounding boundary load fixed.

The same closed identity, with all complete triangles restored, gives
\[
 \widetilde\Phi=\Phi+C_P.
\tag{10}
\]
In particular the original restoration formula is retained literally:
\[
 \widetilde\Phi
   =\min_z\{\widetilde F(z)+q(z)-z\},
 \qquad q(z)=\frac2\pi\operatorname{Ti}_2(e^{z/2}).
\tag{11}
\]
The complete restoration point and the half-load point do not move. The actual original augmented-volume theorem gives
\(2\pi\widetilde\Phi=\operatorname{Vol}(\widetilde Y)\), not the volume of the unrefined exterior.

Let R(s) be the exterior entropy at its two unextracted loads A:s,C:1-s, with every other original ordinary demand one. Equation (8), before the outside maximum, also proves
\[
              \widetilde R(s)=R(s)+C_P\qquad(0\le s\le1).
\tag{12}
\]
Thus the original omitted-tail capacity margin
\(\Phi-\max_{s\ge1/2}R(s)\) is unchanged. Equations (9)--(12) iterate over finitely many blocks with disjoint interiors, including nested substitutions. Constants add even when boundary vertices of different blocks coincide, since their aggregate loads remain identified throughout.

This also describes a decomposition of a given fixed diagram along separating triangles away from the selected cap. The unrefined object is only a device for evaluating its classical pressure. No change is made to that diagram's finite source or its original coefficient targets.

## 5. Consequence for the genuine odd spectral functional

At odd levels, each actual central factor is its original N^2 product of two determinant cofactors. Therefore the new exterior is again the actual nonnegative stable binary polynomial, after extracting every new and old ordinary target d=N-1. Its original protected numerator and cutoff are the same as before. The finite sine-Cauchy and stable-section inequalities in `research_cap_uniform_spectral_gap.md` apply directly to this polynomial; no finite identity between its coefficients and those of the unrefined diagram is needed.

Every classical quantity in that theorem changes as follows:
\[
 \begin{aligned}
 \widetilde F(0)-\widetilde\Phi&=F(0)-\Phi,\\
 \widetilde F(\log T)-\tfrac12\log T-\widetilde\Phi
    &=F(\log T)-\tfrac12\log T-\Phi,\\
 \widetilde\nu&=\nu,\qquad \widetilde\kappa=\kappa,
 \qquad \widetilde\gamma_D=\gamma_D.
 \end{aligned}
\tag{13}
\]
Consequently every strict two-pressure certificate from that theorem transfers with the same exponential margin. The response-region criterion also transfers. Polynomial constants and starting levels may change with the fixed larger diagram, but that does not change the exponential inequalities.

In particular the recorded R54 certificate gives, for every actual diagram assembled from that cap exterior by these central triangular substitutions,
\[
 \limsup_{N\ {m odd}}\frac1N
 \log\sup_{\sigma\in[-2,2]}|\widetilde S_N(\sigma)|
 \le\widetilde\Phi-\min\{3/1000,\gamma_D\}
 <\widetilde\Phi.
\tag{14}
\]
This includes first normal derivatives with their original polynomial normalization, and an optional filling functional in this cap variable alone, exactly as in the source theorem. It does not permit filling or varying the other spectra. It is still an odd one-cap statement, not a full knot-volume equality.

## 6. Literal matched-sphere realizations

The substitutions can be realized by actual matched spheres. Start with an exterior triangle t of the old sphere and its matched neighbor t'. Take any simple matched sphere B with a chosen face f. Remove f, leaving the triangular disk P. The matching of B pairs f across one of its boundary edges with a triangle g. Identify that edge, in the oriented boundary identification, with the old matched side shared by t,t'. Delete t and f, retain P, pair g with t', and retain all other old and block pairings.

Every new matched pair has four distinct vertices. The only old vertices of the block are its three boundary vertices; all block interior vertices are fresh. The union remains a simple oriented triangulated sphere. The selected cap and protected mark remain unchanged because t is outside its two triangles. The original boundary attachment orders are retained. The existing inverse-cut construction gives its actual augmented link in S^3 and its original primitive disk curves. If a main knot is required, the connected-circle spanning-tree parity argument supplies a parity assignment; it does not imply that a previously prescribed parity assignment remains a knot.

The block B is arbitrary. Its internal graph can have many cycles and need not have a tangle-operation-tree presentation. This produces a broad structural class for the one-cap estimate, while making no claim that every simple matched sphere decomposes this way to the same cap core. A separating triangle may be detected and eliminated in the classical comparison of an already specified diagram; the diagram's actual knot and volume target are never replaced by those of a reduced diagram.

As an operation on diagrams this substitution can change knot type and the augmented complement. It is not a cancellation of tangles, a finite source factorization, or an unproved topological decomposition theorem. The actual larger complement is identified independently by the simple-sphere packing/cut theorem; (10) then computes its augmented volume change through the exact source action.

## 7. An explicit symmetry criterion for cap cores

There is a simple geometric class in which no numerical certificate is needed. Suppose the retained exterior triangle incidence admits an automorphism exchanging A and C, permuting the two protected vertices, and permuting the extracted ordinary vertices. It need not preserve their matching into central pairs: the classical central potential is the sum over the same individual triangles, and all extracted demands are one. The universal half-triangle potential Q is symmetric in its three weights.

The reduced exterior potential is therefore symmetric in A,C and homogeneous of total boundary degree one. With C=1 it obeys
\[
                     F(z)=z+F(-z).
\tag{15}
\]
Thus nu=1/2 and H(z)=F(z)-z/2 is even and strictly convex. Its minimum is H(0)=F(0). At the finite attained complete restoration point z*,
\[
             \Phi=H(z_*)+q(-z_*)>F(0).
\tag{16}
\]
The uniform finite cap inequality with T=1 consequently gives a strict original odd spectral gap even without estimating a numerical conductance. This is within the existing response region, not an enlargement of that analytic region. The useful extension is that arbitrary asymmetric triangular blocks may be attached afterward: (9)--(13) preserve this inequality even when the full diagram no longer has the symmetry.

A concrete cap core is the sphere on vertices C,u,v,A,O. Its cap triangles are Cuv and CvA, paired across Cv; mark uv. The retained disk consists of CuO, uvO, vAO, ACO. Pair CuO with uvO across uO, and vAO with ACO across AO. The involution (A C)(u v), fixing O, preserves the exterior triangle set. All protected and ordinary targets are literal. Strict exterior feasibility follows directly from the supported half-load transport, or from its one interior radius equation. Hence it is a valid seed for (16). Attaching arbitrary matched triangular blocks yields arbitrarily large actual sources, without claiming that this small seed itself is a new knot family.

## 8. What this does and does not settle

The reduction shows why graph size, cap incidence degree, or the mere number of cycles cannot alone force a stronger response: arbitrary central triangular blocks leave the entire normalized response curve unchanged. Conversely they need not destroy a valid coherent cap gap. The correct invariant of this comparison is the reduced cap pressure, not the number of surrounding triangles.

For an irreducible cap-containing sphere with no applicable separating triangular blocks, the general comparison remains open. The generic stable-polynomial obstruction in the response note is not an actual-sphere counterexample, and this decomposition does not promote it to one. No inequality for all original matched spheres, all sectors, neighboring spectral variables, even levels, or filled periods is claimed.

The proof imports the fixed-boundary packing/development theorem, the exact half-triangle entropy duality, the actual odd central pressure theorem, and the finite protected sine-Cauchy/stable-section inequalities. Its new geometric calculation is (3)--(8) for arbitrary triangular blocks and the resulting full-curve invariance (9)--(13). Finite numerical experiments are not used as proofs.
