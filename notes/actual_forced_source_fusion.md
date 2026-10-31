# Forced physical overbridges and charged full-block source fusion

28 October 2026. This gives two constructive reductions of the original
source, at every N, arbitrary braid width and arbitrary crossing signs.
First, the exact bridge contractions continue through the actual
closure pivots. A marked-cut extreme therefore removes a whole physical
overbridge, including pieces on opposite sides of the braid cut.
Second, full blocks remain exactly contractible after earlier fusions
lower the source charges. All such contractions terminate, with explicit
charge redistribution, scalars and clock feedback retained.

This does not identify the remaining source with that of a smaller
knot, make its defects sublinear, or establish geometric noncancellation.
In particular the actual figure-eight macrodefects are transported into
the reduced source, not removed by changing its definition.

## 1. Continue bridges through the original source

Write d=N-1, Q=exp(2 pi i/N), x=-exp(-pi i/N). The
[signed bridge theorem](actual_signed_overbridge_unwinding.md) gives,
with the opposite physical pair fixed on its actual grids,

    M_j(Zout,Zin)=c_j Pout_j(Zout) Pin_j(Zin),
    Pin_j(Z)=Z^(-h_j)(b_j/Z;Q)_(d-h_j),
    Pout_j(Z)=(a_j Z;Q)_(h_j).                     (1)

Every original c_j is the explicit signed scalar in that theorem,
including kappa, the phase Q^(+/-h_j(h_j+1)/2), the spectator
monomial, and 1/N. None is discarded here.

Let an identity or original pivotal wire continue the first output
to the next input. In the physical finite basis its operator is
diag(eta t^a), 0<=a<=d. Thus t=1, eta=1 at the unpivoted marked
continuation, whereas

    t=Q^(-1), eta=x^(1-N)                          (2)

at an ordinary closing pivot. The whole original averaged marked row
is converted to this unpivoted continuation with the SINGLE exterior
factor 1/N **before** splitting crossings into clocks. This is the
integer-degree source theorem already used in the
[global charged state](actual_global_charged_bridge_flow.md).
No sectorwise scalar-endomorphism or Schur argument is used.

For arbitrary endpoint Fourier frame roots the exact continued wire is

    sum_(k,l) Pin_next(z_l) E_(l,k) Pout_prev(w_k)
      =N eta CT_Z Pout_prev(t Z) Pin_next(Z).       (3)

Indeed E=G_next diag(eta t^a) G_prev^(-1). The first matrix product
recovers precisely the polynomial eta Pout_prev(t Z), since its
degree is at most d. Multiplication by Pin_next has frequencies in
[-d,d]. The remaining finite root sum is therefore N times its
constant term, with no nonzero cyclic alias. This proves (3) even
when the two old central frame parameters differ. It uses the
finite interpolation source, not a bare full-Psi seam deformation.

The old complementary identity consequently gives

    N eta (-a_j t)^h_next Q^(h_next(h_next-1)/2)
      *[h_j choose h_next]_Q
      *(a_j t b_next Q^(-1);Q)_(h_j-h_next),        (4)

when h_j>=h_next, and zero otherwise. Thus the same monotone clock
simplex and q-multinomial compose across ALL closure continuations.
The only changes are the displayed t and eta factors.

Select every physical over-output-to-over-input continuation,
including closure continuations, and freeze all unselected under
and endpoint labels. These selected paths are disjoint. A directed
cycle would be an entire link component with no under encounter.
For a one-component knot with at least one crossing this is
impossible: both encounters of each self-crossing lie on that
component. Thus the selected components are genuine finite paths.
Applying (3)--(4) to every such path gives exact simultaneous
contraction of all TRUE physical overbridge interiors, independent
of where the braid was cut.

After homogenizing, each physical overbridge still has total block
length exactly

    (d-h_first)+sum(h_j-h_next)+h_last=d.           (5)

The finite multinomial, every c_j, every closing eta and all t shifts
remain. There is one factor 1/N per bridge, canceled by its anchor
root sum as in the global charged theorem. The single exterior
marked factor 1/N remains. In particular the number of polynomial
bridge events may be reduced from the number of open-braid paths
to the number of physical diagram overbridges. No cup, marked row
or nonordinary turn is moved in this assertion.

## 2. A whole overbridge is forced to an extreme source face

