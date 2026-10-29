# The actual framing, its compact-source logarithmic section, and its boundary residue

Research proof, 27 October 2026. This computes the missing common
momentum gauge between the actual critical framing and the compact
coherent source. The physical meridian map resolves holomorphically
at both compact poles after retaining its eigenflag. The full
irreducible knot family nevertheless cannot extend there as regular
matrices. An explicit associated-frame Jacobian gives a nonzero
principal Gaussian boundary residue on the actual compact source.

These are complete-parabolic statements, with the original base and
half-density lines retained. No extension of higher Gaussian loops,
selected-cycle equality, or volume limit is inferred.

## 1. Common momentum is an exact diagonal gauge

In the actual finite head let

    S_c e_a=c^(-a)e_a.

Then exactly `S_c Ecal S_c^(-1)=c Ecal`,
`S_c F S_c^(-1)=c^(-1)F`, and K is unchanged. A common scaling
on all strands is a Hopf automorphism. Every weighted crossing
preserves the integer total index, hence commutes with
`S_c^(tensor b)`. Its closed diagonal cut has the same property.

For the actual compact coherent kernel, direct substitution gives

    sigma_(S_c C S_c^(-1))(w,z)=sigma_C(w/c,c z).

Thus the exact diagonal gauge preserves

    t_c=wz/(1+wz),

and scales the physical momentum `p=1/w` by c. For unit c it
preserves the compact real source cycle; its angle is the exact
common diagonal gauge angle. In particular the compact angular
coordinate does not automatically replace the internal geometric
centralizer coordinate.

The actual critical model has inverse cut flag `p_1=1`. Write its
framing, at M=1, as

    F(r,s)=[r,1-r;s,-s], s!=0,
    mu_s=F^(-1)[1,1;0,1]F=[1+s,-s;s,1-s].

Adding the common momentum gives the genuine third framing
coordinate

    D_p=diag(p,1), Ftilde=F D_p^(-1),
    mu(A,p)=D_p mu_s D_p^(-1)
       =[1+s,-sp;s/p,1-s], A=(1+s)^(-1).          (1)

The SL2 lift uses the marked square root of p; the displayed
conjugation is projective and changes no gauge-invariant shape.
For generic M the identical construction uses the already proved
`F_M(r,s)` and `A=M/(M+s)`. The complete-pole conclusions below
are restricted to M=1, where the actual kappa vacuum term vanishes.

The physical compact-source coordinates of (1) are explicitly

    t_c=Log A/(2pi*i), w=1/p,
    z=p t_c/(1-t_c).                            (2)

They forget r. On the original `p_1=1` framing, their image has
`w=1` and rank one. Therefore there is no meridian- and
momentum-preserving identification of the two original internal
framing coordinates with the whole compact source. The common
momentum gauge must first be restored, and the remaining
centralizer direction must be treated separately.

## 2. An explicit Springer map at both compact poles

Use the compact-source chart

    v=w, a=z/(1+wz), t_c=v a,

and put `c_0=2pi*i`. The physical meridian minus identity is

    mu-I=eta_S[-v,1;-v^2,v],
    eta_S=(1-exp(-c_0 v a))/v.                  (3)

Its eigenflag is `(1,v)`. Division by v is removable: the right
side is an entire function of v,a. Moreover

    partial_a eta_S=c_0 exp(-c_0 v a)!=0.

Thus this is an explicit holomorphic local isomorphism to the
resolved parabolic Gauss chart, rather than a claim obtained by
equating symplectic forms.

On the second compact chart set

    v'=1/v, a'=v-v^2 a, t_c'=v'a'=1-t_c.

Then

    eta_S'=-v^2 eta_S
           =(exp(c_0 v'a')-1)/v'.              (4)

This extends at `v'=0` with derivative `c_0` in `a'`. Equations
(3)--(4) are precisely the two Springer/eigenflag transition
formulas. At the south compact pole `(w,z)=(0,0)`, one has
`eta_S=c_0 z+...`; at the north pole in `W=1/w,Z=1/z`, the
corresponding normal is `c_0 Z+...`. Both meridians become identity,
but their limiting eigenflags are retained.

The marked inverse is rational/logarithmic:

    A=(1-eta_S v)^(-1),
    a=Log A/(c_0 v).                            (5)

