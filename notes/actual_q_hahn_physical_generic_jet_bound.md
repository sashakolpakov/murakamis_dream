# Every fixed generic jet of an actual physical q-Hahn column

30 October 2026. This note extends the
physical prefix estimate to the original generic deformation. Every
fixed generic-q derivative of every admissible physical column has
polynomial cost relative to its nonzero root value, including large
channels. The actual divided pair also has polynomial fixed generic
jets. The upper half of the column is treated by its backward generic
recurrence, not by differentiating a root-only reflection identity.

The statement is on integer physical degrees and magnetic indices.
It supplies no fixed complex magnetic neighborhood, no nonzero
confluent amplitude, and no completed four-port or network norm.

## 1. The actual generic column and its endpoints

Fix N>=3, d=N-1, q0=exp(pi i/N), and integers

    0<=m<=t<=d, 0<=u<=t.

Write q=q0 exp(epsilon), Q=q^2, x=q^d, v=t-u, and F_r=(Q;Q)_r.
The original finite source is

    C_m(q;t,u)=sum_(a=max(0,m-v))^(min(m,u))
       (-1)^a x^(u-2a) Q^[av+a(a-1)/2]
       F_(N-m+a-1)F_(N-a-1)/(F_(N-m-1)F_(N-1))
       [u choose a]_Q [v choose m-a]_Q/[t choose m]_Q. (1)

These are precisely the genuine generic highest-vector ratios of
the [mixed compiler](actual_mixed_augmented_plat_compiler.md), not
the squared-binomial formula obtained after root specialization.
All factorial indices in (1) are below N. The function is regular
near q0. Its endpoints are exact monomials:

    C_m(q;t,0)=1,
    C_m(q;t,t)=(-1)^m q^[dt-2Nm+m^2+m].              (2)

For the second equality only a=m survives; the original ratio of
F-factorials is then one. These formulas hold before differentiating.

There are universal c,C>0 such that, simultaneously for all the
integer indices above,

    C_m(q0;t,u)!=0,
    |C_m(q0 exp(epsilon);t,u)/C_m(q0;t,u)|<=C
                            for |epsilon|<=cN^(-8). (3)

The functions in (3) are holomorphic on that disk. In particular,
for every fixed r>=0,

    |D^r C_m(q0;t,u)|<=C_r N^(8r)|C_m(q0;t,u)|,
    D=q d/dq.                                       (4)

There is no small-channel restriction on m in (3),(4).

## 2. The original generic physical Casimir block

The degree-t balanced tensor basis has entries indexed by u=0,...,t.
Let J_t(q) have diagonal D_u, upper entries A_u^+ and lower entries
A_u^- (the superscripts refer to the matrix positions). A direct
application of the original generic coproduct gives

    D_u=q^-1 Q^(u-t)(1-Q^(N-u))(1-Q^u)
        +q^(-2d-1)Q^u(1-Q^(N-t+u))(1-Q^(t-u))
        +q^(2d+1)Q^-t+q^(-2d-1)Q^t,

    (J_t)_(u,u+1)=A_u^+
       =q^-N Q^(2u+1-t)(1-Q^(N-u-1))(1-Q^(t-u)),
    (J_t)_(u+1,u)=A_u^-
       =q^-N(1-Q^(N-t+u))(1-Q^(u+1)), 0<=u<t.       (5)

For example the lower offdiagonal is the contribution of F on the
first head after E on the second; the upper offdiagonal retains both
Cartan factors of the opposite path. Their generic values differ.
Replacing them by their equal root values before differentiating
would change the source.

The vector (1) satisfies

    J_t(q) C_m(q;t,.)=lambda_m(q) C_m(q;t,.),
    lambda_m=q^(2N-2m-1)+q^(-2N+2m+1).              (6)

This follows from its highest degree m, highest weight 2d-2m, and
the original coproduct Casimir. Alternatively, substitution of the
finite highest-vector and its divided descendants yields (5),(6)
entry by entry. Thus the normalization C_m(0)=1 in the magnetic
index fixes the SAME source vector, not an auxiliary eigenvector.

At q0 the two offdiagonals in (5) coincide, and (5) simplifies to

    D_u=U/T [2(q0^-1+q0 T)-(q0+q0^-1)U],
    A_u=(U-T)(1-Q0 U)/T,
    U=Q0^u, T=Q0^t, Q0=q0^2.                        (7)

For the reversal matrix P_t, (7) also gives

    P_t J_t(q0) P_t=conjugate(J_t(q0)).              (8)

Only this ROOT identity is needed below. No generic version of
(8), or a flat high-degree adapter, is assumed.

## 3. A polynomial generic neighborhood from prefix coercivity

The [physical prefix theorem](actual_q_hahn_physical_partner_normal_bound.md)
proves, for every 1<=h<=floor(t/2),

    Im J_[h](q0) >= 4 sin^3(pi/N)/h^2 * I.           (9)

Although that note applies the estimate to complete double channels,
its weighted-row identity and positive Dirichlet proof use only
1<=t<=d and h<=floor(t/2). In this entire range the weights
1/sin((t-r)pi/N) are positive, its row residual is

    4 sin(r pi/N) sin^2(pi/N) sin(t pi/N)
                              /sin((t-r-1)pi/N)>=0,

and every retained conductance is at least 4sin(pi/N). The same
Poincare step therefore proves (9) for all t used here. It requires
no sign assumption on -cos((t+1)pi/N) and no channel condition t>=l.

The bound is independent of the real spectral parameter. Since
lambda_m(q0) is real, it implies

    ||(lambda_m(q0)I-J_[h](q0))^-1||<=C N^5.        (10)

The reversed prefix has the conjugate root matrix by (8), hence
has the same inverse bound. This holds for every m<=t, not merely
for the two members of a double node.

