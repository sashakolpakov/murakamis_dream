# The long upper right side of the original cap contour

Research deduction, 8 November 2026. The weighted right side can be
extended from the old height \(1/25\) to the new upper alias height
one. This uses the exact endpoint polynomial and its complete
physical coefficient norm on the unit disk. It does not assume an
endpoint saddle packet at large positive private height.

The real cut can be chosen as in the already proved upper-end
current theorem, after reducing its fixed wall distance if needed.
The new segment is a complete weighted current; the left side,
lower long side and outer main path remain separate.
No numerical evaluation is used.

## 1. The exact endpoint-polynomial representation

Retain the original \(H_N,C_N,G_N,D_N,\Pi_N\), as specified in
[the upper-end current theorem](research_mixed_cap_upper_end_currents.md).
The exact identity in Section 6, equation (18), of
[the complex-index coefficient source](research_complete_boundary_complex_index.md)
is
\[
H_N(w,e^{2\pi ie})=G_N(Ne)C_N(e,w).
                                                               \tag{1}
\]
It is an identity of the specified finite functions. It retains
all terms that revive at nonphysical private indices.
The carrier cancellation from
[the tall upper alias](research_mixed_cap_tall_upper_alias.md)
therefore gives
\[
\mathscr A_N(e,a,w)=
H_N(w,e^{2\pi ie})e^{-i\pi Nae}
 \frac{G_N(N(a+e))}{G_N(Na)G_N(Ne)}.
                                                               \tag{2}
\]
The identity is used only at positive imaginary height below,
where all displayed factorials are nonzero.

Put \(b_0=101/125\). The existing full physical endpoint bounds
give, for every \(\tau>0\),
\[
\sum_{j=0}^{N-1}|H_N(w,r^{-j})|
 \le C_\tau N^{B_\tau}e^{N(b_0+\tau)},
 \qquad -2\le w\le2.
                                                               \tag{3}
\]
Here is the full source scope of this consequence. On compact
physical index intervals the all-real-color bound has rate
\(h(e)=\lambda(e)+J(e)\le b_0\), as in Section 2 of
[complementary real colors](research_mixed_three_four_complementary_real_colors.md).
At the low true end, the terminating physical formula and
\[
\frac{S_j}{S_lS_{j-l}}\le\binom jl
\]
give \(|H_N(w,r^{-j})|\le2^j\max_{l\le j}|e_l(w)|\).
The binomial inequality follows from the decrease of
\(\sin x/x\) on \((0,\pi)\). The all-real Newton envelope
tends uniformly to zero as \(l/N\to0\).
At the upper true end \(j=N-1-m\), the exact endpoint bound
in equations (4)--(6) of the same real-color source is
\[
|H_N(w,r^{-j})|
\le\frac{2^m}{S_m}\sum_{l=0}^{j}|e_l(w)|,
\qquad
\sum_l|e_l(w)|\le\operatorname{poly}(N)e^{Nb_2},
\quad b_2<73/125.
\]
Both end rates are below \(b_0\) after choosing one sufficiently
small fixed endpoint width. This proves (3) without extending
a compact-index asymptotic to zero or one.

The degree of \(H_N(w,Y)\) in \(Y\) is at most \(N-1\).
Its exact root-grid cardinal polynomials have modulus at most
one on \(|Y|\le1\), since each is \(N^{-1}\) times a sum of
\(N\) powers of modulus at most one. Thus (3) gives
\[
\sup_{\substack{|Y|\le1\\-2\le w\le2}}|H_N(w,Y)|
\le C_\tau N^{B_\tau}e^{N(b_0+\tau)}.
                                                               \tag{4}
\]
This is cardinal interpolation of this very polynomial in its
own variable \(Y\).

## 2. The weighted source envelope and its height monotonicity

