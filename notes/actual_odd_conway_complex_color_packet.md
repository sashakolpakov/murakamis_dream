# The exact complex color packet for arbitrary signed Conway coupons

29 October 2026. For every retained C(FG), with F and G robust, and
every fixed choice of pure or signed odd-half-twist coupons, the
original mixed-color source has the finite analytic packet required
by the general filling theorem. Its uniform complex asymptotic has
power N^(3/2), a nonzero marked amplitude, and both level parities.
The changed odd action is explicitly identified with a local shear
of the pure action; it is not replaced by the pure colored action.

The representation and primitive peripheral interpretation of that
shear are a separate geometric statement. This note proves the exact
source packet, its phase, Hessian, and whole-source error estimates.

## 1. An exact finite definition in original Newton coordinates

Fix the actual expression and epsilon_l in {0,+1,-1} at each of its
H individual circle leaves. The physical coupon is
T(R^epsilon_l L_(N-h_l)), with t_l=h_l/N. Put D=N-1,
M=floor(D/2), q=exp(pi i/N), kappa=q^(D^2/2), with the original
half-Cartan mark. Let G_N be the canonical sine-factorial completion,
G_N(r)=s_r, and put

    A_N(v,t)=N^2 s_(2v)/
                [s_v^2 G_N(v-Nt)G_N(v+Nt)], 0<=v<=M.       (1)

For a retained high Newton index r define the EXACT finite functions

    d_N^0(r,t)=A_N(r,t),
    d_N^epsilon(r,t)=kappa^epsilon
       sum_(v=r)^M (-1)^v q^[epsilon v(r+1)]
                        [v choose r]_q A_N(v,t), epsilon=+-1.
                                                                 (2)

Here [v choose r]_q=s_v/(s_r s_(v-r)). These are the coefficients
of the literal transported core, by the
[full Newton half-twist identity](actual_odd_conway_newton_transport.md).
For physical integers h<r, (2) is EXACTLY that coefficient in the
full repeated-root algebra, including its normal directions. For
complex t near zero it is its specified factorial continuation.
All functions in (1)--(2) are holomorphic and even in t.

Remove only the explicit common unit phase:

    ell_N^epsilon(r,t)=exp(-i epsilon pi D/4)d_N^epsilon(r,t),
    eta_N=exp[(i pi D/4)sum_l epsilon_l].                       (3)

The positive coupon is the Schwarz reflection of the negative one,
including its original q and kappa phases. For complex parameters
this means ell_N^+(r,t)=overline(ell_N^-(r,overline(t))); it does
not mean conjugating a variable inside a holomorphic function.

The [strict leaf interval](actual_conway_strict_leaf_quarter_bound.md)
places all complete leaf coordinates strictly above 1/4. Choose a
small fixed rectangular window B about the unique complete optimizer
in the d=2H-3 free integer wire coordinates of the
[pure finite-window construction](actual_conway_complex_window_laplace.md).
All leaf indices in this window lie in one compact subinterval of
(1/4,1/2); all retained product inequalities are strict.

The last forced-flat product has exact coefficient one and is removed
using its actual input relation i+j=D. Every other wire index has
the exact form r_w=N L_w(y)+delta_w, with fixed integer offsets
delta_w. The remaining lattice is primitive Z^d. Define

    C_N^epsilon(t)=sum_(k in Z^d, k/N in B)
       product_leaves ell_N^(epsilon_l)(r_l,t_l)
       product_retained_gates mu_N(r_left,r_right,r_out).       (4)

The mu_N are the original positive Newton multiplication coefficients,
not their asymptotic equivalents. Thus (4) is a finite, explicit,
separately-even holomorphic function. For all sufficiently large N,
each state in its fixed window is an actual admissible core state
for every physical small deficit. No support cutoff moves with t.

## 2. The selected local action and amplitude

Use t=h/N throughout; the older mixed-source note uses pi t for its
second variable. Put Y=exp(2pi i x), H_t=exp(2pi i t) and
D_t=(1-Y/H_t)(1-Y H_t). The source-selected quadratic is

    mu^2-p_0 mu-q_0=0,
    p_0=-Y^-1[(H_t+H_t^-1)Y^2+2]/D_t,
    q_0=-Y^-2(1-Y^2)^2/D_t^2,
    mu(x,0)=-Y^-1.                                           (5)

On a fixed complex neighborhood of the high x interval and a small
fixed t disk this root is nonzero, analytic and dominant in the
actual high-to-low source transport. Define

    S(x,t)=integral_x^(1/2) Log mu(u,t)du,
    C(x,t)=sqrt(mu(x,t)) exp[integral_x^(1/2) nu(u,t)/mu(u,t)du].
                                                                 (6)

