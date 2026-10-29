# The original plat source has explicit cup/cap Gram supports

28 October 2026. For EVERY fixed actual 2k-head plat word, the original
scalar has an exact matrix-element presentation between two specified
positive pure states, with a unitary pivot and explicit polynomial
normalization. No period is divided out and neither state is chosen
to favor a geometric saddle.

The transported cup state satisfies the actual incoming inverse-meridian
constraints exactly. The cap state has the outgoing inverse-meridian
constraints in mean square with O(N^-2) error. Hence their positive
moment limits have the two honest compact braid/cap supports. Their
intersection satisfies precisely the plat representation relations
within this bounded star-character space. It is not asserted to exhaust
the unrestricted representation variety.

The overlap need not have nonzero limiting mass. No exponential overlap
estimate, joint atomic-shape comparison or volume bound is inferred.

## 1. Exact ORIGINAL source, after its permitted whole-degree restriction

Use N>=2, d=N-1, q=exp(pi*i/N), Q=q^2 and x=-q^(-1), with the
original balanced basis and actual pivot g_i=x^(1-N)Q^(-i). On a
standard neighboring primal/dual pair the original left cup p and
ordinary right cap l are

    p_(i,j)=N x^(-j) delta_(i+j,d),
    l_(i,j)=x^j g_i/N delta_(i+j,d).

Since |x|=1,

    l=N^(-2) p^* G, G=diag(g on the primal leg).       (1)

Both the N and 1/N are the literal actual turn normalizations. The
full original marked cap is m_(i,j)=x^j/N^2, with NO degree delta.
It is not changed termwise in an arbitrary decomposed tensor.

Put u=p^(tensor k). It has total INTEGER degree kd. Every ORIGINAL
crossing preserves that degree, so the fully assembled W u still has
degree kd. The k-1 ordinary top caps force degree d on each of their
pairs. Consequently the last MARKED pair also has degree d in the
whole scalar pairing. On that specific degree-d subspace,

    m=N^(-3)p^*.                                     (2)

Thus with any chosen marked pair r_*, the exact originally pointed
plat scalar is

    P_N=chi_N N^(-2k-1) <u,G_top W u>,
    G_top=product_(r!=r_*) diag(g on primal leg of pair r). (3)

Here chi_N is the unchanged original external line, including whatever
framing/full peripheral convention has been specified. No component
of g or chi_N is reset. Formula (3) uses integer-degree conservation
BEFORE the marked-cap restriction. The replacement (2) is not asserted
for arbitrary degree-changing coupon insertions or for separated
nonconserving current sectors.

In the actual flat metric ||p||^2=N^3, so ||u||^2=N^(3k). Define

    uhat=u/N^(3k/2), phihat=G_top^* uhat.

The pivot is unitary, and g=x^(-N)K on each primal head. Hence G_top
is a fixed-degree bounded polynomial in the original Cartans, with
its exact parity phase retained. Equation (3) becomes

    P_N=chi_N N^(k-1) <phihat,W uhat>.               (4)

This is an exact same-source scalar identity, not positivity of a
pivotal trace. The states here are fixed by the actual turns.

## 2. The actual inverse-meridian equations of every cup

Let the bounded physical based quantum meridians H_j and their exact
transport be those of
[the all-word theorem](actual_bounded_quantum_meridian_transport.md).
Define, as a two-by-two matrix of physical operators,

    A_r=H_(2r)H_(2r-1)-I, 1<=r<=k.                  (5)

EVERY entry of A_r annihilates u exactly. Here is a direct proof.
On the local pair the actual cup obeys

    E_tot p=0, F_tot p=0, K_tot p=p.

The two product matrices L_(-,2)L_(-,1) and L_(+,2)L_(+,1) therefore
act as the identity on each auxiliary component of p. Their ratio
is precisely the local H_2 H_1, so its difference from I kills p.
For a later pair the global based product is P^(-1)(H_2 H_1)P,
where P consists only of earlier heads. Its matrix entries commute
with the local pair's entries. Thus each term of the difference still
annihilates that cup, irrespective of the state on the earlier heads.
This proves (5) for the full tensor u, with the original ordering.

The total product T=H_(2k)...H_1 also acts as I on u and is preserved
by W. Its preservation follows from the original total E,F,K Hopf
intertwining, equivalently the preserved products of L_+ and L_-.

Let

    psi_N=W uhat/||W uhat||.

It exists for EVERY N because W is invertible and uhat is nonzero;
no assumption on the scalar pairing (4) is required. Define

    A_(r,W)=W A_r W^(-1).

All of these are the N-uniformly bounded Nielsen polynomials already
proved in the physical-meridian theorem, and

    A_(r,W) psi_N=0, (T-I)psi_N=0.                   (6)

Thus for the POSITIVE pure Gram state of psi_N,

    <psi_N,A_(r,W)^* A_(r,W)psi_N>=0                (7)

