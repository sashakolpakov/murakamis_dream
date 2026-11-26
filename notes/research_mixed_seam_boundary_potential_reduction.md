# Exact seam interfaces for the common incoming potential

Research reduction, 5 November 2026. This retains the original periodic
near-zero repair, its partial neighboring heights, and every selected
Fourier factor. It gives explicit sufficient boundary inequalities.
Their signs are not proved here. No plateau reset estimate is applied
to a transition coordinate.

## 1. Fixed collar and the enlarged half-period state space

Use the exact [hybrid graph](research_mixed_split_cutoff_hybrid_contour.md).
Fix its width \(0<\rho\le1/1000\) small enough that the original
[endpoint theorem](research_mixed_all_endpoint_support.md), including
[its remaining orientation](research_mixed_43_endpoint_support.md),
has finite raw gap
\[
                         d_s=1/4000
 \tag{1}
\]
whenever one target is real in \([0,\rho]\). The other target may
have any real angle and its full physical typed height band. The
fixed positive radius exists by the proved raw endpoint thickening.
It is independent of \(N\); it is not asserted to equal \(1/1000\).

In this note the other coordinates lie in the closed half-period.
For counting, use the disjoint sets
\[
 S=\{j:0\le x_j\le\rho\},\qquad
 A=\{j:\rho<x_j\le1/2\}.
 \tag{2}
\]
For auxiliary paths use the compact alphabet
\(\mathcal A_\rho=[\rho,1/2]\), with the original permitted
selections. The target, phase, plane and weight \(w_j\) are exactly
those of the [open-chain construction](research_mixed_nonlow_open_chain_boundary.md),
now restricted to this enlarged alphabet. Edge \(j\) joins vertices
\(j-1,j\).
In particular the left cutoff on this alphabet is
\[
 L_b(x)=\begin{cases}
 0,&\rho\le x\le .1,\\
 (x-.1)/(b-.1),&.1\le x\le b,\\
 1,&b\le x\le .5.
 \end{cases}
\]
It is the zero extension supplied by the hybrid contour. The linear
formula on \([.1,b]\) is not extended below .1. On the physical seam
\([0,\rho]\), the same contour instead uses \(L_b(x)=1-x/\rho\).

These weights have complete source branches on their actual target
sets. If a block has a deep-low endpoint in \([\rho,.1]\), both
targets are real, because that endpoint resets its neighbors. Use
the full real [half-endpoint packet](research_mixed_half_endpoint_conditional_packet.md)
on \([\rho,.5]^2\). Other blocks have their targets in the established
nonlow source products, including zero heights caused by a deep-low
halo. The original branches agree on overlaps. Compactness gives
finite local bounds \(K_{\rho,\theta}\) and \(L_{\rho,\theta}\),
uniform over types, actual references and word lengths, though they
may depend on \(\rho\).

Let \(\omega_j\) be the occupation penalty with coefficient \(1/4000\),
and fix \(0<\theta<1\). Set
\[
 t_j^\theta=w_j+\frac{\theta}{2}(\omega_{j-1}+\omega_j).
 \tag{3}
\]
The [deep-low half-region theorem](research_mixed_deep_low_half_region.md)
proves the original pointwise cyclic inequality on this alphabet.
Thus
\[
 \sum_jt_j^\theta\le-(1-\theta)\sum_j\omega_j.
 \tag{4}
\]
The same inequality holds for every integer repetition of the original
word with its repeated actual reference.

Let \(H_{\rho,\theta}\) be the incoming supremum from baseline at
layer zero, and \(A_{\rho,\theta,i}^{[h]}\) its length-\(h\) version.
The proof of the [finite-depth theorem](research_mixed_finite_depth_boundary_potential.md)
applies to this alphabet. All good symbols still lie in the original
plateau, so its quadratic estimate is unchanged: for \(0<d\le1/40\),
\[
 \begin{split}
 B_{\rho,d}&=\frac{10(6K_{\rho,\theta}+1)}
                    {(1-\theta)d^2},\\
 h&=5(\lfloor B_{\rho,d}\rfloor+1)+3,\qquad
 0\le H_{\rho,\theta}-A_{\rho,\theta}^{[h]}\le40d^2.
 \end{split}
 \tag{5}
\]
This is the same construction and the same reference, not an assumption
that allowing additional incoming paths leaves their supremum unchanged.
The following stronger equality establishes exactly when it does.

