# Full first-normal bounds for all supported Racah partners

29 October 2026. This proves a uniform polynomial relative bound for the
ACTUAL first generic-q normal at every one of the 64 reflected branches
of a supported folded sextuple. The new step is a positive finite
presentation of the full generic source on face-supported branches,
including branches whose seven-factorial formula has a live `[2N]`
current. The already proved Fourier partner involution and exact first-
normal Ward equation then cover the remaining branches.

Every fixed generic normal order is controlled on the face-supported
branches. The general 64-branch conclusion is FIRST ORDER ONLY. No
completed physical recoupling norm or global volume equality follows
merely from this local scalar theorem.

## 1. Statement and source convention

Fix `N>=3`, `D=N-1`, `q=exp(pi i/N)`, and integer folded labels
`j=(a,b,c,d,e,f)` in `[0,D/2]`, with all four face sums at least `D`.
Use the SAME actual generic seven-factorial sum and normalization as
in [the reciprocal source theorem](actual_racah_partner_reflection_identity.md):

    K_B(zeta)=[N]^2 S_B(zeta)^2 product_faces Delta_B^2,
    k(B)=D_log(zeta) K_B(q).

Here B records any subset of the six changes `j -> D-j`. The original
actual source prefactors, peripheral factors and marking are not
changed. The proved root-value identity gives `K_B(q)=W_N^2>0` for
all branches.

There is an absolute constant C such that

    max_B |k(B)| <= C N^2(1+log N) W_N^2.         (1)

The local analytic square root positive at q, and the first inverse
jets of K and its square root, have corresponding relative bounds.
Every implicit constant below is independent of the supported labels,
level parity and compositeness.

A set of high bits is called face-supported if it is contained in one
of the four faces

    (a,b,e), (c,d,e), (a,d,f), (b,c,f).

For every such branch, and every fixed r, the stronger conclusion is

    |D_log(zeta)^r K_B(q)| <= C_r N^(c_r) W_N^2,                  (2)

with the analogous local square-root and inverse bounds. An opposite
pair of high bits is not face-supported; that two-bit case is tail-
free and is already covered by the positive-core theorem.

## 2. A root-unit presentation of the FULL generic source

A tail-free branch already has all fixed-jet bounds. Consider a live
face-supported branch, so all three opposite sums exceed `2D`.
Choose an opposite pair with maximal label sum, and use tetrahedral
relabeling to call it `(e,f)`, with f its high-bit edge and e its
low-bit edge. This is possible: the largest opposite sum exceeds D,
whereas an opposite pair with both bits low has sum at most D.
A face contains at most one edge of each opposite pair.

In this labeling,

    e<=D/2<=f,  e+f>=max(a+c,b+d),
    min(a,b)<=D/2,  min(c,d)<=D/2.                (3)

For the last assertion, the two remaining possible high edges are in
the face containing f. Each of the two faces containing e therefore
has at most one high external edge. The same assertion is immediate
when there are fewer than three high bits.

Set

    p=min(a+d,b+c),  s=a+b+c+d,
    h=max(|a-b|,|c-d|),  t0=s-2p,
    rA=a+b-h, rC=c+d-h,
    n=p-f, t=p+f-D.                              (4)

The exact elementary identity

    p+h=max(a+c,b+d)                             (5)

follows by expanding the difference of the maximum and minimum:
its four possibilities are `a-b,b-a,c-d,d-c`. The true triangle
conditions give `n>=0` and `h<=e`. Equations (3),(5) imply

    n<=e-h,  h+e+n<=2e<=D,  n<=t.                (6)

Furthermore

    0<=n<=rA,rC<=D,
    0<=t<=D,  0<=t0,  t0+n<=D.                  (7)

Indeed `rA,rC<=D` follows from (3), and `n<=e-h` together with
`e<=a+b,c+d` proves their lower bounds. The upper bound on t follows
from `p+f<=2D`, since both relevant face sums are at most `2D`.
Finally `t0+n=max(a+d,b+c)-f` is a face deficit and belongs to
`[0,D]`. All these are literal integer inequalities, including walls.

