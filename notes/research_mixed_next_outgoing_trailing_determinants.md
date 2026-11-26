# Exact trailing determinants for the original outgoing source

Private finite-source deduction, 8 November 2026. The outgoing
energy estimate extends through the last physical index \(D\).
Every trailing Dirichlet determinant is then an explicit nonzero
factor times the original complete conditional polynomial. This
identifies a zero-free finite connection coefficient and the exact
diagonal Green ratio throughout the actual outgoing region.

The remaining lower-boundary cutoff can also be replaced by the
complete conditional value with a proved exponential error. The
resulting Green numerator is still the original coherent inner-period
sum. No asymptotic for a finite ratio is inferred from a principal
critical action, and no suppression of that sum is asserted.
No mathematical numerical evaluation or frozen-source edit is used.

The original task attachment and the current progress front were
reread: the calculation concerns the specified complete reference
family, not stability under arbitrary short partial fillings.

## 1. Original signed source and its last physical equation

Use exactly the notation of the adopted
[full-tail energy theorem](research_mixed_next_outgoing_full_tail_weighted_energy.md):
\[
\begin{gathered}
D=N-1,\quad \theta=\pi/N,\quad q=e^{i\theta},\quad r=q^{-2},
\quad \kappa=q^{D^2/2},\\
M=\lceil N/2\rceil,\quad U=\lfloor N/2\rfloor-1,\quad
L=\lfloor N/6\rfloor,\quad K=\lfloor N/4096\rfloor,\\
s_b=2\sin(b\theta),\quad S_b=\prod_{\nu=1}^{b}s_\nu,\quad
Y_b=r^b,\quad P_k=(r;r)_k,\quad p_k(Z)=(rZ;r)_k,\\
A_b=Y_b(Y_b-1),\quad B_b=3Y_b-(1+r)Y_b^2,\quad
C_b=r^{-1}(1-rY_b)^2.
\end{gathered}                                                     \tag{1}
\]
Distinguish the complete and retained outgoing sources:
\[
\begin{split}
c_b(Z)&=C_{0,N}(r^b,Z)
 =\sum_{k=0}^{D}\frac{Y_b^{-k}p_k(Y_b)p_k(Z)}{P_k^2},\\
\alpha_b(Z)&=(-q)^bc_b(Z),\\
a_b(Z)&=(-q)^b\sum_{k=K+1}^{D}
                   \frac{Y_b^{-k}p_k(Y_b)p_k(Z)}{P_k^2},\\
f_b(Z)&=(-q)^b r^{-K-1}(1-r^{K+1}Z)
                   \frac{Y_b^{-K}p_K(Y_b)p_K(Z)}{P_K^2}.
\end{split}                                                       \tag{2}
\]
At a physical input the sum stops exactly at \(D-b\).
The original signed operator is
\[
(\mathcal J_Nx)_b=-qA_bx_{b-1}+B_bx_b-q^{-1}C_bx_{b+1}.
                                                                    \tag{3}
\]
On \(1\le b\le D-1\), the
[paired finite recurrence, equation (6)](research_mixed_next_outer_paired_newton_characteristics.md)
gives \(\mathcal J_N\alpha=Z\alpha\) and
\(\mathcal J_Na-Za=-f\).

The complete equation also holds at \(b=D\), with its last
coefficient exactly zero:
\[
C_D=0,\qquad c_D=1,\qquad \alpha_D=(-q)^D.
                                                                    \tag{4}
\]
This can be verified directly from the two literal last sums:
\[
\begin{gathered}
c_{D-1}
 =1-\frac{r(1-rZ)}{1-r},\qquad
A_D=\frac{1-r}{r^2},\qquad B_D=\frac{2r-1}{r^2},\\
A_Dc_{D-1}+B_D=Z.
\end{gathered}                                                     \tag{5}
\]
Multiplication by \((-q)^D\) proves the signed equation.
No value at the nonphysical index \(D+1\) is prescribed or
needed, because its coefficient is zero.

For all sufficiently large levels \(K\ge1\), the retained
source has \(a_D=a_{D-1}=f_D=0\) by literal physical
termination. Hence its equation also holds at \(D\).
Equivalently it follows from the original telescoping proof;
the termination argument suffices in the asymptotic range here.

Keep the closed actual containing region
\[
\mathfrak Z=\left\{\rho e^{-i\alpha}:
 \frac45\le\rho\le\frac87,\quad
 \frac{3\pi}{5}\le\alpha\le\frac{39\pi}{50}\right\}.
                                                                    \tag{6}
\]
All later actual-reference assertions concern complete words in
powers three and four beginning \(343\), of length at least
five, at \(w=-2,Z=Z_*\), with the original
\(\Lambda>419/200\).

