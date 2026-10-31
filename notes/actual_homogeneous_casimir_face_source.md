# Homogeneous face kernels for the original Casimir coupons

30 October 2026. This stays
within the original fixed flat-plat presentation. No arbitrary matched
graph-to-plat adapter is being assumed.

## 1. One homogeneous local polynomial

Let N>=3,d=N-1,q=exp(pi i/N),Q=q^2, and let Omega be the actual
balanced pair Casimir. At a box retain the literal face order
(x,b,c,y): input middle b, output middle c. If F=f(-T), where T is
the [source-normalized small-circle face operator](actual_small_circle_polynomial_face_insertion.md), write for 0<=j<N

    F z^j=sum_(a,beta>=0; a+beta<=j)
       M_f(j;a,beta) x^a y^beta z^(j-a-beta).

Define a HOMOGENEOUS polynomial in the four original faces by

    H_f(x,b,c,y)=sum_(j=0)^d sum_(a,beta)
       M_f(j;a,beta) x^a b^(j-a-beta)c^(d-j)y^beta.  (1)

All exponents are nonnegative and its total degree is d. This uses
the whole polynomial f(Omega), with all repeated-node data; it is not
a spectral-value interpolation. The operator T preserves polynomials
and degree and commutes with z^N, so the N input monomials determine
the exact local cyclic shift operator.

Examples, with all scalar conventions explicit:

    H_1=sum_(j=0)^d b^j c^(d-j).
    H_(L_h)=T_h^(b) H_1,
    H_(L_h R^epsilon)=lambda0^epsilon T_h^(b) H_(r_N^epsilon),
    lambda0=q^(d^2/2), epsilon=+/-1.                (2)

Here T_h=P_(h-1)(T), and the superscript means that T acts on the
variable b with outer variables x,y. The original square-root lift in
lambda0 is retained. This is root algebra, not a genuine-q germ.

The normalized crossing polynomial r_N and its inverse have the
literal Hermite data in the signed one-port theorem. Write
M=floor(d/2); the quantities k_a, beta_a, D_a and Ptilde_s below are
the exact factors of the [positive-circle theorem](actual_complete_circle_positive_face_polynomial.md).

The complete circle has the exact identity

    H_(L_N)=N sum_(a=0)^M k_a beta_a^2
             D_a(x,b,y)D_a(x,c,y)Ptilde_(d-2a)(x,y). (3)

It follows either by applying the already proved original complete
spectral identity to (1), or by the finite Newton formula. With a
retained half twist, insert the actual omega_a^epsilon in (3).
For each fixed complete channel, its H is N times that literal local
positive polynomial, including k_a beta_a^2 and its phase.

## 2. Exact local physical face-grid identity

Keep ALL formal Casimir step words and group them by p modulo N only
after inserting the source phase q^(d p). Write the resulting normalized
q-difference operator

    F g(z)=sum_(p mod N) A_p(x/z,y/z) g(Q^-p z).

Its inverse finite Fourier transform is exact:

    A_p(X,Y)=N^-1 sum_(j=0)^d P_j(X,Y) Q^(p j),
    P_j=sum M_f(j;a,beta)X^aY^beta.                 (4)

On the actual face grid, c=Q^-p b. Consequently

    c^-d H_f(x,b,c,y)=sum_j P_j(x/b,y/b)(b/c)^j
                    =N A_p(x/b,y/b).               (5)

For the physical input heads u,v and output heads r,s, the literal
clocks are U=-q^-1 x/b,V=-q^-1 b/y, and p=r-u. The original matrix
element is therefore

    f(Omega)_(r,s;u,v)
        =N^-1 q^(-d p)c^-d H_f(x,b,c,y)            (6)

when the output clocks are represented by c. This includes zero when
the modular output has the wrong UNWRAPPED total: every Casimir word
has the true vanishing physical endpoint coefficient, so an illegal
wrap has zero coefficient before it can become a physical path. The
finite R/R^-1 are the actual polynomials in this same Casimir, with
the specified lambda0 and Hermite derivative. Equation(6) is not an
extension obtained by discarding a physical endpoint.

