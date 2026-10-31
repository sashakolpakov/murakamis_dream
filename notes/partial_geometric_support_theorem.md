# A geometric A-factor for an actual partially summed quantum state

Research note, 27 October 2026. This proves a bulk geometric-support
theorem for the original finite coefficient model. Leave two actual
integer flow coordinates unsummed, and eliminate all remaining flow
coordinates. The resulting finite family has a specifically constructed
nonzero all-level meridian annihilator whose first nonzero classical
symbol contains the marked geometric A-factor. The construction does
not append a known classical factor.

This partial family retains its two framing indices. Pairing them with
the selected full finite source is a further operation. The theorem
does not assert survival under that operation, a statement about the
minimal scalar annihilator, or a volume limit.

## 1. The actual partial family

Use a knot braid with `b` strands and `m` crossings, the balanced
factorial boundary frame, and the original normalized cut average. Set

    q_N=exp(pi*i/N), Q=q^2, x=-M/q, Y=M^2.

All crossings, the original pivot, the full zero-framing correction,
the cut factor `1/N`, lift characters and base-only compact factors
are retained. If the full ADO state is wanted, its complete original
marked factor `d_N(M)` remains an external line; it is not absorbed
into a formal unit or replaced by its value at completeness.

Closing strands `1,...,b-1` gives a cofactor of the knot permutation
matrix minus identity, with determinant `+1` or `-1`. Solve these
closures integrally. The independent actual flow coordinates are

    k=(a_0,k_1,...,k_m),       d=m+1.

The remaining closure follows from total-index conservation. The
summand is the actual product of the finite crossing and boundary
coefficients, zero outside its finite integral support.

On the regular geometric critical chart the Hessian has a
two-dimensional radical equal to the tangent space of the framing
torsor. This is the Morse--Bott statement for the **actual** coefficient
phase proved in [the normal-period note](actual_geometric_normal_period.md).
Select two members `chi_1,chi_2` of the displayed actual coordinate
list whose differentials are independent on this radical. Such a pair
exists because the radical is a two-dimensional subspace of the
coordinate tangent space. No integral change of variables is made.

Keep `chi=(a,b)` external and sum only over the remaining `r=d-2=m-1`
coordinates `j`. The actual partial array is

    F_N^chi(M;a,b)=sum_(j in Z^r) I_N(q_N,-M/q_N;a,b,j).

The sum is finite and includes its exact boundary. Its final contraction
over the two external indices is the original reduced scalar state.
The auxiliary off-root lift uses the same normalized cut trace and
the same partial array, with generic `q`; topological invariance of
that off-root lift is not a premise.

For coefficient bookkeeping put

    z=q^N, Ahat=q^a, Bhat=q^b, t_i=q^(j_i).

The physical phase coordinates are `A=Ahat^2=Q^a` and
`B=Bhat^2=Q^b`. Keeping `Ahat,Bhat` avoids suppressing the genuine
square-root characters in a meridian half-step. Alternatively one may
work on their stated finite etale cover. Let `T` send `M` to `qM`
(equivalently `x` to `qx`) while holding `q,Ahat,Bhat` fixed.

## 2. A global partial-array certificate

The proof in [the finite-array annihilator note](finite_sum_annihilator.md)
extends with the two external multiplication variables. Its summand
ratios are proper and aligned rational functions in

    q,x,z,Ahat,Bhat,t_1,...,t_r.

For `0<=e_x,e_z,e_A,e_B,e_T,beta_i<=R`, consider

    x^e_x z^e_z Ahat^e_A Bhat^e_B T^e_T S^beta I,

where `S_i` shifts `j_i` by one and never shifts `a,b`. These are
`(R+1)^(r+5)` independent formal Ore monomials.

Their image span has dimension `O(R^(r+4))` over `Q(q)`. In the
interior, clear the rational shift ratios by one common denominator
whose Laurent degrees are `O(R)` in the `r+4` multiplication variables
`x,z,Ahat,Bhat,t`. For the boundary proof, stratify every support
inequality according to whether it is far inside, far outside, or
has one specified integer value in an interval of length `O(R)`.
If the near-boundary forms have rank `c` on `(N,a,b,j)`, there are
`O(R^c)` consistent sets of their labels. On each resulting stratum,
the associated `c` binomial relations leave
`O(R^(r+4-c))` Laurent monomials after the fixed Smith reductions.
The total contribution is again `O(R^(r+4))`. Supported shifts have
nonzero common denominators on the stratum, exactly as in the
original proof. Empty and lower-dimensional supports are included.

