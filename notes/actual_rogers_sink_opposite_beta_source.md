# The original Rogers sink is an opposite-root beta source

28 October 2026. The remaining U/U/F sink has an exact finite
order-reversal identity with the already solved Newton sink at the
opposite root. Applying its ACTUAL relative source gives an explicit
two-full-Psi residue and a uniformly bounded retained current on a
nonempty geometric chamber. No new normalization, guessed contour,
or substitution of a positive invariant is required.

Together with the literal three-sink crossing partition, this supplies
local analytic source formulas for all nine original crossing atoms.
It does not prove that the simultaneous exterior knot cycle selects
their geometric product.

## 1. Original Rogers polynomial and field tags

Put Q=exp(2*pi*i/N), h=2*pi*i/N and d=N-1. The actual U/U/F
finite convolution is

    R_N(u,v)=sum_(i+j<N) (Q;Q)_(i+j)
                               u^i v^j/[(Q;Q)_i(Q;Q)_j]. (1)

Its q-Pascal recurrence gives the exact endpoint Ward equations

    (1-u)R_N(u,v)-v R_N(Qu,v)=D_R,
    (1-v)R_N(u,v)-u R_N(u,Qv)=D_R,
    D_R=1-u^N-v^N.                                     (2)

For example h_(a+1)(u,v)=u h_a(u,v)+v h_a(Qu,v), while
h_N=u^N+v^N at the primitive root. Summing a=0,...,d gives (2).
The nonzero inhomogeneous endpoint is part of the source.

For the complete reflected moment field

    F_R(L;U,V)=r^d Psi_-(Log U-L)
                         Psi_-(Log V-L)Psi_+(-L), r=exp L,

the EXACT original tags are

    N Q^d [r^0]F_R=R_N(Q^2 U,Q^2 V).                  (3)

Indeed the two minus coefficients are Q^i/(Q;Q)_i and
Q^j/(Q;Q)_j, while p_(d-i-j)=Q^(i+j+1)(Q;Q)_(i+j)/N.
No Q tag or N factor is dropped.

The exact field step and norm are

    F_R(L+h)/F_R(L)=Q^d (1-Q^(-1)/r)
                              /[(1-U/r)(1-V/r)],
    F_R(L+2*pi*i)/F_R(L)
                  =r^N(r^N-1)/[(r^N-U^N)(r^N-V^N)].    (3a)

Subtracting one in the latter has numerator
[(U^N+V^N-1)r^N-U^N V^N]. Its multiplier-one locus is
the Frobenius copy of the classical linear gluing equation
(U+V-1)r=UV. The retained source does not become a homogeneous
solution merely because that polynomial is displayed.

## 2. A finite source-preserving order reversal

Write B_(q,N)(a,b)=sum_(k=0)^d product_(j<k)(a-q^j b).
Then the WHOLE polynomial kernel satisfies

    R_N(u,v)=v^d B_(Q^(-1),N)(v^(-1),Q^(-1)u/v).      (4)

This is an identity of every boundary coefficient and can therefore
be paired with the SAME exterior functional and original cups/caps.
The apparent negative v powers cancel to the original polynomial;
they are not a new source support assumption.

Here is an all-N coefficient proof. Let q=Q^(-1). The right side is

    sum_(a=0)^d v^(d-a)(q u;q)_a.

The coefficient of u^i v^j has a=d-j and is

    (-1)^i q^(i(i+1)/2)
             (q;q)_(d-j)/[(q;q)_i(q;q)_(d-j-i)].

The numerator quotient equals (Q;Q)_(i+j)/(Q;Q)_j by the
root complement, and
(q;q)_i=(-1)^i Q^(-i(i+1)/2)(Q;Q)_i. The phases cancel
EXACTLY, leaving the coefficient in (1). This uses no asymptotics.

## 3. Carry the opposite-root contour and the full norm

Define the opposite-root current by the actual conjugate source

    I_-(a,b)=overline(I_+(overline(a),overline(b))),

with its conjugate logarithmic marks. The conjugate of the upward
Barnes contour is a DOWNWARD contour; this orientation is retained.
Equivalently it is minus the upward integral with denominator
exp(2*pi*i*z)-1 and the opposite full-Psi function. Its chamber is
a upper and b/a lower. Its uniform compact bound is the conjugate
of the proved original Newton bound.

