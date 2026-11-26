# A finite large-cutoff bound for the original scalar endpoint

Private written proof, 18 November 2026.

The scalar endpoint amplitude in the exact finite-Laplace comparison
[B] is entire. Its growth in the cutoff is at most exponential in the
square root of the cutoff times the color. Consequently one finite
cutoff makes this endpoint contribution exponentially small at the
physical complete-color sequence, at any prescribed rate.

The estimate uses the literal finite-color source. It does not assert
that the canonical Borel source has been continued to that large
cutoff, and it gives no estimate for the other, shift endpoint current.

## 1. Original source and statement

Fix the one-component braid source of [F]. Write its strand count,
crossing count and writhe as \(b,\ell,w\), and put
\[
 m=b-1,\qquad c=m-w,\qquad D=7\ell+2m+|c|.
 \tag{1}
\]
All these integers are fixed. Let \(C_L(q)\) be its original reduced,
zero-framed color-\(L\) polynomial, for each integer \(L\ge1\).
Use the coefficient norm
\[
 \|f\|_1=\sum_j|a_j|\quad\text{for }f(q)=\sum_j a_jq^j.
 \tag{2}
\]
This norm retains the ordinary Laurent coefficients before evaluating
at a root; no positivity of the coefficients is assumed.

Write
\[
 C_L(e^{h/2})=\sum_{n\ge0}c_{L,n}h^n,
 \qquad
 A_L(h,R)=\sum_{k,n\ge0}c_{L,k+n}h^k\frac{R^n}{n!}.
 \tag{3}
\]
The second expression is exactly the scalar endpoint amplitude in
[B, (20)--(21)]. It is defined for all complex \(h,R\), independently
of any continuation of the generic-meridian Borel source.

**Theorem.** The actual finite-color source satisfies
\[
 \operatorname{supp}_q C_L\subset[-DL^2,DL^2],\qquad
 \|C_L\|_1\le L^m3^{\ell(L-1)}.                 \tag{4}
\]
For every \(h,R\in\mathbb C\),
\[
 |A_L(h,R)|
 \le L^m3^{\ell(L-1)}
       \exp\!\left(\frac{DL^2|h|}{2}
                         +L\sqrt{2D|R|}\right).              \tag{5}
\]
In particular, put
\[
 h_N=\frac{2\pi i}{N},\qquad q_N=e^{h_N/2},\qquad R=ir,
 \quad r>0.
 \tag{6}
\]
Then for every integer \(N\ge2\),
\[
 |e^{-R/h_N}A_N(h_N,R)|
 \le N^m\exp\!\left\{N\left[
       \ell\log3+\pi D+\sqrt{2Dr}-\frac r{2\pi}\right]\right\}.
 \tag{7}
\]
For every \(\Lambda>0\) there is one finite \(r\), depending only
on the fixed braid and \(\Lambda\), such that
\[
             |e^{-ir/h_N}A_N(h_N,ir)|\le e^{-\Lambda N}
 \quad\text{for all sufficiently large }N.                  \tag{8}
\]
The cutoff in (8) is fixed before the level tends to infinity.

## 2. Coefficient bounds from both signed crossings

In [F, (2)--(3)], specialize \(Q=q^2\) and \(x=q^{L-1}\).
Its one-component finite-quotient proof shows that every contributing
intermediate index is less than \(L\). The exact cut expression is
\[
 C_L(q)=x^c
 \sum_{0\le a_2,\ldots,a_b<L}Q^{-\sum a_i}
   \langle0,a_2,\ldots,a_b|B_\beta|0,a_2,\ldots,a_b\rangle,
 \qquad x=q^{L-1},                               \tag{9}
\]
where the word acts on the finite quotient. The highest cut supplies
no quantum-dimension denominator. In particular all pivots and the
zero-framing monomial in (9) remain in the calculation.

