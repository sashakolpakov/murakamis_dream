# The projected transfer word, its degree repair, and its remaining source seams

28 October 2026. The two projected outer-collar theorems are genuine
original-operator contour identities. They can be inserted simultaneously
in a fixed signed word. A contractive degree average makes the entire
off-grid word preserve the original integer degree, without changing
its integral or its collar estimates.

This does not yet reduce the sharp bound to the known regular critical
regulator theorem. The retained physical interpolation still has Fourier
interval currents and fails the other crossing Ward equations pointwise.
This is a limitation of THIS phase representation, not an impossibility
of tame linear projections onto the intertwiner space.

## 1. Exact full word and a cost-free degree average

Use Rhat_sigma(z) of
[the lower](actual_projected_transfer_cot_completion.md) and
[upper](actual_projected_transfer_upper_collar.md) collar theorems. It
acts on the original orthonormal two-head space H_N tensor H_N. Every
physical input index remains an integer in 0,...,d, d=N-1. The full
original Cartan factor kappa is included. Write D|a,b>=(a+b)|a,b> and

    E_D(A)=sum_T P_T A P_T
          =integral_0^(2pi) exp(itD) A exp(-itD) dt/(2pi),
    B_sigma(z)=E_D(Rhat_sigma(z)).                    (1)

This is a completely positive contraction in operator norm and a
contraction in Hilbert--Schmidt norm. It is a fixed linear map of the
matrix entries, so holomorphy, removable zeros, and the collar bounds
survive unchanged. The integer transfer slices are also graded, hence
E_D fixes EACH original integer slice in this case.

Consequently, for any of the enlarged finite-height rectangles Gamma_i,

    R_sigma=integral_(Gamma_i) pi cot(pi z) B_sigma(z) dz/(2pi i).

For a fixed braid word the SAME original scalar is exactly

    K_N=chi_(beta,N) integral_(product Gamma_i)
             Phi_N(B_m(z_m)...B_1(z_1))
                      product_i [pi cot(pi z_i) dz_i/(2pi i)]. (2)

Here B_i is embedded on its actual neighboring heads, all spectators
are identities, and Phi_N is the original marked pivotal closure or
cup/cap functional. All integrals are compact and all head spaces
finite, so their ordered composition and Fubini in (2) are exact.

The product is now degree preserving POINTWISE in every transfer z_i.
The original marked cap may therefore be restricted to its forced
degree-d fiber after the ordinary caps, exactly as for the original
whole word. This removes a real potential source error; the degree
leak of the unsymmetrized interpolant is not unavoidable.

For any fixed number of factors the added individual collars have
exp(o(N)) operator cost, uniformly over their physical inputs. This is
not an estimate on an unrestricted exterior word, which may itself
have an exponential norm or scalar period.

## 2. What the repaired physical kernel actually is

Put

    s_c(nu)=[exp(2pi i nu)-1]/[2pi i(nu-c)],
    sinc(pi w)=sin(pi w)/(pi w).

The removable values are retained. If T=a+b, the positive kernel (1) is

    B_+(z)|a,b>=r(a,b;z)
       sum_(c=max(0,T-d))^(min(d,T))
          sinc^2(pi(b+z-c)) |c,T-c>.                 (3)

Indeed s_(T-c)(a-z)=exp(-2pi iz)s_c(b+z), and the two phase factors
cancel in their product, leaving the ENTIRE square in (3). For complex
z it is not the modulus square. For real z its coefficients are
nonnegative before multiplying by the original scalar r.

The exact Fourier representation is

    sinc^2(pi w)=integral_(-1)^1 (1-|t|) exp(2pi iwt)dt. (4)

Thus (2) retains physical interval data even after repairing degree.
Splitting (4) into its two analytic intervals leaves endpoints t=+/-1
and a common interface t=0. The weight vanishes at the outer endpoints
only to first order; its derivative has a jump at zero. These are not
automatically exponentially negligible. Integrating explicitly gives

    sinc^2(pi w)=[2-exp(2pi iw)-exp(-2pi iw)]/(4pi^2 w^2), (5)

with the complete removable value at w=0. Splitting the numerator
without its joint cancellation would introduce a false double pole.

At an INTERIOR stationary point of (4) the missing output relation
b+z=c is restored. At an interval endpoint or interface it is not an
available stationarity equation. Such a restricted critical scheme
must not simply be substituted into the previously proved FULL
original critical ideal.

