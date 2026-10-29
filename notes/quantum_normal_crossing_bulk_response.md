# Whole quantum-normal crossing response and the marked geometric action

Research proof, 27 October 2026. The actual crossing coefficients
have a uniform whole-function comparison between the integral
quantum normal and the fixed-root positive-meridian normal on
every compact bulk-flow chart. The difference is an order-one
shape-dependent function. It is not a small matrix perturbation,
and the Gamma diagonal source comparison alone cannot intertwine
the crossings.

For an arbitrary knot braid, the complete original Cartan,
framing and pivotal factors cancel in a precise way. The remaining
bulk insertion is the Euler derivative minus the actual leading
action. At a marked flattened critical point it is the negative
action itself. This gives a universal comparison of the leading
formal geometric blocks, retaining their full source conventions.
It does not compare the selected global periods or resolve their
endpoint contributions.

The exact scalar source-line comparison is
[the whole Gamma theorem](whole_gamma_frame_profile.md), and its
all-head extension is
[the full-head source transport](full_head_gamma_source_transport.md).
The independent local crossing analysis is recorded in
[the actual crossing ratio calculation](actual_crossing_q_normal_meridian_ratio.md).

## 1. Two actual normal paths and the exact crossings

Put c=2pi*i, H_0=c/N and use a in a fixed complex compact set.
Define

    H=H_0+ca/N^2, b=a/(1+a/N), H b=ca/N,
    q_col=exp(H/2), Q_col=exp(H),
    M_col=exp(Hb/2)=-q_col^N,
    q_0=exp(H_0/2), Q_0=exp(H_0),
    M_+=exp(H_0b/2).                            (1)

The meridian M_+ is the Weyl inverse of the argument used in
the exact Gamma half-source comparison. It is not replaced by
M_col. Retain the actual x=-M/q mark as

    Log x=c/2+H(b-1)/2

on the color path, and with H_0 on the root path. This fixes
the Cartan half-character; it is not a principal-log reset.

At input integer positions i,j the actual stripped positive
coefficient sends `(i,j)` to `(j+k,i-k)` and is

    r_+=(-1)^k x^(-i-j-k)
         Q^[ij+(i-j)k-k(k+1)/2]
         {j+k choose k}_Q (M^2 Q^(-i);Q)_k.     (2)

The negative coefficient sends `(i,j)` to `(j-k,i+k)` and is

    r_-=x^(i+j-k) Q^(-ij)
         {i+k choose k}_Q (M^2 Q^(-j);Q)_k.     (3)

These are the actual canceled common-Verma formulas, with the
original common Cartan unit separated and then restored below.
No recurrences or asymptotic invariant identity are assumed.

Write u=i/N, v=j/N, t=k/N. For positive crossings fix a compact
flow domain with

    u<=1-epsilon, u-t>=epsilon,
    v>=0, t>=0, v+t<=1-epsilon.                (4)

For negative crossings interchange u and v in (4). These are
literal head-flow domains. The Pochhammer factors stay away
from both cyclotomic endpoints; factorial sums at zero are
handled by their removable functions. All coefficients in the
comparison are nonzero there for sufficiently large N and a
in the prescribed compact set.

## 2. The exact whole bulk response

Define the single-valued function on real -1<x<1 by

    F(x)=integral_0^x c y/(1-exp(-cy))dy, F(0)=0.            (5)

Its integrand has removable value one at zero. It has the
corresponding analytic continuation to a marked zero-free
crossing chart. Put

    B_+(u,v,t)=c[uv+(u-v)t-t^2/2]
       +F(v+t)-F(v)-F(t)+F(t-u)-F(-u),

    B_-(u,v,t)=-cuv
       +F(u+t)-F(u)-F(t)+F(t-v)-F(-v).          (6)

Then uniformly on (4) and on compact complex a-sets,

    r_(sign),col/r_(sign),root
             =exp[a B_sign(u,v,t)](1+O(1/N)). (7)

The ratio is a whole function of a on these compact normal
sets. Its expansion does not divide by a vanishing integer
normal factor. Formula (7) is before summing over the flow
indices.

Here is a uniform proof. For a quantum factorial with m/N=x,

    partial_H Log(Q;Q)_m
       =-sum_(r=1)^m r exp(Hr)/(1-exp(Hr)).

