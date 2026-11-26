# All selected terms on the closed low/plateau region

Research proof, 4 November 2026. This extends the separately proved
zero-uniform unaliased cluster bound to all original outer selections.
It uses a different exact coupled contour for each selected Laurent
term. No estimate on the remaining outer regions is inferred.

## 1. Exact selected contours

Fix an original cyclic three/four word of length \(m\ge1\), with
four-type positions \(V_4\), geometric coordinates \(z_j^*\), and
critical real action \(M\). Retain the intervals
\[
 L=[0,1/10],\qquad P=[11/50,9/20]
 \tag{1}
\]
and the periodic cutoff \(\rho\) of
[the uniform unaliased cluster theorem](research_mixed_uniform_low_plateau_clusters.md),
equation (2). Thus \(\rho=0\) on \(L\), \(\rho=1\) on \(P\),
and \(\rho=0\) on \([1/2,1]\), with the stated linear transitions.
For each \(S\subseteq V_4\), put
\[
 c_j^S=\begin{cases}7/500,&j\in S,\\ \Im z_j^*,&j\notin S,
              \end{cases}
 \qquad
 H_j^S(x)=c_j^S\rho(x_{j-1})\rho(x_j)\rho(x_{j+1}).
 \tag{2}
\]
Repeated cyclic incidences are retained, including lengths one and two.

The [exact torus identity](research_mixed_conditional_torus_composition.md)
expresses the original cyclic scalar as the sum of the Laurent terms
with one factor \(X_j^{-N}\) for each \(j\in S\). Let
\(\mathcal D_{N,S}\) denote that literal term with its original
scalar and level normalization. The
[coupled contour identity](research_mixed_coupled_outer_graph.md)
applies separately to every such term:
\[
 \operatorname{CT}\mathcal D_{N,S}
 =\int_{\mathbb T^m}
   \mathcal D_{N,S}\bigl(e^{-2\pi i(x+iH^S(x))}\bigr)
                \det(I+iDH^S(x))\,dx .
 \tag{3}
\]
The finite sum over \(S\) is therefore still exact. There are no
discarded connecting currents. As \(|c_j^S|\le.057\), the same
Jacobian bound \((18/5)^m\) holds. The Jacobian is one almost
everywhere on \((L\cup P)^m\).

A plateau coordinate is called reset if it has a low incidence.
Its height is zero, regardless of its selection. A selected plateau
coordinate without a low incidence is called active; its height is
exactly \(7/500\). Every block incident to a low coordinate has
both heights zero.

## 2. Complete block classification

Use the original allocated phase \(\phi_v\) and complex geometric
plane \(\Gamma_v\) of the unaliased cluster theorem. At all the
targets in (2), the original stationarity equations still give
\[
                         \Re\sum_v\Gamma_v=M.
 \tag{4}
\]
In particular no height-dependent linear term is omitted.

The following are bounds for the whole finite kernels and the true
polynomial Fourier weights, each with a uniform polynomial prefactor.

| Block | Upper rate relative to \(\Re\Gamma_v\) |
|---|---|
| \(LP\) or \(PL\) | \(-1/20\) |
| \(LL\) | \(-1/100\) |
| \(PP\) with an active selected endpoint | \(-1/200\) |
| \(PP\) without an active selected endpoint | \(10\sum_{j\in v,\,\mathrm{reset}}(\Im z_j^*)^2\) |

For the first two lines, every target is real. Hence every selected
factor \(X_j^{-N}\) has modulus one, and the zero-uniform whole-source
proof of the unaliased theorem applies unchanged. The \(LP\) estimate
uses the closed collar and the fixed compact real one-small packet;
the \(LL\) estimate uses the closed raw both-low bound.

For the third line, first suppose neither endpoint is reset.
The [selected plateau theorem](research_mixed_selected_plateau_support.md),
Theorem 1, gives gap \(1/200\), for one or two selected endpoints.
If the other endpoint is reset, the
[selected-reset theorem](research_mixed_selected_reset_plateau_support.md),
Theorem 1, gives the same gap. These are all possibilities: an active
selected endpoint cannot itself be reset. A reset four-type endpoint
may also be selected, since its selection has modulus one at height zero.
Both actual Fourier branches at the positive selected height are
already included in these finite-source estimates.

