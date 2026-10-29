# The full scalar certificate leaves two explicit framing boundary currents

Research proof and obstruction, 27 October 2026. The full actual
finite-array annihilator can be transported through the transverse
Gaussian contraction, including the least-moment repair. Its image
is **not yet an annihilation equation** for the sourced geometric
period: it has two explicitly computable framing boundary terms.
This note derives those terms and states precisely why the residual
flat Ward ideal and the current coherent source constructions do
not remove them.

No full geometric-support theorem, selected-source survival, or
volume limit is claimed here.

Subsequent explicit source maps now include
[polynomial centralizer residues and endpoints](centralizer_normal_residue_and_actual_cut_moments.md),
the [whole actual cut clock](dual_clock_normal_cut_source.md), and the
[degree-N wall row on an actual high color](high_integral_color_frobenius_wall_source.md).
They retain the raw/matrix normalization and first-normal block
arrows. The independent transfer-current map and cancellation in
equation (7) below have not been established by these constructions.

## 1. The least-moment repair has a literal Green certificate

Use the original normalized-average off-root array, whose full
flow support has a strict interior. Construct the global certificate
as in [the finite-array proof](finite_sum_annihilator.md), strip the
common central root factor from the **whole certificate**, and
specialize. Write the resulting nonzero certificate as

    P=sum_beta A_beta(M,T_M) D^beta,
    D_i=S_i-I.

All actual flow indices, including the two framing indices, occur
among the `S_i`. The coefficients contain no multiplication by an
internal index character. Let `h` be the least total degree with
`A_alpha!=0`, and choose such an `alpha`. The actual full scalar
moment operator is `A_alpha`. Put

    p_alpha(k)=product_i binom(k_i,alpha_i),
    nabla_i p=S_i^(-1)p-p.

The exact discrete product rule is

    p D_i f=D_i[(S_i^(-1)p)f]+(nabla_i p)f.       (1)

For a fixed ordered word `i_1,...,i_n` representing `D^beta`, set
`p_0=p_alpha` and `p_m=nabla_(i_m)p_(m-1)`. Iterating (1) gives

    p_alpha D^beta f
      =sum_(m=1)^n D_(i_m)[(S_(i_m)^(-1)p_(m-1))
                                 D_(i_(m+1))...D_(i_n) f]
        +(nabla^beta p_alpha)f.                  (2)

This identity is pointwise on zero-extended integer arrays, with
no summation or boundary omission. Multiplication by an external
Ore coefficient commutes with these index polynomials and shifts.

If `|beta|>h`, the final polynomial in (2) is zero. If
`|beta|=h`, it is zero unless `beta=alpha`, in which case it is
`(-1)^h`. There are no lower-degree coefficients in `P`. Thus
`P I=0` and (2) produce the **global finite Green certificate**

    (-1)^h A_alpha I=sum_i D_i J_i,              (3)

where the actual currents are explicitly

    J_i=-sum_beta A_beta sum_(m:i_m=i)
           (S_i^(-1)p_(m-1))
                            D_(i_(m+1))...D_(i_n) I.          (4)

Every current is still a finite zero-extended array. Summing (3)
over every index kills its right side exactly, proving the actual
full scalar all-level annihilation. Equations (3)--(4) give more
information than the summed moment argument: they retain its
specific boundary currents.

## 2. Transverse Gaussian pushforward leaves exactly two currents

Choose the two external actual flow coordinates of
[the partial support theorem](partial_geometric_support_theorem.md),
with one chosen to be the cut index. Contract only their nondegenerate
transverse complement by the actual formal Gaussian `G`. The
interior rational identity underlying the whole certificate is
valid independently of the multiplication characters, by the strict
support cone argument. Therefore (3) has the same formal realization.

The polynomial moment insertions cause no local difficulty. With
the chosen logarithmic lifts, `k_i=u_i/H`, so they are finite
Laurent powers in `H` with polynomial logarithmic insertions. Their
Wick coefficients are well defined. Transverse total differences
have zero formal contraction by the exact translation identity;
external shifts commute with the Gaussian base substitution. Hence

    (-1)^h A_alpha Z
       =(T_(chi_1)-I) Jhat_1+(T_(chi_2)-I) Jhat_2,             (5)

