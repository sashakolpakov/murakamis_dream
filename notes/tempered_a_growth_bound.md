# A general A-operator growth bound with the cyclic source retained

Research note, 27 October 2026. This gives a one-sided exponential
estimate for the original pointed period, under explicit conditions
on a specified actual quantum A-operator. The proof allows eigenvalue
collisions, nonnormal matrices and exactly vanishing leading columns.
It uses the finite jet source, rather than assuming a regular growing
solution of a classical recurrence. There is no bridge-number bound.

The estimate is an upper bound, not the volume conjecture. Its
classical largest-root integral can be strictly larger than the
selected period's rate. Sections 6--7 make that limitation explicit.

## 1. The Bloch boundary relation forces roots of unity at a leading edge

This general algebraic property already follows from our marked
Bloch relation; no published K-theory proof is needed here. On the
function field of a geometric gluing curve, or a finite augmented
cover of its peripheral curve, the existing calculation gives

    sum_j epsilon_j z_j wedge (1-z_j)=-2 M wedge L
                                 in wedge^2(F^* tensor Q). (1.1)

For a discrete valuation v and units after uniformizer extraction,
define the multiplicative residue

    tau_v(f,g)=(-1)^(v(f)v(g))
                [f^v(g)/g^v(f)]_residue.                (1.2)

It is multiplicative in each input, and alternating after tensoring
the target with Q. Directly tau_v(z,1-z)=1: when v(z)>0 the
residue of 1-z is 1; when v(1-z)>0 that of z is 1; when v(z)<0
the quotient z/(1-z) has residue -1, and the two sign exponents
sum to v(z)^2+v(z), which is even. The remaining unit case is
immediate. Thus (1.2) applied to (1.1) makes tau_v(M,L) torsion.

At a place where M has finite nonzero residue M_0 and L has a
pole, this says that M_0^v(L) is a root of unity. Hence M_0 is
a root of unity. If the valuation is first defined on the
peripheral curve, extend it to the finite gluing field; the
valuation order is multiplied by its positive ramification index
and the same conclusion follows. This keeps the marked lifts.

Every nonzero root of the leading L coefficient of a geometric
A-factor gives a point (M_0,infinity) of its projective closure.
A place on the normalization above that point has v(M)=0 and
v(L)<0, so the preceding argument applies. The same conclusion
holds in the squared meridian Y=M^2. Thus that leading coefficient
has only roots of unity in C^*, apart from its Laurent monomial.
This is the leading-edge part of the usual temperedness property.

This proof concerns the geometric peripheral factor supported by
(1.1). It does not identify a given actual quantum operator's
classical symbol with that factor, remove additional operator
factors, or prove a quantum deformation is unramified.

## 2. Conditions for a source-preserving growth estimate

Use a specified even-meridian actual all-level annihilator

    A=sum_(i=0)^d a_i(q,Y) T^i, T Y=q^2 Y T,
    Y=M^2, a_i in C[q^(+/-1),Y^(+/-1)].                 (2.1)

Even descent for the original state was proved in
[the signed norm note](even_meridian_norm_descent.md). Clear
denominators and remove a common power of q-1. Assume:

1. a_0(1,Y) and p(1,Y), p=a_d, are nonzero Laurent polynomials.
2. Every zero of p(1,Y) on |Y|=1 is a root of unity.
3. Near each such zero zeta the zero divisor of p(q,Y) splits
   into analytic branches Y=lambda_r(q), lambda_r(1)=zeta,
   with multiplicity allowed. Its local remaining factor is a unit.

The third condition holds for simple classical roots, and for
products of the usual binomials 1-zeta q^a Y^b. It is a genuine
condition: a ramified Puiseux branch is not silently treated as
analytic. Roots away from the unit circle require no such condition.
The theorem does not claim these conditions for every knot's
unknown minimal operator. They are directly checkable operator data.

