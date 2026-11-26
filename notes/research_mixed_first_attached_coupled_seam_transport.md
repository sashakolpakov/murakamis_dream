# A positive coupled first-boundary derivative near the real seam

Research deduction, 7 November 2026. When the first ordinary
neighbor has own type four, the regular first-boundary profiles
have a strictly positive derivative at the physical minimum seam,
including both incidences of the neighbor's changing height.
The true last row of that ordinary factor has a positive coupled
derivative too. These inequalities persist on a fixed open
first-minimum collar.

The following ordinary factor is represented by its original
regular profile on the stated index rectangle. Its independent
finite-source eligibility is retained as a hypothesis of an
application. No complete following-factor tail bound or calibrated
boundary sign is inferred.

## 1. Actual coefficients and the coupled derivative

Use the notation and exact allocation of
[the two-incidence reduction](research_mixed_first_attached_two_incidence_reduction.md).
The first cap has own type \(3+\alpha\); its ordinary neighbor
has own type four. Keep the actual first-minimum coefficients
\[
 \begin{gathered}
 a=x-i\lambda_a(x-.1),\qquad
 b=z-i\lambda_b(x-.1),\qquad x\le z\le.5,\\
 0\le\lambda_b=-c_bR(z)/.12\le17/20,\\
 -7/40\le\lambda_a\le3/5\quad(\alpha=0),\qquad
 1/6<\lambda_a<13/20\quad(\alpha=1).
 \end{gathered}                                                \tag{1}
\]
The own-four first coefficient is the actual unattenuated
attached one, with \(-.078<c_a<-.020\).
It uses the coupled reference theorem for \(m\ge3\).
The neighbor has the original ordinary height
\(-.102<c_b<-.001\), with its original upper cutoff \(R(z)\).
Both its actual height and derivative coefficient use the same
\(\lambda_b\).
The first real coordinate supplies the minimum in both affected
cutoffs; in particular the next retained real coordinate is at
least \(x\). A neighbor frozen by a smaller third coordinate is
not assigned the active height derivative in (1).

There must be a following ordinary factor for the second
incidence written here. This holds, for example, for Fourier-ended
prefixes of length at least three and for ordinary-ended words
of length at least four. A following endpoint cap or the literal
Fourier endpoint itself has a different derivative and is not
silently substituted.

For the first ordinary index and the following regular index write
\[
 s=v+i\eta,\quad .22\le v\le.49,\quad -.108\le\eta\le0,
 \qquad
 t=w+i\zeta,\quad .22\le w\le.49,\quad -.108\le\zeta\le.068 .
                                                               \tag{2}
\]
The full derivative on regular profiles is exactly
\[
 \begin{split}
 \mathcal H={}&\Re[(1-i\lambda_a)D_a-i\lambda_bD_b],\\
 D_a={}&g'(e+a)+g'(s+a)-(2+\alpha)g'(a)+2\pi is,\\
 D_b={}&g'(s+b)+g'(t+b)-3g'(b)+2\pi it .
 \end{split}                                                  \tag{3}
\]
The real private cap interval is \(e\in[.27,.49]\) for
own three, and may be restricted to \(e\in[.27,.4]\)
for own four by the
[private-index barrier](research_mixed_first_four_private_index_barrier.md).
The complete cap true-end exponents are absorbed on the actual
early taper by the original own-four theorem and the
[new own-three payment](research_mixed_first_three_early_endpoint_payment.md).
Thus no cap endpoint alternative is omitted from this regular
profile calculation.

We first prove inequalities at \(x=.1\), where \(a=.1\)
and \(b=z\) have real height zero. Proposition 1 of the
two-incidence reduction permits raising \(\eta\) to zero,
with a favorable margin, while retaining all of \(D_b\).

## 2. A uniform lower bound for the entire neighboring force

Let \(A(y,r)=\arg(1-re^{-2\pi iy})\) on the original lift,
and put \(R=e^{2\pi\zeta}\). At the seam and \(\eta=0\),
\[
 \Im D_b
 =\pi(-1-v+2z+2w)+A(w+z,R).                                 \tag{4}
\]
If \(w+z\ge1/2\), the original radial argument bound
\(A(w+z,R)\ge\pi(1-2w-2z)\) gives
\[
                              \Im D_b\ge-\pi v.              \tag{5}
\]

If \(w+z<1/2\), its sine is positive, so \(A\) increases
with \(R\). It is bounded below by its value at
\(R_-=e^{-.216\pi}\). For this radius, the derivative of
\[
                         2\pi y+A(y,R_-)
\]
is \(2\pi(1-R_-\cos2\pi y)/(1+R_-^2-2R_-\cos2\pi y)>0\).
Hence the minimum in this second case is at \(w=.22,z=.1\).
At that point,
\[
 A(.32,R_-)>\frac7{20}.                                     \tag{6}
\]
Here is an elementary witness, retaining the original argument.
The positive atanh series gives
\[
 \log2>2(1/3+1/81+1/1215)=842/1215>69/100,
\]
while \(.216\pi<594/875<69/100\). Thus \(R_->1/2\).
Also
\[
 \sin(.64\pi)=\cos(.14\pi)>9/10,\qquad
 \cos(.64\pi)=-\sin(.14\pi)>-11/25 .
\]
At radius \(1/2\), the argument tangent is consequently
greater than \(45/122>11/30\). Both real and imaginary parts
are positive. Finally
\[
 \arctan(11/30)>
       \frac{11}{30}-\frac{(11/30)^3}{3}
        =\frac{28369}{81000}>\frac7{20}.
\]
This proves (6).

