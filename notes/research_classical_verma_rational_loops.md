# Rational classical loops of the original Verma cut source

Private written proof, 17 November 2026.

The literal source used in [R] also has a rational quantum-normal
expansion at \(q=1\). Its leading coefficient is the reciprocally
normalized Alexander polynomial inverse. The proof uses the original
crossings, one-component cut, ordinary pivots, and zero framing. It
does not define or invoke a level-one ADO invariant.

This supplies an independent proof, in the recorded conventions, of
the perturbative color-degree bound and rational-loop property for
the actual reduced colored Jones family. These are established
results, not novelty claims. The point here is their provenance from
the same finite-color source as the all-root construction.

No convergence of the two-variable formal series, continuation across
an Alexander zero, geometric Stokes coefficient, or scalar lower
bound is proved.

## 1. The original source and the statement

Fix a \(b\)-strand braid \(\beta\) with one-cycle permutation and
zero-framed knot closure. Let \(w\) be its writhe and put
\(c=b-1-w\). Thus \(c\) is even. Set
\[
 \delta=1-Q,\qquad Q=q^2,\qquad q=(1-\delta)^{1/2}
 \quad\text{near }q=1.                              \tag{1}
\]
Initially \(x\) is independent of \(\delta\). On the untruncated
basis \(v_a\), \(a\ge0\), use exactly [R, (2)]:
\[
\begin{split}
 R^+_{b'+n,a-n;\,a,b'}
 &=x^{-a-b'+n}Q^{(a-n)b'}{a\brack n}_Q
                  (x^{-2}Q^{a-n};Q)_n,\quad 0\le n\le a,\\
 R^-_{b'-n,a+n;\,a,b'}
 &=x^{a+b'-n}Q^{-ab'}{b'\brack n}_Q
                  (x^2Q^{1-b'};Q)_n,\quad 0\le n\le b'.
\end{split}                                                   \tag{2}
\]
The symbol \(b'\) is a local input index, distinct from the braid
strand count. All entries are Laurent polynomials in \(Q,x\).
The canceled Gaussian expressions in (2) remain their polynomial
values at \(Q=1\).

Retain the same graded cut:
\[
 V_\beta(Q,x;\tau)=x^c
 \sum_{a_2,\ldots,a_b\ge0}\tau^{\sum a_i}Q^{-\sum a_i}
 \langle0,a_2,\ldots,a_b|B_\beta|0,a_2,\ldots,a_b\rangle .
                                                               \tag{3}
\]
Each coefficient of \(\tau\) is a finite Laurent polynomial.
Indeed every crossing preserves total index, so that fixing the
external total index bounds every intermediate index as well.

For a matrix \(L\), write \(\Gamma(L)\) for substitution on a
polynomial ring, with \(Z_j\mapsto\sum_i L_{ij}Z_i\). Define
\[
 L_+(x)=
 \begin{pmatrix}1-x^{-2}&x^{-1}\\x^{-1}&0\end{pmatrix},
 \qquad
 L_-(x)=
 \begin{pmatrix}0&x\\x&1-x^2\end{pmatrix}.             \tag{4}
\]
Let \(L_\beta(x)\) be their embedded product in the original word
order, and \(A_\beta(x)\) its first-row-and-column deletion. Put
\[
 D_\beta(x,\tau)=\det(I-\tau A_\beta(x)).
                                                               \tag{5}
\]
The universal classical determinant identity recorded in [R, (19)]
is, in the variable \(x\),
\[
 D_\beta(x,1)=x^c\Delta_K(x^2),\qquad \Delta_K(1)=1.
                                                               \tag{6}
\]
Here \(\Delta_K\) is the original symmetric Alexander normalization.
That identity is an identity for the classical matrices (4);
using it does not require a level-one quantum invariant.

**Theorem.** For every \(j\ge0\),
\[
 V_{\beta,j}(x,\tau):=[\delta^j]V_\beta
  =\frac{P_{\beta,j}(x,\tau)}
          {D_\beta(x,\tau)^{2j+1}},
 \qquad P_{\beta,j}\in\mathbb Q[x^{\pm1},\tau].       \tag{7}
\]
The identity first means equality of formal \(\tau\)-series.
It specifies the rational continuation on the right.

Define the grading-one formal completion and its natural meridian by
\[
 \widehat V_\beta(\delta,x)
      =\sum_{j\ge0}\delta^j V_{\beta,j}(x,1),\qquad
 Y=q^2x^2,\qquad
 \mathcal W_K(\delta,Y)
      =\widehat V_\beta\!\left(\delta,
                    \sqrt{\frac{Y}{1-\delta}}\right).
                                                               \tag{8}
\]
The square-root choice has no effect. The result is presentation
independent, and its coefficients satisfy
\[
 \mathcal W_K(\delta,Y)=\sum_{j\ge0}\delta^j W_j(Y),
 \qquad
 W_j(Y)\in
       \frac{\mathbb Q[Y^{\pm1}]}{\Delta_K(Y)^{2j+1}},
 \qquad W_0(Y)=\frac1{\Delta_K(Y)}.                 \tag{9}
\]
For every positive integer \(L\), with the original reduced,
zero-framed color-\(L\) scalar \(C_L(q)\),
\[
 \mathcal W_K\bigl(\delta,(1-\delta)^L\bigr)
                = C_L\bigl((1-\delta)^{1/2}\bigr)
                         \quad\text{as formal series}.         \tag{10}
\]
In particular
\[
 \deg_L[\delta^j]C_L\bigl((1-\delta)^{1/2}\bigr)\le j,
 \qquad
 [L^j\delta^j]C_L
   =\frac{(-1)^j}{j!}
       \left.(Y\partial_Y)^j\Delta_K(Y)^{-1}\right|_{Y=1}.
                                                               \tag{11}
\]
Polynomial dependence means that one polynomial agrees with the
coefficient for every positive integral \(L\).

## 2. Fixed-order crossing coefficients

There is only one residue class at \(Q=1\); no head or carry is
introduced. Factor
\[
 (Q;Q)_a=\delta^a a!\,U_a(\delta),\qquad
 U_a(\delta)=
       \prod_{\ell=1}^{a}
          \frac{1-(1-\delta)^\ell}{\ell\delta},
 \qquad U_a(0)=1.                                  \tag{12}
\]
For \(h\ge1\), the order-\(h\) coefficient of the logarithm of
one factor is polynomial in \(\ell\) of degree at most \(h\).
Indeed the coefficient of \(\delta^r\) in that factor is
\((-1)^r\binom{\ell}{r+1}/\ell\), a polynomial of degree \(r\);
the formal logarithm preserves the total order-degree bound.
Summing over \(\ell\) raises degree by at most one. This follows
directly by expressing a polynomial in falling factorials and
using
\(\sum_{\ell=0}^{a-1}(\ell)_d=(a)_{d+1}/(d+1)\).
Thus \([\delta^h]\log U_a\) has degree at most \(h+1\) in \(a\).

Consequently
\[
 {a\brack n}_Q
       ={a\choose n}\sum_{h\ge0}\delta^h G_h(a,n),
 \qquad G_0=1,\qquad \deg G_h\le2h.                \tag{13}
\]
This includes \(n=0,a\). The proof is the unit quotient
\(U_a/(U_nU_{a-n})\); there is no remaining power of \(\delta\).
In exponentiating its logarithm, a product with positive orders
\(h_i\) has degree at most \(\sum(h_i+1)\le2\sum h_i\).

Work temporarily over \(\mathbb Q(x)\), away from \(x^2=1\).
The root color products in (2) are respectively
\((1-x^{-2})^n\) and \((1-x^2)^n\). After division by these
expressions, their logarithmic order-\(h\) coefficients have
degree at most \(h+1\) in the input index and \(n\).
For the positive sign this is the finite sum of degree-\(h\)
polynomials in the exponents \(a-n,\ldots,a-1\); for the negative
sign the exponents are \(1-b',\ldots,n-b'\). Polynomial summation
works on these signed integer intervals without a positivity
assumption. Exponentiation gives the same degree bound \(2h\).
All temporary denominators are functions of \(x\) alone.

The coefficients of \(Q^{(a-n)b'}\) and \(Q^{-ab'}\) at order
\(h\) have degree at most \(2h\) in the input and transfer indices.
Combining these facts, each signed crossing at order \(h\) is
its root crossing coefficient multiplied by a polynomial in those
indices of total degree at most \(2h\), with coefficients in
\(\mathbb Q(x)\).

## 3. The actual polynomial substitutions and cut trace

At \(\delta=0\), (2) is exactly \(\Gamma(L_\pm(x))\).
For example, the positive coefficient is
\(\binom an(1-x^{-2})^n x^{-a-b'+n}\), with output exponents
\((b'+n,a-n)\). The negative coefficient is
\(\binom{b'}n(1-x^2)^n x^{a+b'-n}\), with output
\((b'-n,a+n)\). These are the two binomial expansions of (4).

The polynomial multipliers just proved are differential operators
of order at most \(2h\). The input indices are input Euler
operators. For the positive crossing \(n\) equals the first
output Euler index minus the second input index; for the negative
crossing it equals the second output index minus the first input
index. Hence polynomials in all these indices are sums of left
and right Euler insertions. Move the right insertions left through
\(\Gamma(L_\pm)\). Both linear substitutions are invertible with
Laurent-\(x\) inverse, so this conjugation preserves polynomial
differential order and homogeneous degree zero.

Composition through the finite word therefore gives, at order
\(j\), a finite sum of
\[
                         D\,\Gamma(L_\beta),\qquad
 \operatorname{ord}D\le2j,\quad \deg D=0.           \tag{14}
\]
The original pivot has not been omitted:
\(Q^{-\sum a_i}=(1-\delta)^{-\sum a_i}\) has order-\(h\)
coefficient polynomial of degree at most \(h\) in the total
Euler index. Allocating \(h\) of the normal order to it leaves
the bound \(2j\) in (14). The scalar \(x^c\) remains external.

The trace fact proved in [R, Section 4] can be seen directly.
For a homogeneous degree-zero differential operator \(D\) of
order at most \(d\),
\[
 \operatorname{Tr}_{\mathrm{Sym}}(D\Gamma(B))
        \text{ has denominator dividing }\det(I-B)^{d+1}.
                                                               \tag{15}
\]
The trace without \(D\) is \(\det(I-B)^{-1}\). A degree-zero
Weyl monomial of order at most \(d\) is a linear combination of
products of at most \(d\) vector fields \(Z_i\partial_{Z_j}\):
normal ordering gives its top monomial, and induction removes
the lower-order terms. Their traces are matrix-directional
derivatives of the determinant inverse. Each derivative raises
the denominator power by at most one. This proof works degree
by degree on finite polynomial spaces and requires no inverse
of \(B\).

Let \(T_0=\operatorname{diag}(0,1,\ldots,1)\). It is the literal
projector to the cut input index zero. Finite-degree cyclicity gives
\[
 \operatorname{Tr}\!\left(
     \Gamma(\tau I)\Gamma(T_0)D\Gamma(L_\beta)\right)
       =\operatorname{Tr}\!\left(D\Gamma(\tau L_\beta T_0)\right),
 \quad
 \det(I-\tau L_\beta T_0)=D_\beta(x,\tau).           \tag{16}
\]
No projector has been inverted. Equations (14)--(16) prove (7)
over \(\mathbb Q(x)\), with polynomial numerator in \(\tau\).

To remove the temporary meridian denominators, write the result
as \(A(x,\tau)/(g(x)D_\beta^{2j+1})\), with
\(A\in\mathbb Q[x^{\pm1},\tau]\) and \(g\ne0\) Laurent.
Every original coefficient of \(\tau\) in \(V_{\beta,j}\) is
Laurent in \(x\), by (2)--(3). Multiplication by
\(D_\beta^{2j+1}\) shows that each of the finitely many
\(\tau\)-coefficients of \(A/g\) is Laurent. Thus \(g\) cancels
coefficientwise, proving (7) even at \(x^2=1\).

At order zero no insertions occur. Equations (6) and (16) give
\[
                         V_{\beta,0}(x,1)
                             =\frac1{\Delta_K(x^2)}.            \tag{17}
\]

## 4. Meridian, parity, and finite-color restrictions

The exact evenness from [R, Section 7] also follows directly here.
On a tensor basis use the staggered diagonal
\(G=(-1)^{\sum_i i a_i}\). Replacing \(x\) by \(-x\) multiplies
each crossing entry by \((-1)^{a+b'+n}\), exactly its output/input
\(G\)-ratio. Diagonal closure cancels this conjugation; \(c\) is
even. Hence \(V_\beta(Q,-x;\tau)=V_\beta(Q,x;\tau)\).
This proves the square-root independence in (8).

At order \(j\), the change \(x^2=Y/(1-\delta)\) applies at most
\(j-\ell\) Euler derivatives to a fixed-\(x\) coefficient of order
\(\ell\). Each derivative raises its Alexander denominator
power by at most one. The resulting power is at most
\(2\ell+1+j-\ell\le2j+1\). Evenness and (17) prove (9).

For completeness, finite-color restriction is before any root
specialization. Put \(x=q^{L-1}\) in (2).
If \(a\ge L>a-n\), the positive product includes the factor
\(1-x^{-2}Q^{L-1}=0\). If \(b'\ge L>b'-n\), the negative product
includes \(1-x^2Q^{1-L}=0\). In either sign a high index cannot
drop below \(L\) along its physical strand; the other strand's
index only rises. A high index created anywhere in a surviving
closed path would therefore propagate around the single knot
component to the fixed cut index zero, a contradiction.
Every contributing intermediate index is consequently \(<L\).
The resulting graded sum is exactly the finite quotient cut.

At \(\tau=1\) its ordinary pivots contribute \(x^{b-1}\);
the common Cartan/twist zero-framing ratio contributes \(x^{-w}\).
Their product is precisely \(x^c\) in (3), as in [R, Section 6].
The highest cut introduces no quantum-dimension division.
Thus the quotient is the original \(C_L(q)\), with \(C_1=1\).
In particular it is even in \(q\): (2) depends on \(q\) only
through \(Q\), and \(q\mapsto-q\) changes \(x=q^{L-1}\) only
by a sign. This also explains why the same proof may be viewed
as the no-head version at \(q_0=-1\); here no such choice is needed.

There is no infinite-sum evaluation hidden in (10).
At \(x=1\), both matrices (4) swap the two variables. The braid
product is its one-cycle strand permutation. Its deleted
compression is nilpotent, so
\[
                            D_\beta(1,\tau)=1.                 \tag{18}
\]
Every fixed-order meridian derivative of (7), evaluated at
\(x=1\), is therefore polynomial in \(\tau\).
Substitute \(x=(1-\delta)^{(L-1)/2}\) coefficientwise.
The preceding high-index argument identifies each coefficient
with that of the finite graded quotient. Both sides are
polynomials in \(\tau\), so evaluation at \(\tau=1\) is legitimate.
Since \(Y=(1-\delta)^L\), this proves (10).

## 5. Color degree, canonical source, and actual recurrences

Put \(E=Y\partial_Y\) and \(\eta=\log(1-\delta)\). In (10),
\[
 W_a((1-\delta)^L)
       =\sum_{r\ge0}\frac{L^r\eta^r}{r!}(E^rW_a)(1).
                                                               \tag{19}
\]
At total order \(j\), one has \(r\le j-a\). Thus the degree in
\(L\) is at most \(j\). Its degree-\(j\) term comes only from
\(a=0,r=j\), with \([\delta^j]\eta^j=(-1)^j\).
This proves (11). In the original coordinate \(q=e^h\) it gives
\[
 \deg_L[h^j]C_L(e^h)\le j,\qquad
 [L^jh^j]C_L(e^h)
       =\frac{2^j}{j!}(E^j\Delta_K^{-1})(1).         \tag{20}
\]
Equivalently the diagonal coefficients have generating series
\(\Delta_K(e^{2z})^{-1}\).

The completion is canonical. If two formal series with rational
meridian coefficients regular at \(Y=1\) have all the restrictions
(10), express their difference in
\((\eta,u)=(\log(1-\delta),\log Y)\).
Its homogeneous degree-\(n\) part restricts on \(u=L\eta\) to
a polynomial in \(L\). It vanishes at every positive integer,
so all its coefficients are zero. This proves equality of the
formal germs and hence of each rational meridian coefficient.
Two presentations of the actual knot have the same \(C_L\);
therefore (8) is presentation independent.

The same argument transports every supplied actual generic color
recurrence, after its coefficient denominators have been cleared.
In the squared-meridian convention a finite shift sends
\(Y\) to \(Q^iY\) and color \(L\) to \(L+i\). The recurrence
applied to (8) restricts to zero on every line \(u=L\eta\) for
all sufficiently large positive \(L\); all shifted arguments
are regular at \(Y=1\). Homogeneous-polynomial rigidity again
makes it zero.

For the original normal-state operator this conclusion applies
to \((Y-1)\mathcal W_K\), with its normal gauge retained.
Indeed evaluation of its all-level root equation at the ordinary
node \(Y=Q_N^L\), with \(N\) larger than every shifted color,
gives a Laurent polynomial identity in \(q_N\).
Infinitely many levels force the corresponding generic color
identity. The preceding argument then applies to that identity.
This does not prove equality of minimal annihilator ideals,
classical end preservation, or geometric-factor survival.

One actual classical consequence does follow. For a normal-state
annihilator whose coefficients are regular at \(q=1\), the
order-zero equation is
\[
 B_{\rm cl}(Y,1)\frac{Y-1}{\Delta_K(Y)}=0 .
 \quad\text{Hence}\quad
 B_{\rm cl}(Y,1)=0.                                \tag{21}
\]
If its primitive classical symbol is nonzero, it therefore has
the abelian factor \(\Lambda-1\) in the shift variable \(\Lambda\).
This does not force its two extreme shift coefficients to survive.

Finally, if \(\alpha\ne0\) is a simple zero of \(\Delta_K\), the
actual classical coefficient has the nonzero residue
\[
             \operatorname{Res}_{Y=\alpha}W_0(Y)\,dY
                         =\frac1{\Delta_K'(\alpha)}.            \tag{22}
\]
This is the \(q\to1\) abelian coefficient. It is distinct from
the fixed-level residue \(F_N(M_*)/\Delta_K'(\alpha)\) at
\(M_*^{2N}=\alpha\) in [R]'s root construction. Neither residue
identifies an analytic geometric contribution of the original
root-of-unity source.

## 6. Coverage and proof source

The general perturbative degree statement and rational Alexander-loop
property are the established Melvin--Morton--Rozansky statements.
No external proof is used here. The repository already contains a
weaker direct degree-\(2j\) PBW argument for every original cut word
and a degree-\(j\), integral-loop argument for the literal figure-eight
Newton sum. Neither is used as a premise.

The addition relative to [R] is the explicit \(Q=1\) source argument,
where there are no head residues or carries, and the normalization
(17). It does not extend [R] merely by assigning a name to a
level-one invariant. It proves no integrality of the rational-loop
numerators beyond the displayed rational coefficient ring.

The only proof direct is the following complete text, read in full
with its used implications checked:

| Label | Complete source | SHA256 |
|---|---|---|
| R | notes/research_all_root_verma_normal_rationality.md | 46e984e3ce5491ff82a18da6914d89a0e42393fd7e66877dc679190e69b125f6 |

All additional fixed-order expansions, no-head differential bounds,
trace specializations, and slope arguments are written above.
Only written mathematics and source-text reads were used; no
mathematical programs, tests, numerical cases, or builds were run.
Frozen notes and public manuscripts are unchanged.
