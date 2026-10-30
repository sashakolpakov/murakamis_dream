# A common head chart for the original charged Ward currents

30 October 2026. Independently reviewed. This makes the off-diagonal Ward construction
on a specified tensor source explicit before its finite head sums.
The charge-zero and neighboring charge-one bands use one primitive
head lattice. Cutting a spanning tree reduces the proof to the
independent-head identities of the actual tensors. Reclosing the
auxiliary cuts gives explicit difference currents. The original
support cycles and their endpoint differences remain part of the
result; a common affine chart does not make those cycles equal.

## 1. Typed incidence equations and their component obstruction

Fix one channel assignment in the original generic source, including
the full generic channel expansion of every routed R and R inverse.
Keep all small and large partners, scalar denominators, physical turns
and ordinary caps. Intermediate scalar poles are treated meromorphically
before root specialization; to take a finite normal one first clears
their known finite pole order and retains the required higher Taylor
coefficients. No root projector replaces this generic expansion.

Each wire e carries its fixed integral highest weight L_e and an
actual head h_e. At a typed vertex the K equation is

    sum_out h_e-sum_in h_e
                =(sum_out L_e-sum_in L_e)/2.             (1)

These are ordinary signed INCIDENCE equations. A contracted wire is
an output at one end and an input at the other. Cups and caps are
vertices, not an unrecorded change of orientation. Their constants
are respectively L and -L. At W:V_(2a)->V_d tensor V_d the constant
is d-a; the dual has the opposite constant. Thus every constant
in (1) is an integer in the actual source.

Delete the original exposed cut and the routed first-head cut.
For their band delta put the first input/output heads a,a+delta
and the second input/output heads l,l+delta. Let B be the incidence
matrix of the remaining INTERNAL graph. Its equation is

    B h=b(a,l)+delta q.                                 (2)

The signs of q come from the literal four port orientations. They
are opposite unit charges at the two shifted boundary ends; they
are not an assigned independent color. Integer degree conservation
is retained, without reduction modulo N.

Check connectedness after THESE cuts on the actual typed graph.
For a connected graph the only incidence relation is the sum of
its rows, and the source makes the right side of (2) have sum zero.
A spanning tree therefore gives an integer-affine solution for
arbitrary complex a,l,delta. With x the heads on the non-tree edges,

    h=h_*(a,l)+delta w+A x,                             (3)

where h_* and w have zero non-tree coordinates, w is the signed
unit tree path for q, and A is the integral fundamental-cycle basis.
The non-tree rows of A are the identity. All three bands delta=0,1,-1
therefore have the SAME primitive free coordinates x. No division
by a quantum number or passage to an index-N cover occurs.

The internal CURRENT terms also have a specified chart: place the
compensating charge on the auxiliary edge carrying the generator,
instead of on the second actual cut, and use its signed unit tree
path w_e in place of w. Its non-tree coordinates are again zero.
Thus all possible placements have the same h_* and A and differ
only by their recorded integral charge-path offsets. We do not
mistake a charged intermediate tensor for a zero-band density.

For a disconnected graph the exact criterion is zero total charge
in EACH component. Components containing neither cut are retained
as their original scalar factors. If a charged right side fails
the component criterion, its affine band has no original states;
one must not invent a path joining those components. If the component
conditions constrain a,l, keep those original affine strata rather
than asserting a two-dimensional chart. On a geometric two-position
chart the required connected deleted graph is the explicit criterion
in the [two-cut construction](actual_two_cut_framing_port_reconstruction.md).
For a chosen route U the graph is checked after its actual expansion;
connectedness of a different uncut diagram is not a substitute.

The physical inequalities 0<=h_e<=L_e remain separate from (3).
In particular a dimension-one channel can give a thin or empty
physical support even though the incidence graph is connected.

## 2. The specified meromorphic bands and local identities

Use the actual large finite white polynomial and the specified
moving-period factorial, with d and every L_e fixed as zeta varies.
The independent-head W identities, proved in
[the source Ward calculation](actual_augmented_plat_framing_density_source_ward.md),
are polynomial identities, not equalities only on root samples.
Its cup/cap equations follow from the same exact unit-step factorial
recurrence. They apply meromorphically also to fixed L_e>=N: the
finite scalar factorial can then have a root zero and its pole is
retained as just specified. Integer-affine source characters are
kept; their unit-step multipliers are the actual recorded ones.

One may instead keep an original R as a four-port vertex only when
using its specified literal factorial continuation. Its exact
independent-variable Ward ratios are those of the
[original crossing currents](local_r_ward_transfer_currents.md).
This is a second permitted primitive presentation, not an assertion
that two different off-grid presentations coincide merely because
their physical matrices agree. The full spectral W/cup presentation
above already suffices for the routed source.

