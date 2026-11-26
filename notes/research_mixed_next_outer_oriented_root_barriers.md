# The geometric root in one oriented factor of the symbol

Private algebraic deduction, 9 November 2026. The nearest zero of
the full recurrence symbol is unselected near frequency one half.
The two factors on the parameter double cover distinguish its
orientation: the nearest outer zero of one factor is the selected
geometric branch, while the closer unselected outer zero belongs
to the other factor. This statement does not permit either factor
to be removed from the finite source.

No mathematical numerical evaluation, saved-value arithmetic or
frozen-source edit is used.

## 1. The two factors and their winding-zero normalization

Use the polynomials \(\mathscr F_\pm(z,w)\) of
[the degree-eleven factorization](research_mixed_next_outer_degree_eleven_factors.md).
For \(0\le t<1/2\), put
\[
 z=e^{iu},\qquad w=e^{i\pi t},\qquad
 a_+(u,t)=w^{-3}z^{-6}\mathscr F_+(z,w),\qquad
 a_-(u,t)=w^{-3}z^{-5}\mathscr F_-(z,w).
\tag{1}
\]
These are Laurent polynomials in \(z\) with coefficients depending
on the chosen lift \(w\). The root counts of the cited theorem
give winding zero for each factor as \(u\) runs along its real
period. The normalization removes six and five powers of \(z\),
respectively; it creates no nonzero root.

Their exact product and reality identities are
\[
\boxed{\quad
 p(u,t)=a_+(u,t)a_-(u,t),\qquad
 a_-(u,t)=\overline{a_+(u,t)}\quad(u,t\text{ real}).
\quad}
\tag{2}
\]
Indeed the polynomial product is
\(\mathscr F_+\mathscr F_-=w^6z^{11}p\), and reciprocal
conjugacy gives the second assertion after division by the powers
in (1). Thus on the real torus \(p=|a_+|^2\).

For the entire trigonometric function \(F\) in the factorization
note and \(x=u/2\), the same formulas are
\[
 a_+=16e^{-ix}\{F(x,\pi t)+i\sin^3x\},\qquad
 a_-=16e^{ix}\{F(x,\pi t)-i\sin^3x\}.
\tag{3}
\]
The identity \(F(-x,-\theta)=F(x,\theta)\) gives
\[
                         a_+(-u,-t)=a_-(u,t).
\tag{4}
\]
This reflection exchanges the two factors. It does not say that
either factor alone preserves the original even Fourier space.

## 2. Distances in the two radial directions

The factors have no root at zero or on the unit circle. Define
\[
\begin{split}
 r_\sigma^{\rm out}(t)
   &=\min_{\mathscr F_\sigma(\zeta,w)=0,\ |\zeta|>1}\log|\zeta|,\\
 r_\sigma^{\rm in}(t)
   &=\min_{\mathscr F_\sigma(\zeta,w)=0,\ |\zeta|<1}(-\log|\zeta|).
\end{split}
\tag{5}
\]
Both minima have nonempty finite index sets by the six/five root
counts. They are positive and continuous on every compact frequency
interval below one half, by continuity of polynomial roots and
absence of crossings through the unit circle.

Reciprocal conjugacy proves
\[
 r_-^{\rm out}=r_+^{\rm in},\qquad
 r_-^{\rm in}=r_+^{\rm out},\qquad
 r=\min\{r_+^{\rm out},r_+^{\rm in}\}.
\tag{6}
\]
Here \(r\) is the root distance used for inversion of the full
original symbol. The outward zero-free homotopy for \(a_+\)
alone would instead permit precisely \(\lambda<r_+^{\rm out}\),
since \(u\mapsto u-is\) moves \(z\) to modulus \(e^s\).
This is a statement about its scalar symbol, not yet an inverse
theorem for a factor of the original finite operator.

## 3. The closest roots near one half

