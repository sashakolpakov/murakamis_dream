# Removing all upper transitions from a nonlow mixed region

Research theorem, 5 November 2026. This combines the completed coherent
and mixed raw/coherent height comparisons and horizontal clamps,
including the two-raw case. No new parameter cover is required.

The conclusion is a pointwise upper-rate comparison on the entire
nonlow mixed region \([.1,1]^m\), for every fixed cyclic word and
selection. It removes every coordinate in \((.45,.5)\), while keeping
all edges incident to the original right region raw. It does not prove
the remaining lower-transition/right comparison or a whole-period
asymptotic.

## 1. Fixed labels and the original upper envelope

Fix the original cyclic type word, its actual zero-lift critical
reference \(r\), and allowed selection indicators
\(\sigma_j\in\{0,1\}\), with \(\sigma_j=0\) at type three. Write
\(c_j=\Im r_j\), \(H=7/500\), and use the
[periodic split-cutoff graph](research_mixed_split_cutoff_hybrid_contour.md).
On the present nonlow domain its formulas are
\[
 L_s(x)=\min\{1,(x-.1)/.12\},\quad
 L_f(x)=\min\{1,(x-.1)/.02\},\quad
 R(x)=
 \begin{cases}1&x\le.45,\\400(.5-x)^2&.45\le x\le.5,\\0&x\ge.5.\end{cases}
 \tag{1}
\]
The arguments of \(L_s,L_f\) are always at least .1. A row uses
its own selection to choose the cutoff:
\[
 z_j=x_j+i h_j,\qquad
 h_j=
 \begin{cases}
 c_jR(x_j)\min_{k\in N(j)}L_s(x_k),&\sigma_j=0,\\
 HR(x_j)\min_{k\in N(j)}L_f(x_k),&\sigma_j=1,
 \end{cases}
 \quad N(j)=(j-1,j,j+1).
 \tag{2}
\]
Indices and incident edges are cyclic and retain their literal
multiplicities.

Choose labels once, from the original real coordinates:
\[
 \mathcal R=\{j:x_j\in[.5,1]\},\qquad
 \mathcal U=\{j:x_j\in(.45,.5)\},\qquad
 \mathcal A=\{1,\ldots,m\}\setminus\mathcal R.
 \tag{3}
\]
An edge with an endpoint in \(\mathcal R\) is bounded by its
**complete sum of absolute original finite rows**, with the original
chirp and both allocated half-Fourier factors. Every other edge uses
its original coherent conditional phase and complete packet.
These edge labels remain fixed during all comparisons.

Let \(\mathcal E_{\mathcal R}(x,\sigma)\) denote the resulting sum
of upper rates. For a coherent edge with types \((\eta,\epsilon)\),
its contribution is
\[
 \Re\phi_{\eta,\epsilon}(z_j,z_{j+1})
   +\frac{\sigma_j}{2}\chi(z_j)
   +\frac{\sigma_{j+1}}2\chi(z_{j+1}),\qquad
 \chi(z)=\max\{\Re g(z),-2\pi\Im z\},
 \tag{4}
\]
where
\(g(z)=(\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6)/(2\pi i)\).
For a raw edge, use its full real-row envelope, with the actual
Fourier upper rate; no conditional saddle is assigned to that edge.
At a real right endpoint \(1/2\), its Fourier upper rate is zero
for either selection, including the forcing tie.

The [complete right-angle reduction](research_mixed_complex_right_row_reduction.md)
gives
\[
 \mathcal E_{\mathcal R}(x,\sigma)
 \le \mathcal E_{\mathcal R}(x^{R},\sigma),\qquad
 x_j^{R}=
 \begin{cases}1/2&j\in\mathcal R,\\x_j&j\notin\mathcal R.\end{cases}
 \tag{5}
\]
Every other height is unchanged, since both left cutoffs equal one
on the entire right interval. If the expression is written as
defects against the original planes \(\Gamma_j\), their moving
right-coordinate slopes cancel by the original complex critical
equations. Equation (5) is a global envelope comparison, not a
claim that each individual plane-subtracted raw edge is maximized
at \(1/2\).

## 2. Selection removal and horizontal clamping

