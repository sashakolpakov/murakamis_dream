# The actual quantum source at every bridge

Research note, 27 October 2026. This continues the
[arbitrary-bridge classical contraction](arbitrary_bridge_source_reduction.md)
using the original finite quantum matrices. It computes all four
balanced turns, a literal marked closure, their cyclic boundary
sources and a flat completion under the actual meridian half-step.
All formulas hold for arbitrary N and arbitrary bridge count.

The completion needs two bulk channels: a single cap's bulk norm
changes sign under the half-step. Keeping only the squared step
would miss this. The explicit three-dimensional system below keeps
that sign and the boundary source, including at the Kashaev color.
This is finite quantum boundary transport. The selected knot
period's comparison with the geometric regulator remains unproved.

## 1. The original caps lose their factorials exactly

Fix q=exp(pi i/N), Q=q^2, N>=2 and x=-M/q. Write
F_a=(Q;Q)_a and w_a=v_a/F_a, both on V(x) and its standard dual
color V(x^(-1)Q^(-1)). No unrolled weight lift is changed.
The existing actual turn matrices have

    c_a=(-x)^a Q^(a(a+1)/2),
    g_b=x^(1-N) Q^(-b).                                  (1.1)

For 0<=a<N, cancellation in the full product F_(N-1)=N gives

    F_a F_(N-1-a)=N (-1)^a Q^(a(a+1)/2).                  (1.2)

Indeed F_(N-1)/F_(N-1-a)=product_(r=1)^a(1-Q^(-r))
=(-1)^a Q^(-a(a+1)/2)F_a. Thus the actual balanced left cap
and cup are simply

    ev_L(w_a^dual tensor w_b)
                           =x^a/N delta_(a+b,N-1),
    coev_L(1)=sum_a N x^(-a) w_(N-1-a) tensor w_a^dual.   (1.3)

The actual right cap and cup are

    ev_R(w_b tensor w_a^dual)
                =x^a g_b/N delta_(a+b,N-1),
    coev_R(1)=sum_a N x^(-a)g_(N-1-a)^(-1)
                            w_a^dual tensor w_(N-1-a).  (1.4)

On their support the right-cap coefficient is

    (Q x^(1-N)/N)(Qx)^a.                                (1.5)

The coefficients (1.3)--(1.4) are whole identities in the original
finite matrices. The unbalanced J_x, its exact double dual g and
all four snake identities were independently proved in
[the pivotal duality note](relative_pivotal_duality.md).
Equations (1.2)--(1.5) do not change their normalization. In
particular, every cup contributes exactly N and every cap 1/N,
in addition to the displayed monomials and pivots.

## 2. A marked nilpotent defect gives the reduced closure

In this same balanced basis the actual cut source and co-source are

    psi_a=1, phi_a=1/N, e=psi phi, e^2=e, Tr(e)=1.

If the cut operator is C=F_N(M) I, the original reduced evaluation
is Tr(e C)=F_N(M). A fully closed ordinary pivotal network instead
has Tr(g C)=0. To implement the original selected cut as a marked
closed network, insert the specified operator

    D=g^(-1)e,      D_(a,b)=x^(N-1)Q^a/N.                (2.1)

Then, for every matrix C, not just scalar ones,

    Tr(g D C)=Tr(e C).                                  (2.2)

Moreover

    rank D=1, D^2=0, Tr(gD)=1, D g D=D.                 (2.3)

The nilpotence follows from sum_a Q^a=0. This defect is completely
fixed by the original pivot and boundary projector. It is not an
ordinary Hopf-intertwining local coupon, and its transport through
a crossing must carry the actual operator, not replace it by the
same local matrix on another strand.

The marked right cap is particularly simple. Insert D on its
primal input. Its array, with primal index b and dual index a, is

    ev_R^D(w_b tensor w_a^dual)=x^a/N^2,                 (2.4)

