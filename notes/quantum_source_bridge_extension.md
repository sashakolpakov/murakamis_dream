# Uniform comparison of the geometric Gaussian and holonomy density lines

Research note, 27 October 2026. This closes the variable principal
determinant comparison previously checked for 4_1 and 5_2. The argument
uses the actual local mixed-Hessian amplitudes, an explicit endpoint
cut complex, and a telescoping canonical moment-map formula. It works
for an arbitrary knot braid and any regular nondegenerate critical
representation in the stated chart. No bound on bridge number or
crossing word, and no published torsion identity, is assumed.

This is a local principal-density theorem. The base-only quantum
normalization line, square-root phases, integral source lattice and
selected finite period remain the original ones. This does not prove
their global geometric period pairing or the volume conjecture.

## 1. Statement and the exact scope

Use the original balanced phase coordinates q_j=Log A_j,
P_j=Log p_j, with

    Omega=sum_j dq_j wedge dP_j.

Let beta be a b-strand braid with m crossings whose closure is a knot.
Write F for its canonical map, also the actual Hurwitz map after the
already proved prefix/Gauss coordinate transformation. At its chosen
fixed representation suppose the holonomy complex is acyclic:

    0 -> sl_2 --A--> V --D--> V --M--> sl_2 -> 0,
    D=dF-I, M(v)=dP(v)P^(-1), P=H_b...H_1.       (1.1)

All actual crossing shape factors and chart denominators are units.
Thus ker D=im A, and A is injective. Let T_beta be the determinant
ratio det[A,V_c]/det[D V_c,W], with M W=I, as in the existing note.

On the actual inverse-eigenflag framing chart use

    F_M(r,s)=[r 1-r;s -kappa-s],
    kappa=M_mer-M_mer^(-1), Delta=s+kappa*r,
    K_1=-(M_mer+s),
    Omega_cut=-dr wedge ds/[Delta(M_mer+s)].      (1.2)

Here M_mer denotes the meridian eigenvalue; the roman M in (1.1)
is the product differential. The distinction is kept below.

Let Omega_raw be the squared-coordinate-normalized variable Gaussian
two-form from the actual coefficient phase, with denominator
det(-H_perp) and all variable amplitude factors retained. Its
parity-normalized version is Omega_beta^2=(-1)^(b-1)Omega_raw^2,
the convention used in the two prototype audits.

**Principal-density theorem.** Under these explicit regularity
hypotheses, as a rational identity on the entire framing chart,

    Omega_beta^2=-(T_beta/2) Omega_cut^2.         (1.3)

Equivalently the unnormalized variable square is
Omega_raw^2=(-1)^b (T_beta/2)Omega_cut^2. Thus the presentation
parity is explicit; it has not been suppressed as a harmless
numerical factor or assigned to an unknown quantum phase.

The proof below does not identify a square-root phase or evaluate
a base-only compact quantum product at a root. Those data are
separate marked normalization lines, just as in the prototype.

## 2. The actual cut removes precisely one conjugation direction

Let beta_0=sum_j dq_j. Since product Gauss decomposition gives
P_11=product_j K_j and A_j=x/K_j at fixed meridian,

    beta_0=-dP_11/P_11.                          (2.1)

The canonical braid map preserves beta_0. Write P=[a b;c d], a!=0.
In the ordered sl_2 basis (h,e,f), with matrices
h=diag(1,-1), e=E_12, f=E_21, (2.1) becomes

    beta_0=b_0 M, b_0=(-1,-c/a,0).              (2.2)

Let lambda=dLog p_1 be the actual cut momentum covector at p_1=1.
The cut meridian has K_1=-(M_mer+s), e_1=kappa+s and x=-M_mer;
hence lambda(delta G_1)=(delta K_1+delta e_1)/(kappa+s).
For xi=[u v;w -u], delta G_1=[xi,G_1]. Since
G_1(1,1)^t=x^(-1)(1,1)^t, direct multiplication gives

    lambda(A xi)=2u+v-w=:ell(xi).                (2.3)

This row is independent of braid, meridian and framing. Its kernel
is the Lie algebra fixing the selected projective eigenflag 1.

The endpoint cut differential is the square map

    D_cut: V -> ker(beta_0) direct_sum k,
    v |-> (D v,lambda(v)).                      (2.4)

Its kernel is A ker ell, of dimension two. Its cokernel is ker b_0,
via (w,z)->M w. This is exactly the retained framing and co-source;
the three product dependencies have not been discarded.

