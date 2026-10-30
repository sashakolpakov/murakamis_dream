# The full original Casimir resolvent is polynomial at the spectral endpoint

30 October 2026. The original physical
Casimir has a uniformly polynomial resolvent at z=2, including all
degrees, both level parities and its Jordan blocks. Fixed genuine
generic-q and spectral derivatives have polynomial cost on an explicit
shrinking neighborhood. This addresses a finite endpoint of the exact
operator contour; it does not prove dominance of a geometric saddle
or control an entire contour segment merely from its endpoint.

## 1. Uniform statement

Put q=exp(pi i/N), d=N-1, N>=3, and use the ACTUAL generic physical
matrix J_t(zeta) from the
[original jet theorem](actual_q_hahn_physical_generic_jet_bound.md).
For every 0<=t<=d there is an absolute constant C such that

    ||(2I-J_t(q))^-1||op<=C N^17.                  (1)

The exponent is a conservative uniform bound, not an optimal rate.
The same bound holds for every high-degree block, by the exact
generic high-degree adapter, and for their full orthogonal direct sum.

For sufficiently small absolute c>0, on the bidisk

    zeta=q exp(h), |h|<=cN^-19, |z-2|<=cN^-18,

the resolvent exists and has norm at most 2C N^17. Consequently its
mixed Taylor coefficients satisfy

    ||[h^r(z-2)^s](zI-J_t(q exp(h)))^-1||op
       <=C_(r,s) N^(17+19r+18s).                  (2)

These are the original matrix normals, with distinct generic upper
and lower entries. No semisimple projection or root-only reflection
is differentiated in (2).

## 2. The exact ground-state congruence

Write theta=pi/N, lambda_0=q+q^-1, delta=2-lambda_0=4sin^2(theta/2).
The original normalized channel-zero vector is

    f_r=(-q^-1)^r.

The root offdiagonal and its positive magnitude are

    A_r=-a_r q^(2r+1-t),
    a_r=4sin((t-r)theta)sin((r+1)theta)>0, 0<=r<t.

The exact row identity proved in the
[off-spectrum prefix theorem](actual_casimir_off_spectrum_prefix_action.md)
is D_r=lambda_0+q^-1 A_r+q A_(r-1), with A_(-1)=0.
For a leading m-by-m prefix, m<=t, let F=diag(f_0,...,f_(m-1))
and let L_m be the REAL weighted Dirichlet matrix with diagonal
a_(r-1)+a_r and offdiagonals -a_r, retaining the right boundary
conductance a_(m-1). Then exactly

    F(J_[m]-lambda_0 I)F=-q^-t L_m,
    F(J_[m]-2I)F=-q^-t(L_m+delta V_m),
    V_m=diag(q^(t-2r)).                            (3)

This is a unitary congruence, not a unitary similarity. Its left and
right factors nevertheless preserve singular values and determinant
magnitudes. Thus it can be used for inverse norms without claiming
that J is Hermitian.

The positive matrix L_m has the elementary exact formulas

    det L_m=product_(r=0)^(m-1) a_r,
    tr L_m^-1=sum_(r=0)^(m-1)(r+1)/a_r.            (4)

Indeed L_m=B^T diag(a_r)B, where (Bv)_r=v_r-v_(r+1) and v_m=0.
The inverse of B has ones above its diagonal; (4) follows directly.

## 3. Both halves are controlled, even when t approaches N-1

Suppose 1<=m<=floor(t/2)+1 and m<=t. Every argument (t-2r)theta
in V_m lies in [0,t theta], and t theta<=pi-theta. Rotation by
exp(-it theta/2) therefore gives

    Re[exp(-it theta/2)(L_m+delta V_m)]
       >=cos(t theta/2)(L_m+delta I).

Since cos(t theta/2)>=sin(theta/2)>=1/N and delta>=4/N^2,

    ||(J_[m]-2I)^-1||op<=N^3/4.                  (5)

This remains uniform at the folded physical endpoint t=N-1.
For these same half-prefixes one has

    a_r>=4(r+1)^2/N^2.                            (6)

For r=0 use sin(t theta)>=sin theta>=2/N. For r>=1,
r<=t/2 and t<=N-1 put t-r in [r,N-r-1]. Both sine factors in
a_r are at least 2r/N, giving a_r>=16r^2/N^2 and hence (6).
Equations (4),(6) show

    delta tr L_m^-1<= (pi^2/4)(1+log N).

