# The actual joint magnetic and pair-degree amplitude

30 October 2026. This note continues the ORIGINAL terminating q-Hahn
kernel jointly in the pair degree t and the magnetic coordinate u.
The channel j remains an integer. The exact accretive determinant,
the canonical center phase and two original finite-shift equations
give an actual nonzero amplitude, not only a formal stationary ansatz.

The domain is a central complex wedge. It is independent of N on
compact subsets and includes the folded limit j/N=1/2. This is not
yet a contributing-cycle or whole-source theorem for an arbitrary plat.

## 1. The source and the domain

Put h=1/N, d=N-1, q=exp(pi i/N), Q=q^2, and x=q^d=-q^(-1).
Let 1<=j<=floor(d/2), xi=j/N. The literal terminating sine-product
continuation is the function fhat_j(u,v) in section 6 of
[the magnetic corridor](actual_q_hahn_magnetic_complex_corridor.md).
Its Gaussian-binomial coefficients, denominator and exponential
prefactor are unchanged. Set

    t=N tau, u=N nu, v=t-u,
    U=exp(2pi i nu), T=exp(2pi i tau),
    z=exp[pi i(tau-2nu)], c_h=-cos[pi(tau+h)].           (1)

Use the convex, simply connected tube

    D={ (tau,nu) in C^2 :
          1/2<Re tau<1, |2Re nu-Re tau|<1/2 }.          (2)

It lies inside 0<Re nu<Re tau. On each compact subset of D, for
all sufficiently large N, Re c_h>0 and Re z>0. All factors
T-Q^r, 0<=r<j, are nonzero there. The channel ratio xi lies in
a fixed compact subinterval of (0,1/2], with its actual value j/N
used in every coefficient function below.

The [exact determinant theorem](actual_q_hahn_joint_accretive_determinant.md)
supplies the monic polynomial

    R_j(z;c_h)=det(z I+c_h D_j+K_j),
    D_j real symmetric positive definite, K_j real skew-symmetric.   (3)

The letter D_j in (3) denotes the matrix, not the product denominator
in the rational H_j formula. In this note write that product as
Delta_j(T)=product_(r=0)^(j-1)(T-Q^r).

The exact scalar normalization is

    fhat_j(u,t-u)
       =x^u q^(jt) [2j choose j]_Q R_j(z;c_h)/Delta_j(T).            (4)

It follows by taking the U^0 coefficient of
U^j H_j(U,T/U): the finite Gaussian Vandermonde identity gives
T^j[2j choose j]_Q. This identity follows by taking the middle
coefficient in the product of two finite Gaussian binomial products;
it has no division by [N]. Here 2j<N, so its scalar is nonzero.

## 2. A canonical joint logarithm, including its finite phase

Let beta(2j,j) be the positive sine binomial. Factoring each sine
in Delta_j makes (4) equivalent to

    fhat_j(Nnu,N(tau-nu))
      =beta(2j,j) exp{pi i[d nu+(j^2-dj)/(2N)]}
          R_j(z;c_h)/product_(r=0)^(j-1) 2sin[pi(tau-r/N)].          (5)

Every sine has positive real part on D. The matrix in (3) has
positive Hermitian part when Re z,Re c_h>0, so its principal matrix
logarithm exists. Define Log R_j by the trace of that matrix logarithm.
This is holomorphic on the product of the two right half-planes and
is real on z,c_h>0. With the positive real logarithm of beta(2j,j),
equation (5) therefore specifies a holomorphic Log fhat on each fixed
compact portion of D for all large N. These specifications agree on
overlaps; no interpolation or sampling character is introduced.

For REAL tau with 1/2<tau<1, at the noninteger center u=t/2, R_j(1;c_h)
and all the sine factors are positive. The prescribed phase is exactly

    Im Log fhat_j(t/2,t/2)
       =pi[d(t-j)+j^2]/(2N).                          (6)

In particular (6) holds between adjacent integer degrees. It fixes
the possible pair-degree sampling alias as well as the magnetic one.

For A=zI+cD_j+K_j, accretivity gives

    |partial_z Log det A|<=j/Re z,
    |partial_c Log det A|<=j/Re c.                    (7)

