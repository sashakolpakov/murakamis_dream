# The early own-four cap maximizer lies below \(2/5\)

Research deduction, 7 November 2026. The full real-private cap
envelope for own type four on the early lower-half tube has its
unique maximizer in \((.27,.4)\). Thus the upper part of its
previous private interval is inactive, with a uniform strict
derivative margin. This preserves the whole finite-source bound
and can be used in coupled neighboring-height comparisons.

This is a statement about the real-profile maximum, not a new
complex critical point or a finite packet at a moving root.
No calibrated boundary sign follows from this restriction.

## 1. The original coherent coefficient and real profile

Use the exact source and coherent endpoint action of
[the early real-row theorem](research_mixed_cap_early_taper_real_rows.md).
Put \(\Lambda(e)=\Re S(e)\), reserving \(\lambda\) elsewhere
for a height coefficient. The real-profile rate is
\[
 R_1(e,a)=\Lambda(e)
       +\int_0^e\log|1-e^{-2\pi i(a+u)}|\,du-J(e)
       =\Re\Psi_1(e,a),\qquad a=x+ih,
                                                               \tag{1}
\]
where
\[
                       .1\le x\le.22,\qquad -.108\le h\le0 .
                                                               \tag{2}
\]
The original additive constants and cap normalization are retained.
The real-private envelope is
\[
 A^{\rm real}_1(a)=\max_{.27\le e\le.49}R_1(e,a).                \tag{3}
\]

The exact curvature identity and endpoint derivative from the
real-row theorem are
\[
 \begin{split}
 -\Lambda''(e)/\pi
 &=\cot\pi e+\frac{2}{\sin\pi e}
          \Re\frac1{\sqrt{2-e^{-2\pi ie}}},\qquad 0<e<1/2,\\
 \Lambda'(1/2)&=-\log2 .
 \end{split}                                                   \tag{4}
\]
The square root is its specified principal branch. That theorem
also proves strict concavity of \(R_1\) throughout \(0<e<1/2\)
for every target in (2), and
\[
                          R_1'(.27,a)>13/100.                 \tag{5}
\]

## 2. An analytic upper barrier at \(e=.4\)

For \(2/5\le e\le1/2\), elementary pentagon identities give
\[
 \cot\pi e<\frac13,\qquad
 \sin\pi e>\frac{19}{20},\qquad
                       2-\cos2\pi e>\frac{14}{5}.             \tag{6}
\]
At the first endpoint, the first and third bounds follow respectively
from \(\sqrt5>20/9\) and \(\sqrt5>11/5\); the sine bound follows from
\(\sqrt5>111/50\). Each inequality persists in the indicated
direction as \(e\) increases. At \(e=1/2\), the first bound
is immediate and the other two remain strict.

Since
\[
 \left|\frac1{\sqrt{2-e^{-2\pi ie}}}\right|
       \le\frac1{\sqrt{2-\cos2\pi e}}<\frac35,
\]
equations (4)--(6) imply
\[
 -\Lambda''(e)
 <\frac{22}{7}\left(\frac13+\frac{24}{19}\right)
 =\frac{2002}{399}<\frac{51}{10}.                              \tag{7}
\]
Integration back from \(1/2\) gives
\[
                    \Lambda'(2/5)<-\log2+\frac{51}{100}.
                                                               \tag{8}
\]

For \(h\le0\), the shifted numerator modulus at \(e=.4\)
is at most \(2\). Differentiating the actual profile (1),
\[
 \begin{split}
 R_1'(.4,a)
 &=\Lambda'(.4)+\log|1-e^{-2\pi i(.4+a)}|
                                      -\log(2\sin(.4\pi))\\
 &<\frac{51}{100}-\log(19/10)<-\frac9{100}.                    \tag{9}
 \end{split}
\]
For the last strict inequality, the elementary exponential bound
gives
\[
 e^{3/5}
 \le1+\frac35+\frac{(3/5)^2}{2(1-(3/5)/3)}
     =\frac{73}{40}<\frac{19}{10}.                            \tag{10}
\]
No outgoing radius or reference has been chosen independently.

Strict concavity now proves
\[
 R_1(e,a)\le R_1(.4,a)-\frac9{100}(e-.4),
                                  \qquad .4\le e\le.49.       \tag{11}
\]
Together with (5) and (9), it also proves the following.

**Proposition 1.** For every target in (2), the maximum in (3)
is attained at one and only one real index \(\widehat e(a)\),
and
\[
              .27<\widehat e(a)<.4,\qquad
                       R_1'(\widehat e(a),a)=0 .              \tag{12}
\]
In particular
\[
             A^{\rm real}_1(a)=\max_{.27\le e\le.4}R_1(e,a).
                                                               \tag{13}
\]

The maximum is a real-envelope optimization. The reference cap
action and its complex stationary index are not replaced by
\(\widehat e(a)\).

## 3. Complete finite-envelope and derivative consequences

For actual own-four references, on their early tube \(c\le h\le0\), the
[complete early cap transport](research_mixed_cap_early_taper_envelope_transport.md)
proves that its true-index ceiling is strictly dominated by
\(A^{\rm real}_1\), with the fixed angular allowance included.
Equations (11)--(13) therefore reduce the entire completed
finite cap envelope to the same private interval \([.27,.4]\).
All compact physical tails, true ends, revived rows, fixed
ordinary-color jets, zeros and both parities remain accounted
for by that already proved source theorem. No source term is
removed solely because it is small at an isolated target.

Adding an adjoining rate, its original Fourier allocations,
marginals or compensation terms does not change the private
maximizer, since these terms are independent of \(e\).
Consequently the coupled derivative reduction of
[the two-incidence note](research_mixed_first_attached_two_incidence_reduction.md)
may retain
\[
                          e\in[.27,.4]                        \tag{14}
\]
when the first cap has own type four. The existing private
endpoint-minimum argument for the moving derivative applies
on this smaller interval too, so its two endpoint values become
\(e=.27,.4\), with the same actual height coefficients.

This restriction does not pay the remaining neighboring term
in that reduction, identify the maximum of the adjoining high
physical tail, or compare the joint envelope with its calibrated
reference. It supplies actual maximizing-profile information
which the earlier uniform first-coordinate slope discarded.
The own-three private interval is unchanged.