The existing uniform vector bound exp(2pi|Im nu|) is tame at the FIXED
transfer height of the collar theorems. At a macroscopic complex
transfer z=N zeta, however, (5) can itself have exponent
2pi N|Im zeta|. This is a leading source phase, not a half-density
which may be discarded. For example for w=N xi with Im xi>0 and
xi bounded away from zero,

    sinc^2(pi N xi)
          =-exp(-2pi iNxi)/(4pi^2N^2xi^2)(1+o(1)).    (6)

The analogous opposite exponential occurs when Im xi<0. These are
the original Fourier endpoint sectors. They may subsequently cancel
in the complete source, but the outer-collar estimate does not prove
that cancellation or identify their coupled stationary support.

### A quantitative whole-word bound for the COMPLETE projection

There is a stronger estimate than bounding the individual sinc entries.
It controls the complete interval/interface aggregate, with no N-dependent
conditioning. Embed the original finite head space isometrically in
L^2([0,2pi],dtheta/(2pi)). If S is the head swap and D_r(z) is diagonal
on the original finite input basis with entries r(a,b;z), then literally

    Rhat_+(z)=P_N^(tensor 2) M_z S D_r(z),
    (M_z f)(theta1,theta2)
                =exp(iz(theta1-theta2)) f(theta1,theta2). (6a)

The output coefficients of (6a) are exactly the two sinc vectors, so
no boundary source has been changed. Multiplication has norm
exp(2pi|Im z|), the swap is isometric and P_N is orthogonal. Thus

    ||B_+(z)||op <= ||Rhat_+(z)||op
              <=exp(2pi|Im z|) max_(a,b physical)|r(a,b;z)|. (6b)

The same holds for the literal negative antiunitary mirror. In
particular REAL-transfer projection is contractive: it adds NO N
factor and no exponential rate to the scalar diagonal coefficient
envelope. This is not an estimate on a new norm or a changed source.

There is also an exact sharp absolute-column version. For nu=u+iv,

    sum_(c in Z) |sinc^2(pi(nu-c))|
                       =sinh(2pi|v|)/(2pi|v|),        (6c)

with value 1 at v=0. Indeed the original Fourier coefficients satisfy
|s_c(nu)|^2=exp(-2pi v)|sinc^2(pi(nu-c))|. Plancherel for
exp(i nu theta) gives sum |s_c|^2=(1-exp(-4pi v))/(4pi v),
which proves (6c). Restricting to the finite allowed c in (3) only
decreases the sum. Thus (3)'s physical output column has l1 norm at
most |r| times the right side of (6c). At real transfer the weights
form a subprobability distribution.

For any original b-head one-cut source, or fixed-width marked plat,
its actual functional norm is polynomial in N at complete color.
Tensoring the local operators with spectators changes none of (6b).
Consequently the COMPLETE interval sources in any fixed word satisfy
the genuine bound

    |Phi_N(B_m(z_m)...B_1(z_1))|
      <=poly_beta(N) exp(2pi sum_i |Im z_i|)
                       product_i max_(a,b)|r_sigma_i(a,b;z_i)|. (6d)

Every original cup/cap normalization and the explicit external chi
in (2) is retained. This is a quantitative full-source statement,
not a claim that separately cut Fourier sectors obey the same bound.
On fixed-height cotangent contours, the projection cost in (6d) is
O_T(1)^m. Their lengths, cotangent bounds and fixed word length add
only polynomial factors. Thus the endpoint/interface aggregate does
not create a new exponential envelope ON THOSE CONTOURS.

Conversely the macroscopic complex cost in (6b) cannot be replaced
by a uniform polynomial for this same scalar interpolation. If
z=N zeta, Im zeta!=0, and Re(b+z) lies in the physical output band,
choose an allowed c with |b+Re z-c|<=1. Formula (3) then has an
individual output coefficient of size

    |r(a,b;z)| exp(2pi N|Im zeta|)/poly(N),           (6e)

provided its total-degree block contains that c. For example a+b=d
contains every physical c. The denominator in (5) is O(N^2), while
its numerator has the stated exponential size. Hence the rate
2pi|Im zeta| is sharp already for the retained physical kernel.
This does not prove it survives the exterior knot pairing; it proves
that such a cancellation must be retained in a sharp complex-contour
argument rather than absorbed into a polynomial projection norm.

## 3. An exact remaining E-coproduct defect

