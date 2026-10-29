# A finite Fourier packet resolves the original long-twist quadrature type

28 October 2026. This is a constructive extension of the
[source-preserving inner quadrature](source_preserving_inner_quadrature.md).
It keeps the original finite lattice values, the original endpoints and
an explicit convergent remainder. A long twist requires more Fourier
modes, not an unproved deletion of its endpoint source.

The theorem below removes the vertical-type obstruction for every fixed
literal twist length. The remaining geometric selection is among a finite
mode family. It does not assert that the geometric mode dominates all
others in an arbitrary knot.

## 1. Exact finite-mode Abel--Plana

Let n be a positive integer and f holomorphic in a neighborhood of the
closed strip 0<=Re z<=n. Suppose, uniformly there,

    |f(x+it)| <= C exp(pi tau |t|),

where tau<2(K+1) and K is a nonnegative integer. Polynomial factors in
|t| are also allowed if the inequality has any fixed strict margin.
Then

    sum_(j=0)^n f(j)
       =(f(0)+f(n))/2
        +sum_(k=-K)^K integral_0^n f(x) exp(2pi i k x) dx
        +R_K(f),                                             (1)

    R_K(f)=i integral_0^infinity exp(-2pi Kt)
       [f(it)-f(-it)-f(n+it)+f(n-it)]
                      /(exp(2pi t)-1) dt.                    (2)

The integral at zero is interpreted by its removable continuous value;
the numerator vanishes there. At infinity it is absolutely convergent.

Here is a direct residue proof, rather than an assumption that Poisson
modes may be discarded. Use the upper and lower kernels

    U_K(z)=exp(2pi i Kz)/(exp(-2pi iz)-1),
    L_K(z)=exp(-2pi i Kz)/(exp(2pi iz)-1).

Their residues at integers are the same as for K=0. Their vertical
damping is 2pi(K+1). For w=exp(2pi iz), their boundary sum is exactly

    U_K(z)+L_K(z)=-sum_(k=-K)^K w^k.

Integrating the two rectangular contours, with half-circles at the
endpoints, gives (1). The horizontal edges vanish by the stated strict
growth inequality. The two vertical edges are exactly (2), with the
same signs as ordinary finite Abel--Plana. This proves the full finite
source identity. Taking K=0 recovers the previous theorem.

One may also take unequal upper/lower cutoffs K_+,K_-; the mode range
is -K_-<=k<=K_+, and the two differences in (2) are weighted by
exp(-2pi K_+t), exp(-2pi K_-t), respectively. Thus an asymmetric
kernel or a specified integer lattice gauge need not be artificially
symmetrized.

## 2. A quantitative endpoint remainder

Suppose the four endpoint values satisfy

    |f(a+it)| <= A exp(pi tau |t|), a=0,n,
    |f'(a+it)| <= A B, |t|<=1.

Put gamma=2(K+1)-tau>0. Splitting (2) at t=1 gives

    |R_K(f)| <= C A [B+1/gamma],                            (3)

with an absolute constant C. Near zero the numerator is O(ABt),
and the denominator is at least 2pi t. At infinity its absolute
value is at most C A exp(-pi gamma t).

For every T>=1 the omitted t>=T part is bounded by

    C A gamma^(-1) exp(-pi gamma T).                        (4)

Thus when A has a known smaller exponential rate than the main
geometric period, the entire finite-mode correction has that same
smaller rate up to polynomial factors. This is the same kind of
source comparison as the original 5_2 error bound by K_(4_1),N.
No rate for A is inferred merely from the existence of the main saddle.

For the reflected factorial kernels in Section 5 of the earlier
quadrature theorem, tau is bounded in terms of the displayed Gaussian
coefficient and linear exponent. A finite K therefore exists even
when its former single-mode inequality fails. Their original
endpoint derivative bound has B=O(1+log N). This is a verifiable
local kernel criterion; no contour or geometric coupling is assumed.

## 3. Application to EVERY literal p-fold crossing sector

The [exact original-matrix calculation](general_bridge_quadrature_and_twist_type_obstruction.md)
gives, after the specified external Cartan line, the literal relative
degree-zero values

    d_j^p, d_j=(-1)^j Q^(j(j+1)/2), 0<=j<N,

for every integer twist length p. Set n=N-1 and use their exact
entire interpolation

    B(z)=exp[pi i p z(z-n)/N].

For every 0<=x<=n,

    |B(x+it)| <= exp(pi c |t|), c=|p|n/N.

The smallest symmetric cutoff satisfying the strict contour-decay
criterion is

    K_min=floor(c/2).                                       (5)

It has at most |p|+1 modes and is bounded independently of N for
fixed p. The resulting remainder is polynomially bounded in N.
For a margin uniform over ALL levels use instead

    K=floor(|p|/2), gamma=2(K+1)-c>=1.                      (6)

The exact endpoint numerator gives the particularly transparent formula

    sum_(j=0)^n d_j^p
       =1+sum_(k=-K)^K integral_0^n
          exp[pi i p x(x-n)/N+2pi i kx] dx
        +4i integral_0^infinity
          exp(-pi i p t^2/N) sinh(pi p n t/N)
                   exp(-2pi Kt)/(exp(2pi t)-1) dt.           (7)

