# The full high physical tail in one exact height-sign class

Research deduction, 10 November 2026. If the first target height is
nonnegative and the second nonpositive, every physical-row rate above
one half is bounded by the half-row rate, for all real target angles
strictly between zero and one half. This removes the plateau restriction
from the corresponding reflected-row theorem. The sign condition
cancels the original reflected drift exactly; it is not a small-height
assumption. No numerical evaluation or source replay is used.

## 1. Original rows, allocations and reflected rate

Let \(a=x+ic\), \(b=z+id\), and assume
\[
             0<x,z<1/2,\qquad c\ge0,\quad d\le0 .
\tag{1}
\]
For \(r_N=e^{-2\pi i/N}\), retain the literal ordinary rows
\[
 R_{j,N}(a,b)
 =X^{-j}\frac{(r_NX;r_N)_j(r_NY;r_N)_j}
                  {(r_N;r_N)_j^{\,2+\epsilon}},
 \qquad X=e^{-2\pi ia},\quad Y=e^{-2\pi ib},\quad
 \epsilon\in\{0,1\}.
\tag{2}
\]
Their full absolute rate is
\[
\begin{split}
 E_\epsilon(s;a,b)
 ={}&\int_0^s\log|1-e^{-2\pi i(a+t)}|\,dt
   +\int_0^s\log|1-e^{-2\pi i(b+t)}|\,dt\\
 &-(2+\epsilon)J(s)-2\pi cs,\qquad 0\le s\le1 .
\end{split}\tag{3}
\]
The first chirp, wrapped rows and integrable logarithmic zeros remain
in (2)--(3). Original Fourier half allocations are independent of
\(s\), so every row-difference assertion below preserves them.

Use precisely the radial primitive in
[the original right-tail reflection proof](research_mixed_right_tail_reflection.md):
\[
 G_H(t)=\Re g(t-iH),\quad H\ge0,\qquad
 f_H(t)=G_H'(t)=\log|1-e^{-2\pi H-2\pi it}|.
\tag{4}
\]
Its original normalization makes \(G_H\) odd and one-periodic, and
\[
                  J(t)\le G_H(t)\le0\qquad(0\le t\le1/2).
\tag{5}
\]
The exact reflected drift is
\(\lambda=2\pi\{(-c)_++d_+\}\), which is zero under (1).
Thus with \(v=1-s\),
\[
\begin{split}
 E_\epsilon(1-v)-E_\epsilon(1)
 ={}&G_c(x-v)-G_c(x)
       +G_{-d}(z-v)-G_{-d}(z)+(2+\epsilon)J(v).
\end{split}\tag{6}
\]
In particular \(E_\epsilon(1)=0\). No independently variable drift
has replaced the radius-height correlation.

## 2. A legwise inequality on the entire angular interval

**Lemma 1.** For every finite \(H\ge0\), \(0<x<1/2\), and
\(0\le v\le1/2\),
\[
                    G_H(x-v)+J(v)+G_H(1/2-x)\le0 .
\tag{7}
\]
Equality occurs at \(v=1/2\); the inequality is strict for
\(0\le v<1/2\).

*Proof.* If \(v\le x\), all three terms in (7) are nonpositive
by (5); its last term is strictly negative.

Suppose \(x<v\le1/6\). Write \(\rho=e^{-2\pi H}\in(0,1]\).
For \(0\le t\le1/6\),
\[
 |1-\rho e^{-2\pi it}|^2
       \le1+\rho^2-\rho\le1 .
\tag{8}
\]
Hence \(f_H(t)\le0\), including its integrable endpoint at
\(H=0,t=0\). It follows that
\(G_H(v-x)\ge G_H(v)\ge J(v)\). By oddness, the sum of the
first two terms in (7) is nonpositive, and its last term is
strictly negative.

It remains to consider \(v>\max(x,1/6)\). Put
\[
       K(v)=-G_H(v-x)+J(v)+G_H(1/2-x).
\]
For \(t=v-x\in[0,v)\), convexity of a norm on the radial segment gives
\[
 |1-\rho e^{-2\pi it}|
 \le\max\{1,2\sin\pi t\}<2\sin\pi v .
\tag{9}
\]
Here \(v>1/6\) and \(v\le1/2\). Consequently
\(K'(v)=J'(v)-f_H(v-x)>0\) wherever the derivative is finite.
The integrable zero, if present at an initial endpoint, is handled
by integration. Since \(K(1/2)=0\), (7) follows strictly at every
smaller \(v\) in this last interval. The preceding two cases cover
its boundaries. This proves the lemma. \(\square\)

**Theorem 2.** Under (1), for either own flag,
\[
 \max_{1/2\le s\le1}E_\epsilon(s;a,b)=E_\epsilon(1/2;a,b).
\tag{10}
\]
The inequality is strict for \(s>1/2\).

