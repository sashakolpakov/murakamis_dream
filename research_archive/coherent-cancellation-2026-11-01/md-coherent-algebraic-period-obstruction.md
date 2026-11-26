# Algebraicity and the known volume budget do not imply the cancellation inequality

This note tests a proposed implication, not a knot invariant. The original
source has an algebraic boundary phase, a positive root distribution,
and a normalized logarithmic period. Those properties are valuable, but
they do not by themselves compare the signed boundary value with the
restored complete action. The example below also satisfies a strict
version of the known one-cap pyramid budget. It therefore goes beyond
the earlier example using an atomic root distribution with an unbounded
restoration deficit.

Every formula below belongs to an abstract binary polynomial model. No
matched triangulation, original coefficient extraction, group
representation, or Kashaev invariant is constructed. The example cannot
refute a theorem that retains those additional data.

## 1. The comparison being tested

For a probability measure \(\mu\) on \((0,1)\), define the normalized
pressure on the slit plane \(\mathbb C\setminus(-\infty,0]\) by

\[
 f(w)=\int\log(1-p+pw)\,d\mu(p),\qquad f(1)=0.
\]

The logarithm continues from positive \(w\). Write

\[
 m(w)=w f'(w),\qquad B(w)=\exp(2\pi i m(w)).
\]

The source comparison in the algebraic-boundary note would require

\[
 \sup_{r>0}\{\operatorname{Re}f(-r+i0)-\log_+r\}
 \le \inf_{w>0}\{f(w)+q(\log w)-\log w\},
 \qquad
 q(z)=\frac2\pi\operatorname{Ti}_2(e^{z/2}),
\]

where
\(\operatorname{Ti}_2(x)=\int_0^x\arctan(t)\,dt/t\).
Define the negative of the left supremum to be \(\chi\), and the
negative of the right infimum to be \(D\). Thus the desired comparison
is \(\chi\ge D\). The symbol \(D\) here is a scalar deficit, not a
diagram. We do not call the right side a hyperbolic volume.

## 2. An explicit algebraic phase with a continuous root measure

For \(a>0\), put

\[
 m_a(w)=\frac2\pi\arctan\sqrt{w/a},\qquad
 f_a(w)=\frac4\pi\left[
 \operatorname{Ti}_2\bigl(\sqrt{w/a}\bigr)
 -\operatorname{Ti}_2(a^{-1/2})\right].
\]

