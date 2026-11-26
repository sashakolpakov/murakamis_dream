# Pointwise removal of terminal alias profiles

Research deduction, 6 November 2026. The lower transform alias of
either terminal type is strictly below its original main-height
profile. For terminal type three, both private aliases have the same
property. These comparisons fix the incoming coordinate and the other
index, including its cut or alias state. The 25 regular profiles
therefore reduce to twelve for type three and twenty for type four.
No remaining comparison sign or numerical evaluation is asserted.

## 1. Original domains and argument bounds

Use the original phases, five states per index, and literal penalties
in [the complete terminal envelope](research_mixed_terminal_concave_profile_envelope.md),
equations (2)--(6). The real target intervals are
\[
t_R\in[.15,.5],\qquad
v_R\in[.1,.4]\ (\epsilon=0),\qquad
v_R\in[.27,.49]\ (\epsilon=1).
\tag{1}
\]
The incoming coordinate can be any
\(a\in[.22,.45]+i[-.12,.12]\). In particular all conclusions
hold at every common selected height \(H\in[0,.014]\).
Keep the actual original main heights:
\[
\begin{array}{c|c|c}
\epsilon&h_t^*&h_v^*\\ \hline
0&(-.072,.021)&(.049,.077)\\
1&(-.108,-.020)&(-.051,-.019).
\end{array}
\tag{2}
\]
These are the [original endpoint image ranges](research_mixed_open_word_endpoint_rectangles.md),
not critical heights at the independent target \(a\).

On the original regular strip put
\[
A(y,k)=\Im g'(y+ik)=\Arg(1-e^{2\pi k-2\pi iy}),\qquad0<y<1.
\]
Its radial derivative has the sign of \(\sin(2\pi y)\);
its limits at radii zero and infinity are zero and
\(\pi(1-2y)\). Therefore
\[
\pi\min(1-2y,0)\le A(y,k)\le\pi\max(1-2y,0).
\tag{3}
\]
At \(y=1/2\) the logarithm's argument is \(1+e^{2\pi k}>0\).
Thus no logarithmic cut or lift is changed. Every summed real
argument below lies strictly between zero and one.

## 2. The lower transform alias of either type

**Proposition 1.** For every fixed admitted \(a,v,t_R\),
\[
\Re\Phi_\epsilon(a;t_R-.12i,v)-.24\pi
<
\Re\Phi_\epsilon(a;t_R+ih_t^*,v)-\frac{213\pi}{5000}.
\tag{4}
\]
The private coordinate may be on any of its five states, with its
penalty unchanged.

Write \(x=t_R,y=a_R,z=v_R,k=\Im t\). The exact derivative,
including the original shared chirp, is
\[
\Im\Phi_{\epsilon,t}
=A(x+y,k+\Im a)+A(x+z,k+\Im v)-3A(x,k)+2\pi y.
\tag{5}
\]
Since \(x\le.5\), \(A(x,k)\ge0\). Also
\[
2y+[1-2(x+y)]_+=\max(2y,1-2x)\le9/10,\qquad
[1-2(x+z)]_+\le1/2.
\]
Thus (3) gives \(\Im\Phi_{\epsilon,t}\le7\pi/5\).
Both actual main heights exceed \(-.12\) and are strictly below
\(.021\). Integrating
\(\partial_k\Re\Phi_\epsilon=-\Im\Phi_{\epsilon,t}\) gives
\[
\Re\Phi_\epsilon(t_R-.12i)-\Re\Phi_\epsilon(t_R+ih_t^*)
\le\frac{7\pi}{5}(.12+h_t^*)<\frac{987\pi}{5000}.
\]
Subtract the original penalty
\(.24\pi=1200\pi/5000\) to obtain (4). This is pointwise,
with no target maximization or contour deformation. \(\square\)

## 3. Both type-three private aliases

**Proposition 2.** For terminal type three and every admitted
\(a,t,x=\xi_R\in[.1,.4]\),
\[
\Re\Phi_0(a;t,x\pm.12i)-.24\pi
<
\Re\Phi_0(a;t,x+ih_\xi^*)-\frac{13\pi}{10000}.
\tag{6}
\]
The transform coordinate can be on any of its five states; its
penalty is unchanged.

