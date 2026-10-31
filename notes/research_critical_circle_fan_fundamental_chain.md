# Direct signed circle fans and the untwisted relative fundamental chain

Unpublished workspace research theorem, 31 October 2026. Conditional on the
original source and group-sewing hypotheses below. Root and coherent
completed internal analytical reviews and separate fresh exact replays.
This is not external peer review. The local identity below uses actual
white and shaded contact polygons, not the incorrectly complete-colored
20-symbol word. The corrected mixed-color word is an independent local
calculation. The global conclusion is conditional on the explicitly stated
original group-sewing data; it does not establish those data at every
maximum of the sharp absolute coefficient entropy.

## 1. Critical local chart and actual contact coordinates

Let x,y,b>0, 0<delta<1/2, s=sin(pi delta), k=cos(pi delta), and

    c=b+(x+y)/s^2,
    T^2=b(x+y)+xy+b^2 s^2=c^2 s^2-c(x+y)+xy.

These are the free-spectral critical equations on the strict LEFT
straddling chart. The input triangle has (q,T_q)=(b,T); the output
triangle has (q,T_q)=(-c,-T). In particular c>max(x,y).
Put D=(x+y)^2-4xy s^2 and use the following common Euclidean similarity
of the actual circle configuration:

    L=D/(xy), a=(y+x cos(2pi delta))/x,
    O=a-2isk,
    Z_q=a+(y-x)/q+2ik T_q/q,
    p_x=q Z_q/(q+x),
    p_y=L+q(Z_q-L)/(q+y).                         (1)

The outer circle centers are 0,L. Their radii in this chart are
sqrt(D)/x and sqrt(D)/y. Z_q is the middle-circle center and its
geometric radius is sqrt(D)/|q|. O is the selected lower intersection
of the outer circles, the actual P:J flag, where J=-exp(-2pi i delta).
The two p's are the MAIN tangent contacts. The normalization is a
Euclidean similarity fixing the ORIGINAL cone apex infinity. There is
no resetting of an independent Gauss reference flag.

Define the four literal fan shapes

    w_x=p_x/O,
    w_q=(p_y-Z_q)/(p_x-Z_q),
    w_y=(O-L)/(p_y-L),
    z_q=(O-p_x)/(p_y-p_x),

and let D_BW denote the Bloch--Wigner function. Set

    V(q,T_q)=D_BW(w_x)+D_BW(w_q)+D_BW(w_y)-2D_BW(z_q).
                                                               (2)

The source force angles and their Legendre normalization are retained:

    mu=atan(bk/T)/pi, nu=atan(ck/T)/pi,
    G=Q_b+log c-J_c,
    h=G-mu log b-(1-nu)log c-xi log x-eta log y,
    xi+eta=nu-mu.                                  (3)

Here G is the actual sharp real action, including the outside-row
products; the retained scalar modes are pure imaginary on this real
chart. The definition and absolute normalization of Q,J,G are those
of the reviewed signed-straddling generating relation.

**Local theorem.** On this connected physical critical chart,

    V(b,T)-V(-c,-T)=2pi h.                         (4)

The reflected RIGHT identity follows by exchanging input/output and
the original orientation. No mixed-color word identification is used
in (4).

## 2. Orientation and the factor two

For a white circle, an original directed polygon edge from contact p
to p' contributes Lambda((arg(p'-Z)-arg(p-Z))/2) to the cone volume
with apex infinity. This holds for the recorded polygon order, even
when it folds or has winding zero: sum the oriented triangle fan,
cancel its internal edges, and use the oddness and pi-periodicity of
Lambda. Since D_BW(exp(i theta))=2 Lambda(theta/2), its contribution
to TWICE the cut-ball volume is the D_BW of the contact-ray ratio.

For the input triangle the recorded white boundary edges are
O->p_x, p_x->p_y, p_y->O. Their three ray ratios are exactly the first
three shapes in (2). The shaded boundary has the opposite edge
orientation, hence is (O,p_y,p_x). A triangle (p_x,p_y,O) coned to
infinity has volume D_BW((O-p_x)/(p_y-p_x)); thus the shaded face
contributes -2D_BW(z_q) to twice the ball volume. This proves (2)
directly from the actual boundary orientation.

The output triangle has the opposite ORIGINAL white-triangle order.
Its displayed contact coordinates may lie on the same side as the
input after folding, but its combinatorial order is not changed.
Its contribution is therefore -V(-c,-T). The two abstract cut balls
have opposite orientations and are developed using one target
reflection, so their equal volume contributions give exactly (4),
with no additional factor two.

