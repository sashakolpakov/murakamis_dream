# A supporting plane for the terminal action

Research deduction, 5 November 2026. The optimized terminal action has
a quantitative concavity bound along an entire horizontal slice of its
input disk. The bound includes the derivative with respect to the
neighbouring leg. It therefore retains the term needed when this end
is joined to the rest of an open word.

This result concerns the geometric action on the full input disk.
The comparison with the finite quantum source is used only on the
smaller rectangles where that comparison has been proved. In
particular, it does not assert the false absolute-value comparison
on the whole independent disk.

## 1. Holomorphic elimination and the real part of the Hessian

For a complex matrix \(H\), write
\(\operatorname{Re}_{\mathrm H}H=(H+H^*)/2\). If \(H\) is complex
symmetric, this is its entrywise real part. The inequality
\(\operatorname{Re}_{\mathrm H}H\ge cI\) means
\(\operatorname{Re}(v^*Hv)\ge c\|v\|^2\) for every complex vector
\(v\).

**Lemma 1.** Let \(X(a,y)\) be holomorphic, with one external complex
variable \(a\) and finitely many internal variables \(y\). Suppose
\(y=y(a)\) is a holomorphic solution of \(X_y=0\), and along its
graph
\[
                 -\operatorname{Re}X''\ge cI,\qquad c>0.
\tag{1}
\]
Then \(P(a)=X(a,y(a))\) satisfies
\[
                     -\operatorname{Re}P''(a)\ge c.
\tag{2}
\]

*Proof.* Put \(H=-X''\) and decompose it into the external and
internal blocks. Its internal block \(H_{yy}\) is invertible:
\(c\|v\|^2\le\operatorname{Re}(v^*H_{yy}v)\le
\|v\|\|H_{yy}v\|\) gives
\(\|H_{yy}^{-1}\|\le1/c\). Implicit differentiation gives
\[
 y'=-H_{yy}^{-1}H_{ya},\qquad
 -P''=H_{aa}-H_{ay}H_{yy}^{-1}H_{ya}.
\tag{3}
\]
For \(v=(1,-H_{yy}^{-1}H_{ya})\), one has
\(Hv=(-P'',0)\). Consequently
\[
 -\operatorname{Re}P''=\operatorname{Re}(v^*Hv)
                 \ge c\|v\|^2\ge c.
\]
This uses the Hermitian pairing even though the differentiation and
Schur complement in (3) are holomorphic. \(\square\)

There is no requirement that the graph \((a,y(a))\) be a straight
line. It is enough that (1) holds at every point of that graph over
the external segment to be considered.

## 2. The actual terminal action, including its external variable

Use \(g,J,\mathcal X_\epsilon\) and the original terminal map
\((e(a),t(a),u(a))\) from
[the calibrated terminal comparison](research_mixed_terminal_half_endpoint_gap.md),
equations (1)--(4). Here \(\epsilon\in\{0,1\}\) is the terminal
block type minus three. Explicitly,
\[
\begin{split}
 \mathcal X_\epsilon(a,e,t,u)
 ={}&g(t+a)+g(t+e)-(2+\epsilon)g(t)\\
    &-g(a)-(1+\epsilon)g(e)+J(e)+B(e,u)+i\pi eu+2\pi iat,\\
 B(e,u)={}&-2J(1/2-u)-3J(u)-J(e-u),\\
 g(z)={}&J(z)+\frac{i\pi}{2}z(1-z).
\end{split}
\tag{4}
\]
All primitives have their original logarithmic determinations.

Set
\[
\begin{split}
 Q&=[.23,.45]+i[-.12,.12],\\
 E&=[.33,.47]+i[-.09,.08],\\
 U&=[.21,.25]+i[.01,.10],\qquad c=6\pi/49.
\end{split}
\tag{5}
\]
The original input disks are
\[
 D_3=\{|a-(.35-.01i)|\le.09\},\qquad
 D_4=\{|a-(.30-.052i)|\le.064\}.
\tag{6}
\]
They lie inside \(Q\). The
[original localization theorem](research_mixed_open_word_critical_localization.md)
provides a holomorphic terminal map on a neighbourhood of each disk,
with \(e\in E,t\in Q,u\in U\).

