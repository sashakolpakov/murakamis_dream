# Finite outgoing Green localization and the actual insertion

Private finite-source deduction, 8 November 2026. The original
outgoing energy margin gives a stronger exponential Green bound
on every physical Dirichlet interval, including the terminating
row. Its rate is the same explicit constant that occurs in the
selected-action inequality, but the proof below uses the actual
finite matrix, not an inference from its principal roots.

For the unresolved lower-boundary observation this gives an
exact finite truncation with a controlled tail. It also gives a
polynomial ceiling for its actual insertion on a fixed spectral
ellipse. Neither conclusion pays the signed boundary observation.
No mathematical numerical evaluation or frozen-source edit is used.

## 1. Original finite operator and the retained energy margin

Use all notation of the
[full-tail energy theorem](research_mixed_next_outgoing_full_tail_weighted_energy.md):
\[
\begin{gathered}
D=N-1,\quad M=\lceil N/2\rceil,\quad U=D-M,\quad
\theta=\pi/N,\quad q=e^{i\theta},\quad r=q^{-2},\\
s_b=2\sin(b\theta),\quad S_b=\prod_{\nu=1}^b s_\nu,\quad
Y_b=r^b,\quad
A_b=Y_b(Y_b-1),\\
B_b=3Y_b-(1+r)Y_b^2,\qquad C_b=r^{-1}(1-rY_b)^2,\\
(\mathcal J_Na)_b=-qA_ba_{b-1}+B_ba_b-q^{-1}C_ba_{b+1}.
\end{gathered}                                                     \tag{1}
\]
Keep the closed actual containing region
\[
\mathfrak Z=\left\{\rho e^{-i\alpha}:
 4/5\le\rho\le8/7,\quad3\pi/5\le\alpha\le39\pi/50\right\}.
                                                                    \tag{2}
\]
The original complete words beginning \(343\), of length at least
five, have \(Z_*\in\mathfrak Z\).

The fixed row factors from that source are
\[
w_j=\exp i\{(5j/2+1/4)\theta-\pi/4\},\quad
t_j=(j\theta-\pi/2)/2,\quad
D_\beta=\operatorname{diag}(1+i\beta(t_j)),
                                                                    \tag{3}
\]
where \(-1\le\beta\le3\) is the same fixed smooth interpolation
between the two proved coercive rotations.
For an interval \(I\subseteq[M,D]\), let
\(\mathsf S_I=\operatorname{diag}(\sqrt{S_j})_{j\in I}\), and put
\[
\mathsf A_I=\mathsf S_I D_\beta W_N
              (\mathcal J_{I,N}-ZI)\mathsf S_I^{-1}.
                                                                    \tag{4}
\]
Zero exterior values here apply to the Dirichlet matrix, not to
the original coefficient sequence.

The proof of the full-tail theorem, equations (16),(19)--(21),
retains the stronger quantitative statement
\[
\Re\langle f,\mathsf A_I f\rangle
 \ge\left(\frac{51}{350}-\varepsilon_N\right)\|f\|_2^2,
 \qquad \varepsilon_N\longrightarrow0,
                                                                    \tag{5}
\]
uniformly in the interval and in (2). In fact
\(\varepsilon_N=O(N^{-1})\). Each off-diagonal entry of
\(\mathsf A_I\) has modulus at most
\[
 |1+i\beta(t_j)|\,s_{j+1}^{3/2}\le\sqrt{80}<9.                      \tag{6}
\]
For the lower adjacent entry the corresponding row factor is
used; the same bound holds. No row factor is commuted past a shift.

Here (5) also holds when \(I\) includes \(D\). To see this
directly, \(C_D=0\), \(S_D=N>0\), and
\(t_D=\pi/4-\theta/2\). The exact diagonal and row-phase formulas
of the full-tail proof still hold. Its quadratic estimate includes
the harmless absent-link comparison \(s_{D+1}^{3/2}=s_N^{3/2}=0\);
the Lipschitz estimate for \(s^{3/2}\) is valid at zero.
The row-rotation commutator remains \(O(N^{-1})\).
No metric with weight \(S_N=0\) is formed, and no value at
\(D+1\) is required.

