# A single exact source for two adjacent power-two blocks

Research deduction, 7 November 2026. The original interface between
two power-two components can be summed exactly. In the original
Fourier basis the result is one triangular factorial matrix. Reversing
its two summation indices gives a complete two-index source, or one
conditional \(C_0\) source with an explicit incoming weight.

All formulas retain the full finite state and its ordinary normal
adapters. The stationary equations below belong to this merged
source. Neither a contributing critical point nor a lower bound for
its prescribed closing functional is inferred. No numerical
evaluation is used.

## 1. The original matrices and a power-two Fourier kernel

Set
\[
 D=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad r=Q^{-1},
 \quad P_j=(r;r)_j,\quad \kappa=q^{D^2/2},\quad
 \nu_j=(-1)^jq^{j(j+1)},\qquad N\ge2.
 \tag{1}
\]
Let \(J\) be the original reversal, \(M\) the original crossing
matrix, and \(A_2=JM^2\). The \(J\) here is a matrix, not the
factorized scalar contour representative.
Use exactly
[wire contraction](research_mixed_wire_exact_contraction.md),
equations (3), (5), (13):
\[
\begin{split}
 f_j(x)&=\frac{e^{-\pi iDx}}N
      Y_x^j\prod_{h=j+1}^{D}(1-Y_xr^h),\qquad Y_x=e^{2\pi ix},\\
 f&=Sh,\qquad S=L M,\qquad
 L_{jj}=\frac{\kappa^{-1}(-q)^{-j}}{P_j},\\
 \Gamma&=SS^T,\qquad
 \Gamma_{jk}=
 \begin{cases}
 Q^{jk}P_{j+k}/(P_j^2P_k^2),&j+k<N,\\
 0,&j+k\ge N.
 \end{cases}
\end{split}
 \tag{2}
\]
All transposes and contractions here are bilinear.

The original Frobenius pairing is
\(\phi(e_i e_j)=J_{ij}\). Since multiplication by the crossing
commutes with multiplication by every algebra element,
\[
                         M^T J=JM.
 \tag{3}
\]
This retains the repeated-root normal directions; it is not a
Hermitian adjoint identity.

The exact complementary factorial formula is
\[
 P_{D-j}=\frac{N}{\nu_jP_j},\qquad
 \nu_{D-j}=\nu_j,\qquad
 \kappa^2(-q)^D=1 .
 \tag{4}
\]
For the first identity, split \(P_D=N\) at \(D-j\) and use
\(\prod_{h=1}^j(1-r^{-h})=\nu_jP_j\).
The other two follow by their displayed integer exponents,
using \(D+1=N\). In particular they hold at both level parities.

**Proposition 1.** The exact Fourier kernel of one power-two block is
\[
 A_2=S^TB_2S,\qquad
 B_2=N\operatorname{diag}(\nu_j^{-1})J.
 \tag{5}
\]

*Proof.* From (3),
\[
 S^{-T}A_2S^{-1}
  =L^{-1}M^{-T}JM L^{-1}
  =L^{-1}JL^{-1}.
\]
Its only nonzero entries have \(j+k=D\), and there they equal
\(\kappa^2(-q)^D P_jP_k=N\nu_j^{-1}\) by (4).
\(\square\)

## 2. The complete adjacent interface is summed

**Theorem 2.** Define
\[
 (\mathcal C_{22,N})_{jk}
 =
 \begin{cases}
 \displaystyle\frac{P_j^2P_k^2}{N P_{j+k-D}},&j+k\ge D,\\[2mm]
 0,&j+k<D.
 \end{cases}
 \tag{6}
\]
Then the full original adjacent operator satisfies
\[
                    A_2^2=S^T\mathcal C_{22,N}S.
 \tag{7}
\]
In particular, for any prescribed original row \(\ell^T\) and
column \(b\),
\[
 \boxed{\quad
 \ell^TA_2^2b
 =\frac1N\sum_{\substack{0\le j,k<N\\j+k\ge D}}
       (S\ell)_j(Sb)_k\frac{P_j^2P_k^2}{P_{j+k-D}} .
 \quad}
 \tag{8}
\]

