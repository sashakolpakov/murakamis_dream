# An original cup slide exposes an amplified normalization packet

29 October 2026. The problematic vector in the terminal-Gram transport
test is reached by a FIXED original braid prefix applied to the original
cup. The complete recorded packet after one further crossing has positive
exponential energy, although its original closed scalar is a unit phase.
There is also an explicit coherent factorial divergence which removes
this amplification at the normalization closure. This is a finite Ward
packet with its endpoint retained, rather than a deletion of individual
channels or a new positive trace.

The result concerns the present full-circle/recorded-color metric. It
does not rule out a nondiagonal coherent metric, a shrinking arc, or a
sharp estimate on a source after coherent normalization pruning.
The [backward Ward disk estimate](actual_normalization_clock_disk_bound.md)
now proves subexponential shrinking-arc energy for this SAME original
normalization packet, including its whole germ and specified sublinear
clock-frequency exteriors.

## 1. A literal source identity on every input color

Use the original complete multiplicity conventions:

    N>=2, d=N-1, q=exp(pi i/N), Q=q^2, x=q^d=-q^-1,
    F_j=(Q;Q)_j, kappa=q^(d^2/2), kappa^2=x^d,
    W=(V tensor V)_(integer degree d), e_j=|j,d-j>,
    p_j=N x^(j-d), ell_j=x^j/N.

Let R=R_12 be the FULL original positive pair crossing on W and
R_23 its adjacent complete multiplicity operator. The original highest
chart, applied to the literal physical crossing, gives

    (R_23 p)_j=kappa N x^(j-d) F_(d-j),
    (R^(-1)e_0)_j=kappa^(-1)x^j F_(d-j).

Consequently the exact source-orbit identities are

    R_23 p=N R^(-1)e_0,
    R R_23 p=N e_0.                                      (1)

There is no arbitrary inserted state in (1). The Cartan identity
kappa^2=x^d fixes the coefficient N at every even or composite level.
The negative coefficient is the literal original inverse crossing,
not a unitary adjoint.

For completeness the second identity has a direct finite-binomial
proof. Multiplying the original positive coefficients yields

    (R R_23 p)_i
      =N x^(-i) Q^[i(d-i)] F_i
           sum_(k=0)^i (Q^(-i);Q)_k Q^(ik)/F_k
      =N x^(-i) Q^[i(d-i)] F_i (1;Q)_i
      =N delta_(i,0).                                    (2)

Every factorial denominator in this calculation has index below N.
The equality is the highest column of the all-input physical cup slide

    (R_12 R_23)(p_12 tensor I_V)=I_V tensor p_23.           (3)

Indeed both sides intertwine the ACTUAL coproduct. Applying its F^a/F_a
to the verified highest column proves (3) on every original |a>,
0<=a<N. Thus (3) is an operator identity and can be tensored with
arbitrary spectator ports. No scalar-knot Schur argument or replacement
of the marked row is used.

## 2. Complete terminal packets and their original closed scalars

Keep the [full terminal operator](actual_terminal_packet_closed_kernel.md)

    T=N^(-1) X R P_rev R, X=diag(x^j),
    P_0=1, P_j=(1-Q^j)^2 P_(j-1)+Q^j,
    P_rev=diag(P_(d-j)), P_d=sum_(j=0)^d F_j.              (4)

Its physical-projector rows sum to the original ordinary/marked whole
co-source after the two terminal crossings. This is the SAME complete
source as in the [positive terminal Gram](actual_terminal_packet_positive_gram.md).
Retain the original external factor chi_N on every side below.

The two actual prefixes [2] and [2,1] give the exact vector formulas

    T R_23 p=kappa P_d e_d,
    b:=T R R_23 p
      =x^(-d) (Q^(-j) conjugate(F_j))_(j=0)^d.             (5)

To check the first formula, write T R^(-1)=N^(-1)X R P_rev,
use (1) and R e_0=kappa x^(-d)e_d. For the second use

    (R e_d)_j=kappa N x^(j-d)/F_(d-j),
    F_(d-j) conjugate(F_j)=N,
    x^2=Q^(-1), kappa^2=x^d.

These retain all coherent Green summation; P_j is never replaced by
its absolute envelope. In particular

    ||T R_23p||^2=|P_d|^2<=9N^4,
    ||T R R_23p||^2=Z_N:=sum_(j=0)^d |F_j|^2.             (6)

The first bound is the original endpoint theorem in the
[Green-capacity proof](actual_terminal_green_capacity_bound.md).
It is not a bound on the sum of absolute factorials.

Both original closed scalars remain explicit:

    1^T T R_23p=kappa P_d,
    1^T b=x^(-d) Q.                                     (7)