Write `Q=zeta^2`, `alpha=zeta^(2h+1)`, `z=zeta^(2e+1)`. The already
proved [actual generic source conversion](actual_general_four_port_single_racah_kernel.md#6-exact-conversion-to-the-seven-factorial-sum-including-its-phase)
is the exact identity

    S=S0 (V_n/C_n) G_n,
    G_n=sum_(k=0)^n
      (Q^-n,Q^(-p-f-1),alpha z,alpha/z;Q)_k Q^k
         /(Q,Q^(t0+1),Q^-rA,Q^-rC;Q)_k.          (8)

This is the actual finite generic series BEFORE specializing q.
By (6),(7), every numerator and denominator factor of every term
in (8) is a root unit. For the second upper parameter use
`p+f+1=N+t`; its root exponents are those of `Q^-t`, and `k<=n<=t`.
For the two spectral factors, their exponent ranges are

    h+e+1,...,h+e+k in [1,D],
    h-e,...,h-e+k-1 in [-D,-1].                  (9)

Thus there is no disappearing generic summand and no singular
Pochhammer denominator in this presentation.

## 3. Every summand has positive root value

Let `s_r=product_(u=1)^r 2sin(pi u/N)` and
`c_j=2cos((2j+1)pi/N)`. Direct conversion of each finite Pochhammer
in (8) to sine factors gives its kth root summand as

    A_k product_(i=0)^(k-1)(c_(h+i)-c_e),
    A_k= s_n/s_(n-k) * s_t/s_(t-k)
         * s_(rA-k)/s_rA * s_(rC-k)/s_rC
         * s_t0/[s_k s_(t0+k)] >0.              (10)

For clarity this is the same finite phase calculation as in the
proved folded spectral formula; it only requires the inequalities
(6),(7), not that every external label is folded. The residual
monomial phase is `q^(Nk)` and the residual sign is `(-1)^k`, so
both cancel. The spectral factorization uses

    (alpha z,alpha/z;Q)_k
       = product_(i<k) alpha Q^i (c_(h+i)-c_e)

at the root. Since `h+i<e<=D/2` whenever `i<k<=n`, every displayed
cosine difference is strictly positive. The term at k=0 is one.
Hence the ENTIRE true generic series has a positive common phase
at q and a nonzero value `G_n(q)>0`.

Each term in (8) is a product of a bounded number of finite unit
Pochhammers of lengths O(N), with integer exponents O(N). On the
uniform disk

    |log(zeta/q)| <= c/[N^2(1+log N)],            (11)

every such term divided by its positive root value remains in a
small sector about one. This is the elementary unit-factor harmonic
estimate proved in the positive-core note: sum the logarithmic
changes using `|sin(pi u/N)|>=2 dist(u,N Z)/N`. The bounded number
of products, including negative exponents and exponents up to `2N`,
only changes the absolute constant. Their positive sum obeys the
same estimate. Cauchy inequalities therefore bound every fixed jet
of G_n and its inverse relative to their root values.

## 4. Actual prefactor cancellation retains the generic normal

It remains essential to check the prefactor in (8). Positivity of
a substituted polynomial alone would not prove the source theorem.
Choose `(a',b',c',d')=(a,b,c,d)` if `a+d<=b+c`, and
`(b,a,d,c)` otherwise. The actual source formula gives

    R=(c+d-e, a+b-e, t0, a'-b'+e, d'-c'+e),
    S0=(-1)^s [s+1]!/product_(u in R)[u]!,
    V_n=zeta^n (Q^(-p-f-1);Q)_n
            /[(Q;Q)_n(Q^(t0+1);Q)_n(Q^(-s-1);Q)_n],
    C_n=alpha^n (Q^(-p-f-1);Q)_n
            /[(Q^(t0+1);Q)_n(Q^-rA;Q)_n(Q^-rC;Q)_n].           (12)

Every entry of R is in `[0,D]`: these are face deficits, together
with t0, bounded by (7). Because the branch is live,

    2N<=s+1<3N,
    0<=s+1-2N<n.                                 (13)

The second inequality follows from
`max(a+d,b+c)+f<=2D`. Consequently `[s+1]!` contains exactly
`[N]` and `[2N]`, while `(Q^(-s-1);Q)_n` contains exactly one
zero factor, namely `1-zeta^(-4N)`. All other factors in (12) are
root units by (6),(7). Cancel the common Pochhammers in V_n/C_n
GENERICALLY. Then cancel the indicated zero factor using the exact
identity

    [2N]/(1-zeta^(-4N))=zeta^(2N)/(zeta-zeta^-1).                (14)

If a superscript circle means omitting exactly the indicated factor,
the result is the explicit analytic unit identity

    (-1)^D S/[N]=A(zeta) G_n(zeta),
    A(zeta)=(-1)^(D+s) zeta^(2N-2hn)/(zeta-zeta^-1)
       * [s+1]!^(omit N,2N)/product_(u in R)[u]!
       * (Q^-rA,Q^-rC;Q)_n
            /[(Q;Q)_n (Q^(-s-1);Q)_n^(omit -2N)].               (15)

Every denominator in (15) is now a root unit. No term proportional
to `[2N]` in the original seven-factorial sum has been dropped:
(15) is an equality of the original generic germs, obtained from
the exact finite source transformation and exact cancellation (14).

The same unit-factor estimate applies to A and its inverse; the
additional monomial has exponent O(N^2), and the extra quantum
integer denominator is a root unit. Combining it with the positive
G_n gives fixed relative jet bounds for the entire original regular
source `(-1)^D S/[N]`. Its root value is the positive original core C,
so A(q)>0 as well. The four regularized face factors are analytic
units with the already proved uniform relative jet bounds.
Therefore (2), its inverse version and its local square-root version
follow on the SAME polynomial disk (11).

## 5. Cover all first normals using exact source relations

The [first-normal Ward theorem](actual_partner_first_normal_ward_reduction.md)
proves, for each opposite pair and every choice of the other bits,

    k(00)-k(01)-k(10)+k(11)=0.                   (16)

Apply it independently to the three opposite pairs. Every branch
is a signed sum of at most 27 branches having at most one high bit
in each opposite pair. Thus it remains to handle high sets of size
at most three, with no opposite pair.

Sets of size zero, one or two are face-supported. A three-edge set
with one edge of each opposite pair is either a face or the
complement of a face, namely a three-edge star. Face sets satisfy
(2). Consider a star set. If the branch is tail-free, use the
positive-core theorem. If its maximal face sum is repeated, use the
proved coherent Fourier bound. Otherwise use the exact controlled
first-normal difference from the
[Fourier source involution](actual_coherent_racah_tail_fourier_residues.md#6-the-residual-is-an-exact-partner-involution):

    |k(B)-k(B*)| <= C N^2(1+log N) W_N^2,         (17)

where B* flips the three edges outside its unique largest face.

The unique maximal face cannot be the all-low face complementary
to the high star. Every other face shares one of its low edges and
replaces its two remaining low edges by their high partners; its
sum is at least that of the all-low face. Equality everywhere would
also contradict uniqueness. Therefore the maximal face contains
two high edges and one low edge.

Its complementary flip turns the third high edge low and turns
its other two low edges high. In terms of opposite pairs, B* has
one pair in state `00` and two pairs in state `11`: a tetrahedral
face contains exactly one edge from each opposite pair. Apply (16)
to those two `11` pairs. This expresses k(B*) as a signed sum of
at most nine branches with at most TWO high bits, all already
controlled by (2). Equation (17) controls the star branch. Finally
the initial 27-term interpolation proves (1) for every original
partner, with constants independent of N, labels and parity.

The estimates are on the actual full generic first normals. The
proof has not replaced a normal by the root core, differentiated
a root-value identity, or imposed the first-order Ward equation
on higher orders.

The original coherent tail itself now has a uniform bound on EVERY
partner branch:

    |T_B(q)| <= C(1+log N) C_B(q).                (18)

For a tail-free branch T is zero. Otherwise write the exact germ as
`K_B=U_B(C_B+[2N]T_B)^2`, where U_B is the product of the four
regularized face factors. The logarithmic derivatives of U_B and
the positive core C_B are `O(N^2(1+log N))`. Divide the first
normal by `K_B(q)=U_B(q)C_B(q)^2` and use (1). This bounds
`[2N]'(q) T_B(q)/C_B(q)` by the same order. Finally

    |[2N]'(q)|=2N/sin(pi/N)>=2N^2/pi,

which proves (18). Thus the contribution of the actual retained tail
to the first normal is controlled through an exact positive source
presentation; no absolute estimate of its alternating summands was
substituted.

## 6. Precise remaining scope

This closes the local ALL-PARTNER FIRST-NORMAL scalar gap. Fixed
higher normals are proved here for face-supported and tail-free
branches. The exact first-normal Ward equation does not extend
homogeneously to second order: its cluster trace contributes there.
Thus arbitrary higher partner normals, the positive completed
physical change-of-frame metric, shared global source constraints,
and geometric overlap remain separate problems.

Audit: [literal generic source transformation and support checks](../experiments/audit_actual_all_partner_first_normal_bound.py)
and [recorded results](../experiments/actual_all_partner_first_normal_bound_results.json).

Independent root review checked the maximal-opposite-pair presentation,
all root-unit ranges, the exact generic prefactor cancellation and the
star-to-Ward covering argument. Fresh replay passed 79,649 supported
face-bit classifications, 2,384 live face branches, 430 complete generic
presentations through four Taylor coefficients, and 13,852 star routes.
The analytic bounds follow from the proof; the finite checks supplement
the source and incidence identities.
