# Joint saddle and global gap of the actual trivalent scalar

29 October 2026. The historical filename is retained, but the actual
scalar identification is now PROVED by the independent
[finite Euler-to-Racah transform](finite_trivalent_euler_racah_transform.md).
This note proves its joint asymptotic and extremal geometry, including
the required nonconstant source normalizer and explicit source phase.
These are actual black-SCALAR estimates; full magnetic tensors,
white/marked sewing and graph geometry remain separate.

## 1. Exact finite partition and symmetric reflection

Let N>=2, d=N-1, s_a=product_(r=1)^a 2sin(pi r/N). For integer
0<=j_i<=floor(d/2), put J=j_1+j_2+j_3. The positive partition is

    R_N(j)=N sum_(max j_i<=t<=min pair sums)
      s_t/[prod_i s_(t-j_i) s_(d+t-J)
                                prod_i s_(J-j_i-t)]. (1)

An empty range means zero. All indices in a nonempty range lie in
0,...,d: in particular J-t<=min pair sums<=d. The exact original
sine-factorial reflection s_a s_(d-a)=N rewrites (1) as

    R_N(j)=sum_t s_t s_(J-t)
                  /[prod_i s_(t-j_i)s_(J-j_i-t)].     (2)

Every term is positive and (2) is EXACTLY invariant under t->J-t.
It works at both level parities, including all endpoint indices.

## 2. Unique joint saddle

Write L(x)=integral_0^x log(2sin pi u)du, a_i=j_i/N, S=sum a_i,
and use z=t/N as the summation variable. The uniform physical
sine-factorial error O(log N) gives the limiting summand phase

    E(z,a)=L(z)+L(S-z)
              -sum_i[L(z-a_i)+L(S-a_i-z)].           (3)

The support is max a_i<=z<=S-max a_i. In its nondegenerate interior
p_i=z-a_i and q_i=S-a_i-z lie in (0,1/2); each p_i<=z and each
q_i<=S-z. Consequently

    E_zz=pi[(cot(pi z)-sum cot(pi p_i))
                    +(cot(pi(S-z))-sum cot(pi q_i))]<0. (4)

For either parent angle, a nonnegative parent cotangent is smaller
than each of its three child cotangents; a negative parent is already
smaller than their positive sum. This proves (4), not just its value
at a stationary point. Symmetry in (2) therefore gives the UNIQUE
saddle z_*=S/2. The one-sided phase derivatives are respectively
+infinity and -infinity at nondegenerate support endpoints.

Put

    r_i=S/2-a_i, i=1,2,3; r_4=1-S/2.

For admissible triangles r_i>=0, r_4>=1/4 and sum r_i=1. The exact
candidate rate is

    Phi(a)=2[L(S/2)-sum_(i=1)^3 L(r_i)]
           =(2/pi)sum_(i=1)^4 Lambda(pi r_i).         (5)

The uniform O(log N) factorial estimate and at most N summands show
log R_N=N Phi(a)+O(log N) uniformly on ADMISSIBLE physical triples
with nonempty summation range; nonadmissible triples have R_N=0.
For a lower
bound choose a nearest physical t to J/2. This includes degenerate
triangles by the same uniform factorial estimate and continuity.

## 3. Strict global maximum and all-color gap

The function sum_(i=1)^4 Lambda(theta_i) is STRICTLY concave on
theta_i>0, sum theta_i=pi. Its negative Hessian on that tangent
space is sum cot(theta_i)v_i^2. If all angles<=pi/2, positivity is
immediate. Otherwise let theta_4>pi/2, so A=sum_(i<=3)theta_i<pi/2.
Weighted Cauchy and sum_(i<=3)tan theta_i<tan A give

    sum_(i<=3)cot(theta_i)v_i^2
       >=v_4^2/[sum_(i<=3)tan theta_i]>cot(A)v_4^2
                                              =-cot(theta_4)v_4^2.

The case v_4=0 is strictly positive unless all v_i=0. This proves
strict concavity throughout the simplex. Symmetry then fixes its
unique maximum at all theta_i=pi/4. Boundary continuity and the
strict line inequality exclude a second boundary maximum.

It follows that (5) has unique maximum

    a_1=a_2=a_3=1/2,
    Phi_max=8 Lambda(pi/4)/pi=v8/pi=:j0.              (6)

Thus R_N<=poly(N)exp(Nj0). For EVERY delta>0 there is gamma_delta>0
such that a physical admissible triple with max_i(1/2-a_i)>=delta
has R_N<=poly(N)exp[N(j0-gamma_delta)]. This is an ENTIRE triple
color gap, rather than three separately maximized envelopes. No
angle-edge gluing of a full graph has been inferred from (5).

## 4. Exact central complex packet and its amplitude

Allow both parities by writing m=d/2, which can be a half-integer,
and j_i=m-N sigma_i. Physical j_i are still integers. Around sigma=0
fix a summation window I_N near t/N=3/4. With S_hat_N the canonical
sine-factorial completion, define the EXACT function

    Rwin_N(sigma)=sum_(t in I_N)
       S_hat_N(t)S_hat_N(sum j_i-t)
       /[prod_i S_hat_N(t-j_i)S_hat_N(sum j_i-j_i-t)]. (7)

All scaled arguments lie in compact zero-free bulk strips. On a
fixed small complex sigma polydisk it is holomorphic. At physical
sigma it is literally the retained part of (2); all other terms
have a strict exponential gap uniform in a smaller physical
corridor. Equation (7) does not choose a moving-q normal germ.

