# The actual meridian cut and the geometric cyclic point source

Research note, 26 October 2026. The original two-factor pivotal cut
has two normalized branch weights that are consecutive meridian
translates. Their ideal, their normalization defect, and the cokernel
of the regularized cut recover the same length-one point module as
the geometric cyclic lattice. A specified formal gauge places the
geometric branch collision on exactly these actual cut walls.

This proves a local comparison of the source and cut presentations
as modules over the quantum--meridian base, with their residues and
full normalization line recorded. It does not identify the actual
global affine difference extension, its selected knot section, or
its regulator norm across levels.

## 1. Two consecutive shift factors come from the actual cut

Keep the original conventions

    q=q_N=exp(pi*i/N), x=-M/q, Y=M^2, U=M^(2N),
    sigma(M)=qM, rho=q-q^(-1), c=q+q^(-1).

Use the branch-marked comparison of the actual Casimir pair with
the geometric node in Section 7 of
[the geometric rigidity note](geometric_rigidity_and_cyclic_source.md).
Write d=L_+-L_-, d(u)=kappa*u+O(u^2), u=Log M, kappa!=0,
and

    B=R[xi]/(xi(xi-d)), R=C[[u]].

The branch xi=d is marked + and xi=0 is marked -. If f belongs
to B, denote its branch values by f_+,f_-. Set

    p=q^(-1)M^2-qM^(-2),
    r=qM^2-q^(-1)M^(-2).

There is an exact meridian identity, before any specialization:

    r=sigma(p).                                    (1.1)

Let Phi_N be the actual scalar pivotal cut on this pair, including
the full ADO modified dimension. The earlier exact cut formulas
give the branch expression

    Phi_N(f)=Gamma_N [r f_+ + p f_-]/d,             (1.2)

where the complete common frame is

    Gamma_N=(-1)^N d_N(M) d/
                    [(M-M^(-1))(M^N+M^(-N))]
           =-zeta_N U d/[(U-1)(U+1)],
    zeta_N=q^(N(1-N)/2).                           (1.3)

This retains both peripheral factors and the original phase.
It is an identity of whole meridian germs; its zeros and poles
are not separately evaluated. At completeness it has value

    Gamma_N(1)=-zeta_N*kappa/(4N).                 (1.4)

For example, to derive (1.2) directly, let

    gamma_N=(-1)^N d/
                    [(M-M^(-1))(M^N+M^(-N))].

The density coefficients from that note obey

    theta_-=theta_0=-gamma_N*p,
    theta_+=theta_0+theta_1*d=gamma_N*r.

The residue functional on B is (f_+-f_-)/d. Substituting these
two density values and multiplying by the actual d_N proves
(1.2). This is a consequence of the actual projector cuts, not
a chosen geometric trace.

## 2. The common algebraic cut germ has a point defect

For the local two-parameter comparison put

    S=C[[u,h]], q=exp(h), M=exp(u),
    sigma(u)=u+h, sigma(h)=h.

Keep Gamma_N as the full normalization line in (1.3). After
factoring this recorded line, the cut coefficients have a common
algebraic germ independent of N. This does not assert an off-root
deformation of the entire N-dimensional root representation.

The two wall equations have expansions

    p=4u-2h+O((u,h)^2),
    r=4u+2h+O((u,h)^2).

Consequently

    (p,r)=(u,h)=:m,
    det partial(p,r)/partial(u,h)|_0=16.           (2.1)

This equality follows from the invertible linear coefficient
matrix and formal inversion. Their walls are exactly the balanced
half-step meridian walls on the chosen local cover:

    p=0 <=> M^2=q,
    r=0 <=> M^2=q^(-1).                           (2.2)

For example p=q^(-1)M^(-2)(M^2-q)(M^2+q); the other factor is
a unit near q=M=1. The first wall equation pulls back to the
second under sigma. Their product is the exact expression

    pr=(M^2-M^(-2))^2-(q-q^(-1))^2.               (2.3)

Thus their intersection is a reduced point, with ordered residue

    Res_0 du dh/[p sigma(p)]=1/16.                (2.4)

At a fixed actual root q_N!=1, this is not a second source at
M=1: p(1)=-rho and r(1)=rho are both nonzero. The point in
(2.1) records their joint quantum--meridian degeneration.

