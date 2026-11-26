# Seam comparison retaining the actual geometric plane

These are bounded floating diagnostics, not certificates. No source theorem,
incoming-potential comparison, or cyclic asymptotic is proved here. The archived
scripts are unchanged copies of the executed `/tmp` drivers and retain their
absolute helper imports. The manifest records every copied file and the relevant
proof hashes. This is a provenance archive, not a registered reproduction check.

The new search uses the actual cyclic reference for each of the type words
`(3)`, `(4)`, `(3,4)`, `(4,3)`, `(3,4,4)`, `(4,3,4)`, and `(4,4,3)`.
References repeat along an open local window; physical target coordinates in
that window are independently varied. Thus a homogeneous reference does not
impose a one-coordinate physical target identification.

The five physical parameters are the last two left A symbols, the first two
right A symbols, and the seam cutoff value lambda. The four A reals vary in
`[.1,.5]`; lambda varies in `[0,1]`. Literal hybrid neighbor heights and the
row-dependent virtual halos are retained. All permitted selection bits at
positions `-2,-1,1` are included: 29 cases in total. Position 2 is only a halo
in the incoming three-step expression and the seam pair, so its selection does
not enter. The seam selection also has no effect because its height is zero.

For theta=1/2 and collar width rho=.001, the searched expression is

    A3_out - A3_in - theta*(omega_left+omega_right)/2
    + A[beta,alpha] + B[gamma] + 2*Delta_rho + beta*nu_rho
    - Re Gamma_pair.

Here A3 is the literal incoming three-transition sum, not the supremum H.
The source constants are the already-proved full-row constants

    A = [[.360050, .447948], [.485081, .551147]]
    B = [.347548, .515591].

Alpha, beta, gamma are the left, center, and right type indicators (0 for
type three, 1 for type four); nu_rho=-J(rho) and
Delta_rho=rho*log(2)-J(rho). The actual pair plane is evaluated at the physical
complex neighbors. Its middle coefficient vanishes by the original critical
equations. There is no further Q subtraction: the coarser G+Q theorem is a
different comparison, not an additional debit.

All 29 jobs used 60 differential-evolution iterations with population factor 6,
plus a fixed set of endpoint/reference candidates. They took approximately
6.38 seconds. Eight found positive A3 values. The largest, approximately
0.0094322901, has an alternating reference, a type-three seam center, selection
bits `(0,1,0)`, and parameters

    (.3481337349630743, .2602214670924836,
     .49999959334889815, .3547345472920625,
     .0000006665248554194037).

At this witness the pair plane is 1.5009535623, the full constant source ceiling
including the collar is .9770650519, and the endpoint occupation debit is
.0013749898. Only this fixed witness was evaluated with deeper incoming
candidates. The resulting comparison estimates are:

| Incoming depth | Comparison estimate |
| --- | ---: |
| 3 | +.0094322901 |
| 4 | -.0057809654 |
| 5 | -.0060895913 |

A4 enumerates both permitted free predecessor selections and maximizes the
single free real using a fixed grid plus local scalar refinements. A5 enumerates
all permitted predecessor selection pairs and uses bounded two-variable
optimization, including the padded A4 candidate. These are maximum estimates
from below. Their differences are neither upper bounds nor counterexamples to
the exact common-potential criterion. The negative values only suggest that
retaining the actual geometric plane may make the old source constants useful;
they do not justify a universal claim or exclude another positive configuration.

No further search or outward cover was run.
