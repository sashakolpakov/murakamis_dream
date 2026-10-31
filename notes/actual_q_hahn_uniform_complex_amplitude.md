# A uniform nonzero complex amplitude for the actual q-Hahn column

Subsequent extension: [joint pair-degree and magnetic amplitudes](actual_q_hahn_joint_complex_amplitude.md)
are now proved on a central complex domain, using the original finite
kernel and an exact accretive determinant. The present theorem and its
proof retain the real-parameter hypothesis stated below.

30 October 2026. The original finite q-Hahn polynomial has a full leading
asymptotic, with a specified nonzero amplitude and relative error O(1/N),
uniformly on compact subsets of the right half-plane. Its magnetic
parameters are the ACTUAL scaled integers, varying in a compact strict
REAL parameter set. No rate of convergence of those parameters is assumed.

The proof starts with the previously proved actual logarithmic limit,
then uses the exact finite difference equation to improve its error.
A positive real Gaussian sum fixes the actual multiplicative constant.
Thus the transport equation below describes the original polynomial,
not merely a formal solution with an unspecified connection coefficient.

This theorem does not interpolate the discrete magnetic parameters
holomorphically, take a generic-q first normal, or control the assembled
global magnetic/channel sum.

## 1. Original finite source and theorem

Let 0<=j<=t<N, 0<=u<=t, v=t-u, theta=pi/N, and

    s_n=product_(r=1)^n 2 sin(r theta),
    beta(n,a)=s_n/(s_a s_(n-a)),
    E_a=beta(j,a) beta(u,a) beta(v,j-a)/beta(t,j),
    P_N(w)=sum_(a=a0)^a1 E_a w^a,
    a0=max(0,j-v), a1=min(j,u).                            (1)

These are exactly the coefficients of the
[original complete-circle phase compiler](actual_augmented_plat_phase_compiler.md).
Put

    lambda_N=(tau,xi,upsilon)=(t/N,j/N,u/N),
    D={0<xi<tau<1, 0<upsilon<tau}.

All uniform statements below take lambda_N in a fixed compact subset
K of D. In particular all saddles at w=1 stay a uniform distance from
the factorial boundaries, even when the two descriptions of a support
endpoint exchange at upsilon=xi or upsilon+xi=tau.

Use the original energy

    J(s)=integral_0^s log(2 sin(pi y))dy,
    Bcal(b,a)=J(b)-J(a)-J(b-a),
    Ecal_lambda(alpha)=Bcal(xi,alpha)+Bcal(upsilon,alpha)
                       +Bcal(tau-upsilon,xi-alpha)-Bcal(tau,xi).

For positive real w, let alpha_lambda(w) be the unique interior maximum
of Ecal_lambda(alpha)+alpha log w. The
[selected complex action theorem](actual_q_hahn_selected_complex_action.md)
continues both alpha and its critical value psi_lambda holomorphically
to Re w>0, with

    psi_lambda(w)=Ecal_lambda(alpha_lambda(w))
                          +alpha_lambda(w) Log w,
    w psi_lambda'(w)=alpha_lambda(w).                    (2)

All logarithms continue from their real values at w=1. Define, with
derivatives in the variable s,

    A_lambda(s)=sin^2(pi s) sin(pi(tau-upsilon-xi+s)),
    B_lambda(s)=sin^2(pi(xi-s)) sin(pi(upsilon-s)),
    F_lambda(s,w)=A_lambda(s)-w B_lambda(s),
    C_lambda=(sin(pi xi)/2)
       sqrt[sin(pi upsilon) sin(pi(tau-upsilon))
                         sin(pi(tau-xi))/sin(pi tau)].

The root selected in (2) satisfies F_lambda(alpha,w)=0. Define

    Acal_lambda(w)=sqrt(2 pi) C_lambda
          /sqrt[B_lambda(alpha_lambda(w))
                        F_(lambda,s)(alpha_lambda(w),w)].             (3)

The square root is the holomorphic continuation of its positive real
value at w=1. It is well-defined and never zero on Re w>0.

**Theorem.** Uniformly for lambda_N in K and w in any compact subset
of Re w>0,

    P_N(w)=N^(-1/2) Acal_(lambda_N)(w)
                 exp[N psi_(lambda_N)(w)] (1+O(N^(-1))).               (4)

The relative error is holomorphic in w. On smaller compact subsets
each fixed number of its w derivatives is O(N^(-1)) as well. Formula
(4) uses the actual lambda_N, not an arbitrarily chosen limiting triple.
Replacing lambda_N by its limit without controlling the displacement
would in general change the leading exponential and the amplitude.

## 2. Exact finite difference equation, including endpoints

Let D_w=w d/dw and h=1/N. The coefficient ratio in (1) gives the exact
identity

    sin^2(pi h D_w) sin(pi h(D_w+v-j)) P_N(w)
      =w sin^2(pi h(j-D_w)) sin(pi h(u-D_w)) P_N(w).       (5)

