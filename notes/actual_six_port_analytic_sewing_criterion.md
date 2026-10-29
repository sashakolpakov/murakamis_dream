# Source-exact analytic sewing: the physical interface and the remaining six-port estimate

29 October 2026. This separates an exact original-source fact from an
analytic criterion. Uncrossed sewing of literal physical ports has only
polynomial norm cost. A coherent scalar packet can then be sewn on any
fixed graph, including graphs with cycles, if its JOINT marked phase has
a controlled nondegenerate saddle and a global gap. Local packet gaps
alone do not establish those hypotheses. The genuine six-port source is
known exactly, but its required physical coefficient estimate is still
missing; no broader knot equality is claimed here.

The distinction matters because the
[generic six-port channel frame](actual_six_port_deformable_source_and_recoupling.md)
is source exact only after saturation, and is not known to be tame.
The theorem below does not assume a tame 6j/Smith frame.

## 1. The literal physical interface is polynomially conditioned

Retain N,d=N-1,q,Q,x and the ORIGINAL turns, with |x|=1:

    p_ab=N x^(-b) delta_(a+b,d),
    ell_ab=x^a delta_(a+b,d)/N,
    m_ab=x^b/N^2.

Let U_ab=x^(-b)delta_(a+b,d). Then U is unitary, the cup matrix
is NU, and the ordinary cap matrix is U^(-1)/N. Consequently a
single-leg bend has matrix norm N or N^(-1), with no factorial
conditioning. As flattened tensors their exact Euclidean norms are

    ||p||=N^(3/2), ||ell||=N^(-1/2), ||m||=N^(-1).       (1)

The last equality uses the FULL unrestricted marked row. Its eventual
integer-degree restriction may be made only after the assembled source
forces it. Pivots, literal leg permutations, and genuine dual-object
isometries have norm one. Closing a fixed number of bare wires costs
at most a fixed power of N by finite-dimensional Cauchy.

Thus for any fixed planar port graph G whose crossings and nontrivial
coupons are kept INSIDE its specified blocks, its remaining original
sewing functional satisfies

    |Gamma_N(A_1,...,A_v)| <= N^(C_G) product_i ||A_i||_2.  (2)

This follows by composing the displayed turns and partial contractions;
C_G is independent of N. Formula (2) retains the actual marked row,
all unit characters, and every original scalar normalization. It does
NOT make R or a changed recoupling frame polynomially bounded. A braid
at an interface must be included in a block, or estimated separately.

In particular the exact six-head source can be sewn in its FULL physical
tensor basis without an inverse generic Clebsch minor. Its known
orthogonal projection onto the saturated generic source has norm one.
But neither the reduced invariant lift Phi nor the unspecified generic
channel inverse is thereby proved tame; those are different maps.
Nor does a flat orthogonal projection prove preservation of an
exponentially weighted geometric corridor.

## 2. A quantitative error budget that survives the actual contraction

Suppose an exact physical block is A_i=A_i^0+E_i, where, for fixed G,

    ||A_i^0|| <= N^C exp(N a_i),
    ||E_i|| <= N^C exp[N(a_i-gamma_i)], gamma_i>0.          (3)

