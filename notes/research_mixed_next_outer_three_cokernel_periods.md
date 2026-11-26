# Three exact cokernel periods for the constrained outer adjoint

Private finite-source deduction, 8 November 2026. The global
constrained radical operator is injective and has an image of
codimension three at both parities. Its cokernel is described by
three explicitly normalized solutions of the original seven-term
recurrence. These solutions retain the physical far endpoint and
omit only the three central equations that would expose normals.

The resulting exact reduction of the actual outer observation does
not give a uniformly bounded inverse on that image. Its natural
projection onto three far-node remainders is exponentially
ill-conditioned on the odd subsequence, by already proved estimates
for the actual inner source. This is a limitation of that projection
norm, not a lower bound for the signed outer observation or a
counterexample to an inverse estimate on the image. No mathematical
numerical evaluation or frozen-source edit is used.

## 1. Original full algebra and the constrained map

Use
\[
\begin{gathered}
N\ge6,\quad m=\lfloor N/2\rfloor,\quad U=m-1,\quad
M=\lceil N/2\rceil,\quad D=N-1,\quad
\theta=\pi/N,\quad q=e^{i\theta},\\
\eta=(-1)^D,\quad \kappa=q^{D^2/2},\quad
c_j=2\cos((2j+1)\theta),\quad
s_j=2\sin(j\theta),\quad S_j=\prod_{\nu=1}^j s_\nu,\quad S_0=1,\\
\mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2).
\end{gathered}                                                     \tag{1}
\]
There are \(m\) double nodes \(c_0,\ldots,c_U\); odd levels
also have the simple node \(-2\). All turns, crossings, Newton
polynomials, and Frobenius traces have their original normalization.

Write
\[
\mathcal D_N
 =q^{-2}(\mathcal L^2-I)\mathcal L_1
       +q^{-3}\mathcal L Z-8q^{-2}\mathcal L+(8q^{-1}+2)I,
                                                                    \tag{2}
\]
as in [the seven-term source, equations (5)--(7)](research_mixed_next_physical_inner_seven_term_recurrence.md).
Its actual full output \(Q_N\) satisfies
\[
\mathcal D_NQ_N=\mathfrak f_N1,\qquad
\mathfrak f_N=
\begin{cases}
4\kappa^3/N^2,&N\text{ even},\\
0,&N\text{ odd}.
\end{cases}                                                       \tag{3}
\]
The off-grid ordinary identity retains its multiple of \(P_N\);
only the full-algebra statement is used here.

The original radical is \(e_M\mathcal A_N\). Set
\[
\begin{split}
\mu_j&=\eta(4-c_j^2)R(c_j)^3e_M'(c_j)\ne0,\\
\mathscr X_N&=\{h=(h_0,\ldots,h_U):
                       h_U=h_{U-1}=h_{U-2}=0\}.
\end{split}                                                       \tag{4}
\]
The exact weights, including the quadratic crossing phase, are
\[
\mu_j=(-1)^U\kappa^3\omega_jq^{3j(j+1)},\qquad
\omega_j=
\begin{cases}
\sin((2j+1)\theta),&N=2m,\\
\displaystyle
\frac{\sin((2j+1)\theta)\sin((m-j)\theta)}
     {\cos^2(\theta/2)},&N=2m+1.
\end{cases}                                                       \tag{5}
\]
In particular none of these is the odd simple-node weight.

The [full endpoint theorem, equations (20)--(24)](research_mixed_next_outer_adjoint_radical_endpoint_conditions.md)
defines a map
\[
\mathscr A_N:\mathscr X_N\longrightarrow\mathbb C^m,\qquad
\mathcal D_N^{\mathrm t}(R^3e_Mh)
                   =R^3e_M(\mathscr A_Nh)
                       \quad\hbox{in }\mathcal A_N.                 \tag{6}
\]
An arbitrary polynomial realizing the values \(h_j\) may be used.
The input radical depends only on those values. The three zeros
in (4) are exactly the conditions for (6); all central first
normals and the odd simple value in the unconstrained transpose
have therefore been accounted for before defining this map.

## 2. The exact rectangular primal matrix

