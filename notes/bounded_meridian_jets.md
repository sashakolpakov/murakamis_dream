# Bounded meridian jets for a fixed quantum A-operator

Research note, 25 October 2026. A fixed recurrence needs only a bounded
amount of meridian jet data to cross all singularities on a root orbit.
The bound depends on the operator, not the level. There is no rank-one
or regular-orbit hypothesis. The subsequent
[all-level period theorem](all_level_a_period.md) uses coherence across
levels to replace these potentially unknown meridian jets by controlled
jets of finitely many fixed small colors in the quantum parameter.

The state and conventions are those of
[the ADO pointing calculation](kashaev_ado_pointing.md):

    q_N=exp(pi*i/N), M_j=-q_N^j,
    F_N(M_j)=C_j(q_N), 1<=j<=N,
    F_N(1)=<K>_N, F_N(-q_N)=1.                       (0.1)

The C_j are the actual reduced fixed-color periods, not new initial
conditions chosen to obtain a desired asymptotic. Their identity in
(0.1) was independently proved by the filtered quotient-color argument
in [the root-orbit note](root_orbit_pointing.md).

## 1. A uniform bound on singularities

Take a specified nonzero reduced-state operator

    P=sum_(i=0)^d a_i(q,M)T^i, T h(M)=h(qM), d>=1.    (1.1)

Clear its rational denominators once, retaining the fixed operator and
the state normalization, so all a_i are Laurent polynomials. Let D be
the M-exponent span of a_d. For all sufficiently large N, a_d(q_N,M)
is a nonzero Laurent polynomial and its exponent span is at most D.
The excluded levels are finite: any one nonzero q-coefficient of a_d
has only finitely many nonzero roots.

Use the same local coordinate at each orbit point:

    M=M_j(1+z), M_j=-q_N^j.                           (1.2)

The points M_j, 1<=j<=2N, are distinct. The sum of the multiplicities
of all nonzero roots of a_d(q_N,M) is at most D. In particular,

    S_N=sum_(j=1)^(N-d) ord_(M=M_j) a_d(q_N,M) <= D.  (1.3)

This is a count with multiplicity. It does not require a torsion-point
classification, primeness of N, or estimates on nearly vanishing factors.

## 2. Exact recovery from finitely many initial jets

Write the forward companion equation on column states as

    V_j(z)=(F_N(M_j(1+z)),...,F_N(M_(j+d-1)(1+z)))^t,
    V_(j+1)(z)=B_j(z)V_j(z).

The superdiagonal of B_j is one; its last row is
(-a_0/a_d,...,-a_(d-1)/a_d), evaluated at (q_N,M_j(1+z)).
Each B_j has pole order at most the j-th summand in (1.3). Thus

    r_N(z)=e_d^t B_(N-d)(z)...B_1(z)
          =sum_(k=-S_N)^infinity r_(N,k) z^k.        (2.1)

Let

    J_k=([z^k]F_N(M_1(1+z)),...,
         [z^k]F_N(M_d(1+z)))^t.

All these are ordinary meridian germs of the actual Laurent polynomial
state. The scalar r_N(z)V_1(z) is regular and equals F_N(1+z). Hence

    <K>_N=sum_(k=0)^S_N r_(N,-k) J_k.                (2.2)

More generally the output jet of order h needs initial jets only
through S_N+h, and therefore through D+h. All negative coefficients
of r_N V_1 vanish by the equation and regularity of the actual state;
they are compatibility equations, not an excuse to evaluate an
undefined quotient.

This gives at most d(D+1) scalar initial data for the value, independent
of N. When the orbit is regular, S_N=0 and (2.2) is the ordinary initial
value formula. No claim that its higher meridian jets are small is made.

For computation one can avoid multiplying Laurent matrices. Put
C_j=a_d(q_N,M_j(1+z)) B_j and multiply the polynomial matrices C_j,
together with the complete scalar denominator product. If its order
at z=0 is S_N, retain the numerator through order S_N+h and divide
by the denominator's unit part. This computes the same whole germ.
For fixed d,D,h this requires O(N) field operations up to a constant
depending on the fixed truncation and matrix sizes.

## 3. An intrinsic bound on the integral kernel defect

