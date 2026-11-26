# The original crossing in the coupled flag Euler exchange

Research note, 22 November 2026. This identifies the nilpotent factor of
the original complete crossing in the physical flag coordinates of [D].
The factor moves the multiplicity clock, and participates in both the
existing cyclic and marked full-dilogarithm exchanges. All identities
hold on the complete two-head space and preserve arbitrary exteriors.

Pascal/Gaussian factorizations of the original crossing already appear
in [C, Section 6.1]. The additional identification here is the explicit
operator \(X\) in the actual coupled flags, and its exchanges with the
same cyclic and full functions used in [A,P]. This does not match every
remaining nine-cell factor or give a geometric scalar lower bound.

## 1. The actual flags and the new nilpotent argument

Use the complete balanced heads and conventions of [D]:
\[
 N\geq2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1},\quad\lambda=x^{-1}=-q,\quad F_h=(Q;Q)_h .
 \tag{1}
\]
The auxiliary flag wraps are \(S_1^N=1\), \(S_2^N=(-1)^d\).
Keep the original positive checked crossing as \(\kappa W\), where
\(\kappa\) is its unchanged common Cartan/source scalar. Thus \(W\)
is exactly the stripped matrix of [A, (11)], with \(W|0,0\rangle=|0,0\rangle\).
Its full negative inverse is \(\kappa^{-1}W^{-1}\).
The actual cup and averaged marked row remain
\[
 p=N\sum_{a=0}^d x^{a-d}|a,d-a\rangle,\qquad
 \ell|a,b\rangle=x^b/N^2,\qquad \ell p=1.
 \tag{2}
\]

Retain the original flag operators
\[
 \Delta=Z_1(\lambda S_2-S_1),\quad
 \gamma=-e_2K_1,\quad v=Z_2^{-1}+S_1e_2,\quad
 M=Z_1Z_2v,\quad S=S_1v^{-1}.
 \tag{3}
\]
Here \(M\) is the multiplicity clock, not a peripheral meridian eigenvalue.
Here \(v^N=M^N=S^N=1\), \(\Delta^N=0\), \(\Delta v=Qv\Delta\),
and \(M\) commutes with \(\Delta,v\). The original \(S_1\) commutes
with \(v\), and \(\Delta S_1=QS_1\Delta\), so \([S,\Delta]=0\).
Define the physical nilpotent operator
\[
 X=(1-Q^{-1}M^{-1})\Delta S^{-1}.
 \tag{4}
\]

For clarity, these formulas have a completely explicit coordinate
meaning. In the rescaled frame \(\widetilde{\mathcal B}\) of [D, (27)],
\[
 \begin{gathered}
 v=Z_s,\quad M=Z_m,\quad S=S_m,\quad S_1=S_mv,\\
 X|m,s\rangle=(1-Q^{-m})(1-Q^{1-s})
                   |m-1,s-1\rangle .
 \end{gathered}
 \tag{5}
\]
Indices in (5) are cyclic, and the displayed zero coefficients are
retained. The identity for \(S_1\) follows by applying
\(S_1\Delta^a=Q^{-a}\Delta^aS_1\) to the columns
\(\Delta^a|m,0\rangle/F_a\). Formula (5) proves \(X^N=0\),
\([X,\Delta]=0\), and \(Xv=QvX\).
The physical space still has dimension \(N^2\).

Let \(E_j(v)\) denote the \(v=Q^j\) projectors, with \(E_N=E_0\), and set
\[
 \mathcal G=\sum_{j=1}^N g_jE_j(v),\qquad
 g_j=(-1)^{j-1}Q^{j(j-1)/2},\qquad g_N=1.
 \tag{6}
\]
It is unitary in the fixed positive Gram of [D], and commutes with
\(M,S_1,v\). Its consecutive ratios give
\[
 \mathcal G\Delta\mathcal G^{-1}=-Q\Delta v^{-1}.
 \tag{7}
\]
The sole exceptional marked transition has input \(v=Q\); its
\(\Delta\)-arrow is zero in the original physical module. No cyclic
arrow has been dropped to impose (7).

## 2. Exact crossing factorization on the full space

For a nilpotent argument \(Y^N=0\), write
\[
 P_N(Y)=\sum_{h=0}^d\frac{(-1)^hQ^{h(h-1)/2}}{F_h}Y^h,
 \qquad \mathcal E_N(Y)=\sum_{h=0}^dY^h/F_h=P_N(Y)^{-1}.
 \tag{8}
\]
The inverse follows from the finite \(Q\)-binomial theorem in every
degree below \(N\); higher degrees vanish. No \(F_N\) is divided out.
The original crossing has the factorization
\[
 \boxed{\qquad W=\mathcal G\mathcal E_N(X),\qquad
 W^{-1}=P_N(X)\mathcal G^{-1}.\qquad}
 \tag{9}
\]

