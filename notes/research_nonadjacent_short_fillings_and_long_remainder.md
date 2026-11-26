# Long fillings after nonadjacent short fillings

Research theorem, 2 November 2026. The result below allows fixed short
fillings at several original vertices, including internal vertices,
before making the remaining powers independently long. The selected
vertices must not be adjacent. All powers are fixed before the quantum
level tends to infinity. The frozen manuscripts are unchanged.

## 1. The marked knot template and the theorem

Let \(\mathcal T=(V,E)\) be a fixed finite ordered circle tree with
at least one edge. Use the original tangle stacks, physical quarter
turns, disk frames, strand orientations, cylindrical closure, and
reduced cut of the
[circle-tree geometry paper](../papers/circle-tree-geometry/main.tex).
There are no unrecorded product junctions. At every vertex retain its
carrier \(\eta_v\in\{-1,0,1\}\). The crossing power and the
integer filling coefficient are related by

\[
 n_v=\eta_v-2p_v,\qquad p_v\in\mathbb Z.
                                                               \tag{1}
\]

The filled primitive curve is the original
\(\mu_v+p_v\lambda_v\), where \(\lambda_v\) is the disk
longitude. Fix the parity pattern so that literal strand tracing
produces one main component and no internal closed component.

Choose a set \(S\subset V\) of original vertices such that no edge
joins two elements of \(S\). Fix a power \(n_s\equiv\eta_s\pmod2\)
at each \(s\in S\), and write \(d_s=\deg_{\mathcal T}(s)\).
Require one of the following at every selected vertex:

- If \(d_s=1\), require \(|n_s|\ge2\).
- If \(d_s=2\), one may also take \(n_s=2\) or \(-2\).
- At any vertex with \(d_s\ge3\), one may take \(n_s=0\).
- At any internal vertex \(d_s\ge2\), one may instead use
  \[
    d_s^2+n_s^2\ge\max\{1024,128d_s\}.                  \tag{2}
  \]

The internal condition (2) is an alternative to the explicitly
included degree-two powers \(\pm2\) and zero powers at degree at
least three. Every fixed power is allowed at an internal vertex of
degree at least 128. Condition (2) also permits every internal degree
when \(|n_s|\ge64\).

Let

\[
 V_0=V\setminus S,\quad r=|V_0|\ge1,\qquad
 E_0=\{vw\in E:v,w\in V_0\},\quad e_0=|E_0|.
\]

The graph \((V_0,E_0)\) need not be connected. The eliminated
internal vertices will contribute functions of several remaining
boundary angles, so their connections have not been discarded.

**Theorem.** There is a finite threshold \(B\), depending on the
fixed marked tree and the fixed selected powers, such that every
assignment of remaining powers

\[
 n_v\equiv\eta_v\pmod2,\qquad |n_v|\ge B
                    \quad(v\in V_0)
                                                               \tag{3}
\]

produces a hyperbolic knot \(K\) whose reduced zero-framed Kashaev
invariant satisfies

\[
 \langle K\rangle_N
 =\Omega_N N^{3/2}D e^{NS}
          (1+O_{\mathbf n}(N^{-1})),\qquad
 |\Omega_N|=1,\qquad D\ne0,                              \tag{4}
\]

through all sufficiently large integer levels, with

\[
       2\pi\Re S=\operatorname{Vol}(S^3\setminus K).
                                                               \tag{5}
\]

Consequently the original Kashaev volume identity holds for these
knots. The remaining powers have independent signs and magnitudes.
The threshold is not asserted to be uniform over the selected powers
or over different trees. The selected vertices are original vertices;
the theorem does not justify selecting a vertex that becomes terminal
only after an earlier short filling.

## 2. Exact elimination with every boundary retained

Put \(q=e^{\pi i/N}\), and let \(e_k\), \(R\), and \(\phi_N\)
be the complete Newton basis, crossing element, and closing functional
of the original finite contraction. The complete edge kernel is

\[
 K_N(t,u)=\sum_{k=0}^{N-1}e_k(-2\cos t)e_k(-2\cos u).
\]

