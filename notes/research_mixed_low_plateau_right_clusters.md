# Combining low, plateau and right coordinates on the original coupled contour

Research proof, 4 November 2026. This extends the completed plateau/right
allocation to arbitrary mixtures of the closed sets
\[
 L=[0,1/10],\qquad P=[11/50,9/20],\qquad R=[1/2,1].                 \tag{1}
\]
The extension uses the unchanged certified right-run support values.
No new reference cover, source saddle, or continuation at zero is assumed.
The two open transition intervals remain outside the result.

## 1. The same raw support includes every low neighbor

Use the original primitive
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \quad J(x)=\Re g(x),\quad
 \ell(x)=J'(x)=\log(2\sin\pi x)\quad(0<x<1).
                                                                    \tag{2}
\]
For \(e,\alpha\in\{0,1\}\), \(-1/5\le k\le1/4\), put
\[
 F(u,p)=J(u+1/2)+J(u+p)-(2+e)J(u)
                    -(1+\alpha/2)J(p)-kp.                         \tag{3}
\]
The [complete-row reduction](research_mixed_right_pair_raw_reduction.md),
Proposition 1, identifies the original right/other raw support with
the maximum of (3) over \(0\le u\le1/2\). Its triangle decomposition
also proves strict joint concavity on the open half-square, with
continuous extension to its boundary.

**Lemma 1.** For every indicated type and slope,
\[
 \max_{\substack{0\le u\le1/2\\0\le p\le9/20}}F(u,p)
 =\max_{\substack{0\le u\le1/2\\11/50\le p\le9/20}}F(u,p)
 =S_{e\alpha,P}(k).                                                \tag{4}
\]
In particular all frozen support values and their convex slope chords
remain valid on \(L\cup P\), without recomputation or extrapolation
of the slope interval.

To prove this, fix \(p_0=11/50\). The strictly concave function
\(u\mapsto F(u,p_0)\) has a unique maximizer \(u_e\) in the open
interval: its derivative tends to \(+\infty\) at zero and to
\(-\infty\) at \(1/2\). The following outward comparisons place it
strictly between \(1/5\) and \(3/10\):
\[
 \begin{split}
 \ell(7/10)+\ell(21/50)-3\ell(1/5)&>13/20,\\
 \ell(4/5)+\ell(13/25)-2\ell(3/10)&<-1/10.
 \end{split}                                                       \tag{5}
\]
Here \(\ell(1/5),\ell(3/10)>0\), so the first is the worst lower
derivative over both \(e\), and the second the worst upper derivative.
The inner derivative is independent of \(\alpha,k\). Moreover,
\(u_e+p_0\in(21/50,13/25)\), and the minimum of \(\ell\) on that
interval is \(\ell(21/50)\). Since \(\ell(p_0)>0\),
\[
 F_p(u_e,p_0)
 \ge\ell(21/50)-\tfrac32\ell(11/50)-\tfrac14
 >\frac1{25}.                                                       \tag{6}
\]
The actual last margin is greater than \(.04698\).
The global concave tangent at \((u_e,p_0)\), where \(F_u=0\), gives
\[
 F(u,p)\le F(u_e,p_0)+F_p(u_e,p_0)(p-p_0)<F(u_e,p_0)
                         \quad(0\le p<p_0).                         \tag{7}
\]
Continuity includes \(u=0,1/2\) and \(p=0\). This proves (4).
No claim is made that the same maximum holds after enlarging the
upper endpoint \(9/20\) to \(1/2\).

The upper-row reduction is also valid at \(p=0\): all its functions
are continuous there, so its already proved inequality for
\(0<p<1/2\) passes to that endpoint. Thus (4) still bounds every
original finite row, including the revived or vanishing endpoint rows.

## 2. Absolute Fourier bounds at zero, with the forcing retained

