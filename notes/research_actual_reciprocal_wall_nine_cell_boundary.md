# The actual reciprocal wall on the nine-cell boundary

Private written proof, 17 November 2026.

The finite wall in the original middle five-point chart has an explicit
local transport to the paired boundary faces of the proved nine-cell
source. Its factorial gauge sees the exact endpoint factor \(N^2\).
After the remaining crossing factor and the actual Fourier adapter, the
original wall has rank \(N\) and norm \(N\). Its lowering-current defect
is retained, with norm \(N|Q^{-1}-1|\), and changes the total boundary
character by one. This is not an identification with the entire
negative-ray current of a full-function period.

## 1. Original operators and insertion

Fix odd \(N>2\), \(Q=e^{2\pi i/N}\), \(s=e^{\pi i/N}\), \(d=N-1\),
\[
 x=-s^{-1},\qquad \lambda=x^{-1}=Qx,\qquad x^N=\lambda^N=1.
 \tag{1}
\]
Bracketed indices are reduced to \(0,\ldots,d\). First use the original
unit wrap \(S_1^N=S_2^N=1\). The complete balanced matrices [S] are
\[
 Z|a\rangle=Q^a|a\rangle,\quad K=xZ^{-1},\quad f=(1-Z)S,\quad
 e|a\rangle=\lambda(1-Q^{-a})|a-1\rangle ,
 \tag{2}
\]
with the last arrow zero at \(a=0\). Put
\[
 p_a=(Q;Q)_a,\quad
 P(T)=\sum_{h=0}^d\frac{(-1)^hQ^{h(h-1)/2}}{p_h}T^h,\quad
 n=e_1S_2,\quad B=-e_1Z_2S_2.
 \tag{3}
\]
The original uncheck crossing [M], with its common scalar Cartan line
retained externally, is
\[
 R_0=DP(B)P(n),\qquad
 D|a,b\rangle=x^{-a-b}Q^{ab}|a,b\rangle .
 \tag{4}
\]
The diagonal also follows from the zero-transfer coefficient [S,(11)].

The actual reciprocal coordinate and wall are
\[
 X=xS_2S_1^{-1},\quad W=E_dX=x|d\rangle\langle0|\otimes S_2,\quad
 U=\Gamma n\Gamma^{-1},\qquad (1-QZ_1)U=X-W,
 \tag{5}
\]
\[
 \Gamma|a\rangle=g_a|a\rangle,\quad
 g_a=(-1)^aQ^{-a(a-1)/2}p_a^2,\quad g_0=1,\quad g_d=Q^dN^2 .
 \tag{6}
\]
These are [M,(8)--(10)], with the finite endpoint retained.
The particular original-head insertion transported here is
\[
 R_W=DP(B)\,W\,P(n)
     =DP(B)\Gamma^{-1}(g_dW)P(U)\Gamma .
 \tag{7}
\]
Inserting bare \(W\) between \(\Gamma^{-1}\) and \(P(U)\) would
instead give \(g_d^{-1}R_W\). These two coupons are distinct.

For the original total lowering matrix \(H=f_1+K_1^{-1}f_2\),
\[
 J=[H,W]=(Q^{-1}-1)|d\rangle\langle0|\otimes S_2^2,\qquad
 [K_1K_2,W]=0.
 \tag{8}
\]
Indeed \(f_1W=Wf_1=0\), \(K^{-1}|d\rangle=x|d\rangle\), and
\(fS-QSf=(1-Q)S^2\); use \(x^2=Q^{-1}\).
The current insertion is \(R_J=DP(B)JP(n)\).

## 2. Remaining-factor transport, including every endpoint

Let \(L=DP(B)\) and \(W_r=x|d\rangle\langle0|\otimes S_2^r\).
Then \(W=W_1\) and \(J=(Q^{-1}-1)W_2/x\).
Nilpotence and the finite binomial identity give
\(P(B)^{-1}=\sum_{h=0}^d B^h/p_h\).
Direct multiplication of (2) yields, for \(0\le h\le a\),
\[
 (B^h)_{a-h,[b+h];a,b}
 =\lambda^hQ^{h(b-a)+h^2}\frac{p_a}{p_{a-h}} .
 \tag{9}
\]
The entire column and row needed for the wall are consequently
\[
 \begin{split}
 P(B)|d,b\rangle
   &=\sum_{h=0}^d\lambda^hQ^{h(b+h)}|d-h,[b+h]\rangle,\\
 (P(B)^{-1})_{0,[a+b];a,b}&=\lambda^aQ^{ab}.
 \end{split}                                                     \tag{10}
\]
For the first use
\(p_d/(p_{d-h}p_h)=(-1)^hQ^{-h(h+1)/2}\); the second is the
term \(h=a\) in the inverse. Both include all endpoints.

