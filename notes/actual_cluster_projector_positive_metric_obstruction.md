# Actual Racah cluster projectors cannot share an orthogonal positive metric

29 October 2026. This is an exact obstruction to one proposed shortcut
for higher generic normals. Even the COMPLETE analytic root clusters
of the two physical Casimirs need not be orthogonal projections for
any common positive Hermitian form. A seven-level source example has
rank-two cluster projectors P,Q with trace(PQ)>33. The bound would be
at most two for orthogonal projections in any positive metric.

This does not refute the proved all-partner first-normal estimate,
higher scalar bounds, or a suitably weighted nonorthogonal transport
estimate. It rules out obtaining those conclusions by declaring the
two actual cluster decompositions simultaneously orthogonal.

## 1. The second normal retains an actual cluster overlap

Use the same generic source as the
[all-partner first-normal theorem](actual_all_partner_first_normal_bound.md).
For a pair of complementary internal channels write e*=N-1-e,
f*=N-1-f, d_j=[2j+1], and

    K_ij=[N]^2 S(e_i,f_j)^2 product_faces Delta^2,
    e_0=e,e_1=e*, f_0=f,f_1=f*.

The proved exact source-projector identity is

    sum_(i,j=0,1) d_(e_i)d_(f_j) K_ij
          =[N]^2 tr(E_e^S E_f^T),                 (1)

where E_e^S and E_f^T are the ANALYTIC complete cluster projectors
on the actual saturated invariant lattice. Each has rank two when
its two channels are distinct. The trace in (1) is the ordinary local
multiplicity-space trace from the source identity; the original
marked exterior has not been replaced by a trace invariant.

Let t=log(zeta/q), and let [t^r] denote Taylor COEFFICIENTS, rather
than unnormalized derivatives. If

    d_(e_i)d_(f_j)=a_ij,0+a_ij,1 t+a_ij,2 t^2+...,
    K_ij=W_N^2+k_ij,1 t+k_ij,2 t^2+...,
    [N]=c_N t+O(t^2),

then the second coefficient of (1) is EXACTLY

    sum_ij(a_ij,0 k_ij,2+a_ij,1 k_ij,1+a_ij,2 W_N^2)
                 =c_N^2 tr(E_e^S(q) E_f^T(q)).     (2)

Consequently the homogeneous first-normal Ward equation cannot simply
be imposed at second order. The additional overlap is a real physical
source quantity, rather than a removable convention.

## 2. An exact seven-level example

Take

    N=7, D=6, q=exp(pi i/7),
    a=b=c=d=2, e=f=2, e*=f*=4.

The ordinary invariant channel range is 0,1,2,3,4, so the saturated
invariant lattice has rank five. The root eigenvalue of channel 2
coincides precisely with that of channel 4. None of channels 0,1,3
shares it. Thus the complete selected cluster has rank two in EACH
pairing. Its projector is analytic at q by the proved cluster theorem.

Set r=q+q^-1=2cos(pi/7). In its real cyclotomic subfield,

    r^3-r^2-2r+1=0,
    W_7^2=(1+r)^2.                                (3)

Literal expansion of the FOUR actual seven-factorial germs in (1)
gives

    [t^0] sum_ij d_(e_i)d_(f_j) K_ij =0,
    [t^1] sum_ij d_(e_i)d_(f_j) K_ij =0,
    [t^2] sum_ij d_(e_i)d_(f_j) K_ij
                           =3444-5180r-6440r^2.   (4)

The leading quantum-integer coefficient is equally explicit:

    c_7=-14/(q-q^-1),
    c_7^2=-28-28r-56r^2.                          (5)

For an independent check of the division, ordinary polynomial
reduction modulo the cubic in (3) gives

    (-28-28r-56r^2)(24r^2+20r-11)
                          =3444-5180r-6440r^2.   (6)

Equations (1),(4)--(6) therefore prove the EXACT source identity

    tr(E_2^S(q) E_2^T(q))=24r^2+20r-11.           (7)

Since pi/7<pi/3, one has r>1. Hence (7) is strictly greater than
33, in particular strictly greater than two. No numerical rounding,
large-level extrapolation, or conjectural asymptotic is used.

The audit evaluates (4) directly in Q[q]/Phi_14(q), retaining the
actual generic t-series. In this example every individual Racah range
is tail-free, because the untouched opposite sum a+b+c+d=8<=12.
This makes the finite coefficient certificate especially short; it
does not substitute a semisimple root value for the source germ.
The calculation uses three Taylor coefficients of the root-unit
factorial products after canceling their actual common [7] zero.

## 3. Why this excludes every common orthogonal positive metric

Suppose H were a positive definite Hermitian form making BOTH
P=E_2^S(q) and Q=E_2^T(q) self-adjoint. They are idempotents, so in
an H-orthonormal basis they would be ordinary orthogonal projections.
For an orthonormal basis u_1,u_2 of the range of P,

    tr(PQ)=tr(PQP)=sum_(j=1)^2 <Q u_j,u_j>_H,
    0<=<Q u_j,u_j>_H<=1.

Thus tr(PQ)<=2. This contradicts (7). Trace is invariant under
simultaneous change of basis, so allowing a different physical gauge
or a nondiagonal positive form does not repair the contradiction.

This excludes simultaneous positive self-adjointness of the ACTUAL
complete cluster projectors, already at one finite level. It does
not exclude a positive form in which those projectors are nonorthogonal,
a metric adapted only to one pairing, a weighted source/dual energy
bound, or a direct bound on the scalar generic germs. The exact generic
bilinear source metric remains a separate, valid statement; a transpose
identity must not be turned into a Hermitian orthogonality identity.

## 4. Consequence for the higher-normal proof path

The first-normal bound uses exact positive generic presentations on
face-supported branches and first-order Ward/Fourier relations. A
higher-order extension must retain the overlap in (2), together with
its derivatives at subsequent orders, or find a different exact
positive presentation. The actual cluster projectors cannot be made
jointly orthogonal to bypass these terms.

This is an obstruction to that proposed METHOD, not a counterexample
to the general volume limit or to polynomial higher-normal scalar
bounds. Those bounds remain open outside the already proved face-
supported and tail-free branches.

Audit: [exact cyclotomic source calculation](../experiments/audit_actual_cluster_projector_positive_metric_obstruction.py)
and [recorded certificate](../experiments/actual_cluster_projector_positive_metric_obstruction_results.json).

Primary-agent analytical review checked the complete-cluster ranks, second-Taylor-coefficient Ward normalization, exact real-cyclotomic division and the positive-projection trace contradiction. Fresh replay of the exact N=7 certificate passed. This excludes the stated common orthogonal metric shortcut, not a general volume conjecture.
