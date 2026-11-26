# Rational quantum normals of the original graded Verma source

Private written proof, 17 November 2026. The same untruncated,
ordinarily pivoted, graded cut source as [V] has rational coefficients
at every quantum-normal order and every prescribed root q_N. At order j its only
possible denominator is the (2j+1)-st power of the original deleted
classical Burau determinant. The proof retains closed head-carry
cycles, not just the root associated graded.

On genuine integral-color curves this source is the original finite
reduced, zero-framed period. Its order-j root jet at color NR is
polynomial in R of degree at most j. The grading-one completion is
uniquely fixed by those finite-color germs, is presentation independent,
and satisfies every supplied actual generic color recurrence.

All-root rational loops and recurrence compatibility have existing
literature coverage, discussed at the end. No literature proof is a
premise here. This is an independent proof for the specified original
graded source, with an explicit determinant exponent and normal path.
It proves no convergence of the whole quantum expansion, large-level
estimate, geometric-cycle coefficient, or volume lower bound.

## 1. The exact source and theorem

Fix N>=2, q0=exp(pi i/N), Q0=q0², and
\[
 \delta=1-Q^N,\qquad
 q=q_0(1-\delta)^{1/(2N)},\quad Q=q^2.                 \tag{1}
\]
Initially x is held fixed. Put \(\mathbb K=\mathbb Q(q_0)\).
On the untruncated Verma basis \(v_a\), \(a\ge0\), retain [V]'s
two canceled checked crossings:
\[
\begin{split}
 R^+_{b+n,a-n;\,a,b}
 &=x^{-a-b+n}Q^{(a-n)b}{a\brack n}_Q
       (x^{-2}Q^{a-n};Q)_n,\quad 0\le n\le a,\\
 R^-_{b-n,a+n;\,a,b}
 &=x^{a+b-n}Q^{-ab}{b\brack n}_Q
       (x^2Q^{1-b};Q)_n,\quad 0\le n\le b.
\end{split}                                                   \tag{2}
\]
Their coefficients are Laurent polynomials in q,x. No vanishing
factorial is divided after root restriction.

Let beta have b strands, writhe w, and one-cycle permutation. Set
c=b-1-w, an even integer. Its literal source is
\[
 V_\beta(q,x;\tau)=x^c
 \sum_{a_2,\ldots,a_b\ge0}\tau^{\sum a_i}Q^{-\sum a_i}
 \langle0,a_2,\ldots,a_b|B_\beta|0,a_2,\ldots,a_b\rangle.
                                                               \tag{3}
\]
Every tau coefficient is a finite Laurent polynomial: crossings
preserve total index, bounding every intermediate index. Thus
\(V_{\beta,j}=[\delta^j]V_\beta\) is defined coefficientwise.

Put k=x^N and retain
\[
 L_+(k)=\begin{pmatrix}1-k^{-2}&k^{-1}\\k^{-1}&0\end{pmatrix},
 \qquad L_-(k)=\begin{pmatrix}0&k\\k&1-k^2\end{pmatrix}. \tag{4}
\]
Let L_beta be their embedded product in the original word order,
and A_beta its first-row-and-column deletion. Write
\[
 D_\beta(x,\tau)=\det(I-\tau^N A_\beta(x^N)),\qquad
                         D_\beta(x,0)=1.             \tag{5}
\]

**Theorem.** For every j>=0,
\[
 V_{\beta,j}(x,\tau)=
 \frac{P_{\beta,j}(x,\tau)}{D_\beta(x,\tau)^{2j+1}},
 \qquad P_{\beta,j}\in\mathbb K[x^{\pm1},\tau].         \tag{6}
\]
The equality is first in formal tau series and thereby specifies its
rational continuation. Factors may cancel. No other meridian or
grading poles occur. At j=0 this is the fully normalized identity
[V, (3.2)].

## 2. Factorial-block jets and the actual transfer zeros

