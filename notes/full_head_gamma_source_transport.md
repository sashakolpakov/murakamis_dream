# A uniform comparison of the whole finite source-factor lattice

Research proof, 27 October 2026. The middle-component Gamma comparison
extends to every color in the actual finite head. A complementary Weyl
chart is essential in the upper half: using the same partial product
there would introduce extra periodic zero divisors.

The result is an exact diagonal unit comparison, uniformly I+O(1/N)
in the full head, including all fixed normal resonance divisors. It
compares source factors and their dual fractional lattices. It does
not identify the two crossing representations or the selected knot
periods. The surviving crossing response is studied separately.

## 1. Actual factors and the two root Weyl charts

Use the actual frame of
[the integral-color source](integral_color_global_q_difference_source.md)
and [its whole Gamma normal](whole_gamma_frame_profile.md). Put

    c=2pi*i, n=N-1, L=floor(n/2), H_0=c/N,
    H=H_0+ca/N^2, b=a/(1+a/N), Hb=ca/N,
    M_col=exp(Hb/2)=-q^N, q=exp(H/2),
    M_+=exp(H_0b/2), M_-=M_+^(-1), Q_0=exp(H_0).

For j=0,...,n, the retained source-frame residual is

    V_(N,j)={n choose j}_(q,sym)/M_col^j.               (1)

Every q-binomial in (1) means its Laurent-polynomial value,
including parameters where a factorial quotient is 0/0.
At such parameters V need not be a unit.

The partial root Weyl factors are the actual functions

    beta_j(M)=(M^2 Q_0;Q_0)_j/(Q_0;Q_0)_j.              (2)

Their denominators are nonzero for j<N. They are the factors
in the diagonal matrix of the exact root Weyl intertwiner,
whose entries are M^j/beta_j(M), with the original meromorphic
and source-lattice interpretation. The marked full half-adapter
is beta_L at odd N, and [(1+iM)/(1+i)]beta_L at even N.
The extra even factor is retained when passing to that scalar.

Define the complementary target source-factor section by

    B_(N,j)=beta_j(M_-),                         j<=L,
    B_(N,j)=M_+^(n-2j)beta_(n-j)(M_-),           j>L.    (3)

These are concrete root Weyl factors and their retained character,
not values of an arbitrary replacement invariant.

The two formulas are the actual norm/complementary charts. If

    H_N(cb)=S_N(M_+^2)/(N M_+^n),

the exact identity is

    beta_j(M_+) beta_(n-j)(M_-)
                    =M_+^(2j-n) H_N(cb).               (4)

Consequently the upper expression in (3) obeys

    beta_j(M_+) B_(N,j)=H_N(cb).                        (5)

Thus B_(N,j) can also be written H_N/beta_j(M_+) after
canceling common factors. Formula (3), rather than division
at a zero, defines its holomorphic value.

To prove (4), transform the last n-j factors of
(M_+^2 Q_0;Q_0)_n using r->N-r. Their ratios become
M_+^(-2)(1-M_+^2Q_0^r)/(1-Q_0^r). The complete product is
S_N(M_+^2)/N. Multiplying its character gives exactly (4).
This also retains the unpaired even residue; replacing the
marked even half-adapter by beta_L alone would lose its scalar
splitting, although (2)--(5) remain valid partial-factor identities.

## 2. Exact unit comparison at every color

Let J(x)=2sinh(x/2)/x, J(0)=1. For 0<=k<=L set

    u_(N,k)=exp[-(H-H_0)bk/2]
        product_(r=1)^k
          J(H(r-b))J(H_0r)/[J(Hr)J(H_0(r-b))].           (6)

There is no even prefactor in this partial-product formula.
Define a diagonal matrix C_N(a) by

    C_(N,j)=u_(N,j),                                      j<=L,
    C_(N,j)=exp[(H-H_0)b(n-2j)/2]u_(N,n-j),               j>L.

Then, exactly for every j,

    V_(N,j)=C_(N,j) B_(N,j).                             (7)

For each compact complex a-set K, all sufficiently large N
have a neighborhood of K on which every C_(N,j) is a
holomorphic unit, C_(N,j)(0)=1, and

    sup_(a in K,0<=j<N)|C_(N,j)-1|<=A_K/N.               (8)

This assertion concerns the comparison unit, not invertibility
of V or B at their common zeros.

For k<=L the exact factorization in the Gamma theorem is

    V_(N,k)=exp(-Hbk/2) product_(r<=k)
          (1-b/r) J(H(r-b))/J(Hr).

The corresponding beta_k(M_-) has H replaced by H_0.
Their common zero polynomial is kept before canceling, and
the remaining factors give (6). All J arguments remain in a
fixed zero-free neighborhood of c[0,1/2] for a in K and large N.
In particular the unit extends through integer b.

Uniformity in k is the same double-difference estimate as in
the middle-component proof. With F=Log J and DeltaH=H-H_0,
the logarithm of one cross ratio is

    DeltaH[(r-b)F'(H_0(r-b))-rF'(H_0r)]
                                      +O_K(DeltaH^2 r^2).

The bracket is O_K(1), because its two arguments differ by b,
F' and F'' are bounded, and H_0r is bounded. Since DeltaH is
O_K(N^-2), summing at most N/2 terms gives O_K(1/N), uniformly
in the prefix length. The phase in (6) has the same bound.

