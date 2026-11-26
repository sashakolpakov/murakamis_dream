# The own-three upper end and its complete-first payment at deeper heights

Private research proof, 8 November 2026. Every next own-three
physical row with reflected index \(v\le q\) is bounded by
its actual last-row rate. The positive outgoing-height carrier
is retained. On the subdomain \(|Y|\le7/10\), that last-row
rate is paid jointly with the complete first conditional factor,
using the actual own-three endpoint certificate and the
first-factor profile transport.

The last-row reduction holds on the entire stated radial
domain. Its complete-first payment at larger radii is not
proved here. No numerical evaluation or frozen-source edit
is used.

## 1. Literal upper-end block and exact reflected rate

Keep the actual ordinary-next own-three references, original
cap plane and following action of
[the complete-first lower-half theorem](research_mixed_next_own_three_below_half_complete_first.md).
Thus
\[
\begin{gathered}
a=x+ih_a,\quad y=q+ih_y,\quad z=u+ih_z,\qquad
x,u\in P=[11/50,9/20],\quad 0\le q\le11/50,\\
-.072<h_a<0,\qquad -.102<h_s,h_y<-.001,\qquad
-.065<h_z<.068 .
\end{gathered}
\tag{1}
\]
All actual reference correlations remain imposed. Write
\[
X=e^{-2\pi ia},\quad Y=Re^{-2\pi iq},\quad
Z=\rho e^{-2\pi iu},\quad
R=e^{2\pi h_y}\in(13/25,1),\quad \rho=e^{2\pi h_z},
\]
and
\[
\delta_a=-2\pi h_a,\quad \delta_y=-2\pi h_y,\quad
L_0=\delta_y+2\pi(h_z)_+=-\log R+\log_+\rho .
\tag{2}
\]
The complete first factor is the original \(C_{1,N}(X,Y)\).
For \(r=e^{-2\pi i/N}\), \(D=N-1\),
\(P_j=(r;r)_j\), \(p_j(W)=(rW;r)_j\), define
\[
\mathcal U_{0,N}^{\rm end}(Y,Z;q)
=\sum_{\lceil N(1-q)\rceil\le j\le D}
       \left|\frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2}\right|.
\tag{3}
\]
An empty sum is zero. This is a positive sum of literal
original rows, not a factorization through the terminal row.

The exact physical rate is
\[
E_0(t;y,z)=
\int_0^t\log|1-Ye^{-2\pi ib}|\,db
+\int_0^t\log|1-Ze^{-2\pi ib}|\,db
-2J(t)+\delta_y t.
\tag{4}
\]
The complete-period means and \(J(1)=0\) give
\[
                            E_0(1;y,z)=L_0.
\tag{5}
\]
For \(v=1-t\), use \(J(1-v)=-J(v)\) and keep the
incoming chirp. Direct subtraction of (5) yields
\[
\begin{split}
\Phi(v)&:=E_0(1-v;y,z)-L_0\\
 &=2J(v)
 -\int_0^v\log|R^{-1}-e^{-2\pi i(q-s)}|\,ds
 -\int_0^v\log|1-\rho e^{-2\pi i(u-s)}|\,ds.
\end{split}
\tag{6}
\]
In particular the folded incoming radius is \(R^{-1}\),
and the outgoing complete-period term has already been
retained in \(L_0\). Both original sign-dependent carriers
are present.

## 2. The entire upper end is below its last rate

For \(0\le v\le q\le11/50\le u\le9/20\), both real arcs
\([q-v,q]\) and \([u-v,u]\) lie in \([0,1/2]\).
The function
\[
f_\rho(s)=\log|1-\rho e^{-2\pi is}|
\]
is increasing on this interval, for every \(\rho>0\),
with the original logarithmic limit at a zero.

For the first integral in (6), \(R^{-1}\ge1\) and
\[
|R^{-1}-e^{-2\pi is}|\ge|1-e^{-2\pi is}|.
\]
Translating the nonnegative arc to start at zero therefore gives
\[
\int_0^v\log|R^{-1}-e^{-2\pi i(q-s)}|\,ds\ge J(v).
\tag{7}
\]

