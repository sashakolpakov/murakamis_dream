# Actual shared quantum flags and their charged exchange

Research note, 28 October 2026. This derives an explicit quantum
flag exchange from the **original** finite crossing, including its
actual cup and marked cap. It is more than independent choices of
four Fermat frames: the flags below belong to the same quantum
meridians and are transported by the original crossing. The
result is a cleared quantum cross-ratio relation, with a compulsory
finite wall and even-level wrap sign.

It does not lift the three five-point certificates of
[the classical crossing cycle](crossing_fundamental_cycle.md) to
a complete quantum Pachner identity. In particular, no positive
geometric kernel or nonzero geometric coefficient is inferred.
The new calculation identifies exactly which finite relative
wall such a lift must preserve.

## 1. The actual quantum meridian

Use the original balanced factorial basis, with

    q=exp(pi*i/N), Q=q^2, d=N-1, rho=q-q^(-1),
    Z e_a=Q^a e_a, K=x Z^(-1), e=q rho^2 E, f=F.

Here E and F are the original nilpotent matrices. Introduce a
cyclic completion S_mu of the raising shift:

    S_mu e_a=e_(a+1) (a<d), S_mu e_d=mu e_0,
    S_mu^N=mu I, mu!=0.

Then, exactly,

    f=(1-Z)S_mu,
    e=(x^(-1)-K)S_mu^(-1)
                  -(x^(-1)-Qx)mu^(-1)|d><0|.       (1)

The first identity already has its original zero endpoint.
The second subtracts its one extra endpoint. Set

    L_+=[[K,e],[0,1]], L_-=[[1,0],[-Kf,K]],
    G=L_-^(-1)L_+=[[K,e],[fK,fe+K^(-1)]].          (2)

All entries are original finite matrices. The lower left entry
is fK, including its quantum ordering. Direct multiplication
using

    fe=c-QK-K^(-1), ef=c-K-QK^(-1),
    c=x^(-1)+Qx,

gives the ordinary matrix identity

    G^2-cG+Q I=0.                                (3)

The cyclic column is an exact relative eigenflag:

    G (1,S_mu)^t=x^(-1)(1,S_mu)^t
                      -(x^(-1)-Qx)(P_d,0)^t.      (4)

Thus its failure away from completeness is the original
(1-M^2) endpoint, with M=-qx. It has not been deleted.

At completeness x=-q^(-1), write lambda=x^(-1)=Qx and
k=x^N=(-1)^(N-1). The endpoint in (4) vanishes for every
mu. In particular, the same original e,f admit all these
completed flag marks. One has

    G-lambda I=(1,S_mu)^t(K-lambda)(1,-S_mu^(-1)),
    (G-lambda I)^2=0,
    [[1,0],[-S_mu,1]] G [[1,0],[S_mu,1]]
                                      =[[lambda,e],[0,lambda]]. (5)

The off-diagonal translation is the original nilpotent e.
Normalizing it to a unit by inverting e would annihilate this
finite module, since e^N=0.

## 2. Exact mixed-color Hurwitz transport

On two original heads define

    H_1=G_1, H_2=L_(-,1)^(-1)G_2 L_(-,1).

Let B be the original checked positive crossing from (x_1,x_2)
to (x_2,x_1). A superscript o denotes these output colors.
The common scalar Cartan line can be included in B or retained
externally; it cancels from each intertwining identity below.
There is no change to that line, the framing, the pivot, or the
peripheral normalization. At every level and nonzero colors,

    B H_1=H_2^o B,
    B H_2=H_2^o H_1^o (H_2^o)^(-1) B.             (6)

Here is a finite proof. Before the flip, write the original
crossing as R_0=D P(e_1 f_2), where

    P(z)=sum_(h=0)^d (-1)^h Q^(h(h-1)/2)z^h/(Q;Q)_h.

Since (e_1f_2)^N=0, its finite recurrence is

    P(Q^(-1)z)=(1-Q^(-1)z)P(z).

Cartan conjugation gives D e_1 D^(-1)=e_1 K_2 and
D f_2 D^(-1)=K_1^(-1) f_2. Therefore

    R_0 e_1=e_1 K_2 R_0,
    R_0 K_1=(K_1-e_1 K_2 f_2)R_0.                 (7)

After flipping, these are exactly the upper row of the first
identity (6). Its lower right follows from (3) and
fK=QKf. For completeness, its remaining lower-left error X
satisfies e'X=Xe'=0 by (3), where e'=e_2 K_1. At generic
colors, the original e_2 has one-dimensional kernel and
cokernel. Consequently X could only map a state (a,d) to
(u,0). Every lower-left term has integer total degree +1,
forcing u=a+N, which is outside the original head. Thus X=0.
Laurent continuation proves the exceptional-color identities
as well.

