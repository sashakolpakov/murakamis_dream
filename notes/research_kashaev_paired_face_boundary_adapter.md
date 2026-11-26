# Kashaev's paired-face boundary adapter and its cyclic carry

Let \(N\ge2\), \(d=N-1\), and let \(Q\) be a primitive \(N\)-th root
of unity. The function in Kashaev's equation (4.28) defines an explicit
map from one crossing index to a pair of boundary-face indices. This
note proves its quotient, inverse, norm and cyclic-carry properties
directly from that function. Its finite algebra works at every level.
The tetrahedral state in the cited paper is restricted to odd levels;
no even-level extension of that state is asserted here.

## 1. The specified finite function

Choose nonzero complex numbers \(A,B\) and roots

\[
 a^N=A,\qquad b^N=B,\qquad r=a/b.
\]

Residues \([k]\) always lie in \(\{0,\ldots,d\}\). Define

\[
 f(k)=a^{[k-1]}b^{[-k]},\qquad
 \Psi_{kj}=Q^{jk}f(k),\qquad 0\le j,k<N.                 \tag{1}
\]

In the published notation, \(a=s_{0m}\), \(b=s_{m5}\), and

\[
 A=s(u_0)-s(u_m),\qquad B=s(u_m)-s(u_5).
\]

Thus (1) is exactly the function \(\psi^k_{m,j}\) of (4.28), with
its modular powers retained. In particular

\[
 f(0)=a^d,\qquad
 f(k)=a^{k-1}b^{N-k}=\frac{B}{a}r^k\quad(1\le k<N).     \tag{2}
\]

The value at zero is not obtained by extending the second expression
without its cyclic carry.

Let \(F_{kj}=N^{-1/2}Q^{jk}\). Orthogonality of the finite geometric
sum gives \(F^*F=I\). With \(D_f=\operatorname{diag}(f(k))\),

\[
 \Psi=\sqrt N D_fF,\qquad
 (\Psi^{-1})_{jk}=\frac{Q^{-jk}}{Nf(k)}.                \tag{3}
\]

These are invertible matrices for every stated \(N,A,B\), with no
primality assumption. The star on \(F\) concerns the fixed root of
unity only; no complex conjugation of \(A,B\) enters the inverse.

## 2. The paired-face quotient and its exact projector

Fix a charge \(c\in\mathbb Z/N\mathbb Z\). On a face pair write
\(\alpha_-,\alpha_+\in\mathbb Z/N\mathbb Z\), and put

\[
 k=\alpha_- -\alpha_+ +c.
\]

Define \(J_c:\mathbb C^N\longrightarrow\mathbb C^{N^2}\) by

\[
 (J_cv)(\alpha_-,\alpha_+)=v(\alpha_- -\alpha_+ +c).
                                                               \tag{4}
\]

Its image \(\mathcal H_c\) consists precisely of the arrays invariant
under simultaneous translation of both face indices. This invariant
subspace is independent of \(c\); the charge specifies its coordinate.
Each value of \(k\) has exactly \(N\) preimages. Consequently

\[
 J_c^*J_c=NI,\qquad
 P_{\rm diag}=\frac1N J_cJ_c^*
             =\frac1N\sum_{t\in\mathbb Z/N\mathbb Z}T_t,          \tag{5}
\]

where \((T_tw)(\alpha_-,\alpha_+)=w(\alpha_-+t,\alpha_++t)\).
This proves both that the quotient has dimension \(N\) and that
\(\iota_c=J_c/\sqrt N\) is an isometry onto its invariant realization.
Explicitly, the quotient is
\(\mathbb C^{N^2}/\operatorname{span}\{(T_t-I)w\}\);
the averaging projector in (5) identifies it with \(\mathcal H_c\).

The literal boundary adapter and a specified left inverse are

\[
 \mathcal A_c=J_c\Psi,\qquad
 \mathcal L_c=\Psi^{-1}\frac{J_c^*}{N}.
\]

They satisfy

