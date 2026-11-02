# Concrete analytic transfer, graph energy and variational estimates

This optional Lean package realizes the elementary analytic interfaces of
[VolumeTransfer](../formal/VolumeLogic/VolumeTransfer.lean) using Mathlib's
complex numbers, complex modulus and real logarithm. It depends on the
existing Std-only package by the relative path `../formal`; its sources are
not copied. The ordinary Std-only check does not need this package or Mathlib.
The package also proves the real finite quadratic-form implication used in
the circle-pattern Hessian argument, the one-variable calculus behind
shared-weight flattening, coercivity from a positive finite transport table,
uniqueness from actual graph-valued second derivatives, and invertibility
of the actual graph Laplacian after grounding one coordinate. The triangle
load module derives the local derivative and its assembled graph energy
from the exponential, square-root and arctangent formulas themselves.
The triangle-potential module then proves that these loads are the
gradient of the literal integral-entropy supremum, including singleton rows.
The triangle-minimizer module combines those actual derivatives with
proved local bounds, continuity and finite corner-table identities to
obtain a unique grounded minimum from the supported table and row paths.
The triangle-balance module then derives the concrete free-vertex Euler
equations and proves that their grounded solution is unique.

## What is proved

[RealTransfer.lean](RealTransfer.lean) contains two definitions and twenty-two
theorems, all in the namespace `VolumeLogic.RealModel`:

- `complexMagnitude` is the actual complex norm. Its nonnegativity,
  definiteness, multiplicativity and triangle inequality are proved.
- `realLogScale.value N x` is `Real.log x / (N : ℝ)`. Its monotonicity,
  product law and fixed-constant limit are proved.
- `eventually_physical_iff` and `real_rateLimit_iff` identify the existing
  epsilon-based level interface with ordinary `Filter.Tendsto` at `atTop`.
  Here a physical level is an integer `N ≥ 2`; removing the initial levels
  does not introduce a prime-level or parity restriction.
- `complex_hasRate_iff` and `complex_hasUpperRate_iff` give the corresponding
  concrete logarithmic rate statements. Eventual nonvanishing is kept
  separate from the totalized value of `Real.log 0`.
- The packet lemmas prove zero rate for unit phases, a complex amplitude
  tending to a nonzero limit, and any fixed real power of the level. They
  prove the rate of `exp(N S_N)` from the convergence of the finite complex
  actions `S_N`.

The main entry points are:

| Theorem | Conclusion and explicit inputs |
| --- | --- |
| `complex_invariant_rate_transfer` | From the exact eventual identity `K_N = u_N (G_N + E_N)`, zero normalization rate, leading rate `a`, and a strictly smaller upper rate for the **whole** remainder `E_N`, derive eventual `K_N ≠ 0` and its rate `a`. |
| `complex_volume_transfer` | From the same inputs and `2πa = volume`, derive the ordinary real limit `(2π/N) log ‖K_N‖ → volume`. |
| `complex_packet_volume_transfer` | Derive the leading rate from the actual packet `N^k a_N exp(N S_N)`, where `k` is any fixed real number, `a_N → a ≠ 0` and `S_N → A`. Restore a unit framing character, use a strict whole-remainder upper rate below `Re A`, and conclude the volume limit from `2π Re A = volume`. |
| `complex_residue_packet_volume_transfer` | Allow separate nonzero amplitude limits and complex action limits on every residue class modulo a fixed positive integer `p`. If all limiting actions have the same real part, derive the full integer-level volume limit under the same exact-source, whole-remainder and geometry hypotheses. |
| `complex_parity_packet_volume_transfer` | Give the preceding conclusion directly from the actual subsequences `a_(2n)`, `a_(2n+1)`, `S_(2n)` and `S_(2n+1)`, with independently specified limits. |

Thus the last theorem proves the packet's logarithmic rate rather than
assuming it. The power `k` includes half-integral Gaussian powers. A relative
correction tending to one can remain inside `a_N`. The more general
`complex_volume_transfer` permits a normalization of rate zero even when its
modulus is not one.

The original `complex_packet_volume_transfer` assumes a **common all-level**
nonzero amplitude limit. The residue and parity theorems remove that
requirement without changing the original theorem's API. They use the same
actual sequence on every class. In particular, when `N = p*n+r`, the rate is
`log ‖K_(p*n+r)‖ / (p*n+r)`, not a rate with denominator `n`.

The new assembly proves three steps. First, finitely many residue thresholds
combine into one threshold for all integers, using quotient and remainder.
Second, convergence of each amplitude to its own nonzero value implies
zero logarithmic rate on that class. Third, taking real parts turns the
possibly different complex action limits into one common real limit, so
the exponential packet has that rate at every sufficiently large level.
The explicit even/odd corollary needs both parity hypotheses. The period
`p`, real power `k`, diagram and filling data are fixed before the limit.
The unit carrier `u_N` may vary arbitrarily with the level; no convergence
or finite-period assumption is imposed on it.

This is an application extension, not a correction to the written Morse
period theorem. [Appendix O](../manuscript/sections/O-morse-geometric-contribution.tex),
equations `mca:eq-3` and `mca:eq-4`, asserts a common finite-action and nonzero
amplitude limit after its displayed level factors and `q` phase are removed;
equation `mcg:eq-36` records the parity-sign cancellation. Likewise,
[the recursive filling chapter](../manuscript/sections/08-filling.tex),
equations `eq:final-asymptotic` and `eq:final-amplitude`, isolates the explicit
unit factors and nonzero coefficient. Those exact common-limit statements
can already use the original concrete theorem. Separately normalized
parity packets can instead use the new theorem, provided their stated
convergence hypotheses and common real rate are proved.

These are conditional analytic transfer theorems, not a construction of the
Kashaev or ADO invariant. The exact original source identity, convergence of
the nonzero packet coefficient and finite action, a strict bound for the
entire complementary remainder, and the geometric action-volume equality
remain explicit application inputs. This package does not formalize the
saddle analysis or hyperbolic gluing that supplies those inputs.

## Weighted graph energy

