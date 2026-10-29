# The actual generic six-head source as a typed recoupling column

29 October 2026. This identifies the full generic source coefficient
`B_abc` with a precisely normalized Clebsch recoupling coefficient. The
proof uses the original nested physical cups and ordered ribbon duals,
including the pivotal clock at the bend. It applies to every ordinary
triangle `0<=a,b,c<=d=N-1`, including the high root partners. It is a
rational generic identity; root zeros and poles are not discarded.

The finite source sum is defined in
[the generic six-head note](actual_generic_six_head_tetrahedral_source.md),
§3. The unequal Clebsch conventions and complete four-port identities are
those of [the four-port kernel](actual_ordinary_four_port_recoupling_kernel.md),
§§1–4. No quantum 6j formula, orthogonality assertion, or asymptotic
estimate is an input here.

## 1. The two genuinely typed Hom bases

Put `Q=zeta^2`, `F_r=(Q;Q)_r`, and `V=V_d`. The ordinary object `Q_j`
has highest weight `2j`. Every Clebsch map `W_AB^C` below has its first
highest-vector component equal to one. Set

    cV=N zeta^(-d^2), pV=cV p_d,
    P_L(u)=(-1)^u zeta^[u(L-u-1)] F_u F_(L-u)/F_L,
    p_L(u,L-u)=P_L(u), ell_L=p_L^(-1).

For fixed `a,b`, a basis of `Hom(Q_b,V tensor V tensor Q_a)` is

    L_c=(W_c tensor I_Qa) W_(Qc,Qa)^Qb,
    |a-b|<=c<=min(a+b,d).                         (1)

Here `W_c:Q_c -> V tensor V` is the physical equal-pair map. A right
basis instead first couples `V tensor Q_a` to an ordinary channel of
highest weight `D`. We use its particular channel `D=d`:

    T=(I_V tensor W_(V,Qa)^V) W_b,
    T=sum_c H_c L_c.                              (2)

All expressions have the displayed physical order `V,V,Q_a`. In
particular `H_c` is a RIGHT-to-LEFT coefficient, rather than the inverse
four-port coefficient. Generic highest-weight decomposition proves the
bases complete; equivalently the explicit unequal Clebsch norms in the
four-port note give their retractions before specialization.

Write

    r=b+c-a, r1=a+b-c, r2=a+c-b.

The exact source-to-recoupling identity is

    H_c=(-1)^(d+c) zeta^E
       F_r1 F_r2 F_(d-a) F_(d-c) F_(2c+1)
       /[F_a F_d F_(d+c+1)] * B_abc,
    E=-2a^2-5c^2+2ac+2bc+ad+3dc-c+d.              (3)

This is an equality of generic rational functions, not an equality
deduced from root nodal values. The following index proof fixes every
clock and scalar in (3).

## 2. Bend the original three-cup source

Let

    J=pV_16 pV_23 pV_45,
    U=(DW_a tensor DW_b tensor DW_c)J.

The actual generic source formula gives `U=sDW_abc Theta_abc`, where
`Theta_abc(2a,r,0)=1` and

    sDW_abc=cV^-3 zeta^[c(d-2c)-2c]
                                     P_(2b)(r1) B_abc.       (4)

Move the first ordinary leg to the last by the ACTUAL inverse cyclic
turn, and bend the now first `Q_b` leg into an input. The resulting map
`M:Q_b -> Q_c tensor Q_a` has literal entries

    M_(gamma,alpha;t)=sum_beta ell_(2b)(t,beta)
                    K_(2a)(alpha)^-1 U_(alpha,beta,gamma).
                                                               (5)

The `K_(2a)^-1` is essential: for an even highest weight `2a`, the
inverse cyclic cup/cap turn is `K_(2a)^-1`, not a permutation. Taking
the input highest color `t=0` and output `(gamma,alpha)=(0,r2)` gives

    M=sDW_abc kTheta W_(Qc,Qa)^Qb,
    kTheta=(-1)^r1 zeta^[2c+r1(2a+1-r1)]
                         F_(2b)F_r2/(F_r F_(2a)).               (6)

Indeed `ell_(2b)(0,2b)=zeta^(2b)` and
`K_(2a)(r2)^-1=zeta^(2c-2b)`. The remaining canonical invariant
coefficient is the direct highest equation

    Theta_abc(r2,2b,0)=(-1)^r1 zeta^[r1(2a+1-r1)]
                              F_(2b)F_r2/(F_r F_(2a)).

