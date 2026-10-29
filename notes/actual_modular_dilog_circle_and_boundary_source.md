# Exact full-dilogarithm circle moments with a controlled original boundary source

28 October 2026. The original finite Euler atoms are exactly moments of
the full rational Faddeev dilogarithm, with a specified radial correction.
At radius one the correction has polynomial operator norm in the actual
unit-shift metric. The function itself is regular across every intervening
cyclotomic root on its selected logarithmic strip. This removes the
norm-one cyclic function's artificial root barriers without discarding
the original coefficient source.

This does **not** identify the original knot period with a bare Faddeev
state integral. The radial corrections remain part of its relative
cycle. Polynomial local operator norms do not imply a smaller exponential
rate after multiplication by the other crossing factors.

## 1. Use the full literature function, including its central period

Put N>=2, epsilon=+1 or -1, Q_epsilon=exp(epsilon*2*pi*i/N), and

    V_epsilon(t)=(1-t^N)^((N-1)/(2N))
                  product_(ell=1)^(N-1)
                    (1-Q_epsilon^ell*t)^(-ell/N).

All these factors are anchored at t=0. On the logarithmic cover write
t=exp(z) and define

    Psi_epsilon(z)=V_epsilon(exp z)
        (1-exp(Nz))^((N+1)/(2N)+epsilon*i*z/(2*pi))
        exp[epsilon*i*Li_2(exp(Nz))/(2*pi*N)].             (1)

For Re z<0 every logarithm and dilogarithm in (1), except the explicitly
displayed z, is its convergent power-series branch. The independently
proved [rational evaluation](rational_quantum_dilogarithm_torsor.md)
identifies Psi_+(z) with

    Phi_(1/sqrt(N))(sqrt(N)*z/(2*pi)-c_(1/sqrt(N))).       (2)

