# Opposite cyclic sources and the canonical Gram of an original Morse cut

24 November 2026. Research proof. Earlier finals and manuscripts are unchanged.

A fixed original one-cut knot diagram admits a cyclic-source presentation
through every odd-width Morse slice. Dual turns use opposite sources;
the total cyclic power consequently stays constant when a pair is born
or dies. In the canonical averaged Grams, normalized literal cups are
isometries, normalized ordinary caps are contractions, and actual
crossings transport between the differently labeled Grams without a
metric-conversion factor. The whole cut matrix remains the original one.

These assertions retain the complete physical spaces. An ordinary cap
is not declared the adjoint of its cup: their ordinary bubble is zero.
The result does not lower-bound the knot scalar or its geometric part.

## 1. Fixed diagram, actual head, and signed sources

Fix \(N\ge2\), and write
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad x=-q^{-1},
 \quad\gamma=x^N=(-1)^{N+1}.
 \tag{1}
\]
The physical basis \(w_0,\ldots,w_d\) is orthonormal. At complete color
use the regular E-semicyclic chart of [B]:
\[
 \begin{split}
 K w_a&=xQ^{-a}w_a,\\
 E_\mu w_a&=(Q^{-a}-1)w_{a-1}\quad(a>0),&
 E_\mu w_0&=\mu w_d,\\
 Fw_a&=(1-Q^{a+1})w_{a+1}\quad(a<d),&
 Fw_d&=0 .
 \end{split}                                                     \tag{2}
\]
Here \(E_\mu\) is [B]'s scaled generator \(\mathcal E\).
The coproducts are
\[
 \Delta E=E\otimes K+I\otimes E,\quad
 \Delta F=F\otimes I+K^{-1}\otimes F,\quad
 \Delta K=K\otimes K.
 \tag{3}
\]
The corresponding antipodes are
\(S(E)=-EK^{-1}\), \(S(F)=-KF\), \(S(K)=K^{-1}\).

Fix an original oriented \(1\to1\) Morse presentation \(\mathscr D\)
of a knot, using the standard actual turns of [P]. Keep its original
signed crossing matrices, common Cartan scalars, pivotal convention,
framing and assigned external normalization lines. All internal deaths
below are ordinary caps. The distinguished original marking is applied
only to the completed one-cut operator.

Choose \(|\mu|=1/N\). On a slice with \(b\) ordered heads set
\[
 \nu_i=\gamma^{i-1}\mu_i,\qquad \nu_i\in\{\mu,-\mu\},
 \qquad \sum_{i=1}^b\nu_i=\mu .
 \tag{4}
\]
The signs are the orientations of the sliced strands, with the surviving
cut strand assigned \(+\mu\). Thus every width \(b\) is odd.
At a birth insert two opposite \(\nu\)'s; at a death remove them.
At a crossing the two \(\nu\) labels exchange positions.
This gives consistent labels along the fixed oriented diagram.

Indeed [B, (8)] at \(x^N=\gamma\) gives, for either crossing sign,
\[
 (\mu_i,\mu_{i+1})\longmapsto
             (\gamma\mu_{i+1},\gamma\mu_i);
 \qquad(\nu_i,\nu_{i+1})\longmapsto(\nu_{i+1},\nu_i).
 \tag{5}
\]
Use the genuinely changing-source finite crossings of [B, (7)] and
their inverses, rather than the unchanged nilpotent crossing matrix.
Their coefficients contain the actual \(E_{\mu_i}\), and they
intertwine the total generators between the stated source fibers.
All sources have modulus \(1/N\), at both parities.

## 2. The literal dual turns at opposite centers

For clarity, duality in this E-chart is checked directly. On the
ordinary linear dual, with action \(\rho(S(h))^{\mathsf T}\), put
\[
 J_Ew_a=x^a w_{d-a}^*,\qquad \mu^\vee=-\gamma\mu.
 \tag{6}
\]
This is an isomorphism \(V_{\mu^\vee}\to V_\mu^*\).
The reversed inverse \(K\)-weight is
\(x^{-1}Q^{d-a}=xQ^{-a}\).
For \(a>0\), the dual \(E\)-coefficient after the change (6) is
\[
 -Q^{-a}(Q^a-1)=Q^{-a}-1.
 \tag{7}
\]
The wrap sends \(w_d^*\) to \(-x^{-1}\mu w_0^*\); comparison with
\(J_Ew_d=x^d w_0^*\) gives
\(\mu^\vee=-x^{-N}\mu=-\gamma\mu\).
Similarly the transposed \(-KF\) coefficient becomes
\(1-Q^{a+1}\); its top arrow vanishes. This verifies all generators.
In particular the different F-semicyclic frame of [R] is not silently
used as the balanced E-chart matrix.

