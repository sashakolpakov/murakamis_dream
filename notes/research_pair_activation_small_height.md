# A small-height bound during simultaneous pair activation

Research note, 3 November 2026. Frozen manuscripts are unchanged.

The positive charge family is supplied by
[the fractional-charge theorem](research_positive_path_fractional_charge_cube.md).
Fix two adjacent vertices of power three and give them the same
charge \(\chi\in(0,1]\). Other selected powers are integers at
least three, and their charges may be any numbers in \([0,1]\).
All original outside vertices remain complete. Write the two new
angles as \(t=a-ih\), \(u=b-ik\), and put \(H=\max(h,k)\).

**Theorem.** If \(0<H\le1/1000\), then
\[
                              H<\frac{59}{50}\chi.
 \tag{1}
\]
This is a bound on the actual stationary geometry. It neither
estimates a quantum source nor proves the corresponding bound at
larger heights.

## 1. Both new angles are small

Suppose, to the contrary, that
\(\chi\le50H/59\). Every individual return has imaginary part
between \(-\pi/2\) and \(\pi/2\). The two charge equations imply
\[
                  a,b<\frac{2\pi}{3}(1+\chi)<\frac{21}{10}.
 \tag{2}
\]
The last inequality uses \(\pi<22/7\) and \(\chi<1/1000\).
On this interval \(\sin a\ge2a/5\), while
\(\cosh h+\cos a<201/100\). Moreover
\[
       \Re\cos(u/2)
          =\cos(b/2)\cosh(k/2)
                       >1-\frac{(21/20)^2}{2}=\frac{359}{800}.
 \tag{3}
\]
The real part of \(\tan(t/2)\cos(u/2)\) is consequently at
least \(359a/4020\): both terms in its real part are nonnegative,
and one is the product of the two real parts.

For a return \(r=p+ig\), the identity
\(\Re\sinh r=\sinh p\cos g\le\sinh p\) shows that this real
part is at most the hyperbolic sine of its real return.
The real period equation bounds that return by \(3h/2\).
Applying the same argument at the other vertex gives
\[
 a,b\le\frac{4020}{359}\sinh(3H/2)<17H,\qquad
                         |t|,|u|<18H.
 \tag{4}
\]
All inequalities here are uniform as \(H\) tends to zero.
For completeness, \(\sin z/z\ge2/5\) on \([0,21/10]\)
follows by its lower alternating polynomial
\[
 1-\frac{z^2}{6}+\frac{z^4}{120}-\frac{z^6}{5040}.
 \]
This polynomial is decreasing there and is greater than \(2/5\)
at \(21/10\). Also
\(\cosh h\le(1-h^2/2)^{-1}<101/100\), and
\[
 \frac{\sinh(3H/2)}{H}
       \le\frac{3/2}{1-3/8000000}<\frac{17\cdot359}{4020}.
 \tag{5}
\]
These positive-series estimates justify the other constants
in (2)--(4).

## 2. The exact return equation and its controlled error

Choose the endpoint of height \(H\), and call its angle \(t\).
Let \(c\) be the cosine of half the angle at its other neighbor.
At a complete neighbor \(c=1\). If the vertex is an original
terminal, pad its absent incidence by \(c=0\).
The uniform height bound and the quarter-ellipse calculation give
\[
 c=x+iy,\quad x,y\ge0,\qquad
                 \frac{x^2}{11/8}+\frac{y^2}{3/8}\le1,
                 \qquad |c|<\frac65.
 \tag{6}
\]
The two exact returns are
\(\operatorname{arsinh}(c\tan(t/2))\) and
\(\operatorname{arsinh}(\cos(u/2)\tan(t/2))\).

