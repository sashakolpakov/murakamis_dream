# Higher window faces and their weighted edge-cover bound

Private written proof, 17 November 2026.

A window change on one endpoint of a repaired edge has zero full
line data at its unchanged endpoint window. It is therefore killed
by that neighboring closed cell trace. Applying this observation
to a tensor opening removes every face whose opened vertex set has
an isolated vertex in the induced represented graph.

Mixed faces do remain. A single edge already has a two-vertex
corner, so tree acyclicity does not cancel all internal currents.
Their coefficients nevertheless contain one exponentially small
factor for each edge in an edge cover of the opened vertices.
This estimate is before the remaining original closing. All outer
pieces, uncovered rows and free polynomial factors remain.

## 1. Fixed source and exact tensor openings

Let \(G=(V,E)\) be a fixed finite loopless graph of represented
same-index edges. The conclusions apply in particular to a finite
tree. Repeated edges are allowed and counted separately. Other
original factors, including edges not represented here, are kept
in a spectator \(S_N(\mathbf z;\mathbf u)\). It is independent of
all window labels and holomorphic at the physical rows where it is
traced. The external variables \(\mathbf u\) remain ordinary free
variables.

At vertex \(v\), take a finite consecutive partition into trace
cells \(B_{v,i}\), each contained in an enlarged short repair
window \(I_{v,i}\). Retain the original node multiplicities:
double spectral nodes have value and first normal, and the odd
simple node has its value only. All window families and buffers
are supplied as in the short spectral repair theorem.

For \(e=vw\), let \(K^e_{i,j,N}(z_v,z_w)\) be its repaired
representative. With the original phase \(\Psi_e\), the family has
one common normalized baseline:
\[
 K^e_{i,j,N}=e^{N\Psi_e}(h_{e,N}+r^e_{i,j,N}),\qquad
 |h_{e,N}|\le e^{o(N)},\qquad
 |r^e_{i,j,N}|\le e^{-\kappa_eN+o(N)},\quad \kappa_e>0.
 \tag{1}
\]
The estimates hold on common fixed buffered product compacts,
with fixed derivatives. A decrease of the finitely many positive
rates is permitted once.

Crucially, at \(k\in I_{w,j}\), the exact identities
\[
 K^e_{i,j,N}(z,c_k)=F_k(z),\qquad
 \partial_wK^e_{i,j,N}(z,c_k)=\widehat G_k(z)
                                      \quad(\nu_k=2)
 \tag{2}
\]
hold as holomorphic functions of \(z\), independently of \(i\).
There are transposed identities independently of \(j\).
At joint physical pairs the required mixed jets are the original
ones. The normal in (2) is the pinned sharp representative; it is
not identified with the ordinary free-color normal polynomial.

Write the labeled source family as
\[
 F_{\mathbf i,N}(\mathbf z;\mathbf u)
   =S_N(\mathbf z;\mathbf u)
       \prod_{e=vw}K^e_{i_v,i_w,N}(z_v,z_w).
 \tag{3}
\]
Its covered original tensor trace is unchanged by this replacement,
by the full joint-jet theorem. All tuples with at least one row
outside the covered cells constitute a separate unchanged source
\(Z_{N,\mathrm{rest}}\).

We first use fixed product contours. Contour choices in one vertex
do not depend on another vertex's window label. The exact cell
opening in the overlap theorem defines linear operators
\[
                         D_v=H_v+I_v.                 \tag{4}
\]
Here \(D_v\) sums the original closed traces on the cells \(B_{v,i}\).
The operator \(I_v\) sums the internal common-side integrals, with
their original normalizations, applied to the difference of the two
adjacent window labels. Choose its orientation so this difference
is left minus right. The operator \(H_v\) retains every other piece
of the opened cell contours, including all top pieces and all outer
connectors. Thus (4) deletes no boundary current.

For example, the even spectral lower-lens opening pairs the two
angular lifts, and its internal side is precisely the joined
quotient seam of the pinned overlap theorem. Its odd central node
has the single original value contribution. Equation (4) also
works with the original closed angular contours; it does not
require assigning an extra normal at a simple node.

