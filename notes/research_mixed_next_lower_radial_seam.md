# The complete unselected source on an explicit lower radial segment

Research deduction, 8 November 2026. The exact forced recurrence
keeps the reciprocal-factorial polynomial at arbitrarily small
exponential rate along every fixed positive radial segment inside
the unit disk. Symmetric finite products then give a complete
unselected-source estimate. In particular it pays the lower seam
through the explicit depth \(1/100\), with a fixed complex tube.
This covers lower endpoint arcs of those actual ordinary-next
cycles whose height is at least \(-1/100\).

The whole actual incoming height interval extends farther downward.
The theorem below does not pay its deeper endpoint arcs or the
lower middle complement. No numerical evaluation is used, and no
frozen source or contour is changed.

## 1. The complete Fourier weight on an inward radial segment

Use the original polynomial \(d_N\), of degree \(D=N-1\), with
\(d_N(r^j)=P_j^{-1}\), where \(r=e^{-2\pi i/N}\) and
\(P_j=(r;r)_j\). Its exact forced recurrence is
\[
 d_N(r^{-1}X)=(1-X)d_N(X)
                  +\frac{X}{N^2}\sum_{k=0}^{D}X^k .
 \tag{1}
\]
This is [the Fourier-weight continuation, equation (5)](research_mixed_fourier_weight_continuation.md).
The forcing in (1) will be retained.

**Lemma 1.** Fix any \(r_0\in(0,1)\). For every \(\tau>0\)
there is a fixed complex neighborhood \(\mathcal V_\tau\) of
the closed segment \([r_0,1]\) such that, at both level parities,
\[
             \sup_{Y\in\mathcal V_\tau}|d_N(Y)|
                       \le C_\tau N^B e^{N\tau}.
 \tag{2}
\]
Every fixed derivative satisfies the corresponding estimate on
smaller fixed neighborhoods.

To prove the lemma, use the logarithm near the positive segment
and write \(Y=e^{-2\pi iz}\). On the real segment,
\(z=-i\eta\), \(0\le\eta\le-\log r_0/(2\pi)\).
The original primitive satisfies
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}.
 \tag{3}
\]
It is continuous from \(0<\Re z<1\) to this closed segment,
including \(z=0\), and \(\Re g(-i\eta)=0\). These assertions
follow directly from the absolutely convergent dilogarithm series
on the closed unit disk and its continuous value at one; (3) is
the original branch fixed in Section 5 of the Fourier-weight
continuation. Thus the function
\[
             \max\{-\Re g(z),\,2\pi\max(\Im z,0)\}
 \tag{4}
\]
tends uniformly to zero on compact strips whose small positive
real coordinate tends to zero and whose imaginary interval tends
to the displayed nonpositive interval. At its possible small
positive-height end this uses only continuity at \(z=0\).

Choose a sufficiently small fixed \(\alpha>0\), then a sufficiently
small tube about \([r_0,1]\). For \(Y\) in the tube choose an integer
\(m\ge0\) so that
\[
           \alpha\le \Re z+m/N<\alpha+1/N .
 \tag{5}
\]
For large \(N\), the starting coordinates belong to a compact
subset of the original strip with real part in
\([\alpha,2\alpha]\). The full absolute Fourier-weight bound,
including its interpolation remainder, applies there. By (4),
and by making its arbitrary tolerance small, it gives
\[
                    |d_N(r^mY)|\le C N^B e^{2N\tau/3}.
 \tag{6}
\]
No relative factorial approximation is asserted on this strip.

All intermediate coordinates \(r^kY\), \(0\le k\le m\), lie
near the positive segment and have arguments tending uniformly
to zero with \(\alpha\) and the tube width. On the positive
segment itself, \(|1-Y|\le1-r_0<1\). Hence these choices may
also ensure one fixed \(q<1\) with
\[
 |1-r^kY|\le q,\qquad
 \log_+|Y|<\tau/3,\qquad 0\le k\le m .
 \tag{7}
\]
The full forcing in (1) is bounded at every step by
\[
 \left|\frac{r^kY}{N^2}\sum_{\nu=0}^{D}(r^kY)^\nu\right|
              \le \frac{\max(1,|Y|)^N}{N}
              \le N^{-1}e^{N\tau/3}.
 \tag{8}
\]
Iterating (1) from \(r^mY\) to \(Y\) and summing a geometric
majorant yields
\[
 |d_N(Y)|\le q^m|d_N(r^mY)|
                   +\frac{e^{N\tau/3}}{N(1-q)}.
 \tag{9}
\]
This proves (2), after increasing its constant to include the
finitely many smaller levels. It includes \(Y=1\) and all
physical support zeros; none of the forcing was canceled by
hand. Cauchy's formula on smaller tubes proves the derivative
assertion.

