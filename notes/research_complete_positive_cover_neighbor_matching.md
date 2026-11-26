# Complete positive covers with no initial cancellation loops

Private research note, 17 November 2026.

Every finite complete positive geometric ideal triangulation has a
finite normal cover in which all signed local opposite-pair differences
are distinct. At every level \(N\ge3\), the immediate neighbor graph
of one zero joint-character block is therefore a disjoint matching.
It contains neither a scalar holonomy loop nor two loops whose boundary
operators could have a nontrivial commutator.

This gives a structural limitation of the initial-loop argument.
The cover need not be a knot exterior in \(S^3\); no quantum invariant
or pointed state is identified between the cover and its base.
Higher-order propagation using several zero blocks is not addressed.

## 1. Incidence and the exact initial graph

Let \(\mathcal T\) be a finite geometric ideal triangulation of a
connected oriented complete finite-volume hyperbolic three-manifold
\(M\) with torus cusps. The tetrahedra are positively oriented convex
ideal tetrahedra, and their lifted interiors in \(\mathbb H^3\) are
disjoint. Write \(\Gamma=\pi_1(M)\) for the deck group.

For a tetrahedron \(t\), let \(a_t,b_t,c_t\) be the multiplicity
vectors of its global edge labels in the opposite pairs
\((01,23),(02,13),(03,12)\). The original edge shifts are the
integer functionals
\[
 \alpha_t=c_t-b_t,\qquad \beta_t=c_t-a_t.
 \tag{1}
\]
Here the vectors mean evaluation on the genuine edge rows. These rows
generate the integral edge lattice \(E\), so equality of these
functionals is tested on all the global edges.

The six signed offsets at \(t\) are
\[
 \mathcal S_t=
 \{\alpha_t,-\alpha_t,\beta_t,-\beta_t,
                \alpha_t-\beta_t,\beta_t-\alpha_t\}.
 \tag{2}
\]
Their indexing by tetrahedron, opposite-pair difference, and sign is
retained, even before proving that their values are distinct.

For clarity, the graph under consideration is an exact source graph.
Normalize an integral basis of commuting edge operators as
\(U_i^N=1\), with all original Weyl and compatible root units retained,
and put \(v_\chi=\Pi_\chi p\), where \(p=\bigotimes_t p_t\) is the
original pointed tensor. Some projectors may have zero rank if the
edge lattice is nonprimitive; no assertion about their ranks is needed
here. Suppose \(v_\chi=0\), and abbreviate
\(v(\delta)=v_{\chi+\delta}\). The original equation
\((X_t+Y_t-1)p=0\) gives
\[
 \begin{split}
 v(-\alpha_t)&=-X_t^{-1}Y_t\,v(-\beta_t),\\
 v(\alpha_t)&=Y_t\,v(\alpha_t-\beta_t),\\
 v(\beta_t)&=X_t\,v(\beta_t-\alpha_t).
 \end{split}
 \tag{3}
\]
The last two equations are the original block equation at
\(\chi+\alpha_t\) and \(\chi+\beta_t\). All three operators in (3)
are invertible.

The initial neighbor graph has the offsets (2), reduced in
\(\operatorname{Hom}(E,\mathbb Z/N)\), as vertices. Its three edges
per tetrahedron are the pairs in (3), with those literal transports.
No further relations or inferred zero blocks are inserted into this
definition.

**Theorem.** There is a connected finite normal cover
\(\widehat M\to M\), carrying the lifted complete positive triangulation,
such that:

1. The six local edges of each lifted tetrahedron have distinct global
   edge labels in \(\widehat M\).
2. The complete indexed collection of offsets (2), over all
   tetrahedra of \(\widehat M\), consists of distinct nonzero integer
   functionals.
3. These offsets remain distinct and nonzero modulo every \(N\ge3\).
   Consequently the graph (3) is a disjoint union of
   \(3\widehat T\) single edges, where \(\widehat T\) is the number of
   tetrahedra in the cover.

The proof uses the actual incidence lattice. It makes no integral
change of polarization and no replacement of the pointed tensor.

## 2. Finite separation for the complete deck group

We include the needed linear-group argument rather than import a
residual-finiteness theorem.

**Finite-ring lemma.** If \(R\subset\mathbb C\) is a finitely generated
ring over \(\mathbb Z\) and \(0\ne f\in R\), there is a homomorphism
from \(R\) to a finite field in which \(f\) is nonzero.

**Proof.** The nonzero ring \(S=R[1/f]\) has a maximal ideal.
Its quotient \(K\) is a field finitely generated as a ring over
\(\mathbb Z\). Such a field is finite, as follows.

