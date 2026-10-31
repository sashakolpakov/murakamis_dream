# The even central trivalent packet, with its actual Jordan normal

29 October 2026. The nearest even central channel has its OWN exact
source evaluation. It is not replaced by the odd simple Steinberg
channel. Its coherent black-vertex scalar is a positive WEIGHTED
fourth-power sine-binomial sum, nonzero for every even N>=4, with
the same scalar exponential rate and prefactor as the odd anchor.
The complete circle's paired normal normalization and a bounded
physical Jordan preimage are explicit. The marked white vertex is
retained separately. No joint-color complex packet or global graph
survival/volume theorem is asserted.

Use the [literal branching vertices](actual_trivalent_complete_circle_vertex_kernel.md)
and the own finite binomial identities in the
[odd central proof](actual_trivalent_steinberg_central_anchor.md).

## 1. Actual even image, ordinary metric and complete-circle normal weight

Put N=2m>=4, d=2m-1, j=m-1, theta=pi/N,
q=exp(i theta), Q=q^2, x=q^d=-q^(-1), F_r=(Q;Q)_r.
The central folded Casimir is c=-2cos(theta), a DOUBLE root.
Its actual image module has highest weight2j=N-2 and dimensionN-1.
Its highest physical degree is m, with vector

    h=sum_(a=0)^m h_a |a,m-a>,
    h_a=q^(a^2)[m choose a]_Q=q^(ma) beta(m,a).          (1)

The literal Ecal_pair highest-vector equation is the ratio(2) of the
odd proof, so (1) is independently valid at the even root. Define

    W_r=F_pair^r h/F_r, 0<=r<=2j.                     (2)

These columns give a genuine embedding of the ordinary highest-weight
2j module Q_j into the physical pair, with all arrows before the last
nonzero. Its divided-F basis has exact positive single-object metric

    G_rr=beta(2j,r)=|1-Q^(r+1)|/|1-Q|.                (3)

This follows from s_r s_(d-r)=N and 2j=N-2, or directly from the
actual ladder norms. In particular1<=G_rr<=1/sin(theta), so changing
between this ordinary basis and its positive normalized basis costs
only a power of N.

The actual CD factor of the complete circle on this central image is

    F_central[:,r]=sqrt(h0/G_rr) W_r
                  =2sqrt(N/|1-Q^(r+1)|) W_r,
    h0=4N/|1-Q|.                                     (4)

To prove (4), at the lowest degree m the full paired CD coefficient is
2s_m^2/s_1=4N/s_1, since s_m^2=2N. The inclusion is a Hopf map;
the normalized target ladder then supplies exactly G_rr in(3).
Equivalently the full-degree canonical CD vector/weight formula gives
(4) entry by entry. This is the POSITIVE coefficient created by the
actual first normal of L_N at its double zero. It is not its zero
Casimir value. Indeed

    W^dagger P W=0.                                   (5)

The image is P-isotropic, unlike the odd simple image. Thus using
W^dagger P as an inverse frame or copying the odd P-isometry would
delete the paired source normal.

The finite Clebsch formula(5) of the odd proof remains valid with the
highest m in(1) and r<=2j. Two exact endpoint evaluations are now

    W_(2j)(j+t,d-t)=q^j h_t, 0<=t<=m,
    W_j(0,d)=q^(-j^2),
    W_j(a,d-a)=q^(-j^2) f_a(c).                        (6)

Here f_a are the actual middle-degree continuants, not distinct-value
normal replacements. For the first identity the lowest-vector equation
has the same successive ratio as h. Its first scalar, by factorial
reflection and finite Vandermonde, is

    q^(-j^2) sum_s Q^(s^2)[m choose s]_Q[j choose s]_Q
      =q^(-j^2) F_d/(F_m F_j)=q^j.

The middle first entry is x^(-j)F_d/(F_mF_j)=q^(-j^2).
All denominators have index<N. This proves every phase in(6) directly.

## 2. Exact coherent scalar and the full central black tensor

Let J_source=p_16 p_23 p_45 be the original nested cup source. For
the moment use the unweighted rows W^dagger P at its three pair ports.
At the magnetic indices(2j,j,0), its black coefficient is N^3 A_N,
where (6) gives

    A_N=q^(-j) sum_(k=0)^m x^(k-N)
                  conjugate(h_k^2 W_j(j+k,m-k)).        (7)

This includes the conjugate q^(-j) of the LOWEST Clebsch scalar in(6).
No extra turn or framing scalar is omitted. The exact evaluation is

    A_N=q^[1-m(m-1)] S_N,
    S_N=sum_(k=1)^(m-1) sin(k theta)cos(k theta) beta(m,k)^4. (8)

Every term is positive. Thus S_N>0 for every even N>=4. At N=2
the sum is empty, consistently with the vanished three-circle source.