Write \(a=1-v\), \(3/10\le v\le1/2\), and \(e=E+iH\).
For \(1/25\le H\le1\), (2), (4), and the original uniform
upper-half-plane factorial theorem give the weighted upper rate
\[
\mathcal L(E,a,H)=
b_0+\Re J_+(a+E+iH)-\Re J_+(E+iH)-J(a)
                 +\pi aH-2\pi H.
                                                               \tag{5}
\]
The last term is the exact upper cotangent-remainder penalty.
The term \(+\pi aH\) is the retained carrier from (2).
All arguments are in fixed regular compacts. In particular
the use of \(J_+\) at real part one is justified by the original
canonical half-plane factorial theorem, not by finite entireness.

For \(0<E<1/2\) and \(1/2<a+E<1\), the original sine arguments
have opposite signs and lie in \((-\pi/2,\pi/2)\).
Consequently
\[
\partial_H\mathcal L
=\Arg\sin\pi(E+iH)-\Arg\sin\pi(a+E+iH)+\pi a-2\pi
<-\pi(1-a)\le-\frac{3\pi}{10}.
                                                               \tag{6}
\]
The whole side above \(H=1/25\) therefore reduces to its
lowest point. The limit \(a+E=1\), used as a comparison in
the next section, is also regular because \(H\ge1/25>0\).

We will use a slightly stronger real action floor. The source
bound \(\lambda(3/10)>17/20\) is already proved in
[wrapped-row transport, equation (15)](research_mixed_cap_wrapped_row_transport.md).
Strict concavity of \(\log(2\sin\pi s)\) and the midpoint
integral comparison give
\[
-J(3/10)
<\frac15\log(2\sin(2\pi/5))<\frac{2}{15}.
                                                               \tag{7}
\]
For an elementary witness to the last inequality,
\[
(2\sin(2\pi/5))^2=(5+\sqrt5)/2<29/8<(48/25)^2,
\]
while
\[
e^{2/3}>
1+\frac23+\frac29+\frac4{81}=\frac{157}{81}>\frac{48}{25}.
\]
Since \(h\) increases up to \(1/2\), the actual cap action
comparison now implies
\[
M(a)=\Re\mathcal T(a)>h(v)\ge h(3/10)>\frac{43}{60}.
                                                               \tag{8}
\]
Only written source constants and elementary inequalities are used.

## 3. The moving wall cut

First set \(E=v\) in (5). The original upper branch has
\(\Re J_+(1+iH)=\pi H/2\), directly from its convergent
primitive formula, and \(J(a)=-J(v)\). Hence
\[
\mathcal L(v,a,H)
=b_0+J(v)-\Re J_+(v+iH)-\pi(v+\tfrac12)H.
                                                               \tag{9}
\]
For \(0<v\le1/2\),
\[
J(v)-\Re J_+(v+iH)
=\int_0^H\Arg\sin\pi(v+is)\,ds
\le\frac{\pi}{2}\cot(\pi v)H^2.
                                                               \tag{10}
\]
This follows from
\(\Arg\sin\pi(v+is)=
\arctan(\cot(\pi v)\tanh(\pi s))\le\pi s\cot(\pi v)\).
On \(v\ge3/10\), \(\cot(\pi v)\le\tan(\pi/5)<3/4\).
At \(H=1/25\), (9)--(10) give
\[
\mathcal L(v,a,1/25)
<b_0-\frac{157\pi}{5000}
<\frac{5679}{8000}.
                                                               \tag{11}
\]
Here \(v+1/2\ge4/5\) and \(\pi>25/8\).
By (8), the reserve over (11) is greater than
\[
\frac{43}{60}-\frac{5679}{8000}
=\frac{163}{24000}.
                                                               \tag{12}
\]

Reduce the fixed positive \(\delta\) in the upper-end current
theorem, if necessary, so that all its former conditions remain
true and
\[
|\mathcal L(v-\delta,a,1/25)-\mathcal L(v,a,1/25)|<1/1000
                                                               \tag{13}
\]
uniformly in \(a\). This is uniform continuity of the displayed
analytic primitive on a fixed compact at positive height;
it asserts no new endpoint packet. Equations (12)--(13)
leave a reserve greater than \(1/250\).

