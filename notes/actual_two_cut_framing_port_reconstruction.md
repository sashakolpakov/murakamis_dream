# Two physical cuts reconstruct both framing positions and their port currents

Research construction, 27 October 2026. Two actual edge positions can
be used as integral framing coordinates. Opening those two physical
edges gives a literal four-port tensor whose double diagonal is the
partially summed two-position array. The original source is its
sum divided by N, with no second pivot inserted. The full port
bands retain the actual Hopf currents and their cut co-sources.

For bounded port shifts, proper coefficient ratios and the same
transverse Gaussian give a canonical nonzero LOCAL band-kernel
map. It is linear on the interior current identities; the exact
finite endpoint rows remain separate relative data. It is not a
product-preserving finite-matrix map,
nor a selection of the global framing cycle or its orientation.

## 1. An etale pair of physical edge positions exists integrally

Use the original actual coefficient model, its full marked
peripheral factors, and the regular geometric critical chart of
[the partial support theorem](partial_geometric_support_theorem.md).
At fixed meridian its critical framing torsor has dimension two.
The original cut position a_0 has nonzero differential there.
Every transfer is an integer difference of physical edge
positions, in the actual oriented boundary convention.
Here differentials on the critical chart mean the continuous
logarithmic physical clocks u_e=H a_e; the integer labels specify
their lattice and are not independent continuous functions there.

If every edge differential were a multiple of da_0 on this
two-dimensional tangent space, all transfer differentials would
be multiples of da_0. All independent flow differentials would
then have rank at most one, a contradiction. Thus some other
physical edge e has

    da_0 wedge da_e != 0                            (1.1)

on a dense open subchart. This selects a FIXED edge of the diagram,
not a level-dependent change of state. Shrink to its regular etale
chart and put a=a_0, b=a_e.

There is no hidden lattice index. Let G be the connected closed
four-valent diagram graph, with the actual oriented integer flow
lattice L=ker(incidence). Bivalent bends/cups/caps may be collapsed
after transporting their dual basis labels; their actual frame
matrices and scalar coefficients remain in the tensor network.
The affine relabeling a->N-1-a in a self-dual chart, if used, is
recorded rather than discarded. It does not change L or its index.

For any set S of removed edges, incidence ranks give

    rank(ev_S:L->Z^S)=|S|+1-c(G\S).                 (1.2)

Indeed rank L=E-V+1, and its kernel under evaluation on S is
the cycle lattice of G\S, of rank E-|S|-V+c(G\S).
For S={e_0,e}, (1.1) forces rank two, hence G\S is connected.
Choose a spanning tree disjoint from both edges. Fundamental
cycles of the complementary chords form an integral basis of L,
and their evaluations on these two edges are the two coordinate
vectors, up to the fixed orientation signs. Thus

    (a,b,j_1,...,j_(m-1))                          (1.3)

are unimodular actual flow coordinates. No finite cover or
congruence class is introduced. The actual finite support and
all zero-extension boundary inequalities are transported by this
integer change of variables.
The physical clocks are A=Q^a and B=Q^b. Actual q^a,q^b and
the original half-Cartan root marks are retained in the coefficient
field, as in the partial support theorem. The unimodular argument
introduces no NEW lattice cover and does not erase those existing
lift characters.

## 2. A literal cut tensor, rather than an invented second state

In a braid circuit write the word as A B at a level containing the
selected edge e, on tensor slot t. Let E_bd^(t) be the literal
matrix unit inserted into that wire. Keep the original closure
caps, pivots and framing/peripheral lines in the SAME places.
Let P denote their contraction, leaving the original cut open.
Define the four-port tensor by

    T_(a,b)^(c,d)=[P(A E_bd^(t) B)]_(c,a).          (2.1)

This is an explicit reconstruction using N^2 insertions in the
original network. The inserted matrix unit replaces the identity
on that one edge; no extra color, trace, state, cap or pivot has
been introduced. The same definition works in any cup/cap/plat
diagram: replace that literal wire identity by E_bd and contract
all other original tensors. It is independent of how the finite
contraction is parenthesized.

Since sum_b E_bb=I, re-closing just this identity edge gives

    C_(c,a)=sum_b T_(a,b)^(c,b).                    (2.2)

If the original diagram happens to put a diagonal transport on
this edge, it is retained on its original side in (2.1), or its
known entries are included in T. An independently added g_b
would change (2.2). In particular cutting an ordinary internal
identity edge does NOT authorize a second pivotal trace.

Set

    J_(a,b)=T_(a,b)^(a,b).                         (2.3)

Actual total-index conservation makes the reclosed C diagonal
termwise for the original kernel and all scalar Green moments.
The original cut coupon has diagonal entries 1/N, hence

    original reduced period=(1/N)sum_(a,b) J_(a,b).  (2.4)

