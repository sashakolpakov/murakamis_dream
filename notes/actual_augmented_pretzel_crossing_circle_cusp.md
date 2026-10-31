# The crossing-circle cusp lattice, including its half-twist marking

29 October 2026. The explicit face-labeled antiprism geometry gives
the crossing-circle cusp shape without an additional factor two.
Put \(c=\cos(\pi/s)\). In the positive diagonal half-twist marking,

\[
 \boxed{\qquad \tau_{\mathrm{std},+}
       =\frac{2ic}{1+ic}
       =\frac{2c^2+2ic}{1+c^2}.\qquad}                 \tag{1}
\]

The opposite half twist has
\(\tau_{\mathrm{std},-}=2ic/(1-ic)\), whose real part is
negative and whose imaginary part is the same. At \(s=3\), these
are \(\pm2/5+4i/5\). The untwisted marked shape is \(2ic\).
These statements concern the crossing-circle cusps, not the main
component cusp.

The words “positive diagonal” specify the peripheral marking below.
The metric face pairing alone does not distinguish the two half twists:
they differ by a full twist. Consequently (1) is not, by itself, a
proof that an independently defined quantum logarithm is the preferred
longitude, or a proof of its sign convention. It gives an explicit
two-path calibration for making that comparison.

## 1. Compute one actual horospherical rectangle

Use the explicit \(\mathcal P_s\) in
[the geometric-volume proof](actual_augmented_pretzel_geometric_volume.md).
Set \(\alpha=\pi/s\), \(t=\tan(\pi/4-\alpha/2)\), and
\(\rho=t^{-1/2}\). Before doubling the antiprism its ideal vertices
in the complex boundary are

\[
 Z_k=\rho e^{2ik\alpha},\qquad
 U_k^+=\rho^{-1}e^{(2k+1)i\alpha}.
\]

Reflection across the base circle \(|z|=\rho\) gives the other
half of the doubled polyhedron:
\(U_k^-=\rho^3e^{(2k+1)i\alpha}\).
The four neighbors of \(Z_0=\rho\) are \(U_{-1}^{\pm},U_0^{\pm}\).
Send \(Z_0\) to infinity by the holomorphic Mobius map
\(m(z)=1/(z-\rho)\). Their images form a Euclidean rectangle.

For an explicit calculation put \(A=\rho^2=(1+\sin\alpha)/\cos\alpha\).
The lower left and lower right corners are

\[
 m(U_0^+)=-\frac{\rho A}{\sin\alpha(1+A^2)}
                   -i\frac{\rho}{\sin\alpha(1+A^2)},
\]
\[
 m(U_0^-)=\frac{1}{\rho\sin\alpha(1+A^2)}
                   -i\frac{\rho}{\sin\alpha(1+A^2)}.
\]

The other two are their complex conjugates. Hence the width and
height are

\[
 W=\frac1{\rho\sin\alpha},\qquad
 H=\frac{2\rho}{\sin\alpha(1+A^2)},\qquad
 \boxed{H/W=\frac{2A}{1+A^2}=\cos\alpha=c.}           \tag{2}
\]

Since all incident faces are vertical planes after this Mobius map,
their intersections with any horosphere about infinity give exactly
this rectangle, up to its common Euclidean scale. Its vertical sides
are the shaded \(T_0^+,T_0^-\) faces. Its horizontal sides are the
white \(Q_0,Q_{-1}\) faces. Normalize by \(W\) and translate to
the rectangle \([0,1]\times[0,c]\).

There are exactly TWO such rectangles at this cusp, one from each
projection polyhedron. There are not four cusp rectangles merely
because the whole three-manifold contains four antiprisms: doubling
across a base merges the two half rectangles into the one just
computed.

## 2. Develop the exact face pairings

Keep rectangle 0 at \(x+iy\), \(0\leq x\leq1\),
\(0\leq y\leq c\). White gluing by the original vertex labels
develops rectangle 1 as

\[
 x+iy\longmapsto x+i(2c-y).
 \tag{3}
\]

It lies in \([0,1]\times[c,2c]\). The two white identifications
therefore give the vertical period \(2ic\).

For no half twist, shaded gluing is within each copy and matches
the same outer labels. It identifies its left and right sides at
the same local \(y\), giving period 1. Thus the untwisted lattice
is

\[
 \mathcal L_0=\langle1,2ic\rangle_{\mathbb Z}.
 \tag{4}
\]

For a half twist, the original face pairing switches copies AND
exchanges the two outer labels. In local rectangle coordinates it
sends
\((0,y)_0\mapsto(1,c-y)_1\). In the development (3) its
translation is \(1+ic\). The other shaded pair gives \(1-ic\).
Consequently the half-twisted lattice is

