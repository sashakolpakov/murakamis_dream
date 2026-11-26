# The joint geometric packet at a regular framing endpoint

Private written proof, 18 November 2026.

A regular finite framing endpoint has a correlated occupation
profile. Its vanishing wire clocks are linear in the same framing
coordinate; the compatible physical Euler interactions are quadratic.
The endpoint transfer variables remain discrete on the resulting
\(\sqrt N\) head scale. They must be kept as the actual finite Euler
blocks, rather than included in an independent Gaussian hypothesis.

Below we construct the analytic neighboring integrand by exact head
gauges and cancellation of endpoint factorials. No noncaustic
environmental principal minor is assumed: all remaining integration
variables are kept together. Their quadratic form, after including
the zero Euler symbols, is the original linearized geometric
generating network. Its sole null direction is the framing direction.
The finite projector/path functional remains at the physical faces.

This is a local source construction on specified charts and supplied
local normal chains. It does not identify the whole neighboring
matrix entry with its local piece, place the original relative cycle
there, or estimate complementary long-transfer and framing strata.
The complete directs are A, T, E, F, S and L, pinned below.

## 1. Endpoint chart, logarithms, and the finite source being retained

Fix the complete geometric holonomy and E's positive gluing
certificate for the chosen braid. Choose L's generic complex-binomial
cut parameter \(\theta\), arbitrarily close to \(1/2\), and put
\[
 c_0=2\pi i,\qquad h=c_0/N,\qquad s=e^{-c_0\theta}-1.
 \tag{1}
\]
Let \(r_*\) be a finite framing puncture at which all actual stage
prefix minors remain units. The cut clock is nonunit and unchanged.
S proves that all clock-one wires at this puncture have the same
physical type: either \(e=0,f\ne0\), or \(f=0,e\ne0\).

All logarithms are recorded. L supplies compatible principal
endpoint charts with the cut logarithm preserved: at a row-type
puncture the unit-edge logs have base value zero; at a column-type
puncture the unit wire logs have base value \(c_0\), and the unit
transfer logs have base value zero. Here is the integer point. Split
crossings into their two visits and keep the directed transfer
edges; the wire edges form the single oriented knot cycle.
Let \(I\) be the edges with clock one. Start with their holomorphic
logs of value zero, and choose arbitrary logs on the other edges,
with the specified cut log. The vertex defects are \(c_0k_v\),
with integers \(k_v\). In each component after deleting \(I\),
their sum is zero: its boundary-edge logs have value zero at
the puncture. A spanning forest in that component repairs the
defects by integer edge shifts, by leaf elimination.

The cut is not a bridge of its complementary component. If it
were, multiplying the clock-conservation rows on one side
would force its clock to be one, since all other boundary
edges belong to \(I\). The repair forests may therefore avoid
the cut. To obtain the column assignment, add \(c_0\) times
the knot circulation, which is one on wires and zero on transfers,
and subtract a complementary integral circulation with cut
coefficient one. Such a circulation exists because the cut is
not a bridge in the complementary graph. This preserves the
cut and supplies exactly the column base values.
The same constant integer shifts repair the holomorphic logs
nearby, since their defects are locally constant integers.
The unit-edge logs remain near their prescribed base values,
not identically equal to them.

This principal log choice does not reset an upper physical head
to a lower one. In the finite source an upper occupation remains
\(d-k\), \(d=N-1\), and its exact clock is \(Q^{-1-k}\).
Its upper monomials, Fourier characters, projector kernels,
and quantum/meridian normal rows are retained. An actual
transfer near \(N\) is not turned into a small transfer by
subtracting a logarithmic period.

The same fixed generic complex cut supplies a buffered regular
chart for every factorial argument surviving the cancellations
below. L proves this simultaneously on all usable finite endpoint
branches. On each such branch the prefix minors are affine in
\(s\); every constant wire or transfer clock is exactly one.
All remaining clocks can therefore be put off the unit circle
by the single generic cut choice. Their normalized marked lengths
have nonzero imaginary part, unchanged by any integer log repair,
and lie in fixed compact subsets of
\[
              {\cal D}=\mathbb C\setminus
                         ((-\infty,0]\cup[1,\infty)).
 \tag{2}
\]
Nonzero clock alone would not prove this condition. It is L's
simultaneous off-circle selection, followed by shrinking the
finitely many endpoint neighborhoods, that supplies the buffer.
The cut variation cost \((|\theta|+|1-\theta|)^{N-1}\) and its
marked commutator current are retained. Its exponential rate
can be made arbitrarily small, but is not set to zero.