The logarithm and square root equal zero and one respectively at
x=1/2. The correction nu is computed from the exact source recurrence:

    nu=[p_1+q_1/mu-q_0 mu_x/mu^2]/[1+q_0/mu^2].             (7)

Here p_1,q_1 are the 1/N derivatives of the EXPLICIT rational
recurrence coefficients in the
[selected mixed-inner theorem](actual_pretzel_mixed_inner_source_wkb.md),
with its color variable replaced by pi t. Its terminal source is
U_M=1; C is therefore normalized by that finite source. In particular

    S(x,0)=i pi(1/2-x)^2,
    C(x,0)=sqrt(sin(pi x))exp[-3pi i(1/2-x)/2].               (8)

Let

    g(x,t)=J(2x)-2J(x)-J(x-t)-J(x+t),
    f_0(x,t)=g(x,t),
    f_-(x,t)=g(x,t)+S(x,t)-S(x,0),
    f_+(x,t)=overline(f_-(overline(x),overline(t))).          (9)

The three functions all equal g(x,0) at t=0, but their color
derivatives differ. Their local leading amplitudes are

    b_0(x,t)=sqrt(sin(2pi x))/
        [2^(3/2)sin(pi x)sqrt(sin(pi(x-t))sin(pi(x+t)))],
    b_-(x,t)=b_0(x,t) exp[i pi(3/4-x)] C(x,t),
    b_+(x,t)=overline(b_-(overline(x),overline(t))).          (10)

All marks continue from the positive complete factorial branches.
They are nonzero after shrinking the fixed domains. At completeness,

    b_epsilon(x,0)/b_0(x,0)
       =sqrt(sin(pi x))exp(-i epsilon pi x/2), epsilon=+-1.
                                                                 (11)

These formulas include the source's quadratic color phase. Indeed
the literal finite sum is A_(h,r)=D_(h,r)U_(h,r), and the canonical
factorial marks give exactly

    q^(h^2)D_(h,r)/D_(0,r)
                  =G_N(r)^2/[G_N(r-h)G_N(r+h)].              (12)

The apparent q^(h^2) has thus combined with the factorial phases;
it has not been discarded as an external unit factor.

## 3. Exponentially accurate joint interpolation of the finite grid

This step is necessary before using a complex wire saddle. A merely
O(1/N) coefficient approximation on the real grid would not suffice.
The selected mixed-source theorem supplies a holomorphic E_N(x,t),
on a fixed joint neighborhood, satisfying

    U_(Nt,r)=exp(E_N(r/N,t))[1+O(exp(-sigma N))],
    exp(E_N(x,t))=C(x,t)exp[N S(x,t)][1+O(N^-1)].            (13)

Both estimates are uniform in the specified complex t disk. The
first compares the ACTUAL finite source with its interpolation on
the physical high-index grid. Its proof uses the exact endpoint
zero in the continued fraction followed by optimally truncated
analytic Euler--Maclaurin; no homogeneous solution is substituted.

The remaining chirp must use a fixed analytic lattice mark. Take

    nu_N(z)=exp[-i pi z+i pi z(z+1)/N],
    P_N(x)=kappa^-1 exp(i pi D/4)/nu_N(Nx).

At integer r, nu_N(r)=(-1)^r q^(r(r+1)) exactly. Moreover

    P_N(x)exp[N S(x,0)]
                       =exp[i pi(3/4-x-1/(2N))].            (14)

This fixes the continuous chirp before the lattice contour estimate.
Replacing exp(-i pi r) by an arbitrary off-grid branch would move
a whole lattice frequency and is not done here.

For complex x define the exact pure interpolation

    A_N^hol(x,t)=N^2 G_N(2Nx)/
               [G_N(Nx)^2G_N(N(x-t))G_N(N(x+t))].            (15)

A joint analytic interpolant of the NEGATIVE normalized coefficient is

    I_N^-(x,t)=A_N^hol(x,t) P_N(x)exp(E_N(x,t)).             (16)

At the physical high grid it agrees with ell_N^- up to the relative
exponential error in (13). Formula (12) proves that this is the same
finite coefficient (2), including its phase. For the positive sign
use its Schwarz reflection, and for the pure coupon use (15) itself.
Equations (8),(13)--(16) and the canonical factorial expansion give

    I_N^epsilon(x,t)=N^(1/2)b_epsilon(x,t)
                      exp[N f_epsilon(x,t)][1+O(N^-1)]       (17)

uniformly holomorphically on a smaller fixed joint neighborhood.
The factor exp(-i pi/(2N)) in (14) belongs to the displayed error,
not to an omitted constant or parity phase.

## 4. Exact identification of the changed action as a shear

There is a useful equivalent expression for (9). For each
epsilon in {0,+1,-1}, solve near s=0 the implicit equation

    t=s-epsilon g_s(x,s)/(2pi i).                           (18)

