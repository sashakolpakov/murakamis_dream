# The original filling kernel is an exact centered Gaussian with a normal source

29 October 2026. The full original twist, including every projective
Casimir jet, is an exact centered Gaussian in the pair eigenlogarithm.
Its finite Fourier coefficients have an exact Poisson/Fresnel formula
with a retained INTEGER LINEAR charge weight. No coprimality or parity
restriction is needed. The representation gives actual nonzero local
Gaussian charge channels near real complete color for fixed |p|>=2.
It does not prove that their exterior pairing survives in a filled knot.

## 1. Full-Hermite Gaussian, not a value-only Gauss sum

Use the original N,d=N-1,q=exp(pi i/N),Q=q^2,
kappa=q^(d^2/2), and hbar=2pi i/N. The node eigenlogs are UNWRAPPED:

    x_k=pi i(2k+1)/N, w_k=exp(x_k), 0<=k<N.

For an integer P, the actual twist2P data in the
[complete Fourier-Hermite theorem](actual_twist_circle_fourier_kernel.md)
are h_k=nu_k^(2P), d_k=-P(d-2k)h_k. They satisfy EXACTLY

\[
 \boxed{h_k=\kappa^{-P}
       \exp\{P(x_k-\pi i)^2/\hbar\},\qquad
 d_k=\left.\partial_x\left[\kappa^{-P}
       e^{P(x-\pi i)^2/\hbar}\right]\right|_{x=x_k}.}   \tag{1}
\]

Indeed the derivative multiplier is P(2k+1-N), and expanding the
square gives precisely Q^(P k(k+1)). Its difference is a full
integer turn, not an omitted even-level sign. The centered square
is invariant under x->2pi i-x, so it has the compatible paired
values, opposite derivatives, and zero derivative at the odd
simple node x=pi i. Every original normal jet is present.

There is also a source-independent matrix form avoiding any sum
over auxiliary colors. The function

    K(z)=arccosh(-z/2)^2

has the branch analytic on C minus[2,infinity), with its removable
continuation at z=-2. On the nodes, K(c_k)=(x_k-pi i)^2.
The actual finite Casimir has all its eigenvalues below2. Full
holomorphic/Hermite functional calculus therefore gives

\[
 \boxed{R^{2P}=\kappa^P\exp\{P K(\Omega)/\hbar\}.}       \tag{2}
\]

This equality uses BOTH (1) conditions and the FULL polynomial
P_N=2T_N(z/2)+2. It is not an assertion that R is Euclidean
unitary; its nilpotent exponential is retained. For the filled odd
box the exact formula is

\[
 \mathscr R(R^{-(2p+1)})
   =\kappa^{-p}\mathscr R\{R^{-1}
                            e^{-pK(\Omega)/\hbar}\}.   \tag{3}
\]

The actual turn map mathscrR is linear, not multiplicative. Formula
(3) does not move the exponential through a turn as a new local
operator or discard a source-normal direction.

## 2. A coherent all-color finite Gaussian kernel

The exact marked transforms are

    H_n=N^(-1)sum_k h_k w_k^(-n),
    D_n=N^(-1)sum_k d_k w_k^(-n),
    a_n=[D_n+(N-n)H_n]/N, 0<=n<N.                     (4)

At n=0, D_0=0 so (4) includes a_0=H_0. These a are the actual
first-kind Chebyshev coefficients, not freely chosen Fourier
values. For an arbitrary original mixed-circle exterior A_j,
where A_j multiplies L_(j+1), put

    eta_n=(-1)^n(A_n-A_(n-2)), A_negative=0.

Then the FULL filling/source identity is

\[
 \kappa^{2P}\sum_{j=0}^{N-1}\beta_j A_j
  =\frac{\kappa^{2P}}{N^2}
     \sum_{n,k=0}^{N-1}h_kw_k^{-n}
         [N-n-P(d-2k)]\,\eta_n.                       \tag{5}
\]

It holds for scalar, Hilbert-valued or operator-valued exteriors
in their original order. Taking a difference on the exterior
retains the two finite color endpoints; no periodic substitute
for that finite difference is made.

