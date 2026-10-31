# Spectral control and the tail-free boundary of Racah normal transport

29 October 2026. The new estimate here is a polynomial spectral gap
for the ACTUAL folded root polynomial and bounds for every fixed
SPECTRAL derivative. It also records a general sufficient criterion
for full generic-q partner-normal transport: the actual factorial
range must stop before its [2N] current. A one-edge partner always
has that property, so its normal bound is a corollary of the existing
positive-core theorem, not a bound on a nonzero discarded current.
The first-normal spectral identity below is exact, but the general
nonempty-tail normal problem and a physical confluent-frame norm
bound remain open.

## 1. Exact source convention and the restricted transport theorem

Put D=N-1, M=floor(D/2), q=exp(pi i/N), Q=q^2, and theta=pi/N.
All six spins below are integers. Let a,b,c,d,e,f<=M and assume

    a+b+e,c+d+e,a+d+f,b+c+f >= D.                 (1)

Use the SAME generic seven-factorial sum S(zeta), face factors
Delta_F^2, and normalized squared scalar

    K_e(zeta)=[N]^2 S(zeta)^2 product_F Delta_F^2 (2)

as in [the common-phase/normal theorem](actual_supported_racah_common_phase_and_normal_metric.md).
This is the scalar diagonal gauge of the ACTUAL generic four-port
source proved in [the full source theorem](actual_general_four_port_single_racah_kernel.md),
not a substituted root 6j value. Let e*=D-e and form K_e* by changing
ONLY e in the same generic formula. Both germs are analytic at q.

More generally let B be ANY of the sixty-four partner branches and
let Q_B be its three opposite sums. If

    min Q_B <= 2D,                              (3a)

then, for every fixed r, in t=log(zeta/q),

    |D_t^r K_B(q)| <= C_r N^(c_r) W_N^2.         (3b)

The constants are independent of labels and N. Indeed its actual
z range ends at min Q_B. Every term therefore contains exactly one
[N], and no [2N]. After [N] cancellation, the generic expression
has a positive common-phase root core and only unit denominator
factors. The uniform positive-core germ theorem applies to all its
fixed jets; its normalized root value is W_N^2 by the all-partner
value theorem. This proves (3b) without discarding any term.

For the single partner e*=D-e, the untouched opposite sum
a+b+c+d<=2D automatically proves (3a). In particular there is an
absolute C such that

    K_e(q)=K_e*(q)=W_N^2>0,
    |dot K_e*(q)| <= C N^8 W_N^2.                (3)

The value equality follows from the stronger
[all-sixty-four VALUE reflection theorem](actual_racah_partner_reflection_identity.md).
The proof below only needs its single-internal-edge case.
By tetrahedral relabeling, (3) applies to ANY ONE partner of a folded
sextuple. Its first-normal estimate is rederived in section4 to
identify exactly the spectral term which higher-order transport
would require. A local square root with positive root value also
has polynomial fixed-jet bounds under criterion (3a).

Criterion (3a) can fail already for TWO adjacent partners: N=5,
folded labels (1,1,2,2,2,2), partners (3,3,2,2,2,2), give the true
range z=8,9, so z=9 contains [2N]. Here the exact regularized sum is
C+[2N]T with C(q)=(3+sqrt(5))/2 and T(q)=-1: the current is really
nonzero, not merely allowed by an index bound. The spectral theorem
below does not control it. No assertion for such branches is made.

## 2. The actual root polynomial and its degree recurrence

Set

    p=min(a+d,b+c), s=a+b+c+d, t0=s-2p,
    h=max(|a-b|,|c-d|), rA=a+b-h, rC=c+d-h,
    L=2p-D, n=p-f, t=p+f-D.                     (4)

