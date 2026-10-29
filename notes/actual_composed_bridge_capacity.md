# A sharp capacity for two coherently composed original bridge packets

29 October 2026. The terminal packet with its adjacent inverse and the
open signed bridge can be estimated TOGETHER, with their common physical
color retained. Their exact operator norm has a strictly smaller exponent
than the product of their separate sharp norms. The resulting constant
is the unique maximum of an explicit strictly concave angle function.

This is a sharp all-input norm theorem for an actual four-crossing
terminal block, and gives a quantitative bound for the full original
source with arbitrary prefixes and arbitrary plat width. Its constant
is a block capacity, not asserted to be the volume of the closed knot.
The requested sharp knot-volume estimate remains open.

## 1. The actual coherent block and its exact row Gram

Use N>=2, d=N-1, q=exp(pi i/N), Q=q^2, x=q^d,
F_j=(Q;Q)_j, s_j=|F_j|. Let R be the FULL original checked crossing
on the pair degree-d multiplicity W_1. Put

    P_0=1, P_t=(1-Q^t)^2 P_(t-1)+Q^t,
    H=T R^(-1)=N^(-1) diag(x^n) R diag(P_(d-u)).          (1)

Here T is the complete original terminal packet, with all cap and
Cartan factors retained. The exact formula, endpoint cancellation,
and uniform bounds are proved in
[the original Green estimate](actual_terminal_green_capacity_bound.md):

    |P_t|<=N+4s_t^2,
    P_t=1/(2-Q^t)+O(1/N)
      uniformly when t/N is in a compact subset of (1/6,1/2). (2)

Let L:W_2->W_1 be the POSITIVE open bridge
(ell_12 tensor I_34)R_23, in the source-fixing physical coordinate
gauge g_j=s_j/sqrt(N). This gauge fixes every original paired cup
and ordinary cap. The whole marked closure is retained through the
complete invariant-source theorem. Its exact row Gram is

    LL^*=diag(E_N(u)),
    E_N(u)=N^2 sum_(k<=d-u) s_k^(-2)
                        sum_(a+c=d-k) s_a^(-4)s_c^(-4).    (3)

Thus the COMPLETE coherent block C=HL satisfies

    CC^*=H diag(E_N) H^*.                                (4)

No exterior coefficient or Green factor is commuted in (4). Both
sides can be tensored with an arbitrary Hilbert spectator space.
The actual source row is 1^T C. Its Cauchy cost is at most N,
also for the positive completion C^*C+exp(-N^2)I.

The [pointed row theorem](actual_terminal_bridge_operator_reduction.md)
gives, uniformly in u including the endpoints,

    log E_N(u)=(N/pi)h(u/N)+O(log N),
    h(t)=v_8,                                  0<=t<=1/2,
    h(t)=8 Lambda(pi*t/2)-2 Lambda(pi*t),        1/2<=t<=1, (5)

where Lambda(theta)=-integral_0^theta log(2sin s)ds and
v_8=8Lambda(pi/4). The transfer restriction k<=d-u is part of
(3); taking independent free maxima would lose it.

## 2. The sharp answer

On 0<=alpha,beta<=pi/2, with gamma=pi-alpha-beta, define

    F(alpha,beta)=4Lambda(alpha)+6Lambda(beta)+2Lambda(gamma)
                                      +8Lambda((pi-beta)/2). (6)

Let C_* be its maximum. It is attained at a UNIQUE point with

    0<alpha_*<pi/2, pi/6<beta_*<pi/2,
    sin(gamma_*)=2sin(alpha_*)^2,
    sin(gamma_*)cos(beta_*/2)^2=sin(beta_*)^3.              (7)

The sharp all-level operator estimate is

    log ||H L||_op^2=(N/pi) C_*+O(log N).                (8)

In particular

    v_8+3v_3<C_*<2v_8,
    C_*=6.930886593131580854...,
    alpha_*/pi=0.243487774973153603...,
    beta_*/pi =0.347871118966627868... .                  (9)

Here v_3=3Lambda(pi/3). The decimal values only describe the
analytically specified unique maximum; the proof does not infer
the rate or its strict gaps from numerical fitting.

