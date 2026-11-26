# Extending the ordinary profile comparisons in the incoming height

Research deduction, 6 November 2026. This extends three completed
pointwise ordinary-profile comparisons using their saved interval bounds
and elementary height derivatives. It evaluates no new primitive, source,
root or target. In particular, the main-index barrier alone is not used
to remove a real-cut or last-row profile.

## 1. Source and saved starting bounds

Write the incoming target as \(b=x+ik\), the selected outgoing target as
\(a=y+iH\), and retain the literal own-four phase
\[
 Q(s;b,a)=g(s+b)+g(s+a)-3g(s)-g(b)-g(a)+2\pi ibs,
 \quad g'(w)=\Log(1-e^{-2\pi iw}),\quad H=1/100.
 \tag{1}
\]
Throughout, \(x,y\in P=[.22,.45]\), \(h\in[-.102,-.001]\), and
\(s_h=.3+ih\). Let \(R_0\) be the maximum of \(\Re Q\) on
\([.125,.5]+ih\), and put
\[
 R_L=\Re Q(1/8;b,a),\quad R_R=\Re Q(1/2;b,a),\quad
 R_1=2\pi(-k)_++2\pi H.
 \tag{2}
\]
The last quantity is the maximum of the four original affine periodic
last-row carriers. The main profile includes \(s_h\).

The following slightly stronger rational summaries of the completed
records are useful. Each is below **every** saved whole-height lower
endpoint in the indicated record; these comparisons use exact fractions.

| Trial comparison | Saved incoming height | Uniform lower bound | Record |
|---|---:|---:|---|
| \(\Re Q(s_h)-R_1\), at the four real corners | \(-.108\) | \(49/2000\) | [128 last-row checks](../repro/results/research-mixed-selected-outgoing-four-last-row-domination.json) |
| \(\Re Q(s_h)-R_L\), at the four real corners | \(.021\) | \(163/10000\) | [128 left-cut checks](../repro/results/research-mixed-second-selected-left-cut-domination.json) |
| \(\Re Q(s_h)-R_R\), after the original outgoing-target reduction | \(-.078\) | \(23/625\) | [32 half-row checks](../repro/results/research-mixed-second-selected-left-half-row-domination.json) |

All inequalities in this table are strict. The respective record hashes
are `23f975f20c70e2f22a197c705d7225c37a30f175c13e92e59353410543d64eeb`,
`1404479b59692fb21ab22663c42bc1841a819a73af9ad8d15d23c6a46efecaf7`,
and `2950716a5606c9eba7155a3cb7b97588916782d09b0b4f2c913edebe1a429701`.
Their original analytic reductions and interval corrections are retained.

Set
\[
 A(t,q)=\Im g'(t+iq)=\Arg(1-e^{2\pi q-2\pi it}).
 \tag{3}
\]
On the original strip its sign is that of \(1/2-t\), and
\(\pi\min(1-2t,0)\le A(t,q)\le\pi\max(1-2t,0)\).
Every real/imaginary component used below is a component of the number
inside this logarithm.

## 2. The half row extends to the entire height rectangle

**Proposition 1.** For all \(k\in[-.116,.08]\),
\[
                         R_R<R_0-1/500.
 \tag{4}
\]

Put \(\Delta_R=\Re\{Q(s_h)-Q(1/2)\}\). The incoming-real
monotonicity calculation (5)--(6) of the
[half-row proof](research_mixed_second_selected_left_half_row_domination.md)
uses only \(h<0\), not a bound on \(k\). Thus its minimum is at \(x=.22\).
At that endpoint the exact chirped derivative is
\[
 (\Delta_R)_k=-A(.52,h+k)+A(.72,k)+2\pi/5.
 \tag{5}
\]
It is positive throughout the enlarged rectangle. Indeed the first
term is nonnegative, while \(A(.72,k)>-\pi/3\): the real part of
the logarithm's argument exceeds one and its imaginary modulus is
less than \(e^{.16\pi}<5/3<\sqrt3\). The exponential bound is the
explicit positive-series estimate in the
[full-input index barrier](research_mixed_terminal_full_input_index_barrier.md).
It therefore suffices to extend the old comparison downward from
\(k_0=-.078\) to \(-.116\).