*Proof.* Insert \(SS^T=\Gamma\) between the two factors in (5).
The intervening Fourier matrix is
\[
 (B_2\Gamma B_2)_{jk}
       =N^2\nu_j^{-1}\nu_k^{-1}\Gamma_{D-j,D-k}.
 \tag{9}
\]
Its exact support is \(2D-j-k<N\), equivalently \(j+k\ge D\).
On that support set \(m=j+k-D\). Substituting (2), then (4),
reduces (9) to
\[
 \frac{P_j^2P_k^2}{N P_m}
       Q^{(D-j)(D-k)}\frac{\nu_j\nu_k}{\nu_m}.
 \tag{10}
\]
The last factor is one. Its sign is \((-1)^D\), while its
\(q\)-exponent is
\[
 2(D-j)(D-k)+j(j+1)+k(k+1)-m(m+1)=D(D+1)=DN.
 \tag{11}
\]
Thus it is \((-1)^Dq^{DN}=1\). This proves (6)--(8).
The factorials in (6) are still complex; cancellation of the
explicit \(Q,\nu\) carriers is not positivity.
\(\square\)

This is a summation of the actual interface in
[full-node composition](research_mixed_three_homogeneous_period_full_node_composition.md),
equations (23), (26):
\[
 S^{-1}\mathsf P^{-1}\mathbf H_N\mathsf B_N
       \mathbf H_N\mathsf D
       =S^T\mathcal C_{22,N}S,
 \qquad
 \mathsf B_N=\kappa\mathsf D M^{-1}\mathsf D^{-1}.
 \tag{12}
\]
It does not replace \(\mathsf B_N\) by an identity or a conjugate
pairing. All colors, including both complementary ranges and the
boundary \(j+k=D\), occur in (8).

For an ordinary terminal \(b=v(w)\), use \(Sv(w)\) in (8).
Every prescribed derivative uses \(S v^{(k)}(w)\), since \(S\)
does not depend on \(w\). The same statement applies on the left
and to the unchanged multiplication tensor at a branching slot.
No raw derivative of a chosen off-grid conditional interpolation
replaces these original adapters.

## 3. A reversed source and one exact conditional contraction

Put
\[
 X=e^{-2\pi ix},\qquad W=e^{-2\pi iy},\qquad
 p_u(Z)=(rZ;r)_u.
\]
The original finite cardinal polynomial obeys
\[
                  f_{D-u}(x)
       =\frac{e^{\pi iDx}}N\,\nu_u p_u(X),
              \qquad 0\le u<N.
 \tag{13}
\]
Indeed factor each of the \(u\) factors in its suffix as
\(1-Y_xr^{-h}=-Y_xr^{-h}(1-Xr^h)\); the resulting carrier is
\((-1)^ur^{-u(u+1)/2}=\nu_u\).

**Corollary 3.** The full Fourier boundary kernel of the adjacent
pair is
\[
 \boxed{\begin{split}
 V_{22,N}(x,y)&:=h(x)^TA_2^2h(y)\\
 &=e^{\pi iD(x+y)}
     \sum_{\substack{u,v\ge0\\u+v<N}}
       \frac{Q^{uv}P_{u+v}p_u(X)p_v(W)}{P_u^2P_v^2}\\
 &=e^{\pi iD(x+y)}
     \sum_{u=0}^{D}\frac{p_u(X)}{P_u}
                         C_{0,N}(r^u,W).
 \end{split}}
 \tag{14}
\]
There is no additional outside \(N\) or \(\kappa\).

*Proof.* Apply (9) to \(f(x)^TB_2\Gamma B_2f(y)\) and
substitute (13). Both factors \(N\), both factors \(\nu_u^{-1}\),
and both original cardinal \(1/N\)'s cancel, leaving \(\Gamma_{uv}\)
and the displayed chirp. For the last equality use the literal
conditional polynomial
\[
 C_{0,N}(r^u,W)=
 \sum_{v=0}^{D-u}
       \frac{Q^{uv}P_{u+v}p_v(W)}{P_uP_v^2}.
 \tag{15}
\]
The upper limit is the actual zero of \(p_v(r^u)\), not an
estimate. \(\square\)

