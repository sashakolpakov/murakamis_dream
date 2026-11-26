# Low, plateau and right coordinates on the periodic hybrid

Research theorem, 5 November 2026. This extends the hybrid low/plateau
estimate to include the closed right half-period. It uses the same
periodic contour, all original selected terms and the original finite
source. The two open transition intervals remain outside the result.

## 1. Regions and a fixed exact contour

Put
\[
 L=[0,1/10],\qquad P=[11/50,9/20],\qquad R=[1/2,1],
 \qquad W_m=(L\cup P\cup R)^m.
 \tag{1}
\]
Fix the periodic graph of
[the split-cutoff hybrid](research_mixed_split_cutoff_hybrid_contour.md)
for each original selected subset. Choose its positive collar width
\(\varepsilon\), independently of \(N\), exactly as in the
[hybrid low/plateau theorem](research_mixed_hybrid_low_plateau_clusters.md),
Section 1: it is at most \(1/1000\) and lies inside the uniform
endpoint-thickening radius. Thus a seam-incident original block has
the fixed finite endpoint gap used in that proof.

Use the disjoint low sets
\[
 S=\{j:0\le x_j\le\varepsilon\},\qquad
 D=\{j:\varepsilon<x_j\le1/10\}.
 \tag{2}
\]
Every low coordinate is real. A deep-low coordinate in \(D\)
resets both neighboring heights completely. A seam coordinate in
\(S\) can leave a neighbor at any fraction of its prescribed height.
Every right coordinate is real because its own right profile is zero.
Its left cutoff is one, so a right neighbor does not reset a plateau
height on this hybrid.

Consequently a plateau height is affected precisely when there is
an adjacent low incidence. An unaffected plateau height is its
prescribed reference height, or \(H=7/500\) when selected. An
affected one is an arbitrary fraction of that prescribed height.
The endpoint of a low incidence may actually remain at its prescribed
height at the seam; still calling it affected only overestimates costs.

Let \(B_{e,N}\) denote the original allocated block modulus, and
\(\Gamma_e\) its full complex geometric tangent. Let \(M\) be
the real part of the original cyclic critical action. Original
stationarity, with all repeated incidences retained, gives
\[
                         \Re\sum_e\Gamma_e=M.
 \tag{3}
\]

## 2. A real low argument beside a real right argument

The following source consequence is needed independently of any
previously prescribed taper graph.

**Lemma 1.** If one argument is real in \([0,1/10]\) and the other
is real in \([1/2,1]\), the complete original allocated block has
finite upper rate
\[
                              \Re\Gamma_e-1/2000.
 \tag{4}
\]
This is uniform through zero, at both parities and for every allowed
selected indicator. The actual Fourier polynomials remain in the bound;
only their selected frequency monomials have unit modulus.

Here is a proof from the underlying complete source profiles. Write
the right angle as \(x\), the other angle as \(y\), and its height
as \(h=0\). Retain the original raw row envelope and both tangent
slopes. The inherited actual-reference slope bounds are
\(-1/5<\Re\Phi_a,\Re\Phi_b<1/4\), as recorded in the
[geometric slope theorem](research_mixed_geometric_support_slopes.md).
The
[right-angle source reduction](research_mixed_right_half_source_reduction.md)
bounds the defect by its right-angle endpoints \(x=1/2\) and
\(x=1\), including the possible extra low-row angular candidate.
At \(x=1\), the full
[all-endpoint theorem](research_mixed_all_endpoint_support.md) and its
[remaining orientation](research_mixed_43_endpoint_support.md) apply
at the original height zero and give (4).

At \(x=1/2\), the small-angle low-row reduction moves the other
angle to \(y=.13\), at the same height zero, after the required
row adjustment. The
[small-angle high-row theorem](research_mixed_small_angle_high_rows.md)
handles every upper row \(u\ge1/2\) at \(0\le y\le.13\),
again at exactly the same height; its hypothesis is
\(|h|\le.03\), which includes zero without a graph relation.
Its endpoint is \((u,y)=(.5,.13)\).

