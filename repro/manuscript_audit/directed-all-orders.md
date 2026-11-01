# From microscopic coefficients to a geometric recurrence factor

This record concerns Appendix M, read in full at commit
`cfc8a9295dca45562634f6021415d0d80dc5f745`, and the independent
existence argument in [the finite-sum annihilator note](../../notes/finite_sum_annihilator.md).
It separates the analytic expansion, its algebraic consequence, and the
geometric interpretation. None of these implications follows from a
finite number of computed Taylor coefficients.

The review found no defect in the formal implication in M.8; the geometric interpretation is a separate dependency reviewed below. Its
substitution argument has been expanded in the manuscript to give the
coefficient formula and its inverse explicitly. This is a written
mathematical review, not a formal verification of Appendix M. In particular,
the original quantum normalization, contour estimates and geometric
longitude construction remain necessary inputs.

The [source snapshot and dependency record](directed-all-orders-snapshot.json)
identify the versions read and distinguish checked implications from
imported results. An acyclic dependency record alone does not prove its
individual statements.

## What the theorem actually assumes

One ordered circle tree, its knot-producing endpoint pairing, signed
crossing powers and directed certificate are fixed before the level
increases. The exact state is the zero-framed reduced function
\(F_N(M)\), with

\[
 q_N=e^{\pi i/N},\qquad K_N=F_N(1),\qquad
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},\qquad
 Z_N(s)=\frac{F_N(q_N^s)}{K_NH_N(s)}.
\]

The all-order assertion requires an expansion on each fixed compact in
the upper half-plane, including all its finitely many translates needed
by an operator. On those compacts, and on the original disk, it asserts

\[
 \log Z_N(s)=\sum_{r=1}^L N^{-r}p_r(s)+O(N^{-L-1}),
 \qquad \deg p_r\le r+1.
\]

The assertion is made for every finite order \(L\), with uniform
remainders. Constants may depend on the fixed tree, certificate, compact
and expansion order. Lower coefficients may be separated by level
parity; the leading diagonal comes from the same geometric phase.

## Exact identities checked in the analytic construction

The canonical factorial interpolation \(G_N\) used in M.4 has three
normalizations that affect the result. Gamma's functional equation and
Euler's sine product give

\[
 \frac{G_N(z+1)}{G_N(z)}=2\sin\frac{\pi(z+1)}N,
 \qquad G_N(z)G_N(-z)=H_N(z)^{-1},
 \qquad G_N(z)G_N(N-1-z)=N.
\]

For example, multiplying the factors at \(z\) and \(-z\) reduces the
infinite product to \(\prod_{j\ge1}(1-z^2/(Nj)^2)\); the remaining
gamma product is \(\pi z/\sin\pi z\). This fixes the inverse in the
second identity. The third follows by applying the first identity
\(N-1\) times and using the finite sine product. These identities give
the displayed turn insertion \(H_N/W_k\), with the same numerator and
denominator as the finite source.

The midpoint arguments in the Newton interpolant use
\(d/2=(N-1)/2\). At a lattice point, each pair of recurrence factors is
\(4\cos((j+1/2)\pi/N+\tau/2)\cos((j+1/2)\pi/N-\tau/2)\),
which equals the source factor \(c_j+2\cos\tau\). Thus the interpolation
does not replace the source by a shifted lattice.

The product for \(W_k(s)\) selects distinct nonzero integers in
\(\prod(1-s^2/m^2)\). On a fixed compact avoiding the real integer
zeros, the finitely many small factors and their inverses are bounded;
the remaining logarithms have an absolutely summable \(m^{-2}\) bound.
This supplies a uniform bound for every selected subproduct, without
assuming positivity for complex \(s\).

The higher-order proof uses the same exact contour decomposition as K.
Only the local nondegenerate contributions are expanded. Outside them,
it retains the exact messages and their strict exponential estimates.
Each child is divided by its exact nonzero value at zero; replacing that
complex value by its modulus would lose the required normalization.
The bulk gamma arguments lie in a fixed right-half-plane sector, and
the remainder after sufficiently many Stirling terms is summable over
the product index. Uniform differentiated expansions follow by Cauchy's
estimate on a slightly larger compact. These are analytic arguments;
finite coefficient checks do not replace them.

## Why the polynomial degree bound is a separate step

The local integral has an auxiliary analytic parameter \(t\), with
physical specialization \(t=s/N\). Its stationary phase is
\(S(t)\), including the original first-charge term and the quadratic
framing term. Its normalized expansion has the form

\[
 N[S(s/N)-S(0)]
 +\sum_{j\ge0}N^{-j}[C_j(s/N)-C_j(0)].
\]

At order \(N^{-r}\), the phase contributes degree \(r+1\) in \(s\),
while every amplitude contributes degree at most \(r\). Iterated and
joint Gaussian integrations give the same coefficients: at any fixed
order they integrate the same finite Taylor polynomial, with the same
Schur complements. The proof therefore concerns the coefficients of the
actual normalized messages. It does not posit a different effective
phase. Nor does it assert a global quantum asymptotic for fixed
\(M\ne1\), which would require \(s\) of order \(N\).

