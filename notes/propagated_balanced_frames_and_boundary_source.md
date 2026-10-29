# Regular propagated Fourier frames move every wire adapter to the boundary

28 October 2026. The exact balanced four-Psi crossing permits a useful
GLOBAL choice of polarization. For an arbitrary open signed braid, all
local Fermat blocks can remain uniformly regular while every INTERIOR
Fourier adapter is exactly the identity. Only the original boundary
closure/cap co-source needs a change of frame. The number of remaining
wire adapters is therefore at most the braid width, independently of
the crossing count.

This is an exact theorem for the original operator and source, not a
selected-geometric-cycle theorem. It moves the explicit WIRE adapters
to the boundary. The bulk full-Psi logarithmic seams during an off-grid
contour deformation are a distinct issue and are not removed here.

## 1. A regular propagated multisection at arbitrary width

At complete color put x=-exp(-pi*i/N), s=x^N=(-1)^(N+1). For b heads
choose pairwise distinct nonzero constants c1,...,cb and initial central
coordinates

    sigma_i(0)=s^(i-1)c_i.                            (1)

Choose one marked N-th root r_i(0) of each coordinate. At a positive
crossing on heads i,i+1 propagate the actual roots by

    (r_i,r_(i+1)) -> (x r_(i+1),x r_i).              (2)

At a negative crossing use the actual antiunitary mirror, hence the
root propagation has x^(-1) in place of x. Untouched roots stay fixed.
Their central propagation is in BOTH cases

    (A,B) -> (sB,sA),                                (3)

because s^(-1)=s. All root phases and label permutations are retained.

Let D=diag(1,s,...,s^(b-1)), and let P_j be the ordinary permutation
of strands after any prefix of the braid. Then the entire vector is

    sigma(j)=D P_j c.                                (4)

Indeed the signed adjacent interchange (3) is D P_i D^(-1).
At the next crossing the regularity condition in
[the exact local theorem](actual_balanced_fourier_crossing_kernel.md)
is B!=sA. Equation (4) gives

    B-sA=s^i(c_(pi(i+1))-c_(pi(i))) !=0.             (5)

The permutation never assigns the same initial strand to both heads.
Thus EVERY local Fermat chart is regular, for every signed word and
every prefix, without any knot census or restriction to twist knots.

For example c_i=i+1 gives an explicit choice for all words of width b.
All central coordinates then have modulus between 2 and b+1. The local
central shape ratios are ratios of two distinct c_i, so their distance
from one is at least 1/(b+1). The internal norm T=BD/(D-B) and all other
central arguments consequently stay in a fixed compact regular set
depending only on b. No parameter depends on the unknown knot value.

## 2. All interior adapters telescope EXACTLY

Let F_j be the tensor product of the normalized one-head Fourier frames
F(r_i(j)) after prefix j. For the next original crossing R_j, the exact
local theorem gives its regular four-Psi kernel

    M_j=F_j R_j F_(j-1)^(-1).                        (6)

Untouched tensor factors in (6) are identities. This is true for either
sign, with the FULL original scalar and marked full-Psi functions.
The outgoing frame on every physical wire is by construction precisely
its next incoming frame. Hence

    M_m ... M_1=F_m W F_0^(-1),
    W=F_m^(-1)(M_m ... M_1)F_0,                      (7)

for the actual word W=R_m...R_1. There is no interior rational adapter,
no deformation through a Cauchy pole, and no discarded current in this
identity. The positive-degree intermediate allowance in the local
construction has already been removed by its exact E-coproduct proof.

For an original endpoint vector p and co-source row m, the whole source
is therefore

    m W p=(m F_m^(-1))(M_m ... M_1)(F_0 p).           (8)

This includes all original pointed-plat cups, ordinary caps and the FULL
marked row. For a trace presentation with source operator C, it is

    Tr(C W)=Tr[(F_0 C F_m^(-1))(M_m ... M_1)].        (9)

Use the actual averaged first-cut matrix and original closed pivots in
C; no scalarity or replacement of the full marked row is required.
All original framing and external scalar factors remain outside the
same exact equality. Already specified inserted operators can also be
transported by the applicable prefix frames.

## 3. The surviving boundary source has no exponential frame cost

The normalized Fourier matrix is a unitary root Fourier matrix times
diag(r^a). If r^N=sigma_i(j), then

    ||F(r)||<=max(1,|c_(pi(i))|),
    ||F(r)^(-1)||<=max(1,|c_(pi(i))|^(-1)).          (10)

These bounds are independent of crossing count and N. The phases
accumulated by (2) have modulus one. With c_i=i+1, each individual frame
and inverse has norm at most b+1.

For a one-cut braid closure, the boundary change on head i is the
specified finite kernel F(r_i(0))F(r_i(m))^(-1), with central ratio

    C_i=c_i/c_(pi_W(i)).                             (11)

