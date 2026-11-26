# The retained Pachner ratio in the original physical flag algebra

Research note, 22 November 2026. The residual cyclic factorial in the
first source-preserving nine-cell beta move has an explicit realization
on the original two quantum-group heads. It is a commutator of the
existing cyclic dilogarithm with a completed physical flag shift. The
completion retains its missing corner, and the change of coordinates
retains the full original exterior covector.

The oscillator preparation used below is already proved in [P]. The new
identification is with the two particular boundary clocks of [R, (31)].
It does not identify the other factors of that source with the
nilpotent factors of the mixed pentagon.

## 1. The original heads and their prepared flags

Fix \(N\geq2\), \(d=N-1\), and
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad x=-q^{-1},\quad
 \lambda=x^{-1}=-q,\quad k=x^N=(-1)^d,\qquad
 F_a=(Q;Q)_a.
 \tag{1}
\]
In particular \(F_0=1\) and \(F_d=N\). Every index of a physical
head lies in \(0,\ldots,d\); brackets denote reduction to this set.
Write \(Z|a\rangle=Q^a|a\rangle\). Choose the auxiliary flag wraps
\[
 S_1|d\rangle=|0\rangle,\qquad
 S_2|d\rangle=k|0\rangle,
 \tag{2}
\]
with the ordinary raising arrows otherwise. Thus \(S_1^N=1\) and
\(S_2^N=k\), including even \(N\). These auxiliary completions do not
change the original nilpotent matrices. In the original balanced basis,
\[
 K|a\rangle=xQ^{-a}|a\rangle,\qquad
 e|a\rangle=\lambda(1-Q^{-a})|a-1\rangle\quad(a>0),
 \qquad e|0\rangle=0.
 \tag{3}
\]
The complete physical flags of [A] are
\[
 \Delta=Z_1(\lambda S_2-S_1),\qquad
 \gamma=-e_2K_1,\qquad v=Z_2^{-1}+S_1e_2.
 \tag{4}
\]
Their exact finite identities are
\[
 \begin{gathered}
 \Delta^N=\gamma^N=0,\quad v^N=1,\quad
 \Delta v=Qv\Delta,\quad v\gamma=Q\gamma v,\\
 \Delta\gamma=\lambda(v-1),\qquad
 \gamma\Delta=\lambda(Q^{-1}v-1).
 \end{gathered}
 \tag{5}
\]
They retain the endpoint rows of the original crossing. In particular,
the sign in (2) is required to obtain \(\Delta^N=0\).

Let \(J_+|a\rangle=|a+1\rangle\) for \(a<d\), with \(J_+|d\rangle=0\),
and put
\[
 P(A)=\sum_{h=0}^d\frac{(-1)^hQ^{h(h-1)/2}}{F_h}A^h,
 \qquad C=P(-S_1e_2Z_2).
 \tag{6}
\]
The argument is nilpotent, so \(C\) is invertible. The preparation
identities of [P, (8)] are
\[
 C^{-1}vC=Z_2^{-1},\qquad
 C^{-1}\Delta C=K_1^{-1}J_{+,2},\qquad [C,\gamma]=0.
 \tag{7}
\]
These are identities of the complete \(N^2\)-dimensional physical
space, rather than a quotient retaining only eigenvalues.

The original cup and averaged marked cap are
\[
 p=N\sum_{a=0}^d x^{a-d}|a,d-a\rangle,\qquad
 \ell|a,b\rangle=x^b/N^2,\qquad \ell p=1.
 \tag{8}
\]
As proved in [P], \(\Delta p=0\), \(vp=Qp\), and
\(p=N\lambda^d C|0,d\rangle\).

## 2. A cyclic completion with its actual corner

Define
\[
 \Pi=E_1(v)=\frac1N\sum_{r=0}^dQ^{-r}v^r,\qquad
 c_*=[(-\lambda)^dF_d]^{-1},\qquad
 \Gamma=\gamma+c_*\Pi\Delta^d.
 \tag{9}
\]
Here \(\operatorname{im}\Pi=\ker\Delta\) has dimension \(N\), by (7).
For \(h\in\ker\Delta\), (5) gives
\[
 \Delta\gamma^j h=-\lambda(1-Q^j)\gamma^{j-1}h,
 \qquad v\gamma^jh=Q^{j+1}\gamma^jh.
 \tag{10}
\]
The first formula is used for \(1\leq j\leq d\), and the second also
holds for \(j=0\). Thus the maps \(h\mapsto\gamma^jh\),
\(0\leq j\leq d\), are injective with distinct clock eigenvalues.
Their images exhaust the physical
space. The explicit coefficient-extraction maps are
\[
 L_j=[(-\lambda)^jF_j]^{-1}\Pi\Delta^j,
 \qquad L_j\gamma^rh=\delta_{jr}h.
 \tag{11}
\]
For \(j<r\), the projector kills the remaining nontrivial clock
eigenvalue; for \(j>r\), a remaining \(\Delta\) kills \(h\).
At \(j=r\), the product in (10) is \((-\lambda)^jF_j\).

