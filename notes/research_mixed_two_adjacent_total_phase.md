# The phase after fixing the total index of the adjacent pair

Research deduction, 7 November 2026. At equal Fourier endpoints,
the inner phase is symmetric in the two physical indices. Its
midpoint gives a one-variable phase in their sum. On the horizontal
line through its original critical point, this reduced phase has
a unique global real maximum throughout the entire unit interval.
This comparison does not use the false absolute dominance of the
two-variable raised square.

The result concerns the original phase and its Gaussian
normalization. An asymptotic for a physical inner sum does not by
itself justify using its continuation at a complex total index.
The corresponding finite-source continuation and its complete
contour corrections remain separate obligations.

## 1. The unchanged action and its total-index coordinate

Use the phase \(F(a,s;x,y)\) of
[the merged source](research_mixed_two_adjacent_merged_source.md),
equations (21)--(25), with equal external parameters \(x=y=x_0\).
Write
\[
 x_0=\xi+i\upsilon,\qquad
 .18299<\xi<.18301,\qquad .07871<\upsilon<.07873.
 \tag{1}
\]
For a total index \(z=a+s\), the inner phase
\(a\mapsto F(a,z-a;x_0,x_0)\) is symmetric about \(a=z/2\).
Its derivative is therefore zero there. Define its midpoint
value, including the original additive constants, by
\[
 \begin{split}
 \phi(z)
  &:=F(z/2,z/2;x_0,x_0)\\
  &=g(z)+2g(z/2+x_0)-4g(z/2)-2g(x_0)
                                      +\frac{\pi i}{2}z^2 .
 \end{split}
 \tag{2}
\]
All arguments are on their original regular strips when
\(0<\Re z<1\). This is a holomorphic function on that whole
strip; its definition is not inferred from sampled values.
The outside factor in the finite pair adds \(2\pi ix_0\)
to its action and \(e^{-2\pi ix_0}\) to its amplitude.

Let \(a_*=\alpha+ih\) be the original symmetric critical point
in [the critical-corridor theorem](research_mixed_two_adjacent_critical_corridor.md).
Then
\[
 z_*=2a_*,\qquad
 \phi'(z_*)=0,\qquad
 \Re\phi(z_*)-2\pi\upsilon=M_{22}.
 \tag{3}
\]
In particular \(h>1/20\) and \(2/3<\Re z_*<5/6\).
These are the already proved critical point and absolute action.

