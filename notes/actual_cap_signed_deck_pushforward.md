# Four-channel actual cap pushforward with signed deck characters

28 October 2026. This extends the exact central-meromorphic
[actual cap extraction](actual_cap_pachner_wall_charge.md) to bounded
SIGNED Puiseux characters. The source, co-source, residue weights and
0/d corner indices are the original ones. Fixed negative characters
cost a power of N. Arbitrary bulk characters are not covered by this
polynomial bound.

## 1. A single exact formula for every actual endpoint channel

Put d=N-1, epsilon=a^N, delta=(1-epsilon)^(1/N), delta(0)=1.
Use the original Fermat sources P^s and L^t, s,t in {0,d},
and alpha_0=beta_0=1, alpha_d=1-Q, beta_d=N. Set

    sigma=1_(s=d), D=sigma+t,
    R=(1-Q delta)/(1-Q),
    E_j=product_(h=0)^(j-1)(1-delta Q^h),
    E_(j+N)=epsilon E_j.

The last identity extends E_j to ALL signed integers j as a
meromorphic germ. It retains, rather than resets, the full central norm.
Let O(a)=a^ell O_ell(epsilon), ell any integer. The exact cap functional

    [alpha_s beta_t]^-1 Res_(a=0)
               a^(D-1) L^t(a) O(a) P^s(a) da

is the central constant coefficient of

    sum_(n=0)^d H_n^(ts,ell)(epsilon)
                [O_ell(epsilon)]_(m(n),n),
    m(n)=(n+t-s+ell) modulo N,

where h=n+sigma and

    H_n^(ts,ell)=B_t R^sigma E_(h+ell)/E_(h+1),
    B_0=1-delta, B_d=epsilon/N.                           (1)

Here the representative m(n) is always in 0,...,d. The epsilon
powers in (1) include the corresponding integer carry exactly.

To prove (1), express every source product in the common E frame:

    denominator(P^0_n)=E_(n+1)/(1-delta),
    denominator(P^d_n)=E_(n+2)/[(1-delta)(1-Qdelta)],
    numerator(L^0_m)=E_m,
    numerator(L^d_m)=E_(m+1)/(1-delta).

The prefactor in the residue contributes a^(D+ell+n-m).
Since D+ell+n-m is a multiple of N, this is precisely its
integer power of epsilon. Apply E_(j+N)=epsilon E_j. All
long products cancel, leaving exactly (1). This proves the
operator indices, normalization and deck charge simultaneously.
At ell=0 it is the four-channel table in the earlier theorem.

No assumption that an arbitrary singular matrix descends to epsilon
has been made: its chosen character a^ell is part of the input.
Summing the actual character decomposition preserves the original
matrix operator. A character may not be deleted because its central
norm later has a numerical specialization.

## 2. Bounded signed characters have polynomial source cost

For ell>=1 the quotient in (1) is the SHORT numerator product

    E_(h+ell)/E_(h+1)
                   =product_(j=h+1)^(h+ell-1)(1-delta Q^j). (2)

For ell=-k, k>=1, it is the SHORT reciprocal product

    E_(h-k)/E_(h+1)
                   =1/product_(j=h-k)^h(1-delta Q^j).      (3)

Take rho=1/16 and N>k. In (3) the interval contains at most
one exceptional factor 1-delta. If it occurs, B_0 cancels it
exactly, while B_d cancels it by

    epsilon/[N(1-delta)]=(1+delta+...+delta^(N-1))/N.

Thus the kernel is holomorphic at epsilon=0. All other factors
have absolute value at least 3/N on |epsilon|<=rho; also |R|<2.
The actual uniform bounds are

    ell=0:       sup_n |H_n| <=2,
    ell>=1:      sup_n |H_n| <=4rho 3^(ell-1)/N,
    ell=-k<0:    sup_n |H_n| <=2(1+rho)(N/3)^k, N>k.     (4)

For (2), use |1-delta Q^j|<=3 and |B_t|<=2rho/N.
For (3), cancel the exceptional factor when present; otherwise
use that same B_t estimate. This proves (4), not merely a
coefficient estimate at one root value.

For an actual central Laurent matrix with fixed pole order p,

    O_ell(epsilon)=sum_(r=-p)^infinity A_r epsilon^r,

Cauchy's estimate and (4) give the exact finite pushforward

    cap(O)=sum_(r=0)^p sum_n [epsilon^r]H_n
                                      (A_(-r))_(m(n),n),

    |cap(O)| <=N C_ell(N) sum_(r=0)^p16^r||A_(-r)||_op, (5)

where C_ell(N) is the corresponding bound in (4). Thus fixed
signed characters and fixed central pole orders have polynomial
cost. For ell=-k the asymptotic requirement N>k is explicit;
smaller levels use the same exact formula (1), after retaining
its additional integer epsilon carry. Fixed finitely many small
levels do not alter the volume-rate assertion.

This is not a bound for unrestricted ell=ell(N). The bulk-sector
example derived in the all-sector analysis has exponential source
cost despite fixed central pole order. Its actual support must be
checked in a singular Pachner operator before applying (5).

