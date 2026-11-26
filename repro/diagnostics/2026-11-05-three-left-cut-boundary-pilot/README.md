# Bounded own-three left-cut boundary pilot

This is an incomplete feasibility run, not a universal source
certificate. It tests only the external-three/three circle-first
face for an ordinary own-three block. Both conditional orientations
must pass on each accepted cell. The cutoff is 3/20 and the requested
strict deficit is −1/2000.

The cap was 511 visited nodes or 60 seconds at 256-bit precision.
The run stopped at the node cap in 0.53 seconds, with 248 accepted
leaves and 16 pending boxes. Its accepted parameter volume is
exactly 21/16384; the pending volume is 16363/16384. The status
“incomplete” is intentional. There was no rigorously positive
midpoint or exhausted-depth stop.

The source is the own-three adaptation
experiments/certify_mixed_three_left_cut_support.py. The result
records its exact SHA256 and that of the proof design
notes/research_mixed_three_left_cut_support.md, along with all
current source dependencies. It uses own flag zero in the original
root solve, interval self-map, Jacobian and response. The phase
has own denominator power two and second outer coefficient one.

The parameter cube is (theta,rho,psi) in [0,1]^3, with the first
input on its circle and the second input in its closed disk.
The exact polar derivatives, original root response, cancellation
of reference forces and clipped target quadratic gains are used
throughout each accepted cell. The target curvature lower bound
is 6/5, before subtracting the prescribed 2*kappa.

The saved partial tree uses right-first LIFO traversal. Its
pending boxes explicitly retain the uncovered part of the cube.
No target grid, word sample, old root-cover replay, or independent
last-row claim is involved.

Reproduction of the same bounded pilot:

    python3 experiments/certify_mixed_three_left_cut_support.py \
      --pilot --precision 256 --max-nodes 511 --max-seconds 60 \
      --output repro/diagnostics/2026-11-05-three-left-cut-boundary-pilot/result.json

The output filename adds “-partial” when the run is incomplete.
No second pilot or full author run is implied by this record.