For every supported a, its coefficient equation is

    sin^2(a theta) sin((v-j+a)theta) E_a
      =sin^2((j-a+1)theta) sin((u-a+1)theta) E_(a-1).

At the lower endpoint either a=0 or v-j+a=0. At the first integer
above the upper endpoint either j-a+1=0 or u-a+1=0. Thus the zero
coefficients outside the support satisfy the SAME equation; there is
no endpoint source term in (5). In functional calculus notation,

    [A_lambda(h D_w)-w B_lambda(h D_w)]P_N=0.             (6)

Every sine product in (6) is a finite linear combination of the four
shifts w -> exp(i pi k h)w, k=-3,-1,1,3. In particular (6) is an
exact finite-shift identity, not an infinite differential expansion.

## 3. Uniform simplicity and the actual derivative bootstrap

The [negative-root theorem](actual_q_hahn_negative_root_source_polynomial.md)
gives positive rho_r and

    P_N(w)/P_N(1)=w^a0 product_r (w+rho_r)/(1+rho_r).

It fixes a holomorphic Log P_N real at w=1. Put

    G_N(w)=Log P_N(w)/N,   a_N(w)=D_w G_N(w).

The actual leading-limit theorem proves

    a_N-alpha_(lambda_N) -> 0                            (7)

uniformly on larger compact subsets of the right half-plane, also
when the real parameters vary in K. Fixed w derivatives converge
there too. Alternatively the explicit expression

    a_N=a0/N+(1/N)sum_r w/(w+rho_r)

directly bounds every fixed derivative on those compact subsets.
These bounds are independent of the positions of the negative roots.

For completeness, the selected branch is uniformly simple here.
Its positive limiting root measure gives

    alpha_lambda'(w)=integral rho/(w+rho)^2 dmu_lambda(rho).

For Re w>0 the integrands lie in an angular sector of width less
than pi, so their positive integral cannot vanish. Its measure has
positive mass strictly between zero and infinity. The support-strip
property of alpha makes A and B nonzero. Differentiating its saddle
equation gives

    F_s(alpha,w) D_w alpha=w B(alpha)=A(alpha),
    Ecal''(alpha)=-F_s(alpha,w)/A(alpha).                 (8)

Consequently F_s is nonzero. Continuity in the real parameters and
compactness make its modulus bounded away from zero on each of the
sets used below. Complex conjugation supplies the same statement in
the lower right quadrant.

Fix nested compact neighborhoods within Re w>0. For each fixed
c=i pi k, k in {-3,-1,1,3}, all small shifts stay in the larger one.
Taylor's theorem along the short logarithmic segment, using the
uniform derivative bounds, yields

    P_N(exp(c h)w)/P_N(w)
      =exp(c a_N(w))
           [1+(h c^2/2)D_w a_N(w)+O(h^2)].              (9)

Indeed the exponent before exponentiating is

    N[G_N(exp(c h)w)-G_N(w)]
        =c a_N+(h c^2/2)D_w a_N+O(h^2).

This is an estimate for the actual polynomial ratios. Inserting all
four shifts into (6), with their exact sine coefficients, proves

    0=F(a_N,w)+(h/2)(D_w a_N) F_ss(a_N,w)+O(h^2).        (10)

Equation (7) and the uniformly simple zero first imply

    a_N-alpha=O(h).

To justify this improvement, use the uniform expansion
F(a_N,w)=F_s(alpha,w)(a_N-alpha)+O(|a_N-alpha|^2), absorb
the quadratic term using (7), and use boundedness of D_w a_N in
(10). Cauchy's estimate on a slightly larger compact set then gives

    D_w a_N-D_w alpha=O(h)

and the analogous estimate for every fixed further derivative.
Substitution back into (10) now proves the sharper actual estimate

    a_N=alpha-(h/2)(D_w alpha)F_ss(alpha,w)/F_s(alpha,w)
                   +O(h^2).                             (11)

The order h^2 remainder is justified by the first improvement and
Cauchy, not assumed as a WKB ansatz.

Differentiating (3) and using (8) gives the exact transport identity

    D_w log Acal_lambda
       =-(1/2)(D_w alpha)F_ss(alpha,w)/F_s(alpha,w).       (12)

