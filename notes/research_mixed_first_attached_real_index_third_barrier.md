# A strict one-third barrier for the real adjoining index

Research deduction, 7 November 2026. On the actual first-minimum
taper, the adjoining own-four real-profile maximum lies strictly
between \(.22\) and \(1/3\). The new upper derivative has a uniform
negative margin. This allows the already proved complete finite
envelope to use its real main line and restrict the maximum
of that line to this shorter interval.

The statement concerns a real ordinary index. It is not asserted
on a negative index-height line, where the same upper barrier
need not hold. The following factor, interior high physical rows,
original boundary marginal and compensation retain their own
requirements.

## 1. Actual targets and the original derivative

Keep the first-minimum domain of the
[two-incidence theorem](research_mixed_first_attached_two_incidence_reduction.md):
\[
 \begin{gathered}
 d=x-\frac1{10},\qquad
 \frac1{10}\le x\le\frac{11}{50},\qquad x\le z\le\frac12,\\
 a=x-i\lambda_a d,\qquad b=z-i\lambda_b d,\qquad
 0\le\lambda_b\le\frac{17}{20}.
 \end{gathered}                                                   \tag{1}
\]
For a first cap of own type three, retain
\(-7/40\le\lambda_a\le3/5\). For own type four retain
the actual attached \(m\ge3\) range
\(1/6<\lambda_a<13/20\), or a nonnegative attenuation
of that range when only the derivative statement below is used.
In particular every nonnegative first coefficient here is at
most \(13/20\). No simultaneous reference is selected from an
independent coefficient box.

The adjoining factor has own type four and original phase
\[
 Q_1(s;a,b)=g(s+a)+g(s+b)-3g(s)+2\pi ias.                         \tag{2}
\]
Put
\[
 r_a=e^{-2\pi\lambda_a d},\qquad r_b=e^{-2\pi\lambda_b d},
 \qquad q=r_a^{-1}.
\]
At the real index \(s=1/3\), the original chirp gives exactly
\[
 \exp\{2\Re Q_{1,s}(1/3;a,b)\}
 =
 \frac{
 |q-e^{-2\pi i(1/3+x)}|^2
 |1-r_b e^{-2\pi i(1/3+z)}|^2}{27}.                             \tag{3}
\]
In particular the first modulus contains \(q=r_a^{-1}\),
not \(r_a\). The denominator is
\(|1-e^{-2\pi i/3}|^6=27\).

## 2. An exact negative upper derivative

**Proposition 1.** Throughout (1),
\[
                     \Re Q_{1,s}(1/3;a,b)<-\frac1{4000}.
                                                                    \tag{4}
\]

*Proof.* Since \(0<r_b\le1\), its modulus in (3) is at
most two. If \(\lambda_a\le0\), then \(q\le1\), so
the first modulus is also at most two. The quotient in (3)
is then at most \(16/27\), more than sufficient for (4).

Suppose \(\lambda_a\ge0\). If \(x\le21/100\), then
\[
 2\pi\lambda_a d\le\frac{143\pi}{1000}<\frac9{20}.
\]
The elementary exponential majorant
\[
 e^u\le1+u+\frac{u^2}{2(1-u/3)},\qquad 0\le u<3,                 \tag{5}
\]
therefore gives
\[
 q<\frac{1067}{680}<\frac{11}{7}.
\]
Formula (3) is bounded above by
\[
                  \frac{4(1+11/7)^2}{27}=\frac{48}{49}.
                                                                    \tag{6}
\]

It remains to consider \(21/100\le x\le11/50\).
Now
\[
 2\pi\lambda_a d\le\frac{39\pi}{250}
      <\frac{429}{875}<\frac{123}{250}.
\]
Applying (5) again yields
\[
 q<\frac{171043}{104500}<\frac{41}{25}.                          \tag{7}
\]
Set
\[
 C=\cos\bigl(2\pi(x-1/6)\bigr).
\]
The angle is between \(13\pi/150\) and \(8\pi/75\).
In particular it is positive and less than \(\pi/2\);
also, by monotonicity and the cosine polynomial,
\[
 0<C<
 1-\frac{(13/50)^2}{2}+\frac{(13/50)^4}{24}
 =\frac{144958561}{150000000}<\frac{29}{30}.                    \tag{8}
\]
The first squared modulus in (3) is \(q^2+1+2qC\).
For the other one, \(1/3+z\in[1/3+x,5/6]\).
On this interval the square of the modulus is convex in \(r_b\).
Its endpoint values at \(r_b=0,1\) are
\(1\) and \(4\sin^2\pi(1/3+z)\).
The latter decreases with \(z\) here and is at least one
up to \(z=1/2\). Consequently
\[
 |1-r_b e^{-2\pi i(1/3+z)}|^2
       \le 2(1+C).
\]
Using (7)--(8), the numerator of (3) is strictly smaller than
\[
 \left\{(41/25)^2+1+2(41/25)(29/30)\right\}
                       2(1+29/30)
                 =\frac{758917}{28125}<27.                    \tag{9}
\]
Thus (3) is less than \(758917/759375\).
Since \(\log(1-u)<-u\) for \(0<u<1\),
\[
 \Re Q_{1,s}(1/3;a,b)
       <-\frac{229}{759375}<-\frac1{4000}.                     \tag{10}
\]
The other two cases, (6) and \(16/27\), have larger strict
margins by the same logarithmic inequality.
This proves (4). \(\square\)