The complete [right-core source certificate](research_mixed_right_core_support.md)
explicitly contains the degenerate angle profile \(y=.13\) at
\(h=0\) for each type-four moving orientation, both unselected
and selected. Type-three profiles cover the entire height interval
\([-.03,.02]\), which also contains zero. Their strict core
support gap is \(1/500\); the proved source passage leaves finite
gap \(1/1000\). Thus all original low and high rows at \(x=1/2\)
have a stronger bound than (4). None of these reductions replaces
the height at \(y=.13\) by a taper height there. The literal
zero-height profile is the input.

The product estimates are uniform through all product zeros. The
true Fourier bounds at both real seams retain the downward forcing
recurrence and the initial value; they give zero upper seam rate
with arbitrarily small fixed tolerance. On the low half, the same
absolute comparison has rate \(-J(y)\) plus that tolerance, as
proved in [the closed low/right source argument](research_mixed_low_plateau_right_clusters.md),
Section 2. Thus no relative-factorial approximation at \(y=0\),
no level-dependent cutoff, and no deleted top row is used. Combining
the two right-angle endpoints proves (4). This proof uses the actual
saved profiles and their source reductions; it does not quote the
old right-block theorem at targets outside its stated taper graph.

## 3. Complete block classification on the hybrid

First let \(E(S)\) be the original edges incident to seam vertices.
The half-pair allocation of the hybrid low/plateau theorem remains
valid with arbitrary neighboring right angles: the
[seam-pair source](research_mixed_hybrid_zero_pair_support.md)
allows all neighboring real angles and their full physical height
bands. It gives total loss at least
\[
                                |S|/10
 \tag{5}
\]
on \(E(S)\), before any other block is used. The unused endpoint
loss and the nonnegative reserved \(Q\) are dropped. No exterior
interpretation of \(Q\) is needed.

Every remaining low-incident edge is \(DP\), \(PD\), \(DD\),
\(DR\), or \(RD\). The first two have both heights zero and
finite loss \(1/20\) from the
[uniform real low-source theorem](research_mixed_uniform_real_low_support.md).
The closed both-low raw source gives loss \(1/100\) on \(DD\).
Lemma 1 gives loss \(1/2000\) on \(DR\) or \(RD\).
An edge between \(D\) and \(S\) was already consumed by (5).

For a \(PP\) edge use the common partial-height bound from the
hybrid low/plateau theorem:
\[
 B_{e,N}\le C_\tau N^A
  \exp N\left\{\Re\Gamma_e+
        10\sum_{j\in A_e}(\Im r_j)^2+\tau\right\},
 \tag{6}
\]
where \(A_e\) consists of affected endpoint incidences. The proof
uses the actual selected Fourier branches and successive height
convexity. It includes two partial selections and two reset endpoints.

For a \(PR\) or \(RP\) edge there are two cases. If the plateau
endpoint is unaffected, its arguments are exactly those of the
proved independent right-half graph; the original full right bound
has finite loss \(1/2000\). If the plateau endpoint is affected,
the new [partial-reset right theorem](research_mixed_partially_reset_right_support.md)
applies, with the finite upper defect
\[
                                    1/100.
 \tag{7}
\]
Both selections at the real right coordinate and all partial selected
plateau heights are included in that theorem. It is a whole finite
row bound, not an off-grid saddle assertion at the right coordinate.
Finally, every \(RR\) edge has two real arguments and the complete
two-right bound has finite loss \(1/100\).

All statements in this classification concern the original allocated
moduli. The finite upper ceiling (7) already includes its Fourier
tolerance. It is not assigned another tolerance during assembly.

## 4. One charge per low-to-plateau incidence

Put
\[
                           a=10(.057)^2=3249/100000.
 \tag{8}
\]
At a plateau vertex with \(k\ge1\) low incidences, there are
\(2-k\le k\) remaining incidences. A remaining \(PP\) incidence
costs at most \(a\) for this endpoint in (6). A remaining \(PR\)
incidence costs at most \(1/100<a\) for the entire block in (7).
The latter edge has only one plateau endpoint, so its ceiling is
charged only here.

