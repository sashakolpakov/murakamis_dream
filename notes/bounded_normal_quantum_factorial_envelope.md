# Uniform factorial bounds through bounded root-normal confluence

29 October 2026. Fixed-order root-normal coefficients of explicit quantum
factorial sums have the SAME positive factorial envelope up to a polynomial
in N. Indices may exceed N by any fixed multiple; every root zero is
removed explicitly before differentiating. This extends the below-N
derivative estimate in
[the complete Casimir packet](actual_complete_casimir_hermite_packet.md),
section 5, to the factorials appearing in generic higher-channel formulas.

This is an upper estimate for the original complex coefficients. It does
not remove their phases, prove a nonzero geometric leading coefficient,
or make a matrix inverse tame merely because its size is bounded.

## 1. Root zeros and their exact leading coefficients

Fix an integer C>=1. For N>=2 set

    q_N=exp(pi i/N), Q_N=q_N^2, zeta(h)=q_N exp(h/N),
    F_n(h)=product_(j=1)^n (1-zeta(h)^(2j)), 0<=n<=C N.

Write n=kN+r, 0<=r<N. Exactly k factors vanish at h=0, those with
j=mN, 1<=m<=k. Define the holomorphic nonzero germ

    H_n(h)=h^(-k) F_n(h).

Let s_r=product_(j=1)^r |1-Q_N^j|, with s_0=1. Then EXACTLY

    |H_n(0)|=2^k k! N^k s_r.                         (1)

Indeed the zero factors have leading coefficients -2m, while each
full nonzero residue cycle has product magnitude N. No factor that
vanishes at a multiple of N is silently set to one.

## 2. A common complex disk controls the germ and its inverse

There are positive constants c_C,B_C,K_C depending only on C such that
for every N,n above and |h|<=c_C/N,

    K_C^(-1) N^(-B_C)
       <= |H_n(h)/H_n(0)| <= K_C N^(B_C).            (2)

In particular these disks have no further zeros after removing h^k.
One may take c_C=1/[32(C+1)^2]; the exact polynomial exponent is not
needed for the application.

Proof. For j not divisible by N, put r_j=j mod N and
m_j=min(r_j,N-r_j). The relative factor is 1+u_j, where

    u_j=-Q_N^j(exp(2jh/N)-1)/(1-Q_N^j).

Since j/N<=C and |h|<=c_C/N,

    |exp(2jh/N)-1|<=4C|h|,
    |1-Q_N^j|>=4m_j/N,
    |u_j|<=C c_C/m_j<1/2.                          (3)

Each nonzero residue occurs at most C+1 times. Thus

    sum_j |u_j| <= 2C(C+1)c_C(1+log N).

The absolutely convergent branch of log(1+u_j) has modulus at most
2|u_j|. Summing gives both polynomial bounds for the product and its
inverse. The removed zero factor, normalized by its value at zero, is

    (1-exp(2mh))/(-2mh)=exp(mh) sinh(mh)/(mh).

There are at most C of these factors. On the stated disk they and
their inverses are bounded by constants depending only on C. This
proves (2), including r=0, N=2 and every quantum-level parity.

For every fixed derivative order D, Cauchy's estimate consequently gives

    |H_n^(j)(0)| <= K_(C,D) N^(B_C+j) |H_n(0)|,
                   0<=j<=D,                        (4)

and the analogous statement for H_n^(-1). This proof handles endpoint
indices without a positive distance from 0 or N.

## 3. Uniform Laurent-coefficient bound for a factorial ratio

Fix also J,A,D. Consider any term

    R(h)=zeta(h)^b product_(a=1)^J F_(n_a)(h)^(eps_a),
    |b|<=A N^2, |eps_a|<=A, 0<=n_a<=C N,             (5)

with integral b,eps_a. Write n_a=k_a N+r_a and put
nu=sum_a eps_a k_a. After removing h^nu the term is a nonzero
holomorphic germ on the disk in section 2. Its normalized modulus
and inverse are polynomially bounded, uniformly in every index.
The monomial causes only constant growth on this disk:

    |exp(bh/N)|<=exp(A c_C).

Its leading absolute coefficient is

    2^nu product_a(k_a!)^(eps_a) N^nu
                             product_a s_(r_a)^(eps_a).

The k_a and nu are bounded independently of N. Hence for every integer
-D<=j<=D there are uniform constants K,B with

    |[h^j] R(h)| <= K N^B product_a s_(r_a)^(eps_a). (6)

To see this directly, the coefficient is zero for j<nu; otherwise apply
Cauchy to h^(-nu)R at order j-nu, which is uniformly bounded. The
polynomial factor in (6) includes all powers N^nu and derivative costs.
One can also allow any fixed rational powers of the nonzero normalized
H_n after choosing their analytic branches; source formulas with actual
Laurent coefficients must still have their integral total valuations.

Changing back to zeta-q_N introduces only further polynomial factors
at any fixed order, because zeta=q_N exp(h/N) has a locally invertible
Taylor series with coefficients of polynomial size in N.

## 4. Coherent sums and what bounded confluence does establish

Let S_N(h) be a sum of at most a fixed polynomial in N terms of form
(5), with uniformly bounded C,J,A. For any fixed finite set of Laurent
coefficients, termwise (6) gives

    |[h^j] S_N(h)|
        <= K N^B sum_terms product_a s_(r_a)^(eps_a). (7)

The same assertion holds for a fixed number of sums, products and fixed
normal derivatives of such expressions. Thus a prescribed bounded-jet
source specialization does not introduce an unrecorded exponential
factor into its EXPLICIT factorial majorant. Root pole cancellations
may improve this upper bound; they are not assumed to be absent.

The uniform elementary estimate

    log s_r=N J(r/N)+O(log N),
    J(x)=integral_0^x log(2sin(pi t))dt,

then expresses (7)'s rate by the maximum of the SAME finite sum of
J(r_a/N) with coefficients eps_a. The error remains O(log N) per term.
This is valid for all indices, including r_a=0 and N-1. It follows,
for example, by subtracting log t+log(1-t) from the integrand and
using monotone sum/integral bounds on the two logarithms.

This result addresses a specific obstacle in the saturated generic
source: a derivative order growing with N could change the exponential
estimate drastically. A proved bound independent of N on the required
normal order removes that obstacle for explicit factorial kernels.

Three separate tasks remain:

* A saturated frame or its inverse must actually be given by controlled
  expressions of the stated kind. A bounded matrix size or bounded
  number of Smith steps alone does not bound inverse determinants.
* The resulting factorial action must be matched to the ACTUAL
  geometric angle constraints before Casson--Rivin supplies its sharp
  volume maximum. An arbitrary factorial envelope need not be sharp.
* An upper envelope cannot prove survival of the original coherent
  coefficient. Even a bounded derivative may annihilate a leading
  saddle amplitude. Its nonzero coefficient must be checked with all
  phases, endpoints and original source data retained.

Accordingly this is a uniform normal-coefficient estimate, not a new
unconditional quantum volume theorem. Its proof is analytical; no
finite numerical sample is used as a substitute for (1)--(7).