Finite linear algebra therefore constructs a nonzero certificate

    P(x,z,Ahat,Bhat,T,S) I=0                       (2.1)

on the whole zero-extended array, with no multiplication by any
internal `t_i`. Separate summand components, if present, can be
retained in a direct sum, giving a common certificate.

The full flow support has a nonempty open cone of strict inequalities:
take all transfers small and positive compared with `N` and the free
cut position near `N/2`. Every position is then `N/2+O(epsilon*N)`.
This is unchanged by choosing a subset of the coordinates as external.
Consequently (2.1), divided by a nonzero interior reference term, is
a rational identity in all independent multiplication variables.
The precise lattice-cone density proof is in
[the sourced-telescoping audit](sourced_telescoping_geometric_support_criterion.md),
Section 2. This step is needed: a relation only on isolated discrete
frame values would not suffice for the formal geometric argument.

## 3. Root specialization and transverse moment repair

Clear fixed coefficient denominators and divide the largest common
central power `(z+1)^s` from the **whole** certificate, obtaining `P0`.
For each fixed generic `N`, `q^N+1` is a nonzero rational function of
`q`, so the global array identity survives this division. The finite
summands are regular at `q_N`; their crossing factorial denominators
have indices below `N`. Thus

    P1(x,Ahat,Bhat,T,S)=P0(x,-1,Ahat,Bhat,T,S)      (3.1)

is nonzero and annihilates the actual root partial arrays for all but
finitely many levels. The same specialization is valid for the
independent-variable interior contiguity identity.

Expand in the commuting transverse shifts only:

    P1=sum_alpha D_alpha(x,Ahat,Bhat,T)(S-1)^alpha.

Let `h0` be the least total degree with a nonzero coefficient, and
choose any nonzero `D_alpha` of that degree. Give the finite internal
sum independent weights `exp(v dot j)`. Exact translation of the
whole finite zero-extended sum sends `S_i` to `exp(-v_i)`. At degree
`v^alpha`, every positive moment multiplies a coefficient of degree
below `h0`, and hence is zero. Therefore

    D_alpha(q_N,-M/q_N,q_N^a,q_N^b,T)
                          F_N^chi(M;a,b)=0.       (3.2)

This is a genuine nonzero all-level operator for the actual partial
family. All external labels and all finite boundary strata are kept.

## 4. The same certificate acts on the exact formal transverse period

Write `H=Log Q=2 Log q`. In logarithmic physical flow coordinates,
the actual interior coefficient has a formal realization

    I_form=C_beta(H) exp(S/H) a(u,H),

with the original characters, `a(u,H)=a_0(u)(1+O(H))`, and `a_0` a
unit on the chosen geometric chart. The retained base line
`C_beta(H)` includes the cut average and the fixed compact factors.
It is not evaluated at an individual root.

This formal realization has the **exact** rational contiguity ratios,
not merely their leading symbols. One construction uses the original
monomials and the compact-product series, for variable arguments
different from `0,1`,

    log P_Q(z)=Li_2(z)/H +(1/2)log(1-z)
      +sum_(n>=1) B_(2n) H^(2n-1)/(2n)! Li_(2-2n)(z).

Its formal functional equation is
`P_Q(Qz)=P_Q(z)/(1-z)`. This follows either coefficientwise from
the Bernoulli generating function or by expanding the defining
geometric-series logarithm. Thus its ratios agree to all orders
with cancellation of the original finite factors. Signs and logarithm
sheets are the ones fixed by the actual critical-correspondence
calculation. The fixed singular argument `P_Q(Q)` stays in the
base-only line. Pivotal monomials and the framing correction have
their literal exact shift ratios as well.

Now fix the two external coordinates `chi`. The remaining coordinate
space complements the radical of the symmetric Hessian. The
restricted `r` by `r` Hessian is therefore nondegenerate. The critical
point of `S` in the remaining variables is unique in the chosen
formal germ. The full geometric critical surface is etale over
`chi`, so its unique point at each nearby external `chi` supplies a
solution of these transverse equations. By uniqueness this is the
same partial critical germ, and all of the full critical equations
hold there. Its unweighted Gaussian contraction is nonzero, with
leading amplitude

    a_0/sqrt(det(-H_perp)).                       (4.1)

