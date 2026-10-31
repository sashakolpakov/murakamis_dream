# A finite whole-source proof of the five-crossing cyclotomic transform

28 October 2026. The candidate in Section 6 of
[the actual five-crossing source](five_two_whole_source_reduction.md)
is an exact identity for EVERY primitive Nth root Q, N>=2,
and arbitrary nonzero Y. No Jones identity, ordinary-color
interpolation, or published Bailey proof is used.

Write q=Q in the proof, `d=N-1`, `F_a=(q;q)_a`, and

    H_n(x)=sum_(j=0)^n {n choose j}_q x^j,
    T_n(Y)=product_(r=1)^n(Y+Y^-1-q^r-q^-r).

Then the original reduced whole source satisfies

    F_N(Y)=sum_(n=0)^d C_n(q)T_n(Y),
    C_n(q)=(-1)^n q^(-n(n+3)/2)H_n(q^(-n-1)).   (1)

Every original turn, cap, Cartan and framing factor is already
contained in the starting triple source below. No factor is
changed in proving (1). The original full ADO modified-dimension
germ, if attached, multiplies both sides unchanged.

The proof supplies three reusable finite identities: a terminating
three-factor q-Chu transform, a generic Newton connection, and a
root Rogers-polynomial convolution with an arbitrary extra variable.

## 1. Elementary finite identities

For k<N and arbitrary a,b,

    sum_(ell=0)^k (q^-k;q)_ell(a;q)_ell(b;q)_ell q^ell/F_ell
       =sum_(r=0)^k {k choose r}_q a^(k-r)b^r(a;q)_r. (2)

Expand `(b;q)_ell`, set ell=r+s, and use

    sum_(s=0)^n(q^-n;q)_s(c;q)_s q^s/F_s=c^n.    (3)

For completeness, expand `(c;q)_s` in (3). For each expansion
index r the remaining sum is
`(q^(1-(n-r));q)_(n-r)` by the finite q-binomial theorem.
It vanishes unless r=n; that last coefficient is c^n.
Substituting (3) into the expansion of (2), together with
`(q^-k)_r/F_r=(-1)^r q^(-kr+r(r-1)/2){k choose r}`,
cancels every extra sign and power. This proves (2).
It is symmetric in a,b, so either factor may be expanded.

We also need the finite q-Vandermonde consequence

    sum_(u=0)^a sum_(j=0)^b {a choose u}_q
                          {b choose j}_q q^(ju)=H_(a+b)(1). (4)

To prove (4), compare coefficients in the finite q-binomial
expansion of a product of lengths a and b. It gives
`{a+b choose l}=sum_(u+v=l){a choose u}{b choose v}
q^((b-v)u)`. Replace v by b-j and sum over l.
All denominators used in this application have indices at
most d; no root-zero factorial is divided out.

## 2. Reduce the ACTUAL triple to a symmetric polynomial basis

The previously proved original source is

    F_N(Y)=sum_(m+ell<=d)sum_(j=0)^m
       Y^(2(d-m))q^(j(m+1)+m+ell+2)
       {m+ell choose ell}_q {m choose j}_q
       (q/Y;q)_(m+ell)(q^(j+1)/Y;q)_ell.        (5)

Replace j by m-j and put k=d-m. The ell sum becomes the left
side of (2) with `a=q^-k/Y`, `b=q^(-k-j)/Y`, because
`q^(m+1)=q^-k`. Use the SYMMETRIC form of its right side.
After the exact prefactor cancellation `q^(m(m+2)+2)=q^(k^2+1)`,
equation (5) is

    q sum_(k=0)^d Y^k(q/Y;q)_(d-k)
       *sum_(r=0)^k {k choose r}_q
          sum_(j=0)^(d-k){d-k choose j}_q
                          q^(jr)(q^(-k-j)/Y;q)_r. (6)

Expand the last Pochhammer with index s. Use
`{k choose r}{r choose s}={k choose s}{k-s choose r-s}`.
The remaining sums over r-s and j are exactly (4), with
lengths k-s and d-k. Thus

    F_N(Y)=q sum_(k=0)^d Y^k(q/Y;q)_(d-k)
       *sum_(s=0)^k {k choose s}_q(-1/Y)^s
                   q^(-ks+s(s-1)/2)H_(d-s)(1). (7)

Interchange k,s, set `n=d-s`, `k=s+r`, and reflect the
root Gaussian by

    {d-n+r choose r}_q
       =(-1)^r q^(-nr+r(r-1)/2){n choose r}_q.  (8)

All powers simplify to

    F_N(Y)=q sum_(n=0)^d (-1)^n q^(-n(n+1)/2)
                                      H_n(1) P_n(Y), (9)
    P_n(Y)=sum_(r=0)^n {n choose r}_q(-Y)^r
                         q^(r(r+1)/2)(q/Y;q)_(n-r).

For the sign at either parity, the root calculation used here is
`(-1)^(d-n)q^(-(d-n)(d-n+1)/2)
=(-1)^n q^(-n(n+1)/2)`. It follows from the full identity
`(-1)^d q^(d(d+1)/2)=1`; no even-level sign is discarded.

## 3. Generic Newton connection

For generic q, and hence at the present root whenever n<N,

    P_n(Y)=(-1)^n q^(n(n+1)/2)
                  sum_(k=0)^n q^(n-k){n choose k}_q T_k(Y). (10)

