# A source-specific Fourier gap for the exact filling endpoints

29 October 2026. The full finite filling kernel, including its linear
normal weight, has exponentially small endpoint-frequency strips when
paired with an analytic source having a strict complete-color maximum.
This is an estimate on a truncated ORIGINAL color corridor. It does not
bound colors outside that corridor or prove survival of the remaining
filled saddle. No Fresnel endpoint remainder is replaced by a polynomial
error.

## 1. An exact finite Fourier lemma with its source hypotheses

Let H=floor(delta N), d_N=(H+1/2)/N. Suppose a physical packet c_h,
-H<=h<=H, has a holomorphic interpolation f_N(z), for
|Re z|<=2delta and |Im z|<=sigma_0, satisfying

\[
 \|f_N(x+iy)\|\le C N^B
       \exp\{N(F-a x^2+C_0 y^2)\},\qquad a>0,
                                                        \tag{1}
\]
\[
 \|c_h-f_N(h/N)\|\le C N^B e^{N(F-\gamma)},\qquad\gamma>0.
                                                        \tag{2}
\]

These are hypotheses on the specified source, not on arbitrary
holomorphic test functions. Scalar or finite-dimensional vector/operator
packets with the displayed norm bounds are allowed. All constants are
independent of N. For any fixed phi_0>0 and fixed nonnegative integer r,
there are g>0 and C',B' such that

\[
 \boxed{\left\|\sum_{h=-H}^Hh^r c_h e^{i\phi h}\right\|
       \le C'N^{B'}e^{N(F-g)},\quad
       \operatorname{dist}(\phi,2\pi\mathbb Z)\ge\phi_0.} \tag{3}
\]

The distance is at most pi; the assertion is empty if phi_0>pi.
In particular no number-theoretic restriction on N is involved.

Here is an exact contour proof retaining the finite endpoints. Reduce
phi modulo2pi into [phi_0,2pi-phi_0], which changes no physical value.
For a fixed small sigma>0 use the rectangle in the UNWRAPPED variable
z whose vertical sides have Re z=+/-(H+1/2) and whose horizontal sides
have Im z=+/-sigma N. Then

\[
 \sum_{h=-H}^H h^r f_N(h/N)e^{i\phi h}
 =\frac1{2\pi i}\oint
 z^r f_N(z/N)e^{i\phi z}
                         (\pi\cot\pi z-i\pi)\,dz.      \tag{4}
\]

Every enclosed integer has residue one. The subtracted entire term
-i pi changes no residue and is essential for simultaneous upper and
lower decay. Indeed

    pi cot(pi z)-i pi=2pi i/(exp(2pi i z)-1).

On the upper horizontal side its product with exp(i phi z) is at
most 4pi exp(-phi sigma N); on the lower side it is at most
4pi exp(-(2pi-phi)sigma N), for all sufficiently large N. On either
vertical half-integer line the sharper exact bound is

    |exp(i phi z)(pi cot(pi z)-i pi)|
        <=2pi exp[-phi_0 |Im z|]<=2pi.

Choose sigma<=sigma_0 so that
C_0 sigma^2<=min(a delta^2/8,phi_0 sigma/2). For large N,
d_N>=delta/2. The horizontal exponent in (4) is at most
F-phi_0 sigma/2, and the vertical exponent is at most
F-a delta^2/8. Its contour length and z^r cost only powers of N.
Equation (2) contributes at most C N^(B+r+1)exp[N(F-gamma)] on the
physical grid. Thus one may take

    g=min(gamma,a delta^2/8,phi_0 sigma/2)>0.             (5)

This proof neither discards a vertical current nor assumes that a
universal residue rewrite lowers the maximum of arbitrary source values.
Its input is precisely the state-specific analytic bound (1).

## 2. Apply the lemma BEFORE any Gaussian approximation to the filling

Use the original q,Q,kappa and the exact full-jet kernel from
[the coherent filling theorem](actual_coherent_filling_gaussian_chirp.md).
For t_k=(k+1/2)/N and y_k=2pi i(t_k-1/2), write

\[
 K_P(h)=\frac{2(-1)^{N-1}}{N^2}
  \sum_{k=0}^{N-1}h_k e^{hy_k}
   \left[(h+2Py_k/\hbar)\sinh y_k+\cosh y_k\right].    \tag{6}
\]

Here |h_k|=1 for every integer P and real physical data. The original
normal derivative has not been dropped: 2Py_k/hbar is its unwrapped
linear weight, and the h term comes from the same exact circle
difference. Every factor outside exp(hy_k) is at most polynomial in
N for fixed P, uniformly over k.

