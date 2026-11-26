# A sharper rational upper bound for the original complete three-action

Private written source deduction, 9 November 2026. The original
calibrated complete action satisfies
\[
                  \boxed{\quad M_3<\frac{1339}{705}<\frac{19}{10}.\quad}
\tag{1}
\]
This sharpens the earlier \(121/63\) upper bound without evaluating
the cubic root or the action. It preserves the complete finite-source
normalization and does not enlarge any kernel domain.
No mathematical numerical evaluation, saved-value arithmetic, script,
or frozen-source edit is used.

## 1. The original source and a stronger height floor

Retain the exact phase, primitive constant, and selected saddle from
[the earlier upper-bound proof, (2)--(3)](research_inner_three_complete_action_upper_bound.md):
\[
\begin{split}
\Phi(t,0)&=2\psi(t,0)+\frac{3it^2}{4\pi}-it,\\
\psi_t(t,0)&=-\pi^{-1}\operatorname{arsinh}\tan(t/2),
\qquad \psi(0,0)=2b_2,\\
M_3&=\Re\Phi(t_3,0),\qquad t_3=a_3-iH_3,\qquad
0<a_3<\pi/2,\quad0<H_3<1 .
\end{split}
\tag{2}
\]
The original cubic branch is
\[
v_3=2\cos(t_3/2)=x+ib,\qquad
v_3^3-2iv_3^2-3v_3+2i-2=0 .
\tag{3}
\]
The exact real-cut obstruction proof establishes
\[
                              b>\frac{29}{50}.
\tag{4}
\]
For clarity, this input is the written monotonicity argument in
[that source, (5)--(9)](research_mixed_next_first_quarter_real_cut_obstruction.md):
\[
p(b)=\frac{b^3-2b^2+3b-2}{3b-2},\qquad
Q(b)=p(b)-3b^2+4b-3,\qquad 2=\sqrt{p(b)}Q(b).
\]
Both \(p\) and \(Q\) increase on \(1/3<b<2/3\), while at
\(b_0=29/50\) its exact rational witnesses give
\[
0<Q(b_0)<7/6,\qquad p(b_0)<20/7,\qquad
\frac{p(b_0)Q(b_0)^2}{4}<\frac{35}{36}<1.
\]
If the actual \(b\le b_0\), the real cubic equation forces \(Q(b)>0\)
and contradicts the last inequality. Thus (4) concerns precisely
the root in (3), not a newly selected algebraic root.

We claim
\[
                              H_3>\frac79 .
\tag{5}
\]
Indeed
\[
b=2\sin(a_3/2)\sinh(H_3/2)<\sqrt2\,\sinh(H_3/2).
\]
For the positive series of \(\sinh z\), successive term ratios at
\(z=7/18\) are at most \(49/1944\), and strictly smaller after
the first. Hence
\[
\sinh(7/18)
 <\frac{7/18}{1-49/1944}=\frac{756}{1895}.
\]
Using \(\sqrt2<10/7\), if \(H_3\le7/9\) we would obtain
\[
b<\frac{10}{7}\frac{756}{1895}
 =\frac{216}{379}<\frac{29}{50},
\qquad 10800<10991,
\]
contradicting (4). This proves (5) by exact inequalities alone.

## 2. Retaining the stronger secant constant

The original branch satisfies
\[
                    \psi_{tt}(t,0)=-\frac{1}{2\pi\cos(t/2)}.
\tag{6}
\]
On \(0\le a\le\pi/2,\ 0\le H\le1\), the earlier proof already
establishes
\[
\cosh(1/2)<\frac{53}{47}.
\tag{7}
\]
It follows directly from the positive series bound
\[
\cosh(1/2)
 <1+\frac{1/8}{1-1/48}=\frac{53}{47}.
\]
Write \(c=\cos(a/2)\), \(s=\sinh(H/2)\), and \(C=\cosh(H/2)\).
Then
\[
\Re\sec((a-iH)/2)=\frac{cC}{c^2+s^2}.
\]
Here \(c^2\ge1/2\), while \(s^2<15/49<1/2\), as in the earlier
proof. Its derivative with respect to \(c\) has the sign of
\(s^2-c^2<0\). Its minimum over the allowed \(c\) is therefore
at \(c=1\), where it equals \(1/C\). Keeping (7), rather than
weakening it to \(C<8/7\), gives
\[
             \Re\sec((a-iH)/2)>\frac{47}{53}.
\tag{8}
\]

The imaginary-axis calculation in the same source is unchanged:
\[
2\Re\psi(-iH,0)\le4b_2+\frac{H^2}{2\pi},
\qquad \Re\psi_t(-iH,0)=0 .
\tag{9}
\]
It uses the original identity
\(\operatorname{arsinh}(-i\tanh(H/2))
 =-i\arctan(\sinh(H/2))\) and
