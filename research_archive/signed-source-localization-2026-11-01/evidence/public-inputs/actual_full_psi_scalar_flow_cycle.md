# An absolute scalar full-Psi cycle for the original whole source

28 October 2026. The actual physical word, its continuous Gaussian
factors and ALL original cups/caps admit one explicit scalar relative
period using the full literature dilogarithm. No finite matrix
resolvent or finite Euler polynomial is present. The missing analytic
step in combining coefficient moments with the untruncated scalar
Hardy network is supplied by a continuous-flow duality lemma: its
fibered head radii make every retained radial source absolutely
integrable, jointly with the Gaussian and the coupled caps.

This does not justify bare substitution of Psi for the cyclic function
on fixed Laurent tori. The radial chains below are compulsory. The
regular all-moment-pole action has the actual meridian/cap equations;
the whole relative cycle's geometric intersection and dominance remain
unproved. An artificial exponential gap for every individual ray term
is specifically not asserted.

The [rational audit](../experiments/audit_actual_full_psi_scalar_flow_cycle.py)
and [certificates](../experiments/actual_full_psi_scalar_flow_cycle_results.json)
check 189 individual all-N atom capacities before and 189 after the
Hardy-forest contraction, and 25 whole-network primal/dual radius
solutions, with rational checks of every constraint
and exact objective equality after recovery. These audit the general
flow proof below; they are not a knot-family proof by examples.

## 1. The actual scalar kernels to which the theorem applies

Subsequent exact simplification:
[the cut-wall pushforward](actual_full_psi_cut_wall_pushforward.md)
removes the remaining moment resolvents in favor of a bare full-Psi
head period PLUS its explicit aggregate scalar cut-wall current.
Every original radial source is retained by that identity; the
current's global growth and geometric selection remain open.

Use the strict original physical crossing order in
[the literal Euler network](actual_euler_gaussian_cauchy_network.md),
the [continuous Gaussian](actual_continuous_gaussian_cyclic_network.md),
and the original physical boundary sources in
[the coupled-cap theorem](actual_coupled_caps_interval_source.md).
Insert scalar Hardy identities before/after elementary gates, in the
same harmless initial chamber as before. All head variables are z_v.

Each scalar atomic kernel is a positive/negative Euler coefficient
generating kernel with a monomial argument. All can be expressed using
v_(epsilon,N), with epsilon=+1 or -1:

    v_N(A)=v_(+,N)(A),
    u_N(A)=v_(-,N)(Q^(-1)A),
    F^(-1) diagonal: v_(-,N)(Q^(-1)z/w),
    F diagonal: N(z/w)^d v_(+,N)(Qw/z), d=N-1.       (1)

Thus a moment atom has argument A_j=kappa_j z^(v_j), where v_j has
one +1 and one -1. The reflected factorial also has its original
prefactor N(z/w)^d. The Q shifts are exact. Gaussian dilation kernels
are ordinary Hardy kernels with coefficient

    g_s(x,y,xi)=-(xy)^(-s)exp(-s h/2)
                         exp(sqrt(pi)(1+i s)xi),
    h=2*pi*i/N, s=+1 or -1.                         (2)

They carry the exact Gaussian weight sqrt(N/(2*pi))exp(-Nxi^2/2).
Every other spectator/reset is 1/(1-z_out/z_in).

The physical cup/ordinary cap/original marked cap are exactly (4) of
the coupled-cap note, including their distinct powers of N and color.
The full marked row is restricted to D=d only by whole integer degree,
as proved there; no Ward identity is reapplied to a summand.

## 2. Full-function moment chains, with no finite resolvent

Let Psi_epsilon be precisely the full rational Faddeev function fixed
in [the full-function source theorem](actual_modular_dilog_circle_and_boundary_source.md).
For R>0 define the scalar functional

    M_(epsilon,R)[f]=
       (1/(2*pi)) integral_(-pi)^pi
          Psi_epsilon(log R+i epsilon theta)
                         f(R exp(i epsilon theta)) dtheta
       -epsilon/(2*pi*i) integral_0^R
          Psi_epsilon(log r+i epsilon pi)(-r)^N f(-r) dr/r.    (3)