Here beta and K_P are the coefficients of the NORMALIZED power
f_P=r_N^(2P), exactly as in the filling theorem. The actual box
R^(-1)R^(2P) multiplies every color pairing below by the known unit
phase kappa^(2P). In particular the actual prefactor corresponding
to kappa^(-P) in (10)--(11) is kappa^P. This original phase is kept;
it does not change any norm estimate.

Let K_P^end retain any subset of the original k values with
|t_k-1/2|>=eta_0>0. For a physical EVEN core c_h=c_(-h), the original
half-color convention gives the exact truncated pairing

    sum_(h=0)^H beta_(N-h-1)c_h
             =(1/2)sum_(h=-H)^H K_P(h)c_h.             (7)

In (6), phi_k=2pi(t_k-1/2) belongs to [-pi,pi], and
dist(phi_k,2pi Z)>=2pi eta_0 on the retained endpoint strips.
Apply (3) for r=0,1 and sum the N original k values. It follows that

\[
 \boxed{\left\|\frac12\sum_{h=-H}^H K_P^{\rm end}(h)c_h\right\|
          \le C_P N^{B_P}e^{N(F-g)}.}                 \tag{8}
\]

This is a bound on the EXACT finite endpoint part, with both parities,
all gcd cases and the normal source retained. There is no infinite
charge tail to estimate, and no O(1/N) Fresnel error against an
exponential target. The bounded current of section8 in the coherent
filling note is consistent with (8), but (8) does not assume that every
endpoint remainder equals that one Ward forcing.

## 3. The actual mixed-source input and its precise remaining scope

The EXACT finite packet in
[the analytic original-source theorem](actual_pretzel_exact_analytic_color_packet.md)
provides (1)--(2) for a mixed pretzel period at fixed odd s>=5,
on a sufficiently small complete-color corridor. Here the other
physical cusp colors may be fixed in a sufficiently small corridor.
To specify the interpolation, retain a fixed regular high Newton-index
window in each box, use its canonical paired factorial continuation
Fhat(v-h)Fhat(v+h) and q^(h^2), and apply the UNCHANGED Hermite
functional Phi_2. The lower index windows and the full nonempty alias
sets are their proved exponentially smaller physical source errors.
Its separate exact-interpolation bridge must be retained; a pointwise
relative O(1/N) approximation on the color lattice alone does NOT imply
(2) with an exponentially small Fourier error. This construction is
even in the continued color, rather than an
arbitrary exp(pi i h) extension.

The resulting nonzero analytic leading phase, composed with chi=pi z,
is even in the color variable z=h/N.
Its real second derivative at zero is strictly negative, uniformly
for the other sufficiently small physical colors. Taylor's formula
and the elementary inequality 2|xy|<=epsilon x^2+y^2/epsilon give

    Re Phi(x+iy)<=Re Phi(0)-a x^2+C_0 y^2.

The analytic amplitude is uniformly bounded by a polynomial in N.
The exact high-window finite-source interpolation error and the alias
bound supply (2), after shrinking the corridor so that its height stays within
gamma/2 of the complete height. Thus (8) removes a genuine class of
endpoints of this original mixed-source corridor.

Aliases need not be even and are estimated before folding. Directly
from the original finite H,D data, |a_n|<=1+|P| for 0<=n<N and
|beta_j|<=2(1+|P|). Their entire corridor pairing therefore costs
only another factor 2N(1+|P|) times the proved alias error. The exact
normal forcing and the vertical color sides in (4) are both retained.

This does not estimate physical colors h>H. It does not discard
the central k strip, establish a nonzero filled critical pairing,
or identify its action with a preferred topological longitude. A
fixed-large-filling proof still requires those three steps, including
the peripheral sign convention. The present source-conditioned
estimate is not an all-input operator norm bound for a free exterior.

## 4. The combined source is a total derivative, with exact paired charges

There is a useful exact representation for the remaining coherent
packet, avoiding the separate interpolation of any a_n. For ANY
physical even core in (7), set

\[
 \mathcal F_N(z)=\sum_{h=-H}^Hc_h e^{2\pi i h z},\qquad
 U_N(z)=e^{2\pi iPNz^2}\sinh(2\pi i z)\mathcal F_N(z),
 \qquad z_k=(k+1/2)/N-1/2.                             \tag{9}
\]

The literal entire-normal filling kernel (6) gives EXACTLY