The actual cup and ordinary cap in these coordinates are [P, Section 1]
\[
 p_{a,b}=N x^{a-d}\,\mathbf1_{a+b=d},\qquad
 \ell_{a,b}=\frac{x^a}{N}\,\mathbf1_{a+b=d}.
 \tag{8}
\]
Their full \(N,1/N\) factors and pivot phases are retained.
Both oriented extrema have these same numerical matrices in the
identified complete balanced frames. Indeed \(c_a=x^a\) in (6) and
\(g_a=x^{-d}Q^{-a}\) give
\(c_a^{-1}g_{d-a}^{-1}=x^{a-d}\) for the right cup and
\(c_{d-a}g_a=x^a\) for the right cap. These use \(x^2Q=1\);
the double-dual ratio \(c_a/c_{d-a}=g_a\) retains the actual pivot.
For adjacent sources \(\mu_1,\mu_2\), these are Hopf intertwiners
from or to the trivial module exactly when
\[
                   \mu_2=-\gamma\mu_1 .
 \tag{9}
\]
This is precisely the opposite-\(\nu\) rule in (4), at any insertion
position.

Here is a direct check that includes the cyclic wall. At zero wraps
the familiar identities
\(E_{\rm pair}p=F_{\rm pair}p=0\), \(K_{\rm pair}p=p\)
follow from \(x^2=Q^{-1}\) and \(Q^N=1\).
For example the two contributions to the \(F\)-output \((a+1,d-a)\)
are proportional to \(1-Q^{a+1}\) and \(Q^{a+1}-1\).
The only new \(E\)-output is
\[
 E_{\rm pair}p
       =N(\gamma\mu_1+\mu_2)\,w_d\otimes w_d.
 \tag{10}
\]
For the cap, its zero-wrap \(E\)-coefficient on an input
\(a+b=N\) is
\[
 \frac{x^a}{N}
 \{Q^{-b}(Q^{-a}-1)+(Q^{-b}-1)\}=0.
 \tag{11}
\]
Its \(F\)-coefficient on \(a+b=N-2\) is proportional to \(1-Q^N\).
The only added cyclic cap coefficient is
\(\ell E_{\rm pair}|_{(0,0)}=(\gamma\mu_1+\mu_2)/N\).
Also \(\ell K_{\rm pair}=\ell\). This proves (9) and its necessity.

The physical norms, snakes and ordinary bubble are exactly
\[
 \|p\|^2=N^3,\qquad \|\ell\|^2=N^{-1},\qquad
 (I\otimes\ell)(p\otimes I)=I
       =(\ell\otimes I)(I\otimes p),\qquad \ell p=0 .
 \tag{12}
\]
For each snake the matched coefficients multiply to one.
For the bubble, their sum is \(x^{-d}\sum_a x^{2a}=0\).
Thus no positive adjoint-cap convention has been substituted.

## 3. One common cyclic normalization through every width

For a labeled odd slice let
\[
 E_\Sigma=\sum_{i=1}^b E_{\mu_i}K_{i+1}\cdots K_b,\qquad
 K_\Sigma=\prod_{i=1}^b K_i .
 \tag{13}
\]
The root product gives \(E_{\mu_i}^N=\gamma N\mu_i I\).
The summands in (13) \(Q\)-commute, so their mixed \(N\)-th
multinomial coefficients vanish. Consequently
\[
 E_\Sigma^N
 =\gamma^bN\sum_i\nu_i I=\gamma N\mu I=:cI,
 \qquad |c|=1.
 \tag{14}
\]
Choose once and for all \(e^N=c\), and on every such slice define
\[
                  T_{\boldsymbol\nu}=E_\Sigma/e,\qquad
                  T_{\boldsymbol\nu}^N=I .
 \tag{15}
\]
Births, deaths and both signed crossings intertwine these \(T\)'s.
For a turn inserted inside other heads this follows from (3):
the pair acts on its cup by \(K_{\rm pair}=1,E_{\rm pair}=0\),
and the cap obeys the corresponding row equations.
The earlier and later head terms therefore pass through unchanged.
Crossing intertwining is the actual changing-source statement of [B].