## 3. Original mark, integer lifts and even-level carries

Use the actual connected flat plat with R boxes and R+2 white faces.
Retain the original cups and every ordinary cap except its ONE original
unrestricted marked cap. There are R ordinary face targets and two
protected faces u,v. All coupons f(Omega) preserve the literal integer
sum of the two main-head indices. Thus after the other caps the two
indices at the marked cap necessarily sum to d, exactly as in the
original marked face-coefficient proof. Its ratio to the ordinary cap
is still the actual N^-1 (L_v/L_u)^d, not a new trace functional.

For a nonzero physical state, the centered main heads define an integer
conserved flow on the actual planar four-valent Morse graph, including
the cups and caps. The elementary planar face-potential argument gives
integer lifted potentials, unique up to a common constant, with the
literal half-index offsets. Equivalently, the main heads have

    i=d/2+n_left-n_right+(t_left-t_right)/2.

Here t=0 for odd N and t is the original gap parity for even N.
Adjacent main regions have opposite t at even N; the two middle
faces of a box have the same t. In particular the ACTUAL physical
p=r-u equals n_b-n_c, not just its residue modulo N.

Use these lifted logarithms in the intermediate half powers. Then

    q^(-d p)(bc)^(d/2)=c^d,                        (7)
    f(Omega)_(r,s;u,v)=N^-1 H_f(x,b,c,y)/(bc)^(d/2). (7a)

The second identity follows DIRECTLY from (6),(7); it does not use a
complete-box factorization as a black box.

Here is the entire remaining turn calculation. It is the literal
matrix calculation in the [original marked face-coefficient theorem](actual_original_marked_face_coefficient.md), sections 2--3.
For a physical complementary pair with first head i and second j=d-i,

    cup(i,j)=N q^(-d^2+di),
    cap(i,j)=N^-1 q^(di),
    mark(i,j)=N^-2 q^(dj).

The centered first head on a cup/cap has outside region o and inside
region z, so q^(di)=q^(d^2/2)(L_o/L_z)^(d/2). Thus each cup constant
is N q^(-d^2/2), each ordinary cap constant is N^-1 q^(d^2/2), and
their k pairs cancel EXACTLY. The mark-to-ordinary-cap ratio is
N^-1 q^(-d^2)Q^(dj)=N^-1(L_v/L_u)^d, with the original SECOND head
j. This uses the whole-source complementary constraint already proved
above, rather than restricting the original mark in advance.

Let T_f count +1 for each outside cup/cap corner and -1 for each
inside corner. The turn product is therefore

    N^-1 (L_v/L_u)^d product_f L_f^[(d/2)T_f].

Let M_f count the input/output middle incidences at ALL original boxes,
independently of which f(Omega) is inserted. The flat-plat sweep gives
M_f-T_f=2 at every bounded face and M_u-T_u=-2 at the exterior.
Every bounded gap segment has two middle-or-inside-turn ends; the
exterior has 2(k-1) middle ends and 2k outside turns. This argument
uses only the original projection, not a smoothed graph.

Multiplying (7a) over the R boxes now gives the literal total summand

    N^(-R-1) product_e H_(f_e)
          *(L_v/L_u)^d product_f L_f^[(d/2)(T_f-M_f)]
      =N^(-R-1) product_e H_(f_e)
                              /product_ordinary L_f^d. (7b)

All half powers have disappeared and every face exponent in the final
expression is integral. Changing any lifted n_f by N leaves it
unchanged. This is why both parities have the same final formula;
local lift signs have not been reset independently. The original cup,
cap, mark and index formulas have all been displayed, and none depends
on using a complete coupon at a box.

Conversely each original finite face-grid point specifies canonical
physical main heads. If an unwrapped conservation equation fails, its
actual matrix element (6) vanishes. If all are nonzero, the conserved
flow gives the lifted potentials just used, so the equality applies.
The original positive complete-channel support zeros are included
when such coupons are retained. Thus this is an equality of the actual
finite source sums, not an unconstrained off-grid continuation.

