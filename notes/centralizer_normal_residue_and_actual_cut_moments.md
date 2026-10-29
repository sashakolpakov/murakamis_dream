# The actual cut moments are centralizer normal-residue co-sources

Research proof, 27 October 2026. Polynomial centralizer currents
have an explicit finite-pole realization on the resolved actual
framing torsor. Their normal residues pair with every actual cut
matrix by a specified Toeplitz row. The two Weyl charts glue by an
explicit rational homotopy, while their current primitives retain
exactly the two endpoint values. A whole cut-clock co-source then
extends the construction beyond individual Taylor jets.

This constructs a framing moment/current map. The centralizer b is
a framing variable, not an unframed critical-field generator. No
descent of the actual state to its geometric critical summand is
inferred from this map.

## 1. Actual framing coordinates and the normal form

Use the source/framing threefold and the original marked density
of [the compact framing bridge](compact_framing_gauge_and_boundary_residue.md).
On the north chart write

    Omega=dv wedge da, T=va, X=eta v, F=1-X,
    b_N=-a/eta=-T/X,
    nu_cut=-(d eta/eta) wedge Omega/F.             (1)

Here b_N is the right regular-unipotent centralizer coordinate.
The south chart is

    V=1/v, a'=v-v^2a, eta'=-v^2eta,
    T'=Va'=1-T, b_S=-a'/eta',
    b_S=b_N+1/X, F=1+eta'V.                     (2)

The form nu_cut is global; its factor 1/F is the actual cut/Haar
adapter and is not set to its boundary value before taking
moments. The original principal Gaussian multiplies (1) by its
marked nonzero algebraic density c_beta and original base line.
These factors tensor through the calculations below.

Work over any characteristic-zero coefficient field of the marked
unframed data. Polynomial coefficients below are independent of
the framing coordinates. The normal residue is taken at eta=0
coefficientwise at finite pole order, with d eta/eta first.

## 2. Polynomial moments have exact normal residues

For every h>=0,

    Res_E[b_N^h nu_cut]=-(-T)^h Omega.           (3)

Indeed `b_N^h=(-a)^h eta^(-h)` and
`1/F=sum_(r>=0)eta^r v^r`; only r=h contributes to the normal
residue. Thus for any polynomial P,

    Res_E[P(b_N)nu_cut]=-P(-T)Omega.             (4)

The adapter 1/F is decisive. Replacing nu_cut by the Haar form
before multiplying by b_N^h would lose every nonconstant moment.
The bounded moment h has finite normal pole order h+1.

With the actual compact sphere and omega_I=-Omega/(2pi*i),
the normalized identity-source period is exactly

    (1/(2pi*i))integral_Gamma Res_E[P(b_N)nu_cut]
                             =integral_0^1 P(-T)dT.        (5)

This is not an assertion that P(b_N) is a global scalar function;
the required chart gluing is provided next.

## 3. The two polynomial moment charts glue by a specified homotopy

The residue-compatible south representative of the north polynomial
P(b_N) is P(b_S-1). It is not P(b_S). With (2),

    b_S-1-b_N=F/X.                              (6)

Direct south-chart residue gives
`Res_E[P(b_S-1)nu_cut]=-P(T'-1)Omega=-P(-T)Omega`.
The normal residue is therefore a global source form.

There is an explicit stronger gluing identity. For P=b^h,

    [P(b_S-1)-P(b_N)]nu_cut=d Xi_h,             (7)

where Xi_0=0 and, on the overlap v!=0,

    Xi_h=-sum_(r=1)^h binom(h,r)(-T)^(h-r)
             sum_(k=0)^(r-1)binom(r-1,k)(-1)^k
                      X^(k-h)/(k-h) Omega.      (8)

The denominator k-h is never zero. To verify (7), its left side is

    -[(F-T)^h-(-T)^h]/[X^(h+1)F] dX wedge Omega.

The numerator is divisible by F. Expanding F=1-X leaves only
powers X^(-j), j>=2, whose primitive is precisely (8).
There is no Gauss-wall pole left and no logarithmic E residue
in the overlap difference. The same formula extends linearly
to every P. This gives the actual finite-pole Cech homotopy,
rather than declaring the two polynomial coordinates identical.

## 4. Vertical currents retain their exact endpoint Cech class

The actual right-centralizer vector field is

    V_b=partial_(b_N)=partial_(b_S)=-eta partial_a.

