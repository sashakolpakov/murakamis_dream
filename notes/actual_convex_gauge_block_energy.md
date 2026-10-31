# Coupled crossing gauges: an exact optimizer and a twist-block improvement

28 October 2026. The original endpoint-preserving gauge program can be
implemented as a finite convex optimization, with its full original
paired source retained. For a broad explicit alternating-sign class,
flat gauges are its **exact finite-N global minimizers** at the
single-crossing Hilbert--Schmidt partition. Even replacing HS norms by
operator norms cannot improve its exponential crossing envelope.
Thus this particular optimization does not produce the Rivin volume.

There is a constructive improvement after coherent block contraction:
an entire repeated-crossing twist block has a uniform exponential norm
bound independent of its length. It improves the crossing bound for
every repeated-generator block of length at least five in the specified
original braid word, at arbitrary width. No conversion of an arbitrary
unoriented diagram twist region is assumed. This is not the sharp
knot-volume bound or a lower bound.

## 1. The implemented original program and its entropy dual

Use the source-preserving gauge program in
[the weighted Fourier energy theorem](actual_weighted_fourier_plat_energy.md#3-a-computable-positive-energy-upper-bound-hierarchy).
The width is 2k; every original cap/cup pair is adjacent. On every
physical wire edge e choose arbitrary real logs s_e(a), 0<=a<N.
At each endpoint the only restrictions are

    s_(odd,a)+s_(even,d-a)=0, d=N-1.                   (1)

These make the endpoint gauges fix the original paired cups, ordinary
caps, and the marked cap after its legitimate whole-degree restriction.
All scalar, pivotal and framing lines stay as before. An internal
wire has a single gauge on its entire segment between incident gates.

For a crossing v let i=(a,b), o=(c,e). Put

    Phi_N(s)=(1/2)sum_v log sum_(i,o)
        |R_v(o,i)|^2 exp(2s_out(o)-2s_in(i)).           (2)

The sums use the original physical crossing support, not a cyclic
completion. Positive entries are exactly

    R_+(a+b-e,e;a,b)
       =kappa x^(-b-e)Q^(eb)
          F_(a+b-e)F_a/[F_(a-e)F_bF_e],               (3)

with 0<=e<=a<N and a+b-e<N. The negative moduli are obtained by
swapping both input and output heads, from the proved actual
antiunitary identity. The common kappa is a retained unit phase.
Thus no knot scalar is input to the objective.

The resulting rigorous bound is

    |P_N| <= |chi_N|N^(k-1) exp(inf_s Phi_N(s)).         (4)

The implementable objective (2) is convex log-sum-exp. The new script
eliminates (1) with a signed union-find and supplies its analytic
gradient to L-BFGS. It keeps separate intermediate wire gauges and
the independent top and bottom source gauges; it does not optimize
each crossing in isolation.

There is a useful dual characterization. At every crossing choose
a probability p_v on its actual nonzero entries. Require identical
one-head marginals at the two ends of every internal wire and require
reflected odd/even marginals at each paired boundary. Such probabilities
annihilate every gauge linear term in (2). The elementary entropy
identity

    log sum_i exp(l_i)=max_p [sum_i p_i l_i-sum_i p_i log p_i]

therefore gives the lower certificate

    inf_s Phi_N(s) >= (1/2)sum_v
          [sum p_v log|R_v|^2-sum p_v log p_v].         (5)

If the maximizing constrained probabilities are strictly positive,
Lagrange multipliers give p_v proportional to the exponentials in
(2), and equality holds. Indeed the entropy has infinite inward
derivative at a zero coordinate whenever a strictly positive feasible
point exists, so its maximum is interior. Its derivative annihilates
the constraint tangent space, hence is a linear combination of the
constraint rows, which gives precisely those multipliers. This is a
finite-dimensional entropy/flow duality with actual R weights. It
does not identify those flows with geometric angle structures.

The subsequent [joint projector-profile bound](actual_twist_block_projector_barrier.md)
sharpens the block constant below to 4v_3+2v_8 while retaining the
same original source, frame and meridian-circle proof. The valid
coarser estimates here are unchanged.

## 2. Exact optimum for alternating signs by generator position

Suppose the word has the sign pattern

    sign(sigma_i)=epsilon*(-1)^(i+1), epsilon=+1 or -1, (6)

at every occurrence of generator i. Its index sequence is arbitrary,
as are its length and even width. The theorem applies whenever its
plat closure is the desired one-component knot; no knot-specific
calculation enters. It is not a claim that every alternating knot
presentation automatically has (6).

**Exact optimizer theorem.** For every N>=2,

    inf_s Phi_N(s)=m log||R_+||_HS.                    (7)

Thus the fully coupled single-crossing HS gauge program is already
minimized by s=0, including all endpoint gauges allowed in (1).

Proof. Normalize the squared moduli of the positive crossing:

    p_+(o,i)=|R_+(o,i)|^2/||R_+||_HS^2.

The literal matrix (3) is symmetric: R_+(o,i)=R_+(i,o).
It follows that its input and output first-head marginals coincide,
as do its second-head marginals. Let them be p_H and p_L.
Root factorial reflection gives a second exact modulus symmetry,

    |R_+(c,e;a,b)|
       =|R_+(d-e,d-c;d-b,d-a)|.                      (8)

Indeed the new transfer difference is still a-e=c-b, and
|F_j||F_(d-j)|=N cancels all reflected numerator/denominator factors
in (3). Consequently p_H(a)=p_L(d-a).

For the negative crossing the two head marginals are interchanged.
Under (6), any given odd physical head therefore has the same marginal
at ALL its incident crossings, and every even head has the reflected
marginal. Which of the two is called H depends only on epsilon.
Assign these same marginals to untouched wire segments too. All
internal wire constraints and all boundary reflection constraints
in Section 1 are satisfied. The strictly positive probabilities
p_v=|R_v|^2/||R_v||_HS^2 are thus feasible in (5). Their entropy value
is exactly sum_v log||R_v||_HS=m log||R_+||_HS.
The same value is attained by s=0 in (2), proving (7).

Equivalently, the entire projected gradient at s=0 vanishes, not
merely the gradients of individually balanced crossings. Convexity
then certifies the global minimum without any numerical convergence
assumption. This is why some randomly initialized large-N numerical
optimizations converge slowly in gauge-null directions; the exact
stationary certificate avoids confusing that with a smaller optimum.

## 3. Even operator-norm gauges retain the crossing exponent

Let a_N+b_N=d with a_N/N ->3/4 and b_N/N ->1/4. When epsilon=+1,
put the fixed indices (a_N,b_N,a_N,b_N,...) on the physical heads;
reverse them for epsilon=-1. At a positive crossing this gives the
diagonal entry R_+(a_N,b_N;a_N,b_N). At a negative crossing it gives
the head-swapped diagonal entry with the same modulus. This is a
single physical index path through the WHOLE network, and its paired
endpoint charges are exactly d.

Every gauge in (1) is one on each of these endpoint states. Along the
path the interior gauge ratios telescope. Bounding each local operator
norm by this one entry therefore gives, for ANY N-dependent choices
of positive diagonal wire gauges,

    product_v ||G_out,v R_v G_in,v^(-1)||_op
              >= |R_+(a_N,b_N;a_N,b_N)|^m.             (9)

This is a lower bound on the norm-based upper-bound program, not on
the actual scalar period; other state paths can cancel that scalar.

The uniform factorial estimate shows

    log|R_+(a_N,b_N;a_N,b_N)|
         =N[2J(3/4)-J(1/2)-2J(1/4)]+O(log N)
         =N v_8/(2pi)+O(log N).

Flat gauges have that same operator-norm exponent by the original
crossing theorem. Hence the best single-crossing operator program,
as well as (7), has the exact exponential rate

    inf_gauge sum_v log||R_v,gauge||
                  =m N v_8/(2pi)+O_word(log N).        (10)

This decides the proposed finest local scaling route for the class
(6), at arbitrary width. It cannot by itself lower the crossing
envelope to the smaller hyperbolic knot volume. A genuinely coherent
block contraction is necessary.

## 4. A uniform twist-block improvement from the actual Casimir

Such contraction does yield a quantitative general improvement.
Let B be either original complete crossing on two physical heads,
with its original unit Cartan/framing factors retained. For every
integer ell and every N>=2,

    ||B^ell||_op <=32 N^2(1+|ell|) c_*^N,
    ||B^ell||_HS <=32 N^3(1+|ell|) c_*^N,
    c_*=7+5sqrt(2).                                  (11)

The exponential constant is independent of twist length. No spectral
condition number or unproved semisimplicity is hidden in (11).

Here is a direct norm proof from the already independently derived
[actual Casimir crossing polynomial](casimir_braiding_and_recoupling_lattice.md#3-the-actual-crossing-has-a-unique-confluent-polynomial).
Use Ecal=rho^2 E and the actual complete physical matrices. They obey

    ||F||,||Ecal||<=2, K unitary,
    F Ecal+qK+q^(-1)K^(-1)=-2I.

On the tensor product put

    Omega=F_tot Ecal_tot+qK_1K_2+q^(-1)K_1^(-1)K_2^(-1),
    F_tot=F_1+K_1^(-1)F_2,
    Ecal_tot=Ecal_1 K_2+Ecal_2.

Expanding and using the single-head Casimir identity gives

    Omega=-2(K_2+K_1^(-1))
       -(q+q^(-1))K_1^(-1)K_2
       +F_1 Ecal_2+K_1^(-1)Ecal_1 F_2K_2,

so ||Omega||<=14 in the original flat balanced metric.

Let P_N(z)=T_N(z)+2, T_0=2,T_1=z,T_(n+1)=zT_n-T_(n-1).
The proved actual polynomial identity is B=lambda_0 r_N(Omega),
|lambda_0|=1, with P_N(Omega)=0. Its roots

    c=2cos(pi h/N), h odd, 1<=h<N

are double. When N is odd there is additionally the simple root -2.
At every double root r_N(c)=nu, |nu|=1 and

    |r_N'(c)|=(N-h)/(4 sin(pi h/N))<=N^2/8.            (12)

The simple root value has modulus one. These spectral jets, including
their derivatives, follow from the defining finite R by confluent
generic-q highest-weight interpolation; no diagonalizability at the
root is used.

For an explicit bounded Hermite basis set

    Q_c(z)=P_N(z)/(z-c)^2,
    A_c=Q_c(c)=N^2/(4sin^2(pi h/N)),
    alpha_c=Q_c'(c)/A_c=c/(4-c^2),
    e_c(z)=Q_c(z)[1-alpha_c(z-c)]/A_c,
    j_c(z)=(z-c)Q_c(z)/A_c.

These polynomials have respectively the jets (1,0) and (0,1) at c,
and zero jets at all other roots. At a possible simple root -2 use
e_-(z)=P_N(z)/[(z+2)P_N'(-2)], with |P_N'(-2)|=N^2.
Consequently the exact polynomial representing B^ell/lambda_0^ell is

    f_ell(z)=sum_double [nu^ell e_c(z)
                 +ell nu^(ell-1)r_N'(c) j_c(z)]
                     +sum_simple nu^ell e_-(z).        (13)

This formula works for negative ell too: r_N is a unit modulo P_N.

For completeness the constants can be controlled explicitly. Integrate
around |z|=R=14+1/N. The resolvent norm is at most N by its Neumann
series. Put r(R)=(R+sqrt(R^2+4))/2. The Chebyshev recurrence gives
|T_N(z)|<=2r(R)^N, and

    |P_N(z)|<=5 c_*^N,
    |z-c|>=12,
    A_c>=N^2/4, |alpha_c|<=N^2/8.

The first inequality uses
N[log r(14+1/N)-log r(14)]<=1/sqrt(200).
It follows on that circle that

    |e_c(z)|<c_*^N/3,
    |j_c(z)|<=5c_*^N/(3N^2),
    |e_-(z)|<=5c_*^N/(12N^2).

Together with (12), the at most N interpolation conditions bound
|f_ell(z)| by N(1+|ell|)c_*^N. Cauchy's matrix functional calculus
therefore gives ||f_ell(Omega)||<=R N^2(1+|ell|)c_*^N, which is
stronger than the operator inequality (11). The HS inequality costs
at most sqrt(N^2)=N. Thus no exponentially conditioned eigenbasis
has entered the proof.

## 5. Whole-word consequence at arbitrary width

Partition any fixed original knot word into maximal repeated-generator
twist blocks of lengths ell_t, leaving other crossings as blocks of
length one. Perform these actual matrix contractions first, preserving
the original source and all common phases. Combining (11) with the
ordinary crossing bound gives the unconditional whole-source estimate

    limsup_N (2pi/N)log|P_N|
       <=sum_t min(|ell_t|v_8, 2pi log(7+5sqrt(2))).   (14)

The factors 32N^3(1+|ell_t|), spectator dimensions and all complete
source normalizations contribute only O_word(log N). The same holds
for the reduced original Kashaev scalar. This applies to arbitrary
width and sign patterns, not just the twist-knot family.

There is also a direct finite-N source justification which includes
ODD braid width and does not require passing to an even plat. For a
b-strand knot cut use its original complete pivot g, which is unitary,
and retain the unit-modulus zero-framing line in W. The exact actual
cut is

    C=Tr_env[W(I tensor g^(tensor(b-1)))]=K_N I.

Every partial trace of a unitary-weighted operator has norm at most
the environment dimension times its operator norm. Thus, with every
normalization still original,

    |K_N| <= N^(b-1)||W||_op
      <= N^(b-1) product_t min(
          ||B_sign(t)||_op^|ell_t|,
          32N^2(1+|ell_t|)(7+5sqrt(2))^N).            (14a)

At completeness the full ADO modified dimension is its known root
phase divided by N, so it does not change the exponential bound.
This proof uses the actual original pivotal cut, not a new positive
closing trace. It supplies the source estimate for (14) at every
braid width.

Since

    2pi log(7+5sqrt(2)) < 5 v_8,

every repeated-generator block of length at least five gives a strict improvement
over its separate-crossing bound. The displayed numerical comparison
can be verified by elementary convergent series for sqrt(2), log and
Catalan's constant; it is not used for (11) or (14). The constant is
deliberately coarse, so (14) is not asserted to equal or be bounded by
Vol(S^3-K). It establishes a real quantitative gain from coherent
block contraction in the specified braid word after the finest gauge program has been shown
ineffective on the alternating-sign class.

## 6. Reproduction and numerical scope

    python3 experiments/actual_convex_gauge_block_energy.py
    python3 experiments/actual_convex_gauge_block_energy.py --full

The script uses exact finite factorial moduli in logarithmic form;
the only floating operations in the objective are ordinary positive
log-sum-exp and its gradient. It checks the transpose/reflection
marginals through N=32 and optimizes complete coupled wire gauges at
width four and six. In the class (6), the independently verified
zero gradient is the global certificate, so starting at that point
does not rely on slow optimization in null directions. Nonalternating
examples are diagnostics; finite-iteration results there are feasible
upper bounds and are not claimed exact optima.

The block tests independently construct the bounded physical Omega,
check its actual polynomial crossing identity, and evaluate positive
and negative twist powers through N=10. The all-N bound is the analytic
Hermite/resolvent proof above, not extrapolation from those powers.
[Saved results](../experiments/actual_convex_gauge_block_energy_results.json).
