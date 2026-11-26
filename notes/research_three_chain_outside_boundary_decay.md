# Outside-color decay for propagated three-crossing chains

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The internal Fourier envelope is supplemented here by a loss in the
actual ordinary outside color. The loss is first established in the
original prepared-cap contours. It is then carried through the same
complete-source saddle contours, without accumulating a norm-to-action
comparison cost. This supplies the boundary estimates needed for later
fillings; it does not change the marking or identify an arbitrary
closure with a knot.

## 1. The ordinary boundary in the preparation contours

Write \(\zeta=-2\cos u\), \(U(u)=1-\cos u\), and retain the
original source
\[
 F_{1,N}(y,u)=v(-2\cos u)^TA_N^2h(y),\qquad
 x_h=\frac16+\frac{i\log2}{2\pi}.
 \tag{1}
\]
Its complete-color phase is \(S_1(y,0)\), with
\(M_1=\Re S_1(x_h,0)>1.9113\). Let
\(R=.005\), \(W=.009\), \(v_r(t)=\min\{d_{\mathbb T}(t,0),r\}\).

**Lemma 1.** There is \(d>0\) such that, uniformly for real
\(-\pi\le u\le\pi\),
\[
 \begin{split}
 |F_{1,N}(x_h+z,u)|
   &\le CN^q e^{N[\Re S_1(x_h+z,0)-dU(u)]},&& |z|\le R,\\
 |F_{1,N}(x_h+t,u)|
   &\le CN^q\{e^{N[\Re S_1(x_h+t,0)-dU(u)]}
                              +e^{1.9107N}\},&& |t|\le.02,\ t\in\mathbb R,\\
 |F_{1,N}(x_h+t,u)|
   &\le CN^q e^{N[M_1+.0113v_{.01}(t)-(29/20)v_{.01}(t)^2-dU(u)]},
                                  &&t\in\mathbb R.
 \end{split}
 \tag{2}
\]
The constant may be reduced so that all three estimates use the same
\(d\). Each fixed ordinary \(\zeta\)-derivative has the same
exponential bounds with polynomial cost. Both level parities are
included. The second line retains its separate absolute error.

*Proof.* We identify exactly where the outside color occurs in the
existing finite preparation, before taking any absolute values: it
occurs only in the original edge \(K_N(\tau,u)\) inside the cap
\(\phi_N[R^3\mathbf B_N(x)K_N(\cdot,u)]\). The retained-vertex
indices and the internal Fourier kernel are independent of \(u\).
Use exactly the contours and the order of decomposition in
[the quantified disk preparation](research_three_prepared_cap_quantified_source.md)
and [the wider real preparation](research_three_prepared_cap_real_extension.md).

