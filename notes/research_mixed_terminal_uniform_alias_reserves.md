# Alias reserves on the complete canonical terminal images

Research deduction and fixed saved-data protocol, 6 November 2026.

The completed alias certificates contain cell-specific bounds stronger
than their global bare reserve \(1/10\). This note restricts those
already proved bounds to the four complete canonical input images.
It retains all original cells meeting each image, all twelve source
families, all sixteen alias labels of the terminal alphabet, and the
original selected-height debit \(41/1000\). No source bound or
reference is reevaluated.

## 1. The unchanged image cover and source scope

Use the external type flag \(\beta\in\{0,1\}\), terminal flag
\(\epsilon\in\{0,1\}\), and canonical ordinary-plus-terminal family
\[
 q_*(b)=(e_*,\xi_*,t_*,a_*,s_*),\qquad b\in D_{3+\beta}.
 \tag{1}
\]
The preceding ordinary block has type four in every case. The
[whole-disk enclosure](research_mixed_terminal_all_input_affine_enclosures.md)
and its [quadratic residual refinement](research_mixed_terminal_quadratic_residual_refinement.md)
give exact rectangles \(A_{\beta,\epsilon}\) containing
\(a_*(D_{3+\beta})\).

The completed
[uniform real-face extraction](research_mixed_terminal_uniform_face_reserves.md)
already reconstructed the original closed endpoint partition and
selected every neighbor-one source cell \(C\) with
\(C\cap A_{\beta,\epsilon}\ne\varnothing\), including edge and
corner contacts. Its immutable result has SHA256
37fc3676a9919525e16b214db0fedebd3e13b980150f5f01ec0d0b28141a07d3.
There are respectively \(72,49,45,25\) selected cells in the
order \((0,0),(0,1),(1,0),(1,1)\).

The present protocol reconstructs that same partition with the
existing exact decoder, checks literal equality with all four saved
selected-cell lists, and checks their exact positive-width image
rectangles and intersection-area sums. Source indices count the
preceding neighbor-zero cells exactly as before. Thus no source-job
number, input rectangle or closed-boundary convention is changed.
No new partition or smaller image is introduced.

For terminal type three the original bare source theorem applies on
its full endpoint input disk. For terminal type four, the
[canonical source-domain lemma](research_mixed_terminal_canonical_source_domain.md)
proves the required oriented input and inverse-leg conditions for
every canonical \(b\in K_{3+\beta}\). Its exact inverse equations
recover \(s_*(b)\) and the same external \(b\); they do not assert
eligibility of independent points of \(A_{\beta,1}\).
All conclusions below are uniform on this actual reduced canonical
source domain. Every corresponding actual word suffix of length at
least three is included by the original uniqueness theorem.

## 2. Saved source families and the sixteen labels

Write \(v=u\) for the type-three Newton coordinate and \(v=e\)
for the type-four private coordinate. Let the alias signs
\(-,+\) select the original heights. They are
\[
 h_t^-=-.12,\quad h_t^+=.12,\qquad
 (h_v^-,h_v^+)=
 \begin{cases}(-.12,.12),&\epsilon=0,\\
               (-.055,.04),&\epsilon=1.
 \end{cases}
 \tag{2}
\]
Use the original penalties \(2\pi|h|\) for each aliased
coordinate, and no penalty for an unaliased actual main height.
Number the twelve source families locally by \(k=0,\ldots,11\):

| Local family \(k\) | \(t\)-height | \(v\)-height |
|---:|---|---|
| 0, 1 | \(h_t^-\) | \(0,\ h_v^*\) |
| 2, 3 | \(h_t^+\) | \(0,\ h_v^*\) |
| 4, 5 | \(0,\ h_t^*\) | \(h_v^-\) |
| 6, 7 | \(0,\ h_t^*\) | \(h_v^+\) |
| 8, 9 | \(h_t^-\) | \(h_v^-,\ h_v^+\) |
| 10, 11 | \(h_t^+\) | \(h_v^-,\ h_v^+\) |

Every real target is free over its original full interval in these
source families. The type-three replay uses family \(k\), while
the type-four replay uses family \(8+k\) of its twenty-one-family
inventory. These are exactly the families verified by the completed
[three-alias extraction](research_mixed_terminal_three_alias_reserve.md)
and [four-alias extraction](research_mixed_terminal_four_alias_reserve.md).

The sixteen labels of the
[terminal alphabet](research_mixed_terminal_concave_profile_envelope.md)
with at least one alias coordinate are covered as follows. Here
\(0\) denotes the actual main height and \(L,R\) the real cuts:
\[
 \begin{array}{c|c@{\qquad}c|c}
 (\sigma_t,\sigma_v)&k&(\sigma_t,\sigma_v)&k\\ \hline
 (-,0)&1& (+,0)&3\\
 (-,L),(-,R)&0& (+,L),(+,R)&2\\
 (0,-)&5& (0,+)&7\\
 (L,-),(R,-)&4& (L,+),(R,+)&6\\
 (-,-)&8&(-,+)&9\\
 (+,-)&10&(+,+)&11
 \end{array}
 \tag{3}
\]
For a real cut, the zero-height source family permits the cut as a
restriction of its free real interval. Thus (3) loses no label and
invents no comparison at an independently changing main height.
The residue penalties and original source branches remain literal.