For the second estimate conjugate by D_j^(-1/2): the resulting
matrix has Hermitian part at least (Re c)I, and its c derivative
is I. No lower bound for the smallest eigenvalue of D_j is needed.
Consequently the estimates remain uniform at the folded limit.

The explicit prefactors in (5) and (7) give locally uniform bounds
for all first derivatives of

    G_N(tau,nu)=N^(-1)Log fhat_j(Nnu,N(tau-nu)).         (8)

A real complete-chamber lattice anchor bounds G_N itself. Cauchy
estimates then bound every fixed holomorphic derivative on smaller
compact subsets.

## 3. The actual selected joint leading action

For real tau,nu with tau+xi>=1 and 0<nu<tau, the preceding real
amplitude theorem has the phase

    Phi_xi(tau,nu)=psi_(tau,xi,nu)(w_*)+pi i nu(1-xi),
    w_*=exp[pi i(tau+xi-1)].                           (9)

Its magnetic continuation is already proved at integer t. The
canonical logarithm there agrees with (5): at nu=tau/2 their
prescribed phases are (6), and continuation in nu fixes the rest.

The bounds in section 2 give a normal family jointly in tau and nu.
For any real complete-chamber tau, choose nearby actual integer
degrees t_N with |t_N/N-tau|<=1/N. The derivative bound changes
G_N by O(1/N) between those degrees. On each such slice the existing
magnetic theorem identifies the limit (9), with the canonical
logarithm just checked. Thus every subsequential joint limit agrees
with (9) on a real open set, and hence throughout the connected tube
D by the holomorphic identity theorem. This proves for the WHOLE
sequence, locally uniformly with all fixed derivatives,

    G_N(tau,nu)-Phi_(xi_N)(tau,nu) ->0, xi_N=j/N.        (10)

Here Phi is the resulting holomorphic continuation on D. The same
subsequence argument gives uniformity for compact real channel-ratio
families, including xi=1/2. The elementary characteristic equations
below also make its local analytic dependence on xi explicit. There
is no finite continuation of the discrete index j in this assertion.

## 4. Two source-exact finite shifts

The determinant note proves the entire Casimir identity for complex
T by polynomial degree: its cleared residual has T-degree at most
j+1, vanishes on the j+1 complete physical slices and also at T=0.
Thus the fixed-t Casimir equation is valid for the ACTUAL joint kernel.
With f=fhat_j(Nnu,N(tau-nu)), it is

    A_+ f(tau,nu+h)+A_- f(tau,nu-h)+(D_h-C_h)f=0,       (11)
    A_+=(U-T)(1-QU)/T,
    A_-=(U-QT)(1-U)/(QT),
    D_h=(U/T)[2(q^(-1)+qT)-(q+q^(-1))U],
    C_h=q J+q^(-1)J^(-1), J=exp(2pi i xi).

The original normalized coproduct gives a SECOND exact identity:

    (1-QT)f(tau+h,nu)
       =x(1-U)f(tau,nu-h)+(U-QT)f(tau,nu).             (12)

One direct finite proof of (12) uses the Newton summands of H_j.
Each summand separately satisfies

    (1-Q^(-j)UV)H(U,V)
       =(1-U)H(U/Q,V)+U(1-V)H(U,V/Q).

Replace V by QV and use
Delta_j(QT)/Delta_j(T)=(1-QT)/(1-Q^(1-j)T), together
with the exact x^u factor. This proves (12) for the original sum.
The Newton identity alone does not determine the Gaussian-squared
coefficients; it is used together with (11), not as a characterization.

Put a=Phi_nu, b=Phi_tau, and

    A=(U-T)(1-U)/T, D=2U(1+T-U)/T,
    H(tau,nu,a)=A(e^a+e^(-a))+D-(J+J^(-1)).            (13)

Passing to the limit in the ACTUAL shifted ratios gives

    H(tau,nu,a)=0,
    (1-T)e^b=(U-1)e^(-a)+U-T.                         (14)

The first equation is simple throughout D. Indeed its discriminant,
apart from nonzero factors, vanishes only if

    cos^2(pi xi) z^2+2c_0 z+1=0,
    c_0=-cos(pi tau).

