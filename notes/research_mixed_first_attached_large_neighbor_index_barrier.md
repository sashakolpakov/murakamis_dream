# The real adjoining index decreases when the neighbor coefficient grows

Research deduction, 7 November 2026. For a neighbor-height coefficient
at least \(3/4\), the actual real central ordinary maximum is below
\(3/10\), with a uniform signed derivative at that cut. Thus the
largest negative-neighbor transport coefficients cannot be combined
with the earlier largest real central indices. The actual upper
taper also excludes the neighbor's far-right real endpoint in this
sector.

These are same-target real-profile statements. They preserve the
two following branches and do not pay the whole coupled derivative
or any interior high physical-row alternative.

## 1. The coefficient and radius are kept together

Use precisely the domain, original phase and normalization of
the [one-third barrier](research_mixed_first_attached_real_index_third_barrier.md):
\[
 \begin{gathered}
 d=x-.1,\quad .1\le x\le.22,\quad x\le z\le.5,\qquad
 a=x-i\lambda_a d,\quad b=z-i\lambda_b d,\\
 Q_1(s;a,b)=g(s+a)+g(s+b)-3g(s)+2\pi ias .
 \end{gathered}                                                     \tag{1}
\]
Retain both first-type coefficient ranges and their exact source
restrictions. In particular \(\lambda_a\le13/20\).
In this note suppose additionally that
\[
                           \frac34\le\lambda_b\le\frac{17}{20}.
                                                                    \tag{2}
\]

**Proposition 1.** On (1)--(2),
\[
                  \Re Q_{1,s}(3/10;a,b)<-\frac1{100}.
                                                                    \tag{3}
\]

*Proof.* Write \(q=e^{2\pi\lambda_a d}\) and
\(r_b=e^{-2\pi\lambda_b d}\). The same original chirp as
in equation (3) of the one-third barrier gives, now at \(v=3/10\),
\[
 e^{\Re Q_{1,s}(v;a,b)}
  =\frac{|q-e^{-2\pi i(v+x)}|\,
             |1-r_b e^{-2\pi i(v+z)}|}
                  {(2\sin\pi v)^3}
  \le\frac{(1+q)(1+r_b)}{(2\sin\pi v)^3}.                         \tag{4}
\]
No independent \(q\) and \(r_b\) extrema are used.
Their shared \(d\) gives
\[
 (1+q)(1+r_b)
 \le f(d):=(1+e^{13\pi d/10})(1+e^{-3\pi d/2}),
                         \qquad 0\le d\le3/25 .
                                                                    \tag{5}
\]
The right side is the sum of the four positive exponential
terms with exponents \(0,13\pi d/10,-3\pi d/2,-\pi d/5\).
It is convex in \(d\), so its maximum on this interval is
at an endpoint.

At \(d=0\), \(f(d)=4\).
At \(d=3/25\), the exact exponential estimate already proved
in the one-third barrier gives \(e^{39\pi/250}<41/25\).
Also
\[
 e^{9\pi/50}>e^{14/25}>
 1+\frac{14}{25}+\frac{(14/25)^2}{2}
       +\frac{(14/25)^3}{6}+\frac{(14/25)^4}{24}
 =\frac74+\frac{261}{1562500}>\frac74 .
                                                                    \tag{6}
\]
Thus \(e^{-9\pi/50}<4/7\), and
\[
                 f(3/25)<(1+41/25)(1+4/7)=\frac{726}{175}.
                                                                    \tag{7}
\]
The latter bound exceeds \(4\), so it bounds (5) everywhere.
The pentagon identity and \(\sqrt5>11/5\) give
\[
                  (2\sin(3\pi/10))^3=2+\sqrt5>\frac{21}{5}.
                                                                    \tag{8}
\]
Consequently (4) is smaller than \(242/245\).
Using \(\log(1-u)<-u\),
\[
             \Re Q_{1,s}(3/10;a,b)<-\frac3{245}<-\frac1{100}.
\]
This proves (3). \(\square\)

