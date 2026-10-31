# A fixed complex external-color packet for the original complete core

30 October 2026. This note assembles the
exponentially accurate local interpolation into the actual shared-face
period. The theorem applies to each fixed certified augmented plat at
arbitrary fixed bridge width. Its object is the exact complete-image term
in color reflection. The other reflected terms remain part of the
long-filling problem.

Subsequent geometric identification: the
[marked deformation theorem](actual_complete_core_geometric_deformation.md)
resolves the boundary reconstruction dependency stated below, retaining
the primitive collar and the complex regulator boundary correction.
It does not remove the ordinary-color subsets from the full source.

## 1. The finite object and theorem

Fix a connected labeled convex ideal right-angled augmented source D
covered by the [signed complete-source theorem](general_signed_augmented_source_volume.md).
Retain its actual two marked faces, exterior normalization, and a vector
of half twists epsilon_i in {0,1,-1}. Let R be its number of crossing
circles and n=R-1 the dimension of the finite-face logarithmic torus
after fixing scale. All constants below may depend on this fixed labeled
diagram. Its bridge number and matching graph are otherwise unrestricted
within that geometric certificate.

Set d=N-1, M=floor(d/2), s0=d-2M, and delta_min=s0/(2N).
The [exact color reflection](actual_external_circle_reflection_and_cusp.md)
specifies the complete-image core F_N(h), before any asymptotics, by
multiplying each complete channel a_i by cos(pi h_i(d-2a_i)/N).
In particular F_N(0) is the original signed complete augmented source.
Cosine makes F_N(h) an entire function of its external variables h.
No interpolation of an unspecified sequence is being chosen here.

The following holds on a fixed complex polydisc |chi_i|<rho, where
chi=h/N. There are holomorphic critical actions S_N(chi), and
nonsingular symmetric Hessians K_N(chi) of dimension m=2R-1, such that

    F_N(N chi)/F_N(0)
      = exp[N(S_N(chi)-S_N(0))]
        sqrt[det K_N(0)/det K_N(chi)] [1+O(N^-1)].       (1)

The error is uniform on a smaller closed polydisc. The square root is
the holomorphic branch equal to1 at chi=0. Thus the actual core is
nonzero throughout that closed polydisc for all sufficiently large N.
Both parities and composite quantum levels are included. The functions
S_N converge holomorphically to S, and

    S(0)=Vol(Y_D^epsilon)/(2pi)=Vol(Q_D)/pi,
    lim (2pi/N) log|F_N(N chi)|=2pi Re S(chi).          (2)

The second equality is a locally uniform limit. The factor (1) retains
S_N in its exponential: holomorphic convergence S_N -> S alone does
not permit replacing exp(N S_N) by exp(N S).

Only the COMPLETE VALUE of S in (2) is identified here with the actual
hyperbolic volume. Identifying its whole germ with the marked geometric
regulator requires the boundary reconstruction described in section7.
The theorem also does not estimate the nonempty ordinary-color subsets
in the original reflection identity.

## 2. Exact reflected period and analytic local factors

Write

    B_(N,a)(x,b,c,y)
       = beta_a^2 D_a(x,b,y)D_a(x,c,y)P_(d-2a)(x,y).

The [exact polynomial reflection](actual_positive_face_fixed_fold_packet.md)
extends this original polynomial from 0<=a<=M to 0<=a<=d by
B_(N,d-a)=B_(N,a); the half-twist eigenvalue obeys the same reflection.
Consequently the original multiplicities k_a and cosine weights unfold
to one full finite sum, with no omitted endpoint:

    F_N(N chi)=chi_(D,N) N^R product_i omega_M^epsilon_i
      *(2pi)^(-n) integral_(face torus)
        sum_(delta in Lambda_N^R)
        product_i B_(N,a_i)(r exp(i theta))
        /product_(finite faces) (r_f exp(i theta_f))^d
        *exp[pi i N sum_i epsilon_i(delta_i^2-delta_min^2)
                     +2pi i N sum_i chi_i delta_i] dtheta.   (3)

