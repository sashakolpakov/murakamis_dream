# The original whole word as a marked cyclic-dilogarithm resolvent period

28 October 2026. Every actual signed braid word admits an exact
period on a product of the literature cyclic-dilogarithm curves.
The marked cycle and its full original cap are specified, and
the finite-head walls are retained inside rational resolvents.
There is no restriction on a geometric atom argument, or
asymptotic replacement of a finite polynomial by a chosen phase.

The cyclic dilogarithm and its nilpotent anchoring were already
proved in [the unfolded Ward calculation](unfolded_ward_factorial_and_regulator.md)
and [the Rees crossing calculation](rees_whole_crossing_source_factorization.md).
The [full-atom note](full_euler_atom_dilog_and_endpoint_regions.md)
also gives their exact scalar Taylor Cauchy formula. The new
content here is their contraction into the original strict signed
word with the specified source and an explicit product cycle.
This constructs a global algebraic period representation; it does
not prove a geometric intersection number or a volume estimate.

## 1. The marked curve realizes the literal nilpotent operators

Put `Q=exp(2pi*i/N)` and let C_N be the normalization of

    y^N=product_(j=1)^(N-1)(1-Q^j t)^j.          (1)

At t=0 choose the sheet y=1. On its disk `|t|<1` this specifies
the analytic function

    D_N(t)=product_(j=1)^(N-1)(1-Q^j t)^(j/N).

All powers have their common constant-one mark, rather than
independent roots chosen after specialization. Weighted root
summation gives for `1<=a<N`

    [t^a]log D_N=1/[a(1-Q^a)].                 (2)

Consequently the first N Taylor coefficients of D_N and its
inverse are precisely those of the literal u_N and v_N. For
ANY actual nilpotent matrix T with `T^N=0`, and any `0<r<1`,

    u_N(T)= (1/(2pi*i)) integral_(gamma_0)
                                  y(t)(tI-T)^-1 dt,
    v_N(T)= (1/(2pi*i)) integral_(gamma_0)
                               y(t)^-1(tI-T)^-1 dt.    (3)

Here gamma_0 is the positively oriented circle `|t|=r` lifted
to that sheet of C_N. It is closed. Expand the exact resolvent

    (tI-T)^-1=sum_(a=0)^(N-1)T^a t^(-a-1).    (4)

Termwise Cauchy evaluation and (2) prove (3). Thus this is exact
holomorphic functional calculus on the actual finite head. It
does not claim that the scalar evaluations u_N(z) and D_N(z)
agree away from a nilpotent argument.

## 2. The full original rational source kernel

Use the strict factorization in
[the original Euler/Gaussian network](actual_euler_gaussian_cauchy_network.md):

    C=F_2 U_- F_1 F_2^-1,
    C^-1=F_2 F_1^-1 V_- F_2^-1,
    R_+=kappa C D U_+ C^-1,
    R_-=kappa^-1 C V_+ D^-1 C^-1,

where `U_±=u_N(T_±)`, `V_±=v_N(T_±)`,
`T_-=x^-1 S_1^-S_2^+`, `T_+=x^-1 S_1^+S_2^-`.
Every T has Nth power zero. Spectator heads are extended by
identity. Every crossing has exactly three such Euler atoms;
its factorial and Gaussian factors remain the specified matrices.

Let beta have b heads and m signed crossings, and let
`A_L ... A_1`, `L=10m`, be its literal stripped matrix word in
the correct order. Mark its `r=3m` Euler slots by `j=1,...,r`.
At slot j set `sigma_j=+1` for u and `-1` for v and replace
its factor by the rational matrix

    mathscr R_j(t_j)=(t_j I-T_j)^-1.            (5)

All other factors retain their actual values. Write B_l for
the resulting factors. Let the original averaged first-cut
functional be

    Phi_(b,N)(W)=(1/N) sum_(a,c,k_2,...,k_b)
       (product_(i=2)^b g_(k_i))
              W_((c,k_2,...,k_b),(a,k_2,...,k_b)),
    g_k=(xQ^-k)^(1-N).                         (6)

One may instead keep the original fixed-first-input-zero source
by fixing a=0 and removing 1/N. The equality of their original
uninserted knot closures is the prior scalar-closure theorem;
no equality for arbitrary inserted resolvents is assumed here.
Choose one of these original sources and keep it throughout.
Define the rational scalar

    R_(beta,N)(t_1,...,t_r)=Phi_(b,N)(B_L ... B_1). (7)

