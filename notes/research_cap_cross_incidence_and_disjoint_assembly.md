# Exact incidence for a cap/CROSS contraction, and what planarity does not force

31 October 2026. **analytical research lemma.**
Unpublished. This concerns the original
marked source and the fixed spectral pair (+2,-2). No general
spectral-neighborhood estimate or filled-volume conclusion is asserted.

## 1. The literal two-port condition is quadrangulation degree two

Let T be the original simple white triangulated sphere, with its recorded
pairing of triangles across MATCHING edges. Deleting those edges gives
the original simple MAIN quadrangulation Q, with four distinct vertices
on every port disk. Fix the original protected MAIN pair u,v.

Name one residual cap as

\[
 F=(u,A,v,C),\qquad
 (u,A,C),\ (u,v,C),\qquad \text{matching edge }uC. \tag{1}
\]

The ordinary middle A is overloaded; C is the ordinary outer. LEFT,
RIGHT and outer-reflected conventions have the identical incidence
statement after relabeling. The protected vertices are still u,v, not
new zeros introduced by a contraction.

For any vertex a, let d_T(a) be its triangle valence and let m_T(a)
count matching edges incident to it. Then its number of original port
incidences is

\[
 d_Q(a)=d_T(a)-m_T(a). \tag{2}
\]

Each incident matching spoke joins exactly two consecutive triangles
into one port; all other incident triangles contribute their own port.
The four-distinct-vertices condition means that a port is counted once
at a, never twice. Formula (2) also follows by deleting the matching
spokes from the cyclic link of a.

The following are equivalent for the cap child A:

* A occurs in no port other than F and one further port E;
* d_Q(A)=2;
* d_T(A)=3 and its unique matching spoke is AZ, where Z is the third
  vertex in the link of A besides u,C.

In that case the two remaining triangles at A are

\[
 (A,C,Z),\qquad(A,u,Z),
\]

paired across AZ. Hence the other port is exactly

\[
 E=(A,u,C,Z). \tag{3}
\]

up to the original middle/outer reflection conventions. This is the
source typing required by the all-demand theorem after u=v=0.

For completeness, if A occurs at F and E only, F contains one triangle
at A because A is its middle. E contains at most two. A vertex of a
simple triangulated sphere has at least three triangles, so there are
exactly three and E contains the other two, paired across AZ. The
converse follows immediately from this full cyclic star. Equivalently,
each matching spoke consumes two triangles and F consumes one
unpaired triangle, so d_Q(A)=2 forces d_T(A)=3 and m_T(A)=1.

Valence three ALONE is not sufficient. The other two triangles can
instead pair separately across uZ and CZ. Then all three spokes at A
are MAIN and A belongs to three ports. For example, take the triangular
bipyramid with apices A,B and equator u,C,Z, match its three equator
edges, and mark MAIN edge uB. Its cap candidate is (u,A,B,C), while
the other ports are (u,A,B,Z) and (C,A,B,Z), with harmless frame
reflections if needed. Here d_T(A)=3 but d_Q(A)=3. This is an exact
combinatorial distinction, not an assertion that this candidate is a
high-value stationary cap.

## 2. At the classified maximum, the degree-two neighbor is CROSS

Assume the positive-value maximum classification: all ordinary
incidences have positive load, ordinary demands are one, and ports are
complete strict CROSS, strict straddling Green, or residual marked caps.
At (1), its common positive weights satisfy L_A=L_C and the cap loads
are q_A=1-nu, q_C=nu with 0<nu<1/2.

If d_Q(A)=2, the neighboring port has (3). A protected middle cannot
be overloaded. The only possible Green child at E is therefore C.
But its strict Green relation would imply L_C>L_A+L_Z, contradicting
L_C=L_A. Thus E cannot be Green.

If Z is ordinary, E has only one protected vertex and cannot be a
residual cap either. Consequently E is strict CROSS at spectrum -2,
while F is the flat cap at +2, exactly the fixed pair of the signed
contraction theorem. If Z=v is protected, the four displayed triangles
are the whole tetrahedral sphere. E could then only be another cap
or CROSS. Two caps saturate the two ordinary demands and have total
sharp value zero; cap plus strict CROSS cannot supply the C demand.
Neither occurs at the stated positive-value maximum. This also follows
from the cap-cap exception in the odd MAIN-cycle theorem.

