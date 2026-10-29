# A geometric supporting-plane bound for positive factorial energies with charge defects

28 October 2026. Complete positive geometry gives a quantitative
upper certificate for the angle-factorial model even when the edge
charges are not exact. Bounded integer edge defects cost only a
polynomial factor. Sublinear defects preserve the sharp volume
exponent. There is also a uniform Gaussian deficit away from the
complete angle point.

This is a statement about the positive angle energy, with its
specified normalization. It does not identify that energy with the
original Kashaev period. In particular, the exact scalar in the
original star--triangle identity is a FULL binomial, whereas the
one-tetrahedron energy amplitude is its square root after division
by N. Section 5 records that compulsory normalization distinction.

## 1. The complete geometric supporting plane

Fix a finite complete positive ideal triangulation T with t
tetrahedra. Let x* be its angle vector in units of pi, and put

    mu=min_i x*_i>0,
    V(x)=sum_i Lambda(pi*x_i),
    Lambda'(theta)=-log(2sin theta).

Let A be the tetrahedral sum matrix and E the global edge-angle
incidence matrix. Thus

    A x*=1, E x*=2*1, V(x*)=Vol(M).                (1)

No peripheral equation is required for the following upper bound.
One may impose additional exact peripheral restrictions on the
same angle variables; that only restricts the set being bounded.
There is no claim that a modular peripheral condition becomes exact.

Define the full coordinate gradient

    g_i=-pi*log(2sin(pi*x*_i)).

There are FIXED real vectors lambda,eta such that

    g=A^t lambda+E^t eta.                         (2)

Indeed, complete geometric gluing is stationary for volume on
the angle slice Ax=1,Ex=2. One direct check uses fixed cusp
horospheres and ideal Schlaefli: a tangent v with Av=Ev=0 has
dV(v)=-(pi/2)sum_e ell_e(Ev)_e=0, with the SAME truncated global
edge length ell_e on all incident tetrahedra. Hence g annihilates
ker(A,E), and elementary real linear algebra proves (2). Equivalently
one can fix a row basis of (A,E), solve (2) once, and retain that
certificate. Row dependencies make the certificate nonunique but
do not change its pairing with a consistent charge defect.

For EVERY weak local angle point x>=0 with Ax=1,

    V(x)<=Vol(M)+eta dot(Ex-2)
                      -c_*||x-x*||_2²,
    c_*=pi³*mu/64>0.                             (3)

Thus the supporting-plane linear terms telescope exactly into
the integral edge defects. They are not independent per-tetrahedron
errors and do not require estimating a different critical branch.

## 2. An explicit global quadratic deficit

Here is a proof of the constant in(3), including boundary points.
For one tetrahedron use independent coordinates x1,x2 and
x3=1-x1-x2. Its negative Hessian is

    pi² [[cot(pi*x1)+cot(pi*x3), cot(pi*x3)],
         [cot(pi*x3), cot(pi*x2)+cot(pi*x3)]].       (4)

Its determinant is pi^4, by the cotangent addition identity,
and it is positive definite in the strict simplex. Along the
FIRST HALF of the segment x_s=(1-s)x*+s x, every coordinate is
at least mu/2 and at most1-mu. Consequently each cotangent has
absolute value at most2/(pi*mu), so the trace of(4) is at most
8pi/mu. Its least eigenvalue is therefore at least pi³*mu/8.

For a tetrahedral tangent v=(v1,v2,-v1-v2),
||v||_3²<=3(v1²+v2²). Thus its second derivative on that
half-segment is at most -(pi³*mu/24)||v||_3². Integrate the
Taylor remainder with weight1-s over0<=s<=1/2. Since the
remaining part of the segment has nonpositive second derivative,

    V(x*)+g dot(x-x*)-V(x)
                 >=(pi³*mu/64)||x-x*||².          (5)

For a boundary endpoint, apply the argument before reaching the
endpoint and then use continuity of Lambda. Summing over tetrahedra
gives(5) for the whole vector. Substitution of(2) and Ax=Ax*=1
proves(3). Global uniform strong concavity of the Hessian at every
boundary point is NOT assumed; integrating its controlled first
half is what gives the global deficit from the fixed interior x*.

## 3. The actual factorial weights and bounded edge-charge errors

Use precisely

    s_N(k)=product_(r=1)^k 2sin(pi*r/N),
    w_N(k)=product_i s_N(k_i)^(-1), 0<=k_i<N.

The uniform estimate, including k=0 and N-1, is

    log s_N(k)=-(N/pi)Lambda(pi*k/N)+O(log N).      (6)

