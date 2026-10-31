# Exact finite-height outer quadrature for the original five-crossing source

28 October 2026. The original double sum now has an exact outer
contour formula with finite upper and lower heights. Its source
edges, upper kernel and lower kernel are all explicit. A uniform
factorial estimate includes BOTH inner endpoints, so a certified
phase bound on the full inner polygon gives a polynomially sized
outer error without an additional amplitude assumption.

This establishes the applied quadrature criterion. The numerical
phase bounds proposed for the geometric contour are not proved
here, and no selected outer saddle or volume limit follows from
the identity alone.

## 1. The actual holomorphic outer function

Use `Q=exp(2pi*i/N)` and the EXACT marked interpolation
`Fhat_N(z)` from [the factorial theorem](exact_factorial_interpolation_and_complex_contours.md).
Define

    K_N(z,w)=Q^[-z(z+2)-w(z+1)]
                  Fhat_N(z)^3/[Fhat_N(w)Fhat_N(z-w)] exp(2pi*i*w),
    g_N(z)=exp(4pi*i*z) integral_0^z K_N(z,w)dw. (1)

Both powers of Q use `Q^z=exp(2pi*i*z/N)`. The two exponential
factors are integer-lattice gauges, with their full off-lattice
values retained. For an actual integer `0<n<N`, g_N(n) is EXACTLY
the selected inner integral of the original double sum in
[the inner quadrature theorem](source_preserving_inner_quadrature.md).

The function g_N is holomorphic on `0<Re z<N`. For a direct
proof use `w=t z`, `0<=t<=1`: both `Re w` and `Re(z-w)` lie
in `[0,Re z]`, where Fhat is holomorphic and nonzero. The
parameter integral is locally uniformly holomorphic. For fixed
z, any inner polygon from zero to z satisfying the same real-part
constraints gives the identical integral, by Cauchy's theorem
in its simply connected zero-free strip. In particular the
selected polygon `0 -> i lambda -> Re z+i lambda -> z` is allowed,
even when lambda is negative. No integer-n reflection formula
is being applied at a noninteger outer z.

## 2. Uniform factorial amplitudes INCLUDING the endpoint zero

Fix epsilon>0 and C<infinity. On

    D={zeta:0<=Re zeta<=1-epsilon, |Im zeta|<=C},

let `J(zeta)=integral_0^zeta Log(2sin(pi t))dt`, marked from
`0<t<1` and extended continuously at zero from the right strip.
Put

    Phi(zeta)=J(zeta)+(pi*i/2)(zeta^2-zeta).

There are positive constants c,C_1, independent of N>=2, with

    c sqrt(1+N|zeta|) exp[N Re Phi(zeta)]
       <= |Fhat_N(N zeta)|
       <= C_1 sqrt(1+N|zeta|) exp[N Re Phi(zeta)] (2)

uniformly on D. In particular its logarithmic error is `O(log N)`
on this CLOSED domain, including zeta=0. The mark of Phi equals
`[Li_2(1)-Li_2(exp(2pi*i*zeta))]/(2pi*i)` with the one-sided
strip continuation; it is not reset on a dilogarithm cut.

### Proof directly from the original Gamma product

In that product set z=N zeta. All kth-factor Gamma arguments
`N(k+zeta)` and `N(k-zeta)` have real part at least
`N(k-1+epsilon)`. Stirling's formula in a fixed right-half-plane
sector therefore gives, uniformly and with a summable remainder,

    log kth_factor
       =N phi_k(zeta)+(1/2)Log(1-zeta^2/k^2)+O_(epsilon,C)(1/(N k^2)),
    phi_k=(k+zeta)Log(1+zeta/k)
                   -(k-zeta)Log(1-zeta/k)-2zeta.

The O bound may be enlarged for finitely many small k; it is
uniform on D. The derivative of phi_k is
`Log(1-zeta^2/k^2)`. The sine product thus combines their
leading terms with the central Gamma term into N J(zeta).
The sum of the half-log terms is
`(1/2)Log[sin(pi*zeta)/(pi*zeta)]`, a bounded analytic function
on D with its removable value at zero. The summed remainder
is uniformly bounded (indeed O(1/N)).

