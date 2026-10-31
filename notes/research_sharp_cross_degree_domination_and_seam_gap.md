# Sharp CROSS-degree domination and a uniform original seam gap

31 October 2026. The comparison is between the explicitly defined sharp functionals. It does not turn a coefficient limsup into a coefficient limit. The global coefficient upper theorem supplies the finite source consequence at both parities and all spectral boundaries.

## 1. The full closed-domain functional

Use the original local degree order q=(q_x,q_b,q_c,q_y), q>=0 and
sum q=1, and put

    mu=q_b, nu=1-q_c, xi=q_x, 0<=xi<=nu-mu.

The CROSS degree closure is

    0<=mu<=1/2<=nu<=1.                               (1)

This is a condition on the original four degrees. It does not assign a
finite coefficient to a new path label at a seam. For 0<=delta<=1/2 use
exactly the full sharp functional in the global coefficient theorem:

    alpha_delta(t)=2cos(2pi t)+2cos(2pi delta),
    Lambda_delta(t;x,y)=2sin(pi t)
      *[(x+y)sin(pi t)
             +sqrt((x-y)^2 sin^2(pi t)+4xy cos^2(pi delta))],
    B_delta(mu,nu)=int_0^mu log|alpha_delta(t)|dt
                              +int_nu^1 log|alpha_delta(t)|dt,
    H_delta(q)=B_delta(mu,nu)
       +inf_(l in R){int_mu^nu log Lambda_delta(t;exp(l),1)dt-xi*l}. (2)

All integrals include their actual unused rows. The logarithmic
singularities are integrable. H is continuous on the entire closed
simplex and spectral interval by the proved uniform tilt-clipping
argument, including xi=0,nu-mu, diagonal rows, protected coordinates,
and delta=1/2.

**Theorem.** On (1), for every real spectrum,

    H_delta(q)<=H_0(q)=h(q),                         (3)

where h is the original continuous complete-endpoint coefficient entropy.
In fact H_delta(q) is nonincreasing as delta goes from0 to1/2 for each
fixed CROSS degree vector q. No sampled finite product is divided by a
zero, and no coefficient lower asymptotic is used.

## 2. The unused products are maximized at the complete spectrum

Set f(t)=log|2cos(pi t)|, as a locally integrable, even, one-periodic
function. Its value is a decreasing function of dist(t,Z) in[0,1/2].
For 0<=a<=1/2 define

    J_delta(a)=int_0^a log|alpha_delta(t)|dt.

The exact factorization alpha_delta(t)=4cos(pi(t+delta))cos(pi(t-delta))
and evenness of f give, with NO extra constant or factor two,

    J_delta(a)=int_(delta-a)^(delta+a) f(t)dt.        (4)

For fixed a this moving integral is absolutely continuous in delta,
because f is locally L1. Almost everywhere,

    partial_delta J_delta(a)=f(delta+a)-f(delta-a).  (5)

If a,delta belong to[0,1/2],

    dist(delta+a,Z)=min(delta+a,1-delta-a)
                                      >=|delta-a|=dist(delta-a,Z).

The first inequality follows separately from delta+a>=|delta-a| and
1-delta-a>=|delta-a|, the latter being equivalent to
1>=2max(delta,a). Thus (5)<=0 almost everywhere. Absolute continuity
retains this sign through the logarithmic singularity at delta+a=1/2.
Consequently

    J_delta(a)<=J_0(a),                             (6)

and, more generally, J_delta(a) is nonincreasing in delta. If a=0 it is
zero. If a=1/2 it is the full-period integral of f, also zero, independent
of delta. For 0<a<1/2 the derivative is strictly negative almost
everywhere in0<delta<1/2, but strictness is not needed below.

On the CROSS domain, alpha_delta(1-t)=alpha_delta(t) and both unused
endpoint lengths are at most1/2. Therefore

    B_delta(mu,nu)=J_delta(mu)+J_delta(1-nu)
                                      <=J_0(mu)+J_0(1-nu)=B_0(mu,nu). (7)

This is where the CROSS degree hypothesis is used. A one-sided row
instead gives a difference of two lower-half prefix integrals; (7)
does not imply the same comparison there.