The use of (4) near zero requires an absolute bound for the literal
Fourier polynomial, not a relative inverse-factorial approximation.
For every \(\delta>0\),
\[
 |d_N(e^{-2\pi ip})|
       \le C_\delta N^A e^{N[-J(p)+\delta]},
                          \qquad 0\le p\le9/20.                    \tag{8}
\]
Indeed the [boundary-strip theorem](research_mixed_boundary_strip_bounds.md),
equation (8), proves a uniform rate \(\omega(\varepsilon)\to0\)
on a neighborhood of the seam, using the downward forced recurrence
and retaining both its forcing and initial value. Choose a fixed
\(\varepsilon>0\) so this rate is less than \(\delta\).
On \([0,\varepsilon]\), \(-J(p)\ge0\), so this proves (8).
On the remaining compact interval, the
[absolute Fourier comparison](research_mixed_fourier_weight_continuation.md),
Section 5, has rate \(\max\{-J(p),0\}+\delta=-J(p)+\delta\).
Combining the two fixed bounds proves (8), uniformly in \(N\) and
the distance to zero. The same argument and periodicity give rate
\(\delta\) on the closed right semicircle, including its seam at one.

The uniform row-product estimates already include every product zero
and both parity endpoint rows. Combining them with (8) proves the
original allocated raw-source bound with rate (4) plus an arbitrarily
small fixed tolerance. All selected monomials have modulus one here.
There is no cancellation-only seam bound, discarded row, or
level-dependent cutoff.

Consequently every isolated-right or longer-right-run source piece
in the [plateau/right assembly](research_mixed_full_plateau_right_clusters.md)
continues to hold when its non-right boundary coordinates belong to
\(L\cup P\). Its actual correlated reference, slope interval, complex
tangent cancellation, oriented debits and type-three allowances are
unchanged. Spend less than \(1/10000\) in total on the Fourier
tolerances of each two- or three-edge piece. Its existing phase
reserve \(1/5000\) then leaves the same finite-source loss
\(1/10000\). In particular the new low endpoints consume no
additional unbudgeted tolerance.

## 3. Disjoint source pieces on the coupled graph

Fix an original cyclic three/four word of length \(m\ge1\), its
actual critical coordinates \(z_j^*\), and the real critical action
\(M\). For each original selected subset use the exact coupled
contour of [the all-selection low/plateau theorem](research_mixed_selected_low_plateau_clusters.md),
with cutoff zero on \(L\cup R\) and one on \(P\).
On \((L\cup P\cup R)^m\), the product and minimum-neighbor
formulas agree: every low or right coordinate and each adjacent
plateau coordinate has height zero. Untouched plateau coordinates
retain their reference height or their selected height \(.014\).
The graph Jacobian is one almost everywhere on these boxes.

First partition all right-incident edges by maximal cyclic right
runs, exactly as in the proved plateau/right assembly: a run of
length one uses its two-edge pair; a run of length two uses its
three-edge piece; a longer run uses its two endpoint pairs and the
remaining individual right/right edges. The new Lemma 1 permits
either a low or plateau boundary at each end. These original edge
sets are disjoint even when two runs share a non-right vertex.
The all-right case uses the original right/right single-block bound.

Every remaining edge is \(LL,LP,PL\), or \(PP\). The closed
whole-source bounds give loss \(1/100\) on each \(LL\) edge and
\(1/20\) on each \(LP\) or \(PL\) edge. These targets have both
heights zero, so all selections have modulus one. No \(LR\) or
\(RL\) edge is charged again: it has already been consumed by a
right-run piece.

Each right-run boundary reserves its existing charges
\[
 L(a)=\tfrac{151}{20}(\Im a)^2,\qquad
 R(c)=\tfrac{11}{2}(\Im c)^2,                                      \tag{9}
\]
and its type-three allowances \(f_L=.01683\), \(f_R=.01202\).
If that boundary target is low, these charges may remain unused.
If it is plateau, its charge can be spent only on the immediately
adjacent \(PP\) block.

## 4. Mixed low/right reset costs

Consider an ordered \(PP\) edge \((p,q)\) without an active
selected endpoint. Its first height resets precisely when the
preceding coordinate is \(L\) or \(R\), and its second height
resets precisely when the following coordinate is \(L\) or \(R\).
Each reset therefore has a unique exterior incidence at this edge.
If the cause is low, assign that incidence's \(LP\) loss to this
edge only. A low/plateau edge can be assigned at most once: its
plateau endpoint has at most one other plateau incidence.

For no reset there is no cost. A single low-caused reset costs at
most \(10(.057)^2=.03249<.04\). Two low-caused resets use the full
matrix estimate, charging each its own \(10h^2<.04\).
A single right-caused reset uses (9). Two right-caused resets use
exactly the established oriented charges, the same-sign four/four
cone, and at most one type-three allowance; no new charge is needed.