For completeness the normal transform can be recovered coherently
from the value transform alone, with its compulsory full finite
Hilbert kernel:

\[
 D_n=-iP\sum_{m\ne n}\frac{H_m}{\sin(\pi(m-n)/N)}.
                                                               \tag{6}
\]

Derive this by the elementary DFT of k: its nonzero-frequency
coefficients are -1/(1-Q^(-l)), and its mean is d/2. That mean
cancels the -PdH_n term exactly. The matrix in (6) is Hermitian
and has norm |P|d. This does NOT allow one to discard D when H_n
vanishes at a particular color: it mixes all retained colors.

All gcd/parity behavior is already exact in (4). For P!=0 put
g=gcd(|P|,N), L=N/g. The value H_n is zero unless g divides n.
After that reduction it has modulus L^(-1/2) for odd L. For even
L it is zero unless

    (P-n)/g congruent to (P/g)L/2 modulo2,

and otherwise has modulus sqrt(2/L). These statements follow by
grouping the quadratic sum into g cosets and expanding its squared
modulus; the latter leaves only the shifts0, and L/2 if L is even.
They include L=1 by its trivial sum. Their PHASES remain the actual
finite Gaussian sum in (4); none is divided out as a nonzero
normalizer. For P=0, H_n=delta_(n,0),D_n=0, exactly.

In particular arithmetic zeros of the value Gauss sum do not
determine support of the full-Hermite filling kernel.

## 3. Exact finite-window Poisson representation and endpoint current

Set t_k=(k+1/2)/N. For P real integer define the entire finite
coefficient interpolation

\[
 a(n)=\frac{\kappa^{-P}}N\sum_{k=0}^{N-1}
 [2P(t_k-\tfrac12)+1-n/N]
 e^{2\pi i PN(t_k-1/2)^2-2\pi i n t_k}.                \tag{7}
\]

It is exactly (4) on the physical n=0,...,N-1. It is a specified
interpolation of the FILLING COEFFICIENT, not a new assertion about
an arbitrary nonintegral ordinary-color exterior.

Define

\[
 I_{P,N}(b)=\int_0^1
     e^{2\pi i PN(t-1/2)^2-2\pi i bt}\,dt,
 \quad
 J_{P,N}(n)=\frac{e^{\pi i PN/2}(1-e^{-2\pi i n})}{2\pi i N}.
\]

The all-N, all-parity exact formula is

\[
 \boxed{a(n)=\kappa^{-P}
   \sum_{\ell\in\mathbb Z}^{\mathrm{symmetric}}(-1)^\ell
        \{(\ell+1)I_{P,N}(n+N\ell)-J_{P,N}(n)\}.}       \tag{8}
\]

The SUM IS PAIRED symmetrically in ell. Each paired tail is
O(ell^(-2)) on compact n sets for fixed N,P; the series is then
locally uniformly convergent. The endpoint current J is essential
off the integer lattice. No unsupported absolute summation of its
constant pieces is intended.

Here is a direct proof. Apply midpoint Fourier sampling to the
periodic extension of the smooth finite-window integrand in (7).
Its Fourier coefficient at frequency N ell acquires (-1)^ell.
The periodic extension may jump at its endpoints, but its Fourier
series converges to each interior t_k. Its paired Fourier aliases
converge as stated, by two integrations by parts; their leading
odd1/ell terms cancel. In that coefficient put b=n+N ell.
The amplitude equals

    [2P(t-1/2)-b/N]+(ell+1).

The first bracket is the phase derivative divided by 2pi i N.
Its integrated endpoint is EXACTLY -J_(P,N)(n). This proves
(8) and specifies the original side current rather than assuming
it vanishes under a later complex-color deformation.

For physical INTEGER n, J=0 and (8) simplifies to

\[
 a_n=\kappa^{-P}\sum_\ell^{\mathrm{symmetric}}
                      (-1)^\ell(\ell+1)I_{P,N}(n+N\ell).
                                                               \tag{9}
\]

Thus the integer linear charge weight is exactly the retained
NORMAL data in (4), not an optional phase-space amplitude. In
particular ell=-1 is killed on the original integer color grid.
Off that grid its term is -J and may NOT be dropped. The zero
charge is therefore not deleted from a deformed source by fiat.

