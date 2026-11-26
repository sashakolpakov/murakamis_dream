# Exact facet assembly and the Fourier-invariant seam character

Private written proof, 18 November 2026.

Shared subdivision faces cancel in the actual source. A physical
support jump instead has an explicit exit current, which is unchanged
by every integer Fourier recharge. On a regular constrained critical
chart the corresponding multiplicative seam character is also
unchanged by recharging. For independent physical wire or transfer
facets, this character is trivial exactly when every seam multiplier
is one. There is no hidden finite-index ambiguity.

These statements identify which cancellations are automatic and
which source terms still require a proof. They do not assert that
the remaining currents cancel, are exponentially smaller, or have a
nonzero geometric pairing. The complete directs are R, S, F and T,
pinned below.

## 1. The actual integral flow lattice

Use the fixed one-component braid and literal source of R. Split
each crossing into its donor and receiver visits, joined by its
directed transfer edge. The wire edges form the single oriented
knot cycle. This gives a connected graph \(\Gamma\), with \(2c\)
vertices and \(3c\) edges for \(c\) crossings. Give every edge its
specified orientation and let
\[
 \Lambda=\ker\{\partial:\mathbb Z^{E(\Gamma)}
                              \longrightarrow\mathbb Z^{V(\Gamma)}\}.
\tag{1}
\]
Wire and transfer occupations are exactly the edge coordinates of
these circulations. Conservation at a donor subtracts its nonnegative
transfer; conservation at the receiver adds it. R's cut-and-transfer
coordinates identify \(\Lambda\) with \(\mathbb Z^{c+1}\) integrally.

Write \(d=N-1\). The physical support is
\[
 S_N=\{k\in\Lambda:0\le a_e(k)\le d
                               \text{ for every physical edge }e\}.
\tag{2}
\]
Redundant upper transfer bounds can be retained. Here \(a_e\) is
restriction of the edge coordinate to \(\Lambda\). All original
cut weights, pivots, scalar factors and coupons of this source remain
in the summand \(I_N(k)\). Additional charged insertions require
their own affine matching adapter; (2) does not silently include
them. Set \(I_N^0=0\) outside \(S_N\).
This is finite-array zero extension, not negative-factorial
evaluation.

For T's tail-head current choose the integral vector \(v\) that
increases that external occupation \(a_j\) by one, fixes the other
external occupations and fixes the chosen non-tree transfers.
The spanning-tree reconstruction in T proves that \(v\in\Lambda\).
It changes every affected internal wire and tree transfer; those
changes cannot be suppressed.

## 2. Exact partition assembly, including its outside current

At the physical root let
\[
 h=2\pi i/N,\quad q=e^{h/2},\quad Q=e^h,\quad
 \lambda_h=(q-q^{-1})/Q,\qquad
 b_a=q^{-3}(1-Q^{a+1}).
\]
Define \(B_N^0(k)=b_{a_j(k)}I_N^0(k)\) and
\((T_vB)(k)=B(k-v)\). T's actual reindexed insertion current is
\[
                {\cal J}_N^0=\lambda_h I_N^0+B_N^0-T_vB_N^0.
\tag{3}
\]
For every finite test \(\chi\),
\[
 \sum_k\chi(k){\cal J}_N^0(k)
 =\lambda_h\sum_k\chi(k)I_N^0(k)
       -\sum_k\{\chi(k+v)-\chi(k)\}B_N^0(k).
\tag{4}
\]
This is reindexing of finite sums. No derivative or asymptotic
replacement is involved.

Suppose finitely many integer-valued tests form a partition:
\(\sum_\alpha\chi_\alpha=\chi\). Summing (4) gives precisely (4)
for \(\chi\). Thus every interface appearing twice with opposite
partition coefficients cancels before absolute values are taken.
This applies to signed partitions and overlapping decompositions
with their exact multiplicities, not just disjoint intervals.

