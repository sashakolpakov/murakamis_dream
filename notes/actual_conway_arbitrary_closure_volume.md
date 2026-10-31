# Volume limits after reducing a Conway tangle closure

31 October 2026.

The earlier net-twist theorem starts with a cylindrical closure of a
product. Here the input may have either of the two usual closures, may
begin with a turn, and may contain twist sums that vanish exactly. Cutting
along the resulting two-punctured spheres decomposes the knot into factors.
When the remaining non-elementary factors have sufficiently large net
twists, a hyperbolic input must be isotopic to just one of them.

This gives a broader criterion for recognizing covered presentations.
Every knot it admits is explicitly isotopic to a long strict knot from
the earlier theorem. The argument does not establish a new estimate for
short twists or enlarge that previously covered set of knot types.

The proof has three distinct inputs. First, actual ordered tangle moves
give a componentwise connected-sum decomposition. Second, the established
strict-presentation theorem identifies each sufficiently long strict knot
factor as hyperbolic and proves its volume limit. Third, an elementary
group argument shows that a hyperbolic input knot cannot have two
nontrivial factors of these known types. Consequently it is isotopic to
one long strict factor. No quantum connected-sum formula is needed.

## 1. The fixed construction and the conclusion

A two-string tangle consists of two arcs with four prescribed boundary
endpoints in a ball; closed components, if a composition creates them,
must also be retained. The endpoints have the original cyclic order.
Let \(R^n\) be the integral two-braid with signed crossing number \(n\),
let \(T\) rotate the ball through a quarter-turn, and put
\(h_i(n_i)=T(R^{n_i})\). Form a finite expression \(E\) from the labelled
pieces \(h_i\), quarter-turns, and ordered vertical stacking. Each label
occurs once. Allow either cylindrical closure \(C(E)\), joining the
upper endpoints to their corresponding lower endpoints, or cap closure
\(D(E)=C(TE)\), joining each upper pair and each lower pair.

Fix the expression, with \(m\ge1\) labelled pieces, and its closing
operation before choosing the integer tuple
\(\mathbf n=(n_1,\ldots,n_m)\). For a nonempty label set \(B\), write

$$
W_B(\mathbf n)=\sum_{i\in B}n_i.
\tag{1}
$$

Apply the deterministic topological reduction described in Section 2.
It returns a tree of componentwise connected sums of:

1. strict literal cylindrical product presentations, with nonzero net
   weights attached to disjoint label blocks;
2. integral braid closures \(C(R^s)\);
3. unknots \(D(R^s)\).

Numerical-zero blocks removed during the reduction are also recorded.
Thus surviving and deleted blocks partition the original labels.
The strict factors use the finite \(L,H,A\) test of the existing theorem.
Each basic piece starts with label \(L\). The labels record intervals
of possible normalized output states in the angle calculation:
\(L=(0,1/2)\), \(H=(1/2,1)\), and \(A=(0,1)\).
They are not twist numbers. A turn \(T\) exchanges \(L,H\) and fixes \(A\);
products \(LL,LA,AA\) have type \(A\), products \(HL,HA\) have type
\(H\), and \(HH\) is forbidden. A closing product must have types
\(AA,AL,AH,LH\), in either order.

**Theorem.** There is a finite number \(B_E\), depending only on the
fixed expression and the choice \(C\) or \(D\), with the following
property. Fix any integer tuple \(\mathbf n\). Suppose:

* the literal filled input is a hyperbolic knot \(K\);
* every net weight on every surviving strict factor of the specified
  reduction satisfies \(|W_B(\mathbf n)|>B_E\).

Then the reduction has exactly one strict factor. Every other terminal
factor is an unknot, and \(K\) is ambient isotopic to that strict factor.
In particular,

$$
\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|
=\operatorname{Vol}(S^3\setminus K).
\tag{2}
$$

The invariant is the existing reduced enhanced Kashaev invariant with
unknot value one. The limit includes both parities and composite levels.
All weights, their zero relations, and the knot are fixed before \(N\)
tends to infinity. Their signs and relative sizes are unrestricted.
No lower bound is imposed on weights carried only by elementary terminal
factors. The hypothesis on the strict factors is not a claim that short
surviving strict weights can be ignored.

## 2. The actual reductions and their termination

The required topological algorithm is the optional reduction in
[the ordered net-twist theorem](actual_conway_net_twist_volume.md),
Appendices A and B. Its essential moves are recalled to make clear
which topology, rather than scalar source algebra, is used.