The existing lower derivative at \(.22\) and strict real
concavity therefore imply
\[
                .22<\widehat v<.3
                                                                    \tag{9}
\]
for the unique real central maximizing profile. As in the
one-third theorem, this restricts the continuous maximum of
the original height-zero finite envelope. Its finite contour,
half-grid cuts, physical row counts and high-tail alternatives
are unchanged.

## 2. The monotonicity behind the correlation

The real maximizing index has a strict coefficient monotonicity
on every coefficient interval retaining the hypotheses of the
one-third theorem, not merely in (2).
This is a mathematical comparison of profiles; it does not assert
that varying a coefficient independently traces canonical references.

Put \(\mathcal R(v)=\Re Q_{1,s}(v;a,b)\).
The one-third theorem places its zero in \((.22,1/3)\).
Using \(g''=\pi\cot\pi z-\pi i\), exact differentiation yields
\[
 \begin{split}
 \partial_{\lambda_a}\mathcal R
       &=\pi d\{1+\Im\cot\pi(v+a)\},\\
 \partial_{\lambda_b}\mathcal R
       &=\pi d\{\Im\cot\pi(v+b)-1\}.
 \end{split}                                                       \tag{10}
\]
The \(+1\) in the first line includes the incoming chirp.

For the first shifted argument,
\(.32<v+x<1/3+.22<3/4\), and its doubled-angle cosine
is negative. Its imaginary cotangent therefore has modulus
less than one at every finite height.
For the second shifted argument,
\[
 .32<v+z<5/6,\qquad
 \cos(2\pi(v+z))\le\frac12,\qquad
 r_b\ge e^{-.204\pi}>\frac12.                                     \tag{11}
\]
The last bound follows from
\(.204\pi<2/3<\log2\).
At nonpositive height the identity
\[
 \Im\cot\pi(y+ih)
  =\frac{1-r^2}{1+r^2-2r\cos(2\pi y)},\qquad r=e^{2\pi h},
\]
shows that this imaginary part is less than one whenever
\(\cos(2\pi y)<r\), as in (11).
Hence for \(d>0\), the two signs in (10) are respectively
positive and negative.

Since \(\partial_v\mathcal R<0\), the implicit equation
\(\mathcal R(\widehat v)=0\) now proves
\[
              \partial_{\lambda_a}\widehat v>0,\qquad
              \partial_{\lambda_b}\widehat v<0,\qquad d>0.
                                                                    \tag{12}
\]
At \(d=0\) both parameter derivatives vanish.
This uses only stationarity in the real index direction,
not a new complex root or a finite source packet.

## 3. The actual upper cutoff restricts \(z\) too

For an actual first-minimum move the neighbor coefficient is
\[
           \lambda_b=-c_bR(z)/.12,\qquad
          -.102<c_b<-.001 ,
                                                                    \tag{13}
\]
with the original upper cutoff
\[
 R(z)=1\quad(z\le.45),\qquad
 R(z)=400(.5-z)^2\quad(.45\le z\le.5).
                                                                    \tag{14}
\]
These are the same coefficients in both the height and its
derivative, as in the
[coupled seam theorem](research_mixed_first_attached_coupled_seam_transport.md).
In particular \(\lambda_b\le(17/20)R(z)\).
If (2) holds, then
\[
                              z<\frac{227}{500}.                 \tag{15}
\]
Indeed \(z\ge227/500\) would imply
\[
 R(z)\le\frac{529}{625}<\frac{15}{17},
\]
contrary to \(\lambda_b\ge3/4\) and (13).
If \(z\le.45\), (15) is immediate.

Equations (9) and (15) are simultaneous restrictions in the
large-coefficient sector, with the original radius still
\(e^{-2\pi\lambda_b(x-.1)}\).
Both exact following-index branches remain in the coupled force;
neither restriction removes one of them.
The regular derivative comparison must retain these coefficient
and radius relations, along with the original first marginal,
compensated middle terms and pinning fee. No sign of their full
sum is inferred solely from (9), (12) or (15).
