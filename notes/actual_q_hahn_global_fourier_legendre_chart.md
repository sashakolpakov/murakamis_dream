# The physical selected Fourier action has a global Legendre chart

30 October 2026. The local action change
of [holomorphic Legendre transport](actual_q_hahn_holomorphic_fourier_legendre_transport.md)
is globally one-to-one on the full physical tube. This removes a possible
multiple-chart ambiguity for the selected classical action. It does not
provide analytic continuation of individual finite Fourier coefficients.

## 1. Statement

Fix 0<xi<=1/2 and the original marked selected action Phi_xi. Retain
all the source constants and logarithmic characters in the local theorem.
Write

    P={1/2<Re tau<1, 0<Re nu<Re tau},
    y=2pi i(nu-tau/2),
    F=J(xi)+(xi-1/2)y+Phi_xi(tau,nu)
                                      -i pi(tau-xi+xi^2)/2,
    lambda=F_y=xi-1/2+Phi_nu/(2pi i).               (1)

Let O be the image of P in (tau,y). Then

    (tau,y) -> (tau,lambda)                        (2)

is a biholomorphism from O onto its open image D_xi. In particular
the selected Legendre action F-lambda y is a SINGLE holomorphic
function on D_xi, with its original additive phase fixed by (1).
The image D_xi is not asserted convex, a product, or the whole
complex coefficient plane.

## 2. A source-selected square root is injective on each physical fiber

Fix tau. Put

    a=pi Re tau in (pi/2,pi), w=exp(y),
    c=-cos(pi tau), C=cos(pi xi), s=sin(pi xi),
    B(w)=w^2+2cw+C^2, V(w)=w^2+2cw+1.

The physical w-domain is exactly the sector

    S_tau={w!=0: |Arg w|<a}.                       (3)

The marked y-strip has imaginary width 2a<2pi, so exp maps that
strip bijectively onto (3). The full physical packet proves B and
V nonzero there. Therefore both roots alpha,beta of B belong to
the complementary closed cone

    K_tau={0} union {w!=0: |Arg(-w)|<=pi-a}.

This cone is convex: its angle is 2(pi-a)<pi. The whole segment
[alpha,beta] consequently misses S_tau. This conclusion also covers
xi=1/2, when one root is zero.

For distinct roots, the function

    r(w)=(w-alpha) sqrt((w-beta)/(w-alpha))          (4)

is holomorphic on C minus [alpha,beta], using the principal square
root in the displayed ratio. Indeed that ratio is a nonpositive
real number precisely on the removed segment. It satisfies

    r(w)^2=B(w), r(w)=w+c+O(1/w) at infinity.       (5)

The reflection R(w)=alpha+beta-w=-2c-w preserves the slit domain
and B. Thus r(R(w))/r(w) is a constant sign on its connected domain.
The asymptotic condition (5) fixes that sign to be minus:

    r(-2c-w)=-r(w).                               (6)

If r(w_1)=r(w_2), the equation B(w_1)=B(w_2) gives either
w_1=w_2 or w_2=-2c-w_1. The second alternative, by (6), would
force r(w_1)=0, impossible off the slit. Hence r is injective on
the slit complement, and in particular on S_tau. If alpha=beta,
the normalized root is simply r(w)=w+c and the same conclusion
is immediate.

The root in (4) is the ACTUAL selected source root. For real tau
and positive w it is the positive square root used to calibrate
the source. For any compact path in the allowed tau strip, a
sufficiently large positive w makes B(w)/w^2 uniformly close to
one. Its continuation remains the root with (5), so the same
calibration holds at the end of the path. Equality then extends
through the connected physical w-sector. No pointwise principal
square root of B is substituted for this continued root.

## 3. The selected momentum and action are globally single-chart

The actual selected source multiplier is

    Y=exp(Phi_nu)=(s+i r)^2/V=(s+i r)/(s-i r).      (7)

The last equality uses V=s^2+B. Its two factors do not vanish on
the physical domain because V is nonzero. Since s>0, the last
expression is an injective Möbius function of r. Equations (6),(7)
prove that Y is injective on each physical w-sector.

If two marked lambda values in (1) agree, their exponentials Y
agree. They therefore have the same w, and the marked strip then
gives the same y. The map (2) is thus globally injective. Its
Jacobian F_yy is everywhere nonzero by the local theorem. The
holomorphic inverse theorem supplies local holomorphic inverses;
injectivity makes them agree on overlaps. This proves the stated
biholomorphism onto D_xi and the single-valued Legendre action.

This is a global coordinate result for the ALREADY selected
ordinary action. It does not choose a different source sheet,
complexify the actual integer channel, or turn the coefficient
label into an available complex finite-source variable. The real
integer coefficient rate, exceptional block, partner normals and
global period questions keep the scopes of their separate theorems.

Focused audit: [reflection and momentum injectivity identities](../experiments/audit_actual_q_hahn_global_fourier_legendre_chart.py).

The chart is a global inverse onto its open image. It does not define finite complex-index coefficients or identify a contributing global-source cycle.