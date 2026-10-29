# Geometric local rigidity and the source lost by scalarizing quantum A

Research note, 26 October 2026. This supplies a local geometric period
for the proposed comparison and identifies a precise two-parameter
source defect when its two geometric branches are scalarized.

The uniform arguments are elementary polarized linear algebra, formal
Gaussian contraction of the existing tetrahedron module, and exact
Ore identities. The local formal period is not identified with the
selected finite ADO evaluation. No quantum volume limit is proved.

## 1. Positive shapes make marked gluing unramified

Take a positive complete geometric ideal triangulation with t tetrahedra,
as supplied by [the audited geometric input](ge_geometric_triangulation_audit.md).
Choose positive local orders and compatible logarithms

    u_j=Log z_j, v_j=Log z_j'', z_j''=1-z_j^(-1),
    tau_j=dv_j/du_j=1/(z_j-1), Im tau_j<0.          (1.1)

No compatible global branching is required for this calculation.
The already proved integral edge/peripheral identities give t-1
independent real edge rows, together with the marked meridian row.
Write their full-rank matrix as (A B). Its rows are isotropic:

    A B^T=B A^T.                                  (1.2)

The logarithmic gluing Jacobian at fixed meridian is

    J=A+B diag(tau_j).                            (1.3)

It is invertible. Indeed ker(A B) is a real Lagrangian subspace.
If J a=0, the shape tangent w=(a,diag(tau)a) belongs to its
complexification, so Omega(w,bar w)=0. On the other hand

    (i/2)Omega(w,bar w)=sum_j Im(tau_j)|a_j|^2<0

for every nonzero a. Thus a=0. This proves nonsingularity
uniformly, without a census or an imported rigidity proof.

The exponentiated gluing equations are algebraic on the open set
z_j(1-z_j)!=0. Multiplying (1.3) by their nonzero monomial
derivatives changes its determinant only by units. Hence the
marked-meridian projection of the geometric gluing germ is etale.
After passing to its residue field, its completed local ring is
K[[U]], U=Log m. Its successive shape coefficients are uniquely
recovered by the invertible Jacobian recursion. The complete shapes
are algebraic: at m=1 they are an isolated point of equations over
Q. This is a local algebraic rigidity statement for this gluing
branch, not a quantum-state selection theorem.

## 2. The two geometric peripheral slopes are distinct

Keep the full marked boundary convention already derived in
[the regulator note](boundary_regulator_period.md):

    Omega_red=-(1/2)dU wedge dV,
    U=Log m, V=Log l,
    m=M^2, l=L_intr^2.

Along the geometric branch normalize dU=1 and write
a_j=du_j/dU. The same polarized identity, now on the edge
coisotropic space, gives

    Im(dV/dU)=-2 sum_j Im(tau_j)|a_j|^2>0.         (2.1)

The vector a cannot vanish since dU=1. Thus the marked cusp
derivative tau_cusp=dV/dU is nonreal and nonzero. Complex
conjugation supplies a second nondegenerate gluing germ with
derivative bar(tau_cusp). Both map to (m,l)=(1,1).

Use the actual meridian coordinate u=Log M=U/2 and a specified
longitude lift L_c=+1 or -1. Its sign is retained. The two
longitude branches L_+,L_- satisfy

    L_+(0)=L_-(0)=L_c,
    L_+'(0)=L_c tau_cusp,
    L_-'(0)=L_c bar(tau_cusp).                     (2.2)

Their difference has a simple zero. These two local images form
a transverse two-branch subgerm of the peripheral curve. There
may be other components; no assertion of their absence or of
global irreducibility is made.

## 3. A nonzero formal period from the existing tetrahedron module

Let Q=exp(epsilon). Use the compact tetrahedron solution already
appearing in [the pointed gluing construction](pointed_tetrahedron_gluing.md):

    psi_Q(Qz)=(1-z)psi_Q(z), psi_Q=P_Q^(-1).

Here multiplication by z and forward Q-shift have quantum-torus
parameter R=Q^(-1). Keeping this inversion is essential. Its
formal logarithm on a compatible dilogarithm sheet is

    Log psi_Q(z)=-Li_2(z)/epsilon-(1/2)Log(1-z)
       -sum_(g>=1) B_(2g) epsilon^(2g-1)
                         Li_(2-2g)(z)/(2g)!.       (3.1)