Indeed D v=f, lambda(v)=c has a solution precisely when M f=0
(with f already in ker beta_0). Choose a right inverse R_D for
D onto ker M, and u in sl_2 with ell(u)=1. A specified solution is

    v=R_D f+A u[c-lambda(R_D f)],                (2.5)

unique modulo A ker ell. A co-source eta evaluates it as

    eta(R_D f)+eta(Au)[c-lambda(R_D f)]

plus its value on the retained two framing directions. Thus the
cut source and the affine dual constant are explicit, even before
any Gaussian or geometric specialization.

## 3. Exact torsion of the endpoint cut complex

Give ker beta_0 its trailing-normal volume: for beta_0(v_0)=1,

    vol_(ker beta_0)(w_1,...,w_(n-1))
                       =vol_V(w_1,...,w_(n-1),v_0), n=2b.

Let K be a 3 by 2 basis of ker ell and ell(u)=1. Let Z be a
3 by 2 basis of ker b_0 and b_0(z_0)=1. Use A K as kernel basis
and Z as cokernel coordinates of (2.4). Then

    T_cut(K,Z)=-det[K,u]/det[Z,z_0] * T_beta.     (3.1)

To prove this, use [A u,V_c] as the complement of A K, and W Z
as a lift of the two-dimensional cokernel. The cut images are
(0,1) and (D V_c,lambda V_c). Subtract multiples of the first
column to remove lambda V_c. Moving (0,1) to the end contributes
(-1)^(n-1)=-1. The remaining target determinant is the volume of
[D V_c,W Z] in ker beta_0. Adjoining W z_0 identifies this with
det[Z,z_0] det[D V_c,W]. The domain determinant is
det[K,u] det[A,V_c], proving (3.1).

For the natural bases

    K=(h+2f,e+f), u=e,
    Z=(e-(c/a)h,f), z_0=-h,

both three-dimensional determinants are -1. Thus T_cut(K,Z)=-T_beta.

This is a determinant identity with a specified kernel and co-source,
not an identification obtained only from equality of critical sets.

## 4. A canonical moment-map identity which telescopes at every strand

Use physical coordinates

    G_j=[K_j e_j;K_j f_j K_j^(-1)+e_j f_j],
    K_j+K_j^(-1)+e_j f_j=x+x^(-1),
    Omega=-sum_j dK_j wedge de_j/(K_j e_j).      (4.1)

The second expression is exactly the actual balanced canonical form.
Let P_j=H_j...H_1=[a_j b_j;c_j d_j], with P_0=I. The prefix
Gauss map gives the elementary recurrences

    a_j=K_j a_(j-1),
    b_j=K_j b_(j-1)+e_j,
    c_j=K_j(c_(j-1)+f_j).                       (4.2)

For simultaneous conjugation xi=[u v;w -u], its induced physical
action on G_j is commutation by the traceless part of

    zeta_j=[u+(v c_(j-1)+w b_(j-1))/(2a_(j-1))  v/a_(j-1);
                         w/a_(j-1)  -u-(v c_(j-1)+w b_(j-1))/(2a_(j-1))].

This follows by differentiating B_-(P)=[1 0;-P_21 P_11] and
G_j=B_-(P_(j-1)) H_j B_-(P_(j-1))^(-1). A scalar trace term
does not affect the commutator.

For local traceless coefficients (U,V,W), contraction of (4.1) is

    iota_[zeta,G] Omega_j
          =2U dK/K+V(df+f dK/K)+W de/K.         (4.3)

Here df=(K^(-2)-1)dK/e-f de/e follows from the fixed trace.
After inserting zeta_j, its coefficient of v is
dc_j/a_j-dc_(j-1)/a_(j-1); its coefficient of w is
db_j/a_j-db_(j-1)/a_(j-1). Its coefficient of u is 2dLog K_j.
The sums telescope, giving the uniform identity

    iota_(A xi) Omega=(2u da+v dc+w db)/a.       (4.4)

In right-trivialized product coordinates M=(delta P)P^(-1),
equation (4.4) is

    A^t Omega=R(P) M,
    R(P)=[2 2c/a 0;-c/a 0 1;b/a d/a 0],
    det R(P)=-2/a^2.                            (4.5)

In particular it is independent of crossing number and presentation.
The factor two is fixed by the h=diag(1,-1) convention; it is not
an adjustable normalization of torsion.

For the bases K,Z in Section 3,

    K^t R Z=[2/a^2 0;(c/a)^2+1/a^2 1],
    det(K^t R Z)=2/a^2.                         (4.6)

