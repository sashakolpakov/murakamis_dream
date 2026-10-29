# A tame paired Fermat frame for the original whole source

28 October 2026. Pairing the actual cap heads before changing frame
removes the exponential factorial norm found in independent-head
Fermat frames. The paired source, its marked dual, and a full invertible
frame are explicit. The frame and inverse are uniformly bounded on
one fixed central neighborhood, for every level. Conjugating the
whole actual word and all currents gives a pointwise identity of the
ORIGINAL invariant, including its full meridian family and scalar lines.

This is a theorem about the selected boundary source. It does not
factor the new crossing into a positive geometric tetrahedron kernel,
or identify its Cartan charge with a new Pachner edge winding.

## 1. The actual charged channel and the paired source

Fix N>=2, d=N-1, Q=exp(2pi i/N). On the original relative dual
pair the actual Cartan is Q^(-1-D), D=a+b, 0<=a,b<=d.
Its invariant channel is EXACTLY

    H_d=span{|j,d-j>:0<=j<=d},        D+1=N.             (1)

Indeed Q^(-1-D)=1 and 0<=D<=2N-2 force D=N-1.
The projector onto this channel is the actual finite Cartan
average, not a new positivity projection. The
[original source reduction](actual_rogers_bridge_transport.md)
uses the input/marked corner e_+=|d,0> and ordinary output
corner e_-=|0,d> in this channel.

Put epsilon=a^N and delta=(1-epsilon)^(1/N), delta(0)=1.
Take the ORIGINAL normalized cap frames from
[the exact cap theorem](actual_cap_pachner_wall_charge.md),
using the SAME a on the two heads, and project their tensor
product to (1). In the basis indexed by j this gives

    V_j(epsilon)= epsilon /
       [(1-Q)(Q^2 delta;Q)_j (Q delta;Q)_(d-j)],
    W_j(epsilon)= (Q delta;Q)_j (delta;Q)_(d-j)/N.        (2)

These are removable formulas at epsilon=0, with

    V(0)=e_+, W(0)=e_+^t,
    V_d=R=(1-Q delta)/(1-Q),
    W_d=A=epsilon/[N(1-delta)]
         =(1+delta+...+delta^(N-1))/N.                  (3)

All j<d entries vanish at zero. Replacing j by d-j gives
V_-,W_- with limits e_-,e_-^t. Write V_+=V,W_+=W.

To derive (2), the normalized input factors are

    (P_hat_d)_j=a^(j+1)/[(1-Q)(Q^2 delta;Q)_j],
    (P_hat_0)_(d-j)=a^(d-j)/(Q delta;Q)_(d-j).

Their powers multiply to a^N=epsilon. The normalized output
factors have powers a^(d-j) and a^(-(d-j)), which cancel.
This proves central descent directly, including the exact affine
charge. It also proves equality with the original corners at zero.

No assertion that epsilon is the actual semicyclic or meridian
normal parameter is needed. In the fixed old current frame,
F_rel V is generally nonzero away from zero. Section 4 transports
that current as well as the source; it does not silently claim
V is an invariant vector of the unchanged current.

## 2. Pairing cancels the exponential factorial profiles

For |epsilon|<=rho<=1/16, one has

    |delta-1|<=2rho/N,
    |1-Q^r|>=4 dist(r,N Z)/N.                            (4)

There is an EXACT symmetry before estimating any long product:

    V_j=V_(d-1-j), W_j=W_(d-1-j),          0<=j<d.      (5)

Indeed, writing A_l=(Q delta;Q)_l, the two expressions are
V_j=epsilon R/[A_(j+1)A_(d-j)] and
W_j=(1-delta)A_j A_(d-j-1)/N. The symmetry swaps their two
factors. It lets us estimate only j=ell-1 with
ell=min(j+1,N-j-1)<=N/2.

The consecutive ratios in (2) are

    V_(j+1)/V_j=(1-delta Q^(-j-1))/(1-delta Q^(j+2)),
    W_(j+1)/W_j=(1-delta Q^(j+1))/(1-delta Q^(-j-2)).   (6)

Their unperturbed magnitudes telescope from j=0 to ell-1,
giving |1-Q|/|1-Q^ell|<=pi/(2ell). Each normalized factor
at root distance s<=ell has relative error at most rho/(2s),
so its logarithmic magnitude changes by at most rho/s.
The numerator and denominator errors therefore sum to at
most 2rho(1+log ell), with NO log N loss. Moreover

    V_0=(1-delta)/(1-Q),
    W_0=epsilon/[N(1-delta Q^-1)],
    |V_0|,|W_0|<=|epsilon|/2.

Combining these statements gives the uniform tail estimate

    |V_j|,|W_j| <= (pi |epsilon|/4) exp(2rho)
                       ell_j^(-1+2rho),       j<d.    (7)

At rho=1/16 the squared power is -7/4. Every ell occurs at
most twice, and sum_(ell>=1)ell^(-7/4)<=1+4/3. Hence
the total off-corner squared norm is less than .015.
Together with |R|<=1+rho/2 and |A|<=1+rho, this proves

    sup_(|epsilon|<=1/16) ||V_+/-||_2,||W_+/-||_2<=3   (8)