Let \(p_r=\prod_{s=1}^r(1-Q_0^s)\), \(0\le r<N\). Factoring every
multiple-of-N zero gives, for A>=0,
\[
 (Q;Q)_{NA+r}=\delta^A A!N^A p_r U_{A,r}(\delta),
 \qquad U_{A,r}(0)=1.                                 \tag{7}
\]
For h>=1 the coefficient of delta^h in log U is polynomial in A
of degree at most h+1. Here is an elementary proof with the zero
factors retained. Each normalized zero factor is
\[
                  \frac{1-(1-\delta)^l}{l\delta};
\]
its logarithmic order-h coefficient is polynomial in l of degree
at most h. A normalized nonzero-residue factor is
\[
 \frac{1-Q_0^s(1-\delta)^{l+s/N}}{1-Q_0^s},\quad 1\le s<N,
\]
with the same degree bound. Sum over the finite residue intervals.
Finite power sums raise degree by at most one, as follows by
expanding in falling factorials and using
\(\sum_{l=0}^{A-1}(l)_d=(A)_{d+1}/(d+1)\).
The root nonzero factors have product \(N^A p_r\), proving (7).
Exponentiating shows that the order-h coefficient of a product or
quotient of these units has polynomial degree at most 2h: in a
product with positive orders h_i, the degree is at most
\(\sum(h_i+1)\le2\sum h_i\).