For example, differentiate log(B(alpha)F_s(alpha,w)). Its two extra
terms cancel:

    (B'/B)D_w alpha+w F_sw/F_s
       =(B'/B)(wB/F_s)-wB'/F_s=0.

Thus (11) identifies the logarithmic derivative of the ACTUAL source
with the explicit amplitude to error O(h^2).

## 4. The real sum fixes the constant, with arbitrary lattice offset

On a compact interior subinterval the sine-factorial estimate is

    s_n=sqrt[2N sin(pi n/N)] exp[N J(n/N)](1+O(N^(-1))).

One elementary derivation subtracts log x from log(2 sin pi x),
applies the trapezoidal estimate to the resulting smooth function,
and applies the usual integral remainder estimate for log(n!). The
errors and their required finite derivatives are uniform away from
0 and 1. Applied to every factor of (1), this gives

    E_a=N^(-1) C_lambda
           /sqrt[A_lambda(a/N)B_lambda(a/N)]
              exp[N Ecal_lambda(a/N)](1+O(N^(-1))).       (13)

The positive real saddle alpha=alpha_lambda(1) stays uniformly inside
the support. Strict concavity and the global factorial O(log N)
bound give an exponential loss outside a fixed saddle neighborhood.
Inside that neighborhood put z=(a-N alpha)/sqrt N. Taylor expansion
of the phase and the smooth prefactor in (13) gives a Gaussian
times

    H(alpha)+N^(-1/2)[H'(alpha)z
               +H(alpha)Ecal'''(alpha)z^3/6]
                +O(N^(-1)(1+|z|^8)),

with a uniformly integrable Gaussian majorant; one may first restrict
|z|<=N^(1/20), whose complementary tails are exponentially small.
Here H=C_lambda/sqrt(AB). The term of order N^(-1/2) is ODD.

No arithmetic assumption about N alpha is needed. For any shifted
grid h_Z(Z+eta), h_Z=N^(-1/2), and a smooth Gaussian times a fixed
polynomial f, the centered-cell Taylor formula gives

    |h_Z sum_(n in Z) f(h_Z(n+eta))-integral_R f|
                         <= (h_Z^2/8) integral_R |f''|.                (14)

The bound is independent of eta: integrate the Taylor remainder
over each cell centered at its grid point, then sum the disjoint
cells. The same estimate applies to the odd term, whose integral
is zero. Hence the arbitrary fractional saddle offset introduces
an error O(N^(-1)), not an uncontrolled O(N^(-1/2)) correction.
Gaussian tails allow the finite interval to be replaced by that
whole translated grid.

The resulting ACTUAL positive sum is

    P_N(1)=N^(-1/2)
       [sqrt(2 pi) C_lambda
          /sqrt(A(alpha)B(alpha)(-Ecal''(alpha)))]
                   exp[N psi_lambda(1)](1+O(N^(-1))).

By (8), A(-Ecal'')=F_s, so the bracket is precisely Acal_lambda(1).
This proves the real normalization in (4), uniformly in lambda_N.

## 5. Integrating the proved derivative error

The function

    H_N=Log P_N-N psi_(lambda_N)+(1/2)log N-log Acal_(lambda_N)

uses the branches fixed at w=1. Sections 3 and 4 prove

    D_w H_N=O(N^(-1)),   H_N(1)=O(N^(-1)).

Join 1 to each w in a chosen compact subset of Re w>0 by its straight
segment. The union of these segments is a compact set bounded away
from zero and the imaginary axis. A slightly larger compact set
supplies all the preceding derivative estimates. Integrating H_N'
on those bounded-length segments proves H_N=O(N^(-1)) uniformly.
Exponentiation proves (4). Cauchy's estimate on nested compact sets
then proves the asserted relative derivative bounds.

This is where both inputs are essential: negative roots gave the
actual leading selection and bounded holomorphic derivatives, while
the positive real sum fixed the multiplicative constant left open
by the finite difference equation.

## 6. The original physical column and both integer offsets

In the complete-circle chamber the exact compiler uses

    f_u(c_j)=(-1)^u q^[-(j+1)u] P_N(q^delta),
    q=exp(pi i/N), delta=t+j-(N-1).

Let w_star=exp[pi i(tau+xi-1)]. Then q^delta=w_star exp(pi i/N).
Keeping both occurrences of +1, formula (4) gives

    f_u(c_j)=N^(-1/2) Acal_(lambda_N)(w_star)
           exp[pi i(alpha_(lambda_N)(w_star)-upsilon)]
           exp{N[psi_(lambda_N)(w_star)
                            +pi i upsilon(1-xi)]}
           (1+O(N^(-1))).                               (15)

In detail, moving w_star to w_star exp(pi i/N) contributes
exp(pi i alpha)(1+O(N^(-1))), while q^[-(j+1)u] contributes
the otherwise easily lost factor exp(-pi i upsilon).

For actual complete-circle channels xi<=1/2 and tau+xi>=1-1/N.
On a fixed strict compact parameter set tau<1, these w_star and
their exact shifted values stay in a compact right-half-plane set.
Thus (15) holds at both level parities, at the folded endpoint,
and at composite levels. The high physical degree block inherits
the formula by its already proved exact index translation, with
the same transported column convention.

The scope is a single ACTUAL local column, with real magnetic
indices. Nothing here selects a global magnetic integration cycle,
proves cancellation bounds for the assembled plat, or differentiates
the root formula in the generic-q normal direction.

Audit: [finite equation, amplitude, and physical offsets](../experiments/audit_actual_q_hahn_uniform_complex_amplitude.py).
The finite computations test conventions and the predicted error;
the all-level uniform statement is proved by (5)--(14).


The magnetic parameter remains strictly real. No assembled-source conclusion follows from the local complex-amplitude theorem.

The theorem does not extend to complex magnetic parameters or an assembled-source asymptotic.