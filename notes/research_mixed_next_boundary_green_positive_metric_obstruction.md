# The actual boundary Green observation still requires cancellation

Private exact-source deduction, 8 November 2026. The remaining
Green observation is an original radical trace with a specified
resolvent-dependent polynomial insertion. Its value at the last
double node is uniformly nonzero. Consequently every positive
nodal Cauchy estimate for this actual observation still has the
complete inner exponential cost \(\mathfrak M_3\).

This is a limitation of the stated positive-metric estimate. It is
not a lower bound for the signed Green observation or for its
product with the original outgoing boundary value. No mathematical
numerical evaluation or frozen-source edit is used.

## 1. The actual unresolved observation

Keep all notation, signs, and normalizations of
[the full-tail weighted-energy theorem](research_mixed_next_outgoing_full_tail_weighted_energy.md):
\[
\begin{gathered}
D=N-1,\quad M=\lceil N/2\rceil,\quad U=D-M=\lfloor N/2\rfloor-1,\\
\theta=\pi/N,\quad q=e^{i\theta},\quad r=q^{-2},\quad
\kappa=q^{D^2/2},\quad I_N=[M,D-1]\cap\mathbb Z,\\
c_j=2\cos((2j+1)\theta),\quad
s_j=2\sin(j\theta),\quad S_j=\prod_{\nu=1}^j s_\nu,\\
G_N(Z)=(\mathcal J_{I_N,N}-ZI)^{-1},\qquad
\lambda_b=\phi_N(R_N^3e_bQ_N^{\rm full}),\qquad
v=G_N(Z)^{\rm t}\lambda .
\end{gathered}                                                     \tag{1}
\]
The transpose is bilinear. The output remains in the original
actual containing region
\[
Z=\rho e^{-i\alpha},\qquad
4/5\le\rho\le8/7,\qquad3\pi/5\le\alpha\le39\pi/50.
                                                                    \tag{2}
\]
For actual complete words beginning \(343\), of length at least
five, that source reduces the remaining transfer correction to
\[
\frac{qA_M}{\kappa^2N}\,a_{M-1}(Z)v_M(Z),
\qquad
v_M(Z)=\sum_{b=M}^{D-1}G_N(Z)_{b,M}\lambda_b,
                                                                    \tag{3}
\]
up to its proved exponentially smaller error. Here \(a_{M-1}\)
is the original signed outgoing sum with its specified small-index
cutoff. It is not an arbitrary exterior datum in the transfer.
All statements below concern exactly the second factor in (3);
the first factor and their phase correlation remain intact.

Use the ordinary radical quotients
\[
P_b^{\rm rad}(\xi)=\frac{e_b(\xi)}{e_M(\xi)}
 =\prod_{h=M}^{b-1}\frac{c_h-\xi}{s_{h+1}^{\,2}},\qquad b\ge M .
                                                                    \tag{4}
\]
The displayed product defines a polynomial, including at every
zero of \(e_M\). Define the actual Green insertion
\[
\boxed{\qquad
\nu_N(\xi,Z)=\sum_{b=M}^{D-1}G_N(Z)_{b,M}P_b^{\rm rad}(\xi).
\qquad}                                                           \tag{5}
\]
It has degree at most \(U-1\) in \(\xi\), with coefficients
holomorphic in \(Z\) on a neighborhood of (2). The inverse exists
uniformly there by the strict full-tail energy bound.

The exact original radical formula gives
\[
\boxed{\quad
v_M(Z)=\phi_N[R_N^3e_MQ_N^{\rm full}\nu_N(\,\cdot\,,Z)]
      =\sum_{j=0}^{U}\mu_{j,N}q_{j,N}\nu_N(c_j,Z),
\quad}                                                            \tag{6}
\]
where \(q_{j,N}=Q_N^{\rm full}(c_j)\) and
\[
\mu_{j,N}=(-1)^U\kappa^3\omega_{j,N}q^{3j(j+1)},\qquad
\omega_{j,N}=
\begin{cases}
\sin((2j+1)\theta),&N=2m,\\[1mm]
\displaystyle
\frac{\sin((2j+1)\theta)\sin((m-j)\theta)}
     {\cos^2(\theta/2)},&N=2m+1 .
\end{cases}                                                       \tag{7}
\]
These are the full consumed-normal weights in
[the Casimir observation, equations (15)--(17)](research_mixed_next_three_outer_casimir_observation.md).
There is no additional normal or odd simple-node summand.
Equation (6) follows by linearity before taking any absolute value.

## 2. A nonzero central value of the actual Green insertion