For the upper half use the exact symmetric q-binomial identity

    V_(N,j)=M_col^(n-2j)V_(N,n-j).                       (9)

Combining (9) with the lower comparison gives (7); its additional
character differs from the root character by the displayed unit
in C_(N,j). Its logarithm is again O_K(1/N). This proves (8)
uniformly in the entire head, without a bulk-color restriction.

For any common diagonal coordinate or coherent metric, (8) gives

    ||C_N-I||<=A_K/N,
    ||C_N||,||C_N^(-1)||<=1+O_K(1/N).                    (10)

The bound is independent of the dimension N. It holds for every
fixed normal jet as well, on a smaller compact set, by Cauchy's
formula. No sum over colors is needed to obtain these operator
norm estimates.

## 3. The resonance divisors are matched, not inverted away

At an integer b=r with 1<=r<=L and N>2r, the exact vanishing
pattern of the residual is

    V_(N,j)=0 precisely for r<=j<=n-r.                  (11)

The same pattern holds for B, with the same simple divisors
in the parameter. Indeed beta_k(M_-) vanishes first at k=r,
and there is no other root-periodic zero in k<=L in a fixed
normal compact set for large N. The complement gives (11)
in the upper half. The unit in (7) preserves these divisors.

The exact parameter centers are a=Nr/(N-r), rather than a=r.
No quotient V/B is evaluated there to define C_N. Defining
V by a raw q-factorial quotient at an upper index would miss
its removable cancellation at these lower-order roots; its
Laurent-polynomial or complementary value in (1) is essential.

For the paired source and co-source one may work first over
the meromorphic parameter field. Equation (7) identifies the
fractional source lattices generated by V_j and B_j, and also
their inverse dual lattices. The dual comparison is C_(N,j)^(-1).
The tensor pairing is preserved before specialization. A zero
source coordinate and a pole in its dual cannot separately be
discarded: their abstract pairing is still one.

## 4. The whole source chirp costs no exponential factor in N

The exact balanced frame satisfies

    D_col^(-1)=U_col diag(V),
    (U_col)_j=q^[Nj-j(j+1)/2].                           (12)

For a root chirp (U_0)_j=exp[H_0(Nj-j(j+1)/2)/2],
use the concrete root-chart source frame U_0 diag(B). Its
comparison to the actual column frame is

    U_col diag(V)=T_N(a) U_0 diag(B),
    T_N=diag(U_col/U_0) C_N.                            (13)

The chirp ratio is exactly

    (U_col/U_0)_j
       =exp{ca[ j/(2N)-j(j+1)/(4N^2)]}.                 (14)

For a in K, T_N and its inverse have uniform operator bounds
independent of N in every common diagonal metric. At j/N->T,
its chirp tends to exp[ca(T/2-T^2/4)]. Thus the normal source
transport has a controlled whole quadratic character, and
the remaining unit tends uniformly to one.

Equations (12)--(14) transport the original source column and
dual row, including their fractional lattices and endpoint
coordinates. They do not replace either by a constant vacuum
after a change of frame. At a resonance, specialize the paired
lattices, not their separately singular coordinate arrays.

More explicitly, U_0 diag(B) is a meromorphic coordinate frame
of the same literature-defined root head. All its root operators
must be conjugated in that frame, together with the original
column psi and row phi. If Gamma_root is the resulting cut coupon,
then its comparison with the actual color-frame coupon is exactly

    psi_col=T_N psi_root,
    phi_col=phi_root T_N^(-1),
    Gamma_col=T_N Gamma_root T_N^(-1).                  (15)

The diagonal T_N commutes with J and both endpoint projectors.
Thus (15) also transports every finite position-moment insertion
and the original endpoint source probes. This does not identify
Q_col^J with Q_0^J; the two quantum parameters and the crossing
operators remain distinct. No new state or closure is defined.

## 5. What is and is not closed

The source-factor comparison now covers the entire head and
both endpoint ranges with a dimension-independent unit bound.
It retains the actual root Weyl norm, even-level mark, all
finite normal zero divisors and the quadratic chirp.

This is not a full crossing similarity. The q-normal and fixed-root
crossings can have different spectral multiplicities and different
periodic alias zeros. Their nontrivial bulk response and the
normal base must also be transported. Nor do the source bounds
bound a cancellation-prone selected knot sum. A source-preserving
comparison of the actual full knot period with its marked geometric
regulator, and its selected exponential norm, remains necessary.

The [all-level crossing spectra](crossing_normal_spectra_obstruction.md)
rule out even an arbitrary scalar-adjusted nondiagonal similarity.
The compatible constructive statement is
[the closed Euler/regulator response](quantum_normal_crossing_bulk_response.md),
which compares the actual normal geometric blocks with their
full sources. Neither statement is replaced by (15).

Verification: [audit](../experiments/audit_full_head_gamma_source_transport.py)
and [results](../experiments/full_head_gamma_source_transport_results.json).
The [independent source audit](gamma_residual_normal_profile_independent_audit.md)
also verifies the whole-head unit, chirp, zero divisors and paired
coupon/lattice identities.
