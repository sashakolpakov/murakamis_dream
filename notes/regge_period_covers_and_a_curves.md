# Regge symmetries, nilpotent period transport, and covers of A-curves

Research note, 26 October 2026, following the user's suggestion of a
twisted Regge group and descent from a cover. There is an explicit
finite-by-Heisenberg structure for the ideal tetrahedron's classical
period. A finite ordering cover removes its finite part. We also
derive the peripheral elimination and quantum restriction-of-scalars
constructions for a manifold cover. None is asserted to identify
the selected original Kashaev period on two different manifolds.

Existing coverage includes the Regge transformation stated in
[Akopyan--Izmestiev, 1903.04929](https://arxiv.org/html/1903.04929v2#S1),
hyperbolic scissors congruence in
[Mohanty, math/0301318](https://arxiv.org/abs/math/0301318), and
the Weyl-group/period interpretation in
[Rudenko, 1908.01141](https://arxiv.org/abs/1908.01141).
For character varieties and A-polynomials under commensurability,
see the stated results of
[Long--Reid](https://web.math.ucsb.edu/~long/pubpdf/commensfinal.pdf).
Only definitions and stated scope were consulted. The elementary
group, period and elimination arguments below are independent.

## 1. The ideal part of the Regge group is smaller

Order the six edge coordinates by opposite pairs

    (a,a',b,b',c,c')=(01,23,02,13,03,12).

A Regge involution fixes a,a' and replaces each of the other
four coordinates e by s-e, with s=(b+b'+c+c')/2. Introduce

    p_i=(e_i+e'_i)/2, d_i=(e_i-e'_i)/2.

The involution swaps p_2,p_3 and acts on d by diag(1,-1,-1).
Vertex permutations act by all three-coordinate permutations
on p and by the 24 signed permutations with sign product +1
on d. The latter group acts faithfully as S_4 on

    (1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1).

The same diagonal sign change diag(1,-1,-1) occurs as a
vertex double transposition and acts trivially on p. Its
product with the Regge involution therefore swaps p_2,p_3
and fixes d. Conjugation gives the whole independent S_3
on p. Removing these p-actions from the vertex permutations
gives the independent S_4 on d. Consequently

    Regge = S_3(p) x S_4(d), order 144.            (1.1)

It is solvable of derived length three, with derived-group
orders 144,36,4,1. It is not nilpotent: its S_3 quotient has
lower central subgroup A_3 that remains A_3 on taking another
commutator with S_3.

For an ideal tetrahedron the dihedral-angle coordinates have

    d_1=d_2=d_3=0, p_1+p_2+p_3=pi.

Thus the faithful action on ideal angles is just S_3, with
kernel the S_4 factor in (1.1). The extra Regge involution
merely swaps the other two angles. Nontrivial additional
transport can still occur on logarithmic lifts, orientations,
face tensors and source lattices; it is not an additional
continuous symmetry of the ideal angle simplex.

## 2. The explicit twist on the logarithmic period

This section uses a local tetrahedral period, distinct from
the globally normalized peripheral R in the earlier notes.
Set tau=pi*i and, for Im z!=0, use principal branches

    u=Log z, v=Log(1-z),
    r=Li_2(z)+uv/2,
    epsilon=sign(Im z).

Then dr=(u dv-v du)/2. The shape generators

    rho(z)=1/(1-z), sigma(z)=1-z

have the exact lifts

    rho: (u,v,r,epsilon)
      ->(-v, u-v-epsilon*tau,
                  r-epsilon*tau*v/2-tau^2/6, epsilon),

    sigma: (u,v,r,epsilon)
      ->(v,u,-r-tau^2/6,-epsilon).                (2.1)

These follow by differentiating the displayed dilogarithms.
For sigma, the constant is fixed by Li_2(1)=pi^2/6.
For rho, evaluate the constant at its fixed point
z=exp(epsilon*pi*i/3); no value of its dilogarithm is needed.
Direct substitution verifies rho^3=sigma^2=1 and
sigma rho sigma=rho^(-1), with the changed epsilon used
at each step. A frozen choice of its sign would fail.

There is a useful simultaneous centering:

    ubar=u-epsilon*tau/3,
    vbar=v+epsilon*tau/3,
    rbar=r-epsilon*tau*(u+v)/6+tau^2/12.

It gives

    drbar=(ubar dvbar-vbar dubar)/2,
    rho:   (ubar,vbar,rbar)->(-vbar,ubar-vbar,rbar),
    sigma: (ubar,vbar,rbar)->(vbar,ubar,-rbar).     (2.2)

Thus the central period transforms by the determinant
character of this integral two-dimensional S_3 action.
The orientation-twisted coordinate epsilon*rbar is invariant
under that finite action. Equivalently, epsilon*D_Bloch(z)
is invariant when the tetrahedral orientation is transported.

This twist matters for descent. The six ordinary Bloch values
in an unordered shape orbit consist of three D and three -D.
Their sum is zero. An untwisted product/norm of exponential
periods therefore erases the volume. Descending the oriented
period requires the determinant local system, rather than
averaging away its sign.

## 3. A finite-by-two-step-nilpotent period group

An explicit discrete Heisenberg lattice preserving (2.2) is

    H(a,b,c):
      ubar -> ubar+2tau*a, vbar -> vbar+2tau*b,
      rbar -> rbar+tau*(a vbar-b ubar)+tau^2*c/3,
      a,b,c in Z.

Its group law is

    (a,b,c)(a',b',c')
      =(a+a',b+b',c+c'+6(ab'-ba')).              (3.1)

Its commutator is central with c-coordinate 12(ab'-ba'),
and every further commutator is trivial. The lattice is an
enlargement convenient for the Tate constants; minimality
is not claimed. Actual logarithmic monodromies around zero
and one belong to it: in the centered coordinates they are
H(1,0,-2epsilon) and H(0,1,-2epsilon), respectively.

For an integral matrix A in the S_3 of (2.2), its action is

    (a,b)->A(a,b), c->det(A)c.

This preserves (3.1). Hence the period symmetries embed in
the explicit group

    H_Z semidirect S_3.                           (3.2)

Its kernel H_Z is two-step nilpotent and has index six.
The full semidirect product is not nilpotent, since its
S_3 quotient is not. This is the concrete virtually nilpotent
structure available here; it concerns the ideal shape period.
It does not assert that all actual quantum tensor transports
or their selected-source monodromy lie in this group.

Passing to the labeled shape cover removes the finite S_3
ambiguity. Away from shapes with stabilizers it is a sixfold
unramified cover of the unordered shape space. At fixed shapes,
including the regular ideal shape, its ramification must be
retained as an orbifold/root marking. The spectral lattices
in [the resonant-source calculation](cyclic_source_connection_and_resonant_flags.md)
are relevant to that extension, but are not identified with
this entire classical period object merely by their names.

The nilpotent connection is already explicitly soluble.
Its rank-three upper-triangular realization has strictly
upper-triangular connection matrix Omega, and a product of
three such matrices vanishes. Its path transport is exactly

    I + integral Omega + integral_(t_1<t_2)
                                      Omega(t_1)Omega(t_2). (3.3)

Thus only logarithmic integrals and their length-two iterated
integrals occur. These are periods; nilpotence does not make
their horizontal values rational functions. The fundamental
class still supplies the additive central mark.

### The quantum ordering maps are explicit Gaussians

The same finite ordering part can be solved on the existing
pointed shape module, without asserting a new quantum invariant.
Use the conventions of
[the pointed tetrahedron calculation](pointed_tetrahedron_gluing.md#2-explicit-pointed-root-intertwiners):

    R=r_0^2, order(R)=N, r_0^N=-1,
    X e_a=s R^a e_a, Y e_a=t e_(a+1),
    s^N+t^N=1,
    p_0=1, p_a=t^a/product_(j=1)^a(1-sR^j).

The target roots for rho are (1/t,r_0 s/t,r_0),
and those for sigma are (t,s,1/r_0). The pure Gaussian
intertwiners, before pointing, are

    (K_rho)_(i,a)=(-1)^a r_0^(a^2) R^(ia)/N,
    (K_sigma)_(i,a)=R^(ia)/N.                    (3.4)

To derive them, the zeroth spectral-projector column in the
earlier construction is the constant vector 1/N. For rho,
the remaining columns apply (-r_0^(-1)P^(-1)Z)^a to it,
where Z is the unit clock and P the unit shift. This gives
the first formula. For sigma the column operator is Z^a,
giving the second. Thus these matrices are independent of
the shape roots, with their Gaussian phases still retained.

For the target kernel p', set

    h_g=(K_g p')_0, J_g=K_g/h_g.                 (3.5)

The kernel is one-dimensional and its zeroth component is
one, so h_g is nonzero and J_g p'=p. Irreducibility and
this equality make every S_3 relation strict for the J's.
These are the existing pointed adapters, now in closed form.

The unpointed phase is also explicit. Direct matrix products
give

    K_sigma(R)K_sigma(R^(-1))=I/N,
    K_rho^3=(G_N/N^2) I,
    G_N=sum_(a=0)^(N-1)(-1)^a r_0^(a^2).         (3.6)

For the second equation, the product commutes with X,Y by
the order-three monomial transformation, so it is scalar.
Its (0,0) entry is G_N/N^2 after reindexing by a+b. The
sequence (-1)^a r_0^(a^2) is N-periodic even when N is
even. Orthogonality of the R-character sum proves |G_N|^2=N
for the complex unit roots. Its phase is not dropped.

In the standard Hermitian norm sqrt(N)K_g is unitary.
Consequently the pointed scalar has the exact norm

    |h_g|=||p'||/(sqrt(N)||p||).                 (3.7)

The normalizations in a finite ordering cycle telescope to
the explicit Gaussian scalar (3.6). They do not create an
uncontrolled exponential multiplier around that cycle.
This solves the quantum shape-ordering part at every N,
including even and composite N. It does not identify the
shape generator with the actual knot's relative source or
construct its full face-tensor Regge action.

## 4. What a finite manifold cover does to the geometric A-curve

Now let p:M'->M be an orientation-preserving finite cover of
degree D, with M a one-cusped hyperbolic knot exterior. For
one boundary component upstairs choose oriented peripheral
bases and write

    mu'=mu^a lambda^b, lambda'=mu^c lambda^d,
    P=[[a,b],[c,d]], k=det P>0.

Use the squared eigenvalues m,l of the earlier PSL boundary
convention, retaining SL sign characters separately. Restriction
of any representation downstairs gives exactly

    m'=m^a l^b, l'=m^c l^d.                       (4.1)

This map of two algebraic tori is an isogeny of degree k.
If A_geo(m,l)=0 is the marked geometric factor, the polynomial
of its image is obtained by Laurent elimination:

    (A_geo(m,l), m'-m^a l^b, l'-m^c l^d)
                            intersect C[m'^(+/-1),l'^(+/-1)]. (4.2)

Its radical is generated by an irreducible image polynomial.
A norm/resultant can carry a power of this polynomial: that
power is the generic degree of the map on the curve. It must
not be mistaken for another component.

If M' has one cusp, k=D. The image in (4.2) is its geometric
A-factor, with its indicated marking. Here is a local proof
of the assertion about the geometric branch. The lifted
positive geometric triangulation gives a smooth one-dimensional
marked gluing germ upstairs. Downstairs use U=Log m and
V=Log l with positive cusp slope t=dV/dU. The restricted
family has

    dU'/dU=a+b t !=0,

because Im t>0 and (a,b)!=(0,0). It therefore fills the
upstairs geometric germ locally. Taking its irreducible
algebraic closure gives exactly the indicated geometric factor.
This does not determine the other A-components upstairs:
representations there are not required to extend downstairs.

If M' has several cusps, its full boundary object is an
eigenvalue variety in a higher-dimensional torus. The restricted
downstairs family is one-dimensional, not the whole geometric
deformation space. The boundary degrees k_j satisfy sum k_j=D.

For the connected cyclic cover from the meridian modulo D,
there is one cusp and (mu',lambda')=(mu^D,lambda). Thus

    A'_geo(m',l') = square-free Laurent part of
                      Res_t(t^D-m', A_geo(t,l')). (4.3)

Conversely A_geo divides A'_geo(m^D,l). The marked lift
selects it among possible translated factors. The cover need
not be a knot complement in S^3, so the appropriate A-object
is that of its torus-boundary manifold.

## 5. The marked regulator descends with exactly the cover degree

Use the original peripheral normalization

    dR=-(U dV-V dU)/4.

On the common centered logarithmic cover, (4.1) gives

    U'=aU+bV, V'=cU+dV,
    U'dV'-V'dU'=k(UdV-VdU).                      (5.1)

For one cusp k=D. Lift the marked ideal fundamental cycle:
every tetrahedron and its flattening occurs D times. This
fixes the integration constant, so exactly on that marking

    p^*R'=D R,
    p^*P'=P^D,
    log||P'_hyp||=D log||P_hyp||,
    Vol(M')=D Vol(M).                            (5.2)

The map on period spaces is implicit in p^*. For multiple
cusps sum (5.1) over them; sum k_j=D gives the same marked
total regulator identity along the restricted family. This
is a genuine classical cover-and-descent law. It follows
from the lifted fundamental cycle, not from the A-polynomial
coefficients alone.

## 6. The quantum boundary parameter changes under the same map

For this algebraic statement choose a quantum-torus convention

    lhat mhat = qbold mhat lhat,
    W(a,b)=qbold^(ab/2) mhat^a lhat^b.

The half power is retained as a coefficient root, without
division by two modulo a level. Direct multiplication gives

    W(c,d) W(a,b)=qbold^k W(a,b) W(c,d).          (6.1)

Thus the peripheral inclusion embeds the cover torus with
parameter qbold'=qbold^k. It is not a map between the two
displayed quantum tori at an unchanged generic parameter.
The actual SL/PSL and half-longitude conventions must be
converted before applying (6.1) to the knot operator.

At a root of order N, qbold^k has order N/gcd(N,k).
Using the principal roots instead, qbold=exp(2pi*i/(kN))
gives qbold'=exp(2pi*i/N). A modular inverse choice when
gcd(N,k)=1 generally chooses another root embedding. It is
not automatically the original archimedean sequence.

This explains why a cover volume theorem cannot simply be
divided by D to prove the original finite-state conjecture:
the chosen period, level, source and boundary convention
must also be compared. No equality of knot invariants under
arbitrary finite manifold covers is assumed here.

## 7. A precise quantum transfer exists by restriction of scalars

For the cyclic case let F=C(qbold,m), F_0=C(qbold,u), u=m^k,
and sigma(m)=qbold m, sigma_0(u)=qbold^k u. Take the specified
semilinear module T=B(m)sigma of rank r. In the F_0 basis
1,m,...,m^(k-1), put

    Z e_a=e_(a+1), Z e_(k-1)=u e_0,
    D_q=diag(1,qbold,...,qbold^(k-1)).

Replacing coefficients f(m) by multiplication matrices f(Z)
gives the exact restricted matrix

    B_res = Mult(B) (D_q tensor I_r),
    T_res=B_res sigma_0, rank k r.               (7.1)

The rank-r block ordering in this formula is by powers of m.
This is a literal restriction of the original module, not
a definition of the actual quantum invariant of M'.

Assume B has a defined specialization at qbold=1. Its
restricted characteristic polynomial there is

    det(L-B_res,0)=Norm_(F/F_0) det(L-B_0).       (7.2)

Indeed after adjoining all k roots of u, the multiplication
representation diagonalizes into the k evaluations at zeta*m.
For a companion this is the resultant of its classical
symbol, including its leading-coefficient denominators.
No AJ theorem for the actual knot is inferred from (7.2).

There is also an exact root comparison wherever the specified
rational matrices specialize. If qbold has order N and
gcd(N,k)=1, sigma_0 has order N. The N-step monodromy
of (7.1) is the restriction of T^N. Its characteristic is

    D_res(u^N,v)
       =Norm_(C(m^N)/C(m^(kN))) D_N(m^N,v).       (7.3)

If gcd(N,k)>1 the minimal downstairs orbit is shorter;
its gcd(N,k)-th power is the restricted T^N, but (7.3)
cannot be used as the characteristic of that shorter orbit.
These extra sectors are retained, including at even levels.

Restriction also keeps the original source, with its extra
channels. A trivial rank-one F quotient restricts to rank k
over F_0, with semilinear matrix D_q. Its distinguished one
is the basis element 1, rather than all k directions being
declared a trivial line. Dropping these directions or taking
a scalar trace would change the selected period unless the
corresponding source and co-source comparison is proved.

## 8. The implication for the proposed strategy

An ordering/parameter cover can remove the finite Regge part
of the classical period transport; its Heisenberg equations
are explicitly solved by (3.3). A finite manifold cover has
the precise geometric A-factor and marked regulator laws
(4.2)--(5.2), and a natural candidate quantum transfer is
(7.1). This makes the cover strategy a concrete comparison
problem rather than an unspecified simplification of A.

A finite sigma-stable algebraic field cover cannot on its
own split a nonsplit horizontal affine source: taking the
normalized field trace of a putative splitting gives one
downstairs. This is proved in
[the affine source note](affine_quantum_a_period.md#2-finite-algebraic-covers-do-not-kill-a-nonzero-affine-class).
It does not rule out useful manifold covers, which change
the group and module. Nor does it identify their selected
Kashaev-type states with (7.1).

There is a precise group-theoretic target for the quantum
comparison. If Gamma is a transport group and Gamma_0
has finite index, their Zariski closures have the same
identity component. Indeed the larger closure is a finite
union of cosets of the smaller one, so its identity component
is contained in that smaller closure. The identity components
therefore coincide. A finite cover can remove a finite
permutation quotient; it cannot turn a nonnilpotent connected
transport group into a nilpotent one. For the period group
(3.2), the connected part is explicitly Heisenberg. For the
selected actual quantum period, identifying the relevant
connected group, or a marked quotient of it, remains necessary.

The useful cover statement must also be controlled across levels.
A finite group at one fixed root level can always be killed
by some finite cover, which by itself gives no bound on its
selected period as N grows. The ordering degree six here is
independent of N, and its quantum Gaussian cycles have the
explicit polynomial norms (3.6). The additional root covers,
source normalizations and level changes are retained separately.

The [subsequent actual-braid calculation](actual_braid_group_and_spectral_source.md)
now proves that the full retained braid transport has a
connected subgroup with an SL_2 quotient at every level.
Two genuine pure powers supply square-zero logarithms with
strictly negative mixed ordinary trace, and the actual
pivotal moment is -2N^2/(q-q^(-1)). Thus finite-index
restriction cannot make that full group nilpotent. The
finite ordering result above still holds. A useful cover
can instead split the explicit spectral source algebra,
reducing its simultaneous comparison to a scalar line.

The remaining conjecture is still the original marked
period identity (2pi/N)log|F_N(1)|->Vol(M). Its selected
quantum-A period has not been identified with the calibrated
regulator line, or descended from an upstairs selected
period with controlled norm. The braid-image theorem does
not determine the minimal operator's difference-Galois group.

[The audit](../experiments/audit_regge_cover_transfer.py)
checks the complete finite Regge action, the period lifts,
the orientation twist, the Heisenberg law, peripheral forms,
elimination, and the quantum restriction matrices.
[Results](../experiments/regge_cover_transfer_results.json).
