# The affine origin is an auxiliary source flag

Research note, 26 October 2026. The selected vacuum in the existing
cyclic endpoint module depends on an affine origin. Keeping that origin
as an extra point s in P^1 gives an intrinsic parameterization of the
same modules. It gives exact unit-preserving projective transport when
s moves with the geometric flags, and an explicit flat adapter when s
changes. For two finite source flags the adapter can be normalized by
the actual edge caps so that pointed fusion, face pairings and cyclic
maps all commute exactly.

The normal chart is also explicit: its extra source point is
sigma=(s-p_*)/epsilon. The first normal coefficient of an adapter is
usually a non-scalar matrix. This realizes a concrete affine change of
normal lifts, with a corresponding change of the selected cut row.

These are statements about the already defined quantum modules and
their selected data, not a replacement invariant or a proof of the
volume conjecture. The global ADO/geometric source identification and
the marked regulator norm remain unproved.

## 1. The source flag and the existing triangle module

Use N>=2, q=exp(pi*i/N), Q=q^2 and the shared difference roots
B_ij from [the shared-face proof](shared_standard_face_gluing.md).
For distinct flags p_i and a finite s avoiding them, choose

    A_i(s)^N=p_i-s.

Only ratios of the A_i occur in the relative triangle module, so
a common rescaling of all A_i has no effect. On f=(i,j,k), use

    D_f^N=lambda_f=(p_i-p_k)/(p_j-p_k),
    Y_f=(v_f-u_f D_f)sigma_Q^(-1),
    u_f=A_j(s)/A_k(s), v_f=A_i(s)/A_k(s).             (1.1)

Here sigma_Q(D)=QD; it is unrelated to the normal source coordinate
introduced in Section 6. Direct subtraction gives Y_f^N=1-lambda_f.
Thus the full relative matrix algebra is independent of s. Its
pointed unit line for Y_f+u_f D_f-v_f varies with s.

The normalized Steinberg parameter is now the four-point function

    t_f(s)=(p_j-s)(p_i-p_k)/((p_i-s)(p_j-p_k)),
    1-t_f(s)=(p_k-s)(p_j-p_i)/((p_i-s)(p_j-p_k)).
                                                        (1.2)

In particular it is invariant under simultaneous projective change
of p_i,p_j,p_k,s. The values s=p_i,p_j,p_k correspond to
t=infinity,0,1. The Nth-root cover for its normalized parameters is
the existing punctured Fermat curve rho^N+a^N=1. No new quantum
function has been defined.

At s=infinity take the endpoint ratios A_i/A_j=1. Then (1.1)
is the usual Steinberg triangle module and t_f=lambda_f. This
chart concerns the relative triangle modules. The original edge
modules and their caps can degenerate there; their retained lattice
and source terms cannot be obtained by substituting these ratios
into a separately singular edge formula.

Define, as before,

    beta_f=B_ik/B_jk, nu_f=B_ji/B_jk,
    rho_f(s)=(A_j(s)/A_i(s)) beta_f,
    a_f(s)=(A_k(s)/A_i(s)) nu_f,
    phi_(f,s)(n)=(Q rho_f(s);Q)_n/a_f(s)^n,
    G_(f,s)=diag(phi_(f,s)^(-1)) H(beta_f).           (1.3)

It follows that G D G^(-1)=beta_f Z and
G Y G^(-1)=nu_f S. The matrices H, clock Z and shift S are
exactly those of the preceding note.

## 2. Moving the source restores pointed projective covariance

Let F(p)=(a p+b)/(c p+d), Delta=ad-bc. Choose compatible roots

    E^N=Delta, D_i^N=c p_i+d, D_s^N=c s+d,
    B_ij'=E B_ij/(D_i D_j),
    A_i'=E A_i/(D_i D_s).                            (2.1)

When F(s)=infinity the ratios in the last formula are read as
A_i'/A_j'=(A_i/A_j)(D_j/D_i); its common factor is unnecessary.
The same ratio interpretation covers other source charts.

Substitution gives the exact identities

    beta_f'=(D_j/D_i)beta_f,
    nu_f'=(D_k/D_i)nu_f,
    rho_f'(F(s))=rho_f(s), a_f'(F(s))=a_f(s).         (2.2)

Set kappa_f=D_j/D_i, eta_f=D_k/D_i and, in the raw
polynomial bases, K_f=diag(kappa_f^(-n)). Then

    K_f 1=1, G_(Ff,F(s)) K_f=G_(f,s),
    D_f' K_f=K_f kappa_f D_f,
    Y_f' K_f=K_f eta_f Y_f.                          (2.3)