Equations (4)--(6) establish, for the full following-height
range in (2),
\[
 \Im D_b>-\pi(v+9/25)+7/20 .
\]
The right side is negative. Multiplying by the actual
\(0\le\lambda_b\le17/20\) therefore gives the useful uniform
bound
\[
 \lambda_b\Im D_b>
       -\frac{17\pi}{20}(v+9/25)+\frac{119}{400}.             \tag{7}
\]
This pays neither incidence separately. Both are kept in (4).

## 3. Own-four regular profiles have slope greater than \(1/12\)

At real \(a=.1,s=v\), the original first gradient is
\[
 \begin{split}
 \Re D_a&=
 \log\frac{4\sin\pi(e+.1)\sin\pi(v+.1)}
                         {(2\sin(\pi/10))^{2+\alpha}},\\
 \Im D_a&=\pi(v-e-2\alpha/5).
 \end{split}                                                  \tag{8}
\]
For \(\alpha=1\), the imaginary expression is negative
throughout the reduced private rectangle.
Using \(\lambda_a\le13/20\) and (7), a lower bound for
\(\mathcal H\) is
\[
 L_1(e,v)-\pi\{v/5+13e/20+283/500\}+\frac{119}{400},
                                                               \tag{9}
\]
where \(L_1\) denotes the logarithm in (8).

This expression decreases with \(e\in[.27,.4]\):
its derivative divided by \(\pi\) is
\(\cot\pi(e+.1)-13/20<1/2-13/20<0\).
For an elementary bound, use
\(\cot(.37\pi)=\tan(.13\pi)<120/263<1/2\),
from \(.13\pi<5/12\), \(\sin u\le u\) and
\(\cos u\ge1-u^2/2\).
At \(e=.4\), expression (9) is concave in \(v\), so its
minimum is at \(v=.22\) or \(v=.49\).

The exact identity
\[
 (2\sin(\pi/10))^3=\sqrt5-2<6/25
\]
and the elementary bounds
\(\sin(.32\pi)>5/6\), \(\sin(.59\pi)>19/20\) imply
\[
              L_1(.4,.22)>\log(125/9)>13/5,\qquad
              L_1(.4,.49)>\log(95/6)>27/10.                 \tag{10}
\]
For the sine bounds use
\(\sin(.32\pi)=\cos(.18\pi)>41/49>5/6\) and
\(\cos(.09\pi)>1-(99/350)^2/2>19/20\).
The logarithm bounds follow from \(\log2>69/100\) and
\[
 \begin{split}
 \log(125/9)&=3\log2+\log(125/72)
                         >207/100+106/197>13/5,\\
 \log(95/6)&=3\log2+\log(95/48)
                         >207/100+94/143>27/10.
 \end{split}
\]
Here \(\log u>2(u-1)/(u+1)\) for \(u>1\).

At the two endpoints, (9)--(10) and \(\pi<22/7\) give
\[
 \mathcal H>
 \begin{cases}
 13/5+119/400-87\pi/100>457/2800,&v=.22,\\
 27/10+119/400-231\pi/250>187/2000,&v=.49.
 \end{cases}
\]
Both bounds exceed \(1/12\). Thus
\[
                 \mathcal H>1/12\qquad(\alpha=1,\ x=.1).
                                                               \tag{11}
\]

## 4. Own-three regular profiles have slope greater than \(1/10\)

For \(\alpha=0\), the lower expression from (7)--(8),
at fixed \(e,\lambda_a\), is concave in \(v\).
It suffices to bound its two endpoints, retaining both
signs of the actual \(\lambda_a\).

For all \(e\in[.27,.49]\), the elementary bounds
\[
 \sin\pi(e+.1)>\frac{183}{200},\qquad
 (2\sin(\pi/10))^2=\frac{3-\sqrt5}{2}<\frac{77}{200}
\]
give
\[
                            L_0(e,.22)>\log(610/77)>2 .
                                                               \tag{12}
\]
The sine bound follows from
\(\cos(.13\pi)>1-(143/350)^2/2>183/200\).
For the logarithm use \(\exp(1)<11/4\), hence
\(\exp(2)<121/16<610/77\).

At \(v=.49\), use additionally
\(\sin(.59\pi)>959/1000\). Then
\[
 L_0(e,.49)>
       \log(175497/19250)>\frac{11}{5}.                       \tag{13}
\]
Indeed
\(175497/19250>1704/187=8(213/187)\), with cross-product
difference \(15939>0\). Therefore
\[
 \log(175497/19250)>
     3\log2+2(213-187)/(213+187)>207/100+13/100.
\]