For an explicit elementary error bound write
log(2sin pi*x)=log x+log(1-x)+h(x), where h is smooth on[0,1].
The increasing log term has sum-integral error between0 and
logN+1, the decreasing log term has absolute error at mostlogN,
and h contributes at most its fixed total variation. Thus the
constant in(6) is universal. In a fixed triangulation all weight
errors are bounded by C_t logN+C'_t.

Suppose A k=N*1 and let

    delta=E k-2N*1.

Combining(3),(6) gives the finite-N Gaussian majorant

    w_N(k)<=C N^C_t exp[
       N Vol(M)/pi+eta dot(delta)/pi
          -c_*||k-Nx*||²/(pi*N)].                 (7)

All original zero-angle weights are retained. In particular, for
ANY set of such configurations with ||delta||_infty<=R_N,

    sum w_N(k)<=C N^C_t
       exp[N Vol(M)/pi+||eta||_1 R_N/pi].          (8)

The number of configurations is at most N^(3t) and has been
absorbed in the fixed polynomial. Thus O(1) edge defects cost
only a polynomial factor; R_N=o(N) preserves the sharp geometric
upper exponent. Exact full2N edge charge is sufficient but is NOT
necessary for this positive-energy estimate.

Here delta is the TRUE INTEGER difference E k-2N, not a distance
between residues modulo2N. A bounded change of a residue need
not give a bounded integer defect: for example the affine residue
2d changes to0 after adding only2, and0 permits zero or multiple
edge windings. Thus robustness under bounded integer defects does
not justify replacing the actual compatible quantum edge character
by a nearby one. The source still has to supply the stated lift
or an independent bound on its true supported defects.

If ||k/N-x*||>=epsilon, the same sum has the extra factor
exp[-N c_*epsilon²/pi]. More quantitatively a radius squared
larger than a fixed multiple of(R_N+logN)/N controls the Gaussian
tail relative to the complete geometric exponential rate. This
is a consequence of the support-plane certificate, not a phase
selection or an assertion about the original quantum cycle.

The useful condition is even weaker than small defects in every
edge: equation(7) controls any supported defect set for which
sup eta dot(delta)=o(N), with the Gaussian deficit still retained.

## 4. Affine charge d=N-1 and further bounded local offsets

For the source-compatible tetrahedral charge A k=d*1, set y=k/d
and delta_d=E k-2d*1. Then Ay=1 and Ey-2=delta_d/d. Equation(3)
applies exactly to y. The arguments k_i/N and k_i/d differ by
at most1/N. Integrating the two logarithmic endpoint singularities
of Lambda gives the uniform modulus

    |Lambda(u)-Lambda(v)|
      <=C |u-v|(1+|log|u-v||).

It contributes only O(logN) to the logarithm of the weight.
Therefore the affine version of(7) is

    w_N(k)<=C N^C_t exp[
       N Vol(M)/pi+(N/(pi*d)) eta dot(delta_d)
         -(c_*N/(pi*d²))||k-dx*||²].               (9)

Bounded or sublinear edge defects have the same conclusions as
in(8), since N/d<=2 for N>=2. This retains flat tetrahedra and
does not rely on endpoint vanishing.

More generally let the local sums be N+u_j, |u_j|<=U_N<N/2,
and normalize each tetrahedral triple by its own local sum.
The normalized edge defects differ from delta/N by O(U_N/N),
with constants determined by the fixed incidence matrix. The
factorial action changes by at most

    C_t U_N[1+log(N/max(1,U_N))].                 (10)

Hence bounded local AND edge charge offsets still cost only a
polynomial, and sublinear offsets still cost exp(o(N)). The
Gaussian deficit in the normalized local angles remains valid.
This extension requires the specified nonnegative angle support;
it does not extend a factorial through a forbidden index N.

On a common allowed nonempty progression, the strict geometric
partition satisfies Z_N(T)>=N^(-C)exp[N Vol(M)/pi] by rounding
the complete strict point in its integer kernel. Consequently
the bounded-defect positive energies above are at most a fixed
polynomial times Z_N(T); the sublinear-defect energies are at
most exp(o(N))Z_N(T).

### 4.1 A bounded-defect comparison exists at EVERY level

There is no lattice-progression obstruction for a sufficiently wide
FIXED integer defect window. Put B=2 max_e sum_i E_(e,i), determined
solely by the fixed edge incidence matrix, and define

    Z_N^B=sum_{k>=0, A k=d*1, ||E k-2d*1||_infty<=B} w_N(k).

