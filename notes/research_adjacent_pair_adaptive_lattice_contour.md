# An exact contour with the second height chosen along the first

Research lemma, 2 November 2026. The adjacent-pair contour needs two
different positive heights for its second variable. The principal
stationary point uses \(\log7/(4\pi)\); the lower correction is
controlled after its second variable is placed at
\(\log2/(4\pi)\). These choices can be made in the original
iterated residue identity. There is no need first to use the
larger height on every face and then to move the lower faces.

This note proves the exact identity and lists the resulting contours.
It keeps the half-grid staircase at the triangular boundary. It is
an assembly lemma: a global asymptotic follows only after estimates
on the listed side and corner currents have been supplied.
The later [full-period contour](research_adjacent_pair_full_period_contour.md)
uses the exact zero extension of the lattice sum to remove the
diagonal staircase. That is the current assembly route. The
triangular identity here remains exact, but its separate corner
estimates have not been proved.

## 1. Half-grid cells and the two height choices

Use the exact interpolant \(f_N(x,y;u)\) from
[the cyclotomic-gauge calculation](research_adjacent_pair_cyclotomic_gauge.md).
Let \(\mathcal I_N\) be the original retained index set after
[the extreme-index theorem](research_adjacent_two_crossing_global_tails.md).
For each retained index put
\[
 I_i=[(i-1/2)/N,(i+1/2)/N],\qquad
 P_N=\bigcup_{(i,j)\in\mathcal I_N}I_i\times I_j .
 \tag{1}
\]
All retained cells lie, for sufficiently large \(N\), in a fixed
regular real neighborhood of
\[
 x>0,\qquad 0<y<1/2,\qquad x+y<1.
 \tag{2}
\]
The sine factorials and the exact Newton interpolation are
holomorphic on the complex contours below, after choosing a
sufficiently small fixed disk of boundary angles \(u\).
Indeed their real arguments remain separated from the original
strip boundaries. The finitely many smaller levels do not enter
the asymptotic assertion.

Set
\[
 h_x=\frac{3\log2}{4\pi},\quad
 h_y=\frac{\log7}{4\pi},\quad
 h_a=\frac{\log2}{4\pi}.
 \tag{3}
\]
Choose a fixed \(H>h_y\), to be increased if required by the
lower-arc estimate, and define
\[
 v(s)=
 \begin{cases}
 h_a,&-H\le s\le0,\\
 h_a+(h_y-h_a)s/h_x,&0\le s\le h_x .
 \end{cases}
 \tag{4}
\]
In particular \(v(-H)=h_a\), \(v(h_x)=h_y\), and \(v(s)\ge h_a>0\).
The \(x\)-rectangle has upper height \(h_x\) and lower height
\(-H\). At each fixed complex value \(x\) of that contour,
the \(y\)-rectangle has upper height \(v(\Im x)\) and lower
height \(-h_y\).

## 2. The one-variable identity with unequal heights

For a half-grid interval \(I=[a,b]\), positive heights \(p,m\),
and a holomorphic function \(F\), define
\[
\begin{aligned}
 U_I^{p}F&=N\int_a^b F(t+ip)\,dt,\\
 C_{I,+}^{p}F&=N\int_a^b F(t+ip)
        \frac{e^{2\pi iN(t+ip)}}{1-e^{2\pi iN(t+ip)}}\,dt,\\
 C_{I,-}^{m}F&=N\int_a^b F(t-im)
        \frac{e^{-2\pi iN(t-im)}}{1-e^{-2\pi iN(t-im)}}\,dt,\\
 E_I^{p,m}F&=-iN\int_{-m}^{p}
       \frac{F(b+is)-F(a+is)}{1+e^{-2\pi Ns}}\,ds .
\end{aligned}
\tag{5}
\]
Integration of
\(\pi N\cot(\pi Nz)-i\pi N\) around that asymmetric rectangle
gives
\[
 \sum_{a<k/N<b}F(k/N)
       =(U_I^p+C_{I,+}^p+C_{I,-}^m+E_I^{p,m})F.
 \tag{6}
\]
This is the same exact residue identity as for equal heights;
the two horizontal sides need not have the same distance from
the real axis.

