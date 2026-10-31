# The actual Fejér half block: uniform coefficient entropy

Independently reviewed, 31 October 2026. This gives the exact
level-N half-block recurrence, its weighted rate, and the uniform
exponential rate of EVERY coefficient, including the boundary degrees.
It also fixes the complete-triangle normalization and disproves one
proposed endpoint-convexity shortcut. These are local source theorems;
no shared forest bound, representation, or filling-cycle conclusion is
asserted. All limits below run through every even N tending to infinity.

## 1. The original finite polynomial and its exact recurrence

Let N=2m>=4, d=N-1, M=m-1, theta=pi/N, and

    c_j=2cos((2j+1)theta), s_j=2sin(j theta),
    a_j=2+c_j=4cos^2((j+1/2)theta), product_(j=0)^M a_j=2.

Use the [original homogeneous source](actual_homogeneous_casimir_face_source.md)
and its [positive cross/half decomposition](actual_fejer_cross_half_source_reduction.md).
Thus P=-H_(V_N(-2)), where V_N is the actual polynomial resolvent
numerator, and P_left contains exactly the physical paths j to i with
0<=i<=j<=M. Their middle monomial is b^i c^(d-j). These pieces are
not separately asserted to be covariant coupons.

For an interval i+1,...,j let K_(i,j) be its positive tiling continuant.
A monomer at r has weight s_r^2(x+y); a dimer ending at r has weight
s_r s_(r-1) a_(r-1)xy. The latter includes the UNUSED intermediate
diagonal. Set K_(i,i)=1 and Q_(i,j)=K_(i,j)/product_(r=i+1)^j a_r.
The actual path expansion is exactly

    P_left=2 sum_(i<=j) b^i c^(d-j)
               product_(r<i)a_r product_(r>j)^M a_r K_(i,j)
          =4 sum_(i<=j) b^i c^(d-j) Q_(i,j)/a_i,          (1)

    Q_(i,i)=1, Q_(i,i+1)=alpha_(i+1),
    Q_(i,j)=alpha_j Q_(i,j-1)+beta_j Q_(i,j-2),
    alpha_j=(s_j^2/a_j)(x+y),
    beta_j=(s_j s_(j-1)/a_j)xy.                         (2)

All absent negative-index terms are zero. The original level remains N,
not m. Define the strictly positive coefficients

    A_N(i,j,k)=[x^k y^(j-i-k)]Q_(i,j), 0<=k<=j-i.

The corresponding coefficient of P_left is (4/a_i)A_N. The multiplier
4/a_i is between a positive constant and CN^2, uniformly in every row.
Right paths are obtained by the literal row reflection j -> d-j and
b <-> c, with the same x,y polynomial.

## 2. Uniform weighted rate, retaining both physical endpoints

Fix positive x,y, uniformly on compact positive sets. The limiting
Perron root at t=j/N is

    L(t;x,y)=[(x+y)sin^2(pi t)+sin(pi t)
       sqrt((x+y)^2 sin^2(pi t)+4xy cos^2(pi t))]
                                           /[2cos^2(pi t)],
    L^2-(x+y)tan^2(pi t)L-xy tan^2(pi t)=0, L>0.        (3)

It increases strictly from zero to infinity. Uniformly over ALL rows,

    sup_(0<=i<=j<=M) |N^-1 log Q_(i,j)(x,y)
               -integral_(i/N)^(j/N) log L(t;x,y)dt| ->0. (4)

Here is a proof with no endpoint gap. Fix eta>0. On
eta N<=j<=(1/2-eta)N the coefficients of (2) stay in a compact
positive set, converge uniformly to their limits, and vary by
O_eta(1/N) per step. For a constant recurrence
q_l=alpha q_(l-1)+beta q_(l-2), q_0=1,q_1=alpha, one has

    q_l=(lambda_+^(l+1)-lambda_-^(l+1))/(lambda_+-lambda_-),
    lambda_-<0<lambda_+, |lambda_-|/lambda_+<=r_eta<1.

