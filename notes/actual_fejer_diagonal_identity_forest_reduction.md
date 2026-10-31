# Diagonal Fejer ports reduce to a true identity smoothing

31 October 2026. diagonal and identity-forest reduction. This keeps the original
protected targets and all remaining cross/left/right data. It does not
factor arbitrary Green ports across matching/matching digon cuts.

## 1. Polynomial cost and the fixed-label distinction

At N=2m,d=N-1 the FULL diagonal part of the positive endpoint numerator
is exactly

  P_diag(b,c)=sum_(i=0)^d (4/a_i)b^i c^(d-i),
  a_i=4cos^2(pi(i+1/2)/N).

Thus coefficientwise

  H_1<=P_diag<=C N^2 H_1,
  H_1=sum_(i=0)^d b^i c^(d-i).                         (1)

Here C is absolute. The root at the half-integer sample closest to
N/2 gives min a_i=4sin^2(pi/(2N)), so (1) is immediate.
A fixed LEFT or RIGHT diagonal label includes only its corresponding
half of the i range. For such a label retain ONLY the upper bound
by C N^2 H_1. Equality of exponential rates with the full identity
kernel is asserted only after summing BOTH actual diagonal types.
At fixed diagram size the product cost remains polynomial.

At the limiting entropy level a diagonal port has exactly

  q=(0,mu,1-mu,0), E=0,

or its actual reflection. Enlarging its two possible half ranges to
all identity loads sigma_b,sigma_c>=0, sigma_b+sigma_c=1 is therefore
valid for an upper-bound reduction, without any phase or entropy cost.
No remaining one-sided port is changed.

## 2. Feasibility forces the diagonal middle graph to be a forest

Take any selected set D of diagonal ports in a feasible limiting
source flow. Its middle b-c edges lie in the original gap graph.
The only possible cycles are the entire internal even-gap cycles,
each containing the protected exterior vertex u. If a component has
n vertices and at least n edges, its identity edge loads already sum
to at least n. Its vertices have total target at most n-1, since it
contains u; all remaining local loads are nonnegative. This is
impossible. Hence the diagonal middle graph is a forest, and its
literal identity smoothing is connected. A tree cannot contain two protected vertices either: its n-1 edge
loads would exceed the at most n-2 available targets. Thus each tree
has at most ONE protected vertex directly from the load count.

For a tree with n vertices the sum of its internal edge loads is n-1.
The total remaining load is therefore1 when all its vertices are
ordinary, and0 when it contains a protected vertex. Collapse that
actual tree to one face of the same ordinary/protected type. Push
all remaining local incidences to their resulting face label.
Every remaining port retains its own local exponent vector and E.

Conversely, for any nonnegative remaining loads with the collapsed
face target, the lift of the identity loads is UNIQUE. Root a tree
at its protected vertex if present, otherwise anywhere. At an edge
parent->child let L be the total remaining load in the child subtree.
Then assign

  sigma_child=1-L, sigma_parent=L.                    (2)

Since a subtree load lies in[0,1] (or is zero in a protected tree),
these are valid identity loads. Summing the subtree balances proves
(2), and subtracting them proves every original face equation.
No local E or entropy changes in this transport.

The same is an EXACT finite coefficient identity. For an arbitrary
remaining polynomial with nonnegative exponents, a surviving monomial
has total degree d on each ordinary merged tree and0 on a protected
tree. At an internal edge its endpoint identity degrees are

  j_child=d-L_degree(subtree), j_parent=L_degree(subtree).

Both lie in[0,d]. Each H_1 coefficient is one, so there is no counting
multiplicity. Consequently extracting the original target after
inserting all H_1 factors equals extracting the ordinary d targets
of the polynomial obtained by IDENTIFYING the face variables in each
tree. This is the actual source-preserving identity smoothing,
not a formal zero-radius substitution. Combined with (1), it bounds
any fixed diagonal sector by the true smoothed remaining positive
source with polynomial cost.

## 3. Two useful exclusions after deleting ALL diagonal ports

Suppose D contains every diagonal port of the particular limiting
flow. The resulting white triangular cellulation has NO loop edge.
To prove this, choose the mark-free side of a proposed loop at a.
If it contains v interior white vertices, Euler counting gives
2v-1 shaded triangles inside. The dual bridge must be MATCHING:
the odd number of dual vertices and one matching incidence per
vertex force its single crossing edge to be matching. There are
v-1 whole retained ports inside and one inside triangle of that
bridge port. Its middle is inside; both outer incidences are at a.
The v ordinary interior targets sum to v. The whole ports supply
at most v-1 there, so the bridge middle must carry the FULL unit,
and every other incidence of that port must be zero. It is therefore
a diagonal endpoint, contrary to its retention.

Likewise no remaining MATCHING edge joins the two protected merged
faces. Both outer loads of that port would be zero. For a one-sided
port this forces nu-mu=0, hence diagonal; for a cross port the two
middle loads would have to be1/2 each, but its actual finite cross
support needs one outer unit. At the limiting functional this is the
same full-diagonal load (1/2,1/2), with zero entropy. It can be included in D ONLY for the LIMITING entropy/load reduction:
its zero entropy and identity load are the same. This does NOT apply
the finite comparison (1) to that cross sector, which still needs its
one outer unit. The separate [full-kernel entropy theorem](actual_fejer_full_kernel_entropy_identity_reduction.md)
supplies the source RATE comparison for these limiting endpoints. The
finite inequality in section1 is still not applied to a cross sector.
The combinatorial no-protected-matching conclusion therefore concerns
the enlarged LIMITING identity reduction when those cross endpoints
are included.

The remaining cellulation may have parallel edges and degree-two
faces. Those are not excluded by this count and must not be replaced
by a simple graph without retaining the actual topology.

## 4. What decomposes and what still does not

A MAIN/MAIN two-edge cut leaves complete ports on each side. On its
mark-free side, the number of internal ordinary targets equals the
number of contained ports. Total-degree conservation then forces
ALL incidences on its two boundary faces to have zero load. Thus this
cut has the same zero-boundary separation as the complete-source
angle proof; absolute local entropy constants are unchanged.

A MATCHING/MATCHING cut is different. Two retained Green ports can
cross it. Let ell>=0 be the total load that the v-1 whole inside ports send to
the two boundary faces. The exact balance is

  q_inside,1+q_inside,2=1+ell.

A cross middle is at most1/2, so in the old complete proof this forced
ell=0 and both inside middles to equal1/2. General Green ports may
have asymmetric middle loads and may also have ell>0. Therefore the
old independent block capacity factorization does NOT extend by the
same argument.
This is an explicit remaining coupling, not a scalar normalization
issue or a reason to alter the original support.

A possible way around it is a DIRECT signed developing disk on the
loopless triangular cellulation with parallel edges. Its vertex
links are still topological circles/intervals, so the signed center
holonomy argument should not require simpliciality. Repeated edges
then develop to the same circle contact, which the global oriented
chain permits. This still requires proving the correct treatment of
structurally forced zero degrees and any escaping ordinary multipliers.
The original representation must be restored by actual identity
meridians at the deleted ports. If their outer product becomes
nonparabolic, its recorded flag and the proved zero-volume filling
cap must be used; an artificial x/y tangency must NOT be inserted.

The exact reductions above do not yet show that the reduced mixed-E
maximum is attained on the regular signed-development stratum, nor
bound the remaining coupled matching cuts. No general diagonal-boundary
volume inequality is asserted.

The full-kernel companion gives the rate-level CROSS-seam reduction. No independent Green-block factorization across matching cuts is asserted.