# A fixed angular gap for the actual protected-middle cofactor

The [whole-source local packet](general_full_spectral_numerator_geometric_packet.md) now assembles these results for the actual full numerator. The original global spectral filling period remains open.

31 October 2026. Internally reviewed. The middle face is the ORIGINAL protected
zero b=0. The proof uses the literal level-N recurrence and preserves
all its endpoint coefficients. It is independent of the relative
cofactor packet and does not assert a whole shared-face torus gap.

Write theta=pi/N and

 s_j=2sin(j theta), a_j=4cos^2((j+1/2)theta),
 A=x+y, P=xy,
 p_j=s_j^2 A, q_j(w)=s_j s_(j-1)(a_(j-1)+w)P.

The original cleared cofactor is

 R_0=1, R_(-1)=0,
 R_j(w)=p_j R_(j-1)(w)+q_j(w)R_(j-2)(w).             (1)

The spectral coordinate is w=-sigma-2. In particular no inverse
of a near-fold diagonal is introduced. All factors at the actual
terminal rows m-2,m-1,m, m=floor(N/2), remain in (1).

## 1. Exact coefficientwise spectral control

For N>=3 and 0<=n<=floor(N/2), as polynomials in x,y,w,

             0 <= R_n(w) <= (1+w)^n R_n(0).           (2)

Inequality means comparison of every coefficient. Therefore, for
positive real x,y and arbitrary complex w,

 |R_n(x,y;w)| <= R_n(x,y;|w|)
                  <= (1+|w|)^n R_n(x,y;0).           (3)

To prove (2), put d_j=s_j s_(j-1)xy. Positivity of the recurrence at
w=0 gives, for j>=2,

 R_j(0)>=(p_j p_(j-1)+q_j(0))R_(j-2)(0).

The polynomial p_j p_(j-1)+q_j(0)-d_j has coefficients

 (s_j s_(j-1))^2 at x^2 and y^2,
 s_j s_(j-1)[2s_j s_(j-1)+a_(j-1)-1] at xy.

Its bracket satisfies the EXACT level-N identity

 2s_j s_(j-1)+a_(j-1)-1
    =4cos(theta)+1-2cos((2j-1)theta) >=1.             (4)

Here N>=3 and all the used s_j are nonnegative. Hence
R_j(0)>=d_j R_(j-2)(0), coefficientwise. The induction from j=0,1 is

 R_j(w) <= (1+w)^(j-1)
       [p_j R_(j-1)(0)+(q_j(0)+w d_j)R_(j-2)(0)]
       <= (1+w)^j R_j(0).

The first inequality uses (1+w)^(j-2)<=(1+w)^(j-1), coefficientwise
also in w. This proves (2), including every zero outer specialization.

## 2. Three-step angular contraction

Fix x0,y0>0, put A0=x0+y0, P0=x0y0, and let x=x0 exp(i alpha),
y=y0 exp(i beta). If the circular distance of alpha-beta from0 is
at least epsilon, with 0<epsilon<=pi, then

 |x+y|<=r A0,
 r=sqrt[1-4P0/A0^2 sin^2(epsilon/2)]<1.              (5)

Set v=|w|. Taking absolute values in (1) is bounded by the positive
recurrence with first coefficient r p_j, second coefficient q_j(v),
where now p_j=s_j^2 A0 and q_j(v)=s_j s_(j-1)(a_(j-1)+v)P0.
Let

 T_j=[[p_j,q_j(v)],[1,0]],
 T_j^r=[[r p_j,q_j(v)],[1,0]].

On the bulk interval N/8<=j<=3N/8 and 0<=v<=1,

 p_j >=4sin^2(pi/8)A0,
 q_j(v) <=4(4+v)P0 <=5A0^2.

Write

 beta0=16sin^4(pi/8)/[16sin^4(pi/8)+5],
 eta=(1-r)beta0>0.                                  (6)

For any three consecutive indices contained in that interval,

 T_j^r T_(j-1)^r T_(j-2)^r
          <=(1-eta) T_j T_(j-1) T_(j-2)              (7)

entrywise. Indeed their top-left entry is a sum of terms with at
least one p, so contracts by at least r. Their bottom-right entry
is p_(j-1)q_(j-2), also contracting by r. The remaining entries are

 (p_j p_(j-1)+q_j)q_(j-2),
 p_(j-1)p_(j-2)+q_(j-1).

In each, the fraction carried by its two-p term is at least beta0.
That part contracts by r^2. Since 1-r^2>=1-r and beta0<=1,
all four entries obey (7). This proves a uniform positive amount
of one-step mass; it does not assert that every individual path
has a linear number of one-steps.

If N>=64 and 3N/8<=n<=floor(N/2), the integer interval from
ceil(N/8) to floor(3N/8) contains at least N/16 disjoint triples.
All remaining matrices satisfy T_j^r<=T_j. Multiplication of
nonnegative matrices and the exact initial vector (1,0)^T gives

 |R_n(x,y;w)| <= (1-eta)^(N/16) R_n(x0,y0;v).       (8)

No division by a transfer entry or by R_(-1) has occurred.

## 3. A fixed complex spectral neighborhood

Combine (3),(8), using n<=N/2. For

                         |w|<=eta/16,

one obtains

 |R_n(x0 exp(i alpha),y0 exp(i beta);w)|
          <=exp(-eta N/32) R_n(x0,y0;0).             (9)

At w=0 the stronger exponent eta N/16 follows. Constants are uniform
when (x0,y0) lies in a fixed positive compact set and epsilon is fixed.
The actual terminal indices m-2,m-1 and m satisfy the interval
condition for all sufficiently large N. Both parities are included.

If exactly one outer face is zero, (1) is instead the exact monomer

 R_n=(x+y)^n product_(j=1)^n s_j^2,

independent of w. Its modulus is unchanged by its sole phase, so
there is no relative-angular condition or gap to claim in that case.
If both outers vanish, R_n=0 for n>0; this is excluded by the original
marked MAIN-versus-MATCHING dictionary on the geometric chart.

The bound is on the actual cofactor, at the original protected target.
A whole shared-face angular gap still requires the graph argument
showing that every nontrivial face phase is detected by an appropriate
ordinary-middle or protected-middle factor. This note supplies only
the protected-middle local input to that argument.

## Focused verification and review

`../experiments/audit_actual_cross_cofactor_protected_angular_gap.py` accepts an
independent `--output` path. Its author result is
`../experiments/actual_cross_cofactor_protected_angular_gap_results.json`, PASS at
70 digits: one exact trigonometric identity, 4,636 original polynomial
coefficient inequalities, 486 actual complex angular bounds, 432
three-step matrix-entry bounds, and 16 exact monomer specializations.
These supplement the all-level proof and do not test a whole-source
torus claim. Independent coherent full analytic review PASS;
independent cluster full analytic and code review PASS.

[Focused audit](../experiments/audit_actual_cross_cofactor_protected_angular_gap.py) · [Recorded output](../experiments/actual_cross_cofactor_protected_angular_gap_results.json). These finite checks supplement the written proof and retain the scope recorded in their output.
