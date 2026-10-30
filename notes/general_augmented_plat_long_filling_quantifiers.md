# Fixed-skeleton long fillings: the proved geometric quantifiers

30 October 2026. The new multi-cusp rigidity result and the existing
geometric completion theorem have a useful joint corollary: an actual
positive marked augmented-link certificate supplies ALL independently
sufficiently long signed integral fillings, without requiring a quantum
source branch to construct those geometric fillings. This is an assembly
of the repo's established geometric arguments, not a claim of a new
general hyperbolic Dehn filling theorem or of a volume-conjecture proof.

## 1. Fix the topology before either parameter limit

Fix k>=2 and one ordered 2k-strand plat skeleton D. Its r designated
crossing-circle disks, outside wires, upper/lower pairings, marked cut,
and retained half twists epsilon_i in {0,+1,-1} are part of D. The
corresponding filled word has exponents epsilon_i-2p_i. Combine adjacent
powers of the same generator before calling the disks independent.
Let Y_D be the actual drilled augmented exterior, with its primitive
crossing-disk pairs (mu_i,lambda_i).

Supply a positive complete ideal gluing certificate for this ACTUAL
marked Y_D, as in
[the general positive certificate](general_marked_positive_gluing_certificate.md).
A certified right-angled matching-graph realization is one existing
way to supply it. The conclusion below applies at every fixed k
and fixed r; neither k nor r is sent to infinity, and constants may
depend on the entire fixed diagram D.

A parity test decides whether filling all auxiliary circles gives knots:
the fixed plat pairings composed with the permutation of the retained
half-twist word must have one component. Full twists have trivial strand
permutation. Consequently the number of surviving main components is
independent of every p_i. Long twisting cannot repair a failed knot
connectivity test. A 2k-plat gives a k-bridge presentation; minimal bridge
number is not being asserted.

## 2. Geometric corollary with independent signed slopes

There exists T_geom(D)<infinity with the following property. Choose ANY
subset I of the r auxiliary cusps and ANY fixed signed integer slopes
p_i, i in I, satisfying

    |p_i|>T_geom(D) for every i in I.

Fill precisely those cusps along the original primitive curves
mu_i+p_i lambda_i. Then the actual filled exterior has a positively
oriented complete finite-volume hyperbolic metric. All main cusps and
all auxiliary cusps outside I remain complete. There is no common-sign
or slope-comparability condition. One threshold works for every subset.
The empty subset recovers the supplied complete augmented geometry.

Here is the direct proof, including the existence step that the older
completion theorem did not assert on its own. By
[multi-cusp marked rigidity](general_marked_multicusp_gluing_rigidity.md),
with main meridian logs fixed to zero, the auxiliary PROJECTIVE meridian
logs U=(U_1,...,U_r) are holomorphic coordinates on the decorated geometric
germ. The actual preferred longitude logs obey

    V_i(U)=U_i t_i(U),
    t_i(0)=tau_i, Im tau_i>0.                            (1)

This divisibility follows from the exact commuting-similarity identity,
not a guessed source potential. Choose a sufficiently small geometric
neighborhood where all t_i are nonzero and where the framed
representations lie in the fixed neighborhood required by the existing
[geometric completion theorem](general_source_regulator_hyperbolic_equality.md).
Normalize a developed triple to obtain a bounded holomorphic representative
of the framed family there.

Introduce complex parameters e_i and solve

    V_i(U)+e_i U_i=-2pi i e_i,  i=1,...,r.               (2)

At (U,e)=(0,0) the U-Jacobian is diag(tau_i), hence invertible. The
holomorphic implicit-function theorem gives one solution U(e) in a
fixed polydisk around zero. Shrink that polydisk so the framed family
stays in the above completion neighborhood and

    |t_i(U(e))+e_i|>=c_D>0.

Using (1), equation (2) becomes the exact coordinatewise identity

    U_i(e)=-2pi i e_i/[t_i(U(e))+e_i].                   (3)

In particular |U_i(e)|<=2pi|e_i|/c_D, even when the e_i have arbitrarily
unequal magnitudes. If e_i=0, then U_i=V_i=0 EXACTLY. That cusp is
unfilled and parabolic; it has not been assigned a filling coefficient
p_i=0.