For \(j\in\mathcal U\), put
\[
 t=x_j,\quad d=.5-t,\quad
 s_j=\min\{L_s(x_{j-1}),L_s(x_{j+1})\},\quad
 f_j=\min\{6s_j,1\}.
 \tag{6}
\]
Its own cutoff is one. The two possible row heights are
\(c_js_jR(t)\) and \(Hf_jR(t)\). The relation
\(L_f=\min(6L_s,1)\) proves (6), also when neighbors coincide.
All these quantities are unchanged by any other upper-transition
motion: throughout \([.45,.5]\), both left cutoffs are one.
Changing a selection affects only that row's height, because the
cutoff in every other row is chosen by that other row.

Define the positive constants
\[
 \kappa_F=.028\pi-.0426,\qquad
 \kappa_G=\log(2\sin(.45\pi))-.639 .
 \tag{7}
\]
The necessary local inputs, classified by the number of **incident
raw edges** at the moving coordinate, are:

| Raw incidences | Selected-to-unselected comparison | Unselected horizontal comparison |
|---|---|---|
| zero | [coherent selected-height removal](research_mixed_right_selected_height_removal.md), (8) | [coherent clamping](research_mixed_unselected_right_clamping.md), (5) |
| one | [mixed height bounds](research_mixed_raw_coherent_height_bounds.md), through the [height-comparison lemma](research_mixed_raw_coherent_height_comparison.md), (8) | [mixed clamping](research_mixed_raw_coherent_right_clamping.md), (4) |
| two | the two-raw case of the same mixed height bounds | [two-raw clamping](research_mixed_two_raw_right_clamping.md) |

For every selected upper coordinate, these comparisons erase its
selection at fixed real \(t\), at rate loss at least
\[
 b_j=\min\{\kappa_F f_jR(t),\kappa_G(.5-t)\}\ge0.
 \tag{8}
\]
The two half-corrections in (4), or their raw counterparts, combine
to the one full correction \(\chi(z_j)\). Every other selected
correction is fixed. The height comparison retains both Fourier
branches; it does not assert monotonicity of the selected contour.

After selection removal, \(k_j=c_js_j\) belongs to
\([-.03,.02]\) at type three and \([-.057,0]\) at type four.
The appropriate horizontal comparison moves
\(t+ik_jR(t)\) down to \(.45+ik_j\). In all three cases its
upper-rate loss is at least
\[
                         (t-.45)/20 .
 \tag{9}
\]
The coherent case has the stronger coefficient \(1/10\).
Neighboring nonright targets lie in the full typed polygons
\(\Omega_3,\Omega_4\) of the cited theorems, including their
selected caps and partially attenuated heights. Right neighbors
are fixed real \(1/2\). The coherent source theorems apply to
every changed coherent edge; the raw edges retain their full
finite row bounds.

For a two-cycle with one right coordinate, the two raw incidences
are two distinct parallel edges, with independent optimizing rows.
For a two-cycle with no right coordinate, the two coherent
neighbors coincide, as allowed in the coherent theorem. A one-cycle
has either one raw right loop and no upper coordinate, or one
coherent loop. In the latter case use the proved diagonal identity
\[
 \frac{d}{dz}\phi_{\alpha,\alpha}(z,z)
 =(\phi_{\alpha,\alpha})_a(z,z)+(\phi_{\alpha,\alpha})_b(z,z);
 \tag{10}
\]
the coherent height and horizontal comparisons apply to that
single loop. The loop is not counted twice.

## 3. Global reduction and finite-source consequence

Let
\[
 x'_j=\begin{cases}
 1/2&j\in\mathcal R,\\
 .45&j\in\mathcal U,\\
 x_j&\text{otherwise},
 \end{cases}
 \qquad
 \sigma'_j=\begin{cases}0&j\in\mathcal U,\\\sigma_j&\text{otherwise}.
 \end{cases}
 \tag{11}
\]
**Theorem 1.** Every actual typed cyclic reference and every allowed selection
satisfy
\[
 \boxed{\ 
 \mathcal E_{\mathcal R}(x,\sigma)
 \le \mathcal E_{\mathcal R}(x',\sigma')
       -\frac1{20}\sum_{j\in\mathcal U}(x_j-.45)
       -\sum_{\substack{j\in\mathcal U\\\sigma_j=1}}b_j .
 \ }
 \tag{12}
\]
The comparison is uniform in the original nonlow target domain
for each fixed word.

After (5), process the upper coordinates in any fixed order.
Removing their selections and moving their real coordinates
changes no other height. All remaining local domains therefore
stay valid, even when upper coordinates are adjacent. At each
step the change in the global rate is exactly the sum of its
incident edge changes, with the loop convention (10).
These changes telescope; no edge is assigned a second independent
debit. Equations (8)--(9) sum to (12). The final points and
selections are precisely (11), on the same hybrid graph.

