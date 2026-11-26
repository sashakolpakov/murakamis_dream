# An actual balanced source family at every width k>=4

PRIVATE PROOF FOR INDEPENDENT REVIEW, 31 October 2026. This proves a
uniform geometric certificate for ONE explicit family of original flat
plats. The general complete-radius balance theorem applies to every
certified diagram that passes its test; the family here establishes
nonvacuity at unbounded actual bridge complexity. It does not assert
balance for every simple-white plat. The analogous reduced width-three
word does not pass this test and is not included.

## 1. Literal source word, mark, and simple white sphere

Use ZERO-BASED adjacent physical slots 0,...,2k-2. Slot j is the braid
generator usually denoted sigma_(j+1). The standard bottom and top cup
pairs are (0,1),(2,3),...,(2k-2,2k-1). For k>=3 put

 O_k=(1,3,...,2k-3),
 E_k^int=(2,4,...,2k-4),
 D_k=O_k E_k^int O_k,                R=3k-4.                 (1)

These are the ORIGINAL bottom-to-top box slots, without an isotopy,
Markov stabilization, or abstract graph-to-plat adapter. Mark the FIRST
original top cap, on slots (0,1).

Name the exterior u, bottom odd-gap regions a_0,...,a_(k-1), and bounded
even-gap regions e_1,...,e_(k-1). The internal middle layer replaces
a_j by b_j for 1<=j<=k-2. Set b_0=a_0 and b_(k-1)=a_(k-1), because
there are NO boxes in slots0 or2k-2. All other named regions are distinct.
The original gap sweep gives exactly

 first O: (a_(j-1),u,e_j,a_j),          1<=j<=k-1;
 middle E: (e_j,a_j,b_j,e_(j+1)),       1<=j<=k-2;
 final O: (b_(j-1),e_j,u,b_j),          1<=j<=k-1.            (2)

A quartet (x,b,c,y) contributes the actual triangles (x,b,y),(x,y,c).
The protected regions are precisely u and a_0. Their edge is MAIN.

The white MAIN edges are u-a_i and u-b_i, with the two named endpoint
identifications retained; and e_j-a_(j-1), e_j-a_j, e_j-b_(j-1), e_j-b_j,
again retaining the two endpoint identifications. The MATCHING edges
are the two chains a_(j-1)-a_j and b_(j-1)-b_j, together with the
internal chain e_j-e_(j+1). For k>=3 no listed edge has equal endpoints,
and there are no parallel edges: the two a/b chains have distinct
interior vertices and share only their two endpoints. Each listed edge
is incident to exactly two of the triangles in (2). At the left end,
for example, e_1-a_0 is shared by the first-O output and final-O input
triangles, while u-a_0 is shared by their other triangles. The right end
is identical. The remaining e_j MAIN incidences close against the
appropriate middle-E triangle; the remaining u incidences close between
consecutive O boxes. Every matching edge pairs its own original box.

Thus this is the actual simple triangulated sphere, with

 V=3k-2,       E=9k-12,       F=6k-8,       V-E+F=2.          (3)

The sphere topology and cyclic order are inherited from the original
Morse construction, not inferred only from Euler characteristic. The
proved simple-block construction in actual_smoothed_source_capacity_blocks
§§4-5 therefore supplies the ACTUAL labeled convex ideal right-angled
certificate and its two original cut balls. In particular (1) is a
certified source diagram for every k>=3.

## 2. The actual reflection packing and height coordinates

The white sphere has the reflection automorphism a_i<->b_i fixing
u,a_0,a_(k-1), and every e_j. It exchanges the first and last layers,
with the original cyclic order reversed. Normalize the marked tangency
u-a_0 to infinity, with the white disks u and a_0 the outside half-planes
below Y=0 and above Y=2. All ordinary disks lie inside this strip.

This automorphism is realized by a reflection of the actual packing.
One way to justify the needed uniqueness is the proved strictly convex
marked angle potential: after fixing the common scale, its ordinary-face
Hessian is a connected positive graph Laplacian. Equivalently, the
maximum-ratio argument for two positive curvature solutions propagates
strictness along every ordinary adjacency until it reaches a fixed
normalization. The normalized radii then determine the contact-center
development uniquely up to a horizontal Euclidean isometry. The
orientation-reversing automorphism preserving BOTH marked lines
individually is therefore a vertical reflection; translate its axis to
X=0. Write a_i for both the named disk and its positive CURVATURE when
no confusion results. Then a_i=b_i.

Put L=k-1. The fixed disks form the actual tangent chain

 a_0(line Y=2), e_1,e_2,...,e_L,a_L,u(line Y=0).

Their centers lie on X=0. Disjoint interiors, successive tangencies and
the two endpoint lines force their intervals to be ordered strictly
from top to bottom. Write y_0=2, and y_j for the contact height between
e_j and the next fixed disk, 1<=j<=L. Consequently

 2=y_0>y_1>...>y_L>0,
 radius(e_j)=(y_(j-1)-y_j)/2,
 radius(a_L)=y_L/2.                                        (4)