## 2. Reciprocal finite-product pairing

Let \(S_j=|P_j|\), \(p_j(Y)=(rY;r)_j\), and put
\[
                    a_j(R)=|p_j(R)|/S_j,\qquad 0<R\le1.
 \tag{10}
\]
For every individual root factor,
\[
              |1-Rr^k|=R\,|1-R^{-1}r^k|.
 \tag{11}
\]
Consequently
\[
                        a_j(R)=R^j a_j(R^{-1}).
 \tag{12}
\]
Apply the exact two bounds of
[upper radial seam, Lemma 1](research_mixed_next_upper_radial_seam.md)
at \(R^{-1}\ge1\). They give
\[
             a_j(R)\le R^{-D/4},\qquad
             R^{-j}a_j(R)\le R^{-D}.
 \tag{13}
\]
These are finite inequalities for every original row and both
parities. In particular (13) retains the actual incoming power
\(R^{-j}\) of the next conditional kernel. It does not assign
the selected factor \(R^{-N}\) to the unselected density.

## 3. A complete unselected-source rate

Keep the literal sources and the original normalization:
\[
 \begin{split}
 F_N(w,Y)&=N\operatorname{CT}_X
                [U_{0,N}(w,X)C_{1,N}(X,Y)],\\
 C_{\beta,N}(Y,Z)&=\sum_{j=0}^{D}
                \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}},\\
 \mathscr D_{0,\beta,N}(w,Y,Z)&=
                  F_N(w,Y)d_N(Y)C_{\beta,N}(Y,Z),
                       \qquad \beta=0,1 .
 \end{split}
 \tag{14}
\]
The unselected Fourier coefficient is
\(N[Y^0](F_Nd_NC_\beta)\). No final Gram or additional
root-average scalar is inserted.

Write \(R=e^{-c}\), \(0\le c\le c_0=-\log r_0\), and use
the notation \(b_0=101/125\), \(c_{\rm b}<13/40\), and
\(M_\beta(C)\) of the upper radial theorem. Its whole coherent
cap and complete disk-index bounds, combined with (13), give
\[
 \begin{split}
 |F_N(w,R)|&\le C_\tau N^B
       e^{N\{b_0+c_{\rm b}+7/15+c/4+\tau\}},\\
 \sup_{|Z|\le T}|C_{\beta,N}(R,Z)|
       &\le C_\tau N^B
             e^{N\{M_\beta(\log_+T)+c+\tau\}} .
 \end{split}
 \tag{15}
\]
For the first line, take the complete \(X\)-circle in (14);
the factor \(p_j(R)/P_j\) in its conditional sum costs at most
\(R^{-D/4}\). The remaining sum is precisely the whole
\(7/15\) disk estimate. For the second line, use the second
inequality in (13) before summing every next conditional row.
Both lines retain all upper rows and the coherent original
\(H_N\) inside \(U_0\).

Lemma 1 proves the complete source bound
\[
 \boxed{\quad
 \sup_{|Z|\le T}|\mathscr D_{0,\beta,N}(w,R,Z)|
 \le C_\tau N^B
 e^{N\{b_0+c_{\rm b}+7/15+M_\beta(\log_+T)+5c/4+\tau\}} .
 \quad}
 \tag{16}
\]
This estimate is valid along every fixed inward radial segment.
Its comparison with the geometric action will use a specific
segment below; (16) alone does not supply that comparison for
every \(c_0\).

There is also a fixed tube version with an arbitrarily small
additional rate. Indeed, for \(R\ge r_0\),
\[
 |1-Rr^k|^2=R|1-r^k|^2+(1-R)^2
                         \ge r_0|1-r^k|^2.
 \tag{17}
\]
If \(|Y-R|\le\varepsilon<r_0/2\), the exact finite product
argument of the seam theorem gives
\[
 |p_j(Y)|\le |p_j(R)|
             e^{N\Omega(\varepsilon/\sqrt{r_0})},\qquad
 \frac{R}{|Y|}\le(1-\varepsilon/r_0)^{-1}.
 \tag{18}
\]
Apply (18) to the prefix and next kernel, and apply Lemma 1
to the complete \(d_N\). Apart from the chosen tolerance in
that lemma, the added rate is at most
\[
       2\Omega(\varepsilon/\sqrt{r_0})
                       -\log(1-\varepsilon/r_0)\longrightarrow0.
 \tag{19}
\]
There is only one inverse-power loss in (19), from \(Y^{-j}\).
No selected \(Y^{-N}\) occurs in (14).

