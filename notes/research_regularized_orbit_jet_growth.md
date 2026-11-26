# Joint growth detected by finite blocks of orbit jets

Research deduction, 6 November 2026.

A fixed Laurent-degree window and a regular finite-order recurrence
give an approximation to the joint growth rate by finitely many
meridian jets at finitely many coalescing orbit points. The number of
jets may depend on the desired accuracy, but not on the level.
The proof keeps the central aliases \(Y^N-1\). It does not identify
the rate of the complete value, prove an all-level lower bound, or
assert that one fixed jet order attains the joint rate exactly.

## 1. Hypotheses and statement

Put \(Q_N=e^{2\pi i/N}\), \(T_Nf(Y)=f(Q_NY)\), and
\(\mathscr D_N=N^{-1}Y\partial_Y\). Suppose the Laurent polynomials
\(R_N\) satisfy, for one fixed integer \(A\ge1\),
\[
 \operatorname{supp}R_N\subset[-AN,AN],\qquad
 \sup_{|Y|=1}|R_N(Y)|\le e^{GN}
 \quad\hbox{for all sufficiently large }N,
 \tag{1}
\]
where \(G>0\) is fixed. Assume the exact equation
\[
 \sum_{i=0}^{d}b_{i,N}(Y)R_N(Q_N^iY)=\beta_N(Y),
 \qquad d\ge1,
 \tag{2}
\]
holds on a fixed complex neighborhood of
\(\{e^{i\theta}:|\theta|\le\alpha_0\}\), with \(0<\alpha_0<\pi\).
The coefficients are holomorphic there and converge, with every
fixed derivative, to \(b_{i,0}\). Require
\[
 b_{0,0}(e^{i\theta})b_{d,0}(e^{i\theta})\ne0
                   \qquad(|\theta|\le\alpha_0).
 \tag{3}
\]
These are the two end coefficients of the actual order-\(d\)
equation; an unexamined drop of degree in its classical symbol is
not allowed. Suppose also that \(\beta_N\) has fixed Laurent
support and polynomially bounded coefficients.

Define
\[
 \begin{split}
 U_0&=\lim_{\delta\downarrow0}\limsup_{N\to\infty}
       \frac1N\log\sup_{|z|<\delta}|R_N(e^z)|,\\
 \mathcal J_{N,K}
   &=1+\max_{\substack{0\le i<d\\0\le r<K}}
          |\mathscr D_N^rR_N(Q_N^i)|,\qquad
 a_K=\limsup_{N\to\infty}\frac1N\log\mathcal J_{N,K}.
 \end{split}
 \tag{4}
\]
Use \(\log0=-\infty\) in the first line.

**Theorem.** There is a constant \(\Gamma>0\), determined by the
regular recurrence on the fixed arc, such that for every
\(0<\alpha<\alpha_0/2\) one can choose a finite integer \(K_\alpha\)
with
\[
 0\le a_{K_\alpha}\le\max(0,U_0)
             \le a_{K_\alpha}+\Gamma\alpha .
 \tag{5}
\]
Consequently
\[
                    \sup_{K\ge1}a_K=\max(0,U_0).
 \tag{6}
\]
Thus every prescribed positive error admits a fixed finite jet
block. Neither (5) nor (6) replaces the \(d\) nearby points by
derivatives at \(Y=1\) alone.

## 2. Full-circle Hermite sampling with central aliases retained

Let \(P\) have Laurent support in \([-DN,DN]\), where \(D\) is a
fixed positive integer, and put \(K=2D+1\). Then
\[
 \sup_{|Y|=1}|P(Y)|
 \le C_D N
       \max_{\substack{0\le n<N\\0\le r<K}}
                         |\mathscr D_N^rP(Q_N^n)|.
 \tag{7}
\]
Here \(C_D\) is independent of \(N\) and \(P\).

Indeed, write \(P(Y)=\sum_k c_kY^k\). The discrete Fourier transform
of the \(r\)-th jet on the orbit gives, for \(0\le t<N\),
\[
 \frac1N\sum_{n=0}^{N-1}Q_N^{-nt}\mathscr D_N^rP(Q_N^n)
       =\sum_{\ell=-D}^{D}(\ell+t/N)^r c_{t+\ell N},
                  \qquad 0\le r<K.
 \tag{8}
\]
Coefficients outside the stated Laurent support are set to zero.
The square Vandermonde matrix has nodes
\(-D+t/N,\ldots,D+t/N\). Their differences are nonzero integers,
and its inverse is uniformly bounded for \(t/N\in[0,1]\).
For example its inverse entries are the coefficients of the
Lagrange polynomials with denominators
\(\prod_{\ell'\ne\ell}(\ell-\ell')\).
Thus each \(c_k\) is bounded by a fixed multiple of the right-hand
maximum in (7); summing at most \(2DN+1\) coefficients proves (7).
The same coefficient estimate gives
\[
 |P(e^z)|\le C_D N e^{DN|\Re z|}
       \max_{\substack{0\le n<N\\0\le r<K}}
                         |\mathscr D_N^rP(Q_N^n)|.
 \tag{9}
\]

