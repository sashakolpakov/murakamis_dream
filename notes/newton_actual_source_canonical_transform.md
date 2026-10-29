# The actual Newton source and its quantum canonical transform

This note gives a generic Newton-index recurrence for the **actual** knot
source, a finite pointing that determines it, and an exact selected-period
formula. It also proves an explicit quantum birational transform and its
classical canonical map. The classical map resolves a signed complete
boundary point into the cut curve. No geometric-support or volume
asymptotic assumption enters these statements.

The final unresolved issue is selection and control of a geometric
coefficient branch in the actual selected sum. An arbitrary root solution
of the operator is insufficient.

## 1. Actual input and Newton interpolation

Use the conventions of [the actual Fourier--Mellin source](fourier_mellin_actual_source.md):
\(Q_N=\exp(2\pi i/N)\), \(Y=M^2\), and the actual reduced periods satisfy

\[
 F_N(Q_N^j)=C_j(Q_N)\quad(1\le j\le N),\qquad
 F_N(1)=C_N(Q_N)=\langle K\rangle_N.                \tag{1.1}
\]

Here \(C_j(Q)\) are the actual finite-color Laurent polynomials over the
recorded rational coefficient field, not a replacement state. Only fixed
small colors will be needed as initial data. Whole reciprocity
\(F_N(Y)=F_N(Y^{-1})\) is proved in
[actual Weyl descent](actual_weyl_descent.md). A nonzero all-level
operator over \(\mathbb Q(Q,Y)\) is proved in
[squared-meridian descent](even_meridian_norm_descent.md).

For generic \(Q\), put

\[
 a_j=Q^j+Q^{-j},\qquad
 t_n(X)=\prod_{r=1}^n(X-a_r),\qquad
 v_n(Y)=(1-Y)t_n(Y+Y^{-1}).
\]

The nodes \(a_1,a_2,\ldots\) are distinct in \(\mathbb Q(Q)\).
Define the universal rational Newton coefficients by

\[
 \boxed{c_n(Q)=
 \sum_{j=1}^{n+1}
 \frac{C_j(Q)}
      {\prod_{\substack{1\le r\le n+1\\r\ne j}}(a_j-a_r)}.}        \tag{1.2}
\]

This is the divided difference at the first \(n+1\) nodes; \(c_0=C_1=1\).
Newton interpolation proves the exact identity

\[
 \boxed{C_m(Q)=\sum_{n=0}^{m-1}c_n(Q)t_n(a_m)}
 \qquad(m\ge1).                                    \tag{1.3}
\]

For completeness, subtract the degree-\((m-2)\) interpolant at the first
\(m-1\) nodes. Its difference from the degree-\((m-1)\) interpolant
vanishes at these nodes, and hence is a scalar multiple of \(t_{m-1}\).
Evaluation at the last node gives its scalar, equivalently (1.2).
Induction proves (1.3).

The formal series

\[
 \mathscr F(Q,Y)=\sum_{n\ge0}c_n(Q)t_n(Y+Y^{-1})                    \tag{1.4}
\]

is interpreted in the Newton completion, not as an asserted analytic
series. Evaluation at \(Y=Q^m\) is finite: all terms \(n\ge m\) vanish.
Thus it has exactly the actual fixed-color values \(C_m(Q)\).

## 2. Exact generic coefficient operators

Let \(T f(Y)=f(QY)\), and put

\[
 X=Y+Y^{-1},\quad S=T+QT^{-1},\quad
 Z=YT+QY^{-1}T^{-1}.
\]

The generic banded identities proved directly in
[whole-source Newton transport](whole_source_newton_transport.md) are

\[
 Xv_n=v_{n+1}+(Q^{n+1}+Q^{-n-1})v_n,
\]

\[
 Sv_n=(Q^{n+1}+Q^{-n})v_n+\delta_n v_{n-1},
\]

\[
 Zv_n=Q^{n+1}v_{n+1}+(1+Q)Q^{2n+1}v_n
                         +Q^n\delta_n v_{n-1},
\quad
 \delta_n=Q^{-2n}(1-Q^{2n})(1-Q^{2n+1}).             \tag{2.1}
\]

Use the bilateral index quantum torus

\[
 u c_n=Q^n c_n,\qquad E c_n=c_{n+1},\qquad Eu=QuE.
\]

Coefficients with negative index are set to zero. Set

\[
 d(u)=Q^{-2}u^{-2}(1-Q^2u^2)(1-Q^3u^2).
\]