It follows either by expanding the defining product formally or
by substitution in the displayed difference equation. Its leading
amplitude (1-z)^(-1/2) is nonzero on the nondegenerate shape cover.
Higher coefficients are rational functions of z after adjoining
the recorded square-root frame.

Write w=Log(1-z)=u+v+pi*i*k with k odd. The exact Gaussian shear
exp(-u^2/(2epsilon)-pi*i*k*u/epsilon) changes its leading action to

    F_j(u)=-Li_2(e^u)-u^2/2-pi*i*k*u,
    F_j'=v, F_j''=tau_j.

Its full shifted equation includes the half-step character

    phi(u+epsilon)=exp(-epsilon/2)(1-exp(-u))phi(u). (3.2)

This factor is retained, rather than set to one. Finite-root Weyl
characters and SL2 lifts still have to be matched in the actual
state comparison; a formal square-root convention alone does not
identify those finite-level data.

For completeness, a nondegenerate formal Gaussian presentation
can always be obtained. Since det(A-iB)!=0 by Section 1, its
multilinear column expansion has a nonzero term choosing one
column from each A_j,B_j pair. Swap (u_j,v_j)->(v_j,-u_j) for
the corresponding subset. The new B is invertible. These
partial formal Fourier transforms keep Im tau_j<0, because
tau_j becomes -1/tau_j, and keep the local amplitude a unit.
They act on the existing quantum torus; they are not a claimed
global tetrahedral face-tensor comparison.

Complete the real gluing rows to a symplectic matrix (A B;C D),
using the marked half-longitude lift so that the last momentum
is p_U=-V/2. All affine reference characters are retained as in
the regulator centering calculation. For invertible B, the full
generating action in constraint values q is

    W(u;q)=sum_j F_j(u_j)+(1/2)u^T B^(-1)A u
                 -u^T B^(-1)q+(1/2)q^T D B^(-1)q. (3.3)

Both quadratic matrices are symmetric. The last term is necessary
for the marked momentum: at a critical point,

    partial_q W=-B^(-T)u+D B^(-1)q=p.

The internal Hessian is

    H=diag(tau_j)+B^(-1)A, Im H<0.                (3.4)

It is invertible. In particular there is a nonzero local formal
period, with a Gaussian leading coefficient equal to the product
of the local units times det(-H)^(-1/2), and the specified Fourier,
measure and character factors. The half-density cover retains all
these roots; their absolute scalar is not equated to the ADO cut.

Here the formal Gaussian is well-defined for an elementary reason.
Subtract W_* and the full quadratic t^T Ht/2, leaving terms of
degree at least three. Wick contraction has covariance
-epsilon H^(-1). At each epsilon order only finitely many cubic
and higher vertices can contribute. Its leading coefficient is
the nonzero amplitude at t=0. No leftover quadratic divided by
epsilon is admitted. Formal integration by parts follows directly
from the same Wick rule, so this is the local formal gluing period
of the supplied tetrahedron and edge equations.

All coefficients are regular at the complete point: the shape
denominators and Hessian determinant there are units. This does
not show that a finite root-level projected vector is nonzero,
or that the formal series converges on the desired sequence.

## 4. The dual line has the actual marked regulator action

Distinguish the gluing vector from its period functional. At fixed
edge values (3.3) gives dW_*=-V dU/2. Thus its scalar state has
inverse-longitude leading shift in the actual M convention.
The dual formal line has action -W_*.

The exact Bloch identity used in
[the actual action proof](quantum_longitude_and_regulator_action.md)
applied to (3.3) gives, at the complete point,

    Im W_*=-D(beta_T)=-Vol(M).                     (4.1)

Indeed the quadratic coefficients are real, the complete constraint
values and reference linear coefficients are purely imaginary,
the internal derivatives vanish, and the boundary quadratic term
at those values is real. Its imaginary part is therefore precisely
the negative tetrahedral Bloch sum. No imaginary integration
constant is selected to force this value.

Put h=Log q, epsilon=Log Q=2h and

    S_geo=-W_*/2, R_geo=-W_*-UV/4.                 (4.2)

Then the dual line exp(S_geo/h) satisfies

    dS_geo=(V/2)d(U/2),
    dR_geo=-(U dV-V dU)/4,
    Im S_geo|_complete=Vol(M)/2.                  (4.3)

The retained SL2 longitude sign is its explicit solution character.
Its meridian ratio has leading value L_intr, rather than its inverse.
Consequently this dual formal line has the already marked regulator
connection and complete regulator norm. This identifies which
formal line is the candidate for the actual classical action;
it does not identify a finite state with the dual of another state.

