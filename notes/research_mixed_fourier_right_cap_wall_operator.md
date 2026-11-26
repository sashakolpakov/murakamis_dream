# The exact outgoing contraction and its second-order difference equation

Research deduction, 7 November 2026. The entire outgoing summation in
the Fourier cap can be performed algebraically before taking an
absolute value. Its result is a terminating little \(q\)-Laguerre
polynomial, also called a Wall polynomial. This gives an exact
second-order difference operator for the contracted function. Its
commutative symbol recovers the quadratic already found from the
original critical equations, with the finite index shift retained.

The finite identity includes the troublesome physical region with
large inner index and small outgoing index. It does not estimate
the contracted polynomial or establish that its geometric stationary
contribution survives. In particular, the operator below is an
operator for this boundary contraction, not the knot's peripheral
quantum \(A\)-polynomial.

## 1. Contract the actual outgoing index first

Let \(N\ge2\), \(r=e^{-2\pi i/N}\), and
\[
 P_j=(r;r)_j,\qquad
 (a;r)_j=\prod_{k=0}^{j-1}(1-ar^k),\qquad
 Y=e^{2\pi iy},\quad |Y|<1.
 \tag{1}
\]
The lift \(y\), including the factor involving \(y\) below, is the
original Fourier variable. In the notation of the
[exact outer-contour source](research_mixed_fourier_right_cap_outer_contour.md),
\[
 \begin{split}
 f_l(y)&=\frac{e^{-\pi i(N-1)y}}N
               Y^l\prod_{k=l+1}^{N-1}(1-Yr^k),\\
 V_N^{\rm F}(y,X)
   &=\sum_{\substack{j,l\ge0\\j+l<N}}
        \frac{X^{-j}(rX;r)_j P_{j+l}}{P_j^3P_l}\,f_l(y).
 \end{split}
 \tag{2}
\]
Set \(n=N-j-1\), so \(0\le n<N\), and retain the whole inner
sum
\[
                     H_{j,N}(y)=
       \sum_{l=0}^{N-j-1}\frac{P_{j+l}}{P_l}f_l(y).
 \tag{3}
\]

Define the finite polynomial in \(u\)
\[
 W_{n,N}(u;a)=
      \sum_{l=0}^{n}
          \frac{(r^{-n};r)_l}{(r;r)_l(ar;r)_l}\,u^l .
 \tag{4}
\]
We assume \(1-ar^k\ne0\) for \(1\le k\le N-1\).
In particular \(|a|<1\) is sufficient. All denominators in (4)
are then nonzero; no term at \(l=N\) is present.

**Proposition 1.** With the original lifted normalization,
\[
 \boxed{\quad
 H_{j,N}(y)=
  \frac{e^{-\pi i(N-1)y}(1-Y^N)}{N(1-Y)}
                            P_j W_{N-j-1,N}(Y;Y).
 \quad}
 \tag{5}
\]
Consequently the exact cap is the single finite sum
\[
 V_N^{\rm F}(y,X)=
 \frac{e^{-\pi i(N-1)y}(1-Y^N)}{N(1-Y)}
       \sum_{j=0}^{N-1}
         \frac{X^{-j}(rX;r)_j}{P_j^2}
                         W_{N-j-1,N}(Y;Y).
 \tag{6}
\]
Both level parities, all physical indices and the original
triangular support are included.

*Proof.* The cyclotomic product identity gives
\[
 \prod_{k=0}^{N-1}(1-Yr^k)=1-Y^N,
 \qquad
 \prod_{k=l+1}^{N-1}(1-Yr^k)
          =\frac{1-Y^N}{(1-Y)(Yr;r)_l}.
 \tag{7}
\]
Also
\[
 \frac{P_{j+l}}{P_l}
       =P_j\frac{(r^{j+1};r)_l}{(r;r)_l},
                   \qquad r^{j+1}=r^{-n}.
 \tag{8}
\]
Substituting (7)--(8) in (3) proves (5) term by term.
Substitute (5) in (2) to obtain (6). The factor \(P_j\)
reduces \(P_j^3\) to \(P_j^2\); it is not discarded as a
normalization. \(\square\)

