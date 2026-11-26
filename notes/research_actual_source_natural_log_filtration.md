# A natural logarithmic filtration of the actual marked source

Private written proof, 18 November 2026.

The actual signed crossings have a relative operator logarithm whose
order-\(h^j\) coefficient has differential order at most \(j+1\).
This filtration survives the finite word, its diagonal marks, original
pivot and framing. The highest-cut projector remains in the trace.
No logarithm of that trace is taken.

The resulting pole-defect count is useful but does not imply a
finite-point spectral carrier. The last section calculates an actual
scalar Borel action that produces a connector between two endpoints.

## 1. Literal crossings and their polynomial kernels

Put \(Q=e^h\), \(x=x_0e^{-h/2}\), and \(Y=x_0^2\). Work on a local
meridian domain with \(x_0\ne0\) and \(x_0^2\ne1\). These conditions
hold near the simple Alexander node used in [R]. The signed entries
are precisely [F, (2)]. Their classical substitutions are
\[
 L_+(x_0)=
 \begin{pmatrix}1-x_0^{-2}&x_0^{-1}\\x_0^{-1}&0\end{pmatrix},
 \qquad
 L_-(x_0)=
 \begin{pmatrix}0&x_0\\x_0&1-x_0^2\end{pmatrix}.
 \tag{1}
\]
Both are invertible. Here \(\Gamma(L)Z_j=\sum_iL_{ij}Z_i\).

For an operator \(A\) on the polynomial basis define its exponential
kernel by
\[
 \mathscr K_A(Z,p)=\sum_{\gamma\ge0}
                         (A Z^\gamma)\frac{p^\gamma}{\gamma!}.
 \tag{2}
\]
This is a formal generating series. In particular
\(\mathscr K_{\Gamma(L)}=\exp(Z^TLp)\). The normal symbol of a
differential operator \(A\) is \(e^{-Z\cdot p}\mathscr K_A\).
Differential order is degree in \(p\).

For the positive crossing set \(a=n+c\), retaining the other input
index \(b\). At \(h=0\), the summand of (2) is
\[
 \frac{U^n V^c W^b}{n!\,c!\,b!},\qquad
 U=(1-x_0^{-2})Z_1p_1,\quad
 V=x_0^{-1}Z_2p_1,\quad W=x_0^{-1}Z_1p_2.
 \tag{3}
\]
For the negative crossing put \(b=n+c\) and retain \(a\). Its
corresponding variables are
\[
 U=(1-x_0^2)Z_2p_2,\quad
 V=x_0 Z_1p_2,\quad W=x_0 Z_2p_1,
 \tag{4}
\]
with factorials \(n!,c!,a!\). Thus the three independent
nonnegative indices in either kernel have the classical generating
series \(e^{U+V+W}\).

The ratio of each quantum summand to its classical summand has
formal logarithm
\[
 \sum_{j\ge1}h^j v_j(N_1,N_2,N_3),\qquad \deg v_j\le j+1.
 \tag{5}
\]
This sharper logarithmic bound is before exponentiation. Indeed
[F, Section 2] proves that the order-\(r\) logarithm of a factorial
unit, or of a color product divided by its classical value, is a
polynomial in its index endpoints of degree at most \(r+1\).
Changing from \(1-Q\) to \(h\) only combines orders \(r\le j\).
The quadratic monomial in \(Q\) contributes only at order one.
Substitution \(x=x_0e^{-h/2}\) differentiates the meridian
coefficients without increasing index degree. The ratio of the
classical summand at \(x\) to that at \(x_0\) has logarithm linear
in the three indices. These observations prove (5) in the stated
fixed-\(Y\) coordinate, for both signs and all endpoints.

## 2. Connected polynomial moments and the ordinary symbol logarithm

Use the formal Poisson functional with three independent parameters:
\[
 \mathbb E_U (N)_a=U^a,\qquad
 \mathbb E_{U,V,W}\prod_i(N_i)_{a_i}=\prod_iU_i^{a_i}.
 \tag{6}
\]
Here \((N)_a=N(N-1)\cdots(N-a+1)\). This is an algebraic
functional on polynomials, with no positivity assumption.
Equations (3)--(5) give the exact kernel identity
\[
 e^{-U-V-W}\mathscr K_{R_h}
       =\mathbb E_{U,V,W}
                    \exp\!\left(\sum_{j\ge1}h^jv_j(N)\right).
 \tag{7}
\]

We need one degree estimate for its logarithm. For polynomials
\(f_1,\ldots,f_v\) of degrees \(d_1,\ldots,d_v\), their joint
cumulant under (6) has degree at most
\[
                         \sum_i d_i-v+1
 \tag{8}
\]
when \(v\ge1\); a negative bound means the cumulant is zero.
Here is a direct proof. Expand each polynomial in falling
factorials, and regard its factorial factors as labeled slots.
Products of factorial moments are indexed by identifications of
slots of the same color; two slots at the same vertex cannot be
identified. A block contributes one power of its Poisson parameter.
The cumulant is
\[
 \sum_{\pi\in\operatorname{Part}\{1,\ldots,v\}}
       (-1)^{|\pi|-1}(|\pi|-1)!
                        \prod_{B\in\pi}\mathbb E\prod_{i\in B}f_i.
 \tag{9}
\]
For a slot identification with \(c\) connected vertex components,
its coefficient in (9) is zero unless \(c=1\), when it is one.
The elementary identity used here is
\(\sum_{r=1}^c {c\brace r}(-1)^{r-1}(r-1)!=\mathbf1_{c=1}\);
its exponential generating series is \(\log(e^t)=t\).
A connected identification of \(v\) vertices reduces the number
of distinct slots by at least \(v-1\). This proves (8), including
constant vertices and several colors.