It extends at v=0 by `a=eta_S/c_0`. Other logarithm sheets are
not identified. This local isomorphism need not be a proper
global covering; other logarithmic sheets can escape a chart.

The resolved Gauss form can now be checked from the map itself:

    dLog A wedge dLog p
      =-d eta_S wedge dv/(1-eta_S v)
      =c_0 dv wedge da.                        (6)

This recovers the physical compact-source form with its sign and
normalization, including at the two pole charts.

## 3. The actual logarithmic centralizer section

The PGL2 conjugator from the reference meridian to (1) is
`G=Ftilde^(-1)`. In the Springer chart write

    g_N=[1,0;v,eta_S^(-1)],
    n(b)=[1,b;0,1].

Direct matrix multiplication shows that G is projectively
`g_N n(b)` with

    v=1/p, eta_S=-s p, b=(1-r)/s.               (7)

The renormalized associated-frame coordinate is

    a_B=-eta_S b=p(1-r).

Its opposite-chart transition is `a_B'=v-v^2 a_B`, exactly the
compact-source transition. Its associated compact radial coordinate
is `v a_B=1-r`. This is initially different from the physical
coordinate `Log A/c_0` in (2).

They agree on one explicitly determined logarithmic centralizer
section:

    r_*(s)=1-Log A/c_0=1+Log(1+s)/c_0.           (8)

Any actual frame reaches this section by the original centralizer
action `r->r+b s`, with

    b=(r_*(s)-r)/s.

This is the explicit gauge/eigenflag transport; all developed
cross-ratios and knot character functions stay constant. The
common diagonal momentum p is a separate gauge from this
centralizer normalization.

On the physical compact path `A=exp(c_0 t_c)`, the section is
`r_*=1-t_c`. It tends to r=1 at the south pole and r=0 at the
north pole. After one marked A loop,

    Log A -> Log A+c_0, r_* -> r_*-1.

The centralizer transition is consequently `b=-1/s`. Its primitive
co-source changes by

    -(1/s)dLog A=ds/[s(1+s)].                   (9)

Its residue at s=0 is exactly +1, and at s=-1 it is -1. This
is a nonzero boundary source forced by the actual logarithmic
section, with its deck orientation specified. A finite algebraic
cover cannot make the logarithm single valued: it multiplies,
rather than removes, its nonzero residue.

## 4. The full irreducible knot family must escape the collapsed meridian

Resolving one meridian does not regularize the entire knot
representation. Normalize its meridian to
`mu_0=[1,1;0,1]`. Irreducibility supplies a group word with

    rho(g)=[A_0,B_0;C_0,D_0], C_0!=0.

Otherwise every group matrix would preserve the meridian's unique
eigenline. Direct multiplication gives the conjugacy invariant

    Tr[mu_0,rho(g)]=2+C_0^2!=2.                (10)

If every conjugated group matrix extended regularly while the
physical compact meridian tends to identity, this commutator
would tend to identity and its trace to two, contradicting (10).
Therefore some other holonomy necessarily has a pole. A single
Springer flag cannot eliminate this full-family escape.

The pole can be seen explicitly. On the r=1 section, the conjugate
of the displayed group matrix is

    [A_0+B_0s, -B_0sp;
     (A_0-D_0+B_0s-C_0/s)/p, D_0-B_0s].

It has a south-pole term `-C_0/(s p)`. On the r=0 section the
conjugate is

    [D_0+B_0s, p(A_0-D_0-B_0s+C_0/s);
     B_0s/p, A_0-B_0s],

with north-pole term `C_0p/s`. Along the compact real cycle these
are respectively of order `t_c^(-1/2)` and
`(1-t_c)^(-1/2)`, with nonzero coefficients. These sections are
the limits of the canonical logarithmic section (8).
Projective developed flags may still have limits, but their
coincidences and normal directions require more data than an
ordinary regular matrix representation at the pole.

## 5. The principal Gaussian has an exact compact boundary residue

Retain the actual marked cut form and covector

    Omega_cut=-dr wedge ds/[s(1+s)], lambda_flag=dLog p.

