# The nilpotent Mobius action is not the actual framing Ward action

28 October 2026. A common fractional-linear change of the charged
nilpotent anchors is an exact algebra automorphism. Its effect on the
original source is computable. However, it does not provide a second
geometric framing integral: invariance of a homogeneous top-degree state
is automatic, while the ordinary common action fails covariance with an
original crossing. Its source-preserving weighted lift also has the wrong
nilpotent Jordan type to be the actual Hopf current on a head.

This rules out that specific identification. It does not rule out a
coupled quantum dressing which transforms clocks, crossings and source
currents together, or the independent positive selection theorem for a
network already satisfying its stated hypotheses.

## 1. Exact automorphism and source Jacobian

Put d=N-1 and A_N=K[X]/(X^N), in characteristic zero. The source is
the original functional lambda(P)=[X^d]P. For a!=0 define

    phi_(a,c)(X)=aX/(1+cX) mod X^N.                    (1)

The inverse is X/(a-cX), so this is an algebra automorphism. Its
SOURCE formula, valid for EVERY polynomial exterior, is

    lambda(P(phi_(a,c)(X)))
          =lambda(P(X) J_(a,c)(X)),
    J_(a,c)(X)=a(a-cX)^(N-2).                        (2)

Proof. In the specified residue lambda=Res P(X)dX/X^N, make the
formal invertible change Y=aX/(1+cX). Then X=Y/(a-cY) and

    dX/X^N=a(a-cY)^(N-2)dY/Y^N.

This proves (2) with its exact scalar and exponent. For k anchors the
source factor is the product of the k displayed J factors. At a=1,
its infinitesimal identity is

    lambda(-X^2 partial_X P)=-(N-2)lambda(XP).         (3)

Thus ordinary Mobius substitution does NOT preserve the original source
on arbitrary exteriors. The coefficient norm of its source multiplier
at a=1 is exactly

    ||(1-cX)^(N-2)||_1=(1+|c|)^(N-2).                (4)

At fixed nonzero c this is exponential in N. This is a norm statement
about the full normal source, not a claim that the original scalar
acquires that factor.

## 2. Why homogeneous-source invariance is automatic

For k original charged anchors let Omega=product_i X_i^d. The top
homogeneous piece of A_N^(tensor k) has degree kd and is the ONE line
K Omega. Every actual whole-source P_h is homogeneous of that degree
before projection, including after the proved closure contractions.

Under common (1), each variable starts with aX_i and all remaining
terms have strictly higher degree. Since no degree above kd survives,

    phi_(a,c)(P_h)=a^(kd) P_h in A_N^(tensor k).       (5)

In particular c-invariance at a=1 holds for EVERY top-degree state,
whether its selected coefficient is nonzero or zero. The induced
c-action on this socle line is trivial. It therefore contains no
information identifying a geometric relative period or selecting a
nonzero second framing fiber. This is the same original homogeneous
socle, not a substituted favorable source.

It remains possible to retain lower-degree normal classes and the full
Jacobian (2). Their covariance must actually be proved; (5) cannot
replace it.

## 3. The exact source-preserving lift has the wrong Ward generator

There is a specified weighted action preserving lambda on ALL states:

    U_(a,c)P(X)=a^(-d)(1+cX)^(N-2)P(phi_(a,c)(X)).    (6)

Indeed (2), or direct substitution in it, gives lambda(U P)=lambda(P).
At a=1 its infinitesimal generator is

    L=(N-2)X-X^2 partial_X,
    L X^j=(N-2-j)X^(j+1).                           (7)

For N>=3 its Jordan blocks are N-1 and 1: it acts in one full chain
on 1,X,...,X^(N-2), and kills the separate socle X^d. At N=2 it is
zero. The UNWEIGHTED substitution generator -X^2 partial_X likewise
has blocks N-1 and 1, with the separate constant line instead.

The original complete quantum E and F on one physical head have a
single Jordan block of size N. For F its consecutive coefficients in
the actual balanced basis are 1-Q^(j+1), 0<=j<=N-2, all nonzero.
The corresponding E coefficients are also nonzero along their whole
chain. Consequently no invertible head gauge conjugates (7), or its
unweighted version, to the actual E or F. Nilpotent Jordan type is
unchanged by any such gauge.

One can instead use the ordinary coherent weight (1+cX)^d, obtaining
the regular classical generator dX-X^2 partial_X. But then the source
is NOT fixed; exactly

    lambda((1+cX)^d P(X/(1+cX)))
           =lambda(P(X)/(1-cX)).                    (8)

Moreover the primitive two-head coherent generator has nilpotency
index 2N-1, whereas the actual root Hopf coproduct has its N-th power
zero. Thus even this alternative is not a factorwise identification
with the actual quantum tensor action. Its source and tensor adapter
would have to be constructed and retained separately.

## 4. A literal original crossing fails common Mobius covariance

This is also visible without a representation classification. Let B
be the original positive checked crossing in the actual balanced
factorial basis and retain its common Cartan scalar kappa. Complete
color means x=-q^(-1), Q=q^2, hence x^(-2)=Q. Its k=0 entries give

    [|0,1>] B |1,0>=kappa x^(-1),
    [|0,2>] B |2,0>=kappa x^(-2).                   (9)

For N>=3 put D=-X^2 partial_X and D_tot=D_1+D_2. Then

    [|0,2>] [B,D_tot] |1,0>
                       =kappa(x^(-1)-x^(-2)) !=0.   (10)

To see the two terms, D_tot|1,0>=-|2,0>; after B only its k=0
term can yield |0,2>. Conversely B|1,0> has |0,1> coefficient in
(9), and D_tot sends it to -|0,2>. This proves (10), with no lost
factorial, source normalization or Cartan scalar. At the actual
half-root x^(-1)=-q and x^(-2)=q^2, so the difference is -q(1+q),
nonzero for every N>=3.

Therefore the common ordinary Mobius action cannot be slid through
the unchanged actual crossing. Full E/F Ward identities do not supply
that missing covariance, since they concern the different Hopf action
in Section 3. At N=2 the unweighted Mobius substitution is already
the identity on K[X]/X^2 and supplies no framing direction at all.

## 5. Consequence for the proposed second framing fiber

The [nilpotent source](actual_charged_socle_and_fermat_source.md) and
[closure contractions](actual_general_flow_fusion.md) are exact. The
ordinary common Mobius changes do not add a selected nonzero fiber to
them. On the original top-degree state they act trivially by (5).
On general exteriors they require the source multiplier (2), and on
the fixed actual network they have the explicit covariance defect (10).

This leaves a precise constructive possibility: a COUPLED quantum
framing transformation, including the underclock feedback, Hopf tensor
factors and boundary co-source, might have a controlled nonzero relative
fiber. It cannot be identified with the common automorphism (1) merely
from nilpotent-source invariance. The existing warning about ordinary
coherent Mobius action versus actual quantum dressing in
[the Springer boundary note](springer_centralizer_boundary_source.md)
is consistent with, and now has the explicit selected-source and
crossing calculations (2)-(10).

No broad knot-volume lower bound or nonzero global geometric coefficient
is proved by this test.

[Audit](../experiments/audit_actual_nilpotent_mobius_source.py): exact
source Jacobians and inverse maps, both weighted source actions, their
Jordan indices, original quantum E/F chains and the full original
crossing witness (10), with kappa retained.
