# A source-exact quotient for normalization boundary currents, including normal jets

29 October 2026. There is a genuine class of singular relative-source
components that can be eliminated before positivity: the zero-pointing
part of a complete visible Markov normalization cell. This is an
operator identity with spectators retained. It composes through any
fixed forest of such cells at arbitrary braid width, even when the
spectator coefficients are not scalar or mutually commuting.

For the original full-Psi radial current, even at radius one, every
normalized Mellin Taylor coefficient of its pointed scalar is at most
N/(2pi). The entire radial operator on a nilpotent contraction has
normalized coefficients bounded by H_N/(2pi). On a fixed radius below
one, oscillation gives the sharper bound C r! log(eN)^r for raw pointed
derivatives. Thus these actual logarithmic normal currents have no
additional exponential normalization cost after contraction.

This extends the known normalization-cell evaluation and its tame
radial value to an operator-valued relative-current quotient with a
quantified normal germ. It does not eliminate internal head/cap alias
currents, identify Mellin order with the knot meridian, or prove a
sharp bound for the remaining knot period.

## 1. The exact selected cell, with all original scalar factors

Use the literal positive equal-color factorization and pivot of
[the Markov source proof](actual_markov_ray_normalization_and_pruning.md):

    R+=kappa C D U C^-1,
    g_b=x^(-d) Q^(-b), d=N-1,
    alpha=kappa x^(-d).

For every diagonal function r of the second RELATIVE channel,

    Tr_new[(I tensor g) kappa C D U (I tensor r) C^-1]
                         =alpha r_0 I.                    (1)

The trace has NO additional 1/N. The original sole cut average, turns,
marked row and full peripheral/framing line are unchanged. Zero framing
cancels the original alpha only when the complete original Markov cell
is contracted. A current with r_0 != 1 keeps that extra factor.

For completeness, the direct finite coefficient proof of (1) computes
the k-th channel's cut diagonal as

    alpha x^(-2k) Q^(-k) (1;Q)_k = alpha delta_(k,0).

Its intermediate q-binomial identity is

    sum_(j=0)^s (-1)^(s-j) Q^[j(j+1)/2]
       (Q^(a-j+1);Q)_s/[F_j F_(s-j)]=(-1)^s.

Expand the Pochhammer as a polynomial in Q^a. All its positive-degree
coefficients contain (Q^(1-ell);Q)_s and vanish; the constant is the
right side. A second finite binomial sum gives (1). This proof retains
the forbidden-index zeros of the original finite head and works at
all levels, including even and composite N.

## 2. Operator-valued pointing and exact cancellation of its kernel

Let S be ANY spectator space. Replace r_k by arbitrary operators
A_k on S, acting at the same relative-channel slot in (1). Then

    Tr_new[(I tensor g tensor I_S)
      kappa (C D U tensor I_S)
      (sum_k I_cut tensor |k><k| tensor A_k)
      (C^-1 tensor I_S)]
                         =alpha I_cut tensor A_0.          (2)

To prove (2), expand in any basis of End(S) and apply (1) to every
coefficient. No positivity, simultaneous diagonalization or assumption
about an exterior knot value enters. In particular A_k may be coupled
to arbitrary tensors outside the cell, but not silently moved through
the cut head or the inside of C.

Define the pointing map epsilon(A)=A_0. The difference

    A_k-A_0 for every k                                  (3)

is annihilated by the COMPLETE cell. Thus a source-current packet may
be replaced by its pointing after the whole cell has been assembled.
It is not necessary for the norms of its individual channels to be
small. Equation (2) remains valid after arbitrary exterior composition
and the original full marked functional.

The same statement holds coefficientwise for a holomorphic or
meromorphic normal germ A_k(sigma), on a common domain where the
cell expression is defined. If epsilon(A(sigma)) is identically zero,
ALL its normal Laurent/Taylor coefficients pair to zero. A pole in
separated channel pieces is canceled only after their common complete
packet is formed; (2) is not a prescription to drop those poles first.

Now suppose a fixed tensor diagram contains a forest of visible cells:
each leaf has the precise form (2), and after contracting a leaf the
next prescribed cell has that form. Contract leaves in this order.
Induction proves that every zero-pointing leaf packet disappears
exactly, and each surviving cell is replaced by its specified A_0,
in the original operator order. This is an all-width source theorem,
not a claim that every braid admits such a pruning or that arbitrary
internal projectors can be slid to a cap.

