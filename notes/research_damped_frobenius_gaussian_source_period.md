# A convergent Gaussian period for the damped Frobenius source

Private written proof, 18 November 2026.

The reduced polynomial Verma word has a convergent graded trace
on a concrete positive Hilbert space. The space is the original
finite residue space tensored with a bosonic Fock space for the
Frobenius variables. A common positive metric makes the complete
Frobenius braid generators unitary. The retained carry operators
have bounded polynomial degree, so grading by
\(\tau=e^{-s/N}\), \(s>0\), makes the whole word trace class.
Distributing the grading gives an absolutely convergent paired
Gaussian integral with all original coefficients and marks.

The undamped source is still obtained by the specified rational
continuation, equivalently the fixed-\(N\) Abel limit. A finite
graded Casimir pair need not satisfy the original residue equation.
Its determinant derivative is therefore retained until that limit.
No identification with a positive geometric cycle is claimed.

The sole complete proof direct is F, the reduced Frobenius
trace and finite-cap transport theorem, pinned at the end.
All Hilbert-space, kernel and convergence arguments are below.

## 1. The full carry matrix

Use F's original conventions:
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-M/q,\quad r=m-1,\quad k=x^N .
 \tag{1}
\]
The braid has \(m\ge2\) heads and one-component closure.
Its fixed finite reduced word has \(L\) local factors;
insert an identity factor if the word is empty.
Its full polynomial lift is \(\widetilde B_\beta\).
Every divided power in the combined Verma crossing is retained.
The infinite polynomial lattice is independent of the physical
factorial basis; only residue indices use the nonzero
\((Q;Q)_a\), \(a<N\).

Write an index as \(NA+a\), where
\[
 a\in\mathcal R_N=\{0,\ldots,d\}^r,\qquad
 A\in\mathbb Z_{\ge0}^r.
\]
The vector-space identification is
\[
 z^{NA+a}\longleftrightarrow e_a\otimes Y^A.
 \tag{2}
\]
Let \(D_{\rm res}e_a=|a|e_a\), and let \(\mathcal N Y^A=|A|Y^A\).
The actual total occupation becomes
\[
                         J=D_{\rm res}+N\mathcal N.
 \tag{3}
\]

The block formulas of F give more than a trace identity.
For each local factor \(\ell\) there are polynomials
\(P_{\ell,ba}(Y;M)\) such that
\[
 (\widetilde A_\ell)_{ba}
       =M_{P_{\ell,ba}}\operatorname{Sym}\Gamma_\ell(k).
 \tag{4}
\]
Here \(M_P\) means multiplication by \(P\). The same
\(\Gamma_\ell\) occurs in every residue block. A nonzero
polynomial in (4) is homogeneous of degree
\[
                  p_{ba}=\frac{|a|-|b|}{N}
                       \in\{0,\ldots,r-1\}.
 \tag{5}
\]

Indeed, for a physical crossing, F's root Gaussian formula
leaves its finite residue coefficient and the symmetric-power
linear substitution. A recipient carry inserts the corresponding
factor \(Y_j\). The star formula does the same, with one factor
for each recipient carry. The diagonal reduced factor has no
carry. The total residue degree falls by \(N\) for each carry,
and the total occupation is unchanged. This proves (4)--(5),
including both inverse signs.

For a product use
\[
 \operatorname{Sym}\Gamma\,M_P
      =M_{\operatorname{Sym}\Gamma(P)}
                              \operatorname{Sym}\Gamma.
 \tag{6}
\]
Linear substitution preserves polynomial degree. Summing over
the finite intermediate residues therefore proves
\[
 (\widetilde B_\beta)_{ba}
             =M_{P_{ba}(Y;M)}\operatorname{Sym}\Gamma_\beta(k),
 \tag{7}
\]
again with degree (5). In particular the number of carries in
any nonzero full path is at most
\(\lfloor r(N-1)/N\rfloor\le r-1\), independently of word length.
All original common crossing and external framing scalars can be
included in \(P\), or kept identically on both sides.
These polynomials are holomorphic in the fixed-root meridian
germ. They are not obtained by specializing individual singular
tetrahedral factors.

