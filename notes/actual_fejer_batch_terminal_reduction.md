# Simultaneous terminal reduction of the actual Fejer entropy source

Independently reviewed, 31 October 2026. The labeled right-angled certificate and
the ORIGINAL protected MAIN edge are used. This does not license an
arbitrary one-port relabel, which fails in the recorded width-three
counterexample. No diagonal or other free endpoint is removed here.

Use the finite pattern set A_D and limiting polytopes P_s of
[the original shared entropy theorem](actual_fejer_shared_entropy_variational.md). Let s belong to A_D,
and let q in P_s include the individual cross triangular allocations.
Let J be the set of ALL its one-sided ports whose terminal parameter
is nu=1/2. Replace every port in J by cross simultaneously, leaving
all other types unchanged; call the new pattern s'.

Then s' belongs to A_D. Moreover the SAME limiting global degree
vector q belongs to P_s', and its local entropies can be preserved.
Thus a maximizer for W_D can be chosen with no terminal one-sided
ports. This statement does not assert that one may change only some
of J while leaving the other terminal labels intact.

## 1. A strict all-cross middle margin from the actual geometry

The existing certified complete circle packing supplies an all-cross
angle flow q_geom on the same original incidence graph. Every port
has total load1, every ordinary face has total1, and both original
protected faces have total0. All its middle loads are STRICTLY less
than1/2. To see this, the middle load is a single triangle center
angle divided by2pi. A finite positive middle can have angle pi only
if BOTH outer curvatures vanish. The two protected vertices form a
MAIN edge, while the two outers of a source triangle form its MATCHING
edge, so they cannot be those two vertices. A protected middle has
load0. Since the original graph is fixed and finite, there is eta>0
such that EVERY middle incidence of q_geom is at most1/2-eta.

This is an actual certified shared flow, not independently selected
local radii or an assumed positive-class realization.

## 2. Strict margins and exact finite integral support

At every port now marked cross in s', each middle incidence of q is
at most1/2. This holds for the old cross ports and for the newly
relabeled ones: their overloaded load is1/2, while their other middle
load is mu<=nu=1/2.

Every one-sided port left in s' has nu<1/2, so its overloaded load
is strictly greater than1/2. If such ports remain, put

    delta=min_(remaining one-sided e)(q_over(e)-1/2)>0.

Choose 0<epsilon<min(1/2,delta/2), ignoring the delta condition if
no one-sided port remains, and set

    q_epsilon=(1-epsilon)q+epsilon q_geom.

This convex combination preserves ALL original port supplies, face
targets, incidence repetitions and protected zeros. Every new cross
middle is at most1/2-epsilon eta. Every remaining overloaded middle
is at least1/2+delta/2, since each individual incidence lies in[0,1]
and its change under the combination is at most epsilon. Let gamma>0
be the smaller of these two margins (or only epsilon eta if there are
no remaining one-sided ports).

For N=2m,d=2m-1 multiply q_epsilon by d. This is a real bipartite
flow with EXACT port supplies d, ordinary-face targets d and protected
targets0. Integral cycle rounding, inside the floor/ceiling interval
of every entry, gives an integer flow with the same exact balances
and entrywise error at most1. No new auxiliary target is introduced.

If d gamma>=2, its middle entries satisfy the ORIGINAL finite bounds:

    cross: d(1/2-gamma)+1<=m-1,
    one-sided: d(1/2+gamma)-1>=m.

All other entries remain nonnegative and have sum d at each port;
protected entries remain exactly zero. Consequently every port is in
its actual original local support, including the forced outer unit
at cross ports. This proves finite feasibility for EVERY even N with
N-1>=2/gamma, hence s' belongs to A_D.

The strict perturbation is used only to prove membership in A_D.
It does not replace the desired limiting point q by q_epsilon.
Once membership is known, the already proved source lattice-approximation
lemma applies to q itself in P_s'.

## 3. Preserve the actual entropy and reduce the maximizing type

For a left port with nu=1/2, the actual load and entropy are

    q=(xi,mu,1/2,1/2-mu-xi),
    E=C(xi,mu,1/2-mu-xi).

Use this vector as the input cross triangle and the degenerate output
triangle(0,1/2,0). Their cross load is exactly q and their entropy
sum is exactly E, since C(0,1/2,0)=0. For a right port interchange the
two triangles. Retain every existing cross allocation unchanged.
Thus all shared limiting targets and the total entropy are preserved.

If J is nonempty, the number of one-sided labels strictly decreases.
In particular choose a maximizer for the compact W_D problem with
the fewest one-sided labels among all maximizing representations.
The preceding construction shows it has no terminal nu=1/2 one-sided
port. If every one-sided port was terminal, the resulting pattern is
all-cross and its value is bounded by the already proved complete
geometric value Phi_D.

The reduction leaves diagonal mu=nu, free lower endpoints, other
outer-degree boundaries and ordinary-multiplier degenerations open.
It also does not imply any individual finite term survives a Gaussian
filling contour.

## Review and scope

Root independently read the full proof and checked the strict geometric
middle margin, all-terminal selection, exact scaling by d, integral cycle
rounding and the explicit large-N threshold. Analytical review PASS.
This is an elementary source-support and entropy lemma; no numerical
audit is claimed or required. The note is frozen at this scope.