It preserves nu_cut. The vertical two-current is

    alpha_N(P)=iota_(V_b)[P(b_N)nu_cut]
                       =P(b_N)d eta wedge dv/F,
    d alpha_N(P)=P'(b_N)nu_cut.                 (9)

Its north normal residue is

    Res_E alpha_N(P)=[P(-T)-P(0)]dlog v.        (10)

For the south representative P(b_S-1), expressed back in the
north base coordinates, it is

    Res_E alpha_S(P)=[P(-T)-P(-1)]dlog v.       (11)

Thus their exact current Cech difference is

    Res_E alpha_S(P)-Res_E alpha_N(P)
                        =[P(0)-P(-1)]dlog v.   (12)

This is the actual relative endpoint class. It has nonzero
period whenever P(0)!=P(-1). Formulas (7)--(8) also give the
current-level overlap homotopy explicitly by Cartan's identity:

    alpha_S(P)-alpha_N(P)
                         =L_(V_b)Xi_P-d iota_(V_b)Xi_P.

In particular the degree-one example P=b has P'=1 and
endpoint difference one. Its differentiated top form is the
nonzero unit source class. Finite moment degree and nilpotence
of a logarithmic transport group do not make this endpoint
class vanish. A relative source must retain it; it cannot
annihilate every such current and preserve the unit period.

## 5. The correct finite cut co-source is the dual Toeplitz row

Let N>=2, n=N-1, J e_j=j e_j. For a polynomial P define the
literal diagonal cut row

    T_N(P)_j
       =N binom(n,j)integral_0^1
                  P(-T)T^j(1-T)^(n-j)dT.       (13)

For each monomial it is exactly

    T_N(b^h)_j=(-1)^h (j+1)^(rising h)/(N+1)^(rising h),     (14)

for EVERY h>=0. The beta integral proves this finite rational
formula. The actual all-matrix trace identity is

    (1/N)Tr[T_N(P)C]
         =integral_Gamma P(-T)sigma_C omega_I.  (15)

For the actual one-cut and Green matrices, which are diagonal
term by term, this is the original normalized cut as well.
It does not replace the original rank-one cut by a trace on
arbitrary off-diagonal Ward matrices.

Equations (4) and (15) therefore specify the residue co-source
against every actual cut-current kernel. All source coefficient
matrices remain literal; their trace is not used to define T_N.
If raw Green arrays already contain 1/N, first use the explicit
matrix normalization C=N I_raw, as in the cut-current theorem.

Actual Weyl reflection is compatible with these rows:

    T_N(P)_(n-j)=T_N(P(-1-b))_j.               (16)

This follows by T->1-T in (13). The actual weighted anti-diagonal
Weyl operator has the same effect by conjugation on a diagonal
row. Its diagonal source factors and the bounded Gamma units
commute with the row; their original fractional source lattices
are retained rather than inverted at a zero.

