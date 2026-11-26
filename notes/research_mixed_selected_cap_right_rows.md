# The right cap cut is below its original horizontal contour

Research deduction, 6 November 2026. At the selected positive height,
the first type-four cap's right real cut is uniformly below its main
private line. The comparison is pointwise in the outgoing coordinate
and preserves both complete Fourier alternatives. It uses only the
canonical cap phase and elementary scalar inequalities. No root,
source sum, or parameter cover is evaluated.

## 1. Statement

Use the bare cap phase and profiles in
[the finite first-four/next-three reduction](research_mixed_selected_four_three_finite_reduction.md):
\[
 \Psi(e,z)=S(e)+J(e+z)-J(z)-i\pi ez-g(e),\qquad
 z=y+iH,\quad y\in P=[.22,.45],\quad 0\le H\le.014,
 \quad -.051<h_e<-.019.
\tag{1}
\]
The fixed private height \(h_e\) is the actual first type-four
reference height. Set
\[
 A_0(y)=\max_{.27\le x\le.49}\Re\Psi(x+ih_e,z),
 \qquad A_R(y)=\Re\Psi(.49,z).
\tag{2}
\]

**Theorem 1.** Throughout (1),
\[
 \Re\Psi(.4+ih_e,z)>A_R(y)+1/1250,
 \qquad A_R(y)<A_0(y)-1/1250.
\tag{3}
\]

The statement does not use the type of the next block. Its
consequences for a proved central gap below use the next-three
comparison at \(H=7/625\).

## 2. Two exact constants at the real private trial

Fix \(e_0=2/5\). Keep the original canonical quantities
\[
 E=e^{-2\pi i e_0},\quad W=\sqrt{1-2/E},\quad D=iEW,
 \quad C=|1-D|^2,\quad T=\pi-2\Arg(1-D).
\tag{4}
\]
The square root and argument are those fixed in
[the cap-alias proof, Section 1](research_mixed_selected_cap_alias_transport.md).
In particular \(\Re D>0>\Im D\), and its original
logarithmic lift gives
\[
 \Re\Psi_e(e_0,z)=\log\frac{|1-Ee^{-2\pi iz}|}{C},
 \qquad
 \Im\Psi_e(e_0,z)=\mathcal A(e_0+y,H)+T,
\tag{5}
\]
where \(\mathcal A(t,h)=\arg(1-e^{2\pi h-2\pi it})\)
on the original regular strip. For the first identity, take moduli
in \((1-E)(V-E)=-(1-D)^2\), with
\(V=e^{-2\pi iu_c(e_0)}\). The contribution
\(2\pi i u_c\) cancels the modulus of \(V\), so there
is no missing exponential factor.

**Lemma 2.** The exact canonical constants satisfy
\[
                         C>12/5,\qquad T>\pi/8.
\tag{6}
\]

*Proof.* Write
\[
 c=\cos(\pi/5)=\frac{1+\sqrt5}{4},\quad
 L=|D|^2=\sqrt{5+4c},\quad
 A=\Re(D^2)=1-2c-2c^2.
\tag{7}
\]
Then
\(2\Re D=\sqrt{2L+2A}\) and
\(C=1+L-\sqrt{2L+2A}\).
The expression
\[
 P(c)=\frac{124}{25}+8c+4c^2-\frac{24}{5}\sqrt{5+4c}
\tag{8}
\]
is positive for \(c\ge4/5\). Indeed its derivative is
\(8+8c-(48/5)/\sqrt{5+4c}>0\), and
\(\sqrt{41/5}<29/10\) gives \(P(4/5)>0\).
Since \(L-7/5>0\), (8) is exactly the strict squared
comparison
\[
                2L+2A<(L-7/5)^2.
\tag{9}
\]
Taking the indicated positive square roots proves \(C>12/5\).

For the angle, the rational bounds
\[
 \frac{809}{1000}<c<\frac{81}{100},\qquad L<\frac{2871}{1000}
\tag{10}
\]
follow by squaring the bounds on \(\sqrt5\) and on
\(\sqrt{5+4c}\). Since \(A\) decreases in \(c\),
they imply
\[
 \begin{split}
 (\Re D)^2
  &=\frac{L+A}{2}<\frac{472019}{1000000}
                                      <\left(\frac{69}{100}\right)^2,\\
 (\Im D)^2
  &=\frac{L-A}{2}<\frac{1501}{625}
                                      <\left(\frac{31}{20}\right)^2.
 \end{split}
\tag{11}
\]
Consequently \(\alpha=\Arg(1-D)\) lies in
\((0,\pi/2)\), and
\[
 \cot\alpha=\frac{1-\Re D}{-\Im D}>\frac15,
 \qquad
 T=\pi-2\alpha>2\arctan(1/5)
 >\frac{148}{375}>\frac\pi8.
\tag{12}
\]
The last two bounds use the alternating arctangent series and
\(\pi<22/7\). This proves (6). \(\square\)

## 3. Horizontal gain and the signed vertical cost

The [bare cap Hessian theorem](research_mixed_first_cap_plateau_phase.md)
gives horizontal concavity in \(e\) on the whole private
rectangle at all heights in (1). It also gives vertical convexity
with the outgoing target fixed. Therefore
\[
 \begin{split}
 \Re\Psi(.4,z)-\Re\Psi(.49,z)
       &\ge-\frac9{100}\Re\Psi_e(.4,z),\\
 \Re\Psi(.4+ih_e,z)-\Re\Psi(.4,z)
       &\ge-h_e\Im\Psi_e(.4,z).
 \end{split}
\tag{13}
\]
Both connecting segments remain inside the established regular
rectangle. In particular the second line is a signed tangent bound;
it does not assert monotonicity in private height.

