# Unselected right clamping on independent neighbor domains

Research proof, 5 November 2026. The full 256-bit outward cover has
passed. The saved replay records provide the independent verification
status. No completed source artifact is changed, and no whole-period
conclusion is asserted here.

Put
\[
\begin{split}
\Omega_3&=\operatorname{conv}\{.1,.22-.03i,.45-.03i,.5,
                                  .45+.02i,.22+.02i\},\\
\Omega_4&=\operatorname{conv}\{.1,.22-.057i,.45-.057i,.5,
                                  .45+.014i,.12+.014i\},\\
K_3&=[-.03,.02],\qquad K_4=[-.057,0],\qquad
R(t)=400(.5-t)^2.
\end{split}                                                    \tag{1}
\]
The polygons in (1) are independent: no conditioned critical-coordinate
box, neighboring minimum, or selected-state restriction is imposed on
their arguments.

## 1. Original phase and holomorphy

Use the original marked primitive
\(g(z)=(\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6)/(2\pi i)\).
For type indicators \(\eta,\epsilon\in\{0,1\}\), let
\(s_\epsilon(a,b)\) be the original zero-lift conditional root and put
\[
\begin{split}
\phi_{\eta,\epsilon}(a,b)
={}&g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias\\
 &-(1+\eta/2)g(a)-(1+\epsilon/2)g(b),\qquad
s=s_\epsilon(a,b).
\end{split}                                                    \tag{2}
\]
Every polygon is the union of its earlier left cap, central rectangle,
and right triangle. These sets lie in the closed cotangent domain
\(\Re\cot\pi z\ge0\), \(|\Im\cot\pi z|<1/2\), including the
vertex \(.5\). The
[closed-cotangent theorem](research_mixed_closed_cotangent_roots.md)
therefore gives the unique simple zero-lift root before any maximum
principle is applied. Its inner argument and both shifted arguments
stay in their original regular strips. Thus (2) is holomorphic on a
neighborhood of each complete compact parameter product.

For three types define
\[
 F(a,b,c)=\phi_{\eta,\beta}(a,b)+\phi_{\beta,\gamma}(b,c),
 \qquad F_b=\partial_b F.                                    \tag{3}
\]
The full canonical conditional packets used in (2) are already proved:
the [interface source](research_mixed_left_right_interface_source.md)
handles a left cap against a right triangle, the
[right-guard source](research_mixed_right_guard_conditional_packets.md)
handles the central rectangle, and the
[right-square source](research_mixed_unselected_right_taper_products.md)
handles two right triangles. These are the same original finite sums
on overlaps, with the same logarithmic root and symbol. Root uniqueness
alone is not being substituted for a finite-source theorem.

## 2. Derivative and clamping statement