For a selected vertex define its exact boundary polynomial

\[
 P_{s,N}((u_v)_{v\sim s})
   =\mathcal D_{n_s,N}^{(t)}
       \left[\prod_{v\sim s}K_N(t,u_v)\right],
 \qquad \mathcal D_{n,N}f=\phi_N(R^n f).
                                                               \tag{6}
\]

At a terminal vertex this is precisely the previously defined
\(H_{n_s,N}\). No two selected vertices share an edge, so the
corresponding sums and traces can be taken independently in the
original finite contraction. The remaining polynomial is exactly

\[
 B_N(\mathbf u)
  =\prod_{vw\in E_0}K_N(u_v,u_w)
     \prod_{s\in S}P_{s,N}((u_v)_{v\sim s}).              \tag{7}
\]

A free variable \(u_v\) may occur in several selected factors.
Their product is retained before applying its own trace. Its degree
in \(-2\cos u_v\) is at most \(\deg_{\mathcal T}(v)(N-1)\).
The exact reduced invariant is

\[
 \langle K\rangle_N
 =q^{(N-1)^2w(D)/2}
       \left(\prod_{v\in V_0}\mathcal D_{n_v,N}^{(v)}\right)
          B_N(\mathbf u),                                \tag{8}
\]

where \(w(D)\) is the writhe of the original oriented diagram.
These formulas use the original quotient traces, including the first
normal derivatives at repeated spectral roots. They do not replace
the raw polynomial in (7) by a reduced representative between nodes.
The identity follows directly from
[the complete finite source](../papers/circle-tree-volume/finite-bounds.tex).

## 3. The selected geometric actions and quantum phases

For each \(s\in S\), let \(t_s(\mathbf u_s)\) be the selected
solution of

\[
 \sum_{v\sim s}\psi_t(t_s,u_v)
                  +\frac{in_s}{2\pi}t_s=i,
 \qquad \mathbf u_s=(u_v)_{v\sim s}.
                                                               \tag{9}
\]

Use the branch continued from the complete structure by its primitive
cone deformation. Define

\[
 G_s(\mathbf u_s)
 =\sum_{v\sim s}\psi(t_s(\mathbf u_s),u_v)
       +\frac{in_s}{4\pi}t_s(\mathbf u_s)^2
       -it_s(\mathbf u_s),
 \qquad M_s=\Re G_s(\mathbf0).                           \tag{10}
\]

Every selected pair satisfies \(d_s+|n_s|>2\). The
[isolated-vertex geometry proof](research_isolated_internal_vertex_geometry.md)
therefore gives this branch, its positive tetrahedra, and its original
primitive periods. For the internal vertices satisfying (2), its small
critical point is the one in
[the degree-and-power source theorem](research_high_degree_short_internal_vertex.md),
by uniqueness on the overlapping branch.

The complete boundary asymptotic at each selected vertex can be written

\[
 P_{s,N}(\mathbf u_s)
 =\varepsilon_{s,N}N^{-3(d_s-1)/2}a_s(\mathbf u_s)
        e^{NG_s(\mathbf u_s)}(1+O(N^{-1})),
 \qquad |\varepsilon_{s,N}|=1.                           \tag{11}
\]

The amplitude is holomorphic and nonzero near zero. For internal
vertices satisfying (2), this is precisely the source theorem just
cited. For degree two and power \(\pm2\), it is supplied by the
[two-boundary source theorem](research_degree_two_power_two_boundary_theorem.md)
and its
[marked phase comparison](research_degree_two_power_two_geometric_phase.md).
At zero power and degree at least three, use the
[whole-boundary zero-power theorem](research_zero_power_internal_boundary_theorem.md).
For terminal
vertices it is supplied by the
[two-crossing](research_two_crossing_terminal_filling.md),
[three-crossing](research_three_crossing_terminal_filling.md),
[finite-range](research_terminal_powers_four_through_thirty_one.md), and
[large-power](research_terminal_large_fixed_powers.md) boundary theorems.