For local input indices \(a,b'<L\), the two nonzero types of entry
are
\[
\begin{split}
 R^+_{b'+n,a-n;\,a,b'}
 &=x^{-a-b'+n}Q^{(a-n)b'}{a\brack n}_Q
                    (x^{-2}Q^{a-n};Q)_n,\quad 0\le n\le a,\\
 R^-_{b'-n,a+n;\,a,b'}
 &=x^{a+b'-n}Q^{-ab'}{b'\brack n}_Q
                    (x^2Q^{1-b'};Q)_n,\quad 0\le n\le b'.
\end{split}                                                   \tag{10}
\]
Only outputs in the quotient are retained; deleting other outputs
can only decrease the bounds below.

The finite Gaussian polynomial \({a\brack n}_Q\) has nonnegative
integer coefficients, coefficient sum \(\binom an\), and degree
\(n(a-n)\). These follow by induction from
\({a\brack n}_Q={a-1\brack n}_Q+
Q^{a-n}{a-1\brack n-1}_Q\), including the endpoint polynomials
\(1\). Each factor of a color product has coefficient norm at most
two after specialization. The monomial factors have norm one.
Submultiplicativity of (2) therefore bounds the positive input-column
sum by
\[
             \sum_{n=0}^{a}\binom an2^n=3^a\le3^{L-1}.
 \tag{11}
\]
The negative input-column sum has the identical bound with \(b'\)
in place of \(a\). This includes both signs, all endpoint transfers,
and every quotient truncation.

For a Laurent-polynomial matrix use the maximum input-column sum
of the coefficient norms of its entries. This matrix norm is
submultiplicative, by the scalar triangle and product inequalities.
Thus the word in (9) has norm at most \(3^{\ell(L-1)}\).
There are exactly \(L^m\) displayed cut inputs. Their diagonal
coefficients are bounded by that norm, while all pivot and framing
factors have norm one. This proves the coefficient bound in (4).

For completeness the exponent support is bounded directly as well.
The absolute \(q\)-exponent budgets for the four factors in either
entry of (10) are respectively
\[
 2(L-1)^2,\qquad 2(L-1)^2,\qquad
                 \tfrac12(L-1)^2,\qquad 2(L-1)^2.             \tag{12}
\]
For the last budget, the positive color factors have exponents
\(2(a-n+t-L+1)\), \(0\le t<n\), lying between
\(-2(L-1)\) and \(-2\). The negative factors have exponents
\(2(L-b'+t)\), lying between \(2\) and \(2(L-1)\).
There are at most \(L-1\) factors. When \(n=0\) the product is
one. The Gaussian budget follows from
\(2n(a-n)\le(L-1)^2/2\), and similarly for the negative sign.
The other two budgets follow immediately from (10).

The sum of (12) is at most \(7(L-1)^2\). Multiplication through
the word adds at most \(7\ell(L-1)^2\). The pivot in (9) adds
at most \(2m(L-1)\), and its framing monomial adds
\(|c|(L-1)\). Hence the sharper support bound
\[
 |j|\le7\ell(L-1)^2+(2m+|c|)(L-1)\le DL^2                 \tag{13}
\]
holds for every exponent in \(C_L\), proving the other part of (4).
For \(L=1\), all these entry budgets vanish and \(C_1=1\).
For the empty one-strand braid, \(m=\ell=c=D=0\), and the
statements reduce to the same constant source.

## 3. The scalar endpoint has square-root cutoff growth

Consider first one exponential \(e^{ah}\), with any \(a\in\mathbb C\).
Its contribution to (3) is
\[
 A^{(a)}(h,R)=\sum_{k,n\ge0}
                  \frac{a^{k+n}h^kR^n}{(k+n)!\,n!}.
 \tag{14}
\]
Since \((k+n)!\ge k!n!\), the absolute sum is bounded by
\[
 e^{|ah|}\sum_{n\ge0}\frac{|aR|^n}{(n!)^2}
                     \le e^{|ah|+2\sqrt{|aR|}}.               \tag{15}
\]
The last inequality is elementary: \(\binom{2n}{n}\le4^n\)
implies
\(x^n/(n!)^2\le(2\sqrt x)^{2n}/(2n)!\) for \(x\ge0\),
so the series is at most \(\cosh(2\sqrt x)\le e^{2\sqrt x}\).
In particular (14) converges normally on every compact set of
\((h,R)\), including \(a=0\).

Writing \(C_L(q)=\sum_j a_{L,j}q^j\), its scalar function is
\(C_L(e^{h/2})=\sum_j a_{L,j}e^{jh/2}\). By linearity,
\[
                  A_L(h,R)=\sum_j a_{L,j}A^{(j/2)}(h,R).
 \tag{16}
\]
This is a finite sum of entire functions. Bounds (4), (13) and
(15) give exactly (5). Cancellations in the actual scalar are
not needed for this upper estimate.

## 4. One finite cutoff pays any prescribed scalar endpoint rate

At (6), \(|h_N|=2\pi/N\) and \(\Re(R/h_N)=rN/(2\pi)\).
Substituting \(L=N\) in (5), and enlarging
\(3^{\ell(N-1)}\) to \(e^{\ell N\log3}\), proves (7).

An explicit sufficient choice for (8) is
\[
 r\ge\max\left\{1,\ 32\pi^2D,\ 
           4\pi(\ell\log3+\pi D+\Lambda+1)\right\}.           \tag{17}
\]
Indeed the second condition gives
\(\sqrt{2Dr}\le r/(4\pi)\). The bracket in (7) is then at
most \(-\Lambda-1\). For sufficiently large \(N\),
\(m\log N\le N\), so the factor \(N^m\) proves (8).
This argument also covers \(D=0\).

In the exact source comparison of [B], whenever the specified
generic-meridian cutoff has been constructed, the two endpoint
amplitudes occur as
\[
 U_R(h,e^{Lh})-C_L(e^{h/2})
      =e^{-R/h}\{K_L(h,R)-A_L(h,R)\}.                         \tag{18}
\]
Equation (8) controls the scalar term in (18) at the complete
physical sequence, without imposing a classical end condition on
an annihilator. Among these two amplitudes, the shift endpoint
\(K_L\) still requires a bound. In addition, constructing the
canonical Borel path and the associated \(U_R,K_L\) at the large
endpoint (17) remains a separate question. The entire function
\(A_L\) and estimate (8) do not assert that construction.

No limit \(R\to\infty\), infinite Laplace sum, selected geometric
coefficient, or lower bound for \(C_N(q_N)\) is obtained. In
particular an upper bound on this endpoint current does not bound
the original complete value by itself.

## 5. Proof sources and coverage

The finite-color coefficient and degree estimates above are elementary
bounds on the existing literal source, not a new assertion of
coefficient positivity. The finite-cutoff identity and its scalar
endpoint were already established in [B]. The quantitative addition
is (15) and its combination with the actual source bounds: its
square-root dependence on \(|R|\) is dominated by the linear cutoff
exponent in (7).

| Label | Complete source | SHA256 |
|---|---|---|
| F | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |
| B | notes/research_canonical_borel_finite_laplace_current.md | b3b1e4246e2b5ed1b364585b8504edf8e0f1f1e15797f62f276fc4b89dca586f |

F supplies the original signed crossings, exact finite quotient,
one-component cut, pivot and zero-framing normalization. B supplies
the exact scalar endpoint (3) and comparison (18). All quantitative
estimates used here are proved above. No external proof, mathematical
program, test or build is used. Frozen notes and public manuscripts
are unchanged.
