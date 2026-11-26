# The geometric framing orbit cannot enter the one-cut acute source

Private written deduction, 15 November 2026. No mathematical code,
numerical calculation, test, or saved numerical evidence is used.
Frozen notes and public manuscripts are unchanged.

For the original complete-color source of a knot braid, a regular
geometric critical point has two independent framing directions in
the full physical phase coordinates. Fixing one physical cut degree
leaves at least one Hessian null direction. The exact clock extension
preserves that direction. Such a point therefore cannot lie in the
acute incidence domain, whose fixed-cut Hessian is nonsingular.

This is an exclusion of regular full geometric critical points in
the certified chart. It is not an exclusion of minimizing imaginary
heights, and does not use geometric rigidity or the existence of a
positive ideal triangulation.

## 1. The actual full phase and its marked critical chart

Take a fixed signed braid with knot closure and \(c>0\) crossings,
at the original complete color \(M=1\). Retain the original pivots,
framing factor and normalized marked closure. Before fixing the
physical first-head degree, let
\[
             z=(A,U_1,\ldots,U_c)                       \tag{1}
\]
be the scaled physical-flow coordinates. These are independent
coordinates on the full flow space: after the transfers are fixed,
the braid permutation is one cycle, so the closing equations
determine all starting degrees from the first one. Their integral
matrix is a deleted incidence matrix of that cycle, with determinant
\(\pm1\). Equivalently, follow the knot: each crossing adds its
transfer once at an under encounter and subtracts it once at an
over encounter, so the final total change is zero.

Write \(G(z)\) for the full variable-dependent physical action on a
regular logarithmic chart. Its crossing terms are exactly
\(G_\sigma\) in the joint-clock source, equation (27a), composed
with these physical flow forms. The original closure and boundary
terms are retained. Scalar framing constants have no internal
Hessian. At complete color the finite pivots have bounded
logarithm on a compact regular color chart; alternative recorded
logarithmic lifts add linear Fourier characters, not Hessian terms.

The relevant marking is fixed by the actual boundary identity in
the marked-braid source. With \(F_a=(Q;Q)_a\), the exact boundary
vectors are \(\psi_a=F_a^{-1}\) and \(\phi_a=F_a/N\).
The factorial basis makes them the constant vector and normalized
average. The strand frame change multiplies a crossing by
\(F_{\rm out,1}F_{\rm out,2}/(F_{\rm in,1}F_{\rm in,2})\).
These factors cancel on shared wires and on the closed cut, whose
two degrees agree by conservation. The boundary pairing retains
the factor \(1/N\). Thus this passage is a telescoping change of
the actual action and boundary frame, not a different invariant.

Sections 4--6 of that source identify the regular exponentiated
critical scheme with framed augmented knot representations whose
selected meridian eigenflag is \(1\). The identification has
explicit rational inverses: the triangular factorization of partial
meridian products recovers the local physical generators and
momenta. All denominators are units on the stated chart, so the
identification holds infinitesimally as well as on complex points.

There is one marking to check when applying this certificate to
the complete periodic physical source. Its momenta are periodic
at the first head, whereas the constant-vector chart fixes the
first marked momentum to one. On a connected regular knot diagram,
the local generating relations determine all momentum ratios from
the physical positions and transfers. Shared wires propagate the
ratios through the connected diagram. Two momentum lifts of the
same physical-flow point therefore differ by one common nonzero
scalar. Normalize this scalar at the first head to obtain the
marked representative. In the factorial frame the relation is
\(p_{\rm new}=(1-X)p\), where \(X\) is the multiplicative physical
position. This normalization is valid on the regular chart and
does not impose an additional equation on (1).

This is the common-momentum normalization proved at the end of
Section 5 of the joint-clock source. It is necessary here: an
abstract representation orbit, without its faithful lift into
the retained phase variables, would not imply a phase degeneracy.

## 2. Two faithful critical directions, without rigidity