## 2. Energy and Green functions through index \(D\)

For any interval \(I\subseteq[M,D]\), use
\(\|x\|_{S,I}^2=\sum_{j\in I}S_j|x_j|^2\), and impose zero
exterior values on tests only. The full-tail row normalization is
\[
w_j=\exp i\{(5j/2+1/4)\theta-\pi/4\},\qquad
t_j=(j\theta-\pi/2)/2,\qquad
D_\beta=\operatorname{diag}(1+i\beta(t_j)),
                                                                    \tag{7}
\]
with the fixed smooth \(\beta\) from that theorem.
Its principal lower bound holds on the closed interval
\(0\le t\le\pi/4\).

The same proof applies at the extra row \(D\). Here
\(t_D=\pi/4-\theta/2\), \(S_D=N>0\), and the exact diagonal
formula of the full-tail theorem is still valid. Every interior
link has sine-product-conjugated magnitude \(s_{j+1}^{3/2}\).
The absent last link is \(C_D=0\). In the lower quadratic bound
its harmless comparison term is \(s_{D+1}^{3/2}=s_N^{3/2}=0\);
no norm with weight \(S_N\) is formed. The Lipschitz estimate
for \(x^{3/2}\) on \([0,2]\) includes this endpoint.
The variable-row commutator is unchanged.

Consequently, for all sufficiently large \(N\), uniformly over
all such intervals and \(Z\in\mathfrak Z\),
\[
\begin{split}
\Re\langle x,D_\beta W_N(\mathcal J_{I,N}-ZI)x\rangle_{S,I}
 &\ge\frac1{20}\|x\|_{S,I}^2,\\
G_I(Z):=(\mathcal J_{I,N}-ZI)^{-1},\qquad
\|G_I(Z)\|_{S\to S}&\le20\sqrt{10},\\
|(G_I)_{i,j}|
 &\le40\sqrt{10}\sqrt{S_j/S_i}\,e^{-\gamma|i-j|},
 \qquad\gamma=\log(1+1/2400).
\end{split}                                                       \tag{8}
\]
All constants are those of the full-tail theorem. In particular
these estimates are independent of the trailing endpoint.

There is also a fixed zero-free complex neighborhood of
\(\mathfrak Z\). Changing \(Z\) to \(Z+\delta Z\) changes the
rotated matrix in (8) by norm at most
\(\sqrt{10}|\delta Z|\). For example
\(|\delta Z|<1/(80\sqrt{10})\) leaves a positive lower bound.
This observation is used only for holomorphy, not to assert
unchanged constants outside (6).

## 3. Exact determinants and every physical ratio

For \(M\le b\le D\), define the trailing determinant
\[
\Delta_b(Z)=\det(\mathcal J_{[b,D],N}-ZI),\qquad
\Delta_{D+1}=1,\quad \Delta_{D+2}=0.
                                                                    \tag{9}
\]
Direct tridiagonal expansion gives
\[
\Delta_b=(B_b-Z)\Delta_{b+1}
                              -C_bA_{b+1}\Delta_{b+2}
                             \quad(b<D),
\qquad \Delta_D=B_D-Z.                                             \tag{10}
\]
The \(A_{D+1}\) term is not needed in the last equation.
Every \(A_b\), \(M\le b\le D\), is nonzero because \(Y_b\ne1\).

The complete homogeneous recurrence, solved backwards from (4),
therefore gives exactly
\[
\alpha_{b-1}
 =\frac{(-q)^D\,\Delta_b}
             {q^{D-b+1}\prod_{h=b}^{D}A_h}.
                                                                    \tag{11}
\]
To verify the induction, solve (3) for \(\alpha_{b-1}\).
Substituting the two next formulas leaves
\((B_b-Z)\Delta_{b+1}-C_bA_{b+1}\Delta_{b+2}\), precisely
(10). The starting value is the direct identity (5).

Dividing (11) by \((-q)^{b-1}\) proves the ordinary polynomial
identity
\[
\boxed{\quad
\Delta_b(Z)
 =(-1)^{D-b+1}
       \left(\prod_{h=b}^{D}A_h\right)
                 C_{0,N}(r^{b-1},Z),
                  \qquad M\le b\le D.
\quad}                                                            \tag{12}
\]
No parity-dependent factor or extra \(N\) remains.
The degree is \(D-b+1\); its determinant leading coefficient
is \((-1)^{D-b+1}\). All polynomial equalities hold for
every complex \(Z\), independently of the energy domain.

