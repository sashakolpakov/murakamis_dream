# Complete figure-eight clock sectors and diagonal Gram metrics

29 October 2026. The exact factorial length frame has a polynomial
original clock co-source. Nevertheless one fully anchor-contracted
clock sector of the original figure-eight knot has twice the desired
volume rate. Consequently every positive DIAGONAL clock metric has
an exponentially excessive Cauchy budget on this actual source.

This concerns a COMPLETE clock sector, after its anchor sums and
original closure contractions. It is not an expanded crossing state
or an arbitrary inserted coupon. It does not disprove Cauchy--Schwarz,
the volume conjecture, or a coherent non-diagonal special inner product.

## 1. The original source and its exact reduced table

Use `q=exp(pi*i/N)`, `Q=q^2`, `d=N-1`, `x=-q^-1`,
`F_a=(Q;Q)_a`, `s_a=|F_a|`. The actual word is `[1,-2,1,-2]`.
Its clocks are the original overclocks `(h_0,h_1,h_2,h_3)`.
The [whole charged source](actual_global_charged_bridge_flow.md) and
[actual closure contractions](actual_general_flow_fusion.md) give

    K_N=sum_h K_(N;h),
    K_(N;h)=(chi_N/N) zeta_(N;h) C_(N;h), |zeta|=1.   (1)

`chi_N` is the unchanged original external dimension/framing line;
at completeness its modulus and inverse have polynomial size.
Every common Cartan, pivot and source factor stays in (1).
`zeta` consists only of the explicitly retained powers of `x,Q`,
the crossing Cartan phases and the closure-rescaling monomials.
No unknown knot scalar has been divided out.

