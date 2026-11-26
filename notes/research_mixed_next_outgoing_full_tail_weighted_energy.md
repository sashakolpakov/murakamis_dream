# Outgoing weighted energy through the last retained physical row

Private exact-source proof, 8 November 2026. The positive outgoing
energy extends from the middle band to every physical index
\(M\le b\le D-1\). The metric remains the original \(S_b\).
A varying scalar row rotation joins the two coercive angular
regions; its exact off-diagonal error is \(O(N^{-1})\).

For the retained outgoing sum the upper exterior value at \(D\)
is exactly zero. Restoring the already paid high physical band
therefore gives a source reduction with only one exterior value.
The full transformed cutoff forcing is paid by its actual weighted
source estimate, leaving one coherent lower-boundary observation.
No outer suppression or change to a frozen source is asserted.
No mathematical numerical evaluation is used.

## 1. Original finite source and the full interval

Keep the notation of the adopted
[outgoing weighted-energy theorem](research_mixed_next_outgoing_weighted_energy.md):
\[
\begin{gathered}
N\ge6,\quad D=N-1,\quad
\theta=\pi/N,\quad q=e^{i\theta},\quad r=q^{-2},\quad
\kappa_N=q^{D^2/2},\\
M=\lceil N/2\rceil,\quad L=\lfloor N/6\rfloor,\quad
K=\lfloor N/4096\rfloor,\\
s_b=2\sin(b\theta),\quad S_b=\prod_{\nu=1}^{b}s_\nu,\quad
Y_b=r^b,\quad P_k=(r;r)_k,\quad p_k(Z)=(rZ;r)_k.
\end{gathered}                                                     \tag{1}
\]
Let
\[
\begin{split}
A_b&=Y_b(Y_b-1),\qquad
B_b=3Y_b-(1+r)Y_b^2,\qquad
C_b=r^{-1}(1-rY_b)^2,\\
a_b(Z)&=(-q)^b\sum_{k=K+1}^{D}
        \frac{Y_b^{-k}p_k(Y_b)p_k(Z)}{P_k^2},\\
f_b(Z)&=(-q)^b r^{-K-1}(1-r^{K+1}Z)
        \frac{Y_b^{-K}p_K(Y_b)p_K(Z)}{P_K^2}.
\end{split}                                                       \tag{2}
\]
The exact signed recurrence is
\[
Za_b=(\mathcal J_Na)_b+f_b,\qquad
(\mathcal J_Na)_b=-qA_ba_{b-1}+B_ba_b-q^{-1}C_ba_{b+1},
                         \quad1\le b\le D-1.                      \tag{3}
\]
This is the full range of
[paired characteristics, Proposition 1](research_mixed_next_outer_paired_newton_characteristics.md).
All numerator zeros are retained. In particular
\[
a_b=0\quad\hbox{if }D-b\le K,\qquad a_D=0,                         \tag{4}
\]
because the literal physical sum stops at \(k=D-b\).
The complete outgoing sum starting at zero has a nonzero
zero-row value at \(D\); (4) is a statement about (2).

Uniformity is proved on the original containing region
\[
Z=\rho e^{-i\alpha},\qquad
\frac45\le\rho\le\frac87,\qquad
\frac{3\pi}{5}\le\alpha\le\frac{39\pi}{50}.                          \tag{5}
\]
The actual complete \(343\) family of length at least five,
with \(w=-2\), \(Z=Z_*\), lies in this region.

The unchanged row phase and angular coordinate are
\[
w_b=\exp i\left\{\left(\frac{5b}{2}+\frac14\right)\theta
                                           -\frac\pi4\right\},
\qquad t_b=\frac{b\theta-\pi/2}{2}.                                 \tag{6}
\]
For \(M\le b\le D-1\), one has
\(0\le t_b\le\pi/4-\theta\). The exact diagonal of
\(W_N(\mathcal J_N-ZI)\), \(W_N=\operatorname{diag}(w_b)\), is
\[
V_b
=3e^{i(t_b+\theta/4)}
 +2\cos\theta\,e^{-i(3t_b+3\theta/4)}
 +\rho e^{i(5t_b+\theta/4-\alpha)}.                                \tag{7}
\]
Its limiting expression is
\[
V(t)=3e^{it}+2e^{-3it}+\rho e^{i(5t-\alpha)}.                        \tag{8}
\]
Equations (6)--(8) hold without a restriction \(b\le D-L\).

