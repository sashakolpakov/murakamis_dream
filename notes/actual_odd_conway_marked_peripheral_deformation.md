# Actual mixed peripheral geometry for arbitrary odd/pure Conway patterns

29 October 2026. Every fixed signed odd/pure coupon pattern on a
retained robust Conway factor has an actual marked representation
family realizing its selected mixed-source action. The odd shaded
gluings satisfy their full pointwise edge words away from completeness.
The physical auxiliary meridians and preferred disk longitudes obey

    U_i=-2pi i chi_i,       V_i=-2 partial_i phi(chi).        (1)

The source phase changes by an explicit canonical shear. It is not
the pure packet with the same color variables. In particular the
complete half-twist marking is retained in every filling equation.

This supplies the geometric input for the whole original-source
long-filling transfer. Its analytic source hypotheses must be supplied
by the separately proved odd-coupon gap and complex packet. The
present proof works for arbitrary fixed turn depth, branching and
coupon signs; it is not a cyclic or pretzel-only construction.

## 1. An exact change of the physical color coordinate

Write the pure leaf action as

    g(x,t)=J(2x)-2J(x)-J(x-t)-J(x+t),
    J(a)=integral_0^a Log(2sin(pi u))du,
    v=g_t=Log[sin(pi(x-t))/sin(pi(x+t))].                   (2)

The continued marks are those of the complete positive chamber.
For a coupon epsilon in {0,+1,-1} define the hidden pure parameter
t=t_epsilon(x,chi) and transformed action by

    chi=t-epsilon*v/(2pi i),
    f_epsilon(x,chi)=g(x,t)-epsilon*v^2/(4pi i).            (3)

For epsilon=0 this is simply the original pure leaf. At t=0 the
derivative of the first equation with respect to t is

    1-epsilon*i cot(pi x),

which is nonzero for 0<x<1/2. Thus (3) determines one holomorphic
branch near every complete leaf. The function t is odd in chi;
f_epsilon is even. Direct differentiation, including the implicit
t dependence, gives EXACTLY

    df_epsilon=g_x dx+v dchi.                              (4)

Thus the internal wire derivative remains g_x evaluated at the hidden
parameter, while the derivative in the PHYSICAL color is v.

## 2. This is the action selected by the original odd source

The exact finite mixed half-twist source has the selected analytic
action, for epsilon=-1,

    f_src(x,chi)=g(x,chi)+S(x,pi chi)-S(x,0),
    S(x,a)=integral_x^(1/2) Log mu(s,a)ds,                 (5)

where mu is the source-selected root of the explicit quadratic in
[the mixed finite-source theorem](actual_pretzel_mixed_inner_source_wkb.md),
with mu(x,0)=-exp(-2pi i x). This formula keeps the original q^(h^2)
term: in the normalized physical coefficient its phase cancels
exactly against the two shifted factorial phases, as in that theorem.
No order-N phase has been dropped from (5).

Put E=exp(2pi i x), H=exp(2pi i chi), K=exp(-partial_x f_src).
With D=(1-E/H)(1-EH), the source quadratic and its selected root give

    K=E mu D/(1+E)^2,
    K^2(1+E)^2+K[(H+H^-1)E^2+2]+(1-E)^2=0.              (6)

At H=1 this polynomial factors as

    (K+1)[K(1+E)^2+(1-E)^2].

The SOURCE selects K=tan(pi x)^2, not K=-1. On the fixed high-index
interval x>1/4 its selected eigenvalue is simple; the same regular
branch continues for small complex chi.

Now let T=exp(2pi i t) in (3). Since exp(v)=(E-T)/(ET-1), its
epsilon=-1 equation is

    H=T(E-T)/(ET-1),
    T^2+E(H-1)T-H=0,                                 (7)

with T=1 at H=1. The pure ordered port value is

    K=(E-T)(1-ET)/[T(1+E)^2].                         (8)

Eliminating T between (7),(8) gives precisely (6). Its branch agrees
at H=1, so (4) and the selected source have the same x derivative.
This fixes the derivative, not yet the possible chi-dependent constant.
That constant is fixed at x=1/2: both (5) and (3) tend to zero there,
because S(1/2,a)=0, g(1/2,t)=0 and g_t(1/2,t)=0. Continue the common
high branch to that endpoint. Therefore f_src=f_- EXACTLY on the
selected neighborhood, with the original complete mark retained.

The positive coupon is the Schwarz conjugate of the negative finite
source. Conjugating (3), including i->-i, proves f_src,+ = f_+.
In particular (3) is an identification with the selected finite
source, not a newly proposed definition of its quantum phase.

## 3. Universal port data with either shaded pairing

For arbitrary nearby complex E,R normalize a port to
(0,infinity,1,R). Choose a leaf flag Z satisfying

    Z^2-(1+E)Z+ER=0.                                  (9)

In the first half use apex Z, and in the second half apex Z/E.
For the hidden pure parameter this means

    Z=(1+E)/(1+T),
    R=T(1+E)^2/[E(1+T)^2]=1/(1+K).                   (10)

