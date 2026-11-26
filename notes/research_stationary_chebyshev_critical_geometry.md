# Global critical-point geometry of the stationary Chebyshev polynomial

Private algebraic lemma, 8 November 2026. No mathematical numerical
evaluation, saved-value calculation, or frozen-source edit is used.

For every positive power, the stationary polynomial has simple zeros.
For powers at least two, all its critical points are also simple and
lie in an explicit upper-half-plane rectangle. These assertions do
not locate the real parts of its critical values.

## 1. Critical points and a dissipative matrix

Use the polynomial from
[the original stationary trace identity](research_two_edge_stationary_chebyshev_trace.md):
\[
 \mathscr P_n(c)=T_n(c)-iU_{n-1}(c),\qquad n\ge1.
 \tag{1}
\]
The Chebyshev normalizations are \(T_n'=nU_{n-1}\) and
\(U_{n-1}(\cos\theta)=\sin(n\theta)/\sin\theta\).
For \(n\ge2\), write \(U=U_{n-1}\); its distinct real zeros are
\[
                  r_k=\cos(k\pi/n),\quad 1\le k\le n-1.
 \tag{2}
\]

**Theorem 1.** Every critical point \(c=x+iy\) of \(\mathscr P_n\)
satisfies
\[
 y>0,\qquad
 \min_k r_k\le x\le\max_k r_k,\qquad
                     y\le\frac{n-1}{n}.
 \tag{3}
\]
For \(n\ge3\), both real inequalities and the upper height
inequality are strict. For \(n=2\), the only critical point is
\(c=i/2\). All \(n-1\) critical points are simple, and their sum is
\[
                    \sum_{\mathscr P_n'(c)=0}c
                                  =i\frac{n-1}{n}.
 \tag{4}
\]

First, \(\mathscr P_n'=nU-iU'\). At a zero of \(U\), its
derivative is nonzero, so that point cannot be critical.
Every critical point therefore satisfies
\[
 \frac{U'(c)}{U(c)}
       =\sum_{k=1}^{n-1}\frac1{c-r_k}=-in.
 \tag{5}
\]
Taking imaginary parts shows \(y>0\). With
\(w_k=|c-r_k|^{-2}>0\), the two real equations are
\[
           x=\frac{\sum_k w_k r_k}{\sum_k w_k},
           \qquad y\sum_k w_k=n .
 \tag{6}
\]
The real bounds in (3) follow. Since
\(\sum_k w_k\le(n-1)/y^2\), the height bound follows too.
For \(n\ge3\) there are at least two distinct \(r_k\);
the positive weighted average is strictly between its extrema,
and equality in the last bound would require all \(r_k=x\).
For \(n=2\), (5) gives the claimed point.

The same equations have an exact finite-dimensional matrix form.
Let \(\mathbf1\) be the column vector of \(n-1\) ones and put
\[
 \mathsf A_n=\operatorname{diag}(r_1,\ldots,r_{n-1})
                            +\frac{i}{n}\mathbf1\mathbf1^T .
 \tag{7}
\]
The determinant lemma, initially away from (2) and then as a
polynomial identity, gives
\[
 \boxed{\quad
 \mathscr P_n'(c)=n\,2^{\,n-1}\det(cI-\mathsf A_n).
 \quad} \tag{8}
\]
Its Hermitian imaginary part is the positive rank-one matrix
\(\mathbf1\mathbf1^T/n\).
Thus (7) is also a direct explanation of the upper-half-plane
location and weighted-average bounds. Formula (4) is its trace,
or equivalently the coefficient comparison in \(nU-iU'\).
The simplicity needed to interpret the sum without multiplicity
is proved next.

## 2. Simplicity and exact values at a critical point

The Chebyshev differential equation is
\[
              (1-c^2)U''-3cU'+(n^2-1)U=0.
 \tag{9}
\]
At a critical point, substitute \(U'=-inU\).
Since (3) excludes \(c=\pm1\), this gives
\[
 \boxed{\quad
 \mathscr P_n''(c)
       =-iU(c)\,
          \frac{1-n^2c^2-3inc}{1-c^2}.
 \quad} \tag{10}
\]
If this vanished, then
\[
                  nc=\frac{i(-3\pm\sqrt5)}2 .
\]
Both possibilities are in the lower half-plane, contradicting
(3). This proves that every critical point is simple.

The identity
\[
                   (1-c^2)U'=cU-nT_n
\]
also gives the exact critical-value formula
\[
 \boxed{\quad
 \mathscr P_n(c)=c(1/n-ic)\,U(c)
       \qquad\text{when }\mathscr P_n'(c)=0 .
 \quad} \tag{11}
\]
In particular no critical value is zero: \(U(c)\ne0\),
\(c\ne0\), and \(1/n-ic\ne0\), the last possible zero being
\(c=-i/n\). Hence \(\mathscr P_n\) has only simple zeros.
For \(n=1\), this conclusion follows directly from
\(\mathscr P_1(c)=c-i\).

For completeness, those zeros also all lie strictly above the
real axis. Let \(\mathsf J_n\) be the real symmetric tridiagonal
matrix with zero diagonal, first off-diagonal entry \(1/\sqrt2\),
and each later off-diagonal entry \(1/2\); for \(n=1\), set
\(\mathsf J_1=[0]\). Expansion of the tridiagonal determinant
gives
\[
 2^{\,n-1}\det(cI-\mathsf J_n)=T_n(c),\qquad
 2^{\,n-1}\det(cI-\mathsf J_n)_{\widehat1,\widehat1}
                                      =U_{n-1}(c).
\]
The empty minor for \(n=1\) has determinant one. Thus
\[
 \mathscr P_n(c)=2^{\,n-1}
       \det\{cI-(\mathsf J_n+i e_1e_1^T)\}.
 \tag{12}
\]
For an eigenvector \(z\ne0\), its eigenvalue has imaginary
part \(|z_1|^2/\|z\|^2\ge0\). Equality would force \(z_1=0\);
the first row and then every successive row force all
coordinates to vanish. This is impossible. Thus every
zero has positive imaginary part. This matrix identity is
algebraic; it is not an identification with an original
quantum crossing operator.

## 3. What these bounds do not establish

The exact symmetries are
\[
 \mathscr P_n(-\overline c)=(-1)^n\overline{\mathscr P_n(c)},
 \qquad
 \mathscr P_n'(-\overline c)
                    =(-1)^{n-1}\overline{\mathscr P_n'(c)}.
 \tag{13}
\]
Thus the critical points are reflected across the imaginary
axis; their values are reflected across the imaginary axis
for odd \(n\), and across the real axis for even \(n\).

At \(n=2\), the sole critical value is \(-1/2\).
At \(n=3\), the two critical values are exactly
\[
                  \mp\frac{5\sqrt5}{27}+\frac{8i}{27},
 \tag{14}
\]
as in [the cubic continuation](research_mixed_next_inner_three_cubic_continuation.md).
Their real parts are less than \(1/2\).

The assertion that every critical value satisfies
\[
                         \Re\mathscr P_n(c)<1/2
 \tag{15}
\]
for all \(n\ge2\) is not proved here.
The weighted-average and height bounds concern the critical
points \(c\), and cannot be substituted into (11) as a bound
for its real part. In particular (3), (10), and (12) do not
yet prove an unramified inverse branch over \(\Re C>1/2\)
for arbitrary \(n\). The adopted \(n=3\) result uses the
explicit values (14).

All matrix identities and location statements above concern
the stationary phase polynomial. They establish no geometric
branch coefficient, finite-source contour estimate, critical
action dominance, or arbitrary-short composition theorem.