## 2. A common positive Frobenius metric

Put
\[
              u=N\log M,\qquad
              k=k_0e^u,\qquad k_0=(-1)^{N+1}.
 \tag{8}
\]
F identifies the degree-one matrices \(\Gamma_i(k)\) with the
quotient of the \(m\)-variable Burau matrices by their fixed
linear form. At \(k_0=1\), those unreduced matrices are adjacent
permutations. At \(k_0=-1\), one fixed diagonal sign change
conjugates all of them to the same permutations. Consequently
their reduced action factors through the finite group \(S_m\).

Choose any positive Hermitian metric on the degree-one quotient
and average its pullbacks over \(S_m\):
\[
 H_{k_0}=\frac1{m!}\sum_{\sigma\in S_m}
                         R_{k_0}(\sigma)^*R_{k_0}(\sigma).
 \tag{9}
\]
This is positive and every \(\Gamma_i(k_0)\), of either sign,
is unitary for it. There are only two choices of \(k_0\).
Thus the metrics, their condition numbers and the following
constants are independent of \(N\), apart from that recorded
parity choice. They concern Frobenius variables, not unitarity
of the original finite quantum crossings.

For some \(u_0>0\) and \(C\ge1\), all local matrices in the
fixed word satisfy
\[
       \|\Gamma_\ell(k_0e^u)\|_{H_{k_0}}\le e^{C|u|}
                       \qquad (|u|\le u_0).
 \tag{10}
\]
To prove this, their entries are fixed Laurent functions of
\(k\), with bounded derivatives on a small disk in \(u\).
Subtract the unitary value at zero and use the triangle
inequality. Enlarge \(C\) for the finitely many factors,
their inverses and both parity choices.

Choose
\[
       0<s\le1,\qquad
       |u|\le c s,\qquad
       c\le\min\{u_0,1/(4LC)\}.
 \tag{11}
\]
Then
\[
 e^{-s/L}\|\Gamma_\ell(k_0e^u)\|\le e^{-3s/(4L)},\qquad
 e^{-s}\|\Gamma_\beta(k_0e^u)\|\le e^{-3s/4}.
 \tag{12}
\]
At \(u=0\), every \(s>0\) is permitted.

## 3. Trace-class estimates, including meridian normals

In orthonormal linear coordinates for \(H_{k_0}\), let
\(\mathcal F_{H_{k_0}}\) be the Bargmann space with
\[
 \langle Y^A,Y^B\rangle=\delta_{AB}A!,\qquad
 d\mu(Y)=\pi^{-r}e^{-|Y|^2}\,d^{2r}Y .
 \tag{13}
\]
This is the bosonic Fock metric induced by (9). Give the finite
residue vectors \(e_a\) the orthonormal metric, and set
\(\mathscr H_N=\mathbb C^{\mathcal R_N}\otimes\mathcal F_{H_{k_0}}\).
This defines a Hilbert completion of (2); it makes no claim
about the conditioning of the original factorial gauge.

If \(P\) is homogeneous of degree \(p\), then on degree \(n\)
\[
 \|M_P\|\le \|P\|_{\rm coeff}
               \sqrt{\frac{(n+p)!}{n!}} .
 \tag{14}
\]
Here the coefficient norm is the sum of absolute monomial
coefficients in these orthonormal coordinates. For one
coordinate multiplier its norm on degree \(n\) is at most
\(\sqrt{n+1}\). Iterating gives (14) for each monomial, and
the triangle inequality gives it for \(P\).
Also
\(\|\operatorname{Sym}^n\Gamma\|\le\|\Gamma\|^n\), by its
realization on the symmetric subspace of the tensor power.