First recall the elementary field lemma: a field generated as an
algebra by finitely many elements over a field \(k\) is a finite
algebraic extension of \(k\). Choose a maximal algebraically
independent subset \(x_1,\ldots,x_r\) of the generators. After inverting
one nonzero polynomial \(g\in k[x_1,\ldots,x_r]\), the remaining
generators are integral over \(B=k[x_1,\ldots,x_r,1/g]\).
Since the generated algebra is a field, it already contains \(1/g\);
it is therefore an integral extension of \(B\).
If an integral extension of a domain is a field, the domain is a
field: the monic equation for \(b^{-1}\), multiplied by \(b^{n-1}\),
puts \(b^{-1}\) in the domain for every \(b\ne0\).
If \(r>0\), an irreducible polynomial in \(k[x_1]\) not dividing
\(g\) is not a unit in \(B\), a contradiction. Such a polynomial
exists by the usual Euclidean proof that \(k[x_1]\) has infinitely
many irreducibles. Thus \(r=0\), proving the field lemma.

If \(K\) has characteristic \(p>0\), that lemma applied over
\(\mathbb F_p\) makes \(K\) finite. If its characteristic were zero,
the same lemma over \(\mathbb Q\) would make its finitely many ring
generators algebraic over \(\mathbb Q\). Choose a positive integer
\(D\) clearing the coefficients of their monic equations. They are
integral over \(\mathbb Z[1/D]\), and \(K\), being a field, already
contains \(1/D\). Hence \(K\) is integral over \(\mathbb Z[1/D]\),
which would make this latter ring a field. A prime not dividing \(D\)
contradicts that conclusion. Therefore \(K\) is finite. Since \(f\)
is a unit in \(S\), its image is nonzero. \(\square\)

Now let a finitely generated subgroup \(\Gamma\subset
\mathrm{GL}_d(\mathbb C)\) and a finite set
\(\mathcal F\subset\Gamma\setminus\{1\}\) be given. Form the ring
generated by the entries of finite group generators and their inverse
matrices. For each \(g\in\mathcal F\), select a nonzero entry of
\(g-I\), and let \(f\) be their product. Applying the lemma and reducing
all matrices gives a homomorphism to a finite general linear group
that separates every \(g\in\mathcal F\) from the identity. The inverse
matrices were included, so invertibility survives reduction. Its kernel
is a finite-index normal subgroup avoiding \(\mathcal F\).

The complete deck group has exactly these properties. It is finitely
generated because the truncated finite triangulation is a finite
compact core. The faithful complete holonomy embeds it in
\(\mathrm{PSL}_2(\mathbb C)\), whose adjoint action on the
three-dimensional space of traceless matrices is faithful. Indeed a
determinant-one matrix commuting with every traceless matrix is scalar
and hence represents the identity in \(\mathrm{PSL}_2\).
This supplies the required faithful finite-dimensional linear
representation without choosing a global \(\mathrm{SL}_2\) lift.

## 3. One bounded dual neighborhood controls all edge coincidences

Let \(\widetilde{\mathcal T}\) be the universal geometric triangulation,
and use face adjacency for its dual graph. Let \(D\) be the maximum
edge valence in the finite triangulation. Around every lifted edge,
its incident tetrahedra form the finite cyclic edge star; any two of
them have dual distance at most \(D\). The same is true in every
cover. The dual graph is locally finite.

The deck group acts freely on its tetrahedra. An element stabilizing a
geometric tetrahedron permutes its four ideal vertices; a power fixes
all four and is therefore the identity. Torsion-freeness of the
manifold deck group then makes the original element the identity.

Choose one lifted tetrahedron \(\tau_i\) from each base tetrahedron.
For the finite dual ball \(B_{2D}(\tau_i)\), let \(\mathcal F_i\)
consist of all nonidentity deck elements that carry some tetrahedron
in this ball to another tetrahedron in the same ball. This is a
finite set: the ball has finitely many vertices and the action on
tetrahedra is free. Apply Section 2 to
\(\mathcal F=\bigcup_i\mathcal F_i\), obtaining a finite-index normal
subgroup \(H\) disjoint from it.

In the corresponding finite normal cover, every ball
\(B_{2D}(\tau)\) injects on its tetrahedra. For the chosen
representatives this is the construction. For an arbitrary translate
\(g\tau_i\), any alleged identification conjugates to an element of
\(H\cap\mathcal F_i\), using normality of \(H\).