[WeightedGraph.lean](WeightedGraph.lean) contains seven definitions and
nineteen theorems in `VolumeLogic.WeightedGraph`. An edge label `e` has
endpoints `src e` and `dst e`, a real weight `w e`, and a real vertex
function `f`. The constructed energy is

\[
E(f)=\sum_e w_e\bigl(f(\operatorname{src}e)-f(\operatorname{dst}e)\bigr)^2.
\]

Edge labels are retained, so parallel edges are allowed. A loop contributes
zero. Connectivity means that every pair of vertices is joined by a finite
path of actual **positive-weight** edges, expressed by the reflexive
transitive closure of the endpoint relation. It is not an assumption that
the energy already has constant kernel. Ordinary graph connectivity and
strictly positive weights imply this path condition.

The main implications are:

| Theorem | Conclusion and explicit inputs |
| --- | --- |
| `energy_nonneg` | Nonnegative edge weights imply nonnegative energy. |
| `energy_eq_zero_iff` | Under the same hypothesis, energy is zero exactly when `f` agrees across every positive-weight edge. Zero-weight edges impose no equality. |
| `equal_of_positive_path` | Endpoint equality propagates by induction on an actual finite path. |
| `energy_eq_zero_iff_constant` | A connected positive support has exactly the constant functions as its zero-energy functions. |
| `grounded_energy_eq_zero_iff` and `grounded_energy_pos` | If one specified vertex has value zero, then zero energy forces `f = 0`; every nonzero grounded function has strictly positive energy. |
| `laplacian_form` and `laplacian_quadratic` | The explicit matrix `L = BᵀWB`, formed from signed edge incidences `B`, has bilinear form equal to the edge sum, and quadratic form equal to `E(f)`. |
| `grounded_laplacian_pos` | The explicit Laplacian quadratic form is strictly positive on every nonzero grounded function. |

The supporting theorems prove symmetry and linearity of the edge form and
invariance of energy under addition of a constant. The matrix identities
require a finite vertex set as well as a finite edge set; they are proved
by expanding the finite sums.

For the intended application, [the marked circle-pattern proof](../notes/actual_marked_deformed_circle_pattern.md)
identifies its Hessian with this energy. Its vertices are ordinary faces,
and an edge is a triangle together with an unordered pair of its ordinary
corners. If those corners have positive curvatures `w_i,w_j`, their weight is

\[
\kappa^t_{ij}=\frac{w_iw_j}{2\pi D_t(w_i+w_j)},
\qquad
D_t^2=\sum_{\{a,b\}\subset t}w_aw_b,
\]

where the sum is over ordinary corner pairs. A triangle with only one
ordinary corner contributes no edge. Different triangles may supply
parallel edges. The `TriangleLoads` and `TrianglePotential` modules below now prove
this differentiation for the displayed entropy-envelope potential and
positivity of its conductances. Identifying that potential and its
connected ordinary-face graph in the geometric application remains a
**written input**. The actual finite real quadratic-form implication
from those inputs is proved here. This module
does not formalize circle-pattern existence, the rest of the geometric
Jacobian argument, or an implicit function theorem.

## Calculus of shared-weight flattening

[Flattening.lean](Flattening.lean) contains one definition and nine theorems
in `VolumeLogic.Flattening`. It supplies the calculus used in
[Appendix P, Sections 2–4](../manuscript/sections/P-weak-balance.tex), rather
than assuming the cost and gain inequalities as scalar premises.

Let `g`, `dg`, and `ddg` be actual real functions. On the interval `[0,t]`,
the hypotheses `HasDerivAt g (dg x) x` and `HasDerivAt dg (ddg x) x`
identify their derivatives. If `t ≥ 0`, `dg 0 = 0`, and
`0 ≤ ddg x ≤ E` throughout that interval, `stationary_quadratic_cost` proves

\[
0\le g(t)-g(0)\le \frac{Et^2}{2}.
\]

Nonnegative second derivative makes `g` convex. The constructed function
`E*x²/2 − g x` also has nonnegative second derivative and is stationary at
zero; its supporting line gives the upper estimate. Thus the theorem uses
real differentiation and convexity, without an assumed Taylor remainder.
The endpoint derivative hypotheses are slightly stronger than necessary,
but any `C²` application on a neighborhood of the interval satisfies them;
continuity of the second derivative is not needed by the proof.

The definition `weightPath P q t = P (fun i => (1-t)*q i)` varies every
ordinary logarithmic weight along the same path. Its index set excludes the
protected zero coordinates. `weight_path_cost` applies the preceding
estimate to this actual composition, with its directional derivatives
explicitly identified by the hypotheses.

For an actual convex real function `Q` on `[0,1]`, differentiable at `1`
with derivative `dQ`, `convex_support_at_one` proves

\[
Q(\beta)\ge \beta Q(1)+(1-\beta)\bigl(Q(1)-dQ\bigr),
\qquad 0\le\beta\le1.
\]

This is the supporting line at `1`. The application identifies the intercept
`Q(1)-dQ` with triangle entropy. The theorem proves the inequality from
convexity and differentiability; it does not assume an entropy gain.

The last three theorems retain the actual maximum of the two one-sided
branches. Write `Qk` for the retained triangle potential, `Qo` for the
overloaded triangle potential, `z` for the overloaded corner's complete
logarithmic weight, and `β=1-t`. The local loss is

\[
L(t)=Q_k(\beta)+Q_o(\beta)
-\max\{\beta z,\ Q_k(\beta)+\beta z/2\}.
\]

From the convex supporting lines, nonnegative retained entropy and the
pure-corner inequality `Qo(1) ≥ z/2`, `side_loss_from_convexity` derives

\[
L(t)\ge th-(1-t)\delta,\qquad
h=Q_o(1)-Q_o'(1),\qquad
\delta=\max\{0,z-Q_k(1)-Q_o(1)\}.
\]

Here the defect `δ` is constructed from the complete values; the loss bound
is proved for both branches of the maximum. `flattening_sector_gap` combines
it with the derived quadratic cost and an actual finite list of other
nonnegative losses. If `Et²/2 < th-(1-t)δ`, the resulting sector rate is
strictly below `g(0)`. In `weak_balance_sector_gap`, the complete balance
inequality gives `δ=0`; `0<t≤1`, `h>0` and `tE≤h` discharge the strict
margin using the existing Std-only `strict_weak_balance_gain` theorem.

