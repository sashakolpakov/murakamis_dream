# A marked short corridor outside the three/four reduction

Private written deduction, 10 November 2026. No mathematical numerical
evaluation, test, import or compilation is used. The existing rational
normal form is not reproved here. Its uniqueness gives an exact test
for a prescribed coefficient alphabet, and already excludes a universal
reduction to positive three/four paths by end twists and proper
half-turns. The obstruction concerns that marked reduction, not the
volume conjecture or the exponential rate of the unreduced source.

The second distinction is analytic: the actual joining of two proved
single-power kernels retains a turn. Omitting it merges their powers
and changes the finite source. The existing concentrated boundary class
is not closed under arbitrary turns, even on actual tangle sources.

## 1. A coefficient-alphabet test with both boundary frames fixed

Use the physical crossing \(R\), turn \(T\), and affine pillowcase
maps of [the marked move theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_marked_degree_two_tangle_moves.md):
\[
 \widetilde R^{\,n}(x,y)=(x+ny+n/2,y),\qquad
 \widetilde T(x,y)=(-y,x+1/2).
 \tag{1}
\]
Their linear parts are
\[
 A_n=\begin{pmatrix}1&n\\0&1\end{pmatrix},\qquad
 S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
 \tag{2}
\]
The symbols \(A_n\) in this section are two-dimensional integral
matrices; the original quantum matrices will have a different symbol
in Section 3.

Let a fixed corridor have projective linear matrix \(G\). Choose its
deck sign so that its lower-left entry is \(C>0\), and suppose
\(C\ge2\). Integral twists on the left and right leave \(C\) and the
two diagonal residues modulo \(C\) unchanged. The determinant-one
condition makes both residues nonzero. There is consequently a unique
normalization by these two end twists of the form
\[
 G_0=\begin{pmatrix}A&B\\C&D\end{pmatrix},
 \qquad 0<A,D<C,\qquad B=(AD-1)/C.
 \tag{3}
\]
All physical half-turns retained in the marked normal form have
identity linear part on the pillowcase, up to the deck sign. They
do not change (3).

Fix any alphabet \(\mathcal B\subseteq\{2,3,\ldots\}\). A replacement
in this section must preserve the two outside frames and arbitrary
outside tangles. It may add fixed integral end twists and the specified
proper half-turn, but may not add an outside quarter-turn or a new
long filling.

**Proposition 1.** Such a uniform-negative replacement
\[
 R^r T R^{-b_1}T\cdots T R^{-b_k}T R^s H,
 \qquad b_j\in\mathcal B,
 \tag{4}
\]
exists if and only if the unique negative continued fraction of
\(C/A\), with all coefficients at least two, has every coefficient
in \(\mathcal B\). A uniform-positive replacement of the same form
with \(R^{b_j}\) instead exists if and only if the corresponding
continued fraction of \(C/(C-A)\) has every coefficient in
\(\mathcal B\).

*Proof.* The [definite corridor normal form](research_definite_rational_corridor_normal_form.md),
Sections 2--3, proves that a negative word with all \(b_j\ge2\)
has normalized ratio
\[
                         C/A=[b_1,\ldots,b_k]_-.
 \tag{5}
\]
It also proves uniqueness by the ceiling Euclidean algorithm:
the next coefficient is the ceiling of the current complete
quotient, and its remainder determines the next quotient.
Thus (5) is necessary. Conversely, the same theorem realizes
that continued fraction with the unique full matrix (3), and
then restores both end twists and the actual affine half-turn.
This gives the marked identity for arbitrary attached tangles.