This is 1/N, not 1/N^2. Every original pivot, zero-framing line,
meridian lift character, base compact factor and external d_N(M)
remains where it was in (2.1); multiplying (2.4) by the retained
external line gives the original full state.

Equivalently the exact weighted family is

    F(x,y)=(1/N)Tr_cut[
                x^J P(A y^(J_t) B)].              (2.5)

Its coefficient of x^a y^b is J_(a,b)/N. Thus the two-position
array is realized by two physical wire couplings before any
formal completion. It is not only an arbitrary array relabeled
as a matrix.

## 3. Actual Hopf transport through the cut coupon

In a genuine integral q-family use the ordinary cap P_o. At the
original root use the original pivotal cap with its retained
scalar adapter. For any actual h, pivotal Hopf naturality gives
the exact insertion identity

    D_h P_o(A X B)=P_o[A D_h,tot(X) B],             (3.1)

where X is ANY inserted operator at the chosen intermediate level,
and D_h=ad_h-epsilon(h). The words A,B intertwine the respective
actual coproduct representations; their boundary object orders
are not silently identified. For a plat, the same proof uses its
actual intertwiners and duality maps before and after the chosen
wire. Thus (3.1) is valid with all actual cups/caps present.

For X=E_bd^(t), (3.1) is a specified current map from the physical
second cut to the original cut. It contains the TRUE total adjoint,
including its mixed terms; the local coupon is not presumed to
be a tensor-product submodule. For example, in a parallel ordered
tensor object

    E_tot=sum_i E_i K_(i+1)...K_l,
    F_tot=sum_i K_1^(-1)...K_(i-1)^(-1) F_i.

For a local coupon X in slot t, put k_X X=K_t X K_t^(-1) when
X is a weight matrix unit. Then

    D_E,tot(X)=[E_tot,X] K_tot^(-1),
    D_F,tot(X)=F_tot X-k_X^(-1) X F_tot.             (3.2)

The E commutator has its local term
[E_t,X]K_(t+1)...K_l and, for EVERY i<t, the term

    E_i K_(i+1)...K_(t-1) [K_t,X] K_(t+1)...K_l.

The F expression has its local term
K_1^(-1)...K_(t-1)^(-1)(F_tX-k_X^(-1)XF_t),
and the prefix terms
(1-k_X^(-1))X K_1^(-1)...K_(i-1)^(-1)F_i for i<t.
Terms i>t cancel exactly. These are the actual induced
off-diagonal/prefix rows; omitting them amounts to replacing the
true coproduct by a different one. In a dual tensor slot use its
actual contragredient matrices, with the same ordered formula.

If the weighted word or scalar Green insertions occur, (3.1)
has the explicit additional local crossing/weight currents from
[the whole Ward construction](actual_divided_ward_closure_and_green_caps.md).
For the frozen off-root ADO cap add its recorded defect

    R_h=chi^(-1)ptr_K[M_(Z^J),ad_h].                (3.3)

Thus this construction does not assume auxiliary truncated
generic-q/M matrices are genuine Hopf intertwiners. It applies
directly on the original root family or on the genuine integral
q-family, and keeps the actual defect rows on another lift.

## 4. The off-diagonal port bands and the original source

Retain the complete bands

    J^(p,q)_(a,b)=T_(a,b)^(a+p,b+q),               (4.1)

zero outside all four actual port ranges. This is a lossless finite
encoding of T. In a parallel oriented charge convention the
original scalar tensor has p+q=0. A contragredient cut uses its
recorded sign or index reversal, not a new conservation law.

The source on these bands is essential. With the original cut
row e_0, (2.2) gives on EVERY current tensor

    Phi^(2)(T)=sum_(a,b,p) (e_0)_(a,a+p)
                                             J^(p,0)_(a,b).    (4.2)

In the original balanced source e_0 has every entry 1/N. Thus a
homogeneous current of cut degree d uses its p=d band with the
same factor 1/N. Only a charge-zero scalar kernel reduces to
(2.4). Applying the J^(0,0) source to all Hopf currents would
delete precisely the original off-diagonal cut co-sources.

For illustration the first output/input port actions are exactly

    (L_A T)^(p,q)_(a,b)
       =sum_r A_(a+p,a+r) J^(r,q)_(a,b),
    (R_B T)^(p,q)_(a,b)
       =sum_s B_(a+s,a) J^(p-s,q)_(a+s,b).          (4.3)

The second-port formulas interchange a,p with b,q. Substituting
the actual E,F,K, antipodes or dual matrices gives every shifted
band and its endpoint coefficient. The
[independent band-current audit](two_cut_port_band_current_audit.md)
records these rows explicitly. All divided rows are obtained with
the full actual coproduct, not by raising a projected scalar row.

