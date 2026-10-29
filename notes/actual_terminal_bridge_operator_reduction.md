# An open six-head bridge reduces exactly to a typed current and angle packet

29 October 2026. The first bridge crossing that couples the two ordinary
cap pairs of a six-head source can be eliminated as an EXACT map between
complete multiplicity modules. The cap forces one physical transfer.
All spectator inputs and operator coefficients remain open. The resulting
six-head terminal packet is the four-head packet composed with the map
below, not a scalar knot-by-knot replacement.

The through-head feedback factors into a contractive strict shift and
a unitary clock in a source-fixing factorial metric. Its remaining
angle coefficient is explicit. It has EXTRA factorial powers, so this
does not yet prove the requested reduction to one half-density angle
cell or a sharp arbitrary-prefix energy estimate. The actual remaining
charge and operator, rather than an unspecified boundary current, are
identified in (9)--(12).

## 1. Complete source modules and the physical terminal

Use the original principal root N>=2,d=N-1,q=exp(pi*i/N),Q=q^2,
x=q^d=-q^-1,F_a=(Q;Q)_a,s_a=|F_a|,kappa=q^(d^2/2).
All crossings and turns are literal original physical ones from
[the complete source module](actual_complete_source_multiplicity_module.md).
In particular

    ell|a,b>=x^(-a)Q^(-a)/N delta_(a+b,d),
    p_(a,b)=N x^(-b)delta_(a+b,d).

Let

    W_2=(V^tensor4)_(degree2d), W_1=(V^tensor2)_(degree d),
    L_0=ell_12 tensor I_34:W_2->W_1.

Let I_w:V->V^tensor5 be the COMPLETE intertwiner of w in W_2,
and D_2 w=I_w|d>. Define the six-head-source terminal rows by

    T_n^(6)=(ell_12 ell_34 tensor <d|_5)
                     (I_123 tensor R_45^2) Pi_(4,n) D_2.

The last marked cap has already been justified through the whole
invariant-tensor source; it is not individually replaced by ell.
Let T_n^(4) be the corresponding original three-physical-head
terminal on W_1 from
[the positive terminal packet](actual_terminal_packet_positive_gram.md).

Since the cap ell_12 is a Hopf map, deleting it commutes with every
prefix coproduct in the highest/lowest intertwiner. In particular

    (ell_12 tensor I_345)I_w=I_(L_0 w).

It also commutes with the specific terminal R_45^2 and Pi_(4,n).
Consequently, for EVERY input column and every adjoining exterior,

    T_n^(6)=T_n^(4)L_0.                                  (1)

Now place ONE actual adjacent signed bridge crossing R_23^epsilon
immediately before that terminal. It acts on the middle two physical
heads of W_2, so define

    L_epsilon=L_0 R_23^epsilon:W_2->W_1.

The complete source identity becomes

    T_n^(6) R_23^epsilon=T_n^(4)L_epsilon.                (2)

This keeps the crossing that couples the eliminated cap to the
remaining port. It is not commuted past the cap as an unknown scalar.

## 2. Every entry of the positive open bridge, with the original phases

Take an input |a,b,c,e> of integer degree2d. For epsilon=+1 the
cap forces the actual transfer and surviving output to be

    k=d-a-c, u=b-k, output |u,e>, u+e=d,
    0<=k<=min(b,d-c).                                    (3)

There is exactly ONE original positive crossing coefficient, so

    (L_+)_(u;(a,b,c,e))
      =kappa/N x^(-a-b-c+k)Q^(-a+cu)
                    F_(d-a)F_b/(F_k F_c F_u),             (4)

with zero outside (3). This follows directly by multiplying the
cap with the literal R coefficient. In particular the original
common Cartan kappa and cap1/N have not been discarded.

The true nonnegative angle charges are

    a+c+k=d.                                             (5)

The through-head relation b=u+k is a SECOND actual constraint;
the spectator is e=d-u. Thus the external through degree has
not been frozen independently of the angle charge k.

Root reflection F_aF_(d-a)=N(-1)^aQ^[a(a+1)/2] rewrites (4) as
a phase times

    F_b/(F_a F_c F_k F_u).