All bounds above concern exact original logarithms and elementary
inequalities on the entire prescribed domain. No parameter point,
root, proposal or analytic function has been evaluated.

## 3. The real maximum in the existing finite envelope

The original
[lower barrier](research_mixed_first_attached_index_barrier.md)
gives
\(\Re Q_{1,s}(.22;a,b)>1/75\) on (1).
The real profile is strictly concave on \([.22,.49]\).
For completeness, each shifted real argument exceeds \(s\).
When it is below \(1/2\), its real cotangent is at most
its zero-height cotangent, which is smaller than
\(\cot\pi s\); when it is at least \(1/2\), its real
cotangent is nonpositive. Hence directly
\[
 \Re Q_{1,ss}(s;a,b)
 =\pi\Re\{\cot\pi(s+a)+\cot\pi(s+b)-3\cot\pi s\}<0.
                                                                    \tag{11}
\]
This also follows from the previously proved pair-form curvature.
The original constant imaginary parts in \(g''\) do not affect (11).
All shifted real arguments stay below one.

Therefore the real central profile has one and only one maximizing
index \(\widehat v\), and
\[
                  .22<\widehat v<\frac13,\qquad
                      \Re Q_{1,s}(\widehat v;a,b)=0.             \tag{12}
\]
Moreover, on the old upper interval,
\[
 \Re Q_1(v;a,b)
 \le\Re Q_1(1/3;a,b)-\frac{v-1/3}{4000},
                              \qquad \frac13\le v\le.49.        \tag{13}
\]
The outer allocations are independent of \(s\), so these statements
hold for the original allocated profile as well.

The
[complete adjoining source envelope](research_mixed_first_attached_complete_contour_envelope.md)
explicitly permits every fixed main height in
\([-.108,.068]\), in particular height zero.
Choose that line before making the comparison, retaining the
original finite contour and its original half-grid cuts.
On that old interval, strict concavity and the lower derivative
at \(.22\) control its lower portion, while (13) controls its
upper portion. Its maximum is therefore exactly the maximum
over \([.22,1/3]\).
Both old real-cut rates are bounded by this same maximum.
The original horizontal aliases and their strict reserves are
unchanged, and each old vertical alias is bounded by its own
real-cut rate. At this chosen real main height the zero-mode
joins to that height are absent.

Only a continuous profile maximum has been restricted.
No finite lattice interval or half-grid cut has been moved.
The exact lower physical-row theorem, and all physical-tail
terms in the original finite decomposition, retain their
original counting and rounding conventions.

This preserves the full finite upper bound, with the same
polynomial factors and arbitrary rate tolerance, both parities,
all original fixed jets and zero-safe multiplication.
The exhaustive original high physical-row profiles above
\(.49\), including every interior critical value and the
true last row, remain present. They are not removed by (13).

## 4. What this pays and what remains

The strict sign (4) and the profile restriction are uniform on the
actual first-minimum family. They do not require a moving critical
packet or a full complex stationary index.
They also do not transfer (4) to a negative fixed index height:
the factor \(27\) in (3) is specific to the real main line.

For transport of the central real envelope, the original coupled
derivative is now needed only for maximizing profiles in
\((.22,1/3)\), or conservatively on its closure. The neighboring
radius and its two following endpoint branches must still be kept.
An endpoint reduction proved for a lower support may be applied
on this smaller interval only under that support's stated
hypotheses.

No positive sign of that coupled derivative is claimed here.
The separate negative-height active-index credit is not being
substituted at the original real cuts. Interior high physical profiles,
the complete following finite-source envelope, the actual marginal,
middle compensation and relative pinning fee retain their
previous obligations.