For \(0\le j\le U-1\), use the regular inward coefficient
\[
A_j=\frac{s_{j+1}^4}{s_{2j+1}s_{2j+2}}.
\]
For \(j\ge1\), use
\[
C_j=\frac{s_j^4}{s_{2j}s_{2j+1}},\qquad
C_0=0,\qquad B_j=c_0+A_j+C_j.                                      \tag{7}
\]
The value \(C_0=0\) means the original removable far limit.
The original outward angular coefficient has a cubic zero there,
so both its value and first derivative vanish; it is not a
truncation of a nonzero exterior term.

For evaluations needed below, put
\[
\begin{split}
(\mathbf Lf)_j&=B_jf_j-A_jf_{j+1}-C_jf_{j-1},\\
(\mathbf L_1f)_j&=B_jf_j+q^{2j+2}A_jf_{j+1}
                              +q^{-2j}C_jf_{j-1},\\
(\mathbf Zf)_j&=c_jf_j,
\end{split}                                                       \tag{8}
\]
omitting the outward term at \(j=0\). Insert (8) into the
ordered expression (2). For every
\[
                              0\le j\le U-3                       \tag{9}
\]
this yields a value-only row
\[
(\mathbf D_Nf)_j
       =\sum_{\substack{-3\le r\le3\\0\le j+r\le U}}
                        d_{j,r}f_{j+r}.                            \tag{10}
\]
The empty row range when \(m=3\) is allowed.

Here is why (10) is valid beyond the interior range originally
used for the recurrence. In the three-step term
\(\mathbf L^2\mathbf L_1\), the largest index at which an
operator coefficient is evaluated is \(j+2\le U-1\).
The value at \(U\) can occur only at the last evaluation.
Thus neither an even coalescing coefficient at \(U\) nor the
odd simple-node map is evaluated. On the other side, every
path that first leaves the physical window must use the
vanishing coefficient at \(j=0\). More directly, induction
through (8) only requires the values of the next polynomial
at node \(0\) and inward nodes. It never requires an exterior
value or normal. This uses the original
[current-free transport, Theorem 1](research_current_free_aw_crossing_transport.md),
and its endpoint limit, not a new finite-difference boundary
condition.

The extreme coefficient is
\[
\boxed{\quad
d_{j,3}=q^{2j+4}A_jA_{j+1}A_{j+2}\ne0
                         \qquad(0\le j\le U-3).
\quad}                                                            \tag{11}
\]
Only \(q^{-2}\mathbf L^2\mathbf L_1\) reaches index \(j+3\);
its two negative \(\mathbf L\) shifts and the positive
\(\mathbf L_1\) shift give the displayed phase. Every sine
factor in the three \(A\)'s is positive in this range.
Let \(\mathbf D_N\) denote the resulting \((m-3)\)-by-\(m\)
matrix.

For any original polynomial \(F\), the Frobenius identity and
(6) give
\[
\begin{split}
\sum_{i=0}^{U}\mu_i(\mathscr A_Nh)_iF(c_i)
 &=\phi_N\!\left(
      \mathcal D_N^{\mathrm t}(R^3e_Mh)F\right)\\
 &=\phi_N(R^3e_Mh\,\mathcal D_NF)\\
 &=\sum_{j=0}^{U-3}\mu_jh_j
                  \sum_i d_{j,i-j}F(c_i).
\end{split}                                                       \tag{12}
\]
Every list of values \(F(c_i)\) has a polynomial interpolant.
Consequently the exact endpoint-completed map is
\[
\boxed{\quad
(\mathscr A_Nh)_i
 =\frac1{\mu_i}\sum_{j=0}^{U-3}
                      \mu_jd_{j,i-j}h_j,\qquad0\le i\le U.
\quad}                                                            \tag{13}
\]
Coefficients outside the band are zero. This is a bilinear
weighted transpose, without complex conjugation. Formula (13)
also describes the last three output values; it does not evaluate
an ungrouped singular endpoint coefficient.

## 3. Three periods, exact range, and exact inverse on the range

For \(a=0,1,2\), define \(p^{(a)}\in\mathbb C^m\) by
\(p_i^{(a)}=\delta_{ia}\) for \(0\le i\le2\), and then
successively by
\[
p_{j+3}^{(a)}
 =-\frac1{d_{j,3}}
     \sum_{\substack{-3\le r\le2\\j+r\ge0}}
                              d_{j,r}p_{j+r}^{(a)},
                       \qquad0\le j\le U-3.                       \tag{14}
\]
Define a particular solution \(v\) by \(v_0=v_1=v_2=0\) and
\[
v_{j+3}
 =\frac1{d_{j,3}}\left(
       1-\sum_{\substack{-3\le r\le2\\j+r\ge0}}
                                   d_{j,r}v_{j+r}\right).          \tag{15}
\]
Thus \(\mathbf D_Np^{(a)}=0\) and \(\mathbf D_Nv=1\).
Equation (11) proves that every homogeneous solution is uniquely
specified by its first three values. In particular
\[
\dim\ker\mathbf D_N=3,\qquad
\operatorname{rank}\mathbf D_N=m-3.                                \tag{16}
\]