There is no division by a root-zero invariant norm in this step.

## 3. The same bend, keeping all physical ports open

Define an actual map from one physical object into `V tensor Q_a` by

    Wtilde_a(i6,alpha;i2)
       =(-1)^d K_d(i2) K_(2a)(alpha)^-1
                  sum_i1 DW_a(alpha;i1,i2) pV(i1,i6).          (7)

This is a rigid bend of `DW_a`, so it is a generic Hopf map. Directly
from the highest entry `(i6,alpha;i2)=(0,a;0)` one obtains

    Wtilde_a=theta_a W_(V,Qa)^V,
    theta_a=cV^-1 zeta^[a(2a-d)]
                         F_a F_d/(F_(2a)F_(d-a)).               (8)

For completeness the entry before the remaining physical cup cancels is

    DW_a(a;d,0)=cV^-2 zeta^[a(2a-d)]
                         F_a F_d/(F_(2a)F_(d-a)).

It follows by taking the unique term of the physical divided-coproduct
formula for `W_a[a](d,0)`. In (7), the signs and the highest physical
clock cancel against `pV(d,0)`, leaving exactly `cV` times that entry.

Now substitute the THREE literal cups of `J` and the ordered formula
for `DW_b` into (5). The cups `pV_23,pV_45` force
`i3=d-i2`, `i5=d-i4`. Their only surviving ratio is

    pV(i4)/pV(d-i4)=(-1)^d K_d(i4).

The ordinary input bend contributes
`P_(2b)(t)/P_(2b)(2b-t)=K_(2b)(t)`. Physical weight conservation
in `W_b[t](i5,i2)` gives

    K_(2b)(t)=K_d(i5)K_d(i2),
    K_d(i4)=K_d(i5)^-1.

Thus the two physical clocks at `i4,i5` cancel, with precisely the
remaining factors in (7). This proves the all-input map identity

    M=(DW_c tensor I_Qa)(I_V tensor Wtilde_a) W_b
      =theta_a (DW_c tensor I_Qa) T.                         (9)

Equation(9) preserves arbitrary allowed exterior tensors and all input
colors of `Q_b`. It is stronger than comparing a single source corner.

Apply `DW_c` to (2). The generic equal-pair norm is

    DW_c W_c=n_c I,
    n_c=(-1)^(d+c)cV^-2
       zeta^[c(c+1)-d(2c+1)]
                      F_(d+c+1)/(F_(d-c)F_(2c+1)).            (10)

Different generic channels are killed. Comparing (6),(9) gives

    H_c=sDW_abc kTheta/(theta_a n_c).                       (11)

Insert (4),(6),(8),(10) and use

    P_(2b)(r1) kTheta
                   =zeta^[2c(r1+1)] F_r1 F_r2/F_(2a).

The powers of `cV`, all three ordinary cups, and `F_(2a)` cancel.
The remaining exponent and factorials are exactly (3).

## 4. Actual Casimir consequence and limits

The RIGHT map `T` factors through the ordinary physical object `V_d`
on positions 2,3. Hence

    Omega_23 T=(zeta^N+zeta^-N) T.                         (12)

Consequently the vector of actual coefficients `H_c` from (3) solves
the genuine left-channel Casimir eigenproblem, including its endpoint
conditions. This supplies a literal source normalization for comparison
with a finite Askey–Wilson/Sears polynomial. Identifying that polynomial
requires matching the actual channel recurrence and gauge; its identity
is not assumed in this note.

All equations above are generic identities. They may be continued as
meromorphic identities to the root, with paired columns and their
normal derivatives retained together. Individual factors in (3) or
(11) can vanish or have poles; the regular original physical source
`B_abc` is still the finite analytic sum in the six-head note. Nothing
here bounds recoupling conditioning, turns the ordered dual into a
Hermitian adjoint, or proves a primitive-graph positive asymptotic.

## 5. Verification

The matching audit constructs the physical `W_j,DW_j` independently,
checks (7),(8) on every input color, and verifies (3) by projecting the
full map (2) for every admissible triangle at generic finite-field
levels. A separate literal six-head contraction verifies (5),(9),
including the pivotal clock, before reducing to a scalar. These finite
checks supplement the displayed generic index proof.
