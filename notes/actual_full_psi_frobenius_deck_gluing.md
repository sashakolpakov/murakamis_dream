# Exact full-Psi deck characters and central gluing

28 October 2026. The full functions in the ORIGINAL source and its
new beta residue factors have an exact algebraic deck character.
Products and integral monomial gluing carry this character without
an unknown central normalizer. Its triviality equations are the
marked exponential gluing equations in Frobenius coordinates.

This constructs central data of the actual specified full-function
components. It does not assert that the original invariant is only
one such component, or that its complete relative source lies on
the character-one locus. The [actual beta deck extension](actual_beta_current_connection_and_monodromy.md)
shows why those additional assertions would be false without source
and cycle control.

## 1. A full-function identity on the logarithmic cover

Put h=2*pi*i/N, N>=2. Use precisely the two original functions
Psi_epsilon, epsilon=+1,-1, with

    Psi_epsilon(L+epsilon*2*pi*i)
                     =Psi_epsilon(L)/(1-exp(NL)).       (1)

For every integer m, meromorphic continuation gives

    Psi_epsilon(L+2*pi*i*m)/Psi_epsilon(L)
                     =(1-exp(NL))^(-epsilon*m).        (2)

This includes negative shifts and all divisor multiplicities. An
identity across a zero or pole is understood after cross-multiplication;
no vanishing norm factor is separately inverted on the source.

Let Z=(Z_1,...,Z_d) be marked logarithmic coordinates. Take integer
row vectors a_j, a symmetric integer matrix C, constants ell_j and
a specified linear term b_N. The constants may include actual
colors and exact h or h/2 shifts. Consider the SPECIFIED component

    F_N(Z)=P_N(exp Z)
       exp[(Z^t C Z/2+b_N^t Z)/h]
       product_j Psi_(epsilon_j)(a_j.Z+ell_j),          (3)

where P_N is single-valued meromorphic in exp Z. It can contain
the original integer powers, factorial constants and boundary
polynomials; it is not assumed small. Write

    X_k=exp(NZ_k), Xi_j=exp(N ell_j),
    A_j=Xi_j product_k X_k^(a_jk),
    gamma_k=exp(N b_N,k+pi*i*N C_kk).

Direct substitution in (2)--(3) gives EXACTLY

    F_N(Z+2*pi*i e_k)/F_N(Z)=chi_k(X),

    chi_k=gamma_k product_l X_l^(C_kl)
                     product_j(1-A_j)^(-epsilon_j a_jk). (4)

All half-step phases are present in Xi_j and gamma_k. In particular
an h/2 shift contributes -1 to Xi_j and cannot be dropped before
taking the Nth-power norm.

The factor pi*i*N C_kk is also necessary. For example the bare
Gaussian exp(-eta^2/(2h)) has character

    (-1)^N exp(-N eta),                            (5)

not exp(-N eta). Such signs can cancel an actual half-step elsewhere
in a complete kernel, but may not be removed from individual factors.

For any winding n in Z^d,

    F_N(Z+2*pi*i*n)/F_N(Z)
       =exp[N n^t C Z+pi*i*N n^t C n+N b_N^t n]
                           product_j(1-A_j)^(-epsilon_j a_j.n)
       =product_k chi_k^n_k.                       (6)

The last equality uses
n^t C n-sum_k n_k C_kk in 2Z. Thus the complete deck action is an
algebraic character on the central torus, not only an infinitesimal
semiclassical relation. Formula (6) fixes the integer Gaussian
cocycle as well as its first generators.

If a later elimination produces rational C or rational linear
coordinates, (4) must be used on the corresponding integral cover
or before that elimination. Clearing a common denominator and
restricting to its integral deck sublattice is sufficient. This
does not identify different logarithmic sheets of the original source.

## 2. The character-one equations are marked Frobenius gluing

On a selected central logarithmic chart Y=Log X define

    W_cent,N(Y)=sum_j epsilon_j Li_2(Xi_j exp(a_j.Y))
                    +Y^t C Y/2+sum_k Log(gamma_k)Y_k.  (7)

The logarithms of gamma keep their specified marks from (4).
Differentiation gives

    exp(partial_(Y_k) W_cent,N)=chi_k(X).            (8)

Consequently chi_k=1 is precisely the EXPONENTIAL marked gluing
equation for this component. Its logarithmic lifts differ by the
recorded multiples of 2*pi*i. This is an exact central identity
at every N, before making a saddle approximation.

The central variables X=exp(NZ) and the ordinary semiclassical
shape variables exp Z are different. Equation (8) is not a
convergence theorem between their evaluations, and does not put
the selected source on chi=1. It specifies the Frobenius copy of
the same monomial/dilogarithmic equations, with its actual norm
and Gaussian marks retained.

## 3. The actual beta residue verifies the complete formula

