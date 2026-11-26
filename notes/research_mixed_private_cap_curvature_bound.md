# A stronger cap curvature on the actual private-height rectangle

Research deduction, 6 November 2026. The canonical complete-boundary
action has a stronger real curvature on the private-coordinate
rectangle now known to contain every factorial-branch maximizer
during the first-height reset. The proof is analytic and preserves
the original endpoint branch. It does not bound the full effective
curvature of the four-variable optimization or any omitted finite
current.

## 1. Domain and canonical square root

Let \(S(e)\) be the original complete endpoint critical action and set
\[
 \mathcal E_0=[3/10,2/5]+i[-51/1000,-19/1000],
 \qquad p=\cot\pi e=a+ib,\qquad \sigma=-S''(e)/\pi.
 \tag{1}
\]
The [whole-reset optimizer argument](research_mixed_selected_boundary_height_envelope.md),
Section 12, puts the factorial maximizer's private coordinate strictly
inside these real bounds, at its unchanged actual private height.
The statement below concerns the entire closed rectangle (1), not
only points found by optimization.

The canonical identity in
[the pair-curvature composition proof](research_mixed_pair_curvature_composition.md)
is
\[
 \sigma=p+\frac{2(p-i)}R,\qquad R^2=E(2-E),\quad
 E=e^{-2\pi ie}.
 \tag{2}
\]
Here \(R\) is the root specified by the original endpoint parameter,
not an arbitrary choice of square root.
On (1) it has positive real part and negative imaginary part.
To verify this branch statement, \(E\) has negative real and
imaginary parts, so
\(\Im(E(2-E))=2\Im E(1-\Re E)<0\).
The original root is identified with the principal lower-half-plane
square root on the edge \(\Re e=.3\) by the explicit calculation
in Section 9 of the height-envelope proof:
\(R=iE\sqrt{1-2/E}\), with the square root in the canonical
\(u_c(e)\) formula. Both roots continue without a zero on the
connected rectangle, so the same identification holds throughout it.

Put \(T=R(p+i)\). Since \(p+i\) has positive real and
imaginary parts, \(\arg T\in(-\pi/2,\pi/2)\).
Moreover
\[
 T^2=(p+i)^2+4,\qquad
 \Im(T^2)=2a(1+b)>0.
\]
Consequently \(T\) is the square root with positive real and
imaginary parts. Equation (2) becomes
\[
 \boxed{\displaystyle
  \sigma=F(p):=p+\frac{2(p^2+1)}{\sqrt{(p+i)^2+4}}.}
 \tag{3}
\]
No logarithmic lift or endpoint solution has changed.

## 2. A rational rectangle for the private cotangent

On (1),
\[
                    \frac3{10}<a<\frac34,\qquad
                    0<b<\frac14 .
 \tag{4}
\]
Here are explicit elementary bounds. Write
\(\theta=2\pi\Re e\in[.6\pi,.8\pi]\) and
\(\nu=-2\pi\Im e\in[.038\pi,.102\pi]\).
The exact cotangent formula is
\[
 a=\frac{\sin\theta}{\cosh\nu-\cos\theta},\qquad
 b=\frac{\sinh\nu}{\cosh\nu-\cos\theta}.
 \tag{5}
\]
Its first numerator is greater than \(7/12\): indeed
\(\sin(\pi/5)>\sin(5/8)>1795/3072>7/12\).
The denominator is less than
\(53/50+81/100=187/100\). Thus
\(a>175/561>3/10\).
For the upper bound, \(a\le\cot(.3\pi)=\tan(\pi/5)<3/4\);
the last assertion follows from
\(\tan^2(\pi/5)=5-2\sqrt5<9/16\).

Because \(\cos\theta<0\), the second ratio in (5) increases
with \(\nu\) and decreases with \(\theta\).
Its maximum is at \(\nu=.102\pi,\theta=.6\pi\).
At that point
\[
 \sinh(.102\pi)<1/3,\qquad
 \cosh(.102\pi)>21/20,\qquad \cos(.4\pi)>3/10,
\]
so \(b<(1/3)/(27/20)=20/81<1/4\).

These constants require no numerical enclosure. Use
\(25/8<157/50<\pi<22/7\), \(.102\pi<9/28\), and
\[
 \begin{split}
 \cosh x&\le1+\frac{x^2}{2}
       +\frac{x^4}{24(1-x^2/30)},\\
 \sinh x&\le x+\frac{x^3}{6(1-x^2/20)}
 \end{split}
 \tag{6}
\]
at \(x=9/28\) to obtain respectively \(53/50\) and \(1/3\)
as strict upper bounds. The lower bound
\(.102\pi>8/25\) gives
\(\cosh(.102\pi)>1+32/625>21/20\).
The exact values of \(\cos(\pi/5)\) and \(\cos(2\pi/5)\),
with \(11/5<\sqrt5<56/25\), give the other rational
cosine bounds. The cubic sine lower bound proves the displayed
inequality at \(5/8\).

## 3. Monotonicity of the canonical curvature