When P!=0, each integral in (8) is explicitly a finite Fresnel
difference. With b arbitrary complex,

\[
 I_{P,N}(b)=e^{-\pi i b-\pi i b^2/(2PN)}
   \int_{-1/2-b/(2PN)}^{1/2-b/(2PN)}e^{2\pi i PN v^2}\,dv.
                                                               \tag{10}
\]

The integration segment is the translated original interval,
and the integrand is entire. For P=0 use its elementary Fourier
integral instead. Thus no division by a Gauss sum or a coprimality
assumption has entered any formula.

## 4. Exact odd-filling operator and its classical charge equation

Put B_j=mathscrR(R^(-1)L_(j+1)), and
eta_n^B=(-1)^n(B_n-B_(n-2)), B_negative=0. Substituting
P=-p into (5),(9) gives an ALL-INPUT identity for the filled box:

\[
 \boxed{\mathscr R(R^{-(2p+1)})
  =\kappa^{-p}\sum_{n=0}^{N-1}\eta_n^B
      \sum_\ell^{\mathrm{symmetric}}(-1)^\ell(\ell+1)
                              I_{-p,N}(n+N\ell).}       \tag{11}
\]

All exteriors and original modified/peripheral factors are kept
when this is inserted in a diagram. Multiple boxes can be replaced
simultaneously before their original marked closure, by ordinary
linearity. Formula (11) is the coherent surgery kernel, rather than
an absolute sum over independently normalized circle invariants.

To state its local symbol precisely, let a=n/N, b/N=a+ell,
y=2pi i(t-1/2), mu=2pi i(a-1), and c=ell+1. Stationarity of
the Gaussian integral in (9) gives

\[
 2P y-\mu=2\pi i c.                                   \tag{12}
\]

For the actual negative odd filling, P=-p, this is
mu+2p y=-2pi i c. It is the canonical FULL-TWIST charge relation
with the half twist already in B_j. The exact physical auxiliary
color is j=n+1, whose squared-meridian log near completeness is
mu_phys=2pi i((n+1)/N-1)=mu+hbar. Thus the finite equation has
the corresponding retained Weyl shift, and (12) is its leading
classical form. Identifying y with a chosen topological longitude
also requires the actual peripheral chart, not an inference from
a classical A-polynomial alone.

For the actual low mixed pretzel core the sign can be checked
directly. Put H=Q^h for auxiliary color j=N-h. Its literal
coefficient has the identity

    a_(h,v)x^v/N^2=q^(h^2)F_(2v)/[F_v^2F_(v-h)F_(v+h)].

Thus its phase replaces 4Li2(X) by
2Li2(X)+Li2(X/H)+Li2(XH), and includes +(Log H)^2/2.
Differentiation at a regular internal saddle gives

    dG/dLogH=LogH+Log(1-X/H)-Log(1-HX)
            =Log[(H-X)/(1-HX)]=Log L_H,

with its continued integer mark. Here mu_phys=-LogH, rather than
LogH. In the circle kernel the factor (-1)^(j-1) cancels the
Gaussian linear action -pi i mu_phys, leaving

    (LogH-2pi i c)^2/(4p)

up to real constants for P=-p. Its combined stationary equation is
therefore LogH+2p LogL_H=2pi i c. This is a calculation from the
original factorial and normal-source phases. It still does not
assert the actual exterior contour selects that stationary point.

## 5. Exact first-order transport of the FULL filling coefficient

There is an additional useful source Ward identity for a(n).
Shifting the original periodic chirp index k->k+1 gives, on integer n,

\[
 H_{n-2P}=Q^{n-P}H_n,
\quad D_{n-2P}=Q^{n-P}(D_n-2P H_n+2Pq^{-n}).
\]

The boundary term 2P is the retained jump of the original LINEAR
normal weight at k=N-1. Substitution in (4) cancels the homogeneous
H terms and proves

\[
 \boxed{a(n-2P)=Q^{n-P}a(n)+\frac{2P}{N}q^{n-2P},
                                      \quad n\in\mathbb Z.}    \tag{12a}
\]

