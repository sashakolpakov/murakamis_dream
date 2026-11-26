# Choosing and repairing the boundary halos of a half-period chain

Research deduction, 5 November 2026. This describes all exact virtual
halos at a seam, removes an unnecessary restriction on the incoming
potential, and gives an explicit three-step upper bound with exact
boundary-edge corrections. Its sign remains a separate finite
comparison. Completed source estimates and their records are unchanged.

## 1. Exact halo freedom

Use the [periodic hybrid contour](research_mixed_split_cutoff_hybrid_contour.md)
and the original \(w_j,t_j^\theta,H_{\rho,\theta},A_i^{[h]},E_i^{[3]}\)
of the [seam boundary reduction](research_mixed_seam_boundary_potential_reduction.md).
Here edge \(j\) joins coordinates \(j-1,j\),
\(t_j^\theta=w_j+\theta(\omega_{j-1}+\omega_j)/2\), and
\(0<\theta<1\). Fix the permitted collar width \(\rho>0\).
The auxiliary alphabet is \({\cal A}_\rho=[\rho,.5]\), with
the original allowed selections. Its row cutoffs are
\[
 L_b(x)=\begin{cases}
 0,&\rho\le x\le .1,\\
 (x-.1)/(b-.1),&.1\le x\le b,\\
 1,&b\le x\le .5,
 \end{cases}\qquad
 b=.22\ \hbox{or}\ .12 .
 \tag{1}
\]
The row chooses \(b=.22,c=\Im r_j\) when unselected and
\(b=.12,c=.014\) when selected. For \(y\ge.1\), its right
cutoff is \(R(y)=1\) through .45 and
\(R(y)=400(.5-y)^2\) thereafter. Below .1 use the original
hybrid cutoff; its value has no effect here because \(L_b(y)=0\).

Consider one endpoint of a half-period run of length at least two.
Let \(y\) be its real coordinate, \(z\) its inner neighbor, and
\(\lambda=1-x_s/\rho\) the attenuation of its adjacent seam.
Set
\[
 m=\min\{L_b(y),L_b(z)\},\qquad
 h_{\rm physical}=cR(y)\min(m,\lambda).
 \tag{2}
\]
A virtual halo \(\xi\in{\cal A}_\rho\) reproduces this row exactly
if and only if
\[
 cR(y)\min(m,L_b(\xi))=cR(y)\min(m,\lambda).
 \tag{3}
\]
The halo may have either selection permitted by its original type.
Its selection does not enter the neighboring row's cutoff or any
physical half-period edge in the run.

**Lemma 1.** The maximal admissible real-halo set is as follows.
If \(cR(y)=0\), it is all of \({\cal A}_\rho\). Otherwise:
\[
 \begin{array}{c|c}
 \text{condition}&\text{admissible }\xi\\ \hline
 \lambda\ge m,\ m=0&[\rho,.5]\\
 \lambda\ge m,\ m>0&[.1+(b-.1)m,\ .5]\\
 \lambda<m,\ \lambda=0&[\rho,.1]\\
 0<\lambda<m&\{.1+(b-.1)\lambda\}.
 \end{array}
 \tag{4}
\]
Indeed if the physical minimum saturates at \(m\), any
\(L_b(\xi)\ge m\) works. Otherwise equality requires
\(L_b(\xi)=\lambda\). Inverting the three pieces of (1) gives
(4). This proof also covers a negative unselected \(c\): it
uses only whether \(cR(y)\) vanishes.

Every baseline symbol \(p_j=(\Re r_j,0)\) has \(L_b(p_j)=1\).
Thus baseline is admissible whenever \(\lambda\ge m\) or
\(cR(y)=0\), in particular at \(y=.5\). The older single
choice \(.1+(b-.1)\lambda\) is always admissible, but need not
be the only admissible halo.

## 2. The potential sees only the final row height

Write a terminal state at layer \(i\) as
\(v=(q_{i-2},q_{i-1},q_i)\). The last appended symbol \(q_i\)
occurs only in the last incoming transition, whose original edge is
\(i-1\). In that edge it is only the halo determining the height of
row \(i-1\). In particular its selection and its occupation do not
occur in this incoming weight.

**Lemma 2.** The functions \(H_{\rho,\theta,i}(v)\) and
\(A_i^{[h]}(v)\), \(h\ge3\), are independent of the selection of
\(q_i\). For fixed first two symbols they depend on its real
coordinate only through the resulting height of row \(i-1\).

**Proof.** Replace the last appended symbol of an incoming history.
If the row height is unchanged, every transition and its occupation
share is unchanged. This is a weight-preserving bijection of the
finite histories with the two terminal states. Histories defining
\(H\) may first be padded by whole baseline periods to have length
at least three. Take maxima or suprema. Types and layers are preserved
even at primitive periods one and two; auxiliary symbols at different
positions are not identified. \(\square\)