For \(0<\rho\le1\), the original radial primitive inequality
\[
G_\rho(v):=\int_0^v f_\rho(s)\,ds\ge J(v),
\qquad 0\le v\le1/2,
\tag{8}
\]
is the radial log-arc bound used in
[the right real-row theorem, Sections 2--3](research_mixed_right_tail_endpoint_bound.md).
After translating the outgoing arc to start at zero,
its integral is at least (8). If \(\rho>1\), first use
\[
f_\rho(s)=\log\rho+f_{\rho^{-1}}(s).
\]
The same argument then gives the lower bound
\(v\log\rho+J(v)\ge J(v)\).
Consequently, for either outgoing-height sign,
\[
\int_0^v\log|1-\rho e^{-2\pi i(u-s)}|\,ds\ge J(v).
\tag{9}
\]
Equations (6)--(9) prove the all-radius rate reduction
\[
\boxed{\quad E_0(1-v;y,z)\le L_0
                 \qquad(0\le v\le q\le11/50).\quad}
\tag{10}
\]
No equality or nonzero lower estimate for a terminal finite
row is asserted.

For every fixed tolerance \(\tau>0\), the uniform zero-safe
factorial and product upper bounds now give
\[
\mathcal U_{0,N}^{\rm end}(Y,Z;q)
\le C_\tau N^{B_\tau}e^{N(L_0+\tau)}
\tag{11}
\]
on all of (1). Indeed every index in (3) has exactly
\(v=1-j/N\le q\); the last index \(j=D\) has \(v=1/N\).
The endpoint and near-end sine-factorial errors are
\(O(\log N)\), and the original numerator zeros can only
improve the positive upper bound. Both parities and arbitrary
subsets of (3) are included.

## 3. Actual own-three calibration and first-profile transport

We now impose just the additional radial restriction
\[
                              R\le7/10.
\tag{12}
\]
For a first main or real-cut profile put
\[
\mathcal A(s;q)
=B_U(x)+\Re Q_1(s;a,y)+L_0-\Re g(y),
\tag{13}
\]
where \(Q_1\) is the original phase, including \(2\pi ias\).
There is no outgoing halfweight for own type three.

At \(q_0=11/50\), the actual own-three last-row theorem
[with its four original carriers](research_mixed_typed_last_row_support_completion.md)
places \(L_0-\Re g(y)/2\) strictly below its own supporting
plane. The first main plane, the cap plane and the matched
marginals therefore give
\[
\mathcal A(s;q_0)<\Lambda_{123}(z)-10^{-10}.
\tag{14}
\]
Here the strict last-row comparison is used only for its
sign. The first main retains at least
\(\kappa(\alpha-q_0)^2>1/6250000000>10^{-10}\),
where \(\kappa=1/2500000\) and \(\alpha=\Re y_*>.24\).
For either first real cut \(1/8,1/2\), the original cut
certificate instead retains \(1/2000\).
These are the actual own-three ordinary source inputs from
[ordinary source assembly, Sections 1--2](research_mixed_three_row_source_assembly.md).

Both first-main clippings, to
\[
1/6\le s_R\le5/12,\qquad \Im s=h_s<0,
\tag{15}
\]
are valid at the same current \(q\) by the joint-profile
theorem. The next last rate is independent of \(s\).
At a fixed clipped point, the exact derivative of (13) is
\[
\partial_q\mathcal A
=\log|1-Rr_s e^{-2\pi i(q+s_R)}|
                 -2\log|1-Re^{-2\pi iq}|,
\qquad r_s=e^{2\pi h_s}\in(1/2,1).
\tag{16}
\]
The positive outgoing carrier in \(L_0\) is constant along
this transport.