For the physical indicator \(\chi={\bf1}_{S_N}\), the result is
\[
 \boxed{\quad
 \sum_{k\in S_N}{\cal J}_N^0(k)
   =\lambda_h\sum_{k\in S_N}I_N(k)+{\cal X}_{v,N},\qquad
 {\cal X}_{v,N}=
   \sum_{\substack{k\in S_N\\k+v\notin S_N}}B_N^0(k).
 \quad}
\tag{5}
\]
Indeed the only nonzero difference of this indicator on the
support of \(B_N^0\) is an exit, where it equals \(-1\).
The complementary reindexed current satisfies
\[
                    \sum_{k\notin S_N}{\cal J}_N^0(k)
                                      =-{\cal X}_{v,N}.
\tag{6}
\]
Equations (5)–(6) recover the full source identity
\(\sum_\Lambda{\cal J}_N^0=\lambda_h\sum_{S_N}I_N\).

The terms in (6) are not unsupported evaluations of the original
word. They are actual affine matching states of the inserted
current, labeled by the output occupation after the unilateral
coupon. Their underlying word state is \(k-v\in S_N\).
An exit caused solely by \(a_j=d\) has coefficient \(b_d=0\)
at the root. Other wire or transfer exits remain in (5).
If several inequalities fail at the same shifted state, its
contribution is counted once by this indicator formula.

The full off-root correction can also be kept explicitly.
For independent \(q,M\) use T's same finite arrays and put
\[
 \omega=Q^{N-1},\quad b_a=q^{-1}\omega(1-Q^{a+1}),\quad
 \lambda_a=q^{-1}(1-\omega)+q^{-1}Q^a(\omega Q-1).
\tag{7}
\]
With \(B=b_{a_j}I^0\), the actual truncated current is
\[
 {\cal J}^0(k)=\lambda_{a_j(k)}I^0(k)+B(k)-B(k-v)
           +{\bf1}_{a_j(k)=N}B(k-v).
\tag{8}
\]
The last term corrects the forbidden output row \(N\): without it,
the difference expression would leave \(-b_d I^0(k-v)\) there.
On all actual rows (8) is exactly T's finite matrix formula.
Consequently
\[
\begin{split}
 \sum_k\chi(k){\cal J}^0(k)
 ={}&\sum_k\chi(k)\lambda_{a_j(k)}I^0(k)
    -\sum_k\{\chi(k+v)-\chi(k)\}B(k)\\
 &+\sum_{a_j(k)=d}\chi(k+v)B(k).
\end{split}
\tag{9}
\]
This retains the \(1-Q^N\) top wall before differentiation.
All parameter derivatives also hit the cut, pivots, scalar line
and summand. As in T, the closed germ retains its stated ADO
pivot; a parameter path alone does not convert it to the ordinary
colored-Jones pivotal and framing germ.

## 3. What the contour and Fourier assemblies cancel

R's product-cell boundary formula is linear in the state
indicator. Its mixed face coefficient is
\[
 \Delta_J\chi(k)=
   \sum_{\delta\in\{0,1\}^J}(-1)^{|\delta|}\chi(k+\delta).
\tag{10}
\]
Hence \(\sum_\alpha\Delta_J\chi_\alpha=\Delta_J\chi\) exactly
for every \(J\), including all intersections and slanted facets.
This is the chain version of internal-interface cancellation.
It leaves the mixed differences of the total indicator.
It does not set those differences to zero at a physical edge
of the total support.

Translation prisms obey the same oriented boundary law. T gives,
on each supplied holomorphic prism,
\[
                {\cal J}_N=\lambda_h\omega_N+h\,d{\cal B}_N.
\tag{11}
\]
Thus a shared face cancels if its two induced chains, interpolants,
marks and orientations agree. Where the charts or source functions
do not agree, that equality has not been established. An external
prism face, a source pole crossing or a physical support jump is
still a retained current. R explicitly keeps these latter terms.

Let \(\nu\in\Lambda^*=\operatorname{Hom}(\Lambda,\mathbb Z)\)
be any integer Fourier change. On the actual lattice,
\[
                         e^{-2\pi i\nu(k)}=1.
\tag{12}
\]
Therefore every summand in (5), (6) and (9), not just their total,
is unchanged by this recharge. F's complete Fourier expansion
assigns different translated contours to its different charges.
Equation (12) is not a termwise equality of those off-lattice
integrals. Their character differences retain R's pole-free
correction and boundary terms.

