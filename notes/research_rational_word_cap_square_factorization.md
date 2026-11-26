# The square factor in every rational-word cap symbol

Research note, 3 November 2026.

Every bulk cap symbol in the normalized rational-word determinant has
an elementary factor times a Laurent-polynomial square. The elementary
factor has zero logarithmic mean on the unit torus. The remaining
Laurent polynomial can be computed by an integer recursion that retains
which of the three trace coordinates is being used.

This is a factorization of the classical symbol of the exact source
operator. It does not factor the finite determinant, identify its small
singular values, or prove that its logarithmic mean is the source rate.
The original terminal counterexample to that last assertion remains.

## 1. The original symbol and its trace conventions

Use the matrices and row-offset convention of the
[normalized cofactor theorem](research_rational_word_normalized_cofactor.md).
Write \(X,Y\) for its two bulk variables. They are not independently
chosen meridian and longitude eigenvalues. The three symbols are
\[
 \begin{split}
 A&=X+X^{-1}+(X+X^{-1}-2)Y^{-1},\\
 B&=X+X^{-1}+(X+X^{-1}-2)Y,\\
 C&=4X-2X^2-(1-X)^2(Y+Y^{-1}).
 \end{split}                                                    \tag{1}
\]
These correspond respectively to multiplication by \(z\), its turned
operator \(L\), and \(L_1=M^{-1}LM\). Here \(M\) is the original
crossing matrix and \(J\) is the original turn. The complete cap is
\(B=2\).

Put \(a=A-2\), \(b=B-2\), \(c=C-2\). Direct simplification gives
\[
 a=\frac{(X-1)^2(1+Y)}{XY},\qquad
 b=\frac{(X-1)^2(1+Y)}X,\qquad
 c=-\frac{(X-1)^2(1+Y)^2}Y,
                                                               \tag{2}
\]
and hence
\[
                         (a+b+c)^2+abc=0.                       \tag{3}
\]
The rational inverse on the common nonempty open set is
\[
                      Y=b/a,\qquad X=-c/(a+b).                 \tag{4}
\]
For example (3), after substituting the second equation, gives
\((X-1)^2/X=ab/(a+b)\), which recovers (2). The surface (3) is
irreducible: as a quadratic in \(c\), its discriminant is
\(ab\{ab+4a+4b\}\), which has odd order along \(a=0\) and is
not a square in \(\mathbb C(a,b)\). Thus the Newton symbols give
the original trace surface, not an additional equation imposed only
on a selected saddle.

The classical actions below follow from the full quantum conjugation
identities in the cofactor theorem:
\[
 \begin{array}{c|ccc}
 &A&B&C\\ \hline
 \operatorname{Ad}M&A&8-AB-C&B\\
 \operatorname{Ad}M^{-1}&A&C&8-AC-B\\
 \operatorname{Ad}J&B&A&8-AB-C.
 \end{array}                                                    \tag{5}
\]
In particular the crossing direction is fixed by the original matrix
conjugation. It has not been chosen from an isolated eigenphase.

## 2. A square-root form of the trace relation

Work initially over the rational function field \(\mathbb C(X,Y)\).
Choose \(v^2=Y\) and a root \(q\) with \(q^2=-b\), and define
\[
                p=q/v,\qquad r=-\frac{(X-1)(1+Y)}v.
                                                               \tag{6}
\]
The letter \(q\) in this section is a square-root variable; it is
not the quantum number \(e^{\pi i/N}\). There is no level in
(6). These roots satisfy
\[
             a=-p^2,\quad b=-q^2,\quad c=-r^2,
             \qquad p^2+q^2+r^2=pqr.                           \tag{7}
\]
All statements eventually obtained below are identities of Laurent
polynomials in \(X,Y\), so no numerical choice of these roots is
required.

