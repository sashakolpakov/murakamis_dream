# Several high incidences at a moving whole junction

Private derivation, 1 November 2026. No repository files are changed.

A pointwise moving-to-complete trace comparison fails for a whole junction with one high incidence. This note treats a different sector: at least two high incidences at a moving junction. Its absolute rate can be placed in the same original complete action by replacing those incidences simultaneously by half labels. The replacement works at arbitrary fixed valence. It uses the full junction, not an artificial trivalent resolution of its moving tensor.

The conclusion is a sector estimate. Every other moving junction must have all incidences low, so that its existing same-level whole-trace comparison applies, or must already have an independently justified complete positive majorant. The one-high moving junctions in the counterexample are not covered.

## 1. Fixed polynomials, actual types, and the finite cardinal identity

Put \(d=N-1\), \(M_N=\lfloor d/2\rfloor\), and
\[
 c_j=2\cos\frac{(2j+1)\pi}{N},\qquad
 S_n=\prod_{r=1}^n2\sin\frac{\pi r}{N},\qquad
 e_n(z)=S_n^{-2}\prod_{j<n}(c_j-z).
 \tag{1}
\]
An incidence is low if \(n\le M_N\), and high otherwise. The actual orientation type chooses either the constant quotient \(P_0=\mathcal T_N+2\), or the moving quotient
\[
 P_s=\mathcal T_N+2\cos(2\pi s),\qquad
 \phi_s(F)=(-1)^dN^2[z^d]\operatorname{rem}_{P_s}F.
 \tag{2}
\]
The full polynomial quotient retains every repeated-node first normal. The actual six-type turn compiler makes the moving equal-color junctions an independent set along original physical quarter-turn edges. A turn edge identifies the same covariant index at its ends and contributes its prescribed bounded paired factor. None of these assertions applies to an unturned edge introduced by a binary resolution.

For odd \(N=2m+1\), the complete quotient has \(m\) double nodes \(c_0,\ldots,c_{m-1}\) and the simple node \(c_m=-2\). The polynomial \(e_m^2\) vanishes to order two at all the double nodes. Moreover,
\[
 e_m(-2)=\frac{N}{S_m^2}=1,
 \qquad \phi_0(e_m^2)=1.
 \tag{3}
\]
The first equality follows from \(S_m^2=N\); the second also follows directly from the top coefficient of the degree-\(d\) polynomial \(e_m^2\). Thus \(e_m^2\) is the full Hermite projector onto the simple node, with trace one. For any polynomial \(F\),
\[
 e_m^2F\equiv F(-2)e_m^2\pmod {P_0},
 \qquad \phi_0(e_m^2F)=F(-2).
 \tag{4}
\]
In particular, for every fixed \(D\), every \(r\ge2\), and low indices \(n_1,\ldots,n_{D-r}\),
\[
 \phi_0\left(e_m^r\prod_{j=1}^{D-r}e_{n_j}\right)
       =\prod_{j=1}^{D-r}e_{n_j}(-2).
 \tag{5}
\]
There is no missing nodal multiplicity or derivative contribution in (4): both first jets vanish at each double node.

Define
\[
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,
 \qquad g(x)=J(2x)-4J(x),\quad 0\le x\le\tfrac12.
 \tag{6}
\]
Uniform endpoint sine-product estimates give
\[
 \frac1N\log e_n(-2)=g(n/d)+O\!\left(\frac{\log N}{N}\right)
                  \quad(0\le n\le m).
 \tag{7}
\]
Here and below labels in the real action are normalized by \(d\). Replacing \(n/N\) by \(n/d\) changes the closed entropy by at most \(O(\log N/N)\), including endpoints.

Let \(V_D\) be the old whole-junction action obtained by maximizing the sum of the positive binary gate actions in any prescribed resolution. Its closed support is
\[
 x_i\ge0,\qquad x_i+x_j\le1\ (i\ne j),\qquad \sum_i x_i\ge1.
 \tag{8}
\]
The exact positive resolution and uniform closed factorial estimates identify this action with the logarithmic rate of the complete tensor. The lattice on a fixed rational face is the original primitive lattice; integer approximation along the odd half-label face preserves its equalities. Applying (5) and then continuity of the closed action proves
\[
 \boxed{\quad
 V_D(\underbrace{\tfrac12,\ldots,\tfrac12}_{r\ge2},
                  x_1,\ldots,x_{D-r})
       =\sum_{j=1}^{D-r}g(x_j),\qquad 0\le x_j\le\tfrac12.
 \quad}
 \tag{9}
\]
The action is parity-independent. Odd levels establish the exact calibration in (9); (9) is not an assertion that the same simple-node projector exists at even levels. The boundary value also includes zero low labels and additional half labels, since \(g(0)=g(1/2)=0\).