The grouped array matrix has ROW=a and COLUMN=b. It is not the
ordinary matrix of a one-cut tangle. Even the actual two-cut
unknot has T_(a,b)^(c,d)=delta_(c,b)delta_(d,a), so J=I. Then
the double diagonal of (E tensor I)T is zero, whereas EJ=E is
nonzero. Thus a single physical Hopf port action does NOT descend
to ordinary left multiplication on J. Actual boundary reordering
may also require braidings or dualities. Those matrices, and their
transported coproduct order, must be kept rather than assigning
the grouped T a naive Delta action.

There is nevertheless an explicit scalar-coordinate lift. For
matrix units define the balanced port channel

    L_ij(T)=(E_ij tensor I)T(E_ji tensor I).

Its double diagonal is E_ij J. On the second port the channel
(I tensor E_ji)T(I tensor E_ij) has double diagonal J E_ij.
These formulas produce exact row and column position shifts and
clocks. Their matrix-algebra unit on the full tensor space is a
diagonal projection, not its identity. A physical crossing can
leave that projection and return through an exchange band, so
these channels are NOT a product-preserving replacement of the
whole R network.

The [two-coordinate Green/coherent construction](two_cut_matrix_green_and_coherent_source.md)
supplies the full left/right Toeplitz shifts with both row/column
tails and their corner. Apply its relative endpoint construction
bandwise to the actual allowed windows in (4.1). No tail created
by a Green translation is folded back into a physical port.

## 5. A canonical nonzero local Gaussian map for bounded bands

This physical opening supplies more than scalar coordinate names.
Remove both cut edges. The remaining internal graph is connected.
Prescribing port shifts p,q with the balanced total charge gives
an integer boundary-divergence vector of total zero. The incidence
matrix of the chosen spanning tree solves it integrally: the flow
on an oriented tree edge is the signed sum of divergences in its
child subtree. All internal chord flows remain free.

Consequently each fixed band has actual coefficients

    I^(p,q)(a,b,j), j in Z^(m-1),

on an affine integral flow coset, with the same free chords as
I^(0,0). Relative to the latter parametrization, every local edge
position and crossing transfer changes by an integer constant,
bounded in terms of the diagram and |p|+|q|. Actual proper
factorial/Cartan ratios therefore give, on the strict interior,

    I^(p,q)=R_(p,q)(q,M,clocks) I^(0,0).            (5.1)

This is an identity derived from the original coefficients.
R_(p,q) is a finite product of the recorded rational shift ratios
and meridian/lift monomials. Every common base-only Cartan,
compact-factor and peripheral line remains common; it is not
reset to a numerical ideal value. On the regular geometric chart,
the variable shape arguments avoid 0 and 1, so for FIXED bounded
port shifts its leading coefficient is a unit. The strict-support
cone remains nonempty for all large N after such a fixed shift.
Equation (5.1) is an INTERIOR identity; its finite zero-extension
endpoint rows remain their separate relative data.

Because (a,b) is etale on the critical torsor, the remaining
m-1 Hessian is nondegenerate. Let G_(a,b) be the original
transverse Gaussian and define

    Z^(p,q)=G_(a,b)[R_(p,q) I^(0,0)].              (5.2)

This has the same marked action/base line as Z^(0,0), and its
leading amplitude is R_(p,q)|_crit times the nonzero amplitude
of Z^(0,0). In particular it is nonzero on the stated chart.

The construction is independent of the integral particular-flow
choice. Two choices differ by a cycle supported entirely in the
internal graph, hence by an integer translation of the transverse
chords. The exact formal Gaussian translation identity, with its
correspondingly shifted insertion and critical point, identifies
the two formulas when these choices are fixed independently of N
(or differ by uniformly bounded shifts). Adding an N-dependent
full cycle is a finite logarithmic-deck move and also requires
transport of its separate flattening/period mark. A different
fixed unimodular chord basis changes only
the actual recorded orientation/half-density frame. This is a
canonical LOCAL band-kernel after those original marks are fixed.

Every bounded ordinary port Ward row in Sections 3--4 is a finite
linear combination of shifts and insertions in these same actual
affine arrays. Formula (5.2), with the exact opposite shift on
its insertion, is consequently a linear COCHAIN pushforward of
their INTERIOR current identities. The exact finite support and
framing endpoints stay in the explicitly recorded relative summand;
this assertion does not evaluate their geometric images. This is
the translation-covariant Wick formula of
[the residual-current theorem](residual_gaussian_ward_currents.md),
now with BOTH external coordinates represented by physical cuts.
The principal B1 fields project independently to (a,b) by (1.1).
Their scalar position directions therefore have the left/right
array realization above; their complete Hopf rows retain the
off-diagonal and prefix data of (3.2)--(4.3).