## 3. Exact maxima and the selected-height transfer

For a selected source cell \(C\) and local family \(k\), decode its
saved outward Arb display \([m\mathbin{+/-}r]\) as the exact
rational upper \(u_{C,k}=m+r\). A finite decimal without an
outward radius is not accepted. Define
\[
 U_{\beta,\epsilon,k}
   =\max_{C\cap A_{\beta,\epsilon}\ne\varnothing}u_{C,k}.
 \tag{4}
\]
A null maximum means the job contains only exclusions, not a
numerical source bound. The new extraction keeps every such job and
conservatively marks (4) unresolved if any selected job is null.
The existing exclusion theorem still applies on admissible
references, but this protocol does not replace a null by a guessed
number or silently drop its cell.

When (4) is defined, the original bare source defect in that family
is at most \(U_{\beta,\epsilon,k}\), uniformly for the actual
reference domain and all independent real targets. Indeed every
canonical \(a_*\) belongs to a selected cell, whose original source
bound applies under the just-proved source-domain conditions.

Let \(a_*=A+ic\), \(a=y+iH\), \(H=1/100\), and retain the
allocated original plane
\[
 B_T(y)=\Re(P_\epsilon-g/2)(a_*)
       +\Re(P_\epsilon'-g'/2)(a_*)(y-A)
       -\kappa(y-A)^2,\qquad \kappa=1/2500000.
 \tag{5}
\]
The original selected-height transport, for
[type three, Section 4](research_mixed_terminal_three_selected_height_completion.md)
and [type four, Section 2](research_mixed_terminal_four_selected_height_completion.md),
has additional allocated cost
\[
 \gamma_c(y,t_R)=\pi(-c)[3/4-3y/2-2t_R]_+
       \le .01296\pi<41/1000.
 \tag{6}
\]
We retain this same global debit; no new height estimate is made.
Consequently every label \(\sigma\) mapped to \(k\) in (3)
satisfies
\[
 T_{\epsilon,\sigma}(a;\mathbf x)
       +\max\{-\tfrac12\Re g(a)-\pi H,0\}
 <B_T(y)+U_{\beta,\epsilon,k}+41/1000 .
 \tag{7}
\]
This keeps the complete selected halfweight and the same height for
both alternatives. Its absolute allocated reserve is therefore
\[
 \rho_{\beta,\epsilon,k}=-U_{\beta,\epsilon,k}-41/1000,\qquad
 \rho_{\beta,\epsilon}=\min_{0\le k<12}\rho_{\beta,\epsilon,k}.
 \tag{8}
\]
These are fixed extracted numbers, not a newly chosen acceptance
threshold. The global old reserve \(1/10\) already implies
\(\rho_{\beta,\epsilon,k}>59/1000\), wherever (4) is defined;
the purpose is to keep the stronger cell-specific information.

If \(E_{\beta,\epsilon,\nu}^+\) is any independently proved
ceiling for the original joined-plane defect, the exact allocation
in [the plane-transfer theorem](research_mixed_terminal_reserved_plane_transfer.md)
gives
\[
       \sup D_{\beta,\epsilon,\nu,\sigma}
       <E_{\beta,\epsilon,\nu}^+-\rho_{\beta,\epsilon,k(\sigma)}.
 \tag{9}
\]
The incoming complex marginal, incoming modulus halfweight and
complete selected Fourier alternatives are unchanged. No plane
ceiling is assumed negative. Equation (9) concerns the sixteen
penalized endpoint labels; vertical alias sides also have real-cut
endpoints and still require their corresponding nonalias comparisons.
This extraction alone does not give a whole-kernel or knot theorem.

## 4. Fixed saved-only protocol

The new
[checker](../experiments/check_mixed_terminal_uniform_alias_reserves.py)
uses only the standard library and exact rational arithmetic.
It binds this proof, the completed uniform-face cover, the source-domain
lemma, the two completed alias audits and their checkers, the immutable
source replays, and every inherited current hash.

The three-alias audit already validates all \(40,164\) jobs.
The preceding canonical-face audit validates all \(40,131\) jobs
of the four-source replay; the four-alias audit separately validates
its \(22,932\) alias jobs, including the excluded-only cases.
The new checker verifies these associations and summary inventories,
then reads only the selected summaries for (4). It never calls an
old source checker or repeats an analytic source evaluation.

The fixed inventory consists of four image rectangles, twelve source
families and sixteen mapped labels per case: 48 family maxima and
64 labeled reserves, with 2,292 selected-job reads. It saves every
selected cell, every contributing job and outward display, the exact
maximum and attaining jobs, all nulls, every allocated reserve, and
the per-case minimum in (8). Complete input hashes are checked before
and after. No subdivision, target proposal, new root, primitive,
analytic callback or automatic continuation is allowed.

The prescribed fresh output is
repro/results/research-mixed-terminal-uniform-alias-reserves.json.
The calculation has not been run when this protocol is frozen.
