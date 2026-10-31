# Positive outer completion and an exact shared dual-work identity

31 October 2026. **Research reduction; the universal comparison is open.** The identities and sufficient
criteria below retain every original face target and protected zero. They
do not assert that the completed triangle array is globally feasible, or
that the criteria hold for every certified diagram.

## 1. Local completion, slack, and equality

Write an original LEFT degree vector as

    q=(xi,mu,1-nu,eta), w=nu-mu=xi+eta,
    0<=mu<=nu<=1/2.

Use the actual coefficient endpoint triangles

    alpha=(a,mu,c), beta=(b,nu,d),
    a-b=xi>=0, c-d=eta>=0, a+c=1/2-mu, b+d=1/2-nu.

Thus h=C(alpha)-C(beta) and g=C(xi,1/2-w,eta). Set delta=1/2-nu.
The letter d in beta is a corner load, not the finite degree N-1.
The original f is symmetric about1/4, f(1/2-t)=f(t), strictly concave
on(0,1/2), and f(0)=f(1/2)=0. For 0<=b<=a<=1/2,

    f(a-b)=f(1/2-a+b)<=f(1/2-a)+f(b)=f(a)+f(b).

Apply this also to c,d and to the middle difference nu-mu. It gives

    C(gamma)<=C(alpha)+C(beta), gamma=(xi,1/2-w,eta),
    tilde h=(h+g)/2=C(alpha)-tau<=C(alpha),               (1)

with the EXACT nonnegative slack

    tau=1/2[D_f(1/2-a,b)+D_f(delta,mu)+D_f(1/2-c,d)].     (2)

This is not the original three-D formula: it records its complementary
triangle-inequality deficit. For D_f(u,v), strict concavity implies
D_f(u,v)=0 iff u=0 or v=0. At a nonterminal port delta>0, equality tau=0
therefore forces mu=0 and alpha to be a pure OUTER vertex. Indeed if
both a,c are positive, both are<1/2 and (2) forces b=d=0, contradicting
b+d=delta>0. Conversely that pure-outer configuration has tau=0. Terminal
nu=1/2 has beta=(0,1/2,0) and tau=0 for every alpha.

In particular tau>0 at every nonterminal row with positive mu, or with
both input outer corners positive. The zero-slack nonterminal cases are
zero joint-entropy monomial degeneracies, not positive-area regular rows.

Complete the local port by retaining alpha on its original input triangle
(x,parent,y) and putting the original output triangle at its pure child
vertex, with child load1/2. These are two genuine nonnegative half-supply
triangle allocations. Their quartet load differs from q by exactly

    Delta_e=b e_x+d e_y-delta e_child.                    (3)

The parent load mu does not change. This sends the overloaded child's
excess to its two original OUTER faces. It does not transfer it to the
parent or change the mark.

Protected corners are still zero. At a protected outer face, the actual
closed coefficient tilt has the corresponding alpha and beta corners
zero. On a diagonal mu=nu the tilt is not determined by the coefficient;
choose a limiting tilt that preserves any protected outer zero. The
original certificate never has both matching outer faces protected.
A protected parent has mu=0. The overloaded child is necessarily ordinary.
RIGHT is the literal reflected construction.

## 2. Global identity with actual shared dual weights

Let q be ANY original feasible flow with a chosen closed CROSS/LEFT/RIGHT
assignment. At CROSS ports choose an entropy-maximizing split into the
two original triangles. At one-sided ports use the completion in section1.
Call the resulting triangle array A. Every row has supply1/2 and every
protected corner is zero. Its ordinary face totals are

    1+Delta_f, Delta=sum_(one-sided e)Delta_e.             (4)

It need not satisfy the desired target1. Nevertheless

    sum_triangles C(A_t)=sum_ports tilde h(q_e)+sum_e tau_e. (5)

For ANY finite positive ordinary radii L, marks exactly0, set

    F_D(L)=sum_t Q(L_t)-sum_(ordinary f)log L_f,
    B(A;L)=sum_t[Q(L_t)-C(A_t)-sum_(ordinary corners f)A_tf log L_f].

Every term of B is nonnegative by the exact triangle Legendre formula.
Using (4)--(5) gives the exact identity

    F_D(L)-sum_e tilde h(q_e)
       =B(A;L)+sum_e tau_e+sum_f Delta_f log L_f.         (6)

