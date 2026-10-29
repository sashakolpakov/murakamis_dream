# Faithful parabolic cap certificates on the complete original character support

29 October 2026. The complete three-head source cubic has an elementary
finite representation atlas, including its pair-trace endpoints. Its
source line imposes the LITERAL cap relation on every irreducible point.
At larger plat width a pair trace and a total trace do not suffice.
A finite list of cubic witness traces, inherited from the original
matrix cap relation, is faithful on the irreducible locus. Nilpotent
normal directions are explicitly distinguished from this statement
about the reduced geometric support.

There is also a uniform bounded-representative construction from bounded
pair traces. For a one-component knot it gives an elementary quantitative
separation from the all-parabolic reducible character. These are genuine
geometric support/compactness results. They do not estimate the quantum
Racah transport or the positive word energy.

## 1. Unipotent trace tests

All matrices below lie in SL2(C). Write a trace-two unipotent as
mu=I+N, where tr N=0 and N^2=0. A nonzero N has rank one and
its image equals its kernel, the fixed flag of mu.

For two NONCENTRAL trace-two unipotents,

    Tr(mu nu)=2 iff they have the same fixed flag.             (1)

Indeed N=u phi, M=v psi with phi(u)=psi(v)=0. The extra trace is
phi(v)psi(u). In dimension two either factor vanishes precisely when
the two fixed lines agree. Central matrices are included separately.

Suppose mu_1,mu_2,mu_3 have trace two and

    Tr(mu_2 mu_1)=2, Tr(mu_3 mu_2 mu_1)=2.                   (2)

If their tuple is irreducible, then mu_2 mu_1=I. To prove this,
put P=mu_2 mu_1. If P!=I, (1) implies that mu_1,mu_2 and P share
one fixed flag, also when one input is central. P is a noncentral
trace-two unipotent. The second equation in (2), together with (1),
makes mu_3 share that flag or be central. The tuple is reducible,
a contradiction. This proof has no affine-position or finite shear
assumption on an individual flag.

## 2. The actual three-head cubic, and both original caps

For the original complete heads set mu_i=-H_i, so Tr mu_i=2.
The full source Hom module has D=Tr(H_3H_2H_1)=-2, hence
Tr(mu_3mu_2mu_1)=2. Write

    A=Tr(mu_2mu_1), B=Tr(mu_3mu_2), C=Tr(mu_3mu_1),
    X=A-2, Y=B-2, Z=C-2, S=X+Y+Z.

The [actual character cubic](actual_adjacent_twist_character_and_source.md)
is

    F(X,Y,Z)=S^2+XYZ=0.                                    (3)

Every finite point except the origin has an explicit irreducible
representative. On X!=0 use

    mu_1=[[1,1],[0,1]], mu_2=[[1,0],[X,1]],
    mu_3=[[1+S/X,Y/X],[Z,1-S/X]].                           (4)

Its determinant minus one is -F/X^2, its trace is two, its pair
traces are exactly A,B,C, and the triple trace is exactly two.
The first two flags are distinct. Cyclically permuting the meridians
supplies the other pair-coordinate charts and preserves the triple
trace. The only missing point is
X=Y=Z=0: all pair traces are two, so (1) makes every such tuple
reducible. This proves the finite atlas without assuming a character
variety reconstruction theorem.

The actual initial ordinary-cup source has A=2. On the irreducible
locus (2) therefore gives mu_2mu_1=I. Its reduced source line is
explicitly

    (A,B,C)=(2,2-t,2+t), t!=0,
    mu_1=[[1,1],[0,1]], mu_2=mu_1^(-1),
    mu_3=[[1,0],[t,1]].                                    (5)

At X=0 equation (3) is (Y+Z)^2=0. The square is important:
the reduced line is honest inverse-pair geometry, while its
polarization has a quadratic normal ramification. It is not
permission to remove the actual c_0 Hermite derivative source.

Every actual Hurwitz word preserves the ordered total product
mu_3mu_2mu_1 and irreducibility. Applying (2) at both ends shows:
an irreducible character on the initial A=2 source and final A=2
source has BOTH literal inverse-pair caps. Preservation of the
total product then matches the remaining meridian as a matrix,
not merely by its trace. Following the actual crossing assignments
and these cap identifications therefore gives an honest representation
of that original one-component cup--braid--cap knot. This applies
to the complete source support, not just its geometric branch.

