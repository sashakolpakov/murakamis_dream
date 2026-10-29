# The divided Ward power is an exact unipotent factorial fusion defect

Research proof, 27 October 2026. Work in the genuine generic quantum
group Weyl color `D_(N-1)(q)`, whose complete root specialization is
the original Kashaev color. A mixed first-normal divided power on
two factors is nonzero although the individual divided powers vanish.
It is exactly the multiplicativity defect of the literal finite Ward
factorial. The defects have a coherent associative fusion law, with
the even-level Frobenius signs retained.

These are operator and normal-source statements. They do not prove
that the ghost survives the selected scalar knot contraction.

## 1. The integral Weyl lift and its divided power

Put `Q=q^2`, `rho=q-q^(-1)`. On `D_(N-1)(q)` use

    F v_a=v_(a+1),
    E v_a=[a]_q [N-a]_q v_(a-1),
    K v_a=q^(N-1-2a) v_a,       0<=a<N,

with endpoint vectors zero. These are genuine finite quantum-group
matrices for generic `q`. In the meridian convention `x=-M/q`, their
color is `x=q^(N-1)`, hence `M=-q^N`. At `q_N=exp(pi*i/N)` this
is the complete color `M=1`, including even and composite `N`.

Use `Ecal=rho^2 E`; its coproduct is

    Delta Ecal=Ecal tensor K+1 tensor Ecal.

In the balanced basis `w_a=v_a/(Q;Q)_a`, the raising coefficient is

    Ecal w_a=(q^(-N)-q^(N-2a))w_(a-1).

At the root this becomes `(Q^(-a)-1)w_(a-1)`, the actual complete
matrix. These basis changes are units at the root for `a<N`.

On two factors put

    A=Ecal tensor K, B=1 tensor Ecal, C=A+B.

They satisfy `AB=Q BA`, and `A^N=B^N=0` for every generic `q`.
The normal-ordered q-binomial expansion is

    C^N=sum_(j=1)^(N-1) {N choose j}_Q B^(N-j) A^j.

Every coefficient has a simple factor `1-Q^N`; its quotient is
regular at every primitive `N`-th root. Thus the literal first-normal
operator

    J=[C^N/(1-Q^N)]_(q=q_N)

is well defined and equals

    J=sum_(j=1)^(N-1)
         N B^(N-j) A^j/[(Q;Q)_j (Q;Q)_(N-j)].        (1)

Here `(Q;Q)_(N-1)=N`. This is the scaled divided quantum-group
power, not an arbitrary operator added to the root color. It records
the specified generic integral lift. Its individual one-factor
counterpart is zero because `Ecal^N=0` identically there.

One has `[J,C]=0`, and `J^2=0`: both follow from the generic identity,
or from total-index lowering by `N` in a two-factor space whose
maximum total index is `2N-2`. Every generic braid intertwines `C`,
so division by the scalar and specialization show that it also
intertwines `J`.

## 2. A uniform explicit nonzero entry

The vector `w_(N-1) tensor w_1` has only one surviving term in (1),
namely `j=N-1`. Its coefficient is `1/(1-Q)`. At the root,

    Ecal^(N-1)w_(N-1)=(-1)^(N-1)N w_0,
    Ecal w_1=(1-Q)Q^(-1)w_0,
    K^(N-1)w_1=q_N^((N-1)(N-3))w_1.

The phase therefore simplifies, using `q_N^N=-1`, to

    J(w_(N-1) tensor w_1)=-N q_N w_0 tensor w_0.       (2)

This proves nonvanishing at every `N>=2` with the original balanced
root normalization. No odd-level restriction is used.

## 3. Exact factorial fusion, including all degrees

Define the positive-argument finite factorial

    p_N(X)=sum_(j=0)^(N-1) X^j/(Q;Q)_j.

