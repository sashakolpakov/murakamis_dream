# A sharp bound for every regular full critical value

28 October 2026. The regular full critical values of the actual
marked knot phase, including its interior integer cut-wall marks,
have imaginary part at most the hyperbolic volume in absolute value.
The representation-volume estimate below is proved directly by
averaging finite regular tetrahedra. It does not assume a volume
conjecture, a positive triangulation for the other representation,
or an efficient triangulation of the knot exterior.

This bounds critical VALUES, not yet the whole original period.
The unresolved upper-bound issue is whether all remaining endpoint
and escaping stationary strata of the selected relative cycle have
such values, or cancel/group away by exact source identities.

## 1. A boundary-parabolic representation has an integrable Lipschitz development

Let M=Gamma\H^3 be an oriented complete finite-volume hyperbolic
3-manifold, and let rho:Gamma->PSL_2(C) be boundary-parabolic.
This means each peripheral image consists of parabolic translations
or the identity and has a common fixed point on the ideal sphere.
No discreteness or irreducibility of rho is assumed.

There exists a rho-equivariant globally Lipschitz map

    f:H^3 -> H^3

which is conical on each lifted cusp. To construct it, put a domain
cusp in coordinates (w,y) in C times (Y,infinity), with peripheral
translations w->w+lambda. Put its target fixed point at infinity.
The target translations tau(rho(gamma)) determine a real-linear map
A:C->C by A(lambda_gamma)=tau(rho(gamma)). Set

    f(w,y)=(Aw+b,c y), c>0.                         (1)

This is peripheral-equivariant. In the metric
(|dw|^2+dy^2)/y^2 its Lipschitz constant is bounded by
max(1,||A||/c). Rank-one or zero A is allowed. Define these maps
on disjoint lifted horoballs and extend rho-equivariantly over the
compact truncated core. The target is contractible; a finite
triangulation and geodesic interpolation extend the boundary map.
A collar joins it to (1). Compactness of the quotient core gives
a finite derivative bound there, so the resulting piecewise smooth
map has one global Lipschitz constant L.

The signed integral

    V(rho)=integral_M f^*(vol_H3)                   (2)

is absolutely convergent, since |f^*vol|<=L^3 vol_M.
It is independent of these choices. On the truncated core use a
rho-equivariant geodesic homotopy and Stokes. On a height-Y cusp
torus, two horizontal derivatives of a conical homotopy are O(1/Y),
and its homotopy derivative is bounded. The side volume is therefore
O(Y^(-2)) and tends to zero. If the peripheral image is trivial,
the affine cusp maps may be chosen independent of w. Changing their
ideal fixed point then gives a side homotopy independent of both
torus directions, whose three-dimensional volume is zero. These
observations also cover different choices of affine cusp data.

The usual ideal straightened sum computes exactly (2). One direct
verification is to truncate the finite ideal fundamental chain,
straighten its developed tetrahedra, and use the same face-homotopy
Stokes argument. Internal faces cancel. All tails point to the
decorated peripheral fixed points and have volume tending to zero
in cusp horospheres. A cusp-equivariant horospherical map differs
from A w by a bounded periodic function; its conical homotopy to
(1) has the same vanishing side estimate. Thus

    V(rho)=sum_Delta oriented Vol(straight_rho Delta)
          =sum_Delta D(z_Delta),                   (3)

with repeated developed vertices contributing zero. Auxiliary
interior vertices may also be idealized: approximate their chosen
ideal flags by finite vertices, use the finite chain identity, and
take the limit in its finitely many bounded tetrahedron volumes.
This is the normalization used by the actual crossing fundamental
cycle, not an independently chosen regulator constant.

## 2. An elementary universal tetrahedron bound

Every geodesic tetrahedron has absolute oriented volume at most v_3,
the volume of the regular ideal tetrahedron. For a finite convex
tetrahedron, put an interior point at the origin of the Klein ball
and extend its four vertex rays to the ideal sphere. The origin is
still in the convex hull of the four ideal endpoints: rescale its
positive barycentric coefficients by the original vertex radii.
Every original vertex consequently lies in the new ideal convex
hull. The finite tetrahedron is contained in that ideal tetrahedron.

For an ideal tetrahedron with positive angles alpha,beta,gamma
adding to pi, its volume is Lambda(alpha)+Lambda(beta)+Lambda(gamma).
The cotangent/Cauchy inequality already proved in
[the charged-simplex calculation](original_crossing_winding_convexity.md)
makes this strictly concave, so its maximum is the balanced regular
value v_3. Degenerate and negatively oriented tetrahedra satisfy
the same absolute bound by continuity and orientation reversal.