Here is a full-space proof from the actual Hurwitz identities.
Directly from (5),
\[
 [X,S_1]=(1-Q^{-1})\Delta v,\qquad
 X(\Delta v)=Q(\Delta v)X .
 \tag{10}
\]
Thus
\[
 [X^h,S_1]=-Q^{-1}(1-Q^h)\Delta vX^{h-1},
 \qquad 1\leq h\leq d.
 \tag{11}
\]
Summing (11) with the coefficients of (8), the only truncated top
correction is \(\Delta vX^d/F_d=0\), because it contains \(\Delta^N\).
Therefore
\[
 \mathcal E_N(X)S_1\mathcal E_N(X)^{-1}
       =S_1-Q^{-1}\Delta v,\qquad
 [\mathcal E_N(X),\Delta]=0.
 \tag{12}
\]
For \(A_*=\mathcal G\mathcal E_N(X)\), equations (7),(12) give
\[
 A_*S_1A_*^{-1}=S_1+\Delta,\qquad
 A_*\Delta A_*^{-1}=-Q\Delta v^{-1}.
 \tag{13}
\]
These are precisely the original identities for \(W\):
the first is [A, (10)], and the second is obtained by subtracting
\(t_2\) from \(t_3\) in [A, (15)]. Both \(A_*\) and \(W\) fix
\(|0,0\rangle\): this is also the frame's \(|0,0\rangle\) column,
so \(X\) kills it, and its clock value is
\(v=1\), where \(g_N=1\).

Their identical first conjugation implies equality on every
\(S_1^m|0,0\rangle=|m,0\rangle\). Their identical second conjugation
then implies equality on every \(\Delta^a|m,0\rangle/F_a\).
These \(N^2\) vectors form the complete invertible frame of [D, (27)].
This proves (9), including every endpoint and both parities, without
an unspecified intertwiner scalar or a semisimple quotient.

The resulting clock updates are also explicit:
\[
 WvW^{-1}=v+X,\qquad
 WXW^{-1}=-QXv^{-1},\qquad
 WMW^{-1}=M+(Z_1Z_2)X .
 \tag{14}
\]
Indeed \(\mathcal E_N(X)v\mathcal E_N(X)^{-1}=v(1-X)\) by the finite
Euler recurrence, and \(\mathcal GX\mathcal G^{-1}=-QXv^{-1}\)
by (4),(7). The actual crossing preserves \(Z_1Z_2\).
In particular the new factor is not confined to the commutant of \(M\).

The completed flag shift also has a closed transport. Put
\(B_0=(1-Q^{-1}M^{-1})S^{-1}\), so \(X=B_0\Delta\).
It is a first-coordinate nilpotent, \(B_0^N=0\), and commutes with
\(\gamma\). Indeed \(M\) does, while the opposite phase factors in
\(S_1\gamma=Q\gamma S_1\) and \(v\gamma=Q\gamma v\) cancel in \(S\).
Consequently
\[
 [X,\gamma]=\lambda(1-Q^{-1})B_0v,\qquad
 \mathcal E_N(X)\gamma\mathcal E_N(X)^{-1}
       =\gamma-\lambda Q^{-1}B_0v .
 \tag{14a}
\]
The same sum as in (11),(12) proves this, with top term
\(B_0vX^d=0\) because it contains \(B_0^N\).
The Gaussian ratios give \(\mathcal G\gamma\mathcal G^{-1}=-\gamma v\);
the exceptional \(v=1\) arrow of \(\gamma\) is physically zero.
For the original completion of [D, (9)], write
\(c_*=[(-\lambda)^dF_d]^{-1}\). Then
\[
 \gamma':=W\gamma W^{-1}=-\gamma v-\lambda Q^{-1}B_0v,\qquad
 W\Gamma W^{-1}=\gamma'+c_*\Delta^d .
 \tag{14b}
\]
Its rank-\(N\) corner is unchanged: \(E_1(v)\Delta^d=\Delta^d\), and
\(( -Q\Delta v^{-1})^d=\Delta^dv=\Delta^d\).
The scalar is \((-1)^dQ^{d(d+1)/2}=1\), including even \(N\);
the last equality uses \(\Delta^d(v-1)=\lambda^{-1}\Delta^N\gamma=0\).
Thus all these updates retain the actual completion, not just
the nilpotent arrows.

