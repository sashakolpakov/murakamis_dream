# Actual signed ports and a quantum-multinomial face kernel

30 October 2026. Independently reviewed and frozen. This gives the exact original crossing on the
polynomial face source, two radius bounds, and a sufficient local
geometric certificate for a signed one-port color corridor. It does
not claim a universal signed smoothing gap or a simultaneous signed
norm estimate.

## 1. Exact kernel, all polynomial degrees

Use the ORIGINAL root conventions N>=3, d=N-1, q=exp(pi i/N),
Q=q^2 and lambda0=q^(d^2/2), with its prescribed square-root lift.
Let T be the [original small-circle face operator](actual_small_circle_polynomial_face_insertion.md), with outer variables
x,y and outgoing middle variable c:

    T c^j = -(q Q^j+q^-1 Q^-j)c^j
        +(2-Q^j-Q^-j)(x+y)c^(j-1)
        +(q+q^-1-q Q^-j-q^-1 Q^j)xy c^(j-2).       (1)

The displayed lowering coefficients vanish at the actual bottom two
rows. They are N-periodic in j. Therefore

    T(c^(mN) f)=c^(mN) T f,                         (2)

and C[x,y,c] is the direct sum, over C[x,y], of invariant blocks
c^(mN) span{1,c,...,c^(N-1)}. The characteristic polynomial on each
block for C=-T is

    product_(j=0)^(N-1) [X-q^(2j+1)-q^(-2j-1)]
        = 2 ChebyshevT_N(X/2)+2.                    (3)

Cayley--Hamilton proves this annihilator on the WHOLE polynomial
space. In particular all confluent root conditions are retained.

Let R_+ = r_N(-T), where r_N is the actual crossing polynomial, and
R_- its inverse modulo (3). For 0<=j<N,

    R_+ c^j = (-1)^j sum_(i+k+l=j)
        q^(j+i^2) {j;i,k,l}_Q c^i x^k y^l.          (4)

Here {j;i,k,l}_Q=(Q;Q)_j/[(Q;Q)_i(Q;Q)_k(Q;Q)_l].
Every denominator is nonzero. R_- is the same formula with q replaced
by q^-1 (and hence Q by Q^-1). For an arbitrary j=mN+r, 0<=r<N,
multiply (4) for r by c^(mN). This is an exact polynomial formula,
not a reduction of c^j modulo c^N-1.

The actual source crossing is lambda0 R_+; its inverse is
lambda0^-1 R_-. All quantum and Cartan phases are present.

Proof of (4). Work first at an indeterminate q for this auxiliary
triangular interpolation. It is not being identified with the original
generic-q crossing germ. The matrix defined by
the right side is triangular with diagonal nu_j=(-1)^j q^(j(j+1)).
It commutes with -T. One direct coefficient proof divides the
c^i x^k y^l coefficient by
(-1)^j q^(j+i^2) (Q;Q)_j/[(Q;Q)_i(Q;Q)_k(Q;Q)_l]. Put I=Q^i,
K=Q^k,L=Q^l,J=IKL and

    c(Z)=qZ+1/(qZ), b(Z)=2-Z-Z^-1,
    e(Z)=q+q^-1-q/Z-Z/q.

The required identity is

    c(I)-b(QI) qI (2-K-L)/(1-QI)
      -e(Q^2 I) Q^2 I^2 (1-K)(1-L)/[(1-QI)(1-Q^2 I)]
     =c(J)+b(J) q^-1 (2-K-L)/(1-J)
      -e(J) Q^-1 (1-K)(1-L)/[(1-J)(1-J/Q)].         (5)

Clearing denominators gives zero by expansion. Boundary rows follow
by the polynomial identity before division. Distinct generic diagonal
nodes imply that this is the unique interpolating polynomial in -T
with values nu_j. At q=exp(pi i/N), the paired nodes j,d-j collide.
Their divided difference has limit

    -nu_j (N-1-2j)/[2(q^(2j+1)-q^(-2j-1))],        (6)

