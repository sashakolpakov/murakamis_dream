# Source eligibility of the canonical ordinary-plus-terminal family

Research deduction, 6 November 2026. The canonical suffix over either
reduced typed input domain satisfies the oriented and inverse-leg
conditions of the completed type-four terminal source certificate.
This follows from the original ordinary equations and their full-map
image bounds, without evaluating a reference or asserting finite-word
realization. It does not extend the source certificate to every point
of the larger auxiliary input disks or of a rectangular image enclosure.

## 1. Domains and the canonical suffix

Keep the original disks and their reduced versions:
\[
\begin{split}
 D_3&=\{|b-(7/20-i/100)|\le9/100\},&
 P_3&=\{|b-(7/20-i/100)|\le83/1000\},\\
 D_4&=\{|b-(3/10-13i/250)|\le8/125\},&
 P_4&=\{|b-(3/10-13i/250)|\le3/50\}.
\end{split}
\tag{1}
\]
The [actual typed envelopes](research_mixed_typed_last_row_envelopes.md)
are
\[
\begin{split}
 K_3&=P_3\cap\{-9/125\le\Im b\le17/250,
                         \ \Re b-3\Im b\le76/125\},\\
 K_4&=P_4\cap\{-27/250\le\Im b\le-1/1000\},\\
 K_4^{\rm adj}&=K_4\cap\{\Re b\ge259/1000\}.
\end{split}
\tag{2}
\]
Their proof includes ordinary and attached nonprivate legs. Private
endpoint legs are not asserted to lie in these domains.

Fix the external type flag \(\beta\in\{0,1\}\). Throughout,
the parameter belongs to its original disk \(b\in D_{3+\beta}\).
The preceding ordinary vertex has own flag one and the terminal
vertex has own flag one. Write the canonical suffix as
\[
 q_*(b)=(e(b),\xi(b),t(b),a(b),s(b)).
\tag{3}
\]
Here \(t\) is the terminal attached leg, \(a\) is the ordinary
leg adjacent to it, and \(s\) is the ordinary leg adjacent to \(b\).
Thus \((s,a)=B_1(b,t)\), and the terminal attached-coordinate
map satisfies \(t=E_4(a)\).

The original five zero-lift equations, prior existence and uniqueness
on the common convex chamber are given in
[the canonical suffix construction, Section 1](research_mixed_terminal_horizontal_envelope_diagnostic.md).
The [complete-disk affine theorem](research_mixed_terminal_all_input_affine_enclosures.md)
and its posterior refinements enclose this same family; their
independent coordinate rectangles are not the reason for the source
eligibility proved below.

## 2. The exact inverse-leg conditions

For an endpoint input \(a\), put
\[
 A=e^{-2\pi ia},\qquad T=e^{-2\pi iE_4(a)},\qquad
 \mathscr S(a)=\frac{1-T(1-A)^3/(1-AT)}{A},\qquad
 \mathscr W(a)=\mathscr S(a)+
       \frac{(1-\mathscr S(a))^3}{1-A\mathscr S(a)}.
\tag{4}
\]
The exponent three is the own-four ordinary exponent. The
[original inverse-leg lemma](research_mixed_endpoint_inverse_filter.md),
Section 1, proves regularity of these denominators on the admitted
endpoint disk. In particular
\(1-A\mathscr S=T(1-A)^3/(1-AT)\ne0\).
Off the actual branch the two numerator functions may vanish; no
logarithm is taken there without the stated half-plane conditions.

Define \(\mathfrak A_4\) to be the endpoint inputs \(a\in K_4^{\rm adj}\)
for which
\[
\begin{gathered}
 \Im\mathscr S(a)<0,\qquad \Im\mathscr W(a)>0,\\
 -\frac{\operatorname{Log}\mathscr S(a)}{2\pi i}\in P_4,
 \qquad
 \frac{\operatorname{Log}\mathscr W(a)}{2\pi i}\in P_3\cup P_4.
\end{gathered}
\tag{5}
\]
Both logarithms in (5) are principal. These half-planes specify the
unique lifts with real part between zero and one half. The conditions
are sufficient for avoiding every length-at-least-three inverse
exclusion in the [coupled source continuation](research_mixed_terminal_four_coupled_source_continuation.md),
not sufficient for realization by a finite word.

**Proposition 1.** For the canonical family (3),
\[
 b\in D_{3+\beta}\cap(P_3\cup P_4)
       \quad\Longrightarrow\quad a(b)\in\mathfrak A_4.
\tag{6}
\]
In particular (6) holds for every \(b\in K_{3+\beta}\).
Membership in the union of reduced disks does not change the original
type \(\beta\): the canonical family is always the one defined on
its fixed disk \(D_{3+\beta}\).