Operators at different vertices commute: their label sums and
differences are finite, their integrations are over the fixed
product chains, and their full local residue functionals act in
different variables. This is the tensor setting used below.
A subsequent coupled homotopy must retain all its additional
faces; no commutation of unrecorded moving-boundary operators is
being asserted.

The covered trace and the fully opened term are
\[
 Z_{N,\mathrm{cov}}=\Big(\prod_{v\in V}D_v\Big)F_N,\qquad
 Z_{N,H}=\Big(\prod_{v\in V}H_v\Big)F_N .
 \tag{5}
\]
The latter notation includes products of outer pieces as well as
top pieces. It is not a top-only parent-height integral.

## 2. Exact higher faces with a closed complement

For a nonempty \(A\subseteq V\), define the actual higher-face term
\[
 C_{A,N}=
       \Big(\prod_{v\in A}I_v\Big)
       \Big(\prod_{w\notin A}D_w\Big)F_N .
 \tag{6}
\]
Every vertex outside \(A\) is still closed on its selected cells.

**Theorem 1.** Exactly
\[
 \boxed{\quad
 Z_{N,\mathrm{cov}}
    = Z_{N,H}
       +\sum_{\varnothing\ne A\subseteq V}
                          (-1)^{|A|+1}C_{A,N}.
 \quad}                                                \tag{7}
\]
If the induced represented graph \(G[A]\) has an isolated vertex,
then \(C_{A,N}=0\), with every original spectator and full product
normal retained.

**Proof of the identity.** Expand
\[
 \prod_v H_v=\prod_v(D_v-I_v)
   =\sum_{A\subseteq V}(-1)^{|A|}
         \Big(\prod_{v\in A}I_v\Big)
         \Big(\prod_{w\notin A}D_w\Big).
 \tag{8}
\]
The empty term is \(\prod_vD_v\). Rearrangement gives (7).
The vanishing assertion is proved below together with the sharper
edge expansion. \(\square\)

Fix one cut for each \(v\in A\), and hold every other label fixed.
Let \(\delta_v\) be the difference at that cut, with the convention
in (4). A repeated product rule for finite differences gives an
exact expression for
\[
                  \delta_A\prod_e K^e,\qquad
                     \delta_A=\prod_{v\in A}\delta_v .
 \tag{9}
\]
Here is a version that keeps all multiple-incidence terms. Give each
cut variable a Boolean coordinate \(\epsilon_v\in\{0,1\}\), with
value one denoting the first term in its difference. For each edge,
\[
 K^e(\boldsymbol\epsilon)
   =\sum_{T\subseteq e\cap A}
              \epsilon_T\,k_{e,T},\qquad
 \epsilon_T=\prod_{v\in T}\epsilon_v,\qquad
 k_{e,T}=\delta_TK^e\big|_{\epsilon_{(e\cap A)\setminus T}=0}.
 \tag{10}
\]
Multiply these finite identities and use \(\epsilon_v^2=\epsilon_v\).
The coefficient of \(\epsilon_A\), equivalently the full difference,
is
\[
 \boxed{\quad
 \delta_A\prod_eK^e
  =\sum_{\substack{T_e\subseteq e\cap A\\
                         \bigcup_eT_e=A}}
                         \prod_e k_{e,T_e}.
 \quad}                                                \tag{11}
\]
Thus a vertex difference may occur on several incident factors;
none of those terms has been discarded.

Call an edge changed when \(T_e\ne\varnothing\). Suppose such an
edge \(e=vw\) meets \(w\notin A\). Then \(T_e=\{v\}\), and (2)
gives
\[
 k_{e,\{v\}}(z_v,c_k)=0,\qquad
 \partial_w k_{e,\{v\}}(z_v,c_k)=0
                         \quad(k\in I_{w,i_w},\ \nu_k=2).
 \tag{12}
\]
These are identities in every remaining complex variable. At the
odd simple node only the first identity is needed. Multiplication
by every other incident factor and by \(S_N\) preserves the zero
value and zero first normal: the full Leibniz rule has no surviving
term. Therefore the closed \(w\)-cell trace kills this summand
before any estimate or any other integration.

