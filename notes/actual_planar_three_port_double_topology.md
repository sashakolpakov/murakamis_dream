# The literal planar three-port double and its original Morse source

30 October 2026. This certifies the topology and pointing of the planar
three-port double used in the whole-source reflection calculation.
It constructs an original augmented-link Morse diagram; it does not
assume the doubled graph admits the older two-row noncrossing ordering.
It does not prove the proposed theta-normalized quantum contraction.

## 1. Delete, reflect and sew the embedded vertex

Start with the ACTUAL plane cubic source graph Gamma and an exposed
trivalent vertex w. Retain its cyclic order and the three labeled
incident edge ribbons a,b,c. Choose a small vertex disk meeting exactly
these ribbons once and containing no circle coupon. Deleting its
interior leaves a three-leg ribbon graph in the complementary disk.
For a connected double assume this remaining graph is connected;
otherwise the same construction records all its components rather
than discarding one.

Reflect this entire remaining ribbon disk, reversing its planar cyclic
orders and interchanging black/white source orientations. Glue its
three boundary ends to their corresponding original ends by the
orientation-reversing boundary identification. This is the embedded
three-edge vertex sum

    Gamma_double=(Gamma minus w) union (mirror Gamma minus mirror w).

At the physical six-strand boundary, use the cyclic terminal list
(a-,a+,b-,b+,c-,c+). The reflected disk reads this list in reverse
order. Glue each actual labeled terminal to its reflected copy; in
clockwise position indices this is j -> 5-j. Thus the full head
reversal is prescribed geometrically. A free permutation of ports,
or a same-order adjoint of a trivalent tensor, is not this gluing.

## 2. One original circle per merged edge

Construct the augmented diagram from the SEWN ribbon graph. Replace
 each surviving trivalent vertex by its original three planar main
strand arcs. In its cyclic labels the pairs are

    (a+,b-), (b+,c-), (c+,a-).

The two main strands follow each edge ribbon. Put exactly ONE actual
crossing circle on every resulting edge, with its twice-punctured
spanning disk and any recorded signed twist. In particular each of
the THREE seam edges receives one circle.

An equivalent cut description amputates the three boundary circle
coupons before reflecting, then inserts one coupon on each sewn edge.
Reflecting two already decorated edge stubs and retaining both circles
would give a different diagram. At even levels it could also replace
one required nilpotent coupon by its vanishing square. No such step
is allowed by this certificate.

This expansion gives precisely the Fisher matching graph of the sewn
Gamma. It retains every vertex arc, disk label and component. The
existence of the actual planar diagram follows from the ribbon disk
gluing, not from a graph incidence count.

## 3. An actual Morse word and a legitimate exposed mark

Make the planar main arcs piecewise smooth and choose a generic height.
After small disjoint isotopies their critical heights and the circle
boxes are distinct. Reading height gives an explicit finite sequence
of the original cups, caps, identity strips and circle coupons. Local
orientations of a two-strand box are changed only by its actual cup/cap
bends, hence by the genuine turned coupon and its recorded clocks.
No crossing of two planar main arcs is introduced.

This is an original Morse source even if it has many alternating
cup/cap levels. It need not have all black vertices in one row or all
white vertices in another. Arbitrary structural relabelings of heads
are not substituted for these actual identity strips.

Because w was exposed, choose the seam sector corresponding to its
original outside-face corner. A main arc bordering that sector gives
a distinguished ONE-HEAD cut. Choose the planar point at infinity in
that white region and place this cut at the exposed closing cap from
the start. The remaining whole tangle is a generic Hopf endomorphism
of the physical V_d and therefore scalar. Its actual ordinary trace
has the single factor (-1)^d[N]. The original physical marked row
extracts that scalar because m pV=1.

This justifies the exposed physical pointing of the NEW diagram. It
does not move a bare mark through an enclosing cap of an already
fixed diagram. If a proposed source formula starts at another cut,
its whole pivotal transport must still be supplied.

## 4. The geometric volume subtraction, when cores are certified

Suppose Gamma has the positive labeled ideal rectified core Q of
[the proved NC core theorem](actual_nc_graph_rectified_core_geometry.md),
and w corresponds to its actual triangular face T_w. Reflect a copy
of Q and glue the two copies along those triangles with the prescribed
three-port correspondence. The adjacent right angles sum to pi,
so the seam's white faces merge. The convex-face union proof in that
same theorem gives the positive core of Gamma_double; its volume is
2Vol(Q). Its remaining face labels are exactly those of the ribbon
vertex sum above.

If Gamma has b black and b white vertices, Gamma_double has 2b-1 of
each type. Its actual augmented link therefore has volume

    4(2b-1)v8+4Vol(Q)
           =2[4b v8+2Vol(Q)]-4v8.                         (1)

The subtracted 4v8 is the complete marked theta-link volume. Thus a
source double formula with a theta denominator has the expected
GEOMETRIC normalization. Equation (1) does not prove that source
formula, its positivity, or its asymptotic rate. It is conditional on
the actual positive core and the correctly sewn original diagram.