Introduce independent weights by replacing the phase with

    S_v(u)=S(u)+sum_(i=1)^r v_i u_i.

The formal implicit-function theorem gives a unique critical point
`u(v)` with `u(0)=u_*`, because `H_perp` is invertible. Formal
stationary contraction there defines `Z_chi(v)`. It is a formal
power series in `v` whose coefficients lie in the original WKB
line times Laurent series in `H`. Its value at zero is nonzero.
The action difference divided by `H` can produce increasingly
negative finite `H` orders as the `v` degree grows; this is allowed.

Formal stationary contraction is invariant under a translation of
an internal integration coordinate. Explicitly, for the unit shift
`u_i -> u_i+H`, substituting `y_i=u_i+H` in the formal Gaussian gives

    G_v(S_i f)=exp(-v_i) G_v(f).                  (4.2)

This is an identity of formal stationary expansions at their
corresponding critical points, with an elementary termwise proof.
For one shifted coordinate its weighted phase is

    S(u+H e_i)+v dot u = S_v(u+H e_i)-H v_i.

Its critical point is `u(v)-H e_i`. Centering at that point gives
exactly the same Hessian, higher vertices, amplitude Taylor series
and coordinate volume as centering `S_v` at `u(v)`. Only the constant
phase changes, by `-H v_i`. Thus every Wick coefficient is multiplied
by `exp(-v_i)`. No integration-by-parts theorem is a premise of this
argument. No finite-array endpoint or framing endpoint is being
discarded here: this is a formal contraction of precisely the `r`
nondegenerate transverse variables. Both framing coordinates remain
external throughout.

The same formal contraction commutes with the meridian step `T`.
The shifted critical point is the unique nearby one with the same
external `Ahat,Bhat`; the formal construction and its retained
half-density are natural under that base shift. Multiplication by
external rational coefficients commutes as well.

Apply this contraction to the exact interior identity (3.1). By
(4.2),

    P1(x,Ahat,Bhat,T,exp(-v)) Z_chi(v)=0.

The same least-degree moment coefficient used for the **finite**
partial sum therefore gives

    D_alpha Z_chi(0)=0.                          (4.3)

Unlike full framed integration, this implication has no missing
relative-source covariance assumption. Nondegeneracy of the
transverse block and leaving both framing coordinates external
provide it directly.

The subsequent [full Green-certificate calculation](full_certificate_framing_boundary.md)
also transports the actual fully summed scalar operator to this
transverse block. Its image includes two explicitly computed framing
boundary currents. Their final endpoint and logarithmic-carry
functional is retained; neither the formal residual Ward ideal nor
the source torsor identities currently prove its cancellation. Thus
the distinction between the present partial theorem and the full
scalar claim is now an explicit source defect, not an omitted
ordinary Gaussian variable.

## 5. The classical symbol has the geometric factor

Divide `D_alpha` by its common scalar `(q-1)` valuation and clear
remaining rational denominators. Call the resulting nonzero operator
`Dhat`. Scalar division is valid both in the actual root identities
(for all large `N`) and in the formal WKB line. Let

    d_cl(M,Ahat,Bhat,L)

be its first nonzero classical symbol in the stated meridian and
lift gauge. The exact preferred-longitude calculation for the actual
phase gives

    leading [T Z_chi(0)/Z_chi(0)]=L_geom(M).

Indeed the full critical gradient vanishes on the framing torsor,
so the critical action has zero derivative in both frame directions.
Its meridian derivative at fixed `chi` is therefore the same marked
longitude derivative as on the unframed geometric branch. The
transverse amplitude is a unit and does not alter this leading
ratio. Equation (4.3) now gives

    d_cl(M,Ahat,Bhat,L_geom(M))=0.                (5.1)

The two selected flow coordinates are etale coordinates on the
framing torsor. Consequently their values range over a dense open
part of a two-dimensional frame space over the geometric branch.
Equation (5.1) is therefore a relation over the purely transcendental
frame coefficient field, not only at one frame.

Let `A_geo(M,L)` denote the irreducible rational polynomial defining
the Zariski closure of the marked geometric longitude branch, in
the same sign, inverse and preferred-longitude convention. Its
irreducibility is preserved by the independent transcendental frame
variables. Clearing peripheral denominators in (5.1) proves

    A_geo(M,L) divides d_cl(M,Ahat,Bhat,L)