## 2. A uniform absolute bound for the moving tensor

The complete spectral norm \(\mathcal J\) contains values and first normals at the complete double nodes. The full-jet Newton estimates give
\[
 \|e_n\|_{\mathcal J}\le N^C
 \begin{cases}
  \exp\{Ng(n/d)+O(\log N)\},&n\le M_N,\\
  1,&n>M_N.
 \end{cases}
 \tag{10}
\]
Canonical degree-\(<N\) sup norms, Chebyshev coefficient norms and \(\mathcal J\) are polynomially equivalent. For a fixed number \(D\) of factors, raw polynomial multiplication, canonical reduction modulo \(P_s\), and the top-coefficient trace each have polynomial norm cost, uniformly on every fixed disk \(|s|\le R<1\). The reduction estimate is the finite Chebyshev folding bound; it does not compare the moving product with a possibly zero complete product.

Consequently, for every index tuple, not only complete-admissible ones,
\[
 \sup_{|s|\le R}\left|\phi_s\left(\prod_{i=1}^D e_{n_i}\right)\right|
  \le N^{C_{D,R}}
       \exp\left\{N\sum_{i:\,n_i\le M_N}g(n_i/d)\right\}.
 \tag{11}
\]
The value of \(C_{D,R}\) may depend on fixed valence and radius. It does not depend on the labels or their proximity to half. The inherited paired turn factors contribute another bounded factor for each of the fixed number of physical edges. Equation (11) follows from the same estimates used in `notes/actual_main_meridian_source_bounds.md`, Section 3.4; no replacement of first normals by zero nodal values is made.

When at least two indices are high, (9) gives a complete junction whose action is exactly the upper action in (11): replace every high index by half, and leave every low incidence as a free variable. The replacements at different junctions must still be made consistently. The next section supplies that consistency using the actual neighboring pressures.

## 3. The sector and the neighboring old regions

Consider a fixed tree of whole product junctions of full valence at least three. Every junction-to-junction edge is an original physical quarter-turn. The external inputs satisfy the original coefficient cone
\[
 |f_{i,N,n}(s)|\le \exp\{N(c_i+\epsilon_N)\}
 \begin{cases}e^{Ng(n/d)},&n\le M_N,\\1,&n>M_N,\end{cases}
 \qquad \epsilon_N\longrightarrow0.
 \tag{12}
\]
Close an output probe in the same way if a branch norm is being estimated. All constants \(c_i\) are retained. Assume the complete reference of this fixed closed tree has its original unique strict maximizing state and action \(F_0\).

Fix a band sector subject to the following conditions.

1. There is a nonempty set \(\mathcal B\) of moving junctions with at least two high incidences each. Their whole tensors are bounded by (11).
2. Every other moving junction has all its incidences low and is bounded by the established same-level positive whole-trace comparison. Alternatively an independently proved complete positive majorant at precisely those labels may be supplied.
3. Constant-quotient junctions retain their exact positive complete tensors. Terms outside their complete support are zero.

In particular, an uncontrolled moving junction with exactly one high incidence is excluded. The pointwise counterexample shows why this is a substantive restriction.

Actual typing makes the vertices in \(\mathcal B\) pairwise nonadjacent. After their removal, the surviving graph is a collection of old regions. Each old junction has at most one strictly high incidence, since its complete support has every pair sum at most \(d\). At every high interface to a deleted junction prescribe the label as a marked boundary. If an original external input is high, its variable action in (12) is zero; mark this boundary as well, retaining its constant. Thus each old junction has at most one mark.

At every low arm from a deleted junction to an old region, add the profile \(g(x)\) from (11) to that region and optimize this arm as an ordinary boundary variable. Each such profile belongs to exactly one region: deleted junctions are nonadjacent. Every original low external input retains its own \(g+c_i\). All other original constants are retained once and only once.