## 3. The cut pairing and its regularized dual retain this point

Extend the geometric node to S and retain d=d(u). The normalized
density element is

    theta_hat=-p+b xi,
    b=(p+r)/d=c(M^2-M^(-2))/d.                    (3.1)

Its branch values are -p and r. Since d=kappa*u+O(u^2),
b is a unit and b(0,0)=8/kappa. The full density is
Gamma_N theta_hat; factoring its line has not changed the period.

For the residue functional Res_B(a+b_1 xi)=b_1, the normalized
trace-pairing matrix in the basis 1,xi is

    H_cut=[ b    r  ],
          [ r   d r ].

It has determinant pr. Elementary simultaneous row and column
operations with the unit b reduce it to

    diag(b,pr/b).

Therefore the pairing's cokernel is the nodal divisor module

    coker H_cut = S/(p r).                        (3.2)

Its normalization has the exact sequence

    0 -> S/(pr) -> S/(p) direct_sum S/(r)
                     -> S/(p,r) -> 0,             (3.3)

where the last map is the difference of the two reductions at
their intersection. Injectivity uses (p) intersect (r)=(pr),
since p,r are regular local coordinates. Its cokernel is exactly
the length-one point module S/m. Thus normalization of the cut
degeneracy divisor loses a specified point datum.

There is also a direct presentation from the cut itself. On the
normalization V=S^2, multiplying (1.2) by d gives the regular row

    ell_hat:V -> S, (f_+,f_-) -> r f_+ + p f_-.

Its image is m and its single primitive relation is (p,-r).
Hence

    0 -> S --(p,-r)--> S^2 --(r,p)--> S
                                     -> S/m -> 0. (3.4)

For exactness, if r a+p b=0, coprimality gives a=p t and
b=-r t. This is the complete proof of the relation. The full
regularized cut is Gamma_N ell_hat, with Gamma_N still recorded.
The factor d used for regularization has a simple meridian zero;
replacing it by another such factor requires keeping their unit
ratio. This does not evaluate the original cut by substitution.

## 4. Calibrating the geometric cyclic generator to the actual wall

Let a,b_geo be any two geometric formal shift ratios in S^times,
with common complete value L_c and classical difference

    a(0,u)-b_geo(0,u)=kappa*u+O(u^2), kappa!=0.

Here a and b_geo are the two ratios of
[the nonzero geometric normal blocks](actual_geometric_normal_period.md),
with their existing leading marked actions. We now give an exact
formal unit gauge whose branch collision is the actual wall p=0.

On the specified square-root meridian cover define

    R_0(h)=[b_geo/a]_(M=q^(1/2)),
    A(h)=(R_0(h)-1)/(q^3-q),
    g(M,h)=1+(M^2-q)A(h).                         (4.1)

R_0(0)=1, and q^3-q has a simple h zero, so A belongs to C[[h]]
and g is a unit with g(0,0)=1. The formula uses division by a
known first-order zero with divisible numerator, not a punctured
formal germ. In particular

    g|_(M=q^(1/2))=1,
    sigma(g)|_(M=q^(1/2))=R_0.

Change the first branch ratio by the exact unit gauge

    a_star=a sigma(g)/g, b_star=b_geo.             (4.2)

It follows identically that a_star-b_star vanishes on p=0.
Its classical specialization remains a(0,u)-b_geo(0,u), because
sigma is identity at h=0. Therefore

    Delta_star=a_star-b_star=v p,
    v in S^times, v(0,0)=kappa/4.                (4.3)

This proves the factorization: the vanishing gives divisibility
by the smooth local equation p, and the derivative ratio gives
the displayed nonzero unit. No higher recursion is needed.
The construction is the unique affine function of M^2 with the
two prescribed values in (4.1). It preserves the leading marked
regulator action. It chooses a model geometric cyclic generator;
it does not identify the original selected knot generator.

For the split module with ratios a_star,b_star, keep e=(1,1)
and f=(1,0). The complete all-shifts cyclic lattice is exactly

    Lambda_star=sum_(j in Z) S T^j e
               =S e direct_sum (p,r)S f.         (4.4)