For Re z>0 this would require
c_0=-(cos^2(pi xi)z+1/z)/2, whose real part is negative,
contrary to Re c_0>0. The same argument includes xi=1/2.
Also A!=0 and J!=1 on the stated domain. Hence H_a!=0.
The second equation is simple in b, since (1-T)e^b!=0.

The prescribed real-chamber values and these simple equations also
give local analytic dependence on xi, including through xi=1/2.
This concerns the coefficient functions of the asymptotic, not an
interpolation of the finite discrete channel.

## 5. Two actual derivative bootstraps and a closed amplitude form

Let a_N=partial_nu G_N and b_N=partial_tau G_N. The joint Cauchy
bounds and exact finite shifts imply

    f(tau,nu+/-h)/f=exp(+/-a_N)[1+(h/2)partial_nu a_N+O(h^2)],
    f(tau+h,nu)/f=exp(b_N)[1+(h/2)partial_tau b_N+O(h^2)].          (15)

All errors here and below are uniform on compact subsets, with
actual xi_N used. Define

    A_1^+=-2pi i U(U-T)/T,
    A_1^-=-2pi i U(1-U)/T,
    D_1=2pi i U(T-1)/T,
    C_1=pi i(J-J^(-1)),
    H_1=A_1^+e^a+A_1^-e^(-a)+D_1-C_1.

Equation (11), simplicity and (10) first imply a_N-a=O(h).
Cauchy's estimate gives the same derivative bound. Substitution
a second time then proves

    a_N=a+h r+O(h^2),
    r=-[H_1+(Phi_(nu,nu)/2)H_(a,a)]/H_a.              (16)

Use this in (12). Its simplicity and the already bounded derivatives
first give b_N-b=O(h), and the second substitution gives

    b_N=b+h s+O(h^2),                                 (17)
    s={ (1-U)e^(-a)[pi i+r-Phi_(nu,nu)/2]
          +2pi i T(e^b-1)
          -(1-T)e^b Phi_(tau,tau)/2 }/[(1-T)e^b].

No logarithmic alias is introduced when solving these equations:
a_N and b_N already converge to the prescribed derivatives in (10).

The holomorphic one-form

    omega=s d tau+r d nu                               (18)

is closed. To see this directly, use the equality of the mixed
derivatives of the ACTUAL G_N in (16)--(17), and Cauchy bounds for
the O(h^2) remainders. It gives partial_tau r-partial_nu s=O(h).
Take sequences of admissible xi_N tending to any fixed xi; the
coefficient functions are continuous, so that difference is exactly
zero. This proves closedness without assuming a formal transport
solution equals the finite source.

On the simply connected tube D there is therefore a nonzero
holomorphic B_xi with d Log B_xi=omega. Fix its constant by the
known real physical amplitude at a strict real complete-chamber
point, for example tau=1-xi/2, nu=tau/2. Nearby actual lattice
samples supply the same normalization to relative error O(h).

Integrate (16)--(17) from such a sample along compact paths in D.
The gradient of Log f-N Phi+(1/2)log N-Log B is O(h), and its
initial value is O(h), choosing the logarithm of its near-one ratio
at that sample. Thus the ACTUAL original kernel satisfies

    fhat_j(Nnu,N(tau-nu))
      =N^(-1/2) B_(xi_N)(tau,nu)
            exp[N Phi_(xi_N)(tau,nu)](1+O(N^(-1))).     (19)

The relative error has the same bound under each fixed derivative
on smaller compact subsets. This proves the joint complex amplitude,
including arbitrary O(1/N) noninteger shifts of t, fixed complex
scaled displacements, both level parities and composite levels.

Near the original physical real chamber, comparison with the prior
amplitude theorem identifies the coefficient with

    B_xi(tau,nu)=Acal_(tau,xi,nu)(w_*)
                       exp[pi i(alpha_(tau,xi,nu)(w_*)-nu)].        (20)

Both integer offsets are retained. Formula (18) continues (20)
wherever a particular internal-saddle coordinate ceases to be a
convenient chart. It does not redefine the finite kernel.

## 6. What this removes from the general problem

