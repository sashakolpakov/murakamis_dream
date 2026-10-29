# Actual analytic bulk propagation and the forced Euler endpoint

28 October 2026. The finite-head projectors in the
[literal Euler/Gaussian network](actual_euler_gaussian_cauchy_network.md)
can be removed with an exponentially small error on a specified
interior analytic packet. The assertion has quantitative hypotheses
on its physical momenta; it is not an inference from an ideal
triangulation. Conversely, an exact forced finite-Euler equation
excludes some apparently regular single-dilogarithm charts. Both
statements concern the actual finite operators and retain the
original source.

## 1. An exact projector decomposition and an exponential estimate

Let `Pi_N` retain Laurent exponents `0,...,N-1`. If `f` is
holomorphic on an annulus containing `r exp(-s)<=|z|<=r exp(s)`,
its convergent Laurent series gives exactly

    Pi_N f=f-f_--f_+,                            (1)

where `f_-` has negative exponents and `f_+` has exponents at
least N. Put `M(rho)=sup_(|z|=rho)|f(z)|`. Cauchy's coefficient
bound, summed as a geometric series, gives

    ||f_-||_r <= M(r exp(-s))/(exp(s)-1),
    ||f_+||_r <= M(r exp(s))exp(-Ns)/(1-exp(-s)). (2)

Thus suppose an actual sequence `f_N` satisfies

    M_N(r exp(-s)) <= C_N exp(-delta Ns) M_N(r),
    M_N(r exp(s)) <= C_N exp((1-delta)Ns) M_N(r), (3)

with fixed `s,delta>0` and `log C_N=o(N)`. Then

    ||Pi_N f_N-f_N||_r
      <= 2 C_N exp(-delta Ns) M_N(r)/(1-exp(-s)). (4)

This is a norm estimate relative to the central packet envelope.
It does not assert a relative pointwise estimate at zeros of the
packet. For b heads, assume (3) for each of the two singly shifted
tori. Since each circle projector has sup-norm at most N,
telescoping the b commuting projectors proves

    ||Pi_N^(tensor b) f_N-f_N||_r
      <= 2b N^(b-1) C_N exp(-delta Ns)
                              ||f_N||_r/(1-exp(-s)).   (5)

All remainders in (1) are retained exactly before (3) is used.
There is no replacement of a finite projector by an unmarked
Cauchy pole.

Here is a useful sufficient physical condition. Write a nonzero
analytic packet as `f_N=a_N exp(NS)` on the polyannular collar,
allowing logarithms in S when its exponential is single-valued.
Suppose the amplitude ratios between the collar and central torus
are `exp(o(N))`, and every logarithmic radial momentum satisfies

    delta <= partial_(log|z_j|) Re S <= 1-delta.   (6)

Integrating (6) along each radial segment gives (3). Thus (5)
proves that a genuinely interior analytic packet is insensitive
to both head walls at exponential accuracy.

## 2. Application to actual transfer Euler atoms

Use `Q=exp(2pi*i/N)`, `h=2pi*i/N`, `F_a=(Q;Q)_a`, and the
literal polynomials

    u_N(t)=sum_(a<N)t^a/F_a,
    v_N(t)=sum_(a<N)(-1)^a Q^(a(a-1)/2)t^a/F_a.

On every fixed closed disk of radius less than 1/4, the actual
canonical polynomials, not just their nilpotent logarithms, obey

    u_N(t)=(1-t)^(-1/2) exp[-Li_2(t)/h](1+O(1/N)),
    v_N(t)=(1-t)^(1/2) exp[Li_2(t)/h](1+O(1/N)), (7)

uniformly with fixed derivatives on smaller disks. The branches
in (7) start at t=0. To check the actual truncation, the finite
logarithm for v is `L_N=sum_(a<N)t^a/[a(Q^a-1)]`. On any fixed
disk of radius less than one,

    L_N=Li_2(t)/h+(1/2)Log(1-t)+O(1/N).

For the lower half of the coefficients expand
`(exp(ha)-1)^-1=(ha)^-1-1/2+O(a/N)`; the upper half has a
geometrically small tail. On `|t|=1/2`, the elementary bound
`|Q^a-1|^-1<=N/4` gives `|L_N|<=N log(2)/4`.
The degree-N Taylor remainder of `exp(plus or minus L_N)` on
`|t|<=1/4` is therefore at most
`2 exp[-3N log(2)/4]`. Its leading exponential is bounded below
by `exp[-N Li_2(1/4)/(2pi)-O(1)]`, so this remainder is
exponentially small relatively. This proves (7) for both actual
polynomials. The same truncation argument was used for the
[primitive Hilbert-90 gauge](actual_hilbert90_gauge_dilogarithm_action.md);
the individual half-density factors in (7) are retained here.

For example the literal actual transfer operator is

    T_N f=Pi_N^(tensor b)[u_N(x^-1 z_2/z_1) f]. (8)

Take an actual finite-head packet f and assume the entire
polyannular collar of its transfer argument t lies in `|t|<=rho<1/4`.
The new action is

    S_new=S-Li_2(t)/(2pi*i).

