# What a source saddle must prove for the Casson--Rivin maximum

29 October 2026. This is an independent implication audit. A saddle of
a reduced source does not, by itself, maximize volume on the full angle
polytope. There are two valid ways to bridge that gap: control every
missing tangent direction, or independently identify a full complex
gluing solution with the correct real peripheral constraints. The latter
is the mechanism used in the
[actual long-pretzel argument](actual_long_pretzel_casson_rivin_equality.md),
not an assumption that its source variables parametrize every angle.

## 1. The full tangent test, with a direct proof

For n positively oriented ideal tetrahedra use independent angle
coordinates (alpha_t,gamma_t), with beta_t=pi-alpha_t-gamma_t>0.
The corresponding shapes are uniquely fixed by the sine rule:

    z_t=exp(i alpha_t) sin(beta_t)/sin(gamma_t),
    z_t''=1-1/z_t.

Write r=(Re Log z_t,Re Log z_t'') and let
Omega=sum_t dx_t wedge dy_t on W=R^(2n). Direct differentiation gives,
for EVERY angle variation delta, whether or not it preserves complex
gluing,

    dV(delta)=Omega(r,delta),
    V=sum_t [Lambda(alpha_t)+Lambda(beta_t)+Lambda(gamma_t)].  (1)

Indeed Re Log z=log(sin beta/sin gamma) and
Re Log z''=log(sin alpha/sin beta); inserting
delta beta=-delta alpha-delta gamma proves (1) term by term.

The following are explicit linear-algebra hypotheses to check on the
ACTUAL marked triangulation. They are not consequences of a source
saddle or a dimension count:

* The edge Hamiltonian space E is isotropic, dim E=n-c.
* The edge-angle tangent space is E^perp.
* The peripheral map b:E^perp -> R^(2c), written (U,V), is onto,
  has kernel E, and satisfies

      Omega|_(E^perp)=b^*[-(1/2) sum_i dU_i wedge dV_i].     (2)

These identities can be checked from the marked edge and peripheral
matrices. The quotient rank and its kernel matter as much as the
pairing constant. Edge/peripheral logarithmic constants here have zero
real part; hence b(r) is exactly (Re U,Re V), with no omitted real
affine offset.

Choose a real rank-c matrix C=(A B) with AB^T=BA^T. The intended angle
slice fixes C(Im U,Im V)=kappa, in addition to tetrahedron and edge
angles. Its full tangent is

    T={delta in E^perp : C b(delta)=0}.                       (3)

**Full-slice criterion.** Suppose the positive shape point satisfies
the REAL edge equations, so r lies in E^perp. Then

    dV|_T=0  if and only if  A Re U+B Re V=0.                 (4)

Proof. L=ker C is Lagrangian in the 2c-dimensional peripheral space:
AB^T=BA^T makes the Hamiltonian row span isotropic, and its rank c
makes its symplectic orthogonal equal to itself. Surjectivity in (2)
gives b(T)=L. Equations (1)--(2) therefore give

    dV(delta)=(1/2) sum_i
       [Re V_i delta Im U_i-Re U_i delta Im V_i].             (5)

This vanishes for every delta in T precisely when b(r) lies in
L^perp=L, which is (4). This proves the claim for ALL angle tangents,
including directions absent from the source parameter space.

For a filled cusp the row is (1,p_i); its imaginary constraint fixes
the actual marked value Im(U_i+p_i V_i)=+/-2pi, while (4) requires
Re(U_i+p_i V_i)=0. For a retained main cusp one can use the meridian
row (1,0); genuine parabolicity gives U_i=V_i=0 and is stronger than
the real condition needed for stationarity. All primitive markings
and the original centered SL signs still have to be proved separately.

## 2. Why this gives the unique maximum, and what it does not identify

On one positive angle simplex the negative Hessian in (alpha,gamma) is

    [[cot alpha+cot beta, cot beta],
     [cot beta, cot gamma+cot beta]].

Its determinant is 1 and its first diagonal entry is
sin(gamma)/(sin(alpha)sin(beta))>0. Thus V is strictly concave on
every affine angle slice. An interior point satisfying (4) is its
unique global maximum, also over the closed slice: along any segment
from that point the derivative starts at zero, then strictly decreases;
continuity of Lambda handles its final boundary endpoint.

Three further identifications remain logically distinct:

1. **Source value.** Vsrc=V(theta_*) requires the absolute action /
   marked regulator comparison on an actual oriented fundamental chain,
   including the 2pi/N scale and all centered peripheral terms.
   Equality of stationary equations cannot fix an additive action
   constant. Nor does a peripheral curve alone fix its Bloch-period lift.
2. **Actual topology and ends.** The constraints must be those of the
   desired manifold. A complete-cusp maximum is not the filled-slope
   problem. For a filling, peripheral holonomy equal to identity only
   modulo 2pi does not establish a smooth primitive tube: winding twice
   produces angle 4pi. Positivity, actual face/shape matching, the
   primitive log period, and smooth end completion must be supplied.
3. **Geometric value.** To infer V(theta_*)=Vol(M), either a geometric
   angle point for the SAME slice must be independently identified (then
   strict concavity identifies the two), or the selected positive
   developing structure must be completed to the actual hyperbolic
   manifold. A representation-volume upper bound alone supplies only
   Vsrc<=Vol(M), not equality.

The long-pretzel proof supplies these via its literal port lift,
absolute marked regulator, positive core and primitive tube completion.
Its direct completion argument remains independent of the optional
positive all-ideal triangulation and quotient-matrix inputs in (2).

## 3. A restricted source saddle is insufficient: an exact angle example

In a single ideal tetrahedron restrict to

    alpha=pi/2, beta=pi/4+t, gamma=pi/4-t.

At t=0 the restricted volume derivative is zero, and the second
derivative is -2: this is the unique restricted maximum. Nevertheless
the legitimate full angle tangent

    (delta alpha,delta beta,delta gamma)=(-2,1,1)

has dV=log 2>0 there. The point is not the full maximum; the regular
tetrahedron has strictly larger volume. This counterexample already
uses the TRUE tetrahedral volume and a positive angle point. It is not
an issue about choosing the wrong dilogarithm branch.

Generally, for a source map Theta:X -> A with image tangent B, source
stationarity gives only dV|_B=0. It implies dV|_(T A)=0 if B spans
T A, or if B plus independently proved zero-derivative directions spans
T A. Alternatively, genuine stationary elimination can supply all
discarded equations. Without one of these mechanisms, strict concavity
of V proves only a maximum on the restricted source family.

No rank condition on Theta is necessary when the full complex gluing
and peripheral criterion (4) has already supplied the missing equations.
That is the useful stronger implication in Section 1.

There is also a separate optimization shortcut: if a source limit is
proved to be max_(theta in Psrc) V(theta), Psrc is contained in the
correct angle polytope, and its image is proved to contain the geometric
maximizer, the two maxima agree. Merely knowing that Psrc is nonempty,
positive, or has its own unique stationary point does not prove that
containment.

## 4. Audit conclusion

The full-angle stationarity step in the existing Casson--Rivin note is
valid UNDER its stated positive-shape, real-edge, full-rank quotient and
actual peripheral hypotheses: it uses (5), not restricted source
stationarity. For a new general source, those hypotheses are substantive
gates. Local tetrahedral volume factors, a source Hessian, a restricted
maximum, or numerical agreement with cusp derivatives cannot replace
them. This note establishes the implication and its precise failure
mode; it makes no new unrestricted knot theorem or quantum survival
claim.