## 3. The actual radial current and its Mellin-normal germ

Fix a real 0<R<1, independent of N. Let Psi be the fully normalized
positive function from
[the original circle/ray source](actual_modular_dilog_circle_and_boundary_source.md).
The actual positive atom's radial part in the displayed cell has
channel coefficients

    r_k(0)=-N Q^(d-k) E_(d-k)(R)/F_k,

where

    E_a(R)=1/(2pi*i) integral_0^R
           Psi(log t)/(1-t^N) * t^(N-a-1) dt.

Consequently its pointed scalar is EXACTLY

    h_N(0)=-N Q^-1 E_d(R).                              (4)

It must be retained: the original ray group is h_N(0) times the
whole exterior invariant, and need not have a smaller exponential
rate. The circle group is (1-h_N(0)) times that same exterior.

There is a natural logarithmic normal of this specified relative
radial current: multiply its radial integrand by t^(-sigma). For
Re sigma<1 set

    h_N(sigma)=-N Q^-1/(2pi*i) integral_0^R
           Psi(log t)/(1-t^N) * t^(-sigma) dt.             (5)

This is holomorphic there, by integrable domination on compact
sigma-sets. Its derivatives are the literal insertions
(-log t)^r in the original radial current. At sigma=0 (5) is (4),
with the original phase and coefficient, not a rescaled boundary state.
Sigma is a Mellin-normal coordinate of this atom source. It is NOT
being identified with the knot's meridian parameter or with a normal
Cartan coupon elsewhere in the word.

## 4. Uniform normal currents through radius one

The exact real-ray modulus, with the complete central factor retained,
is

    |Psi_epsilon(log t)|^2=(1-t)(1-t^N), 0<t<=1.

Consequently its quotient has modulus

    A_N(t)=sqrt((1-t)/(1-t^N))<=1, A_N(1)=1/sqrt(N).   (6a)

There is no pole at t=1. This proves, for EVERY 0<R<=1 and r>=0,

    |h_N^(r)(0)|/r!
       <=N/(2pi*r!) integral_0^R A_N(t)(-log t)^r dt
       <=N/(2pi).                                       (6b)

For Re sigma<1 it also proves

    |h_N(sigma)|<=N/[2pi(1-Re sigma)].                    (6c)

All normal coefficients are those of the actual Mellin current (5).
No fixed-distance-from-one assumption, separated root branch, or
pointwise phase approximation enters (6a)--(6c).

There is an operator version BEFORE the normalization cell is closed.
For a literal nilpotent contraction T on its supplied finite relative
head, T^N=0 and ||T||<=1, retain the full source correction

    E_sigma(T)=epsilon/(2pi*i) integral_0^R
      Psi_epsilon(log t)/(1-t^N) * t^(N-sigma-1)
                          sum_(a=0)^d t^(-a)T^a dt.       (6d)

It is a holomorphic operator germ for Re sigma<1 and includes every
original finite resolvent coefficient. Differentiation and (6a) give

    || E_sigma^(r)(T)|_(sigma=0) /r! ||
       <=(1/(2pi)) sum_(j=1)^N j^(-r-1)
       <=H_N/(2pi), r>=0.                               (6e)

The first inequality uses integral_0^1 t^(j-1)(-log t)^r dt=r!/j^(r+1).
Similarly, for |sigma|<=rho<1 the whole operator germ is at most

    [1/(1-rho)+H_N]/(2pi).                               (6f)

This applies in the stated nilpotent-contraction metric. No assertion
is made that every conjugated interior atom is a contraction in one
common physical metric; changing that metric or composing with an
unrestricted exterior still requires its actual estimates.

The first Mellin pole at the other endpoint is also explicit. The
actual small-t expansion starts with Psi(log t)=1+O(t), up to higher
logarithmic terms which do not affect this first pole. Therefore

    Res_(sigma=1) E_sigma(T)=-epsilon T^d/(2pi*i),
    Res_(sigma=1) h_N(sigma)=N Q^-1/(2pi*i).              (6g)

Subtract the constant term in the a=d coefficient of (6d); the
remaining integral is holomorphic through sigma=1. Every other
coefficient is already integrable there. This proves (6g), with its
sign and full original normalization. It is a retained source current,
not zero. For a fixed ordered collection of such atom endpoints the
iterated residues are the corresponding ordered products of T_j^d;
their norm is at most one in the supplied contraction metrics.
After the displayed normalization-cell pointing their scalar cost
is polynomial in N. No reordering of noncommuting atoms is used.

