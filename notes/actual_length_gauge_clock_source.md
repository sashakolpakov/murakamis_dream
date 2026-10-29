# The original clock source under the factorial LENGTH gauge

29 October 2026. The full original clock co-source has polynomial
Riesz norm in the proposed factorial length frame, provided every
crossing is first kept as a singleton over-event. Each crossing then
supplies a complementary pair of lengths. This is an exact source
embedding for arbitrary signed braid width, including the original
cut, pivots, clock feedback and external scalar.

After an overbridge has been unwound, its factorial Gamma is no
longer a harmless phase. In the same length frame its exact norm
is a positive angle-simplex partition. The two descriptions are
consistent: unwinding has moved a genuine weight from the tensor
network into the clock co-source. It must be retained there or
assigned back to a specified bulk tensor.

This note concerns the LENGTH registers, not a replacement metric
on physical heads. It does not establish a positive geometric
state or a sharp knot bound.

## 1. The actual singleton presentation

Put q=exp(pi*i/N), Q=q^2, d=N-1, x=-q^-1 and

    F_a=(Q;Q)_a,  s_a=|F_a|,
    L_a=s_a^2/N,
    A_a=L_a^(1/8),
    D_a=A_a^2=s_a^(1/2)/N^(1/4).                              (1)

The exact reflection s_a s_(d-a)=N gives

    D_a D_(d-a)=1,  D_d=N^(1/4).                            (2)

For a binary block B_l(X,Y;a)=product_(r<l)(X-Q^r aY), use the
proposed normalization b_l=B_l/D_l. Its coefficients, phases and
spectator dependence are otherwise unchanged.
All original LENGTH SLOTS are retained, including l=0:
D_0=N^-1/4 and b_0=N^1/4. A raw empty factor B_0=1 can be omitted,
but after normalization its scalar must then be recorded. The
complementary products below include those zero-length slots.

In [the original charged source](actual_global_charged_bridge_flow.md),
one may choose EVERY crossing as a singleton over-event: no identity
requires compressing a maximal overbridge. For a word with m
crossings on b heads there are then m+b anchor events. At crossing
j its two binary blocks have lengths

    (d-h_j,h_j), 0<=h_j<=d.                                 (3)

All m clocks are independent. Their feedback into spectator ports
is the same exact signed integer map as in the global source
theorem; it is not suppressed or untwisted. The m crossing Gamma
factors are now just

    kappa^(sigma_j)(-1)^h_j
                  Q^[sigma_j h_j(h_j+1)/2],

of modulus one. Every other factor in W_h is a power of x,Q or
an original pivotal phase. Thus |W_h|=1. The original complete
dimension/framing line is denoted chi_N and remains outside.

Every closure block has length d. Therefore the whole block
normalizer is EXACTLY, and independently of every clock,

    product_edges D_(length)=N^(b/4).                       (4)

There is no factorial action hidden in (4): each pair in (3)
cancels by (2). If f_h is the ACTUAL normalized b-network
coefficient, the exact scalar is

    K_N=(chi_N/N) N^(b/4) sum_(h in{0,...,d}^m) W_h f_h.      (5)

The original cut factor1/N has not been absorbed into an invented
boundary normalization. The f_h can be exponentially large and
oscillatory. Equation(5) makes no assumption about their size.

## 2. Exact source norm and a real full-source Cauchy inequality

Give the clock space C^({0,...,d}^m) its standard orthonormal basis.
The Riesz norm of the co-source in (5) is EXACTLY

    ||ell_N||=|chi_N| N^(b/4+m/2-1).                        (6)

Indeed there are N^m entries, all of the same modulus. This gives
the genuine original-source inequality

    |K_N|^2 <= |chi_N|^2 N^(b/2+m-2) sum_h |f_h|^2.          (7)

For fixed word and the known complete scalar line, the source
factor is polynomial. This is an exact Cauchy--Schwarz theorem,
not a proposed positive pivotal trace or a favorable cut.

Equivalently, the length-register inclusion

    |h_1,...,h_m> -> tensor_j |d-h_j,h_j>
                           tensor |d>^(tensor b)           (8)

is isometric before the diagonal D frame. Applying D on every
length leg leaves every clock pair fixed and multiplies the
closure legs by N^(b/4), exactly as in (4). Arbitrary diagonal
unit-phase clock/flow feedback commutes with this length frame;
its actual phases remain in the network. It supplies no additional
Riesz cost at the boundary. No relation between a length leg and
a physical head index is presumed.

There is a slightly cleaner equivalent source. Contract the b
original closure blocks by the exact source reproducing law
BEFORE taking a norm. Each normalized full block contributes the
retained scalar D_d^-1=N^-1/4, canceling (4). The remaining clocks
are still independent and the new weights W'_h have modulus one.
For a one-component presentation with at least one crossing, the closure edges form the
proved forest, so no unexplained full-loop factor is introduced.
The resulting literal co-source has

    K_N=(chi_N/N) sum_h W'_h f'_h,
    ||ell'_N||=|chi_N|N^(m/2-1).                             (9)

The original pivots survive as their exact root phases in f'_h
and W'_h. Equations(6),(9) use their own typed bulk families;
one must not keep (6)'s family while deleting its closure scalar.