over `Q(Ahat,Bhat)`, up to the recorded monomial and lift gauges.
This is the claimed geometric-support theorem. In particular the
constructed operator has positive meridian-shift order; a nonzero
order-zero rational multiplier cannot annihilate this nonzero
formal period on a dense open chart.

The whole construction of `Dhat` uses actual finite coefficients,
global boundary linear algebra, central specialization, and
transverse moment extraction. It never multiplies an operator by
an independently supplied `A_geo`.

### The actual certified module has a formal geometric line quotient

There is a corresponding precise formal torsor statement. Let `K_geo`
be the algebraic function field of the marked geometric gluing branch
and its two retained framing coordinates, with the recorded
half-density and sign covers. Put `h=Log q`, and let `Z_geo^chi`
be the nonzero transverse block just constructed. On this field the
shift is the formal automorphism `sigma=exp(h delta)`, where
`delta=M partial_M` fixes both framing coordinates and extends
uniquely to the algebraic and half-density covers in characteristic
zero. Its shift ratio

    b_geo=T(Z_geo^chi)/Z_geo^chi
          in K_geo[[h]]^*, b_geo|_(h=0)=L_geom

has algebraic coefficients. The meridian-independent base-only line
cancels in this ratio. The exponent difference has leading `Log L`,
and its higher derivatives are algebraic after exponentiating that
leading logarithm; the transverse amplitudes and all their meridian
derivatives are algebraic as proved in the normal-period calculation.

Right division in the meridian Ore ring over `K_geo((h))` gives

    Dhat=Q_geo (T-b_geo)+r_geo.

Applying this to `Z_geo^chi` gives `r_geo Z_geo^chi=0`. This period
is nonzero in its formal exponential line, so `r_geo=0`. Thus
`T-b_geo` is a right factor of an operator constructed from actual
partial arrays. Equivalently its cyclic module has a formal rank-one
quotient on the marked geometric branch. It is not asserted to be
a rational generic factor or a quotient of the minimal full scalar
operator.

The action of this line is the marked actual crossing regulator
action: in the `h` convention its complete imaginary value is
`Vol/2`, with the original peripheral and base-only lines retained.
The existing formal Gaussian comparison transports it to the positive
triangulation's marked regulator line by an algebraic formal unit.
No convergence, rootwise value of that formal unit, or nonzero
coefficient in the selected scalar period follows from this factor.

In fact every nonzero moment operator obtained from a whole
partial-array certificate by this procedure annihilates the same
formal block. Their generated left ideal in the localized meridian
Ore ring over `Q(q,M,Ahat,Bhat)` is nonzero. Every element annihilates
both the actual partial arrays and the formal block. Its unique monic
least-order generator consequently also has a geometric classical
factor after taking its first nonzero `(q-1)` symbol. This defines a
minimal **certified partial** operator; it is not asserted to equal
the minimal annihilator of one selected scalar solution. Clear its
coefficient denominators in a polynomial Ore combination before
evaluating discrete frame labels; this retains identities also at
labels where the localized formula itself has a pole.

The full literature normalization is transported exactly, if desired.
For the full partial array `N_N^chi=d_N(M)F_N^chi`, retain

    d_N(M)=i^(N+3)M^(N-1)/(1+M^2+...+M^(2N-2)),
    g_N(q,M)=d_N(qM)/d_N(M)
       =q^(N-1)(q^2 M^2-1)/(M^2-1)
                         * (M^(2N)-1)/(q^(2N)M^(2N)-1).

At the ACTUAL root q^N=-1 its meromorphic meridian-germ restriction is

    g_bar(q,M)=-q^(-1)(q^2 M^2-1)/(M^2-1).

The constructed full ROOT operator is the Ore gauge

    Dhat_full=Dhat|_(T -> g_bar^(-1) T).

This notation means ordered Ore substitution, not commutative
substitution of powers. Its all-level identity is a meromorphic
whole MERIDIAN-germ identity ON THE ROOT FIBERS, with the complete
displayed `d_N` retained. For a whole quantum-normal source use
g_N, or its actual independent powers z=q^N,w=M^(2N), before
specializing. The expression g_bar is only its root restriction;
their q-normal derivatives are not identified. Equivalently,

    g_N=q^(-1)z (q^2 M^2-1)/(M^2-1)
                                        * (w-1)/(z^2 w-1).