Let \(\rho\) be a non-elementary boundary-parabolic representation
in that regular marked chart. In particular it may be the complete
geometric representation. Its selected peripheral flag is fixed to
\(1\). The group
\[
              B_1=\operatorname{Stab}_{\mathrm{PGL}_2}(1)
                                                                  \tag{2}
\]
has complex dimension two. Conjugating \(\rho\) by a nearby
element of \(B_1\) preserves its knot relations, complete meridian
color and selected flag. Regularity is open, so this construction
stays in the same rational chart near the identity.

This orbit has two independent tangent directions. Indeed a
non-elementary boundary-parabolic representation has three
distinct fixed flags of conjugates of a noncentral parabolic
meridian. A projective transformation centralizing the
representation fixes those three flags and is the identity.
The infinitesimal assertion follows as well: a projective vector
field vanishing at three distinct points is zero. Thus the
infinitesimal stabilizer in \(B_1\) is zero.

The orbit directions remain independent after passing to (1).
For an explicit check, suppose an infinitesimal orbit direction
has zero variation of every physical position and transfer.
The local generating ratios then make the logarithmic momentum
variations equal on the connected diagram. The normalized first
marked momentum fixes this common variation to zero. Hence all
local physical generators, and therefore all reconstructed
meridians, have zero variation. This contradicts faithfulness
of the conjugation orbit unless its tangent is zero.

Choose logarithmic lifts in a sufficiently small connected
neighborhood of the point. Along this two-dimensional orbit,
the exponentiated stationary equations imply
\[
                  \nabla G(z)=2\pi i\,\ell,\qquad
                          \ell\in\mathbb Z^{c+1},       \tag{3}
\]
with \(\ell\) locally constant. Differentiating (3) on the orbit
gives a two-dimensional subspace
\[
             W\subseteq\ker G''(z),\qquad \dim W=2.     \tag{4}
\]
Subtracting the specified linear Fourier character makes (3)
an ordinary critical equation and leaves its Hessian unchanged.
The multiplicative-to-additive coordinate changes are locally
invertible, so they do not destroy these tangent directions.

Only the framing orbit and the explicit critical chart were used.
No smoothness or dimension assertion about the unframed character
germ is needed. Additional character deformations can enlarge the
kernel; they cannot invalidate (4).

## 3. One physical cut cannot remove this degeneracy

Now fix the actual physical degree \(A=A_*\) in (1), and restrict
the action to the remaining transfers. Since \(dA\) has rank at
most one on \(W\),
\[
              \dim(W\cap\ker dA)\ge1.                  \tag{5}
\]
Let \(0\ne v\) belong to this intersection. For every tangent
\(w\) to the fixed-cut affine space,
\[
                         v^{\mathsf T}G''w=0.           \tag{6}
\]
Consequently the Hessian of the restricted physical action is
singular at the restricted full critical point. Its nullity is
at least one.

This restriction is justified independently by the exact complete
cut identity, but no division by its possibly zero scalar is
being made here. The proof concerns a full critical point before
restriction. It does not assert that every critical point of a
fixed-cut action satisfies the omitted \(A\)-equation.

## 4. Exact clock extension preserves the surviving null direction

Keep all clocks \(H_1,\ldots,H_c\) independent. Let
\(\mathscr F(z,H)\) be the full incidence action with the locally
appropriate clock Fourier characters subtracted. The joint-clock
proof gives the actual physical critical scheme after regular
clock elimination, and on common continued branches its reduced
primitive equals \(G\), up to the retained linear character and
constant. These latter terms have no Hessian.

The clock block is diagonal. With \(R_j=H_j-V_j\), its entries are
\[
 D_j=\mathscr F_{H_jH_j}
       =-\frac{\pi\sin\pi U_j}
           {\sin\pi(U_j-R_j)\sin\pi R_j}\ne0.           \tag{7}
\]
All numerator and denominator sine factors are nonzero on the
regular physical/clock chart. In particular they are nonzero
at a prospective acute critical point: its incidence bounds
give \(0<\Re R_j,\Re(U_j-R_j)<1/2\) and \(0<\Re U_j<1\).

