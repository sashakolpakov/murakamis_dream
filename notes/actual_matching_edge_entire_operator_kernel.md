# An entire finite source for the completed exceptional operator

30 October 2026. The source-matching operator kernel has a complete
cancellation of its apparent ordinary-column poles. Its exact finite
continuation is a product of TWO original q-Hahn determinant polynomials
and a residual sine product. Every monomial phase cancels. It matches
the actual completed matrix on the entire physical grid, including
the entries outside its bandwidth, which are identically zero.

This is a root-value source identity. It supplies the exact function
in the needed second chart, but does not yet supply its asymptotic
there or a continuation of genuine generic-q normals. In particular
the zeros on the forbidden physical grid must remain in any such
analysis.

## 1. Exact finite normalization and cancellation

Put N>=3, d=N-1, q=exp(pi i/N), theta=pi/N and
0<=a<=floor(d/2). Let J_t be the original low physical Casimir block
in total degree t, and let p_a be its original exceptional polynomial.
The [source-exact kernel](actual_matching_edge_antidiagonal_operator_packet.md)
uses output row u<=v=input row, h=v-u and l=t-v. Write

    sigma=d-h, c=-cos((sigma+1)theta)=cos(h theta),
    z_1=q^(-sigma+2u), z_2=q^(sigma-2l),
    beta_a=s_(2a)/s_a^2,
    s_n=product_(r=1)^n 2sin(r theta).

The variables h,u,l may now be arbitrary complex numbers; the
channel a and level N remain integers. The polynomial R_a(z;c) is
the SAME monic original determinant as in
[the joint source theorem](actual_q_hahn_joint_accretive_determinant.md):

    R_0=1, R_1=z+c/cos(theta),
    R_(n+1)=[z+c/(cos(n theta)cos((n+1)theta))]R_n
          +B_n[cos^2(n theta)-c^2]R_(n-1),
    B_n=sin^2(n theta)/[cos^2(n theta)
                   sin((2n-1)theta)sin((2n+1)theta)].           (1)

All denominators used in (1), through degree a, are nonzero.

Define

    K_ent(h,u,l)=beta_a^2/N
        *product_(r=a+1)^(d-a) 2sin((h+r)theta)
        *R_a(z_1;c) R_a(z_2;c).                              (2)

An empty product is one. Formula (2) is an ENTIRE finite function
of h,u,l: it is a finite Laurent polynomial in their elementary
exponentials. It is not a quotient requiring a prescription at an
ordinary-channel pole.

Here is the full phase check. Set

    S_a(h)=product_(r=1)^a 2sin((h+r)theta).

The actual normalized ordinary continuation from the joint source
theorem is

    fhat_a(sigma,u)=beta_a q^[d u+(a^2-da)/2]
                            R_a(q^(sigma-2u);c)/S_a(h).        (3)

This follows from that theorem's formula (5), using
sin((sigma-r)theta)=sin((h+r+1)theta). The holomorphic conjugate
on this chart is therefore

    fhat_a^#(sigma,u)=beta_a q^[-d u-(a^2-da)/2]
                            R_a(q^(-sigma+2u);c)/S_a(h),       (4)

because the coefficients of R_a(z;c) are real polynomials in c
and c itself is real under holomorphic conjugation. This is NOT
pointwise conjugation at complex h,u.

The prior exact kernel is

    q^[-d(l-u)] P_(N,a)(h)
                    fhat_a^#(sigma,u) fhat_a(sigma,l),
    P_(N,a)(h)=N^-1 product_(r=1)^(d-a) 2sin((h+r)theta)
                          *product_(r=1)^a 2sin((h+r)theta).

The three q monomials in (3),(4) and the preceding line cancel
EXACTLY, including the constants (a^2-da)/2. Moreover

    P_(N,a)(h)/S_a(h)^2
          =N^-1 product_(r=a+1)^(d-a) 2sin((h+r)theta),         (5)

since a<=d-a. This proves (2) as an identity of finite meromorphic
functions, hence provides its removable continuation everywhere.
No branch of a logarithm, square root or noninteger channel enters
the cancellation.

## 2. It matches the ENTIRE original physical grid

For every original 0<=u<=v<=t<=d, let h=v-u and l=t-v. Then

    [p_a(J_t)]_(u,v)=K_ent(h,u,l).                            (6)

For h<=a, this is the already proved original kernel identity and
the exact cancellation above. For h>a the original left side is
zero at GENERIC q, since a degree-a polynomial of a tridiagonal
matrix has bandwidth a. We now prove that the right side is zero
at these actual grid points too, without assuming that (3) is a
physical column when sigma<a.

There are two different forbidden ranges.

If a<h<=d-a, the residual product in (2) contains
r=N-h=sigma+1. Indeed a+1<=r<=d-a, and its sine is sin(pi)=0.
Thus (2) vanishes irrespective of the two determinant values.

