# Mixed cusp-color inner packets: exact source and uniform holomorphic WKB

29 October 2026. The low core of the ACTUAL rotated circle of color
j=N-h has a second-order selected recurrence at every integer h.
Near the complete color it admits a source-fixed, nonzero analytic
amplitude on any fixed high-index interval r/N>1/4. A literal zero
in the endpoint recurrence also provides a uniformly holomorphic
ratio interpolant which is EXACT at the physical r-grid. Optimal
analytic Euler--Maclaurin gives an exponentially accurate action
interpolant, with its residual source explicitly retained.

This is a theorem about the low core. The original upper band R P
is the separate, nonzero term in
[the exact two-band theorem](actual_pretzel_cusp_color_two_band_bound.md).
It is not discarded or incorporated into the following amplitude.
No mixed-color period, fixed filling, or knot-volume theorem follows
without the remaining outer-source comparison.

## 1. Literal finite packets and their fixed factorial continuation

Use N>=2, d=N-1, q=exp(pi i/N), Q=q^2, M=floor(d/2),
F_a=(Q;Q)_a, s_a=|F_a|, and the original continuants f_v.
For an INTEGER 0<=h<=M the low core is exactly

    c_(N,h)=kappa^(-1)sum_(v=h)^M a_(h,v)f_v,
    a_(h,v)=N^2 s_(2v)/[s_v^2 s_(v-h)s_(v+h)].

Its marked phase is not optional:

    a_(h,v)x^v=N^2 q^(h^2)
                         F_(2v)/[F_v^2F_(v-h)F_(v+h)].

Interchanging the actual two finite sums therefore gives

    kappa c_(N,h)(z)/N^2
       =q^(h^2)sum_(r=0)^M
         (-1)^r Q^(r(r+1)/2)P_r(z) A_(h,r)/F_r^3,

    A_(h,r)=sum_(v=max(h,r))^M
       Q^(-vr)F_(2v)/[F_vF_(v-h)F_(v+h)F_(v-r)].       (1)

All original normalizations remain. For r>=h define

    D_(h,r)=Q^(-r^2)F_(2r)/[F_rF_(r-h)F_(r+h)],
    U_(h,r)=A_(h,r)/D_(h,r).

On a high interval r/N>=tau_0>1/4 and |chi| small, put
h=N chi/pi. The source's complex continuation means replacing ONLY
F_(v-h),F_(v+h) in (1), with v=r,...,M, by the canonical
Fhat_N(v-h),Fhat_N(v+h) of
[the exact original factorial interpolation](exact_factorial_interpolation_and_complex_contours.md).
All these arguments stay in regular compact factorial substrips.
The same replacement defines D_(h,r). This is holomorphic in complex
chi on a fixed disk and agrees with every physical integer h there.
No assertion about the off-grid continuation of the omitted low
indices r<h is needed for this high-index theorem.

## 2. Exact finite transformation and the all-index Ward equation

For r>=h, n=M-r, the exact normalized finite sum is

    U_(h,r)=sum_(k=0)^n
      (qQ^r;Q)_k(-qQ^r;Q)_k(-Q^(r+1);Q)_k Q^(-rk)
           /[F_k(Q^(r+1-h);Q)_k(Q^(r+1+h);Q)_k].       (2)

It is balanced because the product of its two lower parameters is
independent of h. The OWN finite transformation (3) in
[the coherent inner proof](actual_pretzel_coherent_inner_gauss_elimination.md)
applies exactly, with no absent amplitude. For example at odd N,
choosing its lower parameters in the safe order gives

    U_(h,r)=(qQ^h;Q)_n/(Q^(r+1+h);Q)_n
      *sum_(j=0)^n
       (Q^(2r+1);Q^2)_j(-Q^(-h);Q)_j Q^j
                    /[(Q^(2r+2-2h);Q^2)_jF_j].        (3)

For physical integers r>=h all magnitudes on the second line are
positive after its exact term phase (i q^h)^j is removed. The
monotonicity used at h=0 is NOT asserted when h is macroscopic.

There is a stronger exact source equation. Write H=Q^h and
T_h=H+H^(-1). For EVERY physical 0<=h<=M and 0<=r<=M,

    QY^2(1-Q^2Y)A_(h,r+2)
      +Y(T_h Q^3Y^2+Q+1)A_(h,r+1)
      -Q(QY+1)(QY^2-1)A_(h,r)=0, Y=Q^r,            (4)

    A_(h,M)=D_(h,M), A_(h,M+1)=0.