Assign each possible charge to a distinct adjacent low incidence.
If \(k=1\), there is at most one remaining edge and the assignment
is unique. If \(k=2\), there is no remaining edge and no charge.
The two endpoint costs of a doubly affected \(PP\) edge are assigned
separately, once at each endpoint. No charge is assigned through a
right vertex, whose height remains zero regardless of its neighbors.

Let \(n_{SP},n_{DP},n_{DD},n_{DR}\) count original edges of the
indicated types, combining both orientations. The total positive
block defect is bounded by
\[
                            a(n_{SP}+n_{DP}).
 \tag{9}
\]
As before, \(n_{SP}\le2|S|\). Discarding the strict losses of
unchanged \(PR\) and \(RR\) edges, the remaining loss is at least
\[
 \frac{1751}{50000}|S|+
 \frac{1751}{100000}n_{DP}+
 \frac1{100}n_{DD}+
 \frac1{2000}n_{DR}.
 \tag{10}
\]

If any low vertex is present, (10) is at least \(1/1000\).
Indeed this is immediate if \(S\ne\varnothing\), \(n_{DP}>0\),
or \(n_{DD}>0\). In the remaining case every low vertex is in
\(D\) and both its incidences go to \(R\). Hence
\(n_{DR}=2|D|\ge2\). This degree-two identity includes parallel
edges in a two-cycle. A one-cycle with a low vertex instead has
one \(DD\) loop or the seam loop already treated in (5), so it
does not enter this remaining case.

Choose one tolerance \(0<\tau_m<1/(2000m)\) in (6). At most
\(m\) plateau blocks consume it, with total less than \(1/2000\).
Every other bound was already a finite-source inequality and is used
at its stated finite gap or ceiling. Thus (10) retains the uniform
finite loss \(1/2000\).

## 5. Original restricted contribution

**Theorem 1.** For every fixed finite cyclic three/four word, all
original selections on the periodic hybrid obey
\[
 \sum_{S_0}\int_{W_m\setminus(P\cup R)^m}
   |\mathcal D_{N,S_0}(x)\det(I+iD\mathcal H_{S_0}(x))|\,dx
             \le C_mN^{A_m}e^{N(M-1/2000)}.
 \tag{11}
\]
The estimate is uniform through all zero angles and includes both
integer-level parities. The finite set of selections and regions,
the fixed-collar graph Jacobian and the original scalar powers of
\(N\) cost only polynomial factors. The original unit carrier has
modulus one. The complex tangent terms cancel exactly by (3), and
the allocated half-moduli restore the original integer weights.

The fractional seam proof uses a loop twice before taking its
half-power. The incidence proof assigns no further edge to a plateau
vertex in a mixed two-cycle. Thus (11) includes lengths one and two,
without a four-distinct-edge assumption or a duplicated source factor.

**Corollary 2.** The sum of the original selected integrals restricted
to \(W_m\) has the same central coefficient, action, unit carrier
and cyclic power \(N^0\) as the unselected plateau integral.
One may retain the conservative error rate
\[
 \mathcal Z_N^{\rm hyb}(W_m)
       =\mathcal I_{N,\varnothing}(P^m)
            +O\!\left(N^A e^{N(M-1/160000)}\right).
 \tag{12}
\]
On the low-absent boxes \((P\cup R)^m\), the hybrid is literally
the independent right graph. The pointwise block classification and
global tolerance in Section 5 of
[the complete selected right-taper theorem](research_mixed_selected_right_taper_support.md)
give absolute bounds on each such box outside the unselected plateau.
Those bounds may therefore be restricted to \((P\cup R)^m\);
this step does not infer a subregion bound from a possibly cancelling
integral over the larger region. Combine them with (11). The original
central coefficient is consequently counted once.

Configurations involving \((.1,.22)\) or \((.45,.5)\) remain
outside \(W_m\). In particular (12) is not a whole low-region or
whole-period theorem, and supplies no boundary-insertion or knot-volume
conclusion.

```sh
python3 experiments/check_mixed_hybrid_low_plateau_right_clusters.py
```

The focused checker validates the current complete source records,
the explicit zero-height core profiles, exact charge arithmetic and
the final saved source covers. The written arbitrary-length incidence
argument is not replaced by enumeration of finite words.