The original matrix is symmetric, as is the double sum in
(14) under \((x,u)\leftrightarrow(y,v)\). This supplies an
independent check on the chirp and the support.

## 4. Repeated power-two blocks and the existing single-power reduction

The general coherent reduction of a same-sign power-two run is
already proved in
[the original turn reduction](actual_newton_coherent_turn_reduction.md),
Section 3. Here is its explicit source form in the same Fourier
basis. Define an upper triangular matrix \(K\) and a diagonal
matrix \(H_{\!P}\) by
\[
 K_{jk}=
 \begin{cases}\nu_j^{-1}/P_{k-j},&j\le k,\\0,&j>k,\end{cases}
 \qquad H_{\!P}=\operatorname{diag}(P_j^2).
 \tag{14a}
\]
The letter \(H_{\!P}\) is not the homogeneous-period node matrix.
Direct substitution in (2), (5) gives
\[
 (\Gamma B_2)_{jk}
 =\frac{\nu_j^{-1}P_k^2}{P_j^2P_{k-j}}\quad(j\le k),
 \qquad
 SA_2S^{-1}=H_{\!P}^{-1}K H_{\!P}.
 \tag{14b}
\]
For example the phase used in the first identity is
\(Q^{j(D-k)}\nu_k/\nu_{k-j}=\nu_j^{-1}\).
Thus every positive integer \(m\) has the exact kernel
\[
\begin{split}
 A_2^m&=S^TB^{[m]}S,\\
 B^{[m]}&=\frac1N H_{\!P}\operatorname{diag}(\nu_j)
                              J K^{m-1}H_{\!P}.
\end{split}
 \tag{14c}
\]
To prove this, use \(B^{[m]}=B_2(\Gamma B_2)^{m-1}\) and
\(B_2H_{\!P}^{-1}=N^{-1}H_{\!P}\operatorname{diag}(\nu_j)J\),
the latter being (4). Since \(K\) is upper triangular,
every \(B^{[m]}\) vanishes when \(j+k<D\).
The notation \(B^{[m]}\) denotes a run of \(m\) vertices of
power two, not a single vertex of power \(2m\).

This is exactly a known finite q-binomial operator. If \(C_Q\)
is the lower triangular matrix (4) in
[terminal powers](research_terminal_powers_qbinomial.md),
then
\[
 (C_Q)_{kj}=\frac{\nu_j}{(Q;Q)_{k-j}},
             \qquad K=\overline{C_Q}^{\,T}=C_r^T .
 \tag{14d}
\]
The last notation means the same finite formula at base \(r\).
It is not coefficient conjugation of free boundary parameters.
The original terminal-power similarity
\(M=\kappa D_{\rm tw}C_QD_{\rm tw}^{-1}\),
\((D_{\rm tw})_{jj}=(-q)^j(Q;Q)_j\), gives equivalently
\[
 K=\kappa\,\overline{D_{\rm tw}}\,
                M^*\,\overline{D_{\rm tw}}^{-1}.
 \tag{14e}
\]
All diagonal factors are nonzero.

For a second concrete product, the finite binomial theorem gives
\[
 (K^2)_{jk}
   =\nu_j^{-2}\frac{P_k}{P_jP_{k-j}},\qquad j\le k.
 \tag{14f}
\]
Indeed, writing \(h=j+t\) in \(\sum_hK_{jh}K_{hk}\) leaves
\(\nu_j^{-2}(r^{j+1};r)_{k-j}/P_{k-j}\).
Consequently three adjacent blocks have the exact kernel
\[
 B^{[3]}_{jk}
 =
 \begin{cases}
 \displaystyle\frac{P_j^3P_k^3}{N^2P_{j+k-D}},&j+k\ge D,\\
 0,&j+k<D.
 \end{cases}
 \tag{14g}
\]

The original modular identity, in the convention of
[positive three-crossing chains](research_positive_three_crossing_cycle.md),
equation (2), also writes the all-run reduction directly as
\[
 A_2^m=\kappa^m M^{-1}J M^{-m}J M .
 \tag{14h}
\]
For \(m=1\), this follows by multiplying
\(MJM=\kappa JM^{-1}J\) by \(M^{-1}\) and \(M\);
the general formula is its similarity power. It is algebraically
valid for all integer \(m\), but negative powers here are
powers of \(A_2^{-1}\), not an identification with a run of
the distinct vertices \(A_{-2}=JM^{-2}\).