For the \(x\)-coordinate use the four operators in (5) with
\((p,m)=(h_x,H)\), and call them \(X_U,X_+,X_-,X_E\).
For the \(y\)-coordinate, at a fixed point \(x\), use
\((p,m)=(v(\Im x),h_y)\), and call them
\(Y_U(x),Y_+(x),Y_-(x),Y_E(x)\).

## 3. The exact adaptive identity

**Lemma.** With the order of integration just specified,
\[
 \boxed{\displaystyle
 \sum_{(i,j)\in\mathcal I_N}f_N(i/N,j/N;u)
  =\sum_{(i,j)\in\mathcal I_N}
     \sum_{\alpha,\beta\in\{U,+,-,E\}}
       X_{\alpha,I_i}
           \bigl[Y_{\beta,I_j}(x)f_N(x,\cdot;u)\bigr].}
 \tag{7}
\]
This identity has all sixteen terms. It is exact at each integer
level where the contours are regular.

**Proof.** First apply (6) in \(x\), with \(y=j/N\) fixed.
This gives four integrals of the values \(f_N(x,j/N;u)\).
At every point of each of these integrals, \(x\) is now fixed.
Apply (6) in \(y\) with the indicated positive height
\(v(\Im x)\). It gives the value \(f_N(x,j/N;u)\) exactly.
Substitution in the four \(x\)-integrals proves (7).

No analytic dependence of the height function on \(x\) is
required: the one-variable residue identity is used separately
at each fixed \(x\). All integrals are over compact parameter
sets and \(v\) is continuous and piecewise smooth, so this
substitution and the finite summation are legitimate.
\(\square\)

In geometric notation the same assertion has a useful check.
On an \(x\)-vertical side, write
\[
 x=e+is,\qquad y=t+i v(s).
 \]
