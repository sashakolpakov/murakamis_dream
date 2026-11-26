# The opposite source kernel sews by its actual Krein adjoint

Written research proof, 23 November 2026.

The actual opposite-polarization kernel has an explicit adjoint after
the prefix Krein descent. One frozen Cartan factor converts it into a
single kernel whose reflected meridian value is its Krein adjoint.
The original pointed source is consequently an exact adjoint sewing
of that kernel with the actual reduced word. Every scalar, meridian
pole and root finite part is retained.

The form is indefinite. This is not a positive trace or a lower bound
for the marked scalar. No geometric window or complementary current
is removed by the adjoint identity.

## 1. Spaces, original operators and normalization

Fix the original root and head count
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad m\ge2,\quad r=m-1,\quad x=-M/q .
 \tag{1}
\]
The quantum parameter stays fixed. Initially \(M>0\), on the real
branch of \(\Log M\). Label the full physical space by \(V(M)\)
and its remaining \(r\)-head space by \(U(M)\), retaining the same
ordered occupation bases at every meridian. Their forms are
\[
 H_N|a\rangle=qQ^a|d-a\rangle,\qquad
 \mathscr H_b=H_N^{\otimes b},\qquad
 A^\sharp=\mathscr H_{\rm in}A^\dagger\mathscr H_{\rm out}.
 \tag{2}
\]
The last formula also defines the rectangular adjoint from the output
back to the input. Both forms are Hermitian involutions, independent
of \(M\). Use the prefix of [D], with its original zero endpoint:
\[
 S_M=e_Q(x^{-1}L_1F_{\rm r}(M)),\quad
 q_M=p_0S_M^{-1},\quad i_0v=|0\rangle\otimes v,
 \quad i_dv=|d\rangle\otimes v .
 \tag{3}
\]
Thus \(S_Mi_0=i_0\), \(q_Mi_0=I\), and [D] proves
\(S_M^\sharp=S_M^{-1}\). Write
\[
 K_\Sigma(M)=M^mK_{\Sigma,0},\qquad
 K_{\rm r}(M)=M^rK_0,\qquad K_0^N=\varepsilon I,
 \quad\varepsilon=(-1)^{(N+1)r}.
 \tag{4}
\]
These are the actual total Cartans; \(K_0\) is the frozen remaining
Cartan at completeness. In particular \(K_0^\sharp=K_0\).

We retain [O]'s scaled lowering operator, denoted here by \(E\):
\[
 E|a\rangle=(MQ^{-a}-M^{-1})|a-1\rangle\quad(a>0),
 \qquad E|0\rangle=0 .
 \tag{5}
\]
On ordered heads \(E_\Sigma=E_1K_{\rm r}+E_{\rm r}\).
This is \(q^{-1}\) times the head \(e_x\) convention used in
the physical real-meridian proof; its adjoint is therefore
\(E^\sharp=QE\), not \(E\). Directly, the two reflected
\(H_N\) factors contribute \(Q\), and
\(\overline{MQ^{-(d-a+1)}-M^{-1}}=MQ^{-a}-M^{-1}\).
The zero bottom arrow matches the top zero of the adjoint. Hence
\[
 E_\Sigma^\sharp=QE_\Sigma,\qquad
 (E_\Sigma^d)^\sharp=Q^{-1}E_\Sigma^d,
 \quad K_{\Sigma,0}E_\Sigma K_{\Sigma,0}^{-1}=QE_\Sigma.
 \tag{6}
\]

The entire balanced turnover and its tensor reversal are those of [O]:
\[
 C_M|a\rangle=c_a(M)|d-a\rangle,\quad
 c_a(M)=\prod_{j=1}^a\frac{MQ^j-M^{-1}}{1-Q^j},\quad
 \mathscr C_M=C_M^{\otimes m}\mathsf J .
 \tag{7}
\]
Here \(\mathsf J\) reverses the original head order. In particular
\(\mathscr C_M\) goes from the reflected full module to \(V(M)\).
The actual opposite kernel is
\[
 T_M=q_ME_\Sigma(M)^d\mathscr C_Mi_0:
                                      U(M^{-1})\longrightarrow U(M).
 \tag{8}
\]
Every symbol in this definition is a specified finite original matrix.

## 2. The turnover and rectangular adjoints

For positive real \(M\), each factor in (7) gives
\(\overline{c_a(M)}=c_a(M^{-1})\). On one head the coefficient
of \(C_M^\sharp\) on input \(a\) is
\(q^2Q^{2a}\overline{c_a(M)}\). Since the frozen one-head
Cartan is \(-q^{-1}Q^{-a}\), its inverse square has exactly
that factor. Tensor reversal commutes with the total Cartan,
so the complete identity is
\[
 \mathscr C_M^\sharp
                       =\mathscr C_{M^{-1}}K_{\Sigma,0}^{-2}.
 \tag{9}
\]
No scalar \(M\)-power remains in this frozen-Cartan expression.