\[
 \mathcal L_c\mathcal A_c=I,\qquad
 \mathcal A_c\mathcal L_c=P_{\rm diag},\qquad
 \mathcal A_c=N\iota_cD_fF.                            \tag{6}
\]

Thus the adapter is a rank-\(N\) map into the full face-pair space,
and an isomorphism onto its diagonal-translation quotient. It is not
an isomorphism onto all \(N^2\) boundary coordinates. Charge shifts
permute the \(k\) coordinate and do not alter any singular value.

## 3. Exact singular values and uniform decoration bounds

The singular values of \(\Psi\) are \(\sqrt N|f(k)|\); the nonzero
singular values of \(\mathcal A_c\) are \(N|f(k)|\). Formula (2) gives

\[
 |f(0)|=|A|^{d/N},\qquad
 |f(k)|=|A|^{(k-1)/N}|B|^{(N-k)/N}\quad(k\ge1).
\]

All exponents are nonnegative and sum to \(d/N\). Both extreme
values occur, at \(k=0\) and \(k=1\). Hence

\[
 \min_k|f(k)|=\min\{|A|,|B|\}^{d/N},\qquad
 \max_k|f(k)|=\max\{|A|,|B|\}^{d/N},
\]
\[
 \kappa_2(\Psi)=\kappa_2(\mathcal A_c)
 =\left(\frac{\max\{|A|,|B|\}}{\min\{|A|,|B|\}}\right)^{d/N}.
                                                               \tag{7}
\]

In (7), the rectangular condition number uses its nonzero singular
values. On a fixed compact set of nonzero \(A,B\), the normalized
adapter \(\mathcal A_c/N=\iota_cD_fF\) and its inverse on the image
have bounds independent of \(N\). No factorial diagonal gauge is
being substituted for (1).

These bounds retain every fixed-order decoration derivative. Work
on a simply connected parameter neighborhood with holomorphic choices
of \(\log A,\log B\); each root differs from their exponential roots
by a constant root of unity. In (2), \(f(k)\) is then a constant phase
times \(A^{u_k}B^{v_k}\), where \(u_k,v_k\in[0,1]\). For the inverse
the two exponents lie in \([-1,0]\). Differentiation multiplies these
powers by falling factorials of bounded real exponents and by fixed
negative powers of \(A,B\). On every compact subset \(K\) of this
neighborhood, for each fixed multi-index \(\nu\),

\[
 \sup_K\|\partial^\nu D_f\|+
 \sup_K\|\partial^\nu D_f^{-1}\|\le C_{K,\nu},          \tag{8}
\]

uniformly in \(N\) and in the constant root choices. Equations (3),(6)
give the corresponding normalized operator bounds. Composition with
the linear differences of vertex decorations gives the same result
for those parameters. This does not differentiate the root \(Q\)
off the root-of-unity locus or identify decoration derivatives with
the original meridian or quantum-normal directions.

## 4. The cyclic seam and its complete monodromy

Let \((Sv)(k)=v(k+1)\), with cyclic indices. Direct substitution in
(2), including \(k=N-1\), gives

\[
 Sf-rf=\frac{B-A}{b}\,\delta_0,
 \qquad
 \frac{f(k+1)}{f(k)}
 =r\left[1+\left(\frac BA-1\right)\delta_{k0}\right].  \tag{9}
\]

Equivalently, with \(E_0\) the zero-coordinate projector,

\[
 D_f^{-1}SD_f=r[I+(B/A-1)E_0]S.                       \tag{10}
\]

This is a rank-one correction to the geometric progression, not
an assertion that its norm is one. Its norm contribution is
\(|r|\,|B/A-1|\), uniformly bounded on the compacts used in (8).
The multiplier accumulated around the complete cyclic index is

\[
 r^N\frac BA=\frac AB\frac BA=1.                      \tag{11}
\]

Thus (10) has \(N\)-th power \(I\), as also follows by conjugating
\(S^N=I\). With face charge \(c\), the seam is the actual locus
\(\alpha_- -\alpha_+=-c\). Replacing (9) by a seam-free progression
would change the monodromy unless \(A=B\).

