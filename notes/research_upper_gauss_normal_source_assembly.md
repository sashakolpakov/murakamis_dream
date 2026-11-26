# The upper Gauss normal in the original paired source

Private written proof, 18 November 2026.

The upper Fourier sector is not separately trace-null merely because
one physical block of its first normal is radical. The original
opposite-polarization closure has a precise left-upper contribution.
For every invertible actual three-strand braid, its two extreme
integer-degree sectors give this contribution a nonzero meridian
residue. The complementary lower contribution cancels that residue.
This is a universal source-assembly test, not a computation for a
particular knot or a lower bound for its closed invariant.

Only complete directs C and J, pinned below, are used. The sector
calibration and all closing manipulations are proved inline.

## 1. The exact left-upper closing row

Fix \(N\ge3\), \(d=N-1\), \(q=e^{\pi i/N}\),
\(Q=q^2\), and keep \(q\) fixed while \(M=e^\mu\) varies.
Write \(f_n=(Q;Q)_n\). For \(m\ge2\), use J's actual
reduced word \(B_+(M)\), its reversed-word partner
\(B_-(M^{-1})\), and the same remaining-head occupation space.
Every crossing scalar and the prescribed zero-framing line stay
inside these matrices. Put
\[
 H(M)=D_N(MK_{\rm r}(M)),\qquad
 D_N(z)=\frac{z^N-z^{-N}}{z-z^{-1}}.
 \tag{1}
\]
The Laurent-polynomial continuation defines \(D_N\) at \(z=\pm1\).
C and J give the literal orders
\[
 \begin{split}
 T&=L\mathcal A R,\qquad
 L=\mathcal B_m(W_\tau^{-1}),\quad
 R=D_{\rm top}\mathscr C_{m-1}(M),\\
 J(M)&=H(M)^{-1}T(M),\qquad
 J(M^{-1})=a_N(M)T(M)^{-1},\\
 B_+T&=TB_-(M^{-1}),\\
 \Phi_0(W_\beta(M))
   &=\frac{D_N(M)}{a_N(M)}
       \operatorname{Tr}\bigl(J(M)B_-(M^{-1})J(M^{-1})\bigr).
 \end{split}\tag{2}
\]
Here \(\tau=R_1\cdots R_{m-1}\); C specifies the entire
\(D_{\rm top}\), including its original scalar. The matrices
\(L,R\) are holomorphic and invertible near completeness. The
scalar \(a_N\) is also a holomorphic unit there. Equalities with
inverses initially hold generically and then meromorphically.

Use C's whole-meridian decomposition
\[
 \begin{split}
 \mathcal A&=H_d(M)K_{\rm r}^d\mathcal S_N,\qquad
 H_d(M)=\prod_{j=1}^d(MQ^{-j}-M^{-1}),\\
 \mathcal A_{\rm up}
   &=H_dK_{\rm r}^d
       \sum_{l+k\ge N}C_{lk}(M)\mathcal D_{lk}(K_{\rm r},\Omega_{\rm r}),
 \qquad \mathcal A_{\rm lo}=\mathcal A-\mathcal A_{\rm up}.
 \end{split}\tag{3}
\]
Here \(g_n=(M^{-2}Q;Q)_n\), \(C_{lk}=g_{l+k}/(g_lg_k)\),
and \(\mathcal D_{lk}\) is C's symmetric cardinal coupon.
All indices in the sum lie between zero and \(d\).
In particular \(\mathcal A_{\rm up}(1)=0\) as an actual matrix.
Define \(T_{\rm up}=L\mathcal A_{\rm up}R\) and
\(J_{\rm up}=H^{-1}T_{\rm up}\), retaining the original right
kernel. Its contribution is by definition
\[
 \Phi_{{\rm up},L}(M)=\frac{D_N(M)}{a_N(M)}
       \operatorname{Tr}\bigl(J_{\rm up}(M)
                         B_-(M^{-1})J(M^{-1})\bigr).
 \tag{4}
\]
Then exactly
\[
 \boxed{\quad
 \Phi_{{\rm up},L}(M)=D_N(M)\operatorname{Tr}
     \left[H(M)^{-1}\mathcal A_{\rm up}(M)\mathcal A(M)^{-1}
                         B^\tau(M)\right],
 \quad B^\tau=L^{-1}B_+L.
 \quad}\tag{5}
\]
Indeed use the inverse in (2) and
\(B_-(M^{-1})T^{-1}=T^{-1}B_+\). The product
\(T_{\rm up}T^{-1}\) is
\(L\mathcal A_{\rm up}\mathcal A^{-1}L^{-1}\).
Every actual reduced braid preserves integer degree, so \(L\)
commutes with \(H\). Cyclicity gives (5). Thus neither the
reflected kernel, its central normalization, nor its scalar
derivative has been replaced by a free trace.