Define the damped word initially on polynomials by
\[
              T_{N,s}(M)=e^{-sJ/N}\widetilde B_\beta(M).
 \tag{15}
\]
The block (7) sends degree \(n\) to degree \(n+p_{ba}\).
Equations (12)--(14), and
\(\dim\operatorname{Sym}^n\mathbb C^r=\binom{n+r-1}{r-1}\),
give the trace-norm bound
\[
 \|T_{N,s}(M)\|_1
 \le C_r A_N\sum_{n\ge0}
       (n+1)^{r-1+(r-1)/2}e^{-sn/2}
 \le C_r' A_N s^{-(3r-1)/2}.
 \tag{16}
\]
Here \(A_N\) is the sum, over \(a,b\), of the coefficient
norms of \(P_{ba}\), bounded on the fixed disk \(|u|\le u_0\).
It is finite. To justify the first inequality, take the
trace norm of each finite-rank degree block, bounded by its
rank times operator norm, and sum. The resulting sum is
finite and hence defines a trace-class extension. For the
last inequality compare the exponentially decreasing sum
with the integral after splitting off its first bounded
number of terms. The exponent is also valid when \(r=1\).

The coefficient bound has at worst exponential finite-source
cost. With the original common scalar product denoted
\(\sigma_N(u)\), one may take
\[
              A_N\le e^{C_\beta N}
                            \sup_{|u|\le u_0}|\sigma_N(u)|.
 \tag{17}
\]
No scalar line has been discarded in (17). Here is an
elementary bound for the remaining coefficients. Write
\(S_j=|(Q;Q)_j|\), \(j<N\). If \(j\le N/2\), then
\[
 S_j\ge(4/N)^j j!\ge(4j/(eN))^j\ge e^{-N/4}.
 \tag{18}
\]
The first inequality uses concavity of sine on
\([0,\pi/2]\); the second follows by integrating \(\log t\).
The minimum of \(t\log(4t/e)\), \(0\le t\le1/2\), is
\(-1/4\). If \(j>N/2\), the identity
\(S_jS_{N-1-j}=N\), together with \(S_l\le2^l\), gives
\(S_j\ge N2^{-N}\). Thus \(e^{-N}\le S_j\le2^N\) for all
\(j<N\). Every finite residue Gaussian multinomial has only
a fixed number of these factors. The residual color products
in F's Verma entries have at most \(N\) uniformly bounded
factors; the powers of \(x\) have exponents \(O_\beta(N)\)
and \(|x|=e^{\operatorname{Re}u/N}\).
There are polynomially many residue choices for a fixed word.
Its bounded-degree carry multipliers are transformed only by
fixed bounded matrices. These facts prove (17).

The series of degree blocks converges locally uniformly in
trace norm on (11), so \(T_{N,s}\) is holomorphic there.
On the smaller disk \(|u|\le cs/2\), Cauchy's formula and
\(\partial_M=(N/M)\partial_u\) give, for each fixed \(j\),
\[
 \|\partial_M^j T_{N,s}(M)\|_1
       \le C_{\beta,j} A_N (N/s)^j
                                  s^{-(3r-1)/2}.
 \tag{19}
\]
The full meridian dependence of \(P,\Gamma,\sigma_N\) is
inside this estimate. These are fixed-\(q_N\) meridian
normals; the argument supplies no moving-\(q\) neighborhood.

## 4. The whole paired Gaussian period

Every lifted local factor preserves \(J\) on polynomials.
Distribute the grading equally:
\[
 T_\ell=e^{-sJ/(NL)}\widetilde A_\ell,\qquad
                     T_{N,s}=T_L\cdots T_1.
 \tag{20}
\]
Each \(T_\ell\) has its own trace-class extension by the
same proof. Their product equals (15) on a dense polynomial
subspace and hence on \(\mathscr H_N\).

