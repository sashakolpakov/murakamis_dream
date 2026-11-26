# Exact collective reduction of original cutoff currents

Private written proof, 15 November 2026.

The midpoint forcing of an original low Newton kernel has one low
factor at its tail and one radical factor at its head. Products of
these forcings have more cancellation than the generic matching or
polynomial-norm bound records. At odd levels only outward stars can
remain, and their branching centers are evaluated at the complete
spectral value. At even levels internal vertices are pinned to one
double node; only a root can retain a spectator normal.

These are identities for the whole original contraction, with its
ordinary boundary polynomial retained. They do not show that the
remaining smaller-component rates lie below the geometric rate, or
that every complementary contour current is one of these forcings.

## 1. The actual cutoff and the two local polynomials

Put
\[
 N\ge2,\quad D=N-1,\quad m=\lfloor N/2\rfloor,\quad L=D-m,
 \quad q=e^{\pi i/N},\quad \eta=(-1)^D,
\]
\[
 s_j=2\sin(j\pi/N),\quad S_j=\prod_{h=1}^j s_h,\quad S_0=1,
 \quad c_a=2\cos((2a+1)\pi/N),
\]
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 e_j(z)=S_j^{-2}\prod_{a<j}(c_a-z),\qquad
 \mathcal A_N=\mathbb C[z]/(P_N).
 \tag{1}
\]
The original trace and crossing are
\[
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f,\qquad
 R(c_a)=\kappa(-1)^a q^{a(a+1)},\quad
 \kappa=q^{D^2/2}.
 \tag{2}
\]
All powers of \(R\), including negative ones, are in the full Hermite
algebra. Its physical values have modulus one.

Write
\[
 A=e_L,\qquad B=e_{L+1},\qquad
 K_N^{\rm low}(z,w)=\sum_{j=0}^L e_j(z)e_j(w).
\]
The original difference identity is
\[
 (w-\mathscr L_N^{(z)})K_N^{\rm low}(z,w)
                  =-s_{L+1}^2 A(z)B(w).
 \tag{3}
\]
Here \(\mathscr L_N e_j=c_je_j-s_j^2e_{j-1}\); (3) follows
by telescoping the Newton multiplication recurrence. This is the
literal forcing, not an arbitrary rank-one replacement of a kernel.

For later use retain the original radical weights
\[
 b_{ra}=(-1)^{r+a}
       \frac{s_{2a+1}S_r^2}{S_{r-a}S_{r+a+1}}\quad(0\le a\le r<m).
 \tag{4}
\]
The complete first-normal contraction gives
\[
 \phi_N(R^n Bf)
      =\sum_{a=0}^{m-1}b_{m-1,a}R(c_a)^n f(c_a),\qquad
 |b_{ra}|\le2.
 \tag{5}
\]
In particular (5) consumes the original normal in \(B\); it does
not discard a spectator derivative.

## 2. Odd levels: exact star centers

Suppose \(N=2m+1\). Let \(\Pi_-\) be the spectral idempotent with
value one at the simple node \(-2\), and zero value and first normal
at every double node.

**Lemma 1.** In the physical algebra,
\[
 B^2=AB=0,\qquad A^r=\Pi_-\quad(r\ge2).
 \tag{6}
\]
For every ordinary spectator \(f\) and every signed integer \(n\),
\[
 \phi_N(R^nA^rf)=R(-2)^nf(-2)\quad(r\ge2).
 \tag{7}
\]
The remaining single low insertion is also a value-only observation:
\[
 \phi_N(R^nAf)=R(-2)^nf(-2)
    +\sum_{a=0}^{m-1}(-1)^{m+a}2\cos(t_a/2)
                         R(c_a)^nf(c_a),\qquad
 t_a=\pi-\frac{(2a+1)\pi}{N}.
 \tag{8}
\]
The total absolute weight in (8) is at most \(N\).

**Proof.** The polynomial \(A=e_m\) vanishes at every double
node and has \(A(-2)=1\). The latter follows from
\(S_m^2=N\) and \(\prod_{a<m}(c_a+2)=N\). Thus every
\(A^r\), \(r\ge2\), has the full data of \(\Pi_-\).
The radical \(B=e_{m+1}\) vanishes at all physical nodes.
Consequently \(B^2=0\), and at each double node the first normal
of \(AB\) is zero because \(A\) has value zero there. Its simple
value is zero as well. Hermite uniqueness gives (6), and the
original simple-node trace gives (7).