At the actual complete radii L*, F_D(L*)=Phi_D. Thus the universal joint
comparison is precisely a compensation problem between the nonnegative
B and tau terms and the possibly negative OUTER transfer work

    sum_f Delta_f log L_f
      =sum_e[b_e log(L_x/L_child)+d_e log(L_y/L_child)].   (7)

Protected outer terms vanish rather than introducing log0. No face flow
has been discarded or reassigned without the explicit defect(3).

## 3. A finite shared linear-program sufficient criterion

This consequence needs no minimax exchange. Fix L as above and a genuine
closed sector s, with nonempty one-sided port set J. For each e in J define

    zeta_e(L)=Q(L_x,L_child,L_y)-(1/2)log L_child>0,
    omega_e(L)=max(0, max_(ordinary outer f)log(L_child/L_f)).

Strict positivity of zeta follows because the matching outer pair cannot
be the two protected MAIN faces. The completed output row is pure-child,
so its EXACT term in B is zeta_e. From beta_x+beta_y=delta_e,

    Delta dot log L >= -sum_e omega_e delta_e.

Let P_s be the original shared-flow polytope: each port has total1,
ordinary face targets1 and protected0; CROSS middles<=1/2; the selected
one-sided child>=1/2. All these constraints are linear. Define

    kappa_s(L)=sum_(e in J)zeta_e(L)
      -max_(q in P_s) sum_(e in J)omega_e(L)(q_child-1/2). (8)

This is an ordinary finite transportation LP with its original labels.
For an empty P_s the sector is absent. Equations(6)--(8) prove

    max_(q in P_s)sum_e tilde h(q_e)<=F_D(L)-kappa_s(L).   (9)

Hence the condition

    kappa_s(L_s)>F_D(L_s)-Phi_D                           (10)

for each nonempty noncross sector, allowing a different verified shared
radius vector L_s for each ACTUAL sector, proves the global joint gap and
therefore the full long-filling volume conclusion under the already proved
source transfer theorem. All twists remain independently signed, fixed and
sufficiently long. A finite radius/LP certificate is enough; attainment of
a shared-radius minimizer is not assumed. Since there are finitely many
sectors, strict inequalities give a common positive margin.

At L* the right side of(10) is zero. With arbitrary rational positive
radii one may use a rigorous upper bound for F_D(L_s) and an independent
lower bound for Phi_D, together with feasible LP dual certificates. No
optimizer output is itself a certificate. This criterion applies at any
fixed bridge width and is a theorem about the original incidence graph.
No strict enlargement of prior balanced or anchored classes is asserted
without an actual certified example; (8) deliberately discards useful B
and tau terms and can fail while the joint criterion remains true.

## 4. An explicit additional nonlinear slack

The exact derivative f''(t)=-2pi/sin(2pi t)<=-2pi gives
D_f(u,v)>=2pi uv, by integrating -f'' over the rectangle[0,u]x[0,v].
Thus(2) yields

    tau>=pi[(1/2-a)b+mu delta+(1/2-c)d]
         >=pi delta[2mu+min(xi,eta)].                    (11)

For the second inequality substitute a=xi+b,c=eta+d,b+d=delta.
The convex expression xi b+eta d+b^2+d^2 has maximum
max(xi,eta)delta+delta^2 on that segment, so the first two outer terms
are at least delta(mu+min(xi,eta)). The source identities guarantee the
endpoint choices satisfy the corner bounds. The displayed lower bound may vanish in the monomial directions; it is
strictly positive when delta>0 and 2mu+min(xi,eta)>0. Keeping it in(8) gives a stronger explicit polynomial
optimization criterion on the SAME feasible flow; no concavity of that
optimization is assumed.

The unresolved general issue is proving adequate compensation in(6) for
all feasible original flows, potentially using the outer-transfer graph
and the positive Fourier kernel of f. Neither the middle-only cocycle nor
a lossless cover of the original projection supplies that compensation.

No new diagram coverage is asserted without a certificate verifying the stated sufficient criterion.

The local score is the one in the [joint source criterion](general_endpoint_conditioned_source_energy.md);
its exact three-gap form is recorded in the [triangle decomposition](research_joint_entropy_triangle_decomposition.md).
The [middle-interval leakage lemma](research_joint_middle_interval_leakage.md)
explains why middle-only reassociation is insufficient.