In (3), let s_delta(a,l,x) be the product of these actual factors
with the indicated band charge, BEFORE applying the exposed coherent
or root functional. It includes the fixed scalar, turn and peripheral
characters of that convention; any extra generic boundary row must
be separately specified and transported covariantly. No bare root
mark is moved through this generic calculation. On the
allowed physical lattice its original finite period is the actual
coefficient of C(E_(l+delta,l)) from first input a to output a+delta.
The zero band gives J_(a,l).

For the next displayed interior identity use UNTRUNCATED analytic
coefficients

    f(y)=1-Q^(y+1),
    k(y)=zeta^(d-2y),
    gamma(y)=zeta[Q^(y-N)-1]=e(y)/k(y).                 (4)

For example f(d)=1-Q^N here, whereas the finite matrix arrow f_d
is zero. The distinction is indispensable at a genuine quantum
normal. The physical endpoint will be restored by its source cycle,
not by substituting a root simplification in (4).

## 3. The tree construction of the common difference currents

In addition to the two actual cuts, cut each non-tree edge of the
internal graph. What remains is a typed TREE with auxiliary pairs
of boundary heads. Its internal heads are uniquely determined by
its boundary heads and (1). Its tensor entry is consequently a
literal product of the specified factors, with no internal head
sum. Propagating the original Hopf generator through this tree
using the local identities proves its meromorphic Ward identity.
Every coproduct prefix K factor and every ordered dual map stays
in that propagation.

Now identify the two auxiliary heads of edge e with its common
coordinate x_e, using the original identity contraction. The two
insertions on this cut give a discrete product rule. With their
ACTUAL coefficient and tensor factors denoted j,c, it is

    j T_e c-(T_e^-1 j)c
                         =(T_e-I)[(T_e^-1 j)c],         (5)

where T_e shifts x_e by one. The shift acts on the WHOLE indicated
product, including its insertion and all prefix characters. A reverse
shift is put in this form by
(T_e^-1-I)u=-(T_e-I)T_e^-1 u. These are actual array translations,
not new single-port matrix actions.

This specifies the current algorithm: cut the stated tree, propagate
the original generator in its original tensor order, and for each
auxiliary cut collect the literal product on the right of (5), with
its sign. Tree edges cancel pointwise. Each non-tree edge gives its
own current j_(F,e) or j_(E,e). Equivalently the charge paths for the
two placements of its insertion differ by exactly its fundamental
cycle, which is x_e->x_e+1 in (3). This proves that the construction
uses the same head chart, rather than silently comparing different
charge lattices. The currents are finite sums of specified source
products and shifts, not solutions chosen by interpolation.

At the two remaining cuts the result is the explicit interior
band identity

    f(l)s_+(a,l,x)-f(l-1)s_+(a,l-1,x)
       -f(a)[s_0(a,l,x)-s_0(a+1,l,x)]
                         =sum_e (T_e-I)j_(F,e),        (6)

    gamma(l)s_-(a,l,x)-gamma(l+1)s_-(a,l+1,x)
       -gamma(a)[s_0(a,l,x)-s_0(a-1,l,x)]
                         =sum_e (T_e-I)j_(E,e).        (7)

The boundary head changes do not shift x: the latter are the
literal heads of the fixed internal non-tree edges. All tree heads
do change by their exact affine formulas in (3). Equations (6),(7)
are meromorphic identities in independent complex a,l,x and generic
zeta on every regular source chart, and hence after clearing their
denominators. All genuine quantum derivatives are retained.

Their signs can also be checked directly at the finite matrix
boundary. For a diagonal C(E_ll), ad_F has its (a+1,a) entry
f_a[J_(a,l)-J_(a+1,l)]; C(ad_F E_ll) has the other two terms in
(6). For ad_E the (a-1,a) entry is gamma_a[J_(a,l)-J_(a-1,l)],
and C(ad_E E_ll) has the other two terms in (7). The interior
construction proves these same equations modulo the displayed
actual internal currents BEFORE finite contraction.

## 4. An explicit two-crossing interior current

Here is a source-level calculation with an internal cycle. Let
r(a,b,k) be the literal positive crossing coefficient, sending
(a,b) to (b+k,a-k), and write K(y)=x Q^-y, f(y)=1-Q^(y+1).
Retain its common full Cartan scalar. For two consecutive crossings
take external target c+d=a+b+1 and internal transfer k. Put

    T1=f(a) r(a+1,b,k) r(b+k,a+1-k,c-a-1+k),
    T2=K(a)^-1 f(b) r(a,b+1,k) r(b+1+k,a-k,c-a+k),
    T3=f(c-1) r(a,b,k) r(b+k,a-k,c-a-1+k),
    T4=K(c)^-1 f(d-1) r(a,b,k) r(b+k,a-k,c-a+k).

Then for S_k:k->k+1 the exact independent-head equation is

    T1+T2-T3-T4=(S_k-I)J_F,
    J_F=r(b+k,a-k+1,c-a+k-1)
          *[K(a)^-1 f(b)r(a,b+1,k-1)
                            -f(b+k-1)r(a,b,k-1)].       (8)

