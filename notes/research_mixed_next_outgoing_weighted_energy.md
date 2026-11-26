# A positive weighted energy for the exact outgoing recurrence

Private exact-source proof, 8 November 2026. The signed conditional
three-term equation has a uniformly coercive Dirichlet realization
on the physical middle arc after an explicit unit-modulus row
normalization. Its positive metric is the original sine product
\(S_b\), not the unweighted counting norm. The estimate is uniform
over the actual containing outgoing region and both parities.

The original cutoff forcing and both exterior source values remain
in its application. An inverse estimate in this metric does not
by itself control the pairing with the inner period sequence.
No overlap lower bound, actual cancellation conclusion, mathematical
numerical evaluation, or frozen-source edit is used.

## 1. Original signed operator

Keep exactly the notation and finite source in
[paired Newton characteristics, equations (1)--(12)](research_mixed_next_outer_paired_newton_characteristics.md):
\[
\begin{gathered}
\theta=\pi/N,\quad q=e^{i\theta},\quad r=q^{-2},\quad D=N-1,\quad
\kappa_N=q^{D^2/2},\\
M=\lceil N/2\rceil,\quad L=\lfloor N/6\rfloor,\quad
K=\lfloor N/4096\rfloor,\quad
\mathcal I_N^{\rm mid}=[M,D-L]\cap\mathbb Z,\\
s_b=2\sin(b\theta),\quad S_b=\prod_{\nu=1}^{b}s_\nu,\quad
Y_b=r^b,\quad P_k=(r;r)_k,\quad p_k(V)=(rV;r)_k,\\
A_b=Y_b(Y_b-1),\qquad
B_b=3Y_b-(1+r)Y_b^2,\qquad
C_b=r^{-1}(1-rY_b)^2 .
\end{gathered}                                                     \tag{1}
\]
On this range \(s_b,S_b>0\). The letter \(C_b\) here denotes
an operator coefficient, not the outgoing sum.

The original signed sequence and its equation are
\[
\begin{split}
a_b(Z)&=(-q)^b\sum_{k=K+1}^{D}
       \frac{Y_b^{-k}p_k(Y_b)p_k(Z)}{P_k^2},\\
Za_b&=(\mathcal J_Na)_b+f_b,\qquad
(\mathcal J_Na)_b=-qA_ba_{b-1}+B_ba_b-q^{-1}C_ba_{b+1},\\
f_b(Z)&=(-q)^b r^{-K-1}(1-r^{K+1}Z)
                   \frac{Y_b^{-K}p_K(Y_b)p_K(Z)}{P_K^2}.
\end{split}                                                       \tag{2}
\]
All rows above their physical stop \(D-b\) are zero. The source
identity (2) holds through numerator zeros without dividing by
them. The complete sum starting at \(k=0\) has the same homogeneous
equation. In particular the cutoff forcing is not silently set to
zero for the retained sequence.

For the original complete words in powers three and four beginning
\(343\), of length at least five, retain \(w=-2\), \(Z=Z_*\)
and write
\[
Z=\rho e^{-i\alpha},\qquad
\frac45\le\rho\le\frac87,\qquad
\frac{3\pi}{5}\le\alpha\le\frac{39\pi}{50}.
                                                                    \tag{3}
\]
The original actual inequalities are strict where specified in
the weighted outgoing source. Proving the estimate on the closed
region (3) gives uniformity for that source without changing its
reference or logarithmic branches.

There is no positive diagonal symmetrization of the unmodified
\(\mathcal J_N\) on a block with three consecutive nodes.
Indeed the product of two opposite off-diagonal entries is
\[
(\mathcal J_N)_{b,b+1}(\mathcal J_N)_{b+1,b}
  =C_bA_{b+1}
  =i e^{-i(5b+3)\theta}s_{b+1}^{\,3}.
                                                                    \tag{4}
\]
Diagonal similarity preserves this product. In a Hermitian
tridiagonal matrix it would be positive real. Consecutive products
in (4) have phase ratio \(e^{-5i\theta}\), which is not positive
real for \(N\ge6\). A common scalar rotation or scalar diagonal
shift does not remove this obstruction. This observation concerns
that diagonal symmetrization only.

## 2. Exact row phase and positive metric