In particular the actual prescribed observation is
\[
 \ell^TA_2^m b
   =\kappa^m(\ell^TM^{-1}J)\,M^{-m}\,(JM b).
 \tag{14i}
\]
The two adapters in (14i) must be retained. A terminal-power
packet for the source \(JM^{-m}e_0\) does not automatically
estimate this mixed observation. No bound on these adapters'
conditioning or on their closing overlap follows from the
similarity.

There is already a complete theorem for the particular capped
observation \(e_0^TA_2^2v(-2\cos u)\):
[the adjacent two-crossing boundary theorem](research_adjacent_two_crossing_boundary_theorem.md),
Sections 1--5. Its source identity is (2)--(3) of
[the adjacent pair calculation](research_adjacent_two_crossing_pair.md).
Here \(Se_0=(1/P_j)_j\), directly from (2), so it is a
specified specialization of (8). The new formulas retain two
free boundary states; they do not constitute a new proof of
that previously established capped family or extend its
estimate to arbitrary transformed rows.

## 5. One regular chart for the entire finite residue sum

Let \(\Pi_N\) and \(E_N=1/\Pi_N\) have the exact continuations
proved in
[the joint global factorial chart](research_mixed_fourier_right_cap_joint_global_chart.md):
\(\Pi_N\) is holomorphic for \(\Re z>-1/N\), including its
positive-wall zeros, and \(E_N\) is holomorphic for \(\Re z<1\).
For \(0<\Re x,\Re y<1\), define
\[
 \mathscr R_N(a,s;x,y)=e^{2\pi iNas}
   \Pi_N(a+s)\Pi_N(a+x)\Pi_N(s+y)
          E_N(a)^2E_N(s)^2E_N(x)E_N(y).
 \tag{16}
\]
At physical \(a=u/N,s=v/N\), this is exactly the summand in
(14) when \(u+v<N\), and it is zero when \(u+v\ge N\).
The latter zeros come from \(\Pi_N((u+v)/N)\); none is a
division by a vanishing factorial.

Choose both real contour intervals to be
\[
              \alpha_N=-\frac1{3N},\qquad
              \beta_N=1-\frac1{3N}.
 \tag{17}
\]
All \(N\) physical nodes lie in their interiors. On their
product,
\[
 \Re(a+s)\ge-\frac2{3N}>-\frac1N,\qquad
 \Re(a+x),\Re(s+y)>-\frac1N,\qquad
 \Re a,\Re s\le\beta_N<1.
 \tag{18}
\]
Thus (16) is holomorphic on a
neighborhood of the product of any two fixed finite-height
rectangles with these real cuts. The statement includes
all support-wall crossings \(a+s=1\). These are not midpoint
cuts: no midpoint kernel estimate is imported. Two lower
half-grid cuts would instead place their common corner at
\(a+s=-1/N\), outside the stated numerator domain.

If \(\Gamma_a,\Gamma_s\) are their positive boundaries,
with the real axis in their interiors, the exact identity is
\[
 V_{22,N}(x,y)=\frac{e^{\pi iD(x+y)}}{(2\pi i)^2}
 \int_{\Gamma_a}\int_{\Gamma_s}
     \mathscr R_N(a,s;x,y)
        \{\pi N\cot(\pi Na)\}\{\pi N\cot(\pi Ns)\}\,ds\,da .
 \tag{19}
\]
Both cotangent residues are one. The chart has no other poles
inside. All side currents and aliases generated by deforming
(19) remain part of this identity. In particular the exact
zero of an added physical row does not delete its off-grid
continuation.

## 6. The merged phase, density, and stationary equations

On a compact regular chart on which
\[
 a,\ s,\ a+s,\ a+x,\ s+y,\ x,\ y
        \quad\hbox{all have real part in }(0,1),
 \tag{20}
\]
use the original marked primitive \(g\), and
\[
       \mathfrak a(z)=\sqrt{2\sin\pi z}\,e^{-\pi iz/2}.
 \]
