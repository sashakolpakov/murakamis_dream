# A full-source tree channel exceeds the hyperbolic volume rate

28 October 2026. The short-complement forest representation is exact,
but its individual source channels do not automatically satisfy the
hyperbolic-volume bound. This failure already occurs for the original
figure-eight source AFTER its forced full block has been contracted.
An explicit all-short spanning-tree term has rate

    -5 J(1/5)=0.79366964575974769...,
    J(s)=integral_0^s log(2 sin(pi t)) dt,          (1)

whereas Vol(4_1)/(2 pi)=0.32306594721945051.... All central norm
factors, short-root Jacobians and the extracted source loop are
included. Thus direct absolute estimation of this exact tree
representation cannot give the conjectured sharp upper bound.
The statement concerns this representation and its absolute envelope;
it does not exclude a further phase-aware regrouping of its channels.

There is a separate algebraic limitation: if ordinary parent charges
larger than N-1 are retained during iteration, jets only at the short
roots can require order proportional to N, even at two anchors.
Bounded anchor count alone does not bound that local jet depth.

## 1. The actual source after the forced full block

Use N=5r+1, r>=1, d=N-1=5r and the actual overclocks of the
figure-eight word [1,-2,1,-2]

    h=(0,v,w,t)=(0,3r,2r,4r).                     (2)

The [actual finite block table](actual_alternating_balanced_source.md)
gives its entire closure-contracted source, after the displayed unit
coordinate gauges, as

    [A^d B^d C^d D^d]
      B_d(B,C;1)
      B_(d-v)(D,A;Q^(v+1))
      B_v(A,B;Q^(-v+w+1))
      B_(d-w)(C,B;Q^(w+2))
      B_w(B,D;Q^(-w-t-1))
      B_(d-t)(A,D;Q^(-v)) B_t(D,C;1),             (3)

with Q=exp(2 pi i/N) and B_L(X,Y;a)=product_(j<L)(X-Q^j aY).
All original external and clock scalars remain; they have unit
modulus or polynomial size at complete color in these singleton
overbridges and do not alter the rates below.

Contracting the first, genuinely forced full block sets B=Q^(-1)C.
The middle C-to-B factor becomes a loop. Consequently (3) is EXACTLY

    Q^(-w) L_w [A^d C^w D^d] E(A,C,D),
    L_w=(Q^(w+1);Q)_(d-w)=F_d/F_w,               (4)

where F_k=(Q;Q)_k and

    E=B_(d-v)(D,A;Q^(v+1))
       B_v(A,C;Q^(w-v))
       B_w(C,D;Q^(-w-t))
       B_(d-t)(A,D;Q^(-v)) B_t(D,C;1).           (5)

The factor Q^(-w) is the tail normalization of B_w(Q^(-1)C,D;...).
The source charge of C is w, rather than d. To apply the original
ordinary-d forest residue formula one equivalently uses

    [A^d C^d D^d] C^(d-w) E.                     (6)

This monomial source padding is compulsory and is retained below.
Equations (3)--(6) are ordinary coefficient identities, preserving
the original source. No new boundary functional has been chosen.

## 2. A specified original relative-residue channel

Choose the two actual tree edges

    A -> C: length v=3r, root coefficient Q^(-r),
    D -> C: length t=4r, root coefficient 1.       (7)

Their SHORT complementary polynomials are

    S_A=product_(i=0)^(2r)(A-Q^(2r+i)C),
    S_D=product_(j=0)^r(D-Q^(4r+j)C).              (8)

Take regular fixed centers C_C=1, C_A and C_D distinct from 0 and 1
and from each other. In the complete forest formula of
[the original complementary source](actual_complementary_source_transport.md),
the ALL-SHORT component contains every pair of roots in (8), with
the original relative-cycle coefficient. Select precisely

    i=r, j=0:
    A=Q^(3r) C, D=Q^(4r) C, C^N=1.              (9)

This is not an assumed geometric critical point; it is one explicit
nonzero term of the exact original relative residue formula.

The two central factors in its numerator are
K_A=C_A-1, K_D=C_D-1. At (9) their original Fermat denominators
are 1-C_A and 1-C_D. They cancel EXACTLY, with product sign +1.
Thus there is no omitted central multiplier, large-center choice
or inverse central norm affecting this term.

The remaining Jacobian is

    S_A'(A) S_D'(D) N C^d.                       (10)