Define the unit-modulus row factors
\[
w_b=\exp i\left\{\left(\frac{5b}{2}+\frac14\right)\theta
                                          -\frac{\pi}{4}\right\},
\qquad W_N=\operatorname{diag}(w_b).
                                                                    \tag{5}
\]
The exact original coefficients satisfy
\[
A_b=-i e^{-3ib\theta}s_b,\qquad
C_b=-e^{-2ib\theta}s_{b+1}^{\,2}.
                                                                    \tag{6}
\]
For
\(\varphi_b=(b/2-3/4)\theta-\pi/4\), equations (5)--(6)
give
\[
(W_N\mathcal J_N)_{b,b+1}
       =s_{b+1}^{\,2}e^{i\varphi_b},\qquad
(W_N\mathcal J_N)_{b+1,b}
       =s_{b+1}e^{-i\varphi_b}.
                                                                    \tag{7}
\]
Since \(S_{b+1}=S_bs_{b+1}\), these off-diagonal entries are
self-adjoint for the positive inner product
\[
\langle f,g\rangle_{S,I}
       =\sum_{b\in I}S_b\overline{f_b}g_b
                                                                    \tag{8}
\]
on every integer interval \(I\subseteq\mathcal I_N^{\rm mid}\).
Only the off-diagonal part is asserted self-adjoint. The
diagonal of the pencil is the complex number
\[
                         V_b(Z)=w_b(B_b-Z).
                                                                    \tag{9}
\]

Put
\[
t_b=\frac{b\theta-\pi/2}{2}.
                                                                    \tag{10}
\]
For \(b\in\mathcal I_N^{\rm mid}\), \(0\le t_b\le\pi/6\).
Direct substitution in (9) gives the exact diagonal formula
\[
V_b(Z)
 =3e^{i(t_b+\theta/4)}
       +2\cos\theta\,e^{-i(3t_b+3\theta/4)}
       +\rho e^{i(5t_b+\theta/4-\alpha)}.
                                                                    \tag{11}
\]
In particular its uniform limiting diagonal is
\[
V(t;\rho,\alpha)=3e^{it}+2e^{-3it}
                                      +\rho e^{i(5t-\alpha)}.
                                                                    \tag{12}
\]
This limit keeps the original \((-q)^b\) sign and outgoing
parameter. It is not an unsigned characteristic.

## 3. A uniform trigonometric energy inequality

Define, for (3) and \(0\le t\le\pi/6\),
\[
\begin{split}
\mathcal E(t;\rho,\alpha)
={}&3\cos t-9\sin t+2\cos3t+6\sin3t\\
 &+\rho\{\cos(5t-\alpha)-3\sin(5t-\alpha)\}
                    -4\sqrt2(\cos2t)^{3/2}.
\end{split}                                                       \tag{13}
\]
The real positive power is used, since \(\cos2t\ge1/2\).
We prove
\[
\boxed{\qquad
\mathcal E(t;\rho,\alpha)>\frac{51}{350}
           \quad\hbox{throughout the closed domain above}.
\qquad}                                                           \tag{14}
\]

Write \(\mathcal E=T+\rho G\), where
\[
T=3\cos t-9\sin t+2\cos3t+6\sin3t
                    -4\sqrt2(\cos2t)^{3/2},
\qquad G=\cos(5t-\alpha)-3\sin(5t-\alpha).
                                                                    \tag{15}
\]
For \(c=\cos2t\),
\[
T''=-3\cos t+9\sin t-18\cos3t-54\sin3t
                   +12\sqrt2\,\frac{3c^2-1}{\sqrt c},
\qquad (\rho G)''=-25\rho G.
                                                                    \tag{16}
\]
The function \((3c^2-1)/\sqrt c=3c^{3/2}-c^{-1/2}\)
is strictly increasing for \(c>0\).

Here are the elementary witnesses used below:
\[
\sqrt2<10/7,\quad \sqrt2>7/5,\quad
\cos(\pi/12)>9/10,\quad \sin(\pi/12)<4/15,
\]
\[
\cos(11\pi/50)<4/5,\qquad
\sin(11\pi/50)>5/8,\qquad
\sin(3\pi/8)>23/25,\qquad 2^{3/4}<17/10.
                                                                    \tag{17}
\]
For completeness, \(\pi/12<11/42<4/15\) and
\(1-(11/42)^2/2>9/10\) prove the first small-angle bounds.
For the next pair, \(11\pi/50>2/3\) gives
\(\cos(11\pi/50)<191/243<4/5\).
Also \(11\pi/50>11/16\), and
\[
\sin(11/16)>11/16-(11/16)^3/6
                       =15565/24576>5/8.
\]
The angle lies below \(\pi/2\), so monotonicity applies.
Further,
\(\sin^2(3\pi/8)=(2+\sqrt2)/4>17/20>(23/25)^2\).
Finally \((17/10)^4>8\). These are written rational or
alternating-series comparisons.