with no diagonal-support constraint. Directly, the only summand
in ev_R(D w_b tensor w_a^dual) has c=N-1-a, and
g_c D_(c,b)=1/N. Contracting (2.4) with coev_L in (1.3) gives
the unknot value one, whereas the unmarked cap gives Tr g=0.

Consequently any k-bridge plat can express the original reduced
knot evaluation with k cups, k-1 ordinary caps and one marked
cap. The exact scalar from these turns is

    N^k (1/N)^(k-1) (1/N^2)=1/N.                       (2.5)

All monomials, dual colors, crossing matrices and zero-framing
corrections are still present. Formula (2.5) explains the same
cut average 1/N for arbitrary k. It does not divide a zero quantum
dimension or introduce one modified trace for each bridge.
If the unreduced ADO evaluation is used, its whole d_N(M) remains
the same separate factor.

## 3. A bridge has an explicit cyclic boundary source

On a cap's support use a as the independent index; b=N-1-a.
Let T f(a)=f(a+1 mod N) and let e_partial be the delta function
at a=N-1. Each of (1.3)--(1.5), and the corresponding cup,
has the form

    v_a=kappa lambda^a,                                  (3.1)

with kappa a specified nonzero monomial times N or 1/N and
lambda a specified Q-power times x or x^(-1). There are exact
identities

    (T-lambda)v=kappa(1-lambda^N)e_partial,
    v=kappa sum_(j=0)^(N-1)lambda^(N-1-j)T^j e_partial.  (3.2)

The second identity follows by inspecting its a-th coefficient.
Equivalently (T-lambda)sum lambda^(N-1-j)T^j=1-lambda^N.
There is no division by 1-lambda^N. The vector remains nonzero
and has prescribed anchor v_0=kappa on that divisor as well.

For a left cap lambda=x. At x=-M/q its source factor is

    1-x^N=1+(-1)^N M^N.                                (3.3)

At M=1 this is 2 at even N and 0 at odd N. Those values do not
allow its whole meridian function to be discarded. In the odd
case (3.1) becomes a pointed homogeneous eigenvector; it does not
become the zero vector. The inverse-lambda cups retain their
corresponding 1-x^(-N) factors.

For disjoint bridges all T_i commute. Applying any subset of the
operators T_i-lambda_i to their tensor source gives exactly the
product of the displayed boundary factors and the corresponding
corner deltas, with all other bridge factors unchanged. This is
the entire cubical family of boundary intersections, not only the
single-corner terms.

For the marked cap (2.4), the primal index b is free. Its shift
in b has multiplier one, and the dual-index shift has

    (T_a-x)ev_R^D=(1-x^N)delta_(a,N-1) tensor 1_b/N^2.   (3.4)

Thus its removal of the ordinary cap relation is part of the
actual selected source. It cannot be replaced by an unmarked
inverse-meridian cap when comparing period complexes.

### The principal cap equations are the inverse-meridian equations

This paragraph concerns the q->1 principal symbol, not a fixed
root's center. Let U be the primal position and V the dual position.
The support in (1.3) gives UV=1 at the symbol. Write p_P,p_D for
their balanced momenta. The cup coefficient x^(-a) gives
p_D/p_P=x^(-1). A cap is a co-source, so its phase has the opposite
momentum sign; the leading x^a factor gives the same relation.
The right pivotal monomials and their base-only meridian phases
are still retained, as in the existing actual action calculation.

This has a direct matrix verification. For one balanced meridian use

    K=x/U, e=(1-x^2/U)p_P/x, f=(1-U)/p_P,
    b_+=[K e;0 1], b_-=[1 0;-Kf K].                     (3.5)

For its dual use x_D=x^(-1), position V and momentum p_D.
Substituting V=U^(-1),p_D=p_P/x gives exactly

    b_(+,D)b_(+,P)=I,
    b_(-,D)b_(-,P)=I.                                  (3.6)

