# When a fixed rational corridor can be replaced by one twist region

This note gives an exact test for a marked reduction of an entire
fixed rational word. Both outside attachments remain arbitrary.
The test uses the integral matrix of the word on the double cover
of its four-point boundary sphere. It includes the rotations that
are invisible in that matrix.

When the test succeeds, the remaining crossing powers receive
constant shifts. Their original parameter map is therefore
injective. When it fails, the proposed one-vertex reduction is
unavailable; this says nothing against the volume identity for
that word. A general short connected source still needs its own
theorem.

## 1. The actual boundary maps

Use the original clockwise physical turn \(T\), bottom crossing
\(R\), and endpoint order
\[
 0=\mathrm{BL},\quad1=\mathrm{BR},\quad
 2=\mathrm{TR},\quad3=\mathrm{TL}.
\]
The supported collar calculation in
[the marked degree-two moves](research_marked_degree_two_tangle_moves.md),
Section 2, gives the following affine maps of the pillowcase:
\[
 \widetilde T(x,y)=(-y,x+\tfrac12),\qquad
 \widetilde R^{\,n}(x,y)=(x+ny+\tfrac n2,y).
 \tag{1}
\]
The pillowcase is the quotient of
\(\mathbb R^2/\mathbb Z^2\) by the deck involution
\((x,y)\mapsto(-x,-y)\). Write
\[
 S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
 A_n=\begin{pmatrix}1&n\\0&1\end{pmatrix}
 \tag{2}
\]
for the linear parts. Every finite signed word \(W\) in these
physical operations has an affine lift
\[
             \widetilde W(z)=Gz+v,\qquad
 G=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\mathrm{SL}_2(\mathbb Z),
 \quad v\in\tfrac12\mathbb Z^2.
 \tag{3}
\]
The lift is computed by ordinary affine composition in the same
order as the word. It is not inferred from its endpoint permutation.

The three nonzero half-lattice translations are the actual proper
half-turns
\[
\begin{array}{c|c}
 (1/2,0)&\rho\\
 (0,1/2)&K\\
 (1/2,1/2)&\tau=T^2 .
\end{array}
\tag{4}
\]
They must be carried on an arbitrary attached tangle. Their linear
parts are the identity after passing to the deck quotient.

A *one-vertex collar form* means a boundary mapping-class identity
\[
 W(F)\simeq
 R^rT\!\left(R^mT\!\left(R^s H(F)\right)\right),
 \qquad H\in\{1,\rho,K,\tau\},
 \tag{5}
\]
for arbitrary tangles \(F\), with their marked arcs, closed
components and ribbons transported. The two integral factors at
the ends are intended to be collected with the two surviving
neighboring twist regions. This definition retains the original
outside frames: it does not permit an additional quarter-turn of
one outside attachment.

## 2. The exact two-boundary criterion