The pure first-profile proof in
[next-four last-row transport, Section 2](research_mixed_next_lower_left_next_four_last_row.md)
proves that (16) is positive under (12).
Its calculation is independent of the next own flag.
To specify the exact inequalities being reused, let
\(D=|1-Y|^2\) and let \(U\) be the square of the
numerator modulus in (16). For \(q\le1/10\),
\[
D\le9/20,\qquad U\ge3/4>D^2.
\]
On the other ranges its bounds are
\[
\begin{array}{c|c|c}
q\text{ range}&D\le&U\ge\\ \hline
[1/10,1/5]&1+R^2-3R/5&1+R^2/4+R/10\\
[1/5,11/50]&1+R^2-9R/25&1+R^2/4+13R/20.
\end{array}
\tag{17}
\]
Each numerator minus the square of its denominator bound
is strictly concave on \(R\in[1/2,7/10]\).
Its two endpoint values are respectively
\[
(21/100,119/2500),\qquad
(1213/5000,5607/125000),
\]
all positive. Thus (16) is positive and (14) transports to
the whole interval in (1).

For the first real low cut \(s=1/8\), the same derivative
with \(r_s=1\) is positive on the full radius range; the
four elementary intervals are explicitly retained in
[central-four completion, Section 4](research_mixed_next_lower_left_central_four_completion.md).
That section already calibrates this real-low by next-last
profile for both next own types, including \(L_0\).
The first real half is bounded by its negative-height
half profile, since its whole original vertical comparison
has \(\Im Q_{1,s}\ge\pi(x-q)\ge0\).
It can then be clipped by (15) and transported by (16).

Finally the allocated double-last profile satisfies on the
entire radial range, and hence on (12),
\[
B_U(x)+\delta_a+L_0-\Re g(y)
                 <\Lambda_{123}(z)-109/2000.
\tag{18}
\]
This is exactly the all-typed double-last lemma in Section 4
of central-four completion; its statement explicitly includes
own type three and the positive outgoing carrier.
Equations (14)--(18) pay every first main, real-cut and
last alternative with the actual next last rate attached.
No next own-four low-cut domination is used.

## 4. Complete-first finite consequence and remaining scope

The positive first low physical block increases to its
real cut, including its zero row. The complete first
middle interpolation, with the original half-grid cuts,
reduces to the paid profiles through its two horizontal
aliases at \(-1/5,+4\), all four weighted vertical halves,
and both unweighted joins, by
[the complete-current theorem](research_mixed_next_lower_left_complete_currents.md).
The positive first upper physical block reduces to its
real-half and last alternatives by
[the own-four upper-row theorem](research_mixed_next_lower_left_own_four_upper_rows.md).
These comparisons keep \(L_0\) attached, because it is
independent of the first index.

The full forced \(d_N(Y)\) upper envelope gives the original
allocation \(-\Re g(y)\), including \(q=0\); the canonical
factorial seam theorem supplies the separate row symbol.
Neither is divided out or replaced by a relative weight
asymptotic. All true end rows and both parities are retained.
Choose the finite product tolerances within (14), and use
(11). The result is the actual positive finite bound
\[
\boxed{\quad
|U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)|
       \mathcal U_{0,N}^{\rm end}(Y,Z;q)
\le C N^B e^{N\{\Lambda_{123}(z)-10^{-11}\}},
\qquad R\le7/10 .
\quad}
\tag{19}
\]
It holds for all real ordinary colors and arbitrary subsets
of the positive next block. The central first integration
retains \(+N\,da\), with the same exponential gap.
Fixed-base signed partial sums and integrals have normalized
local mixed jets with gap \(10^{-12}\); the index set in
(3) is frozen at the base point for this assertion.

For \(R>7/10\), (10)--(11) remain proved, as do the separate
first real-low by next-last and double-last inequalities.
The complete first-main by next-last comparison is not
established there. The middle physical strip \(q<v<q+1/5\)
is not controlled by the end-row argument, and no complete
next own-three sum or noncentral first-incoming transfer
is asserted.
