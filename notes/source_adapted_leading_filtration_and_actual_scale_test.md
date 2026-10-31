# Which leading filtration preserves the actual selected period?

28 October 2026. There is an exact, globally defined normal-jet
source functor with polynomial norm. It is compatible with the
whole-word Euler/prefix comparison. It retains the source's marked
degree; taking only the lowest state jet does not preserve it.

Two actual-source calculations determine what may be stripped.
First, a single crossing's square-zero completion correction has
an exponential norm in the specified flat Borel metric. Second,
the original figure-eight period loses its entire positive volume
rate if one retains only a sublinear factorial-index window.
These are different filtrations. Neither bounded nilpotent depth
nor small normal order is an exponential-order estimate.

The surviving global quantum period has not been carried to a
proved nonzero marked hyperbolic regulator class. This note does
not assert that remaining step or a new volume conjecture proof.

## 1. An exact source-adapted normal-jet functor

Use the original reduced state and marks of
[the normal-period theorem](peripheral_normal_period.md):

    q_N=exp(pi*i/N), Q_N=q_N^2, Y=M^2,
    F_N(1)=K_N,
    F_N(Q_N^r)=C_r(q_N), 1<=r<N.

On the complete cyclic meridian fiber put

    t=Y^N-1,
    Y_r(t)=Q_N^r(1+t)^(1/N),
    v_N(t)_r=(Y_r(t)-1)F_N(Y_r(t)).                 (1)

This t is the MERIDIAN Frobenius normal, not the separate
quantum normal delta=1-Q^N. They must not be identified.
Write v_N=v_0+t v_1 modulo t^2. Direct differentiation gives

    (v_0)_0=0,
    (v_0)_r=(Q_N^r-1)C_r(q_N), r!=0,
    (v_1)_0=K_N/N.                                 (2)

No rank hypothesis on an annihilator is needed for (1)-(2).
The operator B_0 rank conditions elsewhere concern recovering
this coefficient from a homogeneous kernel, not its identity
with the actual state.

Thus the selected scalar is the explicit normal-period pairing

    lambda_N(v)=N e_0^*[t^1]v,
    K_N=lambda_N(v_N)
       =N Res_(t=0) e_0^*v_N(t) dt/t^2.           (3)

On the flat coefficient norm of (v_0,v_1), ||lambda_N||=N.
Its quotient norm therefore satisfies exactly

    dist(v_N,ker lambda_N)=|K_N|/N.                (4)

This is a global actual source quotient with polynomially
controlled closure. It is not a definition of an unknown
geometric amplitude or a division by K_N. The quotient line
does not acquire a hyperbolic interpretation merely from (4).

The correct graded contraction pairs the degree-one state
coefficient with the source of degree minus one. More generally,
for a marked Laurent co-source and a jet state, the degree-zero
scalar is the sum of ALL terms whose total source/state degree
is zero. It need not be the pairing of their separately lowest
terms. If those terms cancel, a formal nonzero leading state
does not imply a nonzero leading scalar.

This construction commutes with the
[whole prefix Euler transport](prefix_euler_source_jet_torsor.md):
its identity Tr(D^E A^E)=Tr(D A) holds as a meridian family
BEFORE taking the marked residue. It therefore gives the same
closed F_N, v_N and scalar (3). No action of the physical
prefix matrix on the already closed N-vector v_N is asserted.

More generally, on a vector source presentation of matching
dimension, a gauge G(t) transports a derivative source to

    N e_0^*G(t)^-1 dt/t^2.

If G^-1=H_0+tH_1+... and the new vector is w^E=Gw, its
actual contraction is

    lambda_N(w)=N e_0^*(H_0 w_1^E+H_1 w_0^E).     (5)

The analogous matrix formula uses D^E=D G_m^-1 before taking
the residue. The second term in (5) cannot be discarded. This is why
the source, not just the state, must pass to the associated
graded. At fixed normal depth the prefix correction is finite;
the theorem does not bound the size of H_0,H_1 in an arbitrary
changed metric.

## 2. The lowest nonzero state jet can miss all actual volume

The proved ordinary-color bound for any fixed b-strand knot braid is

    |C_r(q_N)|<=sin(pi/N)^(1-b)<= (N/2)^(b-1).