The canonical self-dual cokernel associated to a tangent v in
ker D_cut is (w,z)->Omega(v,w). It is well-defined and annihilates
the cut image because F is symplectic and Fv=v. It is injective:
Omega(v,ker beta_0)=0 would force v proportional to the Hamiltonian
vector of beta_0, which is -A h/2 and has nonzero lambda value.
Thus (4.6) gives the exact conversion from the product co-source
to this canonical Gaussian co-source.

## 5. Canonical generating families give the same determinant line

This section proves the Gaussian-to-endpoint comparison, retaining
the source/cokernel pairing. It applies to the actual phase but is
pure linear algebra of its quadratic part.

At crossing t, write its generating function S_t(a,u,tau), where
a is the first input position, u the first output position, and
tau is the conserved sum of the two positions. The actual transfer
coordinate is c_t with u=b+sign(t)c_t. Its mixed Hessian is
V_t=(S_t)_(au), the exact unit computed from the actual coefficients.
The graph equations are

    P_1=P_2-(S_t)_a,
    P'_2=P_2+(S_t)_tau,
    P'_1=P'_2+(S_t)_u.                          (5.1)

They imply dS_t=P'_1 dq'_1+P'_2 dq'_2-P_1 dq_1-P_2 dq_2.

For the whole word, let q be the b initial positions and c the m
transfers. The final positions are

    q_out=P_perm q+R c,

where P_perm is the braid permutation matrix and R is integral.
Let S(q,c) be the sum of the local generating phases. If p denotes
final momentum, the generating family gives

    p_in=P_perm^t p-S_q,
    r_int=S_c-R^t p=0.                          (5.2)

At fixed q the Jacobian in (c,p) is

    J_in=[-S_qc P_perm^t;S_cc -R^t].            (5.3)

It is invertible and

    det J_in=(-1)^(m(b-1)) product_t V_t.       (5.4)

For a direct induction append one crossing. Changing its variables
(c_new,p_out) into (p_old,r_new) leaves the old equations unchanged.
On its two active strands, at fixed input positions, the active
3 by 3 Jacobian has rows

    [-sign*(V+S_tau,u) 0 1],
    [-sign*(S_uu+S_tau,u) 1 0],
    [S_uu -sign sign].

Its determinant is -V. The b-2 unchanged momenta give the full
determinant (-1)^(b-1)V. Starting from the empty word proves (5.4).

Close positions 2,...,b. The closure matrix C on (q,c) has rank b-1.
Its cofactor on q_2,...,q_b is P_perm-I with one row/column removed,
of determinant +/-1 because the knot permutation is one cycle.
This supplies the actual integral free coordinates z=(q_1,c),
of dimension d=m+1. Denote the restricted phase Hessian by H.

Let L_cut be the coordinate matrix of (2.4), with rows

    (q_out-q)_2,...,(q_out-q)_b,
    (p_out-p_in)_1,...,(p_out-p_in)_b,
    (p_in)_1.                                  (5.5)

The endpoint target is expressed in these coordinates. Its trailing-
normal volume is the negative of their coordinate volume: the basis
(e_qj-e_q1 for j>1, all e_pj) followed by e_q1 has determinant -1.

For regular H, exact Jacobian elimination gives

    det L_cut=(-1)^(m+b-1) det H/product V_t
             =det H/product V_t.               (5.6)

Here is the sign calculation. On (q,c,p), use output equations
(position closure, p_out-p_in, (p_in)_1, r_int). Their determinant
is det L_cut det J_in, by the change to (q,p_in,r_int).
Adding its first momentum-difference row to the cut row replaces
(p_in)_1 by p_1. Reordering to (S_q-C_q^t rho,S_c-C_c^t rho,
closure,p_1) has sign (-1)^(mb), where rho=(p_2,...,p_b).
Eliminating p_1 has sign (-1)^(b-1). The remaining bordered matrix
is [S'' -C^t;C 0]. The integral cofactor changes it, with determinant
one squared, to H plus b-1 blocks [0 -1;1 0], each determinant one.
This proves the first equality of (5.6). Knot parity m=b-1 mod 2
gives the second equality.

### The rank-two kernel and its co-source are also matched

For a symmetric H with kernel basis B (the actual derivatives in
r,s), define its torsion using cokernel rows B^t. It is

    T_H=det(B_chi)^2/det H_perp,                 (5.7)

where chi is any two coordinates with invertible B_chi. This follows
by adjoining the other coordinate columns as a complement and
using a right inverse of B^t. It is independent of chi.