For a nodal target \(F=(F_0,\ldots,F_U)\), put
\[
\ell_{a,N}(F)=\sum_{i=0}^{U}\mu_i p_i^{(a)}F_i,\qquad
\ell_{v,N}(F)=\sum_{i=0}^{U}\mu_i v_iF_i.                            \tag{17}
\]

**Theorem 1.** At both parities, \(\mathscr A_N\) is injective
and
\[
\boxed{\quad
\operatorname{im}\mathscr A_N
   =\bigcap_{a=0}^{2}\ker\ell_{a,N}.
\quad}                                                            \tag{18}
\]
The three functionals are independent. Every \(F\) has a unique
decomposition \(F=\mathscr A_Nh+\Pi_NF\), \(h\in\mathscr X_N\),
where
\[
(\Pi_NF)_i=
\begin{cases}
\ell_{i,N}(F)/\mu_i,&0\le i\le2,\\
0,&3\le i\le U.
\end{cases}                                                       \tag{19}
\]
In particular \(\Pi_N^2=\Pi_N\) and
\(\ker\Pi_N=\operatorname{im}\mathscr A_N\).

*Proof.* Formula (13) and (16) prove injectivity and codimension
three. Equation (12) with \(F=p^{(a)}\) shows that every image
is annihilated by (17). Independence follows by evaluating these
functionals on the first three coordinate vectors, where their
matrix is \(\operatorname{diag}(\mu_0,\mu_1,\mu_2)\).
This proves (18). Formula (19) preserves all three functionals,
so its difference from \(F\) lies in the image. The two spaces
intersect trivially by the same diagonal calculation. \(\square\)

There is an explicit inverse on the image, without a norm
assertion. For \(i=U,U-1,\ldots,3\), solve successively
\[
h_{i-3}=
\frac{\displaystyle
 \mu_iF_i-
 \sum_{j=i-2}^{\min(i+3,U-3)}\mu_jd_{j,i-j}h_j}
 {\mu_{i-3}d_{i-3,3}}.                                             \tag{20}
\]
An empty sum is zero. The remaining three equations hold exactly
when (18) holds. The same recursion applied to arbitrary \(F\)
gives the \(h\) in (19), since its right-hand side uses only
\(F_3,\ldots,F_U\). Nonzero denominators in (20) establish a
finite inverse, not a level-independent or polynomial norm bound.

The solution space in (14) is not the space of full physical
Hermite solutions. Indeed the original exact conjugation is
\[
\mathcal D_N=TR^3(\mathcal L+2)R^{-3}T,\qquad \mathcal L=TZT.
                                                                    \tag{21}
\]
Thus \(\mathcal D_N\) has zero-dimensional kernel in
\(\mathcal A_N\) at even levels, and one-dimensional kernel at
odd levels, where \(-2\) is a simple physical root. The three
solutions in (14) retain the far endpoint but relax the remaining
central value/normal equations. They cannot all be promoted to
full physical solutions.

## 4. The actual source and its outgoing insertion

Let \(q_i=Q_N(c_i)\). Equations (3),(10),(14),(15) give
\[
\boxed{\quad
q_i=\sum_{a=0}^{2}q_a p_i^{(a)}+\mathfrak f_Nv_i
                         \qquad(0\le i\le U).
\quad}                                                            \tag{22}
\]
Consequently the original outer functional is
\[
\boxed{\quad
\mathcal L_N(F)=\sum_{i=0}^{U}\mu_iq_iF_i
     =\sum_{a=0}^{2}q_a\ell_{a,N}(F)
                         +\mathfrak f_N\ell_{v,N}(F).
\quad}                                                            \tag{23}
\]
Equivalently, if \(h\) is obtained from (20), then
\[
\mathcal L_N(F)
   =\sum_{a=0}^{2}q_a\ell_{a,N}(F)
                     +\mathfrak f_N\sum_{j=0}^{U-3}\mu_jh_j.        \tag{24}
\]
The equality of the forcing terms follows by pairing
\(\mathbf D_Nv=1\) with (13); \(v_0=v_1=v_2=0\) removes
the remainder in (19).

