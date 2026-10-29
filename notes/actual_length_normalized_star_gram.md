# Exact length-normalized stars and their doubled Gram

29 October 2026. The original charged star admits an exact factorial
length normalization which removes its exponential scalar. Its doubled
boundary Gram changes by exactly `1/N`. Contiguous parallel fusion then
supplies the square root of the positive affine-angle weight. These are
source-preserving tensor identities, with all phases retained.

The length frame has a polynomial original clock co-source, as proved in
[the independent source calculation](actual_length_gauge_clock_source.md).
This does not estimate the norm of the completely contracted clock state.
Indeed [a complete figure-eight sector](actual_figure_eight_clock_gram_obstruction.md)
shows why a diagonal norm on those clocks is insufficient for the sharp
volume comparison.

## 1. The typed length frame

Set `q=exp(pi*i/N)`, `Q=q^2`, `d=N-1`, and

    F_a=(Q;Q)_a, s_a=|F_a|, L_a=s_a^2/N,
    A_a=L_a^(1/8), D_a=A_a^2=s_a^(1/2)/N^(1/4).

Root complementation gives, exactly,

    s_a s_(d-a)=N, A_a A_(d-a)=1, D_a D_(d-a)=1.       (1)

For an actual root interval put

    B_l(X,Y;a)=product_(r=0)^(l-1)(X-Q^r aY),
    b_l(X,Y;a)=B_l(X,Y;a)/D_l.                         (2)

The index `l` is an interval LENGTH. Equation (2) is not permission
to apply a physical-head diagonal gauge to a fusion-relative index.
For a fixed charged graph it is a scalar normalization of each actual
polynomial block, so its effect on the full source is unambiguous.
In particular `D_0=N^(-1/4)` and `b_0=N^(1/4)`: zero-length slots
are retained, or their exact scalar is explicitly compensated. An empty
unnormalized block may be omitted; its normalized version is not one.

If `P_G` is a graph polynomial, let `D(G)=product_edges D_l`. Then

    P_G=D(G) P_(b,G).                                 (3)

Every original graph prefactor is multiplied by `D(G)` when the blocks
are changed to `b`. For varying lengths this is a diagonal change of
frame on explicit length registers. Interior inverse changes cancel;
the actual source and all its length constraints must be transported.

For singleton over-events every crossing has lengths `(d-h,h)`, so
its factor in (3) is one. The original closure blocks contribute only
`D_d=N^(1/4)` each; their exact source contractions cancel these factors
in the closure-contracted presentation. Thus the original singleton
clock co-source is polynomial, including its original feedback, pivots,
framing and peripheral line. No knot value is used to choose this frame.

## 2. The normalized balanced star, including its full phase

