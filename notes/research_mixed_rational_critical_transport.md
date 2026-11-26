# Rational propagation of the mixed critical equations

Research deduction, 5 November 2026. The critical equations used in the
mixed three/four construction admit a rational parametrization at a
complete endpoint and an invertible rational transfer through each
ordinary vertex. This gives a way to retain the correlations among
reference coordinates when testing the remaining curvature inequality.
It does not establish a nonzero contribution to the finite sum.

The formulas below are deduced from the original logarithmic equations.
Their converses require the stated nonvanishing conditions and the
original logarithmic lifts. All applications to a finite quantum source
in this note are restricted to the two block types already constructed.

## 1. A rational parameter at a complete endpoint

Let the first vertex have type \(3+\alpha\), where
\(\alpha\in\{0,1\}\). Write \(e\) for its private leg,
\(z\) for its attached leg, \(s\) for the adjacent ordinary
leg, and \(u\) for the original auxiliary endpoint coordinate.
Define

\[
 U=e^{2\pi i u},\qquad E=e^{-2\pi i e},\qquad
 Z=e^{-2\pi i z},\qquad S=e^{-2\pi i s}.
\tag{1}
\]

The sign in the definition of \(U\) differs from those in the other
three exponentials. In the notation of the
[height-envelope calculation](research_mixed_selected_boundary_height_envelope.md),
it is \(U=1/W\). The original endpoint equations give

\[
 \begin{split}
 E&=\frac{(1+U)^2}{1-2U+5U^2},\\
 1-EZ&=\frac{(1-EU)(1-E)^\alpha}{U},\\
 (1-EZ)(1-SZ)&=S(1-Z)^{2+\alpha}.
 \end{split}
\tag{2}
\]

The first two equations are the exact eliminations in
[the first-cap critical-point theorem](research_mixed_first_cap_critical.md).
For completeness, the second follows by exponentiating the private
derivative: its exponential is
\((1-EZ)/[(1-E)^\alpha(U^{-1}-E)]\).
The last equation is the attached-leg derivative, including the chirp
\(2\pi i zs\), exponentiated with its zero lift. Thus no imaginary
linear term has been omitted.

Put \(D(U)=5U^2-2U+1\). Solving (2) successively gives

\[
 \begin{split}
 E(U)&=\frac{(1+U)^2}{D(U)},\\
 Z_\alpha(U)&=\frac{1-(1-E(U)U)(1-E(U))^\alpha/U}{E(U)},\\
 S_\alpha(U)&=\frac{1-E(U)Z_\alpha(U)}
 {Z_\alpha(U)(1-E(U)Z_\alpha(U))+(1-Z_\alpha(U))^{2+\alpha}}.
 \end{split}
\tag{3}
\]

These are rational functions, rather than roots proposed at a new
parameter value. Explicit reduced expressions are

\[
\begin{split}
 Z_0(U)&=\frac{6U^3-5U^2+4U-1}{U(U+1)^2},\\
 Z_1(U)&=\frac{29U^4-36U^3+38U^2-20U+5}{(U+1)^2D(U)},\\
 S_0(U)&=\frac{(1-U)(U+1)^4}
 {(7U^2-6U+3)(17U^3-7U^2+7U-1)},\\
 S_1(U)&=\frac{(U-1)(U+1)^6}
 {(17U^3-21U^2+19U-7)(41U^4-34U^3+36U^2-14U+3)}.
\end{split}
\tag{4}
\]

Here the subscript on \(S_\alpha\) denotes the endpoint type; it is
not the notation for the exponential of a moving conditional index in
the height-envelope note. A useful check in the type-four case is

\[
                 1-E(U)Z_1(U)=-\frac{4(1-U)^4}{D(U)^2}.
\tag{5}
\]

**Proposition 1.** Every original endpoint critical point in the
established regular domain satisfies (3)--(4). On the canonical
endpoint branch, \(U\) is a valid local coordinate in place of the
neighboring exponential \(S\).

*Proof.* The identities follow by solving (2), with denominators
nonzero at an original critical point. In particular \(U,E,S,Z\)
are exponentials and hence nonzero. The regular sine strips exclude
the products equal to one which occur in their logarithms. The
denominator defining \(S_\alpha\) equals
\((1-EZ)/S\) at that point and is nonzero.

