# Exact Clebsch memory for degree elevation and unavoidable actual R excursions

Research proof, 27 October 2026. The degree-elevation map is the upper
corner of an explicit unital algebra representation. Its complementary
channel has dimension N-1, is minimal among per-strand unital matrix
algebra dilations, and strictifies every ordered word exactly. Whole
head/Fr gauges, source and co-source can be transported without losing
that channel. The actual R matrix does not preserve the upper channel;
a uniform inverse-crossing calculation measures the missing excursion.

This gives finite algebraic memory, not an acyclic lower channel or a
Gaussian source projection. No Ward-exactness of the lower excursions
is assumed.

## 1. Explicit upper and lower maps

Let n=N-1, N>=2, H_n=Sym^n with basis v_j, and let u_0,u_1 be
the standard two-dimensional basis. Write H_+=Sym^N with basis V_j
and H_-=Sym^(N-2) with basis w_j. Out-of-range vectors are zero.
Define the upper inclusion and projection

\[
 \Delta V_j=v_j\otimes u_0+v_{j-1}\otimes u_1,
\]
\[
 m(v_j\otimes u_0)=\frac{N-j}{N}V_j,\qquad
 m(v_j\otimes u_1)=\frac{j+1}{N}V_{j+1}.             \tag{1}
\]

The normalized lower maps are

\[
 \iota w_j=\frac{j+1}{N-1}v_{j+1}\otimes u_0
       -\frac{N-1-j}{N-1}v_j\otimes u_1,
\]
\[
 \rho(v_j\otimes u_0)=\frac{N-1}{N}w_{j-1},\qquad
 \rho(v_j\otimes u_1)=-\frac{N-1}{N}w_j.             \tag{2}
\]

At each fixed total weight the two by two inverse matrix gives

\[
 m\Delta=I,\quad\rho\iota=I,\quad m\iota=\rho\Delta=0,
 \qquad\Delta m+\iota\rho=I.                        \tag{3}
\]

Thus S=(Delta,iota):H_+ direct_sum H_- -> H_n tensor C^2 is
invertible, with inverse (m,rho)^t. All maps are classical SL2
intertwiners by direct adjacent-basis calculation; no tensor
structure on the quantum head has been replaced by this assertion.

In the coherent metrics ||v_j||^2=binom(n,j), Delta is an isometry,
||iota||^2=N/(N-1) and ||rho||^2=(N-1)/N. Rescaling the lower
inclusion by sqrt((N-1)/N) makes S unitary. These Clebsch changes
therefore introduce no exponential metric cost.

## 2. Exact multiplicative defect and its rank

For every head matrix C set

\[
 \mathbf M(C)=S^{-1}(C\otimes I_2)S
       =\begin{pmatrix}A(C)&B(C)\\C_-(C)&D_-(C)\end{pmatrix}. \tag{4}
\]

This is an exact unital algebra homomorphism. Its upper block is
precisely the full degree elevation already proved:

\[
 A(C)=m(C\otimes I)\Delta=\mathcal E_N(C).
\]

Its other blocks are explicit. In the original matrix indices,

\[
 B(C)_{i,k}=\frac{(N-i)(k+1)C_{i,k+1}
                         -i(N-1-k)C_{i-1,k}}{N(N-1)},
\]
\[
 C_-(C)_{k,j}=\frac{N-1}{N}(C_{k+1,j}-C_{k,j-1}),
\]
\[
 D_-(C)_{a,k}=\frac{(k+1)C_{a+1,k+1}+(N-1-k)C_{a,k}}N. \tag{5}
\]

Every omitted old entry is zero. Multiplication of (4) gives the
EXACT defect, including its order:

\[
 \boxed{\ \mathcal E_N(CD)-\mathcal E_N(C)\mathcal E_N(D)
                  =B(C)C_-(D)
 =m(C\otimes I)(I-\Delta m)(D\otimes I)\Delta.\ }    \tag{6}
\]

Its rank is at most N-1. The lower space is genuinely needed:
the condition C_-(C)=0 in (5) forces C to be scalar. The first
and last column conditions kill the off-diagonals, and the
interior recurrence makes every diagonal entry equal.

This per-strand memory dimension is minimal in the following
precise sense. Any unital representation of Mat_N in End(W) has
dimension(W) divisible by N, as the N diagonal matrix units have
isomorphic images. Since the upper space has dimension N+1,
the smallest such W has dimension 2N; its complement has dimension
at least N-1. Equations (1)--(4) attain that bound. This does not
assert minimality among arbitrary non-tensor chain models.

## 3. Arbitrary ordered words and full source transport

For every ordered word C_m...C_1, the upper block is EXACTLY

\[
 \mathcal E_N(C_m\cdots C_1)
 =\sum_{\epsilon_1,\ldots,\epsilon_{m-1}\in\{+,-\}}
 M_{+,\epsilon_{m-1}}(C_m)\cdots M_{\epsilon_1,+}(C_1). \tag{7}
\]