Hence c_eta lambda_+^l<=q_l<=C_eta lambda_+^l, and the corresponding
transfer-matrix powers obey the same upper exponential bound. Partition
an arbitrary interior interval into blocks of length floor(sqrt N),
with shorter end blocks. Positivity compares each block with its minimum
and maximum constant coefficients. Retaining only tilings which do not
cross a block boundary gives the lower bound; transfer matrices give
the upper bound. The logarithmic block overhead is O_eta(sqrt N+1),
and the accumulated variation cost is O_eta(sqrt N). Thus (4) holds
uniformly for all interior intervals, including short ones.

The omitted endpoint intervals cost at most

    C eta N log(2/eta)+C log N                         (5)

in absolute logarithmic size. For the upper bound use transfer norm
at most product_j(1+alpha_j+beta_j). Near zero these coefficients are
bounded; near M the denominator a_j is comparable to
((M-j+1/2)/N)^2, giving the sum of logarithms
C eta N+2 sum_(r<=eta N)log(N/r). For the lower bound concatenate
only monomers on the omitted sites. Near zero alpha_j>=c(j/N)^2,
and near M it is bounded below by a positive constant; their negative
logarithms satisfy (5). These arguments also apply to intervals entirely
inside an endpoint portion. Finally log L=log t+O(1) near zero and
log L=-2log(1/2-t)+O(1) near one half, so the omitted limiting
integrals are O(eta log(2/eta)). Let N tend to infinity and then eta
to zero. This proves (4), locally uniformly in the positive weights.

Write F(x,b,y) for the ABSOLUTELY normalized source triangle potential
in [the original action theorem](actual_original_boundary_stationary_character.md),
section6. Equation (1), (4), and polynomially many summands imply

    lim N^-1 log P_left
      =max_(0<=mu<=nu<=1/2)
        [mu log b+(1-nu)log c+integral_mu^nu log L(t)dt]. (6)

For fixed mu the expression is convex in nu, so its maximum is at
nu=mu or nu=1/2. The latter is (log c)/2+H(x,b,y), where

    H=max_(0<=mu<=1/2)
          [mu log b+integral_mu^(1/2)log L(t)dt].

The unique maximizer obeys L(mu)=b, or
tan(pi mu)=b/sqrt(b(x+y)+xy). Its envelope derivative with respect
to log b is mu, exactly the source triangle middle angle divided by
2pi. Both H-(log b)/2 and F-(log b)/2 tend to zero as b tends to
infinity: for H use the logarithmic endpoint tail, and for F use its
original positive logdet integral and integrable cos^(-2) endpoint
bound. Therefore H=F with NO missing additive constant. Also
F>=(log b)/2, from the actual determinant's b^M term. Consequently

    lim N^-1 log P_left =max(log c,F(x,b,y)+(log c)/2),
    lim N^-1 log P_right=max(log b,F(x,c,y)+(log b)/2),
    lim N^-1 log P=max(F(x,b,y)+F(x,c,y),log b,log c).   (7)

The last formula uses the exact cross comparison. All weights in (7)
are positive and fixed before N. It is NOT a coefficientwise bound by
a complete coupon plus an identity coupon, and it licenses no exchange
of infimum over shared radii with a maximum over local branches.

## 3. Actual coefficients in strict interiors

Put

    D={0<=mu<=nu<=1/2, 0<=xi<=nu-mu},
    g(t,l)=log L(t;exp(l),1)
           =l/2+log tan(pi t)+asinh(tan(pi t)cosh(l/2)),
    Phi(mu,nu,l)=integral_mu^nu g(t,l)dt,
    E(mu,nu,xi)=inf_(l real)[Phi(mu,nu,l)-xi l].        (8)

First consider compact subsets of 0<mu<nu<1/2,
0<xi<nu-mu. Normalize Q_(i,j) by product_(v=i+1)^j a'_v,
where a'_v=s_v^2/a_v. The resulting monic degree-r polynomial,
r=j-i, satisfies

    p_0=1, p_1=x+y,
    p_r=(x+y)p_(r-1)+gamma_r xy p_(r-2),
    gamma_r=a_(i+r-1)/(s_(i+r)s_(i+r-1))>0.            (9)