For the proved original trivalent section, put l=Log u, k=Log v.
Its exact form is

    S_N=(N/phi_N)u^N
       exp[(l^2-kl)/h] Psi_+(k-l) Psi_+(h-l).       (9)

Here C=[[2,-1],[-1,0]], both atom signs are positive, and their
rows are (-1,1),(-1,0). The exact h shift has central value one.
The factor u^N is single-valued and stays in P_N; it has a genuine
exponential rate but no deck character.

Let U=u^N,V=v^N,A=U-V. Formula (4) becomes

    chi_u=A(U-1)/V,
    chi_v=1/A.                                     (10)

These are the independently derived exact beta deck multipliers.
They are also the exponential derivatives of the classical marked
phase after substituting the central variables. At chi_u=chi_v=1,
the finite nonzero torus condition is simply A=1. The factor u^N
is INVISIBLE in (10); its correct value was established by the
separate original-source rigidity proof. Thus even this exact
character calculation alone would not normalize the period.

The untouched full-Psi atoms in the original scalar crossing obey
(2) individually. The reflected factorial monomials have integral
exponents N-1 and no additional deck character. The original
continuous Gaussian of sign s is exp[-s eta_s^2/(2h)] with
eta_s=sqrt(2*pi*i*s)xi; its character is
(-1)^N exp(-sN eta_s). Equation (5) displays the positive case.
In these respective coordinates the dilation atom rows remain integral.
The new
beta residue has precisely (9), including its rational prefactors
after exact Q-tag shifts. Therefore all these actual components
are covered by the SAME character rule before their original
external integration. No alternative knot state is introduced.

## 4. Integral head gluing carries the characters exactly

Suppose local component i has logarithmic arguments

    Z_i=L_i T+c_i,

where L_i is an integer matrix describing its actual head and
boundary monomials. Include all untouched atom, Gaussian and
source factors. If T_k makes one full turn, factor i makes the
integer winding L_i e_k. Therefore the geometric product has

    chi_total,k=chi_external,k
                    product_i product_a chi_(i,a)^(L_i[a,k]). (11)

This follows from exact meromorphic identities, so it does not
require pairwise independence of monomial arguments, a nonsingular
B block, or a saddle determinant. Equivalently substitute Z_i
in (3): C_total=sum_i L_i^t C_i L_i and the atom incidence rows
pull back by L_i. The linear terms include C_i c_i as well as
the original b_i. Formula (4) for this substituted function is
identical to (11), including the parity constants in (6).

For the literal eligible crossing star

    u=z_4/z_1, v=x^(-1) z_4/z_0,

its three head characters are

    z_4 turn: chi_u chi_v=(U-1)/V,
    z_1 turn: chi_u^(-1)=V/[A(U-1)],
    z_0 turn: chi_v^(-1)=A.                          (12)

Their product is one, as required by invariance under simultaneous
scaling of its three heads. They are generally not individually
one. The central color x^N remains inside V; it is not specialized
to a clock value merely because the finite head has dimension N.

For a finite collection of pairwise disjoint eligible sink stars,
the sink source has the tensor product presentation of the beta
rank-two extensions, with its original exterior pairing. Formula
(11) computes the character of the full selected component. The
finite sink pointing product_i B_i, which also contains the current
sectors, is invariant in its boundary monomials. Untouched full
functions still have their own characters and matched relative
cycles. Invariance of the sink pointing does NOT imply that its
all-residue sector, or that sector times untouched fields, has
character one.

## 5. What the central equations establish and what they do not

On any stated actual phase graph, (8) and (11) provide the exact
central norm equations whose classical gluing description has
already been checked. An A-polynomial elimination must keep the
same regular graph, peripheral marks and saturation divisors.
Arbitrary denominator-cleared components are not restored by
calling these equations Frobenius gluing.

The theorem does not identify an eliminated curve with the
selected minimal quantum A-operator or prove that its geometric
branch contributes to the original scalar. The current extension
and original relative integration class remain indispensable.
In particular, the exact current can gain a nondegenerate
geometric residue under a deck turn. Killing every current is
not a source-preserving quotient even when a product character
is one.

The constructive output is explicit: the entire residue product's
deck character and its character-one variety are known from the
actual monomial incidence and Gaussian data. The missing global
step concerns the selected marked relative class on that variety,
not an unspecified central multiplier for each local beta section.

The [audit](../experiments/audit_actual_full_psi_frobenius_deck_gluing.py)
checks direct complete-function turns with both orientations,
mixed integer Gaussian matrices, arbitrary integer windings,
half-step and odd-Gaussian signs, the actual beta characters,
and the literal three-head pullback. Finite checks supplement
the exact identities (2)--(6), not a source-selection assertion.
Cap factors are used as their complete finite polynomials or with
their matched relative interval seams. No scalar character is
assigned to an isolated fractional interval-density summand.