Here delta_i=(d-2a_i)/(2N), a_i=0,...,d. Lambda_N is the physical
integer or half-integer lattice of mesh 1/N in the finite interval
[-d/(2N),d/(2N)]. At fixed scale one theta coordinate is zero.
The two marked face variables remain zero. Equation(3) is the literal
marked coefficient measure, including its N^R factor and framing unit.

Use r=r_N, the positive critical radius of the all-M coefficient.
The [coefficient theorem](actual_positive_face_coefficient_saddle.md)
gives r_N -> r_geom, transverse Hessian cN<=H_face,N<=CN, and
fixed logarithmic derivatives O(N) on a common face neighborhood.
Positive-matrix preconditioning makes the determinant factors nonzero
on a fixed complex neighborhood, including the actual zero patterns.

The [exponential interpolation theorem](actual_positive_face_exponential_fold_interpolation.md)
supplies even holomorphic functions Phi_i,N(delta;w)=-H_i,N(delta;r_N exp w)/N
on fixed complex delta and face neighborhoods, with Phi_i,N(0;w)=0,

    B_(N,a)(r_N exp w)/B_(N,M)(r_N exp w)
      = exp[-N(Phi_i,N(delta;w)-Phi_i,N(delta_min;w))]
          [1+O(exp(-cN))].                              (4)

This comparison holds on the actual REAL channel grid and for COMPLEX
face variables w. Uniform holomorphic derivatives and comparison with
V_i(delta;r_N exp w) hold on smaller neighborhoods; these functions
converge to V_i(delta;r_geom exp w). In particular, at the finite radii,

    partial_delta^2 V_i(0;r_N exp w)=2C_i(r_N exp w),
    C_i=pi(sqrt(b_i(x_i+y_i)+x_i y_i)
                  +sqrt(c_i(x_i+y_i)+x_i y_i))/(x_i+y_i)>0

at positive real radii. The comparison error in (4) is exponential,
which is essential when the Fourier transform itself has an exponential
decay. A relative O(N^-1) grid estimate would not suffice.

## 3. Excluding the original complement

Choose small fixed cutoffs delta0,theta0 inside the neighborhoods of
(4). If some |delta_i|>delta0, the original all-channel shared-radius
bound gives an exp(-cN) gap relative to the complete scale. This is the
bound proved from the literal determinant and forced polynomial in the
[channel-rate theorem](actual_positive_face_channel_rate.md), together
with the strict maximum at the fold. The external weight in (3) costs
at most exp(pi N sum_i |Im chi_i|). A sufficiently small fixed chi
polydisc preserves the gap. There are only polynomially many channels.

For all |delta_i|<=delta0 but |theta|>theta0, apply the exact positive
matrix contraction to every original determinant. Its pair-trace lower
bounds cN are uniform for a/N in [1/2-delta0,1/2]. Indeed the bulk
Cholesky-square bounds in the coefficient theorem use a fixed compact
index interval strictly below N/2; choose delta0 so that every matrix
under consideration contains that same macroscopic interval. The
one-variable boundary factors need no pair trace. The remaining actual
pair graph is connected and primitive, exactly as in that theorem.
Thus, uniformly over these channels,

    |product_i B_(N,a_i)(r_N exp(i theta))|
       <= product_i B_(N,a_i)(r_N)
                      *exp[-cN dist(theta,0)^2].         (5)

Each forced polynomial has nonnegative coefficients and cannot increase
the torus modulus. This is a global angular estimate on the actual
physical summands, not on their local interpolants. Shrinking chi again
preserves its fixed gap outside theta0. Both discarded parts of (3)
are therefore bounded by a polynomial times exp[N(f_N-c)], where

    f_N=N^-1 log[product_i B_(N,M)(r_N)/product_f r_N,f^d].

Any polynomial factor is absorbed by reducing c for large N.

## 4. The selected joint critical point

On the retained face box put w=i theta and define the marked logarithms

    psi_N(w)=N^-1 log[product_i B_(N,M)(r_N exp w)]
                       -(d/N) sum_f log(r_N,f exp w_f),

    Psi_N(theta,delta;chi)=psi_N(i theta)
       -sum_i[Phi_i,N(delta_i;i theta)-Phi_i,N(delta_min;i theta)]
       +pi i sum_i epsilon_i(delta_i^2-delta_min^2)
       +2pi i sum_i chi_i delta_i.                       (6)