Use the original complete scaled currents

    Ecal|a>=(Q^-a-1)|a-1>, K|a>=x Q^-a|a>,
    E=Ecal tensor K + I tensor Ecal,
    q=exp(pi i/N), Q=q^2, x=-q^-1.

The original complete R commutes with E. Its repaired interpolation
B_+(z) does not. An exact entry at z=1/2 is

    <0,0|[E,B_+(1/2)]|1,0>
      =(Q^-1-1) r(0,0;1/2) (4/pi^2) (1-Q+q^-1).     (7)

To check it, the two degree-one output weights in (3) are both
4/pi^2, while

    r(1,0;z)/r(0,0;z)
          =x^-1 (1-Q)/(1-Q^(1-z)).

At z=1/2 this gives (7) directly. It is nonzero at EVERY N>=2:
r(0,0;1/2)=kappa x^(1/2)/Fhat(-1/2) is nonzero, and
1-Q+q^-1=0 would imply q^3=q+1. The latter is impossible since
|q+1|>=sqrt(2)>1. Therefore degree repair alone does not turn the
pointwise five-function density into the complete crossing Ward
solution.

This defect is visible to an original source. At N=2 use precisely
the balanced cup and FULL marked row

    p_(a,b)=2 x^(a-1) delta_(a+b,1),
    m_(a,b)=x^b/4,  x=i.

A direct four-state calculation gives

    m [E,B_+(1/2)] p
          =(-16-52i)/(9pi^2 Fhat(-1/2)) != 0.          (8)

All original kappa and x phases are included in this formula. A
marked-fiber replacement must not be applied AFTER the degree-lowering
insertion E; (8) uses the full marked row. In contrast, the complete
cotangent integral of this commutator is [E,R]=0. Its compensating
source currents are therefore essential to any argument based on
pointwise Ward equations. This is not a new nonzero knot invariant
with an arbitrarily inserted coupon; it tests the proposed density
identity before the exact integral is assembled.

## 4. Tame projections exist; they do not supply a free phase theorem

No impossibility of a further tame algebraic repair follows from (7).
For example the Hilbert--Schmidt orthogonal projection onto the common
E,F,K intertwiner space always exists, has HS norm one, and has
operator-to-operator norm at most N on a two-head space of dimension
N^2. It preserves the complete R integral and every added zero. It
need not preserve the separate original transfer residues. More
importantly E,F,K intertwiners need not implement the specified braid
crossing: they also include other functions of the two-head Casimir.
Their phases and canonical relations have to be derived afresh.

The same warning applies to the full Hurwitz intertwiner line. If
the complete physical algebra makes that solution space span{R}, its
HS projection is exactly

    P_R(A)=<R,A>_HS R / ||R||_HS^2.                  (9)

It is still tame as a linear operator. At an integer transfer k the
scalar coefficient is

    lambda_k=||R_k||_HS^2/||R||_HS^2, sum_k lambda_k=1,

because the original transfer slices have disjoint matrix-entry
supports. But the entire known exponential crossing matrix R is now
a CONSTANT factor in the density P_R(Rhat(z))=lambda_N(z)R. The
original word asymptotic is not obtained by analyzing the harmless
scalar lambda alone. Such a projection changes the phase representation
and packages its difficulty into the retained R factor; it does not
contradict (7) or provide the requested sharp geometric bound.

## 5. Critical-path conclusion

The theorem removes both artificial OUTER transfer collars, with the
physical projections and source retained. Formula (2) is an exact
full-word representation, and (1) repairs its pointwise degree at no
norm cost. This is substantive source control.

What is not yet proved is a bulk-only estimate with exponential rate
at most the knot volume. The regular critical-regulator theorem applies
to the genuine full crossing/gluing equations. To use it here one must
either control the complete Fourier interval currents in (4)--(6),
show their coupled stationary support belongs to that actual saturated
graph, or give a different phase-preserving source transport. Keeping
the finite physical head sums avoids these new complex-head seams,
but then the remaining positive matrix bound still loses the global
outer phase and is not sharp by knot volume. These alternatives are
not supplied by the two local collar estimates alone.

[Audit](../experiments/audit_actual_projected_transfer_word_source.py):
exact degree-averaged columns and contraction, original R and E Ward,
the all-level entry (7), the full original source (8), the retained
triangle Fourier identity, and the exact full-intertwiner projection
weights. No sharp bound for a knot family is inferred.