The equation includes r<h. For its direct proof use the summand in
(1), z=Q^v and the rational certificate

    g_h(z)=(1-z/H)(1-Hz)(1-z/Y)/z^2.

The v-step ratio is
Y^(-1)(1-Qz^2)(1+Qz)/[(1-Qz/H)(1-QHz)(1-Qz/Y)].
Consequently the telescoping difference is

    (1/(YQ^2)-1)z^(-2)
      +(1/(YQ)+H+H^(-1)+1/Y)z^(-1)
                                  -1/(YQ)-1-(H+H^(-1))/Y.

The lower endpoint vanishes at z=H or z=Y, according to whether
the actual sum starts at h or r. Its upper endpoint has F_(2M+2)=0.
The r-step ratio is z^(-1)-Y^(-1), so the first two moments yield
(4). On the high interval r>|Re h| the SAME proof holds for the
specified complex-h factorial completion: the lower endpoint is
z=Y and all shifted-factorial identities are exact. Thus this is
the continuation of the original finite source, not a selected
formal solution of an annihilator.

Normalize (4) by its actual D_(h,r). With

    den_r=(1-QY/H)(1-QYH),

one obtains exactly

    U_r=p_N U_(r+1)+q_N U_(r+2),
    p_N=-Q^(-2)Y^(-1)(T_hQ^3Y^2+Q+1)/den_r,
    q_N=-Q^(-4)Y^(-2)(1-Q^2Y)(1-Q^3Y^2)(1+Q^2Y)
                                             /(den_r den_(r+1)). (5)

Here den_(r+1)=(1-Q^2Y/H)(1-Q^2YH). At r=M-1,
q_N=0 at BOTH parities, independently of H. Thus the selected
source is U_M=1 and U_(M-1)=p_N(M-1); no value of D_(h,M+1)
is divided out.

The recurrence is used where its displayed denominators are nonzero;
this holds uniformly in the small complex cusp corridor below. At
extreme colors outside that corridor one uses the uncanceled exact
equation (4), rather than evaluating a spurious 0/0 at r=M.

## 3. A uniform dominant channel, with its endpoint included

Fix tau_0>1/4, tau_0<1/2. Put epsilon=1/N,
tau=r/N, Y=exp(2pi i tau), H=exp(2i chi), and Q=exp(2pi i epsilon).
Regard the rational coefficients (5) as analytic functions
p(tau,chi,epsilon),q(tau,chi,epsilon). Let p_0,q_0 denote their
values at epsilon=0. Explicitly,

    p_0=-Y^(-1)(2cos(2chi)Y^2+2)
                              /[(1-Y/H)(1-YH)],
    q_0=-Y^(-2)(1-Y^2)^2/[(1-Y/H)^2(1-YH)^2].

The roots of mu^2-p_0 mu-q_0=0 at chi=0 are

    mu_1=-Y^(-1), mu_2=Y^(-1)cot(pi tau)^2.

On every compact real interval I contained in (1/4,3/4), there is
a fixed complex neighborhood and a fixed chi disk on which the
continuation mu=mu_1 is analytic, nonzero, and satisfies

    |mu_2/mu|<=kappa<1, Re mu>=m>0.                   (6)

These hypotheses are CHECKABLE from the displayed rational quadratic:
at chi=0 the ratio is cot(pi tau)^2<1 and Re(-Y^-1)>0;
compactness and sufficiently small complex neighborhoods preserve
both strict inequalities. All coefficient denominators stay nonzero.
No eigenvalue selection from unknown period data occurs.

In particular tau=1/2 is INCLUDED: mu(1/2,chi)=1,
q_0 has a double zero there, and the epsilon derivative q_1 also
vanishes there. The eigenvalue and source frame do not become
singular at the physical terminal point.

## 4. A holomorphic ratio interpolant which matches the source exactly

Choose sigma>0 small enough that
[tau_0-sigma,1-tau_0+4sigma] lies strictly inside (1/4,3/4),
and shrink its complex tube and the chi disk until (6) holds.
Let

    L_N=ceil((1/2-tau_0+2sigma)N),
    F_tau(z)=p(tau,chi,epsilon)+q(tau,chi,epsilon)/z.