Repeated nonadjacent contacts in a white face cause no ambiguity:
the cyclic fan identity is applied in the original edge order on
ONE circle. The normalized repeated-vertex chains have zero terms;
one does not invoke continuity for arbitrary coalescing tetrahedra.

## 3. Exact differential and the absolute constant

The identity is scale invariant, so set y=1. Write

    s=2v/(1+v^2), k=(1-v^2)/(1+v^2),
    x=(T^2-b-b^2 s^2)/(b+1), 0<v<1.

For q=b,T_q=T or q=-c,T_q=-T, put co=1-2s^2 and

    N_x=x(1-x)+q(1+x co)+2ixkT_q,
    N_y=(x-1)+q(x+co)-2ikT_q,
    O_x=1+x co-2ixsk, O_y=x+co+2isk.

The four shapes (1) simplify, without changing any flag, to

    w_x=N_x/((q+x)O_x),
    w_q=-(q+x)N_y/((q+1)N_x),
    w_y=(q+1)O_y/N_y,
    z_q=(q+1)[xk-i(T_q+s(q+x))]
          /[k(q(x+1)+2x)+iT_q(x-1)].              (5)

Let p_in=(T-ibk)/(T+ibk), p_out=(T-ick)/(T+ick), and let N_x^b,N_x^c
mean the preceding N_x evaluated at (b,T),(-c,-T). Direct
differentiation of the source Legendre expression gives

    2pi dh=log b dArg p_in-log c dArg p_out
                         -log x dArg(N_x^b/N_x^c). (6)

Substituting (5) into
dD_BW(z)=log|z|dArg(1-z)-log|1-z|dArg z gives EXACTLY (6) for the
eight-shape difference. The accompanying verifier factors the
rational functions over Q(i)[b,T,v], retains Gaussian-rational
unit log norms (in particular log 2), and expands every
log|factor| dArg(factor) coefficient. All 49 tensor positions cancel
against (6). Conjugate factors have the same norm and opposite
argument derivative; only constant arguments have zero derivative.
This is a finite rational identity, with no numerical derivative or
unrecorded logarithm branch.

There are no shape or 1-minus-shape divisors in the physical interior.
Indeed Im O<0, while Im Z_q=2kT_q/q>0 and q/(q+x),q/(q+y)>0 imply
Im p_x,Im p_y>0. Also Z_q,L-Z_q are nonzero and

    p_x-Z_q=-x Z_q/(q+x),
    p_y-Z_q=y(L-Z_q)/(q+y),
    p_y-L=q(Z_q-L)/(q+y).

The numerator of p_y-p_x, apart from its nonzero real denominator,
is Ly(q+x)+qZ_q(x-y). Its imaginary part is 2kT_q(x-y); if x=y its
remaining real term is nonzero. Thus all three contacts are distinct
and all eight shapes and their complements are finite and nonzero.

The domain (b,x,delta)>0 with delta<1/2 is connected. Calibrate at
b=1,x=2,y=1 and delta->1/2. Then c->4,T->sqrt(6); all six white
ratios tend to 1, and the two shaded ratios tend respectively to

    -2(3+sqrt(6))/sqrt(6),
     3(2+sqrt(6))/sqrt(6),                         (7)

which are finite real numbers. Their Bloch--Wigner values tend to
zero. The verifier checks the leading numerator and denominator
separately at this anchor before taking their ratio.

For clarity, the source side tends to zero as well, rather than
being calibrated only by a derivative: put t=k tau in its retained
row integral. With r_k=sin(pi k tau)/k,

    Lambda(k tau)=2k^2 r_k[(x+1)r_k+
                              sqrt((x-1)^2 r_k^2+4x)],
    alpha(k tau)=4k^2(1-r_k^2).

The two endpoints tend to b/(pi T_1),c_1/(pi T_1), strictly on
opposite sides of 1/pi. The scaled interval is compact; the numerator
is uniformly positive and bounded, and the denominator has one
uniformly simple zero. Thus the logarithmic integral is O(k), while
mu,nu,xi,eta are O(k). Consequently h->0. The differential identity,
connectedness, and (7) prove the absolute identity (4).

## 4. Literal marked-line limits

