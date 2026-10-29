# Independent audit of the positive-carry completion and its source scope

27 October 2026. The proposed Euler completion of an actual crossing
does preserve the ENTIRE first-cut matrix of every signed braid at
an original root, as a meridian family. The correcting group has
nilpotence bounded by braid width, independent of N. This is a
genuinely general source-preserving completion, unlike a low-degree
approximation of the quantum factorials.

Two scopes must be retained. Local degree-lowering Ward coupons
can detect its positive-carry error. Also the naive generic-Q Euler
factorization changes the actual q-normal source, already at N=2.
There is a direct repair with explicit normal coupons; at fixed
normal depth their combined correction group is still uniformly
nilpotent. No geometric-sector or volume estimate follows from
nilpotence alone.

## 1. Physical integer degree proves root source preservation

Use the actual balanced nilpotent heads, x=-M/q and Q=q^2 of
exact order N. Put F_a=(Q;Q)_a. The actual two-leg fusion sends
f^a e_k to f_total^a(e_0 tensor e_k). Every physical term of
that vector has TOTAL INTEGER DEGREE a+k, not its reduction
modulo N. The exact actual positive-crossing coefficient is

    a_+=sum_(a+k<N) x^-a d_k f^a e_k/F_a,
    d_k=(-1)^k x^(-2k)Q^(k(k-1)/2).

The common original Cartan scalar is retained externally or on
both matrices. Its Euler completion is

    a_+^E=u_N(x^-1 f) D,
    D=sum_k d_k e_k,

with all a,k between zero and N-1, including a+k>=N. For a
right coefficient f^a e_k to act on a relative input f^b e_j,
the multiplication rule requires j=a+k modulo N. If a+k<N,
input and output integer degrees agree. If a+k>=N, its output
degree is input degree PLUS N. The action is zero when a+b>=N.
Thus, in physical matrices,

    R_+^E=R_+ + E_N,
    E_N raises integer degree exactly N.           (1)

This uses the actual ROOT Borel intertwining/fusion proof. It
holds for every admissible meridian x, not just M=1.

For b strands let A_>=0 be the algebra of matrices whose degree
changes are nonnegative multiples of N, and let n contain its
strictly positive-degree matrices. Original crossings are of
degree zero, so both the completed crossings and their inverses
belong to A_>=0. In fact

    n^b=0,                                         (2)

because the physical total degree is between zero and b(N-1),
whereas b positive carries would raise it by at least bN.
The inverse assertion follows either by graded triangularity or
the finite inverse of 1+n after factoring out the actual crossing.
It holds for every signed word, with no restriction on word length.

The completed word differs from the original by an element of n.
Close all but the first strand with their ORIGINAL pivots. A
possibly nonzero cut entry from first input a to first output c
would have total degree change c-a, which lies strictly between
-N and N. It cannot be a positive multiple of N. Consequently

    ptr_original(W^E-W)=0                           (3)

as the FULL N-by-N cut matrix. Hence every original first-input
probe and the original all-ones output row agree. Every framing,
full d_N(M), peripheral and external Cartan factor multiplies
both sides unchanged. Equation (3) is an identity of root-level
meridian rational families, including their retained regular
germs; it is not obtained by replacing d_N by its complete value.

This does not conflict with the full Borel source-faithfulness
theorem. That theorem allows relative coupons of negative as
well as positive N-degree. The present source quotient is only
on the degree-restricted algebra A_>=0. Lowering an error back
to degree zero is deliberately not an allowed operation there.

The group 1+n has lower-central depth at most b-1, with finite
logarithm and inverse formulas. Braid/coherence errors of the
completed matrices lie in that group since their degree-zero
parts are the actual braid matrices. Their original closed
sources vanish by (3). This supplies an algebraic completion
of the actual source; it supplies no bound for the entries of
the degree-zero word or its hyperbolic action.

## 2. A local Ward coupon detects the carry

At N=2, M=1 use x=i and remove only the shared Cartan scalar
from the positive crossing. In physical basis 00,01,10,11,

    R_+^E-R_+=-i |11><00|.                         (4)

Its original pivotal partial trace is zero. But use the literal
balanced closed-wire Ecal=-2|0><1| and pivot diag(-i,i).
The original first-input-zero/all-ones-output source gives

    ell ptr_g[(I tensor Ecal)(R_+^E-R_+)]e_0=2.    (5)

Restoring the common Cartan scalar multiplies this by the same
nonzero original scalar. The full regular complete dimension and
framing factors do not make it zero. Thus a single local
degree-minus-one coupon can expose a positive N-carry through
an off-diagonal first-cut row. One cannot replace the entire
Hopf/Ward source complex by the quotient in (3).

