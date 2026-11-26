# Long fillings beside fixed chains of three-crossing blocks

Research consequence, 4 November 2026. Frozen manuscripts are unchanged.

Selected components may now include homogeneous three-crossing paths
of any fixed length at least three. Their actual two-boundary sources
have nonzero local packets and strict decay on the whole real outside
period. They can be filled first, alongside the previously controlled
graph components, before making the remaining original powers long.
Each path may have power \(+3\) throughout or power \(-3\)
throughout; different components may choose signs independently.
Arbitrary sign changes within one path are not included.

Length three uses the direct two-cap/one-retained-vertex theorem.
Lengths four and five use their separate closing and outside-boundary
theorems.
Lengths six and above use the existing larger closing and outside-color
theorems; their statements and proofs are unchanged.

The scalar path theorem is not itself a knot identification. This
application retains the original marked circle-tree construction and
its strand, carrier and primitive-filling conditions.

## 1. Statement in the original parameters

Let \(T=(V,E)\) be a finite ordered circle tree with an edge. Keep
its original page and tangle orders, physical rotations, disk framings,
reduced cut, orientations and carriers \(\eta_v\). Fix a parity
pattern for which the original strand tracing has one main component
and no internal closed component. The parameters remain
\[
 n_v=\eta_v-2p_v,\qquad p_v\in\mathbb Z,
 \qquad \text{primitive slope }\mu_v+p_v\lambda_v,
 \tag{1}
\]
with the original disk longitude. No reduced-diagram parameter replaces
these data.

Choose a nonempty proper selected set \(S\subset V\) and fix its
powers. For each component \(C\) of \(T[S]\), require one of:

1. Every \(v\in C\) satisfies \(|n_v|\ge\max\{8,4d_v\}\).
2. Every \(v\in C\) satisfies \(n_v^2+d_v^2\ge64^2\).
3. At each \(v\in C\), either condition 1 holds or
   \(n_v^2+d_v^2\ge512^2\); this choice may vary within \(C\).
4. \(C\) is a path of \(m_C\ge3\) selected vertices, every one
   of original degree two, with \(n_v=3\sigma_C\) for one fixed
   \(\sigma_C\in\{1,-1\}\). Its two boundary edges meet two
   distinct unselected vertices.

Degrees count every original incidence, including boundary edges.
Conditions 1 and 2 may be chosen componentwise, but cannot be combined
vertexwise unless the stronger condition 3 applies. The two boundary
vertices in condition 4 remain distinct original variables, although
each may also meet other selected components. Their coincidence would
create a cycle and is excluded by the original tree hypothesis.

**Theorem 1.** For these fixed data there is a finite \(B\) such
that every remaining assignment
\[
 n_v\equiv\eta_v\pmod2,\qquad |n_v|\ge B
                         \quad(v\in V\setminus S)
 \tag{2}
\]
gives the original hyperbolic knot and
\[
 \langle K\rangle_N=\Omega_N N^{3/2}\mathcal A
    e^{N\mathcal S}(1+O(N^{-1})),\qquad
 |\Omega_N|=1,\quad\mathcal A\ne0,
 \qquad 2\pi\Re\mathcal S=\operatorname{Vol}(S^3\setminus K).
 \tag{3}
\]
The remaining signs and magnitudes are independent. Both level parities
are retained. The marked tree and all powers are fixed before
\(N\to\infty\); \(B\) may depend on those fixed selected powers
and lengths. No uniform threshold over all trees or path lengths is
asserted. Condition 4 requires compatible original carriers, namely
\(p_v=(\eta_v-3\sigma_C)/2\in\mathbb Z\).

## 2. Exact path source, normalization and uniform sign reversal

