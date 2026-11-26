# The sign of the preferred longitude from a Seifert surface

1 November 2026. Private derivation.

This note fixes the last sign after a squared longitude identity.
It uses the actual preferred boundary curve and a spin lift of the
geometric representation. It does not choose a square root to match
a source formula, and it does not infer a finite eigenvalue identity
from a cusp derivative.

## 1. A frame calculation on a once-bordered surface

Let \(S\) be a compact connected oriented surface of genus \(g\)
with one boundary component. Embed it in an oriented three-manifold
which has a spin structure. Choose a smooth oriented tangent frame
\((e_1,e_2)\) on \(S\), and complete it by the positive unit normal
\(\nu\). Such a tangent frame exists because a surface with
boundary has trivial tangent bundle.

Pulling back the ambient spin double cover along
\((e_1,e_2,\nu)\) gives a double cover of \(S\).
Its monodromy is a homomorphism
\(H_1(S;\mathbb Z/2)\to\mathbb Z/2\).
Since the single oriented boundary is zero in this homology,
the lift of this chosen frame closes after one boundary circuit.

Now replace the first tangent vector on the boundary by its positive
unit tangent \(t\), and the second by the corresponding inward
tangent normal \(n\). Relative to \((e_1,e_2)\), the
frame \((t,n)\) has winding number
\[
                         \chi(S)=1-2g.
 \tag{1}
\]
This is the boundary form of the index formula: extend the outward
boundary normal to a tangent vector field with isolated zeros.
The sum of its indices is \(\chi(S)\); measured in the
global tangent frame, it is the degree of its boundary direction.
The boundary tangent differs from that normal by a fixed quarter
turn, which does not change the degree.

A full \(2\pi\) rotation in the tangent plane is the nontrivial
loop of the oriented three-dimensional frame group. It therefore
changes the sign of a spin lift. Formula (1) is odd. It follows
that the boundary-adapted frame
\[
                              (t,n,\nu)
 \tag{2}
\]
has an antiperiodic lift: after one boundary circuit its lift
returns to the other sheet.

No choice of spin structure changes this conclusion. The only
possible change was the monodromy of the first global frame,
and that monodromy vanishes on the boundary.

## 2. Application to a complete hyperbolic knot cusp

Let \(Y\) be the oriented complete finite-volume hyperbolic complement
of a knot in \(S^3\). Take a sufficiently far cusp torus \(T\).
Its preferred longitude \(\lambda\) is primitive and bounds
a Seifert surface in the truncated complement.
Arrange the boundary of the surface to be the straight Euclidean
representative of \(\lambda\) on \(T\), and arrange its
collar to meet \(T\) orthogonally. These changes are made
inside the ordinary product collar of the boundary torus.

Along that boundary, (2) is a translation-invariant horospherical frame, up to
one constant rotation: \(t\) is the constant longitude
direction, \(n\) is the radial direction, and \(\nu\)
is the constant perpendicular direction in the horosphere.
Thus Section 1 says that the translation-invariant horospherical frame has
antiperiodic spin holonomy along \(\lambda\).

For precision, identify the oriented frame bundle of hyperbolic
three-space with \(\mathrm{PSL}_2(\mathbb C)\), and its
spin cover with \(\mathrm{SL}_2(\mathbb C)\).
Conjugate the cusp fixed point to infinity. If the longitude
translation is \(z_\lambda\ne0\), the path of translation-invariant
horospherical frames is represented by
\[
 U(t)=
 \begin{pmatrix}1&t z_\lambda\\0&1\end{pmatrix},
                         \qquad 0\le t\le1.
 \tag{3}
\]
This is the lift starting at the identity.
Here translation-invariant refers to the cusp's Euclidean translation
group; no assertion of Levi-Civita parallel transport along a
horocycle in hyperbolic three-space is needed.
For a determinant-one holonomy lift \(\widetilde\rho\),
the endpoint of (3) closes in the quotient spin bundle precisely
when
\(\widetilde\rho(\lambda)=U(1)\).
It returns to the opposite sheet precisely when
\(\widetilde\rho(\lambda)=-U(1)\).
The antiperiodicity just proved therefore gives
\[
 \boxed{\displaystyle
 \widetilde\rho(\lambda)=
       -\begin{pmatrix}1&z_\lambda\\0&1\end{pmatrix},
 \qquad
 \operatorname{tr}\widetilde\rho(\lambda)=-2.}
 \tag{4}
\]
Reversing the longitude replaces this matrix by its inverse and
does not change the sign. Any two determinant-one lifts differ
by a character to \(\{\pm1\}\), and the preferred longitude
is zero in the knot complement's first homology, so (4) is
independent of that choice as well.