For (8), the Frobenius identity
\(\phi_N(e_i e_j)=\delta_{i+j,D}\) says that the answer is the
coefficient of \(e_m\) in \(R^nf\). Its first \(m+1\) Newton
nodes are all distinct, including \(-2\). Put
\(Q(z)=\prod_{a<m}(z-c_a)\). Divided differences give the
coefficient at a double node as
\[
 \frac{(-1)^mN}{(c_a+2)Q'(c_a)}
                         =(-1)^{m+a}2\cos(t_a/2),
\]
and the coefficient at \(-2\) as one. The displayed equality
follows from
\(Q=U_m(z/2)-U_{m-1}(z/2)\), or directly by differentiating
its trigonometric expression:
\[
 Q'(c_a)^{-1}=\frac4N(-1)^a\sin t_a\sin(t_a/2).
\]
This proves (8), including the simple node. There are \(m\)
double-node weights of modulus at most two and one simple weight.
\(\square\)

Thus a multiple low insertion is not merely bounded at the complete
point: it is the exact complete-value functional. Formula (8) also
explains why no spectator normal remains in the odd single-tail case.

## 3. Even levels: one central double block

Suppose \(N=2m\). Put
\[
 c_*=c_{m-1}=-2\cos(\pi/N),\quad s=s_1,\quad
 E=\frac2s,\quad
 \tau=\sum_{a=0}^{m-2}\frac1{c_*-c_a}.
 \tag{9}
\]
The empty sum at \(N=2\) is zero. Let \(\Pi_*,\Xi_*\) have,
at \(c_*\), value/normal data \((1,0),(0,1)\), respectively,
and zero data at every other double node.

**Lemma 2.** In the full physical algebra,
\[
 B^2=0,\qquad
 A^r=E^r\Pi_*+rE^r\tau\Xi_*\quad(r\ge2),\qquad
 A^rB=-\frac{E^{r+1}}4\Xi_*\quad(r\ge1).
 \tag{10}
\]
Consequently
\[
 \boxed{\ \phi_N(R^nA^rBf)=E^{r-1}R(c_*)^nf(c_*)
                                                \quad(r\ge1).\ }
 \tag{11}
\]
For \(r\ge2\),
\[
 \phi_N(R^nA^rf)=
  \eta E^rR(c_*)^n
   \left[s^2 f'(c_*)+
     \left(rs^2\tau+\frac{ins}{2}-c_*\right)f(c_*)\right].
 \tag{12}
\]
For one low insertion the exact formula is
\[
 \begin{split}
 \phi_N(R^nAf)={}&
    \sum_{a=0}^{m-2}
       \frac{4b_{m-1,a}}{c_*-c_a}R(c_a)^nf(c_a)\\
 &+\eta E R(c_*)^n
   \left[s^2 f'(c_*)+
       \left(s^2\tau+\frac{ins}{2}-c_*\right)f(c_*)\right].
 \end{split}
 \tag{13}
\]

**Proof.** The only nonzero physical value of \(A=e_{m-1}\)
is \(A(c_*)=E\), and \(A'(c_*)=E\tau\). At all other
nodes \(A\) has a simple zero. The Newton recurrence is
\[
                         B(z)=\frac{c_*-z}{4}A(z).
 \tag{14}
\]
It gives \(B'(c_*)=-E/4\). Values and normals now prove
(10). The original residue at a double root is
\[
                 \eta\{(4-c^2)h'(c)-ch(c)\}.
 \tag{15}
\]
At \(c_*\), \(4-c_*^2=s^2\), \(\eta=-1\), and the
actual crossing normal is
\[
                  (R^n)'(c_*)/R(c_*)^n=\frac{in}{2s}.
 \tag{16}
\]
Apply (15) to (10). Since
\(-\eta s^2E^{r+1}/4=E^{r-1}\), this gives (11)--(12).
For a different node, (14) relates the surviving normal of \(A\)
to that of \(B\) by \(4/(c_*-c_a)\). Equation (5) therefore
gives the first line of (13); (15)--(16) give its second line.
At \(N=2\), \(A=1\), \(B=-z/4\), \(c_*=0\); the same
identities hold with the empty sums already specified. \(\square\)

In particular a vertex with one incoming radical factor and any
positive number of outgoing low factors becomes a pure value
observation. Only a vertex with no incoming factor can retain a
spectator normal, and it retains that normal only at \(c_*\).

## 4. The exact whole-source reduction

Let \(G=(V,\mathcal E)\) be a fixed finite simple graph carrying
the original same-index kernels
\(K_N(z,w)=\sum_{j=0}^D e_j(z)e_j(w)\). Let \(I\subseteq V\)
be its traced vertices with fixed signed powers \(n_v\).
Variables at \(V\setminus I\) remain ordinary boundary variables;
they are not reduced modulo \(P_N\).

Choose a nonempty subset \(F\) of edges with both endpoints in
\(I\), and orient each chosen edge once. Replace precisely these
edges by (3), leaving every other edge full. Call the resulting
original contraction \(\mathscr J_{F,N}\). For \(v\in S=V(F)\),
write \(a_v\) for its outdegree and \(b_v\) for its indegree in
the chosen orientation. Define the actual joint spectator
\[
 G_{F,N}(\mathbf z_S,\mathbf u)=
 \left(\prod_{v\in I\setminus S}\phi_N^{(z_v)}\right)
 \left[
   \prod_{v\in I\setminus S}R(z_v)^{n_v}
   \prod_{\{v,w\}\in\mathcal E\setminus F}K_N(z_v,z_w)
 \right].
 \tag{17}
\]
All unforced edges remain in (17), including edges between two
vertices of \(S\) and multiple incidences at a shared free variable.
Put
\[
 \mathcal O_v(f)=\phi_N(R^{n_v}A^{a_v}B^{b_v}f).
\]
Distributivity gives the source identity
\[
 \boxed{\quad
 \mathscr J_{F,N}=(-s_{L+1}^2)^{|F|}
                    \left(\prod_{v\in S}\mathcal O_v\right)G_{F,N}.
 \quad}
 \tag{18}
\]
The local rules (5)--(13) apply coefficientwise to this joint
polynomial. They retain all original crossing phases, every first
normal, and every fixed ordinary derivative in \(\mathbf u\).

**Theorem 3.** The following are exact collective reductions.

1. If \(b_v\ge2\) at any vertex, then \(\mathscr J_{F,N}=0\)
   at every level.
2. At odd levels it is also zero if \(a_vb_v>0\) at any vertex.
   Therefore any forcing component not already killed by these rules
   is an outward star. Its leaves use (5). A center with one outgoing
   edge uses (8); a center with at least two uses the complete
   evaluation (7). All these observations are value-only.
3. At even levels a forcing component not already killed is either
   an outward rooted tree, or a directed cycle with outward trees
   attached. In a rooted component, each nonroot internal vertex
   uses (11), each leaf uses (5), and only the root uses (12) or
   (13). In a cyclic component every internal vertex uses (11)
   and every leaf uses (5); there is no spectator derivative.

In the tree case of the original question only the rooted-tree
alternative in item 3 is possible. These support rules are necessary;
they do not assert that the remaining coherent contraction is nonzero.

**Proof.** Both \(B^2=0\) and, at odd levels, \(AB=0\)
remain zero after multiplication by the original crossing and
arbitrary spectators. This proves the vanishing statements.

A finite connected forcing graph with indegree at most one has at
most as many edges as vertices. If it is a tree, its indegrees
sum to one less than its vertex count: precisely one vertex has
indegree zero, and all edges point away from that root. If it has
a cycle, it is unicyclic and every vertex has indegree one. The
cycle is therefore directed, and the remaining edges point away
from it. At odd levels a vertex of indegree one cannot have an
outgoing edge; the only remaining components are outward stars.
Apply the local formulas to (18). In particular (11) consumes
the normal at every nonroot internal vertex. \(\square\)

For example, a pure directed cycle at even levels has \(a_v=b_v=1\)
at every vertex. Since \(s_{L+1}=s_m=2\), its entire contribution,
with any joint exterior, is exactly
\[
 \mathscr J_{F,N}
   =(-4)^{|F|}
       \left(\prod_{v\in S}R(c_*)^{n_v}\right)
                        G_{F,N}(c_*,\ldots,c_*;\mathbf u).
 \tag{19}
\]
At odd levels this same forcing is zero. This identity does not
remove any unforced edge from \(G_{F,N}\).

## 5. Joint radical and cutoff sectors

The same local identities apply when radical edges and cutoff
forcings are present together. This is more restrictive than treating
the two expansions separately.

Write \(h_r=e_{D-r}\), \(0\le r<m\), so the full high edge is
\[
                     H_N(z,w)=\sum_{r=0}^{m-1}h_r(z)h_r(w).
\]
At a double node \(c_a\), \(h_r\) has zero value and its first
normal vanishes unless \(a\le r\). It vanishes at the odd simple
node as well. Therefore the exact identities in
\(\mathcal A_N^{(z)}[w]\), imposing the relation only in the
traced variable, are
\[
 h_r e_j=0\quad(j>r),\qquad
 h_r(z)K_N(z,w)=h_r(z)\sum_{j=0}^{r}e_j(z)e_j(w).
 \tag{19a}
\]
Indeed \(e_j(c_a)=0\) when \(a\le r<j\), so every required
normal of the product vanishes. The second variable \(w\) stays
an ordinary free polynomial. These are the local index restrictions
already implicit in the original physical radical contraction.
In particular,
\[
 \begin{array}{ll}
 A^a h_r=0\quad(a\ge1,\ 0\le r<m),&N\text{ odd},\\
 A^a h_r=0\quad(a\ge1,\ r<m-1),\qquad
 A^a h_{m-1}=A^aB,&N\text{ even}.
 \end{array}
 \tag{19b}
\]
All products of two radical factors are zero at either parity.

Choose disjoint sets of edges: oriented cutoff edges \(F\) and
unoriented radical edges \(H\), with every endpoint traced.
Replace the edges of \(F\) by (3), the edges of \(H\) by the
full \(H_N\), and keep every other original edge. Put
\(S=V(F\cup H)\), and let \(G_{F,H,N}\) be (17) with
\(\mathcal E\setminus(F\cup H)\) in place of
\(\mathcal E\setminus F\). The exact joint sector is
\[
 (-s_{L+1}^2)^{|F|}
 \sum_{\mathbf r\in\{0,\ldots,m-1\}^{H}}
 \left(\prod_{v\in S}
   \phi_N^{(z_v)}
     \left[R(z_v)^{n_v}A(z_v)^{a_v}B(z_v)^{b_v}
                 \prod_{\substack{e\in H\\v\in e}}h_{r_e}(z_v)
                    \,\,\cdot\,\right]\right)G_{F,H,N}.
 \tag{19c}
\]
Here \(a_v,b_v\) count only the cutoff edges. A radical edge has
the same label \(r_e\) at both ends. All unchosen edges stay in
the joint spectator; different chosen-edge components need not
be independent in that spectator.

**Theorem 4.** The following reductions hold before any estimate.

* At odd levels, a radical edge sharing a vertex with any other
  radical edge or any cutoff edge makes the sector zero.
  Thus the radical edges form a matching disjoint from every
  cutoff vertex, and the cutoff components obey Theorem 3.
* At even levels, every nonzero-eligible connected component of
  the chosen-edge support containing both types has exactly one
  radical edge. Its underlying graph is a tree, all cutoff edges
  point away from the two endpoints of that radical edge, and
  the radical label is forced to \(r=m-1\), that is, to \(B\).
  There is no remaining sum over a radical label in this component.
  Every internal vertex uses the pure value formula (11), and
  every leaf uses (5). No spectator derivative remains.

A chosen-edge component containing a radical edge but no cutoff
edge is just an isolated radical edge and retains its full
original label sum. Components containing only cutoff edges are
exactly those of Theorem 3. None of these support rules asserts
nonvanishing of the final coherent sum.

**Proof.** Count at each vertex its incoming radical slots: one
for each cutoff head and one for each incident radical edge.
If there are two, their product is zero. At odd levels (19b)
also kills a radical edge incident to any cutoff tail. This gives
the first assertion.

For a connected even chosen-edge component, let \(v\) be its
vertex count, \(e\) its total edge count and \(q\) its number
of radical edges. Its total number of incoming radical slots is
\(e+q\), so survival requires \(e+q\le v\). Connectivity gives
\(e\ge v-1\), hence \(q\le1\). If \(q=1\), necessarily
\(e=v-1\), and every vertex has exactly one incoming slot.
It is a tree. The radical edge supplies the incoming slot at
each of its endpoints, which forces all other edges outward
from them. If any cutoff edge is present, at least one radical
endpoint has an outgoing cutoff edge. Equation (19b) forces
the shared radical label to \(m-1\). Every internal vertex
then has the form \(A^aB\), \(a\ge1\), and every leaf has
the form \(B\). Equations (11) and (5) prove the remaining
claims. \(\square\)

For an even mixed component with \(\ell_C\) leaves (vertices with
no outgoing cutoff edge), its observation, including its cutoff
scalar, has physical-value norm at most
\[
                            C_F N^{2\ell_C-2}.
 \tag{19d}
\]
This statement allows a joint spectator depending on all the other
chosen-edge components. To prove it, let \(i\) be the number of
internal vertices. There are \(i+\ell_C-2\) cutoff edges:
the tree has \(i+\ell_C-1\) edges, one of which is radical.
Thus \(\sum a_v=i+\ell_C-2\). Each internal observation (11)
costs at most \(N^{a_v-1}\), each leaf (5) at most \(N\).
Their product is \(N^{2\ell_C-2}\); the fixed number of factors
\(|s_{L+1}^2|\le4\) is included in \(C_F\).
In particular arbitrarily long mixed chains with two leaves have
cost \(O_F(N^2)\), with no derivative cost and no high-label sum.
The remaining physical sums and their signs are still retained.

## 6. Smaller components and the cost of the remaining observations

Return first to the pure cutoff source (17), with \(S=V(F)\).
Deleting the forcing edges gives the exact factorization
\[
                       G_{F,N}=\prod_{C\in\pi_0(G\setminus F)}
                                             Z_{C,N},
 \tag{20}
\]
where \(Z_{C,N}\) is the original component source with the
vertices of \(S\cap C\) left as ordinary boundary variables and
their crossings omitted. In a tree every \(C\) is a proper
subtree. In any case every factor has at most
\(|I|-|S|\le |I|-2\) traced vertices. A free vertex can still
have several incidences: their product is retained at its ordinary
degree. No nilpotence rule is imposed there before (18).
The identical factorization applies to \(G_{F,H,N}\) after deleting
\(F\cup H\), now with \(S=V(F\cup H)\); every unchosen edge still
belongs to its original component.

There is a useful polynomial bound whose exponent does not increase
with the number of internal vertices in a forcing chain. Let
\(\ell\) be the number of forcing leaves (\(a_v=0,b_v=1\)),
and let \(r_1\) be the number of rooted forcing components whose
root has outdegree one. For a fixed outside parameter \(\mathbf u\),
write
\[
 M_{F,N}(\mathbf u)=
        \sup_{\mathbf z_S\in[-2,2]^S}|G_{F,N}(\mathbf z_S,\mathbf u)|.
 \tag{21}
\]
If a support rule has not already made the source zero, then
\[
 |\mathscr J_{F,N}(\mathbf u)|
 \le
 \begin{cases}
  4^{|F|}N^{\ell+r_1}M_{F,N}(\mathbf u),&N\text{ odd},\\
  C_{G,\mathbf n,F}N^{2\ell+r_1}M_{F,N}(\mathbf u),
                                                    &N\text{ even}.
 \end{cases}
 \tag{22}
\]
The odd supremum may be restricted to physical node assignments.
Every fixed ordinary outside derivative satisfies the same statement
with \(G_{F,N}\) replaced by that derivative. Alternatively (20)
bounds \(M_{F,N}\) by the product of the component boundary norms.

**Proof.** At odd levels (5) and (8) each have total absolute
weight at most \(N\); every multiple-tail center has one unit
weight in (7). This proves the first line directly.

At even levels use
\[
 E\le N/2,\quad s\le2\pi/N,\quad |\tau|\le N^2/8
 \tag{23}
\]
(with \(\tau=0\) at \(N=2\)). The coefficient of \(f'\) in
(12) is \(O_r(N^{r-2})\), and its value coefficient is
\(O_{r,n}(N^r)\). The total value weight in (13) is
\(O_n(N^2)\), and its derivative coefficient is bounded.
For the noncentral weights this follows from (4) and
\[
 c_a-c_*\ge16(m-1-a)^2/N^2,\qquad
 \sum_{j\ge1}j^{-2}<2;
\]
the central coefficients follow from (23). Formula (11) costs
at most \(N^{a_v-1}\), while each leaf observation (5) costs
at most \(N\).

The ordinary degree of (17) in any \(z_v\), \(v\in S\), is
at most \(\deg_G(v)(N-1)\). Markov's inequality on \([-2,2]\)
therefore bounds a first derivative by
\(\deg_G(v)^2N^2/2\) times the supremum. It applies also to
complex coefficients, by rotating the derivative at a point and
taking a real part. Successive Markov inequalities handle distinct
root variables, including when their derivatives act on one
component of (20). Thus a root of outdegree \(a\ge2\) costs
\(O(N^a)\), a root of outdegree one costs \(O(N^2)\), and
there are no other derivative costs.

For a rooted forcing tree with root outdegree \(a\), \(i\)
nonroot internal vertices and \(\ell_C\) leaves, its edge count
is \(i+\ell_C\). The sum of the outdegrees is that same count.
The preceding exponents therefore sum to \(2\ell_C\) if
\(a\ge2\), and to \(2\ell_C+1\) if \(a=1\). For a cyclic
component the edge count equals its vertex count; summing
\(a_v-1\) over its internal vertices and adding its leaf costs
gives \(2\ell_C\). Summing over forcing components and retaining
\(|s_{L+1}^2|\le4\) proves (22). \(\square\)

For a long directed forcing path, the even exponent in (22) is
three regardless of its length; all internal vertices are exact
middle-value insertions. This concerns the observation cost only.
The remaining component sources and their rates still depend on
the original graph.

## 7. Scope for the short-filling induction

The generic radical matching expansion for arbitrary finite graphs
was already established. The additional conclusions here are the
complete cancellation of nonstar cutoff clusters at odd levels,
the exact pinning of even internal clusters, and the restriction of
spectator normals to roots. The joint radical/cutoff reduction
additionally eliminates all shared mixed clusters at odd levels and
forces the radical label in every even mixed cluster. Formulas
(18) and (19c) are valid before taking any absolute value, so one may
retain their signs, crossing phases and joint component correlations
instead of replacing them by norm bounds.

When a pinned vertex has other incident edges, those edges remain
as \(K_N(-2,z)\), \(K_N(c_*,z)\), or their prescribed derivatives.
They are not equal to one in general. Nor is \(c_*\) replaced by
\(-2\) at even levels: their \(N\)-dependent difference is retained
in every value and normal.

An estimate by a product of smaller-component suprema is only an
upper bound. Having fewer traced vertices does not imply that the
sum of their complete-boundary rates is below the full geometric
rate. The cancellation and pinning formulas prove no such universal
comparison. They also do not classify every current created by a
joint contour deformation, prove a nonzero coefficient of its
geometric cycle, or supply an arbitrary-short-filling volume theorem.

## Direct sources and prior coverage

The proof above uses the following full written sources, with their
original normalization:

* [Full high Newton contraction](research_high_newton_radical_contraction.md),
  SHA256
  1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03:
  the physical trace, radical, exact weights (4)--(5), their uniform
  bound, and arbitrary ordinary spectator coefficients.
* [Bare kernel and cutoff current](research_bare_kernel_power_three_obstruction.md),
  SHA256
  9feabd083c6ec0d864680b3fd49203508e54517abec974472f3065a15110fbaa:
  Sections 5--6 supply the literal forcing (3), midpoint values,
  central normal (16), and the root-gap bounds used in (23).

The local odd annihilation \(AB=0\) already appears in
[the upper-row deletion theorem](research_mixed_next_outer_exact_low_edge_reduction.md).
The polynomial bound for products of literal cutoff forcings on paths
is in [the path sector theorem, Section 8](research_radical_path_sector_gap.md).
The present theorem gives the collective all-level support and exact
root/value reduction, including branching, rather than claiming those
earlier local identities or generic matching expansions as new.

All arguments are finite identities and written inequalities. No
mathematical execution or numerical evidence is used.