The indicated logarithmic lift on the negative ray is retained.
For every 0<=a<N, the independently proved shifted-keyhole identity is

    M_(epsilon,R)[t^(-a)]=v_(epsilon,a).             (4)

On its negative ray, exactly

    |Psi_epsilon(log r+i epsilon pi)|=sqrt(1+r).     (5)

In the scalar network replace every v_(epsilon,N)(A_j) by the moment
kernel

    M_(epsilon,R)[1/(1-A_j/t_j)].                   (6)

Expression (6) is NOT defined as a standalone function with a fixed
head-variable circle on its radial piece. Its meaning is the jointly
fibered scalar cycle specified in Sections 4--5. The untruncated
geometric kernel has no numerator 1-(A_j/t_j)^N and no matrix source.

## 3. Coefficient-independent continuous support

Expand every ordinary Hardy kernel in nonnegative powers. A reflected
factorial contributes diagonal index a=d-r, r>=0; a following Hardy
identity forces a>=0. Hence it retains the upper barrier a<=d, entirely
independently of the numerical coefficient assigned to r.

The complete strict crossing has the following ordered barriers.

* In C^(-1), its transfer lowers head one. Its following reciprocal
  first-head diagonal therefore sees an index at most d. The reflected
  second-head diagonal kills a second-head overflow before the central
  transfer.
* The central transfer only lowers head two and may overflow head one.
  The reflected first-head diagonal of the final C kills this overflow
  BEFORE its lowering transfer can return it.
* The final transfer lowers head one; the final reflected second-head
  diagonal kills its second-head overflow.

The incoming second-head reciprocal diagonal of each inverse fusion
sees the finite incoming head. All Gaussian indices are likewise in
[0,d]. Every nonzero original whole-source route therefore has

    0<=r_j<=d at EVERY moment atom.                 (7)

This argument uses inequalities and degree conservation only. It holds
for REAL nonnegative flows, not only integer paths, and for arbitrary
coefficient values at the atoms. All intermediate nonnegative head
indices are bounded by the fixed total degree k d of a k-pair plat.
The scalar flow polytope is consequently bounded. Its source cup and
cap variables range over [0,d].
It is nonempty: take every transfer order zero and match the cup and
cap head labels, with the diagonal indices then fixed. Numerical
coefficients of different routes may cancel, but this feasible
nonnegative continuous route exists independently of those values.

## 4. Exact toric-flow duality supplies the joint radii

Write a geometric kernel as 1/(1-exp(ell_e) z^(v_e)). Its v_e is the
incidence vector of an oriented edge: one +1, one -1. Atomic edges
have ell_e=log|kappa_e|-log|t_j|; Gaussian edges include log|g_s|;
other Hardy edges have ell_e=0. Let gamma=d gamma_0 be the total
head-monomial exponent from reflected factorials and the cup/cap
prefactors. A cup/cap K_N is a bounded edge c with index a_c in [0,d]
and log coefficient ell_c. All original scalar factors outside head
monomials are kept separately.

For fixed t,xi choose head log radii lambda_v. Impose the strict
geometric-kernel constraints, for a fixed eta>0,

    ell_e+v_e.lambda <= -eta.                       (8)

There is a common feasible chamber for every positive set of |t_j|:
the previous gate-order reset construction works with its atomic
threshold rho replaced by rho |t_j|. No terminal Hardy edge closes
the time paths. Finite cap polynomials impose no radius constraint.

On this chamber the head source/monomial growth is bounded by

    J(lambda)=gamma.lambda
          +d sum_c max(0,ell_c+v_c.lambda).         (9)

The dual of minimizing (9) subject to (8) is EXACTLY

    maximize sum_e f_e(ell_e+eta)+sum_c a_c ell_c,
    gamma+sum_e f_e v_e+sum_c a_c v_c=0,
    f_e>=0, 0<=a_c<=d.                             (10)