Put \(\delta=s/L\). In the orthonormal coordinates of (13),
the exact residue-block kernel is
\[
 \mathcal K_{\ell,ba}(Z,\overline W)
 =e^{-\delta|b|/N}P_{\ell,ba}(e^{-\delta}Z;M)
                  \exp\!\big(e^{-\delta}Z^t\Gamma_\ell
                                                 \overline W\big).
 \tag{21}
\]
The matrix convention is that \(\Gamma\) acts on the column
of degree-one basis vectors. Thus the kernel of its symmetric
power is \(\exp(Z^t\Gamma\overline W)\). Formula (21) follows
by expanding that exponential and using
\(\int Z^A\overline Z^B\,d\mu=\delta_{AB}A!\).

For a fixed function \(f(K_0)\) of the finite Cartan eigenvalues,
insert its diagonal residue matrix at the closing interface.
The trace is exactly
\[
 \sum_{a_0,\ldots,a_{L-1}\in\mathcal R_N}
 f(x_0^rQ^{-|a_0|})
 \int\prod_{\ell=1}^L
       \mathcal K_{\ell,a_\ell a_{\ell-1}}
                     (Z_\ell,\overline Z_{\ell-1})
                \prod_{\ell=0}^{L-1}d\mu(Z_\ell),
 \quad a_L=a_0,\quad Z_L=Z_0,
 \tag{22}
\]
where \(x_0=-q^{-1}\). Both the finite residue sum and the
whole continuous cycle are part of the specified source.

This integral is absolutely convergent before contraction.
Indeed, by (12), all cross terms in its absolute exponential
are bounded by
\(\rho |Z_\ell||Z_{\ell-1}|\), with
\(\rho=e^{-3s/(4L)}<1\). Therefore
\[
 -\sum_\ell|Z_\ell|^2+
       \rho\sum_\ell|Z_\ell||Z_{\ell-1}|
              \le -(1-\rho)\sum_\ell|Z_\ell|^2.
 \tag{23}
\]
The remaining factors are polynomials of bounded degree.
Fubini and Gaussian monomial orthogonality are consequently
legitimate in (22). This proves the period identity directly,
in addition to the trace-class argument. Fixed meridian
derivatives satisfy the same assertion, either by (19) or by
the additional polynomial factors from differentiating (21).

There is a limited genuine contour transport here. Regard
\(Z_\ell,W_\ell\) as independent complex variables and use
the holomorphic Gaussian form whose restriction to
\(W_\ell=\overline Z_\ell\) gives (22). Translate that cycle
by arbitrary bounded constants in all \(Z_\ell,W_\ell\).
The quadratic part at infinity is unchanged; translation
adds only linear terms and a constant to its exponent.
Equation (23) then bounds the ends by a polynomial times
\(\exp(-c_s|Z|^2+C_s|Z|)\). Stokes on truncated cylinders,
followed by this vanishing boundary bound, proves equality
of the translated and original periods. This concerns the
combined entire kernels (21), not the singular separate
tetrahedral factors.

## 5. The rational trace, its normals, and the Abel endpoint

Set \(\tau=e^{-s/N}\). Since (15) is trace class and preserves
\(J\), its ordinary trace is the absolutely convergent sum
of its finite total-\(J\) sector traces. Each such trace is
basis independent and equals the corresponding coefficient
of F's graded series. Thus F's coefficientwise identity is
an analytic equality on (11):
\[
 \operatorname{Tr}_{\mathscr H_N}\big(f(K_0)T_{N,s}(M)\big)
 =\widetilde t_f(M;e^{-s/N})
 =\frac{t_f(M;e^{-s/N})}
               {d_\beta(x(M)^N;e^{-s})}.
 \tag{24}
\]
The denominator is nonzero there by (12).
Equation (24), and every fixed meridian derivative, retain
the complete divided powers and original Cartan marks.
This does not assert absolute convergence of the ungrouped
diagonal entries in the original Frobenius monomial basis:
that basis need not be orthonormal for \(H_{k_0}\).

