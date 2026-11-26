# The remaining small-angle upper rows reduce to the half-row endpoint

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This note closes a missing scalar source region. It retains the same
height and original orientation, so its conclusion feeds directly into
the already certified right-core profiles at the other angle \(.13\).
It does not by itself prove the global mixed-word source theorem.

## 1. Statement with the complete row and Fourier weights

Use the notation \(I_h,J,\nu_h\) of the
[whole-period endpoint source](research_mixed_all_endpoint_support.md).
Let \(\epsilon,\beta,c\in\{0,1\}\), and keep the actual normalized
Fourier weight:
\[
 \begin{split}
 E(u,y)={}&I_0(u,1/2)+I_h(u,y)-(2+\epsilon)J(u)-2\pi chu\\
 &+\frac\beta2\{\max(\nu_h(y),2\pi h_+)-2\pi\sigma h\}
       -\kappa y .
 \end{split}                                                       \tag{1}
\]
Here \(c=1\) means that the other variable is the first original
argument. The selected normalization \(\sigma\) is kept literally;
it is independent of the row and angle derivatives below.

**Theorem 1.** For every \(|h|\le3/100\) and \(\kappa\le1/4\),
\[
 \max_{\substack{1/2\le u\le1\\0\le y\le13/100}}E(u,y)
       =E(1/2,13/100).                                          \tag{2}
\]
In particular, this applies to all six source-type combinations and
all slopes in \([-1/5,1/4]\). There is no change in height in (2).
Every original row remains in the inequality; no cancellation-only
endpoint identity is used.

## 2. The near half-row strip

Write \(L_h(v)=\log|1-e^{2\pi h-2\pi iv}|\). On either analytic
Fourier branch, the weight is independent of \(u\). For
\(1/2<u\le3/5\), \(0\le y\le13/100\),
\[
 \begin{split}
 E_u
 &=\log|2\cos\pi u|+L_h(u+y)
       -(2+\epsilon)\log(2\sin\pi u)-2\pi ch\\
 &\le \log(2\sin(\pi/10))
       +\log(2\cosh(3\pi/100))+3\pi/100
       -2\log(2\sin(2\pi/5))<-9/10 .
 \end{split}                                                       \tag{3}
\]
The bound uses
\(|1-e^{2\pi h-2\pi iv}|\le2e^{\pi h}\cosh(\pi h)\),
\(|(1-2c)h|\le|h|\), and the positivity of
\(\log(2\sin\pi u)\) on this strip. The singular endpoint at
\(u=1/2\) is handled by continuity of the integrated phase.

At \(u=1/2\), every Fourier branch \(q\in\{0,\beta\}\) has
\[
 E_y=L_h(y+1/2)-(1+q/2)L_h(y)-\kappa .                         \tag{4}
\]
The modulus in \(L_h(y)\) is less than one throughout the stated
rectangle. Its square is convex in \(e^{2\pi h}\), so the two
height endpoints and \(y=13/100\) suffice. At the positive height
endpoint its square is less than \(.805\), and the other endpoint
is smaller. Thus the extra \(-qL_h(y)/2\) is favorable. Put
\(C=\cosh(3\pi/50)\), \(d=\cos(13\pi/50)\). The ratio of the
remaining moduli is minimized at the maximal height and angle:
\[
 E_y\ge\frac12\log\frac{C+d}{C-d}-\frac14>\frac12 .           \tag{5}
\]
Equations (3)--(5) first move the row to \(1/2\), then the angle
to \(13/100\), at exactly the same height. They apply separately
to both Fourier branches, and therefore to their maximum.

## 3. A universal far-row comparison

Put \(H=|h|\), \(G_H(v)=\Re g(v-iH)\). Subtract the value of
each branch at \((1/2,13/100)\) from its value at \((u,y)\).
For \(u\ge3/5\), the difference is bounded above by
\[
 \begin{split}
 D(u,y,H)={}&J(u+1/2)+G_H(u+y)-G_H(63/100)\\
 &-G_H(y)+G_H(13/100)-2J(u)\\
 &+2\pi H(u-1/2)+\tfrac14(13/100-y).
 \end{split}                                                       \tag{6}
\]
Here and below \(J\) is extended periodically when its argument
exceeds one. To verify (6), note the following signs:

* \(J(u)\ge0\) on \([1/2,1]\), so the extra own-type term
  \(-\epsilon J(u)\) can be dropped.
