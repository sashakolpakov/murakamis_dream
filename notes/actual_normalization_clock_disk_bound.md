# A source-specific backward Ward estimate on shrinking clock disks

29 October 2026. The exact normalization packet identified in
[the original cup-slide calculation](actual_terminal_source_normalization_packet.md)
has a polynomial bound on a disk of radius 1/N about its original
clock. This controls the entire clock germ, not only its value. The
proof uses an exact backward recurrence; its contraction product
cancels the exponential size of the original factorial coefficients.

More generally the packet is subexponential on EVERY shrinking disk.
This supplies a genuine sharp, zero-exponent estimate for this actual
normalization source and for specified sublinear-frequency exterior
couplings. It does not prove the hyperbolic-volume bound for an
arbitrary braid, or a uniform bound on a different open physical head.

## 1. The original finite polynomial and its exact Ward equation

Put N>=2, d=N-1, Q=exp(2*pi*i/N), F_j=(Q;Q)_j, s_j=|F_j| and

    H_N(t)=sum_(j=0)^d F_j t^j.                            (1)

Every statement below also holds with Q replaced by its conjugate.
Since F_j=(1-Q^j)F_(j-1), and F_N=0 exactly, the polynomial satisfies

    (1-t)H_N(t)+t Q H_N(Qt)=1.                            (2)

This is an identity of the original finite function. No endpoint
remainder, coefficient, or peripheral factor has been discarded.

Let k=floor(N/6). The elementary sine sequence obeys

    min_(0<=j<N) s_j=s_k,
    s_j s_(d-j)=N,
    max_j s_j=N/s_k.                                    (3)

For the first assertion use s_j/s_(j-1)=2sin(pi*j/N): this ratio is
at most one up to N/6, at least one from N/6 to 5N/6, and then at
most one. The final value s_d=N exceeds s_0=1. Reflection follows
from F_d=N and the complementary conjugate factors, and proves the
last assertion, including ties and small N.

In particular, for any t with |t-1|<=c/N,

    |H_N(tQ^r)| <= exp(c) N^2/s_k                         (4)

for every integer r. This coarse bound uses absolute values and is
exponential by itself. The next step retains a coherent recurrence
before using it.

## 2. Exact backward propagation cancels that exponential

Iterate (2) from tQ^(-k) to t. With empty products equal to one,

 H_N(t)=sum_(r=0)^(k-1)
       (-1)^r t^(-r-1) Q^[r(r+1)/2]
       product_(j=1)^r(1-tQ^(-j))
   +(-1)^k t^(-k)Q^[k(k-1)/2]
       product_(j=1)^k(1-tQ^(-j)) H_N(tQ^(-k)).           (5)

This follows by substitution, so phases as well as moduli remain
specified. For k=0 it is simply the original polynomial.

Assume 0<c<=N/2 and |t-1|<=c/N. For 1<=j<=k,

    4j/N <= |1-Q^(-j)| <= 1,
    |1-tQ^(-j)| <= |1-Q^(-j)|+c/N.

Consequently

 product_(j=1)^k |1-tQ^(-j)|
       <=s_k product_(j=1)^k(1+c/(4j)).                  (6)

Also |t|^(-k)<=exp(c/3). For an intermediate product in the sum
of (5), its modulus is at most (1+c/N)^r<=exp(c/6). Thus the
whole forcing sum has modulus at most 2k exp(2c/3).

For b=c/4 and k>0, a decreasing-function integral estimate gives

 sum_(j=1)^k log(1+b/j)
   <=integral_0^k log(1+b/u)du
   =k log(1+b/k)+b log(1+k/b)
   <=b[1+log(1+k/b)].                                 (7)

Since k/b<=2N/(3c), the combination of (4)--(7) bounds the
remainder by

    exp(19c/12) N^2 (1+2N/(3c))^(c/4).                 (8)

The decisive cancellation is the factor s_k in (6) against 1/s_k
in (4). There is no estimated adiabatic eigenbranch or untracked
mode conversion in this first-order finite identity.

Adding the forcing sum, and treating k=0 directly by (4), proves
the uniform, all-level bound

    SUP_(|t-1|<=c/N) |H_N(t)|
       <= B_(N,c):=2 exp(2c) N^2
                              (1+2N/(3c))^(c/4),
    0<c<=N/2.                                          (9)

A simpler bound sufficient when c is fixed is

    SUP |H_N(t)| <=2 exp(2c) N^(2+c/4).                 (10)

For (10), use sum_j log(1+c/(4j))<=c H_k/4 and
H_k<=1+log(k+1), with k+1<=N, directly in (6).

