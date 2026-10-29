# A polynomial normal-jet envelope for the central Racah sum

29 October 2026. This proves a quantitative bound for an EXPLICIT
seven-factorial finite sum, including both low and high folded partners.
The main terms have a common root phase; the terms activated by a second
root zero have a uniform strict gap. Consequently four fixed normal jets
cost only a polynomial relative to the known positive central marked
partition. This is a new analytic estimate, not a numerical inference.

The finite algebraic bridge to the ACTUAL boundary Gram is now proved
in [the generic source identity](actual_generic_trivalent_racah_source_identity.md):
the original double sum equals this normalized Racah sum before root
specialization, with all high partners and normal tails. Consequently
the estimates here prove polynomial conditioning of the actual
correlated boundary Gram on a fixed central corridor. The original
mark and all-partner moment formula are those of
[the generic source theorem](actual_generic_six_head_tetrahedral_source.md).
No arbitrary six-port recoupling operator norm or whole-support bound
is inferred.

## 1. Explicit object and the theorem

Write d=N-1, q=exp(pi i/N), zeta=q(1-Z)^(1/(2N)), with its analytic
branch through q. Use symmetric quantum integers and factorials

    [n]=(zeta^n-zeta^(-n))/(zeta-zeta^(-1)),
    [n]!=product_(k=1)^n[k].

For an ordinary integer triangle a,b,c in 0,...,d put J=a+b+c and
r_i=J-2j_i. Define the finite sum

    S_abc(zeta)=sum_t (-1)^(d+t) [N+t]!
       /{[d+t-J]! product_i[t-j_i]! product_i[J-j_i-t]!}, (1)

where max(a,b,c,J-d)<=t<=min(a+b,a+c,b+c). Every factorial index
is nonnegative. Put

    D_abc^2=[r_1]![r_2]![r_3]!/[J+1]!,
    D_j^2=[j]!^2[d-j]!/[N+j]!,
    Tcal_abc=(-1)^d product_i[2j_i+1]
                      *D_abc^2 product_i D_(j_i)^2 *S_abc^2. (2)

These are rational functions before removable zeros are peeled; no
square-root normalization is part of (2).

Take folded labels l_i<=floor(d/2), with
sigma_i=(d/2-l_i)/N>=0. Let r be their number of paired axes.
An unfolded branch j_i is l_i or d-l_i on a paired axis, and l_i
alone on a simple odd axis. Use the actual paired-circle character
unit ell_j(Z)=L_N(c_j(zeta))/Z, explicitly defined in the
generic source theorem. For I a subset of paired axes put

    Hcal_I(Z)=sum_branches Z^r Tcal_abc product_(i in I)ell_(j_i)(Z),
    mcal_I=(-1)^d(q-q^(-1))[Z^(r+1-|I|)]Hcal_I(Z).   (3)

There are constants delta_0>0, C,C0, independent of N and of the
labels, such that whenever max sigma_i<=delta_0,

    |mcal_I|<=C0 N^C tau_N(l),                     (4)

where tau_N(l)=Z_N(l)/N^(3-r)>0 is the PROVED positive marked
top moment, with Z_N given by the
[all-channel marked formula](actual_trivalent_all_channel_marked_contraction.md).
The estimate includes both parities and arbitrarily close paired
neighbors of the odd simple axis. It is asserted for sufficiently
large N; finitely many remaining supported labels can be absorbed
in C0.

## 2. One common root phase in the main sum

Choose initially delta<1/20. Every branch has
j_i/N in (1/2-delta-O(1/N),1/2+delta). For every term in (1), all
SEVEN denominator factorial indices are <N. For instance
t-j_i<=N/2+3delta N+O(1), and
d+t-J<=N/2+5delta N+O(1); the other differences have the same
strict margin. Also J+1<2N.

Separate (1) into t<N and t>=N. In the main part,

    ([N+t]!/[N])|_(zeta=q)=(-1)^t[N-1]! [t]!.

All denominator quantum factorials are positive at this root.
Thus EVERY term of S_main/[N] has the SAME phase (-1)^d. Its
absolute sum is exactly

    Rcore_N(j)=N sum_(max j_i,J-d<=t<=min pair,d)
       s_t/{s_(d+t-J) product_i s_(t-j_i)s_(J-j_i-t)}, (5)

where s_u=product_(k=1)^u 2sin(pi k/N). This is a genuine positive
finite sum for the unfolded as well as folded labels. Its support
is invariant under t->J-t. Sine-factorial reflection also gives

    Rcore_N=sum_t s_t s_(J-t)
                          /product_i s_(t-j_i)s_(J-j_i-t). (6)

The restriction t,J-t<=d is retained in (5),(6); no alias endpoint
has been silently removed.