For a fixed normalization forest, (6b) bounds an independent normalized
multijet by (N/(2pi))^L. If all cells share one normal coordinate, the
order-r coefficient has the additional count binom(r+L-1,L-1). Thus
even growing normalized jet orders cost only a polynomial in N and r
for this fixed forest. These coefficients may be nonzero; they are
retained scalar source factors, not declared negligible.

### Sharper pointed estimate at a fixed interior radius

There is C_R, independent of N, such that

    sup_(|sigma|<=1/log(eN)) |h_N(sigma)| <= C_R.           (6)

Here is a direct proof, including the t=0 endpoint. The exact
small-disk full-Psi expansion, with one fixed derivative, gives

    Psi(log t)/(1-t^N)=a_N(t) exp[-iN phi(t)],
    phi(t)=Li2(t)/(2pi),
    ||a_N||_(C^1[0,R])<=C_R,
    0<c_R<=phi'(t)<=C_R, |phi''(t)|<=C_R.               (7)

It follows from the normalized full function, including its central
period; the proof and two-derivative version are given in the Markov
source note. The finitely many small levels can be absorbed in C_R.

Split the integral at 1/N (or at R if R<1/N). On the first interval,
with rho=1/log(eN),

    N integral_0^(1/N) |t^(-sigma) a_N(t)| dt
      <=C_R N^(Re sigma)/(1-Re sigma)<=C_R.

On [1/N,R], integrate the oscillatory exponential once by parts,
keeping BOTH endpoint terms. Multiplication by N cancels its 1/N.
The endpoint terms are bounded since N^(Re sigma)<=e and R is fixed.
The derivative of a_N/phi' gives a bounded integral. The only remaining
term is bounded by

    C_R |sigma| integral_(1/N)^R t^(-Re sigma-1) dt
      <=C_R |sigma| log N max(1,N^(Re sigma))<=C_R.

This proves (6). No claim of pointwise smallness of the original ray
has been used, and its lower endpoint contribution is not discarded.
In particular Cauchy's formula on that normal disk gives

    |h_N^(r)(0)| <= C_R r! log(eN)^r, r>=0.               (8)

For a fixed forest of L cells with independent normal coordinates,
the resulting pointed scalar germs are products in the specified
operator order. In the scalar radial case their multijets satisfy

    |partial^nu product_(j=1)^L h_(N,j)(0)|
         <=C^L product_j(nu_j!) log(eN)^(|nu|).           (9)

For fixed L and fixed total order this is polynomial (indeed
polylogarithmic). Raw derivative orders with
|nu| log((|nu|+1)log(eN))=o(N) still cost exp(o(N)); normalized
Taylor coefficients need only |nu| log log(eN)=o(N).

The conjugate radial integral has the same analytic estimate. The
operator-valued pointing assertion here is for the displayed POSITIVE
cell. A negative cell may be contracted as its complete original
normalization, but no unstated negative arbitrary-channel formula is
assumed. In particular no original pivot is replaced by a fresh average.

## 5. Scope for the global contour question

This is a source-specific cancellation before positivity, valid with
all original spectators and marked data. The full radial current is
not thrown away: its pointed scalar and its controlled normal germ
remain. The zero-pointing part vanishes as a complete original-source
pairing, without assuming a thimble comparison.

The operation can remove normalization boundary components even when
separate circle/ray pieces individually carry the whole knot rate.
It changes individual-state evaluation tests and so evades the genuine
obstruction to a UNIVERSAL cotangent chart homotopy. Its hypothesis is
the literal visible-cell/forest structure, not merely a rational
spectral relation or a matching character value.

For genuinely internal head, transfer and alias clusters that structure
has not been proved. Their complete currents may not lie in this
pointing kernel. No sharp upper bound for the remaining pruned period,
no all-face descending cycle, and no original-source lower bound follow
from (1)--(9). Extending source-specific contraction to those internal
clusters remains substantive work.

[Audit](../experiments/audit_actual_normalization_boundary_current.py)
checks the operator-valued all-input identity with original crossings,
ordinary pivots and marked exteriors, and independently evaluates the
full-Psi Mellin current and its first logarithmic normal derivatives.
