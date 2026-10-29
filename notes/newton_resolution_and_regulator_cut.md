# The Newton chart resolves the complete boundary point and its cut

Research proof, 27 October 2026. The exact Newton source transform has
a classical meaning at the complete hyperbolic boundary character:
it resolves the signed peripheral singularity and turns completeness
into the stationary equation of the universal cut kernel. This is
uniform in the knot and its bridge number.

The actual quantum Newton transform and its coefficient recurrence
are separate exact constructions. This note compares their classical
chart and kernel with the marked geometric target. It does not prove
that a chosen actual operator has geometric classical support, or
that the actual selected period couples to that geometric branch.
The volume conjecture remains unproved.

## 1. The classical Newton coordinates

Use the boundary quantum-torus convention TY=QYT. Its commuting
symbols are Y,L. Weighted Weyl inversion sends (Y,L) to
(Y^(-1),L^(-1)). Put

    x=Y+Y^(-1), s=L+L^(-1), z=YL+(YL)^(-1).

Direct expansion gives the Fricke surface

    x^2+s^2+z^2-xsz-4=0.                         (1)

In the Newton coefficient chart write u for the index character
Q^n and e for the symbol of the forward coefficient shift. The
rational map to (1) is

    x=e^(-1)+u+u^(-1),
    s=u+u^(-1)+(u-u^(-1))^2 e,
    z=u(x+s)-2.                                  (2)

Away from the displayed denominator loci its inverse is

    u=(z+2)/(x+s), e=1/(x-u-u^(-1)).              (3)

In the full boundary torus these coordinates are

    u=(YL+1)/(Y+L),
    e=Y(Y+L)(YL+1)/[L(Y^2-1)^2].                 (4)

Both functions are Weyl invariant. Substitution proves (2)--(4).
Their differential identity is

    dlog Y wedge dlog L=dlog u wedge dlog e.      (5)

Thus this is a symplectic birational chart on the Weyl quotient,
with a degree-two map from the full torus. It does not remove the
marked eigenvalue/sign cover where that cover is needed.

The exact whole-source operators X,S,Z and their finite-root
lattice are proved in
[the whole-source transport note](whole_source_newton_transport.md).

## 2. The complete signed point and a regular exceptional curve

Work at the marked complete point

    Y=1, L=-1, (x,s,z)=(2,-2,-2).                (6)

This is a singular point of (1). The sign in (6) is retained as
part of the longitude lift. A convention with a different complete
longitude must first apply its corresponding recorded sign change;
substitution of L=1 into (4) is a different chart situation.

Define

    g(u)=2-u-u^(-1), r=1-e g(u).                 (7)

Equation (2) gives the exact identity

    r=e(x-2).                                    (8)

The curve

    E_cut: r=0, e=-u/(u-1)^2                     (9)

maps entirely to (6). Indeed x=2; also
(u-u^(-1))^2/g(u)=-(u+1)^2/u, so s=-2 and z=-2.
This curve is regular for u!=0,1,infinity in the Newton torus.
The two-form in (5) becomes

    dlog u wedge dlog e
          =-du/u wedge dr/(1-r).                 (10)

It is nondegenerate at r=0. Thus the chart resolves this portion
of the singular boundary point symplectically, with a genuine
regular normal coordinate r. Its exceptional curve is not deleted
by taking the complete value first.

## 3. The geometric branch meets this curve transversely

Take a marked positive geometric gluing branch etale over the
meridian, as supplied by the existing positive gluing-Jacobian
proof. Put y=Log Y and lambda=Log(-L), centered at (6), and write

    lambda(y)=tau y+O(y^3), Im tau>0.             (11)

The positive imaginary sign uses the recorded boundary orientation.
The absence of even powers uses Weyl inversion and preservation of
the marked place. Generically swap the two peripheral eigenflags.
At the complete nontrivial parabolic meridian they both specialize
to its unique eigenline. All developed flags and their cross-ratios
therefore specialize to the same nondegenerate positive shapes.
The smooth gluing germ is the same normalization place after this
swap. The involution fixes it and sends y,lambda to -y,-lambda.
Etaleness over y then gives the odd expansion (11). This also
explains why the eigenflag cover is retained before quotienting.

Substitution in (4) gives finite limits

    u_0=(tau+1)/(tau-1), e_0=(1-tau^2)/4.        (12)

For example the first quotient is
-(sinh((y+lambda)/2))/(sinh((y-lambda)/2)); its common simple
zero cancels since tau!=1. Formula (12) follows directly from
the first-order terms of the numerator and denominator in (4).
Both functions are even holomorphic germs in y. Moreover

    Im u_0=-2 Im tau/|tau-1|^2<0,
    e_0=-u_0/(u_0-1)^2!=0.                     (13)

The trace-normal coordinate w=x-2=y^2+O(y^4) is a parameter on
the normalized Weyl-quotient geometric germ. Its strict transform
in the Newton chart satisfies, exactly,

    r(w)=e(w)w, r'(0)=e_0!=0.                  (14)

Consequently the geometric germ is smooth there and intersects
E_cut transversely. It is etale over r. Every nilpotent r-lift
of that selected geometric place has a unique curve lift by the
same elementary inverse-function/Newton argument. This statement
requires no hypothesis that u itself be a local parameter.
If its u projection ramifies, one retains the two-coordinate curve
rather than dividing by du/dw.

