# One-sided comparison atoms, their convex mixtures, and the missing geometric adapter

PRIVATE analytical audit, 31 October 2026. No workspace/public files are
changed. This assesses the original LEFT/CROSS/RIGHT weighted comparison,
not the phase-sensitive source itself. It gives an exact obstruction to
reusing the existing hybrid circle-development proof without a new adapter;
it does not prove that an optimized comparison capacity exceeds volume.

## 1. Exact source conventions and the two pure atoms

For an original port (x,b,c,y), LEFT has the proved real-spectral weighted
upper rate

    L(l)=max{ log c, Q(x,b,y)+(1/2)log c }.                 (1)

Here every Q is the actual half-degree triangle action, with

    Q(w)=max_{alpha>=0, sum alpha=1/2}
              [ C(alpha)+sum_j alpha_j log w_j ],
    C(alpha)=sum_j f(alpha_j),
    f(s)=[Lambda(pi s)+Lambda(pi/2-pi s)]/pi.              (2)

There is no additive constant or change of original face targets. Each
ordinary face has load one and the two protected faces load zero. All
four incidences remain in their original positions. If c is protected,
the finite LEFT sector is identically zero; it is not assigned a positive
regularized geometric value here.

The second atom forces the output $(0,1/2,0)$; the first pure-middle atom has the stated identity contribution. The linked triangle-capacity duality retains these boundary allocations.

There is also a useful uniform statement for arbitrary pure atom patterns.
Choose, at every selected LEFT/RIGHT port, either its identity endpoint or
its fixed output/input half-triangle; leave other ports CROSS. At every
such allocation the proposed entropy is EXACTLY the frozen full endpoint
entropy h at the same original degree vector: at a pure middle endpoint
h=0, and at the half seam h is the one retained triangle entropy. The
whole source balance equations are unchanged. Every nonempty pure atom
pattern therefore lies in the closed set with some middle load >=1/2.
The unique geometric endpoint theorem gives the SAME fixed positive
one-sided gap on that closed set. Empty polytopes have value -infinity.

Thus the pure patterns themselves are not the unresolved comparison.
Their strictness can be proved by the existing actual endpoint geometry,
or by the fixed-triangle lemma and actual identity-smoothing bounds.

## 2. The exact convexified comparison problem

For positive face weights, (1)--(2) give the identity

    L(l)=max_{0<=t<=1, alpha>=0, sum alpha=1/2}
       [ t C(alpha)+t alpha_x log x+t alpha_b log b
           +t alpha_y log y+(1-t/2)log c ].              (3)

The corresponding original degree vector is

    q_x=t alpha_x, q_b=t alpha_b, q_y=t alpha_y,
    q_c=1-t/2.                                         (4)

It has total degree one and q_c>=1/2. For q_c<1 put

    t=2(1-q_c),
    h_env(q)=t C(q_x/t,q_b/t,q_y/t);                    (5)

at q=e_c define h_env=0. This perspective is concave and continuous on
its whole closed LEFT simplex: C is concave and bounded, and t C tends
uniformly to zero as t tends to zero. RIGHT is its literal reflection.
At CROSS ports keep the two original half-triangle allocations.

For any fixed actual LEFT/CROSS/RIGHT sector, minimizing the sum of these
weighted expressions minus the original ordinary log targets is exactly
the maximum of the corresponding sum of h_env and triangle entropies on
the original incidence-flow polytope. This follows from compact concave
hypograph separation, including infeasible and nonattained cases, by
the same proof as the fixed-triangle duality. This is a proved convex
duality statement, not an interchange of infimum with the finitely many
pure atom patterns.

The variables t in (3) are independent continuous optimization variables.
The pure patterns are t in {0,1}; restricting to them need not preserve
the maximum of a concave objective. Therefore strict gaps for every pure
pattern do not by themselves prove the fixed-sector envelope gap.

## 3. This is not the actual Green entropy

The actual positive LEFT coefficient entropy is

    h(q)=E(q_b,1-q_c,q_x),                             (6)

not (5). An exact source coefficient makes the distinction quantitative.
At q=(1/4,0,3/4,0), the source's single-x path gives

    h(q)=2 integral_0^(1/4) log tan(pi s) ds
        =-2 Catalan/pi <0,

