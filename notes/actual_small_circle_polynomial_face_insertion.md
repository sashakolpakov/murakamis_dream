# A small untwisted circle is an exact polynomial face operator

30 October 2026. At one actual
untwisted port, the complete sum of the original small-color paths
preserves the polynomial face ring. Its physical endpoint zeros cancel
the negative powers that occur in individual path or clock terms.
Consequently the whole source still selects one coefficient, with no
level-shift aliases. A fixed-positive-radius bound costs only C^(h-1).

The port has distinct unmarked input/output middle faces, and its literal
identity smoothing is connected with the two original marked faces still
distinct. Multiple small ports, a marked middle face, and a retained
crossing at the replaced port are not included in this theorem.

## 1. The original operator and its endpoint factors

Put N>=3, d=N-1, q=exp(pi i/N), Q=q^2. Keep the original complete
physical module and balanced basis. The external circle operator is

    L_h=(-1)^(h-1) P_(h-1)(Omega), 1<=h<=N,
    P_0=1, P_1=X, P_(r+1)=X P_r-P_(r-1).             (1)

These are the actual operators of the
[external reflection theorem](actual_external_circle_reflection_and_cusp.md),
not their eigenvalues on a selected channel. Write U=Q^u,V=Q^v for
the two INPUT physical indices. Directly from the original coproduct,
Omega has diagonal and upward/downward transition coefficients

    D(U,V)=2q U+2q^-1 V^-1-(q+q^-1)U/V,
    A_+(U,V)=(V^-1-1)(1-Q U),
    A_-(U,V)=(Q^-1 V^-1-1)(1-U).                    (2)

Here A_+ sends (u,v) to (u+1,v-1), and A_- sends it to
(u-1,v+1). Formula (2) is valid for every physical total, including
the high blocks. For example expanding F_12 Ecal_12+qK_12+q^-1K_12^-1
gives (2) directly, with no low-block reflection.

One may use cyclic shifts modulo N in (2) EXACTLY: A_+ is zero at
u=d or v=0, and A_- is zero at u=0 or v=d. Hence any cyclic path
that attempts to leave the physical square has zero weight at its
first illegal step. Every power and the polynomial (1) therefore
retain the original unwrapped endpoints. This is a root statement;
it does not differentiate a root-periodic operator in generic q.

At the chosen original port let x,b,c,y be its ordered outer,
incoming-middle, outgoing-middle and final face variables. In the
literal convention of the
[complete-circle factorization](actual_complete_circle_positive_face_polynomial.md),

    S=d/2+N(Log x-Log b)/(2pi i),
    R=d/2+N(Log x-Log c)/(2pi i).

Thus p=R-S (OUTPUT minus INPUT FIRST head) gives c=Q^(-p)b.
The alternative formula c=Q^p b uses input-minus-output, or the
opposite second-head displacement. These conventions must not be mixed.
In particular U=-q^-1 x/b and V=-q^-1 b/y.

## 2. The exact polynomial operator

Temporarily retain b and c as independent variables. Let T act on
polynomials in c, with every other original face variable fixed.
The unmarked bounded middle face c is distinct from either outer
face x,y in the literal Morse region chart, so this prescription is
well-defined. The outer labels x=y are allowed and substituted literally:

    T f(c)= -q^-1[1+q(x+y)/c+q^2 xy/c^2]f(Q^-1 c)
            -q[1+q^-1(x+y)/c+q^-2 xy/c^2]f(Q c)
            +[2(x+y)/c+(q+q^-1)xy/c^2]f(c).          (3)

Despite the displayed denominators, T preserves the POLYNOMIAL ring.
Indeed for each integer j>=0,

    T c^j = a_j c^j+b_j(x+y)c^(j-1)+e_j xy c^(j-2),
    a_j=-(q Q^j+q^-1 Q^-j),
    b_j=2-Q^j-Q^-j,
    e_j=q+q^-1-q Q^-j-q^-1 Q^j.                    (4)

The term with b_0 vanishes, and e_0=e_1=0. Thus no negative power
occurs. T also preserves total homogeneous degree in ALL face variables.
Define

    T_1=I, T_2=T, T_(h+1)=T T_h-T_(h-1).            (5)

Every T_h preserves polynomials and their homogeneous degree.

Here the phases in (3) are essential. For L_2=-Omega, substitution
of the actual clocks into (2) gives the three path weights

    l_0=2(x+y)/b+(q+q^-1)xy/b^2,
    l_+=(1+q x/b)(1+q y/b),
    l_-=(1+q^-1 x/b)(1+q^-1 y/b).                   (6)

The WHOLE remaining source supplies the factor q^(pd) for a path
with displacement p. Since q^d=-q^-1, the weighted shifts in (6)
are exactly (3), evaluated at c=b. For several successive steps,
the current middle clock is Q^(-p)b, so the ordered path weights
are exactly the successive applications of T. The physical
Chebyshev recurrence (1) gives (5). This argument uses the original
path product before expanding its endpoint factors; it does not discard
forbidden paths one Laurent monomial at a time.

## 3. Whole-source coefficient and the retained measure

Fix a connected original plat with R complete-circle ports and its
literal unrestricted main mark. Replace just the chosen untwisted
port by L_h. All other ports retain fixed folded labels a_i and
their original half-twist phases omega_(a_i)^epsilon_i. Assume b,c
are distinct unmarked faces, and that deleting this port leaves a
connected flat projection. The literal identity smoothing merges b,c;
its two original marked faces u,v remain distinct.