The cusp derivative tau is algebraic at the complete shape place:
differentiating the integer gluing and peripheral equations gives
an invertible linear system with algebraic coefficients. Hence
u_0,e_0 are algebraic there too. A cusp field can be smaller than
the full marked shape field. The pair (u_0,e_0) need not distinguish
every representation place; the original geometric/shape marking
is retained. The lower-half-plane condition alone is not a global
geometric-selection theorem.

## 4. The same exceptional curve is the stationary cut equation

The actual Newton kernel is

    t_n(Y)=product_(j=1)^n(Y+Y^(-1)-Q^j-Q^(-j))
       =(-1)^n Q^(-n(n+1)/2)(QY;Q)_n(Q/Y;Q)_n. (15)

For H=Log Q, U=Log u and a matched logarithmic sheet, its leading
generating action is

    K(Y,u)=i*pi*U-U^2/2+Li_2(Y)+Li_2(Y^(-1))
                                -Li_2(uY)-Li_2(u/Y). (16)

Its derivatives are exact dilogarithm identities:

    partial_U K=Log(x-u-u^(-1)),
    partial_y K=Log[(uY-1)/(Y-u)]=Log L.         (17)

The logarithms are continued together; integers in their sheets
are not independently reset. Equation (17) is precisely the
canonical relation (4), with e=exp(-partial_U K). It can be
checked without an asymptotic argument. Formula (16) is the
integral of Log(x-v-v^(-1)) dlog v from the lower endpoint of
the product, on the same sheet; ordinary Euler summation recovers
it wherever that product avoids its endpoint/polar divisors.
No uniform selected-knot asymptotic is inferred from this local
kernel calculation.

If a coefficient branch has action S_c with dS_c=Log e dlog u,
the stationary equation for its pairing with the cut at Y=1 is

    partial_U(S_c+K(1,u))=0
       iff e(2-u-u^(-1))=1
       iff r=0.                                  (18)

Thus the universal cut meets the transformed geometric branch
at exactly the resolved complete point (12). Completeness becomes
a transverse Lagrangian intersection in the regular Newton
surface. This is a general geometric statement, not a recognition
from the two prototype knots.

The transform preserves the peripheral action differential:

    d(S_c+K)=Log L dlog Y                        (19)

on its stationary relation. The marked Bloch fundamental class
still supplies the integration constant and the complete volume
value. Equation (19) alone does not determine that constant or
show that the actual coefficient solution has this branch.

## 5. The finite-root normal adapter and its N-squared factor

Let C_N(x) be the monic Chebyshev polynomial defined by
C_N(Y+Y^(-1))=Y^N+Y^(-N). With U_c=Y^N retained, the exact
central corner is

    W=U_c+U_c^(-1)-2=C_N(x)-2.                  (20)

It has the polynomial factorization

    C_N(x)-2=(x-2)H_N(x), H_N(2)=N^2.          (21)

For the value, put x=2cosh y and differentiate
2cosh(Ny)-2=N^2 y^2+O(y^4),
2cosh y-2=y^2+O(y^4). Equivalently differentiate the polynomial
identity at x=2; this is an exact algebraic leading coefficient.
Thus W=N^2 w+O(w^2). The central trace normal and the ordinary
trace normal have a specified, nonzero N-squared adapter. This
does not identify their normalization with that of the first
Bockstein normal U_c-1: W=(U_c-1)^2/U_c is quadratic in it.
In logarithmic eigenvalue coordinate y, U_c-1=N y+O(y^2), so
the physical first-normal cut carries N, while the trace-to-trace
adapter carries N^2. Both directions and factors are retained.

At U_c=1, H_N(X)/N^2 is exactly the projector onto the simple
X=2 line of the full abstract source lattice fiber: it is one
there, and zero with the required multiplicities at the other
roots of C_N(X)-2. This is the distinguished source line proved
in [the source/monodromy chain-map note](source_lattice_monodromy_chainmap.md).
It is a statement about that retained source fiber, not a global
rank-one projector on the unsplit generic field cover.

## 6. Remaining source-selection theorem

This supplies a regular algebraic geometric target and a canonical
cut equation, with the exact normal adapter. Rivin positivity and
the gluing Jacobian select its marked algebraic place. The actual
quantum Newton transform preserves the original period and its
normal source data.

To prove the conjecture one still has to establish that the actual
coefficient/module object carries this geometric branch with the
selected regulator period, and control its norm at the prescribed
cyclotomic evaluation. Transversality proves a nondegenerate
geometric candidate intersection. It does not by itself give its
coefficient in the original selected quantum period, exclude
cancellation, or prove a uniform asymptotic estimate.

[Exact algebraic audit](../experiments/audit_newton_resolution_and_regulator_cut.py).
[Audit results](../experiments/newton_resolution_and_regulator_cut_results.json).
[Independent proof audit](newton_resolution_independent_audit.md).

The [actual Newton canonical transform](newton_actual_source_canonical_transform.md)
proves the generic coefficient recurrence and exact selected whole-germ
period, with finite actual pointing. The
[partial geometric-support theorem](partial_geometric_support_theorem.md)
now proves a geometric factor for an actual two-index extension by
transverse-only telescoping. Its final framing contraction is still
required to reach the selected scalar invariant.
