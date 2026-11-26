# Marked Seifert leaf absorption after short fillings

Private written proof, 19 November 2026.

A supplied planar Seifert piece with one retained boundary has an
elementary absorption test. Nonfiber fillings leave either a solid
torus with a computable primitive meridian, or a boundary-injective
piece whose infinite central fiber obstructs a hyperbolic result
after boundary-injective gluing. The test works with any number of
incoming fillings and retains their actual peripheral bases.

This is an application and explicit marked form of standard Seifert
filling facts, not a new classification. It concerns supplied marked
pieces, not recognition of arbitrary short descendants of a strict
template. The required conclusions and slope formulas are proved
directly below. No new volume-conjecture class is asserted.

## 1. Marked input and nonfiber fillings

Let \(\Sigma\) be an oriented sphere with finitely many open disks
removed, with one boundary circle labelled \(0\). Start with
\(\Sigma\times S^1\). On each boundary torus choose the product
section \(\mu_i\) and the common oriented fiber \(h\). The boundary
circles carry their induced base orientations, so
\[
                    \mu_0+\sum_{i>0}\mu_i=0
                    \quad\text{in }H_1(\Sigma\times S^1).
\tag{1}
\]
Slopes are unoriented primitive classes; their displayed vectors are
therefore determined up to simultaneous sign. All subsequent changes
of section and all boundary gluing matrices are recorded.

Some boundaries may already have been filled by specified primitive
slopes \(\alpha_i\mu_i+\beta_i h\), with \(\alpha_i\ge2\). These
are the supplied exceptional fibers of the initial Seifert piece.
For an initially presented manifold, a fibered homeomorphism to this
marked construction is part of the input, not a conclusion.
Fill every other boundary except \(0\) by a primitive slope
\[
                         a_i\mu_i+b_i h.
\tag{2}
\]
The theorem assumes \(a_i\ne0\). Reverse the representative if
necessary so \(a_i>0\). Its distance from the fiber is exactly
\(a_i\). Distance one is a regular filling; distance at least two
is a genuine exceptional filling. A fiber filling \(a_i=0\) is a
separate stopping stratum, not a limiting case of this theorem.

After collecting the regular fillings, write their slopes as
\(\mu_i+p_i h\), and put \(P=\sum_i p_i\). Let the remaining
genuine exceptional slopes, including the initial ones, be
\((\alpha_j,\beta_j)\), \(1\le j\le q\). Thus \(q\) counts
exceptional fibers, not the quantum level.

The claim that (2) has exactly this fiber multiplicity can be checked
inside an explicit solid torus. Choose integers \(s,t\) satisfying
\(a_i t+b_i s=1\). On \(D^2\times S^1\) use the circle action
\[
        (z,w)\longmapsto(e^{is\theta}z,e^{ia_i\theta}w).
\tag{3}
\]
In a meridian-longitude basis \((m,l)\), identify
\(h=s m+a_i l\) and \(\mu_i=t m-b_i l\). Then
\(a_i\mu_i+b_i h=m\). The action is free off the core and has
core stabilizer of order \(a_i\), since \(\gcd(s,a_i)=1\).
It therefore extends the given boundary fibers across the filling.
Orient the filling torus so the actual boundary attachment is
orientation reversing; the slope calculation uses the displayed
marked bases. For \(a_i=1\), (3) has no exceptional core.

## 2. Absorption and the exact outgoing meridian

**Theorem 1.** For the data above, if \(q\le1\), the filled piece
is a solid torus. Its primitive meridian on the retained boundary is
\[
 \begin{array}{ll}
       \mu_0-P h, &q=0,\\[1mm]
       \alpha\mu_0-(\alpha P+\beta)h,
             &q=1\text{ with exceptional slope }(\alpha,\beta).
 \end{array}
\tag{4}
\]
If \(q\ge2\), its retained boundary is \(\pi_1\)-injective and
the piece is not a solid torus.