\[
 \boxed{\sum_{h=0}^H\beta_{N-h-1}c_h
   =\frac{(-1)^{N-1}\kappa^{-P}}{2\pi iN^2}
                           \sum_{k=0}^{N-1}U_N'(z_k).} \tag{10}
\]

Indeed differentiating U multiplies its sinh term by
2pi i(2PNz+h) and differentiating sinh supplies 2pi i cosh.
These are precisely BOTH linear normal contributions in (6).
This holds with operator-valued c_h in their unchanged exterior
order.

In particular U_N(1/2)=U_N(-1/2)=0, and

    U_N'(1/2)=U_N'(-1/2)
       =-2pi i exp(pi iPN/2)sum_h(-1)^h c_h.

The periodic extension of U_N' is continuous, with piecewise smooth
derivative. Its Fourier series is absolutely convergent (two
integrations by parts bound its nonzero coefficients by a constant
times frequency^(-2)). Exact midpoint Fourier selection and one
integration by parts therefore prove

\[
 \boxed{\sum_{h=0}^H\beta_{N-h-1}c_h
 =(-1)^{N-1}\kappa^{-P}
  \sum_{m\in\mathbb Z\setminus\{0\}}
   (-1)^{m(N-1)}m\int_{-1/2}^{1/2}
    e^{2\pi iN(Pz^2-mz)}\sinh(2\pi i z)
                                    \mathcal F_N(z)\,dz.} \tag{11}
\]

The series is absolutely convergent for each N. Its constants can
depend on the actual source; no uniform asymptotic tail estimate is
silently inferred. The zero charge vanishes EXACTLY from the two
original endpoint zeros of U_N, not by discarding a Fresnel current.
Because the core is even, mathcalF_N is even and U_N is odd. The
integrals at -m and m are opposites, so their weighted contributions
in (11) are equal. Thus the +/-m channels ADD exactly, at every
parity and level, before any saddle approximation.

For the source obeying (1)--(2), mathcalF_N and its fixed derivatives
are exponentially small on any fixed real strip eta_0<=|z|<=1/2,
by (3). Equations (10)--(11) therefore provide a source-faithful
central phase problem with exact normal charge m. The finite-k
endpoint bound (8) is already quantitative. Passing between a
restricted central integral and (11) must still retain the new
side currents at its artificial cutoff; absolute convergence at
fixed N alone is not a uniform exponential bound on all charges.
The uniform infinite-tail bound is proved separately below; a
central-saddle conclusion is not inferred from fixed-N convergence.

## 5. A uniform exponential high-charge tail, with its paired current

Under (1)--(2), the large-|m| part of (11) is exponentially smaller
than exp(NF). This is a UNIFORM estimate; absolute convergence at
each fixed N alone would not suffice. For fixed integer P there are
M_P>0 and finite B_P,C_P, independent of N, such that

\[
 \boxed{\sum_{|m|>M_P}
   \left\|m\int_{-1/2}^{1/2}U_N(z)e^{-2\pi imNz}\,dz\right\|
           \le C_P N^{B_P}e^{N(F-g_*)}.}              \tag{12}
\]

The positive gap g_* and the contour width below depend ONLY on the
source hypotheses, not on P. This matters for independently large
fillings with no comparability between their lengths.

First, (3), for a small real neighborhood of +/-1/2 in z, extends
to a FIXED small complex strip. In its exact rectangle proof, an
extra Im z=v in the Fourier variable costs at most
exp(2pi delta |v|N) on the physical source support. The same
argument applies to fixed derivatives of mathcalF_N, by taking r
larger in (3). Thus for some fixed sigma_1,g_1>0,

    ||mathcalF_N^(j)(+/-1/2+iv)||
        <=poly(N)exp[N(F-g_1)], |v|<=sigma_1, j=0,1,2.

Fix a smaller sigma>0 using ONLY this source strip. On either
endpoint line, at height -v, the chirp costs at most
exp(2pi|P|Nv), and its first two derivatives cost powers of N and P.
Keep that v-dependent cost; do not bound it by exp(2pi|P|sigma N)
and then shrink sigma as the filling length grows.

For m>0 shift its Fourier integral DOWN by sigma. On the lower
horizontal side the elementary physical-grid estimate

    ||mathcalF_N(x-i sigma)||
        <=poly(N)exp[N(F+2pi delta sigma)]

gives an upper bound

    poly(N)exp{N[F-2pi sigma(m-|P|-delta)]}.            (13)

Crucially the two vertical currents must be paired. Their common
Fourier endpoint phase is (-1)^(mN), and their difference is

    V_N(v)=U_N(1/2-iv)-U_N(-1/2-iv), 0<=v<=sigma.

The ORIGINAL integer Fourier polynomial mathcalF_N is periodic.
Together with the sinh zeros this gives V_N(0)=V_N'(0)=0 exactly,
as already checked before (11). The source derivative bound on the
two vertical strips, with the chirp cost explicitly retained, gives

    ||V_N(v)||<=poly(N,P)v^2
                          exp[N(F-g_1)+2pi|P|Nv].

Consequently the paired vertical contribution obeys

\[
 \left\|m\int_0^\sigma e^{-2\pi mNv}V_N(v)\,dv\right\|
 \le\frac{\operatorname{poly}(N,P)m}{(m-|P|)^3N^3}
                           e^{N(F-g_1)},\quad m>|P|. \tag{14}
\]

For m>M_P>=2|P|+2delta+2 this is at most a fixed multiple of
poly(N,P)m^(-2)N^(-3)exp[N(F-g_1)], which is summable. The
horizontal bounds (13) have an exponentially convergent geometric
sum with gap at least 2pi sigma, independent of P. Take
g_*=min(g_1,2pi sigma)>0. The upper shift for negative m is
identical; for an even core it also follows from the exact +/-m
identity. This proves (12).
Neither individual vertical current is set to zero.

Here is the precise multiport justification. Leave all remaining
z_j variables REAL until their tails have been removed. On the
entire source U=exp(2pi iN sum P_i z_i^2) product_i sinh(2pi i z_i)
mathcalF_N(z), define the commuting COLOR-register functionals

    D_i U=(2pi iN^2)^(-1)sum_k partial_i U(z_(i,k)),
    I_(i,m)U=(-1)^(m(N-1))m integral_[-1/2,1/2] U dz_i,
    D_i^lo=sum_(0<|m|<=M_i) I_(i,m), D_i^tail=D_i-D_i^lo.

Midpoint Poisson and the matched endpoint values prove D_i=sum_m
I_(i,m) exactly. These operations act linearly on scalar color
registers; they do NOT commute or reorder physical Hopf boxes or
matrix-valued exterior coefficients. Exact telescoping gives

\[
 \prod_iD_i-\prod_iD_i^{\rm lo}
 =\sum_i\left(\prod_{j<i}D_j^{\rm lo}\right)
                   D_i^{\rm tail}\left(\prod_{j>i}D_j\right). \tag{14a}
\]

For fixed M_j, the real-integral functional D_j^lo has supremum
norm at most sum_(0<|m|<=M_j)|m|=M_j(M_j+1). The original D_j
uses N samples and one derivative. Its mixed derivatives on U cost
powers of N and P_j: all remaining chirps have modulus ONE at real
z_j, while differentiating them supplies only P_j N. Differentiating
mathcalF_N supplies integer powers of h_j, bounded by powers of N.

The endpoint Fourier bound and (14) are uniform in these remaining
real spectators AND in every mixed derivative just described. To
see this directly, sum the other physical h_j in absolute value
using the original source bound
exp[N(F_0-a sum x_j^2+C sum y_j^2)]. Their sums and fixed powers
of h_j cost only powers of N; no positive exponential is introduced.
The contour shift and paired vertical current occur ONLY in the
tail coordinate i. Thus each term of (14a) is bounded by
poly_(s,p)(N)exp[N(F_0-g_*)], with g_* fixed by the source and
independent of the largest slope. There is no uncontrolled infinite
charge sum in a spectator coordinate. Later central saddle-contour
motions are made only AFTER (14a) has removed the tails.

Equations (8),(11),(12) leave a FINITE set of nonzero coherent
central charges for every fixed collection of integer fillings.
Their source Fourier saddle is made explicit next. Comparing the
remaining charge actions and bounding colors outside the chosen
corridor are separate tasks.

## 6. A nonzero central Fourier packet from the EXACT analytic source

This step uses the stronger, proved input from the exact color packet:
on a fixed complex polydisk, with r color ports,

    C_N(pi x)=N^(3/2)e^(-i s pi d/4) A(pi x)
                                  exp[N phi(x)](1+O(1/N)),
    phi(x)=Phi_s(pi x), phi(0)=F_0,
    phi''(0)=2pi i tau_s I,
    tau_s=(1+exp(2iu_s))/2, Im tau_s>0.                 (15)

The exact function C_N, not just this leading expression, has the
complex Gaussian bound (1) in all continued coordinates. The case
needed for filling all boxes is r=s. Define the ENTIRE finite packet

    mathcalF_N(z)=sum_(|h_i|<=H) C_N(pi h/N)
                                         exp(2pi i h dot z). (16)

It is exactly even in every z_i. For a fixed sufficiently small
complex z-polydisk, the holomorphic implicit-function theorem defines

    grad phi(xi(z))+2pi i z=0,
    Psi(z)=phi(xi(z))+2pi i xi(z) dot z.

Then, UNIFORMLY on a smaller fixed complex polydisk,

\[
 \boxed{\mathcal F_N(z)=N^{(r+3)/2}e^{-i s\pi d/4}
         B(z)e^{N\Psi(z)}(1+O(1/N)),\quad
 B(z)=\frac{(2\pi)^{r/2}A(\pi\xi(z))}
                       {\sqrt{\det[-\phi''(\xi(z))]}}.} \tag{17}
\]

The Gaussian square root is fixed at zero by the positive real part
of -phi''(0). In particular

    B(0)=A(0)(-i tau_s)^(-r/2) !=0,
    xi(z)=-z/tau_s+O(||z||^3),
    Psi(z)=F_0-i pi sum_i z_i^2/tau_s+O(||z||^4).        (18)

Both Psi and B are even in each z_i and B is nonzero on a smaller
polydisk. All phases in (15) remain in (17).

Here is the finite-source proof of (17). Apply exact half-integer
cotangent rectangles in the h coordinates to (16). The two constant
cotangent parts give the ordinary integral with density N^r. The
nonconstant parts cost exp(-2pi sigma N) on its horizontal sides;
the extra factor exp(2pi iN x dot z), the quadratic complex-source
growth and the small complex z displacement cost strictly less after
choosing sigma first and then the z-polydisk. The vertical h sides
keep their strict endpoint gap from (1). This proves

    mathcalF_N(z)=N^r integral_[-d_N,d_N]^r
                C_N(pi x)exp(2pi iN x dot z)dx
                          +poly(N)exp[N(F_0-g)], g>0. (19)

Slightly changing the half-integer endpoints of the integral is
exponentially harmless, and all corresponding side currents are in
the displayed error. This is a statement about the EXACT holomorphic
source; a pointwise real-grid O(1/N) error would not imply (19).

Deform the ordinary integral locally to the parallel real contour
through xi(z). Its end connectors retain their strict gap for small
z. The real part of phi'' remains negative definite, uniformly near
zero. The elementary multivariate Gaussian integral and the uniform
analytic amplitude in (15) therefore give (17); its exponentially
small cotangent remainder stays below the saddle after shrinking the
z-polydisk. This also proves the required uniformity BEFORE any later
z-contour motion. No original-cycle coefficient has been assigned.

For completeness, apply (11) successively in all r filled ports.
The actual R powers restore their phases as explained above. The
exact corridor source is

\[
 (-1)^{r(N-1)}\kappa^{\sum_iP_i}
 \sum_{m_i\ne0}(-1)^{(N-1)\sum_i m_i}\prod_i m_i
 \int_{[-1/2,1/2]^r}
  e^{2\pi iN\sum_i(P_i z_i^2-m_i z_i)}
                   \prod_i\sinh(2\pi i z_i)\mathcal F_N(z)\,dz.
                                                               \tag{20}
\]

All original normal charges and the full original source are kept.
Every coordinate reflection (m_i,z_i)->(-m_i,-z_i) preserves its
term, so the 2^r all-unit charges have exactly equal contributions,
including the even-level signs. There is no charge with m_i=0.
The large-charge remainder is controlled by (12) before any Gaussian
approximation; the real endpoint-frequency strips are controlled by
(8). Equations (17),(20) therefore give an actual nonzero analytic
source amplitude for the remaining finite central phase problem

    Psi(z)+2pi i sum_i(P_i z_i^2-m_i z_i).               (21)

The comparison of its finite charges, its legitimate local saddle
contours, and the physical color complement are not replaced by
formal stationarity. In particular (20) alone is not a theorem for
an entire filled knot.

[Audit](../experiments/audit_actual_filling_source_fourier_endpoint_gap.py)
checks the exact finite-k normal-weighted decomposition, its retained
half-color source and endpoint split, the contour equality (4), and
the quantitative estimates on explicitly controlled analytic packets,
and the combined-source total derivative and exact paired-charge
Fourier selection in (10)--(11).
The actual mixed-source hypotheses are proved in the linked source
notes; finite tests alone do not establish them.
