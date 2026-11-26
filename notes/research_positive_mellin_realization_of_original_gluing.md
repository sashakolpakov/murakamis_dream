# A positive Mellin realization of the original Conway gluing

Private written proof, 23 November 2026.

The original full Frobenius pairing is a Mellin residue of a positive
real measure. This identity is valid for arbitrary ordinary polynomial
products, so it retains the actual Conway multiplication, turns and
normal channels. A normalized positive integral also approximates the
squared original closing with an explicit error uniform in the level.
Its regularization parameter can be chosen from local source budgets,
without evaluating or dividing by the closed invariant.

These are finite-source identities and estimates. No geometric growth
estimate for the positive integral, or finite-exception theorem, follows.

## 1. Original source and the pure positive measure

Fix \(N\ge2\), and put \(D=N-1\), \(\eta=(-1)^D\). Use the actual
pair algebra, canonical representative and original cylindrical row:
\[
 P_N(z)=2T_N(z/2)+2,\qquad H_N=\mathbb C[z]/(P_N),\qquad
 \phi_N(h)=\eta N^2[z^D]\operatorname{rem}_{P_N}h .
 \tag{1}
\]
Here \(T_N\) is the ordinary Chebyshev polynomial. The monic \(P_N\)
has roots \(c_j=2\cos((2j+1)\pi/N)\), counted with multiplicity.
The original double roots and odd-level simple root are retained.
On \(x>2\), write
\[
 w=w(x)=\frac{x+\sqrt{x^2-4}}2>1,\qquad x=w+w^{-1}.
\]
Then \(P_N(x)=w^N+2+w^{-N}>0\). Define the pure positive measure
\[
                         d\nu_N(x)=\frac{dx}{P_N(x)},\qquad x>2.
 \tag{2}
\]
This is not the Ward current: its density has no hyperbolic-tangent
factor. Its source identification will instead be the exact residue
in the next section.

Every actual finite Conway packet has a canonical polynomial of degree
at most \(D\). All prescribed external scalar factors may be included
in that packet. Thus write its original scalar closing as
\(K_N=\phi_N(f_N)\), without changing its normalization.

For the other original Conway row \(\lambda_0(f)=f(c_0)\), use the
actual turn \(T e_i=e_{D-i}\). The exact identity
\(\phi_N(Tf)=\lambda_0(f)\) puts it in the same form. This retains
the full original packet and its prescribed closing.

## 2. Exact regularized gluing at every polynomial degree

For any ordinary polynomial \(h\), initially define
\[
 I_N(s;h)=\int_2^\infty x^{-s}\frac{h(x)}{P_N(x)}\,dx,
                    \qquad \Re s>\deg h-N+1.
 \tag{3}
\]
The zero polynomial causes no exception. The logarithm of the positive
real \(x\) fixes \(x^{-s}\).

**Theorem 1.** This integral continues meromorphically to \(\Re s>-1\),
and
\[
 \boxed{\qquad
          \phi_N(h)=\eta N^2\operatorname*{Res}_{s=0}I_N(s;h).
 \qquad}                                                       \tag{4}
\]
The residue in (4) depends only on the class of \(h\) in \(H_N\),
with no bound on its ordinary degree. In particular \(\phi_N(fg)\)
is the original full bilinear gluing.

**Proof.** Divide \(h=P_Nq+r\), where \(\deg r<N\), and let
\(a=[x^D]r\). Write \(q=\sum_k q_kx^k\). Direct integration gives
the continuation
\[
 I_N(s;h)=
 \sum_k q_k\frac{2^{k+1-s}}{s-k-1}
       +a\frac{2^{-s}}s
       +\int_2^\infty x^{-s}
                  \left\{\frac{r(x)}{P_N(x)}-\frac a x\right\}dx.
 \tag{5}
\]
The last integrand is \(O_{N,h}(x^{-2-\Re s})\) at infinity and
has no singularity at \(2\), since \(P_N(2)=4\). It is holomorphic
for \(\Re s>-1\), locally uniformly with the needed logarithmic
derivatives in \(s\). None of the polynomial terms has a pole at
zero. The residue is therefore \(a\), proving (4). In particular
every ordinary multiple of \(P_N\) has zero residue. \(\square\)

