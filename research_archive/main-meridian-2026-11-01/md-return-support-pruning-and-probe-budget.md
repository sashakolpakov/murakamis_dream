# Return support, terminal complete branches, and the missing gluing budget

Private lemma, 1 November 2026. No repository file is changed.

The exact coefficient input is `/private/tmp/md-fixed-newton-return-gates-and-contracted-tensor.md`. This report proves a tree statement under an explicit edge hypothesis. It explains when the old high-output estimate applies to actual complete branches, and why those estimates alone do not give a global meridian bound. A final exact example shows why the edge hypothesis cannot be omitted for higher-valence multiplication hubs.

## 1. The tensor convention and hypotheses

Fix \(N\ge2\), \(d=N-1\), and \(M=\lfloor d/2\rfloor\). A label \(r\in\{0,\ldots,d\}\) is low if \(r\le M\) and high otherwise.

Consider a finite connected trivalent tree. Its external legs carry labels, and each internal edge identifies the two incident labels. Every external label is assumed low. Each trivalent vertex has been assigned one of the two nonzero support types of the fixed-coordinate covariant tensor
\[
V_s(i,j,k)=\phi_s(e_i*_se_j*_se_k).
\]
The complete type has
\[
i+j,\ i+k,\ j+k\le d,\qquad i+j+k\ge d.
\tag{1}
\]
The return type has
\[
i+j,\ i+k,\ j+k\ge N,\qquad i+j+k\ge2N-1.
\tag{2}
\]
Only assignments satisfying these exact integer inequalities are considered.

The equal-label edge condition has physical content. With this covariant tensor, the inverse Frobenius metric contracts complementary labels. A physical complete turn is reversal, so an edge with a turn contracts equal labels instead. The actual fixed-frame deformed turn adds a bounded diagonal factor and does not change this support. Thus this lemma applies to a trivalent reduced tree all of whose internal edges carry turns. It does not automatically apply to a binary resolution of a higher-valence multiplication hub: the auxiliary edges introduced by that resolution are unturned and contract complementary labels.

A complete vertex has at most one high incident label, since two high integers have sum at least \(N\). A return vertex has at least two high incident labels, since two low integers have sum at most \(2M\le d\).

## 2. Two exact counting statements

First retain only the high internal edges. No high edge ends on an external leg. Every nonempty connected component of this forest containing a return vertex has return vertices of degree two or three and complete vertices of degree one. If \(R\) denotes its return vertices and \(L\) its complete leaves, the tree degree identity gives
\[
|L|=2+\sum_{v\in R}\bigl(\deg_{\mathrm{high}}(v)-2\bigr)\ge2.
\tag{3}
\]
In this formula all degrees count high incident edges only. In particular a complete leaf of this high-edge forest need not yet be a complete terminal subtree of the original tree: its low edges could lead to further returns. The next argument removes that ambiguity.

Partition the full trivalent tree into maximal connected vertex regions of one type, complete or return. Contract each such region to a vertex. If there is at least one return vertex, the resulting component graph is a finite bipartite tree with both types present.

Every return region has at least two high boundary edges to complete regions. To prove this, let it contain \(q\) vertices and let \(E_h\) be its number of internal high edges. Every one of its vertices has high degree at least two, and no external physical leg is high. Hence its number \(b_h\) of high boundary edges satisfies
\[
b_h=\sum_{v}\deg_{\mathrm{high}}(v)-2E_h
   \ge2q-2E_h\ge2,
\tag{4}
\]
because the internal high graph is a forest. This argument allows low edges inside the return region.

**Terminal-branch lemma.** There are at least two leaf complete regions in the component tree whose unique boundary edge is high.

For a proof, remove from the component tree every leaf complete region whose unique boundary edge is low. This removes only low edges. Each return region therefore retains its at least two high boundary edges. A complete region which was not a leaf loses no edge in this operation, since all its neighbors are return regions; its degree remains at least two. The remaining graph is a nonempty connected finite tree. Its leaves can only be the unremoved complete regions that were already leaves, with high boundary edge. A finite nontrivial tree has at least two leaves. This proves the assertion without replacing a high-edge leaf by an unjustified old subtree.

