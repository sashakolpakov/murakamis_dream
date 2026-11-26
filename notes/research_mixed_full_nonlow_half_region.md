# The complete half-period above the low cutoff

Research theorem, 5 November 2026. The complete unselected right-clamping
and selected-height certificates have passed, together with their full
320-bit saved replays. This argument combines them with the proved
left-region estimates. No full-period or knot-volume conclusion is asserted.

## 1. The integral and its rate

Fix a cyclic word of length \(m\ge1\) in the original three- and
four-crossing blocks. Use its original geometric critical point \(r\),
allocated action \(\Phi\), and critical rate \(M=\Re\Phi(r)\).
The real integration coordinates are normalized to period one. Put
\[
 A_m=[.1,.5]^m,\qquad Q_m=[.1,.45]^m,\qquad P=[.22,.45].
                                                               \tag{1}
\]
For every subset \(S\) of the type-four positions use its exact
[periodic hybrid contour](research_mixed_split_cutoff_hybrid_contour.md).
Its collar width is fixed independently of \(N\). Denote its original
selected integral on a real parameter set \(D\) by
\(\mathcal I_{N,S}^{\rm hyb}(D)\), and sum these integrals over
\(S\) to obtain \(\mathcal Z_N^{\rm hyb}(D)\).

At a target point \(z=z_S(x)\), its complete upper rate is
\[
 \mathcal E_S(x)=\Re\Phi(z)+
       \sum_{j\in S}\max\{\Re g(z_j),-2\pi\Im z_j\}.        \tag{2}
\]
The maximum retains both alternatives in the actual Fourier-polynomial
bound. For an unselected type-four coordinate the height is nonpositive
and its real part is at most .5. Its Fourier rate is already included in
\(\Phi\); the forcing tie at .5 is retained in the uniform upper bound.
Every other factor in the original finite density has a uniform
polynomial prefactor on these compact products.

The complex domains in (2) are the polygons \(\Omega_3,\Omega_4\)
defined in the [selected-height comparison](research_mixed_right_selected_height_removal.md).
Their products are unions of the proved cap/cap, cap/plateau,
plateau/plateau, cap/right-triangle and right-square source products.
The [interface source theorem](research_mixed_left_right_interface_source.md)
supplies the formerly missing cap/right-triangle products. Thus every
original finite block is covered, including all its rows, normalization
factors and both level parities. This is stronger than just the existence
of a critical point on those products.

## 2. A strict left-region bound on its right face

Let \(\mu>0\) be the plateau Hessian constant used in the
[full left-region theorem](research_mixed_full_left_region.md), and put
\[
                         a=\min\{1/2000,\mu/1600\}>0.       \tag{3}
\]
The phase inequalities in that theorem imply
\[
 \mathcal E_S(x)\le M-a
 \quad\text{if }x\in Q_m\text{ and some }x_j=.45.             \tag{4}
\]
Here (4) uses the proof's pointwise inequalities, not an inference from
its integrated conclusion. To verify the extra face condition, follow
that proof's minimum-coordinate transport. It changes only coordinates
below .22, so a coordinate equal to .45 stays equal to .45. If no early
coordinate and no selection remain, plateau concavity gives loss at
least
\[
 \frac\mu2(.45-.39)^2=\frac{9\mu}{5000}>\frac\mu{800},       \tag{5}
\]
since every geometric real coordinate is at most .39. A nonempty
selection or a coordinate in the early interval already gives the
strict loss proved in the left-region argument, each larger than (3).
The frozen-coordinate cases in that argument have the same early-block
loss. These alternatives exhaust \(Q_m\), proving (4).

## 3. Reducing a right-transition coordinate

Take \(x\in A_m\setminus Q_m\). Choose a coordinate
\(t=x_j>.45\). All slow and fast left cutoffs are one on
\([.45,.5]\). Consequently changing this real coordinate within
that interval changes only its own row height. Its neighbors keep
their original target values throughout the change.