Consequently \(\Gamma\gamma^jh=\gamma^{j+1}h\) for \(j<d\), while
\(\Gamma\gamma^dh=h\). In particular
\[
 \Gamma^N=1,\qquad v\Gamma=Q\Gamma v.
 \tag{12}
\]
The added rank-\(N\) term is essential. In the original prepared
coordinates its entire matrix is printable:
\[
 C^{-1}\Gamma C=-e_2K_1+
       c_*K_1^{-d}\otimes|d\rangle\langle0|_2.
 \tag{13}
\]
Indeed \(C^{-1}\Pi C=I\otimes|d\rangle\langle d|\), and
\(C^{-1}\Delta^dC=K_1^{-d}\otimes|d\rangle\langle0|\).
The last arrow in (13), multiplied by the \(d\) ordinary arrows,
has coefficient one. No nilpotent operator has been inverted.

## 3. The cyclic factor and its finite commutator

Let \(t\beta\ne0\), \(\beta^N=1-t^N\), on the marked root cover.
Use the existing determinant-normalized function from [A, (22)],
\[
 \mathfrak d_N(z)=(1-z^N)^{d/(2N)}
             \prod_{j=1}^d(1-Q^jz)^{-j/N},\qquad
 \mathcal C_t=\mathfrak d_N(tv).
 \tag{14}
\]
All roots are continued together from the anchored chart at zero to
the specified value of \(\beta\). On each clock eigenvalue its exact
functional equation is
\[
 \frac{\mathfrak d_N(Qz)}{\mathfrak d_N(z)}
       =\frac{\beta}{1-z},\qquad z^N=t^N.
 \tag{15}
\]
These factors are units on the stated nondegenerate cover. Combining
(12) and (15), including the cyclic arrow, gives
\[
 \mathcal C_t\Gamma^m\mathcal C_t^{-1}
       =\Gamma^m\frac{\beta^m}{(tv;Q)_m},\qquad
 R_m(tv):=\beta^{-m}(tv;Q)_m
       =\mathcal C_t\Gamma^{-m}\mathcal C_t^{-1}\Gamma^m.
 \tag{16}
\]
This holds for \(0\leq m\leq N\). At \(m=N\), both sides equal one
because \((tv;Q)_N=1-t^N=\beta^N\). Thus (16) retains the complete
periodic shift, unlike a verification on the nonzero nilpotent arrows
alone. It uses precisely the cyclic factor in the mixed identity
[A, (24)]; its common determinant normalization cancels in this
commutator, while the relative root \(\beta\) remains fixed.

## 4. Matching the two boundary clocks of the actual source

For the positive eight-face adapter [R, (17)], name its physical output
indices
\[
 m=[-k_2],\qquad s=[-k_1].
 \tag{17}
\]
Its physical matrix entry is \(M_{m,s;a,b}\). These are full colors,
not meridian or quantum-parameter derivative indices. In [R, (30)],
rename the four internal variables \(u,v,s,z\) as \(u_0,v_0,s_0,z_0\).
Then
\[
 K=u_0+v_0+1,\quad L=1-k_1+s_0+z_0,\quad
 r_0=u_0+v_0+s_0+z_0+2,
 \qquad K+L=r_0+s\pmod N.
 \tag{18}
\]
For \(\alpha=\alpha_{0235}\) and \(\beta=\beta_{0235}\), the retained
ratio of [R, (31)] and [E, (13)] is exactly the following, with the
primitive root called \(q\) in [E] here identified with \(Q\):
\[
 \frac{\overline W_{0235}(K+L)}
      {\overline W_{0235}(K+L-k_2)}
   =R_m(\alpha Q^{r_0+s}).
 \tag{19}
\]
Here \(\alpha^N+\beta^N=1\). Fixing the internal \(r_0\) only fixes a
scalar \(t=\alpha Q^{r_0}\); no internal variable is identified with a
physical boundary index. Define the corresponding output coupon
\[
 \mathcal F_{r_0}|m,s\rangle
       =R_m(tQ^s)|m,s\rangle.
 \tag{20}
\]
It is defined on every two-head boundary coordinate, independently
of any subsequent support restriction.