The local assertion includes the nondegenerate single-line limits
by the same contact formulas, in the ORIGINAL apex frame. Here are
their explicit limits, with y=1 by the same harmless similarity.

When b->0 with x>0, put T_0=sqrt(x) and
F=1-x+2ik sqrt(x). The input contacts become

    p_x=F/x, p_y=L+F,
    w_x=F/(1+x co-2ixsk), w_q=1,
    w_y=-(x+co+2isk)/F,
    z_q=[xk-i(sqrt(x)+sx)]/[2kx+i sqrt(x)(x-1)].  (7a)

The actual middle line is Re((z-a) conjugate(F))=2k^2(x+1).
Both contacts have positive imaginary part and O has negative
imaginary part; p_y-p_x=4k^2+2ik(x-1)/sqrt(x) is nonzero. Thus
the limiting shaded triangle remains distinct, and only the middle
white fan becomes flat. In the source,
mu=bk/(pi sqrt(x))+O(b^2), so mu log b->0. Its interval endpoint
approaches 0, where Lambda(t) has a simple zero and alpha(0)>0.
The discarded small integral is O(mu |log mu|); all remaining
integrals and loads converge. Hence h has the same literal limit.

When x->0 with b>0, first translate every contact and center by -1/x
(or -y/x before normalizing y). This is affine and fixes infinity.
For q=b,T_q=T or q=-c,T_q=-T the limits are

    O*=co-2isk,
    Z_q*=co+1/q+2ikT_q/q,
    p_x*=co+2ikT_q/q,
    p_y*=[(q+2)co+1+2ikT_q]/(q+1),
    w_x=1,
    w_q=-(-1+q co-2ikT_q)/(q+1),
    w_y=(q+1)(co+2isk)/(-1+q co-2ikT_q),
    z_q=-i(q+1)(T_q+sq)/(kq-iT_q).                (7b)

Here T^2=b+b^2s^2 and c=b+1/s^2. The outer x-circle becomes the
actual line Re z=co; its two contacts are distinct on that line.
The affine map z->i(z-co) identifies it literally with the existing
outer-line adapter: O maps to +2sk and the middle center maps to
-2kT_q/q+i/q. Thus the same selected raw J flag is retained.
Both p's have positive imaginary part, and
p_y*-p_x*=2k(kq-iT_q)/(q(q+1)) is nonzero. Thus the shaded triangle
remains distinct and only the x-white fan becomes flat. The source
interval endpoints stay strictly inside (0,1/2), on opposite sides
of its simple alpha zero. On this compact interval Lambda is smooth
and nonzero even at x=0, and its x-logarithmic derivative is bounded;
the alpha zero is independent of x. Therefore xi=x partial_x G=O(x),
so xi log x->0, and all other terms of h converge.

For completeness y->0 can also be taken without ANY outer-label
reversal: in (1), with x fixed and no translation, the x-center
stays 0 with limiting radius1, the y-circle tends to Re z=co,
O->co-2isk, Z_q->co-x/q+2ikT_q/q, and

    p_x->(q co-x+2ikT_q)/(q+x),
    p_y->co+2ikT_q/q, w_y->1.

This is the same selected lower-intersection family. The identical
compact-interval estimate gives eta=O(y) and eta log y->0.

These calculations prove continuity for this ONE explicit family
and its literal line triangles, not for arbitrary colliding ideal
vertices. The only flat white contribution is D_BW(1)=0.

A strict straddling triangle with both x=b=0 (or y=b=0) is NOT added
by this statement: T=0 and nu=1/2 there, a terminal/free boundary
stratum. The global theorem below permits a forced two-line corner
only when its actual local branch is the already proved complete
CROSS line triangle. Any other double-zero or free boundary needs
a separate adapter.

## 5. Conditional original untwisted group and chain

Fix the original certified simple-white marked plat. Assume the
actual signed source clocks, selected spectral flags and full face
stationary equations satisfy the hypotheses of
[the regular signed group-sewing lemma](research_regular_signed_spectral_group_sewing.md) and yield
one global developed reflection family. Restrict the local branches
to complete CROSS triangles and strict free-spectral LEFT/RIGHT
triangles covered by (4), including only the line limits of section4.
All original cups, caps, prefixes and the unrestricted original mark
are retained. In particular this is not a construction from an
absolute maximum for which the sign cocycle has not been solved.