Differentiating (2) with its original logarithms gives
\[
 \phi'(z)=g'(z)+g'(z/2+x_0)-2g'(z/2)+\pi iz .
 \tag{4}
\]
Put
\[
 X=e^{-2\pi ix_0},\qquad U=e^{-\pi iz}.
\]
Exponentiation, on this regular strip, gives exactly
\[
 e^{\phi'(z)}
             =\frac{(1+U)(1-XU)}{U(1-U)}.
 \tag{5}
\]
Thus its critical equation is
\((1-X)U^2-XU+1=0\), with the original zero lift at \(z_*\).
No constant has been changed to obtain this equation.

## 2. The phase increases throughout the left part of the interval

For \(z=t+iH\), let
\[
 R=e^{\pi H},\qquad S=|X|=e^{2\pi\upsilon},\qquad
 \theta=\pi t,\qquad \vartheta=2\pi\xi .
 \tag{6}
\]
The original elementary output bounds give
\[
 \frac{163}{100}<S<\frac{33}{20},\qquad
 0<\cos\vartheta<\frac{41}{100},\qquad
 \sin\vartheta>\frac{91}{100}.
 \tag{7}
\]
For example the radius bounds are the ones used in
[the complete right-contour proof](research_mixed_three_left_cycle_right_contour.md),
and the sine and cosine bounds are proved by rational
trigonometric inequalities in
[the actual-input subdomain](research_mixed_three_conditional_actual_input_subdomain.md),
equations (7)--(11).

**Lemma 1.** For every \(H\ge0\),
\[
       \Re\phi'(t+iH)>0\qquad(0<t\le1-2\xi).
 \tag{8}
\]

*Proof.* Here \(R\ge1\). By (5), it suffices to prove
\[
 |1+U|^2|1-XU|^2>R^2|1-U|^2 .
 \tag{9}
\]
First suppose \(0<t\le1/2\). Then \(\cos\theta\ge0\),
so \(|1+U|\ge|1-U|\). Also
\(\vartheta\le\vartheta+\theta<\pi\), whence
\[
 \begin{split}
 |1-XU|^2-R^2
 &\ge 1+(S^2-1)R^2-2S R\cos\vartheta\\
 &>1+\frac{33}{20}R^2-\frac{34}{25}R\\
 &\ge1+\frac{29}{100}R^2>0 .
 \end{split}
 \tag{10}
\]
The last inequality uses \(R\le R^2\). This proves (9).

Now let \(1/2\le t\le1-2\xi\), and abbreviate
\(c=\cos\vartheta\), \(d=\sin\vartheta\).
Then
\[
 \frac{\pi}{2}\le\theta\le\pi-\vartheta,\qquad
 \cos\theta\ge-c,\qquad
 \cos(\vartheta+\theta)\le-d .
 \tag{11}
\]
Both factors in the following product are positive. Hence the
left side of (9) minus its right side is at least
\[
 \begin{split}
 &(1+R^2-2cR)(1+S^2R^2+2SdR)
                         -R^2(1+R^2+2cR)\\
 &=(S^2-1)R^4
   +\{2Sd-2c(S^2+1)\}R^3
   +(S^2-4cSd)R^2+(2Sd-2c)R+1 .
 \end{split}
 \tag{12}
\]
The bounds (7), with \(d\le1\), give the strict coefficient
bounds
\[
 \begin{split}
 S^2-1&>\frac{33}{20},\\
 2Sd-2c(S^2+1)&>
       \frac{14833}{5000}-\frac{61049}{20000}
                                                    >-\frac9{100},\\
 S^2-4cSd&>\frac{26569}{10000}-\frac{5412}{2000}
                                                    >-\frac1{20},\\
 2Sd-2c&>\frac{14833}{5000}-\frac{41}{50}>2 .
 \end{split}
 \tag{13}
\]
Consequently (12) is greater than
\[
 \frac{33}{20}R^4-\frac9{100}R^3-\frac1{20}R^2+2R+1
              \ge\frac{151}{100}R^4+2R+1>0.
 \tag{14}
\]
This uses \(R^2,R^3\le R^4\), and completes (9).
Taking the logarithm of the modulus in (5) proves (8).
\(\square\)

## 3. Strict decrease of the derivative on the remaining interval

The double-angle identity
\(\cot(\pi z)-\cot(\pi z/2)=-\csc(\pi z)\)
simplifies the second derivative to
\[
 \phi''(z)=
 \pi\left\{-\csc(\pi z)
       +\frac12\cot\bigl(\pi(z/2+x_0)\bigr)+\frac i2\right\}.
 \tag{15}
\]
For \(0<t<1\),
\[
 \Re\csc\bigl(\pi(t+iH)\bigr)
   =\frac{\sin(\pi t)\cosh(\pi H)}
           {|\sin(\pi(t+iH))|^2}>0 .
 \tag{16}
\]
If \(1-2\xi\le t<1\), then
\(1/2\le\Re(z/2+x_0)<1\). The real part of the cotangent
in (15) is therefore nonpositive, at every height. It follows that
\[
       \Re\phi''(t+iH)<0
                 \qquad(1-2\xi\le t<1).
 \tag{17}
\]

**Theorem 2.** On the entire horizontal line segment
\[
                            [0,1]+2ih,
 \tag{18}
\]
the real part of the original reduced phase has its unique
maximum at \(z_*\). It strictly increases before that point
and strictly decreases afterward. The maximum is nondegenerate.
Every closed subset of (18) outside a neighborhood of \(z_*\)
has a strictly positive gap from \(\Re\phi(z_*)\).

*Proof.* Since \(1/6<\xi\), the threshold \(1-2\xi\) is
less than \(2/3\), while \(\Re z_*>2/3\). Lemma 1 gives
positive first derivative to the left of the threshold.
On the remaining interval the first derivative is strictly
decreasing by (17), and it equals zero at \(z_*\) by (3).
Its sign is therefore positive before that point and negative
afterward. The strict second derivative there proves
nondegeneracy. Because \(2h>0\), the original global upper
primitive is regular at both endpoints in (18), and the
phase is continuous on that closed segment. Compactness gives
the last assertion. \(\square\)

The same conclusion persists for equal endpoints in a sufficiently
small complex neighborhood of \(x_0\), on the horizontal segment
through their continued critical total index. The strict parameter
bounds (7), the original zero lift, and the critical-point location
persist there; (8) and (17) therefore give the same argument.
This statement keeps the two external endpoints equal.

## 4. Agreement with the joint Gaussian normalization

Define the second derivative of the inner phase at its midpoint by
\[
 \mu(z)=
 \left.\frac{\partial^2}{\partial a^2}
                  F(a,z-a;x_0,x_0)\right|_{a=z/2}
 =2\pi\left\{\cot\bigl(\pi(z/2+x_0)\bigr)
                         -2\cot(\pi z/2)-i\right\}.
 \tag{19}
\]
At the symmetric critical point, let \(\lambda_-\) and
\(\lambda_+\) be the antisymmetric and symmetric Hessian
eigenvalues from the critical-corridor theorem. Then
\[
       \mu(z_*)=2\lambda_-,\qquad
       \phi''(z_*)=\frac{\lambda_+}{2},\qquad
       \mu(z_*)\phi''(z_*)=\det F''(a_*,a_*).
 \tag{20}
\]
Both \(-\mu(z_*)\) and \(-\phi''(z_*)\) have positive real
part. Thus iterating their two Gaussian integrations gives
exactly the same coefficient and square-root branch as the
joint Gaussian, with no missing density or factor of two.
The row has power \(N^{-3/2}\); an inner sampled Gaussian
has power \(N^{-1}\) after its first lattice density, and
the remaining density and Gaussian give the final power
\(N^{-1/2}\).

This is a consistency statement for the original phase and
normalization. Theorem 2 bounds a one-variable phase, not the
original finite sum by itself. To use it for that sum requires
a complete inner-source estimate at the relevant complex total
indices, followed by an exact outer summation contour with
all its corrections controlled. None of those corrections is
removed by a phase comparison.