There are two explicit two-crossing phase conventions. If
\(d_s=1\), \(n_s=2\sigma\), \(\sigma=\pm1\), the source
phase in the two-crossing formula differs from (10) by
\(\sigma i\pi/2\). Thus in (11) take

\[
 \varepsilon_{s,N}=e^{\sigma i\pi N/2},\qquad
 a_s(u)=\frac{e^{-\sigma i\pi/4}}{2\sqrt{\cos(u/2)}}.
                                                               \tag{12}
\]

If \(d_s=2\), \(n_s=2\sigma\), use instead

\[
 \varepsilon_{s,N}=e^{\sigma i\pi N/2},\qquad
 a_s(u,v)=A_\sigma(u,v),
\]

where \(A_+\) is the amplitude (7) of the two-boundary theorem
and \(A_-\) is its coefficient conjugate. The marked phase
comparison proves the exact difference
\(\sigma i\pi/2\) between that source action and (10).
Its power of \(N\) is \(-3/2\), as prescribed by (11).

For every other selected vertex take

\[
 \varepsilon_{s,N}=C_{N,n_s}
       =q^{n_s(N-1)^2/4},                                \tag{13}
\]

and use the amplitude of its boundary theorem. In particular a
zero-power vertex has \(\varepsilon_{s,N}=C_{N,0}=1\), with exactly
the geometric action (10). No parameter-dependent
phase has been moved into a framing correction. The two constants
just recorded are the only differences between those local source
phases and the geometric action (10).

Each theorem also gives a bound on its entire boundary polynomial:

\[
 |P_{s,N}(\mathbf x_s+i\mathbf y_s)|
 \le C_sN^{A_s}\exp N\left\{
 M_s-c_s\sum_{v\sim s}(1-\cos x_v)
                         +B_s\sum_{v\sim s}y_v^2\right\}.
                                                               \tag{14}
\]

The constants are positive and the strip width is fixed. This estimate
includes the omitted wire terms, all nonunit Fourier charges, and the
exact endpoint currents; they are not premises left for the assembly.

## 4. The remaining full source meets the analytic hypotheses

The full edge kernel has a nonzero holomorphic asymptotic

\[
 K_N(u,v)=N^{-3/2}a_e(u,v)e^{N\psi(u,v)}(1+O(N^{-1}))
                                                               \tag{15}
\]

near zero, together with a whole-period Gaussian strip bound having
positive angular loss in both variables. The passage from retained
wire indices to this full kernel is justified in Section 2 of
[the terminal-filling assembly](research_verified_terminal_fillings_and_long_remainder.md):
the omitted wire rate has a fixed gap, which persists on a sufficiently
small bidisk and can be combined with the retained angular bound.

Multiplying (11) and (15) in the exact identity (7) gives the local
phase

\[
 P(\mathbf u)
 =\sum_{vw\in E_0}\psi(u_v,u_w)
      +\sum_{s\in S}G_s((u_v)_{v\sim s}),                 \tag{16}
\]

the nonzero amplitude
\(a(\mathbf u)=\prod_{E_0}a_e\prod_Sa_s\), and the power

\[
 \alpha=-\frac32\left[e_0+\sum_{s\in S}(d_s-1)\right]
        =-\frac32(r-1).                                 \tag{17}
\]

For the equality, independence of \(S\) partitions the original
edges into \(E_0\) and the selected stars. Thus
\(e_0+\sum_s d_s=|E|=r+|S|-1\). This computation does not
assume that the remaining forest is connected.

Write \(k_s=\cos(t_s(\mathbf0)/2)\). The boundary Hessian of
each selected action is diagonal, with entry \(-k_s/(2\pi)\)
at every neighbor, and \(\Re k_s>0\). Consequently

\[
 -\Re P_{vv}(\mathbf0)
 =\frac1{2\pi}\left[
       \deg_{E_0}(v)+\sum_{s\in S:\,s\sim v}\Re k_s
                      \right]>0,\qquad
 P_{vw}(\mathbf0)=0\quad(v\ne w).                       \tag{18}
\]