exactly the derivative of the [ORIGINAL crossing polynomial](casimir_braiding_and_recoupling_lattice.md),
not only its nodal values.
The finite coefficients of (4) specialize regularly. This proves (4)
including the nilpotent component. The inverse follows either from
the inverse Hermite conditions or q->q^-1: (1) is invariant under
that substitution, whereas every nu_j is inverted.

There is also a useful exact alternating Newton expansion. Put
S_r=product_(j=1)^r 2sin(pi j/N) and
Bhat_r(z)=product_(j=0)^(r-1)(c_j-z)/S_r^2, S_0=1. Then

    r_N(z)=sum_(r=0)^d (-q)^r Bhat_r(z),
    r_N^minus(z)=sum_(r=0)^d (-q^-1)^r Bhat_r(z)      (6a)

modulo (3). Indeed Bhat_r(-T)c^m=0 for r>m. For r<m its x-degree
is at most r, whereas the x^m coefficient of Bhat_m(-T)c^m is one:
it is product_(j=1)^m (2-Q^j-Q^-j)/S_m^2. Formula (4) gives the
x^m coefficient (-q)^m. This triangular comparison determines every
Newton coefficient, including the folded nilpotent part.

## 2. Original one-port marked source

Use the literal input b/output c convention in the frozen one-port
theorem. For displacement p=R-S, c=Q^(-p)b, and the original middle
monomial contributes q^(dp). Let P_rem be the full remaining positive
face polynomial BEFORE merging b,c. Its marked and exterior faces and
all remaining twists are unchanged. If L_h=P_(h-1)(-Omega), put
T_h=P_(h-1)(T), with T_1=I,T_2=T. Then the signed deleted-port
polynomial is exactly

    Q_(h,eps) = [lambda0^eps R_eps T_h P_rem]_(c=b),
        eps in {+1,-1}.                             (7)

R_eps and T_h commute. The original physical endpoints are included
because (7) agrees with the actual finite matrix L_h R^eps; this is
not a newly cyclically truncated source. The frozen connected one-port
argument applies: Q is polynomial, homogeneous of degree d(R-1),
and the original finite grid has exactly one target coefficient,
with no omitted level alias. The source is

    N^(R-1) product_remaining[k_a beta_a^2 omega_a^epsilon]
       [product_ordinary L_f^d] Q_(h,eps)|protected faces=0. (8)

This section assumes connected identity smoothing and distinct unmarked
middle faces, as in the frozen one-port theorem. The root transpose
adapter treats a single protected middle face separately. No ordered
or arbitrary simultaneous signed norm bound is inferred from (7).

An exact target restriction will be useful below. The merged face is
ordinary, so its target is d<N. Both T_h and R_eps preserve the ideal
(c^N), and their output is polynomial in every face variable. Therefore
every input term divisible by c^N gives, after c=b, a term divisible by
b^N and contributes ZERO to (8). One may discard exactly those input
terms before bounding this coefficient. This statement holds for all
h, not only h=1; it does not discard terms from an arbitrary period.

## 3. Explicit radius penalty and sufficient certificate

At fixed positive merged radii let x,y,b be the numerical outer/middle
radii, X=x/b,Y=y/b, and S_j=product_(r=1)^j 2sin(pi r/N), S_0=1.
The absolute value of every multinomial in (4) is
S_j/(S_i S_k S_l). Consequently the EXACT operator norm of R_eps on
the weighted coefficient l1 norm in independent x,c,y variables is

    K_N(X,Y)=max_(0<=r<N) sum_(i+k+l=r)
                   S_r/(S_i S_k S_l) X^k Y^l.       (9)

For additional variables, or identified outer variables, (9) remains
an upper bound. Formula (2) is essential: higher powers of c introduce
no larger norm. The original unit lambda0 has absolute value one.
The one-port norm theorem therefore gives

    ||Q_(h,eps)||_ell
       <=K_N(X,Y) [3+4X+4Y+4XY]^(h-1) P_sm(ell).   (10)