Use the actual finite cyclic-source support theorem from
[the cut peeling proof](original_source_cyclic_variation_peeling.md)
and its [current-clock dictionary](actual_alternating_balanced_source.md).
For either sign, put u=[b-a-1], v=[a-c], t0=[c-e], z=[e-b].
A supported local crossing has u+v+t0+z=d. The actual overclock is

    h_plus=u+v,       h_minus=u+z=d-t0.            (6)

The whole original source forces at its first position-1 crossing
u=v=0, and at its last position-1 crossing v=t0=0. These are actual
pathwise statements, for every cut color, before coefficient sums.
They apply after the whole source replacement preceding (3).

Suppose the first position-1 crossing is positive. It is an OVER
encounter at the first cut head, and (6) forces h=0. After the exact
bridge sums, monotonicity forces every subsequent clock of this
physical overbridge to be zero. If the cut lies inside the bridge,
the preceding encounter at that cut head must be the last negative
position-1 crossing: only the negative OVER output is on that head.
Equation (6) forces its clock d. Monotonicity forces the entire
pre-cut portion of the same physical overbridge to have clock d.
The bridge therefore has either all clocks zero (if the cut is its
initial endpoint), or the form

    d,...,d | 0,...,0,                             (7)

where the bar is precisely the marked continuation. Dually, if
the last position-1 crossing is negative, the distinguished bridge
has an all-d terminal portion, and an all-zero portion beyond the
marked continuation if that continuation is inside the bridge.

Consequently its homogeneous source kernel has exactly ONE
nonzero-length block, and that block has length d: the input block,
output block, or the single internal d-to-0 jump. All its other
Pochhammer lengths vanish and its multinomial is one. The FULL
bridge, of arbitrary length and signs, is thus a reproducing block
against the complete remaining exterior, to which Section 3 applies.

The propagation in this paragraph is a statement about the EXACT
SUMMED clock sector. It is not a pointwise restriction on each
unsummed cyclic path. For example at N=2 the word [1,2,-1,-2]
has a supported original path with clocks (0,0,1,1); its increasing
overbridge clocks cancel under (4). Only the initial clock extreme
itself is the pointwise cut restriction.

This applies to arbitrary signed words having first position-1 sign
positive or last position-1 sign negative, with no alternation,
twist-family or bridge-width hypothesis. A whole-word cyclic recut
may put any positive position-1 occurrence first; if none exists,
the last such occurrence is negative. Such a recut uses the
original knot invariant's whole braid-conjugacy equivalence before
decomposition, and is not an identification of its individual
clock sectors. The exact source reduction itself needs only the
stated first/last sign condition and the local support proof above.

All feedback of the removed bridge remains explicit. In particular
its under continuation is

    z_out=x^sigma z_in             when h=0,
    z_out=x^sigma Q^sigma z_in     when h=d.         (8)

The second line is Q^(-sigma d)=Q^sigma, not the first line. The
original integer charge d and its phase must not be discarded as
if this were a zero clock. Remaining bridge parameters still depend
on all surviving clocks through the proved feedback matrix.

## 3. Full blocks fuse arbitrary relative source charges

Write B_d(X,Y;a)=product_(r<d)(X-Q^r aY), s=aQ^(-1). Root
complementation gives B_d=sum_(j=0)^d X^(d-j)(sY)^j. For ANY
polynomial exterior F and ANY 0<=q_X,q_Y<=d,

    [X^q_X Y^q_Y] B_d(X,Y;a) F(X,Y,U)
      =s^(d-q_X) [Y^(q_X+q_Y-d)] F(sY,Y,U).       (9)

The right side is zero when its source charge is negative.
This is an exact coefficient identity, without a bound on the
degree or valency of F. To prove it, the term X^r of F contributes
only j=d-q_X+r. The left side thus includes r<=q_X. On the right,
every omitted r>q_X has Y-degree at least d-q_X+r>d>=q_Y in the
unshifted source, and cannot contribute. Its scalar is exactly
s^(d-q_X), as displayed. Equivalently the substituted exterior is
needed only modulo the actual remaining source charge plus one.

The new anchor charge is

    q_new=q_X+q_Y-d.                              (10)

