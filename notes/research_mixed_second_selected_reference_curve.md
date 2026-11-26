# The original reference curve at the second selected position

Research deduction, 6 November 2026. The five references in the
[second-position central budget](research_mixed_second_selected_central_budget.md)
are rational functions of one original endpoint parameter. Two further
facts make this a usable reference chart: elementary argument bounds
recover the zero logarithmic lifts, and the original Hessian proves
that its next-external-coordinate projection has no ramification.
No root, finite source, parameter sweep or certificate is evaluated.

## 1. Two transfers, with the endpoint sign retained

Let \(m\ge4\), with first three flags \((\alpha,1,\beta)\).
Use exactly the budget's notation
\[
 (a,u,z,v,b)=(r_1,s_2^*,r_2,s_3^*,r_3).
 \tag{1}
\]
Write \(\xi\) for the auxiliary coordinate at the first endpoint,
\(e\) for its private leg, and \(c=s_4^*\) for the next external
leg. Thus \(c\) is attached when \(m=4\), ordinary when \(m\ge5\);
it is never the private terminal leg.

To avoid confusing the ordinary index \(u\) with the endpoint
parameter, put \(W=e^{2\pi i\xi}\). All the other exponentials
use the negative sign. The original
[rational endpoint map](research_mixed_rational_critical_transport.md),
equations (3)--(4), gives
\[
 \begin{split}
 D&=5W^2-2W+1,\qquad E=(1+W)^2/D,\\
 A&=\frac{1-(1-EW)(1-E)^\alpha/W}{E},\\
 U&=\frac{1-EA}{A(1-EA)+(1-A)^{2+\alpha}}.
 \end{split}
 \tag{2}
\]
Here \(E=e^{-2\pi ie}\), \(A=e^{-2\pi ia}\), and
\(U=e^{-2\pi iu}\). For \(p=2,3\), define
\[
 \begin{split}
 T_p(P,Q)&=(R,T),\\
 R&=\frac{1-P(1-Q)^p/(1-PQ)}{Q},\\
 T&=\frac{1-QR}{R(1-QR)+(1-R)^p}.
 \end{split}
 \tag{3}
\]
The required two iterations are precisely
\[
                 (Z,V)=T_3(A,U),\qquad
                 (B,C)=T_{2+\beta}(Z,V).
 \tag{4}
\]
Their meanings are
\[
 Z=e^{-2\pi iz},\quad V=e^{-2\pi iv},\quad
 B=e^{-2\pi ib},\quad C=e^{-2\pi ic}.
 \tag{5}
\]
Thus (2)--(4), rather than five independent coordinate boxes, give
every reference needed by the central majorant. In particular the
second retained coordinate \(Z\) depends on \(\alpha,W\);
\(\beta\) and the suffix restrict which \(W\)'s are admissible.

Every division must be regular. At a transfer these conditions include
\(P,Q,R,T\ne0\), \(1-PQ,1-QR,1-RT,1-Q,1-R\ne0\), and the
two displayed denominators. At the endpoint retain \(W,D,E,A,U\ne0\)
and \(1-EW,1-E,1-EA,1-UA,1-A\ne0\).
The original critical points satisfy all these conditions. In particular
the last denominator of (3) equals \((1-QR)/T\), and the last
denominator of (2) equals \((1-EA)/U\). An interval overlapping a
forbidden zero is inconclusive; it is not an exclusion.

## 2. Necessary filters independent of the remaining word

For the negative-sign shapes \(X\in\{E,A,U,Z,V,B,C\}\), decode
the corresponding coordinate by
\[
                         \ell(X)=\frac{i}{2\pi}\Log X.
 \tag{6}
\]
The positive-sign shape \(W=e^{2\pi i\xi}\) retains its separate
endpoint convention. The principal logarithm in (6) is correct because
every decoded leg below has real part strictly between zero and \(1/2\).
Let
\[
 \begin{split}
 P_3&=\{|w-(.35-.01i)|\le.083\},\\
 P_4&=\{|w-(.30-.052i)|\le.060\},\\
 O_3&=P_3\cap([.267,.433]+i[-.065,.068]),\\
 O_4&=P_4\cap([.24,.36]+i[-.102,-.001]).
 \end{split}
 \tag{7}
\]
Closed intervals are safe enclosures; actual references satisfy the
corresponding strict bounds. Use the following filters:

