# A rank-three actual source: two endpoint envelopes give a sharp norm

29 October 2026. The next repeated Newton twist/turn word has a genuine
cubic spectral cover and an interior forward dominant-modulus switch.
Nevertheless its ENTIRE positive original-source norm has a sharp limit.
The proof keeps its exact source currents, uses a gapped backward branch
only for the lower bound, and overlaps two full spectral-radius envelopes
for the upper bound. The required profile comparisons have finite
outward-rounded interval/Rouche certificates. No hyperbolic volume or
link identity is inferred from the resulting constant.

## 1. The actual source and both of its boundary vectors

Use T=T_1,P=P_rev and the unchanged original Newton metric. By the
[universal endpoint identity](actual_newton_run_endpoint_vectors.md),
(T^2P)^4 1 has, up to a unit scalar, coefficients

    v_i=kappa^(-2)(-q)^(i-d)K_i,
    K_i=sum_(j=0)^i nu_j [i choose j]_Q conjugate(P_(d-j)). (1)

Here P_i is the original Green sequence, not the turn matrix. Its
rank-three forced Ward, with G_i=K_i/F_i and M_i=F_i^3G_i, is proved
in [the endpoint theorem, section5](actual_twist_endpoint_gaussian_certificate.md).
Write its coefficients as B_i,C_i,D_i there. The exact monic equation is

    M_i+B_i M_(i-1)+C_i(1-Q^(i-1))^3 M_(i-2)
       -Q^3(1-Q^(i-1))^3(1-Q^(i-2))^4 M_(i-3)
                                             =Q^2 delta_(i,1). (2)

Negative-index terms are absent. Its literal data are
M_0=conjugate(P_d), M_1=(1-3Q+Q^2)conjugate(P_d)+Q^2;
D_2=0 fixes the next datum. In particular the source forcing has not
been deleted.

There is a regular exact backward equation. Put

    g_k=conjugate(F_k)^4 M_(d-k), Z_k=Q^(-k).

For every3<=k<=d,

    g_k=a_k g_(k-1)+b_k g_(k-2)+c_k g_(k-3),             (3)
    a_k=1+Q^(-1)+Q^(-2)-(4+Q^(-1))Z_k,
    b_k=[-Q^(-3)-Q^(-2)-Q^(-1)
                 +(3+4Q^(-1))Z_k-3Q Z_k^2](1-Q Z_k),
    c_k=Q^(-3)(1-Q Z_k)(1-Q^2 Z_k)^4.

All original currents are encoded in its INITIAL VECTOR. Let
S_0=sum_(j=0)^d conjugate(P_j). Exactly, for N>=3,

    g_0=N^2 S_0,
    g_1=N^2 Q^(-1)[(Q-3)S_0+2N],
    g_2=N^2 Q^(-4)[(Q^4-3Q^3-3Q^2+6Q+3)S_0
                                  +2(Q^3+Q^2-3Q-1)N].   (4)

For a direct proof of(4), root reflection gives

    K_(d-h)=nu_h sum_(j=h)^d [j choose h]_Q conjugate(P_j).

Writing S_m=sum_j Q^(mj)conjugate(P_j), the original finite Green
equation yields

    (1-Q^m)S_m+2Q^(m-1)S_(m-1)-Q^(m-2)S_(m-2)
                                      =N delta_(m,1 modN).

The actual inverse-crossing last row also gives S_(-1)=NQ: equivalently
sum_j Q^jP_j=NQ^(-1). These evaluate S_1,S_2 from S_0,N and give(4).
Reversing(2) and multiplying by the displayed fourth factorial proves(3).

The independently evaluated original endpoints give

    |M_0|~N^(3/2),
    S_0=N^(3/2)exp[-i pi(3-N)/4]+O(N).

Consequently (g_2,g_1,g_0)/g_0=(4,-2,1)+O(N^(-1/2)).
This is the nonzero dominant eigenvector at the backward endpoint.
The N terms in(4) are retained source currents, not arbitrary choices.