Apply the EXACT opposite Newton decomposition to (4), using

    a=v^(-1), b=Q^(-1)u/v,
    Log a=-Log v, Log(b/a)=Log u-h.

The complete norm transforms by

    v^d(1-a^N+b^N)=-v^(-1)(1-u^N-v^N).

The original Rogers source is consequently

    R_N=T_N+D_R J_N,
    J_N(u,v)=-v^(-1) I_-(v^(-1),Q^(-1)u/v),
    T_N(u,v)=phi_N exp[-Log u Log v/h]
                    Psi_-(Log u-h)Psi_-(Log v-h).      (5)

All constants are exact: N/phi_-=phi_+ because |phi_N|^2=N,
and v^d a^N times the shifted Gaussian contributes v^(-1)*v=1.
Thus (5) is an actual relative-cycle pushforward, not a normal
determinant calculation. The opposite circle/ray source, its
endpoints and deck choices are transported by (4) and conjugation.

For u,v both strictly lower, the transformed opposite chamber is
valid uniformly on compact subsets for all sufficiently large N.
It follows immediately that

    |J_N(u,v)|<=C_K.                                  (6)

Its principal normalization symbol is also explicit:

    J_N=1/(1-u-v)+h*u*v/(1-u-v)^3+O_K(h^2).             (6a)

This follows by substituting the exact Q^(-1) tag into the proved
opposite Newton symbol, or by expanding (2). Its all-order rational
recursion has poles only on the bubble locus u+v=1. Exact current
continuation and exponentially small sectors are still retained.

At smaller N, or after continuation outside that chamber, (5) keeps
its transported logarithmic marks and currents; no bare replacement
by a principal contour is assumed.

There is a useful full-positive-function version that displays the
norm factors. The exact identity

    Psi_-(z-h)=(1-exp(Nz))/Psi_+(z)

gives

    T_N=phi_N (1-u^N)(1-v^N) exp[-Log u Log v/h]
                              /[Psi_+(Log u)Psi_+(Log v)]. (7)

The factor is (1-u^N)(1-v^N), NOT (uv)^N. On the balanced
Fermat locus u^N+v^N=1 these agree, but off that locus their
difference is D_R. Replacing one by the other changes the retained
current by an explicit full-Psi term. Such a change cannot be
declared tame or ignored at an ideal specialization.

## 4. Balanced Fourier check and both homogeneous Ward equations

On u^N+v^N=1, the source recurrence is homogeneous. The finite
u-orbit has

    R_N(Q^k u,v)=R_N(u,v) (u;Q)_k/v^k.

Summing the orbit and taking the zero Fourier coefficient of the
polynomial gives

    R_N(u,v) B_(Q,N)(v^(-1),u/v)=N u^N/(1-v).         (8)

The balanced Newton sum is nonzero. Using its independently proved
normalizer, (8) yields exactly (7) with its balanced factor (uv)^N.
This is an independent finite-source normalization check.

Off balance, (5) supplies the actual full norm extension. Its
geometric block obeys BOTH exact homogeneous equations

    (1-u)T_N(u,v)=v T_N(Qu,v),
    (1-v)T_N(u,v)=u T_N(u,Qv),                         (9)

and J_N obeys (2) with right side one. The all-level source choice
is therefore fixed by order reversal, not just by data on D_R=0.

## 5. An actual growing local source on a full open chamber

For u,v strictly lower, write l=Log u,m=Log v on (-pi,0).
The actual negative-strip full-Psi symbol and exact shift yield

    T_N=phi_N/ sqrt[(1-u)(1-v)]
        exp[W_R(u,v)/h](1+O_K(1/N)),
    W_R=-Li_2(u)-Li_2(v)-l*m.                         (10)

Every density is explicit and nonzero, with all fixed derivative
bounds uniform on compact lower-half-plane families. Put

    Lambda_R=Im W_R/(2*pi),
    delta_R=max(0,log|u|,log|v|).

If Lambda_R>=delta_R+eta on a compact family, (5)--(6) prove

    R_N(u,v)=T_N(u,v)[1+O_K(N^(-1/2)exp(-N eta))].    (11)

The ORIGINAL residue has coefficient one; its entire retained
normalization current is exponentially smaller. This is a genuine
source theorem on a nonempty open family, not a knot-family claim.