The coefficient action, including the shifts of \(n\), is

\[
 \boxed{\widehat X=E^{-1}+Qu+Q^{-1}u^{-1},}                       \tag{2.2}
\]

\[
 \boxed{\widehat S=Qu+u^{-1}+d(u)E,}                             \tag{2.3}
\]

\[
 \boxed{\widehat Z=uE^{-1}+(1+Q)Qu^2+Qu\,d(u)E.}                  \tag{2.4}
\]

These preserve sequences supported on \(n\ge0\). In particular the possible
output at \(n=-1\) from the \(E\) term vanishes because \(d(Q^{-1})=0\).
This boundary fact is required: replacing unilateral shifts by invertible
ones without checking the boundary would not define an exact transform.

For any finite combination \(f=\sum_n c_n v_n\), (2.1) proves

\[
 A f=\sum_n(\widehat A c)_n v_n,\qquad A=X,S,Z.                    \tag{2.5}
\]

It also holds for the Newton completion because each output coefficient
uses only finitely many neighboring input coefficients.

### Generating-function form

Let \(\mathcal C(z)=\sum_{n\ge0}c_n z^n\), and
\(D_z\mathcal C(z)=\mathcal C(Qz)\). The same action is

\[
 \boxed{\mathcal X=z+QD_z+Q^{-1}D_z^{-1},}                       \tag{2.6}
\]

\[
 \boxed{\mathcal S=QD_z+D_z^{-1}
     +z^{-1}\big(D_z^{-2}-(1+Q)+QD_z^2\big),}                    \tag{2.7}
\]

\[
 \boxed{\mathcal Z=QzD_z+(1+Q)QD_z^2
     +z^{-1}\big(D_z^{-1}-(1+Q)D_z+QD_z^3\big).}                 \tag{2.8}
\]

Each bracket multiplying \(z^{-1}\) kills a constant. Thus these preserve
formal power series; there is no omitted constant-term source. The finite
pointing in section 4 supplies the actual source data.

## 3. The transformed recurrence is actual at generic \(Q\)

As proved in [whole-source Newton transport, section 6](whole_source_newton_transport.md),
the actual all-level annihilator may be made nonzero and invariant under

\[
 \theta(Y)=Y^{-1},\qquad \theta(T)=QT^{-1}.
\]

Its fixed algebra is generated by \(X,S,Z\). Fix such an actual operator
\[
 R=R(Q;X,S,Z)\ne0
\]
annihilating \(f_N=(1-Y)F_N\), and form
\[
 \widehat R=R(Q;\widehat X,\widehat S,\widehat Z)
            =\sum_{k=p}^{r}b_k(Q,u)E^k.                         \tag{3.1}
\]

Then the coefficients (1.2) satisfy the **generic exact recurrence**

\[
 \boxed{\sum_{k=p}^{r}b_k(Q,Q^n)c_{n+k}(Q)=0
        \quad(n\ge0),\qquad c_j=0\ (j<0).}                     \tag{3.2}
\]

### Proof by the actual whole source, not an off-root lift

At a fixed root \(Q_N\), write the actual reciprocal Laurent polynomial
as a polynomial in \(X\):

\[
 F_N(Y)=\sum_{m=0}^{D_N}c_m^{(N)}t_m(Y+Y^{-1}).
\]

The monic Newton polynomials remain a basis even if some nodes coincide.
For a fixed \(m\), take \(N>2(m+1)\). The first \(m+1\) nodes are then
distinct, so their actual values (1.1) give

\[
 c_m^{(N)}=c_m(Q_N).                                             \tag{3.3}
\]

Apply the exact root operator \(R\) and extract a fixed output coefficient
\(n\) using (2.1). Only finitely many indices \(n+k\) occur. For every
sufficiently large \(N\), all their coefficients are given by (3.3), and
there are no coefficient poles. Consequently the rational function

\[
 H_n(Q)=\sum_k b_k(Q,Q^n)c_{n+k}(Q)
\]

vanishes at infinitely many distinct \(Q_N\). It is identically zero.
This proves (3.2) for every fixed \(n\). No uniform limit in \(n,N\) and no
claim of reciprocity for an arbitrary off-root matrix lift are used.

### Exact finite-root folding and its corner

At \(Q=Q_N\), set \(U=Y^N\), \(W=U+U^{-1}-2\). If the actual finite Newton
coefficients are collected as

