# Survival of the original filling sum restricted to a cusp-color corridor

29 October 2026. For every fixed odd box count s>=5 there is a fixed
complete-color corridor in which the ENTIRE original coherent filling
sum has a nonzero selected asymptotic, for all independently sufficiently
large signed integer slopes. This includes all physical normal jets,
the actual half-color weight, every Fourier charge and the original
marked source. It does not estimate the complementary physical colors,
and therefore is not yet a theorem about the whole filled knot.

## 1. The precise truncated original scalar

Use q,Q,kappa,d and the original mixed marked source A_(s,N)(h).
For an integer P let beta_j^(P) be the ACTUAL circle-basis coefficient
of r_N^(2P); the full R^(2P) includes the factor kappa^(2P).
Choose a sufficiently small fixed delta>0 and H=floor(delta N).
For fixed nonzero integers p_i define

\[
 \mathcal K_{N,\delta}^{\boldsymbol p}
 =\kappa^{-2\sum_i p_i}
  \sum_{h_1,\ldots,h_s=0}^{H}
       \prod_i\beta_{N-h_i-1}^{(-p_i)}
                           A_{s,N}(h_1,\ldots,h_s).       \tag{1}
\]

This is the indicated physical color corridor of the actual boxes
rotation(R^(-(2p_i+1))). It is not a single color term. No new
modified dimension is placed on the ordinary auxiliary loops.

There is p_0(s,delta) such that for EVERY FIXED tuple |p_i|>=p_0,
with no comparability condition between slopes, (1) has

\[
 \boxed{\mathcal K_{N,\delta}^{\boldsymbol p}
   =N^{3/2}e^{-is\pi d/4}\kappa^{-\sum_i p_i}
      D_s(\boldsymbol p)e^{N\mathcal A_s(\boldsymbol p)}
                                      (1+O_{s,\boldsymbol p}(N^{-1})),}
                                                               \tag{2}
\]

where D_s is explicitly specified below and is NONZERO. This holds
at both parities and all composite levels as N tends to infinity.
The slopes are fixed before this limit; no claim uniform in growing
slopes is made.

## 2. The source action, actual Fourier amplitude and leading constant

Let C_N be the EXACT finite packet in
[the analytic color-source theorem](actual_pretzel_exact_analytic_color_packet.md).
It has the SAME original full-Hermite Phi_2 functional. Its uniform
complex asymptotic supplies A_s(chi),Phi_s(chi), with

    F_0=Phi_s(0)=V_s/(2pi), A_s(0)=C_s !=0,
    phi(x)=Phi_s(pi x), phi''(0)=2pi i tau_s I,
    tau_s=(1+exp(2iu_s))/2, Im tau_s>0.

The exact Fourier-packet theorem in
[the source Fourier estimate](actual_filling_source_fourier_endpoint_gap.md),
section6, gives holomorphic even functions xi(z),Psi(z),B(z):

    grad phi(xi)+2pi i z=0,
    Psi(z)=phi(xi)+2pi i xi dot z,
    B(z)=(2pi)^(s/2) A_s(pi xi)/sqrt(det[-phi''(xi)]).

Thus Psi=F_0-i pi sum z_i^2/tau_s+O(||z||^4), and B is nonzero
near zero. These are defined by the original selected packet, not
an arbitrary classical branch.

Put

    T_m(z)=Psi(z)-2pi i sum_i(p_i z_i^2+m_i z_i).

For sufficiently large |p_i| the all-unit charge m=(1,...,1) has
the unique nearby critical point z_*=z_(1,...,1). Define

\[
 \mathcal A_s(\boldsymbol p)=T_{\boldsymbol1}(z_*),\qquad
 D_s(\boldsymbol p)=
  \frac{2^s(2\pi)^{s/2}B(z_*)\prod_i\sinh(2\pi i z_{*,i})}
                          {\sqrt{\det[-T_{\boldsymbol1}''(z_*)]}}.
                                                               \tag{3}
\]

Every square root is the one from the actual translated real
Gaussian contour. Equivalently it is the analytic Gaussian branch
on complex symmetric matrices with positive definite real part,
fixed positive on real positive matrices. This retains the signed
slope Gaussian phases, rather than choosing their moduli.