There is an exact derivative/current identity. For any diagonal
matrix C and its literal adjacent difference
`Delta C_j=C_(j+1)-C_j`, j=0,...,n-1,

    (1/N)Tr[T_N(P')C]
       =P(0)C_00-P(-1)C_nn
            +n*(1/n)Tr_[dimension n][T_n(P)Delta C].       (17)

Integration by parts and the derivative formula for Bernstein
polynomials prove (17). It retains both endpoint rows and
the change of source degree. This is a finite current map,
not a statement that the knot has changed its quantum color.
For C=I, (17) reduces exactly to P(0)-P(-1), as in (12).
The same definition (13) is used at dimension one when N=2
makes the current target n=1; it is the scalar beta integral.

There is a corresponding explicit product-current correction
before pairing. For a general kernel f_C(v,T),

    d iota_(V_b)[P(b_N)f_C nu_cut]
                  =[P'(b_N)f_C-X P(b_N)partial_T f_C]nu_cut. (17a)

Indeed V_b(T)=-X and V_b(v)=V_b(eta)=0. The north current
residue is `f_C[P(-T)-P(0)]dlog v`. Its derivative verifies
(17a) directly with the normal residue differential sign.
The finite Bernstein derivative in (17) is exactly the kernel
derivative that appears here. It must not be dropped by
treating the source kernel as constant along the centralizer.

## 6. Symbol quantization is distinct from co-source quantization

For degree h<=n there is also a unique diagonal matrix with
coherent symbol (-T)^h:

    Q_N(b^h)=(-1)^h (J)_h/(n)_h,              (18)

where the factorials are falling. This gives the useful exact
symbol derivative identity

    Q_(N-1)(P')=-n Delta Q_N(P).               (19)

The trace in the left target has dimension N-1=n. Summing it
gives P(0)-P(-1), with the same endpoints.

But Q_N(P) is not the co-source (13) against a general C:
ordinary multiplication of coherent symbols is not the matrix
or star product. The rising factorials in T_N and falling
factorials in Q_N must not be interchanged. For identity C
their normalized traces agree with (5); for a general Green
matrix, (13)--(17) are the appropriate paired identities.

## 7. The actual whole cut clock has a compatible normal co-source lift

The companion
[dual whole-clock source theorem](dual_clock_normal_cut_source.md)
constructs the explicit polynomial P^dual_(N,w) of degree<=n
with

    T_N(P^dual_(N,w))_j=w^j, 0<=j<N.           (20)

Its formula is

    P^dual_(N,w)(b)=sum_(h=0)^n [(N+1)^(rising h)/h!]
          [sum_(r=h)^n(-1)^r binom(r,h)(w-1)^r]b^h.

Thus (15) becomes an exact ACTUAL cut-clock pairing,
`Tr(w^J C)/N`, for every C. The map is not guessed from its
limiting symbol. It obeys the exact Weyl relation

    P^dual_(N,w)(-1-b)=w^n P^dual_(N,w^(-1))(b).            (21)

Its finite polynomial endpoints are specified as well:

    P^dual_(N,w)(0)=sum_(r=0)^n(1-w)^r,
    P^dual_(N,w)(-1)=w^N-(w-1)^N.                         (21a)

They are not identified with the two clock eigenvalues.

For w=exp(z/N), it converges locally uniformly in the whole
variables z,b to exp(-zb), with every fixed holomorphic jet.
The centered lift converges to exp[-z(b+1/2)] and its exact
identity-source period is the already marked H_N(z). The
normal pole degree of the whole polynomial can reach N;
it is not discarded before the residue.

Differentiating (20) gives the literal normalized cut-index
moments `(J/N)^h`, including the exact finite Newton correction
in their normal polynomial. The h-th z derivative at zero has
degree at most min(h,n), so its normal pole order is at most
h+1, independently of N. Hence bounded Green LOG moments
of the actual cut clock are included. For example the actual
first normalized moment has

    P_(N,1)(b)=-1/N-(N+1)b/N,
    P_(N,1)(0)-P_(N,1)(-1)=-(N+1)/N.                     (21b)

This is a nonzero endpoint/current Cech class for an ACTUAL
bounded cut-log moment. It does not prove that a particular
complete Green certificate has a nonzero combined boundary;
it proves that bounded degree alone cannot force vanishing.

The degree bound applies to the cut-clock polynomial itself;
a weighted word kernel can still have full coherent degree
N-1. This does not identify
an independent crossing-transfer clock with that cut clock.
For the latter one needs the actual network Ward/current map,
not only a common polynomial or abstract Borel representation.

## 8. Scope of the framing integration

The construction supplies actual source moments, all their
finite endpoint terms, the global polynomial normal gluing,
and the whole cut-clock limit. It is a concrete part of the
missing framing pushforward. The bounded-degree example (12)
also shows why a generic bounded unipotent logarithmic complex
cannot by itself make every Green boundary vanish.

The normal polynomial b is a framing variable. Its normalized
moments are (-1)^h/(h+1), not automatically a finite unframed
critical-field trace. The intended geometric critical algebra
belongs after framing integration. The present maps do not
construct that transverse critical observable or identify the
remaining actual transfer log with the centralizer current.
They also do not prove global polar control for every internal
Gaussian coefficient, selected geometric source survival or
a volume limit.

## 9. Exact audit

[audit_centralizer_normal_cut_moments.py](../experiments/audit_centralizer_normal_cut_moments.py)
and its
[results](../experiments/centralizer_normal_cut_moments_results.json)
verify the finite normal residues, explicit Cech primitive,
both vertical-current endpoint residues and the product-current
covariance correction through degree six. They verify the
dual Toeplitz moments, actual Weyl reflection and paired
current identity with independent matrix entries at dimensions
2 through 9 and moment degrees through seven. The separate
covariant-symbol and degree-lowering map is checked as well.
All these tests are exact rational identities.

The whole-clock construction and its bounded moment-degree
sharpening have their own exact audit linked in the companion
note. The independent
[Gauss-wall/current audit](gauss_wall_current_independent_audit.md)
checks the signs, global polynomial clutch, distinction between
trace and the original average cut, and all endpoint dimensions.
No internal Gaussian or selected critical-field descent is
inferred from these checks.