In particular, changing Fourier labels cannot change or erase
the finite exit datum \({\cal X}_{v,N}\). Its cancellation in the
full current is exactly (6), not a smaller-action estimate for
either side of (5).

## 4. The physical facet lattice has no finite-index defect

For an edge subset \(I\subseteq E(\Gamma)\), let
\[
                         a_I:\Lambda\longrightarrow\mathbb Z^I
\]
be edge restriction. Delete the edges in \(I\), and contract each
connected component of \(\Gamma\setminus I\) to a vertex. Keep
all edges of \(I\), including any resulting loops; call the
contracted graph \(\Gamma_I\).

**Integral projection lemma.**
\[
              \operatorname{im}a_I=\ker\partial_{\Gamma_I}.
\tag{13}
\]
In particular this image is a saturated subgroup of \(\mathbb Z^I\).

To prove necessity, sum the circulation equations over every
component of \(\Gamma\setminus I\). Internal edges cancel and
give exactly the contracted incidence equation. Conversely,
prescribe \(y\in\ker\partial_{\Gamma_I}\) on \(I\). In each
complementary component the required remaining vertex divergence
has sum zero. Choose a spanning tree of that component. Successive
leaf elimination assigns its incident edge an integer value,
removes that divergence, and leaves the same problem on the
smaller tree. The last divergence is zero. This constructs an
integral circulation extending \(y\), proving (13). A kernel of
an integer homomorphism into a free abelian group is saturated.

If the covectors \(a_i\), \(i\in I\), are linearly independent
on \(\Lambda\otimes\mathbb C\), the image in (13) has rank
\(|I|\). The connected graph \(\Gamma_I\) consequently has zero
incidence rank, hence one vertex. Equivalently,
\(\Gamma\setminus I\) is connected, and
\[
                           a_I(\Lambda)=\mathbb Z^I.
\tag{14}
\]
Choose integral \(v_i\in\Lambda\) mapping to the standard basis.
Then
\[
          \Lambda=\ker a_I\ \oplus\!
                              \bigoplus_{i\in I}\mathbb Z v_i.
\tag{15}
\]
These are exact independent normal shifts for the active physical
edge coordinates. There is no normal-lattice congruence or
ramification. At a simple vertex with \(c+1\) independent active
edge constraints, the active coordinate map is unimodular.
No assertion that an arbitrary nonsimple tangent cone is an
orthant follows from (15).

## 5. The seam character and its exact charge invariance

Work on S's stated holomorphic unit chart. Let
\(\Phi_q(\zeta)=\Phi_0(\zeta)-2\pi i q(\zeta)\) be the phase
with its original integer Fourier covector. At an affine
constrained critical point \(\zeta_*\), write
\[
 d\Phi_q(\zeta_*)=\sum_{i\in I}t_i a_i
                          \quad\text{in }\Lambda_\mathbb C^*,
\tag{16}
\]
where the active physical edge covectors are independent.
Their affine constants may be shifted; their linear parts
are those in (1).

The multiplicative seam invariant is the character
\[
 {\mathfrak s}_{\zeta_*}:\Lambda\longrightarrow\mathbb C^*,
 \qquad
 {\mathfrak s}_{\zeta_*}(k)
             =\exp(d\Phi_q(\zeta_*)[k])
             =\prod_{i\in I}e^{t_i a_i(k)}.
\tag{17}
\]
It is exactly the vertex-gauge class of S's diagonal momentum
seams. Here is an elementary graph verification. Assign the
multiplier \(e^{t_i}\) to edge \(i\) and multiplier one elsewhere.
Vertex rescalings multiply edge labels by a coboundary.
Choose a spanning tree and use vertex rescalings to make its
labels one. Each remaining chord label is the product along
its fundamental circulation. These products are precisely (17).
Thus all edge seams can be gauged away exactly when (17) is trivial.

