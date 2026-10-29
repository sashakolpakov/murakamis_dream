# Squared-meridian descent and the signed cyclic norm

Research note, 26 October 2026. The actual reduced knot period is even
in its meridian eigenvalue M. Its specified quantum operator therefore
descends to Y=M^2. At q=exp(pi*i/N), the cyclic extension then has degree
N, matching the parameter Q=q^2 in the actual factorials. The full ADO
period retains a sign line at even levels. These exact statements do not
identify a root central curve with the geometric A-curve or establish
the selected volume limit.

The input is the actual state and exact insertion proved in
[the longitude/action note](quantum_longitude_and_regulator_action.md).
The general norm theorem remains
[the intrinsic construction](intrinsic_quantum_a_norm_torsor.md).

## 1. The exact insertion uses the squared meridian

For a b-strand knot braid of writhe w put kappa_D=w-b+1; it is even.
Let q=exp(pi*i/N), Q=q^2, Y=M^2=Qx^2. At a crossing with input indices
a,b and shift k set A=Q^a, B=Q^b, C=Q^k. The exact insertion is

    L_D(q,Y;s)=q^(-kappa_D)
      product_positive (1-YC/A)/(BC(1-Y/A))
      product_negative A(1-YC/B)/(1-Y/B).             (1.1)

Indeed x^(-w)=product_crossings x^(-sign). Each factor cancels x
against tau_sign^(-1) in the longitude note. Its integer-position
coboundary already fixes the q-phase; no square root is being chosen.
The finite identities are therefore

    F_N(q^j M)=sum_s W_N(M;s)
                           product_(r=0)^(j-1)L_D(q,Q^rY;s).    (1.2)

At special meridians this means the whole cancelled inserted weight.

## 2. Each closed state has cyclic norm one

Here A^N=B^N=C^N=1. The elementary identity
product_(r=0)^(N-1)(1-Q^r z)=1-z^N proves, as rational identities,

    product_r (1-Q^rYC/A)/(BC(1-Q^rY/A))=1,
    product_r A(1-Q^rYC/B)/(1-Q^rY/B)=1.

The remaining framing norm is q^(-N*kappa_D)=(-1)^kappa_D=1. Thus

    Norm_(Y->QY,N)(L_D)=1.                          (2.1)

Take j=N in (1.2). Since q^N=-1, this gives

    F_N(-M)=F_N(M).                                 (2.2)

This applies to every knot and every N>=2, with no positivity,
alternatingness, primality, or parity restriction. At Y^N=1 cancel
the rational norm first; do not evaluate two vanishing products.

A direct proof also works for the auxiliary finite closed lift.
The finite formulas show that a closed state's total x-power is

    E=(N-1)kappa_D
       +sum_positive(-a-b-k)+sum_negative(a+b-k).

All other x-dependence is through Qx^2. Modulo two, either crossing's
contribution is c-a, where c is its first output index. The integer
position coboundary proves sum_crossings(c-a)=0. Hence E is even.
After x=-q^(-1)M the lift uses only Q,Y. This last assertion about
a finite lift does not imply q-sign stability of the all-level
minimal operator on the specified sequence of roots.

### A nonzero actual annihilator can nevertheless be chosen over Q=q^2

The auxiliary finite lift is enough for an existence statement which
does not assert that minimal-operator symmetry. There is a nonzero
specified all-level operator

    P_K(Q,Y,T) in ℚ(Q,Y)[T;sigma], sigma(Y)=QY,   (2.3)

annihilating the original reduced F_N at Q_N=exp(2pi*i/N), outside
a finite set of coefficient poles. No full-state sign or
modified-dimension factor is removed by this assertion.

Here is the construction. The finite closed lift has a sum of
individual closed-state weights. Rewrite its crossings by the
exact Q-Pochhammer formulas in the relative octahedral note. All
entries apart from a monomial in x are rational functions of Q
and Qx^2=Y. The monomial's total exponent is E above. Its parity
proof is statewise and holds for generic q: kappa_D is even and
sum(c-a)=0 on the entire integral closed-flow lattice. Thus E/2
is integral on that lattice. In an integral lattice basis,

    x^E=(Y/Q)^(E/2)

