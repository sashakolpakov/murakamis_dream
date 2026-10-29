# A nonzero asymptotic for the whole original long-pretzel source

**Width extension, 29 October.** The [varying-radius alias estimate](actual_pretzel_all_width_extension.md)
now supplies the full-color gap for every fixed odd s>=9. All local
packet and filling inputs used here already hold there, so the theorem
and its geometric equality extend to those widths without changing
the invariant or signed-slope quantifiers. The older s>=25 argument
below remains as the original assembly with its coarser sufficient bound.

29 October 2026. The full original source, with ALL auxiliary colors
and original normal terms, now has a nonzero selected asymptotic for
every fixed odd pretzel width s>=25 and every independently sufficiently
large fixed signed twist tuple. This is a quantitative whole-source
survival theorem. Its rate is specified by the exact source action.
The separate [geometric completion theorem](actual_long_pretzel_geometric_filling_completion.md)
now proves that this rate equals the filled hyperbolic volume. Its
[Casson--Rivin presentation](actual_long_pretzel_casson_rivin_equality.md)
identifies the source point as the unique filled-slope volume maximizer.
The equality uses these geometric proofs, rather than naming a formal
source action a volume.

## 1. The unchanged invariant and the statement

Use the literal original diagram, turns and marked cap from
[the odd-pretzel source theorem](actual_odd_pretzel_augmented_transfer_source.md).
There are s boxes R^(-(2p_i+1)), where s is odd. Its connectivity
calculation proves that this is a one-component pretzel diagram.
Let Kraw_N(p) be its original marked tensor contraction, including
the full physical Cartan factors on every crossing. Its exact filling
identity is

    Kraw_N(p)=kappa^(-2 sum_i p_i)
      sum_(j_1,...,j_s=1)^N [product_i beta_(j_i-1)^(-p_i)]
                                 A_(s,N)(N-j_1,...,N-j_s). (1)

Here beta^(P) is the full Fourier--Hermite coefficient of r_N^(2P),
and kappa=q^((N-1)^2/2), q=exp(pi i/N). The upper auxiliary bands
and the Casimir normal derivatives are part of A and beta in (1).
There is no replacement of this finite source by a positive model.

For every fixed odd s>=25 there exists an integer p_s>0 such that
for every FIXED tuple of integers |p_i|>=p_s,

    Kraw_N(p)=N^(3/2) exp[-i s pi(N-1)/4]
                 kappa^(-sum_i p_i) D_s(p) exp[N A_s(p)]
                                      (1+O_(s,p)(1/N)),   (2)

with D_s(p) NONZERO. The action and amplitude are the explicit
holomorphic functions defined in section2 of
[the cusp-corridor filling theorem](actual_pretzel_cusp_corridor_filling_survival.md).
The slopes can be positive or negative and can have arbitrarily
different magnitudes. They are fixed BEFORE N tends to infinity.
Both parities and all composite levels are included.

The [original normalization calculation](actual_complete_augmented_source_normalization.md)
applies here to the actual one-component marked diagram as well:
its reduced Kashaev evaluation differs from Kraw only by its recorded
unit framing character. In particular its absolute value is |Kraw|.
The full one-cut modified ADO convention instead contributes the
retained whole-germ value i^(N+3)/N at the main complete color.
There is one such factor, not a new factor for each auxiliary color
used in (1). Thus (2) specifies the original reduced invariant's
growth, and not just an unnormalized comparison sum.

## 2. Exact assembly of the global and local estimates

Write F0=V_s/(2pi) for the already calibrated COMPLETE augmented
source rate. Choose a fixed sufficiently small corridor
0<=h_i=N-j_i<=H=floor(delta N) for which the exact analytic-packet
and cusp-corridor theorems hold.

The [global full-color theorem](actual_pretzel_global_alias_and_colored_source_gap.md)
gives gamma>0 and a sequence epsilon_N->0, uniform over the ENTIRE
complement of this color corridor, such that

    |A_(s,N)(h)|<=exp[N(F0-gamma+epsilon_N)].             (3)

Replacing delta by a slightly smaller positive value handles the
integer floor without changing this statement. The theorem includes
every intermediate color, the even-level middle color j=N/2, the
whole RP band, and the original value-plus-normal source functional.
Its sufficient width condition is

    V_s/(2pi)>(s-1)v_8/pi + (1/2)log(4+sqrt(15)),

which is proved for all odd s>=25. No small-color unitarity claim is
used: the alias itself can grow exponentially, but its proved rate
is small enough for (3).