Consequently v_0 in (2) has polynomial norm. It is NONZERO:
the ordinary one-color anchor is C_1(q_N)=1, so its r=1
coordinate is Q_N-1. Its normal valuation is therefore zero.

For the original figure-eight knot, the independently proved
[whole source identity and volume evaluation](figure_eight_whole_source_identity.md)
give

    log|K_N|=N Vol(4_1)/(2pi)+O(log N), Vol(4_1)>0.

Its formally subleading jet (v_1)_0=K_N/N has that positive
exponential rate, whereas the nonzero formally leading state
jet v_0 has rate at most zero. Thus projecting to the lowest
nonzero normal state jet before applying (3) loses ALL the
volume in an actual hyperbolic knot, not just in an unsummed
formal saddle or an arbitrarily chosen zero-source current.

Keeping the marked derivative source in (3) avoids this loss.
It does not, by itself, prove a positive rate for another knot.

There is also a useful global removal of genuinely bounded
parts already available. The actual
[regularized cyclotomic period](regularized_kashaev_period.md)
satisfies

    t_N=(1/N)Tr_(C(Y)/C(Y^N))(Y F_N(Y))|_(Y^N=1),
    K_N=N t_N+O(N^B)                                (6)

for a fixed B depending on the braid. The trace is taken in
its specified regular lattice before the fiber value. Thus
for any V>0 the limits N^-1 log|K_N|->V and
N^-1 log|t_N|->V are equivalent: the polynomial difference
is negligible relative to either positive exponential lower
bound. Equation (6) constructs the same leading class modulo
subexponential scalar sequences, without assuming it is nonzero.
Its exact family identity composes with the prefix comparison.
To retain meridian operators one must keep the whole orbit and
normal extension, not just the single scalar t_N.

## 3. A square-zero ACTUAL prefix correction has exponential norm

Here is a norm test specific to the new crossing completion.
Work at |x|=1 in A_0 with FLAT basis f^a e_k. Put F_a=(Q;Q)_a,
lambda=x^-1 and d_k=(-1)^k x^(-2k)Q^(k(k-1)/2). The actual
positive crossing's right coefficient and its completion are

    a=sum_(a+k<N)lambda^a d_k f^a e_k/F_a,
    a^E=sum_(all a,k)lambda^a d_k f^a e_k/F_a.

Their original common Cartan scalar cancels in the relative
prefix. Since right multiplication reverses composition,

    G=R_(a^E)R_a^-1=R_(a^-1 a^E)=I+R_h.

The coefficient h is supported exactly on wrapped paths a+k>=N,
and it has the explicit formula

    h_(a,k)=x^(a-2N) Q^a F_k
                      /[N(1-Q^a)F_(a+k-N)].        (7)

In particular h^2=0. To derive (7), the actual nonwrapped
inverse is

    [f^a e_k]a^-1=d_(a+k)^-1 (-1)^a
                      Q^(a(a-1)/2)lambda^a/F_a,
    a+k<N.

For a wrapped final path put r=a+k-N. The product a^-1 a^E
then has coefficient

    lambda^a(d_k/d_r)/F_a
        *sum_(l=0)^r (-1)^l Q^(l(l-1)/2){a choose l}_Q.

The partial binomial sum is
(-1)^r Q^(r(r+1)/2){a-1 choose r}_Q. This follows directly
from the Gaussian Pascal identity by telescoping. Reflecting
F_(N-k-1)=N(-1)^kQ^(k(k+1)/2)/F_k gives (7).

Let M_N=max|h_(a,k)|. Every interval 0<=r<k<N occurs in (7),
with a=N-k+r, and its magnitude is

    product_(j=r+1)^k 2sin(pi*j/N)
                    /[2N sin(pi*(k-r)/N)].        (8)

The denominator is bounded between a fixed positive constant
and 2N. Every interval product is bounded by the product of
all factors exceeding one. Taking exactly that interval gives
the matching lower bound up to a polynomial factor. Hence

    log M_N=N integral_(1/6)^(5/6)
                        log(2sin(pi*t))dt+O(log N)
           =N Vol(4_1)/(2pi)+O(log N).            (9)

The final equality uses the already calibrated Lobachevsky value
Vol(4_1)=4 Lambda(pi/6). It is a scale in THIS UNIVERSAL local
correction, not the volume of the knot in whose word it occurs.

