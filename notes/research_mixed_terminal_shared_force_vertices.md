# Retaining the common force parameter in the terminal scalar costs

Research deduction and fixed saved-data protocol, 6 November 2026.

The [whole-D4 integral test](research_mixed_terminal_four_input_integral_outcome.md)
leaves only its terminal-four factorial budget inconclusive. Its
three forces share the same mean cotangent components. A convexity
argument retains that dependence using sixteen scalar vertices of
the existing saved intervals, without another analytic evaluation.

## 1. A convex gain majorant for an uncertain reference center

Keep a node target interval \(I=[L,R]\subset[.18,.5]\), a containing
reference-center interval \([c_-,c_+]\subset I\), and \(K>0\).
Set
\[
 d=.5-c_+>0,\qquad U_-=c_+-L,\qquad U_+=R-c_-.
 \tag{1}
\]
For an exact real force \(q\), define \(\mathcal B(q)\) as the
maximum of zero and the following suprema:
\[
 \begin{split}
 &\sup_{0\le v\le U_-}
       \{-qv-Kdv^2/2-Kv^3/6\},\\
 &\sup_{0\le v\le\min(U_+,d)}
       \{qv-Kdv^2/2+Kv^3/6\},\\
 &\sup_{d\le v\le U_+}\{qv-Kv^3/3\}
               \quad\text{when }U_+>d.
 \end{split}
 \tag{2}
\]
The [integral-budget proof](research_mixed_terminal_four_input_integral_budget.md),
Section 4, shows that this majorizes the original node conjugate for
every center in its saved interval. In the last line, the actual
constraint \(.5-x_*\ge v\) is essential; it follows from the
target endpoint being at most \(.5\).

**Lemma 1.** \(\mathcal B\) is convex as a function of the force.

Every expression inside a supremum in (2) is affine in \(q\), and
all displacement domains are fixed independently of \(q\).
A supremum of affine functions, and a maximum with zero, is convex.
This argument concerns the underlying exact majorant, not the rounded
output of a numerical maximization routine.

The existing clipped cubic formulas evaluate (2). Replacing \(-q\)
by \(\max(0,-q)\) in the first line, or \(q\) by
\(\max(0,q)\) in the last two lines, does not change their maximum
with zero: every affected branch was nonpositive. Thus the frozen
`gain` routine, called with the exact force interval \([q,q]\),
returns a rigorous upper endpoint for \(\mathcal B(q)\).

## 2. The sixteen-vertex inequality

For the remaining terminal-four factorial case use the three fixed
majorants \(\mathcal B_s,\mathcal B_a,\mathcal B_t\), with the
reference-center intervals from the completed
[quadratic residual refinement](research_mixed_terminal_quadratic_residual_refinement.md),
the original target intervals, and
\[
                  (K_s,K_a,K_t)=(88/5,98/5,88/5).
 \tag{3}
\]
Let \(\mathcal K,\mathcal I_a,\mathcal I_s,\mathcal I_t\)
be enclosing intervals for \(\kappa=\pi\Delta\) and the three mean
imaginary cotangents. Reconstruct \(\mathcal K\) using the saved
\(\pi\) interval and the refined height interval for
\(\Delta=H-\Im a_*\). The three means remain the sums of the
sixteen original saved cotangent intervals with weight \(1/16\).
Those enclose the same whole-disk family, so remain valid after the
reference enclosures are narrowed. The original forces are exactly
\[
 \mathcal F(\kappa,I_a,I_s,I_t)
   =\bigl(\kappa(1-I_s),\
          \kappa(3I_a-I_s-I_t-1),\
          -\kappa(1+I_t)\bigr).
 \tag{4}
\]