## 3. When the old probe theorem applies

Each terminal complete region found above is a genuine one-output complete subtree. All its vertices use the old tensor, every internal edge has its original turn, and its other external legs are low effective inputs. If the region contains \(v\ge1\) trivalent vertices, then its number of external legs is \(v+2\); after removing its unique output, it has \(v+1\ge2\) inputs. No one-input exceptional case is hidden in the argument.

Suppose those effective input arrays satisfy the established coefficient cone
\[
|f_{a,N,r}|\le
\begin{cases}
\exp\{N(c_a+g(r/N)+o(1))\},&r\le M,\\
0,&r>M,
\end{cases}
\tag{5}
\]
with uniform error, where \(g(u)=J(2u)-4J(u)\) and
\(J(u)=\int_0^u\log(2\sin\pi t)\,dt\).
The old unflagged-core probe theorem applies to this exact region. Restricting its boundary arrays to low coordinates is allowed because that theorem is an upper statement for arbitrary arrays in the cone.

If the unturned output is \(A_N\), then the covariant boundary index \(r\) selects
\[
\phi(e_rA_N)=[e_r]T_0(A_N).
\tag{6}
\]
The high boundary identified in Section 2 is therefore exactly a high output coordinate in the theorem, rather than its complement. For some fixed \(\gamma_A>0\), the whole high output part has the bound
\[
\|(T_0A_N)^{\mathrm{hi}}\|_{\mathrm J}
\le\exp\{N(\Omega_A-\gamma_A)\}.
\tag{7}
\]
The budget \(\Omega_A\) is the intrinsic complete probe action for this region, including its input constants. Every internal turn edge of this complete region also has a bounded paired factor. Taking magnitudes termwise in its old positive state sum multiplies that majorant by at most \(C_R^{E_A}\), where \(E_A\) is the fixed number of internal edges. Its multiplication vertices are in the selected complete sector, so they retain exactly the old positive coefficients. Thus these internal weights do not alter the exponential bound. For the outgoing deformed turn, use the positive coefficient majorant in equations (8) and (11) of the old probe theorem, before cancellations: each reversed Newton coefficient is multiplied by the paired factor \(\gamma_N(s)W_{d-r}(s)/H_N(s)\), uniformly bounded for \(|s|\le R<1\). Its high-band positive coefficient sum therefore changes by at most a bounded factor, and the existing polynomial basis-to-\(\mathrm J\) conversion gives (7), with a smaller fixed gap if necessary. This is not an inference from the norm of a signed output alone. The separate direct full-\(\mathrm J\) multiplier comparison has polynomial, rather than bounded, cost and is currently proved on \(|s|\le1/16\). Thus at least two actual complete branches in every supported return sector have a strict high-output deficit relative to their own intrinsic budgets.

This is conditional on (5). The lemma does not establish the moving-main-meridian coefficient cone for the original physical leaves. It also makes no assertion that all other branches left after cutting one return region are complete; other return regions may remain.

## 4. The budget that cannot be omitted

The existence of two deficits does not show that their budgets fit below the action of the original connected source. The issue can be stated exactly in boundary variables.

For a complete branch \(b\), let \(f_b(t)\) denote its prescribed-boundary coefficient action in the covariant coordinate of (6). Define the probe weight
\[
w(t)=\begin{cases}g(t),&0\le t\le1/2,\\0,&1/2<t\le1.\end{cases}
\tag{8}
\]
The probe theorem supplies an intrinsic budget \(\Omega_b\) with
\[
f_b(t)+w(t)\le\Omega_b,
\qquad
f_b(t)\le\Omega_b-\gamma_b\quad(t>1/2)
\tag{9}
\]
on its feasible support. For the positive reference arrays, the optimized probe attains its advertised complete action. Define the nonnegative loss
\[
\ell_b(t)=\Omega_b-f_b(t)-w(t).
\tag{10}
\]
The high inequality says \(\ell_b(t)\ge\gamma_b\) on the high range.

