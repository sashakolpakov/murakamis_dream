# The entire transformed outgoing cutoff forcing is exponentially smaller

Private finite-source theorem, 8 November 2026. The weighted outgoing
inverse can be paired with the complete original inner periods at an
adequate rate. This pays its entire transformed cutoff forcing, over
the full physical middle interval, and leaves exactly two exterior
Green observations. The proof keeps the sine-product metric, the
original signed outgoing recurrence, and the consumed radical normal.
It uses no mathematical numerical evaluation or frozen-source edit.

## 1. Original source and statement

Use the notation of
[the weighted energy theorem, equations (1)--(3)](research_mixed_next_outgoing_weighted_energy.md):
\[
\begin{gathered}
D=N-1,\quad \theta=\pi/N,\quad q=e^{i\theta},\quad r=q^{-2},
\quad\kappa=q^{D^2/2},\\
M=\lceil N/2\rceil,\quad U=D-M=\lfloor N/2\rfloor-1,\quad
L=\lfloor N/6\rfloor,\quad K=\lfloor N/4096\rfloor,\\
B=D-L,\qquad I=[M,B]\cap\mathbb Z,\qquad
s_j=2\sin(j\theta),\quad S_j=\prod_{\nu=1}^j s_\nu,\\
Y_b=r^b,\quad P_k=(r;r)_k,\quad p_k(Z)=(rZ;r)_k,\\
A_b=Y_b(Y_b-1),\quad B_b=3Y_b-(1+r)Y_b^2,\quad
C_b=r^{-1}(1-rY_b)^2 .
\end{gathered}                                                     \tag{1}
\]
The index endpoint \(B\) is distinct from the operator coefficient
\(B_b\). Retain exactly
\[
\begin{split}
a_b(Z)&=(-q)^b\sum_{k=K+1}^{D}
              \frac{Y_b^{-k}p_k(Y_b)p_k(Z)}{P_k^2},\\
f_b(Z)&=(-q)^b r^{-K-1}(1-r^{K+1}Z)
              \frac{Y_b^{-K}p_K(Y_b)p_K(Z)}{P_K^2},\\
(\mathcal J_Na)_b&=-qA_ba_{b-1}+B_ba_b-q^{-1}C_ba_{b+1},
\qquad Za_b=(\mathcal J_Na)_b+f_b,\\
\lambda_b&=\phi_N(R_N^3e_bQ_N^{\rm full}).
\end{split}                                                       \tag{2}
\]
All rows above their physical stop \(D-b\) vanish exactly. The last
line is the original full inner period, not a shortened or
pointwise asymptotic replacement.

The actual application is an original complete word in powers three
and four beginning \(343\), of length at least five, at its base
outside values \(w=-2,Z=Z_*\). In particular
\[
Z=\rho e^{-i\alpha},\qquad
\frac45\le\rho\le\frac87,\qquad
\frac{3\pi}{5}\le\alpha\le\frac{39\pi}{50},\qquad
\Lambda=\Re\mathcal P_*>419/200 .                                  \tag{3}
\]
The estimates below are uniform on the closed containing \(Z\)
region. Write
\[
G=(\mathcal J_{I,N}-ZI)^{-1},\qquad
v=G^{\rm t}\lambda_I .
                                                                    \tag{4}
\]
The transpose is bilinear, with \(Z\) unchanged.

**Theorem.** At all sufficiently large levels of both parities,
\[
\boxed{\qquad
\left|\frac1{\kappa^2N}\sum_{b=M}^{B}v_bf_b\right|
 \le C\exp N\left(\frac{419}{200}-\frac1{25}\right).
\qquad}                                                           \tag{5}
\]
Consequently the complete original middle observation satisfies
\[
\begin{split}
\frac1{\kappa^2N}\sum_{b=M}^{B}\lambda_ba_b
={}&\frac{qA_Ma_{M-1}}{\kappa^2N}
                          \sum_{i=M}^{B}G_{i,M}\lambda_i\\
 &+\frac{q^{-1}C_Ba_{B+1}}{\kappa^2N}
                          \sum_{i=M}^{B}G_{i,B}\lambda_i
 +O\!\left(e^{N(419/200-1/25)}\right).
\end{split}                                                       \tag{6}
\]
Both exterior values and both coherent Green observations in (6)
remain unestimated at the required volume rate. In particular (5)
is a bound for the forcing after the inverse, rather than an
application of a bound for the different pairing
\(\sum\lambda_bf_b\).