Outside 0<=n<N this uses the specified finite interpolation (7),
not an extension of missing Chebyshev coefficients by zero.
For complex n the EXACT retained current is

\[
 a(n-2P)-Q^{n-P}a(n)-\frac{2P}{N}q^{n-2P}
 =\frac{(e^{-2\pi i n}-1)q^{n-2P}}{N^2}
                       [N-n+P(N+1)].                  \tag{12b}
\]

Thus the physical coefficient recurrence is affine, not an illicit
homogeneous theta recurrence after complex-color deformation.

For P!=0, define g_n=q^(n^2/(2P))a_n, with the original log q.
Equation (12a) says

    g_(n-2P)-g_n=(2P/N)q^(n^2/(2P)-n).

Every physical coefficient packet is therefore a sum of at most
2|P| homogeneous quadratic chirps and explicit INCOMPLETE finite
quadratic sums. For instance along n_j=n_0+2Pj in the actual
window, j>=0,

\[
 a_{n_j}=q^{-n_j^2/(2P)}
 \left[q^{n_0^2/(2P)}a_{n_0}
      -\frac{2P}{N}\sum_{t=1}^j q^{n_t^2/(2P)-n_t}\right].
                                                               \tag{12c}
\]

The anchors are explicit finite Gaussian data (4), bounded by
1+|P|. No anchor is a knot period. Equation (12c), or the exact
Fresnel representation (8), supplies the endpoint function with
its actual source rather than approximating D by a Gaussian value.
Polynomially small errors in this endpoint function cannot simply
be discarded against an exponentially smaller filled rate.

## 6. The actual circle difference cancels its current and folds EXACTLY

The current J in (8) is periodic in n with period1. It therefore
cancels TERMWISE in the original circle-basis difference. Define
the canonical ENTIRE extension

    b_ext(j)=exp(pi i(j-1))[a(j-1)-a(j+1)],
    K_P(h)=b_ext(N-h).

The physical circle coefficient for color j is beta_(j-1).
For 1<=j<N it equals b_ext(j); for the last color,

\[
 \beta_{N-1}=\tfrac12 b_{\mathrm{ext}}(N).                   \tag{12d}
\]

The half is compulsory: the original aliases give a(N)=0 and
a(N+1)=-a(N-1), while the missing actual coefficient a_(N+1)
was extended by ZERO in the finite circle-basis conversion.

There is an exact ENTIRE Weyl symmetry, not only an equality on
the color lattice:

\[
 \boxed{K_P(h)=K_P(-h),\qquad h\in\mathbb C.}            \tag{12e}
\]

To prove it without discarding a current, put y_k=x_k-pi i and
use the finite Gaussian expression (7). Directly

\[
 K_P(h)=\frac{2(-1)^{N-1}}{N^2}\sum_k h_k e^{hy_k}
   [(h+2Py_k/\hbar)\sinh y_k+\cosh y_k].               \tag{12f}
\]

The k,d-k pair has y mapped to -y and h_k unchanged. Its sum
is even in h. The odd simple y=0 term is even as well. Equivalently,
the exact alias identities H(-n)=e^(2pi in)H(n),
D(-n)=-e^(2pi in)D(n), together with antiperiodicity at n+N,
give (12e), including its necessary exp(pi i(j-1)) factor.

For ANY even core exterior C_h=C_(-h), scalar or operator-valued,
and any integer H with 0<=H<N, the literal physical-color sum
therefore obeys

\[
 \boxed{\sum_{h=0}^H\beta_{N-h-1}C_h
       =\frac12\sum_{h=-H}^H K_P(h)C_h.}              \tag{12g}
\]

This keeps the physical half weight at h=0. In the actual pretzel
core, C_h is even on the physical grid by its finite Chebyshev
relation. Its symmetric finite-factorial continuation keeps the
pair F_(v-h)F_(v+h) and q^(h^2), and is even as well; a new
one-sided exp(pi i h) continuation must not be substituted for it.
Thus
the fold applies before the original marked closure and with
arbitrary spectator boxes. It iterates over several color ports.
The remaining high bands/aliases and any cutoff at +/-H remain
their actual source terms; (12g) makes no global tail assertion.