The supports imply 0<=t<=n, n+t=L, and rA,rC>=L. In particular
L>=0. If t=0 (possibly with L>0) the root polynomial below is 1,
all its positive-order spectral derivatives vanish, and no killed
matrix is needed. Let alpha=q^(2h+1), lambda=z+z^-1. The actual
generic source polynomial is

    G_n(z;zeta)=sum_(k=0)^n
       (Q^-n,P Q^(n-1),alpha z,alpha/z;Q)_k Q^k
                         /(Q,Q^(t0+1),Q^-rA,Q^-rC;Q)_k,
    P=Q^(-2p),                                  (5)

where in the GENERIC formula Q=zeta^2 and alpha=zeta^(2h+1).
The denominators are root units. At the root P=Q^(1-L), the second
upper parameter is Q^-t, and (5) becomes the degree-t polynomial

    R_t(lambda)=sum_(k=0)^t A_k
                    product_(i<k)(c_(h+i)-lambda),
    c_j=2cos((2j+1)theta),
    A_k= [s_n/s_(n-k)] [s_t/s_(t-k)]
          [s_(rA-k)/s_rA] [s_(rC-k)/s_rC]
                         s_t0/(s_k s_(t0+k)) >0. (6)

Here s_j=product_(u=1)^j 2sin(u theta). This is an identity of root
polynomials, not a deletion of the GENERIC k>t terms. The phase in
(6) cancels exactly: the residual exponent is Nk and the remaining
sign is (-1)^k, so (-1)^k q^(Nk)=1. It also follows directly by
converting each finite Pochhammer to sine factors.

For completeness the following recurrence is an OWN finite-product
calculation. For arbitrary generic alpha,beta,gamma,delta, put
P=alpha beta gamma delta, and define R_j by the finite sum (5) with
upper parameters Q^-j,PQ^(j-1) and denominators
Q,alpha beta,alpha gamma,alpha delta. Then

    lambda R_j=A_j R_(j+1)
          +(alpha+alpha^-1-A_j-C_j)R_j+C_j R_(j-1),
    A_j=product_(u=beta,gamma,delta)(1-alpha u Q^j)
          (1-PQ^(j-1))
           /[alpha(1-PQ^(2j-1))(1-PQ^(2j))],
    C_j=alpha(1-Q^j)
          product_(uv=beta gamma,beta delta,gamma delta)(1-uvQ^(j-1))
           /[(1-PQ^(2j-2))(1-PQ^(2j-1))].        (7)

To verify it without invoking a polynomial-family theorem, use
M_k=(alpha z,alpha/z;Q)_k and

    lambda M_k=(alpha Q^k+alpha^-1 Q^-k)M_k
                                      -alpha^-1 Q^-k M_(k+1).

If h_jk is its coefficient in R_j, the three required ratios are

    h_(j+1),k/h_jk=(1-Q^(-j-1))(1-PQ^(j+k-1))
                       /[(1-Q^(k-j-1))(1-PQ^(j-1))],
    h_(j-1),k/h_jk=(1-Q^(k-j))(1-PQ^(j-2))
                       /[(1-Q^-j)(1-PQ^(j+k-2))],
    h_j,k-1/h_jk=(1-Q^k) product_u(1-alpha u Q^(k-1))
                    /[Q(1-Q^(k-j-1))(1-PQ^(j+k-2))].

Substitution proves (7) after one common-denominator multiplication;
the k=0 and terminating endpoints are obtained before division, or
by the same cleared polynomial identity. Thus it remains valid at
our root whenever j<t. Here C_0 is identically zero and is set to
zero BEFORE root specialization; after omitting it, the remaining
recurrence denominators are units.

## 3. A killed birth-death operator with a polynomial spectral gap

At the parameters in (4), A_j=-a_j and C_j=-b_j, where b_0=0 and
for 0<=j<t

    a_j=4 sin((t0+1+j)theta) sin((rA-j)theta)
             sin((rC-j)theta) sin((L-j)theta)
           /[sin((L-2j)theta) sin((L-2j-1)theta)],
    b_j=4 sin(j theta) sin((rA-L+j)theta)
             sin((rC-L+j)theta) sin((s+2-N-j)theta)
           /[sin((L-2j+1)theta) sin((L-2j)theta)]. (8)