After division by N^2 this is a Riemann sum whose limit is
F(x)/c. The summand normalized by N has a removable limit at
r=0. Its second H derivative is O(N^3), uniformly below the
far cyclotomic endpoint. Since H-H_0=ca/N^2, Taylor's formula
with a uniform remainder gives

    (Q_col;Q_col)_m/(Q_0;Q_0)_m
                          =exp[a F(x)](1+O(1/N)).          (8)

For the Pochhammer in (2), take the same logarithmic derivative
at arguments b-i+r. Its range is uniformly separated from
zero and from -N by (4). The same Taylor/Riemann calculation
gives `exp{a[F(t-u)-F(-u)]}(1+O(1/N))`. The b-shift is
O(1) in each argument and changes this limit only by O(1/N).
The Gaussian coefficient is the factorial quotient in (8).
Finally the explicit Q monomial gives the quadratic term in
(6), while the x ratio contributes only O(1/N). This proves
(7). The proof for (3) is identical with its displayed support.

The original positive common Cartan unit is

    C(H,b)=exp{H[c/H+b-1]^2/4}.

Indeed the unrolled color is `c/H+b-1`, equal to N-1 on the
integral path and N-1+b on the fixed-root path. Therefore

    C(H,b)/C(H_0,b)=exp(-ca/4)(1+O(1/N)).       (9)

For a negative crossing use its inverse. This scalar cannot
be omitted from a crossing comparison; its cancellation in
the complete zero-framed word is the next step.

## 3. Why the scalar Gamma source map does not already intertwine R

At k=0 the stripped positive coefficient is simply

    r_+(i,j,0)=x^(-i-j)Q^(ij).

Its exact ratio on (1) is

    exp{(H-H_0)[ij-(b-1)(i+j)/2]}.             (10)

A diagonal conjugation on the two input/output strands
multiplies a checked crossing at equal inputs i=j by one:
the corresponding output is the same pair. This remains true
for different diagonal gauges on the two strands. A common
scalar can match i=j=0, but then cannot also match (10) at
another i=j for generic a.

For i/N approaching a nonzero bulk u the ratio in (10) tends
to `exp(ca u^2)`, whereas at i=j=0 it is one. Restoring the
common Cartan scalar changes both by the same factor and does
not repair this. Thus the actual Gamma diagonal source maps,
alone, cannot extend to a scalar-adjusted diagonal crossing
intertwiner. A nontrivial Cartan/base transport is necessary.
This is an exact local obstruction, not a knot example or a
claim that all possible source/base extensions are impossible.

## 4. The complete source cancels the nongeometric bulk terms

Let beta be any fixed b_strand-strand braid closing to a knot,
with writhe w and

    kappa_D=w-b_strand+1.

This integer is even. Let n=N-1 and let `sum_closed i` denote
the initial closed-strand index sum. Restoring the exact common
Cartan line, auxiliary root pivot `K^(1-N)`, root-compatible
twist, and the original cut 1/N gives the literal array weight

    W_aux=(1/N)x^(n kappa_D)
                  Q^(n sum_closed i) product_crossings r_sign. (11)

To verify (11), the product of common crossing scalars and the
inverse zero-framing twist is x^(nw). Each closed pivot is
`x^(-n)Q^(n i)`. Their product gives (11). Thus no isolated
Cartan scalar or numerical ideal-point multiplier was removed.

For the color path versus root path in (1), the prefactor
x^(n kappa_D) has ratio 1+O(1/N), while the Q prefactor has
ratio `exp[ca sum_closed(i/N)](1+O(1/N))`.

The genuine ordinary integral cap/twist is not this frozen
root auxiliary source. Their exact adapter, proved in
[the integral-source audit](integral_color_source_detour_audit.md), is

    W_aux,col/W_int,col
       =q_col^(Nn kappa_D)(Q_col^N)^(sum_closed i).          (12)

Its root value is one by knot parity. Its whole normal limit
is `exp{ca[kappa_D/2+sum_closed(i/N)]}`. Consequently the
original pivot-dependent position terms cancel, and (7) gives

    W_int,col/W_aux,root
      =exp{a B_beta(flow)}(1+O(1/N)),
    B_beta=sum_crossings B_sign-c kappa_D/2.   (13)

This is uniform for every fixed word on a common compact
interior flow chart. Every original projection is retained;
on the two actual walls the finite head is respectively the
genuine quotient or submodule. The common-Verma excursion
factor delta*w vanishes on both paths. External full modified
dimensions, if one passes from reduced to full states, remain
their specified separate factors, as in the regular-profile
and Gamma-source notes.