Write \(v(z)=(e_0(z),\ldots,e_{N-1}(z))^T\). The original
edge and full trace identities are
\[
 K_N(z,w)=v(z)^Tv(w),\quad
 \phi_N(e_i e_j)=J_{ij}=\mathbf1_{i+j=N-1},\quad
 \phi_N(R_N^n e_i e_j)=(JM^n)_{ij}.
 \tag{4}
\]
These are the all-level algebraic identities in
[the original source calculation](research_quantum_cap_primitive_source.md#2-the-actual-crossing-and-turn-substitutions)
and [the three-crossing matrix proof](research_positive_three_crossing_cycle.md#1-exact-source-and-positive-conjugacy).
The last identity uses \(M^TJ=JM\), where \(M\) is multiplication
by the original crossing. It retains all first normals at double roots.
Expand each original edge kernel and take the selected traces. A path
with \(m\) selected vertices and \(m+1\) incident edges gives exactly
\[
 Z_{C,N}(z_L,z_R)=
 \left(\prod_{v\in C}\phi_N^{(v)}R_N(t_v)^{3\sigma_C}\right)
          \prod_{e\in E_C}K_N(t_{e,-},t_{e,+})
 =v(z_L)^T A_{\sigma_C}^{m}v(z_R),
 \qquad A_\sigma=JM^{3\sigma}.
 \tag{5}
\]
There is no additional power of \(N\). The outside colors remain
literal polynomial variables of separate degree at most \(N-1\).

For positive power, use [the three-block theorem, Theorem 1](research_three_chain_three_closure.md)
when \(m=3\), [the four-block theorem, Theorems 1--2](research_three_chain_four_closure.md)
when \(m=4\), and [the five-block theorem, Theorems 1--2](research_three_chain_five_closure.md)
when \(m=5\). For \(m\ge6\), use the
[larger closing theorem](research_three_larger_source_closure.md)
and [outside-color theorem](research_three_chain_outside_boundary_decay.md).
These give the same nonzero holomorphic packet on a fixed ordinary-color neighborhood
of \((-2,-2)\):
\[
 Z_{C,N}=C_{N,3}^2\kappa^{m-2}N^{-3/2}
       a_C(z_L,z_R)e^{NW_C(z_L,z_R)}(1+O(N^{-1})),
 \qquad a_C(-2,-2)\ne0.
 \tag{6}
\]
They also give, for all real outside angles and sufficiently small
fixed heights, all ordinary derivatives and both parities,
\[
 |\partial_{z_L}^{a}\partial_{z_R}^{b} Z_{C,N}|
 \le C_{a,b}N^{q_{a,b}}
 e^{N[\Re W_C(0)-c_C(1-\cos u_L+1-\cos u_R)
                         +B_C(h_L^2+h_R^2)]},\quad c_C>0,
 \tag{7}
\]
where \(z_i=-2\cos(u_i+ih_i)\); \(W_C(0)\) denotes complete
outside angles. These are bounds for the undeleted source, including
the original radical and Fourier-corner errors. In particular the
local assertion is stronger than complete-point finite jets.

The [original exact identity](research_positive_three_crossing_cycle.md#1-exact-source-and-positive-conjugacy)
\(\bar M=M^{-1}\), with real \(J\)
and real Newton polynomials, proves
\[
 A_-=\overline{A_+},\qquad
 Z_{C,N}^-(z_L,z_R)=
       \overline{Z_{C,N}^+(\bar z_L,\bar z_R)}.
 \tag{8}
\]
This is a polynomial identity, including all ordinary derivatives.
It conjugates the full trace, not a value-only approximation. Thus
(6)--(7) hold for negative paths too, with inverse unit carrier,
conjugate phase and amplitude, and reversed height signs.

For a general selected tree component, put \(k_C=|C|\), let
\(b_C\) count boundary edges and \(e_C=|E_C|\). Then
\[
 e_C=k_C-1+b_C,
 \qquad b_C=2\Longrightarrow\frac32(k_C-e_C)=-\frac32.
 \tag{9}
\]
The path power in (6) therefore agrees exactly with the component
normalization. Its carrier equals \(C_{N,3}^m\) times the unit
\((\kappa/C_{N,3})^{m-2}\) in the positive case, and its conjugate
in the negative case. These original unit factors are retained in
\(\Omega_N\); they do not alter a filling parameter.

## 3. Original periods and absolute action

At complete outside angles take the actual positive path solution
\(t_v^+\). Its negative counterpart is
\[
 t_v^-=-\overline{t_v^+},\qquad
 r_{v,e}^-=-\overline{r_{v,e}^+},\qquad
 r_{v,e}=\operatorname{asinh}\{\tan(t_v/2)\cos(t_w/2)\}.
 \tag{10}
\]
Oddness and Schwarz symmetry on the original continued branch give
the return identity. It preserves the full logarithmic equations:
\[
 3t_v^++2i\sum_{e\ni v}r_{v,e}^+=2\pi
 \quad\Longrightarrow\quad
 -3t_v^-+2i\sum_{e\ni v}r_{v,e}^-=2\pi.
 \tag{11}
\]
Both solutions have \(\Im t_v<0\). With \(a_v=\tan(t_v/2)\),
the positive edge root \(q_e^2=1+a_v^2+a_w^2\) transforms to
\(\bar q_e\), while \(a_v\) transforms to \(-\bar a_v\).
The criterion
\(\Re q_e>\sqrt{(\Re a_v)^2+(\Re a_w)^2}\) is unchanged.
Hence the same original ordered cells remain positive, with their
original marking and primitive periods.

The [connected action chart](research_three_chain_action_volume_calibration.md)
identifies each retained vertex phase with the original angular phase
plus a fixed purely imaginary constant \(i\gamma\). This is a
holomorphic derivative identity on an open chart. The
[original free-outside cap phase](research_homogeneous_wire_complete_cap.md)
uses the literal free edge \(\psi(t,u)\). Consequently, for small
free outside angles as well as at completeness,
\[
 W_C(\mathbf u)=\operatorname{stat}_{(t_v)_{v\in C}}
 \left[\sum_{e\in E_C}\psi(t_{e,-},t_{e,+})
   +\sum_{v\in C}\left(\frac{3\sigma_C i t_v^2}{4\pi}-it_v\right)
 \right]+i\sigma_C(m_C-2)\gamma.
 \tag{12}
\]
Nondegeneracy and the open action chart continue the actual selected
solution; equality is not inferred merely from its complete value.
Stationarity removes derivatives of the eliminated variables, so the
outside derivatives of (12) are the original peripheral returns.
At zero outside angles its real action is the original marked
partial-filling volume divided by \(2\pi\). The imaginary constant
is retained and has zero real part and zero outside derivative.

## 4. Assemble the source before tracing the remaining vertices

For alternatives 1--3 use the component theorems in
[componentwise stability](research_componentwise_short_filling_stability.md).
For alternative 4 use (5)--(12). Every component supplies the literal
polynomial and packet
\[
 Z_{C,N}(\mathbf u_{\partial C})=
 \varepsilon_{C,N}N^{3(k_C-e_C)/2}
 a_C(\mathbf u_{\partial C})e^{NW_C(\mathbf u_{\partial C})}
 (1+O(N^{-1})),\qquad a_C(0)\ne0,
 \tag{13}
\]
with a full real-period and quadratic-strip bound. Its selected
degrees are exactly the original degrees. No threshold from one
graph regime is borrowed for a different regime at an adjacent vertex.

Let \(V_0=V\setminus S\), \(r=|V_0|\), and let \(E_0\)
contain edges with both endpoints in \(V_0\). Commuting the exact
finite traces in distinct selected variables leaves
\[
 B_N(\mathbf u)=\prod_{vw\in E_0}K_N(u_v,u_w)
                   \prod_C Z_{C,N}(\mathbf u_{\partial C}),
 \qquad
 P(\mathbf u)=\sum_{vw\in E_0}\psi(u_v,u_w)
                      +\sum_C W_C(\mathbf u_{\partial C}).
 \tag{14}
\]
An outside vertex meets a component at most once in a tree. The
separate ordinary degree of (14) is at most \(d_v(N-1)\) at each
remaining vertex. The source is not reduced to lower-degree values;
its full normal data remain present before the remaining traces.

The local amplitudes multiply to a nonzero amplitude. The boundary
and strip estimates multiply as well. Every remaining vertex has
an original incidence, hence receives a positive real angular loss
from a component or an untouched edge. Separate evenness makes the
boundary Hessian diagonal at zero, with strictly negative real
diagonal. Thus (14) satisfies the hypotheses of the
[complex-phase long-filling theorem](research_long_fillings_complex_boundary_phase.md),
including its allowed fixed-multiple polynomial degrees.

Every original edge occurs once. The prefactor exponent is
\[
 -\frac32|E_0|+\frac32\sum_C(k_C-e_C)
    =-\frac32(|E|-|S|)=-\frac32(r-1).
 \tag{15}
\]
The \(r\) remaining original traces add \(3r/2\), giving
\(N^{3/2}\). Their nonzero Gaussian coefficients and the component
coefficients give the finite-source asymptotic (3), with
\[
 \mathcal S=\operatorname{stat}_{\mathbf u}
 \left[P(\mathbf u)+\sum_{v\in V_0}
          \left(\frac{in_vu_v^2}{4\pi}-iu_v\right)\right].
 \tag{16}
\]

## 5. Marked completion and scope

At zero free angles the selected components supply positive original
edge shapes, negative imaginary selected angles and the original
unit-charge period equations. Negative paths satisfy these by
(10)--(11). Components meet only at complete outside vertices;
untouched edges are complete. Their data therefore fit simultaneously
on the single original circle tree.

Apply [positive-point marked completion](research_positive_point_marked_completion.md)
to the entire selected set. It gives the original smooth partial
filling, with remaining auxiliary cusps and the main cusp complete,
and volume \(2\pi\Re P(0)\). The selected equations and outside
periods continue holomorphically by (12) and the other component
theorems. Choose the threshold in (2) so that the remaining critical
point and its charge path stay in this positive neighborhood. The
selected fillings remain smooth, and the remaining original primitive
slopes finish at cone angle \(2\pi\). Under the original strand
and component hypotheses, marked completion identifies the result
with the original knot complement. Integrating the volume differential
from \(2\pi\Re P(0)\) proves the volume equality in (3).
This is precisely the geometric assembly of componentwise stability,
now with the additional actual path kernels (6)--(8).

The result is stability beside fixed selected components, not a
cofinite-assignment theorem for general fixed templates. Uncontrolled
short components can still leave infinitely many assignments at other
vertices. Nonuniform short words and changed boundary identifications
are not supplied here. No
zero-power reduction, modular conjugacy or reassignment of original
filling fibers is used.

## 6. Reproduction

```sh
python3 experiments/check_three_chain_short_filling_stability.py --precision 256
```

The [checker](../experiments/check_three_chain_short_filling_stability.py)
and [record](../repro/results/research-three-chain-short-filling-stability.json)
give finite normalization diagnostics for the trace/matrix and mirror
identities in the original basis, whose all-level proofs are cited
above. They also check symbolic component/degree and power bookkeeping,
carrier counting, and passed source provenance, including the separate
three-block central-current and cap-complement certificates and their
independent replays, as well as the four-block and five-block records.
The concrete tree diagnostic includes paths of lengths three, four, five
and six meeting the same remaining vertex. Geometric completion
and knot identification use the written marked theorems and hypotheses;
they are not inferred from finite matrix tests.