\[
 C^{(N)}(z)=\sum_m c_m^{(N)}z^m
           =\sum_{s=0}^{N-1}z^s C_s^{(N)}(z^N),
\]

then the exact folded whole source is

\[
 f_N=\sum_{s=0}^{N-1} C_s^{(N)}(W)v_s.                           \tag{3.4}
\]

This is \(v_{s+N}=Wv_s\); it retains the entire central corner. The finite
matrices of \(X,S,Z\), including \(Wv_0\) in their last columns, are those
of the whole-source transport note.

Equation (3.3) concerns fixed indices and sufficiently large levels.
It does **not** assert \(c_m^{(N)}=c_m(Q_N)\) simultaneously for every
\(m<N\). At colliding nodes the latter expression can have poles, and
whole parameter jets must be retained.

There is an exact confluent extraction rule for the actual root
polynomial \(P_N(X)=F_N(Y)\):
\[
 c_m^{(N)}
 =\sum_{\alpha}
   \operatorname{Res}_{X=\alpha}
       \frac{P_N(X)}{t_{m+1}(X)}\,dX,                           \tag{3.5}
\]
where the sum runs over the distinct first \(m+1\) nodes, with their
multiplicities retained in the denominator. To verify it, expand \(P_N\)
in the Newton basis. Terms of index below \(m\) have no \(X^{-1}\)
coefficient at infinity; the term of index \(m\) has coefficient \(1\);
higher terms are divisible by \(t_{m+1}\) and have no finite residues.
Repeated nodes therefore demand whole source jets rather than division
by zero. For \(m<N\) their multiplicities are at most two, so values and
first \(X\)-derivatives suffice. The last node at \(m=N-1\) includes
\(X=2\), whose value is the selected period; this rule does not compute
that missing value from nonidentity ordinary-root values.

## 4. Finite pointing and the selected Newton period

The generic recurrence (3.2) determines its actual solution from finitely
many fixed colors. Here is a direct bound.

Left-multiply \(\widehat R\) by \(E^{-p}\), so its shifts are \(0,\ldots,d\),
where \(d=r-p\). Clear a common coefficient denominator in \(Q\) and write

\[
 \widetilde R=\sum_{j=0}^d B_j(Q,u)E^j,\qquad
 B_j\in\mathbb Q[Q^{\pm1},u^{\pm1}],\quad B_d\ne0.                \tag{4.1}
\]

