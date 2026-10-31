# Independent audit of the corrected literal pretzel cap order

29 October 2026. The physical box order is left to right, while the
turned operators compose right to left. The corrected port theorem
uses the latter traversal and satisfies EVERY original bottom and top
cap. This audit checks the full physical tensor identity with arbitrary
NONCOMMUTING degree-preserving boxes, so commutativity of Casimir
polynomials cannot conceal an ordering error.

## 1. What the actual cups and caps force

Use original box b input (a_b,b_b) and output (c_b,d_b), with physical
boxes labeled left to right. The actual source pairs

    bottom: b_b with a_(b+1), outer a_1 with b_s;
    top: d_b with c_(b+1), outer c_1 with d_s.

The marked outer row is unrestricted before the full contraction.
Integer-degree conservation forces its total degree d only after all
boxes and ordinary turns are assembled. It is kept literally in the
finite checks below.

For a physical box parameter t_b and t'_b=U_b t_b, the corrected
unturned meridians are

    bottom (h(t'_b),h(t_b)^(-1)),
    top (g(t'_b)^(-1),g(t_b)).

Consequently both inner caps, and the two outer caps at closure,
require EXACTLY

    t_b=t'_(b+1), equivalently t_(b-1)=U_b t_b.          (1)

This is the propagation order s,s-1,...,1. The previous forward
assignment t_(b+1)=U_b t_b does NOT satisfy the physical caps in
general; the fact that product U_b=1 would close that unrelated
cycle does not repair its individual cap failures.

## 2. An exact index identity detects the operator order

For the actual unscaled turn write

    (Rot B)_((u,b);(v,e))=x^(u-e)B_((d-u,v);(b,d-e)).

In the product Rot(B_1)...Rot(B_s), input to factor i is output
from factor i+1. Write its intermediate indices (u_i,b_i), cyclically.
The corresponding physical input/output of B_i are

    (a_i,b_i^phys)=(b_i,d-b_(i+1)),
    (c_i,d_i^phys)=(d-u_i,u_(i+1)).                    (2)

These are precisely the two original cap matchings above. The pivot
on the second traced head is g_b=x^(2b-d); thus

    (1/N)Tr[(I tensor g)Rot(B_1)...Rot(B_s)]

has the original turn factor

    (1/N)x^[(s-1)d+2a_1-sum a_i-sum c_i].

This is the direct cup/cap/marked factor, with no extra average or
component sign. The identity holds for ANY physical integer-degree
preserving boxes, even when their turns do not commute. In particular
one cannot freely reverse the factors by an unmentioned Casimir
specialization. Each factor still acts rightmost first, proving (1).

## 3. Reverse traversal does not reverse geometric orientation

For the complete geometric anchor label its cyclic traversal by
i=1,...,s corresponding to physical b=s,s-1,...,1. Then
z_(i+1)=U_b z_i and the geometric face labels must follow THIS same
traversal. This is not a permutation of physical source boxes.

There is also an explicit oriented-diagram check: the planar half
turn (X,Y,Z)->(-X,-Y,Z) sends b to s+1-b and its port labels to

    a_b -> d_(s+1-b), b_b -> c_(s+1-b),
    c_b -> b_(s+1-b), d_b -> a_(s+1-b).

It exchanges the two displayed cap matchings and their corresponding
outer arcs. Its ambient determinant is +1 and its planar determinant
is +1. It preserves the over/under coordinate Z, hence each oriented
crossing sign. It is a rigid rotation, not complex conjugation or a
mirror. The actual turn also obeys Rot^2 B=B with all its x factors;
this can be checked directly in the displayed index formula. Thus no
curl or quantum half-twist change is introduced.

Transport each oriented crossing disk AND its oriented auxiliary
circle in this rotation. The primitive meridian and disk longitude
are carried together, with their intersection number and zero
self-linking preserved. The actual retained R^(-1) remains R^(-1).
The geometric generators are relabeled by
the reverse physical traversal; their developed maps and their
positive regulator are not conjugated. This geometric relabeling
does not replace the original marked row by another local source.
The finite tensor checks leave that row in its original slot.

## 4. An explicit holomorphic isometry fixes the orientation qualification

The geometric reverse traversal can also be checked directly in the
complete developing coordinates, without inferring it from a diagram.
Use the port theorem's rho,alpha and indexed vertices. The Mobius map

    F(zeta)=rho^2/zeta

is HOLomorphic and hence an orientation-preserving H3 isometry. It
sends

    Z_i -> Z_(-i),
    U_i^+ -> U_(-i-1)^-, U_i^- -> U_(-i-1)^+.

Thus it reverses the cyclic traversal while exchanging top and bottom,
as required by the literal cap map above. Directly on the complete
source generators it has

    F g_i F^(-1)=h_(1-i)^(-1),
    F h_i F^(-1)=g_(1-i)^(-1),
    F P_i F^(-1)=P_(-i)^(-1),
    F C_i F^(-1)=C_(-i)^(-1).                           (3)

The first two follow from the displayed g,h matrices and
z_i z_(1-i)=r^2/rho^2. The third uses P_i=g_i g_(i+1)^(-1)
and h_i g_i=A. For the fourth use
C_i=I-(P_i+I)/(1+Y), P_i^(-1)+I=-(P_i+I), and (P_i+I)^2=0.
The same indexed matrices generate the geometric holonomy group,
so (3) proves that F normalizes it. It is therefore the actual
orientation-preserving hyperbolic isometry implementing this relabeling,
not a complex conjugate of the geometric representation.

There is an IMPORTANT marking qualification: the two peripheral
generators are jointly inverted, (mu_i,lambda_i)->
(mu_(-i)^(-1),lambda_(-i)^(-1)). Their intersection number and
positive cusp ratio are unchanged. In particular this preserves the
positive diagonal mu_+ marking up to JOINT orientation reversal;
it does not change mu_+ to mu_-=mu_+-lambda. The filled slope
mu+p lambda changes only its overall orientation. In the quantum
packet this is exactly the Weyl pair m_i<->-m_i, whose two
contributions were retained and proved equal. There is no hidden
framing shear or volume-orientation reversal.

Accordingly the corrected
[global port/anchor theorem](actual_pretzel_port_lift_and_geometric_anchor.md)
has no remaining cap-order or orientation objection from this audit.
Its full face-isometry calculation is still the source of the actual
geometric anchor; cyclic closure alone would not establish it.

[Fresh audit](../experiments/audit_actual_pretzel_literal_cap_order.py)
checks literal generic noncommuting physical tensors, the original
full marked row and pivot, distinguishes the reversed matrix product,
checks every inverse-pair cap with nonconstant U_b, and checks the
rigid half-turn port/crossing convention. It also checks the full
holomorphic generator/peripheral identities (3) at complete widths
through s=25.

## 5. Completion audit of the stated sharp-upper assembly

The final
[long-pretzel sharp upper theorem](actual_long_pretzel_sharp_volume_upper_bound.md)
passes this independent assembly audit after the corrected cap order
and the explicit holomorphic marking qualification above:

- Its whole-source limit is the original marked Kraw, not a selected
  color term. The actual reduced Kashaev normalization has the same
  modulus; the optional one-cut modified factor is applied only once.
- Every stationary local matrix is glued by the actual physical caps
  in (1). The nearby commuting peripherals are regular semisimple, so
  the scalar filled-slope eigenvalues really give +/-I matrices and
  a representation of the FILLED group in PSL2.
- The preferred SL sign lambda=-L_H^(-1), its centered character, the
  actual filling quadratic and the source factor 2pi are retained.
  The paired regulator therefore has the same absolute constant as
  the complete positive geometric anchor.
- The old ideal boundary is first compared with an axis cusp using
  the explicit O(Y^(-2)) homotopy. Only then are compatible old/new
  finite solid-torus vertices placed on that axis. Thus the filled
  representation regulator has no lost boundary constant.
- The representation-volume estimate uses only the descended PSL2
  action. No faithfulness or unproved SL2 descent is required.

The theorem's stated scope is essential and correct: fixed odd s>=25,
independently sufficiently large FIXED signed slopes, and a HYPERBOLIC
filled complement. Equality with its hyperbolic volume is not claimed.
This audit does not turn that broad-class upper bound into a theorem
for every hyperbolic knot or a proof of the full volume conjecture.
