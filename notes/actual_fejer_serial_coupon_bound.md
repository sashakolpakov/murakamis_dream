# Exact serial Fejer coupons have only a polynomial composition cost

31 October 2026. This concerns the literal SAME
ordered pair Casimir and its actual homogeneous composition. A diagrammatic
digon may be replaced using this lemma only after its cups, dual turns and
port order have been identified with that serial composition. No assertion
about an arbitrary matching/matching separating cut is made.

## 1. Exact finite source and positive paths

Let N be even, d=N-1, theta=pi/N. On the actual polynomial source block
with basis z^j, 0<=j<=d, write

    Omega z^j=c_j z^j-s_j^2(x+y)z^(j-1)
                        -s_j s_(j-1)xy z^(j-2),
    c_j=2cos((2j+1)theta), s_j=2sin(j theta),
    a_j=2+c_j=4cos^2((j+1/2)theta)>0.

The endpoint factors s_0=0 make every illegal physical step zero. The
even root characteristic polynomial is chi_N(sigma)=2T_N(sigma/2)+2,
with chi_N(-2)=4. Hence the FULL positive endpoint coupon is exactly

    P_N=-V_N(-2)=4(2+Omega)^(-1).                    (1)

This includes all repeated-node/Hermite data, with the
[original full numerator convention](actual_gaussian_resolvent_numerator_and_cap.md).
Its homogeneous polynomial
H_P is the already proved original marked-source coupon; it has no new
trace normalization or independently reset half-power.

Put K=(2+Omega)^(-1). For any downward path pi from j to i, with steps
one or two, let Vert(pi) be its distinct visited row indices and w(pi)
the product of the literal nonnegative lowering weights. Expanding the
triangular inverse gives its contribution to K as

    w(pi) product_(v in Vert(pi)) a_v^(-1).          (2)

One-steps retain (x+y) and two-steps retain xy. Thus all comparisons
below are coefficientwise in the original four homogeneous faces,
not only positive-weight evaluations.

## 2. Composition and the repeated-vertex multiplier

Fix an integer ell>=1. Composing ell copies of K decomposes a complete
downward path into ell consecutive subpaths, allowing zero-step subpaths.
Each of the ell-1 break vertices is then counted an extra time in the
inverse diagonal product. Breaks may repeat; their order along the path
is fixed. Therefore the multiplier of (2) is EXACTLY

    h_(ell-1)({a_v^(-1):v in Vert(pi)}),             (3)

where h_r is the complete homogeneous symmetric polynomial of degree r.
There is one decomposition for every multiset of break vertices. This
also proves the formula for a zero-step path and arbitrary ell.

All variables are nonnegative, and h_r(t)<= (sum t)^r. The full inverse
diagonal sum has the exact value

    sum_(j=0)^d a_j^(-1)=N^2/4.                     (4)

Indeed chi_N'(sigma)/chi_N(sigma)=sum_j(sigma-c_j)^(-1), while
chi_N'(-2)=T_N'(-1)=-N^2 at even N and chi_N(-2)=4. This uses every
row with its multiplicity, including repeated Casimir eigenvalues.

The P_N^ell-to-P_N path multiplier is 4^(ell-1) times (3). Retaining
the term with every break at the initial row j gives the lower bound
(4/a_j)^(ell-1)>=1, since a_j<=4. Equations (3)--(4) therefore give
the finite, uniform coefficientwise comparison

    H_(P_N) <= H_(P_N^ell)
                          <= N^(2ell-2) H_(P_N).    (5)

No exponential asymptotic or fixed-radius comparison enters this bound.
For fixed ell the two sides have the SAME exponential rate. It also
holds when x=y, or after
any original nonnegative variable identification or zero specialization.

For reference the zero-step part satisfies the two-sided comparison

    H_1 <= (H_P)_diag=sum_j (4/a_j)b^j c^(d-j)
                        <=N^2 H_1,                 (6)
    H_1=sum_j b^j c^(d-j).

The lower bound uses a_j<=4; the upper bound follows from (4) or from
min_j a_j=4sin^2(pi/(2N)). It concerns the FULL diagonal range, not
one fixed left or right half label.

## 3. Literal homogeneous and whole-source use

The [original homogeneous composition](actual_crossing_casimir_torus.md)
gives, for the SAME pair Casimir,

    H_FG(x,b,c,y)=[z^d]H_F(x,b,z,y)H_G(x,z,c,y).    (7)

Thus a literal serial chain with the same ordered outer faces x,y and
successive middle faces z_1,...,z_(ell-1) contracts to H_(P_N^ell)
by extracting each ordinary internal target d. There is NO additional
N, pivot, mark or common crossing phase in (7). Its source normalization
has already been included in H, as established by the original physical
grid/cup/cap/mark compiler.

If the other remaining factors have nonnegative coefficients, substitute
(5) into their product and then extract the unchanged original targets.
The resulting whole positive source lies between the source with one
P_N coupon and N^(2ell-2) times that source, with its internal middle
targets removed by (7). Their exponential rates are identical, including
the possibility that both coefficients are zero. All other ordinary and
protected targets stay literal. Any actual cup/dual orientation needed
to realize (7) is a separate diagrammatic premise, not inferred from
the existence of two parallel edges alone.

The exact identity smoothing in (6) and the serial bound (5) do not
establish a full block factorization across arbitrary separating digons,
nor a bound for the original phase-sensitive long-twist period.

## Validation and scope

The [focused audit](../experiments/audit_actual_fejer_serial_coupon_bound.py)
and its [results](../experiments/actual_fejer_serial_coupon_bound_results.json)
check 30 exact characteristic endpoint identities, 3 original full
resolvent identities, and 15 original serial powers through 3,960 physical
grid entries, including 1,290 wrong-unwrapped-total zeros. At 75 digits
they also check 6,116 path break multipliers and 3,120 independently
composed coefficients against BOTH bounds, with maximum relative error
below 6.20e-74. Five full inverse-diagonal sums and 40 diagonal bounds
retain the actual finite endpoint constants.

Root the complete proof and audit code. Cluster
the complete proof/code and freshly replayed all
checks with redirected output, including the lower comparison and the
absence of an extra N in homogeneous composition. Public promotion only
changed links and file-relative audit paths; the portable author replay
reproduced the same results. These checks concern the literal same ordered
pair and its physical endpoints. They do not certify an arbitrary
diagrammatic digon adapter, global volume comparison or filling cycle.