This is an entirely explicit rational function with poles only
at the coordinate loci `t_j=0`; its Laurent powers in each
variable run from -1 through -N. It retains every finite-head
projector because each T_j is the literal truncated transfer.
It also retains all pivotal closures and the first-cut coupon.
There is no quotient that kills the degree-zero wall terms.

If chi is the original external dimension, framing and common
Cartan factor, included exactly once, then the original scalar is

    P_(beta,N)(M)=chi_(beta,N)(M)/(2pi*i)^r
       integral_(gamma_0^r)
           R_(beta,N)(t) product_(j=1)^r y_j^(sigma_j) dt_j. (8)

The proof applies (3) to each slot, in its original order, and
then the finite linear functional (6). No Fubini convergence
issue arises on the compact small circles: the matrices have
finite dimension and the curves are regular there. Equation
(8) holds for the full root meridian family, with the same
external factors as the actual invariant. It is not an assertion
about generic-q normal derivatives.

Thus the desired first step of the torsor route is concrete:
the algebraic curve, the meromorphic differential, and the
original marked cycle are all supplied. The number r of curve
factors depends on the braid word, not on N. The curve and
source rational function themselves do depend on N.

There is also a FULL version with no factorial constants hidden
in the rational source. The exact reflection identity is

    F_a=N Q^(-a-1) [t^(N-1-a)]D_N(t)^-1.

Consequently replace each factorial diagonal on its head by

    F^-1=(1/(2pi*i)) integral_(gamma_0)
                         y diag_(a)(t^(-a-1)) dt,
    F=(1/(2pi*i)) integral_(gamma_0)
                   y^-1 diag_(a)(N Q^(-a-1)t^(a-N)) dt. (9)

Every crossing has six such factorial diagonals and three
transfer Euler atoms. Apply (9) to all six. Formula (8) now
holds on `C_N^(9m)` with a new rational source formed by the
same ordered matrix contraction; its only remaining local
constants are the specified Gaussian diagonals and explicit
powers of N,Q,x. Their marked Gaussian phase and all external
Cartan, dimension and framing factors are retained. All actual
factorial growth is inside the cyclic-dilogarithm differential.
Both the minimal `3m` and full `9m` representations are exact.

## 3. An all-inverse realization with no growing infinity factors

An exact change of auxiliary completion makes the cut-cycle
problem simpler. Write `v_(Q^-1)` for the SAME finite factorial
formula with Q replaced by its inverse. Directly,

    (Q^-1;Q^-1)_a=(-1)^a Q^(-a(a+1)/2)F_a,
    [t^a]v_(Q^-1)(t)=Q^a/F_a,
    u_Q(T)=v_(Q^-1)(Q^-1 T).                   (10)

These are identities of the actual finite polynomials and
operators, not conjugations of the physical invariant. Define
C_(N,epsilon) by (1) with `Q^j` replaced by `Q^(epsilon*j)`;
its y=1 sheet at zero is the corresponding cyclic dilogarithm.
Equation (10) replaces each u resolvent in (8) EXACTLY by

    (1/(2pi*i)) integral_(gamma_0 on C_(N,-1))
                      y^-1(tI-Q^-1 T)^-1 dt.   (11)

For the full factorial version replace F^-1 by

    (1/(2pi*i)) integral_(gamma_0 on C_(N,-1))
                         y^-1 diag_(a)(Q^-a t^(-a-1)) dt, (12)

while F still uses the inverse-y formula in (9) on C_(N,+1).
The v transfers likewise keep their original inverse-y curve.
Thus the full original word is an exact period on a product
of `9m` oriented curves C_(N,epsilon), with EVERY algebraic
factor equal to y^-1. All physical Gaussian, pivotal, Cartan,
framing and dimension factors are unchanged. The rational
source is formed by the same original ordered contraction.

This auxiliary completion changes the analytic function beyond
its first N Taylor coefficients. It does not discard the
infinity contribution of the old positive-y representation;
it supplies a different exact period for the same finite
operator. No generic-q continuation follows from it.

For every variable in this all-inverse realization, the rational
matrix kernel is `O(t^-1)` at infinity. Also

    |y^-1|=O(|t|^(-(N-1)/2)).                  (13)

Every outer cut arc therefore has integral tending to zero in
absolute value, for every fixed N>=2. At a root `t=Q^(-epsilon*j)`
the exponent of y^-1 is `-j/N>-1`, so each cut endpoint is
integrable. Consequently all variables admit convergent radial
cut deformations without an infinity regularization. The banks
and monodromy of these cuts must be kept on the chosen sheet.
For even N a large base circle need not close on a single
sheet; (13) applies to its cut arcs, not to an unmarked closed
lift asserted without proof.