If the center is selected, first remove its selection while keeping
\(t\) fixed. Its selected and unselected heights are exactly
\[
 H\min\{6s,1\}R(t),\qquad (\Im r_j)sR(t),
 \quad H=.014,\quad R(t)=400(.5-t)^2,
\]
where \(s\in[0,1]\) is its fixed minimum of neighboring slow
cutoffs. The [selected-height theorem](research_mixed_right_selected_height_removal.md),
including both Fourier alternatives, says this replacement cannot
decrease the comparison rate. The neighbors' selections and their
corrections in (2) are unchanged.

The center is now unselected. Its height has the form \(kR(t)\)
with constant \(k\) in the appropriate type interval. The
[unselected clamping theorem](research_mixed_unselected_right_clamping.md)
therefore gives
\[
 \mathcal E_{\rm before}\le\mathcal E_{\rm after}
                                 -\frac{t-.45}{10},          \tag{6}
\]
when the real coordinate is replaced by .45. The cutoff remains one,
so every other row height is still unchanged. The result is exactly the
hybrid target for the new real point and its remaining selected subset.

Repeat these two operations at every coordinate originally above .45.
They terminate after at most \(m\) real-coordinate changes. The final
point \(x^*\) belongs to \(Q_m\), and at least one coordinate is
equal to .45. If its remaining selection is \(S^*\), then
\[
 \mathcal E_S(x)\le\mathcal E_{S^*}(x^*)
        -\frac1{10}\sum_{j:x_j>.45}(x_j-.45)\le M-a.        \tag{7}
\]
The purpose of (6) is to compare real-valued rates. No integral is
pushed forward by the clamping map, and no monotonicity of the original
finite kernels is needed.

For a two-cycle the two neighboring variables coincide, but its two
edges remain distinct and the comparisons apply by specialization.
For a one-cycle, use \(G_\beta(b)=\phi_{\beta\beta}(b,b)\).
Its derivative is the sum of the two incident partial derivatives,
\(G_\beta'(b)=F_b(b,b,b)\). The same independent-domain derivative
bound applies pointwise along the moving diagonal. For a selected
type-four loop, the vertical comparison is proved in the same way,
using the clipped-domain bound and \(s=1\). There is one original
edge, not the square of a two-edge expression. This proves (7) also
for \(m=1\).

## 4. Returning to the original finite integral

**Theorem 1.**
Set \(\delta=a/2\). At every sufficiently large integer level,
\[
 \left|\mathcal Z_N^{\rm hyb}(A_m)
              -\mathcal I_{N,\varnothing}(P^m)\right|
           \le C N^B e^{N(M-\delta)}.                       \tag{8}
\]
It follows that the restricted sum retains the original nonzero
geometric coefficient, unit carrier and cyclic level power \(N^0\).

For each original block use its complete uniform source bound with
Fourier tolerance less than \(a/(2m)\). Their total tolerance is
less than \(a/2\). Equation (7) then bounds each original selected
density on \(A_m\setminus Q_m\) by a polynomial times
\(e^{N(M-a/2)}\). The hybrid graph Jacobian is bounded independently
of \(N\) for the fixed collar. The domain has finite measure and
there are finitely many selections, so the same bound holds after
integration and summation. On \(Q_m\) the original left-region
theorem already gives (8) with the stronger loss \(a\). Adding the
two disjoint regions proves (8). The central nonzero asymptotic is
unchanged, so this strictly smaller error cannot cancel it.

The conclusion covers arbitrary mixtures of left and right transition
coordinates in this half-period. Coordinates above .5 mixed with left
transitions, and low coordinates mixed with transitions or right regions,
still require separate bounds. External boundary variables and arbitrary
short-filling stability are also outside (8).

```sh
python3 experiments/check_mixed_full_nonlow_half_region.py
```

This checker validates the complete source inputs and their current
proof and code bindings, both clamping domain sets and completed replays,
and the exact loss budgets. It does not substitute tests of finitely
many cyclic words for the arbitrary-length argument above.