From (2)--(3) the rectangular adjoints are exactly
\[
 i_0^\sharp=q^{-1}p_d,\qquad
 p_0^\sharp=qi_d,\qquad q_M^\sharp=qS_Mi_d .
 \tag{10}
\]
The first two follow from the entries \((H_N)_{0d}=q^{-1}\)
and \((H_N)_{d0}=q\); the last uses prefix isometry.

The finite top-row identities needed below are
\[
 p_dF_\Sigma(M)^d=Nq_M,\qquad
 S_Mi_d=F_\Sigma(M)^di_0/N,\qquad
 K_{\Sigma,0}^{-2}i_d=Q^{-1}i_dK_0^{-2}.
 \tag{11}
\]
Indeed \(F_\Sigma=S_MF_1S_M^{-1}\),
\(p_dS_M=p_d\), and
\(F_1^di_0=(Q;Q)_di_d=Ni_d\). These prove the first two
formulas, with both factors \(N\) retained. For the last,
the first-head top Cartan is \(-q\), whose inverse square is
\(Q^{-1}\). All statements include the finite top and bottom rows.

## 3. The exact adjoint of the opposite kernel

Use the shorthand \(\widehat M=M^{-1}\). Combining (6),(9),(10)
first gives
\[
 T_M^\sharp=Q^{-1}p_d\mathscr C_{\widehat M}
          K_{\Sigma,0}^{-2}E_\Sigma(M)^dS_Mi_d.
 \tag{12}
\]
The factors \(q^{-1}\) and \(q\) from the rectangular adjoints
have canceled; \(Q^{-1}\) is still present from \(E^d\).
Moving \(K_{\Sigma,0}^{-2}\) through \(E_\Sigma^d\) contributes
\(Q^{-2d}=Q^2\). It commutes with \(S_M\), and the last formula
of (11) then contributes \(Q^{-1}\). Thus all three remaining
phases cancel, leaving
\[
 T_M^\sharp=p_d\mathscr C_{\widehat M}
                         E_\Sigma(M)^dS_Mi_dK_0^{-2}.
 \tag{13}
\]
The actual turnover in [O, (7)] exchanges the two totals:
\(\mathscr C_{\widehat M}E_\Sigma(M)=
 F_\Sigma(\widehat M)\mathscr C_{\widehat M}\) and
\(\mathscr C_{\widehat M}F_\Sigma(M)=
 E_\Sigma(\widehat M)\mathscr C_{\widehat M}\).
Use these and the first two formulas of (11) in order:
\[
 \begin{split}
 T_M^\sharp
 &=Nq_{\widehat M}\mathscr C_{\widehat M}S_Mi_dK_0^{-2}\\
 &=q_{\widehat M}\mathscr C_{\widehat M}
                              F_\Sigma(M)^di_0K_0^{-2}\\
 &=q_{\widehat M}E_\Sigma(\widehat M)^d
                              \mathscr C_{\widehat M}i_0K_0^{-2}
  =T_{\widehat M}K_0^{-2}.
 \end{split}
 \tag{14}
\]
The factor \(N\) has canceled only against the specified \(1/N\)
in the top section. Equation (14) holds for all positive real
meridians and every original primitive level.

## 4. Source normalization gives one kernel and its adjoint

Retain exactly [O]'s notation for the scalar normalization:
\[
 \begin{gathered}
 \mathcal D_N(z)=\frac{z^N-z^{-N}}{z-z^{-1}},\quad
 \gamma_N(M)=(-1)^d\mathcal D_N(M)/N,\quad
 a_N(M)=(-1)^dN\gamma_N(M)^m,\quad
 \mathcal H_M=\mathcal D_N(MK_{\rm r}(M)),\quad
 J_M=\mathcal H_M^{-1}T_M .
 \end{gathered}
 \tag{15}
\]
The Laurent-polynomial continuation defines \(\mathcal D_N\)
at \(z=\pm1\). The actual finite identities of [O, (11),(13),(16),(19)]
are
\[
 \begin{gathered}
 K_0T_M=T_MK_0^{-1},\quad
 \mathcal H_MT_M=T_M\mathcal H_{\widehat M},\quad
 T_MT_{\widehat M}=a_N(M)\mathcal H_M,\quad
 J_MJ_{\widehat M}=a_N(M)\mathcal H_M^{-1}.
 \end{gathered}
 \tag{16}
\]
Here inverses are generic meromorphic matrices; the complete source
is continued before specializing a singular meridian.
For positive real \(M\), \(\mathcal H_M^\sharp=\mathcal H_M\),
since \(K_{\rm r}^\sharp=K_{\rm r}\) and \(\mathcal D_N\)
has real Laurent coefficients. Equations (14),(16) therefore give
\[
 J_M^\sharp=J_{\widehat M}K_0^{-2}.
 \tag{17}
\]
For example, in this calculation
\(T_{\widehat M}\mathcal H_M^{-1}
 =\mathcal H_{\widehat M}^{-1}T_{\widehat M}\);
the diagonal factor cannot simply be commuted through \(T\).

