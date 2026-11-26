# The negative retained Pachner ratio after an ordered pivotal bend

Research note, 22 November 2026. The negative nine-cell residual uses
an input color and an output color. Bending that input with the original
ordered cup makes these two colors a genuine pair of complete physical
heads. The residual is then the same commutator as in [D], with the full
original exterior transported by its inverse dual.

The bend is the ordinary rigid adjunction, not a new quantum operation.
The source-specific identification here is the negative index placement
in [R, (18),(31)]. It does not assume a Hermitian pairing or the proposed
reflected full-dilogarithm seam.

## 1. Original ordered cup, evaluation and bend

Fix \(N\geq2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\(x=-q^{-1}\). Write \(V\) for the original complete balanced head.
The original cup and ordinary evaluation, as fixed in [D,C], are
\[
 p_{m,a}=N x^{m-d}\delta_{m+a,d},\qquad
 \varepsilon_{a,m}=\frac{x^a}{N}\delta_{a+m,d}.
 \tag{1}
\]
The deltas in (1) are ordinary equalities in \(0,\ldots,d\).
The orders of the two indices are part of these tensors. Directly,
\[
 \sum_a p_{m,a}\varepsilon_{a,n}=\delta_{mn},\qquad
 \sum_m\varepsilon_{a,m}p_{m,b}=\delta_{ab}.
 \tag{2}
\]
No inverse quantum dimension is used; the ordinary closed-circle
evaluation may vanish at this root.

The original head representation \(\rho\) has an explicit right-dual
identification, with the dual head placed first:
\[
 T_R e_j=x^{-j}e_{d-j},\qquad
 T_R\,\rho(\mathscr S^{-1}h)^tT_R^{-1}=\rho(h).
 \tag{3}
\]
Here \(\mathscr S\) is the original Hopf antipode. For the balanced
generators,
\(\mathscr S^{-1}(K)=K^{-1}\),
\(\mathscr S^{-1}(F)=-FK\),
\(\mathscr S^{-1}(e)=-K^{-1}e\), and
\(\mathscr S^{-1}(H)=-H\).
Substitution gives respectively the original coefficients
\(xQ^{-j}\), \(1-Q^{j+1}\),
\(x^{-1}(1-Q^{-j})\), and \(d-2j\), with their zero endpoints.
Thus both heads used below carry the original complete color,
not an unidentified Euclidean dual. The right coevaluation
\(N\sum_jT_Re_j\otimes e_j\) is precisely the ordered cup in (1).

Let \(T:V_a\otimes V_b\longrightarrow V_c\otimes V_e\) be any
two-head tensor, with entries \(T_{c,e;a,b}\). The letter \(e\)
here is an output index, not the generator in (3). Define
\[
 \mathfrak B(T)=(I_m\otimes T)(p_{m,a}\otimes I_b),
 \qquad
 \mathfrak B(T)_{m,c,e;b}
       =N x^{m-d}T_{c,e;d-m,b}.
 \tag{4}
\]
There is no permutation between the ordered cup and \(T\).
The result is a map \(V_b\to V_m\otimes V_c\otimes V_e\).
Its inverse is the actual evaluation bend:
\[
 T_{c,e;a,b}=\sum_m\varepsilon_{a,m}
                          \mathfrak B(T)_{m,c,e;b}.
 \tag{5}
\]
In particular \(\mathfrak B(I)=p\otimes I\), confirming the native
head order. Feeding the other leg of the cup and then flipping
the two outputs would require an additional pivotal clock; that
operation is not silently substituted for (4).

As a map of full coefficient spaces, \(\mathfrak B\) is an invertible
reshuffling times unit phases and \(N\). Therefore
\[
 \|\mathfrak B(T)\|_{\rm HS}=N\|T\|_{\rm HS},\qquad
 \|\mathfrak B^{-1}(Y)\|_{\rm HS}=N^{-1}\|Y\|_{\rm HS}.
 \tag{6}
\]
There is no rank projection or discarded boundary coordinate.

## 2. The negative physical indices

In the negative replacement array [R, (18)], write
\[
 (c,e;a,b)=(\gamma,\delta;\alpha_0,\beta_0),\qquad
 c=[-k_1],\quad e=[-k_4],\quad
 a=[k_2-1],\quad b=[k_3-1].
 \tag{7}
\]
Use \(\beta\) below only for the recorded Fermat root, not for
the input index \(\beta_0\) of [R]. The first beta move retains
\[
 \frac{\overline W_{0235}(K+L)}
      {\overline W_{0235}(K+L-k_2)}
   =R_{d-a}(tQ^c),\qquad
 R_j(Z)=\beta^{-j}(Z;Q)_j .
 \tag{8}
\]
Indeed \([-k_2]=d-a\). Renaming the four internal variables of
[R, (30)] as \(u_0,v_0,s_0,z_0\), one has
\[
 K+L=r_0+c\pmod N,\qquad
 r_0=u_0+v_0+s_0+z_0+2,\qquad
 t=\alpha_{0235}Q^{r_0},\quad
 \beta^N=1-t^N.
 \tag{9}
\]
The internal \(r_0\) is independent of the external \(m,c\) pair.
Work on \(t\beta\ne0\); all cyclic products use the same recorded root \(\beta\).

Define its Schur action on a whole tensor by
\[
 (\mathcal R_t^-(T))_{c,e;a,b}
       =R_{d-a}(tQ^c)\,T_{c,e;a,b},\qquad
 \mathcal F_t|m,c\rangle=R_m(tQ^c)|m,c\rangle .
 \tag{10}
\]
The ordered pivotal bend gives the exact all-entry identity
\[
 \boxed{\quad
 \mathfrak B(\mathcal R_t^-(T))
       =(\mathcal F_t\otimes I_e)\mathfrak B(T).
 \quad}
 \tag{11}
\]
This is obtained simply by substituting \(a=d-m\) in (4).
No Hopf-intertwining condition on \(T\) is required.

## 3. The same physical commutator with its actual row

Apply the rescaled physical flag frame
\(\widetilde{\mathcal B}_{m,c}\) of [D, (27)] to the first two
outputs of (4), leaving \(e,b\) as spectators. Put
\[
 \mathfrak Q(T)=(\widetilde{\mathcal B}_{m,c}\otimes I_e)
                     \mathfrak B(T),\qquad
 O_t=\mathcal C_t\mathcal U^{-1}\mathcal C_t^{-1}\mathcal U .
 \tag{12}
\]
Here \(\mathcal C_t=\mathfrak d_N(tv)\) and
\(\mathcal U=\sum_{j=0}^dE_j(M)\Gamma^j\) are exactly those in [D],
on this actual dual-input/output pair. In particular \(M\) is the
multiplicity clock, not a peripheral meridian. Equations (11) and
[D, (23)] give
\[
 \boxed{\quad
 \mathfrak Q(\mathcal R_t^-(T))
        =(O_t\otimes I_e)\mathfrak Q(T).
 \quad}
 \tag{13}
\]
All \(N^4\) tensor coefficients remain. This extends the negative
mixed-index placement; it does not declare that the negative
crossing has the positive left-output placement before bending.

For an arbitrary bilinear exterior \(\eta_{c,e;a,b}\), its exact
bent row is
\[
 \widehat\eta_{m,c,e;b}
       =\frac{x^{d-m}}{N}\eta_{c,e;d-m,b}.
 \tag{14}
\]
Thus, writing pairings as complete coefficient contractions,
\[
 \langle\eta,\mathcal R_t^-(T)\rangle
  =\left\langle
    \widehat\eta(\widetilde{\mathcal B}_{m,c}^{-1}\otimes I_e),
    (O_t\otimes I_e)\mathfrak Q(T)\right\rangle .
 \tag{15}
\]
There is no complex conjugation. The ordinary evaluation in (1)
serves only to bend the chosen input; it does not replace the
full marked cap present in \(\eta\).

For the actual source, use the entire exterior of [R, (23b),(23c)],
or its full paired-fiber version [R, (29)]. The factors \(f_m\),
\(C_N\), all original Cartan and pivotal factors, framing and peripheral
lines remain in that row and the remaining tensor. The negative
sector factor \(Q^{D_\chi}\) also remains there; it is not a shift of
the clock in (9). The already computed negative phase \(\phi_-=0\)
of [R, (18)] is unchanged.

The equality holds for each fixed internal tuple before every
remaining finite sum. It therefore holds in every original circle/ray
pattern with its complete source measure and relative boundary
components. The bend is independent of the pattern variables;
the source-preserving integrability statement in [R] remains applicable.

## 4. Scope and complete sources

The ordered bend and physical operator identity (13) hold for every
\(N\geq2\), including even and composite levels, on the regular marked
Fermat cover. Their occurrence as the literal charged negative
nine-cell source is currently proved in [R] for odd \(N>2\).
Together with [D], both signs of the retained ratio now have explicit
physical commutator realizations, with their different boundary typing
and full inverse-dual rows retained.

Only the bend itself has the exact norm costs (6). No condition-number
bound for \(\widetilde{\mathcal B}\), common positive Gram for further
gluings, reflected full-function sewing, or selected geometric
noncancellation follows. The complete remaining nine-cell factors
and original general closing are not eliminated by this identity.

- [D] [Physical flag adapter](research_retained_pachner_ratio_physical_flags.md), 365 lines, SHA-256 650d25db94060e306464ae00ef92ceb1e51ba4bec53da2c15ee67a89113be21a.
- [R] [Full-Psi ray crossings and the original nine-cell boundary](research_full_psi_ray_crossings_and_nine_cell_boundary.md), 588 lines, SHA-256 495a2fde1ed1d7ca0707f060208121bddb2673be21ff3bcb9bac737420ac2d24.
- [C] [Actual Pascal packets and their original turns](actual_pascal_coherent_gram.md), 494 lines, SHA-256 b6e6d697b4e21d30ca683f265b9c41170a0bee424d783169b2e0c70233dc889e.

The complete 645-line [shared-face Fourier source](actual_crossing_shared_face_fourier_source.md),
SHA-256 e2168c834bca48121428977473a8277d2684d19e47314034e1dc5c38c5c93179,
is coverage only: it retains the original Green/current source and
circle-to-orbit map, but does not identify this negative mixed pair
with the physical commutator. No novelty is claimed for pivotal
adjunction or coefficient reshuffling.