This is a closed finite kernel, not a sum of absolute paths. Tensoring
an arbitrary spectator space leaves (2)--(5) unchanged. If the input
entries are matrices on that space, they multiply this kernel in
their original order. No commutation of spectator operators is used.

## 3. The negative bridge and its retained complement charges

For epsilon=-1 the literal negative crossing instead forces

    k=a+c-d, u=b+k, output |u,e>, u+e=d,
    0<=k<=min(c,d-b).

Its exact full coefficient is

    (L_-)_(u;(a,b,c,e))
      =kappa^(-1)/N (-1)^k x^(b+c-k-a)
          Q^[-bc-ck+k(k-1)/2-a]
                        F_u F_c/(F_k F_b F_(d-a)).        (6)

If A=d-a and C=d-c, its nonnegative charges are

    A+C+k=d, b=u-k.                                     (7)

Equations (6)--(7), including their phase, are the actual negative
source kernel. They are not obtained by deleting an end channel or
assuming a scalar beta identity for noncommuting ports.

## 4. The full feedback is a contractive physical current in a typed metric

Use the PHYSICAL diagonal coordinate gauge

    G_a=s_a/sqrt(N)=L_a^(1/2), tau_a=F_a/s_a.

It fixes every original paired cup and ordinary cap because
G_aG_(d-a)=1. The full marked source is transported literally;
on the assembled invariant source its complementary-degree
restriction is the one already proved in the complete module.
This is not the different quarter physical gauge or length gauge.

For the POSITIVE bridge conjugate input and output heads by G.
On the total-degree slices the output pair is complementary, so
its product gauge is one. Equation (4) factors EXACTLY as

    Lhat_+ entry=gamma_(a,c,k) U_(c,k)[u,b],
    gamma_(a,c,k)
      =kappa N (-1)^a x^(-d+k) Q^[a(a-1)/2]
                               /(s_a s_c F_a F_c F_k),
    U_(c,k)|b>=1_(b>=k) x^(-u)Q^(cu)
                           tau_b/tau_u |u>, u=b-k.      (8)

Every nonzero coefficient of U is a UNIT PHASE and different
inputs have different outputs. Hence ||U_(c,k)||_op=1 for k<N.
More intrinsically it is the literal strict lowering current
G(F^T)^kG^-1, followed by the unitary clock x^(-J)Q^(cJ).
The condition u+e=d is a final orthogonal degree projector on
the retained head and its untouched spectator; its norm is1.

For the NEGATIVE bridge use the dual source-fixing gauge G^-1.
With A,C as in (7), its exact factorization is

    Lhat_- entry=gamma^-_(A,C,k) U^-_(c,k)[u,b],
    gamma^-_(A,C,k)=kappa^(-1)N(-1)^(k+C)x^(A-C-2k)
          Q^[C(C+1)/2+k(k-1)/2-a]
                               /(s_A s_C F_A F_C F_k),
    U^-_(c,k)|b>=1_(b+k<N) x^u Q^(-cu)
                           tau_u/tau_b |u>, u=b+k.       (9)

This is a unitary clock times the contractive strict raising
G^-1 F^k G. No cyclic wrap or transfer alias is added. These
typed gauges both fix the original paired turns, but they are
different: changing between them across a later overlap retains
the actual G^2 interface. It is not declared polynomial.

## 5. What remains after one exact bridge elimination

Both scalar factors have the same known magnitude on their actual
angle triple, denoted (A,C,k) in the signed typed coordinates:

    |gamma|=N/(s_A^2 s_C^2 s_k).                         (10)

Thus feedback has been isolated as a contractive operator rather
than estimated by an arbitrary exterior norm. But the scalar energy
is NOT the single half-density-cell weight w_d(A,C,k):

    |gamma|^2=N^2/(s_A^4 s_C^4 s_k^2).

The extra factorial powers are genuine in the exact kernel. They
must be grouped coherently with the subsequent T packet or another
physical boundary contraction. Deleting them would change (4),(6).
This identifies the specific missing angle-energy comparison; it
does not rule out such a further coherent contraction.