Here spin existence needs no general three-manifold theorem.
Remove a point of the knot from \(S^3\); its complement is
\(\mathbb R^3\), whose standard tangent frame restricts to \(Y\).
Orthonormalizing for the hyperbolic metric gives a spin structure
on its oriented frame bundle and hence a lift of its geometric
holonomy. The sign calculation itself is the explicit surface-frame
argument above.

## 3. Compatibility with the original augmented representation

Return to the original all-circle construction. Write
\(\mu_K\) for its main meridian and \(\mu_v\) for its
original auxiliary meridians. The original circles are pairwise
unlinked. If \(\ell_v\) is the linking number of circle
\(v\) with the main knot and \(p_v\) is its integral
filling coefficient, the fixed main-boundary word which becomes
the preferred filled longitude is
\[
 \lambda_{\mathrm{fill}}
       =\lambda_K\mu_K^{\sum_vp_v\ell_v^2}.
 \tag{5}
\]
In the augmented exterior its first homology class is
\[
 [\lambda_{\mathrm{fill}}]
      =\sum_v\ell_v[\mu_v]
           +\sum_vp_v\ell_v^2[\mu_K].
 \tag{6}
\]
The original crossing disk is punctured by exactly two main
strands, so
\[
                              \ell_v\in\{0,2,-2\}.
 \tag{7}
\]
Consequently (6) vanishes modulo two.

At an actual complete filled knot point, pull back any
determinant-one lift of its complete holonomy to the augmented
group. Locally this lift continues through the augmented geometric
family: lift the finitely many generator matrices holomorphically;
the signs of the finitely many relations are discrete and remain
their identity values at the initial point.
If another local determinant-one lift is used for the face
construction, its ratio with this lift is a
\(\{\pm1\}\)-valued character: both project to the same
projective representation after one fixed conjugation.
By (6)--(7), that character is one on
\(\lambda_{\mathrm{fill}}\).
Thus any such local face-map lift has exactly the same longitude
sign as the filled lift in (4). A globally rational
determinant-one lift over the entire source variety is not
assumed or needed.

This step is useful because the original matrices of an auxiliary
filling slope may be \(-I\) rather than \(I\). One need not
assume that the particular auxiliary lifts descend to the filled
group. Their possible discrepancy is a character and cannot
change (5).

## 4. Fixing a holomorphic squared longitude identity

Suppose a connected germ of the actual geometric representation,
with its original selected main flag and fixed filling equations,
has already supplied
\[
 L_{\mathrm{geom}}^2
     =M^{2a(D)}
          \prod_e\left(\frac{M^2-X_e}{1-M^2X_e}\right)^2.
 \tag{8}
\]
Assume the factors are holomorphic units on that germ, and define
the longitude coordinate as the inverse eigenvalue on the source
\(M^{-1}\) meridian line. The ratio of the two sides before
squaring is then a holomorphic function taking values in
\(\{1,-1\}\); it is constant on the connected germ.

At the actual complete filled point, \(M=1\).
Each edge factor in (8) is one, since the geometric wire does
not have \(X_e=1\). The inverse selected longitude eigenvalue
is \(-1\) by Sections 2--3. Therefore the constant is negative:
\[
 \boxed{\displaystyle
 L_{\mathrm{geom}}
       =-M^{a(D)}
          \prod_e\frac{M^2-X_e}{1-M^2X_e}.}
 \tag{9}
\]
The conclusion requires the exact squared identity as input.
The complete-value sign fixes only its remaining two-valued
ambiguity; it is not being used to infer the dependence on \(M\)
or on any auxiliary parameter.