## 2. Simple wire contacts and the actual compatible gauges

F and S give the uncancelled wire wall
\[
 A_j-1=-\frac{s(\alpha_ra_j)(b_j^tP_{j-1}v_r)}{Q_{P_j}},
 \quad
 v_r=(r,s)^t,\quad \alpha_r=(1,(1-r)/s).
 \tag{3}
\]
At a finite prefix-unit root the two affine factors cannot
both vanish, and the vanishing one has nonzero derivative.
Thus, writing \(z=r-r_*\),
\[
                         A_j=1+\lambda_jz+O(z^2),
                              \qquad \lambda_j\ne0.
 \tag{4}
\]
The complete physical identity is
\[
                         e_jf_j=(A_j-1)^2/A_j.
 \tag{5}
\]
If \(f_j\) is a unit, \(e_j=\lambda_j^2z^2/f_j(r_*)+O(z^3)\);
if \(e_j\) is a unit, the analogous formula holds for \(f_j\).
This is quadratic contact, not a simple zero of the physical
nilpotent entry.

Use T's exact gauges
\[
 G_F=\operatorname{diag}F_a,\qquad
 G_E=\operatorname{diag}H_a^{-1},\qquad
 H_a=\prod_{\ell=1}^a(MQ^{-\ell}-M^{-1}).
 \tag{6}
\]
They give, with the actual zero extreme arrows,
\[
 G_F^{-1}FG_F=S_+,\quad
 G_F^{-1}{\cal E}G_F=\beta_aS_-,
 \qquad
 G_E^{-1}{\cal E}G_E=S_-,\quad
 G_E^{-1}FG_E=\beta_{a+1}S_+,
 \tag{7}
\]
where at completeness \(\beta_a=(1-Q^a)^2/Q^a\).
Their principal momentum coordinates are
\[
                  p_F=1/f,\qquad p_E=e.
 \tag{8}
\]
Indeed the original symbols are
\(e=(A^{-1}-1)p,\ f=(1-A)/p\); the gauge identities (7)
give (8). These are regular Darboux charts when the displayed
physical entry is a unit. For example
\(d\log A\wedge d\log p=-d\log A\wedge d\log f\)
on the \(F\)-chart; the extra differential of
\(\log(1-A)\) wedges to zero.

Thus use \(G_F\) at an \(e\)-zero wire and \(G_E\) at an
\(f\)-zero wire. The opposite gauge need not have a bounded
geometric momentum, even though its finite matrix exists.
Upper gauges retain their exact full-head factors \(F_d,H_d\);
none is normalized away. The gauge changes are made on the
whole network with their inverse neighboring factors.

## 3. Extracting all zero Euler blocks makes the environment analytic

Write every signed crossing in its literal order from A/T:
its flip, Cartan diagonal and common scalar, followed or
preceded by its specified Euler factor or inverse. At the
puncture extract every Euler factor whose physical interaction
vanishes. The negative factor uses its actual reversed order
and its Cartan-dressed interaction. S proves that each such
interaction has exactly one quadratic zero.

For a remaining nonzero interaction, its donor \(e\) and
recipient \(f\) are units. Choose \(G_E\) on that donor and
\(G_F\) on that recipient. Exactly, its Euler matrix becomes
\[
                       \Theta_N(S_-\otimes S_+)
                  \quad\hbox{or its literal inverse}.
 \tag{9}
\]
Thus its coefficient contains only the transfer factorial
\(F_n^{-1}\), not endpoint head factorials. The Cartan
diagonal commutes with these diagonal gauges; the flip
transports the two gauges to the correct output heads.