At generic `q`, q-binomial expansion gives the finite identity

    p_N(B)p_N(A)=sum_(n=0)^(2N-2) C^n/(Q;Q)_n.       (3)

Indeed the coefficient of `B^i A^j` on both sides is
`1/[(Q;Q)_i(Q;Q)_j]`; terms with either index at least `N` vanish.
For `n=N+s`, cancel `1-Q^N` in (3) before taking the root. Since

    [(Q;Q)_(N+s)/(1-Q^N)]_root=N (Q;Q)_s,

the resulting summand is `J C^s/[N(Q;Q)_s]`. Terms with
`s>=N-1` vanish by total degree. Therefore the exact root identity is

    p_N(B)p_N(A)=(I+J/N)p_N(C).                       (4)

The literal Ward polynomial has argument `-t Ecal`, not positive
`Ecal`. Thus its corresponding form is

    p_N(-tB)p_N(-tA)
       =(I+(-t)^N J/N)p_N(-tC).                       (5)

The sign `(-t)^N` must not be suppressed. The first missing degree
is `N`, but (4)--(5) identify the **entire** finite product defect.
Since `J^2=0`, its logarithm is exactly `(-t)^N J/N`.

This is also the resonant logarithm of the unfolded factorial.
The degree-`N` term of
`log p_infinity(X)=sum_m X^m/[m(1-Q^m)]` is
`X^N/[N(1-Q^N)]`. Along the specified tensor lift its regular
value is `J/N`. The normal extension, rather than the bare root
identity `C^N=0`, retains this term.

## 4. Coherent fusion on arbitrary ordered blocks

For an ordered block `X` of Steinberg factors let `C_X` be its total
`Ecal`, `K_X` its total `K`, and

    J_X=[C_X^N/(1-Q^N)]_root,
    chi_X=K_X^N=(-1)^((N-1) length(X)) I.

Regularity of `J_X` follows from the ordered q-multinomial expansion:
all nonzero exponent tuples have entries below `N`, while the
numerator has the factor `1-Q^N`. The operator lowers total degree
by `N`, and satisfies `[J_X,C_X]=[J_X,K_X]=0` at the root.

For any `k,s` with `0<=s<N`, direct factor grouping gives

    [(Q;Q)_(kN+s)/(1-Q^N)^k]_root
                          =N^k k! (Q;Q)_s.

Consequently the root of the generic finite quantum exponential is

    E_X(t)=exp[(-t)^N J_X/N] p_N(-t C_X).             (6)

The exponential is finite: its `k`-th term lowers total degree
by `kN`, so it terminates before `k=length(X)`. Formula (6) is
also the ordered product of the individual factorials, with each
individual raising generator dressed by all later `K` factors.

For two consecutive blocks define the mixed divided power

    j_(X,Y)=J_(X tensor Y)-J_X tensor chi_Y-1 tensor J_Y.

The coproduct q-binomial expansion gives explicitly

    j_(X,Y)=sum_(a=1)^(N-1)
      N (1 tensor C_Y)^(N-a)(C_X tensor K_Y)^a
                      /[(Q;Q)_a(Q;Q)_(N-a)].        (7)

The inherited terms `J_X tensor chi_Y` and `1 tensor J_Y` commute
with both arguments in (7). Canceling them in the generic
q-exponential product proves the block fusion identity

    p_N(-t(1 tensor C_Y)) p_N(-t(C_X tensor K_Y))
      =Theta_(X,Y)(t) p_N(-t C_(X tensor Y)),

    Theta_(X,Y)(t)=exp[(-t)^N j_(X,Y)/N].             (8)

These transitions are unipotent. In a block of length `b`, all their
nonconstant terms lower total degree by at least `N`; the ideal of
such endomorphisms has `b`-th power zero. This nilpotence bound is
independent of the level `N`.

### Associativity, with the Frobenius character retained