For completeness the entire open bridge has an exact row Gram in
these typed source metrics. Rows have disjoint spectator color e.
Therefore

    Lhat_+ Lhat_+^*=diag(E_+(u)),
    E_+(u)=N^2 sum_(k=0)^(d-u) s_k^(-2)
                     sum_(A+C=d-k) s_A^(-4)s_C^(-4),
    E_-(u)=E_+(d-u).                                    (11)

Equation (11) retains the actual restriction k<=d-u, or k<=u
in the negative orientation. It is not replaced by independent
unconstrained tetrahedra or by an ideal-edge angle equation.

Most importantly (2) remains the COHERENT composition, so its
pointed doubled energy for any vector- or operator-valued input is

    sum_n ||T_n^(4)L_epsilon w||^2.                     (12)

No diagonal sum of |gamma|^2 paths has been inserted into (12).
The [closed all-input terminal kernel](actual_terminal_packet_closed_kernel.md)
now makes this remaining operator explicit: each six-head entry is
T_(n,u) times (4) or (6), with u=b-k or b+k and u=d-e.
Its Newton register t has the ACTUAL bounds t<=min(n,u), and
its scalar multiplier is the retained partial factorial Green
P_t=F_t^2 sum_(v<=t)Q^v/F_v^2. The associated terminal angle
triple is (t,n-t,d-n). These are coupled integer port constraints,
not independently adjustable spectator variables or a full ideal-edge
sum. The partial Green and its coherent clock/shift ordering are not
replaced by a scalar norm when composing (12).
By the terminal packet theorem, the row sum factors the ORIGINAL
co-source. Consequently

    H_epsilon=(T^(4)L_epsilon)^*(T^(4)L_epsilon)
                                      +exp(-N^2)I

is a positive Gram on the complete W_2, and its exact boundary
dual norm squared is at most N. The regularizer is negligible
for fixed original prefixes by the original physical bound.
This polynomial dual cost is independent of the spectator ports.
Its sharp energy still requires controlling the full composition
(12), including every noncommuting clock/shift interface (8),(9).

### The exact row Gram has a uniform pointed octahedral profile

Let Lambda(theta)=-integral_0^theta log(2sin t)dt, and
v_8=8Lambda(pi/4). Equation (11) has a quantitative asymptotic
UNIFORM in EVERY output color, including u=0 and u=d:

    log E_+(u)=(N/pi)H(u/N)+O(log N),
    H(t)=v_8,                                 0<=t<=1/2,
    H(t)=8Lambda(pi*t/2)-2Lambda(pi*t),        1/2<=t<=1,
    log E_-(u)=(N/pi)H(1-u/N)+O(log N).                 (13)

The implicit constant is independent of u. In particular the
COMPLETE open bridge, in its indicated signed source metric, obeys

    log ||Lhat_+||_op^2=log ||Lhat_-||_op^2
                                      =N v_8/pi+O(log N). (14)

This is an actual pointed row-capacity formula; it is not obtained
by maximizing unconstrained independent tetrahedron weights.

Here is a proof including its boundary uniformity. The uniform
sine-factorial estimate gives the exponent of a term in (11) as

    (N/pi)[4Lambda(alpha)+4Lambda(chi)+2Lambda(kappa)]
                                                     +O(log N),

where alpha=pi*A/N, chi=pi*C/N, kappa=pi*k/N. The exact
sum is pi*d/N and the actual upper bound is k<=d-u. Replacing
d/N by1 changes the maximized exponent by O(log N): Lambda
has uniform modulus O(delta*(1+|log delta|)) even at0 and pi.
For a fixed limiting kappa, alpha+chi=pi-kappa. The unique
maximum is alpha=chi=(pi-kappa)/2. Indeed the second derivative
on this interval is proportional to

    -cot(alpha)-cot(chi)=-sin(alpha+chi)/(sin alpha sin chi)<0.

The limiting endpoints follow by continuity. The resulting action is

    F(kappa)=8Lambda((pi-kappa)/2)+2Lambda(kappa),
    F'(kappa)=2log cot(kappa/2),
    F''(kappa)=-(tan(kappa/2)+cot(kappa/2))<0.