Pair degree and magnetic coordinate may now vary together in a
uniform complex central domain. A finite product of these ordinary
column factors, composed with the actual affine wire maps of a
fixed plat, has the corresponding joint estimate on any compact
common preimage of D. The number of factors is fixed with the
diagram, so the relative errors still multiply to 1+O(1/N).

This statement does not itself place the geometric critical point
in that domain, match its sheet to the selected one, choose a
contributing physical cycle, or estimate a coherent sum over wires
and channels. It also does not continue the discrete channel j or
bound new generic-q normal currents. Those remain explicit tasks
in the general original-source volume conjecture.

## 7. An explicit algebraic test for the selected local sheet

The preceding continuation has a useful exact branch description. Put

    s=sin(pi xi), C=cos(pi xi), c_0=-cos(pi tau),
    W=1+2c_0 z+C^2 z^2, V=1+2c_0 z+z^2.              (21)

Both W/z and V/z have positive real part when Re c_0,Re z>0.
Their arguments and the argument of z lie in (-pi/2,pi/2), so W
and V avoid the nonpositive real axis. In particular the PRINCIPAL
square root sqrt(W) is holomorphic and has positive real part.

The actual selected magnetic multiplier is

    Y=exp(Phi_nu)=(s z+i sqrt(W))^2/V.                 (22)

To prove this, substitute U=exp(pi i tau)/z into (13). It gives

    Y+Y^(-1)=2-4W/V.

The two solutions are (s z+/-i sqrt(W))^2/V. Their numerators
are nonzero, since a zero would force V=0; the two solutions are
distinct. At a real center c_0>0,z=1, the actual canonical derivative
has imaginary part strictly between 0 and pi, fixing the plus sign.
Holomorphic continuation on D then proves (22) everywhere. This
also includes the folded endpoint C=0.

Suppose a candidate marked geometric multiplier Y_geo satisfies
the same characteristic equation at a point of D. Then

    r_geo=[V Y_geo-s^2 z^2+W]/(2i s z),
    r_geo^2=W.                                        (23)

Consequently it belongs to the source-selected local sheet if and
only if Re r_geo>0. This is a strict algebraic inequality after the
already selected peripheral square roots in z,c_0 are retained.
It is a checkable additional condition on a geometric candidate,
not a proof that every coupon of a general plat satisfies it in
one common frame. The contributing-cycle problem remains separate.

Audit: [the original joint source, both shifts and amplitudes](../experiments/audit_actual_q_hahn_joint_complex_amplitude.py).
The primary reader's fresh run and an independent fresh replay passed.
The finite comparisons test the normalization and correction formulas;
sections 2--5 supply the uniform analytical proof.

Independent source-transport review: full analytical read PASS. The
reviewer checked the exact scalar and principal matrix-logarithm
normalization, noninteger center phase, joint normal-family selection,
both original finite shifts, discriminant exclusion throughout the
central wedge, both subleading gradient corrections, closed amplitude
form, and the normalized lattice anchor including +(1/2)log N.
The review retains the integer-channel hypothesis and does not infer
a contributing global cycle or a bound on an assembled coherent sum.
Fresh independent 160-digit audit replay also PASS: 476 exact
off-lattice coproduct identities, 32 independent terminating-source/
determinant comparisons, 32 joint amplitude calibrations and eight
actual folded-channel gradient corrections. The maximum scaled
relative error was 0.476 and the maximum N-squared gradient remainder
was 0.407; these finite checks confirm the conventions, while the
written argument supplies the uniform theorem.

Independent analytical review: a second reader checked the exact
source-to-sine normalization and canonical matrix logarithm, joint
normal-family selection using nearby physical degrees and the marked
center phase, simplicity on the full central tube including xi=1/2,
and both source-exact finite shifts. The two subprincipal corrections
were independently expanded with their signs and integer offsets.
The review also checked Cauchy control of their remainders, closedness
from the actual mixed derivatives, and normalization at moving lattice
samples before integration. The proof passed. This review does not
supply a common physical frame, selected whole-source cycle, or
continuation of the discrete channel.

The explicit selected-sheet formula in section 7 received a separate
independent analytical review. Its characteristic equation and recovered
square root were checked by two formal polynomial identities, and four
complex saddle comparisons distinguished the selected and opposite signs.
Those additional focused checks passed; no global sheet or cycle assertion
was added.