For three consecutive blocks, direct cancellation of the inherited
`J_X,J_Y,J_Z` terms gives the exact additive identity

    j_(X,Y) tensor chi_Z+j_(X tensor Y,Z)
       =1 tensor j_(Y,Z)+j_(X,Y tensor Z).          (9)

Within the left pair the two operators commute: `j_(X,Y)` commutes
with `C_(X tensor Y)` and `K_(X tensor Y)`, and the next mixed
operator is a polynomial in that block's total raising operator
and the last block's raising operator. The corresponding right pair
commutes for the same reason. Exponentiating (9) therefore gives

    [Theta_(X,Y) embedded with degree-N factor chi_Z]
          Theta_(X tensor Y,Z)
       =Theta_(Y,Z) Theta_(X,Y tensor Z).          (10)

This is the coherent twisted fusion-cocycle identity. At odd `N`
the displayed character is one; at even `N` it can invert the
embedded unipotent transition. It is part of the tensor convention.
Repeated application proves independence of parenthesization.

Thus the actual divided-power normal extension has literal coherent
unipotent fusion transitions on this ordered tensor category. No
braided source torsor, chosen cohomology class, or selected-period
survival is inferred solely from the associative identity. This
nilpotence statement concerns the positive raising-factorial
transitions. Adjoining lowering divided powers is a different
operation and need not preserve a nilpotent group.

## 5. The Hopf-adjoint and cohomological qualifications

The new normal generator avoids the finite-order-flow obstruction:
it is not the logarithm of the finite-order `ad_K`. It acts
nontrivially on tensor and dual multiplicity data even though its
one-color action vanishes. Its first-normal coproduct is not
primitive; the mixed term (7) is indispensable. A factorwise
primitive flow with zero action on each individual color would
miss the entire operator (2).

For matrix Ward complexes one must use its **divided Hopf adjoint**,
not just the ordinary commutator with `J_X`. The coproduct has the
inherited `J` terms and the mixed lower-power terms in (7). The
antipode is the regular specialization of the generic antipode;
in this normalization it gives `S(J)=-J K^(-N)`. Hence on an
endomorphism `T` its action has the form

    ad_J(T)=J T K^(-N)-T J K^(-N)
       +sum_(a=1)^(N-1) c_a Ecal^a T
                                S(Ecal^(N-a)K^a),
    c_a=N/[(Q;Q)_a(Q;Q)_(N-a)].                  (11)

The mixed terms need not vanish on arbitrary matrices, even when
`J` vanishes on the underlying single-color module. Commutation
of `J` with a braid alone does not replace this all-matrices action.
A compatible pivotal trace can be obtained from the genuine
generic Hopf trace before dividing and specializing, retaining the
actual root pivotal and peripheral scalar adapters. The separate
original marked defect is still not an ordinary intertwining coupon.

Moreover the mixed insertion is negligible under the ordinary full
cut trace for a grading reason. Any braid operator has total-degree
zero, while `J_X` lowers total degree by `N`. Closing all but one
color forces the remaining color to lower by `N`, impossible in
the range `0,...,N-1`. Thus the ordinary cut operator with this
insertion is zero. A nonzero relative class would have to retain
compensating wrap and marked-cut currents before taking this
quotient. Their existence and nonzero pairing have not been proved
by (4) or (10).

Finally, nilpotence by itself does not identify a class in the
geometric Gaussian pushforward. It makes a specified perturbation
finite only after that perturbation is an actual filtered chain map
on a common source complex. The map, differential, endpoint/carry
terms, and the nonzero leading scalar projection are still required.
The exact fusion cocycle supplies new coherent normal-source data;
it does not by itself supply these HPL hypotheses or a selected
volume asymptotic.

[Exact audit](../experiments/audit_divided_ward_factorial_fusion.py)
and [results](../experiments/divided_ward_factorial_fusion_results.json)
compare (1) with an independent generic-q normal derivative, check
the full signed factorial identities, and verify triple fusion
associativity with both Frobenius characters.
