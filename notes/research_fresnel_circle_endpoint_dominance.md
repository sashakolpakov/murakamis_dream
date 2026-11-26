# Complex-color Fresnel endpoints survive the original circle difference

Private written deduction, 14 November 2026. No numerical calculation,
test, or frozen-manuscript change is used. This isolates a specific
issue in extracting a geometric symbol from a fused original twist.
It concerns an individual retained charge integral, not the coherent
sum of all charges or its original exterior pairing.

The exact full-Hermite filling formula in
[the coherent Gaussian note](actual_coherent_filling_gaussian_chirp.md),
equations (8), (10), and (12h), uses
\[
 I_{P,N}(b)=\int_0^1
   e^{2\pi iPN(t-1/2)^2-2\pi i bt}\,dt,
 \qquad P\in\mathbb Z\setminus\{0\}.
 \tag{1}
\]
The original circle-basis difference cancels the entire endpoint
current called \(J\) there. Its retained charge integral is nevertheless
\[
 D_{P,N}(b)=I_{P,N}(b-1)-I_{P,N}(b+1)
 =\int_0^1 2i\sin(2\pi t)
       e^{2\pi iPN(t-1/2)^2-2\pi i bt}\,dt.
 \tag{2}
\]
The integer charge and the exact common phases multiplying (2) in
the original kernel remain unchanged. In particular cancellation
of \(J\) does not identify (2) with a complete Gaussian integral.

## 1. Exact leading endpoint coefficients off the real color line

Write \(b=N\beta\), \(\beta=x+iy\), with \(y\ne0\), and put
\[
 S_\beta(t)=2\pi iP(t-1/2)^2-2\pi i\beta t.
 \tag{3}
\]
All asymptotic errors below are uniform when \(\beta\) ranges over
a fixed compact subset of either open half-plane and \(P\) is fixed.

**Lemma 1.** If \(y>0\), then
\[
 \begin{split}
 I_{P,N}(N\beta)
  &=\frac{e^{N(i\pi P/2-2\pi i\beta)}}
          {2\pi iN(P-\beta)}(1+O(N^{-1})),\\
 D_{P,N}(N\beta)
  &=\frac{i\,e^{N(i\pi P/2-2\pi i\beta)}}
          {\pi N^2(P-\beta)^2}(1+O(N^{-1})).
 \end{split}
 \tag{4}
\]
If \(y<0\), then
\[
 \begin{split}
 I_{P,N}(N\beta)
  &=\frac{e^{Ni\pi P/2}}
          {2\pi iN(P+\beta)}(1+O(N^{-1})),\\
 D_{P,N}(N\beta)
  &=-\frac{i\,e^{Ni\pi P/2}}
          {\pi N^2(P+\beta)^2}(1+O(N^{-1})).
 \end{split}
 \tag{5}
\]
In particular the displayed leading coefficients are nonzero.

*Proof.* On the real interval,
\[
 S_\beta'(t)=2\pi i\{P(2t-1)-\beta\},\qquad
 |S_\beta'(t)|\ge2\pi|y|,\qquad
 |e^{NS_\beta(t)}|=e^{2\pi Nyt}.
 \tag{6}
\]
Thus integrations by parts with
\(e^{NS}=(NS')^{-1}(e^{NS})'\) have uniformly bounded
coefficient functions. The integral of their absolute remainders
is \(O(e^{2\pi Ny}/N)\) for \(y>0\), and \(O(1/N)\)
for \(y<0\). The first integration for amplitude one gives the
first lines of (4) and (5); the opposite endpoint is exponentially
smaller.

For \(a(t)=2i\sin(2\pi t)\), both endpoint values vanish.
Two integrations give the endpoint term
\[
 -\frac1{N^2}
       \left[\frac{a'(t)}{S_\beta'(t)^2}
                                  e^{NS_\beta(t)}\right]_0^1.
 \tag{7}
\]
Here \(a'(0)=a'(1)=4\pi i\),
\(S_\beta'(1)=2\pi i(P-\beta)\), and
\(S_\beta'(0)=-2\pi i(P+\beta)\).
The remainder bound from (6) after these integrations is one
further power of \(N^{-1}\) below (7). These evaluations give
the second lines of (4) and (5). \(\square\)

## 2. The Gaussian saddle is exponentially smaller in an interior strip

The exact quadratic saddle and its phase are
\[
 t_* =\frac12+\frac{\beta}{2P},\qquad
 S_\beta(t_*)=-\pi i\beta-\frac{\pi i\beta^2}{2P}.
 \tag{8}
\]
Suppose its real projection lies strictly inside the original
interval, equivalently \(|x/P|<1\). The three real phase values are
\[
 \Re S_\beta(0)=0,\qquad
 \Re S_\beta(1)=2\pi y,\qquad
 \Re S_\beta(t_*)=\pi y(1+x/P).
 \tag{9}
\]
For every nonzero \(y\), the saddle value is strictly between
the two endpoint values. Its gap below the larger endpoint is
\[
 \max(0,2\pi y)-\Re S_\beta(t_*)
       =\pi|y|\{1-\operatorname{sgn}(y)x/P\}>0.
 \tag{10}
\]
The endpoint asymptotics therefore show, for both (1) and the
actual circle difference (2),
\[
 \lim_{N\to\infty}N^{-1}\log|I_{P,N}(N\beta)|
 =\lim_{N\to\infty}N^{-1}\log|D_{P,N}(N\beta)|
 =\max(0,2\pi y).
 \tag{11}
\]
The circle subtraction lowers the leading endpoint by one power
of \(N\), but does not lower its exponential rate. The statement
does not extend uniformly to \(y=0\); real-color stationary-phase
packets in the coherent Gaussian note remain valid.

## 3. Consequence for finite Gaussian fusion

A finite residue-class fusion of the physical Gaussian charges can
retain their normal data through a discontinuous linear or sawtooth
weight on a real Fresnel line. Lemma 1 explains why deleting that
weight's endpoint or jump contributions before a complex-color
deformation is not an exponential approximation to the original
single-charge source. The normal circle difference alone does not
make this deletion valid.

This calculation does not show that such terms survive their
coherent charge sum or the exterior contraction. They can cancel,
and the original source already supplies identities that exploit
those cancellations. In particular
[the source Fourier endpoint theorem](actual_filling_source_fourier_endpoint_gap.md)
proves a gap after pairing with its specified analytic exterior;
its hypotheses and actual color corridor remain essential.
That theorem is entirely compatible with the nonzero coefficients
in (4) and (5).

Thus finite Gaussian fusion offers an exact constructive kernel,
but nonzero geometric filling for arbitrary fixed short tangles
still requires a source-preserving treatment of its joined jumps
and external color contour. A nonzero complete-Gaussian symbol by
itself omits exponentially larger terms even in the concrete
circle-difference integral (2). No conclusion about the whole
knot's geometric coefficient or hyperbolic volume follows from
this single-charge obstruction.
