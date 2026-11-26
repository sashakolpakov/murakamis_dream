# Bounds for the geometric supporting slopes

Research proof, 4 November 2026. Frozen manuscripts are unchanged.
The bounds below concern the geometric supporting slopes; they do not
establish the source comparison in which those slopes occur.

## 1. Three neighboring blocks

Let \((e_0,e_1,e_2)\in\{0,1\}^3\) specify three consecutive blocks,
where \(0\) denotes crossing power three and \(1\) denotes power four.
The two external parameters range independently over
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].
 \tag{1}
\]
The [open-window holomorphy lemma](research_mixed_cyclic_critical_height_bounds.md#2-arbitrary-finite-open-windows-have-global-root-branches)
(Lemma 2 of the height-window proof) supplies the selected holomorphic six-variable solution
\((s_0,t_0,s_1,t_1,s_2,t_2)\) on the larger product of typed disks.
The closed rectangles (1) lie strictly inside those disks.
For every internal variable \(z_j\), the equations are
\[
 g'(z_j+z_{\mathrm{partner}})
 +g'(z_j+z_{\mathrm{external}})
 -(2+e_{\lfloor j/2\rfloor})g'(z_j)
 +2\pi i z_{\mathrm{external}}=0.
 \tag{2}
\]
Here the external leg in (2) means the adjacent leg in the chain,
or one of the two prescribed endpoints; the partner is the other
leg in the same block. The branches are the original zero-lift branches.

For the middle conditional sum put \(a=t_0,\ s=s_1,\ b=t_1\).
With \(g(z)=(\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6)/(2\pi i)\),
its half-weight phase is
\[
 F(s,a,b)=g(s+a)+g(s+b)-(2+e_1)g(s)+2\pi ias
               -(1+e_0/2)g(a)-(1+e_1/2)g(b).
 \tag{3}
\]
Since \(F_s=0\), the derivatives of its conditional critical value are
\[
 p_a=g'(s+a)+2\pi is-(1+e_0/2)g'(a),\qquad
 p_b=g'(s+b)-(1+e_1/2)g'(b).
 \tag{4}
\]
Both are holomorphic functions of the two external parameters.
These are the derivatives used in the actual geometric supporting
plane, with all half-weights retained.

## 2. Uniform bounds

**Theorem 1.** On each full reference product, the slopes in (4) satisfy
\[
                    -1/5<\Re p_a,\Re p_b<1/4.                 \tag{5}
\]
There are eight internal words, four choices of external types, and
sixteen products of rectangle edges: 512 two-real-parameter products.
On each product the certificate reuses the original six-variable
affine Newton enclosure, with its residual and Jacobian estimates.
The approximate solution and inverse are proposals only. Every
accepted enclosure verifies nonsingularity, the self-map inequalities,
and containment in the old chamber before (4) is evaluated outward.

The binary parameter cells must form a prefix-free exact cover with
Kraft mass one for every edge product. The checker verifies both
strict inequalities in (5) on every accepted cell. Since the branch
was holomorphic before the boundary calculation, successive harmonic
maximum principles then extend (5) to the entire rectangle products.
No claim about a root is inferred from a boundary sampling.

The author cover has 4820 cells on the 512 edge products. A separate
replay uses the original sine logarithms, cotangent differences and
sine-based Taylor remainder to reconstruct each enclosure. It also
evaluates (4) with
\(g'(z)=\log(2\sin\pi z)+\pi i(1/2-z)\), keeping its original lift.
The replay accepts the same cells without further subdivision and
checks the complete list of products and every exact cover.

At an actual cyclic critical point, unroll any three consecutive
blocks and use their neighboring critical legs as the two external
parameters. The old type-three bound and the
[refined type-four bound](research_mixed_type_four_height_refinement.md)
put those external legs in (1). Uniqueness of the open-window solution
identifies (4) with the actual supporting derivatives. This argument
also allows repeated incidences for cyclic lengths one and two.

## 3. Scope and reproduction

The bounds (5) constrain the slopes
in a separate scalar support problem. They do not bound a finite kernel,
its exterior integral, or a knot invariant.

    python3 experiments/certify_mixed_geometric_support_slopes.py --precision 192
    python3 experiments/replay_mixed_geometric_support_slopes.py --precision 256

A record produced with the optional case selector is a partial check.
Only a record with all 512 edge products and the full-family flag
can support the extension in Section 2.