First prove the topological assertion for \(q\le1\), rather than
inferring it from (4). There is a map \(g:\Sigma\to S^1\) with
boundary degrees \(p_i\) on the regular filling circles, zero on
the exceptional ones, and \(-P\) on circle \(0\). To construct it,
retract the planar surface onto a graph, assign the prescribed
integer degrees to its inner boundary generators, and extend along
the graph. The outer degree is their negative sum. The fibered
homeomorphism \((z,w)\mapsto(z,g(z)w)\) changes the sections to
\(\mu_i+p_i h\) on regular circles and \(\mu_0-P h\) on the
retained circle, leaving the exceptional sections unchanged.
In these coordinates the regular fillings are literal product disk
caps. Fill them first; their boundary winding changes have been
retained rather than reset.

For \(q=0\), the remaining base is a disk, so the filled piece is
\(D^2\times S^1\). For \(q=1\), leave its exceptional filling
until last. The remaining piece is an annulus times \(S^1\), hence
a torus collar. Attaching the specified solid torus to its inner
boundary yields that same solid torus with an outer collar. This
proves the asserted homeomorphism in both cases independently of
homology.

Now compute the marking. A regular filling gives
\(\mu_i=-p_i h\). In the case \(q=0\), (1) gives
\(\mu_0=P h\). In the case \(q=1\), its exceptional section is
\(\mu_e=-\mu_0+P h\), so
\(\alpha\mu_e+\beta h=0\) gives the second vector in (4).
These vectors are primitive: in the second case
\(\gcd(\alpha,\alpha P+\beta)=\gcd(\alpha,\beta)=1\).
For a solid torus, the primitive kernel of its boundary map on
first homology is its meridian. Thus the established topology and
this calculation together prove (4). The nonabsorption assertion
is proved next.

In particular, with no initial exceptional fiber, every collection
of slopes \(\mu_i+p_i h\) absorbs, however large or differently
signed the \(p_i\) are. Its outgoing slope depends only on their
sum. With one initial exceptional fiber the same assertion holds
with the second formula of (4). No boundedness of the original
individual fillings follows from boundedness of that sum.

## 3. Boundary injection and an elementary hyperbolicity obstruction

For \(q\ge2\), van Kampen applied to the product piece and the
specified fillings gives
\[
 \pi_1(Y)=\left\langle h,x_1,\ldots,x_q\ \middle|\
 [h,x_j]=1,\ x_j^{\alpha_j}h^{\beta_j}=1\right\rangle,
 \qquad
 \mu_0=(x_1\cdots x_q)^{-1}h^P.
\tag{5}
\]
Choose disjoint base arcs and the boundary order giving this standard
planar presentation. The proof uses that recorded choice.

The fiber has infinite order. Indeed the assignment to the additive
group \(\mathbb Q\)
\[
                         h\longmapsto1,
             \qquad x_j\longmapsto-\beta_j/\alpha_j
\tag{6}
\]
respects every relation. On quotienting by \(h\), (5) becomes
\[
                    C_{\alpha_1}*\cdots*C_{\alpha_q}.
\tag{7}
\]
The word \(\bar x_1\cdots\bar x_q\) is cyclically reduced:
its first and last letters belong to different factors and every
letter is nonidentity. Its positive powers have reduced length
\(q,2q,3q,\ldots\), so it has infinite order. If
\(\mu_0^u h^v=1\), passage to (7) forces \(u=0\), and (6)
then forces \(v=0\). The boundary group generated by \(\mu_0,h\)
is therefore an injected \(\mathbb Z^2\). This completes Theorem 1.

There is also an obstruction to a hyperbolic final exterior which
does not require recognizing this torus as a JSJ torus.

**Theorem 2.** Glue this \(q\ge2\) piece to a connected rest
\(X\) along its retained torus. If the attaching torus also injects
into \(\pi_1(X)\), the resulting manifold cannot admit a complete
finite-volume hyperbolic structure.

Both boundary injections make the van Kampen amalgam an amalgam
of injected groups. The reduced alternating-word construction of an
amalgam gives injections of both vertex groups: choose coset
representatives for the common subgroup, successively combine
adjacent letters in the same factor, and a reduced word containing
a nontrivial factor representative cannot become the identity.
Thus \(\pi_1(Y)\) embeds in the resulting group. It is nonabelian,
since (7) is nonabelian, and all its elements commute with its
nontrivial infinite central element \(h\).