The [local charge theorem](actual_pretzel_long_filling_charge_selection.md)
proves that every z_(star,i) is nonzero, |z_(star,i)|<1/4, and the
Hessian is nondegenerate. Consequently every factor in (3) is
nonzero. In particular D_s is not a postulated cycle coefficient.
The actual critical action has

    Re A_s(p)=F_0-pi Im(tau_s)
               sum_i |1+2p_i tau_s|^(-2)+O(sum_i |p_i|^(-4)),

where the exact holomorphic action in (3), not this truncation, is
used in (2). Its geometric peripheral interpretation is separate.

## 3. Exact source replacement and finite charge reduction

The source theorem proves, on the physical grid in (1),

    |A_(s,N)(h)-C_N(pi h/N)|
                          <=poly(N)exp[N(F_0-gamma)], gamma>0.

Since |beta_j^(-p)|<=2(1+|p|), replacing A by C in the WHOLE
truncated sum costs poly_(s,p)(N)exp[N(F_0-gamma)]. The upper color
aliases need not be even and are estimated here, BEFORE folding.
No full physical source is analytically continued by fiat.

The exact C_N is even in each color. Apply the physical Weyl half
weight and the full normal kernel in every coordinate. With

    mathcalF_N(z)=sum_(|h_i|<=H) C_N(pi h/N)exp(2pi i h dot z),

the SAME truncated packet is exactly

\[
 (-1)^{s(N-1)}\kappa^{-\sum_i p_i}
 \sum_{m_i\ne0}(-1)^{(N-1)\sum_i m_i}\prod_i m_i
 \int_{[-1/2,1/2]^s}
 e^{-2\pi iN\sum_i(p_i z_i^2+m_i z_i)}
                   \prod_i\sinh(2\pi i z_i)\mathcal F_N(z)\,dz.
                                                               \tag{4}
\]

The source Fourier theorem proves a UNIFORM exponentially gapped
tail outside |m_i|<=M_i, where one may take M_i>=2|p_i|+2delta+2.
Its gap depends only on the SOURCE, not on the largest slope: the
paired vertical current keeps its growth exp(2pi|p_i|Nv), which
the larger charge absorbs. Shrinking the contour as 1/|p_i| would
not give the needed independent-slope conclusion.

Its multiport use is exact telescoping of commuting COLOR-register
functionals, not a physical operator relocation: remove one high
charge with every remaining coordinate still on its original REAL
finite grid or in a FINITE real charge integral. Those spectators
have unit-modulus chirps, and their fixed derivatives/sums cost only
powers of N. Formula (14a) in the source Fourier note gives the
precise identity and uniform mixed-derivative estimate. No other
port is moved to a complex saddle until all such tails are removed.

The same theorem shows that mathcalF_N and its fixed derivatives
are exponentially small whenever any real |z_i|>=eta for fixed
sufficiently small eta>0. Thus only a finite set of nonzero charges
and a fixed central real z-cube remain, with original side currents
already included in the errors. On a fixed complex neighborhood of
that cube, the EXACT Fourier packet has its nonzero, uniform
asymptotic with exponent Psi and prefactor N^((s+3)/2)B. This is
established BEFORE moving any central charge contour.

## 4. Nonlocal finite charges have a fixed gap

Choose the local charge scale t_0 from the local charge theorem
much smaller than the central analytic z-window. If some
|m_i/p_i|>=t_0, split its REAL coordinate into
|z_i|<=t_0/4 and its complement. The complement has a fixed
source Fourier gap, regardless of the other real coordinates.

On the inner interval, m_i+2p_i z_i has the sign of m_i and
magnitude at least |p_i|t_0/2. For sufficiently large |p_i| the
bounded normal derivative of Psi cannot change that sign.
Shift z_i by -i sigma sign(m_i) for a fixed small sigma>0.
The real part of the filling phase decreases along the entire
translation, including BOTH endpoint connectors. The real part
of the chirp derivative is controlled because p_i is real, with
either sign; its imaginary normal derivative depends on the
combination m_i+2p_i Re z_i. The exact analytic Fourier packet
remains within its proved complex neighborhood.