\[
 \boxed{\quad \mathcal L_{\mathrm h}
       =\langle1+ic,1-ic\rangle_{\mathbb Z}
       =\langle2,1+ic\rangle_{\mathbb Z}.\quad}       \tag{5}
\]

Its area is \(2c\), the sum of the two original rectangle areas.

## 3. Identify the meridian and preferred longitude paths

The shaded faces are the two sides of the original twice-punctured
crossing disk. The cusp boundary of that disk runs ALONG their
vertical sides and passes through the two white identifications.
It has translation

\[
 \lambda=2ic.                                      \tag{6}
\]

This is the disk-framed longitude: pushing the crossing circle off
inside its spanning disk has zero linking with the circle itself.
Punctures by the other component do not change that self-linking
calculation. The loop traverses each of the two shaded sides once;
using \(4ic\) would traverse this longitude twice.

A positively transverse local meridian crosses the disk seam once.
In the untwisted marking it has translation 1. In the positive
diagonal half-twist marking it follows the corner path
\((0,0)_0\mapsto(1,c)_1\) in local labels and has

\[
 \mu_+=1+ic.
 \tag{7}
\]

The opposite half-twist marking uses \(\mu_-=1-ic=\mu_+-\lambda\).
Both \((\mu_+,\lambda)\) and \((\mu_-,\lambda)\) are primitive
bases of (5): their oriented parallelogram area is \(2c\).
Equations (6)--(7) prove (1). In particular choosing a half of
\(\lambda\) would not define a curve in (5), and doubling
\(\lambda\) would not give a peripheral basis.

The explicit integer-shear calibration is

\[
 \mu_++p\lambda=1+i(2p+1)c,\qquad
 \mu_-+p\lambda=1+i(2p-1)c.                          \tag{8}
\]

Thus a claimed filling equation must record which of these two
base meridians corresponds to its retained physical half twist.
The original source \(R^{-(2p+1)}\) has a specified braid convention
and a specified kernel integer \(p\). To match it to (8), it is
enough to identify the \(p=0\) corner path and the direction of the
\(p\mapsto p+1\) full twist; one cannot infer that information from
the unmarked ideal triangle isometry alone. Replacing \(R^{-1}\)
by \(R\) changes the half-twist marking by one longitude even
though the complete metric volume is unchanged.

## 4. Comparison with the complete mixed-phase Hessian

If the original mixed-phase coordinates have
\(z=2\log M\), \(\partial G/\partial z=\log L\), and
\(\partial^2G/\partial z_i^2=\tau_s\), then the geometric cusp
shape they predict is \(\tau_{\mathrm{std}}=2\tau_s\), since
\(d\log L/d\log M=2\,d\log L/dz\).
For the stated formal value

\[
 \tau_s=e^{iu_*}\cos u_*,\qquad
 \tan u_*=\sec\alpha,
\]

one gets

\[
 2\tau_s=\frac{2ic}{1+ic},
\]

which is exactly the positive-diagonal shape (1). This independent
geometric calculation excludes the proposed extra factor two.
It does not supply the missing quantum-to-peripheral coordinate
identification or select the half-twist sign by itself.

There is a concrete source sign to check in making that identification.
For the literal auxiliary color \(j=N-h\), put \(H=Q^h\).
The centered auxiliary meridian \(M_{\mathrm{aux}}=-q^j\) has
\(2\operatorname{Log} M_{\mathrm{aux}}=-\operatorname{Log} H\). Thus if a phase calculation uses
\(z=\operatorname{Log} H\) and \(G_z=\operatorname{Log} L_H\), its ratio with this auxiliary
meridian is \(-2G_{zz}\), not \(+2G_{zz}\). The positive sign in
the preceding comparison requires, for example, the dual longitude
\(L_{\mathrm{geom}}=L_H^{-1}\). This is a coordinate/peripheral sign
that must be proved; it cannot be hidden in the rectangle count.

For coverage only, the statement of Theorem 1.1 in
[Purcell--Reid--Stewart](https://users.monash.edu/~jpurcell/papers/GeometryAugLinksSfces.pdf)
records that crossing-circle cusps have two rectangles, that the
longitude uses two shaded sides, and that a half-twist meridian is
a diagonal. No proof from that source is used above.

[Audit](../experiments/audit_actual_augmented_pretzel_crossing_circle_cusp.py)
checks the literal vertex images, labeled face translations, primitive
areas and both half-twist/filling markings at 28 widths.