Values alone cannot replace these jets. The family
\[
 R_N(Y)=e^{cN}(Y^N-1)^m,\qquad c>0,
 \tag{10}
\]
has fixed degree bound \(mN\), satisfies \((T_N-1)R_N=0\), and
has joint growth \(U_0=c\). Every orbit jet of order less than \(m\)
vanishes. Its order-\(m\) jet detects that rate. This is an exact
recurrence example, not an alternative knot period.
More generally the degree window in (1) bounds the multiplicity
of a global central factor \(Y^N-1\) by \(2A\).

The [existing central-source freedom](central_source_freedom_in_regular_profiles.md)
can preserve any preassigned jet budget by increasing the Laurent
degree constant. That observation does not remove the fixed
degree-window hypothesis here.

## 3. Jet transfer on the regular arc

For each fixed \(K\), differentiating (2) through order \(K-1\)
gives an exact recurrence for the scaled Euler jets. The operator
\(\mathscr D_N\) commutes with \(T_N\), so its product rule reads
\[
 \sum_{i=0}^d\sum_{r=0}^{j}
    \binom jr(\mathscr D_N^{j-r}b_{i,N})(Y)
       (\mathscr D_N^rR_N)(Q_N^iY)
                       =\mathscr D_N^j\beta_N(Y).
 \tag{11}
\]
For positive differentiation order,
\(\mathscr D_N^r b_{i,N}=O_K(N^{-r})\) uniformly on the arc.
In the matrix solving for the new \(K\)-jet, the diagonal is
\(b_{d,N}I_K\) and the strictly lower triangular part is
\(O_K(N^{-1})\). Its inverse therefore has diagonal
\(b_{d,N}^{-1}I_K\) and remainder \(O_K(N^{-1})\).
The analogous statement for backward transfer uses \(b_{0,N}\).

After collecting \(d\) consecutive jet blocks, the forward
transition is the ordinary companion matrix tensored with \(I_K\),
plus \(O_K(N^{-1})\). The backward matrix has the same property.
The row-sum norms of the two limiting companion matrices have a
fixed bound \(M\), independent of \(K\). Hence, for each fixed \(K\)
and all sufficiently large \(N\), both enlarged transition norms
are at most \(M+1\). The starting level may depend on \(K\);
this is not a bound uniform in a jet order growing with \(N\).

The differentiated affine source is polynomially bounded.
Iterating forward and backward from the block \(0,\ldots,d-1\)
therefore gives constants \(C_K,p_K\) such that
\[
 \max_{\substack{|\arg Q_N^j|\le\alpha\\0\le r<K}}
       |\mathscr D_N^rR_N(Q_N^j)|
 \le C_KN^{p_K}
            e^{\Gamma\alpha N}\mathcal J_{N,K}.
 \tag{12}
\]
The argument of an orbit point here is in \([-\pi,\pi]\).
The finitely many extra companion positions fit in the larger
arc for large \(N\). One may take any fixed
\(\Gamma>\log(M+2)/(2\pi)\), absorbing the bounded endpoint
steps into \(C_K\). Crucially, \(\Gamma\) is independent of the
fixed \(K\), although polynomial constants and starting levels
may depend on it.

## 4. Localizing the Hermite norm

Fix \(\alpha\) as above and put
\[
 w(Y)=\frac{2+Y+Y^{-1}}4,\qquad
 \rho_\alpha=\cos^2(\alpha/2)<1.
 \tag{13}
\]
Choose a fixed positive integer \(L\) so that
\[
                       G+L\log\rho_\alpha<-2.
 \tag{14}
\]
Set
\[
 W_N=w^{LN},\qquad P_N=W_NR_N,\qquad
 D=A+L,\qquad K_\alpha=2D+1.
 \tag{15}
\]
This \(P_N\) is only an auxiliary localization polynomial, unrelated
to the ordinary-color interpolation polynomial used in the
regularized-period decomposition. It has Laurent support in
\([-DN,DN]\), so (7)--(9) apply.

For every fixed \(r<K_\alpha\), the finite product rule gives
\[
 \begin{split}
 |\mathscr D_N^rW_N(e^{i\theta})|&\le C_{L,K_\alpha},
                                      &&-\pi\le\theta\le\pi,\\
 |\mathscr D_N^rW_N(e^{i\theta})|
   &\le C_{L,K_\alpha}\rho_\alpha^{LN-r},
                                      &&|\theta|\ge\alpha .
 \end{split}
 \tag{16}
\]
To check even the zeros at \(\theta=\pi\), expand the derivative
as a sum of terms with a falling factorial \((LN)_j/N^r\),
bounded derivatives of \(w\), and a factor \(w^{LN-j}\), where
\(j\le r\). For large \(N\), all these exponents are nonnegative.
No logarithmic derivative at \(w=0\) is taken.

