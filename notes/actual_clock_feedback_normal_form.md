# Exact underclock feedback and charge elimination in the original source

28 October 2026. This note promotes the independent-parameter bridge
generating function to an exact whole-word identity, retaining the actual
UNDER clock feedback. The additional operation is an explicit diagonal
root-of-unity Gaussian, equivalently a normalized finite Fourier kernel.
The bridge charges can then be eliminated with their fugacities retained.

This does not prove geometric selection or a volume lower bound. In
particular, ordinary evaluation of the independent generating function
before this feedback changes the original scalar. We prove the precise
failure rather than treating its parameters as independently adjustable.

## 1. Original source and the actual feedback matrix

Use the complete original root family

    N>=2, d=N-1, Q=q^2=exp(2*pi*i/N), x=-q^(-1).

The original external dimension/framing factor is chi_N; every crossing
still contains its original kappa factor. For any signed braid word W
on b heads, take the overbridge/closure events and k=B+b anchor segments
of [the whole charged source](actual_global_charged_bridge_flow.md).
The original scalar source is its equation (1), not a newly chosen
functional. Denote the anchor on a segment by X_s.

At crossing j of sign sigma_j, with overclock h_j, the UNDER transport is

    z_out=x^(sigma_j) z_in Q^(-sigma_j h_j).               (1)

For a port v let P_v list earlier UNDER encounters on its segment and
S_v=sum_(ell in P_v) sigma_ell. Then literally

    z_v=x^(S_v) X_(s(v))
                       Q^(-sum_(ell in P_v) sigma_ell h_ell). (2)

Let P_j,S_j denote these data at the UNDER INPUT of crossing j.
The actual conditioned overbridge parameter a_j is alpha_j/u_j,
where u_j is the UNDER OUTPUT and

    alpha_j=Q^(-h_j)/x, sigma_j=+1,
    alpha_j=Qx,         sigma_j=-1.

Substituting (1) and (2) gives the exact formula

    a_j=Q^(delta_j) x^(-S_j) X_(s(j))^(-1)
           Q^[sum_(ell in P_j) sigma_ell h_ell-epsilon_j h_j],
    delta_j=(1+sigma_j)/2, epsilon_j=(1-sigma_j)/2.        (3)

Thus the positive a_j has no self-clock dependence, while the negative
one has the compulsory factor Q^(-h_j). Both signs retain all earlier
UNDER clocks. These facts follow by cancellation of alpha_j with its
own transport; no geometric central relation has been imposed.

Introduce independent primitive Laurent variables R_i consisting of
one A_j for each a_j and one Z_v for every event endpoint port. Equations
(2)-(3) have the uniform form

    R_i(actual)=rho_i X^(v_i) Q^((T h)_i).                (4)

The integer matrix T and the monomials rho_i X^(v_i) are diagram data.
For A_j the row is

    rho_j=Q^(delta_j)x^(-S_j), v_j=-e_(s(j)),
    T_(j,ell)=sigma_ell for ell in P_j,
    T_(j,j)=-epsilon_j, all other entries zero.           (5)

For an endpoint Z_v its row has rho_v=x^(S_v), v_v=e_(s(v)),
and entries -sigma_ell for ell in P_v. No future UNDER crossing enters
(5). Closure ports use their whole actual segment prefix, as in (2).

## 2. Independent event polynomials with charge fugacities

Put F_n=(Q;Q)_n and define the finite formal series

    U_z(v)=sum_(n=0)^d (z;Q)_n v^n/F_n.                  (6)

Take one overbridge e with crossings j_1,...,j_m in its physical
order, signs sigma_r, and independent primitives A_r=A_(j_r),
V=Z_in, W=Z_out. Define w_r=sum_(s<=r) sigma_s and

    t_0=1, t_r=(-1)^r q^(2+w_r)/(V A_r),
    z_0=Q^2x/(A_1 V),
    z_r=x^(-1) A_r/A_(r+1) for 1<=r<m,
    z_m=A_m W.

Let Y_(e,r)=product_(s<=r) Y_(j_s), Y_(e,0)=1. The independent,
event-normalized generating polynomial is

    E_e^0(R,Y)=N kappa^(w_m) [v_e^d]
             product_(r=0)^m U_(z_r)(v_e t_r Y_(e,r)).    (7)