Let \(\operatorname{Rev}_0|s\rangle=|[-s]\rangle\), and put
\[
 \mathcal B=C(I\otimes\operatorname{Rev}_0),\qquad
 M=\mathcal BZ_1\mathcal B^{-1}=CZ_1C^{-1}.
 \tag{21}
\]
Then \(\mathcal BZ_2\mathcal B^{-1}=v\). The operator \(M\) has \(M^N=1\)
and commutes with \(\Delta,\gamma,v\): this follows from (7), since
\(Z_1\) commutes with \(K_1^{-1}J_{+,2}\), with \(\gamma\), and with
\(Z_2^{-1}\). It therefore commutes with \(\Gamma\) as well.
Define its explicit projectors and a controlled shift by
\[
 P_m(M)=\frac1N\sum_{j=0}^dQ^{-mj}M^j,\qquad
 \mathcal U=\sum_{m=0}^dP_m(M)\Gamma^m,\qquad
 \mathcal U^{-1}=\sum_{m=0}^dP_m(M)\Gamma^{-m}.
 \tag{22}
\]
The projectors retain all \(N\) multiplicity coordinates. No choice of
an eigenbasis or a smaller physical module is required.

**Exact residual adapter.** For every boundary coordinate and every
internal \(r_0\),
\[
 \boxed{\quad
 \mathcal B\mathcal F_{r_0}\mathcal B^{-1}
   =\mathcal C_t\mathcal U^{-1}
               \mathcal C_t^{-1}\mathcal U,
 \qquad t=\alpha Q^{r_0}.\quad}
 \tag{23}
\]
To prove this, conjugate the two commuting boundary clocks by
\(\mathcal B\). The left side is
\(\sum_mP_m(M)R_m(tv)\). Each projector commutes with
\(\mathcal C_t\) and \(\Gamma\), so (16) gives exactly the right side.
This proof establishes all matrix entries, including every wrap.

## 5. Original cap and arbitrary exterior

The coordinate change has the following exact source data:
\[
 \mathcal B^{-1}p=N\lambda^d|0,1\rangle,\qquad
 (\ell\mathcal B)_{m,s}=\frac{x^aF_a}{N^2},
 \quad a=[-s].
 \tag{24}
\]
The first formula follows from (8). For the second, expand the finite
preparation, with the wrap \(S_1^N=1\) fixed in (2), using
\({a\brack h}_Q=F_a/(F_hF_{a-h})\):
\[
 C|m,a\rangle=\sum_{h=0}^a(-1)^hx^hQ^{h(h+1)/2}
       {a\brack h}_Q|[m+h],a-h\rangle.
 \tag{25}
\]
Pairing with \(\ell\) leaves \(x^a/N^2\) times
\(\sum_h(-1)^hQ^{h(h+1)/2}{a\brack h}_Q=(Q;Q)_a\).
Thus (24) retains the whole marked row. Its pairing with its displayed
source column is one. With a different first wrap, (25) would carry
the corresponding wrap powers; they have not been silently omitted.

These are the original flag source expressed in the clock frame.
They do **not** assert that the exterior of the nine-cell coupon is
this special source. For an arbitrary actual exterior row \(\eta\)
and remaining output tensor \(Y_{r_0}\), the correctly oriented equality is
\[
 \eta\mathcal F_{r_0}Y_{r_0}
   =(\eta\mathcal B^{-1})
       (\mathcal C_t\mathcal U^{-1}
                    \mathcal C_t^{-1}\mathcal U)
       (\mathcal BY_{r_0}).
 \tag{26}
\]
The row in [R, (23b),(23c)] is used literally in this formula. All
paired-fiber sums, \(f_m\) factors, \(C_N\), Cartan factors, pivots,
framing and peripheral lines stay in that row or in \(Y_{r_0}\).
Equation (26) is bilinear; there is no Hermitian conjugation.
It holds before the remaining finite sums. The identity applies to
each circle/ray pattern before integration, so the source-preserving
integrability statement of [R] carries it through the actual pattern
integrals and their retained relative boundary components.

## 6. A source-fixed orthogonal coordinate frame

