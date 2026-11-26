# One conic for the principal equations of arbitrary crossing words

Private source algebra, 8 November 2026. This note gives a uniform
parametrization procedure for the principal period equation of every
fixed word in the original crossing and turn operators. It does not
identify the resulting curve with a knot's peripheral polynomial, select
a contributing branch, or bound a finite quantum sum. No numerical
evaluation is used.

## 1. The trace surface and the original conjugations

Use the principal symbols \(X,Y,V\) of the original operators
\(Z_{\rm sp},\mathcal L,\mathcal L_1\), respectively. Their surface is
\[
 S=\{(X,Y,V):(X+Y+V-6)^2+(X-2)(Y-2)(V-2)=0\}.
 \tag{1}
\]
The full-source identities in
[crossing transport, equations (24),(28)](research_current_free_aw_crossing_transport.md)
give the following point maps on this surface:
\[
 r(X,Y,V)=(X,V,8-XV-Y),\qquad
 t(X,Y,V)=(Y,X,8-XY-V).
 \tag{2}
\]
In particular, principal conjugation by \(R^{-1}(\cdot)R\)
acts on coordinate functions by \(f\mapsto f\circ r\), and
conjugation by \(T(\cdot)T\) acts by \(f\mapsto f\circ t\).
These formulas retain the original crossing direction.
For example, \(\mathcal L_{s+1}+qZ_{\rm sp}\mathcal L_s
+q^2\mathcal L_{s-1}=8qI\) gives the first map, and
\(T\mathcal L_1T=\mathcal L_{-1}\) gives the second.

Both maps are polynomial automorphisms of \(S\). Their inverses are
\[
 r^{-1}(X,Y,V)=(X,8-XY-V,Y),\qquad t^{-1}=t.
 \tag{3}
\]
Indeed the equation of \(S\) is
\(X^2+Y^2+V^2+XYV-8(X+Y+V)+28=0\). As a monic
quadratic in \(Y\), its two roots have sum \(8-XV\).
This proves invariance under the replacement in (2); permutations
give the remaining assertions.

Let \(g\) be any fixed composition of \(r,r^{-1},t\). The period
characteristic considered here is
\[
                         b_g=Y\circ g+2.                 \tag{4}
\]
For the weighted transpose with inner power \(n\) and outer power
\(k\), its actual operator is
\(R^{-k}T\mathcal L_nTR^k+2I\). Hence (4) uses
\[
                         g=r^n\circ t\circ r^k.           \tag{5}
\]
The reversal in (5) follows from composition of pullbacks and is
essential. For \(n=k=3\), it gives exactly the polynomial in the
[paired Newton theorem, equation (25)](research_mixed_next_outer_paired_newton_characteristics.md).

## 2. Polynomial parametrization for every word

The conic \(S\cap\{Y=-2\}\) has the parametrization
\[
 \gamma(p)=\bigl(2+(p+1)^2,-2,2+(p-1)^2\bigr),\qquad
                         p=(X-V)/4.                       \tag{6}
\]
Both maps are polynomial and inverse to one another. Define
\[
 (X_g(p),Y_g(p),V_g(p))=g^{-1}(\gamma(p)),\qquad
 a=X_g-2,\quad b=Y_g-2,\quad c=V_g-2.                      \tag{7}
\]
Every coordinate in (7) is an ordinary polynomial in \(p\).

**Theorem 1.** Equation (7) is a polynomial parametrization, with a
polynomial inverse on its image, of the entire curve \(b_g=0\) in
\(S\). Its image is a closed copy of the affine line. Moreover,
\[
                         \Delta_g(p)=abc(a+b)              \tag{8}
\]
is not the zero polynomial.

*Proof.* The first assertions follow by applying the automorphism
\(g^{-1}\) to (6). The inverse on the image is the difference
of the first and third coordinates of \(g(X,Y,V)\), divided by four.

To prove the last assertion, the only singular point of \(S\) is
\(o=(2,2,2)\). In shifted coordinates its equation is
\((a+b+c)^2+abc=0\). If one coordinate vanishes at a singular
point, its gradient equations force all three to vanish. If none
vanishes, equality of the three gradient equations forces
\(a=b=c=u\); the gradient gives \(u=-6\), which does not satisfy
the surface equation. Thus only \(u=0\) is possible.