For clarity, the second term of (9) is the support function of [0,d].
Insert a_c in that interval, add the multipliers f_e of (8), and
minimize in lambda; its coefficient must vanish, giving (10).
Strong equality is finite polyhedral duality: introduce u_c>=0 and
u_c>=ell_c+v_c.lambda to make (9) linear. A separating hyperplane
between its attainable objective epigraph and a smaller objective
value gives exactly the nonnegative multipliers in (10). Feasibility
of (8) and boundedness of the continuous route polytope give a finite
attained optimum on both sides. Thus no integer-only inference or
asymptotic convexity is being used.

Every f_e in (10) is precisely a nonnegative head or atom flow of
Section 3. At R=1, put tau_j=-log|t_j|>=0 on radial pieces; tau_j=0
on circle pieces. The moment contribution is sum_j r_j tau_j. By (7),
and since every other flow is at most k d,

    min J <= d sum_j tau_j+C_word N(1+sum|xi|).     (11)

Color moduli on a fixed nonzero meridian chart are included in C_word.
Equation (11) is the required simultaneous bound, rather than a
possibly divergent independent choice of a radius at each atom.

The incidence/capacity matrix and the normalized charges gamma_0
are fixed by the word. An optimal basic solution, after fixing harmless
componentwise radius gauges, has

    |lambda| <= C_word(1+sum tau_j+sum|xi|).         (12)

One can use piecewise affine solutions on their finitely many
polyhedral parameter cells. To obtain a genuine fibered chain, glue
different solutions by log-linear head-radius prisms on cell walls;
(8) is convex, so no pole is crossed. These prisms have zero period:
the scalar form contains ALL base moment/Gaussian differentials, whose
pullback has deficient rank on a base cell wall. Equivalently use a
continuous smoothed choice with a smaller fixed margin; (11) changes
by only C_word N. No source term is lost by the radius selection.

## 5. Absolute convergence, including every original coupled cap

Under (8) every geometric kernel has modulus at most
(1-exp(-eta))^(-1). The bound |K_N(r)|<=N exp(d max(0,log|r|)) is
exactly the source support function already present in (9).
All scalar N powers are the original reflected-factorial and cap
normalizations. Thus the head integrand is bounded by

    C N^B exp(C_word N(1+sum|xi|)) prod_radial r_j^(-d).    (13)

The full-Psi radial measure in (3), using (5), has modulus
sqrt(1+r) r^(N-1)dr/(2*pi). Since d=N-1, its product with
r^(-d) is uniformly integrable at r=0. The circles are compact and
their selected full functions have no poles. The Gaussian weight
dominates exp(C_word N sum|xi|), so all variables are jointly
absolutely integrable at every N. This proves the required Fubini;
it is stronger than declaring a finite matrix-coefficient sum first.

The exact interval sources of the coupled-cap theorem may be included
as well. Choose principal Log r on its cut plane. Uniformly there,
with its removable value at 1,

    |Log r/(r-1)|
       <=C(1+|log|r||) exp(-max(0,log|r|)).         (14)

Near 1 this follows from removability; for |r|>=2 or <=1/2 it is
immediate, and the remaining compact annulus is bounded. On ANY
fixed compact cap path with 0<=Re s<=1,

    |exp(Ns Log r)|<=exp(N max(0,log|r|)+C_path N).

The one power lost in (14) changes N back to d=N-1. Hence the
interval source obeys (13), up to a fixed product of logarithmic
factors bounded by powers of 1+sum tau+sum|xi| using (12). Radial
integrals of those logarithms still converge. Thus the real intervals
and the compact complex cap paths inside the vertical strip have
the SAME absolute convergence theorem. The generic simultaneous
classical framing in the cap note puts all desired s_g in that strip.

Source logarithmic cuts are matched exactly, rather than discarded.
If L changes to L+2*pi*i, the difference of the two interval densities
N L exp(NsL)/(exp L-1) is

    d_s { [exp(Ns(L+2*pi*i))-exp(NsL)]/(exp L-1) }.