The remaining written inputs are the geometric differentiation identifying
`P`, `Qk` and `Qo`, the stationary complete point, the directional Hessian
bound `E`, the entropy and pure-corner identities, and the identification of
these expressions with the actual shared source envelopes. This module does
not formalize those geometric formulas, coefficient asymptotics, or the
invariant's volume limit. It proves the intervening real-calculus and
finite-sector implications.

## Coercivity from supported transport

[TransportCoercivity.lean](TransportCoercivity.lean) contains seven
definitions and sixteen theorems in `VolumeLogic.TransportCoercivity`.
It proves the finite-dimensional coercivity argument used in
[the triangular-insertion paper, Sections 2–4](../papers/triangular-insertion/main.tex).
The corner table and its graph are actual finite data, rather than an assumed
constant-kernel property or an assumed coercivity bound.

Let `T` be a finite set of rows, `V` a finite set of vertices, and `S t` a
nonempty finite set of supported vertices in row `t`. A real table entry
`α t i` is strictly positive whenever `i ∈ S t`; entries outside that
support are ignored. The definitions construct the row supply and column
demand from the same table:

\[
m_t=\sum_{i\in S_t}\alpha_{ti},\qquad
d_i=\sum_{t:\,i\in S_t}\alpha_{ti}.
\]

For a real vertex function `h : V → ℝ`, the actual recession function is

\[
\mathcal R(h)=\sum_t m_t\max_{i\in S_t}h_i-\sum_i d_i h_i
=\sum_t\sum_{i\in S_t}\alpha_{ti}
\left(\max_{j\in S_t}h_j-h_i\right).
\]

The last equality is proved by finite summation. Nonnegativity follows
term by term. Because the supported entries are positive, equality holds
exactly when every supported value equals its row maximum. A graph step
joins two vertices belonging to one row, and `connected` requires an
actual finite path of such steps between every pair of vertices. Induction
on that path propagates equality. After fixing one vertex `root` and
requiring `h root = 0`, every nonzero `h` therefore has positive recession.

`grounded_recession_coercive` proves the stronger uniform conclusion

\[
\exists c>0\quad\forall h\text{ with }h_{\rm root}=0,
\qquad \mathcal R(h)\ge c\lVert h\rVert.
\]

Here the norm is the finite function space's supremum norm. Finite maxima
make `𝓡` continuous, and its positive homogeneity is proved directly.
Compactness of the grounded unit sphere supplies `c`; scaling then gives
the bound for every grounded direction. The compactness lemma explicitly
allows an empty sphere, as happens with a single vertex: any positive
constant works because the only grounded function is zero. Empty row
supports are excluded by hypothesis. No quantitative value of `c`, or
uniformity over different transport tables, is asserted.

For actual functions `Q t : (V → ℝ) → ℝ` and fixed real row constants
`C t`, the definition `potential` is

\[
\mathcal J(h)=\sum_t Q_t(h)-\sum_i d_i h_i.
\]

The explicit local hypotheses

\[
Q_t(h)\ge m_t\max_{i\in S_t}h_i-C_t
\]

imply `𝓙(h) ≥ 𝓡(h) − Σ_t C_t`. Thus
`grounded_potential_coercive` derives
`𝓙(h) ≥ c ‖h‖ − Σ_t C_t`. Every grounded sublevel is bounded; if each
`Q t` is continuous, it is compact. `exists_grounded_minimizer` obtains an
actual minimum from the nonempty sublevel through zero. A minimizer is
not an input, and convexity is not needed for this existence statement.
This module alone does not claim uniqueness or differentiability of the
minimum. The next module derives uniqueness under explicit derivative and
connected graph hypotheses.

The application must still construct the strictly positive supported table
from the disk's Hall inequalities, identify its prescribed margins (row
supply `1/2` and the required face demands), and verify the connected
grounded support. It must also identify the geometric potential with the
displayed `𝓙`. For a general row function Q, its local vertex bounds remain
hypotheses; `TriangleMinimizer` below proves them for the actual supported
triangle envelope. Fixed boundary logarithms may enter the constants `C_t`; any identification of fixed boundary
directions with the grounded coordinates is part of that written
application. For a disk with three positive fixed boundary weights, pool
the boundary destinations into the single grounded root, aggregating the
table entries at repeated boundary corners and retaining their prescribed
logarithms as row offsets. Grounding just one of three separately retained
boundary vertices would not express that fixed-boundary problem. The
two-zero supported limit already has the form `V = I ∪ {b}`, grounded at
`b`. The Lean result proves the subsequent finite-sum, path,
compactness and minimization implications without assuming their conclusion.

## Strict convexity and the unique grounded minimum

[GroundedConvexity.lean](GroundedConvexity.lean) contains three definitions
and eight theorems in `VolumeLogic.GroundedConvexity`. It joins the preceding
existence proof to the Hessian argument in
[the triangular-insertion paper, Sections 2–4](../papers/triangular-insertion/main.tex).
Neither strict convexity nor uniqueness is supplied as a premise.

Let `P : (V → ℝ) → ℝ` be the actual potential, and fix a vertex `root`.
The grounded set consists of all vertex functions `x` with `x root = 0`.
For grounded endpoints `x,y`, the module constructs

\[
p_{x,y}(t)=(1-t)x+ty,\qquad g_{x,y}(t)=P(p_{x,y}(t)).
\]

An explicit real function `dg x y` supplies the first derivative:
`HasDerivAt (segmentValue P x y) (dg x y t) t` on `0 ≤ t ≤ 1`.
The second derivative is identified, for `0 < t < 1`, with

\[
\frac{d}{dt}dg_{x,y}(t)
=\sum_{e\in E}w_e(p_{x,y}(t))
\bigl((y-x)_{\operatorname{src}e}-(y-x)_{\operatorname{dst}e}\bigr)^2.
\]

Here `E` is a finite set of actual edge labels with endpoints `src e` and
`dst e`. At each grounded point, the weights must be nonnegative and the
positive-weight edges must connect all vertices by finite paths. Parallel
edges, loops and zero weights are allowed. The positive support may change
with the point; no uniform lower eigenvalue bound is assumed.