If d-a<h<=d, then 0<=sigma=d-h<a. In this case the actual physical
rows satisfy 0<=u,l<=sigma. The original finite Newton numerator
of the ordinary column vanishes at EVERY node U=Q^r,
0<=r<=sigma, where Q=q^2. To see this directly, its kth summand
contains

    product_(j<k)(U-Q^j)
       *product_(j<a-k)(Q^sigma/U-Q^j).

Either k>r or a-k>sigma-r, because a>sigma. The corresponding
product is zero. The other coefficients are regular: 2a<N and
the root leading coefficient [2a choose a]_Q is nonzero.
The exact original numerator-to-determinant relation therefore gives

    R_a(q^(sigma-2r);-cos((sigma+1)theta))=0,
                                      0<=r<=sigma<a.          (7)

For z_1 use r=sigma-u, and for z_2 use r=l. Thus BOTH determinants
in (2) vanish. This proves (6) also in the second forbidden range.
It does not mistakenly apply the second argument to the first range,
where sigma can still be at least a.

Equivalently, (7) gives the exact polynomial divisibility

    product_(r=0)^sigma (z-q^(sigma-2r))
        divides R_a(z;-cos((sigma+1)theta)), sigma<a.           (8)

At a=sigma+1, the two monic polynomials are equal. In recurrence
(1), the coefficient of R_sigma at the next step contains
cos^2((sigma+1)theta)-c^2=0, so the factor persists inductively
at every subsequent degree. This gives a second direct check of
the finite-source zero mechanism.

Root transpose symmetry supplies the entries u>v, using (6) with
the two row labels exchanged. The actual generic translated adapter
supplies the physical totals above d. Thus (6) is a full root-grid
statement, not only an anti-diagonal or low-total diagnostic.

## 3. The needed second chart and what remains unproved

At the odd maximal fold a=d/2, the residual product in (2) is EMPTY.
At the even maximal fold a=(d-1)/2, it has ONE sine factor. The
apparently singular transition to 0<Re(sigma/N)<1/2 is therefore
entirely an analysis of the two actual determinant polynomials,
with that scalar retained. The finite support zeros in (7) do not
disappear when the denominators in (3) are canceled.

There is also an exact elementary chart relation

    R_a(z;-c)=(-1)^a R_a(-z;c),                              (9)

proved by induction in (1). It may help analyze the complementary
degree range, but does not turn it into the already controlled
ordinary physical tube: its reflected magnetic coordinates can
lie outside that tube. In particular (2),(8),(9) alone do not give
an N-independent zero-free region, a selected action, or a nonzero
relative amplitude in the second chart.

There is an elementary obstruction to one possible stronger claim.
Fix a real limiting channel alpha<=1/2 and a real point in

    delta>alpha, nu>0, lambda>0, nu+lambda+delta<1.

Every neighborhood of that point contains, at all sufficiently large
levels, genuine physical grid points h,u,l with h>a and
t=u+h+l<=d. Equation (6) says K_ent is EXACTLY ZERO there.
Therefore it cannot have a uniform relative formula
A exp(N H)(1+O(N^-1)) with A nowhere zero on an N-independent
complex neighborhood of that real point. This remains true for a
nonzero analytic limiting amplitude on an open real subchamber:
choose a point where its value is nonzero, then nearby grid points.
The statement does not exclude a chart centered at a genuinely
nonreal geometric point or an expansion retaining several branches
and their support cancellations.

There is a related exact period limitation. Fix any physical integer
h>a. Every original matrix entry on that h-slice is zero, so its
contraction with ANY surrounding physical tensor is zero as well.
This remains true before root specialization and for every retained
generic derivative. An exact contour rewriting followed only by a
deformation of magnetic variables at this fixed h must preserve that
zero. Consequently a nonzero off-grid packet on this slice does not
give a nonzero slice period: another contribution must cancel it,
or its selected contour coefficient must vanish. A joint degree
transport or a different exact grouping still needs its own proof.

The actual generic-q source remains the UNSPECIALIZED tensor
D_a/(rho_a beta_N) B^-1 R^-1(W_a p_(2a) W_a^T) in the kernel
theorem. The simplifications (3)--(5) use the root identity
q^N=-1. They cannot be differentiated to manufacture its genuine
normal. This note does not assert that replacing q in (2) by
q exp(epsilon) is that source. A continuation of the original
generic tensor or its retained normals must still be proved.

The exact result here is the entire finite ROOT source (2), its
agreement with every original physical entry, and its explicit
support-zero factorization. Neither a global contributing cycle
nor a general long-twist volume theorem follows from it alone.

Focused audit: [phase-canceled source and every physical support
range](../experiments/audit_actual_matching_edge_entire_operator_kernel.py).

The entire operator kernel does not imply a generic-q lift or a second-chart asymptotic.