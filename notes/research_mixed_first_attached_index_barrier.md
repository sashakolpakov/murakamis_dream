# A raised low-index cut on the actual first-attached taper

Research deduction, 7 November 2026. The actual upper height cutoff
of the second retained target supplies a stronger index barrier than
the independent containing rectangle. On every nonpositive fixed
ordinary index height, the central maximum lies strictly above
real index \(.22\). The exact geometric estimate for low physical
rows also extends through \(\lfloor .22N\rfloor\), with its unchanged
constant 201.

This allows the lower central cut to be raised from \(.2\) to \(.22\)
in the complete finite-source envelope. It does not assert a calibrated
gap for the new cut or a sign for the neighboring-height contribution.
No numerical evaluation is used.

## 1. The correlated target restrictions

Use the original \(Q_\epsilon\), literal rows, allocations and actual
target family of the
[complete adjoining envelope](research_mixed_first_attached_complete_contour_envelope.md).
Thus
\[
 a=x+ih_a,\quad .1\le x\le.22,\qquad
 b=z+ih_b,\quad .1\le z\le.5.
 \tag{1}
\]
The actual first taper and the second target's upper cutoff give
\[
 \begin{split}
 -.108&\le h_a\le\frac7{40}(x-.1),\\
 h_b&\ge-.102 &&(.1\le z\le.45),\\
 h_b&\ge-.102\cdot400(.5-z)^2 &&(.45\le z\le.5).
 \end{split}
 \tag{2}
\]
The last line retains the genuine quadratic cutoff of the
[hybrid graph](research_mixed_left_boundary_shallow_taper.md),
equation (9). Further minimum cutoffs only attenuate a negative
height and preserve that bound; positive second heights also
satisfy it. An independent rectangle with height \(-.102\) at
\(z=.5\) is not admitted.

Fix
\[
       -.108\le\eta\le0,\qquad R=e^{2\pi\eta},\qquad
       r_a=e^{2\pi h_a},\quad r_b=e^{2\pi h_b}.
 \tag{3}
\]
The old elementary exponential bound gives \(1/2<R\le1\).

## 2. The two numerator factors at real index .22

**Lemma 1.** Throughout (1)--(3),
\[
 \begin{split}
 |r_a^{-1}-R e^{-2\pi i(x+.22)}|^2
                      &> A(R):=1+R^2+\frac{21}{25}R,\\
 |1-Rr_b e^{-2\pi i(z+.22)}|^2
                      &> B(R):=1+\frac{R^2}{4}+\frac{21}{50}R.
 \end{split}
 \tag{4}
\]

*Proof of the first line.* Its modulus increases with \(r_a^{-1}\),
since the angular cosine is negative. By (2),
\[
 r_a^{-1}\ge t(x):=e^{-k(x-.1)},\qquad k=7\pi/20.
 \tag{5}
\]
Consider \(t^2+R^2-2Rt\cos\theta\), with
\(\theta=2\pi(x+.22)\). Its derivative has the sign of
\[
                  N=-kt+R(k\cos\theta+2\pi\sin\theta).
 \tag{6}
\]
At every zero,
\[
                        N'=R(k^2+4\pi^2)\cos\theta<0.
 \tag{7}
\]
Thus all stationary points are maxima, and the minimum is at
\(x=.1\) or \(x=.22\).

At the first endpoint \(t=1\) and
\(-\cos(.64\pi)=\sin(.14\pi)>21/50\), giving the first
line of (4). At the other endpoint,
\[
 t=e^{-.042\pi}>\frac{20}{23}>\frac{43}{50},\qquad
                    -\cos(.88\pi)=\cos(.12\pi)>\frac{23}{25}.
 \tag{8}
\]
The exponential estimate is the original early-cap radius bound.
The resulting squared modulus is greater than
\[
 \frac{1849}{2500}+R^2+\frac{989}{625}R.
 \tag{9}
\]
Subtract \(A(R)\). Since \(R>1/2\), the difference exceeds
\[
 -\frac{651}{2500}+\frac{464}{625}\frac12
                                      =\frac{277}{2500}>0.
 \tag{10}
\]
For elementary trigonometric witnesses in (8), use
\(.14\pi>1099/2500\), \(.14\pi<11/25\) in
\(\sin u\ge u-u^3/6\); this gives \(\sin(.14\pi)>21/50\).
Also \(.12\pi<66/175\) and
\(\cos u\ge1-u^2/2\) give \(\cos(.12\pi)>23/25\).
This proves the first line.

*Proof of the second line.* For \(.1\le z\le.45\),
\[
 \cos2\pi(z+.22)<-\frac{21}{50},\qquad r_b>\frac12.
 \tag{11}
\]
The cosine bound follows from its two endpoint values on
\([.32,.67]\), using the sine witness just given; the radius
bound follows from \(h_b\ge-.102>-.108\).
Both terms in the squared modulus increase with \(r_b>0\),
which proves the second line of (4) in this range.

For \(.45\le z\le.5\), put \(u=.5-z\in[0,1/20]\) and
\[
        v(u)=e^{-Ku^2},\qquad K=\frac{408\pi}{5},\qquad
                         \zeta=.06\pi+2\pi u.
 \tag{12}
\]
By (2), \(r_b\ge v(u)\). The squared modulus is bounded below
by \(1+R^2v^2+2Rv\sin\zeta\). Its derivative has the sign of
\[
                   M=2\pi\cos\zeta-2Ku(Rv+\sin\zeta).
 \tag{13}
\]
At a zero,
\[
 M'=-4\pi^2\sin\zeta-2K(Rv+\sin\zeta)
                                  -4K^2u^2\sin\zeta<0.
 \tag{14}
\]
Its minimum is therefore at an endpoint. At \(u=1/20\),
\(v=e^{-.204\pi}>1/2\) and
\(\sin\zeta=\sin(.16\pi)>21/50\), so (4) follows.
At \(u=0\), the lower value is
\[
 1+R^2+2R\sin(.06\pi)>1+R^2+\frac9{25}R
                                >B(R).
 \tag{15}
\]
Here \(\sin(.06\pi)>9/50\) is the old cap sine bound, and
the final difference is
\(R(3R/4-3/50)>0\), since \(R>1/2\).
This completes the proof. \(\square\)