for EVERY N. In fact the displayed estimates give norms below
1.1. The simple bound 3 suffices for all subsequent constants.
This fixed CENTRAL disc corresponds to |a|=(1/16)^(1/N), near one, rather
than the individual-head micro-collar |a|<=1/(16N).
The Cartan-charge pairing is essential to the cancellation.

More precisely ||V-e_+|| and ||W-e_+^t|| are O(|epsilon|),
uniformly in N on this disc. This includes the endpoints by (3).
The same holds in the reversed orientation.

## 3. The exact paired normalizer is a known algebraic unit

The full paired value is

    G(epsilon)=W V
       = R (2-epsilon)/(1+delta)
       = R (1+delta^N)/(1+delta).                       (9)

For a direct proof, for j<d put r=j+1 and multiply (2):

    W_j V_j = epsilon(1-delta)R /
       [N(1-delta Q^r)(1-delta Q^-r)].

The missing endpoint is W_dV_d=RA. The finite root identity

    sum_(r=0)^(N-1) 1/[(1-delta Q^r)(1-delta Q^-r)]
       = N(1+delta^N)/[(1-delta^N)(1-delta^2)]           (10)

follows by multiplying the two convergent geometric series first
for |delta|<1, taking the root sum, and then rational continuation.
Subtract its r=0 term. Its contribution exactly cancels RA,
giving (9). Removable values extend the calculation to zero.

On |epsilon|<=1/16, R and G are bounded units: for example
|R-1|<=rho/2 and |G-1|<1/8. In particular G(0)=1.
This scalar is computed from the known source alone. It is
NOT a normalization by an unknown knot period. Its entire
factor (2-epsilon)/(1+delta) must be retained.

Equation (9) also holds for W_-V_-. It does not normalize
the cross-oriented pairing W_-V_+, which vanishes at zero.
Dividing by that latter pairing would destroy the ordinary
zero-dimensional cup-cap behavior and is not permitted here.

For real 0<epsilon<1, there is also an exact positive Hermitian
structure. Reflection of complementary root factors gives

    W=(A/conjugate(R)) V^*,
    W/G=V^*/||V||^2,
    ||V||^2=|R|^2(2-epsilon)/[(1+delta)A].              (9a)

For j<d, use
conjugate((Q delta;Q)_(j+1))=
epsilon/[(1-delta)(Q delta;Q)_(d-j-1)] and the analogous
identity for d-j. Substitution in (2) proves (9a); the
endpoint follows from (3). Hence V W/G is an ORTHOGONAL
rank-one projector on this real interval. Its diagonal is
the explicit probability distribution

    pi_j=epsilon(1-delta^2) /
       [N(2-epsilon)|1-delta Q^(j+1)|^2].              (9b)

This describes the paired boundary functional. Ordinary output
caps have the other orientation, and the transformed word remains
complex. No positivity or noncancellation of the knot scalar follows.

The paired source also has a fixed-order exact cyclic equation.
Let A_clk act by Q^j and let (Tf)_j=f_(j+1 mod N), so
T A_clk=Q A_clk T. Direct ratios in (2), including the wrap,
give

    [(1-delta Q^2 A_clk)T
                 -(1-delta Q^-1 A_clk^-1)] V=0,
    W[(1-delta Q^-1 A_clk^-1)T^-1
                 -(1-delta Q A_clk)]=0.                (9c)

The two finite operators have different ordering, as the actual
marked co-source requires. Their regular classical symbol is the
Gaussian relation p=-A_clk^-1. The dilogarithmic factorial profiles
cancel in this paired boundary relation. At A_clk=1 its factors
cannot be divided out; the exact equations retain the cap wall.
The [degree/cap audit](actual_degree_carry_and_cap_winding_obstruction.md)
proves these ratios and their wrapped endpoint identities.

## 4. An explicit full invertible frame of uniformly bounded norm

Use either matched orientation, with reference corner e and
v=V_+/- , w=W_+/- /G. Then wv=1 and e^t v=R!=0.
Define on H_d

    g=v e^t+(I-vw)(I-ee^t),
    g^-1=I-v e^t/R+e w.                                (11)

Direct multiplication gives

    g e=v, e^t g^-1=w, det g=R,
    g(0)=I,
    rank(g-I)<=2, rank(g^-1-I)<=2.                      (12)

For instance decompose an input as ae+z with e^t z=0.
The output is z+v(a-wz), and e^t applied to it determines
a-wz because R!=0. This gives precisely the inverse in (11).

On the disc (8), the bounds above imply the uniform estimates

    ||g||<=15, ||g^-1||<=8.                             (13)

Both matrices in fact differ from the identity by O(|epsilon|),
uniformly in N.
They are algebraic meromorphic functions of epsilon,delta,Q,
regular on the stated marked disc. Extend g by the identity on
all other total-degree channels in the two-head space. This
retains its norm bounds and commutes with total degree and
with the actual Cartan clock. This is a full matrix frame,
not only an isomorphism of one line.

