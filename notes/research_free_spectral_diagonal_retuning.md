# Free spectral retuning removes the negative diagonal singularity

Retuning applies to a global maximum with freely varying spectra. It is not a statement about fixed-spectrum local maxima or a uniform finite-$N$ estimate in a shrinking cap neighborhood.

## 1. A uniform lower bound from one exact word

Put k=cos(pi delta), 0<delta<1/2, and

    alpha_k(t)=4[k^2-sin^2(pi t)], beta(t)=4sin^2(pi t),
    eta_k(t)=k^2/sin^2(pi t),
    rho_k(t;x)=[1+x+sqrt((1-x)^2+4eta_k(t)x)]/2.

For 0<=mu<=nu<=1/2 and 0<=xi<=w=nu-mu, the exact sharp LEFT
functional is

    h_delta=B_delta+int_mu^nu log beta+J^*,
    B_delta=int_0^mu log|alpha_k|+int_nu^(1/2) log|alpha_k|,
    J^*=inf_(x>0){int_mu^nu log rho_k(t;x)dt-xi log x}. (1)

The [normalized positive-eta word](research_positive_eta_word_transfer.md)
has, for EVERY outer degree, a
monotone word x^K y^(r-K) with no y-to-x transition. Its coefficient
is exactly one. This is why its coefficient entropy is nonnegative.
Directly in (1), rho_k>=max(1,x), so, for 0<=xi<=w,

    int_mu^nu log rho_k-xi log x>=0,
    J^*>=0.                                             (2)

This includes both extreme outer loads and w=0. It uses the actual
word normalization; no missing sine or outside-row factor is discarded.

The full unused-row integral satisfies the exact identity

    int_0^(1/2) log|alpha_k(t)|dt=0.                      (3)

Indeed alpha=4cos(pi(t+delta))cos(pi(t-delta)). The two translated
log-cosine integrals have sum independent of delta, since their upper
endpoint derivatives agree by reflection about 1/2; at delta=0 the
sum is zero. The integrable endpoint and interior logarithms justify
continuation to the closed delta interval. Consequently

    h_delta>=int_mu^nu g_k(t)dt,
    g_k(t)=log[sin^2(pi t)/|k^2-sin^2(pi t)|].             (4)

There is an elementary UNIFORM bound for its negative part. The
integrand is negative only when sin^2(pi t)<k^2/2. On [0,1/2],
sin(pi t)>=2t, so this set lies inside [0,k/2], and there

    (-g_k(t))_+ <= 2 log[k/(2t)].

Extend this positive upper bound to [0,k/2] and integrate:

    int_0^(1/2) (-g_k)_+ dt <=
           int_0^(k/2) 2log[k/(2t)]dt=k.

Thus, simultaneously for ALL closed degree vectors,

    h_delta(mu,nu,xi)>=-k=-cos(pi delta).                 (5)

The reflected RIGHT functional has the same bound. For full-row
intervals 0<=mu<=nu<=1, use both outside intervals on [0,1].
Reflection t->1-t doubles (3) and the negative-part estimate, yielding

    h_delta^full(mu,nu,xi)>=-2k.                          (6)

The constants in (5)--(6) do not depend on the interval or outer
proportion. In particular no strict outer-degree condition is hidden.

For clarity, the continuous cap functional is identically zero:
at k=0, alpha=-beta and rho_0=max(1,x), so h_(1/2)=0 at every degree.
This also is a uniform limit of the open-spectral functional. For
small k the L1 norm of g_k is O(k): set s=sin(pi t)/k near t=0;
log[s^2/|1-s^2|] is integrable on bounded s intervals. Above s=2,
|g_k|<=C k^2 csc^2(pi t), whose integral from arcsin(2k)/pi to
1/2 is O(k). The reflected endpoint is the same. Also

    0<=J^*<=J(x=1)
      <=int_0^(1/2) log(1+k/(2t))dt
      =[(1+k)log(1+k)-k log k]/2

on a half interval, and at most twice this on a full interval.
Thus |h_delta|<=C k log(1/k) uniformly as k decreases to zero.
The main lower bound (5) is sharper in the direction needed below.

## 2. Retuning a diagonal along any admissible opening

At a diagonal mu=nu=a, xi=0, (3) implies

    h_delta(a,a,0)=0 FOR EVERY delta.                     (7)

Let q(eps) be any feasible opening, with the original face loads
unchanged globally. At this port its interval and outer split may be
arbitrary admissible functions of eps. Choose the open real spectrum

    delta_eps=arccos(eps^2)/pi.

Then (5)--(7) give

    h_(delta_eps)(q(eps))-h_delta(q(0))>=-eps^2           (8)

for LEFT/RIGHT, and >=-2eps^2 for full rows. This holds uniformly
in all closed outer loads, including monomial openings, every diagonal
center, and variable interval lengths. In particular there is no
negative eps log(1/eps) contribution after this allowed retuning.