Only one term keeps the upper channel at every stage. Every other
term is an actual lower excursion. The memory dimension is fixed
independently of word length. On several head legs tensor these
two-channel splittings and retain the resulting channel list at
each internal contraction.

The base upper source psi_+=sum_j V_j and uniform co-source
phi_+(V_j)=1/(N+1) satisfy, for EVERY head matrix C,

\[
 \phi_+m(C\otimes I)\Delta\psi_+=\Phi_{\mathrm{head}}(C). \tag{8}
\]

This is exactly the uniform-average preservation in the
[full degree-elevation theorem](degree_elevation_actual_head_ward_map.md),
not an assumption about a chosen knot. Thus upper exterior sources
and the FULL internal memory word give the original cut functional.
Upper exterior sources do not authorize dropping the internal
lower summands in (7).

### Every physical clock and Green moment retains one auxiliary bit

Let J_head v_j=jv_j and let A_aux=I tensor |u_1><u_1|. The total
Clebsch index is J_total=J_head+A_aux, whose two blocks are
J_N and J_(N-2)+1. Since these commuting operators are retained,

\[
 \mathbf M(J_{\mathrm{head}})=\mathcal J_{\mathrm{total}}-\mathcal A,
 \quad\mathcal A=S^{-1}A_{\mathrm{aux}}S,\quad\mathcal A^2=\mathcal A,
\]
\[
 \mathbf M(w^{J_{\mathrm{head}}})
   =w^{\mathcal J_{\mathrm{total}}}
                          [I+(w^{-1}-1)\mathcal A]. \tag{8a}
\]

For any polynomial P, its exact moment is P(J_total-A), not
P(J_total). The same equality holds for retained Laurent clocks
and marked function evaluations. In the upper corner it gives

\[
 \mathcal E_N(w^JC)=w^{J_N}
       [\mathcal E_N(C)+(w^{-1}-1)\mathcal E_{1,N}(C)],
 \qquad (\mathcal E_{1,N}C)_{ij}=\frac iN C_{i-1,j-1}. \tag{8b}
\]

Thus whole clock covariance under conjugation was not a license
to transport a one-sided clock or Green moment without its offset.
Equations (8a)--(8b) keep that offset and its off-diagonal channel
pieces exactly. The full D/B gauge below commutes with the total
index and conjugates A to B A B^(-1), so the identities survive
with every whole source unit.

Now keep the actual WHOLE head gauge D(q) and actual upper Fr
gauge B_+(q) of that theorem. Choose a specified regular lower
gauge B_-(q), for instance the identity, and let
mathcal B=diag(B_+,B_-). Define

\[
 \mathbf T_q(C)=\mathcal B S^{-1}
                 (DCD^{-1}\otimes I)S\mathcal B^{-1}. \tag{9}
\]

Its upper block is the actual cut map T_s(C), and (9) remains
unital and multiplicative. No whole q-factorial or source unit
has been replaced by a numerical root value. Put

\[
 \mathcal G_q=\mathcal B S^{-1}(D\otimes I)S.
\]

The EXACT source and dual for the original head cut are

\[
 \Psi_q=\mathcal G_q(\psi_+,0)^t,\qquad
 \Lambda_q=(\phi_+,0)\mathcal G_q^{-1}.              \tag{10}
\]

They pair to one and satisfy Lambda_q T_q(C_m)...T_q(C_1)Psi_q
=Phi_head(C_m...C_1). Their lower components generally do not
vanish after D; they must be retained, including their normal
derivatives. The tame Clebsch bound does not imply a tame bound
for D, whose full marked phase/lattice remains separate.

There is also a literal coupon/trace version. Send every original
matrix g,D_mark,e through the algebra homomorphism, retaining
gD_mark=e and all their other products. Its represented e has
rank two, and the normalized auxiliary trace is 1/2:

\[
 \Phi_{\mathrm{head}}(C)=\tfrac12\operatorname{Tr}
                      [\mathbf M(e)\mathbf M(C)].   \tag{11}
\]

The rank-one pointing of (8) agrees with (11) on the represented
head-word algebra; it is not the claim M(e)=Psi Lambda on arbitrary
extended operators. Use (11) when transporting the literal pivotal
defect coupon. The 1/2, the original 1/N cut normalization, and the
full modified-dimension/peripheral scalar line are distinct and
are all retained. Actual pivots, twists and head projectors are
sent by the same multiplicative representation.

For several legs this is an auxiliary MATRIX-MEMORY extension:
represent the original endomorphism on all old head factors and
put the ancillary identities in fixed tensor slots before the
Clebsch change. A checked head crossing is represented with its
actual head permutation in that endomorphism. We are not asserting
a new ribbon functor or choosing an unmentioned ancillary braid
cap. If ancillary slots are instead made to follow braid strands,
their permutation and every resulting cap/trace normalization
must also be included explicitly.

## 4. The actual crossing leaks into the lower channel at every level

Use the original integral N-color un-checked R with n=N-1,
including its full chosen half-Cartan character

\[
 R=q^{H\otimes H/2}
       \sum_{k=0}^{n}q^{k(k-1)/2}\rho^k[k]!\,
                                      E^{(k)}\otimes F^{(k)}.
\]

