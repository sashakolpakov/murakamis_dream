# A macroscopic polynomial quantum-normal window for every fixed plat

28 October 2026. For an original knot presented as a fixed 2k-plat,
ordinary-color quantum-normal jets are polynomially bounded throughout

    k(j-1)+1<=N.                                    (1)

The endpoint is INCLUDED. This follows from a one-sided angular
positive-path interval and elementary polynomial differentiation; no
derivative of a singular root path basis is taken. Thus the conclusion
controls a macroscopic part of the actual pointed quantum-A source,
not only finitely many small colors. It does not bound the remaining
high-color packet or independent meridian derivatives of the root ADO
state.

## 1. Exact original family and statement

Let C_j(q) denote the original reduced, zero-framed ordinary integral
color-j knot scalar. The ordinary pivot is K(q), with its matching
ribbon twist. At q_N=exp(pi*i/N), j<N, its equality with the original
reduced root state is the independently proved quotient/cabling
comparison, with the actual half-Cartan and parity adapters retained.
Off the root this note uses that ORDINARY integral family. It does not
differentiate a frozen ADO pivot as though it were the same family.

Fix the plat word and k. Its actual Laurent degree in the marked
variable z=q^(1/2) obeys

    deg_Laurent C_j <=D_j<=C_word (j+1)^2.          (2)

For every fixed r>=1 there is a constant C_(word,r) such that, for
all N and j>=1 satisfying (1),

    |partial_s^r C_j(q_N(1+s/N)) at s=0|
             <=C_(word,r) j^(k-1)(D_j+1)^(2r+1). (3)

For r=0 the sharper bound is |C_j(q_N)|<=j^(k-1).
In particular the right side of (3) is polynomial in N, for example
C_(word,r) N^(k+4r+1). There is no level-parity or primality restriction.

The same polynomial conclusion holds for the root normal coordinate

    Delta=1-q^(2N), q=q_N(1-Delta)^(1/(2N)),       (4)

and for the actual weighted colors d_j(q)=(q^(2j)-1)C_j(q), including
their fixed-order jets. The constants can change with r and the word,
but not N or j in this window.

For k>=2, the endpoint of (1) is below N, so these are ordinary colors.
The k=1 knot is the unknot, whose reduced scalar is one; its possible
j=N endpoint is harmless and can instead be handled separately.

## 2. Positivity on the full one-sided angular interval

Put m=j-1 and n=2km. The fundamental cable of this colored plat has
n endpoints. Work in its VACUUM path space: nonnegative paths

    a_0=a_n=0, |a_(i+1)-a_i|=1.

Every such path has maximum height at most n/2=km. This is the
important improvement over the full trace path space, whose paths
need not end at zero. On

    pi/(2N)<=theta<pi/N, q=exp(i theta),            (5)

condition (1) implies that all required weights

    mu_a=[a+1]_q=sin((a+1)theta)/sin theta,
                 0<=a<=km,

are strictly positive. At the upper endpoint, mu_(km) is allowed
to become zero if km+1=N. Positivity is only asserted strictly
BELOW that endpoint.

For completeness the elementary TL generator on this orthonormal
path basis has, when a_(i-1)=a_(i+1)=a, the two-state matrix

    e_i[b,c]=sqrt(mu_b mu_c)/mu_a, b,c in {a-1,a+1}.

The omitted height -1 has weight zero. Its nonzero eigenvalue is
(mu_(a-1)+mu_(a+1))/mu_a=2cos theta. The same elementary adjacent
calculation gives e_i e_(i+1)e_i=e_i; disjoint generators commute.
The maximum-height states introduce no missing term: a neighbor of
an editable middle height is at most km-1, so its two weights are
within the stated finite vacuum range. Thus every elementary
fundamental crossing

    B_i=q^(1/2)I-q^(-1/2)e_i                       (6)

is unitary: its eigenvalues are q^(1/2) and -q^(-3/2). Negative
crossings are its adjoints. These are the actual ordinary full-Cartan
normalizations, not a changed braid operator.

Jones--Wenzl recursion on each m-strand color block has positive
denominators [1],...,[m], is selfadjoint, and gives an orthogonal
projection onto the original color-j cable subspace. Its quantum
trace is EXACTLY [m+1]=[j]. One direct induction uses
f_m=f_(m-1)-([m-1]/[m])f_(m-1)e_(m-1)f_(m-1) and the ordinary
partial trace, giving [2][m]-[m-1]=[m+1].