Every elementary exponent in (5),(6) is O(N). On a fixed disk
|epsilon|<=c/N the entries and eigenvalues are O(1) and their
epsilon derivatives are O(N), uniformly over all indices. The
bandwidth is fixed. For either the forward or reversed prefix,

    ||M(epsilon)-M(0)||<=C N|epsilon|,
    M(epsilon)=lambda_m(q)I-J_prefix(q).             (11)

Combining (10),(11), on rho_N=cN^(-8) the relative perturbation
has norm at most Cc/N^2. Decrease c so that it is below 1/2.
For prefix size h<=N,

    |det M(epsilon)/det M(0)|
       <=(1+Cc/N^2)^h<=C,                           (12)

and the determinant is nonzero throughout the disk.

The offdiagonal products introduce only polynomial local costs.
At the root

    |A_u^+|=|A_u^-|
       =4 sin((t-u)pi/N) sin((u+1)pi/N)
       >=4 sin^2(pi/N)>=16/N^2.                    (13)

Equation (5) gives derivative O(N), so these entries remain nonzero
on the same disk. Their relative logarithmic changes are bounded
by C N^3|epsilon|. A product of at most N such entries therefore
has a uniformly bounded ratio to its root value, and so does its
inverse. In fact its logarithmic change is O(N^4|epsilon|).

For u<=floor(t/2), the exact forward recurrence gives

    C_m(q;t,u)=det(lambda_m(q)I-J_[u](q)) /
                                    product_(r=0)^(u-1) A_r^+(q). (14)

The empty determinant and product at u=0 are one. Equations
(10)--(14) prove root nonvanishing and (3) on this half.

For u>=ceil(t/2), put h=t-u and reverse the ACTUAL generic recurrence.
Normalize its endpoint by the exact nonzero C_m(q;t,t) in (2).
The normalized reversed column has initial entry one and is again
a leading-prefix determinant divided by its own upper offdiagonal
product. Its prefix has size h<=floor(t/2). Equations (8)--(13)
apply to this reversed generic matrix because its ROOT is conjugate
to the forward one and its generic entries satisfy the SAME bounds.
The endpoint exponent in (2) is O(N^2), so its ratio on the small
disk is also uniformly bounded. This proves (3) on the upper half,
including t=0,1 by the endpoint formulas alone.

Cauchy's formula now gives (4) for the genuine generic source.
The derivative holds N,t,u fixed, as the original compiler does.

## 4. The completed divided pair also has fixed generic jets

Suppose j<l, j+l=d and l<=t. Put s=l-j and define the original
generic divided pair

    W_(j,l)(q;t,u)=
          (C_j(q;t,u)-C_l(q;t,u))/(lambda_j(q)-lambda_l(q)). (15)

The [exact collision identity](actual_q_hahn_partner_normal_collision.md)
gives C_j(q0;t,u)=C_l(q0;t,u), and its actual gap is

    lambda_j-lambda_l=(q^s-q^-s)(q^N-q^-N).           (16)

The second factor has a simple zero at q0; the first does not.
Thus (15) has a removable singularity, with root value exactly
the retained physical paired normal

    W_(j,l)(q0;t,u)
       =[D C_j-D C_l]/[-2N Delta_j],
    Delta_j=q0^(2j+1)-q0^(-2j-1)=q0^s-q0^-s.         (17)

On |epsilon|=rho_N, the first factor in (16) has modulus at least
c/N and the second at least cN rho_N. There are no other zeros
inside this disk. The two bounds (3), using their equal root values,
therefore give

    |W_(j,l)(q;t,u)|<=C rho_N^-1 |C_j(q0;t,u)|
                                  on |epsilon|=rho_N.

Cauchy's formula applied AFTER the removable singularity is filled
proves, for every fixed r>=0,

    |D^r W_(j,l)(q0;t,u)|
                   <=C_r N^[8(r+1)] |C_j(q0;t,u)|.  (18)

For r=0 the earlier N^6 physical paired-normal estimate is sharper.
The additional content here is the higher genuine generic-q jets,
including the variation of the matrix, both original columns, and
the gap. Equation (18) is not obtained by treating a q derivative
as a spectral derivative. For example D W at the root contains
second q derivatives of the original columns, as it must.

## 5. Interface and limits

The [matching-edge rewrite](actual_matching_edge_marked_four_port_block.md)
needs Taylor order two after clearing its simple poles. Equations
(4),(18) remove a possible physical-column obstruction to controlling
such jets. To apply them to a completed target pair one must STILL
prove its exact expression in these normalized columns, their
divided pair, and its actual scalar measures. The native boundary
cost of that four-port tensor has not been replaced by a polynomial
in this note. Nor is a surrounding contraction estimated here.

The estimates concern integer t,u. They do not prove a fixed
complex magnetic corridor or control the extra poles of the large
partner's unrestricted continuation. The separate shrinking-channel
complex theorem and the present physical generic theorem address
different domains. No lower bound for W or a nonzero selected global
contribution follows from either upper estimate.

Audit: [original generic physical matrix and retained divided-pair jets](../experiments/audit_actual_q_hahn_physical_generic_jet_bound.py).
The focused exact audit passed 1,204 original physical column four-jets,
1,204 generic eigenvector equations, 2,408 forward/backward comparisons,
432 generic endpoint jets, and 378 divided-pair jets through order two.
It retains 4,816 column and 1,134 pair coefficients; 323 tested second
pair jets are nonzero. Those checks verify source and normal conventions,
while the prefix perturbation proof supplies the uniform bounds.

The theorem retains the integer physical domain. It gives neither a completed four-port norm nor a fixed complex magnetic neighborhood.