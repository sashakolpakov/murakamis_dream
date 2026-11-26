# A coefficient-swap root-count bound for stable source pieces

This note records a finite algebraic ingredient proposed for a signed spectral decomposition. It does not provide that decomposition or its coefficient norm. All extractions below are the original shared extractions; independent local face targets are not substituted.

## 1. One ordinary-face swap

Let \(F(A,C,L,t,\boldsymbol W)\) be homogeneous, real stable, and have nonnegative coefficients. Extract one fixed multiindex in the spectator variables \(\boldsymbol W\), and call the resulting polynomial again \(F\). The usual differentiation and real specialization construction of coefficient extraction preserves stability, unless the result is zero. Let \(K\ge1\), and define the three polynomials

\[
\begin{aligned}
h&=[L^{K-1}t^0]F,\qquad
p=[L^Kt^0]F,\qquad
q=[L^{K-1}t^1]F.
\end{aligned}
\tag{1}
\]

with \(p,q\) nonzero. When \(h\ne0\), their binary degrees are respectively \(d+1,d,d\). A factor multiplying an insertion by the ordinary face \(L\) is exactly responsible for the target change \(K\mapsto K-1\) in (1).

When \(h\ne0\), both \(p\) and \(q\) interlace the same \(h\), with zero and infinite roots interpreted by homogeneous limits. Here is a direct justification of the coefficient-adjacency step. Differentiate a stable polynomial in the auxiliary variable the required number of times and set all other auxiliaries to real values. For \(A\) in the upper half-plane, every zero \(\zeta\) of the remaining auxiliary-variable polynomial lies in the closed lower half-plane. Its logarithmic derivative at zero is a sum of \(-1/\zeta\), with nonpositive imaginary part. Thus the ratio of the first auxiliary coefficient to the constant coefficient has nonpositive imaginary part. The two real polynomials are in proper position: their real zeros interlace. Repeated roots and zero leading coefficients follow by small positive regularization and limits. Apply this first in \(L\) after setting \(t=0\), and then in \(t\) after extracting \(L^{K-1}\).

The case \(h=0\) is also controlled. After differentiating \(K-1\) times in \(L\), divide by \((K-1)!\) and replace \((L,t)\) by \((\epsilon L,\epsilon t)\). Dividing by \(\epsilon\) and taking \(\epsilon\downarrow0\) gives the nonzero stable limit \(K Lp+tq\). For fixed upper-half-plane \(A,C\), stability in \(L,t\) forces \(q/p\) to be a nonnegative real number: any other argument permits both \(t\) and \(-tq/(Kp)\) in the upper half-plane. The holomorphic ratio \(q/p\) is therefore constant on the connected domain. Thus \(p,q\) are positive scalar multiples and their root counts agree. This removes the need to assume a nonzero common interlacer.

Equivalently, factor each degree-\(d\) binary polynomial in its positive normalization as

\[
\frac{p(A,C)}{p(1,1)}
=\prod_{j=1}^d\bigl((1-\lambda_j^p)C+\lambda_j^p A\bigr),
\qquad 0\le\lambda_j^p\le1,
\tag{2}
\]

and similarly for \(q\). Real stability and nonnegative coefficients justify this factorization. The value \(\lambda=0\) records a factor \(C\), and \(\lambda=1\) a factor \(A\). With

\[
N_p(s)=\#\{j:\lambda_j^p\le s\},\qquad
N_q(s)=\#\{j:\lambda_j^q\le s\},
\tag{3}
\]

interlacing with the same degree-\(d+1\) polynomial gives

\[
\sup_{0\le s\le1}|N_p(s)-N_q(s)|\le1.
\tag{4}
\]

At coincident roots either consistent one-sided convention gives the bound; equivalently one can state it first away from atoms and pass to one-sided limits.

## 2. Boundary insertions and a finite sequence

If instead the compensating monomial is \(A\) or \(C\), the extracted first-\(t\) coefficient has degree \(d-1\) and interlaces the unperturbed degree-\(d\) polynomial. Multiplication by the compensating boundary variable adds one endpoint root in (2). The same bound (4) follows.

Consequently, along any sequence of \(r\) such swaps whose intermediate extracted polynomials are nonzero, the unnormalized counting functions differ by at most \(r\). If

\[
\nu_p=\frac1d\sum_j\lambda_j^p,
\qquad
\kappa_p=\frac1d\sum_j\lambda_j^p(1-\lambda_j^p),
\tag{5}
\]

then integration by parts on \([0,1]\) gives

\[
|\nu_p-\nu_q|\le\frac rd,
\qquad
|\kappa_p-\kappa_q|\le\frac{r}{2d}.
\tag{6}
\]

The second constant is the total variation
\(\int_0^1|1-2s|\,ds=1/2\). Thus a low-rank stable piece retains the two moments used in the common-negative-axis estimate, provided its compensating monomials and shared targets are connected by such a feasible sequence.

## 3. What remains to apply this to the original source

For a product of positive Hermitian determinants, all rank-one insertions can be placed in a block-diagonal pencil. Cauchy–Binet expands it into a positive weighted polynomial of bases of a finite vector matroid, with each column labeled by its face or insertion variable. A monotone exchange property for the resulting color-count support would supply the nonzero sequence in Section 2 whenever its two endpoints are feasible. That exchange property is not proved in this note and is not silently assumed here.

Even after feasibility is proved, equations (4)–(6) do not bound the total coefficients of a signed stable decomposition. They also do not control pieces of macroscopic rank deficit or a nonuniform sum of such pieces. Those are separate obligations for the fixed spectral window. In particular a polynomial bound for interpolation weights alone does not make distant lower-channel contributions negligible at exponential scale.
