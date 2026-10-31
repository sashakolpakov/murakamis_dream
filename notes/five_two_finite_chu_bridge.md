# An unconditional finite q-Chu reduction of the actual five-crossing source

28 October 2026. The actual three-index period in
[the whole-source calculation](five_two_whole_source_reduction.md)
has a two-index whole-meridian reduction by elementary finite
q-binomial identities. This reduction does not assume the candidate
Newton coefficients in its Section 6. The further transform is now
proved in [the full cyclotomic proof](five_two_cyclotomic_transform_proof.md);
this note records the independent double-sum route.

Write q=Q here (the Gaussian base, not the half-root),
`d=N-1`, `F_a=(q;q)_a`, and `H_a(z)=sum_j {a choose j}_q z^j`.
Every denominator below has index less than N.

## 1. A reusable terminating three-factor transform

For k with `F_1,...,F_k` nonzero, and arbitrary a,b, exactly

    sum_(ell=0)^k (q^-k; q)_ell (a;q)_ell (b;q)_ell
                                      q^ell/F_ell
       =sum_(r=0)^k {k choose r}_q
                                a^(k-r)b^r(a;q)_r.   (1)

This is a polynomial identity in a,b, without a genericity
condition on their Pochhammer factors.

First prove the finite q-Chu identity

    sum_(s=0)^n (q^-n;q)_s(a;q)_s q^s/F_s=a^n. (2)

Expand `(a;q)_s` by the finite q-binomial theorem and interchange
the finite sums. For its coefficient with index r the remaining
sum is

    sum_(t=0)^(n-r)(q^(-(n-r));q)_t q^t/F_t
                                  =(q^(1-(n-r));q)_(n-r).

The last equality is the same finite q-binomial theorem. It is
zero unless r=n, because otherwise one factor is `1-q^0`.
The r=n term simplifies to a^n, proving (2).

To prove (1), expand `(b;q)_ell`, put ell=r+s, and use (2)
with length k-r and parameter a q^r. The inner sum is
`(a q^r)^(k-r)`. Substitute

    (q^-k;q)_r/F_r=(-1)^r q^(-kr+r(r-1)/2){k choose r}_q.

All signs and q powers cancel, leaving exactly (1).

## 2. Applying it to the original triple source

Start with the proved actual source formula

    F_N(Y)=sum_(m+ell<=d)sum_(j=0)^m
       Y^(2(d-m))q^(j(m+1)+m+ell+2)
       {m+ell choose ell}_q {m choose j}_q
       (q/Y;q)_(m+ell)(q^(j+1)/Y;q)_ell.        (3)

Replace j by m-j and put k=d-m. At a primitive Nth root,
`q^(m+1)=q^-k` and `q^(m(m+2)+2)=q^(k^2+1)`.
The ell sum is the left side of (1) with

    a=q^-k/Y, b=q^(-k-j)/Y.

Its r-th term is
`Y^-k q^(-k^2-jr){k choose r}(q^-k/Y;q)_r`.
The prefactor in (3) consequently simplifies to q Y^k.
Set n=k-r and use the exact contiguous product

    (q/Y;q)_(d-k)(q^-k/Y;q)_(k-n)
                                        =(q/Y;q)_(d-n),

which follows from q^N=1 before any Y evaluation. One obtains

    F_N(Y)=q sum_(0<=n<=k<=d)
          Y^k {k choose n}_q (q/Y;q)_(d-n)
                                  H_(d-k)(q^n).       (4)

This is already an exact simpler finite source transform.
It preserves arbitrary Y and all of its meridian derivatives.

## 3. One more finite q-binomial sum gives a DOUBLE sum

Expand H in (4). Put k=n+r and `d-k=j+s`, so
`n+r+j+s=d`. The root reflection identity gives

    F_(n+r) F_(j+s)
        =N(-1)^(j+s)q^((j+s)(j+s+1)/2).        (5)

Fix n,j and set `L=d-n-j=r+s`. The remaining r,s sum is

    sum_(s=0)^L (-1)^s q^(s(s+1)/2+js)Y^-s
                                      /(F_s F_(L-s))
                           =(q^(j+1)/Y;q)_L/F_L.     (6)

Equation (6) is the ordinary finite q-binomial theorem. Thus
the whole actual reduced scalar has the unconditional formula

    F_N(Y)=Nq sum_(n,j>=0,n+j<=d)
       (-1)^j q^(j(j+1)/2+nj) Y^(d-j)
       (q/Y;q)_(d-n)(q^(j+1)/Y;q)_(d-n-j)
                     /[F_n F_j F_(d-n-j)].     (7)

The factor N in (5)-(7) is the exact full root factorial,
not a normalization chosen after evaluating Y. The original
Cartan, turning, cut and framing factors are already included
in (3), so remain included in (7). The separate full ADO
modified-dimension factor multiplies both unchanged.

Equivalently, with k=d-n, (7) is

    Nq Y^d sum_(k=0)^d (q/Y;q)_k^2/[F_(d-k)F_k]
       * sum_(j=0)^k (q^-k;q)_j Y^-j
                                      /[F_j(q/Y;q)_j]. (8)

Formula (8) is initially read after cancelling Pochhammer
denominators termwise back to (7); no division at a Y source
zero is implied.

## 4. Relation to the proved cyclotomic formula

Putting t=q^-1, the proved cyclotomic form in the original note is

    F_N(Y) =sum_(n=0)^d t^n(tY;t)_n(t/Y;t)_n
                       sum_(j=0)^n t^(j(j+1)){n choose j}_t. (9)

The inner normalized coefficient is the elementary Bailey
convolution `sum_j t^(j^2+j)/[F_j(t)F_(n-j)(t)]`.
Equations (1)-(8) give an independent double-sum expression.
The [full proof](five_two_cyclotomic_transform_proof.md) instead
uses the symmetric three-factor expansion, a generic Newton
connection, and an exact root Rogers-polynomial convolution to
prove (9). Repeated ordinary-color nodes are not used as an
interpolation proof.

[Exact audit](../experiments/audit_five_two_finite_chu_bridge.py)
checks (1) at generic finite parameters and compares (3),
(4), (7), and the original literal source at primitive roots
with unrestricted whole-meridian evaluations. The displayed
finite identities, not the samples, establish their scope.