Finite intermediate pair traces A=+/-2 or B=+/-2 do not invalidate
(4)--(5): another nonzero pair coordinate supplies a chart, unless
the entire character is reducible. This statement is about finite
characters, not about ignoring a polar spectral-coordinate Jacobian.

## 3. A faithful witness certificate at arbitrary plat width

For a tuple mu_1,...,mu_b of trace-two unipotents and a selected cap
pair, put P=mu_v mu_u. On the irreducible locus the following finite
trace conditions are EQUIVALENT to the literal matrix relation P=I:

    Tr P=2,
    Tr(mu_k P)=Tr mu_k=2, every k=1,...,b.                  (6)

The reverse implication is immediate. For the forward implication,
if P!=I it is a noncentral unipotent. Every noncentral mu_k shares
its fixed flag by (1), making the whole tuple reducible. This proves
the equivalence at arbitrary fixed width, with no chosen flag chart.

These are genuine source witnesses, not new favorable constraints.
The exact original cup obeys the framed matrix identity
(H_v H_u-I)p=0, as proved in
[the original plat source theorem](actual_plat_cup_cap_gram_support.md).
Left multiplication by ANY specified based quantum meridian and
taking its ordered quantum trace gives another exact annihilator.
Its commutative principal equation is the corresponding witness in
(6). The same applies to the outgoing ordinary cap, with its actual
row order. Under the original Hurwitz transport these equations
give literal incoming and outgoing cap relations on irreducible
reduced support. The full marked co-source is retained separately;
it is not replaced by an invariant cap on arbitrary exteriors.

For the original even plat, use its WHOLE invariant-tensor source
identification first. The input cups impose the full ordered total
meridian product I, which the exact Hurwitz word preserves. At the
output, literal inverse pairs at the ordinary caps then force the
last pair to be inverse by that total MATRIX equation. This is how
the marked pair acquires the faithful classical cap relation in the
assembled source. It is not an annihilator assertion for an arbitrary
unrestricted marked row; its quantum values and normal components
remain in the scalar and its norm estimate.

Pair traces and the total product alone are insufficient. For example,
take six heads with

    mu_1=upper(1), mu_2=upper(-1),
    mu_3=mu_4=lower(1), mu_5=mu_6=lower(-1),
    upper(t)=[[1,t],[0,1]], lower(t)=[[1,0],[t,1]].

All three cap-pair traces are two and their total product is I.
The tuple is irreducible, but the second and third pair products
are lower(2) and lower(-2). A witness with mu_1 detects the failure:
Tr(mu_1 lower(2))=4. Thus the all-width assertion uses the actual
witnesses (or literal framed matrix constraints), not a total trace.

There is also an exact nonreduced qualification. Localize where two
witness meridians are upper(1) and lower(a), a!=0. Write P=I+T,
T=[[u,v],[w,-u]]. Its trace and determinant equations give u^2+vw=0.
The two witness equations give w=0 and av=0, leaving u^2=0.
Thus their REDUCED support is P=I, but a square-zero normal direction
can remain in the trace scheme. The original framed matrix relation
is stronger, and the quantum source jets must remain. No amplitude
bound for such jets is inferred from radical equality.

### Exact interval-Casimir Ward identities already provide a faithful list

There is a particularly direct ORIGINAL quantum certificate which does
not need independent single-head witness operators. Let iota_p insert
the original cup into two adjacent tensor positions a,a+1. It is a Hopf
map from the trivial representation: E_p p=F_p p=0 and K_p p=p.
Coassociativity of the LITERAL coproduct therefore gives, for j>=a+1,

    Omega_[a,j] iota_p=iota_p Omega_[a+2,j],               (6a)

with spectators unchanged. An empty interval is the trivial module,
whose Casimir is q+q^(-1), not an invented constant two at finite N.
For i<=a there is also the left version

    Omega_[i,a+1] iota_p=iota_p Omega_[i,a-1].             (6b)

Both identities hold for EVERY original E,F,K element before taking
the Casimir: on the cup its counit values reduce the coproduct to
the remaining ordered factors. This proves them including endpoints,
all N normalizations, and arbitrary spectator vectors. It is not a
scalar source argument or a commutative approximation.

Their commutative principal trace equations, with the two meridian
minus signs canceled by deleting a pair, are

    Tr P=2,
    Tr(S_j P)=Tr S_j, S_j=mu_j...mu_(a+2), j>=a+2,
    Tr(P T_i)=Tr T_i, T_i=mu_(a-1)...mu_i, i<=a-1.       (6c)