Lift it with ancillary identities and apply the two Clebsch splittings.
Its upper-to-lower matrix entry is exactly

\[
 V_1\otimes V_0\longmapsto w_0\otimes V_0:
 \qquad\frac{N-1}{N}q^{n^2/2}(q^{-n}-1).           \tag{12}
\]

For this output the second total Clebsch label is zero, so only
transfer k=0 contributes. The two first-leg input components of
Delta V_1 have Cartan factors q^((n-2)n/2) and q^(n^2/2), and
rho takes their difference with coefficient (N-1)/N. This proves
(12). At q_N, q_N^(-n)!=1, so it is nonzero at EVERY N>=2.
The common half-character has not been canceled or reset.

More generally, if an operator R on the old first leg and any
other head space preserved the upper channel, (5) applied to
each other-leg matrix coefficient would force R=I tensor T.
The nontrivial actual Cartan already excludes that possibility.
Thus this is a uniform structural obstruction, not a knot example.

## 5. A uniform inverse-crossing test measures the omitted excursion

Let A_R be the upper/upper block of the lifted R, and A_(R^-1)
the corresponding block of its ACTUAL inverse. The full lifted
word is identity, but their upper-only product is not. On the
diagonal entry V_j tensor V_0 -> V_j tensor V_0, one gets EXACTLY

\[
 [A_{R^{-1}}A_R]_{j,0;j,0}
  =1+\frac{j(N-j)}{N^2}(q^n+q^{-n}-2).             \tag{13}
\]

Indeed all nonzero transfers raise the second total Clebsch label,
so cannot occur in this entry of either factor. The remaining
Cartan diagonal on the first old head is d_i=d_0 a^i with
a=q^(-n). Degree elevation at j averages d_j,d_(j-1) with weights
(N-j)/N,j/N. Multiplying the corresponding inverse average proves
(13). The common half-Cartan factors cancel only as dictated by
the exact inverse word.

At the marked root this becomes

\[
 1-\frac{4j(N-j)}{N^2}\cos^2\!\frac{\pi}{2N}.       \tag{14}
\]

For even N and the binomial center j=N/2 its value is
sin^2(pi/(2N)), rather than one. The lower excursion restores the
entire missing term in (14). The defect is not a scalar peripheral
factor: it vanishes at j=0,N and depends on j in the interior.
It need not be small in the macroscopic source region.

Equations (12)--(14) do not determine the Ward/cohomology class of
the excursions after a full knot contraction. They prove that raw
R invariance or an inverse-crossing identity cannot be obtained
by discarding this channel. Any cohomological cancellation must
be a further actual current/source map.

## 6. Relation to the existing source complexes

This strictification is the explicit Clebsch representation behind
the nonmultiplicative degree-elevation map. It is different from
the tail constraints in
[the constrained Verma word](constrained_verma_word_source_extension.md),
which repair original finite-head compression before a Rees limit.
Those constraints and every original internal projector can be
transported through (9); the present lower Clebsch channel does
not replace them. The ordered weighted current and endpoint maps
of [the relative word transport](relative_word_green_transport.md)
likewise act on the FULL block word, not just its upper corner.

The global Fr P1/Cech source realizes each finite block operator
with its dual endpoints. A highest-spin quotient current may
subsequently isolate a Bockstein wall line; it is not presumed
R-invariant or acyclic here. No Gaussian, geometric-source
survival or volume limit is inferred from the finite dilation.
The complementary current calculation is recorded in
[the degree-elevation Bockstein wall](degree_elevation_complement_bockstein_wall.md);
its Borel current quotient is not a license to drop the actual
R excursions in (12)--(14).

The upper Sym^N coordinates can be adapted by B_+ to the actual
high-color divided F string for the CUT K/F map. The full memory
R above is still the literal OLD head R with an auxiliary identity,
not automatically the existing high-integral-color R on Fr tensor
head. Their whole normal intertwiner remains an additional theorem.

Nor can an off-image highest-spin source be changed to the uniform
interval row. On E_(N,0)=f^N/N!, the uniform Fr average is 1/(N+1),
whereas the actual binomial coherent row is 2^(-N). The ratio
2^N/(N+1) is retained. With the original coupled source it is
2^(-N)H_(0,0) on E_(N,0) tensor H. This operator is outside the
degree-elevation image, whose extreme corners vanish. The exact
cut homotopy on that image does not justify replacing the original
pointing on a wall generated by lower-channel excursions.

[Exact actual-word and universal crossing audit](../experiments/audit_clebsch_memory_and_actual_r_excursions.py).
The [results](../experiments/clebsch_memory_and_actual_r_excursions_results.json)
pass seven whole-word/source cases N=2,...,8 and five complete
actual R/inverse families N=2,...,6. They check the full memory
identity, multiplicative defect, actual D/B source units, marked
pivot/defect relation and auxiliary trace factor, exact clock/moment
offset, every asserted leakage, and 25 inverse-pair diagonal entries.