It stays at most min(q_X,q_Y), and is nonnegative precisely when
the saturated pair has enough charge to support its d internal
factors. Thus a full block never stops being contractible merely
because earlier fusions lowered its endpoint charges. Equation
(9) extends the previous q_X=q_Y=d source reproducing identity.
All scalar monomials generated by the substitution remain.

For a loop of ANY length L,

    B_L(X,X;a)=X^L (a;Q)_L.                       (11)

Extract its displayed scalar and lower the charge of X by L;
negative charge means zero. In particular a full loop requires
q_X=d and then removes X by evaluating the entire exterior at
X=0. Its scalar is

    (a;Q)_d=G_N(aQ^(-1)), G_N(t)=sum_(j=0)^d t^j. (12)

At unit root phases this is the retained resonant value N, zero,
or 2/(1-q^m) already computed in the general fusion theorem.
For partial loops, (a;Q)_L can have exponential size and MUST
remain; no tame-modulus claim is made for (11).

A zero-charge anchor is also eliminated exactly by evaluating its
whole incident polynomial at zero. Each outgoing B_L(X,Y;a)
then contributes (-a)^L Q^(L(L-1)/2) Y^L; each incoming block
contributes its other endpoint to the power L. These monomials
lower the neighboring source charges by L, retaining their exact
coefficients. A negative resulting charge gives another exact zero.

It follows that loop extraction, zero-charge evaluation and all
full-block contractions form a TERMINATING reduction for every
original clock sector, with no branching sum or omitted current.
Each loop step removes an edge, each other step removes an anchor,
and no block length increases. The residual source is loop-free,
has all charges between 1 and d, and has no length-d block. It is
an exact charged polynomial exterior, not automatically the source
of another knot diagram.

## 4. Defect transport and the full-block topology

Let S_v count all incident factor lengths, with loops counted twice,
and define delta_v=S_v-2q_v. Under a nonloop full contraction,

    S_new=S_X+S_Y-2d,
    q_new=q_X+q_Y-d,
    delta_new=delta_X+delta_Y.                     (13)

Thus opposite macrodefects can cancel when the actual full-block
adjacency permits their fusion. Other macrodefects can add. Partial
loop extraction removes 2L from S and L from q, so preserves delta.
A zero-charge evaluation distributes its removed incident lengths
as precisely the charge loads just described. These are actual
source transformations, rather than a declaration that the shell
has become balanced.

There is also a useful topology-only zero test. If a connected
full-block subgraph has m vertices and r full edges, its internal
degree rd cannot exceed sum q_v in a nonzero source coefficient.
Since every q_v<=d, r>=m+1 forces zero. If r=m, all its q_v must
equal d. Hence the full-block graph of a nonzero sector is a
PSEUDOFOREST. Its trees reduce by (9) to charge

    q_C=sum_(v in C) q_v-(m-1)d.                   (14)

A unicyclic component reduces to the explicit full-loop scalar
and evaluation of its complete exterior at its surviving anchor
zero. This gives exact outward monomial loads. A component with
q_C<0 vanishes. Different spanning-tree elimination orders give
equal complete source pairings because every step is the ordinary
coefficient identity (9); the retained gauges and scalar phases
can of course be expressed in different coordinates.

Balanced star--triangle fusion is now available wherever the
reduced actual anchor still has charge d, exactly three incident
blocks, and total length 2d. These conditions are explicit and
testable. The forced bridge alone does not ensure them. The
[all-N figure-eight support theorem](actual_alternating_balanced_source.md)
already shows why setting the remaining defects to zero would
discard the original source. Repeating the new reduction does
terminate, but termination at a positive geometric core or a
nonzero leading scalar remains to be proved.

## 5. Reproducible audit

    python3 experiments/audit_actual_forced_source_fusion.py

The audit checks identity and original pivot continuations between
different finite Fourier frames at N=2,...,10, all relative charges
and arbitrary monomial exteriors at those levels, twelve arbitrary
sign/width physical-bridge support problems (including bridges
crossing multiple closure heads), and eight COMPLETE original
signed word sources. Every clock sector of each whole-source test
is reduced by (9)--(12), compared with its unreduced exact source,
then summed with the original feedback weights and compared with
the original crossing matrices and pivotal cut. The N=3 tests
include surviving reduced sources with charges strictly between
0 and d. These checks validate the formulas; the general proofs
are the coefficient and support arguments above.
