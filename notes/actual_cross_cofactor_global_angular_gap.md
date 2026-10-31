# A global angular gap for the actual cleared cross cofactors

The [whole-source local packet](general_full_spectral_numerator_geometric_packet.md) now assembles these results for the actual full numerator. The original global spectral filling period remains open.

31 October 2026. . All matrices,
paths and spectral nodes are at the original level N. This is a local
cofactor estimate on a thin spectral cover strip, not a Gaussian-cycle
or whole-source theorem.

## 1. Statement and exact source inputs

Put d=N-1, J=floor(d/2), theta=pi/N,

 a_r=4cos^2((r+1/2)theta), s_r=2sin(r theta),
 A=x+y, P=xy, p_r=s_r^2 A,
 q_r(u)=s_r s_(r-1)(a_(r-1)+u)P.

For j=J-k, with 0<=k<=k0 fixed, let R_j(b,u) be the actual cleared
cofactor with recurrence

 R_j=b^j product_(r<j)(a_r+u)+p_j R_(j-1)+q_j(u)R_(j-2).
                                                               (1)

This includes D,E's R factor, and odd G. A zero face remains zero.
Assume the positive entries of (x,b,y) range in a fixed positive compact,
A>0, and at least TWO entries are positive. Let epsilon>0. If the
circular phases of the positive face entries have diameter at least
epsilon, then there exist gamma>0,C,K and a FIXED strip height tau>0
such that, uniformly for |Im delta|<=tau and all real Re delta,

 |R_j(x exp(i theta_x),b exp(i theta_b),y exp(i theta_y);
                                      -4sin^2(pi delta))|
       <=C N^K exp(-gamma N) R_j(x,b,y;0).             (2)

The statement includes b=0 and either single protected outer face.
For b=0,xy=0 there is only one positive variable and the cofactor is an
exact monomial; there is no relative-angle condition to assert. The
case x=y=0 is excluded by the actual marked matching-edge dictionary.

The exact node adapter, proved independently from the original matrices,
is, for 0<=a<=j,

 R_j(b,-a_a)=K_(a,j)(-a_a) S_(2a)D_a(x,b,y),          (3)
 R_a(b,-a_a)=S_(2a)D_a(x,b,y).

Here K_(a,a)=1, K_(a,a-1)=0, and K follows p_v,q_v above. Also

 0<=R_a(b,-a_a)<=R_a(b,0),
 0<=K_(a,j)(-a_a)<=K_mono(a,j):=product_(v=a+1)^j p_v. (4)

These are COEFFICIENTWISE statements. For completeness the latter
normalizes K by product s_v^2, giving

 Q_r=A Q_(r-1)-gamma_r xy Q_(r-2),
 gamma_r=1-s_a s_(a+1)/(s_(a+r)s_(a+r-1)) in [0,1].

Induction on Q_r-xQ_(r-1)=y[Q_(r-1)-xQ_(r-2)]
 +(1-gamma_r)xyQ_(r-2) proves Q_r>=0, then Q_r<=A^r.
Thus no absolute value of a sign-changing tail is assumed positive.
The nodal positivity proof is in the cross-cofactor handoff §8.

## 2. A strict gap at all far nodes

Choose a fixed small delta0>0, for example delta0<1/8. Call a node far
if a/N<=1/2-delta0. This definition only separates nodes for this proof.
It does not alter the physical folded label or its half-index.
We prove, whenever at least two faces are positive,

 R_j(b,-a_a)<=C exp(-gamma_far N)R_j(b,0)             (5)

uniformly over ALL these far nodes. This estimate needs no angular
separation. Polynomial factors are harmless and can be absorbed by
slightly reducing gamma_far.

First suppose xy>0; b may be zero. The fixed interval

 I=[1/2-delta0/2, 1/2-delta0/4]

lies AFTER every far row a and BEFORE j for all sufficiently large N.
On it every ratio

 q_v(0)/(p_v p_(v-1))
       =(a_(v-1)xy)/(s_v s_(v-1)(x+y)^2)