If `x ≠ y`, then `y-x` is a nonzero grounded function. The proved
`WeightedGraph.grounded_energy_pos` therefore makes the displayed second
derivative strictly positive. The one-variable calculus theorem
`strictConvexOn_Icc_of_second_pos` uses these actual derivatives and endpoint
continuity to prove strict convexity on `[0,1]`. Consequently,
`segment_strict_jensen` proves

\[
P((1-t)x+ty)<(1-t)P(x)+tP(y)\qquad(0<t<1).
\]

`strictConvexOn_grounded` assembles all grounded segments into Mathlib's
`StrictConvexOn` statement. `grounded_minimizer_eq` then proves that two
grounded global minima coincide. Finally,
`exists_unique_grounded_minimizer` applies these results to the **same**
constructed potential `TransportCoercivity.potential S α Q`. The positive
transport table, connected row support, local vertex bounds and continuity
give existence; the actual segment derivatives and connected conductance
graph give uniqueness. The transport graph and Hessian graph need not have
the same edge presentation, so both connectivity assumptions remain explicit.
The one-vertex case is included: its grounded space is a singleton and no
distinct segment must be considered.

These derivative hypotheses are satisfied by a `C²` potential with the
stated Hessian identity; the proof needs only the indicated derivatives,
not continuity of the Hessian. For the explicit triangle entropy-envelope sum, `TrianglePotential`
below now supplies the derivatives, including singleton rows. Identifying
the geometric potential and its positive connected conductance support,
and Hall feasibility of the transport table, remain written inputs. In the
fixed-boundary disk application, the boundary pool and prescribed offsets
are those described above; the Hessian must be that of the resulting
potential in the free interior coordinates. The module does not prove
smooth dependence of the minimizer, the implicit function theorem's
application, circle-pattern development or a volume identity.

## Inverting the grounded graph Laplacian

[GroundedLaplacian.lean](GroundedLaplacian.lean) contains four definitions
and eighteen theorems in `VolumeLogic.GroundedLaplacian`. It proves the
finite nondegeneracy step after a Hessian has been identified with the
graph form. Positive definiteness, injectivity and invertibility are
conclusions, not additional hypotheses.

Let `V` and `E` be finite vertex and edge types. An edge `e` has endpoints
`src e`, `dst e` and real weight `w e`. Fix a vertex `root`. The assumptions
are `0 ≤ w e` for every edge and connectivity by actual finite paths whose
edge weights are strictly positive, as defined in `WeightedGraph.connected`.
Loops, parallel edges and zero weights remain allowed. Put

\[
I=\{v\in V:v\ne\mathrm{root}\},\qquad
B_{ev}=\mathbf 1_{\operatorname{src}e=v}
       -\mathbf 1_{\operatorname{dst}e=v},\qquad
L_{uv}=\sum_e w_e B_{eu}B_{ev}.
\]

The definition `reducedMatrix` is precisely the principal matrix
\(L^\circ=(L_{uv})_{u,v\in I}\), and `reducedOperator` is multiplication by
this matrix. For `f : I → ℝ`, `extend root f` is the vertex function
\(\bar f\) equal to `f` away from the root and zero at the root.
The theorem `reduced_bilinear` proves

\[
\sum_{u\in I} f_u(L^\circ g)_u
=\sum_e w_e(\bar f_{\operatorname{src}e}-\bar f_{\operatorname{dst}e})
             (\bar g_{\operatorname{src}e}-\bar g_{\operatorname{dst}e}).
\]

The self-pairing is therefore exactly the previously constructed graph
energy. If `f ≠ 0`, connected positive support and grounding make that
energy strictly positive. This proves the kernel is zero and the operator
is injective. Finite dimensionality gives surjectivity, after which
`reducedEquiv` constructs a real linear equivalence and hence its inverse.
`reducedMatrix_det_ne_zero` also proves \(\det L^\circ\ne0\).

The two main solvability statements are
`exists_unique_reduced_solution` and `exists_unique_grounded_solution`.
The latter says that for **every** right-hand side `b : V → ℝ` there is a
unique `f : V → ℝ` satisfying

\[
f_{\mathrm{root}}=0,\qquad
\sum_{v\in V}L_{uv}f_v=b_u\quad(u\ne\mathrm{root}).
\]

The root equation is omitted: its value is the reaction to the grounding
condition, so no zero-sum compatibility condition is imposed on `b`.
If the graph has one vertex, `I` is empty, its determinant is one, and the
unique grounded function is zero; the same proofs include this case.

To apply this result to the geometric variational problem, the actual
derivative matrix must still be identified with this reduced Laplacian,
with the displayed nonnegative weights and connected positive support.
For several fixed boundary coordinates, a pooled boundary vertex can be
used only after that identification has been supplied. This module proves
neither a uniform inverse norm bound nor differentiable dependence on
parameters, a nonlinear implicit-function theorem, or geometric development.

## Differentiating the actual triangle loads

[TriangleLoads.lean](TriangleLoads.lean) contains ten definitions and
twenty-four theorems in `VolumeLogic.TriangleLoads`. It proves the
calculus behind equation `mf:hessian` in
[the marked-fillings paper](../papers/marked-fillings/main.tex) and
equations `ti:eq-4`–`ti:eq-5` in
[the triangular-insertion paper](../papers/triangular-insertion/main.tex).
The derivative formula is a conclusion, not a supplied Hessian identity.

For corners indexed by `Fin 3`, fix nonnegative real coefficients
\(a_i\) and logarithmic coordinates \(q_i\). The definitions are

\[
w_i=a_i e^{q_i},\qquad
S=w_0w_1+w_1w_2+w_2w_0,\qquad D=\sqrt S,\qquad
\alpha_i=\frac1\pi\arctan\frac{w_i}{D}.
\]

The load theorem assumes \(S>0\). This covers both three positive
corners and two positive corners with one zero coefficient.
`radicand_pos_of_positive_pair` proves positivity of \(S\) from any two
distinct positive weights and nonnegativity of the others.
`pair_sum_pos` proves \(w_i+w_j>0\) for distinct corners under the
load theorem's hypotheses. Thus the off-diagonal denominators below
are nonzero even at a zero corner. No limiting argument or division by
that corner's weight is used.

