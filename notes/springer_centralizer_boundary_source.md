# The compact source is the boundary of a resolved geometric framing torsor

Research proof, 27 October 2026. The regular-unipotent meridian
centralizer torsor has a canonical renormalized compactification.
Its exceptional divisor is the actual compact coherent source
X=(P1 times P1) minus the incidence divisor. This is an explicit
matrix construction, not just an equality of dimensions or a local
choice of framing coordinates.

The principal Gaussian framing form, with its actual diagonal flag
co-source retained, has a global nonzero logarithmic residue class
on this divisor. The intrinsic coherent source line and all normal
weights are determined as well. The logarithmic source/current
complex is still required to use this class in the selected quantum
period: allowing an unrestricted logarithm of the normal would make
its logarithmic differential exact.

The actual finite source geometry is proved in
[the compact coherent calculus](compact_coherent_source_period.md).
The explicit r,s,p gauge and physical-symbol section used below are
independently calculated in
[the compact framing and residue construction](compact_framing_gauge_and_boundary_residue.md).
The principal Gaussian comparison is the general theorem of
[the density-line calculation](quantum_source_bridge_extension.md).

## 1. The cut meridian has its literal Springer resolution

Fix the physical meridian sign so the complete eigenvalue is +1.
The unipotent cone is mu=I+N, where tr N=det N=0. Its resolution is

    L=Tot(O_P1(-2)),
    N(v,eta)=eta [[-v,1],[-v^2,v]],
    eigenflag=[1:v].                                      (1.1)

The other chart has

    V=1/v, eta'=-v^2 eta,
    N=eta' [[V,-V^2],[1,-V]].                              (1.2)

Both formulas are verified by multiplication. Away from N=0 its
unique kernel/image line recovers the retained flag. At N=0 the
flag is the exceptional P1. Thus this resolves the cut meridian;
it does not assert that a whole irreducible representation has a
regular raw-matrix limit when this meridian approaches I.

For the actual physical compact symbol, put

    a=z/(1+wz), v=w, T=v a,
    A=exp(c T), p=1/v, c=2pi*i.

Its complete Gauss matrices give exactly

    eta_phys=(1-A^(-1))/v,
    mu-I=N(v,eta_phys).                                  (1.3)

At v=0 the quotient has the removable value c a. More explicitly

    eta_phys=(1-exp(-c v a))/v=c a+O(v a^2),
    partial_a eta_phys=c exp(-c v a),                     (1.4)

so it is a local holomorphic change of coordinates at the compact
north pole. In the south chart, a'=v-v^2a and T'=V a'=1-T;
since exp(c)=1,

    eta'_phys=(exp(c V a')-1)/V=c a'+O(V(a')^2).           (1.5)

Both real compact poles therefore retain their limiting eigenflag.
The exact form identity is

    dv wedge d eta_phys/(1-v eta_phys)
                 =c dv wedge da
                 =c dw wedge dz/(1+wz)^2.                (1.6)

This is an algebraic/logarithmic resolution of the physical symbol:
one may retain A as a multiplicative coordinate with the marked
relation Log A=c va. There is no N-dependent limit in (1.3)--(1.6).
The clock is still a period of its exponential connection, not an
algebraic function on a finite cover of X. Globally A=1 has every
integer T fiber; the two poles above are the endpoints of the
specified real compact cycle, not the entire analytic divisor.

## 2. The full geometric framing torsor has a nonextendible pole

Choose the reference cut meridian I+E_12 of a fixed irreducible
representation. The full projective conjugation torsor is G=PGL2.
Its map to the nonzero cone is

    g -> g E_12 g^(-1),

