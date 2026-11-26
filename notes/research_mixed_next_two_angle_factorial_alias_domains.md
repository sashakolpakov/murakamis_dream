# Zero-safe reflected aliases for the continued two-angle edge

Private written source calculation, 8 November 2026. No mathematical
numerical evaluation, saved-value calculation, or frozen-source edit
is used.

An exact integral describes the difference between the two reflected
factorial upper exponents, including every numerator zero and
negative-factorial cut. It pays the lower alias relative to the upper
profile for real outer angles, and also for outer angles in the upper
angular half-plane. For the positive lower outer half, the
first-quarter theorem supplies the retained comparison; copying it to
the entire reflected ray would be incorrect near its right endpoint.
No full edge or inner three-kernel packet is inferred.

## 1. The original finite interpolation and its real upper exponent

Use the unchanged complete kernel
\[
 K_N(t,u)=\sum_{j=0}^{N-1}
                  e_j(-2\cos t)e_j(-2\cos u)
\]
and the canonical interpolation from
[the exact factorial source](exact_factorial_interpolation_and_complex_contours.md)
and [the uniform factorial theorem, Sections 2--3](research_uniform_factorial_and_boundary_decay.md):
\[
 B_N(y,a)=
 \frac{N}{
 G_N(N(1/2-y+a/(2\pi))-1/2)
 G_N(N(1/2-y-a/(2\pi))-1/2)G_N(Ny)^2}.
 \tag{1}
\]
In particular \(B_N(j/N,a)=e_j(-2\cos a)\) for every original
physical index, and \(B_N(0,a)=1\) exactly. The unmarked Gamma
product has real coefficients under conjugation:
\[
 G_N(\overline z)=\overline{G_N(z)},\qquad
 B_N(\overline y,\overline a)=\overline{B_N(y,a)}.
 \tag{2}
\]
These are meromorphic identities, first obtained on the defining
strip from the positive-base powers and Gamma product, and then
continued by the exact shift relation.

Let
\[
 L(s,\sigma)=\Re J_{\rm side}(s+i\sigma),
 \qquad J'(z)=\Log(2\sin\pi z),\qquad J(0)=0,
 \tag{3}
\]
where a negative real argument uses the upper continuation for
\(\sigma>0\) and the lower continuation for \(\sigma<0\).
The real boundary values at \(\sigma=0\) agree.
Thus \(L(s,-\sigma)=L(s,\sigma)\). The original zero-safe upper
exponent of (1) is
\[
 \mathfrak b(y,a)=
 -\Re J_{\rm side}(1/2-y+a/(2\pi))
 -\Re J_{\rm side}(1/2-y-a/(2\pi))
 -2\Re J(y).
 \tag{4}
\]
On compact wire strips with real part strictly between zero and
one half, the uniform factorial theorem bounds (1) by
\(CN^{-1}e^{N\mathfrak b(y,a)}\).
Every reflected cosine term is retained in this upper bound.
In particular it is not an expansion obtained by deleting a
numerator zero.

## 2. An exact reflected comparison through the factorial cuts

Suppose \(a=\alpha-iH\), where
\[
 0\le\alpha\le\pi/2,\qquad H\ge0,\qquad 0<x<1/2,\qquad v\ge0.
\]
Put
\[
 p=\frac12-x+\frac{\alpha}{2\pi},\quad
 m=\frac12-x-\frac{\alpha}{2\pi},\quad h=\frac{H}{2\pi},
\]
\[
 D_a(x,v)=\mathfrak b(x-iv,a)-\mathfrak b(x+iv,a).
 \tag{5}
\]
Then the following formula is exact:
\[
 \boxed{\quad
 D_a(x,v)=
 \int_{|v-h|}^{v+h}
 \left\{\Arg\sin\pi(m+i\sigma)
                  -\Arg\sin\pi(p+i\sigma)\right\}\,d\sigma .
 \quad}
 \tag{6}
\]
The arguments in the integrand are their principal values for
\(\sigma>0\); the endpoint at zero is interpreted by its integrable
one-sided limit.

