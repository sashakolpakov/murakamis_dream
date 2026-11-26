# Closed-source degree averaging and section independence

Private written proof, 19 November 2026.

The assembled marked operator in the original pointed source can be
replaced by its total-integer-degree part without changing the source
or any true meridian normal. This averaging contracts operator and
trace norms, including the actual total-arrow commutator norms. After
averaging, every closed lower-section pairing is exactly independent
of the section parameter. The original total-E source correction
remains; degree preservation does not imply total-F invariance.

The sole complete directs are S, the full section theorem, and B,
the bounded quotient-source theorem. All averaging arguments below
are elementary calculations on their actual finite spaces.

## 1. Finite degree averaging and the actual currents

Fix \(m\ge2\), \(r=m-1\), \(N\ge2\), \(d=N-1\),
\(Q=e^{2\pi i/N}\), and \(M=e^\mu\) at this fixed quantum root.
Give the physical occupation basis of \(V=(\mathbb C^N)^{\otimes m}\)
the coefficient Euclidean metric. Write
\[
 J_i e_a=ae_a,\qquad J=\sum_{i=1}^mJ_i,\qquad
 V=\bigoplus_{j=0}^{md}V_j,\qquad P_j:V\longrightarrow V_j.
 \tag{1}
\]
These are integer degrees, not residues modulo \(N\). The projectors
and the unitary matrices \(U_\theta=e^{i\theta J}\) are independent
of the meridian. For any full matrix \(C\), define
\[
 \mathcal A(C)=\sum_jP_jCP_j
   =\frac1{2\pi}\int_0^{2\pi}U_\theta C U_\theta^{-1}\,d\theta.
 \tag{2}
\]
The equality follows by integrating each matrix entry. In particular
\([J,\mathcal A(C)]=0\), \(\mathcal A^2=\mathcal A\), and
\[
 \|\mathcal A(C)\|_\nu\le\|C\|_\nu,
 \qquad \operatorname{Tr}\mathcal A(C)=\operatorname{Tr}C,
 \qquad \nu=\mathrm{op}\text{ or }1.
 \tag{3}
\]
Here \(1\) denotes trace norm. Unitary invariance and the triangle
inequality prove both norm bounds. More generally put
\[
 \mathcal A_\ell(X)=\frac1{2\pi}\int_0^{2\pi}
 e^{-i\ell\theta}U_\theta XU_\theta^{-1}\,d\theta
   =\sum_{j-k=\ell}P_jXP_k.
 \tag{4}
\]
The same proof gives \(\|\mathcal A_\ell(X)\|_\nu\le\|X\|_\nu\).

The capped total arrows \(E=E_\Sigma(M)\), \(F=F_\Sigma(M)\)
have exact integer degrees \(-1,+1\), respectively. Therefore
\[
 [E,\mathcal A(C)]=\mathcal A_{-1}([E,C]),\qquad
 [F,\mathcal A(C)]=\mathcal A_{1}([F,C]).
 \tag{5}
\]
For example, a component of \(C\) of degree \(b\) contributes
degree \(b-1\) to its E-commutator, so only \(b=0\) survives
the first projection. Thus
\[
 \|[E,\mathcal A(C)]\|_\nu\le\|[E,C]\|_\nu,
 \qquad \|[F,\mathcal A(C)]\|_\nu\le\|[F,C]\|_\nu.
 \tag{6}
\]
If \(C(M)\) is analytic, so is \(\mathcal A(C(M))\). Averaging
commutes with every true \(\partial_\mu\) derivative. Differentiating
(5) proves (6) also for each derivative of the entire commutator,
including derivatives of the actual arrows. No unrecorded estimate
on a moving mark is needed.

## 2. Preservation of the original and quotient source rows

Use B's maps on \(U=(\mathbb C^N)^{\otimes r}\):
\[
 q_F=p_0S^{-1},\quad q_FF=0,\quad q_Fi_0=I,\quad
 q_Fj=I,\qquad j\text{ preserves integer degree}.
 \tag{7}
\]
Here \(i_0u=e_0\otimes u\), and \(q_F\) also preserves degree,
with the first occupation omitted on \(U\). Let
\[
 D_N(z)=\frac{z^N-z^{-N}}{z-z^{-1}},\quad
 H=D_N(MK_{\rm r}),\quad D=D_N(M)H^{-1},
 \qquad g=K_{\rm r}^{-d}.
 \tag{8}
\]
Here \(K_{\rm r}\) is B's tail Cartan. Let
\(\Pi_0=|e_0\rangle\langle e_0|\) on the first head, distinct
from the full-degree projectors in (1). All inverses use the original
meromorphic continuation. B's two quotient coupons and pointed coupon are
\[
 Q_{\rm h}=i_0Dq_F,\qquad Q_{\rm b}=jDq_F,\qquad
 Q_{\rm pt}=\Pi_0\otimes g,\qquad
 \Phi(C)=\operatorname{Tr}_V(Q_{\rm pt}C).
 \tag{9}
\]
Every coupon in (9) has degree zero. Indeed \(D\) is scalar on
each tail degree and all the rectangular maps in (7) preserve it.
For any degree-zero matrix \(Z\), entrywise trace gives
\(\operatorname{Tr}(Z\mathcal A(C))=\operatorname{Tr}(ZC)\).
Consequently, with \(\bar C=\mathcal A(C)\),
\[
 \boxed{\quad
 \Phi(\bar C)=\Phi(C),\qquad
 \operatorname{Tr}(Q_{\rm h}\bar C)=\operatorname{Tr}(Q_{\rm h}C),
 \qquad
 \operatorname{Tr}(Q_{\rm b}\bar C)=\operatorname{Tr}(Q_{\rm b}C).
 \quad} \tag{10}
\]
These are whole-meridian identities for arbitrary analytic marks,
not merely for total intertwiners. They retain every Laurent
coefficient of the quotient rows and every true derivative of the
analytic pointed row. A prescribed analytic outside scalar may be
included in \(C\); a meromorphic outside scalar retains its full
Laurent multiplication. No separate residue is discarded.