On either geometric embedding, its normalized ratio has the form

    a(h,u)=L_intr(u)+h a_1(u)+h^2 a_2(u)+...,

with every coefficient regular at u=0. The exact action differential,
algebraic unit leading amplitude and rational Gaussian vertices
show that these coefficients are algebraic on the normalized
gluing germ. Thus the two embeddings supply two regular formal
ratios with the distinct slopes (2.2).

If an operator of this dual gluing module annihilates the local
section, its first nonzero classical symbol vanishes on this
geometric longitude branch: substitute the ratio and take the
constant formal coefficient. This gives the geometric factor
for that gluing object. It does not identify the annihilator
ideal of the selected ADO sum with the dual gluing ideal.

## 5. A scalar quantum-A equation must retain the collision data

Let sigma(u)=u+h, S=C[[u,h]], and a,b in S^times be any two
such regular ratios, with a(0,0)=b(0,0)=L_c and

    kappa=partial_u(a-b)(0,0)!=0.

For a scalar operator P=sum p_j(h,u)T^j, put
P_0(u,L)=sum p_j(0,u)L^j and P_1=sum [h]p_j L^j.
The first-order right-remainder calculation gives on a branch

    (P_0)_L a_1+P_1+(L L'/2)(P_0)_(LL)=0.          (5.1)

If P annihilates both regular formal lines, evaluate at the collision.
Subtract their two conditions to obtain

    (L_c/2)(L_+'-L_-')(P_0)_(LL)(0,L_c)=0.        (5.2)

Thus P_0 cannot be just the reduced two-branch equation times a
factor nonzero there: that would have (P_0)_(LL)!=0. It must
retain additional vanishing data, such as a meridian factor or
an additional characteristic multiplicity. This is a necessary
condition on a proposed comparison operator. It does not assert
that the unknown actual minimal knot operator already acts on
both formal geometric lines.

There is an exact model with no extra characteristic branch.
Write Delta=a-b. The primitive regular second-order operator

    P=ab sigma(Delta)-(a sigma(a)-b sigma(b))T+Delta T^2 (5.3)

annihilates both lines. Substitution gives zero on each without
division. Its classical symbol is

    P_0=(L_+-L_-)(L-L_+)(L-L_-).                   (5.4)

The additional factor L_+-L_- is u times a unit. Nevertheless
the quantum coefficients have no common local divisor. Indeed
Delta and sigma(Delta) have independent linear parts:

    Delta=kappa*u+beta*h+O((u,h)^2),
    sigma(Delta)=kappa*u+(kappa+beta)h+O((u,h)^2).

Their Jacobian determinant is kappa^2, so they generate (u,h).
The constant and leading coefficients in (5.3) are units times
sigma(Delta) and Delta. The coefficient ideal is exactly (u,h),
which has no common nonunit divisor. Cancelling the meridian
factor after h=0 therefore changes the integral quantum data.

## 6. The complete cyclic source is a length-one point defect

On the split semilinear module V=S e_a direct_sum S e_b let
T e_a=a e_a, T e_b=b e_b and choose e=e_a+e_b. The two-vector
cyclic frame (e,Te) has determinant b-a and cokernel S/(Delta).
It is not in general T-stable. Keep every shift and define

    Lambda=sum_(j in Z) S T^j e subset V.

Use f=(1,0), e=(1,1), so V=S e direct_sum S f. The differences
of the two components of Te and T^2e are

    Delta, a sigma(a)-b sigma(b)
      =a sigma(Delta)+Delta sigma(b).

They generate (Delta,sigma(Delta))=(u,h). Every shifted component
difference vanishes at (0,0), including negative shifts since
a,b are units. Hence exactly

    Lambda=S e direct_sum (u,h)S f,
    V/Lambda=S/(u,h), T acts on this quotient by L_c. (6.1)

This is a length-one source supported at the simultaneous quantum
and meridian point. Lambda has rank two but three generators in
its complete fiber. A free presentation has generators e,u f,h f
and the single relation h(u f)-u(h f)=0.

Its ordinary dual loses that point quotient:

    Lambda^vee=V^vee, Lambda^(vee vee)=V.           (6.2)

For a direct proof, a functional on the ideal (u,h) sends u,h
to A,B with hA=uB. Coprimality forces A=u c,B=h c, so it
extends uniquely to S. This proves (6.2) without a duality theorem.
The normalization or generic period line alone has therefore
forgotten a specified source even though all its dual vectors lift.

The same free presentation also computes the part retained by
duality with its relation included:

    Ext^1_S(Lambda,S)=S/(u,h).                    (6.3)

Indeed applying Hom(-,S) to S -> S^3 -> Lambda gives the row
(0,h,-u), whose image is (u,h). Thus keeping that single
relation retains the source that the ordinary dual loses.

The ordered two-variable residue of this source has nonzero value

    Res_0 du dh/(Delta sigma(Delta))=1/kappa^2.     (6.4)

This follows directly from their invertible Jacobian. It is a local
algebraic source residue, not the hyperbolic volume or the value
of the selected knot invariant.

## 7. Relation to the actual source and what remains

### A fixed-level nodal order and its cut can be compared explicitly

Fix N first and retain the two geometric branches marked in (2.2).
Write d(u)=L_+(u)-L_-(u), so d'(0)=kappa. Their spectral order is

    A_geo=R[xi]/(xi(xi-d)), R=C[[u]],
    xi=L-L_-.

The actual two-color Casimir pair c_0,c_last has local order

    A_src=R[t]/(t(t-delta_s)),
    delta_s=c_last-c_0=rho(M^2-M^(-2)), t=z-c_0.

The unit alpha=delta_s/d has alpha(0)=4rho/kappa. Choosing
c_last -> L_+ and c_0 -> L_- fixes the explicit isomorphism

    psi:A_src -> A_geo, psi(t)=alpha xi.           (7.1)

It transports the partial normalization and conductor (u,t)
to their geometric counterparts. On the fraction fields it also
sends the actual source projector E_last=t/delta_s to the
geometric branch projector xi/d. Their polar residues therefore
agree under the same map. This is a marked local-order
comparison; choosing these branch marks is not a proof of the
global quantum period comparison.

Let Phi_src be the actual scalar pivotal cut on the local pair.
Put C=M+M^(-1), D_N=M^N+M^(-N), c=q+q^(-1). The already proved
two-color projector weights give the exact whole-germ formulas

    A(u)=Phi_src(1)=(-1)^N c C/D_N,
    B(u)=Phi_src(t)=(-1)^N rho C(qM^2-q^(-1)M^(-2))/D_N. (7.2)

For example the two projector numerators add to
(q+q^(-1))(M^2-M^(-2)); their common denominator is
M^(2N)-M^(-2N). Dividing by the original color dimension
ratio cancels M^N-M^(-N) and leaves precisely D_N. This
derives (7.2), including its full 1+U factor:

    D_N=M^(-N)(1+U), U=M^(2N).

No specialization of that peripheral factor was made in deriving
the comparison.

Use the geometric algebraic residue Phi_geo(a+b xi)=b. It is
perfect, but its value on 1 is zero. A scalar rescaling cannot
generally match (7.2). The unique matching unit density is

    theta=theta_0+theta_1 xi,
    theta_1=A,
    theta_0=B/alpha-A d
       =(-1)^(N+1) [d/(M-M^(-1))]
                   (q^(-1)M^2-qM^(-2))/D_N,
    Phi_src(a)=Phi_geo(theta psi(a)).              (7.3)

This equality is checked on 1,t and therefore holds identically.
At completeness it reads

    theta_0(0)=(-1)^N kappa*rho/4,
    theta_1(0)=(-1)^N(q+q^(-1)).                  (7.4)

The first coefficient is nonzero, so theta is a unit. For N>2
the second is nonzero as well. It is fixed by the actual pivotal
cut and must be retained. Equivalently the complete actual
Casimir projector and its nilpotent satisfy

    Phi_src(e_0)=(-1)^N(q+q^(-1)),
    Phi_src(J_N)=(-1)^N rho^2.

These are precisely (7.4) under t -> (4rho/kappa)xi. The full
ADO cut multiplies theta by the original d_N(M), keeping eta_N.

In fact that full density has a fixed rational central presentation.
Put Y=M^2, U=M^(2N) and zeta_N=q^(N(1-N)/2)=i^(1-N). Then

    Theta=d_N(M)theta
      =zeta_N U/((U-1)(U+1))
          [d(u)(q^(-1)Y-qY^(-1))
                  -(q+q^(-1))(Y-Y^(-1))xi].        (7.5)

This follows by writing d_N(M)=eta_N(M-M^(-1))M^N/(U-1)
and D_N=M^(-N)(1+U) in (7.3). Its only N dependence is the
specified root data and evaluation U=Y^N. Both peripheral
factors and the full phase remain. At M=1 the numerator and
U-1 must be combined on that actual root curve before evaluation.
The expression is not a replacement of the root constraint by
an independent geometric central character.

Every fixed meridian jet of (7.1), (7.3), and their inverses is
polynomially bounded in N in these marked bases. Indeed kappa
and the geometric Taylor coefficients are fixed, rho has size
comparable to 1/N, and D_N=2cosh(Nu) has fixed-order Taylor
coefficients polynomial in N and constant term two. The other
vanishing ratios have nonzero normalized constant terms; their
inverse coefficients follow by finite recursive division.
At the complete fiber the full density's coefficients have
sizes O(N^(-2)), O(N^(-1)), and its inverse has coefficients
O(N^2), O(N^3), respectively. These bounds keep all phases.

This controls a local, non-scalar source/cut normalization. It
does not identify the difference transport or chosen global
section, control jets whose order grows with N, or exclude
cancellation in the final scalar contraction.

### The fixed-level wall and the two-parameter point remain distinct

At each fixed N the actual
[meridian source order](intrinsic_cut_and_meridian_atlas.md)
has an elementary partial normalization, quotient C[[u]]/(u),
and a conductor dual. The formal geometric scalarization here
has the different two-parameter defect S/(u,h). Both are
explicit data erased by generic line comparison. They must
not be identified merely because each has length one.
The relation q_N^N=-1 in the actual root family is additional
data beyond the formal completion at h=0. The local comparison
must retain the actual root germ and pointing as well.

The [full integral cut theorem](integral_projective_cut_duality.md)
provides the actual self-dual centralizer and its unit-group
torsor. Section 6 explains why order or dual-lattice comparison
alone can still miss the cyclic source pointing. A full
comparison must carry that source as well as its operator,
selected section and cut functional.

The positive triangulation now supplies an unramified marked
gluing germ, a nonzero local formal period, the required dual
regulator action, and a concrete scalarization constraint at
the peripheral collision. The actual finite ADO source has
not been transported to that formal geometric line. Nor has
its coefficient or possible cancellation in the selected
period been established. No asymptotic specialization of the
formal series is assumed. The original target remains

    (4/N)log|F_N(1)|-log||P_hyp|| ->0.

## 8. Coverage and exact diagnostics

Geometric deformation and peripheral-potential theory are existing
subjects of [Neumann--Zagier, Volumes of hyperbolic three-manifolds](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1016/0040-9383%2885%2990004-7/fulltext.pdf).
Its introduction and scope were consulted for coverage, not its
proof techniques. No novelty claim is made for polarized
transversality, formal stationary phase or cyclic-vector methods.
The arguments above reconstruct the exact statements needed for
the current marked ADO comparison. The old analytic AK volume
calculation remains a separate state-comparison problem.

[The audit](../experiments/audit_geometric_rigidity.py) checks
25 exact rational-complex symplectic gluing charts with one to
five tetrahedra, including singular B blocks requiring partial
Fourier changes. It checks invertibility, the marked cusp energy
identity, all Hessian/Jacobian coordinate factors and the full
boundary Gaussian derivative. The local tetrahedron difference
equation is checked through epsilon^5, retaining its half-step
character. Six exact Ore examples test both remainders, the
classical meridian factor, the absence of a common local quantum
divisor and the nonzero point-defect residue. These are abstract
uniform diagnostics, not six claimed knot operators.
Eight additional cases at N=2,3,4,5,6,9,12,15 check the actual
nodal cut formulas and the matching unit density, both at the
complete fiber and at a generic color. The geometric slope in
these finite-field diagnostics is an arbitrary nonzero parameter;
the cusp nonvanishing itself is proved in Section 2.
[Results](../experiments/geometric_rigidity_results.json).

Reproduce with:

    python3 experiments/audit_geometric_rigidity.py

The subsequent [cut-wall source theorem](cut_wall_and_cyclic_source.md)
now relates the two-parameter cyclic point module above to the
actual cut. Its normalized branch density values are -p,sigma(p),
where p=q^(-1)M^2-qM^(-2). The resulting point ideal, regularized
cut presentation and calibrated residue agree with the geometric
cyclic model after an explicit regular formal unit gauge. The
physical ADO common frame remains fixed. This identifies a local
source presentation, while the global difference action and
selected quantum period still have to be compared.