Here is a direct verification independent of (5).
The defining finite convolution for P_n gives

    P_0=1, P_1=1-qX,
    P_n=(1-q^n X)P_(n-1)+q^n(1-q^(n-1))P_(n-2),
    X=Y+Y^-1.                                  (11)

One way to verify (11) purely formally is to set
`A(z)=sum_n P_n z^n/F_n`. Its defining convolution gives
`A(qz)/A(z)=(1-z)/[(1-qYz)(1-qz/Y)]`; the two first-order
series equations follow immediately by comparing successive
coefficients in the finite q-binomial series. Comparing
coefficients in this displayed equation gives (11). This is
an identity of formal rational coefficients, not a rootwise
infinite-product evaluation.

Set `R_n=(-1)^n q^(-n(n+1)/2)P_n`. Then (11) becomes

    R_n=(X-q^-n)R_(n-1)+(q^(1-n)-1)R_(n-2).     (12)

The sum on the right of (10), after removing its prefactor,
satisfies the same recurrence and initial values. To check a
T_k coefficient, use `X T_k=T_(k+1)+(q^(k+1)+q^(-k-1))T_k`
and `{n choose k}={n-1 choose k-1}+q^k{n-1 choose k}`.
The only remaining ratio is
`{n-2 choose k}/{n-1 choose k}
=(1-q^(n-1-k))/(1-q^(n-1))`, which makes the two residual
terms `q^-n-q^(-k-1)` cancel. This proves (10).

Substitution of (10) into (9) cancels BOTH quadratic phases
and signs. Consequently the actual Newton coefficient is

    C_k(q)=q sum_(n=k)^d q^(n-k){n choose k}_q H_n(1). (13)

## 4. A reusable ROOT convolution evaluates every coefficient

In fact for arbitrary x, as a polynomial identity in x,

    q sum_(n=k)^d q^(n-k){n choose k}_q H_n(x)
      =(-1)^k q^(-k(k+3)/2)
                              x^d H_k(q^(-k-1)/x).  (14)

The right side is interpreted after multiplying by x^d,
so is polynomial also at x=0. Thus every x-Euler moment
can be differentiated in (14), with its source character
`x^(N-1)` retained.

Here is a finite coefficient proof. Put
`h_x(z)=sum_(n=0)^d H_n(x)z^n`. Gaussian generating functions
and the exact root product `prod_(r=0)^d(1-q^r z)=1-z^N` give

    h_x(z)=sum_(j=0)^d (xz)^j(q^(j+1)z;q)_(d-j). (15)

Indeed both sides have degree at most d, and their first N
coefficients agree by
`sum_(n>=j){n choose j}z^n=z^j/(z;q)_(j+1)`.
This last generating identity follows directly from q-Pascal;
it is used only through degree d where all factorials are units.

Set `a=q^(-k-1)=q^(d-k)`. The convolution

    sum_(r=0)^(d-k) a^r {r+k choose k}_q H_(d-r)(x)

is the coefficient of z^d in `h_x(z)/(az;q)_(k+1)`.
In (15), every term with `j<=d-k-1` cancels the whole
denominator, leaving a polynomial of degree d-k-1 and hence
ZERO z^d coefficient. Write the remaining j as d-k+s,
`0<=s<=k`. Its quotient is

    x^(d-k+s)z^(d-k+s)/(az;q)_(s+1).

Its z^d coefficient is
`x^(d-k+s)a^(k-s){k choose s}`. Summing over s gives

    x^d H_k(a/x).                               (16)

Finally use the exact root reflection
`{d-r choose k}=(-1)^k q^(-rk-k(k+1)/2){r+k choose k}`
in the left side of (14), setting n=d-r. Its prefactor is
`(-1)^k q^(-k(k+3)/2)` and the remaining sum is (16).
This proves (14) at every parity and composite level.

## 5. The candidate is proved as a WHOLE meridian identity

Take x=1 in (14) and substitute into (13). This gives
exactly (1), proving the candidate (6.1) of the source note.
At Y=1, `T_n(1)=(-1)^n q^(-n(n+1)/2)F_n^2`, so in
the original Q orientation the exact reduced state is

    <5_2>_N=sum_(0<=j<=n<N)
            Q^[-n(n+2)-j(n+1)](Q;Q)_n^3
                              /[(Q;Q)_j(Q;Q)_(n-j)]. (17a)

This is the source-preserving double sum used by the inner
quadrature theorem; its endpoints are not changed.
Equivalently, with t=Q^-1,

    F_N(Y)=sum_(n=0)^(N-1) t^n(tY;t)_n(t/Y;t)_n
                 sum_(j=0)^n t^(j(j+1)){n choose j}_t. (17)

All steps were identities of Laurent polynomials in Y.
Therefore every fixed-root meridian derivative, including
the normal complete-color source, is retained. No conclusion
about generic-q derivatives of the actual whole crossing is
obtained by differentiating the root identity in Q.

This proves a finite source transform; it does not establish
the saddle selection or the exponential volume lower bound.
Those analyses may now use (17) as an identity of the
original state, with its original normalization.

[Exact audit](../experiments/audit_five_two_finite_chu_bridge.py)
checks the reusable generic identities, every intermediate
root transform, the x-polynomial convolution, and whole-Y
Laurent coefficients at small levels. The uniform proof is
the finite calculation above, not interpolation of test colors.