For tau in a fixed complex neighborhood of [tau_0,1/2], define

    v_N(tau)=F_tau o F_(tau+epsilon) o ...
             o F_(tau+(L_N-1)epsilon)
                       (mu(tau+L_N epsilon)).          (7)

Every iterate is within C epsilon of its corresponding nonzero mu.
Indeed F_tau(mu(tau+epsilon))-mu(tau)=O(epsilon), while
its z derivative has modulus at most kappa+O(epsilon)<kappa'<1
on those disks. A sufficiently large C gives an invariant disk
at each backwards step. This proves that (7) is uniformly
holomorphic, nonzero and bounded, with a uniform bounded inverse.

At EVERY physical tau=r/N with tau_0N<=r<M, the continued fraction
reaches r=M-1. There q_N=0 EXACTLY, so it forgets its entire
remaining analytic tail and takes the value p_N(M-1). Hence

    v_N(r/N)=U_r/U_(r+1) EXACTLY,                     (8)

and every physical high-index U_r is nonzero. This works also for
complex chi in the fixed disk because the wall zero is independent
of H. There is no assertion that v_N(M/N) equals a nonexistent
physical ratio U_M/U_(M+1); the source product stops at M-1.

Moreover the Riccati defect of (7) is O((kappa')^L_N): adding
one future step changes its terminal value by O(epsilon), which
is contracted by the preceding L_N steps. Thus the chosen terminal
function cannot hide a macroscopic source change.

## 5. The selected action and a nonzero joint amplitude

All derivatives in the following formula are derivatives of the
EXPLICIT rational functions (5). Let

    p_1=partial_epsilon p|_0, q_1=partial_epsilon q|_0,
    nu=[p_1+q_1/mu-q_0(partial_tau mu)/mu^2]
                                             /[1+q_0/mu^2].

The denominator equals 1-mu_2/mu and is bounded away from zero.
The analytic trial ratio mu+epsilon nu has Riccati residual
O(epsilon^2), obtained by Taylor expansion at tau+epsilon.
Applying the same strict contraction as in section4 gives uniformly
on a fixed complex neighborhood

    v_N=mu+epsilon nu+O(epsilon^2).                   (9)

The principal log is well defined by Re v_N>0. Define

    S(tau,chi)=integral_tau^(1/2) Log mu(s,chi) ds,
    C(tau,chi)=sqrt(mu(tau,chi))
                      *exp[integral_tau^(1/2)nu(s,chi)/mu(s,chi)ds]. (10)

The square root is its branch equal to one at tau=1/2. Both are
holomorphic on fixed neighborhoods, and C has a uniform nonzero
lower bound on compact subsets. The physical selected packet is

    U_(h,r)=C(r/N,chi)exp[N S(r/N,chi)](1+O(1/N)),     (11)

uniformly in physical r/N>=tau_0 and complex chi in a fixed small
disk. The proof is to sum Log v_N, use (9) and one-step
Euler--Maclaurin. Since Log mu(1/2,chi)=0, replacing the true
endpoint M/N by 1/2 introduces O(1/N), at BOTH parities. There
is no extra unknown endpoint matching constant. In particular
U_M=1 is its original source normalization, not an imposed WKB scale.

At chi=0, the formulas calibrate against the independent finite
transformation:

    S(tau,0)=i pi(1/2-tau)^2,
    C(tau,0)=sqrt(sin(pi tau))
                              *exp[-3pi i(1/2-tau)/2]. (12)

This calibration also follows directly without that transformation:
substitution in the rational derivatives gives
nu/mu=-(pi/2)cot(pi tau)-(5pi i/2), and Log mu=i pi-2pi i tau.
Integrating these two expressions in (10) proves (12), with its
constant fixed by C(1/2,0)=1.

Thus the joint amplitude is an analytic nonzero deformation of
the already proved complete-color amplitude. This is not a formal
normal-jet assertion: it is uniform for h up to delta N with a
fixed sufficiently small delta, and for the displayed complex
factorial completion.

## 6. Exponentially accurate analytic action, with residual source kept

This strengthening matters before taking an oscillatory outer sum.
An O(1/N) error on individual real-grid terms alone cannot justify
a complex saddle at a fixed nonzero chi.

The functions f_N=Log v_N are uniformly bounded and holomorphic on
a FIXED larger complex neighborhood of [tau_0,1/2]. On an inner
neighborhood there are constants B,a>0, independent of N, such that

    |f_N^(k)|<=B k! a^(-k).

Put b_N=M/N and, for K_N=floor(pi a N/4), define the analytic
Euler--Maclaurin expression

    E_N(tau)=N integral_tau^b_N f_N(s)ds
        +(f_N(tau)-f_N(b_N))/2
        +sum_(k=1)^K_N B_(2k)/(2k)! N^(1-2k)
                  [f_N^(2k-1)(b_N)-f_N^(2k-1)(tau)]. (13)

The Bernoulli polynomial remainder is bounded by
C N (K_N/(pi a N))^(2K_N), after shrinking a if necessary.
This follows from |B_(2k)(x)|<=4(2k)!/(2pi)^(2k) and the
displayed Cauchy derivative bound. Hence, for some c>0,

    U_(h,r)=exp[E_N(r/N)](1+R_(N,r)),
    |R_(N,r)|<=C exp(-cN),                            (14)

uniformly on the physical high grid and the complex chi disk.
There is NO approximation of source values prior to this bound:
the product of the exact grid ratios (8) is precisely U_r.
Its endpoint product is empty and equals one at r=M.

The interpolant E_N is holomorphic in complex tau,chi. Equations
(9) and (13) also give, uniformly on an inner complex neighborhood,

    exp(E_N(tau))=C(tau,chi)exp[N S(tau,chi)](1+O(1/N)). (15)

Indeed the higher Bernoulli terms in (13) sum to O(1/N), and
f_N=Log mu+N^(-1)nu/mu+O(N^-2) there. The grid residual R is
retained explicitly; it is not relabeled a homogeneous solution
or zero current. One may use exp(E_N) in an outer analytic estimate
ONLY after bounding that residual in the whole original sum.

For example on a fixed negative-w neighborhood and |chi| small,
its total high-packet contribution is at most

    poly(N)exp{N[j_0+C|chi|^2-c]},                    (16)

where j_0 is the complete-color real action envelope on that
neighborhood. This follows by the original factorial estimates,
the even analytic perturbation S(tau,chi)-S(tau,0)=O(chi^2),
and (14); no unrestricted exterior operator norm is inserted.
For a fixed small enough chi disk the error barrier survives any
O(|chi|^2) action perturbation, in particular a smaller O(|chi|^4)
loss from a nearby complex index saddle.

This supplies the quantitative source input for a finite-Poisson
or cotangent contour argument in the outer r variable. Its endpoint
currents, the lower r packets, and the R P upper color band still
require their own estimates. No such current is erased by (14).

## 7. A full real-color upper envelope retains the lower indices

For physical integer h define V_(h,r)=q^(h^2)A_(h,r)/D_(0,r).
Its normalized recurrence has EXACTLY the complete-color q_N and
in the shifted variable Z=Q^(r+1) its other coefficient changes by

    p_(h,N)-p_(0,N)=-Z(T_h-2)/(1-Z)^2.               (17)

For 0<=r<=tau_0N, the old full branch envelope
rho=max(1,cot(pi(r+1)/N)^2) gives
|p_h-p_0|/rho<=C|chi|^2, uniformly even at r=0.
The globally conditioned frame of
[the all-index source bound](actual_pretzel_all_index_backward_envelope.md)
therefore changes its one-step bound only by the factor
1+C|chi|^2. The selected high-index anchor (11), together with
s_r^2/(s_(r-h)s_(r+h))<=1 for real physical h<=r<=M,
is at most exp(CN chi^2) times a fixed polynomial. Iteration proves

    |V_(h,r)|<=poly(N)exp{N[E(pi r/N)+C chi^2]},
    E(u)=(2/pi)integral_u^(pi/4)log cot v dv for u<pi/4,
    E(u)=0 for u>=pi/4.                              (18)

The exact mixed Ward (4) proves this also for r<h; its lower
telescoping endpoint is then v=h. Thus no low-index terms have been
omitted. At a fixed complete-color outer radius the strict old
lower-index profile gap persists for sufficiently small |chi|.
This is a controlled continuity estimate, not a claim that the
second recurrence branch disappears.

[Audit](../experiments/audit_actual_pretzel_mixed_inner_source_wkb.py)
checks the original finite mixed coefficients, balanced transform,
all-r Ward and normalized endpoint wall at both parities; verifies
the holomorphic source ratios and the calibrated selected amplitudes.

Fresh replay: PASS 17 complete finite-field families N=2,...,18,
with EVERY admissible integer color and inner index, the original
low-core marked phases and odd mixed finite transformation; four
independent canonical complex-Fhat source cases; and six full selected
analytic-WKB families at N=32,33,64,65,128,129. The last families
include complex chi and compare the literal finite source, its exact
continued-fraction ratios and its normalized nonzero amplitude.
The exponential Euler--Maclaurin barrier is proved analytically above;
finite tests are supplementary, not an inference of that barrier.

## 8. The actual analytic Newton factor has prefactor one

Let w=-exp eta, initially eta>0 real, and set

    alpha_+=(N+1)/2-iN eta/(2pi),
    alpha_-=(N+1)/2+iN eta/(2pi).

Then Q^(alpha_+)=qw and Q^(alpha_-)=q/w EXACTLY, with the
negative-argument logarithmic marks retained. Define

    Bhat_N(r,eta)=q^(-r^2)
       Fhat(alpha_++r-1)Fhat(alpha_-+r-1)
                     /[Fhat(alpha_+-1)Fhat(alpha_--1)]. (19)

At physical integer r it is EXACTLY the original Newton product
product_(a<r)(c_a+2cosh eta). The claim below holds uniformly on
fixed complex neighborhoods with tau=r/N in a compact subinterval
of (0,1/2), eta near a fixed positive real value, and all four
scaled factorial arguments in compact subsets of 0<Re a<1:

    Bhat_N(N tau,eta)
      =exp{N/(2pi) integral_0^(2pi tau)
                              Log(2cosh eta+2cos v)dv}
                                                    *[1+O(1/N)]. (20)

There is no missing periodic multiplier or square-root factor.
Here is the branch calculation. Put a_+=1/2-i eta/(2pi),
a_-=1/2+i eta/(2pi), and
f(a)=[Li2(1)-Li2(exp(2pi i a))]/(2pi i). The canonical
factorial expansion on its marked strip gives

    Fhat_N(Na-1/2)=sqrt(iN) exp[Nf(a)] [1+O(1/N)].

Indeed the displacement contributes -f'(a)/2, where
f'(a)=Log(1-exp(2pi i a)); it cancels the variable part of the
factorial square-root prefactor. The remaining sqrt(iN) has the
same fixed mark exp(i pi/4)sqrt N at all four arguments, so it
cancels between numerator and denominator. In particular one
must NOT reset Log[i(1-X)] to an unrelated principal logarithm.

The exponent of (19) divided by N is

    f(a_++tau)+f(a_-+tau)-f(a_+)-f(a_-)-i pi tau^2.

Its tau derivative is

    Log(1+exp(eta)Y)+Log(1+exp(-eta)Y)-2pi i tau
                               =Log(2cosh eta+2cos(2pi tau)).

At real 0<tau<1/2 the two arguments on the left have positive
imaginary parts, their arguments sum to 2pi tau, and the argument
on the right is positive. Thus the integer logarithmic ambiguity
is ZERO. Holomorphic continuation gives the same identity on the
specified complex neighborhood. Both primitives vanish at tau=0,
which proves (20) with its constant.

This is sufficient for a fixed high-index Poisson window whose
upper cutoff is STRICTLY below 1/2. It is not a uniform bulk
asymptotic through tau=1/2: there an upper scaled factorial reaches
the edge of its strip, and using a reset dilogarithm could lose a
second-shift current. Physical indices beyond such a fixed cutoff
must first be bounded by their strict profile gap, or their upper
continuation treated separately. Formula (20) makes no such
endpoint current vanish.

The updated audit includes four marked Newton-factor cases: exact
integer-r identities at N=8,9 and complex-r,complex-eta bulk
asymptotics at N=12,24, computed independently with the canonical
finite Barnes product. Fresh full replay passes these together with
the finite mixed-source and selected-WKB families listed above.