Expansion in the diagonal perturbation gives an especially simple
determinant bound: all principal minors of L_m are positive, and
every diagonal entry of V_m has modulus one. Therefore

    |det(L_m+delta V_m)|<=det(L_m+delta I)
       <=det L_m exp(delta tr L_m^-1)
       <=C N^3 product_(r=0)^(m-1) a_r.            (7)

This is an upper bound for the ACTUAL determinant; no estimate on
individual nonorthogonal spectral projectors was used. The trailing
half at the root is the reflected conjugate of a leading half, so
(5),(7) apply to it too. Only these root norm statements use reflection.

## 4. The exact full determinant prevents a small Schur denominator

The actual characteristic polynomial gives

    chi_t(2)=det(2I-J_t(q))
       =product_(r=0)^t [2sin((r+1/2)theta)]^2>0.   (8)

Let s_t=product_(r=1)^t 2sin(r theta). Then

    product_(r=0)^(t-1)a_r=s_t^2,
    chi_t(2)/s_t^2>=4/N^2.                        (9)

Here is an elementary uniform proof of the second inequality. The
positive sequence

    H_t=product_(r=0)^t 2sin((r+1/2)theta)/s_t

has successive ratios sin((t+1/2)theta)/sin(t theta). They are first
at least one and then at most one, so its minimum occurs at an
endpoint. The cyclotomic products give H_(N-1)=2/N, while
H_0=2sin(theta/2)>=2/N. Squaring proves (9).

For t>=1 split J_t-2I between its two middle rows. Its diagonal
blocks B,C have sizes floor((t+1)/2), ceil((t+1)/2), so (5),(7)
apply. Let A be their single connecting root offdiagonal and
a=|A|<=4. In (7) the connecting conductance occurs in BOTH
Dirichlet halves. Consequently

    |det B det C|<=C N^6 a s_t^2.

The two-by-two bridge correction has determinant

    Delta=1-A^2(B^-1)_(last,last)(C^-1)_(first,first)
         =det(J_t-2I)/(det B det C).

Using (8),(9) and a<=4 yields

    |Delta|>=c N^-8.                              (10)

Every entry of its adjugate is bounded by C N^3 by (5). Its inverse
therefore has norm at most C N^11. The rank-two resolvent formula,
with two diagonal-block inverse factors of norm at most C N^3,
gives C N^(3+3+11)=C N^17 for the whole inverse. This proves (1).
The case t=0 is the scalar inverse delta^-1<=N^2/4.

This argument controls the actual full Jordan resolvent; it does not
bound it by a sum of exponentially large individual projector norms.

## 5. The original generic normals and the contour qualification

Every exponent in the displayed original generic matrix entries is
O(N), and the bandwidth is fixed. On |h|<=c/N the matrix perturbation
has operator norm at most C N|h|, uniformly in physical t. Combining
this with (1), the two perturbations h and z-2 on the stated bidisk
have relative inverse norm less than 1/2 for sufficiently small c.
The Neumann resolvent formula proves the uniform bidisk bound;
two-variable Cauchy gives (2). This argument starts from the genuine
generic matrix and so retains all moving-node and moving-projector
contributions automatically.

The endpoint matters because the largest root Casimir node tends
to 2, while the source-polynomial zeros approach 2 from above. A
fixed contour enclosing all nodes cannot remain a fixed compact
of the scalar limiting slit plane. Equations (1),(2) provide uniform
finite control at 2 and on the displayed shrinking neighborhood.
They do not alone estimate the path connecting that neighborhood
to a fixed contour, establish a steepest-descent deformation, or
show that the geometric contribution is nonzero.

Focused audit: [actual ground-state congruence, halves and full endpoint resolvent](../experiments/audit_actual_casimir_endpoint_resolvent_bound.py).

Primary and independent analytical reviews: PASS. The independent read
checked the unitary congruence rather than a claimed similarity, the
two half-block bounds uniformly through t=N-1, the duplicated bridge
conductance, exact characteristic-product lower bound and full Schur
denominator, and the genuine generic perturbation. A fresh independent
replay passed 187 original full blocks, 5,030 congruence entries, 251
half-inverse, positive-determinant and trace checks, 187 characteristic
products, and 170 exact Schur determinants. The numerical full norms
are diagnostics; the stated uniform exponent comes from the proof.
No contour deformation or geometric contribution is included in these
reviews.