All logs continue the original positive factors. The even-level anchor
delta_min is retained. The framing and omega_M factors stay outside
this phase.

At chi=0, evenness makes every delta derivative vanish exactly at
delta=0. Also d_theta psi_N(0)=0, and the anchor contributes only
O(N^-2), with the same bound for fixed derivatives. The joint critical
point therefore lies O(N^-2) from (theta,delta)=(0,0). The negative
Hessian there has the blocks

    N^-1 H_face,N + O(N^-2),
    diag_i[2(C_i(r_N)-pi i epsilon_i)]+o(1).             (7)

Mixed theta/delta blocks vanish exactly at delta=0. The real quadratic
part on real integration directions is uniformly positive. All fixed
holomorphic derivatives of Psi_N are bounded independently of N.

The analytic inverse-function argument now gives a unique nearby joint
critical point z_N(chi) on a fixed small complex polydisc. One direct
uniform construction is Newton iteration after multiplying by the
inverse Hessian at chi=0: its norm is bounded, and the bounded third
derivatives give a common contraction ball. Define

    S_N(chi)=Psi_N(z_N(chi);chi),
    K_N(chi)=-d_z^2 Psi_N(z_N(chi);chi).                (8)

The Hessian stays nonsingular and its real quadratic part stays
positive along the translated real contour. S_N(chi)-f_N is uniformly
small when chi is small. The neighborhood can therefore be chosen so
that the preceding fixed complement gaps remain gaps relative to the
selected critical value, not just relative to f_N.

## 5. Finite lattice to contour integral, with exponential errors

Use (4) only on the retained physical grid. Its accumulated error in
(3) is at most exp[N(f_N-c)] on a smaller fixed chi polydisc: the
finite count is polynomial, the model is bounded by the original real
scale up to the small complex Fourier cost, and (4) has a fixed
exponential rate.

For one channel write its lattice as z=alpha_N+j/N. Enclose its retained
nodes in a rectangle whose vertical sides are halfway between the last
retained node and the first deleted node, and whose horizontal sides
have heights +/-eta. For a holomorphic f the exact residue identity is

    (1/N) sum_(retained nodes) f(z)
        =(1/(2i)) integral_(rectangle)
                         cot(pi N(z-alpha_N)) f(z) dz.  (9)

On the upper and lower sides cot approaches -i and +i respectively,
with errors O(exp(-2pi eta N)). On the vertical sides it is bounded
because their real coordinates are lattice midpoints. The constant
upper/lower terms deform to the real interval integral. The vertical
closing segments are exponentially small by the original quadratic
channel gap and its analytic continuation.

Here are the estimates needed for that last assertion and for the
horizontal errors. On the small box, the real Hessian bound from (7)
and the bounded derivatives imply, for real theta and real channel
coordinates x with imaginary shifts y,

    Re Psi_N(theta,x+i y;chi)
       <= f_N+C/N^2-c(|theta|^2+|x|^2)
                      +C|y||x|+C|y|^2+C|chi|(|x|+|y|).

After completing squares this is at most
f_N+C/N^2+C'(|y|^2+|chi|^2). At a vertical edge |x_i| near delta0,
retain half its negative quadratic term before completing squares.
Choose eta sufficiently small compared with delta0. Then choose chi
small compared with eta and delta0, so both the vertical edge loss and
the horizontal cotangent loss 2pi eta dominate the possible phase
growth. This estimate includes the cross term from the half-twist
quadratic; a pointwise claim of only O(eta^2) growth would omit it.

Apply (9) successively in all R channel variables. For the resulting
mixed contours, |y|^2<=R eta^2. R is fixed, so reserve constants such
that C'R eta^2<pi eta, then shrink chi. Every term containing at least
one horizontal cotangent error or vertical segment retains a fixed
exponential loss. Thus, uniformly on the local real theta box,

    sum_(local grid) exp(N Psi_N)
        =N^R integral_(local real delta box) exp(N Psi_N) ddelta
                              +O(exp[N(f_N-c)]).        (10)