The current-inclusive Poisson formula becomes especially simple
for this folded kernel. With c=ell+1 and b=Nc-h,

\[
 K_P(h)=\kappa^{-P}e^{\pi i(N-h-1)}
       \sum_\ell^{\mathrm{symmetric}}(-1)^\ell c
                         [I_{P,N}(b-1)-I_{P,N}(b+1)].   \tag{12h}
\]

There is NO omitted J in this equation: J(j-1)=J(j+1) cancels
exactly for all complex j. The charge c=0 is thus truly absent
from the full circle kernel, even off lattice. This stronger
conclusion holds after the actual circle difference, not for an
individual a(n) in section3.

Reflection (h,c)->(-h,-c) preserves each paired contribution in
(12h). Indeed I(-b)=e^(2pi ib)I(b) by t->1-t; its factor
e^(-2pi ih) cancels the reflected prefactor and the two odd
signs cancel. Thus +/-charge folding keeps the EXACT endpoint
Fresnel functions too. The h=0 endpoint is removed by a genuine
whole-source identity, not by comparing two formal saddle heights.

## 7. An actual nonzero LOCAL Gaussian charge, and the remaining gate

Fix |P|>=2 and 0<=h/N<=delta<1/2, with physical
n=N-1-h. For each c=+1 or -1, the stationary point of the labeled
integral with ell=c-1 stays strictly inside [0,1], uniformly for
large N. The exact Fresnel integral therefore has

\[
 I_{P,N}(n+N\ell)=
 \frac{e^{i\,\operatorname{sgn}(P)\pi/4}}{\sqrt{2|P|N}}
  e^{-\pi i(n+N\ell)-\pi i(n+N\ell)^2/(2PN)}
                         +O_{P,\delta}(N^{-1}).        \tag{13}
\]

This follows by the elementary full real Gaussian integral and
one integration by parts on its two nonstationary omitted tails.
It is uniform and NONZERO for sufficiently large N. The original
normal charge factor c is nonzero on both channels. No unknown
cycle coefficient occurs INSIDE this labeled real Gaussian
integral. For P=0 or |P|=1, the exact formulas remain valid;
uniform endpoint asymptotics are not substituted for (13).

For the circle difference itself the corresponding leading charge
term is, with b=Nc-h and ell=c-1,

\[
 \frac{2i\kappa^{-P}e^{i\operatorname{sgn}(P)\pi/4}}
      {\sqrt{2|P|N}}
 (-1)^{(N+1)\ell}c\sin\frac{\pi b}{PN}
        \exp\{-\pi i(b^2+1)/(2PN)\}.                  \tag{13a}
\]

This follows by subtracting the two actual Gaussians at b-1,b+1.
Its c=+/-1 amplitudes are nonzero in a fixed sufficiently small
real complete-color corridor for |P|>=2. Under (h,c)->(-h,-c),
the sine and c both reverse and all remaining factors agree.
Thus the two geometric-charge halves ADD at h=0; the apparent
half-line endpoint is not an independent positive-height error.
One must still retain exact endpoint corrections until their
exterior pairing is estimated to the needed exponential accuracy.

This is a local source-channel result, not yet nonzero filled-knot
pairing. The complete sum in (11) retains all charges; arithmetic
Gauss cancellations can and do occur. A complex geometric color
deformation must retain the full current-inclusive kernel before
using the proved difference cancellation, all exterior/source data,
and its endpoint transport. Neither (13) nor the formal relation
(12) proves survival after that original exterior contraction.

The subsequent
[exact source Fourier estimate](actual_filling_source_fourier_endpoint_gap.md)
retains those endpoint currents and proves a uniform high-charge gap.
Combined with the original analytic mixed source it now yields
[nonzero survival of the entire truncated cusp-color sum](actual_pretzel_cusp_corridor_filling_survival.md)
for independently large fixed signed fillings. That theorem still
retains the complementary physical color region as an open whole-source
gate; it does not infer its absence from the local Gaussian above.

## 8. The wrapped normal current is an explicit original source