For the ranges in (4), elementary Taylor bounds give
\[
 \begin{split}
 |\tan(t/2)-t/2|&\le |t|^3/16,&
 |\tan(t/2)|&\le(51/100)|t|,\\
 |\cos(u/2)-1|&\le |u|^2/7,&
 |\cos(u/2)|&\le101/100,\\
 |\operatorname{arsinh}z-z|&\le |z|^3/5
                                &&(|z|\le1/50).
 \end{split}
 \tag{7}
\]
Here all inverse hyperbolic sines are on their analytic branch at
zero. The arguments in question have modulus less than \(1/50\),
since \(|t|<18/1000\).
One direct justification of the first bound is to integrate
\((\tan z-z)'=\tan^2z\) along a radius:
for \(|z|\le1/100\), the positive sine and cosine series give
\(|\tan z|\le(6/5)|z|\). The resulting error is at most
\(3|t|^3/50<|t|^3/16\).
For the cosine bound, use
\[
 |\cos(u/2)-1|
       \le\frac{|u|^2}{8(1-|u|^2/48)}\le |u|^2/7.
 \]
Finally the absolute binomial coefficients in
\((1+z^2)^{-1/2}-1\) are at most \(1/2\), so radial
integration bounds the inverse-sine error by
\(|z|^3/[6(1-|z|^2)]\le|z|^3/5\).

Set \(A=\tan(t/2)\), \(d=\cos(u/2)\).
Subtracting \(t(1+c)/2\) from the sum of the two returns leaves
\[
 (A-t/2)(1+c)+A(d-1)
       +\{\operatorname{arsinh}(Ac)-Ac\}
       +\{\operatorname{arsinh}(Ad)-Ad\}.
 \]
Thus their sum has the exact form
\[
                    \frac t2(1+c+\epsilon),\qquad
                            |\epsilon|<200H^2\le\frac1{5000}.
 \tag{8}
\]
Indeed (7) bounds its relative error by
\[
 \begin{split}
 |\epsilon|\le{}&
 \left[\frac{11}{40}
    +\frac25\left(\frac{51}{100}\right)^3
             \left\{\left(\frac65\right)^3
                          +\left(\frac{101}{100}\right)^3\right\}\right]|t|^2
       +\frac{51}{350}|u|^2\\
 <{}&200H^2.
 \end{split}
 \tag{9}
\]
The coefficient after using \(|t|^2,|u|^2\le324H^2\)
is the rational number
\(803822915834217/4375000000000<184\).

## 3. A positive quadratic separation

Put \(C=1+c+\epsilon\). The full logarithmic equation at the
chosen endpoint becomes
\[
             \frac t2 C=\frac{3it}{2}-\pi i\chi,\qquad
             t=\frac{2\pi\chi}{3+iC},\qquad
       \frac H\chi=\frac{2\pi\Re C}{|3+iC|^2}.
 \tag{10}
\]
In particular the assumed inequality \(H/\chi\ge59/50\)
would require
\[
       |3+iC|^2-\frac{100\pi}{59}\Re C\le0.
 \tag{11}
\]
We prove the opposite inequality uniformly over (6).

First set \(\epsilon=0\), put \(\kappa=100\pi/59\), and
write
\[
 G_0=(1+x)^2+(3-y)^2-\kappa(1+x).
 \]
Subtract twice the nonnegative ellipse slack in (6).
Completing squares on the whole real \((x,y)\)-plane gives
\[
 \begin{split}
 G_0&\ge 8-\kappa-\frac{11(\kappa-2)^2}{108}-\frac{27}{19}\\
 &\ge
 8-\frac{2200}{413}
   -\frac{11}{108}\left(\frac{2200}{413}-2\right)^2-\frac{27}{19}
       =\frac{1213006}{9722433}.
 \end{split}
 \tag{12}
\]
For the second inequality use \(2<\kappa<2200/413\),
which follows from \(3<\pi<22/7\), and observe that the preceding
quadratic expression decreases for \(\kappa\ge2\).

Let \(D=3+i(1+c)\). Equation (6) gives
\(|D|^2\le9+(11/5)^2<16\).
Perturbing by \(\epsilon\), and dropping its nonnegative
squared modulus, therefore gives
\[
 \begin{split}
 |3+iC|^2-\kappa\Re C
 &\ge G_0-(2|D|+\kappa)|\epsilon|\\
 &> \frac{1213006}{9722433}
                       -\frac{40}{3}\frac1{5000}>0.
 \end{split}
 \tag{13}
\]
Here \(\kappa<16/3\). This contradicts (11) and proves
the theorem.

The [exact scalar checker](../experiments/check_pair_activation_small_height.py)
verifies all rational comparisons in this argument; its
[saved results](../repro/results/research-pair-activation-small-height.json)
do not use numerical fitting or interval subdivision.

## 4. Extending the height interval by the exact period equation

The small disk in the preceding proof can be enlarged. The useful
observation is that the exact equation (10) improves a coarse bound
for the real angles before the Taylor remainder is estimated again.

**Theorem 2.** In the same setting, the conclusion
\[
                          H<\frac{59}{50}\chi
 \tag{14}
\]
holds whenever \(0<H\le3/100\).

*Proof.* Suppose instead that \(\chi\le50H/59\).
The imaginary period equation now gives
\[
 a,b<\frac{2\pi}{3}(1+\chi)
     \le\frac{44}{21}\left(1+\frac3{118}\right)
     <\frac{43}{20}.
 \tag{15}
\]
On this interval \(\sin a\ge3a/8\): the decreasing lower
alternating polynomial used in Section 1 is still greater than
\(3/8\) at \(43/20\). Also
\(\cosh h+\cos a<201/100\), and
\[
 \Re\cos(u/2)>
          1-\frac12\left(\frac{43}{40}\right)^2
                         =\frac{1351}{3200}.
 \tag{16}
\]
The real return argument in Section 1 therefore gives
\[
 \Re\{\tan(t/2)\cos(u/2)\}
          \ge\frac{1351}{17152}a,\qquad
 a,b\le\frac{17152}{1351}\sinh(3H/2)<20H.
 \tag{17}
\]
For the last comparison one may use
\(\sinh(3H/2)/H\le(3/2)/(1-3H^2/8)\).
Consequently \(|t|,|u|<21H\le63/100\).

We first estimate the return error on this larger disk. The following
constants suffice:
\[
 \begin{split}
 |\tan(t/2)-t/2|&\le |t|^3/16,&
 |\tan(t/2)|&\le(11/20)|t|,\\
 |\cos(u/2)-1|&\le |u|^2/7,&
 |\cos(u/2)|&\le17/16,\\
 |\operatorname{arsinh}z-z|&\le(11/50)|z|^3
                                  &&(|z|\le9/20).
 \end{split}
 \tag{18}
\]
Here is a direct check of the ranges. If \(|z|\le r=63/200\),
then \(|\sin z|\le\sinh r\) and
\(|\cos z|\ge\cos r\ge1-r^2/2\). More precisely,
\[
 |\tan z|
   \le\frac{|z|}{(1-r^2/6)(1-r^2/2)}
   <\frac65|z|.
 \tag{19}
\]
Integrating \(\tan^2z\) along a radius proves the first estimate
in (18), with the stronger coefficient \(3/50<1/16\).
It then gives the displayed \(11/20\) bound. The cosine estimate
follows from
\(|u|^2/[8(1-|u|^2/48)]\), and gives the absolute bound \(17/16\).
The two inverse-hyperbolic-sine arguments have moduli at most
\[
 \frac{11}{20}\frac{63}{100}\frac65<\frac9{20},
 \qquad
 \frac{11}{20}\frac{63}{100}\frac{17}{16}<\frac9{20}.
 \tag{20}
\]
On that disk the radial binomial estimate gives
\[
 \frac{|\operatorname{arsinh}z-z|}{|z|^3}
     \le\frac1{6(1-(9/20)^2)}<\frac{11}{50},
\]
which completes the justification of (18).

At either endpoint, let \(c\) denote its other neighbor's cosine,
as in Section 2. Its return sum is exactly
\(t(1+c+\epsilon)/2\). The same subtraction as in (8)--(9),
now using (18), bounds its error by
\[
 \begin{split}
 |\epsilon|
 &\le
 \left[\frac{11}{40}
       +\frac{11}{25}\left(\frac{11}{20}\right)^3
                 \left\{\left(\frac65\right)^3
                                +\left(\frac{17}{16}\right)^3\right\}\right]|t|^2
       +\frac{11}{70}|u|^2\\
 &<286H^2\le\frac{1287}{5000}.
 \end{split}
 \tag{21}
\]
The coefficient after substituting \(|t|,|u|<21H\) is
\(285.083470\ldots<286\); the checker uses its exact rational value.

For either endpoint write its own height as \(h\le H\) and
\(C=1+c+\epsilon\). Its exact equation, not a Taylor approximation,
is still
\[
 t=\frac{2\pi\chi}{3+iC},\qquad
 \frac{a}{h}=\frac{3-\Im C}{\Re C}.
 \tag{22}
\]
Since \(c\) is in the closed first quadrant, whenever
\(|\epsilon|\le e<1\), this gives
\[
 \frac{|t|}{h}
 \le\sqrt{1+\left(\frac{3+e}{1-e}\right)^2}.
 \tag{23}
\]
The numerator in (22) is positive because the actual angle \(a\)
is positive. With \(e=1287/5000\), (23) is strictly less than
\(23/5\). The improvement applies to both endpoints, so now
\[
                         |t|,|u|<\frac{23}{5}H
                                             \le\frac{69}{500}.
 \tag{24}
\]

On the smaller disk (24), the sharper numerical constants of
(7) apply: the tangent factor is \(51/100\), the absolute cosine
bound is \(101/100\), and both return arguments have modulus less
than \(1/10\). The inverse-hyperbolic-sine cubic bound \(1/5\)
remains valid on this disk, since
\(1/[6(1-(1/10)^2)]<1/5\). Thus the error calculation (9),
with the new angle bound, gives
\[
                         |\epsilon|<13H^2
                                           \le\frac{117}{10000}.
 \tag{25}
\]
Substituting this value of \(e\) into (23) improves the two angle
bounds again, to \(|t|,|u|<(13/4)H\).
Using (9) a final time gives
\[
                          |\epsilon|<6H^2
                                              \le\frac{27}{5000}.
 \tag{26}
\]
For clarity, if \(C_*\) is the sum of the two coefficients of
\(|t|^2\) and \(|u|^2\) in (9), the two comparisons just used are
\[
             C_*(23/5)^2<13,\qquad C_*(13/4)^2<6.
 \tag{27}
\]
They are exact rational inequalities.

The separation in Section 3 can now be repeated without change,
apart from its error budget. Equations (12), (13), and (26) give
\[
 |3+iC|^2-\frac{100\pi}{59}\Re C
 >\frac{1213006}{9722433}
                       -\frac{40}{3}\frac{27}{5000}
 =\frac{64123853}{1215304125}>0.
 \tag{28}
\]
This contradicts \(H/\chi\ge59/50\) at the endpoint whose height
is \(H\), as before. The theorem follows. \(\square\)

The same scalar checker records the rational estimates in this
extension. This proves a larger small-height interval independently
of the ongoing support certificates; it does not by itself settle
the bounds at larger heights.