**Proposition 2.** On either disk, for either terminal type, let
\[
 P_\epsilon(a)=\mathcal X_\epsilon(a,e(a),t(a),u(a)).
\tag{7}
\]
Then
\[
 -\operatorname{Re}P_\epsilon''(a)\ge c,
 \qquad |P_\epsilon''(a)|\le D:=\frac{1261\pi}{6}.
\tag{8}
\]

*Proof.* The real part of the Hessian in (4) is exactly that of
\[
 B(e,u)+W(e,t)+V(t,a)-\epsilon[J(e)+J(t)],
\quad
 W(e,t)=J(e+t)-J(t),\quad
 V(t,a)=J(t+a)-J(t)-J(a).
\tag{9}
\]
The omitted difference is \(i\pi\) times a polynomial with real
coefficients of degree at most two, whose Hessian has zero Hermitian
real part. In particular, (9) has not acquired an extra \(-J(e)\).

The elementary bounds in
[the open-word Hessian proof](research_mixed_open_word_hessian.md),
equations (5), (9) and (10), give
\[
\begin{split}
 -\operatorname{Re}B''&\ge cI_{e,u},\\
 -\operatorname{Re}W''&\ge(\pi/8)I_t,\\
 -\operatorname{Re}V''&\ge(\pi/8)I_{t,a}.
\end{split}
\tag{10}
\]
The remaining terms in (9) have positive semidefinite negative real
Hessian. Since \(\pi/8>6\pi/49\), these bounds prove (1) for
the four variables \((a,e,t,u)\), including the external variable.
Lemma 1 proves the first inequality in (8).

For the explicit upper bound, direct differentiation gives
\[
 \mathcal X_{aa}=\pi\cot\pi(t+a)-\pi\cot\pi a,
 \qquad \mathcal X_{at}=\pi\cot\pi(t+a)+i\pi,
 \qquad \mathcal X_{ae}=\mathcal X_{au}=0.
\tag{11}
\]
For real \(x,y\),
\[
 |\cot(x+iy)|^2
 =\frac{\cos^2x+\sinh^2y}{\sin^2x+\sinh^2y}
 \le\max\{1,\cot^2x\}.
\tag{12}
\]
On \(a\in Q\), this implies \(|\cot\pi a|<2\), since
\(\Re a\in[.23,.45]\subset(1/6,1/2)\). On
\(\Re(t+a)\in[.46,.90]\), it gives
\(|\cot\pi(t+a)|<4\): the real sine is at least
\(\sin(\pi/10)=(\sqrt5-1)/4>3/10\).
Thus \(|\mathcal X_{aa}|<6\pi\) and
\(|\mathcal X_{at}|<5\pi\). The internal inverse norm is at
most \(1/c\). The scalar Schur complement consequently satisfies
\[
 |P_\epsilon''|
 \le6\pi+\frac{25\pi^2}{c}=\frac{1261\pi}{6}.
\]
This rough bound is used only to make a vertical error explicit.
\(\square\)

## 3. The supporting plane and the cost of changing height