For |u|=|v|=1, with both lower, delta_R=0 and

    Lambda_R=[-Im Li_2(u)-Im Li_2(v)]/(2*pi)>0.

The cross term l*m is real. A compact pair of lower unit arcs has
a uniform positive gap, which persists in a full open neighborhood.
In particular, uniformly for theta,eta on compact subsets of (0,pi),

    lim_(N->infinity) (2*pi/N)
                log|R_N(exp(-i*theta),exp(-i*eta))|
                             =D(exp(i*theta))+D(exp(i*eta)). (12)

The identical limit holds with the ACTUAL Q^2,Q^2 tags in (3).
These are original local polynomial volume identities. They are not
asserted to be Kashaev invariants of a new family of knots.

There is a genuinely positive three-side bipyramid subfamily too.
At u=exp(-i theta),v=exp(-i eta), its three-side shapes are

    A=(u+v-1)/v, B=(u+v-1)/u,
    C=(u+v-1)/(uv).

C is upper for all theta,eta in (0,pi). Both A and B are lower
when eta<pi/2+theta/2 and theta<pi/2+eta/2. These strict inequalities
hold in particular near every equal-angle pair. Thus the three
signed shapes -[A]-[B]+[C] and the two negative output shapes
-[u]-[v] are strictly positive and nondegenerate there. The five-term
relation identifies their equal positive volume. This verifies a
nonempty open geometric family without asserting that every possible
unit-angle pair is a positive 2-to-3 move in this ordering.

## 6. What is now available globally

The literal crossing assembly has three disjoint finite sinks. For a
positive crossing, exact Gaussian absorption leaves two Newton kernels
and one Rogers kernel. For a negative crossing there are again two
Newton kernels and one Rogers kernel, with its original Gaussian
retained. Equations (4)--(11) thus fill the missing analytic local
entry in that assembly, including its source and norm factors.

This does not permit independent sector integrations on arbitrary
new circles. The simultaneous original boundary pairing, logarithmic
seams, caps and residual Gaussian remain compulsory. The full exterior
cycle and its geometric noncancellation are the next global issue.

## 7. Sew the actual opposite face BEFORE taking an asymptotic symbol

In the literal positive crossing, the final Newton and Rogers kernels
share the EXACT variable w=v_B/u_B=v_R. Write their paired polynomial
kernel as

    F(a,c,w)=B_N(a,a w) R_N(c,w),
    alpha=Log a, chi=Log c, sigma=Log w,
    A=a^N, C=c^N, W=w^N,
    D_B=1-A+AW, D_R=1-C-W.                            (13)

The Newton positive growth chamber asks w upper while the Rogers
negative growth chamber asks w lower. There is NO simultaneous
principal positive chamber for the two unsewn face factors. The
literal product must first use the exact shifted identity

    Psi_+(sigma)Psi_-(sigma-h)=1-W.

Consequently its full residue product is exactly

    P(a,c,w)=(1-W) G(a,c,w),
    G=N a^N exp[-sigma(alpha+chi)/h]
                       Psi_+(h-alpha)Psi_-(chi-h).      (14)

The ordinary factor 1-w is absent: the EXACT h shift removes it.
The central factor 1-W is retained. All remaining original currents
are the explicit aggregate

    F=P+D_B I_B(a,a w) T_R(c,w)
          +D_R J_R(c,w) S_B(a,a w)
          +D_B D_R I_B(a,a w)J_R(c,w).                 (15)

This is an identity of actual marked functions; their relative
cycles and overlaps are inherited from the original finite pair.
It does not assign independent principal contours to the three
terms in the incompatible half-plane chambers.

The paired endpoint Ward identity is also explicit and polynomial:

    F(a,c,w)-a c F(a,c,Qw)
       =D_B R_N(c,w)+a D_R B_N(a,Qa w).                (16)

It follows by multiplying the two exact finite Ward equations.
No artificial denominator 1-w is introduced. The source norms obey

    D_B+A D_R=1-AC.                                  (17)

Thus the two simultaneous balanced constraints force the single
external central relation AC=1. Their coupling must not be replaced
by two independent local angle-domain choices.

The remaining field G has no dilogarithm in sigma; its sigma phase
is the explicit linear Fourier coupling -sigma(alpha+chi). Its
regular remaining shape functions can both be on selected strips
when a and c are lower, irrespective of the removed face's sign.
The OTHER factors of the complete crossing still depend on this
same internal variable, so this observation alone does not evaluate
its full Fourier integral or select its exterior cycle.

