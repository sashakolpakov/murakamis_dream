# Fixed right-cubic collision and lift witnesses

This archive preserves the completed fixed-parameter experiment from
5 November 2026. It supplies only the rational witnesses used by the
[exact checker](../../../experiments/check_mixed_right_cubic_collision.py).
The mathematical continuation argument is in
[the research note](../../../notes/research_mixed_right_cubic_collision.md).
The canonical result is
[research-mixed-right-cubic-collision.json](../../results/research-mixed-right-cubic-collision.json).

`fixed_witnesses.json` contains the rational isolation interval for the
collision polynomial and three fixed rational Rouché centers at
\((p,q)=(1,-4)\). The checker recomputes every acceptance inequality;
it does not trust a numerical root proposal or rerun a parameter search.
Run from the repository root:

    python3 experiments/check_mixed_right_cubic_collision.py --precision 320

Two conclusions are proved: an algebraic continuation attached to the
original half-endpoint root reaches a double root, and a separate exact
point changes the marked logarithmic lift by one alias. No finite-source
dominance, finite-sum cancellation, or counterexample to the volume
asymptotic follows. Earlier exploratory floating root or finite-sum
values are not theorem inputs and are not used here.
