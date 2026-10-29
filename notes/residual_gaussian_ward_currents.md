# Residual Gaussian Ward currents and the cyclotomic source resonance

Research proof and audit, 27 October 2026. At COMPLETE color, the
literal local currents and explicitly computed cut boundary rows
give an all-order transverse Gaussian Ward ideal on the geometric
framing torsor. It is a flat rank-one ideal, with the actual Gaussian
amplitude as its nonzero horizontal generator. The original cut
co-source has precisely the leading covariance required by the
uniform Gaussian density. These formal statements do not identify
the global finite framing contraction. An explicit cyclotomic
resonance obstructs a naive extension to that source; keeping the
whole power normal gives a separate exact divided-current/source
comparison.

## 1. An explicit operator on the actual transverse block

Use the actual independent flow coordinates of
[the partial support theorem](partial_geometric_support_theorem.md).
Keep two coordinates `chi=(chi_1,chi_2)` external, and contract the
other `r=m-1` logarithmic coordinates `u` by the nondegenerate
geometric Gaussian. Write `H=Log Q` and

    I=C_beta(H) exp(S/H) a(chi,u,H),
    Z(chi,H)=G_chi(I).

All original characters, half-steps, pivots and base-only factors are
kept. The normalized moment of a regular insertion is

    E_chi[h]=G_chi(h I)/Z(chi,H).                  (1)

The denominator is a nonzero formal Gaussian block, not the selected
finite knot scalar. After its recorded common exponential and base
line are factored out, it is a formal unit. Thus every coefficient of
(1) is recursively computable by Wick contraction and finite formal
division, and is algebraic on the stated geometric/half-density cover.

Compose the literal local currents in
[the crossing-current note](local_r_ward_transfer_currents.md), keeping
their multiplication insertions. Use the same unimodular integral
closure solver as for the actual flow coordinates. Every resulting
interior term has the explicit form

    h_(gamma,beta)(chi,u,H) T_chi^gamma S_u^beta I,

where the shifts translate logarithmic coordinates by `H` times
their displayed integer vectors. Transverse translation gives its
exact Gaussian image

    E_(chi+H gamma)[S_u^(-beta)h_(gamma,beta)(chi,u,H)]
                                      T_chi^gamma Z.           (2)

The proof is the literal substitution `y=u+H beta`, with the
critical point recentered at the unique corresponding branch.
The insertion is shifted in the opposite direction; it may not be
replaced by its unshifted value. External base substitution commutes
with the finite Wick recursion. Summing (2) defines an explicit
all-order residual difference operator for each composed current.
It annihilates `Z` whenever the corresponding interior current
identity is zero. Finite endpoint indicators remain their separate
source terms; they have not been given a fictitious value in this
interior completion.

For the two full-tensor Hopf-adjoint combinations

    2(ad_K-I)+2 ad_Ecal,       ad_F+ad_Ecal,

the already proved moment-map calculation gives the two cut-Borel
principal fields `A(h_sl+2f_sl)` and `A(e_sl+f_sl)`. Formula (2)
transports each term of their interior current equations. The
marked `e,D` coupon is not Hopf invariant, so its cut boundary
insertions must also be written and transported. The next section
does this explicitly at complete color. The generic-M endpoint
terms are retained and are not covered by the homogeneous
complete-color assertion.

## 2. Gaussian covariance supplies genuine quantum corrections

The map (1) is linear, not multiplicative. This matters even in the
coherent all-level interior model. If `H_perp=S_uu` is the critical
Hessian, direct quadratic Wick contraction gives

    E[fg]-E[f]E[g]
      =-H (partial_u f)^t H_perp^(-1)(partial_u g)+O(H^2),     (3)

for H-independent regular insertions, evaluated at the critical
point. The sign comes from covariance `-H H_perp^(-1)` for the
phase convention `exp(S/H)`. Cubic-phase and amplitude-drift terms
cancel from this covariance at first order.

Consequently replacing each coefficient of a product or bracket of
Ward currents separately by its scalar expectation is incorrect.
Formula (2), applied to the whole ordered term with all insertions,
retains these corrections. This is different from the impossible
product-preserving fixed-root matrix-to-scalar map.

## 3. The actual complete cut co-source matches the principal density

The missing cut terms can be calculated directly, without postulating
a Haar form. For `Phi(C)=Tr(e C)`, cyclicity gives the exact dual
Hopf rows

    e_K=K^(-1)eK-e,
    e_E=K^(-1)eEcal-Ecal K^(-1)e,
    e_F=eF-KFeK^(-1).

Thus `Phi((ad_K-I)C)=Tr(e_K C)` and similarly for the other two
generators. The actual one-cut operator has diagonal support
term by term, before the remaining internal sums, by total-index
conservation. Only the diagonals of these rows contribute.