One full sigma deck gives

    P -> P/(AC),
    (F-P) -> (F-P)+(1-(AC)^(-1))P.                    (18)

The original pair F remains fixed. This is the inherited shared-face
source extension, with the exact norm currents. It shows both the
benefit of sewing the opposite face first and why its currents cannot
then be deleted independently.

### 7.1. The exact locus for an aggregate geometric quotient

The sewn pair permits a precise algebraic statement stronger than
deleting its individual current sectors. Keep a,c,w nonzero and the
same marked function P in (14). Its three full logarithmic turns have
characters

    mu_a=(A-1)/(AW),
    mu_c=(1-C)/W,
    mu_w=1/(AC).                                      (18a)

For example an alpha turn contributes W^(-1) from its Fourier
exponential and 1-A^(-1) from Psi_+(h-alpha); a chi turn contributes
W^(-1)(1-C). Equation (18) gives the sigma turn. All factors and
logarithmic marks are exact, including the h shifts.

On this regular central torus, the CHARACTER-ONE IDEAL is exactly
the joint balanced ideal, since

    1-mu_a=D_B/(AW),
    1-mu_c=-D_R/W,
    1-mu_w=-(D_B+A D_R)/(AC).                         (18b)

Thus (1-mu_a,1-mu_c,1-mu_w)=(D_B,D_R) after the indicated unit
localization. The weaker shared-face condition AC=1 alone does not
make the other two characters one.

Let H=F-P be the AGGREGATE current. Under each turn it changes by
(1-mu)P. A deck-compatible pointwise quotient killing H therefore
has geometric image supported on this joint balanced locus (or on
its retained normal/derived thickening). Conversely on its regular
matched base change D_B=D_R=0, the exact finite source identities
give

    F=P!=0.                                          (18c)

Indeed the Newton and Rogers balanced polynomials are each nonzero
by their finite Fourier proofs. Their exact marked residues equal
those polynomials there, so (18c) is a nonzero local source-preserving
restriction, not a section defined from an unknown knot value.
One is killing the COMBINED current on a specified algebraic base;
one is not declaring its separate summands zero off that base.

This identifies a possible local geometric quotient and the exact
support it requires. It does NOT prove that the remaining original
head/cap co-source factors through this base change, nor replace its
finite degree relations by scalar norm equations. Normal source jets,
the other head factors and the actual exterior integration still
have to be transported. Character-one and nonzero local pointing do
not by themselves determine a nonzero global period coefficient.

The [audit](../experiments/audit_actual_rogers_sink_opposite_beta_source.py)
and [results](../experiments/actual_rogers_sink_opposite_beta_source_results.json)
check original finite reversal and actual tags, the two conjugate
Barnes source identities, balanced Fourier normalization and the
paired polynomial Ward relation. The proofs do not infer their
all-level statements from finite checks.

## 8. The ACTUAL shared-head source combines the currents into a ground channel

There is a stronger physical identity once the first, still unsplit
Newton factor is included. In the literal positive crossing put

    E=x^(-1)z_6/z_1, s=x^(-1)z_1/z_0,
    a=x^(-1)z_7/z_6, c=z_6/z_0,
    B_0(w)=B_N(E/w,sE/w),
    K_m=Pi_+^(6) CT_w B_N(Q^m E/w,Q^m sE/w)F(a,c,w).

The common original scalar kappa remains external. These are literal
operators on the original finite input space; Pi_+^(6) is the original
nonnegative first-output barrier. K_0 is the original positive crossing
without kappa. K_m inserts the ACTUAL internal Cartan clock Q^(mJ)
on the t=z_4 head just after C^(-1), before its remaining gates.

The first factor has w degree between -d and zero. Therefore pairing
the polynomial Ward equation (16) with it kills every w^N times a
nonnegative polynomial. The exact source equation before the physical
barriers is

    CT B_0[F-acF(Qw)]
        =(1-a^N) CT B_0 R+corr,
    corr=a(1-c^N) CT B_0 B_N(a,Qaw).                  (19)

No D_B or D_R has been set to zero. Their w^N parts have vanished by
the FINITE DEGREE of the actual third sink, rather than a branchwise
replacement of the source. Rotating w in the second left term gives
the next clock insertion K_(m+1).