On \(0\le t\le\pi/12\), put \(\beta=\alpha-5t\).
Then
\[
11\pi/60\le\beta\le39\pi/50,\qquad
G=\cos\beta+3\sin\beta>43/40 .
                                                                    \tag{18}
\]
To justify the last inequality, this trigonometric function is
positive on the entire interval: before \(\pi/2\) both terms
are nonnegative, and afterward (17) gives the lower bound
\(-4/5+3(5/8)=43/40\).
It is therefore concave on this interval. Its left endpoint
exceeds \(3/2\), since \(11\pi/60>\pi/6\); its right endpoint
exceeds \(43/40\), again by (17). Thus its minimum exceeds
\(43/40\). It follows that \(\rho G>43/50\).
Equation (16) gives
\[
T''<
\frac{240}{7}+\frac{12}{5}-\frac{27}{10}-\frac{63}{5}
=\frac{1497}{70},
\qquad
\mathcal E''<\frac{1497}{70}-\frac{43}{2}
                                    =-\frac4{35}<0.
                                                                    \tag{19}
\]
The omitted term \(-54\sin3t\) is nonpositive.

On \(\pi/12\le t\le\pi/8\), one has
\[
-109\pi/300\le5t-\alpha\le\pi/40.
                                                                    \tag{20}
\]
For negative angles in this interval \(G>0\) directly.
For nonnegative angles, \(\pi/40<1/12\) gives
\(G>1-1/288-1/4>0\).
Here \(-3\cos t+9\sin t<2\),
\(\sin3t>7/10\), and \(\cos3t\ge0\).
Since \(c\le\sqrt3/2<7/8\), monotonicity in (16), together
with \(\sqrt{7/8}>9/10\), gives
\[
12\sqrt2\,\frac{3c^2-1}{\sqrt c}<\frac{2075}{84}.
                                                                    \tag{21}
\]
Consequently
\[
\mathcal E''<T''<
2-\frac{189}{5}+\frac{2075}{84}
                               =-\frac{4661}{420}<0.
                                                                    \tag{22}
\]

On \(\pi/8\le t\le\pi/6\), the relevant angle lies in
\([-31\pi/200,7\pi/30]\). Negative angles give \(G>0\).
On the nonnegative part,
\[
                         G>-13/10 .
                                                                    \tag{23}
\]
Indeed \(3\sin x-\cos x\) is increasing on this interval,
and \(7\pi/30<11/15\). The alternating sine upper bound
and quadratic cosine lower bound give
\[
\begin{split}
3\sin(11/15)-\cos(11/15)
&\le \frac65+\frac{242}{3375}+\frac{(11/15)^5}{40}\\
&<\frac65+\frac3{40}+\frac1{40}=\frac{13}{10}.
\end{split}
\]
Thus \(\rho G>-52/35\). In this last interval
\(\sin3t>23/25\), \(\cos3t\ge0\), and \(c\le1/\sqrt2\).
The last term of (16) is at most \(6\,2^{3/4}<51/5\).
Therefore
\[
T''<2+\frac{51}{5}-\frac{1242}{25}=-\frac{937}{25},
\qquad
\mathcal E''<-\frac{937}{25}+\frac{260}{7}
                                     =-\frac{59}{175}<0.
                                                                    \tag{24}
\]

Equations (19), (22), and (24) prove strict concavity of
\(\mathcal E\) on its full interval. At its left endpoint,
(18) and (17) give
\[
\mathcal E(0)>5-\frac{40}{7}+\frac{43}{50}
                                             =\frac{51}{350}.
                                                                    \tag{25}
\]
At its right endpoint, (23) gives
\[
\mathcal E(\pi/6)
 >\frac{3\sqrt3}{2}-\frac12-\frac{52}{35}
 >2-\frac{52}{35}=\frac{18}{35}>\frac{51}{350},
                                                                    \tag{26}
\]
using \(\sqrt3>5/3\).
A concave function lies above the chord between its endpoints.
This proves (14), uniformly over (3).

