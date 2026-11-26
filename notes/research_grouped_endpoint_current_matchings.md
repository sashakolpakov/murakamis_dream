# Simultaneous endpoint currents are a matching polynomial

Research note, 3 November 2026.

Several endpoint currents in the original circle network can be
contracted together before any estimate. The answer is a matching
polynomial on the vertices where currents were inserted, with
explicit coupons at the remaining vertices. This keeps the mixed
first normals on every shared edge. It is more precise than multiplying
separate estimates for one-vertex currents.

When the remaining components already have controlled trace contours,
the matching expansion also computes the leading coefficient of the
current. Except for an inserted zero-power current, that coefficient
is nonzero. In particular simultaneous endpoint terms do not generally
cancel among themselves. Their comparison with the desired filled
volume remains a separate issue.

## 1. The endpoint functional and the edge jets

Use
\[
 D=N-1,\quad \eta=(-1)^D,\quad \sigma=(-1)^N=-\eta,\quad
 c_0=2\cos(\pi/N),\quad s_1=2\sin(\pi/N),\quad \rho=i s_1.
 \tag{1}
\]
Let \(W_{n,N}\) be the exact one-step Ward insertion for the normalized
Gaussian crossing of signed power \(n\). For any original polynomial
spectator \(f\),
\[
 \phi_N(W_{n,N}f)=a_n f(c_0)+b_n f'(c_0),                 \tag{2}
\]
where
\[
 \begin{array}{c|cc}
  &a_n&b_n\\ \hline
 n\text{ even}&\sigma nN\rho&0\\
 n\text{ odd}&\eta(n\rho-2c_0)&2\eta s_1^2 .
 \end{array}                                             \tag{3}
\]
This is the exact endpoint formula in
[the logarithmic contour-transport note](research_gaussian_logarithmic_contour_transport.md).
The removed common crossing units \(\kappa_N^n\) must be restored
when the normalized identity is used in a physical source; they are
not changed by the calculations below.