The complete regular-row expansion of (16) is
\[
 \mathscr R_N
   =N^{-3/2}\mathcal A_{22}(a,s;x,y)
                   e^{N F_{22}(a,s;x,y)}(1+O(N^{-1})),
 \tag{21}
\]
uniformly with fixed derivatives on smaller compact charts, where
\[
\begin{split}
 F_{22}&=g(a+s)+g(a+x)+g(s+y)
                -2g(a)-2g(s)-g(x)-g(y)+2\pi ias,\\
 \mathcal A_{22}
   &=\frac{\mathfrak a(a+s)\mathfrak a(a+x)\mathfrak a(s+y)}
       {\mathfrak a(a)^2\mathfrak a(s)^2
          \mathfrak a(x)\mathfrak a(y)}\ne0 .
\end{split}
 \tag{22}
\]
This follows by substituting the original
\(\Pi_N(z)=N^{1/2}\mathfrak a(z)e^{Ng(z)}(1+O(N^{-1}))\)
in every factor of (16). The three numerator factorials
and six reciprocal factorials give \(N^{-3/2}\).
The outside chirp in (19) adds \(\pi i(x+y)\) to the action
and \(e^{-\pi i(x+y)}\) to the leading coefficient.

The original critical equations are
\[
\begin{split}
 0&=g'(a+s)+g'(a+x)-2g'(a)+2\pi is,\\
 0&=g'(a+s)+g'(s+y)-2g'(s)+2\pi ia.
\end{split}
 \tag{23}
\]
With \(U=e^{-2\pi ia}\) and \(V=e^{-2\pi is}\), they imply
\[
\begin{split}
 (1-UV)(1-UX)&=V(1-U)^2,\\
 (1-UV)(1-VW)&=U(1-V)^2.
\end{split}
 \tag{24}
\]
Conversely (24) only fixes the derivatives modulo
\(2\pi i\mathbb Z\). The original lifts in (23), critical
eligibility, and a contributing contour require their own proof.
The Hessian on this chart is
\[
\begin{split}
 F_{aa}&=\pi\{\cot\pi(a+s)+\cot\pi(a+x)-2\cot\pi a\},\\
 F_{ss}&=\pi\{\cot\pi(a+s)+\cot\pi(s+y)-2\cot\pi s\},\\
 F_{as}&=\pi\cot\pi(a+s)+\pi i .
\end{split}
 \tag{25}
\]
No definiteness or global dominance assertion is made here.

If a contributing nondegenerate two-dimensional Gaussian
and a strict bound for every remaining current in (19) are
proved, the density \(N^2\), row power \(N^{-3/2}\), and
Gaussian power \(N^{-1}\) give a full \(N^{-1/2}\) packet.
For a chosen oriented Gaussian chart its coefficient would be
\[
 \frac{2\pi e^{-\pi i(x+y)}
          \mathcal A_{22}(a_*,s_*;x,y)}
               {\sqrt{\det(-F_{22}'')}} .
 \tag{26}
\]
This conditional coefficient is nonzero on such a regular
nondegenerate chart. Equation (26) is a normalization check,
not a theorem that this critical point contributes.

## 7. The exact remaining composition estimate

The
[complete physical-input packet](research_mixed_three_physical_input_complete_packet.md)
now estimates each conditional factor in (14) for
\(u/N\in[.267,.433]\) and \(y\) near \(x_0\), including
its nonzero coefficient and outgoing derivatives.
It supplies no estimate for the other \(u\)'s in that exact
sum. Nor does it by itself justify moving its incoming
argument off the real lattice.

On a chart where an incoming holomorphic representative has
also been justified, the candidate outer phase is specifically
\[
       g(a+x)-g(a)-g(x)+\Phi_1(a,y)+\pi i(x+y).
 \tag{27}
\]
Its stationary point must satisfy the first equation in
(23), with \(s\) the actual inner conditional critical point.
Thus the incoming variable of the composition is not free
to remain at a convenient real center of the one-block packet.
The complete complementary colors, incoming sampling currents,
and all endpoints of (19) must be compared to the action
of this same stationary point.

