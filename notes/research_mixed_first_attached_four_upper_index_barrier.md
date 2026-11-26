# An upper index barrier for the adjoining own-four source

Research deduction, 7 November 2026. On the actual early
first-minimum taper, the adjoining own-four fixed-height central
profile has its unique maximum in \((.22,.4)\).
The original upper real cut at \(.49\) is paid by the value at
\(.4\), with a strict derivative margin. This applies throughout
the early taper, not only near the physical seam.

The proof retains the shared incoming chirp and actual height
correlation. It evaluates no source, root or numerical proposal.
It does not pay the coupled neighboring derivative or the remaining
high physical-tail maxima.

## 1. Actual source and a squared row ratio

Use the literal source, original primitive and allocations of
[the complete adjoining envelope](research_mixed_first_attached_complete_contour_envelope.md).
The adjoining factor has own type four, so
\[
 Q_1(s;a,b)=g(s+a)+g(s+b)-3g(s)+2\pi ias .
\]
Assume the actual first-minimum target restrictions
\[
 \begin{gathered}
 a=x+ih_a,\quad b=z+ih_b,\qquad
 .1\le x\le.22,\quad x\le z\le.5,\quad h_b\le0,\\
 h_a=-\lambda_a(x-.1),\qquad
           -7/40\le\lambda_a\le13/20,\qquad
                  -.108\le\eta\le0 .
 \end{gathered}                                                \tag{1}
\]
The original coupled attached bound is used for a first own-four
cap, hence its \(m\ge3\) restriction remains.
First own three is covered by its smaller original coefficient
interval. All actual cotangent/finite-source conditions in the
adjoining envelope remain in force; (1) is not an independent
replacement for them.

Evaluate the original index derivative only symbolically at
\(s=2/5+i\eta\), and put
\[
 d=x-.1,\quad R=e^{2\pi\eta},\quad
 q=e^{-2\pi h_a},\quad r_b=e^{2\pi h_b},\quad
 \phi=\frac{1+\sqrt5}{2}.
\]
Then \(1/2<R\le1\), \(0<r_b\le1\), and exactly
\[
 e^{2\Re Q_{1,s}}=
 \frac{\{q^2+R^2+2qR\cos(2\pi d)\}
       |1-Rr_b e^{-2\pi i(.4+z)}|^2}
                      {(1+R^2+\phi R)^3}.                   \tag{2}
\]
The factor \(q^2\) absorbed in the first braces is the original
incoming chirp. Omitting it would change the source comparison.
For the lower bound on \(R\), use
\(.216\pi<69/100<\log2\), with the latter following from the
first two positive terms of
\(\log2=2\operatorname{atanh}(1/3)\).

Since \(.5+d\le.4+z\le.9\), its angular cosine is at least
\(-\cos(2\pi d)\). Maximizing the convex quadratic in
\(r_b\in[0,1]\) at its endpoints gives
\[
 |1-Rr_b e^{-2\pi i(.4+z)}|^2
                      \le1+R^2+2R\cos(2\pi d).               \tag{3}
\]
The right side exceeds one, so it also pays the endpoint \(r_b=0\).

## 2. Rational correlated envelopes

Throughout \(0\le d\le3/25\),
\[
 q\le q_d:=1+\frac{65}{12}d,\qquad
 \cos(2\pi d)\le c_d:=1-\frac{37}{2}d^2,\qquad
                    \phi>\frac{161}{100}=:L .               \tag{4}
\]
For the first bound, if \(\lambda_a<0\) use \(q\le1\).
Otherwise \(q\le e^{(13\pi/10)d}\).
At the right endpoint this is less than
\(e^{1/2}\le33/20\); convexity of the exponential bounds it
above by the chord in (4).
The displayed exponential bound is elementary:
\[
 e^{1/2}<1+\frac12+
       \frac{(1/2)^2}{2(1-(1/2)/3)}=\frac{33}{20},
\]
by bounding its factorial tail with the geometric series
\(n!\ge2\cdot3^{n-2}\) for \(n\ge2\).

For the second bound use the alternating cosine estimate:
\[
 \cos(2\pi d)\le1-2\pi^2d^2+\frac{(2\pi)^4d^4}{24}.
\]
Here
\[
 \frac{(44/7)^4}{24}\left(\frac3{25}\right)^2<1,\qquad
 2(157/50)^2-1>\frac{37}{2}.
\]
These give (4). Finally
\(\sqrt5>111/50\) proves the bound on \(\phi\).
In particular \(1\le q_d\le33/20\) and \(0<c_d\le1\).

