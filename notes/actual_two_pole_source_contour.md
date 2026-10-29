# The selected endpoint source is a marked two-pole cycle

27 October 2026. The exact all-strand coefficient source has an ordinary
one-variable contour representative, with two nearby marked pole cycles.
Neither pole is an invariant by itself: a characteristic-zero actual
figure-eight braid calculation changes BOTH endpoint values under braid
conjugacy while leaving their difference unchanged. The coalescing-root
limit also has a precise cyclotomic boundary layer. Replacing it by one
ordinary double-pole contour loses even the constant source.

This gives a concrete contour input for gate C. It does not prove a
nonzero geometric thimble intersection. The final section records the
derived source-symbol test that a whole geometric comparison would need.

## 1. Exact contour of the original all-strand source

Use the canonical degree-<N endpoint polynomials from
[the original all-strand theorem](all_strand_euler_cauchy_cap.md), and
combine all tail heads BEFORE attempting a source limit:

    T_N(Z)=sum_lambda Q^-j B_lambda(Z),
    S_N=T_N(1)-T_N(Q^-1), Q=exp(2pi*i/N).

No unknown invariant is divided out in forming T_N. Its coefficients
are determined by the actual complete word, its actual fusion/Euler
frames and every off-diagonal tail transition. The original full
peripheral and framing line is retained in that theorem; in modulus
the reduced original invariant satisfies

    |Kashaev_N(K)|=N|S_N|/|1-Q|.                    (1)

Define the source differential

    omega_N(T)=T(z) dz/[z^N(1-z)(1-Qz)].           (2)

Its residue at zero is the original rational-kernel coefficient
functional. Since degree T<N, its order at infinity is at most -3,
so there is no residue at infinity. Its two other residues are

    Res_(z=1) omega_N=-T(1)/(1-Q),
    Res_(z=Q^-1) omega_N=T(Q^-1)/(1-Q).            (3)

Here both centers have z^N=1. Thus the global residue theorem gives
the EXACT all-level source identity

    Res_(z=0) omega_N
      =[z^(N-1)] T(z)/[(1-z)(1-Qz)]
      =[T(1)-T(Q^-1)]/(1-Q).                    (4)

Equivalently the small positive circle around zero can be deformed
to the negative sum of the two pole circles. The opposite signs
in their scalar periods come from the residues, not a choice to
discard one contour. Formula (4) is a representation of the existing
finite source, not the definition of a replacement state.

## 2. An actual braid conjugacy changes both endpoint values

At N=2 use q=i, Q=-1, x=i and eta=exp(pi*i/4). The original
balanced positive crossing, with its actual common Cartan line, is

    R_+=[[eta,0,0,0],
         [0,0,eta^-1,0],
         [0,eta^-1,2i eta^-1,0],
         [0,0,0,eta]].

Use its literal inverse, K=diag(i,-i), F_(1,0)=2 and the original
pivot K^-1. Form the original three-strand word, tail-head fusion
and right Euler conjugation from the all-strand theorem. Exact
matrix multiplication over Q(i,sqrt(2)) gives

    beta=(1,-2,1,-2),
    T_beta(Z)=-1+(5/2)Z,

    beta'=(1,1,-2,1,-2,-1)=sigma_1 beta sigma_1^-1,
    T_beta'(Z)=2+(5/2)Z.                          (5)

Both words have the same braid index and writhe, so all external
source, peripheral and framing factors agree. Their endpoint pairs are

    beta:   (T(1),T(-1))=(3/2,-7/2),
    beta':  (T(1),T(-1))=(9/2,-1/2).               (6)

Both endpoints change by three, while both differences are exactly
five, the same original reduced cut value. The change is a constant
polynomial, which the source (4) annihilates.

Thus neither individual endpoint can be identified with an intrinsic
marked knot period using only a scalar adapter depending on N, color,
braid index and writhe. The transported co-source or the complete
two-endpoint difference is required. This is an exact actual-word
countertest, not an arbitrary polynomial chosen to mimic a knot.

## 3. The pole collision has a cyclotomic boundary layer

There is a simple all-level warning against merging the two poles
before retaining the normal clock. For the constant polynomial one,

    [z^(N-1)]1/[(1-z)(1-Qz)]=0

