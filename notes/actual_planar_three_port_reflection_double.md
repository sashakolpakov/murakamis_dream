# An exact positive full-source formula for planar three-port doubles

30 October 2026. A literal planar three-port double has an exact
nonnegative complete-circle source at EVERY quantum level. All interior
and seam colors are summed; there are no fixed Steinberg cycle
projections. The formula is a sum of squared COHERENT boundary packets,
with the positive original marked theta scalar as its prescribed weight.
It retains the single physical mark and every paired circle normal.

The primitive half can have arbitrary fixed size and branching. Its
boundary packet is still a genuine coherent contraction, not a product
of local black scalar magnitudes. Thus this theorem removes cancellation
between the double's boundary sectors; it does not yet compute their
exponential size or prove the volume limit for arbitrary plats.

## 1. A reflection operation on the whole original Morse word

Let J_n reverse ALL n physical V_N tensor factors. For a matrix
F:V_N^tensor a -> V_N^tensor b put

    F^sharp = J_a F^dagger J_b.                              (1)

This reverses composition and tensor order. It is a whole-word
operation, not a partial transpose of one leg. Set d=N-1,
q=exp(pi i/N), x=q^d. For the original physical cup and cap,

    p_(u,v)=N x^-v delta_(u+v,d),
    ell_(u,v)=x^u delta_(u+v,d)/N,

one has exactly

    p^sharp=N^2 ell,        ell^sharp=N^-2 p.                (2)

Indeed p^dagger P=N^2 ell, with P=J_2. The original unrestricted
marked row is m_(u,v)=x^v/N^2; it is NOT replaced by its local adjoint
in this argument.

Let L_j be a FULL complete-circle Hermite sector. Its actual
all-degree factorization, including a paired root normal, is

    L_j=F_j F_j^dagger P.

Consequently

    L_j^sharp=L_j,
    (R^e L_j)^sharp=R^-e L_j.                               (3)

For the second identity use the proved all-input equality
R^e L_j=omega_j^e L_j with |omega_j|=1. If a structural crossing
is present elsewhere in the original word, it obeys the independently
proved identity P R^dagger P=R^-1 as well. These are actual matrix
identities, including both parities; a paired nilpotent is not being
replaced by a projector.

In a Morse word from a physical one-head cut back to that head,
the numbers of cups and caps are equal. Therefore every scale N^2
in (2) cancels globally. The word obtained by reversing its composition
and tensor order, exchanging its cups/caps, and reversing its signed
crossings is exactly T^sharp=T^dagger. It is the literal reflected
Morse diagram. Boundary labels are transported by that same geometric
reflection, including its reversal of the cyclic three-port order.

The cut word T is a Hopf endomorphism of the original V_N. This
module is irreducible: its interior E and F coefficients are all
nonzero and its K weights are distinct. Hence T=z I. The original
marked closure extracts precisely z, since m p=1. Its reflected
one-head cut is z-bar I, so

    Z_reflected(reflected boundary labels)
                         =conjugate(Z_original(boundary labels)). (4)

This proves the marked identity without reflecting a bare local m,
without moving a bare mark through a nested cap, and without first
specializing an ordinary quantum trace to zero. A correct generic
first-normal trace quotient gives the same scalar, but is not needed
to establish (4). Any original exterior framing line is reflected
and conjugated separately.

Legitimate one-head cuts on another physical main arc give the same
raw scalar when needed in the seam construction. To verify this,
choose the regular generic lift of the WHOLE labeled diagram. Its
closed scalar F(zeta) equals D_N(zeta) times the open scalar at either
cut, where D_N is the same physical V_N quantum dimension. Away from
its isolated zeros those open scalars agree; they are regular and
therefore agree at the root. This transports the complete cut tangle,
not a bare local marked row. The chosen lift is used only to establish
this equality of the actual root coupons.

## 2. The double is a specified physical source

Start with an actual planar complete-circle graph source Gamma and a
specified three-port vertex disk for which its punctured source has
an actual Morse realization. For example take the exposed outer white
vertex of an original NC/Morse graph. Remove that vertex disk, reflect
its remaining planar piece as in section1, and glue the two disk
boundaries in their reversed cyclic order.

The seam has three edges, not six consecutive edge coupons. Install
ONE original complete-circle coupon on each merged edge. Equivalently
remove the old boundary circle coupons before joining the two pieces
and reinstall one on each seam. Signed seam exponents add; reflected
partners cancel there. Reflect every remaining signed crossing in the
second half as required by (3).

Expand the surviving vertices to their actual nested main-strand arcs.
A generic planar height produces the corresponding cups, caps and
turned-circle Morse word. Choose its single physical one-head mark on
an outer-face seam main arc FROM THE START. This construction is the
planar vertex sum Gamma #_3 reflected(Gamma), with its actual source
orientations. It does not assert that the result has the previous
one-row NC edge order, nor insert unrecorded edge permutations or
structural crossings to force such an order.

The [geometric source certificate](actual_planar_three_port_double_topology.md)
records this disk construction, including its six-terminal reversal.
The algebra below uses only its specified physical port joining and
one-circle-per-seam convention. Applying two old root circle coupons
in succession instead would give a different source and is NOT the
double studied here.