Every numerator sine index of a_j is in 1,...,D, and hence

    a_j>=64/N^4,  a_j>=b_j>=0.                   (9)

Here is a proof of the second inequality, which is important for
the uniformity. First t0<=2h and rA,rC>=L follow from the four
choices of the largest difference in h and a,b,c,d<=D/2. For
example, when h=a-b>=|c-d|, p=b+c,
rA-L=D-2c>=0 and rC-L=D-a-b-c+d>=0 because c-d<=a-b.
The other cases follow by exchanging the two pairs and their ends.
For j>=1 put v=L-2j, x=t0+1+j, y=rA-L+j, z=rC-L+j, and

    Delta_v(u)=log sin((u+v)theta)-log sin(u theta).

All indices used are strictly between 0 and N. The function Delta_v
is decreasing, and Delta_v(N-v-u)=-Delta_v(u). Moreover
y+z=t0+D-2h-v<=D-v<N-v, so Delta_v(y)+Delta_v(z)>=0.
Since x>=j+1, (8) gives

    log(a_j/b_j)>=Delta_v(j)-Delta_v(j+1)
                           +log[sin((v+1)theta)/sin((v-1)theta)]>=0.

For the last step clear its positive denominators and use EXACTLY

    sin((v+j)theta)sin((j+1)theta)sin((v+1)theta)
       -sin(j theta)sin((v+j+1)theta)sin((v-1)theta)
      =sin(theta)[cos(theta)-cos(v theta)cos((v+2j+1)theta)]>=0.

The final inequality uses 1<=v<=D. This proves the drift inequality;
at j=0 it is immediate. The lower bound in (9) uses
sin(u theta)>=sin(theta)>=2/N and denominators at most 1.

For t>=1 let B_t be the t by t tridiagonal matrix with diagonal
c_h+a_j+b_j, upper diagonal -a_j and lower diagonal -b_j. Its
characteristic roots are EXACTLY those of R_t, by (7), R_0=1,
and the nonzero leading coefficients. It is diagonally similar to
a real symmetric matrix, since a_j b_(j+1)>0. Put M_t=B_t-c_h I.
The maximum principle with a Dirichlet boundary at t and reflection
at 0 proves M_t^-1 is entrywise nonnegative. To bound its row sums,
solve M_t u=1, u_t=0, and set d_j=u_j-u_(j+1). Then

    a_j d_j-b_j d_(j-1)=1,
    0<d_j<=(j+1)/a_min,
    ||M_t^-1||_infinity=max_j u_j
                       <=t(t+1)/(2a_min)<=N^6/64. (10)

The real eigenvalues of M_t are positive (also by the same maximum
principle), so every zero rho of R_t satisfies

    rho>=c_h+64/N^6.                            (11)

This proof does not need the stronger observed but unproved claim
that all these zeros exceed 2.

Every supported folded e has lambda_e=c_e<=c_h. Factoring R_t
over its real roots and using (11) now proves, for each fixed r,

    |R_t^(r)(lambda_e)|/R_t(lambda_e)
                            <=(N^7/64)^r.        (12)

The same argument bounds fixed derivatives of 1/R_t by a polynomial
times 1/R_t(lambda_e). This is a root SPECTRAL statement, not an
assertion about the coefficients of the disappearing generic tail.

## 4. Convert spectral control to the actual first partner normal

The proved full-source formula is S=S0(E)(V_n/C_n)G_n(E).
The factor V_n/C_n is independent of E and is kept generically.
Write

    K_e=J_e G_n(lambda_e;zeta)^2,
    R_J=J_e*/J_e
       =[product_F D_F(e*)/product_F D_F(e)]
                                      [S0(e*)/S0(e)]^2,             (13)