At t=1 the same argument is sharper and especially elementary:

    |H_N(1)|<= k+N^2.                                  (11)

All forcing products then have modulus at most one, and (6) is
exactly s_k. Thus this independently bounds the original endpoint
sum without a spectral trace formula or a saddle argument.

## 3. Whole shrinking germs and their derivatives

If c_N=o(N), equation (9) gives

    log SUP_(|t-1|<=c_N/N) |H_N(t)|=o(N),                (12)

as an upper bound: c_N log(1+N/c_N)=o(N), and log N=o(N).
More explicitly, the logarithm is at most

    log 2+2log N+2c_N+(c_N/4)log(1+2N/(3c_N)).          (13)

For a fixed c>0, ordinary complex Cauchy on this actual holomorphic
disk gives, for EVERY integer r>=0,

    |H_N^(r)(1)|/r! <= B_(N,c) (N/c)^r.                 (14)

The bound is polynomial in N at every fixed normal order. It is
also an explicit quantitative estimate when r grows; no claim of
subexponential cost is inferred for arbitrary r=O(N).

## 4. The exact original source packet to which the theorem applies

The complete physical cup slide gives R12 R23 p=N e0. After the
specified terminal R23^2 and actual cap, its recorded rows are

    b_j=x^(-d) Q^(-j) conjugate(F_j)
       =x^(-d) Q[conjugate(F_j)-conjugate(F_(j+1))],
    x=Q^(d/2), conjugate(F_N)=0.                        (15)

Here x has its ORIGINAL mark x=q^d, q=exp(pi*i/N); the notation
Q^(d/2) retains that mark. Every full crossing scalar and source
factor in (15) is the one in the linked original-source proof.

Define Hbar_N(t)=sum_j conjugate(F_j)t^j. The exact phase-generating
function of these rows is

    f_N(t)=sum_j b_j t^j
          =x^(-d) Q[(1-t^(-1))Hbar_N(t)+t^(-1)].         (16)

Its apparent pole at zero is removable. In particular
f_N(1)=x^(-d)Q has unit modulus, whereas the full-circle packet
energy sum_j|b_j|^2=sum_j s_j^2 is exponential. Thus (9) resolves
an actual full-source normalization test that the flat packet norm
fails, not merely an arbitrary polynomial example.

On the disk of (9),

    |f_N(t)| <=2+(2c/N) B_(N,c).                        (17)

For the weighted Cayley-arc energy of
[the exact Cauchy metric](actual_shrinking_arc_cauchy_metric.md),
put t=(1+i a s)/(1-i a s), -1<=s<=1. Then |t-1|<=2a.
Choose c=2Na (for large N so that c<=N/2). Equations (12),(17)
and (1+a^2s^2)^d<=exp(Na^2) show

    log E_arc(f_N)=o(N) whenever a=a_N->0.               (18)

The equality of the exponential rate to zero also uses the exact
evaluation lower bound E_arc>=|f_N(1)|^2/kappa_d>=1/N.
For a<=C/N the upper bound is polynomial. All fixed derivatives
of f_N at one are polynomially bounded as well, by (17) and Cauchy.

The original external scalar chi_N, if used, multiplies f_N and
its squared energy by chi_N and |chi_N|^2 respectively. It remains
explicit. The raw source identity above already retains all common
crossing phases; no auxiliary positive invariant is substituted.

## 5. Precise scope of the exterior and global problem

For an exposed recorded packet with operator-valued diagonal exterior

    A_j(t)=sum_(|ell|<=D_N) A_ell(t) Q^(ell*j),

its actual contraction is sum_ell A_ell(t) f_N(tQ^ell), with the
original order of each spectator operator retained. Since

    |tQ^ell-1| <= (c_N+2pi D_N)/N,

(9),(17) give subexponential norm whenever c_N+D_N=o(N) and
sum_ell||A_ell(t)||=exp(o(N)) uniformly. Fixed degrees and fixed
polynomial spectator costs give polynomial bounds.

This is a statement about the specified exposed RECORDING slot.
It is not automatically a uniform estimate for every physical input
color of the open normalization tangle. Inserting physical raising
or lowering operators can expose a different two-color packet and
requires its literal source calculation. Likewise a general original
crossing has degree N-1 in the adjacent observable; it is not a
sublinear-frequency perturbation covered by this result.

For a general exterior sequence A_j the exact Ward equation instead
retains the forcing term

 (1-t)H_A(t)+t Q^(-1)H_A(Q^(-1)t)
    =A_0+sum_(j=1)^d conjugate(F_j)(A_j-A_(j-1))t^j,
 H_A(t)=sum_(j=0)^d conjugate(F_j) A_j t^j.               (19)