The remaining physical barriers have precise effects:

* H_m=CT B_N(Q^m E/w,Q^m sE/w)R_N(c,w) has first-output
  degree at most d, so a^N H_m has negative first-output degree and
  is killed by Pi_+^(6).
* Every term of a CT B_0 B_N(a,Qaw) has first-output degree -i-1<0,
  so this entire term is killed by the SAME barrier.
* Multiplication of that last expression by c^N can remove the negative
  output degree, but then it requires first INPUT index at least N.
  The original finite input space kills it.

These claims hold with every clock m: the clock changes coefficients,
not the indicated index supports. Thus on the ORIGINAL finite heads,

    K_m-(ac)K_(m+1)=H_m.                              (20)

The boundary source is explicit. For input indices alpha,beta and
alpha+beta<N,

    H_m |alpha,beta>
      =Q^(m beta)x^(-beta) {alpha+beta choose alpha}_Q
            (Q^m x^(-2);Q)_alpha |alpha+beta,0>,       (21)

and it is zero if alpha+beta>=N. To derive (21), expand the Euler
factor (s;Q)_j in the first Newton kernel. If its Euler order is k,
the surviving indices are j=beta+k and i=alpha-k. The q-binomial
sum is exactly (Q^m x^(-2);Q)_alpha. This proves all normalizations
with the actual color x retained.

H_0 has rank N: the inputs (0,beta) span every output (beta,0).
It is a ground-SECOND-output channel, not a rank-one operator and
not a negligible error. At complete color x^(-2)=Q its coefficient
is x^(-beta)(Q;Q)_(alpha+beta)/(Q;Q)_beta; it is nonzero on every
supported input and can have bulk factorial growth.

This growth is quantitative in the complete flat balanced metric.
Rows have disjoint input total degrees, so the exact operator norm is

    ||H_0||^2=max_(0<=t<N) |F_t|^2
                                    sum_(b=0)^t |F_b|^(-2).

With J(s)=integral_0^s log(2 sin(pi y))dy, the uniform factorial
estimate log|F_k|=N J(k/N)+O(log N) gives

    log||H_0||=N integral_(1/6)^(5/6)
                              log(2 sin(pi y))dy+O(log N).

Indeed the largest profile rise is J(5/6)-J(1/6). Thus the physical
ground-output source is not an exponentially small boundary error.
Its exact endpoint support does not justify discarding its period
after composition with the remaining word.

The fusion operation itself is associative multiplication with explicit
weights. On e_a=t^a/F_a in C[t]/(t^N), ordinary multiplication has
m(e_a tensor e_b)={a+b choose a}_Q e_(a+b), with zero output when
a+b>=N. Consequently H_m is this multiplication after diagonal
weights (Q^m x^(-2);Q)_J on the first input and (Q^m/x)^J on the
second, followed by the ground-second-head inclusion. The exact
identity (z;Q)_(a+b)=(z;Q)_a(Q^a z;Q)_b describes the weight
transport under further fusion. This structural description preserves
all original factorial frames; it is not a new positive state model.

Equation (20) has an exact nilpotent Green solution. Multiplication
by ac=x^(-1)z_7/z_0 raises the second output index and increases the
first input demand by one. Hence (ac)^N times any K_m is zero on
the original finite input space. Iterating gives

    K_0=sum_(j=0)^d (ac)^j H_j.                       (22)

This reconstructs the ACTUAL crossing, including the combined current
endpoints, from explicit fusion-to-ground channels. For example its
only possible output from input (alpha,beta) has the form
(alpha+beta-j,j), with j<=alpha and alpha+beta-j<N, and coefficient

    x^(-beta-j)Q^(j beta)
       {alpha+beta-j choose alpha-j}_Q
                       (Q^j x^(-2);Q)_(alpha-j).      (23)

All identities are literal finite operators and may be inserted in
ANY original signed word with the same caps and pivotal source.
They do not assert that every H_m insertion has a degenerate global
representation, or that the remaining bulk sums have no cancellation.
What has been proved is an actual sourced boundary/Green identity,
without discarding the norm currents or changing the invariant.

The independent
[finite-head audit](../experiments/audit_actual_crossing_green_ground_fusion.py)
compares (20)--(23) with the original gate word, including whole
signed words and their original pivotal source.
