# The final coefficient and the two boundary values of the cumulative sum

Research deduction, 7 November 2026. The last coefficient of the
first-node cardinal correction is a derivative of the original
interpolation polynomial. This gives a second boundary estimate for
the cumulative sum. In particular, its possible accumulated constant
does not persist at the largest exponential rate of the interior
coefficients.

All identities below refer to the original finite sum. The bounds
are analytic consequences of earlier factorial and column estimates;
no numerical evaluation is used.

## 1. An exact endpoint value

For an integer \(N\ge2\), put
\[
 D=N-1,\qquad r=e^{-2\pi i/N},\qquad
 P_j=\prod_{\nu=1}^j(1-r^\nu),\qquad
 p_j(Y)=\prod_{\nu=1}^j(1-r^\nu Y).
 \tag{1}
\]
The polynomial \(d_N\), of degree at most \(D\), is specified by
\[
                         d_N(r^b)=P_b^{-1},\qquad 0\le b<N.
 \tag{2}
\]
In particular \(d_N(1)=1\). Let
\[
 K_1(Y)=\frac{d_N(Y)-1}{Y-1},\qquad
 A_j(1)=\operatorname{CT}_Y[K_1(Y)Y^{-j}p_j(Y)],\qquad
 a_j=\frac{A_j(1)}{P_j}.
 \tag{3}
\]
The quotient in (3) is a polynomial of degree at most \(N-2\);
\(\operatorname{CT}_Y\) means the constant Laurent coefficient.
These are the exact coefficients in
[the coherent-response theorem, equations (3) and (13)](research_mixed_next_low_cardinal_coherent_response.md).