This expanded-graph description agrees with S's crossing graph.
The transfer edges join disjoint donor–receiver pairs and form a
forest. Gauging their labels to one and contracting them transfers
a transfer seam to the two opposite wire seams in S. The remaining
vertex gauges are the common crossing-momentum gauges. No new
physical gauge freedom has been introduced.

By (14), there is a circulation testing each \(i\) separately.
Consequently
\[
 \boxed{\quad {\mathfrak s}_{\zeta_*}=1
       \quad\Longleftrightarrow\quad
       e^{t_i}=1\ \text{for every }i
       \quad\Longleftrightarrow\quad
       t_i\in2\pi i\mathbb Z\ \text{for every }i.\quad}
\tag{18}
\]
This is global in the multipliers, not just a statement near
\(t_i=0\). It uses actual independent edge covectors. Arbitrary
affine normals do not automatically have the primitivity (14).

For every integer recharge \(\nu\),
\[
 d\Phi_{q+\nu}=d\Phi_q-2\pi i\nu,\qquad
                       \exp(d\Phi_{q+\nu}[k])
                         =\exp(d\Phi_q[k])\quad(k\in\Lambda).
\tag{19}
\]
So a nontrivial character cannot be repaired by choosing another
Fourier charge. A recharge preserves face stationarity at the
same point only if its covector is conormal to that face.

Conversely, if (18) holds, put
\(\nu=\sum_i(t_i/(2\pi i))a_i\in\Lambda^*\).
Then \(d\Phi_{q+\nu}(\zeta_*)=0\): the constrained point is an
unconstrained critical point for that integer charge. On the
same unit chart S's original incidence adapter now gives the
ordinary crossing matching, rather than a network with seams.
The actual closure and peripheral conditions must still be
retained when identifying its representation.

On a finite physical face \(a_i(k)=B_i\in\mathbb Z\), such a
conormal recharge changes its lattice character by
\(\exp(-2\pi i\sum_i m_iB_i)=1\), where \(t_i=2\pi i m_i\).
This includes the exact upper value \(B_i=N-1\). On a displaced
complex face its constant character need not be one and must
remain in the contour formula.

## 6. What has and has not been removed

The exact assembly removes shared artificial partition interfaces.
The total support's exit currents are the finite sums (5), with
their compensating affine-current states (6) and off-root wall
(9). Those data survive every Fourier relabeling. Their size and
possible cancellation in a proposed geometric decomposition have
not been determined.

On a supplied regular critical chart, (18)–(19) give a precise
test for compatibility with unseamed gluing. Nontrivial seam
characters cannot be assigned a knot-representation volume merely
by relabeling their charge. Proving that their assembled weighted
periods vanish would be an additional source theorem, not a
consequence of the incidence lattice or irreducibility.

Finally, a clock-one physical endpoint can leave the unit momentum
chart altogether, as S proves. Neither (16) nor a representation
interpretation is asserted across that singular layer without an
actual source-compatible extension. The finite array identities
remain valid there. No lower-dimensional weighted face, quantum
normal, or same-action endpoint term has been discarded.

## Complete proof-source pins

* R: notes/research_actual_oblique_geometric_contour_decomposition.md,
  SHA256 9180de472bafb38c479d3e1aafac6c75c388d668371892f54219de658728034c.
* S: notes/research_actual_facet_seams_and_geometric_boundary.md,
  SHA256 ac250fc87e7bf1d4f6851c346ef08f7cd08d9e4566d1283981c03dee2427441c.
* F: notes/research_oblique_top_fourier_aliases.md,
  SHA256 9fa4d981c401c1b744fa12b1241f0404d7ba8da90d21f6b90f556ef6a065b584.
* T: notes/research_pivotal_current_regular_collar_transgression.md,
  SHA256 e207f8a8b5440b909f9844aee09fb7f59ad02889066b8a6929abde3cffe36c86.

All four complete texts were read nontruncated in the active
author sequence; unchanged complete R/T reads were retained from
the immediately preceding formal review. The older complete
factorial-core contour compiler was read for coverage: its mixed
facet telescoping is not claimed as a new theorem here. The
integral projection lemma and its normal-lattice consequence were
independently derived by root and checked by the proof above.
Only written mathematics and text/hash operations were used.