The original endpoint theorem supplies a holomorphic root
\((e(s),z(s),u(s))\) over the neighboring typed input disk. On this
branch the identity
\(S_\alpha(U(s))=e^{-2\pi i s}\) holds. Differentiating it gives

\[
 S_\alpha'(U(s))U'(s)=-2\pi i e^{-2\pi i s}\ne0.
\tag{6}
\]

Both factors on the left are finite, so neither vanishes. The
holomorphic inverse-function theorem proves the local-coordinate
claim. This does not assert global injectivity of \(S_\alpha\)
on the rational parameter line. \(\square\)

In fact the rational maps \(S_0,S_1\) have degrees five and seven.
Thus solving only for an arbitrary preimage of a neighboring
exponential can select a different sheet. Formula (3) simplifies
evaluation on the canonical branch; it does not replace the branch
condition by an arbitrary polynomial root.

## 2. The ordinary vertex as a rational transfer

Consider an ordinary vertex of type \(3+\epsilon\),
\(\epsilon\in\{0,1\}\), and put \(p=2+\epsilon\).
Let \(a,c\) be its left and right external legs, and \(s,b\)
its two own legs in that order. Capital letters denote their
exponentials with the negative sign, as in (1). The original
two-leg equations of
[the universal localization theorem](research_mixed_cyclic_critical_localization.md)
are

\[
 \begin{split}
 (1-AS)(1-SB)&=A(1-S)^p,\\
 (1-SB)(1-BC)&=C(1-B)^p.
 \end{split}
\tag{7}
\]

Solving the first for \(B\) and the second for \(C\) gives

\[
 R_p(A,S)=(B,C),\qquad
 B=\frac{1-A(1-S)^p/(1-AS)}{S},\qquad
 C=\frac{1-SB}{B(1-SB)+(1-B)^p}.
\tag{8}
\]

Work on the open set where these expressions and their reverse
expressions are defined, all four exponentials are nonzero, and
\(1-AS,1-SB,1-BC,1-S,1-B\) are nonzero. These are ordinary
chart restrictions. At an original regular critical point they
follow from the source strips and (7); for example the second
denominator in (8) is \((1-SB)/C\).

**Proposition 2.** The transfer is invertible by rational formulas.
If \(J(A,S)=(S,A)\), then

\[
                         R_p^{-1}=J\circ R_p\circ J.
\tag{9}
\]

*Proof.* From a given \((B,C)\), the same two equations yield

\[
 S=\frac{1-C(1-B)^p/(1-BC)}{B},\qquad
 A=\frac{1-SB}{S(1-SB)+(1-S)^p}.
\tag{10}
\]

These solve the equations in reverse order and are exactly (9).
Substitution proves both inverse identities wherever the stated
denominators are nonzero. \(\square\)

The transfer determines the reference data adjoining the first cap
by taking \((A,S)=(Z_\alpha(U),S_\alpha(U))\). Its first output
is the outgoing reference \(B=e^{-2\pi i t_2}\), and its second
is \(C=e^{-2\pi i s_3}\). This is the inverse reconstruction used
in the endpoint compatibility filter, now expressed rationally in
one endpoint parameter. Both outputs must still satisfy their
appropriate geometric domains and logarithmic equations.

## 3. A two-form preserved by every transfer

The transfer also preserves a rational differential form. Define

\[
 \omega(A,S)=\frac{dA\wedge dS}{AS(1-AS)},\qquad
 \omega_{\rm int}(S,B)=\frac{dS\wedge dB}{1-SB}.
\tag{11}
\]

The first is the form on a boundary pair, and the second is the
form on the two legs of the same ordinary vertex.

**Proposition 3.** On the open set of Proposition 2,

\[
                          R_p^*\omega=\omega.
\tag{12}
\]

*Proof.* Factor the transfer into
\((A,S)\mapsto(S,B)\mapsto(B,C)\). For the first map,
differentiate (8) at fixed \(S\):

\[
 \frac{\partial B}{\partial A}
       =-\frac{(1-S)^p}{S(1-AS)^2}.
\tag{13}
\]