At a clock-one wire shared by two remaining crossings,
both require the same gauge. Otherwise one would require
its vanishing physical entry to be a unit. At an incident
extracted crossing choose the same physical-unit gauge (8).
Consequently the gauge transition at every clock-one wire
is the identity. At every other wire keep its exact
transition, a quotient of the \(F_a,H_a\) factors in (6).
By (2), their arguments are regular.

This proves cancellation of endpoint factorials in the
remaining environment, as an identity of finite products.
It is not a claim that separate singular factors can be
discarded from a closed source. All gauge matrices at
exposed ports, all original cut/pivotal factors, and all
finite projector and interface rows are retained.
The same cancellation follows for inverse crossings by
inverting the exact gauged factorization, not by changing
only the sign of its principal phase.

Let \(\boldsymbol n\) be the actual small transfers in the
extracted blocks, and set \(\boldsymbol\nu=h\boldsymbol n\).
Use \(h\) times the cut and all remaining integer transfers
as variables \(y\), with their recorded constant logarithmic
periods. Before scaling, the single knot traversal reconstructs
every wire as an integer affine form in the chord occupations.
After scaling it is affine in \((y,\boldsymbol\nu)\), with
the actual upper \(d=N-1\) offsets retained. A logarithmic
period change is recorded in this affine formula and its
source character; it does not change a finite head index.
Thus no external occupations are declared independent
unless they are independent on this actual matching lattice.

A's finite-product theorem now applies uniformly to the
remaining summand, even when the exposed endpoint
occupations tend to their walls. After keeping its exact
occupation-independent scalar line \(\Gamma_N\), it has
the form
\[
 I_{{\rm env},N}(y,\boldsymbol\nu)=
 \Gamma_N N^\alpha a(y,\boldsymbol\nu;h)
                      e^{S_{\rm env}(y,\boldsymbol\nu)/h},
 \qquad
 a=a_0+O(h),\quad a_0\ne0.
 \tag{10}
\]
Here \(I_{{\rm env},N}\) is the analytic coefficient factor
before multiplication by the finite physical/window
indicators. Those indicators are still separate factors
of the exact state sum. Their vanishing is not included
in the assertion that \(a_0\) is a unit.
The functions are holomorphic on a fixed neighborhood
of \((y_*,0)\); all fixed derivatives of the error are
uniform on smaller neighborhoods. The exponent \(\alpha\)
is the half-count of the surviving signed factorials,
with the unchanged measures accounted for when integrated.
\(\Gamma_N\) is their actual remaining scalar product,
including full upper gauge factors where present, not a
freely chosen normalization.

The finite array is the input to (10). The analytic statement
uses only the surviving arguments satisfying (2). It does
not analytically continue a noninteger occupation through
an uncancelled factorial wall.

The corresponding exact closed-normal identities are still
identities of the full gauged arrays. Their top arrows
\(\delta=1-Q^N\), \(MQ^{-N}-M^{-1}\), the cut, Cartan and
pivotal derivatives remain before specialization.
Equation (10) is the central-root asymptotic statement.
It is not permission to differentiate a root identity after
deleting those normal walls.

## 4. The neighboring transfer character is obtained before integration

The geometric matching at the puncture gives
\(\partial_y S_{\rm env}(y_*,0)=0\), with its full retained
Fourier correction. Indeed each extracted Euler graph is
the identity in value there, all gauged momenta are units,
and the remaining canonical matching is the original one.
No stationary integration of the environment alone is used.

Taylor expansion of (10) at fixed \(y\) gives, for each
fixed transfer vector,
\[
 \frac{I_{{\rm env},N}(y,h\boldsymbol n)}
      {I_{{\rm env},N}(y,0)}
   =\prod_i\zeta_i(y)^{n_i}
          \exp\{O(h|\boldsymbol n|^2)\}(1+O(h)),
 \quad
 \zeta_i(y)=
        \exp\{\partial_{\nu_i}S_{\rm env}(y,0)\}.
 \tag{11}
\]
The actual endpoint ordering in this derivative is the
reverse matrix pairing with the Euler block: for one
positive factor it is
\(E[(a,b),(a-n,b+n)]\). The generating correspondence
therefore identifies \(\zeta_i\) with the gauged donor
momentum divided by the gauged recipient momentum.
All Cartan, pivot, cut and Fourier terms are already in
\(S_{\rm env}\); no extra momentum logarithm is added later.

