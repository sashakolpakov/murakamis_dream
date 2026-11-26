# Exact simultaneous high-row truncation in the filtered transfer

Private research deduction, 8 November 2026. The old low-node
deletion permits exact truncation of both conditional row indices
before the complete filtered transfer is estimated. This keeps the
same filter and all original normalizations. It is a finite algebra
identity; it does not bound a remaining contour or spend an
unspecified endpoint margin.

## 1. The original prefix and the old filter

Put
\[
D=N-1,\quad r=e^{-2\pi i/N},\quad
P_j=(r;r)_j,\quad p_j(V)=(rV;r)_j,
\qquad B_b=r^b.
\tag{1}
\]
Use exactly the conditional kernels
\[
C_{\gamma,N}(X,Y)=\sum_{j=0}^{D}
          \frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\gamma}},
\qquad\gamma=0,1,
\tag{2}
\]
and the complete cap \(U_{0,N}(w,X)\), which is a polynomial
of degree at most \(D\) in \(X\). The full first prefix is
\[
F_N(w,Y)=N\operatorname{CT}_X[U_{0,N}(w,X)C_{1,N}(X,Y)].
\tag{3}
\]
The integrand in (3) has incoming band \([-D,D]\), so (3)
equals its original physical sum over all \(X=B_a\).

Let the fixed old low width be \(\delta\), with the choice and
source estimates of [the low physical-interval theorem](research_mixed_next_low_physical_interval.md).
Write
\[
L_N=\lfloor\delta N\rfloor,\qquad
A_N=\lceil23N/24\rceil,\qquad B_N=\lceil11N/12\rceil,
\qquad I_N=\{L_N<b<B_N\}.
\tag{4}
\]
In this note \(B_N\) is an integer cut, whereas \(B_b\) in (1)
is a physical root. The first-coordinate deletion gives
\[
F_N^{<}(w,Y)=\sum_{a=0}^{A_N-1}
       U_{0,N}(w,B_a)C_{1,N}(B_a,Y).
\tag{5}
\]
Let \(\Pi_{I_N}\) be the original degree-\(D\) cardinal
projection onto the values at \(b\in I_N\), and set
\[
F_N^{\rm mid}=\Pi_{I_N}F_N^{<}.
\tag{6}
\]
This is exactly the old filtered polynomial; no low width,
high cut or first-coordinate deletion is changed.

## 2. Truncate the first conditional row before projecting

For each fixed first row \(j\), (5) has the form
\[
F_N^{<,(j)}(w,Y)=c_{j,N}(w)p_j(Y),\qquad
c_{j,N}(w)=\frac1{P_j^3}
  \sum_{a=0}^{A_N-1}U_{0,N}(w,B_a)B_a^{-j}p_j(B_a).
\tag{7}
\]
Every coefficient and every original phase in this formula is
retained. At physical nodes the exact support is
\[
p_j(B_b)=0\quad\hbox{if }b+j\ge N,
\qquad 0\le b,j<N.
\tag{8}
\]
Indeed the product contains its factor \(1-r^N\).
Set
\[
                         J_N=D-L_N=N-1-L_N.
\tag{9}
\]
If \(j\ge J_N\), any nonzero physical value of (7) has
\(b\le D-j\le L_N\), a deleted low node. Thus
\[
\Pi_{I_N}F_N^{<,(j)}=0\quad(j\ge J_N),\qquad
F_N^{\rm mid}=\Pi_{I_N}
       \sum_{j=0}^{J_N-1}F_N^{<,(j)}.
\tag{10}
\]
The equality is an equality of polynomials, since both sides
have degree at most \(D\) and agree at every physical node.
It also holds with the complete first prefix (3), if the
first-coordinate deletion is omitted on both sides.