At the connectors' starting points the source Fourier gap already
holds. On the translated inner segment the phase drops by a fixed
positive amount when |p_i| is large enough. This gives an absolute
bound poly_(s,p)(N)exp[N(F_0-g_0)] for every such finite charge,
with g_0>0 independent of the particular large slopes. The number
of finite charges depends on p but not on N. No finite-order
integration-by-parts error is substituted for this exponential gap.

## 5. Local finite charges: actual contour and noncancellation

For |m_i/p_i|<=t_0 the local charge theorem gives a unique saddle
z_m, with

    z_(m,i)=-m_i tau_s/(1+2p_i tau_s)+O(|p_i|^(-1)||m/p||^3),
    |Im z_(m,i)|<=C |p_i|^(-1)|m_i/p_i|.

The second estimate is COMPONENTWISE: it follows from the exact
separate-evenness factorization (12) in the local charge theorem,
not merely its coarser multivariate Taylor remainder. It is what
allows unrelated filling lengths in the next contour estimate.

Translate the small real integration cube to the parallel real
cube through Im z_m. Its saddle has real coordinates strictly
inside that cube. The endpoint connectors stay below the selected
height: their original source Fourier gap is fixed, while
|p_i Im z_(m,i)|<=C t_0 and |m_i Im z_(m,i)|<=C t_0^2.
Taking t_0 sufficiently smaller than the cube width controls these
changes uniformly for independently unequal signed slopes.

On the translated cube the REAL Hessian of T_m is the real Hessian
of Psi; the quadratic filling chirp has purely imaginary Hessian.
It is uniformly negative definite. The critical point is therefore
the unique real maximum on that translated contour and its ends
have a strict Gaussian gap. Holomorphic Gaussian expansion of the
EXACT packet, with its uniform complex asymptotic, yields the
nonzero contribution

    N^(3/2)e^(-is pi d/4) kappa^(-sum p_i)
       parity(m) (2pi)^(s/2) B(z_m)
       [product_i m_i sinh(2pi i z_(m,i))]
       exp[N T_m(z_m)]/sqrt(det[-T_m''(z_m)])
                                                *(1+O_(s,p)(1/N)).

Here parity(m)=(-1)^((s+sum_i m_i)(N-1)) is unchanged by every
coordinate reflection. The factor N^(s/2) from the source Fourier
packet cancels the z Gaussian N^(-s/2); the original N^(3/2)
marked-source factor remains.

For fixed slopes, all nonminimal local charges have a strict gap
below the unit charges:

    Re T_m(z_m)<=Re T_1(z_*)
             -(b/8)sum_i(m_i^2-1)/p_i^2, b>0.

This is the exact monotonicity theorem, not a quadratic guess.
The minimal charges m_i=+/-1 have identical contributions by the
EXACT reflected source integral. Their parity factor is one, and
their products m_i sinh are unchanged under reflection. Their 2^s
contributions ADD and give precisely (3).

Finally, Re A_s(p) tends to F_0 as all |p_i| tend to infinity.
Choose p_0 large enough that its deficit is smaller than half every
fixed source, high-charge and nonlocal-charge gap above. This
absorbs all absolute source errors. For each fixed tuple the
remaining local nonminimal gap may be small, but is strictly positive
and is exponential in N. The leading coefficient (3) is nonzero,
so (2) follows.

## 6. The remaining whole-source gates

This theorem is a source-preserving result for the PHYSICAL color
corridor in (1). It retains every normal mode and does not discard
the color complement h_i>H. That complement could still alter or
cancel this contribution unless separately bounded. Nor is the
identification of A_s(p) with a preferred filled hyperbolic action
assumed: the auxiliary meridian and preferred-longitude sign must
still be matched. Neither condition follows from local stationarity
or from Cauchy alone.

[Audit](../experiments/audit_actual_pretzel_cusp_corridor_filling_survival.py)
checks the full normalized-source chirp, signed Gaussian branches,
N^(3/2) density and parity pairing on explicit analytic packets.
The actual pretzel source hypotheses are the independently proved
finite-packet and charge theorems linked above.

The finite checks retain the original source and Fourier normalization. They supplement the analytic proof and do not establish uniform estimates by sampling.