Every h coefficient appears as an entry of the right-regular
matrix: apply it to the suitable degree-zero idempotent and
read its f^a e_k row. Therefore

    M_N<=||R_h||<=N^2 M_N.

Both G=I+R_h and G^-1=I-R_h consequently have the positive
exponential rate in (9), despite (G-I)^2=0. This is the actual
one-crossing prefix correction, not an arbitrary unipotent
matrix chosen for a counterexample. The metric is the flat
regular Borel metric; no unestimated transfer to the physical
head metric is made.

The bare original cut annihilates this positive carry exactly.
Thus its algebraic associated-graded quotient is source-faithful
on the restricted uninserted network. It is NOT an exponential
small-error filtration. Norm or source-jet estimates cannot
follow merely from its bounded nilpotent depth.

## 4. The exact original figure-eight source decides the bulk scale

For the actual invariant, not a substitute positive model, the
whole-source identity is

    K_N=sum_(n=0)^(N-1)t_(N,n),
    t_(N,n)=product_(r=1)^n 4sin^2(pi*r/N)>0.

Put Phi(x)=integral_0^x log(4sin^2(pi*t))dt. The direct
endpoint-aware rectangle estimate already proved there gives

    log t_(N,n)=N Phi(n/N)+O(log N)                (10)

uniformly in n. For ANY nonempty retained index set A_N,
positivity and at most N summands imply the exact scale test

    (1/N)log sum_(n in A_N)t_(N,n)
       =max_(n in A_N)Phi(n/N)+O(log N/N).        (11)

Phi has its unique global maximum at x_*=5/6, with value
Vol(4_1)/(2pi). By compactness and strict uniqueness, the
retained source has the FULL volume rate if and only if

    dist(5/6,A_N/N)->0.                            (12)

Thus even a single properly chosen bulk index retains the
exponent; recovering the Gaussian coefficient needs a stronger
window statement. In contrast a retained initial window
n<=d_N=o(N) has rate zero. The elementary upper bound
t_(N,n)<=4^n already proves this, while its n=0 term is one.

More precisely an initial window n<=alpha N has rate

    0,                         0<=alpha<=1/2,
    Phi(alpha),                1/2<alpha<5/6,
    Vol(4_1)/(2pi),             5/6<=alpha<=1.      (13)

The sign changes of log(4sin^2(pi*x)) occur at 1/6 and 5/6;
Phi(0)=Phi(1/2)=Phi(1)=0, giving (13).

This is an original-network obstruction to discarding high
factorial/color degree as if it were a subleading jet. Fixed
normal depth zero still retains the whole sum in (10); it is
not the same truncation as fixing n. The scale n/N is a plausible
bulk coordinate for a whole period. In this positive source,
the exponential associated graded is strict and picks x_*=5/6.
For a general signed braid the source sum need not be positive,
so its maximal action supplies an upper bound but not a proved
nonzero leading scalar. The marked cycle/cancellation question
must still be solved.

## 5. What leading functor is justified now?

The source-adapted normal contraction (3), or the regular-period
class (6), is a genuine GLOBAL quantum leading object. It
commutes with the original scalar closure and with its pointed
Euler/prefix realization. Its original source norm is polynomial.
It is not yet a quotient carrying a proved nonzero geometric
Bloch period. Its nonzero positive exponential class is exactly
the missing lower-bound question for a general knot.

The carry associated graded removes source-invisible completion
artifacts but returns the full original degree-zero word. The
normal associated graded must retain the co-source's degree.
Neither operation strips the macroscopic factorial data in
(10), and neither supplies a norm estimate by nilpotence alone.
An action-normalized leading period functor would additionally
need a whole source-compatible geometric realization and a
nonzero graded contraction there. That is not constructed by
declaring a formal geometric block to be the leading class.

The [audit](../experiments/audit_source_leading_filtration_scale.py)
and [saved output](../experiments/source_leading_filtration_scale_results.json)
check (7) against direct products of the actual crossing's
relative coefficients, test the square-zero correction, and
diagnose the scale tests (9)-(13). Exact matrix tests are finite;
the coefficient, grading, interval-product and positivity
proofs above establish the all-level statements.
