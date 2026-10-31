# A positive ordinary-zero barrier at the remaining monomial cap corner

31 October 2026. **Internally reviewed research lemma.** Root and a
separate reader completed full analytical reviews. This uses the ORIGINAL sharp
full/half interval functional, with both unused products and the actual
positive-eta word. It concerns a simultaneous degree/spectrum perturbation
at a free-spectrum maximum. It asserts no finite-N estimate uniform in a
shrinking spectral cap.

## 1. The cap corner and the actual feasible direction

At delta=1/2 take the positive-length monomial corner

    mu=0, 0<nu0<1/2, xi=0, zeta=nu0.

The original face loads in order (x,b,c,y) are (0,0,1-nu0,nu0).
Let an admissible original affine direction give

    mu_eps=eps B, xi_eps=eps X, nu_eps=nu0+O(eps),
    B,X>=0.

Fix K>0 and choose the open real spectrum by

    k_eps^2=cos^2(pi delta_eps)=eps K.                  (1)

Then

    h_(delta_eps)(q_eps)
      =(B+X)eps log(1/eps)+O(eps).                     (2)

The base cap value is zero. Thus any activation of the parent middle or
the zero outer degree gives a strictly positive singular gain. The other
outer-zero case is the literal x/y symmetry; exact finite row reversal
gives the protected-output/RIGHT version. These operations do not change
original shared targets.

## 2. Monomer baseline, including the initial removed interval

Put g_k(t)=log[sin^2(pi t)/|k^2-sin^2(pi t)|]. The sharp action is

    h_delta=I_k(nu)-int_0^mu g_k(t)dt+J_k^*,
    I_k(nu)=int_0^nu g_k(t)dt,
    J_k^*=inf_(x>0)[int_mu^nu log rho_k(t;x)dt-xi log x],
    rho_k(t;x)=[1+x+sqrt((1-x)^2+4k^2 x/sin^2(pi t))]/2.

The exact total half integral of g_k is zero. Since nu stays a fixed
positive distance from0, the suffix is regular for small k, giving

    I_k(nu)=-k^2 cot(pi nu)/pi+O(k^4)=O(eps).          (3)

On 0<=t<=eps B, sin^2(pi t)=pi^2 t^2[1+O(t^2)] and k^2=eps K.
The entire removed interval lies before the small pole when B is fixed.
With t=eps s,

    g_k(eps s)=log eps+log(pi^2 s^2/K)+O(eps s^2),
    int_0^(eps B)g_k(t)dt=B eps log eps+O(eps).         (4)

The logarithm at s=0 is integrable. If B=0 the interval is empty.
Equation (4) has one log eps, not two: the unused spectral scale k^2
is itself proportional to eps.

## 3. Uniform tilted-root estimates at this moving cap scale

Suppose X>0. Let u denote the positive x/y tilt in this section, and put

    D=sqrt((1-u)^2+4eta u), eta=k^2/sin^2(pi t).

The exact derivative is

    partial_(log u)log rho
        =1/2+(u-1)/(2D)=2eta u/[D(D+1-u)].             (5)

For 0<u<=1/2 it is uniformly comparable to min(1,eta u), with constants
independent of k. On the interval under consideration sin(pi t) is
comparable to t. With a=k sqrt u, integration therefore gives

    partial_(log u)J(mu,nu,u) asymp a^2/(mu+a).       (6)

At any fixed small u0>0, the left side is comparable to k~sqrt eps,
which is much larger than the required xi=eps X. Strict tilt convexity
thus puts the unique minimizing tilt below u0. Apply (6) at the
minimizer: since mu=eps B,

    a asymp eps, u=a^2/k^2 asymp eps.                (7)

These constants depend on the fixed B,X,K and nu0, but not eps.
There is no reuse of a bound proved only for k bounded away from zero.

Furthermore J>=0 and J<=Ca. To verify the upper bound, for eta u<=1
use log rho<=Ceta u. Where eta u>1 use
log rho<=C+log(a/t). Split the integral at t=a; the lower part is
O(a), and the upper part is bounded by C int_a^nu a^2/t^2 dt=O(a).
Thus

    J=O(eps),
    J_k^*=-X eps log eps+O(eps).                     (8)