## 3. A strict derivative barrier with an exact rational margin

**Proposition 2.** On (1)--(3),
\[
                  \Re Q_{\epsilon,s}(.22+i\eta;a,b)>\frac1{75},
                         \qquad \epsilon=0,1 .
 \tag{16}
\]

*Proof.* Retain the original chirp. Its real contribution is
\(-2\pi h_a\), so the exact exponential identity is
\[
 e^{2\Re Q_{\epsilon,s}}
 =\frac{|r_a^{-1}-R e^{-2\pi i(x+.22)}|^2
                  |1-Rr_b e^{-2\pi i(z+.22)}|^2}
              {|1-R e^{-.44\pi i}|^{2(2+\epsilon)}}.
 \tag{17}
\]
Since \(\cos(.44\pi)>9/50\), its denominator base is less than
\[
                       D(R)=1+R^2-\frac9{25}R\le\frac{41}{25}.
 \tag{18}
\]
All quantities are positive. Expanding the polynomials from (4)
gives
\[
 \begin{split}
 AB-D^2={}&\frac{99}{50}R-\frac{1317}{2500}R^2
                              +\frac{27}{20}R^3-\frac34R^4\\
 &\ge\frac{3633}{2500}R+\frac35R^3>\frac18,\\[1mm]
 AB-D^3={}&\frac{117}{50}R-\frac{893}{500}R^2
       +\frac{177291}{62500}R^3-\frac{7847}{2500}R^4
                              +\frac{27}{25}R^5-R^6\\
 &\ge\frac{277}{500}R-\frac{4721}{15625}R^3
                                      +\frac2{25}R^5\\
 &\ge\frac{15741}{62500}R+\frac2{25}R^5>\frac18 .
 \end{split}
 \tag{19}
\]
Only \(1/2<R\le1\) is used. In particular
\(15741/125000>1/8\).
Equations (4), (17)--(19) imply, for either type,
\[
 e^{2\Re Q_{\epsilon,s}}>1+\frac{15625}{551368}.
 \tag{20}
\]
The elementary inequality \(\log(1+t)>t/(1+t)\) gives
\[
 \Re Q_{\epsilon,s}>
                  \frac{15625}{1133986}>\frac1{75},
 \tag{21}
\]
the final cross-product difference being \(37889>0\).
This proves (16). \(\square\)

The complete envelope already proves strict horizontal concavity of
\(\Re Q_\epsilon(v+i\eta)\) for \(.2\le v\le.49\) on the
actual cotangent domains. Its derivative is decreasing. Thus (16)
proves both
\[
 \Re Q_{\epsilon,s}(v+i\eta)>\frac1{75}
                      \quad(.2\le v\le.22)
 \tag{22}
\]
and
\[
 \Re F_{\alpha\epsilon}(.22+i\eta)
       -\Re F_{\alpha\epsilon}(.2+i\eta)>\frac1{3750}.
 \tag{23}
\]
Every central maximizing real index is strictly greater than \(.22\).
The maximum \(B^0\) is unchanged if its interval is replaced by
\([.22,.49]\).

## 4. Exact low rows and the resulting source reduction

At \(\eta=0\), the derivative in (22) is the original real-row
logarithmic ratio. Combine (22) with the existing
[low-row ratio](research_mixed_first_attached_low_row_transport.md),
which exceeds \(1/200\) for \(0<u\le.2\). Therefore every
successive literal row up to
\[
                            L_N=\lfloor11N/50\rfloor
 \tag{24}
\]
increases in modulus by a factor greater than \(e^{1/200}\).
All numerator arguments up to this index have real parts strictly
between zero and one, so the same exact recurrence and geometric
sum give
\[
 \left|\sum_{j=0}^{L_N}R_{j,N}\right|
       \le\sum_{j=0}^{L_N}|R_{j,N}|<201|R_{L_N,N}|.
 \tag{25}
\]
This holds at every \(N\ge2\), for both types and parities; the
case \(L_N=0\) is immediate. Multiplication by the literal cap
and exterior Fourier factors preserves the nonstrict estimate
including their zeros.

The complete adjoining contour theorem may now use lower cut
\(.22\) and upper cut \(.49\). Its fixed-height maximum is
unchanged by (23), and all old alias bounds remain valid on the
smaller real interval. The two joins are still paid by their
endpoints and this same maximum. In its physical-tail list replace
the low cut \(.2\) by \(.22\); keep the entire high tail, its
endpoints and all four or six stationary-root candidates.
No source row or Fourier allocation is removed.

Finally, for the regular moving-height comparison, the endpoint
reduction in
[the moving-height note](research_mixed_first_attached_moving_height_reduction.md)
can use \(v\in[.22,.49]\). Its upper endpoint remains paid.
The remaining two expressions therefore have \(v=.22\), rather
than \(v=.2\). Their signs and the two-incidence neighboring-height
term are not asserted here. Equation (23) is a same-height
inactivity margin, not a comparison of a real cut with the
negative-height main contour or with the calibrated boundary plane.
