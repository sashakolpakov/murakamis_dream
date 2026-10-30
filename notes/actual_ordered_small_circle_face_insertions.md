# Ordered small-circle insertions and the original marked face

30 October 2026. Independently reviewed and frozen. This note extends
the exact polynomial insertion to several untwisted ports in a specified
literal Morse class. The operators act in reverse source order, including
on all coefficients created by later ports. It also supplies a one-port
adapter when the outgoing middle face is the original marked or exterior
face. No mark is moved and no generic-q transpose identity is inferred.

The general subset with several protected outgoing faces or disconnected
smoothing remains outside the statement below.

## 1. Literal face births, not an arbitrary operator order

Use the flat 2k-plat sweep and actual region labels of the
[marked face coefficient theorem](actual_original_marked_face_coefficient.md).
Number boxes in their original bottom-to-top order. At box i write
(x_i,b_i,c_i,y_i) for the outside, input-middle, output-middle and final
faces. Only its middle gap changes. The output region is created at
this box and remains in that gap until its next box or the top cap.

Only the top exterior gap identifications can identify such a new
region with a region already present earlier: those identifications
all give the exterior face u. Every bounded output face c_i is
therefore a distinct face with a unique birth i. In particular c_i
does not occur as ANY face of a box j<i. This includes outer faces,
not only the two middle positions. A bounded middle face is distinct
from the two outer faces at its incident box; the outer faces may
coincide with one another.

The other protected face v is the bounded face of the original
marked cap. Choose a set S of ports such that

    epsilon_i=0 and c_i not in {u,v}, for every i in S. (1)

The input b_i may equal u. All other physical turns, the mark and the
retained half twists outside S are unchanged. No one-main-component
assumption is made.

The relations c_i=b_i, i in S, form a forest directed from an older
face to a newer one. Each c_i has one birth and at most one such incoming
edge. A directed cycle would contradict the strict birth order, and
an undirected cycle would have a newest vertex with two incoming
edges. Neither protected face is eliminated. In the flat plat one can
also see this forest as consecutive deleted segments in the original
gaps. Each even gap retains its last box, whose outgoing face is u;
connectedness of the original plat requires a box in each internal
even gap. Thus the identity-smoothed projection remains connected.
The marked gap retains its last box if it has one, so the two original
marked faces remain distinct.

For clarity, this is a source-coordinate class with a proved order.
It is not a claim that an arbitrary untyped graph or a differently
routed collection of coupons has this triangular incidence.

## 2. The exact reverse-ordered polynomial

Retain N,d,q,Q and the operators T_h(x,c,y) of the
[one-port theorem](actual_small_circle_polynomial_face_insertion.md).
They preserve polynomials and total degree; their coefficients retain
the full source phase q^(pd), where p is output-minus-input first head.
Each h_i is an actual integer in 1,...,N.

Let P_rem be the product D_a D_a Ptilde_s over all ports outside S,
in ALL original face variables before any identifications. Starting
with this polynomial, process i in S in STRICTLY DECREASING original
Morse order. At step i apply T_(h_i)(x_i,c_i,y_i) to the CURRENT
polynomial, then substitute c_i=b_i everywhere. Apply the same region
identification to the remaining notation. Call the result Q_S.

This instruction acts on every factor created at preceding steps.
For example an earlier output c_i may occur as an outer variable in
a later port's operator. Its q-shifts must then act on that operator's
coefficients as well. Commuting the operators or applying them only
to the initial product is not the stated formula.

Why this order is exact can be checked before any coefficient extraction.
Keep the original finite physical paths at every small port. For the
latest pending port i, its bounded output c_i occurs in no earlier
pending port, by section 1. Thus summing its paths and eliminating
c_i=Q^(-p_i)b_i acts ONLY on the current remaining source polynomial;
the other pending port weights are independent of c_i. The true factor
q^(p_i d) is unchanged because the eliminated face c_i has the ordinary
exponent -d, whereas b_i is retained. The local path calculation is
therefore exactly T_(h_i), followed by the merge. Repeating proves the
algorithm. If later eliminated faces were merged into c_i, all their
factors already occur in the current polynomial and are shifted along
with it. This is precisely the cross-shift contribution required by
the original paths.

Let r=R-|S|, and let F_sm be the r faces other than u,v in the
identity-smoothed diagram. Then Q_S is homogeneous of degree dr and
the actual fixed-sector source is

    A_(N,a;h_S)=N^r product_(i not in S)
        [k_(a_i)beta_(a_i)^2 omega_(a_i)^epsilon_i]
        [product_(f in F_sm)L_f^d] Q_S(L)|_(L_u=L_v=0). (2)

