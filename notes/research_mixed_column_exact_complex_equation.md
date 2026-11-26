# The complex source equation retains a cyclotomic forcing term

Research deduction, 7 November 2026. The original Fourier column has
a specified finite Laurent-polynomial continuation. Its recurrence
away from the sampling roots is inhomogeneous. The forcing is explicit,
and adjoining its first-order equation gives an exact homogeneous
annihilator for the full source. This distinguishes a recurrence at
the sampled roots from an equation for the function on which a
complex contour argument would operate.

No numerical evaluation is used. The operator below annihilates the
specified finite source; no identification with a knot's
\(A\)-polynomial is asserted.

## 1. The finite continuation and its physical values

Fix \(N\ge2\) and put
\[
 D=N-1,\qquad q=e^{\pi i/N},\qquad r=q^{-2},\qquad
 \kappa=q^{D^2/2},\qquad
 P_k=(r;r)_k,\qquad p_k(X)=(rX;r)_k.
 \tag{1}
\]
All \(P_k\) with \(0\le k<N\) are nonzero. Define
\[
 \mathcal V_N(X)=\kappa^2N\,C_{1,N}(X,1)
       =\kappa^2N\sum_{k=0}^{D}
                      \frac{X^{-k}p_k(X)}{P_k^2},
                         \qquad X\in\mathbb C^\times.
 \tag{2}
\]
The equality uses \(p_k(1)=P_k\) in the original conditional
kernel. Thus \(\mathcal V_N\) is a polynomial in \(X^{-1}\)
of degree at most \(D\), with no unspecified interpolation.

Let
\[
             \gamma=MJM^3e_0,\qquad v_j=(-q)^{-j}\gamma_j.
 \tag{3}
\]
Here \(M\) is the original crossing matrix, \(J\) reverses its
coordinate indices, and \(e_0\) is the first coordinate vector.
The exact source identity in
[the cumulative endpoint theorem, equations (17)--(19)](research_mixed_next_low_cardinal_endpoint_packet.md)
gives
\[
                       \mathcal V_N(r^j)=v_j,\qquad 0\le j<N.
 \tag{4}
\]
It follows from the literal conditional sum and its moment identity,
not from the asymptotic of the column.

Set
\[
                         d(X)=2-X-X^{-1}.
 \tag{5}
\]
The original initialized column recurrence, including its two
endpoint values, is recorded in
[the Fourier-column theorem, equations (4)--(6)](research_three_crossing_next_crossing_fourier.md).
In the present normalization it reads
\[
 \begin{split}
 d(r^{j+1})v_{j+1}
    -[3-(1+r)r^j]v_j+(1-r^j)v_{j-1}&=0,
                                      &&1\le j<D,\\
 d(r)v_1-(2-r)v_0&=-\kappa^2.
 \end{split}
 \tag{6}
\]
There is also an exact last-row relation
\[
                  -(2-r^{-1})v_D+(1-r^{-1})v_{D-1}=0.
 \tag{7}
\]
For example, (7) follows from the same theorem's right-end
normalization
\[
 (-q)(1-r^{-1})\gamma_{D-1}/N=2-r^{-1},
                          \qquad \gamma_D=N.
 \tag{8}
\]
These formulas retain the actual first-row forcing. At \(N=2\)
the interior range in (6) is empty; the endpoint formulas still
apply.

## 2. The exact equation off the sampling grid

For a function \(f\) on \(\mathbb C^\times\), write
\[
 (Tf)(X)=f(rX),\qquad
 \mathcal L_N=d(rX)T-[3-(1+r)X]+(1-X)T^{-1}.
 \tag{9}
\]
Multiplication coefficients in (9) act before the following
shift is evaluated.

**Theorem 1.** The complete source satisfies
\[
 \boxed{\quad
 \mathcal L_N\mathcal V_N(X)
       =\mathcal F_N(X)
       :=-\frac{\kappa^2}{N}\sum_{k=1}^{N}X^{-k}
       =-\frac{\kappa^2}{N}\frac{1-X^{-N}}{X-1}.
 \quad}
 \tag{10}
\]
At \(X=1\), the last expression means its removable value
\(\mathcal F_N(1)=-\kappa^2\).

