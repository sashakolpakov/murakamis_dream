# An obstruction to the independent-reference left-cut comparison

Research deduction, 5 November 2026. The real row at the fixed cut
\(3/20\) can exceed its original conditional supporting plane on the
auxiliary reduced input bidisk. The reference is an original coupled
two-leg root, and both reference heights and horizontal target heights
are retained. A single outward root witness proves the strict excess.
It is not known to be the reference of an actual finite word.

This defeats the proposed uniform inequality on that independent
reference family. It does **not** disprove the corresponding inequality
on actual word references, a bound using a different contour or a
specified positive allowance, or dominance of the complete finite
source. No invariant or knot-family conclusion follows from the
example.

## 1. An exact auxiliary reference and the original allocation

Use the two reduced disks of the
[completed conditional source theorem](research_mixed_reduced_disk_conditional_packets.md):
their centers and radii are
\[
 c_3=7/20-i/100,\quad \rho_3=83/1000,\qquad
 c_4=3/10-13i/250,\quad \rho_4=3/50.
 \tag{1}
\]
Fix the following rational circle arguments and define the exact
external inputs:
\[
 \begin{split}
 \theta_3&=\frac{382614753601}{1000000000000},&
 A&=c_3+\rho_3 e^{2\pi i\theta_3},\\
 \theta_4&=\frac{121984810683}{200000000000},&
 C&=c_4+\rho_4 e^{2\pi i\theta_4}.
 \end{split}                                                    \tag{2}
\]
The ordinary block has own type four and external types three and
four. Let \((s,t)\) be its original zero-lift solution of
\[
 \begin{split}
 0&=g'(s+t)+g'(s+A)-3g'(s)+2\pi iA,\\
 0&=g'(s+t)+g'(t+C)-3g'(t)+2\pi iC.
 \end{split}                                                    \tag{3}
\]
Here \(g\), \(g'\), their additive constants, and their logarithmic
lifts are the original ones in the cited source theorem. The saved
point witness verifies (3) directly, rather than only its exponentiated
polynomial. The old ordinary-block uniqueness identifies the witness
with the original branch on this reduced input product.

In the first conditional orientation set
\[
 a=A,\qquad b=t,\qquad
 F(s;a,b)=g(s+a)+g(s+b)-3g(s)-g(a)-\frac32g(b)+2\pi ias.
 \tag{4}
\]
Thus the first type is three and the own/second type is four.
Equation (4) includes the original asymmetric chirp and one half of
the second factorial Fourier weight. Define its original reference
value and real marginals by
\[
 \begin{split}
 M&=\Re F(s;a,b),\\
 p_a&=\Re\{g'(s+a)-g'(a)+2\pi is\},\\
 p_b&=\Re\{g'(s+b)-\tfrac32g'(b)\}.
 \end{split}                                                    \tag{5}
\]
No marginal is evaluated at the cut or at a moved critical point.

## 2. A fixed real-cut row above that plane

Take the rational horizontal targets
\[
 x=\frac{11}{50},\qquad
 y=\frac{22252624287}{50000000000},\qquad
 \widehat a=x+i\Im a,\quad \widehat b=y+i\Im b,\quad
 \ell=\frac3{20}.
 \tag{6}
\]
Both targets belong to the original real plateau
\([11/50,9/20]\). The heights are exactly the reference heights.
All real parts of the individual and shifted arguments at this cut
lie strictly between zero and one. Consequently the full allocated
absolute-row rate at \(\ell\) is exactly
\(\Re F(\ell;\widehat a,\widehat b)\), with no reflected-row
correction or branch change. The second height is negative, so the
displayed factorial halfweight is the actual unselected branch.

**Proposition 1.** The exact data (1)--(6) satisfy
\[
 \boxed{\quad
 \Re F(\ell;\widehat a,\widehat b)
      -M-p_a(x-\Re a)-p_b(y-\Re b)>\frac1{1000}.
 \quad}                                                        \tag{7}
\]
In particular the row also exceeds the smaller plane containing the
quadratic subtraction
\(\{(x-\Re a)^2+(y-\Re b)^2\}/2500000\).

The containing rational rectangles verified by the checker are
\[
 \begin{array}{c|cc}
 &\Re&\Im\\ \hline
 A&(.288,.289)&(.045,.046)\\
 C&(.253,.254)&(-.091,-.090)\\
 s&(.267,.268)&(-.088,-.087)\\
 t&(.332,.333)&(-.058,-.057).
 \end{array}                                                   \tag{8}
\]
Thus every displayed height is already smaller than \(27/250\)
in absolute value. Restricting the auxiliary inputs only by that
height bound does not remove this example.

## 3. The single-point certificate and its scope

The original accepted reduced-disk cover is unchanged. An authorized
diagnostic first selected a weak saved midpoint in the single family
\((4;3,4)\), optimized the two horizontal targets using their proved
strict concavity, and then varied only the two external circle
arguments locally. That search is not an acceptance condition.
Its preserved files are in
[the diagnostic archive](../repro/diagnostics/2026-11-05-left-cut-weak-reference/).

The focused checker instead takes just the exact data (2), (6) and
the saved rational root witness. It reuses the original interval
self-map and original-log lift test from the reduced-disk certifier.
At this degenerate parameter rectangle there is no parameter
subdivision. Its tiny original-log root enclosure is then substituted
directly into (4)--(7), with the same interval reference used in the
value, marginal slopes, and target heights. The checker requires the
strict lower bound in (7); the floating maximizer and floating deficit
play no role in acceptance.

The saved replay reads the same point witness and performs no root
proposal or optimization. The whole previous parameter family is not
recomputed. Proof, checker, original input records and all imported
source dependencies are bound by their current hashes.

Because (7) is a strict point inequality, it establishes an actual
failure of the **independent-reference fixed-cut comparison**. The
external pair in (2) has not been realized by the coupled equations
of a whole open word. Further neighboring constraints can therefore
still exclude it. Moreover a positive absolute-row rate relative to
this plane is not a lower bound for the complete conditional kernel:
coherent cancellation and alternative contour choices remain possible.
The matched-reference source packet is not contradicted.

Reproduction:

    python3 experiments/check_mixed_left_cut_independent_reference_obstruction.py --precision 256

Saved replay:

    python3 experiments/check_mixed_left_cut_independent_reference_obstruction.py --precision 320 --input repro/results/research-mixed-left-cut-independent-reference-obstruction.json --output repro/results/research-mixed-left-cut-independent-reference-obstruction-replay.json