For the second identity, note

    H_2 H_1=(L_(-,2)L_(-,1))^(-1)L_(+,2)L_(+,1).

The original Hopf intertwiner preserves both displayed
coproduct matrices. Together with the first identity, this
proves the second. Thus the shared meridians themselves have
the actual quantum Hurwitz law, before taking a symbol.

## 3. The original complete crossing exchanges coupled flags

For the rest of the note both colors are complete. Choose
the convention that B has its original common Cartan scalar
kappa retained externally, as in coefficient (11). All
conjugation identities are independent of this convention;
the unstripped crossing has B_full p=kappa p in Section 5.
Choose
the two cyclic wrap marks to be

    S_1^N=mu I, S_2^N=k mu I.                     (8)

From this section onward, B denotes the original checked
crossing with its common Cartan scalar kappa retained in
the unchanged external line: the full crossing is kappa B.
The conjugation identities are insensitive to this
convention, while the cup identity in Section 5 reads Bp=p
and therefore (kappa B)p=kappa p for the full crossing.

The second mark is compulsory: it is not generally mu when
N is even. Let S_1,S_2 act on the first and second original
head and put

    t_1=S_1,
    t_2=f_1+K_1^(-1)S_2,
    Delta=t_2-t_1=Z_1(lambda S_2-S_1),
    gamma=(K_2-lambda)S_2^(-1)K_1=-e_2K_1,
    v=Z_2^(-1)+S_1e_2.                           (9)

The column (1,t_2)^t is L_(-,1)^(-1)(1,S_2)^t, so these
are flags of the shared H_i of Section 2, rather than four
independently chosen lines. The original crossing satisfies

    B S_1 B^(-1)=t_2,
    B S_2 B^(-1)=lambda S_1 v^(-1).               (10)

In particular, (10) supplies an explicit generator for the
flag transport; its right side does not contain an unknown
conjugated crossing kernel.

Here is a coefficient proof, including its endpoint. The
original coefficient from (a,b) to (b+h,a-h), after stripping
only its common external Cartan scalar, is

    r(a,b,h)=x^(-a-b-h)Q^(ab-(b+1)h)
                   F_a F_(b+h)/(F_(a-h)F_b F_h),
    F_j=(Q;Q)_j, 0<=h<=min(a,d-b).                (11)

This follows directly from the original E coefficient and
Cartan diagonal, using Qx^2=1. Its two finite Pascal
recurrences are

    r(a+1,b,h)=(1-Q^(b+h))r(a,b,h-1)
                                  +lambda Q^(b+h)r(a,b,h),

    Q^(-(a-h))r(a,b+1,h)
      +(lambda-xQ^(-(a-h)))r(a,b+1,h-1)
                                             =lambda r(a,b,h). (12)

Illegal transfer indices are zero. In the interior these
follow simply by dividing successive factorial products.
The first recurrence is B S_1=t_2 B. The second is

    v B S_2=lambda S_1 B.                        (13)

At a=d, the first wrap row equates
mu x^(-b) to mu_2 k^(-1)x^(-b). At b=d, the second
wrap row equates mu_2 x^(-a)Q^(-a) to
mu k^(-1)x^(-a)Q^(-a). The other terms in the first
endpoint row cancel by the first recurrence with F_N=0.
For the second endpoint row, the nonzero wrapped input
coefficients have
r(a,0,h)/r(a,0,h-1)=x(1-Q^(a-h+1)); substitution gives
the required adjacent cancellation directly. Both rows therefore
hold precisely for mu_2=k mu, since k^2=1. These are the
original endpoint rows, not cyclic replacement crossings.
Finally v^N=1, as shown below, so (13) implies (10).

Freezing both wraps to one at even N fails (10): even a
single original crossing detects the missing wrap sign.

## 4. Cleared quantum cross-ratio and finite collision wall

The following identities are exact in the original finite
matrix algebra:

    Delta gamma-Q gamma Delta=lambda(Q-1),
    v=1+lambda^(-1)Delta gamma,
    Delta v=Q v Delta,
    v^N=1, Delta^N=gamma^N=0.                    (14)

For example, put a=S_1,b=lambda S_2. They commute, and
Delta=Z_1(b-a). With
gamma=(xZ_2^(-1)-lambda)b^(-1)Z_1^(-1), direct
multiplication gives the first two identities. The third
then follows from the first. In v, the summands
Z_2^(-1) and S_1e_2 Q-commute, with N-th powers 1 and 0,
respectively, proving v^N=1. In Delta, the two summands
Q-commute, and their root binomial powers give

    Delta^N=lambda^N(k mu)-mu=0.

The identity gamma=-e_2K_1 immediately gives gamma^N=0.

