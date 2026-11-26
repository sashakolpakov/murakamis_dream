# A central gap at two genuine canonical prefixes

Research result, 6 November 2026. For first flag \(\alpha=1\),
second type four, external coordinate \(c_{\rm ext}=1/3\), and
either next flag \(\beta=0,1\), the original canonical prefix
has a main/main central phase gap strictly larger than \(1/64\).
The comparison is uniform in the five independent real target
coordinates at each of these two fixed references.

## 1. References, targets and retained tangents

The [canonical reference record](../repro/results/research-mixed-second-selected-canonical-reference.json)
localizes the two genuine canonical solutions
\((e_*,\xi_*,a_*,u_*,z_*,v_*,b_*)\) at fixed
\(c_{\rm ext}=1/3\). Their existence and original logarithmic lifts
come from the [canonical-reference theorem](research_mixed_second_selected_reference_curve.md)
and [residual-localization theorem](research_mixed_prefix_residual_localization.md).

Use the original phase \(F\), with \(\alpha=1\), from equations
(3)--(5) of the [central-budget proof](research_mixed_second_selected_central_budget.md).
Keep its two original complex marginals
\(p_L=F_{a,*}\), \(p_R=F_{b,*}\) and baseline
\(M_\beta=\Re F(a_*,u_*,z_*,v_*,b_*)\).
Only the selected height changes to \(H=1/100\); all other heights
stay at their canonical reference values. Set
\[
 \begin{split}
 P&=[.22,.45],\\
 K_\beta&=P\times[1/8,1/2]\times P
                  \times[\ell_\beta,1/2]\times P,
 \qquad \ell_0=3/20,\quad\ell_1=1/8,\\
 f_{\beta,\nu}(a_R,u_R,z_R,v_R,b_R)
 &=\Re\{F-p_L(a-a_*)-p_R(b-b_*)\}
                   +(1-\nu)\Re g(z)-2\nu\pi H.
 \end{split}
 \tag{1}
\]
Here \(\nu=1\) is factorial and \(\nu=0\) is forced.
In particular the boundary targets \(a_R,b_R\) still range over
all of \(P\), and both affine tangents remain subtracted.

**Theorem.** For each of the two prescribed canonical references,
\[
 \sup_{r\in K_\beta}\max_{\nu=0,1}
       \{f_{\beta,\nu}(r)-M_\beta\}<-\frac1{64}.
 \tag{2}
\]

## 2. Exact budget bounds and passage to the full target product

The [index-barrier theorem](research_mixed_second_selected_horizontal_concavity.md)
reduces both maxima to
\[
 K'_\beta=P\times[.22,.5]\times P\times[q_\beta,.5]\times P,
                 \qquad q_0=.2,\quad q_1=.22.
 \tag{3}
\]
Those barriers are pointwise in all other targets. The
[directional theorem](research_mixed_second_selected_directional_budget.md)
then bounds the factorial branch on all \(z_R\in P\), and the
forced branch on \(z_R\in[.4,.45]\), by the corresponding three-gain
budgets. Its optional [curvature refinements](research_mixed_second_selected_curvature_evaluation.md)
only replace component bounds by smaller valid upper bounds.

The [saved two-case budget record](../repro/results/research-mixed-second-selected-canonical-budgets.json)
gives the following conservative rational ceilings for these refined
upper bounds. Each displayed decimal is an exact terminating rational,
rounded upward from the stored rational upper endpoint.

| Next flag \(\beta\) | Forced, \(z_R\in[.4,.45]\) | Factorial, \(z_R\in P\) |
| --- | ---: | ---: |
| 0 | \(-.089=-89/1000\) | \(-.026=-13/500\) |
| 1 | \(-.065=-13/200\) | \(-.016=-2/125\) |

Exact fraction comparisons with the saved endpoints prove that
all four refined upper bounds are strictly smaller than their
displayed ceilings, which in turn are all strictly below \(-1/64\).
The weakest ceiling satisfies \(-2/125<-1/64\), since \(128>125\).

For \(z_R<.4\), the same directional theorem proves
\[
 f_{\beta,1}-f_{\beta,0}
       =-\Re g(z_R+iH)-2\pi H>0.
 \tag{4}
\]
Thus the factorial estimate controls both branches there. On
\([.4,.45]\), the table controls each branch separately. Combine
this dominance with (3) to obtain (2) on the original full product.
No minimum of the two Fourier alternatives is taken.

The budget record has SHA256
`e1eb9b7a9ef2ed5c07fbbb7bcf3f7044880aa4f063e4e80814552e7789831a46`;
it binds the canonical reference record
`5c9fe5c7cddc01fce993818ccde45005e10b768dae20dab8f37ce03ab3781ff8`
and all proof and evaluator inputs. This deduction uses only their
saved directed endpoints; it performs no new evaluation.

## 3. Reproduction and scope

From the repository root, use unused output paths, for example:

```sh
python3 experiments/certify_mixed_second_selected_canonical_reference.py --output /tmp/mixed-second-selected-canonical-reference-reproduction.json
python3 experiments/evaluate_mixed_second_selected_canonical_budgets.py --output /tmp/mixed-second-selected-canonical-budgets-reproduction.json
```

The first command repeats the two prescribed canonical solves and
their original-residual certification. The second reads the frozen
canonical record pinned in its driver; it does not replace that input
with the first command's output. Both scripts refuse to overwrite an
existing output. The [evaluation specification](research_mixed_second_selected_canonical_budget_evaluation.md)
fixes the two cases, precision and callback limits.

The result concerns central phase targets at two fixed genuine
canonical references. It does not prove that either reference is
realized by a finite-word suffix, bound the whole external-coordinate
domain, or control the remaining finite-current profiles. It is not
a full finite-source or global filling-volume theorem.
