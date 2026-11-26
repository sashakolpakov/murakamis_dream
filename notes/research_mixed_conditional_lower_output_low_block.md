# Low conditional rows through two twenty-fifths at lower outgoing height

Research deduction, 8 November 2026. This companion to
[the complete upper-block bound](research_mixed_conditional_lower_output_upper_block.md)
pays the original physical rows \(j/N\le2/25\), jointly with
the complete first cap, throughout the same incoming rectangle.
It also pays a fixed small-height part of the canonical lower-cut
current. The middle rows and long currents are retained.
No numerical evaluation or frozen-source edit is used.

## 1. The exact finite group and its disk rate

Use the exact \(U_{0,N},P_j,p_j,X\) and incoming rectangle of
the upper-block theorem:
\[
 a=x-i\eta,\quad x\in[1/2,7/10],\quad
 0\le\eta\le9/125,\quad X=e^{-2\pi ia},\quad
             T=e^{2\pi\eta}<8/5.
                                                               \tag{1}
\]
Let
\[
 L_N=\lfloor2N/25\rfloor+1,\qquad
 C^{\rm lo}_{1,N}(X,Y)=
       \sum_{j=0}^{L_N-1}
          \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
                                                               \tag{2}
\]
The zero row is included. There is no termination rule at a
continuous input, and both parity cases use the literal index set.

For \(|Y|\le1\), the original carrier and incoming numerator
combine exactly, factor by factor, into
\[
 |X|^{-1}|1-Xr^k|
       =|T-e^{-2\pi i(x+k/N)}|\le T+1<13/5<e.
                                                               \tag{3}
\]
Here \(e>8/3>13/5\) follows from the first four exponential
terms. The outgoing numerator obeys \(|1-Yr^k|\le2\).
Consequently the full absolute row rate satisfies
\[
 E(t)\le (1+\log2)t-3J(t)
       <t\{47/10-3\log(6t)\},
               \qquad0<t\le2/25.                              \tag{4}
\]
We used \(\log2<7/10\) and
\[
 2\sin\pi s\ge6s\quad(0\le s\le1/6),\qquad
 J(t)\ge t(\log(6t)-1).
 \]
The sine inequality is the chord inequality on \([0,1/6]\).
The right side of (4) is increasing up to \(2/25\), since
its derivative is \(17/10-3\log(6t)>0\) there. Moreover
\[
 \log(25/12)<3/4,\qquad
 e^{3/4}>1+\frac34+\frac9{32}+\frac9{128}
                   =\frac{269}{128}>\frac{25}{12}.
 \]
Thus
\[
             \sup_{0\le t\le2/25}E(t)<\frac{139}{250}.
                                                               \tag{5}
\]
At \(t=0\) the exact rate and row are respectively zero and one.

The endpoint-uniform sine-factorial estimate and (3) give the
complete positive finite bound
\[
 \sum_{j=0}^{L_N-1}
       \left|\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}\right|
 \le C_\tau N^{A_\tau}e^{N(139/250+\tau)},\qquad |Y|\le1.
                                                               \tag{6}
\]
This does not need a numerator lower bound; every numerator
zero and every positive subset of these rows are retained.

The complete all-real cap bound
\(1549/1500\), with the separate true private ends, is traced
in Section 3 of the upper-block theorem. Therefore
\[
 \begin{split}
 &|U_{0,N}(w,X)|
       \sum_{j=0}^{L_N-1}
          \left|\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}\right|\\
 &\hspace{12mm}\le C_\tau N^{A_\tau}
          e^{N(2383/1500+\tau)},\qquad
                 w\in[-2,2],\quad |Y|\le1 .
 \end{split}                                                    \tag{7}
\]
The cap remains the complete coherent source. No positive
estimate for its separate Newton terms is asserted.

## 2. Comparison with the actual ordinary-next source

Use exactly the ordinary-next references, independent unselected
plateaux, \(A_*,p,B_3,\Lambda_{123}\), and outgoing halfweight
of the upper-block theorem, Section 4. In particular
\[
 y=q+ih_*,\quad q\in[.22,.45],\quad -.102<h_*<-.001,
 \qquad z=u+i\Im z_*,\quad u\in[.22,.45].
                                                               \tag{8}
\]
The original whole weight and third-factor estimates reduce
the comparison for (7) to
\[
 \frac{2383}{1500}-\frac{J(q)}2-p(q-\Re y_*)-A_*,
             \qquad A_*>\frac74+\frac{819}{35200}.
                                                               \tag{9}
\]
The same two marginal cases give the following strict reserves.
For \(p\le0\),
\[
 \frac74-\frac{2383}{1500}-\frac{11}{80}
                     =\frac{143}{6000}>\frac1{50}.
 \]