Put \(R=e^{2\pi H}\). Since \(2\pi H<1/10\),
\(1\le R<10/9\). Split the outgoing interval as follows:
\[
 I_1=[.22,.27],\qquad I_2=[.27,.35],\qquad I_3=[.35,.45].
\tag{14}
\]
The exact numerator modulus and its upper bounds are
\[
 |1-Ee^{-2\pi iz}|^2=(R-1)^2+4R\sin^2\pi(.4+y),
 \qquad
 |1-Ee^{-2\pi iz}|<
 \begin{cases}
 19/9,&y\in I_1,\\
 {}11/6,&y\in I_2,\\
 {}3/2,&y\in I_3.
 \end{cases}
\tag{15}
\]
For the first use \(1+R<19/9\). In the second interval,
\(.4+y\ge.67>2/3\), so the sine square is less than
\(3/4\); the squared bound is \(271/81<(11/6)^2\).
In the third interval it is at most \(1/2\), giving
\(181/81<(3/2)^2\).
Equations (5)--(6), and
\(\log r>2(r-1)/(r+1)\) for \(r>1\), now give
\[
 -\Re\Psi_e(.4,z)>
 \begin{cases}
 26/203,&y\in I_1,\\
 {}34/127,&y\in I_2,\\
 {}6/13,&y\in I_3.
 \end{cases}
\tag{16}
\]

For the imaginary derivative, the original argument has
\(\mathcal A(t,0)=\pi(1/2-t)\) when \(1/2<t<1\),
and \(\partial_h\mathcal A=\pi\Re\cot\pi(t+ih)\).
Its real cotangent is at least \(\cot\pi t\) on this
strip, for all real heights. Thus (5)--(6) imply
\[
 \Im\Psi_e(.4,z)>
       \pi\{9/40-y+H\cot\pi(.4+y)\}.
\tag{17}
\]
The cotangent is bounded below on the three intervals in (14) by
\(-3/5,-1,-2\), respectively. The first is the elementary
\(\tan(.17\pi)<3/5\) bound in
[the left-row proof](research_mixed_selected_three_left_rows.md).
The last follows from \(\cot(.15\pi)<2\): the sine
cubic and cosine quartic at the rational lower angle
\(.15(157/50)\) give respectively \(\sin(.15\pi)>.45\)
and \(\cos(.15\pi)<.9\).
Since \(H\le7/500\), (17) gives
\[
 \Im\Psi_e(.4,z)>-\pi
 \begin{cases}
 267/5000,&y\in I_1,\\
 {}139/1000,&y\in I_2,\\
 {}253/1000,&y\in I_3.
 \end{cases}
\tag{18}
\]
The bound \(-h_e<51/1000\) retains its sign in the
second line of (13). Combining (13), (16), and (18), the
three lower bounds for the difference in (3) are strictly larger
than
\[
 \frac9{100}
   \left(\frac{26}{203},\frac{34}{127},\frac6{13}\right)
 -\frac{51}{1000}\frac{22}{7}
   \left(\frac{267}{5000},\frac{139}{1000},\frac{253}{1000}\right).
\tag{19}
\]
Every entry exceeds \(1/1250\), by rational cross
multiplication. This proves (3). \(\square\)

## 4. What the comparison removes

For any ordinary profile \(B_j\) and either complete Fourier
alternative, the same pointwise comparison gives
\[
 A_R+B_j+W_\sigma<A_0+B_j+W_\sigma-1/1250.
\tag{20}
\]
At \(H=7/625\), the proved main/main gap \(1/500\)
therefore pays the right-cap-cut times ordinary-main pair, with
gap \(7/2500\). The right-cap-cut times ordinary-half-row
pair is merely reduced to the still-open main-cap times that same
half row. No sign for the latter is inferred from (20).

Together with the complete alias and left-row reductions, and the
already proved last rows, the remaining independent comparisons
for first-four/next-three are exactly
\[
                       A_0B_R,\qquad A_LB_0,\qquad A_LB_R,
\tag{21}
\]
where a product label means the sum of the corresponding rates,
with the original Fourier alternative and outgoing tangent retained.
More explicitly, at \(H=7/625\) put
\[
 \mathcal D_3(y,v)=
 \max_{(i,j)\in\{(0,R),(L,0),(L,R)\}}
 \max_{\sigma\in\{\mathrm{fac},\mathrm{force}\}}
 \{A_i(y)+B_j(y,v)+W_\sigma(y)-M-\ell_b(v)\}.
\tag{22}
\]
The [complete five-comparison assembly](research_mixed_selected_four_three_five_comparisons.md)
and (20) imply, for each fixed ordinary-color derivative order \(k\)
and every \(\tau>0\),
\[
 |\partial_w^k\mathcal K_N(w;X,Y)|
 \le C_{\tau,k}N^{D_{\tau,k}}
 \exp N\{M+\ell_b(v)+\max(-1/500,\mathcal D_3(y,v))+\tau\}.
\tag{23}
\]
Here \(\mathcal K_N\) is the entire literal finite product in
the finite-source reduction, including its full selected Fourier
polynomial, every physical row and all contour contributions.
The same compact regular-strip transfer as in the finite reduction
preserves ordinary colors, fixed derivatives, half-grid cuts and both
level parities, with a single arbitrarily small rate tolerance.
This statement does not prove those three remaining signs or whole
open-word dominance.