Indeed Te and T^2e generate component differences Delta_star
and a_star sigma(Delta_star)+Delta_star sigma(b_star). Their
ideal is (p,r)=m. Every positive or negative shifted difference
vanishes at (0,0); invertibility of both ratios covers negative
shifts. This proves both inclusions in (4.4).

## 5. A local source and cut presentation now agree

Equation (4.4) has generators e,p f,r f and one relation

    r(p f)-p(r f)=0.

Dualizing this presentation gives

    Ext^1_S(Lambda_star,S)=S/(p,r)=S/m.           (5.1)

Explicitly the dual relation is the row (0,r,-p); its cokernel
is S/(p,r). After reversing the sign of its last generator and
discarding the zero first column, it is the regularized actual
cut row (r,p) in (3.4). This is an explicit comparison of the
two source presentations, not only an equality of their lengths.
The normalization quotient in (3.3) gives the same point module.

The calibrated geometric ordered residue also has the required
value:

    Res_0 du dh/[Delta_star sigma(Delta_star)]
                   =(4/kappa)^2/16=1/kappa^2.     (5.2)

The two density branch values have an opposite ordered sign,
since they are -p,r; their normalized ordered residue is -1/16.
This sign is retained under comparison rather than absorbed into
the phase zeta_N or a longitude sign. The full physical frame
Gamma_N has the exact complete value (1.4) and remains separate.

Thus the actual two-factor cut has now specified the same local
point ideal, presentation, and calibrated residue as a geometric
cyclic model whose collision has been placed on its meridian wall.
This strengthens a fixed-N nodal-order isomorphism. It identifies
how a source appears when q and M degenerate together and why an
ordinary normalization or ordinary dual alone can forget it.

The following assertions have not been established by this local
comparison:

* The actual global meridian source has this difference-module
  presentation, including its induced transport on the source.
* The actual selected knot section is the calibrated model generator.
* Sewing the other crossings preserves this class and pairs it
  nontrivially with the geometric block.
* The resulting selected root period has the regulator norm across
  levels.

In particular (5.1) does not imply vanishing of the global affine
extension obstruction in Section 8 of the normal-period note.
That requires an intertwining map with the actual source arrows,
not just the presentation over S. The positive triangulation
supplies the geometric ratios needed in Section 4; the actual
projector cuts supply the walls in Sections 1--3.

## 6. Coverage and independent exact checks

Modified traces have existing coverage in
[Beliakova--Blanchet--Gainutdinov, 1801.00321](https://arxiv.org/abs/1801.00321).
The literature quantum-A definition remains the recurrence
definition covered by
[Garoufalidis--Sun, 0802.4074](https://arxiv.org/abs/0802.4074).
Only their abstracts were consulted for scope in this step; no
proof or recurrence coefficient from either is used. No novelty
claim is made for modified-dimension numerators, normal crossings,
cyclic-vector changes, or the elementary presentation duality.

[The audit](../experiments/audit_cut_wall_source.py) verifies the
universal shift identity, all wall factorizations, the two-coordinate
Jacobian, the complete trace-pairing reduction, and the primitive
cut relation with exact rational functions. Four rational formal
ratio pairs check (4.1)--(4.3), including nonzero subprincipal terms
and both complete longitude signs.

Twelve generic root cases at N=2,3,4,5,6,9 construct the original
tensor E,F,K and actual highest-vector projectors, then contract
them with the original pivotal matrix. Their two projector cuts
agree with (1.2), including the complete common peripheral frame.
Six complete cases independently contract the confluent Casimir
projector and nilpotent. The level checks include both parities
and even and odd composite levels. They validate the exact
coefficient derivation, not the global selected-period assertions.
[Results](../experiments/cut_wall_source_results.json).

Reproduce with:

    python3 experiments/audit_cut_wall_source.py

The subsequent [equivariant transport calculation](equivariant_cut_source_transport.md)
now supplies the meridian matrices for the normalized presentations
above. It identifies the cut complex with an explicit quotient of
the geometric dual cyclic presentation, tensored with the dual
geometric period line. The point source therefore keeps its
inverse complete longitude character. The root matrices verify
the cut-weight shift, while the physical difference-constant
normalizer and its poles remain retained. The actual global
source, selected section and central lattice at U=1 still need
comparison.