Apply the first crossing's literal F identity at k and the second
one at k, keeping the middle insertion. Their shared middle terms
cancel except that the first-head middle insertion is evaluated
at k and k+1. This gives (8) with its displayed sign. It is not
an identity obtained by summing a finite row. The source's proper
ratios verify it rationally in independent Q,x,Q^a,Q^b,Q^c,Q^k.
For the E calculation use c+d=a+b-1 and the actual analytic
e(y)=q^-1[x^-1-Q x Q^-y]. The four boundary terms are

    U1=K(b)e(a)r(a-1,b,k)r(b+k,a-1-k,c-a+k+1),
    U2=e(b)r(a,b-1,k)r(b-1+k,a-k,c-a+k),
    U3=K(d)e(c+1)r(a,b,k)r(b+k,a-k,c-a+k+1),
    U4=e(d+1)r(a,b,k)r(b+k,a-k,c-a+k).

Its exact current is

    U1+U2-U3-U4=(S_k-I)J_E,
    J_E=r(b+k-1,a-k,c-a+k)
          *[K(a-k)e(b+k)r(a,b,k)-e(b)r(a,b-1,k)].       (8a)

The middle first-input insertion now appears at k+1 in the first
local equation and at k in the second. This proves (8a), including
the displayed K prefix and its sign. Both identities keep the same
two original crossing scalars on their two sides.

The coefficients in (8) are interior functions. Its physical finite
support and truncated endpoint arrows must still be retained when
it is summed. In particular a generic f(d) is not set to zero as
a meromorphic function merely because the physical matrix has no
arrow there.

## 5. Original period chains, endpoints and the remaining global step

For every charged band keep its ORIGINAL support polytope in (3)
and its ordered product-cotangent tori Gamma_delta. These supports
are different at neighboring bands and at adjacent a,l. A constant
forbidden polar stratum remains its original zero state. When a
separately proved source-null torus is added, its proof and ordered
residue convention are retained.

Equations (6),(7) may be integrated against any common regular test
cycle. To replace the resulting band periods by the original ones,
keep the differences between each Gamma_delta and that test cycle.
For every internal current its translated-cycle correction is
exactly

    integral_Gamma c w(T_e-I)j
      =integral_Gamma c(T_e^-1 w-w)j
          +integral_(Gamma+e-Gamma)c(T_e^-1 w)j,
    c=product_i pi cot(pi x_i).                         (9)

The source normalization is (2pi i)^(-dim x). A chain filling the
last cycle difference contributes ALL its crossed source residues
and its remaining ends. Coincident cotangent/source poles require
their actual finite parts and complement derivatives. The specified
moving-P factorial and fixed highest weights remain in this process.
No periodicity of the summand identifies the support cycles.

On the original finite arrays the actual endpoint arrows and support
rules recover the already proved
[braided coherent flux](actual_braided_residual_framing_current.md).
Pairing the first head with beta_a requires only its exact finite
sum; no new meromorphic interpolation of beta is used. The first-head
and second-head ends of a selected finite window remain the interval
terms in that theorem. The individual meromorphic continuations of
an outside-head term are not set to zero; its ORIGINAL source cycle
is empty, and transport out of that source domain is accounted for
by these chain differences.

Thus the local meromorphic Ward equation and its actual charged
source lattice are now specified together. This still does not
identify the original cycle with a geometric descending cycle or
compute the coefficient of the framing-diagonal residue. The
stationary pushforward must carry the currents (6),(7) and the
explicit chain differences (9), including all resonant characters
and generic normals. A zero closed finite flux alone cannot make
that relative coefficient nonzero.

The focused [audit](../experiments/audit_actual_matching_graph_common_band_ward_current.py)
and [results](../experiments/actual_matching_graph_common_band_ward_current_results.json)
check the actual expanded two- through five-bridge plat graphs,
including routed inverse pairs and all fixed channel weight types:
92 primitive cycles, 196 integral charge paths, and the disconnected
component test. The two composed currents (8),(8a) are verified
rationally in independent head exponentials. A separate comparison
with the original generic crossing matrices checks 539 value/first-jet
entries, including their full Cartan scalar, and seven nonzero
untruncated endpoint-normal defects. These checks do not establish
equality of the different charged support cycles or a geometric-cycle
coefficient.

Independent validation: the primary and coherent-source readers fully
checked the typed incidence equations, disconnected component criterion,
tree covariance and reclosure currents, boundary signs, complete generic
source coefficients, and separation of interior identities from physical
support cycles. The coherent-source reader freshly replayed the focused
audit and independently rederived the E current (8a). The geometry reader
checked the primitive charge chart, routed-graph connectedness requirement
and endpoint/divisor scope. No equality of charged cycles or nonzero
geometric-period coefficient is included in these reviews.