It peaks at kappa=pi/2, with value v_8. The REAL allowed interval
is0<=kappa<=pi*(1-u/N), up to its exact1/N endpoint shift.
If u/N<=1/2 it contains the maximum; otherwise its maximum is
the upper endpoint. Using Lambda(pi-theta)=-Lambda(theta)
gives exactly H in (13).

For the discrete lower bound choose k nearest N/2, clipped to
0,...,d-u, and choose A,C differing by at most one with sum d-k.
Every coordinate differs from a limiting optimizer by O(1/N),
uniformly also when the allowed interval collapses. The modulus
of Lambda therefore costs only O(log N) after multiplication by N.
There are at most N^2 positive terms, and every factorial estimate
has the same O(log N) error. Taking the largest term and then
summing proves both bounds in (13) uniformly. The negative formula
uses the exact mirror E_-(u)=E_+(d-u); replacing (d-u)/N by
1-u/N has the same uniform logarithmic error. Finally E_+ is
exactly nonincreasing in u, so its maximum row is u=0; its signed
mirror has the same maximum. This proves (14).

Thus the remaining weighted angle packet has a precise octahedral
capacity depending on the retained output color. Replacing every
bridge by its free maximum v_8 would discard the correlations and
can overcount the knot volume. Whether its coherent gluing to T
enforces the needed GLOBAL geometric angle constraints is not
proved by (13)--(14).

### Exact source-fixing pair-degree biases

There is additional nontrivial metric freedom with NO original
paired-boundary cost. On input heads1,2 multiply the physical
coordinate gauges by exp(lambda_1*(j-d/2)) on each head, and
on heads3,4 by exp(lambda_2*(j-d/2)). On the output pair use
any common exp(lambda_out*(j-d/2)). Every original cup and
ordinary cap is fixed pointwise, because its pair degree is d.
The assembled marked source retains its original complementary
degree restriction and is therefore fixed as well.

For an entry (3), the input pair degree is

    a+b-d=u-c, c+e-d=c-u.

The output pair has degree d. Thus the EXACT change of coefficient
is exp(delta*(c-u)), where delta=lambda_1-lambda_2. This uses
the original physical charge; it is not an adjustable geometric
edge label. The full positive row Gram becomes

    E_(+,delta)(u)=N^2 sum_(k<=d-u) sum_(a+c=d-k)
           exp(2delta*(c-u))/(s_a^4 s_c^4 s_k^2).         (15)

For delta in any fixed compact real set, the same uniform factorial
and rounding proof gives

    log E_(+,delta)(u)=(N/pi) max
      [4Lambda(pi*a)+4Lambda(pi*c)+2Lambda(pi*k)
                                      +2pi*delta*(c-t)]
                          +O(log N), t=u/N,              (16)

where a,c,k>=0, a+c+k=1 and k<=1-t. Its error is uniform in
u and in that delta set. For fixed k at an interior maximizer
the tilted A,C equation is sin(pi*c)/sin(pi*a)=exp(delta/2).
No optimization over delta or global gluing theorem is claimed.

These gauges can therefore encode pair-degree constraints without
an exponential source norm. Interfaces with preceding/following
crossings must still be transported. In particular the factor
exp(-delta*u) is an actual through-head degree clock; it is not
a unitary factor that can be discarded from (8) or (12).

## 6. Verification and scope

[Audit](../experiments/audit_actual_terminal_bridge_operator_reduction.py)
uses original signed R matrices and the full original E/F
intertwiner construction. Fresh replay PASS: seven all-input signed
bridge maps N=2,...,8; three COMPLETE six-head-to-four-head terminal
identities N=2,3,4; and seven physical source/current metric families.
It verifies the complete phases in (4),(6),(8),(9), both gauges,
every spectator color, and the exact row Grams (11).
Six further growing-level row-profile families through N=256
check the uniform endpoint/interior profile (13) and its mirror.

The proof is all-level and all-exterior. Its new operation is an
actual open bridge contraction with explicit angle/current feedback.
It does not assert that arbitrarily many such contractions close in
a one-cell positive algebra, nor a broad sharp knot-volume estimate.
