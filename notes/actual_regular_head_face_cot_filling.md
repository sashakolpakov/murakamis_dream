# Exact two-neighbor filling of regular physical head faces

28 October 2026. Grouping the TWO actual crossings neighboring a physical
head before estimating its normal contour gives a source-faithful
outward filling at every regular physical head endpoint. This uses the
complete original scalar state, not a discarded tail of a low-band Hardy
kernel, a new boundary state, or an independent output projection.

The theorem is uniform for every fixed signed braid and bridge count.
Its scope is a head face whose other head colors AND all transfers remain
in a fixed bulk chamber. Simultaneous head/transfer endpoint clusters
are excluded. The estimate does not by itself give the sharp whole-knot
volume bound or geometric noncancellation.

## 1. Exact signed scalar and the head-factor composition identity

Retain N>=2, d=N-1, Q=exp(2*pi*i/N), x=-exp(-pi*i/N), the
original kappa, all pivots and the original external chi_N. Let Fhat_+
be the actual factorial interpolant and Fhat_- its conjugate-root
partner. Their exact relation is

    Fhat_-(s)=g_N(s) Fhat_+(s),
    g_N(s)=exp[i*pi*s-i*pi*s*(s+1)/N].               (1)

Indeed both factorials have the SAME real meromorphic sine-factorial
part in their independent Barnes definition; only their displayed
quadratic chirps differ. This proves (1) as a whole meromorphic identity,
including every normal coefficient. It is not just equality at integer
states. In particular g_N(n)=(-1)^n Q^(-n(n+1)/2).

For positive transfer k, the actual signed checked coefficients are

    r_+(a,b;k)=kappa x^(-a-b+k) Q^(b*(a-k))
                    Fhat_+(b+k)Fhat_+(a)
                     /[Fhat_+(k)Fhat_+(b)Fhat_+(a-k)],

    r_-(a,b;k)=kappa^(-1) x^(a+b-k) Q^(-a*(b-k))
                    Fhat_-(a+k)Fhat_-(b)
                     /[Fhat_-(k)Fhat_-(a)Fhat_-(b-k)]. (2)

Their unwrapped outputs are respectively (b+k,a-k) and (b-k,a+k).
The physical OVER strand always loses k, and the physical UNDER strand
always gains k; the sign determines which tensor slot has that role.

Replace each Fhat_- in (2) using (1), retaining its entire factor g_N.
At EITHER crossing sign the head incidences are now exactly

    OVER input: +1, OVER output: -1,
    UNDER input: -1, UNDER output: +1,              (3)

and its transfer has exponent -1. Thus, on any closed physical knot,
the complete ordered scalar product has the exact meromorphic form

    A_N(u)=E_N(u) product_(physical arcs e) Fhat_+(h_e(u))^(c_e)
                         product_j Fhat_+(k_j)^(-1), (4)

where

    c_e=+2 for UNDER output -> OVER input,
    c_e=-2 for OVER output -> UNDER input,
    c_e= 0 for a continued OVER or UNDER role.       (5)

All original kappa, half-Cartan, g_N conversion chirps and closure
pivots are retained in the specified nonzero entire exponential E_N;
the original external chi_N/N stays outside unchanged. The logarithm
of E_N is an explicit quadratic polynomial with quadratic
coefficients O_word(1/N) and linear coefficients O_word(1); its external
state-independent factor is not normalized away. Formula (4) is an
EXACT two-neighbor composition identity. If different physical arcs
have the same state linear form, their factors are multiplied, not
declared independent.

## 2. Which endpoint can occur with nonzero adjacent transfers?

Consider a physical arc of color h. At h=0 with both adjacent transfers
strictly positive, its previous crossing cannot have UNDER output:
the UNDER input h-k would be negative. Its next crossing cannot have
OVER input: the OVER output h-k would be negative. Therefore this is
necessarily an OVER-output -> UNDER-input local MINIMUM and c_e=-2.

At h=d with both adjacent transfers strictly positive, its previous
crossing cannot have OVER output (its input would be d+k), and its
next crossing cannot have UNDER input (its output would be d+k).
It is a local MAXIMUM, UNDER output -> OVER input, and c_e=+2.

These statements use the actual nonnegative transfer convention at
both crossing signs. They are physical state inequalities, not a
positivity claim about crossing coefficients. If one of the adjacent
transfers is zero, this deduction is unavailable and that joint corner
is deliberately retained.

## 3. The exact whole source and its normal cotangent contour

Use the [cardinal completion](actual_scalar_cardinal_source_completion.md)
of the COMPLETE original averaged marked source, before splitting any
head bands. For a one-component diagram its coordinates are exactly
u=(t,k_1,...,k_m), and every arc h=t+sum_j epsilon_j k_j has
epsilon_j in {0,+1,-1}. Hence

    (t,k) -> (h,k), determinant 1,                  (6)

is an INTEGRAL bijection. All original valid states have 0<=h,k_j<=d.
Choose a fixed O(N) complex box in these coordinates, and sufficient
fixed cardinal powers at each original factorial occurrence. The
completed scalar is holomorphic throughout the box, equals the
original scalar on valid integer states, and vanishes at invalid
integer states, including simultaneous scalar poles.

Consequently the original scalar is exactly chi_N/N times the product
cotangent residue integral of that completed scalar in (h,k). Every
pi*cot(pi*h) and pi*cot(pi*k_j) factor is retained. This assertion
follows by the finite residue sum, not by dropping a transformed source
factor: a pointwise pullback of the old cotangent in t would instead
be pi*cot(pi*(h-sum epsilon_j k_j)). Taking the k residues first gives
integer k and its exact periodic equality with pi*cot(pi*h). Thus the
new source representation and the old one have the SAME complete
integer residues, with no Jacobian, grid factor, or omitted side current.