In the order-\(h^j\) logarithm of (7), a term with \(v\) vertices
has positive orders \(j_1+\cdots+j_v=j\). By (5) and (8) its
degree is at most
\[
                    \sum_i(j_i+1)-v+1=j+1.
 \tag{10}
\]
Consequently the ordinary, commutative logarithm of the normalized
kernel has this degree bound.

Now set \(A_h=R_h\Gamma(L)^{-1}\). Its kernel is
\(\mathscr K_{R_h}(Z,L^{-1}p)\), so its normal symbol \(S(h)\)
has constant term one. The linear substitution in \(p\) preserves
degree. We have proved
\[
 V(h):=\log S(h)=\sum_{j\ge1}h^jV_j(Z,p),
 \qquad \deg_pV_j\le j+1.
 \tag{11}
\]
Each coefficient is polynomial in \(Z,p\); every monomial has equal
\(Z\)-degree and \(p\)-degree. Its meridian coefficients are
holomorphic on the chosen domain.

## 3. Passing from the symbol logarithm to the operator logarithm

This step cannot be inferred merely by replacing indices with Euler
operators. We prove it in the normal-symbol algebra, whose exact
product is
\[
 f\star g=\sum_{\gamma\ge0}\frac1{\gamma!}
                  (\partial_p^\gamma f)(\partial_Z^\gamma g).
 \tag{12}
\]
The formula follows by applying the product rule to normally ordered
differential monomials.

Suppose \(D=\sum_{j\ge1}h^jD_j\), with
\(\deg_pD_j\le j+1\). Define
\(K_t=\exp_\star(tD)\) and \(F_t=\log K_t\), where the latter
logarithm is the ordinary commutative logarithm of symbols.
Formal differentiation gives
\[
 \partial_tF_t=
 \sum_\gamma\frac{\partial_p^\gamma D}{\gamma!}
                     e^{-F_t}\partial_Z^\gamma e^{F_t}.
 \tag{13}
\]
For \(\gamma\ne0\), each Bell term in the last factor is a
product of \(r\) positive-order derivatives of \(F_t\), with
\(1\le r\le|\gamma|\). If its total \(h\)-order is \(j\),
induction on that order bounds its differential degree by
\[
       j+1+r-|\gamma|\le j+1.
 \tag{14}
\]
Indeed the differentiated \(D\) loses \(|\gamma|\) powers of \(p\);
each of the \(r\) factors supplies at most its \(h\)-order plus
one. The term \(\gamma=0\) is exactly \(D\).

Every term with \(\gamma\ne0\) has at least two positive-order
vertices. Thus, more precisely,
\[
 [h^j]F_1=D_j+\text{an expression in }D_1,\ldots,D_{j-1}
                  \text{ of order at most }j+1.
 \tag{15}
\]
Starting from (11), solve (15) recursively for \(D_j\). It proves
that the actual relative operator has the unique formal expression
\[
 \boxed{\displaystyle
 R_h\Gamma(L)^{-1}
       =\exp\!\left(\sum_{j\ge1}h^j\mathcal D_j\right),
 \qquad \operatorname{ord}\mathcal D_j\le j+1.}
 \tag{16}
\]
The exponential in (16) is the operator exponential. All statements
are coefficientwise formal; no convergence of this logarithm is
asserted.