Then
\[
 dx\wedge dy=i\,ds\wedge dt .
 \tag{8}
\]
The apparent extra term \(i v'(s)\,ds\) in \(dy\) vanishes
when wedged with \(dx=i\,ds\). Thus (7) does not omit a
Jacobian or a connector caused by the changing height.
The iterated proof above remains the primary justification.

## 4. Cancellation of shared cell boundaries

The cancellation in (7) is the same literal cancellation as
in the fixed-height cell formula.

On a shared \(x\)-side, the same complex point \(e+is\)
appears from the two adjacent cells. They use the same
\(v(s)\), the same \(y\)-interval and the same \(y\)-operator.
Their signs are opposite. Their entire currents cancel.
On a shared \(y\)-side the \(y\)-endpoint integrands cancel
for each fixed \(x\), before applying its \(x\)-operator.

At a corner, the coefficient of the two-endpoint current
is the alternating sum of the four adjacent cell indicators.
Its parameter region is the same from every adjacent cell,
because it depends only on \(s=\Im x\):
\[
              -H\le s\le h_x,\qquad
                    -h_y\le t\le v(s).
 \tag{9}
\]
Thus all interior corner currents cancel. Nonzero corner
currents at the boundary staircase remain. Their coefficients
can have either sign, and their full two-parameter regions
(9) must be kept.

For the retained triangular cutoff, every row contains a
consecutive interval of \(i\)'s. After the shared-side
cancellation, its right endpoint is the actual half-grid
endpoint of that interval. As the row changes, these
endpoints form the original staircase. No endpoint has
been replaced by a smooth function of a complex \(y\).

## 5. The resulting contours and their weights

The four products with horizontal \(x\)-contours have the
following coordinate heights:
\[
\begin{array}{c|c|c|c}
x\text{ term}&\Im x&\Im y\text{ for }Y_U,Y_+
                   &\Im y\text{ for }Y_-\\ \hline
X_U&h_x&h_y&-h_y\\
X_+&h_x&h_y&-h_y\\
X_-&-H&h_a&-h_y.
\end{array}
\tag{10}
\]
The \(X_UY_U\) term is exactly
\[
 N^2\int_{P_N}
            f_N(x+ih_x,y+ih_y;u)\,dx\,dy.
 \tag{11}
\]
It is the surface containing the original finite critical point.

For \(X_EY_U\) and \(X_EY_+\), the \(x\)-side currents are
on the coupled surfaces
\[
 x=e+is,\qquad y=t+i v(s),
                  \qquad -H\le s\le h_x.
 \tag{12}
\]
For \(X_EY_-\), replace \(v(s)\) in (12) by \(-h_y\).
For \(X_UY_E\), \(X_+Y_E\), and \(X_-Y_E\), the \(y\)
endpoint ranges are respectively
\[
 [-h_y,h_y],\qquad [-h_y,h_y],\qquad [-h_y,h_a].
 \tag{13}
\]
The \(X_EY_E\) currents have precisely the region (9).

The exponential penalties, to be subtracted from
\(\Re W\) when applying an absolute bound, are
\[
\begin{array}{c|c}
\text{factor}&\text{penalty}\\ \hline
X_U&0\\
X_+&2\pi h_x\\
X_-&2\pi H\\
X_E\text{ at height }s&2\pi(-s)_+\\
Y_U&0\\
Y_+\text{ at the current }x&2\pi v(\Im x)\\
Y_-&2\pi h_y\\
Y_E\text{ at height }t&2\pi(-t)_+ .
\end{array}
\tag{14}
\]
These bounds follow from the exact rational kernels in (5).
Their denominators are uniformly bounded away from zero on
the horizontal sides because \(v(s)\ge h_a>0\).
At vertical endpoints the exact logistic factor is bounded
by \(1\) on the upper part and by the indicated exponential
on the lower part. There is no singular zero-height estimate
being assigned separately to an infinite Fourier series.

## 6. Where the complementary-arc theorem applies

The term \(X_-Y_U\) has \(y\)-height \(h_a\) from the start.
For each horizontal \(y\)-parameter, sum its consecutive
\(x\)-cell intervals into the one interval belonging to
that row of \(P_N\). Its lower \(x\)-integral is then
exactly the complete rational kernel treated in
[the complementary-arc theorem](research_adjacent_pair_lower_arc_cancellation.md).
Take \(H\) sufficiently large that its fixed radius
\(r=e^{-2\pi H}\) satisfies that theorem.

The two endpoints differ from the ideal endpoints
\(\epsilon\) and \(1-\Re y-\epsilon\) by \(O(N^{-1})\).
This includes the displacement from the center of a
\(y\)-cell to a point on its horizontal side. The
complementary-arc estimate was proved on fixed neighborhoods
of those endpoints, so it applies uniformly.

The \(y\)-kernel in \(X_-Y_+\) is independent of \(x\).
The same arc replacement can therefore be made before
multiplying by that kernel. Its additional penalty
\(2\pi h_a\) only improves the estimate.
Consequently these two terms are exponentially below the
selected rate, with all lower \(x\)-modes retained.

This replacement changes only those horizontal \(x\)-integrals.
It does not remove the \(X_-Y_E\) currents in (13), the
coupled \(X_EY_\beta\) surfaces in (12), or the staircase
corner currents in (9).

## 7. A precise sufficient conclusion

Assume, in addition to the proved horizontal maximum and
the complementary-arc estimate, that the following bounds
are established with one fixed positive loss:

* every remaining horizontal correction has its penalized
  phase below the selected rate;
* every uncancelled side current on (12)--(13) has its
  penalized phase below that rate;
* every nonzero corner current has that bound on the
  whole region (9), including corners approaching an
  oblique limiting side.

Then (7) leaves only (11) at the selected rate. The known
nondegenerate stationary point and the exact summand
normalization give its usual two-dimensional Gaussian
coefficient. The selected boundary polynomial consequently
has the desired nonzero local asymptotic. This is a
conditional conclusion until the stated side and corner
bounds are supplied.

Unlike moving the \(y\)-height after decomposing the old
rectangular contour, (7) introduces no additional
deformation currents. The price is explicit: the corner
domain is (9), and the \(x\)-side surfaces have the
coupled height \(v(s)\). Bounds proved only on a
rectangular subset of those domains would be insufficient.