Define the typed kernel
\[
 A_M=J_MK_0^{-1}:U(\widehat M)\longrightarrow U(M).
 \tag{18}
\]
Its right Cartan acts on its reflected input. Since
\(K_0J_M=J_MK_0^{-1}\) and \(K_0^\sharp=K_0\), we obtain
\[
 \boxed{\qquad A_M^\sharp=A_{\widehat M},\qquad
 A_MA_M^\sharp=a_N(M)\mathcal H_M^{-1}.
 \qquad}
 \tag{19}
\]
These are adjoints between the two actual tail modules, whose
numerical forms are the same \(\mathscr H_r\).

For the original reduced word \(B_\beta(M)\), [O, (21)] is
\(\Phi_0(W_\beta(M))=\mathcal D_N(M)
 \operatorname{Tr}_{U(M)}(\mathcal H_M^{-1}B_\beta(M))\).
Consequently (19) and cyclicity give the source-exact sewing
\[
 \boxed{\quad
 \Phi_0(W_\beta(M))=\frac{\mathcal D_N(M)}{a_N(M)}
 \operatorname{Tr}_{U(\widehat M)}
                    (A_M^\sharp B_\beta(M)A_M).
 \quad}
 \tag{20}
\]
The outside trace is on the reflected tail. It is not an additional
factor \(N\), a reset cap, or an unidentified opposite word.
The density identity holds for any remaining matrix \(B\);
identifying it with \(\Phi_0(W)\) uses the actual intertwiner
and original source formula just stated.

For real positive \(M\), the scalar in (20) is exactly
\[
 \frac{\mathcal D_N(M)}{a_N(M)}
   =\sigma\left(\frac{N}{\mathcal D_N(M)}\right)^{m-1},
 \qquad\sigma=(-1)^{d(m+1)}.
 \tag{21}
\]
It is real; the sign is retained. An equivalent Hermitian congruence
for the original trace density is
\[
 \mathcal D_N(M)\mathcal H_M^{-1}\mathscr H_r
     =\frac{\mathcal D_N(M)}{a_N(M)}
                                  A_M\mathscr H_rA_M^\dagger.
 \tag{22}
\]
This is an indefinite congruence, not a positive Gram factorization.

## 5. Root finite parts and scope

For the meridian germ about completeness put \(M=e^u\).
The holomorphic reflected adjoint means
\(A^{\natural\sharp}(u)=
 \mathscr H_r\overline{A(\bar u)}^{\mathsf T}\mathscr H_r\),
not a pointwise conjugation of an unrelated complex meridian.
Polarization of (19) gives \(A^{\natural\sharp}(u)=A(-u)\).
Thus (20) continues meromorphically with the literal product
\(A(-u)B_\beta(e^u)A(u)\) and the even scalar (21).
All root finite parts are taken after this whole product.
The original source is analytic there; its individual kernel
factors need not be.

In particular [O] gives at most a simple pole. If
\(A(u)=\sum_{j\ge-1}A_ju^j\), then exactly
\[
 A_j^\sharp=(-1)^jA_j,\qquad A_{-1}^2=0.
 \tag{23}
\]
The second statement follows because the right side of (19) has
at most a simple pole, so the coefficient of \(u^{-2}\) in
\(A(u)A(-u)\) vanishes. Neither residue nor its normal terms
is discarded. The sandwiched MATRIX \(A(-u)B_\beta(e^u)A(u)\)
can still have coefficient \(-A_{-1}B_\beta(1)A_{-1}\) at
\(u^{-2}\). Its full trace is zero by cyclicity and (23);
it is not set to zero pointwise or inside relative windows.
The first-meridian-jet source remains the original
one reconstructed in [O] and [D]. Quantum-parameter normals
are different and are not differentiated in this proof.

The gain is a genuine adjoint sewing of the original source,
using a specified single kernel and its reflected meridian value.
No assertion is made that a partial coherent resolution commutes
with that kernel, that its relative-window defect vanishes, or
that the actual geometric cycle is selected. The two tails retain
all \(N^r\) physical coordinates and every root Jordan direction.
All exterior rows, pivots, framing and modified-dimension factors
retain their original positions and their own conjugate factors.
No positive norm, two-eigenline noncancellation, or marked scalar
lower bound follows from (20).

## Complete sources and coverage

Both complete direct texts were read at the matching pins:

| Source | SHA-256 |
|---|---|
| [D: Reduced prefix Krein descent](research_reduced_prefix_krein_descent.md), 310 lines | `5f0ab1e56d6a2877cec8d52e2f13efc355729caf48f3726b4cd8654a1c9b3abe` |
| [O: Original opposite-polarization source kernel](research_opposite_polarization_source_kernel.md), 639 lines | `d52c6dd8e62f575a262fc7af460e258f7cb0e40b5a9c037ac46dd8d151002d44` |

The complete [paired Bargmann/Krein proof](research_paired_bargmann_krein_sewing.md),
256 lines, SHA-256 `23f6029f059e6d63cb25dc0f9450052fc7aa541e9122afcef0a159416949da2f`,
was checked for coverage. Its exact coefficient-form pairing does not
identify the adjoint of the opposite source operator; that is proved
here. Only written mathematics and text/hash operations were used.
Earlier final files remain unchanged.