After \(W_r\), put \(h=d-u\) in the first line and apply the Cartan
ratio. The complete result is
\[
 \boxed{(LW_rL^{-1})_{u,v;a,b}
 =Q^{-b-1}x^{a-u+r-1}\delta_{v,[a+b+r-1-u]}.}
 \tag{11}
\]
For a phase check, before the Cartan ratio the \(Q\)-exponent is
\(ab+h([a+b+r]+h)\); that ratio adds \(uv-ab\), giving \(dv\).
The remaining \(\lambda\)-powers give (11).

At \(r=1\), each total-clock block is rank one, with \(N\) by \(N\)
entries of modulus one. Distinct blocks have orthogonal source and
target spaces. The same argument applies to \(r=2\), so
\[
 \|LWL^{-1}\|_2=N,\qquad
 \|LJL^{-1}\|_2=N|Q^{-1}-1|.
 \tag{12}
\]
The bare reciprocal coupon in (7) has exterior norm \(1/N\).
Separate exponential bounds on \(\Gamma^{\pm1}\) would lose this
exact polynomial endpoint calculation.

For the original common wrap \(S_1^N=S_2^N=\mu\ne0\), use
\(W_r=x\mu^{-1}|d\rangle\langle0|\otimes S_2^r\).
Then (11) has the additional factor
\[
 \mu^{\lfloor(a+b+r-1-u)/N\rfloor}.
 \tag{13}
\]
Choose a local \(\zeta^N=\mu\) and \(T_\zeta|a\rangle=\zeta^a|a\rangle\).
Conjugating by \(T_\zeta\otimes T_\zeta\) removes (13) and leaves
\(\zeta^{r-1}\) times (11). The total degree changes by
\(r-1-N\lfloor(a+b+r-1-u)/N\rfloor\), proving this also at the seam.
The original \(R_0\) conserves ordinary integer degree and commutes
with this gauge. At unit marks it is unitary; on compact nonzero
\(\mu\)-domains it and its inverse have uniform bounds and
fixed-order parameter derivatives. Below \(\mu=1\); under this
optional gauge the current acquires the specified \(\zeta\).

## 3. The actual planar Fourier adapter

Let \(F_{ia}=N^{-1/2}Q^{ia}\), \(\mathcal F=F\otimes F\), and
\(D_x|a\rangle=x^a|a\rangle\). The original coefficient [S,(11)]
before the flip is
\[
 (R_0)_{a-h,b+h;a,b}
 =x^{-a-b-h}Q^{ab-(b+1)h}
       \frac{p_ap_{b+h}}{p_{a-h}p_bp_h}.
 \tag{14}
\]
The literal Fourier matrix \(A=\mathcal F^{-1}R^o\mathcal F\)
in [P,(1.1)] has the same support and factorial ratio, with phase
\(Q^{1+(a-h)(b+1)}\). Their ratio is \(Qx^{b-(a-h)}\), giving
\[
 A=Q(D_x^{-1}\otimes I)R_0(I\otimes D_x).
 \tag{15}
\]
All displayed matrices besides \(R_0,A\) are unitary. An exterior
left coupon \(C\) becomes
\(\mathcal F(D_x^{-1}\otimes I)C(D_x\otimes I)\mathcal F^{-1}\).
No factorial similarity is omitted.

Applying this to (11) gives
\[
 (C_r)_{\rm pl}
 =NQ^{-1}\sum_{i=0}^d(\lambda Q^i)^{r-1}
                         |i,i+1\rangle\langle i,i|.
 \tag{16}
\]
For clarity, the pre-Fourier \(r=1\) matrix is
\(Q^{-v-1}\delta_{u+v,a+b}\). In \(\mathcal F C\mathcal F^{-1}\)
its exponent is
\((i-j+1)u+(j-1-k)a+(j-1-l)b-1\), so the output is
\((i,j)=(i,i+1)\) and the input is \((k,l)=(i,i)\).
This fixes the Fourier sign. Thus
\[
 \boxed{C_{\rm pl}=NQ^{-1}\sum_i|i,i+1\rangle\langle i,i|,
 \quad
 J_{\rm pl}=N(Q^{-1}-1)\sum_iQ^i|i,i+1\rangle\langle i,i|.}
 \tag{17}
\]