**Proposition 1.** Suppose \(c\ne0\). The word \(W\) admits
a one-vertex collar form if and only if
\[
                 a\equiv d\equiv\varepsilon\pmod{|c|}
                 \quad\hbox{for some }\varepsilon\in\{1,-1\}.
 \tag{6}
\]
For any such choice put
\[
 c'=\varepsilon c,\qquad
 r=\frac{\varepsilon a-1}{c'},\qquad
 s=\frac{\varepsilon d-1}{c'},\qquad m=-c'.
 \tag{7}
\]
These are integers, and (5) holds with an explicitly determined
half-turn \(H\).

**Proof.** For integers \(r,s,c'\),
\[
 A_r\begin{pmatrix}1&0\\c'&1\end{pmatrix}A_s
 =
 \begin{pmatrix}
 1+rc'&r+s+rc's\\c'&1+c's
 \end{pmatrix}.
 \tag{8}
\]
Also \(SA_mS=-\left(\begin{smallmatrix}1&0\\-m&1\end{smallmatrix}\right)\).
Thus (5) implies (6), since its linear part must agree with \(G\)
up to the one deck sign. The rotations in (4) do not change this
condition.

Conversely, the choices (7) make the diagonal and lower-left
entries in (8) equal to those of \(\varepsilon G\).
Their upper-right entries agree as well: their determinants are
one and \(c'\ne0\), so that entry is uniquely
\(((\varepsilon a)(\varepsilon d)-1)/c'\).
Consequently
\[
 A_rSA_mSA_s=-\varepsilon G.
 \tag{9}
\]
Let \(\widetilde B\) be the full affine lift of the right side
of (5) before inserting \(H\), using (1), not merely (9).
Write
\[
       \widetilde B^{-1}\widetilde W(z)
                    =\lambda z+w,\qquad \lambda=-\varepsilon.
\]
Here \(w\in\tfrac12\mathbb Z^2\). On the pillowcase this
relative map is translation by
\(\delta=\lambda w\bmod\mathbb Z^2\): applying the deck
involution if \(\lambda=-1\) changes the linear part to
the identity. Select \(H\) from (4), including the identity,
with that translation. Then
\(\widetilde W=\widetilde B\,\widetilde H\) as pillowcase maps.

The supported representative of every crossing in (1) is
isotopic to its affine representative relative to the four
marked points. Hence the equality just proved is an equality
of the actual boundary mapping classes. Extend the isotopy
over a collar. The difference of the resulting ball maps
fixes its boundary pointwise and is contracted by the
Alexander isotopy. Applying these maps to all of \(F\)
proves (5), carrying its closed components and markings.
\(\square\)

The second congruence in (6) follows from the first and
\(ad-bc=1\), but writing both makes the symmetry between
the two retained ends explicit. When \(|c|\) is one or
two the sign choice need not be unique; either resulting
form is valid with its own affine rotation.

If \(c=0\), the determinant gives \(a=d=\pm1\).
After the deck sign \(G=A_k\) for an integer \(k\).
The same affine calculation gives \(W(F)\simeq R^kH(F)\).
There is then no intervening turn. In a circle-tree
application this can merge two still variable twist
regions. The parameter issue is different from (7)
and is treated in Section 5.

The necessity statement is about the collar form (5).
Special attached tangles can have additional stabilizers;
it does not claim that no other isotopy exists for a
particular choice of \(F\).

## 3. The pendant version, including caps

Let \(I=R^0\) be the through tangle. In the slope convention
of (2), its vector is \((0,1)^T\), and the rational tangle
\(W(I)\) has slope
\[
                      p/q=b/d,
 \tag{10}
\]
reduced with \(q\ge0\). This convention gives slope \(n\)
to \(R^n\) and sends \(z\) to \(-1/z\) under \(T\).

For completeness, equality of these slopes gives a literal
tangle isotopy in the present conventions. If two affine
words have proportional second columns, their relative
linear map, after a deck sign, is
\(\left(\begin{smallmatrix}1&0\\k&1\end{smallmatrix}\right)\).
It is \(SA_{-k}S^{-1}\). In its physical realization one
turn first makes the cup-cap tangle; the intervening
crossings are curls adjacent to its cap and can be removed
by an isotopy, with the ribbon transported. Turning back
therefore fixes \(I\). The remaining affine discrepancy
is one of the half-turns (4), all of which preserve \(I\).
This proves the required stabilization directly.

**Proposition 2.** For \(q\ge2\), a pendant word has the form
\[
                         W(I)\simeq R^rT(R^m),
                         \qquad |m|\ge2,
 \tag{11}
\]
with its original outside frame, if and only if
\[
                          p\equiv1\ \hbox{or }-1\pmod q.
 \tag{12}
\]
If \(p\equiv-1\pmod q\), take \(m=q\) and
\(r=(p+1)/q\). If \(p\equiv1\pmod q\), take
\(m=-q\) and \(r=(p-1)/q\).

Indeed the slope of the right side of (11) is
\(r-1/m=(rm-1)/m\), already a reduced fraction.
This proves necessity and supplies the stated choices;
the stabilization argument above proves sufficiency.

For \(q=1\) the tangle is the integral braid \(R^p\);
its fixed power can be collected with its parent.
For \(q=0\) it is the cup-cap tangle \(T(I)\).
This last case invokes the actual cap decomposition,
not a positive terminal source. It can expose arbitrary
closed factors in a larger Conway expression.

The elementary slope calculation belongs to the classical
rational-tangle calculus; see
[Kauffman–Lambropoulou](https://arxiv.org/abs/math/0311499).
The proof above specifies the supported maps and stabilizers
used for these particular marked reductions. No novelty is
claimed for the classification of rational tangles.

## 4. What the test says for two adjacent powers

For two fixed internal powers \(a,b\), the corresponding
two-boundary word is \(TR^bTR^aT\). Its matrix is
\[
                 SA_bSA_aS
                 =\begin{pmatrix}-a&1\\ab-1&-b\end{pmatrix}.
 \tag{13}
\]
Suppose \(|a|,|b|\ge2\). Then it has a one-vertex
collar form exactly when
\[
                         (a,b)=(2,2)\quad\hbox{or }(-2,-2).
 \tag{14}
\]
To prove this assertion, if \(ab<0\), then
\(|ab-1|=|a||b|+1>|a|+1,|b|+1\); neither nonzero
diagonal entry in (13) can be congruent to \(1\) or
\(-1\) modulo that number. If \(ab>0\), write
\(A=|a|\), \(B=|b|\). The modulus is \(AB-1\),
strictly larger than \(A,B\). The only possible
congruence in (6) requires
\[
                     A=B=AB-2.
\]
Thus \(A=B\) and \(A^2-A-2=0\), giving \(A=B=2\).
The two indicated pairs do satisfy (6).

For the mixed pendant word \(TR^{-2}TR^2\),
\[
                  SA_{-2}SA_2
                     =\begin{pmatrix}-1&-2\\-2&-5\end{pmatrix},
 \tag{15}
\]
so its slope is \(2/5\). It fails (12); its two-boundary
extension also fails (6). Its now proved boundary theorem
and marked geometry therefore supply information that
this one-vertex compression cannot supply.

Longer fixed words are tested by the same matrix
calculation; they are not restricted to a displayed list
of short powers. The
[same-sign two-crossing theorem](research_repeated_two_crossing_chain_reduction.md)
is one family for which the test succeeds at every length,
with its rotation already given in closed form.

## 5. Original filling parameters and the volume consequence

Consider a fixed ordered circle-tree template. Fix all
powers in finitely many disjoint degree-two corridors
and pendant rational strings. Keep at least one outside
circle unfilled. Each corridor has exactly two ends
at outside circles and no side branch; each pendant
string has exactly one outside end.

Suppose every corridor passes (6) with \(c\ne0\), and
every pendant string is either integral or passes
(12) with \(q\ge2\). Apply the corresponding marked
reductions. In (5), collect \(R^r\) and \(R^s\) with
the powers at the two outside circles, using the actual
twist-sliding isotopy. All intervening branches receive
their prescribed proper rotations. The resulting
circle tree has one fixed nonzero degree-two power
\(m=-\varepsilon c\) for each corridor, and a fixed
terminal power of magnitude \(q\ge2\) for each
nonintegral pendant string.

The new selected vertices are nonadjacent: each
joins only the retained outside circles. The original
strand tracing and carrier parities are transported
by the isotopies. Suppose the reduced tree has at
least one edge. The complete isolated-boundary
theorem and its nonadjacent assembly therefore apply;
use [the full coverage statement](research_isolated_vertex_coverage_and_assembly.md),
which includes every nonzero degree-two power.
All remaining outside powers may be independently
sufficiently long, with either sign. Whenever the
transported closure is a knot with no internal closed
component, this gives its original Kashaev volume
identity.
If every edge has disappeared instead, the closure
is an integral two-strand braid closure, which has
no hyperbolic knot among its assignments. That case
does not invoke the hyperbolic isolated-boundary
theorem.

This conclusion concerns the original assignments.
Each surviving power changes by a fixed integer
\(\Delta_v\):
\[
                      n'_v=n_v+\Delta_v .
 \tag{16}
\]
The shifts can add when several fixed strings meet the
same outside circle. Choose its new carrier
\(\eta'_v\equiv\eta_v+\Delta_v\pmod2\). Then
\[
 p'_v=p_v+\frac{\eta'_v-\eta_v-\Delta_v}{2}.
 \tag{17}
\]
The fraction is an integer. Thus the map on all
remaining original surgery coefficients is a
translation, possibly followed by a recorded
permutation of labels. It is injective and preserves
independent eventual longness. All powers deleted
inside the strings were already fixed.

The reduction identifies the actual filled knot
complements and transports a supplied ribbon.
After the prescribed zero-framing conversion, their
reduced Kashaev invariants agree. This is a transfer
of a closed invariant theorem. It does not identify
unreduced boundary polynomials as ordinary functions
away from the repeated-root spectrum, nor supply
their asymptotics without a separate canonical
boundary-multiplication estimate.

If a corridor has \(c=0\), collecting the two end
powers instead gives a sum \(n_a+n_b+\Delta\).
When both remain free its fibers are infinite.
Similarly, the pendant cap case \(q=0\) uses the
cap-sum identities and can leave an arbitrary closed
core. These cases are not discarded as nonhyperbolic
intermediates. The exact rank test and core
obligation are proved in
[the reduction-fiber note](research_affine_reduction_fibers_and_core_obligation.md).

The congruence theorem therefore gives additional
exactly recognized long-remainder strata and a
complete test for this particular compression
strategy. It does not provide cofinite coverage of
all assignments or a reduction of every connected
arborescent block to the known source families.

## 6. Why an ideal-pants decomposition does not perform the missing reduction

There is a useful geometric distinction between an unfilled
belt and a filled twist region. Let \(\mu,\lambda\) be the
original primitive meridian and disk longitude at a crossing
circle. Filling the primitive slope \(\mu+p\lambda\) makes
\(\lambda\) a primitive core class: the two classes
\(\mu+p\lambda,\lambda\) have intersection determinant one.
On a positive-core hyperbolic filling, its holonomy is
loxodromic.

The original crossing disk had the curve \(\lambda\) as one
of the cuffs of its twice-punctured disk. A complete ideal
pair of pants has parabolic holonomy on every cuff.
Consequently that particular disk cannot remain a complete
ideal-pants seam after such a filling. It might enter a
different geometric subdivision, but keeping it as an ideal
seam would already contradict its primitive holonomy.
This is not a claim that the filled manifold contains no
other geodesic pants.

At retained unfilled belts, actual ideal pants can be glued.
The geometric existence and volume additivity of such belted
sums are established territory; see the introduction of
[Morgan–Ransom–Spyropoulos–Trapp–Ziegler](https://nyjm.albany.edu/j/2025/31-1p.pdf).
That paper's canonical decomposition is for fully augmented
links, and does not assert that an arbitrary partially filled
rational block still has those same seams. Here the
[marked seam theorem](research_marked_pants_seam_isotopy.md)
and the original annular gluing keep the actual unfilled
belt's primitive curves.

Thus a continued-fraction or Conway normal form is not
automatically a decomposition into rigid ideal pants.
It can change a four-punctured boundary, whose representation
still has nontrivial parameters. The exact collar test above
is one way to obtain a valid reduction without making that
geometric assumption. When it fails, neither geometric
volume additivity nor a nonzero quantum contribution has
been proved by merely drawing additional decomposition cuts.

## 7. Exact reproduction

The rational-arithmetic checker evaluates the full affine
maps, including their half-lattice translations:

    python3 experiments/check_rational_corridor_compression.py \
      --output repro/results/research-rational-corridor-compression.json

Its default run checks all 2,800 words of lengths one through
four and powers between \(-3\) and \(3\), every successful
deck-sign choice, and the pendant stabilizer calculations.
It also records the displayed mixed and same-sign examples.
The [saved output](../repro/results/research-rational-corridor-compression.json)
contains the script hash. These finite checks confirm the
conventions and arithmetic. The matrix factorization and
supported-collar proof establish the propositions for
arbitrary finite words.

A further [run through length five](../repro/results/research-rational-corridor-compression-root.json)
checks 19,607 words in the same power range. It verifies 11,136
successful deck-sign factorizations, 463 forms with \(c=0\),
and 6,172 pendant reductions. This is still a check of the exact
affine identities, not an asymptotic or hyperbolicity test.