In a torsion-free discrete subgroup of \(\mathrm{PSL}_2(\mathbb C)\),
the centralizer of a nontrivial element is abelian. Here is the
elementary check. There is no nontrivial elliptic element: finite
order contradicts torsion freeness, and powers of an infinite-order
elliptic accumulate at the identity. A nontrivial element is thus
parabolic or loxodromic. Conjugate a parabolic to \(z\mapsto z+1\);
commutation forces every centralizing map to be a translation.
For a loxodromic, a commuting map preserves its two fixed points
individually, so all centralizing maps are diagonal in that basis.
Both centralizers are abelian. This contradicts the embedded group
from (5), proving Theorem 2.

Boundary injectivity of the rest is essential. It must be checked
after its own specified fillings, not inferred from an earlier
unfilled decomposition. The theorem makes no assertion on a branch
where that boundary becomes compressible.

## 4. What independently long coordinate slopes do

Suppose an incoming filling is written in its actual peripheral
basis as \(\gamma_i(n_i)=m_i+n_i\ell_i\), with
\(|\det(m_i,\ell_i)|=1\). Its oriented fiber distance is
\[
       \det(\gamma_i(n_i),h)
          =\det(m_i,h)+n_i\det(\ell_i,h).
\tag{8}
\]
If \(\ell_i=\pm h\), the absolute distance is identically one.
Otherwise it tends to infinity with \(|n_i|\). Conversely,
\(\det(\ell_i,h)=0\) implies \(\ell_i=\pm h\), because both
classes are primitive. Thus there is no unexplained constant
distance greater than one in an actual integral peripheral basis.

More explicitly, write the primitive fiber in the actual basis as
\(h=r_i m_i+s_i\ell_i\). The distance in (8) is
\(|s_i-r_i n_i|\). If \(r_i=0\), primitivity forces
\(|s_i|=1\), so every integer value of this coordinate is a regular
filling. If \(r_i\ne0\), the distance is at least two for all
sufficiently large \(|n_i|\).

First perform the fixed nonfiber fillings, and let \(q_{\rm fixed}\)
count their genuine exceptional fibers together with the initial
ones. If a fixed slope is a fiber, the present rule stops instead.
For independently long values of the remaining coordinates, the
number of genuine exceptional fibers is exactly
\[
 q_\infty=q_{\rm fixed}
       +\#\{i:r_i\ne0\}.
\tag{8a}
\]
Thus \(q_\infty\le1\) gives solid-torus absorption by (4)
throughout a cofinal coordinate region. If \(q_\infty\ge2\),
Theorem 1 gives a boundary-injective piece there; whenever the
rest's attaching boundary is also injective after its fillings,
Theorem 2 excludes hyperbolic final exteriors. Fiber-parallel free
coordinates contribute no exceptional fiber, however long they
are. The finitely many exceptional coordinate values where a
transverse filling is a fiber or regular remain separate strata;
their assignment fibers need not be finite. None is discarded.

## 5. A marked forest procedure and its stopping conditions

Suppose a finite rooted forest of pieces is supplied, together with
each planar Seifert presentation and every integral torus gluing
matrix. Each node has one outgoing torus; its other boundary tori
are incoming fillings or child attachments. This additional input
is not asserted to arise from every strict-template short filling.

Process a node only after all its children have actually become
solid tori. A child's primitive meridian vector is transported by
its specified unimodular gluing matrix into the parent's section-
fiber basis. It is still primitive. Apply the following finite rules:

1. If an incoming slope is a fiber, stop on that branch and retain
   the exact slope. No claim about that filling's prime factors or
   its quantum source is made by the present rule.
2. Otherwise count the genuine exceptional fibers. If there are at
   most one, replace the filled node by its solid torus and pass
   the exact vector (4) to its parent.
3. If there are at least two, retain the boundary-injective piece.
   Theorem 2 excludes a hyperbolic result only when the rest's
   attaching boundary is also known to inject.

