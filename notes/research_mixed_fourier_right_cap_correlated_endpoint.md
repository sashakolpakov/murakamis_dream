# The correlated scalar endpoint of the literal Fourier right cap

Research deduction, 7 November 2026. The last Fourier critical
equation determines its outgoing leg by one quadratic with a unique
root inside the unit disk. Together with one rational backward
formula, this gives an exact filtered parametrization of every
actual last-four reference. It is stronger than treating that leg
as an arbitrary point of the full type-four disk. It requires no
new root computation or reference cover.

This is a critical-reference theorem. The whole finite right cap
still needs a source bound; neither an exponential equation nor
the auxiliary inverse leg is substituted into that finite function.

## 1. The original source and equations

Retain the [literal Fourier right cap](research_mixed_fourier_ended_boundary_windows.md),
equations (5) and (9). With \(r=e^{-2\pi i/N}\),
\(P_j=(r;r)_j\), \(p_j(X)=(rX;r)_j\), \(Y=e^{2\pi iy}\)
and the original cardinal scalar \(c_y\), it is exactly
\[
 V_N^{\rm F}(y,X)
 =c_y\sum_{\substack{j,\ell\ge0\\j+\ell<N}}
 \frac{X^{-j}p_j(X)P_{j+\ell}Y^\ell}
 {P_j^3P_\ell(Y;r)_{\ell+1}}.
 \tag{1}
\]
Every apparent output pole retains its original removable
continuation. In particular the outgoing four halfweight has
already canceled in this identity.

For a fixed incoming leg \(a\), the two-index action is
\[
 Q_1(s;a,q)+\ell_q(y),\qquad
 Q_1=g(a+s)+g(s+q)-3g(s)-g(a)-g(q)+2\pi ias .
 \tag{2}
\]
Its incoming allocated version subtracts \(\eta g(a)/2\).
Use the original primitives and lifts throughout.
At \(y=x_0\), put
\[
 Y=K,\quad A=e^{-2\pi ia},\quad
 S=e^{-2\pi is},\quad Q=e^{-2\pi iq}.
 \tag{3}
\]
The inherited bounds are
\[
 3/5<|Y|<5/8,\qquad
 7/40<\Re x_0<3/16 .
 \tag{4}
\]
The completed boundary update and ordinary bidisk maps give a
unique critical point for every \(a\in K_3\) or \(K_4\).
Both \(s,q\) lie in the original ordinary type-four image
\[
 O_4=\{|z-(.30-.052i)|\le .060,\quad
                     -.102\le\Im z\le-.001\}.
 \tag{5}
\]
Here \(K_3,K_4\) are the original
[typed source domains](research_mixed_typed_last_row_envelopes.md),
not newly enlarged products. Existence and uniqueness are those
of Section 3 of the Fourier boundary-window theorem. The role of
this last vertex is ordinary even when it is adjacent to a first
cap; a private first-cap leg is not substituted for \(s\).

