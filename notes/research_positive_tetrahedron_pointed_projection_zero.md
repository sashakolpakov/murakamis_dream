# A positive tetrahedron with a vanishing pointed monomial projection

Private research note, 17 November 2026.

The nonzero rank of a primitive quantum-torus projector, even at a
positive regular tetrahedron, does not imply that it preserves the
distinguished tetrahedron generator. The following exact level-three
calculation disproves that implication. It is not an interior-edge
gluing example and does not show that the generator of an actual knot
triangulation vanishes.

## 1. The original pointed tetrahedron

Use the clock/shift convention of the direct source, Sections 1--2:

\[
 XY=RYX,\qquad (X+Y-1)p=0,\qquad p_0=1.
\tag{1}
\]

Set

\[
 N=3,\quad R=e^{-2\pi i/3},\quad r=e^{-\pi i/3},\quad
 z=-R=e^{i\pi/3}.
\tag{2}
\]

Thus \(r^2=R\), \(r^3=-1\), and \(z\) is the positive regular
tetrahedron shape. Choose any of the three roots \(s^3=-R\), and first
put \(t=s^{-1}\). Then

\[
 s^3+t^3=-R-R^2=1.
\tag{3}
\]

In the ordered basis \(e_0,e_1,e_2\), the literal matrices are

\[
 X=s\begin{pmatrix}1&0&0\\0&R&0\\0&0&R^2\end{pmatrix},\qquad
 Y=s^{-1}\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}.
\tag{4}
\]

Their distinguished vector, without a change of pointing, is

\[
 p=\begin{pmatrix}
 1\\[2pt] [s(1-sR)]^{-1}\\[2pt] s(1-s)
 \end{pmatrix}.
\tag{5}
\]

Indeed the zeroth and first rows of (1) give the last two displayed
coordinates, and the remaining row follows from (3). Equivalently,
these are the recurrence \(p_a/p_{a-1}=t/(1-sR^a)\) and its cyclic
closure. All denominators and all coordinates are nonzero: an equality
\(sR^a=1\) would force \(s^3=1\), contrary to (2).

For completeness, the three central triad shapes of the source are

\[
 Z_0^3=s^3=z,\qquad Z_1^3=t^{-3}=(1-z)^{-1}=z,\qquad
 Z_2^3=-s^{-3}t^3=-(1-z)/z=z,
\tag{6}
\]

where \(Z_0=X,Z_1=Y^{-1},Z_2=-X^{-1}Y\). Thus this is the positive
orientation convention of the original pointed module, not merely a
choice of a nonreal central character.

## 2. A nonzero primitive projector kills the pointing

Let

\[
 U=XY=\begin{pmatrix}0&0&1\\R&0&0\\0&R^2&0\end{pmatrix},
 \qquad U^3=1,\qquad \lambda=R^2.
\tag{7}
\]

The corresponding spectral projector is

\[
 \Pi=\frac13\sum_{a=0}^2\lambda^{-a}U^a
     =\frac13(I+RU+R^2U^2).
\tag{8}
\]

It has rank one. More explicitly, with

\[
 v=(1,R^2,R^2)^{\mathsf T},\qquad \ell=(1,R,R),
\]

one has \(Uv=\lambda v\), \(\ell U=\lambda\ell\), \(\ell v=3\),
and \(\Pi=v\ell/3\). In particular the projector is nonzero; indeed
it is an orthogonal projector for this displayed clock basis.

Nevertheless \(\ell p=0\). To check the exact cancellation, multiply
by the nonzero denominator \(s(1-sR)\):

\[
 \begin{aligned}
 s(1-sR)\ell p
 &=s(1-sR)+R+Rs^2(1-s)(1-sR)\\
 &=s+R+s^3+R^2s^4\\
 &=s+R-R-R^3s=0.
 \end{aligned}
\tag{9}
\]

Consequently

\[
 \boxed{\operatorname{rank}\Pi=1,\qquad \Pi p=0.}
\tag{10}
\]

The monomial exponent of \(XY\) is primitive. In the source's
\((A,B)=(X,Y^{-1})\) lattice it is \((1,-1)\); its rank-one span is
primitive and isotropic. Its order-three character \(\lambda\) is
compatible with its central power. Passing to a Weyl-normalized
monomial only rescales the character and leaves this projector
unchanged. Thus neither primitivity, the compatible character
condition, nor the rank computation excludes (10).

All independent root choices can be retained. Write
\(t=\rho/s\), \(\rho\in\mu_3\), and
\(D_\rho=\operatorname{diag}(1,\rho,\rho^2)\). Then

\[
 Y_\rho=D_\rho YD_\rho^{-1},\qquad
 p_\rho=D_\rho p,\qquad
 X Y_\rho=D_\rho U D_\rho^{-1}=\rho U.
\tag{11}
\]

The projector of the actual monomial \(XY_\rho\) at the same
eigenvalue \(R^2\) is \(D_\rho\Pi D_\rho^{-1}\), and it kills
\(p_\rho\). This covers all nine pairs with
\(s^3=z,t^3=1-z\). If instead the monomial is normalized as
\(XY_\rho/(st)=U\), its vanishing character is \(R^2/\rho\).
No root is changed to select a nonzero projection.

## 3. What the example does and does not establish

It disproves the proposed local inference that positive shapes,
primitive isotropic monomial reduction, and nonzero reduced-module
rank force a nonzero projected distinguished generator. An arbitrary
symplectic diagonalization of the edge lattice must retain the
pointing; its transformed coordinate can vanish as in (9). The
nonzero components of (5) in the original clock basis do not supply
nonzero components in every monomial eigenbasis.

This monomial has not been realized as an actual interior edge with
the original gluing characters. In particular its minimal local
opposite-pair incidence counts are \((a,b,c)=(2,0,1)\): they give
\(X^{a-c}Y^{c-b}=XY\), up to the recorded ordering unit. At the
regular shape their total angle is \(\pi\), not \(2\pi\). No face
pairing or additional incidence data are supplied to complete that
edge, and no claim is made that the selected character is the one
prescribed by such a completion.

Thus an actual triangulation theorem could still use its full edge
incidences, angle sums, and fixed characters to rule out this
cancellation. It would also have to identify its projected tensor
with the original relative quantum source. Neither conclusion follows
from this local example or from nonzero module rank alone. No global
generator counterexample, scalar-period vanishing, or volume claim
is asserted here.

## Direct source and review boundary

The sole direct source is
[Pointed tetrahedron modules and all-level edge reduction](pointed_tetrahedron_gluing.md),
SHA256
`ba91c4be463e38add42b2f8ebc53c3cd3a7e96e97ac4247330dc325e7f6b3a7c`.
Its full text was read for this author cycle. Sections 1--2 fix the
matrices and pointing; Sections 3--6 distinguish primitive projector
rank from the projected generator and retain actual edge characters.
All calculations above are exact written algebra at level three.