Write \(\tau=T^2\) for the actual planar half-turn. It reverses the
order of a stack and is retained on subexpressions. Rotation about
the stacking axis is denoted \(\rho\). The empty-collar isotopy and
the original closed pairing give

$$
R^aF\simeq \rho^a(F)R^a,\qquad
R^aR^b\simeq R^{a+b},\qquad
C((TF)G)\simeq C(F(TG)).
\tag{3}
$$

The first move rotates the intervening tangle; it does not assert that
the tangle is invariant under that rotation. The rotation depends only
on the parity of \(a\), preserves crossing signs, and is pushed through
the ordered syntax by the actual rotation identities. The closed
pairing in the last move has its recorded reflection and no extra
boundary twist. Cyclically moving the cut in the closed cylinder also
gives \(C(FG)\simeq C(GF)\).

To expose a selected leaf, follow its path to the root. Associativity
and closed cyclicity transfer each sibling into the other factor;
the last identity of (3) transfers every encountered turn. This
terminates at a form \(C(h_iQ)\), retaining every other leaf exactly
once and recording every induced order. If the selected weight is zero,

$$
C(h_i(0)Q)\simeq D(Q).
\tag{4}
$$

This uses \(h_i(0)=T(R^0)\), the cup-cap tangle; it is not the
through-identity tangle.

At a cap-closed root one has

