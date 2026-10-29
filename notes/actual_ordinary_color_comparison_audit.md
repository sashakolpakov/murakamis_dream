# Independent audit of the ordinary-color identification

28 October 2026. This checks the two representation comparisons needed
before applying the positive path trace in
[the regular-period note](regularized_kashaev_period.md#2-a-positive-trace-bounds-all-the-ordinary-colors).
Neither comparison assumes a published colored-Jones or ADO comparison
proof. They are exact finite-matrix statements, including the Cartan
scalar and zero framing. The positive path trace itself is a separate
algebraic step.

The conclusion is that, for a **one-component** zero-framed closure of a
fixed b-strand braid and every 1 <= j < N,

    F_N^M(-q^j) = F_N^Y(Q^j) = C_j(q),
    C_j(q) = theta_j^(-w) tau(P rho(cable(word)) P)/[j],
    q=exp(pi*i/N), Q=q^2, theta_j=q^((j^2-1)/2).         (1)

The coordinate superscripts in (1) are essential. In
`root_orbit_pointing.md`, the reduced family is a function of
M=-q x=-q^(alpha+1); here it is denoted F_N^M(M). In
`regularized_kashaev_period.md`, the symbol F_N denotes its even
descent to Y=M^2; here that function is denoted F_N^Y(Y). Thus

    F_N^M(M)=F_N^Y(M^2),
    alpha=j-1 <=> x=q^(j-1), M=-q^j, Y=Q^j.

In particular one must NOT insert -q^j into the Y-coordinate function.
The complete point is M=1, Y=1. All these are reduced periods;
the full modified-dimension factor can have poles at the ordinary
orbit points and is not asserted polynomially bounded there.

For an independent check that this descent is legitimate, use the
actual stripped Laurent crossing formulas. Under x -> -x, a transfer
of order h contributes (-1)^(u+v+h) for either crossing sign, where
u,v are its inputs. Modulo two this is (-1)^(c-u), with c its first
checked output: c=v+h for a positive crossing and c=v-h for a negative
one. Conservation of the integer pair sum makes c-u the negative
change of the sum of index times strand position. Its total is zero
on every diagonal cut state. The remaining pivot/framing sign is
(-1)^((N-1)(b-1-w))=1 for a knot. Hence the reduced Laurent family
is even in x, equivalently in M. Since it is Laurent polynomial,
it descends uniquely to a Laurent polynomial in Y=M^2. This proof
uses the original reduced framing; the unreduced/full state has
the separate sign line and pole factors described in the pointing
notes.

Here tau is the algebraic fundamental pivotal closure trace, P is the
product of the actual Jones--Wenzl idempotents p_(j-1), and every crossing
in rho is the full fundamental matrix, with its common Cartan scalar.
The usual value of q^(1/2) is exp(pi*i/(2N)). The source is the original
reduced cut; the modified-dimension line is not divided out in a new way.

## 1. The invariant quotient is genuinely the ordinary color

At alpha=j-1 the original N-dimensional unrolled color V has

    H v_a=(j-1-2a)v_a,
    K v_a=q^(j-1-2a)v_a,
    E v_a=[a][j-a]v_(a-1), F v_a=v_(a+1).

All missing vectors are zero. The subspace

    U=span(v_j,...,v_(N-1))

is invariant: its only possible downward escape is E v_j, whose
coefficient is zero. H,K,F preserve it as well. The quotient V/U has
basis v_0,...,v_(j-1), with exactly the ordinary j-dimensional
highest-weight matrices. At j=1 this quotient is the trivial color.

The actual uncheck R is

    R=q^(H tensor H/2) sum_(h=0)^(N-1) c_h E^h tensor F^h,
    c_h=q^(h(h-1)/2)(q-q^(-1))^h/[h]!.                  (2)

Every summand preserves U on each input strand separately, as does the
Cartan factor. The inverse has the same preservation property, either
from its finite inverse formula or from invertibility of its induced
diagonal blocks. Its induced quotient is the defining ordinary R:
all terms h >= j vanish there. The checked R exchanges the two typed
strands; it does not exchange the status of a strand with an unrelated
one. The quotient maps consequently satisfy, for both crossing signs,

    (pi tensor pi) B_N = B_j (pi tensor pi).             (3)

The pivot and twist preserve U. There is no singular factorial in this
calculation: h < N in (2), and h < j on the quotient.

## 2. Why quotienting only the open strand quotients the entire knot

This is the essential one-component trace lemma. Choose a basis adapted
to U and V/U on every physical strand. Along each underlying oriented
strand segment, attach status 1 to a basis vector in U and status 0 to
a quotient-basis vector. For every nonzero crossing coefficient,
status can change from 0 to 1, but cannot change from 1 to 0. This is
exactly preservation of U by each uncheck factor, with the strand types
followed through the check permutation. The diagonal pivot preserves
status, and a closing partial trace identifies the status at the two
ends of each traced strand.

To calculate the induced open cut on V/U, its two open ends both have
status 0. If the closed braid is a knot, there is one underlying
component, and it passes through those ends. Following that entire
component from its open input to its open output, a status-1 segment
could never return to the final status 0. Therefore **every** segment
of every contributing state has status 0. The contributing summands
are precisely those obtained by replacing every color by V/U and
taking the same cut trace there. This proves the all-strands color
comparison; Schur's lemma alone would not prove it.

This argument is termwise and works for arbitrary positive/negative
words and any number of strands. It does not require a splitting
V=U direct-sum W into modules. The original reduced cut on V is scalar
even at this reducible color: it commutes with K and F, K has N
distinct eigenvalues, and every internal arrow of F has coefficient
one. Thus its scalar is the same scalar found on the nonzero quotient.

The component assumption cannot be omitted. For the identity two-strand
braid, a separate closed N-color component has pivotal trace zero,
whereas replacing it by the trivial quotient gives trace one. Our audit
checks this failure as well as the knot identities. No analogous
unqualified statement for links is used.

## 3. Pivotal, framing and half-root scalars

Write m=j-1 and epsilon_j=(-1)^m. On the quotient,

    K^(1-N)=epsilon_j K,
    theta_ADO=epsilon_j theta_j,
    theta_j=q^(m(m+2)/2).                              (4)

Indeed K^N=q^(Nm) I=epsilon_j I, since the other weight term is
q^(-2Na)=1. Also

    theta_ADO/theta_j=q^(-Nm)=epsilon_j

from the defining ADO twist q^((alpha^2+2(1-N)alpha)/2).
For a cut of a b-strand knot with writhe w, the b-1 traced pivots and
the framing correction therefore produce the total factor

    epsilon_j^(b-1-w)=1.                               (5)

The braid permutation is a b-cycle, so w and b-1 have the same parity.
This proves the first equality in (1) without an unspecified phase.

The same bookkeeping can be performed in the stripped matrices used by
the exact audits. The common positive Cartan scalar is q^(m^2/2), and
its inverse occurs at a negative crossing. After removing it, the
ordinary residual twist is

    theta_j/q^(m^2/2)=q^m=x.

The ADO residual twist is x^(1-N)=epsilon_j x. Both conventions give
(5). In particular no half-root factor is silently rounded to an
integer q power. The proof covers even N and both parities of j.

## 4. The fundamental cable is the literal colored R

This comparison is needed to use a positive fundamental path trace for
the actual j-color; calling a cable a color is not a proof. Work first
over rational functions of q^(1/2), and retain the coproducts

    Delta E=E tensor K+1 tensor E,
    Delta F=F tensor 1+K^(-1) tensor F.

Formula (2), now as a locally finite operator on highest-weight
modules, has the directly verifiable identities

    (Delta tensor 1)R=R_13 R_23,
    (1 tensor Delta)R=R_13 R_12.                      (6)

For detail, put Q=q^2 and h=r+s. The finite q-binomial expansion gives

    (Delta E)^h = sum_(r+s=h) {h choose r}_Q
                              E_1^r E_2^s K_2^r,
    (Delta F)^h = sum_(r+s=h) {h choose r}_Q
                              F_2^r K_2^(-s) F_3^s,
    c_h {h choose r}_Q = Q^(rs)c_r c_s.                (7)

For the first identity of (6), move the R_23 Cartan factor left
through E_1^r F_3^r in R_13. It supplies K_2^r; moving it past
E_2^s supplies Q^(rs). This is exactly the first expansion in (7).
For the second identity, moving the R_12 Cartan factor through the
R_13 nilpotent term supplies K_2^(-s), and ordering it with F_2^r
again supplies Q^(rs). The second expansion in (7) follows.
These coefficient identities prove (6), including the Cartan scalar;
they do not assume a tensor-category comparison theorem. The q-binomial
identities themselves follow by induction from AB=QBA.

Let V_f be the fundamental two-dimensional module. In V_f^(tensor m)
put

    J_m(v_r)=(Delta^(m-1)F)^r(v_0 tensor ... tensor v_0),
                     0 <= r <= m.                    (8)

The coproduct relations give

    E J_m(v_r)=[r][m-r+1]J_m(v_(r-1)),
    F J_m(v_r)=J_m(v_(r+1)),
    K J_m(v_r)=q^(m-2r)J_m(v_r).

The endpoint at r=m+1 is zero. There is a nonzero vector at every
weight for m < N, so J_m is an injective intertwiner at the roots
under consideration. Repeated use of (6), followed by naturality
under this explicitly verified intertwiner, proves

    B_fused (J_m tensor J_m)=(J_m tensor J_m) B_j,        (9)

where B_fused is the ordinary m-by-m crossing cable with its m^2
fundamental crossings. The inverse identity follows by invertibility.
Equivalently (9) follows by expanding the two sides with (7).
The highest-highest entry on each side is q^(m^2/2), so no additional
central scalar is available or required.

On fundamental 01,10 the operator

    U=q I-q^(1/2)B_f

has block [[q,-1],[-1,q^(-1)]] and is zero on 00,11.
The kernel of all adjacent U_i in a fixed weight has dimension one:
each adjacent exchange fixes the q-ratio between the two coefficients,
and exchanges connect all binary words of that weight. It is the vector
in (8). Thus the common kernel has dimension m+1 and is exactly
im J_m. The Jones--Wenzl recursion used in the regular-period note
has image this common kernel: its image is annihilated by the U_i,
and it acts as identity on every common-kernel vector, by induction.
Consequently its actual tensor image is precisely the j-color.

All specializations in this paragraph are regular for m <= N-2.
The recursion uses only [1],...,[m], which are nonzero, and the
ordinary R uses only [h]!, h <= m. No projector on a color of zero
quantum dimension is used in the bound. The constant-color j=1 case
is the empty tensor power and is immediate.

## 5. The trace identification and bound

The fundamental coproduct pivot is K^(tensor m), and (8) identifies
its restriction with the ordinary pivot K_j. For any operator preserving
the idempotent image, finite matrix trace on that image equals
Tr(K^(tensor m) p_m A). Applying this to every block of (9) gives
the second equality in (1). The framing scalar theta_j is exactly
the one in (4). It also follows directly from the positive crossing's
pivotal partial trace: its highest-input entry has just the zero-transfer,
zero-closed-index summand q^(m^2/2)q^m=theta_j.

The fundamental trace obeys

    tau_(l+1)(A tensor I)=(q+q^(-1))tau_l(A),
    tau_(l+1)((A tensor I)U_l)=tau_l(A).

The second equation is the literal partial pivotal trace of the
displayed 2-by-2 block of U. These recursions identify it with the
path trace whose local positivity is audited separately. At the
principal root q=exp(pi*i/N), that trace is positive, the fundamental
braid is unitary, and p_m is an orthogonal projection there. Its
trace is [j], and the b-fold projection has trace [j]^b. Therefore

    |F_N^M(-q^j)|=|F_N^Y(Q^j)|=|C_j(q)| <= [j]^(b-1)
       <= sin(pi/N)^(1-b) <= (N/2)^(b-1).              (10)

This applies to every j<N uniformly, with the original one-component
source and framing. At j=N the quantum dimension vanishes, so the
division in (1) and the positive-color argument do not apply.

## 6. Independent exact audit

[The new audit](../experiments/audit_actual_ordinary_color_comparison.py)
constructs the defining full colored R independently, builds the
fundamental coproduct highest-weight embedding (8), constructs the
literal crossing cable, and tests both signs of (9). It also assembles
the tensor-basis Jones--Wenzl projector, checks its image, generator
intertwining and quantum trace, and restores the full Cartan/twist
factors. The quotient tests use a separate original N-dimensional
matrix construction and compare all colors j<N through complete knot
cuts, including four-strand words and non-highest open inputs. A separate
closed-component failure is checked explicitly.

Fresh result: **PASS**, seven quotient levels N=2,...,8, 228 whole-knot
quotient-cut comparisons, and 22 literal signed-cable families through
N=9, including boundary colors j=N-1 and both level parities.
An additional 28 exact cut comparisons at generic x and -x, away
from the integer-color orbit, independently check the even M descent
used to pass to the Y-coordinate. No full-state pole is evaluated.
[Saved results](../experiments/actual_ordinary_color_comparison_results.json).

The checks supplement the all-level arguments above. The result is a
verification of the ordinary-color polynomial bound's input, not a
volume estimate for the Kashaev color or a claim of reflection positivity
of its modified source.