No endpoint or parity factor is omitted. For p=0 the original sum
is N and (1) with K=0 gives it exactly. For p!=0 the correction in
(7) satisfies the explicit bound

    |R_K| <= (4c/pi) sum_(r=K+1)^infinity 1/(4r^2-c^2).     (8)

This follows by expanding the positive denominator and integrating
the absolute sinh bound; strict 2(K+1)>c justifies Tonelli.
For K in (6), (8) is O_p(1), uniformly in N. For the minimal
cutoff (5) it is O_p(N): gamma is a positive rational with
denominator N, hence gamma>=1/N. Near t=0, B'=O_p(1), so (3)
gives the same polynomial conclusion directly.

With the uniform cutoff (6), taking T=eta N in (4) leaves an
O_p(exp(-pi eta N)) far tail. The low Fourier modes in (7) are
kept exactly; they have not been put in that error. Their number
depends on p and not on the quantum level. Each is an ordinary
finite Gaussian integral, so for p!=0 equation (7) also directly bounds the whole
clock sum by O_p(sqrt N) using the elementary Fresnel bound,
plus its O_p(1) correction.

The analogous formula with a different original linear lattice
gauge simply shifts the retained finite mode window. There is no
freedom to call one of its modes the original selected state
without carrying the other modes and (2).

### 3.1 The entire marked Gaussian kernel, not only its constant argument

The source-preserving extension needed for an actual word keeps a
spectral argument and the meridian. The original finite Gaussian
polynomial is exactly

    Gamma_(p,N)(t,M)=sum_(j=0)^(N-1) d_j(M)^p t^j,
    d_j(M)=(-1)^j Q^(j(j+1)/2) M^(-2j).

Choose a specified logarithm L of Z=t M^(-2p) and put

    f(z)=B(z) exp(Lz).

This has the literal marked Gaussian coefficients at every integer.
On compact annuli for t,M and any fixed bounded logarithmic branch,

    |f(a+is)| <= A exp(pi tau |s|), a=0,n,
    A=max(1,|Z|^n), tau=|p|n/N+|Im L|/pi.                   (9)

The same bound holds uniformly over 0<=Re z<=n. The endpoint
derivative bound is A times a constant depending on p and the
specified compact logarithmic chart, independently of N. Hence
(1)--(4), with a finite cutoff depending only on that chart and p,
give an EXACT finite-mode presentation of the entire original
Gamma_(p,N)(t,M), including its endpoint terms and remainder.
For |Arg Z|<=pi the simple choice K=floor((|p|+1)/2) has a
uniform positive type margin. A change L->L+2pi i ell is exactly
a shift of the Fourier mode labels; the scalar polynomial is unchanged.

This has an immediate whole-network consequence. In
[the original Cauchy network](actual_euler_gaussian_cauchy_network.md),
each Gaussian factor is literally Gamma_(+1,N)(z/w,M) or its
negative-sign counterpart. Replace each by its exact expression (1).
On the specified compact Cauchy circles its logarithmic arguments
range over finitely many bounded branch charts, with transition by the
just stated exact relabeling. More explicitly, partition each circle's
parameterization into finitely many arcs carrying continuous logarithmic
lifts; alternatively carry its unwrapped mark throughout. No global
single-valued Log is assumed on a full circle, and individual mode
integrals are not identified across marks. Their combined formula is
the same original polynomial. Formula (9) gives absolute uniform
integrability of the endpoint remainder. Fubini therefore carries this
replacement through the complete original cap, pivot and external
normalization. No source coupon is changed. This yields a finite
Fourier-packet presentation for the Gaussian part of EVERY fixed
original braid word. The packet size is independent of N. All its
factorial/Euler and projection factors remain the same exact functions;
no exponential bound for their contracted endpoint periods is asserted.

## 4. The resulting generalization target

This resolves the specific long-twist vertical-type failure: every
fixed p has a finite, explicitly sourced mode packet, including
arbitrarily large positive or negative twists. The same theorem
applies to each reflected finite-factorial bridge kernel with a
known finite vertical type. It does not require p=1 or a twist-knot
diagram.

For many bridges, this produces finitely many mode combinations
for each fixed word, together with endpoint faces and corners.
Iterating it requires its uniform strip estimates at the actual
intermediate parameters; after an earlier integration those may be
complex, so the original finite-product reflection must be checked
again. The original word is not automatically a product of independent
one-variable kernels. The general finite-height residue construction
remains available when an infinite-height strip is not justified.

A broad knot theorem still needs a structural way to prove that the
actual endpoint periods and the other retained modes have smaller
rate, and that the geometric mode has nonzero original coefficient.
The present result replaces an invalid one-mode shortcut by a
concrete finite-dimensional selection problem. It does not solve
that remaining selection by asserting an assumed geometric contour.

[Exact finite-packet diagnostics](../experiments/audit_twist_vertical_type_obstruction.py).