$$
D(TF)=C(\tau F),\qquad
D(FG)=D(F)\mathbin{\#}D(G).
\tag{5}
$$

In the second operation, the upper-cap component of \(D(F)\) is joined
to the lower-cap component of \(D(G)\). The horizontal empty collar
contains a sphere meeting the link in exactly two points. Cutting it
and capping its punctures gives the two stated cap closures. Hence this
is an exhibited componentwise connected sum, with its components and
marks specified. It is not a four-punctured Conway mutation.

![The sphere around the lower tangle and its bottom cap meets the two connecting strands. Cutting and capping gives the two specified cap closures.](../book/figures/conway-cap-splitting.png)

The diagram uses bottom-to-top stacking: \(F\) is below \(G\). The
amber arcs are the new upper cap of \(F\) and lower cap of \(G\).
Joining along these arcs reconstructs the original stack. This specifies
the connected sum even when a cap closure has more than one component.

For a cylindrical product, the established ordered normalization
gathers direct integral factors using (3), fuses them, and records
their disjoint label unions. Any resulting zero weight can be removed
by (4). With no remaining zeros, its output is strict or is one
integral braid closure. The possible failed \(LL\) closing pair is
resolved by

$$
C((TU)(TV))\simeq C(U(\tau V)),
\tag{6}
$$

which exposes two integral factors for a genuine fusion. Root turns
switch \(C\) and \(D\), retaining \(\tau\) where (5) requires it. A
single box terminates in one of

$$
C(R^s),\quad D(R^s),\quad
C(h(s))=D(R^s),\quad D(h(s))=C(R^s).
\tag{7}
$$

Here \(C(R^s)\) is the \((2,s)\) torus braid closure and \(D(R^s)\)
is an unknot. The latter isotopy moves successive crossings into the
end cap and removes curls. Any ribbon framing is transported and
recorded, not silently replaced by a blackboard convention. At \(s=0\),
\(C(R^0)\) is the two-component unlink.

The one-box rule is applied before a numerical-zero deletion. In
particular a last zero box terminates as the appropriate unknot or
two-component unlink in (7); it is not removed to create an unspecified
empty scalar or an unrecorded component.

Fix a rule for selecting the next operation; for example, give the
one-box rule priority, process the root closure next, and choose the
first eligible leaf or stack in the written order for the remaining
steps. Use this same rule for every integer assignment. Every fusion or zero deletion lowers the
number of live labelled blocks. Between such events, shortening turn
chains, flattening stacks, and processing cap roots removes vertices
from the finite expression forest. Exposing a chosen zero follows a
finite path without copying its siblings. Thus the process terminates.
Connected-sum edges form a tree because each arises by splitting one
pending factor into two; rotations and later reductions act within
these factors and retain the attaching arcs.

## 3. Finitely many output types and one threshold

The algorithm only tests two kinds of integer data:

$$
\bigl(n_i\bmod2\bigr)_{i=1}^m,\qquad
\bigl(\mathbf 1_{W_B(\mathbf n)=0}\bigr)_{
                 \varnothing\ne B\subset\{1,\ldots,m\}}.
\tag{8}
$$

The first determines every \(\rho^{W_B}\) decoration. The second
determines every numerical-zero deletion. Rotations preserve the signs
of the integral crossings, fusion takes an ordinary sum, and no step
copies a label. Every integer expression tested is consequently one of
the subset sums (1), not an unbounded new family of linear forms.

There are finitely many patterns (8), although some are not realized by
integer tuples. On each realized pattern, the chosen schedule, ordered
output templates, attaching components, and surviving/deleted label
blocks are fixed. Their integer weights remain the displayed linear
forms. In particular, approaching another zero wall may change the
partition, but there are only finitely many such possibilities.

Let \(\mathcal S_E\) be the finite set of strict terminal templates
that occur among the realized patterns. For each template \(\sigma\),
the existing
[strict-tree theorem](actual_conway_all_strict_tree_long_twist_volume.md)
supplies a finite threshold \(B(\sigma)\), uniform over its independently
signed weights and its knot-producing parity choices. Set

$$
B_E=\max\!\left(\{2\}\cup
                   \{B(\sigma):\sigma\in\mathcal S_E\}\right).
\tag{9}
$$

This maximum is finite. It gives a single threshold for the fixed
input, over all input parities and all subset-sum zero patterns.
It is an existence and finite-reduction statement; no effective
numerical algorithm for the analytic thresholds is added here.

## 4. A knot input makes every terminal factor a knot

Retain all closed components throughout the reductions. If \(c_v\ge1\)
is the number of components of terminal factor \(v\), and the decomposition
tree has \(r\) vertices, componentwise connected sum gives

$$
c(K)=\sum_v c_v-(r-1)
    =1+\sum_v(c_v-1).
\tag{10}
$$

Thus a one-component input forces \(c_v=1\) for every factor. In
particular, no even-\(s\) torus braid closure or two-component zero
closure can occur among the terminal factors of the knot.

Within a terminal tangle expression, a circle already closed in a
subtree cannot reconnect to an outside endpoint. The remaining two
arcs still close to at least one other component. Therefore a terminal
knot has no such internal circle. Its whole component test, including
these circles, satisfies the hypothesis of the strict-tree theorem.

By (9) and the assumed longness, every strict terminal factor is a
hyperbolic knot with the established volume limit. A terminal elementary
knot is either an unknot or a \((2,s)\) torus knot with odd \(|s|\ge3\).
No assertion is being made about the primeness of an unknown short
strict factor: the longness hypothesis has removed that case.

## 5. The group obstruction to two nontrivial factors

Let \(\mu\) denote a knot meridian. Its class generates the infinite
cyclic abelianization, so its cyclic subgroup is infinite and injective.
Van Kampen applied to the meridional annulus of a connected sum gives

$$
\pi_1(X_{K_1\#K_2})
\cong
\pi_1(X_{K_1})*_{\langle\mu\rangle}\pi_1(X_{K_2}),
\tag{11}
$$

where the two meridians are identified, with their orientation carried
through the attaching arcs. Iterating over the exhibited sum tree gives
the analogous amalgam of all factor groups over the same infinite cyclic
subgroup. The usual reduced-word proof for an amalgam injects each
factor group. If \(u\) and \(v\) belong to different factor groups and
neither belongs to \(\langle\mu\rangle\), the word

$$
uvu^{-1}v^{-1}
\tag{12}
$$

is a reduced word of length four, and is not the identity.

Each nontrivial factor in Section 4 has an element outside
\(\langle\mu\rangle\) which commutes with \(\mu\).

For a long hyperbolic factor, take its preferred longitude. Its complete
rank-two cusp injects the peripheral \(\mathbb Z^2\) into the group, so
the longitude is not a power of the meridian.

For a \((2,s)\) torus knot, odd \(|s|\ge3\), use its central fiber.
Here is an argument independent of a longitude sign convention.
The two solid tori on either side of the standard torus, joined through
the annulus left by the knot neighborhood, give

$$
G_s=\langle a,b\mid a^2=b^s\rangle,\qquad z=a^2=b^s.
\tag{13}
$$

The annulus winds twice around one core and \(s\) times around the
other, which gives this relation. The element \(z\) is central.
Abelianization is infinite cyclic, with
\([a]=s t\), \([b]=2t\), and \([z]=2s t\). A meridian has class
\(\pm t\).

The quotient by \(\langle z\rangle\) is
\(C_2*C_{|s|}\). Its abelianization is cyclic of order \(2|s|\),
and the image of any meridian is a generator of that abelianization.
A finite-order element in a free product is conjugate into a factor:
after cyclic reduction, a word of length at least two has powers of
strictly increasing reduced length. Its finite order would therefore
divide \(2\) or \(|s|\), incompatible with abelianization order \(2|s|\).
The image of \(\mu\) in this quotient has infinite order.

It follows that \(z\notin\langle\mu\rangle\). Indeed
\(z=\mu^k\) would force \(k=\pm2s\) in abelianization and then force
a nonzero power of the infinite-order image of \(\mu\) to vanish
in the quotient. More strongly, a relation \(\mu^u z^v=1\)
first gives \(u=0\) in the quotient and then \(v=0\) by abelianization.
Thus \(\langle\mu,z\rangle\cong\mathbb Z^2\).
This proves the precise commuting-element fact needed below without
assuming a peripheral injection theorem for torus knots. In conventional
oriented torus coordinates the preferred longitude is
\(z\mu^{-2s}\), because the torus push-off has linking number \(2s\);
that additional identification is not used.

Now suppose two terminal factors are nontrivial. Choose the elements
just constructed in their two groups. They both commute with the
common meridian, while (12) proves that they do not commute with each
other. Hence the centralizer of \(\mu\) in the input knot group is
nonabelian.

This is impossible for the hyperbolic input. Its faithful complete
holonomy sends a meridian to a nontrivial parabolic. Conjugate this
parabolic to \(z\mapsto z+1\). A Möbius transformation commuting with
it must fix its unique point at infinity and have the form
\(z\mapsto z+c\). Such transformations commute. Faithfulness therefore
makes the meridian centralizer in the knot group abelian.

There is at most one nontrivial terminal factor.

## 6. Selecting the strict factor and transporting the conclusion

If every factor were an unknot, the input would be an unknot. If its
only nontrivial factor were a torus knot, the input would be that torus
knot. The first has cyclic group. The second has the nontrivial central
element \(z\) of (13), so neither can be a finite-volume hyperbolic knot.
For completeness, the center of such a hyperbolic knot group is trivial:
a central element commutes with the peripheral parabolic group and is
itself a translation fixing that cusp point; centrality would force
every group element to commute with this nontrivial translation. The
same Möbius calculation then makes every element a translation. A
discrete translation group has an infinite-volume quotient of all of
hyperbolic three-space, even when its quotient horospheres are compact.
It cannot be the complete finite-volume knot group.

Consequently the unique nontrivial factor is strict, and all other
terminal factors are unknots. Connected sum with each exhibited unknot
is removed by straightening the trivial summing arc across its spanning
disk. This gives an actual orientation-preserving ambient isotopy from
the input knot to the one strict terminal knot \(K_*\).

Restricting that isotopy to transported tubular neighborhoods gives a
homeomorphism of exteriors carrying the meridian and preferred
zero-linking longitude. Pull back the already constructed complete
hyperbolic metric of \(S^3\setminus K_*\); this supplies the same complete
metric and volume on the input complement. There is no attempt to
identify the different augmented exteriors before auxiliary filling.

The reduced enhanced Kashaev invariant is the invariant of this same
zero-framed knot, so \(K_N(K)=K_N(K_*)\) at every level. If ribbon
framings are kept during the moves, their correction is the existing
unit complete-color twist; zero-framing removes it, and its modulus
would not change the logarithmic rate in any event. The full one-cut
modified value retains its single factor

$$
\mathcal N_N(K;1)=\frac{i^{N+3}}{N}K_N(K).
\tag{14}
$$

Apply the inherited strict-tree volume theorem to \(K_*\). These exact
identifications prove (2). Neither multiplicativity of \(K_N\) nor
additivity of quantum exponential rates over a connected sum is used.

## 7. Scope of the extension

The conclusion applies to either closing operation on every fixed
finite expression made by the stated actual Conway operations, including
initial root turns and all numerical-zero walls. The prescribed
reduction and the uniform threshold account for all their finitely many
parity and zero patterns.

The hypothesis that the original filled link is a hyperbolic knot is
essential to this argument. For a composite input, two long strict
factors can remain, and (12) correctly detects the obstruction.
No new quantum connected-sum theorem has been proved here.

Long written twists alone do not imply the hypothesis on surviving
strict weights: opposite large twists can cancel. Conversely, original
weights or intermediate sums may be zero; only final weights in strict
terminal factors must satisfy (9). The theorem does not give a
short-twist assertion or a threshold uniform over growing expressions.

The topological input is the actual ordered normalization and its
two-punctured cap spheres, not the commutativity of the colored source.
The analytic and geometric long-filling theorem is inherited for the
strict terminal presentation. The new step is the finite all-root
reduction together with the group argument forcing a hyperbolic input
to equal one of those known strict knots.

## 8. A finite topological criterion and simple conditions on the integers

The reduction itself requires no hyperbolic metric. It uses the ordered
tangle expression, its endpoint connections, and the integer sums in (1).
Under the longness assumption of the theorem, its output also determines
whether a knot input is hyperbolic:

**Corollary 1.** Suppose the input has one component and every surviving
strict-factor weight has magnitude greater than \(B_E\). The input is
hyperbolic if and only if its reduction has exactly one strict factor
and every other terminal factor is an unknot.

Indeed, the forward implication is Sections 4–6. For the reverse
implication, straighten the summing arcs of the unknot factors. The
resulting knot is the long strict factor, whose complete hyperbolic
metric is supplied by the strict-tree theorem.

The elementary factors are explicit. A factor \(D(R^s)\) is always an
unknot. A factor \(C(R^s)\) is a knot only for odd \(s\), and among
those knots it is an unknot exactly when \(s=1\) or \(s=-1\).
Consequently the reduction gives a finite topological test once the
longness hypotheses have been established. Determining whether an
elementary factor is trivial requires these tests for \(s=\pm1\), in
addition to the parity and zero tests used to choose the output templates.
No numerical values for the inherited analytic thresholds are supplied
by this argument.

There is also a sufficient condition stated entirely in the original
integer parameters. It is stronger than the condition on surviving
strict factors, but avoids computing which of their sums will survive.

**Corollary 2.** Fix the expression and closure, and suppose that

\[
 \sum_{i\in B}n_i=0
 \quad\text{or}\quad
 \left|\sum_{i\in B}n_i\right|>B_E
 \qquad\text{for every nonempty }B\subseteq\{1,\ldots,m\}.
 \tag{15}
\]

If the resulting knot is hyperbolic, it satisfies (2). In particular,
fix any integer vector \(\mathbf a\) and set \(\mathbf n=t\mathbf a\).
For every integer \(t\) with \(|t|>B_E\), every hyperbolic knot obtained
in this way satisfies the volume equality. The parameter \(t\) is fixed
before the quantum level \(N\) tends to infinity.

To prove the corollary, each surviving strict weight is a nonzero subset
sum, so (15) implies the theorem's hypothesis. On the integer ray, such
a sum is \(t\sum_{i\in B}a_i\); its magnitude is at least \(|t|\)
unless it vanishes. This also allows zero entries and exact cancellations
in \(\mathbf a\). The corollary does not say that every ray contains
hyperbolic knots; Corollary 1 determines the topological alternative
under the same longness condition. Another sufficient special case of
(15) is that all original integers have the same sign and each has
magnitude greater than \(B_E\).

## 9. The operator period and the volume of this complement

The [pointed quantum \(A\)-period theorem](actual_conway_pointed_quantum_a_volume.md)
applies to the same reduced knot invariant. Fix a genuine annihilator
\(P\), its prescribed finite vector of initial ordinary-color
polynomials \(c_0(q)\), and the companion row \(r_N(q)\). With
\(q_N=e^{\pi i/N}\), its exact reconstruction is

\[
 \mathscr P_N(P,c_0)
 =\operatorname{CT}_{u=0}
   \bigl[r_N(q_N(1+u))c_0(q_N(1+u))\bigr]
 =K_N(K).
 \tag{16}
\]

The product of Laurent germs is formed before its constant term is
taken. This retains the derivatives needed at singular recurrence steps.
The required number of initial derivatives depends on the fixed
operator, not on \(N\). For every knot satisfying the theorem,

\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|\mathscr P_N(P,c_0)|
 =\operatorname{Vol}(S^3\setminus K).
 \tag{17}
\]

The positive Gram determinant ratio of the same pointing theorem has
the exact value \(\mathscr G_N=\sum_{j=j_0}^{N}|C_j(q_N)|^2\).
Its ordinary-color terms have a polynomial total bound. Therefore
\((\pi/N)\log\mathscr G_N\) tends to this same positive volume.
These conclusions transfer through the actual knot isotopy of Section 6;
they do not compare unrelated recurrence operators or their classical
polynomial factors. The classical geometric-factor question remains
separate.