where D_F=(-1)^(F-D)[N]Delta_F^2 is analytic and nonzero at q.
The total face sign is even. All numerator [N] zeros in (13)
cancel before evaluation; every remaining factor is a root unit.
The exact root value symmetry, or its elementary factorial reflection
s_(D-r)=N/s_r, gives R_J(q)=1. Each fixed logarithmic derivative
of R_J is polynomially bounded uniformly in the labels: it is a
quotient of O(N) unit quantum-integer factors with index O(N).
In particular |dot R_J(q)|<=C N^3.

Set z_e=zeta^(2e+1), z_e*=zeta^(2N)/z_e. Because G_n is symmetric
in its spectral argument, its partner evaluation is EXACTLY
G_n(zeta^(-2N)z_e;zeta). The two spectral coordinates satisfy

    lambda_e*-lambda_e
       =(zeta^(2N)-1)(zeta^(2N)-z_e^2)/(zeta^(2N)z_e),
    |dot lambda_e*-dot lambda_e|<=4N.             (14)

At q they coincide. Differentiating the FULL generic polynomial
only ONCE therefore cancels its common coefficient normal and gives
the exact identity

    (dot K_e*-dot K_e)/W_N^2
      =dot R_J+2(dot lambda_e*-dot lambda_e)
                                      R_t'(lambda_e)/R_t(lambda_e). (15)

Equation (15) differentiates the full source identity (13), rather
than its value alone. In THIS one-edge case its [2N] tail is empty
by (3a); thus (15) must not be presented as a new bound for a
nonzero T. Equation
(12), the root-unit derivative bound in (13), and the uniform
folded-germ bound from the common-phase theorem imply (3).

At SECOND order the common coefficient derivative no longer cancels:
mixed spectral/generic-q derivatives of G_n appear. Its generic
degree is n, whereas its root degree is t, and the vanished k>t
coefficients can contribute to precisely these mixed derivatives.
Consequently (12) ALONE cannot be iterated to higher generic-q jets.
The already proved tail-free criterion still handles every fixed
order in the one-edge case, by its separate positive-core proof.
Neither argument yet bounds a nonempty [2N] tail or the relevant
mixed coefficient/spectral derivatives after external partners.

## 5. An exact central normal check by a finite product derivative

For odd N=2m+1 and a=b=c=d=f=m, R_m is the actual turned Steinberg
projector h_N. Its endpoint c_0 obeys h_N(c_0)=1 and

    h_N'(c_0)=-[2sin(theta)]^-1 sum_(u=1)^m cot(u theta). (16)

This is an exact identity, not a fitted asymptotic. To prove it,
specialize the OWN [balanced Sears identity](finite_balanced_sears_operator_proof.md)
by canceling its parameter c=d. The transformed sum has an upper
parameter 1 and only its k=0 term survives, giving the finite product

    sum_(k=0)^m (Q^-m,Q^-m,A;Q)_k Q^k
                     /(Q,Q,AQ^-2m;Q)_k
        =(Q^(m+1),Q/A;Q)_m/(Q,Q^(m+1)/A;Q)_m.   (17)

At Q^N=1, Q^-2m=Q and (A)_k/(AQ)_k=(1-A)/(1-AQ^k).
Differentiate (17) at A=1. Pairing u with N-u on its right gives

    sum_(k=1)^m (Q^-m;Q)_k^2 Q^k
                          /[F_k^2(1-Q^k)]
                         =-i sum_(u=1)^m cot(u theta).

Differentiating the finite Newton expression (6) at c_0 gives (16),
with its factor -i/[2sin(theta)]. In particular
|h_N'(c_0)|<=C N^2(1+log N), consistent with the general polynomial
bound. This identity tests a genuine normal direction and does not
replace the source germ by its value.

Audit: [degree recurrence, positive drift, spectral derivatives and exact first normals](../experiments/audit_actual_partner_normal_transport.py).
The finite tests supplement the recurrence, drift and generic source
proofs above. They do not certify transport for a nonempty [2N]
tail or an all-partner higher-jet theorem.

The one-flip case has an empty tail. The nonempty-tail boundary remains unestimated.

The theorem is restricted to the tail-free case; it does not extend to the nonempty [2N] current.