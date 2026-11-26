# From long fillings to finitely many exceptions

Research note, 2 November 2026. The manuscripts remain frozen. This note
proves elementary consequences of their stated hypotheses and a limitation
of the printed directed criterion. It does not prove a new volume theorem
for short fillings.

## 1. The target and the present quantifiers

The target is Kashaev's original volume identity for a hyperbolic knot K:

\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|\langle K\rangle_N|
   =\operatorname{Vol}(S^3\setminus K).
\]

There are two different finite-exception questions:

1. For one fixed marked tangle template, are only finitely many integer
   filling assignments that give hyperbolic knots untreated?
2. Among all hyperbolic knot types, are only finitely many untreated?

The second statement does not follow from the first for infinitely many
templates. Parameter assignments also need not give distinct knot types.

For a fixed admissible template with d filling parameters, the current
theorem supplies a finite nonnegative integer B such that every assignment with
|p_i| > B for every i satisfies the volume identity. All parameters are
fixed before the level N tends to infinity. The threshold can depend on
the template. A retained half-twist pattern is fixed, so integer surgery
parameters already preserve the relevant crossing parities.

## 2. The density consequence

For an integer H > B, the fraction of assignments in [-H,H]^d covered
by this sufficient condition is exactly

\[
 \left(\frac{2(H-B)}{2H+1}\right)^d.
\]

Indeed each coordinate has 2(H-B) choices outside [-B,B]. The number
not certified by this condition is at most

\[
 d(2B+1)(2H+1)^{d-1},
\]

by the union bound over coordinates. Thus the covered assignments have
density one in this fixed parameter space. For d >= 2, the complement
of this sufficient condition is nevertheless infinite: p_1 can remain
zero while p_2 tends to infinity. This is a statement about untested
assignments, not about failures of the volume conjecture or necessarily
about infinitely many distinct untested knot types.

For a single free parameter the corresponding exceptional assignments
are already finite. No counting statement here concerns knots ordered
by crossing number.

## 3. A finite-exception lemma for one template

Let D be any subset of Z^d. In the intended application, D consists of
the assignments giving hyperbolic knots with the prescribed marking.
Let P(p) be a property defined for p in D; here P is the volume identity.

For I a proper subset of {1,...,d} and a in Z^I, fixing p_i=a_i for
i in I is called a partial assignment. The coordinates outside I
remain free.

**Proposition.** Suppose that every partial assignment (I,a) has a
finite integer B(I,a) >= 0 such that

\[
 \mathbf p\in D,\quad p_i=a_i\ (i\in I),\quad
 |p_j|>B(I,a)\ (j\notin I)
 \quad\Longrightarrow\quad P(\mathbf p).
\]

Then D contains only finitely many points where P fails.

**Proof.** Begin with I empty. A point where P fails has a free
coordinate j with |p_j| <= B(I,a). Branch over the finitely many
choices of j and of the integer p_j in that interval, adding this
coordinate to I. Apply the same argument at each new partial
assignment. There are finitely many children at every node, and
every step fixes one previously free coordinate. After at most d
steps each remaining branch specifies one complete tuple. A finite
tree of bounded depth has finitely many leaves. Every point of D
where P fails belongs to this finite set of complete tuples. QED.

The thresholds may depend arbitrarily on the previously fixed values;
no uniform threshold over all partial assignments is assumed. If the
thresholds and applicable source theorems are effective, the argument
also gives an effective finite list. It does not settle the points
on that list.

The lemma only needs the partial assignments visited by the finite
branching procedure. Proving a theorem stable under all fixed partial
fillings is a convenient sufficient hypothesis, stronger than that
finite collection of needed cases.

## 4. The missing stability theorem

The next substantive target is the following statement, currently
unproved in this project:

> Fix an admissible marked parent, choose one of its crossing circles,
> and give that circle any fixed integer filling, provided at least one
> crossing circle remains unfilled. For all independently
> sufficiently long fillings of the remaining crossing circles that
> produce hyperbolic knots, prove the original Kashaev volume identity.
> Establish the same statement for the partially filled sources so
> that it can be applied repeatedly.

Stop the iteration when no free coordinate remains. Those finitely
many fully assigned leaves are the possible exceptions; no theorem
for them is being smuggled in through a vacuous longness condition.

One application alone is insufficient in three or more parameters:
there can be two or more short coordinates. The class of sources must
be stable under iteration, or each required partial assignment must
be treated separately.

The existing filling-functional norm estimate is already valid for
every fixed integer crossing power n:

\[
 |\mathcal L_N^n H|\le(1+|n|/2)\|H\|_{[-2,2]}.
\]

Its prefactor has zero exponential rate as N tends to infinity.
Therefore an upper bound for the short filling is not the main missing
step. The problem is to identify the geometric stationary point after
the partial filling, prove that its contribution is nonzero, and bound
the other contributions below it. A closed-tangle volume limit does
not provide the uniform open-boundary estimates needed for further
gluing.

Intermediate partial fillings need not remain in the current geometric
class. One cannot silently discard an intermediate nonhyperbolic
exterior without proving that its relevant descendants are absent or
already controlled. The abstract proposition uses only the final
domain D and hides no assumption about intermediate hyperbolicity.

## 5. A concrete limitation of the current directed estimates

The directed criterion in
[the circle-tree manuscript](../papers/circle-tree-volume/directed-criterion.tex)
fixes k_0=2^{-16} and t_0=2^{-14}. At a nonroot leaf, the degree is
one and there are no child contributions. Its quantities are

\[
 A=\frac{2k_0}{\pi^2},\qquad
 C=16+\frac{n^2}{32k_0},\qquad
 |D|^2=\frac{1+n^2}{4\pi^2},\qquad
 \beta=\frac{420\pi}{361(1+n^2)}.
\]

The printed contour-height and error estimates give

\[
 y\le\frac{t_0|D|}{4C},\qquad
 \eta\le\frac{t_0|D|y}{2}
       \le\frac{t_0^2|D|^2}{8C}.
\]

For n nonzero, the required inequality beta < eta/2 therefore implies

\[
 n^2+2+n^{-2}>
 \frac{840\pi^3}{361t_0^2k_0}.
\]

Since pi > 31/10 and t_0^2 k_0=2^{-44}, the right side exceeds
69 times 2^{44}. If 1 <= |n| <= 2^{25}, the left side is at most
2^{50}+3, which is smaller. For n=0 the separate required condition
t_0|D| >= 2 fails. Thus:

**Proposition.** No nonroot leaf with |n| <= 2^{25} satisfies the
printed directed criterion, for any choice of its adjustable decay
parameters.

Every finite tree with at least two vertices has a nonroot leaf,
whatever root is selected. This limitation concerns this sufficient
criterion alone. It is not a necessary condition for the volume
identity, nor a limitation on all other methods in the project.
It shows why optimizing the final 2^{27} rounding cannot reach
ordinary short twists without changing the analytic estimates.

## 6. The additional issue for all hyperbolic knots

To pass from fixed templates to finitely many excluded knot types,
one sufficient statement would be a universal C such that every
hyperbolic knot either has an established volume proof or has crossing
number at most C. There are finitely many knot types of bounded
crossing number. The current degree-and-twist criteria supply no
such bound on untreated knots.

Two weaker conclusions must not be mistaken for this statement:

- Finitely many short local tangle types can form arbitrarily large
  diagrams.
- Finitely many unresolved reduced cores can have infinitely many
  unresolved extensions. A reduction that only transports a proof
  from a core to its extensions does not control those extensions
  when the core remains unresolved.