At \(M=1\) the denominator is explicitly
\[
 d_\beta(k_0;e^{-s})
       =\frac{1-e^{-ms}}{1-e^{-s}}\longrightarrow m.
 \tag{25}
\]
This follows from the nontrivial \(m\)-cycle eigenvalues.
For each fixed \(N\), the rational right side of (24) is
holomorphic near \((M,\tau)=(1,1)\). Consequently its
\(s\downarrow0\) limit, including fixed meridian derivatives,
is precisely F's prescribed rational trace. No undamped
trace-class assertion follows from this limit.

For clarity keep the finite-grade source bookkeeping explicit.
Use \(f=P_{\mathfrak o}K_0^{\pm1}\) or sum over the pairs.
Write \(t_{s,\pm}\), \(\widetilde t_{s,\pm}\), and
\(d_s(M)=d_\beta(x(M)^N;e^{-s})\). Then
\[
 t_{s,\pm}=d_s\widetilde t_{s,\pm},\qquad
 t_{s,\pm}'=d_s'\widetilde t_{s,\pm}
                              +d_s\widetilde t_{s,\pm}'.
 \tag{26}
\]
There is no assumption that
\(t_{s,+}(1)-t_{s,-}(1)=0\) for \(s>0\).
The original source is exactly the following fixed-\(N\) limit:
\[
 \begin{split}
 \Phi_{\mathfrak o}
 =\lim_{s\downarrow0}\bigg\{&
 d_s(1)\left[
 \frac{\widetilde t_{s,+}(1)+\widetilde t_{s,-}(1)}
                                                    {2\varepsilon}
 +\frac{\widetilde t_{s,+}'(1)-\widetilde t_{s,-}'(1)}
                                                    {2\varepsilon m}
 \right]\\
 &+\frac{d_s'(1)}{2\varepsilon m}
          \big(\widetilde t_{s,+}(1)-\widetilde t_{s,-}(1)\big)
 \bigg\},\qquad \varepsilon=(-1)^{(N+1)r}.
 \end{split}
 \tag{27}
\]
This follows by substituting (26) into F's first-jet row
and taking the rational limit. Only at that endpoint does
the original residue identity cancel the last line.
At finite \(s\) the bracket is a specified first-jet
expression, not a claimed finite part of a meromorphic
graded source with a nonzero residue. All external scalar
normalization lines remain as in F.

The limits \(N\to\infty\) and \(s\downarrow0\) have not been
interchanged. The constants in (16), (19) and (23) deteriorate
as \(s\downarrow0\). Nor does a separately chosen geometric
component automatically satisfy the residue cancellation
in (27).

## 6. Scope of the analytic improvement

Equations (21)--(24) give an actual convergent, whole-word
Gaussian period for the damped untruncated source, rather
than only a formal graded series. The metric and cycle are
specified, the full finite residue/carry data are retained,
and bounded translations have controlled ends.
The original value and first meridian jet are obtained by
the exact Abel/rational prescription (27).

On an original occupation region with \(J=O(N)\), the
grading factor \(e^{-sJ/N}\) contributes only an order-one
logarithm. This does not prove a global asymptotic comparison
between a fixed \(s>0\) period and its Abel endpoint.
The positive metric is on Frobenius block variables; these
are not thereby identified with semiclassical shape variables.
No positive geometric contour, component coefficient,
noncancellation, or uniform partial-filling estimate has
been obtained. The original short-filled knot may be used
as a fixed braid exactly as in F.

## Complete proof direct

F: notes/research_reduced_frobenius_trace_and_cap_transport.md,
SHA256 647539c72374cecd69a4decc6531684852f8f3d34c889972103abd24db9bd3a8.

The complete matching F was read nontruncated in the active
author sequence. Its full polynomial lattice, carry formulas,
reduced classical quotient, exact trace identity, and original
first-jet source are the only imported proof results.
The finite coherent-period coverage does not supply the
infinite trace-class assertion proved here. No numerical
calculation or mathematical program is used.