For clarity the one-sided dependence has the exact Bellman form
\[
 \begin{split}
 H_i(a,b,d)={}&\frac\theta2(\omega_a+\omega_b)\\
 &+\max_{p}\{H_{i-1}(p,a,b)
       +{\cal W}_{i-1}(z_a(p),z_b(d))\},
 \end{split}
 \tag{5}
\]
where \(p\) ranges over its real coordinate and permitted selection,
and
\[
 {\cal W}_j(u,v)=\Re\{\phi_j(u,v)-\Gamma_j(u,v)\}
                    +\frac{\sigma_{j-1}}2\chi(u)
                    +\frac{\sigma_j}2\chi(v).
 \tag{6}
\]
The notation suppresses fixed symbols, types and actual reference data.
The maximum in (5) exists by continuity and compactness. The infinite
incoming supremum itself need not be attained. The corresponding
finite identity replaces \(H_i,H_{i-1}\) by \(A_i^{[h]},A_{i-1}^{[h-1]}\)
for \(h\ge4\).

For a run \(I=[l,r]\) of length at least two, let
\({\cal E}_L,{\cal E}_R\) be its admissible halo sets (4), including
permitted selections. Set
\[
 v_I^-(\xi)=(\xi,q_l,q_{l+1}),\qquad
 v_I^+(\eta)=(q_{r-1},q_r,\eta),\qquad
 \Omega_I=\sum_{j=l}^r\omega_j-\frac{\omega_l+\omega_r}{2}.
 \tag{7}
\]
All \(\eta\in{\cal E}_R\) give exactly the same \(H(v_I^+(\eta))\)
by Lemma 2. All \(\xi\in{\cal E}_L\) preserve the entire future
physical run, but their incoming values need not agree. Consequently
\[
 \sum_{j=l+1}^r w_j^{\rm physical}
 \le H(v_I^+(\eta))
       -\max_{\xi\in{\cal E}_L}H(v_I^-(\xi))-\theta\Omega_I .
 \tag{8}
\]
This is stronger than insisting on one preassigned entrance halo.
Both halo optimizations are at most one-dimensional with finitely
many selection choices. They change no physical Fourier allocation.

## 3. Baseline repair with exact edge corrections

Baseline halos can also be used when (3) fails. Keep all symbols of
the physical run, replace only its two exterior halos by the
correctly phased baseline symbols, and call the resulting targets
and weights repaired. Only its first and last rows can change.
At either endpoint the signed height change is exactly
\[
 \Delta h=h_{\rm repaired}-h_{\rm physical}
                   =cR(y)(m-\lambda)_+ .
 \tag{9}
\]
No interior row changes, because its cutoff depends on real neighboring
coordinates, not on their heights.

Let \(\Delta_I\) be the sum of the physical minus repaired original
\(w\)-weights on the affected edges. If \(r-l+1\ge3\), explicitly
\[
 \begin{split}
 \Delta_I={}&
 w_{l+1}(\xi_L,q_l,q_{l+1},q_{l+2})
       -w_{l+1}(p_{l-1},q_l,q_{l+1},q_{l+2})\\
 &+w_r(q_{r-2},q_{r-1},q_r,\xi_R)
       -w_r(q_{r-2},q_{r-1},q_r,p_{r+1}),
 \end{split}
 \tag{10}
\]
where \(\xi_L,\xi_R\) can be any exact physical emulators from
(4). For a two-symbol run there is one edge, and its joint correction
is
\[
 \Delta_I=w_{l+1}(\xi_L,q_l,q_{l+1},\xi_R)
               -w_{l+1}(p_{l-1},q_l,q_{l+1},p_{l+2}).
 \tag{11}
\]
It is not the sum of two independently changed copies of that edge.
For a singleton put \(\Delta_I=0\); there is no AA edge.

Use baseline-halo states
\[
 v_I^-=(p_{l-1},q_l,q_{l+1}),\qquad
 v_I^+=(q_{r-1},q_r,p_{r+1})
 \tag{12}
\]
for a nonsingleton; for a singleton both states mean
\((p_{l-1},q_l,p_{l+1})\) at the same layer. The repaired path
is an admissible auxiliary half-period path. Thus
\[
 \sum_{j=l+1}^r w_j^{\rm physical}
 \le H(v_I^+)-H(v_I^-)-\theta\Omega_I+\Delta_I .
 \tag{13}
\]
The correction retains the full complex tangent and the actual
selected halfweights in (6). It is a difference of original phases,
not an approximation or monotonicity claim for a finite kernel.
Both the physical and repaired targets are in the proved source
products, so the physical finite source is bounded by its physical
phase before (13) is used.

