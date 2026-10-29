# The fusion kernel has a rational symplectic chart with a retained source wall

27 October 2026. The explicit actual fusion kernel determines a
birational symplectic relation on its regular interior symbol chart.
Its right Euler argument is a ratio of relative MOMENTA, not a
physical position by definition. The exact finite kernel also has a
nonzero bottom wall, and the original source detects that wall after
an actual crossing. The Euler basis orientation is fixed by the
original cap; reversing it gives a different boundary valuation.

These results make the local comparison concrete while retaining the
source issue. They do not prove that the selected finite root period
has a nonzero geometric image or the hyperbolic-volume exponent.

## 1. Kernel, shifts and the exact bottom wall

Use the notation of [the actual fusion-clock proof](actual_fusion_right_euler_clock.md):

    C_(u,v;a,j)=x^(u-a) F_a F_v/[F_(a-u) F_j],
    F_r=(Q;Q)_r,
    0<=u<=a<N, v=j+a-u<N,

and zero outside that support. Let S_a increase the relative a
label by one, with its top arrow zero. Let S_u similarly increase
the physical first index. Put D_a=diag(Q^a), D_j=diag(Q^j),
U=diag(Q^u), V=diag(Q^v), and let Pi_0 project onto physical
u=0 and Pi_top onto relative a=N-1.

There are the following exact finite-kernel identities:

    C D_aD_j=UV C,                                      (1)
    C F_j=F_2 C,                                        (2)
    C S_a-S_u C(1-QD_a)
       =Pi_0 C S_a-(1-Q^N)S_u C Pi_top.                 (3)

Here F_j is the balanced raising matrix on the relative j head;
F_2 is the same physical second-head lowering matrix. Equations
(1)--(3) hold for the displayed truncated kernel also at generic
Q where F_1,...,F_(N-1) are units. This generic-Q assertion is
only about the explicit kernel, not full generic-q braid fusion.

For (1), use u+v=a+j on every nonzero entry. Equation (2) follows
by consecutive j,v coefficients, or from the fact that physical
F_2 commutes with f_total and takes the seed e_0 tensor e_j to
(1-Q^(j+1))e_0 tensor e_(j+1). Its two top endpoints both vanish.

For (3), at u>0 and a<N-1 compare

    C_(u,v;a+1,j)
       =(1-Q^(a+1)) C_(u-1,v;a,j).

The factorial F_(a+1-u) and the exponent u-a-1 agree on both
sides. Excluded support also agrees. At u=0 only the first term
can survive, giving Pi_0 C S_a. At a=N-1 the left first term
is zero by truncation, and the other term supplies exactly the
displayed top correction. This is an entry proof at EVERY endpoint.

At the actual root Q^N=1, total lowering is intertwined exactly:
C S_a C^-1=f_total=F_1+K_1^-1 F_2. Thus the bottom wall in (3)
is the physical operator

    E_bottom=Pi_0 f_total=x^-1 Pi_0 tensor F_2.           (4)

It cannot be discarded on the strength of a regular interior symbol
identity. For example at N=2 take x=i, eta=exp(pi*i/4), and the
original positive crossing. Its coefficient from e_0 tensor e_1
to e_1 tensor e_0 is eta^-1. With the original pivotal cap g_0=-i,
the original highest-input/all-ones-output source gives

    Lambda_phys(R_+ E_bottom)=-2 eta^-1 !=0.             (5)

This is a literal original-word/source value. No new state or
unweighted trace is used. The uninserted cap of E_bottom alone
can vanish; that does not make its word-dependent source zero.

## 2. A regular interior canonical graph

Use commuting interior clocks A,J for the relative labels and U,V
for physical labels. Let K=A/U and impose AJ=UV. With logarithms
chosen locally, the factorial kernel has the generating expression

    S=-Li_2(A)-Li_2(V)+Li_2(K)+Li_2(J)-log(x)log(K).     (6)

Its exponent is obtained directly from the finite factorial atoms:
the leading logarithmic primitive of F_r is
[Li_2(1)-Li_2(Q^r)]/log Q. The four constants cancel in (6).
Equivalently one can define the interior symbol graph by the
coefficient-shift ratios; no convergence of growing-level periods
is required to define or verify the following algebraic graph.

Write p_A,p_J,p_U,p_V for exponentials of logarithmic covectors.
The kernel convention is that

    theta_out-theta_in=dS+lambda*dlog[UV/(AJ)],
    theta_in=log(p_A)dlog A+log(p_J)dlog J,
    theta_out=log(p_U)dlog U+log(p_V)dlog V.

Differentiating (6) and putting t=exp(lambda) gives

    p_U=t*x*(1-K),       p_V=t*(1-V),
    p_A=t*x*(1-K)/(1-A), p_J=t*(1-J),
    AJ=UV.                                              (7)

This convention matters: a raising operator on basis indices
acts on wavefunctions by a BACKWARD argument shift. It therefore
has principal value the inverse of the corresponding p coordinate.

Equations (7) give the explicit forward map

    z=x*p_J/p_A,
    K=1-(1-A)(1-J)/z,
    U=A/K,                 V=J*K,
    p_U=(1-A)*p_A,
    p_V=p_J*(1-J*K)/(1-J).                               (8)

This is a birational map between nonempty open cotangent tori.
All clocks and momenta are nonzero; the factors K, 1-A, 1-J,
1-V and their inverse-chart counterparts are kept invertible.
Its rational inverse is

    K=1-p_U*(1-V)/(x*p_V),
    A=U*K,                 J=V/K,
    p_A=p_U/(1-A),
    p_J=p_V*(1-J)/(1-V).                                 (9)