* The endpoint coordinates \((e,a,\xi)\) obey the row of the
  [endpoint rectangle theorem](research_mixed_open_word_endpoint_rectangles.md)
  for type \(3+\alpha\), and \(a\in P_{3+\alpha}\). In particular
  \(\xi\in[.218,.242]+i[.049,.077]\) for \(\alpha=0\), and
  \(\xi\in[.217,.234]+i[.027,.045]\) for \(\alpha=1\).
* \(u,z\in O_4\) and \(v,b\in O_{3+\beta}\).
* For at least one next type \(3+\sigma\), \(c\in K_{3+\sigma}\),
  where the [typed envelopes](research_mixed_typed_last_row_envelopes.md)
  are
  \[
  \begin{split}
  K_3&=P_3\cap\{-.072\le\Im c\le.068,\
                       \Re c-3\Im c\le.608\},\\
  K_4&=P_4\cap\{-.108\le\Im c\le-.001\}.
  \end{split}
  \tag{8}
  \]
  To exclude an unknown next type, both alternatives must be excluded.

The [reduced-disk pair-sum theorem](research_mixed_reduced_disk_pair_sums.md)
also gives
\[
 .545<\Re(a+u),\Re(z+v),\Re(b+c)<.77,\qquad
 \Re(u+z),\Re(v+b)<.77.
 \tag{9}
\]
For the first internal sum the lower bound is \(.49,.525,.55\)
according as \((\alpha,\beta)\) has zero, one or two four-flags.
For the second it is \(.6\) if \(\beta=0\), and \(.525\) or
\(.55\) if \(\beta=1,\sigma=0\) or \(1\), respectively.
These follow by applying that theorem to external pairs
\((a,v)\) and \((z,c)\). Both external legs lie in the reduced
disks; no periodic repetition of the word is used.

Optional stronger filters retain their orientation. From the
[adjacent-four image bounds](research_mixed_first_cap_oriented_plateau_certificate.md),
\(\Re u>.259\) when \(\alpha=1\), \(\Re z>.259\) when
\(\beta=1\), and \(\Re v>.259\) when \(\beta=1\).
If also \(\sigma=1\), then \(\Re b>.259\); the both-external-four
cases permit the stronger \(.263\) bound stated there.
The [coupled endpoint height theorem](research_mixed_first_four_attached_height_bound.md)
gives \(-.078<\Im a<-.020\) when \(\alpha=1\).
None of these is a universal type-four coordinate bound.

At a known length four one may replace (8) by the corresponding
attached rectangle intersected with \(P_{3+\sigma}\); at length at
least five use \(O_{3+\sigma}\). The union (8) is enough for a
single evaluator uniform over every suffix and every \(m\ge4\).

## 3. The filters recover the original logarithmic lifts

Here is a useful addition to merely exponentiating the equations.
Put \(L(w)=\Log(1-e^{-2\pi iw})\) on the original regular strip.
For any real \(h\),
\[
 \begin{array}{ll}
 0<\arg(1-e^{-2\pi i(x+ih)})<\pi(1-2x),&0<x<1/2,\\
 \pi(1-2x)<\arg(1-e^{-2\pi i(x+ih)})<0,&1/2<x<1.
 \end{array}
 \tag{10}
\]
At \(x=1/2\) the argument is zero. These bounds follow by varying
the positive radius of \(e^{-2\pi i(x+ih)}\); they do not bound \(h\).

**Lemma 1.** A point of (2)--(5) satisfying the endpoint rectangles,
(7)--(9), and the regular divisions satisfies the original zero-lift
endpoint equations and both original ordinary block equations.