Let t_3=B t_2 B^(-1). Since the original B preserves
F_tot=f_1+K_1^(-1)f_2 and K_tot=K_1K_2, equation (10)
gives

    t_3=t_2-Q Delta v^(-1).                      (15)

Indeed t_2=F_tot+x K_tot^(-1)S_2, so substitution of
(10) reduces (15) to S_2v-Q Z_2^(-1)S_2
+lambda Z_2^(-1)S_1=lambda S_1. This is just the
original complete formula for e_2. Thus the four shared
flags obey the **cleared** ordered cross-ratio identities

    v(t_3-t_2)=t_1-t_2,
    (1-v)(t_3-t_2)=t_3-t_1.                      (16)

The mnemonic fraction
(t_3-t_1)(t_3-t_2)^(-1)=1-v would require an inverse of
t_3-t_2. It is **not defined or asserted in this finite
module**. Equation (16) is the actual cleared relation;
no difference was inverted to prove it. Equivalently, the
Möbius denominator for H_2(1,t_1)^t is exactly

    (H_2)_11+(H_2)_12 t_1=xv,                   (17)

which is invertible, with N-th power x^N. Thus the relevant
transport does not fail because of its Möbius denominator.
It fails to belong to an ordinary generic cross-ratio field
because Delta, and hence t_3-t_2, is nilpotent.

This is a precise obstruction to a direct generic five-flag
field lift: localizing this actual finite module at Delta
gives the zero module. The same applies to inverting e in
(5). It does not obstruct an identity first established in
a tagged generic module and then compressed with a retained
relative source, or a contour/residue construction that
keeps this collision wall. Such a construction is still
needed for the three classical certificates.

## 5. The original cap selects the charged wall with unit pairing

At completeness the actual dual color is again x. The
original left cup and averaged marked cap, in the same
balanced basis used above, are

    p=N sum_(a=0)^d x^(a-d)|a,d-a>,
    m|a,b>=x^b/N^2, m p=1.                      (18)

They retain their original scalar factors. The full exterior
Cartan, framing and peripheral line multiply both sides as
before; they have not been assigned new values. Directly,

    Bp=p, Delta p=0, vp=Qp,
    (D+1)p=Np, D=J_1+J_2.                       (19)

The first identity follows as well from the original Hopf
cup intertwiner and its zero-transfer coefficient. For a
direct check of Delta p, the ordinary raising terms cancel
using lambda x=1. The two exceptional (0,0) terms cancel
using mu_2=k mu and x^N=k. For v, on the degree-d fiber
its diagonal is Q^(a+1) and its raising entry is
lambda(1-Q^(a+1)); the ratio p_a/p_(a-1)=x gives vp=Qp.

Define its exact spectral projectors by

    E_j(v)=(1/N)sum_(r=0)^d Q^(-jr)v^r.

Then the original, full marked pairing satisfies

    m E_j(v) p=delta_(j,1),                     (20)

for every N, including N=2. Hence the collision is not an
auxiliary source choice or an unmarked matrix singularity.
The actual source lands on v=Q, and this wall has pairing
one. In a classical limit v tends to 1 on this cup and
the corresponding 1-v cross-ratio tends to 0. This describes
the **cap** wall; it does not say that a bulk geometric
tetrahedron in an entire closed word must degenerate.

The finite integer carry is also explicit. Write B_i for
|0><d| on head i. Then

    [D,Delta]=Delta-N Z_1(lambda k mu B_2-mu B_1),
    m Z_1 lambda k mu B_2 p=m Z_1 mu B_1 p=mu/N. (21)

Thus the signed endpoint currents cancel on the cup, while
each original endpoint has nonzero augmented weight. A
cyclic congruence or the cancellation of the two currents
does not erase this wall. The separate identity (D+1)p=Np
retains the actual affine charge. Equation (21) does not
by itself identify that cap charge with a Pachner internal
edge winding; the required typed gluing of the five-point
move remains to be constructed.

Equations (6), (10), and (16) can be composed at every
crossing of an arbitrary bridge or braid word, with its
actual cups and caps. They provide closed local shared-flag
updates and the exact boundary ideal (19), rather than an
assumed scalar preservation under a hypothetical tetrahedral
kernel. They do not prove that the three quantum five-point
moves preserve that boundary ideal after a change to a
positive triangulation chart.

## 6. A finite mixed cyclic/nilpotent two-to-three identity

There is a constructive local identity on precisely these
original heads. It uses the same literature cyclic atom as
[the four-atom note](four_cyclic_atoms.md), not a new
definition of a quantum invariant. For an auxiliary parameter
t with t^N!=1 retain the marked root nu^N=1-t^N and set

    C_t=mathfrak_d_N(tv;Q),
    mathfrak_d_N(z;Q)=(1-z^N)^((N-1)/(2N))
                      product_(j=1)^d(1-Q^j z)^(-j/N),
    P(A)=sum_(h=0)^d (-1)^h Q^(h(h-1)/2)A^h/F_h. (22)

