# Affine real-star and exterior-repair diagnostics

Bounded diagnostics, 5 November 2026. The executed drivers, outputs and logs
are preserved byte-identically. Drivers use the original recorded workspace
path and write to `/tmp`. No optimizer, interval cover or universal sign
certificate is included here.

For real star coordinates `(a,t,c)`, the proposed lower bound is its real
phase sum minus the imaginary real-phase gradients times the repaired
heights, including `pi*selection` at each selected endpoint. This is the
vertical supporting plane of the forcing branch. The source upper bound
is the proved height profile at each physical neighbor height plus the
complete collar. Exterior corrections use coherent rates `e`, not tangent
defects `w`, because this is a direct source-versus-repaired-phase comparison.

The first grid has 49 allowed local type/selection configurations based on
seven actual periodic references, with 1,600 target/attenuation evaluations
per configuration. Inner real coordinates and outer halos are baseline.
Both exact AA corrections are retained; the maximum proxy is approximately
-.2608462. This tests a local isolated-star window repeated from those
references, not a physical one-cycle or joint short-run change.

The second calculation uses the same points and replaces each exact repair
by the convex-chord derivative envelope. If the changing endpoint has
physical height `t*h` and repaired height `h`, `0<=t<=1`, then convexity
and the forcing-branch supporting plane at height zero give
`e(t*h)-e(h) <= (Im(phi_endpoint(other,x))+pi*selection)*(h-t*h)`.
The derivative is evaluated with the changing endpoint real and its other
endpoint at the unchanged admitted complex target. All sampled exact
corrections lie below this envelope; the maximum proxy is about -.2337428.

The third grid additionally assumes the separately investigated acute
phase-gradient lemma, and uses its signed repair envelope. For fixed real
neighbor x and reference-height coefficient c, let
`H=c*R(x)*L_b(x)`. Every physical/repaired pair lies in the triangle
with vertices `(0,0),(0,H),(H,H)`. The profile is convex in physical height,
the star lower plane is affine in repaired height, and the signed repair
envelope is convex in their difference, so these three vertices suffice
for this enlarged expression. Reference-height intervals also reduce to
their endpoints by convexity. This removes arbitrary inner reals/halos and
common attenuation, rather than fixing them at baseline.

The third grid has 18 type/selection configurations, nine middle reference
reals per type, and 400 neighbor-real pairs: 64,800 real-grid points. Its
maximum is about -.1954552 at types(4,3,3), selected left neighbor,
reals(.12,.39,.1). This is still a floating grid; it does not prove the
acute lemma or a uniform three-variable inequality. The independent
height relaxation does not impose actual geometric correlations.

A simultaneous global replacement must still count every original AA edge
once. Two changed endpoints on one edge require an appropriate joint or
sequential correction; the first two diagnostics do not certify that
assembly. No finite-source or knot-family theorem follows from these grids.