The normalization of the covector is fixed by the exact diagonal
gauge in Section 1: it takes value one on its common logarithmic
momentum generator. It has not been selected by guessing a Haar
volume. In the coordinates (7), direct differentiation gives

    d eta_S wedge dv wedge db
                     =-dr wedge ds wedge dp/(s p).

Consequently the exact full-form identity is

    Omega_cut wedge dLog p
      =A_cut d eta_S wedge dv wedge db
      =-(d eta_S/eta_S) wedge dv wedge da_B
                                            /(1-eta_S v).   (11)

The interior Haar adapter is `A_cut=(1+s)^(-1)`; it cannot be
omitted away from the boundary. It is one at `eta_S=0`, so (11)
has the canonical logarithmic residue

    Res_(eta_S=0)(Omega_cut wedge dLog p)=-dv wedge da_B.      (12)

With the actual compact trace form

    omega_I=-dv wedge da_B/(2pi*i), integral_Gamma omega_I=1,

equation (12) is a nonzero global compact-source class.
The algebraic associated-frame transition makes this statement
independent of the two charts.

The uniform Gaussian comparison gives, on its recorded square-root
and base-line cover,

    Omega_(beta,0)=c_beta Omega_cut,
    c_beta^2=-T_beta/2, c_beta!=0.

Here the common original base-only line is factored but retained;
it tensors both sides back into their original normalization.
Since c_beta is conjugation invariant, (11)--(12) imply

    (1/(2pi*i))Res_(eta_S=0)
           [Omega_(beta,0) wedge lambda_flag]=c_beta omega_I. (13)

Thus the normalized **principal boundary form** has actual compact
period c_beta, with the original half-density phase retained.
This is a computed residue, not an assumption that the critical
family has a proper interior limit. Real gauge-circle orientation
and normal-residue orientation must be transported as specified;
they are not reset by taking an absolute norm.

## 6. Exact scope

The physical compact meridian map, the actual common-momentum
gauge, the logarithmic centralizer section, and the principal
boundary residue have now been computed from the actual frames.
The original fixed-cut-flag two-dimensional torsor is not simply
the compact coadjoint leaf: restoring momentum adds a third
dimension, and the internal centralizer remains a separate fiber.

The associated boundary and the physical section must be kept
distinct. In the associated-frame threefold, `eta_S=0` is an
independent divisor over the entire compact algebraic source X.
On the physical logarithmic section, however, (3) imposes
`eta_S=(1-exp(-2pi*i*v*a_B))/v`. At finite nonzero v, that section
meets the divisor precisely where `v*a_B` is integral; at v=0 the
removable formula instead requires `a_B=0`. On the real compact source with
`0<=t_c<=1` these are its two endpoint poles. In particular the
compact cycle in the residue divisor has not been proved to be
the geometric pushforward of the original physical compact cycle.

Equation (13) proves nonzero leading boundary cohomology. It does
not show that every higher Gaussian coefficient has only the same
logarithmic pole, that all developed-flag degenerations are resolved,
or that the actual full Green currents map to this boundary class
with no additional contribution. Equation (10) shows that full
critical-family escape is a real issue, not a hypothetical warning.
The global geometric pushforward preserving the compact current
period, and the selected volume growth, remain unproved.

## 7. Audit and dependencies

The exact symbolic checks in
[audit_compact_framing_gauge_boundary.py](../experiments/audit_compact_framing_gauge_boundary.py)
and its
[results](../experiments/compact_framing_gauge_boundary_results.json)
verify the finite coherent gauge at levels 2 through 5, the full
frame conjugation and Jacobian, both physical Springer charts,
the logarithmic residue, both unavoidable escape poles, and the
principal Gaussian boundary-form coefficient. The displayed
calculations are universal rational or entire-function identities;
the finite levels only audit the coherent-coordinate convention.

The principal determinant normalization is the one proved in
[the uniform Gaussian comparison](quantum_source_bridge_extension.md),
and the finite trace form and physical whole-clock limit are those
in [the actual compact source](compact_coherent_source_period.md).
The global associated-bundle construction and its normalization
lines are developed separately in
[the Springer boundary-source note](springer_centralizer_boundary_source.md).
The [independent joint audit](resolved_framing_boundary_independent_audit.md)
also checks the logarithmic deck signs, pole escape and principal
residue normalization.