Use `A=Q^a`, `k_a=xQ^(-a)`,
`epsilon_a=M Q^(-a)-M^(-1)` for `1<=a<N`, and actual endpoints
`epsilon_0=epsilon_N=0`. Direct multiplication gives

    (e_K)_aa=0,
    (e_F)_aa=(1-Q)A/N,
    (e_E)_aa=(Q-1)A/(N M x)
          +kappa(1_(a=N-1)-1_(a=0))/(N x).        (3a)

For example the E diagonal is
`[epsilon_a/k_a-epsilon_(a+1)/k_(a+1)]/N`; the displayed two
endpoint corrections are exactly what replacing the actual truncated
edges by their interior formula would miss.

At complete color `M=1,x=-q^(-1)`, these simplify exactly to

    (e_E)_aa=q(1-Q)A/N,
    (e_F)_aa=(1-Q)A/N.                           (3b)

If the original scalar summand already includes its `1/N`, the
boundary multiplication coefficients of the two displayed cut-Borel
combinations are therefore

    b_1=2q(1-Q)A,
    b_2=(1+q)(1-Q)A.

Both have `b_i/H -> -2A` as `H=Log Q` tends to zero. These are
literal co-source contributions, not guessed scalar connection terms.
Choosing the external pair to contain the actual cut index is always
possible: its differential is nonzero on the framing torsor, and
one more actual coordinate completes it to an etale pair.

The matching geometric divergence is equally explicit. At `M=1`
right multiplication of
`F(r,s)=[r,1-r;s,-s]` by a row-stochastic frame change has fields

    X_a=r partial_r+s partial_s,
    X_b=(1-r)partial_r-s partial_s.

The conjugation convention `delta G=[xi,G]` gives

    xi_1=A(h_sl+2f_sl)=-2X_b,
    xi_2=A(e_sl+f_sl)=X_a-X_b.

Explicitly both traceless matrices have eigenvalue one on `(1,1)`.
Subtracting `I` gives the row-sum-zero matrices with parameters
`(a,b)=(0,2)` and `(-1,1)`, respectively, and normalized frame
variation is `delta F=-F(xi-I)`. This checks the projective
normalization and the signs in the two fields.

For the actual cut density

    Omega_cut=-dr wedge ds/[s(1+s)], A_cut=1/(1+s),

direct differentiation gives

    div_(Omega_cut)(xi_1)=div_(Omega_cut)(xi_2)=2 A_cut.

Consequently the actual co-source terms satisfy the precise leading
covariance identity

    Lie_(xi_i) Omega_cut+(b_i/H)|_(H=0) Omega_cut=0.           (3c)

The uniform Gaussian density is a nonzero base-only multiple of this
form, so it obeys the same identity. This proves the principal source
covariance with the original cut. It does not yet prove that all
finite normal/endpoint insertions have the required all-order image.

## 4. The complete residual current ideal is a flat line

### The actual graph current and its first-order field

Use the local current identities with the input/output operator
order fixed in the crossing-current note. Pair adjacent edge
insertions along the braid. Every reindexing is retained as its
finite difference current. The elementary product rule is

    j T^v c-(T^(-v)j)c=(T^v-I)[(T^(-v)j)c].

It fixes the sign and placement of each resulting boundary
multiplier. The actual pivotal caps cancel the
matched Hopf-adjoint insertions; their remaining boundary is
exactly the dual cut row computed in Section 3. The determinant-one
flow solver expresses all translations in the independent actual
flow coordinates. This gives scalar divergence identities with
the boundary coefficients `b_i` included. A translation by an
integer vector can be written as a sum of coordinate differences
by telescoping its steps, so no nonintegral current is introduced.

At COMPLETE color these are homogeneous equations on the original
scalar array after the explicit boundary term is brought to the
same side. Each multiplier is `N diag(e_h)`, since the scalar
summand already contains `1/N`. At generic `M`, equation (3a)
instead leaves the two specified kappa-endpoint currents. They
must not be omitted by continuity from the complete value.

Here is a direct principal-field proof, beyond just identifying
the full End-space Hopf symbols. For a local observable

    h(q,T)=sum_v h_v(q,H) T^v,

acting on a generating kernel `exp(S/H)a`, its first
amplitude-derivative coefficient is

    sum_v h_v(q,0) exp(v dot p) v=partial_p h_cl.

This follows by first-order Taylor expansion of each shifted
amplitude. The right kernel action uses the opposite input
translation; therefore its commutator gives the position velocities
of the corresponding Hamiltonian field on the canonical graph.
The zero-order first correction is carried by the current's
amplitude and boundary terms; it is not used to determine these
vector coefficients.