The resulting recurrence is valid when \(n\ge\max(0,p)\).
Let \(A_*\) be the \(Q\)-exponent span in the collected support of \(B_d\).
For every integer \(n>A_*\), \(B_d(Q,Q^n)\ne0\) identically: a collision
between monomials \(Q^a u^b\), \(Q^{a'}u^{b'}\), with \(b\ne b'\),
would require \(n=|a-a'|/|b-b'|\le A_*\). Terms with equal \(b\) do not
collide after collection.

Choose \(n_*\ge\max(0,p,A_*+1)\). The finitely many coefficients
\[
 c_0,\ldots,c_{n_*+d-1}
\]
propagate rationally to all later indices. They require only the fixed
ordinary colors \(C_1,\ldots,C_{n_*+d}\) through (1.2).
For \(d=0\), the recurrence instead forces the tail \(c_n=0\) for
\(n\ge n_*\). Thus no assumed order or regular-singular condition at
\(n=0\) is needed.

The selected period is now the following **whole regular evaluation**:

\[
 \boxed{\langle K\rangle_N=
 \left[
 \sum_{n=0}^{N-1}c_n(Q)
 \prod_{j=1}^{n}
   \big(Q^N+Q^{-N}-Q^j-Q^{-j}\big)
 \right]_{Q=Q_N}.}                                             \tag{4.2}
\]

Indeed the bracketed rational expression is exactly \(C_N(Q)\) by
(1.3), and \(C_N(Q)\) is Laurent polynomial. It is regular at \(Q_N\),
with value (1.1). This formula uses the actual finite pointing and actual
operator. No new levelwise normalization is free.

One must not replace (4.2) by
\(\sum_{n<N}c_n(Q_N)t_n(2)\) unless the individual \(c_n\) are known regular
there. Equation (4.2) first combines the whole germ, including all
coefficient poles and cancellations.

### Uniformly bounded parameter jets

Let \(D_*\) be the \(u\)-exponent span and \(s_*\) the number of monomials
of \(B_d\). For all sufficiently large \(N\), the nonzero Laurent polynomial
\(B_d(Q_N,u)\) has at most \(D_*\) zeros among a segment of fewer than \(N\)
distinct orbit points \(u=Q_N^n\). Each nonzero substituted Laurent
polynomial \(B_d(Q,Q^n)\) has at most \(s_*\) monomials. Its vanishing
multiplicity at any nonzero \(Q\) is at most \(s_*-1\): otherwise its first
\(s_*\) logarithmic derivatives give a Vandermonde system in its distinct
integer exponents.

The recurrence propagation needed to produce \(c_0,\ldots,c_{N-1}\)
therefore has total pole budget at \(Q_N\) bounded by

\[
 \boxed{B_*=D_*(s_*-1),}                                       \tag{4.3}
\]

outside finitely many levels where a fixed coefficient or initial
denominator has a pole. Multiplication by the analytic weights in (4.2)
does not increase it. A common propagation denominator gives a numerator
whose prescribed vanishing cancels these poles, so a \(Q\)-jet of order
at most \(B_*\) of the fixed initial data suffices for the regular value.
This includes tangencies of the moving orbit \(u=Q^n\), not merely zeros
of \(B_d(Q_N,u)\).

## 5. Exact quantum birationality

Let \(\mathcal Q\) be the generic quantum torus generated by \(Y^{\pm1}\)
and \(T^{\pm1}\), \(TY=QYT\), and let \(\mathcal A=\mathcal Q^\theta\).
The assignments (2.2)--(2.4) give an injective homomorphism

\[
 \psi:\mathcal A\longrightarrow
 k\langle u^{\pm1},E^{\pm1}\rangle/(Eu=QuE).                     \tag{5.1}
\]

To see that it is well defined, a relation in \(X,S,Z\) acts as zero
on every \(v_n\), hence its coefficient action acts as zero on every
finite sequence supported on \(n\ge0\). A finite difference operator
\(\sum a_j(u)E^j\) doing so has \(a_j(Q^m)=0\) for infinitely many \(m\);
each rational function \(a_j\) is zero. Thus the coefficient formulas
respect all relations.

For injectivity, if a quantum-torus element annihilates all \(v_n\), write
it in normal form \(\sum_{a,b}r_{a,b}Y^aT^b\). Since
\(v_n=-Y^{n+1}+\cdots\), the largest \(a\) gives
\(\sum_b r_{a,b}Q^{b(n+1)}=0\) for all \(n\). The Vandermonde system in
the distinct \(Q^b\) makes these coefficients zero. Descend through \(a\).
The element is zero.

Most importantly, the coefficient formulas obey the exact identity

\[
 \boxed{\widehat Z=u(\widehat X+Q\widehat S)-(Q+Q^{-1}).}         \tag{5.2}
\]

Therefore in the quantum division ring

\[
 \boxed{u=(\widehat Z+Q+Q^{-1})
                  (\widehat X+Q\widehat S)^{-1},\qquad
 E^{-1}=\widehat X-Qu-Q^{-1}u^{-1}.}                            \tag{5.3}
\]

The order of the inverse in (5.3) is essential. Its denominator is nonzero
since the \(E^{-1}\) coefficient in \(\widehat X+Q\widehat S\) is \(1\).

These formulas prove an isomorphism of quantum fraction fields, not just
a representation on special states. Here is a short justification that the
fractions exist without importing a structural theorem. The quantum torus
is an Ore domain: to find a common right multiple of nonzero \(a,b\),
choose unknown multipliers in a large monomial square of side \(m\).
There are \(2(m+1)^2\) unknown scalar coefficients and only
\((m+O(1))^2\) output coefficients in \(ar-bs\), so a nonzero solution
exists for large \(m\). The domain property ensures both multipliers are
nonzero. The left argument is identical.

Its fixed subalgebra is Ore too. For \(ar=bs\), with \(a,b\) invariant,
average \(r,s\) with their images under \(\theta\). If the average is
zero, both are anti-invariant; multiply both on the right by the nonzero
anti-invariant \(Y-Y^{-1}\). The resulting common multipliers are
invariant and nonzero. The left version is analogous.
Thus (5.1) extends to fractions, and (5.3) shows its image contains the
entire \(u,E\) quantum division ring.

## 6. Classical characteristic and the canonical chart

At \(Q=1\), write \(e\) for the commuting symbol of \(E\). The transform is

\[
 \boxed{
 x=e^{-1}+u+u^{-1},\quad
 s=u+u^{-1}+(u-u^{-1})^2e,\quad
 z=u(x+s)-2.}                                                  \tag{6.1}
\]

These obey

\[
 x^2+s^2+z^2-xsz-4=0.                                         \tag{6.2}
\]

They are birational coordinates on this Weyl-quotient boundary surface,
with rational inverse

\[
 \boxed{u=\frac{z+2}{x+s},\qquad
        e=\frac1{x-u-u^{-1}}.}                                \tag{6.3}
\]

For a direct converse calculation, put \(u=(z+2)/(x+s)\); then

\[
 (x-u-u^{-1})(s-u-u^{-1})-(u-u^{-1})^2
 =-\frac{x^2+s^2+z^2-xsz-4}{z+2}.
\]

This proves the inverse on the displayed open chart.

On the full boundary torus \(Y,L\), the same chart is

\[
 \boxed{
 u=\frac{YL+1}{Y+L},\qquad
 e=\frac{Y(Y+L)(YL+1)}{L(Y^2-1)^2}.}                           \tag{6.4}
\]

Both functions are invariant under \((Y,L)\mapsto(Y^{-1},L^{-1})\).
They generate its invariant function field, and direct differentiation
gives

\[
 \{\log e,\log u\}=1
 \quad\text{when}\quad\{\log L,\log Y\}=1.                       \tag{6.5}
\]

Thus this is a canonical chart on the quotient. The full boundary torus
generically double-covers it; claiming birationality to the full
\(Y,L\) curve would omit this Weyl cover.

If \(R\) is normalized to have a nonzero classical symbol
\(r(x,s,z)\), then the classical characteristic of \(\widehat R\)
is precisely \(r\) after (6.1). Specialization is valid term by term;
the map on classical function fields is injective, so no nonzero leading
symbol is silently lost. Every curve component meeting the common open
chart is carried birationally to its transformed component. This statement
concerns the symbol of the **actual specified invariant operator**. It
does not assume that its zero set has already been proved to be the
geometric \(A\)-component.

### Exceptional curves and the signed complete point

The chart has explicit exceptional factors

\[
 H_-=e(u-1)^2+u,\qquad H_+=e(u+1)^2+u,\qquad
 x+s=\frac{H_-H_+}{eu^2}.                                     \tag{6.6}
\]

The curve \(H_-=0\) is collapsed to
\((x,s,z)=(2,-2,-2)\), the quotient of \((Y,L)=(1,-1)\);
\(H_+=0\) is collapsed to \((-2,2,-2)\).
Thus the signed complete point cannot be evaluated by substituting into
(6.3). A pulled-back characteristic can contain exceptional factors.
Its proper transform is obtained only after removing components supported
on the exceptional locus, or equivalently restricting to the common
open chart and taking closure.

For a branch

\[
 L=-1+\lambda(Y-1)+O((Y-1)^2)
\]

with finite generic slope, (6.4) resolves its direction to

\[
 \boxed{u=\frac{\lambda-1}{\lambda+1}.}                         \tag{6.7}
\]

The companion resolved coordinate is
\[
 e=\frac{1-\lambda^2}{4}=-\frac{u}{(u-1)^2}.
\]
Both follow by substituting the first-order branch in (6.4), retaining
the quadratic numerator and denominator in \(e\).

If \(\tau=d\log(-L)/d\log Y=-\lambda\), this is
\(u=(\tau+1)/(\tau-1)\). For \(\operatorname{Im}\tau>0\) its image has
imaginary part \(-2\operatorname{Im}\tau/|\tau-1|^2<0\).
This is an algebraic direction calculation,
not a proof that the actual source selects that branch.

## 7. The kernel action and the cut curve

The exact Newton kernel is

\[
 t_n(Y)=(-1)^n Q^{-n(n+1)/2}
                   (QY;Q)_n(Q/Y;Q)_n.                         \tag{7.1}
\]

On a simply connected logarithmic chart, let \(U=\log u\), \(y=\log Y\).
The dilogarithmic kernel potential is

\[
 \mathcal K(U,y)=i\pi U-\frac{U^2}{2}
 +\operatorname{Li}_2(Y)+\operatorname{Li}_2(Y^{-1})
 -\operatorname{Li}_2(uY)-\operatorname{Li}_2(u/Y).               \tag{7.2}
\]

Direct differentiation, using
\(d\operatorname{Li}_2(z)=-\log(1-z)\,d\log z\), gives compatible branches
of

\[
 \frac{\partial\mathcal K}{\partial U}
  =\log(Y+Y^{-1}-u-u^{-1})=-\log e,\qquad
 \frac{\partial\mathcal K}{\partial y}
  =\log\frac{uY-1}{Y-u}=\log L.                                \tag{7.3}
\]

Thus \(d\mathcal K=\log L\,d\log Y-\log e\,d\log u\), another direct proof
of the canonical identity. These are exact local period identities;
no assertion about an actual coefficient asymptotic is used.

If a coefficient phase has adjacent ratio \(e\), the selected sum at
\(Y=1\) has the stationary equation

\[
 e(2-u-u^{-1})=1
 \quad\Longleftrightarrow\quad
 \boxed{e=-\frac{u}{(u-1)^2}.}                                \tag{7.4}
\]

It is exactly the exceptional curve \(H_-=0\) above the signed complete
point. A candidate critical point is therefore the intersection of the
coefficient characteristic with this resolved cut curve.
Equation (7.4) identifies the algebraic stationary equation; it does not
establish existence, domination, phase cancellation bounds, or selection
of any actual coefficient branch.

As a diagnostic only, for \(s=x^2-x-4\), substitution gives

\[
 s-(x^2-x-4)=\frac{(e-1)H_-H_+}{e^2u^2}.
\]

Its proper transform is \(e=1\), and intersection with \(H_-=0\) yields
\(u^2-u+1=0\). This illustrates why exceptional factors must be retained
and then distinguished from the proper transform, rather than discarded
before the source has been resolved.

## 8. What root operator data alone do not select

There is an explicit counterexample to selection from only a root
operator, reciprocity, degree, and nonidentity ordinary-root values.
At each level let

\[
 f_0=1-Y,\qquad f_1=Y^N-Y^{1-N}.
\]

Both are exactly \(J\)-fixed and satisfy
\((S-1-Q_N)f_i=0\). For any scalar \(\varepsilon_N\), put

\[
 F_N^\varepsilon(Y)
 =1+\varepsilon_N\left(
       \frac{Y^N-Y^{1-N}}{1-Y}-1\right).                        \tag{8.1}
\]

The quotient is a Laurent polynomial of degree \(N-1\) in \(X\).
This family is reciprocal, has the same fixed root operator and degree
bound, and obeys

\[
 F_N^\varepsilon(Q_N^j)=1\quad(1\le j<N),\qquad
 F_N^\varepsilon(1)=1-2N\varepsilon_N.                          \tag{8.2}
\]

In particular \(\varepsilon_N=a^N\) can have arbitrary exponential growth
while remaining a proper finite hypergeometric factor. The weighted
source difference is the exact normal class
\[
 (1-Y)(F_N^\varepsilon-1)
       =\varepsilon_N(U-1)(1+Y/U).
\]

This does **not** refute the actual all-level pointing construction.
For every fixed color \(j\), the infinitely many nonidentity values in
(8.2) would force \(C_j(Q)\equiv1\). Actual complete-color compatibility
then requires \(F_N(1)=C_N(Q_N)=1\), excluding
\(\varepsilon_N\ne0\). The generic Newton recurrence and selected
evaluation in sections 1--4 retain precisely this missing cross-level
source condition; levelwise interpolation alone does not.

## 9. Proven outcome and remaining work

For every actual knot state, a specified actual all-level operator and
finitely many fixed small colors determine a generic Newton-index
solution and its selected regular period (4.2), with the bounded parameter
jets in (4.3). The operator transform is quantum birational. Its
characteristic is the actual invariant-symbol characteristic in canonical
coordinates, with an explicit exceptional cut curve at signed completion.

To derive a volume theorem from this construction still requires an
actual-source theorem selecting a geometric proper-transform branch and
controlling its coefficient period, including its regulator normalization
and the contribution to (4.2). None of those selection or dominance claims
follows just from the birational transform.

[The independent audit script](../experiments/audit_newton_actual_source_canonical_transform.py)
checks the exact operator, source, and canonical identities without
ordinary-color extrapolation or numerical asymptotic fitting.
It passes 278 exact checks: 119 coefficient/power-series identities,
17 ordinary and confluent interpolation checks, 21 canonical/kernel
identities, and 121 finite-root source checks at levels \(2,\ldots,12\).