The same statement applies to the actual integral solution lattice,
not just a selected scalar period. Put n=2N, u=M^n,
O=C[u]_(u-1), and represent P on E=C(M) over C(u), as in
[the cofactor construction](root_orbit_pointing.md#4-the-root-period-can-be-read-from-the-quantum-a-operator).
Let

    Lambda=ker_(C(u)) P intersection O^n.

This is a saturated free O-module. Complete and use u=(1+z)^n,
R=C[[z]]. Evaluation at the n root germs M_j(1+z) is an invertible
Vandermonde change of basis over R. It identifies Lambda_R with a
saturated submodule of R^n.

Choose an integral basis, with matrix G(z) of size n by r, and let
A(z) be its first d rows. Generic recurrence propagation shows
r<=d and A has column rank r over C((z)). Its Smith exponents obey

    0<=b_1<=...<=b_r<=D.                             (3.1)

Here is a proof of the bound. Propagation through the whole orbit
uses each point at most once; the total pole budget is still at
most D. Therefore G=L A for a meromorphic n by d matrix L with
z^D L integral. Since G is saturated, it has an integral left
inverse Q. Consequently

    (Q z^D L) A=z^D I_r.

Smith normal form implies every z^b_i divides z^D, proving (3.1).
In particular if two integral solutions have the same initial
meridian jets through D, their difference vanishes on the entire
central fiber. The order-h version follows by the same calculation.

This is the precise bounded extension data in the kernel lattice.
It is a genuine linear solution module. No module structure is being
inferred from a nonlinear condition on proposed scalar sections.

The bound can be sharp: for f=(M+q)^D and
P=f(M)T-f(qM), the solution lattice has rank one, but its first
evaluation has order D. Its first nonzero initial jet is the D-th.
This example has zero reference value; it does not contradict the
earlier rank-one theorem with a nonzero anchor.

## 4. Ordinary initial values can miss a jet

Consider the fixed second-order operator

    P=(M+q)T^2-[(q^2+1)M+q(q+1)]T+q^2(M+1).         (4.1)

It annihilates both 1 and f=(M+q)(M+q^2). At a root of order 2N,
N>=3, all rational solutions are C(u)-linear combinations of these
two functions. Indeed, putting g=sigma(f)-f, its equation is

    g*sigma(Delta h)-sigma(g)*Delta h=0.

Thus Delta h=c(u)Delta f and h=b(u)+c(u)f.

The basis (1,f) is integral and saturated: at the first and third
orbit points its evaluation minor is a unit. At the first two
points the minor has order one, since

    [z] (f(-q^2(1+z))-f(-q(1+z)))=q^2(q^2-1).

The Smith exponents are (0,1). Every h_N=1+c_N f has both ordinary
initial values equal to one, yet

    h_N(1)=1+c_N(1+q_N)(1+q_N^2).

The exact missing datum is

    h_N(1)=1+[(1+q)(1+q^2)/(q^2(q^2-1))]
                 *([z]h_N(-q^2(1+z))-[z]h_N(-q(1+z))). (4.2)

Taking c_N=a^N, a>1, gives logarithmic rate log(a), with the same
fixed operator and the same two ordinary initial values. These
are manufactured states, not knot invariants. The example explains
why an independent bound on meridian jets cannot be silently assumed.
The all-level theorem below uses additional coherence actually
available for the knot state.

## 5. The full ADO normalization keeps its residue and first jet

Keep the exact factor

    N_N=d_N F_N,
    d_N=eta_N*(M-M^-1)*M^N/(M^(2N)-1), eta_N=i^(N+3).

The regular numerator is

    R_N=(u-1)N_N=eta_N*(M-M^-1)*M^N F_N.

Its reference residue and target jet are

    R_N(-q)=eta_N*(-1)^N*(q-q^-1),
    [z]R_N(1+z)=2 eta_N <K>_N.                      (5.1)

These follow by direct substitution; the second retains the zero
of M-M^-1 until differentiation. The factor M^N has shift character
-1, and the exact generic full/reduced gauge is

    d_N(qM)/d_N(M)=-(qM-q^-1 M^-1)/(M-M^-1).

On the initial d colors, N>d, the diagonal multiplication by
eta_N*(M-M^-1)*M^N is a meridian unit. At the target it has one
zero. Thus the full target transfer row acquires a factor z and
the required output first jet compensates for that zero: transport
under this actual gauge needs no additional initial jet beyond
the reduced bound D. Using a general full-state operator directly
also gives the weaker bound D_full+1 by Section 2.

A central unit equal to one at u=1 cannot change (2.2) or (5.1):
the whole output is regular, and its value, or first coefficient
after the target zero, only sees that unit's constant term.
This is distinct from erasing a generic peripheral factor.

## 6. Coverage, checks, and the remaining comparison

Desingularization of q-difference equations and systems is existing
coverage: [Koutschan--Zhang, 1801.04160](https://arxiv.org/abs/1801.04160)
and [Barkatou--Jaroschek, 1802.01150](https://arxiv.org/abs/1802.01150).
Only their stated scope was consulted here. No algorithm or proof
from them is a premise; the degree, propagation, and Smith arguments
above are complete. No novelty claim is made.

The [exact diagnostics](../experiments/audit_bounded_meridian_jets.py)
check 30 second-order examples, including higher contact orders
and the full-state gauge, and 28 examples attaining the first-order
bound. Even and composite levels are included. The
[results](../experiments/bounded_meridian_jets_results.json) are
diagnostics of these uniform proofs, not a knot-class or volume test.

For a specified actual annihilator, the finite-jet bound is now
unconditional in its root-level rank. The subsequent
[finite cut-state proof](finite_sum_annihilator.md) now constructs
a nonzero actual all-level annihilator for every knot in principle.
Its geometric symbol still requires independent identification. The
[next theorem](all_level_a_period.md) removes the unknown meridian
jets from the exact period formula using cross-level polynomial
coherence. It does not establish the geometric regulator norm.