Formula (5) holds also after restricting the trace to any fixed
integer-degree sector, because all matrices in its right side
preserve that degree. The upper and lower versions add exactly
to the original source, also sector by sector.

J proves that \(T^{-1}=a_N^{-1}J(M^{-1})\) has at most a
simple pole. Thus \(\mathcal A^{-1}=RT^{-1}L\) has at most
a simple pole. Since \(\mathcal A_{\rm up}(1)=0\),
\[
              P_{\rm up}(M):=\mathcal A_{\rm up}\mathcal A^{-1}
 \tag{6}
\]
is holomorphic at completeness. The remaining \(H^{-1}\) in
(5) can still have a simple pole. Its residue and finite part
must be computed before declaring any separate sector removable.
For example, on a nonself Cartan sector write
\(H^{-1}=h_{-1}/\mu+h_0+\cdots\),
\(P_{\rm up}=P_0+\mu P_1+\cdots\), and
\(B^\tau=B_0+\mu B_1+\cdots\). Since
\(D_N(e^\mu)=N+O(\mu^2)\), the finite part of (5) there is
\[
 N\operatorname{Tr}\{h_0P_0B_0+
                   h_{-1}(P_1B_0+P_0B_1)\}.
 \tag{7}
\]
In general \(P_1\) includes the second coefficient of
\(\mathcal A_{\rm up}\), multiplied by the residue of
\(\mathcal A^{-1}\). A lone upper first-normal matrix is
therefore insufficient for this unassembled finite part.

## 2. A universal extreme-pair calibration at width three

Set \(m=3\), so there are two remaining heads. The integer
degrees zero and \(2d\) are one-dimensional. On each head,
\(K w_a=xQ^{-a}w_a\), with \(x=-M/q\). Consequently
\[
       K_{\rm bottom}=M^2Q^{-1},\qquad
       K_{\rm top}=M^2Q.
 \tag{8}
\]
The bottom is killed by total \(E\), and the top by total
\(F\), with the literal missing extreme arrows retained.
The two equivalent ordered expressions for the actual Casimir are
\[
 \Omega=FE+qK+q^{-1}K^{-1}
        =EF+q^{-1}K+qK^{-1}.
 \tag{9}
\]
They follow from \([E,F]=(q-q^{-1})(K-K^{-1})\).
Thus the respective scalar values are
\(qK+q^{-1}K^{-1}\) and \(q^{-1}K+qK^{-1}\).

C writes \(\Omega=z+z^{-1}\), \(a=qKz\), \(b=qK/z\),
\(c=M^{-2}Q\), \(u=a^{-1}\), \(v=b^{-1}\). On the bottom
choose \(z=M^2q^{-1}\). Then
\[
        a=M^4Q^{-1},\quad b=1,\quad v=1.
 \tag{10}
\]
Since \(L_k(1)=\mathbf1_{k=0}\), the upper sum is identically
zero there, throughout the meridian germ. The full Gauss polynomial
is one, so \(P_{{\rm up},{\rm bottom}}=0\) identically.

On the top choose \(z=M^2q\). This gives
\[
       a=M^4Q^2,\quad b=Q=Q^{-d},\quad
       u=M^{-4}Q^{-2},\quad v=Q^{-1}.
 \tag{11}
\]
The finite Chu identity in C yields the exact total scalar
\[
 \mathcal S_{{\rm top}}(M)
      =\frac{(M^{-6}Q^{-1};Q)_d}{(M^{-2}Q;Q)_d}.
 \tag{12}
\]
For \(N\ge3\), the numerator contains exactly one root zero,
the factor \(1-M^{-6}\). The other factors have product
\(N/(1-Q^{-2})\) at completeness, while the denominator is
\(f_d=N\). Hence
\[
 \mathcal S_{{\rm top}}(1)=0,\qquad
 \partial_\mu\mathcal S_{{\rm top}}|_0
                         =\frac6{1-Q^{-2}}.
 \tag{13}
\]
For the upper part, all its coefficients vanish at the root, so
moving-coupon derivatives contribute zero to its first normal.
At \(u=Q^{N-2},v=Q^{N-1}\), its derivative is just C's
specified grid coefficient
\[
 \partial_\mu\mathcal S_{{\rm up},{\rm top}}|_0
       =2N\frac{f_{N-3}}{f_{N-2}f_d}
       =\frac2{1-Q^{-2}}.
 \tag{14}
\]
The common factor \(H_dK^d\) cancels in the quotient (6).
Equations (12)--(14) therefore prove the removable values
\[
 \boxed{\quad
 P_{{\rm up},{\rm top}}(e^\mu)=\frac13+O(\mu),
       \qquad P_{{\rm up},{\rm bottom}}=0.
 \quad}\tag{15}
\]
This retains the actual moving top argument \(u=M^{-4}Q^{-2}\).
Replacing its true total normal by a fixed-grid derivative would
incorrectly change the ratio in (15).

