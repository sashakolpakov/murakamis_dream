# Exact literal transfers and the limitation of node-magnitude induction

Research deduction, 7 November 2026. The original three/four
contraction preserves a finite polynomial message space exactly.
There is also an exact weighted-norm propagation formula on its
physical nodes. That formula is the absolute row-sum bound, with
no cancellation advantage. Moreover neither conditional kernel
can be made asymptotically entrywise nonnegative by independent
input and output phase gauges. These facts constrain an inductive
proof of the global boundary sign; they do not rule out a smaller
class retaining correlated holomorphic phase data.

## 1. Exact prefix, suffix and closing operations

Use the original source of
[conditional torus composition](research_mixed_conditional_torus_composition.md):
\[
 r=e^{-2\pi i/N},\quad P_a=(r;r)_a,\quad
 p_j(X)=(rX;r)_j,\quad
 C_{\beta,N}(X,Y)=\sum_{j<N}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\beta}}.
 \tag{1}
\]
All \(P_a\), \(a<N\), are nonzero. Put
\[
 W_{\alpha,N}(X)=\{d_N(X)(1+X^{-N})\}^{\alpha},
 \qquad \alpha,\beta\in\{0,1\}.
 \tag{2}
\]
Keep every original normalization outside the following explicitly
normalized algebraic transfer. For a polynomial \(f\) of degree
less than \(N\), define
\[
 (\mathsf T_{\alpha\beta,N}f)(Y)
   =N\,\operatorname{CT}_X
          [f(X)W_{\alpha,N}(X)C_{\beta,N}(X,Y)].
 \tag{3}
\]
It is again a polynomial of degree less than \(N\). The initial
literal first cap \(U_{\alpha,N}(w,X)\) belongs to this space.

**Proposition 1.** The exact physical-node formula is
\[
 (\mathsf T_{\alpha\beta,N}f)(Y)
       =\sum_{a=0}^{N-1}
          \frac{f(r^a)}{P_a^\alpha}C_{\beta,N}(r^a,Y).
 \tag{4}
\]
It is an identity in the free complex variable \(Y\), at both
parities and for arbitrary coefficients of \(f\).

*Proof.* The \(X\)-band of \(fC_\beta\) is contained in
\([-N+1,N-1]\). At \(\alpha=0\), node averaging extracts
only its constant coefficient. At \(\alpha=1\), multiplication
by the original degree-\((N-1)\) polynomial \(d_N\) puts the
band in \([-N+1,2N-2]\). Node averaging now extracts exactly
the coefficients of \(X^0\) and \(X^N\). Multiplication by
\(1+X^{-N}\), followed by \(\operatorname{CT}\), extracts
exactly the same two coefficients. Finally \(d_N(r^a)=P_a^{-1}\).
The \(Y\)-degree assertion follows directly from (1). \(\square\)

The two retained Fourier sectors have not been identified. For
\(\alpha=1\), if \(F(X,Y)=f(X)d_N(X)C_{\beta,N}(X,Y)\), then
\[
 \mathsf T^{(0)}f=N[X^0]F,\qquad
 \mathsf T^{(1)}f=N[X^N]F,\qquad
 \mathsf T=\mathsf T^{(0)}+\mathsf T^{(1)}.
 \tag{5}
\]
Formula (4) applies to their sum, not separately to either one.
The fact that \(X^{-N}=1\) at the physical nodes does not make
the two constant-term integrals equal.

At the other end the exact terminal polynomial
\(\mathcal V_{\epsilon,N}(w,Y)\) has band \([-N+1,0]\).
For every \(g\) with that band,
\[
 (\mathsf S_{\beta,N}g)(X)
   =N\,\operatorname{CT}_Y
       [C_{\beta,N}(X,Y)W_{\beta,N}(Y)g(Y)]
   =\sum_{b<N}C_{\beta,N}(X,r^b)\frac{g(r^b)}{P_b^\beta}
 \tag{6}
\]
has the same negative band. The identical coefficient argument
proves (6). Thus both literal ends admit exact finite-dimensional
induction, with dimension \(N\), without an approximate packet.

When they meet, the normalized closing functional is the signed
bilinear pairing
\[
 N\,\operatorname{CT}_X[f(X)W_{\alpha,N}(X)g(X)]
             =\sum_{a<N}\frac{f(r^a)g(r^a)}{P_a^\alpha}.
 \tag{7}
\]
There is no conjugation in (7). It is not a positive quadratic
form or a norm. All these formulas retain the original terminal
contraction, diagonal correction and Laurent sectors.

## 2. The sharp propagation bound for a node-magnitude class