As an exact endpoint check, \(P_D=N\) and
\[
p_D(X)=\frac{1-X^N}{1-X}=\sum_{k=0}^{D}X^k.
\]
Consequently the full first row \(j=D\) contributes
\[
F_N^{(D)}(w,Y)=\frac{U_{0,N}(w,1)}{N^2}p_D(Y)
             =\frac{U_{0,N}(w,1)}{N}\mathfrak l_0(Y).
\tag{11}
\]
Here \(\mathfrak l_0=N^{-1}\sum_{k=0}^{D}Y^k\).
The constant term in (3) sums all coefficients of \(U_0\),
which is its value at one. The same formula holds in (5),
because only \(a=0\) survives this row and that index is
retained. Also, directly from the original cap,
\[
U_{0,N}(w,1)=\sum_{e=0}^{D}H_N(w,r^{-e}).
\tag{12}
\]
Thus its all-real-color upper rate is the coherent constant
\(b_0=101/125\), by [the complete seam source, equation (10)](research_mixed_next_complete_source_seam_collar.md).
This last bound is not needed for the exact annihilation (10).

## 3. Truncate the next row in the complete paired observation

Define
\[
C_{\beta,N}^{<J_N}(Y,Z)=\sum_{k=0}^{J_N-1}
                \frac{Y^{-k}p_k(Y)p_k(Z)}{P_k^{2+\beta}}.
\tag{13}
\]
At every retained physical node \(b\in I_N\), equations
(8)--(9) give
\(C_{\beta,N}(B_b,Z)=C_{\beta,N}^{<J_N}(B_b,Z)\).
At every other node \(F_N^{\rm mid}(B_b)=0\). Therefore
\[
\boxed{\quad
\sum_{b=0}^{D}\frac{F_N^{\rm mid}(w,B_b)}{P_b}
                  C_{\beta,N}(B_b,Z)
=\sum_{b=0}^{D}\frac{F_N^{\rm mid}(w,B_b)}{P_b}
                  C_{\beta,N}^{<J_N}(B_b,Z).
\quad}
\tag{14}
\]
This is the original complete conditional transfer, for either
next type and every complex output \(Z\).

Keep the complete reciprocal-factorial polynomial
\(d_N(B_b)=P_b^{-1}\). The exact band of the right-hand
product in (14) is contained in
\([-J_N+1,2D]\). Its only possible multiples of \(N\)
are zero and \(N\). Hence the original coefficient formula is
unchanged:
\[
\sum_b\frac{F_N^{\rm mid}(w,B_b)}{P_b}
                  C_{\beta,N}^{<J_N}(B_b,Z)
=N[Y^0](F_N^{\rm mid}d_N C_{\beta,N}^{<J_N})
 +N[Y^N](F_N^{\rm mid}d_N C_{\beta,N}^{<J_N}).
\tag{15}
\]
There is no extra root-average factor and no replacement of
\(d_N\) by an unforced factorial interpolant. At a physical
output, the same final scalar
\(\kappa_N^{4+\beta}N^{1+\beta}P_k^{1-\beta}\)
from [the exact attachment identity](research_mixed_three_four_next_conditional_attachment.md)
restores the original output row.

## 4. Exact contour scope

Let
\[
\mathcal E_N(Y,Z)=F_N^{\rm mid}(w,Y)d_N(Y)
              \{C_{\beta,N}(Y,Z)-C_{\beta,N}^{<J_N}(Y,Z)\}.
\tag{16}
\]
It vanishes at every physical node. Its two complete Fourier
observations satisfy exactly
\[
                 N[Y^0]\mathcal E_N+N[Y^N]\mathcal E_N=0.
\tag{17}
\]
Equivalently, its original full unselected and selected
coefficient cycles cancel in their sum, with their original
orientations and factors \(+N\). Equation (17) does not
assert that either coefficient is zero separately, or that an
open subarc or a boundary current is zero. In a paired
meromorphic contour the apparent physical poles of this
difference are removable; its complete closed integral is zero.
All exact formulas hold at both parities and commute with
fixed derivatives of the outside parameters.

The first truncation (10) is performed inside the original
cardinal projection and is stronger: that projected polynomial
tail itself is zero. It does not discard an unprojected
first-incoming contour piece. The next truncation (14)--(17)
uses the complete paired observation and cannot be applied
independently to its lower or upper open pieces.

Thus the fixed old filter permits simultaneous replacement of
both conditional row ranges by \(0\le j<J_N\), while keeping
every other original source factor. The surviving upper rows
can still have rates near the old last-row envelope. The
choice of \(\delta\) in the low-node theorem has no stated
quantitative width here, and no useful exponential debit is
deduced merely from removing these rows. The remaining
source comparison and complementary contours are unchanged
obligations.