This vertex injectivity also controls edge labels, without assuming
that a whole truncated cusp neighborhood embeds.
If two distinct edges \(e_1,e_2\) of a tetrahedron \(\tau\) acquired
the same edge label in the cover, there would be \(h\in H\) with
\(he_1=e_2\). Then \(h\tau\) and \(\tau\) both meet \(e_2\), so
\(h\tau\in B_D(\tau)\). Ball injectivity gives \(h\tau=\tau\),
and freeness gives \(h=1\), contradicting \(e_1\ne e_2\).
Thus all six local edges in the cover have distinct labels.

## 4. Four supporting edges determine the tetrahedron

Suppose two indexed integer offsets in (2), at cover tetrahedra
\(\bar\tau,\bar\sigma\), agree. Each has four distinct supporting
global edges, with two coefficients \(+1\) and two coefficients
\(-1\). Their supporting four-edge sets therefore agree.

Choose a lift \(\tau\) of the first tetrahedron. Using one common
support label, choose a lift \(\sigma\) of the second tetrahedron
so that one of its support edges is the same actual lifted edge as a
support edge of \(\tau\). Such a choice is possible precisely because
the edge labels agree in the cover. Both tetrahedra meet this edge,
so \(\sigma\in B_D(\tau)\).

For every other support edge \(e\) of \(\tau\), let \(f\) be the edge
of \(\sigma\) with the same label in the cover. There is \(h_e\in H\)
with \(h_e f=e\). The tetrahedron \(h_e\sigma\) meets \(e\), as does
\(\tau\), so \(h_e\sigma\in B_D(\tau)\). Both \(\sigma\) and
\(h_e\sigma\) lie in the same injective ball. Hence
\(h_e\sigma=\sigma\), and freeness gives \(h_e=1\).
All four support edges thus agree as actual edges in
\(\widetilde{\mathcal T}\), not only as quotient labels.

The union of two opposite edge pairs in an ideal tetrahedron is a
four-cycle containing its four vertices. The shared four actual edges
therefore determine the same four ideal vertices for \(\tau\) and
\(\sigma\). Their convex hull is the same geometric ideal tetrahedron.
Distinct tetrahedra of the universal geometric triangulation have
disjoint interiors, so \(\tau=\sigma\).

Within this tetrahedron, the three unsigned opposite-pair differences
have different four-edge supports. Their negatives have opposite
nonzero coefficients. Thus all six indexed offsets are distinct, and
the alleged equality was the same indexed offset. This proves
assertion 2 of the theorem as well as the asserted nonvanishing.

Finally every entry of each offset, evaluated on a genuine edge row,
is in \(\{-1,0,1\}\). The difference of two offsets has entries in
\([-2,2]\). At \(N\ge3\), congruence on all edge rows is therefore
integer equality. Since these rows generate \(E\), this proves
assertion 3. Each tetrahedron contributes exactly three disjoint pairs
in (3); no vertex is shared with another tetrahedron. The initial
neighbor graph is consequently a disjoint matching. \(\square\)

## 5. Exact scope

The proof supplies finite connected complete positive geometric covers,
not a classification of all triangulations or a claim that every
original triangulation has this property. It uses no knot list.
The cover may have several cusps, need not be an \(S^3\) link exterior,
and need not have a primitive edge lattice. The congruence argument
uses its genuine edge rows directly, so none of these qualifications
changes the matching conclusion.

The conclusion concerns only the graph generated immediately from one
zero block by (3). It rules out a universal proof based on initial
transport cycles, including an argument that two such cycles must
realize noncommuting peripheral directions. Further zeros, longer
source relations, or a different source-preserving construction may
produce additional vertices and relations; they are not ruled out.

No transfer of a quantum invariant, prescribed character, or selected
vector between \(M\) and its cover is made. In particular, the result
neither proves nor disproves joint pointed nonvanishing for the
original knot source.

## Direct sources and coverage

1. [Pointed tetrahedron modules and all-level edge reduction](pointed_tetrahedron_gluing.md),
   SHA256
   \(\texttt{ba91c4be463e38add42b2f8ebc53c3cd3a7e96e97ac4247330dc325e7f6b3a7c}\).
   This fixes the original incidence lattice, Weyl units, local
   equation and commuting edge operators, including nonprimitive
   scope.
2. [Joint pointed nonvanishing by character-subgroup propagation](research_joint_edge_character_bootstrap.md),
   SHA256
   \(\texttt{09f8f96a582e15488e8758c33ce4693da7937c438fde5e72b935262916c9e9ca}\).
   This fixes the exact block equation and the shift evaluations
   used in (1)--(3).

Both complete source texts were read at these matching pins.
The finite-ring argument is the standard elementary proof of residual
finiteness for finitely generated linear groups, supplied in full here.
The bounded edge-star and geometric four-cycle arguments are also
proved above. No normal-surface realization, cover comparison of
quantum states, mathematical program, or numerical test is used.