Let A_cl(Y,L)=sum a_i(1,Y)L^i and, outside the finite leading-zero
set, let

    R(theta)=max{|L|:A_cl(exp(i theta),L)=0},
    E(A)=integral_0^(2pi) log R(theta) dtheta.           (2.2)

The logarithmic singularities at the excluded finite set are
integrable, as shown in Section 5. No selected source is replaced
by a choice of the largest root in the definition of the invariant.

**Pointed growth theorem.** Under conditions 1--3, the original
Kashaev value recovered from this actual operator satisfies

    limsup_(N->infinity) (2pi/N)log|<K>_N| <= E(A).      (2.3)

Zero values on the left are interpreted as log 0=-infinity.
For the positive pointed Gram period of the previous note,

    limsup_(N->infinity) (pi/N)log G_N <= max(0,E(A)).    (2.4)

We prove these statements below. Neither is an equality assertion.

## 3. A fixed-size positive transport keeps every singular step

Use the exact generic color recurrence and bounded q-jet budget B
from [the pointed Gram construction](pointed_a_gram_period.md).
Write V_j=(C_j,...,C_(j+d-1))^t. Before specializing any root,

    p(q,q^(2j)) V_(j+1)=N_j(q) V_j,                    (3.1)

where N_j has p on its superdiagonal and last row
(-a_0,...,-a_(d-1)), evaluated at Y=q^(2j). Put q=q_N(1+t)
and use the scaled variable s=N t. Let K_(N,j) be the lower
Toeplitz lift of N_j(q_N(1+s/N)) through s-degree B. Its size
is d(B+1), independent of N, and its entries are uniformly bounded.

Let m_j be the actual order of p(q,q^(2j)) at q_N and define

    eta_j=[s^m_j]p(q_N(1+s/N),q_N^(2j)(1+s/N)^(2j)),
    beta_N=sum_(j=j_*)^(N-d)m_j <= B.                   (3.2)

The fixed small-color jet column u_N is bounded. Multiplying (3.1)
in the generic field and only then taking the indicated coefficient
gives the exact formula

    <K>_N=e_(beta_N,d)^t
       K_(N,N-d)...K_(N,j_*)u_N / product_j eta_j.       (3.3)

Indeed the unlifted numerator is (product_j p_j)V_(N-d+1).
The product has first nonzero s-coefficient product_j eta_j in
degree beta_N, and the color column is regular. Thus (3.3)
does not divide by a vanishing specialized leading coefficient.

There is an exact positive transport of its squared norm. With
rho_0=u_N u_N^dagger propagate

    rho_(j+1)=K_(N,j) rho_j K_(N,j)^dagger,
    |<K>_N|^2=Tr(E_(beta_N,d)rho_final)
                                      /product_j |eta_j|^2. (3.4)

The last effect is its specified rank-one coordinate projector.
All phases and jet couplings remain in the matrices and source.
This is a positive matrix transport, not an entrywise-positive
recurrence or a license to drop the source. The denominator is
the same whole leading germ used in the original A-period.

## 4. The leading germ has a controlled logarithmic product

Under conditions 2--3 one has

    sum_j log|eta_j|=N I_p+O(log N),
    I_p=(1/(2pi))integral_0^(2pi)log|p(1,exp(i theta))|dtheta.
                                                        (4.1)

Here is a proof retaining exact root zeros. Away from a fixed
neighborhood of the classical unit-circle zeros, p(q_N,Y)/p(1,Y)
is uniformly 1+O(1/N). Near a zero zeta, each analytic root branch
moves by O(1/N). At grid points with distance at least K/N from
zeta, choose K large enough so the root displacement is less
than half that distance. Factoring locally gives a log-modulus
error O(1/(N distance)). Summation over these points costs O(log N).

Only a bounded number of points lie within K/N of zeta. Because
zeta is a root of unity, write zeta=exp(2pi i a/r). On each
residue class of N modulo r, every such point is

    j=aN/r+k, Y_j=zeta q_N^(2k),                      (4.2)