By (8), every determinant (9) is nonzero on (6) and its
fixed neighborhood. Thus all polynomials
\[
C_{0,N}(r^{b-1},Z),\qquad M\le b\le D,
                                                                    \tag{13}
\]
are zero-free there. The final value \(c_D=1\) is also nonzero.
This is a statement about complete finite sums, including all
numerator zeros and phases, not about a selected saddle.

For \(I_b=[b,D]\), its first diagonal cofactor gives
\[
(G_{I_b})_{b,b}=\Delta_{b+1}/\Delta_b.
\]
Hence both exact ratio conventions are
\[
\boxed{\quad
\frac{\alpha_b}{\alpha_{b-1}}
       =qA_b(G_{I_b})_{b,b},\qquad
\frac{C_{0,N}(r^b,Z)}{C_{0,N}(r^{b-1},Z)}
       =-A_b(G_{I_b})_{b,b},
                   \qquad M\le b\le D.
\quad}                                                            \tag{14}
\]
The minus sign in the unsigned ratio is the original
\((-q)^b\) normalization. These are exact finite identities;
no limiting characteristic root has been substituted.

The entire first Green column is similarly explicit:
\[
\boxed{\quad
(G_{I_b})_{i,b}
 =q^{\,i-b}\left(\prod_{h=b+1}^{i}A_h\right)
                     \frac{\Delta_{i+1}}{\Delta_b}
 =\frac{\alpha_i}{qA_b\alpha_{b-1}},
                   \qquad b\le i\le D.
\quad}                                                            \tag{15}
\]
The empty product is one. One may prove the first equality
by cofactors, or the second by applying (8) to the exact
homogeneous source restriction
\[
(\mathcal J_{I_b,N}-ZI)\alpha_{I_b}
                           =qA_b\alpha_{b-1}\mathbf e_b.
\]
There is no upper exterior contribution at \(D\).

For completeness, (8),(15), and \(|\alpha_D|=1\) give the
finite lower estimate
\[
|C_{0,N}(r^{b-1},Z)|
 \ge\frac1{80\sqrt{10}}\sqrt{S_D/S_b}\,
                                 e^{\gamma(D-b)}
                   \qquad(Z\in\mathfrak Z),                       \tag{16}
\]
using \(|A_b|\le2\). This supplies a modest quantitative
nonvanishing estimate. It is not a small upper bound for
the remaining observation.

## 4. The cutoff boundary can be replaced by the complete value

Let \(I=[M,D]\), \(\lambda_i=\phi_N(R^3e_iQ_N^{\rm full})\),
and
\[
v=G_I(Z_*)^{\mathrm t}\lambda_I.                                  \tag{17}
\]
This new test uses the interval through \(D\). It is not
identified with the test on \([M,D-1]\). The original retained
source still satisfies the exact identity
\[
\sum_{i=M}^{D}\lambda_i a_i
  =-\sum_{i=M}^{D}v_if_i+qA_Mv_Ma_{M-1}.                           \tag{18}
\]
At the new row \(D\), both \(a_D\) and \(f_D\) vanish for
the sufficiently large levels under consideration.

Every source bound in Section 5 of the full-tail theorem also
holds on \([M,D]\). Specifically
\[
\max_{M\le i\le D}|\lambda_i|
 \le C_\tau N^{A_\tau}e^{N(\mathfrak M_3+\tau)},\qquad
\mathfrak M_3<121/63,
\]
\[
1\le S_i\le C N^{1/2}2^{N/3},\qquad
S_M\asymp N^{1/2}.
                                                                    \tag{19}
\]
Its proof already establishes the radical quotient bound through
\(D\), and the added endpoint is \(S_D=N\). Thus the full
transformed forcing in (18), with the original \(\kappa^{-2}/N\),
still has gap \(1/25\) below \(419/200\).

The difference between complete and retained lower boundary
values has a separate small-row bound:
\[
\alpha_{M-1}-a_{M-1}
 =(-q)^{M-1}\sum_{k=0}^{K}
           \frac{Y_{M-1}^{-k}p_k(Y_{M-1})p_k(Z_*)}{P_k^2},
\qquad
|\alpha_{M-1}-a_{M-1}|\le C N e^{N/200}.
                                                                    \tag{20}
\]
To check its endpoint eligibility, the physical stop is
\(D-(M-1)=\lfloor N/2\rfloor\). Factorial reflection gives,
for \(n=\lfloor N/2\rfloor\),
\[
|R_{M-1,k}(Z_*)|
       =\frac{S_n}{S_{n-k}S_k^2}|p_k(Z_*)|
       \le\frac{(30/7)^k}{S_k^2}.
\]
The sine-chord and factorial estimate of
[small outgoing indices, Section 2](research_mixed_next_three_small_outgoing_indices.md)
therefore applies unchanged at \(k\le K\), including the
zero row. The earlier condition \(b\ge M\) is not required
for this explicit product comparison: \(n\le N/2\) suffices.