*Proof.* The original endpoint map has \(t(b)\in D_4\).
The [full-bidisk ordinary image theorem](research_mixed_cyclic_critical_height_bounds.md),
Proposition 1 and its proof before the cyclic specialization, gives
\[
 a(b),s(b)\in\operatorname{int}P_4,
 \qquad -51/500<\Im a(b),\Im s(b)<-1/1000.
\tag{7}
\]
This applies to \(B_1(b,t(b))\) even though its two inputs are
correlated: its estimates hold on the entire typed product.
The [oriented full-map bound](research_mixed_first_cap_oriented_plateau_certificate.md),
Section 1, gives \(\Re a>259/1000\) when \(\beta=0\),
and \(\Re a>263/1000\) when \(\beta=1\). It is the output
adjacent to the type-four input \(t\), not an arbitrary ordinary
leg, that has this bound. Hence \(a(b)\in K_4^{\rm adj}\).

Set \(S=e^{-2\pi is(b)}\) and \(B=e^{-2\pi ib}\). The original
shared-leg and ordinary-index equations are
\[
\begin{split}
 g'(s+a)+g'(t+a)-3g'(a)+2\pi it&=0,\\
 g'(a+s)+g'(s+b)-3g'(s)+2\pi ib&=0.
\end{split}
\tag{8}
\]
Exponentiating these already established zero-lift equations gives
\((1-AS)(1-AT)=T(1-A)^3\) and
\((1-AS)(1-SB)=B(1-S)^3\). Solving exactly yields
\(\mathscr S(a(b))=S\) and \(\mathscr W(a(b))=B^{-1}\).
By (7), \(s\in P_4\); by the hypothesis in (6),
\(b\in P_3\cup P_4\). Every point in these disks has real part
strictly between zero and one half. The required half-plane signs
and the principal lifts in (5) are therefore respectively \(s\)
and \(b\). This proves (6), without recovering original lifts
from exponentiation at any unrelated auxiliary point. \(\square\)

## 3. What the completed source certificate supplies

The [completed source author and replay](research_mixed_terminal_four_alias_reserve.md)
cover all 40,131 original jobs. A new filter leaf removes a box only
when both the length-two and length-at-least-three tests exclude it.
No point of \(\mathfrak A_4\) can be removed by the latter test,
regardless of its length-two test. Nor can a point of (5) be removed
by the disk, height or oriented-real exclusions. All surviving source
leaves retain their original inequalities. Thus the completed
twenty-one comparisons apply pointwise on \(\mathfrak A_4\), not
only to a discrete set of known word references.

Equations (7) also give the independent conditions used by the coherent
physical-tail estimates: \(.24<\Re a<.36<.433\) and
\(-.102<\Im a<-.001\). The real bounds follow from the reduced
disk \(P_4\), with strictness supplied by (7). The original endpoint
rectangles and endpoint branch at \(a\) are unchanged. Therefore the
same source hypotheses used in the complete terminal envelope and
selected-height transport hold along the canonical image of either
\(K_{3+\beta}\). This is a domain deduction, not a new comparison
of its 27 profiles with an adjacent ordinary factor.

Boundary contact with a reduced disk is retained by the original strict
distance exclusions. For any fixed eligible input, the finite collection
of closed excluded boxes misses it; hence some neighborhood also misses
them. The local ordinary-color germs and original finite-current
estimates are not lost at these retained boundaries. Uniform constants
on a compact eligible family follow by the same finite-cover argument,
with their original positive tolerance and source hypotheses.

Finally take an actual open word of length \(m\ge3\) whose penultimate
vertex is four and whose terminal vertex is four. Its outside coordinate
\(b=t_{m-2}\) is ordinary when \(m>3\), and the first endpoint's
attached leg when \(m=3\). The [actual local-factor theorem](research_mixed_open_local_factor_coverage.md)
and the typed envelopes give \(b\in K_{3+\beta}\). The last five
coordinates solve exactly (3)'s original system with that fixed \(b\).
Uniqueness identifies them with \(q_*(b)\), so Proposition 1 covers
every such suffix. This argument does not apply the ordinary equations
to a length-two word; its penultimate vertex is an endpoint.

An arbitrary independent point of a rectangular enclosure of \(a(b)\)
need not have the inverse legs in (5). A null source-extraction job
therefore remains unresolved unless its exclusion is justified for the
correlated family, rather than for the rectangle alone. No assertion
on all of \(D_{3+\beta}\), no realization of arbitrary canonical
inputs by words, and no whole-source or knot-volume theorem follows.