For the algebraic assembly below it is harmless to allow Z=v: setting
Z=0 selects the missing C^d coefficient, since M+H=N-2<d. Both
projected pair polynomials are identically zero. We do not assume that
every typed finite pair has an ordinary Z.

There are at most two residual caps, corresponding to the two distinct
triangles adjacent to the marked MAIN edge uv. If BOTH cap children
have d_Q=2, their two-port patches are automatically port-disjoint at
positive-value classified data. Each neighboring E is CROSS, so it
cannot be the other cap. If the two E's were the same port, that port
would have one protected middle and one ordinary middle C. Both caps
would consequently have the same ordinary C in their (u,v,C) triangle.
But the two triangles incident to uv have distinct third vertices in a
simple sphere. This is impossible. Their internal child vertices are
also distinct and have no incidence in the other patch.

This conclusion is conditional on d_Q=2 for the cap children. The
maximum classification itself has not proved that combinatorial
condition.

## 3. Simultaneous replacement with arbitrary shared exterior variables

Fix any finite collection of port-disjoint typed pairs (E_i,F_i), each
with its own ordinary A_i internal exclusively to that pair. The two
protected vertices remain the original ones. Allow C_i,Z_i to coincide
with remaining variables of other patches or of the unchanged exterior;
within an individual port its four actual vertices remain distinct.

At the exact spectra E_i=-2, F_i=+2, retain the original CROSS and
one-sided cap projections. Write

\[
 B_i(C_i,Z_i)=[A_i^d]\,
 H_{F_i,\mathrm{cap}}(+2)H_{E_i,\mathrm{CROSS}}(-2).
\]

and B_i^ref for the positive paired reference after the SAME A_i^d
extraction. At even levels this is the positive endpoint projection;
at odd levels it is the actual fixed-root regularizer at both ports.
The numerator is raw at both parities. The all-demand theorem supplies
a factor kappa_N>=1 with log kappa_N=o(N), independent of the remaining
degree n, such that

\[
 |B_i|_{\mathrm{coeff}}\le\kappa_N B_i^{\mathrm{ref}}. \tag{4}
\]

The common unit source signs do not affect (4). All remaining degree
coefficients are included: n=0,...,N-2 are controlled by the theorem,
and the n=d coefficient is zero on both sides. Both polynomials have
degree d in their remaining two variables. The original unused factors
and normalizations are part of B_i and B_i^ref.

Let G_N be ANY complex polynomial in the remaining original face
variables, with no A_i incidence; it can be the unchanged product of
the other original spectral coupons at arbitrary fixed parameters.
Denote coefficientwise absolute value by |.|_coeff, and let L^t be any
remaining original target monomial. Exact extraction and the triangle
inequality give

\[
 \left|[L^{\mathbf t}]\,G_N\prod_i B_i\right|
 \le\kappa_N^s[L^{\mathbf t}]\,
       |G_N|_{\mathrm{coeff}}\prod_i B_i^{\mathrm{ref}},
 \qquad s=\#\{\text{pairs}\},\quad\log(\kappa_N^s)=o(N). \tag{5}
\]

Indeed the A_i extractions commute and see only their own pair.
Coefficientwise absolute value is submultiplicative, and positive
coefficient inequalities remain valid when remaining variables shared
by different patches are identified. Thus disjoint VARIABLES C_i,Z_i
are not required. The internal A_i's, however, really are exclusive:
one cannot put an A_i-bearing exterior into this argument.

Every target in (5) is the original target d at an ordinary face and
zero at a protected face. Each extracted pair still has its original
remaining degree d. This is a conditional original-sector replacement,
not a topological smoothing, an identity coupon insertion, or a proof
that the reference/exterior contraction is below hyperbolic volume.
It also gives no open spectral neighborhood of the pair (+2,-2), so
it is not by itself a whole Fourier-period bound.

## 4. A structural obstruction to a universal two-port elimination

Neither spherical planarity nor the original matching forces a
degree-two cap child. The family of bipyramids makes this failure
explicit without a knot scan. Let T be the bipyramid over an n-cycle,
n>=3, with apices A,B and equatorial vertices z_0,...,z_(n-1). Pair
the two triangles on each equatorial edge. The MAIN quadrangulation
is the embedded K_(2,n), with ports

\[
 (z_i,A,B,z_{i+1})
\]

up to cyclic frame choice. All quadrilaterals have four distinct
vertices, and T is simple. Every MAIN mark joins one apex and one
equatorial vertex. For mark B z_0, either possible residual cap has
overloaded child A, whose original port-incidence degree is n.
For mark A z_0 the roles reverse. Hence for n>=3 NO possible residual
cap at ANY allowed MAIN mark has the required internal face. For n=3
this is already the valence-three counterexample in section 1.