The full source support gives `h_0=0`, before any separate-sector
Schur argument. In the rescaled anchors of
[the actual alternating-source table](actual_alternating_balanced_source.md#3-a-second-support-inequality-in-the-actual-reduced-polynomial),
write `B_L(U,V;Q^p)=product_(r<L)(U-Q^(p+r)V)`. Then

    C_(N;h)=[A^d B^d C^d D^d] product of these EIGHT blocks:

| tail -> head | length | p |
| --- | --- | --- |
| B -> C | d-h_0 | 0 |
| C -> A | h_0 | 1 |
| D -> A | d-h_1 | h_1+1 |
| A -> B | h_1 | -h_1+h_2+1 |
| C -> B | d-h_2 | h_0+h_2+2 |
| B -> D | h_2 | -h_2-h_3-1 |
| A -> D | d-h_3 | -h_1 |
| D -> C | h_3 | 0 |

This table includes the original pivotal closure substitutions. For
auditability, `zeta` in (1) is obtained without any scalar choice by:
the `charged_data` weight; the `normalized_graph` tail monomials;
the `contract_edge` closure factors; and the substitutions of anchors
`B,D` by `x^-1 B,x^-1 D`. Each factor is an original root of unity.
Those exact operations are implemented in the audit linked below.

The normalized blocks

    b_L=B_L/D_L, D_L=s_L^(1/2)/N^(1/4)

have `D_(d-h_i)D_(h_i)=1` at each crossing. Thus the product of all
EIGHT table normalizers is exactly one. The coefficient `C_(N;h)`
is also the completely contracted normalized-b clock STATE in this
closure-contracted presentation. The co-source remains polynomial,
as in [the exact clock-source theorem](actual_length_gauge_clock_source.md).

## 2. A uniform family with no internal cancellation

Let

    N=3k+1, d=3k, h=(0,2k,k,2k), k>=1,
    beta_(L,r)=|[L choose r]_Q|=s_L/(s_r s_(L-r)),
    S_k=sum_(r=0)^k beta_(2k,r) beta_(2k,k-r)>0.         (2)

Then the COMPLETE table coefficient is exactly

    C_(N;(0,2k,k,2k))=N q^(3k^2-2k) S_k/F_k.          (3)

In particular the original sector modulus is

    |K_(N;(0,2k,k,2k))|=|chi_N| S_k/s_k.              (4)

Here is a direct coefficient proof. The full `B_d(B,C;1)` contracts
`B=Q^-1 C`. Its `C -> B` loop is `C^(2k)N/F_k`.
Reversing the `D -> A` interval and concatenating it with the
`A -> D` interval produces `B_(2k)(A,D;Q)` with reversal factor

    xi_1=(-Q^(2k+1))^k Q^[k(k-1)/2].

The replacement in `B -> D` contributes `Q^-k`. For the two
remaining C/D intervals use

    B_k(C,D;Q^(-3k)) B_(2k)(D,C;1)
       =xi_J (C^N-D^N)/(C-Q^(-2k)D),
    xi_J=(-1)^(2k)Q^[(2k)(2k-1)/2].                   (5)

For `0<=r<=k` its coefficient of `C^(k-r)D^(2k+r)` is
`xi_J Q^[-2k(2k+r)]`. The remaining A/D extraction is therefore
the `D^k` coefficient of `B_(2k)(A,D;Q)^2`, times the displayed
common root factors. Indeed the second interval has effective start
`Q^(k-2k-2k)=Q^(-3k)=Q`.

The coefficient of `A^(2k-r)D^r` in `B_(2k)(A,D;Q)` is

    (-q^(2k+1))^r beta_(2k,r).

Consequently every summand of its `D^k` coefficient has the SAME
phase. Combining this phase, (5), `xi_1` and `Q^-k` gives precisely
`q^(3k^2-2k)`, proving (3). All finite sums, including the loop
factor, have been evaluated; no uncontracted anchor is left.

## 3. Its exact exponential rate

Put `Lambda(theta)=-integral_0^theta log(2sin u)du` and
`v_3=3 Lambda(pi/3)`. The successive ratios of `beta_(2k,r)` are

    beta_(2k,r+1)/beta_(2k,r)
       =sin((2k-r)pi/N)/sin((r+1)pi/N),

which decrease with `r` because `(2k+1)pi/N<pi`. Hence the
symmetric summands in `S_k` are maximal at the integer(s) nearest
`k/2`. The sum lies between that maximum and `(k+1)` times it.
The uniform factorial estimate, including its endpoints, is

    log s_a=-(N/pi)Lambda(pi*a/N)+O(log N).

It follows directly that

    lim_(k->infinity) (1/N)log(S_k/s_k)
       =[3Lambda(pi/3)+2Lambda(pi/6)]/pi
       =2v_3/pi=Vol(4_1)/pi.                        (6)

The elementary Lobachevsky duplication identity gives
`2Lambda(pi/6)=3Lambda(pi/3)=v_3`. The identification
`Vol(4_1)=2v_3` uses its two regular ideal tetrahedra, rather than
an asymptotic volume formula for the invariant.

Thus the actual complete sector has

    lim (2pi/N)log|K_(N;h)|=2 Vol(4_1).               (7)

This is larger than the desired full-knot rate `Vol(4_1)`.
The full original figure-eight scalar does have that latter rate
by its separately proved positive finite sum. There must therefore
be cancellation between COMPLETE clock sectors in this exact frame.

## 4. What this forces on a special inner product

For the flat clock energy `G_N=sum_h |K_(N;h)|^2`, (7) gives

    liminf_(N=1 mod3) (pi/N)log G_N >=2 Vol(4_1).       (8)

The same exponent holds for the normalized-b state energy, because
the original co-source coefficient in (1) has only polynomial norm.
This rules out identifying that flat energy, up to subexponential
factors, with a positive geometric angle partition of rate `Vol/pi`.

More generally let `K=sum_h a_h f_h`. For EVERY positive diagonal
metric `G=diag(g_h)` the exact Cauchy budget is

    B(G)=(sum_h g_h|f_h|^2)(sum_h |a_h|^2/g_h)
         >=(sum_h |a_h f_h|)^2.                      (9)

The infimum over all positive `g_h` is the right side, obtained by
`g_h` proportional to `|a_h|/|f_h|`; zero entries follow by limits.
In particular (7) makes ALL diagonal-clock Cauchy budgets too large
for the desired geometric upper exponent, even when the metric
depends arbitrarily on `N` and on the entire diagram.

For a general positive definite, possibly non-diagonal `G`, the
Riesz vector of the linear co-source `sum_h a_h f_h` is `conj(a)`.
Consequently its budget is

    B(G)=(f^*Gf)(a^T G^(-1)conj(a))
       >=||f||^2 ||a||^2/kappa(G).                   (10)

In the original singleton source `||a||` has polynomial upper and
lower bounds, while this fixture gives
`||f||^2>=exp[2N Vol(4_1)/pi-o(N)]`. Therefore a sharp budget
`B(G)<=exp[N Vol(4_1)/pi+o(N)]` requires

    log kappa(G)>=N Vol(4_1)/pi-o(N)                  (11)

along this subsequence. Exponential conditioning is allowed: the
factorial metrics already exhibit it. Equation (11) is not a
nonexistence theorem. It says that a successful coherent Gram has
to retain genuine phase cancellation; a diagonal reweighting cannot
replace it.

[Audit](../experiments/audit_actual_figure_eight_clock_gram.py): the
literal original reduced table and its exact root-field coefficient,
the common-phase formula (3), positive-sum maximum bounds and the
large-level rate. The proof above is uniform in all `k`.