On the normalization the finite branch endpoints do not in fact
produce poles of the differential. If `g=gcd(N,j)`, a uniformizer
has `t-alpha=s^(N/g)` and `y=unit*s^(j/g)`. Hence `y^-1 dt`
has nonnegative order `(N-j)/g-1`. The rational matrix kernel
is regular at alpha. The cut deformation is genuine sheet and
homology transport, not a sum of residues at those branch points.
The [explicit Hankel cycle theorem](actual_cyclic_dilog_hankel_cycle.md)
computes these banks and their exact nonzero sine weights, and
carries them through the entire original ordered source.

## 4. The full original source is polynomially bounded on these cuts

At `|M|=1` one has `|x|=1`. Equip the actual head basis with
its ordinary Euclidean norm. Each truncated transfer and its
Q^-1 multiple have operator norm at most one. Therefore on the
ENTIRE exterior `|t|>=1`, including its endpoint circle,

    ||(tI-T)^-1|| <= sum_(a=0)^(N-1)|t|^(-a-1)
                                             <= N/|t|. (14)

The full all-inverse factorial kernels obey

    ||diag_(a)(Q^-a t^(-a-1))||<=1/|t|,
    ||diag_(a)(NQ^(-a-1)t^(a-N))||<=N/|t|.     (15)

Every Gaussian diagonal is unitary here. The averaged original
cut in (6) is `Tr[(E tensor G^(tensor(b-1)))W]`, where
`E=J/N` is the rank-one orthogonal projection onto the constant
head vector and G is the unitary pivotal diagonal. Its trace
norm is exactly `N^(b-1)`. Thus `|Phi(W)|<=N^(b-1)||W||`.

Each crossing contains three transfer resolvents, three direct
factorial kernels and three inverse-factorial kernels. Taking
the norm of their original ordered product proves the uniform
bound for the full all-inverse rational source

    |R_(beta,N)(t)|
       <= N^(b-1+6m) product_(j=1)^(9m)|t_j|^-1,
       whenever all |t_j|>=1 and |M|=1.        (16)

For the retained fixed-first-input-zero source, its first coupon
has trace norm sqrt(N); the right side acquires only that
additional factor. No actual source is replaced to obtain a
bound. A fixed total number k of logarithmic t-derivatives
costs at most a constant depending on k,m times an additional
factor `N^k`, by differentiating the finite resolvents and
diagonal monomials. Thus the whole rational source has no
hidden exponential growth on the canonical exterior cut chain.

This global upper-amplitude control is unconditional for the
specified root source. It supplies neither a lower bound nor
a nonzero geometric coefficient. A complex rational source
bounded by a polynomial may still carry rapidly varying phase
or vanish on the relevant critical image. Those remain part
of the cycle-selection and lower-bound question.

## 5. What a global cut deformation must retain

Unlike the finite scalar Euler polynomials, the y factors in
(8) have genuine branch divisors at `t=Q^-j`. This puts a
possible cut deformation on an actual marked algebraic cover.
The resolvent expression avoids replacing a finite projector
by a spurious reproducing pole. Any subsequent deformation
must still be an equality of marked cycles on this cover,
with its infinity and branch-boundary terms retained.

For example the leading magnitude of `y` at infinity is
`|t|^((N-1)/2)`; its inverse decays by that order. Formula (4)
therefore gives automatically decaying infinity behavior for
each v-variable coefficient. For a positive-y u-variable
coefficient of T^a, the absolute-decay argument applies when
`a>(N-1)/2`; it gives no automatic vanishing below that threshold.
Lower powers may need a boundary or Taylor regularization.
Whether the original source cancels their coefficients is an
explicit question about (7), not a freedom to discard them.
Nonzero examples occur in the actual figure-eight word in the
audit. The all-inverse realization above avoids that particular
regularization problem by an exact change of auxiliary curve.

The marked small circle in (8) is now a definite cycle whose
branch-cut or relative-chain image can be computed. It has not
been proved to project with degree one to a positive Rivin
angle domain, nor to have nonzero geometric thimble coefficient.
Equation (8) avoids assuming that coefficient; it is a suitable
starting point for proving or disproving the needed cycle map.

The [exact audit](../experiments/audit_whole_word_cyclic_dilog_resolvent.py)
checks the Taylor identification from the fractional product,
each original signed crossing, whole signed words with their
original cap, and the retained low-power u-source terms.