Its derivative in s at completeness is 1-epsilon i cot(pi x),
which is nonzero. Then EXACTLY

    f_epsilon(x,t)=g(x,s)-epsilon g_s(x,s)^2/(4pi i),
    partial_x f_epsilon=g_x(x,s),
    partial_t f_epsilon=g_s(x,s).                          (19)

The last two identities follow by differentiating (18); what needs
proof is that (19) is the action selected by the original source.
For epsilon=-1 put E=exp(2pi i x), H=exp(2pi i t), T=exp(2pi i s).
Exponentiating (18) gives

    H=T(E-T)/(ET-1),
    T^2+E(H-1)T-H=0, T=1 at H=1.                           (20)

The pure ordered-port quantity K=exp(-g_x(x,s)) is
-(1-E/T)(1-ET)/(1+E)^2. Eliminating T from (20) gives

    K^2(1+E)^2+K[(H+H^-1)E^2+2]+(1-E)^2=0.                (21)

On the other hand, differentiating the ACTUAL selected action (9)
in x and using (5) gives

    exp(-partial_x f_-)=E mu D_t/(1+E)^2,

which obeys precisely (21). At H=1 the polynomial factors as
(K+1)[K(1+E)^2+(1-E)^2], and both constructions take the branch
K=tan(pi x)^2. Their x derivatives therefore agree, with the
logarithms fixed at t=0. Their difference could only depend on t.
Both actions tend to zero as x tends to 1/2: S(1/2,t)=0 and
J(1/2+t)=-J(1/2-t); the implicit shear has s=t and g_s=0 there.
This fixes that remaining function to zero. Schwarz reflection
proves the positive case, and epsilon=0 is immediate.

Thus the half-twist source really implements this action change;
matching its Hessian alone was not used to identify it.

## 5. The finite packet's uniform complex saddle

Let y be the primitive free wire coordinates. With all exact turn
relations retained in their affine limiting maps, put

    F_epsilon(y,t)=sum_l f_(epsilon_l)(x_l(y),t_l)
                                  +sum_retained_gates m(w_g(y)).

At t=0 it is the pure complete action. Its wire Hessian is negative
definite, so it has one holomorphic critical branch y_*(t) near the
strict complete optimizer. Set

    Phi_epsilon(t)=F_epsilon(y_*(t),t).                      (22)

To specify the amplitude without losing integer offsets, write
r_w=N L_w(y)+delta_w. Use the leaf amplitudes (10), the usual positive
gate amplitude

    b_mu(x,y,z)=2^(-3/2)
       sqrt[sin(pi(x+y))sin(pi z)/
          (sin(pi x)sin(pi y)sin(pi(z-x))sin(pi(z-y))
                                           sin(pi(x+y-z)))],

and multiply their product by the EXACT leading offset factor

    exp[sum_l delta_l partial_x f_(epsilon_l)
                              +sum_g grad m(w_g) dot delta_(w_g)].
                                                                 (23)

Call the resulting holomorphic nonzero function b_E(y,t). In (23)
the changed f_epsilon is essential at nonzero colors; one must not
reuse a pure colored offset factor. Define

    a_epsilon(t)=(2pi)^(d/2)b_E(y_*(t),t)/
                             sqrt(det[-F_(epsilon,yy)(y_*(t),t)]).
                                                                 (24)

The determinant square root is positive at completeness. All factors
are fixed by the original grid and its canonical factorial marks.
Then, uniformly on a fixed smaller complex color polydisk,

    C_N^epsilon(t)=N^(3/2)a_epsilon(t)
                      exp[N Phi_epsilon(t)][1+O(N^-1)].      (25)

Proof with the finite errors retained. Replace the grid leaf factors
in (4) by (16), (15), or their reflected versions, and use the
canonical interpolation for each unchanged gate. The total grid
error is bounded by

    poly(N)exp[N(F0+C||t||^2-sigma)],

because (13) is relative at each original state and all local actions
are even perturbations of the complete real action. Shrink the fixed
color disk until this is exponentially below Re Phi_epsilon(t).
This estimates the error BEFORE any oscillatory saddle cancellation.

The interpolated summand has amplitude N^(3-H)b_E and phase
F_epsilon, uniformly holomorphically on the same fixed wire tube.
Apply the finite tensor-cotangent rectangle proof from the pure
window theorem: vertical half-grid sides retain a boundary gap;
each nonconstant horizontal kernel term loses exp(-2pi N eta),
dominating the O(eta^2) complete phase increase and sufficiently
small complex-color perturbation. The constant horizontal terms
give N^d times the ordinary integral, including all orientations.
Replacing half-grid endpoints by the fixed rectangle costs only
exponentially small boundary strips.