On the common disk |Z|<=c/N^2, fixed-factorial zero removal and
the [bounded normal factorial estimate](bounded_normal_quantum_factorial_envelope.md)
give a uniform constant envelope for each nonzero root product.
Here the same fact follows directly: a nonzero factor has size at
least a constant/N, while its change is O(|Z|); there are O(N)
factors in each fixed factorial ratio. Their accumulated relative
cost is bounded on this disk. The normalization zeta-zeta^(-1)
and the removed root zeros cost only fixed powers of N.

Because the main root terms have a common phase, summing those
envelopes costs at most a polynomial times the POSITIVE value (5).
Cauchy's estimate for any fixed order k<=4 adds at most C_k N^(2k).
This step uses no cancellation estimate on the original B double sum.

## 3. The second-zero tail has a strict central gap

For t>=N, the numerator in (1) contains BOTH [N] and [2N]. After
the first is removed, the term still vanishes at Z=0. After both
are peeled, its root magnitude has, up to polynomial factors,
numerator s_(t-N) instead of s_t. All denominator arguments stay
physical by section2. Its continuous summand rate is therefore

    Htail(s,a)=L(s-1)-L(1+s-S)
                 -sum_i[L(s-a_i)+L(S-a_i-s)],       (7)

where s=t/N, a_i=j_i/N, S=sum a_i and
L(u)=integral_0^u log(2sin pi v)dv. The tail has at most N terms.

At a_1=a_2=a_3=1/2 the tail collapses to s=1 and (7)=0. All
arguments in (7) stay in [0,1] for its actual nearby support. Since
L is continuous there, the supremum of the tail rate tends to zero
uniformly as delta->0. This remains true at zero factorial indices;
no derivative of L at an endpoint is being bounded.

The main profile from (6) is

    H(s,a)=L(s)+L(S-s)
                  -sum_i[L(s-a_i)+L(S-a_i-s)].      (8)

At the center it is 4[L(s)-L(s-1/2)], has unique maximum j0=v8/pi
at s=3/4, and has strictly negative second derivative throughout
its interior. A fixed compact neighborhood of 3/4 has a strict
gap from its complement. Uniform continuity first localizes every
nearby maximizer to that neighborhood; there every child argument
is <1/2 and both parent arguments >1/2, so the cotangent second
derivative is strictly negative. Symmetry then fixes the maximum
at s=S/2. Its value is

    Phi(a)=2[L(S/2)-sum_i L(S/2-a_i)].              (9)

It tends to j0 as delta->0. Choose delta_0 small enough that the
tail supremum is <j0/4 and the main maximum >3j0/4. The difference
is a UNIFORM positive gap. This argument is effective using the
explicit continuous functions, but no numerical choice of delta_0
is needed for the existence theorem.

Fixed normal derivatives of the peeled tail cost only polynomial
factors on the same disk. Even after the second zero is activated,
the tail is exponentially below the main sum. Squaring S in (2)
does not change that conclusion: mixed main/tail terms retain a
strict gap from the main square.

## 4. All eight branch actions equal the folded marked action

Let x_i=S/2-a_i, i=1,2,3, and x_4=1-S/2. These remain in a compact
positive half-angle strip in the central corridor. The normalized
per-edge factor has the particularly simple root value

    ([N] D_j^2)|_q=(-1)^j,                         (10)

because [j]![d-j]!=[d]! and
([N+j]!/[N])|_q=(-1)^j[d]![j]!. It has no factorial exponential.
An odd simple dimension [2j+1]=[N] supplies its own root zero.
The remaining triple factor, after its one zero is removed, has
rate sum_i L(2x_i)-L(S-1). Together with the main square (9), the
FULL rate of (2) is

    E=sum_(i=1)^4 [L(2x_i)-4L(x_i)]
     =-2sum_(i=1)^4[L(x_i)+L(1/2-x_i)].             (11)

Thus none of the dimension/triangle factors may be omitted from
this comparison. At finite N set j_i=d/2-N sigma_i; replacing a_i
by 1/2-sigma_i only changes the factorial asymptotics by polynomial
prefactors, uniformly on this corridor. The four x_i are then the
tetrahedral sign rows in the whole-label marked theorem. Its proof
shows that (11) is SEPARATELY EVEN in every sigma_i.

An actual high-partner change j_i->d-j_i is EXACTLY sigma_i->-sigma_i.
Therefore every unfolded main branch has the SAME exponential rate
as the folded positive marked weight. The sine-factorial envelope,
the positive interior saddle and at most N summands give

    |[Z^k]{Z^r Tcal_abc product ell}|<=poly(N)e^(N E_fold),
                       k<=4.                      (12)

All apparent poles in (2) are removed by Z^r; in fact its main part
starts at least at order Z because S has its first zero on every
branch. Paired ell units have polynomial jets even at the nearest
paired neighbor, since their nonzero root denominator is at least
2sin(pi/N). The second-zero tail is controlled by section3. These
observations justify applying the common-disk Cauchy bound to the
ENTIRE expressions in (12), not to a bare singular factor.

The proved positive marked partition has uniformly

    tau_N(l)>=c N^(-3)e^(N E_fold)                 (13)

