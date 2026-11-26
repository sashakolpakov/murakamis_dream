# A unified balanced original plat family for every k>=2

PRIVATE THEOREM FOR INDEPENDENT REVIEW, 31 October 2026. This is a
right-end extension of the reviewed reduced-layer construction. It
retains the original flat-plat source, first-cap mark, all half twists
and all independently signed full twists. The proof covers EVERY k>=2;
it does not assert balance for every certified plat.

## 1. Exact word and conclusion

Number physical adjacent slots from0 to2k-2, so slot j is conventional
braid generator sigma_(j+1). Define

 O_k=(1,3,...,2k-3),
 E_k^right=(2,4,...,2k-2),
 D_k^right=O_k E_k^right O_k,       R=3k-3.                  (1)

Keep the standard adjacent cup/cap pairs and mark the FIRST original
top cap on slots(0,1). In conventional generator notation, the actual
filled braid is

 prod_(j=1)^(k-1) sigma_(2j)^(epsilon_j-2p_(1,j))
 prod_(j=1)^(k-1) sigma_(2j+1)^(-2p_(2,j))
 prod_(j=1)^(k-1) sigma_(2j)^(-2p_(3,j)),                   (2)

with each epsilon_j=+1 or-1 fixed. All products retain bottom-to-top
order and increasing j within the layer. The first O layer is odd;
the other two layers are even. Its plat is therefore a knot, as checked
again below.

THEOREM. For every fixed k>=2 and fixed first-layer sign pattern there
is a threshold T(k,epsilon) such that for EVERY integer vector p with
all |p_(r,j)|>=T, fixed before N tends to infinity, the full original
normalized root invariant obeys

 lim_(N->infinity) (2pi/N) log|K_N(K_k(p))|
                      =Vol(S^3 minus K_k(p)).              (3)

All 3k-3 twist parameters can have independent signs and magnitudes.
The result holds at both level parities. No comparability of twist
magnitudes or joint growing-twist/level limit is asserted. Moreover,
in the congruence subfamily where every exponent in(2) is divisible
by3, the minimal bridge number is EXACTLY k. The congruence is used
only for that lower bound, not for(3).

The analytic implication is the already proved general complete-radius
balance theorem. It remains to prove its hypotheses for the actual
source(1), uniformly in k, which occupies Sections2-5 below.

## 2. Literal incidence, simple certificate and reflection

Let u be the exterior, a_0,...,a_(k-1) the bottom odd-gap faces, and
e_1,...,e_(k-1) the first-layer bounded even-gap faces. The middle
layer changes a_j to b_j for EVERY1<=j<=k-1, while a_0 remains
unchanged. Set b_0=a_0 and e_k=u. All other names are distinct.
The literal gap sweep gives

 first O: (a_(j-1),u,e_j,a_j),       1<=j<=k-1;
 middle E: (e_j,a_j,b_j,e_(j+1)),    1<=j<=k-1;
 final O: (b_(j-1),e_j,u,b_j),       1<=j<=k-1.              (4)

Each quartet has the original two triangles (x,b,y),(x,y,c). The
protected pair is u,a_0 on its original MAIN edge. There is no graph-
to-plat adapter or isotopy in this description.

The MAIN edges are u-a_i, u-b_i (sharing only u-a_0 at the left end)
and e_j-a_(j-1), e_j-a_j, e_j-b_(j-1), e_j-b_j (sharing only e_1-a_0).
The MATCHING edges are the two chains a_(j-1)-a_j and b_(j-1)-b_j,
and the chain e_1-e_2-...-e_(k-1)-u. All these edges have distinct
endpoints; none is repeated as a separate edge. This includes k=2:
the three matching edges are a_0-a_1,a_0-b_1,e_1-u. Every listed
edge is incident to exactly two of the actual triangles in(4), by the
same gap incidence pairing as in the reduced family, with the right
middle-E box now closing against the exterior. The inherited sphere has

 V=3k-1,        E=9k-9,        F=6k-6,        V-E+F=2.       (5)

Thus the white cellulation is a simple triangulated sphere for EVERY
k>=2. The existing simple-block construction gives the actual labeled
convex ideal right-angled packing and its original two cut balls.

There is an orientation-reversing sphere automorphism a_i<->b_i,
fixing u,a_0,e_1,...,e_(k-1), and interchanging the first/final layers.
Normalize the original marked tangency u-a_0 to infinity, with u the
outside lower half-plane Y<=0 and a_0 the outside upper half-plane
Y>=2. Uniqueness of the marked positive curvature solution up to
scale, followed by unique contact-center development, realizes the
automorphism by a vertical reflection. Translate its axis to X=0.
This is precisely the uniqueness/reflection argument in the reviewed
reduced-family proof, with the same connected ordinary-face Hessian.
In particular the ACTUAL curvatures satisfy A_i=B_i.

