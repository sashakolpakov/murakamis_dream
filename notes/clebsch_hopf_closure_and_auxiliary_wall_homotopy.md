# Global Hopf closure and an explicit auxiliary homotopy for the Clebsch wall

Research proof, 27 October 2026. The full two-channel memory has an
exact global cut-source complex, including the actual Hopf generators,
pivotal partial trace and retained Green moments. Its upper highest-spin
wall vanishes on the represented old-head algebra before Schur scalarity
or internal summation. More generally the wall of an arbitrary memory
operator is an explicit auxiliary Ward boundary.

This is an actual OLD-HEAD memory theorem. It does not identify this
algebra with the existing high-integral-color R, its coupled binomial
source, or a selected geometric Gaussian sector. An actual full-memory
word and an isolated upper channel have different current constraints.

## 1. The represented algebra and all actual Hopf rows

Use the Clebsch S and whole gauges D,B of
[the exact memory dilation](clebsch_memory_dilation_and_actual_r_excursions.md).
It is convenient to use its full frame

\[
 L_q=\mathcal B S^{-1}(D\otimes I_2),\qquad
 M_q(C)=L_q(C\otimes I_2)L_q^{-1}.                  \tag{1}
\]

For b old head factors use L_(q,b)=tensor_i L_(q,i), with the
actual head/auxiliary reordering understood. For EVERY actual total
Hopf operator retain

\[
 K_{\mathrm{tot}}^{mem}=L_b(\Delta^{b-1}K\otimes I_{aux})L_b^{-1},
 \quad E_{\mathrm{tot}}^{mem}=L_b(\Delta^{b-1}Ecal\otimes I_{aux})L_b^{-1},
 \quad F_{\mathrm{tot}}^{mem}=L_b(\Delta^{b-1}F\otimes I_{aux})L_b^{-1}.
                                                               \tag{2}
\]

For two old factors the literal totals are K tensor K,
Ecal tensor K+I tensor Ecal, and F tensor I+K^(-1) tensor F.
Equation (2), not a primitive replacement on the upper Fr channel,
keeps every mixed coproduct term. Since (1) is multiplicative,

\[
 M_b(\operatorname{ad}_h C)
       =\operatorname{ad}^{mem}_h M_b(C)              \tag{3}
\]

for the actual K,Ecal,F adjoints, and hence for their compositions
and all regular divided actions of the original integral family.
This is a strict map of the actual image Ward complexes. No matrix
entry or source coefficient is replaced by its separate expectation.

Here are explicit upper channel rows. Write T_ab,E_ab,F_ab,K_ab
for the two-by-two blocks, a,b in {+,-}. Then

\[
 (\operatorname{ad}_K T-T)_{++}
   =\sum_{a,b}K_{+a}T_{ab}(K^{-1})_{b+}-T_{++},
\]
\[
 (\operatorname{ad}_{Ecal}T)_{++}
   =\sum_{a,b}(E_{+a}T_{ab}-T_{+a}E_{ab})(K^{-1})_{b+},
\]
\[
 (\operatorname{ad}_FT)_{++}
   =\sum_a F_{+a}T_{a+}
     -\sum_{a,b,c}(K^{-1})_{+a}T_{ab}K_{bc}F_{c+}.   \tag{4}
\]

Every block in (4) is given by the explicit finite Clebsch formulas
applied to the actual generator or its inverse. The analogous
multi-leg rows follow by the same channel contractions in (2).
Deleting the terms with a lower channel changes these rows.

## 2. Auxiliary Ward rows identify exactly the represented algebra

Work first before L_q. Write an arbitrary operator on old head
tensor C^2 as an auxiliary block matrix T=(T_ab), a,b=0,1, whose
entries are old-head matrices. Define

\[
 P_{aux}(T)=\frac{T_{00}+T_{11}}2\otimes I_2,
 \qquad h_a=\operatorname{diag}(1,-1),\quad f_a=E_{10}.
\]

For an auxiliary current X set H_h(X)_01=X_01/2,
H_h(X)_10=-X_10/2 and its diagonal blocks zero. For a current Z
set H_f(Z)=diag(Z_10/2,-Z_10/2). Literal block multiplication gives

\[
 T-P_{aux}T=H_h([h_a,T])+H_f([f_a,T]).              \tag{5}
\]

The common kernel of the two auxiliary rows is precisely
End(old head) tensor I_2. Their actual-image two-term Ward complex
therefore contracts onto that algebra by the specified P_aux and H.
This is not a claim that the lower Clebsch channel itself is acyclic.