## 2. Spectral envelopes, and a source-selected backward lower bound

Put Y=e^(2iu),Z=e^(-2iu). The forward and backward principal cubics are

    f_u(lambda)=lambda^3+(-3+7Y-3Y^2)lambda^2
                    +(3-5Y)(1-Y)^3lambda-(1-Y)^7,
    b_u(lambda)=lambda^3+(5Z-3)lambda^2
                    +(3-7Z+3Z^2)(1-Z)lambda-(1-Z)^5.    (5)

Let rho_f,rho_b be their largest root moduli. They are continuous
and bounded below by1/3,2/3 respectively, by their traces.
Set I_e(u)=pi^(-1)integral_0^u log rho_e(t)dt, e=f,b.

Uniformly for all indices in any indicated compact u interval, the
actual matrix product has the spectral-radius upper bound

    log|M_i|<=N I_f(pi i/N)+o(N),
    log|g_k|<=N I_b(pi k/N)+o(N).                        (6)

This remains valid at modulus switches and the initial double fast
zero. Here is an elementary proof avoiding an ill-conditioned full
eigenframe. A bounded3x3 matrix of spectral radius at most1 has
||A^l||<=C(l+1)^2, uniformly in repeated roots: Newton interpolation
of z^l bounds its order0,1,2 confluent differences by the corresponding
complete homogeneous polynomials, of size at most (l+1)^2. The matrix
factors in that interpolation are uniformly bounded. Freeze the exact
smooth companion over blocks of length L=floor(N^(1/8)). Its step
error is O(L/N). Expanding the product in those errors bounds one block
by rho^L C L^2 exp(C L^4/N). Multiplying the blocks costs
O(N log L/L+L^3)=o(N) in its logarithm. Uniform continuity of log rho
gives the Riemann integral, uniformly also for partial final blocks.
Polynomial initial data add only O(log N). This proves(6).

The upper-bound mechanism is valid for ANY FIXED companion rank r,
not only this cubic. A uniformly bounded rank-r matrix with spectral
radius at most one has powers bounded by C(l+1)^(r-1), by the same
order-(r-1) confluent divided-difference formula. Freezing L steps
therefore costs at most rho^L C L^(r-1) exp(C L^(r+1)/N).
Over O(N/L) blocks the extra logarithm is
O(N log L/L+L^r). Taking L=floor(N^(1/(2r))) makes this o(N).
This requires a fixed-rank uniformly smooth actual recurrence, a
positive lower spectral-radius bound, and subexponential initial data;
it permits eigenvalue collisions and modulus switches. It is a FULL
spectral-radius upper envelope, not a lower bound or a license to
replace the radius by an arbitrarily selected single branch.

For every strict backward prefix0<=u<=u_0<pi/2 there is also a lower:

    log|g_k|=N I_b(pi k/N)+O_(u0)(log N).                 (7)

The [independent exact dominant-root certificate](actual_backward_cubic_dominant_source_certificate.md)
proves a unique simple dominant branch of b_u beginning at-2 on the
ENTIRE strict half-circle. Its two fast roots may coalesce at0.
Its regular dominant projection and a uniformly stable complement
power-Gram give source transport without diagonalizing those fast
roots. Equation(4) supplies the required actual nonzero projection
with relative O(N^(-1/2)) error. The exact backward equation is
homogeneous for k>=3, so no interior forcing is omitted in applying
that certificate. Summed dominant logarithms prove(7). This argument
does not transport a branch through the forward modulus switch.

## 3. One algebraic profile maximum and two finite comparisons

Let Lambda be Lobachevsky and define

    J_e(u)=I_e(u)+2Lambda(u)/pi, e=f,b.

Since M_i=F_i^2K_i and s_i s_(d-i)=N, (6) gives the two original
coefficient envelopes J_f(pi i/N) and J_b(pi(d-i)/N). The lower(7)
gives J_b at every fixed strict backward prefix.

