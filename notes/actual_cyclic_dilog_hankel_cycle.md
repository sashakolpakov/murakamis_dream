# The original quantum period has an explicit convergent cut cycle

28 October 2026. The whole-word cyclic-dilogarithm construction now
admits an exact deformation from its marked small circles to radial
branch cuts. By choosing the opposite-root realization of every u
factor, all factors are inverse cyclic dilogarithms. Every cut integral
converges at both ends, with no omitted contribution at infinity.

The resulting cycle and its nonzero local-system jump coefficients are
specified for the original quantum state. This is not yet a proof that
their full contraction has a nonzero geometric critical contribution.
In particular the complex integrand is not made positive by the sine
weights below.

## 1. The actual marked covers

Let N>=2, Q=exp(2pi i/N), and epsilon=+1 or -1. On the t-plane put

    D_epsilon(t)=product_(k=1)^(N-1)(1-Q^(epsilon k)t)^(k/N),
    A_epsilon(t)=D_epsilon(t)^-1.

The branches start with D_epsilon(0)=1. Their algebraic cover is

    y^N=product_(k=1)^(N-1)(1-Q^(epsilon k)t)^k.

The factor with k=1 shows that the cover is connected: its divisor
valuation is one, so the defining right side cannot be a p-th power
for any prime p dividing N. Equivalently the local monodromy about
that root generates all N sheets. We use its normalization.

The actual first N Taylor coefficients of A_epsilon are

    c_(epsilon,a)=(-1)^a Q^(epsilon a(a-1)/2)
                       /(Q^epsilon;Q^epsilon)_a, 0<=a<N. (1)

This follows from the logarithmic coefficient identity for D and the
finite Euler inversion. In particular, for T^N=0, the corresponding
v polynomial is exactly

    v_(epsilon,N)(T)=(1/(2pi i)) integral_(|t|=rho)
                             A_epsilon(t)(tI-T)^-1 dt, (2)

where 0<rho<1 and the small circle is lifted from the marked sheet.
The resolvent is a finite Laurent polynomial in t^-1. No spectral
choice or unknown knot normalization is involved.

Every original u factor has a realization of this form as well:

    u_(Q,N)(T)=v_(Q^-1,N)(Q^-1 T).                 (3)

Indeed (Q^-1;Q^-1)_a=(-1)^a Q^(-a(a+1)/2)(Q;Q)_a.
The auxiliary root orientation changes in (3); the physical knot
parameter Q, its source and its Gaussian factors do not change.
The [whole-word construction](actual_whole_word_cyclic_dilog_resolvent_period.md)
also realizes every factorial diagonal by an inverse-D coefficient
functional. Thus it uses only (2) and the nonnegative coefficient
orders in Section 3 below.

## 2. Exact boundary values and the oriented cut identity

The distinct cuts are

    L_(epsilon,j)={Q^(-epsilon j)r : 1<=r<infinity},
                                    1<=j<N.

Their complement contains zero and carries the marked branch. Define
for r>1

    h_(epsilon,j)(r)=(r-1)^(-j/N)
       product_(k!=j)(1-r Q^(epsilon(k-j)))^(-k/N). (4)

For each k!=j, continue its logarithm radially from r=0. It never
crosses its zero on this path; equivalently use the corresponding
principal logarithm. The remaining real power in (4) is positive.

Let + denote the side obtained by a small counterclockwise rotation
of the outward ray, and - the clockwise side. The j-th factor then
has logarithms log(r-1)-i pi and log(r-1)+i pi, respectively. Hence

    (A_epsilon)_+=exp(+pi i j/N)h_(epsilon,j),
    (A_epsilon)_-=exp(-pi i j/N)h_(epsilon,j),
    (A_epsilon)_+-(A_epsilon)_-
                    =2i sin(pi j/N)h_(epsilon,j). (5)

The sign is independent of epsilon: both sides refer to the actual
complex orientation of the t-plane. Let a>=0. Cauchy's theorem on
the plane with the rays and a small zero disk removed gives

    [t^a]A_epsilon(t)
      =sum_(j=1)^(N-1) sin(pi j/N)/pi * Q^(epsilon j a)
          *integral_1^infinity h_(epsilon,j)(r)r^(-a-1)dr. (6)

To check the orientation, a positive contour around an outward slit
runs inward on its + side and outward on its - side. The small
zero circle equals the large outer contour minus those slit
contours, which gives the + minus - jump in (6).