This shorter list is faithful on the irreducible locus. If P!=I,
put P=I+tau E_12 in a common frame, tau!=0. Each deletion equation
says exactly that the corresponding S_j or T_i has lower-left
entry zero. Thus every such partial product preserves the flag.
Taking successive quotients shows that ALL meridians to the right
and to the left preserve it. The two members of the cup pair do so
by (1). This is a reducible tuple, a contradiction. The proof also
covers a pair at either endpoint; for an interior pair BOTH sides
are retained, so no cyclic recut or unavailable prefix is assumed.

The entire exact annihilator list is transported by the actual signed
braid intertwiner, or its actual Hurwitz map on meridians, rather than
being reimposed after a selected channel was dropped. The outgoing
ordinary cap has the dual interval identities. The assembled marked
pair is treated by total-product preservation as stated above.
Equations (6a)--(6c) therefore give an original-source-derived,
all-width faithful REDUCED geometric cap certificate. The nonreduced
qualification preceding this paragraph still applies; none of these
arguments removes the retained quantum Hermite normal data.

## 4. Bounded characters have bounded representatives

For ANY irreducible trace-two parabolic tuple choose a pair maximizing

    M=max_(r,s)|Tr(mu_r mu_s)-2|>0.

After relabeling, a common SL2 conjugation puts that pair in the form
mu_r=upper(1), mu_s=lower(a), |a|=M. Write any other meridian as
I+[[u,v],[w,-u]]. Its pair traces give

    |w|<=M, |v|<=1, |u|^2=|vw|<=M.                         (7)

Consequently every mu_k AND its inverse have operator norm at most
B_M=2+sqrt(M)+M. This gives uniformly bounded representatives on
every bounded pair-character set, even when a previous affine flag
coordinate escaped. If M tends to zero, after a subsequence these
representatives tend to upper unipotents and hence a reducible tuple.

For a ONE-COMPONENT knot there is a stronger quantitative separation.
Following its fixed crossing/cap identifications expresses any two
oriented head meridians as conjugate or inverse-conjugate by a fixed
word of length at most L in the head meridians and their inverses.
The finite L is determined by the original diagram; it follows by
successive substitution of its literal Hurwitz and cap equations.
Enlarge L to at least one. If M<=1, the representatives above have
all generator/inverse norms at most four. For the maximizing pair,
||upper(1)-I||=1 and ||lower(a)-I||=M. Their fixed conjugacy relation
therefore gives

    1<=4^(2L) M, hence M>=4^(-2L).                         (8)

If M>1 the same lower bound is automatic. Thus irreducible
boundary-parabolic representations of this fixed knot are separated
from the all-pair-traces-two character. On a set M<=M_0, every
individual meridian also satisfies

    ||mu_k-I||>=B_(M_0)^(-2L).                              (9)

This follows by comparing it to the normalized upper(1) generator.
The conclusion does not assume that distinct meridians have distinct
fixed flags: honest cap partners have the same flag. It rules out
central-meridian degeneration within this bounded irreducible family.

## 5. Geometric consequence and precise remaining scope

Initial and final faithful cap certificates, sewn by the actual
Hurwitz graph, give the original Wirtinger/cap representation space
on irreducible reduced support at every fixed plat width. The above
finite atlas and bounds treat finite pair-character degenerations;
an escaping unbounded-character family is a separate boundary problem.
Every resulting honest boundary-parabolic representation satisfies
[the independently proved representation-volume bound](general_peripheral_representation_volume_bound.md).

Accordingly a FULL canonically calibrated critical action on this
closed character support is bounded by knot volume. The present
proof identifies the source geometry; it does NOT establish that
every constrained face critical of a scalar kernel follows that full
canonical graph, nor bound its exit currents. It does not identify
an arbitrary balanced Racah action with the regulator without its
normalizer and branch constants. Most importantly, it does not prove
the remaining positive word-energy estimate or geometric noncancellation.

[Audit](../experiments/audit_actual_parabolic_cap_trace_certificate.py):
exact symbolic cubic reconstruction, source-line caps, all-width
counterexample/witnesses, nonreduced normal qualification, and bounded
representatives for explicit irreducible unipotent tuples.

Fresh replay: PASS 37 literal all-position quantum cup AND ordinary-cap
E/F/K/Casimir interval deletions, including empty intervals and levels
of both parities; exact symbolic cubic/source/prefix-witness/normal
identities; the six-head insufficiency example; and four bounded
irreducible reconstruction families. Compilation passes.