has integral exponents; the remaining Q exponents are integer-valued
quadratic forms. We obtain an actual finite lift

    G_N(Q,Y) in ℚ(Q)[Y^(+/-1)]

with proper Q-Pochhammer factors, the same integer support and
the same boundary faces. Its value at Q_N is exactly F_N(Y).

Apply the already proved filtered shift-span and finite-moment
argument in [the finite-sum proof](finite_sum_annihilator.md), now
with base Q, meridian Y, shift Y->QY and central variable Z=Q^N.
Its alignment condition holds with Pochhammer step one. It gives
a nonzero operator A(Y,Z,T) over ℚ(Q). Strip its largest common
central factor (Z-1)^h before specialization. For each fixed N,
Q^N-1 is a nonzero rational function of generic Q, so this
stripping preserves the exact off-root identity for G_N. At
Q=Q_N all factorial lengths are less than N and are regular.
Setting Z=1 therefore gives the nonzero operator (2.3).

This argument constructs an actual annihilator over the smaller
parameter field. It does not prove that the annihilator ideal
defined only on the selected half-roots is invariant under q->-q,
nor that its old minimal generator descends. One can instead work
with the specified operator (2.3), or with the minimal generator
in the nonzero ideal over C(Q,Y).

All finite lifts have rational coefficients in Q. Their root
identities therefore have the expected Galois conjugates at the
other primitive Q-roots. This supplies the correct parameter
setting for a cyclotomic-curvature comparison. It does not show
identity of the entire cyclic transport, existence of its geometric
comparison line, or the selected regulator norm.

## 3. The actual minimal meridian operator descends

Let I be the actual all-level annihilator ideal in

    R_M=C(q,M)[T;sigma], sigma(M)=qM.

It is nonzero by [the finite cut-state proof](finite_sum_annihilator.md).
The involution iota(M)=-M, iota(q)=q, iota(T)=T commutes with sigma.
Equation (2.2) implies iota(I)=I: evaluate any actual annihilating
equation at -M. Coefficient specializations are understood after
clearing denominators, as in that all-level definition.

Every coefficient decomposes uniquely as a_0(q,Y)+M*a_1(q,Y).
Thus P=P_0+M P_1 in I implies P_0=(P+iota(P))/2 and
M P_1=(P-iota(P))/2 are in I, and so is P_1. The descended ideal in

    R_Y=C(q,Y)[T;sigma], sigma(Y)=q^2Y

is consequently nonzero. If P is the unique monic least-order
operator in I, P-iota(P) has smaller order and is zero. Its coefficients
lie in C(q,Y); minimal order is unchanged by the descent.

The full state also gives an iota-stable ideal: its parity scalar
(-1)^(N-1) is nonzero and cancels in the same argument at every level.
Its shift gauge is rational in q,Y. No descent in q is inferred.

Classically, twisting an SL(2) knot representation by the sign
character of its abelianization sends M to -M and fixes the preferred
longitude. The full lifted peripheral locus descends to (Y,L).
Individual irreducible lift components may be exchanged by this twist;
their separate evenness is not assumed.

## 4. The natural root norm torsor has degree N

At a level where its leading/trailing coefficients and companion
specialization are defined and nonzero, specialize the descended
specified module at q_N. On C(Y)
write T=B(Y)sigma, sigma(Y)=Q_NY. Its order is N, and

    H_N=B(Y)B(Q_NY)...B(Q_N^(N-1)Y),
    D_N(U,W)=det(W-H_N), U=Y^N=M^(2N).              (4.1)

Translation conjugates H_N by B, so D_N belongs to C(U)[W]. On a
simple spectral component with function field k, set S=k[Y]/(Y^N-U).
The eigenline has rank one over this cyclic etale algebra. In a frame
T e=a e and Norm_(S/k)(a)=W. Thus the norm torsor has dimension N-1.
The intrinsic Hilbert-90 comparison and cyclic stable lattice apply
with this N, retaining apparent poles and the pointing.

