# Sixteen terminal raw-envelope cardinal checks

This archive is a bounded point diagnostic. It does not assert a lower
bound around an entire disk boundary or a whole open-word contour theorem.

For each own type and external type, the driver uses only the four cardinal
points of the proved smaller attached-leg disks:

- type three: center `.35-.01i`, radius `.083`;
- type four: center `.30-.052i`, radius `.060`.

At each point, an existing containing endpoint witness is revalidated.
The actual optimized endpoint action is enclosed by a holomorphic Taylor
bound at that witness center, with its full original gradient and Hessian.
No new endpoint root or parameter subdivision is proposed. The lower-row
maximum uses a rational scalar bracket and original derivative signs.
The two additional branches are the explicit upper-row ceilings
`2*pi*max(-Im(a),0)` and `b2/2+pi*max(-Im(a),0)`.

All 48 point comparisons have positive outward lower bounds. The smallest
is the lower-row comparison at own type three, external type three,
`a=.35+.073i`; its enclosed gap is centered near `.00133245`. This is
evidence that the larger disk comparison may be feasible, not a proof
between the cardinal points. A negative upper-majorant comparison would
not, by itself, be a counterexample to the actual finite source.

The driver records exact inputs, selected old nodes, scalar brackets,
outward intervals, and all input/helper hashes. Reproduce with:

    python3 repro/diagnostics/2026-11-05-terminal-raw-disk-cardinals/diagnose.py