The primitive vanishes at both s=0 and s=1. Thus the seam is an exact
relative interval derivative with fixed ends; it produces no extra
period. This is the explicit scalar cut gluing needed when using the
principal source chart in (14).

## 6. Exact equality with the original selected scalar

If the interval presentation is used, first evaluate those intervals
to recover their exact cap polynomials; the joint absolute bound permits
this order. Then integrate the head circles in the convergent chamber. Expansion
of their rational geometric kernels is absolutely convergent. By
Section 3, only indices 0<=r_j<N survive the original source, so this
head integral is a FINITE Laurent polynomial in the moment t_j^(-1).
Apply (4) separately at every atom. Equations (1) recover the original
finite Euler/factorial coefficients exactly, with all Q shifts and N
factors. The joint Gaussian moments give the exact original Gaussian
diagonal. All original Cartan, pivot, framing, modified-trace and
peripheral lines remain attached once.

Consequently, for every fixed signed physical word and its original
selected plat source,

    P_(beta,N)=chi_(beta,N)(N/(2*pi))^(m/2)
       integral_R^m exp(-N||xi||^2/2)
       (tensor_j M_(epsilon_j,1))
       [ integral_head_tori R_(beta,N)(z,t,xi) prod_v dz_v/(2*pi*i z_v) ] dxi. (15)

Here R is the explicitly specified product of ordinary scalar Hardy
kernels, original reflected monomials and the coupled sources, or
their exact interval forms. Its number of variables is determined by
the word and bridge count, independently of N. Equation (15) is a
single tensor-product scalar RELATIVE cycle. Writing it as circle/ray
pieces is optional bookkeeping, not a selection of a new invariant.

In particular no exponentially large unspecified matrix source is
hidden in (15). All possible exponential factors are explicit: full
Psi functions, Gaussian weights, original monomial/interval phases,
and the retained radial powers (-r)^N. Their cancellations are still
part of the original problem.

## 7. What the pole pushforward does and does not prove

The new atomic rational poles are t_j=A_j(z). Each is primitive and
has scalar normal form dt_j/(t_j-A_j). With its induced orientation
its residue is +1; their normals are independent because every t_j
occurs in its own pole equation. The ordinary head Hardy poles have
the already proved forest normal degree +1. At a regular local chart
where these residue operations are allowed, the ALL-CIRCLE atomic
residue branch has density
the product of the full functions Psi_epsilon(Log A_j), with exactly
the original reflected monomials, Gaussian and coupled caps.
The complete relative source also has its retained ray-weighted pole
and cut currents. Its full residue is not being identified with this
single bare-function product.

Using the uniform full-Psi symbol on its selected strip, its leading
action is therefore the SAME signed sum of Li_2 and monomial/Gaussian
terms computed in the Hardy-forest note. The exact Gaussian canonical
graph and the actual fusion graphs give the actual framed Hurwitz
holonomy. The cap equations are precisely the inverse-meridian locus
proved in the coupled-cap note. This is a statement about the regular
all-pole critical scheme, not existence of a global geometric cycle.

The full functions are regular across the apparent interior cyclotomic
roots on their selected strip; a positive geometric argument may have
ANY modulus. Local residue/chart deformations may use that regularity
while retaining every negative-ray and source-cut face in (3).
Enlarging an outer radius is an exact moment-chain deformation, but
its extra ray segment must be kept; for R>1 it need not be small.

The known ordered support theorem can push the HEAD Hardy forest on
every radially truncated cycle r_j>=delta>0, with all source-null
negative currents retained first. Section 8 below proves the stronger
fact that the reduced whole-source flow polytope is unchanged. Thus
the reduced full-source cycle itself has the same absolute radial
bound, without needing a new divergent-piece prescription. This does
not permit deleting atomic ray/cut currents or independently assigning
a period to a divergent separated negative-current component.

Bare substitution remains false. For example the ordinary full-turn
moment at a<N differs from the original v_a by its nonzero radial
source E_a(R). Its small-radius leading term is

    E_a(R)=epsilon R^(N-a)/(2*pi*i*(N-a))+O_N(R^(N-a+1)|log R|).

