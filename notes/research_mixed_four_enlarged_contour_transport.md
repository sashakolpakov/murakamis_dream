# Transport after a type-four coordinate on the enlarged contours

Research proof, 5 November 2026. The horizontal source estimates use a
longer index contour than the original first-collar argument. This note
proves the required height transport on that contour. The other target
may vary independently through its whole real plateau. The comparison
uses the original reference action and retains the two possible real-row
excesses. No critical point is continued to a new target.

## 1. The fixed reference and the finite quantity

Consider an ordinary conditional factor whose first external coordinate
has type four and whose own type is \(3+\epsilon\), with
\(\epsilon\in\{0,1\}\). Fix its actual open-word reference
\((s_0,a_0,b_0)\). Write
\[
 c=\Im a_0\in(-.102,-.001),\qquad h_b=\Im b_0,
 \qquad y_0=\Im s_0\in(-.108,.068).
 \tag{1}
\]
All references and allocations are those of the ordinary conditional
theorems. In particular \(|h_b|\le .108\); a type-four second
argument has its actual negative height. An attached external leg is
allowed only when the ordinary reference theorem includes it and all
bounds in (1) hold; a first attached type-four leg with height at or
below \(-.102\) is outside this statement. A terminal
conditional factor with its different endpoint graph is not included.

Choose independent horizontal targets
\[
 x\in I_4=[.24,.363],\qquad z\in P=[.22,.45],
 \qquad a_k=x+ik,\quad b=z+ih_b,
 \tag{2}
\]
and put \(H=7/500\). The unselected path is \(c\le k\le0\);
the selected path is \(0\le k\le H\). Let
\[
 \begin{split}
 Q_\epsilon(w;a,b)&=g(w+a)+g(w+b)-(2+\epsilon)g(w)+2\pi iaw,\\
 g'(v)&=\log(1-e^{-2\pi iv}),\\
 F_k(w)&=\Re\{Q_\epsilon(w;a_k,b)-\tfrac32g(a_k)
                                      -(1+\epsilon/2)g(b)\}.
 \end{split}
 \tag{3}
\]
The primitive, its constant, and its logarithmic lift are unchanged
from the [original fixed-contour proof](research_mixed_four_fixed_contour_transport.md).
For the selected first halfweight the two upper rates are
\[
 F_k^{\mathrm{fac}}(w)=F_k(w)-\pi k,
 \qquad F_k^{\mathrm{force}}(w)=F_k(w)+\tfrac12\Re g(a_k).
 \tag{4}
\]
They come from the actual Fourier polynomial, including its selected
monomial. Their maximum bounds that halfweight with any prescribed
positive rate tolerance. On the negative path the unselected
factorial rate in (3) bounds it.

Let \(B(x,z)\) be the original supporting plane with quadratic loss
\(\kappa=1/2500000\), as in equation (4) of the
[fixed-reference prefix theorem](research_mixed_first_collar_fixed_reference_completion.md).
The full allocated row rate at the horizontal baseline
\((a_c,b)\) is denoted by \(\mathcal R_c(u)\). Define
\[
 D(x,z)=\bigl[\max\{\mathcal R_c(1/2),\mathcal R_c(1)\}
                                  -B(x,z)\bigr]_+,
 \qquad V(x,z)=B(x,z)+D(x,z).
 \tag{5}
\]
Both ordinary left-row comparisons have been proved. Together with
the right-tail endpoint theorem, they bound every real tail by \(V\)
at the baseline. They also bound each central current by \(V\),
using the following contours:
\[
 \begin{array}{c|ccc}
 \epsilon&\text{left cut }\ell&\text{lower height}&\text{upper height}\\\hline
 0&3/20&-1/5&1\\
 1&1/8&-1/5&5/4.
 \end{array}
 \tag{6}
\]
The right cut is \(1/2\) in both cases. The zero-mode horizontal
segment stays at the original height \(y_0\); the two joins run
from zero to that height. The baseline horizontal additional-frequency
terms have gaps at least \(13/100\) below \(B\). Specifically,
the [half-index theorem](research_mixed_half_index_contour.md) gives
gaps \(557\pi/6250\) and \(13/100\) for own type three;
the [smaller-cut theorem](research_mixed_four_left_cut_extension.md)
gives \(1893\pi/25000\) and more than \(7/50\) for own type four.
These are estimates on the complete currents, not an assumption
about a saddle at the horizontal target.