For a prescribed ordinary closing row, the sufficient estimate
must instead apply to its actual signed sum (8), or to the
equivalent exact closed-period contraction with its original
adapters. A lower bound for a vector norm, the two-point
calibrated difference observation, or a nonzero kernel entry
does not supply that scalar estimate.

The algebraic interface obstruction in \(\mathbf H\mathsf B\mathbf H\)
has therefore been removed: (8), (14), and (19) are explicit
complete sources with the interface already summed. The new
one-block packet removes the local full-source coefficient
hypothesis for its stated physical rows. The geometric
critical-domain, complete-complement, and prescribed-closing
noncancellation hypotheses for the adjacent pair remain.
No new knot family or finite-exception statement follows here.

## 8. Pairing the two sides before estimating the first variable

The full-period cuts in (17) also give an exact one-variable
reorganization of the merged source. This pairs the two vertical
sides before taking absolute values. In particular the boundary
factors associated with the free Fourier parameters remain present.

To distinguish the level-period exponentials from \(X,W,U,V\),
write
\[
 A=e^{-2\pi iNa},\qquad B=e^{-2\pi iNs},\qquad
 C=e^{-2\pi iNx},\qquad E=e^{-2\pi iNy}.
 \tag{28}
\]
The letter \(E\) in this display is a scalar, not the reciprocal
factorial \(E_N\). The exact factorial period relations imply
\[
\begin{split}
 \mathscr R_N(a+1,s;x,y)&=\mathcal J_a(A,B;C)
                                      \mathscr R_N(a,s;x,y),\\
 \mathcal J_a(A,B;C)&=\frac{(1-AB)(1-AC)}{B(1-A)^2},\\
 \mathscr R_N(a,s+1;x,y)&=\mathcal J_s(A,B;E)
                                      \mathscr R_N(a,s;x,y),\\
 \mathcal J_s(A,B;E)&=\frac{(1-AB)(1-BE)}{A(1-B)^2}.
\end{split}
 \tag{29}
\]
The quotients are used where their denominators do not vanish;
the resulting meromorphic identities retain the cancellations
in the original factorial products. On the contour
\(a=\alpha_N+iv\), the first denominator never vanishes:
\[
 A=e^{2\pi i/3}e^{2\pi Nv},\qquad
 |1-A|^2=1+e^{2\pi Nv}+e^{4\pi Nv}.
 \tag{30}
\]
No midpoint identity is used.

**Proposition 4.** Fix \(N\ge2\), \(0<\Re x,\Re y<1\), and
\[
                    -\frac{2}{3N}<\Re s<1.
 \tag{31}
\]
For every real \(h\), the sum over the entire first physical
index has the exact representation
\[
\begin{split}
 \sum_{u=0}^{D}\mathscr R_N(u/N,s;x,y)
 ={}&N\int_{\alpha_N+ih}^{\beta_N+ih}
                                     \mathscr R_N(a,s;x,y)\,da\\
 &+N\int_{\alpha_N-i\infty}^{\alpha_N+ih}
               \mathcal K_-(A,B;C)\mathscr R_N(a,s;x,y)\,da\\
 &+N\int_{\alpha_N+ih}^{\alpha_N+i\infty}
               \mathcal K_+(A,B;C)\mathscr R_N(a,s;x,y)\,da,
\end{split}
 \tag{32}
\]
where both vertical contours point upward, and
\[
\begin{split}
 \mathcal K_+(A,B;C)
   &=\frac{(1-B)+A(B-C)+A^2B(C-1)}{B(1-A)^3},\\
 \mathcal K_-(A,B;C)&=A\mathcal K_+(A,B;C).
\end{split}
 \tag{33}
\]
The two integrals in (32) converge absolutely at fixed \(N\).
The identity is locally uniform for \(s,x,y\) in the stated
domains. It retains the factors \(C=X^N\) and \(B\) without
specialization.

