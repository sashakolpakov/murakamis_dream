# The whole original Fermat source as a toric residue, with its wire seams

28 October 2026. The exact balanced Fourier crossing theorem gives a
single scalar period for the original complete knot source. Its
co-source is an explicit rational function of bounded degree on the
finite Fermat grids. This note computes its root-grid Jacobian and the
different Jacobian of a wire-pole pushforward.

The latter has coefficient one, but its other relative currents need
not vanish. In fact an exact local calculation shows that sewing a
balanced full-Psi block off its original central grid REGENERATES the
beta/Rogers current. Thus the residue formula does not by itself
identify the original period with a positive geometric cycle.

All frame changes below are reversible finite changes of basis. All
original cups, ordinary caps, the FULL marked row, pivots and external
scalar lines are retained. The proofs use the exact crossing theorem,
not a new invariant or a favorable source.

## 1. Exact bounded-degree rational co-source

Put N>=2, d=N-1, Q=exp(2*pi*i/N), x=-exp(-pi*i/N), and
s=x^N=(-1)^(N+1). On a port with central coordinate C choose a marked
root r^N=C and the finite grid z=r Q^k. The normalized frame is

    F(r)_(k,a)=z^a/sqrt(N),
    F(r)^(-1)_(a,k)=z^(-a)/sqrt(N),  0<=a,k<N.       (1)

The [exact balanced crossing](actual_balanced_fourier_crossing_kernel.md)
and its complete antiunitary mirror apply independently at every
signed crossing. Join their ports with the actual frame adapters.
No matching of distinct central grids is implicit.

Let K_N(t)=sum_(a=0)^d t^a. For an output port x0^N=C and the next
input y^N=D the adapter is exactly

    E(y,x0)=[1-D/C]/[N(1-y/x0)].                    (2)

The pivot on the actual oriented head is
g_a=x^(1-N)Q^(-a)=(x/s)Q^(-a), so its adapter is

    E_g(y,x0)=(x/s)[1-D/C]/[N(1-Q^(-1)y/x0)].       (3)

At a removable collision the original finite K_N is understood. The
unpivoted first trace, where present, has its original external
normalization; it is not absorbed into (3).

For completeness, use the actual physical pair sources proved in
[the coupled-cap theorem](actual_coupled_caps_interval_source.md):

    p(a,b)=N x^(a-d) delta_(a+b,d),
    m(a,b)=N^(-1)(x^(-1)Q^(-1))^a delta_(a+b,d),
    m_mark(a,b)=x^b/N^2,  ALL 0<=a,b<N.             (4)

If z_i^N=C_i, their transformed entries are the following exact
rational functions ON THE GRIDS:

    (F_1 tensor F_2)p
       =(x/s)(C_2-s C_1)/(z_2-x z_1),

    m(F_1^(-1) tensor F_2^(-1))
       =z_1 z_2(C_1-s C_2)
          /[N^2 C_1 C_2(z_1-x^(-1)Q^(-1)z_2)],

    m_mark(F_1^(-1) tensor F_2^(-1))
       =z_1 z_2(C_1-1)(C_2-s)
          /[N^3 C_1 C_2(z_1-1)(z_2-x)].           (5)

In particular the marked source in (5) is the FULL row in (4), not
its restriction to an invariant fiber after some decomposition.
The first two formulas follow from K_N and z_i^d=C_i/z_i.
The marked row gives N^(-3)K_N(z_1^(-1))K_N(x/z_2), which gives
the last formula. These computations fix every N and Q factor.

For a fixed diagram the product of (2), (3), (5) is therefore a
rational function of degree bounded independently of N, after its
explicit powers of N and the actual unit phases are separated.
The central parameters are fixed nonzero constants. On the generic
source chart require the corresponding numerator differences in
(2), (5) to be nonzero. This is a finite list of proper algebraic
conditions and can be arranged by the independent local frames.
One may insert another reversible frame on a wire if needed; the
added grid variable and BOTH adapters are then retained.

On compact subsets of this generic central chart, each entry of this
rational source and its reciprocal has at most polynomial size in N.
Indeed the moduli of all marked Nth roots are uniformly bounded above
and below, each numerator difference stays nonzero, and

    |1-y/x0| >= c/N  if C!=D,

and likewise for the shifted denominators in (5). To see the last
bound, use (1-t^N)/(1-t)=sum_(a=0)^d t^a and the fixed nonzero
central numerator. The elementary upper bound on this sum is O(N)
because |t|^N is fixed. Thus no exponential source gauge is hidden
in this initial regular chart. An ambient rational unit is not a
geometric thimble coefficient.

## 2. The exact single toric residue of the whole source

Expand the complete transformed word, including (5), as its finite
sum over all port labels. Write it as

    P_N=chi_N sum_(z_i^N=C_i, all i) H_N(z) A_N(z).   (6)