On the unit circle, the coefficient bound
\(|[Y^k]R_N|\le\sup_{|Y|=1}|R_N|\) and (1) imply
\[
 \sup_{|Y|=1}|\mathscr D_N^rR_N(Y)|
                    \le C_{A,r}N e^{GN}.
 \tag{17}
\]
Combining the product rule, (12), and (14)--(17), the full orbit
jet maximum of \(P_N\) has upper exponential rate at most
\[
 \max\{a_{K_\alpha}+\Gamma\alpha,\,
                         G+L\log\rho_\alpha\}
                  =a_{K_\alpha}+\Gamma\alpha.
 \tag{18}
\]
The second term is negative, whereas \(a_{K_\alpha}\ge0\).

For small complex \(z\),
\[
 w(e^z)=\cosh^2(z/2),\qquad
 |\log w(e^z)|\le C|z|^2.
 \tag{19}
\]
In particular it is nonzero on a fixed small disk about zero.
Equation (9) divided by \(W_N(e^z)\), using (19), bounds the
joint upper rate on \(|z|<\delta\) by
\[
       a_{K_\alpha}+\Gamma\alpha+D\delta+CL\delta^2.
 \tag{20}
\]
Here \(\alpha,L,K_\alpha\) are fixed before \(N\) tends to
infinity. Letting \(\delta\downarrow0\) proves the last inequality
of (5).

Conversely, each of the fixed jets in (4) is bounded by Cauchy's
formula on any fixed small logarithmic disk. Its evaluation point
\(2\pi i j/N\) tends to zero, and the derivative factor
\(N^{-r}r!(2/\delta)^r\) has zero exponential rate.
Consequently \(a_K\le\max(0,U_0)\) for every fixed \(K\).
This proves (5). The sequence \(a_K\) is nondecreasing; taking
arbitrarily small \(\alpha\) proves (6).

## 5. The actual regularized meridian period

The actual degree hypothesis follows directly from the finite
crossings; it is not an additional asymptotic conjecture.
For a fixed braid with \(m\) crossings, \(b\) strands, and writhe
\(\mathfrak w\), use the exact formulas in
[the relative octahedral source](relative_octahedral_period.md),
Section 1. Each crossing contributes a monomial in the raw color
\(x\) whose exponent has absolute value at most \(3(N-1)\), and
one Pochhammer polynomial in \(x^2\) of degree at most \(N-1\).
The \(b-1\) pivotal entries and the residual framing scalar
contribute at most
\((b-1+|\mathfrak w|)(N-1)\) to the absolute \(x\)-exponent.
The statewise parity proof in
[squared-meridian descent](even_meridian_norm_descent.md), Section 2,
makes the total monomial exponent even. After \(x=-q_N^{-1}M\)
and \(Y=M^2\), every closed summand therefore has \(Y\)-exponents
in \([-A_FN,A_FN]\) for any fixed integer
\[
 A_F\ge
   \frac{3m+b-1+|\mathfrak w|}{2}+m+1.
 \tag{21}
\]
The root-phase chirps have modulus one; the Gaussian-binomial/factorial
coefficients are independent of the meridian and introduce no further
color exponents. Summation preserves this Laurent support bound.

Write the actual regularization as
\[
 F_N=S_NR_N+P_N^{\rm col},\qquad
 S_N=1+Y+\cdots+Y^{N-1},\qquad
 \deg P_N^{\rm col}\le N-2.
 \tag{22}
\]
Since \(S_N\) has constant coefficient one and leading coefficient
one, the lowest exponent of a nonzero \(R_N\) is that of
\(F_N-P_N^{\rm col}\), and its highest exponent is lower by
\(N-1\). Thus \(R_N\) has support in \([-A_FN,A_FN]\) too.
The identically zero remainder causes no exception.

The [whole-period growth theorem](research_regularized_period_growth_characteristics.md),
Sections 1--2, supplies (1), the exact affine equation (2), its
fixed-support polynomially bounded source, and all coefficient
bounds. To apply the present theorem at the complete point one
still needs the explicit regularity condition
\[
                         b_0(1,1)b_d(1,1)\ne0
 \tag{23}
\]
for the chosen actual polynomial operator. Continuity then gives
a fixed arc satisfying (3). Primitivity alone does not imply
(23); the classical symbol can lose degree or vanish identically
at \(Y=1\).

Under (23), (5)--(6) apply to the literal regular remainder,
with all ordinary-color polar terms retained in its exact affine
source. They concern a limsup of a finite block of scaled
meridian jets, not a lower bound for every level, not the
zero-jet complete evaluation, and not a geometric identification
of the joint growth rate. They also do not establish that a
single fixed \(K\) attains the supremum in (6).
