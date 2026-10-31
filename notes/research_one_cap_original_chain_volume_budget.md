# The one-cap exterior has an original group representation, with a positive pyramid deficit

31 October 2026. **analytical research theorem.**
Unpublished. Hypotheses are the
strict ONE-cap stationary configuration of the geometric-double
theorem: the original simple matched sphere has protected MAIN edge uv,
F=(u,A,v,C), all other original ports CROSS, all ordinary incidences
positive and finite common weights. The cap split is 1/4<nu<1/2.

This constructs a representation of the original UNTWISTED drilled
group using the positive exterior packing. It is NOT the failed direct
specialization of the signed sigma=+2 source chart. The latter's [raw central/noncentral obstruction](research_double_protected_cap_finite_collar_obstruction.md) is unchanged. The construction gives a
quantified absolute budget, not the desired nonpositive cap deficit.

## 1. Boundary packing and the actual ordered collar

Normalize the four boundary contacts as

\[
uA=1,\qquad AC=0,\qquad Cv=-1,\qquad uv=\infty.\tag{1}
\]

Put k=cot(pi nu), phi=atan k, so 0<k<1 and
phi=pi/2-pi nu in (0,pi/4). The actual white circles have centers

\[
\begin{aligned}
\operatorname{center}(A)&=\frac{1+ik}{2},&
\operatorname{center}(C)&=-\frac{1+ik}{2},\\
\operatorname{radius}(A)&=\operatorname{radius}(C)
 =\frac{\sqrt{1+k^2}}2,&
u:&\ X-kY=1,\qquad v:\ X-kY=-1.
\end{aligned}\tag{2}
\]

The recorded exterior D lies on the LOWER side of the real contact
line. In particular the A fan is the minor arc from0 to1 below the
line, with angle pi-2phi=2pi nu. This fixes the side and orientation;
the circles alone would not select which complementary disk is D.

Write d0=sqrt(1+k^2). The following anti-Mobius reflection matrices
have determinant -1 and the original coorientations:

\[
\begin{aligned}
J_A&=d_0^{-1}\begin{pmatrix}1+ik&0\\2&-1+ik\end{pmatrix},&
J_C&=d_0^{-1}\begin{pmatrix}-1-ik&0\\2&1-ik\end{pmatrix},\\
J_u&=d_0^{-1}\begin{pmatrix}1-ik&-2\\0&-1-ik\end{pmatrix},&
J_v&=d_0^{-1}\begin{pmatrix}-1+ik&-2\\0&1+ik\end{pmatrix}.
\end{aligned}\tag{3}
\]

Thus every original MAIN product at this port has trace -2. Set

\[
\begin{aligned}
A_b&=J_A\overline{J_u},& B_b&=J_C\overline{J_A},\\
A_v&=J_v\overline{J_u},& B_v&=J_C\overline{J_v},\\
P_{\mathrm{raw}}&=B_bA_b=B_vA_v=J_C\overline{J_u}.
\end{aligned}\tag{4}
\]

Its raw trace is -2(3-k^2)/(1+k^2)<-2. The harmless central choice
P=-P_raw has positive trace. Define the projective collar

\[
\mathcal C=\begin{pmatrix}a&-1\\-1&1\end{pmatrix},\qquad
 a=\frac{-1+3ik}{1+ik}=1-2e^{-2i\phi}.\tag{5}
\]

Direct multiplication gives the literal ordered relations

\[
\mathcal C A_b\mathcal C^{-1}=A_v,\qquad
\mathcal C B_b\mathcal C^{-1}=B_v,\qquad
\mathcal C P_{\mathrm{raw}}=P_{\mathrm{raw}}\mathcal C.\tag{6}
\]

It sends the recorded flags 1->infinity and0->-1. It preserves each
of the two outer white planes: projectively
\(\mathcal C\) J_u=J_u bar(\(\mathcal C\)) and \(\mathcal C\) J_C=J_C bar(\(\mathcal C\)).
The scalar in both raw identities is (k+i)/(k-i), so no equality of
unscaled anti-linear matrices is being asserted. The determinant is
-2 exp(-2i phi). Hence

