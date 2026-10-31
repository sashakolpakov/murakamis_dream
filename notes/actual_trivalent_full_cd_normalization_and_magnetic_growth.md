# Full trivalent CD normalization and an actual magnetic-growth obstruction

29 October 2026. The complete-circle image on EVERY physical pair has
an exact ordinary-channel normalization. This lifts a black scalar to
its entire magnetic tensor, but does not preserve the scalar's growth
rate. An explicit coefficient of the already proved odd central tensor
has rate 5j0/4, where its scalar has rate j0=v8/pi. Thus even the
central scalar cannot be used as an upper bound for the full CD vertex
norm. This is a source-exact obstruction, not a conjecture about a
candidate Racah formula or a counterexample to a volume conjecture.

## 1. Original modules and the general positive single-object metric

Use the full physical conventions of
[the positive-circle quotient](actual_complete_circle_positive_quotient.md):
N>=2, d=N-1, q=exp(pi i/N), Q=q^2, x=q^d, F_a=(Q;Q)_a,
s_a=|F_a|, and the complete physical module V_N. On V_N tensor V_N
write E_t,F_t,K_t for the original ordered coproduct, Omega for the
actual Casimir, P for physical leg exchange, and L=L_N. In particular

    E_t^dagger P=-P F_t, F_t^dagger P=-P E_t,
    H=L P>=0, C=P L>=0.                               (1)

Put M=floor(d/2). At folded node c_j=q^(2j+1)+q^(-2j-1), 0<=j<=M,
set t_j=d-j and define the first-entry-one highest vector

    h^(j)=sum_(a=0)^t_j q^(a^2)[t_j choose a]_Q |a,t_j-a>,
    W_(j,r)=F_t^r h^(j)/F_r, 0<=r<=2j.               (2)

Its literal highest ratio is -x^(-1)Q^a(1-Q^(t_j-a))/(1-Q^(a+1)).
Its highest K is q^(2j), and its Casimir is c_j. The established
full paired-image theorem gives one image vector in each degree
t_j,...,t_j+2j; their nonzero ladder coefficients show that (2)
is an injective ACTUAL Hopf map W_j:Q_j->V_N tensor V_N, where
Q_j is the ordinary (2j+1)-dimensional module. No root semisimplification
is used. At odd j=M it is the simple Steinberg module V_N.

In this divided-F basis its matrices are

    K_j|r>=q^(2j)Q^(-r)|r>,
    F_j|r>=(1-Q^(r+1))|r+1>,
    E_j|r>=q^(-2j-1)(1-Q^(2j+1-r))|r-1>.

Every interior coefficient is a unit at the root. Define

    G_(j,r)=beta(2j,r)=s_(2j)/[s_r s_(2j-r)],
    G_j=diag(G_(j,r)).                                 (3)

This is positive. Its ratio is
sin((2j+1-r)pi/N)/sin(r pi/N), so DIRECTLY

    E_j^dagger G_j=-G_j F_j, K_j^dagger G_j K_j=G_j.    (4)

It is a metric of one ordinary object. A tensor coproduct is not
therefore unitary in its product metric: its adjoint reverses order.

## 2. Exact full-degree CD normalization

Let H_j be the ACTUAL c_j summand of L P, after L has acted with
its first normal on a paired block. Its full column factor is

    H_j=h0_j W_j G_j^(-1) W_j^dagger,
    F_j[:,r]=sqrt(h0_j/G_(j,r)) W_(j,r),                (5)

where

    h0_j=2 s_(d-j)^2/s_(d-2j)=2N beta(2j,j), 2j<d,
    h0_(d/2)=N,                              2j=d.    (6)

The first equality in(6) is the exact canonical CD coefficient in
the first degree t_j, whose eigenvector has first entry one. Root
reflection s_a s_(d-a)=N gives its second form. The simple odd node
has HALF the paired prefactor. It is not continued as two simple
copies of a double node.

Here is a proof that the same constant fixes EVERY magnetic row.
The original covariance and centrality of L imply

    F_t H_j=-H_j E_t^dagger.

The range of H_j is W_j(Q_j). Since H_j preserves physical integer
degree and W_(j,r) have distinct degrees, write
H_j=sum_r a_r W_(j,r)W_(j,r)^dagger. The covariance gives
a_(r+1)/a_r=G_(j,r)/G_(j,r+1). Its first coefficient is h0_j,
so (5) follows. This uses actual physical arrows and the original
positive circle, not a presumed unitary Clebsch frame.

The correctly typed channel map is

    pi_j=G_j^(-1) W_j^dagger P.                       (7)

It is a Hopf map by(1),(4). On paired nodes pi_j W_j=0; on the odd
simple node it is I. Indeed L W_j is zero or N W_j respectively,
and (5) gives exactly these compositions. In particular the paired
map is not a retraction. Equations(5)--(7) retain the normal source
before passing to the ordinary image.

These factors need not be polynomial away from the center. Uniformly
on physical indices, with Lcal(u)=integral_0^u log(2sin pi v)dv,

    log beta(2j,r)
      =N[Lcal(2j/N)-Lcal(r/N)-Lcal((2j-r)/N)]+O(log N). (8)

For example j/N near1/4,r near j has strictly positive exponential
rate j0/4. Separate bounds on the factors in(5) can lose the
cancellations of a specific magnetic coefficient.

## 3. The whole black source, its true support and its 3j tensor

Let J_source=p_16 p_23 p_45 be the literal nested six-head cup,
with p_(a,b)=N x^(-b)delta_(a+b,d). For any fixed triple j_1,j_2,j_3
put

    U_bal=(pi_j1 tensor pi_j2 tensor pi_j3) J_source,
    J=j_1+j_2+j_3.