On that connecting interval,
\[
          -A(.52,h+k)<1/20,\qquad A(.72,k)<-2/5.
 \tag{6}
\]
For the first inequality, \(h+k\le-.079\) gives
\(r=e^{2\pi(h+k)}<5/8\). Also
\(\sin(.04\pi)<63/500\) and \(\cos(.04\pi)>99/100\), so
\[
 -A(.52,h+k)
 <\frac{(5/8)(63/500)}{1+(5/8)(99/100)}<1/20.
 \tag{7}
\]
For the second, \(r=e^{2\pi k}>19/40\),
\(\sin(.44\pi)>49/50\), and \(\cos(.44\pi)<1/5\). Consequently
\[
 -\tan A(.72,k)>
 \frac{(19/40)(49/50)}{1+(19/40)(1/5)}
 =\frac{931}{2190}>\frac{17}{40}>\tan(2/5).
 \tag{8}
\]
The arguments here lie in \((-\pi/2,0)\), so (8) proves (6).
Using \(\pi<22/7\), equations (5)--(6) give
\[
       (\Delta_R)_k<2\pi/5-7/20<127/140.
 \tag{9}
\]
This derivative is independent of the outgoing real target \(y\).
The original outgoing reduction therefore remains unchanged. The old
uniform bound and integration over a length at most \(19/500\) give
\[
 \Delta_R>\frac{23}{625}-\frac{19}{500}\frac{127}{140}
          =\frac{163}{70000}>\frac1{500}.
 \tag{10}
\]

For explicit rational witnesses in (6)--(8), use
\(2\pi(.079)>.474=237/500\), whose exponential series through degree
three exceeds \(8/5\) by \(1021851/250000000\). Also
\[
 e^{.232\pi}<e^{.73}
 \le1+\frac{73}{100}+
 \frac{(73/100)^2}{2(1-73/300)}<40/19;
 \tag{11}
\]
the last gap is \(19949/862600\). The sine/cosine claims follow from
their first alternating bounds and \(3<\pi<22/7\); specifically,
\(\sin(.44\pi)=\cos(.06\pi)>
1-(.06\cdot22/7)^2/2>49/50\). Finally
\((17/40)(1-(2/5)^2/2)-[(2/5)-(2/5)^3/6+(2/5)^5/120]
=593/375000>0\), proving the tangent bound. This completes the proof.

## 3. A wider left-cut comparison, including the whole type-four height range

**Proposition 2.** For all \(k\in[-.116,.03]\),
\[
                         R_L<R_0-1/500.
 \tag{12}
\]

For \(\Delta_L=\Re\{Q(s_h)-Q(1/8)\}\), separate concavity in
\(x,y\) still reduces its minimum to the four real corners, although
the general corner lemma's old height bound cannot simply be reused.
Here is a direct check at the fixed trial \(.3\).
Write \(C(t,q)=\Re\cot\pi(t+iq)\). If \(.125+x\le.5\), then
\(C(.3+x,h+k)<0\le C(.125+x,k)\). Otherwise \(x\in[.375,.45]\),
and \(u=2\pi(.3+x-.5)\in[.35\pi,.5\pi]\). Since
\(|h+k|\le.218\),
\[
 C(.3+x,h+k)<-\frac{4/5}{11/5+1/2}=-\frac8{27}
 <-\frac14<C(.125+x,k).
 \tag{13}
\]
Indeed \(\sin u>4/5\), \(\cos u<1/2\),
\(\cosh(.436\pi)<11/5\), and
\(C(.125+x,k)\ge-\tan(.075\pi)>-1/4\).
For the cosh bound, \(.436\pi<11/8\) and
\(\cosh q\le1+q^2/2+(q^4/24)/(1-q^2/30)\) at \(q=11/8\);
the gap below \(11/5\) is \(220449/2302720\).
The remaining witnesses are
\(\sin(21/20)\ge21/20-(21/20)^3/6>4/5\) and
\((1/4)(1-(33/140)^2/2)-33/140=1151/156800>0\).
The same comparison handles \(y\), with its smaller fixed height \(H\).

At either incoming real corner, the exact derivative is
\[
 (\Delta_L)_k=-A(.3+x,h+k)+A(.125+x,k)-7\pi/20.
 \tag{14}
\]
At \(x=.22\), the argument bounds give \((\Delta_L)_k\le0\).
At \(x=.45\), the second argument is negative and
\(-A(.75,h+k)=\arctan e^{2\pi(h+k)}<\pi/3\), because
\(h+k\le.079\) even on the larger rectangle \(k\le.08\).
Thus this corner derivative is also negative. Extending the lower
height below \(-.078\) costs nothing. For the extra interval
\(.021\le k\le.03\), equation (14) also gives the lower bound
\((\Delta_L)_k\ge-\pi/2\): at \(x=.22\) both argument contributions
are nonnegative, and at \(x=.45\) the second is at least \(-.15\pi\).
The corner bounds in Section 1 now imply
\[
 \Delta_L>\frac{163}{10000}-.009\frac\pi2
 >\frac{151}{70000}>\frac1{500}.
 \tag{15}
\]

