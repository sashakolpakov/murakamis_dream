# Two degree-eleven factors of the original recurrence symbol

Private algebraic deduction, 9 November 2026. The degree-22 polynomial
in the zero-free Fourier estimate is a quadratic norm. On the double
cover of its frequency parameter it factors into two explicit
degree-eleven polynomials. Along the real frequency interval their
roots are reciprocal conjugates; one factor has six roots inside the
unit circle and five outside. Thus one factor suffices to determine
the root-distance function in the proved inverse criterion.

All statements below concern the principal symbol of the original
finite recurrence. No identification with a knot's A-polynomial or
with a topological quantum invariant is asserted. No mathematical
numerical evaluation, saved-value arithmetic or frozen-source change
is used.

## 1. Symbol, variables and the square identity

Let \(u\) be the angular Fourier variable and \(t\) the rescaled
frequency. The symbol \(p(u,t)\) is the one in the
[zero-free inverse theorem](research_mixed_next_outer_zero_free_symbol_weights.md).
Write
\[
 x=u/2,\qquad \theta=\pi t,\qquad
 z=e^{iu},\qquad w=e^{i\theta},\qquad v=w^2=e^{2\pi it}.
\tag{1}
\]
Here \(z\) is the variable of the characteristic polynomial; it is
independent of the outgoing source parameter denoted by \(Z\) in
the inverse theorem. For algebraic identities, \(z,v,w\) may be
nonzero complex variables subject to \(v=w^2\).

Retain the exact entire identity from the
[symbol endpoint theorem](research_mixed_next_outer_complex_symbol_endpoint_restriction.md):
\[
 \frac{p(u,t)}{256}=\sin^6x+F(x,\theta)^2,
\tag{2}
\]
where
\[
\begin{split}
 F(x,\theta)={}&4\cos^3x\cos^2(3x+\theta)\cos(2x+\theta)\\
 &+\cos x\sin^2x\cos(2x+\theta)
       +2\cos^2x\cos(3x+\theta)\sin^2x.
\end{split}
\tag{3}
\]
Equation (3) removes the apparent poles of the rational expression
for \(p\). For real \(x,\theta\), the function \(F\) is real.
Moreover
\[
 F(x+\pi,\theta)=-F(x,\theta),\qquad F(0,\theta)=4\cos^3\theta.
\tag{4}
\]
The Laurent expression from the inverse theorem can also be used
without trigonometric variables. Put
\[
\begin{split}
 Q&=2-z-z^{-1},& P&=2+z+z^{-1},\\
 L&=8+P(z^3v+z^{-3}v^{-1}),&
 M&=8+P(z^2v+z^{-2}v^{-1}).
\end{split}
\]
Then
\[
 p(z,v)=(L^2-Q^2)M-(8+z+z^{-1})LQ^2+10Q^3.
\tag{5}
\]
In (5), \(p(e^{iu},e^{2\pi it})=p(u,t)\). These are two
expressions for the same original symbol, with its original carrier.

## 2. Polynomial factorization and its double cover

Define the polynomial
\[
\begin{split}
 B(z,v)={}&(z+1)^3(1+vz^3)^2(1+vz^2)\\
 &-vz^3(z+1)(z-1)^2(1+vz^2)\\
 &-vz^2(z+1)^2(z-1)^2(1+vz^3),
\end{split}
\tag{6}
\]
and, for \(\sigma\in\{+1,-1\}\), put
\[
 \mathscr F_\sigma(z,w)
       =B(z,w^2)-\sigma\,2w^3z^4(z-1)^3.
\tag{7}
\]
Both polynomials have degree eleven in \(z\), leading coefficient
\(w^6\), and constant coefficient one when \(w\ne0\).

**Proposition 1.** The cleared characteristic polynomial satisfies
\[
\boxed{\quad
 R(z,v):=v^3z^{11}p(z,v)
       =B(z,v)^2-4v^3z^8(z-1)^6,
 \qquad
 R(z,w^2)=\mathscr F_+(z,w)\mathscr F_-(z,w).
\quad}
\tag{8}
\]
In particular \(R\) is a polynomial with integer coefficients.
The deck transformation of the double cover exchanges the factors:
\[
               \mathscr F_\sigma(z,-w)=\mathscr F_{-\sigma}(z,w).
\tag{9}
\]