Substituting x/y=-z^2 and dividing by z^r gives the Jacobi recurrence
q_r(t)=t q_(r-1)(t)-gamma_r q_(r-2)(t), t=z^-1-z.
Its symmetric tridiagonal matrix has positive off-diagonal entries,
so its roots are real and simple. The map z>0 ->z^-1-z is bijective
onto the real line. Thus p_r(x,1) has exactly r negative real roots.
The compact-interval bounds on gamma give a uniform Jacobi norm bound,
placing all these roots in a compact negative interval away from zero
and infinity. The polynomial is reciprocal as well.

After a bounded tilt x=exp(l), y=1, its coefficient distribution is
therefore a sum of r independent Bernoulli variables with probabilities
uniformly away from zero and one. For k/r in a compact subset of (0,1),
the unique exact-mean tilt stays bounded. Its probability at that mean
is comparable to r^(-1/2): Fourier inversion has a Gaussian expansion
on |theta|<=r^(-2/5), variance comparable to r, and modulus bounded
by exp[-c r sin^2(theta/2)] elsewhere. Bounded third moments give the
relative Gaussian error o(1). The logarithm of this probability is
therefore O(log N).

The weighted theorem (4) and this exact coefficient identity give

    N^-1 log A_N(i,j,k) -> E(mu,nu,xi)                (10)

for every sequence i/N->mu,j/N->nu,k/N->xi in a strict interior,
locally uniformly there. To justify convergence of the exact tilts,
the normalized log polynomials are convex and converge locally
uniformly to differentiable strictly convex Phi. The two secant
inequalities imply convergence of their first derivatives on compact
intervals; the unique limiting tilt satisfies Phi_l=xi. The same
root/variance bounds imply Phi_ll>0. No derivative of an unsupported
weighted asymptotic has been taken.

## 4. The closed-domain theorem

The function E is continuous on ALL of D, and

    sup_(0<=i<=j<=M,0<=k<=j-i)
      |N^-1 log A_N(i,j,k)-E(i/N,j/N,k/N)| ->0.         (11)

This also holds for the actual half-block coefficient (4/a_i)A_N,
since its additional logarithm is uniformly O(log N).

For continuity set q=nu-mu, B=2 integral_mu^nu log tan(pi t)dt, and

    delta_r(t)=asinh(tan(pi t)cosh(r/2))-r/2-log tan(pi t), r>=0.

This is positive, decreases to zero, and is dominated by the integrable
delta_0: it is -log t+O(1) at zero and tends to log2 at one half.
Its full-interval integral tends to zero as r tends to infinity.
Exactly, with a=min(xi,q-xi),

    E=B+inf_(r>=0)[a r+integral_mu^nu delta_r(t)dt].    (12)

Hence B<=E<=B+integral_mu^nu delta_0, which proves E->0 uniformly
as q->0. As a->0 choose a large fixed r first; (12) gives E-B->0
uniformly. Where a>=a0>0 the minimizer is restricted to a common
compact r interval, so continuity follows by compact minimization.
In particular E(mu,nu,0)=E(mu,nu,nu-mu)=B.

For the uniform upper bound, every finite real l gives
N^-1 log A_N<=N^-1 log Q_(i,j)(exp(l),1)-(k/N)l.
At each point of D select a finite l within epsilon of its infimum,
even when the infimum is reached only at infinity. Continuity gives
a neighborhood where the same l works within 2epsilon. A finite cover
of D and (4) for this finite set of tilts give the uniform upper bound.