For an ordinary coordinate \(s\), its own partner \(t\), and
adjacent external coordinate \(q\), the residual is
\[
                 L(s+t)+L(s+q)-pL(s)+2\pi iq.
 \tag{11}
\]
Its exponential is one by (3). The wire sum in (9) exceeds \(1/2\).
For \(p=3\), both own real parts lie in \([.24,.36]\).
If \(\Re(s+t)\ge1/2\), (10) bounds the imaginary part of (11),
divided by \(\pi\), below by
\(-1+2\Re s-2\Re t\ge-1.24\).
If \(\Re(s+t)\le1/2\), the lower bound is
\(-2+4\Re s\ge-1.04\). Its upper bound is at most
\(.02+2(.45)=.92\), using \(\Re(s+t)\ge.49\).
For \(p=2\), both sums exceed \(1/2\), and the bounds are
\(-2\Re t\ge-.866\) and \(2\Re q\le.9\).
Every residual therefore lies strictly between \(-2\pi i\) and
\(2\pi i\) on the imaginary axis and must be zero.

At the endpoint, the attached residual has the same form (11),
with \(s=a,t=e,q=u,p=2+\alpha\). Both sums exceed \(1/2\).
For \(\alpha=0\) its lower bound is \(-2\Re e>-.876\);
for \(\alpha=1\) it is
\(-1+2\Re a-2\Re e>-1.234\). Its upper bound is less than
\(.72\). The private residual, in the same original branch, is
\[
                  L(e+a)-L(e-\xi)-\alpha L(e)+2\pi i\xi.
 \tag{12}
\]
Its imaginary part divided by \(\pi\) lies above
\(-2\Re a-\alpha+2\alpha\Re e\), hence above \(-1.034\),
and below \(2\Re\xi<.484\). Both residuals exponentiate to one
by (2), so they too vanish.

Finally the original auxiliary residual, expressed with \(W\), is
\[
 2\Log(1+W)+\Log(1-EW)-3\Log(1-W)+2\pi i(e-1).
 \tag{13}
\]
This identity follows directly from the sine/cosine expressions in
[the original endpoint equations](research_mixed_open_word_critical_localization.md),
equation (6). Here \(0<\arg W<\pi/2\), \(|W|<1\),
\(0<\Re(e-\xi)<1/2\). Consequently
\[
 0<\arg(1+W)<\pi/4,\quad
 -\pi/2<\arg(1-W)<0,\quad
 0<\arg(1-EW)<\pi.
 \tag{14}
\]
The imaginary part of (13), divided by \(\pi\), lies between
\(2(\Re e-1)>-1.334\) and \(1+2\Re e<1.876\).
Its exponential is one because
\((1+W)^2(1-EW)=E(1-W)^3\). It is therefore zero.
All seven equations retain their original logarithms and chirps.
This proves the lemma. \(\square\)

In particular the endpoint auxiliary is the canonical \(\xi=u_c(e)\),
by uniqueness in the original endpoint chamber. The argument does
not require a newly selected polynomial root or an assumed connected
component of the auxiliary rectangle.

## 4. A genuine canonical prefix, not an independently chosen saddle

Fix \(c\) in either original input disk \(D_3,D_4\), with the
same centers as (7) and radii \(.09,.064\). Update the three
disjoint coordinate groups
\[
 (e,a,\xi)=\text{endpoint}_{\alpha}(u),\qquad
 (u,z)=\text{ordinary}_{1}(a,v),\qquad
 (v,b)=\text{ordinary}_{\beta}(z,c).
 \tag{15}
\]
The already proved original maps send their compact typed products
into themselves. Brouwer gives a fixed point. Its seven-variable
Jacobian is the principal block of the original length-four Hessian,
with \(s_4=c\) and the remaining right-end coordinates fixed.
The [original Hessian bound](research_mixed_open_word_hessian.md)
therefore gives \(-\Re F_{\rm prefix}''>(6\pi/49)I\).
It proves uniqueness throughout the common convex product and
holomorphic dependence on \(c\) near each point of the closed disk.
The maps for the two choices of the next type agree on overlaps,
because the prefix equations themselves do not depend on that type.

For \(c\in K_3\cup K_4\), its canonical solution obeys all mandatory
filters in Section 2. Conversely Lemma 1 identifies every filtered
rational point with this canonical solution for its own \(c\).
It need not extend to any prescribed finite suffix.

