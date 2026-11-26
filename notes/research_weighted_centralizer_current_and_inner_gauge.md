# The weighted centralizer current is not a matrix gauge derivation

Private written proof, 18 November 2026.

The actual weighted Ward current has the required classical
centralizer field. It is nevertheless not an inner derivation of
the finite tensor matrix algebra. A local matrix-algebra splitting
therefore does not turn this existing current into a change of
basis. This statement concerns the specified lift; it does not
rule out a different lift with additional terms.

The sole complete proof source is W, the actual weighted Ward lift,
pinned below. All finite calculations needed for this conclusion
are given here.

## 1. The current and its part vanishing on the identity

Use \(N\ge2\), \(q=e^{\pi i/N}\), \(Q=q^2\),
\(\rho=q-q^{-1}\), and \(h=2\pi i/N\).
On \(b\ge1\) actual heads retain W's ordered coproducts
\[
 \mathsf K=K_1K_{\rm t},\qquad
 \mathsf E=\mathcal E_1K_{\rm t}+\mathcal E_{\rm t},
 \qquad
 \mathsf F=F_1+K_1^{-1}F_{\rm t}.
 \tag{1}
\]
The subscript \({\rm t}\) denotes the remaining tensor heads.
For \(b=1\), set \(K_{\rm t}=1\) and
\(\mathcal E_{\rm t}=F_{\rm t}=0\).

In W's exact order the coefficients needed here are
\[
 A_E=K_1F_1\mathsf K^{-1},\qquad A_F=\mathcal E_1 .
 \tag{2}
\]
Keep its entire third coefficient \(A_K\); its explicit value
will not enter the test. Write
\[
 \mathcal D(B)=h^{-1}\sum_{\iota=E,F,K}[X_\iota,A_\iota B],
 \qquad (X_E,X_F,X_K)=(\mathsf E,\mathsf F,\mathsf K).
 \tag{3}
\]
Removing its multiplication term gives
\[
 \delta(B):=\mathcal D(B)-\mathcal D(1)B
        =h^{-1}\sum_\iota A_\iota[X_\iota,B].
 \tag{4}
\]
Thus \(\delta(1)=0\), as any derivation would require.
Its exact product defect, however, is
\[
 \delta(BC)-\delta(B)C-B\delta(C)
       =h^{-1}\sum_\iota[A_\iota,B][X_\iota,C].
 \tag{5}
\]
This follows by expanding the two commutators in (4).
The defect may not be dropped merely because the principal
commuting symbols have a vector-field interpretation.

## 2. A diagonal test at the original root head

Evaluate (4) on \(\mathsf K\). The weight relations give
\[
 [\mathsf E,\mathsf K]=(1-Q)\mathsf E\mathsf K,\qquad
 [\mathsf F,\mathsf K]=(1-Q^{-1})\mathsf F\mathsf K.
\]
Since \(\mathsf K^{-1}\mathsf E\mathsf K=Q^{-1}\mathsf E\),
substitution in (2)--(4) yields
\[
 \delta(\mathsf K)=\frac{1-Q^{-1}}h
       \bigl(\mathcal E_1\mathsf F\mathsf K
                         -K_1F_1\mathsf E\bigr).
 \tag{6}
\]
Expanding (1), commuting only different tensor heads, and
using \([\mathcal E_1,F_1]=\rho(K_1-K_1^{-1})\), gives
\[
 \delta(\mathsf K)=\frac{1-Q^{-1}}h
 \left[
    \rho(K_1^2-1)K_{\rm t}
    +\mathcal E_1F_{\rm t}K_{\rm t}
    -K_1F_1\mathcal E_{\rm t}
 \right].
 \tag{7}
\]
All these are identities of the actual finite matrices.
In particular their zero endpoint arrows remain unchanged.

In the original tensor weight basis the last two terms in
(7) have zero diagonal: they change the first-head index.
At complete color \(M=1\),
\[
 K_1w_a=-q^{-1}Q^{-a}w_a,
\]
so
\[
 \operatorname{diag}\delta(\mathsf K)
  =\frac{(1-Q^{-1})\rho}h (K_1^2-1)K_{\rm t}
  \ne0 .
 \tag{8}
\]
Indeed on the first-head index \(a=0\),
\(K_1^2=Q^{-1}\ne1\), while \(K_{\rm t}\) is invertible.
This proves (8) for every \(N\ge2\) and every width \(b\ge1\).
Here \(\operatorname{diag}\) means taking matrix diagonal
entries in this specified basis, not an invariant trace.

For any finite matrix \(H\), the diagonal of
\([H,\mathsf K]\) is zero in the same basis.
Consequently \(\delta\) cannot have the form
\[
                          \delta(B)=[H,B].
 \tag{9}
\]
It is not any derivation of the full matrix algebra either.
For completeness, every complex-linear derivation \(D\) of
\(\operatorname{Mat}_n(\mathbb C)\) is inner: in matrix units set
\(H=\sum_i D(E_{i1})E_{1i}\). Applying the product rule to
\(E_{kl}E_{i1}\), then multiplying by \(E_{1i}\) and summing,
gives \([H,E_{kl}]=D(E_{kl})\). The matrix units span the
algebra, proving the assertion.

## 3. Consequence for a framing descent

W proves that (3), with its full multiplication term and
marked cut/pivot boundary, quantizes the principal field
\(s\partial_r\) on the stated geometric chart. That sourced
identity remains valid. Equations (5)--(8) show precisely
why one cannot reinterpret it as an inner splitting change
of the finite matrix algebra.

A proposed replacement by such a change must supply a
different finite derivation and compare its entire current,
including the difference from (3), with the original source.
Subtracting \(\mathcal D(1)B\) alone does not suffice.
No relative framing period, contour coefficient or
volume-conjecture lower bound follows from this calculation.

## Complete proof source

* W: notes/research_actual_weighted_ward_centralizer_lift.md,
  SHA256 e689364ab8e756ef51f8da43a7ea86d84086afd6bf57ffbe0af1a4f508c2648a.

The entire unchanged source was read in the author sequence,
every used implication checked, and its matching pin renewed.
The exact test was independently derived from its finite
matrices. Only written mathematics and text/hash operations
were used. Frozen and public files are unchanged.
