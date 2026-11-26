# The outgoing four-type half row at the second selection

Research deduction and fixed scalar-certificate criterion, 6 November
2026. The analytic reductions below reduce a pointwise main-versus-half-row
comparison to 32 whole-height checks. The scalar signs are not presumed.
The argument is for an ordinary own-four block with selected incoming
height; it does not assert the corresponding own-three comparison.

## 1. Original difference and incoming real coordinate

Retain the original bare phase
\[
 Q(s;a,b)=g(s+a)+g(s+b)-3g(s)-g(a)-g(b)+2\pi ias,
 \qquad g'(w)=\Log(1-e^{-2\pi iw}).
 \tag{1}
\]
Consider the full containing domain
\[
 \begin{gathered}
 a=x+iH,\quad b=y+ik,\quad H=1/100,\quad
 x,y\in P=[11/50,9/20],\\
 s_h=3/10+ih,\qquad h,k\in[-51/500,-1/1000].
 \end{gathered}
 \tag{2}
\]
Let
\[
                  \Delta(x,y,k,h)=\Re\{Q(s_h;a,b)-Q(1/2;a,b)\}.
 \tag{3}
\]
Both outer terms \(-g(a)-g(b)\) cancel; the original asymmetric
chirp remains. The main profile contains the trial \(s_h\), so a
lower bound for \(\Delta\) is a lower bound for \(R_0-R_R\).

Put \(S=e^{-2\pi is_h}\), \(A=e^{-2\pi ia}\),
\(r_s=|S|<1\), \(t=|A|>0\). Direct differentiation gives
\[
 \Delta_x=\log\left|\frac{S^{-1}-A}{1+A}\right|,\qquad
 |S^{-1}-A|^2-|1+A|^2
 =r_s^{-2}-1-2t\{r_s^{-1}\cos2\pi(.3+x)+\cos2\pi x\}>0.
 \tag{4}
\]
For \(x\in[.25,.45]\) both cosines in braces are nonpositive.
For \(x\in[.22,.25]\) the first is less than \(-9/10\),
the second less than \(1/5\). These elementary inequalities and
the chirp in (4) are exactly those in Section 2 of the
[left-factor half-row proof](research_mixed_second_selected_left_half_row_domination.md);
they require no sign restriction on the incoming height.
Thus the minimum in \(x\) occurs at \(x=11/50\).

## 2. Controlling the outgoing real target uniformly in its height

Write \(C(w)=\Re\cot\pi w\). As in the same half-row calculation,
\[
 \Delta_{yy}=\pi\{C(s_h+b)-C(1/2+b)\}.
 \tag{5}
\]
The first summed real part lies in \([.52,.75]\), where the real
cotangent is nonpositive. An imaginary displacement increases its value.
Consequently
\[
 C(s_h+b)\ge\cot\pi(.3+y),\qquad
 C(1/2+b)=-\frac{\sin2\pi y}{\cosh2\pi k+\cos2\pi y}.
 \tag{6}
\]
The difference of these comparison expressions is positive precisely
when
\[
 \cosh2\pi k<
 -\frac{\cos\pi(.3-y)}{\cos\pi(.3+y)}.
 \tag{7}
\]
Throughout \(P\), the ratio on the right exceeds
\[
           \frac{7/8}{5/7}=\frac{49}{40}.
 \tag{8}
\]
Indeed \(\cos(.15\pi)>7/8\), by
\(\cos q\ge1-q^2/2\) and \(.15\pi<33/70\), and
\(|\cos\pi(.3+y)|\le\sqrt2/2<5/7\).
The proved bound \(\cosh(.204\pi)<49/40\) is equation (9) of the
[four-type corner comparison](research_mixed_selected_four_left_row_corners.md).
Since \(|k|\le.102\), (7) follows. Thus \(\Delta\) is strictly
convex in \(y\) on the entire target interval.

Its first outgoing derivative has no chirp term:
\[
            \Delta_y=\log\left|
               \frac{1-S e^{-2\pi ib}}{1+e^{-2\pi ib}}\right|.
 \tag{9}
\]
Put \(r_b=e^{2\pi k}\), so \(0<r_b<1\), while \(r_s>1/2\).
The latter follows from \(.204\pi<2/3<\log2\), as proved in the
[outgoing left-cut deduction](research_mixed_second_selected_outgoing_four_left_cut.md).
At \(y=.25\), numerator minus denominator of the squared ratio
in (9) exceeds
\[
 r_b\{(9/5)r_s-r_b(1-r_s^2)\}
           >r_b(9/10-3/4)>0.
 \tag{10}
\]
Here \(-\cos(1.1\pi)>9/10\). Strict convexity and
\(\Delta_y(.25)>0\) show that the minimum in \(y\) lies in
\([.22,.25]\).