The actual generic cabling comparison follows from the explicit
highest-weight embedding and the original R coproduct. Its proof
in [the ordinary-color audit](actual_ordinary_color_comparison_audit.md)
is algebraic BEFORE root specialization, so it applies throughout
(5), where none of those denominators vanish. No root-only quotient
has been analytically differentiated.

## 3. The original plat normalization and the improved bound

A single actual colored cup has squared positive norm [j]: closing
it against its adjoint evaluates precisely the quantum trace of its
Jones--Wenzl projector. The k disjoint ordinary colored cups therefore
have squared norm [j]^k. The actual output caps have the same norm.
The required self-dual orientation and ribbon identifications retain
their original signs and q monomials; on (5) these are unitary factors,
not additional positive dimension factors. They stay in C_j(q), and
their degree is included in (2).

One can see the cup normalization directly in the orthonormal vacuum
path model: one colored cup is sqrt([j]) times the unique length-2m
mountain path. The k-cup source is [j]^(k/2) times the concatenation
of those mountains. Every internal color projector fixes this source.
The cabled braid is unitary and maps the prescribed color subspace
to its actual corresponding output subspace. Consequently the raw
ordinary colored plat scalar has absolute value at most [j]^k.

The reduced KNOT scalar is the raw scalar divided by ONE [j]. This
is its original cut/trace identity, not one division per cup or per
strand. Hence throughout the CONTINUOUS interval (5),

    |C_j(exp(i theta))|<=[j]^(k-1)<=j^(k-1).        (7)

The last inequality follows from [j]=sum_(a=0)^(j-1)q^(j-1-2a)
and positivity. The full zero-framing line has modulus one on this
interval. Neither it nor any original pivotal factor is reset.

At theta=pi/N, use continuity of the actual Laurent polynomial C_j.
This includes equality in (1) even though the top path weight becomes
zero. It is invalid to differentiate that singular path basis; the
next step differentiates only a bounded POLYNOMIAL on the closed
one-sided interval. This is why the endpoint is genuinely included.

## 4. An elementary quadratic Laurent-degree bound

For clarity, (2) does not rely on a colored-Jones degree theorem.
In an integral highest-weight color-j basis, the original universal
R nilpotent coefficient is a Gaussian polynomial times a product
of at most j-1 quantum integers and a power of q-q^(-1). Its
divided-power denominator cancels in the Gaussian coefficient.
The latter's Laurent degree is O(j^2), as follows by its finite
Pascal recurrence. The Cartan exponent is a product of two weights
of size at most j-1, and hence also has degree O(j^2).

Both signs have the same degree bound. A fixed word adds only a
fixed number of such degrees. The actual pivotal powers contribute
O_word(j), and the matching ribbon framing contributes O_word(j^2).
Use the reduced cut scalar, rather than introduce a division by [j]:
it is a finite sum of these integral entries and pivots. Thus its
Laurent support is contained in [-C_word(j+1)^2,C_word(j+1)^2] in
z=q^(1/2). Summing paths cannot increase that support. This proves
(2) with a fixed coarse word constant while retaining the half-root.

## 5. Endpoint differentiation without a cited Markov inequality

Let z_N=q_N^(1/2) be its original marked branch. Put

    a=tan(pi/(8N)), t=a(x-1)/2, -1<=x<=1,
    z=z_N(1+i t)/(1-i t).

The q-angle now runs exactly from pi/(2N) to pi/N. Define

    P(x)=(1+t^2)^D C_j(z^2), D=D_j.                (8)

It is a polynomial of degree at most 2D: multiplication clears
every Laurent monomial's denominators. Since D a^2=O_word(1),
(7) gives

    sup_[-1,1]|P|<=exp(D a^2)j^(k-1)<=C_word j^(k-1). (9)

For any complex polynomial P of degree n, expand it as
sum_(l=0)^n c_l T_l(x). The cosine integral for its Chebyshev
coefficients gives |c_0|<=M and |c_l|<=2M, M=sup|P|.
The elementary differential equation

    (1-x^2)T_l''-x T_l'+l^2 T_l=0

implies, at x=1,

    T_l^(r+1)(1)=(l^2-r^2)T_l^r(1)/(2r+1).

Thus, for each FIXED r, |T_l^r(1)|<=C_r(l+1)^(2r), and

    |P^r(1)|<=C_r M(n+1)^(2r+1).                 (10)

