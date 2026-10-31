# Feasible anchor phases are not globally flat, even on surviving knot states

28 October 2026. The new EXACT charged bridge-flow coefficient has a
positive-magnitude expansion with a specified U(1) graph connection.
Its phases cannot in general be removed by vertex gauges. This remains
true on feasible charge flows in a nonzero source sector of a reduced
alternating hyperbolic knot, and the holonomy persists semiclassically.

The counterfamily also has an exact q-binomial fusion: its entire
coefficient is polynomially sized. Thus this is a constructive example
of source cancellation, not evidence that its particular sum remains
unsolved. The next general step must use such phase-aware fusions,
rather than assume vertex-gauge positivity of the charged source.

## 1. The exact positive-magnitude expansion and its proper flatness test

The event polynomials of
[the actual whole charged source](actual_global_charged_bridge_flow.md)
are products of blocks

    product_(r=0)^(L-1)(alpha X_u-Q^r beta X_v),
    0<=L<=d=N-1, q=exp(pi*i/N), Q=q^2.              (1)

Since all sine factors in F_j are positive in magnitude for 0<j<N,

    [L choose k]_Q=q^(k(L-k))*|[L choose k]_Q|.

The coefficient of X_u^(L-k)X_v^k in (1) is therefore EXACTLY

    alpha^L *|[L choose k]_Q| *w_e^k,
    w_e=-(beta/alpha)q^(L-1).                       (2)

The quadratic k phases cancel. Every magnitude in (2) is strictly
positive for 0<=k<=L. The common alpha factors and the original
clock/source factor W_h remain outside this expansion.

Let k_e be the chosen head-charge on each oriented block u->v.
The actual source requires degree d at EVERY anchor. Thus

    incoming(k)-outgoing(k)
                     =d-sum_(e leaving anchor)L_e.  (3)

If w_e=eta_v/eta_u, the phase product is constant on this charge
polytope. But a bare graph cycle need not be feasible: some edges may
be forced to capacity zero or their full capacity. The exact test is
the lattice of DIFFERENCES OF FEASIBLE FLOWS.

For a feasible flow k, form its residual directed graph: use an edge
forward if k_e<L_e and backward if k_e>0, carrying phase w_e or
w_e^(-1), respectively. A residual cycle with nontrivial phase gives
another feasible flow with a different phase by one unit augmentation.
Conversely, every difference of feasible integer flows decomposes into
such residual cycles, by following an available positive edge until a
vertex repeats and then subtracting its minimum multiplicity. Therefore
phases are constant on the full feasible support if and only if all
these feasible cycle holonomies are one. This criterion retains the
source capacities and charges, not only graph topology.

Self-loop blocks may first be evaluated as their exact scalar
Pochhammer; if one is zero the entire clock sector is zero. The
counterexamples below have no such hidden zero factors.

## 2. A uniformly surviving BULK-curvature family

Use the actual reduced alternating three-braid

    W=[1,-2,1,1,-2,-2].                             (4)

Its closure is the 13/5 two-bridge knot 6_3. The existing
[6_3 certificate](six_three_and_two_bridge_audit.md) proves its
hyperbolic geometry. An optional exact marked-triangulation check in
the audit compares (4) with RationalTangle(13,5).numerator_closure();
both give isosig gLLPQccdefffhggaacv_aBBb. None of the coefficient or
phase calculations below depends on a numerical knot recognition.

Put N=2r+1, d=2r and choose the original overclocks

    h=(0,r,r,r,0,r), r>=1.                          (5)

All bridges in this alternating diagram have length one, so (5) is
in the exact monotone source domain. The nine anchors are numbered
by the six bridge events followed by the three original closures.
The nonempty grouped blocks are as follows; w_e=q^(k_e^phase).
The last column is a feasible head-charge, not its phase exponent.

| e | tail -> head | L | phase exponent | base charge |
| --- | --- | --- | --- | --- |
| 0 | 6 -> 7 | 2r | 2r | r |
| 1 | 8 -> 0 | r | -r | 0 |
| 2 | 0 -> 1 | r | r | 0 |
| 3 | 7 -> 1 | r | -r | 0 |
| 4 | 1 -> 2 | r | -r | 0 |
| 5 | 1 -> 2 | r | r | 0 |
| 6 | 2 -> 3 | r | -r | 0 |
| 7 | 0 -> 3 | 2r | -2r | r |
| 8 | 3 -> 4 | r | r | 0 |
| 9 | 4 -> 5 | r | r | 0 |
| 10 | 2 -> 6 | 2r | 0 | r |
| 11 | 5 -> 7 | 2r | -2 | 0 |
| 12 | 4 -> 8 | 2r | -2 | r |

The sum of the common alpha^L exponents is zero. The last three
rows are the original source closures, including both pivots.
Every row is obtained from the original signed event formulas;
the table is not an auxiliary graph chosen to create a phase.

The base charges satisfy (3), and so do

    k(t)=k(0)+t*(+e2+e4+e6-e7), 0<=t<=r.           (6)