**Proposition 2.** If \(\mathcal V\) is the set of the sixteen
endpoint vertices of
\(\mathcal K\times\mathcal I_a\times\mathcal I_s\times\mathcal I_t\),
then every actual force triple satisfies
\[
 \mathcal B_s(A_s)+\mathcal B_a(A_{a,1})+\mathcal B_t(A_t)
 \le\max_{v\in\mathcal V}
       \{\mathcal B_s(\mathcal F_s(v))+
         \mathcal B_a(\mathcal F_a(v))+
         \mathcal B_t(\mathcal F_t(v))\}.
 \tag{5}
\]
Indeed the sum of the three majorants is convex on force space.
The force map (4) is affine in each of its four arguments separately.
Fixing the other three arguments therefore gives a convex function
of the remaining argument, whose maximum is attained at an endpoint.
Applying this fact successively to the four coordinates proves (5).
Equivalently, the multiaffine image is contained in the convex hull
of its sixteen vertex images.

The parameter intervals may still contain combinations absent from
the actual reference family. This only enlarges the bound. The
improvement is that a single value of \(I_s\) must occur in both
the ordinary and selected forces at every vertex; their independent
worst values cannot be combined.

The same narrowing can be applied algebraically to the trial.
If \(\mathcal V_0\) is the unchanged saved normalized interval for
\(\int_0^1(1-\theta)(3C_a-C_s-C_t)\,d\theta\), then
\(\pi\mathcal\Delta^2\mathcal V_0\) is a valid new interval for
\(W\). Put
\[
 \widehat W^+=\min\{W^+_{\rm old},
                   \sup(\mathcal\Pi\mathcal\Delta^2\mathcal V_0)\},
 \qquad \widehat T_1^+=\widehat W^+-2\pi_{\rm lower}H.
 \tag{6}
\]
Here \(\mathcal\Pi\) is the old saved \(\pi\) interval and
\(\mathcal\Delta\) is the refined positive displacement interval.
This is a new product of already proved intervals; no height
integral is reevaluated. A sufficient whole-D4 factorial bound is
consequently
\[
 \widehat T_1^++\max_{v\in\mathcal V}
       \sum_{j=s,a,t}\mathcal B_j(\mathcal F_j(v))<0.
 \tag{7}
\]
No positivity is assumed for the individual forces, and no branch of
the complete selected weight is discarded. The three already proved
main comparisons are inherited unchanged.

## 3. Fixed saved-only evaluation protocol

Use exactly the terminal-four case of the pinned integral record
9831e8bdbc884cfc0b0c99dbc7f92245403988ae7dc4bbbba86b5606c5a1575e,
and its completed
[saved audit](../repro/results/research-mixed-terminal-four-input-integral-budget-saved-audit.json).
The audit's `normalized_Imcot_means` and `kappa` intervals have exact
`lower_rational` and `upper_rational` fields; they have no `finite`
field. Reconstruct these values from the saved cotangent intervals
and the old \(\pi\Delta\) and require exact agreement.
Then bind the
[refinement record](../repro/results/research-mixed-terminal-quadratic-residual-refinement.json),
SHA256 2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331,
its proof and checker. Use only its \((\beta,\epsilon)=(1,1)\)
entry. Verify its unchanged canonical center, response and input disk,
and that all new coordinate intervals lie inside the old ones.
Use its `coordinate_enclosures` for the three center intervals and
\(\mathcal\Delta\); compute the new \(\mathcal K\) and (6).

Enumerate the sixteen vertices once in lexicographic lower/upper
order for \((\kappa,I_a,I_s,I_t)\). Evaluate exactly three scalar
cubic gains at each vertex, using (3), these refined saved center
intervals and the original intervals \([.22,.5],P,[.22,.4]\).
The gain implementation may be reused from the frozen integral
driver because it uses only exact fractions and integer square roots;
neither that driver's `main` nor any analytic callback is invoked.
An independent rational gain checker verifies each of the 48 results.

Save every vertex, force triple, all cubic branches and clipped
optimizer enclosures, its sum, and the final maximum in (7).
An outcome of either sign is final for this protocol. There are no
new roots, reference evaluations, primitive evaluations, logarithms,
cotangents, input or height subdivisions, alternative centers, extra
vertices, or automatic retries. All old and new input hashes are
checked before and after.

The analytic implication (5) is proved here. The scalar sign in (7)
has not yet been evaluated. A positive resulting upper would remain
inconclusive, not a counterexample to the original comparison.
