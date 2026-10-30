# A polynomial bound for the actual partner normal on the physical grid

Subsequent complex estimate: the
[near-fold theorem](actual_q_hahn_near_fold_complex_partner_bound.md)
controls the full paired normal on a fixed complex compact when
(l-j) log N=o(N). It is a relative upper bound in a shrinking scaled
channel window; fixed nonzero scaled shifts and a leading normal
amplitude remain open. The theorem below retains its original scope.

30 October 2026. Every original physical magnetic entry of a complete
double Casimir channel has a polynomially bounded confluent normal
relative to its nonzero ordinary value. This includes both halves of
every physical degree block, both parities, and every complete double
channel. The estimate is for the ACTUAL generic divided difference.
It is not an estimate obtained by differentiating a root-only formula.

The argument is a positive-imaginary-part estimate for a half-prefix
of the original complex symmetric Casimir matrix, followed by its exact
reflection symmetry through first order at a double spectral node.
No complex magnetic continuation, global magnetic contour, or whole
marked-source estimate follows from this physical-grid statement.

## 1. The source and the quantitative statement

Put theta=pi/N, q=exp(i theta), Q=q^2, d=N-1, x=q^d. Let

    0<=j<l, j+l=d, l<=t<=d, 0<=u<=t,
    c_j=q^(2j+1)+q^(-2j-1),
    Delta_j=q^(2j+1)-q^(-2j-1).

All these indices are integers. Let C_(j,u) be the original root
column normalized by C_(j,0)=1. Let w_(j,u) be its actual confluent
normal as specified by
[the mixed compiler](actual_mixed_augmented_plat_compiler.md):

    w_(j,u)=[D C_(j,u)-D C_(l,u)]/[-2N Delta_j],
    D=zeta d/dzeta, evaluated at zeta=q.                (1)

Both generic columns in (1) use the original highest weight d and
its full factorial ratio. Then EVERY C_(j,u) is nonzero and

    |w_(j,u)/C_(j,u)|<=N^6/256+N^2/8.                 (2)

If t/N stays in a fixed compact subset of (0,1), the right side can
be replaced by C_K N^4. In the present complete range t>=l this
only requires a fixed upper separation from t/N=1. No separation
from the folded channel is required.

## 2. The actual prefix has positive imaginary part

The original degree-t Casimir block J_t is complex symmetric
tridiagonal, as proved directly from the balanced tensor operators in
[the complete Hermite packet](actual_complete_casimir_hermite_packet.md).
For r=0,...,t put U_r=Q^r, T=Q^t. Its entries simplify exactly to

    D_r=U_r/T [2(q^(-1)+qT)-(q+q^(-1))U_r],
    A_r=(U_r-T)(1-QU_r)/T,             0<=r<t.          (3)

Every A_r is nonzero. For 1<=m<=floor(t/2), let J_[m] be its
leading m-by-m principal submatrix. Because the matrix is symmetric,
its Hermitian imaginary part is the entrywise imaginary-part matrix.
Set h_r=(t-2r)theta and c=-cos((t+1)theta). Its diagonal and upper
offdiagonal imaginary parts, including the next boundary coefficient,
are

    d_r=4 sin(h_r)[c+cos(theta)cos(h_r)],
    o_r=4 sin(h_r-theta)sin((t-r)theta)sin((r+1)theta).
                                                               (4)

For 0<=r<m these o_r are positive. Introduce positive weights

    a_r=1/sin((t-r)theta),          0<=r<=m.

A direct sine expansion gives the EXACT weighted row identity

    d_r-o_(r-1)a_(r-1)/a_r-o_r a_(r+1)/a_r
      =4 sin(r theta)sin^2(theta)sin(t theta)
                         /sin((t-r-1)theta) >=0,       (5)

where the r=0 term involving o_(-1) is absent. The right side is
zero at r=0. All denominators in (5) are positive in the stated
range. One elementary verification expands sin(b-a) and
cos(a+b+theta), with a=r theta and b=(t-r)theta. After multiplying
by sin(b-theta)/4, the residual is precisely
sin(a)sin^2(theta)sin(a+b).

Conjugate Im J_[m] by diag(1,-1,1,...), so its offdiagonals are
-o_r. For a vector v write v_r=a_r y_r, and set y_m=0. Equation
(5) expresses its quadratic form as

    sum_(r=0)^(m-1) k_r |y_r-y_(r+1)|^2
           +sum_(r=0)^(m-1) V_r a_r^2 |y_r|^2,

    k_r=o_r a_r a_(r+1)
       =4 sin((t-2r-1)theta)sin((r+1)theta)
                                  /sin((t-r-1)theta),
    V_r=the nonnegative right side of (5).             (6)

There is a genuine Dirichlet term at the right endpoint; it is not
discarded when the prefix is taken. The conductances obey

    k_r>=4 sin(theta).                                (7)

Indeed the two numerator sine arguments alpha,beta are at least
theta, with alpha+beta=(t-r)theta<pi. On the interval
theta<=alpha<=alpha+beta-theta, their product is minimized at an
endpoint, so sin(alpha)sin(beta)>=sin(theta)
sin(alpha+beta-theta), which is (7).

Since a_r<=1/sin(theta) and
sum|y_r|^2<=m^2 sum|y_r-y_(r+1)|^2, equations (6),(7) prove

    Im J_[m] >= [4 sin^3(theta)/m^2] I.               (8)

The sign-conjugation is unitary and does not change this lower bound.
For t/N in a fixed compact inside (0,1), all a_r in this half-prefix
are uniformly bounded; the stronger lower bound is c_K/N^3.

