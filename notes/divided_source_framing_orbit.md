# A divided-normal source orbit and the canonical framing form

Research proof, 27 October 2026. The actual divided Hopf adjoints
contain a two-dimensional standard SL2 module. Its cut Borel orbit
is an explicit sign cover of the classical framing torsor, with
the correct canonical two-form and leading co-source covariance.
The same normal matrices admit a concrete clock/shift realization
and a regular diagonal comparison with the actual cyclic source.

These are algebraic source, group, and density maps. They do not
identify this source orbit with the two internal critical framing
coordinates of the knot network. The exact loss of information
after a normalized cut is computed below, rather than suppressed.

The later [unprojectivized high-color source theorem](actual_unprojectivized_frobenius_borel_torsor.md)
realizes a marked Borel torsor using ACTUAL Sym^N divided source
vectors and their contragredient co-source. Retaining scale U and
one actual descendant m gives Omega_cut=(A/N)dlog U wedge dm;
an actual old-clock normal row detects that scale. This retains
the prequantum character erased by a normalized projector. It
does not infer the full network-current comparison from the
standard group/density formulas already proved here.

## 1. The actual standard module and its cut covector

At complete color fix N>=2, Q=q_N^2, and the original balanced
space V_N. Let

    W=E_(N-1,0), U=sum_(j=0)^(N-2) E_(j,j+1), Ubar=U/(N-1).

The [complete divided-Ward theorem](complete_color_divided_ward_and_fusion.md)
proves for the true divided Hopf adjoints J_E,J_F that

    J_E(W)=-N U, J_E(U)=0,
    J_F(U)=N W, J_F(W)=0.

Consequently on L=span(Ubar,W), the operators

    e_sl=-J_E/[N(N-1)], f_sl=(N-1)J_F/N,
    h_sl=[e_sl,f_sl]

are exactly the standard two-dimensional SL2 Lie matrices in the
ordered basis (Ubar,W). This action exponentiates algebraically
on L. It is an action on the **linear source space**: the divided
Hopf coproduct has mixed terms, so no action by automorphisms of
the full matrix multiplication algebra is inferred.

For the actual cut Phi(C)=Tr(e C), e_ij=1/N, one has

    Phi(Ubar)=Phi(W)=1/N.

Thus the restricted cut covector is phi=(1,1)/N. Let G_phi be
the SL2 Borel preserving its projective line. For

    v=a Ubar+b W, z=a+b!=0,

there is a unique g in G_phi with gW=v. In these source coordinates
it is

    g_v=[[a+1/z,a],[b-1/z,b]],
    det(g_v)=1, phi g_v=z phi.                 (1)

This proves directly that the open source orbit z!=0 is a genuine
G_phi torsor with anchor W, not merely a dimension count.

## 2. An equivariant sign cover of the geometric B1 framing torsor

Let j(g)=z(g)g^(-T), where phi g=z(g)phi. It has row sums one
and determinant z(g)^2. Since z is a character, j is a group
homomorphism. Its kernel is {I,-I}; it is the usual sign cover
of the row-stochastic PGL2 cut Borel, with the sign retained.

Take F_0=[[0,1],[1,-1]] and define

    F(v)=F_0 j(g_v)^(-1)
        =[[r,1-r],[s,-s]],
    r=a/z, s=z^(-2).                            (2)

Every regular framing matrix of this form has two lifts, related
by v->-v. Source left translation g_0 sends

    F(v) -> F(v) j(g_0)^(-1).

Thus (2) has exactly the established right-frame action convention;
replacing j(g)^(-1) by j(g) would reverse it.

Pull back the canonical complete framing two-form and cut coordinate:

    Omega_cut=-dr wedge ds/[s(1+s)],
    A_cut=1/(1+s).

On the open set 1+z^2!=0 their exact source expressions are

    Omega_src=2 da wedge db/(1+z^2),
    A_src=z^2/(1+z^2).                          (3)

Indeed dr wedge ds=-2 z^(-4) da wedge db, and
s(1+s)=(1+z^2)z^(-4). No determinant or sign is omitted.

For the two geometric cut stabilizers
xi_1=h+2f, xi_2=e+f, the corresponding source matrices are
-xi_i^T. Their vector fields are

    X_1=(-a-2b)partial_a+b partial_b,
    X_2=-b partial_a-a partial_b.

Both satisfy X_i(z)=-z and

    div_(Omega_src) X_i=2 A_src.                (4)

Their images under (2) are exactly the two compensated geometric
fields in [the residual Ward proof](residual_gaussian_ward_currents.md).
Equation (4) is the same leading covariance as the actual cut
co-source b_i/H=-2 A_cut. This is an explicit source-level
density comparison with its fixed group convention.
The divided action on L and the ordinary finite Ward action on
the network are distinct actions. Equation (4) does not by itself
intertwine them or identify their internal source coordinates.

## 3. The relative centralizer coordinate and its transgression

The geometric additive centralizer coordinate is

    tau=r/s=a z.

The source vector field

    V=z^(-1)(partial_a-partial_b)

has V(tau)=1 and V(A_src)=0. Direct contraction gives

    iota_V Omega_src=dlog A_src,
    Omega_src=dtau wedge dlog A_src.            (5)