Its two changed momenta differ from the old momenta by opposite
signed real parts of `Log(1-t)/(2pi*i)`. Each change has size at
most `-log(1-rho)/(2pi)`. Thus if the old momenta have twice
that margin from the head walls, (5) and (7) give an actual
analytic propagation formula for (8), with an exponentially
small projection remainder and an `O(1/N)` analytic amplitude
comparison. The same assertion, with opposite action, applies
to v and to the reversed transfer argument. This is a local
operator theorem, rather than formal substitution of a classical
symbol into a finite matrix.

For a finite ordered product, a telescoping error bound propagates
these local estimates. A sufficient condition is that each
intermediate packet satisfies (3) and that downstream propagation
in the corresponding packet norms is `exp(o(N))`. More generally,
an error with rate c remains exponentially small if the total
downstream amplification rate is strictly less than c. These are
explicit conditions to verify, not properties proved for the
original marked knot source.

## 3. Actual factorial and Gaussian bulk diagonals

The other nontrivial factors in the strict crossing are diagonal
in the physical momentum index. Their bulk symbols also admit
direct actual estimates. For `t=k/N` in a fixed compact subinterval
of `(0,1)`, define

    A(t)=integral_0^t Log(1-exp(2pi*i y))dy,
    Log(1-exp(2pi*i y))=log(2sin(pi*y))+pi*i*y-pi*i/2.

Then uniformly on that interval,

    F_k=sqrt(2N sin(pi*t))
         exp[N A(t)+pi*i*t/2](1+O(1/N)).         (9)

This follows without a formal product-to-integral replacement.
Exactly factor

    F_k=exp[pi*i*k(k+1)/(2N)-pi*i*k/2]
             (2pi/N)^k k! product_(r=1)^k g(r/N),
    g(y)=sin(pi*y)/(pi*y), g(0)=1.

Euler--Maclaurin applied to the smooth zero-free function `log g`
has uniform remainder `O(1/N)` here; Stirling's formula for k!
has the same uniform remainder. Their endpoint terms combine
into the precise square root and phase in (9). Inversion gives
the reciprocal factorial symbol with the same relative error.
The phase A and amplitude are analytic in a neighborhood of each
such interior momentum interval. Pointwise diagonal relative
error is therefore an actual weighted coefficient-norm estimate.
It does not by itself estimate a cancelling summed kernel.

Finally, with the original marked logarithm of x, the literal
Gaussian diagonal is exactly

    d_k=exp{N[pi*i*t^2+pi*i*t-2t Log x]-pi*i*t}. (10)

Thus no approximation or discarded scalar is needed for its
quadratic Fourier phase. Equations (5), (7), (9), and (10)
supply an actual interior analytic calculus for the elementary
crossing factors. They neither prove that every intermediate
geometric chart lies in these domains nor replace the original
cap by an interior packet.

## 4. A forced endpoint that an actual analytic chart cannot ignore

The literal Euler polynomials satisfy, at every nonzero t,

    u_N(Qt)=(1-t)u_N(t)+t^N/N,
    v_N(t)=(1-t)v_N(Qt)+t^N/N.                  (11)

The first equality is coefficient subtraction and `F_(N-1)=N`.
For the second, the top coefficient contributes
`(-1)^(N-1)Q^(N(N-1)/2)/N=1/N`.
Consequently each polynomial satisfies the actual two-point bound

    max(|w_N(t)|,|w_N(Qt)|)
          >= |t|^N/[N(1+|1-t|)], w=u or v.     (12)

Suppose a proposed uniform single-phase analytic chart has
`w_N(t)=a_N(t)exp[N B(t)]`, with amplitude bounded above by
`exp(o(N))` on a neighborhood. Since Qt tends to t, (12)
forces

    Re B(t)>=log|t|.                           (13)

This is a necessary condition, not a sufficient asymptotic theorem.
In particular the homogeneous dilogarithm phases in (7) cannot
describe the actual u polynomial on a neighborhood of a unit
argument in the upper half-plane, or the actual v polynomial at
its conjugate: there `Re B=-|Im Li_2(t)|/(2pi)<0`, whereas
`log|t|=0`. At `t=exp(pi*i/3)`, (12) is at least `1/(2N)`
for the pair of u evaluations, while that homogeneous phase is
exponentially decreasing. A forced endpoint branch must be
retained or cancelled by an exact larger network identity before
using that single phase. The statement is about the literal atom
argument; no unproved identification of that argument with a
developed geometric tetrahedron shape is used.

## 5. The remaining source transition

The original fixed-first-input cap and its averaged compact
realization are exact boundary data. Their entry into an interior
geometric analytic chart has not been proved. In particular (5)
cannot be applied to a boundary packet by assuming (6), and (13)
cannot be bypassed by citing algebraicity of a gluing solution.
An exact source-preserving reduction can exploit (5) where its
hypotheses hold, but must carry the remaining tail chains and
the forced terms in (11). Establishing the geometric intersection
degree of that complete marked chain remains the cycle-selection
problem in the comparison proposition, not a consequence of this
bulk calculus.

The [exact audit](../experiments/audit_analytic_bulk_projection.py)
checks the finite Euler equations, the two-point bound, the original
source-visible degree-zero wall, and explicit interior Laurent
packets. Its numerical samples of (9) check the normalization;
the proofs above give the uniform estimates.
