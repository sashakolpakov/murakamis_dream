# Root-star sources: exact overlap with prior belt and pretzel results

31 October 2026. This is a source and coverage audit, not a new asymptotic
theorem or a classification of tangle isotopy types. It compares the literal
mixed-color source of \(C(h_0T(h_1\cdots h_s))\) with the earlier notes,
including all first Casimir normals and the original marked closure.

## 1. The mixed-color identity and the belt alphabet

Work in the full physical pair algebra
\(\mathcal H_N=\mathbb C[z]/(2T_N(z/2)+2)\), with its original turn
\(T\), crossing \(R\), ordinary circle \(L_j\), and marked functional
\(\phi\). Put

\[
h_j^\epsilon=T(R^\epsilon L_j),\qquad
Z_N(\mathbf j)=\phi\!\left(h_{j_0}^{\epsilon_0}
 T\!\left(\prod_{i=1}^s h_{j_i}^{\epsilon_i}\right)\right)
=\phi\!\left(L_{j_0}R^{\epsilon_0}
                  \prod_{i=1}^s h_{j_i}^{\epsilon_i}\right).
\tag{1}
\]

The last equality is the Frobenius turn identity, proved with the full
Newton basis in [the root-character contraction](actual_conway_root_character_fourier_contraction.md),
§1. Every color \(1\le j_i\le N\) remains independent.

The [literal octahedral belt construction](actual_balanced_octahedral_belt_stack_volume.md),
§1 and §4a, reads its two typed pieces as
\(f_+=T(RL_N)R^{-1}\) and \(f_-=RT(R^{-1}L_N)\).
The [mixed-circle packet](actual_belt_stack_auxiliary_color_inner_packet.md),
§§1 and 6, retains the same physical reflection and turn with every
ordinary color. Thus their mixed versions are exactly

\[
f_+(j)=h_j^{+1}R^{-1},\qquad f_-(j)=Rh_j^{-1}.
\tag{2}
\]

Here the superscript \(-1\) on \(h_j^{-1}\) denotes the negative
half-twist sign, not a multiplicative inverse. If all inner signs are
nonzero, let \(n_+\) and \(n_-\) count them and choose the fixed outer
crossing power \(a=\epsilon_0+n_+-n_-\). Commutativity within the full
pair algebra gives

\[
\begin{aligned}
\phi\!\left(L_{j_0}R^a\prod_{i=1}^s f_{\epsilon_i}(j_i)\right)
&=\phi\!\left(L_{j_0}R^{a-n_++n_-}
                       \prod_{i=1}^s h_{j_i}^{\epsilon_i}\right)\\
&=Z_N(\mathbf j).
\end{aligned}\tag{3}
\]

This is equality of the entire mixed-color scalar, not only its complete
value or its leading action. The physical turn/reflection formulas establish
(2) before commutativity is used; no normal directions or Cartan factors
are discarded.

The [long-filled belt theorem](actual_long_filled_octahedral_belt_stack_volume.md)
already supplies the whole-source packet and all-color estimates for every
fixed two-type word and every fixed integer \(a\), at both parities and
composite levels. It also proves independently long signed fillings of any
auxiliary subset for its literal belt diagram. Consequently the all-inner-
\(\pm1\) scalar in (1) overlaps that prior analytic theorem. A pure root
\(\epsilon_0=0\) is included by the choice of \(a\). An inner pure leaf
\(\epsilon_i=0\) is outside the recorded two-type alphabet; its inclusion
in the current source estimate should be stated separately.

Equation (3) alone proves neither isotopy of the two diagrams nor a
correspondence of their peripheral curves. The current root-star geometry
and filling calibration use the [marked-mask construction](actual_conway_general_mask_marked_filling.md)
for the literal current presentation. No new topological family or priority
claim follows from this comparison.

## 2. The missing Fourier mode was already proved

The [outer squared-kernel theorem](actual_outer_color_squared_kernel.md),
§§1–4, already retains values and first normals and gives

\[
\phi(L_{N-h}F)=N^2\sum_{\ell\in\mathbb Z}
 (1-\ell)(-1)^{(N-1)\ell}\widehat F_{\ell N-h},
\tag{4}
\]

where its angular coordinate is \(z=-2\cos\theta\). The potentially
small winding \(\ell=1\) has coefficient zero. Its finite double-pole
contour keeps all four boundary pieces and proves a whole-color gap from
a Gaussian angular packet and a strict complementary-node gap.

The present coordinate \(z=2\cos\vartheta\) differs by a shift of
\(\pi\). Writing \(F(2\cos\vartheta)=\sum a_re^{ir\vartheta}\), symmetry
and \(m=-\ell\) turn (4) into

\[
\phi(L_{N-h}F)=(-1)^hN^2\sum_{m\in\mathbb Z}
 (-1)^m(m+1)a_{h+mN}.
\tag{5}
\]

Thus the missing \(m=-1\) mode is the same cancellation. The current
residue derivation, calibrated chirp and periodic endpoint repair give an
alternative proof and an application to the stated child estimate; they
do not establish a previously absent Fourier identity.

## 3. Distinct nearby source families

The [pretzel source reduction](actual_pretzel_complete_base_casimir_polynomial.md),
§1, identifies the ordinary mixed odd-pretzel scalar with a product of
rotated boxes, hence with \(\phi(\prod_i h_{j_i}^{-1})\) in these
conventions. It has no outer \(L_{j_0}\). Its [long-filling theorem](actual_long_pretzel_full_source_survival.md)
and [width extension](actual_pretzel_all_width_extension.md) concern that
different marked source. The root-star argument therefore does not, merely
by (3), remove the recorded pretzel width restriction.

The [balanced alternating-source note](actual_alternating_balanced_source.md)
instead treats anchor defects in the charged source of an alternating
diagram, with an exact figure-eight obstruction. It is not a Conway
root-star or belt-source theorem.

## Audit scope

The comparison above reads the cited finite-source identities and their
stated theorem scopes. It does not reprove their asymptotic or geometric
dependencies, claim a new tangle equivalence, or assert coverage of every
algebraic link. Mathematical rendering and relative-link checks are
preservation checks; no numerical asymptotic experiment is used.
