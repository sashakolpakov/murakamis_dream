# An exact balanced literal width-three seed

PRIVATE proof for independent review, 31 October 2026. This is one literal
six-strand plat family, with the original first top-cap mark. It completes
the missing width three in the separately proved k>=4 reduced-layer family;
it does not assert balance for arbitrary width-three diagrams.

## 1. The original diagram and its white sphere

Use zero-based box slots and the bottom-to-top word

  D_3=(1,3,2,4,1,3).

The first two boxes have prescribed half twists epsilon_1,epsilon_2 in
{+1,-1}; the other four have epsilon=0. Mark the first original top cap,
on slots(0,1). In conventional braid generators the full knot is the
standard six-strand plat of

 sigma_2^(epsilon_1-2p_1) sigma_4^(epsilon_2-2p_2)
 sigma_3^(-2p_3) sigma_5^(-2p_4)
 sigma_2^(-2p_5) sigma_4^(-2p_6).

Every p_i is an independently chosen signed integer. These are the actual
boxes, not an isotopic drawing or an abstract matched-graph realization.

Name the eight source faces u,a0,a1,a2,e1,e2,b1,b2, in that order. The literal
Morse gap sweep gives exactly the six quartets

 (a0,u,e1,a1), (a1,u,e2,a2), (e1,a1,b1,e2),
 (e2,a2,b2,u), (a0,e1,u,b1), (b1,e2,u,b2).                 (1)

The protected faces are u,a0. A quartet(x,b,c,y) supplies the actual two
triangles(x,b,y),(x,y,c). The resulting twelve triangles are distinct; their
eighteen edges each occur twice, with no loop or parallel edge. Thus the
original white sphere is simple, with (V,E,F)=(8,18,12). The sphere and its
cyclic orders are those of the original gap sweep. Its protected edge u-a0
is MAIN. The proved simple-white certificate therefore applies.

## 2. Exact original marked packing

Normalize the protected disks u,a0 as the exterior halfplanes below Y=0 and
above Y=2. Put q=sqrt(2), r=3-2q>0. The six finite disks have the following
centers and Euclidean radii:

 face    center                   radius
 a1      (q,1)                    1
 a2      (2-q,r)                  r
 e1      (0,3/2)                  1/2
 e2      (0,1/2)                  1/2
 b1      (-q,1)                   1
 b2      (q-2,r)                  r.                       (2)

All radii are positive. Direct distance identities show that the tangent
pairs are EXACTLY the eighteen original white edges, including the
protected line-line tangency at infinity. For clarity, for two finite
circles use the squared-distance slack

 |center_i-center_j|^2-(radius_i+radius_j)^2,

and for a line use distance(center,line)-radius. Every original edge has
zero slack. Every nonedge has positive slack, drawn from the exact list

 1, 4(q-1), 4, 8(q-1), 32q-44.                            (3)

The last is positive since (32sqrt2)^2=2048>1936=44^2. These checks also
show that every finite disk lies in the strip and that no unintended
contact is introduced. The triangular gaps are exactly the twelve
original listed faces: this can be checked directly from (1),(2), with
a1,a2 on the right and b1,b2 on the left. Hence (2) is a packing of the
actual labeled sphere in its actual cyclic order, up to the one global
orientation choice. The uniqueness of the normalized marked packing
identifies it with the complete source packing; no independent local
weights are being chosen.

The actual curvatures are therefore

 u=a0=0,   a1=b1=1,   e1=e2=2,
 a2=b2=1/r=3+2sqrt2.                                      (4)

## 3. Every original port is strictly balanced

The first, second, fifth and sixth quartets in (1) have one zero middle.
The positive middle is always e_j=2. Their outer sums are respectively
1, 4+2sqrt2, 1, 4+2sqrt2. Thus every such ratio satisfies

 positive_middle/(sum of outers) <=2 <9/4.

The proved source-normalized zero-middle 9/4 lemma gives strict balance
with gap greater than1/2500, including the first/fifth protected-zero
outer corner. The third and fourth quartets have equal positive middles:
a1=b1 and a2=b2. Their outer sums are respectively4 and2. The original
strict inequality Q(x,b,y)>(1/2)log b for b>0 and x+y>0 therefore supplies
strict balance at these ports too. The fourth port retains the actual
zero outer u; the inequality is valid there by its exact one-line formula.

Thus ALL six original ports pass the complete-radius balance test on the
ONE actual packing (2), for either choice of each fixed first-layer sign.

## 4. Knot parity, full volume theorem and exact bridge subfamily

Only the first two boxes have odd exponents. Their zero-based endpoint
transpositions(1 2),(3 4), with the standard adjacent cups and caps, give
one component. This is the usual chain joining the three lower cup pairs;
the remaining even boxes have identity permutation. Therefore every
integer filling vector produces a knot in this prescribed parity.

By the general complete-radius balance theorem, for each fixed pair
(epsilon_1,epsilon_2) there is T>0 such that every fixed independently
signed vector with all |p_i|>=T satisfies

 lim_(N->infinity) (2pi/N)log|K_N(K_3(p))|
     = Vol(S^3 minus K_3(p)).                             (5)

This is the FULL original normalized root invariant, both level parities,
and the entire charge sum, through that theorem. The twist parameters are
fixed before N tends to infinity; no bound on their mutual ratios is
imposed. Hyperbolicity/smooth filling is part of the cited sufficiently
long threshold.

For an exact minimal-bridge subfamily impose additionally 3|(epsilon_i-2p_i)
at every box (epsilon_i=0 after the first two). The exact Fox-coloring
certificate then gives 3^3 colorings. Since the diagram is a knot and has a
six-strand plat presentation, its minimal bridge number is exactly3.
The congruence is needed only for this lower bound; (5) covers every
independently sufficiently long filling vector in the fixed knot parity.

## Verification scope

The companion exact audit compares (1) against the original Morse compiler,
checks every pair support in Q(sqrt2), all triangle incidences and the
literal component permutation. It does not numerically infer the volume
limit: (5) follows from the reviewed balance theorem and exact certificate.