Put \(D=\mathscr F_{HH}\). The exact Schur identity is
\[
        G''=\mathscr F_{zz}
                 -\mathscr F_{zH}D^{-1}\mathscr F_{Hz}.  \tag{8}
\]
For any \(v\in\ker G''\), direct block multiplication shows
\[
 \widetilde v=(v,-D^{-1}\mathscr F_{Hz}v)
                           \in\ker\mathscr F''.        \tag{9}
\]
Choose the nonzero \(v\) from (5). Its lift is nonzero, and
its \(A\)-component remains zero. Thus the full incidence
Hessian restricted to \(A=A_*\), in the \(2c\) independent
transfer/clock coordinates, is singular.

On the other hand, the acute-source theorem proves on
\[
      0<\Re n_{ja}<1/2,\qquad
      n_j=(1-U_j-V_j,U_j-H_j+V_j,H_j-V_j,V_j),           \tag{10}
\]
that the Hermitian part of minus that fixed-cut Hessian is
positive definite. Explicitly it is
\[
       \pi L^{\mathsf T}
                  \operatorname{diag}(\Re\cot\pi n_e)L>0,
                                                                  \tag{11}
\]
where \(L\) has full column rank. A matrix with positive
Hermitian part has no nonzero kernel. Equations (9) and
(11) contradict one another.

**Theorem.** In the certified regular complete-color knot-braid
chart, no full critical point associated with a non-elementary
boundary-parabolic representation can have its regular clock
extension in the one-cut acute incidence domain. This holds
for every fixed physical cut value and every retained Fourier
lift. In particular it excludes every regular point of the
complete geometric framing orbit from that domain.

The argument allows a complex cut value: the acute Hessian
theorem still has its real quadratic Hessian after that cut is
fixed. The real-cut hypothesis of the separate imaginary
coercivity theorem is not required here.

## 5. Scope and the next possible reductions

The theorem is unconditional for the regular braid-source chart
identified above. Its linear-algebra argument also applies to a
Morse-source chart once that chart is identified, with its actual
momenta, bend phases and marked boundary, with the same faithful
two-dimensional critical framing orbit. The classical-crossing
note proves the actual local bend canonical relations and their
inverse-meridian identities, so there is local compatibility.
Those group identities alone are not used here as a substitute
for a complete Morse action-and-boundary identification. No
new all-Morse critical-scheme theorem is claimed in this note.

A full geometric critical point cannot be made acute merely by
choosing its one remaining cut degree differently. To remove
this particular degeneracy requires two independent conditions
transverse to the framing orbit in the full physical space;
one cut can provide at most one of them. Imposing a second
slice does not by itself transport the original quantum source,
preserve a selected cycle, or establish an acute geometric chart.
Another possibility is a different domain whose Hessian permits
the retained framing directions.

Finally, this theorem does not contradict minimizing imaginary
height in the separate zonotope criterion. Such a minimizer
sets only the imaginary part of the phase gradient to zero.
It need not be a full critical point or belong to a geometric
representation orbit. The positive volume identity on that
height graph remains valid on its feasible domain; it cannot
be interpreted as direct inclusion of the regular full
geometric point in the one-cut acute chart.

## Direct written source versions

The following entire source notes and their directly used
implications were read. No saved audit or numerical result is
a premise.

| Source | SHA-256 | Direct use |
| --- | --- | --- |
| marked_braid_holonomy.md | eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f | Exact boundary frame, rational inverse critical chart, marked flag and faithful Borel orbit, Sections 1 and 4--7. |
| research_joint_clock_phase_equations.md | 71393aa353909dfa2dd19b078b1d3fccdf8561520aa071b7537e4bbfc50bb867 | Actual physical action, common momentum marking, regular clock scheme and Hessian Schur identities (27a--k). |
| research_original_incidence_acute_tube.md | 17892b7654e7f7668be2fde7743d5adab0bf8e9dc813c29f8114023e740e78f6 | Exact fixed cut, free flow coordinates and nonsingular fixed-cut acute Hessian. |
| research_rivin_classical_crossing_relation.md | edbc5e4c588f4a690f8dad095392aa245b5ed729dfc615267ff9091a3da0485d | The local external/physical/incidence action dictionary and the explicitly limited Morse bend scope in Section 5. |
