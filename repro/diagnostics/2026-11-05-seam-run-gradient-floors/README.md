# Coarse imaginary-gradient floors for seam runs

This is a bounded floating diagnostic, not an outward certificate.
It evaluates 16 internal-edge corners and 32 oriented boundary-edge
corners. There is no optimization and no word-length enumeration.

The exact proposed gradient bounds give affine costs
cL0=.02*pi, cL1=.057*pi*(.5-a)/2,
cR0=.03*pi, cR1=.057*pi*(1+(.5-b)/2).
The internal source retains both small product perturbations and both
Fourier halves; boundary sources use the original height-zero endpoint
ceilings with one small product perturbation and the seam Fourier half.
At a low boundary the repaired seam is real; at a half boundary the
one admitted height cost is retained.

Every value uses the existing original phase helper, identified by path
and hash in the result. There are no temporary helper imports. Acceptance
of a future theorem requires original-log root enclosures and outward
evaluation, not these proposals.