Global Hopf-adjoint partial-trace identities may still cancel
their complete sums, because all their coupled terms are kept.
Equation (5) says the individual local terms cannot be deleted.
Meridian M shifts and derivatives, in contrast, do not change
integer degrees, so the root-family equality (3) preserves
them. A moving-q normal needs the separate correction below.

## 3. An explicit generic-Q counterexample and repair

The same finite fusion kernel and Euler/path formulas are
well-defined matrices for generic Q, with F_1,...,F_(N-1) units.
They are not automatically a generic-q Hopf fusion. At N=2 the
Euler matrix calculated from those formulas is

    R^E(Q,x)=[[1,0,0,0],
              [0,0,x^-1,0],
              [0,x^-1,1-x^-2,0],
              [-x^-3,0,0,-x^-2]].

The actual generic-q compressed crossing has the same first
three rows but final row (0,0,0,Q*x^-2). Therefore

    R^E-R_actual=-x^-3 |11><00|
                      -(Q+1)x^-2 |11><11|.         (6)

Only the first term survives at Q=-1. Off root the second is
of degree ZERO and is visible to the full cut. With the same
original pivot diag(x^-1,Q/x), the cut difference is

    -Q(Q+1)x^-3 E_(1,1).

For the actual averaged all-ones source its first Q-normal
at Q=-1, with D_Q=Q partial_Q, is

    -1/(2x^3) !=0.                                (7)

Allowing x to vary with Q does not alter (7), since the source
difference itself vanishes identically in x at the root. This
is an explicit failure of the naive Euler extension to preserve
the actual whole q-normal germ, not just a missing proof.

The repair in this example is the RETAINED normal coupon

    R^sharp=R^E+(Q+1)x^-2 |11><11|,

after which R^sharp-R_actual has only positive carry. Calling
Q=-1 before taking the normal derivative would erase that
coupon and give the wrong source in (7).

## 4. General normal repair and bounded nilpotence at fixed jet depth

There is a direct matrix construction at every N. The generic
fusion kernel preserves its integer degree exactly, and the
right path matrix has only changes 0 or +N. Hence its generic
Euler matrix R^E(Q,x) has only these two grades. Write pi_0,
pi_>0 for those degree projections and set

    Delta_N=R_actual-pi_0 R^E,
    R^sharp=R^E+Delta_N
            =R_actual+pi_>0 R^E.                  (8)

Then R^sharp has the actual degree-zero part and the Euler
completion's positive-carry part for ALL Q on this chart.
The proof of (3) now applies to R^sharp before root
specialization, including its inverse and full normal jets.
This is not a claim that R^sharp is an uncorrected Euler
factorization or a full Hopf intertwiner.

Delta_N vanishes at every primitive Nth root by (1). In the
localized coefficient ring where intermediate factorials are
units, it is divisible by delta=1-Q^N:

    Delta_N=delta Z_N, Z_N regular there.          (9)

Indeed all proper-divisor cyclotomic factors of 1-Q^N are
already units; the remaining primitive cyclotomic factor
divides the regular matrix difference. The normalized original
crossing and the generic kernel here have rational Q,x entries;
the shared full Cartan line is retained separately on both sides.

At finite Q-normal depth J, work modulo delta^(J+1). In the
nonnegative N-graded matrix algebra the ideal

    j=(delta,n)

satisfies the uniform bound

    j^(b+J)=0.                                    (10)

Each term of a product of length b+J either contains at least
b positive carries or at least J+1 central delta factors. Thus
the actual-to-Euler correction lies in a unipotent group of
depth bounded independently of N at fixed b,J. Units and their
inverses are regular near the root. This is a useful bounded
transport statement for actual finite normal data.

The source DOES see the delta*Z_N terms, as (7) proves. They
must be carried as explicit normal coupons rather than
quotiented out. Nor does the bounded group depth bound their
coefficients or the actual word's exponential period: the
Euler factors and degree-zero word still depend on N. Local
E/F Ward insertions also require their complete transported
defects from Section 2. These qualifications leave the
geometric-period and global volume gates open.

## 5. Independent exact checks

[The audit](../experiments/audit_positive_carry_source_scope.py)
and [saved results](../experiments/positive_carry_source_scope_results.json)
pass 26 literal signed-word cases at braid indices 2,3,4,
levels N=2,...,5, and meridians M=1,3. They check both local
inverses, positive-degree support, the full first-cut matrix
and the retained original framing/dimension on regular charts.
The N=2 local E coupon is nonzero. An independent symbolic
generic-Q calculation proves (6)-(7) and the exact repair.
The grading and local-ring arguments above are all-level.