For a regular lower head face the original left normal edge Re h=-1/2
can now move to Re h=-M-1/2. All negative integer cotangent poles have
zero residue because the completed scalar vanishes there. The two
finite-height horizontal connecting pieces are retained in this
closed rectangle identity. At an upper face move the right edge from
Re h=d+1/2 to Re h=d+M+1/2, retaining the same connecting pieces and
all cotangent factors. No physical integer state is crossed or deleted.

The tangent variables are fixed, not replaced by independent off-grid
outputs. Their actual unwrapped arc forms shift with h according to
(6). The bounds below hold uniformly while every other head and every
transfer stays in its stated bulk chamber.

## 4. Uniform normal estimate, including all original phases

Fix an imaginary-height bound T and a compact marked BULK chamber for
the remaining factorial arguments. For a literal fixed-height source
contour one may require their scaled real parts in [eta,1-eta], with
bounded scaled imaginary parts and consistent factorial branches.
Let B_N be the unwindowed original scalar at the endpoint h=0 or d,
with that head factorial replaced by its actual finite value. All
other factorials, pivots and kappa remain in B_N; the same original
external chi_N/N multiplies both sides of every estimate.

There are constants C,B,delta>0 depending only on the diagram and this
chamber such that, for 1<=M<=delta*N, the WHOLE windowed scalar on the
outward normal edge satisfies

    |Atilde_N| <= N^B exp(C(M+1))
                  [C(M+1)/N]^(2M) |B_N|.          (7)

The same estimate with the appropriate integer floor of the normal
distance holds on the horizontal connecting pieces. The powers of
N absorb the finite number of fixed cardinal windows and the bounded
normal factorial base. On a macroscopic nonreal tangent chamber one
may expand the BULK windows by their exact finite-mode packet and
apply (7) to each specified bulk mode with its original integer-marked
N-order phase retained: its right-hand B_N is then the MODE-WEIGHTED
bulk amplitude, including that exponential, rather than the literal
unwindowed B_N used on the fixed-height contour. The HEAD windows
stay whole: their separated
modes have poles at outside-band integers and their matched currents
are essential to the same contour identity. No wrong-side bulk-window
exponential or normal cancellation current is erased.

Here is a direct uniform proof. At a lower face write h=nu-M with
nu in the fixed strip -1<=Re nu<=0, |Im nu|<=T. The exact factorial
step gives

    1/Fhat_+(h)=product_(r=0)^(M-1)(1-Q^(nu-r)) / Fhat_+(nu). (8)

The reciprocal base on that compact strip is O_T(N^C): shift once
to 0<=Re(nu+1)<=1, where the bounded-order Gamma expansion gives the
usual polynomial base, and retain 1-Q^(nu+1). Moreover

    |1-Q^(nu-r)| <= C_T(r+1)/N

for M<=delta*N. The gathered head factor is its SQUARE by (5).
At the upper face write h=d+nu+M with 0<=Re nu<=1. Exactly,

    Fhat_+(h)=Fhat_+(d+nu)
                      product_(r=1)^M(1-Q^(nu+r-1)),
    Fhat_+(d+nu)=N exp[i*pi*nu*(nu+d)/N]/Fhat_+(-nu). (9)

The second identity is the actual factorial reflection, including
its chirp. It proves a polynomial upper base through both endpoints;
the first proves the same small-factor product as (8).

For every OTHER bulk factorial, a normal displacement of size M+1
has relative modulus at most exp(C(M+1)). This follows either from
the uniform complex factorial symbol with bounded logarithmic
derivative on the marked compact chamber, or by the exact unit step
followed by the bounded fractional Gamma base. The logarithmic
derivative of E_N in (4) is O_word(1) on the fixed O(N) box, so ALL
Cartan, conversion, pivot and Gaussian phases cost exp(C(M+1)) too.
Finally the exact cardinal bound is sqrt(N)*exp(2pi*|Im ell|).
On a fixed-height joint contour every Im ell is bounded by a diagram
constant, independent of N and M. This proves (7), also at coincident
negative integer poles, since all completed factors are holomorphic.

For M=N^alpha, 0<alpha<1, the entire collar has exp(o(N)) cost, and
its far edge relative to B_N is at most

    exp[-2(1-alpha)N^alpha log N+O(N^alpha+log N)]. (10)

One may also take M=floor(delta*N) with a sufficiently small fixed
delta. Then its far edge has a strict exponential drop
exp[-c*delta*N*log(1/delta)] relative to the endpoint bulk amplitude.
The whole intervening collar has only polynomial normal overhead:
choose delta so C+2log(C*delta)<0 in (7), and treat bounded M with
the polynomial base. This is a NORMAL estimate; it does not bound
the unrestricted tangent exterior amplitude B_N by volume.

## 5. What has and has not been removed

The zero-side direction comes from composing the two original
neighboring scalar factors FIRST. It is absent from an isolated
low-head kernel K_R, whose Hardy residues cancel at its apparent
matching pole. No such pole residue was asserted here. The whole
head bands remain together in the original finite source, and the
outer cotangent edge is filled with its exact scalar continuation.

This removes a regular head endpoint as a compulsory scalar POLE
exit. It supplies a quantitative outward contour with the original
normalization and unwrapped routing. It does not prove that the
remaining whole cycle reaches the geometric thimble, or that every
simultaneous endpoint cluster has this direction. In particular a
head endpoint next to a zero transfer, a repeated head face, and
escaping tangent bulk coordinates require their own compensated
whole-source treatment. The full global growth estimate remains open.

[Audit](../experiments/audit_actual_regular_head_face_cot_filling.py):
literal signed head incidence, original statewise composition, exact
negative-root conversion and both normal small-factor identities.
