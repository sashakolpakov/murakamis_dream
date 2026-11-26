# The final index block of the complete first \(44\) sum

Private written proof, 11 November 2026. At an original physical
node, a conditional index close to \(N-1\) forces the preceding
index to be close to zero. Keeping this exact vanishing before
taking absolute values bounds a whole final block uniformly over
the second period. The rest of the first conditional sum is not
estimated here.

## 1. Source and statement

Use the actual source and reference of the
[complete first-sum seam theorem](research_mixed_complete44_second_period_seam_collar.md).
The word has length \(m\ge4\), with first three flags
\((1,1,\beta)\), \(\beta=0,1\). Set
\[
 r=e^{-2\pi i/N},\quad D=N-1,\quad
 P_j=(r;r)_j,\quad S_j=|P_j|,\quad p_j(V)=(rV;r)_j,
\]
\[
 U_N(w,X)=\sum_{i=0}^{D}\frac{H_N(w,r^{-i})p_i(X)}{P_i^2},
 \qquad C_{\beta,N}(Y,Z)=
 \sum_{j=0}^{D}\frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}}.
 \tag{1}
\]
The endpoint coefficient \(H_N\) remains its complete signed sum.
The exact first polynomial is the unnormalized physical sum
\[
 f_{44,N}(w,Y)=
 \sum_{a=0}^{D}\frac{U_N(w,r^a)}{P_a}C_{1,N}(r^a,Y).
 \tag{2}
\]
Both first Fourier terms occur in its coefficient-integral
representation. For fixed \(0<\delta<1/6\), define
\[
 T_{\delta,N}(w,Y)=
 \sum_{a=0}^{D}\frac{U_N(w,r^a)}{P_a}
 \sum_{j=\lceil(1-\delta)N\rceil}^{D}
       \frac{r^{-aj}p_j(r^a)p_j(Y)}{P_j^3}.
 \tag{3}
\]
An empty inner sum is zero. This finite decomposition precedes any
contour change.

Put \(y=q+ih\), \(Y=e^{-2\pi iy}\), and retain
\[
 {\cal T}_{\sigma,\beta,N}
       =T_{\delta,N}(w,Y)d_N(Y)Y^{-\sigma N}C_{\beta,N}(Y,Z).
 \tag{4}
\]
Here \(d_N\) is the original degree-\(D\) interpolation polynomial,
with \(d_N(r^a)=P_a^{-1}\), including its forcing. Carry
\[
 D_{\beta,N}(Z)=
 \begin{cases}1,&\beta=0,\\ |d_N(Z)|^{1/2},&\beta=1.\end{cases}
 \tag{5}
\]
The third coordinate is \(z=v+ic_3\), \(v\in P=[11/50,9/20]\),
at its actual reference height:
\[
 -13/200\le c_3\le17/250\quad(\beta=0),\qquad
 -51/500\le c_3\le-1/1000\quad(\beta=1).
 \tag{6}
\]
At \(m=4\) this factor is still ordinary with its original following
incidence. Let \(\Lambda_{123}(z)\) be the seam theorem's original
three-factor affine action, with the same constants and marking.

**Theorem.** There is a fixed sufficiently small \(\delta>0\) such
that, at both parities and all sufficiently large \(N\),
\[
 |{\cal T}_{\sigma,\beta,N}(w,Y,Z)|D_{\beta,N}(Z)
 \le C N^B e^{N\{\Lambda_{123}(z)-1/50\}}.
 \tag{7}
\]
This holds for all \(q\in[0,1]\), all real colors \(w\in[-2,2]\),
and a sufficiently small fixed color disk about \(-2\), in either
of the two regimes
\[
 \sigma=0,\quad -51/500\le h\le0,
 \qquad\hbox{or}\qquad
 \sigma=1,\quad 0\le h\le1/100.
 \tag{8}
\]
Fixed color derivatives satisfy the same rate on a smaller disk.
Integration over any fixed finite-length portion of these contours,
with its original measure \(N\,dy\), has only polynomial cost.