For the literal original allocated product, its fixed scalar
normalization, and the graph Jacobian at every differentiability
point of the graph (hence almost everywhere for integration), the completed source
estimates give, for every fixed \(\delta>0\),
\[
 |\mathcal D_{N,\sigma}(z(x,\sigma))\,
       \det(I+iD\mathcal H_\sigma)|
 \le C_\delta N^A
 \exp N\!\left\{\mathcal E_{\mathcal R}(x',\sigma')
       -\frac1{20}\sum_{\mathcal U}(x_j-.45)
       -\sum_{\mathcal U\cap\{\sigma=1\}}b_j+\delta\right\}.
 \tag{13}
\]
There are finitely many edges for the fixed word. Give their
Fourier/source upper bounds a total tolerance below \(\delta\)
once, before using the rate comparisons. Polynomial factors and
the fixed graph-Jacobian bound are absorbed in \(C_\delta N^A\).
This is not a comparison with a nonzero finite kernel at the
mapped point, nor a change of variables in the contour integral.
The mapped source may have zeros without invalidating (13).

Thus the remaining nonlow pointwise problem lies on the strictly
smaller marked domain
\[
       x'_j\in[.1,.45]\ \text{or}\ x'_j=1/2\text{ with label }\mathcal R,
       \qquad \sigma'_j=0\text{ at every newly clamped coordinate}.
 \tag{14}
\]
Lower-transition/right configurations in this domain are not
bounded by (12). No enlarged knot family, whole-period central
coefficient, or arbitrary-short filling conclusion follows from
this reduction alone.

## 4. The local early–plateau–upper–right debit

The originally motivating chain has ordered real regions
\(E\!-\!P\!-\!U\!-\!R\), where
\(E=[.1,.12]\), \(P=[.22,.45]\), and its reverse is also allowed.
At the \(U\) coordinate, the neighboring \(P,R\) cutoffs are both
one. Apply the one-raw comparisons above. Its target becomes
\(.45+ic_U\), unselected, while the partially attenuated \(P\)
target is fixed.

For an unselected \(P\) leg, the
[oriented one-height reset theorem](research_mixed_oriented_height_reset.md)
bounds the coherent \(P\!-\!U\) defect by \(q_Pc_P^2\), where
\(q_P=11/2\) in the forward chain and \(151/20\) in the reverse.
For a selected \(P\) leg, separate height convexity reduces its
height segment to zero and \(H\). At zero its selected correction
is zero and the same oriented bound applies. At \(H\), the
[selected-plateau theorem](research_mixed_selected_plateau_support.md)
gives a negative defect. Thus \(q_Pc_P^2\) remains a valid
bound for every actual partial \(P\) height and selection.

At \((.45+ic_U,1/2)\), in either order, the
[complete upper-transition/right source bound](research_mixed_upper_transition_right_support.md)
has an underlying raw support gap at least \(1/1000\).
The coefficient of the moving \(U\) target in the two original
planes cancels by the actual critical equation. Consequently
\[
 \mathcal C_{PU}+\mathcal R_{UR}
       -\Re(\Gamma_{PU}+\Gamma_{UR})
 \le q_Pc_P^2-\frac1{1000}.
 \tag{15}
\]
Here \(\mathcal C\) is the coherent allocated rate and
\(\mathcal R\) the complete raw allocated rate, not a coherent
replacement of the right edge. A single combined tolerance below
\(1/2000\) gives finite reserve \(1/2000\).
This pays the particular early oriented credit without requiring
an independent-height \(Q/Q\) reset theorem. Its use in a larger
allocation still requires that every early credit and raw edge
be counted only once.

## 5. Focused verification

The checker binds the completed source records and the final 384-bit
saved replays of the 77 height, 96 mixed-clamp and four two-raw
families. It exhausts their unchanged split/reduction trees, including
the degenerate first parameter of the two-raw height cases, and checks
the exact cutoff and scalar-budget identities. The 1,092 cyclic-label
patterns through length six are incidence diagnostics; the all-length
proof is the local identity and telescoping argument above.
The canonical run passes 30 checks, 14 primary records and 350 current
file bindings. It recomputes no numerical source or derivative cover.

    python3 experiments/check_mixed_nonlow_upper_transition_removal.py
    python3 experiments/check_mixed_nonlow_upper_transition_removal.py --input repro/results/research-mixed-nonlow-upper-transition-removal.json --output /tmp/research-mixed-nonlow-upper-transition-removal-review.json