## 3. Arbitrary meromorphic operators on the cap cover

There is also a separate statement that needs no central descent.
Define the ORIGINAL normalized source frames

    p_hat_s=a^sigma P^s/alpha_s,
    l_hat_t=a^t L^t/beta_t.

They are holomorphic with respective values e_s,e_t^t at zero,
and have uniformly bounded Euclidean norms on
|a|<=1/(16N), by the explicit cap-frame estimate. If

    O(a)=sum_(j=-p)^infinity A_j a^j

is any actual matrix Laurent germ with fixed COVER pole order p,
the exact cap residue is

    CT_a l_hat_t(a) O(a) p_hat_s(a).

The rank-one source kernel has trace norm bounded by an absolute
constant C on that circle. Cauchy on its coefficients proves

    |cap(O)| <= C sum_(j=0)^p(16N)^j||A_(-j)||_op.       (6)

Thus every such actual cover-meromorphic operator has a polynomial
finite-jet extraction, even if it is not invariant under a->Qa.
Fixed central pole order and fixed cover pole order are different:
an epsilon pole of order p has cover order Np. Formula (6) must
not be substituted for (5) while hiding that growth.

For 0<=r<N, the four normalized cover jets are explicitly

| Endpoint | r=0 | 1<=r<N |
|---|---|---|
| input0 | e_0 | e_r/F_r |
| inputd | e_d | e_(r-1)/F_r |
| output0 | e_0^t | e_(N-r)^t/F_r^- |
| outputd | e_d^t | e_(d-r)^t/F_r^- |

Here F_r^-=(Q^-1;Q^-1)_r. These follow by canceling the unique
vanishing factor and using full factorial reflection; they include
the wrapped channels. They independently fix the indices in (1).

## 4. Actual-network scope

The source functionals in (1), (5) and (6) are the actual normalized
0/d corners used simultaneously by the original pair-fused plat.
The original Cartan, framing, turn and peripheral lines multiply
the same expressions. Independent source variables tensor with
the displayed constants. For a fixed word and bounded pole orders
and signed-character support, the total extraction cost is a fixed
power of N relative to the ORIGINAL Laurent-coefficient norms.
These are the specified relative-head coordinate norms. No equality
with the physical tensor metric across a nonunitary fusion is asserted,
and an exponentially large coefficient matrix remains exponentially
large in these bounds.

An equality of complete actual typed meromorphic operators on the
same marked cover remains an equality after this finite extraction.
This supplies the regularized residue rule for a typed Pachner
identity when its actual exterior maps and common cover have been
specified. It does not supply that exterior comparison merely
from a classical five-term identity, nor equate the character label
with a geometric edge winding. Singular factors must first be
composed with their actual maps, or all their finite source jets
and integer carries must be retained term by term in a common
Laurent expansion. The coincident residue is not a silent pullback
of independent differential forms across a singular diagonal.

[Exact original-source audit](../experiments/audit_actual_cap_signed_deck_pushforward.py).

## 5. Sharp scope: a bulk character has exponential cap extraction

The bounded-character hypothesis above cannot be removed from the
original SINGLE-HEAD d-to-d cap functional. For N>=7 set

    L=ceil(N/6), U=floor(5N/6),
    n=L-2, r=U-n, m=U,
    O(a)=a^r epsilon^-1 |m><n|.

All indices lie in the original head range and 1<=r<N. The exact
d-to-d positive-character kernel from (1)--(2) gives

    cap(O)=[epsilon]H_n^(dd,r)
          =(1/N) product_(j=L)^U(1-Q^j).                 (7)

This can also be read directly from the literal normalized cap
frames: their relevant leading components are

    (p_hat_d)_n=a^(n+1)/F_(n+1)+higher central powers,
    (l_hat_d)_m=a^(d-m)F_m/N+higher central powers.

The coupon contributes a^(r-N). The total power is zero since
m=n+r and d+1=N, leaving F_U/[N F_(L-1)], exactly (7).
Thus the example retains the actual cap normalization and indices;
it is not a redefinition using an unknown knot period.

The elementary Riemann sum on the nonsingular interval [1/6,5/6]
proves

    lim_N (1/N)log|cap(O)|
       =integral_(1/6)^(5/6) log(2sin(pi t))dt
       =Vol(4_1)/(2pi)>0.                               (8)

On every fixed circle |epsilon|=rho in (0,1), however,

    ||O(a)||_op=rho^(r/N-1)<=rho^-1,

uniformly in N. Its central pole order is exactly one; the deck
character r grows proportionally to N. Thus neither bounded
central pole order nor bounded inserted-coupon norm alone makes
the SINGLE-HEAD actual cap extraction tempered over all characters.

This is an original cap with an INSERTED auxiliary coupon. It is
NOT an original knot counterexample, and the coupon does NOT
intertwine the actual degree/Cartan charge: it changes the head
degree by r. In particular extending it trivially on the other
head gives zero between the paired D=d charge projections. The
[tame paired source](tame_paired_fermat_source_transport.md)
uses that actual charge and is not contradicted by (7)--(8).
The example explains why that paired-charge improvement and the
explicit deck-support hypotheses are substantive.