Both numerator factors in (2)--(3) increase in these positive
variables. It suffices to bound
\[
 A=q_d^2+2q_dc_dR+R^2,\qquad
 B=1+2c_dR+R^2,\qquad
                         D_L=1+LR+R^2.                     \tag{5}
\]
We prove the uniform surplus
\[
                            D_L^3-AB>\frac38.                \tag{6}
\]

For fixed \(q=q_d,c=c_d\), expand this difference in \(R\):
\[
 \begin{split}
 \Delta(R)={}&1-q^2+
       \{3L-2q(q+1)c\}R\\
 &+\{2+3L^2-q^2-4qc^2\}R^2\\
 &+\{L^3+6L-2(q+1)c\}R^3
       +(2+3L^2)R^4+3LR^5+R^6 .
 \end{split}                                                  \tag{7}
\]
The coefficients of \(R,R^2,R^3,R^4\) are respectively
greater than \(-4,0,8,9\) on the stated \(q,c\) ranges.
The last two coefficients are positive.
Consequently, for \(R\ge1/2\),
\[
                \Delta'(R)>-4+3\cdot8/4+4\cdot9/8
                                          =13/2>0.           \tag{8}
\]
Thus it suffices to treat \(R=1/2\).

## 3. A single endpoint polynomial

At \(R=1/2\), the numerator product is the polynomial
\[
 \begin{split}
 f(d)
 &=\{q_d^2+q_dc_d+1/4\}\{5/4+c_d\}\\
 &=\frac{81}{16}+\frac{585}{16}d-\frac{1103}{64}d^2
       -\frac{16835}{32}d^3-\frac{57757}{288}d^4
       +\frac{88985}{48}d^5 .
 \end{split}                                                   \tag{9}
\]
It is strictly increasing for \(0\le d\le3/25\).
Indeed, dropping the positive quartic term in its derivative,
\[
 \begin{split}
 f'(d)
 &>\,36-35d-1580d^2-803d^3\\
 &\ge36-35(3/25)-1580(3/25)^2-803(3/25)^3>7 .
 \end{split}                                                   \tag{10}
\]
All coefficients and endpoint comparisons here are exact rationals.

At \(d=3/25\), one has \(q_d=33/20\), \(c_d=917/1250\),
and
\[
 A=\frac{209147}{50000},\qquad B=\frac{4959}{2500},\qquad
 D_L=\frac{411}{200}.
\]
Thus the exact endpoint surplus is
\[
 \left(\frac{411}{200}\right)^3
       -\frac{1037159973}{125000000}
        =\frac{381036591}{10^9}>\frac38 .                    \tag{11}
\]
Equations (8)--(11) prove (6) for the whole continuous domain,
with no tested mesh or proposal.

For the actual denominator \(D=1+R^2+\phi R\),
\(\phi<13/8\) and \(R\le1\) give \(D^3<(29/8)^3<48\).
Combining (2)--(6),
\[
 e^{2\Re Q_{1,s}(.4+i\eta;a,b)}
                 <1-\frac{3/8}{48}=\frac{127}{128}.
\]
Therefore the original logarithmic derivative satisfies
\[
             \boxed{\ \Re Q_{1,s}(.4+i\eta;a,b)<-1/256.\ }     \tag{12}
\]

## 4. Complete central and cut consequences

Strict real-index concavity on the original fixed-height strip
is already proved in Section 3 of the complete adjoining envelope.
The
[lower index barrier](research_mixed_first_attached_index_barrier.md)
gives a strictly positive derivative at \(v=.22\).
Together with (12), these facts imply that the fixed-line
central maximum is attained uniquely in
\[
                              .22<v<.4.                      \tag{13}
\]
This is a real-profile maximum; it is not a new original complex
root or a moving finite packet.

Also, on each fixed line in (1),
\[
 \Re F_{\alpha1}(v+i\eta;a,b)
 \le \Re F_{\alpha1}(.4+i\eta;a,b)-\frac{v-.4}{256},
                              \qquad .4\le v\le.49.           \tag{14}
\]
The allocations do not depend on the index \(v\).
At zero index height, the real physical rate equals this same
original phase on the regular strip.
Thus the entire physical interval \([.4,.49]\), and the old
upper cut at \(.49\), are paid by the value at \(.4\).

One may keep the existing finite contour and simply use (13)--(14)
inside its proved complete upper envelope.
Equivalently its central interval can be shortened to
\([.22,.4]\): all arguments lie in the old regular domain,
and the old alias/join estimates apply to that subset.
The new short physical strip is paid by (14).
No new analytic replay or source certificate is required.

In either description the complete conditional source still
retains the true last row and every high-tail critical value
not already paid by a physical-tail theorem.
The coupled neighboring-height force and the calibrated
boundary comparison remain separate.
The present deduction supplies an actual restriction on the
maximizing ordinary profile throughout the taper, including
all first-cap types covered by (1).