## 5. Four legs and the full boundary normalization

Take four nonzero pairs \(A_m=a_m^N,B_m=b_m^N\), charges \(c_m\),
and a nonzero root \(s_{05}\). For an arbitrary four-index array
\(R=(R_{j_1j_2j_3j_4})\), define its boundary array by the literal
right-hand expression of the published (4.25):

\[
 \mathcal B_R(\boldsymbol\alpha_-,\boldsymbol\alpha_+)
 =s_{05}^{d}\sum_{j_1,\ldots,j_4}R_{j_1j_2j_3j_4}
       \prod_{m=1}^4\Psi^{(m)}_{\alpha_{m,-}-\alpha_{m,+}+c_m,j_m}.
                                                               \tag{12}
\]

No property of \(R\) is needed for the following exact identities:

\[
 \mathcal B_R=s_{05}^{d}N^4
       \left(\bigotimes_{m=1}^4\iota_{c_m}D_{f_m}F\right)R,
\]
\[
 R=\frac1{s_{05}^{d}N^4}
       \left(\bigotimes_{m=1}^4F^*D_{f_m}^{-1}\iota_{c_m}^*\right)
        \mathcal B_R.                                       \tag{13}
\]

In particular the \(N^4\) factor is the four-leg paired-face
normalization; it is not removed by using normalized Fourier matrices.
The image projector is \(\bigotimes_mP_{\rm diag}\), and the map has
rank \(N^4\). Its norm bounds are precisely

\[
 |s_{05}|^dN^4\prod_m\min_k|f_m(k)|\,\|R\|_2
 \le\|\mathcal B_R\|_2
 \le |s_{05}|^dN^4\prod_m\max_k|f_m(k)|\,\|R\|_2.       \tag{14}
\]

For published vertex decorations, \(A_m+B_m=s_{05}^N\) for every
leg. When these differences range over fixed nonzero compacts,
\(|s_{05}|^d=|s_{05}^N|^{d/N}\) and its fixed-order derivatives are
uniformly bounded, as are its inverse and the normalized maps (13).
The four-leg exponential scale is therefore unchanged under these
specific fixed-decoration bounds.

Original tensor contractions use their specified dual rows. If a
column is sent to \(\mathcal A_cv\), its row \(\ell\) is transported
to \(\ell\mathcal L_c\); then
\(\ell\mathcal L_c\mathcal A_cv=\ell v\) exactly. The inverse uses
\(f(k)^{-1}\), not \(\overline{f(k)}\). Replacing the transported row
by a Hermitian adjoint changes the contraction in general. Positive
singular-value estimates do not authorize that replacement.
For an arbitrary row on the full face-pair space, only its restriction
through \(P_{\rm diag}\) contributes on the adapter image.

## 6. Opposite-face sewing retains the original wire clock