Every old variable has its final merged weight; evaluation at c=b
cannot increase this coefficient norm. P_rem has nonnegative
coefficients, so its norm is exactly P_sm(ell).

There is a finite, explicit limiting penalty. Put

    f(t)=integral_0^t log(2sin(pi u)) du,
    kappa(X,Y)=max_(i,k,l>=0, i+k+l<=1)
       { f(i+k+l)-f(i)-f(k)-f(l)+k log X+l log Y }.   (11)

Then log K_N(X,Y)=N kappa(X,Y)+O(log N), locally uniformly for
positive X,Y. To prove this, the monotone sine-product Riemann sums
give log S_j=N f(j/N)+O(log N) UNIFORMLY for 0<=j<N; isolate the
first and last unit intervals of the integrable logarithmic endpoint
singularities. There are O(N^3) terms in (9), and the uniform modulus
of continuity of f is O(eta log(1/eta)). A nearest grid point to a
maximizer therefore changes N times (11) by O(log N). These facts
give both bounds. The elementary weaker estimate

    K_N(X,Y)<=(1+X+Y)^(N-1)                          (12)

follows from sin(n theta)/sin(r theta)<=n/r for 1<=r<=n<N,
which bounds every sine multinomial by its ordinary counterpart.

There is also an exact transfer bound between TWO different norms.
Keep all other face weights fixed, use c=b+x+y in the input norm,
and c=b in the output norm. For c^(mN+r), its output-to-input norm
ratio is at most

    b^(mN)(b+x+y)^r/(b+x+y)^(mN+r)<=1.              (12a)

Hence R_eps has norm at most one for this transfer, for BOTH inverse
signs. Applying T_h afterwards at the output weights and then merging
gives the alternative exact source bound

    ||Q_(h,eps)||_ell
      <=[3+4X+4Y+4XY]^(h-1)
          P_rem(...,b,c=b+x+y,...).                 (12b)

The target denominator is STILL the actual merged face weight b^d.
The right side is a split-radius evaluation of the ORIGINAL remaining
polynomial; it is not its identity-smoothing evaluation. In particular
it has no established geometric volume interpretation.

More generally the target restriction permits ANY positive independent
input weight c and output weight b. Set B=b/c,X=x/c,Y=y/c. The finite
block norm is

    K_N(B,X,Y)=max_(r<N) sum_(i+k+l=r)
                  S_r/(S_i S_k S_l) B^i X^k Y^l.    (12c)

Unlike a norm on the whole untruncated polynomial space, (12c) has no
condition b<=c: all higher blocks were excluded by the actual target.
Define the homogeneous potential

    G(b,x,y,c)=max_(xi_j>=0, sum xi_j=1)
       [sum_(j=1)^4 Lambda(pi xi_j)/pi
               +xi_1 log b+xi_2 log x+xi_3 log y+xi_4 log c], (12d)

where Lambda(t)=-integral_0^t log|2sin u|du. Since f(1-t)=-f(t),
the preceding uniform Riemann-sum proof gives

    log K_N(b/c,x/c,y/c)=N[G(b,x,y,c)-log c]+O(log N). (12e)

The actual one-port upper rate is thus the remaining source evaluated
at its original, INDEPENDENT middle weights b,c, plus (12e), with
the original merged target denominator b^d. This is an exact source
norm consequence, not a new side-pairing or a representation theorem.
The ordinary multinomial bound gives the useful elementary inequality

    G(b,x,y,c)<=log max(c,b+x+y).                    (12f)

The entropy in (12d) is strictly concave in the simplex interior.
Indeed its negative Hessian, up to a positive factor, is
sum cot(alpha_j)v_j^2 on sum v_j=0, where alpha_j=pi xi_j. If all
alpha_j<=pi/2 this is positive definite. Otherwise alpha_0>pi/2 is
the only such angle. Put beta=sum_(j>0)alpha_j=pi-alpha_0<pi/2.
Weighted Cauchy and tan(beta)>sum_(j>0)tan(alpha_j) show that
the positive terms strictly dominate -cot(beta)v_0^2; when v_0=0,
they are themselves positive unless v=0. This proves the assertion.