On this smaller interval the squared numerator and denominator obey
\[
 |1-S e^{-2\pi ib}|^2>1+r_b^2/4+(9/10)r_b,\qquad
 |1+e^{-2\pi ib}|^2<1+r_b^2+(2/5)r_b.
 \tag{11}
\]
The first lower bound minus four fifths of the second upper bound is
\[
              \frac15-\frac{11}{20}r_b^2+\frac{29}{50}r_b
                           \ge\frac15>0
                  \qquad(0\le r_b\le1).
 \tag{12}
\]
This concave polynomial has its minimum at an endpoint; the values
are \(1/5\) and \(23/100\). Therefore
\(\Delta_y>\tfrac12\log(4/5)>-1/8\), using \(e^{1/4}>5/4\).
For every \(y\in P\) it follows that
\[
 \Delta(.22,y,k,h)\ge\Delta(.22,.22,k,h)-3/800.
 \tag{13}
\]

## 3. The outgoing height has a definite direction after this reduction

At the remaining outgoing real target \(y=.22\), let
\(A_0(t,q)=\arg(1-e^{2\pi q-2\pi it})\).
The outgoing height does not enter the chirp. Hence exactly
\[
 \begin{split}
 \Delta_k(.22,.22,k,h)
 &=-A_0(.52,h+k)+A_0(.72,k)\\
 &=\arctan\frac{r_s r_b\sin(.04\pi)}
                       {1+r_s r_b\cos(.04\pi)}
   -\arctan\frac{r_b\sin(.44\pi)}
                       {1+r_b\cos(.44\pi)}<0.
 \end{split}
 \tag{14}
\]
To prove the strict sign, the first fraction increases with \(r_s\),
so it is less than its value at \(r_s=1\). Then
\(0<.04\pi<.44\pi<\pi/2\) makes its numerator smaller and
denominator larger than those of the second fraction.
Thus the minimum occurs at the largest outgoing height \(k=-1/1000\).

Define the single remaining function
\[
 d(h)=\Delta(11/50,11/50,-1/1000,h).
 \tag{15}
\]
The preceding reductions prove the full-domain bound
\[
                         \Delta(x,y,k,h)\ge d(h)-3/800.
 \tag{16}
\]
This is a lower bound for a literal difference, not for its absolute
value and not for a maximum chosen independently of the other variables.

## 4. Thirty-two whole-height checks

Differentiating (15), the real half row is independent of \(h\):
\[
 d'(h)=-A_0(.52,h+.01)-A_0(.52,h-.001)
                           +3A_0(.3,h)-11\pi/25.
 \tag{17}
\]
The first two terms lie in \([0,\pi/25]\), and
\(0<A_0(.3,h)\le\pi/5\) because \(h<0\). Thus
\[
                   -11\pi/25\le d'(h)\le6\pi/25.
 \tag{18}
\]
In particular \(9\pi/10\) is a valid conservative Lipschitz constant.

Divide \([-51/500,-1/1000]\) into 32 equal closed intervals
\([l_j,r_j]\), with midpoint \(q_j\). The sufficient scalar tests are
\[
       d(q_j)-\frac3{800}-\frac{9\pi}{10}\frac{r_j-l_j}{2}>
                           \frac1{20},\qquad 0\le j<32.
 \tag{19}
\]
The [standalone checker](../experiments/check_mixed_second_selected_outgoing_four_half_row.py)
uses the original regular-strip primitive
\[
                g(w)=\frac{\operatorname{Li}_2(e^{-2\pi iw})-\pi^2/6}
                                          {2\pi i}
 \tag{20}
\]
at 160 bits, with explicit strip, cut and finiteness guards. It evaluates
the exact canceled difference in (3), including \(2\pi ia(s_h-1/2)\).
The midpoint inputs are exact rationals. The record retains every
whole-interval directed endpoint, both corrections, the partition
and before/after dependency hashes. It refuses an existing output.
No adaptive cover, root solve, earlier certificate replay or finite
quantum sum is evaluated.

**Proposition 1 (certificate implication).** If all 32 tests (19) pass,
then throughout the full domain (2)
\[
              \Re Q(1/2;a,b)<
                 \max_{1/8\le t\le1/2}\Re Q(t+ih;a,b)-1/20.
 \tag{21}
\]
The whole-interval consequence of (18)--(19), followed by (16), gives
\(\Delta>1/20\); the trial \(s_h\) belongs to the main line.
Every common Fourier allocation and affine tangent may be added
unchanged to (21).

## 5. Exact source scope

For a second-position selection with \(m\ge4\) and first three flags
\((\alpha,1,1)\), the right ordinary factor has exactly the heights
in (2): its incoming height is \(H_2=.01\), and its ordinary index
and outgoing coordinate have own-four heights in \((-.102,-.001)\).
This includes \(m=4\), when the next external leg is attached.
Its outgoing modulus halfweight is common to both sides of (21).

Consequently a completed (19) would remove the right half-row profile
pointwise from each Fourier alternative of the
[second-selection finite reduction](research_mixed_second_selected_plateau_reduction.md).
Together with the completed left-profile and right-left-cut dominations,
only the two main/main alternatives would remain when position 1 is
unselected; the separately paid right last row keeps its original
joint \(1/400\) loss. This does not assert either central sign.

The pointwise comparison (21) also survives multiplication by any
cap contribution when position 1 is selected. The right last row is
still not paid in that situation by an unselected supporting plane.
No own-three half-row domination or whole-chain estimate is inferred.