It is an ACTUAL invariant of Q_j1 tensor Q_j2 tensor Q_j3. Its
physical support gives the TRUE integer condition

    r_1+r_2+r_3=J, 0<=r_i<=2j_i.                     (9)

It vanishes unless the ordinary triangle inequalities hold. The
invariant space in this H=0 sector is at most one-dimensional.
To see this, let v_r be its third magnetic slice. The first slice
satisfies F_12 v_0=0 at degree J. The rectangular bidiagonal F_12
has a one-dimensional kernel exactly in the triangle range and
is injective, or has empty domain, outside it. Every later slice
is forced by

    v_r=-K_j3(r-1)/E_j3(r-1,r) E_12 v_(r-1).          (10)

Its denominators are units. An explicit ordinary trivalent tensor
Theta_j is obtained from that lowest-vector kernel and (10), with

    Theta_j(2j_1,j_2+j_3-j_1,0)=1.                   (11)

For completeness its initial F-kernel ratios are

    v_0(a+1,J-a-1)/v_0(a,J-a)
       =-K_j1(a+1)(1-Q^(a+1))/(1-Q^(J-a)).            (12)

All required indices lie in the physical ranges below N. These are
also the regular finite ordinary Clebsch recursions before root
specialization; their initial nonzero column and nonzero interior
arrows give the stated canonical tensor. The top E endpoint is
the same finite intertwiner identity, with no division by F_N.

There is a stronger original-source restriction:

    U_bal=0 whenever J<d.                            (13)

This is the cleared missing-corner identity of the
[actual saturated three-circle source](actual_six_port_three_circle_support.md),
applied to the genuine six-head cup. Its complete-circle observation
is exactly ||(F_j1^dagger tensor F_j2^dagger tensor F_j3^dagger)
P_ports J_source||^2. The source Ward identity annihilates it outside
J>=d. Positivity then annihilates the black tensor itself. Odd simple
axes are included by that proof. This is not inferred from an
ordinary semisimple fusion rule. For J>=d the triangle inequalities
already follow from j_i<=M, but(13) is not by itself a nonvanishing
assertion.

Let the unweighted source coefficient at the magnetic point(11) be
N^3 A_j, namely take rows W_j^dagger P before dividing by G_j.
Then the ENTIRE tensor is exactly

    U_bal=[N^3 A_j/G_(j2,j2+j3-j1)] Theta_j,
    U_CD(r)=sqrt(h0_j1 h0_j2 h0_j3)
                         product_i sqrt(G_(ji,ri)) U_bal(r). (14)

This supplies the precise interface for any independently proved
scalar formula. It does not assign that scalar's rate to the whole
tensor, nor bound the marked white packet by an ordinary covector.

## 4. An unconditional central magnetic-growth counterexample

Now take odd N=2m+1 and all three j_i=m. Then G_j=I,h0_j=N exactly.
The already proved
[central actual source](actual_trivalent_steinberg_central_anchor.md) gives

    U_CD=N^(7/2)q^(-m^2) A_N Theta,
    Theta_(a,b,c)=N x^(-c) W_(d-c)(a,b),
    A_N=q^[m(2-m)] sum_k beta(m,k)^4.                 (15)

Here Theta uses its physical normalization, not the normalized (11).
Its exact lowest-column formula is W_d(m+k,d-k)=h_k, with
|h_k|=beta(m,k). Therefore an ACTUAL magnetic coefficient is

    U_CD(m+k,d-k,0)=N^(9/2)q^(-m^2) A_N h_k.          (16)

At k nearest m/2, the same affine-shift Laplace expansion already
proved for the scalar gives

    beta(m,k)=2^(-1/4)N^(-1/2)exp(Nj0/4)[1+O(1/N)],
    |A_N|=(1/4)N^(-3/2)exp(Nj0)[1+O(1/N)].

Consequently, at odd levels with that chosen nearest magnetic index,

    |U_CD(m+k,d-k,0)|
      =2^(-9/4)N^(5/2)exp[(5/4)Nj0][1+O(1/N)],       (17)
    liminf_(N odd) N^(-1)log ||U_CD||_2^2 >=(5/2)j0.  (18)

This is the original positive three-circle black energy
J_source^dagger C_St^tensor3 J_source, in a valid CD factor of the
actual circles. Changing that factor by a unitary frame leaves the
energy unchanged. It is not a freely selected abstract inner product.

Thus an upper bound exp[Nj0+o(N)] for the FULL vertex amplitude,
or exp[2Nj0+o(N)] for its Euclidean CD energy, is FALSE. A metric
subexponentially equivalent to that CD metric cannot repair it.
A rescaling must retain its corresponding co-source dual cost.

## 5. Consequences for coherent graph sewing

The scalar C R partition, when identified with A_j by its exact
source proof, can control a specific normalized magnetic coefficient.
Equations(14)--(18) show why it does not by itself control the
remaining magnetic sums. Ordinary white Hopf covectors, the sole
marked row, genuine bends and their pivotal factors may contract
that growth coherently. They must be sewn BEFORE a sharp energy
estimate is asserted. Nothing here contradicts a knot-volume bound
or rules out a different coherent positive metric on the complete
pointed source. It rules out precisely the scalar-to-full-CD-norm
shortcut, already at the actual odd central anchor.

The [focused exact source audit](../experiments/audit_actual_trivalent_full_cd_normalization_and_magnetic_growth.py)
passes eight all-parity physical levels N=2,...,9: every CD magnetic
degree, both typed channel compositions, whole balanced black tensors
against independently constructed ordinary 3j recursions, exact
forbidden source blocks, and the central magnetic identity(16).
Four separately labeled 85-digit growing-level checks calibrate(17).
The covariance, support and growth proofs above establish the general
claims; these checks are supplementary. No source-to-graph scalar bound is inferred from the finite range.