Equation (4) retains the full first normals, rather than only the
distinct-root values. For example, its original physical form is
\[
 \phi_N(h)=\eta\sum_{c\ {\rm double}}
       \{(4-c^2)h'(c)-ch(c)\}
                    +\mathbf1_{N\ {\rm odd}}h(-2).
 \tag{6}
\]
This is the same coefficient functional (1), as established by the
actual source calculus. There is no new normal at the odd simple node.

Consequently every finite original tensor contraction may replace each
Frobenius contraction by (4), leaving its polynomial kernels and
crossing coupons unchanged. With one variable per contracted algebra
copy, the resulting iterated Mellin residues reproduce the original
contraction. To justify the statement directly, expand its finite
multivariate polynomial numerator into monomials. In a sufficiently
far right half-plane in every \(s\)-variable all integrals converge
absolutely. Formula (5), applied coefficientwise, continues them;
their iterated residues commute and extract precisely the original
quotient coefficients. Arbitrary free spectators remain coefficients.
Thus unreduced trivalent products are allowed in this exact identity.

This is a bilinear regularized gluing, not a positive inner product at
the residue. Positivity of (2) does not make (6) positive.

## 3. A positive approximation to the squared original closing

For this section \(f\) is its **canonical** polynomial, \(\deg f\le D\).
Set
\[
 M=\max_{-2\le x\le2}|f(x)|,\qquad K=\phi_N(f),
 \qquad C_N=3+\tfrac12\log N.
\]
For every real \(\varepsilon>0\), define
\[
 \mathcal A_{N,\varepsilon}(f)=
 N^4\varepsilon\int_2^\infty
       (x/2)^{-\varepsilon}x^{-(N-1)}|f(x)|^2\,d\nu_N(x).
 \tag{7}
\]
This converges and is nonnegative; it is positive if \(f\ne0\).

**Theorem 2.** Uniformly for every \(N\ge2\), every canonical \(f\),
and every \(\varepsilon>0\),
\[
 \boxed{\quad
 0\le\mathcal A_{N,\varepsilon}(f)\le N^4M^2,\qquad
 \left|\mathcal A_{N,\varepsilon}(f)-|K|^2\right|
                            \le\varepsilon N^4M^2C_N.
 \quad}                                                       \tag{8}
\]
No nonzero-source or relative-precision hypothesis is imposed.

**Proof.** If \(f=0\), all assertions hold. Otherwise write
\(a_D=[z^D]f\) and \(H(\zeta)=\zeta^D f(\zeta+\zeta^{-1})\).
This is a polynomial, including when \(\deg f<D\). On the unit
circle its modulus is at most \(M\); hence the maximum principle
gives \(|H|\le M\) on the closed disk and \(H(0)=a_D\).
Each Taylor coefficient has modulus at most \(M\). Therefore, for
\(x\ge3\),
\[
 |H(1/w)-a_D|\le\frac{M}{w-1}\le\frac{2M}{x}.
 \tag{9}
\]
The last inequality follows directly from the displayed formula for
\(w(x)\). Together with \(|H|,|a_D|\le M\), this proves
\[
 \int_2^\infty
       \left||H(1/w)|^2-|a_D|^2\right|\frac{dx}{x}
 \le M^2\left\{\log(3/2)+\frac43\right\}<2M^2.
 \tag{10}
\]

Since \(f(x)=w^DH(1/w)\), (7) is exactly
\[
 \mathcal A_{N,\varepsilon}(f)=N^4\varepsilon
 \int_2^\infty (x/2)^{-\varepsilon}
                       R_N(x)|H(1/w)|^2\frac{dx}{x},
\]
\[
 R_N(x)=\frac{(1+w^{-2})^{-(N-2)}}{(1+w^{-N})^2}.
 \tag{11}
\]
We have \(0<R_N\le1\). Also \(w^{-N}\le w^{-2}\) and
\[
 1-R_N\le (N-2)w^{-2}+2w^{-N}
                   \le Nw^{-2}\le\frac{4N}{x^2}.
\]
Splitting at \(2\sqrt N\) gives
\[
 \int_2^\infty(1-R_N(x))\frac{dx}{x}
                         \le\tfrac12\log N+\tfrac12.
 \tag{12}
\]
The weight in (11) obeys
\[
 \varepsilon\int_2^\infty(x/2)^{-\varepsilon}\frac{dx}{x}=1.
 \tag{13}
\]
Thus (11) immediately gives the upper bound in (8).
Subtract \(N^4|a_D|^2=|K|^2\) using (13). In the resulting integral
use (10), (12), and \((x/2)^{-\varepsilon}\le1\). Its absolute value
is at most
\[
 \varepsilon N^4M^2
             \{2+\tfrac12\log N+\tfrac12\}
 \le\varepsilon N^4M^2C_N.
\]
This proves (8). The positive density and a nonzero polynomial give
strict positivity when \(f\ne0\). \(\square\)

The rightmost possible pole gives an equivalent exact normalization:
\[
 |\phi_N(f)|^2=N^4\operatorname*{Res}_{s=N-1}
               \int_2^\infty x^{-s}|f(x)|^2\,d\nu_N(x).
 \tag{14}
\]
Its residue is \(|a_D|^2\); it is zero if \(\deg f<D\).
For continuation the numerator means the ordinary polynomial
\(f(z)\overline{f(\bar z)}\), restricted to real \(x\).
The estimate (8), rather than just this coefficient identity, controls
the positive integral at a specified finite regularization parameter.

## 4. Source-only budgets and the unchanged volume target

Put \(M_N=\max_{[-2,2]}|f_N|\). Any supplied
\(B_N\ge\max(1,M_N)\) gives the explicit choice
\[
 \varepsilon_N=\frac1{N^6B_N^2C_N},\qquad
 \left|\mathcal A_{N,\varepsilon_N}(f_N)-|K_N|^2\right|
                                                   \le N^{-2}.
 \tag{15}
\]
Such a budget need not use the closed coefficient. In the original
Newton basis
\[
 e_i(z)=S_i^{-2}\prod_{j<i}(c_j-z),\qquad
 S_i=\prod_{r=1}^i2\sin(\pi r/N),\quad S_0=1,
\]
we have \(|e_i(x)|\le4^i/S_i^2\) on \([-2,2]\). If a known local
tensor budget gives \(L_N\ge\|f_N\|_{\rm Newton}\), take
\[
 B_N=\max\left(1,L_N\sum_{i=0}^{D}\frac{4^i}{S_i^2}\right).
 \tag{16}
\]
For completeness, products of recorded leaf norms and gate
Hilbert--Schmidt norm bounds supply \(L_N\) by induction: the norm
of each contracted output is at most the gate norm times the product
of its input norms. The actual turn is unitary in the Newton metric.
Known external scalar factors are included in this budget. No closed
invariant is required as an input, and no efficient algorithm is claimed.

For every fixed positive number \(V\), (15) implies the equivalence
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|K_N|=V
 \quad\Longleftrightarrow\quad
 \lim_{N\to\infty}\frac\pi N
              \log\mathcal A_{N,\varepsilon_N}(f_N)=V.
 \tag{17}
\]
Use \(\log0=-\infty\). If either limit is \(V>0\), its positive
quantity grows exponentially and dominates the absolute error
\(N^{-2}\). The ratio of the two quantities in (15) then tends to
one, proving the other limit. Positivity of \(V\) is essential here.

