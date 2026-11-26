# A half-plane bound for the original reference shapes

Research lemma, 6 November 2026. This supplies a necessary condition
that can be checked before taking a complex logarithm.

Use the original reference coordinates
\((e,a,u,z,v,b,c)\) in the
[second-selection reference theorem](research_mixed_second_selected_reference_curve.md).
Here \(e\) is the private endpoint coordinate, \(a\) its attached output,
\(u,z\) the first ordinary pair, \(v,b\) the second ordinary pair,
and \(c\) the next external coordinate. The first endpoint flag and
the second ordinary flag may each be zero or one.
Every one of these seven coordinates satisfies
\[
        \frac{11}{50}\le\Re w\le\frac9{20},\qquad
                         \Im w\ge-\frac{27}{250}.
        \tag{1}
\]
For the ordinary and next external coordinates this follows from
the sets \(O_3,O_4,K_3,K_4\) in that theorem.
For \(e,a\), it follows from the two rows of the
[endpoint rectangle theorem](research_mixed_open_word_endpoint_rectangles.md).
These are bounds for reference coordinates. They are not restrictions
on the independent contour targets.

**Lemma.** Every negative-sign shape \(X=\exp(-2\pi i w)\) from (1)
satisfies
\[
                              \Im X<-\frac3{20}.
                              \tag{2}
\]

Write \(w=x+ih\). Then
\[
          \Im X=-e^{2\pi h}\sin(2\pi x).
          \tag{3}
\]
The sine on the interval in (1) is at least
\(\sin(\pi/10)=(\sqrt5-1)/4>3/10\), since \(\sqrt5>11/5\).
For the radial factor, \(\pi<22/7\) gives
\[
 \frac{27\pi}{125}<\frac{594}{875}<\frac{17}{25}.
 \tag{4}
\]
The positive exponential series, at \(t=17/25\), gives the rational
upper bound
\[
 e^t\le\sum_{j=0}^{5}\frac{t^j}{j!}
       +\frac{t^6}{6!(1-t/7)}
       =\frac{2192855025919}{1110937500000}<2.
       \tag{5}
\]
Indeed the successive ratios in the tail after its first term
are at most \(t/7\). Equations (1), (4), and (5) imply
\(e^{2\pi h}>1/2\). Substitution in (3) proves (2).

Consequently, if a whole-parameter enclosure of any one of
\(E,A,U,Z,V,B,C\) has imaginary lower endpoint strictly greater
than \(-3/20\), that parameter cell contains no admissible reference.
This conclusion needs neither a decoded logarithm nor values of the
later rational maps. The enclosure must still contain the original
rational shape at every regular admissible point.

An interval crossing the cutoff is inconclusive. A successful
exclusion removes no possible original reference; it does not
prove a scalar rate estimate. The positive-sign auxiliary
\(W=\exp(2\pi i\xi)\) is not among the shapes in this lemma.