The exact full-normal filling coefficients satisfy

    sum_(j=0)^(N-1) |beta_j^(-p_i)|<=2N(1+|p_i|).

Apply this to the complement in (1), BEFORE any limiting operation.
All its kappa factors have modulus one. Its absolute contribution is
therefore at most

    product_i[2N(1+|p_i|)] exp[N(F0-gamma+epsilon_N)].     (4)

Inside the corridor the independently proved source-preserving
filling theorem supplies exactly (2), with nonzero coefficient,
for all independently sufficiently large |p_i|. In that theorem
all color and Fourier endpoint terms have fixed positive source
gaps. The high-charge estimate has a gap independent of the largest
slope; this is essential when the |p_i| are not comparable.
The exact source includes no zero Fourier charge. Its 2^s all-unit
signed charges add, and all other local charges have a strict gap.

The same theorem gives Re A_s(p)->F0 uniformly as all |p_i| tend
to infinity. Increase the common threshold p_s so that

    Re A_s(p)>F0-gamma/2

whenever every |p_i|>=p_s, and so that the fixed corridor theorem
also applies. For each such fixed tuple, (4) is exponentially smaller
than its nonzero corridor asymptotic. Adding it cannot cancel the
leading coefficient, and its relative error is eventually O(1/N).
This proves (2) for the WHOLE original finite sum (1).

## 3. The rate and its subsequent geometric equality

Define only as notation

    Vsrc_s(p)=2pi Re A_s(p).

Then the theorem proves an actual limit for the original invariant:

    lim_(N->infinity) (2pi/N)log|<Pretzel(2p_1+1,...,2p_s+1)>_N|
                                                =Vsrc_s(p). (5)

The displayed knot notation uses the source's crossing convention
R^(-(2p_i+1)); globally mirroring the convention changes phases but
does not change this absolute-value statement.

Let tau_s=(1+exp(2iu_s))/2, u_s=atan(sec(pi/s)). The exact action
calculation gives

    Vsrc_s(p)=V_s-2pi^2 Im(tau_s)
                  sum_i |1+2p_i tau_s|^(-2)
                                     +O_s(sum_i |p_i|^(-4)). (6)

More fundamentally, A_s is the value of the analytic source phase

    Psi(z)-2pi i sum_i(p_i z_i^2+z_i)

at its selected nondegenerate critical point, with Psi the explicitly
defined Fourier Legendre transform of the actual mixed-color action.
Formula (6) is a consequence, not a substitute for that exact action.

The subsequent geometric completion proves

    Vsrc_s(p)=Vol(S^3 minus Pretzel(2p_1+1,...,2p_s+1)).   (7)

The [geometric comparison and completion](actual_long_pretzel_geometric_filling_completion.md)
match the actual auxiliary meridian and preferred longitude, construct
the filled-knot representation rho_p, and prove

    Vsrc_s(p)=Vol(rho_p)=Vol(S^3 minus K).

The positive core and primitive2pi tubes give a complete finite-volume
hyperbolic metric with holonomy rho_p. This closes equality(7), not
merely the earlier upper-bound checkpoint. The actual fundamental-chain
regulator and smooth completion, rather than agreement of one cusp
derivative, establish it.

Neither an uncontrolled complementary color sector nor an assumed
nonzero cycle coefficient remains in(2). The separate geometric
argument is explicitly linked so that equality(7) is not hidden
in the name of the source action.

## 4. Verification and its scope

The global complement proof and the corridor proof have each passed
independent analytic reviews, including signed unequal slopes,
the even-level middle color, and the paired high-charge endpoint
currents. The assembly above has also passed an independent review.
Fresh root replays of all four supporting audits passed:

- `audit_actual_pretzel_global_alias_and_colored_source_gap.py`:
  exact physical band identities, normal coefficients, spectral
  ellipse, frozen blocks, binomial sum and the rational width bound.
- `audit_actual_pretzel_exact_analytic_color_packet.py`:
  actual marked-source decompositions and exact complex packets.
- `audit_actual_filling_source_fourier_endpoint_gap.py`:
  full-normal kernels, exact contour currents and charge transforms.
- `audit_actual_pretzel_cusp_corridor_filling_survival.py`:
  original filling coefficients and signed Gaussian density/phase
  calibrations on controlled analytic packets.

The analytic-packet calibrations in the last audit are not numerical
proofs of the pretzel asymptotic. The actual-source hypotheses and
uniform asymptotic estimates are proved in the linked notes. None
of these finite checks alone supplies geometric equality(7); that
conclusion uses the separate geometric completion proof.
