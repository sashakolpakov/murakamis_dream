# Literal port gluing and the complete geometric holonomy anchor

29 October 2026. The selected regular mixed source has an explicit
matrix lift to the original augmented pretzel diagram. Its common
\(w\) and outer equation \(\prod_iU_i=1\) glue the actual ports.
At completeness, every white AND shaded face map agrees with the
explicit four-antiprism geometry. Thus its base representation is
the oriented geometric holonomy, not merely a character with the
same cusp Hessian or a representation with similar trace equations.

This note uses the actual stationary identities in
[the local mixed-character lift](actual_pretzel_mixed_regular_character_lift.md).
It does not infer a source cycle or a quantum asymptotic from those
identities; those were proved separately from the finite source.
The lift below is a DIRECT algebraic construction: its group relations,
framed peripheral eigenvalues and cap equalities are verified explicitly.
It does not require a further assertion identifying the canonical
state graph of an arbitrary scalar operator \(F(\Omega)\) from its
unwrapped eigenphase. In particular a state-versus-observable Hurwitz
convention is not silently used to choose between \(U\) and \(U^{-1}\).

## 1. A common two-head frame and the literal turned ports

Let \(w\ne0,\pm1\), set
\(k=(w-1)^2/(w+1)^2\), and for \(z\ne0\) put

\[
 g(z)=\begin{pmatrix}
 -2w/(w+1)&z\\-k/z&-2/(w+1)
 \end{pmatrix},\qquad h(z)=g(-wz),\qquad
 A=\operatorname{diag}(w,w^{-1}).                     \tag{1}
\]

They have determinant one and trace \(-2\), and
\(h(z)g(z)=A\). Neither meridian is central on this chart.
The fixed flag of \(g(z)\) is \(z/r\), where
\(r=(w-1)/(w+1)\); the fixed flag of \(h(z)\) is \(-wz/r\).

For a rotated box with character \(U\ne0\), take incoming pair
\((g(z),h(z))\) and outgoing pair \((g(Uz),h(Uz))\).
The original turn index map is

\[
 (\mathscr R B)_{(u,b);(v,e)}
                  =x^{u-e}B_{(d-u,v);(b,d-e)}.
\]

The actual cup/cap identifies the bent meridian with its inverse.
Choose based paths along these turn arcs. Therefore the original
UNROTATED box has incoming and outgoing ordered meridians

\[
 (a,b)=(h(Uz),h(z)^{-1}),\qquad
 (r_{\mathrm{out}},s_{\mathrm{out}})=(g(Uz)^{-1},g(z)).          \tag{2}
\]

Their common product is the actual crossing-disk product

\[
 P=ba=h(z)^{-1}h(Uz)=g(z)g(Uz)^{-1}
                         =s_{\mathrm{out}}r_{\mathrm{out}}.     \tag{3}
\]

This is the literal turn convention, rather than a free choice of
independent strand gauges. At the quantum level the same turns
and their scalars are those of the exact rotated source. Their
normalization does not alter the group inverse relation.

## 2. The auxiliary circle is an explicit regular centralizer

On the local regular stationary branch write

\[
 U=\frac{wY-1}{w-Y},\qquad
 L=\frac{H-X}{1-HX},\qquad
 \operatorname{Tr}P=-L-L^{-1}.
\]

The stationary \(X\) equation also gives the exact identity

\[
 \frac{1+YL}{1+Y/L}=\frac{L^2}{H}.                   \tag{4}
\]

These are the rational equations certified from the actual finite
factorial phase, with its selected branch, in the linked local
theorem. Put

\[
 \Delta=(1+YL)(1+Y/L)=1-Y\operatorname{Tr}P+Y^2,
\]
\[
 J=\frac{I-YP}{\sqrt\Delta},\qquad
 C=\frac{YI-P}{\sqrt\Delta}.                         \tag{5}
\]