For every real direction \(h\), `load_hasDerivAt` proves the derivative
of the **actual** function \(t\mapsto\alpha_i(a,q+t h)\) at zero:

\[
\alpha_i'(0)=\sum_j\kappa_{ij}(h_i-h_j),\qquad
\kappa_{ij}=\frac{w_iw_j}{2\pi D(w_i+w_j)}\quad(i\ne j).
\]

The proof first differentiates the exponential weights and \(D\), then
uses Mathlib's quotient and arctangent chain rules. The algebraic step
uses the exact identity
\(D^2+w_i^2=(w_i+w_j)(w_i+w_k)\) for the three distinct corners.
`load_off_diagonal_hasDerivAt` specializes to the coordinate direction
\(h=e_j\), giving \(\partial_{q_j}\alpha_i=-\kappa_{ij}\) for
\(i\ne j\). A common shift has zero Jacobian action. Conductances are
nonnegative, and they are strictly positive when both endpoint weights
are positive. Diagonal values of the helper `conductance` do not matter:
they multiply \(h_i-h_i=0\), and are never edges in the graph form.

The graph has three explicit edge labels, for the pairs \(01,02,12\).
`jacobian_pairing` identifies its full bilinear form with
\(\sum_i h_i(Jk)_i\); `jacobian_energy` consequently gives

\[
\sum_i h_i\alpha_i'(0)
=\kappa_{01}(h_0-h_1)^2+
  \kappa_{02}(h_0-h_2)^2+
  \kappa_{12}(h_1-h_2)^2.
\]

`load_pairing_hasDerivAt` proves this equality as the derivative of
\(\sum_i h_i\alpha_i(a,q+t h)\), so the graph interpretation is tied
to an actual function. `sum_load_pairing_hasDerivAt` then treats any
finite collection of triangles with a corner map into one common vertex
type. It differentiates the sum using the **same** vertex functions
\(q,h\) at every occurrence. Its graph edge type is the product of the
triangle labels and the three pair labels. Parallel edges and coincident
corner labels are retained, and every unordered local pair is counted
once. There is no choice of independent coordinates for each occurrence
of a shared face.

A zero corner has identically zero load. A singleton is handled separately
by `singletonLoad`: its sole supported corner has the constant load
\(1/2\), with zero derivative. This is not an evaluation of the
arctangent formula at \(D=0\). All-zero triangles are not part of the
positive-radicand theorem. Singleton rows add no Hessian energy.

This module alone does not identify these \(\alpha_i\) with a
potential gradient. The next module proves that identification from the
actual integral entropy and supported constrained maximum. With the
actual supported incidence graph identified, the derivative above is the
displayed Hessian energy. Existing `WeightedGraph` and
`GroundedLaplacian` results apply when positive-weight paths connect the
actual supported vertex space and the appropriate coordinate is grounded.
Zero-weight corners do not create positive edges; inactive coordinates
or pooled boundary data must be treated according to the application.
Neither graph connectivity, packing existence nor nonlinear deformation
is inferred solely from the local formula.

## The integral entropy and its variational gradient

[TrianglePotential.lean](TrianglePotential.lean) contains eight definitions
and forty-one theorems in `VolumeLogic.TrianglePotential`. It identifies
the actual supported triangle envelope in equation `pc:Q` of
[the planar-certificates paper](../papers/planar-certificates/main.tex)
and equations `ti:eq-1`, `ti:eq-4`–`ti:eq-5` of
[the triangular-insertion paper](../papers/triangular-insertion/main.tex).
The potential is defined by the integral and supremum themselves; its
gradient is not an assumption or a definition.

The first three definitions are

\[
\Lambda(x)=-\int_0^x\log|2\sin u|\,du,\qquad
f(t)=\frac{\Lambda(\pi t)+\Lambda(\pi/2-\pi t)}{\pi},\qquad
f'(t)=\log\cos(\pi t)-\log\sin(\pi t)
\quad(0<t<1/2).
\]

Here the integral is Mathlib's actual real interval integral. The proof
uses integrability of the logarithmic sine singularities, the fundamental
theorem of calculus away from those singularities, and the evaluated
log-sine integral on `[0,π/2]`. It derives continuity of `Λ` and `f`,
`f(0)=f(1/2)=0`, the displayed interior derivative, and concavity of `f`
on the closed interval `[0,1/2]`. The supporting-tangent inequality
therefore includes competitors at the endpoints; it does not require an
entropy derivative at either endpoint.

For fixed nonnegative coefficients `a : Fin 3 → ℝ`, put
`w_i = a_i exp(q_i)`. The supported feasible set consists of vectors
`α : Fin 3 → ℝ` satisfying

\[
\alpha_i\ge0,\qquad \sum_i\alpha_i=1/2,\qquad
 a_i=0\Longrightarrow\alpha_i=0.
\]

The actual definition `potential a q` is the supremum of

\[
\sum_i f(\alpha_i)+\sum_{i:a_i>0}\alpha_i(\log a_i+q_i)
\]

over that set. The helper `logWeight` assigns zero at inactive corners,
whose feasible loads are already zero, so no logarithm of a zero weight
is used as a boundary penalty. For positive `a_i`, its value is proved
to be `log w_i`.

When `D²=w_0w_1+w_1w_2+w_2w_0>0`, the proof establishes directly that

\[
\alpha_i^*=\frac1\pi\arctan\frac{w_i}{D},\qquad
\sum_i\alpha_i^*=\frac12,
\qquad
 f'(\alpha_i^*)+\log w_i=\log D\quad(a_i>0).
\]

The arctangent sum is proved for three nonnegative weights with positive
`D²`, including one zero weight. Active loads lie strictly between zero
and one half. Applying the entropy tangent inequality to every active
corner and summing cancels the common multiplier `log D`, because all
competitors have the same total mass. `objective_le_loads` bounds every
feasible objective by the explicit one; `potential_eq_loads` then proves
that the supremum is attained there. This does not rely on a general
envelope differentiation theorem or an assumed optimizer.

Differentiating the resulting explicit value along the actual path
`q+t h` gives