In the fourth line, every selection present in the block is at a
reset real endpoint. Such selections again have modulus one.
The full matrix reset estimate and the relative Fourier comparison
on \(P+i[-.057,0]\) give precisely the unaliased \(PP\) bound,
with no positive rate tolerance. It permits both real coordinates
to readjust. Any reset debit on a block covered by the third line
is unnecessary and is not charged.

The allocated half-moduli recombine into the literal integer powers
of the original Fourier polynomials and selected factors. This
classification concerns their product; it does not choose holomorphic
square roots of those polynomials.

## 3. Uniform incidence budget

Let \(n_{LP}\), \(n_{LL}\) have their original cyclic multiplicities,
put \(n_G=n_{LP}+n_{LL}\), and let \(n_S\) count \(PP\) blocks
with an active selected endpoint. The reset debits of the remaining
\(PP\) blocks form a subset of the unaliased debits. The same
incidence argument therefore gives
\[
 \sum_{\substack{PP\text{ blocks}\text{without an active selection}}}
       10\sum_{j\in v,\,\mathrm{reset}}(\Im z_j^*)^2
                 \le10(.057)^2 n_{LP}.
 \tag{5}
\]
Indeed a reset plateau vertex with \(k\) low incidences has
\(2-k\le k\) plateau incidences; removing selected gapped blocks
only decreases its possible debit. Both endpoints of a doubly reset
plateau block are counted. This remains valid for loops and for the
two parallel incidences of a length-two cycle.

The literal selected density thus satisfies
\[
 \begin{split}
 |\mathcal D_{N,S}|
 &\le C N^A\exp N\left[
 M-\frac{1751}{100000}n_{LP}
       -\frac1{100}n_{LL}-\frac1{200}n_S\right]\\
 &\le C N^A e^{N(M-n_G/100-n_S/200)}.
 \end{split}
 \tag{6}
\]
Constants may depend on the fixed word, but not on the target's
distance to zero. All integer-level parities are retained.

If a target has any low coordinate then \(n_G\ge1\), for every
selection. On \(P^m\), no coordinate is reset. Thus if \(S\ne\varnothing\),
at least one plateau block has an active selected endpoint and
\(n_S\ge1\). For a length-one four-type word the single block has
two selected incidences, while its block gap is used only once.

**Theorem 1.** On the exact contours (2), every selected term on
\((L\cup P)^m\) is exponentially smaller than the original critical
rate, except for the unaliased term on \(P^m\). More precisely,
\[
 \begin{split}
 &\sum_{S\subseteq V_4}
   \int_{(L\cup P)^m\setminus P^m}
       |\mathcal D_{N,S}\det(I+iDH^S)|\,dx
                         \le C N^A e^{N(M-1/100)},\\
 &\sum_{\varnothing\ne S\subseteq V_4}
   \int_{P^m}|\mathcal D_{N,S}\det(I+iDH^S)|\,dx
                         \le C N^A e^{N(M-1/200)}.
 \end{split}
 \tag{7}
\]
The selected sum is empty if the word has no four-type vertex.

Consequently the sum of the original contributions over
\((L\cup P)^m\), with each term on its specified exact contour,
has the same critical action, nonzero coefficient, Gaussian branch
and level power as the original unaliased plateau contribution.
In particular its level power remains \(N^0\), with the exact
original scalar normalization. Equations (6)--(7) apply uniformly
through every zero angle.

## 4. What is not assembled

Equation (3) concerns the entire original scalar, but (7) estimates
only the indicated restricted region. Coordinates in \((.1,.22)\)
or \((.45,1]\) still require estimates on these coupled contours.
Neighbor resets there change target heights, so the earlier independent
right-half and taper support bounds are not imported. This is not a
complete mixed-word asymptotic or a knot-volume theorem.

## 5. Reproduction

    python3 experiments/check_mixed_selected_low_plateau_clusters.py

The checker binds the completed original-source inputs, verifies the
exact loss arithmetic, and checks every low/plateau and selection
pattern through length seven. The incidence proof above applies to
every fixed cyclic length and every placement of three/four types.
