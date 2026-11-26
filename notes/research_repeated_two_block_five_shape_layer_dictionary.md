# Five surviving Newton layers for the repeated two-block cap

Research deduction, 8 November 2026. No numerical evaluation is used.

The sharp second capped moment has a concrete five-shape description
coming from the original signed Newton crossing layers. It is different
from choosing positive shapes merely to reproduce a dilogarithm sum.
The resolved original cap, all four crossings, both turns, and the
three flat limiting tetrahedra can be followed explicitly. The five
remaining oriented shapes are positive at the selected maximum, and
their regulator is exactly the absolutely calibrated source action.
The stationary output also closes the literal original parabolic
representation by an exact reversal identity.

This is a layer and regulator dictionary. It does not yet prove that
the flat cap layers can be collapsed relative to their marked boundary,
or that doubling the surviving five cells gives a complete ideal
triangulation of the original knot. Those precise missing attachments
are retained in Section 7.

## 1. The actual source and its original cap parameter

Use the full Newton matrices and closing convention of
[the repeated-block theorem](research_repeated_reflected_block_positive_moments.md).
For \(K_2=(M^2)^*M^2\), the actual vector is
\[
 \beta_N=K_2\mathbf e_0=JM^{-2}JM^2\mathbf e_0.
 \tag{1}
\]
It is the coefficient vector of the literal mixed rational tangle
\[
                       F=T(R^{-2}T(R^2)).
 \tag{2}
\]
Its original positive capped double is
\[
 \begin{split}
 Z_{2,2,N}
 &=\phi(M^2JM^4JM^2JM^3\mathbf e_0)\\
 &=\kappa^3\|\beta_N\|_2^2.
 \end{split}
 \tag{3}
\]
Thus the original positive list is \((2,4,2,3)\), with the
fraction \(29/17\) and original cap convention proved in that
theorem. Neither the cap nor the turn in (1) is a freely chosen
Hermitian observation.

Let \(t_*\in(0,1/4)\) be the unique maximum in Section 6 of
[the complete coefficient packet](research_repeated_two_block_half_interval_packet.md).
Write
\[
 p=e^{2\pi it_*},\qquad u=e^{2\pi ix(t_*)},\qquad
 d=1-u+u^2,\qquad w=u(1-u).
 \tag{4}
\]
The original critical equation and stationarity of the outer norm are
\[
 u^2p-u=(1-u)^3,\qquad
 \frac12<|u|<1,\quad \frac\pi3<\arg u<\frac\pi2,\qquad
 |1-pu|=|1-p|^2.
 \tag{5}
\]
The through-cap parameter of
[the marked mixed-word representation](research_mixed_word_collar_representation.md),
Section 1, is
\[
                         \zeta=1+u^{-1}.
 \tag{6}
\]
Here \(\zeta\) is the original trace of the first two cap
meridians. The actual input cap is the trace triple
\((\zeta,2,4-\zeta)\), resolved in Newton coordinates by
\[
 X_0=q_0\longrightarrow1,\qquad
 V_0=\frac{(q_0-1)^2}{\zeta q_0-q_0^2-1}.
 \tag{7}
\]
The variable \(q_0\) in (7) is a classical resolution coordinate,
not the quantum root. The actual cap matrices and their exceptional
normal are those of
[the original Newton graph, Section 5](actual_newton_twist_canonical_graph.md).
No finite-level cap is replaced by its reduced trace triple.

## 2. All intermediate clocks and momenta

