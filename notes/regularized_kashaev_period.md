# The regular ADO period, its bounded source, and a cyclic trace

Research note, 26 October 2026. This isolates a canonical regular period
of the actual literature state. All its polar data come from ordinary
colors and have polynomial size at the specified principal root. The
regular period at completeness is exactly a weighted field trace on
the squared-meridian cyclic algebra. Any specified actual all-level
operator gives it a rootwise affine equation with a source in a fixed
finite-dimensional Laurent space, with polynomially bounded coefficients.

These statements hold for every knot. They neither prove that this
source couples to the geometric branch nor establish the volume limit.
They do not identify this rootwise source with a fixed generic rational
source or import a published volume theorem.

## 1. The actual pointing and the statement

Fix a b-strand braid closing to a zero-framed knot. The parameters and
state are those of [the ADO audit](kashaev_ado_pointing.md):

    q_N=exp(pi*i/N), Q_N=q_N^2, Y=M^2,
    F_N(Y) in C[Y,Y^(-1)],
    F_N(1)=K_N=<K>_N,
    F_N(Q_N^j)=C_j(q_N), 1<=j<N.                  (1.1)

The evenness and operator descent to Y were proved in
[the squared-meridian note](even_meridian_norm_descent.md).
The integer-color identities are the independently proved
[quotient-color pointing](root_orbit_pointing.md). Here C_j has unknot
value one; it is used to control exact polar data, not through a Jones
asymptotic assumption.

Put zeta_j=Q_N^j and S_N(Y)=1+Y+...+Y^(N-1). There is a unique polynomial
P_N of degree at most N-2 with

    P_N(zeta_j)=C_j(q_N), 1<=j<N.

Define

    p_N(Y)=P_N(Y)/S_N(Y),
    R_N(Y)=(F_N(Y)-P_N(Y))/S_N(Y).                 (1.2)

Then R_N is Laurent polynomial. With eta_N=i^(N+3), the exact full
ADO state decomposes as

    N_N(M)=eta_N M^(N-1) R_N(M^2)
                       +eta_N M^(N-1) p_N(M^2).  (1.3)

The second term has every polar principal part of the full state away
from M=0 and infinity. The first term is regular there. This prescription
is canonical in the marked Y-coordinate: p_N has precisely those simple
principal parts, is regular at zero, and tends to zero at infinity.

The main conclusions, proved below, are:

* All C_j(q_N), 1<=j<N, satisfy the uniform bound
  |C_j(q_N)|<=[j]_(q_N)^(b-1)<=D_N, where
  D_N=sin(pi/N)^(1-b)<=(N/2)^(b-1).
* |p_N(1)|<=D_N. Thus the regular full period and the full ADO value at
  completeness differ by a polynomially bounded quantity.
* Exactly

      R_N(1)=(1/N) Tr_(C(Y)/C(U))(Y F_N(Y))|_(U=1), U=Y^N.       (1.4)

* A specified actual all-level operator, after a fixed rational gauge
  and denominator clearing, gives an affine equation for R_N. Its
  source has Laurent support in a fixed interval and coefficients
  O(D_N), independently of N.

The last claim concerns meridian functions at each root. No corresponding
bound on q-derivatives transverse to the root is inferred.

## 2. A positive trace bounds all the ordinary colors

We reconstruct the finite algebra needed for the bound. Assume N>=3,
theta=pi/N, and put

    delta=2cos(theta),
    mu_a=sin((a+1)theta)/sin(theta), 0<=a<=N-2.

All mu_a are positive; with mu_(-1)=mu_(N-1)=0 they obey
mu_(a-1)+mu_(a+1)=delta*mu_a. Let H_m have the orthonormal basis of
length-m walks on the chain 0,...,N-2 starting at zero. On a walk a,
define U_i to be zero unless a_(i-1)=a_(i+1)=c. Otherwise it replaces
the middle height a_i by a neighbor a_i' of c, with matrix entry

    (U_i)_(a',a)=sqrt(mu_(a_i')mu_(a_i))/mu_c.     (2.1)