**Proposition 1.** At every integer level,
\[
                         a_D=\frac{d_N'(1)}{N}.
 \tag{4}
\]

*Proof.* Factoring \(1-Y^N\) over all \(N\)-th roots gives
\[
                    p_D(Y)=\frac{1-Y^N}{1-Y}
                              =\sum_{k=0}^{D}Y^k,\qquad P_D=N.
 \tag{5}
\]
If \(K_1(Y)=\sum_{m=0}^{D-1}k_mY^m\), each coefficient \(k_m\)
contributes once to the constant coefficient of
\(K_1(Y)Y^{-D}p_D(Y)\), at \(k=D-m\). Thus
\[
               A_D(1)=\sum_{m=0}^{D-1}k_m=K_1(1)=d_N'(1).
 \tag{6}
\]
Division by \(P_D=N\) proves (4). This includes \(N=2\).
\(\square\)

Write
\[
 J(t)=\int_0^t\log(2\sin\pi s)\,ds,\qquad
                         c_{\mathrm b}=-2J(1/6).
 \tag{7}
\]
The whole-disk interpolation estimate in
[the complete-sector bound, equations (17)--(18)](research_mixed_next_high_cardinal_whole_sectors.md)
states
\[
                 \sup_{|Y|\le1}|d_N(Y)|
                          \le C N^C e^{Nc_{\mathrm b}/2}.
 \tag{8}
\]
The constant \(C\) may change between inequalities. This estimate
includes both end indices. Directly, its input is the uniform
sine-factorial estimate and the cardinal representation
\[
 d_N(Y)=\sum_{b=0}^{D}P_b^{-1}\mathfrak l_b(Y),\qquad
 \mathfrak l_b(Y)=\frac1N\sum_{\nu=0}^{D}(Yr^{-b})^\nu,
                  \qquad |\mathfrak l_b(Y)|\le1\quad(|Y|\le1).
 \tag{9}
\]
If \(d_N(Y)=\sum_k d_kY^k\), Cauchy's coefficient formula gives
\(|d_k|\le\sup_{|Y|=1}|d_N(Y)|\). Hence (4) implies
\[
 |a_D|\le\frac1N\sum_{k=1}^{D}k|d_k|
                   \le C N^C e^{Nc_{\mathrm b}/2}.
 \tag{10}
\]
The chord inequality \(2\sin\pi s>6s\) on \(0<s<1/6\) yields
\[
                          0<c_{\mathrm b}/2<1/6.
 \tag{11}
\]
Thus (10) is substantially smaller than an estimate obtained by
summing the absolute values of all increments near their interior
maximum.

## 2. Comparison with the original column profile

Keep the branches of the
[original Fourier-column theorem](research_three_crossing_next_crossing_fourier.md):
\[
 \begin{split}
 X(t)&=e^{-2\pi it},\\
 \lambda(t)&=\frac{3-2X(t)+\sqrt{4/X(t)-3}}2,\\
 I(t)&=\int_0^t\log\lambda(s)\,ds,\qquad
 A(t)=\Re I(t)-2J(t).
 \end{split}
 \tag{12}
\]
The square root and logarithm continue from \(1\) and \(0\),
respectively, at \(t=0\). The profile \(A\) has a unique
nondegenerate maximum \(x_*\in(1/3,1/2)\), increases before it,
and decreases after it. It has a continuous limit at \(1/2\).

The following elementary bounds compare the true endpoint (10)
with the entire decreasing part of this profile:
\[
                  A(x_*)>\frac{20}{63},\qquad
                  A(1/2)>\frac{\log3}{6}>\frac16.
 \tag{13}
\]

To prove them, set \(c=\cos(2\pi t)\). For \(0\le c\le1\),
\[
 \left(\Re\sqrt{4e^{2\pi it}-3}\right)^2
       =\frac{\sqrt{25-24c}+4c-3}{2}\ge1.
 \tag{14}
\]
Indeed \(5-4c>0\), and
\[
                  (25-24c)-(5-4c)^2=16c(1-c)\ge0.
 \tag{15}
\]
For \(-1\le c\le0\), the selected square root has nonnegative
real part. Consequently
\[
 |\lambda(t)|\ge\Re\lambda(t)\ge
 \begin{cases}
 2-c,&0\le c\le1,\\
 (3-2c)/2,&-1\le c\le0.
 \end{cases}
 \tag{16}
\]
In particular \(|\lambda|\ge1\) on \([0,1/2]\), so
\[
 A(x_*)\ge A(1/6)\ge-2J(1/6)
 >\frac13\{1-\log(\pi/3)\}>\frac{20}{63}.
 \tag{17}
\]
Here \(\sin\pi s<\pi s\), \(\pi<22/7\), and
\(\log(22/21)<1/21\) prove the last two inequalities.

Equation (16) also gives \(|\lambda|\ge3/2\) on
\([1/6,1/3]\), and \(|\lambda|\ge2\) on \([1/3,1/2]\).
The inequalities are strict on subintervals of positive length.
Since \(J(1/2)=0\),
\[
 A(1/2)=\int_0^{1/2}\log|\lambda(t)|\,dt
       >\frac16\log(3/2)+\frac16\log2=\frac{\log3}{6}.
 \tag{18}
\]
Finally \(e<3\), for example by bounding the terms of its
exponential series from \(1/2!\) onward by a geometric series,
proves \(\log3>1\).

## 3. Exponential control from both boundaries

The exact cumulative recurrence is
\[
 \begin{split}
 a_0&=1-\frac{\gamma_0}{\kappa^2N^2},\\
 a_j-a_{j-1}
   &=-\frac1{\kappa^2N^2}
      \left(v_j+\frac{r^j}{1-r^j}v_{j-1}\right),\qquad 1\le j<N,
 \end{split}
 \tag{19}
\]
where
\[
 q=e^{\pi i/N},\quad \kappa=q^{D^2/2},\quad
 \gamma=MJM^3e_0,\quad v_j=(-q)^{-j}\gamma_j.
 \tag{20}
\]
The matrices \(M,J\) are the original crossing and index reversal,
and \(e_0\) is the first coordinate vector. Thus
\(|v_j|=|\gamma_j|\) and \(|\kappa|=1\).
The initial column normalization gives
\(|\gamma_0|=N^{3/2}(1+O(N^{-1}))\).

**Theorem 2.** For every neighborhood \(U\) of \(x_*\) whose
closure lies in \((0,1/2)\), there is \(\eta_U>0\) such that
\[
             \max_{j/N\notin U}|a_j|
                 \le C_U N^{C_U}e^{N\{A(x_*)-\eta_U\}}.
 \tag{21}
\]

*Proof.* Choose an interval about \(x_*\) with closure inside
\(U\). The original column theorem, Lemma 2, gives a strict
exponential gap for all \(v_j\) outside a smaller such interval.
On the left, sum (19) forward from its actual \(a_0\).
On the right, sum it backward from its actual \(a_D\) in (4).
Every column index in the respective sum remains on the same
side of the smaller interval. The bound
\[
                    |1-r^j|^{-1}\le N/4,\qquad 1\le j<N,
 \tag{22}
\]
and the at most \(N\) increments cost only polynomial factors.
The left boundary has polynomial size. The right boundary has
rate \(c_{\mathrm b}/2<1/6<A(x_*)\), by (10)--(13).
Taking a smaller common positive gap proves (21).
\(\square\)

A more precise right boundary estimate is useful when extending
a local asymptotic past the maximum.

**Proposition 3.** For each fixed \(b\in(x_*,1/2)\),
\[
              \max_{j/N\ge b}|a_j|
                        \le C_bN^{C_b}e^{NA(b)}.
 \tag{23}
\]

*Proof.* First the original column estimates imply
\[
              \max_{j/N\ge b}|v_j|
                        \le C_bN^{C_b}e^{NA(b)}.
 \tag{24}
\]
Here is the required one-sided version of their argument. Up to
\(1/2-\varepsilon\), the compact column formula and the strict
decrease of \(A\) bound the rate by \(A(b)\). To the right of
\(1/2+\varepsilon\), the original right-end formula bounds the
rate by \(B(1/2)=A(1/2)<A(b)\), where \(B=\Re I-J\).
In the intervening band the exact transfer matrices have norm
at most a fixed \(K\). Their rate is at most
\[
                   A(1/2-\varepsilon)+2\varepsilon\log K.
 \tag{25}
\]
As \(\varepsilon\) decreases to zero, this tends to \(A(1/2)\).
Choose a sufficiently small fixed \(\varepsilon\) to make (25)
strictly smaller than \(A(b)\), with \(b<1/2-\varepsilon\).
This proves (24), including polynomial factors from the original
endpoint estimates.

Now sum (19) backward from \(D\). For \(j/N\ge b\), all terms
involve \(v_k,v_{k-1}\) with \(k-1\ge j\). Apply (22)--(24).
The endpoint rate \(c_{\mathrm b}/2\) is smaller than
\(A(1/2)<A(b)\), so (10) is absorbed by the same bound.
This proves (23). \(\square\)

## 4. Consequence for the remaining Fourier argument

The earlier
[peak-window theorem](research_mixed_next_low_cardinal_peak_window.md)
kept a possible constant of size \(O(N^{-2}e^{NA(x_*)})\)
throughout the late indices. Its estimate remains valid.
The actual endpoint identity now proves the stronger exponential
tail bound (21). A proof of a sharper full-vector asymptotic can
therefore use both boundaries, instead of carrying that crude
constant through a macroscopic set of indices.

This result concerns the initialized coefficient vector. It does
not estimate its signed outgoing sum
\(\sum_j a_jp_j(Z)/P_j^{1+\beta}\), and it does not establish
noncancellation in the completed knot invariant.