## 3. Lower-half spectral derivatives

Let f_r(z) be the original normalized forward column,

    f_0=1, f_r(z)=det(zI-J_[r])/(A_0 ... A_(r-1)).      (9)

The real point c_j is a double eigenvalue of J_t. The actual source
and normal are exactly

    C_(j,r)=f_r(c_j),             w_(j,r)=f_r'(c_j).    (10)

This is the generic-confluence identity in the complete Hermite
packet and the mixed compiler: differentiating the two normalized
generic columns cancels the common q derivative and retains the
original eigenvalue-gap derivative -2N Delta_j.

For ANY real z, (8) gives

    ||(zI-J_[m])^(-1)||<=m^2/[4 sin^3(theta)].

In particular the determinant in (9) is nonzero there. Taking its
logarithmic derivative gives

    |f_m'(z)/f_m(z)|
       =|tr((zI-J_[m])^(-1))|
       <=m^3/[4 sin^3(theta)].                        (11)

Since m<=N/2 and sin(theta)>=2/N, (11) is at most N^6/256.
The compact-degree improvement of (8) gives C_K N^4 instead.
For m=0 the normal is zero and the value is 1.

## 4. Reflection extends the bound through the full physical block

Let P reverse the indices 0,...,t. Formula (3) gives exactly

    P J_t P=conjugate(J_t).                           (12)

The characteristic polynomial is

    p_(t+1)(z)=product_(m=0)^t(z-c_m),

and the forward column satisfies

    (J_t-zI)f(z)=-p_(t+1)(z)e_t/(A_0 ... A_(t-1)).     (13)

At a double node c_j, both the residual and its first derivative
vanish. Reflecting and conjugating (13), and using uniqueness of
the forward recurrence with its first component fixed, therefore
gives, at that node,

    f_(t-r)=f_t conjugate(f_r),
    f'_(t-r)=f'_t conjugate(f_r)+f_t conjugate(f'_r).    (14)

This is a first-order identity at a DOUBLE node. It is not inferred
by differentiating a value identity known only at isolated points.
One may justify (14) as an identity modulo (z-c_j)^2: the reflected
column has first entry conjugate(f_t(conjugate z)); its first-row
error is a multiple of p_(t+1)(z), so its forward recurrence agrees
to this order. Setting r=t in the value identity gives |f_t|=1.

The endpoint normal has a particularly simple ORIGINAL generic
calculation. At u=t only a=m survives in the generic Clebsch sum,
and its highest-vector ratio R_(m,m) is identically 1. Thus

    C_(m,t)(zeta)=(-1)^m
              zeta^[d(t-2m)+m(m-1)].                 (15)

The two exponents for j,l differ by N(l-j). Combining (15) with
the actual gap in (1) gives

    f'_t(c_j)/f_t(c_j)=-(l-j)/(2 Delta_j),
    |f'_t/f_t|<N/[4 sin(theta)]<=N^2/8.               (16)

For r>t/2 apply (14) with t-r in the lower half. Its value is
nonzero and

    f'_r/f_r=f'_t/f_t+conjugate(f'_(t-r)/f_(t-r)).       (17)

Equations (11),(16),(17) prove (2) for every physical entry.

## 5. Scope of the estimate

The paired normal, including its formerly hidden large-channel
contribution, is controlled on the entire physical grid. Its
exponential rate there cannot exceed that of its ordinary column
by more than O(log N)/N. This is a relative entrywise statement;
it does not control cancellations after a whole graph is sewn.

The high-total-degree blocks are transported by the constant
Chevalley-plus-flip adapter in the complete Hermite packet. Thus
the same root spectral-column estimate applies after the stated
physical index translation. It is the root confluent column being
transported here, not a new generic-q adapter assumed to be flat.

The estimate does NOT extend by continuity to a fixed complex
magnetic neighborhood. The canonical large-partner continuation has
the additional degree poles proved in
[the generic collision note](actual_q_hahn_partner_normal_collision.md),
and its finite tail requires a separate complex estimate. A bound
on integer magnetic samples, even at all levels, supplies no such
analytic continuation theorem.

Focused audit: [original normal, positive prefix and reflection](../experiments/audit_actual_q_hahn_physical_partner_normal_bound.py),
with [saved results](../experiments/actual_q_hahn_physical_partner_normal_bound_results.json).
The symbolic weighted-row identity passed. Exact arithmetic checked
131 original Casimir blocks, 726 weighted-row identities, 8,578
actual generic paired normals and their first-order reflections,
and 571 original endpoint normals. At 90 digits, 10,164 actual
relative-normal bounds passed; the audit also checked 288 positive
prefix matrices and 2,384 conductance inequalities. These finite
checks supplement the uniform proof above.

An independent analytical review checked the original source
conventions, weighted Dirichlet identity, conductance minimum,
Poincare bound and N^6 constant, the reflected recurrence modulo
the double characteristic zero, and the generic endpoint exponent
difference N(l-j). It also checked that the high-degree adapter
transports the actual root spectral column without assuming flatness
of an individual generic derivative. Its verdict covers the stated
physical-grid theorem only.

A second independent analytical review and fresh replay passed.
That reader verified the weighted row identity independently as a
formal Laurent identity, the alternating conjugation and boundary
Dirichlet term, the conductance and resolvent constants, and the
first-order reflection with the actual generic endpoint sign. The
fresh audit passed all reported exact and high-precision checks,
including 8,578 original generic paired normals and 571 endpoints.
No complex magnetic continuation or whole-source bound is inferred.
