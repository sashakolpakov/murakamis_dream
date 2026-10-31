# The actual q-Hahn column selects a complex leading action

30 October 2026. The negative-root theorem gives an asymptotic for the
ACTUAL local Fourier sum, including its cancellation. The normalized
logarithm converges on the entire slit plane to the analytic continuation
of its positive real variational action. In the right half-plane this
selects a nondegenerate internal saddle with its original logarithms.

This is a local leading-order theorem at both level parities. It does
not give a complete amplitude expansion, a uniform generic-q normal,
or a noncancellation theorem for the assembled plat source.

## 1. The exact finite polynomial and its logarithm

Use the original coefficients of the
[phase compiler](actual_augmented_plat_phase_compiler.md):

    P_N(w)=sum_a E(t_N,j_N,u_N,a) w^a,
    E(t,j,u,a)=beta(j,a) beta(u,a) beta(t-u,j-a)/beta(t,j),
    a0_N=max(0,u_N-t_N+j_N), a1_N=min(j_N,u_N).

Here 0<=j_N<=t_N<N and 0<=u_N<=t_N. Every beta is the positive
sine binomial at theta=pi/N. No fitted scalar or knot value enters
this definition. The [negative-root theorem](actual_q_hahn_negative_root_source_polynomial.md)
proves the exact factorization

    P_N(w)/P_N(1)=w^a0_N product_(r=1)^(a1_N-a0_N)
                                      (w+rho_(N,r))/(1+rho_(N,r)),
    rho_(N,r)>0.                                         (1)

Consequently on Omega=C minus (-infinity,0] the actual polynomial
has a unique holomorphic logarithm that is real at w=1. Define

    L_N(w)=Log(P_N(w))/N.                                 (2)

This is a specified logarithm, not the principal argument of a possibly
many-times-wound numerical value. Its real part is always
log|P_N(w)|/N, independent of that qualification.

## 2. The real variational problem is strict

Suppose

    (t_N,j_N,u_N)/N -> (tau,xi,upsilon),
    0<xi<tau<1, 0<upsilon<tau.                            (3)

Set a0=max(0,upsilon-tau+xi), a1=min(xi,upsilon), and use

    J(s)=integral_0^s log(2 sin(pi y))dy,
    B(v,a)=J(v)-J(a)-J(v-a),
    Ecal(alpha)=B(xi,alpha)+B(upsilon,alpha)
                 +B(tau-upsilon,xi-alpha)-B(tau,xi).

The interval (a0,a1) is nonempty. For every real w>0 the function
Ecal(alpha)+alpha log w has a unique interior maximum, denoted
alpha(w), and write its value as psi(w). Its derivative is

    Ecal'(alpha)=log[sin^2(pi(xi-alpha)) sin(pi(upsilon-alpha))
                / (sin^2(pi alpha) sin(pi(tau-upsilon-xi+alpha)))].

The derivative tends to +infinity at a0 and -infinity at a1. Its
second derivative is strictly negative:

    Ecal''=-pi{2[cot(pi(xi-alpha))+cot(pi alpha)]
             +cot(pi(upsilon-alpha))
             +cot(pi(tau-upsilon-xi+alpha))}<0.           (4)

For the sign, the first paired arguments sum to pi xi in (0,pi);
the second pair sums to pi(tau-xi) in (0,pi). Apply
cot A+cot B=sin(A+B)/(sin A sin B). All displayed individual
arguments lie in (0,pi) on the support interior.

Uniform sine-factorial estimates give

    log E(t_N,j_N,u_N,a)=N Ecal_N(a/N)+O(log N),

over the ENTIRE finite support; Ecal_N uses the actual scaled
parameters. The support is an interval of the full integer lattice.
An upper bound by its largest term and a lower bound by a nearest
lattice point to the unique maximizer therefore prove

    L_N(w) -> psi(w),           w>0.                      (5)

The argument is uniform when (3) ranges over a compact subset of
its strict domain and w ranges over a compact positive interval.
Factorial endpoints are included in the upper bound; none is silently
removed before taking the maximum.

## 3. Negative roots prove the complex limit

For each compact K in Omega,

    sup_(w in K,rho>=0)
       |Log((w+rho)/(1+rho))| < infinity.                 (6)

Indeed (w+rho)/(1+rho) is on the segment between w and 1. Its
modulus stays bounded above and away from zero uniformly on K,
and its argument stays on the single branch between Arg w and zero.
Equivalently compactify rho by rho/(1+rho) in [0,1]. The same
bound applies to Log w. Since a1_N<N, (1) implies that

    L_N(w)-L_N(1)

is locally uniformly bounded on Omega. Equation (5) bounds L_N(1).
Cauchy estimates and subsequence compactness now give holomorphic
subsequential limits, uniformly on compact subsets. All such limits
agree on the positive real axis by (5); the identity theorem makes
them identical on the connected slit plane. Thus the WHOLE sequence
converges:

    L_N(w) -> psi_hol(w), locally uniformly on Omega.      (7)