## 4. The old \(49/100\) cut

Keep
\[
b(a)=\min\{49/100,\,1-a-\delta\}.
                                                               \tag{14}
\]
When \(b(a)=49/100\), one has \(1/2\le a<51/100\).
Put \(H=1/25\). For \(99/100\le s\le1\),
\[
|2\sin\pi(s+iH)|\ge2\sinh(\pi/25)>1/4,
\]
so \(\Re J_+'(s+iH)>-\log4>-3/2\). Integration gives
\[
\Re J_+(a+49/100+iH)
\le\Re J_+(1+iH)+3/200.
                                                               \tag{15}
\]
Also \(-J(49/100)<7/1000\), since \(J(1/2)=0\) and
\(\log2<7/10\). As \(\cot(49\pi/100)=\tan(\pi/100)<1/25\),
the same integral comparison as in (10) gives
\[
-\Re J_+(49/100+iH)
<\frac7{1000}+\frac{\pi}{31250}<\frac1{125}.
                                                               \tag{16}
\]
For the tangent bound one may use
\(\pi/100<1/30\) and
\(\tan x\le x/(1-x^2/2)\), which gives
\(\tan(\pi/100)<60/1799<1/25\).
The final inequality in (16) follows already from \(\pi<4\).

Substitute (15)--(16) into (5), retaining \(J(a)\ge0\):
\[
\begin{split}
\mathcal L(49/100,a,1/25)
&<\frac{101}{125}+\frac3{200}+\frac1{125}
                    -\frac{99\pi}{2500}\\
&<\frac{3561}{5000}.
\end{split}                                                     \tag{17}
\]
By (8), the reserve is greater than
\[
\frac{43}{60}-\frac{3561}{5000}
=\frac{67}{15000}>\frac1{250}.
                                                               \tag{18}
\]
Combining (6), (12)--(18), throughout the full long side,
\[
\mathcal L(b(a),a,H)<M(a)-1/250,\qquad 1/25\le H\le1.
                                                               \tag{19}
\]

## 5. The complete weighted side and its exact scope

For each base incoming parameter take the original half-grid
right boundary \(b_N=(\lceil Nb(a)\rceil-1/2)/N\).
The original cotangent remainder on its upper sign half has
modulus at most \(2e^{-2\pi NH}\). Its exact density remains
\(+N\); its orientation and the constant modes are unchanged.
Uniform continuity preserves (19) under the \(O(N^{-1})\)
cut displacement.

**Theorem.** With a sufficiently small fixed \(\delta\) in
(14), the entire weighted right-side current from
\(b_N+i/25\) to \(b_N+i\) has, after one common tolerance
and polynomial absorption, modulus at most
\[
C N^B e^{N(M(a)-1/500)}
                                                               \tag{20}
\]
uniformly for \(a\in[1/2,7/10]\), every real ordinary color,
and both level parities. Every original coefficient in \(H_N\)
and every revived term of its equivalent \(C_N\) source is retained.

Fixed ordinary derivatives follow by applying Markov's inequality
to the complete physical endpoint polynomials before (3), and
then interpolating in \(Y\). Small complex ordinary-color
neighborhoods cost an arbitrarily small rate tolerance by the
degree bound. All factorial arguments on this side remain in
their regular compact domains under small complex incoming
perturbations. Fix the base cut and contour first, preserve the
strict reserve, and apply Cauchy's formula on smaller neighborhoods.
This gives all fixed normalized mixed jets near complete color,
for example with gap \(1/1000\).

The previously proved short upper right side, from the real cut
to height \(1/25\), uses its own endpoint packet. Combining that
result with (20) pays the full upper right sign-half of a rectangle
whose upper height is one. The tall upper horizontal alias is
independently paid by its own theorem.
No new unweighted connector is suppressed by this statement:
the original constant-mode decomposition and the real-cut-to-main
joining currents remain exactly those in the upper-end theorem.
The long lower side, the left side, and a complete central path
still need their separate comparisons.