## 4. The actual finite Dirichlet inverse

Let \(\mathcal J_{I,N}\) be the restriction of the original
operator to any nonempty interval
\(I=[a,b]\subseteq\mathcal I_N^{\rm mid}\), with zero exterior
test values only. Define
\[
\mathcal A_{I,N}(Z)=(1+3i)W_N(\mathcal J_{I,N}-ZI).
                                                                    \tag{27}
\]
The letters \(a,b\) in the interval endpoints are indices,
not the sequence or coefficients of (2).

**Theorem.** For all sufficiently large \(N\), uniformly over
both parities, every such interval, and all \(Z\) in (3),
\[
\boxed{\quad
\Re\langle f,\mathcal A_{I,N}(Z)f\rangle_{S,I}
                    \ge\frac1{20}\|f\|_{S,I}^2,\qquad
\|(\mathcal J_{I,N}-ZI)^{-1}\|_{S\to S}
                    \le20\sqrt{10}.
\quad}                                                            \tag{28}
\]

To prove it, use the exact off-diagonal adjointness (7).
Its quadratic form is real, so multiplication by \(1+3i\)
does not change its real part. In coordinates
\(\sqrt{S_j}f_j\), the magnitude of each adjacent
off-diagonal entry is \(s_{j+1}^{3/2}\).
The elementary two-term quadratic inequality therefore gives
\[
\Re\langle f,\mathcal A_{I,N}(Z)f\rangle_{S,I}
\ge\sum_{j\in I}S_j
 \{\Re V_j-3\Im V_j-s_j^{3/2}-s_{j+1}^{3/2}\}|f_j|^2 .
                                                                    \tag{29}
\]
Missing links at the two ends only improve this bound.

By (10)--(11) and \(s_j=2\cos(2t_j)\), the quantity in braces
is
\(\mathcal E(t_j;\rho,\alpha)+O(N^{-1})\), uniformly on
the whole closed domain. The \(s_{j+1}\) term has the same
uniform error since its argument changes by \(\theta\) in
a fixed interval where the sine is positive and bounded
away from zero. Thus (14) makes (29) at least
\((1/20)\|f\|_{S,I}^2\) for all large \(N\).

This finite square matrix is injective, hence invertible,
and its inverse has norm at most \(20\) in (8).
Multiplication by \(W_N\) is an isometry there, and
\(|1+3i|=\sqrt{10}\). Applying this to (27) proves the
second assertion of (28). No commutation of the row
normalization with a shift is used.

The inverse also has an explicit weighted entry estimate.
Let \(\mathsf D_S=\operatorname{diag}(\sqrt{S_j})\) on \(I\).
Every entry of
\(\mathsf D_S\mathcal A_{I,N}(Z)\mathsf D_S^{-1}\)
has modulus less than \(20\): its diagonal is bounded by
\(\sqrt{10}(5+8/7)<20\), and its off-diagonal magnitude
is at most \(\sqrt{10}\,2^{3/2}<9\).
Set
\[
                         \gamma=\log(1+1/2400)>0.
                                                                    \tag{29a}
\]
Conjugating this width-one matrix by
\(\operatorname{diag}(e^{\pm\gamma j})\) changes its row
and column sums by at most
\(3\cdot20(e^\gamma-1)=1/40\).
The corresponding operator norm is at most \(1/40\), so
its accretivity remains at least \(1/40\).
Its inverse consequently has norm at most \(40\).
The row factor \(W_N\) commutes with both diagonal
conjugations. Choosing the sign according to \(i-j\)
therefore proves
\[
\boxed{\quad
\left|(\mathcal J_{I,N}-ZI)^{-1}_{i,j}\right|
 \le40\sqrt{10}\sqrt{\frac{S_j}{S_i}}\,
                              e^{-\gamma|i-j|}.
\quad}                                                            \tag{29b}
\]
The sine-product ratio in this estimate is part of the
conclusion and is not replaced by a constant.

## 5. Original forcing, exterior values, and period pairing