whereas t=1/2 and alpha=(1/2,0,0) give h_env(q)=0.
The frozen entropy-sign note proves this from the literal coefficient,
with its scalar normalization retained. It is not a numerical example.
By continuity the strict inequality persists at strictly positive local
degree vectors. More explicitly, the previously proved diagonal expansion
gives, as epsilon tends to zero through positive values,

    q=(epsilon,epsilon,1-3epsilon,epsilon),
    h(q)=E(epsilon,3epsilon,epsilon)
        =2epsilon log epsilon+O(epsilon)<0,
    h_env(q)=6epsilon C(1/6,1/6,1/6)>0.                 (7)

Thus the actual full-h volume/unique-maximum theorem cannot be applied
pointwise to replace h_env by h. This is a local comparison obstruction,
not a counterexample to a shared capacity bound.

## 4. Why the geometric construction does not transfer

At an interior fractional stationary row, 0<t<1, variation of alpha
in (3) gives the actual triangle angles alpha at the shared positive
curvatures (x,b,y). Variation of t gives

    Q(x,b,y)=(1/2)log c.                               (8)

The actual normalized input center angles are alpha, however, while the
source balance equations use t alpha. Attaching an ordinary positive
input triangle and a collapsed output triangle with angle load e_c/2
would change the prescribed face loads by

    Delta q=(1-t)(alpha_x e_x+alpha_b e_b
                          +alpha_y e_y-e_c/2).         (9)

For a single fractional port in an original simple sphere this vector
is nonzero: the four labels are distinct and at least one allowed input
corner has positive alpha. Its c component is -(1-t)/2. At ordinary
faces the resulting center-star angles would be 2pi(1+Delta q_f), not
the required multiples of 2pi. Thus even stationarity of the fractional
comparison does not license that tangent-circle development. For several
ports one would need to prove cancellation of the SUM of (9); it is not
among the comparison's face equations. Even such cancellation would not
alone construct the collapsed original contact triples or pairings.

There is a second, independently precise failure of a hypothesis in the
hybrid tight-cut theorem. Its GREEN modification merges two half-supply
triangle rows into a unit-supply four-incidence row and can only INCREASE
each Hall capacity. The fractional comparison instead has an input row
of supply t/2 and a deterministic c row of supply 1-t/2. For a set S,
its local capacity is

    (t/2) 1_{ {x,b,y} touches S }
          +(1-t/2) 1_{ c in S }.                       (10)

For an ordinary singleton S={b}, this is t/2, whereas the original
complete pair contributes 1/2. For an ordinary outer singleton not c,
it is t/2 whereas the complete pair contributes one. Thus the monotone
Hall comparison used to identify all tight sets with actual permitted
digons fails. Artificially imposed zero corners need not come from those
original cuts. The existing relative-interior and marked-piece geometry
theorems consequently do not apply by relabeling this row as GREEN.

Finally the actual signed relative-chain proof counts the original two
cut balls with their prescribed face maps and integer oriented triangles.
Replacing a triangle volume by t times its volume is not a constructed
relative fundamental chain of the original group. The formula t C is
therefore not itself a representation volume. A new construction would
have to supply common ordered contact triples, all original shaded maps,
the original peripheral decorations and an actual relative class. None
of those follows from convex separation or the scalar envelope identity.

These are failures of the proposed direct adapter, not a theorem that
no different representation/capacity argument can control the mixtures.

## 5. Legitimate routes still available

One may choose a different shared positive radius vector for each ACTUAL
fixed LEFT/CROSS/RIGHT sector, since the finite source is first decomposed
into those sectors. A strict weighted certificate for each such sector
does not require its comparison atoms to have a geometric realization.
Likewise an anchored finite certificate bounding one selected one-sided
port and the full envelope at all spectators is legitimate. Cluster is
independently developing and certifying this stronger sufficient route.

For a general theorem without such certificates, the missing input is
one of: a strict bound for the exact fractional problem (3)--(5); a
source-preserving finite comparison that separates the pure atoms before
extraction; or a direct shared bound retaining the actual oscillatory
one-sided coefficients. Existing pure-atom, identity-forest and hybrid
representation results alone do not furnish this input.

## Audit provenance

Independently read the frozen hybrid piece, tight-cut, diagonal identity,
full-kernel entropy and unique-max proofs, the LEFT weighted envelope,
and the newly drafted fixed-triangle capacity lemma. Identities (3)--(5),
(8)--(10) are direct finite-dimensional algebra; (7) uses the already
proved original coefficient/closed-entropy identities. No numerical
experiment or new public theorem is claimed, and no genuine-q normal is
required in this fixed-root discussion.