This is a four-vertex BULK cycle 0->1->2->3->0. It uses no closure
edge. All bounds are satisfied for every integer in (6); all its
flow weights are nonzero. Its exact phase per augmentation is

    w2 w4 w6/w7=q^r -> exp(pi*i/2).                 (7)

This is a genuine order-N exponent, not Q raised to a fixed integer.
One may take t near r/2 to obtain an interior cycle margin of order N.
Vertex gauges preserve relative phases of equal-charge flows, so
cannot turn (6) into positive weights.

The WHOLE clock-sector coefficient nevertheless survives, at every
odd level:

    [X_0^d ... X_8^d]P_h=N q^(2-r^2) !=0.          (8)

Thus the example is not a nonflat graph supported only in a sector
which the charged source kills. We now prove (8) by exact fusion.

## 3. Exact fusion of the surviving curved sector

First the two parallel r-blocks e4,e5 concatenate their root intervals
and become

    product_(j=1)^d(X1-Q^j X2)
                 =sum_(j=0)^d X1^(d-j)X2^j.        (9)

This already performs their internal phase cancellation. Even on
the resulting coarser graph, the feasible cycle through e2,(9),e6,e7
has holonomy q^(2r)=x -> -1, not one.

Let C_j=|[r choose j]_Q| and

    B(t)=sum_(j=0)^r C_j t^j
                      =(-q^(1-r)t;Q)_r.            (10)

All six remaining r-blocks supply positive C_j magnitudes. Solving
the source charges after (9) gives free b in [0,r] and nonnegative
a,c,f with a+f<=r,c+f<=r. The r-block head-charges, in edge order
e1,e2,e3,e6,e8,e9, are

    a,c,b,f+c,f+a,f.

The other head-charges are

    e0=e10=r+b-f, e45=b+c, e7=r+a-c,
    e11=f, e12=r+a.

These are all the feasible flows, not a restricted subfamily.
Using the phase table, their total exponent is

    -2r+r b-(2r+2)a+2r c-(r+2)f.                   (11)

There are no further alpha^L factors. Since q^(4r+2)=1, the two
correlation sums in a,c use the SAME weight q^(2r).
The exact finite identity

    B(t)B(q^(2r)t)=sum_(j=0)^d q^(rj)t^j            (12)

follows directly by concatenating the two root progressions in
(10) and using [d choose j]_Q=(-1)^j Q^(-j(j+1)/2).
Taking the coefficient of t^(r-f) yields

    sum_a C_a C_(a+f)q^(2r a)=q^(r(r-f)).          (13)

Apply (13) twice in (11). The remaining b and f sums both equal

    B(q^r)=(Q^(r+1);Q)_r=N/F_r.                    (14)

The result is q^(-2r+2r^2)(N/F_r)^2. Root reflection gives
F_r^2=N(-1)^r Q^(r(r+1)/2); reducing the exponent modulo 2N proves
(8). This supplies the actual nonzero surviving source coefficient
and explains its polynomial size by explicit q-binomial cancellations.
It is not an assumed asymptotic lower bound.

## 4. A second, simpler full-source cycle

For the original figure-eight word [1,-2,1,-2], at ANY N choose
h=(0,0,H,d),1<=H<d. The grouped feasible flows reduce to a rectangle
0<=k<=d-H,0<=v<=H. In the eight nonempty-edge ordering of the audit,

    k0=k5=H-v+k, k1=k7=d, k2=k,
    k3=k4=k6=v.

There is a feasible five-edge cycle changing v down by one at fixed
k, with holonomy q^(N+H+1). It includes closure edges and can have
order-N residual capacity. Exact q-binomial summation gives

    coefficient=N q^(4+H-H^2-NH) !=0.               (15)

For example its two separated sums are
(Q^(H+1);Q)_(d-H) and (Q^(-H);Q)_H. Their product is N times a unit
phase. This demonstrates why retaining the actual closure is essential
even when the bulk support happens to be phase-flat in a small example.

## 5. What the graph criterion does and does not settle

The positive-sine grouping is exact and useful. It converts unknown
flow-dependent phases into a finite graph character. But neither the
global nor the bulk character is automatically a vertex coboundary on
nonzero source support. Equations (5)--(8) prove this uniformly for an
actual reduced alternating hyperbolic-knot state.

The same example exhibits the constructive alternative: fuse the root
progressions and their charge correlations BEFORE taking absolute
values. Here that gives (8) exactly, hence only polynomial size. The
example does not obstruct a further phase-aware normal form or a
geometric asymptotic theorem for the full remaining clock sum. It
rules out erasing anchor cancellation by a blanket flatness/positivity
assertion, and provides an explicit q-cycle fusion for testing a more
general rule.

[Exact audit](../experiments/audit_anchor_phase_cycles_and_fusion.py)
and its saved certificate verify original block metadata, all source
charges/capacities, the nonflat bulk cycle, exact cyclotomic coefficients,
and the two finite product fusion identities. Optional --topology
compares the explicit braid with the 13/5 rational tangle.