The original sequence \(a_b(Z)\) is not given zero exterior
values. Its exact restriction satisfies
\[
(\mathcal J_{I,N}-ZI)a_I
 =-f_I+qA_a a_{a-1}\mathbf e_a
                      +q^{-1}C_ba_{b+1}\mathbf e_b.
                                                                    \tag{30}
\]
In particular, writing \(G_{I,N}(Z)=(\mathcal J_{I,N}-ZI)^{-1}\),
the exact source representation is
\[
a_i=-\sum_{j\in I}G_{I,N}(Z)_{i,j}f_j
       +qA_aG_{I,N}(Z)_{i,a}a_{a-1}
       +q^{-1}C_bG_{I,N}(Z)_{i,b}a_{b+1}.
                                                                    \tag{30a}
\]
Equation (29b) estimates each of these terms with its
displayed factor \(\sqrt{S_j/S_i}\) and its exact distance.
It gives a response to the original forcing and the two
exterior values, rather than discarding either boundary.

Here \(\mathbf e_j\) is the coordinate vector at \(j\);
when \(a=b\) both displayed terms occur at that coordinate.
Consequently the source-valid energy consequence is
\[
\|a_I\|_{S,I}\le20\sqrt{10}
\left\{\|f_I\|_{S,I}
 +\sqrt{S_a}|A_a a_{a-1}|
 +\sqrt{S_b}|C_ba_{b+1}|\right\}.
                                                                    \tag{31}
\]
For the complete outgoing sum the forcing term is zero,
but the two exterior values still remain.

Retain the actual inner periods
\(\lambda_j=\phi_N(R^3e_jQ_N^{\rm full})\).
Their original paired contribution has normalization
\[
\frac1{\kappa_N^2N}\sum_{j\in I}\lambda_ja_j .
                                                                    \tag{32}
\]
The weighted dual norm is
\(\|\lambda_I\|_{S^{-1},I}
  =(\sum_{j\in I}|\lambda_j|^2/S_j)^{1/2}\).
Cauchy's inequality bounds (32) by
\(N^{-1}\|\lambda_I\|_{S^{-1},I}\|a_I\|_{S,I}\);
neither factor is assigned an adequate action bound here.

There is also an exact inverse version without taking absolute
values. Let the auxiliary test \(v\), with zero exterior
values, solve
\[
(\mathcal J_{I,N}^{\rm t}-ZI)v=\lambda_I .
                                                                    \tag{33}
\]
The transpose is bilinear, without complex conjugating \(Z\).
The weighted dual inverse norm equals the primal inverse norm,
so
\(\|v\|_{S^{-1},I}\le20\sqrt{10}\|\lambda_I\|_{S^{-1},I}\).
Pairing (33) with (30) gives the exact identity
\[
\boxed{\quad
\sum_{j\in I}\lambda_ja_j
 =-\sum_{j\in I}v_jf_j
      +qA_a v_a a_{a-1}
      +q^{-1}C_bv_ba_{b+1}.
\quad}                                                            \tag{34}
\]
The two terms here are the exterior source terms of this newly
constructed zero-exterior test. They are not a declaration
that the original period sequence has zero boundary values.
If the original \(\lambda\), rather than \(v\), is used in
summation by parts, all four terms of paired-characteristics
equation (20) remain exactly as stated there.

The adopted small-index source bound pays the literal pairing
\(\sum\lambda_jf_j\). It does not by itself pay
\(\sum v_jf_j\) in (34), since the inverse changes the test.
The original twelve-term period equation, its even forcing,
its odd vanishing, and its own endpoints are unchanged.
No estimate for their interaction with this inverse is asserted.

Finally the metric is \(S_j\). It has nonconstant factorial
scale across the middle interval, so changing from this
norm to unweighted source norms is not free. Equation (28)
excludes a small-residual, zero-exterior vector for the
outgoing pencil in this specified metric. The actual outgoing
sequence has the forcing and exterior terms (30), and the
original observation has the separate period vector (32).
Controlling those terms jointly remains necessary before
deducing outer suppression or a statement about almost
invariant vectors for the complete source.

## Source versions

- Paired Newton characteristics:
  8372ed7387b7465b6a66cc207f2ac8e3803e3def10d7beff115c038d4334c909.
- Original actual weighted outgoing source:
  9a34c4d9e22d75f3e4d5152eeb6841812e2ba3e67f12afd9357dcc4c288d4a5d.

All comparisons above are exact written inequalities. No numerical
evaluation, replay, or change to a frozen source was used.