Use the same roots \(a,b\) on two paired-face adapters. Reverse the
face order in the second adapter and impose the charge condition
\(c+c'=1\) modulo \(N\). Their arguments are then

\[
 k=\alpha_- -\alpha_+ +c,\qquad
 k'=\alpha_+ -\alpha_- +c'=[1-k].
\]

The exact complement identity is

\[
                 f(k)f([1-k])=(ab)^d.                \tag{15}
\]

At \(k=0,1\), this is \(a^db^d=(ab)^d\). For \(2\le k<N\),
the second residue is \(N+1-k\); the two exponents of \(a\)
sum to \((k-1)+(N-k)=d\), and those of \(b\) sum to
\((N-k)+(k-1)=d\). Thus (15) also includes both cyclic endpoints
and \(N=2\).

There are \(N\) face pairs with each argument \(k\). Bilinear
contraction therefore gives, with \(Z_{jj'}=Q^j\delta_{jj'}\),

\[
 \begin{split}
 &\sum_{\alpha_-,\alpha_+}
   \mathcal A_c(\alpha_-,\alpha_+;j)
   \mathcal A_{c'}(\alpha_+,\alpha_-;j')\\
 &\quad=N(ab)^d
       \sum_{k=0}^{N-1}Q^{jk+j'(1-k)}
       =N^2(ab)^dQ^j\delta_{jj'}.
 \end{split}                                                   \tag{16}
\]

If the specified non-link edge factors are \(a^{-d}b^{-d}\),
they cancel the decoration factor in (16), leaving \(N^2Z\).
The factor \(Q^j\) is the wire factor appearing in the original
planar source (3.6). It is not an identity pairing or a Hermitian
square. The statement here requires exactly the roots, reversed
face order and complementary charges just specified; it does not
prove that a proposed global triangulation has those data.

Even changing only the root branches retains an explicit wire
operator. If the second adapter instead uses
\(a'=Q^u a,\ b'=Q^v b\), then
\[
 f'(l)=Q^{(u-v)l-u}f(l).
\]
Repeating the same finite sum yields
\[
 \sum_{\alpha_-,\alpha_+}
   \mathcal A_c^{a,b}(\alpha_-,\alpha_+;j)
   \mathcal A_{c'}^{a',b'}(\alpha_+,\alpha_-;j')
 =N^2(ab)^dQ^{j-u}\delta_{j',\,j-u+v}.                \tag{17}
\]
Thus branch changes give a recorded phase and index translation;
they cannot silently be replaced by the common-root formula.

## 7. The literal fixed cut and its one-face marginal

The planar definition in the primary paper fixes both open-edge
indices to zero in (3.2). Its rank-one cut operator in that index
basis is \(E_{00}\). Transport this particular operator, with the
inverse row from (6), to the paired-face space:

\[
                 \mathcal E_c=\mathcal A_cE_{00}\mathcal L_c.
\]

For row index \((\alpha_-,\alpha_+)\), column index
\((\alpha'_-,\alpha'_+)\), and their respective differences \(k,k'\),
(3),(6) give

\[
 (\mathcal E_c)_{\alpha_-\alpha_+;\,\alpha'_-\alpha'_+}
                  =\frac{f(k)}{N^2 f(k')}.           \tag{18}
\]

Thus \(\mathcal E_c^2=\mathcal E_c\), its rank and trace are one,
and \(P_{\rm diag}\mathcal E_c=\mathcal E_cP_{\rm diag}=\mathcal E_c\).
These identities follow either from (6) or directly from (18).
They retain the fixed-index cut; no change of the original planar
index basis is made in identifying \(E_{00}\).

Trace out the second face and call the resulting \(N\)-dimensional
matrix \(M\). Put
\[
 t=A/B=r^N,\qquad h=[\alpha'-\alpha].
\]
Then
\[
 M_{\alpha\alpha'}
 =\frac1{N^2}\sum_{k=0}^{N-1}\frac{f(k)}{f([k+h])}
 =\frac{r^{-h}}{N^2}\bigl[(N-h)+ht\bigr].            \tag{19}
\]
For \(h=0\), every summand is one. For \(1\le h<N\),
the ratio is \(r^{-h}\) at \(N-h\) indices and \(tr^{-h}\) at
the remaining \(h\). More explicitly, \(k=0\) and
\(N-h<k<N\) give the latter value; \(1\le k\le N-h\)
give the former, including the denominator endpoint \(k+h=N\).
This proves (19) without dropping either seam endpoint. The charge
has disappeared because \(k\) ranges over every residue.
Tracing out the first face gives \(M^{\mathsf T}\), so the two
marginals have the same spectrum.

The Fourier vector with entries \(N^{-1/2}Q^{j\alpha}\) has
eigenvalue
\[
 \lambda_j=\frac1{N^2}\sum_{h=0}^{N-1}
                  [(N-h)+ht]z_j^h,\qquad z_j=r^{-1}Q^j.        \tag{20}
\]
If \(t\ne1\), then \(z_j^N=t^{-1}\) and \(z_j\ne1\).
Using the finite geometric sum and its derivative in (20) gives
\[
                \lambda_j=
       \frac{(t-1)^2z_j}{N^2t(1-z_j)^2}.             \tag{21}
\]
For example, the numerator before substitution is
\[
 N(1-z_j^N)(1-z_j)
 +(t-1)\bigl[z_j-Nz_j^N+(N-1)z_j^{N+1}\bigr],
\]
which becomes \((t-1)^2z_j/t\). All eigenvalues are nonzero
when \(t\ne1\), even though the two-face cut itself has rank one.
Their sum is \(\operatorname{Tr}M=1\). If \(t=1\), (19) instead
gives \(M_{\alpha\alpha'}=r^{-[\alpha'-\alpha]}/N\);
this is the rank-one Fourier projector onto the unique character
with \(Q^j=r\).

There is a positive case of the actual fixed cut. Suppose
\(|A|=|B|\), so \(|r|=1\). Then all \(|f(k)|\) are equal,
and (18) is an orthogonal rank-one projector. Its marginal
is consequently positive semidefinite. If also
\(t=e^{i\theta}\ne1\), write \(z_j=e^{i\varphi_j}\); (21) gives
\[
 \lambda_j=\frac{\sin^2(\theta/2)}
                   {N^2\sin^2(\varphi_j/2)},\qquad
 \frac{\sin^2(\theta/2)}{N^2}\le\lambda_j\le1.         \tag{22}
\]
The denominator is nonzero because \(z_j^N=t^{-1}\ne1\).
The lower bound uses \(\sin^2(\varphi_j/2)\le1\), and the upper
bound follows from positivity and trace one. Hence for every
positive semidefinite one-face operator \(H\),
\[
 \frac{\sin^2(\theta/2)}{N^2}\operatorname{Tr}H
 \ \le\ \operatorname{Tr}(MH)\ \le\ \operatorname{Tr}H.          \tag{23}
\]
The same holds on the other face. The constant is uniform in
\(N\) when \(t\) stays on a fixed compact subset of the unit
circle excluding \(1\); no such positive lower bound is asserted
at \(t=1\).

Equation (23) concerns a positive operator on one face against
this explicitly transported fixed cut. It is not a lower bound
for arbitrary signed crossings, two-face operators, or the
remaining contracted knot network. It also does not identify a
different uniform-vector mark in another matrix basis with
the planar \(E_{00}\) used here.

## 8. Tetrahedral and source scope

Equations (1)--(23) prove a concrete boundary-module adapter and
transport its literal fixed-index cut. They
do not prove that the nine-tetrahedron state sum equals (12). The
published identity (4.25) makes that additional assertion for its
specified crossing tensor at odd \(N\). Its four paired boundary
faces, tangle edges, vertex measures, charge sums and root phases
must all be retained in any use of that assertion. In particular,
(13) alone does not supply an adapter from an independently assigned
five-cell or pointed tetrahedral state.

The sewing statement (16) supplies the original local wire phase
under its stated charge and edge-factor conditions. No identification
with the original marked meridian, a free-vertex
deletion, a globally charged triangulation, or a selected geometric
period is inferred. The explicit seam in (9), the inverse dual row,
and the factor \(s_{05}^dN^4\) are part of the boundary data for that
comparison, rather than discarded normalizations.

## Direct definition

R. M. Kashaev, *A Link Invariant from Quantum Dilogarithm*,
[q-alg/9504020v1](https://arxiv.org/pdf/q-alg/9504020),
especially (4.25)--(4.28), with the odd-level convention (4.1),
the fixed-index cut (3.2), the wire phase (3.6), and the non-link
edge factor (4.19)--(4.20).
The sole imported mathematical datum is the displayed function
(4.28); the boundary expression (12) is defined for arbitrary \(R\).
The complete paper also specifies the original three-dimensional
state and its restrictions, which are not substituted for a proof
of the broader source comparisons excluded above.

Local archived PDF:
`research_archive/finite-source-identification-2026-11-01/md-kashaev-normalization-critical-audit/kashaev1995.pdf`.
SHA256:
`0baef40fa9934c9119af2c67252f8032e288c884da72eeaecf405bf91569cda9`.
The archived and linked PDF bytes agree.