The coefficient of Y^h is N times the entire actual bridge formula
with independent parameters: n_0=d-h_1, n_r=h_r-h_(r+1), n_m=h_m.
Indeed the exponent of Y_(j_s) is sum_(r>=s)n_r=h_s. This is exactly
equation (3) of [the complete bridge-phase proof](actual_bridge_charge_phase.md),
with every scalar, sign, Gaussian phase and endpoint retained.

For a closure event on head i use its original numerator kernel,
including its denominator and pivot but omitting only the explicit 1/N:

    C_i^0=eta_i Z_in^(-d)
                 sum_(a=0)^d Z_in^(d-a)(t_i Z_out)^a,
    (eta_1,t_1)=(1,1),
    (eta_i,t_i)=(x/x^N,Q^(-1)) for i>1.                 (8)

Set F_N^0(R,Y)=product_e E_e^0 product_i C_i^0. Each crossing clock
occurs once and has range 0,...,d. Its coefficient remains a Laurent
polynomial in the independent primitives R. No clock is yet summed
after falsely freezing the actual spectator variables.

## 3. Exact source-preserving feedback theorem

Define on Laurent monomials the linear operator

    G_T(R^nu Y^h)=Q^(nu^T T h) R^nu Y^h.               (9)

For every signed braid word and its original source,

    K_N=chi_N/N * CT_X
           [G_T F_N^0(R,Y)]_(Y=1, R_i=rho_i X^(v_i)).  (10)

In particular the full normalization is fixed by the original period,
not by division by an unknown knot invariant.

Proof. On its Y^h coefficient, (9) is exactly substitution (4) in
every primitive monomial. Equation (7) then gives the actual bridge,
and (8) gives the actual boundary event. There are k events and each
has its original factor 1/N. Every original anchor orbit sum gives N
times its constant term: after clearing the single event-input
denominator, the numerator is nonnegative of total degree kd. If an
orbit kept exponents e_s-d=N l_s, then e_s>=0 gives l_s>=0 and
homogeneity gives sum l_s=0. Thus all aliases vanish, exactly as in
the whole-source theorem. Its N^k cancels the k event factors 1/N.
The remaining 1/N in (10) is the original averaged first-cut source.
This proves (10), for links as well as knots and at arbitrary bridge
number. It does not make sectorwise replacements of the marked row.

The feedback has an exact finite Fourier realization. If m is the
number of crossings, then for any polynomial with these clock ranges

    [G_T F(R,Y)]_(Y=1)
       =N^(-m) sum_(lambda,eta in (Z/N)^m) Q^(-lambda dot eta)
                F(R_i Q^((T eta)_i), Y_j=Q^(lambda_j)). (11)

For a monomial the lambda sum enforces eta=h modulo N. Since h_j is
already in 0,...,d, it gives its actual value, and the remaining phase
is precisely (9). This verifies both the exponent and N^(-m), rather
than N^(-2m). There are no hidden central or peripheral normalizers.

On the coefficient basis G_T is diagonal unitary. That observation
controls its coefficient norm only; the actual charged evaluation
and clock sum can still cancel.

## 4. The bridge charges can be eliminated with feedback retained

Formula (11) does allow the bridge charge sums to be performed exactly,
but it requires ALL the Fourier fugacities. Choose the representatives
0<=lambda_j<N, put Y_j=Q^(lambda_j), and on a bridge write

    Y_r=product_(s<=r)Y_(j_s), Y_0=1,
    T_end=(-1)^m q^(2+w_m) W/V.

Then its v-series in (7) is, modulo v^N, EXACTLY

    product_(r=0)^m U_(z_r)(v t_r Y_r)
       =U_(T_end Y_m)(v)
          product_(r=1)^m
             (v t_r Y_(r-1);Q)_(lambda_(j_r))
             /(v t_r Y_(r-1);Q)_(epsilon_r).           (12)

The denominators in (12) have constant term one and hence a unique
inverse modulo v^N. Equation (12) leaves just one coefficient [v^d]
per bridge, together with the explicit Fourier feedback (11). It is
a uniform charge elimination, not a knot-specific summation identity.

Proof. For the finite Euler series P, U_z(v)=P(zv)/P(v) modulo v^N,
and P(Qv)=P(v)/(1-v). The actual bridge parameters obey

    z_(r-1)t_(r-1)=Q^(epsilon_r)t_r,
    z_m t_m=T_end.