## 3. The Green remainder has a strictly smaller exponent

The actual crossing support is i+u>=d. With h_0=i+u-d,

    |R_(i,u)|=s_i^2 s_u^2/(N^2 s_(h_0)).                 (10)

By (2), pointwise on this support,

    |H_(i,u)|<=|R_(i,u)|+4N|R_(i,u)|/s_u^2.             (11)

Multiply each column by sqrt(E_N(u)). The operator norm is bounded
by the Hilbert--Schmidt norm, and (11) bounds that norm by the sum
of the two Hilbert--Schmidt norms of the displayed nonnegative
entry majorants. This is used only AFTER the actual coherent P_t
endpoint cancellation which proves (2).

Write J(t)=integral_0^t log(2sin(pi*s))ds=-Lambda(pi*t)/pi.
For the second majorant the squared exponential profile is at most

    h(u/N)+pi[4J(i/N)-2J((i+u-d)/N)]<=v_8+3v_3.         (12)

Indeed max J=v_3/(2pi) and min J=-v_3/(2pi). Polynomial N
factors and the uniform factorial errors cost O(log N). This
argument includes all physical endpoints and every parity.

The first majorant has squared profile

    h(u/N)+pi[4J(i/N)+4J(u/N)-2J((i+u-d)/N)].            (13)

If u/N<=1/2 then J(u/N)<=0, so (12) bounds (13) too.
For u/N>=1/2 put alpha=pi(1-i/N), beta=pi(1-u/N).
Replacing the exact offset d=N-1 by N changes the action by
O(log N/N), uniformly, using the modulus
|Lambda(a)-Lambda(b)|<=C|a-b|(1+|log|a-b||).
This includes the thin support strip where the limiting gamma
would otherwise be between -pi/N and zero; adjust the angles
by O(1/N) into the closed simplex before applying the formula.

The limiting expression (13) is precisely (6), with beta<=pi/2.
An alpha>pi/2 cannot maximize it: then 0<gamma<pi/2 and swapping
alpha and gamma raises 4Lambda(alpha)+2Lambda(gamma) by
2[Lambda(gamma)-Lambda(alpha)]>0. Hence its maximum is C_*.

Finally C_*>v_8+3v_3. Evaluate (6) at alpha=pi/4,beta=pi/3.
Its excess over v_8+3v_3 is

    -4Lambda(pi/4)+5Lambda(pi/3)+2Lambda(5pi/12)>0.

Strict concavity of Lambda on (0,pi/2), with Lambda(pi/2)=0,
gives Lambda(5pi/12)>Lambda(pi/3)/2 and
Lambda(pi/3)>2Lambda(pi/4)/3. Combining them proves the displayed
strict inequality. Thus the remainder in (12) cannot control the
sharp exponential rate, and the upper half of (8) follows.

## 4. Strict concavity, the unique optimizer, and the lower bound

Inside the rectangle 0<alpha,beta<pi/2 put
a=cot(alpha)>0, b=cot(beta)>0, g=cot(gamma)=(1-ab)/(a+b).
The negative Hessian of (6) is

    [[4a+2g, 2g],
     [2g, 6b+2g+2tan(beta/2)]].                         (14)

Its first principal minor is positive. If g>=0 this is immediate;
if g<0, then g>-ab/(a+b)>-a, so 4a+2g>2a.
Before its last positive diagonal term, the determinant is

    24ab+8ag+12bg=8+16ab+4bg>0.

For g>=0 the first expression is positive. For g<0,
bg=(1-ab)b/(a+b)>=1-ab, so the second is at least12+12ab.
The extra term in (14) increases the determinant. Thus F is
STRICTLY concave throughout this convex rectangle.

The alpha derivative tends to +infinity at alpha=0, and at alpha=pi/2
it is 2log(cos(beta)/2)<0. The beta derivative at beta=pi/2 is
2log(cos(alpha)/2)<0. At beta=pi/6 it is

    2log(2sin(gamma))+4log(2cos(pi/12))>0,