## 2. A second coercive rotation on the physical tail

For \(\pi/6\le t\le\pi/4\), set
\[
\mathcal E_+(t)=\Re V(t)+\Im V(t)
                              -4\sqrt2(\cos2t)^{3/2}.
                                                                    \tag{9}
\]
Write
\[
\mathcal E_+(t)=T_+(t)+\rho(\cos\psi+\sin\psi),\qquad
\psi=5t-\alpha,
\]
where the exact trigonometric simplification is
\[
T_+(t)=(\cos t+\sin t)(5-4\sin2t)
                              -4\sqrt2(\cos2t)^{3/2}.              \tag{10}
\]

First, \(T_+>0\) on this entire closed interval. Put
\[
d=1-\sin2t,\qquad
0\le d\le d_*=1-\sqrt3/2<1/7.
\]
The last inequality follows from \(\sqrt3>12/7\).
The first term in (10) is
\(\sqrt{2-d}(1+4d)\), and its second term is
\(4\sqrt2[d(2-d)]^{3/4}\).
After dividing by \(\sqrt{2-d}>0\), both compared quantities
are nonnegative. Their fourth-power difference is
\[
P(d)=(1+4d)^4-1024d^3(2-d)
     =1+16d+96d^2-1792d^3+1280d^4.                                \tag{11}
\]
On \([0,1/7]\),
\[
P'''(d)=-10752+30720d<0,\qquad P''(0)=192>0,\quad P'(0)=16>0.
\]
Thus \(P''\) can cross zero at most once. The derivative
\(P'\) first increases, and then may decrease; it can change
sign at most once, from positive to negative. Accordingly \(P\)
increases and then possibly decreases, so its minimum on
\([0,d_*]\) is at an endpoint.
At \(d=0\), \(P=1\). At \(d=d_*\), the original difference
in (10) is
\[
T_+(\pi/6)=\frac{3\sqrt3-5}{2}>0,
\]
using \(\sqrt3>5/3\). The positive fourth-power comparison
therefore gives \(P(d_*)>0\). This proves the assertion.

Next
\[
\frac{4\pi}{75}\le\psi\le\frac{13\pi}{20},
\qquad \cos\psi+\sin\psi>\frac25.                                 \tag{12}
\]
Up to \(\pi/2\), the sum is at least one. After \(\pi/2\),
write \(\psi=\pi/2+x\), \(0\le x\le3\pi/20<12/25\).
The last inequality uses \(\pi<22/7<16/5\).
The elementary sine and cosine bounds give
\[
\cos x-\sin x\ge1-x^2/2-x
   >1-\frac{72}{625}-\frac{12}{25}
    =\frac{253}{625}>\frac25.
\]
Combining (5), (10), and (12) proves the uniform strict bound
\[
\boxed{\qquad
\mathcal E_+(t)>\frac8{25},
                    \qquad \pi/6\le t\le\pi/4.
\qquad}                                                          \tag{13}
\]

The adopted energy theorem supplies, on \(0\le t\le\pi/6\),
\[
\mathcal E_-(t)=\Re V(t)-3\Im V(t)
                     -4\sqrt2(\cos2t)^{3/2}>\frac{51}{350}.         \tag{14}
\]
These inequalities have a uniform overlap. By continuity on the
compact parameter set (5), choose a fixed
\(\delta\in(0,\pi/6)\) such that (13), weakened to
\(\mathcal E_+>51/350\), also holds on
\([\pi/6-\delta,\pi/6]\).
Choose a fixed smooth real function \(\beta(t)\) with
\[
\beta=3\quad(t\le\pi/6-\delta),\qquad
\beta=-1\quad(t\ge\pi/6),\qquad -1\le\beta\le3.                     \tag{15}
\]
In the transition interval the expression with \(\beta\) is a
convex combination of (13) and (14). Hence
\[
\boxed{\quad
\Re V(t)-\beta(t)\Im V(t)
       -4\sqrt2(\cos2t)^{3/2}>\frac{51}{350},
                              \qquad0\le t\le\pi/4.
\quad}                                                            \tag{16}
\]
The interpolation and its bounded derivative are fixed before
the level varies.

## 3. The actual finite energy at the vanishing-sine endpoint

Let \(I=[a,b]\cap\mathbb Z\) be any nonempty interval in
\([M,D-1]\). Its test values are zero outside \(I\). Use exactly
the metric
\[
\langle f,g\rangle_{S,I}=\sum_{j\in I}S_j\overline{f_j}g_j.
\]
Define
\[
\mathcal A_{I,N}
 =D_\beta W_N(\mathcal J_{I,N}-ZI),\qquad
D_\beta=\operatorname{diag}(1+i\beta(t_j)).                         \tag{17}
\]
No row phase or row rotation has been commuted past a shift.

In coordinates \(g_j=\sqrt{S_j}f_j\), the off-diagonal part
\(H_N\) of \(W_N\mathcal J_{I,N}\) is Hermitian, with exact
adjacent magnitude \(s_{j+1}^{3/2}\). This follows from
\[
(W_N\mathcal J_N)_{j,j+1}=s_{j+1}^2e^{i\varphi_j},\qquad
(W_N\mathcal J_N)_{j+1,j}=s_{j+1}e^{-i\varphi_j},\qquad
S_{j+1}=S_js_{j+1},
                                                                    \tag{18}
\]
with the original \(\varphi_j\) of the energy source.
These identities remain valid through the last link before
\(D\), since every \(s_j,S_j\) being used is positive.

Write \(\beta_j=\beta(t_j)\). The exact Hermitian part of
the rotated off-diagonal operator is
\[
H_N+\frac{i}{2}[\operatorname{diag}(\beta_j),H_N].                  \tag{19}
\]
Since \(t_{j+1}-t_j=\theta/2\) and
\(\sup|\beta'|<\infty\), the commutator norm is \(O(N^{-1})\).
For example each of its two possible row entries has magnitude
at most
\(\tfrac14\theta\sup|\beta'|\,2^{3/2}\); the same row and
column bound controls its Euclidean operator norm.
No division by a small \(s_j\) occurs.

The remaining two-term quadratic estimate gives
\[
\begin{split}
\Re\langle f,\mathcal A_{I,N}f\rangle_{S,I}
\ge\sum_{j\in I}S_j
 \{\Re V_j-\beta_j\Im V_j-s_j^{3/2}-s_{j+1}^{3/2}
                                      -O(N^{-1})\}|f_j|^2.
\end{split}                                                       \tag{20}
\]
Missing links only improve this lower bound. The error is
uniform over all intervals and parameters.

The passage from (20) to (16) is also uniform up to \(D-1\).
Indeed \(s_j=2\cos(2t_j)\) exactly,
\[
|s_{j+1}-s_j|\le2\theta,
\]
and the function \(x^{3/2}\) is Lipschitz on \([0,2]\),
with derivative bounded by \(3\sqrt2/2\).
Thus
\[
s_j^{3/2}+s_{j+1}^{3/2}
 =4\sqrt2(\cos2t_j)^{3/2}+O(N^{-1}),                               \tag{21}
\]
even as \(s_j\) tends to zero. The exact diagonal (7) differs
from (8) by \(O(N^{-1})\) uniformly on the whole interval.
Equation (16) now proves:

**Theorem 1.** For all sufficiently large levels, at both
parities, uniformly over (5) and every interval
\(I\subseteq[M,D-1]\),
\[
\boxed{\quad
\Re\langle f,\mathcal A_{I,N}f\rangle_{S,I}
          \ge\frac1{20}\|f\|_{S,I}^2,\qquad
\|(\mathcal J_{I,N}-ZI)^{-1}\|_{S\to S}
          \le20\sqrt{10}.
\quad}                                                            \tag{22}
\]
The first inequality gives injectivity and therefore invertibility
of this finite square matrix. Since
\(\|D_\beta W_N\|\le\sqrt{10}\), it gives the second inequality.

The same explicit entry estimate as before remains valid. Every
entry of
\(\operatorname{diag}(\sqrt{S_j})\mathcal A_{I,N}
 \operatorname{diag}(\sqrt{S_j})^{-1}\)
has modulus below \(20\): its diagonal is at most
\(\sqrt{10}(5+8/7)<20\), and each off-diagonal entry at most
\(\sqrt{10}\,2^{3/2}<9\).
With
\[
\gamma=\log(1+1/2400),
\]
conjugation by \(\operatorname{diag}(e^{\pm\gamma j})\)
changes its operator norm by at most
\(60(e^\gamma-1)=1/40\). Its inverse then has norm at most
\(40\). The diagonal row factors commute with this conjugation.
Consequently, writing \(G_{I,N}=(\mathcal J_{I,N}-ZI)^{-1}\),
\[
\boxed{\quad
|(G_{I,N})_{i,j}|
 \le40\sqrt{10}\sqrt{\frac{S_j}{S_i}}\,
                              e^{-\gamma|i-j|}.
\quad}                                                            \tag{23}
\]
The sine-product ratio is part of this estimate. Neither (22)
nor (23) changes the metric into an unweighted source norm.

## 4. One exterior value for the retained actual source

Take the complete interval
\[
                              I_N=[M,D-1].
\]
The exact restriction of (3), using (4), is
\[
(\mathcal J_{I_N,N}-ZI)a_{I_N}
   =-f_{I_N}+qA_Ma_{M-1}\mathbf e_M.                              \tag{24}
\]
Thus
\[
a_i=-\sum_{j=M}^{D-1}(G_{I_N,N})_{i,j}f_j
                  +qA_M(G_{I_N,N})_{i,M}a_{M-1}.                  \tag{25}
\]
In particular
\[
\|a_{I_N}\|_S
 \le20\sqrt{10}
     \{\|f_{I_N}\|_S+\sqrt{S_M}|A_Ma_{M-1}|\}.                     \tag{26}
\]
This keeps the original lower exterior value at \(M-1\); only
the exactly terminating upper one has disappeared.

Retain the original inner periods
\[
\lambda_j=\phi_N(R^3e_jQ_N^{\rm full}).
\]
Let \(v\) be the unique zero-exterior solution of
\[
(\mathcal J_{I_N,N}^{\mathrm t}-ZI)v=\lambda_{I_N}.                 \tag{27}
\]
The transpose is bilinear and does not conjugate \(Z\).
The inverse in the dual metric \(S^{-1}\) has the same norm
bound as (22), so
\[
\|v\|_{S^{-1}}\le20\sqrt{10}\|\lambda_{I_N}\|_{S^{-1}}.
\]
Pairing (24),(27), before any absolute values, gives
\[
\boxed{\quad
\sum_{j=M}^{D-1}\lambda_ja_j
 =-\sum_{j=M}^{D-1}v_jf_j+qA_Mv_Ma_{M-1}.
\quad}                                                            \tag{28}
\]
The original period's own endpoint conditions have not been
replaced by zero boundary data. The latter condition belongs
only to the new test \(v\).

## 5. The transformed forcing on the extended interval

The source proof of the
[transformed-forcing theorem, Sections 2--4](research_mixed_next_outgoing_transformed_forcing_bound.md)
extends to this interval with only polynomial extra costs.
Here are the required changes of range.

First its complete physical-source bound is independent of the
outgoing index:
\[
\max_{0\le j\le U}|Q_N^{\rm full}(c_j)|
 \le C_\tau N^{A_\tau}e^{N(\mathfrak M_3+\tau)},\qquad
U=\lfloor N/2\rfloor-1,\qquad \mathfrak M_3<121/63.
                                                                    \tag{28a}
\]
It combines the actual physical packet up to angle \(\pi/2\),
its original decreasing action, and the complete upper-physical
majorant beyond that angle. Thus no new off-grid packet or
normal estimate is required here.

For \(M\le b\le D\), use the ordinary radical quotient
\[
P_b^{\rm rad}(z)=e_b(z)/e_M(z)
       =\prod_{h=M}^{b-1}(c_h-z)/s_{h+1}^2.
                                                                    \tag{28b}
\]
At a double node \(c_j\) it is zero if \(j>D-b\).
Otherwise the same monotone physical-node comparison as in
that source gives \(|c_h-c_j|\le2-c_h\le s_h^2\).
Consequently
\[
|P_b^{\rm rad}(c_j)|\le s_M^2/s_b^2\le C N^2 .
\]
The last inequality holds through \(b=D\): on this half of
the physical range \(s_b\ge2\sin(\pi/N)\ge4/N\).
The empty product at \(b=M\) also satisfies the bound.
The exact consumed-normal formula
\(\lambda_b=\sum_{j=0}^{U}\mu_jP_b^{\rm rad}(c_j)
Q_N^{\rm full}(c_j)\), with \(|\mu_j|\le2\), therefore
retains the same exponential rate in (28a) uniformly on the
extended interval. All full first normals have been consumed
by that original formula; the odd simple node is absent there.

The metric does not require a lower bound by \(S_M\) on the
new tail. The sufficient bounds are instead
\[
1\le S_b\le C N^{1/2}2^{N/3}
                  \qquad(M\le b\le D).
                                                                    \tag{28c}
\]
Indeed the factors \(s_j\) are at least one until \(5N/6\)
and at most one afterward. The product first increases and
then decreases, so its minimum on this half interval is at
\(M\) or \(D\). The exact identities
\(S_D=N\), \(S_M^2=2N\) at even levels and
\(S_M^2=4N\cos^2(\pi/(2N))\) at odd levels prove the lower
bound. Up to its maximum there are at most \(N/3\) additional
factors, each at most two. These same identities prove the
upper bound, including the rounded maximum.

The literal \(k=K\) bound \(|f_b|\le(15/7)e^{N/200}\)
continues to hold for every \(b\ge M\), including all
terminated rows. Thus (28a)--(28c) and the dual inverse
bound (22) give
\[
\begin{split}
\left|\frac1{\kappa_N^2N}
               \sum_{j=M}^{D-1}v_jf_j\right|
&\le N^{-1}\|v\|_{S^{-1}}\|f\|_S\\
&\le C_\tau N^{A_\tau}
  e^{N\{\mathfrak M_3+\tau+1/200+(\log2)/6\}}.
\end{split}
\]
The written inequalities \(\log2<7/10\) and (28a) give
\[
\frac{419}{200}
 -\left(\frac{121}{63}+\frac7{60}+\frac1{200}\right)
   =\frac{83}{1575}>\frac1{20}>\frac1{25}.
\]
Choosing the fixed tolerance and absorbing polynomial factors
inside this strict reserve proves
\[
\boxed{\quad
\left|\frac1{\kappa_N^2N}
             \sum_{j=M}^{D-1}v_jf_j(Z_*)\right|
 \le C e^{N(419/200-1/25)}.
\quad}                                                            \tag{28d}
\]
This estimates the forcing after the inverse. It does not
substitute the different literal pairing with \(\lambda_j\).

## 6. Restoring the paid high band in the original observation

The original remaining middle observation is
\[
\mathscr R_N
  =\frac1{\kappa_N^2N}
          \sum_{j=M}^{D-L}\lambda_ja_j(Z_*).                       \tag{29}
\]
Its upper limit satisfies \(D-L=\lceil5N/6\rceil-1\) exactly,
at both parities.

The [actual high-band theorem, equations (13),(16)--(19)](research_mixed_next_right_insertion_actual_high_band.md)
also pays the retained \(k>K\) version of its physical band.
This is licensed by its proof, not by subtracting part of a
coherent sum. More explicitly, at \(j\ge\lceil5N/6\rceil\)
the physical outgoing stop is \(n=D-j<N/6\). Its equation
(13) is the positive estimate
\[
\sum_{k=0}^{n}|R_{j,k}(Z)|
 \le \frac1{S_n}\sum_{k=0}^{n}\binom nk(15/7)^k
 =\frac{(22/7)^n}{S_n}.
\]
Restricting to \(k>K\) only decreases this right-hand-side
construction. Every terminal insertion and every physical
normal of the same proof is unchanged. Hence its positive
attached bound, with the original scalar, remains
\[
\sum_{j\in J}
 \left|\frac{\lambda_ja_j(Z_*)}{\kappa_N^2N}\right|
 \le C_\tau N^{A_\tau}e^{N(1499/720+\tau)}
       \quad
 \left(J\subseteq\{\lceil5N/6\rceil,\ldots,D\}\right).               \tag{30}
\]
The source action satisfies \(\Lambda>419/200\), and
\(419/200-1499/720=47/3600>1/100\).
After absorbing polynomial factors with the strict reserve,
(30) allows restoring the band through \(D-1\) with an
\(O(e^{N(\Lambda-1/200)})\) error. No additional small-\(k\)
subtraction is needed for this restoration.

Combining (28), (28d), and (29)--(30) gives the source-specific
conclusion
\[
\boxed{\quad
\mathscr R_N
 =\frac{qA_M}{\kappa_N^2N}v_Ma_{M-1}(Z_*)
            +O(e^{N(\Lambda-1/200)}).
\quad}                                                            \tag{31}
\]
All finite indices, \((-q)^j\) phases, and the original
\(\kappa_N^{-2}/N\) are retained. In the complete transfer
identity its error is combined with the already established
contour/deletion error by taking the smaller positive gap.
Both original Fourier sectors enter through that unchanged
identity.

In particular the
[original complete transfer reduction](research_mixed_next_three_outer_casimir_observation.md)
now reads
\[
\boxed{\quad
\mathcal T_0[F_N](-2,Z_*)
 =I_{{\rm geom},N}
  +\frac{qA_Ma_{M-1}(Z_*)}{\kappa_N^2N}
       \sum_{i=M}^{D-1}(G_{I_N,N}(Z_*))_{i,M}\lambda_i
  +O(e^{N(\Lambda-\epsilon_0)}),
\quad}                                                            \tag{32}
\]
where \(\epsilon_0=\min(\epsilon_*,1/200)>0\), and
\(\epsilon_*\) is the already proved transfer-reduction gap.
The geometric integral and its nonzero coefficient are unchanged.

The remaining quantity is the single coherent product
\(a_{M-1}v_M\), with the exact Green observation displayed
in (32). Neither a bound for each original high-index tail
nor the weighted inverse alone pays that product. The upper
boundary and all transformed forcing are paid, but this
lower-boundary observation still requires a sufficient action
bound. No full transfer asymptotic or new jet statement is
inferred here.

## Source bindings

- Original weighted energy:
  fdcc1fab386fd94047022c04911d0f5874768674dd546aef33985b54a758b372.
- Paired finite recurrences:
  8372ed7387b7465b6a66cc207f2ac8e3803e3def10d7beff115c038d4334c909.
- Full high-band source:
  1e15ac042b91461b3bd9b619f8205db2266ad7fee4185a04d0c7c3acfd5a5be6.
- Original small-outgoing source:
  6905d51ca102e2686d9b9845cfe333017ddcbcf45a70dbcf10741438f31dc1f0.
- Transformed-forcing source:
  840126070ec5c85f8e6dd0c5423515e2027a2191a62bd08ffc51a6f237e5773b.
- Original complete outer observation:
  cbbc62951666d06e0ae77b29f49f563d91c2024dc8da900ae996144d7db39dab.

All inequalities were checked by written algebra and source reading;
no numerical evaluation or replay was performed.