For a tetrahedron with faces A=ikl,B=ijk,C=ijl,D=jkl,
these rescalings commute with both total and relative algebra
embeddings. For example kappa_A=kappa_C kappa_D and
eta_A=kappa_C eta_D=eta_C. Consequently

    R_(F p,F(s))(K_A tensor K_B)
                  =(K_C tensor K_D)R_(p,s).         (2.4)

A proof including the scalar is immediate from the pointed
uniqueness theorem: both sides intertwine the same full matrix
algebra and send the unit tensor to the unit tensor. Therefore
the scalar is one. No determinant root or inverse of two modulo
N is needed. This does not assert that arbitrary vertex
permutations give equal bare tensors.

Holding the origin fixed while applying F changes the source
flag data. The nonconstant Hilbert-90 factor in the earlier
[projective-frame construction](projective_frame_period_torsor.md)
records exactly that distinction.

## 3. Changing the source: an explicit flat connection

For fixed geometric flags define the source-change adapter

    H_f(s',s)=G_(f,s')^(-1)G_(f,s)
       =H(beta_f)^(-1)
          diag(phi_(f,s')/phi_(f,s)) H(beta_f).        (3.1)

It intertwines both raw generators, has value one at the marked
spectral root beta_f and satisfies the strict composition law

    H_f(s'',s')H_f(s',s)=H_f(s'',s).                 (3.2)

This is the explicit normalized Hilbert-90 map already present
in [the affine transport proof](affine_frame_period_transport.md),
now written on the intrinsic source-flag cover. The adapter is
usually not unit-preserving. Indeed a scalar image of 1 would
make H_f a scalar, since 1 is cyclic for D_f. Intertwining Y
would then force both endpoint ratios in (1.1) to coincide;
distinct source flags and distinct p_i rule that out.

Equivalently (3.1) is parallel transport for the algebraic flat
connection, with p_i fixed,

    nabla_f=d+G_(f,s)^(-1)dG_(f,s)
       =d-H(beta_f)^(-1)diag(d log phi_(f,s))H(beta_f).
                                                        (3.3)

This is a logarithmic connection on its root cover. It describes
the finite-level source frame, not the dilogarithmic regulator
connection or a norm comparison across levels.

## 4. The full source scalar is a cocycle with an explicit cone

Write K_t(s) for the retained scalar kappa_t(s)phi_(B,s)(e_t)
in equation (4.2) of the shared-face proof. The standard shape
u_t,v_t and the clock/shift insertion depend on B_ij and edge
orientations, and are independent of s. Therefore exactly

    R_(s')(H_A tensor H_B)
       =c_t(s',s)(H_C tensor H_D)R_s,
    c_t(s',s)=K_t(s')/K_t(s).                         (4.1)

All factors are the actual nonzero finite sums/products of the
pointed fusion; no source value has been independently normalized.

Compare the ordered pentagon at s and s'. The standard kernel
operators in its two presentations are identical, so its scalar
part gives delta c=1 on every nondegenerate five-flag chart.
Thus c is a configuration three-cocycle. This proof uses the
previously proved algebraic pointed pentagon, not a published
state-sum invariance theorem.

Choose a further flag o distinct from those in use, with all
root data on the same cover, and put

    b_f(s',s;o)=c_(o,i,j,k)(s',s), f=(i,j,k).
    delta b_(i,j,k,l)=b_(j,k,l)b_(i,j,l)
                         /(b_(i,k,l)b_(i,j,k)).       (4.2)

Expanding delta c(o,i,j,k,l)=1 gives delta b=c. Hence
Hhat_f=b_f H_f obeys the tetrahedron comparison with scalar
one. Its source composition is strict because b itself is a
ratio of K values.

The anchor dependence is also explicit. For another anchor o',

    b_f(o')/b_f(o)=a_(i,k)/(a_(j,k)a_(i,j)),
    a_(i,j)=c_(o,o',i,j).                            (4.3)

Thus changing the anchor gives an edge coboundary with its
full value retained. These are identities of actual algebraic
functions; they do not discard a central multiplier or a phase.

## 5. The actual caps fix a different, compatible scalar

The cone correction by itself does not preserve the already
selected cap and cyclic normalizations. Write the shared-frame
actual pairings as mu_f(s) Mcal_f and cyclic maps as
xi_f(s) Ucal_f. Direct substitution gives the retained defects

    Hhat_f^t M_f(s') Hhat_(bar f)
          =d_f M_f(s),
    d_f=b_f b_(bar f) mu_f(s')/mu_f(s),

    U_f(s') Hhat_f
          =u_f Hhat_(r f) U_f(s),
    u_f=(b_f/b_(r f)) xi_f(s')/xi_f(s).               (5.1)

They are not generally one. At N=2 and the regular reduction
p=241 in the audit, face (1,2,3) has d_f=152 and u_f=45.
This refutes a claim that the cone scalar alone supplies the
actual pivotal comparison; it does not obstruct the following repair.

For two finite source flags use the actual edge modules, with
fixed g_ij=(1,p_i-p_j). On each chosen edge orientation define
T_ij by the normalized Hilbert-90 product

    h_0=1,
    h_n=product_(r=1)^n
          (A_i(s')-A_j(s')x_ij Q^r)/
          (A_i(s)-A_j(s)x_ij Q^r),
    T_ij=H(x_ij)^(-1)diag(h_n)H(x_ij).              (5.2)

The cyclic norm of the ratio is one. Its marked evaluation
fixes the scalar and makes composition strict. Let J_ij(s)
be the actual source-normalized cap, already shared on the
whole edge. Define the reverse adapter by

    T_ji=J_ij(s')^(-1) T_ij^(-t) J_ij(s).            (5.3)

It is an intertwiner of the reverse edge modules and preserves
the cap exactly. The double-dual identity
J_ij^(-t)J_ji=X^(N-1), together with [T_ij,X]=0, gives the same
naturality on the reverse orientation. Equations (5.2)--(5.3)
also compose strictly.

The actual face adapter S_f is now fixed by

    (T_ij tensor T_jk) C_(f,s)
           =C_(f,s') (T_ik tensor S_f).              (5.4)

To prove existence, conjugate the left side by C_(f,s')^(-1)
and remove T_ik. The remainder commutes with the total full
matrix algebra, so it is I tensor S_f. Its partial trace divided
by N computes S_f explicitly. The relative generators show

    S_f=theta_f H_f(s',s), theta_f nonzero.           (5.5)

The scalar theta_f is fixed by (5.2)--(5.4), not chosen to
force a period. Tree naturality, cap naturality and the trivalent
definition of the corrected cyclic map prove, respectively,

    R_(s')(S_A tensor S_B)=(S_C tensor S_D)R_s,
    S_f^t M_f(s') S_(bar f)=M_f(s),
    U_f(s') S_f=S_(r f) U_f(s).                     (5.6)

These assertions include every scalar and hold at all N>=2.
They also compose strictly in the source flag. In particular

    delta theta=c=delta b.

Thus theta/b is a configuration two-cocycle: the actual edge
data supply the further scalar correction needed by (5.1).
This extends the earlier affine triangle transport to the
specified pivotal and cyclic face data. It does not specialize
a separately singular edge cap at s=infinity.

## 6. The normal chart is the same source family

Let the geometric flags collide as

    p_i=p_*+epsilon delta_i,
    B_ij=epsilon^(1/N) b_ij, b_ij^N=delta_i-delta_j.

If the source also approaches the collision, write

    s=p_*+epsilon sigma,
    A_i(s)=epsilon^(1/N)(delta_i-sigma)^(1/N).        (6.1)

All common fractional powers cancel from (1.1) and (1.3).
The resulting triangle module and face frame are exactly
the source-flag family for (delta_i,sigma), independent of
epsilon. This is an algebraic identity on the marked root
chart, not an estimate.

A source s staying away from p_* is the chart sigma=infinity.
More precisely its local coordinate is

    tau=1/sigma=epsilon/(s-p_*),
    (A_i(s)/A_j(s))^N=(1-tau delta_i)/(1-tau delta_j).
                                                        (6.2)

Thus the normal source and its transverse coefficients are
ordinary algebraic jets of this same family at the source
flag infinity. A full projective transformation of the
normal flags also moves that source flag. Fixing infinity
selects the affine subgroup; replacing the transported
source by the default unit would change the data.

At this stage (6.1)--(6.2) identify the local triangle source
chart. Identifying its epsilon with the actual marked
meridian normal coordinate and carrying the whole cut/source
lattice are additional requirements.

## 7. The non-scalar first coefficient and the affine source class

For fixed finite s avoiding p_*, put w_s=(p_*-s)^(-1),
and w_infinity=0. Set beta=b_ik/b_jk and let H=H(beta).
The frame is regular and invertible in epsilon: the shared
fractional edge factor has canceled, and t_f(0) differs from
zero and one. Its source adapter has expansion

    H_f(s',s)=I+epsilon B_f+O(epsilon^2),

    B_f=(w_(s')-w_s)/N H^(-1)diag(J_f(n))H,
    J_f(n)=-(delta_j-delta_i)
              sum_(r=1)^n beta Q^r/(1-beta Q^r)
                      -n(delta_k-delta_i).           (7.1)

This follows by differentiating the finite product phi, using
rho=beta[1+epsilon w_s(delta_j-delta_i)/N+...]
and a=nu[1+epsilon w_s(delta_k-delta_i)/N+...].
In particular B_f commutes with D_f. The linear intertwining
identity is

    [B_f,Y_0]=(w_(s')-w_s)/N
       [(delta_i-delta_k)I-(delta_j-delta_k)D_f]
                                      sigma_Q^(-1). (7.2)

Its right side is nonzero for distinct flags and distinct
sources. Hence B_f is not scalar and B_f*1 has a nonconstant
part. A scalar cone or edge correction cannot erase that
part. For Hhat its first coefficient is B_f plus the retained
scalar derivative of b.

This is the promised affine normal-lift interpretation.
For a fixed ordinary vector v_0, an adapter I+epsilon B sends

    v_0+epsilon v_1 -> v_0+epsilon(v_1+Bv_0).
                                                        (7.3)

Suppose the difference automorphism sigma_diff fixes epsilon,
and v_0 is horizontal for C_0. If its lift obeys
sigma_diff(v_1)=C_0 v_1+c, (7.3) changes the source by

    c -> c+sigma_diff(Bv_0)-C_0 Bv_0.               (7.4)

Thus the local source-flag adapter supplies an explicit
translation in the same difference cokernel as the affine
quantum-A extension. This is a conditional comparison
formula; no identification with the actual knot source
has been assumed.

In particular (7.4) changes a representative by a difference
coboundary. It does not make a nonzero actual extension class
split by passing to a finite cover; the trace obstruction in
[the affine extension proof](affine_quantum_a_period.md) still applies.

The cut row must also move. For
ell=ell_0+epsilon ell_1, inverse transport gives
ell_1 -> ell_1-ell_0 B. Consequently the selected first
coefficient ell_0 v_1+ell_1 v_0 is preserved exactly.
At higher retained orders the usual finite convolution
of Taylor coefficients gives the complete jet action.
Keeping the ordinary fiber while dropping these normal
changes would lose the selected period data.

## 8. Coverage, audit and the remaining global comparison

These are the existing cyclic Weyl/Borel modules underlying
[Kashaev's cyclic 6j definition](https://arxiv.org/abs/hep-th/9411147).
The odd-level standard matrix definition compared in the previous
note is [Baseilhac--Benedetti's](https://arxiv.org/abs/math/0306283).
Their abstracts were checked for coverage; their invariance,
symmetrization and state-comparison proofs are not premises.
No novelty is claimed for normalized Hilbert-90 transport.
The contribution here is the source-flag parameterization,
the explicit full-scalar/actual-dual adapters and their
normal-jet interpretation for the specified period problem.

[The independent audit](../experiments/audit_source_flag_transport.py)
checks symbolic projective invariance and the two normal-chart
identities. At N=2,3,4,5,6,9 it checks 60 triangle adapter
compositions, 60 actual edge-induced pivotal face adapters,
their cap and cyclic naturality, 24 full ordered tetrahedron
comparisons and moving-source inversions, the scalar cocycle,
six anchor-change formulas and 60 nonzero first normal shears.
The anchor cap/turn defects are recorded before their exact
edge-induced repair. All checks pass, with every scalar retained.
[Results](../experiments/source_flag_transport_results.json).

    python3 experiments/audit_source_flag_transport.py

The ideal triangulation supplies the geometric developing flags
and marked Bloch class. This note gives a more explicit local
source family and finite-source dual transport on those charts.
It still does not construct the full equivariant colored
presentation of the actual ADO cut on that triangulation,
prove its relevant geometric A-block, or identify its selected
all-level norm with the Bloch-regulator norm. The source flag
at infinity must retain the genuine edge degeneration and
normal lattice. The original volume conjecture remains unproved.

The [actual threaded-character separation](ado_threaded_shadow.md)
also remains in force. The source-flag family does not identify
the actual rational root state with a fixed hyperbolic central
eigenline. A successful global comparison must keep its relative
source and selected evaluation, as required by that test.

The subsequent [carry extension](source_flag_carry_extension.md)
now supplies the full integral tree/source comparison at the
marked infinity. The total source frame cancels the fractional
edge weights to the integer carry, giving the same carry lattice
and its actual sublattice in all those source charts. Their full
duals and the original whole cut evaluation extend as well.
This resolves the ordered-tree lattice issue identified above;
it does not identify the full geometric tensor presentation,
the marked meridian normal coordinate or the regulator norm.