Cancel consecutive P factors while retaining Y_r/Y_(r-1)=Q^lambda.
Their remaining ratio is
P(Q^epsilon w)/P(Q^lambda w)=(w;Q)_lambda/(w;Q)_epsilon,
which proves (12). Lambda=0 recovers the independent-parameter
telescoping, but the full original source requires (11), not that
single Fourier fiber.

## 5. A precise obstruction to pre-feedback telescoping

Evaluation at Y=1 is NOT a quotient respected by G_T. Whenever
T_(ij) is nonzero modulo N,

    [(Y_j-1)R_i]_(Y=1)=0,
    [G_T((Y_j-1)R_i)]_(Y=1)=(Q^(T_(ij))-1)R_i !=0.    (13)

Thus the actual feedback does not descend to the ideal (Y_j-1).
This is a direct obstruction to replacing the independent bridge
generating function by its pre-summed Y=1 value, then attempting
to restore the spectators afterwards. The audit below also checks
that this omission changes full original pivotal scalars, rather
than merely an arbitrary auxiliary observable.

Although the histories in (5) are causal, the operation is not
nilpotent transport: the phases in (9) have order up to N. Causal
ordering therefore does not supply a uniform finite unipotence
argument for the original clock sum.

The exact conjugation laws are

    G_T R_i G_T^(-1)=R_i Q^(sum_j T_(ij) E_(Y_j)),
    G_T Y_j G_T^(-1)=Y_j Q^(sum_i T_(ij) E_(R_i)),        (14)

where E is the integer exponent operator. They make the missing
coupling explicit. In a regular semiclassical chart, write nu/N=v,
h/N=H. Feedback contributes the full phase
exp(2*pi*i*N*v^T T H). Equivalently it shears logarithmic coordinates

    log R -> log R+2*pi*i*T H,
    log Y -> log Y+2*pi*i*T^T v.                       (15)

For example, if F_N^0 has a smooth leading log action S_0 and the
finite Fourier sum admits a critical description, its internal
stationary equations are exactly

    H=partial_(log Y) S_0,
    Lambda=T^T partial_(log R) S_0,
    log Y=2*pi*i*Lambda, log R=log R_base+2*pi*i*T H.   (16)

The charged CT also imposes sum_i (v_i)_a partial_(log R_i)S_0=0
at every anchor. These are the feedback/implicit equations with the
actual source. They contain the terms omitted by varying bridge
charges with independent spectators. Equations (15)-(16) are a
stationary interpretation of the exact (10)-(11), not a proof that
the original contour meets a particular geometric branch.

## 6. What is proved and what remains

The original whole period now has (i) an explicit clock-independent
integer feedback matrix, (ii) a normalized Fourier realization, and
(iii) an exact charge-eliminated bridge formula at every Fourier fiber.
The coupled phase has not been replaced by its absolute value or by
the zero-feedback fiber. No unknown multiplier has been introduced.

This does not fix the selected geometric coefficient. In particular,
the known surviving nonflat anchor cycles in
[the exact fusion note](anchor_phase_cycles_and_exact_fusion.md) prevent
a blanket argument that the remaining phase is a vertex gauge.
Regular critical equations may still be compared with the previously
proved holonomy/calibration equations, but neither (10) nor their
implicit stationary form proves a nonzero original geometric period.
No new knot is claimed to satisfy the volume conjecture here.

Generic q-Weyl/determinant and quantum MacMahon approaches to knot
invariants already occur in the literature; this note makes no
novelty claim for that general architecture. Coverage references are
[Huynh-Le](https://arxiv.org/abs/math/0503296),
[quantum MacMahon](https://arxiv.org/abs/math/0303319), and
[noncommutative Jones](https://arxiv.org/abs/math/0411505).
Their proofs are not premises of the identities above.

## 7. Reproducible checks

[audit_actual_clock_feedback_normal_form.py](../experiments/audit_actual_clock_feedback_normal_form.py)
constructs (3)-(5) without using any clock values, then independently
compares the whole substituted polynomial, every primitive port, and
the charged coefficient with the actual bridge-flow implementation.
It sums all allowed clocks and compares with original signed R
matrices and the original pivotal averaged cut. Five whole sources
are checked at N=2,3. At least one changes if feedback is suppressed.

The same audit checks the normalized finite Fourier delta for N=2,...,9
with positive and negative primitive exponents, and 96 complete
fugacity-preserving telescopes (12), including negative crossings
and the extreme residues lambda=0,N-1. These numerical checks audit
the all-N proofs; they do not replace them.
