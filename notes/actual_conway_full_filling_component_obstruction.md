# Full-twist fillings of the positive Conway class remain links

29 October 2026. The robust positive Conway grammar cannot produce
knots by filling all its auxiliary circles with the existing integral
FULL-TWIST kernel. If a compiled expression contains S occurrences
of its seed A=h^3, every such filled diagram has at least 2S+1 main
components. In particular the smallest seed still has at least three.

This is a literal connectivity obstruction, independent of any
asymptotic estimate or geometric deformation. It does not contradict
the complete retained-circle volume theorem. It prevents presenting
a future filling theorem for this unchanged class as a knot theorem.

## 1. The two internal circles in every seed

The original unrotated complete circle L_N threads two through
main arcs, with identity endpoint pairing. The genuine quarter-turn
h=Rturn L_N has the planar U pairing: its two bottom main ports
are joined to one another, as are its two top main ports.

Stacking two U boxes creates one closed internal main component
between the upper cap of the lower box and the lower cup of the
upper box. It leaves U pairing on the four external ports.
Therefore A=h^3 has exactly TWO closed internal main components
and U external pairing. This is an actual tangle calculation, not
a decomposition into quantum channels.

A quarter-turn rotates a tangle and preserves all its already
closed components. Stacking two tangles also preserves every
closed component in each: identity wires are attached only to
their exposed ports, so they cannot connect an existing closed
component to another one. A stack can create additional closed
components, but cannot destroy those present before it.

Induction on E ::= A | Rturn E | E E consequently gives

    internal main components of E >= 2S(E),

where S(A)=1, S(Rturn E)=S(E), and S(EF)=S(E)+S(F).
Closing the four exposed ports adds at least one further main
component. Hence every actual closed expression has

    c_main(E) >= 2S(E)+1.                           (1)

Both cylindrical and cap closures satisfy this lower bound.
All 3S(E) auxiliary components are counted separately.

## 2. The exact filling kernel preserves that connectivity

The original auxiliary-color filling identity replaces a retained
complete circle by the literal full twist R^(-2p), with p an integer,
and its separately recorded scalar. A full twist has the IDENTITY
permutation of its two main endpoints for every sign and magnitude
of p, including p=0. Thus the replacement has the same main pairing
as the original unrotated L_N.

After the same physical quarter-turn, each replaced leaf has the
same U pairing as h. All subsequent identity stacks, rotations and
closures therefore have exactly the SAME main-component connectivity
as the unfilled expression. In particular every one of the seed's
two internal main circles persists after these fillings.

If I is any subset of the auxiliary circles, the filled link has

    c_total(E,I)=c_main(E)+3S(E)-|I|,
    c_total(E,I) >= 5S(E)+1-|I|.                    (2)

Filling every auxiliary component gives c_total=c_main>=2S+1>1.
The threshold "sufficiently long" does not change this conclusion.
Neither a sign choice nor arbitrarily large full-twist powers can
change an even braid permutation into an odd one.

## 3. What a knot extension actually requires

To reach knots one must change the original source topology, for
example by retaining an ODD half-twist coupon at selected auxiliary
ports before performing the full-twist fillings, or by using another
seed whose exposed main connections can join these components.
Such a change has its own exact quantum source. The present positive
Newton coefficients and whole-source theorem cannot silently be
reused after changing those coupons.

The existing odd-pretzel knot construction does retain the required
odd half twists, which is why its connectivity differs from the
pure h grammar here. Volume invariance of an unmarked complete
half-twist partner does not identify its finite quantum source or
prove its long-filled asymptotic.

The general complete Conway construction and any verified full-twist
extension of it therefore provide a broad LINK theorem. A broad
KNOT theorem remains a separate critical-path task.

Audit: [literal pairings and full-twist permutation checks](../experiments/audit_actual_conway_full_filling_component_obstruction.py)
and [results](../experiments/actual_conway_full_filling_component_obstruction_results.json).
The proof of (1)--(2) is the all-expression component-preservation
induction, not an extrapolation from the finite samples.

Primary-agent analytical review checked the two permanent internal main circles in every seed, their preservation under turns/stacks, and the identity permutation of every full-twist filling. The resulting link-only scope is independent of source asymptotics.