## 3. Average FINITE regular tetrahedra; the face errors cancel

Let G=Isom^+(H^3). The finite-volume quotient Gamma\G carries its
normalized right-Haar probability measure mu. Its projection under
g->g p, for any fixed p in H^3, is vol_M/Vol(M).

Choose a finite regular tetrahedron Delta_R. For example in the Klein
ball take the four regular ideal vertex directions, each at radius
tanh R. Let v_R=Vol(Delta_R). These tetrahedra increase to the regular
ideal tetrahedron, so v_R increases to v_3.

First, Fubini and invariance give

    integral_(Gamma\G) integral_(g Delta_R) f^*vol dmu(g)
                  =[v_R/Vol(M)] V(rho).             (4)

This holds for any integrable 3-form: write it as h vol_M,
average h(g p) for each p in Delta_R, and then integrate in p.
The Lipschitz bound above justifies absolute Fubini.

Next replace f composed with g Delta_R by the straight tetrahedron
whose four vertices are f(g v_i). Use a symmetric, face-compatible,
isometry-equivariant straightening: in the hyperboloid model normalize
the positive Lorentz-barycentric sum of the vertex vectors. Its Klein
projection parametrizes their convex hull. For each face take the
geodesic homotopy between its image under f and this straightening.
Stokes gives

    integral_(g Delta_R) f^*vol - c_rho(g)
          =sum_(i=0)^3 (-1)^i b_rho(g,face_i),       (5)

up to the one fixed homotopy orientation; the sign will not matter.
Here c_rho(g) is the oriented volume of the straight tetrahedron.

The face prisms are uniformly bounded as g varies. The domain face
has fixed diameter D_R and fixed parametrization. Its f-image and
the convex hull of its three f-vertices lie in a ball of radius
L D_R. The geodesic homotopy has length at most 2 L D_R and
derivative bounds depending only on R,L. Its volume is at most a
finite constant C(R,L). Thus every b_rho in (5) is Haar-integrable.
No uniform bound as R tends to infinity is needed.

All FOUR ordered regular faces are congruent by orientation-preserving
isometries of H^3. Naturality of the chosen parametrization and
homotopy, followed by right-Haar invariance, therefore makes their
averages equal. The alternating sum in (5) has two plus and two
minus signs and averages to zero. Consequently

    [v_R/Vol(M)] V(rho)=integral c_rho(g) dmu(g).     (6)

By Section 2, |c_rho(g)|<=v_3. Therefore

    |V(rho)|<=Vol(M) v_3/v_R.

Letting R tend to infinity proves the SHARP bound

    |V(rho)|<=Vol(M).                              (7)

The proof did not use an unproved equality between an ordinary
measure-homology cycle and a fundamental class. Equations (4)-(6)
are direct integrals; finite regular face congruence cancels the
only straightening error. It also did not need a controlled norm
for an exponentially conditioned quantum face frame.

## 4. Apply it to all regular FULL critical values of the actual period

Use the actual cotangent/fusion and coupled-cap equations from
[the full scalar period](actual_full_psi_scalar_flow_cycle.md), and
the exact regulator identity in
[the critical-wall calculation](actual_wall_critical_regulator.md).
At a regular full critical point Z, the actual crossing/cap equations
give a framed representation rho of the knot group. At the complete
meridian its peripheral image is boundary-parabolic. Indeed a
noncentral parabolic meridian has parabolic centralizer; if the
meridian is central in PSL_2, normal generation makes the entire
representation trivial.

The actual crossing certificate is representation-independent:
its finite oriented-chain proof uses the Wirtinger relations,
unipotent meridian action, and generic auxiliary region flags, not
the geometric embedding. Degenerate developed configurations are
normalized to zero, as specified in
[the fundamental-cycle proof](crossing_fundamental_cycle.md).
Together with (3) it gives

    sum_j epsilon_j D(A_j)=V(rho).                  (8)

For an interior ray/cut mark, the action has the retained integer
form W_m=W+2*pi*i sum_j m_j Log A_j. The proved identity is

    Im W_m -sum_j epsilon_j D(A_j)
                        =Re Z dot Im(gradient W_m). (9)