At the last double node \(c_U=c_M\), every polynomial (4) with
\(b>M\) contains the factor \(c_M-\xi\). Therefore
\[
                         \nu_N(c_U,Z)=G_N(Z)_{M,M}.                \tag{8}
\]
The following lower bound is a consequence of the proved
coercivity, and does not require estimating a determinant.

Let \(\mathsf S=\operatorname{diag}(\sqrt{S_b})_{b\in I_N}\).
Use exactly the row phase \(W_N\) and smooth row rotation
\(D_\beta\) of the full-tail theorem, and put
\[
\mathsf A_N=\mathsf S D_\beta W_N
                     (\mathcal J_{I_N,N}-ZI)\mathsf S^{-1}.
                                                                    \tag{9}
\]
That theorem proves
\[
\Re\langle f,\mathsf A_Nf\rangle\ge\frac1{20}\|f\|_2^2,
\qquad \|\mathsf A_N\|_{2\to2}\le60.                               \tag{10}
\]
For the second inequality, every entry has modulus below \(20\)
and there are at most three entries in each row and column.
These estimates are uniform at both parities and throughout (2).

Set \(y=\mathsf A_N^{-1}\mathbf e_M\). Then
\(\|y\|_2\ge1/60\), and the real parts of
\(\langle\mathbf e_M,\mathsf A_N^{-1}\mathbf e_M\rangle\)
and \(\langle y,\mathsf A_Ny\rangle\) agree. Thus
\[
\Re(\mathsf A_N^{-1})_{M,M}
 \ge\frac1{20}\|y\|_2^2\ge\frac1{72000}.
                                                                    \tag{11}
\]
At the lower endpoint \(M\), the fixed interpolation has
\(\beta(t_M)=3\) for all sufficiently large \(N\). Since all
other factors in (9) are diagonal,
\[
G_N(Z)_{M,M}=(1+3i)w_M(\mathsf A_N^{-1})_{M,M},
\qquad |w_M|=1 .
                                                                    \tag{12}
\]
Together with the original inverse upper bound, this proves
\[
\boxed{\qquad
\frac{\sqrt{10}}{72000}
 \le|\nu_N(c_U,Z)|=|G_N(Z)_{M,M}|
 \le20\sqrt{10}.
\qquad}                                                           \tag{13}
\]
Only the rotated inverse diagonal has a positive real part in
(11). Neither \(G_N(Z)_{M,M}\) itself nor the weights in (6)
are asserted positive.

## 3. The complete inner source at that node

The exact angle of the node in (8) is
\[
u_{U,N}=
\begin{cases}
\pi/N,&N\ {\rm even},\\
2\pi/N,&N\ {\rm odd}.
\end{cases}                                                       \tag{14}
\]
Both are double nodes. The odd simple angle zero is not used.
The adopted
[complete physical packet](research_mixed_next_inner_three_physical_outgoing_packet.md)
and its original even action near zero give
\[
q_{U,N}=C_{N,3}N^{-3/2}\mathcal A(u_{U,N})
                     e^{NS_3(0,u_{U,N})}(1+O(N^{-1})),
\quad |C_{N,3}|=1,
                                                                    \tag{15}
\]
\[
|\mathcal A(u_{U,N})|\ge c>0,\qquad
S_3(0,u_{U,N})=S_3(0,0)+O(N^{-2}),\qquad
\mathfrak M_3=\Re S_3(0,0)>9/5 .
                                                                    \tag{16}
\]
These precise source facts, including the phase constant, are
traced in
[the self-adjoint norm obstruction, equations (16)--(20)](research_mixed_next_outer_self_adjoint_norm_obstruction.md).
In particular
\[
|q_{U,N}|\ge cN^{-3/2}e^{N\mathfrak M_3}.
                                                                    \tag{17}
\]
The measure at the same node is exactly
\[
|\mu_{U,N}|=
\begin{cases}
\sin\theta,&N\ {\rm even},\\
\sin(2\theta)\sin\theta/\cos^2(\theta/2),&N\ {\rm odd}.
\end{cases}                                                       \tag{18}
\]
The sine chord gives a common lower bound \(cN^{-2}\) at
all sufficiently large levels. Combining (13), (17), and (18),
\[
\boxed{\quad
|\mu_{U,N}\nu_N(c_U,Z)q_{U,N}|
 \ge cN^{-7/2}e^{N\mathfrak M_3}.
\quad}                                                            \tag{19}
\]
This is a lower bound for one absolute summand, not for (6).
It uses the entire inner physical source with its nonzero
coefficient, not an unsigned approximation of that source.