On every same-collar range
\(|\boldsymbol n|\le C\sqrt N\), the ratio in (11) is bounded
by \(C D^{|\boldsymbol n|}\), uniformly on a smaller
neighborhood. The phase has a fixed Lipschitz bound and
\(|h\boldsymbol n|=O(N^{-1/2})\); the amplitude and its
reciprocal are bounded. This estimate does not require
an invertible Hessian of \(S_{\rm env}\).

Put \(S_*=S_{\rm env}(y_*,0)\). With
\(y=y_*+N^{-1/2}w\), on each fixed compact \(w\)-set,
\[
 \frac{I_{{\rm env},N}(y,h\boldsymbol n)}
 {\Gamma_NN^\alpha e^{S_*/h}}
 \longrightarrow
 a_0(y_*,0)
 \exp\!\left\{\frac1{2c_0}w^tH_{\rm env}w\right\}
                     \prod_i\zeta_{i,0}^{n_i},
 \tag{12}
\]
for fixed \(\boldsymbol n\). Here
\(H_{\rm env}=\partial_y^2S_{\rm env}(y_*,0)\) may be
singular. Formula (12) is an actual integrand statement,
not an assumed Gaussian neighboring matrix coefficient.

## 5. The joint interior quadratic form and the framing null direction

For a row-type puncture use \(G_F\) on its wall wires;
for a column-type puncture use \(G_E\). The quadratic
coefficient of each extracted transfer generator is read
directly from (7). If the physical endpoint distance
is \(a=\sqrt N x+O(1)\), then
\[
                    \beta_a/h\longrightarrow c_0x^2.
 \tag{13}
\]
The actual \(+1\) in a recipient coefficient and the
upper endpoint \(d=N-1\) stay in the finite formula.
They do not change (13). Unit shifts still have their
literal zero extreme arrows.

Let \(t_i(w)\) be the resulting quadratic transfer coefficient
including its unchanged regular-head factors. Then
\[
                \zeta_{i,0}t_i(w)=X_{i,2}(w)/c_0,
 \tag{14}
\]
where \(X_{i,2}\) is the quadratic part of the corresponding
physical Euler interaction in these coordinates. For example,
if \(A_1=1+\lambda z+\cdots\), \(f_1,f_2\) are units,
\[
 X=e_1f_2=\frac{\lambda^2f_2(r_*)}{f_1(r_*)}z^2+O(z^3).
 \tag{15}
\]
In \(G_F\otimes G_F\), the transfer coefficient is the
donor \(\beta\), and the momentum ratio is \(f_2/f_1\);
this proves (14) with the actual source gauges.
The column case is identical with \(e_1/e_2\).
An inverse Euler factor has its literal sign
\(\varepsilon_i=-1\); a positive one has
\(\varepsilon_i=1\).

For fixed transfers the finite Euler coefficients, including
their ordered shifted inputs, converge to
\(\prod_i\varepsilon_i^{n_i}t_i(w)^{n_i}/n_i!\).
T's global factorial majorant and (11) dominate their sum
by a product of exponential series. Wherever every fixed
transfer path stays in the interiors of its retained
intervals, the joint interior profile is consequently
\[
 a_0(y_*,0)\exp\!\left\{\frac1{2c_0}w^tH_{\rm joint}w\right\},
 \qquad
 H_{\rm joint}=H_{\rm env}
                         +\sum_i\varepsilon_i\,\operatorname{Hess}X_{i,2}.
 \tag{16}
\]
The statement is before any integration. There is no
separate environmental normal determinant in (16).

Here is why this is the actual geometric quadratic form.
In the regular physical Darboux coordinates (8), a zero
interaction \(X\) has \(dX=0\) at the wall. Its quadratic
term is independent of momentum variations: its unit
momentum factors are evaluated at the reference point.
Its first-order canonical map is therefore position
identity and the momentum shear generated by \(X_2\).
This also follows directly from the leading finite
shift series above. Its position-transfer variation is
zero. Replacing that vertex by its shared positions and
this quadratic shear gives exactly its full linearized
canonical graph, not merely its value at the puncture.