For \(p\ge0\), use \(819/35200>1/45\); then
\[
 \frac74+\frac1{45}-\frac{2383}{1500}
                  -\frac1{12}-\frac{801}{10000}
                    =\frac{1811}{90000}>\frac1{50}.
                                                               \tag{10}
\]
All ingredients are original action comparisons, with no
evaluation of a new critical point.

It follows that, for \(\beta=0,1\),
\[
 \begin{split}
 &|U_{0,N}(w,X)|
   \sum_{j=0}^{L_N-1}
     \left|\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}\right|
   |d_N(Y)C_{\beta,N}(Y,Z)|\,|d_N(Z)|^{\beta/2}\\
 &\hspace{12mm}\le C_\tau N^{A_\tau}
         e^{N\{\Lambda_{123}(z)-1/50+\tau\}} .
 \end{split}                                                    \tag{11}
\]
This holds on the full incoming rectangle (1), with all real
ordinary colors, both parities, and the complete third kernel.
Both factorial and forcing alternatives of \(d_N(Y)\) remain
in the cited weight estimate. There is no selected factor
\(Y^{-N}\) in (11).

## 3. A regular collar at the canonical lower cut

The lower residue boundary for the retained middle indices is
\[
 \ell_N=(L_N-\tfrac12)/N
       =\frac{\lfloor2N/25\rfloor+1/2}{N}
                       =2/25+O(N^{-1}).
                                                               \tag{12}
\]
The canonical interpolation from
[the original lower-current proof](research_mixed_conditional_negative_height_lower_currents.md)
is
\[
 T_N(s;a,y)=e^{2\pi iNas}
       \Pi_N(a+s)\Pi_N(y+s)
       E_N(a)E_N(y)E_N(s)^3 ,
                                                               \tag{13}
\]
with exactly the original continued factorials. At a physical
\(s=j/N\), it is the row in (2).

Near real \(s=2/25\), all relevant real parts are uniformly
inside their original strips: \(s>0\),
\(\Re(a+s)\in[.58,.78]\), and
\(\Re(y+s)\in[.30,.53]\). The incoming and outgoing
primitives therefore use the original logarithmic branches,
and the canonical factorial estimate is uniform on a fixed
small complex neighborhood. Its complete phase is
\[
 Q(s;a,y)=g(a+s)+g(y+s)-3g(s)-g(a)-g(y)+2\pi ias .
                                                               \tag{14}
\]
At real \(s=2/25\), \(\Re Q\) is exactly the rate bounded
in (4)--(5). The complete cap bound and the strict reserves
in (10) are uniform on the compact base parameter sets.
Consequently uniform phase continuity supplies fixed numbers
\(\epsilon,\sigma_0>0\), independent of \(N\), such that
the full original product with \(T_N(s;a,y)\) in place
of a conditional row has a following-plane gap greater than
\(1/100\) for
\[
 |\Re s-2/25|\le\epsilon,\qquad |\Im s|\le\sigma_0 .
                                                               \tag{15}
\]
One first chooses a tolerance smaller than the strict reserve
in (10), then the compact factorial neighborhood and these
widths; no quantitative width is inferred.

For all sufficiently large \(N\), the cut (12) lies in (15).
On its vertical line,
\[
 e^{2\pi iN\ell_N}=-1 .
 \]
Thus the original upper and lower cotangent remainders have
bounded factors \(1/(1+e^{2\pi N|\Im s|})\), up to their
fixed scalar constants. The whole cotangent kernel is also
bounded there. Multiplication by the original factor \(N\)
and integration over the fixed short segment
\(\ell_N+i[-\sigma_0,\sigma_0]\) preserve an exponential
gap. The same statement holds for its unweighted main-path
subsegments. This proves only the short regular lower-cut
pieces, not either long side or a join reaching an as yet
uncontrolled saddle.

## 4. Exact scope and normalization

The first outer measure is \(N\,da\), and the next measure
is \(N\,dy\). The row set (2), all contour endpoints and
paths are held fixed at each base reference. The same
nonzero outgoing \(d_N(Z)\) packet and action identity as
in the upper-block theorem remove the halfweight only near
the actual \(z_*\), with no division on the independent
plateau. After sharing the strict reserves, the unweighted
low-block integral and the short lower-cut currents have
normalized local gap \(1/200\). Cauchy's formula on smaller
fixed neighborhoods gives all fixed normalized mixed jets.
The all-real ordinary-color estimate is retained separately.

Together with the upper-block theorem this leaves exactly the
middle physical indices
\[
                   L_N\le j<\lceil N/2\rceil
 \]
in the troublesome incoming rectangle. Their complete main
integral, the long alias sides, and any unweighted joins
outside (15) remain obligations. No full conditional packet,
whole next transfer, or terminal-reference extension follows
from the present bound.