Their selected cap critical angles satisfy, uniformly on the closed
output disk and the real interval \([-.02,.02]\),
\[
            3/2<\Re\tau_c<31/20,
       \qquad .97<-\Im\tau_c<1,
       \qquad |\cos(\tau_c/2)|<1.
 \tag{3}
\]
For the disk these are the explicit 4,096-cell bounds in the quantified
proof. For the real interval the same assertions follow from the 399
stored critical-coordinate boxes; the focused checker verifies their
domain inclusions without repeating their Newton solves. The last
inequality also follows directly from
\((\cosh1+\cos(3/2))/2<1\). Since \(31/20<\pi/2\), this
compact critical set lies strictly inside the domain of
[the free-edge whole-period theorem](research_pair_free_boundary_kernel.md#7-whole-outside-period-decay-and-a-complex-strip):
\(0<\Re\tau<\pi/2\), \(0<-\Im\tau<1.07\),
\(|\cos(\tau/2)|<1\). On a fixed neighborhood of this entire
set that theorem gives
\[
 |K_N(\tau,u)|\le CN^q
 e^{N[\Re\psi(\tau,0)-d_0U(u)]},\qquad d_0>0.
 \tag{4}
\]
The same assertion holds for the literal low kernel \(L_N\)
there: its omitted radical has the strictly smaller rate
\(|\Im\tau|\), while \(\Re\psi(\tau,0)>|\Im\tau|\)
uniformly on this compact neighborhood. Decrease \(d_0\) to
absorb that difference for \(U\le2\). This use of the edge
theorem is confined to selected critical neighborhoods.

Every other piece of the original preparation remains bounded at
its complete-color rate for all real outside colors. This is not
an assumption that the complete outside value is a pointwise maximum
of a complex kernel. The precise source bounds are:

* On every remaining cap contour the color \(-2\cos\tau\)
  stays in a compact subset of \(\Re z<2\). Lemma 1 of
  [the free-boundary observation proof](research_free_boundary_half_charge_observation.md)
  gives the literal low-kernel bound
  \(|L_N(\tau,u)|\le CN^q e^{N\Re\psi(\tau,0)}\) for every
  real \(u\). It comes from physical Jacobi rows and polynomial
  interpolation, not from continuation of a complete-end relative error.
* The physical rows removed before the cap contour have
  \(|F_a(-2\cos u)|\), \(|G_a(-2\cos u)|\le
  \operatorname{poly}(N)F_a(-2)\), by equations (11)--(15) of
  that same proof. Thus all actual selected first normals keep
  their original tail bounds. The odd simple node uses its value only.
* The original outside radical is removed before the cap contour,
  using its physical values and normals. Its real-color polynomial
  bounds are uniform on \([-2,2]\), so this error keeps its
  complete rate. It is not replaced by a complex full-kernel bound
  on distant cap angles.
* The [Fourier corner estimate](research_three_chain_fourier_corner_transfer.md),
  Theorem 2 and Section 4, is already uniform over all real ordinary
  outside colors and their fixed normals. Its two-vertex rate is
  below \(1.715\). Thus restoring the exact original word is harmless
  uniformly in \(u\).

Consequently all the cap exterior intervals, original physical tails,
reflected factorial pieces, folded angular currents, index aliases,
wire joins and joint-translation faces keep the bounds of the two
preparation proofs. Nothing in these changes a contour or a residue.
The exact source is first decomposed in their original order; no
bound for a canceled sum is reused for an arbitrary subset.

On the final joint critical-height plane, restrict to a fixed small
neighborhood of the unique complete-color maximum. Its cap angle
lies in the neighborhood of (3), so (4) subtracts \(d_0U(u)\)
from the original density exponent. The other original factors have
their complete-color upper bounds there. Away from this neighborhood,
strict joint real concavity and compactness give a positive loss
relative to \(\Re S_1(y,0)\), uniformly over either output set.
The remaining preparation currents have the original absolute upper
rate \(1.9107\). Hence the same exact decomposition gives
\[
 |F_{1,N}(y,u)|\le CN^q
 \{e^{N[\Re S_1(y,0)-d_1U(u)]}+e^{1.9107N}\},
                         \qquad d_1>0,
 \tag{5}
\]
on the disk and on the real interval. Here choose \(2d_1\)
below the uniform noncritical horizontal gap, and \(d_1\le d_0\).
The absolute plateau in (5) is not silently assigned a boundary loss.

On the true disk the quantified action satisfies
\(\Re S_1>1.910725\). Decreasing \(d\) until \(2d<.000025\)
absorbs the plateau into the first line of (2).
For the full real period, use the complete real phase comparison
\[
 \Re S_1(x_h+t,0)\le M_1+.0113|t|-4.65t^2
                      \qquad (|t|\le.02).
 \tag{6}
\]
It is bounded above by the capped exponent in the third line of (2),
as in Corollary 4 of the wider real preparation. That capped exponent
is greater than \(1.911268\) everywhere. Its gaps over the plateau
\(1.9107\) and over the actual far-arc bound \(1.91115\) are
positive. The latter far-arc proof uses the same uniform real-outside
cap estimates just listed, so it remains valid for all \(u\).
Taking \(2d\) below these gaps proves the third line of (2).

Finally, (1) has ordinary outside degree at most \(N-1\).
The elementary Laurent majorant from Section 4 below extends each
proved real bound with a linear \(O(|\Im u|)\) cost. On ordinary
color circles of radius \(N^{-2}\), inverse cosine changes the angle
by \(O(N^{-1})\), including its two ramification points. Cauchy's
formula therefore gives the stated fixed ordinary derivatives with
only polynomial cost. \(\square\)

## 2. The actual entrance has both boundary-deficit bounds

Use the larger source constants and phases from
[the full propagation theorem](research_three_larger_source_propagation.md),
and write
\[
 \mathcal U=\{|z|\le.005\}\cup[-.009,.009],\qquad
 H_0=.0057,\quad A=29/20,\quad K=|k_0|,\quad
 v(t)=\min\{d_{\mathbb T}(t,0),.03\}.
 \tag{7}
\]

**Lemma 2.** The original entrance
\(F_{0,N}(y,u)=v(-2\cos u)^TA_N^3h(y)\), with complete-color
phase \(S_0\) and center \(M_0\), satisfies for some \(d>0\)
\[
 \begin{split}
 |F_{0,N}(x_h+z,u)|
   &\le CN^q e^{N[\Re S_0(x_h+z,0)-dU(u)]},&&z\in\mathcal U,\\
 |F_{0,N}(x_h+t,u)|
   &\le CN^q e^{N[M_0+KH_0v(t)-Av(t)^2-dU(u)]},&&t\in\mathbb R.
 \end{split}
 \tag{8}
\]
The bounds include all real outside angles, all fixed ordinary outside
derivatives and both level parities.

*Proof.* Repeat the already proved actual
[disk entrance](research_three_first_entrance_source.md) and
[real entrance](research_three_first_entrance_real_extension.md)
with Lemma 1 in place of their complete-color input upper bounds.
Their central V contour is inside the incoming disk. The first
line of (2) therefore supplies \(-dU(u)\) on that entire contour,
while the retained kernel is independent of \(u\). The maximum
is the already selected complete-color critical action \(S_0\).

On the real input intervals, the principal upper term in the second
line of (2) has the same boundary deficit. Its absolute plateau has
no deficit, but the entrance proofs retain a strict gap for that
plateau relative to the complete outgoing phase on the entire output
union. Their far-input and corner errors likewise have strict gaps
and are uniform in real outside color. Decrease \(d\) so that
\(2d\) is smaller than the minimum of these fixed gaps. This proves
the first line of (8) using the literal full integral, not a formal
continuation in the outside angle.

For the global real envelope use the third line of (2) and the
two-wire real retained bound in the entrance proof. Completing the
input square gives exactly its former upper exponent
\[
 M_0+B_2-(3/2)v(t)^2-dU(u),\qquad
 B_2=.000066+\frac{(.0113)^2}{4(29/20+3/2)}<.000077.
 \tag{9}
\]
For \(v(t)\ge R\), the proved comparison
\(B_2<KH_0v(t)+(1/20)v(t)^2\) resets this to the second line
of (8). For \(|t|\le R\), use the first line of (8) and the
complete outgoing phase curvature. The undeleted three-vertex
corner error is uniform in real outside color, has rate below
\(2.38\), and has a strict gap from both desired complete upper
profiles. Reduce \(d\) once more to absorb it. This restores the
literal entrance in the statement. Ordinary derivatives follow by
the same polynomial argument as in Lemma 1. \(\square\)

## 3. Propagation of the boundary deficit and the local outside packet

**Theorem 3.** For every fixed \(j\ge0\), the original retained
word
\[
 F_{j,N}(y,u)=v(-2\cos u)^TA_N^3\widetilde A_N^{\,j}h(y)
 \tag{10}
\]
satisfies (8), with its actual complete-color phase \(S_j\),
\(M_j=\Re S_j(x_h,0)\), and \(H_j=Z^jH_0\).
One positive \(d\) from Lemma 2 works for all these fixed steps;
the polynomial constants may depend on \(j\). Moreover its nonzero
packet is genuinely holomorphic on a fixed neighborhood of
\((x_h+\mathcal U)\times\{\zeta=-2\}\), for each fixed \(j\),
with all fixed ordinary derivatives.

*Proof of the real-outside bounds.* Use the complete-color contours
of the full propagation theorem. On the central V contour, the first
bound (8) for the incoming source and the actual retained-kernel packet
give the complete combined phase minus \(dU(u)\). Its maximum is
exactly \(\Re S_{j+1}(y,0)\). No outside critical point is needed
for this upper bound. On every real complementary input interval,
the second bound (8) gives the same deficit, while the proved
complete-color comparisons give their original strict gaps.
Thus the first bound (8) is preserved. For the whole real output,
the exact square completion and reset in the propagation theorem
likewise retain \(-dU(u)\). The small-output part uses the first
bound and the complete phase curvature, as before. This proves both
bounds without adding a new action-normalization cost to the deficit.

*Proof of the local outside packet.* The entrance has its proved
holomorphic packet on a fixed ordinary outside neighborhood. Suppose
the same is known at stage \(j\). Both bounds (8) concern actual
polynomials of outside degree at most \(N-1\), uniformly on their
internal domains. Their Laurent majorant gives the same complete
profiles with at most \((1+d)|\Im u|\) added to the rate.
Every complete-source complementary gap is uniformly positive.
Consequently, for a sufficiently small fixed complex outside angle,
these bounds still place all complementary integrals below the
continued critical action; that action differs continuously from
the complete one on the compact output union. The central incoming
packet is available on its ordinary outside neighborhood by the
inductive hypothesis. Its nondegenerate critical wire and the
original amplitude continue holomorphically. Parameter stationary
phase supplies the nonzero outgoing packet with the same original
power and carrier.

This proves an actual off-color packet, rather than deducing one
from complete-point jets. For any fixed number of steps the outside
neighborhood is shrunk finitely many times. Evenness in \(u\) gives
ordinary-color holomorphy at the complete ramification point.
The original finite integrals and Cauchy estimates retain all fixed
ordinary derivatives. \(\square\)

## 4. Closing the original boundary source and its quadratic strip

Consider any fixed pair of propagated caps for which the proved
complete-color bilinear closing argument applies. The
[larger closing theorem](research_three_larger_source_closure.md)
supplies such a closing for every fixed \(m\ge6\): close the
original three-vertex entrance against its \(j=m-6\) attachments.
For \(j=0\), use the sharper two-entrance product bound (9), which
already carries both boundary deficits; for \(j\ge1\), the two
standard envelopes in Theorem 3 satisfy the unequal-preparation
criterion. Apply the closing theorem's
same central contour and complementary estimates to the two bounds
of Theorem 3. The outside factors simply multiply. The resulting
retained word therefore satisfies
\[
 |\widetilde Z_{m,N}(u,v)|\le CN^q
 e^{N[M_m-d\{U(u)+U(v)\}]},\qquad
 M_m=\Re\Xi_m(0,0).
 \tag{11}
\]
It also has its nonzero local holomorphic two-outside packet by
Theorem 3 and parameter stationary phase in the same closing
contour. The independent marked action calibration identifies
\(2\pi M_m\) with the original partial-filling volume.

The original two-ordinary-boundary corner transfer has a uniform
real-color gap \(31/600\) from \(M_m\). Since
\(U(u)+U(v)\le4\), decreasing \(d\) until \(4d<31/600\)
restores exactly
\[
                   Z_{m,N}(u,v)=v(-2\cos u)^TA_N^m v(-2\cos v)
 \tag{12}
\]
with the same nonzero packet and the real bound (11). This retains
both ordinary boundaries; neither has been replaced by a Fourier
endpoint. Its degree in each ordinary color is at most \(N-1\).

Here is the promised complexification argument. If an even outside
polynomial \(P_N(u)\) of angular degree at most \(N-1\) satisfies
\(|P_N(u)|\le CN^q e^{N[B-d(1-\cos u)]}\) on the real circle,
put \(q=e^{iu}\) and multiply \(q^{N-1}P_N\) by
\(e^{-Ndq}\). The maximum principle in the disk, and evenness
for the other height sign, give
\[
 |P_N(u+iv)|\le CN^q
 e^{N[B-d(1-\cos u)+(1+d)|v|]}.
 \tag{13}
\]
This applies also when the complete upper profile \(B\) depends
on an internal Fourier variable, since it is constant in the outside
variable. For two outside variables, apply it successively using
their separate degrees and evenness.

Away from a fixed small real neighborhood of \((0,0)\), choose
a sufficiently thin fixed complex strip so that the linear height
costs from (13) are absorbed by half the real loss in (11). Near
\((0,0)\), use the actual nonzero holomorphic packet just proved.
Taking its exponential rate in (11) and using separate evenness gives
\[
 \nabla\Xi_m(0,0)=0,\qquad
                 -\Re\Xi_m''(0,0)\succeq dI_2.
 \tag{14}
\]
Holomorphic Taylor expansion and Young's inequality for the mixed
real-height terms then give constants \(c_m,B_m,h_m>0\) such that
\[
 |\partial_{\zeta_1}^{a}\partial_{\zeta_2}^{b}
 Z_{m,N}(u+iv,r+is)|
 \le C_{a,b}N^{q_{a,b}}
 e^{N[M_m-c_m\{1-\cos u+1-\cos r\}+B_m(v^2+s^2)]},
 \quad |v|,|s|\le h_m.
 \tag{15}
\]
Ordinary derivatives follow on color circles of radius \(O(N^{-2})\)
as above, and include both ramified real endpoints. The same derivatives
have the real bound (11), after a harmless reduction of its constant.
This is the whole-boundary and quadratic-strip input of
[componentwise short-filling stability](research_componentwise_short_filling_stability.md#2-why-the-component-results-can-be-assembled).
It does not itself re-identify any marked tangle, assignment fiber or
original knot closure.

## 5. Reproduction and scope of the finite check

Run

```sh
python3 experiments/check_three_chain_outside_boundary_decay.py --precision 192
```

The [checker](../experiments/check_three_chain_outside_boundary_decay.py)
and [record](../repro/results/research-three-chain-outside-boundary-decay.json)
verify the critical-cap domain inclusion, the rational preparation
reserves, and record the exact
dependencies. They do not numerically establish the compactness
loss \(d\), redo the source contour certificates, or replace the
written term-by-term source argument above.