The determinant in the displayed input/output orders is the negative
of this derivative. Since \(1-SB=A(1-S)^p/(1-AS)\), pulling
back \(\omega_{\rm int}\) gives \(\omega(A,S)\).

For the second map, write
\(T=B(1-SB)+(1-B)^p\). At fixed \(B\),

\[
 \frac{\partial C}{\partial S}
       =-\frac{B(1-B)^p}{T^2},\qquad
 C=\frac{1-SB}{T},\qquad 1-BC=\frac{(1-B)^p}{T}.
\tag{14}
\]

Its determinant is again the negative of the displayed derivative.
Dividing by \(BC(1-BC)\) shows that the pullback of
\(\omega(B,C)\) is \(\omega_{\rm int}(S,B)\).
Composition proves (12). \(\square\)

For a familiar coordinate expression, put

\[
                 Y=\frac{AS}{1-AS}.
 \qquad \omega=d\log A\wedge d\log Y.
\tag{15}
\]

Indeed \(d\log Y=d\log(AS)/(1-AS)\). The inverse coordinate
change is \(S=Y/[A(1+Y)]\), with its displayed denominators
retained. Thus both block types act by invertible rational maps
preserving the same nondegenerate two-form. This is an explicit
algebraic property of their classical critical equations, not a
claim about a positive metric for the finite quantum operators.

## 4. An arbitrary mixed chain and the original endpoint marking

For a word of length \(m\ge3\), with endpoint types
\(3+\alpha_L,3+\alpha_R\) and ordinary types
\(3+\epsilon_2,\ldots,3+\epsilon_{m-1}\), start from

\[
 (A_1,S_2)=(Z_{\alpha_L}(U),S_{\alpha_L}(U)),\qquad
 (A_j,S_{j+1})=R_{2+\epsilon_j}(A_{j-1},S_j).
\tag{16}
\]

At an original critical point these are precisely
\(A_j=e^{-2\pi i t_j}\), \(S_j=e^{-2\pi i s_j}\).
Every propagated coordinate is a rational function of \(U\).
All maps in the composition preserve (11), regardless of the
length or order of the two types.

The original right endpoint, read in reverse order, has its own
parameter \(V=e^{2\pi i u_R}\). Its matching conditions are

\[
              A_{m-1}(U)=S_{\alpha_R}(V),\qquad
              S_m(U)=Z_{\alpha_R}(V).
\tag{17}
\]

For length two, the same endpoint matching is used without an
ordinary transfer. These rational equations retain the endpoint
marking. If they are converted to polynomial equations, all
denominators excluded above must remain excluded: multiplying by
them and accepting their zeros would change the problem.

Every actual mixed critical point satisfies (16)--(17). A solution
of the rational equations alone need not solve the original
logarithmic equations, lie in the geometric component, or contribute
to the original integration cycle. No assertion of a unique
algebraic root, a knot A-polynomial, or a nonzero period follows
from this parametrization.

## 5. Use in the outstanding endpoint estimate

For a first type-four cap, equations (3) and (8) express its
correlated reference exponentials \(E_*,Z_*,S_*,B_*\) rationally
in \(U\). They determine the three fixed private heights by
their moduli and determine the original outgoing tangent. The
optimizer equations and curvature numerator in Section 11 of the
[height-envelope note](research_mixed_selected_boundary_height_envelope.md)
can therefore be evaluated without replacing these reference
quantities by independent extrema.

A proof may bound the curvature on a larger parameter set than the
actual word references, provided that set contains every canonical
reference and all its parameter regions are covered. Sampling this
set does not prove a uniform inequality. Nor may a boundary maximum
principle be applied to the optimizing value merely because the
endpoint map is holomorphic: the fixed contour heights are themselves
functions of the reference, and the real optimization retains those
heights. The new formulas simplify that correlated problem; they do
not solve its remaining sign inequality or estimate the other finite
currents.

The algebra in (8)--(14) can be written with other integer exponents.
That formal extension is not an identification with a crossing block
of another power. Only the exponents \(p=2,3\) have been tied here
to the original mixed finite source. An extension to other tangles
requires their exact source formulas and markings.