Every remaining vertex has an original incident edge, and each such
edge either remains in \(E_0\) or belongs to one selected star.
This proves strict positivity even at an isolated vertex of the
remaining forest.

The product of (14) and the full edge bounds similarly gives

\[
 |B_N(\mathbf x+i\mathbf y)|
 \le CN^A\exp N\left\{
 \Re P(\mathbf0)-c\sum_{v\in V_0}(1-\cos x_v)
                            +C_0\sum_{v\in V_0}y_v^2\right\},
                                                               \tag{19}
\]

with \(c>0\): every free coordinate occurs in at least one factor
with positive angular loss. There are finitely many factors, so take
the smallest permitted strip width and the minimum positive total
loss over the free vertices. Products of the holomorphic relative
errors are still \(1+O(N^{-1})\). Equations (16)–(19) verify
all hypotheses of
[the complex-phase long-filling theorem](research_long_fillings_complex_boundary_phase.md)
for the entire source (7).

For independent sufficiently large powers at the remaining vertices,
that theorem supplies a unique small stationary point \(\mathbf u_*\)
for

\[
 \mathcal F(\mathbf u)
 =P(\mathbf u)+\frac{i}{4\pi}\sum_{v\in V_0}n_vu_v^2
                         -i\sum_{v\in V_0}u_v.           \tag{20}
\]

Its coordinates have negative imaginary part, and
\(S=\mathcal F(\mathbf u_*)\). The leading coefficient is

\[
 D=\left(-\frac1{\pi i}\right)^r(2\pi)^{r/2}
       \frac{a(\mathbf u_*)\prod_{v\in V_0}\sin u_{*,v}}
            {\sqrt{\det[-\mathcal F''(\mathbf u_*)]}}
       \ne0.                                             \tag{21}
\]

The square root is the accretive Gaussian branch. The final power is
\(\alpha+3r/2=3/2\), and the exact unit scalar is

\[
 \Omega_N=q^{(N-1)^2w(D)/2}
       \left(\prod_{s\in S}\varepsilon_{s,N}\right)
       \left(\prod_{v\in V_0}C_{N,n_v}\right).            \tag{22}
\]

This proves (4), including the original framing and both level
parities. It remains to prove that its real action is the actual
knot-complement volume.

## 5. The complete partially filled exterior

Start with the original complete circle-tree exterior, whose edge
blocks are pairs of regular ideal octahedra. Keep every remaining
angle \(u_v=0\). At each selected vertex replace the right side
of (9) by \(i\lambda_s\), with independent
\(0\le\lambda_s\le1\). Because selected vertices are not
adjacent, these equations decouple on this slice. Every incident
edge is used by at most one selected star.

The geometric theorem constructs this entire product of positive
cone paths. Its ordered face maps are the original maps, not just
equalities between eigenvalues. On a shared free boundary their
compatibility depends on that boundary angle, which is zero throughout.
The meridian contribution there is
\(\psi_u(t_s,0)=0\), and its longitude period is also zero.
Thus every unselected auxiliary cusp and every original main cusp
remains complete. Tetrahedron positivity along the path preserves
the original edge-angle winding; the full logarithmic periods are
continued from the complete end rather than reset to principal values.

At a selected vertex, with its original carrier and integer coefficient,
those periods satisfy

\[
 U_s=-2\pi\sum_{v\sim s}\psi_t(t_s,0)-i\eta_st_s,
 \qquad V_s=2it_s,
 \qquad U_s+p_sV_s=-2\pi i\lambda_s.                    \tag{23}
\]

The core length is \(-2\Im t_s>0\). The original primitive
solid-torus completion therefore gives cone angle
\(2\pi\lambda_s\), becoming smooth at \(\lambda_s=1\).
Section 8 of
[the geometric proof](research_isolated_internal_vertex_geometry.md)
justifies this assembly also when several selected stars meet the
same unselected vertex.