Equation (13) is an actual whole-array insertion comparison.
It does not interchange the finite sum with a limit and does
not bound the contribution of flows outside that compact chart.

## 5. The insertion is the Euler derivative minus the actual action

Choose a marked primitive

    L(x)=integral_0^x Log(1-exp(cy))dy.

Its logarithmic singularity at zero is integrable. Consistent
branch changes add linear terms. Integration by parts gives

    F(x)=x L'(x)-L(x).                         (14)

The leading stripped log-weights per N are

    A_+=-c(u+v)/2+c[uv+(u-v)t-t^2/2]
          +L(v+t)-L(v)-L(t)+L(t-u)-L(-u),

    A_-=c(u+v-t)/2-cuv
          +L(u+t)-L(u)-L(t)+L(t-v)-L(-v).      (15)

The signs in these linear terms follow directly from the
marked Log x=c/2+O(1/N) and the actual `(-1)^k` in (2).
Let E be the Euler field in these scaled position/transfer
variables. Equations (6) and (14) prove

    B_sign=(E-1)A_sign.                        (16)

For the whole root array (11), the leading log-weight per N is

    A_beta=sum_crossings A_sign
                  +c kappa_D/2+c sum_closed(i/N).         (17)

The initial closed positions and all intermediate positions
are homogeneous integral-linear functions of the actual free
flow coordinates: follow the one braid-permutation cycle from
the cut. Therefore the free-flow Euler field gives exactly

    B_beta=(E-1)A_beta.                        (18)

The constant `c kappa_D/2` in (17) must be kept. Its exponential
at complete integer N is one, but its Euler contribution is
exactly the nontrivial normal term in (13). Resetting it would
destroy the whole comparison.

## 6. The actual marked geometric block has a universal normal action factor

On the existing regular actual critical chart choose the marked
linear flattening so `d A_flat=0` at the chosen geometric point.
Subtracting an integral linear character does not change
`(E-1)A_beta`. Thus (18) gives there

    B_beta|_crit=-A_flat|_crit=-S_geo/c.         (19)

Here S_geo is the marked Log Q action of the actual state,
with its original Bloch-regulator and source signs. Equations
(13) and (19) give the leading formal geometric-block comparison

    block_int,col/block_aux,root
                   has normal multiplier exp(-a S_geo/c). (20)

The interpretation of (20) is precise. The finite-array
uniform proof is on the real bulk charts (4). At the complex
geometric point use the already constructed actual local
proper-ratio/WKB branch and its analytic marked continuation.
The two phases have the same leading critical scheme and
transverse Hessian; (13) inserts the nonzero amplitude
`exp(a B_beta)`. Ordinary nondegenerate transverse Gaussian
contraction therefore evaluates its leading multiplier at
the critical point, giving (20). The two framing directions
remain external as in the partial support theorem. The marked
action is constant along this critical framing torsor, so the
factor is independent of that framing.

This is a formal local block assertion, not an analytic
continuation of the finite sum inferred from real lattice
estimates. In the recorded geometric Log Q convention
`Re(S_geo/c)=Vol/(2pi)`. For real a the modulus of (20) is
therefore `exp[-a Vol/(2pi)]`, without a new adjustable
Cartan or ideal-point scalar.

The exact Gamma half-source remains necessary at the framing
and resonance boundaries. Its zeros are not supplied by the
nonvanishing exponential (20). No selected global geometric
contribution, endpoint/carry cancellation, full normal-profile
identity, or volume limit is proved by this block comparison.

## 7. Audit

[audit_quantum_normal_bulk_response.py](../experiments/audit_quantum_normal_bulk_response.py)
and its
[results](../experiments/quantum_normal_bulk_response_results.json)
evaluate the literal finite crossing products at 85-digit
precision for N=16 through 256 and compact real/complex normal
parameters. They check both signs, the original common Cartan
line, and the complete source/framing cancellation for several
even knot-parity values of kappa_D. They also check the exact
diagonal obstruction at N=2,3,5,16 and the marked Euler/dilog
primitive on positive and negative bulk intervals.

These checks confirm the formulas and their O(1/N) error scale.
The uniform proof is the Taylor/Riemann argument in Section 2;
the arbitrary-word source cancellation is exact (11)--(12).
No knot-specific example or selected-sum asymptotic is used.