Put \(\delta=1/2-t\). The
[endpoint-root theorem](research_mixed_next_outer_symbol_endpoint_roots.md)
proves that the six angular roots approaching zero are
\[
 u_c(\delta)=\frac{2\pi}{3+ic}\,\delta+O(\delta^3),
\tag{7}
\]
for the three roots of
\[
 \mathscr P_3(c)=4c^3-3c-i(4c^2-1)=1,
\]
together with the conjugate branches. The three values are
\[
 c_0=-\tfrac12,
 \qquad c_\pm=\frac{1+2i\pm\sqrt{5-4i}}4,
\tag{8}
\]
with the principal square root. The original selected action uses
\(c_+\).

The three branches (7) with \(\mathscr P_3(c)=1\) belong to
\(\mathscr F_+\). To verify the sign, the scaled endpoint square
has \(k\to ic\) and
\(\mathcal W(ic)=-i\mathscr P_3(c)=-i\), with
\(\mathcal W(k)=4k^3+4k^2+3k+1\). Thus the limiting equation
is \(F+i\sin^3(u/2)=0\). Each limiting root is simple after
scaling, so its continuation belongs to that same factor. The
conjugate branches belong to \(\mathscr F_-\).

For \(c=a+ib\),
\[
 \Im\frac{2\pi}{3+ic}
                   =-\frac{2\pi a}{(3-b)^2+a^2}.
\tag{9}
\]
The endpoint proof gives \(\Re c_+>0\), whereas
\(\Re c_0<0\) and \(\Re c_-<0\). Consequently, among
the three roots of \(\mathscr F_+\) tending to one, precisely
the selected \(c_+\) branch is outside the unit circle:
\(|e^{iu}|=e^{-\Im u}\). The other two are inside. The
remaining eight roots stay uniformly away from the unit circle.

Write \(c_+=A+iB\), with \(A,B\) real, and define
\[
 \gamma_{\rm g}=
       \frac{2\pi A}{(3-B)^2+A^2}>\frac{\pi}{6}
                                      >\frac{4\pi}{37}.
\tag{10}
\]
The first strict bound is proved by the elementary root estimates
in the endpoint theorem; the second is the integer comparison
\(37>24\). Its strict comparison of the two inner slopes also
shows that \(c_0\) is the nearest inner branch. Therefore
\[
\boxed{\begin{split}
 r_+^{\rm out}(1/2-\delta)
     &=\gamma_{\rm g}\delta+O(\delta^3),\\
 r_+^{\rm in}(1/2-\delta)
     &=\frac{4\pi}{37}\delta+O(\delta^3).
\end{split}}
\tag{11}
\]
By (6), the closer outer zero of the full symbol is in the
opposite factor \(\mathscr F_-\). This locates the obstruction
in one specified algebraic factor; it does not remove that factor.

## 4. The finite-source requirement that remains

The proved zero-free inverse estimates the original operator
\(\mathcal C_N\), whose principal symbol is the complete product
\(p\). Its admissible outward widths are still restricted by
both factors in (2). Equations (1)--(11) do not replace that
operator by one with symbol \(a_+\).

Such a replacement would require additional finite algebra and a
source estimate. For example, one possible route would be an exact
factorization of the actual finite operator, together with a
representation of the actual right-hand side in the image of the
other factor and a bound on its preimage. Another would be a
proved lower-order identity for the original observation functional.
Neither property follows from a factorization of the principal
symbol. In either route the original boundary conditions, parity
terms and generated output modes must still be accounted for.

These are possible sufficient mechanisms, not necessary conditions
for cancellation and not established constructions. The result here
is the directional root statement (11), together with the exact
quadratic norm structure that explains why the full-symbol estimate
encounters an unselected branch first.

## Frozen source versions

- Degree-eleven factors, root counts and reciprocal conjugacy:
  b5793f83ec635753a592f6497787f7d11231f9fb15765c0ab6b718f6e4e1351d.
- Endpoint roots, selected cubic and strict slope comparisons:
  aa0a17aec890cfe3951feaafd14a0c35b0d809a348181009e497cdc02dcdee90.
- Original zero-free finite inverse:
  b499a21141be11650f30b94498626e01383c9493edd670e4ef38e5ec985e11d6.