Use the UNTWISTED drilled exterior Y_D^0. Its literal first-ball
shaded pair is S_0=(O,C_1,C_2), S_1=(O,C_3,C_0), paired by
O->O,C_1->C_0,C_2->C_3 within that ball. These displayed tuples are
the FIXED PAIRING-LABEL listings. They
do not override the oriented boundary-chain orders of section2:
the input shaded chain has order (O,p_y,p_x). In particular no
orientation sign is inferred just from the listing S_0.
At a strict critical port, the primitive collar C has projective
eigenratio -1 on P's selected
flag. Hence C is the half-turn about the axis joining the two
outer-circle intersections. Each outer white plane contains that
axis, so C preserves BOTH outer planes. Its proved simultaneous
main-head conjugations then show that C carries the input middle
plane to the output middle plane. It therefore carries precisely
all three ordered contact flags in this original permutation, not
only O. At complete CROSS ports use their established three-point
collar, including the literal line cases.

Keep ONE global white reflection r_u for the second ball. Its shaded
map is r_u C r_u with the same original labels; white face f pairs
second to first by r_f r_u. The latter fixes the whole white plane
after removing r_u and identifies its complete recorded polygon
chain. These are exactly the original UNTWISTED face permutations.
No retained-half across-copy permutation is asserted here.

Use the labeled convex complete certificate to fix a degree-one
abstract triangulation of the original two balls: fan the incident
white faces from the original marked vertex p and cone p to the
nonincident boundary triangles. Change only its developed vertex
images to the present contacts. The original combinatorial boundary
identifications still hold, so this is the original equivariant
relative fundamental chain, even when its image folds. No new
interior vertex, replacement mark or image-degree assertion occurs.
Section2 computes its signed volume by its original face order.

## 6. Whole peripheral groups, truncation and the uniform gap

Every main peripheral subgroup contains its noncentral parabolic
meridian and hence preserves all horospheres at its contact. At a
strict critical auxiliary cusp, its actual two generators are the
primitive C^{-1} and P, up to the recorded central lifts. They commute,
fix the same two ideal flags, and have unit-modulus eigenvalues.
Therefore the WHOLE peripheral subgroup preserves every horosphere
at the selected flag. At a complete CROSS cusp the corresponding
whole subgroup is parabolic and has the same property. Merely
commuting with identity is not used.

Choose a horosphere at one lift of each original cusp and propagate
it equivariantly. Peripheral preservation makes this well defined.
No orthogonality of the now-intersecting white/shaded planes is
required. Truncate the finitely many incidence corners compatibly;
the ideal-chain limit agrees with the horospherically adapted
equivariant volume. For a compact critical peripheral group this is
also the canonical normalization used in the published general
volume bound: put its chosen flag at infinity and its other fixed
flag at 0. The cusp group acts by rotations z->exp(i theta)z on a
horosphere y=H. The equivariant homotopy (z,H)->((1-t)z,H) remains
on this horosphere and has rank at most two, hence zero three-volume.
Its endpoint is the finite axis point (0,H); the remaining axis tail
has rank at most one. This is a proof for the CONSISTENT original
horospherical boundary cycle, not a claim that an arbitrary rotating
torus or open mixed-flag bridge has zero cone volume.

Consequently the canonical representation volume is the computed
original two-ball chain volume, and

    2pi sum_e h_e=Vol(rho),
    |sum_e h_e| <= Vol(Y_D^0)/(2pi).               (8)

If at least one port is strict Green, its ACTUAL auxiliary meridian
has trace zero: the raw matrix M_0 satisfies M_0^2=-I. The original
complete auxiliary meridians have trace squared 4. Apply the proved
fixed-peripheral-word gap to the finite list of original auxiliary
meridians, with deviation 4. It gives a diagram-dependent g_D>0,
uniform on this entire conditional stratum, such that

    sum_e h_e <= [Vol(Y_D^0)-g_D]/(2pi).           (9)

This does not need a lower bound on delta, nor compactness of the
ordinary radius parameters beyond the existence of the stated
representation and chain. The published gap theorem uses exactly
the canonical peripheral volume just verified.

The same bound holds for any finite action limit of a sequence of
these coherent regular stationary configurations, each containing a
Green port. The finite meridian list and g_D are fixed, so take the
limsup in (9). Clocks, row endpoints and spectral parameters may
degenerate along that sequence. This is closure of ACTUAL solutions,
not a density assertion for an arbitrary KKT boundary datum.