There are also arbitrarily large simple spherical quadrangulations
with minimum degree at least three: subdivide each face of a cube into
an l by l square grid, consistently across cube edges. The eight old
corners have degree three and all new vertices have degree four.
There are 6l^2 port disks, each with four distinct vertices. The
diagonalization theorem gives simple choices and the general
Morse construction gives actual sources. In EVERY choice, Q and its
vertex degrees are unchanged. Thus no marked cap can meet the
two-port internal-face condition anywhere in this family, for any mark.

Euler only forces some quadrangulation vertex to have degree at most
three, since its average degree is 4-8/V. It does not force degree two,
and it certainly does not place that degree at a cap's overloaded child.
The cap-edge forest and demand-one inequalities concern a different
graph; they cannot delete the other original port incidences of A.

These are structural obstructions to proving universal elimination
solely from planarity and the known local source theorem. They are NOT
examples of dominant non-CROSS maxima, counterexamples to the original
volume conjecture, or a proof that a different multi-port block cannot
work. A theorem forcing an applicable pair at every actual high maximum
would first need an additional exclusion of caps on these incidence
patterns. That exclusion is not contained in the existing activation,
stationary, or odd-cycle classification.

## 5. Why an exterior A load is a genuinely different finite problem

At a classified maximum all ordinary incidences are positive. If
d_Q(A)>2, any selected F plus one neighboring port leaves positive
A-load in the exterior. At a fixed such maximum that load is a
positive constant in normalized degree, not a one-unit endpoint error.

Even in the typed pair (3), keeping an exterior A-degree r changes the
required extraction to A^(d-r). In the even notation of the exact
original-demand convolution, the actual coefficient then becomes

\[
\begin{aligned}
 &[C^nZ^{d+r-n}][A^{d-r}]\,H_F(+2)H_E(-2)
   =\text{(common unit sign)}\sum_j(-1)^jU_jC_{j-r,n-j},\\
 &\max(r,n-H,0)\le j\le\min(M,n).
\end{aligned} \tag{6}
\]

The theorem controls r=0, not all these shifted diagonals. This is not
the already covered variation of the remaining degree n.

In fact an unconditional shifted analogue is false. Set n=r; then
the sum in (6) has only j=r and C_(0,0)=N^2. Its ratio to the paired
endpoint coefficient is exactly U_r/V_r. For N divisible by eight,
N>=16, and r=N/8, the original sine products give

\[
 \frac{U_r}{V_r}
 =\prod_{j=0}^{r}\cot^2\!\left(\frac{(j+1/2)\pi}{N}\right)
 \ge3^{N/8+1}. \tag{7}
\]

This is precisely the uncontracted-pair obstruction,
now expressed as the missing internal-demand shift. It uses a boundary
CROSS monomial with zero ordinary incidences and therefore does NOT
disprove a possible shifted estimate restricted to the positive-incidence
stationary regime. It does show why (4) cannot simply be attached to an
A-dependent exterior or promoted to an all-shifts identity.

## Dependencies

The source bound is the [all-demand, both-parity signed contraction](research_cap_cross_all_demand_subexponential_contraction.md),
with the exact typing and coefficients in the
[original-demand convolution](research_two_port_main_cap_original_demand_convolution.md).
The maximum hypotheses come from the
[finite-multiplier stationary classification](research_full_fiber_sharp_stationary_classification.md)
and [odd MAIN-cycle theorem](research_stationary_noncross_main_cycle_obstruction.md).
The actual general-source realization is the
[matched-sphere Morse construction](research_matched_sphere_morse_source.md);
its simple-chart existence input is the
[maximal-diagonalization theorem](research_maximal_diagonalization_source_gap.md).

The assembly requires the stated degree-two internal faces and exact unshifted demands. It does not assert that every stationary cap has that incidence pattern.

No numerical audit or purported global realization of a non-CROSS
maximum is used. The false preliminary converse “valence three implies
two ports” was corrected before preservation: the actual criterion is
degree TWO in Q, with the matching condition retained. The conclusions
are a conditional fixed-spectrum source replacement and an obstruction
to a topology-only universal use of that replacement. They do not rule
out an additional theorem restricting high-value stationary maxima,
a larger-star contraction, or a spectral-neighborhood estimate.