The specified unbraided matrix obeys
\(R^o_{i,j;k,l}=R_{\rm can}(i,j,k,l)Q^{k+l}\).
Its input factors are untouched by a left coupon. Therefore
\[
 (R_W)_{\rm can}(i,j,k,l)
 =NQ^{-1}\delta_{j,i+1}R_{\rm can}(i,i,k,l).
 \tag{18}
\]
In [P]'s actual composition support, equal first two indices give
\(u=[j-i-1]=d\), forcing the other three composition indices to zero.
Using \(p_d=N\) proves
\[
 R_{\rm can}(i,i,k,l)=Q^{1-2i}\delta_{k,i}\delta_{l,i},
\]
\[
 \boxed{\begin{split}
 (R_W)_{\rm can}&=NQ^{-2i}\delta_{j,i+1}\delta_{k,i}\delta_{l,i},\\
 (R_J)_{\rm can}&=N(Q^{-1}-1)Q^{1-i}
                         \delta_{j,i+1}\delta_{k,i}\delta_{l,i}.
 \end{split}}                                                   \tag{19}
\]
Their matrix norms are exactly \(N\) and \(N|Q^{-1}-1|\le2\pi\).
These are local inserted-crossing bounds, not bounds for an arbitrary
exterior contraction.

## 4. Literal paired-face operators and cyclic seams

Use [A] unchanged. On the first two output ports set
\[
 k_m=\alpha_{m,-}-\alpha_{m,+}+h_m,\quad
 l_m=\beta_{m,-}-\beta_{m,+}+h_m,\quad
 f_m(k)=a_m^{[k-1]}b_m^{[-k]} .
 \tag{20}
\]
Here \(a_m=s_{0m}\), \(b_m=s_{m5}\).
The actual adapter and inverse dual have entries
\[
 \mathcal A_m(\alpha;j)=f_m(k_m)Q^{jk_m},\qquad
 \mathcal L_m(j;\beta)=\frac{Q^{-jl_m}}{N^2f_m(l_m)}.
 \tag{21}
\]
Summing the single index in (17) gives the full face kernels
\[
 \boxed{\mathcal W_{\alpha;\beta}
 =\frac{Q^{k_2-1}}{N^2}
   \frac{f_1(k_1)f_2(k_2)}{f_1(l_1)f_2(l_2)}
                  \delta_{k_1+k_2,l_1+l_2},}
 \tag{22}
\]
\[
 \boxed{\mathcal J_{\alpha;\beta}
 =\frac{(Q^{-1}-1)Q^{k_2}}{N^2}
   \frac{f_1(k_1)f_2(k_2)}{f_1(l_1)f_2(l_2)}
                  \delta_{k_1+k_2-l_1-l_2,-1}.}
 \tag{23}
\]
They act on the simultaneous-translation invariant paired images
and kill their specified complementary kernel. The other two ports
retain the identity on their paired images.
The current is nonzero and lowers the total boundary character by one.

Every seam is retained. In particular,
\[
 \frac{f_m(k+1)}{f_m(k)}
 =\frac{a_m}{b_m}
   \left[1+\left(\frac{b_m^N}{a_m^N}-1\right)\delta_{k0}\right].
 \tag{24}
\]
Neither the seam nor the inverse dual \(f_m(l)^{-1}\) is replaced
by an unwrapped progression or a Hermitian adjoint.

When the decoration differences \(a_m^N,b_m^N\) range over compact
nonzero sets, [A]'s normalized adapters and inverse on the image are
uniformly bounded. Hence
\[
 c_KN\le\|\mathcal W\|_2\le C_KN,\qquad
 c_KN|Q^{-1}-1|\le\|\mathcal J\|_2\le C_KN|Q^{-1}-1|.
 \tag{25}
\]
Fixed-order decoration derivatives have the corresponding upper
bounds. No genuine-\(Q\) or meridian-normal derivative is used.

## 5. Actual nine-cell insertion and sector transport