It remains to treat a \(PP\) edge with one low cause and one right
cause. Write \(h_p=\Im p^*,h_q=\Im q^*\). For two four-type
endpoints, the same-sign cone costs
\((11/2)h_p^2+(151/20)h_q^2\). After the right charge, the low
incidence therefore pays at most \(.02452995<.04\).
If at least one endpoint is type three, use the safe full-matrix
cost \(10(h_p^2+h_q^2)\). The following table gives its largest
remaining debit after the indicated right charge, using
\(|h_3|\le.03\), \(|h_4|\le.057\):
\[
\begin{array}{c|ccc}
 \text{right-caused endpoint}&(3,3)&(3,4)&(4,3)\\\hline
 p&.01305&.03654&.0236205\\
 q&.011205&.01696005&.034695
\end{array}                                                        \tag{10}
\]
Every entry is less than \(.04\). Thus every low incidence pays
less than \(.04\) of its existing \(.05\) source loss, retaining
at least \(.01\). No type-three right allowance is needed in
this mixed case. When both causes are right, the prior allowance
rule still assigns each allowance to at most one block; allowing
low boundaries only removes possible uses.

If a \(PP\) block has an active selected endpoint, the selected
plateau or selected/reset theorem instead gives a full loss
\(1/200\). Its nonnegative reset debit need not be charged.
A doubly reset block has both heights zero and no active selection.
Consequently the preceding allocation holds for every selected
subset, with both true Fourier branches retained.

This is an incidence argument, not a restriction on word length.
For \(m=2\), parallel edges retain their distinct incidences; a
plateau vertex adjacent to two non-plateau incidences has no \(PP\)
edge to charge. For \(m=3\), the two exterior reset causes of a
\(PP\) edge may be the same vertex, but the two exterior edges are
distinct. A one-cycle is wholly low, plateau, or right and uses its
single original loop bound. These cases involve no duplicated source
edge or repeated allowance.

## 5. The original restricted integral

Let \(n_R\) be the number of right coordinates, and let \(n_{LP}\)
and \(n_{LL}\) count the remaining low/plateau and low/low edges,
with their original cyclic multiplicities. The right-run allocation
leaves loss at least \(n_R/20000\), including all-right cycles.
Sections 3--4 leave loss at least \((n_{LP}+n_{LL})/100\).
Hence every literal selected density on the specified boxes obeys
\[
 |\mathcal D_{N,S}|
 \le C_mN^{A_m}
 \exp N\left[M-\frac{n_R}{20000}
                  -\frac{n_{LP}+n_{LL}}{100}\right].               \tag{11}
\]
All allocated half-moduli recombine into the original integer
Fourier factors. The sum of the full complex tangent planes is
\(M\), by the original zero-lift critical equations, including
their imaginary parts and all repeated cyclic incidences.
The original scalar, parity and level normalization are preserved.

**Theorem 1.** Summing all selections and all boxes of
\((L\cup P\cup R)^m\) except the unaliased pure plateau gives
an absolute error bounded by
\[
 C_mN^{A_m}e^{N(M-1/20000)}.                                      \tag{12}
\]
If no right coordinate occurs but a low coordinate occurs, then
\(n_{LP}+n_{LL}\ge1\). If only plateau coordinates occur, a
nonempty selection has the already proved gap \(1/200\).
The unaliased plateau contribution therefore retains its original
nonzero coefficient, Gaussian branch and level power \(N^0\) after
the entire indicated restricted region is included.

The estimate is uniform through zero angles for each fixed word.
Its constants and starting level need not be uniform in word length.
Coordinates in \((.1,.22)\) or \((.45,.5)\) remain unestimated on
these coupled contours. Thus this is not a full outer-period mixed
asymptotic, a marked boundary-filling theorem, or a knot-volume claim.

## 6. Reproduction

```sh
python3 experiments/check_mixed_low_plateau_right_clusters.py
```

The checker verifies the outward derivative margins proving the
unchanged support extension, every typed mixed-reset budget, current
source provenance, and the disjoint original-edge and charge
allocation for all three-region patterns through length ten. The
incidence proof above, rather than that finite enumeration, applies
to every fixed cyclic length.