Translate that integral to its nearby complex critical point. The
endpoint connectors retain their gap, its real tangent Gaussian is
uniformly nondegenerate, and the odd first corrections integrate to
zero. This gives relative O(N^-1), with power
N^(3-H+d/2)=N^(3/2). Adding back the already bounded exponential
grid residual proves (25) for the EXACT finite function (4).
Neither parity changes the lattice density or any displayed phase.

## 6. Nonzero amplitude, color Hessian and the whole physical source

The functions Phi_epsilon and a_epsilon are separately even. At zero,

    Phi_epsilon(0)=F0,
    a_epsilon(0)=a_pure(0)
        product_(epsilon_l!=0)
          sqrt(sin(pi x_(l,*)))exp(-i epsilon_l pi x_(l,*)/2),
                                                                 (26)

which is nonzero. Since F_(y t_l)(y,0)=0 identically by evenness,
the critical-point Schur correction vanishes. With c_l=cot(pi x_(l,*)),

    partial_(t_l)partial_(t_m) Phi_epsilon(0)
        =[-2pi c_l/(1-epsilon_l i c_l)] delta_lm
        =2pi i tau_l delta_lm,
    tau_l=i c_l/(1-epsilon_l i c_l), Im tau_l>0.              (27)

For epsilon=-1 this is tau=(1+exp(2pi i x))/2; for epsilon=+1
it is -(1+exp(-2pi i x))/2. The pure value is i cot(pi x).
These are the packet parameters; the corresponding geometric cusp
ratios are twice these numbers in the original full-twist convention.
At the level of the exact local action (19), if U_old=-2pi i s and
V=-2g_s, then U_new=-2pi i t=U_old-epsilon V/2. Identifying these
as the primitive paths on a changed half-twist partner requires its
literal geometric cut, not just this generating-function equation.

The negative-definite real part of the diagonal Hessian and separate evenness give, after
shrinking the fixed complex polydisk,

    |C_N^epsilon(u+iv)|<=poly(N)
       exp[N(F0-a||u||^2+B||v||^2)], a>0.                    (28)

The bound concerns the finite packet itself by (25); imaginary
quadratic cross terms are absorbed by completing squares.

Finally the [whole mixed-source gap](actual_odd_conway_uniform_mixed_source_gap.md)
controls all actual aliases. On real physical colors, the omitted
core states outside B have a fixed gap from the common concave
majorant and its unique complete maximizer. Therefore, uniformly
for 0<=h_l<=delta N,

    |Z_N(h)-eta_N C_N^epsilon(h/N)|
                           <=poly(N)exp[N(F0-gamma)],         (29)

for some fixed delta,gamma>0. The full physical color complement
has its separately proved gap as well. Thus (25),(27)--(29) supply
ALL quantum source hypotheses of the general long-filling transfer
for the changed coupons, with mu=3/2 and eta_N exactly as in (3).
The actual peripheral geometry remains its distinct hypothesis.

## 7. The same action transformation holds on the entire source branch

Let Phi_0(s) be the optimized PURE colored action, with all its
actual wire equations retained. Since f_(epsilon,x)=g_x in (19),
the changed critical wire state is precisely the pure critical wire
state at the corresponding local s parameters. The global action
identity is consequently

    t_i=s_i-epsilon_i partial_i Phi_0(s)/(2pi i),
    Phi_epsilon(t)=Phi_0(s)
                  -sum_i epsilon_i [partial_i Phi_0(s)]^2/(4pi i).
                                                                 (30)

The first map has invertible diagonal derivative
1-epsilon_i i cot(pi x_(i,*)) at zero. It therefore fixes a unique
small analytic branch. Differentiation gives
partial_(t_i)Phi_epsilon=partial_(s_i)Phi_0 exactly; mixed source
couplings are retained in this global map.

At a full-twist filling saddle with charges +1, this implies the
action identity

    S_epsilon,p = S_0,p_eff, p_eff,i=p_i-epsilon_i/2,            (31)

at their corresponding critical points. This is an equality of
selected analytic ACTIONS, not a replacement of the actual filled
manifold by a pure rational-slope filling. Multiplying the pure
half-integral slope equation by two would also double its rotation
charge, so primitive geometric completion does not follow that way.
The original changed meridian and its physical filling equation must
still be used.

Audit: [finite coefficients, action shear and color normalization](../experiments/audit_actual_odd_conway_complex_color_packet.py).
The [recorded results](../experiments/actual_odd_conway_complex_color_packet_results.json)
pass 18 exact finite transported-source comparisons, 12 continuous
chirp/parity checks, the symbolic selected-port, implicit-derivative,
Hessian and effective-slope identities, and eight complex amplitude
calibrations across both parities. These computations check finite
normalizations; the uniform estimates and their error bounds are
proved above.

The quadratic color phase q^(h^2) cancels the shifted factorial phases. Integer offsets and the N^(3/2) power remain in the finite packet. The interpolation residual is converted to an absolute bound before the complex saddle is evaluated.
