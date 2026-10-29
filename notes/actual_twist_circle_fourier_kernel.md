# A polynomial-cost Fourier kernel for every original twist block

29 October 2026. Every signed power of the original equal-color
crossing has an explicit Chebyshev expansion whose coefficient mass
is O(N(1+|ell|)). It retains the full Casimir Hermite jets, including
the odd simple node. For a full twist ell=2p this supplies the
coefficient kernel for the entire ordinary circle-color packet,
rather than an inversion of a single complete-color circle.

The [literal mixed-color circle calculation](actual_crossing_circle_source_and_filling.md)
identifies the displayed operators with the original pivotal
encircling sources. This is therefore an exact quantitative source
transformation at arbitrary width, with the marked cut unchanged.
Polynomial coefficient mass does not prevent cancellation in the
resulting filling sum, and does not prove geometric survival.

## 1. The complete local spectral data

Use N>=2, d=N-1, q=exp(pi*i/N), Q=q^2, kappa=q^(d^2/2).
The original pair Casimir Omega has polynomial

    P_N(z)=2T_N(z/2)+2,
    c_k=w_k+w_k^(-1), w_k=q^(2k+1), 0<=k<N.

Its distinct nodes have multiplicity two, except c=-2 when N is
odd. The original full checked crossing is R=kappa r_N(Omega),
with the original, already derived values and jets

    nu_k=r_N(c_k)=(-1)^k q^[k(k+1)],
    r_N'(c_k)/nu_k=-(d-2k)/[2(w_k-w_k^(-1))]             (1)

at double nodes. The possible simple node has only the value
condition. These are the complete physical spectral data; there
is no semisimple projection. For a negative power use the actual
inverse crossing, not its adjoint.

For any integer ell let f_(N,ell) be the unique polynomial of degree
less than N representing r_N^ell modulo P_N. Negative powers exist
because every nu_k is nonzero. Define finite data

    h_k=nu_k^ell,
    d_k=-(ell/2)(d-2k) h_k.                             (2)

At double nodes, d_k=(w_k-w_k^(-1))f'(c_k). At the odd simple
node d-2k=0 and w_k-w_k^(-1)=0, so d_k=0 without prescribing an
additional derivative. All |h_k|=1 and |d_k|<=|ell|N/2.

## 2. Exact Fourier-Hermite interpolation

Take the marked finite Fourier transforms

    H_n=(1/N)sum_k h_k w_k^(-n),
    D_n=(1/N)sum_k d_k w_k^(-n), 0<=n<N.                (3)

Then the COMPLETE polynomial is

    f_(N,ell)(z)=a_0+sum_(n=1)^d a_n 2T_n(z/2),
    a_0=H_0,
    a_n=[D_n+(N-n)H_n]/N, 1<=n<N.                     (4)

Here is a direct proof, avoiding a conditioned confluent Vandermonde
inverse. Set g(w)=f(w+w^(-1)). Its Laurent coefficients are a_0 and
the symmetric pair a_n at exponents n and -n. Since w_k^N=-1,
the node values and logarithmic derivatives have Fourier aliases

    H_n=a_n-a_(N-n),
    D_n=n a_n+(N-n)a_(N-n), 1<=n<N,
    H_0=a_0, D_0=0.                                   (5)

Solving the two equations gives (4). The paired nodes k,d-k have
the same h and opposite d, so the compatibility conditions for
(5) are automatic. At n=N/2, when present, H_n=0 and the second
equation still gives the correct coefficient. At the odd simple
node the logarithmic derivative of every such g is zero. Thus
(4) imposes exactly the N original Hermite conditions, with no
extra endpoint constraint, at every even and composite level too.

Equation (4) immediately gives the uniform coefficient bounds

    |a_0|<=1, |a_n|<=1+|ell|/2.                        (6)

No separation bound for nearby Casimir nodes is needed.

## 3. Full circle-color coefficients and their norm

Let U_j denote the second-kind Chebyshev polynomial, U_0=1,
U_1=z when its argument is z/2. Put a_N=a_(N+1)=0 and define

    beta_j=(-1)^j(a_j-a_(j+2)), 0<=j<N.                (7)

The identities 2T_n=U_n-U_(n-2), n>=2, and 2T_1=U_1 give

    f_(N,ell)(Omega)
       =sum_(j=0)^d beta_j (-1)^j U_j(Omega/2),
    R^ell=kappa^ell sum_(j=0)^d beta_j L_(j+1),
    L_(j+1)=(-1)^j U_j(Omega/2).                       (8)

All phases, including kappa^ell, are retained. Summing (6) gives

    sum_(j=0)^d |beta_j| <= 2N(1+|ell|/2).             (9)

For ell=2p, (8) is an exact full-twist filling kernel of mass at
most 2N(1+|p|). The separate
[physical circle proof](actual_crossing_circle_source_and_filling.md)
realizes L_j as the actual ordinary pivotal j-color encircling
operator, including its original framing and trace. A single L_N
is not inverted or declared
sufficient; the whole degree-<N basis occurs in (8).

This bound holds uniformly in N and p, including negative twists and
all gcd/parity cases. There is no division by p or by a Gauss sum.
For ell=0 the expansion reduces exactly to L_1=I.

For full twists the data in (3) are particularly explicit:

    h_k=Q^[p k(k+1)], d_k=-p(d-2k)h_k,
    H_n=(1/N)sum_k Q^[p k(k+1)]q^[-n(2k+1)].            (10)

The corresponding D_n is the SAME finite quadratic sum with its
retained linear normal weight -p(d-2k). Dropping this weight would
erase the derivative data of the original crossing and generally
change the invariant. Formula (10) specifies the filling phases
before any large-N or long-filling analysis.

## 4. Simultaneous filling and the actual remaining theorem

Replace a fixed collection of disjoint twist blocks R^(2p_i) by
(8) BEFORE any exterior contraction. Distributivity gives the exact
sum of the same original tensor diagram with circle operators
L_(j_i) in those slots. All spectator tensors, the original marked
cut and peripheral/framing line retain their order and values.
The total coefficient mass is at most

    product_i [2N(1+|p_i|)].                            (11)

For a fixed number of blocks this is polynomial when the p_i are
fixed; more generally its logarithm is o(N) whenever
sum_i log(1+|p_i|)=o(N). Thus no exponential coefficient cost is
introduced by retaining the complete circle-color data.

Together with the physical circle identification, this supplies
an original-source input for simultaneous crossing-circle fillings.
It does not identify a fixed complete-color augmented-link scalar
with this packet, nor replace its trace by a different invariant.

The next geometric survival question is substantive: obtain a
nonzero selected geometric period for that actual MIXED-COLOR
augmented source and control the coherent filling sum (10). Taking
absolute values in (11) gives only a maximum over the base packet;
it does not automatically yield the smaller filled-manifold volume.
No broad original-knot volume theorem is claimed by this expansion.

The [complete Fourier--Hermite Gram](actual_filling_fourier_hermite_gram.md)
turns these coefficients into an explicit positive Cauchy metric.
Its exact dual cost is 1+ell^2(N^2-1)/(12N^2), uniformly bounded
in N for a fixed twist. A literal original normalization insertion
also proves that this metric's energy can be excessive even when
the final knot is hyperbolic. A sharp geometric energy estimate
requires more than the controlled filling-source norm.

[Audit](../experiments/audit_actual_twist_circle_fourier_kernel.py):
PASS 81 signed full-physical crossing-power comparisons at N=2,...,10
and 64 complex full-Hermite/coefficient-mass cases through N=48.
Independent proof review checked both Fourier aliases, the even
middle index, the odd simple node, and the circle-basis conversion.
