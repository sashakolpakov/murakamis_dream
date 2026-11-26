# The action gap needed to discard extreme wire indices

Research lemma, 2 November 2026. This note treats the selected classical
action of an isolated original vertex. It supplies an estimate needed
in a quantum contour proof; it does not by itself prove the asymptotic
of that quantum source.

## 1. The action and the assertion

Let \(d\ge1\) be the degree, \(n\in\mathbb Z\) the signed crossing
power, and put
\[
 M_\infty=\psi(0,0)=\frac{4G}{\pi},
 \qquad G=\sum_{j\ge0}\frac{(-1)^j}{(2j+1)^2}.
\]
For a real cone parameter \(0\le\lambda\le1\), let \(t(\lambda)\)
be the selected solution of
\[
 d\psi_t(t,0)+\frac{in}{2\pi}t=i\lambda,
 \qquad
 \psi_t(t,0)=-\pi^{-1}\operatorname{arsinh}(\tan(t/2)).
\]
The [geometric branch theorem](research_isolated_internal_vertex_geometry.md)
proves existence and nondegeneracy throughout this path when
\(d+|n|>2\). Define
\[
 M_{d,n}=\Re\left[
 d\psi(t(1),0)+\frac{in}{4\pi}t(1)^2-it(1)\right],
 \qquad
 \Delta_{d,n}=dM_\infty-M_{d,n}.
 \tag{1}
\]

**Proposition.** Among the integer pairs with \(d+|n|>2\),
\[
 0<\Delta_{d,n}<M_\infty
 \tag{2}
\]
except at \((d,n)=(2,1),(2,-1),(3,0)\). At these three pairs,
\[
 \Delta_{d,n}=M_\infty.
 \tag{3}
\]
Consequently every nonexceptional pair has
\[
 M_{d,n}>(d-1)M_\infty.
 \tag{4}
\]
The assertion includes every internal degree and both signs. It does
not rely on a numerical scan of the remaining small pairs.

## 2. Monotonicity in the crossing power

For \(n>0\), write \(t(1)=2a-2ib\), with \(a,b>0\).
Nondegeneracy permits \(n\) to vary through the real interval on which
the positive branch exists. Differentiation of the stationary value
eliminates its derivative through \(t\), giving
\[
 \frac{\partial M_{d,n}}{\partial n}
 =\Re\frac{it(1)^2}{4\pi}=\frac{2ab}{\pi}>0.
 \tag{5}
\]
Thus \(\Delta_{d,n}\) strictly decreases as \(n>0\) increases.
Conjugation gives \(\Delta_{d,-n}=\Delta_{d,n}\).
For \(d\ge3\), the branch and action extend continuously to \(n=0\).

Stationarity in the cone parameter likewise gives
\[
 \Delta_{d,n}=2\int_0^1 b(\lambda)\,d\lambda>0.
 \tag{6}
\]
At zero crossing power, the explicit branch is
\[
 b(\lambda)=\operatorname{arsinh}
                  \tan\frac{\pi\lambda}{d},
 \qquad d\ge3.
 \tag{7}
\]
For each \(0<\lambda\le1\), this decreases strictly with \(d\).
Therefore \(\Delta_{d,0}\) decreases strictly with \(d\).

## 3. The exact endpoint value at degree three

Using (7) and substituting \(x=\pi\lambda/3\),
\[
 \Delta_{3,0}=\frac6\pi
       \int_0^{\pi/3}\operatorname{arsinh}(\tan x)\,dx.
 \tag{8}
\]
On this interval,
\(\operatorname{arsinh}(\tan x)=\log\tan(\pi/4+x/2)\).
Integrating the Fourier series of \(\log\tan y\) gives
\[
 \int_0^a\operatorname{arsinh}(\tan x)\,dx
 =2\sum_{\substack{k\ge1\\k\ {\rm odd}}}
    \frac{\sin(k\pi/2)-\sin(k(\pi/2+a))}{k^2}.
 \tag{9}
\]
For completeness, one may first multiply each \(k\)-th term of the
logarithmic Fourier series by \(\rho^k\), \(0<\rho<1\).
The resulting series is uniformly convergent and can be integrated.
The interval from \(\pi/4\) to \(5\pi/12\) stays away from every
zero and pole of the tangent, so its Abel limit is uniform there.
After integration, the series in (9) is absolutely convergent.

For odd \(k\), direct evaluation modulo twelve gives
\[
 \sin(5k\pi/6)=
 \begin{cases}
 \tfrac12\sin(k\pi/2),&3\nmid k,\\
 -\sin(k\pi/2),&3\mid k.
 \end{cases}
\]
Also
\[
 \sum_{\substack{k\ge1\\k\ {\rm odd},\,3\mid k}}
       \frac{\sin(k\pi/2)}{k^2}=-\frac G9.
\]
Hence the sine series at \(5\pi/6\) is
\(\tfrac12G-\tfrac32(-G/9)=2G/3\).
Equation (9) at \(a=\pi/3\) is therefore \(2G/3\).
Substitution in (8) yields
\[
 \Delta_{3,0}=\frac{4G}{\pi}=M_\infty.
 \tag{10}
\]
Monotonicity in \(d\) and \(n\) now proves (2) for every \(d\ge3\)
except \((3,0)\).