There is a useful explicit rescaling of the same adapter. For
\(a=[-s]\), set
\[
 H|m,s\rangle=\frac{\lambda^aQ^{ma}}{F_a}|m,s\rangle,
 \qquad \widetilde{\mathcal B}=\mathcal BH,\qquad
 \widetilde{\mathcal B}|m,s\rangle
       =\frac{\Delta^a|m,0\rangle}{F_a}.
 \tag{27}
\]
The last identity follows from (7), since \(C|m,0\rangle=|m,0\rangle\).
The diagonal \(H\) commutes with both boundary clocks and with
\(\mathcal F_{r_0}\). Replacing \(\mathcal B\) by
\(\widetilde{\mathcal B}\) leaves the actual right side of (23) unchanged;
the same replacement applies in (26).
In these coordinates, with \(S_s\) the cyclic shift of the second
coordinate and \(E_0\) its zero-coordinate projector,
\[
 \begin{gathered}
 v=Z_s,\quad M=Z_m,\quad \Gamma=\lambda S_sZ_s,\\
 \Delta=S_s^{-1}(1-QZ_s^{-1}),\qquad
 \gamma=\lambda S_sZ_s(I-E_0).
 \end{gathered}
 \tag{28}
\]
For \(\Delta\), this follows directly from (27). For \(\gamma\), use
\(\Delta\gamma=\lambda(v-1)\) and \(\gamma|m,0\rangle=0\).
The added arrow of \(\Gamma\) has coefficient
\((-\lambda)^{-d}=\lambda\). Its full cycle is
\(\lambda^NQ^{N(N-1)/2}=1\), retaining the even-level sign.
The original endpoint data become
\[
 \widetilde{\mathcal B}^{-1}p=N^2|0,1\rangle,\qquad
 (\ell\widetilde{\mathcal B})_{m,s}=Q^{-ms}/N^2.
 \tag{29}
\]
Hence, in the flat norm of these coordinates, \(v,M,\Gamma,\mathcal U\)
are unitary, \(\|\Delta\|\leq2\), and \(\|\gamma\|=1\).
The source column and full cap row have norms \(N^2\) and \(N^{-1}\).
Equivalently this specifies the positive physical Gram
\((\widetilde{\mathcal B}^{-1})^*\widetilde{\mathcal B}^{-1}\), fixed
without reference to the exterior word. It is not asserted to have
tame condition number in the original balanced norm. The cyclic
factor \(\mathcal C_t\), and every transformed exterior coupon, retain
their actual matrix entries and actions.

## 7. Scope

The physical operator construction (1)--(29) is valid for all \(N\geq2\), even
or composite. The existing literal nine-cell source occurrence
(17)--(19) is proved in [R,E] for odd \(N>2\); nothing here extends
that charged triangulation definition to even levels. The physical
space throughout has dimension \(N^2\), including all original head
coordinates and their original crossing endpoint data.

This realizes the specific retained ratio as a coupon in the actual
flag algebra. It does not show that the remaining \(W\)-factors in
[R, (31)] are the neighboring \(P(a\Delta)\) factors in [A, (24)].
The negative adapter [R, (18)] uses a mixed input/output pair of
boundary indices; (23) does not assert the same left-output
endomorphism formula for it without a further typed dual transport.
Nor does it justify cancelling adjacent commutators without checking
their full shared frames and inverse-dual exterior. No further
Pachner move, geometric source identification, whole-word norm bound or scalar
noncancellation follows from (23) alone. At a singular Fermat wall,
the relative expressions and their source lattices must be retained;
separate inverse factors in (14)--(23) are not evaluated there.

## Complete direct sources

All operator and source normalizations used above are fixed by these
complete texts. The cyclic-function and oscillator methods are existing
ones; the contribution is the source-specific all-boundary matching
(18)--(23) and its literal exterior transport.

- [A] [Actual shared quantum flags and their charged exchange](actual_shared_quantum_flags_and_charged_exchange.md), 459 lines, SHA-256 `dcab795cc141e2e1db726998cf7b1141dd03c681eaae9076387f90581f53a7d9`.
- [P] [The full dilogarithm resolves the actual charged flag pentagon at the root](actual_marked_full_phi_flag_pentagon.md), 328 lines, SHA-256 `3052cef4a1d666253562c13ceaf6a9bc472baf7691f23d13e33bb3f8d6e9888f`.
- [R] [Full-Psi ray crossings and the original nine-cell boundary](research_full_psi_ray_crossings_and_nine_cell_boundary.md), 588 lines, SHA-256 `495a2fde1ed1d7ca0707f060208121bddb2673be21ff3bcb9bac737420ac2d24`.
- [E] [Canonical evaluation of the literal nine-cell crossing](research_nine_cell_canonical_crossing_evaluation.md), 424 lines, SHA-256 `332062e67d64ab4a0767637c0fdd96f186d62c430ad38042aef35ad857d8d7c9`.