Exponentiating the two equations in (2) gives exactly
\[
 \begin{split}
 (1-AS)(1-SQ)&=A(1-S)^3,\\
 YQ^2+Q(YS-Y-1)+(1-Y)&=0 .
 \end{split}
 \tag{6}
\]
The second equation follows from
\(Y(1-SQ)=(1-Q)(1-YQ)\), including the original cardinal
chirp in \(\ell'_q\).

## 2. The unique inside root and the backward input

Set \(c=Y^{-1}-1\). The second equation of (6) is
\[
             Q^2-(1+Y^{-1}-S)Q+c=0.
 \tag{7}
\]
One has \(|c|>1\): since
\(\cos(2\pi\Re x_0)<1/2\),
\[
 |c|^2-1
 =\frac{1-2|Y|\cos(2\pi\Re x_0)}{|Y|^2}>0 .
 \tag{8}
\]
At an actual reference \(|Q|<1\), by (5). The other root
is \(c/Q\), whose modulus is greater than one. Consequently
the actual \(Q\) is the unique root of (7) inside the unit disk.
The roots cannot coincide there. This selection is analytic on
a neighborhood of the actual compact image of \(S\), with no
choice of an independently evaluated square-root branch.

Conversely, the outgoing exponent determines both other exponents:
\[
 \begin{split}
 S(Q)&=1+Y^{-1}-Q-\frac{Y^{-1}-1}{Q},\\
 A(Q)&=\frac{1-S(Q)Q}
 {S(Q)(1-S(Q)Q)+(1-S(Q))^3}.
 \end{split}
 \tag{9}
\]
The denominators are nonzero on actual references. For the first
one this follows from \(Q\ne0\); for the second use (6),
\(A\ne0\), and \(|SQ|<1\).

There are useful necessary restrictions before any domain test.
For example (5) implies
\[
 |S|<1,\quad \Im S<0,\quad
 \Re S<1/16,\quad
 \Re S+\frac1{15}\Im S<0 .
 \tag{10}
\]
Indeed \(.24\le\Re s\le.36\) and \(\Im s\le-.001\), so
\[
 \Re S\le e^{-\pi/500}\sin(\pi/50)
 <\frac{\pi/50}{1+\pi/500}<\frac1{16}.
\]
The last inequality follows from \(159\pi<500\), using
\(\pi<22/7\).
The last bound follows from
\(\tan(\pi/50)<1/15\): use
\(\tan u\le u/(1-u^2/2)\) and \(\pi<22/7\).
These are necessary half-plane constraints, not a replacement for
the full typed image (5).

## 3. The filtered image has the original zero lifts

Define a filtered set of \(Q\)'s as follows. Decode \(q\) and
\(s\) from \(Q\) and (9), using their principal logarithms
\(z=-\Log(e^{-2\pi iz})/(2\pi i)\), and require both to
belong to (5). Decode \(a\) from \(A(Q)\) by the same branch,
and require \(a\in K_\alpha\), for \(\alpha=3\) or \(4\).
Retain all these conditions simultaneously.

Every point of this filtered set solves the original equations,
not merely their exponentials. Here is an explicit lift check.
All factors in the following logarithms have positive real part.
For the own type-four legs,
\[
 0<\arg(1-S),\arg(1-Q)<13\pi/50,
 \qquad
 -11\pi/50<\arg(1-SQ)<\pi/50 .
 \tag{11}
\]
These follow by moving the radius of the exponential from zero
to a value less than one with its angle fixed. Also
\[
                   -\pi/2<\arg(1-AS)<\pi/2 .
 \tag{12}
\]
For (12), \(\Re(a+s)\in[.48,.793]\) and
\(\Im(a+s)\le.067\). If the cosine is positive, it is less
than \(\cos(2\pi/5)<1/3\), while the radius is less than
\(e^{.14\pi}<2\). Thus \(\Re(1-AS)>1/3\).
This also verifies the original strip and branch; it does not
replace a continued logarithm by a favorable lift.

Because \(.24\le\Re a\le.433\), the original first residual
satisfies
\[
 -51\pi/50
 <\Im\{g'(a+s)+g'(s+q)-3g'(s)+2\pi ia\}
 <693\pi/500 .
 \tag{13}
\]
Its exponential is one by (6); the only multiple of \(2\pi i\)
in this strip is zero.

For the second residual, \(YQ\) is in the lower half-plane and
\(|YQ|<5/8\). The disk centered at \(1\) of radius \(5/8\)
lies strictly inside the sector of arguments between
\(-\pi/4\) and \(\pi/4\), since \(5/8<1/\sqrt2\).
Hence \(0<\arg(1-YQ)<\pi/4\), and
\(\Im\Log Y=2\pi\Re x_0\in(7\pi/20,3\pi/8)\).
Together with (11), this yields
\[
 -19\pi/50
 <\Im\{g'(s+q)-g'(q)+\Log Y-\Log(1-YQ)\}
 <79\pi/200 .
 \tag{14}
\]
Equation (6) again forces its original value to vanish.
The inequalities used in (11)--(14) hold throughout the stated
filtered products, so this argument does not assume a path to
the alternating reference.

The original strong Hessian uniqueness now identifies every
filtered point with the canonical last-four point for its decoded
incoming \(a\). Conversely every such canonical point passes the
filters. Thus (9) is an exact description of the actual family,
including its incoming marginal and absolute action (2).

The parametrization is locally unramified. Write \(F=Q_1+\ell\)
and let \(H=F_{(s,q)(s,q)}\). On the canonical family,
\[
 \frac{dq}{da}=\frac{F_{sq}F_{sa}}{\det H}\ne0,\qquad
 F_{sq}=\frac{2\pi iSQ}{1-SQ},\quad
 F_{sa}=\frac{2\pi i}{1-AS}.
 \tag{15}
\]
The denominator is nonzero by accretivity, and the two numerator
factors are nonzero. Global injectivity of the outgoing coordinate
on each incoming family follows from (9) and the unique decoding
of \(a\). These statements concern the already existing branch;
they do not assert that every \(s\in O_4\) supplies a feasible
incoming \(a\).

## 4. What the failed independent disk test does and does not say

The fixed saved test
[boundary-domain record](../repro/results/research-mixed-fourier-boundary-k3-saved-domain.json)
has SHA-256
\(04e00eb7d04878b1f4d8092a7271786c8363a83a1efebf1a9e1284148be8c219\).
It disproves \(\beta_K(D_4)\subset K_3\) on the independent
full disk. Its first lower-height violation is arc 107 and
its first slanted-side violation is arc 153 of the fixed 512
arc cover. No test is repeated here.

Those two particular arcs cannot contain an actual outgoing leg.
On either arc the original angle belongs to
\([\pi/3,2\pi/3]\), so a boundary point of the original disk
\(q=.30-.052i+.064e^{i\theta}\) has
\[
 \Im q\ge-.052+.064\,\frac{\sqrt3}{2}
                =\frac{8\sqrt3-13}{250}>0 .
 \tag{16}
\]
The last inequality is \(192>169\). This contradicts (5).
This explicit exclusion does not dispose of every violating
arc or prove the desired containment on the actual filtered
image. That stronger implication remains unproved.

## 5. The still missing whole-source comparison

The complete ordinary \(C_1\) theorem can only be imported when
its actual external inputs satisfy its typed source hypotheses.
The new description (9)--(15) keeps precisely the correlation
that an independent \(D_4\) test discards. It does not yet prove
that the auxiliary exterior leg \(\beta_K(q)\) is in \(K_3\).

There is a second, distinct allocation issue. The published
complete conditional plane includes the outgoing halfweight.
At profile level, removing that allocation adds
\(\Re g(q)/2\); one may not divide a finite \(d_N\) factor.
If \(\delta q\) is a horizontal displacement, its bare bound
therefore contains the extra term
\[
 \frac12\Re\{g(q)-g(q_*)-g'(q_*)\delta q\}.
 \tag{17}
\]
After multiplication by the outgoing cardinal profile, the
corresponding curvature is that of
\(\Re[g(q)/2+\ell_q(x_0)]\), not that of \(\ell_q\)
alone. The correct bare main phase (2) is strictly concave, but
the small published complete-source quadratic loss cannot
silently be replaced by that stronger main-phase curvature.

Thus a right-end completion still needs either a direct complete
bound for (1), or a justified full-profile allocation retaining
enough bare curvature. The exact parametrization here supplies
the actual reference family for that problem. It proves neither
that remaining inequality nor a finite quantum noncancellation
or whole-word estimate.
