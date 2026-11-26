# The actual following-reference curve and its boundary comparisons

Research deduction, 7 November 2026. The rational Gram closing map
already present in the ordinary critical transport has a canonical
global sheet for the cap-initialized \(34\) prefix. On the union of
the two following typed disks, both its endpoint parameter and its
last prefix leg are one-to-one holomorphic coordinates. This reduces
the actual following-reference action comparison from independent
neighboring boxes to finitely many one-real-parameter boundary curves.
The boundary signs are not proved here. No numerical evaluation is
used.

## 1. The existing rational map with the actual Gram closing

Use the variables of
[the prepared-cap critical curve](research_mixed_prepared_three_four_cap_critical_curve.md):
\[
 U=e^{-2\pi iu},\quad Z=e^{-2\pi is},\quad
 T=e^{-2\pi it},\quad P=e^{-2\pi ip},\quad
 Q=e^{-2\pi iq},\qquad C=e^{-2\pi ic}.
 \tag{1}
\]
Here \(s,t\) are the first type-three vertex's private and
attached legs, and \(p,q\) are the second type-four vertex's
legs. The external \(c\) is the following Gram coordinate.
It is neither the original right ordinary endpoint nor the
Fourier wire coordinate used in the last equation of that source.

Keep the literal original action
\[
 \begin{split}
 B(s,u)&=-2J(1/2-u)-3J(u)-J(s-u)
                   +i\pi su-\frac{i\pi}{2}(s-s^2),\\
 \mathcal A(u,s,t,p,q;c)
   &=B(s,u)+g(s+t)+g(t+p)+g(p+q)\\
   &\hspace{8mm}-2g(t)-3g(p)-g(q)+2\pi itp+G(q,c),\\
 G(q,c)&=g(q+c)-2g(q)-2g(c)+2\pi iqc .
 \end{split}
 \tag{2}
\]
The first four equations in the prepared critical curve are
unchanged. They give the existing rational functions
\[
 \begin{split}
 Z(U)&=\frac{(U+1)^2}{U^2-2U+5},&
 T(U)&=\frac{1+Z(U)-U}{Z(U)},\\
 P(U)&=\frac{1-Z(U)T(U)}
               {(1-T(U))^2+T(U)(1-Z(U)T(U))},\\
 Q(U)&=\frac{1-T(U)(1-P(U))^3/(1-T(U)P(U))}{P(U)} .
 \end{split}
 \tag{3}
\]
Before closing, the retained derivative is
\(\mathcal P_{34}'(q)=g'(p+q)-g'(q)\). Adding the actual
Gram incidence makes its equation
\[
 \begin{split}
 0={}&\Log(1-PQ)+\Log(1-QC)-3\Log(1-Q)+2\pi ic,\\
 (1-PQ)(1-QC)&=C(1-Q)^3.
 \end{split}
 \tag{4}
\]
Consequently the external exponential is
\[
 \boxed{\displaystyle
 \mathcal C(U)=
 \frac{1-P(U)Q(U)}
 {Q(U)(1-P(U)Q(U))+(1-Q(U))^3}.}
 \tag{5}
\]
This is exactly the own-four instance of the existing rational
transfer in [rational critical transport](research_mixed_rational_critical_transport.md),
Section 2. Formula (5) is not claimed as a new general transfer.
The statements below specify its actual global sheet and a useful
maximum principle on that sheet.

At an original critical point every denominator in (3)--(5) is
nonzero. In particular the denominator in (5) equals
\((1-PQ)/C\). The original sum strip excludes \(PQ=1\),
and \(C\) is a nonzero exponential. No zero of a cleared
denominator is admitted.

## 2. Original logarithmic lifts on the following domains

Put
\[
 \begin{split}
 D_3&=\{|c-(.35-.01i)|\le.09\},\\
 D_4&=\{|c-(.30-.052i)|\le.064\},\qquad
 \Omega=\operatorname{int}D_3\cup\operatorname{int}D_4 .
 \end{split}
 \tag{6}
\]
The [actual cap-phase entrance theorem](research_mixed_alternating_cap_phase_entrance.md),
Lemma 1, already proves a unique original-log root of (2) for
every \(c\) in either full closed disk. The roots glue on their
overlap by uniqueness. The endpoint and ordinary whole-map image
bounds give, strictly,
\[
 \begin{array}{c|c}
 \text{coordinate}&\text{range needed below}\\ \hline
 s&(.376,.438)+i(-.019,.037)\\
 u&(.218,.242)+i(.049,.077)\\
 t&A_3\subset(.278,.391)+i(-.072,.021)\\
 p,q&O_4\subset(.24,.36)+i(-.102,-.001).
 \end{array}
 \tag{7}
\]
The domains \(A_3,O_4\) are those of
[actual last-row references](research_mixed_actual_last_row_reference_domains.md).
The first two rows come from
[the original endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md).
Their use is valid on the full typed input disks of the endpoint
maps, not only at a closed word.

For completeness, a rational preimage of (5) whose coordinate lifts
obey (7) solves the original equations, rather than merely their
exponentials. All single and sum logarithms have real arguments in
\((0,1)\), and \(0<\Re u<\Re s<1/2\), \(\Im u>0\).
For every \(r>0\) and \(0<x<1\),
\[
 \min\{0,\pi(1-2x)\}
 <\Arg(1-re^{-2\pi ix})
 <\max\{0,\pi(1-2x)\},
 \tag{8}
\]
with the zero value used when \(x=1/2\).
The endpoint and private-leg lift arguments in the prepared
critical-curve proof apply unchanged.

Here are explicit bounds for the other three derivatives. Write
real parts as \(s_R,t_R,p_R,q_R,c_R\).
The sums \(s_R+t_R,t_R+p_R\) are greater than one half;
the positive allowances for the remaining sums \(p_R+q_R\)
and \(q_R+c_R\), after division by \(\pi\), are at most
\(1/25\) and \(6/125\), respectively. In particular
\[
 \begin{array}{c|cc}
 &\text{strict lower bound for }\Im\mathcal A_j/\pi
 &\text{strict upper bound}\\ \hline
 t&-2s_R>-1&2p_R<18/25\\
 p&-26/25+2p_R-2q_R>-32/25&1/25+2t_R<411/500\\
 q&-136/125-2p_R+2q_R>-166/125&
                       11/125+2c_R<121/125 .
 \end{array}
 \tag{9}
\]
For example the lower bound in the last line uses the two lower
sum-argument bounds from (8), the upper bound
\(3\pi(1-2q_R)\) for the subtracted single-leg arguments,
and the actual chirp \(2\pi c_R\). Its \(c_R\) terms cancel.
All rows lie strictly between \(-2\pi\) and \(2\pi\).
Since exponentiation puts each derivative in
\(2\pi i\mathbb Z\), every lift is zero.
Thus (5), with the admitted original ranges and nonvanishing
conditions, is equivalent to the original Gram closing.

## 3. One global conformal sheet for the actual prefix

Write the proved root as
\[
 z(c)=(u(c),s(c),t(c),p(c),q(c)),\qquad
 H(c)=\mathcal A(z(c);c).
 \tag{10}
\]
Both functions are holomorphic near the two closed disks and agree
on their overlap. Let \(\mathcal H=\mathcal A_{zz}''\) at the
root, and let \(\mathcal H_0\) be its principal block obtained
by deleting the last coordinate \(q\). Original accretivity
implies that both matrices are nonsingular. Since only the last
gradient has an external derivative,
\[
 q'(c)=
  -\frac{\det\mathcal H_0}{\det\mathcal H}
                     \frac{2\pi i}{1-Q(c)C(c)}\ne0 .
 \tag{11}
\]
There is no conjugation in this implicit derivative.

The full Hessian is tridiagonal in the order in (10).
Its four adjacent entries are
\[
 \frac{2\pi i}{1-Z/U},\qquad
 \frac{2\pi iZT}{1-ZT},\qquad
 \frac{2\pi i}{1-TP},\qquad
 \frac{2\pi iPQ}{1-PQ},
 \tag{12}
\]
and none vanishes. The corner cofactor formula therefore gives
\(u'(c)\ne0\), and hence \(U'(c)\ne0\). Differentiating (5)
on the actual branch yields
\[
             \mathcal C'(U(c))U'(c)
                      =-2\pi i e^{-2\pi ic}\ne0.        \tag{13}
\]
This proves nonramification at every actual following input,
not just at one admitted preimage.

**Proposition 1.** Both \(c\mapsto U(c)\) and
\(c\mapsto q(c)\) are one-to-one holomorphic maps on \(\Omega\).
The actual rational sheet is \(U(\Omega)\), with inverse given
by (5) and the unique \(c\)-lift in \(\Omega\).

*Proof.* If \(U(c_1)=U(c_2)\), the rational formulas give the
same \(C\). The total real width of \(\Omega\) is less than
one, so equality of \(e^{-2\pi ic}\) implies \(c_1=c_2\).

Suppose instead that \(q(c_1)=q(c_2)\). With that value of \(q\)
fixed, the four equations for \(u,s,t,p\) do not contain \(c\).
Their negative real Hessian is the corresponding principal block
of the original accretive Hessian on the common larger convex
endpoint/leg product. Integrating along the segment joining two
candidate internal roots proves injectivity of this gradient.
Thus their four internal coordinates coincide. Equation (5)
then gives the same \(C\), and again \(c_1=c_2\).
The nonzero derivatives in (11)--(13) give holomorphic local
inverses, which glue by this injectivity. \(\square\)

There is consequently one absolute pre-Gram action on the actual
image \(q(\Omega)\):
\[
 \begin{split}
 \mathscr P(c)&=H(c)-G(q(c),c),\\
 \mathcal P_{\rm act}(q)&=
         \mathscr P\bigl(q^{-1}(q)\bigr),\\
 \mathcal P_{\rm act}'(q)&=g'(p+q)-g'(q).
 \end{split}
 \tag{14}
\]
In the middle line, \(q^{-1}\) denotes the inverse map of
Proposition 1. The last line follows by stationary differentiation.
All constants are fixed by (2). This is a geometric continuation
on the actual image; it is not a whole finite-source continuation.
Where the image overlaps the proved prefix germ at its original
private reference, uniqueness identifies their actions.
No assertion that the saved private reference, or its effective
Gram neighbor, lies in this image is needed or made.

## 4. A finite boundary reduction for the actual remainder deficit

The fixed left ordinary cap is now retained in the map \(z(c)\).
In particular \(t(c)\) is no longer an independently varying
attached input. For a next terminal vertex of type \(\nu=3,4\),
the sufficient following parameter set is \(c\in A_\nu\);
for a next ordinary vertex it is \(c\in O_\nu\). These are the
four compact clipped domains defined in the actual-reference note.
They are strictly inside \(\Omega\). Their actual occurrences
may be smaller correlated subsets, but their images under \(q(c)\)
are sufficient enclosures for this fixed prefix.

Let \(K\) be any one of these four domains. Set
\[
 h(c)=\Im q(c),\qquad R(c)=e^{2\pi h(c)}.
 \tag{15}
\]
The whole-map bound (7) keeps \(h<0\) and \(1/2<R<1\)
on a neighborhood of \(K\).
The complete complementary source has the proved ceiling
\[
 \begin{split}
 \mathfrak C(R)
  &=C_+-\frac{23}{64000}-\frac6{25}\beta(R)
                                  +\frac{\beta(R)^2}{20},\\
 C_+&=\frac{17539}{9600},\qquad
 \beta(R)=\frac12\log\frac2{1+R^2},
 \end{split}
 \tag{16}
\]
by [the outgoing-radius theorem](research_mixed_transformed_following_four_radial_majorant.md).
Its incoming deformation is the same fixed contour for every
output; no moving contour maximum is being differentiated here.
The complete initial interval has the independent ceiling \(7/4\).

Define the two actual deficits
\[
 D_+(c)=\mathfrak C(R(c))-\Re\mathscr P(c),\qquad
 D_0(c)=7/4-\Re\mathscr P(c).
 \tag{17}
\]

**Theorem 2.** On each of the four domains \(K\),
\[
       \max_K D_+=\max_{\partial K}D_+,\qquad
       \max_K D_0=\max_{\partial K}D_0.                \tag{18}
\]
Moreover \(D_+\) is strictly subharmonic. There is a constant
\(m_K>0\), defined without a numerical evaluation, such that
\[
 D_+(c)\le
  \max_{\partial K}D_+
       -\frac{m_K}{4}\operatorname{dist}(c,\partial K)^2
                     \qquad(c\in K).                 \tag{19}
\]

*Proof.* Write \(b(h)=\beta(e^{2\pi h})\). Direct
differentiation gives
\[
 b'(h)=-\frac{2\pi e^{4\pi h}}{1+e^{4\pi h}},\qquad
 b''(h)=-\frac{8\pi^2e^{4\pi h}}{(1+e^{4\pi h})^2}<0.
 \tag{20}
\]
For \(h<0\), \(0<b(h)<(\log2)/2<7/20\).
The outer polynomial
\(C_+-23/64000-6b/25+b^2/20\) has positive second
derivative \(1/10\) and strictly negative first derivative
\(-6/25+b/10\). Hence the composed function
\(\mathcal B(h)=\mathfrak C(e^{2\pi h})\) satisfies
\[
 \mathcal B''(h)
    =\frac{b'(h)^2}{10}
       +\left(-\frac6{25}+\frac{b(h)}{10}\right)b''(h)>0.
 \tag{21}
\]
Both \(h(c)\) and \(\Re\mathscr P(c)\) are harmonic.
Since \(q\) is holomorphic and \(q'\ne0\),
\[
          \Delta D_+(c)=\mathcal B''(h(c))|q'(c)|^2>0,
                       \qquad \Delta D_0(c)=0.        \tag{22}
\]
The maximum principles prove (18). Compactness permits
\[
 m_K=\min_{c\in K}\mathcal B''(h(c))|q'(c)|^2>0.
 \tag{23}
\]
For an interior \(c\), apply the submean inequality to
\(D_+(\zeta)-m_K|\zeta-c|^2/4\) on any disk centered at
\(c\) inside \(K\), and use (18) to bound its circular
values. Let its radius increase to
\(\operatorname{dist}(c,\partial K)\). This gives (19).
\(\square\)

Every \(\partial K\) is a finite union of portions of a fixed
circle and horizontal or vertical clipping chords, with their
endpoints retained. Thus (18) is an explicit reduction to finitely
many one-real-parameter curves
\[
             c\longmapsto (U(c),t(c),p(c),q(c),\mathscr P(c)).
 \tag{24}
\]
It is smaller than the independent products
\(A_3\times A_\nu\) or \(A_3\times O_\nu\) used when
only a single ordinary block is retained.
No proper part of a clipping chord can be discarded on the
basis of a circle-only maximum principle.

If both boundary deficits in (18) have a negative uniform margin,
the existing whole-source bounds pay these two complete prefix
remainders throughout \(K\), in the normalization
\(e^{-N\mathscr P(c)}\). Strict margins persist on neighborhoods,
where the original polynomial bounds and Cauchy's formula give
fixed derivatives. Neither (18) nor (19) proves those boundary
signs. They do not estimate the other prefix contour pieces,
remove either sector of the next \(d_N(Y)(1+Y^{-N})\) transfer,
or give a nonzero observed coefficient for the next short word.

## 5. Different valid boundary majorants can be combined

The global sheet also permits a direct maximum principle for the
exact finite remainder. At complete left ordinary color define
\[
 \mathcal R_N(c)=e^{-N\mathscr P(c)}
                  f_{+,N}(-2,e^{-2\pi iq(c)}).
 \tag{25}
\]
The finite source is a polynomial in its outgoing exponential,
and both \(q\) and \(\mathscr P\) are holomorphic on \(\Omega\).
Thus (25) is holomorphic on that entire domain, with no division
by a finite prefix value.

**Corollary 3.** Cover \(\partial K\) by finitely many closed
arcs or chord portions \(I_1,\ldots,I_L\), retaining every
endpoint. Suppose valid estimates for the original complete
remainder give
\[
 |\mathcal R_N(c)|\le C_jN^{B_j}e^{-\delta_jN}
       \quad(c\in I_j),\qquad \delta_j>0.
 \tag{26}
\]
Then, with \(C=\max_jC_j\), \(B=\max_jB_j\) and
\(\delta=\min_j\delta_j\),
\[
             |\mathcal R_N(c)|\le CN^Be^{-\delta N}
                                \qquad(c\in K).
 \tag{27}
\]

*Proof.* Equations (26) bound the whole boundary by the right side
of (27). Apply the maximum-modulus principle to the actual
holomorphic function (25) on the interior of \(K\), and use
continuity on its closure. \(\square\)

For example one may use the radial ceiling on some pieces and
the [angular-majorant theorem](research_mixed_transformed_following_four_angular_majorant.md)
on others, provided each chosen complete-source estimate gives
the required positive action gap there. This argument does not
assert that the minimum of their scalar profiles is subharmonic.
It uses the same exact normalized finite function on every piece.
If the boundary estimates have strict rate margins and the
uniform source neighborhoods already supplied by those theorems,
compactness and continuity give them on a fixed small boundary
neighborhood after reducing the gap. Applying the same principle
on a slightly enlarged \(K\), then Cauchy's formula, gives every
fixed \(c\)-derivative on \(K\). Additional holomorphic parameters
can be treated the same way when their uniform boundary
hypotheses are supplied.

No boundary signs in (26) are asserted here. This corollary
permits the valid majorants to be combined after such signs are
proved; it is not a new estimate for the unobserved complementary
cycle or either later Fourier sector.