## 4. Whole-source polynomial coefficient, with no smoothing hypothesis

The original finite face grid has N^(R+1) points, after fixing the
exterior potential. The original marked scalar is N^-1. Each of the
R local inverse Fourier transforms contributed exactly N^-1. Therefore
the actual source is the normalized face-grid average of

    product_(boxes e) H_(f_e)(L_x,L_b,L_c,L_y)
                      /product_(ordinary faces) L_f^d. (8)

Equivalently it is

    Z_N=[product_(ordinary faces) L_f^d]
               product_e H_(f_e)(L_x,L_b,L_c,L_y),
              with both protected exponents equal0.  (9)

The primitive grid normalization is exactly accounted for: there is
NO extra N^R in (9), because H_f itself includes the N in (3).
If r boxes remain complete and the others are general, extracting
their N factors gives N^r times the original remaining spectral scalars.
All external Cartan and framing factors stay exactly where specified.

To prove that the grid average is exactly (9), the numerator is a
polynomial with nonnegative exponents (not necessarily positive
coefficients), homogeneous of degree dR. The grid selects exponents
d mod N at all R ordinary faces and0 mod N at the protected face v.
Since d=N-1, the former have minimal nonnegative representative d.
The total degree forces them ALL to equal d, and the protected
exponents to equal zero. The exterior face exponent then also equals
zero. In the even coset, the resulting phase is one since every
exponent equals its target. This excludes ALL aliases on the original
grid. It does not use a merge forest, an elimination order, or the
connectedness of any identity-smoothed projection.

In particular (9) applies to disconnected small-port subsets and to
sets with outer-variable dependency cycles. The fixed original
projection remains connected, which is the stated flat-plat hypothesis.

## 5. Exact signed magnitude and all-subset local norm certificate

For the geometric rate and corridor statements below, assume the
original flat plat has the same actual labeled nondegenerate
right-angled certificate as the complete-source volume theorem.
The finite algebra in sections 1--4 needs only the stated connected
original flat-plat source.

Put S_0=1 and S_j=product_(v=1)^j 2sin(pi v/N). For i+k+l+t=d,
the normalized positive crossing polynomial has exact
coefficient on b^i x^k y^l c^t

    (-1)^(k+l+1) q^[kl-(i+1)(t+1)]
                     N/(S_i S_k S_l S_t).          (10)

For the inverse, invert q in the displayed phase; all sine factors
remain positive. The original lambda0^epsilon multiplies this whole
polynomial. Formula(10) follows from the finite q-multinomial kernel:
j=d-t, and S_j S_t=S_d=N. In particular its weighted coefficient norm
is EXACTLY the positive homogeneous polynomial

    A_N(b,x,y,c)=sum_(i+k+l+t=d)
                  N b^i x^k y^l c^t/(S_i S_k S_l S_t). (11)

Uniform sine-product estimates give N^-1 log A_N -> G(b,x,y,c), the
four-angle potential of the [signed one-port theorem](actual_signed_small_circle_face_kernel.md). This follows
directly from a single degree-d simplex, not from a maximum over
operator blocks. At fixed positive radii, (2) therefore implies

    ||H_(L_h R^epsilon)|| <=C_b^(h-1) A_N,
    ||H_(L_h)|| <=N C_b^(h-1) max(b,c)^d,          (12)
    C_b=3+4(x+y)/b+4xy/b^2.

The second inequality retains the exact leading rate of H_1,

    I(b,c)=log max(b,c),
    max(b,c)^d <= ||H_1|| <=N max(b,c)^d.

In particular I<=G, since the b and c corners occur in (11). This keeps
the actual cancellations within each local f before taking absolute
values. Multiplying (12) and taking the SINGLE coefficient (9)
gives the independent-old-face bound without any dependency-order issue.

The strongest direct finite certificate is allowed to use different
SHARED old-face radii for different subsets. For a nonempty reflected
subset S, choose ONE positive radius l_f for each original face, and set

    C_S(l)=sum_(e notin S) [F(l_x,l_b,l_y)+F(l_x,l_c,l_y)]
           +sum_(e in S, epsilon_e!=0) G(l_b,l_x,l_y,l_c)
           +sum_(e in S, epsilon_e=0) I(l_b,l_c)
           -sum_(ordinary f) log l_f.               (13a)

