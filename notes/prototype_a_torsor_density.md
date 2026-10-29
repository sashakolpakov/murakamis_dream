# The same geometric residue in the two prototype A-periods

Research note, 27 October 2026. The user suggested using 4_1 and
5_2 to guide a general proof. Here the two cases give the same
exact determinant-line identity, with a simple Riley residue.
The calculation uses the original coefficient model and the
intrinsic linearized holonomy complex. It does not prove the
selected finite period's volume asymptotic.

## 1. A precise statement in both complete trace fields

Use the three-strand words, in the fixed Hurwitz action order,

    beta_4=[1,-2,1,-2],
    beta_5=[1,1,1,2,-1,2].

The first is the figure-eight braid. An independent local
SnapPy recognition of the second gives 5_2. The symbolic
fixed-point calculation below does not use that recognition
as a representation-theoretic input.

Let

    A=[1 1;0 1], B=[1 0;t 1].

For 4_1 take C=A^(-1)B A B^(-1)A; for 5_2 put

    D=A^(-1)B A, E=D^(-1)A D, C=E A E^(-1).

The respective nonabelian parabolic fixed-point equations are

    f_4(t)=t^2-t+1=0,
    f_5(t)=t^3+t^2+2t+1=0.                       (1.1)

These follow by substituting the matrices in the Hurwitz
word and factoring the entries of F_beta(A,B,C)-(A,B,C).
Thus the comparison uses their exact complete trace fields,
not a floating-point hyperbolic representation.

Conjugate by the full framing matrix

    F(r,s)=[r 1-r;s -s], s!=0.

Let Omega_beta denote the original variable principal normal
Gaussian density, retaining both framing derivatives and all
crossing, pivot and writhe variable factors. Its fixed
base-only quantum normalization line remains separately
marked, as in the
[normal-period construction](actual_geometric_normal_period.md).
Let T_beta be the torsion of the acyclic holonomy complex
proved invariant under presentation moves in
[the uniform Markov theorem](pointed_markov_reduction.md).

**Prototype proposition.** In the respective exact function
fields Q[t]/(f_i)(s,r), one has

    Omega_beta^2=-(T_beta/2) Omega_cut^2,
    Omega_cut=-dr wedge ds/[s(1+s)].             (1.2)

More explicitly,

    4_1: -T_beta/2=(2t-1)/3,
    5_2: -T_beta/2=(3t^2-6t+1)/23.              (1.3)

These identities hold on the full two-variable framing
chart, rather than on finitely many frames. The omitted
chart divisors are retained when comparing the selected
relative source; (1.2) is a statement on its regular locus.

## 2. Independent sides of the determinant calculation

The Gaussian side is computed directly from the actual
balanced crossing Hessians and amplitudes. The integral
closure lattice has d=m+1 variables: d=5 and d=7 in the
two words. The Hessian has its two independently
differentiated framing null vectors. Its transverse
determinants are nonzero, of ranks 3 and 5. The squared
normal density is

    a_beta^2 det(d chi/d(r,s))^2/det(-H_perp).

The torsion side is computed independently from dF_beta-I,
infinitesimal conjugation and d(H_b...H_1)(H_b...H_1)^(-1).
It does not use the crossing Hessian or an expected density
formula. Exact ranks make the holonomy complex acyclic.
Its determinant ratio is evaluated at the ordinary frame
(r,s)=(2,3); the general framing invariance of that ratio
was proved by the chain argument, not by interpolation.

The audit then proves (1.2) by exact equality of these
independent expressions in the full function field.
FLINT polynomial arithmetic in s,r and an explicit reduced
quadratic or cubic number-field arithmetic are used. No
finite-field sampling, interpolation or numerical rounding
is part of this equality.

## 3. The common scalar is an ordinary algebraic residue

Define S_4(t)=-1 and S_5(t)=t^2+2. The two constants in
(1.3) satisfy exactly

    -T_beta/2=1/[S_i(t) f_i'(t)]
            =Res_(v=t) dv/[S_i(v)f_i(v)].       (3.1)

For 4_1 this is -1/(2t-1)=(2t-1)/3. For 5_2 it is

    1/[(t^2+2)(3t^2+2t+2)]
                        =(3t^2-6t+1)/23

modulo f_5. Both S_i f_i' are units in their trace fields.
The Gaussian source coefficient is therefore a nonzero
algebraic residue at each simple marked parabolic place.

This is a concrete instance of the requested rigid-period
viewpoint: the coefficient is an evaluation in a finite
spectral algebra with its residue co-source. It does not
assert that the whole finite Kashaev invariant is already
the trace of these classical residues.

## 4. The uniform twist lemma suggested by both cases

This section records the prototype diagnostic, rather than the scope
of the main program. The subsequent
[arbitrary-bridge source reduction](arbitrary_bridge_source_reduction.md)
uses a 2k-plat with unrestricted k and crossing word, eliminates every
intermediate stage with its source and dual, and replaces the single
Riley residue by an endpoint determinant complex. No twist-family
assumption is imposed on that theorem or the intended volume result.

For the signed twist presentation already used in
[the A-curve note](a_polynomial_volume_limits.md#5-a-connected-infinite-class-from-the-twist-presentation),
let S_j(z) be the second-kind Chebyshev recurrence and put

    f_k(t)=(1+t)S_(k-1)(t^2+2)-S_(k-2)(t^2+2).

The prototypes are k=-1 and k=2. A precise next determinant
lemma is the following proposed uniform identity at a simple
nonabelian parabolic root:

    T_k=-2/[S_(k-1)(t^2+2) f_k'(t)].             (4.1)

Together with a uniform Gaussian/holonomy determinant map,
it would make the principal cut residue explicit for the
entire regular twist family. Equation (4.1) is not claimed
proved here for arbitrary k.

There is a direct route to the general algebraic calculation.
For A=[M 1;0 M^(-1)], B=[M 0;-u M^(-1)], W=AB^(-1)A^(-1)B,
the complete relation is

    A W^k-W^k B=R_k(A-B),
    R_k=(s-u-1)S_(k-1)(z)-S_(k-2)(z),
    s=M^2+M^(-2), z=u^2+(2-s)u+2.

At R_k=0, W^(-k)=S_(k-1)(z)(W^(-1)-(s-u-1)I).
Differentiating the relator therefore exposes the factor
S_(k-1) dR_k. At M=1,u=-t, dR_k=f_k'(t)dt on the
parabolic slice. This explains the denominator in (4.1).
What remains is the explicit determinant/source map from
that one-relator complex to the braid complex, with its
normalization. Merely observing the denominator is not a
proof of the uniform identity.

## 5. Relation to the required volume theorem

The geometric regulator action was already calibrated to
hyperbolic volume. This proposition fixes its algebraic
principal coefficient and its framing/cut dependence in
both prototypes, with the same residue rule. It provides
a testable common lemma for the general construction.

To prove the original volume limit, one still has to show
that the actual selected global quantum period pushes to
this marked source with a nonzero, subexponential comparison
factor. A nonzero local Gaussian coefficient alone does
not prove that statement. Neither this proposition nor the
Markov theorem is presented as a volume-conjecture proof.

[Exact characteristic-zero audit](../experiments/audit_cubic_framing_density.py).
[Results](../experiments/cubic_framing_density_results.json).
[Finite-field diagnostic evaluator](../experiments/audit_geometric_a_density.py).
