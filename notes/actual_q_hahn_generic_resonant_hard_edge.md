# The actual generic white numerator at the resonant hard edge

30 October 2026. source theorem. A genuine quantum
deformation of the original white numerator has a uniform boundary
packet. Its root limit is a Bessel function, while its retained
quantum normals differentiate the ORDER parameter of a confluent
hypergeometric function. The exact large monomial normalization stays
in the answer. No zero of the limiting function, cup divisor, or
global selected cycle is removed.

## 1. The original generic polynomial and its exact reindexing

Use the ACTUAL polynomial H_m^B(U,V) in the
[generic white-source theorem](actual_generic_boundary_gauge_and_source.md),
not a small root-colliding replacement for the large white channel.
Write Q=q^2, B=Q^(-N), and

    H_m^B(U,V)=sum_(k=0)^m c_k V^k
                 product_(r<k)(U-Q^r) product_(r<m-k)(V-Q^r),

    c_k=(-1)^k B^k Q^[k(k+1)/2] [m choose k]_Q
                           (BQ^(m-k+1);Q)_k/(BQ;Q)_k.    (1)

In particular c_m=(-B)^m Q^[m(m+1)/2], EXACTLY. Divide by the
actual k=m term

    Z_m=c_m(UV)^m product_(r=0)^(m-1)(1-Q^r/U).            (2)

Setting k=m-l gives the identity

    H_m^B/Z_m=sum_(l=0)^m T_l, T_0=1,

    T_l=(-1)^l B^(-l)Q^[-ml+l(l-1)/2] [m choose l]_Q
           (BQ^(m-l+1);Q)_l/(BQ;Q)_l
           (UV)^(-l) product_(r<l)(V-Q^r)
                      /product_(r=m-l)^(m-1)(1-Q^r/U).    (3)

This is a termwise identity of the original generic source. The
additional Pochhammer ratio in (3) is essential: replacing it by
another Gaussian binomial before differentiating would erase the
normal proved below. To verify the ratio directly, cancel
(BQ^(l+1);Q)_(m-l)=(BQ;Q)_m/(BQ;Q)_l in c_(m-l)/c_m.

## 2. A joint boundary packet with the actual moving parameter

Fix delta>0, and suppose m=m_N is an integer with
delta<=mu_N=m/N<=1-delta. At the original root q0=exp(pi i/N),
choose marked, possibly complex head lifts x_N,y_N such that

    U_N(0)=q0^(2x_N)=N^2 kappa_N,
    V_N(0)=q0^(2y_N)=V_N^0,
    |x_N|+|y_N|<=C N(1+log N).                            (4)

The kappa_N and V_N^0 range over fixed compact subsets of C minus
zero. Their logarithms are the specified head marks, not reset
principal values. Set

    epsilon=t/N^2, q_N(t)=exp(pi i/N+t/N^2),
    Q_N=q_N^2, B_N=Q_N^(-N),
    U_N(t)=exp[2x_N Log q_N(t)],
    V_N(t)=exp[2y_N Log q_N(t)].                           (5)

All integers N,m and all marked head lifts stay fixed under this
quantum deformation. Define

    K_N=sin^2(pi mu_N)(V_N^0-1)/(pi^2 kappa_N V_N^0),
    b(t)=1-t/(pi i),
    F(t;K)=sum_(l>=0) (-K)^l/[l! (b(t))_l].               (6)

The last line DEFINES the function customarily written
0F1(;b(t);-K); no hypergeometric transformation is imported.
On any fixed |t|<=rho<pi, the actual normalized source satisfies

    H_m^(B_N(t))(U_N(t),V_N(t))/Z_m(t)
          =F(t;K_N)+O((1+log N)/N),                      (7)

uniformly in all the displayed compact parameters. At t=0 this
is sum (-K_N)^l/(l!)^2=J_0(2sqrt(K_N)), interpreted by its entire
series so that no square-root choice is necessary.
The root specialization is the same actual boundary model as in
[the resonant root hard-edge theorem](actual_q_hahn_resonant_hard_edge.md).

The result is holomorphic in t on a larger disk of the same type.
Consequently, for every fixed j and a smaller disk,

    N^(-2j) partial_epsilon^j[H_m^B(U,V)/Z_m]|_0
        =partial_t^j F(t;K_N)|_0+O((1+log N)/N).           (8)

These are GENUINE generic-q normals of the specified source at
fixed marked heads. They are not derivatives of its root Bessel
formula. Across zeros of F the estimates are absolute in the
normalization (2). Relative estimates require a compact avoiding
the relevant zeros.

For example, with H_l=sum_(r=1)^l 1/r and
H_l^(2)=sum_(r=1)^l 1/r^2, the first two retained limits are

    partial_t F(0;K)=(pi i)^(-1)
                         sum_(l>=0) (-K)^l H_l/(l!)^2,
    partial_t^2 F(0;K)=(pi i)^(-2)
               sum_(l>=0) (-K)^l[H_l^2+H_l^(2)]/(l!)^2.  (8a)

They follow by differentiating the actual denominator in (6), and
are generally nonzero even though the root Bessel formula alone
has no moving-q parameter.