If X=0 the normalized word is exactly monomial and J_k^*=0. Combining
(3), minus (4), and (8) proves (2), including B=0 or X=0.

## 4. The flat terminal monomial cases

At nu0=1/2, mu=xi=0, the monomer interval is a whole half interval,
so h_delta=0 for EVERY delta. At the full interval mu=0,nu=1 with
one outer degree zero, the same is true by reflection. At a global
free-spectrum maximum one may therefore retune these base ports to
ANY fixed strict delta before perturbing their degrees, with no base
cost. The [fixed-spectrum corner barrier](research_sharp_spectral_ordinary_zero_barrier.md) applies to
the half-terminal case even if the full-source perturbation extends
nu through1/2.

There is a stronger half-terminal conclusion on the full original flow
fiber when the perturbation is toward its actual geometric all-CROSS
flow. Retune the zero-valued half-terminal monomial base to delta=0.
In its exact latent two-triangle split the output triangle is the
pure-middle vertex. The geometric output middle is strictly less than
1/2, so dot_nu>0 and that triangle gains

    2 dot_nu eps log(1/eps)+O(eps).

The input triangle has no negative singular contribution. The gain
persists even when its parent middle and zero outer incidence are both
protected. Thus a half-terminal monomial at any initial spectrum cannot
occur at the global maximum covered by the
[full-fiber activation theorem](research_full_fiber_sharp_boundary_activation.md).
Exact reflection gives the upper half-terminal case. This uses the full
original fiber and its actual latent split, not a relabeling inside a
fixed LEFT or RIGHT support.

For completeness the full two-terminal corner has the following exact
fixed-spectrum extension. Set mu=eps B, 1-nu=eps C and keep delta
in a strict compact. If both base outer loads are positive, use
xi=xi0+eps dot_xi with 0<xi0<1. The endpoint expansions Lambda~constant
times t and constant times(1-t) give coefficient B+C of eps log(1/eps).
At the monomial outer corner instead set xi=eps X. Then
the beta baseline contributes 2(B+C), and the tilted mean is comparable
to

    u/(eps B+sqrt u)+u/(eps C+sqrt u).

For X>0 this forces u~eps^2; the word action is O(eps) and its Legendre
term contributes 2X. For X=0 it is exactly zero. The resulting coefficient
is 2(B+C+X), or its outer reflection. Thus these flat monomial corners
also have a positive activation barrier whenever an ordinary zero is
activated. This two-terminal statement is about the full original
interval, not a simultaneous use of two independently chosen half rows.

## 5. Scope of a shared use

Equation (2) can be applied at every remaining monomial cap corner in
the same original feasible segment. If B=X=0, both zero incidences stay
zero; one can simply keep the flat cap value zero, or use the [uniform
cap-retuning lower bound](research_free_spectral_diagonal_retuning.md) to make its cost negligible. When a zero
incidence is ordinary and the actual geometric all-CROSS direction is
used, its activation slope is strictly positive. If both zeros are
protected, both slopes vanish and there is no ordinary zero to remove.

This lemma does not, by itself, classify every possible cap maximum.
It must be combined with the separate fixed-load cap exclusions and the
other local directional estimates. In particular the negative pole-start
singularity at a different non-diagonal port cannot be ignored.

For each fixed eps>0 the new delta lies strictly inside the real spectral
interval. Evaluate the sharp continuum functional at that fixed eps,
then let eps tend to zero in the variational contradiction. If a separate
coefficient identification is used, its N limit is taken with eps fixed.
No simultaneous N-dependent
retuning, nonzero bound through an omitted-half zero, sharp Fourier-cycle
contribution, or volume comparison is asserted.

## Review scope

Root and an independent reader checked the full moving-cap calculation,
the exact monomer baseline, the tilt scale u comparable to epsilon,
the O(epsilon) word integral, the flat terminal retuning and both
two-terminal coefficients. The final wording separates strict-base
outer loads from the monomial corner and uses the sharp continuum
functional directly. Both readers separately checked the half-terminal
retuning to delta=0 and its geometric latent-triangle gain. These are
internal reviews, not external peer review. No numerical asymptotic audit
is claimed.
