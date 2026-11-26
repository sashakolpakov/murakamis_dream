# Signed grade blocks for the original bipyramidal source

This note continues the exact cyclic transfer without changing its source or taking absolute values of local coefficients. It gives an exact polynomial functional-calculus factorization of the north rows, a coefficient formula for the south rows, and the precise shared remainder estimate that would be sufficient for long filling. The estimate itself remains unproved.

The fixed diagram is the opposite-offset bipyramid of even size \(m\ge6\), with the original orientations, protected mark and knot-parity data of the cyclic source note. The quantum level is \(N\), \(d=N-1\), \(q=e^{\pi i/N}\). The north variable is denoted \(X\), to distinguish it from \(N\), and the south variable is \(S\). The original ordered factors are
\[
 F_j=
 \begin{cases}
 H_{f_j}(0,z_{j-1},z_{j+1},z_j),&j\text{ odd},\\
 H_{f_j}(S,z_{j+1},z_{j-1},z_j),&j\text{ even}.
 \end{cases}
 \tag{1}
\]
Here \(z_0\) has target zero, all other equatorial variables have target \(d\), and the one common south variable has target \(d\). This is the source-normalized homogeneous coupon \(H_f\), including all repeated-root data. A functional-calculus polynomial below is the actual \(f_j\), not its nodal-value interpolation.

## 1. The one-protected-face matrix

Put
\[
 c_r=q^{2r+1}+q^{-2r-1},\qquad
 s_r=2\sin\frac{\pi r}{N}.
 \tag{2}
\]
On the ordered monomial basis \(1,z,\ldots,z^d\), define
\[
 C(S)z^r=c_rz^r-s_r^2(1+S)z^{r-1}
                  -s_rs_{r-1}S z^{r-2},\qquad C=C(0).
 \tag{3}
\]
Missing endpoint terms are zero. This is precisely minus the original face operator with outer variables \(S,1\). It is upper triangular in the usual column-action convention. In particular \(C\) is upper bidiagonal, with entry \(-s_r^2\) in row \(r-1\), column \(r\).

Use \((x,B,C_*,Y)\) for the four ordered face variables, so that the matrix \(C\) is not confused with the output face \(C_*\). The homogeneous definition of \(H_f\) gives the finite identities
\[
 [B^aY^bC_*^c]H_f(0,B,C_*,Y)
       =f(C)_{a,d-c}\quad(a+b+c=d),
 \tag{4}
\]
\[
 [S^pB^cY^bC_*^a]H_f(S,B,C_*,Y)
       =[S^p]f(C(S))_{c,d-a}
       \quad(p+a+b+c=d).
 \tag{5}
\]
The exponent names \(a,b,c\) are integer indices. In (4) the input monomial has degree \(d-c\), the output middle degree is \(a\), and its lost degree is the remaining outer degree \(b\). Formula (5) has input degree \(d-a\), output degree \(c\), and outer degrees \(p,b\). Thus no interchange of the bottom middle faces is made. These are polynomial identities, including at every spectral collision.

## 2. Exact north and south grade blocks

In the cyclic transfer let the incoming state be \((u,v)\), the outgoing state \((u',v')\), and its grade be \(g=u+v\). At an ordinary target the local exponents are
\[
 a=d-u,\qquad b=u'-v,\qquad c=v'.
 \tag{6}
\]
The north row has \(a+b+c=d\), so it preserves \(g\). Set
\[
 I_g=\{\max(0,d-g),\ldots,\min(d,2d-g)\},
 \qquad i=d-u,\quad i'=d-u'.
 \tag{7}
\]
The endpoints of \(I_g\) add to \(2d-g\). Let \(J_g\) reverse this interval, and let \(C_g\) be the principal block of \(C\) on \(I_g\). Then the exact north-row transfer on grade \(g\), in these coordinates, is
\[
                  \mathsf O_{f,g}=f(C_g)J_g.
 \tag{8}
\]
Indeed \(d-v'=2d-g-i'\), so (4) gives precisely the corresponding entry of \(f(C)J_g\). Any upper-triangular path between two indices in the interval stays in the interval. Consequently \(f(C)_{I_g,I_g}=f(C_g)\), for every polynomial \(f\); this proves (8) without discarding normal derivatives.