Equation (19) follows coefficientwise from the ORIGINAL recurrence.
Dropping its finite differences would lose genuine spectator
feedback. Controlling this forcing for complete interior crossings,
with the geometric exponent, remains part of the broad goal. The
present theorem proves source-specific cancellation at a nontrivial
normalization germ, not a general hyperbolic knot-volume estimate.

## 6. Where the excessive full-circle energy actually resides

The same exact Ward equation also bounds all root samples, so its
nonlocal energy is not an unspecified error. Write H_k=H_N(Q^k),
H_0=H_N(1), m=floor(N/6). Then

    H_1=Q^(-1),
    |H_k|<=N+2N s_(k-1), 1<=k<N.                      (20)

For k<=m+1, forward propagation of (2) from H_1 uses only factors
|1-Q^j|<=1 and proves |H_k|<=k. For k>=m+1, backward propagation
from H_N=H_0 gives exactly the modulus bound

    |H_k|<=s_(k-1)[|H_0|/N+sum_(r=k)^d 1/s_r].          (21)

After its minimum at m, the sine factorial rises to its unique
maximum interval and then decreases to N. Hence
min_(r>=k)s_r>=min(s_(k-1),N). Substituting (11) into (21) yields
(20). All inverses here have indices strictly between zero and N;
no zero root factor is divided out.

For the actual normalization polynomial (16), reflection now gives

    |f_N(Q^r)| <=1+2N+4N^2/s_r, 1<=r<N,
    |f_N(1)|=1.                                        (22)

Indeed Hbar_N(Q^r)=conjugate(H_N(Q^(-r))), and
s_(N-r-1)=N/s_r. Thus the full macroscopic clock cost has the
uniform leading envelope

    log |f_N(Q^r)| <= N max{-J(r/N),0}+O(log N),
    J(u)=integral_0^u log(2sin(pi v))dv.                 (23)

This uses the already proved uniform sine-factorial estimate; at a
zero of f it is simply an upper bound. The function -J has its
unique maximum c_*=v_3/(2pi) at u=1/6.

Finite Plancherel for the ORIGINAL coefficients (15) is exact:

    sum_(r=0)^d |f_N(Q^r)|^2
       =N sum_(j=0)^d |F_j|^2
       =exp(2c_*N+O(log N)).                            (24)

Consequently, for every fixed delta>0 small enough to give a proper
neighborhood of 1/6, there is eta_delta>0 such that

 [sum_(|r/N-1/6|>=delta)|f_N(Q^r)|^2]
 /[sum_r |f_N(Q^r)|^2] <= N^C exp(-eta_delta N).         (25)

To prove it, use the strict gap of the continuous envelope in (23)
off that neighborhood and (24). There are only N samples. No
pointwise lower estimate for an individual root sample is needed.

Thus the excessive ROOT-SAMPLED Fourier energy of this literal
normalization source is concentrated away from t=1, near phase
exp(pi*i/3). This discrete concentration statement alone does not
prove a corresponding continuum-arc concentration statement.
Equations (9),(18) control the original phase neighborhood and its
normal germs by a separate uniform complex-disk argument, while
(22)--(25) describe the sampled large-phase energy quantitatively.
No analogous concentration or local bound
is inferred for a general hyperbolic source.

There is also a sharp reason to retain the frequency restriction in
Section 5. Choose r_N maximizing |f_N(Q^r)|. Equations (23)--(25)
and the average in (24) imply

    r_N/N ->1/6,
    log |f_N(Q^(r_N))|=N v_3/(2pi)+O(log N).              (26)

The inserted diagonal clock Q^(r_N j) is UNITARY in the recording
space, yet produces this exponential scalar on the known packet.
It is an additional observable, not the original closed knot value.
Thus mere norm-one control of an arbitrary diagonal exterior cannot
replace the sublinear-frequency or geometric conditions in the
source estimate.

The [independent audit](../experiments/audit_normalization_clock_disk_independent.py)
checks exact finite recurrences, all backward phases, factorial
reflection and the product/integral bounds at ten levels through
N=192, as well as three noncommuting spectator-mode packets. Its
1,152 complex-disk samples supplement the all-disk proof; they are
not a numerical supremum certificate. The original physical source
identification is separately checked on every input column by the
[cup-slide audit](../experiments/audit_actual_terminal_source_normalization_packet.py).
Two independent analytic reviews verified the displayed constants,
the k=0 case, the endpoint, and the growing-bandwidth limit. The
expanded audit also checks nine complete root-sample profiles through
N=192, including all exact sample bounds and Plancherel, while
explicitly distinguishing discrete from continuum concentration.