## 2. A uniform complete physical inner bound

For \(0\le j\le U\), set
\[
c_j=2\cos((2j+1)\pi/N)=-2\cos u_{j,N},\qquad
u_{j,N}=\pi-(2j+1)\pi/N,
\qquad q_{j,N}=Q_N^{\rm full}(c_j).
                                                                    \tag{7}
\]
Here \(q_{j,N}\) is an inner value, not the quantum parameter \(q\).
Every such node is a double node of the original Hermite trace.
The possible odd simple node is not included.

The exact physical-row identity in
[the physical outgoing packet, equations (1), (4), and (5)](research_mixed_next_inner_three_physical_outgoing_packet.md)
identifies \(q_{j,N}\) with that theorem's complete inner trace:
the second full kernel terminates at \(j\), and hence equals its
shortened kernel as an ordinary polynomial. The first edge and
the inner Hermite trace remain full. For \(0<u_{j,N}\le\pi/2\),
the adopted uniform packet therefore gives the upper bound
\[
|q_{j,N}|\le C N^A e^{Ns(u_{j,N})},\qquad
s(u)=\Re S_3(0,u).                                                 \tag{8}
\]
Only this upper consequence is used; no relative packet error is
dropped inside a coherent observation.

On the real interval \(0\le u\le\pi/2\),
[cubic continuation, equation (8)](research_mixed_next_inner_three_cubic_continuation.md)
gives, on the original branch,
\[
S_3'(0,u)=-\frac1\pi\operatorname{arsinh}
             \left(\cos(t_*(u)/2)\tan(u/2)\right),\qquad
0<\Re t_*(u)<\pi/2,\quad -1<\Im t_*(u)<0 .
                                                                    \tag{9}
\]
The argument of the principal return has positive real part for
\(u>0\). Its principal \(\operatorname{arsinh}\) has positive real
part: if \(w=\operatorname{arsinh}z\), its principal imaginary part
lies between \(-\pi/2\) and \(\pi/2\), and
\(\Re z=\sinh(\Re w)\cos(\Im w)>0\) forces \(\Re w>0\).
Thus \(s\) decreases on this interval, with
\[
s(u)\le s(0)=\mathfrak M_3<121/63.                                \tag{10}
\]
The strict upper bound is the original action estimate
[proved here](research_inner_three_complete_action_upper_bound.md);
it retains the original additive constant.

For the remaining physical nodes \(u_{j,N}\ge\pi/2\),
[the complete upper-physical majorant, equation (3)](research_mixed_next_inner_three_upper_physical_majorant.md)
gives, for every fixed \(\tau>0\),
\[
|q_{j,N}|\le C_\tau
 e^{N\{s(\pi/2)-\kappa_0(u_{j,N}-\pi/2)+\tau\}},
\qquad \kappa_0>0 .
                                                                    \tag{11}
\]
Equations (8)--(11) prove the full physical bound
\[
\boxed{\quad
\max_{0\le j\le U}|q_{j,N}|
 \le C_\tau N^{A_\tau}e^{N(\mathfrak M_3+\tau)} .
\quad}                                                            \tag{12}
\]
This includes both physical endpoints and both parities. It is not
an off-grid bound or an extension of the physical packet.

## 3. The exact radical quotient has no exponential cost

The original Newton normalization is
\[
e_b(w)=S_b^{-2}\prod_{h=0}^{b-1}(c_h-w),\qquad
P_b^{\rm rad}(w)=\frac{e_b(w)}{e_M(w)}
 =\prod_{h=M}^{b-1}\frac{c_h-w}{s_{h+1}^{\,2}},\qquad b\ge M .
                                                                    \tag{13}
\]
The last expression is an ordinary polynomial, so no quotient at a
root is taken. For \(j>D-b\), \(P_b^{\rm rad}(c_j)=0\):
the factor \(h=D-j\) lies between \(M\) and \(b-1\), and
\(c_h=c_j\). For \(j\le D-b\), one has
\[
c_j\ge c_{D-b}=c_b>c_h\quad(M\le h<b).
\]
The sequence \(c_h\) increases on this latter index interval.
Consequently
\[
|c_h-c_j|\le2-c_h
 =4\sin^2((h+1/2)\theta)\le s_h^2,
                                                                    \tag{14}
\]
since \(h\ge N/2\) and sine decreases up to \(\pi\).
The denominator in (13) is \(s_{h+1}^2\), so the correct bound
telescopes:
\[
|P_b^{\rm rad}(c_j)|
 \le\frac{s_M^2}{s_b^2}\le4,\qquad M\le b\le B .
                                                                    \tag{15}
\]
Here \(B<5N/6\), hence \(s_b\ge1\); the empty product at \(b=M\)
also obeys (15).