The fixed graph cycle u-a_0-e_1-...-e_L-a_L-u divides the original
white sphere into two triangulated disks: all interior a_i belong to
one disk, all interior b_i to the other. In the consistently oriented
a-side development, the triangles (a_i,e_i,e_(i+1)) all lie on the same
side of their downward-directed fixed-chain center edges. Their
original cyclic orders therefore put EVERY a_i on the same side of
X=0; one cannot choose these signs separately. The reflection puts
all b_i on the opposite side. Choose the a-side to be X>0. Thus for
1<=i<=L-1 each reflected pair consists of two DISTINCT disks, and the
a_i center is (X_i,r_i) with X_i>0, where r_i is its Euclidean radius. These disks are
tangent to u and to e_i,e_(i+1). The first pair is also tangent to the
upper line a_0, hence r_1=1. The last a_L is the single axis disk.

Elementary squared-distance tangency gives EXACTLY

 2r_i = y_i(y_(i-1)-y_(i+1))/(y_(i-1)-y_i),
 X_i^2 = y_(i-1)y_i(y_i-y_(i+1))/(y_(i-1)-y_i).             (5)

For clarity, a circle of radius r centered at (X,r), tangent to the
axis circle whose bottom/top heights are U,V, satisfies X^2=V(2r-U).
Applying this to the two neighboring fixed circles proves (5). No
circle-packing approximation is used.

## 3. Exact scalar recurrence, with its branch fixed by geometry

Define

 z_j=sqrt(1-y_j/y_(j-1)),  1<=j<=L;
 z_0=z_(L+1)=0.                                          (6)

All actual z_j lie strictly between0 and1. I claim

 (1+z_(j-1))(1-z_j^2)(1+z_(j+1))=1,
                      1<=j<=L.                           (7)

At j=1, r_1=1 and y_0=2 in (5) imply
z_2=z_1^2/(1-z_1^2), which is (7). At the other end, tangency of
a_(L-1) to a_L at X=0 gives X_(L-1)^2=2r_(L-1)y_L.
Equation (5) then gives

y_L=y_(L-2)-sqrt[y_(L-2)(y_(L-2)-y_(L-1))],

where the plus root is excluded by y_L<y_(L-1). Hence
z_L^2=z_(L-1)/(1+z_(L-1)), again (7).

For an interior j put p=z_(j-1), z=z_j, w=z_(j+1), and q=1-z^2.
The positive horizontal coordinates and radii of the two consecutive
right-side disks, normalized by y_(j-1), are

 X_(j-1)/y_(j-1)=z/p,
 X_j/y_(j-1)=q w/z,
 2r_(j-1)/y_(j-1)=[p^2+(1-p^2)z^2]/p^2,
 2r_j/y_(j-1)=q[z^2+q w^2]/z^2.                           (8)

Their literal tangency is (X_(j-1)-X_j)^2=4r_(j-1)r_j. Substitution
and cancellation of the positive factor y_(j-1)^2/p^2 gives

 1-2q(1+pw)+q^2(1-p^2)(1-w^2)=0.                          (9)

The two possible roots are

 q=1/[(1+p)(1+w)]   or   q=1/[(1-p)(1-w)].                 (10)

The second root is strictly greater than1 since p,w>0, whereas the
actual height ratio q lies in(0,1). This excludes it before making
any reconstruction or selecting a formal branch. The first root is
precisely (7). The interior proof needs no order assumption on the two
positive horizontal centers beyond the actual tangency.

## 4. A comparison principle gives the uniform 2/3 bound

Set v_j=log(1+z_j), so 0<v_j<log2 and v_0=v_(L+1)=0. Define

 f(v)=-v-log(2-exp(v)).

Equation (7) becomes

 f(v_j)=v_(j-1)+v_(j+1).                                  (11)

On[0,log2), f(0)=0 and

 f''(v)=2exp(v)/(2-exp(v))^2>0.

In particular f(tv)>t f(v) whenever t>1 and 0<v<tv<log2.

For L=3 the explicit positive solution is

 (z_1,z_2,z_3)=(2/3,4/5,2/3),
 (v_1,v_2,v_3)=(log(5/3),log(9/5),log(5/3)).              (12)

Direct substitution verifies all three equations and both zero
boundary values. For any L>=3, place this three-node vector at ANY
three consecutive positions and extend it by zeros elsewhere, calling
the resulting vector s. It satisfies

 f(s_j)<=s_(j-1)+s_(j+1),                                 (13)

including at every zero position next to its support. If some s_j>v_j,
let t=max(s_j/v_j)>1 and choose an attaining index. There s_j=t v_j,
so strict convexity gives f(s_j)>t f(v_j). On the other hand (13) and
the maximal-ratio property give

 f(s_j)<=s_(j-1)+s_(j+1)
         <=t[v_(j-1)+v_(j+1)]=t f(v_j),