\(\arctan(\sinh s)\le s\), preserving the additive constant.
Integrating (6),(8) twice horizontally, and then retaining the
literal crossing in (2), yields
\[
\begin{split}
\Re\Phi(a-iH,0)
&\le4b_2-H+\frac{H^2}{2\pi}
             -\frac{47a^2}{106\pi}+\frac{3aH}{2\pi}\\
&\le4b_2-H+\frac{665H^2}{376\pi}.
\end{split}
\tag{10}
\]
The second line maximizes the displayed quadratic over all real
\(a\); thus no constraint on the actual \(a_3\) is lost in the
upper bound. Explicitly its coefficient is
\[
\frac12+\frac{9}{8(47/53)}=\frac{665}{376}.
\]

## 3. The rational upper bound and its source scope

Use the established \(b_2<7/12\) and the elementary \(\pi>25/8\).
Equations (2),(5),(10) give
\[
M_3<
g(H_3),\qquad
g(H)=\frac73-H+\frac{133}{235}H^2,\qquad \frac79<H_3<1.
\tag{11}
\]
The quadratic is convex. Its endpoint values are
\[
g(7/9)=\frac{36127}{19035},\qquad
g(1)=\frac{1339}{705}=\frac{36153}{19035}.
\tag{12}
\]
Consequently \(M_3<1339/705\). Finally
\[
                  \frac{19}{10}-\frac{1339}{705}
                         =\frac{1}{1410}>0.
\tag{13}
\]
This proves (1).

As in the original source proof, \(M_3=\Re S_3(0,0)\) is the
action in the complete canonical packet
\[
Q_N^{\rm full}(-2\cos u)=P_{3,N}(0,u)
 =C_{N,3}N^{-3/2}A_3(0,u)e^{NS_3(0,u)}(1+O(N^{-1})).
\tag{14}
\]
The full single-vertex theorem supplies (14) near \(u=0\), with its
original modulus-one scalar, nonzero amplitude, both parities,
and all repeated-root normal data. No part of that source has
been deleted or rephased in (1). This deduction is an action
bound only, not a new finite contour estimate.

## 4. What this improves in the attachment budget

Keep the actual complete \(343\) reference of length at least five,
the original half-input action \(E_0(Z_*)=\mathcal E(1/2,Z_*)\),
and its original geometric rate \(\Lambda\). The exact half-input
identity and complete outgoing anchor give
\[
E_0(Z_*)\le\Lambda-\frac{17}{10}
\tag{15}
\]
as recorded in
[the combined-action deduction, (23)](research_mixed_next_positive_transition_combined_action_bound.md).
Thus the present improvement gives
\[
\mathfrak E_*:=M_3+E_0(Z_*)-\Lambda
                       <\frac{281}{1410}.
\tag{16}
\]
This is smaller than the earlier \(139/630\) ceiling, but it still
does not imply the sufficient comparison
\[
                         \mathfrak E_*<\frac{5\pi}{226}.
\tag{17}
\]
For example \(281/1410>1/10>3/40>5\pi/226\), where the final
inequality follows from \(\pi<22/7\).

There is a stronger precise limitation of tightening (1) alone.
The adopted original-action lower bound is \(M_3>46/25\).
Therefore any valid real upper bound \(B\ge M_3\) necessarily has
\[
B-\frac{17}{10}>
\frac7{50}>\frac3{40}>\frac{5\pi}{226}.
\tag{18}
\]
Accordingly an upper estimate obtained solely by adding a bound
on \(M_3\) to (15) cannot certify (17). An improved correlated
half-input comparison or another source estimate is required.
This does not lower-bound the actual excess \(\mathfrak E_*\)
and does not obstruct cancellation in the original observation.

## Frozen source bindings

| Source | SHA-256 |
|---|---|
| Original complete-action upper bound | 7ef8adaa33c1fed792379d4ead3aef70cb4e704816b6979fb1f156fe16b07a9d |
| Original cubic continuation | 8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a |
| Exact real-cut cubic inequality | d21bb5387258faadfdefd0f4bd2acfb5d002042c0e2e0de9c9e4448f0ef23c30 |
| Full single-vertex source | 7ac634d458e5805e95a7ce064d4e1fc513c96c0b758cfaee9f91fd46de10304c |
| Complete-action lower bound | dd5153c7eabefe865b6fd1ed03e6f2fb08c63283f20fd48a999b625ec4836c42 |
| Combined transition/action deduction | c4134027f8297321f91363bbf252f55d755596c45ac41c63492212a0c0c23974 |

The frozen inputs remain unchanged.