## 3. The tail comparison and the exact endpoint normalization

For every finite real l and every0<t<1, the displayed positive root
in (2) is nonincreasing in delta, since cos^2(pi delta) decreases.
Thus

    log Lambda_delta(t;exp(l),1)<=log Lambda_0(t;exp(l),1).

Integrate over the same original interval and subtract xi*l. The
inequality holds for EVERY finite tilt, so it also holds after the two
infima over l. Combining with (7) proves H_delta<=H_0. The same argument
between any two ordered spectra proves monotonicity. Integrable endpoint
bounds justify each integral; alternatively the already proved closed
continuity passes from interior row endpoints. No finite minimizing tilt
is assumed when an outer degree is zero or at its full value.

For completeness H_0 in (3) is the actual endpoint entropy, not another
normalization. Put tau=1-nu. Symmetry about1/2 splits the tail integral
into [mu,1/2] and [tau,1/2]. The identity
int_0^(1/2)log alpha_0(t)dt=0 converts each corresponding prefix term
J_0(a) into minus the alpha integral over its active half. Hence

    H_0(q)=inf_l{Phi_mu(l)+Phi_tau(l)-xi*l},
    Phi_a(l)=int_a^(1/2) log[Lambda_0(t;exp(l),1)/alpha_0(t)]dt. (8)

The integrand is exactly the source-normalized endpoint function

    l/2+log tan(pi t)+asinh(tan(pi t)cosh(l/2)).

Its half-interval Legendre entropy is the proved triangle entropy
Ctri(alpha)=V(2pi alpha)/(2pi), with alpha summing to1/2. The infimum
in (8) equals the maximum of the sum of the two such entropies over
xi_1+xi_2=xi and 0<=xi_1<=1/2-mu,0<=xi_2<=1/2-tau. Indeed every split
is bounded above by its value at a common tilt. At a finite minimizing
tilt choose xi_a=Phi_a'(l); this attains equality in both half infima.
The closed endpoint/outer cases follow by continuity of H_0 and of the
triangle entropies and their closed split interval. This is only
one-dimensional outer Legendre convolution, not concavity or duality
in the row endpoints. It gives exactly the published h(q) on CROSS
closure, including both terminal seams and the pure-middle corner.

## 4. A strict gap for all seam-only original shared data

Fix an original simple-white certified marked plat D. Let Q_D be its
actual compact incidence-flow polytope: each port supplies1, each
ordinary face demands1, and both original protected faces demand0.
Let Phi_D=Vol(Y_D)/(2pi). The proved endpoint theorem and unique
geometric maximum give

    max_(q in Q_D) sum_e h(q_e)=Phi_D,
    q_geom is the unique maximizer,
    q_geom,e,b<1/2 and q_geom,e,c<1/2 at EVERY port.  (9)

These assertions retain the actual original marked packing and
matching. They are not claims about a freely chosen incidence graph.
Define the closed seam-only subset

    Sigma_D={q in Q_D: all q_e,b,q_e,c<=1/2,
                         and at least one equals1/2}. (10)

If it is empty, no seam-only candidate exists. There is an explicit
fixed-diagram gap when it is nonempty. Put

    a_D=min_e{1/2-q_geom,e,b, 1/2-q_geom,e,c}>0,
    gamma_D=(pi/2) a_D^2.                            (11)

Here and below ||q-q_geom|| is the Euclidean norm on ALL original
incidence coordinates, namely the square root of
sum_e sum_(f=x,b,c,y)(q_(e,f)-q_geom,(e,f))^2. A shared face's separate
port incidences remain separate coordinates; protected coordinates are
fixed at zero. No norm on the vector of distinct global face sums is used.

To prove (11) is a valid gap, recall the exact triangle entropy
Ctri(alpha)=sum_j f(alpha_j), sum_j alpha_j=1/2, where

    f(t)=[Lob(pi t)+Lob(pi/2-pi t)]/pi,
    f''(t)=-2pi/sin(2pi t)<=-2pi, 0<t<1/2.