Its entries are the finite-sum/removable values of

    [1-C_i]/[N(1-(r_i(0)/r_i(m))Q^(j-k))].           (12)

The original pivot adds its retained scalar and label shift. At most b
such boundary adapters remain. Each and its inverse have norm bounded
by max(1,|C_i|) and max(1,|C_i|^(-1)), respectively. The actual cups,
caps and marked source keep their original polynomial norms up to
constants depending only on the fixed width and chosen c_i.

The rational off-diagonal tails in (12) are generally only O(1/N), not
exponentially small. Their bounded operator norms do not prove that
the boundary co-source is nonzero on a particular geometric sector.

## 4. Why closing the final adapters by bare diagonal residues fails

If the SAME grid were matched across every closure wire as well,
the vector sigma(0) would be fixed by the full signed permutation.
For a knot, pi_W is one cycle. Equations (1),(4) would then require

    c1=...=cb.                                      (13)

But (13) makes B=sA at every crossing, and its internal sampling radius
T=BD/(D-B) escapes to infinity. Thus the ALL-wire-diagonal stratum is
absent from the regular balanced knot chart. Bare unit Cauchy residues
cannot collapse both the interior and final boundary wires while
remaining in the regular multisection.

Independent or propagated frames avoid that collision, but a nontrivial
boundary source remains. The
[wire-source calculation](whole_fermat_toric_residue_and_wire_source.md)
identifies how a locally balanced section regenerates a Newton/Rogers
current when pushed to a different endpoint center. Equations (7)--(12)
concentrate that transport problem at the original boundary rather
than creating one at every crossing.

The next geometric comparison can therefore start with regular pure
four-Psi bulk blocks on a coherently matched open braid, and a specified
bounded wire co-source on only b boundary heads. This describes the
EXACT grid network. It does not say that only boundary seams survive
after an off-grid analytic interpolation: the local full-Psi deck
characters equal one on the balanced multisection, but their products
at a shared bulk variable need not equal one away from it. Those bulk
logarithmic cut lips remain part of any contour transport. See the
[exact port characters](balanced_crossing_deck_characters.md).
Neither (7) nor boundedness computes the intersection with the positive
constrained-lens cycle. That selected geometric coefficient remains
to be proved.

## 5. Knot scalarity does not slide unequal radius gauges unchanged

There is also a direct obstruction to erasing the boundary co-source
by moving each radius gauge along the knot to its marked cut. Put
D(t)|a>=t^a|a>. In the ORIGINAL complete crossing a positive transfer k
has input (a,b), output (b+k,a-k); a negative transfer has output
(b-k,a+k). Consequently, EXACTLY,

    R_epsilon (D(t1) tensor D(t2))
       =(D(t2) tensor D(t1)) R_epsilon^[t1/t2],

    (R_epsilon^[lambda])_(transfer k)
                         =lambda^(epsilon*k) R_(transfer k). (14)

The extra factor is an actual transfer-clock insertion. It is not a
scalar and is not eliminated by connectedness. To see that it is
unavoidable, suppose an unchanged crossing allowed a product-diagonal
slide with some other outgoing diagonal gauges. Its nonzero transfer-0
entries force those gauges to be the swapped ones in (14); a nonzero
transfer-1 entry then forces t1=t2. Only the common total-degree gauge
slides unchanged through an arbitrary original crossing.

This is visible in the actual connected hyperbolic-knot source, with
no arbitrary replacement exterior. At N=2 use the normalized original
positive crossing (its unit scalar cancels in the writhe-zero word)

    R=[[1,0,0,0],[0,0,-i,0],[0,-i,2,0],[0,0,0,1]],
    g=diag(-i,i), e=ones(2,2)/2,
    W=R_2^(-1) R_1 R_2^(-1) R_1,
    mu(X)=Tr[(e tensor g tensor g) W X].

Direct exact multiplication gives the ORIGINAL figure-eight value
mu(1)=5 and, for the same radius gauge placed on the three heads,

    mu(D(t) tensor I tensor I)=5(1+t)/2,
    mu(I tensor D(t) tensor I)=(11-t)/2,
    mu(I tensor I tensor D(t))=(-7+17t)/2.           (15)

Thus one-cut scalarity does not identify a radius factor on an ordinary
closed head with the same factor at the marked cut. Sliding it requires
the nontrivial current/transfer corrections (14). Applying scalarity
AFTER the whole closure simply recovers the unknown knot scalar; it
does not prove that a separately action-normalized geometric component
has a nonzero source coefficient.

[Audit](../experiments/audit_propagated_balanced_frames_and_boundary_source.py):
exact original signed kernels, regular propagated centers, identity
interior adapters, full-word operator and pivotal-source equality, and
uniform complex frame/boundary norms.