*Proof.* Along the parametrization (1), use the continuous half
powers \(z^{1/2}=e^{iu/2}\). Substitution in (3) gives
\[
 16w^3z^{11/2}F(u/2,\pi t)=B(z,w^2).
\tag{10}
\]
For clarity, the three terms in (3), after multiplication by
\(16w^3z^{11/2}\), are respectively the three terms displayed
in (6). This follows directly from
\[
\begin{split}
 \cos x&=\frac{z+1}{2z^{1/2}},&
 \sin^2x&=-\frac{(z-1)^2}{4z},\\
 \cos(3x+\theta)&=\frac{1+w^2z^3}{2wz^{3/2}},&
 \cos(2x+\theta)&=\frac{1+w^2z^2}{2wz}.
\end{split}
\tag{11}
\]
Also
\[
 i\sin^3x=-\frac{(z-1)^3}{8z^{3/2}}.
\]
Consequently (7) equals
\[
 \mathscr F_\sigma(e^{iu},e^{i\pi t})
   =16w^3e^{11iu/2}
          \{F(u/2,\pi t)+\sigma i\sin^3(u/2)\}.
\tag{12}
\]
Multiplying the two identities (12) and using (2) proves (8).
The substitution identities are algebraic Laurent identities, so
the resulting polynomial identity holds for all nonzero complex
\(z,w\), and hence as a polynomial identity after clearing powers.
Equation (9) follows from (7). The first term of (6) has leading
coefficient \(v^3\) and degree eleven; the other terms have smaller
degree. The constant term is one. This proves all assertions.
\(\square\)

This is literally a norm over a quadratic extension. Over
\(\mathbb Q(v,z)\), adjoining \(w\) with \(w^2=v\) gives
\[
 R(z,v)=\operatorname{Norm}_{\mathbb Q(v,z)(w)/\mathbb Q(v,z)}
       \bigl(B(z,v)-2vwz^4(z-1)^3\bigr).
\tag{13}
\]
On the parameter torus \(v\ne0\), the map \(w\mapsto w^2\)
is an unramified double cover, with the group \(\{1,-1\}\)
acting freely on every fiber. In algebraic terminology it is a
\(\mu_2\)-torsor. Equation (13) concerns this specified parameter
cover; it supplies no additional topological interpretation.

If \(w^2\ne-1\), the two factors have no common root. Indeed their
difference is a nonzero multiple of \(z^4(z-1)^3\). Zero cannot
be a common root because their constant terms are one, while
\[
                \mathscr F_\sigma(1,w)=8(1+w^2)^3\ne0.
\tag{14}
\]

## 3. Root counts and reciprocal conjugation

Fix a real \(0\le t<1/2\), so \(w=e^{i\pi t}\) and
\(\cos(\pi t)>0\). Define
\[
 H_\sigma(u)=F(u/2,\pi t)+\sigma i\sin^3(u/2).
\]
For \(0<u<2\pi\), the imaginary part of \(H_+\) is strictly
positive and that of \(H_-\) strictly negative. At the endpoints,
\[
 H_\sigma(0)=4\cos^3(\pi t)>0,\qquad
 H_\sigma(2\pi)=-4\cos^3(\pi t)<0.
\tag{15}
\]
In particular neither polynomial factor vanishes on \(|z|=1\).

The argument of \(H_+\) increases in total from zero to \(\pi\):
one chooses its continuous argument in \((0,\pi)\) on the open
interval and takes the endpoint limits. No monotonicity of that
argument in between is needed. The total change for \(H_-\) is
\(-\pi\). In (12), the exponential factor contributes \(11\pi\)
and \(16w^3\) contributes no change. Hence the total argument
changes of \(\mathscr F_+\) and \(\mathscr F_-\) along the unit
circle are \(12\pi\) and \(10\pi\), respectively.
The argument principle proves the exact counts:
\[
\begin{array}{c|cc}
 & |z|<1 & |z|>1\\ \hline
 \mathscr F_+(z,e^{i\pi t})&6&5\\
 \mathscr F_-(z,e^{i\pi t})&5&6.
\end{array}
\tag{16}
\]
All counts include multiplicities.