The logarithmic term t^N Log t has nonzero low Cauchy moments. It is
not an integer high-degree tail annihilated by a head barrier. The
explicit relative cycle (3), plus the flow-controlled radii, is the
proved correction to that substitution. A further global pole
pushforward must transport this whole relative class. Normal degree
one of the all-pole graph does not determine its geometric-thimble
coefficient and does not prove noncancellation of the original period.

## 8. The full-Psi cycle remains absolute after Hardy-forest contraction

Contract all head-Hardy edges at their pole equations, including the
Gaussian edges with their full g factors. Their graph is the forest
already proved in the Hardy-reduction note. In a component, write
z_v=c_v z_root, where c_v is its nonzero product of Gaussian dilation
factors. Every remaining moment argument is still a primitive ratio
of two DIFFERENT retained head segments. A transfer connects different
heads; an active factorial connects the two segments it separates.
Thus no atomic argument becomes a constant self-loop.

There is an exact equality of CONTINUOUS route polytopes:

    reduced atom/cap flows
      <--> original atom/cap/head-Hardy flows.       (16)

Here the reduced constraints only require atom orders nonnegative and
cup/cap orders in [0,d]; omitted head currents are not assumed
nonnegative. To prove (16), first reconstruct the omitted currents as
SIGNED real numbers. On each forest component, the contracted balance
equation is exactly the compatibility condition for a unique solution
of its tree incidence equations; solve from the leaves. These numbers
are precisely the signed head indices in the ordered physical word.

Suppose a reconstructed index first becomes negative. A diagonal
preserves the index, and Gaussian dilation does too, so a lowering
transfer must create it. There are only the following possibilities.

* In C^(-1) it is the first head, whose following reciprocal first-head
  factorial forces the index to be nonnegative.
* In the central transfer it is the second head, which the incoming
  reciprocal second-head factorial of C forces nonnegative before
  another transfer touches it.
* In the final transfer of C it is the first head. At the next touching
  crossing it is either the second head, killed immediately by the
  incoming reciprocal factorial, or the first head, lowered before
  that crossing's reciprocal first-head factorial. An untouched
  negative head is incompatible with the final finite cap.

These are inequality statements for real indices. They do not use
integrality, coefficient cancellation, or a finite matrix norm. The
initial cup and final cap indices are in [0,d]. Hence no reconstructed
negative current is possible. All omitted head currents are
nonnegative and (16) follows. The upper barriers of Section 3 then
give atom order at most d and all head currents at most k d.

The g factors introduce only explicit costs. If delta_v=log|c_v|,
the reduced atomic coefficient log is ell_e+v_e.delta, the source
monomial has its additional fixed term gamma.delta, and a cap edge
has the same substitution. After reconstructing a flow, these costs
sum to the original Gaussian/color costs by the tree balance
equations. Their bound is still C_word N(1+sum|xi|).

Apply exactly the duality of Section 4 to this reduced incidence
matrix, now with ONLY atomic geometric kernels. Equations (11)--(14)
hold unchanged. The graph has b+6m complex head coordinates, its
original m continuous Gaussian variables and its original coupled
sources. It has NO head-Hardy/reset kernels. The pure full-Psi moment
cycle on this reduced graph is jointly absolutely convergent.

For exact equality, perform the original forest annulus argument at
every common radial cutoff delta>0. All nonempty negative-current
components have zero original head/source pairing, by the same
coefficient-independent signed-index proof. The initial and reduced
whole-source cycles both satisfy the absolute bound above, so take
delta to zero in those cycles. No separate convergence of an
individually source-null annulus component is required or asserted.

The audit contracts the literal time-layered head forest, drops ALL
of its nonnegativity constraints, maximizes each reduced atom order,
and reconstructs the unique omitted tree currents exactly. It finds
189 rational all-N certificates with every omitted current
nonnegative, plus ten reduced strict-radius certificates. The proof
(16), rather than those examples, establishes this for all words.