No intermediate tail is required to have nonzero central power.
If the first normalized label is \(+\mu\), its remaining even tail
has \(E_{\rm tail}^N=0\). If it is \(-\mu\), that power is \(2cI\).
Crossings can exchange these situations. Formula (15) remains valid
in either case; no inverse of the tail coproduct or fusion-wall
specialization is used.

## 4. Source preservation for the completed original cut

Let \(\mathcal A_\mu(\mathscr D)\) be this literal fixed-diagram
operator, with all original external factors restored.
Its entire one-head matrix satisfies
\[
             \mathcal A_\mu(\mathscr D)
                    =\mathcal A_0(\mathscr D)
                    =K_N(\mathscr D)\,I .
 \tag{16}
\]
The first equality has a direct degree proof extending [B, Section 5].
Give \(w_a\) integer degree \(a\), without reducing totals modulo \(N\).
A birth (8) adds \(d\); an ordinary death removes \(d\).
In a positive crossing term \(E_{\mu_1}^kF_2^k\), every ordinary
lowering cancels one raising. Each cyclic \(E\)-wrap instead changes
the total degree by an additional \(+N\).
The diagonal Cartan and checked flip preserve the total.

The actual negative crossing uses the finite inverse Euler series in
[B, Section 4], evaluated in its recovered source fiber. It also has
only \(E^kF^k\) terms with \(0\le k<N\); \(F\) has no wrap.
Hence every source-dependent wrap in either sign contributes \(+N\),
never \(-N\). Products of source labels may have signs, but do not
alter this integer-degree accounting.

A \(1\to1\) presentation has equally many births and deaths.
If a matrix-entry path has \(r\) wraps, its output minus input degree
is therefore \(rN\). Both degrees lie in \(\{0,\ldots,d\}\), forcing
\(r=0\). All surviving entries are exactly the original nilpotent
entries. This proves the first equality in (16), without changing
an intermediate cap or testing an arbitrary marked sector.

For the second equality, the completed original unmarked one-cut
operator intertwines \(E_0,K\). The \(K\)-weights are distinct, so
it is diagonal; every ordinary \(E_0\)-arrow is nonzero, so the
diagonal entries agree. Its scalar, with the prescribed framing
and external normalization, is the original selected value \(K_N\).
The original final marking is applied to this completed matrix.

This argument concerns a fixed Morse presentation. It does not infer
a local crossing-through-cup identity from Hopf intertwining, define a
new semicyclic ribbon invariant, or move a cap through an arbitrary
exterior. No such move is needed for (16).

## 5. Exact averaged-Gram transport with all physical channels

For each labeled slice define the actual canonical Gram
\[
 J_{\boldsymbol\nu}
       =\sum_{k=0}^{N-1}(T_{\boldsymbol\nu}^k)^*
                                  T_{\boldsymbol\nu}^k .
 \tag{17}
\]
As in [C], \(J_{\boldsymbol\nu}\succeq I\),
\(T_{\boldsymbol\nu}^*J_{\boldsymbol\nu}T_{\boldsymbol\nu}
=J_{\boldsymbol\nu}\), and it commutes with the physical unitary
\(K_\Sigma\). These facts need only (15), not the all-equal fixed
line used for the sharp asymptotic in [C].

If \(A\) is any actual rectangular intertwiner
\(T_{\rm out}A=AT_{\rm in}\), then
\[
 \|A v\|_{J_{\rm out}}^2
    =\sum_{k=0}^{N-1}\|A T_{\rm in}^kv\|_{\rm ph}^2
    \le\|A\|_{\rm ph}^2\|v\|_{J_{\rm in}}^2 .
 \tag{18}
\]
Thus \(\|A\|_{J_{\rm out}\leftarrow J_{\rm in}}\le\|A\|_{\rm ph}\).
For an invertible crossing the same statement applies to its
actual inverse between the reversed fibers. This is a comparison
in different inherited Grams, not a fixed-metric unitarity claim.