The trace actions (5) lift to the following polynomial substitutions:
\[
 \begin{array}{c|ccc}
 &p&q&r\\ \hline
 M&p&pq-r&q\\
 M^{-1}&p&r&pr-q\\
 J&q&p&pq-r.
 \end{array}                                                    \tag{8}
\]
For example the new shifted second trace under \(M\) is
\(-ab-2a-2b-c\). By (7),
\[
 -(pq-r)^2=-p^2q^2+2(p^2+q^2)+r^2
                         =-ab-2a-2b-c.                         \tag{9}
\]
This verifies the sign as well as the shift by two. The other
identities follow in the same way. The substitutions preserve (7);
the first two are inverses and the third is an involution.

The product of two different initial roots is a Laurent multiple of
the third. More explicitly,
\[
 \begin{split}
 pq&=\mu_{pq}r,&\mu_{pq}&=(X-1)/X,\\
 pr&=\mu_{pr}q,&\mu_{pr}&=-(X-1)(1+Y)/Y,\\
 qr&=\mu_{qr}p,&\mu_{qr}&=-(X-1)(1+Y).
 \end{split}                                                    \tag{10}
\]
These equations are checked directly from (6). Writing them first
in the fraction field avoids dividing by a value at a zero of a
root. Their resulting Laurent identities extend across such zeros.

## 3. A labelled integer recursion

Attach to a triple of transformed roots a permutation
\((\ell_1,\ell_2,\ell_3)\) of the initial labels \((p,q,r)\),
and Laurent polynomials \((P_1,P_2,P_3)\), so that the triple is
\[
                      (\ell_1P_1,\ell_2P_2,\ell_3P_3).
                                                               \tag{11}
\]
Initially the labels are \((p,q,r)\) and all three polynomials
equal one. Every generator in (8) replaces one entry by the product
of the other two minus that entry, and possibly permutes the entries.
Use (10) for the product. For instance replacing the third entry
gives
\[
       P_3\longmapsto \mu_{\ell_1\ell_2}P_1P_2-P_3.
                                                               \tag{12}
\]
The labels remain distinct, so the multiplier in (12) is always one
of the three displayed Laurent polynomials. This supplies a finite
algorithm in \(\mathbb Z[X^{\pm1},Y^{\pm1}]\), with no division
by a newly computed coefficient.

To avoid an order ambiguity, process the displayed word from left
to right. If the current word is \(W\), appending a letter \(G\)
on its right means
\(\operatorname{Ad}(WG)=\operatorname{Ad}W\circ
\operatorname{Ad}G\). Consequently the new triple is obtained by
applying the polynomial rule in row \(G\) of (8) to the current
triple. A power is processed by its signed unit letters, or by the
equivalent finite iterated recurrence.

**Theorem 1.** Let \(\mathsf d_W\) be the bulk symbol of
\(W(L-c_0)W^{-1}\), with the original word and conventions retained.
There is an explicitly computed label
\(\ell_W\in\{p,q,r\}\) and a nonzero integer Laurent polynomial
\(P_W\) such that
\[
 \boxed{\quad
 \mathsf d_W=E_{\ell_W}P_W^2,\qquad
                   E_p=a,\ E_q=b,\ E_r=c.
 \quad}                                                        \tag{13}
\]
The label and polynomial are the second entry of recursion (11).
The label depends only on the generator permutation: \(M^{\pm1}\)
swaps the second and third labels, and \(J\) swaps the first two.
Thus the crossing exponents modulo two suffice to compute the label,
although the full exponents are needed for \(P_W\).

**Proof.** The induction (10)--(12) proves (11) for every finite
word. Equations (5)--(9) identify its second squared root with the
actual transported shifted cap trace. Its negative square is
precisely (13). The trace substitutions are automorphisms and the
parametrization (4) is dominant; the nonzero cap function therefore
cannot become identically zero. Since its elementary factor is
nonzero, \(P_W\) is nonzero. The equality was proved in a function
field, and both sides are Laurent polynomials. It is consequently
an identity on the entire algebraic torus, including the zero sets
encountered during its derivation. \(\square\)