The endpoint function also has a finite operator Ward identity. It
identifies its forcing term without discarding it. Let f_P be the
degree-<N Casimir polynomial for r_N^(2P), so that
R^(2P)=kappa^(2P)f_P(Omega). Define a LINEAR map on Casimir
polynomials by

\[
 (\mathcal T f)(w+w^{-1})
   =f(Qw+Q^{-1}w^{-1})+f(Q^{-1}w+Qw^{-1}).             \tag{14}
\]

The symmetric Laurent expression is a polynomial: its constant
Chebyshev coefficient is doubled and its nth coefficient is
multiplied by Q^n+Q^(-n). Products on the following left side are
evaluated in the FULL Casimir algebra, with reduction modulo P_N
where necessary. Write rho=q-q^(-1). Then, for every integer P
and every N>=2,

\[
 \boxed{\mathcal T f_P(\Omega)
       -Q^P\,2T_{2P}(\Omega/2)f_P(\Omega)
    =\frac{2PN}{\rho}\,\Xi_0(\Omega)
    =2PN(-1)^N\rho\,p\ell.}                          \tag{15}
\]

Here T_(-n)=T_n and Xi_0 has value zero at every node, derivative
one at c_0=q+q^(-1), and derivative zero at the other double nodes.
The literal original cup and ordinary cap p,ell have precisely the
normalizations used throughout this note.

To prove (15), put G(x)=kappa^(-P)exp(P(x-pi i)^2/hbar).
Its exact shifts satisfy G(x+/-hbar)=Q^P exp(+/-2Px)G(x).
The interpolating Laurent polynomial g(x)=f_P(e^x+e^(-x)) has
the same value and x derivative as G at every original node x_k.
Consequently both sides of (15) have zero node values. All their
normal derivatives agree except when a shift crosses the original
logarithmic window. At x_0 the derivative defect is +2PN, and at
x_d it is -2PN; the shifted endpoint value is one in both cases.
Dividing by dc/dx=rho and -rho, respectively, gives the SAME
Casimir derivative 2PN/rho at the paired node c_0. At the odd simple
node no extra normal condition is imposed. Full Hermite uniqueness
proves the first equality, including even and composite levels.

For the second equality use the
[normalized original source observable](actual_adjacent_observable_source_filtration.md),
Xi_0=(-1)^N rho^2 p ell on the degree-d block. This identity extends
to the entire physical pair: both sides are Hopf intertwiners, and
the degree-d block generates the whole pair by the actual E/F
maps, as proved in the
[full pair commutant theorem](actual_pair_casimir_commutant_and_rotated_trace.md).
There is no unrecorded projector onto that block.

Most usefully, the exact endpoint forcing becomes a scalar when
placed in its ACTUAL odd-box turn. Indeed R^(-1)p=kappa^(-1)p
and the genuine unscaled turn obeys mathscrR(p ell)=I. Therefore

\[
 \boxed{\mathscr R\!\left[
 R^{-1}\{\mathcal T f_P-Q^P 2T_{2P}(\Omega/2)f_P\}\right]
       =2PN(-1)^N\rho\,\kappa^{-1}I.}                \tag{16}
\]

Its scalar modulus is at most 4pi|P|, uniformly in N. This is an
all-input original-source reduction, not just a formal critical
value statement. It can be inserted with arbitrary spectators in
this typed slot. In a composed source the displayed current removes
that box and leaves its explicitly known scalar factor.

Equations (15)--(16) do not bound the inverse Ward transport, nor
identify a general Fresnel endpoint remainder with this one term.
The map mathcalT is the specified linear Casimir q-shift, not a
physical gate that may be relocated through other boxes. A global
filled-knot estimate must still control the resulting actual source
and any iteration of this identity.

The [audit](../experiments/audit_actual_coherent_filling_gaussian_chirp.py)
tests original full physical signed twists and odd filled boxes,
all-node Gaussian values AND derivatives, finite Hilbert normal
data, gcd/parity selection, the current-inclusive Poisson/Fresnel
identity, the uniform nonzero labeled charge asymptotic, and the
full physical endpoint Ward (15) with its scalar turned source (16).
