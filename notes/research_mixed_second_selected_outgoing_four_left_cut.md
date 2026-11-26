# The outgoing four-type left cut at the second selection

Research deduction and fixed scalar-certificate design, 6 November 2026.
This treats the factor to the right of the selected coordinate.
Its outgoing argument keeps its negative original height. The analytic
reduction below leaves 128 fixed midpoint checks; their uniform sign
is a separate certificate requirement.

## 1. Exact difference and real-target reduction

Use the original bare own-four phase
\[
 Q(s;a,b)=g(s+a)+g(s+b)-3g(s)-g(a)-g(b)+2\pi ias,
 \qquad g'(w)=\Log(1-e^{-2\pi iw}).
 \tag{1}
\]
Let
\[
 \begin{split}
 l&=1/8,\quad s_h=3/10+ih,\quad
 a=x+iH,\quad b=y+ik,\quad H=1/100,\\
 x,y&\in P=[11/50,9/20],\qquad
 h,k\in[-51/500,-1/1000].
 \end{split}
 \tag{2}
\]
Define \(\Delta=\Re\{Q(s_h;a,b)-Q(l;a,b)\}\).
The main profile \(R_0=\max_{1/8\le t\le1/2}\Re Q(t+ih;a,b)\)
includes \(s_h\), while \(R_L=\Re Q(l;a,b)\). Thus
\[
                              R_0-R_L\ge\Delta.
 \tag{3}
\]
The outer terms \(-g(a)-g(b)\) cancel in the difference, but its
original chirp remains.

The two real-target second derivatives are
\[
 \Delta_{xx}=\pi\Re\{\cot\pi(s_h+a)-\cot\pi(l+a)\},\qquad
 \Delta_{yy}=\pi\Re\{\cot\pi(s_h+b)-\cot\pi(l+b)\}.
 \tag{4}
\]
They are strictly negative by Lemma 1 of the
[four-type corner reduction](research_mixed_selected_four_left_row_corners.md):
the trial real part is \(.3\), and each individual height has
modulus at most \(.102\). Consequently
\[
 \Delta(x,y,k,h)\ge
 \min_{\xi,\eta\in\{11/50,9/20\}}\Delta(\xi,\eta,k,h).
 \tag{5}
\]

## 2. Every corner increases with the outgoing height

Write \(A(t,q)=\arg(1-e^{2\pi q-2\pi it})\) on the original strip.
The outgoing height does not enter the chirp. Hence
\[
              \Delta_k=-A(3/10+y,h+k)+A(1/8+y,k).
 \tag{6}
\]
At \(y=11/50\), the two real parts are \(.52,.345\).
The first argument is strictly negative and the second strictly
positive, proving \(\Delta_k>0\).

At \(y=9/20\), put \(r_s=e^{2\pi h}\), \(r_b=e^{2\pi k}\).
The two arguments are evaluated at \(.75,.575\), so exactly
\[
 \Delta_k=
 \arctan(r_sr_b)
 -\arctan\frac{r_b\sin(.15\pi)}{1+r_b\cos(.15\pi)}.
 \tag{7}
\]
All arctangents here are real and positive. Since
\[
 .204\pi<\frac23<\log2,\qquad
 r_s\ge e^{-.204\pi}>\frac12,\qquad
 \sin(.15\pi)<\frac12,\quad \cos(.15\pi)>0,
 \tag{8}
\]
the first argument of the arctangent in (7) is larger than the
second. The elementary logarithmic bound in (8) follows from strict
convexity of \(1/t\):
\(\log2=\int_1^2dt/t>1/(3/2)=2/3\);
\(\pi<22/7\) proves its first inequality.
Thus \(\Delta_k>0\) at this corner as well. No relation between
the two target real parts was used.

Every corner minimum therefore occurs at \(k=-51/500\). Put
\[
 d_{\xi,\eta}(h)=\Delta(\xi,\eta,-51/500,h).
 \tag{9}
\]
Equations (5)--(8) give
\[
                   \Delta(x,y,k,h)\ge\min_{\xi,\eta}d_{\xi,\eta}(h).
 \tag{10}
\]