**Theorem 1.** For all eight ordered
type triples, independently
\(a\in\Omega_{3+\eta}\), \(c\in\Omega_{3+\gamma}\),
\(t\in[.45,.5]\), and \(k\in K_{3+\beta}\), one has
\[
 D(a,c,t,k):=
 \Re\left[(1+ikR'(t))F_b(a,t+ikR(t),c)\right]<-\frac1{10}.
                                                               \tag{4}
\]
Consequently, with the same fixed \(a,c,k\),
\[
 \Re F(a,t+ikR(t),c)
 \le \Re F(a,.45+ik,c)-\frac{t-.45}{10}.                     \tag{5}
\]

For fixed real \(t,k\), the expression inside the real part in (4)
is holomorphic separately in \(a,c\). Two harmonic maximum principles
therefore reduce (4) to the two polygon boundaries. There are exactly
\(8\cdot6\cdot6=288\) boundary products. The remaining two real
parameters \(t,k\) are covered in full; no harmonic reduction in
these parameters is asserted.

On a boundary product, use edge parameters \(u,v\in[0,1]\),
\(t=.45+.05w\), and \(k=k_-+(k_+-k_-)z\). Write
\(q=1+ikR'(t)\). The complete differential needed by the checker is
\[
\begin{split}
 dD&=\Re\{q\,dF_b+(dq)F_b\},\\
 dF_b&=(\phi_{\eta,\beta})_{ba}\,da
  +\bigl((\phi_{\eta,\beta})_{bb}
         +(\phi_{\beta,\gamma})_{aa}\bigr)\,db
  +(\phi_{\beta,\gamma})_{ab}\,dc,\\
 db&=q\,dt+iR(t)\,dk,\qquad
 dq=i\{R'(t)\,dk+800k\,dt\}.
\end{split}                                                    \tag{6}
\]
In particular, neither the derivative of the direction \(q\) nor the
implicit conditional-root derivatives are omitted. The condensed
Hessians in (6) are the exact complex Schur complements of the original
conditional phases.

The checker uses original-logarithm affine Newton self-maps for both
conditional roots, and separately encloses the roots at every rational
cell midpoint. It bounds (4) by the midpoint value plus the full
gradient radius, optionally intersecting this upper bound with direct
interval evaluation. A monotonic reduction is accepted only when a
whole-cell derivative has strict sign; it retains the maximizing face.
Otherwise exact rational bisection covers both children. Every saved
tree is exhausted, and every root witness and signed reduction is
rechecked in replay mode. The complete 256-bit cover passed all 288
products, with 253,378 leaves, 510,537 visited nodes and 4,069 monotonic
reductions. The bounded floating diagnostic is not an acceptance input.

After that finite cover, the maximum principles prove (4). Integrating
the exact derivative along the fixed-
\(k\) quadratic path proves (5), including both endpoints.

## 3. Consequence on the original hybrid graph

In the [split-cutoff hybrid](research_mixed_split_cutoff_hybrid_contour.md),
move one unselected coordinate \(x_j=t\in[.45,.5]\) down to \(.45\).
Every slow or fast left cutoff is one throughout this interval.
Consequently every neighboring row height is unchanged. The moving
row has constant \(k=c_j s\), where \(s\in[0,1]\) is its fixed
neighbor minimum; this belongs to the corresponding interval in (1).
If both neighboring arguments belong to the polygons in (1), (5)
therefore gives the exact two-incident allocated-phase comparison.
Any selected-neighbor Fourier corrections are fixed and cancel from
this comparison. Coincident neighbors in a two-cycle simply specialize
the independent arguments \(a,c\); the two incidences are retained.

For a one-cycle use its actual diagonal phase
\(G_\beta(b)=\phi_{\beta,\beta}(b,b)\). The chain rule gives
\[
 G_\beta'(b)=(\phi_{\beta,\beta})_a(b,b)
                 +(\phi_{\beta,\beta})_b(b,b)
             =F_b(b,b,b).                                    \tag{7}
\]
The moving point \(b=t+ikR(t)\) belongs to its corresponding polygon
throughout the path. Hence the pointwise inequality (4), with
\(a=c=b\), applies directly to the derivative of this diagonal phase.
Its integral gives the same loss \((t-.45)/10\). There is no extra
factor of two, and (5) with falsely fixed diagonal neighbors is not
being used.

For the original finite source, write
\[
 B_N(a,b,c)=
 C_{\beta,N}(e^{-2\pi ia},e^{-2\pi ib})
 C_{\gamma,N}(e^{-2\pi ib},e^{-2\pi ic})
 d_N(e^{-2\pi ib})^\beta .                                  \tag{8}
\]
All other Fourier factors are identical before and after clamping.
At a type-four moving coordinate \(k\le0\), the complete weight
envelope has \(\nu(b)=-\Re g(b)\ge0\) for \(\Re b\le.5\).
At the baseline \(b_0=.45+ik\) its relative factorial asymptotic is
uniform, since \(\nu(b_0)>0\). The full conditional packets and the
[actual Fourier-weight bound](research_mixed_fourier_weight_continuation.md)
thus imply, for each fixed \(\delta>0\),
\[
 |B_N(a,t+ikR(t),c)|
 \le C_\delta
 e^{N\{-(t-.45)/10+\delta\}}
 |B_N(a,.45+ik,c)| .                                        \tag{9}
\]
For \(\beta=0\) the weight tolerance is unnecessary. The fixed powers
of \(N\) in the conditional packets cancel in the ratio; their original
nonzero symbols are bounded above and below on these compact products.
No termwise real-row bound, replacement interpolation, or discarded
alias is used in (9). Multiplying by unchanged neighboring factors
preserves the inequality, also when such a common factor vanishes.
For a one-cycle the same argument instead uses its actual single-factor
expression \(C_{\beta,N}(X,X)d_N(X)^\beta\) and the diagonal phase
in (7), without squaring the conditional kernel.

Neither (5) nor (9) covers a right coordinate greater than \(.5\), a
neighbor outside (1), or the change of a selected center to an
unselected baseline. They do not themselves identify two contour
integrals or establish whole-period noncancellation.

## 4. Reproduction

```sh
python3 experiments/certify_mixed_unselected_right_clamping.py --precision 256
python3 experiments/certify_mixed_unselected_right_clamping.py --precision 320 --input repro/results/research-mixed-unselected-right-clamping.json --output /tmp/research-mixed-unselected-right-clamping-review.json
```

The author record preserves the earlier proof hash and its snapshot for
the final proof-only addition of the diagonal corollary and completed
counts. The numerical acceptance code and all saved witnesses are
unchanged; saved replay checks the current proof and all source bindings.
