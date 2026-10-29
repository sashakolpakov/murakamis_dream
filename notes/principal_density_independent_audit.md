# Independent audit of the principal-density comparison

Audit, 27 October 2026. This checks Sections 5--6 of
[the uniform comparison](quantum_source_bridge_extension.md), with
particular attention to the perturbation pairing, cokernel marking,
determinant signs and the factor -1/2. No substantive defect was found
under the printed acyclicity, unit-chart and parity conventions.

## 1. Direct derivation of the rank-two perturbation pairing

The pairing in equation (5.8) has the printed positive sign. It can
be derived directly from the generating equations, avoiding any
ambiguity about exact boundary terms in the Liouville form.

Write P_0 for the permutation matrix, R for the transfer matrix,
and w=(q,c). At the chosen fixed point, a cut-fixed kernel tangent u
has a generating-family lift B_u=(q_u,c_u) and equal input/output
momenta p_u. Thus

    P_0 q_u+R c_u=q_u,
    S_cq q_u+S_cc c_u=R^t p_u.                  (1.1)

Perturb the phase by epsilon times a quadratic f centered at the
critical point, while holding an input tangent v fixed. Let tau be
the resulting variation of its transfers and pi the variation of
its output momentum. The linearized generating equations are

    P_0^t pi-S_qc tau=f_q(B_v),
    S_cc tau-R^t pi=-f_c(B_v).                  (1.2)

The mixed Jacobian is invertible by the stated crossing-unit
hypothesis, so these variations exist uniquely. Multiply the first
equation by q_u^t, use the second equation to eliminate R^t pi,
and then use (1.1). The result is

    q_u^t pi-p_u^t R tau
       =q_u^t f_q(B_v)+c_u^t f_c(B_v)
       =Hess(f)(B_u,B_v).                      (1.3)

The left side is exactly Omega(u,(partial_epsilon F)v), since the
output-position variation is R tau and the input is fixed. This
proves (5.8), including the cut source: its last covector is the
fixed input momentum p_1 and therefore acquires no perturbation.

## 2. Leading determinant coefficients and the endpoint volume

For a square map L of corank two, let B be its kernel basis and C
its cokernel coordinate map. With the torsion convention in the
comparison note, a perturbation L+epsilon E satisfies

    [epsilon^2] det(L+epsilon E)=det(C E B)/T_L. (2.1)

To verify this, use the input basis [B,V_c] and target basis
[L V_c,W], C W=I. Moving the two kernel columns past the
n-2 image columns contributes (-1)^(2(n-2))=1. The two epsilon
columns then give det(C E B), with the indicated torsion ratio.

For the symmetric phase Hessian, C=B^t and
T_H=det(B_chi)^2/det H_perp. For the endpoint, the rows in (5.5)
use coordinate volume, whereas the trailing-normal target volume
is its negative. Indeed the target basis

    (e_qj-e_q1 for j>1, all e_pj), followed by e_q1,

has determinant -1 in the canonical order. Consequently the
coordinate determinant's leading coefficient is

    -det(pairing)/T_cut^Omega.

Combining (1.3), (2.1) and the nonsingular determinant elimination
therefore gives exactly

    (product V_t) T_H=-T_cut^Omega.

The perturbation need not remain a sum of local crossing phases.
Its mixed Jacobian stays a unit near epsilon=0; only that unit's
constant determinant contributes to the leading epsilon^2 term.
This is sufficient for the argument in the source note.

## 3. The two remaining numerical factors

For the stated bases of ker ell and ker b_0, the canonical pairing
conversion matrix is

    K^t R(P) Z=[2/a^2 0;(c^2+1)/a^2 1].

Its determinant is 2/a^2. The endpoint torsion with the unconverted
product co-source is -T_beta, using the ordered bases printed in
Section 3 of the comparison note.

Directly differentiating the framing matrix gives its coefficient
matrix in K=(h+2f,e+f):

    C_frame=(1/Delta)
        [-(kappa/2+s)  r-1/2;
          kappa+s     1-r].

Its determinant is -1/(2Delta). Kernel and canonical cokernel both
change by this framing matrix, so the contribution is its square.
Thus

    T_cut^Omega(r,s)=-T_beta/(2a^2 Delta^2).

Finally det(-H_perp)=(-1)^(m-1)det H_perp, because the normal rank
is m-1. Combining this with the endpoint minus sign and the specified
(-1)^(b-1) parity normalization leaves (-1)^(m+b-1)=1 for a knot
braid. The remaining amplitude factor is a^2/K_1^2, giving

    Omega_beta^2=-(T_beta/2) Omega_cut^2.

## 4. Scope

The source and cokernel assumptions needed above are already present:
acyclicity of the four-term holonomy complex, ell(Au)=1 for the
removed conjugation direction, the actual fixed momentum cut, and
the unit mixed Jacobian. A generic equality of critical sets alone
would not supply them. The factor -1/2 is relative to the explicitly
specified parity normalization and does not choose a square-root
phase or its base-only quantum normalization.

The audit establishes no nonzero selected global period coefficient
and no archimedean volume growth. Those remain separate obligations,
as the comparison note states.