At a FULL critical point the right side vanishes. The original
real phase constants and scalar line are retained in the cited
calibration. Equations (7)-(9) therefore prove

    |Im W_m(Z_critical)|<=Vol(M)                    (10)

for every such regular full critical point, including nongeneric,
nongeometric and integer-marked embeddings on that regular chart.
No positivity of the individual developed tetrahedra is required.
The oversized weak alias-face example is not a counterexample:
a maximum on a constrained angle face need not solve the full
critical equations of this actual knot representation.

## 5. Regular cap-endpoint stationary values are exactly zero

There is a further class of non-full source strata to which the
same argument DOES extend. Use the exact coupled interval sources,
and write their logarithmic variables as

    p_c=2*pi*i*s_c.

Consider any stationary point of a regular stratum where one or
more s_c are fixed at 0 or 1. Require stationarity in ALL remaining
variables, including head, Gaussian and interior cap variables.
The phase, its logarithmic marks and its physical canonical/Hurwitz
maps must remain regular on this stratum. No assertion below applies
to an infinite position or an undefined logarithmic shape chart.
All ACTION coordinates, including auxiliary fusion positions, must be
finite and regular; bounded physical meridian matrices alone do not
supply this hypothesis.

In (9) the only potentially nonzero gradient entries are now those
of endpoint p_c. But Re p_c=0 both at p_c=0 and at p_c=2*pi*i.
Their weighted contribution vanishes EXACTLY. Therefore

    Im W_m=sum_j epsilon_j D(A_j)                  (11)

even though stationarity in these endpoint variables was not imposed.
The missing equation partial_(p_c)W=0 would have required the paired
position ratio to be one. It is not needed for the following argument.

Differentiate the actual source phase in its two adjacent head
coordinates, using the input or covector orientation as appropriate.
At complete color the two PHYSICAL momenta are

    p_1=p_c, p_2=2*pi*i-p_c,
    B_1=exp(p_c), B_2=exp(-p_c).                   (12)

This formula follows from the retained degree d=N-1, whose leading
affine charge is one. It uses neither partial_(p_c)W=0 nor the
paired position relation z_2=-z_1. At either endpoint, B_1=B_2=1.
For finite nonzero physical positions, the actual complete generators

    K=-B^(-1), f=(1-B)z, e=z^(-1)(B^(-1)-1)

give K=-1, e=f=0 and hence G=-I on both incident heads. Their
based meridians are also central, so their paired cap product is I
regardless of the position ratio.

The other stationary equations give the actual Hurwitz transport;
the remaining interior caps give their ordinary inverse-meridian
relations. Thus these data still define the knot representation.
For a ONE-component knot, all oriented meridians are conjugate up
to inverse. One central meridian makes every PSL_2 meridian the
identity; the Wirtinger generators then make the entire PSL_2
representation trivial. Its volume is zero, as is its marked
fundamental Bloch regulator. This last assertion can also be checked
without choosing eigenflags of a central matrix: every physical
Gauss meridian then has clocks A=B=1 and e=f=0, so C_+=C_-=1
in the original five-argument coefficient symbol. Every one of its
Bloch--Wigner arguments is 1 and contributes zero, by the continuous
normalization D(1)=0. The exact nine-to-five regulator identity gives
the same zero in every regular continuation. Equations (8) and (11) prove

    Im W_m=0                                       (13)

on every such regular cap-endpoint stationary stratum. The proof
allows simultaneous endpoints and any number of remaining interior
caps. In charts where centrality forces an atomic degeneration,
there is no regular solution; no singular extension is being claimed.
The ordinary-cap integrated source can still cancel exactly, as in
K_N(Q^(-1))=0. This is a bound on stationary VALUES, not a claim
that the corresponding integrated source coefficient is nonzero.

## 6. Exact critical degenerations are safe; arbitrary boundary strata are not covered

An EXACT sequence of full regular critical points obeys (10)
pointwise even if its coordinates, frames or matrices escape.
Every finite limit of its imaginary critical values still lies
in [-Vol(M),Vol(M)]. The bounded continuous Bloch--Wigner
function also extends to the degenerate shape values 0,1,infinity
by zero, so exact critical degenerations do not create a larger
regulator value. No compactness of the representation matrices
is needed for this statement.

An approximate logarithmic gradient tending to zero at infinity
is weaker. Equation (9) has the weight Re Z; its error need not
vanish unless the weighted residual does. Moreover approximate
primitive gluing equations at infinity need not approach the
saturated closure of their exact representation scheme. Neither
claim follows just from polynomiality or local Zariski rigidity.