at every original root, since this coefficient is
(1-Q^N)/(1-Q). If one sets Q=1 in that rational kernel first,
the same coefficient instead becomes

    [z^(N-1)](1-z)^-2=N.                          (7)

This is a failure of the premature specialization, not a failure
of the exact residue formula. The original source is normalized
on the cyclotomic relation Q^N=1 and must retain it through the
pole collision.

To see the correct normal geometry, put H=2pi*i/N and
z=exp(H xi). The two source poles are xi=0 and xi=-1 on their
local logarithmic lifts. The pullback of (2) is EXACTLY

    H T_N(exp(H xi)) exp(H xi) exp(-2pi*i xi)
       /[(1-exp(H xi))(1-exp(H(xi+1)))] dxi.       (8)

On compact xi charts away from 0,-1 this has the kernel form

    H^-1 exp(-2pi*i xi) T_N(exp(H xi))
           /[xi(xi+1)] * (1+O(H)) dxi.           (9)

The poles stay one unit apart, and the cyclotomic exponential
survives. A fixed-z double-pole model that omits these data is
not the source normal limit. In particular an ordinary residue
of the principal geometric framing density alone cannot decide
the selected endpoint class.

## 4. What a whole geometric source calculation would have to show

There is a precise local source-symbol criterion once a uniform
WHOLE asymptotic near the two endpoints has been proved. Let
D=z partial_z and suppose on a fixed complex neighborhood of one

    T_N(z)=H^alpha exp(S(z)/H)
                    [a_0(z)+H a_1(z)+O(H^2)],      (10)

with holomorphic S,a_0,a_1, uniform errors (including the required
derivatives), and a_0(1)!=0. This hypothesis concerns the complete
selected tail sum T_N, not one unsummed local geometric block.
Set mu=exp(-D S(1)). Direct Taylor expansion at z=exp(-H) gives

    S_N=H^alpha exp(S(1)/H)
       {(1-mu)a_0(1)
        +H[(1-mu)a_1(1)+mu D a_0(1)
                         -(mu/2)D^2 S(1)a_0(1)]
        +O(H^2)}.                                (11)

If mu!=1, the first coefficient is nonzero. If mu=1, the
principal coefficient cancels and the next source coefficient is

    D a_0(1)-(1/2)D^2 S(1)a_0(1).                (12)

The uniform Taylor expansion proves these formulas: write
S(exp(-H))=S(1)-H D S(1)+(H^2/2)D^2 S(1)+O(H^3)
and do the same for the amplitude. No contour or thimble
selection is assumed during that algebraic expansion.

If the first nonzero coefficient of the resulting derived source
series occurs at some fixed finite order, and (10) holds to that
order with controlled error, the original invariant has the same
exponential rate Im S(1)/(2pi). In particular a calibrated action
with Im S(1)=Vol(X) would imply the required volume rate. This is
a sufficient conditional source criterion, not a proof that (10)
holds for the knot state or that its derived coefficient is nonzero.

The source variable here is the right-Euler coefficient variable.
Its identification with a geometric framing or peripheral clock
is still required. Only AFTER such a marking could a classical
closure relation be used to assert mu=1. The actual source-wall
and fusion-orientation audit in
[the canonical-chart theorem](fusion_canonical_chart_and_retained_source_wall.md)
prevents making that substitution by inspection.

Thus the cycle problem is not settled by Rivin uniqueness: it must
transport the marked TWO-pole functional and establish its first
nonzero derived coefficient on the actual selected geometric
image. Exact finite source jets or the unsourced nonzero Gaussian
alone do not establish these hypotheses. No broad knot class is
proved here.

## 5. Exact checks

[The actual-source audit](../experiments/audit_actual_two_pole_source_contour.py)
and [saved results](../experiments/actual_two_pole_source_contour_results.json)
pass 15 literal signed-word cases, levels N=2,...,6, and three
same-index/same-writhe figure-eight braid conjugacies. The N=2
pair (5)-(6) is additionally checked by exact characteristic-zero
matrix multiplication. All original word, pivot, fusion and Euler
factors are used. Finite-field tests verify conventions; the
residue and boundary-layer proofs above are all-level.