The kernel map to the endpoint is explicit. Put w=(q,c)=E z for
the integral closed-flow embedding. For B in ker H solve uniquely

    C^t rho=S'' E B,

and send B to v=(q, p), with p_1=0 and p_j=rho_j for j>1.
The q part is the initial-position part of E B. These equations
give p_in=p_out, and yield exactly the kernel of L_cut. Thus the
kernel uses the same r,s framing, not a rescaled substitute.

To verify the cokernel, perturb the generating phase by epsilon f,
where f is any quadratic form in the free closed-flow coordinates,
extended as a quadratic form in (q,c). The position map and closure
matrix stay unchanged, so total-position conservation and beta_0
are preserved. Differentiating the generating identity in (5.1)
gives on two cut-fixed kernel tangents u,v

    Omega(u,(partial_epsilon F)v)
                        =Hess(f)(B_u,B_v).       (5.8)

An explicit equation check fixes the sign without a boundary-form
convention. At fixed input tangent v, write the internal and final-
momentum variations as (tau,pi). Differentiating (5.2) gives

    P_perm^t pi-S_qc tau=f_q(B_v),
    S_cc tau-R^t pi=-f_c(B_v).

Pair the first equation with q_u and subtract the second paired
with c_u. Position closure gives P_perm q_u+R c_u=q_u, while
the tangent internal equation gives
q_u^t S_qc+c_u^t S_cc=p_u^t R. The resulting left side is
q_u^t pi-p_u^t R tau=Omega(u,(partial_epsilon F)v); the right
side is B_u^t Hess(f) B_v. This proves (5.8) with its positive
sign and its specified kernel/co-source identification.

Choose f nondegenerate on the two-dimensional kernel. In the leading
epsilon^2 determinant coefficient, (5.8) is precisely the pairing
used for both Hessian cokernel B^t and endpoint cokernel Omega(u,-).
The unit J_in(epsilon) contributes only its constant determinant.
The negative endpoint target volume in (5.5) and (5.6) therefore give

    (product_t V_t) T_H=-T_cut^Omega(r,s).       (5.9)

No limiting convergence is involved: this is extraction of the leading
coefficient of a finite determinant polynomial (or a regular rational
matrix germ). It also verifies the kernel/cokernel map, which cannot
be inferred merely from det H=det L_cut=0 on a Morse--Bott locus.

## 6. The universal factor is -1/2

For the actual framing F_M(r,s), its infinitesimal conjugation columns
are the traceless parts of -F_M^(-1)partial_r F_M and
-F_M^(-1)partial_s F_M. In the fixed basis K=(h+2f,e+f) their 2 by 2
coefficient matrix has determinant

    det C_frame=-1/(2Delta).                    (6.1)

This is direct multiplication of the displayed F_M. The framing
changes both the kernel and its canonical self-dual cokernel, so it
contributes det(C_frame)^2. Combining (3.1), (4.6) and (6.1) gives

    T_cut^Omega(r,s)
       =-T_beta * (2/a^2)/(4Delta^2)
       =-T_beta/(2a^2 Delta^2).                 (6.2)

The original actual amplitude identity already proved in the
[principal-density note](actual_cut_residue_and_principal_density.md) is

    a_beta^2=(product_(j=2)^b K_j^2) product_t V_t,
    product_(j=2)^b K_j^2=a^2/K_1^2.           (6.3)

Its Gaussian denominator is det(-H_perp), so

    Omega_raw^2=(-1)^(m-1) a_beta^2 T_H.

Insert (5.9), then normalize by (-1)^(b-1). Because m+b-1 is even,

    Omega_beta^2=(a^2/K_1^2) T_cut^Omega(r,s)
       =-T_beta/(2Delta^2 K_1^2) (dr wedge ds)^2
       =-(T_beta/2) Omega_cut^2.

This proves (1.3) uniformly. Every scalar comes from an explicit
Jacobian, source constraint or original pivotal factor. The argument
does not set a peripheral factor to its value before forming these
maps, and does not choose a square-root sign from an identity of squares.

## 7. Remaining quantum assertion

The local geometric principal coefficient is now the same holonomy
torsion/cut density for every regular knot braid, beyond the two
prototype fields. The selected finite quantum period still has to be
pushed to this normal block with its actual lattice, period mark and
base-only normalization. A principal-density identity does not prove
that the selected global cycle has a nonzero component there, or give
its archimedean norm across levels. Those remain the volume theorem.

[Exact audit](../experiments/audit_uniform_cut_density_comparison.py).
[Results](../experiments/uniform_cut_density_comparison_results.json).