## 2. Exact support and the first coefficient

At a physical node,
\[
 p_j(r^a)=
 \begin{cases}P_{a+j}/P_a,&a+j<N,\\0,&a+j\ge N.\end{cases}
 \tag{9}
\]
Thus a surviving term in (3) has \(0\le a\le D-j<\delta N\).
The literal last index \(j=D\) contributes exactly
\[
                         U_N(w,1)p_D(Y)/P_D^2.
 \tag{10}
\]
We estimate the whole final block, not only this one row.

Write
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\quad
 c_{\rm b}=-2J(1/6)<13/40,\quad b_1=433/500 .
 \tag{11}
\]
The seam theorem's complete coherent coefficient norm gives
\[
 \sum_{i<N}\frac{|H_N(w,r^{-i})|}{S_i}
       \le C_\tau N^{B_\tau}e^{N(b_1+\tau)}.
 \tag{12}
\]
Its real-color and fixed complex-color versions include all rows.
For \(a+i<N\), bounding \(a\) consecutive factors by two gives
\[
 \frac{|p_i(r^a)|}{S_i}
       =\frac{S_{a+i}}{S_aS_i}\le\frac{2^a}{S_a};
 \tag{13}
\]
the other terms vanish. The full \(U_N\) therefore satisfies
\[
 |U_N(w,r^a)|\le C_\tau N^{B_\tau}
 e^{N\{b_1+\omega(\delta)+\tau\}},\quad
 \omega(\delta)=\delta\log2-J(\delta)\longrightarrow0 .
 \tag{14}
\]
Here we used \(\log S_k=NJ(k/N)+O(\log N)\), uniformly through
both endpoints, and the decrease of \(J\) on \([0,1/6]\).

After (9), the remaining physical coefficient in (3) has modulus
\[
                          \frac{S_{a+j}}{S_a^2S_j^3}.
 \tag{15}
\]
Put \(x=a/N\), \(t=j/N\). We have \(t>5/6\) and \(x\le1-t<1/6\).
The decrease of \(J\) on \([5/6,1]\) and on \([0,1/6]\) gives
\[
 J(x+t)\le J(t),\quad J(x)\ge J(1-t)=-J(t),\quad
                  J(x+t)-2J(x)-3J(t)\le0.
 \tag{16}
\]
Thus (15) is uniformly polynomial in \(N\).

The all-index numerator estimate in
[the boundary-strip proof, Section 2](research_mixed_boundary_strip_bounds.md)
is
\[
 |p_j(Y)|\le N^A e^{N\{L(t)+t\log_+|Y|\}},
 \qquad L(t)=-2J((1-t)/2).
 \tag{17}
\]
It includes every numerator zero. When \(t\ge1-\delta\),
\(L(t)\le\nu(\delta):=-2J(\delta/2)\to0\).
Summing at most \(N^2\) terms proves
\[
 |T_{\delta,N}(w,Y)|\le C_\tau N^{B_\tau}
 e^{N\{b_1+\omega(\delta)+\nu(\delta)+\log_+|Y|+\tau\}} .
 \tag{18}
\]
Cancellation inside \(H_N\) is retained. None is required between
the physical pairs \((a,j)\).

## 3. A scalar bound for the next type-three kernel