The construction does not assert that g commutes with the old
raising and lowering currents. They are transported by the same
conjugation, which is necessary for a pointed network identity.

These are bounds for whole algebraic functions on an N-independent
disc. They do not require truncating the source to a fixed list
of Taylor coefficients or shrinking its central neighborhood.

The norm is the fixed Euclidean norm in the ORIGINAL relative-head
basis of the exact Rogers presentation. Conjugating back by a
physical fusion matrix C_x need not preserve these estimates;
that separate matrix can be exponentially conditioned. The
new source frame adds no exponential cost within this specified
exact presentation, and the scalar equality in Section 5 is
independent of the metric.

## 5. Pointwise transport of the whole original arbitrary-plat invariant

Use the literal original fused word B_beta, with EVERY degree
channel retained, and its known source formula

    P_(beta,N)=chi_beta N^(1-k) <e_out|B_beta|e_in>.      (14)

At each chosen horizontal slice form a tensor product Gamma
of the paired frames (11), extended off H_d as above. For an
actual letter or coupon O between consecutive slices use

    O'=Gamma_next O Gamma_previous^-1.                 (15)

The actual currents, sewing maps, projectors, and any other
insertions use the same prescription. Internal frames cancel
exactly, giving B'_beta=Gamma_out B_beta Gamma_in^-1.
At the boundary use the original input orientation e_+ on
each pair, the ordinary output e_- on k-1 pairs, and the
marked output e_+ on the remaining pair. Then, POINTWISE in
every allowed auxiliary parameter,

    P_(beta,N)=chi_beta N^(1-k)
       (tensor_out W_sigma/G)
                     B'_beta (tensor_in V_+).          (16)

This follows from (12), not from a limiting argument or a
proposed triangulation invariant. The original full meridian
dependence and original scalar lines remain those of B_beta
and chi_beta. With unnormalized output rows W, retain the
explicit additional factor product_out G^-1 in (16).

No cross-oriented source pairing is divided out. No independent
head coherent frame H or M is substituted for g. Those frames
have the exponential norms proved in the four-line note;
the present paired, charge-preserving frame has the different
explicit bounds (13). For a fixed bridge number its tensor
norms remain bounded independently of N.

At an actual input dual pair, (15) carries F_rel to a current
annihilating V_+ exactly, since F_rel e_+=0. For an ordinary
OUTPUT the sided identity is (W_-/G)F'_rel=0, because
e_-^t F_rel=0. The marked output is not an ordinary Hopf cap.
Thus the relevant auxiliary completion's Ward defect is resolved
by an explicit full current transport.
This does not identify epsilon with a semicyclic normal
parameter, nor turn intermediate non-dual pairs into dual ones.

## 6. Normal residue corrections have uniformly bounded source cost

For completeness, the paired source also supplies an exact
finite-jet regularization of singular terms. With one common
central variable set J(epsilon)=V(epsilon)W(epsilon), or use
its explicit normalized version J/G. These rank-one kernels
have uniformly bounded trace norm on (8). Hence

    ||[epsilon^r]J||_1 <=9*16^r.                        (17)

For an actual matrix expansion O(epsilon)=sum_(r=-p)^infinity
O_r epsilon^r with fixed pole order, the paired constant-term
functional is exactly

    CT tr(OJ)=sum_(r=0)^p tr(O_(-r) J_r),
    |CT tr(OJ)|<=9 sum_(r=0)^p 16^r ||O_(-r)||.         (18)

The normalized kernel has another absolute constant. Independent
input and output central parameters, or a fixed number of pairs,
give the corresponding product Cauchy bounds. Central descent
of the paired source is proved in Section 1; descent or bounded
deck support of a transformed operator must still be checked.

Equations (17)--(18) specify a linear regularization which agrees
with the original cap on every assembled holomorphic word. It
preserves any exact meromorphic matrix identity to which it is
applied on one common domain. They do not assert that every
singular summand has the same value as an older independent-head
residue prescription. Such a comparison retains its actual
Ward/sewing corrections. The stronger pointwise identity (16)
does not depend on making that termwise identification.

## 7. What remains on the main critical path

The original paired source is now represented by a genuine tame
pointed frame, with its affine charge, dual scalar and currents
all explicit. This is the part of boundary transport proved here.

The new crossing in (15) has not been identified with the positive
geometric tetrahedron kernels. The three angular clocks of a
Pachner edge have not been proved to represent the charge D+1.
In particular (16) neither removes the certified oversized weak
alias face nor proves that the geometric scalar survives. A
nonzero bulk component of V can still cancel against the exact
transformed kernel. The general volume conjecture remains open.

The independent checks are in
[the paired-source audit](../experiments/audit_paired_actual_cap_source_independent.py).
They compare literal two-head cap products and the actual Cartan
projector, source bounds, the full normalizer, and the full frame
identities. The uniform assertions follow from the proofs above.