Direct multiplication gives U_i*=U_i, U_i^2=delta U_i,
U_i U_(i+1) U_i=U_i, and commuting distant generators. For the square
use the displayed neighbor sum. In the adjacent product the middle
heights are forced at its two outer steps and the square-root ratios
cancel, leaving the single U_i entry. Thus these are actual
Temperley--Lieb matrices. The braid matrix

    B_i=q_N^(1/2) I-q_N^(-1/2) U_i                (2.2)

is unitary: its two eigenvalues are q_N^(1/2) and -q_N^(-3/2).
The braid relation follows by expanding and using the three local
Temperley--Lieb relations.

The nonnormalized positive trace is

    tau_m(A)=sum_walks mu_(a_m) A_(a,a).           (2.3)

Endpoint preservation makes it tracial. The neighbor sum gives
tau_(m+1)(A tensor I)=delta*tau_m(A), and (2.1) gives
tau_(m+1)((A tensor I)U_m)=tau_m(A). These identities determine
the diagram trace: every Temperley--Lieb diagram at the next level
is in the span of the included algebra and A U_m B, and cyclicity
reduces the latter trace to the preceding level. In particular this
trace agrees with the algebraic closure trace.

Here is its connection with the fixed actual R. On the ordinary
two-dimensional color, after retaining the common Cartan scalar,

    R_checked=q^(1/2) I-q^(-1/2) U,

where U is zero on 00 and 11 and has block

    U|_(01,10)=[ q  -1 ; -1  q^(-1) ].            (2.4)

This follows by substituting E v_1=v_0 into the actual finite R.
It obeys U^2=(q+q^(-1))U and the adjacent relation. With
K=diag(q,q^(-1)), its partial quantum trace is I. Thus the actual
quantum trace has precisely the two trace recursions above and
equals (2.3), even though (2.4) itself is not Hermitian in the
unmodified tensor basis.

For completeness the j-color is represented by the idempotent p_(j-1).
The recursion, within the requisite tensor power, is

    p_0=p_1=I,
    p_(m+1)=p_m tensor I
       -[m]/[m+1]*(p_m tensor I)U_m(p_m tensor I).  (2.5)

The Temperley--Lieb relations inductively give
p_m U_i=U_i p_m=0 for i<m and
(p_m U_m p_m)^2=([m+1]/[m])p_m U_m p_m; substituting this last identity
in (2.5) verifies idempotence at the next step. All coefficients are
real and denominators nonzero in the range used here. Hence these
idempotents are orthogonal projections in (2.1). The trace recursion
and delta*[m+1]-[m]=[m+2] give

    tau_m(p_m)=[m+1].                              (2.6)