\[
\widehat C=\frac{\mathcal C}{i\sqrt2e^{-i\phi}},\qquad
\det\widehat C=1,\qquad
\operatorname{Tr}\widehat C=2\sqrt2\sin\phi=2\cos\psi,
\qquad 0<\psi<\frac\pi2.\tag{7}
\]

The actual untwisted auxiliary meridian is the projective \(\widehat C^{-1}\);
the preferred longitude is P (up to the recorded central sign).
There is no introduced framing, half twist or replacement peripheral
word. Every other original coupon has its usual tangent-circle collar
from the complete positive exterior packing.

## 2. Both auxiliary flags, with their side fixed

The common fixed points of P and \(\mathcal C\) solve

\[
O^2-2e^{-2i\phi}O-1=0.
\]

Write alpha=arcsin(sqrt(2)sin phi) in (0,pi/2),
ell=asinh(cos alpha)>0. They are

\[
O_{\mathrm{out}}=e^{\ell-i\alpha},\qquad
O_{\mathrm{in}}=-\frac1{O_{\mathrm{out}}}
=e^{-\ell-i(\pi-\alpha)}.\tag{8}
\]

Both lie STRICTLY BELOW the real line, on the existing exterior side.
For the explicit P=-P_raw in (4), O_in is the expanding flag and O_out
the contracting flag. \(\widehat C\) has eigenvalues exp(-i psi), exp(+i psi)
there respectively, with psi=pi/2-alpha. Thus the meridian eigenvalue
at the expanding longitude flag is exp(+i psi). Using the other flag
does not change the volume calculation below.

Reflection r_u swaps these flags: r_u P_raw r_u=P_raw^-1 and P_raw is
genuinely loxodromic. The original cap parameter is NOT a real spectral
delta in the earlier intersecting/signed source chart. No identification
with that chart's local source action or its regulator primitive is
used here.

## 3. Original group sewing and its non-reflected auxiliary flag

Use the single global white circle family supplied by the geometric
double, restricted to D and its four boundary faces. At every original
MAIN edge the two adjacent white circles are tangent, so its ordered
head is the actual noncentral parabolic reflection product. The
reflection prefixes at a Morse slice telescope exactly. A cup/cap
inserts F,G,F and its two ordered heads multiply to identity. Every
unchanged CROSS box has its original primitive collar. At F use (6).
These are precisely the original untwisted van Kampen/Morse relations;
no local spectral interpretation is required to construct the group
representation. This is the algebraic part of the variable-headcount
group dictionary, independent of its source-action application.

Here is an explicit compatible ideal-chain decoration, which avoids
the false assertion that the chosen cap flag lies on both outer white
planes. On the first original cut ball assign all unchanged contact
vertices their exterior packing contacts. Assign its matching uC vertex
one selected O in (8). On the second ball reflect every OTHER contact
vertex by the ONE global r_u, but assign the cap vertex the SAME O,
not r_u(O). This exception is essential.

The original white pairing for face f is r_f r_u. On white u this is
identity, so it matches O to O. On white C it is P_raw, which also
fixes O. These are the only white faces containing this cap vertex.
All their other vertices match by the usual reflection argument.
Every other white polygon remains exactly the reflected polygon.
Therefore the entire triangulated white face chains pair correctly,
although the two altered polygons need no longer lie in white planes.
Use the existing original abstract fan triangulations, chosen compatibly
across paired faces. Degree one comes from the original positive
polyhedron's abstract domain certificate, not from convexity or planarity
of these newly developed polygons.

The first-ball shaded cap pairing is \(\mathcal C\) with its original permutation

\[
(O,1,0)\longmapsto(O,\infty,-1).
\]

