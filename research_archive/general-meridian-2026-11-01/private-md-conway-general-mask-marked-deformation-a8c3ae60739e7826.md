# Actual marked deformation and smooth filling for every strict Conway mask tree

Private research draft, 31 October 2026. No manuscript/public changes.

This extends the complete geometric theorem in
`notes/actual_conway_general_strict_mask_geometry.md` to the original
pure/odd face pairings, their actual primitive peripheral paths, and the
absolute filled-volume calibration. A new port argument proves that all
complete leaves are at or above the quarter index. Thus the established
high and quarter local packet theorems cover every leaf. A global
nonempty-alias gap remains a separate hypothesis for knot patterns. The
all-core gap follows from retained-gate strict concavity as explained
below; the two-leaf all-odd link is a separately stated exception. No
general invariant limit is inferred from the geometric deformation alone.

## 1. Scope and complete data

Take a fixed literal expression C(FG) in leaves h, ordered products and
ordered turns T. Delete only the forced final product and retain its
original complementary-wire relation. Assume the reduced polytope has a
strict state: each leaf a_i lies in (0,1/2), and every retained product
satisfies max(x,y)<z<x+y<1. The positive action has a unique strict
optimizer and a negative definite reduced wire Hessian. The complete
geometry note constructs its actual two-ball right-angled augmented-link
exterior, with every original bowtie triangle, ideal vertex and oriented
ribbon path retained. It also proves that two corners of one leaf are
never transitively identified and each edge cycle has four distinct
occurrences.

An open expression has strict type L=(0,1/2), H=(1/2,1), A=(0,1), or
empty. The nonempty product table is LL,LA,AA -> A and HL,HA -> H,
including reversed orders; HH is empty. Turns exchange L,H and preserve
A. The strict cylindrical root pairs are AA,AL,AH,LH and their reverses.