Indeed K_D=K^(-1),e_D=-K^(-1)e,f_D=-Kf. Under the already
proved prefix transformation H_j=B_(-,j-1)^(-1)G_j B_(-,j-1),
equation (3.6) is precisely the inverse-meridian cap in the
arbitrary-plat representation scheme. This checks the cap from
the actual quantum coefficients, rather than assigning a
classical inverse relation independently.

The marked cap (2.4) instead imposes p_P=1,p_D=x^(-1),
with no position constraint of its own. At every bottom cup
both total Borel products are I. Each crossing preserves them.
All ordinary top caps also have product I. Therefore the two
products at the remaining marked pair must be I; on the regular
chart this restores V=U^(-1). The extra marked equation p_P=1
is exactly the fixed inverse-eigenflag: direct substitution gives

    G_P(1,1)^t=x^(-1)(1,1)^t.                            (3.7)

Conversely (3.7) forces p_P=1 when its stated shape factors are
units. It follows that the regular principal critical scheme of
the actual pointed plat is the knot representation scheme with
this selected peripheral flag fixed to 1. The inverse maps are
the same rational prefix/Gauss maps already proved for crossings.
The identities hold over Artin rings on that chart, since every
inverse used is a unit there. The retained meridian is M=-x at
the symbol, so the selected actual eigenvalue is M^(-1), consistent
with the original cut convention.

Thus every bridge's quantum turn, boundary source and principal
holonomy constraint now come from the same finite matrices. This
does not perform the remaining selected global period pairing.

## 4. The actual meridian half-step forces a second bulk channel

Put A=Q^a and let delta x=qx, delta A=A. This is the actual
M->qM step, not its square. First normalize kappa=1 and lambda=x.
The internal bulk monodromy of T-lambda is X=x^N. The half-step
sends X to -X. Therefore an invertible commuting meridian
transport cannot preserve a two-dimensional affine system whose
internal monodromy has only eigenvalues X and 1: its characteristic
polynomial would have to be both (z-X)(z-1) and (z+X)(z-1).
This fails over the generic coefficient field.

There is an explicit minimal three-dimensional completion. Put

    v_0(a,x)=x^a, v_1(a,x)=(qx)^a, w=(v_0,v_1,1)^t,
    B_T=[x 0 (1-X)e_partial;
         0 qx (1+X)e_partial;
         0 0 1],
    B_delta=[0 1 0; A 0 0; 0 0 1].                    (4.1)

Then

    T w=B_T w, delta w=B_delta w,
    T(B_delta) B_T=delta(B_T) B_delta.                  (4.2)

For the last identity use T(A)=QA and
QA e_partial=e_partial. The first bulk channel goes to the
second, and delta v_1=A v_0. The two boundary factors 1-X and
1+X are swapped. Both matrices are invertible for x!=0, even
at X=1 or X=-1; their determinants are qx^2 and -A.

The internal N-fold monodromy has eigenvalues X,-X,1. Hence
three is the least possible generic rank for a flat completion
retaining this bulk sector and its trivial source. The preceding
spectral argument is a rank obstruction, not a choice of an
extra physical state. The selected cap is still its specified
first component v_0 with its anchor. There are two bulk channels
because the meridian transports their central characters.

For a turn with lambda=q^s x^epsilon, epsilon=+1 or -1,
and kappa=c x^r (c fixed under delta), replace x,qx by
lambda,q^epsilon lambda, replace A by A^epsilon, and multiply
B_delta by q^r. The third selected component is then kappa,
and the first two are kappa lambda^a and
kappa(q^epsilon lambda)^a. The same direct calculation proves
flatness. This covers the actual cups, caps and marked cap,
with their full normalizations. No inverse of 1+X or 1-X occurs.

### The equivalent pointed norm-one frame