*Proof.* Subtract the half-row instance of (6) from its general
instance. The result is
\[
\begin{split}
 E_\epsilon(1-v)-E_\epsilon(1/2)
 ={}&[G_c(x-v)+J(v)+G_c(1/2-x)]\\
 &+[G_{-d}(z-v)+J(v)+G_{-d}(1/2-z)]
                                      +\epsilon J(v).
\end{split}\tag{11}
\]
Each bracket is nonpositive by Lemma 1, strictly negative for
\(v<1/2\); and \(J(v)\le0\). This proves (10), retaining the
own-type-four factorial. \(\square\)

## 3. The complete finite upper block

**Corollary 3.** On every compact parameter subset of (1), including
zero heights, for every \(\tau>0\) and both level parities,
\[
 \sum_{j=\lceil N/2\rceil}^{N-1}|R_{j,N}(a,b)|
 \le C_\tau N^{A_\tau}
                  e^{N\{E_\epsilon(1/2;a,b)+\tau\}} .
\tag{12}
\]

*Proof.* The zero-safe finite-product argument from
[the original contour-allowance proof](research_mixed_conditional_contour_allowance.md),
Section 2, gives the rate (3) uniformly on every physical index,
including the true last rows. Its row portion does not use a
critical-point or retained-contour hypothesis. To spell out its
extension to the present angles, replace each numerator logarithm by
\(\log(|1-e^{-2\pi i(a+t)}|+\delta)\), and likewise for \(b\).
For fixed \(\delta>0\), the Riemann-sum error is bounded uniformly
on the compact parameter set. The integral error tends uniformly
to zero as \(\delta\downarrow0\), since the only possible real
zeros are simple and their local error is
\(O(\delta(1+|\log\delta|))\). The denominator sine factorial
has its original uniform \(O(\log N)\) endpoint error for \(j<N\).
The chirp contributes exactly \(-2\pi c j/N\) to the rate.
Thus every row is bounded by a polynomial times
\(\exp N(E_\epsilon(j/N)+\tau/2)\). Use (10) and sum at most
\(N\) rows. No zero is divided out and no physical row is omitted.
The proof is independent of parity. \(\square\)

The ceiling in (12) is a continuous half-index rate; it is not an
assertion that \(N/2\) is an integer or a comparison to a possibly
zero finite half-row value. The original Fourier factors may be
multiplied exactly on both sides. When their unselected estimate
is used, each type-four target still requires its actual negative
height. No phase or scalar is changed by this multiplication.

## 4. Application and exact limits

For actual early first-boundary targets, take \(x\in[.1,.22]\),
\(z\in[.22,.45]\), with unchanged original heights \(c,d\).
If \(c\ge0,d\le0\), the first type must be three. Corollary 3
reduces its complete joint cap--high-row block to the joint
cap--half-row rate. Use the separately frozen
[joint low- and half-row transport proof](research_mixed_early_joint_low_tail.md),
with its original reference, ordinary polynomial
\(U_{0,N}(w,X)\), reciprocal-factorial interpolation \(d_N\), and
allocated plane \(\Gamma(z)\). Its equation (23) bounds every
complete-cap profile plus the continuous allocated half-row rate
by \(\Gamma(z)-1/2000\). It retains the true cap ends and the
positive-height upper-row allowance.

Consequently, for every \(\tau>0\), both parities satisfy
\[
 |U_{0,N}(w,X)|\,|d_N(Y)|^{\epsilon/2}
 \sum_{j=\lceil N/2\rceil}^{N-1}|R_{j,N}(a,b)|
 \le C_\tau N^{A_\tau}
             \exp N\{\Gamma(z)-1/2000+\tau\}.
\tag{13}
\]
The ordinary color \(w\) may range over a sufficiently small fixed
neighborhood of \(-2\); every fixed derivative in that color obeys
the same rate on a smaller neighborhood. Indeed combine (12) with
the complete-cap profile comparison in the cited equation (23),
then use its all-real-color bounds, degree continuation and Cauchy
argument. This is a comparison of continuous rates and retained
profiles, not a division by, or a comparison to, any literal
finite half-row value. It introduces neither a pointwise cap
asymptotic nor a new normalization.

Other height signs retain the nonnegative drift
\(2\pi\{(-c)_++d_+\}\), which is generally nonzero. It cannot be
erased from (6); the present theorem makes no endpoint-only
claim for those classes. It also does not control rows between
the old cut \(49/100\) and one half, the central ordinary contour,
or changing-height joins. There is no signed lower-bound,
whole-word, or short-partial-filling assertion.

## Source bindings

| Source | SHA-256 |
|---|---|
| research_mixed_right_tail_reflection.md | e3928f2d9549159f6955c654b202dc87198137f4cfdb80f85151af567a976ce1 |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |

All three statements and the directly used proofs were read. The
deduction is written analysis only; no mathematical evaluation,
source replay, import, compilation or test was performed.
