# The Bloch--Wigner value of the actual reduced braid word

Private written proof, 18 November 2026.

At the complete meridian, the literal reduced Euler network has
the same Bloch--Wigner value as the original crossing word at
its corresponding regular semisimple fixed point. The comparison
is a boundary coboundary before closing the word. It is fixed
by a real calibration, rather than by assuming that equality
of canonical graphs fixes their marked holomorphic primitives.

The complete proof directs are G, the actual reduced
correspondence; M, the original signed crossing symbols; and C,
the oriented complete fundamental-cycle comparison. All additional
regulator and calibration arguments are given below. The result
concerns the single-valued Bloch--Wigner function only.

## 1. The literal local sums

Fix the complete principal meridian \(M=1,x=-1\). Use G's
actual finite reduced generators
\[
 \mathcal B(R_i)=R_{i-1}\quad(i\ge2),\qquad
 \mathcal B(R_1)=\kappa S_{m-1}D ,
 \tag{1}
\]
and their exact inverses, with the original scalar lines.
The first-head reduction is the resolved level \(t=0\),
where \(A_1=1+p_1t=1\), with its flag \(p_1\) retained.

For a positive \(S_r\) factor, its literal factorial part has
the Bloch expression
\[
 \beta_S=\sum_{j=2}^r
          \bigl([B_j]+[C_j]-[B_jC_j]\bigr).
 \tag{2}
\]
Here \(B_j\) is the recipient's input occupation clock and
\(C_j\) its transfer clock. The omitted \(-[1]\) has zero
Bloch--Wigner value. The inverse finite coefficient has the
same factorial expression, evaluated on its own inverse
canonical graph. Its additional sign and Gaussian are
\(\pi i\sum\log C_j+\tfrac12(\sum\log C_j)^2\) in the
principal primitive; these are retained, not a reason to
put an extra minus sign in (2). The diagonal \(D\) has
zero Bloch sum.

For an original positive crossing, M gives
\[
 \beta_+=[B]+[C]+[A^{-1}]-[BC]-[C/A],
 \tag{3}
\]
and for its actual negative coefficient
\[
 \beta_-=[A]+[C]+[B^{-1}]-[AC]-[C/B].
 \tag{4}
\]
The variable conventions are those of the corresponding
signed finite coefficients. In particular (4) is not
assigned an additional orientation sign. For any local
expression \(\beta\), write \(\mathcal D(\beta)\) for the
sum of the Bloch--Wigner values of its symbols.

## 2. The boundary differential

For nonzero meromorphic functions without poles on the
chosen chart define the real one-form
\[
 \eta(a,b)=\log|a|\,d\arg b-\log|b|\,d\arg a .
 \tag{5}
\]
It is additive in each multiplicative argument and
antisymmetric. A constant of modulus one contributes
zero. Direct differentiation of
\[
 D(z)=\operatorname{Im}\operatorname{Li}_2(z)
                         +\log|z|\arg(1-z)
 \tag{6}
\]
gives
\[
                  dD(z)=\eta(z,1-z).
 \tag{7}
\]
These formulas are independent of the local argument
branches. They therefore define identities of real
one-forms on the common nondegenerate chart.

Consider a local literal principal expression
\[
 \mathcal S=G+\sum_\nu\epsilon_\nu
                                  \operatorname{Li}_2(z_\nu),
 \tag{8}
\]
where the \(z_\nu\) are monomials in independent clocks
\(X_i\) with modulus-one constants. At the fixed
\(x=-1\), the Gaussian \(G\) has real symmetric
quadratic coefficients in the logarithms, purely
imaginary constant linear coefficients, and a constant.
This is explicit for the \(S_r,D\) expressions in G;
M proves it and the corresponding wedge calculation
for the signed physical crossings.

Since
\(\partial_{\log X_i}\operatorname{Li}_2(z_\nu)
 =-a_{\nu i}\log(1-z_\nu)\), equations (5)--(7) give
\[
 d\mathcal D(\beta)
    =-\sum_i\eta\bigl(X_i,
                       \exp(\partial_{\log X_i}\mathcal S)\bigr).
 \tag{9}
\]
The Gaussian contributes zero to this sum: its symmetric
quadratic matrix pairs with an antisymmetric form, while
its constant linear exponentials have modulus one.
Thus the signs and Gaussians are accounted for in (9).