Cut any fixed region from the original all-complete positive source, and write \(G_{\mathrm{cut}}\) for the sum of the actions in that region, retaining all its internal variables. Let \(t_b^*\) and the internal cut variables be their values at the original complete maximum. The branch profiles are optimized with these prescribed boundary values. If all complementary components are the listed branches, then
\[
\Phi=G_{\mathrm{cut}}(t^*)+\sum_b f_b(t_b^*),
\]
and hence the exact accounting identity is
\[
\boxed{\quad
\sum_b\Omega_b-\Phi
=\sum_b\ell_b(t_b^*)
 +\sum_b w(t_b^*)-G_{\mathrm{cut}}(t^*).
\quad}
\tag{11}
\]
If an additional component remains, its prescribed-boundary action must appear on both sides; it cannot be discarded.

The term \(\sum_b w-G_{\mathrm{cut}}\) is the contribution of closing the separated branches by probes instead of joining them through the original region. The separate nonzero gaps \(\gamma_b\) in (9) do not estimate this term or the losses at \(t_b^*\). Thus no inequality \(\sum_b\Omega_b\le\Phi\) has been proved.

For a single return region with otherwise complete branches, its local action is nonpositive. Substituting (9) gives the legitimate bound
\[
\text{return-sector action}\le\sum_b\Omega_b-
       \sum_{\text{forced high }b}\gamma_b.
\tag{12}
\]
Comparison of (12) with \(\Phi\) requires precisely the missing gluing-budget inequality (11), or a stronger coupled estimate that retains the boundary variables. With several return regions the same issue occurs at each cut; repeating the one-output norm bound does not make the budgets additive.

## 5. Why arbitrary multiplication valence needs a different argument

There is an exact infinite-level family showing that an all-low external assignment can return inside a single higher-valence hub. This is a statement about the actual algebraic kernel, not a knot or a claim about its final invariant.

At even levels \(N\ge8\), set \(M=(N-2)/2\) and take the five factors
\[
F_N=e_M^4e_3.
\]
At odd levels \(N\ge3\), set \(M=(N-1)/2\) and take
\[
F_N=e_M^4e_1.
\]
All five Newton indices are low. In both cases \(\deg F_N=2N-1\), and its leading coefficient is nonzero. Divide once by the monic polynomial \(P_0\):
\[
F_N=P_0Q_N+R_N,\qquad \deg Q_N=d,\quad\deg R_N<N.
\]
Reduction modulo \(P_s\) is exactly \(R_N-\Delta_sQ_N\). Since the leading coefficient of \(Q_N\) is that of \(F_N\),
\[
\boxed{\quad
\phi_s(F_N)-\phi_0(F_N)
=-\Delta_s(-1)^dN^2\operatorname{coeff}_{z^{2N-1}}F_N\ne0
\quad}
\tag{13}
\]
whenever \(\Delta_s\ne0\). This argument uses only polynomial degree and the exact top-coefficient trace. It is not a numerical experiment.

In a trivalent resolution of this five-input multiplication hub, some internal edges are unturned. They identify complementary cubic labels, allowing the return sector despite low external labels. Thus the support lemma of Sections 1–2 is valid as stated, but cannot be extended to all strict trees by silently treating these resolution edges as turn edges. An arbitrary-valence argument must retain that distinction or work directly with the full hub tensor.

## 6. Remaining precise task

For the equal-edge trivalent class, two terminal complete branch losses are rigorously available under the original input cone. A global conclusion still needs the coupled pressure comparison in (11). For arbitrary hubs, even the all-low return support requires an additional argument, as (13) demonstrates. These are distinct obligations. Neither is removed by the polynomial bounds for individual return coefficients or by the relative spectral norm estimate for one turn.