Use the actual signed crossing and turn maps
\[
 \begin{split}
 R(X,V)&=\left(X+\frac{X-1}{V},-X(1+V)\right),\\
 R^{-1}(X,V)&=\left(\frac{XV}{V+1-X},-\frac{V+1}{X}\right),\\
 T(X,V)&=(X^{-1},V^{-1}).
 \end{split}
 \tag{8}
\]
They are fixed by the original finite matrices, not by a
choice of a character-variety convention. Applying
\(R,R,T,R^{-1},R^{-1},T\) to (7) gives
\[
 \begin{array}{c|c|c}
 \text{operation completed}&\text{clock}&\text{momentum}\\ \hline
 R^2&u^{-1}&(1-u)/u\\
 TR^2&u&u/(1-u)\\
 R^{-1}TR^2&u^2/d&-1/[u(1-u)]\\
 R^{-2}TR^2&p^{-1}&d^2/[u^3(1-u)]\\
 TR^{-2}TR^2&p&V=u^3(1-u)/d^2 .
 \end{array}
 \tag{9}
\]
These are exact rational limits. They also follow by substitution
in the full marked cap table of the mixed-word representation.
In particular,
\[
 V=-\frac{1-pu}{(p-1)^2},\qquad |p|=|V|=1.
 \tag{10}
\]
The first equality is an actual outgoing momentum identity.
The second equality for \(V\) uses the outer stationary equation
in (5); it is not imposed at an arbitrary coefficient row.

For completeness, put \(q_0=1+\varepsilon\) in (7). The first
crossing has
\[
 X_1=\zeta-1+\frac{\zeta-2}{\varepsilon},\qquad
 V_1=-q_0(1+V_0)\longrightarrow-1.
 \tag{11}
\]
Thus its clock escapes the Newton torus chart. The second crossing
has finite limits \(X_2=\zeta-1\), \(V_2=\zeta-2\), as in (9).
This escape is retained. It is not a claim that every unfolded
crossing saddle is regular.

All entries in (9) are regular at the selected point.
Indeed \(u\ne0,1\), \(w\) lies in the upper half-plane by
Section 4, so \(d=1-w\ne0\); also \(p\ne0,1\).
These statements exclude the displayed rational divisors.

## 3. The signed two-flip cells and their cap limit

The exact local attachment in
[the two-flip theorem](research_newton_crossing_two_flip_attachment.md)
assigns to a positive crossing with input \((X,V)\) and output
momentum \(U\) the two ordered tetrahedra
\[
 T_{\rm in}=(P,\infty,D,0),\qquad
 T_{\rm out}=(P,-1,D,\infty),
 \quad
 P=\frac{V}{(V+1)(X-1)},\quad D=\frac1{X-1}.
 \tag{12}
\]
In its original shape convention these have shapes
\(-V\) and \(-U\). Their common face cancels with the exact
opposite orientations printed in that theorem. Reading the collar
backwards gives the inverse crossing with both cell orientations
reversed. Both actual boundary quadrilaterals and all their white
transition maps must be carried through each turn.

For the first two positive crossings in (9), the four shape limits are
\[
                      0,\quad1,\quad1,\quad1-u^{-1}.
 \tag{13}
\]
This follows directly from \(V_0\to0\), \(V_1\to-1\), and
\(V_2\to\zeta-2\). The last shape is an even tetrahedral
permutation of \(u\).

For the next two inverse crossings put
\[
 v_0=\frac{u}{1-u},\qquad
 v_1=-\frac1{u(1-u)},\qquad
 v_2=\frac1V.
 \]
Their signed shape list is
\[
                    -[-v_0]-2[-v_1]-[-v_2].
 \tag{14}
\]
The signs here are cell orientations, not absolute values.
Reversing the vertex order of a negatively oriented cell replaces
its shape by its reciprocal. Since
\[
 (-v_0)^{-1}=1-u^{-1},\qquad
 (-v_1)^{-1}=w,\qquad
 (-v_2)^{-1}=-V,
 \]
the five nonflat oriented shape limits of all four crossings are
\[
                         \boxed{u,\ u,\ w,\ w,\ -V.}
 \tag{15}
\]
This is a direct layer dictionary, including its orientation signs.
The three other cells in (13) have zero limiting Bloch--Wigner
regulator. Their faces need not disappear from the relative chain:
zero regulator is not permission to collapse them topologically.

The two-flip theorem supplies actual local face attachments whenever
its incoming boundary is an actual all-white interface. Formulae
(12)--(15) specify the same rational developed cells and cancelling
interior faces on their regular charts. At the initial exceptional
cap, (11) prevents importing that regular-interface theorem without
a separate relative cap construction. This is the unresolved
attachment described in Section 7.