## 4. A wider last-row comparison, including the whole type-three height range

**Proposition 3.** For all \(k\in[-223/2000,.08]\),
\[
                         R_1<R_0-1/400.
 \tag{16}
\]

Set \(D=\Re Q(s_h)-R_1\). The
[original last-row proof](research_mixed_selected_outgoing_four_last_row_domination.md)
gives, without a restricted height range,
\[-3\pi/5\le\partial_k\Re Q(s_h)\le0.\]
For \(k<0\), therefore, \(7\pi/5\le D_k\le2\pi\).
Lowering the old endpoint \(-.108\) to \(-.1115=-223/2000\)
loses at most \(2\pi(7/2000)<22/1000\). Separate concavity in the
real targets is unchanged, since the relevant summed real parts are
in \([.52,.75]\). Hence
\[
 D>49/2000-22/1000=1/400.
 \tag{17}
\]
For positive heights up to \(.08\), the earlier gain from \(-.108\)
to zero exceeds every possible loss afterward:
\((7\pi/5)(.108)-(3\pi/5)(.08)=129\pi/1250>0\).
Thus (17) also covers that entire range.

## 5. Exact source consequence and the two remaining height strips

For incoming height \(k\in[-.1115,.03]\), all six nonmain ordinary
labels are dominated by the same main ordinary profile, with strict
gap at least \(1/500\). This extends Proposition 3 of the
[joint-main theorem](research_mixed_terminal_joint_main_budget.md).
The original chirp has been retained in each derivative. All terminal
profiles, alias penalties, incoming halfweights, affine tangents, and
both alternatives of the **complete** selected weight are independent
of the ordinary index, and are unchanged by these replacements.
One total positive tolerance gives the corresponding original finite
profile bound. No terminal-profile sign follows from this reduction.

The canonical input disks are
\(D_3=\{|b_*-(.35-.01i)|\le.09\}\) and
\(D_4=\{|b_*-(.30-.052i)|\le.064\}\). Proposition 1 covers
both entire height ranges; Proposition 2 covers all of \(D_4\), and
Proposition 3 covers all of \(D_3\). The only ordinary labels still
requiring a different argument on the full input disks are therefore:

* the real left cut when \(b_*\in D_3\) and \(\Im b_*>.03\);
* the periodic last row when \(b_*\in D_4\) and
  \(\Im b_*<-223/2000\), retaining its four affine carriers when
  a concave-profile calculation needs them separately.

These are unresolved comparisons, not proved adverse signs. In
particular, disk correlation of \(\Re b_*\) with \(\Im b_*\)
cannot narrow the independent real **target** \(x\in P\).
The main-index barrier on the full disks does not remove these
nonmain source profiles. No reference existence, whole-word theorem,
or knot-family volume statement is added here.

For actual word inputs, the smaller
[typed envelopes](research_mixed_typed_last_row_envelopes.md), equations
(1)--(3), give a stronger immediate conclusion:
\[
 \begin{split}
 K_3={}&\{|b_*-(.35-.01i)|\le.083\}
   \cap\{-.072\le\Im b_*\le.068,\ 
                \Re b_*-3\Im b_*\le.608\},\\
 K_4={}&\{|b_*-(.30-.052i)|\le.060\}
   \cap\{-.108\le\Im b_*\le-.001\}.
 \end{split}
 \tag{18}
\]
All ordinary and attached type-four inputs lie in \(K_4\), so all
ordinary labels reduce to the main label on that entire actual domain.
On \(K_3\), only the real left cut for \(\Im b_*>.03\) remains.
The attached type-three rectangle has upper height \(.021\) and is
therefore already covered. Thus the unresolved actual-input strip
can contain only ordinary type-three external legs. The reduced disk
and the oblique clipping inequality in (18) do not remove that strip;
for example \(.35+.05i\) satisfies every defining inequality.
This example is a point of the containing domain, not a claimed
finite-word reference or an adverse profile comparison.