For \(0\le C\le11/20\), define
\[
 M_0(C)=\max_{0\le t\le1}\{L(t)-J(t)+Ct\}.
\]
We claim
\[
                              M_0(C)<3/5.
 \tag{19}
\]
It suffices to take \(C=11/20\). The function \(F\) being maximized
then has
\[
 F'(t)=11/20-\log(2\sin(\pi t/2)),\qquad
 F''(t)=-(\pi/2)\cot(\pi t/2)<0 .
 \tag{20}
\]
Its maximum lies between \(1/2\) and \(7/10\). At \(1/2\),
\(\log2<7/10\) makes \(F'>0\). At the other endpoint use
\[
 2\sin(7\pi/20)=2\cos(3\pi/20)>7/4,\quad
 \log(7/4)>6/11+18/1331=744/1331>11/20.
 \tag{21}
\]
The cosine bound follows from \(\cos x>1-x^2/2\) and
\(3\pi/20<33/70\). The logarithm bound uses its first two
positive arctanh-series terms.

On this maximizing interval,
\[
                 -F''(t)\ge(\pi/2)\tan(3\pi/20)>3/4.
 \tag{22}
\]
Indeed \(\tan x>x+x^3/3\), by integration of
\(1+\tan^2x>1+x^2\). At \(x>15/32\) this exceeds \(1/2\):
the integer comparison is \(49455>49152\). Also \(\pi>3\).
The written bound \(b_2=-4J(1/4)<7/12\) in
[the low-index kernel proof, equations (13)--(16)](research_mixed_next_low_index_kernel_margin.md)
and \(\log2>2/3\) give
\[
 F(1/2)<7/24+11/40=17/30,\qquad F'(1/2)<13/60.
\]
Integrating (22) and completing the square yields
\[
 M_0(11/20)<\frac{17}{30}
       +\frac23\left(\frac{13}{60}\right)^2
       =\frac{3229}{5400}<\frac35.
 \tag{23}
\]
This proves (19) without evaluating a critical point or action.

## 4. The entire next conditional sum

Let \(R=|Y|\), \(C=(-\log R)_+\), \(C_z=(\log|Z|)_+\).
The exact reciprocal numerator identity and (17) give
\[
 R^{-j}|p_j(Y)|\le N^A e^{N\{L(t)+Ct\}} .
 \tag{24}
\]
At \(R\ge1\), this uses
\(|p_j(Y)|=R^j|p_j(1/\overline Y)|\); the incoming power is
included exactly.

For \(\beta=0\), the resulting full-row rate is
\(2L(t)-2J(t)+(C+C_z)t\).
In both regimes (8),
\[
 C+C_z\le17\pi/50<11/10.
\]
Twice (19) therefore bounds the entire positive sum:
\[
                  |C_{0,N}(Y,Z)|\le C_\tau N^{B_\tau}
                                      e^{N(6/5+\tau)} .
 \tag{25}
\]
For \(\beta=1\), \(|Z|<1\), and the seam theorem supplies
\[
 \frac{|p_j(V)|}{S_j}\le CN^B e^{Nc_{\rm b}},\qquad
 \sum_{j<N}\frac{|p_j(V)|}{S_j^2}
       \le C_\tau N^{B_\tau}e^{N(7/15+\tau)},\quad |V|\le1.
 \tag{26}
\]
The first follows from the finite binomial identity. If \(R\ge1\),
(24) and (26) bound the entire kernel at rate
\(c_{\rm b}+7/15<19/24\).

If \(R\le1\), then \(C\le51\pi/250<13/20\).
On \(t\le1/2\) the same argument adds at most \(C/2\), giving
rate less than \(67/60\). On \(t\ge1/2\), use \(J(t)\ge0\) and
\(L(t)\le c_{\rm b}\) in (17), (24). The rate is at most
\(2c_{\rm b}+C<13/10\). Consequently
\[
 |C_{1,N}(Y,Z)|\le C_\tau N^{B_\tau}
 \begin{cases}
 e^{N(13/10+\tau)},&R\le1,\\
 e^{N(19/24+\tau)},&R\ge1 .
 \end{cases}
 \tag{27}
\]
Both endpoint indices and both level parities occur in these bounds.

## 5. Fourier weights and the original geometric action

The original cardinal interpolation proof, followed by the maximum
principle, gives
\[
             |d_N(Y)|\le CN^B e^{Nc_{\rm b}/2}\quad(|Y|\le1).
 \tag{28}
\]
For \(R\ge1\), apply the maximum principle to the reversed degree-\(D\)
polynomial to obtain
\[
 |d_N(Y)|R^{-N}
 \le R^{-1}\sup_{|V|=1}|d_N(V)|\le CN^B e^{Nc_{\rm b}/2}.
 \tag{29}
\]
This uses the actual forced polynomial and retains the selected
monomial once.

The [affine-floor proof](research_mixed_complete44_three_factor_affine_floor.md),
equations (11), (46)--(48), supplies
\[
 \Lambda_{123}(z)>\frac73+\frac1{100}\quad(\beta=0),\qquad
 \Lambda_{123}(z)+\tfrac12\Re g(z)>
                         \frac73+\frac{43}{400}\quad(\beta=1).
 \tag{30}
\]
For the second, the type-four rational lower witness improves by
\(39/400\), besides the original \(1/100\) profile reserve.
This does not assert a difference between the two actual actions.
For \(\beta=1\), the original Fourier-weight continuation gives
\[
 D_{1,N}(Z)\le C_\tau N^{B_\tau}
                          e^{N\{-\Re g(z)/2+\tau\}} .
 \tag{31}
\]
The bound includes its zeros without division.

Before the small losses in (18), the negative-height unselected
rates have the reserves
\[
\begin{split}
 &\left(\frac73+\frac1{100}\right)
 -\left(\frac{433}{500}+\frac{13}{80}+\frac65\right)
                          =\frac{689}{6000}>\frac1{10},\\
 &\left(\frac73+\frac{43}{400}\right)
 -\left(\frac{433}{500}+\frac{13}{80}+\frac{13}{10}\right)
                          =\frac{337}{3000}>\frac1{10}.
\end{split}
 \tag{32}
\]
The second comparison retains the same outgoing halfweight on both
sides through (31).

For the positive-height selected regime, the common next-kernel
ceiling \(6/5\) covers both types, because \(19/24<6/5\).
The additional rate in (18) is at most \(\pi/50<13/200\).
Even the smaller type-three floor leaves
\[
 \left(\frac73+\frac1{100}\right)
 -\left(\frac{433}{500}+\frac{13}{80}+\frac65+\frac{13}{200}\right)
                            =\frac{299}{6000}>\frac1{25}.
 \tag{33}
\]
Choose fixed \(\delta>0\) so that
\(\omega(\delta)+\nu(\delta)<1/100\), then choose the total
allowance from all finite estimates and the color neighborhood
less than \(1/100\). Equations (32)--(33) leave a gap greater
than \(1/50\), proving (7). Cauchy's formula on smaller color
disks gives the stated derivatives.

The first physical sum already has its original normalization.
The remaining integration contributes only its factor \(N\) and
a fixed path length. Thus (7) is an error estimate for an entire
physical index block under the next contraction. It does not estimate
the complementary indices, prove the whole second-period asymptotic,
or establish finitely many exceptional assignments.

## Direct inputs

The complete seam theorem supplies (2), (6), (12), (26), (28);
the boundary-strip theorem supplies (17); the low-index kernel
proof supplies \(b_2<7/12\); the affine-floor proof supplies (30);
and the original Fourier-weight continuation supplies (31).
The author has read back the full proof and all five directly used
source implications. The checked source versions are:

| Source | SHA-256 |
|---|---|
| research_mixed_complete44_second_period_seam_collar.md | e203f8041ddcc3c002d09de0a5d94a458f2499a3f55325fce27126c3c7b66a6c |
| research_mixed_boundary_strip_bounds.md | e288c5d0bcf77a073dbaa8bb2f27bd46ce208a56e63c8bd0e98dfdbbc8f8c6ff |
| research_mixed_next_low_index_kernel_margin.md | 35de8662e57070a4f19aef409f82c921283493ba3f0e17268f1c11a7eac1738c |
| research_mixed_complete44_three_factor_affine_floor.md | 112f3b5a8d40c7a3bb770b8deae7b189c4729235851d8a2036f8869edc332b7d |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |

Separate full proof and direct-source review is required before
adoption. No mathematical numerical evaluation, test, import,
compilation or frozen-source modification was used.