Here the actual meridian step sends w to z^2 w. It is not a
constant dual-nome coordinate off the root. Also g_N has limit
+1 at q=1 with N FIXED, whereas the root-character-specialized
g_bar below has limit -1. These are different classical regimes;
the root-symbol statement is not a claim that their fixed-N
whole quantum-normal symbols agree.

The [independent peripheral-shift audit](full_peripheral_shift_root_and_normal_audit.md)
checks this full ratio, the ordered gauge direction and its
retained-character normal discrepancy explicitly.

At generic classical `M`, `g_bar->-1`, so its geometric factor is
`A_geo(M,-L_full)` in the full shift convention. The regular
completion at `M=1` uses the original source lattice and complete
normalization germ; the separate pole of the localized `g_bar` is not
evaluated there.

## 6. Scope of the result

The proof applies to every knot for which the audited regular
geometric critical chart and Hessian-radical statement hold. In
particular its braid complexity is unrestricted: it is not confined
to two-bridge, twist, alternating, or a fixed bridge number. The
geometric input and the retained SL2 sign cover are exactly those
of the actual normal-period theorem; no literature asymptotic
or creative-telescoping theorem is a premise.

The finite partial state and its operator depend on the braid and
the selected two flow coordinates. They have been constructed from
the original coefficient model; no topological invariance of this
two-index extension is asserted. Summing its remaining two indices
with the original selected source requires further elimination.
The geometric factor can be lost in that pushforward. The theorem
does not identify the full scalar minimal quantum-A operator, the
selected global geometric cycle, Kashaev's volume growth, or the
value of any individually normalized compact product at a root.

## 7. A source-preserving Fourier partial family has the same geometric factor

There is now a second actual partial family with a different and
useful framing polarization. It requires the FULL four-port tensor,
not only its double diagonal. Use the original first-cut rank-one
source and Fourier-transform the second identity wire as in
[the whole polarization construction](actual_two_cut_fourier_polarization_and_cap.md).
At a primitive root put V_jb=Q^(jb), with V^(-1)_bj=Q^(-bj)/N,
and T^V=(I tensor V)T(I tensor V^(-1)). Define the RAW partial
family by

    Ftilde_N(M;a,j)=sum_c (T^V)_(c,j;a,j)
       =(1/N)sum_(b,nu,u) Q^(j nu) W_N(M;a,b,nu,u). (7.1)

Here W_N is the original raw open coefficient on its integral
flow coset, T_(a-nu,b+nu;a,b)=sum_u W_N, and u has m-1 internal
chord coordinates. All four actual port bounds and every original
phase/pivot/peripheral line remain in W_N. The Fourier factor 1/N
in (7.1) is not the first-cut source normalization. The original
selected scalar is exactly

    F_N(M)=(1/N)sum_(a,j) Ftilde_N(M;a,j).         (7.2)

Indeed the sum over j kills every nonzero offset nu in its actual
range |nu|<N and restores the identity second closure. It does not
replace the physical b sum by evaluation of a momentum function.
Equivalently, partial trace on that wire is invariant under the
whole invertible basis change. If its first cut were also made
diagonal BEFORE this operation, charge conservation would force
nu=0, and the resulting array would be independent of j. The sum
over c in (7.1) is essential.

The following assertions hold under the regular geometric input
of this note.

**Fourier partial support theorem.** There is a nonzero all-level
meridian operator constructed from (7.1) by finite coefficient
linear algebra and moment repair, whose first nonzero classical
symbol contains the same marked geometric A-factor. On a dense
geometric framing chart its nonzero normal block is parametrized
by the original cut position and the second physical wave
momentum. At the discrete-faithful complete point these are
birational framing coordinates; no new quadratic framing cover
is required. This does not assert a geometric factor after the
final selected sum (7.2).

Here is the certificate and specialization proof, including the
distinction between root data and the whole q-normal source.

First keep a,j external and b,nu,u internal. Their number is
r_F=m+1. Removing both physical cuts leaves the same connected
graph, so the integral tree particular flow makes W_N proper
with linear finite support, exactly as in the two-cut proof.
The added monomial Q^(j nu) is also proper: shifting nu multiplies
it by the external character Q^j, and shifting any remaining
flow has its stated rational coefficient. There is a nonempty
strict cone: take all original transfers small and positive,
the original positions near N/2, and the open offset nu in a
sufficiently small two-sided interval about zero. The Fourier
index j may independently range through a strict subinterval
of its original head.