*Proof.* On the whole first-variable rectangle, (31) gives
\(\Re(a+s)>-1/N\). The other numerator and reciprocal arguments
in (16) remain in their respective holomorphic domains.
Set
\[
                           k_N(a)=\frac1{1-A}.
\]
At \(a=u/N\) its residue is \(1/(2\pi iN)\). The residue
theorem consequently expresses the left side of (32) as
\(N\oint k_N(a)\mathscr R_N(a,s;x,y)\,da\).

The exact nonreal factorial formulas, with the normalization of
[factorial alias elimination](research_mixed_fourier_factorial_alias_elimination.md),
equations (2)--(6), give
\[
\begin{split}
 \mathscr R_N(a,s;x,y)
   &=c_{-,N}(s,x,y)e^{2\pi iNas}(1+o(1)),
                                      &&\Im a\longrightarrow-\infty,\\
 \mathscr R_N(a,s;x,y)
   &=c_{+,N}(s,x,y)e^{-2\pi iNxa}(1+o(1)),
                                      &&\Im a\longrightarrow+\infty.
\end{split}
 \tag{34}
\]
The constants do not depend on \(a\). Uniformity holds on the
bounded real interval \([\alpha_N,\beta_N]\) and on fixed
compact subsets of the other parameters. If a factor independent
of \(a\) vanishes, the whole row vanishes and the identity follows
directly or by holomorphic continuation.
For the upper end, the terms involving \(a\) in the two
numerator quadratic exponents and the two reciprocal exponents
sum to \(-2\pi iN(s+x)a\); the original factor
\(e^{2\pi iNas}\) leaves precisely the second exponent in
(34). At the lower end these factorial exponents cancel.

Since \(k_N\to1\) below and \(k_N\to0\) above, the horizontal
corrections \((k_N-1)\mathscr R_N\) below and
\(k_N\mathscr R_N\) above decay, respectively, at the strictly
positive rates
\[
                  2\pi N(1-\Re s),\qquad
                  2\pi N(1-\Re x).
 \tag{35}
\]
They therefore disappear at fixed level. The bottom integral
of the unweighted row is moved to height \(h\) by Cauchy's
theorem, retaining its two joining sides. Pair the right side
with the left using \(\beta_N=\alpha_N+1\), the periodicity
of \(k_N\), and (29). Below \(h\) the combined multiplier is
\[
 (k_N-1)(\mathcal J_a-1);
\]
above \(h\) it is \(k_N(\mathcal J_a-1)\).
Their expansion is exactly (33), including both signs in (32).

At the lower end, \(A\to0\), so
\(\mathcal K_-=O(A)\). At the upper end,
\(\mathcal K_+=O(A^{-1})\). Formula (34) now gives the
same integrable rates (35) on the two vertical tails.
The estimates are uniform on compact parameter sets, proving
the claimed local uniformity. \(\square\)

At a retained physical second index \(s=v/N\), one has \(B=1\).
Thus the complete side kernels reduce to
\[
 \mathcal K_+=(1-C)\frac{A}{(1-A)^2},\qquad
 \mathcal K_-=(1-C)\frac{A^2}{(1-A)^2}.
 \tag{36}
\]
There is also the exact multiplicative identity
\[
 \mathscr R_N(a,v/N;x,y)
   =\frac{p_v(W)}{P_v}\,
     T_N(a;v/N,x),
 \tag{37}
\]
where \(T_N\) is the original conditional factorial row in
[the particular-current theorem](research_mixed_three_fourier_conditional_particular_current.md).
Indeed its remaining factor is
\(\Pi_N(v/N+y)E_N(v/N)E_N(y)=p_v(W)/P_v\).
No division by \(p_v(W)\) is used, so its possible zeros are
retained. Equations (36)--(37) identify (32) with the conditional
decomposition in the other summation order. If also \(C=1\),
both side kernels vanish exactly; this specialization alone
gives no estimate for the remaining horizontal integral.

For the second physical sum, (32) may be used at each
\(s=v/N\) and then summed, with the outside factor
\(e^{\pi iD(x+y)}\) from (14). This is still an exact finite
operation. It does not estimate those currents at the critical
action. Nor does fixed-level convergence in (35) establish a
uniform estimate as \(\Re s\) approaches one. Deforming the
second variable while the first current is unbounded requires
its own joint tail bounds; no interchange of two unbounded
contours is asserted here.