## 4. Positivity of every surviving cell

Write \(u=R e^{i\varphi}\), \(p=e^{i\theta}\). The packet theorem gives
\[
 \frac12<R<1,\qquad \frac\pi3<\varphi<\frac\pi2,\qquad
                       0<\theta<\frac\pi2.
 \tag{16}
\]
The two copies of \(u\) are positive. Moreover
\[
 \Im w=\Im u\,(1-2\Re u)>0
 \]
because \(\Re u=R\cos\varphi<1/2\).
On the unit circle,
\[
 (p-1)^2=-p|1-p|^2,\qquad
 V=\frac{p^{-1}-u}{|1-p|^2}.
 \tag{17}
\]
Hence
\[
 \Im V=-\frac{\sin\theta+\Im u}{|1-p|^2}<0,
 \]
so \(-V\) is positive too. At the maximum \(|V|=1\), but its
positivity does not require that extra equality. None of these
five cells is degenerate.

## 5. The exact regulator, with its constant fixed

Let \(\mathcal D\) be the Bloch--Wigner function, with one positive
ideal tetrahedron of shape \(z\) having volume \(\mathcal D(z)\).
The rational identities
\[
 \begin{gathered}
 f=1-2u+3u^2-u^3,\qquad p=f/u^2,\qquad
 V=u^3(1-u)/d^2,\\
 1-p=-\frac{(1-u)d}{u^2},\qquad
 1-pu=-\frac{(1-u)^3}{u},\qquad
 1+V=\frac f{d^2}
 \end{gathered}
 \tag{18}
\]
prove the regulator identity
\[
 \boxed{\quad
 2\mathcal D(u)+2\mathcal D(w)+\mathcal D(-V)
   =3\mathcal D(u)+2\mathcal D(p)-\mathcal D(pu).
 \quad}
 \tag{19}
\]
Here is a direct normalization check. In the rational multiplicative
group tensored with \(\mathbb Q\), write
\(\alpha=[u]_{\rm mult}\), \(\beta=[1-u]_{\rm mult}\),
\(\delta=[d]_{\rm mult}\), and \(\varphi=[f]_{\rm mult}\);
the sign \(-1\) is torsion. Using
\(\partial[z]=[z]_{\rm mult}\wedge[1-z]_{\rm mult}\),
the boundary of either formal shape sum in (19) is exactly
\[
 2\alpha\wedge\beta-4\alpha\wedge\delta
   +3\alpha\wedge\varphi+\beta\wedge\varphi
   -2\delta\wedge\varphi .
 \tag{20}
\]
For the left side use \(w=u(1-u)\), \(1-w=d\), and
\((-V,1+V)\) from (18). For the right side use the two
complement identities for \(p\) and \(pu\) in (18).

The differential formula
\[
 d\mathcal D(z)
   =\log|z|\,d\arg(1-z)-\log|1-z|\,d\arg z
 \]
therefore makes the difference in (19) constant on the complex
line with its finitely many rational zeros, poles and shape-one
points removed. This domain is connected. At any generic real
\(u\), every argument is real and every regulator is zero.
Thus the constant is zero. No additive real period or numerical
anchor is left unspecified. Equation (20) is used to prove this
real regulator identity, not to assert equality of integral
flattenings or relative fundamental chains.

By the absolutely calibrated identity of the packet theorem,
\[
 2\pi\mathcal S(t)
    =3\mathcal D(u(t))+2\mathcal D(p(t))
                          -\mathcal D(p(t)u(t)).
 \tag{21}
\]
At \(t=t_*\), the sharp original capped rate consequently has the
positive ten-cell regulator expression
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|Z_{2,2,N}|
   =2\{2\mathcal D(u)+2\mathcal D(w)+\mathcal D(-V)\}.
 \tag{22}
\]
The factor two is the actual squared norm in (3), not an
unverified degree of a topological developing map.

## 6. The stationary point closes the original parabolic representation