At \(v=.22\), the worst \(\lambda_a(v-e)\) is at
\(\lambda_a=3/5,e=.49\), and is at least \(-81/500\).
At \(v=.49\), it is at least
\(-(7/40)(.49-.27)=-77/2000\).
Equations (7), (12)--(13) give
\[
 \mathcal H>
 \begin{cases}
 2+119/400-131\pi/200>669/2800,&v=.22,\\
 11/5+119/400-761\pi/1000>1481/14000,&v=.49.
 \end{cases}
\]
Both are greater than \(1/10\). Consequently
\[
                 \mathcal H>1/10\qquad(\alpha=0,\ x=.1).
                                                               \tag{14}
\]
Raising the first ordinary index height in Section 1 was
conservative for both signs of \(\lambda_a\), so (11) and
(14) hold on the full first-index range (2).

## 5. The ordinary true-last-row alternative is paid too

Use the exact endpoint rate and first allocation of the
[true-last-row transport](research_mixed_first_attached_true_last_row_transport.md).
When the first ordinary row is replaced by its true endpoint
\(u=1\), the neighboring gradient in (3) becomes
\[
                   D_b^{\rm end}=g'(t+b)-2g'(b)+2\pi it .
                                                               \tag{15}
\]
The extra \(2\pi(h_b)_+\) has right derivative zero, since
the actual own-four neighbor moves into nonpositive height.
At the seam, the same two cases used in Section 2 give
\[
 \Im D_b^{\rm end}>
                -9\pi/25+7/20,\qquad
 \lambda_b\Im D_b^{\rm end}>
                -153\pi/500+119/400.                        \tag{16}
\]

For own three, the first-coordinate derivative of the regular
cap plus this row is greater than
\[
 \log\frac{2\sin\pi(e+.1)}{2\sin(\pi/10)}>1.                  \tag{17}
\]
The height term is nonnegative for either sign of
\(\lambda_a\), by the original rotated-ratio argument.
For the logarithm use
\(2\sin(\pi/10)<5/8\), so its ratio exceeds
\(366/125>11/4>\exp(1)\).
Adding (16) gives a coupled derivative greater than
\[
                 1+119/400-153\pi/500
                     >4701/14000>1/3.                      \tag{18}
\]
The former cap true-end alternative is already absorbed by the
actual own-three endpoint payment; it is not discarded merely
because (17) is favorable.

For own four, the first real logarithmic part exceeds
\[
 \log\frac{2\sin\pi(e+.1)}{(2\sin(\pi/10))^2}
                     >\log(366/77)>\frac32.                 \tag{19}
\]
The exponential witness is \(\exp(3/2)<19/4<366/77\),
using \(e^z\le1+z+z^2/[2(1-z/3)]\).
The original first imaginary gradient, including its endpoint
chirp, is \(\pi(8/5-e)\ge6\pi/5\).
With the unattenuated \(\lambda_a>1/6\), its contribution
exceeds \(\pi/5\). Together with (16), this yields
\[
 \mathcal H_{\rm end}>
       \frac32+\frac\pi5+\frac{119}{400}-\frac{153\pi}{500}
                >\frac{20501}{14000}>1.                     \tag{20}
\]
The own-four cap endpoint absorption applies as before.
The coefficient restriction in (1) is essential to (20).

## 6. A genuine first-minimum collar and its source scope

All original logarithmic arguments in these derivatives stay in
compact regular strips: their real parts range from \(.1\)
to at most \(.99\), and the fixed index heights are bounded.
The coefficients and real profile variables range over compact
closed enlargements of (1)--(2). The one-sided true-row height
term is continuous as a function of \(\lambda_a\), including
\(\lambda_a=0\).

Uniform continuity of the exact coupled derivatives therefore
gives a fixed \(\varepsilon>0\) such that, throughout the actual
first-minimum region
\[
                    .1\le x\le.1+\varepsilon,\qquad z\ge x,
\]
the regular derivatives remain greater than \(1/20\) for
own three and \(1/24\) for own four.
The true-row derivatives retain at least these same bounds.
Decrease \(\varepsilon\), if necessary, to lie in the
[physical high-tail collar](research_mixed_first_attached_high_tail_seam.md).
Then the first ordinary factor's complete envelope has only its
central, real-cut and true-last-row alternatives: its other high
physical maxima have been paid, and all aliases and joins remain
covered by the original complete envelope.

For each following regular profile which is valid on the target
domain, integration of these pointwise coupled inequalities and
then maximization over the unchanged real profile intervals
therefore proves a strictly increasing joint envelope under the
actual first-height and neighbor-height move. Both cap true-end
branches, both first ordinary cuts, its entire central interval,
and its true last row have been included.

This is a sign theorem for the coupled local profile comparison,
not a claim of a complete following ordinary finite-source bound
on an unproved enlarged domain. Its high-tail alternatives or
another following endpoint require their own derivatives.
Nor does it identify the envelope at \(x=.1+\varepsilon\)
with the calibrated geometric value. The intermediate taper,
original middle compensation and relative pinning fee remain
in the boundary problem. No whole-source lower bound or larger
knot-family theorem is asserted.