is bounded below by a positive compact-set constant. Choose cN disjoint
pairs of adjacent steps in this interval. Starting with the all-monomer
path from j to a, either retain each selected pair or replace it by its
original dimer. The choices are independent and all paths are physical.
Their sum therefore gives

 K_(a,j)(0)>=exp(c' N)K_mono(a,j).                   (6)

On the other hand, K_(a,j)(0)R_a(b,0) is precisely the subset of paths
in R_j(b,0) whose starting row is at most a and which visit a. There
is no multiplicity in splitting a path at that row. Combining (4),(6)
proves (5). All selected rows stay in a fixed strict bulk interval, so
neither a near-zero initial row nor the actual folded endpoint affects
the constants.

Now suppose xy=0 and b>0. Write A for the sole positive outer face.
The recurrence is first order and its actual zero-spectral starting
terms are

 W_i=b^i product_(r<i)a_r product_(v=i+1)^j [s_v^2 A],
 R_j(b,0)=sum_(i=0)^j W_i.

For a far node, all starts i>a vanish exactly, and for i<=a the ratio
to W_i is product_(r<i)(1-a_a/a_r). Uniformly for sufficiently large N,
a_a>=c_delta0>0 and a_r<=4. Hence starts i>=eta N have ratio at most
(1-c_delta0/4)^(eta N).

The remaining short starts have an independent exact gap. Choose fixed
eta>0 small enough that, on the given positive compact,

 W_(i+1)/W_i=b a_i/(s_(i+1)^2 A)>=1+c
                for all 0<=i<=2eta N

and all sufficiently large N. Such eta exists from the displayed
original sine/cosine entries. Each i<=eta N is then exponentially
smaller than W_floor(2eta N), by at least eta N consecutive ratios.
Summing at most N terms gives

 sum_(i<=eta N) W_i<=CN exp(-c'eta N)R_j(b,0).

Combining the two ranges proves (5), including x=0 and y=0. The only
remaining case b=0,xy=0 is the excluded one-variable angular case.

## 3. The near nodes have the original determinant angular gap

For a/N>=1/2-delta0, a>=a0N for a fixed a0>0. Apply the EXACT PSD
contraction of actual_positive_face_coefficient_saddle.md §2 to

 D_a=det[bI+(x/2)H_-+(y/2)H_+].

Its finite pair-trace lower bounds hold for every a0N<=a<=floor(d/2),
not only a deficit o(N): this is the explicit scope and bulk-square
proof in actual_q_hahn_boundary_model_curvature.md §§1--4.

When x,b,y are all positive, the b--x and b--y pair traces are at least
cN. If the positive-phase diameter is at least epsilon, one of these
two phase differences is at least epsilon/2. When one outer face is
zero, its single remaining pair has the same bound (220/022). When
b=0 and x,y>0, the original 202 variance/pair trace is at least cN.
Consequently in every applicable zero pattern,

 |D_a(x exp(i theta_x),b exp(i theta_b),y exp(i theta_y))|
       <=exp(-gamma_ang N)D_a(x,b,y).                (7)

This is a determinant modulus inequality on the ENTIRE phase torus,
not a local complex-log estimate. The positive polynomial K in (3)
has modulus at most its positive-radius value. Equations (3),(4),(7)
therefore prove the same exponential nodal bound relative to R_j(0).
For far nodes, (5) and the positive coefficient statement (4) already
prove the bound at arbitrary phases. Thus ALL nodes a=0,...,j satisfy

 |R_j(faces with phases;-a_a)|
       <=C exp(-gamma0 N)R_j(positive faces;0).       (8)

## 4. Exact interpolation, including the omitted last nodes

The actual spectral degree of R_j is at most j. The full physical
node family a=0,...,J is the even Chebyshev-root or odd Chebyshev-Radau
family after the affine change z=-1-u/2. Its exact interpolation
Lebesgue norm on [-4,0] is O(log(N+1)); this follows from discrete
cosine inversion on the original N-point odd-angle grid and the bound
|D_J(t)|<=min(2J+1,1/|sin(t/2)|). This is the same exact interpolation
used in the cofactor handoff, not interpolation of full V.

If j=J, apply it directly to (8). If j<J, DO NOT use an unavailable
D_a adapter at a>j. Instead put

 p(u)=R_j(faces with phases;u),
 Q(u)=p(u) product_(a=j+1)^J (u+a_a).

The degree of Q is at most J. At the retained nodes its absolute value
is bounded by 4^k times the right side of (8); at the omitted nodes it
is EXACTLY zero. Full-grid interpolation gives

 ||Q||_[-4,0]<=C_k log(N+1) exp(-gamma0 N)R_j(0).     (9)

Division by these k fixed-in-number factors costs only a polynomial in
N, even though their roots cluster at the endpoint. Here is an elementary
bound with no spacing assumption. A polynomial p of degree j and interval
supremum M has derivative supremum at most C(j+1)^3 M: expand in
Chebyshev polynomials, whose coefficients have magnitude at most2M,
and use ||T_l'||<=l^2. Around a point attaining M, a one-sided interval
of length c/(j+1)^3 has |p|>=M/2. Remove small neighborhoods of the k
roots occupying less than half that interval. At a remaining point every
factor has magnitude at least c_k/(j+1)^3. Hence

 ||p||_[-4,0]<=C_k(j+1)^(3k)||Q||_[-4,0].            (10)

This also holds for complex p, by the same cosine coefficient bound.
Thus every required literal terminal cofactor satisfies an exponential
angular gap on the WHOLE real spectral interval, with a polynomial
prefactor. No last row or parity node has been silently replaced.

Finally the elementary polynomial Bernstein bound on [-4,0] gives

 |p(-4sin^2(pi delta))|
   <=exp(2pi j |Im delta|)||p||_[-4,0].              (11)

Indeed z=-1-u/2=-cos(2pi delta)=(w+w^-1)/2 with
|w|=exp(2pi|Im delta|); apply the exterior maximum principle to the
polynomial of degree j after this substitution. Since j<=N/2, choosing
pi tau<gamma0/2 makes (9)--(11) imply (2), with a possibly reduced gamma.
The estimate is uniform for the full real fold interval and its periodic
copies, not only near delta=0.

## 5. Scope

This proof uses exact original node identities, finite positive paths,
actual PSD angular bounds and finite polynomial interpolation. No complex
starting-row contour or generic off-node PSD representation is required.
Every physical starting row and the protected-middle i=0 contribution
remains. The one-variable monomials are explicitly exempt because their
sole phase is a common homogeneous phase.

The local factors can serve a whole shared-face angular argument only
after checking the actual connected phase graph, keeping every other
factor under a uniform spectral bound, and retaining the original marked
coefficient and finite central prefactors. The local theorem alone is
not a full shared coefficient asymptotic or a selected Gaussian period.

## Scope

This is a local cofactor input, with no independent whole-source or Gaussian-cycle assertion.