At a crossing with actual update
`q_out=P q_in+R k`, the transfer velocity is uniquely obtained from
that crossing's two output velocities. For example, in the positive
update `(a,b)->(b+k,a-k)` it is simultaneously
`k_dot=c_dot-b_dot=a_dot-d_dot`; equality follows from conservation
of the local total position. The negative update gives the same
statement with the prescribed signs. Determine this velocity
crossing by crossing, then compose. This avoids trying to solve
an underdetermined whole-word position equation.

Restrict to the complete critical germ. The exact critical-scheme
correspondence identifies this propagated Hamiltonian variation
with infinitesimal conjugation of the framed representation. For
the two compensated cut-stabilizer combinations it is exactly
`xi_1,xi_2` above. The `ad_K` part alone can have zero position
projection; no independent field is inferred from it alone.
The compensated fields are tangent to the full critical framing
surface. Since the retained actual coordinates are etale there,
their two projected velocities are independent.

Transverse Gaussian pushforward evaluates the leading velocity
coefficients at the critical point and kills the transverse total
currents. Formula (2), together with the explicit complete boundary
weights, therefore constructs two homogeneous residual operators
with these independent first-order vector fields. Their scalar
leading term agrees with (3c). All higher coefficients are given
by the same actual normalized moments, with the boundary terms
still included. No separate scalar Ward character was assumed.

### Exact operator-ideal reduction

Here is the exact operator-algebra reduction, without assuming
multiplicativity of (1). Factor the framing-independent action and
base line from `Z`, leaving an algebraic formal amplitude

    z(chi,H) in K_geo[[H]]^times.

The full critical action has zero derivatives along the framing
torsor, so it cancels from external framing shifts. Let `Wbar_1,2`
be the complete-color residual operators just constructed, normalized
by their common `H`. Expand their external shifts as formal
differential operators; each H coefficient has finite differential
order. Conjugate by the computed actual amplitude:

    P_i=z^(-1) Wbar_i z.

Then `P_i(1)=0`. Right-normal ordering in commuting etale framing
derivations writes, exactly,

    P_i=sum_(a=1)^2 A_ia(H,partial_chi) partial_(chi_a),
    A_ia(0)=xi_i^a.

The leading 2 by 2 matrix is invertible on the framing chart.
Its inverse in the H-adically completed matrix algebra of
differential operators is the convergent Neumann series. Hence

    partial_(chi_a)=sum_i (A^(-1))_ai P_i.

Conversely every `P_i` is a left differential-operator combination
of these derivatives. Thus the residual current left ideal is
precisely the annihilator ideal of the constant line after this
gauge. Ungauged it is the flat connection

    nabla_a=partial_(chi_a)-partial_(chi_a)Log z.                (4)

Its flatness follows by direct commutation of logarithmic
derivatives. This identifies the resulting complete-color
formal Ward **ideal** and its cyclic rank-one module. Every other
residual current annihilates `z` and hence belongs to this same
annihilator ideal. It does not assert that separately
expectation-substituted generators obey an undeformed Borel
bracket, or that their full relation complexes have already been
identified with the finite-source Ward complex.

The uniform principal-density theorem gives
`Omega_perp^2=-(T_beta/2)Omega_cut^2`. With the recorded square-root
mark, the leading framing density is a base-only nonzero multiple
of `Omega_cut`. Consequently (4) has that canonical leading
trivialization. Its higher gauge coefficients are the actual
Gaussian coefficients, rather than freely chosen transport data.

## 5. Why this interior comparison does not extend coefficientwise to the source

Even one frame direction detects the missing completion. For the
Euler derivation `D=A partial_A`, ordinary formal shift-to-current
comparison uses

    exp(H D)-1=H D B(H D),
    B(v)=(exp(v)-1)/v, B(0)=1.                    (5)

On the local stationary formal completion, the corresponding
operator has positive stationary degree, so the Bernoulli adapter
`B` is a unit. On a cyclotomic carry sector `A^N`, with
`H=2pi*i/N`, it instead has

    B(H D) A^N=B(2pi*i) A^N=0.                  (6)

The ordinary Euler current there is nonzero. These sectors are
not regular coefficients in the same WKB line: `A^N` is an extra
exponential character when `N=2pi*i/H`. Thus the local formal
current isomorphism cannot be extended by the same invertible
adapter while preserving the literal finite carry source.

Deleting `A=1` by the proved relative-Ward homotopy does not remove
this resonance. The relation `A^N=U` and its whole normal remain
on the retained source. Nor does the normalized moment (1) control
spectral degree near `N`, endpoint currents, or exponentially small
local functions with a different global cut pairing.

## 6. The divided Frobenius current gives the exact normal repair

The necessary extra direction can be computed, rather than
postulated. Retain

    C_U=k[U^+/-1,A]/(A^N-U).