Every automorphism fixes this unique singular point. The conic (6)
misses it, so the image (7) also misses it. On the other hand, the
zero set of \(abc(a+b)\) in \(S\) consists of the three lines
\[
 a=0, b+c=0;\qquad b=0, a+c=0;\qquad c=0, a+b=0
\]
and the parabola \(b=-a,\ c=a^2\). Every component contains the
singular point. An irreducible closed curve contained in this finite
union must equal one of its components: a proper closed subset of
any of these copies of the affine line is finite. The image (7)
is an infinite closed curve missing the singular point, so it cannot
be contained in that union. This proves (8). \(\square\)

## 3. Return to the actual Newton variables

The original Newton parametrization is
\[
 X-2=\frac{(x-1)^2(z+1)}x,\quad
 Y-2=\frac{(x-1)^2(z+1)}{xz},\quad
 V-2=-\frac{(x-1)^2(z+1)^2}{z}.                            \tag{9}
\]
It is a biregular parametrization of the open part
\(abc(a+b)\ne0\) of \(S\), with domain
\(x\ne0,1\), \(z\ne0,-1\). Its inverse is
\[
                         x=-\frac{c}{a+b},\qquad z=\frac ab.
 \tag{10}
\]
For a direct check, put \(s=a+b+c\). Then
\(s^2=-abc\), \(x-1=-s/(a+b)\), and \(z+1=(a+b)/b\).
Substitution in (9) returns \(a,b,c\). Conversely (9) has the
stated nonzero factors and returns its original \(x,z\) in (10).

**Theorem 2.** For any fixed \(x\ne0,1\), the principal period
roots in the original Newton chart are in bijection with
\[
 H_{g,x}(p):=c(p)+x(a(p)+b(p))=0,\qquad \Delta_g(p)\ne0.
 \tag{11}
\]
Here \(c(p)=V_g(p)-2\), as in (7). The polynomial
\(H_{g,x}\) is never identically zero.
Thus the set is finite, with degree bounded solely by the fixed
word and independently of the quantum level.

*Proof.* The bijection follows from Theorem 1 and (9)--(10).
If \(H_{g,x}\) vanished identically, substituting
\(c=-x(a+b)\) into the surface equation would give
\[
 (a+b)\{(1-x)^2(a+b)-xab\}=0.
\]
Theorem 1 shows that \(a+b\) is not identically zero. Put
\(h=(1-x)^2/x\ne0\). The remaining factor gives
\((a-h)(b-h)=h^2\). A product of two complex polynomials
is a nonzero constant only if both are constants. Then \(a,b,c\)
would all be constant, contradicting the inverse parametrization
in Theorem 1. This proves the claim. \(\square\)

The exclusion \(\Delta_g\ne0\) in (11) must be retained. For a
general word, clearing denominators can introduce roots on the
boundary of this chart. The special \(n=k=3\) calculation has the
stronger denominator result in the
[rational trace theorem](research_mixed_next_outer_principal_rational_trace_locus.md).
No such stronger result is assumed here.

The original signed outgoing characteristic can now be evaluated at
the rational functions (10):
\[
 Z_g(p)=\frac{3x_g-2+(x_g-1)z_g-(x_g-1)^2/z_g}{x_g^2}.
 \tag{12}
\]
Equations (11)--(12) give a uniform procedure for forming the common-root
test for every fixed crossing word, using the same signed outgoing
equation. They do not prove that the actual outgoing parameter avoids
this image. A degree bound alone also gives no uniform separation of
roots, no lower bound on a resultant, and no bound on an ordered finite
operator inverse. In particular, this algebraic reduction does not
establish stability under short partial fillings.

## Sources

The exact crossing and turn identities are used at source hash
`f81b9fc3edc2504c5250ad283bf0ceff191a1fc3a310c00fdb57602362f0bf4a`.
The Newton chart and signed outgoing characteristic are used at
`8372ed7387b7465b6a66cc207f2ac8e3803e3def10d7beff115c038d4334c909`.
This is an algebraic consequence of those identities, not a novelty
claim about trace-coordinate descriptions of rational tangles.