## 3. Exact closed section independence

S gives \(F^N=0\) and the actual section, for every complex \(a\),
\[
 E_N(aF)=\sum_{n=0}^{d}\frac{a^nF^n}{f_n},\qquad
 f_n=(Q;Q)_n,\qquad i_a=E_N(aF)i_0,\qquad q_Fi_a=I.
 \tag{11}
\]
For \(n>0\), the matrix \(q_F\bar C F^ni_0\) takes tail degree
\(k\) to \(k+n\). Its trace against any degree-preserving tail
weight is zero. Likewise \(Q_{\rm pt}\bar C F^n\) has positive
full degree. Therefore
\[
 \boxed{\quad
 \operatorname{Tr}_U(Dq_F\bar C i_a)
      =\operatorname{Tr}_U(Dq_F\bar C i_0),\qquad
 \Phi(\bar C E_N(aF))=\Phi(\bar C)=\Phi(C).
 \quad} \tag{12}
\]
No small-activity condition is used. These finite polynomial and
meromorphic identities preserve all true meridian normals.

The unclosed section current need not vanish. Explicitly, set
\[
 D_{ab}=\sum_{n=1}^{d}\frac{b^n-a^n}{f_n}F^{n-1}.
 \quad\text{Then}\quad
 q_F\bar C(i_b-i_a)=q_F[\bar C,F]D_{ab}i_0.
 \tag{13}
\]
This follows from \(i_b-i_a=FD_{ab}i_0\) and \(q_FF=0\).
Each term on the right has positive tail degree. Its closed
weighted trace is zero exactly, although neither the matrix
in (13) nor \([\bar C,F]\) is asserted to be zero.

B retains the original forced-source identity
\(Q_{\rm pt}-Q_{\rm h}=[\mathcal W_E,E]\). Rectangular trace,
(10), and (12) now give the useful combined source row
\[
 \boxed{\displaystyle
 \Phi(C)=\operatorname{Tr}_U
       \left(D_N(M)H^{-1}q_F\mathcal A(C)i_a\right)
       +\operatorname{Tr}_V\left(\mathcal W_E
                           [E,\mathcal A(C)]\right).
 } \tag{14}
\]
The second term equals \(\operatorname{Tr}(\mathcal W_E[E,C])\)
by subtracting the two preserved rows in (10). No smaller bound or
separate pole cancellation is inferred. Its residue and finite part
must still be combined with those of the first term.

## 4. Scope of the closed reduction

Average the assembled marked operator. In general
\(\mathcal A(C_1C_2)\ne\mathcal A(C_1)\mathcal A(C_2)\):
for unit vectors of degrees zero and one, take
\(C_1=|0\rangle\langle1|\), \(C_2=|1\rangle\langle0|\).
The right side is zero and the left side is \(|0\rangle\langle0|\).
Thus independently averaging several window factors is not licensed.

Equation (14) removes the lower-section parameter from the closed
marked source. It needs neither a concentrated first-head profile
nor an estimate of the unclosed section kernel. It does not remove
the original E-current, or the distinct opposite-polarization return.
Averaging can spread a window along its whole phase orbit. The
finite scalar identities do not construct a selected geometric
Morse window, a contributing relative cycle, or a source lower bound.

## Complete proof-source pins

* S: notes/research_full_section_coalescent_kernel.md, 576 lines,
  SHA256 c26240d060f4474d3d59baae0c44c58dff60dcd550cf184defaadec5760509c7.
* B: notes/research_bounded_quotient_source_and_ward_homotopy.md, 456 lines,
  SHA256 a105d3b6aa2848ba14f978566d8f7bfeff3741910eef3ffe056fb02e972a5da7.

Both complete directs were freshly whole-read nontruncated in this
active sequence and retained unchanged. The entire matching final was
read back, every used implication checked, and all pins renewed before
freezing. Only written proofs and text operations were used; frozen
and public files were not edited.