The class in (16) is closed under finite products. For completeness,
commutators satisfy
\[
 [\mathcal F_a,\mathcal F_b]\subseteq\mathcal F_{a+b-1},
 \tag{17}
\]
where \(\mathcal F_a\) denotes differential order at most \(a\).
This follows from (12), since the zero-contraction products cancel.
If \(e^{C(t)}=e^{tA}e^{tB}\), its right logarithmic derivative is
\(A+e^{t\operatorname{ad}A}B\), while that of \(e^{C(t)}\) is
\(\sum_{r\ge0}(\operatorname{ad}C)^r C'/(r+1)!\).
The constant operator in the latter series is the identity.
Recursive comparison in positive \(h\)-order, using (17), proves
the same order-\(j+1\) bound for \(C\). This establishes the needed
finite-product closure directly.

## 4. Marks, pivots, framing and the original highest-cut trace

Keep independent diagonal marks \(\mathbf w\) at the original word
stages, as in [M]. They are invertible linear substitutions.
Conjugation by them, or by any \(\Gamma(L_\pm)\), preserves
differential order and homogeneous degree zero. Moving these
classical substitutions right and applying the product closure
therefore proves (16) for the entire marked word.

The original pivot \(Q^{-T}\) is the exponential of \(-h\) times
the total Euler operator. The framing factor is
\(x^c=x_0^c e^{-ch/2}\), with the same even integer \(c\) as [F].
Both belong to the filtration and are retained. Consequently the
actual graded source has the exact formal expression
\[
 V_\beta(h,Y;\tau,\mathbf w)
   =x_0^c\operatorname{Tr}_{\mathrm{Sym}}\!
       \left[
        \exp\!\left(\sum_{j\ge1}h^j\mathcal D_j(Y,\mathbf w)\right)
                 \Gamma\!\left(\tau L_\beta(x_0,\mathbf w)T_0\right)
       \right],
 \quad T_0=\operatorname{diag}(0,1,\ldots,1).
 \tag{18}
\]
The trace is first taken degree by degree, on finite polynomial
spaces. The cyclic move giving (18) is the one in [F, (16)].
No inverse of \(T_0\), cut averaging, or logarithm of the trace
has been used. At each fixed order the rational grading completion
is the original one in [M].

There is an immediate pole-defect consequence. In the exponential
at normal order \(n\), a product with \(v\) vertices of orders
\(j_1+\cdots+j_v=n\) has differential order at most \(n+v\).
The determinant trace formula [F, (15)] gives its denominator at
most
\[
       \det(I-\tau L_\beta T_0)^{\,n+v+1}.
 \tag{19}
\]
At a simple determinant zero, a coefficient of pole order
\(2n+1-k\) can therefore receive such a contribution only if
\[
                   n-v=\sum_i(j_i-1)\le k.
 \tag{20}
\]
In particular at most \(k\) vertices have order greater than one,
and each has order at most \(k+1\). Arbitrarily many order-one
vertices remain, including their lower differential-order parts.
Equation (20) does not evaluate their contractions or give a
spectral carrier theorem.

## 5. A primitive keeps a connector, even for a scalar action

The exact exceptional full-clock family [R] is
\[
 F_0(\eta,\nu)=\frac r{w(\eta)}e^{a(\eta)\lambda},
 \quad w=\sqrt{1-4\sigma\eta},\quad
 a=\frac{1-w}{2\sigma},\quad \lambda=\mu\cdot\nu,
 \quad a'=\frac1w.
 \tag{21}
\]
No nonvanishing of the vector \(\mu\) is assumed. The scalar
quantum action \(Q=e^h\), under \(h=z^2\varepsilon\), has Borel
action \(e^{z^2I_\eta}\). Its order-\(z^2\) addition is exactly
\[
 I_\eta F_0
     =r\int_0^{a(\eta)}e^{\lambda s}\,ds
     =r\,\frac{e^{a(\eta)\lambda}-1}{\lambda},
 \tag{22}
\]
with the entire value \(ra(\eta)\) at \(\lambda=0\).
The path is the image under \(a\) of the initial \(\eta\)-path.

When \(\mu\ne0\), \(\lambda\) is a genuine clock coordinate.
For \(a\ne0\), (22) is not a finite sum of derivatives of
evaluation at the two points \(0,a\): such a sum would be
\(P(\lambda)e^{a\lambda}+Q(\lambda)\) with polynomials \(P,Q\).
Multiplying by \(\lambda\) and using independence of two distinct
exponentials over polynomials would require
\(\lambda P=r\), which is impossible. That independence follows
directly by choosing a ray on which \(a\lambda\) tends to positive
real infinity and then peeling off the exponential polynomial.

Its one-dimensional canonical Cauchy density is explicitly
\[
 g_{\rm prim}(\theta)
    =-r\log(1-a/\theta)
    =r\int_0^a\frac{ds}{\theta-s}
    =r\sum_{n\ge1}\frac{a^n}{n\theta^n}.
 \tag{23}
\]
On a circle \(|\theta|>|a|\),
\((2\pi i)^{-1}\int e^{\lambda\theta}g_{\rm prim}(\theta)\,d\theta\)
is (22), by termwise integration. The logarithmic branches at
zero and \(a\) have opposite monodromy. Splitting the outer cycle
into separate endpoint loops without retaining their connecting
banks is not a Cauchy deformation of this density.

Thus the natural filtration allows primitive/path carriers as well
as derivatives of point evaluations. The original scalar framing
also has a scalar order-one term, but this calculation does not
assert that its contribution survives cancellation with the other
terms of a particular full word. It rules out a derivative-only
carrier inference from the filtration itself, including for the
displayed exact \(Q\)-action.

The full marked source continuation, its localized Ward quotient,
and its finite-meridian character remain outside this theorem.

Complete direct sources, read in full with their used implications
checked:

| Label | Complete source | SHA256 |
|---|---|---|
| F | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |
| M | notes/research_marked_verma_full_certificate_transport.md | a2d94711bb80e69139e25b4932f0878440934c0586ddd0535dc24fcfd61987b4 |
| R | notes/research_rescaled_clock_exceptional_character.md | 310d88352c703038e8d3066be27e96cabb056929a289bc32337e32759c166cab |

Only written mathematics, source reads and hash checks were used.
Frozen proofs and public documents are unchanged.