## 4. The explicit depth and the old filtered source

Take
\[
                   r_0=e^{-\pi/50},\qquad c_0=\pi/50.
 \tag{20}
\]
The rate (16) is identical to the upper radial rate, so the
fully proved action comparisons in equations (19)--(21) of
the upper radial theorem apply without alteration:
\[
 \begin{array}{c|c|c}
 \text{actual output}&\Re\mathcal P_\beta^+(-2,z_*)
       \text{ lower bound}&\text{unselected ceiling}\\ \hline
 \text{ordinary four}&109/50&43/20\\
 \text{terminal four}&56/25&43/20\\
 \text{ordinary three, }h_z\le0&419/200&201/100\\
 \text{ordinary three, }h_z\ge0&441/200&219/100\\
 \text{terminal three}&89/40&219/100 .
 \end{array}
 \tag{21}
\]
The smallest displayed reserve is \(3/200\). Choose the
source tolerances and fixed tube width inside this reserve.
The output sign split is imposed only at actual references;
the strict reserves and compactness permit fixed complex
neighborhoods without sign restrictions on perturbed parameters.

**Theorem.** On a fixed complex neighborhood of the entire
segment \(Y=e^{2\pi h}\), \(-1/100\le h\le0\), the full
unselected density (14) is exponentially smaller than its
actual next conditional action. It holds for both next types,
all ordinary and terminal reference families, both parities,
and all real ordinary colors, normalized against the complete
color. On smaller fixed complex complete-color and actual-output
neighborhoods, every fixed normalized mixed derivative obeys
\[
 \partial^\alpha\!
 \left[e^{-N\mathcal P_\beta^+(w,z)}
       \mathscr D_{0,\beta,N}(w,e^{-2\pi iy},e^{-2\pi iz})\right]
                         =O_\alpha(e^{-N/1000}).
 \tag{22}
\]
The proof uses the same fixed-neighborhood Cauchy argument as
the upper theorem. For real ordinary derivatives use Markov's
inequality after bounding the complete polynomial. All paths
are fixed before differentiation. The locally restored outgoing
halfweight, when present, retains its original nonzero factorial
packet and action shift; no division at independent output zeros
is asserted.

The statement also holds for the older \(11/12\) filtered prefix.
Its complete correction \(E_N^{\rm all}=F_N-F_N^{\rm mid}\)
has unit-disk rate \(77/50\) and degree at most \(D\).
For \(R\le1\), its radial contribution therefore has rate
\[
                  77/50+M_\beta(\log_+T)+c+\tau.
 \tag{23}
\]
This is below the same conservative ceiling in (21), since
\(77/50<4799/3000=b_0+13/40+7/15\) and \(c\le5c/4\).
For the fixed tube its polynomial degree adds at most
\(\log(1+\varepsilon)\); the other tube costs are (18) and
Lemma 1. They tend to zero. Exact subtraction proves (22)
for \(F_N^{\rm mid}\), without changing the filter or inferring
an estimate for a different correction.

## 5. Consequence for actual lower endpoint arcs

A sufficiently small fixed angular width \(s>0\) sends
\[
 \operatorname{dist}(\Re y,\mathbb Z)\le s,\qquad
                         -1/100\le\Im y\le0
 \tag{24}
\]
into the tube of the theorem. Thus, if an actual ordinary
reference has \(h_*=\Im y_*\ge-1/100\), the lower endpoint arcs
\([0,s]+ih_*\) and \([1-s,1]+ih_*\) are paid for the original
unselected density, and for the old filtered density.
The original incoming cycle measure remains \(+N\,dy\).

On the actual paired lower line, \(h_*<-1/1000\), the kernel
is
\[
 K_N(y)=
 \frac{N\mathscr D_{0,\beta,N}^{\rm mid}(w,Y,Z)}{1-Y^N},
       \qquad |1-Y^N|\ge1-e^{2\pi Nh_*}\ge\frac12
 \tag{25}
\]
for all sufficiently large \(N\). Hence the same endpoint
arcs in that paired representation are paid, with polynomial
costs and a smaller fixed gap. This assertion is limited to
the ordinary family for which the paired contour was proved.
The terminal source bound in (22) does not promote that contour
assembly to terminal references.

The full permitted interval \(h_*\in(-.102,-.001)\) is larger
than (24). Lemma 1 controls \(d_N\) throughout that full inward
radial segment, and (16) remains a valid complete-source upper
bound there, but its \(5c/4\) debit has not been absorbed by
the actual action over the deeper part. No deeper lower
endpoint, full lower complement, or whole transfer is claimed.