The derivatives of (1+t^2)^(-D) at x=1 have bounded fixed-order
norms because D a^2=O_word(1). The angular chain rule costs at
most C_r N^r. Applying (9)--(10) to (8) therefore proves

    |partial_theta^r C_j(exp(i theta)) at theta=pi/N|
        <=C_(word,r)N^r j^(k-1)(D_j+1)^(2r+1).   (11)

This is an endpoint estimate, so a two-sided positive arc is not
needed. Finally q partial_q=(1/i)partial_theta on that angular
curve. For q=q_N(1+s/N), the order-r operator is

    N^(-r) product_(l=0)^(r-1)(q partial_q-l).

Its expansion uses only angular derivatives through r, and (11)
gives (3). For (4) it is instead the fixed polynomial
(-1)^r product_(l=0)^(r-1)((q partial_q)/(2N)-l),
which has the same bound. Derivatives of q^(2j)-1 on either scale
are bounded at fixed order since j<=N. This proves the weighted
color statement too.

## 6. The entire low-color packet is bounded on a complex normal disk

There is a useful strengthening of the fixed-jet assertion. Fix ANY
A>4. Uniformly for every color satisfying (1), the ACTUAL entire
ordinary family obeys

    |C_j(q_N exp(s/N))|<=C_(word,A)(D_j+1)j^(k-1)
                       <=C_(word,A)N^(k+1),
                  |s|<=2N^(-A).                  (12)

No eigenframe, recurrence denominator, truncated Taylor polynomial
or root color quotient is used on this disk.

To prove (12), keep the same polynomial P in (8). The half-root
ratio is now exp(s/(2N)), so its exact rational coordinate is

    t=-i tanh(s/(4N)), x=1+2t/a.

Consequently |x-1|<=C|s|. For |x-1|<=d<1/4 the elementary formula

    T_l(x)=[(x+sqrt(x^2-1))^l
                         +(x-sqrt(x^2-1))^l]/2

gives |T_l(x)|<=exp(C l sqrt(d)): the two reciprocal factors have
moduli at most 1+C sqrt(d). The finite Chebyshev expansion and
|c_l|<=2M from (9) yield

    |P(x)|<=C(D_j+1)j^(k-1)
                            exp(C D_j sqrt(|s|)).

Since D_j=O_word(N^2) and A>4, this exponential is bounded by a
word constant on the whole displayed disk. The denominator in
(8) is nonzero there and its inverse has modulus at most
exp(C D_j |t|^2), also bounded. This proves (12), including the
one-sided-positivity endpoint: only the original real-arc bound
was used in its polynomial continuation.

The weighted d_j(q)=(q^(2j)-1)C_j(q) has the same bound, since
|q^(2j)|<=exp(4N^(-A)) on this disk. The linear normal
q=q_N(1+s/N) and the normal (4) map smaller disks of comparable
radius into this exponential disk by their exact logarithms.
Cauchy's formula on a slightly smaller circle gives simultaneous
polynomial bounds for ANY fixed jet depth of this ENTIRE packet.

This stronger result is important at singular recurrence steps:
one can transport the honest holomorphic low-color germs around
nearby coefficient zeros, rather than infer that a finite Taylor
truncation selected the correct meromorphic continuation. No
recurrence denominator has been declared absent from that circle;
the actual scalar colors themselves are holomorphic and bounded.

## 7. What this supplies for the original pointed source

For fixed k, the interval reaches

    j<=1+floor((N-1)/k).

At every singular recurrence step whose entire retained bounded
jet packet lies within this color interval, its ACTUAL quantum-normal
data are polynomially bounded without inverting that singular step.
In particular a 2-bridge presentation controls the ordinary-color
quantum jets through the midpoint, including the valid endpoint.
The original complete/root source and all remaining high-color
normal packets stay in the subsequent boundary transport.

This does NOT assert a meridian-derivative bound for F_N(Y) at
fixed q_N. Along C_j(q), q and Y=q^(2j) move together. Nor does
pointwise unitarity at q_N extend the result beyond (1): there the
continuous vacuum path space encounters nonsemisimple wall channels.
Those channels and their original source must be retained. No bound
for the complete K_N or the full high-color response is inferred.

[Audit](../experiments/audit_ordinary_color_macroscopic_normal_jet_window.py):
continuous untruncated vacuum path unitarity, colored cup/JW
normalization, endpoint-inclusive angular bounds and exact
Chebyshev endpoint derivative estimates.