Let P_rem be the product of the R-1 remaining positive circle
polynomials D_a D_a Ptilde_s, retaining their original face incidences
and keeping b,c independent. Define the polynomial on the smoothed
face graph

    Q_h(L)=[T_h P_rem(L)]_(c=b).                     (7)

It is homogeneous of degree d(R-1). It need not have positive
coefficients. Let F_sm be the R-1 faces other than u,v after merging.
The actual fixed-sector small-circle contribution is EXACTLY

    A_(N,a;h)=N^(R-1) product_(i!=port)
       [k_(a_i) beta_(a_i)^2 omega_(a_i)^epsilon_i]
       [product_(f in F_sm)L_f^d] Q_h(L)|_(L_u=L_v=0). (8)

Every cup, ordinary cap, exterior phase and the original mark are as
in the [marked coefficient theorem](actual_original_marked_face_coefficient.md).
Any separately recorded exterior framing unit multiplies both sides.

To prove the phase used in section 2, first use the exact full-source
monomial of that theorem BEFORE merging. Removing the chosen complete
coupon removes its two middle denominators, so the remaining scalar
face factor is

    N^-1 product_(i!=port)[k_a beta_a^2 omega_a^epsilon]
        (bc)^(d/2) product_(f!=u,v)L_f^(-d).          (9)

Since b,c are unmarked, c=Q^(-p)b converts their part to
q^(pd)b^(-d), exactly. No root clock or half-integer power has been
reset. This proves (3) with its true scalar and chosen direction.

For fixed paths at the small port, sum over the remaining primitive
face grid. All surviving complete coupons enforce their original
unwrapped support, and (2) enforces the small port's physical endpoints.
The chosen path specifies c=Q^(-p)b; the input and output middle faces
have the same even-level parity, so this relation respects the original
coset. Summing paths gives (7) on the smoothed grid. The globally
assembled exponents are integers, and the remaining carry signs cancel
by the same integral face-flow argument, with the displacement p fixed.

There are N^R smoothed grid points. A monomial of Q_h survives that
average only if its exponent is 0 modulo N at the marked bounded
face and d modulo N at every face in F_sm. POLYNOMIALITY and total
degree d(R-1) force the unique possibility: exponent zero at both
marked faces and exactly d at every face in F_sm. No coefficient
positivity is needed for this argument. The even coset multiplier at
that exponent is one. Combining N^R with N^-1 in (9) proves (8).

Individual clock or diagonal-path pieces can have genuine whole-N
aliases. It is the exact sum (3)--(5), including both off-diagonal
bands, that cancels their negative powers and restores this argument.

## 4. A fixed-positive-radius cost of C^(h-1)

Give EVERY smoothed face a fixed positive value l_f, including u,v.
Give the two unmerged variables b,c that same value l_b. For a
polynomial P write ||P||_l=sum_n |P_n|l^n. From (4),

    ||T P||_l <= A(l)||P||_l,
    A(l)=2+4(l_x+l_y)/l_b+4l_x l_y/l_b^2.            (10)

Thus (5) implies

    ||T_h P||_l <= [A(l)+1]^(h-1)||P||_l.            (11)

The elementary induction retains the subtraction in (5); it bounds
its norm rather than asserting positivity. Merging two variables of
equal positive weight cannot increase this weighted coefficient norm.
Since P_rem has nonnegative coefficients,
||P_rem||_l=P_sm(l), where P_sm is the original identity-smoothed
positive polynomial. Coefficient extraction in (8) therefore gives

    |[L^(d F_sm)]Q_h|
       <= [A(l)+1]^(h-1) P_sm(l)/product_(f in F_sm)l_f^d. (12)

This avoids separate estimates of shifted targets or their modular
aliases. Equivalently, the finite lowering expansion changes each
ordinary exponent by at most 2(h-1), with total displacement bounded
by 4(h-1), only AFTER its exact polynomial cancellations.

At fixed l, all remaining label weights are the original ones. Sum
their absolute values and use the existing uniform all-label circle
rate bound. If the identity-smoothed coefficient bound at these SAME
positive variables has a strict gap g below the original volume rate,
then the whole one-small-port source has that gap up to
(h-1)log[A(l)+1]/N and o(1). In particular h=O(sqrt N) has no rate
cost, and sufficiently small h<=delta N preserves a strict gap.
The marked variables may be chosen fixed positive as in the
[fixed-radius smoothing bound](actual_smoothing_fixed_radius_gap.md);
their targets remain zero. They are not set to zero before (12).

This implication requires an established compatible smoothing gap.
It does not assert that every smoothing has one. Nor does it cover
several deleted ports, a marked middle face, disconnected smoothing,
or an R^epsilon crossing retained at the small port. Those cases need
their own exact scalar, incidence and endpoint analysis.

## 5. Focused source verification

The [focused audit](../experiments/audit_actual_small_circle_polynomial_face_insertion.py),
with [saved results](../experiments/actual_small_circle_polynomial_face_insertion_results.json),
checks seven symbolic operator/endpoint identities, 15,316 actual
coproduct entries and 154 physical endpoint zeros. It compares 1,512
literal L_h path pairings with polynomial monomials, including 504
high-total cases. The whole-source check compares 139 actual marked
fixed-sector contractions with (8), for every h=1,...,N in its
fixtures, both level parities and both original mark positions. It
includes width two and three, maximal/mixed/zero folded channels,
and the other ports' retained half twists. The 121 surviving modular
monomials all have the unique asserted target. These checks concern
the original finite tensors; the all-diagram identity and norm bound
are the preceding analytical arguments.

The face-insertion theorem does not include multiple, marked-middle or signed small ports.

The theorem retains its one-port scope.