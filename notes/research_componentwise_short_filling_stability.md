# Long fillings after connected components with controlled quantum sums

Research consequence, 4 November 2026. Frozen manuscripts are unchanged.

The new graph estimates remove the dependence on component size from
one part of the short-filling argument. In particular, an arbitrarily
large connected component whose original degrees are at least 64 can
be filled with arbitrary fixed integer powers, before making the
remaining powers sufficiently long. Adjacent selected vertices and
zero powers are allowed. This statement concerns the original marked
circle-tree construction; it does not cover every short component.

## 1. Statement with the original parameters

Let \(T=(V,E)\) be a finite ordered circle tree with at least one edge.
Retain the original tangle order, physical rotations, disk framings,
reduced cut and orientations. Fix its carriers \(\eta_v\) and the
parity pattern for which the original strand tracing has one main
component and no internal closed component. Write
\[
                  n_v=\eta_v-2p_v,\qquad p_v\in\mathbb Z.
 \tag{1}
\]
The primitive filling curve remains \(\mu_v+p_v\lambda_v\), with
the original disk longitude \(\lambda_v\). No parameter is replaced
by a parameter of a reduced diagram.

Choose a nonempty proper subset \(S\subset V\) and fix its powers.
Let \(\mathcal C\) be the components of the induced subgraph on
\(S\). For every component \(C\), require either
\[
             |n_v|\ge\max(8,4d_v)\quad(v\in C),
 \tag{2}
\]
or
\[
                    n_v^2+d_v^2\ge4096\quad(v\in C),
 \tag{3}
\]
where \(d_v\) is its degree in the original tree. Different components
may use different alternatives. This does not permit choosing between
(2) and (3) separately at vertices of one component.

There is also a proved mixed alternative for a component: require
at each of its vertices that
\[
 |n_v|\ge\max(8,4d_v)
       \quad\text{or}\quad n_v^2+d_v^2\ge512^2.
 \tag{3a}
\]
The choice in (3a) may vary between adjacent vertices. Its larger
second threshold is part of the separate mixed proof; it is not
replaced by 64.

**Theorem 1.** There is a finite \(B\), depending on the marked tree,
the selected set and its fixed powers, such that all remaining choices
\[
 n_v\equiv\eta_v\pmod2,\qquad |n_v|\ge B
                             \quad(v\in V\setminus S)
 \tag{4}
\]
give hyperbolic knots with
\[
 \langle K\rangle_N
   =\Omega_N N^{3/2}A\,e^{N\mathcal S}(1+O(N^{-1})),
 \qquad |\Omega_N|=1,\quad A\ne0,\qquad
 2\pi\Re\mathcal S=\operatorname{Vol}(S^3\setminus K).
 \tag{5}
\]
The powers in (4) have independent signs and magnitudes and are fixed
before \(N\) tends to infinity. The asymptotic holds along all integer
levels. No uniform threshold over all choices of the fixed short
powers is asserted.

In particular, (3) permits every fixed power at every vertex of a
selected component whose original degrees are at least 64. There is
no bound on the number of its vertices. The older sufficient degree
bound \(d_v\ge256|C|\) is not needed for these components.

## 2. Why the component results can be assembled

For a component \(C\), let \(k_C=|C|\), let \(E_C\) contain all
edges with at least one endpoint in \(C\), and put \(m_C=|E_C|\).
Let \(b_C\) count its boundary edges. Since the original graph is a
tree,
\[
                   m_C=k_C-1+b_C.
 \tag{6}
\]
An outside vertex meets a given component at most once. Thus its
boundary polynomial has degree at most \(N-1\) in each of its own
outside colors, even though several components may later share the
same free vertex.

Apply the [branching source theorem](research_degree_controlled_network_source.md)
in case (2), or the
[degree-power source theorem](research_network_degree_power_source.md)
in case (3); for (3a), use Theorem 3 of that note. Apply the chosen
theorem to the graph consisting of \(C\) and all its boundary
edges. The degrees of its selected vertices are exactly their original
degrees. These theorems and the
[whole-boundary estimate](research_network_whole_boundary_decay.md)
give the literal polynomial obtained by tracing all vertices in \(C\):
\[
 Z_{C,N}(\mathbf u)=\varepsilon_{C,N}
       N^{3(k_C-m_C)/2}a_C(\mathbf u)
                  e^{NW_C(\mathbf u)}(1+O(N^{-1})),
       \qquad a_C(0)\ne0.
 \tag{7}
\]
It has the required bound on the entire real boundary period and a
quadratic bound on a fixed complex strip. All ordinary derivatives
and both level parities are retained.