Use the exact consumed-normal formula in
[the Casimir observation, equations (15)--(16)](research_mixed_next_three_outer_casimir_observation.md):
\[
\lambda_b=\sum_{j=0}^{U}\mu_{j,N}
                       P_b^{\rm rad}(c_j)q_{j,N},\qquad
\mu_{j,N}=(-1)^U\kappa^3s_{2j+1}A_{j,N}q^{3j(j+1)},
                                                                    \tag{16}
\]
where, writing \(m=\lfloor N/2\rfloor\),
\[
A_{j,N}=
\begin{cases}
1/2,&N=2m,\\
s_{m-j}/\{4\cos^2(\pi/(2N))\},&N=2m+1 .
\end{cases}
                                                                    \tag{17}
\]
In particular \(|\mu_{j,N}|\le2\) for all sufficiently large
levels. This is the original crossing phase and the full consumed
normal; there is no omitted odd simple-node term. Combining
(12), (15), and (16) proves
\[
\max_{M\le b\le B}|\lambda_b|
 \le C_\tau N^{A_\tau}e^{N(\mathfrak M_3+\tau)} .
                                                                    \tag{18}
\]
Absolute values are taken only after the complete inner source
\(q_{j,N}\) has been bounded.

## 4. The metric costs and all transformed forcing

For every \(b\in I\), each added factor from \(S_M\) to \(S_b\)
lies between one and two. Also
\(B-M=U-L<N/3\), with the literal rounded endpoints. Thus
\[
S_M\le S_b\le S_M2^{b-M}\le S_M2^{N/3}.                            \tag{19}
\]
For reference, the exact half-factorials are
\[
S_M^2=2N\quad(N\ {\rm even}),\qquad
S_M^2=4N\cos^2(\pi/(2N))\quad(N\ {\rm odd}).
                                                                    \tag{20}
\]
In fact their common factor will cancel below.

The exact row estimate in
[small outgoing indices, equations (9)--(13)](research_mixed_next_three_small_outgoing_indices.md)
applies at \(k=K\). The extra factor in \(f_b\) has modulus at
most \(15/7\), so
\[
|f_b|\le(15/7)e^{N/200}\quad(b\in I).
                                                                    \tag{21}
\]
If a physical numerator row is zero, this inequality still holds.
Every phase in (2) has modulus one at the physical incoming node.

Let \(\|\cdot\|_S^2=\sum_{b\in I}S_b|\cdot|^2\), and use its
dual norm with weights \(S_b^{-1}\). Equations (18)--(21) give
\[
\begin{split}
\|\lambda_I\|_{S^{-1}}
 &\le C_\tau N^{A_\tau}S_M^{-1/2}
                       e^{N(\mathfrak M_3+\tau)},\\
\|f_I\|_S
 &\le C N^{1/2}S_M^{1/2}
                   e^{N\{1/200+(\log2)/6\}} .
\end{split}                                                       \tag{22}
\]
The adopted weighted inverse has
\[
\|v\|_{S^{-1}}\le20\sqrt{10}\|\lambda_I\|_{S^{-1}} .
                                                                    \tag{23}
\]
This is the bilinear-transpose version of the actual inverse
bound, not a positivity assertion about the period sequence.
Cauchy's inequality and \(|\kappa|=1\) now imply
\[
\left|\frac1{\kappa^2N}\sum v_bf_b\right|
 \le C_\tau N^{A_\tau}
 \exp N\{\mathfrak M_3+\tau+1/200+(\log2)/6\}.
                                                                    \tag{24}
\]
In particular both \(S_M\) factors cancel, while the full remaining
factorial cost \((\log2)/6\) is retained.

The small-index source includes the written witness
\(\log2<7/10\). Together with (10), this yields the exact budget
\[
\frac{419}{200}
 -\left(\frac{121}{63}+\frac7{60}+\frac1{200}\right)
 =\frac{83}{1575}>\frac1{20}>\frac1{25}.
                                                                    \tag{25}
\]
Choose the fixed \(\tau\) and the eventual polynomial allowance
inside the strict remaining margin. Equation (24) then proves (5).
No estimate for the literal pairing \(\sum\lambda_bf_b\) was used.

