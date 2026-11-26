# Quantitative rate budget for a protected cap and its complete star

This note concerns the original marked source at cap spectrum \(+2\) and
all other crossing spectra \(-2\). It keeps every shared face variable,
the two protected zero variables, and every original coefficient target.
It gives a computable sufficient inequality and a limitation of one
specific four-term moment estimate. It does not give an absolute source
gap or a filled-volume theorem for the 54-circle example.

## 1. The unchanged coefficient problem and normalization

Let the protected cap have ordinary faces \(A,C\). Its original finite
polynomial is
\[
 H_{\mathrm{cap}}(A,C;2)=\sum_{j=0}^{M}(-1)^jU_{N,j}A^{d-j}C^j,
 \qquad d=N-1,\quad M=\lfloor N/2\rfloor-1.                         \tag{1}
\]
Let \(P_N(A,Y)\) be the product of all complete crossing factors incident
to \(A\), after the cap is removed. The remaining shared variables are
denoted by \(Y\), including \(C\). The coefficient of \(A^d\) is retained
as a single contraction. All other original targets are extracted only
after this contraction.

Fix positive shared radii \(L\), with \(L_A=L_C\), and leave the protected
radii exactly zero. Write \(P_N^+\) for the same product at positive face
arguments and endpoint spectra. Its radial pressure is
\[
 F(t)=\lim_{N\to\infty}\frac1N
       \log P_N^+(L_Ae^t,L_Y),\qquad f(t)=F(t)-F(0).               \tag{2}
\]
The complete triangle formula supplies this limit at each finite real
\(t\); in particular \(f\) is convex and \(f(0)=0\).
The relative-star hypotheses include
\(0<\nu=f'(0)<1/2\).

The global weighted cap-sector bound at these same radii has rate
\(G(L)\). In the present one-cap problem it is
\[
 G(L)=\sum_{\text{triangles outside the cap}}Q(L_i,L_j,L_k)
       +\log L_A-\sum_{\text{ordinary }v}\log L_v.                \tag{3}
\]
Here \(Q\) is the original half-triangle pressure:
\[
 Q(w)=\max_{\substack{\alpha_i\geq0\\\sum_i\alpha_i=1/2}}
 \left\{\sum_i f_{\mathrm{tri}}(\alpha_i)+\sum_i\alpha_i\log w_i\right\},
 \quad
 f_{\mathrm{tri}}(a)=
 \frac{\Lambda(\pi a)+\Lambda(\pi/2-\pi a)}{\pi}.                  \tag{4}
\]
A zero weight forces its allocation to be zero. The function
\(f_{\mathrm{tri}}\) in (4) is distinct from the radial increment \(f\) in (2).

Let \(\Phi\) be the original complete source action. Its geometric
normalization is
\[
                         \operatorname{Vol}(Y)=2\pi\Phi.         \tag{5}
\]
Thus the excess to overcome is \(G(L)-\Phi\), in source-rate units.
No new choice of coefficient targets or independently optimized face
radii is permitted when the local improvement is inserted into (3).

The exact inputs are the original triangle entropy formula, the cap
moment representation, and Section 9 of
\(\texttt{research_cap_cross_shared_star_spectral_gap.md}\).
The constrained-cap identity in
\(\texttt{research_cap_constrained_capacity_budget.md}\) explains why
\(G(L)\) can exceed \(\Phi\): at a finite common-weight cap stationary
point its value is the cap-sector capacity.

## 2. A quantitative form of the existing moment estimate

There is a positive random variable \(X_N\) such that
\[
 U_{N,j}=U_{N,0}\mathbb E X_N^j\quad(0\leq j\leq d),\qquad
 U_{N,0}=O(N^2),\qquad
 \mathbb E X_N^d=N^2\sin^2\frac{\pi}{2N}\leq\frac{\pi^2}{4}.       \tag{6}
\]
Only these finite moments are used. In particular the full untruncated
star polynomial, whose degree may exceed \(d\), is never integrated
against this law.

Suppose the actual angular estimate, uniform in all remaining face
phases, gives on \(1-\delta_0\leq x\leq1+\delta_0\)
\[
 |P_N(-L_Ax,Y)|
 \leq \operatorname{poly}(N)e^{-\gamma N}P_N^+(L_Ax,L_Y).         \tag{7}
\]
For \(0<\delta<\min(1,\delta_0)\) and \(t>\log(1+\delta)\), the original
finite four-term estimate has limiting losses
\[
 \begin{aligned}
 \eta_1&=-f(\log(1-\delta)),\\
 \eta_2&=\tfrac12\log(1+\delta),\\
 \eta_3&=\gamma-f(\log(1+\delta)),\\
 \eta_4&=\tfrac12\{t-\log(1+\delta)\}-f(t).
 \end{aligned}                                                  \tag{8}
\]
The exact finite cap cutoffs are \((d-M)/N\to1/2\) and
\((M+1)/N\to1/2\), at both parities. Polynomial factors have zero rate.

If verified bounds on (2), (3), (7), and the original \(\Phi\) establish
\[
                  \eta:=\min_i\eta_i>G(L)-\Phi,                  \tag{9}
\]
then the contracted cap sector at these fixed spectra has a strict
absolute exponential gap below \(\Phi\), uniformly in all remaining
face phases. Indeed, multiply the contracted estimate by the unchanged
exterior, and perform one Cauchy extraction with the same radii and
targets as in (3). Its resulting rate is at most \(G(L)-\eta<\Phi\).

This is a finite-dimensional sufficient certificate. Upper enclosures
for \(f\) and \(G\), a lower enclosure for \(\gamma\), and a lower
enclosure for \(\Phi\) suffice. The fixed-spectrum moment argument by
itself does not establish (9) on a spectral neighborhood. The separate
analytic-antidifference proof in the star theorem gives such a
neighborhood with another quantified loss; one must retain its window
endpoints and connecting contours. A full filling argument also needs
the relevant complete spectral remainder, not only this one sector.

## 3. A ceiling intrinsic to this four-term estimate

Define the positive radial cutoff cost
\[
             K_{1/2}=\sup_{t\geq0}\{\tfrac12t-f(t)\}.             \tag{10}
\]
Then every choice allowed in (8) satisfies
\[
 \eta_2+\eta_4=\tfrac12t-f(t)\leq K_{1/2},
 \qquad
                         \eta\leq\tfrac12K_{1/2}.                \tag{11}
\]
This elementary restriction does not involve \(\gamma\).
Consequently better angular estimates alone cannot make (8) certify
an excess larger than \(K_{1/2}/2\).

If \(f'\) is strictly increasing, \(f'(0)<1/2\), and \(f'\) eventually
exceeds \(1/2\), the unique \(t_*>0\) with \(f'(t_*)=1/2\) gives
\[
 K_{1/2}=\frac{t_*}{2}-f(t_*)
        =\int_0^{t_*}\left(\frac12-f'(u)\right)\,du.              \tag{12}
\]
This can be evaluated directly from the finite classical star. It is
not the Schur-complement pressure obtained after extracting the other
ordinary faces. Those two pressures have different cutoff costs.

The assertion is a limitation of estimate (8), not a lower bound for
the original signed contraction. It does not exclude sharper use of
the moment distribution, coherent control of the omitted polynomial
tail, or an estimate after the other original targets have been
extracted.

## 4. The literal star of the 54-circle example

In the published rational obstruction, the protected vertices are
\(29,50\), and the selected left quartet is \((0,50,16,29)\).
Use
\[
 A=16,\quad C=0,\quad Z=41,\quad W=44,\qquad
 L_A=L_C=a,\quad r=L_Z/a,\quad s=L_W/a.                           \tag{13}
\]
After the cap is removed, the three triangles containing \(A\) are
\[
                   (Z,C,A),\quad(Z,A,W),\quad(29,W,A).            \tag{14}
\]
The last has its protected coordinate zero. Every other original
triangle contributes a constant to the pressure when only \(A\) is
scaled. Homogeneity cancels \(a\), and hence
\[
 \begin{aligned}
 f'(t)=\nu(t)=\frac1\pi\bigg[
  &\arctan\frac{e^t}{\sqrt{e^t+r+re^t}}
  +\arctan\frac{e^t}{\sqrt{re^t+se^t+rs}}\\
  &+\arctan\sqrt{\frac{e^t}{s}}\bigg].
 \end{aligned}                                                  \tag{15}
\]
This is the exact complete-triangle derivative, including the
protected zero. It follows either by differentiating (4) at its
maximizing loads or from the positive triangle Hessian.

There is a useful exact radius-box obstruction to (9).
Suppose
\[
                         0<r\leq4,\qquad0<s\leq9,               \tag{16}
\]
and retain the applicability condition \(\nu(0)<1/2\).
Each summand in (15) decreases when \(r\) or \(s\) increases.
At \(r=4,s=9,t=0\) its three tangent arguments are
\(1/3,1/7,1/3\), whose arctangent sum is exactly \(\pi/4\).
Therefore \(\nu(0)\geq1/4\).

At \(t=\log4\) the three tangent arguments are at least
\[
                   \frac4{\sqrt{24}}>\frac45,\qquad
                   \frac4{\sqrt{88}}>\frac25,\qquad
                   \frac23.
\]
Their pairwise-product sum is greater than
\[
                \frac8{25}+\frac8{15}+\frac4{15}
                =\frac{28}{25}>1.
\]
The sum of three positive arctangents is thus greater than \(\pi/2\),
so \(\nu(\log4)>1/2\). Strict convexity gives \(0<t_*<\log4\), and
(12) yields
\[
 K_{1/2}<\frac{\log4}{4},\qquad
             \eta<\frac{\log2}{4}<\frac15.                       \tag{17}
\]
The last inequality follows already from
\(e^{4/5}>1+4/5+(4/5)^2/2>2\).

The exact rational obstruction proves that the same cap-sector
capacity is greater than \(\Phi+1/5\). Therefore every shared positive
weight vector has \(G(L)>\Phi+1/5\). In particular, for every weight
vector in (16) to which the star theorem applies, the four-term losses
cannot satisfy (9). This statement does not assume that the true
stationary radii have been certified to lie in (16).

## 5. Numerical location, separated from the proof

The parent's stationary exterior locator gives approximately
\[
 r=3.2079293385,\quad s=7.7900679949,\quad \nu(0)=0.2741093817.
\]
Integrating the explicit derivative (15), with no further optimization
of the exterior, gives
\[
 t_*\simeq1.0907454390,\quad K_{1/2}\simeq0.1304979129,\quad
 K_{1/2}/2\simeq0.0652489564.                                    \tag{18}
\]
The located capacity excess is approximately \(0.205572838\).
These floating-point values guide the comparison; they do not certify
the stationary point or its placement in (16). The proof of the
conditional radius-box obstruction is entirely (13)--(17).

The conclusion is therefore specific and quantitative: the existing
four-term moment/star bound has too small a guaranteed budget on this
whole explicit radius box. The original negative-axis polynomial
after all remaining targets are extracted retains information that
this fixed-radius star estimate discards. That globally conditioned
route remains a separate problem.