It follows that in (6),(11) all changed edges may be restricted to
\(E(G[A])\). Their endpoint subsets still cover \(A\). If a vertex
of \(G[A]\) is isolated, no such assignment exists, proving the
vanishing assertion of Theorem 1.

Equivalently, every discarded term is in an unchanged neighbor's
full window ideal
\[
 \prod_{k\in I_{w,i_w}}(z_w-c_k)^{\nu_k}\,\mathcal O.
 \tag{13}
\]
This is stronger than matching only shared rows at the opened cut.
It uses the complete line identity (2), and is valid only while
the indicated neighbor remains closed. Replacing that closed trace
by a top path alone loses the annihilation and produces the higher
faces in (7).

## 3. Why a single-edge corner remains

The two-line repair formula makes the smallest surviving face
explicit. For one edge, let \(\mathscr L_{v,i}\) and
\(\mathscr L_{w,j}\) be its normalized spectral Hermite operators.
Its formula is
\[
 e^{-N\Psi_e}K^e_{i,j}
       =h_e+E_{v,i}+E_{w,j}-E_{vw,i,j}.
 \tag{14}
\]
The first correction depends only on \(i\), the second only on
\(j\). Let \(c_{kl}^{ab}\) be its actual compatible mixed error
data. On the finite unions of the windows choose the tensor
Hermite polynomial \(\mathcal C_e(z,w)\) with these data. It is
used only for this algebraic identity; no norm bound is assigned
to that possibly large union interpolation. Then exactly
\[
             E_{vw,i,j}
                 =\mathscr L_{v,i}\mathscr L_{w,j}\mathcal C_e.
 \tag{15}
\]
Consequently the actual double jump is
\[
 \boxed{\quad
 \delta_v\delta_wK^e
   =-e^{N\Psi_e}
       (\mathscr L_{v,i}-\mathscr L_{v,i+1})
       (\mathscr L_{w,j}-\mathscr L_{w,j+1})\mathcal C_e .
 \quad}                                                \tag{16}
\]
It is one mixed correction, not a product of two independently
small errors.

For a graph consisting of this edge, with any original
window-independent spectator, the two singleton terms in (7)
vanish by (12). Thus
\[
                    Z_{N,\mathrm{cov}}=Z_{N,H}-C_{\{v,w\},N}.
 \tag{17}
\]
The coefficient (16) remains in that corner.

There is no interpolation identity setting (16) to zero. Indeed,
for distinct windows choose a polynomial \(p\) whose prescribed
jets vanish on one window and not on the other. Then
\((\mathscr L_{v,i}-\mathscr L_{v,i+1})p\ne0\); make the same
choice \(q\) at the second endpoint. For mixed data represented
by \(p(z)q(w)\), the right side of (16) is nonzero. Such data
satisfy the ordinary two-line compatibility conditions. This
shows that those conditions and graph acyclicity do not force
annihilation. It is not a lower bound or a nonvanishing claim for
the particular original kernel's integrated corner. Any further
cancellation for that kernel requires an additional source identity.

## 4. The weighted edge-cover gain