Indeed substitution in (4) gives
\[
 D_a=L(p,v+h)-L(p,v-h)-L(m,v+h)+L(m,v-h).
 \tag{7}
\]
Evenness of \(L\), and
\(\partial_\sigma L(s,\sigma)=-\Arg\sin\pi(s+i\sigma)\) for
\(\sigma>0\), prove (6). This includes \(m<0\): the upper
continuation satisfies \(J_+(z)=-J(-z)+i\pi z\), so its
derivative has exactly the indicated principal argument.

For \(\alpha,\sigma>0\), the integrand in (6) is strictly between
zero and \(\pi\). First,
\[
 \partial_s\Arg\sin\pi(s+i\sigma)
 =-\frac{\pi\sinh(2\pi\sigma)}
         {\cosh(2\pi\sigma)-\cos(2\pi s)}<0.
 \tag{8}
\]
Moreover
\[
 \Im\{\sin\pi(m+i\sigma)\,
                 \overline{\sin\pi(p+i\sigma)}\}
   =\cosh(\pi\sigma)\sinh(\pi\sigma)\sin\alpha>0.
 \tag{9}
\]
The continuous positive argument difference therefore belongs to
\((0,\pi)\); its limit as \(\sigma\) tends to infinity is
\(\alpha\). Consequently, when \(\alpha,H,v>0\),
\[
 \boxed{\qquad 0<D_a(x,v)<2\pi\min(v,h)\le2\pi v. \qquad}
 \tag{10}
\]
If \(\alpha=0\), \(H=0\), or \(v=0\), its value is zero.
Conjugation gives
\[
 D_{\alpha+iH}(x,v)=-D_{\alpha-iH}(x,v).
 \tag{11}
\]

In particular, if \(t\) is in the lower angular half-plane as
below and the outer angle \(u\) is real or in the upper angular
half-plane, with \(0\le\Re u\le\pi/2\), then
\[
 \mathfrak b(x-iv,t)+\mathfrak b(x-iv,u)-2\pi v
 <
 \mathfrak b(x+iv,t)+\mathfrak b(x+iv,u),\qquad v>0.
 \tag{12}
\]
This is a comparison of the original sidewise upper exponents.
It does not require one holomorphic phase across a moving
numerator zero. For real \(u\), the second factor cancels even
at the finite level by (2).

## 3. Numerator-zero placement on the actual cubic family

Let \(t=t(u)\) be the adopted original branch of
[the inner-three cubic theorem](research_mixed_next_inner_three_cubic_continuation.md)
on
\[
 \mathcal U=\{|\Re u|\le\pi/2,\ |\Im u|\le1/2\}.
\]
Restrict in this section to its positive lower outer half
\[
 \mathcal U_+=\{0\le\Re u\le\pi/2,\ -1/2\le\Im u\le0\}.
\]
Write \(t=a-iH_t\), and set
\[
 v_0=2\cos(t/2)=X+iY,\qquad
 A=\cos^2(t/2),\quad B=\cos^2(u/2),\quad
 W=\frac{AB}{A+B-AB}.
 \tag{13}
\]
The cubic theorem gives, with the original branches,
\[
 \frac32<X<\frac{15}{8},\quad
 \frac13<Y<\frac23,\quad
 0<a<\pi/2,\quad 0<H_t<1,
\]
\[
 \Re A>\frac12,\qquad \Im A>\frac14,\qquad
                    |A|<\frac{127}{144}<1.
 \tag{14}
\]