## 4. What positive metrics and almost-invariance do not provide

For any positive weights \(\omega_j\), which may depend on
\(N,Z\), define the nodal norm
\[
\|p\|_\omega^2=\sum_{j=0}^{U}\omega_j|p(c_j)|^2
\]
and the actual Green functional
\[
\ell_{\nu,Z}(p)=\sum_{j=0}^{U}\mu_{j,N}\nu_N(c_j,Z)p(c_j).
                                                                    \tag{20}
\]
The Cauchy cost of bounding (6) by this norm is
\[
\mathfrak C_N(\omega,Z)
 =\left(\sum_{j=0}^{U}
          \frac{|\mu_{j,N}\nu_N(c_j,Z)|^2}{\omega_j}\right)^{1/2}
  \left(\sum_{j=0}^{U}\omega_j|q_{j,N}|^2\right)^{1/2}.
                                                                    \tag{21}
\]
For every such choice, Cauchy's inequality in the opposite
direction gives
\[
\mathfrak C_N(\omega,Z)
 \ge\sum_{j=0}^{U}|\mu_{j,N}\nu_N(c_j,Z)q_{j,N}|.
                                                                    \tag{22}
\]
The right-hand side is also the infimum of (21): at nonzero
components choose
\(\omega_j=|\mu_{j,N}\nu_N(c_j,Z)|/|q_{j,N}|\), and approach
the appropriate zero or infinite weights at zero components.
This limiting statement does not require nonzero values at all
nodes.

Equations (19)--(22) prove, uniformly over (2),
\[
\boxed{\quad
\inf_{\omega_j>0}\mathfrak C_N(\omega,Z)
 \ge cN^{-7/2}e^{N\mathfrak M_3}.
\quad}                                                            \tag{23}
\]
The positive self-adjoint realizations of the reduced ordinary
Casimir are exactly these nodal metrics: its distinct real
eigenvalues force orthogonality of different cardinal vectors.
This classification, proved in the cited self-adjoint norm
source, therefore applies to the actual insertion (5), not
just to its constant mode. In particular it cannot give a bound
for \(v_M\) at the preceding-factor ceilings \(17/10\) or
\(B_f=77/50+\pi/50<9/5\).

The weighted outgoing energy is a different and valid positivity
statement. It proves for zero-exterior vectors on \(I_N\)
\[
\|(\mathcal J_{I_N,N}-ZI)f\|_S
 \ge\frac1{20\sqrt{10}}\|f\|_S.
                                                                    \tag{24}
\]
Thus it excludes almost-null vectors in that specified metric
and boundary realization. The actual retained outgoing source
instead has the exact residual
\[
(\mathcal J_{I_N,N}-ZI)a
       =-f+qA_Ma_{M-1}\mathbf e_M,
                                                                    \tag{25}
\]
with the original cutoff forcing and exterior value. Neither
(24) nor (25) turns the signed bilinear pairing (6) into a
positive quadratic form or supplies a small overlap with it.
The modulus and phase of the boundary value in (3) remain
those of the original source.

If (21) is used to estimate the complete boundary product,
its best possible cost has the lower bound
\[
\frac{|qA_Ma_{M-1}|}{N}
       \inf_{\omega>0}\mathfrak C_N(\omega,Z)
 \ge cN^{-9/2}|A_Ma_{M-1}|e^{N\mathfrak M_3}.
                                                                    \tag{26}
\]
No positive lower exponential rate for \(a_{M-1}\) is assumed
or inferred here. Accordingly (26) does not compare the actual
product with \(\Lambda\), and does not show failure of a
phase-correlated estimate. It identifies precisely the large
central contribution that such an estimate must retain.

The general finite-exception goal still requires stability of
the complete partially filled source with its nonzero geometric
coefficient and all competing terms controlled. This
reference-specific obstruction neither proves nor disproves
that stability theorem.

## Source versions

- Full-tail outgoing energy:
  0037a31d5f2a8cedea53d70bf1f0434f906668fe0934e5ee303890a8b3eceee7.
- Original weighted energy:
  fdcc1fab386fd94047022c04911d0f5874768674dd546aef33985b54a758b372.
- Original radical observation:
  cbbc62951666d06e0ae77b29f49f563d91c2024dc8da900ae996144d7db39dab.
- Complete physical packet:
  c43064953e7d3bfa92a6ecc05725719661e45d0b6bfca76fe1b78a28c68de4f3.
- Positive self-adjoint norm source:
  ddad67e85205d7d637ea4ab156f4e67938aacdc6aaed86213e8128d55d8a1849.

All source identities and inequalities were checked statically.
