# Accretivity and original gradient strips on the enlarged paired rectangle

Research deduction, 7 November 2026. The coherent real index box may
be enlarged in the first two coordinates while keeping the same
original negative and positive contour heights. The full complex
Hessian remains accretive, and all four original gradient imaginary
parts remain strictly between \(-2\pi\) and \(2\pi\).
These are analytic domain statements. They neither change the failed
old physical-tail comparisons nor assert newly evaluated face bounds.

Retain the exact finite source, phase \(\mathcal F\), parameter
\(K=\rho e^{2\pi i\xi}\), and original primitive \(g\) from
[the contracted pair](research_mixed_contracted_pair_rectangle.md).
The new product is
\[
\begin{split}
 \mathcal S&=[1/4,1/2]+i[-3/100,3/200],\\
 \mathcal T&=[1/5,9/20]+i[-3/100,3/200],\\
 \mathcal P=\mathcal Q&=[1/5,21/50]+i[-11/200,3/200],\\
 \mathcal R'&=\mathcal S\times\mathcal T\times\mathcal P\times\mathcal Q,
 \qquad C'=\mathcal R'\cap\mathbb R^4.
\end{split}
 \tag{1}
\]
The inherited bounds imply
\(3/5<\rho<5/8\) and \(7/40<\xi<3/16\).
The three summed real arguments lie in
\([.45,.95],[.4,.87],[.4,.84]\), strictly inside the original
factorial strip. The external denominator modulus remains less
than \(.7\). Thus the same exact interpolant and original branches
are regular on a neighborhood of \(\mathcal R'\).

## 1. The small exceptional summed-real region is still accretive

Write \(V(z,w)=g(z+w)-g(z)-g(w)\). The exact phase decomposes as
\[
 \mathcal F=
 \underbrace{g(s+t)-g(t)+\ell_s(x_0)}_{B(s,t)}
 +V(t,p)+V(p,q)-g(p)+2\pi itp+\ell_q(x_0).
 \tag{2}
\]
The negative real Hessians of both \(V\) pairs are positive
definite throughout (1), by the original complex triangle criterion:
all their real legs are at least \(.2\) and below \(.5\),
and \(\cos(.4\pi)<1/2<e^{-.11\pi}\). The own \(-g(p)\)
term is positive in the negative Hessian. Both external incidence
diagonals are positive because
\(0<\Re s-\xi,\Re q-\xi<1/2\).

If \(\Re(s+t)\ge1/2\), the \(g(s+t)\) contribution is
positive semidefinite in the negative real Hessian. The remaining
own \(-g(t)\) and external \(s\) diagonal make \(B\)
strictly accretive as well. The only new case is
\(\Re(s+t)<1/2\). Then necessarily
\[
 \Re s\in[1/4,3/10),\qquad \Re t\in[1/5,1/4).
 \tag{3}
\]
Put \(C=\Re\cot\pi(s+t)\) and \(T=\Re\cot\pi t\).
Since the summed real part is at least \(.45\),
\[
                   0<C\le\tan(\pi/20)<1/5,
                  \qquad T>4/5.
 \tag{4}
\]
For the first upper bound, use \(\sin x\le x\),
\(\cos x\ge1-x^2/2\), and \(\pi<22/7\).
For the second, \(\sin(2\pi\Re t)>9/10\),
\(\cos(2\pi\Re t)\ge0\), and
\(\cosh(.06\pi)<11/10\), so \(T>9/11>4/5\).
The hyperbolic bound follows, for example, from \(.06\pi<1/5\)
and \(\cosh(1/5)\le(1-(1/5)^2/2)^{-1}=50/49\).

Let \(r_s=\rho e^{2\pi\Im s}\) and
\(\theta=2\pi(\Re s-\xi)\). The original parameter bounds
and (3) give
\[
 \frac{12}{25}<r_s<\frac7{10},\qquad
 \frac\pi8<\theta<\frac\pi4,
 \qquad\sin\theta>\frac38,\quad\cos\theta>\frac7{10}.
 \tag{5}
\]
Indeed \(e^{.06\pi}<5/4\) and
\(e^{.03\pi}<28/25\), by the elementary exponential-series
bounds already used in the contour proof. The two trigonometric
comparisons follow from the exact half-angle values at \(\pi/8\)
and \(\pi/4\).

The external diagonal therefore obeys
\[
\begin{split}
 a_s&=-\Re\ell_{s,ss}(x_0)
       =\frac{2\pi r_s\sin\theta}
                    {1+r_s^2-2r_s\cos\theta},\\
 1+r_s^2-2r_s\cos\theta
       &<1+\frac{49}{100}-2\frac{12}{25}\frac7{10}
         =\frac{409}{500}<\frac56,\\
 a_s&>\frac{54\pi}{125}.
\end{split}
 \tag{6}
\]
For real horizontal variations, the complete two-coordinate form is
\[
 -\Re d^2B=a_s\,ds^2+\pi T\,dt^2-\pi C(ds+dt)^2
       >\frac{4\pi}{125}\,ds^2+\frac{2\pi}{5}\,dt^2,
 \tag{7}
\]
using \((ds+dt)^2\le2(ds^2+dt^2)\). The chirp in (2)
has zero real Hessian. Combining (7) with the positive pair forms
proves that \(-\Re\mathcal F''\) is positive definite everywhere
on \(\mathcal R'\). Compactness supplies a uniform
\(\mu'>0\), and continuity supplies a fixed neighborhood in
the external variables \(x,y\). In particular the whole real
box \(C'\), not just its faces, is strictly concave for the
original physical rate \(E=\Re\mathcal F\).

## 2. The same original gradient strips extend to this box

At \(x=y=x_0\), the exact four gradients are unchanged:
\[
\begin{split}
 \mathcal F_s&=g'(s+t)+\ell_{s,s}(x_0),\\
 \mathcal F_t&=g'(s+t)+g'(t+p)-2g'(t)+2\pi ip,\\
 \mathcal F_p&=g'(t+p)+g'(p+q)-3g'(p)+2\pi it,\\
 \mathcal F_q&=g'(p+q)-g'(q)+\ell_{q,q}(x_0).
\end{split}
 \tag{8}
\]
All logarithms are original \(g'(z)=\operatorname{Log}(1-e^{-2\pi iz})\)
lifts. For an own leg \(z\in\{t,p,q\}\),
\(e^{2\pi\Im z}<10/9\) and
\(\cos(2\pi\Re z)\le\cos(2\pi/5)<5/16\).
The complex number inside its logarithm consequently has real part
greater than \(47/72\), positive imaginary part at most \(10/9\),
and hence
\[
                         0<\Im g'(z)<\pi/3,
                  \qquad\frac{80}{47}<\sqrt3.
 \tag{9}
\]
For \(t+p\) and \(p+q\), the original positive-real-part
argument from the smaller rectangle still applies: their real
parts are in \([.4,.87]\), their heights are at most \(.03\),
and \(e^{.06\pi}\cos(\pi/5)<637/640<1\).
Their imaginary logarithms therefore lie in
\((-\pi/2,\pi/2)\).

The first sum \(s+t\) now has real part in \([.45,.95]\).
Below \(1/2\), the complex number inside its logarithm has
positive real part, and its argument is less than \(\pi/2\).
Above \(1/2\), its imaginary part is negative, so its original
argument stays in \((-\pi,0)\), even where its real part
is negative. No negative-axis crossing or lift reset occurs.
Thus
\[
                          -\pi<\Im g'(s+t)<\pi/2.
 \tag{10}
\]
Both external rotated factors still lie in the lower half-plane
with modulus below \(.7\); as before,
\(\Im\ell_{s,s},\Im\ell_{q,q}\in(-\pi/2,\pi/2)\).
Equations (8)--(10) and the original real-coordinate intervals give
\[
\begin{array}{c|c}
 j&\Im\mathcal F_j/\pi\\\hline
 s&(-3/2,1)\\
 t&(-53/30,46/25)\\
 p&(-8/5,19/10)\\
 q&(-4/3,1).
\end{array}
 \tag{11}
\]
Every interval is strictly inside \((-2,2)\). Compactness again
makes the margin uniform and preserves it under small half-grid
and external-parameter perturbations.

Consequently the entire
[simultaneous contour argument](research_mixed_contracted_pair_simultaneous_contour.md)
applies on \(C'\) with the same original contour heights:
the common-height joins use joint imaginary convexity; vertical
lattice corrections use the corresponding physical-face gap;
and the 80 horizontal products reduce to the same eight
single-coordinate-height maxima, now over \(C'\).
This transfers a valid reduction, not any numerical values of those
maxima.

## 3. What this permits for saved tangents

For any old support point \(y\in C\subset C'\), concavity on
the whole new real box gives
\[
             E(x)\le E(y)+\nabla E(y)\cdot(x-y),
                           \qquad x\in C'.
 \tag{12}
\]
In particular \(y\) need not lie on a new face. The new fixed
face coordinate and all new free-coordinate endpoints must be
inserted into this same affine function, with their exact signs.
No previously saved derivative or scalar enclosure is replaced by
a midpoint. Thus existing full-gradient records may supply new
face uppers through a separate exact saved-data recombination.
This note performs no such recombination and makes no new sign claim.

The enlarged coherent box also changes the physical-tail domain.
Its complete tail-preserving clips are treated separately in
[the enlarged tail reduction](research_mixed_contracted_pair_enlarged_tail_reduction.md).
The failed old real faces remain part of the immutable evidence;
they are now included in the coherent region instead of being
bounded separately by a smaller raw absolute rate.

## 4. An equivalent original primitive for direct enclosure

On the strip \(0<\Re z<1\), the same original primitive is
\[
            g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}
                                    {2\pi i}.
 \tag{13}
\]
Here \(\operatorname{Li}_2\) is its principal continuation
off \([1,\infty)\). The exponential of a point in this open
strip never meets that cut. Differentiating (13) gives exactly
\(\operatorname{Log}(1-e^{-2\pi iz})\), with the lift used
above. Its limit as \(z\downarrow0\) on the positive real
axis is zero, fixing the same additive constant as the original
\(J(z)+i\pi(z-z^2)/2\). The derivative identity and this limit
prove (13) throughout the strip.

At \(x=y=x_0\), the complete phase may consequently be evaluated
in the equivalent form
\[
\begin{split}
 \mathcal F={}&g(s+t)+g(t+p)+g(p+q)-2g(t)-3g(p)-g(q)\\
             &+2\pi itp+(s+q-1)\operatorname{Log}K-I_K(s)-I_K(q),\\
 I_K(z)&=\frac{\operatorname{Li}_2(Ke^{-2\pi iz})-
                                  \operatorname{Li}_2(K)}{2\pi i},
 \qquad \operatorname{Log}K=2\pi ix_0.
\end{split}
 \tag{14}
\]
The two denominator arguments stay inside the original disk of
radius less than \(.7\). Each of the three summed \(g\)
arguments and each own argument stays in its stated original
strip. Formula (14) retains the chirp, both cardinal contributions
and every primitive constant; it introduces neither a new phase
nor a different logarithmic branch.