a contradiction. Thus v dominates every translated three-node vector.
Every index1,...,L belongs to such a placement, and the smallest
nonzero seed entry is log(5/3). Therefore for EVERY k>=4,

                         z_j>=2/3  for all j.             (14)

This comparison uses the ACTUAL packing solution already constructed
from the source certificate. It does not require a shooting guess or
a new nonlinear existence theorem. It also establishes the bound for
every interior index, not just for the two ends.

## 5. Exact curvature comparison and strict source balance

Let E_j denote the curvature of e_j and A_i the curvature of a_i,
with A_0=0. From (4),(5), with p=z_(j-1), z=z_j, and
D_0=p^2+z^2-p^2z^2>0, equation (7) simplifies the two adjacent
curvature ratios to

 A_(j-1)/E_j = p^2 z^2/D_0,
 A_j/E_j     = z^4(1+p)^2/D_0.                            (15)

At j=1 the first ratio is0 and the second is z_1^2 because r_1=1;
at j=L the second formula is the actual endpoint curvature2/y_L.
Thus (15) includes BOTH boundary cases with their original zero/axis
interpretation, not a continued finite-circle formula imposed there.
Adding gives

 (A_(j-1)+A_j)/E_j
 =z_j^2[1+2p(1+p)z_j^2/D_0]>=z_j^2>=4/9.

Consequently

                    E_j/(A_(j-1)+A_j)<=9/4                (16)

at every first/final O port, uniformly for all k>=4.

The independently checked zero-middle lemma
/private/tmp/md-zero-middle-nine-quarter-balance.md uses the ORIGINAL
absolutely normalized triangle action Q and proves

 Q(x,E,y)+Q(x,0,y)-log E>1/2500
       whenever x+y>0 and E/(x+y)<=9/4.                    (17)

It retains either protected zero outer corner. Its proof is elementary:
at fixed A=x+y the cofactor Perron action increases with P=xy; the
worst boundary value at E/A=9/4 is
(2/pi)Ti2(2/3)-log(3/2), which has an exact rational positive lower
bound from four alternating Ti2 terms and the atanh series for log.
Thus every O port passes the actual complete-radius balance condition.

At each internal E port the two middle curvatures are equal,
A_j=B_j>0, while both outer curvatures are positive. The original
strict inequality Q(x,A_j,y)>(1/2)log A_j gives
2Q(x,A_j,y)>log A_j. Thus EVERY port in the literal diagram (1)
satisfies the balance condition, using ONE common marked packing.
No independent local radius optimization or entropy min/max exchange
is involved.

## 6. General-theorem coverage, knot parity, and genuine width

The general balanced-diagram long-filling theorem therefore applies
to D_k for every k>=4 and every fixed half-twist pattern. For each
fixed k and source pattern there is a diagram-dependent threshold;
all fixed filling powers beyond it may have independent signs and
magnitudes. The family construction places no comparison constraint
between these powers and no joint growing-twist/level limit.

For knot parity put epsilon=+1 or-1 on EACH box of the FIRST O layer,
and zero on the other boxes. The first-layer zero-based transpositions
(1 2),(3 4),...,(2k-3 2k-2) merge the k initially separate cap cycles
successively; each joins two previously different components. Every
other box has even exponent and trivial endpoint permutation. Thus
the filled main diagram is a knot for every integer full-twist vector.
This is a direct computation on the original cups and slots.

There are genuinely unbounded minimal bridge numbers inside this
family, not merely arbitrarily wide presentations of two-bridge knots.
Require additionally that every actual exponent n_i=epsilon_i-2p_i
be divisible by3. This is one residue class of p_i modulo3, compatible
with all retained parities and arbitrary independent large signs.
The Fox-coloring crossing operator on ordered strand colors is
T=[[2,-1],[1,0]] over F_3; (T-I)^2=0 and T^3=I, for either signed
crossing convention. Every whole box therefore acts identically on
slot colors, though odd boxes still permute strand endpoints. The
k independent adjacent bottom-cup colors survive every top cap, so
the knot has exactly3^k Fox 3-colorings. Any b-bridge diagram has at
most3^b such colorings, because colors on its b overpassing bridges
determine every underpassing segment by the crossing rule. Reidemeister
moves preserve colorings, so b(K)>=k; the supplied plat gives b(K)<=k.
Hence b(K)=k for this congruence subfamily. The independent full proof
is /private/tmp/md-fox-coloring-exact-plat-bridge-certificate.md.

The congruence condition is used ONLY for this bridge lower bound.
The analytic volume theorem still covers ALL independently long powers
in the prescribed knot parity. Conversely, this explicit family is
not claimed to exhaust balanced diagrams, all simple-white diagrams,
or all k-bridge knots. The present uniform construction covers k>=4;
it makes no balance claim for the reduced k=3 word.