## 3. The fixed whole-height certificate

The real cut is independent of \(h\), and differentiation gives
\[
 \begin{split}
 d'_{\xi,\eta}(h)={}&-A(.3+\xi,h+.01)
                   -A(.3+\eta,h-.102)\\
                 &+3A(.3,h)-2\pi\xi .
 \end{split}
 \tag{11}
\]
The first three terms are nonnegative. Moreover the regular-strip
radius bounds give
\[
 -A(.3+\xi,\cdot)\le\pi(2\xi-.4),\quad
 -A(.3+\eta,\cdot)\le\pi(2\eta-.4),\quad
 0<A(.3,h)\le\pi/5
 \tag{12}
\]
because \(h<0\). It follows that
\[
                         -9\pi/10\le d'\le7\pi/10.
 \tag{13}
\]
The last term of (11) is the retained incoming chirp, not an
outgoing-height charge.

Partition \([-51/500,-1/1000]\) into 32 equal closed intervals
\([l_j,r_j]\) and set \(q_j=(l_j+r_j)/2\). The sufficient tests are
\[
 d_{\xi,\eta}(q_j)-\frac{9\pi}{10}\frac{r_j-l_j}{2}>
                 \frac1{1000},
 \quad 0\le j<32,\quad \xi,\eta\in\{11/50,9/20\}.
 \tag{14}
\]
The Lipschitz bound (13) makes each test a whole-interval inequality.
The [standalone checker](../experiments/check_mixed_second_selected_outgoing_four_left_cut.py)
uses 160-bit outward arithmetic with the original primitive
\[
                  g(w)=\frac{\operatorname{Li}_2(e^{-2\pi iw})-\pi^2/6}
                                           {2\pi i}
 \tag{15}
\]
and the exact canceled difference
\[
 \Re\{g(s_h+a)-g(l+a)+g(s_h+b)-g(l+b)
                         -3g(s_h)+3g(l)+2\pi ia(s_h-l)\}.
 \tag{16}
\]
It validates the primitive strips and dilogarithm cut, records all
128 rational lower and upper endpoints, binds its inputs before and
after evaluation, and refuses an existing output file.

An earlier authorized
[eight-endpoint diagnostic](../repro/results/research-mixed-second-selected-outgoing-four-left-cut-endpoints.json)
evaluated only the two extreme heights and four real corners, using
[this fixed diagnostic](../experiments/diagnose_mixed_second_selected_outgoing_four_left_cut.py).
Its smallest lower endpoint is greater than \(.00608\).
That record motivates (14); it is not used as a whole-height proof.
There is no adaptive cover, source root or finite quantum sum here.

**Proposition 1 (certificate implication).** If all 128 tests (14)
pass, then throughout (2)
\[
                              R_L<R_0-\frac1{1000}.
 \tag{17}
\]
Indeed (10), (13)--(14) bound every real target and both full height
intervals, and (3) transfers the strict lower bound to the main
profile. All common allocations and tangents may be added unchanged.

## 4. Its place in the finite second-selection problem

For \((\epsilon_1,\epsilon_2,\epsilon_3)=(\alpha,1,1)\), \(m\ge4\),
position 1 unselected and position 2 selected at height \(1/100\),
the right factor of the
[second-selection reduction](research_mixed_second_selected_plateau_reduction.md)
is precisely (1)--(2). Both \(h=\Im s_3^*\) and
\(k=\Im r_3\) obey the ordinary own-four interval in (2),
also when the fourth vertex is the terminal endpoint.

Thus (17), once certified, replaces every right profile \(L\)
by its corresponding main profile, for either complete Fourier
alternative and either left profile. The outgoing halfweight
\(|d_N(X_3)|^{1/2}\) is common and remains unchanged, as do
the original two boundary tangents.

Combined with the two last-row comparisons and the
[left-factor left-cut reduction](research_mixed_second_selected_left_cut_domination.md),
this leaves at most eight terms: left and right profiles in
\(\{0,R\}\), with two Fourier alternatives. Their signs remain
separate. No cap comparison for simultaneous first selections or
whole-source conclusion follows from this pointwise domination.