It remains to control the CENTRAL Gamma without assuming
`|N zeta|` large. Put w=N zeta. Its difference from its leading
primitive is exactly

    log Gamma(1+w)-w Log w+w.

For `Re w>=0`, `|w|>=1`, uniform Stirling gives real part
`(1/2)log|w|+O(1)`. For `|w|<=1`, Gamma(1+w) is nonzero
and bounded above/below on the compact right half-disk, and
`w Log w` has a bounded continuous extension at zero. Thus
the same real part is `(1/2)log(1+|w|)+O(1)` everywhere.
The explicit phase relating G_N and Fhat contributes only
the bounded term `Re(pi*i*zeta/2)` after N Phi is removed.
Exponentiation proves (2). A finite initial set of N is
absorbed by compactness and nonvanishing, if needed.

## 3. A phase certificate suffices for the whole inner polygon

Let `x=z/N`, `y=w/N`, with x in a fixed compact late strip
`0<alpha<=Re x<=beta<1`, bounded imaginary part. Suppose
the chosen inner polygon Gamma_x has a uniformly bounded
number of straight segments and bounded total length, and
`0<=Re y<=Re x` throughout. The action from the LITERAL (1) is

    S(x,y)=3J(x)-J(y)-J(x-y)
                         +pi*i(3x+2y-x^2-xy-y^2). (3)

It is exactly the marked action used by the selected-inner
contour calculation. Equations (1)-(2), including the O(1)
linear Gaussian factors, give uniformly

    |exp(4pi*i*Nx)K_N(Nx,Ny)|
      <= C sqrt(N) exp[N Re S(x,y)]
                    /sqrt[(|y|+1/N)(|x-y|+1/N)]. (4)

The endpoint factors in (4) are uniformly integrable on this
polygon family. Since |x|>=alpha, y and x-y cannot both be
small. Near either endpoint the only remaining singularity
is distance to that endpoint to power -1/2. Its integral on
a straight segment of bounded length is bounded independently
of the segment's angle or distance from the endpoint. Summing
the fixed number of segments gives a uniform bound.

Consequently, with

    G(x)=sup_(y in Gamma_x) Re S(x,y),

the ACTUAL outer function has the quantitative estimate

    |g_N(Nx)|<=C N^(3/2) exp[N G(x)].            (5)

This controls the original inner endpoints rather than assuming
the interior square-root expansion extends through them.
For an interior compact subchart, the usual nonzero analytic
amplitude is more explicitly

    sqrt(2N) [sin(pi*x)^3/(sin(pi*y)sin(pi*(x-y)))]^(1/2)
            exp[-pi*i(3x+2y)] exp[N S(x,y)](1+O(1/N)),

with its inherited square-root mark. Only the bound (5) is
needed for the outer error criterion below.

## 4. Exact finite-height residue formula with the original integers

Let a<=b be integers in the allowed outer range. Set

    L=a-1/2, R=b+1/2.

These half-integer source edges enclose exactly the original
integers a,...,b. Let gamma_+ be any piecewise smooth upper
curve from `L+iH_L` to `R+iH_R`, with positive height, and
let gamma_- run from `L-iD` to `R-iD`, with D>0. Assume
their enclosed domain lies in `0<Re z<N`. Define paths
Gamma_+,Gamma_- from L to R by adjoining their vertical
endpoint connectors. All orientations below run left to right
on the upper and lower curves.

For every function g holomorphic on this closed domain,

    sum_(n=a)^b g(n)
       =integral_L^R g(s)ds
          +integral_(Gamma_+) g(z)/(exp(-2pi*i*z)-1)dz
          +integral_(Gamma_-) g(z)/(exp(2pi*i*z)-1)dz. (6)