For \(A\ne\varnothing\) define
\[
 \tau_\kappa(A)=
 \min\left\{\sum_{e\in E'}\kappa_e:
       E'\subseteq E(G[A]),\ 
       A=\bigcup_{e\in E'}e\right\},
 \tag{18}
\]
with value \(+\infty\) if no such cover exists. Put
\(\Psi_{\mathrm{rep}}=\sum_{e\in E}\Psi_e\).

**Theorem 2.** After discarding the terms annihilated by the closed
complement in Section 2, the kernel coefficient of every fixed
cut tuple in \(C_{A,N}\) has a representative \(R_{A,N}\) satisfying
\[
 \left|e^{-N\Psi_{\mathrm{rep}}}R_{A,N}\right|
       \le \exp\{-N\tau_\kappa(A)+o(N)\}.
 \tag{19}
\]
The estimate holds on the admitted common buffered product
compacts, including fixed derivatives. It is before multiplication
by the unbounded original spectator and before the remaining
closing or seam integrations.

**Proof.** In (10), an unchanged edge has normalized bound
\(e^{o(N)}\). For any nonempty \(T\), the common baseline in (1)
cancels from \(\delta_TK^e\). A single jump is a difference of two
errors; a double jump is a signed sum of four errors. Both obey
\[
            |e^{-N\Psi_e}k_{e,T}|
                           \le e^{-\kappa_eN+o(N)}.    \tag{20}
\]
The surviving assignments in (11) have all changed edges in
\(G[A]\), and their endpoint subsets cover \(A\). The changed
edges therefore form an edge cover of \(A\). Multiplying (20)
and the unchanged-edge bounds gives the exponent at least (18).
There are only finitely many vertices, edges and cuts, so the
sum changes only the subexponential factor. Fixed derivatives
follow from the buffered estimates and the finite product rule.
No amplitude is inverted. \(\square\)

If all available edge rates are at least \(\kappa>0\), let
\(\nu(G[A])\) be the maximum matching size of the induced graph.
When it has no isolated vertices,
\[
                   \tau_\kappa(A)
                        \ge\kappa\bigl(|A|-\nu(G[A])\bigr).
 \tag{21}
\]
For equal rates this is equality. To verify the combinatorial
identity, a maximum matching covers \(2\nu\) vertices. Add one
incident edge for each unmatched vertex. No two unmatched
vertices are adjacent, so this yields an edge cover of size
\(|A|-\nu\). Conversely, in any edge cover with \(c\) nontrivial
connected components, its edge count is at least \(|A|-c\),
and choosing an edge in each component gives a matching of size
\(c\le\nu\). This proves the reverse inequality.

In particular a forest face gains at least
\(\kappa\lceil|A|/2\rceil\), and disconnected components add their
weighted cover costs. A single-edge mixed face has only one
edge rate. Counting its two endpoint jumps as two exponential
factors would contradict (16).

## 5. Original source scope

The full source is \(Z_{N,\mathrm{rest}}+Z_{N,\mathrm{cov}}\).
Its uncovered rows and every free ordinary polynomial remain
unchanged. All equations above retain the original signed
crossings, the exact local trace normalizations, mixed product
normals and simple-node values.

The equality in (7) is constructive: it replaces internal faces
with an alternating sum whose complement is still closed, and
then removes the terms killed by those exact closed traces.
It does not replace \(H_v\) by only its top contribution, nor
does it set the surviving mixed faces to zero. A further coupled
contour deformation retains all its endpoints and boundary faces.

The estimate (19) controls a kernel coefficient, not the norm
of the remaining joint closing. In particular it compares no
unspecified \(\kappa_e\) with a parent energy deficit. To obtain
a positive-parent estimate one still needs the actual action
and spectator budgets for the surviving faces and outer pieces,
or a further coherent cancellation among them.

Complete direct sources used are:

* [Short spectral window repair](research_short_spectral_window_repair.md),
  SHA256 581ccd3ec9232a6aa1f42172fcff856f94a6d76efccc001bd411cf2243de2550:
  exact two-line and mixed data, the common baseline, the
  \(E_v+E_w-E_{vw}\) formula and its buffered error bound.
* [Overlapping windows and seam transport](research_overlapping_spectral_window_seam_transport.md),
  SHA256 b19521e052b2e5db60abed1a284600467c7df56e319f4ebd8b29213ccfd481c7:
  exact tensor cell traces, one-vertex window differences,
  shared-node division, oriented openings and every outer face.

Only written mathematics, complete source reads and metadata hashes
are used. No mathematical program, numerical calculation, test or
compilation is run. Adopted notes and public manuscripts are unchanged.