since gamma ranges from pi/3 to5pi/6. Concavity then excludes every
beta<=pi/6 from the maximum. These statements give the unique
interior optimizer and the range in (7). Setting the two first
derivatives to zero gives exactly its trigonometric equations.

The upper gap C_*<2v_8 is also strict without decimals. The separate
crossing squared profile has maximum v_8 only at alpha=beta=pi/4.
The row profile h has maximum v_8 only for u/N<=1/2, i.e. beta>=pi/2.
They cannot attain both maxima together. Continuity on the compact
angle domain therefore gives a strict gap for their sum.

For the lower bound in (8), take integers i,u nearest
N(1-alpha_*/pi), N(1-beta_*/pi), with the exact support retained.
The Green index t=d-u satisfies t/N->beta_*/pi in (1/6,1/2),
so (2) gives a nonzero limiting P_t. Equations (5),(10) then imply

    log(|H_(i,u)|^2 E_N(u))=(N/pi)C_*+O(log N).

Equation (4) has norm at least this single squared entry of
H diag(sqrt E). Conversely its Hilbert--Schmidt bound costs at
most N^2 terms. This completes (8), including odd, even and
composite levels and all original normalization factors.

## 5. A full-source consequence at arbitrary plat width

For a six-head plat the actual terminal block has action order

    [2,-3,4,4].

First R23 couples the first ordinary cap to the remaining pair,
then the inverse R34 is retained, and finally R45^2 meets the
terminal cap. The exact cap identities give C=HL on W_2.
Thus for ANY preceding original braid B,

    |K_N|^2<=|chi_N|^2 N ||HL||^2 ||B w_0||_g^2.         (15)

The input metric g is the specified source-fixing physical factorial
metric. Its original paired source w0=p tensor p has polynomial norm.
The preceding operator is transported in that metric; its cost has
not been dropped from (15).

The same terminal block can be placed at the last five odd heads
of a 2k-head plat for ANY k>=3, with action order

    [2k-4,-(2k-3),2k-2,2k-2].

All earlier ordinary caps commute with this terminal block and can
be contracted exactly. Their product norm is polynomial. This leaves
the same complete W_2 input and the SAME HL estimate. The preceding
braid may use every head, including the last marked partner: its
complete invariant-tensor inverse is (x^d/N) times extraction of the
last two colors (0,d), not an unjustified odd-head cut replacement.
The gauges of those two colors multiply to one.

For reference each original physical signed crossing in the common
gauge g_j=s_j/sqrt(N) has Hilbert--Schmidt norm

    exp[Nv_8/(2pi)+O(log N)].                            (16)

Its nonzero modulus is s_(b+k)^2/(s_b^2 s_k) for the positive sign,
and s_(a+k)^2/(s_a^2 s_k) for the negative sign. With three
nonnegative complementary variables the limiting action is
2Lambda(alpha)+2Lambda(beta)+Lambda(gamma); its maximum is v_8/2,
at alpha=beta=pi/4,gamma=pi/2. The strict physical support admits
nearest lattice points, and its O(N^3) entries cost only log N.

Consequently an arbitrary fixed m-crossing prefix in this all-width
family satisfies the actual bound

    |K_N|<=|chi_N| N^C
              exp{N[m v_8+C_*]/(2pi)}.                 (17)

The exponent C depends only on the fixed word and width. This saves
more than two crossing capacities compared with separately charging
the FOUR terminal crossings; it also improves the two separate
packet capacities 2v_8. It is a bound for the whole original source,
with chi_N retained. It is not a claim that m v_8+C_* equals or is
at most the hyperbolic volume. Further coherent global constraints
and geometric survival remain to be proved.

[Audit](../experiments/audit_actual_composed_bridge_capacity.py)
checks the actual finite operator product, its exact row Gram,
the unique angle optimizer and growing-level capacity bounds.

Fresh audit: PASS four full original marked sources through ten heads,
seven complete finite compositions including both signed physical
crossing formulas, the optimizer equations, and five growing-level
norm sandwiches. An independent analytic review checked the strict
Hessian, boundary exclusion, remainder gap and lower bound. The
finite support strip is accounted for explicitly in Section 3.