Here Lob is the Lobachevsky function in the endpoint triangle theorem.
Its continuous endpoint values extend the resulting strong-concavity
inequality to the CLOSED triangle simplex. The sum over both latent
triangles of every CROSS port is therefore 2pi-strongly concave in the
Euclidean latent incidence norm. The actual linear projection to q sums
the two outer entries and retains each middle entry separately; its
squared operator norm is at most2. Given two feasible q vectors, choose
their maximizing latent allocations. Their convex mixture is feasible
for the mixture of the original q vectors. Applying the latent
strong-concavity inequality and ||P v||^2<=2||v||^2 shows that

    F(q)=sum_e h(q_e)

is pi-strongly concave on the entire closed original CROSS fiber. This
argument also covers a protected monomial half, which has no free latent
coordinate. For any q in that fiber and0<t<1, maximality at q_geom gives

    Phi_D>=F((1-t)q_geom+t q)
      >=(1-t)Phi_D+t F(q)+(pi/2)t(1-t)||q-q_geom||^2.

Divide by t and let t decrease to0. No boundary gradient is needed:

    F(q)<=Phi_D-(pi/2)||q-q_geom||^2.                (11a)

Every seam q has at least one middle coordinate equal to1/2, hence
||q-q_geom||>=a_D. Equations (11)--(11a) give its entropy gap directly,
without an uncomputed seam maximization. The constant uses the exact
normalization Phi_D=Vol(Y_D)/(2pi), and is not uniform over diagrams.

Apply (3) portwise. Uniformly over ALL original spectra,

    max_(q in Sigma_D, delta in[0,1/2]^R)
                  sum_e H_(delta_e)(q_e)<=Phi_D-gamma_D. (12)

In particular a maximum of the sharp functional on the closed non-CROSS
union {q: some q_e,b>=1/2 or q_e,c>=1/2} with value at least Phi_D
MUST have a strictly overloaded middle >1/2. Its possible seam-only
alternative is excluded. This supplies that hypothesis for the existing
restricted-non-CROSS activation and stationary reductions; it does not
settle the remaining strictly overloaded, phase-inconsistent candidates.

There is moreover a UNIFORM fixed-diagram overload margin eta_D>0:

    q in Q_D, max_middle(q)>=1/2,
    sum_e H_(delta_e)(q_e)>=Phi_D
          => max_middle(q)>=1/2+eta_D.                (12a)

To prove this, the set of pairs (q,delta) satisfying the two premises is
closed in a compact space. If it is empty the conclusion is vacuous.
Otherwise none of its points has max_middle(q)=1/2, since such a q lies
in Sigma_D and contradicts (12). The continuous positive function
max_middle(q)-1/2 therefore has a positive minimum on this set. This
also handles an empty Sigma_D: then equality max_middle=1/2 is already
excluded by the flow constraints themselves. Equivalently, a sequence
of high-valued candidates whose maximal middle decreases to1/2 would
have a seam-only limit, contradicting (12). No lower coefficient rate
is used in this compactness argument.

Thus the strict-overload qualifier in the existing high-value restricted
non-CROSS reductions is automatic, with a margin uniform over their
candidate maxima for this one fixed D.

## 5. Uniform finite-source consequence near the entire seam set

Joint continuity of sum H on Q_D times the compact spectral cube makes
(12) stable on a fixed neighborhood. There is rho_D>0 such that

    dist_infinity(q,Sigma_D)<=rho_D
       => sum_e H_(delta_e)(q_e)<=Phi_D-gamma_D/2     (13)

for every q in Q_D and every real spectral vector. This neighborhood
may include actual LEFT or RIGHT degree vectors slightly beyond the
seams; no finite path label is changed. If Sigma_D is empty, compactness
instead gives an empty sufficiently small neighborhood of the seam
conditions, and there is no such contribution to bound.

For each N let a_(e,N)(n_e;delta_e) be the ACTUAL local coefficient,
with the original total degree d=N-1, unused products and raw phases.
Sum over any set of original target arrays n whose EXACT normalized
flow q=n/d lies in the neighborhood (13). The global uniform coefficient
LIMSUP majorant and the polynomial number of arrays at fixed D give

    limsup_(N->infinity) N^(-1)log
      sup_(delta in[0,1/2]^R)
      sum_(such arrays n) prod_e |a_(e,N)(n_e;delta_e)|
                                <=Phi_D-gamma_D/2.    (14)