Let \(\omega_a>0\) and \(\nu_b>0\) be arbitrary weights; they
may depend on \(N\) and on the actual reference. Define
\[
 \|f\|_\omega=\max_{a<N}\frac{|f(r^a)|}{\omega_a}.
 \tag{8}
\]
Because \(N\) distinct samples determine a polynomial of degree
less than \(N\), this is a norm on the entire message space.
The exact operator norm in (3) is
\[
 \|\mathsf T_{\alpha\beta,N}\|_{\omega\to\nu}
   =\max_{b<N}\frac1{\nu_b}
       \sum_{a<N}\frac{|C_{\beta,N}(r^a,r^b)|}
                            {|P_a|^\alpha}\,\omega_a .
 \tag{9}
\]
The triangle inequality proves the upper bound. For a maximizing
column \(b\), prescribe
\(f(r^a)=\omega_a e^{-i\arg(C_\beta(r^a,r^b)/P_a^\alpha)}\)
at every nonzero coefficient, with arbitrary unit phases at zeros.
Polynomial interpolation realizes these values simultaneously.
This \(f\) has norm one and attains the displayed sum at \(b\),
proving equality.

Thus the class of all polynomial messages satisfying only (8)
is closed under transfer with exactly the absolute row-sum cost.
Holomorphy and degree alone do not improve that cost. The analogous
formula holds for (6). Extra bounds on whole complex contours, or
restrictions to the actual phase-correlated messages, can change
the operator norm; they are additional information and have not
been ruled out by this argument.

## 3. No diagonal positive gauge for either original kernel

The failure of positivity is explicit at arbitrarily large levels.
Let \(N\ge7\). In the node matrix \(C_\beta(r^a,r^b)\), the row
\(a=N-1\) and column \(b=N-1\) consist of ones, since their
positive-index Pochhammer terms vanish. At \(a=0,b=N-2\),
only \(j=0,1\) survive, and
\[
 C_{\beta,N}(1,r^{N-2})
   =1+\frac{P_1(1-r^{-1})}{P_1^{2+\beta}}
   =1-\frac{r^{-1}}{P_1^\beta}.
 \tag{10}
\]
Consequently the nonzero \(2\times2\) cross-ratio formed by
rows \(0,N-1\) and columns \(N-2,N-1\) equals (10).
All independent nonzero row and column gauges cancel in this
ratio, including the original factors \(P_a^{-\alpha}\) in (4).

Write \(x=\pi/N\). The two values are
\[
 \begin{split}
 \beta=0:\quad&1-e^{2ix}
                     =-2i e^{ix}\sin x,\\
 \beta=1:\quad&-\tfrac12+2\sin^2x
                           +i\,\frac{\cos3x}{2\sin x}.
 \end{split}
 \tag{11}
\]
For \(N\ge7\), the first has negative imaginary part and the
second positive imaginary part. In particular neither ratio is
positive real. A matrix whose four entries are strictly positive
real has a positive cross-ratio. Therefore no independent input
and output diagonal gauges make either original transfer matrix
entrywise nonnegative.

The obstruction does not disappear asymptotically: the arguments
of the two cross-ratios tend respectively to \(-\pi/2\) and
\(+\pi/2\). Hence even making these four nonzero entries positive
up to relative \(o(1)\) errors by such gauges is impossible.
This conclusion concerns the literal source at every sufficiently
large \(N\), not an isolated exceptional level.

## 4. Consequence for a calibrated boundary induction

Equations (3)--(7) give an exact operation-preserving representation,
but not a positive cone or a calibrated boundary sign. On the
unrestricted node-magnitude class, (9) is the best possible bound;
it cannot exploit cancellation inside the literal \(U,\mathcal V\)
or the transferred message. The signed closing functional (7)
also admits nonzero polynomial inputs with zero pairing, so norm
control alone cannot establish its nonzero geometric coefficient.
No such zero is asserted for an actual mixed word.

The stationary Hessian and forgetting estimates control the
original local phase and safe interior completion. They do not
restrict the arbitrary phase-aligned interpolants used to saturate
(9), nor do they identify the literal endpoint messages with a
positive node cone. A successful smaller inductive class must
therefore retain information that excludes those interpolants:
for example a coherent phase germ together with a global,
operation-controlled remainder on the actual contour and its
complement. Merely knowing finitely many local jets is insufficient,
as the [original turn-remainder theorem](research_source_germ_truncation_and_turn_remainders.md)
already demonstrates for short filling operations.

For the present mixed path, the
[contracted finite-window reduction](research_mixed_contracted_finite_boundary_windows.md)
keeps precisely the missing calibrated endpoint and completion
information. Its boundary-function signs have not been replaced
by (9). Neither the phase-gauge obstruction nor the sharp norm
identity is a counterexample to the desired full source theorem;
they rule out those two proposed simplifications of an induction.
No analytic evaluation or finite-level experiment is used here.