Use the square root positive on the positive axis and continue its
arctangent from there. Direct differentiation gives
\(w f_a'(w)=m_a(w)\). Its Stieltjes representation is

\[
 m_a(w)=\int_0^\infty\frac{w}{w+r}\rho_a(r)\,dr,
 \qquad
 \rho_a(r)=\frac1{\pi^2r}
 \log\left|\frac{\sqrt a+\sqrt r}{\sqrt a-\sqrt r}\right|.
\]

Here \(\rho_a\) is positive, integrable, and has total mass one.
For a direct derivation, apply the Cauchy formula on a slit contour to
\(m_a(w)/w\). The upper boundary value of \(m_a\) has imaginary part
\(\pi^{-1}\log| (\sqrt a+\sqrt r)/(\sqrt a-\sqrt r)|\).
The jump of \(m_a(w)/w\) is therefore the displayed density. The small
circle at zero contributes zero because \(m_a(w)/w=O(|w|^{-1/2})\);
the large circle contributes zero after multiplication by the Cauchy
kernel. The logarithmic singularity at \(-a\) is integrable, so its
small indentation also disappears. Finally, monotone convergence as
\(w\to+\infty\) gives total mass one, since \(m_a(w)\to1\).

Push this measure to \(p=(1+r)^{-1}\). Integration of the derivative
identity, with normalization at \(w=1\), gives exactly the pressure
integral in section 1. There are no atoms, including at the endpoints.
The density is real analytic except for its logarithmic singularity;
at zero and infinity it is respectively \(O(r^{-1/2})\) and
\(O(r^{-3/2})\). Both logarithmic endpoint moments are finite.

Set

\[
 \varepsilon=\frac1{16},\qquad
 f=\frac13f_{\varepsilon^2}+\frac23f_{\varepsilon^{-2}},
 \qquad m=\frac13m_{\varepsilon^2}+\frac23m_{\varepsilon^{-2}}.
\]

The associated probability measure is the same convex combination.
If
\(b_a(w)=(1+i\sqrt{w/a})/(1-i\sqrt{w/a})\), then

\[
 B(w)^3=b_{\varepsilon^2}(w)^2
              b_{\varepsilon^{-2}}(w)^4.
\]

For an explicit rational eliminant, put

\[
 P(t,B)=B^3(1-16it)^2(16-it)^4
                -(1+16it)^2(16+it)^4.
\]

The product \(P(t,B)P(-t,B)\) is even in \(t\) and has rational
coefficients. Substitution of \(t^2=w\) gives a polynomial over
\(\mathbb Q\) satisfied by \(B(w)\). Its leading coefficient in
\(B^6\) is \((1+256w)^2(256+w)^4\), so it is nonzero.
The selected branch is regular along the positive
axis, since \(B\ne0\) and the derivative in \(B\) of its cubic
equation is nonzero there. The actual branch is selected by
\(B=\exp(2\pi i m)\), not by independently choosing cubic roots.

Moreover \(m(0+)=0\), \(m(+\infty)=1\), and the imaginary part of
\(m\) is positive in the upper half-plane. Hence \(0<|B|<1\) there.
The root measure has the same density relation

\[
 \rho(r)=-\frac{\log|B(-r+i0)|}{2\pi^2r}
\]

as the original algebraic-pressure construction. Its two interior
exceptional points are \(\varepsilon^2\) and \(\varepsilon^{-2}\).

## 3. Positive response and a selected algebraic critical point

Write \(z=\log w\). The initial mean and response are

\[
 \nu=m(1)=\frac13+\frac2{3\pi}\arctan\frac1{16},\qquad
 \kappa=\left.\frac{d}{dz}m(e^z)\right|_{z=0}
       =\frac{16}{257\pi}.
\]

In particular \(1/4<\nu<1/2\), \(\kappa>0\), and
\(\kappa\le\nu(1-\nu)\). More generally, each component response is

\[
 \kappa_a(z)=\frac{\sqrt{e^z/a}}{\pi(1+e^z/a)},\qquad
 \left|\frac{d}{dz}\log\kappa_a(z)\right|\le\frac12.
\]

The positive mixture therefore satisfies
\(e^{-|s|/2}\kappa(z)\le\kappa(z+s)\le
e^{|s|/2}\kappa(z)\). This is stronger than the exponential response
comparison used in the existing Dirichlet estimate.

Let \(V(z)=f(e^z)+q(z)-z\). Then

\[
 V'(z)=m(e^z)+\frac1\pi\arctan(e^{z/2})-1,
 \qquad V''(z)>0.
\]

Its derivative tends to \(-1\) and \(1/2\) at the two ends. There is
one finite minimum. If its positive coordinate is \(w_*\), then

\[
 B(w_*)\frac{1+i\sqrt{w_*}}{1-i\sqrt{w_*}}=1,
 \qquad m(w_*)+\frac1\pi\arctan\sqrt{w_*}=1.
\]

The second equation retains the logarithmic lift. Conversely the first
equation on the selected positive branch forces that lift, since the
sum lies strictly between zero and \(3/2\). The minimum is isolated,
so \(w_*\) is algebraic. There is also an exactly normalized period:

\[
 -D=V(\log w_*)=q(0)+
 \int_1^{w_*}\left[m(w)+\frac1\pi\arctan\sqrt w-1\right]
                         \frac{dw}{w}.
\]

The additive constant and the continuous logarithmic branch are fixed.
Neither the algebraic point nor this period guarantees the comparison
with the negative-axis supremum.

## 4. The negative-axis supremum is explicit

Analytic continuation of the arctangent gives

\[
 \operatorname{Re}f_a(-r+i0)
  =\log_+(r/a)-\frac4\pi\operatorname{Ti}_2(a^{-1/2}).
\]

For example, differentiate this boundary value in \(\log r\): its
derivative is zero for \(r<a\) and one for \(r>a\). Its value at
zero is fixed by the displayed definition of \(f_a\), and continuity
at \(r=a\) fixes the second interval. The identity
\(\operatorname{Ti}_2(x)-\operatorname{Ti}_2(x^{-1})
=(\pi/2)\log x\) follows by differentiation and its value at one.

Put \(L=\log256\), \(s=\log r\), and
\(C=(4/\pi)\operatorname{Ti}_2(1/16)\). The objective on the
negative axis becomes

\[
 \frac13(s+L)_++\frac23(s-L)_+-s_+-\frac L3-C.
\]

Its slopes on the four successive intervals are \(0,1/3,-2/3,0\).
The maximum is therefore \(-C\), attained at \(s=0\). Consequently

\[
 \chi=C<\frac2{25}.
\]

The strict bound follows already from
\(\operatorname{Ti}_2(1/16)<1/16\) and \(\pi>25/8\).

## 5. Rational bounds for the deficit and the geometric budget

Put \(t=e^{z/2}\). For \(1<t<16\), the inversion identity gives

\[
 V(2\log t)=-\frac13\log t+
 \frac4{3\pi}\operatorname{Ti}_2\!\left(\frac1{16t}\right)
 +\frac8{3\pi}\operatorname{Ti}_2\!\left(\frac t{16}\right)
 +\frac2\pi\operatorname{Ti}_2\!\left(\frac1t\right)-C,
\]

\[
 V'(2\log t)=-\frac16+
 \frac{4\arctan(t/16)-2\arctan(1/(16t))-3\arctan(1/t)}{3\pi}.
\]

The accompanying rational interval calculation proves

\[
 -\frac{277}{1000}<V(2\log8)<-\frac{276}{1000},\qquad
 -\frac{12}{1000}<V'(2\log8)<-\frac{11}{1000},\qquad
 V'(2\log9)>0.
\]

Convexity puts the minimum between these two arguments. Its supporting
line at \(2\log8\), together with \(2\log(9/8)<1/4\), gives
\(\min V>-277/1000-(12/1000)/4=-28/100\).
Evaluation at \(2\log8\) gives the other side. Hence

\[
 \boxed{\quad \frac{27}{100}<D<\frac{28}{100},\qquad
                 \chi<\frac2{25},\qquad D-\chi>\frac{19}{100}.\quad}
\]

The desired cancellation comparison is false by a fixed margin.

The scalar pyramid budget in the original geometric construction is

\[
 W(\nu)=2\int_0^\alpha\operatorname{arsinh}(\cos t)\,dt,
 \qquad \alpha=\arcsin(\sqrt2\cos\pi\nu).
\]

Our model satisfies this budget with a strict margin. Indeed
\(\pi\nu=\pi/3+(2/3)\arctan(1/16)<\pi/3+1/24\). The elementary
Taylor bounds and \(\sqrt3<7/4\), \(\sqrt2>7/5\) give

\[
 \sqrt2\cos\pi\nu>
 \frac75\left(\frac12-\frac1{2304}-\frac7{192}\right)
 >\frac7{10}-\frac{(7/10)^3}{6}+\frac{(7/10)^5}{120}
 \ge\sin\frac7{10}.
\]

Thus \(\alpha>7/10\). On \([0,7/10]\),
\(\cos t\ge1-t^2/2>3/4\). Using
\(\operatorname{arsinh}(3/4)=\log2>2/3\) and \(\pi<22/7\),

\[
 \frac{W(\nu)}\pi>
 \frac7{5\pi}\log2>\frac{49}{165}
 >\frac{28}{100}+\frac1{100}>D+\frac1{100}.
\]

In particular the example obeys a bound of the form
\(D<W(\nu)/\pi-g/(2\pi)\) with \(g=\pi/50>0\).
This is the same form as the known strict geometric budget; it is not
a realization of its underlying group representation.

The checker uses the alternating series for \(\arctan x\) and
\(\operatorname{Ti}_2(x)\) at rational \(0<x<1\), with the first
omitted term bounding the error. It uses
\(\pi=16\arctan(1/5)-4\arctan(1/239)\), and the positive series
\(\log x=2\sum_{k\ge0}y^{2k+1}/(2k+1)\),
\(y=(x-1)/(x+1)\), with a geometric upper bound for its tail.
All comparisons are rational; decimal evaluations are unnecessary.

## 6. Stable polynomial realization and exact scope

Choose empirical measures of \(d\) points in \((0,1)\) converging
weakly to \(\mu\); the points may be rational. Define

\[
 P_d(A,C)=\prod_{j=1}^d[(1-p_{d,j})C+p_{d,j}A].
\]

These are homogeneous real-stable polynomials with rational positive
coefficients, every degree from zero to \(d\) present, and
\(P_d(1,1)=1\). Their normalized logarithms converge to \(f(w)\)
locally uniformly on the slit plane. To see this directly, on a compact
subset the kernels \(\log(1-p+pw)\) and all fixed derivatives are
uniformly continuous and bounded in \(p\in[0,1]\); a finite net
upgrades weak convergence to uniform convergence. The same argument
gives all fixed local pressure derivatives.

This realization establishes the pressure, not an unproved
pointwise asymptotic at every negative-axis zero. The failed inequality
above concerns the continuous limiting pressure and its boundary
values; its exact computation does not need such an extrapolation.

The example retains algebraicity over a rational ground field, the
selected logarithmic lift, an atom-free root measure, endpoint limits,
positive response, a strong response-transport estimate, an isolated
positive algebraic critical point, and a strict pyramid budget.
These properties alone cannot prove the missing inequality. A proof
for original knots must use further information from their actual
triangular incidence, coefficient constraints, or representation
and cycle structure. None of those data is replaced by this example.