For positive weights a boundary point with at least two positive
coordinates cannot maximize, because inserting a missing coordinate
gains a positive epsilon log(1/epsilon) term. At a corner j the largest
directional derivative is log(sum_(k!=j) l_k)-log l_j. Thus the maximum
is interior exactly under the four strict polygon inequalities, and
otherwise it is the dominant corner, with G=log(max l_j). At an
interior maximum sin(alpha_j) is proportional to l_j. The alpha_j
are half-arcs of the cyclic quadrilateral with those side ratios.
Coning it to infinity and triangulating by a vertex fan gives volume
sum Lambda(alpha_j): the internal half-arc terms cancel in pairs.
This is a local ideal-pyramid interpretation, not a global gluing claim.
In particular strict concavity and symmetry give the exact constant

    G(1,1,1,1)=4 Lambda(pi/4)/pi=:G_*.              (12g)

For an actual compatible positive radius ell, let Phi_sm(ell) denote
the full smoothing upper rate INCLUDING its original sine scalars,
and let F0=Vol(Y)/(2pi) be the original complete rate. If

    g=F0-Phi_sm(ell)-kappa(x/b,y/b)>0,              (13)

then (8)--(11), together with the existing uniform all-channel rate,
give a strict exponential upper gap for this signed small-port source
when h=o(N), in particular for h=O(sqrt N). The same conclusion holds
for h<=delta N with a sufficiently small fixed delta depending on g
and the explicit constant in (10). Polynomial channel counts and
the retained k_a factors do not change the rate. This is a SUFFICIENT
fixed-radius certificate, not a claim that (13) always holds.
The analogous sufficient certificate replaces Phi_sm+kappa by the
all-channel upper rate of the split evaluation (12b), with that same
merged target denominator. No equality of either optimized certificate
with a smoothing capacity is used.

## 4. A local original-packing certificate

Assume the selected signed port has distinct unmarked middle faces,
connected identity smoothing, and four POSITIVE curvatures x,b,c,y
in the original marked right-angled packing. Let F(x,b,y) be the
original fold determinant rate, with its proved absolute normalization
in [the stationary-character theorem](actual_original_boundary_stationary_character.md),
section6. Define

    g_port=F(x,b,y)+F(x,c,y)-G(b,x,y,c).             (13a)

If g_port>0, the signed small-port source is exponentially below the
original complete rate for h=o(N), or for h<=delta N with a sufficiently
small fixed delta. This is a local certificate valid for any certified
fixed-width graph satisfying these hypotheses.

In particular let A_N have external color N-h at this ONE signed port
and N at every other port, with every original half twist retained.
Let F_N^(port)(h) denote its exact empty-subset complete-image term
in the [original reflection identity](actual_external_circle_reflection_and_cusp.md),
including that identity's scalar sign. Under (13a) there are fixed
delta,gamma>0 and K such that, for both parities and all integer
0<=h<=delta N,

    |A_N(N-h,N_else)-F_N^(port)(h)|
        <=N^K exp[N(Phi_D-gamma)].                  (13c)

There is just one nonempty reflection subset here, the actual L_h R^eps
source of (7). Ports whose external colors remain N may have arbitrary
retained signs. Equation (13c) is not asserted when additional ports
are simultaneously varied.

Proof. Evaluate the remaining positive factors at the ORIGINAL packing.
Before deletion the two ordinary middle targets contribute -log b-log c,
and the removed fold circle contributes F(x,b,y)+F(x,c,y). Its beta and
short forced-product factors have zero limiting logarithmic rate at the
fold, including both parities. After the exact target restriction and
(12e), the upper bound has the same remaining factors, the target
-log b, and the added term G-log c. Their difference is exactly (13a).
Thus it is g_port below the proved original capacity Phi_D. The two
marked zero radii elsewhere can now be replaced by sufficiently small
fixed positive values. Continuity preserves a fixed portion of the
strict gap; the resulting small-color constant in (10) is finite.
The [uniform all-channel fold upper bound](actual_positive_face_channel_rate.md)
handles every remaining label.
Their number is polynomial; all their retained half-twist phases and
the removed lambda0 phase are units. This proves the stated corridor.
No optimum for the split-radius potential is identified with the
identity-smoothing capacity.