Nor can all hyperbolic knots be fillings of a finite list of fixed
hyperbolic parents: filling decreases hyperbolic volume, whereas
hyperbolic knot volumes are unbounded. Explicit weaving-knot bounds
are given by [Champanerkar--Kofman--Purcell](https://arxiv.org/abs/1506.04139).
The general finite-exception target needs a theorem handling unbounded
diagram complexity, in addition to the partial-filling theorem above.

## 7. Attribution and novelty

[Kashaev's original conjecture](https://arxiv.org/abs/q-alg/9601025)
is the target. Chen and Yang explicitly credit it in the introduction
to their [different conjectures for Turaev--Viro and Reshetikhin--Turaev
invariants](https://arxiv.org/html/1503.02547v4). A theorem about those
invariants does not automatically prove the original Kashaev evaluation.
The [long-filling theorem stated by Shen](https://arxiv.org/abs/2609.11839v3)
belongs in related work rather than direct coverage of our main knot
theorem. A reflection or cancellation argument taken from it must
nevertheless be credited, and its existing scope matters to any claim
that a particular analytic technique is new.

The counting and finite-branching propositions above are elementary
deductions. They are not being advertised as new knot theorems. The
research contribution still sought is the stability under short partial
fillings and the control of arbitrarily long compositions of short
tangles.

## 8. A consequence of counting assignments: strict padding

The literal finite-assignment target is stronger than a statement about
distinct knot types. The following observation was obtained while
pursuing the active goal. It uses the ordered conventions and the
explicit cap isotopies of
[Ordered tangle reductions and long net twists](../papers/conway-reductions/closures.tex).
Here "strict" means the enlarged literal grammar in
[the Conway asymptotics manuscript](../papers/conway-asymptotics/main.tex):
the closing children may be elementary or turned elementary boxes.
The construction below is not asserted to belong to the older,
narrower grammar requiring two completed closing children.

Write T for a physical quarter-turn, h(n)=T(R^n) for an elementary
leaf, C for cylindrical closure, D for cap closure, and tau=T^2
for the physical half-turn. An unframed cap closure D(R^a) is an
unknot for every integer a: its crossings are removable curls.
The zero leaf h(0) closes an adjacent tangle by caps. Consequently

\[
 C(h(0)F)\simeq D(F),\qquad
 D(FG)\simeq D(F)\mathbin\# D(G),\qquad
 D(TQ)\simeq C(\tau Q).
\]

The connected sum uses the two specified cap components; internal
components are retained. If C(Q) is a knot, the application below
contains no extra component. Rotating the entire cylindrical closure
identifies C(tau Q) with C(Q).

**Proposition.** For the class of strict Conway templates, these two
statements are equivalent:

1. Each fixed admissible template has only finitely many hyperbolic
   filling assignments at which the original Kashaev volume identity
   fails.
2. Every hyperbolic knot represented by a strict Conway template
   satisfies that identity, at every integer assignment of its powers.

**Proof.** The second statement implies the first with no exceptions.
For the converse, fix an arbitrary strict core K=C(Q), with all its
powers fixed, and assume K is hyperbolic. Add two new leaves and form

\[
 E(a,b)=C\bigl(h(b)[R^aT(Q)]\bigr).
\]

The factor R^a can be written T^3(h(a)), so the displayed expression
uses precisely the permitted leaves, turns, and products.

This is formally strict. When Q is inserted as an open tangle, its
former closing product becomes an ordinary retained product. This is
allowed: each permitted closed pair AA, AL, AH, LH (in either order)
also has a nonempty open product, respectively of type A, A, H, H.
All products below it were already strict. Thus Q, now considered
open, has output type A or H in the
[original type table](../papers/newton-calculus/supports.tex).
This is an existence argument for a new strict state; it does not
reuse the old closed optimizer. Consequently T(Q) has type A or L, while
R^a=T^3(h(a)) has type H. Their product has type H, and the outer
closing pair consists of types L and H, which is allowed. None of
these formal type assertions depends on the numerical powers.

At b=0 the cap identities give

\[
 E(a,0)\simeq D(R^aT(Q))
      \simeq D(R^a)\#D(T(Q))
      \simeq U\#C(\tau Q)\simeq K
\]

for every integer a. Fix either parity for a, use even parity at b,
and retain the core parities. These are infinitely many distinct
filling assignments in one fixed admissible marked template, all
giving the same hyperbolic knot. After the prescribed zero-framing
correction they have the same reduced invariant and volume. If K
failed the identity, the first statement would be contradicted.
Therefore K satisfies it. Since the core was arbitrary, the second
statement follows. QED.

More explicitly, choose retained carriers \(\eta_a=\eta_b=0\)
at the two new circles and keep the fixed core carriers. In the
original primitive surgery coordinates, the assignments
\[
             (p_a,p_b,\mathbf p_Q)=(r,0,\mathbf p_Q),
             \qquad r\in\mathbb Z,
\]
give \(a=-2r\), \(b=0\), and the same fixed core. They are distinct
tuples of the original template. Its retained pattern passes the
knot test: changing a braid power by an even integer changes no
endpoint pairing or internal component, and every displayed closure
is the knot \(K\). The physical half-turn \(\tau\) permutes the
cylindrical closing pairs \(\{0,3\},\{1,2\}\), carrying the prescribed
empty outside arcs to one another. Thus the last isotopy above is
the rotation of the entire closed picture, with no unrecorded
boundary Dehn twist.

This does not disprove the requested theorem. It identifies its actual
strength: a proof for every strict template cannot leave any unresolved
hyperbolic strict core behind a finite list of assignments. Replacing
assignments by distinct knot types, or excluding inessential parameters,
would change the goal and is not done here.

The same construction explains why a short partially filled exterior
that is nonhyperbolic cannot simply be ignored. Its remaining circle
can control a removable curl while all its fillings still produce the
fixed hyperbolic knot K. The proposed partial-filling theorem must
handle this possibility rather than assume that every intermediate
exterior remains in the original augmented geometric class.