## 3. A nonzero pole in the original integer-degree pair

Let \(b_{\rm top}(M)\) be the scalar by which the actual
invertible reduced braid acts on its all-top degree. It is a
holomorphic unit. Conjugation by \(L\) does not change a scalar
on this one-dimensional sector, so it is also the top value of
\(B^\tau\). Every original writhe/framing scalar remains in
\(b_{\rm top}\).

For \(m=3\), the top factor in (1) is \(H=D_N(M^3Q)\).
The actual scalar closing coefficient has expansion
\[
 \frac{D_N(e^\mu)}{D_N(e^{3\mu}Q)}
     =\frac{Q-Q^{-1}}{6\mu}
          +\frac{Q+Q^{-1}}2+O(\mu).
 \tag{16}
\]
The bottom sector contributes nothing to (5). Therefore its
exact integer-degree pair \((0,2d)\) satisfies
\[
 \boxed{\quad
 \operatorname*{Res}_{\mu=0}
    \Phi_{{\rm up},L}^{\{0,2d\}}(e^\mu)
       =\frac{Q-Q^{-1}}{18}\,b_{\rm top}(1)\ne0.
 \quad}\tag{17}
\]
The inequality holds at every \(N\ge3\) and for every
invertible actual three-strand braid. No arbitrary matrix mark
has been inserted to obtain it.

J proves the whole-meridian reciprocity of the two original
integer-sector traces. In particular
\(b_{\rm bottom}(1)=b_{\rm top}(1)\), and the two residues
of the *full* closing row cancel. Its pair value is removable.
By the exact linear decomposition after (5), the complementary
left-lower contribution has the opposite residue to (17).
Thus (17) is a compulsory complementary-source cancellation,
not a singularity of the original invariant.

It also does not assert that the sum of the upper residues over
all other degree pairs is nonzero. An integer-sector trace is
an exact term of the reduced finite closing formula; no analytic
original intertwiner projector or geometric window is inferred
from that bookkeeping. Nor is a lower bound for the closed source
deduced from the nonzero pole in one such term.

## 4. Paired frames do not delete one fixed contribution

There is elementary paired-frame covariance of (2). If \(S\)
is generically invertible and degree preserving, it commutes
with \(H\). Replacing the two outer factors by
\[
       H^{-1}ST,\qquad a_NT^{-1}S^{-1}
 \tag{18}
\]
leaves the whole trace unchanged, because it becomes
\(D_N\operatorname{Tr}(H^{-1}SB_+S^{-1})\).
This generic trace identity is not a new covariance theorem.
It explains why compensating changes of the right kernel can
cancel a variation of the left one, without making (4), whose
right kernel is fixed, zero. With relative resolution matrices
between the factors, their corresponding conjugations or
commutator defects must also remain; J gives their exact rows.

In particular the actual reduced braid is not asserted to commute
with the remaining-head Casimir. Degree preservation only gives
commutation with the total Cartan. A radical on a particular
Cartan block cannot be erased from (5) by an unproved stronger
commutation. The explicit whole-meridian obstruction (17) already
rules out this sectorwise shortcut without needing a norm estimate.
No assertion here supplies a nonzero geometric coefficient or
removes the remaining source-compatible contour problem.

## Complete proof directs

* C: notes/research_balanced_gauss_cyclic_divisor_source.md,
  SHA256 c15668d7dff95346d72801b721bf95970b661e5b17d125aaadd7e0dc38905b00.
* J: notes/research_opposite_polarization_source_kernel.md,
  SHA256 d52c6dd8e62f575a262fc7af460e258f7cb0e40b5a9c037ac46dd8d151002d44.

Both complete directs and the entire final were read nontruncated in
the active author sequence; every used implication and pin was checked.
Only written mathematics and text/hash operations were used. Frozen
and public files were not edited.