There is an explicit open geometric class for this criterion. Put

    F_*=F(1,1,1)
       =3[Lambda(pi/6)+Lambda(pi/3)]/pi.

If the four curvatures lie in [t,rho t], monotonicity and homogeneity
of both actual potentials, together with (12g), give

    g_port>=2F_*-G_*-log rho>0
            whenever 1<=rho<exp(2F_*-G_*).         (13b)

The threshold is approximately 2.807257219. It is strictly greater than
one without relying on that decimal: F_*>F(1,1,0)=G_*>0. Thus (13b) describes
a nonempty open locus of local positive-curvature data. Realization of
this comparable-ratio locus by a fixed labeled right-angled diagram is
a separate requirement; its rigidity does not follow from this local
inequality. The criterion does not cover
ports adjacent to a marked zero face or arbitrary curvature ratios.
Several signed deleted ports would require a separate simultaneous
source/norm argument; (13b) is not multiplied over interacting ports.

## 5. A precise obstruction to a uniform small-h norm bound

Even for h=1, no bound poly(N) C^h can hold for the weighted polynomial
coefficient norm at all positive radii. Take x=y=c=1, let i,k,l be
integers each N/4+O(1), and j=i+k+l=3N/4+O(1)<N. A single coefficient
of R_+ c^j has size

    S_j/(S_i S_k S_l)
      = exp{N[-4 f(1/4)]+O(log N)}.                 (14)

Here f(3/4)=-f(1/4), and -4 f(1/4)>0 (it equals v_oct/(2pi)).
The input monomial has norm one. Thus exponential growth is already
present in an actual one-port polynomial action, not merely in a
poorly chosen Hermite coefficient representation. This does not rule
out cancellation in the FINAL marked coefficient or a more adapted
source norm. It explains exactly what (13) must pay for, and why the
untwisted C^h estimate cannot be imported unchanged.

## 6. Validation and scope

The [focused audit](../experiments/audit_actual_signed_small_circle_face_kernel.py)
and [saved result](../experiments/actual_signed_small_circle_face_kernel_results.json)
pass. It checks (5) as an exact rational identity, then compares the
kernel against 8,312 original balanced crossing monomial paths for
R and R^-1, including 3,620 high totals and degrees through 2N+1.
Thirteen full polynomial blocks check the annihilator, inverse and
commutation identities, and 26 independently summed Newton expansions.
It does not build the original R matrices from the interpolating
polynomial.

There are 144 whole original marked signed-source comparisons, 106
nonzero, at both parities and both original mark positions. Their
remaining polynomial includes 534 monomials above the first c-period;
18 comparisons explicitly check that the removed higher blocks have
zero actual target. At 80 digits the audit also checks 1,972 original
quantum coefficient magnitudes and 366 split-radius norm transfers,
with maximum relative error 8.63e-80. The finite determinant/rate and
exponential-norm samples are explicitly diagnostics, not proofs of a
uniform asymptotic theorem or a geometric certificate for a fixture.

The theorem is a ROOT source result. It supplies no genuine-q normal
identity, no universal signed smoothing gap, and no simultaneous signed
norm estimate through dependent ports. The local radius test concerns
one varied signed port; all other external colors remain complete.

Independent root full analytical and audit-code review: PASS, including
the actual Hermite derivative, every polynomial degree block, independent
input/output weights and the original-packing rate subtraction.
Independent cluster full analytical/code review and fresh redirected
audit replay: PASS, reproducing all stated counts and errors.
Independent geometry full kernel review and targeted final radius,
entropy and corridor review: PASS. These reviews do not infer a
simultaneous signed estimate or a global quadrilateral representation.