Let \(c\) be the resolved original cap character (7), with
trace triple \((\zeta,2,4-\zeta)\), and let
\(b=F(c)=(p,V)\). Complex conjugation of a character is
denoted by a bar. The actual maps (8) have real rational
coefficients. With \(T^2=1\), the word (2) satisfies
\[
 F=T F^{-1}T,\qquad
 I:=T\circ\text{complex conjugation},\qquad
 F I=I F^{-1}.
 \tag{23}
\]
These are identities of the actual character maps. They first
hold in the regular Newton chart and extend to the resolved
cap by the original finite parabolic matrix representation.
In that chart,
\[
                  (X,V)\longmapsto
                          (\overline X^{-1},\overline V^{-1})
 \tag{24}
\]
is exactly \(I\). Thus (10) says \(I(b)=b\). Consequently
\[
 F^2(c)=F I(b)=I F^{-1}(b)=I(c),\qquad
                   T F^2(c)=\overline c.
 \tag{25}
\]
In particular the final character in (25) has the original
closing trace \(B=2\), not a newly selected Hermitian boundary
condition.

Here are the cap and word checks behind this conclusion.
At the finite level, \(\phi J=\mathbf e_0^T\), and therefore
\[
 \mu_{2,2,N}=\mathbf e_0^T K_2^2\mathbf e_0
       =\phi[J K_2^2\mathbf e_0],\qquad
 J K_2^2=M^{-2}JM^2JM^{-2}JM^2.
 \tag{26}
\]
This is precisely the literal reflected word in equation (7)
of the repeated-block theorem. Its classical word is \(T F^2\);
the original braid/source identities give the positive capped
word (3), retaining its scalar \(\kappa^3\). Thus (25) uses
the closing turn and cap of the actual source.

For completeness, put \(z=\zeta-2=(1-u)/u\ne0\). The input
matrices from the original Newton graph are
\[
 \mu_1=-\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
 \mu_2=-\begin{pmatrix}1&0\\z&1\end{pmatrix},\qquad
 \mu_3=\mu_2^{-1},\qquad \mu_4=\mu_1^{-1}.
 \tag{27}
\]
Their flags are not all equal, so the ordered quadruple is
irreducible. Every actual signed Hurwitz substitution and
turn preserves irreducibility and the ordered product
relation. These are finite matrix operations throughout:
the escape in (11) is a Newton-coordinate escape, not a
singularity of (27) or of its propagated matrices.

The [faithful cap certificate](actual_parabolic_cap_trace_certificate.md),
in the four-port form of Section 5 of the original Newton
graph, now applies at the final \(B=2\) character. It forces
the literal terminal inverse-pair matrices, not just equal
pair traces. Hence the selected stationary point defines an
irreducible boundary-parabolic representation of the original
capped word \((2,4,2,3)\), with its original meridian marking.
This conclusion concerns its actual reduced character and
matrix relations; it neither removes the finite source's
exceptional normal nor asserts that the representation is
discrete or faithful.

## 7. The remaining marked attachment

Section 6 closes the actual representation. It does not
identify the reflection (24) with a complete gluing of the
two developed five-cell pieces. That still requires the
actual face maps and relative cap attachments.

In particular a complete geometric proof from (15) must supply:

1. The relative cap construction for the three flat layers in
   (13), preserving every boundary triangle, annular end, original
   meridian and closing inverse-pair relation through (11).
2. The labelled gluing of the two five-cell pieces, with all
   face maps, edge links and cusp links of the actual \(29/17\)
   closure. Its derivation must use the original turn and
   Hermitian source identification (1)--(3).
3. The exact edge products and complete cusp translations at
   (5),(10), with the original marking. Positivity in Section 4
   can then invoke the
   [marked positive-gluing theorem](general_marked_positive_gluing_certificate.md).

The existing two-flip table proves local collars on regular eligible
interfaces; it does not silently discharge the exceptional cap or
the doubled boundary in these three items. The source theorem
already provides noncancellation and the full quantum rate.
What remains here is this specific marked geometric realization,
not another estimate of the finite coefficient sum.
