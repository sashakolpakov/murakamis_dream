# Bounded source-asymptotics proof read

Reviewed public working source `papers/source-asymptotics/main.tex`, SHA-256
`b39a4b036ed8c7acd9966d224bd5a8055b183b1ee6307354174119bc15bd2808`. Exact companion hashes and stable label/line anchors are in
`source-asymptotics-companion-snapshot.json`. No finite numerical test or formal proof of the
analytic estimates is being counted as part of this read.

## Finding and repair

The original statement of Proposition `sa:local-log` did not explicitly
exclude the singleton `(x,b,y)=(0,b,0)`, although the subsequent proof used
`x+y>0`. That omitted hypothesis matters: the exact recurrence gives
`R_n=b^n product_(r<n)(a_r+u)`, whose zeros approach `u=0`. There cannot be a
fixed zero-free spectral disk in that excluded case.

The current source now states `x+y>0` both before the proposition and in
its hypotheses (lines 321–330). Lines 50–55 discharge it for every actual
box: simplicity makes the edge joining the two protected vertices the
unique marked nonmatching edge, so it cannot be a matching diagonal. The
included sole-variable case is `b=0, xy=0, x+y>0`, whose monomer formula is
independent of `u`. This fixes a local statement's scope and does not narrow
the actual marked-sphere application.

No further concrete defect was found in the inspected chain below.

## Finite polynomial and positive matrix adapter

At `sa:node` (line 226), the row equations agree with the
actual cleared recurrence: the coefficient of a two-row jump retains its
unused diagonal. The normalized degree-a polynomial is the eigenpolynomial
of the displayed q-difference operator with eigenvalue s_a s_(a+1), and
successive eigenvalues are distinct through the physical cutoff J.
The displayed Jacobi recurrence is the determinant recurrence of
bI+xH_-/2+yH_+/2: its squared off-diagonal is
b_(a-1)[(x+y)^2-4xy cos^2((a-1)theta)]/4. The supplied Cholesky pivots are
positive through the last actual row. The moment argument needs moments
only through degree 2J-1; its denominators remain below N. It uses generic
nonzero norms and polynomial continuation, not a false positive-moment
assumption.

The node identity's scalar is S_(2a). At the maximal physical fold the odd
case has S_J^2=N and no forced linear factor; the even case has S_J^2=N/2,
s_m=2 and one factor x+y. Both give exactly `sa:anchor` (line
307). The odd skipped-middle term remains in `sa:odd`,
including its derivative at u=0. No odd determinant identity is applied to
the even complete off-grid cofactor.

The actual polynomial definition and Fourier gauge use Finite Proposition
4.1 (`prop:local-face-fourier`), on one N-dimensional residue block with
transpose and diagonal gauge. Finite Theorem 9.1 and Corollary 9.2 identify
the whole marked coefficient and subsequent tensor filling. Their numbering
was checked against their current sources/compiled label records. These
finite diagram-identification results are imported, not reproved here.

## Local analytic chart

Proposition `sa:local-log` (line 327) is proved from
the actual recurrence, not by differentiating a nodal interpolant. On an
interior starting interval the dominant recurrence root is separated;
the nested-domain Riccati construction retains an exponentially small
residual. The initial conditions give the written alternating geometric
amplitude, converging to (1+k_0)^(-1). Its truncation is made before the
terminal row. The unused-diagonal comparison controls omitted starting
rows, and is used only on distinct positive lower diagonals at u=0; the odd
central zero diagonal is not inserted into that comparison.

The cotangent rectangle formula has the correct N/(2i) coefficient. The
vertical sides lie on half-grid lines and retain the endpoint loss. The
horizontal cotangent error is exponentially small after choosing height
before the parameter neighborhood. For a protected middle variable,
`r(0)=-1` is a modulus equality, not an eigenvalue collision: `1-r` remains
invertible. The displayed near-identity conjugation leaves O(h^2) per step
and hence O(h) total error. The exact monomer case is treated separately.

The terminal ratio gives the central unit limits in `sa:central-unit`
(line 518). In particular the odd limit includes
1+4uP/lambda_*^2=2sqrt(A^2+uP)/(A+sqrt(A^2+uP)); it does not discard the
skipping term. Defining B_N=N^(-2)P_C retains every finite local prefactor
inside its logarithm. The absolute action constant and derivative are the
proved Local Lemma 5.1, not a geometric volume normalization.