Set \(f(h)=\Re\Phi_0(a;t,x+ih)\), \(\eta=3/25\),
and \(h_*=h_\xi^*\). The
[full enlarged type-three Hessian theorem](research_mixed_terminal_three_joint_zero_mode.md),
equation (10a), proves \(f''(h)>0\) for \(|h|\le\eta\),
including every admitted incoming coordinate and transform state.
At the real private coordinate its original derivative gives
\[
L:=-f'(0)=2\pi x+A(t_R+x,\Im t),\qquad
0\le L\le
\begin{cases}
7\pi/10,&x\in[.1,.25],\\
4\pi/5,&x\in[.25,.4].
\end{cases}
\tag{7}
\]
The real \(J'\)-terms contribute no imaginary part, while
\(-2g'(x)+i\pi\) contributes \(2\pi x\).
If \(t_R+x\le.5\), (3) bounds \(L\) above by
\(\pi(1-2t_R)\le7\pi/10\). Otherwise it bounds \(L\)
above by \(2\pi x\) and below by
\(\pi(1-2t_R)\ge0\). This proves (7).

The exact second derivative is
\[
f''(h)/\pi=
4\Re\cot\pi(x+ih)+2\Re\tan\pi(x+ih)
                         -\Re\cot\pi(t+x+ih).
\tag{8}
\]
Individual real cotangents and tangents are at most their real-axis
values here. A negative summed real cotangent also has magnitude at
most its real-axis value. It follows that
\[
0<f''(h)<
\begin{cases}
14\pi,&x\in[.1,.25],\\
(111/10)\pi,&x\in[.25,.4].
\end{cases}
\tag{9}
\]
For explicit witnesses set \(k=\cot(\pi/10)\).
The identity \(k^2=5+2\sqrt5\) gives
\(3<k<37/12<31/10\), using \(2<\sqrt5<9/4\).
On the first interval \(r=\cot\pi x\in[1,k]\);
\(4r+2/r\) increases there and is less than
\(4(37/12)+2/(37/12)=1441/111<13\).
Also \(t_R+x\le.75\), so the final negative cotangent in
(8) is at most one. On the second interval, convexity of
\(4r+2/r\) bounds it by its endpoint values six and
\(4/k+2k<4/3+37/6=15/2<8\).
Now \(t_R+x\le.9\), so the final negative cotangent is
less than \(31/10\). These bounds hold for every admitted
imaginary sum.

Convexity and Taylor's formula yield
\[
f(h_*)\ge f(0)-Lh_*,
\qquad f(\pm\eta)\le f(0)\mp L\eta+M\eta^2/2,
\tag{10}
\]
where \(M\) is the appropriate constant in (9).
For the negative alias, use \(h_*<77/1000\). After subtracting
its penalty and dividing by \(\pi\), the resulting bounds are
\[
\begin{split}
\frac7{10}\left(\frac3{25}+\frac{77}{1000}\right)
+7\left(\frac3{25}\right)^2-\frac6{25}
&=-\frac{13}{10000},\\
\frac45\left(\frac3{25}+\frac{77}{1000}\right)
+\frac{111}{20}\left(\frac3{25}\right)^2-\frac6{25}
&=-\frac{31}{12500}.
\end{split}
\tag{11}
\]
For the positive alias, \(L(h_*-\eta)\le0\); the corresponding
bounds are \(-87/625\) and \(-2001/12500\).
Both are smaller than \(-13/10000\). The strict inequalities
in (2) and (9) give (6). \(\square\)

## 4. Remaining regular comparisons

In the original state notation \(0,L,R,-,+\), Proposition 1
replaces transform state \(-\) by \(0\) at the same real
coordinate. Proposition 2 replaces either private alias by \(0\),
also at the same real coordinate. Hence the retained alphabets are
\[
\begin{array}{c|c|c|c}
\epsilon&\text{transform states}&\text{private states}&\text{count}\\ \hline
0&\{0,L,R,+\}&\{0,L,R\}&12\\
1&\{0,L,R,+\}&\{0,L,R,-,+\}&20.
\end{array}
\tag{12}
\]
If both replacements apply, make them successively. Every removed
rate has at least the strict reserve in (4) or (6). This bounds
the original currents; it does not alter their exact decomposition.

All terms outside \(\Phi_\epsilon\) are independent of the replaced
index. The inequalities therefore survive addition of the adjacent
ordinary phase, its original incoming tangent, the incoming
halfweight, and either complete selected Fourier alternative at
the same incoming target and height. The two rates still combine
by a maximum. In particular the reduction is valid at \(H=.0135\).

There remain 24 or 40 regular terminal/Fourier comparisons before
using an established main sign. The entropy and constant profiles
are separate. No domination of the original real cuts, upper
transform alias, or type-four private aliases is asserted here.
Saved alias reserves against an original supporting plane alone
do not imply domination by the selected-height main maximum:
that plane is an upper, not a lower, bound for the main profile.

Only elementary identities and previously proved full-product
curvature were used. No analytic function, root, source, optimizer,
or reference image was evaluated.