The general old simultaneous-half lemma, proved in `/private/tmp/md-old-whole-hub-simultaneous-half-pressure.md`, applies to each region with marks. It retains the original positive resolved action and every artificial unturned wire. It states
\[
 \Psi(\mathbf z)\le\Psi(\tfrac12\mathbf1)
                    \quad\text{for all feasible }\mathbf z\ge\tfrac12\mathbf1.
 \tag{13}
\]
An unmarked old region is simply optimized with its ordinary boundary profiles. The hypothesis of (13) is satisfied here because no old junction has two marks. The half/three-eighths strict witness is assigned on physical edges only, with the hidden product wires constructed by the exact fixed-association interval lemma. Thus (13) does not assume independent capped pressures or reset a neighboring completed branch to \(g+c\).

## 4. Simultaneous reassembly and its strict gap

Choose maximizing states of the old regions after (13). Their low-arm boundary labels may have changed; their new values are shared with the corresponding deleted junctions. Replace every high incidence at each deleted junction by half. All these replacements agree across an internal edge, because the other endpoint was marked and clamped. By (9), the reinserted complete junction contributes exactly the sum of the \(g\) profiles already charged on its low arms.

This is an accounting identity, not an added action. Remove each fictitious low-arm \(g\) from its neighboring region when the complete junction is reinserted; the same value is now supplied by (9). Original boundary profiles remain where they were. The two external-arm cases are also exact:

- A high original external input becomes half. Its variable cone action was zero, and the complete leaf has \(g(1/2)=0\).
- A low original external input retains its original \(g(x)+c_i\), while the deleted-junction upper bound supplies a second \(g(x)\). The reinserted complete hub supplies precisely that second term. The label can be optimized jointly, or kept at its previous value.

If the whole graph is one deleted junction there are no neighboring regions. The same external-arm accounting applies directly. Zero low arms and limiting half labels follow by the continuous formula (9). Reinserted vertices have at least two half incidences and are therefore in the closed complete support (8). The exact positive resolution supplies the corresponding hidden wires. No assertion is made that these boundary tensors have a strict geometric realization.

The result is a feasible state of the *same original complete tree*, with action no smaller than the absolute upper action of the prescribed sector. At least one reinserted junction has a pair sum equal to one. Let \(\mathcal F\) be the finite union of the corresponding closed pair-equality faces in the original compact resolved polytope. Its unique strict maximizing state is outside \(\mathcal F\); hence
\[
 \max_{\mathcal F}\mathcal A=F_0-\delta,
                         \qquad \delta>0.
 \tag{14}
\]
This separation concerns the same original coupled action, with its constants. It does not subtract a fixed budget at each turn. Compactness and continuity include every boundary degeneration.

There are only polynomially many label tuples for a fixed tree. The complete sine-factorial upper errors are uniform on closed support, and the other factors in (11) and the low-trace comparison have polynomial cost. Therefore the entire absolute sum in any sector described in Section 3 satisfies
\[
 \boxed{\quad
  \sup_{|s|\le R}|Z_{N,\mathrm{sector}}(s)|
       \le \exp\{N(F_0-\delta+o(1))\},\qquad R<1.
 \quad}
 \tag{15}
\]
The same bound holds for the sum over these finitely many band sectors. The geometric loss in (14) can be fixed before the radius \(R\); the subexponential errors and their eventual level threshold may depend on \(R\). Both parities are included. An inherited loss in a full external coefficient array subtracts that loss from the entire argument by homogeneity.

## 5. Exact remaining obstruction

This result removes the sectors with two or more high incidences at a moving whole junction, subject to the other-moving-junction hypothesis. It is valid at arbitrary fixed valence and uses the actual neighboring old pressure, not a sum of independently maximized caps.

It does not remove a one-high moving junction. Such a junction may have all its pair sums within the complete support, and its moving trace can nevertheless exceed the complete trace exponentially. The family \(N=5a+1\), \(e_{4a}e_a^8\) proves precisely this. Its absolute bound has action \(8g(1/5)\), but replacing its only high incidence by half does not supply the cardinal identity (9). A second incidence cannot be set to half freely: it is shared with a genuine adjacent branch whose original profile must be preserved.

Nor does (15) allow a one-high moving tensor inside one of the old regions without a separate estimate. All-low moving junctions are handled by the established signed whole-tensor domination before the regions are formed. No individual Fourier alias or additional high-valence coefficient is discarded on a positivity assumption.

Thus the general whole-component problem is reduced further, but not solved: the unresolved configurations contain one-high moving junctions coupled through actual old regions. The counterexample is a warning against a pointwise shortcut, not a counterexample to the original volume or meridian-profile assertions.