The [relative finite-depth estimate](research_mixed_finite_depth_subaction.md)
also applies on this enlarged alphabet. For clarity, define
\[
 \Psi_i(v)=\omega_{i-2}+\omega_{i-1}+\omega_i,\quad
 C_{\rho,\theta}=\max\{200,24000K_{\rho,\theta}\},\quad
 h=5\left(\left\lfloor
       \frac{2400(C_{\rho,\theta}+1)}{(1-\theta)\theta}
                     \right\rfloor+1\right)+3.
 \tag{5a}
\]
Then, with the original layer alignment,
\[
 \begin{split}
 V_{\rho,i}(v)&=A_{\rho,\theta,i}^{[h]}(v)
                   +\theta\left(\frac{\omega_{i-1}}6
                                      +\frac{\omega_i}3\right),\\
 w_i(v,v')&\le V_{\rho,i+1}(v')-V_{\rho,i}(v)
                                      -\frac\theta6\Psi_{i+1}(v').
 \end{split}
 \tag{5b}
\]
Here is why enlarging the alphabet preserves that proof. If
\(\Psi_i<1/4000\), all three symbols lie in the old unselected
plateau, where the three-step entry and exit costs obey the same
quadratic bound \(-A^{[3]}-E^{[3]}\le200\Psi_i\).
For \(\Psi_i\ge1/4000\), their sum is at most
\(6K_{\rho,\theta}\le24000K_{\rho,\theta}\Psi_i\).
The cyclic occupation inequality (4) and the five-symbol quadratic
cut therefore prove the relative error bound with the same constants.
The gauge in (5b) changes the allocated occupation to one third of
the output triple; choosing relative error \(\theta/6\) gives
(5a)--(5b). No new estimate at a deep-low symbol is required in the
quadratic part of this argument.

## 2. Deep internal histories give no extra incoming value

Write \(H_\theta,A_{\theta,i}^{[h]}\) for the old alphabet
\(\mathcal A_0=[.1,.5]\).

**Lemma 1.** If the terminal triple belongs to \(\mathcal A_0\), then
\[
 A_{\rho,\theta,i}^{[h]}(v)=A_{\theta,i}^{[h]}(v)
       \quad(h\ge3),\qquad H_{\rho,\theta}(v)=H_\theta(v).
 \tag{6}
\]

**Proof.** In any incoming path of length \(h\), only the final three
appended symbols are prescribed. Raise every free appended coordinate
below .1 to .1, preserving its selection. Throughout this motion every
left cutoff at that coordinate remains zero. Its own and both neighboring
heights are therefore unchanged and zero; all other heights are unchanged.

If the terminal layer is \(i\), a free appended coordinate has index
\(k\le i-3\). Both original edges \(k,k+1\), in which it is an
endpoint, occur in the path. Their original action derivatives are
strictly positive by the real-low derivative lemma in the deep-low
theorem. The arguments of both blocks are real. The two tangent
derivatives cancel exactly by actual cyclic criticality:
\[
                  \phi_{k,b}(r)+\phi_{k+1,a}(r)=0.
 \tag{7}
\]
Other appearances are only as halos and change no target height.
The selected correction at a real low coordinate is zero, and its
occupation is unchanged. Thus the total \(t^\theta\)-weight does
not decrease.

If the terminal triple is in the old alphabet, the raised path lies
entirely there and has the same length and prescribed states. The
reverse inequality follows from inclusion of path sets, proving the
finite equality. Baseline padding permits restriction to lengths at
least three in the incoming supremum and proves the second equality.
This keeps the original layer alignment and all repeated incidences.
\(\square\)

At the same finite depth \(h\), (6) also identifies the functions
\(V_{\rho,i}\) and \(V_i\) on every old terminal triple, since
their added occupation terms are identical. This comparison uses the
same depth, not separately chosen truncations on the two alphabets.

For a terminal triple with prescribed deep-low symbols, the same raising
removes all *free* internal deep lows. Only that final triple remains.
Let \(T_{\rho,\theta}^{[3]}(u,v)\) be the literal three-transition
weight obtained by appending \(v\) to a triple \(u\) at layer \(i-3\).
Consequently
\[
 \begin{split}
 H_{\rho,\theta}(v)
   &=\sup_{u\in\mathcal A_0^3}
        \{H_\theta(u)+T_{\rho,\theta}^{[3]}(u,v)\},\\
 A_{\rho,\theta,i}^{[h]}(v)
   &=\max_{u\in\mathcal A_0^3}
        \{A_{\theta,i-3}^{[h-3]}(u)
                        +T_{\rho,\theta}^{[3]}(u,v)\},\quad h\ge6 .
 \end{split}
 \tag{8}
\]
Types and allowed selections are fixed at their layers in these
suprema. Near-optimal incoming paths justify the first equality;
no attainment of \(H_\theta\) is required. Equation (8) is a finite
terminal extension, not a new gain hidden in an arbitrarily long
deep-low history.

## 3. Exact virtual halos for the physical seam attenuation

For a seam coordinate \(s\in S\), put
\[
 \lambda_s=1-x_s/\rho,\qquad
 \xi(s;j)=.1+(b_j-.1)\lambda_s,\qquad
 b_j=\begin{cases}.22,&\sigma_j=0,\\ .12,&\sigma_j=1.\end{cases}
 \tag{9}
\]
The symbol at \(\xi(s;j)\) has the original type at position \(s\)
and virtual selection zero. It belongs to \(\mathcal A_0\), and
\[
                        L_{b_j}(\xi(s;j))=\lambda_s=L_{b_j}(x_s).
 \tag{10}
\]
The cutoff is chosen by the adjacent row \(j\), not by the seam type.

Let \(I=[l,r]\) be a maximal nonempty A-run in a mixed cycle.
Replace its left seam halo by \(\xi(l-1;l)\), and its right seam
halo by \(\xi(r+1;r)\). All physical AA target heights, hence all
their original weights, remain exactly unchanged by (10). The two
virtual values need not agree even if they represent copies of the
same physical seam coordinate: different endpoint selections can
choose different slow or fast cutoffs. They are independent symbols
of the auxiliary path, not a change in the original integral.

For a run of length at least two, its initial and final states are
\[
 v_I^-=(\xi(l-1;l),q_l,q_{l+1}),\qquad
 v_I^+=(q_{r-1},q_r,\xi(r+1;r)),
 \tag{11}
\]
at layers \(l+1\) and \(r+1\). A singleton has the same state at
both ends, \((\xi(l-1;l),q_l,\xi(l+1;l))\), and no AA edge.
Define
\[
 \Omega_I=\sum_{j=l}^r\omega_j-\frac{\omega_l+\omega_r}{2}\ge0.
 \quad\text{Then}\quad
 \sum_{j=l+1}^{r}w_j
 \le H_{\rho,\theta}(v_I^+)-H_{\rho,\theta}(v_I^-)-\theta\Omega_I.
 \tag{12}
\]
If the first two and last two run symbols are in \([.1,.5]\),
all symbols in the two boundary triples (11) are in the old alphabet.
For a singleton only its one physical symbol is needed. The potentials
in (12) are then exactly the old \(H_\theta\), by (6). Any prescribed
deep symbol in a boundary triple is handled by (8). No height convexity
or exterior reset bound is needed.

## 4. Raw pair allocation and the exact remaining comparison

Let \(E(S)\) be the original edges incident to \(S\). The
[complete seam-pair theorem](research_mixed_hybrid_zero_pair_support.md)
gives, at every seam vertex \(s\),
\[
 \mathcal B_{s,N}\mathcal B_{s+1,N}
 \le C N^A
 \exp N\{\Re(\Gamma_s+\Gamma_{s+1})-G-Q_s\},
\quad G=7/25,
 \quad Q_s=\frac{151}{20}(\Im r_{s-1})^2
                         +\frac{11}{2}(\Im r_{s+1})^2.
 \tag{13}
\]
This holds for the raw row sums as well as the coherent moduli,
with every actual Fourier halfweight and selection retained.
Here \(Q_s\) is only a reserved positive quantity. It is not
identified with an exterior cost on transition or deep-low blocks.

The constant in (13) is an extraction from the completed certificate,
stronger than its previously stated \(1/5\). Here are the details
needed to use it. For each complete reference cell, the original
checker forms the geometric gap after subtracting \(Q_s\), applies
the full-cell mean-value error, and takes the minimum of the sixteen
outward lower endpoints at the target corners. It then takes the
minimum over every accepted cell and reference product. Both the
256-bit author record and its saved 320-bit replay have all 2,048
reference products and 18,988 cells; all recorded minima exceed
\(303/1000\). Their global lower bounds exceed .30347868248 and
.30347868250, respectively. The original acceptance threshold was
only \(1/4\), but these stronger whole-cell lower endpoints were
already computed and saved. They are not midpoint samples.

The same separate maximum principles in the original proof therefore
give geometric gap greater than \(303/1000\), with the same reserved
\(Q_s\). Its established collar cost on \([0,1/1000]\) is less
than \(1/50\). Choose the total Fourier tolerance for the two raw
blocks below \(3/1000\), once. The resulting complete finite pair
has gap greater than
\[
             \frac{303}{1000}-\frac1{50}-\frac3{1000}
                               =\frac7{25}.
\]
This derives (13) from the underlying source estimates. It does not
spend another tolerance on the earlier rounded finite bound. Every
selection, row, original normalization and both level parities remain
in the two raw blocks. The focused checker below validates both
current records, all case keys and complete covers, and their saved
minima. No numerical cell is recomputed for this extraction.

Choose nonnegative star weights \(\alpha_s\), subject to
\[
 c_e=\sum_{\substack{s\in S\\\text{endpoint incidences of }e}}\alpha_s
                         \le1\qquad(e\in E(S)).
 \tag{14}
\]
An original loop counts its endpoint twice. Multiply (13) to the
power \(\alpha_s\), and fill each exponent \(1-c_e\) with the
direct endpoint bound (1). All factors are nonnegative; no kernel
division is used. Since \(\sum_e c_e=2\sum_s\alpha_s\), the
total raw seam loss is
\[
 \mathcal L_S(\alpha)=
 G\sum_s\alpha_s+\sum_s\alpha_sQ_s
          +d_s\left(|E(S)|-2\sum_s\alpha_s\right).
 \tag{15}
\]
In particular, an isolated seam in a mixed cycle permits
\(\alpha_s=1\): its full loss is \(G+Q_s\), not \(G/2\).
Uniform weights \(\alpha_s=1/2\) give the previously proved
overlap-safe allocation. A one-cycle seam loop permits only
\(\alpha_s\le1/2\); the half-power of its pair inequality restores
its one original block.

For every fixed word and every \(\tau>0\), combine (12) with
(15) and the complete AA source packets. Original stationarity gives
\(\Re\sum_e\Gamma_e=M\). The physical allocated product is bounded
by a fixed-word polynomial times the exponential of
\[
 M-\mathcal L_S(\alpha)
 +\sum_I\{H_{\rho,\theta}(v_I^+)-H_{\rho,\theta}(v_I^-)\}
 -\theta\sum_I\Omega_I+\tau .
 \tag{16}
\]
Only the physical AA packets spend the freely chosen total tolerance
\(\tau\). The rounded pair and endpoint bounds are already finite;
no new tolerance is charged to them or to a virtual path. The
bounded Jacobian of the fixed hybrid graph has no exponential cost.

There is an entirely finite alternative to (16). Apply (5b) to the
same virtual paths. Write \(\mathcal O_I\) for the output triples
of the actual AA edges in run \(I\); a singleton has none. The
upper exponent is
\[
 M-\mathcal L_S(\alpha)
 +\sum_I\{V_\rho(v_I^+)-V_\rho(v_I^-)\}
 -\frac\theta6\sum_I\sum_{v\in\mathcal O_I}\Psi(v)+\tau.
 \tag{16a}
\]
The output occupations include the prescribed virtual halo wherever
it occurs in that triple. They arise from the exact auxiliary path
inequality and are not additional physical factors. Formula (16a)
has no truncation error per run. Its only tolerance is the chosen
total finite-source tolerance on the physical AA blocks.

Thus the remaining seam criterion is explicit. For example, for one
isolated seam it suffices to bound
\[
 H_{\rho,\theta}(v_I^+)-H_{\rho,\theta}(v_I^-)
                   -\theta\Omega_I < G+Q_s-\eta
 \tag{17}
\]
with a uniform \(\eta>0\). When both boundary triples lie in the
old alphabet, the potential here is the established common \(H_\theta\).
Replacing it by the same incoming length-\(h\) function incurs
only one approximation error per nonsingleton A-run, as in the
finite-depth theorem. For singleton runs the values cancel exactly.
The original \(m=2\) mixed cycle has this singleton form and is
already bounded by its full seam pair. An \(m=1\) cycle is either
entirely seam or entirely half-period.

More generally, (15) can be distributed among maximal seam runs;
each adjacent A-run supplies one exit and one entrance potential.
The choices of \(\alpha_s\) may preserve the full disjoint-star
loss wherever incident edges do not overlap. This is a finite
boundary comparison with explicit original source and action
conventions, not a claim that its sign follows from \(G>0\).
In particular a coarse bound \(6K_{\rho,\theta}\) on a potential
difference has not been shown smaller than the available pair
reserve. A short incoming candidate that fails its Bellman
inequality cannot be substituted for \(H_{\rho,\theta}\) without
the proved finite-depth error.

## 5. A stronger allocation on consecutive seam runs

In a mixed cycle, let a maximal seam run have \(k\ge1\) vertices,
numbered from its left end in the original cyclic order. Give weight
one to the stars at positions \(1,3,5,\ldots\) and zero to the
other stars. These centers are not adjacent, so they share no original
edge. Different seam runs also share no original edge, even if only
one nonseam vertex separates them. Shared target variables do not
prevent multiplying the bounds: every allocated source edge still
occurs once.

For odd \(k\), the chosen \((k+1)/2\) stars cover all \(k+1\)
edges incident to the run. For even \(k\), its \(k/2\) chosen
stars cover \(k\) such edges, leaving exactly one boundary edge for
the direct endpoint bound. Consequently this run contributes at least
\[
 \gamma(k)+\sum_{s\text{ chosen}}Q_s,\qquad
 \gamma(k)=G\left\lceil\frac k2\right\rceil
                       +d_s\mathbf1_{\{k\text{ even}\}}.
 \tag{18}
\]
For even \(k\) one may instead start at the second vertex, leaving
the other boundary edge. Either choice is valid; it is not necessary
to optimize it. In particular an isolated seam retains the full
\(7/25\) loss and its full \(Q_s\).

For an entirely seam cycle, use \(\alpha_s=1/2\) in (14).
Every original edge is then covered once, and the loss is
\(Gm/2+\frac12\sum_sQ_s\). This includes the one-cycle loop
and the two parallel edges of a two-cycle. In a mixed two-cycle the
single seam vertex uses its full star, covering those two distinct
physical edges as in (18).

Summing (18) over seam runs in (16) is a valid stronger sufficient
boundary comparison. Its advantage for an odd run is a full extra
half-pair allowance, apart from the one endpoint credit it replaces.
It does not determine the signs of the accompanying potential
differences. Those still require an estimate.

No source packet at zero, plateau-only reset estimate on a transition,
whole-period asymptotic or boundary-insertion lower bound is inferred.
All completed source artifacts remain unchanged.

Reproduction:

```sh
python3 experiments/check_mixed_seam_boundary_potential_reduction.py
```

The checker verifies the virtual-cutoff and star-allocation identities,
the stronger saved pair margins and current source provenance. The
general path and finite-integral arguments are the written proofs here.
