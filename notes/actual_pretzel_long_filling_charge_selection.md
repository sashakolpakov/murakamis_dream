# Local charge selection for independently long pretzel fillings

29 October 2026. This proves a uniform analytic property of the
ACTUAL mixed-source action, not a choice of a new quantum invariant.
For independently large positive or negative filling integers, the
nonzero charges of smallest absolute value have strictly largest
real critical action throughout a fixed local charge corridor. Their
local coefficients do not cancel under the exact Weyl symmetry.
Global color and Fourier-tail estimates remain separate inputs to a
theorem about the whole filled knot.

## 1. The source action and its Fourier transform

Fix odd s>=5. Use the independently proved analytic action Phi(chi)
in [the mixed-source theorem](actual_pretzel_mixed_cusp_period_survival.md)
and its [exact analytic source packet](actual_pretzel_exact_analytic_color_packet.md).
Write

    F0=V_s/(2pi), u_s=atan(sec(pi/s)),
    tau=(1+exp(2iu_s))/2.

Both Re tau and Im tau are strictly positive. The exact source's
selected action is holomorphic, even separately in each chi_i, and

    Phi(chi)=F0+(i tau/pi) sum_i chi_i^2+O(||chi||^4).       (1)

All roots and action constants continue from the original complete
source. In particular F0 is not a freely chosen normalization.

There is a unique holomorphic chi(z) near zero satisfying

    partial_(chi_i) Phi(chi(z))+2i z_i=0.

Indeed the derivative in chi at zero is (2i tau/pi)I. Define

    Psi(z)=Phi(chi(z))+2i sum_i chi_i(z)z_i.                (2)

This is the local action of the actual color Fourier transform:
chi_i=pi h_i/N and exp(2pi i h_i z_i) contributes 2i chi_i z_i
to the exponent divided by N. Existence of (2) alone is not the
asymptotic evaluation of that finite transform; its contour/error
estimates must use the exact analytic packet, not a pointwise
O(1/N) error on the color grid.

Uniqueness and the separate evenness of Phi give separate evenness
of Psi. Differentiation of (2) gives Psi_(z_i)=2i chi_i, hence

    Psi(z)=F0-(i pi/tau) sum_i z_i^2+O(||z||^4).           (3)

Put b=pi Im(tau)/|tau|^2>0. For real z this has real quadratic
term -b sum_i z_i^2. In a sufficiently small complex polydisk,
Psi has a convergent series in z_1^2,...,z_s^2.

## 2. Remove the apparent singularity at infinite slope

For fixed nonzero integers p_i and charges m_i, the actual centered
filling kernel with P_i=-p_i has local phase

    T_m(z)=Psi(z)-2pi i sum_i (p_i z_i^2+m_i z_i).         (4)

The half twist is already included in Phi; it is not removed here.
Set epsilon_i=1/p_i and t_i=m_i/p_i. The critical equation is

    z_i=-t_i/2+epsilon_i Psi_(z_i)(z)/(4pi i).             (5)

At epsilon=0 its derivative in z is I. Consequently one fixed
polydisk in (t,epsilon) has a unique holomorphic solution z(t,epsilon),
with z(t,0)=-t/2. The epsilons can vary independently and can have
either sign. No comparability of the filling lengths is required.

Completing the square in (4) gives

    T_m(z(t,epsilon))
       =(pi i/2) sum_i t_i^2/epsilon_i+B(t,epsilon),

    B(t,epsilon)=Psi(z(t,epsilon))
          +(i/(8pi)) sum_i epsilon_i Psi_(z_i)(z(t,epsilon))^2.
                                                               (6)

The last expression is holomorphic even when any epsilon_i=0.
For real t,epsilon the first term in (6) is purely imaginary.
Thus Re B is exactly the real critical action whenever p_i are
real and nonzero. The apparent large charge-dependent phase is not
discarded; it is explicitly isolated from its real growth.

Equation (5), the symmetry of Psi and uniqueness show that B is
separately even in the t_i. Thus B(t,epsilon)=Bhat(t_1^2,...,t_s^2,epsilon)
for a holomorphic Bhat near zero. Equations (3),(6) imply

    partial_(xi_i) Re Bhat(0,0)=-b/4, xi_i=t_i^2.        (7)