A node with a child not proved to be a solid torus is not processed
by these rules. Each absorption removes a node, so the procedure
terminates. It is a postorder calculation on the supplied forest,
not a general JSJ algorithm or a classification of fiber fillings.

The coordinate calculation uses primitive integral pairs and their
actual gluing matrices. In rational slope coordinates it gives the
usual fractional-linear substitutions and, where nonsingular,
plumbing-style eliminations. Every zero denominator, section change
and sign remains recorded. A homological Schur complement cannot
replace the topological absorption test.

For example, take two exceptional fibers with coprime orders
\(\alpha,\gamma\ge2\), and primitive pairs \((\alpha,\beta)\),
\((\gamma,\delta)\), with no regular fillings. Abelianizing (5)
gives a rank-one torsion-free group: the relation matrix's maximal
minors are \(\alpha\gamma,\alpha\delta,\gamma\beta\), whose gcd
is one. Its boundary homology kernel is generated by the primitive
vector
\[
              \alpha\gamma\mu_0-(\gamma\beta+\alpha\delta)h.
\tag{9}
\]
Nevertheless Theorem 1 proves that its boundary fundamental group
injects and that it is not a solid torus. This entire family has
the homological appearance needed for a rational outgoing slope
without the disk needed for absorption.

## 6. The original source and the unresolved core obligation

Absorption identifies a filled piece with a solid torus with a
specified meridian. A boundary homeomorphism between solid tori
extends across them when it sends meridian to meridian: isotope
it to match a meridian circle, extend across a meridian disk, cut
along that disk, and extend over the resulting ball by radial
coning. Hence the replacement can be made with the prescribed
retained boundary attachment, leaving the rest unchanged.

If that relative replacement identifies the same final oriented
knot, marked cut and zero framing, its original normalized
Kashaev invariant is equal at every level \(N\). If instead one
keeps a diagram framing, its actual twist scalar must be retained
before passing to zero framing. Equality is asserted only with
this identification of the actual final marked knot; a calculation
of slopes or first homology alone is not such an identification.
Nor is an equality of open quantum kernels in arbitrary boundary
frames asserted here. No JSJ-volume conjecture or cabling-growth
principle is used.

The source normalization and the obligation to retain original
assignment fibers are those of the complete direct A below.
Already \(q=0\) in (4) can leave a fixed outgoing slope while
\(p_1\to+\infty\) and \(p_2\to-\infty\). The reduction then
preserves the same core rather than proving its volume limit.
An unresolved hyperbolic core with an infinite original fiber
cannot be counted as finitely many exceptional assignments.

What remains for a universal strict-template reduction is substantial:
recognize the pieces and their fiber/peripheral markings after an
arbitrary fixed short partial filling; handle fiber fillings and
boundary-compressible rest; identify all resulting marked cores;
and prove the original-source lower bound for every core whose
assignment fiber requires it. The supplied-piece theorem proves
none of those recognition or analytic assertions. It gives a
general exact absorption-or-obstruction rule where its marked
topological input is available, with no knot-by-knot catalogue.

## Complete direct and coverage

* A: notes/research_affine_reduction_fibers_and_core_obligation.md,
  845 lines, SHA256
  1af02b1250cee23a1d144cd4e04b67e4ed749afbb9029248f7df142b5f395313.

A supplies the original-assignment, marking and core-obligation
scope; the product-piece filling, fundamental-group, slope and
forest arguments are proved here. Circle bundles over planar
surfaces, Seifert multiplicities and rational peripheral elimination
are standard constructions, with no novelty claimed for their
general principles. For coverage, Hatcher's official contents page
for [Notes on Basic 3-Manifold Topology](https://pi.math.cornell.edu/~hatcher/3M/3Mdownloads.html)
lists Seifert manifolds in Chapter 2 and torus decomposition in
Chapter 1. Only that contents page was checked for this reference;
no external proof is imported. Only written
mathematics and text/hash operations were used. Frozen notes,
public manuscripts, mathematical programs, tests and builds were
not changed or run.