## 3. Proof: fixed terms, uniform domination and the error

For each fixed l and r, the actual small denominator factors are

    1-Q_N^r=(-2pi i/N)r(1+O(N^-1)),
    1-B_N Q_N^r=(-2pi i/N)[r-t/(pi i)](1+O(N^-1)).         (9)

The second line follows from
B_N Q_N^r=exp[(2pi i r-2t)/N+2rt/N^2]. This fixes the sign
of b(t). The first limiting singular parameter is t=pi i,
corresponding to the nearby moving period N-1. Our disks stay
strictly away from it.

The two numerator products in (3) each tend to
(1-exp(2pi i mu_N))^l. Combining their phase with
(-1)^l Q_N^(-ml) and the two factors (-2pi i/N)^l gives
(-N^2 sin^2(pi mu_N)/pi^2)^l. Moreover U_N(t)/U_N(0)
and V_N(t)/V_N(0) are 1+O((1+log N)/N), and the last denominator
product in (3) tends to one. Thus the lth term tends to

    (-K_N)^l/[l!(1-t/(pi i))_l],                         (10)

with the ACTUAL generic denominator rather than a squared factorial.

Here is a uniform summable bound, including large l. On a slightly
larger fixed t disk with radius less than pi, for all 1<=r<=m,

    |1-Q_N^r|>=c_delta r/N,
    |1-B_N Q_N^r|>=c_(delta,rho) r/N.                    (11)

For r bounded, (9) and |r-t/(pi i)|>=r(1-rho/pi) prove
the second estimate. For larger r it follows from the root sine
bound and its O(N^-1) perturbation; dividing at a sufficiently
large fixed r makes this comparison uniform. All numerator factors
are bounded by a constant. The powers of B,Q in (3) have bounded
modulus (or may be absorbed in C^l). Since |U_N(t)|>=c N^2
and |V_N(t)|>=c, the two binomial-type factors and (UV)^(-l)
cancel their N^(2l) costs. Finally

    product_(r=m-l)^(m-1)|1-Q_N^r/U_N(t)|^(-1)<=exp(C/N).

It follows that |T_l|<=C^l/(l!)^2, uniformly for 0<=l<=m.
The limiting terms satisfy the same type of bound. This proves
normal-family convergence by the actual finite series, not by
matching a formal solution of a differential equation.

The error in (7) can also be quantified directly. For l<=cN,
with c chosen below delta/2, compare each product in (3) with
(10). The numerator phases and the two denominator products have
relative logarithmic error O(l^2/N), and the retained moving heads
add O(l(1+log N)/N). Apply |exp(w)-1|<=|w|exp(|w|), and absorb
exp(C l^2/N)<=exp(C' l) into the preceding factorial majorant.
Summing gives O((1+log N)/N). This comparison is made factorwise
for product_(r<l)(V-Q^r), without dividing by V_N^0-1; it is
therefore uniform when K_N=0 as well. A telescoping product
difference gives the same bound there. For l>cN both factorial
tails are smaller than every inverse power of N. This proves
(7), uniformly on the larger t disk. Cauchy's formula then
proves (8) and all fixed t derivatives of the error.

## 4. The exact normalization is not a harmless constant

Equation (2) is kept at the moving parameter. In particular it
contains U_N(t)^m even though U_N(t)/U_N(0) tends to one.
For standard fixed marks Log U_N(0)=2log N+Log kappa_N,

    U_N(t)^m/U_N(0)^m
       =exp[mu_N t Log U_N(0)/(pi i)]
       =N^[2mu_N t/(pi i)]
                     exp[mu_N t Log kappa_N/(pi i)].       (12)

Other retained head carries give their actual additional factors;
they are not removed from (2). The exact top coefficient contributes

    c_m(t)/c_m(0)=exp[t(-2Nm+m(m+1))/N^2].                (13)

The remaining product in (2) is nonzero on the stated disks. Its
logarithmic t derivatives are uniformly bounded with the same
marked heads. Equations (12),(13), V_N(t)^m and that product give
the original unnormalized jets by ordinary Leibniz. In particular
they are not obtained by simply differentiating J_0 at fixed K.

On any compact where F(0;K_N) stays away from zero, (7),(8)
give a nonzero local root packet and relative fixed-normal bounds.
If the limiting Bessel factor vanishes, the normalized series and
its true parameter derivatives are still covered, but no nonzero
leading amplitude is asserted. The theorem concerns the actual
white numerator; all scalar, cup and marked contraction factors
must still be restored before discussing an operator or its
original finite period.

The [focused audit](../experiments/audit_actual_q_hahn_generic_resonant_hard_edge.py)
and [results](../experiments/actual_q_hahn_generic_resonant_hard_edge_results.json)
check 20 symbolic reindexed coefficients, 54 nonroot and 54 root
original-H four-jet identities with 432 coefficients, 48 complex
scaled-parameter packets, 24 genuine scaled first/second normals,
12 independent terminating source values, six retained top-term
normalizations and both harmonic normal formulas. Finite convergence
errors are recorded as diagnostics, separately from the uniform proof.

The result is restricted to the specified white numerator and its normalization, with limiting zeros retained; it is not a full-operator or selected-period theorem.