## 4. Degrees one and two

For \(d=n=2\), the real cone equations simplify to
\[
 a(\lambda)=\frac{\pi\lambda}{4},
 \qquad b(\lambda)=\operatorname{arsinh}
                         \sin\frac{\pi\lambda}{4}.
\]
Indeed the first equation is \(\sin a=\sinh b\), and then the
second inverse-tangent term equals \(a\). Thus
\[
 \Delta_{2,2}
 =2\int_0^1\operatorname{arsinh}
                 \sin\frac{\pi\lambda}{4}\,d\lambda
 <\frac{\pi}{4}<M_\infty.
 \tag{11}
\]
Here \(\operatorname{arsinh}x\le x\), \(\sin x\le x\), and
strictness holds away from zero. For the last inequality,
\(G>8/9\) and \(\pi<22/7\) already give
\(M_\infty>112/99>\pi/4\).
Equation (5) proves (2) for every \(d=2,\ |n|\ge2\).

The [two-crossing terminal action](research_two_crossing_terminal_filling.md)
has \(M_{1,2}=M_\infty/2\). Equation (5) therefore proves (2)
for every allowed degree-one pair, namely \(|n|\ge2\).

To evaluate the remaining internal pair \((2,1)\), use the exact
symmetry of the selected geometry under interchange of the positive
integers \(d,n\), proved in Section 6 of the geometric branch note.
Writing \(w=e^{it/2}\) and \(R=\sec(t/2)+\tan(t/2)\), the interchange
replaces these parameters by
\[
 w'=\overline R,\qquad R'=\overline w.
\]
Each edge block has the eight shapes
\((iR,iw,i/R,i/w)\), \((i/R,iw,iR,i/w)\).
The Bloch--Wigner identity \(D(1/\overline z)=D(z)\) shows that
the sum of their volumes is unchanged by this replacement: for
example \(D(i\overline R)=D(i/R)\) and
\(D(i/\overline R)=D(iR)\).
The absolute calibration in the same geometric note therefore gives
\[
 \frac{M_{d,n}}{d}=\frac{M_{n,d}}{n}
       \qquad(d,n>0,\ d+n>2).
 \tag{12}
\]
This is an identity of the selected classical actions, not an
asserted equivalence of quantum sources or knot complements.
Taking \((d,n)=(2,1)\) and the known value of \(M_{1,2}\) gives
\(M_{2,1}=M_\infty\), hence \(\Delta_{2,1}=M_\infty\).
Conjugation completes (3) and the proposition.

## 5. Consequence for the original wire tails

Fix a nonexceptional pair, and put
\[
 \eta=M_{d,n}-(d-1)M_\infty>0.
\]
Let \(g(x)=J(2x)-4J(x)\) be the low-index Newton rate, where
\(J(x)=\int_0^x\log(2\sin(\pi v))\,dv\).
It is continuous on \([0,1/2]\), has zero endpoint values, and
\(\max 2g=M_\infty\).
Choose rational \(0<\alpha<\beta<1/2\), sufficiently close to the
two endpoints, so that
\[
 \sup_{x\in[0,\alpha]\cup[\beta,1/2]}2g(x)<\eta/2.
 \tag{13}
\]

The complete Hermite norm estimates in
[the finite-source proof](../papers/circle-tree-volume/finite-bounds.tex)
apply before the trace is taken. A low wire in the discarded range
has rate at most \(\eta/2\); all other wires have rate at most
\(M_\infty\). A high wire has only polynomial norm, and hence rate
zero. Multiplication by the fixed crossing power and the original
trace cost only a polynomial in \(N\). Consequently the sum of all
assignments with any discarded wire is bounded, uniformly over all
real free boundary angles, by
\[
 C_{d,n}N^A
 \exp\left\{N\left(M_{d,n}-\eta/2\right)\right\}.
 \tag{14}
\]
There are at most \(N^d\) wire assignments, which is polynomial
because \(d\) is fixed. The estimates retain first normal derivatives
and both level parities.

For a finite collection of nonexceptional pairs, take the smallest
positive \(\eta\) and common rational cutoffs satisfying (13).
Thus extreme wire indices can be discarded simultaneously for every
remaining isolated pair except the explicitly listed equality cases.
This removes one obstacle to a common finite contour certificate.
The necessary central contour inequalities remain to be proved.

At the equality cases, the elementary estimate for one high wire has
rate exactly \(M_{d,n}\). This failure of a strict upper-bound gap
does not establish that such terms contribute at the leading rate.
Their exact algebra or cancellation must be retained.