The properly balanced ordinary-channel row is G^(-1)W^dagger P,
which is a genuine Hopf map. The ordinary triple invariant is one
dimensional: its third-color-zero slice is the one-dimensional
lowest-vector kernel of F on Q_j tensor Q_j, and the E recurrence
uniquely determines every later slice since its third-leg coefficients
are nonzero. This is also obtained from its regular generic trivalent
vector, whose explicit ladder denominators here all have index<N.
Normalize that tensor Theta_j to value1 at(2j,j,0). Therefore the whole
balanced black tensor is

    U_bal=(N^3 A_N/G_jj) Theta_j.                      (9)

In the actual positive CD coordinates(4) it becomes

    U_CD(r1,r2,r3)=h0^(3/2) product_i sqrt(G_ri,ri)
                                      U_bal(r1,r2,r3),
    U_CD(2j,j,0)=h0^(3/2) N^3 A_N/sqrt(G_jj).          (10)

Thus the full central black packet is known up to a genuine ordinary
3j tensor, with its scalar and every normal/positive normalization
explicit. The ordinary and marked white packets are STILL their
distinct full kernels; (9) is not a claim that the marked row is a
zero-current invariant covector.

## 3. Own finite proof of the weighted quartic identity

Use the FULL actual anti-Pascal recoupling mathcal J, reserving J_source
for the cups. At this even root its factorial reflection form is

    mathcal J_(a,b)=q^(-1) D_a D_b [a+b choose a]_(Q^(-1)),
    D_a=(-q^(-1))^a, a+b<=d; zero otherwise.

The own finite inversion proof of the odd note works at this root too:
conjugate(mathcal J) P mathcal J=P. Set f=(f_a(c)) and y=mathcal J f.
The actual upper-bidiagonal Casimir recurrence gives

    y_a=0, a<m;
    y_(m+k)=beta(j,k)^2/sin((k+1)theta), 0<=k<=j.       (11)

The repeated diagonal entries occur at j=m-1 and m; their nonzero
joining arrow forces the earlier eigenvector entry y_j to vanish.
Afterward the ratio is cos^2(k theta)/[sin(k theta)sin((k+1)theta)].
The last entry y_d=f_0=1 fixes the stated constant. This uses the
actual repeated-node eigenvector, not two artificial simple channels.

Put b_k=beta(m,k)^2. Its endpoint relation is
beta(j,k)=cos(k theta)beta(m,k). On the tail indexed by a=j+k,
write w_a=q^(-k)b_k. Equations(6),(7) simplify to

    A_N=-q^[j^2-j] conjugate(f)^T w.

Let z=P y and t=P w, extending them by zero through indexm. Then

    z_i=cos(i theta)b_i, 0<=i<=m (so z_m=0),
    t_i=-i q^i b_i, 0<=i<=m.

Full P-unitarity gives conjugate(f)=P mathcal J P y, hence the source
scalar is -q^[j^2-j] z^T mathcal J t. Every nonzero term has indices
a<=m-1,b<=m, so a+b<=d: no forbidden top-right matrix entry is added.

For a parameter a define the finite transform

    T_k(a)=sum_(i=k)^m b_i(-1)^i a^i [i choose k]_(Q^(-1)).

The finite Durfee factorization used in the odd proof gives

    z^T mathcal J t=q^(-1) sum_k Q^(-k^2) Z_k T'_k,
    Z_k=[T_k(1)+T_k(Q^(-1))]/2, T'_k=-i T_k(1).        (12)

Put n=m-k. Converting all Gaussian factors to Q gives exactly

    T_k(a)=(-1)^k a^k Q^[k^2-mk][m choose k]_Q^2
       *2phi1(Q^(-n),Q^(-n);Q^(k+1);Q,a Q^(1-k)).       (13)

At a=1 the second finite q-Chu applies, because its required argument
cQ^(2n)=Q^(1-k). It gives

    T_k(1)=(-1)^k q^[(m-k)^2] sin(k theta)b_k,
                                                    1<=k<=m. (14)

Indeed the Pochhammer ratio(-Q;Q)_(m-k)/(Q^(k+1);Q)_(m-k)
has magnitude sin(k theta) and phase q^[(m-k)^2]. At k=0 that ratio
has its EXACT zero factor1+Q^m, so T_0(1)=0.

One contiguous step evaluates the second term in(12). For the finite
q-Chu polynomial F(z)=2phi1(Q^(-n),b;c;Q,z), at z=cQ^n/b, subtract
F(z) from F(z/Q), cancel1-Q^r and shift the index. The remaining
length n-1 polynomial is AGAIN second q-Chu, with parameters bQ,cQ.
This gives

    F(z/Q)/F(z)=1+(1-Q^(-n))(1-b)(z/Q)/(1-z/Q).         (15)

Here b=Q^(-n)=-Q^k and z/Q=Q^(-k). Including a^k in(13) yields

    T_k(Q^(-1))/T_k(1)=(1+3Q^(-k))/(1-Q^(-k)),
    Z_k=T_k(1)(1+Q^(-k))/(1-Q^(-k)), 1<=k<=m-1.       (16)