For the lower bound consider any sequence tending to a point with
0<xi<q. Trim to i'=max(i,ceil(eta N)),
j'=min(j,floor((1/2-eta)N)), and set r'=j'-i', r=j-i,
k'=floor(k r'/r). For small fixed eta, r'>0 and
0<=k-k'<=r-r'. Retain an arbitrary interior tiling and specified
x- and y-monomers on the omitted sites. This is an actual subset of
the original tilings, with no crossing dimer, and gives

    A_N(i,j,k)>=A_N(i',j',k') product_(omitted v)a'_v. (13)

The omitted logarithmic cost is at most (5). Apply (10) to the strict
retained interval, let N tend to infinity, and then eta to zero.
Continuity gives the required lower rate. If xi=0 or q, including
sequences whose integer k is not exactly extreme, the all-monomer
term gives A_N>=binom(r,k) product a'_v>=product a'_v. Uniform
log-sine/cosine Riemann estimates, including the upper half-step, give

    N^-1 log product_(v=i+1)^j a'_v
                  =B(i/N,j/N)+O(log N/N).             (14)

This also handles q=0. Compactness turns these sequential lower
bounds into the uniform statement (11). It is an exponential-rate
theorem, not a relative amplitude or derivative asymptotic.

## 5. Exact endpoint normalization and a finite entropy formula

Let R_M(b) be the original lower-block path numerator starting at M,
with every ending b^i retained. Replace each unused spectral factor
a_r, r<M, by a_r^*=c_r-c_*, where c_*=-2cos(pi/N), to obtain
D_b=R_M^*(b). These definitions keep every original sine coefficient.
The exact path comparisons give

    D_b<=R_M<=sqrt(C_N)D_b,
    C_N=4(4-delta)/(delta N^2)<2, delta=2-2cos(pi/N),
    [b^i x^k y^(M-i-k)]R_M=(2/a_i)A_N(i,M,k),
    B_cross=4(x+y)D_bD_c, B_cross<=P_cross<3B_cross.    (15)

For completeness, the comparison factor is the product over the lower
unused rows of a_r/a_r^*, bounded by sqrt(C_N). Splitting the paired
root path at its compulsory central one-step gives the last exact
factorization. The recorded complete-channel identity implies
D_b=C_front D_M(x,b,y), where D_M is the original determinant and
C_front=product_(r<M)a_r^*=N/[2sin(pi/N)]. Thus this normalization
differs from that determinant by only a polynomial scalar, not an
unknown exponential constant.

It follows uniformly on the ENTIRE triangle simplex that its actual
coefficient entropy is

    C(alpha_x,alpha_b,alpha_y)=E(alpha_b,1/2,alpha_x),
    alpha_x+alpha_b+alpha_y=1/2, alpha_j>=0,
    C(alpha)=V(2pi alpha)/(2pi),
    V(theta)=2sum_j[Lambda(theta_j/2)+Lambda((pi-theta_j)/2)],
    Lambda(t)=-integral_0^t log|2sin w|dw.             (16)

The finite third degree is M-i-k, not N/2-i-k. Its bounded offset
disappears only after (11) and uniform continuity. To prove the
absolute last equality, for strict positive alpha choose
x=tan(pi alpha_x), b=tan(pi alpha_b), y=tan(pi alpha_y).
Their pairwise product sum is one. The unique maximizer in (6) with
nu=1/2 is alpha_b, and the original triangle derivatives of F are
exactly alpha_x,alpha_b,alpha_y. Differentiating this already proved
smooth formula shows that log(x/y) is the correct minimizing tilt.
Therefore E=F-sum alpha_j log L_j. The absolute source identity
2pi F=sum theta_j log L_j+V(theta) proves (16); continuity includes
every boundary face. At a cross port the two triangular allocations
and the ONE forced x-or-y unit in (15) must remain explicit before
shared coefficient extraction.

There is also a finite formula for the general E. For mu<nu put

    q=nu-mu, Dangle=2pi(xi-q/2),
    a=cos(pi mu), b0=cos(pi nu),
    kappa=sin Dangle/sqrt(a^2+b0^2-2a b0 cos Dangle),
    alpha_x(t)=1/4-t/2+asin(kappa cos(pi t))/(2pi),
    alpha_b(t)=t, alpha_y(t)=1/2-t-alpha_x(t).          (17)

Use the real principal arcsine. The domain |Dangle|<=pi q implies
|kappa|<=1: the difference between the squared denominator and
sin^2 Dangle is
(cos Dangle-a b0)^2-(1-a^2)(1-b0^2)>=0.
For strict outer degrees kappa=tanh(l/2) for the unique tilt, because
direct integration gives alpha_x(t)=partial_l Phi(t,1/2,l) and
Dangle=asin(kappa a)-asin(kappa b0). The right side is strictly
increasing with the required range; this fixes the original branch
after squaring. At xi=0,q take kappa=-1,+1. Subtracting the two
correct endpoint Legendre identities gives

    E(mu,nu,xi)=C(alpha(mu))-C(alpha(nu)).             (18)

Set E=0 when mu=nu. This is a finite Lobachevsky evaluation on the
whole closed domain. Its corresponding left degree vector is
alpha(mu) on (x,b,y), minus alpha(nu) on (x,c,y), plus e_c.
The output triangle can be written with generalized angles
(-theta_x,2pi-theta_c,-theta_y); the Lobachevsky reflection identities
give its negative V. This is a signed-angle identity, not a developing
map, an independent geometric volume bound, or a cycle-selection rule.

## 6. The fixed-outer-degree endpoint convexity claim is false

At l=0 one has g_l=1/2 and g_ll=sin(pi t)/4. At the balanced
xi=(nu-mu)/2, the tilt is therefore zero. Hold mu and xi FIXED
while varying nu. The exact Legendre Schur complement is

    E_(nu,nu)=pi cos(pi nu)/[sin(pi nu)(1-sin(pi nu))]
                    -pi/[cos(pi mu)-cos(pi nu)].       (19)

Indeed Phi_(nu,l)=1/2 and
Phi_(l,l)=[cos(pi mu)-cos(pi nu)]/(4pi). At nu=1/4 the
first term is pi/(1-1/sqrt2); for every 0<mu<1/4 the second
term is larger. In particular mu=1/8,nu=1/4,xi=1/16 is a strict
regular negative-curvature point.

Choose a sufficiently small fixed rational epsilon>0. For all large
even N use rounded i=N/8,k=N/16,j0=N/4 and
jplus/minus=N(1/4+/-epsilon). The uniform coefficient theorem and
(19) give, for the ACTUAL coefficients
mathcal A_N(j)=(4/a_i)A_N(i,j,k),

    log mathcal A_N(j0)
      -[log mathcal A_N(jminus)+log mathcal A_N(jplus)]/2
                                       >=c_epsilon N>0. (20)

Thus coefficient log-convexity in this exact direction fails
exponentially. The common source factor 4/a_i is retained. This
does not disprove a shared forest bound: an exchange that changes
other face degrees could behave differently. Holding the proportion
xi/(nu-mu) fixed is a DIFFERENT direction and is not addressed by
(19). Fixed-positive-radius endpoint convexity in (6) cannot be used
after fixing xi without this Schur correction.

## 7. Validation and scope

The [focused audit](../experiments/audit_actual_fejer_half_block_entropy.py)
and [saved results](../experiments/actual_fejer_half_block_entropy_results.json)
retain independent original numerator comparisons, positive paths,
and the absolute triangle anchor. Finite closed-boundary rate and
coefficient-curvature profiles are diagnostics for the displayed
proofs, not substitutes for uniform estimates. The exact source
interface is also covered by the frozen numerator and cross-half
audits linked above.

The author run passes at 75 digits: 329 left and 329 right original
numerator coefficients, 96 direct positive paths, 5 independent
triangle anchors, 11 recurrence identities and 11 Jacobi/log-root
identities, 52 actual negative roots, 12 closed-entropy integral
reconstructions, and 64 extreme coefficient checks. It records 25
weighted-rate and 88 closed-coefficient profiles, and four increasing-level failures of the
proposed coefficient log-convexity. The largest anchor or entropy
reconstruction error is below 7e-76. These finite checks do not prove
the uniform limits; those are proved above.

The weighted, strict-coefficient and closed-domain proofs were developed
and independently reviewed in the collaborating source and coherent
threads. The consolidated public proof and audit code received full
root and independent analytical review. The independent redirected
75-digit replay reproduced every stated count and error; geometry's
targeted review checked the paired-root normalization and unsquared
arcsine branch, including all closed endpoints.
No shared entropy maximum is evaluated here; in particular no local
max/min exchange, general forest-volume inequality, or signed long-filled
knot asymptotic is claimed.