For the south rows it is more convenient to retain the coordinate \(u\). Put
\[
 K_g=\{\max(0,g-d),\ldots,\min(d,g)\},\qquad
 A_{f,p}=[S^p]f(C(S)).
 \tag{9}
\]
An \(S\)-degree \(p\) lowers the grade from \(g\) to \(g-p\). The exact rectangular block, with incoming \(u\in K_g\) and outgoing \(u'\in K_{g-p}\), is
\[
 \mathsf E_{f;g,p}(u,u')
            =(A_{f,p})_{g-p-u',u}.
 \tag{10}
\]
This follows from (5), since the output middle exponent is \(v'=g-p-u'\), and the input middle degree is \(d-a=u\). Equivalently, if \(J_{K_{g-p}}\) reverses the output interval,
\[
 \mathsf E_{f;g,p}
       =(A_{f,p}|_{K_{g-p},K_g})^{\mathsf T}
                                      J_{K_{g-p}}.
 \tag{11}
\]
This is a coefficient of the *whole* polynomial \(f(C(S))\); expanding it into absolute monomer and dimer weights would lose the cancellations it records.

The marked-target north row is \(j=1\). It has \(u=0\), incoming grade \(g=v\le d\), and outgoing grade \(d+g\). Its entry is
\[
 \mathsf M_f\bigl((0,v),(u',v')\bigr)
       =f(C)_{0,d-v'},\qquad u'+v'=d+v,
 \tag{12}
\]
with \(0\le u',v'\le d\); all other entries are zero. The marked row is not an ordinary block (8).

## 3. The full nonincreasing grade path

Cut the cyclic product just after row \(j=1\). Choose the state \((0,v)\) before that row and its state after it. The grade immediately after the marked row is \(d+v\). Through rows \(2,3,\ldots,m-1,0\), every north row preserves grade and every south row lowers it by its actual integer \(p_j\ge0\). The state finally returns to \((0,v)\). Hence every closed path satisfies
\[
 d+v=g_2\ge g_3\ge\cdots\ge g_{m+1}=v,
 \qquad
 \sum_{\substack{j\ \mathrm{even}\\0\le j<m}}p_j=d.
 \tag{13}
\]
Here the cyclicly ordered rows are \(2,\ldots,m-1,0\); repeated grades occur at north rows. The inequalities include both endpoint states, not only the grade totals.

The exact source is therefore the sum of the entries of the products of (8), (10), and (12), over these grade sequences and their compatible internal states. This is simply the trace identity with its \(S\)-degree exposed. It retains a single common \(S\)-degree \(d\), all original equatorial demands, and all coefficient signs. In particular a product containing only \(p=0\) south blocks cannot close around the marked row.

Here is an explicit closed product formula. Let \(P_g\) be the diagonal projector onto states of grade \(g\), and order the rows as
\[
 (r_0,r_1,\ldots,r_{m-1})=(1,2,\ldots,m-1,0).
 \tag{13a}
\]
For \(0\le v\le d\) and nonnegative even-row drops \(\boldsymbol p\) with sum \(d\), set \(\gamma_0=v\), \(\gamma_1=v+d\), and
\(\gamma_{k+1}=\gamma_k-p_{r_k}\) for \(1\le k<m\), with \(p_j=0\) at odd \(j\). Thus \(\gamma_m=v\). Put
\[
 B_N(v,\boldsymbol p)=
 \operatorname{tr}\prod_{k=0}^{m-1}
       \left(P_{\gamma_k}\mathsf T_{r_k}(1)
                                    P_{\gamma_{k+1}}\right).
 \tag{13b}
\]
Illegal grades give zero. The source equals \(\sum_{v,\boldsymbol p}B_N(v,\boldsymbol p)\). The projectors force the corresponding \(S\)-degree in every even row; evaluation at the one shared \(S=1\) therefore loses no information. The number of possible pairs \((v,\boldsymbol p)\) is at most
\[
       N\binom{d+m/2-1}{m/2-1}=O_m(N^{m/2}).
 \tag{13c}
\]
Each \(B_N\) still sums all compatible internal degree states with their original signs.

For the full resolvent source take \(f_j(z)=V_N(\sigma_j;z)\), where
\[
 \chi_N(z)=2T_N(z/2)+2,\qquad
 V_N(\sigma;C)=\chi_N(\sigma)(\sigma I-C)^{-1}.
 \tag{14}
\]
The latter denotes the resulting degree-\(d\) polynomial in \(\sigma\). For the CROSS source use its original path projection before constructing the blocks. One does not identify that path projection with a polynomial \(f(C_g)\) unless it follows separately from the original cutoff.

## 4. A genuine but limited positive form

Let \(J\) reverse the full index range \(0,\ldots,d\). The reflected coefficients satisfy
\[
 c_{d-r}=c_r,\qquad s_{N-r}=s_r,\qquad
                    JC(S)^{\mathsf T}J=C(S).
 \tag{15}
\]
Thus \(f(C(S))J\) is transpose-symmetric. At \(S=0\), grade \(g=d\) is the full interval, and for a polynomial \(f\) and its coefficientwise conjugate \(\bar f\),
\[
 \bigl(f(C)J\bigr)\bigl(\bar f(C)J\bigr)
             =f(C)\,\overline{f(C)}^{\mathsf T}
             =f(C)f(C)^* \succeq0.
 \tag{16}
\]
All matrices \(C\) here are real. For the actual crossing polynomial the full Hermite inverse is its coefficientwise conjugate modulo \(\chi_N\): its nodal values have modulus one and its inverse derivative is the conjugate derivative. Therefore the pair of powers \(a,-a\), in precisely the full-grade zero-drop configuration of (16), is an example. The original Cartan scalar is inside \(f\); it has not been dropped. The corresponding exact invariant Hermitian form is
\[
                    f_a(C)^*Jf_a(C)=J.
 \tag{16a}
\]
It is indefinite, since \(J\) has both signs for \(N\ge2\). Thus (16a) retains the original phases but supplies no bound in a positive norm by itself.

This positive form is not available for arbitrary original adjacent rows. Away from \(g=d\), reversal of \(I_g\) does not in general preserve the Casimir diagonal. Consequently (15) cannot be asserted with \(C_g,J_g\). Moreover the actual south blocks in (13) must have positive total drop \(d\); they are the coefficients (10), not arbitrarily chosen conjugate partners of (8). The two spectral parameters at adjacent boxes are independent as well. Equation (16) is an exact possible building block, not a positive realization of the entire source.

There is a further obstruction to replacing all these forms by one positive invariant norm. The full bidiagonal \(C\) is cyclic: all its superdiagonal entries are nonzero. Its minimal polynomial is \(\chi_N\), with double roots for \(N\ge3\). Hence \(C\) is not diagonalizable. It cannot be self-adjoint for a positive definite Hermitian form. For a nonzero integral crossing power, its actual Hermite data obey
\[
 f_a(2\cos\phi)=q^{ad^2/4}
       \exp\!\left(\frac{iaN(\phi-\pi)^2}{4\pi}\right),\qquad
 f_a'(2\cos\phi)=
       -\frac{iaN(\phi-\pi)}{4\pi\sin\phi}\,f_a(2\cos\phi).
 \tag{16b}
\]
The second formula is nonzero at every double root, using its representative \(0<\phi<\pi\). Therefore \(f_a(C)\) retains a nonzero Jordan part and cannot be unitary for a positive definite Hermitian form. This observation concerns the unturned \(f(C)\); it makes no unsupported assertion about diagonalizability of \(f(C)J\). A useful estimate must exploit the actual product and its grade constraints, or another correlated form.

## 5. The precise signed-product target and filling normalization

Let \(\mathsf T^{\mathrm{full}}_{j,N}(\sigma_j)\) be the exact source transfer at the one common gauge \(S=1\), and let \(\mathsf T^{\mathrm{C}}_{j,N}\) be its original CROSS projection. Define
\[
 D_N(\boldsymbol\sigma)=
  \operatorname{tr}\prod_{j=0}^{m-1}
                 \mathsf T^{\mathrm{full}}_{j,N}(\sigma_j)
  -
  \operatorname{tr}\prod_{j=0}^{m-1}
                 \mathsf T^{\mathrm{C}}_{j,N}(\sigma_j).
 \tag{17}
\]
Both products retain the marked step (12). The order is the original cyclic order. The next sufficient estimate is the following statement about this one signed scalar polynomial:
\[
 \boxed{\qquad
 \sup_{\boldsymbol\sigma\in[-2,2]^m}|D_N(\boldsymbol\sigma)|
       \le
 \exp\{N(\Phi_{\mathrm{drilled}}-\eta_m+o(1))\},
 \qquad \eta_m>0.
 \qquad}
 \tag{18}
\]
The diagram is fixed before \(N\), and the bound must hold along both level parities. Its normalization is
\[
                 \Phi_{\mathrm{drilled}}
                    =\frac{\operatorname{Vol}(Y)}{2\pi},
 \tag{19}
\]
for the original drilled augmented exterior \(Y\). An estimate at this rate for the *full* source alone does not prove a smaller fixed-filled rate. The strict loss in (18) is required for the complementary source.

For example, a stronger sufficient block inequality is
\[
 \sup_{\boldsymbol\sigma\in[-2,2]^m}
  |B_N^{\mathrm{full}}(v,\boldsymbol p;\boldsymbol\sigma)
       -B_N^{\mathrm{C}}(v,\boldsymbol p;\boldsymbol\sigma)|
   \le \exp\{N(\Phi_{\mathrm{drilled}}-\eta_m+o(1))\},
 \tag{18a}
\]
uniformly over the original allowed grade sequences. The polynomial count (13c) would then give (18). This is a proposed sufficient inequality, not an established one; cancellations between different grade sequences might instead be essential. Equations (8)–(13b) specify every boundary index and phase that it retains. A bound obtained by independently maximizing either endpoint, or by treating an arbitrary south row as the Gram partner in (16), would not prove (18).

To spell out the consequence, let \(a_j=\epsilon_j-2p_j\) be the actual fixed signed filling powers. The original full-Hermite functional satisfies the exact finite estimate
\[
 \left|\left(\bigotimes_j\mathcal L_N^{a_j}\right)D_N\right|
 \le
 \left[
 \prod_j\left(1+\frac{|a_j|}{2}\right)
 -
 \prod_j\left(\frac1N+\frac{|a_j|}{2}\right)
 \right]\|D_N\|_{[-2,2]^m}.
 \tag{20}
\]
This uses the fact that full and CROSS agree at the entire product node grid; it does not discard the double-root normal derivatives. Formula (20) is the source-normalized marked contraction, with no extra \(N^m\). The actual crossing's Cartan and square-root phases are already in the \(\mathcal L_N^{a_j}\). The original zero-framing/component character has modulus one at complete color, and any prescribed one-cut modified normalization is retained separately as its original polynomial factor. No sine, derivative or Fourier charge factor is to be appended a second time.

The independent all-CROSS long-filling theorem supplies a nonzero leading term with rate
\[
 \Phi_{\boldsymbol a}
      =\frac{\operatorname{Vol}(Y(\boldsymbol p))}{2\pi},
 \qquad
 \Phi_{\boldsymbol a}
      =\Phi_{\mathrm{drilled}}-O_Y\!\left(\sum_j|a_j|^{-2}\right).
 \tag{21}
\]
Its actual primitive words and knot-parity hypotheses remain necessary. If (18) were proved, independently sufficiently long fixed signed powers would make
\(\Phi_{\boldsymbol a}>\Phi_{\mathrm{drilled}}-\eta_m/2\). Equations (18)–(20) would then make the entire complementary source exponentially smaller than that nonzero CROSS term, proving the full original invariant's volume limit. The finite norm estimate itself does not establish (18), and no assertion of (18) is made here.

## 6. Dependencies and present scope

The literal finite inputs are the homogeneous Casimir face source, the matched-sphere Morse coefficient identity, and the frozen cyclic-transfer proof. The only new factorization is (8), with its actual off-grade continuation (10) and marked boundary (12). The finite filling step is the separate uniform-filling-norm theorem. The actual augmented geometry and the all-CROSS nonzero long-filling theorem are unchanged.

The all-parity two-row telescope in the cyclic-transfer note is a boundary specialization of this signed problem. Its cancellation survives the original spectral normal, but it does not supply the missing general boundary block estimate. Thus the exact current obstruction is quantitative control of the correlated signed sum (17), not an additional filling-normal or Fourier-tail cost.