There is no division at k=0: T'_0=0, so its contribution in(12) is
zero. At k=m, Z_m=0 directly. For the remaining indices
(1+Q^(-k))/(1-Q^(-k))=-i cot(k theta). Also
Q^(-k^2) T_k(1)^2=(-1)^m sin^2(k theta)b_k^2.
Consequently

    z^T mathcal J t=-(-1)^m q^(-1)
                   sum_(k=1)^(m-1) sin(k theta)cos(k theta)b_k^2.

Multiplying by -q^[j^2-j] gives(8), since
(-1)^m q^[j^2-j-1]=q^[1-m(m-1)] (their exponent difference is
2N(m-1)). This proves the actual coherent positive scalar with the
paired normal retained throughout.

## 4. A bounded actual Jordan preimage, and its nonzero Ward current

At the lowest degree T=m, let v(z) be the actual Jacobi continuant
vector with first entry1, so v(c)=h. Its block characteristic polynomial
has a DOUBLE zero at c. Differentiating the finite continuant equations
therefore gives (Omega-c)v'(c)=h, including the last row. Put

    n=v'(c)/L_N'(c),
    L_N'(c)=-N/[2sin^2(theta)].                        (17)

Then, as ACTUAL physical vectors,

    L_N n=h,
    h^dagger P h=0,
    h^dagger P n=1/h0.                                (18)

The last identity follows from L_N P=h0 h h^dagger in this degree.
This is a genuine Jordan preimage rather than division by the zero
value L_N(c). For every polynomial B, its complete local action is

    B(Omega)h=B(c)h,
    B(Omega)n=B(c)n+[B'(c)/L_N'(c)]h.                  (19)

Thus its first normal is explicitly retained. These two vectors are
an analysis frame for this lowest paired block, NOT a new source
coupon or a claimed frame for the entire physical projective module.

There is no exponential EXTRA cost in this normal. Write v'_a(c)=h_a H_a,
H_0=0. The symmetric Jacobi equation gives its exact discrete current

    H_(a+1)-H_a=(sum_(r=0)^a h_r^2)/(t_a h_a h_(a+1)),
    t_a=Q^[-m+a](1-Q^(m-a))(1-Q^(a+1)).                (20)

Finite Vandermonde gives sum_(r=0)^m h_r^2=[2m choose m]_Q=0.
The magnitudes beta(m,a) increase to their midpoint and then decrease.
Use the forward partial sum before that midpoint and its NEGATIVE
backward tail afterward. The numerator is then at most N times the
smaller appropriate adjacent magnitude squared, yielding

    |H_(a+1)-H_a|<=N/|t_a|<=N^2/8,
    max_a |H_a|<=N^3/16,
    |n_a|<=(pi^2/8)|h_a|.                             (21)

Here |t_a|=4cos(a theta)sin((a+1)theta)>=4sin(theta)>=8/N,
and |L_N'(c)|>=N^3/(2pi^2). The estimates hold also at the endpoints.
The factorial/exponential profile already in h is kept; no claim that
h itself is polynomially bounded in the physical metric is made.

The source normal is NOT highest. Its exact omitted-if-one-dropped-it
Ward current is

    Ecal_pair n=[x/(2L_N'(c))] h_previous,
    (h_previous)_a=q^(a^2)[m-1 choose a]_Q.             (22)

Indeed Ecal_pair n is the unique c-eigenvector in degree m-1, and
its first component follows from n_0=0 and n_1=1/(t_0 L_N'(c)).
That vector is a genuine extension direction, not to be set to zero
to imitate the odd simple source. The marked vertex likewise remains
the exact distinct Vm of the branching theorem; no zero-current
covector is substituted for it.

## 5. Common scalar asymptotic, and its limits

With j0=v8/pi from the odd central proof, the EVEN positive sum in(8)
satisfies

    S_N=(1/4)N^(-3/2)exp(N j0)(1+O(N^(-1))).           (23)

Here s_m^2=2N exactly, and there is no odd affine shift in m/N=1/2.
The local fourth-power density is N^(-2)exp[Nj0-4pi u^2] for
k=m/2+sqrt(N)u. Its extra sin(k theta)cos(k theta) tends to1/2.
The Gaussian integral is1/2, giving again1/4. Symmetry removes odd
terms, and the strict sine-factorial profile gives the same global
gap and O(1/N) Laplace error as in the odd proof.

The actual CD highest coefficient in(10) consequently has magnitude

    (sqrt(2)/(2pi)) N^4 exp(Nj0)(1+O(N^(-1))),         (24)

with its exact phase q^[1-m(m-1)]. Its DIFFERENT polynomial power
from the odd coefficient N^3/4 is the retained paired-normal CD
normalization, not a new exponential. Equations(8),(23) together
with the odd theorem give a nonzero central scalar at BOTH level
parities. They do not produce a uniform analytic packet for shifted
joint colors, a full projective frame, a tame marked-vertex norm,
or a global Casson--Rivin maximum. Those remain additional tasks.

Audit: [literal even Clebsch/normal, contiguous finite transform, marked kernel and scalar density](../experiments/audit_actual_trivalent_even_central_normal_packet.py).

The full marked packet, noncentral joint-color continuation and global graph estimates remain outside this central theorem.