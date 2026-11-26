# Long fillings with adjacent powers three and four

Research assembly, 7 November 2026. This note uses the complete
two-boundary theorem for the pair of powers three and four to allow
arbitrarily many such pairs in an original circle tree. The remaining
powers are independently sufficiently long. The adjacent short powers
are summed before any asymptotic approximation is made.

The statement concerns the original marked presentations and the
original Kashaev invariant. It does not establish stability under
arbitrary short partial fillings.

## 1. The allowed selected components

Fix an admissible original ordered circle-tree template \(\Gamma=(V,E)\)
with at least one edge, retaining its crossing disks, half-twist
carriers, reduced cut and closure.
The effective integer power at a vertex is

\[
                     n_v=\eta_v-2p_v,\qquad p_v\in\mathbb Z.
                                                               \tag{1}
\]

Choose a proper subset \(S\subset V\). Every connected component
of the induced subgraph on \(S\) is required to consist of two
adjacent vertices, each of degree two in the original tree. With
either order of its two distinct outside boundaries, the powers of
this component must be one of

\[
                  (3,4),\quad(4,3),\quad(-3,-4),\quad(-4,-3).
                                                               \tag{2}
\]

The original carriers must permit the chosen powers. The other
vertices, denoted by \(V_0=V\setminus S\), remain free. Different
selected components can meet the same free vertex, but they cannot
share a selected vertex or be joined by an edge between selected
vertices. There is no bound on their number as the fixed template
varies.

**Theorem 1.** For each fixed marked template and selection above,
there is an integer \(B\) such that every fixed assignment

\[
                       |n_v|\ge B\qquad(v\in V_0)
                                                               \tag{3}
\]

with the prescribed parities satisfies the original volume identity,
provided its original strand tracing gives one knot and no internal
closed component:

\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|\langle K\rangle_N|
                         =\operatorname{Vol}(S^3\setminus K).
                                                               \tag{4}
\]

The free powers can have unrelated magnitudes and signs. The entire
assignment is fixed before \(N\) tends to infinity, and the limit
uses all integer levels. The threshold may depend on the fixed
template, selection and marking.

## 2. The exact component polynomial

Write \(v(w)=(e_0(w),\ldots,e_{N-1}(w))^T\) for the original
Newton evaluation column, \(M_N\) for multiplication by the crossing,
and \(J_N\) for reversal. Set

\[
 A_{n,N}=J_NM_N^n,
 \qquad
 K_N(s,t)=v(-2\cos s)^Tv(-2\cos t).
                                                               \tag{5}
\]

The original trace satisfies
\((A_{n,N})_{ij}=\phi_N(R^ne_i e_j)\). For a selected component
with powers \(a,b\), its entire boundary polynomial is therefore

\[
 \begin{split}
 E_{a,b,N}(s,t)
 &=\phi_N^{(x)}\phi_N^{(y)}
   [R(x)^aR(y)^bK_N(s,x)K_N(x,y)K_N(y,t)]\\
 &=v(-2\cos s)^TA_{a,N}A_{b,N}v(-2\cos t).
 \end{split}                                                   \tag{6}
\]

To verify (6), expand the three finite edge sums and take the traces
in \(x,y\). Their coefficients are respectively
\(\phi_N(R^ae_i e_j)\) and \(\phi_N(R^be_j e_k)\).
Summing the common index gives the displayed matrix product. Every
first normal at a repeated root is part of the trace in this
calculation. There is no extra factor of \(N\).

The [full boundary theorem](research_mixed_three_four_full_boundary_kernel.md)
provides a fixed complex bidisk on which

\[
 E_{3,4,N}(s,t)
 =\kappa_N^3N^{-3/2}a_{34}(s,t)e^{NW_{34}(s,t)}
                           (1+O(N^{-1})),\qquad a_{34}(0,0)\ne0.
                                                               \tag{7}
\]

The error is holomorphic and uniform. The phase is separately even,
has strictly negative real Hessian at zero, and the complete finite
polynomial has the whole-period estimate

\[
 |E_{3,4,N}(x+iy,u+iv)|
 \le CN^d\exp N\{M_{34}-c(1-\cos x)-c(1-\cos u)
                                      +C_0(y^2+v^2)\},
                                                               \tag{8}
\]

where \(M_{34}=\Re W_{34}(0,0)\), \(c>0\), and the two
heights lie in a fixed strip. These are estimates for (6), rather
than for a selected term in a decomposition of it.

Commutativity of the original algebra gives \(A_{n,N}^T=A_{n,N}\).
Consequently \(E_{4,3,N}(s,t)=E_{3,4,N}(t,s)\). The established
identities \(\overline M_N=M_N^{-1}\) and real \(J_N,e_j\) give

\[
 E_{-a,-b,N}(s,t)
          =\overline{E_{a,b,N}(\bar s,\bar t)}.          \tag{9}
\]

Thus (7)--(8), including fixed ordinary derivatives, hold for all
four types in (2). Reversal exchanges the two boundary variables.
Simultaneous sign reversal conjugates the phase and amplitude and
inverts the unit scalar. Their real curvature remains positive
after the minus sign is taken. Since this collection is finite,
all disks, positive losses and strip widths may be chosen in common.

## 3. Assemble the exact source at the remaining vertices

Let \(E_0\) be the original edges whose two endpoints lie in
\(V_0\), and write \(r=|V_0|\). Each selected component has two
distinct outside vertices: identifying them would create a cycle
in the original tree. Write these vertices as \(l(C),r(C)\).
After taking only the selected traces, the remaining entire source is