## 2. Negative heights on the zero-mode segment and its joins

Both rectangles in (6) lie in
\[
             \mathcal K=[1/8,1/2]+i[-1/5,5/4].
 \tag{7}
\]
Fix \(w=v+iy\in\mathcal K\). Direct differentiation gives
\[
 F_k''(w)=\pi\{\tfrac32\Re\cot\pi a_k
                         -\Re\cot\pi(w+a_k)\}>0
                    \qquad(-.102\le k\le0).
 \tag{8}
\]
Here \(\Re\cot\pi a_k>1/3\) on the stated rectangle, as
proved in the original fixed-contour argument. If \(x+v\ge1/2\),
the second cotangent has nonpositive real part. Otherwise it is at
most \(\cot(.365\pi)=\tan(.135\pi)<1/2\).
For the last inequality, \(.135\pi<17/40\) and
\(t/(1-t^2/2)<1/2\) at \(t=17/40\).
Thus the enlarged real interval causes no loss of convexity.

Set
\[
 A(t,y)=\arg(1-e^{2\pi y-2\pi it}),\qquad 0<t<1,
 \tag{9}
\]
with the original argument. At zero height,
\[
 F'_0(w)=\tfrac32\pi(1/2-x)-2\pi v-A(x+v,y).
 \tag{10}
\]
If \(x+v\ge1/2\), the argument bounds in the original proof
give \(F'_0(w)\le\pi(x/2-1/4)<0\). If \(x+v<1/2\),
then \(A(t,y)\) increases with \(y\). At a fixed negative
height \(y_*\),
\[
                 A_t(t,y_*)=\pi\{\Im\cot\pi(t+iy_*)-1\}>-\pi.
 \tag{11}
\]
Consequently, after replacing \(y\ge-.108\) by \(-.108\),
the right side of (10) decreases with both \(x\) and \(v\).
Its maximum is at \(x=.24,v=1/8\), where it is
\[
                     .14\pi-A(.365,-.108)<17/100.
 \tag{12}
\]

For an explicit rational verification, \(e^{-.216\pi}>1/2\),
\(\sin(.27\pi)>37/50\), and \(\cos(.27\pi)<67/100\).
The exponential bound follows from \(\log2>.69>.216\pi\),
using the first three terms of the positive
\(2\operatorname{atanh}(1/3)\) series. For the trigonometric
bounds use \(.27\pi>21/25\), the lower sine polynomial
\(t-t^3/6\), and the upper cosine polynomial
\(1-t^2/2+t^4/24\) at \(t=21/25\).
The tangent of the angle in (12) therefore exceeds \(74/267\).
The inequality
\[
       \arctan(74/267)>74/267-(74/267)^3/3>27/100
 \tag{13}
\]
and \(.14\pi<.44\) prove (12).

Convexity (8) now shows, on the zero-mode segment and both joins,
\[
 F_k(w)-F_c(w)\le(k-c)F'_0(w)
             <\frac{51}{500}\frac{17}{100}<\frac9{500}.
 \tag{14}
\]
Indeed their heights lie between zero and \(y_0\), and hence
are at least \(-.108\). On the larger horizontal sides one
may instead use \(A(t,y)>0\) when \(t<1/2\). This gives
\[
 F_k(w)-F_c(w)<\frac{51}{500}\frac{7\pi}{50}<\frac9{200}.
 \tag{15}
\]
That increase is smaller than every baseline horizontal alias gap
in Section 1.

## 3. The selected branches decrease on the entire rectangle

For \(0\le k\le H\), write
\(A_0=A(x,k)\), \(A_1=A(x+v,y+k)\). The exact derivative is
\[
            (F_k^{\mathrm{force}})'=A_0-A_1-2\pi v.
 \tag{16}
\]
If \(x+v\ge1/2\), the bounds
\(A_0<\pi(1-2x)\) and \(A_1\ge\pi(1-2x-2v)\)
make (16) negative. Suppose \(x+v<1/2\). The original bound
\(\cot(.24\pi)<11/10\) implies
\[
 A_0\le\pi(1/2-x+77/5000),\qquad
 A_1\ge A(x+v,-1/5).
 \tag{17}
\]
By (11), the resulting upper bound for (16) decreases with
\(x\) and \(v\). At their lower endpoints it is
\[
              \frac{127\pi}{5000}-A(.365,-1/5)<0.
 \tag{18}
\]
For a rational verification, \(e^{-2\pi/5}>1/4\): the
exponential-series estimate in the type-three fixed-reference proof
even gives \(e^{2\pi/5}<15/4\). The same sine and cosine
bounds as above give
\[
 A(.365,-1/5)>\arctan(74/467)
             >74/467-(74/467)^3/3>3/20,
 \tag{19}
\]
whereas \(127\pi/5000<2/25\). This proves (18).

The factorial derivative is (16) plus \(A_0/2-\pi<0\), so
it is also negative. At \(k=0\) the forced branch lies below
the factorial branch because \(J(x)=\Re g(x)<0\). Thus both
selected branches stay below the unselected rate at zero throughout
\(\mathcal K\). In particular (14) controls their zero-mode
currents, and (15) controls their horizontal aliases.

## 4. Every real row and every vertical additional-frequency term

Let \(R(u;k)\) be the bare complete row rate, so that
\[
 R(u;k)=I_{a_k}(u)+I_b(u)-(2+\epsilon)J(u)-2\pi ku,
 \qquad I_a(u)=\int_0^u\log|1-e^{-2\pi i(a+t)}|\,dt.
 \tag{20}
\]
The other halfweight is the fixed constant \(-\epsilon\Re g(b)/2\).
The first halfweight is
\[
 q_0(k)=-\tfrac12\Re g(a_k),\qquad
 q_1(k)=\max\{-\tfrac12\Re g(a_k)-\pi k,0\}.
 \tag{21}
\]
The exact Poisson-kernel calculation in the
[real-tail transport proof](research_mixed_four_first_vertical_source_transport.md)
gives, on every row \(0\le u\le1\),
\[
 \partial_kR=
 \begin{cases}
 -\pi u-\pi\displaystyle\int_x^{x+u}P_{e^{2\pi k}}(t)\,dt,&k<0,\\
 -\pi u+\pi\displaystyle\int_x^{x+u}P_{e^{-2\pi k}}(t)\,dt,&k>0.
 \end{cases}
 \tag{22}
\]
Both integrals lie in \([0,1]\), including intervals crossing
an integer. Their integrated bounds extend continuously to \(k=0\),
including logarithmic zeros.

For \(u\ge1/8\), the negative-path allocated derivative is at most
\(\pi(1/4-x/2-u)\le\pi/200\). Its total increase is therefore
less than \(51\pi/100000\). The positive selected factorial
derivative is at most \(\pi(1/2-x-u)\le27\pi/200\); its
increase is at most \(189\pi/100000\). Their sum is
\[
                      \frac{3\pi}{1250}<\frac1{125}.
 \tag{23}
\]
The selected forced branch increases from zero by at most
\(\pi H(1-u)\le49\pi/4000\). At zero it starts below the
factorial branch by \(-J(x)/2>137/3500>49\pi/4000\), as
proved by the integral estimate in the same real-tail note.
Thus this branch needs no larger allowance than (23).

For \(u\le\ell\), the positive left-row derivative on the full
plateau, equation (17) of the asymmetric-contour theorem, remains
greater than \(1/2\) after the height change. Its hypotheses are
\(\Re a,\Re b\in[.22,.45]\) and
\(|\Im a|,|\Im b|\le.12\), which include (1)--(2).
The halfweights are independent of the row. Consequently this
entire tail is bounded by its moved left cut, to which (23) applies.
All remaining real rows outside the central interval also satisfy
(23) directly. At their baseline, these rows are bounded by \(V\)
from (5). No new endpoint-shape theorem at the moved heights is used.

It remains to control the vertical additional-frequency terms. The
all-height bounds for \(\Im\partial_wQ_\epsilon\) in the two
contour theorems apply to every outer argument in the same plateau
strip. They therefore still apply to \((a_k,b)\). After subtraction
of \(2\pi|\Im w|\), the rate decreases away from each real cut.
The Fourier allocations in (4) are independent of \(w\), so this
holds for both selected branches. Each vertical term is bounded by
its moved real-cut rate and hence by \(V+1/125\).
This argument uses the all-height marginal bounds, not a convexity
claim on a taller strip than the one where Hessian bounds are known.

## 5. Complete finite transport and the first-collar consequence

All shifted real arguments on the fixed central contours lie strictly
between zero and one. The exact factorial interpolation and residue
identity therefore retain the original rows, coefficient \(+N\),
and both level parities on these larger compact rectangles. The
zero-mode currents have allowance \(9/500\), the real tails and
vertical aliases have allowance \(1/125\), and the horizontal
aliases remain strictly below \(B\). They combine by taking a
maximum, not by adding the allowances.

**Theorem 1.** Put \(Y_k=e^{-2\pi ia_k}\), \(Z=e^{-2\pi ib}\).
For every \(\tau>0\), the literal conditional factor satisfies
\[
 \begin{split}
 &|C_{\epsilon,N}(Y_k,Z)|
 |d_N(Y_k)Y_k^{-N\sigma}|^{1/2}|d_N(Z)|^{\epsilon/2}\\
 &\hspace{8mm}\le C_\tau N^A
        \exp N\{B(x,z)+D(x,z)+9/500+\tau\},
 \end{split}
 \tag{24}
\]
where \(\sigma=0\) on \([c,0]\) and \(\sigma=1\) on
\([0,H]\). The bound is uniform over the ordinary reference
families and the targets in (2). It includes every original finite
row and both Fourier upper alternatives. Half-grid rounding,
polynomial factors and the original Fourier bound use the single
prescribed tolerance. There is no division by a finite factor.

For application to an open word, take \(m\ge4\), a first pair
\((3+\alpha,4)\), and an ordinary cut \(3\le h\le m-1\).
Allow \(y_2\in I_4\) and independent unselected targets
\(y_3,\ldots,y_h\in P\) at their actual heights. Use the
notation \(M_h,P_{h,b},d_j,D_j\) of the fixed-reference prefix
theorem. The prefix has the selected second weight when
\(\sigma_2=1\); explicitly its modulus is
\[
 \begin{split}
 \mathcal L_{h,N}={}&
 \left|U_{\alpha,N}(w_L,X_1)
                 \prod_{j=2}^hC_{\epsilon_j,N}(X_{j-1},X_j)\right|
 |d_N(X_1)^\alpha X_1^{-N\sigma_1}|\\
 &\quad\cdot|d_N(X_2)X_2^{-N\sigma_2}|
 \prod_{j=3}^{h-1}|d_N(X_j)|^{\epsilon_j}
 |d_N(X_h)|^{\epsilon_h/2}.
 \end{split}
 \tag{25}
\]
The first selected label is \(\sigma_1\in\{0,\alpha\}\);
\(\sigma_2\) has the physical path just specified. The factor at
the cut carries only one halfweight.

The first-pair tangent theorem proves, uniformly on \(I_4\),
\[
          U_{\alpha1}(k)<M_{12}+p\,d_2-1/20.
 \tag{26}
\]
Pay (24) on edge three, then use \(B_j+D_j\) on the remaining
ordinary edges. Original stationarity cancels all internal linear
terms. Thus, with one total tolerance,
\[
 \begin{split}
 \frac1N\log\mathcal L_{h,N}
 \le{}&M_h+\Re P_{h,b}d_h-\frac4{125}
                  +\sum_{j=3}^hD_j+\tau\\
 &-\kappa\left(d_2^2+2\sum_{j=3}^{h-1}d_j^2+d_h^2\right)
       +O_h(\log N/N),
 \end{split}
 \tag{27}
\]
since \(1/20-9/500=4/125\). This is unconditional with the
displayed excesses. If those excesses vanish, it gives more than the
common loss \(1/50\) after \(\tau<1/250\).

Together with the ending-three proof, (27) supplies the same
fixed-reference prefix estimate for all four first-pair types. At an
unpinned cut its surviving tangent cancels the opposite boundary
tangent exactly. The old safe corridor estimates still pay their
pinning costs; the small constant \(\kappa\) is not substituted
for their stronger curvature. Squaring the literal prefix makes all
Fourier weights integral, so the complex-neighborhood theorem also
applies, with \(k\) an independent compact height label. Fixed
ordinary-color derivatives retain the original cap disk.

The two row excesses have not been shown to vanish everywhere. Neither
this argument nor its complex extension supplies a lower bound or a
nonzero leading coefficient for the ordinary closure. Terminal factors,
later selected coordinates, and later departures from the plateau
still require their separate estimates. Stability under arbitrary
short partial fillings and the finite-exception theorem remain open.