where k is in a fixed finite set of rational numbers; use both
endpoint representations a/r=0,1 when zeta=1. Its ordinary value
is a fixed analytic germ p(q,zeta q^(2k)) at q=1. Unless
identically zero, that germ has a finite order, so its nonzero
value at q_N is bounded above and below by powers of N.

For an exactly zero value use the q-jet along the actual color
trajectory. A coefficient of fixed jet degree is a finite sum
of terms

    c zeta^b q_N^(u+2bk) N^(-m)
                       binom(u+2b(aN/r+k),m).           (4.3)

Here u is the q-exponent of the monomial and b its Y-exponent.
Formula (4.3) is meromorphic in 1/N with a finite-order pole or zero.
The finite-monomial Vandermonde bound from the jet theorem bounds
the first nonzero degree m. For each of the finitely many residue
classes and offsets, that leading coefficient is therefore bounded
above and below by powers of N for all sufficiently large N.
If all bounded-degree germs vanished identically, their evaluations
would violate that Vandermonde bound on every large actual trajectory.
Thus exact zeros, including coalescing analytic branches, cost only
O(log N) at this bounded number of points. The fixed discarded
initial and final colors have the same control.

Finally the classical grid product itself has the claimed mean.
Factor p(1,Y) over C. Off-circle roots contribute N times their
circle mean plus O(1), by the identity product_(Y^N=1)(Y-lambda)
=(-1)^N(lambda^N-1). A unit-circle root of unity either has
zeta^N!=1, giving a nonzero value in a finite set, or is a grid
root. In the latter case omitting its zero factor gives modulus N
by differentiating Y^N-1 at zeta. Multiplicities and the fixed
removed points add O(log N). Combining these facts proves (4.1).

The analytic-branch condition is used exactly in the O(1/N)
displacement above. Classical temperedness alone does not prove it.

In particular, if p(1,Y) is a Laurent monomial times cyclotomic
factors with leading scalar of modulus one, then I_p=0. The
entire product of leading germs is then bounded above and below
by powers of N. Individual factors may still vanish or become
numerical multipliers at a root. Their complete germs, rather
than those separate numerical values, give this conclusion.

## 5. A direct upper bound for slowly varying matrix products

We need only the following elementary norm lemma. Suppose bounded
matrices K_(N,j) tend uniformly to a continuous matrix K(x), x=j/N,
of fixed dimension. If log rho(K(x)) is integrable, then

    limsup (1/N)log||product_j K_(N,j)||
                       <=integral_0^1 log rho(K(x)) dx. (5.1)

For completeness first fix epsilon>0 and set a(x)=rho(K(x))+epsilon.
The matrix

    H(x)=sum_(n>=0)(K(x)^dagger)^n K(x)^n/a(x)^(2n)

converges uniformly, is continuous, satisfies H>=I and is bounded
above on the compact interval. Uniform convergence follows, for
example, by unitary triangularization: bounded upper triangular
matrices of fixed size have power growth bounded by a fixed
polynomial times (rho+epsilon/2)^n, uniformly with constants
depending on epsilon and the dimension. Its induced norm obeys
||K(x)v||_(H(x))<=a(x)||v||_(H(x)).

Uniform convergence of K_(N,j) and uniform continuity of H make
each step cost at most a(j/N)+o(1), and the change between the
two neighboring H norms costs 1+o(1), uniformly. Multiplying, taking
logarithms, and dividing by N yields integral log(rho+epsilon).
Let epsilon decrease to zero. In the present application integrability
and the passage to that limit follow from the polynomial lower
bound on rho stated below. No diagonalization through an eigenvalue
collision and no spectral-gap hypothesis enters this upper bound.

For our lifted matrices the limit K(x) is lower triangular in
jet degree, with the same diagonal block at every degree:

    N_0(x)=[0 p 0 ...; ...; -a_0 -a_1 ... -a_(d-1)]
                                     at q=1,Y=exp(2pi i x).