In particular the retained commutator \(O_t\) of [D, (23)] transports
explicitly. Using the primed operators in (14),(14b), put
\[
 \mathcal U'=\sum_{m=0}^dE_m(M')(\Gamma')^m,\qquad
 WO_tW^{-1}=\mathfrak d_N(tv')(\mathcal U')^{-1}
                  \mathfrak d_N(tv')^{-1}\mathcal U'.
 \tag{14c}
\]
All root marks are transported with the same clock labels. The right
side has no unspecified \(W\)-conjugate. An actual observation uses
the inverse-dual row \(\eta W^{-1}\) and column \(WY\); no bound on
that row or on a common Gram for overlapping pairs is asserted.

## 3. The cyclic and marked full exchanges with the actual crossing

On the marked Fermat cover \(t\beta\ne0\), \(\beta^N=1-t^N\), let
\(\mathcal C_t=\mathfrak d_N(tv)\) be exactly the cyclic matrix of
[A, (22)] and [D, (14)]. Its functional equation and \(Xv=QvX\) give
\[
 \mathcal C_tX\mathcal C_t^{-1}
       =\beta^{-1}X(1-Q^{-1}tv).
 \tag{15}
\]
The two summands on the right \(Q\)-commute. Their finite Euler
factorization is the mixed identity of [A], now on this explicit
argument from the original crossing. Inverting it reverses the order.
Since \(\mathcal C_t\) commutes with \(\mathcal G\), (9) gives
\[
 \boxed{\quad
 \mathcal C_tW=
  \mathcal G\,\mathcal E_N(-\beta^{-1}Q^{-1}tXv)
              \mathcal E_N(\beta^{-1}X)\,\mathcal C_t .
 \quad}
 \tag{16}
\]
Every argument has nilpotent degree \(N\); apparent higher degrees
in the product vanish, rather than requiring a cyclic replacement.
The same \(\mathcal C_t\), with its full scalar and root marks,
occurs once on both sides. The full crossing is obtained by retaining
the original multiplier \(\kappa\).

There is also a nonsingular physical-root version. Use the marked
matrix \(F_v\) of [P, (10)--(12)], not a separate specialization of
the singular \(\beta^{-1}\) factors:
\[
 F_v=\phi_N\sum_{j=1}^N\frac{E_j(v)}{F_{j-1}},\qquad
 \phi_N=\sqrt N\exp\!\left\{i\pi\left[
        \frac14-\frac{N+N^{-1}}{12}\right]\right\}.
 \tag{17}
\]
The exact relation \(F_v\Delta F_v^{-1}=\Delta(1-Q^{-1}v)\),
and the commuting factors of (4), imply
\(F_vXF_v^{-1}=X(1-Q^{-1}v)\). Hence
\[
 \boxed{\qquad
 F_vW=\mathcal G\,\mathcal E_N(-Q^{-1}Xv)
                      \mathcal E_N(X)\,F_v .
 \qquad}
 \tag{18}
\]
This equality retains the marked \(j=N\) value of the full function.
It is not obtained by identifying its top and bottom logarithmic marks.

## 4. Original source and exterior scope

The source identities \(\Delta p=0\), \(vp=Qp\), and \(Mp=p\) imply
\(Xp=0\), \(\mathcal Gp=p\). Consequently the literal original pairings are
\[
 \ell\mathcal C_tWp=\mathfrak d_N(tQ),\qquad
 \ell F_vWp=\phi_N .
 \tag{19}
\]
For the full crossing they are multiplied by the unchanged \(\kappa\).
No scalar on either side of (16) or (18) has been reset to one.

More generally, (9),(16),(18) preserve every actual two-head exterior
row and input tensor, before any further sums or relative integrals.
The exterior remains attached; (19) does not replace it by a special
cap. Original turns, pivots, framing and peripheral factors remain
unchanged outside these operator equalities. All \(N\) coordinates of
each physical head are retained.

This gives an actual crossing factor, not merely a pure-\(\Delta\)
oscillator identity. It does not assert that distinct overlapping
crossings use one common flag frame or one positive Gram with tame
transition norms. Nor does it identify the remaining complete
nine-cell tensor with the right side of (16), or authorize cancelling
its exteriors. No global geometric period, sharp whole-source bound,
or nonvanishing of the original general closing is proved here.

## Complete proof sources and coverage

- [D] [The retained Pachner ratio in the original physical flag algebra](research_retained_pachner_ratio_physical_flags.md), 365 lines, SHA-256 650d25db94060e306464ae00ef92ceb1e51ba4bec53da2c15ee67a89113be21a.
- [A] [Actual shared quantum flags and their charged exchange](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_shared_quantum_flags_and_charged_exchange.md), 459 lines, SHA-256 dcab795cc141e2e1db726998cf7b1141dd03c681eaae9076387f90581f53a7d9.
- [P] [The full dilogarithm resolves the actual charged flag pentagon at the root](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_marked_full_phi_flag_pentagon.md), 328 lines, SHA-256 3052cef4a1d666253562c13ceaf6a9bc472baf7691f23d13e33bb3f8d6e9888f.

[C] [An explicit coherent Gram for an actual split source](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_pascal_coherent_gram.md),
494 lines, SHA-256 b6e6d697b4e21d30ca683f265b9c41170a0bee424d783169b2e0c70233dc889e,
is coverage only. It already proves an exact original crossing
Pascal/Gaussian alphabet. No novelty is claimed for that factorization
method; the proof above identifies its needed physical flag argument
and the actual cyclic/full exchange, with literal source normalization.