The label here describes a trace coordinate. It does not replace
the proper rotations of a marked tangle or its original carrier
scalar. Those remain part of the finite word in the cofactor theorem.

For example, \(W=JM^2\) transforms the second root into \(qr-p\).
By (10),
\[
        \ell_W=p,\qquad P_W=-(XY+X-Y),\qquad
 \mathsf d_W=\frac{(X-1)^2(1+Y)(XY+X-Y)^2}{XY}.
                                                               \tag{14}
\]
This recovers the exact original-terminal example in the cofactor
note, including which elementary factor occurs.

## 4. The logarithmic mean and the remaining finite determinant

For a nonzero Laurent polynomial \(P\), put
\[
 m(P)=\int_0^1\int_0^{2\pi}
          \log|P(e^{2\pi ix},e^{i\vartheta})|
                         \frac{d\vartheta}{2\pi}\,dx.
                                                               \tag{15}
\]
This is the logarithmic mean, with its usual integrable logarithmic
zeros. One can verify finiteness directly by first applying the
one-variable Jensen formula: possible zeros of its coefficient
polynomials in the other variable are finite in number, and their
finite orders give integrable logarithmic bounds. Monomial factors
have zero mean.

Each of \(a,b,c\) in (2) has mean zero. Indeed both
\(\log|X-1|\) and \(\log|1+Y|\) have mean zero on their circle,
as do Laurent monomials and the sign in \(c\). Therefore (13) gives
the exact simplification
\[
                         \mathfrak m_W=2m(P_W).                \tag{16}
\]
Together with the proved singular-value moment upper bound, this
yields for the same original closing scalar
\[
 \limsup_{N\to\infty}\frac1N
             \log|\phi_N(W_N1)|\le m(P_W).                    \tag{17}
\]
There is no equality claim in (17). For (14), Jensen gives
\[
 m(P_W)=\int_0^{2\pi}\log\max\{|1+e^{i\vartheta}|,1\}
                                    \frac{d\vartheta}{2\pi}>0,
                                                               \tag{18}
\]
whereas the actual closed source has
\(|\phi_N(JM^21)|=|\kappa_N^2|=1\).
Thus even after extracting the elementary factors and the square,
the surviving polynomial's logarithmic mean need not be the source
rate.

For completeness, the exact normalized cofactor formulas also give
\[
 \frac{\prod_{j=1}^{N-1}s_j(B_{W,N})}
      {\prod_{j=1}^{N-1}s_j(D_{W,N})}
          =\frac{|\phi_N(W_N1)|^2}{\|W_N1\|_2^2}.
                                                               \tag{19}
\]
In the denominator only the nonzero singular values of \(D_{W,N}\)
are included. Formula (19) records the original closing coordinate;
it is not determined by the bulk factorization. Deleting one row
and one column is a bounded-rank operation, but it can change the
logarithmic determinant by order \(N\), as (18) and the proved
small-singular-value example show. A calculation of the corresponding
boundary contribution is still required.

## 5. The geometric information actually retained

On the regular Newton chart away from the elementary factors in
(2), the equation \(P_W=0\) is exactly the transported cap-trace
equation. Its squared occurrence records the nonreduced normal of
the original parabolic cap. The
[original source and cap construction](actual_newton_twist_canonical_graph.md),
Sections 4--5, identifies the trace action and explains the exceptional
incoming cap: the incoming condition \(B=2\) is not a regular finite
point of this Newton chart. One must retain its resolved boundary,
the actual inverse-pair cap matrices, and the original closing
functional to obtain a representation of the closed word.

Accordingly (13) does not identify \(P_W\) with a Riley polynomial,
an A-polynomial, or a selected geometric component. It is a concrete
factor of the original bulk cap equation with its label and
multiplicity fixed. It applies in particular to every negative
continued-fraction word, but it supplies neither the missing
boundary determinant asymptotic nor a general finite-exception
theorem.