This is not an identification of a finite fixed-N matrix algebra
with a scalar function algebra. It is a linear map on an actual
local coefficient/current completion. It also makes no claim for
port shifts growing like N, for summing all such bands, or for
the behavior at the two external finite-window boundaries.

## 6. The nearest actual bands measure the physical wave momentum

Their principal ratio can be computed without guessing an extra
source. Use the ACTUAL balanced/factorial boundary frame. The
crossing generating functions satisfy

    dS_vertex=sum_out Log(p_new) du
                                -sum_in Log(p_new) du.         (6.1)

This follows from the exact generating relations already derived
from the actual crossing ratios in
[the marked holonomy calculation](marked_braid_holonomy.md), with
the canonical boundary form in
[the determinant-line proof](quantum_source_bridge_extension.md).
The actual diagonal factorial frame change adds its output-minus-
input boundary primitive; accordingly its momentum is
p_new=(1-A)p_old. Using p_old in (6.1) while keeping the new
constant source would change the band marks.

Sum (6.1) over the open network at its original geometric critical
point. All internal edge terms cancel by momentum continuity.
The only boundary terms are

    Log p_(0,out) du_(0,out)+Log p_(e,out) du_(e,out)
      -Log p_(0,in) du_(0,in)-Log p_(e,in) du_(e,in). (6.2)

The original cut has p_(0,in)=p_(0,out)=1. At the second identity
edge p_(e,in)=p_(e,out)=p_e. The original closed pivotal phases
can add 2pi i integer multiples to the logarithmic momenta. Their
exponentiated multipliers are one; their finite coefficients and
flattening/period marks remain retained in the exact ratios.

In the band J^(p,q), the inputs a,b are held fixed and the
outputs are a+p,b+q. Hence the first action change is

    (S_(p,q)-S_0)/H=p Log p_(0,out)+q Log p_(e,out)+O(H).

The integral tree particular flow makes no additional term:
its internal contributions cancel in (6.2). The shifted regular
amplitude tends to the original amplitude. Thus the ratio in
(5.1) has the EXACT marked principal symbol

    R_(p,q),0=p_cut^p p_e^q.

For the nearest charge-zero exchange bands this gives

    R_(+1,-1),0=p_e^(-1),
    R_(-1,+1),0=p_e.                              (6.3)

These are the ACTUAL local edge wave momenta in the physical
Gauss matrix. If a developed Wirtinger meridian is written in a
common global frame, its prefix conjugation must be retained:
that matrix is not silently identified with the local Gauss
matrix solely because both are meridians.

There is a useful precise parity consequence on a physical
two-parabolic chart. Suppose the matrices in the same ACTUAL
physical cut frame are as follows, with Tr(g_cut g_e) a FIXED
representation invariant on that framing chart:

    g_cut=[[1+s,-s],[s,1-s]],
    g_e=[[k,(1-k)p_e],[(k-1)/p_e,2-k]].

Put z=s(k-1), c=Tr(g_cut g_e)-2 and

    c=z(2-p_e-p_e^(-1)),
    D=-z(p_e-p_e^(-1)).

The two branches at fixed position clocks exchange p_e and its
inverse. On the regular chart z!=0,p_e!=0, (6.3) therefore proves

    R_(+1,-1),0-R_(-1,+1),0=D/z.                 (6.4)

The principal ODD orientation section is realized by two actual
nearby port bands. It was not imposed by a field trace or by a
postulated Weyl action. If the two-position density is
Omega_cut=dlog A wedge dlog B/(B D), its product with this
actual odd-band symbol is the nonzero DECK-EVEN density

    dlog A wedge dlog B/(B z).                   (6.5)

Equations (6.4)--(6.5) require the displayed physical Gauss chart
(including any prefix adapter); they are not a replacement of
that dictionary for an arbitrary pair of developed word matrices.

## 7. The remaining orientation and global-source datum

An etale two-position chart need not have degree one. On a
two-sheeted framing chart its leading density can be odd under
the deck involution. The local choice of geometric critical point
and marked square-root/orientation in (5.2) then selects a local
sheet; ordinary field trace of that odd density would be zero.
The literal source (4.2) and full relative finite-window tails do
not authorize replacing a selected cycle by that field trace.

Section 6 now computes an actual local odd-band observable that
distinguishes those sheets, when the physical chart is fixed.
However the original second-edge closing operation is the q=0
identity-cap source (4.2). It has not been proved that its global
relative current/cycle selects the odd combination in (6.4).
Substituting that inserted observable for the uninserted scalar
state would be a different problem. The construction supplies a
specified physical current/source problem, a nonzero local band
map and two independent position directions. It does not yet
determine the global marked cycle or prove that its geometric
coefficient survives the final contraction.

Exact actual tensor audits: [script](../experiments/audit_actual_two_cut_ports.py)
and [results](../experiments/actual_two_cut_ports_results.json).