The reduced rational period in Y forces a W=1 sector. This identifies
neither that sector nor D_N with the geometric classical A-curve.
Matching the order of the factorial parameter does not identify the
fixed-center and fixed-semiclassical-shape trajectories.

## 5. The full ADO period retains the even-level sign

The independently fixed full normalization is

    d_N(M)=eta_N M^(N-1)/S_N(Y),
    S_N(Y)=1+Y+...+Y^(N-1), eta_N=i^(N+3).

Consequently d_N(-M)=delta_N d_N(M), delta_N=(-1)^(N-1). Its rational
shift gauge factors as

    g(q,Y)=-q^(-1)(QY-1)/(Y-1)
          =kappa(q)*sigma(f)/f,
    kappa(q)=-q^(-1), f=Y-1.                       (5.1)

At the actual root kappa=q^(N-1), and exactly

    Norm_N(g)=kappa^N=delta_N.                     (5.2)

The full state has W=delta_N: W=-1 at even N and W=1 at odd N.
After the explicit constant-character twist kappa, the remaining
Hilbert-90 comparison is the rational frame f. The entire scalar is

    d_N(M)=eta_N M^(N-1)(1-Y)/(1-U).               (5.3)

Retain its central factor and germ at U=Y=1; d_N(1)=eta_N/N.
At even N the full period is a section of this parity line over
the quadratic M-cover, rather than a rational function of Y.

For rank d, the scalar twist gives, up to companion-frame gauge,

    H_N^full=delta_N H_N^reduced,
    D_N^full(U,W)=delta_N^d D_N^reduced(U,W/delta_N). (5.4)

These are signed root norm identities, not classical A-polynomial
identities. They retain the factors lost by an unmarked comparison
of norm-one sectors.

## 6. The former 2N norm is the square of this one

Extend the same module to C(M), with sigma(M)=q_NM. Its coefficients
still depend only on Y and sigma^N(Y)=Y. Therefore

    H_(2N)=H_N^2,
    D_(2N)(U,V)=(-1)^d Res_W(D_N(U,W),W^2-V).        (6.1)

Over a splitting field the latter is the elementary identity
product_i(V-lambda_i^2)=(-1)^d product_i(lambda_i^2-V), so it holds
also with repeated eigenvalues. The former 2N-description retains
V=W^2; the N-description retains the sign W=delta_N. No sign has
been removed by a numerical evaluation at M=1.

## 7. The regulator conversion agrees with the actual half-step

Put H=Log Q=2pi*i/N, u=Log M. The action in the longitude note obeys
dS_Q=2 Log(L) du, equivalently dS_Q=Log(L) dLog(Y). The full geometric
peripheral rows are m=Y,l=L^2, whose exponent determinant in (Y,L)
is two. Hence the marked regulator is

    R=S_Q-(1/2)Log(Y)Log(L)=S_Q-u Log(L).           (7.1)

This is the action already calibrated by Im S_Q=Vol at completeness.
In the original M-shift parameter h=Log q=H/2, the action is S_q=S_Q/2
and the peripheral exponent determinant is four. Both give the same
exponential and invariant regulator norm. This resolves a parameter
and parity conversion, not selection or cancellation in the finite
period.

The subsequent [integral half-longitude theorem](integral_half_longitude.md)
now realizes this conversion directly in the saturated edge lattice:
the preferred longitude has a unique integral half-class and pairs
by -1 with the actual marked meridian. Its Weyl lift satisfies
TY=QYT at every level. The square of that lift retains an explicit
edge character, and at even N its central sign cannot be changed
by replacing T with -T. This supplies the marked boundary algebra;
the actual central lift and selected source still require matching.

## 8. Verification

[The exact audit](../experiments/audit_even_meridian_descent.py)
compares 40 dense cut matrices at generic auxiliary parameters and
actual roots. It checks local longitude norms and the full sign at ten
levels including even and composite ones, and symbolically verifies
the spectral square identity in ranks one through three. All checks
passed; the proofs above are uniform. Results are in
[the audit output](../experiments/even_meridian_descent_results.json).

    python3 experiments/audit_even_meridian_descent.py