For an optimized port of output b set

    B=cot(pi b), kappa=exp(-f_E'(b)),
    X²=(1+B²)/(1+kappa), Y²=kappa X², X,Y>0.

Thus X²+Y²-B²=1. The exact port types are

    L: (B,X,Y)=(B,B,1), B>0;
    H: (B,X,Y)=(-Y,1,Y), Y>0;
    A: -Y<B<X.                                           (1)

A turn maps (B,X,Y) to (-B,Y,X). At a strict product the children have
common X and, writing S=B_1+B_2>0,

    B_out=(B_1B_2+X²-1)/S,
    Y_out=Y_1Y_2/S.                                      (2)

Number the four port edges cyclically. FREE edges are 0,2. The actual
individual mask eta_j is one precisely when the nonport adjacent face
is SHADED. Its angles divided by pi are b-eta_j/2 on FREE edges and
1-b-eta_j/2 on CAP edges. L masks are supported only on CAP edges, H
masks only on FREE edges, and A masks vanish. The leaf mask is (0,1,0,1).
A turn rotates the mask. A product has mask
(eta^F_0,0,eta^G_2,0). The shared child FREE edge has angle
1-(eta^F_2+eta^G_0)/2; the sum of these bits can never be two at a
strict product. Root complementary types likewise forbid two shaded
bits on a closing seam. These are literal color/edge statements, not
pair-symmetric substitutes for the asymmetric H pattern.

## 2. A general quarter-index theorem

**Proposition.** At the complete optimizer of every strict closed tree
above, every port has X,Y<=1. Consequently every original leaf has

    1/4 <= a_i < 1/2.                                    (3)

Proof. Root complementarity gives B_F=-B_G and equality of the ordered
port metrics, hence common X,Y. In type AA the two strict inequalities
in (1) give |B|<min(X,Y). Since X²+Y²-B²=1, both X,Y<1. In AL, the L
port is (B,B,1), so the A port has B_A=-X>-Y=-1, giving X<1,Y=1. In AH,
the H port has X=1,B_H=-Y; the A port has B_A=Y<X=1, giving X=1,Y<1.
In LH the two explicit forms in (1) force X=Y=1. Reversing the children
does not alter these conclusions.

For the downward step put c=1-X². Since Y_i²=B_i²+c, the exact identity

    Y_1²Y_2²-(B_1B_2-c)²=c(B_1+B_2)²

and (2) give Y_out²-B_out²=1-X². Positivity therefore gives
X_out=X, the common child value. Every child type in (1) has B_i<=X.
Strict S>0 then gives B_i>-B_j>=-X. Thus |B_i|<=X and

    Y_i²=1+B_i²-X²<=1.

Starting with X_out<=1, both child X,Y are at most one. A turn merely
swaps X,Y. This proves the assertion by induction down the finite tree.
At a leaf X=cot(pi a)>0, so X<=1 is exactly a>=1/4. QED.

The equality case is real, not a forced-flat state. For example
C(h T(h^s)) has the unturned h^s port (1/s,1,1/s), its turn
(-1/s,1/s,1), and root leaf (1/s,1/s,1). The seed leaves have a=1/4
and the root leaf has a=atan(s)/pi. Every retained product is strict.
At a=1/4 the two source recurrence eigenvalues are +i and -i: this is
an equal-modulus boundary, not a repeated eigenvalue. No uniform strict
quarter inequality is asserted for this enlarged syntax.

## 3. Source branch and regular deformed charts

For each original leaf retain its physical half-twist sign epsilon_i
in {0,+1,-1}, in the ORIGINAL leaf frame. Define

    J(s)=integral_0^s Log(2 sin(pi u)) du,
    g(x,t)=J(2x)-2J(x)-J(x-t)-J(x+t),
    v=g_t=Log[sin(pi(x-t))/sin(pi(x+t))],
    chi=t-epsilon*v/(2pi i),
    f_epsilon(x,chi)=g(x,t)-epsilon*v²/(4pi i).          (4)

Branches continue from the strict complete state. For every strict leaf,
the derivative of the implicit shear is 1-epsilon*i cot(pi x), nonzero.
Thus (4) is a unique holomorphic germ, even in chi, and exactly

    df_epsilon=g_x dx+v dchi.                            (5)

The completed source identity proved on the high interval identifies
(4) with its selected finite-source action, with the original chirp.
The quarter packet theorem extends that SAME selected action across a
fixed neighborhood of 1/4 using an exponentially accurate actual-source
interpolant. Proposition (3) therefore covers the complete leaf set of
ANY fixed strict tree: each leaf is in the high region or in the proved
quarter neighborhood. No unproved continuation into arbitrary low
complete indices is needed.

For precision, the negative-source action and (4) have the same
K=exp(-f_x) branch of

    K²(1+E)²+K[(H+H^-1)E²+2]+(1-E)²=0,
    E=exp(2pi i x), H=exp(2pi i chi),
    K=tan²(pi x) at H=1.                                (6)

Their constant is fixed at x=1/2 for fixed small chi. There v=0,
t=chi, g(1/2,t)=0 by J(1/2+t)=-J(1/2-t), and the selected source
integral S=integral_x^(1/2) Log(mu) tends to zero with regular
mu(1/2,chi)=1. This argument does not incorrectly send t to zero.
The positive sign is Schwarz reflection with its physical sign retained.

Let y be the original reduced free wire coordinates and put

    A_epsilon(y,chi)=sum_i f_epsilon_i(x_i(y),chi_i)
                              +sum_retained_products m(x,y,z).

At chi=0 this is the complete positive action. Its invertible wire
Hessian gives a unique holomorphic critical branch y_*(chi). Let
Phi_epsilon(chi)=A_epsilon(y_*(chi),chi). By (5), its stationary wire
conditions are precisely the original ordered port metric matching,
with g_x evaluated at each hidden pure t_i. The turn relation b->1-b
and root complementary relation are retained literally. All finitely
many complete flags and three-point charts are nondegenerate by the
complete geometry theorem, so they remain regular on one small polydisk.

We use holomorphic second-copy charts: prism angle phases are inverted,
not complex-conjugated as free variables. In a normalized leaf port
(0,infinity,1,R), put T=exp(2pi i t) and

    Z=(1+E)/(1+T), R=T(1+E)²/[E(1+T)²],
    Z²-(1+E)Z+ER=0.                                    (7)

The two projection apices are Z and Z/E. This fixes the original
reflected-minus convention even when the deformed white pieces are
not planar.

## 4. The masked white-map induction: the new geometric step

Use the universal matrices

    W0=[[1,0],[0,E]], W1=[[1,E-1],[0,E]],
    W2=[[E-R,R(1-E)],[E-1,1-ER]],
    W3=[[R,0],[1-E,ER]].                                (8)

They fix the endpoints of their respective port edges. The stronger
induction invariant is:

* If eta_j=0, W_j is the actual transition to the second projection
  copy on the WHITE piece adjacent to that port edge.
* If eta_j=1, W_j is a VIRTUAL WHITE COMPLETION map, not a transition
  assigned to the actual SHADED face. It prescribes the white map
  that must lie on the other side of this surviving shaded edge once
  that edge is internal or closed.
* Every already internal original shaded edge has its actual adjacent
  WHITE map equal to that same completion map in the original leaf
  frame. Pieces already joined by WHITE/WHITE seams carry one entire
  identical Mobius map, including its translation.

At a leaf, W0,W2 are actual WHITE maps, sending Z to Z/E by (7).
W1,W3 are precisely the virtual completions at its two shaded CAP bases.
No fictitious leaf white face is introduced.

The exact generic prism identities in the original world charts are

    W_F1=W_G1=W_out1=B_top,
    W_F3=W_G3=W_out3=B_bottom,
    W_F2=W_G0,
    W_out0=W_F0, W_out2=W_G2.                            (9)

Here B_top and B_bottom are the actual WHITE prism triangle maps.
These are already verified rational identities in independent prism
phases, valid also when a child label is above 1/2. They use the
original maps F:(C0,C1,C2,C3)->(v0,v1,P,infinity) and
G:(C0,C1,C2,C3)->(infinity,P,v2,v3), not a reflected substitute.

There are exactly three relevant seam cases.

(a) A child CAP seam has the adjacent WHITE prism triangle. If the
child bit is zero, (9) identifies the two actual WHITE maps across
its flat seam. If it is one, the shaded face stays intact and the
prism supplies its required actual completion map B_top or B_bottom.

(b) At the shared FREE edge, the pair of bits is (0,0), (1,0), or
(0,1). In the first case the two actual WHITE pieces merge with equal
maps by W_F2=W_G0. In the second or third, the unmasked child's actual
WHITE map equals the masked child's completion map. The shaded edge
remains right and receives exactly the required transition. The forbidden
(1,1) case would be an HH strict product and never occurs.

(c) The remaining output FREE maps are inherited by the last two
identities of (9), with the same masks; both output CAP maps are the
new actual prism WHITE maps. This is exactly mask (eta_F0,0,eta_G2,0).

For a turn and a root closure the exact coordinate identities are

    T_Q(z)=(R-1)/(z-1),
    T_Q W_(j+1)(E,R)=W_j(E^-1,1-R) T_Q,

    C_Q(z)=(z-R)/(z-1),
    C_Q W_j(E^-1,R)=W_(2-j)(E,R) C_Q.                  (10)

The turn rotates the mask, so it transports actual and virtual maps
with their status unchanged. At the root, the complete type/mask rule
forbids two shaded bits on any paired edge. Thus a zero/zero pair
merges actual WHITE maps; a one/zero pair supplies the masked completion
from the actual WHITE side. There is no output left after closure.
EVERY original shaded base now has an actual neighboring white face
with its prescribed completion map.

Equations (9)-(10) prove the invariant without assuming the pair-symmetric
H pattern, without using b<1/2 for internal wires, and without treating
a virtual map as a face pairing before it is supplied. In particular,
turning a bare leaf and closing it against another bare or composite
child is covered by the same explicit cases.

It follows that every triangular piece of one original WHITE face
has one and the same full Mobius transition. This remains true when
the deformed pieces no longer lie in one geodesic plane. The theorem is
about the original abstract face-paired balls; deformed embeddedness is
not required.

## 5. Pure/odd shaded words and the actual group

In each ORIGINAL leaf frame retain

    S=[[0,-ER],[1,-1-E]],
    A=[[R,-R],[1,ER-1-E]],
    B=[[R/E-1-1/E,R],[-1,R]].                            (11)

S gives the pure within-copy shaded pairing. A,B give the actual odd
cross-copy pairings

    (Z,infinity,1)->(Z/E,R,0),
    (Z,R,0)->(Z/E,infinity,1).

At completeness these are the original half-disk rotations, so every
half-twist pattern has the same positive complete metric. The four
right-angle occurrences in each edge cycle stay distinct by the
complete terminal-pair invariant; changing the copy permutation does
not identify original leaf corners. The canonical shaded-side length-one
horospheres are preserved. Thus the actual half-twist partner also has
complete volume 2pi Phi_epsilon(0).

With bar(S) meaning E->E^-1, the pure edge identities are

    W0 S=bar(S) W0, W2 S=bar(S) W2,
    W3 S=bar(S) W1.                                     (12)

The odd edge identities are

    W0^-1 B W2^-1 A=I,
    W2^-1 B W0^-1 A=I,
    W1^-1 B W3^-1 A=I.                                  (13)

These generic rational identities hold for independent E,R. Section 4
is what makes every W in their base-edge words an ACTUAL final white
transition for general masks. All side, base and inverse words are
therefore pointwise identity, not just trivial linear parts.

The original closed cut consists of two actual topological balls.
Use their dual two-skeleton presentation: face transitions generate
and original edge words give relations. The WHITE seams and all
shaded relations have just been verified. They define an actual
holomorphic framed representation rho_chi of the original signed
augmented-link group, near its oriented complete holonomy. Turns and
products only conjugate the original leaf data into the common world
frame. They do not replace a physical leaf by an equivalent scalar
coupon or change its primitive disk curves.

At a leaf corner the two final original WHITE sectors, one possibly
supplied as a completion in Section 4, have maps W_(j-1),W_j. The
small actual main meridian is W_(j-1)^-1 W_j or its inverse. Both
fix the corner and have equal derivatives: E^-1 at C0,C2, E at C1,C3
in finite local coordinates. Hence its multiplier is one identically.
It is nonidentity at completeness and nearby, so it is parabolic.
Its commuting peripheral partner is a translation too. ALL main cusp
groups remain parabolic, whatever the number of main components.

## 6. Original primitive auxiliary curves and absolute action

The auxiliary collar lies in its original leaf box. Its two shaded
triangles and apex are untouched by the port attachments. Therefore the
same actual disk-framed curves apply before and after a turn or closure;
transport to world coordinates conjugates their entire words and does
not change their integral marking.

Put

    rho=Z/(1+E-Z), Q=(E-Z)/(Z-1).

The disk longitude is W2^-1 W0, with flag-at-infinity multiplier Q².
The pure meridian S^-1 has multiplier rho. The two actual odd primitive
meridians A^-1 W0 and W0^-1 B have multipliers rho Q and rho/Q.
Their complete translations are -2 and 2E and the longitude translation
is -2(E+1); the two-rectangle lattice proves primitivity. The original
negative coupon R^-1 uses the first path and R the second. This sign
is fixed by the local typed threading loop [2,1,1,2] followed by R^-1:
its actual auxiliary matrix is I-(P+I)/(1+E), Tr P=-2, with preferred
PSL longitude -P and translation ratio 1+E. This local word identity
is independent of any surrounding grammar. The literal original leaf
frame is retained after a turn; one does not change epsilon by renaming
an exposed port.

By (7), rho=exp(-2pi i t), Q=exp(-v). The actual centered similarity logs
are therefore

    U_i=-2pi i t_i-epsilon_i V_i/2=-2pi i chi_i,
    V_i=-2v_i=-2 partial_i Phi_epsilon.                  (14)

These are squared-eigenvalue logs with the original SL/pivot choices
retained in the finite source. The half-longitude shear compares the
actual two primitive cusp bases; it is not an integral half-longitude
curve in either basis and not a replacement by pure-link rational filling.

Let G=2pi i Phi_epsilon. Then, on this SAME connected marked family,

    dG=(1/2)sum_i V_i dU_i,
    G_epsilon-G_pure=-sum_i epsilon_i V_i²/8
          (with hidden pure colors and stationary wires retained),
    Im G(0)=Vol(Y_E^epsilon)=2pi Phi_epsilon(0).          (15)

The original ideal-chain Bloch differential, with all internal faces
cancelled and each primitive torus retaining its -2 eigenlog wedge,
gives

    d Vol(rho)=(1/2)sum_i[Re V_i dIm U_i-Re U_i dIm V_i].

The complete anchor and (15) therefore give the ABSOLUTE identity

    Vol(rho_chi)=Im G(chi)
                    -(1/2)sum_i Re U_i Im V_i.          (16)

The regulator is attached to the actual original fundamental class,
not to an unrelated curve with the same differential. Any known real
Cartan constant is retained; the complete imaginary normalization is
fixed by the degree-one geometry.

## 7. Smooth actual long fillings and the local packet scope

The color Hessian follows from (4) and evenness: mixed wire/color
first derivatives vanish at zero, so no wire Schur term is present.
With c_i=cot(pi a_i)>0,

    Phi_ij(0)=-2pi c_i/(1-epsilon_i i c_i) delta_ij
             =2pi i tau_i delta_ij,
    tau_i=i c_i/(1-epsilon_i i c_i), Im tau_i>0.          (17)

For any chosen subset of auxiliary cusps keep chi_i=0 at the others.
Separate evenness makes their V_i=0, so they remain parabolic. For the
filled subset choose independently signed integers p_i and impose

    U_i+p_i V_i=-2pi i.                                 (18)

Writing r_i=1/p_i, the equations V_i+r_i U_i=-2pi i r_i have at r=0
invertible chi-Jacobian -4pi i diag(tau_i). The implicit-function theorem
therefore gives the selected solution in a fixed reciprocal-slope
polydisk, without any comparability condition on the slopes.

Apply the proved original framed completion interface, now printed in
`manuscript/sections/D-marked-cell-calibration.tex`, section 4 (equivalently
`notes/general_source_regulator_hyperbolic_equality.md`). Its hypotheses
are all present: actual representation near oriented complete holonomy,
actual selected flags, primitive small logs, and parabolic unfilled cusps.
The proof constructs a positive local metric on the compact core and
ends, proves the actual small-log link periods before multiplying by
p_i, and fills the punctured tube by ONE angular turn. It gives a smooth
complete finite-volume metric on the original topology obtained by the
specified disk fillings. The physical crossing power is
R^(epsilon_i-2p_i), once. A knot cusp, when present, is never filled.

At this saddle the absolute identity (16) is

    Vol(Y_E^epsilon(p))
      =2pi Re[Phi_epsilon(chi_*)
          +(pi i/2)sum_filled_i (chi_i-1)²/p_i].         (19)

This geometric theorem is unconditional for every fixed strict syntax
and sign pattern. If all auxiliaries are filled and its literal main
pairing has one component, the right side is the volume of the resulting
KNOT COMPLEMENT. No isotopy to a completed-root expression is asserted.

For clarity, a one-main-component pattern exists for every literal tree.
For cyclic terminals (0,1,2,3), write I=(03)(12), U=(01)(23), X=(02)(13).
A bare leaf offers the two loop-free pairings {U,X}; a turn exchanges
I,U and fixes X. The original ordered product table is

             I       U                  X
    I        I       U                  X
    U        U       U + internal loop  U
    X        X       U                  I.

There is only one forbidden choice, U*U. To check the induction without
a hidden combinatorial claim, let A={I,U}, B={I,X}, C={U,X}. The allowed
output sets for AA,AB,AC,BB,BC,CC are respectively A,{I,U,X},C,B,
{I,U,X},A; reversed orders give the same sets. Every result contains
two pairings. A larger set contains one of these subsets. Induction
therefore gives at least two loop-free choices at every node. At the
cylindrical root at least one of U,X is available and closes to one
main component. Full twists preserve endpoint permutation. This is a
finite pairing argument, not an invariant-limit argument.

### Exact local packet for the enlarged syntax

Let H be the number of literal leaves. Before the final complementary
relation there are H leaf indices and H-2 retained product-output
indices. The forced last product has coefficient exactly one and
removes one wire by a relation with coefficient +1 or -1. The free
integer lattice is therefore primitive with K=2H-3 coordinates.
This is still true when a root child is a bare or turned leaf: its
root relation eliminates that leaf index or one child output with a
unit pivot. All turns are the original integer map r->d-r, d=N-1.
Thus in primitive coordinates k in Z^K every wire is

    r_w=N L_w(k/N)+delta_w,

where L_w is the actual affine wire map and delta_w is the original
fixed integer offset. No half-lattice or index multiplicity is introduced.
The strict optimizer has an every-level bounded-distance rounding.

Choose a small fixed rectangular window B around the complete optimizer.
Every retained gate is strictly inside its original Newton support on
a neighborhood of B. By (3), for each complete leaf choose either a
fixed high interval or the proved fixed quarter-index neighborhood;
then shrink B to lie in all those coordinate neighborhoods. Choose a
fixed sufficiently small complex physical-color polydisk. Let ell_N^e
be the original exact continued finite core coefficient after extracting
only its known constant unit chirp; its continuation uses the canonical
two shifted factorials, not a free solution of the recurrence. Define

    C_N(chi)=sum_(k/N in B)
       product_i ell_N^(epsilon_i)(r_i,chi_i)
       product_g mu_N(r_g1,r_g2,r_g3).                   (20a)

The mu_N are the EXACT seven-factorial Newton gate coefficients.
This is a finite, separately even holomorphic function. Its support is
fixed before complex colors. At every physical sufficiently small
color deficit, it is the original core window with its original normal
directions; each r_i is uniformly positive and exceeds the small deficit.
The product of the extracted constant unit phases is eta_N.

For each leaf the high or quarter theorem supplies a specified
holomorphic index interpolant with exponentially small relative error
on the physical grid, uniformly in the complex color polydisk. Their
exponential constants may differ; take the minimum over finitely many
leaves. Interpolate each gate by the canonical factorial expression,
which agrees exactly on its grid. Before ANY oscillatory summation,
the sum of all leaf residuals is bounded absolutely by

    poly(N) exp{N[F0+C||chi||²-c]}, c>0.                 (20b)

Indeed the complete local phase has maximum F0 on B, its even color
perturbation is O(||chi||²), and the number of states is polynomial.
Shrink the fixed color disk so (20b) is strictly below the selected
nearby critical action. The residual cannot hide a contour or phase loss.

The interpolated summand has phase A_epsilon(y,chi) from section 3.
Each leaf has leading factor N^(1/2)b_epsilon and each retained gate
N^(-3/2)b_mu, all b holomorphic and nonzero at the complete state.
Consequently the summand is

    N^(3-H) b(y,chi) exp[N A_epsilon(y,chi)](1+O(1/N)).

The density includes, WITHOUT resetting offsets,

    exp[sum_i delta_i partial_x f_epsilon_i
                    +sum_g grad m dot delta_g].

In particular the changed signed f_epsilon, not the pure action,
appears in the offset factor at nonzero color. At completeness the
wire Hessian is negative definite, and its nearby holomorphic critical
branch is y_*(chi).

Apply the exact finite cotangent residue kernel in every primitive
coordinate, choosing rectangular side faces at half-grid positions.
The strict local maximum gives a fixed loss on those side faces. On
horizontal contours of small fixed imaginary height a, every nonconstant
kernel term loses exp(-2pi aN), while the analytic phase costs at most
exp[N(Ca²+C||chi||²)]. First choose a small, then the color disk small;
the horizontal errors and all joining faces are exponentially below
the critical value. The constant kernel term is N^K times the finite
ordinary integral. Shift it to the nearby critical contour and apply
the nondegenerate complex Gaussian estimate. All these contours stay
inside the fixed common leaf/gate interpolation domains.

The primitive measure contributes N^K and the Gaussian N^(-K/2).
Thus 3-H+K/2=3/2. Adding back (20b), only after this cancellation has
been estimated, proves the exact-window asymptotic

    eta_N C_N(chi)=eta_N N^(3/2) a_epsilon(chi)
                   exp[N Phi_epsilon(chi)](1+O(1/N)),
    a_epsilon(0) != 0,                                  (20)

uniformly holomorphically on a fixed smaller color polydisk at both
level parities. The Gaussian determinant branch continues the positive
complete one. Its density is the product of nonzero local amplitudes
and the actual offset exponential, so it cannot vanish at completeness.
Separate evenness gives A_(y chi_i)(y,0)=0; hence the color Hessian is
exactly (17), with no wire Schur correction. In particular the exact
finite window has the usual bound poly(N) exp[N(F0-a||Re chi||²+
B||Im chi||²)] on a smaller box, for some a>0.

### What the quarter theorem now gives globally for the all-core sector

The local packet alone is not a whole-source theorem. There is, however,
a further all-core conclusion for H>=3, and for every two-leaf KNOT
pattern. This does not estimate any nonempty alias sector.

Write V(alpha,beta,gamma) for the actual ideal-tetrahedron
volume with alpha+beta+gamma=1. On its strict angle triangle its Hessian
in two free angles is negative definite: apart from a positive constant
its negative has diagonal entries cot(pi alpha)+cot(pi gamma),
cot(pi beta)+cot(pi gamma), off-diagonal cot(pi gamma), and determinant
one. The diagonal entries are positive by the sine addition formula.
Put p=z−x, q=z−y, r=x+y−z, w=1−x−y. The exact THREE-atom gate identity is

    pi*m(x,y,z)=V(y,x,w)+V(p,q,1−p−q)+V(p+q,r,r+w).

Consequently its Hessian is negative definite in the three variables:
a null vector of the first summand has delta x=delta y=0, and then the
second summand forces delta z=0. The third summand is concave and can
only strengthen this conclusion. All tetrahedron angles are positive
at a strict gate. On the whole closed gate polytope m is concave.

For H>=3 the retained gate-label maps jointly have zero kernel on the
primitive wire tangent space. Indeed every leaf or internal-output wire
is incident to a retained gate, except possibly a bare/turned root leaf.
If all retained gate input/output displacements vanish, all their
incident leaf and wire displacements vanish, while the complementary
root relation pins that sole exceptional root leaf too. Turns only
change signs of those displacements. Hence the sum of gate Hessians
is negative definite on the full primitive tangent space at the strict
complete point.

Use g for every pure leaf and tilde g(x)=g(max(x,1/4)) for a signed core.
These are concave and C1; at every complete a>=1/4 their value and
first derivative agree with g. The all-core majorant therefore has the
same stationary point and value F0 as the complete action. Concavity
makes that point a global maximum; the negative definite gate part
makes it a strict local maximum. A second global maximum would give a
constant segment through this neighborhood, impossible. Compactness
thus gives a strict all-core state gap outside the chosen window.
The uniform closed coefficient upper estimate absorbs its o(N) error
into that gap. Inside the window every leaf index is bounded above by
some beta<1/2, so the existing all-color recurrence estimate supplies
a strict far-color loss, including quarter leaves. Thus the ALL-CORE
sector has the required global physical-color and state control.

For H=2 the only strict root types are LH. Up to the literal turns its
root relation identifies the two original leaf indices. If at least one
leaf is pure, the sharper envelope g+tilde g (or 2g) has a unique strict
quarter maximum and gives the same conclusion. If BOTH leaves are odd,
the majorant is 2 tilde g(a), flat on [0,1/4], whereas the actual complete
action 2g(a) has unique maximum at 1/4. This is a real limitation of this
majorant argument for that two-leaf LINK. It is not a knot pattern:
both odd leaves have pairing X, turns fix X, and X*X=I closes to two
main components. It is not a counterexample to a sharper source bound.

For every strict KNOT pattern, therefore, only the nonempty alias sectors
remain to be uniformly bounded below F0 in order to use the existing
whole-source transfer. That transfer retains the original currents,
charges, parity and nonzero coefficient, and would identify (19) with
the original invariant's full-sequence rate. No general alias gap is
proved by the masked geometry, port rigidity, or the core argument.
No universal volume-conjecture theorem for all arborescent knots is
claimed here.

## Dependencies and review status

Exact complete masks, corner/edge incidence, original cut and strict
positive optimizer: `notes/actual_conway_general_strict_mask_geometry.md`.
Exact interval compiler, primitive lattice and original affine offsets:
`notes/actual_conway_single_leaf_source_composition.md`.
Generic nine prism, turn and closing matrices:
`notes/actual_conway_marked_peripheral_deformation.md`.
Actual odd words, local threading sign, source shear and absolute primitive:
`notes/actual_odd_conway_marked_peripheral_deformation.md`.
High/quarter finite-source interpolation:
`notes/actual_odd_conway_complex_color_packet.md`,
`notes/actual_conway_quarter_index_color_packet.md`.
General metric completion and whole-source conditional transfer:
`notes/general_source_regulator_hyperbolic_equality.md`,
`notes/general_original_source_long_filling_transfer.md`.

New assertions requiring independent review are principally the exact
masked WHITE-map induction in section 4, its use at arbitrary root masks
in sections 5-6, the general quarter-index proposition in section 2, and the final
retained-gate rank argument for the all-core gap.
All generic rational identities themselves are the existing independently
verified identities; no new sampled calculation is used.