with fiber the additive regular-unipotent centralizer. On the
Springer charts with eta!=0 take the projective sections

    g_N=[[1,0],[v,eta^(-1)]],
    g_S=[[V,(eta')^(-1)],[1,0]].                           (2.1)

Their conjugations of E_12 are precisely (1.1)--(1.2). Directly,

    g_N^(-1)g_S ~ [[1,-1/(v eta)],[0,1]],                 (2.2)

where ~ means equality after a nonzero scalar. If b_N,b_S are
the additive centralizer coordinates on the right, then

    b_S=b_N+1/(v eta).                                   (2.3)

This torsor cannot extend as an ordinary algebraic Ga torsor over
the zero section of L. Here is an elementary proof. On the
punctured line bundle the cocycle in (2.3) has fiber degree -1.
A coboundary of that degree is a sum

    eta^(-1) f(v)+(eta')^(-1)g(V)
      =eta^(-1)[f(v)-v^(-2)g(1/v)].                       (2.4)

The Laurent powers available on the right are >=0 and <=-2.
The required v^(-1) is missing. Thus (2.3) has nonzero Cech class.
On the whole bundle only nonnegative fiber degrees occur. At
degree j>=0, the north regular powers are >=0 and the south ones
are <=2j; together they span every Laurent power. Hence every
regular Ga torsor on this two-chart total space has zero class.
Its restriction cannot equal (2.3). This proves the obstruction
without a torsor-triviality citation.

For the elementary additive-descent step used here, an additive
torsor on an affine chart is trivial: on a finite principal-open
trivializing cover, clear all cocycle denominators by powers f_j^k,
write 1=sum_j h_j f_j^k, and take the weighted sums of its additive
transition functions. The cocycle identity makes these sums a
coboundary. Thus no affine-chart torsor has been omitted from the
two-chart calculation.

There is also a direct irreducible-representation obstruction.
Conjugating by diag(r,r^(-1)) makes the chosen meridian
I+r^2E_12 approach I. Some other group element has a nonzero
lower-left coefficient, because otherwise the representation
preserves the chosen line. That coefficient becomes r^(-2)c.
The raw representation escapes. Resolving its cut eigenflag
does not remove this pole of the full irreducible framing family.
This obstruction is independent of the chosen degeneration: for
U=I+E_12 and B=[[a,b],[c,d]] in SL2, direct multiplication gives
tr[U,B]=2+c^2. Irreducibility supplies some c!=0. If a regular
raw limit had its cut meridian equal to I, this trace would tend
to 2, contradicting its conjugation-invariant value. Thus no
different regular raw framing can evade the escape.

## 3. Renormalizing the centralizer produces the actual source X

Use the determined rescaling

    a_N=-eta b_N, a_S=-eta' b_S.

Equation (2.3) becomes exactly

    V=1/v, a_S=v-v^2 a_N.                                (3.1)

This is the compact coherent-source torsor. Indeed with
a_N=z/(1+vz), one has a_S=v/(1+vz), and its complement condition
is the transversality of the two flags

    ell=[1:v], ell_other=[-z:1].

Thus the renormalized space is the threefold

    Y=Tot(O_P1(-2)) times_P1 X,
    E_exc={eta=0}=X.                                     (3.2)

Its open part eta!=0 is exactly PGL2 by (2.1)--(2.3), not merely
birational to a new state. In north coordinates its actual
projective conjugator has the polynomial representative

    g(v,eta,a)=[[eta,-a],[eta v,1-va]], det g=eta.           (3.3)

At eta=0 this is rank one. Its image is the second flag and
its first-column direction is the retained flag; the two are
transverse. Formula (3.3) displays the compact source as the
exceptional data of a degenerating actual projective frame.
The south representative is -v times (3.3), with the appropriate
south row convention. Scalar transition does not change conjugation.

The original constant Ga action b->b+c becomes a->a-eta c.
It vanishes on E_exc. The rescaled additive group of the line
O(-2), acting by translation in a, instead extends freely. This
is the precise twisted-centralizer replacement at the shell;
there is no global choice a=0 in the nontrivial affine torsor X.

The full representation extends on its elementary-modification
lattice g O^2, with its projective scalar clutch retained. In
that lattice the representation matrices are the fixed reference
ones. Its abstract cut meridian remains nontrivial; only its
singular inclusion into the original raw trivialization has
become I. This associated-bundle extension must not be mistaken
for an ordinary regular deformation of the raw representation
to the central identity color.

## 4. The global logarithmic volume has the compact source residue

Define the invariant three-form on the actual frame torsor by

    H_G=d eta wedge dv wedge db.

Its normalization is specified by this equation. To verify invariance,
on the SL2 cover write g=n_-(v)diag(r,r^(-1))n_+(b), r^2=eta.
The h,e,f components of its Maurer--Cartan form have wedge
r dr wedge db wedge dv=-H_G/2; conjugation by n_+(b) has determinant
one, so this calculation holds for all b. Thus the stated factor
of -2 relative to that Maurer--Cartan convention is explicit.
Substitution
b=-a/eta gives its exact extension to Y:

    H_G=-(d eta/eta) wedge dv wedge da.                    (4.1)

This is global: dv wedge da is unchanged by (3.1), while
d eta'/eta'=d eta/eta+2dv/v, whose added term wedges to zero.
Consequently

    Res_(E_exc) H_G=-dv wedge da=2pi*i omega_I,
    omega_I=-(1/(2pi*i))dv wedge da.                      (4.2)

The compact coherent sphere Gamma has integral omega_I=1.
Thus (4.2) is a nonzero global algebraic de Rham class on X.
A small normal circle bundle over Gamma is a lens-space cycle
with Chern number -2, the compact PGL2 framing cycle. No global
normal-circle section is needed for the residue pairing.

The line-bundle calculation agrees with the explicit form:

    K_Y=pi^*O(2), O(E_exc)=pi^*O(-2),
    K_Y(E_exc)=O, K_(E_exc)=K_X=O.                        (4.3)

In particular the logarithmic volume and its residue have trivial
torus weight even though the ordinary centralizer torsor did
not extend.

### 4.1 The actual principal Gaussian has the same nonzero residue

This comparison uses the actual diagonal Hopf scaling, not an
assumed arbitrary classical source action. On the old inverse-flag
cut chart at complete meridian, retain its centralizer coordinate r
and scale s:

    F(r,s)=[[r,1-r],[s,-s]],
    Omega_cut=-dr wedge ds/[s(1+s)].

Allow the exact common diagonal momentum gauge p, and take the
source conjugator g=(F(r,s)diag(p^(-1),1))^(-1). The explicit
comparison with (2.1) is

    v=1/p, eta=-s p, b=(1-r)/s,
    a=p(1-r), A_cut=(1+s)^(-1)=(1-eta v)^(-1).            (4.4)

These are the bridge note's full three-dimensional framing
coordinates; r remains present and is not confused with the
two-dimensional meridian leaf. Their Jacobian is

    d eta wedge dv wedge db
                      =-dr wedge ds wedge dp/(s p).

It follows exactly that

    Omega_cut wedge dLog p
       =A_cut H_G
       =-(d eta/eta) wedge dv wedge da/(1-eta v).          (4.5)

The missing Haar adapter is A_cut in the interior. Its restriction
to E_exc is one, so the residue is fixed, not guessed from weights.

For any nondegenerate geometric critical representation satisfying
the general density theorem, retain its original square-root phase
and set c_beta^2=-T_beta/2. The torsion T_beta is nonzero and is
constant along this conjugation torsor. Hence the actual principal
Gaussian density has Omega_beta=c_beta Omega_cut on that marked
line. Equation (4.5) proves

    (1/(2pi*i))Res_(E_exc)
              (Omega_beta wedge dLog p)=c_beta omega_I.   (4.6)

Its compact period is c_beta!=0. This is a global nonzero leading
geometric logarithmic-residue class for an arbitrary such knot
braid. It strengthens nonzero local Gaussian density to a global
class on the actual compact source domain. The co-source dLog p
and the phase line in (4.6) are part of the assertion.
Here the domain identification is the canonical isomorphism
E_exc=X. It is not an assertion that the physical compact cycle
has already been pushed onto this exceptional divisor.
The original base-only quantum normalization line is tensored through
unchanged. No isolated compact factorial or full modified-dimension
factor is evaluated at a root or removed by this variable-density
calculation.

This does not yet state that the whole actual quantum network
pushes its selected source to (4.6). In particular Green currents
can contain Log eta. Once that coordinate is admitted without its
relative endpoint data, d eta/eta is exact and an absolute argument
can erase the residue. The actual relative source/current complex
must be carried through this boundary construction; a nonzero
principal residue is not itself the global selected-period theorem.

## 5. Source and Gaussian line weights are distinct and explicit

Let h(alpha)=diag(alpha,alpha^(-1)). At the north and south fixed
flags the tautological O(-1) fibers have characters alpha and
alpha^(-1), respectively, meaning weights +1,-1. The relevant
integer weights are therefore

| Line | North weight | South weight |
|---|---:|---:|
| tautological O(-1) | +1 | -1 |
| nilpotent normal O(-2) | +2 | -2 |
| ordinary K_Y=O(2) | -2 | +2 |
| ordinary half-canonical K_Y^(1/2)=O(1) | -1 | +1 |
| logarithmic K_Y(E_exc) | 0 | 0 |
| logarithmic half-canonical line, on its sign mark | 0 | 0 |
| prequantum O(N) | -N | +N |
| polarized half-form K_P1^(1/2)=O(-1) | +1 | -1 |
| actual coherent wave line O(N-1) | -(N-1) | +(N-1) |
| geometric torsion/Gaussian ratio c_beta | 0 | 0 |

The half-form identity is the exact intrinsic source identity

    H_N=H^0(P1,O(N-1))
       =H^0(P1,O(N) tensor K_P1^(1/2)).                    (5.1)

The determinant-line accounting is also compatible with square
roots: the ordinary half-canonical character and half-normal divisor
character cancel on a compatible logarithmic half-density line.
The actual density theorem fixes the weight-zero ratio c_beta after
the original cut-density factors have been combined. It does not
identify a separately normalized transverse Gaussian with K_Y^(1/2)
alone. These line statements retain the original square-root phases
and do not equate ordinary coherent clutch with quantum dressing.

The coherent vector line is the dual O(-(N-1)); its coefficient
wave line is O(N-1). Their distinction avoids a sign ambiguity in
the table. Pairing the actual source and co-source and retaining
the incidence denominator gives the globally defined compact
kernel, whose normalized trace period is already exact.

There is a useful representation-theoretic check of the boundary
weight. On the SL2 sign cover, (3.3) lifts as eta^(-1/2)g, so for
n=N-1,

    Sym^n(g_SL2)=eta^(-n/2)Sym^n(g).                       (5.2)

Its leading coefficient is the rank-one coherent operator of the
two boundary flags. At v=a=0 the eigenvalues are eta^(1/2),
eta^(-1/2), and the powers are eta^((n-2j)/2). This yields precisely
the source normal pole and torus weight in the table. For odd n
the single source requires its SL2 sign mark; the End kernel and
paired compact period descend to PGL2 for every N.

Equation (5.2) is the standard polynomial coherent-line clutch.
It is not proved here to be the actual unrestricted quantum-group
dressing of a physical Gauss frame. Ordinary SL2 Möbius action
on coherent coordinates and the actual quantum dressing are
different constructions until a source-preserving network map
has been supplied. The exact actual result in this note is (4.6),
which uses the independently checked physical diagonal gauge and
principal Gaussian density, not this unproved identification.

## 6. Physical-symbol and residue sections remain separately marked

The compact source also has the physical map of Section 1. Under
the actual bridge coordinates it is reached by the logarithmic
centralizer section

    r_*(A)=1-Log A/(2pi*i),
    a=p(1-r_*)=p Log A/(2pi*i).                           (6.1)

The mark at the north pole is r_*=1 and that at the south pole
is r_*=0. A logarithm deck shift changes r_* by -1 and its old
frame coordinate b=(1-r)/s by +1/s; the relative comparison
coordinate (r_*-r)/s has the opposite jump. Thus the global
source needs the logarithmic transition, not a single split B1
section. The r,s,p note retains its boundary primitive and sign.

The associated boundary coordinate T=va=1-r and the physical
symbol coordinate Log A/(2pi*i) agree on the marked section (6.1).
They are not identical functions on the full three-dimensional
framing family. In particular taking an arbitrary framing section
or identifying the old two B1 coordinates with the two compact
leaf coordinates would change the comparison.

More precisely the physical section is the graph
eta=(1-exp(-2pi*i va))/v inside Y; eta on Y is otherwise independent.
This graph meets E_exc at the analytic identity locus, not along all
of X. For finite v!=0 that locus has va in Z; at v=0 its removable
condition is a=0. On the real compact sphere only the two poles
occur. Therefore the nonzero residue class on E_exc is not yet
the image of the actual physical compact-cycle pairing. A relative
cycle or source-chain comparison is still necessary.

Equivariant descent supplies the global principal class (4.6)
and fixes its line weights. It does not fix the scalar of a whole
actual quantum source or ensure that unrestricted logarithmic
Green transgressions preserve that class. The remaining operation
is a marked relative pushforward with the actual source, caps,
Weyl transitions and normal jets retained, rather than another
choice of a local geometric optimum.

The [exact universal audit](../experiments/audit_springer_centralizer_boundary_source.py)
checks the matrix transitions, compact flag and form maps, actual
Gaussian adapter, normal weights and coherent rank-one boundary.
The [independent resolved-boundary audit](resolved_framing_boundary_independent_audit.md)
also verifies the centralizer nonextension, matrix compactification,
line bundles and principal Gaussian residue with the physical-cycle
and quantum-dressing qualifications retained.
The [independent global boundary audit](resolved_framing_boundary_independent_audit.md)
checks the torsor obstruction, compactification, exact Haar adapter
and marked principal residue, including its selected-cycle limitation.