The second-ball pairing is r_u \(\mathcal C\) r_u. It fixes the SAME O because
r_u swaps the two fixed flags and \(\mathcal C\) fixes both. It sends the other
two reflected contacts in the same recorded order. All other shaded
pairings are unchanged. Consequently these assignments give the
original degree-one relative fundamental chain, with the original
within-copy untwisted permutations and one common choice of all other
flags. They are not the differently marked chain of the doubled link.

The auxiliary peripheral subgroup is of axis type, generated by the
elliptic \(\widehat C^{-1}\) and loxodromic P with common fixed flags. All other
cusps remain boundary-parabolic. The already proved general-peripheral
volume theorem, section 2, identifies the sum of the developed ideal
tetrahedron volumes with the canonical representation volume also in
this axis case. Its explicit cusp homotopy has boundary flux O(y^-2);
no horosphere preservation is asserted for P, and no extra arbitrary
peripheral constant can be added to this ideal-chain calculation.

## 4. The cap is a pyramid subtraction, not a zero-volume patch

In the convex doubled polyhedron the four contacts (1) lie in the
vertical geodesic plane over the real line. They form an ideal
quadrilateral K. The intersections of this plane with the four
boundary white planes are its four sides. Convexity shows the plane's
intersection with the doubled polyhedron is EXACTLY K: K is contained
by convexity of its four vertices, and the four white halfspaces cut
out no larger region. The plane splits the doubled polyhedron into
the two exterior pieces. In this normalization the copy involution is
the orientation-preserving half-turn \(z\mapsto-z\), which exchanges their
sides; it is not reflection in the real contact line. Thus equality of
the two volumes does not presume a reflected packing.
The recorded D side is the lower side: absence of the boundary diagonal
uC forces an interior neighbor in the A fan, whose positive angle lies
on the minor arc below the real line. This fixes which of the two
components is D, consistently with (2).
Each has volume

\[
V_D=\pi M_{\mathrm{cap}}.\tag{9}
\]

The first original ball's boundary is obtained from the D piece by
replacing K with the four-triangle cone to O. Two of these triangles
are the original shaded cap faces; the other two are the additions
to the white u and C faces. This is a statement about the oriented
abstract boundary chain, not a convexity claim for its new image.

Since O lies on the EXISTING D side of K, that oriented replacement
SUBTRACTS the volume of the ideal pyramid with base K and apex O.
Using Vol[infinity,0,1,z]=D(z), its positive volume is

\[
W(O)=D(-O)-D(O)>0,\qquad \Im O<0.\tag{10}
\]

Here is a chain-level sign check in this tetrahedron convention. The
outward cut face is

\[
K=[\infty,-1,0]+[\infty,0,1].
\]

The NEW-ball-minus-exterior chain is

\[
S=[O,\infty,1,0]+[O,\infty,0,-1],\qquad
\partial S=\operatorname{fan}_O(\partial K)-K.
\]

Its boundary is exactly fan_O(boundary K)-K, and its volume is
D(O)-D(-O). This fixes the subtraction sign without identifying the
orientation of a listed pairing tuple with an oriented face chain.
This provides an absolute orientation/calibration, not a differential
guess or a claim that the four flat contacts alone make the cap zero.
Thus the first original ball has signed volume V_D-W(O).

Reflecting the second ball back by r_u and reversing its abstract
orientation gives the same exterior D piece but the OTHER auxiliary
flag r_u(O). Formula (8) and D(1/z)=-D(z) imply

\[
W(O_{\mathrm{in}})=W(O_{\mathrm{out}}).
\]

The exact two-ball canonical-chain identity is therefore

\[
\operatorname{Vol}(\rho)=2\pi M_{\mathrm{cap}}-2W(O_{\mathrm{out}}).
\tag{11}
\]

Both the factor two and the sign come from the literal ball pairings.
The original all-CROSS source, source spectral phase, and its possible
cancellation have not been changed or identified with this representation.

## 5. Explicit positive budget and its sharp elementary range

Put O=O_out from (8). One has

\[
|O-1|^2=2,\qquad \frac{1+O}{1-O}=-\overline O.
\]

The Bloch--Wigner differential