Expansion of the multilinear contraction and (2) give the PROVED bound

    |Gamma_N(A)-Gamma_N(A^0)|
      <= N^(C') exp[N(sum_i a_i-min_i gamma_i)].           (4)

If the proposed coherent main signal has rate F, preservation of its
nonzero leading coefficient is therefore guaranteed by

    min_i gamma_i > sum_i a_i-F.                          (5)

One can improve (4) using boundary-dependent profiles and joint maxima,
but one cannot omit the loss sum a_i-F. Relative O(1/N) block errors
do not in general preserve an exponentially smaller closed signal.

For an elementary sharp warning, contract vectors

    A=(exp(Na),exp(Na),1), B=(exp(Nb),-exp(Nb),1).

Their exact pairing is 1. Perturbing the second coordinate of A by
exp[N(a-gamma)] changes the pairing by exp[N(a+b-gamma)].
The contraction itself has norm one. Thus exponential amplification
here comes from coherent cancellation, not an ill-conditioned measure.

The actual source has its own stronger warning: at even N the full
circle satisfies L_N^2=0 although L_N is nonzero. Hence multiplying
nonzero local circle images cannot supply a nonzero sewn density by
itself. This is precisely why the genuine six-port junction cannot be
replaced by Frobenius multiplication or by dephased positive routes.

## 3. A nonzero marked lattice-saddle theorem

Here is a sufficient analytic statement with an explicit noncancellation
proof. After solving the EXACT wire/complement constraints, suppose a
piece of the original scalar is

    S_N=c_N sum_(k in NP intersect (Z^r+sigma_N))
                    a_N(k/N) exp[N Phi(k/N)],              (6)

where P is a fixed compact convex polytope, r is fixed, and c_N is its
original nonzero unit-character/power-of-N line. Affine O(1/N) shifts
from d=N-1 must be retained in a_N or Phi_N, not silently replaced by
their limit. For simplicity (6) displays one exact lattice coset.
For example Phi_N=Phi+Psi/N+O(N^(-2)) changes the leading density to
a_0 exp(Psi); that nonzero normalization factor is part of the answer.

Assume the following on a fixed neighborhood of an interior x_*:

* Phi is C^3 there, a_0 is C^1, and a_N=a_0+O(1/N)
  uniformly, with a_0(x_*)!=0.
* For a RETAINED integer Poisson mark m, grad Phi(x_*)=2pi i m.
* H=-Phi''(x_*) is complex symmetric with Re H positive definite.
* Re Phi has its unique maximum F=Re Phi(x_*) on P; it has a fixed
  gap outside every fixed neighborhood of x_*. The local drop is
  quadratic. Globally |a_N| is polynomially bounded.

Then the whole sum (6), not just its absolute envelope, has

    S_N=c_N exp(2pi i m.sigma_N) exp[N Phi_m(x_*)]
        N^(r/2) (2pi)^(r/2) a_0(x_*)/sqrt(det H)
        (1+O(N^(-1/2))),                                  (7)

where Phi_m=Phi-2pi i m.x. The square root is the continuous Gaussian
branch on Re H>0. In particular its leading coefficient is nonzero.

Proof. On the exact coset the removed mark is the constant phase in
(7). All terms outside a small fixed ball have a uniform exponential
gap. Inside, put t=sqrt(N)(x-x_*). Taylor expansion gives the Gaussian
exp(-t^T H t/2), with an integrable quadratic envelope. Restrict first
to |t|<=N^epsilon, epsilon<1/6; the Taylor error is controlled by the
Gaussian moments and is O(N^(-1/2)) after summation. The complementary
local tail is exponentially small in N^(2epsilon). Gaussian Riemann
sums with mesh N^(-1/2) converge uniformly in their bounded coset
shift to the Gaussian integral, with O(N^(-1/2)) error by integrating
the summable first derivatives over grid cells. That integral equals
(2pi)^(r/2)/sqrt(det H): prove it first for real positive H and continue
holomorphically on the convex domain Re H>0, using the same integrable
bound. This proves (7) without deleting any endpoint residue.

For finitely many lattice cosets or marked sectors, their ACTUAL leading
coefficients must be summed. Individual nonzero coefficients need not
have nonzero sum. The single-coset theorem does not supply that extra
arithmetic/source pairing. The original pretzel proof checks its paired
charges explicitly; the six-port problem must do the corresponding work.

If the saddle is off the original real grid, (7) cannot be applied by
declaring a new contour. One must first prove an EXACT source contour
identity with all side currents retained. On a specified middle-
dimensional contour having a real parametrization, the analogous
continuous Gaussian proof applies to its pulled-back phase and density.
Its Jacobian, boundary gaps and residual source currents are hypotheses,
not consequences of a formal complex Hessian.

### Fixed original normal jets: a uniform packet is the needed input

The [bounded-confluence theorem](actual_six_port_bounded_confluent_blocks.md)
now bounds the actual six-port source clusters by eight and their
required normal coefficient order by a fixed constant (ten coefficients
suffice). This removes an unbounded-order jet problem, but not a
conditioning or nonvanishing problem.

Here is the exact analytic consequence. Let t=zeta-q be the ACTUAL
normal parameter. If a coherent error E_N(t) is holomorphic on
|t|<=r_N, r_N>=N^(-B), and

    sup_|t|<=r_N ||E_N(t)|| <= N^C exp[N(F-gamma)],

then for every fixed j<=J,

    ||[t^j] E_N|| <= N^(C+Bj) exp[N(F-gamma)].             (7a)

This is Cauchy's coefficient formula in any fixed physical tensor norm;
finite dimension does not add an exponential loss. A fixed-pole Smith
regularization uses only finitely many such coefficients, so (7a)
preserves its exponential gap IF its explicit multiplying matrices
have polynomial bounds, or their exponential rates are included in
the budget (5). The bound on cluster size alone supplies neither fact.

The selected leading normal density must also be nonzero. For a scalar
packet exp[N Phi(t)]a(t), any fixed derivative is exp[N Phi(0)] times
an explicit finite Bell polynomial in N and the derivatives of Phi,a.
The original source's specified linear combination of those polynomials
must be shown to have at least a polynomial lower bound. A fixed
derivative order does not prevent that combination from vanishing.
If only a finite inverse-N approximation to a(t) is used, it must be
taken to sufficient order to survive the N^(BJ) Cauchy cost; a pointwise
O(1/N) approximation is not automatically differentiable at that cost.

The [bounded factorial envelope](bounded_normal_quantum_factorial_envelope.md)
controls explicit termwise normal coefficients. It does not imply the
UNIFORM COHERENT disk estimate in (7a). The physical original finite
tangles have their own regular normal family, which must remain the
one used in (7a); a root-only identity or another interpolating germ is
not interchangeable with it. This is a precise analytic target for the
new bounded six-port source, rather than a claim of automatic survival.

## 4. Closure on a fixed graph and the geometric test

Suppose every specified scalar block packet is expressed in its actual
physical boundary labels. After literal sewing, these labels are affine
functions L_i x+b_i of the independent wire coordinates. The total
phase and density are the SUM of block phases and the PRODUCT of their
densities, with the original wire characters included. The integration
domain is the intersection of their actual support domains. In the
real-concave case below this sewn domain is required to be compact and
convex. If its actual support is not convex, a global uniqueness and
gap statement must instead be proved on all its components.

For real concave phases, uniform strict concavity on all free directions
follows from the checkable matrix inequality

    sum_i L_i^T[-Phi_i''] L_i >= h I, h>0.                (8)

This allows local gauge zero modes if their joint kernel has been
removed by the exact lattice constraints. An interior solution of the
FULL sewn equations has a unique maximum and the required boundary
gap; the finite lattice theorem proves its nonzero coefficient.
Nothing in this argument restricts the fixed graph to a tree.

For complex phases the corresponding LOCAL statement is also stable
under elimination. If Re H>0 and internal coordinates are eliminated
at their genuine stationary point, the effective Hessian is

    H_eff=H_ee-H_ei H_ii^(-1)H_ie, Re H_eff>0.             (9)

Indeed for w=(-H_ii^(-1)H_ie v,v), H w=(0,H_eff v), so
Re(v^*H_eff v)=w^*(Re H)w>0. The effective density is multiplied
by the NONZERO Gaussian determinant of H_ii. A global gap and the
source contour family still need a separate proof; (9) alone is local.

If, in addition, the actual block canonical graphs identify the sewn
stationarity equations with full shape matching, true INTEGER edge
angles and the marked peripheral periods, the
[full-slice criterion](source_angle_stationarity_critical_audit.md)
identifies the positive critical point with the Casson--Rivin maximum.
Absolute regulator calibration and primitive smooth end completion
then identify its value with hyperbolic volume. These geometric tests
cannot be inferred from (8), ordinary channel triangle inequalities,
or the fact that a physical source polytope is combinatorially an
octahedron.

## 5. Actual applicability and the next local estimate

The measure hypothesis is ALREADY true for literal original physical
sewing by Section 1. Exact cap-tree kernels also give a real, all-width
test case for positive squared kernels: their complete contraction has
once-power positive simplex
energy and strict concavity, with all internal factorials and phases
accounted for in the
[cap-tree theorem](actual_cap_tree_angle_energy.md). That test case
does not give a complete interior six-port block.

For the genuine six-port source, the
[divided-power theorem](actual_six_port_divided_power_source_kernel.md)
provides the exact saturated source kernel, all original marked
normalizations, and a finite formula for every physical coefficient.
It does NOT yet provide:

* a coherent physical coefficient packet with the nonzero density and
  uniform complex/corridor bounds needed in (6), or an exact permitted
  contour putting its saddle on that real parameter domain;
* an error exponent satisfying the JOINT budget (5), and a global
  complementary-source gap;
* the actual six-port canonical/angle incidence required after (9).

Thus a generic 6j formula followed by an unspecified inverse minor is
not the missing estimate. A sufficient concrete target is a uniform
packet for the literal six-head tensor of a SPECIFIED prime tangle in
its physical ports, retaining its divided Ward relation. Such a result
can be sewn without first proving a tame generic channel frame. This
changes where the conditioning problem must be solved, but does not
pretend the currently known six-port kernel already meets the analytic
hypotheses or establish a new general volume-equality family.