Substitution proves both inverse identities. On the graph AJ=UV,
the constraint differential vanishes, so (7) gives
theta_out-theta_in=dS. Taking an exterior derivative proves
preservation of

    dlog p_A wedge dlog A+dlog p_J wedge dlog J.

Thus (8) is symplectic. This is a direct graph theorem rather than
an inference from a dimension count or presumed quantum limit.

The exact relations underlying it include (1)--(3), physical total
lowering and the polynomial right-Euler relation already proved:

    x(1-U^-1 A_operator)f_R=(1-Q A_operator)(1-J_operator).

In the interior, right multiplication by f shifts (a,j) to
(a+1,j-1). Its wavefunction symbol is p_J/p_A. Thus its right
Euler argument has the definite symbol

    z=x*p_J/p_A=(1-A)(1-J)/(1-A/U).                      (10)

The last expression is valid on this regular commutative chart.
At the actual finite root, its apparent denominator is nilpotent
and has no inverse. Formula (10) is not an evaluation homomorphism
from the finite root representation to a geometric character.

## 3. Exact Euler conjugation fixes the orientation

On the relative regular module let R_f be RIGHT multiplication by
f, and now let z=x R_f be the nilpotent MATRIX. Set

    u(z)=sum_(r=0)^(N-1) z^r/F_r,
    v(z)=u(z)^-1,
    T_u=u(z), T_v=v(z).

At the actual root z^N=0, all 1-Q^k z are units and
u(Qz)=(1-z)u(z). The relative clocks obey
D_a R_f=Q R_f D_a and D_j R_f=Q^-1 R_f D_j. Consequently

    T_u D_a T_v=(1-z)^-1 D_a,
    T_u D_j T_v=(1-Q^-1 z)D_j,
    T_v D_a T_u=(1-z)D_a,
    T_v D_j T_u=(1-Q^-1 z)^-1 D_j.                       (11)

These are exact ordered finite matrices. Their clock product is
unchanged; the Q-shift in the second factor is required for this.

Let the actual word have fused RIGHT coefficient a. Its cap theorem
uses b=u^-1 a u. Right multiplication reverses composition, so

    R_b=T_u R_a T_v,
    W=C R_a C^-1=(C T_v) R_b (C T_v)^-1.                 (12)

Thus the new-to-physical basis fixed by the actual cap is C T_v,
not C T_u. With D_phys=(e_0 ell) tensor K_2^(1-N), its complete
matrix co-source is transported EXACTLY as

    D_new=(C T_v)^-1 D_phys (C T_v).                      (13)

Weighted trace proves the same original period on every physical
matrix. Restricting (13) to the right-word algebra recovers precisely

    Lambda_new(b)=gamma*rho_0[J_Q(z)b],
    J_Q(z)=1/[(1-z)(1-Qz)],
    gamma=N(xy)^(1-N)Q.                                 (14)

Indeed the original cap is gamma*rho_0[v(Q^2z) a u(z)]; substitute
a=u b v and use v(Q^2z)u(z)=J_Q(z). All original scalar lines
can be retained externally, and multiply both sides unchanged.

There is an additional orientation distinction. An operator
conjugation gives the PULLBACK by the inverse of a forward point
map. Hence the symbol point map of T_v, which occurs in the
actual basis C T_v, sends

    (A,J,p_A,p_J) -> (A/(1-z), J*(1-z), p_A,p_J).        (15)

Using the operator formula in (11) as the forward point map would
reverse (15) and produce an incorrect boundary interpretation.

## 4. The two Euler orientations have different boundary valuations

Put delta=1-z, and hold regular generic input A,J fixed. Compose
the forward map (15) with (8), and put

    D_plus=A-AJ*delta+(J-1)*delta^2.

For the ACTUAL new-to-physical basis C T_v one obtains

    U=A*z/D_plus,         V=J*D_plus/z,
    U -> 1,              V -> AJ.                       (16)

The corresponding p_U=(1-A/delta)p_A has a simple pole for generic
nonzero A. Thus there is a real singular symbol chart, but its
first clock has valuation zero, with limiting value one.

The OPPOSITE basis C T_u instead uses A*delta,J/delta in (8).
Writing D_minus=J-AJ*delta+(A-1)*delta^2, it gives

    U=A*z*delta^2/D_minus,
    V=J*D_minus/(z*delta^2),
    delta^-2 U -> A/J,   delta^2 V -> J^2.               (17)

Therefore an apparent match to a quadratic escaping geometric
position can select the wrong Euler orientation if one tracks
only valuations. Formula (17) is not the forward primal map of
the word basis dictated by the original source in (12).

Neither calculation identifies this fused first-plus-tail clock
with the internal second-meridian position of the universal-cut
geometric chart. Such a marking would require an actual word and
source comparison. The original first source is highest input;
the prior regular geometric block used a suitable high-input phase.
Those are related by exact Ward identities, not by forgetting
the bottom source wall (3)--(5).

## 5. Scope and independent checks

The regular local canonical graph is now explicit and symplectic,
and the exact source/basis transformation is specified. The
finite endpoint wall is also explicit and is detected by an
original word. This is usable input to a whole period transform.
It is not a proof that the selected class crosses to the marked
geometric A-component, that its coefficient is subexponential,
or that its global norm has the hyperbolic-volume growth.

The [audit](../experiments/audit_fusion_canonical_source_chart.py)
and [saved results](../experiments/fusion_canonical_source_chart_results.json)
pass twelve exact kernel cases and six actual root Euler/source
cases at N=2,...,7. They check both boundary terms, exact Euler
clock orientation, literal signed-word source transport and nonzero
word-coupled bottom-wall periods. A separate symbolic calculation
checks the rational inverse and all six independent logarithmic
Poisson brackets, as well as both distinct Euler boundary limits.
The proofs above establish the identities; finite checks verify
their conventions and endpoints.