The common original resolvent numerator uses H_V and is independent
of retained half-twist signs; those signs enter the outside Gaussian
through n_e=epsilon_e-2p_e. Thus (9), if its source hypotheses are
established for a relevant sharp remainder stratum, uses Y_D^0 with
the same capacity Phi=2Vol(Q_D)/(2pi)=Vol(Y_D^epsilon)/(2pi).
It is NOT an identification of the differently marked exteriors or
their filling phases. The existing all-CROSS filling theorem retains
the actual epsilon and framing separately.

## 7. Verification and remaining scope

The [portable exact verifier](../experiments/research_audit_critical_circle_fan_fundamental_chain.py)
and its [saved result](../experiments/research_critical_circle_fan_fundamental_chain_results.json)
check four generic contact-coordinate identities, the eight actual
fan shapes and 49-position differential tensor, eight real endpoint
values and sixteen separately nonzero uncancelled leading anchor
factors. The author replay passed. The verifier imports only rational
factor/differential utilities from the quarantined formal-word audit;
no complete-color mixed-symbol claim is imported. Root and coherent
completed full conditional analytical/code reviews and separate fresh
redirected replays, reproducing all counts. The saved result is the
author result; both independent results agree on all counts and exact
identities. The portable workspace verifier was compared by Python AST
to the replayed stable private verifier after exactly two documented
changes: its helper import is relative to its own file, and its default
result path is beside that file. No separate portable runtime is claimed.

The global chain uses the original combinatorics of
[matching geometry](general_augmented_plat_matching_geometry.md), the
reviewed abstract-chain construction in the
[endpoint signed cut-ball proof](actual_fejer_signed_cut_ball_regulator.md),
and the canonical normalization and uniform conclusion of the
[fixed peripheral-word volume gap](general_representation_volume_peripheral_gap.md).
Its new intersecting-circle fan calculation replaces the endpoint
orthogonal-shaded-face formula; that old formula is not imported
outside its tangent case.

The global proof still assumes actual signed-clock compatibility,
the full original face stationary equations, the stated regular
branch list and flags, and the permitted marked-line limits. It
does not prove that every sharp absolute coefficient maximum has
these properties, handle free spectral/row/ordinary boundary strata,
or give a contributing Fourier cycle. Those are the remaining source
and compact-boundary questions. The retained-half global face adapter
is separate and unnecessary for this common untwisted numerator
upper-bound statement.

An inconsistent phase assignment may have an exponential cancellation
relative to its own positive envelope. That envelope can exceed Phi;
such a relative loss alone does not bound it by Phi. No combination of
that local phase exclusion with this conditional geometric theorem is
being asserted to cover the missing global remainder.

## 8. Mixed complete Green ports in the same original chain

The [shared-stationarity reduction](research_regular_shared_spectral_stationary_reduction.md)
also checks the following extension for general stationary data.
Some one-sided ports may have delta=0 while another is strict
positive-spectral Green. Retain their ORIGINAL endpoint signed
triangle fans from the tangent cut-ball theorem; do not replace
their parabolic collars by identity.

The exact old adapter is C=I+i r(P+I), where
r=(eta_c T_c-eta_b T_b)/(2(x+y)) is real, including its literal
one-line and two-line versions. Normalize the tangent outer planes
to Re w=0,1. Their raw product is P=-[[1,2],[0,1]], so C acts by
w->w-2ir. It therefore preserves BOTH outer planes. Its already
proved simultaneous head conjugations carry the middle plane and
all three original ordered contacts. This proves the same shaded
pairing used in section5, without an inference from eigenratio1.
Its whole peripheral subgroup is parabolic and preserves the
chosen contact horosphere.

Consequently these endpoint Green fans and the new intersecting
critical fans sum in ONE developed family and the SAME original
two-ball relative chain. The permitted branch list in section5
can be extended by these old endpoint branches, including their
proved forced two-line corners. At least one strict positive-
spectral Green port still supplies the uniform trace-zero gap.
If all spectral parameters are0, the existing endpoint noncross
entropy gap applies separately; no trace-zero conclusion is made.

Root and coherent independently reviewed this explicit endpoint
adapter and its mixed-chain implication. For MAXIMA of the sharp
interval functional, the new reduction gives more: a positive-
length nonterminal one-sided delta=0 port can be improved at fixed
face loads, so such mixed endpoint ports cannot occur on that
regular maximizing stratum. Diagonal and terminal strata are not
removed by that argument.