Use the same four white/completion matrices as in the pure proof:

    W0=[[1,0],[0,E]],
    W1=[[1,E-1],[0,E]],
    W2=[[E-R,R(1-E)],[E-1,1-ER]],
    W3=[[R,0],[1-E,ER]].                             (11)

W0,W2 send Z to Z/E by (9). The pure shaded map is
S=[[0,-ER],[1,-1-E]], pairing the two shaded triangles within one
half. At an odd leaf use instead the ACTUAL cross-half pairings

    (Z,infinity,1) -> (Z/E,R,0),
    (Z,R,0) -> (Z/E,infinity,1),

whose matrices are

    A=[[R,-R],[1,ER-1-E]],
    B=[[R/E-1-1/E,R],[-1,R]].                        (12)

The second is the inverse of the first with E replaced by E^-1
and R retained. Equation (9) checks both apex correspondences.
These are the same local puncture and copy permutations proved by
the literal half-disk rotation in
[the complete half-partner proof](actual_conway_half_twist_partner_geometry.md).
They are not a change of the original main-wire compiler.

Crucially, the three odd edge relations hold for INDEPENDENT E,R:

    W0^-1 B W2^-1 A=identity,
    W2^-1 B W0^-1 A=identity,
    W1^-1 B W3^-1 A=identity.                         (13)

These are rational 2-by-2 matrix identities. No complete relation
R=(1+E)^2/(4E), unit-modulus condition, or equality of edge angles is
needed. The reverse words are their inverses. Thus all odd side and
CAP-base edge words remain pointwise trivial, including translations
and dilations, throughout the mixed deformation.

## 4. Assemble actual representations for the whole grammar

At each leaf use (3),(10), and retain the original multiplication
action m and every actual turn/final closing relation. Let

    F(y,chi)=sum_leaves f_epsilon(x_i(y),chi_i)
                                      +sum_products m.

At zero it is the pure complete action. Its wire Hessian is therefore
negative definite there. The implicit-function theorem gives its one
holomorphic critical branch y_*(chi), and phi(chi)=F(y_*(chi),chi).

By (4), internal stationarity is exactly the old ordered port
cross-ratio matching, with each pure g_x evaluated at its own hidden
t_i. The nine prism transport identities, all turn identities and
the final cylindrical identities from the pure marked-deformation
proof are rational identities, so they continue unchanged. They
supply a SINGLE Mobius map on every original white face, even if
its deformed triangular pieces are not coplanar.

For complex source parameters the construction uses holomorphic
charts: the second prism's coordinates invert its angle phases,
as in the rational transport identities. The normalized port value
R remains the same in its two charts, and the leaf apex pair is
specified directly by (9). No antiholomorphic operation on the
physical parameters is being used. Three-point charts are regular
near the complete anchor; stationarity matches their fourth points.

Use the exact pure shaded words at pure leaves and (13) at odd
leaves. The actual closed bowtie quotient, with the changed local
half-disk pairings, supplies the labeled fundamental-group presentation.
All its face-edge words are now identities. Thus the matrices give
an ACTUAL representation of the original half-twist partner link
group, in a bounded framed neighborhood of its complete holonomy.

The small meridian around a main segment still crosses its two
white sectors and is W_(j-1)^-1 Wj at that corner. Their derivatives
at the common flag are equal, so this meridian is exactly parabolic;
it stays nonidentity near completeness. Its peripheral commutant
consists of translations. Therefore ALL main cusps remain parabolic,
including when the changed pairing joins many old main components
into one knot component.

## 5. Exact primitive auxiliary meridians and longitude

Define

    rho=Z/(1+E-Z),       Q=(E-Z)/(Z-1).              (14)

The common longitude is the actual disk path W2^-1 W0. In the
selected flag-at-infinity coordinate its multiplier is Q^2. The
pure meridian is S^-1, with multiplier rho. At the two half-twist
markings the primitive collar paths are

    mu_geometric,+ = A^-1 W0,
    mu_geometric,- = W0^-1 B.

Direct differentiation at the finite flag Z, taking the reciprocal
to get the flag-at-infinity multiplier, gives respectively

    exp(U_plus)=rho Q,
    exp(U_minus)=rho/Q,
    exp(V)=Q^2.                                        (15)

These paths reduce at completeness to the primitive translations
-2 and 2E, while the disk longitude translates by -2(E+1). Their
primitivity and sign were independently checked on the two-rectangle
cusp lattice. Thus (15) retains the original integral collar paths;
it is not an arbitrary choice of eigenvalue square root.

The physical coupon R^-1 uses the geometric positive-diagonal
meridian, and R uses the negative-diagonal meridian. This local sign
can be checked against the literal threading and Hurwitz convention,
without identifying a meridian from a Hessian. Write P for its actual
disk-product SL(2) matrix. At the complete negative coupon, the
source-selected regular local calculation gives

    C=I-(P+I)/(1+E),       Tr P=-2.                    (16)