## 3. Exact theta division before taking the fixed root normal

Let D_N be the supported folded triples

    0<=a,b,c<=floor((N-1)/2),       a+b+c>=N-1.

Write theta_N(a,b,c)>0 for the RAW original marked theta source with
these three full-circle sectors and no twists. Its positivity and
normalization are proved in the all-channel marked-theta theorem.
Let Z_Gamma(a,b,c) be the original coherent source with these three
boundary sectors fixed and EVERY other complete-circle color summed.
The mark is a legitimate physical cut of the original closed source.

The [three-port source sewing theorem](actual_nc_three_port_source_sewing.md)
has an all-entry local proof. Removing the ordinary boundary invariant
row from the regular generic lift leaves a genuine invariant column

    Y_Gamma(zeta)=alpha_Gamma(zeta) Theta_abc(zeta).

The canonical Theta corner is one, so alpha is the finite open-corner
contraction and is regular BEFORE dividing by a closed theta. The
same argument applies to the literal disk joining in section2: the
punctured source is an actual composition of Hopf morphisms, not a
bare permutation of a six-head array.

For a supported triple the ordinary theta has exactly one root zero.
Its local source scalar is nonzero. The generic cross-multiplied
sewing identity can therefore be divided by its single common quantum
dimension factor BEFORE specializing. The one-circle-per-seam edge
constants and the two removed source scalars give exactly

    Z_sewn(a,b,c)=Z_A(a,b,c) Z_B(a,b,c)/theta_N(a,b,c).       (5)

No paired projector norm or root L_j inverse is used. The retained
first normal is the originally specified one; higher nonzero
coefficients are not selected if it vanishes.

Nontriangles vanish. For unsupported triples the actual product of
three complete circles kills the regular saturated six-head boundary
source before the exterior or the mark acts, by the exposed six-port
pruning theorem. Thus there is no missing marked-white boundary
current in the COMPLETE-circle sum. This is a whole-source statement;
it is not an assertion that an arbitrary open local current vanishes.

At the reflected boundary identify its labels by the actual reversed
cyclic port map. Equation (4) makes its coherent packet the conjugate
of Z_Gamma, while theta is symmetric and positive. Therefore the RAW
original source of the double is exactly

    Z_double = sum_(a,b,c in D_N)
                  |Z_Gamma(a,b,c)|^2/theta_N(a,b,c) >= 0.   (6)

All interior color sums in each factor of (6) are performed coherently.
The sum includes every physical seam triple. Both parity cases and all
paired first normals occur. If D_N is empty the sum and source are zero.
If D_N is nonempty, strict positivity holds exactly when at least one
coherent boundary packet is nonzero. No universal nonvanishing premise
for an unknown primitive piece is added.

## 4. What the positive formula controls quantitatively

Define the actual weighted boundary maximum

    B_N=max_(j in D_N) |Z_Gamma(j)|/sqrt(theta_N(j)).

When the supported set is nonempty,

    B_N^2 <= Z_double <= |D_N| B_N^2,
    |D_N| <= N^3.                                          (7)

Hence whenever the source is nonzero its complete exponential rate is
controlled, with an O(log N/N) error, by the largest COHERENT weighted
boundary packet. This is a full-source estimate, not a norm of one
fixed central channel or an absolute magnetic-state envelope.

Equation (6) does not make the inside of each Z_Gamma a positive
factorial sum. Estimating that coherent packet is still required to
identify (7) with the actual doubled hyperbolic volume. In particular
known projected cube or ladder packets cannot be substituted for the
full Z_Gamma in (6). The double class has arbitrary fixed primitive
size; it is a specified subclass of physical planar sources, not a
proof for every fixed k-bridge skeleton.

## 5. A literal full-color NC cube double

There is an especially direct certificate using the original ordered
cube, with interval black vertex (0,1,2) and outer white vertex
(0,10,11). Its ribbon reflection swaps the color classes and has edge
permutation

    (1 10)(2 11)(4 7)(5 8), with 0,3,6,9 fixed.             (8)

It maps the interval black boundary to the outer white boundary IN
THE DISPLAYED ORDER. The induced rotations at the other vertices
are the genuine pivotal cyclic moves, not plain magnetic-leg swaps.
Insert the reflected cube at that interval by the existing literal
NC graft. The result has fourteen trivalent vertices and twenty-one
complete circles. Its original mark stays exposed in that construction.
Reflecting the signed interior edge exponents by (8) gives exactly (6).

The focused audit computes this TWENTY-ONE-CIRCLE source directly by
full physical magnetic tensors, with all colors already assembled
in each complete L_N coupon. It independently compares the result
to the supported three-color sum in (6), and checks each reflected
boundary packet against the conjugate-root calculation. In particular
none of its cycle colors is frozen to the central channel.

Audit: [whole-word reflection and full physical doubles](../experiments/audit_actual_planar_three_port_reflection_double.py).

The reflection-double identities do not give a full-source volume estimate.

The size estimate for the remaining coherent half-packet is separate from these identities.