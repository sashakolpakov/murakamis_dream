# A direct bound for the small indices in the neighboring three-twist block

Research theorem, 6 November 2026.

The real cut at index \(3N/20\) can be bounded by the original
horizontal index contour, even after the incoming height is raised.
The comparison is pointwise in both boundary variables. It therefore
remains valid when multiplied by any of the first block's contributions.
The proof uses convexity and elementary inequalities, with no moving
critical point or evaluation of a quantum sum.

## 1. Statement and its consequence for the finite expression

Use the logarithmic primitive from the
[finite two-block expression](research_mixed_selected_four_three_finite_reduction.md),
so that \(g'(w)=\log(1-e^{-2\pi i w})\) on the original regular
strip. Write
\[
 Q(s;z,b)=g(s+z)+g(s+b)-2g(s)-g(z)-g(b)+2\pi izs.
 \tag{1}
\]
Let
\[
 \begin{gathered}
 z=y+iH,\qquad b=v+ih_b,\qquad
 y,v\in[11/50,9/20],\qquad 0\le H\le7/625,\\
 -13/200\le h_s,h_b\le17/250.
 \end{gathered}
 \tag{2}
\]
The original horizontal contour for the index \(s\) has height \(h_s\).
Define its upper rate and the left real-cut rate by
\[
 B_0(y,v)=\max_{3/20\le x\le1/2}\Re Q(x+ih_s;z,b),
 \qquad B_L(y,v)=\Re Q(3/20;z,b).
 \tag{3}
\]

**Theorem 1.** Throughout (2),
\[
 \Re Q(11/50+ih_s;z,b)>B_L(y,v)+1/125.
 \quad\text{Consequently}\quad B_L<B_0-1/125.
 \tag{4}
\]

In particular this holds on every actual first-four/next-three
reference used in the finite two-block expression. For any cap rate
\(A_i(y)\) and either full selected Fourier rate \(W_\sigma(y)\),
\[
 A_i+B_L+W_\sigma<A_i+B_0+W_\sigma-1/125.
 \tag{5}
\]
This is a reduction to the same cap contribution with the ordinary
main contour. It does not assert that every expression on the right
is below the geometric rate. For the main cap \(A_0\), that bound
is already proved with gap \(1/500\), so (5) gives gap \(1/100\).

## 2. Moving the real index into the contour interval

Put \(x_0=11/50\), \(x_1=3/20\),
\(d=x_0-x_1=7/100\), and \(m=(x_0+x_1)/2=37/200\).
For real \(x\in[x_1,x_0]\), differentiation of (1) gives
\[
 \Re Q_s(x;z,b)
 =\log\frac{|\sin\pi(x+z)\sin\pi(x+b)|}{\sin^2\pi x}
       +\pi(h_b-H).
 \tag{6}
\]
Here the last term includes the original factor \(2\pi izs\).
Dropping it would change the finite expression's rate.

The identity
\(|\sin\pi(t+ih)|^2=\sin^2\pi t+\sinh^2\pi h\)
bounds the logarithm in (6) below by its value at zero heights.
For each \(w\in[11/50,9/20]\), the function
\[
 x\longmapsto\log\sin\pi(x+w)-\log\sin\pi x
 \tag{7}
\]
is convex on \([x_1,x_0]\). Its second derivative is
\(\pi^2\{\csc^2\pi x-\csc^2\pi(x+w)\}>0\):
\(x+w\in[.37,.67]\), where the sine exceeds its values
for \(x\in[.15,.22]\). The integral form of Jensen's inequality
therefore gives
\[
 \Re Q(x_0;z,b)-\Re Q(x_1;z,b)
 \ge C(y,v)+\pi d(h_b-H),
 \tag{8}
\]
where the explicit real function is
\[
 C(y,v)=d\log\frac{\sin\pi(m+y)\sin\pi(m+v)}{\sin^2\pi m}.
 \tag{9}
\]

## 3. Moving to the original imaginary height

The negative real Hessian of
\(g(s+z)-g(s)-g(z)\) is positive on the domains of (2)
and \(s\in[.15,.5]+i[-.065,.068]\), by the
[ordinary pair estimate](research_mixed_half_index_contour.md).
Apply the same estimate to \(b\). The term \(2\pi izs\)
has zero second derivative in \(s\). Hence
\(h\mapsto\Re Q(x_0+ih;z,b)\) is convex, and its
tangent at zero gives
\[
 \Re Q(x_0+ih_s;z,b)
 \ge\Re Q(x_0;z,b)-h_s I(y,v,h_b,H),
 \quad I=\Im Q_s(x_0;z,b).
 \tag{10}
\]
All arguments stay inside the same regular strips. At zero outer
heights their original arguments give \(I=\pi(y-v)\).
For nonzero outer heights define
\[
 \Delta(t,h)=\pi\int_0^h\Re\cot\pi(t+i\eta)\,d\eta.
 \tag{11}
\]
Since \(g''(w)=\pi\cot\pi w-i\pi\), the exact expression is
\[
 I=\pi(y-v)+\Delta(x_0+y,H)+\Delta(x_0+v,h_b).
 \tag{12}
\]
The sign of each correction matters. Bounding both corrections by
absolute values would lose the margin needed below.

Split each of \(y,v\) into the intervals
\[
 I_0=[11/50,7/25],\qquad I_1=[7/25,9/20].
 \tag{13}
\]
For all real \(\eta\), the cotangent formula gives
\[
 \Re\cot\pi(x_0+w+i\eta)\in
 \begin{cases}[0,1/5],&w\in I_0,\\ {}[-3/5,0],&w\in I_1.
 \end{cases}
 \tag{14}
\]
Indeed its real part has the sign of
\(\sin 2\pi(x_0+w)\), and its magnitude is at most
\(|\cot\pi(x_0+w)|\). At the two outer endpoints use
\(\tan(.06\pi)<1/5\) and \(\tan(.17\pi)<3/5\).
Both follow from \(\pi<22/7\), the upper sine polynomial
\(x-x^3/6+x^5/120\), and the lower cosine polynomial
\(1-x^2/2\).

For \(w\in I_j\), write \([a_j,b_j]\) for the corresponding
interval in (14). Then
\[
 \begin{split}
 I/\pi&\le y-v+H b_i+\max(h_ba_j,h_bb_j)=:U,\\
 I/\pi&\ge y-v+H a_i+\min(h_ba_j,h_bb_j)=:L
 \end{split}
 \tag{15}
\]
on \(I_i\times I_j\). Combining (8), (10), and (15) bounds the
difference in (4) below by
\[
 C(y,v)+\pi\{d(h_b-H)-h_s U\}\quad(h_s\ge0),
 \qquad
 C(y,v)+\pi\{d(h_b-H)-h_s L\}\quad(h_s\le0).
 \tag{16}
\]

## 4. A finite elementary inequality

For fixed signs of the two heights, each expression in (16) is
affine in either height with the other held fixed. Its minimum is
therefore attained with
\[
 h_s\in\{-13/200,0,17/250\},\qquad
 h_b\in\{-13/200,0,17/250\}.
 \tag{17}
\]
The value at \(h_s=0\) is bounded below by the smaller of the two
endpoint bounds: these are the lower bounds for the same affine
function \(C+\pi d(h_b-H)-h_s I\), with \(I\) fixed.
Thus only the two nonzero endpoints for \(h_s\) need checking.

The coefficient of \(H\) in (16) is at most
\(-d+|h_s|\,3/5<0\), so it suffices to take \(H=7/625\).
For each fixed height choice, (16) is concave in \((y,v)\)
on \(I_i\times I_j\): \(C\) is a sum of concave log-sine
functions and the remaining dependence is affine. Its minimum
occurs at a corner of that rectangle. This leaves
\(4\cdot4\cdot2\cdot3=96\) explicit scalar inequalities.

They admit rational verification. Set \(p=22/7\), and define
\[
 U_m=mp-(mp)^3/6+(mp)^5/120,
 \qquad L_w=1-\{p|1/2-m-w|\}^2/2.
 \tag{18}
\]
At the three possible corner values \(w=.22,.28,.45\),
\(0<L_w<\sin\pi(m+w)\) and
\(\sin\pi m<U_m\). For \(r=L_yL_v/U_m^2>1\), put
\[
 T(r)=2\sum_{k=0}^7\frac{1}{2k+1}
                   \left(\frac{r-1}{r+1}\right)^{2k+1}.
 \tag{19}
\]
The positive series for the logarithm gives \(T(r)<\log r\).
Consequently \(C>dT(r)\). For the remaining term \(\pi q\)
in (16), use \((22/7)q\) if \(q<0\), and
\((157/50)q\) if \(q\ge0\). All entries are now rational.
Their lower bounds, grouped by the two intervals, are
\[
 \begin{array}{c|cc}
       &v\in I_0&v\in I_1\\\hline
 y\in I_0&243/5000&207/20000\\
 y\in I_1&409/50000&1543/100000
 \end{array}
 \tag{20}
\]
Every entry exceeds \(1/125\). Exact reproduction of all 96
inequalities is provided by
[the rational checker](../experiments/check_mixed_selected_three_left_rows.py).
It uses integer fractions, not floating-point evaluations of the
phase. This proves (4). \(\square\)

## 5. Scope of the reduction

The existing finite-row argument bounds all real ordinary indices
below the left cut by \(B_L\). Together with (4), those indices
need no separate comparison to the geometric critical value.
The same holds for the contour joins already reduced to the left
cut in the finite two-block expression. Polynomial prefactors,
half-grid rounding, and any fixed ordinary-color derivative are
handled by the arbitrarily small exponential tolerance in that
expression.

For example, the literal main cap current multiplied by the entire
lower ordinary tail has rate at most
\(M+\ell_b-1/100+\tau\), with the notation of that expression.
For the whole cap, its two real cuts still require their own bounds.
The real ordinary cut at \(s=1/2\) is also unaffected by this theorem.
The result supplies no lower bound for a cancelling full quantum sum
and no new filling-volume identity by itself.
