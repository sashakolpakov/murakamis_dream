# A shrinking-arc inner product for the original terminal packet

29 October 2026. Weighted Cauchy does not require the full Fourier
circle. The exact evaluation norm on a suitably weighted arc is
polynomial, uniformly in the arc width. This constructs an additional
positive metric on the original complete module. It does not by itself
bound its energy by hyperbolic volume.

## 1. An exact polynomial evaluation theorem

Let f(t)=sum_(j=0)^d z_j t^j, let a>0, and write

    t_a(s)=(1+i a s)/(1-i a s),  -1<=s<=1,
    Q_a(s)=(1-i a s)^d f(t_a(s)).                       (1)

The latter is an ordinary polynomial of degree at most d. Define

    E_(a,d)(f)=1/2 integral_(-1)^1 |Q_a(s)|^2 ds
             =1/2 integral_(-1)^1
                    (1+a^2 s^2)^d |f(t_a(s))|^2 ds.     (2)

Then the SHARP all-polynomial evaluation inequality is

    |f(1)|^2 <= kappa_d E_(a,d)(f),
    kappa_d=(2m+1)^2 [binom(2m,m)/4^m]^2 <= d+1,
    m=floor(d/2).                                      (3)

In particular the exact constant does not depend on a. A very small
arc need not have an exponential dual-source cost.

Proof. Let P_j be the Legendre polynomials, normalized by P_j(1)=1.
Integration by parts in their Rodrigues formula gives

    (1/2) integral P_j P_k = delta_(j,k)/(2j+1),
    P_(2r)(0)=(-1)^r binom(2r,r)/4^r, P_(2r+1)(0)=0.

Expand Q_a in this orthogonal basis and apply Cauchy at zero. Its
evaluation norm squared is

    sum_(r=0)^m (4r+1) b_r^2=(2m+1)^2 b_m^2,
    b_r=binom(2r,r)/4^r.

The equality telescopes using b_r/b_(r-1)=(2r-1)/(2r).
Induction gives b_m^2<=1/(2m+1), hence the last bound in (3).
Equality in the evaluation bound holds for the reproducing polynomial
sum_(j=0)^d (2j+1)P_j(0)P_j(s). The map f->Q_a is an invertible
linear map between degree-d polynomial spaces: its inverse is the
inverse fractional linear substitution with its denominator cleared.
Thus the constant is sharp for every a>0.

For the unweighted normalized arc energy

    E^0_(a,d)(f)=1/2 integral_(-1)^1 |f(t_a(s))|^2 ds,

the same proof gives

    |f(1)|^2 <= kappa_d (1+a^2)^d E^0_(a,d)(f).           (4)

If d=O(N) and a=N^(-A), A>0 fixed, this extra factor is exp(o(N)).
For a=1/N it is 1+O(1/N). The measure in (2) is specified in the
Cayley coordinate s; it is not silently replaced by uniform angle.

## 2. The explicit finite Gram and its original co-source

Let V_(k,j) be the coefficient of s^k in

    (1+i a s)^j (1-i a s)^(d-j),

and let H_(k,l)=0 for k+l odd and 1/(k+l+1) for k+l even.
The coefficient-space Gram of (2) is exactly

    W_(a,d)=V^* H V >0.                                 (5)

All entries are explicit finite rational combinations of powers of a
and i. For the row e=(1,...,1), equation (3) says more precisely

    e W_(a,d)^(-1) e^* = kappa_d.                        (6)

This is an algebraic inner product construction, not an unknown period
inserted into the definition of its own norm. Its condition number
can be large; no polynomial condition number is asserted or needed.

Now use the ACTUAL original terminal packet rows T_j from
[the complete terminal construction](actual_terminal_packet_positive_gram.md).
They satisfy sum_j T_j=lambda U on every input of the complete module,
and are defined before the preceding braid B is chosen. Put

    f_v(t)=sum_j t^j T_j v,
    G_(a,epsilon)=T^* W_(a,d) T+epsilon I, epsilon>0.      (7)

This is a positive definite metric, including when T is singular.
Its original final contraction b=sum_j T_j obeys

    b G_(a,epsilon)^(-1) b^* <= kappa_d <= d+1.           (8)

For example, factor W=A^*A and use (6) and Cauchy on ATv.
The resulting inequality holds for every v; its optimal squared
dual norm in G is therefore at most kappa_d. No inverse of T is used.