Put L=k-1. The fixed graph cycle is

                   u-a_0-e_1-e_2-...-e_L-u.

It separates the original sphere into the a-side and b-side triangulated
disks. The ordered axis chain now runs from the upper marked line
through e_1,...,e_L to the LOWER marked line, with NO extra endpoint
a-circle on the axis. All a_i lie on one side, all b_i on the other:
this follows from the consistently oriented a-side triangles along
the fixed chain, including the last triangle(a_L,e_L,u). Choose the
a-side to be X>0. The fixed disks have disjoint axis intervals, ordered
strictly from top to bottom. Write

 y_0=2>y_1>...>y_(L-1)>y_L=0,
 radius(e_j)=(y_(j-1)-y_j)/2,
 E_j=curvature(e_j)=2/(y_(j-1)-y_j).                       (6)

For L=1 this means e_1 is the unit disk centered at(0,1).

## 3. Height recurrence with the correct right boundary

For1<=i<=L-1 the ordinary right-side circle a_i is tangent to u and
both e_i,e_(i+1). If its center is(X_i,r_i), elementary tangency gives

 2r_i=y_i(y_(i-1)-y_(i+1))/(y_(i-1)-y_i),
 X_i^2=y_(i-1)y_i(y_i-y_(i+1))/(y_(i-1)-y_i).              (7)

These are actual squared-distance identities, not a continuation past
a zero height. The final circle a_L is treated separately in Section5.

Set

 z_j=sqrt(1-y_j/y_(j-1)),   1<=j<=L;
 z_0=0,                   z_L=1.                         (8)

For L>=2 the first pair a_1,b_1 touches BOTH marked lines, so r_1=1.
Using y_0=2 in(7) gives

                       (1-z_1^2)(1+z_2)=1.               (9)

At every other interior index2<=j<=L-1 use actual tangency of
consecutive right-side circles a_(j-1),a_j. With p=z_(j-1),z=z_j,
w=z_(j+1),q=1-z^2, the same substitution as in the reduced proof gives

               1-2q(1+pw)+q^2(1-p^2)(1-w^2)=0.            (10)

For w<1, its second root1/[(1-p)(1-w)] exceeds1 and is excluded by
the actual height ratio0<q<1. At the LAST such index w=z_L=1, the
quadratic becomes the exact LINEAR equation1-2q(1+p)=0. Both cases,
together with(9), yield

 (1+z_(j-1))(1-z_j^2)(1+z_(j+1))=1,
                         1<=j<=L-1.                      (11)

There is NO equation at j=L and no evaluation of f at log2 below.
This is the new boundary condition; the old zero-endpoint equation
must not be imposed on the added end box.

## 4. Uniform interior bound, including k=2 and k=3

For L>=3 let v_j=log(1+z_j), with v_0=0, v_L=log2 and
0<v_j<log2 at all interior indices. The same strictly convex function

 f(v)=-v-log(2-exp v),        f(0)=0,
 f''(v)=2exp(v)/(2-exp(v))^2>0

satisfies

                    f(v_j)=v_(j-1)+v_(j+1),
                               1<=j<=L-1.                 (12)

Place the exact three-node seed

                  (log(5/3),log(9/5),log(5/3))

at ANY consecutive three positions among1,...,L and extend by zeros.
Call the resulting vector s, with s_0=0. At every interior index,
f(s_j)<=s_(j-1)+s_(j+1), while the RIGHT boundary automatically obeys
s_L<=log2=v_L. Put t=max_(1<=j<=L)(s_j/v_j). If t>1, its attaining index must be interior.
At that index strict convexity gives f(s_j)>t f(v_j), while the neighbor
comparison gives f(s_j)<=t f(v_j), a contradiction. Therefore v>=s.
Every interior index lies in a translated seed, so

                         z_j>=2/3,  1<=j<=L-1.             (13)

The inclusion of position L in a translated seed is legitimate because
it is compared only as a boundary value; f(log2) is NEVER evaluated.

For L=2, equation(9) with z_2=1 gives z_1=1/sqrt2>2/3 exactly. For
L=1 there is no interior index. Thus(13) holds wherever needed for
EVERY k>=2, with these exact small-width interpretations.