where `Z=G(I)` is the actual nonzero transverse block and each
`Jhat_a=G(J_(chi_a))` is computed by the same actual normalized
moment formula used in
[the residual-current theorem](residual_gaussian_ward_currents.md).
External meridian shifts in (4) are retained. This is an exact
formal identity, with the original base and peripheral lines.

Thus the actual FULL scalar operator has been transferred to the
geometric block with a **specified two-current defect**. It has
not been proved to annihilate a final nonzero sourced period.

## 3. The precise remaining relative boundary functional

Let `Gamma` be a specified marked relative framing chain and let
`F_(a,H)` be the frame-coordinate translation underlying `T_(chi_a)`.
For a top-degree current form `J`, its final defect is

    B_(Gamma,a)(J)=integral_(F_(a,H)Gamma-Gamma) J.              (6)

This notation includes the marked endpoint co-sources and the
logarithmic-cover endpoints, rather than silently identifying them.
Equivalently the formal Cartan homotopy is

    K_(a,H)=integral_0^H F_(a,eta)^* iota_(X_a) d eta,
    F_(a,H)^*-I=d K_(a,H)+K_(a,H)d.

Top forms are closed; consequently (6) is the integral of
`K_(a,H)J` over the marked boundary. The formula is coefficientwise
formal and needs no convergence of the Gaussian expansion.

Applying a source-compatible final functional to (5) would give

    (-1)^h A_alpha V_geo
       =B_(Gamma,1)(Jhat_1)+B_(Gamma,2)(Jhat_2).                (7)

The needed theorem is that the **actual finite normal/endpoints**
map to the co-sources making the right side of (7) zero, with
`V_geo!=0`. Neither equality has yet been proved.

At completeness, in centralizer coordinates `t=r/s` and cut
coordinate `A=1/(1+s)`, the leading form is
`dt wedge dlog A`. The vertical endpoint part is already explicit:

    Res_(A=0)[j(1,A)-j(0,A)]dlog A              (8)

for an infinitesimal current `partial_t j`. In a flat frame-line
gauge with horizontal unit `g`, it becomes

    Res_(A=0)[g(1,A)^(-1)j(1,A)
                     -g(0,A)^(-1)j(0,A)]dlog A.               (9)

The complete residual Ward ideal fixes this flat connection. It
does not assign the two endpoint co-sources of every `Jhat_a`.

There is a sharp algebraic reason. Since

    nabla_t(t g)=g,

any absolute linear functional annihilating every covariant current
would also annihilate the horizontal generator itself. Nonzero
source survival therefore requires the relative endpoint terms;
it cannot be obtained by quotienting all frame divergences away.
Polynomial moments in (4) produce precisely the kind of coordinate
insertions to which this issue applies.

The logarithmic direction has a second recorded boundary: continuation
around `A=0` changes the actual index lift by `k->k+N`. Thus the
moment polynomial has jump `p_alpha(k+N)-p_alpha(k)`. This is the
source carry that is absent from a single regular-coefficient WKB
sector. It is not removed by the residual flat ideal.

## 4. Every ordinary one-cut source collapses to one index weight

There is a uniform constraint on attempts to realize the last
framing period using a family of finite cut coupons. Every actual
crossing conserves the integer sum of positions. Closing all but
one strand forces the cut output index to equal its input index,
for each individual internal state. Thus the uninserted cut array
is diagonal before its remaining internal sums.

For **any** linear functional `lambda_B` on that matrix space,
including one formed using divided adjoints and additional finite
parameters, one has

    lambda_B(C)=sum_(a=0)^(N-1) w_B(a) C_aa.                  (10)

The weights may have many parameters, but as scalar flow insertions
they depend on the one actual cut index. They do not create a second
independent internal framing coordinate.

In particular the exact divided-normal source

    Phi_div(C)=-Phi(J_E^ad(CW))/(N-1), W=E_(N-1,0),

