# A uniform closed route in the original Pascal-cell source

29 October 2026. The exact positive angle cells of the actual divided
fusion maps have a simultaneous, source-admitted closed route at every
crossing of ANY signed braid. Its energy is exponential. In particular,
the phase-free path partition of these cells cannot itself be the sharp
geometric angle partition for the figure-eight knot. Coherent contraction
of the physical maps is essential before such a geometric comparison.

This is about the original averaged-trace presentation AFTER its
authorized whole-word degree reduction. It is not a statement about
every possible pointed presentation or a surviving coherent clock sector.

## 1. Exact physical alphabet and original source

Use N>=2, d=N-1, q=exp(pi i/N), Q=q^2, and x=-q^(-1). The exact
[physical fusion and crossing theorem](actual_reassociation_angle_kernel.md)
gives C=C'_12 and its literal inverse with entries

    C_(a-r,b+r;a,b)=x^(-r)[b+r choose r]_Q,
    C^(-1)_(a-r,b+r;a,b)
       =(-1)^r Q^(r(r-1)/2) C_(a-r,b+r;a,b),
    0<=r<=min(a,d-b).                                      (1)

Write C_21=Flip C Flip and

    D_2|a,b>=(-1)^b Q^(b(b-1)/2)x^(-2b)|a,b>.

The FULL original checked crossings are

    R_+=kappa C D_2 C_21 C^(-1),
    R_-=kappa^(-1) C C_21^(-1) D_2^(-1) C^(-1).             (2)

No physical cutoffs or common Cartan scalars have been removed. All
displayed diagonals, kappa and original closing pivots have unit modulus
at completeness. Both signs are included below with their actual order.

For the whole original knot word W, integer total-degree conservation
first gives the exact source

    K_N=chi_N/N Tr[(I tensor g tensor ... tensor g)W].         (3)

This is [the original charged-source theorem](actual_global_charged_bridge_flow.md#1-use-the-original-scalar-source-before-splitting).
It is used BEFORE expanding W into fusion paths. It is not a sectorwise
replacement of the full marked row, nor a rule for arbitrary insertions.
The original dimension/framing line chi_N remains outside (3).

The physical quarter gauge G_a=N^(1/4)/sqrt(s_a), s_a=|(Q;Q)_a|,
commutes with the closing pivots. Thus its tensor similarity preserves
(3) exactly. The squared entry of either C or C^(-1) in this gauge is

    |Chat_entry|^2=N^2 w_d(r,a-r,d-a)w_d(r,b,d-b-r),
    w_d(i,j,k)=1/(s_i s_j s_k), i+j+k=d.                     (4)

The operator C_21 has the same formula with the two physical heads
exchanged. The inverse phases in (1) remain in the coherent word.

## 2. One closed route works for all signs and all braid positions

Put N=3r+1, d=3r, r>=1, and choose the PHYSICAL initial trace state

    a_star=(2r,r,2r,r,...).                                  (5)

Every adjacent pair is either (2r,r) or (r,2r). At each crossing use
the following transfers, listed in operator ACTION order:

| input pair | right C^(-1) | middle C_21 or C_21^(-1) | left C | output pair |
| --- | --- | --- | --- | --- |
| (2r,r) | r | r | 0 | (2r,r) |
| (r,2r) | 0 | r | r | (r,2r) |

For a negative crossing its D_2^(-1) is between the right and middle
maps; for a positive crossing D_2 is between the middle and left maps.
It is diagonal and never changes this route or its nonzero modulus.
Each intermediate pair is (2r,r) or (r,2r), so all physical bounds
in (1) hold as ORDINARY integers. Inverse maps have exactly the same
support and modulus as the forward maps.

Each row therefore returns the pair to its initial value. Applying
the indicated row at every crossing keeps the complete physical state
(5) fixed after EVERY complete R. It supplies a closed route for any
braid width and any signed word, regardless of crossing order. Its
original pivotal factor in (3) is nonzero and of modulus one, and its
single cut factor is 1/N. This is an admitted expanded route of the
complete original source, not an isolated entry without boundary gluing.

## 3. Exact energy and its uniform growth

Every active transfer in the table sees a high input head 2r and a
low input head r in the orientation of that C. Both triples in (4)
are EXACTLY (r,r,r). Each zero transfer contributes the two triples
(0,a,d-a) and (0,b,d-b), with

    w_d(0,a,d-a)=1/N.

Thus its squared entry is exactly one. There are two active C maps
per crossing, giving four regular cells. For a word with m crossings,
the product of squared, quarter-gauged path entries is exactly

    E_route=N^(4m) w_d(r,r,r)^(4m)=N^(4m)/s_r^(12m).           (6)

All internal gauge factors telescope, since the route is closed.
Equation (6) is therefore also its ungauged squared modulus; no
endpoint gauge or source normalizer is missing. Including the literal
cut coefficient changes (6) by N^(-2), and including chi_N multiplies
it by |chi_N|^2. These known external factors remain explicit.

Let Z_path be the positive sum of squared entries over all closed
physical paths in the alphabet (2), with the original trace boundary
conditions. Then

    Z_path>=N^(4m)w_d(r,r,r)^(4m).                             (7)

With Lambda(theta)=-integral_0^theta log(2sin t)dt and
v_3=3Lambda(pi/3), the uniform endpoint factorial estimate gives

    log s_r=-(N/pi)Lambda(pi*r/N)+O(log N),
    lim_(N=3r+1) (1/N)log E_route=4m v_3/pi.                  (8)

This is an exact all-r family with a proved rate, not extrapolation
from a few levels. Every cell has the correct affine sum d and every
physical head-flow/source constraint is satisfied.

For the original figure-eight word [1,-2,1,-2], m=4 and its geometric
volume is 2v_3 (two regular ideal tetrahedra). The lower rate in (8)
is 16v_3/pi, whereas a sharp angle ENERGY partition has rate 2v_3/pi.
Hence neither a polynomial normalization nor bounded polynomial
multiplicity can identify the complete phase-free Z_path with that
sharp positive geometric fiber. In particular the actual shared-spin
relations alone do not imply the required geometric edge equations.

## 4. What has to remain coherent

The route is NOT claimed to survive summing its internal C channels.
For example, for R_+ at input (r,2r), the diagonal physical entry is
zero: the literal positive R requires output first head b+k with
k>=0, so returning it to r is impossible. Its nonzero expanded routes
cancel exactly. For R_- the analogous statement holds at (2r,r).
This is a constructive reason to perform the available complete
crossing contractions before assigning an angle partition, not a new
obstruction to doing so. It also prevents misidentifying (6) with an
already coherently summed, nonzero original clock sector.

The exact positive cells and coherent Gram remain useful. What fails
is the shortcut of imposing the original physical head/source support
on their phase-free path expansion and inferring a sharp geometric
edge fiber from that support alone. An additional source-preserving
coherent regrouping, such as complete-channel recoupling with its
full mixed Gram, is necessary. This theorem does not rule out that
route or a different global inner product.

[Focused audit](../experiments/audit_actual_closed_pascal_route_energy.py):
original coproduct-derived C and inverse, full positive and negative R,
both path orders, quarter metric and all regular/boundary cells,
original pivotal trace conversion, and nonzero closed routes at
arbitrary adjacent positions.