A singular or escaping cap endpoint, a ray endpoint, or another
critical point of a boundary restriction may have fewer equations
than a full critical point. Outside Section 5 it cannot be declared
a knot representation using (10). The
[Markov ray normalization example](actual_markov_ray_normalization_and_pruning.md)
further shows why some equal-exponent boundary pieces must first
be grouped by exact operator identities rather than assigned a
strict gap individually.

Thus (10) closes the regular critical-VALUE part of the desired
sharp upper bound. To conclude limsup N^(-1)log|K_N|<=Vol(M)/(2*pi),
one still needs a source-preserving global stationary/compactification
theorem placing every unpruned contributing asymptotic stratum
under this bound, or cancelling/eliminating the remaining strata.
The present proof does not assert that last theorem.

## 7. A whole-source quantitative cutoff at very deep zero ends

There is a separate global tail estimate directly from the EXACT
scalar flow cycle. It applies to every fixed original word, before
or after a valid normalization-cell pruning. Retain its external
line chi_(beta,N) explicitly. Let T_N(delta) denote the sum of the
ABSOLUTE integrals over all circle/ray components on which at least
one radial coordinate lies in 0<r_j<delta. There are constants
C,B,L depending on the fixed word and fixed compact cap paths, but
not on N or delta, such that for 0<delta<=1/2,

    T_N(delta)<=|chi_(beta,N)| C N^B exp(CN)
                                 delta(1+|log delta|)^L. (14)

Here is the proof. The source-faithful LP radius bound is
N^B exp(CN(1+sum|xi|)) product_radial r_j^(-d).
The EXACT shifted full-Psi ray measure has modulus
sqrt(1+r_j) r_j^(N-1)dr_j/(2*pi). Since d=N-1, the powers
cancel exactly. With interval cap sources only a fixed power of
1+sum|log r_j|+sum|xi| remains. In particular this cancellation
retains the affine +1; replacing d by N would lose the conclusion.

The full-Psi factors on the finitely many fixed outer circles have
a coarse uniform bound exp(CN), with a possible harmless fixed
power of N. One elementary justification uses the compact
finite-product estimate (7b)-(7c) on two vertical logarithmic lines
Re z=+/-L away from zero. It extends along those lines through
the ends of a full turn, because their nonzero real parts keep the
regularized summand away from its other poles. The exact real-axis
moduli (10) and top-turn monodromy bound the two horizontal sides.
The maximum principle on the intervening rectangle then gives the
same exponential bound on every required circle. Lower-half lifts
introduce only the retained factor 1-t^N, again at most exp(CN)
on a fixed circle. Thus this is a bound for the actual full
functions, not an assumed endpoint-uniform small-disk asymptotic.

The normalized Gaussian integral of
exp(CN sum|xi|-N||xi||^2/2), with a fixed polynomial in |xi|,
is bounded by exp(C'N) times a fixed polynomial in N. Finally

    integral_0^delta(1+|log r|)^L dr
                           <=C_L delta(1+|log delta|)^L.

Integrate the other radial variables on (0,1], whose corresponding
logarithmic moments are finite; any fixed exterior segments are
absorbed in the exp(CN) constant using their retained radial powers.
Take the finite union over j.
This proves (14), including all original coupled sources and all
matched relative components.

In particular, with delta_N=exp(-aN),

    limsup N^(-1)log[T_N(delta_N)/|chi_(beta,N)|]
                                                <=C-a. (15)

Taking a sufficiently large fixed a makes this tail exponentially
small at any prescribed finite scale. This does not prove the sharp
upper bound: the retained region r_j>=exp(-aN) still permits
logarithmic head coordinates of order N, and layers such as r~1/N
remain. The same-volume normalization rays are compatible with
(14). Neither fixed-domain compactness nor domination by the regular
critical values follows from this cutoff alone.

## 8. Literature coverage only

The representation-volume inequality and stronger rigidity statements
are established territory; see the abstract of
[Francaviglia, Hyperbolic volume of representations of fundamental
groups of cusped 3-manifolds](https://arxiv.org/abs/math/0305275).
The independently supplied argument above is not a novelty claim for
that inequality. Its role here is to justify its application to the
actual nine-atom period and its retained integer cut marks without
assuming a published proof. No proof technique from that paper was
used as an input to this derivation.