## 2. A finite exponential-conjugation estimate

Set
\[
 R_0=\frac{126}{125},\qquad \gamma_0=\log R_0,\qquad
 E_\pm=\operatorname{diag}(R_0^{\pm j})_{j\in I}.
                                                                    \tag{7}
\]
These symbols are unrelated to the original crossing polynomial.
The diagonal of \(E_\pm\mathsf A_IE_\pm^{-1}\) is unchanged.
For either sign, each row and each column of its difference
from \(\mathsf A_I\) has absolute sum bounded by
\[
9\{(R_0-1)+(1-R_0^{-1})\}
 =9(R_0-R_0^{-1})
 <\frac{18}{125}.
                                                                    \tag{8}
\]
The same bound therefore holds for its Euclidean operator norm.
The strict inequality uses \(1-R_0^{-1}=1/126<1/125\).

The exact remaining reserve is
\[
\frac{51}{350}-\frac{18}{125}=\frac3{1750}.                         \tag{9}
\]
Choose the common level threshold so that
\(\varepsilon_N\le3/3500\). Equations (5),(8) give
\[
\Re\langle f,E_\pm\mathsf A_IE_\pm^{-1}f\rangle
 \ge\frac3{3500}\|f\|_2^2.
                                                                    \tag{10}
\]
Thus both conjugated inverses have norm at most \(3500/3\).
The diagonal row factors commute with \(E_\pm\), and
\(\|D_\beta W_N\|\le\sqrt{10}\). Reversing the sine-metric
conjugation proves the following actual finite estimate.

**Theorem 1.** Uniformly for \(Z\in\mathfrak Z\), both parities,
all sufficiently large \(N\), and every nonempty physical
interval \(I\subseteq[M,D]\),
\[
\boxed{\quad
\left|(\mathcal J_{I,N}-ZI)^{-1}_{i,j}\right|
 \le \frac{3500\sqrt{10}}3
       \sqrt{\frac{S_j}{S_i}}\,
                         R_0^{-|i-j|}.
\quad}                                                            \tag{11}
\]
For \(i\ge j\) use \(E_+\), and for \(i<j\) use \(E_-\).
There is no endpoint exclusion in (11), including as the
last sine tends to zero.

The rate \(\gamma_0\) equals the explicit rate in the
[selected-action transport inequality](research_mixed_next_outgoing_selected_action_transport.md).
Here it follows from (4)--(10) at each finite level.
No selected-branch asymptotic or finite coefficient ratio
was used.

## 3. The actual boundary observation and its finite tail

Return to the exact interval of the original transfer reduction,
\[
 I_N=[M,D-1],\qquad G_N=(\mathcal J_{I_N,N}-ZI)^{-1},\qquad
 \lambda_b=\phi_N(R_N^3e_bQ_N^{\rm full}).
                                                                    \tag{12}
\]
The lower-boundary observation is
\[
v_M=\sum_{b=M}^{D-1}(G_N)_{b,M}\lambda_b .
                                                                    \tag{13}
\]
Every \(\lambda_b\) retains the original full inner Hermite source.

For all sufficiently large levels,
\[
                         S_b\ge S_M\qquad(M\le b\le D).             \tag{14}
\]
Indeed the factors \(s_b\) are at least one until \(5N/6\)
and at most one afterward, so the minimum of this half-range
is at one of its two ends. The exact endpoint products are
\(S_D=N\), \(S_M^2=2N\) at even levels and
\(S_M^2=4N\cos^2(\pi/(2N))\) at odd levels. They imply
\(S_D\ge S_M\) for all sufficiently large \(N\).