\[
dD(z)=\log|z|\,d\operatorname{Arg}(1-z)
      -\log|1-z|\,d\operatorname{Arg}z
\]

then gives dW=2ell d alpha. At alpha=0 the two tetrahedra are flat and
W=0, fixing the absolute constant. Consequently

\[
\begin{aligned}
W(\nu)&=2\int_0^\alpha\operatorname{arsinh}(\cos t)\,dt,
&\alpha&=\arcsin\bigl(\sqrt2\cos(\pi\nu)\bigr),\\
\frac{dW}{d\nu}
&=-2\sqrt2\pi\sin(\pi\nu)\,
\frac{\operatorname{arsinh}\!\sqrt{-\cos(2\pi\nu)}}
     {\sqrt{-\cos(2\pi\nu)}}.
\end{aligned}\tag{12}
\]

Equivalently W=integral_psi^(pi/2) 2asinh(sin t)dt. In particular
W is strictly positive and strictly decreasing for 1/4<nu<1/2.
Its endpoint values are

\[
W(\tfrac12)=0,\qquad W(\tfrac14)=2G,\qquad 0<W<2G.\tag{13}
\]

where G=integral_0^1 atan(t)dt/t is Catalan's constant. To check the
upper endpoint without a special-value import, differentiate
I(a)=integral_0^(pi/2) asinh(a cos t)dt. The substitution u=sin t
gives I'(a)=atan(a)/a and I(0)=0, hence I(1)=G.

Apply the actual original representation-volume bound to (11):

\[
M_{\mathrm{cap}}-\Phi_D
\le\frac{W(\nu)}\pi<\frac{2G}\pi=C_0.\tag{14}
\]

There is also a strict representation-theoretic improvement at any
fixed configuration. The actual primitive auxiliary meridian has
trace squared 4cos^2(psi)<4. The fixed-peripheral-word gap gives
some g>0 for the fixed original exterior and meridian (uniform when nu
ranges in a compact subset of (1/4,1/2) with those data fixed), with

\[
M_{\mathrm{cap}}-\Phi_D
\le\frac{W(\nu)}\pi-\frac g{2\pi}
<\frac{W(\nu)}\pi.\tag{15}
\]

No available estimate asserts g>=2W, so this still does not prove the
desired nonpositive deficit. The word is the ONE fixed original
auxiliary meridian; no level-dependent peripheral power is used.

Equivalently the original constrained defect obeys
Delta_cap<=C0+W(nu)/pi<2C0. This is a uniform complexity-independent
bound for a strict ONE-cap-only stationary configuration. It is
weaker than Delta_cap<=C0; it does not settle the desired absolute
cap comparison. A signed-source loss exceeding W(nu)/pi would suffice
to close that configuration's absolute budget, but no such loss is
asserted here. In particular a positive local loss, or a single
opposite-face cofactor estimate, need not pay this entire amount.

## Scope and proof dependencies

The original source incidence, mark and unsigned cap action are those of
[the original cap-capacity budget](research_cap_constrained_capacity_budget.md). The genuine exterior
and its exact capacity are supplied by
[the one-cap geometric double](research_one_cap_geometric_double.md). The group sewing is the
literal reflection-prefix/Morse relation from
[the actual Morse group dictionary](research_general_morse_cross_action.md), section 2, used only as
an algebraic group construction. The ordered within-copy shaded
permutations and degree-one two-ball chain are those of
[the original cut-ball chain](actual_fejer_signed_cut_ball_regulator.md), section 3; its old
all-reflected auxiliary-flag choice is explicitly REPLACED at this one
cap. The canonical ideal-chain volume equality for an axis cusp is
[canonical volume for general peripheral images](general_peripheral_representation_volume_bound.md), section 2.
The optional strict inequality (15) uses
[the fixed-peripheral-word volume gap](general_representation_volume_peripheral_gap.md).

In particular the
old finite-collar obstruction at the signed real spectral cap remains
valid and is not overridden by this different positive exterior chart.