All limits in this deformation are justified at fixed N. Near the
j-th endpoint the integrand is O((r-1)^(-j/N)), which is integrable
because j<N. At infinity A_epsilon(t)=O(|t|^(-(N-1)/2)) on every
slit sector. The outer arc integral with t^(-a-1) is therefore
O(R^(-a-(N-1)/2)) and tends to zero. The finitely many sectors have
fixed marks. This argument does not require a single-valued branch
on an entire large base circle, including when infinity ramifies.
The small endpoint circles also tend to zero.

On the normalized cover the apparent endpoint singularity is even
more transparent. Set g=gcd(N,j), t-t_j=s^(N/g). Then
A_epsilon is a unit times s^(-j/g), and its product with dt has
order (N-j)/g-1>=0. Thus the lifted differential is holomorphic
at that ramification point. The slit description simply records
the marked combination of its sheet paths.

For N=2, (6) gives

    [t^a](1+t)^(-1/2)
       =(-1)^a/pi * integral_1^infinity
                          (r-1)^(-1/2)r^(-a-1)dr,

including the value one for a=0 and -1/2 for a=1. This checks
both the orientation and the full normalization.

## 3. Matrix transport and the whole original source

Expand the finite resolvent in (2) and apply (6) coefficientwise.
For every T^N=0, exactly

    v_(epsilon,N)(T)
      =sum_(j=1)^(N-1) sin(pi j/N)/pi
           *integral_1^infinity h_(epsilon,j)(r)
                          (rI-Q^(epsilon j)T)^-1 dr. (7)

This retains all original finite-head walls inside the NILPOTENT
matrix T. It does not replace T by an invertible Laurent shift.
There is no pole of this resolvent on r>=1. The same proof applies
to a matrix coefficient source sum_(a=0)^(N-1)B_a t^(-a-1): its
cut kernel is sum_a B_a Q^(epsilon j a)r^(-a-1).

Apply (7) in the original order to every factor of the full
9m-variable construction for an m-crossing braid. The Gaussian
diagonals, original caps, pivots, Cartan scalars, framing and
peripheral line are retained. The original scalar becomes a
sum over j_1,...,j_(9m) in {1,...,N-1} of integrals over
[1,infinity)^(9m). Its scalar jump weight is

    product_l sin(pi j_l/N)/pi,                    (8)

and its matrix/rational source is precisely the unchanged ordered
network with the cut kernels of (7). The upper endpoint and
infinity estimates above dominate every finite matrix entry by a
product of integrable one-variable functions at fixed N. Thus
Fubini and multilinearity justify the whole substitution, not
only its isolated scalar atoms.

This is an exact source-preserving global cycle deformation for
every original word. It does not assume geometricity, positivity
of an ideal triangulation, a nonvanishing Kashaev value, or a
large-level asymptotic. All original normalization factors remain
in the original source; no factor is chosen to fit a volume limit.

## 4. What this settles about cycle selection, and what it does not

The marked quantum cycle is now a completely specified convergent
combination of sheet paths on actual cyclic-dilogarithm covers.
Every local jump coefficient in (8) is nonzero. For indices whose
j_l/N stay in a compact subinterval of (0,1), these coefficients
are bounded above and below independently of N. Even over all
indices their loss is at worst polynomial at fixed braid length.

These statements control ONLY the local-system jump coefficients.
The remaining functions h, the ordered matrix source and their
full contraction are complex and may cancel. The number of cut
summands grows with N. None of these facts proves that a marked
geometric critical point lies on the selected deformation, that
its full derived coefficient is nonzero, or that the sum of all
other pieces has a smaller exponential rate.

The task is therefore no longer to invent a quantum cycle or to
guess its local branch weights. The remaining comparison must
carry this explicit whole cut cycle to the positive geometric
chart, preserving its matrix source and all branch orientations.
The positive-chart maximum and the actual-atom analytic regions
are available inputs; a global identification with the marked
Bloch regulator period is still unproved.

[Numerical sign and coefficient audit](../experiments/audit_cyclic_dilog_hankel_cycle.py).
The Cauchy deformation and estimates above, rather than those
finite diagnostics, prove (6)-(8) for all N.

## 5. Exact radial localization and a whole-word bound on infinity escape

The radial variables in this ACTUAL cycle have a uniform bound,
not merely fixed-N convergence. Put

    u=j/N,
    g_(epsilon,j)(r)=(r-1)^u h_(epsilon,j)(r),
    G_j=|g_(epsilon,j)(1)|,
    C_j=(N-1)/4-u/2.

The endpoint magnitude G_j is independent of epsilon. For r>1
and |w|=r the elementary identity

    d_(Log r) Log|1-w|
      =Re[w/(w-1)]
      =1/2+(r^2-1)/(2|1-w|^2)>1/2

