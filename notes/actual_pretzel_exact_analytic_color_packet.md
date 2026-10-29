# An exact analytic color packet carrying the original mixed pretzel source

29 October 2026. Fix an odd s>=5. There is an EXACT finite,
holomorphic, separately even color packet C_N(chi_1,...,chi_s),
defined using the original factorial coefficients and the full marked
Hermite functional. It approximates the physical mixed-color source
with a uniform, explicitly retained exponential gap in a fixed cusp
corridor. The packet ITSELF, rather than merely its leading expression,
satisfies a complex Gaussian growth bound. This is the source input
needed before applying a Fourier/cotangent endpoint estimate.

The theorem does not remove the rest of the physical color cube or
identify a filled-knot volume. Those remain separate source terms.

## 1. Definition by actual finite coefficients and the original mark

Use N,d,q,Q,kappa,M and the original f_v,P_r,Omega as in
[the exact complete polynomial](actual_pretzel_complete_base_casimir_polynomial.md).
Let eta_s=2asinh(tan(pi/s)), R_s=exp eta_s,
u_s=atan(sec(pi/s)), and F_0=V_s/(2pi). Choose FIXED numbers

    1/4<a<u_s/pi<b<1/2,
    I_N={ceil(aN),...,floor(bN)}.

For sufficiently large N this is a nonempty physical index window.
Shrink a fixed complex chi disk so that |Re chi|/pi<a/2 and all
arguments below lie in regular compact scaled factorial substrips.
Put h=N chi/pi, and define the finite holomorphic function

    Ahat_(N,r)(chi)=sum_(v=r)^M
      Q^(-vr)F_(2v)
       /[F_v F_(v-r) Fhat_N(v-h)Fhat_N(v+h)], r in I_N.

Here F_a=(Q;Q)_a at the physical integers, and Fhat is the canonical
whole factorial completion with its ORIGINAL marks. Define the
polynomial

    c_N^win(z,chi)=N^2 sum_(r in I_N) b_(N,r)(chi) B_r(z),

    b_(N,r)(chi)=kappa^(-1)q^(h^2)(-1)^r q^(2r^2+r)
                                         Ahat_(N,r)(chi)/F_r^3,
    B_r(z)=product_(v=0)^(r-1)(c_v-z),
    c_v=q^(2v+1)+q^(-2v-1).                            (1)

The powers q^(h^2)=exp(iN chi^2/pi) and the full kappa are KEPT.
They are not replaced by absolute values or a fitted period scale.
This polynomial is a finite explicit function, not an asymptotic
definition. It has degree at most floor(bN)<M+1 and is even in chi.
Its coefficients are holomorphic on a fixed complex disk, uniformly
in the sense of domains, since each denominator Fhat(v+/-h) is
nonzero there.