Every other vertex retains its regular gauged generating
graph. The flip and Cartan quadratic forms were left in
the environment. For the linear calculation, set the
zero-transfer variations to zero and delete those
transfer edges from the expanded matching graph. Its
oriented knot wire cycle still connects all visits.
The independent position variables are exactly the cut
and the remaining transfers used in \(y\).

Introduce momentum variations on the visits of this graph.
The derivative of each local quadratic form is its
outgoing-minus-incoming momentum row, including the shear
just computed at the corresponding wire visits. A functional
annihilating the incidence kernel is an incidence
coboundary: this follows by solving its edge potentials
along a spanning tree and testing each remaining chord.
Connectedness makes the vertex potentials unique modulo
one common constant. Thus stationarity of (16) is
equivalent to all linear momentum-matching rows, with
exactly the original common-momentum ambiguity. Its kernel is
the original linearized braid-fixed scheme with its
soft-cut row, modulo the same one common momentum.

E's fixed-trace rigidity applies in these noncentral
physical charts. The cut clock and its selected flag
remain regular; its entropy Hessian is nonzero. It fixes
the cut direction, leaving exactly the framing tangent.
Consequently
\[
            \ker H_{\rm joint}=\mathbb C\kappa,\qquad
            \kappa=\left.\frac{dy_{\rm geom}}{dr}\right|_{r_*}.
 \tag{17}
\]
The vector is nonzero, since every vanishing wire is a
local coordinate by (4). This argument concerns the joint
quadratic form. It does not infer that any chosen principal
minor of \(H_{\rm env}\) is invertible.

Choose a linear complement to \(\kappa\), and write
\(w=\kappa R+LY\). Then (16) is Gaussian only in \(Y\);
it is constant in \(R\). For two observed endpoint
occupations, let \(\ell_j\) be the linearized normalized
physical endpoint-distance form in \(y\) at \((y_*,0)\):
the lower distance is \(a_j/N\), the upper distance is
\((d-a_j)/N\), with its exact \(d=N-1\) offset retained
before taking the linearization. Thus a logarithmic
wire coordinate contributes \(1/c_0\) at a lower end
and \(-1/c_0\) at an upper end. Their leading distances
on the \(\sqrt N\) scale have projection
\[
 \binom{x_1}{x_2}
       =\binom{\ell_1(\kappa)}{\ell_2(\kappa)}R
                       +\binom{\ell_1(L)}{\ell_2(L)}Y .
 \tag{18}
\]
Thus the profile is the pushforward of a flat framing
direction and the joint normal Gaussian, with the actual
finite restrictions. It is not two independent positive
occupation Gaussians. A supplied descending normal chain
may be used for \(Y\); no such chain is assigned to the
original state by this calculation.

## 6. The envelope term and the compensating environment phase

The transfer character in (11) is essential in interpreting
flatness. For one block let \(\nu=hn\), and let \(a(u)\)
be its gauged transfer weight before the character.
Near a compatible quadratic wall, \(a=O(z^2)\).
The literal positive coefficient can be written
\[
 \frac{(-1)^nq^{n^2}}{F_n}
 =\frac{h^{-n}}{n!}
       \exp\!\left\{\frac{hn^2}{2}
        -\sum_{k=1}^n\log\frac{e^{hk}-1}{hk}\right\}.
 \tag{19}
\]
This fixes its entropy branch and its value one at \(n=0\).
Its classical transfer phase, including the ordered
input shifts of \(a\), is
\[
 \nu\{\log a(u)-\log\nu+1\}
                         +O(\nu^2/|z|)+O(\nu^2).
 \tag{20}
\]
The first error comes from varying a quadratically
vanishing weight over an occupation displacement \(O(\nu)\);
on the geometric blowup \(\nu=O(z^2)\) it is \(O(z^3)\).
The last exponent in (19) begins at order \(\nu^2\).
These estimates follow either by its finite-product
principal integral or by Taylor expansion of the analytic
weight ratios after setting \(\nu=z^2v\).