The formula on the right of (7.1), with the same monomial
Fourier kernel at generic q, is a convenient AUXILIARY whole
coefficient lift. At every root it is the literal actual family.
Its common factor 1/N can be kept as a source line or removed
from a homogeneous coefficient certificate, since internal and
meridian shifts fix it. The finite support-stratum count of
Section 2 applies with r replaced by r_F and the second external
character replaced by q^j, retaining its square-root mark when
required. Thus a nonzero whole certificate with no internal
multiplication characters exists. Strip its largest common
q^N+1 power from the ENTIRE certificate before root evaluation.
The least internal-shift moment then gives a nonzero meridian
operator annihilating the actual root arrays (7.1), by the exact
same zero-extended summation identity as Sections 2--3.

This auxiliary lift is not identified with the actual generic-q
inverse Fourier matrix. The source-preserving whole basis change
uses the Vandermonde V(Q) and its Lagrange inverse, with their
explicit connection and endpoint carries. Its inverse equals
Q^(-bj)/N at the root but generally has different normal jets.
Thus the argument proves an operator identity for the literal
ALL-LEVEL ROOT partial family; it does not discard the source
normal terms in the whole polarization theorem. All M-dependent
identities at a fixed root still agree, since the two Fourier
bases are independent of M.

The geometric normal block comes from the macroscopic open
coefficient phase, rather than extrapolating a bounded-band
Taylor formula to offsets of order N. Put t=H nu, v=Hj. Its phase
is

    Phi=S_open(a,b,t,u)+v t.                      (7.3)

On the original geometric critical manifold t=0, the old internal
equations hold and partial_t S_open=Log p_e, in the actual
balanced boundary frame. Therefore (7.3) is stationary precisely
on the selected geometric germ with

    v=-Log p_e,   eta=exp(v)=p_e^(-1).

The original cut position together with p_e is etale on a
nonempty geometric open chart. The bordered-Hessian proof in
[the Fourier normal-block theorem](actual_fourier_polarized_geometric_normal_block.md)
then gives a nondegenerate (m+1)-dimensional internal Hessian.
Its mixed entry along the old fixed-cut framing tangent is the
nonzero derivative of Log p_e. The added Fourier pair has its
literal factor 1/N and supplies no new exponential action.
The geometric critical value is still S_geo, since t=0.

The auxiliary coefficient realization has the same exact proper
ratios and full marked formal phase (7.3). It consequently has
a nonzero formal Gaussian block. Translate its internal variables
in the whole certificate and extract the least weighted moment
as in Section 4. The operator obtained from the finite root
arrays annihilates that SAME normal block. Section 5 now applies:
its first nonzero classical symbol vanishes at the marked
geometric longitude and has the geometric A-factor. The formal
Ore right-factor statement follows by the same division argument.

The original peripheral dimension line is transported using the
ordered Ore gauge already displayed above. Its separate whole
normal adapter is not replaced by a root norm in this proof.
Nor is the sum over j interpreted as the old cap point eta=0:
the correct new source is the finite j sum in (7.2), with every
tail/carry retained on inserted currents. Survival and the volume
norm after that last sourced pushforward remain unproved.

## 8. The original root period has a one-exterior-index Fourier presentation

One of the two exterior sums can be removed EXACTLY, without
replacing the first-cut source by a double diagonal. The
[fixed-column/Ward theorem](actual_one_index_fourier_source_and_ward_reduction.md)
proves that the fully reclosed one-cut word C_N(M) is scalar on
the actual root family. This follows directly from its true K,F
intertwining: K has distinct eigenvalues and F connects all
successive head basis vectors with nonzero coefficients. Hence
every first column sum is the same selected scalar. In the RAW
Fourier presentation above,

    sum_j Ftilde_N(M;a,j)=sum_c(C_N(M))_(c,a)=F_N(M)
                       for EVERY a in [0,N-1].                (8.1)

The full peripheral factor, if present, multiplies both sides as
its original line. Equation (8.1) keeps the sum over c in (7.1).
Replacing it by c=a before Fourier polarization would destroy
the momentum coordinate and is a different operation.