The proved canonical identity [C] is
\[
 \mathcal B=C_N(\mathbf s)Q^{3(h_1-1)/2}s_{05}^{d}
 \sum_{\mathbf i}R_{\rm can}(\mathbf i)
                       \prod_{m=1}^4 f_m(k_m)Q^{i_mk_m}.
 \tag{26}
\]
Applying (22)--(23) to its first two ports, equivalently substituting
(19), gives the all-boundary identities
\[
 \boxed{\begin{split}
 \mathcal B_W&=
 N^2C_NQ^{3(h_1-1)/2+k_2}s_{05}^{d}
          \prod_m f_m(k_m)\,\delta_{\sum k_m,2},\\
 \mathcal B_J&=
 N^2(Q^{-1}-1)C_NQ^{3(h_1-1)/2+1+k_2}s_{05}^{d}
          \prod_m f_m(k_m)\,\delta_{\sum k_m,1}.
 \end{split}}                                                   \tag{27}
\]
The arbitrary physical exterior and its inverse dual are unchanged.
In particular the actual \(C_N\), its phase and all lifted roots
remain in the identity. No whole-cut scalarity is used.

For distinct real decorations and real odd roots, [C] proves
\(|C_N|=N^{-2}\). On fixed compact noncollision decoration sets,
every other absolute factor in (27) is bounded above and below.
Each support has \(N^7\) literal eight-face assignments. Thus these
unnormalized Euclidean array norms are respectively
\(\Theta_K(N^{7/2})\) and \(\Theta_K(N^{5/2})\).
This is a local source bound with its actual scalar retained.

For clarity, canonical support is not imposed after an untransported
sector change. Let \(\chi=(\chi_0,\chi_1,\chi_2,\chi_3)\), \(\sum\chi_i=1\),
and set \(\beta=1-\chi_0,\gamma=\chi_2+\chi_3,\delta=\chi_3\).
The literal covariance of [C] is
\[
 R_\chi(i,j,k,l)
 =Q^\gamma R_{\rm can}(i,j+\beta,k+\gamma,l+\delta).
 \tag{28}
\]
Transporting the wall with these same port shifts yields
\[
 (R_W)_\chi=NQ^{\gamma-2i}
 \delta_{j,i+1-\beta}\delta_{k,i-\gamma}\delta_{l,i-\delta};
 \tag{29}
\]
the current has the same support and phase
\(N(Q^{-1}-1)Q^{\gamma+1-i}\).
The first-two-port kernels (22)--(23) acquire
\(Q^{-\beta(k_2-l_2)}\). The full nine-cell sector scalar is the
one in [C] and stays external. An unchanged canonical coupon in
the shifted coordinates would be a different insertion.

## 6. Current and analytic scope

Writing \(H_L=LHL^{-1}\), the actual current equation is
\[
 [H_L,LWL^{-1}]=LJL^{-1}.
 \tag{30}
\]
The right side has been evaluated explicitly in (17),(23),(27),
not discarded. All dual rows use the literal inverse adapters.
The partial-factor generator \(H_L\) is not asserted to be the
unchanged external coproduct. The weight commutator remains zero,
since \(L\) commutes with \(K_1K_2\).

This is a local realization of the specified finite reciprocal wall
and lowering defect on the actual nine-cell boundary. It neither
makes the wall Hopf-natural nor relocates it to the marked cut.
It does not identify it with the full negative-ray atomic current,
its intersections, or its continuous cycle: those functions and
chains still require their own source-preserving transport.
All formulas are at the complete fixed odd root. Decoration
derivatives do not supply a generic-meridian or off-root quantum
identity. No selected geometric coefficient or whole scalar lower
is inferred.

## Direct sources and readback

The complete target and all five complete direct texts are read
before freezing, with matching hashes renewed. Only written
mathematics, file reads and hashes are used.

* [M](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_middle_five_point_wall_factorization.md),
  SHA256 a3c9d055fd2acc763f746113379987bfefddb46431a14577067dabb1a46dbcd7:
  exact two-factor crossing, reciprocal wall and factorial gauge.
* [S](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_shared_quantum_flags_and_charged_exchange.md),
  SHA256 dcab795cc141e2e1db726998cf7b1141dd03c681eaae9076387f90581f53a7d9:
  original balanced matrices, crossing coefficients and currents.
* [P](kashaev_crossing_and_period_lattice.md),
  SHA256 71e67223742fe905af47d0475435f3a13acc877695bd0cdc321798cf2e608037:
  literal Fourier crossing and canonical composition support.
* [A](research_kashaev_paired_face_boundary_adapter.md),
  SHA256 c430fd2714acdc7588003e1c18c60453e1ebe123bd7c0155d20a0eef639ec8ed:
  paired image, inverse dual, cyclic seam and uniform bounds.
* [C](research_nine_cell_canonical_crossing_evaluation.md),
  SHA256 332062e67d64ab4a0767637c0fdd96f186d62c430ad38042aef35ad857d8d7c9:
  actual all-boundary identity and retained scalar modulus.