All physical endpoint factors remain those of the original Casimir.
Each elimination reduces the primitive grid by exactly one variable;
there are N^(r+1) final grid points and the unchanged single N^-1
marked factor. All exponents in Q_S are nonnegative integers, so its
degree dr excludes every whole-N alias exactly as in the one-port
proof. Neither positivity of Q_S nor independent periodicity of a
local half-integer source factor is needed.

## 3. Uniform cost at an actual compatible smoothing radius

Choose fixed positive values l on the final smoothed faces, including
both marked faces. Give each old face the value of its merged class.
For each i put

    C_i(l)=3+4(l_(x_i)+l_(y_i))/l_(c_i)
                  +4l_(x_i)l_(y_i)/l_(c_i)^2.       (3)

These use the literal old incidences followed by the final region map.
The weighted polynomial norm in the one-port theorem applies at every
step; merging variables of equal weight cannot increase it. Therefore

    |[L^(d F_sm)]Q_S|
      <= product_(i in S) C_i(l)^(h_i-1)
          P_sm(l)/product_(f in F_sm) l_f^d,         (4)

where P_sm is the original positive polynomial obtained by identity
smoothing all ports in S. This includes all dependence of later
operator coefficients on earlier shifted faces. The original scalar
factors in (2) are retained outside (4).

A proved strict coefficient-rate gap at the SAME positive smoothed
variables thus survives with only O(sum_i h_i) added logarithmic cost.
This is subexponential for a fixed number of ports with h_i=O(sqrt N),
and preserves a fixed strict gap for sufficiently small h_i<=delta N.
An optimized or fixed-radius gap is a separate geometric/capacity input;
none is asserted for every smoothing by this algebra.

## 4. A one-port adapter at the original mark or exterior

There is a useful boundary extension that does not require moving the
mark. The original root Casimir is TRANSPOSE-SYMMETRIC in the balanced
physical basis. Indeed its true coefficients satisfy

    A_+(U,V)=A_-(Q U,Q^-1 V),                        (5)

including the endpoint zeros, and its diagonal is unchanged. Hence
L_h^T=L_h at the root. This is ordinary transpose, not Hermitian
conjugation and not a statement about its genuine generic-q jet.

For ONE port suppose its middle faces b,c are distinct, at least one
is unmarked, and the identity smoothing is connected with u,v still
distinct. Eliminate an unmarked middle face. If it is c, use the
original T_h in c. If instead c is protected and b is unmarked,
use (5), regard the outgoing pair as input for this local calculation,
apply the SAME T_h(x,b,y) to P_rem, and then set b=c. The displacement
is now S-R and the exact source phase is q^((S-R)d), because the
eliminated variable b has exponent -d. All other variables and the
actual original mark are retained. Formula (2) with |S|=1 and bound
(4) follow without changing the marked functional.

If the incoming b is protected and outgoing c unmarked, no transpose
is required: the q^(pd) computation only uses that the ELIMINATED
face c is unmarked. Its merged target is then zero rather than d,
as required by the same original mark. The degree/alias argument
again applies with the two protected faces retained.

In a flat plat a middle gap has fixed parity. The exterior belongs
to even gaps and the marked-cap face belongs to an odd gap, so they
cannot be the two distinct middle faces of one box. A nondegenerate
certified port has distinct middle faces. Thus every such single
untwisted port whose smoothing stays connected admits this adapter,
irrespective of which actual top cap was marked.

This one-port transpose does NOT justify arbitrary compositions of
forward and reverse eliminations. A reversed elimination can act on
earlier pending port weights, unlike the ordered class in section 1.
Several protected outgoing ports, disconnected smoothings, and retained
R^epsilon at the small ports remain separate source problems.

## 5. Original-source verification and reviews

The [focused audit](../experiments/audit_actual_ordered_small_circle_face_insertions.py),
with [saved results](../experiments/actual_ordered_small_circle_face_insertions_results.json),
checks 81 original Morse charts, 1,143 bounded output births, 9,056
earlier-face exclusions, 243 deleted forests and connected literal
smoothings, and 1,836 genuine cross-coefficient incidences. It compares
27 whole original multiport contractions and 122 original one-port
mark/exterior adapters with the stated coefficients, retaining the
other half twists, actual cups and unrestricted mark. The root transpose
check uses 4,659 original coproduct entries. All 86 surviving modular
targets are the asserted unique coefficients. An explicit original
source gives a different answer when the reverse order is replaced
by forward order. Coincident outer labels are also tested literally.

Two independent full analytical reviews checked the source births,
ordered summation including coefficient shifts, scalar/primitive-grid
normalization, weighted norm and protected-face transpose adapter.
The second reviewer freshly replayed the full audit with redirected
output and reproduced every count. A third targeted source-geometric
review independently checked the literal sweep, older-face forest,
last-even-gap connectedness and retained marked-gap assertions in
sections 1--2. None of these reviews extends the theorem to arbitrary
mixed-direction subsets, disconnected smoothings or signed small ports.
The note, audit and saved results are frozen.