Write a=NA+r, n=NC+t, and
\[
 e=\mathbf1_{t>r},\qquad r'=r-t+Ne.                   \tag{8}
\]
The actual factorial zero count in the Gaussian is e. Equation (7)
therefore yields the exact series
\[
 {NA+r\brack NC+t}_Q
 =\delta^e\frac{N^e p_r}{p_t p_{r'}}
 {A\choose C}(A-C)^e
 \sum_{h\ge0}\delta^h G_h(A,C),
 \quad G_0=1,\quad \deg G_h\le2h.                     \tag{9}
\]
When e=1, C<=A-1. Extending to C=A adds only the displayed zero
A-C; it does not create a continued endpoint.

Temporarily work over \(\mathbb K(x)\) away from the root zeros
of the color products. The positive color product has root value
\[
 (1-k^{-2})^C H_{r,t}(x),\qquad
 H_{r,t}(x)=(x^{-2}Q_0^{r-t};Q_0)_t.                 \tag{10}
\]
After dividing by (10), its order-h coefficient is polynomial in
A,C of degree at most 2h, with rational x coefficients. Indeed,
split its NC+t factors into C complete residue cycles and a
partial cycle. The logarithmic order-h coefficient of each factor
is polynomial of degree at most h in its block index. Its finite
sum, whose endpoints are affine in A,C, has degree at most h+1.
Exponentiation gives the asserted 2h bound.

For the negative crossing the root color product is
\((1-k^2)^C(x^2Q_0^{1-s};Q_0)_t\); the same proof gives degree
at most 2h in B,C. Negative starting exponents cause no change
in the finite power-sum calculation. All temporary color-product
inverses will be removed in Section 5.

Finally the varying parts of \(Q^{(a-n)b}\) and \(Q^{-ab}\)
have order-h coefficients of degree at most 2h in A,B,C.
Their exponents are quadratic and
\(\log(Q/Q_0)=N^{-1}\log(1-\delta)\).
This proves the full local polynomial budget, including Cartan.

## 3. Differential realization and the bounded closed carries

Represent a block tuple by the polynomial monomial
\(Z_1^{A_1}\cdots Z_b^{A_b}\), keeping each residue as a finite
head. Let Gamma(L) send \(Z_j\) to \(\sum_iL_{ij}Z_i\);
then Gamma(L)Gamma(L')=Gamma(LL').

For a positive crossing fix r,s,t and put
\[
 f=\mathbf1_{s+t\ge N}.
\]
Its actual output blocks and residue-sum change are
\[
 (B+C+f,A-C-e),\qquad
             \text{output head sum}-\text{input head sum}=N(e-f).
                                                               \tag{11}
\]
Before these shifts, the root block coefficient
\[
 {A\choose C}(1-k^{-2})^C k^{-A-B+C}                 \tag{12}
\]
is exactly Gamma(L_+) on \(Z_1^A Z_2^B\).
At total normal order j, after the factor \((A-C)^e\), the
remaining multiplier in (12) is polynomial in A,B,C of degree
at most \(2(j-e)\); there is no term unless j>=e.

These polynomials are actual Euler operators. A,B are the input
Euler eigenvalues, and C is the first output Euler eigenvalue
minus B, before (11). Products of left and right Euler operators
give the specified polynomial. Right operators may be moved left
through Gamma(L_+): conjugation by an invertible linear substitution
preserves polynomial differential order. L_+ and its inverse have
Laurent entries in k. Thus each local head entry is a finite sum
of terms
\[
 Z_1^f\partial_{Z_2}^{\,e}D\,\Gamma(L_+),\qquad
 \operatorname{ord}D\le2(j-e),\quad \deg_{\rm Fr}D=0.   \tag{13}
\]
The derivative supplies A-C and the correct endpoint zero.
The multiplication supplies the other carry. Total order is at
most \(2j-e\), and the Frobenius degree shift is f-e.

For a negative crossing, instead set
\[
 e=\mathbf1_{t>s},\quad f=\mathbf1_{r+t\ge N},\quad
                    (A',B')=(B-C-e,A+C+f).
\]
Its base coefficient is
\({B\choose C}k^{A+B-C}(1-k^2)^C\), from Gamma(L_-).
The exact analogue of (13) is
\(Z_2^f\partial_{Z_1}^{\,e}D\Gamma(L_-)\), with the same bound.
This derives the inverse sign directly from its literal entry.

Compose along the original word, moving linear substitutions to
the right. Differential order is subadditive and is preserved by
these conjugations. There are finitely many head paths for fixed
N and word, although no block index is truncated. For a traced
head path, including the head-zero cut, (11) implies
\[
                         \sum f=\sum e\le j.          \tag{14}
\]
Every e costs at least one normal order. Root downward carries
therefore cannot occur without a compensating order-costly rise
in a closed path. All such cycles are included. The resulting
operator before Gamma(L_beta) has degree zero and order at most 2j.

The pivot is still present. For a_i=NA_i+r_i,
\[
 Q^{-\sum a_i}
 =Q_0^{-\sum r_i}(1-\delta)^{-\sum A_i-\sum r_i/N}.    \tag{15}
\]
Its order-h coefficient is a degree-h polynomial in block Euler
operators. Allocating h of the normal budget to (15) preserves
the bound 2j. The scalar x^c and the actual head phase and
grading \(\tau^{\sum r_i}\) remain as specified in (3).

## 4. The cut trace and its unchanged determinant

An elementary trace fact is needed. If D is a degree-zero polynomial
differential operator of order at most d, then
\[
 \operatorname{Tr}_{\rm Sym}(D\Gamma(B))
             \quad\text{has denominator at most}\quad
                         \det(I-B)^{d+1}.            \tag{16}
\]
This is a formal identity when B has positive formal degree and
requires no inverse of B.

The order-zero trace is \(\det(I-B)^{-1}\), proved coefficientwise
in [V, (3.1)]. Each homogeneous Weyl monomial
\(Z^\alpha\partial^\beta\), with \(|\alpha|=|\beta|\le d\),
is a linear combination of products of at most d vector fields
\(Z_i\partial_{Z_j}\). Normal ordering their product gives the
desired leading monomial plus smaller-order terms; induction
subtracts the latter. A vector field on Gamma(B) is the
infinitesimal left substitution \(B\mapsto(I+sE_{ij})B\).
Thus the trace is obtained by at most d polynomial directional
derivatives of the determinant inverse. Each raises its denominator
power by at most one. These identities hold on each finite
homogeneous polynomial space, proving (16).

Put \(T_0=\operatorname{diag}(0,1,\ldots,1)\), the ACTUAL
first-block-zero projector, and z=tau^N. Giving z to every block
variable gives the original grading on this projector. For each
degree-zero D from Section 3, finite-degree cyclicity yields
\[
\begin{split}
 \operatorname{Tr}\bigl(\Gamma(zI)\Gamma(T_0)
                         D\Gamma(L_\beta)\bigr)
 &=\operatorname{Tr}\bigl(D\Gamma(zL_\beta T_0)\bigr),\\
 \det(I-zL_\beta T_0)&=\det(I-zA_\beta)=D_\beta(x,\tau).
\end{split}                                                   \tag{17}
\]
Neither T0 nor A_beta has been inverted. Equations (14)--(17)
prove (6) over \(\mathbb K(x)\). Their numerator is polynomial
in tau: head grading is nonnegative and the trace differentiations
have polynomial matrix-entry numerators. No negative grading
powers have been introduced.

## 5. Removal of every apparent meridian pole

Clear the temporary x-only denominators:
\[
 V_{\beta,j}=
 \frac{A(x,\tau)}{g(x)D_\beta(x,\tau)^{2j+1}},
 \quad A\in\mathbb K[x^{\pm1},\tau],\
       0\ne g\in\mathbb K[x^{\pm1}].                 \tag{18}
\]
The original finite-sector definition says every tau coefficient
of V_beta,j is Laurent in x. Multiplication by D_beta^(2j+1)
therefore says A/g has Laurent-x coefficients. Since A/g is a
polynomial in tau, each of its finitely many coefficients is
Laurent; cancel g from each coefficient of A. This proves (6).
In particular the inverses of 1-x^(±2N) and all temporary head
factors disappear. Genuine determinant poles remain.

At tau=1 the exact normalization in [V, (4.1)] is
\[
 D_\beta(x,1)=x^{Nc}\Delta_K(x^{2N}).                 \tag{19}
\]
Thus each completed coefficient has only Alexander poles, of
order at most 2j+1, apart from Laurent meridian powers.
At j=0 it is precisely
\(F_N(M)/\Delta_K(M^{2N})\), \(M=-q_0x\), as in [V].
No zero and pole were evaluated separately.

## 6. Integral colors before any specialization

For ANY positive integer L, put x=q^(L-1) before taking a root.
The actual subspace W_L=span{v_a:a>=L} is a Verma submodule;
the quotient is the ordinary L-dimensional color. This follows
also directly from (2). If a>=L>a-n, the positive color product
contains \(1-x^{-2}Q^{L-1}=0\); its other strand rises b to b+n.
If b>=L>b-n, the negative product contains
\(1-x^2Q^{1-L}=0\); its other strand rises a to a+n.
Both signs therefore propagate any high flag along its physical
strand, in the actual swapped order.

A high flag in any contributing matrix path, even one first
created internally, cannot disappear. Follow it around the ONE
closed component: it must eventually reach the fixed cut index
zero, which cannot carry it. Thus every surviving intermediate
index is <L and has its literal quotient coefficient. Hence
\[
 V_\beta(q,q^{L-1};\tau)
      =\text{the finite graded quotient cut polynomial}.       \tag{20}
\]
This identity precedes root specialization; no infinite tail
survives along the curve.

At tau=1 this is the original reduced zero-framed C_L(q).
The ordinary closed pivots contribute x^(b-1). Restoring the
common Cartan scalar of each crossing and dividing by the
ordinary twist for zero framing contributes x^(-w).
Their product is exactly x^c in (3). The highest cut introduces
no additional dimension factor. This is the finite source
convention in [A], and uses no frozen root pivot.

## 7. High-color jets have degree at most their normal order

There is an exact generic parity identity. Set
\[
 G|a_1,\ldots,a_b\rangle=(-1)^{\sum_i i a_i}
                                  |a_1,\ldots,a_b\rangle .
\]
Replacing x by -x multiplies either crossing entry by
\((-1)^{a+b+n}\). Degree conservation identifies this with
the quotient of its output and input G signs. Thus
B_beta(q,-x)=G B_beta(q,x)G^(-1). Diagonal closure cancels G,
and c is even, so
\[
                       V_\beta(q,-x;\tau)=V_\beta(q,x;\tau).
                                                               \tag{21}
\]

Set x*=q0^(N-1). At color L=NR, R>=1, (21) removes the
R-dependent root sign, and the integral curve is
\[
 x=x_*(1-\delta)^{s_R},\qquad s_R=R/2-1/(2N).        \tag{22}
\]
At k=x*^N=±1, L_beta is diagonally conjugate to the one-cycle
strand permutation. Its deleted compression is nilpotent:
every remaining permutation path eventually hits the deleted
strand. The same argument holds at q0^i x* for any integer i.
Therefore
\[
 D_\beta(q_0^i x_*,\tau)=1\quad\text{for every }\tau.  \tag{23}
\]
Every coefficient of (6) is regular at these meridians.

Substitution of (22) into the rational normal coefficients is
legitimate coefficientwise. At order j, the fixed-x coefficient
of order l receives at most j-l Euler-x differentiations, with
coefficients polynomial in s_R of that degree. Equation (20)
identifies the result at tau=1 with the finite-color jet. Hence
\[
 [\delta^j]C_{NR}\!\left(q_0(1-\delta)^{1/(2N)}\right)
       \text{ is polynomial in R of degree at most j}.          \tag{24}
\]
This holds for every R>=1 at each fixed N>=2, with no parity
character. Its coefficient of R^j is
\[
 \frac{(-1/2)^j}{j!}(x\partial_x)^j
 \left.\frac{F_N(-q_0x)}{\Delta_K(x^{2N})}\right|_{x=x_*}.
                                                               \tag{25}
\]
Only l=0 and the highest displacement power in (22) contribute.
This coefficient may vanish; no bound in N is asserted.

The original meridian gives a useful coordinate without an offset.
Set \(Y=M^2=q^2x^2\). Evenness makes
\[
 \mathcal W_{N,K}(\delta,Y)=
  \widehat V_{N,K}\bigl(q(\delta),-\sqrt Y/q(\delta)\bigr)
                                                               \tag{25a}
\]
independent of the square-root choice; here the completion is
defined in (26) below. Each order-j coefficient is rational in Y
with denominator dividing \(\Delta_K(Y^N)^{2j+1}\), apart from
Laurent Y powers. Indeed an order-l fixed-x coefficient receives
at most j-l Euler derivatives in this substitution; each raises
the determinant pole order by at most one. Its bound is therefore
\(2l+1+(j-l)\le2j+1\). At the root \(q_0^{2N}=1\).
On the genuine color-NR curve one has EXACTLY
\[
 Y=(1-\delta)^R,\qquad
 \mathcal W_{N,K}(0,Y)=
             \frac{\mathfrak F_N(Y)}{\Delta_K(Y^N)},
 \quad \mathfrak F_N(M^2)=F_N(M).                    \tag{25b}
\]
The last definition is legitimate by (21) and the root comparison.
Thus the coefficient of R^j in (24) also equals
\[
 \frac{(-1)^j}{j!}(Y\partial_Y)^j
       \left.\frac{\mathfrak F_N(Y)}{\Delta_K(Y^N)}
       \right|_{Y=1}.                               \tag{25c}
\]
This retains the original meridian path; it does not freeze x
while differentiating a fixed-M family.

## 8. Canonical completion, uniqueness, and actual recurrences

Define
\[
 \widehat V_{N,K}(q,x)=
           \sum_{j\ge0}\delta^j V_{\beta,j}(x,1).     \tag{26}
\]
It is a formal series with rational meridian coefficients.
This does not assert generic convergence of (3) at tau=1.

The following elementary rigidity suffices. In
eta=log(1-delta), u=log(x/x*), a formal germ H(eta,u)
vanishing on every line u=s_R eta is zero. Its homogeneous
degree-n coefficient restricts to a polynomial of degree at
most n in s_R. Infinitely many distinct slopes force every
coefficient of that polynomial to vanish.

Two presentations of the same zero-framed knot have the same
C_NR(q) in (20), hence the same restrictions on all these lines
after (21). Equation (23) makes their coefficients regular germs.
Rigidity identifies the full germs; equality of a rational
meridian germ identifies the rational function. Thus (26)
is presentation independent.

It is also unique among formal rational-meridian series regular
at x*, even in x, and with the prescribed integral-color germs.
Without evenness, use one parity of R, still infinitely many
slopes, for the analogous local uniqueness at each root point.

Take any SUPPLIED actual generic color recurrence, in the
original meridian convention M=-q^L,
\[
 \sum_{i\in I}a_i(q,-q^L)\,C_{L+i}(q)=0,             \tag{27}
\]
for all sufficiently large positive L and a fixed finite
integer shift set I. Clear coefficient denominators first.
Its action on the completion is
\[
 H(q,x)=\sum_{i\in I}a_i(q,-qx)
                         \widehat V_{N,K}(q,q^i x).  \tag{28}
\]
All terms are regular at x*, by (23). On the genuine curve
x=q^(NR-1), the shifted colors NR+i are positive for large R.
The ANY-L statement (20) makes (28) exactly (27). Restrict here
to odd positive R: the genuine curve then has root x* itself,
and its logarithmic slope is s_R, with no sign gauge applied
to the possibly odd recurrence coefficients. These are still
infinitely many distinct slopes. Rigidity gives H=0 as a germ
and coefficientwise as rational functions.

Thus every supplied actual generic color annihilator acts on
this same selected all-root completion. No existence theorem
for a recurrence, minimality, equality of annihilator ideals,
or geometric-factor identification is inferred.

## 9. Coverage and scope

The general all-root rational-loop and recurrence statements
have existing literature coverage. Garoufalidis--Wheeler,
[“A lift of the colored Jones polynomial of a knot” (2026)](https://arxiv.org/abs/2603.01619),
Theorem 1.3 and Corollaries 1.5 and 1.9, state all-root loop
expansions via an etale Habiro ring and recurrence compatibility.
Their abstract and theorem/corollary statements were consulted
for coverage only. Willetts's unified
invariant already gives the root ADO/Alexander normalization
recorded in [V]. These are statement-level coverage, not proof
premises. No novelty is claimed for all-root rationality itself.

The internal addition here is the independent, literal proof
for (3): its bounded differential insertion, all closed carry
cycles, exact projector and determinant power, cancellation of
apparent poles, and original finite-color normal restrictions.
The finite high-color PBW theorem cannot simply replace Section 3:
at generic Verma meridian, unbounded block transfers survive
already at order zero.

Fixed-x, fixed-M=-qx, and integral-color normals are different.
The latter paths require their original chain rule. No generic
analytic completion, coefficient-size estimate, geometric
cycle comparison, or selected scalar lower follows.

The only complete proof directs are:

| Label | Complete source | SHA256 |
|---|---|---|
| V | notes/frobenius_verma_period.md | b11489368e7ac1106c7a5e760154b0713dfbc7eaf9b76193438df57b48041a90 |
| A | notes/adequacy_and_algebraic_periods.md | d471549b23c1dd982b7152ef0e90d6fb51d1be9a3c73c1b52ed0e41c9b2c0caa |

V supplies (2)--(5), the polynomial root trace, and the exact
Alexander/ADO normalization. A is used only for the original
finite reduced-color, ordinary cut and zero-framing convention;
its adequacy and degree theorems are not used. All factorial-jet,
carry, differential, pole-removal and slope-rigidity steps are
proved above without mathematical programs or tests.