applies to every non-endpoint factor of g. Consequently

    |g_(epsilon,j)(r)|<=G_j r^(-C_j),
    |h_(epsilon,j)(r)|<=G_j (r-1)^(-u)r^(-C_j).   (9)

Here C_j>=c_N:=(N-1)(N-2)/(4N)>=0. Euler's beta
integral gives the exact normalization

    sin(pi*u)/pi * integral_1^infinity
                           (r-1)^(-u) dr/r=1.

Thus for EVERY nonnegative coefficient order a and R>=1,

    sin(pi*u)/pi * integral_1^infinity
                       |h_(epsilon,j)(r)|r^(-a-1)dr <= G_j,
    sin(pi*u)/pi * integral_R^infinity
                       |h_(epsilon,j)(r)|r^(-a-1)dr
                                             <=G_j R^(-C_j). (10)

This controls all cuts, including indices approaching either end
of the index range. No lower bound on a jump weight is needed.

The endpoint weight is itself explicit:

    G_j=|(Q;Q)_j|/N^(j/N+1/2).                   (11)

For a direct verification put L_l=Log|1-Q^l|. Reindex k-j
modulo N in the product defining g(1), retaining the absent
k=0 factor with coefficient zero. Use

    sum_(l=1)^(N-1)L_l=Log N,
    sum_(l=1)^(N-1)l L_l=(N/2)Log N,
    L_(N-l)=L_l.

It follows that

    Log G_j=-(j/N+1/2)Log N
                         +sum_(l=N-j)^(N-1)L_l,

which is (11). Thus the endpoint is an original quantum-factorial
weight, with its complete polynomial normalization retained.

For the full all-inverse construction set s=9m. At |M|=1 the
[actual rational-source bound](actual_whole_word_cyclic_dilog_resolvent_period.md)
is

    |R_(beta,N)(t)|<=N^(b-1+6m) product_l |t_l|^(-1),
                                                |t_l|>=1. (12)

Its proof uses the literal truncated shifts, unitary root Gaussian
and pivotal diagonals, and the original averaged source. It does
not absorb the external dimension or framing line. Apply (10)
variable by variable to the absolute value of the whole cut
integral, and use a union bound for the s radial variables.
If P_tail(R) denotes the contribution with max_l r_l>=R,

    |P_tail(R)|
      <=|chi_(beta,N)| s N^(b-1+6m) R^(-c_N)
                                     (sum_(j=1)^(N-1)G_j)^s. (13)

The same bound without s R^(-c_N) bounds the full absolute
integral. This is a bound on the original whole source; it is
not a termwise claim about a substituted positive knot model.

Write J(v)=integral_0^v Log(2sin(pi*t))dt. The uniform
endpoint-aware factorial estimate already proved in
[the full-atom note](full_euler_atom_dilog_and_endpoint_regions.md)
gives

    Log G_j=N J(j/N)+O(Log N)

uniformly for 1<=j<N. Its maximum occurs at v=5/6 and is

    max J=Lambda(pi/6)/pi=v_3/(2pi),

where v_3 is the volume of a regular ideal tetrahedron.
At M=1 the original external line chi has polynomial size.
Since c_N/N tends to 1/4, (13) proves the unconditional
whole-word escape estimate

    limsup_(N->infinity) (1/N)Log|P_tail(R)|
      <=s v_3/(2pi)-(1/4)Log R.                  (14)

In particular any fixed R>exp(4s v_3/(2pi)) makes this
whole infinity tail exponentially small in ABSOLUTE size.
The required R depends on the fixed word, not on N. Thus
escape to infinity can be excluded as a competing positive
exponential contribution in this representation.

For smaller radial collars, (13) controls the tail relative to
the stated endpoint ABSOLUTE envelope. It does not imply
localization on an O(1/N) collar relative to the ACTUAL selected
period: cancellation may make that period much smaller than
the envelope. The angular/source coupling and a nonzero
geometric contribution remain unresolved. None of (9)-(14)
replaces that remaining lower-bound theorem.

[Radial and endpoint audit](../experiments/audit_actual_cut_radial_localization.py)
and [saved results](../experiments/actual_cut_radial_localization_results.json).

The subsequent [bulk radial theorem](full_cut_geometric_coupling.md)
evaluates each original coefficient moment with an explicit nonzero
Gamma symbol, uniformly in the actual coefficient order. The
[cyclic sewing comparison](exact_quantum_quad_source_transport.md)
instead splits the nilpotent transfers into cyclic resolvents and
mandatory boundary terms. For that split representation, use the
[regularized cut rule](cyclic_sewing_regularized_cut_cycle.md), which
retains its new endpoint finite parts and cyclic-pole residues. The
ordinary unsplit Hankel formula must not be applied to its terms
without those corrections.