These are exact formulas for the original full source.
The physical values agree with the shortened inner source, but
no equality of full and shortened first normals has been used.
At odd levels the forcing in (23) vanishes; the actual source
selects one linear combination of the three relaxed periods.
At even levels the original forcing remains explicitly present.

For the actual polynomial \(H_N\) and its original cutoffs, the
[exact Newton coefficient theorem, equation (11)](research_mixed_next_middle_exact_newton_coefficients.md)
gives
\[
H_N(\xi,Z)
 =\sum_{\ell=0}^{d}K_{\ell,N}(\xi)
                    C_{0,N}^{>K}(r^{M+\ell},Z),                    \tag{25}
\]
where
\[
\begin{gathered}
r=q^{-2},\quad K=\lfloor N/4096\rfloor,\quad
L=\lfloor N/6\rfloor,\quad d=U-L,\\
K_{\ell,N}(\xi)
 =q^\ell\frac{S_{U-\ell}^2}{S_U^2}
                    \prod_{a=U-\ell+1}^{U}(\xi-c_a).
\end{gathered}
\]
Thus each obstruction has the exact, finite outgoing pairing
\[
\ell_{a,N}(H_N)
 =\sum_{\ell=0}^{d}
     \ell_{a,N}(K_{\ell,N})\,
                          C_{0,N}^{>K}(r^{M+\ell},Z_*).             \tag{26}
\]
This keeps every outgoing row and all phases.

The conditional outgoing recurrence supplies a relation for the
second factor in (26), not a proved adjoint relation for the first.
In its original notation, put
\(\mathsf D=(1-rX)T_X+rX\). The exact operator is
\[
\mathcal O_{N,Z}
 =(1-r^{-2}X^{-1})\mathsf D^2
 +(r^{-1}-2+Zr^{-1}X^{-1})\mathsf D+1-Z.                            \tag{27}
\]
For the complete outgoing sum its forcing is
\(-(1-Z^N)(X^{-N}-1)/N^2\).
For the actual retained sum \(k>K\), the termwise identity
(10c) in [the outgoing difference source](research_mixed_three_fourier_conditional_difference_equation.md)
instead gives
\[
\mathcal O_{N,Z}C_{0,N}^{>K}(X,Z)
 =B_N((K+1)/N;X,Z)
                  -\frac{(1-Z^N)(X^{-N}-1)}{N^2}.                 \tag{28}
\]
Here \(B_N(s)=(e^{2\pi is}-1)^2T_N(s)\) is exactly the
original undivided factorial boundary term. Off the physical
nodes, \(C_{0,N}^{>K}(X,Z)\) means the finite sum from \(K+1\)
through \(D\); its physical stopping zeros are not replaced.
The first term on the right of (28) is
not zero at a physical \(X\) in general. Summing (28) against
(26) would also expose both physical \(\ell\)-endpoints.
Neither (14) nor the full endpoint theorem proves the required
adjoint identity for those transformed weights. The homogeneous
specialization of the complete outgoing equation therefore does
not erase (26) or its retained cutoff forcing.

Finally the complete transfer reduction has precisely the
original scalar
\[
\mathcal T_0[F_N](-2,Z_*)
 =I_{{\rm geom},N}
   +\frac{(-q)^M}{\kappa^2N}
       \left\{\sum_{a=0}^{2}q_a\ell_{a,N}(H_N)
                         +\mathfrak f_N\ell_{v,N}(H_N)\right\}
   +O(e^{N(\Lambda-\epsilon_*)}).                                  \tag{29}
\]
This is substitution into the adopted outer observation, not a
new estimate. Both original Fourier coefficients and all earlier
paid deletions remain those of that source.

## 5. A conditioning obstruction for the far-node projection

There is a source-specific limitation on (19).
On the odd subsequence, (22) has no particular-solution term.
At the last double node, the adopted physical packet and its
complete-color limit give
\[
|q_U|\ge cN^{-A}e^{N\mathfrak M_3},\qquad
                       \mathfrak M_3>9/5.                         \tag{30}
\]
The angle is \(u_U=2\pi/N\), not the odd simple angle zero.
The original even holomorphic action differs from its value at
zero by \(O(N^{-2})\), and the nonzero packet coefficient is
uniform there. These are exactly the source facts used in
[the self-adjoint norm obstruction, equations (16)--(20)](research_mixed_next_outer_self_adjoint_norm_obstruction.md).