For the complete unchanged original source v=B w_0,

    |K_N|^2 <= |chi_N|^2 kappa_d
                [E_(a,d)(f_v)+epsilon ||v||^2].          (9)

All external and peripheral factors remain in chi_N. Taking
epsilon=exp(-N^2) makes the added term negligible for every fixed
original braid, by the already proved exp(O(N log N)) source bound.
At arbitrary fixed plat width one can record a fixed number r of
physical colors, use the product arc measure, and apply (3) in each
variable. The dual cost is product kappa_(d_j)<=product(d_j+1),
still polynomial. No source channel is removed.

For the original figure-eight, T_j Bp=|(Q;Q)_j|^2>=0 exactly.
On every unit-circle arc |f_v(t)|<=f_v(1). Equations (2)--(3) give

    |K_N|^2/kappa_d <= E_(a,d)(f_v)
                  <=(1+a^2)^d |K_N|^2.                 (10)

Hence any a=N^(-A), A>0, has the same known sharp benchmark rate.
This uses the original finite positive formula; it is not a general
noncancellation assertion.

## 3. Precisely what localization does and does not accomplish

With a=1/N, the extra Cartan parameter in the norm stays within O(1/N)
of its original value t=1. The comparison no longer requires a sharp
estimate at every fixed t on the unit circle. This is a useful change
in the proposed metric, not a proof that the local energy is sharp.

Even a degree-one polynomial can have exponentially amplified local
energy. Set f_N(t)=1+exp(cN)(t-1), c>0, use d=1 in (1), and obtain

    Q_a(s)=1+i a s[2exp(cN)-1],
    E_(a,1)(f_N)=1+(a^2/3)[2exp(cN)-1]^2.               (11)

For a=N^(-A) this has rate 2c although f_N(1)=1. This is an
elementary diagnostic, not a knot counterexample. Polynomial degree,
localization and controlled evaluation norm alone do not bound jets
of the original source. Using d=N-1 only increases the energy of this
same f by the weight (1+a^2s^2)^(d-1), so the issue also occurs in
the degree-N ambient space.

Conversely choosing an excessively small arc can make the energy
arbitrarily close to the unknown |K_N|^2. That would be an exact
reformulation, not an independent geometric estimate. The useful
remaining assertion is a source-derived bound on (2), at a prescribed
scale such as a=1/N, by exp[N Vol(M)/pi+o(N)].

There is also no automatic compactness argument from t->1. The
[complete coupon kernel](actual_terminal_effective_cartan_kernel_and_graph.md)
has an additional orbital channel; its Fourier coordinates can escape
while its character coordinates remain bounded. Arc endpoints need
not satisfy the full-circle interior phase stationarity equation.
Both the calibrated action and accessibility of such contributions
remain to be checked before using representation volume.

The finite Cauchy step, including an explicit metric and polynomial
dual cost, is proved. The sharp global quantum-energy estimate and
geometric survival remain open.

## 4. A quantitative test for amplified source derivatives

The same finite polynomial argument gives a useful lower bound on
the proposed energy. For d>=1 let r=floor((d-1)/2) and put

    D_d=sum_(j=0)^d (2j+1)P'_j(0)^2
       =[(2r+1)(2r+3)b_r]^2/3 <= (d+2)^3/3.            (12)

Indeed P'_(2r+1)(0)=(-1)^r(2r+1)b_r; the sum telescopes as in
Section 1. Evaluation of the derivative at zero therefore gives

    E_(a,d)(f) >= a^2 |2f'(1)-d f(1)|^2 / D_d.          (13)

Here Q'_a(0)=i a[2f'(1)-d f(1)] exactly. The upper bound on D_d
follows from b_r^2<=1/(2r+1), 2r+1<=d and 2r+3<=d+2.
For the unweighted arc energy divide the right side by (1+a^2)^d.
Thus an actual source with an excessive exponential first derivative
would refute sharpness of every polynomially shrinking arc in this
metric family. A numerical growth trend alone does not prove that
derivative exponent.

[Audit](../experiments/audit_actual_shrinking_arc_cauchy_metric.py):
PASS nine exact rational Gram inverses, sharp evaluation constants
and derivative norms; seven complete original terminal source Grams,
positive completions and benchmark energy comparisons; and the exact
degree-one localization diagnostic. The audit uses rational arithmetic
for (6) and independent polynomial quadrature for the complex source.