The square root is its analytic branch tending to \(1+Y\) at
\(H=1,L=1\). It is nonzero near the complete branch. Both
matrices have determinant one, commute with \(P\), and
\(JC=-P\). On the \(P\)-eigenflag with eigenvalue
\(\lambda=-L^{-1}\), equation (4) gives

\[
 C\text{ eigenvalue }M=H^{-1/2},                     \tag{6}
\]

on the branch tending to \(+1\). The reciprocal flag has eigenvalue
\(M^{-1}\). Thus this is the actual auxiliary meridian together
with the preferred disk-longitude eigenvalue \(-L^{-1}\); its
SL spin character is kept.

These data realize the actual threaded half twist, not just its
trace. Direct substitution of (1), with
\(Y=(Uw+1)/(w+U)\), gives \(Ja=g(z)J\).
Together with (3), and \(JC=-P\), this proves

\[
 \boxed{\quad
 r_{\mathrm{out}}=C^{-1}bC,\qquad
 s_{\mathrm{out}}=C^{-1}bab^{-1}C.\quad}                  \tag{7}
\]

This is precisely the physical \(R^{-1}\) half-Hurwitz convention
with its typed auxiliary circle, as independently derived in the
local theorem. The formulas are valid with every exterior port
retained.

At completeness,

\[
 C=I-\frac{P+I}{1+Y},\qquad
 J=I-\frac{Y}{1+Y}(P+I).                            \tag{8}
\]

Here \(P\) is a NONCENTRAL trace-\(-2\) parabolic and
\(Y\ne-1\), so \(C\) is a finite noncentral parabolic. No
singular diagonal frame or semisimple deletion of the complete
circle is used.

## 3. Global gluing and the actual filled-knot representation