Changing N parity changes alpha_N only. There is no periodic extension
past the original physical endpoints and no removal of a source factor.

## 6. Uniform saddle formula and limiting action

The retained integral now has m=n+R=2R-1 real variables. Move the
local box through z_N(chi) inside its holomorphic neighborhood. Its
side faces keep the same fixed gap after decreasing rho. On the
translated real box the quadratic part has positive real part.
Expand at z_N(chi), scale by N^-1/2, and extend the Gaussian integral
with an exponentially small error. The odd cubic term integrates to
zero; bounded fourth and higher derivatives give relative O(N^-1).
This proves

    F_N(N chi)=chi_(D,N) N^(2R) product_i omega_M^epsilon_i
       *(2pi)^(-n)(2pi/N)^(m/2)
       *exp[N S_N(chi)]/sqrt(det K_N(chi)) [1+O(N^-1)]. (11)

The Gaussian square root is selected by the real positive quadratic
part and continued from chi=0. It cannot vanish on the chosen
polydisc. All omitted terms remain exponentially small relative to
(11), because |Re(S_N(chi)-f_N)| was reserved below their gaps.
Taking the ratio at zero gives (1) with every original normalization
factor canceled literally. Uniformity and nonvanishing also permit
differentiation of its holomorphic relative error on smaller polydiscs.

For completeness, psi_N converges holomorphically on a smaller face
neighborhood. Its real-radius limit is the original determinant and
sine-product rate. Uniform bounds for its marked logarithm follow from
positive-summand preconditioning and that rate. Cauchy estimates make
the family locally compact; any subsequential holomorphic limit has
the prescribed values on the real open cube, hence is unique by
successive one-variable identity theorems. This proves convergence
without exchanging an uncontrolled large determinant with a derivative.
The same conclusion for Phi_i,N follows directly from its construction.
The uniform critical-point contraction then gives S_N -> S and
K_N -> K holomorphically.

At chi=0, the actual facet-coning calculation in the coefficient theorem
fixes the additive constant f_N -> Vol(Y_D^epsilon)/(2pi).
The anchor and critical displacement tend to zero. Equation(11) has
only polynomial outside factors and framing of unit modulus. These
facts prove (2), including the actual complete hyperbolic volume.

## 7. What this proves on the general long-twist path

The theorem supplies a fixed complex external-color neighborhood for
the original complete core; the earlier h=O(sqrt N) packet did not
supply this. It proves a selected nonzero analytic period, with its
complete action fixed by actual geometry, for every fixed diagram in
the stated certificate class.

The [coupled polynomial system](actual_whole_source_coupled_face_difference_system.md)
also identifies the ordered local momenta on regular character charts,
including the face momenta and peripheral equation. At the two marked
zero faces those charts can degenerate. For example x>0,b=y=0 gives
E=x and D=x^2 for all channel deformation: the quadratic root is
double and no longer records the chosen flag. A separate developing
map or finite common-conjugated boundary limit is still needed to
identify the whole S germ with the actual marked geometric regulator.
The complete volume and cusp-Hessian matches alone do not prove that.

The full color reflection has additional terms with one or more
ordinary colors. The core also has an opposite-end alias that cancels
only after those terms are restored. Consequently (1) cannot be
substituted for a whole-source filling estimate. General proper-subset
and combined far-alias bounds remain required for all independently
long fixed twists. The twist threshold in that target depends on the
fixed diagram; the twist numbers are fixed before N tends to infinity.

## Verification scope

The argument uses the coefficient, signed-source, exact-reflection and exponential-interpolation theorems, with the original normalization and both parity anchors.

The [focused audit](../experiments/audit_actual_complete_core_complex_packet.py) and [saved results](../experiments/actual_complete_core_complex_packet_results.json) check 10 literal original W/pi sources with off-grid external clocks, 24 shared K4 complex cores and exact face coefficients, 768 retained reflection entries, 20 cotangent basis identities and two full two-register contour identities, and 36 original fixed-window matrix gap samples. Finite complex values and nonzero samples are diagnostics. The written proof supplies the uniform estimates; these checks do not settle the remaining marked-geometric or mixed-source steps.