For nomenclature, the standard finite definition is
\[
 p_n(x;a\mid r)
       ={}_2\phi_1(r^{-n},0;ar;r,rx).
 \tag{9}
\]
It is the \(b=0\) specialization of the little \(q\)-Jacobi
definition in
[NIST DLMF, §18.27(iv)](https://dlmf.nist.gov/18.27#iv).
Thus \(W_{n,N}(u;a)=p_n(u/r;a\mid r)\).
Only this finite algebraic definition is used. The usual
orthogonality statements in that reference assume a real base
between zero and one; they do not supply positivity at the
root of unity used here. Equations (5)--(8) are independent
proofs in our original finite normalization.

## 2. The exact operator and its normalization

Keep the parameter \(a\) fixed and let
\[
                         (T F)(u)=F(ru).
 \tag{10}
\]
Multiplication by \(u\) and this shift obey \(Tu=ruT\).

**Proposition 2.** The polynomial in (4) satisfies
\[
 \bigl[(1-T)(1-aT)-u(1-r^{-n}T)\bigr]W_{n,N}=0,
                         \qquad W_{n,N}(0;a)=1.
 \tag{11}
\]
It is the unique polynomial of degree less than \(N\) with this
normalization satisfying (11).

*Proof.* Write \(c_l\) for the coefficient in (4). For
\(1\le l\le n\), its exact ratio is
\[
 \frac{c_l}{c_{l-1}}
       =\frac{1-r^{l-1-n}}{(1-r^l)(1-ar^l)}.
 \tag{12}
\]
The coefficient of \(u^l\) on the two sides of
\[
       (1-T)(1-aT)W=u(1-r^{-n}T)W
\]
is therefore the same. The constant coefficient on each side
is zero. The potential coefficient of \(u^{n+1}\) on the
right vanishes because \(1-r^{n-n}=0\), so the finite
polynomial satisfies the equation exactly.

Conversely let \(F(u)=\sum_{l=0}^{N-1}d_lu^l\) satisfy (11)
and \(d_0=1\). For \(1\le l<N\), both factors in the
denominator of (12) are nonzero. Coefficient comparison therefore
determines \(d_l\) uniquely. It gives \(d_l=c_l\) up to degree
\(n\), and zero thereafter. The coefficient of \(u^N\) also
vanishes: if \(n<N-1\) its preceding coefficient is zero,
while if \(n=N-1\) its multiplier is zero. This proves
uniqueness without a formal infinite series argument.
\(\square\)

Equivalently, the ordered difference equation is
\[
 aW_{n,N}(r^2u;a)
  +(r^{-n}u-1-a)W_{n,N}(ru;a)
  +(1-u)W_{n,N}(u;a)=0.
 \tag{13}
\]
In particular the finite state is specified by an exact operator
and a normalization. This uniqueness statement does not assert
a lower bound on its value at \(u=a=Y\).

## 3. The quadratic critical curve, with the finite shift retained

Replacing \(T\) by a commuting variable \(\lambda\) in the
written ordering (11) gives the polynomial
\[
                    a\lambda^2+
           (r^{-n}u-1-a)\lambda+1-u .
 \tag{14}
\]
At the physical specialization \(u=a=Y\), \(n=N-j-1\),
it is exactly
\[
          Y\lambda^2+(Yr^{j+1}-1-Y)\lambda+1-Y.
 \tag{15}
\]
The appearance of \(r^{j+1}\), rather than \(r^j\), follows
from the original finite factorial and must be retained in
finite-level identities.

For a macroscopic inner coordinate \(s\), \(j/N\to s\)
gives \(r^{j+1}\to S=e^{-2\pi is}\). Dividing the resulting
symbol by \(Y\) yields
\[
              \lambda^2-(1+Y^{-1}-S)\lambda
                                +(Y^{-1}-1)=0.
 \tag{16}
\]
This is exactly the outgoing quadratic in the
[original correlated endpoint equations](research_mixed_fourier_right_cap_correlated_endpoint.md).
The [half-plane branch theorem](research_mixed_fourier_endpoint_halfplane_branch.md)
selects its unique root inside the unit disk on its stated domain.
Here the relation between the finite operator and that quadratic
has been obtained directly from the coefficients of the original
contracted sum.

The parameter and argument must remain distinct during the shift:
\(T\) sends \(u\) to \(ru\) while keeping \(a\) fixed.
Consequently (13), evaluated at \(u=a=Y\), involves
\(W(rY;Y)\) and \(W(r^2Y;Y)\). It is not an equation that
simultaneously replaces both occurrences of \(Y\) by \(rY\).
No one-variable recurrence for the diagonal value is asserted.

## 4. What this changes in the remaining source problem

The physical wedge left in the outer-contour reduction is part of
the exact sum (3). Formula (6) offers a way to keep its cancellation:
estimate \(W_{N-j-1,N}(Y;Y)\) as a whole before summing the
remaining index. The finite normalization in Proposition 2 is a
constraint on the actual solution, and (16) identifies the same
geometric branch already used by the contour argument.

What is still required is a uniform asymptotic or sufficiently
sharp global bound for this specific finite solution, with its
nonzero geometric coefficient established. The two roots of (16),
and the uniqueness of the polynomial in Proposition 2, do not by
themselves prove that coefficient nonzero. No positivity, spectral
gap, almost-invariant vector or whole-cap volume conclusion is
inferred from the Wall-polynomial name.