Let \(C\) insert the literal cup and \(B\) apply the ordinary cap,
with identity operators on all other heads. Equations (12), (15)
give the stronger exact cup identity and cap bound
\[
 C^*J_{\rm out}C=N^3J_{\rm in},\qquad
 B^*J_{\rm out}B\preceq N^{-1}J_{\rm in}.
 \tag{19}
\]
The first follows by putting \(C^*C=N^3I\) inside the sum (17).
The second is (18) with \(\|B\|_{\rm ph}=N^{-1/2}\).
Hence \(C_{\rm iso}=N^{-3/2}C\) is an isometry and
\(B_{\rm ctr}=N^{1/2}B\) is a contraction.
The cap is neither asserted coisometric nor the Gram adjoint of
that cup.

If the fixed presentation has \(h\) births and \(h\) deaths, replacing
its turns by \(C_{\rm iso},B_{\rm ctr}\) yields a normalized word
\(\widetilde{\mathcal A}_\mu\) with the exact restoration
\[
              \mathcal A_\mu=N^h\widetilde{\mathcal A}_\mu .
 \tag{20}
\]
In particular a normalized snake equals \(I/N\), not \(I\).
For example (18)--(20) give the source-preserving upper estimate
\[
 |K_N(\mathscr D)|\le
   |\chi_N|\,N^h
       \prod_{\text{crossings }v}\|R_{v,\mu}\|_{\rm ph},
 \tag{21}
\]
when \(\chi_N\) collects exactly the separately retained original
scalar lines. No new estimate on the crossing product is asserted.

## 6. Scope and closest coverage

The construction supplies a single source-compatible positive-metric
system for a fixed original cut through variable odd widths.
It retains every physical tensor coordinate. No multiplicity or
normal direction is removed by a quotient or an eigenvalue-only
Casimir specialization, and no cap-tree projection is inserted in
a neighboring crossing.

[R] already constructs oriented source duality and explains its
degenerate fusion character. [S] already controls the original marked
density in its complete fixed-width graph Gram. [A] already gives
coisometric ordinary-cap tree packets after their specific
factorial gauges. The additional statement here is the opposite-center
E-source assignment through the fixed original Morse diagram,
its full one-cut preservation, and the exact cross-width identities
(18)--(20) in the canonical averaged Grams.

The norm of the completed matrix in (16) is of course \(|K_N|\)
in its one-head Gram. This is the existing scalarity identity, not
a separately growing positive energy. The zero bubble in (12)
explicitly prevents treating ordinary closure as a positive norm.
No geometric boundary packet, nonzero marked overlap, lower bound for
\(K_N\), or finite-exception volume theorem follows from these facts.
Nothing here supplies off-root or quantum-normal estimates.

## Complete inputs and coverage

All six complete matching texts were read. Only written mathematics
and text/hash operations were used. No earlier final was edited.

| Label | Complete text | SHA-256 |
| --- | --- | --- |
| B, source, 247 lines | [Balanced cyclic source](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/balanced_verma_coherent_braiding.md) | 0203bdd7dbb36a4f8deb1c310b3445608e53d10922049447da8eecec4f87d1c4 |
| P, source, 229 lines | [Literal original turns](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_plat_cup_cap_gram_support.md) | d780592fac1067eba868d2a8939ea1bf6a4191361d1c100eefe789833fe1451d |
| C, source, 376 lines | [Canonical coproduct Gram](research_sharp_physical_coproduct_gram.md) | 6fcdfbece5d9f06c541649926345876aab8daf6dee09022160e79d99a02bafeb |
| R, coverage, 658 lines | [Oriented source duality](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/relative_pivotal_duality.md) | e763274b97cee5227dbace45bae17557d2df6d7e80dc934c02db4a8b163970c2 |
| S, coverage, 367 lines | [Original source in the graph Gram](research_original_source_in_coproduct_graph_gram.md) | 92e6ed646ec359bd85c7245a12c5d98210b37043bdcfd2026c8693d56ff3de6b |
| A, coverage, 226 lines | [Complete ordinary-cap trees](actual_cap_tree_angle_energy.md) | ecaf7177962dfa5a944a532fed37d505b97e81361926039f69cbf7f9b674a2da |
