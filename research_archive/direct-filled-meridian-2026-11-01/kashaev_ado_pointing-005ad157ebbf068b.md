# A literature quantum A-family with the Kashaev evaluation fixed

Research note, 25 October 2026. The preceding
[crossing calculation](kashaev_crossing_and_period_lattice.md) independently
identifies the normalized enhanced Kashaev period with the reduced
highest-weight quantum-group period. Here we give its meridian family,
its exact normalization lattice, and its implications for the norm torsor.

Definitions are the unrolled quantum-group R, pivotal and modified-dimension
formulas in Brown--Dimofte--Garoufalidis--Geer,
[2005.08176](https://arxiv.org/abs/2005.08176), Section 2. Their holonomicity
and recursion-ideal comparison theorems are not assumed. The calculations
below use the displayed definitions directly.

## 1. The zero-framed reduced family is rational in its color

Fix r>=2, q=exp(pi*i/r), and x=q^alpha. On V_alpha use

    H v_j=(alpha-2j)v_j, K v_j=x q^(-2j)v_j,
    E v_j=[j]_q[alpha-j+1]_q v_(j-1),
    F v_j=v_(j+1),       0<=j<r.

Use the finite universal R from the preceding note with k<r, pivotal
matrix K^(1-r), and twist

    theta_alpha=q^((alpha^2+2(1-r)alpha)/2).

Let F_r(alpha) be the reduced (1,1)-tangle scalar for a zero-framed
knot, with unknot value one. It is the usual modified-trace ADO
invariant divided by the modified dimension, not a new local weight.

**Rationality lemma.** F_r(alpha) is a Laurent polynomial in x with
complex coefficients at fixed q.

Proof: remove the common factor q^(alpha^2/2) from each positive R
and its inverse from each negative R. The remaining entries are Laurent
polynomials in x, since

    q^((alpha-2c)(alpha-2d)/2)
           =q^(alpha^2/2) x^(-c-d) q^(2cd),
    [alpha-j+1]_q
           =(x q^(-j+1)-x^(-1)q^(j-1))/(q-q^(-1)).

All denominators [k]_q!, k<r, are nonzero constants. For a braid word
of writhe w, the total removed factor is q^(w alpha^2/2). It cancels
with theta_alpha^(-w); the remainder is x^(-w(1-r)). The pivotal
entries are also Laurent monomials in x. Finite products, sums and
partial traces prove the assertion. Scalarity on generic typical colors
and the resulting identity extend through the finite exceptional set.

In particular F_r(alpha+2r)=F_r(alpha). This has a direct algebraic
proof from the defining matrices; it is not a consequence imported
from a holonomicity theorem.

## 2. Exact specialization to the original Kashaev period

At alpha=r-1 the matrices are the r-dimensional highest-weight matrices
of the crossing note. The two pivotal conventions differ by

    K^(1-r)=(-1)^(r-1) K.

The corresponding twists differ by the same sign. For a b-strand braid
closing to a knot, w has parity b-1. Hence the resulting factor
(-1)^((r-1)(b-1-w)) is one. The dual convention in the crossing note
is equivalent to the original highest-weight color: an explicit
intertwiner with its dual is

    B v_j=(-1)^j q^(j(j-r)) v_(r-1-j).

For example, with Delta E=E tensor K+1 tensor E and
Delta F=F tensor 1+K^(-1) tensor F, the antipodes are
S(E)=-E K^(-1) and S(F)=-K F. Direct substitution verifies B on
E,F,K. The same substitution in the finite R gives
R^T=(B tensor B)R(B^(-1) tensor B^(-1)).

Consequently the already specified enhanced period satisfies

    F_r(r-1)=<K>_r.                                   (2.1)

This is a uniform matrix and pairing comparison for knots, with the
zero framing and unknot normalization fixed.

The subsequent [root-orbit pointing proof](root_orbit_pointing.md)
extends this calculation to every integer color 1<=j<=r:
F_r(M=-q^j)=C_j(q), where C_j is the reduced j-dimensional period.
Its proof uses the invariant quotient of the color and a filtered
cut-trace argument for a one-component braid closure. In particular
F_r(-q)=1 supplies a nonzero reference anchor on the same central
fiber as M=1. For the full state this is a residue anchor, as the
modified dimension has a pole at M=-q.

The [all-level period theorem](all_level_a_period.md) now uses these
identities and polynomial rigidity to recover the exact Kashaev
value from any specified actual all-level annihilator and finitely
many fixed small colors. Whole q-germs handle singular steps with
a uniform jet bound. Root-level rank one is not required.

## 3. The generic peripheral factor is an actual cyclic lattice gauge

Write N_r(alpha)=d_r(alpha)F_r(alpha) for the modified-trace ADO
invariant. Its defining modified dimension is

    d_r(alpha)=-q^(r(1-r)/2)
          (q^(alpha+1)-q^(-alpha-1))/(q^(r alpha)-q^(-r alpha)).

Introduce the marked meridian coordinate M=-q x, so that M=1 at
alpha=r-1. Then, exactly,

    d_r(M)=eta_r (M-M^(-1))/(M^r-M^(-r))
           =eta_r M^(r-1)/P_r(M^2),
    eta_r=(-1)^(r+1)q^(r(1-r)/2)=i^(r+3),
    P_r(t)=1+t+...+t^(r-1).                           (3.1)

Thus the modified-dimension factor is the cyclic stable-lattice
generator 1/P_r(t) from Section 3.1 of the intrinsic norm-torsor note,
with t=M^2, together with its explicit monomial and phase. This is
an instance in the literature state itself, not just a model.

At M=1 the whole rational germ is regular and evaluates to

    d_r(1)=eta_r/r,
    <K>_r=r eta_r^(-1) N_r(r-1).                      (3.2)

Setting numerator and denominator separately to zero would discard this
value. The exact comparison keeps the peripheral polynomial P_r and its
specialization P_r(1)=r. No topological or norm conclusion uses a bare
numerical multiplier in its place.

There is also a level-independent difference equation. Since the color
shift sends M to q M and q^r=-1,

    d_r(qM)/d_r(M)=g(q,M),
    g(q,M)=-q^(-1)(q^2 M^2-1)/(M^2-1).               (3.3)

If f(M)=M-M^(-1), then g=-f(qM)/f(M). Thus this normalization line
is a fixed rational gauge tensored with the sign character of the shift.
Its root-level realization is the explicit peripheral divisor in (3.1).
It is not a collection of arbitrary independent finite-level scalars.

The subsequent [relative octahedral calculation](relative_octahedral_period.md)
also derives 1/P_r(M^2) as the missing cyclic transition of the
finite factorial actually appearing in these R entries. Its
polynomial recurrence retains the source M^(2r)e_partial, and
its cyclic system is nonsingular even on the completion's polar
divisor. Thus this normalization has an explicit local relative
origin as well as the meridian gauge calculation above. The
global source/regulator comparison is not inferred from it.

## 4. The literature annihilator ideal and the pointed conjecture

The all-level ADO annihilator ideal is defined in the literature by

    I_ADO={P(q,x,T): P(q_r,x,T)N_r(x)=0
                         for all but finitely many r},
    T x=q x T, q_r=exp(pi*i/r).

See equation (1.5) of the cited definition source. Under x=-q^(-1)M,
the exact change from N_r to F_r induces the automorphism of the
localized Ore algebra C(q,M)[T^(+/-1);sigma]

    M -> M,          T -> g(q,M) T.                  (4.1)

Indeed d_r^(-1) T d_r=g T. Therefore existence of a nonzero all-level
annihilator is equivalent in the two normalizations, and their
localized ideals correspond by (4.1). No unverified equality with the
colored-Jones recursion ideal or AJ specialization is needed for this
statement. The subsequent [finite cut-state proof](finite_sum_annihilator.md)
now supplies a nonzero actual all-level meridian annihilator for
every knot. The cited paper's holonomicity theorem remains outside
the proof premises; the stronger multicomponent dimension statement
is not needed for this conclusion.
At M=1 the comparison uses the lattices and regular whole period germs
in (3.1)--(3.2), since the localized coefficient g is meromorphic there.
Localization alone does not specify this specialization.

The subsequent [actual peripheral-fusion proof](actual_peripheral_fusion.md)
derives this gauge from the pivotal partial traces of the two
adjacent-color projectors, without a modified-trace comparison theorem.
The full state has elementary boundary actions M+M^(-1) and
T+T^(-1). The fusion wall at M=1 has a nonzero square-zero Casimir
residue with exactly normalized partial trace; its actual knot
coefficient and the normal Kashaev functional are retained as
distinct meridian derivatives. Peripheral skein relations thus
yield actual annihilators, without identifying the entire ideals
or their geometric components.

For this literature family with its prescribed pointing, the desired
quantum-A volume statement is

    lim_(r->infinity) (2*pi/r) log|F_r(M=1)|=Vol(S^3 minus K).
                                                               (4.2)

Equations (2.1) and (3.2) identify (4.2) with Kashaev's original
conjecture. The same rate for N_r at the regular germ M=1 is equivalent,
since log r/r tends to zero and |eta_r|=1. This is a precise formulation
with a fixed literature state, not an arbitrary solution of an operator.
Equation (4.2) is not proved here.

## 5. What a root-of-unity central torsor does and does not select

There is a useful general constraint. Let a nonzero rational function
h(x) solve a specialized finite-order q-difference equation with q a
primitive n-th root. Let H=T^n be its companion monodromy as in the
intrinsic norm-torsor note. Then

    det(I-H)=0.                                       (5.1)

Proof: evaluation at h is a nonzero module map from the cyclic operator
module to (C(x),sigma). On the target sigma^n=1. Hence the map kills
H-I, so H-I cannot be invertible. This proof uses the solution pairing,
not an identification of column vectors with solutions.

Both F_r and N_r are rational in x at zero framing. Thus any specified
all-level operator annihilating them has a central v=1 sector at its
regular root levels n=2r. This finite-level sector must not be identified
automatically with the geometric component of the classical q->1
A-curve. The quantum family and its distinguished pointing remain
essential. No assertion is made that the literal classical A-curve is
the central spectral curve of each root-level state.

The required torsor comparison is therefore a comparison of the
all-level pointed period with the marked geometric regulator, retaining
the normalization lattice. The cyclic norm torsor alone does not select
the volume-dominant geometric sector.