Regard the expression \(F\) in (3) on the larger closed rectangle
\[
             3/10\le a\le3/4,\qquad 0\le b\le1/4.
 \tag{7}
\]
Its square root is analytic there, with positive real and imaginary
parts. Write \(q=1+b\), \(t=a^2\), and
\[
 \begin{gathered}
 T^2=A+iB,\qquad A=t-q^2+4,\quad B=2aq,\\
 N=(p+i)^3+8(p+i)-8i,\\
 N_R=a(t-3q^2+8)>0,\qquad
 N_I=3tq-q^3+8q-8,\\
 F'(p)=1+\frac{2N}{T^3}.
 \end{gathered}
 \tag{8}
\]
In this rectangle \(A>5/2\), \(0<B\le15/8\), so
\(\theta=\arg(T^2)\) lies in \((0,\pi/4)\).
Direct multiplication gives
\[
 \begin{split}
 N_I A-\tfrac32 B N_R
 &=t(5q^3-4q-8)+q^5-12q^3+8q^2+32q-32\\
 &\le-\frac{4527}{25600}<0.
 \end{split}
 \tag{9}
\]
To verify the uniform last bound, the coefficient
\(C(q)=5q^3-4q-8\) increases on \([1,5/4]\) and is
at most \(-207/64<0\). The derivative of the remaining
polynomial is positive, since
\[
 5q^4-36q^2+16q+32
 \ge-31q^2+16q+32\ge57/16>0.
\]
The expression in (9) is therefore largest at
\(t=9/100,q=5/4\), where it is
\(-1863/6400+117/1024=-4527/25600\).

Since \(N_R,A>0\), (9) gives
\[
 \arg N<\arctan\!\left(\tfrac32\tan\theta\right)
                     <\tfrac32\theta=\arg(T^3).
 \tag{10}
\]
The middle inequality follows from strict convexity of tangent,
and \(3\theta/2<\pi/2\). Both arguments lie between
\(-\pi/2\) and \(\pi/2\), so their negative difference lies
strictly between \(-\pi\) and zero. Hence
\(\Im(N/T^3)<0\), and
\[
                         \partial_b\Re F(a+ib)>0 .
 \tag{11}
\]

It remains to minimize on \(b=0\).
There \(N_R=a(a^2+5)\) and \(N_I=3a^2-1\).
Their sum is positive for \(a\ge3/10\), since its value at
that endpoint is \(797/1000\) and its derivative is positive.
Thus \(\arg N>-\pi/4\).
Also
\[
 \frac{\Im(T^2)}{\Re(T^2)}
       =\frac{2a}{a^2+3}\le\frac8{19}<\frac1{\sqrt3},
\]
so \(0<\arg(T^3)<\pi/4\).
It follows that \(\Re(N/T^3)>0\), and therefore
\(\partial_a\Re F(a)>1\) on this bottom edge.
Together with (11), this proves that the minimum of \(\Re F\)
on (7) occurs at \(p=3/10\).

## 4. The strict cap bound and its scope

At \(p=3/10\),
\[
 T^2=\frac{309}{100}+\frac35i,\qquad
 |T|^2=\frac{\sqrt{99081}}{100}<\frac{63}{20},
 \qquad \Re T>\sqrt{309/100}>\frac74 .
 \tag{12}
\]
Consequently \(\Re(1/T)>5/9\). Substituting in (3) proves
the stronger explicit bound
\[
 \boxed{\displaystyle
    -\frac{\Re S''(e)}{\pi}
       >\frac3{10}+\frac{109}{50}\frac59
       =\frac{68}{45}>\frac32
                  \qquad(e\in\mathcal E_0).}
 \tag{13}
\]

The same proof also retains a useful dependence on the private
cotangent. Since \(\partial_a\Re F(a)>1\) on the bottom edge
and \(\partial_b\Re F>0\), it gives the stronger variable bound
\[
 \boxed{\displaystyle
       \Re\sigma>a+\frac{109}{90},
       \qquad a=\Re\cot\pi e,\quad e\in\mathcal E_0.}
 \tag{14}
\]
Indeed integrate the bottom-edge derivative from \(3/10\) to \(a\)
and use \(68/45-3/10=109/90\).

For example, the private real pivot in the height-envelope Schur
formula is
\[
 E_0=\Re\sigma+\Re\cot\pi e+b_e
                   >2a+\frac{109}{90}+b_e
                   >\frac{163}{90}+b_e,
 \qquad b_e=-\Re\cot\pi(e+z),
 \tag{15}
\]
at every actual factorial optimizer: there
\(\Re(e+z)>.52\) and \(<.79\), so \(b_e>0\).
This improves the earlier bound obtained from \(1/43\), while
retaining the same canonical action and all fixed private heights.

An improved private pivot decreases one response contribution, but
does not by itself control the last shared-coordinate Schur
denominator or the combined effective curvature. In particular
(13) does not prove \(K_{\mathrm{eff}}\le6\pi\).
The stationary modulus constraints, original outgoing tangent,
the rest of the optimizing path, and all finite-source currents
remain separate parts of that problem.