The actual turn kernel and its required jets are
\[
 \begin{split}
 K_N(z,w)&=\sum_{j=0}^D e_j(z)e_j(w),\\
 K_N(c_0,w)&=1,\qquad
 \partial_zK_N(c_0,w)=Q_N(w),\\
 K_N(c_0,c_0)&=1,\quad
 K_{N,z}(c_0,c_0)=K_{N,w}(c_0,c_0)=0,\\
 K_{N,zw}(c_0,c_0)&=k_N
                    :=\frac{N^2-1}{12s_1^2}.
 \end{split}                                             \tag{4}
\]
Here
\[
             Q_N=\frac{\eta\,T\Pi_0+c_0}{s_1^2}.         \tag{5}
\]
Equations (4)--(5) are full-jet identities. For the last line of (4),
use \(e_j'(c_0)=(-1)^j/(s_1s_j)\) and
\(\sum_{j=1}^{N-1}s_j^{-2}=(N^2-1)/12\). These identities are proved
in [the endpoint-normal calculation](research_endpoint_normal_cap_rate.md)
and [the diagonal-density calculation](research_turn_trace_residue_density.md).

## 2. Exact contraction of an arbitrary current subset

Let \(G\) be a fixed finite circle tree and let \(S\) be any subset
of its vertices. Put a one-step Ward insertion \(W_{n_v,N}\) at
each \(v\in S\), and retain all original operations at the other
vertices. For the moment leave the variables \(w\) outside \(S\)
uncontracted. The current part of the network is
\[
 \mathcal E_{S,N}(\mathbf w)=
 \left(\prod_{v\in S}\phi_N^{(z_v)}\right)
 \left[
  \prod_{v\in S}W_{n_v,N}(z_v)
  \prod_{uv\in E(S)}K_N(z_u,z_v)
  \prod_{\substack{e=(v,w)\\v\in S,\ w\notin S}}K_N(z_v,w)
 \right].
 \tag{6}
\]
The edges in the last product are counted with their actual incidences.
In particular different removed components may meet the same outside
vertex. No reduction is performed in an uncontracted variable.

Let \(O\subseteq S\) be the vertices with odd \(n_v\), and write
\(d_{\rm ext}(v)\) for the number of incidences from \(v\) to the
outside of \(S\). Define the vertex polynomials
\[
 A_v(\mathbf w)=
 \begin{cases}
   \sigma n_vN\rho,&n_v\text{ even},\\[1mm]
   2\displaystyle\sum_{e=(v,w),\,w\notin S}T\Pi_0(w)
       +\eta\{n_v\rho+2(d_{\rm ext}(v)-1)c_0\},
                                      &n_v\text{ odd},
 \end{cases}                                             \tag{7}
\]
and the positive edge weight
\[
                         d_N=\frac{s_1^2(N^2-1)}3.       \tag{8}
\]
A matching is a set of edges with no shared endpoint.

**Theorem 1.** The exact whole-boundary current is
\[
 \boxed{\quad
 \mathcal E_{S,N}(\mathbf w)=
   \sum_{\substack{M\text{ a matching}\\M\subseteq E(O)}}
        d_N^{|M|}
        \prod_{v\in S\setminus V(M)} A_v(\mathbf w).
 \quad}                                                   \tag{9}
\]
It holds at both parities with all mixed first normals retained.

**Proof.** Apply (2) at all vertices simultaneously. Each vertex is
either evaluated or differentiated once. A derivative of the product
of its incident kernels chooses one edge. By (4), a derivative assigned
to an internal edge is zero unless its other endpoint also assigns its
derivative to that same edge. Thus the internally differentiated edges
form a matching, and both endpoints have odd powers. Their contribution
is
\[
                  b_{n_u}b_{n_v}k_N
             =(2\eta s_1^2)^2 k_N=d_N.
 \tag{10}
\]
At every unmatched vertex the two possibilities are evaluation with
weight \(a_{n_v}\), or differentiation of one external edge with weight
\(b_{n_v}Q_N(w)\). Their sum is exactly (7), by (5). Every remaining
edge contributes its value one. All product-rule terms occur once in
(9); no mixed edge derivative is omitted. \(\square\)

Multiplying by the original exterior and performing its remaining
traces preserves (9). The formula therefore applies to simultaneous
corner currents of an iterated contour identity whenever its local
cycle differences are the specified one-step Ward currents. It does
not identify every arbitrary contour remainder with such a current.
It is also not a replacement for the original relative cycle.

For fixed \(G,S,\mathbf n\), every coefficient in (9) is bounded by
a fixed polynomial in \(N\). The only nonconstant boundary coupons
are finitely many \(T\Pi_0\), with their original multiplicities.
The formula gives an exact finite reduction to decorated deleted
forests, not a new topological simplification of the knot.

## 3. The leading matching terms have a common phase

There is a useful consequence when the exterior has already been
controlled analytically. Suppose the exterior scalar contraction
\(Z_{G\setminus S,N}\) has a nonzero packet, and its proved full
trace contours permit the exact logarithmic-factorial representative
of \(T\Pi_0\) at every incidence in (7). As in
[the Ward-interpolation theorem](research_odd_ward_logarithmic_factorial.md),
assume those charts stay in fixed interior physical rectangles,
with their original complementary currents and gaps retained.
Then every fixed collection of \(r\) such insertions has leading
factor
\[
                         (2\sigma\log N)^r(1+o(1))
 \tag{11}
\]
relative to the same exterior packet. This includes products of
coupons at a shared outside vertex.

If an even \(n_v\) is zero, the corresponding current and (9) vanish
identically. Otherwise put
\[
 E=S\setminus O,\qquad
 B=\{v\in O:d_{\rm ext}(v)>0\},\qquad I=O\setminus B,
 \quad
 \mathcal Z_I=\sum_{M\subseteq E(I)\ {\rm matching}}
                          \left(\frac{\pi^2}{12}\right)^{|M|}.
 \tag{12}
\]
The empty matching shows \(\mathcal Z_I>0\).
Contracting (9) against the controlled exterior gives
\[
 \begin{split}
 \frac{\mathcal E_{S,N}[\,\text{exterior}\,]}
                  {Z_{G\setminus S,N}}
  ={}&\sigma^{|S|}(2\pi i)^{|E|}
       \left(\prod_{v\in E}n_v\right)
       4^{|O|}(\log N)^{|B|}
       \left(\prod_{v\in B}d_{\rm ext}(v)\right)
       \mathcal Z_I\,(1+o(1)).
 \end{split}                                             \tag{13}
\]
Empty products equal one.

To prove it, the unmatched even weight tends to
\(\sigma\,2\pi i n_v\). An unmatched odd vertex in \(I\) has
weight \(4\sigma+o(1)\), while a vertex in \(B\) has leading
weight \(4\sigma d_{\rm ext}(v)\log N\). Also
\(d_N\to4\pi^2/3\). The largest power of \(\log N\) is \(|B|\);
it occurs exactly when no matching edge meets \(B\). The remaining
matchings are those in \(I\). Removing two odd monomers changes
their phase by \(\sigma^{-2}=1\), and replaces their factor \(16\)
by \(4\pi^2/3\). All their leading coefficients therefore have the
same phase and sum to the strictly positive factor \(\mathcal Z_I\).
The nonzero assertion follows.

Equation (13) is a rate statement for the current when the exterior
has a proved contour theorem. It does not assume that this rate is
smaller than the desired filled rate. The
[unit-crossing example](research_endpoint_normal_cap_rate.md)
shows that the reverse strict inequality can occur before exact
diagram reductions. Even after reductions, a comparison between
these forest rates and the filled action needs a separate argument.

## 4. Consequence for a general contour induction

The simultaneous first-normal bookkeeping is finite and explicit:
internal edges pair derivatives into matchings, and the remaining
derivatives become known Ward coupons. This provides the exact
lower-complexity boundary terms for a proposed induction on vertices.

It does not make that induction triangular in exponential growth.
Under the hypotheses of Section 3, those boundary terms survive
with a specified nonzero coefficient. A general proof must either
put their rates below the geometric rate, or exhibit their cancellation
against the other pieces of the original contour. Neither algebraic
nilpotence nor the fact that a deleted forest has fewer vertices
gives this comparison.

## 5. The whole physical tree trace has a colored determinant formula

The same product-rule calculation applies to every physical spectral
node, and therefore to the entire original trace. This observation
gives an exact representation, not a new estimate.

Let \(\mathcal C_N\) be the set of distinct roots of the physical
Chebyshev relation. At a double root \(c\), the local contribution
of the original filled-vertex trace is
\[
 \begin{split}
 \phi_{c,N}(R^{n_v}f)
   &=a_v(c)f(c)+b_v(c)f'(c),\\
 a_v(c)&=\eta\{(4-c^2)(R^{n_v})'(c)-cR^{n_v}(c)\},\\
 b_v(c)&=\eta(4-c^2)R^{n_v}(c).
 \end{split}                                             \tag{14}
\]
At the odd simple root \(c=-2\), take
\(a_v(-2)=R^{n_v}(-2)\) and \(b_v(-2)=0\).
All powers and derivatives in (14) are those of the original
full algebra element. In particular signed powers are not
replaced by their reduced spectral values.

Fix a spectral assignment \(\mathbf c=(c_v)_{v\in G}\).
Let \(F(\mathbf z)\) be the product of the original edge kernels
and any retained one-variable boundary factors. For the moment
suppose those factors are nonzero at \(\mathbf c\).
Define
\[
 \begin{split}
 A_v(\mathbf c)&=a_v(c_v)
       +b_v(c_v)\,\partial_{z_v}\log F(\mathbf c),\\
 w_{uv}(\mathbf c)&=b_u(c_u)b_v(c_v)\,
                 \partial_{z_u}\partial_{z_v}
                    \log K_N(c_u,c_v).
 \end{split}                                             \tag{15}
\]
For each edge choose an orientation. Form a matrix \(D_{\mathbf c}\)
with diagonal entries \(A_v\), entries \(1,-w_{uv}\) in the two
opposite off-diagonal positions of that edge, and zeros elsewhere.
Then the full local contribution is exactly
\[
 \left[\prod_v(a_v+b_v\partial_{z_v})F\right]_{\mathbf z=\mathbf c}
       =F(\mathbf c)\det D_{\mathbf c}.                   \tag{16}
\]
Consequently the original scalar tree source is the finite sum
\[
                         Z_N=
       \sum_{\mathbf c\in\mathcal C_N^{\,V(G)}}
                         F(\mathbf c)\det D_{\mathbf c}. \tag{17}
\]

To prove (16), derivatives of \(\log F\) involving three or more
distinct vertex variables vanish: every factor depends on at most
two adjacent variables. Expanding derivatives of its exponential
therefore partitions the differentiated vertices into singletons
and pairs, with every pair an edge. These are precisely the matchings,
with monomer and edge weights (15). In the determinant expansion,
a permutation supported by a tree has only fixed points and
transpositions, since a longer cycle would be a graph cycle.
Each edge transposition contributes
\(-1\cdot1\cdot(-w_{uv})=w_{uv}\), proving (16).
The local residue formula (14) then proves (17).

There is no hidden internal denominator at a physical node.
Represent distinct roots as \(c_j\), \(0\le j\le\lfloor D/2\rfloor\).
The original \(e_i(c_j)\) are positive for \(i\le j\) and zero
for \(i>j\). Hence
\[
                         K_N(c_j,c_k)\ge1.               \tag{18}
\]
If a retained free-boundary factor vanishes, multiply out (16)
before evaluating it. Its apparent denominators cancel by the
product-rule identity, so it extends polynomially to that point,
including every free-boundary normal.

Formula (17) preserves the coherent spectral sum and the original
crossing derivatives. It does not assert that its determinant or
its summands are positive, and does not replace that sum by a
single critical representation. The number of spectral assignments
still grows with \(N\). Its use is that the entire nilpotent
first-normal calculation has been reduced to an explicitly defined
finite matrix at each assignment.

The left side of (16) is the denominator-free definition, including
when a free-boundary factor vanishes. The local logarithms are only
a compact notation for its matching expansion where division is
permitted. Integration by parts in the existing exact complete-period
representation reorganizes the same first normals into its charge
factors. Formula (17) therefore does not remove the already known
cancellation inside those charge integrals.

## 6. Reproduction

Run
~~~sh
python3 experiments/check_endpoint_current_matchings.py \
  --precision 120 \
  --output repro/results/research-endpoint-current-matchings.json
~~~
The [script](../experiments/check_endpoint_current_matchings.py) constructs
the original quotient by monic polynomial division, builds the full
endpoint projectors, and sums every internal Newton edge label. It
compares those contractions with (9) on paths, a branching star,
and disconnected removed components sharing a free boundary variable.
The [saved record](../repro/results/research-endpoint-current-matchings.json)
contains 42 matching comparisons at \(N=2,\ldots,8\), including both
parities, signed powers, zero-power currents, and nonnodal complex
boundary values. Fourteen further comparisons verify the exact
cap and Ward-current identities from the endpoint-rate note.
Seven whole-tree checks compare the complete determinant sum (17)
with an independent Newton-edge-index contraction for powers
\((2,-3,4)\), including the odd simple root and every first normal.
These finite calculations check normalization and implementation;
the all-level matching formula and rate statement are proved above.

The same checks were repeated at 150 decimal digits; the
[record](../repro/results/research-endpoint-current-matchings-root.json)
includes the script hash and all seven whole-tree determinant
comparisons.