Empty sums have logarithm minus infinity. In particular the actual
signed sum over those arrays is eventually bounded by
exp{N(Phi_D-gamma_D/3)}. This includes both parities, composite levels,
all protected/row/spectral boundaries and sampled spectral zeros.
The d-normalized target is unchanged; no lower approximation of a
limiting flow or every-level coefficient limit is required.

A degree-array restriction chosen independently of the spectral variables
still produces an original spectral polynomial of degree at most d in
each variable. Thus the existing cosine-Bernstein and whole-domain
three-integration-by-parts transfer applies to this restricted source:
its fixed thin-strip and entire weighted Fourier/Hermite period have a
strict gap below Phi_D. All original scalar characters and endpoint
currents remain. This concerns only the stated seam neighborhood; it is
not a bound on the whole non-CROSS period.

There is a direct interface with the actual filled volume. Denote this
whole seam-neighborhood period by I_seam and the original whole all-CROSS
period by I_cross, with the SAME original Fourier/Hermite normalization.
After retaining a smaller fixed gap kappa_D>0, the transfer just used gives

    |I_seam|<=C_D prod_e(1+|n_e|)^3
                         exp{N(Phi_D-kappa_D)},
    n_e=epsilon_e-2p_e.                              (15)

The [entire all-CROSS theorem](general_all_cross_long_filling_volume.md)
gives an eventually nonzero period and its relative asymptotic, with

    lim_(N->infinity) N^(-1)log|I_cross|
      =Vol(the actual smooth filled exterior)/(2pi)
      =Phi_D-O_D(sum_e |n_e|^(-2)).                   (16)

The prescribed half twists, primitive fillings and actual final-diagram
normalization are exactly those of that theorem. Choose a fixed-diagram
threshold T(D) above its geometric and analytic thresholds and large
enough that the loss in (16) is less than kappa_D/2 whenever every
|p_e|>T(D). For each independently signed vector p fixed BEFORE N tends
to infinity, equations (15)--(16) then imply

    I_seam/I_cross=O_p(exp(-c_D N)), c_D>0,           (17)

for example with any fixed c_D<kappa_D/2 after enlarging the
vector-dependent starting level. Both level parities and composite levels
are retained. No bound on ratios of the twist magnitudes is imposed,
and no joint growing-twist/level estimate is asserted. Any common recorded
framing/component character or common nonzero normalization factor cancels
in (17); it has not been replaced by a new marked normalization.

Equation (17) proves only negligibility of the specified seam remainder.
It does not give equality of the FULL invariant with all-CROSS: the
macroscopic, strictly overloaded non-CROSS contribution remains to be
controlled. The nonzero all-CROSS contribution is the cited theorem,
not a new lower-period claim from the present coefficient upper bound.

## 6. Dependencies

The [global coefficient majorant](research_global_sharp_coefficient_limsup_majorant.md)
supplies (2), closed continuity and the uniform original coefficient
upper bound. Section 3 above and the [closed half-block theorem](actual_fejer_half_block_entropy.md)
supply the normalized half/triangle identity. The
[full endpoint entropy](actual_fejer_full_kernel_entropy_identity_reduction.md)
and [unique geometric maximum](actual_fejer_unique_geometric_maximizer.md)
give the original endpoint function and (9). The
[whole-domain Fourier lemma](actual_global_diagonal_spectral_sector_gap.md),
section 4, applies to the restricted polynomial in section 5.

The [full-fiber activation](research_full_fiber_sharp_boundary_activation.md)
and [stationary classification](research_full_fiber_sharp_stationary_classification.md)
are downstream applications of the uniform overload statement (12a),
not premises of the direct CROSS comparison or seam gap.


No numerical audit or coefficient lower limit is used. The comparison
covers only CROSS degrees and the resulting seam neighborhood;
macroscopic strictly overloaded phase-inconsistent candidates remain
outside the conclusion. In particular (17) is not a full-invariant
volume theorem.