Here F is the actual fold triangle rate, including its beta scalar,
from the [all-channel rate theorem](actual_positive_face_channel_rate.md)
and its [absolute endpoint normalization](actual_original_boundary_stationary_character.md).
All local factors use the SAME l_f wherever that face occurs. The
complete half-twist phases have modulus one and remain in the exact
source before applying this bound. The sufficient test is

    for every nonempty S subset E, there exists l^(S)>0 with
          C_S(l^(S)) < Phi_D=Vol(Y_D)/(2pi).        (13b)

No uniformity over a changing graph or infinitely many subsets is
needed: the original graph and E are fixed. An infimum certificate
strictly below Phi_D suffices, because then some finite positive
radii realize a smaller strict margin. This formulation retains I
for unsigned deleted ports; replacing I by G is a weaker optional
bound. The I-only capacity is the same smoothed positive-source
capacity underlying the already proved untwisted corridor. No
universal existence of mixed signed/unsigned certificates is asserted.

Here is a direct justification of that I-only identification. Use the
literal merge-forest/exterior-cycle classification in the
[simultaneous source theorem](actual_simultaneous_small_circle_face_correspondence.md),
including its disconnected case, and the finite angle-entropy duality
of the [smoothed-source capacity theorem](actual_smoothed_source_capacity_blocks.md).
The dual of
I(b,c)=max(log b,log c) assigns nonnegative loads sigma_b,sigma_c
with sum one to the edge endpoints, with zero entropy. A connected
merge tree has total remaining triangle load one if its root is
ordinary, and zero if its root is protected. Given a feasible merged
angle flow, its lift to the original vertices is unique: at an edge
oriented parent-to-child, let L be the remaining triangle load in
the entire child subtree, and set sigma_child=1-L, sigma_parent=L.
All these loads are in [0,1], since the subtree load is nonnegative
and at most the whole component load. Subtracting neighboring
subtree balances verifies every original face target; the root
balance follows from the component total. Conversely, summing an
original feasible flow over each component gives the merged flow.
The edge entropy is zero, so both maximized entropies, hence both
capacities, agree, whether or not a finite radius minimizer exists.
If smoothing disconnects the projection, the exterior component has
beta>=1 actual cycles and would require remaining triangle load
-beta: its number of original ordinary targets minus its number of
deleted edges. Nonnegative angle loads make this impossible; the
dual capacity is -infinity. No analogous identification is made for
a signed G edge.

One simpler sufficient test uses the original marked packing for
all S. At those radii put

    g_e=F(x,b,y)+F(x,c,y)-G(b,x,y,c).                (13)

If g_e>0 for every port in E, then (13b) follows, because I<=G.
Every original ordinary target remains d, so this is the literal
original target subtraction and it also covers disconnected
replacements. Readjusting the shared radii in (13b) can certify a
subset even when its original-packing local g_e is nonpositive.

For a boundary quartet with some marked face variables zero, this
criterion is understood by the LITERAL polynomial and its continuous
rate. In (11), zero variables require the corresponding exponents to
vanish. The entropy maximum is over that simplex face; G is continuous
on every nonzero nonnegative quartet. The same is true of the actual
triangle potential F. Hence if (13) is strictly positive there, one
may set the marked zeros to sufficiently small FIXED positive radii
before applying (12). The C_b constants can grow, but are then fixed;
delta is chosen afterwards. No positivity of every boundary g_e is
assumed. The local criterion is sufficient, not universal.

## 6. Whole mixed-source corridor under finite shared-radius certificates

Let E be any set of varied original circle ports, with their actual
epsilon_i in {0,+1,-1}. Suppose the finite shared-radius test (13b)
holds. In particular it holds under the simpler local test (13),
with the literal marked-zero convention above. No assumption on the
identity smoothing of E or of its subsets is needed. All external
colors outside E remain N, with arbitrary original complete half
twists retained.