Use the ORIGINAL full-Hermite marked functional

    Phi_2(f)=(-1)^d sum_(c double)
                  [(4-c^2)f'(c)-c f(c)]
                        +1_(N odd)f(-2),

where the double and possible simple nodes are those of
P_N(z)=2T_N(z/2)+2. The exact packet is

    C_N(chi_1,...,chi_s)=Phi_2(product_i c_N^win(z,chi_i)). (2)

It is holomorphic and even in EACH color. Every original Casimir
normal derivative remains in (2). No positive quotient, ordinary
semisimple trace, or modified dimension for auxiliary components
is substituted. An external original normalization, if required,
is still multiplied separately with its already proved value.

Equivalently, for ANY fixed R>1, the SAME exact packet is

    C_N=(-1)^d N^2/(2pi i) integral_(|w|=R)
        product_i c_N^win(w+w^(-1),chi_i)
                   w^N(1-w^(-2))/(1+w^N)^2 dw.          (3)

This is the established residue formula for the actual marked
source. It keeps all finite windings, including the double-pole
normal weight. Formula (2), or (3), is the definition of C_N;
no unknown scalar knot period defines its metric or amplitude.

## 2. Exact relation to the physical mixed source and its residual

At an actual integer deficit 0<=h<aN/2, Fhat(v+/-h)=F_(v+/-h)
for every v>=r in I_N. Thus (1) is EXACTLY the indicated Newton
window of the physical low core c_(N,h). The finite source
identity proves

    z_(N,h)=c_(N,h)+R P_(N,h),

with the actual nonzero upper band retained separately. Put
A_N(h)=Phi_2(product_i z_(N,h_i)). The exact residual is

    A_N(h)-C_N(pi h/N)
      =Phi_2(product_i z_(N,h_i)-product_i c_(N,h_i))
       +Phi_2(product_i c_(N,h_i)
                         -product_i c_N^win(pi h_i/N)). (4)

There is a fixed corridor 0<=h_i<=delta_s N and gamma_s>0 such
that, uniformly on this physical color grid,

    |A_N(h)-C_N(pi h/N)|
                         <=poly(N)exp[N(F_0-gamma_s)].  (5)

Here are the two bounds, so neither residual in (4) is silently
discarded. The first is the proved
[uniform original RP-band source gap](actual_pretzel_mixed_alias_source_gap.md)
for odd s>=5. For the second, use the REAL-color all-index bound
from the mixed-source theorem and the original circle estimate at
R_s. The complete positive Newton profile J_R+E has its unique
maximum at u_s, so

    g_I=j(eta_s)-max_(u/pi outside(a,b))(J_R(u)+E(u))>0.

Every removed r-summand has circle height at most
j(eta_s)-g_I+C chi^2, and every retained or full core has height
at most j(eta_s)+C chi^2, with polynomial prefactors. Telescope the
product of s cores and use the EXACT source-circle bound from (3).
This gives

    |second residual|<=poly(N)
                 exp[N(F_0-g_I+C sum_i chi_i^2)].

First fix the index window and its gap, then shrink delta_s to
preserve at least half this gap and the independent RP gap. This
proves (5). The underlying sums in (4) remain the actual source
terms. The estimate is absolute, so it remains usable before a
subsequent filling sum with its known polynomial coefficient mass.
It is not an assertion that those terms vanish.

No complex continuation of the FULL physical low-index or upper-band
source is needed for (5). Only the EXACT packet (2) is continued.

## 3. The exact packet has a uniform complex-color asymptotic

After shrinking its fixed chi disk, the packet ITSELF satisfies

    C_N(chi)=N^(3/2)exp(-i s pi d/4)
              A_s(chi)exp[N Phi_s(chi)](1+O(1/N)),       (6)

UNIFORMLY on a fixed closed complex polydisk. The analytic functions
are those in the
[mixed-cusp construction](actual_pretzel_mixed_cusp_period_survival.md),
and A_s is nonzero there. This statement is stronger than a
pointwise approximation to the original real-grid full source.
It follows by applying that construction to (2) as follows.

First, the high-window coefficients are the natural COMPLEX-color
factorial source. The literal endpoint wall makes their continued
fractions exact on every physical r-grid, even when chi is complex.
The source theorem supplies a uniformly analytic action interpolant,
and its original-grid residual is relatively O(exp(-cN)), uniformly
in that complex color disk. The analytic Newton factor has its
proved prefactor ONE with all the original logarithmic marks.

Second, use the EXACT finite half-grid cotangent rectangle for the
r-window. Its vertical sides have |cot(Nu)|<=1 and a fixed endpoint
gap. Its horizontal remainders are O(exp(-2Nd)); their complete
phase grows only O(d^2) under that fixed vertical displacement.
Choose d first, then the fixed complex eta,chi neighborhoods.
All these remainders, INCLUDING the retained grid residual, are
exponentially below the complex saddle. The two constant cotangent
parts give the same analytic saddle integral with total density N/pi.
Uniform analytic Gaussian expansion gives the nonzero box amplitude
a(eta,chi), with the original exp(-i pi d/4) factor. This proves
the local box asymptotic for the EXACT high-window polynomial at
complex eta,chi.

Third, control the rest of the w circle WITHOUT invoking real-color
estimates on an off-grid source. The high-window WKB and canonical
factorial ratio imply, directly on the physical r-grid,

    |b_(N,r)(chi)|<=poly(N)[s_(2r)/s_r^6]
                                      exp(CN|chi|^2).

The finite Newton factor B_r(w) has the old strict angular envelope
away from w=-R_s, uniformly for a<=r/N<=b. Thus the exact packet's
noncentral circle parts have a fixed exponential gap for all small
COMPLEX chi. These estimates concern only the explicit finite packet,
whose domain contains that entire complex color polydisk.

Finally insert the analytic box asymptotic into the ORIGINAL source
contour (3). The nearby eta saddle has nonzero Hessian, stays in
Re eta>0, and is reached by a local contour shift with gapped
end connectors. No pole of (3) is crossed. The original sign and
normal kernel give exactly N^(3/2) and the amplitude A_s in (6).
The exact packet's exponential interpolation remainders stay below
this saddle after a fixed further shrink of the color disk. This
proves (6) uniformly in complex colors; it is NOT inferred by
analytic continuation of a pointwise real-grid error estimate.

## 4. A genuine complex Gaussian growth estimate for C_N itself

Write u_s=atan(sec(pi/s)) and

    a_0=sin(2u_s)/(2pi)>0,
    b_0=(1+cos(2u_s))/(2pi).

The actual source curvature is

    Phi_s(chi)=F_0+(-a_0+i b_0)sum_i chi_i^2+O(||chi||^4).

For chi=x+i y, the real quadratic part is

    -a_0||x||^2+a_0||y||^2-2b_0 sum_i x_i y_i
       <=-(a_0/2)||x||^2
                         +(a_0+2b_0^2/a_0)||y||^2.

Shrink the fixed complex polydisk until the quartic remainder is
at most (a_0/4)(||x||^2+||y||^2). Then (6), with bounded A_s,
proves an ACTUAL uniform inequality

    |C_N(x+i y)|<=C_s N^(3/2)
       exp{N[F_0-a_s||x||^2+B_s||y||^2]},              (7)

    a_s=a_0/4,
    B_s=5a_0/4+2b_0^2/a_0.

The constants and the color domain are independent of N. The
uniform relative O(1/N) error in (6) changes only C_s. In particular
(7) is a bound on the EXACT source function (2), not on
A_s exp(N Phi_s) after discarding a polynomially small error.

For Fourier estimates in the physical variable h/N, substitute
chi=pi h/N; both quadratic constants are multiplied by pi^2.
Because the packet is exactly even in every color, the actual
complete-color coefficient retains its physical half weight under
the proved Weyl fold. No extra 2N average, ordinary trace, or
one-sided exp(pi i h) completion is introduced.

## 5. Precisely what can now be combined with filling

The [Fourier endpoint lemma](actual_filling_source_fourier_endpoint_gap.md)
may be applied to the exact packet C_N, or to a slice of it with
the other colors retained, using (7). The physical error (5) is
still a separate explicit source term and must be multiplied by
the actual filling coefficient mass before estimating it. For fixed
twists that mass is polynomial, so its fixed gap is preserved.

This handles only the displayed small cusp-color window. The
complement of that physical color window, its upper RP bands,
other Fresnel charges and the geometric identification of the filled
critical action require their own proofs. Neither (5) nor (7)
licenses deletion of those parts of the original filling source.

[Audit](../experiments/audit_actual_pretzel_exact_analytic_color_packet.py)
checks the literal finite polynomial/source definition, its marked
phases, exact evenness and retained physical source decomposition;
complex growth diagnostics supplement the uniform proof above.

Fresh replay: PASS six original physical source families N=5,...,10,
each with five genuine boxes, retained color deficits, all E/F/R
normalizations and the full marked transfer. The same packet is
independently evaluated by the full physical pivotal trace and the
Hermite coefficient-residue functional. Its low-index and RP
residuals are checked as exact separate source terms. Four further
canonical complex-color families verify separate exact evenness and
the unchanged derivative source. These diagnostics do not establish
an exponential estimate from finite samples; bounds (5),(7) follow
from the proofs above.