satisfies, for every diagonal matrix,

    Phi_div(C)=C_(N-1,N-1).                                  (11)

Indeed `CW=C_(N-1,N-1)W`, and the proved normal pairing is
`Phi(J_E^ad W)=-(N-1)`. Thus this source is exactly the endpoint
cut on the diagonal state. Its all-matrices Ward homotopy remains
valuable, but after ordinary partial trace it does not independently
specify the vertical centralizer endpoints in (8).

If a boundary weight has leading phase `G(A_cut)/H`, then its
differential and Hessian along the framing torsor have no component
in the vertical direction: `V_J A_cut=0`. At an unchanged geometric
critical point, criticality forces `G'(A_cut)=0`, and the added
Hessian has rank at most one on the two-dimensional framing radical.
Thus no family of ordinary one-cut coupons removes both framing
modes at that point. This extends the earlier coherent-cut
obstruction to all such finite linear source families.

Divided-adjoint pivotal naturality does not evade (10): it moves
the full inserted action, with its mixed terms, to a cut functional.
A two-dimensional abstract source orbit may still provide a useful
relative normal complex, but its group/torsor isomorphism alone is
not a map from the two internal framing coordinates to that orbit.

## 5. What the balanced coherent Verma source adds, and what it does not

The [common Verma source](common_verma_two_wall_source.md) supplies
literal head inclusion/projection, the two boundary arrows, and
their mixed adapter `delta w H_beta`. The
[balanced coherent crossing](balanced_verma_coherent_braiding.md)
supplies an actual source kernel and changing-source braid matrices.
Its selected cut is exactly source independent:

    C_beta(s_1,...,s_b)=F_N(M) I.

Consequently any normalized scalar period formed solely from those
coherent parameters tensors this same unknown knot scalar by its
universal source period. Its meridian/centralizer normalization is
specified, but it does not determine the coefficient of the
geometric block. In particular the ordinary source independence
does not identify the logarithmic polynomial-current jumps or
relative endpoints in (7)--(9).

The common module is a promising place to retain those terms:
degree-N block carries and the original marked coupon exist there
before either wall quotient. The required next map must send the
explicit currents (4), including their moment polynomials, through
that relative source and identify their geometric endpoint/carry
functional. The currently proved coherent-kernel identities and
the complete residual formal Ward ideal do not supply this map.

Equation (7), with currents (4), is therefore the precise remaining
defect for upgrading the partial support theorem to the actual full
scalar certificate. No geometric factor of the selected full scalar
operator has been established by this note.

The subsequent [whole relative-word construction](relative_word_green_transport.md)
now supplies the actual coefficient/current map through Fock, Mellin
and Rees source complexes for every moment in (4), retaining all
projectors and endpoint terms. The
[compact coherent period](compact_coherent_source_period.md)
also supplies its global algebraic cycle and exact product calculus.
The unresolved map is from that specified actual class to the
geometric Gaussian class: the compactified critical framing family
and its possible polar/escaping terms must be controlled. Neither
construction yet proves the nonzero geometric pairing or the
cancellation in (7).

[Universal Green audit](../experiments/audit_full_certificate_green.py)
and [results](../experiments/full_certificate_green_results.json)
verify (2) as an identity in the free shift module, with independent
symbols for all shifted array values. They check its least-degree
residual in one, two and three dimensions. No knot example or
unproved framing-boundary cancellation is used.

[Independent Green and source-map audit](fock_mellin_and_green_independent_audit.md).

The [actual Gauss-wall cut-current theorem](actual_gauss_wall_cut_current_complex.md)
now computes one part of this missing boundary map at the finite
source level. Its two hemisphere rows have a shared binomial
wall co-source and both shifted endpoints. Matrix-normalized
currents are N times the original raw Green arrays, so no cut
normalization is absorbed. The exact two-current identity retains
the second framing divergence. Commuting this finite source map
with the internal Gaussian, and transporting its nonzero Cech
source class, remain necessary for (7).