\[
\frac{d}{dt}Q(a,q+t h)
 =\sum_i h_i\alpha_i(a,q+t h).
\]

The terms containing derivatives of the loads cancel because their sum
is zero. `potential_path_hasDerivAt` proves this at every real path
parameter. The conductance Jacobian from `TriangleLoads` consequently
gives the second derivative as the actual graph energy.

A singleton uses the **same** feasible-set and supremum definitions.
If `a_active>0` and every other coefficient vanishes, feasibility forces
its sole load to be one half. The module proves

\[
Q(a,q)=\tfrac12(\log a_{\mathrm{active}}+q_{\mathrm{active}}),\qquad
\frac{d}{dt}Q(a,q+t h)=\tfrac12 h_{\mathrm{active}},\qquad
\frac{d^2}{dt^2}Q(a,q+t h)=0.
\]

It never evaluates `atan(w_i/D)` at `D=0` to produce that convention.
The all-zero case is outside the stated hypotheses.

The definition `summedPotential` retains one common vertex function and
the actual face-demand term:

\[
\mathcal P(q)=\sum_{t\in T}Q(a^t,q\circ c_t)
                   -\sum_{v\in V}\delta_v q_v.
\]

Here `T,V` are finite types, `c_t : Fin 3 → V` is the corner map, and
`δ_v` is the specified demand. The first shared-sum theorems require
positive radicand in every row. The final theorems
`summedPotential_mixed_hasDerivAt` and
`summedPotential_mixed_second_at` allow a fixed partition into those
rows and singleton rows with explicitly supplied active corners. They
prove the actual first derivative, including each singleton's affine
term, and the actual second derivative at **every** point of the path.
Its graph edge type is `T × Fin 3`, retaining the three unordered corner
pairs in each triangle. Nonsingleton weights are the proved conductances;
singleton weights are zero. Repeated shared corners and parallel edges
are preserved. The demand term contributes to the first derivative and
has zero second derivative.

Thus the entropy-gradient identification is now proved for this concrete
potential, including mixed supported rows. To apply `GroundedConvexity`,
write a segment as `q+t h` and supply connectivity of the actual positive
conductance support and the appropriate grounding. The next module derives
that conductance connectivity from the actual row paths. The derivative
identity itself no longer needs to be supplied for this potential. The geometric
or source interpretation of `Q`, the incidence maps, fixed-boundary
pooling and offsets, Hall transport feasibility, and graph connectivity
remain written application inputs. No continuity theorem as the fixed
coefficients `a_i` change support is claimed; the one-zero and singleton
cases are proved directly at their own fixed supports. Packing existence,
nonlinear deformation and the volume identity are not conclusions of
this module.

## The actual supported triangle minimum

[TriangleMinimizer.lean](TriangleMinimizer.lean) contains six definitions and
thirty-two theorems in `VolumeLogic.TriangleMinimizer`. It instantiates the
coercivity and uniqueness results with the **same** `TrianglePotential`
supremum, rather than assuming its lower bound, continuity, gradient or
Hessian. Its two main entry points are
`exists_unique_triangle_minimizer` and
`exists_unique_prescribed_minimizer`.

Let `T,V` be finite triangle and vertex types, `root : V` the grounded
vertex, and `c : T → Fin 3 → V` the corner map. The fixed corner
coefficients `a_ti` are nonnegative. An actual table `β_ti` must satisfy

\[
\beta_{ti}>0\quad(a_{ti}>0),\qquad
\beta_{ti}=0\quad(a_{ti}=0),\qquad
\sum_{i=0}^2\beta_{ti}=\frac12.
\]

In the Lean statement the zero condition is written for every corner
without a strictly positive coefficient; nonnegativity of `a` makes these
the same inactive corners. These conditions themselves imply that each
row has nonempty support. Define

\[
S_t=\{c_t(i):a_{ti}>0\},\quad
\alpha_{tv}=\sum_{i:c_t(i)=v}\beta_{ti},\quad
d_v=\sum_t\alpha_{tv}.
\]

The proofs retain repeated corners. `aggregate_rowMass` gives the exact
half-row masses, `aggregate_demand` identifies the actual column demands,
and `transport_potential_eq` identifies the constructed transport potential
with `summedPotential c a d`. Positive entries on each set `S_t` follow
from the original supported corner table; demands are not substituted by
an unrelated vector.

The local lower bound is proved by putting the full feasible mass `1/2`
at any active corner. Its entropy is zero, so

\[
Q(a,q)\ge\frac{\log a_i+q_i}{2}\qquad(a_i>0).
\]

The explicit row constant

\[
C_t=\frac12\sum_{i:a_{ti}>0}|\log a_{ti}|
\]

therefore gives `Q_t(q) ≥ (1/2) max_(v∈S_t) q_v − C_t` for every q.
This is the precise lower-bound input of `TransportCoercivity`; it includes
fixed boundary offsets and needs no uniform bound on their magnitudes.
The module also proves the quantitative fixed-support estimate

\[
|Q(a,q)-Q(a,p)|\le\frac12\lVert q-p\rVert_\infty.
\]

For any feasible load, the two objective values differ by
`Σ_i α_i(q_i−p_i)`; comparing the attained maximizers in both directions
proves this estimate and hence multivariate continuity. This is not an
inference from differentiability on each line, and it includes singleton
rows.

The connectivity hypothesis is the actual finite-path condition
`TransportCoercivity.connected S`. The module **derives** connectivity of
the positive conductance graph at every q. A row step between distinct
vertices chooses two distinct active corners, which form one of the
three pair labels of `TriangleLoads`. Their conductance is positive. A
step from a vertex to itself uses a zero-length path. Induction transports
the complete row path. Singleton rows provide no distinct-vertex edge;
parallel edges and loops from repeated destinations are allowed.

The existing mixed-support derivative theorems are then applied to the
identity `(1-t)x+t y = x+t(y-x)`. They supply the actual first derivative
and the actual graph-energy second derivative on every grounded segment.
Together with the proved vertex bound, continuity and finite table
identities, `GroundedConvexity.exists_unique_grounded_minimizer` yields
exactly one grounded minimum of