The negative version is its conjugate-reflected function. Thus (1) uses
the literature function with its fixed normalization, not a new invariant
or an arbitrarily chosen periodic multiplier. The underlying rational
evaluation is standard; the proof in the linked note is independent.
For coverage see [Garoufalidis--Kashaev, 1411.6062](https://arxiv.org/abs/1411.6062).
Conversion of Kashaev sums into full-dilogarithm integrals also predates
this note; no novelty is claimed for that general idea.

The first N ordinary coefficients of V_epsilon are

    v_(epsilon,a)=(-1)^a Q_epsilon^(a(a-1)/2)
                    /(Q_epsilon;Q_epsilon)_a, 0<=a<N.

Equation (1) gives the stronger local statement

    Psi_epsilon(z)=sum_(a=0)^(N-1) v_(epsilon,a) exp(az)
                    +O_N((1+|z|)exp(N Re z))             (3)

uniformly on any bounded imaginary interval as Re z tends to -infinity.
The omitted logarithmic terms do not vanish in an ordinary fixed-radius
Cauchy integral. Their exact contribution is the radial correction below.

## 2. The selected full turn is regular, including the unit circle

For Re z<0, (1) immediately gives the marked monodromy

    Psi_epsilon(z+epsilon*2*pi*i)
                  =Psi_epsilon(z)/(1-exp(Nz)).            (4)

The elementary quantum shift, with the logarithmic lift retained, is

    Psi_epsilon(z+epsilon*2*pi*i/N)
                  =Psi_epsilon(z)/(1-exp z).              (5)

These are different statements from norm-one cyclic transport. The full
central factor in (1) is necessary for both.

There are no zeros or poles in the open strip

    0<epsilon*Im z<2*pi.                                 (6)

One can check the apparent cyclotomic singularities directly, without
assuming a cancellation of fractional powers. Differentiating (1) cancels
its two logarithmic terms and gives the meromorphic expression

    d_z log Psi_epsilon
      =sum_(ell=1)^(N-1) (ell/N)
                Q_epsilon^ell exp(z)/(1-Q_epsilon^ell exp(z))
       -N(1+epsilon*i*z/(2*pi)) exp(Nz)/(1-exp(Nz)).       (7)

At z=epsilon*2*pi*i*j/N, 1<=j<N, the two residues are
-(N-j)/N and 1-j/N, so they cancel. The derivative is holomorphic
there and the continued function is nonzero. At z=0 it has residue
one: Psi has a simple zero. At z=epsilon*2*pi*i the residue is zero
and Psi is nonzero. These statements also follow from (2), but (7)
checks the exact norm and the selected strip directly.

Consequently the path z=log R+epsilon*i*theta, 0<=theta<=2*pi,
is a regular lifted circular path for EVERY R>0, including R=1.
When R=1 its initial endpoint is a zero, and its terminal endpoint
is regular. The radial correction has a removable singularity at t=1.

### A uniform geometric phase on the whole selected strip

The full function also has the correct leading phase beyond the unit
disk. For every delta>0 and delta<=epsilon*Im z<=2*pi-delta,
uniformly in ALL Re z, the independently derived defining-integral
estimate in [the literature-state audit](literature_state_volume.md#21-a-uniform-complex-remainder-on-an-entire-horizontal-strip)
gives

    Psi_epsilon(z)=(1-exp z)^(1/2)
       exp[Li_2(exp z)/(epsilon*2*pi*i/N)]
                                  (1+O_delta(1/N)).        (7a)

For epsilon=+1 substitute b=N^(-1/2) and
w=z-i*pi*(1+1/N) into that estimate. Its leading argument is
-exp(w)=exp(z-pi*i/N). Taylor expansion by this exact half-step gives

    Li_2(exp(z-pi*i/N))/(2*pi*i/N)
      =Li_2(exp z)/(2*pi*i/N)+(1/2)Log(1-exp z)+O_delta(1/N).

The second logarithmic derivative of Li_2 is bounded on the smaller
angular strip, for every real part. The original defining-integral
remainder is O_delta(1/N) there as well. This proves (7a), including
its nonzero amplitude. Conjugate reflection proves the negative case.
All branches are those continued through the selected strip. On
smaller strips Cauchy's estimate gives the same remainder control
for every fixed number of logarithmic derivatives.

Thus (7a) applies at any nonreal positive geometric shape, irrespective
of whether its modulus is below, equal to, or above one. This is a
uniform statement about the actual full function in (9), not an
analytic continuation of the norm-one cyclic atom's disk asymptotic.
It still does not assert a uniform estimate on the radial edges at
the strip's boundary; their exact bound is retained separately below.

#### Independent finite-product verification on compact subsets

There is also a direct proof of (7a) on every compact subset of
0<Im z<2*pi, using only (7). Put

    s_*=1+i*z/(2*pi),
    R_z(s)=exp(z+2*pi*i*s)/(1-exp(z+2*pi*i*s)),
    g_z(s)=(s-s_*)R_z(s).

The finite root identity
sum_(ell=0)^(N-1)R_z(ell/N)=N exp(Nz)/(1-exp(Nz))
rewrites the EXACT logarithmic derivative as

    d_z log Psi_+(z)=sum_(ell=0)^(N-1)g_z(ell/N).       (7b)

At s=s_* the apparent pole of g is removable. Its other poles
are s=s_*+k, nonzero integers k. Since 0<Re s_*<1 in this
strip, on any compact z-set the function g is holomorphic and
uniformly bounded on a fixed complex neighborhood of [0,1].
This remains true at Re z=0, including every apparent
cyclotomic root. Equation (7b) extends across those points
by these removable values.

Euler--Maclaurin, with a uniform first remainder, now gives

    sum g_z(ell/N)=N integral_0^1 g_z(s)ds
                          +(g_z(0)-g_z(1))/2+O_K(1/N).

For Re z<0 the convergent Fourier series proves
integral g_z=-Log(1-exp z)/(2*pi*i): the constant Fourier
coefficient of R_z is zero and integral s exp(2*pi*i*m*s)ds
is 1/(2*pi*i*m). Holomorphic continuation proves the same
formula throughout the strip. Also g_z(0)-g_z(1)
=-exp z/(1-exp z). Hence

    d_z log Psi_+(z)=-N Log(1-exp z)/(2*pi*i)
                       -exp z/[2(1-exp z)]+O_K(1/N).   (7c)

Integrate (7c) from a fixed left-half-plane anchor. At that
anchor the convergent small-disk expansion already gives
log Psi_+=Li_2(exp z)/(2*pi*i/N)+(1/2)Log(1-exp z)+O(1/N).
Bounded paths in a compact substrip preserve the O_K(1/N)
error and fix its logarithmic mark, proving (7a) there.
Cauchy's estimate on larger compact sets gives every fixed
derivative version. Conjugate reflection treats epsilon=-1.
This finite-product proof is independent of the stronger
all-real-parts defining-integral estimate above.

## 3. Exact generalized coefficient extraction

For a<N and R>0 define

    B_(epsilon,a)(R)=1/(2*pi) integral_0^(2*pi)
       Psi_epsilon(log R+epsilon*i*theta)
                       (R exp(epsilon*i*theta))^(-a) dtheta,

    E_(epsilon,a)(R)=epsilon/(2*pi*i) integral_0^R
       Psi_epsilon(log t) t^(N-a-1)/(1-t^N) dt.           (8)

The function on the real radial path is its continuation from t<1.
At t=1 the quotient in (8) has its removable value. Then exactly

    v_(epsilon,a)=B_(epsilon,a)(R)-E_(epsilon,a)(R).       (9)

Proof: take the rectangular logarithmic contour between Re z=log r
and Re z=log R, with imaginary endpoints 0 and epsilon*2*pi. Its
vertical sides are the two lifted circles. Pair its horizontal sides
using (4). The resulting radial difference is

    Psi_epsilon(log t)-Psi_epsilon(log t+epsilon*2*pi*i)
           =-t^N Psi_epsilon(log t)/(1-t^N).

Use the orientation factor epsilon/(2*pi*i). By (3), the inner vertical
integral tends to v_(epsilon,a), since its error is
O_N(r^(N-a)(1+|log r|)). The paired radial integral converges at zero
for precisely the required indices a<N. Equation (7) justifies
continuation through R=1 and arbitrary positive R. This proves (9)
with its sign and every scalar fixed.

Thus the coefficient source is a relative cycle consisting of one
lifted circle and one paired radial edge. It is not the circle alone.

## 4. Exact radial modulus and a uniform boundary bound

For 0<t<1, conjugate-pair the finite factors in V_epsilon. This gives

    |V_epsilon(t)|^2=(1-t)(1-t^N)^(-1/N).

The remaining modulus in (1) is (1-t^N)^((N+1)/N); the explicitly
imaginary logarithmic and dilogarithmic terms have modulus one. Hence

    |Psi_epsilon(log t)|^2=(1-t)(1-t^N).                 (10)

In fact (10) holds for all t>0. For t>1 its two factors are both
negative. To check this extension without choosing fractional powers
across the zero, take the real part of (7). On the real radial line,
the paired finite terms give

    d_(log t) log|Psi_epsilon|
        =-t/[2(1-t)]-N t^N/[2(1-t^N)].

This is the logarithmic derivative of the positive square root of
|(1-t)(1-t^N)|. The simple zero at t=1 fixes the same multiplicative
constant on both sides by continuity of its nonzero first derivative.

For 0<R<=1, (10) gives the UNIFORM estimate

    |E_(epsilon,a)(R)|
       <=1/(2*pi) integral_0^R t^(N-a-1)
                                  sqrt((1-t)/(1-t^N)) dt
       <=R^(N-a)/[2*pi*(N-a)].                         (11)

This includes a=N-1 and R=1; no fixed-distance-from-the-endpoint
condition is needed. For R>1 the same calculation yields the explicit
bound

    |E_(epsilon,a)(R)| <=1/[2*pi*(N-a)]
          +1/(2*pi) integral_1^R t^((N-1)/2-a) dt.      (12)

Here t^N-1 >= t^(N-1)(t-1). In particular an exterior-radius radial
term need not have polynomial size. Its possible exponential rate is
retained in (12), rather than discarded in a geometric deformation.

If T^N=0 and ||T||<=1, define B_epsilon(T) and E_epsilon(T) using
the finite resolvent (tI-T)^(-1). Equivalently sum (8) times T^a.
Then (9) and (11), at R=1, give

    v_(epsilon,N)(T)=B_epsilon(T)-E_epsilon(T),
    ||E_epsilon(T)|| <= H_N/(2*pi),
    H_N=sum_(j=1)^N 1/j.                               (13)

This bound is on the FULL source correction, not on its logarithm.
The nilpotent resolvent retains the finite original head and introduces
no unknown scalar normalization.

### 4a. The shifted full turn and its exact negative-ray source

There is a second useful coefficient cycle for the SAME full function.
Write Psi=Psi_+ and v_a=v_(+,a). For every R>0 and 0<=a<N put

    C_a(R)=1/(2*pi) integral_(-pi)^pi
       Psi(log R+i theta)(R exp(i theta))^(-a) dtheta,

    J_a(R)=(-1)^(N-a)/(2*pi*i) integral_0^R
       Psi(log t+i*pi) t^(N-a-1) dt.

Then, with the indicated logarithmic marks, exactly

    v_a=C_a(R)-J_a(R).                               (13a)

The shifted rectangle is holomorphic even though it contains zeros:
in the lower half-strip, a cyclotomic point z=-2*pi*i*j/N has
residues -j/N and 1+j/N in (7), hence a simple zero of Psi,
not a pole. The upper half-strip has the cancellations already
proved. Thus the rectangle with imaginary endpoints -pi and pi
requires no additional pole residues. Its paired rays satisfy

    Psi(log t-i*pi)=(1-(-t)^N)Psi(log t+i*pi).

Substituting this into the same rectangular argument as Section 3
cancels the central denominator in its radial difference. The phase
of (t exp(-i*pi))^(N-a) is exactly (-1)^(N-a), giving (13a).
The inner circle tends to v_a for the same reason as before.

The selected upper negative ray has the particularly simple EXACT
modulus, for ALL t>0,

    |Psi(log t+i*pi)|^2=1+t.                         (13b)

Indeed in (7) put exp z=-t. Pairing the finite terms gives real part

    (1/2)[N(-t)^N/(1-(-t)^N)+t/(1+t)].

The second term of (7) cancels its first summand because
Re(1+i(log t+i*pi)/(2*pi))=1/2. The remaining logarithmic
derivative is t/[2(1+t)]. The anchor Psi->1 at t->0 fixes
the constant. When N is even and t=1, the apparent terms cancel
at a regular interior-strip point, so the same identity extends
through it. Consequently

    |J_a(R)| <= (1/(2*pi)) integral_0^R
                       sqrt(1+t)t^(N-a-1) dt
             <=sqrt(1+R) R^(N-a)/[2*pi(N-a)].        (13c)

At R=1 this again gives a polynomial original-head bound: the
nilpotent unit-shift correction has norm at most
sqrt(2)H_N/(2*pi). For R>1 the factor R^(N-a) is retained;
no exterior polynomial bound is asserted. The epsilon=-1
identity is the conjugate-reflection of (13a)-(13c).

Thus BOTH full angular choices [0,2*pi] and [-pi,pi] have exact
original coefficient cycles. In particular the cut prescribed by
[the all-radius angular maximum theorem](all_radius_angular_geometric_cycle_and_polarization.md)
need not be imposed as a new source choice: its matching ray is
specified by (9) or (13a). This fixes the local coefficient cycle,
not its whole-word geometric dominance. Carrying those ray terms
through the actual positive chart, and proving their total
contribution cannot cancel the geometric term, remains necessary.

## 5. Application to every original crossing and its boundary factors

At the complete unit meridian the actual transfer shifts have norm
at most one in the standard balanced head metric. Their scalar color
factors have modulus one. For the actual Q=e^(2*pi*i/N), exactly

    u_(Q,N)(T)=v_(-,N)(Q^(-1)T).                       (14)

This is the finite factorial reflection, not an asymptotic equality.
Equations (9), (13), and (14) therefore treat both types of actual
transfer with the literature full function and their retained radial
sources. In particular no reciprocal full function with a divergent
radial endpoint is needed to represent u.

All original factorial diagonals have the same coefficient realization:

    1/F_a=Q^(-a) v_(-,a),
    F_a=N Q^(N-1-a) v_(+,N-1-a), 0<=a<N.              (15)

At R=1 the radial-error operator norms for these DIAGONAL kernels are,
respectively, at most 1/(2*pi) and N/(2*pi). These are maxima of the
coefficient bounds, not sums. The positive factorial's original factor
N and phase are retained exactly.

Insert (9) and (14)-(15) in the strict original signed crossing word.
Keep its Gaussian, Cartan, framing, peripheral and original input/output
functionals. Expanding the finite product gives an EXACT finite sum
over choices of circle or radial source at each atom. The number of
choices is fixed by the word, independently of N. Each term is an
ordinary full-dilogarithm relative period with the original finite
rational kernel/source. Absolute convergence at each fixed N follows
coefficientwise from the finite nilpotent resolvents and (8)-(10).

This applies to the full original knot scalar, not just an unpointed
operator. It does not require a nonzero knot value or division by one.
The previous ordinary-Gaussian replacement can also be retained: its
diagonal acts on the same finite degrees and the initial domination
argument is unchanged.

This construction is distinct from the [Hardy forest reduction](actual_hardy_forest_residue_reduction.md).
It supplies full-function relative moments on the original finite heads;
one must not replace every scalar atom in the unwrapped Laurent graph
by (1) and assume that its nonanalytic logarithmic tails are source-null.
The radial terms in (9) are exactly what such a substitution would miss.

## 6. What this changes on the path to the geometric period

The cyclic atom's accumulating root divisors are not intrinsic barriers
to the selected full-function transport. Equations (1), (7), and (9)
give the full dilogarithm and its exact coefficient cycle, with an
explicit locally polynomial correction at radius one. The independently
proved Fourier and pentagon identities for that full function can now
be tested against this specified source, rather than against an unspecified
state integral or an assumed equivalence of formal jets.

Two conclusions do NOT follow. First, a positive geometric change of
coordinates must carry the radial edges and finite resolvents as well
as the circle integrand. Second, a polynomial norm bound for one radial
factor does not make its whole-word contraction exponentially small:
the remaining factors and their source can still carry the volume rate.
The nonzero geometric image and the global comparison with the marked
Rivin period remain unproved. Those, rather than a further choice of
local quantum-dilogarithm normalization, are the next required steps.

## 7. Reproducible checks

[The main audit](../experiments/audit_actual_modular_dilog_circle.py)
checks 30 exact shift/monodromy/modulus instances, 16 entire
circle-plus-radial moments, 14 original diagonal/reflection families,
and 12 full-strip phase instances at interior, unit, and exterior
radii. The moments use the full function, not its truncated polynomial;
the bare circle is explicitly checked to give the wrong coefficient.
[Results](../experiments/actual_modular_dilog_circle_results.json).

[The shifted-circle audit](../experiments/audit_actual_modular_shifted_circle.py)
separately checks the negative-ray formula and its exact modulus.
These checks supplement the all-level proofs above. Neither audit
computes a geometric cycle coefficient or verifies a volume limit.