The functional calculus is well defined because v^N=1.
All roots, including the half roots needed at even N, are
anchored at t=0 and then continued together. Thus C_t is
the actual determinant-normalized literature atom, including
its scalar and root marks. Its finite functional equation is

    mathfrak_d_N(Qz;Q)/mathfrak_d_N(z;Q)
                                              =nu/(1-z).

Using Delta v=QvDelta gives

    C_t Delta C_t^(-1)
                     =nu^(-1)Delta(1-Q^(-1)t v). (23)

For every scalar a there is consequently the exact finite
two-to-three identity

    C_t P(aDelta)
      =P(a nu^(-1)Delta)
          P(-a nu^(-1)Q^(-1)t Delta v) C_t.       (24)

To prove it put X=a nu^(-1)Delta and
Y=-a nu^(-1)Q^(-1)t Delta v. Then XY=QYX. The
finite Q-binomial theorem with this ordering gives
P(X+Y)=P(X)P(Y). Every term of total Delta-degree >=N
vanishes, including the apparent extra degrees in the
product on the right. Equations (23) and this polynomial
identity prove (24) at the actual root; no individual
infinite compact product is specialized. The same retained
cyclic atom C_t, with exactly the same determinant and
root scalar, occurs once on each side.

This identity is boundary compatible in a literal sense:

    C_t p=mathfrak_d_N(tQ;Q)p,
    P(aDelta)p=P(-a nu^(-1)Q^(-1)t Delta v)p=p,

    m C_t P(aDelta)p
      =m P(a nu^(-1)Delta)
             P(-a nu^(-1)Q^(-1)t Delta v) C_t p
      =mathfrak_d_N(tQ;Q).                       (25)

The factor in (25) has not been replaced by one. Each side
also retains the original common exterior scalar line.
After dividing the **equality** by its same displayed
factor, both sides are the original marked unit pairing;
this is a check of source transport, not a redefinition of
the original invariant. At t^N=1 the separate nu^(-1)
factors cannot be evaluated. The whole source comparison
in (25), with its displayed common factor, is the retained
relative expression. Its quotient is identically one and
extends as such. An independent insertion of C_t into a
closed invariant would change its value; (24) authorizes
replacing a specified local factor product by its equal
product, with the exterior source left intact.

Thus there is an all-level mixed cyclic/nilpotent 2<->3
identity on the actual coupled quantum flags, preserving
their charged cap ideal and source factor. The auxiliary
t has not been identified with a geometric tetrahedral
edge parameter. In particular, (24) alone does not exhibit
the factor products of the three classical certificates
inside the actual four-atom crossing word. That specific
identification, together with its shared flags and all
central factors, is the next missing local equality.

## 7. What is new, and what remains on the critical path

The existing [four cyclic atoms](four_cyclic_atoms.md) and
[Verma transport](verma_tetrahedral_transport.md) already
prove compact-dilogarithm factorizations and generic/tagged
pentagons. The [classical crossing cycle](crossing_fundamental_cycle.md)
already identifies the shared shadow octahedron and gives
its three five-point certificates. The
[four-line Fermat calculation](actual_four_line_fermat_crossing_and_conditioning.md)
already gives independent coherent-frame matrix elements.

The additional result here is an explicit **actual** coupled
quantum flag/Ptolemy update (10), (14)--(16), including its
typed even-N wrap, the original selected wall (18)--(21),
and the mixed finite identity (24) on these same heads.
It neither chooses new independent face flags nor merely
renames a conjugation of the crossing. It supplies algebraic
relations and a boundary ideal that any claimed lift of
the three classical certificates can now be tested against.

The missing local theorem is still a refactorization of
those certificates with this finite collision source and
all central/root factors retained. No resulting positive
geometric kernel, geometric intersection coefficient, or
volume estimate is asserted here.

## 8. Reproducible exact audit

Run

    python3 experiments/audit_actual_shared_quantum_flags.py

The independent evaluator starts from the original E
coefficients and Cartan diagonal, rather than (10). It checks
21 mixed-color quantum Hurwitz families, 21 complete
typed shared-flag families, all projectors (20), and four
even-level frozen-wrap failures, for N=2,...,8 over exact
prime fields. It additionally checks 42 identities (24)
at nonzero finite-field Fermat parameters t^N+nu^N=1,
including their literal source factors. This test uses the
cyclic functional equation to construct a scalar
representative of C_t. Identity (24) is homogeneous in
that same scalar on both sides; the proof (22)--(24)
retains the actual determinant-normalized atom and its
marked roots. The audit also checks the original cup,
marked pairing, and affine charge. The all-level proofs are the
finite recurrences and matrix identities above, not an
extrapolation from these tests.