From (8),(17),(19),
\[
|v_M|\le\sqrt{S_M}\|v\|_{S^{-1}}
   \le20\sqrt{10}\sqrt{S_M}\|\lambda_I\|_{S^{-1}}
   \le C_\tau N^{A_\tau}e^{N(\mathfrak M_3+\tau)}.
\]
Since \(|A_M|\le2\), (20) gives a boundary-replacement cost
with rate at most \(\mathfrak M_3+1/200+\tau\).
The exact strict reserve is
\[
\frac{419}{200}-\frac{121}{63}-\frac1{200}
       =\frac{1067}{6300}>\frac16>\frac17.                         \tag{21}
\]
After tolerances and polynomial factors, this proves
\[
\left|\frac{qA_Mv_M}{\kappa^2N}
                        (\alpha_{M-1}-a_{M-1})\right|
       \le C e^{N(419/200-1/7)}.                                  \tag{22}
\]
This is an actual bound after the new inverse, not an
assumption that a relative cutoff error is small.

The positive high-band restoration of the full-tail theorem
is unchanged. Hence its original middle observation obeys
\[
\boxed{\quad
\mathscr R_N
 =\frac{qA_M\alpha_{M-1}}{\kappa^2N}\,v_M
                       +O(e^{N(\Lambda-1/200)}).
\quad}                                                            \tag{23}
\]
Here the error includes the paid restored high band, the entire
transformed forcing, and the new boundary replacement.
The original scalar and all source phases have been retained.

## 5. What the determinant formula does and does not simplify

Combining (15),(17) gives the exact identity
\[
\boxed{\quad
qA_M\alpha_{M-1}v_M
       =\sum_{i=M}^{D}\lambda_i\alpha_i
       =\sum_{i=M}^{D}(-q)^i
                       \lambda_i C_{0,N}(r^i,Z_*).
\quad}                                                            \tag{24}
\]
Equivalently
\[
v_M=\frac1{\Delta_M}
 \sum_{i=M}^{D}\lambda_i q^{i-M}
        \left(\prod_{h=M+1}^{i}A_h\right)\Delta_{i+1}.
                                                                    \tag{25}
\]
The denominator in (25) is the explicitly zero-free connection
polynomial (12), times its known scalar. The numerator still
contains every original coherent inner period. Multiplying
by the actual complete boundary value cancels that determinant
and restores precisely (24).

Thus the determinant identification is useful for analyzing the
actual finite ratio (14), for example by a separately proved
resolvent comparison. It does not by itself reduce the required
cancellation estimate in (24) to a determinant norm estimate.
The energy bound controls the Green operator in its stated
sine-product metric; it does not assign a sufficient action to
the original \(\lambda\)-weighted numerator.

The complete transfer therefore remains
\[
\mathcal T_0[F_N](-2,Z_*)
 =I_{{\rm geom},N}
  +\frac1{\kappa^2N}\sum_{i=M}^{D}(-q)^i
                  \lambda_i C_{0,N}(r^i,Z_*)
  +O(e^{N(\Lambda-\epsilon_0)}),
\]
with the same positive choice
\(\epsilon_0=\min(\epsilon_*,1/200)\).
This writes the one remaining boundary connection in complete
finite-source form; it does not prove it smaller than the
nonzero geometric integral. No free-boundary or normalized-jet
extension is claimed.

## Frozen source bindings

- Full-tail weighted energy:
  0037a31d5f2a8cedea53d70bf1f0434f906668fe0934e5ee303890a8b3eceee7.
- Original middle weighted energy:
  fdcc1fab386fd94047022c04911d0f5874768674dd546aef33985b54a758b372.
- Paired finite recurrences:
  8372ed7387b7465b6a66cc207f2ac8e3803e3def10d7beff115c038d4334c909.
- Transformed forcing:
  840126070ec5c85f8e6dd0c5423515e2027a2191a62bd08ffc51a6f237e5773b.
- Small outgoing source:
  6905d51ca102e2686d9b9845cfe333017ddcbcf45a70dbcf10741438f31dc1f0.
- Original outer observation:
  cbbc62951666d06e0ae77b29f49f563d91c2024dc8da900ae996144d7db39dab.

All proof steps are exact written identities or inequalities.
No numerical evaluation or replay was performed.