**Corollary 3.** Suppose \(r,a\) belong to the same disk (6), and
write \(a-r=\xi+i\eta\), where \(\xi,\eta\) are real. Then
\[
\begin{split}
 \Re P_\epsilon(a)
 \le{}&\Re P_\epsilon(r)
       +\Re[P_\epsilon'(r)(a-r)]
       -\frac c4\xi^2+C_{\rm v}\eta^2,\\
 C_{\rm v}:={}&\frac D2+\frac{D^2}{c}.
\end{split}
\tag{13}
\]
If \(\eta=0\), the stronger inequality is
\[
 \Re P_\epsilon(a)
 \le\Re P_\epsilon(r)+\Re[P_\epsilon'(r)(a-r)]
                    -\frac{3\pi}{49}\xi^2.
\tag{14}
\]

*Proof.* The segment is contained in the disk. Taylor's integral
formula applies to \(P_\epsilon\) along that segment. Write
\(P_\epsilon''=-A+iB\); (8) gives \(c\le A\le D\) and
\(|B|\le D\). Therefore
\[
 \Re[P_\epsilon''(\xi+i\eta)^2]
 \le-c\xi^2+D\eta^2+2D|\xi\eta|
 \le-\frac c2\xi^2+\left(D+\frac{2D^2}{c}\right)\eta^2.
\tag{15}
\]
Integration against \(1-s\), for \(0\le s\le1\), proves
(13). When \(\eta=0\), integrate the first inequality in (8)
directly to obtain (14). \(\square\)

The affine term in these formulas is essential. The external variable
is not itself stationary for the isolated terminal action. Its
derivative cancels the derivative supplied by the adjacent part of
the original open-word action.

## 4. Consequence for the proved terminal right sector

Let \(S_{\epsilon,N}(a,e,w;\sigma)\) denote the exact finite
terminal expression
\[
 C_{\epsilon,N}(e^{-2\pi ia},e^{-2\pi ie})
 H_N(w,e^{2\pi ie})d_N(e^{-2\pi ie})^\epsilon
 e^{2\pi iN\sigma e},\qquad\sigma\in\{0,\epsilon\}.
\tag{16}
\]
Here \(e\) is the real terminal integration coordinate, rather than
the optimized coordinate \(e(a)\) in (7), and \(w\) is the ordinary
boundary colour variable, whose complete value is \(-2\). Keep
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.001].
\tag{17}
\]
The [full-row terminal theorem](research_mixed_terminal_raw_half_gap.md),
combined with the
[polynomial endpoint estimate](research_mixed_endpoint_polynomial_collar.md),
already proves, uniformly on the appropriate rectangle and
\(1/2\le e\le1\),
\[
 |\partial_w^jS_{\epsilon,N}(a,e,w;\sigma)|
 \le C_jN^{A_j}
       \exp N\{\Re P_\epsilon(a)-1/400-K(e)\},
 \quad K(e)=-\int_{1/2}^{e}\log\sin(\pi t)\,dt.
\tag{18}
\]
For each fixed derivative order the colour variable ranges in a
sufficiently small fixed disk about \(-2\); both level parities
and both terminal selections are included.

If \(r,a\in R_\nu\) have the same height, (14) and (18) give
\[
\begin{split}
 |\partial_w^jS_{\epsilon,N}(a,e,w;\sigma)|
 \le C_jN^{A_j}\exp N\bigl\{
 &\Re P_\epsilon(r)+\Re[P_\epsilon'(r)(a-r)]\\
 &-1/400-K(e)-(3\pi/49)|a-r|^2\bigr\}.
\end{split}
\tag{19}
\]
This holds throughout the horizontal slice of the rectangle, with
no assumption that \(a\) is close to \(r\).

For different heights, (13) gives the same assertion with the last
quadratic term replaced by \(-c\xi^2/4+C_{\rm v}\eta^2\).
In particular, if \(C_{\rm v}\eta^2\le1/800\), the finite
terminal loss remains at least \(1/800+K(e)\), in addition to
the horizontal loss. This is a quantitative small-height statement;
it does not cover every physical attenuation.

Any external factorial allocation or external Fourier selection
belongs to the adjacent part of the full sum and has not been
discarded in (19). The estimate supplies the terminal contribution
and its exact affine term for subsequent assembly. It does not by
itself bound that adjacent part, prove noncancellation of the whole
open sum, or extend the class of short partial fillings.

## 5. Verification

The proof uses the written Hessian inequalities, the established
holomorphic terminal map and the already checked finite-source
estimate. All new steps are exact matrix algebra, trigonometric
inequalities and Taylor's integral formula. No new critical roots,
parameter covering or numerical test are required.