For the positive statement, conjugate a negative-word matrix by
\(\operatorname{diag}(1,-1)\). On projective linear parts this
changes every negative crossing to a positive one and preserves
the turn. If the negative normalized matrix is
\(\left(\begin{smallmatrix}A'&B'\\C&D'\end{smallmatrix}\right)\),
the positive matrix, after choosing lower-left entry \(C>0\),
is
\[
                 \begin{pmatrix}-A'&B'\\C&-D'\end{pmatrix}.
 \tag{6}
\]
Its normalized first diagonal residue is \(C-A'\).
Consequently matching (3) requires \(A'=C-A\), and (5)
becomes the second continued fraction in the proposition.
The full affine correction is again the prescribed proper
half-turn. This argument proves a boundary-map identity; it
does not replace only one attachment by its mirror. \(\square\)

This is a test for reductions of the specified marked corridor
form. Special fixed attachments can have further stabilizers.
The proposition does not exclude identities exploiting such an
attachment or an unrelated finite-level quantum relation.

## 2. An explicit adjacent pair

Consider the fixed corridor
\[
                           W=T R^3 T R^5 T.
 \tag{7}
\]
Direct integer multiplication gives
\[
 S A_3 S A_5 S
   =\begin{pmatrix}-5&1\\14&-3\end{pmatrix},\qquad
 A_1(S A_3 S A_5 S)A_1
   =\begin{pmatrix}9&7\\14&11\end{pmatrix}.
 \tag{8}
\]
Its two ratios in Proposition 1 are exactly
\[
 \frac{14}{9}=[2,3,2,2,2]_-,
 \qquad
 \frac{14}{5}=[3,5]_-.
 \tag{9}
\]
For the first equality the successive tails from the right are
\(2,3/2,4/3,9/4,14/9\); the second is \(3-1/5\).
Thus neither sign has a replacement whose coefficients all
belong to \(\{3,4\}\), even allowing arbitrary length and fixed
integral twists at both ends. Reversing the corridor reverses
the continued-fraction lists and does not change this conclusion.

Nor can (7) be replaced by one arbitrary nonzero-power kernel
with only those end adapters. The necessary and sufficient test
in [single-corridor compression](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_rational_corridor_compression.md),
Proposition 1, requires the two normalized diagonal residues to
be the same \(1\) or \(-1\) modulo \(C\). Here they are \(9,11\)
modulo \(14\), neither \(1\) nor \(13\).

The same obstruction excludes reducing (7) to a same-sign run
of twos with only those end adapters: every such run has the
marked one-vertex form proved by
[the repeated-two reduction](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_repeated_two_crossing_chain_reduction.md),
Proposition 2. Composing its end twists and proper rotation
with the proposed adapters would give the excluded one-vertex
form for (7).

These are exact restrictions even under the stronger hypothetical
assumption that every positive three/four path already had a complete
boundary theorem. They do not assert that the pair \((3,5)\) has no
other useful presentation or cannot be estimated directly. In
particular (9) is itself a valid uniform-sign presentation; its
new adjacent powers still require their actual coherent contraction.
No added separator has been used to turn them into a covered
long-separated family.

## 3. The turn in the exact finite composition

Now return to the original full algebra and use the quantum notation
\[
 \mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2),\quad D_N=N-1,
 \quad \phi_N(e_i e_j)=\delta_{i+j,D_N},\quad
 \mathsf J_{ij}=\delta_{i+j,D_N}.
 \tag{10}
\]
Let \(M\) be multiplication by the original crossing, including
\(\kappa_N=\exp(\pi iD_N^2/(2N))\), and put
\[
 \mathsf A_n=\mathsf J M^n,\qquad
 v(w)=(e_0(w),\ldots,e_{D_N}(w))^T,\qquad
 P_n(w,z)=v(w)^T\mathsf A_n v(z).
 \tag{11}
\]
The identity \(M^T\mathsf J=\mathsf J M\) makes every
\(\mathsf A_n\) symmetric. The full single-power theorem
[for every nonzero degree-two filling](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_all_nonzero_degree_two_fillings.md)
estimates precisely \(P_n\), with both free ordinary variables
and their original normal data.

Two different contractions of these same polynomials must be
distinguished. Direct Frobenius gluing gives
\[
 \phi_z[P_a(w,z)P_b(z,u)]
   =v(w)^T\mathsf A_a\mathsf J\mathsf A_bv(u)
   =P_{a+b}(w,u).
 \tag{12}
\]
The last equality uses
\(\mathsf A_a\mathsf J\mathsf A_b
 =\mathsf J M^a\mathsf J^2M^b=\mathsf A_{a+b}\).

In contrast, the actual two-adjacent-vertex path is
\[
 Q_{a,b}(w,u)=v(w)^T\mathsf A_a\mathsf A_bv(u)
 =\phi_x\phi_y[
       P_a(w,x)K_T(x,y)P_b(y,u)],
 \qquad K_T(x,y)=\sum_{j=0}^{D_N}e_j(x)e_j(y).
 \tag{13}
\]
Indeed the two pairings contribute
\(\mathsf A_a\mathsf J I\mathsf J\mathsf A_b\).
Equivalently, (13) is
\(\phi_x[P_a(w,x)(\mathsf T_xP_b)(x,u)]\), where
\(\mathsf T e_j=e_{D_N-j}\).
There is no extra scalar in either identity: the original
crossing factors already occur in \(M^a,M^b\).
All products are taken before the full traces, so (12)--(13)
retain both parities, every first normal at a double root,
and the odd simple root.

Thus replacing (13) by the easier single-trace composition
(12) deletes the turn and changes the source to power \(a+b\).
Single-power upper bounds do not make that deletion legitimate.
The exact ordinary adapters and their potentially growing-order
Fourier observations are also explicit in
[the adjacent-kernel observation theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_mixed_two_adjacent_ordinary_observation_adapter.md),
Sections 1--3.

End crossing adapters are different: if a complete concentrated
boundary theorem is already known, canonical multiplication by
a fixed crossing preserves it under
[boundary crossing preservation](research_boundary_crossing_packet_preservation.md).
For a rational normal-form identity the exact quantum transformation is
\[
 \mathcal Q_N(W)=\kappa_N^\ell
 M^r[\mathsf J M^{-b_1}\mathsf J\cdots
               \mathsf J M^{-b_k}\mathsf J]M^s,
 \qquad
 \ell=\frac{e(W)-r-s+\sum_jb_j}{3}\in\mathbb Z.
 \tag{14}
\]
Here \(e(W)\) is the original signed crossing sum. The phase changes
and unit scalars from the two canonical boundary multiplications are
those in Sections 4--5 of the normal-form theorem. Formula (14)
does not erase the separately specified physical half-turn.

## 4. Why the known analytic class cannot supply automatic turns

There is already an actual-source obstruction, not merely a formal
possibility. For every fixed \(|p|\ge2\), the terminal source
\(H_{p,N}=\mathsf T(R^p)\) has the complete nonzero local packet
and a strict whole-real angular gap. But
\[
             \mathsf T H_{p,N}=\operatorname{can}(R^p).
 \tag{15}
\]
At every physical angle \(\tau_j=\pi(D_N-2j)/N\), the latter has
the exact value
\[
 \operatorname{can}(R^p)(-2\cos\tau_j)
  =\exp\!\left(\frac{\pi i pD_N^2}{4N}
                     +\frac{ipN\tau_j^2}{4\pi}\right),
 \qquad |\operatorname{can}(R^p)(-2\cos\tau_j)|=1.
 \tag{16}
\]
As proved in Section 7 of boundary crossing preservation, a nonzero
even local packet at the nodes tending to zero forces its real
complete rate to be zero. At physical nodes tending to any fixed
nonzero real angle, a strict angular bound at rate zero would
then force the modulus to tend to zero, contradicting (16).
This holds at both parities.

Consequently a theorem asserting closure of the existing concentrated
class under every short turn is false. This does not disprove a
source-specific theorem for (13), whose geometric action and contributing
cycle can change. The existing
[finite-kernel composition theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_finite_two_boundary_kernel_closure.md)
proves such preservation with a sufficiently long intervening power,
and explicitly retains that hypothesis.

## 5. What remains for arbitrary partial fillings

The exact [source compiler](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_arbitrary_power_source_compilation.md)
does cover every finite Conway expression. At a branch it keeps the
multiplication tensor
\[
                       \mu_{ijr}=\phi_N(e_i e_j e_{D_N-r}),
 \tag{17}
\]
and every still-free ordinary boundary variable. The
[internal-wire averaging theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_internal_wire_exact_circle_averaging.md)
then integrates every paired index exactly, with factor \(N\) per
internal wire. It retains full Hermite data and all signed powers.
That identity removes internal-index alias errors in its stated
representation; it does not remove the original angle traces or
provide their calibrated competing-current bounds.

Thus the obstruction is already present for the rational two-port
example (7), before branching is considered. General arborescent
components additionally retain (17) and more outside boundaries.
The rational-corridor theorem does not replace those tensors by
a two-boundary path.

A useful sufficient next theorem is therefore a complete boundary
estimate for the actual uniform-sign chains with arbitrary magnitudes
at least two, stable under the particular turns in (13), or a direct
estimate for the fixed short component after its actual surrounding
contraction. The marked rational normal form would transfer such a
theorem with its end crossings and scalar (14) retained. No such
general analytic conclusion follows here, and no closed-knot or
finite-exception statement is inferred.

## 6. Frozen direct source bindings

All files below were read in the sections used above. The listed
hashes bind the exact source statements, not new evaluations.

| Source | SHA-256 |
|---|---|
| research_definite_rational_corridor_normal_form.md | 7d74cd2247aee1b87a1d225364c29df12469a9bd87d6680667cf48367475d147 |
| research_rational_corridor_compression.md | 3feea5432842284b8c6fe20f1ea8c3cae2b10c174b8f707340a69183641f368c |
| research_marked_degree_two_tangle_moves.md | 0951bded882c68d38fc6f1cede247f628f103102386940d63d5ed93d90b55158 |
| research_repeated_two_crossing_chain_reduction.md | e56a85bae513ebaadb28bd0b50a752e892e3b29035e8b3d43a7ee33f9fb7a6d1 |
| research_all_nonzero_degree_two_fillings.md | 7ac634d458e5805e95a7ce064d4e1fc513c96c0b758cfaee9f91fd46de10304c |
| research_boundary_crossing_packet_preservation.md | a2f9cadf0fd6f23889ea7d20b469055fe33cb9df4d971668a2923666983cfec8 |
| research_finite_two_boundary_kernel_closure.md | 759118c877a9657355d5c457bfc3d0b7a45cc2601a8b247f4e030c90770155cc |
| research_arbitrary_power_source_compilation.md | 55e2de84870cfd20dac5922791dbc2bed54909439dfbf4663f17c70a1089445f |
| research_internal_wire_exact_circle_averaging.md | 0efa85a43da064197f25422d86ef37688971f2dface55da9d5efef3ccb0d08ef |
| research_mixed_two_adjacent_ordinary_observation_adapter.md | 9d6cd4139f53754c2fc4164e239f3f6c650fbc4631923416eeb7016179e53478 |