The canonical differential convention is
\[
 d\mathcal S
   =\sum_{\rm out}\log p'\,d\log A'
                     -\sum_{\rm in}\log p\,d\log A
 \tag{10}
\]
on the local conservation hyperplane. The output clocks
are integral monomials in its independent input and
transfer clocks. Multiplicativity of (5) converts (9)
exactly into
\[
 d\mathcal D(\beta)
   =\sum_{\rm in}\eta(A,p)
                       -\sum_{\rm out}\eta(A',p').
 \tag{11}
\]
This applies to (2), to its actual inverse graph, to
(3)--(4), and to \(D\), whose right side is zero.
For example \(D\) has \(A'=A,\ p'=-Ap\) at \(x=-1\);
then \(\eta(A,p')=\eta(A,p)\).

## 3. Real calibration of the local comparison

Let \(\chi\) denote G's rational canonical map of \(S_m\)
from new variables to original ones. On the new level
\(t=0\), its first position is exactly \(A_1=1\).
For a physical braid generator \(R_i^{\pm1}\), form the
three-block canonical composition
\[
                    \chi^{-1}R_i^{\pm1}\chi .
 \tag{12}
\]
G proves from the literal finite coefficients that its
map on the remaining tuple is the graph of (1) or its
inverse. The new first position stays one; its flag
momentum is allowed to change. No uniform action of
the finite matrix \(S_m\) on its vacuum is used here.

On a common nondegenerate chart define \(\mathcal T_i\)
as the sum of the three Bloch--Wigner expressions in
(12). Define \(\mathcal B_i\) from the literal reduced
generator in (1). All intermediate variables are the
rational ones of G's graphs, in their actual order.
Summing (11) cancels every intermediate boundary term.
The first-head term is zero on this level, since
\[
                         \eta(1,p_1)=0.
 \tag{13}
\]
The remaining input/output terms are the same for
\(\mathcal T_i\) and \(\mathcal B_i\). Consequently
\[
                         d(\mathcal T_i-\mathcal B_i)=0.
 \tag{14}
\]

Here the constant can be determined. Before imposing
the closed-word fixed equations, the new remaining
positions, momenta, and the retained \(p_1\) are free
rational coordinates. The common domain is obtained
by excluding the finitely many zeros and poles in
these maps and in the shapes. It is a connected
Zariski open subset of that rational parameter space.
It is defined over the reals, because \(x=-1\) and all
the canonical formulas of G and M are real rational.

For precision, this open domain is nonempty. Generic
remaining coordinates make every physical crossing
factor regular; a nonzero generic \(p_1\) makes the
first-head \(S_m\) factors regular. The transfer
equations of G show that none of their excluded
numerators is identically zero. Their inverse
conditions follow from the same birational maps.
For \(S_1\) the list is empty. Restricting \(A_1=1\)
introduces no donor factorial in (2). The open set
therefore has a real point: a finite list of nonzero
real polynomials cannot vanish on all real values of
these independent coordinates. It is connected over
\(\mathbb C\), since the complement has complex
codimension at least one in the connected rational
chart; polygonal paths can be perturbed off that
finite algebraic set.

At such a generic real point, every shape in both
expressions is real and different from \(0,1\) and
infinity. The Bloch--Wigner value of a real shape is
zero. Hence the constant in (14) is zero:
\[
                              \mathcal T_i=\mathcal B_i.
 \tag{15}
\]
This determines a single-valued regulator constant.
It does not determine a holomorphic action constant
or its logarithmic deck character.

The same argument applied to
\(\chi^{-1}\chi=I\) proves
\[
 \mathcal D(\beta_{S_m^{-1}})(\chi(z))
                         =-\mathcal D(\beta_{S_m})(z)
 \tag{16}
\]
on its common chart. The minus sign is a consequence
of the inverse graph and real calibration, not a
change to the finite inverse coefficient's sign rule.

## 4. The word coboundary and closure

Follow a finite signed braid word from an initial new
point \(z\) on \(t=0\), retaining its first flag.
Let \(z'\) be the final new point under
\(\chi^{-1}R_\beta\chi\), and write
\(\beta_{\rm red}\) for the sum of (2)--(4) in the
literal reduced network. Equation (15) at every
generator, followed by (16) at the matched interfaces,
gives the exact real-valued identity
\[
 \mathcal D(\beta_{\rm red})
  =\mathcal D(\beta_{\rm original})
    +\mathcal D(\beta_{S_m})(z)
    -\mathcal D(\beta_{S_m})(z').
 \tag{17}
\]
This is the boundary coboundary before closure. It
has not discarded either end of the composition.

Suppose the remaining tuple is a reduced fixed point
and \(K_\Sigma^2\ne1\). G's exact conservation argument
then makes the first flag close as well:
the possible upper-unipotent seam \(s\) obeys
\(s(K_\Sigma^{-1}-K_\Sigma)=0\), so \(s=0\).
Thus \(z'=z\), and (17) proves
\[
               \boxed{\ \mathcal D(\beta_{\rm red})
                              =\mathcal D(\beta_{\rm original})\ }.
 \tag{18}
\]
Without that closing condition, the two displayed
boundary terms in (17) remain.

The common momentum quotient does not change (18).
It conjugates all holonomies diagonally and preserves
the source clocks and every shape in these expressions.
Nor is a new physical cut or a finite support projector
substituted in obtaining (17).

## 5. Resolved geometric limits and the oriented volume

The function \(D\) extends continuously to the sphere,
with value zero at \(0,1,\infty\). For example (6) gives
\(D(z)=O(|z|\,|\log|z||)\) near zero. Differentiating
(7) and checking on a real interval gives
\(D(1-z)=-D(z)\) and \(D(1/z)=-D(z)\); these give the
other two extensions. This uses only the single-valued
function, not a holomorphic logarithm across a divisor.

At a resolved geometric point in G, the relevant
prefixes and the \(S\) partial denominators are units.
Some shapes may equal one, and some ordinary phase
coordinates may then fail. Approximate the point in
the ambient rational chart by the nondegenerate open
set used above. All its shape maps have their
specified resolved limits. Equations (17)--(18)
therefore persist by continuity whenever their
closing conditions hold at the limiting point.
The approximating points need not be fixed points:
the word identity (17) holds before imposing closure.
At the limiting fixed point its two boundary limits
agree. No nearby family of nondegenerate critical
points has been assumed.

For the complete oriented geometric representation
of the knot exterior, C's complete fundamental-cycle
proof identifies the original crossing sum with
the oriented idealized fundamental class. It proves
\[
                  \mathcal D(\beta_{\rm original})
                                =\operatorname{Vol}(M_{\rm knot}).
 \tag{19}
\]
One may approximate the resolved full frame by
generic frames of the same representation. C's
normalized degenerate configurations and the
continuity just explained give the same value in
the resolved frame of G. The source-preserving
presentation changes retained in G leave the
same oriented knot exterior. Combining (18)--(19)
therefore gives the oriented volume as the
Bloch--Wigner value of the actual reduced word at
that complete geometric fixed point.

This is a complete-color comparison. It does not
discard generic-meridian corrections, their first
jets, the original peripheral factors, or the
Fourier characters of the actual source. No equality
of marked holomorphic actions is claimed. A common
analytic amplitude chart, source-contour occurrence,
noncancellation and the asymptotic size of the
specified finite trace remain separate.

## Complete proof-source pins

* G: notes/research_actual_reduced_braid_critical_scheme.md,
  SHA256 ddddcd9bf75f35afdf3e5de0c03323acee2c66e624db36142c2344ef729a977a.
* M: notes/marked_braid_holonomy.md,
  SHA256 eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.
* C: notes/crossing_fundamental_cycle.md,
  SHA256 0d7d7da0f5cf4fe0d16907e7e999d5ce7980f7ff39d437df167c99ca30205b0f.

All three complete sources were freshly read nontruncated
in this active sequence and retained unchanged; every used
implication was checked. The comparison above is a written
proof. No mathematical programs were run, and frozen or
public files were not edited.