Therefore rho(K(x))=rho(N_0(x)). Where p!=0 its eigenvalues are
p(1,Y)L_i(Y), so

    log rho(K(x))=log|p(1,Y)|+log R(2pi x).             (5.2)

Both sides are integrable. Indeed the characteristic coefficients
of N_0 are a_i p^(d-1-i), and a_0 p^(d-1) is nonzero by condition 1.
Their finite-order zeros give a polynomial lower bound on rho near
its finitely many possible zeros. This justifies the limiting norm
argument as well as the integral in (2.2).

Apply (5.1) to (3.3). The input is bounded, the selected coordinate
has norm one, and (4.1) subtracts I_p from the growth rate. Equation
(5.2) gives (2.3). The polynomial ordinary-color remainder in the
Gram theorem then gives (2.4). This proves the pointed upper bound.

## 6. The source prevents turning this bound into a volume formula

An exact countercheck is the unknot with the actual annihilator

    (T-c)(T-1), c>1,
    C_j(q)=1 for every color.

All conditions above hold. The entropy is E=2pi log c, but the
selected period is identically one and has zero rate. Its source
is entirely in the L=1 line; the positive evolution (3.4) retains
this fact. The same left multiplication can be applied to an
actual hyperbolic knot operator and can enlarge E arbitrarily
without changing its pointed period. Thus source reachability
and a sharp estimate cannot be inferred from root moduli alone.

Even full classical temperedness does not fix this source issue.
Let C(Y,L) be the figure-eight geometric polynomial displayed below,
and form the dummy left factor C(Y,T). The operator
C(Y,T)(T-1) is an actual annihilator of the unknot's constant
period. Its classical symbol is (L-1)C(Y,L), whose edge
polynomials are cyclotomic, yet its selected period is still one.
This is not claimed to be a standard quantum figure-eight operator;
it is an exact countercheck on any argument using only the
tempered characteristic polynomial and omitting the actual source.

There is also a useful geometric calibration. For the figure-eight
geometric polynomial in Y,L,

    A_geo=L^2-(Y^2-Y-2-Y^(-1)+Y^(-2))L+1,

put c(theta)=1+cos theta-cos(2theta). Then log R is
arcosh c(theta) on (0,2pi/3) and (4pi/3,2pi), and is zero on
the remaining arc. Hence

    E(A_geo)=2 integral_0^(2pi/3)arcosh c(theta)dtheta
            =2 Vol(4_1).                               (6.1)

The last equality is the already calibrated
[classical cone/regulator comparison (historical context omitted)](quantum_a_volume.md),
not an identification of that note's custom transfer state with
Kashaev. This factor of two shows why the full-circle largest-root
integral is not the desired selected volume. The quantum boundary
and resonance data must choose the appropriate action; (2.3)
does not prove that selection or its lower bound.

## 7. Coverage and remaining scope

The leading-edge root-of-unity statement has existing coverage in
[Cooper--Culler--Gillet--Long--Shalen, Proposition 5.10](https://homepages.math.uic.edu/~culler/papers/PlaneCurves/curves.pdf).
The direct residue proof in Section 1 uses only our recorded Bloch
boundary relation. Existing regular q-difference asymptotics include
[Garoufalidis--Geronimo](https://arxiv.org/abs/math/0405331), whose
abstract specifies noncollision and nonvanishing assumptions. Only
their stated scope was used for coverage; none of their proofs is
a premise for Sections 3--5.

The new step relative to the previous repo notes is a one-sided
estimate for the actual pointed A-period that retains the complete
cyclic leading germ, a bounded number of singular jets, and its fixed
source, while allowing eigenvalue collisions. It requires the
explicit leading-divisor hypotheses in Section 2. It neither proves
those hypotheses for every knot operator nor proves a sharp geometric
rate. Identifying and estimating the source-selected geometric action
is still the central unresolved part of the volume conjecture.

[Audit](../experiments/audit_tempered_a_growth.py).
[Results](../experiments/tempered_a_growth_results.json).