There is also no ramification in the projection \(C=C(W)\) on
this filtered curve. Near any filtered point the exponentiated
identities hold on a regular complex neighborhood; their logarithmic
residuals are locally constant in \(2\pi i\mathbb Z\). Lemma 1
sets those constants to zero. This also justifies differentiation
at a point on a clipping boundary. Differentiate the seven equations with
respect to \(\xi\). If \(dc/d\xi=0\), the nonsingular prefix
Jacobian would force all seven derivatives to vanish, including
the derivative \(d\xi/d\xi=1\). This is impossible. Hence
\[
                              C'(W)\ne0.
 \tag{16}
\]
If two filtered parameters have the same \(c\), uniqueness forces
their seven coordinates, including \(\xi\), to agree. Thus this
restricted projection is injective. This statement concerns the
filtered canonical prefix, not the global rational map on the sphere.

## 5. Direct data and correlated derivatives for the central test

With \(g'=L\), the two original boundary marginals are
\[
 \begin{split}
 p_L&=L(a+u)-(1+\alpha/2)L(a)+2\pi iu,\\
 p_R&=L(v+b)-(1+\beta/2)L(b).
 \end{split}
 \tag{17}
\]
The internal equations \(F_u=F_z=F_v=0\) in the central budget
are among the zero equations just proved. In particular all vertical
costs, final gradients, target displacements and boundary tangents
in that budget can be evaluated from the same \(\xi\) in (2)--(6).
The selected target height changes none of these reference maps.

The derivatives are rational before taking logarithms. For any shape
\(X(W)\),
\[
             \frac{d\,\ell(X(W))}{d\xi}
                         =-\frac{W X'(W)}{X(W)}.
 \tag{18}
\]
For an explicit transfer differentiation set
\[
 n=1-PQ,\quad h=(1-Q)^p,\quad f=n-Ph,\quad
 R=f/(Qn),\quad k=1-QR,\quad d=Rk+(1-R)^p.
 \tag{19}
\]
For any shared parameter differential,
\[
 \begin{split}
 dn&=-Q\,dP-P\,dQ,\qquad dh=-p(1-Q)^{p-1}dQ,\\
 df&=dn-h\,dP-P\,dh,\qquad
 dR=R(df/f-dQ/Q-dn/n),\\
 dk&=-R\,dQ-Q\,dR,\qquad
 dd=(k-p(1-R)^{p-1})dR+R\,dk,\\
 dT&=T(dk/k-dd/d).
 \end{split}
 \tag{20}
\]
All denominators here are already nonzero on the admitted chart.
These formulas permit a common-point plus whole-parameter-derivative
enclosure for a combined scalar test; no implicit root response is
needed. Necessary coordinate intersections may tighten pointwise
values. They cannot replace the full rational images when enclosing
derivatives on an entire auxiliary rectangle.

## 6. The precise remaining second-height inequality

The current geometry gives only \(-.102<\Im z<-.001\) universally.
Write, using the first transfer,
\[
 N_2=1-AU-A(1-U)^3,\qquad D_2=U(1-AU),\qquad Z=N_2/D_2.
 \tag{21}
\]
The proposed useful strengthening is exactly
\[
 \Im z\le-1/50
 \quad\Longleftrightarrow\quad
 |N_2|^2\le e^{-2\pi/25}|D_2|^2.
 \tag{22}
\]
It must be proved on the filtered curve for both \(\alpha,\beta\)
and both suffix-type alternatives. Formula (22) is not a consequence
of the existing independent ordinary rectangle; no sign for it is
claimed here.

There is a smaller exact boundary formulation: the canonical \(z(c)\)
of Section 4 is holomorphic on a neighborhood of either \(K_3\) or
\(K_4\). Its imaginary part is harmonic. Thus the maximum of
\(\Im z\) over either compact envelope occurs on its complete
boundary (circle arcs and every clipping segment). A bound there
would prove (22) for every actual suffix without independently
maximizing the other four coordinates. Neither that boundary bound
nor any selected-source comparison has been evaluated in this note.