There are constants delta,gamma>0 and K such that the original mixed
source A_N and its EXACT empty-subset complete-image core F_N^E obey

    |A_N(N-h_E,N_else)-F_N^E(h)|
             <=N^K exp[N(Phi_D-gamma)]              (14)

for every sufficiently large N of both parities and every PHYSICAL
integer 0<=h_i<=delta N. Indeed the exact reflection expands over
finitely many nonempty subsets. A term selecting a zero deficit
vanishes because L_0=0; apply (12) only to the positive deficits in
the remaining terms. Equations(9),(12) bound each original
subset at its chosen shared old-face radii l^(S). The strict margins
in (13b) have a positive minimum over the finitely many subsets.
If using marked-zero data, first fix positive regularizations
preserving those margins. Choose delta afterwards so that all the
finite small-color costs C_b^(h_i-1) consume less than half the
smallest margin. No N-dependent optimization of radii is used.
The uniform all-channel upper estimate handles all remaining complete
labels, and their number and measures are polynomial. The original
reflection signs and half-twist phases are retained before this bound.

Shrink delta further inside the [zero-free complex-core packet](actual_complete_core_complex_packet.md).
Its uniform lower rate is at least Phi_D-gamma/2 there. Thus

    A_N(N-h_E,N_else)/F_N^E(h)=1+O(exp(-cN))         (15)

uniformly on that integer corridor. For h_N/N -> chi real in this
cube, the [actual marked geometric assembly](actual_complete_core_geometric_deformation.md) then gives

    lim (2pi/N)log|A_N(N-h_(N,E),N_else)|
                                    =Vol(rho_chi).  (16)

The regulator boundary correction vanishes because the selected
peripheral U_i=-2pi i chi_i have zero real part. Finite-N critical
actions are kept in the core's relative asymptotic; only their proved
uniform limit is used here. This is a SUFFICIENT shared-radius corridor.
The local-G test is only one way to satisfy it. Some actual boundary
quartets fail (13); no universal certificate or positivity,
far-color bound, genuine-q normal identity, or filling transfer follows.

## 7. A certified actual local instance and validation

The criterion is not merely an open locus of unrelated curvature
data. The already used actual width-three flat plat with box word
[1,3,0,2,4,1,3], protected faces 0,8, has an exact marked strip
packing with finite curvatures (25,9,16,4,1,9,1). At its zero-based
port 3 the actual quartet (x,b,c,y) is (4,9,1,1), with distinct
unmarked middle faces. Here G=log9 by the dominant-side case, and

    F(4,9,1)+F(4,1,1)-log9 > 0.45.                (17)

The audit gives rational centers/radii, verifies every white
contact/noncontact and shaded supporting-circle inequality on the
original face chart, and certifies (17) by a finite Lobachevsky
series with its explicit analytic tail. This supplies an actual
one-port instance of (13b), not a claim that all actual diagrams
satisfy (13). For the stronger simultaneous theorem, (13b) must be
verified for every nonempty subset of the chosen E.

Focused audit: [original local matrices, full sources and certificate](../experiments/audit_actual_homogeneous_casimir_face_source.py),
with [saved results](../experiments/actual_homogeneous_casimir_face_source_results.json).
The local checks retain arbitrary polynomial coupons, both crossing
signs with lambda0, wrong unwrapped totals, and complete-channel
phases. The whole checks use original cups/caps/unrestricted mark,
compare coefficient extraction with full physical contractions, and
independently average the original even/odd face grids on selected
fixtures. They include all-deleted and disconnected substitutions.
These finite checks support the exact proof; they do not numerically
prove universal shared-radius certificates or a volume limit.

The source audit compares complete and signed polynomial coefficients, retained crossing phases, physical entries, whole sources and face-grid points, including illegal-total zeros. It also checks exact white and shaded support. The geometric gap is certified by a 256-bit outward-rounded Arb evaluation of a 100-term Lobachevsky series, with total tail below 0.01910 and lower bound above 0.46643723013, stronger than (17).

The conclusion retains the sufficient-certificate, physical-root and fixed-presentation scope.