The backward profile has exactly one first-half maximum u_*. Put

    p_6(z)=z^6-9z^5+29z^4-38z^3+10z^2+2z+1.

Its unique root z_* in[1,4] lies in(19/5,77/20), and
u_*=arcsin(sqrt(z_*)/2), so 2pi/5<u_*<pi/2. Indeed

    J_b'(u)=pi^(-1)log[rho_b(u)/(2sin u)^2].

Imposing |lambda|=z=4sin^2u in b_u and its conjugate and eliminating
lambda,Z gives z^24 p_6(z)^2=0. Exact Sturm counts give just two
positive roots of p_6 in[0,4]: one in(2/3,7/10) and z_* above.
The smaller cannot give rho_b=z because the product of the three
root moduli gives rho_b>=z^(5/6)>z when0<z<1. At u=pi/2 all roots
of lambda^3-8lambda^2+26lambda-32 have modulus<4: its unique real
root lies in(2,3), and the conjugate pair has modulus sqrt(32/r)<4.
Continuity now proves the claimed maximum. These eliminations use
full polynomials, not a sampled eigenvalue branch.

The forward profile is increasing: its root trace has modulus1+3z,
so rho_f>=z+1/3>z. Two further finite inequalities suffice for a
global overlap:

    integral_0^(2pi/5)log(rho_f/rho_b)du<0,
    integral_(2pi/5)^(pi/2)log[rho_b/(2sin u)^2]du<0.      (8)

The audit supplies rigorous interval bounds on WHOLE parameter cells.
For each cubic it chooses rational complex root centers and verifies
three disjoint disks by

    |p'(c)|_lower r > |p(c)|_upper+|p''(c)|_upper r^2/2+r^3.

Rouche therefore encloses all roots for EVERY parameter in that cell.
Their moduli bound rho and its logarithm. The small initial interval
uses a monic Cauchy bound and rho_b>=2/3. At4096 outward-rounded cells
the two certified upper bounds in(8) are respectively less than
-.0327 and-.0114. This is a finite proof of the comparisons, not
extrapolation from samples.

The first inequality makes J_f(2pi/5)<J_b(2pi/5). The second makes
J_b(pi/2)<J_b(2pi/5). Root-conjugation symmetry gives
J_b(pi-u)=2J_b(pi/2)-J_b(u), so J_b(3pi/5)<J_b(pi/2).
The only profile criticals before3pi/5 are u_* and its reflected
minimum. Therefore the maximum of J_b on[0,3pi/5] is J_b(u_*).
Use the forward envelope for i/N<=2/5 and the backward envelope
for i/N>=2/5. They cover EVERY physical index and neither exceeds
this backward maximum.

## 4. Whole original-source conclusion and scope

The polynomial number of positive norm terms gives the upper rate;
a rounded backward index near u_* and(7) give the matching lower.
For the literal original halfword A=(T_2P_rev)^4,

    lim_N N^(-1)log||A1||_Newt^2=2J_b(u_*).              (9)

Its original adjoint-word marked closure equals this positive norm
exactly. All Cartan lines and all fixed-root Casimir normals remain.
No value-only trace or arbitrary diagonal Newton coupon was substituted.
The assertion concerns fixed word depth before N tends to infinity.

This extends the source-aware folded Ward method to a genuine cubic
with an interior modulus switch. Its inputs are explicit resets,
the full opposite source vector, finite algebraic dominant-mode tests,
and finite certified envelope comparisons. It is not a general theorem
that an arbitrary scalar A-polynomial selects its largest root, and
it is not a new broad bridge-family or hyperbolic-volume claim.

Audit: [original source, exact folded current, algebraic criticals and interval spectral profiles](../experiments/audit_actual_newton_rank_three_folded_packet.py).

The proposed roots are used only after the stated Rouché validation. Finite source/current families, exact resultants and Sturm counts, and outward-rounded whole-cell disks check the formulas. No topological or volume identification follows.