## The recurrence implication

Let \(P=\sum_{j=0}^d a_j(q,M)T^j\), \(TM=qMT\), be a fixed nonzero
operator annihilating the whole reduced state at all sufficiently large
levels. After clearing rational denominators and removing a common
\(q-1\) factor, write \(P_0(M,L)\ne0\) for its first classical symbol.
The exact conversion to \(Z_N\), with \(f(M)=M-M^{-1}\), is

\[
 \widetilde P=\sum_j a_j(q,M)(-1)^j
                 \frac{f(M)}{f(q^jM)}T^j.
\]

Multiplying on the left by \(\prod_{j=1}^d f(q^jM)\) gives classical
symbol \(f(M)^dP_0(M,-L)\). Both the sign and the meridian factor are
retained. The exact operator equation on a disk and its translates makes
each coefficient of the asymptotic expansion vanish there. After the
denominators are cleared these coefficients are polynomials in \(s\),
so they vanish identically.

Put \(h=\log q\), \(u=hs\), and use the degree bound to write the formal
logarithm as \(h^{-1}\mathcal S(u)+\sum_{j\ge0}h^j A_j(u)\).
Its finite difference under \(u\mapsto u+jh\) has no negative powers
of \(h\), and its constant term is \(j\mathcal S'(u)\).
Substitution in a bivariate formal series is well defined because

\[
 [h^ns^b]B(h,hs)=B_{n-b,b}\quad(b\le n),\qquad
 B_{a,b}=[h^{a+b}s^b]B(h,hs).
\]

It is therefore injective. Applying this inverse coefficient rule to
the vanishing operator expression gives

\[
 f(e^u)^d P_0(e^u,-e^{\mathcal S'(u)})=0.
\]

The nonzero formal factor \(f(e^u)^d\) can be canceled in this identity.
This cancellation does not remove a component of the original operator.
If the independently constructed longitude is
\(L_{\rm geom}(e^u)=-e^{\mathcal S'(u)}\), then evaluation on its germ
has a nonzero prime kernel in
\(\mathbb C[M^{\pm1},L^{\pm1}]\). The kernel contains no nonzero
polynomial in \(M\) alone, since \(M\) varies on an open disk. It is a
height-one prime in a unique factorization domain. Its irreducible
generator therefore divides \(P_0\). Over \(\mathbb Q\), contraction
gives the rational factor, possibly containing several complex conjugate
components. No multiplicity or equality with the full A-polynomial follows.

## Existence of a genuine recurrence

The finite-sum note is an additional input, not a consequence of the
asymptotic expansion. Its proof was read in full. The original truncated
crossing matrices have a generic-\(q\) finite lift; the lift is not claimed
to define a topological invariant away from the roots. Its summands have
aligned factorial endpoints and finite integral-linear support.

The dimension count includes the zero extension at support boundaries.
A stratum with \(r\) independent near-boundary constraints has
\(O(R^r)\) possible labels and a Laurent span of dimension
\(O(R^{s+2-r})\). Smith normal form retains unsaturated lattice
components. Summing over strata leaves \(O(R^{s+2})\) dimensions, fewer
than the \((R+1)^{s+3}\) formal shift monomials. Thus a nonzero operator
exists before summation.

That operator can vanish when internal shifts are set to one. The note
handles this explicitly: expand it to its first nonzero degree about
those shift values and use finite exponential moments of the summand.
The lowest coefficient annihilates the complete sum. Before specializing
\(q^N=-1\), remove the common central factor in the unspecialized
operator. Regularity of the finite lift at the root then gives a nonzero
fixed all-level recurrence. The boundary, moment and specialization
arguments were checked; no holonomicity closure theorem was substituted
for them.

## The geometric interpretation

The [separate geometric review](directed-geometry.md) found and replaced
one indirect dependency in the geometric-germ identification. The old
route required a positive triangulation of the filled manifold. The
new subsection in Appendix I instead uses the retained positive
augmented tetrahedra at the filling endpoint. Edge rows together with
the main meridian and primitive auxiliary slopes form a full-rank real
Lagrangian system. Positivity makes its logarithmic shape Jacobian
invertible. The explicit shape/representation inverse and the distinct
auxiliary longitude eigenvalues then show that fixing the slope
logarithms imposes the projective filled-group relations, leaving the
main eigencharacter as local coordinate. This removes the separate
filled-triangulation existence input from this family’s argument.

## What remains outside formal verification

The exact quantum pointing and framing convention remain imported from
the original source construction. The global contour margins come from
K and its exact finite-source inputs. The local analytic family uses
canonical interpolation and uniform nondegenerate stationary phase.
The geometric conclusion additionally requires the full marked face
relations and the preferred-longitude calculation, not merely the
exponentiated stationary equations. These dependencies are written
proofs, not consequences of the formal substitution or finite scripts.

The review does not prove the full quantum A-ideal, a result for cyclic
source graphs, or a volume limit outside the stated diagram criteria.
Its conclusion is an audit of this implication with its hypotheses
retained, not a proof that every hyperbolic knot satisfies them.