For the first three nodes, \(u_a=\pi-(2a+1)\pi/N\).
The full-source far-angle estimate gives, for each
\(\varepsilon>0\),
\[
\max_{0\le a\le2}|q_a|
 \le C_\varepsilon N^{A_\varepsilon}
                       e^{N(8/5+\varepsilon)}.                    \tag{31}
\]
It applies to these moving physical nodes for all sufficiently
large \(N\); see
[far angles, equation (25)](research_mixed_next_outer_far_angles_and_verticals.md).
Combining (22),(30),(31) proves
\[
\max_{0\le a\le2}|p_U^{(a)}|
 \ge c_\varepsilon N^{-B_\varepsilon}
              e^{N(\mathfrak M_3-8/5-\varepsilon)}
                              \qquad(N\text{ odd}).                \tag{32}
\]
No cancellation lower bound was used: (32) follows from the
triangle inequality for the exact three-term expression for
one already nonzero physical value.

Every ratio \(|\mu_U/\mu_a|\), \(a=0,1,2\), is bounded below
by a negative power of \(N\), directly from (5) and the sine
chord. Applying (19) to the coordinate vector at \(U\)
therefore gives
\[
\boxed{\quad
\liminf_{\substack{N\to\infty\\N\ {\rm odd}}}
       \frac1N\log\|\Pi_N\|_{\ell^\infty\to\ell^\infty}
 \ge \mathfrak M_3-\frac85>\frac15.
\quad}                                                            \tag{33}
\]
The same exponential lower rate holds for the largest norm
of the three normalized functionals
\(\ell_{a,N}/\mu_a\).

Thus this exact projection cannot transfer a generic nodal
supremum estimate to three inexpensive far-node remainders.
It does not refute a bounded inverse of \(\mathscr A_N\) on
its image with a different complement or an orthogonal
projection, and does not estimate the actual pairings (26).

The all-character principal lower bound \(d\ge4\) and the
adopted interior Dirichlet inverse apply on fixed compact
interior angular intervals. Their coefficient estimates are
not uniform through the central \(N^{-1}\) layer. In fact
(7) has coefficients of order \(N^2\) there, and the full
grouped endpoint map is essential. Neither principal positivity
alone nor the exact rank calculation supplies a global
accretivity or singular-value estimate for (13).
A source-specific estimate for (26), or an inverse together
with a quantitatively controlled compatible complement, remains
necessary.

## 6. Frozen source bindings

All cited identities were read statically; no source was evaluated.

- Seven-term source: 49cd08c5759bd6669d3cbf1a7e661d60188639c9added0c973659c4723d0a21a.
- Full endpoint theorem: 9cde443d65bfdc41104ffe9e78ce4e4540ec998b53681923f99fd42a5d436d71.
- Current-free transport: f81b9fc3edc2504c5250ad283bf0ceff191a1fc3a310c00fdb57602362f0bf4a.
- Exact Newton coefficients: d8b58688c4da4237ac9cc5073fb32e0601d1326aab52dc9d71cee2070618ed48.
- Outgoing difference equation: 8d53391830ba5de33a8b1f79c355d7ccd85878ff49f16c5d99cd44034a1de051.
- Original outer observation: cbbc62951666d06e0ae77b29f49f563d91c2024dc8da900ae996144d7db39dab.
- All-character symbol: c88ba98093fc147f5acfcf1790aa5b6f0f26edda6d741d2efc7c55315942e55e.
- Interior inverse: e1b713461bacdf263c07c3baa21de67960fae5e5e2735e5c400c009c987afddf.
- Complete degree-two source: 7ac634d458e5805e95a7ce064d4e1fc513c96c0b758cfaee9f91fd46de10304c.
- Far-angle source: 5e64e4909b55107431d13fcbff92f41776ff101757c5a9f7eb70ae2d8ea1408d.
- Physical inner packet: c43064953e7d3bfa92a6ecc05725719661e45d0b6bfca76fe1b78a28c68de4f3.
- Self-adjoint norm obstruction: ddad67e85205d7d637ea4ab156f4e67938aacdc6aaed86213e8128d55d8a1849.