For the last equality, Q^(j+1)F_j=F_j-F_(j+1), with F_N=0,
implies sum_j Q^(-j)conjugate(F_j)=Q. Thus the second full word
[2,1,2,2] is a normalization source with raw scalar of modulus one.
No phase is fitted from its scalar value. The original chi_N multiplies
both this scalar and the corresponding packet; any specified framing
normalization remains literal.

The usual uniform factorial estimate, with
J(t)=integral_0^t log(2sin(pi s))ds, gives

    log Z_N=N v_3/pi+O(log N),                           (8)

where v_3 is the volume of the regular ideal tetrahedron. Its proof is
elementary: log|F_j|=N J(j/N)+O(log N) uniformly to both endpoints,
and J has maximum v_3/(2pi) at5/6. A nearest lattice point supplies
the lower bound; N terms supply the upper bound.

Thus a fixed original source trajectory, rather than only an arbitrary
all-port vector, realizes the exponential metric-motion obstruction in
[the terminal-Gram test](actual_terminal_gram_lyapunov_obstruction.md).
With epsilon=exp(-N^2), the same exact regularized quotient there is
obtained after multiplying both test vectors by N. A source-dependent
changing metric or a further coherent packet is not excluded.

## 3. Exact coherent pruning and the retained exterior current

The amplified vector (5) is a particularly simple finite divergence.
Put G_j=conjugate(F_j) for0<=j<N and G_N=0. Then

    b_j=x^(-d) Q(G_j-G_(j+1)).                           (9)

For ANY row f_j of scalar, vector or operator-valued spectator
coefficients, distributivity alone proves

    sum_j f_j b_j
      =x^(-d)Q [f_0+sum_(j=1)^d(f_j-f_(j-1))G_j].        (10)

No commutativity of the f_j is needed. The factorial factors G_j are
fixed scalars. The original constant closing row kills the interior
differences and retains the unit endpoint f_0. A general exterior
instead keeps the explicit finite-difference current in (10).

The difference matrix in (9) has operator norm at most2, and its
finite cumulative inverse has norm at most N. These are coefficient
bounds; G itself has exponential norm. Accordingly (10) supplies a
source-preserving coherent normalization pruning operation. It does
NOT give a bound for a general exterior by dropping its difference.
This is the exact point at which an iterated bridge estimate needs
the neighboring original Ward equations or another coherent identity.

## 4. Arbitrary diagonal recorded-color metrics cannot repair this source

For any positive diagonal packet metric D=diag(w_j), including weights
with arbitrary N dependence, the complete Cauchy budget is

    (1^T D^(-1)1)(b^*Db)
      =(sum_j w_j^(-1))(sum_j w_j |F_j|^2)
      >=(sum_j |F_j|)^2.                                (11)

The minimum is exactly the right side: choose w_j=1/|F_j|, since
every F_j with j<N is nonzero. Uniform factorial asymptotics show its
logarithmic rate is again N v_3/pi+O(log N), while the squared raw
scalar in (7) is one. This is a complete coherent packet counterexample
to a diagonal recorded-color metric, not a sum of isolated shear paths.

A genuinely nondiagonal metric can retain the telescoping in (9).
Neither (11) nor the full-circle energy proves failure of the
[shrinking-arc metric](actual_shrinking_arc_cauchy_metric.md). Indeed
the first jet of this particular packet is still polynomial: summation
by parts gives

    sum_j j b_j=x^(-d)Q conjugate(P_d-1).

In fact the [whole normalization germ](actual_normalization_clock_disk_bound.md)
is polynomial on disks of radius C/N, and subexponential on EVERY
shrinking disk. Its shrinking-arc energy therefore has rate zero.
This uses the complete backward Ward recurrence, beyond the first-jet
identity above. The distinct source
in [the jet diagnostic](actual_terminal_shrinking_arc_jet_diagnostic.md)
still has no proved positive all-N jet exponent.

## 5. Audit and scope

[The audit](../experiments/audit_actual_terminal_source_normalization_packet.py)
checks (3) on EVERY physical input color directly from the original
signed matrices, not from a chosen reduced R_23. It also extracts the
complete highest chart, verifies (1),(5)--(7) on every retained packet,
and checks (10) with noncommuting spectator matrices. Complex tests
verify the complete energies and the optimized diagonal budget.

The algebraic and asymptotic proofs above are all-level. The resulting
normalization move is source-exact and usable with arbitrary spectators;
the remaining finite-difference exterior in (10) is retained. No broad
knot-volume upper bound or selected geometric noncancellation follows.

The finite terminal checks concern the displayed normalization identities only.