## 5. Exact remaining boundary observations

The source restriction, with the original exterior values, is
\[
(\mathcal J_{I,N}-ZI)a_I
 =-f_I+qA_Ma_{M-1}\mathbf e_M+q^{-1}C_Ba_{B+1}\mathbf e_B.
                                                                    \tag{26}
\]
Pairing with (4) gives exactly
\[
\sum_{b=M}^{B}\lambda_ba_b
 =-\sum_{b=M}^{B}v_bf_b
             +qA_Mv_Ma_{M-1}+q^{-1}C_Bv_Ba_{B+1}.
                                                                    \tag{27}
\]
This proves (6), including both signs and the original scalar.
Neither exterior value is assigned zero.

The exterior stops are
\[
D-(M-1)=U+1=\lfloor N/2\rfloor,\qquad
D-(B+1)=L-1 .
                                                                    \tag{28}
\]
For clarity, the positive envelope of
[the outgoing attachment budget, equations (3)--(6)](research_mixed_next_physical_three_outgoing_attachment_budget.md)
therefore gives
\[
\begin{split}
|a_{M-1}|&\le
 \exp\{N\mathcal E_C((U+1)/N,Z)+O(\log N)\},\\
|a_{B+1}|&\le
 \exp\{N\mathcal E_C((L-1)/N,Z)+O(\log N)\},
\end{split}                                                       \tag{29}
\]
where
\[
\mathcal E_C(\delta,Z)=
\max_{0\le t\le\delta}
\left\{J(\delta)-J(\delta-t)-2J(t)
                +\int_0^t\log|1-Ze^{-2\pi is}|\,ds\right\},
\quad J(t)=\int_0^t\log(2\sin\pi s)\,ds .
                                                                    \tag{30}
\]
The estimates concern the complete positive envelopes, and so
bound the retained high-\(k\) subsets as well.

The actual quantities to control are the coherent
\[
v_M=\sum_{i=M}^{B}G_{i,M}\lambda_i,\qquad
v_B=\sum_{i=M}^{B}G_{i,B}\lambda_i .
                                                                    \tag{31}
\]
For example, the existing entry estimate gives
\[
\begin{split}
|v_M|&\le40\sqrt{10}\sum_{i=M}^{B}
       e^{-\gamma(i-M)}\sqrt{S_M/S_i}\,|\lambda_i|,\\
|v_B|&\le40\sqrt{10}\sum_{i=M}^{B}
       e^{-\gamma(B-i)}\sqrt{S_B/S_i}\,|\lambda_i|,
\qquad \gamma=\log(1+1/2400)>0 .
\end{split}                                                       \tag{32}
\]
These metric ratios and the exterior costs (29) remain part of
the problem. No adequate volume-rate bound for either product in
(27) is deduced here. In particular the adopted bound on an
original high physical tail does not itself estimate its
transformed boundary observation \(v_Ba_{B+1}\).

The complete-transfer reduction and all its already bounded
contours and filter terms remain unchanged. This theorem removes
the whole transformed cutoff forcing from that exact finite
obstruction; it does not yet prove the required outer suppression
or noncancellation of the complete transfer.

## Source versions

- Weighted outgoing energy:
  fdcc1fab386fd94047022c04911d0f5874768674dd546aef33985b54a758b372.
- Paired Newton characteristics:
  8372ed7387b7465b6a66cc207f2ac8e3803e3def10d7beff115c038d4334c909.
- Physical inner packet:
  c43064953e7d3bfa92a6ecc05725719661e45d0b6bfca76fe1b78a28c68de4f3.
- Upper physical inner majorant:
  6fd4d8c0d67e184312f0d1106b112ac00a965f7d40716aae8ac7b502eb709c18.
- Complete action upper bound:
  7ef8adaa33c1fed792379d4ead3aef70cb4e704816b6979fb1f156fe16b07a9d.
- Cubic continuation:
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.
- Radical Casimir observation:
  cbbc62951666d06e0ae77b29f49f563d91c2024dc8da900ae996144d7db39dab.
- Small outgoing indices:
  6905d51ca102e2686d9b9845cfe333017ddcbcf45a70dbcf10741438f31dc1f0.
- Outgoing attachment budget:
  dc10368628b9426fddbf2c74ae55ee1e288af6953b7bf5a53cad255ad95897aa.

All comparisons are written exact source identities or inequalities.
No mathematical numerical evaluation or modification of a frozen
source was performed.