## 5. Curvature ratios and the last physical interstice

For j<L, let p=z_(j-1), z=z_j and D_0=p^2+z^2-p^2z^2>0.
The physical formulas(7) and recurrence(11) give exactly

 A_(j-1)/E_j=p^2z^2/D_0,
 A_j/E_j=z^4(1+p)^2/D_0,
 (A_(j-1)+A_j)/E_j
       =z^2[1+2p(1+p)z^2/D_0]>=z^2.                     (14)

At j=1 this includes A_0=0 and r_1=1. At j=L-1 it uses w=1 only
through the valid LINEAR boundary recurrence, and all circles in(7)
are still genuine finite disks. Therefore(13),(14) give

                    E_j/(A_(j-1)+A_j)<=9/4,
                                      1<=j<L.             (15)

It remains to check the actual FINAL O ports, involving e_L and a_L.
For L>=2, the circle a_L has exactly three white neighbors: the lower
line u, e_L, and a_(L-1). These three neighbors are pairwise tangent.
The a-side disk decomposition places a_L in their bounded curvilinear
interstice next to the u-e_L contact; its reflected partner lies in
the opposite interstice. The positive Descartes branch is consequently

 A_L=A_(L-1)+E_L+2sqrt(A_(L-1)E_L).                        (16)

There is also a direct physical branch check requiring only the already
proved same-side development. Put H=y_(L-1) and p=z_(L-1) in(0,1).
Formula(7) gives X_prev=H/p>H and 2r_prev=H/p^2, while radius(e_L)=H/2.
For a_L centered at(X,r), tangency to u and e_L gives X^2=2Hr.
Tangency to a_prev then gives |1/X-1/X_prev|=1/H. Since X_prev>H
and X>0, the only positive solution is

                       X=H/(1+p).

Consequently A_L=2(1+p)^2/H=(sqrt(A_prev)+sqrt(E_L))^2, proving(16)
without an arbitrary Descartes-root choice. It also agrees with the
original bounded-gap contact order. In particular A_L>=E_L, so

                   E_L/(A_(L-1)+A_L)<=1.                  (17)

For L=1, the actual marked strip contains e_1 of radius1 at(0,1)
and a_1,b_1 of radius1 at(2,1),(-2,1). Thus E_1=A_1=B_1=1 and
(17) holds directly with A_0=0. This is the literal word(1,2,1),
not a changed marking of the reduced width-two word.

Equations(15),(17) establish the zero-middle bound E/(x+y)<=9/4
at EVERY first/final O port. The independently proved source-normalized
nine-quarter lemma gives strict balance there, with gap>1/2500.
At EVERY middle-E port, INCLUDING the last port with outer u=0,
the two positive middles have equal curvatures A_j=B_j. Since the
outer sum E_j+E_(j+1)>0 (with E_(L+1)=0), the original strict inequality
Q(x,A_j,y)>(1/2)log A_j gives balance there as well. There is no
exception at a protected outer line.

Thus EVERY port passes the actual complete-radius balance test for
EVERY k>=2, in ONE shared original marked packing.

## 6. Full source, knot parity and exact bridge subfamilies

The general complete-radius balance filling theorem now proves(3),
including the full original one-sided remainder, the entire all-charge
period, the original normalization and both parities. Its threshold
can depend on the fixed diagram and prescribed parity, and no claim
is made for arbitrary certified diagrams failing balance.

The first O layer has odd exponent on the zero-based slots1,3,...,2k-3.
The resulting transpositions(1 2),(3 4),...,(2k-3 2k-2) join the initially
k cap components successively. All remaining boxes have even exponent.
Therefore the original endpoint-pairing graph is one cycle and the
plat in(2) is a knot. This argument includes k=2 and does not confuse
zero-based slots with conventional generator indices.

The Fox-coloring certificate applies without change: if every actual
exponent in(2) is divisible by3, every full crossing box acts as the
identity on ordered F_3 colors, and the standard cup/cap register has
exactly3^k colorings. Any b-bridge knot has at most3^b colorings.
Together with the supplied k-bridge plat this gives minimal bridge
number exactly k. Each required exponent congruence is compatible
with its prescribed parity and independent arbitrarily large signed
full twists. This identifies unbounded actual bridge complexity,
without putting a congruence restriction on the volume theorem.

No finite search over k or numerical packing values are used to prove
this uniform statement. The previously reviewed reduced-family proof
supplies the recurrence algebra, comparison principle and source Q
normalization; this note proves the changed right boundary and the
literal all-width incidence explicitly.