Let \(Y'\) be the complete partially filled exterior at the end of
these paths. Its absolute volume is

\[
 \operatorname{Vol}(Y')
    =2e_0v_{\rm oct}+2\pi\sum_{s\in S}M_s
    =2\pi\Re P(\mathbf0).                              \tag{24}
\]

This equality has an absolute normalization. Along a selected cone
path, differentiation of its stationary action gives
\(d\Re G_{s,\lambda_s}/d\lambda_s=\Im t_s\).
Schläfli's formula for the actual positive block chain gives
the corresponding volume derivative \(2\pi\Im t_s\).
At the complete end a star of degree \(d_s\) contributes exactly
\(2d_sv_{\rm oct}=2\pi d_s\psi(0,0)\). Integrating these
identities and adding the untouched edge blocks proves (24), with
no undetermined additive constant and no repeated edge block.

## 6. Complete the remaining original primitive fillings

Each selected angle extends holomorphically as its neighboring free
angles move near zero. Its equation (9) remains fixed at unit charge,
so its original primitive filling stays smooth. Nondegeneracy was
proved for the entire selected geometric branch; positivity of its
finitely many shapes persists on a sufficiently small neighborhood
of the endpoint. The untouched edge blocks are positive there as well.

The envelope derivative of (10) is its explicit boundary derivative:
all terms containing a derivative of \(t_s(\mathbf u_s)\) cancel
by (9). Thus the remaining original periods are

\[
 U_v=-2\pi P_v-i\eta_vu_v,\qquad V_v=2iu_v,
 \qquad
 U_v+p_vV_v=-2\pi\left(P_v+\frac{in_v}{2\pi}u_v\right).
                                                               \tag{25}
\]

These are full periods continued from \(Y'\), with the original
integer slopes (1). Elimination has changed their analytic dependence
on the free angles, but has not changed the curves being filled.

For \(0\le c\le1\), solve

\[
      P_v(\mathbf u)+\frac{in_v}{2\pi}u_v=ic
                         \qquad(v\in V_0).              \tag{26}
\]

The contraction proof of the complex-phase theorem is uniform on this
charge interval. Increasing the fixed threshold \(B\), if necessary,
keeps the entire path inside the geometric neighborhood just described.
For \(c>0\) it has \(\Im u_v<0\). Equations (25)–(26)
then give the original primitive cone angles \(2\pi c\) and
positive lengths \(-2\Im u_v\). The original log-link and
solid-torus completion apply on every remaining auxiliary cusp.
Main cusps remain complete. At \(c=1\), this is the complete
hyperbolic metric on the knot complement specified by the original
strand tracing.

Set

\[
 \mathcal C(c)=P(\mathbf u(c))
     +\frac{i}{4\pi}\sum_{v\in V_0}n_vu_v(c)^2
                         -ic\sum_{v\in V_0}u_v(c).
\]

Stationarity gives
\(d\Re\mathcal C/dc=\sum_v\Im u_v(c)\). Schläfli's formula
for the assembled metric gives
\(d\operatorname{Vol}/dc=2\pi\sum_v\Im u_v(c)\).
The equality at \(c=0\) is (24). Integrating to one proves

\[
 \operatorname{Vol}(S^3\setminus K)
       =2\pi\Re\mathcal C(1)=2\pi\Re S,
\]

which is (5). Together with the nonzero coefficient in (4), this
proves the stated volume identity.

## 7. Relation to finite exceptions

This theorem covers short fillings at arbitrary original terminal
vertices with magnitude at least two, and a new collection of original
internal vertices, provided no two selected vertices are adjacent.
The remaining powers can grow independently. In particular it covers
infinite families lying outside the region where every original power
is long.

It does not yet supply the stability under every fixed partial filling
needed for finitely many exceptional assignments. An isolated internal
pair outside the explicitly listed cases and (2) still needs its own
whole-boundary theorem, unless an exact reduction supplies one.
Adjacent selected vertices are treated separately by
[the connected-cluster theorem](research_connected_short_filling_clusters.md),
under its own cumulative conditions; arbitrary short blocks remain
unsettled. Terminal powers zero and
\(\pm1\) have exact algebraic reductions, but are not silently
included in the present marked-template statement. Thresholds in (3)
may depend on all powers already fixed; no uniform bound over those
choices is asserted.