Therefore the marked interval tau=0,...,1 transgresses the source
form to exactly the canonical logarithmic cut form. Translating
both endpoints by a regular function tau_0(A_src) changes neither
this two-form nor that relative class. Poles of such a section
require their marked boundary lattice; (5) does not delete them.

This gives a concrete classical source orbit for the same relative
framing complex. To make it the **network's** source comparison,
the actual boundary currents must still be sent to its endpoint
and logarithmic-carry co-sources. The
[full-certificate calculation](full_certificate_framing_boundary.md)
states those unresolved currents explicitly.

## 4. The orbit matrix is an actual cyclic quantum-torus generator

Put c=a/(N-1). In the original finite matrix algebra,

    v=c U+b W,
    K v=Q v K,
    v^N=b c^(N-1) I.                           (6)

The last identity follows by following one complete cyclic string.
For a b!=0, v and the clock K give the split cyclic torus, not
only an abstract two-dimensional representation.

There is an explicit regular diagonal comparison with the actual
E-cyclic source from [the coherent crossing proof](balanced_verma_coherent_braiding.md).
At M=1 write epsilon_j=Q^(-j)-1, P_j=product_(l=1)^j epsilon_l,
P_0=1. Every P_j, j<N, is nonzero and P_(N-1)=(-1)^(N-1)N.
Set

    mu=b c^(N-1)/P_(N-1),
    D_jj=P_j/c^j.

Then D commutes with K and direct arrow comparison gives

    D(Ecal_head+mu W)D^(-1)=v.                  (7)

The transformed F is fixed by the original Casimir:

    Ftilde=(-2-qK-q^(-1)K^(-1))v^(-1),
    Ftilde^N=0.                                (8)

Thus the orbit has a rational matrix gauge into a genuine actual
source family. This does not assert that its G_phi action preserves
matrix multiplication or the knot's entire intertwiner network.
The source coordinate A_src in (3) is still a parameter function;
it has not been identified with the physical clock x/K by (6).

## 5. The original cut has an exact marked cyclic anchor

For z!=0 define the normalized matrix coupon

    e_v=(N/z) v e.

It has rank one, trace one and e_v^2=e_v, since e v e=(z/N)e.
Its entries are explicit:

    (e_v)_ij=r/(N-1), i<N-1,
    (e_v)_(N-1,j)=1-r, r=a/z.                  (9)

The **whole coupon**, not only its diagonal restriction, loses
the scale z. Its row Phi_v(C)=Tr(e_v C) is cohomologous to the
original normalized cut on the actual split Ward complex, by
(Phi_v-Phi)h delta=Phi_v-Phi. On closed scalar cut operators it
therefore returns exactly the original invariant.

At r_*=(N-1)/N, equation (9) is literally e_v=e on all matrices.
Retaining the shift and its eigenvalue mark fixes the scale as
well: the actual point

    v_*=(N-1)Ubar+W=U+W=S,
    S^N=I, S e=e, e=(1/N)sum_(j=0)^(N-1)S^j      (10)

is the original cyclic shift and selected eigenprojector. It has
a_*=N-1,b_*=1,z_*=N. Its image in (2)--(3) is the exact source
orbit section

    r_*=1-1/N, s_*=1/N^2,
    A_*=N^2/(N^2+1), tau_*=N(N-1).             (11)

The companion gauge (7) has c=1 and mu=1/[(-1)^(N-1)N] there.
Thus the original cut has an intrinsic cyclic-source anchor; it
is not fixed by normalized coupon data alone. Equation (11)
approaches a framing boundary as N grows. It is a section of the
constructed source orbit, not yet a proof that the network's
geometric period is evaluated at that same section.

There is a second exact restriction. For any diagonal cut array,

    Phi_v(C)=r sum_(j<N-1)C_jj/(N-1)+(1-r)C_(N-1,N-1).        (12)

Every actual uninserted one-cut array is diagonal before its final
internal sums. Hence (12) probes only one strand-index weight;
the two orbit parameters do not themselves create two internal
flow coordinates. The divided-adjoint cut is likewise precisely
the endpoint functional on these arrays, as proved in the
full-certificate note. A pre-collapse source-current map remains
necessary.

## 6. The logarithmic normal comparison has a separate scale

The [strict Fock-to-normal comparison](fock_cyclic_normal_mellin_map.md)
retains resonant U^k sectors and the relative endpoint U, on the
marked logarithmic torsor. The bare geometric pullback here is

    u=Log U=N Log A_src,
    Omega_cut=(1/N)dtau_geo wedge du.

It does not identify the Fock coherent parameter with tau_geo.
At the physical H_N=2pi*i/N, a putative canonical phase
tau_geo Log A/H_N is tau_geo u/(2pi*i), whereas the exact
source kernel is exp(s_Fock u). Matching them would rescale the
endpoint and change U to U^(1/(2pi*i)); that adapter has not
been established. The exact orbit and density identities above
do not permit discarding this marked factor.

The source orbit, clock gauge, cyclic anchor, and leading density
are now explicit. The selected internal framing map, endpoint
and carry cancellation for the full scalar certificate, and the
regulator norm are still unproved. No volume limit follows here.

[Exact symbolic and actual-matrix audit](../experiments/audit_divided_source_framing_orbit.py).
[Results](../experiments/divided_source_framing_orbit_results.json).
[Independent proof audit](divided_source_framing_orbit_independent_audit.md).
