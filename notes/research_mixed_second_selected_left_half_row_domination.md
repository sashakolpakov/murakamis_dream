# Dominating the left half row at the second selection

Research deduction, 6 November 2026. A fixed point of the original
own-four main contour can dominate its real half-row profile when the
outgoing argument is selected. The analytic reduction below leaves
32 fixed scalar interval checks. Their signs are not asserted until
the complete saved record passes. No root, finite source, or adaptive
parameter cover is part of this deduction.

## 1. The literal phase and the containing domain

Retain the bare own-four phase of the
[second-selection reduction](research_mixed_second_selected_plateau_reduction.md):
\[
 Q(s;a,b)=g(s+a)+g(s+b)-3g(s)-g(a)-g(b)+2\pi ias.
 \tag{1}
\]
Its primitive, logarithms, and chirp are unchanged. Let
\[
 \begin{gathered}
 a=x+ik,\quad b=y+iH,\quad x,y\in P=[11/50,9/20],
 \quad H=1/100,\\
 -39/500\le k\le21/1000,\qquad
 s_h=3/10+ih,\quad -51/500\le h\le-1/1000.
 \end{gathered}
 \tag{2}
\]
For a word of length at least four with second type four and first
position unselected, the actual first attached height belongs to this
interval. This uses the
[endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
for first type three and the
[coupled attached-height theorem](research_mixed_first_four_attached_height_bound.md)
for first type four. The index height is the unchanged ordinary
own-four height. The later type does not affect this bare comparison.

Define
\[
 \Delta(x,y,k,h)=\Re\{Q(s_h;x+ik,y+iH)-Q(1/2;x+ik,y+iH)\}.
 \tag{3}
\]
The main profile includes \(s_h\). Therefore a proof of
\(\Delta>1/30\) on (2) would give the pointwise comparison
\[
 R_R^2<R_0^2-1/30.
 \tag{4}
\]
Every common outgoing or incoming halfweight, selected Fourier
alternative, and affine subtraction preserves (4).

## 2. The incoming real coordinate and height

Put \(S=e^{-2\pi is_h}\), \(A=e^{-2\pi ia}\),
\(r=|S|<1\), and \(t=|A|>0\). Differentiation in the
incoming real variable, including the chirp, gives
\[
 \partial_x\Delta=\log\left|\frac{S^{-1}-A}{1+A}\right|.
 \tag{5}
\]
The difference of the squared numerator and denominator is
\[
 r^{-2}-1-2t\{r^{-1}\cos(2\pi(.3+x))+
                                      \cos(2\pi x)\}>0.
 \tag{6}
\]
For \(x\in[.25,.45]\), both cosines in braces are nonpositive.
For \(x\in[.22,.25]\), the first is less than \(-9/10\)
and the second less than \(1/5\), again giving a negative brace.
Consequently \(\Delta\) increases strictly in \(x\), and its
minimum occurs at \(x=11/50\).

Use the original argument
\(A_0(q,j)=\arg(1-e^{2\pi j-2\pi iq})\).
At this incoming real endpoint, the exact height derivative is
\[
 \partial_k\Delta=
 -A_0(.52,h+k)+A_0(.72,k)+\frac{2\pi}{5}>\frac\pi{15}.
 \tag{7}
\]
The first summand is nonnegative because its real argument exceeds
one half. Since \(\cos(1.44\pi)<0\), the real part of
\(1-e^{2\pi k-1.44\pi i}\) exceeds one, and its imaginary
modulus is smaller than \(e^{2\pi k}\). The bounds
\[
 e^{2\pi k}\le e^{.042\pi}<20/17<\sqrt3
 \tag{8}
\]
give \(A_0(.72,k)>-\pi/3\), which proves (7).
For (8), use \(.042\pi<3/20\) and
\(e^q<1/(1-q)\) on \(0<q<1\).
It follows that the minimum in the incoming height occurs at
\(k=-39/500\).

The elementary cosine bounds used in (6) require only
\(\pi<22/7\):
\(\cos(.1\pi)\ge1-(11/35)^2/2>9/10\) and
\(\cos(.44\pi)=\sin(.06\pi)<.06(22/7)<1/5\).

## 3. A controlled reduction of the outgoing real target

Write \(C(w)=\Re\cot\pi w\). The second outgoing derivative is
\[
 \partial_y^2\Delta=
 \pi\{C(s_h+b)-C(1/2+b)\}>0,
 \qquad y\in P.
 \tag{9}
\]
Indeed, the summed real part \(.3+y\) lies in \([.52,.75]\).
An imaginary displacement increases a negative real cotangent, so
\[
 C(s_h+b)\ge\cot\pi(.3+y),\qquad
 C(1/2+b)=-\frac{\sin(2\pi y)}{\cosh(.02\pi)+\cos(2\pi y)}.
 \tag{10}
\]
The difference of these two lower-comparison expressions is positive
precisely when
\[
 \cosh(.02\pi)<
 -\frac{\cos\pi(.3-y)}{\cos\pi(.3+y)}.
 \tag{11}
\]
The right side exceeds \((7/8)/(3/4)=7/6\): its numerator
is at least \(\cos(.15\pi)>7/8\), while the absolute denominator
is at most \(\sqrt2/2<3/4\). The left side is less than
\(11/10\). For explicit elementary witnesses, use
\(\cos(.15\pi)\ge1-(33/70)^2/2>7/8\), and
\(\cosh q\le\sum_{n\ge0}q^{2n}=1/(1-q^2)<11/10\)
at \(q=.02\pi<1/10\). This proves (9).

The first outgoing derivative has no chirp contribution:
\[
 \partial_y\Delta=
 \log\left|\frac{1-S e^{-2\pi ib}}{1+e^{-2\pi ib}}\right|.
 \tag{12}
\]
Put \(R=e^{2\pi H}\), so \(1<R<11/10\), and retain
\(r>1/2\). The latter follows from
\(.204\pi<2/3<\log2\); the former follows from
\(e^{.02\pi}<1/(1-.02\pi)<11/10\).
At \(y=.25\), numerator minus denominator in the squared ratio
of (12) exceeds
\[
 R\{(9/5)r-R(1-r^2)\}
 >R\left(\frac9{10}-\frac{33}{40}\right)>0.
 \tag{13}
\]
Here \(-\cos(1.1\pi)>9/10\) supplies the cross term.
Thus \(\partial_y\Delta(.25)>0\). Strict convexity in (9)
shows that the global minimum in \(y\) lies in \([.22,.25]\).

On that smaller interval, the numerator and denominator of the
squared ratio satisfy
\[
 |1-S e^{-2\pi ib}|^2>1+R^2/4+(9/10)R,
 \qquad |1+e^{-2\pi ib}|^2<1+R^2+(2/5)R.
 \tag{14}
\]
The difference of the first lower bound and four fifths of the
second upper bound is
\[
 \frac15-\frac{11}{20}R^2+\frac{29}{50}R
                       \ge\frac{69}{400}>0,
                \qquad 1\le R\le11/10.
 \tag{15}
\]
The polynomial decreases on this interval and has the stated value
at its right endpoint. Consequently
\(\partial_y\Delta>\tfrac12\log(4/5)>-1/8\), because
\(e^{1/4}>5/4\). Combining this slope bound with (9) and (13)
gives, for every \(y\in P\),
\[
 \Delta(.22,y,-.078,h)
          \ge\Delta(.22,.22,-.078,h)-\frac3{800}.
 \tag{16}
\]

## 4. Thirty-two whole-interval checks

Let
\[
 d(h)=\Delta(11/50,11/50,-39/500,h),
                   \qquad -51/500\le h\le-1/1000.
 \tag{17}
\]
The preceding reductions prove
\[
                   \Delta(x,y,k,h)\ge d(h)-3/800.
 \tag{18}
\]
The height derivative of the real half-row term is zero. The other
term has derivative
\[
 d'(h)=-A_0(.52,h-.078)-A_0(.52,h+.01)
                         +3A_0(.3,h)-\frac{11\pi}{25}.
 \tag{19}
\]
The first two terms are nonnegative and at most \(\pi/25\)
each. Since \(h<0\), \(0<A_0(.3,h)\le\pi/5\).
Thus \(-11\pi/25\le d'(h)\le6\pi/25\); in particular the
conservative inherited constant \(9\pi/10\) is a valid
Lipschitz bound on the whole interval.

Partition the height interval into 32 equal closed intervals \([l,r]\)
and let \(q=(l+r)/2\). A sufficient finite set of comparisons is
\[
 d(q)-\frac3{800}-\frac{9\pi}{10}\frac{r-l}{2}>\frac1{30}
                        \quad\text{on all 32 intervals}.
 \tag{20}
\]
The [new standalone checker](../experiments/check_mixed_second_selected_left_half_row_domination.py)
evaluates only these 32 expressions at fixed 160-bit precision. It
uses the original primitive
\[
 g(w)=\frac{\operatorname{Li}_2(e^{-2\pi iw})-\pi^2/6}{2\pi i},
 \tag{21}
\]
with the regular-strip and dilogarithm-cut checks used in the
[last-row comparison](research_mixed_selected_outgoing_four_last_row_domination.md).
All midpoint inputs and partition endpoints are exact rationals.
The original outgoing-independent terms \(-g(a)-g(b)\) cancel
algebraically in the difference; every remaining phase and chirp
is evaluated explicitly.

The record saves each exact directed rational bound, both corrections
in (20), the full partition, and dependency hashes checked before and
after evaluation. An arithmetic error or failed comparison does not
establish the sign. There is no adaptive subdivision, retry, source
root calculation, or finite quantum sum.

**Proposition 1 (certificate implication).** If all 32 comparisons
(20) pass, then (4) holds throughout (2).

Indeed (20) bounds every whole height interval using (19), and the
32 intervals cover (17). Equations (6)--(7) and (16) then prove
\(\Delta>1/30\) on the full domain, while the main profile
contains its fixed trial point. This proves the proposition.

At the second selection this would replace every term with left
profile \(R\) by the corresponding term with left profile \(0\),
for each right profile and each full Fourier alternative. The
comparison has no implication for the sign of that remaining main
term. It does not by itself settle the local finite-source envelope
or any whole-invariant asymptotic.