* The extra branch terms must be combined, including the positive-height
  reflection term. Their exact sum is
  \[
  -\frac q2[G_H(y)-G_H(13/100)]
       +q\pi h_+(13/100-y)
   =-\frac q2[\Re g(y+ih)-\Re g(13/100+ih)]\le0.
  \]
  The inequality uses \(L_h(y)<0\) for both signed heights, proved
  above, so the signed-height primitive decreases on this entire interval.
  Monotonicity of \(G_H\) alone would not justify dropping the two
  positive-height terms separately.
* The row-height coefficient is
  \(2\pi(h_+-ch)\in[0,2\pi H]\), and \(u-1/2\ge0\).
* \(\kappa(13/100-y)\le(13/100-y)/4\).

All constants independent of \(u,y\), including the selected alias
normalization, cancel in this subtraction. These observations prove
(6) for every combination in Theorem 1, without choosing its active
Fourier branch.

**Lemma 2.** On the entire closed box
\[
 (u,y,H)\in[3/5,1]\times[0,13/100]\times[0,3/100],
             \qquad D(u,y,H)<-1/20 .                            \tag{7}
\]

The accompanying exact interval certificate proves (7) on 1,392
dyadic boxes. The independent 256-bit reflected-row replay passes on
2,557 boxes after 1,165 exact refinements. Both checks also verify the
branch-subtraction identity and six scalar margins. Its simple natural
interval bound uses the exact
ranges of \(J\) and the complex dilogarithm ranges of \(G_H\).
The only real critical points required for a \(J\)-range are the
integer translates of \(1/6,5/6\), in addition to the endpoints.
The interval boxes include the original singular rows and the line
\(u+y=1\); they are not discarded.

For completeness, the fallback at a logarithmic zero is analytic,
not a numerical convention. The absolutely convergent Fourier series
gives uniformly in real \(v\)
\[
 |G_H(v)-J(v)|
 \le\omega(H):=\frac{\pi^2/6-
                  \operatorname{Li}_2(e^{-2\pi H})}{2\pi},
       \qquad \omega(H)\longrightarrow0 .                     \tag{8}
\]
Indeed the absolute sum of the changed Fourier coefficients is
\(\sum_{k\ge1}(1-e^{-2\pi kH})/(2\pi k^2)\). If a direct
complex interval contains the branch point, a \(J\)-range enlarged
by \(\omega(H_{\rm upper})\) is used instead. Exact dyadic coverage
and a strict upper comparison with \(-1/20\) are required on every
accepted box. The independent replay uses the opposite-frequency
primitive and the same proved zero bound, with exact refinements if
needed. This proves Lemma 2.

Combining (7) with the near-row argument proves Theorem 1.

## 4. The actual graph tapers and finite-source consequence

For a type-three target the full height interval is \([-.03,.02]\).
For a type-four target on the old or new taper and \(0\le y\le.13\),
\[
 \begin{cases}
 -.057(y/.22)^2\le h\le-.02(y/.25)^2,&\sigma=0,\\
 .014(y/.25)^2\le h\le.014(y/.22)^2,&\sigma=1.
 \end{cases}                                                       \tag{9}
\]
All these heights have absolute value less than \(.03\). At the
fixed comparison angle \(.13\), the resulting heights lie in
\[
 [-.057(.13/.22)^2,0]\quad\hbox{or}\quad
 [0,.014(.13/.22)^2],                                            \tag{10}
\]
respectively. These are precisely included in the degenerate
\(y=.13\) source profiles of the
[right-core support theorem](research_mixed_right_core_support.md).
It is not necessary that the comparison height itself lie on one
chosen graph at \(y=.13\); the certified profile includes it.

Uniform finite-product estimates turn (2) into an upper bound for
the absolute sum of all original rows \(j/N\ge1/2\), up to the
usual polynomial prefactor and arbitrarily small Fourier-envelope
error. Thus the actual finite-source region with other angle below
\(.13\) reduces to a source profile already available in the
geometric comparison, for both parities and orientations. This
statement neither changes the source polynomial nor infers any
uncertified geometric or remaining exterior comparison.

Reproduction:

    python3 experiments/certify_mixed_small_angle_high_rows.py --precision 192
    python3 experiments/replay_mixed_small_angle_high_rows.py --precision 256