Keep the original left-to-right box label \(b=1,\ldots,s\).
For that box let its incoming rotated parameter be \(t_b\) and
its outgoing parameter \(t'_b=U_bt_b\), with the SAME \(w\)
at every box. Formula (2) says that its original bottom ports are
\((h(t'_b),h(t_b)^{-1})\) and its top ports are
\((g(t'_b)^{-1},g(t_b))\). The literal original caps pair bottom
port 2 of box \(b\) with bottom port 1 of box \(b+1\), and
likewise the corresponding top ports. They therefore impose EXACTLY

\[
 t_b=t'_{b+1},\qquad\text{equivalently }\quad
                 t_{b-1}=U_b t_b,                    \tag{8a}
\]

with cyclic box indices. This is right-to-left operator composition:
the product \(\mathscr R(B_1)\cdots\mathscr R(B_s)\) applies the
rightmost box first. Starting at \(t_s\ne0\) and propagating in
the order \(s,s-1,\ldots,1\), the outer marked stationary equation
\(\prod_bU_b=1\) closes both ports exactly. Every individual
bottom and top cap is an inverse pair by (8a).

Below we index this reverse cyclic TRAVERSAL by \(i\), so its
successive incoming and outgoing parameters are denoted
\(z_i,z_{i+1}=U_bz_i\). This notation does not change or permute
the physical source boxes. The geometric face labels follow this
same traversal. The explicit orientation-preserving reversal
isometry (13) below checks that its half-twist pairings describe
the SAME oriented manifold. No mirror, arbitrary mutation or
omission of a cap is used.
The [independent literal cap-order audit](actual_pretzel_literal_cap_order_audit.md)
also checks this multiplication direction on generic NONCOMMUTING
physical boxes; commutativity of the special Casimir polynomials
is not being used to hide the order of these individual ports.
The independently proved odd-width connectivity makes the main
component one component. The pivot and marked normal source have
already been retained in the source derivation of the outer
equation; no missing half-angle closure is inserted here.

This constructs a representation of the actual augmented-link
group, with its main meridians parabolic, and its \(i\)-th auxiliary
meridian/longitude represented by \(C_i,P_i\).

At a selected filling point put \(z_i^{\mathrm{eig}}=\operatorname{Log} H_i\),
\(\ell_i=\operatorname{Log} L_i\), using the source's continuous logarithms.
The actual unit-charge filling equation is

\[
 z_i^{\mathrm{eig}}+2p_i\ell_i=2\pi i m_i,\qquad m_i=\pm1.
 \tag{9}
\]

By (6), \(C_iP_i^{p_i}\) has BOTH eigenvalues
\((-1)^{p_i-m_i}\). The nearby selected filling has
\(L_i\ne\pm1\): its nonzero small Fourier saddle
\(\zeta_i\) satisfies \(\ell_i=-2\pi i\zeta_i\), by the
actual Fourier stationarity, so \(\ell_i\ne0\) and
\(|\ell_i|<\pi\). Thus these commuting matrices are diagonalizable
together and their product is that scalar matrix. Hence
\(C_iP_i^{p_i}=1\) in PSL(2,C). The relation also extends by
continuity if needed. Substituting it into (7) gives
\(\operatorname{Ad}(P_i^{p_i})(b,bab^{-1})\), which is exactly
the \((2p_i+1)\)-st power of the physical half-Hurwitz map.
The representation therefore descends to the literal original
filled pretzel knot. No faithfulness is assumed at this step.

## 4. Every complete geometric face pairing is matched

Put \(\alpha=\pi/s\), \(U=e^{2i\alpha}\),
\(\rho^2=\sec\alpha+\tan\alpha\), \(R=\rho^4\),
\(w=-R\), and \(r=\csc\alpha=(w-1)/(w+1)\).
Choose the allowed common scale

\[
 z_i=\frac r\rho e^{(2i-1)i\alpha}.
\]

The fixed flags of \(g_i=g(z_i)\), \(h_i=h(z_i)\) are now

\[
 U_{i-1}^+=\rho^{-1}e^{(2i-1)i\alpha},\qquad
 U_{i-1}^-=\rho^3e^{(2i-1)i\alpha},
\]

and \(P_i=g_i g_{i+1}^{-1}\) fixes
\(Z_i=\rho e^{2ii\alpha}\). These are exactly ALL ideal
vertices of the explicit polyhedron \(\mathcal P_s\) in
[the geometric-volume construction](actual_augmented_pretzel_geometric_volume.md).

Let \(r_F\) denote reflection in the white face plane \(F\),
acting antiholomorphically on its boundary circle. The two polygon
circles are \(|\zeta|=\rho^{-1},\rho^3\), so

\[
 r_{W_+}(\zeta)=\rho^{-2}/\bar\zeta,\qquad
 r_{W_-}(\zeta)=\rho^6/\bar\zeta.
\]

The white quadrilateral \(Q_i\) has circle center and radius

\[
 c_i=\rho\sec\alpha\,e^{(2i+1)i\alpha},\qquad
 R_{Q}=\rho\tan\alpha.
\]

Its reflection is \(r_{Q_i}(\zeta)=c_i+
R_Q^2/(\bar\zeta-\bar c_i)\). Their products give EXACTLY

\[
 r_{Q_i}r_{W_+}
 =\frac1{\tan\alpha}
  \begin{pmatrix}-\rho^2&c_i\rho^{-2}\\
                         -\bar c_i&\rho^{-2}\end{pmatrix}
 =g_{i+1},\qquad r_{W_-}r_{W_+}=-A.                 \tag{10}
\]

All equalities are literal SL matrices as displayed, except the
explicit harmless central sign in the last equality.
Also \(h_{i+1}=r_{W_-}r_{Q_i}\) in PSL. Thus every white-face
holonomy has been identified, not merely its fixed flags.

Develop the second projection polyhedron as
\(r_{W_+}(\mathcal P_s)\), using \(W_+\) as the face tree.
Define

\[
 \gamma_i^+=J_i g_{i+1},\qquad
 \gamma_i^-=h_{i+1}J_i^{-1}=J_i^{-1}g_i.             \tag{11}
\]

These are the TWO shaded face pairings at the \(i\)-th retained
half twist. They act on the ideal vertices as

\[
 \gamma_i^+:r_{W_+}(Z_i,U_i^-,U_{i-1}^-)
                              \longmapsto(Z_i,U_{i-1}^+,U_i^+),
\]
\[
 \gamma_i^-:r_{W_+}(Z_i,U_{i-1}^+,U_i^+)
                              \longmapsto(Z_i,U_i^-,U_{i-1}^-).
 \tag{12}
\]

Here is a direct reason for each map. The white reflection product
fixes its \(Q_i\) vertices, while \(J_i\) fixes \(Z_i\) and
maps the flag of \(a=h_{i+1}\) to that of \(g_i\), by
\(J_i a=g_iJ_i\). The other outer vertex uses
\(h_{i+1}^{-1}=r_{Q_i}r_{W_-}\): \(r_{W_-}\) fixes
\(U_{i-1}^-\), and the inverse-Hurwitz relation in the proof of
(7) maps the remaining flag to \(U_i^+\).
For the second shaded pairing use
\(h_{i+1}J_i^{-1}=J_i^{-1}g_i\) and
\(P_i=g_i g_{i+1}^{-1}\), with \(J_i\) commuting with \(P_i\).
They give the crossing-circle vertex and both outer vertices in
the second line of (12).

Three distinct ideal vertices determine the orientation-preserving
hyperbolic face isometry uniquely. Equations (12) are precisely the
cross-copy, outer-label-swapping shaded gluings in the literal
half-twisted source geometry. This checks ALL \(2s\) shaded
pairings, not only one per crossing circle.

The white generators and (11) are words in the actual main and
auxiliary meridians: \(J_i=-P_i C_i^{-1}\).
Conversely the actual meridians are words in these face generators.
The same labeled oriented cellulation is therefore developed by
our source representation and by the complete geometric face
pairings. Its oriented fundamental Bloch regulator is exactly
\(V_s\). This is the needed absolute geometric anchor.

Here is also an explicit check of the reverse traversal used in
section3. The HOLOMORPHIC Mobius isometry

\[
 F(\zeta)=\rho^2/\zeta                              \tag{13}
\]

acts by
\(Z_k\mapsto Z_{-k}\),
\(U_k^+\mapsto U_{-k-1}^-\),
\(U_k^-\mapsto U_{-k-1}^+\).
It sends \(Q_k\) to \(Q_{-k-1}\), interchanges \(W_+,W_-\),
and sends \(T_k^+\) to \(T_{-k}^-\) and conversely.
Conjugating the literal cross-copy, outer-label-swapping shaded
pairing by \(F\) gives the inverse of that SAME pairing at
\(-k\), not a pairing with the opposite half twist. Since (13)
is holomorphic, it preserves the hyperbolic orientation.
Thus the right-to-left traversal forced by the source cap indices
has the exact same oriented geometric anchor, rather than its
mirror or a different permutation of the source boxes.

The [independent cusp lattice](actual_augmented_pretzel_crossing_circle_cusp.md)
and the absolute peripheral translation calculation in the local
mixed-character note identify \(P_i\) with the primitive disk
longitude and \(C_i\) with the positive-diagonal meridian. They
retain the SL longitude sign \(-L_i^{-1}\); a metric ratio alone
would not fix that marking.

## 5. Scope

The result supplies a regular, source-compatible representation
lift and its actual complete geometric anchor. The geometric
meaning of the SOURCE ACTION also requires a regulator comparison,
not just these matrices or their cusp shapes. Its separate proof
can use the actual peripheral Bloch boundary formula, the anchor
above, and a finite filling-chain comparison. Neither faithfulness
of every deformed representation nor a filled-volume equality is
asserted just from (9).