These polynomial SOURCE norms do not estimate the positive energy
sum|f_h|^2. In particular they do not identify that energy with
the geometric angle partition. A large energy is compatible with
an exact Cauchy inequality. Global angle support, edge characters
and coherent normalized-block gluing are additional requirements.

## 3. The exact cost after overbridge unwinding

An m_e-encounter bridge has r=m_e+1 composition lengths

    n_0=d-h_1, n_j=h_j-h_(j+1), n_(r-1)=h_(m_e),
    n_i>=0, sum_i n_i=d.                                    (10)

The original Gamma in the bridge theorem satisfies EXACTLY

    |Gamma_e|=s_(h_1)/(s_(h_m) product_j s_(h_j-h_(j+1)))
             =N/product_(i=0)^(r-1) s_(n_i).                (11)

No normalization is chosen by dividing by the knot value. Under
the SAME b=B/D convention its transformed co-source coefficient
has modulus

    |Gamma_e product_i D_(n_i)|
        =N^(1-r/4) product_i s_(n_i)^(-1/2).                (12)

Thus its exact squared Riesz norm, on the orthonormal composition
basis, is

    N^(2-r/2) Z_(r,N),
    Z_(r,N)=sum_(n_i>=0,sum n_i=d) product_i s_(n_i)^(-1).    (13)

For a collection of compressed bridges, after the closure forest
has been contracted, independence of their monotone clock domains
gives the WHOLE original co-source norm

    ||ell_comp||^2=|chi_N|^2/N^2
                   product_e [N^(2-r_e/2) Z_(r_e,N)].       (14)

The feedback phases can couple the bulk coefficients but do not
change this norm: their moduli are one. Keeping a normalized
coefficient family and declaring its Gamma source unit would
change the original source.

For r=2, reflection gives Z_(2,N)=1 EXACTLY. Consequently (13)
is N, agreeing with the singleton source norm in (9). For r>=3,
the source weight really can have exponential scale. If
Lambda(theta)=-integral_0^theta log(2sin u)du, then

    log Z_(r,N)=N r Lambda(pi/r)/pi+O_r(log N).                (15)

In particular r=3 is the positive tetrahedral angle energy of
rate v_3/pi. This is useful geometric weight, not an unrecorded
error or a claim of geometric knot gluing.

Proof of(15). The uniform factorial estimate gives
log s_a=N J(a/N)+O(logN), with J(t)=-Lambda(pi*t)/pi, including
a=0,d. There are polynomially many compositions and changing
their total d/N to1 changes the maximum by O(logN/N), using the
integrable logarithmic endpoint modulus of continuity. It remains
to maximize sum_i Lambda(pi*x_i), x_i>=0,sum x_i=1.

For r>=3 a maximum cannot lie on the boundary: adding a small
positive coordinate increases the sum by a positive
-delta log delta term, except at a pure vertex; there, distributing
delta equally among two zero coordinates gives a positive
delta log2 term. At an interior maximum no coordinate can be
at least1/2: each of the other coordinates is strictly smaller
than its complement, so shifting mass to one of them increases
the function by the derivative -pi log(2sin(pi*x)). On the remaining
region all coordinates are below1/2, where this function is
strictly concave. Its unique maximum is therefore the uniform
point x_i=1/r. Rounding that point to a composition of d gives
the matching lower bound with O(logN) loss. This proves(15).

An isometric complementary-pair encoding cannot erase the Riesz
norm(13): isometries preserve it. It may instead KEEP the
positive simplex weight as a bulk/source tensor. That is exactly
the weight(12), and its global geometric incidence must still be
proved. The polynomial singleton source and the weighted
compressed source are two exact organizations of the SAME state.

## 4. What this settles for the proposed special inner product

The original clock source is not an uncontrolled exponential
boundary factor in the uncompressed length frame: (6)--(9) give
its exact polynomial norm at arbitrary width. The original
clocks, phases, closure and full external line are explicit.

This does not mean that a contracted normalized b-network scalar
has polynomial norm, nor that its anchor coefficient functional
has polynomial dual norm in every proposed polynomial metric.
For example, with the half-factorial metric ||X^a||^2=s_a, a
valence-v anchor's exact dual norm squared is
sum_(sum a_i=d, a_i<=l_i) product_i s_(a_i)^(-1). Complementary
valence2 is tame; higher valency carries another positive simplex
weight when its capacity constraints allow it. Those gluing
weights must be retained in a global Cauchy/angle calculation.
These are typed source and dual norms. They do not replace every
trivalent tensor by a positive sum-d vertex with complementary
pairings on every edge: a closed such network would require both
Vd=Ed and 3V=2E, which are incompatible for d>0,V>0. In the
actual binary blocks the two flow powers sum to the BLOCK LENGTH
l, not d; the remaining length registers and oriented dual source
charges are essential. A geometric edge-incidence theorem cannot
be inferred by forgetting those types.

No geometric coefficient or lower bound follows from this source
norm alone. The useful next question is whether the COMPLETE
normalized state energy, with these exact source and gluing
weights, has the desired geometric edge support and volume bound.

[Audit](../experiments/audit_actual_length_gauge_clock_source.py):
uncompressed original signed source identities, complementary
normalization, complete bridge Gamma and Riesz partition formulas.