For \(1\le\ell\le U\), define
\[
v_M^{<\ell}
  =\sum_{b=M}^{M+\ell-1}(G_N)_{b,M}\lambda_b .
                                                                    \tag{15}
\]
Theorem 1 gives the metric-retaining bound
\[
\boxed{\quad
|v_M-v_M^{<\ell}|
 \le\frac{3500\sqrt{10}}3
 \sum_{b=M+\ell}^{D-1}
       \sqrt{\frac{S_M}{S_b}}\,
       R_0^{-(b-M)}|\lambda_b|.
\quad}                                                            \tag{16}
\]
An empty sum is zero. The full-tail source proof, equations
(28a)--(28b), supplies for each \(\tau>0\)
\[
\max_{M\le b\le D}|\lambda_b|
 \le C_\tau N^{A_\tau}e^{N(\mathfrak M_3+\tau)}.
                                                                    \tag{17}
\]
It uses the complete physical inner packet, its complementary
physical majorant, and the original consumed-normal formula.
Using (14) and the geometric tail in (16) gives
\[
|v_M-v_M^{<\ell}|
 \le C_\tau N^{A_\tau}
          e^{N(\mathfrak M_3+\tau)}R_0^{-\ell}.                    \tag{18}
\]
In particular, a fixed macroscopic deletion \(\ell\ge\delta N\)
gains the rate \(\delta\gamma_0\) in this stated upper bound.
No such deletion of the original source is made without retaining
the finite first sum (15).

To keep the attachment explicit, the full-tail transfer identity is
\[
\mathcal T_0[F_N](-2,Z_*)
 =I_{{\rm geom},N}
   +\frac{qA_Ma_{M-1}(Z_*)}{\kappa_N^2N}v_M
   +O(e^{N(\Lambda-\epsilon_0)}).
                                                                    \tag{19}
\]
Replacing \(v_M\) here by (15) adds at most
\[
\frac{|A_Ma_{M-1}(Z_*)|}{N}\,
 C_\tau N^{A_\tau}
 e^{N(\mathfrak M_3+\tau)}R_0^{-\ell}.
                                                                    \tag{20}
\]
The original signed retained outgoing value \(a_{M-1}\) is
not assigned an unproved rate. The original cutoff forcing
is still the forcing in the full-tail identity; its proved
transformed bound is already part of the error in (19).
Neither it nor the lower exterior value has been dropped.

## 4. A fixed ellipse for the exact Green insertion

Write
\[
P_b^{\rm rad}(\xi)=\frac{e_b(\xi)}{e_M(\xi)}
 =\prod_{h=M}^{b-1}\frac{c_h-\xi}{s_{h+1}^2},
 \qquad c_j=2\cos((2j+1)\theta),
                                                                    \tag{21}
\]
and define exactly as in the
[actual Green-observation theorem](research_mixed_next_boundary_green_positive_metric_obstruction.md)
\[
\begin{split}
\nu_N(\xi,Z)&=\sum_{b=M}^{D-1}(G_N)_{b,M}P_b^{\rm rad}(\xi),\\
\nu_N^{<\ell}(\xi,Z)
 &=\sum_{b=M}^{M+\ell-1}(G_N)_{b,M}P_b^{\rm rad}(\xi).
\end{split}                                                       \tag{22}
\]
Their degrees are at most \(U-1\) and \(\ell-1\), respectively.
For every double node \(c_j\), the full-tail source proves
\[
|P_b^{\rm rad}(c_j)|\le C N^2.                                    \tag{23}
\]
Its proof keeps the exact zeros: the product is zero if \(j>D-b\);
otherwise \(|c_h-c_j|\le s_h^2\) telescopes to
\(s_M^2/s_b^2\le CN^2\). Hence (11),(14) imply
\[
\max_{0\le j\le U}
 |\nu_N(c_j,Z)-\nu_N^{<\ell}(c_j,Z)|
             \le C N^2R_0^{-\ell}.                               \tag{24}
\]