entrywise, exactly at each level. These are the actual transported
bottom cup constraints, not a newly imposed classical graph.

## 3. The actual top cap has controlled mean-square support

The cap state in (4) is phihat=G_top^* uhat. Since A_r uhat=0,

    A_r phihat=[A_r,G_top^*] uhat.                   (8)

All entries of A_r and G_top are fixed-degree polynomials in the
actual bounded scaled head observables. Their star commutators
have the proved norm bound C_k/N. Therefore

    ||(A_r)_(ab) phihat||<=C_k/N,
    <phihat,(A_r)_(ab)^*(A_r)_(ab)phihat><=C_k^2/N^2. (9)

This includes the marked pair: it has no pivot of its own in G_top,
but pivots on earlier heads can enter its based prefix. Equation (8)
handles them rather than treating the based constraint as a local
unbased one. The estimate is independent of W and does not replace
the original marked source before its permitted whole-degree use.

The stronger exact cap-row equations for ordinary top caps are also
consistent with (9); they are not needed to infer support here.

## 4. Positive limits and the honest plat intersection

The all-word bound supplies a common finite bounded star family for
H_j, all W H_j W^(-1), their entries and adjoints. Their commutators
are O(1/N). Consequently subsequential moment limits of the two
positive pure states have compact commutative realizations as in the
physical-meridian theorem.

At every character write h_j for the SL2 matrices determined by H_j;
the physical meridians are -h_j and have trace two. The limiting cup
measure is supported by

    phi_W(h_(2r))phi_W(h_(2r-1))=I for all r,
    h_(2k)...h_1=I,                                 (10)

where phi_W is the EXACT Nielsen word read contravariantly from the
actual W. This follows from the zero mean squares (7). The cap
measure is supported by

    h_(2r)h_(2r-1)=I for all r,                       (11)

by (9). No positivity of the original pivotal closing is assumed.

The intersection of (10) and (11) is the subset of the bounded character
space satisfying the honest plat representation relations, including
degenerate/central meridians. To verify the group
statement, take free meridian generators at the braid's top. Each
top cap identifies its two oriented meridians as inverses, giving
(11). Pull the bottom meridians through the literal braid Hurwitz
words; its bottom caps then give precisely (10). These are exactly
the Wirtinger/van-Kampen identifications of the plat diagram. The
total product relation is redundant once all adjacent cap products
are I, but it is genuinely retained by the quantum source as well.

For a one-component knot any noncentral trace-two meridian has
parabolic centralizer, so its commuting peripheral image is
boundary-parabolic. If it is central in PSL2, normal generation
makes the representation trivial. Hence the sharp representation
volume bound applies to every representation in this intersection.
This is not yet a claim that its joint atomic shapes have the
saturated critical regulator values.

## 5. A bounded overlap limit also has this intersection support

There is a further statement which does not assume a nonzero overlap.
For any fixed polynomial observable F in that bounded star family set

    omega_N(F)=<phihat,F psi_N>.                      (12)

Its norm is at most the operator norm of F. Polarization expresses it
as a linear combination of four positive vector Gram functionals of
phihat+i^j psi_N, whose norms are at most four. Their subsequential
compact commutative realizations from Section 4 therefore give a
bounded complex measure for (12), possibly the ZERO measure. From
(6) we have omega_N(F A_(r,W))=0.
From (9), <phihat,A_r^* F psi_N>=O(1/N); commuting fixed-degree
observables changes this by O(1/N). Consequently the limit annihilates
every polynomial multiple of A_(r,W) and A_r^*. Including all adjoints
and using continuous approximation shows that it is supported on the
intersection (10)-(11). There is no division by omega_N(1) or P_N.

These moments belong to the exact scalar representation (4).
They are not asserted equal to old marked-cap moments after arbitrary
degree-changing coupon insertions, for which (2) need not hold.

The distinction from an exponential theorem is essential. From (4),

    |P_N|=|chi_N| N^(k-1)||W uhat|| |omega_N(1)|.     (13)

The overlap can be exponentially small, and every fixed-degree moment
in (12) can then tend to zero. The separate positive cup and cap
measures do not create a normalized overlap measure or a nonzero
intersection coefficient. Dividing by that small overlap would
destroy the uniform moment bound just proved. No claim is made that
the discrete-faithful point lies in this real compact intersection.
Complex stationary deformation and its original source still matter.

The new unconditional result is the SAME original scalar's explicit
cup/cap support and bounded overlap-support statements, for all
widths and words. A sharp upper bound still needs exponential
control of that overlap and of the associated atomic regulator at
singular shape charts. A volume lower bound also needs nonzero
geometric selection. Neither conclusion is inferred here.

[Audit](../experiments/audit_actual_plat_gram_support.py): exact full
marked-source reduction, all cup and transported constraints, retained
total product and pivots, plus direct flat-complex mean-square cap
bounds. Both crossing signs and marked-pair locations are retained.