The finite-\(\varepsilon\) expression is a controlled approximation
to the original squared source, not a substituted knot invariant.
The canonical requirement in Theorem 2 is essential; Theorem 1 has
no such degree restriction. Full original channels and arbitrary fixed
short components remain allowed. A geometric estimate of the positive
integral in (17), with its actual packet and chosen parameter, is still
unproved. No Casson--Rivin growth or finite-exception case is asserted.

## Complete source and coverage readbacks

All complete matching texts below were read. The residue realization,
uniform estimate and budget argument above use only written proofs.

| Role | Complete text | Lines | SHA-256 |
| --- | --- | ---: | --- |
| Input | [Original dualizing residue](research_actual_source_dualizing_residue.md) | 408 | 806f8e4530736632830a15cff19f4c0f72e659fa6280d48005c4184a6ffc9afb |
| Input | [Full Conway boundary algebra](research_conway_full_boundary_quotient_gram.md) | 463 | debe56dbad8151b90d44d0fccbf0dcf33dafb780370e01c8acdadbd2939dc077 |
| Coverage | [Positive Ward measure](research_positive_ward_measure_and_coherent_cauchy_tail.md) | 492 | 18d2aa9142806d0acd744abbbb412843acd35bf18015b8c6fc73b23428a75096 |
| Coverage | [Cyclotomic Mellin residue](cyclotomic_mellin_residue.md) | 215 | 918cbf22fcfd6c5b156e133dd6f6f8c4dca75e6c0d7b1d70063a6ee5c172aff3 |
| Coverage | [Cauchy metric checkpoint](cauchy_metric_route_checkpoint.md) | 425 | 063766ead607758a71c40eebf07c4ae964a487bdbda65c29da52b6512bedb70a |

The Ward measure has its additional hyperbolic-tangent factor and an
existing full indefinite cut pairing. The cyclotomic Mellin residue
uses the ordinary-color generating variable. Neither is identified
with (2)--(5). Cheap Cauchy boundaries alone already have extensive
coverage; they do not supply the estimate (8) or geometric growth here.
No mathematical program, numerical test, build, git operation or edit
to a previous final or public manuscript was performed.