on a smaller central corridor. This follows directly from its
positive local Laplace prefactor, with the actual odd/even half-step
and the paired multiplicities; alternatively an interior nearest
saddle term gives a sufficient polynomial lower bound. Combine
(12),(13), sum the at most eight branches, and use the coefficient
order in (3). This proves (4).

## 5. The proved finite source bridge and actual conditioning

The proved generic source identity for the B of the original nested
cups and ordered duals is

    B_abc=(-1)^J zeta^[a^2-b^2+c^2-ab-ac+bc-cd]
                   *[a]![b]![c]!/[J+1]! *S_abc.    (14)

It is established by the actual mixed-highest Casimir recurrence,
the literal source coefficient COLUMN, the uniquely normalized finite
polynomial eigenproblem and an own finite Sears conversion. The
exceptional c=0 Jacobi diagonal is computed by the ACTUAL cup/cap
projection; it is not obtained by canceling its identically zero
Fricke factor. Polynomial continuation in X=Q^N includes the high
partners. No published quantum-6j formula is a premise. An independent
analytical review and fresh generic/vector certificate replay passed.

Here is explicit normalization bookkeeping when substituting (14)
into the proved physical trace. Its F-factor prefactor is

    (-1)^d zeta^E/(1-Q) F_r1 F_r2 F_r3 F_(J+1)
          product_j [F_(d-j)(1-Q^(2j+1))/F_(N+j)],
    E=d(3a+2b+3c+3)-4a^2-4c^2+2ac-2J.

Write D(a,b,c)=a^2-b^2+c^2-ab-ac+bc-cd and T_n=n(n-1)/2.
The two B prefactors, for (a,b,c) and (c,b,a), have total sign
(-1)^(2J)=1. All (1-Q) factors cancel, and the remaining zeta
exponent is IDENTICALLY zero:

    E+D(a,b,c)+D(c,b,a)+sum_i T_(r_i)+T_(J+1)
             +sum_j[T_(d-j)-T_(N+j)+2j]=0.

The factorials left over are precisely Tcal in (2). This is an
identity before specialization, not an equality modulo a root
character. Hence the actual marked moments equal (3), including
all lower moments and normal tails. Equation (4) proves

    max_I |m_I/tau_N|<=poly(N),
    K_j=sum_I |coeff_I q_j^(1/2)|^2<=poly(N)        (15)

uniformly throughout a fixed central corridor, at both parities,
with simple axes handled by the same formula with their absent
paired variables. In particular log K_j=O(log N)=o(N) there.
The second implication is immediate from the finite binomial
polynomial of degree <=3 in the
[actual marked boundary frame](actual_six_pants_boundary_torsor_and_sewing.md).
Source and co-source costs remain the exact K_j and tau_j^2 K_j
from that theorem. No recoupling operator norm or whole-support
conditioning follows from this central result.

The diagnostic [original moment implementation](../experiments/diagnose_actual_marked_boundary_conditioning.py)
uses the already proved generic source/cut formula, not (14), to
measure the actual moments. For nearest paired central labels K is
1.000043544... at N=128 and 1.000011164... at N=256. Macroscopic
central tests remain bounded, while some saturation-boundary tests
grow slowly. Those finite measurements guided the proof but are
not substituted for the proved finite bridge or a whole-support
estimate. The data include polynomially small normal steps and
precision growing with N; further paired-precision validation is
kept separate from a theorem claim.

## 6. Actual-source diagnostic and paired precision

The [diagnostic audit](../experiments/audit_actual_marked_boundary_conditioning.py)
evaluates the PROVED generic physical double-sum trace, groups every
low/high partner before extracting the physical marked normal, and
uses no instance of (14) in its measurements. It compares normal
steps N^-8 and N^-8/2 while increasing precision by seventy digits.
Its saved results are labeled PASS_DIAGNOSTIC, not a proof of (15).

The refined values include:

| N | folded triple | precisions | K_j |
| --- | --- | --- | --- |
| 16 | (7,7,7) | 150 / 220 digits | 1.00184624542464 |
| 64 | (31,31,31) | 180 / 250 digits | 1.00016536760140 |
| 128 | (51,51,51) | 240 / 310 digits | 1.01103593283933 |
| 129 | (32,32,64) | 260 / 330 digits | 2.59529339844986 |
| 256 | (127,127,127) | 360 / 430 digits | 1.00001116412322 |

The maximum difference of normalized moments is below 1.3e-16 in
the smallest case and below 3e-23 in every other listed case. The
independent positive tau formula checks the top moment at the same
normal-step accuracy. The boundary example at N=129 has delta=0;
it is outside the central theorem and illustrates why a uniform
constant bound is not inferred from nearest-center samples.

These tests establish numerical consistency of the original moment
implementation at the stated parameters. The finite transformation
(14) is proved separately; the sampling itself does not control
all q-jets or establish any whole-support conditioning exponent.