Continuity now gives fixed positive t0,epsilon0 such that on the
REAL box 0<=xi_i<=t0^2, |epsilon_i|<=epsilon0,

    partial_(xi_i) Re Bhat(xi,epsilon)<=-b/8.             (8)

This is a uniform derivative estimate, not a comparison only along
the diagonal t_1=...=t_s.

## 3. Every nonminimal local charge has a strict action gap

Take independent integers |p_i|>=1/epsilon0, enlarged if necessary
so that 1/|p_i|<t0. Let all m_i be NONZERO integers with
|m_i/p_i|<=t0. Choose any signs sigma_i in {+1,-1}. Integrate
(8), one squared coordinate at a time, from xi_i=1/p_i^2 to
xi_i=m_i^2/p_i^2. Equation (6) gives

    Re T_m(z_m) <= Re T_sigma(z_sigma)
                      -(b/8) sum_i (m_i^2-1)/p_i^2.    (9)

The rightmost term is strictly negative unless every |m_i|=1.
For each fixed tuple of slopes this is a positive exponential gap
in N, even when some slopes are much larger than others. Every
choice of signs sigma has exactly the same complex critical value,
since (4) is preserved by the simultaneous transformations
(m_i,z_i)->(-m_i,-z_i), separately in each coordinate.

The quadratic approximation also has a useful exact-in-p form.
Solving (5) for the quadratic part of Psi and using analytic
perturbation gives, uniformly in the same parameter polydisk,

    z_i=-m_i tau/(1+2p_i tau)+O(|epsilon_i| ||t||^3),

    T_m(z_m)=F0+i pi sum_i m_i^2 tau/(1+2p_i tau)
                                      +O(||t||^4).     (10)

Here constants may depend on s and the chosen fixed polydisk.
There is no singular denominator for the permitted real slopes:
Im tau>0. Consequently

    Re T_m(z_m)=F0-pi Im(tau)
                 sum_i m_i^2/|1+2p_i tau|^2+O(||t||^4).
                                                               (11)

The exact inequality (9), rather than the truncated expansion (11),
is what proves charge ordering for arbitrarily unequal slopes.
Equation (11) has the expected negative quadratic volume correction;
it does not identify the full action with the filled geometric volume.

## 4. Nonzero local amplitude and the exact sign pairing

The exact combined filling formula retains the amplitude

    product_i m_i sinh(2pi i z_i)

and the finite parity character product_i (-1)^(m_i(N-1)); see
[the original filling kernel](actual_coherent_filling_gaussian_chirp.md)
and the subsequent source-inclusive Fourier calculation. The local
Fourier-source amplitude is holomorphic and nonzero near zero
whenever its analytic stationary evaluation has been established.

Write Psi_(z_i)=z_i Q_i(z_1^2,...,z_s^2) with Q_i analytic.
Equation (5) becomes

    z_i=-t_i/[2(1-epsilon_i Q_i(z)/(4pi i))].             (12)

Shrink the polydisk so the denominator is nonzero and |z_i|<1/4.
For t_i!=0, z_i is nonzero; therefore sinh(2pi i z_i) is nonzero.
The Hessian in (4) is also nondegenerate: multiplication of its i-th
row by epsilon_i makes it tend uniformly to -4pi i I. Its real
part on real tangent vectors is the negative definite real part of
Psi'' near zero. The translated real local contour thus has a
nonzero Gaussian coefficient with its branch fixed by that contour.

Under m_i->-m_i and z_i->-z_i, both m_i and its sinh factor change
sign. Their product, the parity character, the source amplitude and
the local integral are unchanged. This is also an exact change of
variables in the finite-interval charge integral when the retained
source is separately even. Hence the 2^s minimal signed charges ADD;
they cannot cancel solely because of their signs or level parity.
This does not remove any other charge by assumption.

## 5. Scope of the result

The proof establishes local charge dominance for the actual action
and a nonzero paired local coefficient. To turn it into an asymptotic
for the original filled scalar one must still bound the complementary
color regions and Fourier regions, retain every endpoint current,
and compare the action with the correctly marked filled geometry.
Those requirements cannot be replaced by (11) or by formal stationary
equations. The exact source packet and exact filling kernel supply
the inputs for those additional estimates.