The three-dimensional assertion keeps the unmodified bulk norm
and its source as separate data. It is not a claim that a known
cap vector intrinsically needs three components. There is also
an explicit rank-one norm torsor which includes the last transition
in its multiplier. On the supported orbit put

    h(A)=sum_(a=0)^(N-1) q^a e_a(A), h^2=A,
    T(h)=q h (1-2e_partial),
    a_T=lambda[1+(lambda^(-N)-1)e_partial],
    a_delta=q^r h^epsilon.                              (4.3)

Every displayed multiplier is a unit when lambda!=0. The last
internal multiplier is lambda^(1-N), so

    Norm_T(a_T)=1, T(v)=a_T v, delta(v)=a_delta v,
    T(a_delta) a_T=delta(a_T) a_delta.                   (4.4)

To check the mixed square, use the ordinary q^epsilon factor
off the cut and T(h)(N-1)=1 at the cut. Equations (4.3)--(4.4)
also follow from a_T=T(v)/v and a_delta=delta(v)/v with the
explicit anchored unit v=kappa lambda^a. Thus this cap's
Hilbert-90 frame and full half-step transport are solved exactly,
including at lambda^N=1. The boundary defect is recoverable as
(a_T-lambda)v=kappa(1-lambda^N)e_partial. It is encoded in
the retained cut multiplier, rather than discarded.

For fixed q, h is a specified polynomial in A of degree <N;
its two square-root choices are not interchangeable. Its cut
sign is exactly what the two bulk channels in (4.1) record.
The meridian transport has 2N-fold norm one, and the entire
frame is fixed by v_0=kappa. This gives the explicit torsor
description of every turn alongside its affine-source presentation.

## 5. All bridges share one half-step, rather than independent parity choices

The construction has a uniform simultaneous version. For k bridges
let lambda_i=q^(s_i)x^(epsilon_i), epsilon_i in {+1,-1},
A_i=Q^(a_i), X_i=lambda_i^N and kappa=c x^r the full retained
monomial normalization. Use a component u_empty=kappa, and for
each nonempty subset I of {1,...,k} use two components

    u_(I,b)=kappa product_(i in I)
                           (q^(b epsilon_i)lambda_i)^(a_i),
    b=0,1.                                             (5.1)

There are 2^(k+1)-1 components, independent of N. The equations
retain two synchronized half-step channels for each nonempty
subset, sharing one empty-subset source.
Set u_(empty,0)=u_(empty,1)=u_empty. Their internal equations are

    T_i u_(I,b)=u_(I,b),                    i notin I,
    T_i u_(I,b)=q^(b epsilon_i)lambda_i u_(I,b)
          +(1-(-1)^b X_i)e_(partial,i)u_(I\{i},b), i in I.
                                                        (5.2)

The full meridian step is

    delta u_empty=q^r u_empty,
    delta u_(I,0)=q^r u_(I,1),
    delta u_(I,1)=q^r product_(i in I)A_i^epsilon_i
                                             u_(I,0).  (5.3)

These are commuting flat transport matrices. For distinct internal
directions, lowering subsets commutes and their coefficients depend
only on their own clock. To check a mixed square with delta, use
T_i(A_i)=QA_i and QA_i e_(partial,i)=e_(partial,i), just as
in (4.2); after lowering I the remaining product is exactly that
in (5.3) for I\{i}. The empty subset has the same retained scalar
character q^r. This proves flatness for every k and N.

The actual simultaneous bridge source is the component
u_({1,...,k},0), with the known diagonal-support embeddings and,
at the distinguished cap, its extra constant primal factor.
Thus the source intersections and actual half-step transport have
a finite explicit description for unbounded bridge number. The
exponential dependence here is on k, not on the root level N.

Their determinant line has no boundary denominator. With
R_k=2^(k+1)-1 the explicit matrices give

    det B_(T_i)=(q^epsilon_i lambda_i^2)^(2^(k-1)),
    det B_delta=-q^(r R_k)
                    product_i A_i^(epsilon_i 2^(k-1)).  (5.4)