## All phases, missing interpolation nodes, and the shared saddle

For `sa:triangle-gap` (line 569),
Tr(I-B*B)=sum_(j<k)|phase_j-phase_k|^2 Tr(A_j A_k); singular-value
logarithms give exactly the factor 1/2 in the determinant bound. With a
positive middle entry, disjoint interior Cholesky vectors give cN pair
trace without needing a uniform bound on the last physical matrix row.
For zero middle entry, the exact binary polynomial has a mode separated
from both ends and variance at least cN; that variance equals the relevant
pair trace. Monomial triangles are excluded from this phase-loss claim.

For `sa:cofactor-gap` (line 619), the near-fold
nodes use the positive matrix phase loss, and the far nodes have a
positive path/dimer loss, or the explicit start-ratio loss when xy=0.
Local Lemmas 3.1–3.2 provide actual nodal positivity and the O(log N)
full-grid interpolation. If j<J, multiplying by the missing-node factors
first is essential; the paper includes it and proves a polynomial division
cost using a one-sided interval beside a maximum. Thus unavailable nodes
are not silently assigned arbitrary values.

Every term of the exact central factorization retains a terminal cofactor
from each triangle. The other factors obey Local Proposition 3.3 / Lemma
3.2 and the explicit endpoint comparisons. Consequently the angular loss
is a bound for the actual whole central product at every real spectral
vector, not for a favorable term. The surviving ordinary graph is connected.
Its edge difference rows contain a spanning tree and generate the full
sum-zero integer lattice. Quotienting the common phase therefore gives
exact measure (2pi)^(-(R-1)) dtheta, with no index or parity multiplier.

The finite phase `sa:Psi` (line 729) keeps d/N, all exact
local logarithms and the even fold offset. Its limiting face Hessian is the
positive weighted graph form `sa:laplacian`. Fixing one face scale gives the
nondegenerate saddle. The actual Laurent polynomial permits the contour
change; the global angular estimate controls its complement after a small
fixed complex parameter perturbation. Uniform analytic Taylor estimates
then give the relative Gaussian error O(N^(-1)), with cubic terms cancelling
on the symmetric local domain. No missing amplitude is supplied by an
external interpolation.

## Global real gap and fixed complex strip

Local Lemmas 4.1 and 5.2 yield `sa:real-upper` (line
798) with both the true triangle action and the
endpoint branch (1/2)log b. The latter is strictly below the complete
nonmonomial action; the former strictly decreases away from zero. The
finite-block transfer proof is perturbed only after its block length has
been chosen, so repeated transfer roots do not require an ill-conditioned
eigenbasis. This supplies the stated small complex face neighborhood.

The separated spectral coordinate gives a loss on the small phase chart;
`sa:global-angular` handles the complementary phase torus. Both use the
same radii and the same target factor, giving the shared coefficient gap.
The separate spectral degree is at most d=N-1 directly from the divided
difference. The product Poisson estimate `sa:Poisson` (line
847) then extends the real gap to a fixed complex strip:
a separated real coordinate assigns uniformly at least 3/4 harmonic mass
to the eta/2 separated set. The monomial growth cost is exactly
2pi d sum |y_e|. This is an actual shared-polynomial extension, not an
inference from positive real local data alone.

## Export and limits of this read

At `sa:export` (line 871), the H1 exponent is
alpha=2R-(R-1)/2=(3R+1)/2 and the amplitude is
(2pi)^(-(R-1)/2)/sqrt(det H_N). Substitution in Oscillatory Theorem 1.1
(`of:main`) gives N^(R+1/2) sqrt(2pi), the displayed product of spectral
sines and both Hessian determinants. The level signs cancel exactly:
(-1)^((N+1)R+dR)=1. The original unit Gamma_N is retained. The finite A_N
remain inside the exponential; mere convergence is not used to replace
them by their limit in a relative formula.

The source theorem supplies only the central-sector H1/H2 inputs. The
oscillatory companion still supplies the whole charge sum, endpoint
currents, independently signed long-twist comparison and noncancellation.
The finite companion supplies original diagram/normalization identity.
Marked primitive filling, action-volume equality and complementary-sector
suppression are separate inputs to any full invariant theorem. No such
full invariant conclusion is asserted by the present source paper.