The environment supplies, in the actual endpoint order,
\[
 S_{\rm env}(u,\nu)=S_{\rm env}(u,0)
                         +\nu\log\zeta(u)+O(\nu^2).
 \tag{21}
\]
The stationary envelope therefore has
\(\nu=a\zeta(1+O(z))\), and its value is
\[
             S_{\rm env}(u,0)+a(u)\zeta(u)+O(z^3).
 \tag{22}
\]
The term \(\nu\log\zeta\) has been included, not dropped
as a Legendre boundary term. Integer Fourier changes are
kept in both marked logarithms in this calculation.
The \(n=0\) value fixes the additive constant.
For finitely many zero blocks the same calculation gives
the sum of their signed quadratic terms; changes of
ordered inputs affect only degree at least three.

Along the geometric framing curve the full corrected
phase is constant. Thus the diagonal environment
quadratic form restricted to \(\kappa R\) is exactly the
negative of the Euler quadratic contributions in (16).
This is the compensation seen in the actual joint
profile. It is not obtained by subtracting a scalar
dilogarithm from an unrelated stationary action.

## 7. Physical faces and what is still not a whole-source theorem

The interior exponential in (16) is not asserted on every
microscopic face. A unit shift \(S_+\) still vanishes at
its finite upper row, and \(S_-\) at its lower row.
At a fixed finite endpoint distance, some fixed transfer
paths are absent even though their unrestricted limiting
quadratic coefficient is nonzero. The exact finite path
indicators and shortened Fourier sums must then multiply
the coefficients in (12)--(14) before summation.

For each interval \(I=[L,U]\) this is precisely the
retained finite projector
\[
             N^{-1}t^L K_{U-L}(t),\qquad
                         K_R(t)=\sum_{a=0}^R t^a .
 \tag{23}
\]
Neither its upper monomial nor its endpoint value is
replaced by a delta. The local packet at such a face is
the resulting finite-path/Poisson boundary functional
paired with (12). It need not be the interior exponential.
All interface and normal currents of the original
finite factorization remain.

Only single-interval, small-transfer blocks are used in
the uniform estimate. Opposite-collar transfers near
\(n=N\), unions of upper and lower collars, prefix-zero
punctures and \(r=\infty\) remain separate source terms.
A principal logarithmic repair does not remove them.

Finally the construction has produced a neighboring
analytic integrand and its local joint normal family.
Integrating it on a supplied compact local chain gives
a local contribution of the original interpolated source.
It is not an equality between that contribution and the
entire neighboring finite matrix entry. No global
geometric coefficient, endpoint noncancellation,
framing period or scalar lower bound has been inferred.

## Complete proof-source pins

* A: notes/research_literal_crossing_slit_chart_amplitude.md,
  SHA256 c3682b0f84000aad4c2f53235b9c93bbd86283905a75d6f07ac03b1a3c00bc4a.
* T: notes/research_actual_compressed_endpoint_euler_transition.md,
  SHA256 9c735f005fa94afe56931af5fc0cb77ee95849a9c4c89067290711135ad1ed16.
* E: notes/research_soft_cut_morse_bott_density.md,
  SHA256 e411f25c7b66b61d865427db1e1f789aeb09b9c76471a303dfdb8d7673fe6f9a.
* F: notes/research_actual_facet_seams_and_geometric_boundary.md,
  SHA256 ac250fc87e7bf1d4f6851c346ef08f7cd08d9e4566d1283981c03dee2427441c.
* S: notes/research_soft_cut_separates_regular_endpoint_types.md,
  SHA256 935f6d97b9ca3a068412b33075610d17e0a571f68f2bc2925eac70c0480a2555.
* L: notes/research_regular_endpoint_logarithms_and_slit_chart.md,
  SHA256 dc340b9beef5dcdc2a01a35030515cc36cf5e6a6babad66b3fce03351817dc7b.

All six complete sources were freshly read nontruncated in this
active author sequence; E was also reread in full after the joint
draft was written. Every used implication was checked. The proof
uses only written mathematics and text/hash operations. Frozen
and public files were not changed.