The first identity counts the 2^(k-1) subsets containing i.
For the second, each nonempty-subset block has determinant
-product_(i in I)A_i^epsilon_i and every i occurs 2^(k-1)
times. All are units. In fact B_delta^(2N)=I, and its
determinant has meridian norm one. These statements retain
the actual half-step characters, with no division by a factor
that becomes 0 or 2 at completeness.

## 6. Exact propagation through the actual crossing word

Let B_N(x) be any actual oriented braid operator in the plat,
using the original R matrices and the literal turned matrices
J_V^(-1)C^t J_W where appropriate. They are invertible; same-color
formulas cannot be substituted on a dual-colored turn.

For the cup vector U and any finite boundary equation L U=b,
the transported equations and source are exactly

    (B_N L B_N^(-1))(B_N U)=B_N b.                     (6.1)

For several source channels apply B_N to all components. If
delta U=C_delta U, the meridian transport becomes

    delta(B_N U)=delta(B_N) C_delta B_N^(-1)(B_N U).     (6.2)

For an internal cyclic shift replace delta(B_N) by
T_i B_N T_i^(-1). Consequently all commuting squares in
Sections 4--5 survive; this is an identity in the finite matrix
algebra, including the corner projectors. The co-source is
transported by B_N^(-t). Its pairing with the source is unchanged.
No central character, corner source, pivot or selected normalization
is replaced by a scalar chosen after specialization.

Equations (1.3)--(6.2), together with the marked cap, specify the
original quantum boundary data for arbitrary k. They go beyond
assigning unnamed b_s to the classical contraction. They do not
yet prove that those full finite data descend to its geometric
normal deformation complex, or that their selected scalar has
the regulator's norm.

## 7. Boundary norms at completeness and the remaining volume problem

At M=1 the balanced g is unitary, e is an orthogonal projector
and D=g^(-1)e has operator norm one. The actual cups have norm
N^(3/2), ordinary caps N^(-1/2), and the marked cap N^(-1).
For a fixed k-bridge presentation their product has norm

    N^(k-1/2).                                         (7.1)

The zero-framing character has modulus one. In these specified
balanced bases, Cauchy--Schwarz therefore gives

    |F_N(1)| <= N^(k-1/2) ||B_N(1)||.                   (7.2)

The same control retains bounded meridian jets. Write u=Log M.
Every coefficient in the tensor of all turns is a monomial in M;
its total exponent has absolute value at most 2kN. Consequently,
for each fixed j, its j-th u derivative has norm at most

    (2kN)^j N^(k-1/2).                                 (7.3)

This estimates the actual whole boundary germ, rather than only
its value at M=1. The unchanged unreduced peripheral factor is

    d_N(e^u)=i^(N+3) sinh(u)/sinh(Nu).                   (7.4)

The fixed-order Taylor coefficients of N i^(-N-3)d_N(e^u)
are polynomials in N of degree at most their order. The j-th
derivative of d_N at zero is therefore O_j(N^(j-1)); the odd derivatives
vanish. Thus retaining that whole germ also preserves polynomial
boundary-jet control. No factor 1+M^N or 1-M^N has been evaluated
and canceled separately in deriving these bounds.

If the zero-framing monomial is included with the boundary data,
replace 2k in (7.3) by 2k+|w|, where w is the fixed diagram's
writhe. Its value at completeness has modulus one.

This is a uniform polynomial boundary bound. It does not give a
lower bound on the selected matrix coefficient or rule out an
exponentially small overlap. Any volume proof through the A-torsor
must still control that coupling and compare the resulting pointed
period with the calibrated geometric action. The nonzero boundary
vectors, flat completion and fixed normalization proved here do
not supply that remaining theorem by themselves.

[Audit](../experiments/audit_quantum_bridge_cap_source.py).
[Results](../experiments/quantum_bridge_cap_source_results.json).