Proof: the positive whole boundary is Gamma_- minus Gamma_+.
Use the residue-one kernel pi cot(pi z) and the identities
`pi cot(pi z)=-pi*i-2pi*i/(exp(-2pi*i*z)-1)` above,
`pi cot(pi z)=pi*i+2pi*i/(exp(2pi*i*z)-1)` below.
The unweighted halves are each `integral_L^R g/2` by
holomorphy. This proves (6) with no endpoint half-residue
convention or limit at infinite height.

Deform the real integral in (6) through Gamma_+. Then

    sum_(n=a)^b g(n)=integral_(gamma_+) g(z)dz
                                  +T_+(g)+T_-(g)+E(g), (7)
    T_+(g)=integral_(gamma_+) g(z)/(exp(-2pi*i*z)-1)dz,
    T_-(g)=integral_(gamma_-) g(z)/(exp(2pi*i*z)-1)dz,
    E(g)= i integral_0^(H_L) g(L+it)/(1+exp(-2pi*t))dt
          -i integral_0^(H_R) g(R+it)/(1+exp(-2pi*t))dt
          +i integral_0^D g(L-it)/(1+exp(2pi*t))dt
          -i integral_0^D g(R-it)/(1+exp(2pi*t))dt. (8)

The upper edge weights in (8) are at most one; the lower
weights are at most exp(-2pi*t). In particular no endpoint
derivative estimate for g is needed. The identity is still
the original integer source. The half-grid edges specify its
residue cycle rather than replacing its lattice values.

## 5. Applied geometric contour and its sufficient exponential bounds

Choose a fixed window `alpha_0=.51`, `beta_0=.99`, and take
`a=ceil(alpha_0 N+1/2)`, `b=floor(beta_0 N-1/2)` when nonempty.
Then `ell=L/N`, `r=R/N` belong to this fixed window.
All other original outer indices remain in the two real
collars and retain their separate estimates.

For fixed `u_g in (alpha_0,beta_0)`, `h_g>0`, put

    h(u)=min(h_g,h_g(1-u)/(1-u_g)),
    gamma_+: z=N[u+i h(u)], ell<=u<=r,
    gamma_-: z=N[u-.1i], ell<=u<=r.             (9)

The proposed marked geometric choices are approximately
`u_g=.86919340003238`, `h_g=.09218763788516`. Formula (7)
holds for any exact choices; taking the exact marked saddle
values makes the upper curve pass through that point. Its
kink is harmless because the curve is piecewise smooth.
Since beta_0<1, h has a fixed positive minimum on the window.

Suppose rigorous bounds on the FULL inner polygons establish

    G(u+i h(u))-2pi*h(u) <= Lambda_top,
    G(u-.1i)-.2pi <= Lambda_bottom,
    G(ell+i tau), G(r+i tau) <= Lambda_upperedge,
    G(ell-i tau)-2pi*tau,
             G(r-i tau)-2pi*tau <= Lambda_loweredge, (10)

on the respective top, bottom and connector ranges. They
must include the horizontal maximum AND both inner connector
pieces, not just the selected inner saddle. By (5) and the
exact kernel bounds, equations (7)-(10) give

    |sum_(n=a)^b g_N(n)-integral_(gamma_+)g_N(z)dz|
       <= C N^(5/2) exp[N Lambda],
    Lambda=max(Lambda_top,Lambda_bottom,
                           Lambda_upperedge,Lambda_loweredge). (11)

Indeed on the upper curve its kernel has modulus at most
`exp(-2pi*N h)/(1-exp(-2pi*N h))`, uniformly at most twice
the exponential for large N; the bottom has the analogous
fixed-height bound. The connector weights are already bounded
in (8). Their lengths are O(N), giving the stated polynomial.

Thus any certified Lambda strictly below the proposed geometric
rate proves that the OUTER discretization error is exponentially
smaller. Add the already proved inner error and both actual
real collars before inferring a statement about the full
original double sum. This theorem does not supply the bounds
(10), a nonzero outer Gaussian coefficient, or the geometric
volume calibration; those are separate required steps.

[Formula and endpoint-amplitude diagnostics](../experiments/audit_outer_finite_height_quadrature.py).
The residue calculation and uniform Gamma-product estimates
above, rather than numerical phase samples, prove (2), (6)-(11).