Take nonnegative `k_1+k_2+k_3=d`, put `l_i=d-k_i`, and assume
`|a_i|=1`. The [proved actual star identity](actual_general_flow_fusion.md#3-balanced-star--triangle-identity)
has outer triangle

    B_(k_3)(X_1,X_2;Q^(k_2+1)a_1/a_2)
    B_(k_1)(X_2,X_3;Q^(k_3+1)a_2/a_3)
    B_(k_2)(X_3,X_1;Q^(k_1+1)a_3/a_1).

Define `T(k)=k(k-1)/2` and

    w(k)=1/(s_(k_1)s_(k_2)s_(k_3)),
    u(k,a)=(-1)^(k_1+k_3)
       *Q^[T(k_1)+T(k_3)-k_2]*q^(k_1 k_3)
       *a_1^(k_2)a_2^(k_3)a_3^(k_1).                 (4)

Here `|u|=1`. The sine-binomial identity

    [l choose r]_Q=q^[r(l-r)] s_l/(s_r s_(l-r))

and (1) give the original star scalar `N w(k) u(k,a)`.
Changing all six interval blocks according to (2) therefore gives

    [Z^d] product_i b_(d-k_i)(X_i,Z;a_i)
       =N^(-1/2) u(k,a) product_triangle b_k.          (5)

Indeed the normalizer ratio is

    product_i D_(k_i)/D_(d-k_i)
       =product_i D_(k_i)^2
       =1/[N^(3/2)w(k)].                             (6)

This proves (5) at every level, including zero lengths and coincident
outer variables. It is a polynomial identity, valid inside ANY
polynomial exterior paired by the original socle coefficient. There is
no change of selected period and no positive-trace assumption.

More generally the normalization `B_l/A_l^theta` changes the scalar to

    N^(1-3theta/4) w(k)^(1-theta/2) u(k,a).            (7)

Thus `theta=1` gives `N^(1/4) sqrt(w) u`, while the frame (2),
`theta=2`, makes the star scalar polynomial and independent of the
angles in modulus. Formula (7) explains precisely where the full
binomial is moved; it has not been discarded.

Let `v_old,v_new` be the boundary coefficient vectors of (5) in ANY
common positive Hermitian boundary metric `H`. Then

    <v_old,H v_old>=N^(-1)<v_new,H v_new>.             (8)

The stronger rank-one Gram equality follows as well. The same `H`
must be used on the typed outer boundary on both sides; replacing it
by unrelated positive metrics would require their actual adapters.

## 3. Parallel fusion produces the positive angle weight

For `L+M<=d` the ordered intervals concatenate exactly:

    B_L(X,Y;a) B_M(X,Y;aQ^L)=B_(L+M)(X,Y;a).

In the same frame (2),

    b_L(a)b_M(aQ^L)
       =N^(1/4) sqrt(|[L+M choose L]_Q|) b_(L+M)(a)
       =N^(3/4) sqrt(w_N(L,M,d-L-M)) b_(L+M)(a),      (9)

where `w_N(a,b,c)=1/(s_a s_b s_c)` and `a+b+c=d`.
The local identity `|[a+b choose a]_Q|=N w_N(a,b,c)` is exact.
All interval roots and reversal phases remain in their stated places.
In particular (9) is a genuine square-root positive-angle amplitude,
not an identification of an unnormalized star with its square root.

For a full block, `b_d=N^(-1/4)B_d`. Its arbitrary-exterior
reproducing contraction therefore has polynomial cost `N^(-1/4)`
times the original unit monomial. A saturated full-block loop retains
its exact finite geometric sum; short loops are not declared tame.

A fixed valid reduction program made from (5), (9), full-block
contractions and explicit interval reversals has scalar equal to a
power of `N`, a retained unit phase, and the product of the square-root
angle weights from its parallel fusions. A tame terminal pairing and a
proved geometric incidence certificate would turn such a program into
a sharp comparison. Existence of that program and certificate for all
original clock graphs, or for a broad knot class, is not proved here.

## 4. A compatible anchor metric and its compulsory dual weight

One useful coefficient metric on a single anchor is

    ||X^a||^2=m_a=s_a/sqrt(N).                         (10)

The coefficient of `X^(L-r)Y^r` in `b_L(X,Y;a)`, for `|a|=1`,
has squared norm in the tensor product of (10)

    N^(-1/2) |[L choose r]_Q|
       =sqrt(N) w_N(r,L-r,d-L).                      (11)

This follows by multiplying its squared coefficient by
`m_r m_(L-r)`; no phase is changed. Its sum over `r` is therefore
an actual positive affine-angle partition up to a power of `N`.

The trivalent anchor co-source `lambda_d(X^aY^bZ^c)=delta_(a+b+c,d)`
has squared dual coefficient weight

    1/(m_a m_b m_c)=N^(3/2)w_N(a,b,c), a+b+c=d.       (12)

Equations (11)--(12) must both be retained. Merely using (11) and
declaring the anchor contraction a unit functional loses its dual
angle weight. The metric `m_a=s_a` instead changes only the displayed
powers of `N`. It does not remove the exponential weight.

These exact local Gram identities provide a concrete special inner
product for the user's Cauchy proposal. The remaining requirement is
a coherent GLOBAL estimate of the normalized network energy with its
actual dual contractions. The complete clock-sector example linked
above rules out obtaining that estimate from a diagonal clock norm
alone; it does not rule out a non-diagonal Gram retaining cancellation.

[Audit](../experiments/audit_actual_length_normalized_star_gram.py):
full normalized polynomial stars and phases, parallel fusion, and both
coefficient/dual angle-weight identities.