Here H_N is the product of the exact signed four-full-Psi crossing
entries (including their Gaussian and actual local constants);
A_N is the rational co-source from Section 1. The external original
line chi_N is unchanged. No new normalization of the sum is used.

Let f_i=z_i^N-C_i. The coordinate algebra

    T_N=C[z_1^(+/-1),...,z_n^(+/-1)]/(f_1,...,f_n)

is finite etale. Its source is the actual finite trace in (6), not a
postulated trace on a geometric critical algebra. At a grid point

    det(d f_i/d z_j)=N^n product_i z_i^(N-1).        (7)

Choose the continued local full-Psi germs which give the specified
grid entries. With coordinate order fixed as dz_1 wedge ... wedge dz_n,
the exact period is

    P_N=chi_N Res_(all f_i=0)
       H_N(z) A_N(z)
       product_i [N z_i^(N-1) dz_i/(z_i^N-C_i)].    (8)

The normalized residue is the sum of the local product-circle
integrals divided by (2*pi*i)^n. Every grid point has coefficient
ONE, by (7). The same statement holds with N C_i/z_i in place of
N z_i^(N-1); these numerators agree on the grid. Such a change of
off-grid extension need not preserve individual zero/infinity
boundary terms during a later contour deformation.

Equation (8) is a specified original cycle and a single period. It
does not turn the grid algebra into the classical gluing algebra.
Different off-grid holomorphic extensions with the same grid values
have the same small residues and can have different critical schemes.
Any proposed deformation to a geometric shape cycle must therefore
transport the whole form, source and relative boundaries, not just
its sampled values.

## 3. Wire-pole pushforward and its exact Jacobian

Keep one wire with x0^N=C, y^N=D, C!=D. Let f(x0) denote the
complete remaining local field, with its actual logarithmic marks.
Its Fourier interpolation is

    I_(C->D) f(y)
       =sum_(x0^N=C) [1-D/C]/[N(1-y/x0)] f(x0)
       =sum_(x0^N=C) Res_x0 omega,

    omega=(C-D)f(x0) dx0/[(x0^N-C)(x0-y)].          (9)

The grid residue in (9) is (2) times f. The DISTINCT wire collision
pole x0=y has

    Res_(x0=y) omega=-f(y).                         (10)

Thus pushing the grid contours across the collision gives a
coefficient-one substitution x0=y. No color, Gaussian or root
Jacobian is missing. It is a different residue calculation from (7).

More precisely, on any marked branch domain U containing the grid
points and y, with all additional poles and branch lips retained,
the residue theorem gives

    I_(C->D) f(y)
       =f(y)+(1/(2*pi*i)) integral_(boundary U) omega
                    -sum_(other poles in U) Res omega.   (11)

The boundary includes the logarithmic cut lips and any zero/infinity
or endpoint circles needed to specify that branch domain. There is
no assumption that they vanish. If f is a polynomial of degree<N,
one can take U approaching the sphere, the integral at infinity
vanishes, and (11) is ordinary polynomial interpolation. For a full
function these hypotheses generally fail.

For a collection of wire edges whose undirected graph is a forest,
successive collision residues eliminate one variable at a time with
the same coefficient one. Retain one variable in each component;
with leaf-first orientation their coordinate incidence matrix is
triangular with diagonal one. All non-wire branches in (11) are
still present. For an edge closing a cycle there is no additional
independent leaf variable; a closure condition or a remaining
residue has to be retained. In particular the forest calculation
does not dispose of the closed knot source.

## 4. Sewing recreates the exact original beta current

Fix v and choose the old central grid

    C=1+v^N, C!=0.

On that grid the EXACT original Newton source identity is

    B_N(x0,v)=S_N(x0,v),
    B_N(u,v)=S_N(u,v)+(1-u^N+v^N)I_N(u,v).          (12)

The functions and marks in (12) are those of
[the normalized beta source](actual_trivalent_quantum_beta_source.md).
Choose the grid germs by that identity, away from its exceptional
divisors. The polynomial B_N has degree<N in its first argument.
For y^N=D, its interpolation theorem and (12) therefore imply the
EXACT identity

    I_(C->D)[ S_N(.,v)|_(x0^N=C) ](y)
       =B_N(y,v)
       =S_N(y,v)+(C-D)I_N(y,v).                    (13)

Consequently the aggregate non-wire term in (11), for this source,
is exactly

    boundary integral - other-pole residues
                      =(C-D)I_N(y,v).             (14)

This is an identified beta source, rather than an unspecified
remainder defined by a putative global asymptotic. Its coefficient
is the difference between the two central wire parameters. The
current is generally nonzero; it is not killed by the old balance
C=1+v^N after y has moved off that grid.

The Rogers sink is identical in structure. On its old grid
C=1-v^N, use the independently proved

    R_N(u,v)=T_N(u,v)+(1-u^N-v^N)J_N(u,v).

