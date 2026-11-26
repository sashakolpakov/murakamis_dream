# Dominating a four-type last row when its outgoing argument is selected

Research deduction, 6 November 2026.

This note reduces a pointwise comparison between a bare ordinary kernel's
last-row rate and its main-contour rate to 128 scalar interval checks.
The incoming argument keeps its original height, while the outgoing
argument has height \(1/100\). The comparison requires no relation
between the two real targets and no moving critical point.

The analytic reduction is proved below. The scalar sign in Section 3
is a separate certificate requirement until a complete result is saved.

## 1. The trial point and the two rates

For the own-type-four phase write
\[
 Q(s;a,b)=g(s+a)+g(s+b)-3g(s)-g(a)-g(b)+2\pi ias,
 \qquad g'(w)=\log(1-e^{-2\pi iw}).
 \tag{1}
\]
The primitive and logarithm are those of
[the original second-selection reduction](research_mixed_second_selected_plateau_reduction.md).
Consider the whole containing domain
\[
 \begin{split}
 a&=x+ik,\qquad b=y+iH,\qquad x,y\in P=[11/50,9/20],\\
 -27/250&\le k\le17/250,\qquad H=1/100,\\
 s_h&=3/10+ih,\qquad -51/500\le h\le-1/1000.
 \end{split}
 \tag{2}
\]
The main contour includes this trial at its original fixed index height.
The full periodic last-row rate is
\[
                  R_1=2\pi(-k)_++2\pi H.
 \tag{3}
\]
Define its deficit below the trial by
\[
             D(x,y,k,h)=\Re Q(s_h;x+ik,y+iH)-R_1 .
 \tag{4}
\]
A uniform inequality \(D>1/50\) would imply
\[
 R_1<\max_{1/8\le t\le1/2}\Re Q(t+ih;a,b)-1/50
          =R_0-1/50 .
 \tag{5}
\]
Both quantities are bare profiles, so any common Fourier weights
and affine subtractions preserve this comparison.

## 2. Reducing the incoming height and both real targets

Use the regular-strip argument
\(A(t,k)=\arg(1-e^{2\pi k-2\pi it})\).
Its bounds (8)--(9) in
[the outgoing last-row transport proof](research_mixed_second_selected_outgoing_last_rows.md)
apply at all heights in (2). Differentiating the incoming argument
of (1), including the original chirp, gives
\[
 \partial_k\Re Q=A(x,k)-A(3/10+x,h+k)-3\pi/5 .
 \tag{6}
\]
Here \(x<1/2\) and \(1/2<3/10+x<1\). Thus
\[
                    -3\pi/5\le\partial_k\Re Q\le0.
 \tag{7}
\]
For the upper bound, the two argument bounds sum to
\(\pi(1-2x)+\pi(2(3/10+x)-1)=3\pi/5\).
For the lower bound, the first argument is nonnegative and the
second nonpositive.

On the negative part of the height range,
\(\partial_kD\ge7\pi/5\), so \(D\) increases with \(k\).
On the positive part, \(\partial_kD\ge-3\pi/5\). Consequently,
for \(k\ge0\),
\[
 \begin{split}
 D(x,y,k,h)-D(x,y,-27/250,h)
 &\ge\frac{7\pi}{5}\frac{27}{250}
                         -\frac{3\pi}{5}\frac{17}{250}\\
 &=\frac{69\pi}{625}>0.
 \end{split}
 \tag{8}
\]
Every height in (2) is therefore bounded below by the single negative
endpoint \(k=-27/250\).

For fixed heights and \(s_h\), (4) is separately strictly concave
in \(x,y\). Indeed
\[
 \partial_x^2\Re Q
 =\pi\Re\{\cot\pi(s_h+a)-\cot\pi a\}<0,
 \tag{9}
\]
because \(\Re(s_h+a)\in[.52,.75]\) and \(x\in(0,.5)\).
The same argument applies to \(y\). The chirp is affine in \(x\),
and (3) has no real-target dependence. Taking the minimum successively
in \(x\) and \(y\) now yields
\[
 D(x,y,k,h)\ge
 \min_{\xi,\eta\in\{11/50,9/20\}}
                         d_{\xi,\eta}(h),
 \qquad
 d_{\xi,\eta}(h)=D(\xi,\eta,-27/250,h).
 \tag{10}
\]
Only four functions on one real interval remain.

Their derivatives have the useful uniform bound
\[
       -9\pi/10\le d_{\xi,\eta}'(h)\le7\pi/10 .
 \tag{11}
\]
To see this, direct differentiation gives
\[
 d'=-A(3/10+\xi,h-27/250)
       -A(3/10+\eta,h+H)+3A(3/10,h)-2\pi\xi.
 \tag{12}
\]
The first two summands and \(A(3/10,h)\) are nonnegative.
This proves the lower bound \(-2\pi\xi\ge-9\pi/10\).
Since \(h<0\), the bound
\(A(3/10,h)\le\pi/5\), together with the general argument
bounds for the other two summands, gives
\[
 d'\le\pi(2\xi-2/5)+\pi(2\eta-2/5)
                      +3\pi/5-2\pi\xi
         =\pi(2\eta-1/5)\le7\pi/10.
 \tag{13}
\]
Thus \(9\pi/10\) is a Lipschitz constant for all four functions.

## 3. The finite scalar certificate

Partition \([-51/500,-1/1000]\) into 32 equal closed intervals.
For each interval \([l,r]\), let \(q=(l+r)/2\). Equation (11)
gives the whole-interval lower bound
\[
 d_{\xi,\eta}(h)\ge
       d_{\xi,\eta}(q)-\frac{9\pi}{10}\frac{r-l}{2},
                     \qquad l\le h\le r.
 \tag{14}
\]
The [standalone checker](../experiments/check_mixed_selected_outgoing_four_last_row_domination.py)
evaluates the right side with outward ball arithmetic at 160 bits.
It uses the explicit original primitive
\[
 g(w)=\frac{\operatorname{Li}_2(e^{-2\pi iw})-\pi^2/6}{2\pi i}.
 \tag{15}
\]
Every argument has real part strictly between zero and one. At the
fixed midpoint inputs the dilogarithm arguments also avoid its cut.
The checker verifies these facts and checks that each exact rational
lower endpoint from (14) exceeds \(1/50\). It saves all 128 intervals
and endpoints, the precision, the dependency hashes, and the result.
No source root, finite quantum sum, earlier certificate or adaptive
parameter cover is evaluated.

**Proposition 1 (certificate implication).** If all 128 checks pass,
(5) holds on all of (2).

*Proof.* The 32 closed intervals cover the whole index-height range.
Equation (14) supplies a lower bound on each entire interval,
not only at its midpoint. The four corner tests and (10) cover
every real target and incoming height in (2).
The main profile includes the trial \(s_h\), proving (5).
\(\square\)

## 4. Consequence for the second-position comparison

Assuming the certificate requirement in Proposition 1 is discharged,
every term in the second-selection envelope with left profile 1
is strictly below the corresponding term with left profile 0.
This holds for each of the four right profiles and for both
Fourier alternatives, because all other terms are unchanged.

At \(H=1/100\), the
[outgoing last-row theorem](research_mixed_second_selected_outgoing_last_rows.md)
already controls the six terms with right profile 1 and left profile
\(0,L,R\). Combining the two comparisons would leave precisely
the eighteen terms with both profiles in \(\{0,L,R\}\) and either
Fourier alternative. Their signs remain separate. No conclusion
about the whole invariant follows from these last-row comparisons alone.