Equation (8) compares different spectra at the perturbed point. It
is not a continuity assertion at the old fixed delta. Because the
initial diagonal value is independent of delta, this change incurs no
baseline loss at a GLOBAL free-spectrum maximum. It need not remain
in an arbitrarily small neighborhood of the old spectral parameter,
so it does not exclude a local fixed-spectrum maximum.

## 3. Stronger gains for interior diagonal centers

The uniform cap choice already suffices to neutralize every diagonal.
For an affine opening at a fixed center a in (0,1), write

    mu_eps=a+eps B, nu_eps=a+eps C,
    w_eps=eps W, W=C-B>0,
    0<=xi_eps<=eps W.

If a!=1/2, place a simple alpha pole at the interval midpoint,
using delta_eps=|1/2-(mu_eps+nu_eps)/2|. The chosen spectrum stays
in a fixed strict real compact when a stays away from 0,1/2,1.
Throughout the interval beta is bounded below, and
|alpha_(delta_eps)(t)|<=C eps. By (2)--(4),

    h_(delta_eps)(q(eps))>=
                    W eps log(1/eps)-C eps.              (9)

The pole's logarithm is integrable. No division by the sampled finite
alpha factors is made. The lower bound is uniform in the entire closed
outer split; it uses only J^*>=0, not a bounded minimizing tilt.

At a=1/2, choose delta_eps=eps D with any fixed D>0.
Then |alpha_(delta_eps)(t)|<=C eps^2 on the interval and beta
stays bounded below. Therefore

    h_(delta_eps)(q(eps))>=
                    2W eps log(1/eps)-C eps.             (10)

No placement of both small poles inside the interval is necessary:
their common quadratic scaling is enough. This covers a lower-half
terminal diagonal by restricting its admissible opening to that half.
At a=0 or1 the bound (8) is used instead; the fixed-spectrum negative
monomer singularity from the [ordinary-zero barrier note](research_sharp_spectral_ordinary_zero_barrier.md)
is not retained.
If W=0, the port stays diagonal and (7) applies exactly.

## 4. A global activation lemma with diagonal ports allowed

Consider the actual shared feasible flow fiber. Its face constraints
do not involve the independently free real spectra. Let (q,delta) be
a GLOBAL maximum of the sum of the specified sharp local entropies.
Separate the ports into:

* non-diagonal regular intervals covered by the [ordinary-zero barrier
  lemma](research_sharp_spectral_ordinary_zero_barrier.md), including its
  terminal-row calculus extension, at their fixed strict spectral parameters;
* arbitrary diagonal intervals, at any initially allowed spectra;
* any other terms whose change in the proposed common-target direction
  has no negative eps log(1/eps) term and an O(eps) remainder.

Suppose an actual feasible segment q(eps) activates a removable
ordinary zero at a regular port. Keep every regular spectrum fixed.
Retune ONLY the diagonal-port spectra by (8), or by (9)--(10) if a
positive interior opening is useful. The regular terms have a strictly
positive total coefficient b of eps log(1/eps), all other regular
singular coefficients are nonnegative, and every diagonal costs at
most O(eps^2). For a fixed finite diagram,

    sum h_new - sum h_old
               >=b eps log(1/eps)-C eps-C'eps^2>0,

contradicting global maximality. Thus diagonal ports do not obstruct
the prior regular ordinary-zero exclusion when their spectra truly
are free over the original real interval.

Likewise, a feasible positive opening of an interior diagonal gives a
strict gain by (9) or (10), provided all other affected terms satisfy
the stated nonnegative-singularity conditions. Row-zero/row-one
diagonals alone receive only the neutral bound; this does not exclude
all such vertices or all structural identity strata.

The finite Hall/residual-cycle test from the ordinary-zero barrier
note still decides whether an incidence can be activated in the
original fiber. No larger fractional network, projected cover, or
independent local reassignment is substituted. Pole-touching non-diagonal
rows can still have a negative singular term and remain outside this
global lemma unless separately controlled.

## 5. Order of limits and source scope

These are exact inequalities for the sharp continuum functional, with
the original degree constraints and unused-product normalization.
For each fixed eps>0, delta_eps is strictly between0 and1/2; only then
is N sent to infinity. The subsequent eps->0 argument is a finite-
dimensional variational contradiction. It asserts no uniform finite-N
coefficient asymptotic when cos(pi delta) is comparable to N^-1,
no nonzero lower bound through a sampled omitted-half zero, and no
simultaneous eps_N or delta_N limit. Exact common scalar zeros and
their spectral phases remain part of any later source reconstruction.

As before, the argument is a calculus theorem for the sharp upper
functional, and applies to a genuine source entropy only where its
coefficient identification has been established. It does not identify
the rate of a signed sum of central CROSS paths, construct a volume
representation, or prove a universal complete-volume comparison.

## Scope

Root and an independent reader checked the complete argument, including
the exact half/full normalizations, the constants one and two in the
uniform lower bound, closed outer loads, cap continuity, both interior
diagonal gains, and the global feasible-direction consequence. The
fixed-perturbation-before-level limit is essential. No finite-level cap
asymptotic, source-period lower bound or universal volume comparison is
claimed, and no numerical audit is used as a substitute for the proof.