*Proof.* Write \(\mathcal V_N(X)=\sum_{k=0}^{D}c_kX^{-k}\)
and let \(R_N=\mathcal L_N\mathcal V_N\). The possible Laurent
degrees initially range from \(-N\) to \(1\). The coefficient
of \(X\) is
\[
                         (-r+1+r-1)c_0=0.
 \tag{11}
\]
The constant coefficient is
\[
             (2-3+1)c_0+\{-1+(1+r)-r\}c_1=0.
 \tag{12}
\]
Consequently \(X^NR_N(X)\) is a polynomial of degree at most
\(N-1\). At \(X=r^j\), equations (4)--(7) give
\[
                  R_N(1)=-\kappa^2,\qquad
                  R_N(r^j)=0\quad(1\le j<N).
 \tag{13}
\]
For the last node the factor \(d(rX)=d(1)=0\), so (7)
supplies the value without an unprescribed \(v_N\).
Since \((r^j)^N=1\), the same values hold for \(X^NR_N\).
The degree-\((N-1)\) polynomial with these values is exactly
\[
                    -\frac{\kappa^2}{N}
                                      \sum_{m=0}^{N-1}X^m.
 \tag{14}
\]
Dividing by \(X^N\) proves (10). \(\square\)

The proof uses root interpolation for a polynomial whose degree
has first been bounded. It therefore proves an identity on
\(\mathbb C^\times\), including the points between sampling roots.

## 3. A homogeneous equation for the enlarged source

The forcing in (10) obeys its own exact first-order equation.
Define
\[
                   \mathcal Q_N=(rX-1)T-(X-1).
 \tag{15}
\]
Because \(r^N=1\), equation (10) gives
\[
       (rX-1)\mathcal F_N(rX)
               =(X-1)\mathcal F_N(X)
               =-\frac{\kappa^2}{N}(1-X^{-N}).
 \tag{16}
\]
Thus the specified source has the exact homogeneous annihilator
\[
                         \mathcal Q_N\mathcal L_N\mathcal V_N=0.
 \tag{17}
\]
The order in (17) matters: the coefficients do not commute with
\(T\). This is an operator of shift range from \(-1\) to \(2\).

There is a simple algebraic description of its limiting symbol.
Replace \(r\) by \(1\) in the coefficient expressions, and replace
the shift \(T\) by a commuting variable \(z\). Multiplication by
\(z\) clears the negative shift and gives
\[
       (X-1)(z-1)
          \{d(X)z^2-(3-2X)z+1-X\}.
 \tag{18}
\]
The quadratic factor is precisely the characteristic curve of the
original column: if \(\lambda=d(X)z\), it becomes
\[
                 \lambda^2-(3-2X)\lambda+d(X)(1-X)=0.
 \tag{19}
\]
The additional \(z-1\) factor comes from the forcing equation.
Equation (18) is a symbolic algebraic limit, not an asymptotic
statement for solutions of (17). In particular the extra factor
and the coefficient \(X-1\) do not justify removing the actual
source value at \(X=1\).

## 4. Bounds relevant to a complex continuation

Away from \(X=1\), the forcing has the exact elementary bound
\[
       |\mathcal F_N(X)|
             \le\frac{1+|X|^{-N}}{N|X-1|}.
 \tag{20}
\]
At any fixed \(X\) with \(|X|\ne1\),
\[
 \lim_{N\to\infty}N^{-1}\log|\mathcal F_N(X)|
                                =\max\{0,-\log|X|\}.
 \tag{21}
\]
The assertion is uniform on compact subsets of either
\(\{|X|>1\}\) or \(\{0<|X|<1\}\).
On the unit circle, (20) is an upper bound on compact arcs
away from one; a two-sided limit is not asserted there because
of the exact sampling zeros.

For completeness, the original global column bound also gives a
whole-function upper bound for the finite continuation. Let
\(A_* = A(x_*)\) be the maximum in the Fourier-column theorem.
That theorem implies
\[
                         \max_{0\le j<N}|v_j|
                                      \le CN^C e^{NA_*}.
 \tag{22}
\]
The polynomial \(\mathcal V_N(U^{-1})\), of degree at most \(D\)
in \(U\), has the values \(v_j\) at \(U=r^{-j}\).
Its cardinal polynomials have modulus at most one on \(|U|\le1\).
Interpolation there and the exterior polynomial bound therefore give
\[
       |\mathcal V_N(X)|
          \le CN^C e^{NA_*}\max\{1,|X|^{-D}\},
                            \qquad X\ne0.
 \tag{23}
\]
This includes all original coefficients. It is not a local
geometric-branch asymptotic.

With \(X=e^{-2\pi it}\), (21) has rate
\(\max\{0,-2\pi\Im t\}\). Thus moving the coefficient variable
downward can make the forcing exponentially large. A continuation
argument must compare that term with the proposed action and retain
the actual boundary data. The homogeneous recurrence at the
noninitial sampling roots alone does not provide such a comparison.