For fixed \(|w|=1\), conjugating (12) on the unit circle gives
the polynomial identity
\[
\boxed{\qquad
 \mathscr F_-(z,w)
   =w^6z^{11}\overline{\mathscr F_+(1/\overline z,w)}.
\qquad}
\tag{17}
\]
The expression on the right means conjugation of the value with
the fixed parameter \(w\); after multiplying by \(z^{11}\) it
is a polynomial in \(z\). Equality on the whole unit circle
proves equality of these polynomials. Thus roots of the two factors
are paired by \(z\mapsto1/\overline z\), with multiplicities.

It follows that the original root-distance function is exactly
\[
\boxed{\qquad
 r(t)=\min_{\zeta:\,\mathscr F_+(\zeta,e^{i\pi t})=0}
                  |\log|\zeta||,\qquad 0\le t<1/2.
\qquad}
\tag{18}
\]
Equation (18) still takes the minimum over all eleven roots. It
does not select one continuous root as the closest root throughout
the frequency interval. The root counts alone would not justify
that stronger assertion.

## 4. What happens at the limiting frequency

At \(t=1/2\), the only possible unit-circle zero of either factor
is \(z=1\): the imaginary parts used above remain nonzero for
\(0<u<2\pi\). Both factors vanish at \(z=1\) by (14).

The order is exactly three. The original square identity has the
Taylor expansion, at this frequency,
\[
 F(x,\pi/2)=-80x^3+O(x^5),\qquad
 \sin^3x=x^3+O(x^5).
\tag{19}
\]
For completeness, the cubic coefficient in (3) is
\(-72-2-6=-80\), using
\(\cos(3x+\pi/2)=-\sin3x\) and
\(\cos(2x+\pi/2)=-\sin2x\).
The coefficient of \(x^3\) in \(H_\sigma\) is therefore
\(-80+\sigma i\), which is nonzero. Since
\(z-1=2ix+O(x^2)\) and the prefactor in (12) is nonzero,
\(\mathscr F_\sigma(z,i)\) has a zero of order exactly three
at one. The product \(R(z,-1)\) has order exactly six there.

The remaining eight roots of \(\mathscr F_+(z,i)\) are off the
unit circle. By continuity of polynomial roots, on some fixed
left neighborhood of \(t=1/2\) they remain separated from it,
while precisely three roots tend to one. On a sufficiently small
such neighborhood the minimum in (18) is attained among those
three roots. This proves \(r(t)\to0\) as \(t\uparrow1/2\),
but supplies no quantitative rate or uniform lower bound.

## 5. Consequence for the current comparison

The inverse theorem gives, at a fixed cutoff \(\alpha<1/2\),
the optimal saving available to its weight class as
\[
 \mathcal J_Z(\alpha)=
 \min_{0\le t\le\alpha}
 \left\{E_Z(0)-E_Z(t)+\int_t^\alpha r(s)\,ds\right\}.
\tag{20}
\]
Here \(E_Z\) is the original outgoing action profile. Equation
(18) expresses the integrand using one explicit degree-eleven
polynomial, and (16) keeps track of which roots lie on each side
of the unit circle. This is an algebraic reduction of (20).

No lower bound adequate for
\(\sup_{\alpha<1/2}\mathcal J_Z(\alpha)>
\mathfrak M_3+E_Z(0)-\Lambda\) has been proved here. Neither the
double cover nor the root counts imply that inequality or the
noncancellation of the complete finite source. The free-boundary
and arbitrary-short-filling requirements remain open.

## Frozen source versions

- Original symbol, zero-free inverse and optimal root integral:
  b499a21141be11650f30b94498626e01383c9493edd670e4ef38e5ec985e11d6.
- Exact square identity and its original carrier:
  a072317a34adf75b02aec9c1d20421e88016820040b73cb9cdaa41468d12aed8.
- Original full-shift finite operator:
  7b11e96c482d3c435e3fac0d9a488d0025aae31e2ec9d806949858031381b84c.