\[
\mathcal P_d(q)=\sum_t Q(a^t,q\circ c_t)-\sum_v d_vq_v.
\]

For a prescribed physical demand `δ`, only the free-vertex equalities
`δ_v=d_v` for `v≠root` are required. The theorem
`root_demand_difference` keeps the exact identity

\[
\mathcal P_\delta(q)-\mathcal P_d(q)
=(d_{\mathrm{root}}-\delta_{\mathrm{root}})q_{\mathrm{root}}.
\]

Thus the two functions agree on `q_root=0`, and
`exists_unique_prescribed_minimizer` proves the unique minimum for the
original free-vertex demands. No boundary equation is introduced.

For a disk with several fixed boundary corners, map them to one root but
retain their **separate** prescribed coefficients `a_ti` in the potential.
`pooled_boundary_weight` proves that grounding leaves each original
boundary weight equal to that coefficient. Only the transport table is
aggregated. This includes two-zero protected boundary data and singleton
rows without interpreting a zero denominator in the arctangent formula.
The one-vertex grounded space is covered by the same theorems.

The supplied positive table must still come from the written Hall argument,
and the stated incidence/support and its row connectivity must describe
the actual disk. Those geometric/combinatorial application proofs have not
been replaced by hypotheses asserting a minimum. The module does not prove
support-changing limits of minimizers, parameter smoothness, nonlinear
implicit-function results, circle development or the action-volume
identity. The earlier general coercivity and convexity modules remain
applicable to other potentials with their own explicit inputs.

## Euler equations for the actual triangle potential

[TriangleBalance.lean](TriangleBalance.lean) contains three definitions and
nineteen theorems in `VolumeLogic.TriangleBalance`. It identifies the minimum
just constructed with a unique solution of the concrete free-vertex load
equations. It uses the same `TrianglePotential.summedPotential`, not a new
potential defined by a desired gradient.

Let `T` and `V` be finite sets of triangles and vertices. Corner `i : Fin 3`
of triangle `t` has destination `c t i` and nonnegative fixed coefficient
`a t i`. Each row has nonempty positive support. For `q : V → ℝ`, put
`w_(t,i) = a_(t,i) exp(q_(c(t,i)))`. On a row with at least two positive
corner coefficients, the maximizing load is the actual formula

\[
\alpha_{t,i}(q)=\frac1\pi\arctan\!
 \frac{w_{t,i}}{\sqrt{w_{t,0}w_{t,1}+w_{t,1}w_{t,2}+w_{t,2}w_{t,0}}}.
\]

On a singleton row, the sole active corner has load `1/2` and the other
corners have load zero. `supportedLoad` combines these two cases;
`potential_eq_supportedLoad` proves that it attains the original supported
entropy supremum. The cases are determined by the fixed coefficients,
so differentiation never changes support.

The vertex load and residual are

\[
 L_v(q)=\sum_{t}\sum_{i:\,c(t,i)=v}\alpha_{t,i}(q),
 \qquad R_v(q)=L_v(q)-d_v,
\]

where `d : V → ℝ` is the prescribed demand. All corner contributions are
retained when destinations coincide. The entropy optimization continues to
use the three distinct corner variables; only their loads are aggregated
at the shared vertex. Fixed boundary offsets remain in the coefficients
`a`, including when multiple boundary corners are pooled at one root.

For the actual shared potential
`P(q) = summedPotential c a d q`, the module proves

\[
 \left.\frac{d}{ds}P(q+s h)\right|_{s=u}
   =\sum_v R_v(q+u h)h_v.
\]

Thus varying one coordinate gives precisely `R_v(q)`. The proof applies
the previously proved arctangent and singleton derivatives, then expands
the finite incidence sums. It does not assume a gradient identity.

| Theorem | Content |
| --- | --- |
| `potential_supporting` and `summedPotential_supporting` | The maximizing loads at `q` are feasible competitors at every `p`; their objective difference gives `P(p) ≥ P(q) + Σ_v R_v(q)(p_v−q_v)`. No convexity premise is supplied. |
| `summedPotential_path_derivative` and `coordinate_derivative` | Actual affine-path and coordinate derivatives equal the residual pairing and single-vertex residual. |
| `minimizer_balance` | A minimum on `q_root = 0` satisfies `L_v(q)=d_v` for every `v ≠ root`, by the derivative at a one-variable minimum. |
| `balance_minimizer` and `grounded_minimizer_iff_balance` | Conversely, those free equations make the supporting inequality nonnegative on every grounded displacement, proving a global grounded minimum. This equivalence needs only nonnegative coefficients and nonempty rows, not a transport table or connectedness. |
| `exists_unique_balance` | An explicit positive supported corner table of row mass `1/2`, matching the demands away from the root, together with actual connected row paths, gives exactly one grounded solution of all free load equations. Existence and uniqueness reuse the proved minimum theorem. |
| `sum_vertexLoad`, `root_residual` and `root_balance_iff_total` | Total load is exactly `card T / 2`. After the free equations hold, the root residual is `card T / 2 − Σ_v d_v`; hence its equation holds exactly when the total demand matches. |

The last point preserves the physical boundary convention. Grounding a
coordinate does not impose its Euler equation. The root demand can be
arbitrary, just as in `exists_unique_prescribed_minimizer`. With a single
vertex there are no free equations, but the grounded solution is still
unique. Without connected support, unused free coordinates can give
multiple solutions.

The checker compiles four exact boundary controls: a triangle has total
load `1/2`, repeated destinations retain the sum of their corner loads, a
one-vertex grounded minimum need not satisfy the root equation, and
disconnected support can admit distinct grounded solutions. These are
small mathematical counterexamples to stronger unsupported conclusions,
not sampled tests of the general theorem. Their axioms are audited
separately from the reusable module's declaration inventory.

The corner table's existence and its free columns, actual incidence and
row connectivity remain explicit inputs. Hall feasibility, geometric
identification/development and limits that change support are not proved
by this module. No stationary point, coercivity, strict convexity or
Hessian formula is assumed as a substitute for the actual load equations.

## Pinned dependencies