There is a practical upper bound involving only three-step functions.
Write \(a=1-\theta\) and \(\Psi(v)\) for terminal triple occupation.
Closing any incoming history with its three baseline exit steps gives
\[
                         H(v)\le-E^{[3]}(v)-a\Psi(v).
 \tag{14}
\]
Indeed the cyclic \(t^\theta\)-weight is at most minus \(a\)
times its entire occupation. That occupation includes the final
three appended symbols. Pad a short history by baseline periods
before applying this argument.
Together with \(H(v)\ge A^{[3]}(v)\), (13) yields, for a
nonsingleton,
\[
 \sum_{j=l+1}^r w_j^{\rm physical}
 \le -E^{[3]}(v_I^+)-A^{[3]}(v_I^-)
            -a\Psi(v_I^+)-\theta\Omega_I+\Delta_I .
 \tag{15}
\]
Each \(A^{[3]},E^{[3]}\) is its literal three-edge function.
There is no connector optimization or asymptotic truncation error.
This is an explicit finite-variable sufficient comparison, not an
assertion that its right side is always negative. A singleton instead
retains its exact empty sum zero.

One may use the same direct bound without repairs by replacing
\(-E^{[3]}(v_I^+)\) by
\(-\max_{\eta\in{\cal E}_R}E^{[3]}(v_I^+(\eta))\), dropping
the additional term \(-a\Psi\), and replacing the entry by
\(-\max_{\xi\in{\cal E}_L}A^{[h]}(v_I^-(\xi))\).
This follows from (8), Lemma 2, and the entry/exit bounds; at \(h=3\)
there are only two one-dimensional halo maximizations.

## 4. A quantitative bound for a small repair

The exact correction (10)--(11) is preferable when its phases can
be evaluated. A uniform derivative bound gives a further useful
estimate. On the original compact nonlow source products, let
\(L_{\rm row}\) bound each vertical derivative of every branch
of (6), with references in their established typed rectangles.
For example the finite compact supremum of
\[
 |\phi_{j,k}(z)|+|\phi_{j,k}(r)|
                         +\frac12\max\{|g'(z_k)|,2\pi\},
 \qquad k\in\{1,2\},
 \tag{16}
\]
is a valid common choice. This includes the derivative of the
complex tangent. Both Fourier branches are retained: their vertical
derivatives have magnitudes at most \(|g'|\) and \(2\pi\).
The maximum of those branches is therefore Lipschitz with this
constant. Holomorphic source branches on neighborhoods of the compact
products prove finiteness and independence from the word length;
no numerical value for \(L_{\rm row}\) is asserted.

All intervening vertical segments remain in the typed source domains.
Consequently
\[
 |\Delta_I|\le L_{\rm row}
          (|\Delta h_l|+|\Delta h_r|)
 \le .057L_{\rm row}\{R(x_l)+R(x_r)\}.
 \tag{17}
\]
For a two-symbol run use two successive vertical segments of the
same edge's product domain to prove (17). A nonzero repair requires
both endpoint and inner-neighbor coordinates to exceed .1; if either
is at most .1, then \(m=0\). Thus the constant in (16) is the
fixed nonlow constant even when other run symbols belong to
\([\rho,.1]\).
If both endpoints lie in \([.45,.5]\), (17) becomes
\[
 |\Delta_I|\le\frac{114}{5}L_{\rm row}
           \{(.5-x_l)^2+(.5-x_r)^2\}.
 \tag{18}
\]
This is a quadratic boundary error with an explicitly defined
compact constant. It is not a finite-kernel comparison at modified
targets; only their proved phase upper bounds are compared.

## 5. Exact cancellation and remaining source allocation

At an endpoint of angle .5, \(R=0\), so baseline is an exact
halo and its contribution to \(\Delta_I\) is zero. If the two
baseline-halo states in (12) coincide at the same periodic layer,
their common potential cancels identically in (13).
This observation applies, for example, to the preserved alternating
reference configuration with one seam, both neighboring type-four
angles .5, equal selections on those endpoints, and their next
inner symbols equal to the corresponding type-three baselines.
Entry and exit are then the identical triple \((p_3,q_4,p_3)\)
at equal layers of the period-two reference. The old fixed virtual
halo .1 at seam attenuation zero had introduced an unnecessary
incoming-history cost. This cancellation is exact, not an inference
from numerical potential values.

For general runs combine (13) or (15) with the actual raw seam
deficits of the [source refinement](research_mixed_half_angle_seam_source.md).
The full allocated upper rate, for example using (13), is
\[
 M-{\cal L}_{\rm actual}(\alpha)
   +\sum_I\{H(v_I^+)-H(v_I^-)-\theta\Omega_I+\Delta_I\}
   +\tau .
 \tag{19}
\]
Every physical AA edge occurs once. Its phase is compared to its
repaired phase only through (10) or (11); the raw seam pair continues
to use its actual physical targets and tangent plane. Thus tangent
terms still cancel by original stationarity, each Fourier halfweight
is retained once, and no exterior debit is charged twice. The sole
additional \(\tau>0\) is the chosen total tolerance of the physical
AA source packets. The graph Jacobian has no exponential cost.

The same bookkeeping retains loops, parallel edges and repeated
reference positions. A mixed two-cycle has a singleton AA run and
no repair. A mixed three-cycle may have a two-symbol run and uses
the joint correction (11). Larger runs use the two distinct boundary
edges, including when these share an interior vertex. No general sign
for (19), full-period asymptotic, or knot-family consequence is asserted.
