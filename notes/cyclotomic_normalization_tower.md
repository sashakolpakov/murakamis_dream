# A local cyclotomic normalization tower and its regulator norm

Research note, 25 October 2026. The normalization in the
[Heisenberg torsor](heisenberg_period_torsor.md) is a finite-product
object. Its compatibility between levels can be proved without a
Habiro-ring or algebraic K-theory theorem. This note supplies those
identities for every level, including even and composite levels, and
derives its local archimedean norm directly. This is a local result,
not the identification of a contracted knot invariant with a product
of tetrahedron norms.

The cyclic dilogarithm and its recurrence are existing definitions
(Faddeev--Kashaev, [hep-th/9310070](https://arxiv.org/abs/hep-th/9310070)).
No novelty is claimed for the finite products or their distribution.
The larger rings and K3-indexed modules introduced in
[Garoufalidis--Scholze--Wheeler--Zagier](https://arxiv.org/abs/2412.04241v2)
concern Frobenius-modified arithmetic gluing of formal series. None of
their theorem claims or proofs is used below. The local identities here
do not construct those modules or identify their elements with Kashaev's
actual values.

## 1. One pointed root at every level

For N>=1 let zeta_N=exp(2pi*i/N) and set

    D_N(x)=product_(j=1)^(N-1)(1-zeta_N^j*x)^j,
    Q_N(x)=D_N(x)^2/(1-x^N)^(N-1),
    s_N(x)^(2N)=Q_N(x), s_N(0)=1.                    (1.1)

The last equation defines a unique formal power series in
Q(zeta_N)[[x]]: raising a series with constant term one to the power
2N is a bijection in characteristic zero. It also defines its
analytic branch on |x|<1. Outside that disk one retains the root
torsor and a specified continuation, rather than suppressing its phase.

For odd N, (1.1) reduces to the earlier normalization:

    s_N(x)^N=product_(j=0)^(N-1)
                     (1-zeta_N^j*x)^(j-(N-1)/2).     (1.2)

This follows by squaring (1.2) and using its constant term. For even
N the half-integral centering is represented by the 2N-th root in
(1.1); no oddness assumption is inserted into a formula with halves.

Index translation in the finite product gives exactly

    D_N(zeta_N*x)/D_N(x)=(1-x)^N/(1-x^N),
    s_N(zeta_N*x)/s_N(x)=(1-x)/(1-x^N)^(1/N).         (1.3)

All roots in (1.3) have constant term one. These are the cyclic
intertwiner recurrence and its determinant normalization, with a
pointing that fixes the local scalar.

## 2. Exact compatibility between arbitrary levels

Let N=m*n and choose zeta_m=zeta_N^n, zeta_n=zeta_N^m. Then

    D_(mn)(x)=D_m(x^n)
                 product_(b=0)^(m-1) D_n(zeta_(mn)^b*x)^m,

    Q_(mn)(x)=Q_m(x^n)
                 product_(b=0)^(m-1) Q_n(zeta_(mn)^b*x)^m,

    s_(mn)(x)=s_m(x^n)^(1/n)
                 product_(b=0)^(m-1) s_n(zeta_(mn)^b*x). (2.1)

These are equalities of the pointed formal series, hence of their
matched continuations. There is no restriction that m,n be coprime
or avoid a set of bad primes.
This statement concerns characteristic-zero finite-product identities;
it does not assert integral or p-adic gluing at those primes.

For the first equality write each index as j=a*m+b. The exponent
a*m yields the D_n factors, while the exponent b yields

    product_(a=0)^(n-1)(1-zeta_n^a*zeta_(mn)^b*x)^b
                        =(1-zeta_m^b*x^n)^b.

The denominators in Q multiply correctly because
(m-1)+m(n-1)=mn-1. Raise the last equality of (2.1) to the power
2mn and use the pointed root to prove it without a scalar ambiguity.
For three levels, every regrouping has the same power and constant
term; equivalently, one groups the index by three digits. This proves
associative distribution with its phases fixed locally.

The maps here include x -> x^n and deck rotations of x. Consequently
this identity is not an equality of independently chosen values at
one fixed central character for every level.

## 3. A direct Galois/Kummer certificate

Let K=Q(zeta_N), let a be prime to N, 1<=a<N, and let sigma_a send zeta_N to
zeta_N^a while fixing x. With [k]_N the residue in {0,...,N-1}, put

    B_(N,a)(x)=product_(k=1)^(N-1)
       (1-zeta_N^k*x)^((a*[a^(-1)*k]_N-k)/N).

Its exponents are integers. Reindexing the product proves

    sigma_a(D_N)^a/D_N = B_(N,a)^N.                  (3.1)

Thus the class of D_N in K(x)^*/K(x)^(N*) has the inverse cyclotomic
Galois character, since a*sigma_a[D_N]=[D_N]. In terms of Q_N,

    sigma_a(Q_N)^a/Q_N
       =B_(N,a)^(2N)*(1-x^N)^(-(a-1)(N-1)).         (3.2)

This is an explicit local Kummer certificate. It does not show that
these classes satisfy the global Bloch five-term relation with the
required period normalization, nor identify a global Chern class.

## 4. The local norm from an exact logarithmic series

On |x|<1, expand the logarithms in (1.1). The finite sums are

    sum_(j=1)^(N-1) j*zeta_N^(j*k)
       =-N/(1-zeta_N^k) if N does not divide k,
       =N(N-1)/2        if N divides k.

The divisible terms cancel the denominator of Q_N exactly. Therefore

    log s_N(x)=sum_(k>=1, N does not divide k)
                         x^k/[k*(1-zeta_N^k)].        (4.1)

There is no asymptotic assumption in (4.1). For any r<1 it implies,
uniformly on |x|<=r,

    log s_N(x)=-N Li_2(x)/(2pi*i)
                         -(1/2)log(1-x)+E_N(x),

    |E_N(x)| <= pi*r/[4N(1-r)]
                       +2*r^(floor(N/2)+1)/(1-r).   (4.2)

Here N>=2. One elementary proof splits the sum at k=N/2. For the
first part use

    1/(1-exp(2pi*i*k/N))=1/2+(i/2)cot(pi*k/N),
    0 <= 1/u-cot(u) <= u/2, 0<u<=pi/2.

The last inequality follows from
sin(u)-u*cos(u)=integral_0^u v*sin(v)dv
and sin(v)<=sin(u). This bounds each error coefficient by
pi*k/(4N). In the tail, for a nondivisible k,
|1-zeta_N^k|^(-1)<=N/4. Bound the difference coefficient by N
and use 1/k<2/N. The same bound includes the omitted divisible
terms of the two comparison series. Geometric summation proves
(4.2). In particular E_N=O_r(1/N).

Define the metric on the inverse of this specified local frame by

    log ||s_N(x)^(-1)||_reg
       =-log|s_N(x)|+N log|x| Arg(1-x)/(2pi).         (4.3)

The expression extends at x=0. On this disk the branch of Arg is
the one from log(1-x). With the Bloch--Wigner function

    D(x)=Im Li_2(x)+log|x| Arg(1-x),

equation (4.2) gives the quantified comparison

    (2pi/N)log ||s_N(x)^(-1)||_reg
       =D(x)+(pi/N)log|1-x|-(2pi/N)Re E_N(x).        (4.4)

It is valid at all levels. This establishes the local regulator
rate of the existing normalization frame on compact subdisks.
The norm is specified in (4.3); it is not a new definition of the
knot invariant and is not yet its absolute-value norm.

## 5. What happens outside this chart and at resonance

The restriction in (4.2) matters. Cyclic factors have zeros on the
unit circle, and an independent evaluation of one frame can be
undefined even when the whole period has a regular germ. For
example x=exp(pi*i/3) has x^N=1 at multiples of six. A whole
period identity and its lattice must be specialized before its
individual factors. The
[recoupling lattice](cyclic_steinberg_lattice.md) gives one explicit
instance of such a regular integral replacement.

An exact identity also detects the chart correction. With
S=N(N-1)/2 and T=sum_(j=1)^(N-1)j^2, direct inversion gives

    D_N(x)D_N(1/x)
       =(-1)^S*zeta_N^T*x^(-S)
                              [(1-x^N)/(1-x)]^N,

    Q_N(x)Q_N(1/x)
       =(-1)^(N-1)*zeta_N^(2T)
                              (1-x^N)^2/(1-x)^(2N). (5.1)

For any matched root choices away from the divisors, it follows that

    log|s_N(x)|+log|s_N(1/x)|
                         =log|1-x^N|/N-log|1-x|.    (5.2)

One must transport the regulator metric as well as this algebraic
frame. In particular, using the unchanged formula (4.3) on both
sides of inversion would introduce the quadratic logarithmic term
log|x| Arg(-x); it would not give D(x)+D(1/x)=0. The logarithmic
connection and its frame transport supply additional data.

## 6. The remaining knot theorem

This gives an exact local system across all levels and proves its
local regulator estimate. The
[regular cyclic/Steinberg family](cyclic_steinberg_lattice.md) also
places the vacuum in the actual Kashaev color. Neither result says
that contracting the knot tensor is a product of these scalar norms.
Contraction includes phases and cancellation, and its distinguished
global pairing still has to be compared with the geometric period.

The required global assertion remains

    (2pi/N)log|<K>_N| -> Vol(S^3 minus K).

No Hilbert-90 calculation or rigidity of a finite-level unpointed
intertwiner fixes that pairing by itself. A proof must identify its
integral pointing, its global normalization, and its archimedean norm.
The identities above do not establish that assertion for a knot class.

`experiments/audit_cyclotomic_normalization.py` checks distribution,
Galois certificates, inversion, and the series and norm estimates.
They are diagnostics for the uniform proofs, not replacements for them.