- Lean: `leanprover/lean4:v4.32.2`.
- Mathlib: `905b95818eb32af7874a58b427f50c1711a5e96c`.
- [lake-manifest.json](lake-manifest.json) fixes all nine Git dependencies,
  including Mathlib's transitive packages.
- `volumeLogic` is the existing `../formal` path dependency.

The checker validates the complete expected dependency set and every URL and
revision. It also checks each materialized Git checkout's `HEAD` and requires
its tracked sources to be clean. Local cache symlinks may be used inside the
ignored `.lake/` directory; no machine-specific path is part of the package.

## Fresh-checkout setup

Use Git, Python 3.11 or newer, and Elan's `lake` command. Run the following
from the repository root. The first command installs the pinned Lean release
if it is not already present.

```sh
elan toolchain install leanprover/lean4:v4.32.2
cd formal-real
MATHLIB_NO_CACHE_ON_UPDATE=1 lake update volumeLogic mathlib
lake exe cache get \
  Mathlib.Analysis.Complex.Basic \
  Mathlib.Analysis.Convex.Deriv \
  Mathlib.Analysis.SpecialFunctions.Integrals.LogTrigonometric \
  Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus \
  Mathlib.Analysis.Calculus.Deriv.Shift \
  Mathlib.Analysis.Calculus.LocalExtr.Basic \
  Mathlib.Analysis.Normed.Module.FiniteDimension \
  Mathlib.LinearAlgebra.Matrix.ToLin \
  Mathlib.LinearAlgebra.Matrix.NonsingularInverse \
  Mathlib.LinearAlgebra.FiniteDimensional.Basic \
  Mathlib.Topology.Order.Compact \
  Mathlib.Topology.Order.Lattice \
  Mathlib.Algebra.Order.GroupWithZero.Finset \
  Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic \
  Mathlib.Analysis.SpecialFunctions.Pow.Real \
  Mathlib.Analysis.SpecialFunctions.Log.Basic \
  Mathlib.Analysis.SpecialFunctions.ExpDeriv \
  Mathlib.Analysis.SpecialFunctions.Sqrt \
  Mathlib.Analysis.SpecialFunctions.Trigonometric.ArctanDeriv \
  Mathlib.Data.Fin.VecNotation \
  Mathlib.Tactic.FieldSimp \
  Mathlib.Tactic.FinCases \
  Mathlib.Tactic.Positivity \
  Mathlib.Tactic.Linarith \
  Mathlib.Data.Real.Basic \
  Mathlib.Algebra.Order.BigOperators.Group.Finset \
  Mathlib.Algebra.BigOperators.Ring.Finset \
  Mathlib.Logic.Relation \
  Mathlib.Tactic.Ring
cd ..
python3 repro/check_concrete_limits.py
```

The environment variable suppresses Mathlib's automatic whole-library cache
download during dependency setup. The explicit `cache get` requests only
the listed modules and their transitive imports, as supported by this pinned
Mathlib's [cache documentation](https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Cache/README.md).
The replay then rejects any dependency drift. Do not update the pins merely
to make a different installed Mathlib version pass.

This remains an optional, heavier check. The full compatible Mathlib cache
used during development occupied about 5.83 GiB, shared locally; that is not
a measurement of the smaller selected download. Cold setup time and the
selected cache size have not been measured. With that cache present, the
bridge itself compiled in seconds. No cache download is part of routine
replay, and a missing dependency produces setup instructions.

## Replay and audit record

From the repository root:

```sh
python3 repro/check_concrete_limits.py --output concrete-limits-output
```

The output directory is caller-chosen. Omit `--output` for a temporary check
whose logs are removed afterward. `--lake` can select a Lake executable;
the executed Lean version must still match the pin.

The checker rebuilds the Std-only path dependency, compiles
`RealTransfer.lean`, `WeightedGraph.lean`, `Flattening.lean`,
`TransportCoercivity.lean`, `GroundedConvexity.lean` and
`GroundedLaplacian.lean`, `TriangleLoads.lean`, `TrianglePotential.lean`
`TriangleMinimizer.lean` and `TriangleBalance.lean`, and runs
[AxiomAudit.lean](AxiomAudit.lean). Every
definition and theorem must appear exactly once in the audit. Only Lean's
standard foundational axioms `propext`, `Classical.choice` and `Quot.sound`
are permitted; placeholders and additional axioms fail the check.

`summary.json` records every declaration, its axioms, all dependency pins,
and the SHA-256 hashes of the optional package, checker and Std-only sources.
It contains relative paths and omits timestamps so identical inputs produce
the same summary. Twenty-six negative controls check altered pins, missing or
duplicate dependencies, an absolute local dependency, incomplete or
duplicate declaration audits, an omitted graph module or grounded-energy
audit entry, an omitted flattening module or quadratic-cost audit entry,
an omitted transport module or grounded-coercivity audit entry,
an omitted grounded-convexity module or unique-minimum audit entry,
an omitted grounded-Laplacian module or unique-linear-solution audit entry,
an omitted triangle-load module or shared-load derivative audit entry,
an omitted triangle-potential module or actual supremum-gradient audit entry,
an omitted triangle-minimizer module or actual prescribed-minimum audit entry,
an omitted triangle-balance module or unique-load-solution audit entry,
and an unexpected logical axiom. A failed run
removes any old success summary in its output directory.

The optional count is **fifty-one definitions and two hundred eight theorems**, separate
from the Std-only theorem count: `RealTransfer` has two definitions and
twenty-two theorems, `WeightedGraph` has seven definitions and nineteen
theorems, `Flattening` has one definition and nine theorems,
`TransportCoercivity` has seven definitions and sixteen theorems,
`GroundedConvexity` has three definitions and eight theorems, and
`GroundedLaplacian` has four definitions and eighteen theorems, and
`TriangleLoads` has ten definitions and twenty-four theorems, and
`TrianglePotential` has eight definitions and forty-one theorems, and
`TriangleMinimizer` has six definitions and thirty-two theorems, and
`TriangleBalance` has three definitions and nineteen theorems. Four compiled
mathematical boundary controls have their own recorded axiom inventory and
are not added to these reusable-library counts. The audit
checks these proofs and the
listed dependency pins; it does not certify that a particular knot family
satisfies the remaining written analytic and geometric hypotheses.
