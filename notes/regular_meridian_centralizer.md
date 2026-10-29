# The regular meridian centralizer and the actual normalization line

Research note, 26 October 2026. There is a smaller commutative
group relevant to the framed geometric period: the centralizer
of the regular marked meridian. It is multiplicative away from
the parabolic fiber and additive on that fiber. Its framing
torsor, invariant differential and power adapters can all be
computed exactly. The actual ADO modified dimension is the
inverse Lie factor of one such adapter, with its original phase.

The group model G^(lambda) is an existing definition, already
recorded in [the uniform source-base note](uniform_frobenius_source_base.md#3-the-deformation-group-is-an-existing-definition),
from [Mezard--Romagny--Tossici, Section 1.2](https://arxiv.org/html/1104.2222v1#S1.SS2).
Here its parameter is the meridian eigenvalue gap, rather than
the quantum gap rho. The matrix calculations below supply the
geometric application without importing a classification proof.

This identifies the peripheral normalization line, not the
selected global quantum period or its Bloch-regulator norm.

## 1. The centralizer is a smooth commutative group model

On the marked meridian eigenvalue cover put

    kappa=M-M^(-1),
    mu_M=[M 1;0 M^(-1)].

This meridian is regular even at M=1, where it is a nontrivial
unipotent. Commutation of a general invertible matrix with mu_M
forces its lower-left entry to zero and a-d=kappa*b. Normalize
the lower diagonal entry to one in PGL_2. The projective image
of this GL_2 centralizer is

    J_M={C_b=[1+kappa*b  b;0 1]:1+kappa*b!=0},
    b*b'=b+b'+kappa*b*b',
    b^(-1)=-b/(1+kappa*b).                       (1.1)

It is commutative. Its generic multiplicative coordinate is
y=1+kappa*b; its kappa=0 fiber is the additive b-line. Its
invariant relative differential is

    omega_J=db/(1+kappa*b).                      (1.2)

These facts are identities of the smooth open affine-line
group scheme. A limit of diagonalizing matrices is unnecessary.
The PGL convention is explicit; fixed SL_2 sign characters
remain separate marked data.

On the open set M+M^(-1)!=0 this is also the full PGL_2
centralizer: a projectively commuting lift can only commute
with mu_M, since conjugation preserves its nonzero trace.
At trace zero there is an additional anticommuting component.
For example, at M=i the invertible matrix [1 0;-2i -1]
conjugates mu_i to -mu_i. All statements here use the
commutative regular centralizer (1.1); near the complete
meridian M=1 the distinction disappears.

This geometric meridian centralizer is distinct from the
large quantum commutant End_(U_q)(V^(tensor b)) computed in
[the intrinsic cut atlas](intrinsic_cut_and_meridian_atlas.md).
Its commutativity does not contradict the genuine SL_2 sector
of the full actual braid transport.

## 2. The framing torsor has an explicit quotient by this group

Use the same two framing coordinates as in the actual critical
correspondence, with

    F_M(r,s)=[r 1-r;s -kappa-s],
    Delta=s+kappa*r !=0,
    F_M(1,1)^t=(1,-kappa)^t.

The latter vector is the M^(-1) eigenvector of mu_M. Direct
conjugation gives

    F_M^(-1) mu_M F_M
       =[M+s -kappa-s;s M^(-1)-s]=mu_s.         (2.1)

In particular this boundary meridian is independent of r.
Left multiplication by C_b acts on the frame by

    r -> r+b Delta, s -> s,
    Delta -> Delta(1+kappa*b).                   (2.2)

Where s!=0, r=0 is a section and b=r/s is the torsor coordinate.
Thus r is the residual centralizer direction, while s records
the boundary coadjoint coordinate. At completeness the action
is r->r+bs. These statements hold for every representation in
the marked chart, independently of its knot presentation.

The initial position coordinate on the classical critical chart
of the actual balanced state is

    A_cut=M/(M+s),                               (2.3)

because x=-M and the raw K is -(M+s). At fixed M an invariant
framing two-form adapted to this original cut coordinate is

    Omega_cut=(dr/Delta) wedge dlog A_cut
             =-dr wedge ds/[Delta(M+s)].         (2.4)

Its fundamental centralizer vector is V_J=Delta partial_r.
Direct differentiation gives

    Lie_(V_J) Omega_cut=0,
    contraction_(V_J) Omega_cut=dlog A_cut.       (2.5)

At M=1 this is -dr wedge ds/[s(1+s)]. It is not an arbitrary
choice of Haar measure on the two-dimensional framing group:
it uses its one-dimensional centralizer and the specified cut
coordinate. If t=r/s, then it is -dt wedge ds/(1+s).

Equation (2.5) is a canonical algebraic reduction of this form.
It does not yet prove that the actual selected finite period
implements that contraction or divides out a group volume.

## 3. The marked A-curve supplies a second section of J_M

Let ell be the centered longitude eigenvalue, with ell(1)=1;
retain the original preferred-longitude sign separately. Any
SL_2 longitude commuting with mu_M has the form

    lambda=[ell (ell-ell^(-1))/kappa;0 ell^(-1)]. (3.1)

Normalize its lower diagonal entry in PGL_2. Its section of
the same group (1.1) is

    b_lambda=(ell^2-1)/kappa,
    b_mu=M,
    1+kappa*b_lambda=l=ell^2,
    1+kappa*b_mu=m=M^2.                         (3.2)

On the normalized smooth geometric branch,

    b_lambda|_(M=1)=dlog ell/dlog M=tau_cusp.     (3.3)

This is an ordinary value of a regular function: both numerator
and denominator in (3.2) have simple first meridian terms.
The positive cusp shape selects the geometric direction.

The geometric A-equation in these coordinates is exactly

    A_geo(M^2,1+kappa*b_lambda)=0.                (3.4)

Its strict transform removes the common kappa power; the
exceptional polynomial is its tangent-cone equation in
b_lambda. Distinct slopes separate there. Normalization still
retains the branch mark if several branches have the same
tangent. The group model alone does not supply the marked
central regulator constant or its volume.

## 4. Powers give the actual ADO normalization, including its phase

Define the Laurent polynomial

    u_n(M)=(M^n-M^(-n))/(M-M^(-1)),
    u_0=0, u_1=1,
    u_(n+1)=(M+M^(-1))u_n-u_(n-1).

Matrix multiplication gives exactly

    mu_M^n=[M^n u_n(M);0 M^(-n)].                (4.1)

At M=1 the polynomial has value n, and at M=-1 it has value
(-1)^(n-1)n. The original full ADO factor is therefore

    d_N(M)=eta_N/u_N(M), eta_N=i^(N+3).          (4.2)

This is precisely the previously fixed formula, since
u_N=M^(1-N)(1+M^2+...+M^(2N-2)). It is an exact algebraic
evaluation, with its whole meridian germ and phase retained.

For a power degree D, let H_D=diag(u_D(M),1). Wherever
u_D!=0, it is the canonical meridian normalization adapter:

    H_D^(-1) mu_M^D H_D=mu_(M^D),
    H_D^(-1) C_b^(kappa) H_D
                 =C_(b/u_D)^(kappa_D),
    kappa_D=M^D-M^(-D)=kappa*u_D(M).             (4.3)

Its map on the centralizer Lie coordinate is multiplication
by 1/u_D. Thus the actual dimension line is eta_N times
this determinant line for D=N. At the parabolic fiber the
adapter is diag(D,1), so the original value eta_N/N follows
without separately evaluating two zero factors.

### The same adapter is a determinant and residue map

There is an intrinsic spectral-algebra version. Put

    B_M=R[T]/(T^2-(M+M^(-1))T+1).

The regular matrix mu_M is cyclic: the vectors e_2,mu_M e_2
form a basis of determinant -1 at every M. An operator
commuting with mu_M is therefore uniquely a+b mu_M. This
identifies its GL_2 centralizer with B_M^times, including the
nonreduced fiber B_1=R[epsilon]/(epsilon^2), epsilon=T-1.
Its norm is

    Norm(a+bT)=a^2+(M+M^(-1))ab+b^2.

The PGL normalization of (1.1) is the class of
(1-b/M)+bT; its norm is 1+kappa*b. Adjoining the marked
square root of that norm gives its SL_2 lift. This is a
spectral unit torsor, with its quadratic root retained.

For a degree D power define

    phi_D:B_(M^D)->B_M, T'->T^D.

The Cayley--Hamilton relation gives, integrally,

    T^D=u_D(M)T-u_(D-1)(M),
    Mat(phi_D)=[1 -u_(D-1);0 u_D],
    det(phi_D)=u_D(M).                           (4.4)

Use the canonical algebraic residue Res_M(a+bT)=b.
Its Gram matrix in 1,T is [[0,1],[1,M+M^(-1)]], with
determinant -1 even at the dual-number fiber. Equation
(4.4) gives the exact comparison of these functionals:

    Res_M(phi_D(f))=u_D(M) Res_(M^D)(f),
    (d_D(M)/eta_D) Res_M(phi_D(f))
                                  =Res_(M^D)(f). (4.5)

The same map also preserves the spectral norm exactly:

    Norm_(B_M)(phi_D(a+bT'))
       =a^2+(M^D+M^(-D))ab+b^2
       =Norm_(B_(M^D))(a+bT').                  (4.6)

Indeed mu_M^D has determinant one and the indicated trace,
so the determinant of aI+b mu_M^D is that polynomial.
The norm torsor and the residue co-source therefore have
compatible cover maps, including at the dual-number fiber.

Thus the normalization line and its residue co-source are
compared together. At M=1, phi_D(epsilon')=D epsilon;
the original 1/D factor is its exact dual correction. This
does not identify B_M with the knot's entire quantum-A
spectral algebra or its two-Casimir source: it proves the
specified peripheral determinant and residue-line identity.

The adapter becomes singular at a nontrivial torsion root
where mu_M^D is scalar. The regularized lattices in
[the resonant-source calculation](cyclic_source_connection_and_resonant_flags.md)
must be retained there; a regular matrix conjugation through
that point is not asserted.

The actual root-central augmentation is still the identity
representation in the earlier threaded-character test.
We have not identified it with the nontrivial geometric
parabolic mu_1 or with mu_M^N. Equations (4.2)--(4.3)
identify the peripheral scalar line and its adapter only.

## 5. The source normalization composes exactly across cover degrees

Taking powers in two orders gives

    u_(DN)(M)=u_D(M)u_N(M^D)
             =u_N(M)u_D(M^N).                   (5.1)

The original phases satisfy

    eta_(DN)/(eta_D eta_N)=i^((D-1)(N-1)).

Consequently the exact dimension tower is

    d_(DN)(M)=i^((D-1)(N-1)) d_D(M)d_N(M^D).    (5.2)

Its phase factors obey the associative three-degree cocycle
identity, by expanding their integer exponents. This includes
even and composite degrees. For example

    d_(2N)(M)/d_N(M)
                 =i^N M^N/(1+M^(2N)).          (5.3)

The peripheral factor becomes i^N/2 only after M=1. This
is a verified power-composition factor; identifying a move's
multiplier still requires its actual source adapter.

The paired actual source comparison has a simpler strict law.
Its previously proved scalar is

    Gamma_N=gamma_N(M)gamma_N(M^(-1))
           =d_N(M)/(N eta_N)=1/[N u_N(M)].

It therefore satisfies the exact identity

    Gamma_(DN)(M)=Gamma_D(M) Gamma_N(M^D).       (5.4)

This supplies a coherent peripheral paired line across power
covers. It is not an identification of the tensor spaces or
selected knot periods at levels D,N,DN.

The actual root meridian step is compatible as well:

    d_N(q_N M)/d_N(M)
              =-kappa(q_N M)/kappa(M),          (5.5)

because (q_N M)^N=-M^N. Thus this line has exactly the
original ADO difference cocycle, not a newly chosen gauge.

## 6. Covers also transform the framing coordinate

For the connected meridional D-cover, the longitude is
unchanged while M'=M^D. Equations (3.2) and (4.3) give

    b'_lambda=b_lambda/u_D,
    tau'_cusp=tau_cusp/D.

The actual boundary coadjoint coordinate changes differently.
The Cayley--Hamilton power formula in (2.1) gives

    mu_s^D=mu_(s'), evaluated at M'=M^D,
    s'=u_D(M)s.

The normalized cover frame is

    F_(M^D)(r,u_D s)=u_D H_D^(-1) F_M(r,s).      (6.1)

In particular

    A'_cut=M^D/(M^D+u_D s),                     (6.2)

which is generally different from A_cut^D. This distinguishes
the internal position coordinate from the peripheral eigenvalue
m, whose cover map really is m'=m^D.

Pulling back the two-form (2.4) yields exactly

    Omega'_cut/Omega_cut=(M+s)/(M^D+u_D s).      (6.3)

Thus a cover comparison must keep both the Lie adapter and
the specified cut-coordinate Jacobian. The regulator's
degree-D law from the A-curve cover note does not replace
this local source data.

## 7. Relation with the actual normal density

The exact figure-eight calculation on the full two-variable
framing chart now gives

    Omega_actual^2=-tau_cusp/[6 s^2(1+s)^2]
                                      (dr wedge ds)^2.

It has precisely the dependence of Omega_cut^2 at M=1,
with a representation-dependent scalar -tau_cusp/6. The
old tests against dr ds/s and dr ds/s^2 did not test the
centralizer/cut form (2.4). The
[two-variable audit](../experiments/audit_full_framing_density.py)
retains both free variables, the actual coefficient amplitude,
the two Hessian null vectors and its transverse determinant
in Q(sqrt(-3))(s,r). The exact identity proves independence
of r; no interpolation or finite-field inference is used.
[Results](../experiments/full_framing_density_results.json).
The displayed density law is not asserted for every knot.

The uniform conclusions proved here are the geometric
centralizer, its framing quotient, its marked longitude
section, and the exact original normalization and cover
composition laws. Establishing that the actual source
implements the reduction (2.5), and then transporting the
selected period to its geometric regulator line, remains
necessary for the original volume conjecture.

## 8. At the additive fiber the relative boundary is essential

The quotient form specifies a sharper requirement on the
source. On the chart s!=0 put t=r/s. At M=1 one has

    Omega_cut=dt wedge dlog A_cut
             =d(t dlog A_cut), A_cut=1/(1+s).    (8.1)

Thus its ordinary closed two-periods vanish on this chart.
Commutativity of the centralizer does not give a nonzero
absolute period by itself. Its relative boundary data cannot
be discarded during the proposed reduction.

For a concrete relative cycle let gamma be a closed curve
in the s-plane avoiding 0,-1, and take the oriented chain

    Gamma=[t_0,t_1] times gamma.

Stokes' theorem gives exactly

    integral_Gamma Omega_cut
       =(t_1-t_0) integral_gamma dlog A_cut.     (8.2)

For a positive small circle around s=-1 the last integral
is -2 pi i; around s=0 it is zero. The endpoint separation
is part of the relative source, rather than a consequence
of the invariant two-form. Setting it to one specifies a
normalization, which must be compared with the actual cut.
The rectangular cycle here is a model relative class; it
has not been identified with that selected quantum cut.

Off the parabolic fiber the same chart has

    Omega_cut=db/(1+kappa*b) wedge dlog A_cut,
    b=r/s,
    kappa Omega_cut=dlog(1+kappa*b)
                                      wedge dlog A_cut. (8.3)

The multiplicative fiber has an absolute logarithmic circle;
the additive fiber does not. This elementary change is why
one must transport a relative source or its regularized
lattice, not just a class of ordinary closed cycles. It
agrees with the earlier need to retain resonant normal jets,
without identifying the different source constructions.

The subsequent [actual cut-residue calculation](actual_cut_residue_and_principal_density.md)
now identifies beta=dlog A_cut in the original finite cut
pairing, with its canonical representative, pole packet and
normal carry retained. It also derives the principal
crossing determinant and pivotal-volume factors uniformly.
The remaining relative pushforward is not supplied by
this exact boundary co-source identification.

[The audit](../experiments/audit_regular_meridian_centralizer.py)
checks the group, frame, longitude, invariant-density and
cover identities, including the full normalization phases.
[Results](../experiments/regular_meridian_centralizer_results.json).