All complex derivatives converge locally uniformly as well. This
proves existence and uniqueness of the analytic continuation in (7),
instead of assuming that an arbitrary algebraic saddle has that role.
The same subsequence argument proves uniformity for compact strict
parameter families in (3): any proposed failure has a convergent
parameter subsequence, to which the preceding proof applies.
Continuity of psi_hol in those parameters follows by the same
compactness and positive-axis uniqueness argument.

Only elementary compactness for holomorphic functions is used here:
Cauchy estimates give equicontinuity on a compact exhaustion; successive
subsequences converge there, and the real-axis values determine their
unique holomorphic limit. No contour replacement of the finite source
or unproved saddle coefficient is inserted.

## 4. A positive root measure fixes the branch

Put alpha_hol(w)=w psi_hol'(w). Differentiating (1) yields

    w L_N'(w)=a0_N/N+(1/N)sum_r w/(w+rho_(N,r)).          (8)

The measures (1/N)sum_r delta_rho have total mass tending to
a1-a0. Compactify their domain by adjoining zero and infinity.
Any weak limit mu obeys

    alpha_hol(w)=a0+integral w/(w+rho) dmu(rho).          (9)

For real w, the envelope derivative of the strict maximum gives
alpha_hol(w)=alpha(w). The barrier equation shows alpha(w)->a0
as w decreases to zero and alpha(w)->a1 as w increases to infinity.
Thus mu has no mass at zero or infinity and has total mass a1-a0
on (0,infinity). Formula (9), rather than a chosen ordering of
quadratic roots, specifies the actual selected branch.

For Im w>0 its imaginary part is strictly positive. If additionally
Re w>=0 and w!=0, then

    a0<Re alpha_hol(w)<a1.                               (10)

For (10), each integrand w/(w+rho) has real part strictly between
zero and one. At positive real w, alpha_hol is the original real
interior maximum. Along the physical first-quadrant arc all four
sine arguments in (4) stay nonzero: their imaginary parts are
nonzero away from the positive real axis, and their real-axis
initial values lie in the support interior.
More explicitly, (10) keeps each argument in the vertical strip
0<Re s<1. There Re(sin(pi s))>0, so its logarithm has one analytic
branch agreeing with the positive real logarithm.

The saddle equation therefore continues there without an arbitrary
logarithm reset:

    Ecal'(alpha_hol(w))+Log w=0.                         (11)

It is nondegenerate throughout that quadrant. In fact

    alpha_hol'(w)=integral rho/(w+rho)^2 dmu(rho)

never vanishes there. For 0<=Arg w<pi/2 the integrands lie in an
open angular sector of width less than pi; at Arg w=pi/2 each
has strictly negative imaginary part. Their positive integral is
nonzero. Differentiating (11) gives

    Ecal''(alpha_hol(w))=-1/[w alpha_hol'(w)] !=0.         (12)

Thus on the physical arc psi_hol is exactly the continued critical
value Ecal(alpha_hol)+alpha_hol Log w, with its positive-axis
normalization. This conclusion concerns the leading logarithm. It
does not by itself compute a Gaussian prefactor or an error O(1/N).

## 5. Consequence for every actual complete-circle column

On a complete-circle channel, the exact column is

    f_(u_N)(c_(j_N))=(-1)^u_N q^[-(j_N+1)u_N] P_N(q^delta_N),
    delta_N=t_N+j_N-(N-1).

If (3) holds and xi<=1/2, tau+xi>=1, then

    q^delta_N -> w_star=exp[pi i(tau+xi-1)],
    0<=Arg w_star<=pi/2.

Equation (7) supplies the actual, cancellation-sensitive limit

    lim_N (1/N)log|f_(u_N)(c_(j_N))|
                              =Re psi_hol(w_star).        (13)

Both level parities and all composite levels are included. The
explicit unit prefactor gives the unwrapped leading complex phase
psi_hol(w_star)+pi i(upsilon-xi upsilon) in the compiler's convention.
At the folded endpoint xi=1/2 this selects the actual local branch
of its previously derived quadratic. The high physical degree block
uses its already proved exact index translation, so (13) applies
there in those translated variables too.

For comparison, negative roots give the finite bound

    cos(phi/2)^(a1_N-a0_N) P_N(1)
       <= |P_N(exp(i phi))| <= P_N(1), |phi|<pi.          (14)

The lower factor can be EXPONENTIAL in N. It is not a polynomial
normalization loss. Formula (13) determines that cancellation rate
through the selected analytic action instead of dropping it.

This does not yet control cancellations among different magnetic or
channel states in a whole plat, the mixed-color aliases, the original
generic first normals, or the selected global geometric period.
Those remain necessary for the general long-filling volume equality.

Audit: [actual Fourier columns and selected complex action](../experiments/audit_actual_q_hahn_selected_complex_action.py).
The analytic proof above is uniform; finite numerical checks only
verify the formula conventions and the selected continuation.

The selected-complex-action theorem retains its actual logarithmic sheets and the stated global and amplitude limitations.

The real magnetic-parameter theorem does not imply a complex global-source packet.