Since R_N also has degree<N in u, the corresponding exact formula is

    I_(C->D)[ T_N(.,v)|_(x0^N=C) ](y)
       =R_N(y,v)=T_N(y,v)+(C-D)J_N(y,v).            (15)

It retains the opposite-root contour and the full norm of
[the Rogers source](actual_rogers_sink_opposite_beta_source.md).
Apparent C=D collisions are interpreted by the finite interpolation
and the continued complete source, not by dividing (14) by C-D.

Thus balancing the local blocks and then gluing by only the
collision residues is not in general an exact source operation.
The omitted seam is the original current in a different
polarization. Its exact logarithmic continuation can itself carry
a regular geometric sector, as proved in
[the current connection](actual_beta_current_connection_and_monodromy.md).
Neither its vanishing nor an exponential gap follows from local
balancing or from the unit residue (10).

## 5. Interior adapters and bulk logarithmic seams are different

The [propagated-frame theorem](propagated_balanced_frames_and_boundary_source.md)
makes every INTERIOR finite Fourier adapter the identity on an open
braid. Thus at most the braid width many nontrivial frame adapters
remain at its boundary. This exact statement does not imply that the
off-grid bulk full-Psi continuation has no logarithmic seams.

Here is an explicit sewn test, using the independently verified
[four-port characters](balanced_crossing_deck_characters.md). Sew two
positive crossings with central port data

    M_1=M(A,B,C,D), M_2=M(C,D,E,F).

The internal C and D variables have whole-product characters

    nu_C=-s E(A-C)/[D(C-E)],
    nu_D=-s B(F-D)/[C(D-B)].                        (16)

For example nu_C is mu_c of the first crossing times mu_a of the
second; C-sD=-s(D-sC) cancels the common local factor. No wire
adapter was introduced. After the propagated pair of crossings the
external centers return to their original values, so set E=A,F=B.
Then, as identities of the WHOLE bulk product away from divisors,

    nu_C=sA/D, nu_D=sB/C.                          (17)

These characters equal one on the original internal grids C=sB,
D=sA, but do not equal one during arbitrary off-grid motion. The
whole product has a bulk seam even though it has no interior
Fourier adapter.

This example also permits an exact, but limited, dual-character
residue transformation. Write c,d for the actual internal variables
and put

    f_c=c^N-sB, f_d=d^N-sA,
    G_c=nu_C-1=-f_d/d^N,
    G_d=nu_D-1=-f_c/c^N.                            (18)

The change from (f_c,f_d) to (G_c,G_d) is invertible near every
nonzero grid point. Its coefficient matrix and determinant are

    L=[[0,-d^(-N)],[-c^(-N),0]], det L=-(cd)^(-N).

Consequently the exact local Grothendieck transformation rule is

    Res_f H dc wedge dd/(f_c f_d)
       =Res_G H det(L) dc wedge dd/(G_c G_d).       (19)

At a grid point the two coordinate Jacobians are respectively
N^2 c^(N-1)d^(N-1) and -N^2/(cd). Their ratio is exactly det L,
including its sign; the residue contours use their respective
ordered defining functions. Thus (19) has no missing Jacobian.

But the zero sets in (18) are EXACTLY the same finite grid. This
calculation replaces its defining equations; it does not transform
the source to a different classical geometric cycle. In particular
nu_C=nu_D=1 pins the two internal centers at their original values
when A,B are fixed. Also, the first defect in (18) cancels the
OPPOSITE grid denominator f_d in a seam form. The resulting regular
current is not zero merely because its numerator vanished on the
grid. Formula (13) gives a fully normalized source example of that
same cancellation mechanism.

The source-deformation problem therefore includes both the remaining
boundary Fourier co-source and the bulk logarithmic seams of the
chosen off-grid continuation. Neither is removed by the telescoping
of interior finite changes of basis.

## 6. What is fixed and what is still required

Equations (5)--(8) give the entire original co-source and a single
finite etale residue period, without an exponentially unspecified
matrix source. Equations (9)--(15) compute what an actual wire-pole
pushforward adds. Iterated forest collision residues have exact
degree one, but the independent non-wire currents remain and can
be identified explicitly on the elementary trivalent blocks.

The remaining theorem is an actual deformation or exact regrouping
of this complete relative source onto the geometric shape cycle,
with its geometric coefficient proved nonzero and the other total
sectors controlled. A nonzero rational density on the grid, or a
unit collision Jacobian, does not prove that theorem. No volume
limit for a broad knot class is claimed here.

## 7. Reproducible audit

    python3 experiments/audit_whole_fermat_toric_residue_and_wire_source.py

The audit checks the normalized source table via its unnormalized
finite Fourier form (so every square-root normalization is explicit),
the original whole signed plat contraction, the toric Jacobians,
the wire/extra-pole residue identity, both exact current regeneration
identities using independent full-Psi evaluations, the sewn characters
(16)--(17), and the exact dual-character Jacobian in (19).