The original cardinal interpolation on these \(U+1=m\) double
nodes has polynomial norm at both parities. Explicitly the monic
node polynomials are \(2T_m(\xi/2)\) at \(N=2m\) and
\(U_m(\xi/2)-U_{m-1}(\xi/2)\) at \(N=2m+1\).
The derivative and Markov bounds in
[the slit-plane theorem, Section 6](research_mixed_next_first_short_edge_slit_plane_bound.md)
give cardinal norms at most \(m\) and \(2m^2\), respectively.
Summing the \(m\) cardinal norms and applying exact interpolation
to the degree-at-most-\(U-1\) difference in (24) yields
\[
\boxed{\quad
\|\nu_N-\nu_N^{<\ell}\|_{[-2,2]}
                  \le C N^5 R_0^{-\ell}.
\quad}                                                            \tag{25}
\]
The same argument, summing (22) from \(b=M\), gives
\(\|\nu_N\|_{[-2,2]}\le CN^5\).

Expand the exact polynomial in the ordinary Chebyshev basis:
\[
\nu_N(\xi,Z)=\sum_{k=0}^{U-1}\widehat\nu_{k,N}(Z)T_k(\xi/2).
\]
For \(k\ge1\), take \(\ell=k\) in (25). Since
\(\deg\nu_N^{<k}<k\), the \(k\)-th coefficient is unchanged
by that subtraction. The elementary cosine-coefficient bound,
and the preceding real norm for \(k=0\), give
\[
\boxed{\quad
|\widehat\nu_{k,N}(Z)|\le C N^5R_0^{-k},
                       \qquad0\le k\le U-1.
\quad}                                                            \tag{26}
\]
Let \(\mathcal E_{\gamma_0}\) be the filled ellipse bounded by
\(\xi=2\cos(\vartheta+i\gamma_0)\).
The identity \(T_k(\cos z)=\cos(kz)\) and (26) imply
\[
\boxed{\quad
\sup_{\xi\in\mathcal E_{\gamma_0}}|\nu_N(\xi,Z)|\le CN^6.
\quad}                                                            \tag{27}
\]
The filled version follows from the maximum-modulus principle.
Every fixed spectral derivative has a polynomial bound on a
strictly smaller ellipse, by Cauchy's formula. This proves a
source-specific analytic ceiling for the actual insertion, not
just an arbitrary bounded vector of physical values.

The exact central value is still
\[
                   \nu_N(c_U,Z)=\nu_N^{<\ell}(c_U,Z)=G_{M,M}
                              \qquad(\ell\ge1).
                                                                    \tag{28}
\]
More generally, the remainder in (22) vanishes at
\(c_U,c_{U-1},\ldots,c_{U-\ell+1}\): every term with
\(b\ge M+\ell\) contains each corresponding reflected Newton
zero. This is an exact statement about the remainder, not an
estimate discarding any of the first \(\ell\) contributions.

The original signed pairing is
\[
v_M=\phi_N[R_N^3e_MQ_N^{\rm full}\nu_N]
     =\sum_{j=0}^{U}\mu_{j,N}Q_N^{\rm full}(c_j)\nu_N(c_j,Z).
                                                                    \tag{29}
\]
All crossing phases and both-parity consumed-normal weights
remain those of its source. The nonzero complete-node value
(28) and the original complete inner packet remain present.
The actual Green-observation theorem proves that every positive
nodal Cauchy estimate for (29) still has rate at least
\(\mathfrak M_3\). Thus (27) is analytic regularity, not a
bound at the required preceding-factor rate.

No finite packet, relative coefficient asymptotic, signed outer
suppression, or finite-exception theorem follows from this
localization alone.

## Source versions

- Full-tail finite energy and original boundary reduction:
  0037a31d5f2a8cedea53d70bf1f0434f906668fe0934e5ee303890a8b3eceee7.
- Selected action transport, used only to identify the matching rate:
  77ffb14e6f3a3408b4aee3594d1c205b9db61fccdbf011181de9f86c26e9dbd5.
- Exact Green insertion and positive-metric limitation:
  518de800d265868ede37b7ec858b28c45d1ff9006d7d26b85899f1e174d795f8.
- Original double-node cardinal interpolation:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.