This also verifies the actual color rather than assigning it by name.
For generic q the common kernel of the U_i in V_1^(tensor m) has
one vector at each weight: each adjacent exchange imposes the
q-ratio read from (2.4), and adjacent exchanges connect all words
of that weight. These m+1 vectors are F^r(v_0 tensor ... tensor v_0),
with E F^r=[r][m-r+1]F^(r-1). Thus the image is exactly the ordinary
(m+1)-dimensional highest-weight color. This identity specializes
for m<=N-2, when all needed denominators remain nonzero. Cabling
the actual finite R and restricting to these images gives its color
R by the coproduct identity; equivalently expand the coproduct powers
by the q-binomial formula. This is the same color comparison proved
in [the degree note](adequacy_and_algebraic_periods.md#3-passing-from-parallel-strands-to-the-actual-color).

For a b-strand braid colored by j<N, the tensor product P of these
projections has positive trace [j]^b. The cabled braid is unitary,
preserves P, and its framing correction has modulus one. On the
image of P each diagonal entry of a unitary has modulus at most one.
The positive trace therefore gives

    |C_j(q_N)|<=tau(P)/[j]=[j]^(b-1).              (2.7)

This is uniform in j,N. For N=2 only j=1 occurs and the statement
is immediate. Since sin(pi/N)>=2/N, the D_N bound in Section 1 follows.
At j=N the positive trace of the corresponding projection is zero;
division by [N] is unavailable. Nothing here bounds the Kashaev color.

## 3. The exact principal parts and the regular remainder

At a root zeta_j of S_N,

    S_N'(zeta_j)=N*zeta_j^(-1)/(zeta_j-1).

Lagrange interpolation gives

    P_N(Y)=sum_(j=1)^(N-1) C_j(q_N)
                        *S_N(Y)/((Y-zeta_j)S_N'(zeta_j)),
    p_N(Y)=sum_(j=1)^(N-1)
      C_j(q_N)*zeta_j*(zeta_j-1)/(N*(Y-zeta_j)).    (3.1)

The roots are simple and F_N-P_N vanishes at all of them. Since
S_N(0)=1, division in the Laurent ring proves R_N is Laurent polynomial.
It also gives the whole wall value

    R_N(zeta_j)=(F_N'(zeta_j)-P_N'(zeta_j))/S_N'(zeta_j).         (3.2)

The full state's phase, its monomial M^(N-1), and every divisor
in S_N remain in (1.3). This is an identity of meridian germs,
not a replacement of any factor by its numerical value at M=1.
In particular both summands retain parity (-1)^(N-1) on the M-cover.

Putting Y=1 in (3.1) gives

    P_N(1)=-sum_(j=1)^(N-1) zeta_j C_j(q_N),
    p_N(1)=-(1/N)sum_(j=1)^(N-1) zeta_j C_j(q_N),
    |p_N(1)|<=D_N,
    K_N=N R_N(1)+P_N(1).                          (3.3)

The interpolation coefficients themselves are

    [Y^r]P_N=(1/N)sum_j C_j(q_N)(zeta_j^(-r)-zeta_j),
    0<=r<=N-2.                                   (3.4)

They have modulus at most 2D_N. More usefully, every Taylor
coefficient of the proper polar function at zero satisfies

    [Y^r]p_N=(1/N)sum_j C_j(q_N)(1-zeta_j)zeta_j^(-r),
    |[Y^r]p_N|<=2D_N, r>=0.                      (3.5)

This direct formula avoids estimating a growing Vandermonde inverse.

The subsequent [actual Weyl-descent proof](actual_weyl_descent.md)
now proves C_(N-j)=C_j for every knot in these conventions. It
rewrites (3.5) as an exact sine-matrix moment and improves its
bound to D_N. Thus the bounded Laurent source has an explicit
Weyl structure, without a new quantum-state definition. Its
geometric coupling and cross-level norm remain unproved.

## 4. Any actual operator supplies a bounded rootwise source

Take the specified actual all-level reduced operator in squared-meridian
coordinates,

    P_hat=sum_(j=0)^d a_j(q,Y)T^j, T Y=q^2Y T.

Existence and descent were proved in the
[finite-state](finite_sum_annihilator.md) and
[even-meridian](even_meridian_norm_descent.md) notes. Let f=Y-1.
Choose and retain a fixed nonzero clearing factor c(q,Y) so that

    A_hat=c*f*P_hat*f^(-1)
          belongs to C[q^(+/-1),Y^(+/-1)][T].       (4.1)

At the actual root U=Y^N is shift-invariant, and
F_N/S_N=f F_N/(U-1). Therefore exactly

    A_hat(F_N/S_N)=0,
    A_hat R_N=b_N, b_N=-A_hat p_N.                 (4.2)

This is the full ADO normalization after extracting its explicitly
known eta_N M^(N-1). Equivalently this extraction twists the full
shift by kappa=-q^(-1), retaining its N-cyclic sign (-1)^(N-1).
It is not a new chosen knot state.

Write the Laurent support of all coefficients of A_hat as contained
in [r_-,r_+]. The source b_N is Laurent polynomial: (4.2) also equals
A_hat R_N, which has no finite nonzero poles. At zero every shifted
p_N is O(1); at infinity every shifted p_N is O(Y^(-1)). Hence

    b_N in span{Y^r : r_-<=r<=r_+-1}.              (4.3)

This finite-dimensional space is independent of N. Empty intervals
mean the source is zero; nonvanishing or geometric coupling is not
being assumed.

There is also a uniform bound on its coefficients. If
a_(j,e)(q) is the coefficient of Y^e in A_hat's j-th term, the
coefficient of Y^k in -A_hat p_N is a sum of

    -a_(j,e)(q_N)*Q_N^(j*(k-e))*[Y^(k-e)]p_N,
    k-e>=0.

Equation (3.5) and |Q_N|=1 bound it by

    2D_N sum_(j,e)|a_(j,e)(q_N)|=O_A(D_N).         (4.4)

The sum is bounded because A_hat is fixed and Laurent polynomial
in q. The argument holds at all sufficiently large levels where
the specified annihilation identity applies. Every fixed meridian
jet of b_N at Y=1 has the same polynomial bound, since its Laurent
support is fixed. Restoring the full monomial contributes only
the corresponding fixed powers of N to such jets.

This removes a rational-source-factorization hypothesis from this
*rootwise* construction. It does not prove that the coefficients
of b_N come from a single rational function b(q,Y), that its generic
difference-extension class is the earlier one, or that q-jets of
those coefficients are bounded. The latter are not controlled by
principal-root unitarity.

The individual rootwise affine equation has the rational particular
solution R_N, so it splits over that root field. This does not split
the generic all-level extension: the source coefficients and the
selected sections have not been algebraized in q. The cross-level
period and its regulator norm remain the issue.

There is a useful pointed uniqueness statement under a separate
rank hypothesis. Suppose the rational homogeneous solutions of A_hat
form the one-dimensional C(U)-line generated by u_N=F_N/S_N. Then
every rational solution of (4.2) regular at both Y=Q_N and Y=1 has
the same value R_N(1). Indeed the difference of two such solutions
is c(U)u_N. The anchor C_1=1 makes u_N have a nonzero simple pole
at Y=Q_N, so regularity there forces c to vanish at U=1. Since
u_N is regular at Y=1, the difference has value zero there.
Thus this source and its two meridian lattices determine the
complete period without a remaining central scalar. Rank one
is sufficient, not asserted for every actual knot operator.

## 5. The complete regular period is an intrinsic cyclic trace

Let E_N=C(Y), K_N^cent=C(U), U=Y^N. The extension is cyclic with
sigma(Y)=Q_NY, and

    Tr_(E_N/K_N^cent)(Y F_N(Y))
      =sum_(j=0)^(N-1) Q_N^j Y F_N(Q_N^jY).       (5.1)

It is Laurent polynomial in U; its whole value at U=1 is defined.
Equations (1.1) and (3.3) give

    t_N:=R_N(1)=(1/N)Tr(Y F_N)|_(U=1).            (5.2)

Thus the regularized complete value is already an algebraic period
pairing on the actual cyclic object. The functional uses the marked
monomial Y, not a selected eigenvalue with largest modulus. An anchored
central rescaling F_N->c(U)F_N, c regular and c(1)=1, preserves it.
An unpointed Hilbert-90 module alone still does not supply F_N.

More generally every Fourier coefficient

    t_(N,r)=(1/N)sum_(j=0)^(N-1) zeta_j^(-r)F_N(zeta_j)

satisfies |t_(N,r)-K_N/N|<=D_N. The particular r=N-1 is (5.2).
If the target volume is positive, exponential growth with that rate
for K_N is equivalent to the same growth for any of these coefficients:
their differences from K_N/N are polynomial, and log N/N tends to zero.
This is an equivalence of the conjecture, not a proof of either side.

## 6. A positive trace norm gives another exact formulation

On S_1=C[Y]/(Y^N-1), define the involution by conjugating coefficients
and sending Y to Y^(-1). At the actual principal root it preserves the
cyclic structure. The pointed state has the positive squared trace norm

    H_N=(1/N)Tr_(S_1/C)(F_N^* F_N)
       =|K_N|^2/N+(1/N)sum_(j=1)^(N-1)|C_j(q_N)|^2,
    0<=H_N-|K_N|^2/N<=D_N^2.                      (6.1)

For a hyperbolic knot with volume V>0, the following statements are
equivalent:

    (2pi/N)log|K_N| -> V,
    (2pi/N)log|t_N| -> V,
    (pi/N)log H_N -> V.                           (6.2)

For example the first implication uses (3.3): a polynomial term is
exponentially smaller than a sequence of positive exponential rate.
The converse follows from the same identity. The norm equivalence
follows directly from the positive identity (6.1). Equivalently the
regulator target log||P_hyp||=2V/pi becomes

    (4/N)log|t_N|-log||P_hyp|| ->0,
    (2/N)log H_N-log||P_hyp|| ->0.                 (6.3)

The positivity here controls the semisimple tail. It does not estimate
the complete regular period or prove its geometric coefficient.

## 7. Why a regularized period is needed at the complete point

The anchor and evenness give F_N(q_N)=F_N(-q_N)=1. Therefore a
nonvanishing geometric WKB amplitude uniformly valid across both
M=1 and M=q_N cannot directly describe the reduced state if it has
positive volume growth. Indeed a holomorphic geometric action with a
nonzero finite shift multiplier, and an amplitude whose ratio at those
points tends to a nonzero number, would give a nonzero finite limit
for F_N(q_N)/F_N(1). The anchor would then exclude positive exponential
growth of F_N(1).

The exact decomposition explains how such an inference fails:

    F_N(Y)=S_N(Y)R_N(Y)+P_N(Y).                    (7.1)

The regular term is multiplied by a function with S_N(1)=N and
S_N(zeta_j)=0 for every ordinary orbit color. The actual full ADO
normalization precisely removes that function, leaving the regular
period R_N and the controlled polar part. The zeros and poles occur
at spacing O(1/N); a coefficientwise formal branch cannot erase
their whole meridian germs. This uses the exact original factors,
including the sign character, rather than an asymptotic replacement.

The [geometric action proof](quantum_longitude_and_regulator_action.md)
and [triangulation bridge](triangulation_regulator_bridge.md) now provide
the marked regulator connection and norm to compare with t_N or H_N.
What remains is proving that this specified regular quantum period
has that norm. Bounded source coefficients alone do not prove its
coupling, noncancellation, or the geometric factor's survival in
the summed operator. No volume conjecture is claimed here.

The subsequent [normal-period construction](peripheral_normal_period.md)
keeps the factor Y-1 in the polynomial quantum module. Its complete
full ADO value is the first normal derivative of (Y-1)F_N across
U=1. A boundary-column argument gives a necessary factor condition
for positive volume growth. Under the stated rank, or checked
Weyl-sector invertibility, condition that derivative is an exact
inverse-matrix period with known bounded source. It equals R_N(1)
plus the controlled p_N(1), with the full phase retained. Its norm
comparison is still additional work.

## 8. Coverage and independent verification

Positive Temperley--Lieb path traces and unitary braid matrices are
existing theory; [Aharonov--Jones--Landau](https://arxiv.org/abs/quant-ph/0511096)
is one explicit coverage source. The connection of root-of-unity
nonsemisimple invariants with derivatives already has coverage in
[Murakami](https://arxiv.org/abs/1406.1287), while the ADO/integer-color
unification is covered by [Willetts](https://arxiv.org/abs/2003.09854).
No proof, completion theorem, or asymptotic result from those sources
is a premise here. Partial-fraction interpolation and cyclic field
traces are standard algebra; no novelty claim is made for them.

[The audit](../experiments/audit_regularized_kashaev_period.py) compares
30 positive colored path traces with independently assembled actual
highest-weight cut states, checks 62 principal-root color bounds
including colors next to the truncation wall, and checks the ADO
quotient-color identification at the small levels. Ten exact finite-
field Laurent cut calculations verify all polar divisions, every
ordinary-color value, the cancelled wall derivatives, and the weighted
cyclic trace identity. All checks passed. The uniform arguments above,
rather than these finite samples, prove the statements. Results are in
[the audit output](../experiments/regularized_kashaev_period_results.json).

    python3 experiments/audit_regularized_kashaev_period.py