Unfold the shift coherently by

    sigma_Q(A)=Q A, sigma_Q(U)=Q^N U.

It preserves the relation. At `Q=zeta` its `N`-th power is identity.
Before specializing put `delta=1-Q^N`. Then

    sigma_Q^N(A)=(1-delta)A,
    sigma_Q^N(U)=(1-delta)^N U.

Therefore on every Laurent polynomial, and hence every regular
whole normal germ, the exact divided normal is

    [(sigma_Q^N-I)/(1-Q^N)]_(Q=zeta)=-D_phys,
    D_phys=A partial_A+N U partial_U.             (7)

The derivation preserves `A^N-U`. It does not descend to the fiber
`U=1`: `D_phys(U-1)=N U` is nonzero there. This proves precisely
which normal datum a fixed-fiber framing derivative would discard.

Let `tau_N=Tr_(C_U/k[U^+/-1])/N`, the original averaged cut on this
whole finite algebra. In the canonical basis `1,A,...,A^(N-1)`,
`tau_N(f)=f_0(U)`, so direct coefficient differentiation gives

    tau_N D_phys=N U partial_U tau_N.             (8)

This is an actual source-current chain map with all carries retained.
It also extends coefficientwise through the polynomial relative
source resolution and its endpoint transgression.

More explicitly mark `alpha(U)^N=U`, `alpha(1)=1`, and use the
evaluation branches `A=alpha(U)zeta^a`. In this basis `D_phys`
is `N U partial_U`. On matrix families it gives the induced
connection on endomorphisms. The coefficientwise extension of
the original head projector `e` is constant. The whole-normal
pivot has two distinct marked lifts:

    K_U=x A^(-1),
    g_red=x^(1-N)A^(-1), g_lit=K_U^(1-N)=U g_red,
    D_red=g_red^(-1)e, D_lit=U^(-1)D_red.

Only g_lit is the literal clock power away from U=1. Their
physical normal rates are

    D_phys(g_red)=-g_red, D_phys(D_red)=D_red,
    D_phys(g_lit)=(N-1)g_lit,
    D_phys(D_lit)=-(N-1)D_lit.

Both products are exactly e, so their paired cut has the same
normal covariance. Their separate pivot/source jets differ by
the retained U adapter and must not be identified from the
common root value.

Thus for the **original** marked matrix cut,

    Phi_U(D_phys C)=N U partial_U Phi_U(C),
    Phi_U(C)=Tr(g_red D_red C)
             =Tr(g_lit D_lit C)=Tr(e C).         (9)

No Haar division or normalization replacement is used. This e is
the coefficientwise whole-normal projector, not the finite-rank
Verma coupon Gamma=i e pi_0. Under the explicit
[Mellin comparison](fock_cyclic_normal_mellin_map.md), those act
respectively as tau_N(f)1 and [tau_N(f)]_(U=1)1. The latter has
the additional normal row
[nabla,Gamma_U]f=-[tau_N(nabla f)]_(U=1)1, nabla=D_phys/N.
Equation (9) does not discard that finite-vacuum cut derivative.

The boundary split Ward complex can be carried along this normal
connection as well. On degree zero use the displayed derivative;
on its image degree one define
`nabla^1(delta_W C)=delta_W(D_phys C)`. It is well defined because
`ker delta_W` is the scalar line, which the derivative preserves.
The explicit splitting makes this a strict normal current map on
the relative-Ward boundary complex. Its degree-one action is not
an uncorrected entrywise derivative of the varying K,F Ward rows.

## 7. Exact scope of the new comparison step

Equations (1)--(2), the explicit complete dual rows, and the
principal-field proof construct the complete-color all-order
residual Ward ideal. Equation (3c) identifies the original cut's
leading covariance with the Gaussian framing density. Equations
(7)--(9) independently identify the divided Frobenius normal current
with the literal whole cut source, including `g,D` and endpoint
transgression. These are proved pieces of the needed comparison.

They are not yet a map between those two completed modules.
The interior connection is over a single geometric WKB sector;
the whole source carries the resonant exponential characters and
normal modes exposed by (6)--(7). A source-compatible extension
must transport these sectors, not replace the adapter in (5) by
a unit outside its domain. The explicit marked transgression
therefore does not yet prove that this residual geometric class
has nonzero image under the selected finite cut. No nonzero
selected global cycle, Stokes coefficient, or volume limit follows.

[Exact source audit](../experiments/audit_residual_ward_source_covariance.py)
and [results](../experiments/residual_ward_source_covariance_results.json)
check the actual complete/generic-M boundary rows, both geometric
divergences and field independence, and whole-normal Euler/carry
identities. The all-order current/ideal argument above is a proof,
not inferred from these finite diagnostics.
