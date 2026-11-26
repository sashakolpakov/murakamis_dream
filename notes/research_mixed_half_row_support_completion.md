# Completed ordinary half-row supporting-plane comparison

Research result, 5 November 2026. The complete author record and its
320-bit saved replay establish the half-row inequality below on all
twelve ordinary reference faces. This note records the result of the
unchanged [resumable certificate](research_mixed_resumable_half_row_support.md);
it does not alter its proof, code or saved trees.

## 1. The uniform inequality

Let
\[
 P_3=\{|z-(.35-.01i)|\le.083\},\qquad
 P_4=\{|z-(.30-.052i)|\le.060\},\qquad I=[.22,.45].
 \tag{1}
\]
For each own flag \(\epsilon\in\{0,1\}\), external flags
\((\alpha,\beta)\in\{(0,0),(0,1),(1,1)\}\), and
\((A,C)\in P_{3+\alpha}\times P_{3+\beta}\), take the original
zero-lift two-leg root \((s,t)\). Use either conditional orientation
\((s_*,a,b,\eta)=(s,A,t,\alpha)\) or
\((t,C,s,\beta)\), exactly as in
[the original assertion, equations (2)--(4)](research_mixed_half_row_support.md).
In particular the two-leg equations, rather than independent output
rectangles, determine the reference correlation. Write
\[
\begin{split}
 F(v;a,b)={}&g(v+a)+g(v+b)-(2+\epsilon)g(v)+2\pi iav\\
 &-(1+\eta/2)g(a)-(1+\epsilon/2)g(b),\\
 \phi(a,b)&=F(s_*;a,b),\qquad Z=(a,b)=U+iH,\\
 B_Z(X)&=\Re\phi(Z)+\Re\phi'(Z)\cdot(X-U)
                -\frac{\|X-U\|^2}{2500000}.
\end{split}
 \tag{2}
\]
The primitives, logarithmic lifts, chirp and both halfweights remain
those of the original finite source.

**Theorem.** On all six own/external reduced products, in both
conditional orientations, every independent real target \(X\in I^2\)
satisfies
\[
             \Re F(1/2;X+iH)<B_Z(X)-\frac1{2000}.
 \tag{3}
\]
The exchanged ordered mixed pair is included by the exact input/root
exchange. The reference domain is the full reduced product, not only
the product of its two boundary circles.

*Proof.* The original half-row proof reduces (3) to the ordinary
boundary, a circle times a disk in either slot, using the full
matched right-tail entropy gap and the reference horizontal Hessian.
Strict target concavity reduces the complete square \(I^2\) to each
leaf's validated target-gain or optimized-envelope calculation.
The completed records below cover all twelve resulting faces.
Every leaf passes its stored acceptance rule with upper deficit
strictly below \(-1/2000\). The saved replay validates both
orientations, including every exactly exchanged leaf, with the
original root and response equations. The ordinary-boundary argument
therefore proves (3) on the whole reference products. \(\square\)

The allocated functions in (2) are defined on the entire auxiliary
products. Their interpretation as physical unselected Fourier upper
rates still uses the actual negative type-four heights. Theorem (3)
does not extend that interpretation to positive type-four auxiliary
heights. It proves the half-row comparison, not the independent last
row, terminal endpoint graph, or full ordinary source theorem.

## 2. Completed records

The [256-bit complete author record](../repro/results/research-mixed-resumable-half-row-support-attempt02.json)
and [320-bit complete saved replay](../repro/results/research-mixed-resumable-half-row-support-replay.json)
both have status `passed`, all twelve faces complete, and final
bindings verified. The replay covers 453,367 leaves, counting the
exactly exchanged faces, with 37 bound dependencies. It makes zero
root or target proposals and zero refinements. The original trees,
stored axes, rational witnesses, targets and acceptance-rule labels
are preserved; higher-precision interval display bounds need not
be identical.

| Artifact | SHA256 |
|---|---|
| Complete author | `4695aeadfb8d160d7884c1595198cb4de807d8376625fe32933f7efd33e75613` |
| Complete saved replay | `254d6a715a47338117ae9aa228f05aafbcc08a6f836ddaf4fed1874e9bdab8cd` |
| Pinned resumable proof | `86cbdc690df7d71822922847e4bd2dd45364668566d4ac0d2c718a4c09e4ad69` |
| Pinned certifier | `3f2a161b0cf22521462036afd1e768d30302aee472a0385301050f8841973370` |

The replay input hash is the complete author hash in this table.
The two original acceptance rules, immutable seeds and exact swap
construction are documented in the pinned proof. No new numerical
calculation is needed for this completion deduction.

Together with the completed
[typed last-row comparison](research_mixed_typed_last_row_support_completion.md),
this supplies the remaining row inputs to the
[three-row source assembly](research_mixed_three_row_source_assembly.md).
Arbitrary short fillings and branching do not follow from (3).