\[
 B_N(\mathbf u)=
 \prod_{vw\in E_0}K_N(u_v,u_w)
 \prod_C E_{a_C,b_C,N}(u_{l(C)},u_{r(C)}).
                                                               \tag{10}
\]

This identity follows by commuting finite traces in distinct
variables. It retains the full polynomial in each free ordinary
color, whose degree is at most \(d_v(N-1)\). It is not reduced
to values at distinct spectral roots.

Write \(\psi\) for the original bare-edge phase. The local phase
and amplitude of (10) are

\[
 F(\mathbf u)=\sum_{vw\in E_0}\psi(u_v,u_w)
              +\sum_C W_{a_C,b_C}(u_{l(C)},u_{r(C)}),
 \qquad a(\mathbf u)=\prod_e a_e\prod_C a_C.
                                                               \tag{11}
\]

The amplitude is nonzero on a sufficiently small common polydisk.
All phases are separately even. Their Hessians at zero are diagonal
in their boundary angles and have negative real diagonal entries.
Every free vertex has an original incidence, so the aggregate Hessian
has a strictly negative real diagonal at every free variable.

Multiplying (8) and the corresponding bare-edge bounds gives the
whole-period quadratic-strip estimate for (10). The positive
angular losses add at shared free vertices. The separate degree
bound and all first normals are precisely those allowed in the
[complex-phase long-filling theorem](research_long_fillings_complex_boundary_phase.md).

If there are \(k\) selected pairs, contracting each of their
length-three paths to one edge produces a tree on \(r\) vertices.
Hence \(|E_0|+k=r-1\). Each factor in (10) has power
\(N^{-3/2}\), and thus

\[
 B_N=\epsilon_N N^{-3(r-1)/2}
              a(\mathbf u)e^{NF(\mathbf u)}(1+O(N^{-1})).
                                                               \tag{12}
\]

Applying the remaining \(r\) original traces at (3) now gives

\[
 Z_N=\Omega_N N^{3/2}D(\mathbf n)
           e^{N\mathcal S(\mathbf n)}(1+O_{\mathbf n}(N^{-1})),
 \qquad |\Omega_N|=1,\qquad D(\mathbf n)\ne0,             \tag{13}
\]

where \(\mathcal S\) is the stationary value of

\[
 F(\mathbf u)+\sum_{v\in V_0}
           \left(\frac{in_vu_v^2}{4\pi}-iu_v\right).
                                                               \tag{14}
\]

In particular the original finite source has a nonzero coefficient
after all its remaining sums and first normals are taken. The power
of \(N\) is \(-3(r-1)/2+3r/2=3/2\). This deduction uses the
whole-boundary estimates (8), not just the value of (7) at zero.

## 4. The original periods and the volume

The [marked geometric boundary theorem](research_mixed_geometric_boundary_germ.md)
identifies \(W_{34}\), throughout its boundary germ, with the
stationary original geometric action up to its recorded purely
imaginary constant. It retains positive original cells, face
identifications, the primitive integer filling periods and the
absolute real volume anchor. Reversing the path exchanges its two
boundary labels and uses the same identities.

For simultaneous sign reversal, the geometric variables transform by

\[
                  t_v^-=-\overline{t_v^+},
             \qquad r_{v,e}^-=-\overline{r_{v,e}^+}.
                                                               \tag{15}
\]

At a nonzero prescribed outside angle \(\theta\), take the positive
germ at \(-\overline\theta\) before applying (15). The resulting
negative germ has the prescribed angle \(\theta\). Separate evenness
of its boundary action reconciles this continuation with (9).

At each selected vertex its original equation transforms as

\[
 n_vt_v^++2i\sum_e r_{v,e}^+=2\pi
 \quad\Longrightarrow\quad
 (-n_v)t_v^-+2i\sum_e r_{v,e}^-=2\pi.                   \tag{16}
\]

Both sides have negative imaginary selected angles. The positive
edge-root condition is preserved under (15), exactly as in the
[signed component calculation](research_three_chain_short_filling_stability.md),
Section 3; that calculation applies to each vertex separately and
does not require its neighboring power to be equal. The action
conjugates as in (9). Thus all four component types have their
original marked geometric boundary germs.

At zero free angles, the components and untouched edges meet along
their original complete outside boundaries. Their absolute real
actions add. The long-filling theorem keeps the new critical point
and its charge path in this fixed common geometric neighborhood
once (3) is sufficiently strong. The original primitive return
identities therefore continue with every selected slope fixed and
each free slope equal to (1). Positive core lengths and the original
main-cusp completeness persist.

The marked completion and Schläfli argument in Sections 4--5 of
the signed component theorem consequently identify

\[
              2\pi\Re\mathcal S(\mathbf n)
                        =\operatorname{Vol}(S^3\setminus K).
                                                               \tag{17}
\]

The original finite-source identity changes (13) to the reduced,
zero-framed Kashaev invariant only by its recorded unit framing
factor. Taking the logarithm of its absolute value proves (4).

## 5. Relation to the finite-exceptions objective

The number of selected pairs is arbitrary, and the free vertices
can branch. What is fixed in Theorem 1 is the finite template before
the level limit is taken. This is therefore a composition theorem
for a class of partially filled templates, not a list of separate
closed-knot calculations.

It does not allow an arbitrary adjacent short word, or a selected
component containing a branching vertex. Nor does it show that the
remaining untreated assignments of any fixed template form a finite
set. The finite-branching deduction still needs an applicable source
theorem or exact reduction at every short partial assignment it
encounters. The present theorem supplies one additional kind of
selected component for that deduction.