Here C is the actual auxiliary meridian from the typed loop
[2,1,1,2] followed by R^-1; the preferred PSL longitude is -P.
Consequently its complete translation ratio is lambda/mu=1+E,
exactly the positive-diagonal primitive path above. Formula (16)
and its actual word meaning are proved by the explicit local
threading calculation in
[the regular character lift](actual_pretzel_mixed_regular_character_lift.md),
sections 4--5. They concern one coupon and do not use a cyclic
global pretzel gluing. Reversing the retained half twist changes
the meridian by one disk longitude, giving the other path.

There is also a direct algebraic check against the finite source:
eliminating Z from (9) and rho Q=H^-1 gives exactly (6), with its
selected complete branch. Thus the actual primitive meridian and
the selected physical-color variable agree, beyond the complete
translation calibration.

Using (10),(14), rho=exp(-2pi i t), Q=exp(-v). Hence for the
physical epsilon convention, with all small logs continued from zero,

    U= -2pi i t-epsilon*V/2
      =-2pi i[t-epsilon*v/(2pi i)]=-2pi i chi,
    V=-2v=-2 partial_chi f_epsilon.                   (17)

Equations (15)--(17) are exact on the connected local branch. In
particular the framing correction is a HALF-longitude shear between
different cusp lattices, not an assertion that lambda/2 itself is a
primitive loop in either lattice. The actual integral paths were
fixed before writing their logarithms.

## 6. The full source primitive, regulator and filling equation

The envelope rule in the stationary wires now gives (1) for every
auxiliary component of the whole source. Unfilled auxiliary colors
have chi_i=0. Separate evenness then gives V_i=0 as well, so they
remain parabolic. All main components were treated in section 4.

Put G=2pi i phi, retaining the known real Cartan/framing constant.
Then

    dG=(1/2)sum_i V_i dU_i.                            (18)

Locally the change in the leaf primitive is explicitly

    G_epsilon=G_pure-epsilon*V^2/8.                    (19)

Its derivative is exactly the shear U_new=U_pure-epsilon V/2.
Thus the quadratic framing term required by the odd cusp is PRESENT
in the selected action, rather than appended after a volume comparison.
The original SL(2) pivot spin is retained when taking eigenlogs;
(1),(17) use centered PSL(2) similarity multipliers, the squares of
those eigenvalues, as in the general transfer theorem.

At the complete point Im G(0)=2pi phi(0) is the ACTUAL half-twist
partner volume by the complete geometry theorem. The same oriented
fundamental-chain boundary calculation therefore gives the absolute
regulator identity

    Vol(rho_chi)=Im G-(1/2)sum_i Re U_i Im V_i.         (20)

This uses the actual nearby representation just constructed, its
primitive markings, and its complete geometric anchor. It does not
compare unrelated Bloch cycles by equal regulators.

For independently sufficiently long fixed signed integral full
twists on any chosen auxiliary subset, the original transfer saddle

    phi_i(chi)+(pi i/p_i)(chi_i-1)=0

is precisely U_i+p_i V_i=-2pi i. The unfilled peripheral groups
remain parabolic. The general geometric completion theorem therefore
makes this actual nearby representation the smooth complete
hyperbolic holonomy of the correctly marked filled topology. At its
saddle, (20) equals

    2pi Re[phi(chi)+(pi i/2)sum_i(chi_i-1)^2/p_i].       (21)

This completion uses the ACTUAL ODD-LINK primitive basis. In the
hidden pure variables its equation reads
U_pure+(p_i-epsilon_i/2)V=-2pi i. Multiplying it by two would give
the pure-link primitive pair (2,2p_i-epsilon_i) with right-hand side
-4pi i, not the smooth primitive 2pi equation. Consequently the
half-integer shear must not be replaced by an assertion about ordinary
rational Dehn filling of the pure partner. It relates local marked
representation branches of different face-paired topologies.

Whenever the separately proved odd-source whole-color gap and exact
complex packet supply the analytic transfer hypotheses, (21) is
therefore the FULL original invariant's actual filled hyperbolic
volume limit. For retained C(FG) these are the current source inputs;
the stronger all-color theorem does not include the small C(h^3)
exception merely because the geometric construction also works there.

Finally choose one of the constructive one-main-component patterns
from the complete half-partner theorem and fill all auxiliary circles.
The resulting topology is a KNOT for every integral full-twist tuple.
Thus, with the stated original-source inputs, this geometry applies
to arbitrarily branching long-filled knot families, rather than only
links or a fixed-width twist/pretzel subclass.

Audit: [generic odd transport, actual peripheral flags and selected-source shear](../experiments/audit_actual_odd_conway_marked_peripheral_deformation.py)
and [results](../experiments/actual_odd_conway_marked_peripheral_deformation_results.json).
The finite audit checks the three odd edge words over Q(E,R), both peripheral
commutators, all apex and primitive multiplier formulas, the actual
meridian/source resultants at both signs, and the exact implicit
generating-function derivatives. No complete-R specialization or
numerical phase samples are used.

The odd-link construction uses its own primitive filling equation, not a rational filling of the pure link. The sign calibration uses Y=E in the specified R^-1 convention, and the selected action retains its endpoint constant.