Conjugate every map in (5) by L_q. Put a_h=L_q(I tensor h_a)L_q^(-1)
and a_f=L_q(I tensor f_a)L_q^(-1), and use H_h^mem,H_f^mem for the
conjugated maps. Then on EVERY memory operator

\[
 T-P^{mem}T=H_h^{mem}([a_h,T])+H_f^{mem}([a_f,T]),
 \quad P^{mem}T=M_q\!\left(\tfrac12\operatorname{Tr}_{aux}
                                      L_q^{-1}TL_q\right).       \tag{6}
\]

The actual quantum action and this auxiliary action commute before
conjugation. Consequently the contraction (6) commutes with all
actual Hopf adjoints (2)--(3). It is a strong cut-source complex
retraction, not only a statement about invariant matrices. On b legs
use the commuting auxiliary averages P_i; the explicit global
homotopy is the telescoping sum of P_1...P_(i-1) H_i. This retains
all internal channel sources and is independent of word length.
For quantum-normal derivatives use the induced connection
nabla=partial-[L'_q L_q^(-1),-]. It transports the old derivative
and commutes with the auxiliary contraction. Unadorned entrywise
derivatives would omit the actual D/B/source connection terms.
An external semilinear/Ore map uses L_after O sigma(L_before^(-1));
the displayed conjugations are for the linear maps at their stated
coefficients. This retains changed source frames under Ore shifts.

The source matters. The literal original coupon e=gD_mark has the
memory row

\[
 \Phi_{mem}(T)=\tfrac12\operatorname{Tr}[M_q(e)T].    \tag{7}
\]

It satisfies Phi_mem P^mem=Phi_mem on ALL extended operators,
directly by the auxiliary trace. Thus (6) preserves the original
cut source, pivot, defect, 1/N and the separate full peripheral
line. A rank-one upper pointing agrees on represented complete
words but need not satisfy this identity on arbitrary channel
pieces. In particular an original high-color coupled binomial
pointing is not silently replaced by (7).

## 3. An explicit wall projection and its nullhomotopy

For an upper matrix A in End(Sym^N) let
K_A(t,u)=ell_N(u) A psi_N(t), with the actual binomial dual.
Define the polynomial wall row

\[
 \mathcal W_N(A)(t)=t^N K_A(t,-1/t)
   =\sum_{i,j=0}^N(-1)^i{N\choose i}A_{ij}t^{N+j-i}.
                                                               \tag{8}
\]

Its kernel is EXACTLY image(E_N). The already proved numerator
identity makes every elevated matrix divisible by 1+tu. Conversely
vanishing at u=-1/t implies this divisibility in k[t,u]; a quotient
of bidegree at most (N-1,N-1) is the unique old-head matrix numerator.
This also gives an explicit wall projection, not just a dimension
or highest-spin assertion. Its quotient has dimension 2N+1.

With the whole upper gauge use W_(N,q)(A)=W_N(B_+^(-1)AB_+).
For EVERY old matrix C, before any Ward closure or finite sum,

\[
                 \mathcal W_{N,q}([M_q(C)]_{++})=0. \tag{9}
\]

Apply the same row to (6). The represented part is killed by (9),
so an ARBITRARY upper wall has the exact auxiliary cochain formula

\[
 \mathcal W_{N,q}(T_{++})
 =\mathcal W_{N,q}\!\left(
  [H_h^{mem}([a_h,T])+H_f^{mem}([a_f,T])]_{++}\right). \tag{10}
\]

This is the promised explicit nullhomotopy, with the two auxiliary
current rows retained. Actual represented R words, pivots and Green
moments commute with a_h,a_f, so their full wall is zero by (10).
Individual channel paths need not commute with them. Their upper
wall cancels against the retained excursion walls in precisely
the sum (10), not because each path is zero or because a knot
endomorphism has already been declared scalar.
Precisely, this is a nullhomotopy from the auxiliary actual-image
Ward complex to the wall vector space in degree zero. It does not
assert that the FULL memory Hopf action induces an autonomous
differential on the upper wall alone. In particular it is not an
unproved map to the intrinsic high-color Fr Borel quotient complex.

## 4. Actual pivotal closure, including the channel cap

Let g_W be the SPECIFIED actual pivot on an old closed strand.
For the full memory pivot g_W^mem=M_W(g_W), define the normalized
auxiliary partial trace

\[
 \mathfrak P_W(T)=\tfrac12\operatorname{Tr}_{mem W}
                               [(I\otimes g_W^{mem})T].          \tag{11}
\]

It has the explicit four-block cap

\[
 \mathfrak P_W(T)=\tfrac12\sum_{a,b\in\{+,-\}}
                   \operatorname{Tr}_{H_a}[(I\otimes g_{ab})T_{ba}].
                                                               \tag{12}
\]

Both off-diagonal cap terms are part of the actual source. Trace
invariance on the closed leg proves, for EVERY old tensor matrix C,

\[
 \mathfrak P_W(M_{VW}(C))
       =M_V\!\left(\operatorname{Tr}_W[(I\otimes g_W)C]\right).
                                                               \tag{13}
\]

No R invariance, scalarity or summation hypothesis is used in (13).
It therefore holds coefficientwise on retained actual Green arrays
and normal insertions whenever they are represented old operators.
Equations (9), (13) imply wall zero after arbitrary actual closure
as a cochain identity. The same holds for the full channel currents
(4), because (3) puts each back in the represented algebra.

For the actual pivotal family, (11) is a Hopf-adjoint chain map
on ALL memory operators, by the actual cap identities; the auxiliary
normalization is an explicit scalar factor. The auxiliary currents
on a closed leg have zero trace, those on an open leg pass through,
and (13) commutes with the global auxiliary retraction. The 1/2 is
not relabeled as a new ribbon quantum dimension or a new cup/cap
functor. It is the stated normalized auxiliary co-source in this
matrix-memory comparison.

### The frozen ADO pivot has its actual normal cap defect

Whole pivotal naturality must use the correct family. The ordinary
generic integral family uses its genuine pivot g=K. At Q_N the
original ADO pivot g=K^(1-N) is also pivotal because K^(-N) is
central. Freezing that expression off the root is different.
For a diagonal g commuting with K, direct actual coproduct expansion
gives the two OLD cap defects

\[
 \operatorname{ptr}_g(\operatorname{ad}_{Ecal}C)
 -\operatorname{ad}_{Ecal}\operatorname{ptr}_g(C)
  =\operatorname{Tr}_W([K_W^{-1}g_W,Ecal_W]C)K_V^{-1},
\]
\[
 \operatorname{ptr}_g(\operatorname{ad}_{F}C)
 -\operatorname{ad}_{F}\operatorname{ptr}_g(C)
  =K_V^{-1}\operatorname{Tr}_W
                  [(g_WF_W-K_WF_Wg_WK_W^{-1})C].     \tag{14}
\]

For g=K^(1-N), Z=Q^N, these inserted rows are respectively

\[
 [K^{-N},Ecal]=\frac{1-Z}{Z}Ecal K^{-N},\qquad
 gF-KFgK^{-1}=-\frac{1-Z}{Z}gF.                    \tag{15}
\]

Their divided first normals need not vanish. Transport them through
M_W and the SAME four-block cap; they remain represented old rows
and retain (9), but are not silently set to zero. The prescribed
meridian/modified-dimension source and framing derivatives remain
their original marked data.

## 5. Whole moments and the remaining comparison

The auxiliary-bit identity M(J_head)=J_total-A_aux^mem from the
memory theorem is part of this global complex. Consequently every
retained polynomial Green moment and whole clock is represented
with its exact offset, before closure or a normal jet is taken.
Dropping that bit would violate (13) for the actual weighted rows.

On P1 these are finite global-section and Serre-co-source maps.
The Clebsch splitting is not an O-linear bundle isomorphism
O(N-1)^2=O(N) direct_sum O(N-2); those bundles have different
splitting types. The relevant Euler sequence splits on global
section representations, and the Cech maps are differential/chain
maps with the stated endpoint homotopies. No fiberwise gauge is
invented from the finite vector-space isomorphism.

The represented-old-operator wall is now controlled explicitly,
including tensor Hopf currents and pivotal closure. This does not
prove that a selected internal Gaussian period belongs to that
represented source complex, nor identify the ACTUAL high-color
R and coupled wall source with this auxiliary model. The latter
source can evaluate an off-image highest-spin wall nontrivially;
its character cannot be removed using (10). Those are the remaining
normal/mixed-current and geometric-source comparisons.

[Exact global current/closure/wall audit](../experiments/audit_clebsch_hopf_closure_and_wall.py).
The [results](../experiments/clebsch_hopf_closure_and_wall_results.json)
pass eight generic/root actual cases N=2,...,5, including 432 full
auxiliary matrix-unit homotopies, 108 represented-head current units,
the actual tensor R Ward rows, both specified pivotal families and
their frozen-ADO cap defects. All 16 tested off-diagonal channel
cap contributions are nonzero and retained.