This statement also has a controlled WHOLE source defect. The
whole actual balanced K,F Ward contraction gives

    h delta C=C-I Tr(C)/N,
    delta C=((Ad K-I)C, F C-K^(-1)C K F).

If lambda_a(C)=sum_c C_(c,a) and Phi is the original rank-one
average, then (lambda_a-Phi)(I)=0 and therefore

    lambda_a-Phi=(lambda_a-Phi) h delta.            (8.2)

Its primitive and the original source adapters are explicit in
the fixed-column theorem. Thus (8.1) is not extended to an
arbitrary off-root lift by setting its Ward defects to zero.
The actual whole normal derivatives act on every term of (8.2).

There is a uniform way to fix a good interior sequence of first
input indices while retaining the geometric normal block. The
bad first-position fibers of its nonempty algebraic open chart
form a FINITE set: after writing its finitely many shape/Jacobian
units as rational functions of the first position and momentum,
an entire fiber can fail only at a common zero of their nonzero
coefficient functions. Also exclude the finitely many first
half-phases where the already constructed operator's nonzero
leading symbol becomes identically zero in M, the second
exterior character and L. Clearing the specified denominators
first makes this an ordinary polynomial coefficient test.

Choose a rational theta=k/d in (0,1) such that

    A_*=exp(2pi*i*k/d), alpha_*=exp(pi*i*k/d),

avoid these finite bad sets, including A=1. Such a choice exists
because these algebraic phases are infinite. Put

    a_N=floor(kN/d), r_N=kN modulo d.

At the original root its physical and half clocks are EXACTLY

    A_N=A_* q_N^(-2r_N/d),
    Ahat_N=alpha_* q_N^(-r_N/d).                  (8.3)

These indices are in the strict interior for all sufficiently
large N. For each fixed residue class r_N=r the right side is
one fixed algebraic q germ on a marked d-th-root cover, and it
tends to the chosen good geometric framing phase. The same
nondegenerate normal block therefore persists there, with its
original geometric action.

Substitute Ahat=alpha_* q^(-r/d) in the operator of Section 7,
after its stated coefficient localization. This is an Ore
homomorphism because the meridian shift fixes q and both
exterior frame characters. By the choice of alpha_* its first
nonzero classical symbol stays nonzero and still has the SAME
geometric A-factor. On N residue class r the specialized operator
annihilates the actual one-index partial family

    G_(N,r)(M;j)=Ftilde_N(M;a_N,j),
    F_N(M)=sum_j G_(N,r)(M;j).                    (8.4)

Its formal geometric line is now over the marked geometric
representation field and ONE momentum coordinate. No restriction
to a knot family or bridge number has been introduced. The
values G_(N,r) still contain the original bulk finite contractions;
this is one exterior source index, not an asserted closed
single-product formula for the knot invariant.

For a WHOLE quantum-normal source calculation, (8.3) must not
freeze the underlying power coordinates. Before root restriction,
the actual fixed-N clocks are

    A_N=(Q^N)^(k/d) Q^(-r/d),
    Ahat_N=(q^N)^(k/d) q^(-r/d),                  (8.5)

with the logarithmic/finite-cover marks Log(Q^N)=N Log Q and
Log(q^N)=N Log q. Their root values give (8.3), but their normal
derivatives retain the N terms. The operators in (8.4) are
certified ALL-LEVEL ROOT operators, as in Section 7; no whole
q-normal identification is inferred from (8.3).

If one wants a single operator across these finitely many residue
classes, take a common LEFT multiple of their nonzero specialized
operators in the localized meridian Ore ring and then clear the
original denominators. A naive ordered product is not justified.
The per-residue statement (8.4) already suffices for the present
source reduction. It still does not prove that the final one-index
sum retains its geometric block with the regulator norm. That is
the remaining selected-period theorem.

The [actual Fourier current theorem](actual_fourier_source_cancellation.md)
now provides a rigorous scope test for this last step. The literal
second-port Cartan current has zero whole second partial trace,
yet on the good-A chart its formal geometric block is a nonzero
derivative of the block above with the SAME action. Its own
partial certificate still has a geometric classical factor, while
its selected scalar is identically zero. Thus a geometric partial
factor is not a certificate of survival under the last source.
The final theorem must control the actual class in the cyclic
source/current quotient, including the polar and normal data.