Let \(V_0=V\setminus S\), \(r=|V_0|\), and let \(E_0\) contain
the edges with both endpoints in \(V_0\). Commuting finite traces in
different selected variables leaves exactly
\[
 B_N(\mathbf u)=
       \prod_{vw\in E_0}K_N(u_v,u_w)
       \prod_{C\in\mathcal C}Z_{C,N}(\mathbf u_{\partial C}).
 \tag{8}
\]
No edge is shared by two selected components. The polynomial in (8)
is retained before tracing the remaining variables; a shared variable
may have degree \(d_v(N-1)\). No reduction of its degree or loss of
first normal data is made.

Its local phase is
\[
 P(\mathbf u)=\sum_{vw\in E_0}\psi(u_v,u_w)
                        +\sum_C W_C(\mathbf u_{\partial C}).
 \tag{9}
\]
The amplitudes multiply to a nonzero amplitude. The global angular
losses and strip bounds multiply as well. Every remaining vertex has
an original incidence, so it receives a positive angular loss. Separate
evenness makes the Hessian of \(P\) diagonal at zero. The whole-boundary
bound gives a strictly negative real diagonal entry for every remaining
variable. Consequently (8) satisfies all hypotheses of the
[complex-phase long-filling theorem](research_long_fillings_complex_boundary_phase.md).
That theorem explicitly permits polynomial degrees that are fixed
multiples of \(N-1\).

The initial power of \(N\) is
\[
 -\frac32|E_0|+\frac32\sum_C(k_C-m_C)
       =-\frac32(|E|-|S|)=-\frac32(r-1).
 \tag{10}
\]
The remaining \(r\) traces add \(3r/2\). The resulting coefficient
is nonzero, and the final power is \(3/2\), as in (5). The action is
\[
 \mathcal S=\operatorname{stat}_{\mathbf u}
      \left[P(\mathbf u)+\sum_{v\in V_0}
                  \left(\frac{in_vu_v^2}{4\pi}-iu_v\right)\right].
 \tag{11}
\]
This proves the full finite-source asymptotic, including its lower bound.

## 3. Absolute volume and what remains outside the theorem

At zero free angles each selected component has positive original
edge shapes and the original unit-charge filling periods, by its
source theorem. Different components share only complete outside
vertices, so these configurations fit together with the untouched
complete edges. Apply the
[marked positive-point completion theorem](research_positive_point_marked_completion.md)
to this single original circle tree and the entire selected set.
It gives the complete partially filled exterior with absolute volume
\(2\pi\Re P(0)\). This use does not require the selected set as a
whole to satisfy one of (2), (3) or (3a); the positive shapes and actual
period equations have already been supplied component by component.

For small free angles the selected equations have their holomorphic
solutions from (7). The remaining periods are derivatives of (9)
in the original meridian and longitude bases. Choose the threshold
in (4) large enough that the long-filling stationary point and its
small charge path stay in this positive neighborhood. The already
selected fillings stay smooth, and the remaining primitive slopes
finish with cone angle \(2\pi\). Marked completion therefore gives
the original knot complement. Integrating the volume differential,
with the initial value \(2\pi\Re P(0)\), gives the last equality
of (5). Equivalently this is the geometric assembly in Section 10
of the [connected-component argument](research_connected_short_filling_clusters.md),
now with the stronger component estimates (7). The original framing
and carrier factors have modulus one and are kept in \(\Omega_N\).

The theorem permits different proved kinds of component in the same
partially filled tree and removes the former size-dependent degree
condition. It does not estimate an arbitrary component that fails
all of (2), (3) and (3a). Such a fixed component can leave infinitely many
choices for the remaining powers, so this is a partial-filling
stability theorem, not the finite-exception theorem. The original
assignment fibers, including those in zero-power reductions, are
unchanged.