Then this sum is nonempty for every N>=2, and fixed constants give

    C^-1 N^-C exp[N Vol(M)/pi]
      <= Z_N^B <= C N^C exp[N Vol(M)/pi].          (10a)

For nonemptiness, in each complete tetrahedral triple set
k_1=floor(d x*_1), k_2=floor(d x*_2), k_3=d-k_1-k_2.
All entries lie in[0,d]. Their errors relative to d x* lie in
(-1,0] for the first two and [0,2) for the third. Hence every
edge defect has absolute value at most B. This constructs an
admissible state at each N, without a rationality assumption on x*.
For large N it is strictly positive and k/N=x*+O(1/N). Smoothness
of the coordinate Lobachevsky sum near x* and (6) give a single
weight exp[N Vol(M)/pi+O(logN)], proving the lower bound.
The upper bound is (9) summed with the fixed defect bound B.
Increasing C handles the finitely many remaining levels.

Thus this bounded-defect positive model has the desired energy
rate at all levels, independently of any exact-fiber progression.
It may be used as an upper comparison target. Its polynomial
two-sided estimate still proves nothing about K_N until an exact
original-source comparison is established; neither nonemptiness nor
rounding constructs that comparison or enforces the true edge lift.

## 5. The exact affine local weight is not its amplitude square root

There is a particularly direct connection to the original charged
star. If a+b+c=d, root reflection gives

    w_N(a,b,c)=1/[s_N(a)s_N(b)s_N(c)]
                =|[a+b choose a]_Q|/N.           (11)

The exact ORIGINAL source-preserving balanced star--triangle
identity in [the general fusion theorem](actual_general_flow_fusion.md)
has scalar modulus |[a+b choose a]_Q|, with its full phase and
typed outer factors retained. It is the FULL binomial, namely
N w_N, not the normalized energy amplitude sqrt(w_N).

For example at a=b=c=d/3, N=1 modulo3, the scalar divided by
sqrt(w_N) has modulus

    sqrt(N*|[a+b choose a]_Q|),
    log of this ratio=N v_3/(2pi)+O(logN).          (12)

Here v_3=3Lambda(pi/3) is the regular ideal tetrahedron volume.
Thus a uniform local one-tetrahedron comparison which simply
replaces this scalar by sqrt(w_N) pays an exponential cost.
Two-tetrahedron assignments, a genuinely different doubled
contraction, or the exact exponentially varying internal gauges
could compensate it. Their compensation at the ORIGINAL full
source has to be proved; it cannot be inferred from the factorial
identity(11) or absorbed into an unknown knot normalization.

This warning does not disprove the requested upper comparison.
It keeps its amplitude/energy and source normalizations explicit.
The subsequent [exact length-frame calculation](actual_length_normalized_star_gram.md)
now supplies a constructive compensation: b_L=N^(1/4)B_L/sqrt(s_L)
makes a balanced star scalar N^(-1/2) times its retained phase,
and parallel fusion produces a polynomial times sqrt(w_N). The
[original singleton clock co-source](actual_length_gauge_clock_source.md)
also has polynomial norm in that frame. Thus the flat-frame ratio
in (12) is not an obstruction to a properly transported metric.
The compulsory dual anchor weights and the coherent global state
norm remain; [every diagonal clock metric fails the sharp budget
in an actual complete figure-eight sector](actual_figure_eight_clock_gram_obstruction.md).
The supporting-plane theorem supplies a general geometric bound
once a suitable positive angle energy with small charge defects
has actually been obtained from the source. It does not construct
that source map or bound the norm of an unproved one.

## 6. Reproduction and scope

```sh
python3 experiments/audit_positive_angle_supporting_plane.py
```

The audit uses the irregular complete three-tetrahedron shape point,
solves the nontrivial edge supporting-plane certificate, tests the
explicit global quadratic deficit including boundary triples,
checks factorial estimates with charge defects, and verifies(11).
The uniform proof is(2)--(10), not the numerical tests. No broad
original Kashaev upper bound or geometric survival is asserted.

For coverage only, the classical optimization framework is recorded
in [Rivin, Combinatorial optimization in geometry](https://arxiv.org/abs/math/9907032)
and [Futer--Gueritaud, From angled triangulations to hyperbolic structures](https://arxiv.org/abs/1004.0440).
The latter abstract explicitly describes the volume critical-point
method on an angle polytope. Only those abstracts were consulted
for coverage here; no proof or technique from either paper is an
input to the supporting-plane, deficit, or finite-factorial arguments.