For the analytic limiting phase use a_i^0=1/2-sigma_i,
R_0=sum a_i^0/2 and r_i=R_0-a_i^0, r_4=1-R_0 in (5).
The saddle is still z=R_0, up to its actual half-step shift. Put
D=sum_(i<=3)cot(pi r_i)-cot(pi R_0)>0. The negative Hessian is
2pi D. The compact sine-factorial expansion in (7), before its
half-step shift is included, has saddle prefactor

    sin(pi R_0)/[4N^2 prod sin(pi r_i)].

The actual j_i=N a_i^0-1/2 changes each r_i by -1/(4N) and R_0
by -3/(4N). Its exponential constant is therefore
exp[-3G(R_0)/2+sum_i G(r_i)/2], G=L'. Combining these and the
Gaussian integral gives

    Rwin_N(sigma)=N^(-3/2)exp[N Phi(sigma)]
        /[4sqrt(prod_i cos(pi sigma_i))] *[1+O(1/N)]. (8)

The useful elementary identity is

    sin(pi R_0)prod_i sin(pi r_i) D
       =prod_(i<k)sin(pi(r_i+r_k))
       =prod_i sin(pi a_i^0).

It proves the amplitude in (8), including its factor 1/4. The square
root is +1 at zero. This also proves the amplitude for even physical
nearest-center labels, whose sigma_i are half-integral multiples of
1/N; there is no guessed parity factor.

For complex uniformity apply the exact pi N cot(pi N z) rectangle
to the fixed physical t window, with half-grid endpoints. On its
vertical sides |cot|<=1 and the endpoint phase has a strict gap.
On horizontal sides the error is exp(-2pi N b), while phase growth
is <=Cb^2+C||sigma||b. Choose b first small, then shrink the complex
polydisk. Keep the endpoint connectors, which remain gapped.
Deform only the main integral to its analytic saddle. The canonical
factorial remainders are holomorphic O(1/N) on a larger tube, so
ordinary analytic Gaussian integration proves (8) for the EXACT
packet, with every fixed derivative controlled by Cauchy estimates.

Its local action is explicitly

    Phi(sigma)=j0-pi sum sigma_i^2
                         +2pi^2 sigma_1 sigma_2 sigma_3+O(||sigma||^4). (9)

Indeed the four r_i are 1/4 plus the four tetrahedral sign rows
(+--),(-+-),(--+),(+++) applied to sigma/2. Their squared changes
sum to sum sigma_i^2, and their cubed changes sum to 3sigma_1sigma_2sigma_3.
Thus the exact complex window obeys a real-coercive bound
poly(N)exp[N(j0-c||Re sigma||^2+C||Im sigma||^2)]. In particular
the JOINT action is not separately even, although each one-leg
restriction is even. Internal pair-Casimir labels are not thereby
identified with ordinary auxiliary colors or peripheral meridians.

## 5. The actual source normalizer and its nonconstant action

The proved original scalar, in the actual highest-column convention, is

    A_N=(-1)^(N+J)q^[2j_1^2-j_1j_2-j_1j_3+j_2j_3-J-3]
                                             C_N(j)R_N(j),

    delta=J-d>=0,
    C_N(j)=prod_i s_(j_i)/[N s_delta],               (10)

and zero when J<d. The root-Fourier source theorem proves the zero
branch; the finite Euler/Sears bridge proves the positive branch,
including its displayed phase and all label orders.
Whenever a permitted j_i is incremented,

    C_N(j+e_i)/C_N(j)
       =sin[pi(j_i+1)/N]/sin[pi(delta+1)/N]>=1,

since delta<=j_i and both arguments are on the increasing half of
the sine curve. Thus its maximum is 1 at the odd central triple,
and cos(pi/N) at the even nearest-central triple (when this domain
is nonempty). Consequently the ACTUAL scalar has the same upper
envelope and strict macroscopic color gap as (6), unconditionally
on the scalar level.

This does not mean C_N can be discarded from a local packet. Its
continuous exponential action is

    Gamma(a)=sum_i L(a_i)-L(S-1).

The exact near-central factorial completion
prod_i S_hat_N(m-Nsigma_i)/[N S_hat_N(m-Nsum sigma_i)]
has the uniform bulk asymptotic exp[N Gamma(sigma)](1+O(1/N)),
with prefactor ONE: each half-shifted sine factorial contributes
sqrt(N), and their powers cancel. Therefore the fully normalized
actual scalar packet is (8) with action Phi+Gamma and the SAME
displayed amplitude, multiplied by the exact phase above. For its
analytic completion take j_i=m-Nsigma_i and use exp[pi i(N+J)]
for the displayed integer character. That known phase must be
retained separately: it is unit on physical channels and may have
linear complex-direction growth. The positive core has Hessian
-2pi I, while

    Gamma(sigma)=-(pi^2/6)[(sum sigma_i)^3-sum sigma_i^3]
                                                   +O(||sigma||^5). (11)

The actual normalizer thus changes the cubic interaction and
the Lobachevsky interpretation. Formula (5) alone is the rate of R,
not an already identified original-source volume. Since C_N<=1 on
the physical source domain, its action is nonpositive there.

## 6. Source and geometry qualification

The actual scalar now has an explicit strict concavity certificate
for its positive partition, a whole scalar-color envelope and a
nonzero complex central scalar packet with its known phase. These
claims use the proved finite source identity, rather than inferring
it from agreement of limiting actions. White and marked rows,
all magnetic T_i, ordered graph sewing and full geometric angle-edge
constraints remain additional source data. Formula (5) is a local
four-angle Lobachevsky functional, not an identification of a graph
complement or an automatic survival theorem after coherent sewing.

Audit: [finite reflection, joint saddles and complex packets](../experiments/audit_actual_trivalent_candidate_racah_partition_geometry.py).

The scalar saddle theorem and finite source identity do not imply a full-tensor geometric conclusion.