Now put e_i=1/p_i for i in I and e_i=0 otherwise. For sufficiently
large independently signed |p_i| this is in the same polydisk and (2)
gives the ACTUAL small-log equations

    U_i+p_i V_i=-2pi i, i in I.                         (4)

The curve mu_i+p_i lambda_i is primitive because its meridian coefficient
is one. Equation (4) has unit charge, with its original orientation.
All unfilled groups are parabolic and nontrivial nearby. These are
precisely the inherited hypotheses of the geometric completion theorem:
actual nearby framed representation, correct primitive marking,
parabolic unfilled ends, and unit-charge filling logarithms. That theorem
constructs the complete smooth metric on the correctly marked filled
topology. This proves the corollary.

The argument makes no rational-surgery quantum claim. Retained half twists
belong to Y_D and its own primitive collar. A hidden half-integer slope
on a different pure link is not substituted for (4).

## 3. The strongest honest general volume statement is still conditional

For this SAME D, suppose the original mixed-color marked source satisfies
all hypotheses of
[the general original-source long-filling transfer](general_original_source_long_filling_transfer.md):
an exact analytic color packet, uniform complex asymptotic with nonzero
leading density, the full complementary-color/alias/normal-current gap,
and selection of the actual marked geometric action and its complete
regulator anchor. Then that transfer theorem gives a threshold
T_vol(D)>=T_geom(D) such that, for every FIXED signed vector p with
all |p_i|>T_vol(D),

    lim_(N -> infinity) (2pi/N) log |K_N(K_D(p))|
                      =Vol(S^3 minus K_D(p)).           (5)

Here the parity test in section 1 is assumed, and all auxiliary circles
are filled. Every quantum level is included, both parities and composite
levels. The order of quantifiers is

    for each fixed k and admissible fixed D,
      there exists T_vol(D),
        for every fixed signed long vector p,
          take the full sequence N -> infinity.

The general quantum hypotheses have NOT yet been proved for every D.
Thus T_geom(D) is established under the positive marked certificate,
whereas existence of T_vol(D) for arbitrary certified D remains the
active volume-conjecture target. The exact compiler, classical geometric
critical scheme and local column amplitudes do not by themselves supply
that missing full-source estimate or period coefficient.

If only a nonzero analytic density germ is proved, rather than a unit
or a controlled peripheral monomial times a unit, the
[source-divisor extension](general_long_filling_source_divisor.md)
allows an exceptional analytic divisor of slopes. Its density-one
conclusion must not be restated as the all-long-slopes assertion (5).

There is no assertion of uniformity when p depends on N. The transfer
errors and their constants are proved with p fixed. Likewise no threshold
depending ONLY on k follows from these arguments: bridge width bounds the
number of simultaneous heads, while the number/order of boxes and all
geometric and source constants remain part of D. This is a limitation of
the proved quantifiers, not a proof that a universal k-only threshold
cannot exist within a more restrictive certified class.

## 4. What long twisting does and does not provide

Given the positive marked base certificate, long integral twists provide
the hyperbolic filled geometry by section 2. They preserve the already
fixed knot/link connectivity. They do not imply the base certificate:
Y_D is independent of p, as are its cusp labels, essential crossing disks
and actual cut topology. Nor does hyperbolicity of a filled knot imply
that every chosen augmented presentation has a hyperbolic base.

There is an elementary obstruction to using raw crossing counts in place
of essential marked disks. Two adjacent same-pair blocks can satisfy

    R^(2p) R^(-2p+2c)=R^(2c)

with fixed c while both apparent twist counts grow. This identity holds
in the ORIGINAL source, with its Cartan factor and marked closure. It
motivates merging redundant regions and certifying the drilled topology;
it does not disprove a uniform threshold inside the certified essential
class.

The present target is therefore broad but precise: every fixed certified
essential augmented 2k-plat skeleton, for every k>=2, with the required
parity and independently long signed full twists. It is not a claim that
every k-bridge knot already lies in that long-twist class, nor that the
full volume conjecture for that class has now been proved.

Root analytical review: checked the holomorphic cusp divisibility,
invertible Jacobian, one fixed parameter polydisk, coordinatewise bounds,
exact partial-filling locus and every inherited hypothesis of the cited
geometric completion theorem. The geometric threshold is proved under
the marked positive certificate. The quantum threshold remains conditional.
No additional finite audit is needed for this direct assembly corollary.