The
[first-quarter source theorem, Section 2](research_mixed_next_two_angle_bare_first_quarter_contour.md)
proves \(0<\arg W<\pi/2\), \(|W|<1\), and
\(0<\Re y_*<1/4\), where
\(y_*=\pi^{-1}\arctan\sqrt W\) is the original selected wire
saddle. In particular the denominator in (13) is nonzero.
The ray \(z=\sqrt W\,r\), \(r>0\), is the graph
\[
 y=x+ih_W(x),\qquad
 h_W(x)=\frac1{2\pi}
      \operatorname{arsinh}\{\tan(\tfrac12\arg W)\sin(2\pi x)\}.
 \tag{15}
\]
The relevant numerator zeros are
\[
 y_t=\frac12-\frac{t}{2\pi},\qquad
 y_u=\frac12-\frac{u}{2\pi},\qquad
 \tan(\pi y_t)=\cot(t/2),\quad
 \tan(\pi y_u)=\cot(u/2).
 \tag{16}
\]
The formula involving \(\cot(u/2)\) is used only when \(u\ne0\);
at \(u=0\) its zero is the wire half-endpoint itself.
The \(t\) zero is strictly above the ray (15).
To check this directly, \(\Im A>1/4\) implies
\[
                  \arg\frac{A}{1-A}>\frac{\pi}{4}.
 \tag{17}
\]
If the real part of this quotient is positive, its tangent is
\(\Im A/(\Re A-|A|^2)>4/3>1\), since
\(\Re A-|A|^2\le1/4-(\Im A)^2<3/16\).
Otherwise (17) is immediate.
The cubic inequality
\(\Re\tan(t/2)/[-\Im\tan(t/2)]>7/(8\sqrt2)\)
also gives
\[
              \arg\cot(t/2)<\pi/3.
 \tag{18}
\]
Indeed \(8\sqrt2/7<\sqrt3\).
For every \(u\in\mathcal U\),
\[
                         |\arg B|<1/2<\pi/6.
 \tag{19}
\]
One may use
\(|\arg B|\le2\arctan(\tanh(1/4))
=\arctan(\sinh(1/2))<1/2\).
Therefore \(A/[B(1-A)]\) lies strictly in the upper half-plane.
The exact identity
\[
 \frac{\cot^2(t/2)}W=1+\frac{A}{B(1-A)}
 \tag{20}
\]
and the principal angle ranges imply
\(\arg\cot(t/2)>\tfrac12\arg W\).
In particular the \(t\) zero is outside the region between
the upper ray and its reflection when \(u\in\mathcal U_+\).

The \(u\) zero has no corresponding universal placement.
For every real \(u\in(0,\pi/2]\), it is on the original real
wire interval, below the upper ray. Equations (1)--(7) retain
its exact reciprocal-factorial continuation rather than pretending
that this region is zero-free.

## 4. An actual right-end limitation of the reflected comparison

The first-quarter source theorem proves the reflected comparison
for all of \(\mathcal U_+\) when \(x<1/4\). It also keeps every
original weighted side, unweighted join, finite row and parity
in its exact source reduction. That comparison does not extend
to the whole reflected ray for every parameter in the same family.
For example fix
\[
                     u=\pi/3-i\epsilon,\qquad 0<\epsilon\le1/2.
 \tag{21}
\]
Both \(\cos t-1\) and \(\cos u-1\) have negative real and
positive imaginary parts. For the first this follows from
\(|A|<1\), \(\Im A>0\). For the second use
\(\cosh\epsilon<8/7\). Since \(h_W(x)\) tends to zero as
\(x\) tends to \(1/2\), the exact reflected difference satisfies
\[
 \lim_{x\uparrow1/2}
 \frac{D_t(x,h_W(x))+D_u(x,h_W(x))}{h_W(x)}
     =2\Arg(\cos t-1)+2\Arg(\cos u-1)>2\pi.
 \tag{22}
\]
This follows either by differentiating (4) at wire height zero,
where these angular arguments are nonzero, or directly from (6).
Thus the lower reflected rate minus its penalty exceeds the upper
rate on a sufficiently short right endpoint sector. This does not
show that either rate exceeds the selected action.

For clarity, the original zero-safe endpoint rates themselves are
\[
 \mathfrak b(0,t)+\mathfrak b(0,u)=0,\qquad
 \mathfrak b(1/2,t)+\mathfrak b(1/2,u)
                   =\frac{H_t+|\Im u|}{2}.
 \tag{23}
\]
At the half endpoint this follows from the two exact identities
for \(J_\pm(-z)\); their real boundary values agree at real \(u\).

Neither (22) nor the individual upper rate in (23) determines
the sign of the endpoint's deficit below \(\Re\psi(t,u)\).
The actual right real cut, physical right rows, and their
coherent closing observation need separate estimates or an exact
source reduction. This note supplies neither the global maximum
nor the intersection coefficient of a whole wire contour.
No full \(K_N(t,u)\) or inner three-kernel packet, and no lower
bound on an original signed contribution, is asserted here.