The numerator has total degree 3d-v-t, equal to the total degree
of this Jacobian. Therefore the N root labels of C have identical
values. Their sum cancels the N in (10) exactly. The whole selected
channel, including the source loop (4), is, up to the fixed relative
orientation sign,

    T_r=Q^(-w) L_w
       E_rest(Q^(3r),1,Q^(4r))
       /[S_A'(Q^(3r)) S_D'(Q^(4r))],             (11)

where E_rest is (5) with the two selected long tree blocks removed.
There is no factorial normalizer or root-label average suppressed
in (11). An individual ungrouped C root has magnitude |T_r|/N;
this has the same exponential rate.

## 3. Exact magnitude and its entropy

All factors in (11) are nonzero. Directly splitting the short-root
derivatives gives

    |S_A'|=|F_r|^2,  |S_D'|=|F_r|.               (12)

The three remaining long products have respective root intervals

    2r+1,...,4r;
    3r+1,...,5r;
    3r+1,...,4r.

Their product magnitude is

    |F_(4r)/F_(2r)| * |F_(5r)/F_(3r)|
       *|F_(4r)/F_(3r)|.

Together with |L_w|=N/|F_(2r)|, this gives

    |T_r|=N^2 |F_(4r)|^2
                    /(|F_(2r)|^2 |F_(3r)|^2 |F_r|^3)
           =N^2/|F_r|^5.                         (13)

The final equality uses the exact root reflection
|F_k F_(d-k)|=N at k=r and 2r. It is not an asymptotic estimate.
The uniform factorial estimate log|F_k|=N J(k/N)+O(log N) now proves
(1), since r/N tends to 1/5.

The strict comparison with the figure-eight volume does not require
decimal diagnostics. Since sin(pi s)<=pi s,

    -5J(1/5)>=1-log(2pi/5)>=2-2pi/5>26/35.

The calibrated figure-eight volume is 2D(exp(pi i/3)), and the
dilogarithm series gives D(exp(pi i/3))<=sum_(n>=1)1/n^2=pi^2/6.
Hence its volume rate is at most pi/6<11/21<26/35.
The actual rates are the decimals in (1).

Thus the triangle-inequality envelope of this tree representation
is too large even after the genuine source-forced full contraction.
Its currents and root channels must undergo further cancellations
or exact regrouping before a sharp Rivin-volume estimate is possible.
We do not assert that (2) is a leading surviving clock sector, or
that an individual residue rate is the rate of its complete source.
The finite audit certifies nonzero complete clock-sector coefficients
at several levels as an additional check, not an all-r hypothesis.

## 4. Short-root jets can require macroscopic depth

The obstacle here is algebraic and has arbitrary degree. Let
1<=m<N, L=N-m, and put

    B=B_L(X,Y;a), S=B_m(X,Y;aQ^L),
    q_X=d, q_Y=2d,
    s<=floor((d+m-1)/m).

Define the allowed homogeneous exterior

    H_s=X^d S(X,Y)^s Y^(d+m-1-ms).               (14)

Its degree is 3d-L=2d+m-1, precisely the exterior degree required
by this pair of source charges. It vanishes to order s at EVERY
short-root branch S=0. In particular all normal jets of order
strictly less than s are zero there. Nevertheless

    [X^d Y^(2d)] B H_s
       =B(0,1) S(0,1)^s !=0.                    (15)

Indeed the exterior factor X^d forces every other factor to its
X-constant term. All their Y-degrees sum to 2d and their constants
are nonzero for a!=0. For fixed m, s can be proportional to N.
Already m=2, L=d-1 excludes the full blocks removed in (4).

Therefore no unrestricted interpolation of these larger ordinary
source charges using ONLY short-root jets of depth bounded by
anchor count is valid. This does not obstruct retaining the original
Fermat-root/mixed-current channels, or derivatives on a complete
finite-Frobenius presentation. Such channels contain source data
which short-root evaluations alone have lost. Nor is (14) claimed
to be a new original-knot source: it refutes the unrestricted
arbitrary-exterior interpolation needed for such a proposed closure.

## 5. Audit

    python3 experiments/audit_actual_forced_source_tree_entropy.py

The audit verifies the actual figure-eight block table, the full
source/loop reduction, the exact nonzero central-norm cancellation
and ALL C-root labels of the specified relative-residue channel.
It checks (13) independently by complex products and reflection,
the actual fixed-clock source over finite cyclotomic fields, and
the short-root-jet obstruction including m=2. It imports no volume
proof; the rate comparison is the elementary argument above.
