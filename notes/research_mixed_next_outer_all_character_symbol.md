# Uniform positivity of the outer symbol at every unit character

Private exact-source proof, 8 November 2026. The leading symbol of the
original seven-term equation is strictly positive at every unit
character. This includes the actual weighted adjoint after conjugation
by either character in any Chebyshev mode of degree at most \(N/3\).
On each fixed interior color interval, the resulting finite operators
have a common analytic coefficient chart and a uniform small-shift
estimate.

These are leading-symbol and coefficient conclusions. They do not
estimate an inverse, the finite endpoint currents, or the complete
outer observation. No mathematical numerical evaluation is used.

## 1. Original operator and the unit-character theorem

Use the full Hermite source and ordered operator in
[the seven-term recurrence](research_mixed_next_physical_inner_seven_term_recurrence.md),
equations (5), (12), and (20). In particular
\[
 \mathcal D_{3,N}
 =q^{-2}(\mathcal L^2-I)\mathcal L_1
       +q^{-3}\mathcal L Z-8q^{-2}\mathcal L
                              +(8q^{-1}+2)I,
 \qquad q=e^{\pi i/N}.
 \tag{1}
\]
For real \(0<u<\pi\), put
\[
 x=\cos u,\qquad a=\cot^2(u/2)=\frac{1+x}{1-x}.
 \tag{2}
\]
The actual leading symbols, with an index shift represented by
\(\zeta\), are
\[
\begin{split}
 \ell(u,\zeta)&=2+2a-a(\zeta+\zeta^{-1}),\\
 m(u,\zeta)&=2+2a-a(e^{-iu}\zeta+e^{iu}\zeta^{-1}),\\
 d(u,\zeta)&=(\ell^2-1)m-(8+2x)\ell+10 .
\end{split}
 \tag{3}
\]
The phases of \(m\) follow from
\(q^{2j+2}\longrightarrow-e^{-iu}\) and
\(q^{-2j}\longrightarrow-e^{iu}\) on
\(u=\pi-(2j+1)\pi/N\). The multiplication symbol of \(Z\) is
\(-2x\). Thus (3) is the leading symbol of the ordered source
(1), with its original constants.

**Theorem 1.** For every \(0<u<\pi\) and every \(|\zeta|=1\),
\[
                         d(u,\zeta)\ge4 .
 \tag{4}
\]
In particular this symbol is real and positive on the full real
character circle.

*Proof.* Write \(\zeta=e^{i\vartheta}\) and set
\[
 P=\ell-2=2a(1-\cos\vartheta),\qquad
 Q=m-2=2a(1-\cos(\vartheta-u)),\qquad
 K=(P+1)(P+3).
 \tag{5}
\]
Then \(0\le P\le4a\), \(Q\ge0\), and
\[
                   d=KQ+2P^2-2xP-4x.
 \tag{6}
\]
The two nonnegative increments in (5) are correlated. The
angle-addition identity and
\(\sin^2\vartheta=1-(1-P/(2a))^2\) give
\[
\begin{split}
 Q&\ge 2(1+x)+xP-\mathcal R,\\
 \mathcal R^2
   &=P\{(4-P)+8x+(4+P)x^2\}\ge0,\qquad \mathcal R\ge0.
\end{split}
 \tag{7}
\]
This inequality retains either sign of \(\sin\vartheta\).

Define the following polynomials in \(P\):
\[
\begin{split}
 A'&=4P^2+8P+2,\\
 B&=P^3+6P^2+9P+2,\\
 V&=P(P+1)^2-2.
\end{split}
 \tag{8}
\]
Equations (6)--(7) yield
\[
             d-4\ge A'+Bx-K\mathcal R.
 \tag{9}
\]
The exact difference of squares is itself a square:
\[
          (A'+Bx)^2-K^2\mathcal R^2=(2x-V)^2 .
 \tag{10}
\]
For clarity, its three coefficients in \(x\) are
\[
\begin{split}
 (A')^2-K^2P(4-P)&=V^2,\\
 2A'B-8PK^2&=-4V,\\
 B^2-K^2P(P+4)&=4.
\end{split}
 \tag{11}
\]
The last identity also follows from
\((P+2)^2=K+1\) and \(B=(P+2)(K-2)\).

The sign of the unsquared expression is fixed by the admissible
range \(P\le4a\), which is equivalent to
\[
                      x\ge\frac{P-4}{P+4}.
 \tag{12}
\]
Since \(B>0\), for \(P>0\) this gives
\[
 A'+Bx\ge
 \frac{(P+4)A'+(P-4)B}{P+4}
             =\frac{P^2(P+3)^2}{P+4}>0.
 \tag{13}
\]
For \(P=0\), the same expression is \(2(1+x)>0\).
Thus (10) implies \(A'+Bx\ge K\mathcal R\), and (9)
proves (4). In fact the proof retains the explicit bound
\[
 d-4\ge
 \frac{(2x-V)^2}{A'+Bx+K\mathcal R}\ge0 .
 \tag{14}
\]
\(\square\)

## 2. The actual adjoint and Fourier carriers

Let \(U=\lfloor N/2\rfloor-1\), \(\epsilon=N^{-1}\), and
retain the exact outer weights
\[
 \mu_{j,N}=(-1)^U\kappa_N^3\omega_N(u_{j,N})q^{3j(j+1)},
 \qquad u_{j,N}=\pi-(2j+1)\pi\epsilon,
 \tag{19}
\]
where
\[
 \omega_N(u)=
 \begin{cases}
 \sin u,&N\ \text{even},\\
 \sin u\sin(u/2)/\cos^2(\pi\epsilon/2),&N\ \text{odd}.
 \end{cases}
 \tag{20}
\]
The exact angular adjoint of the recurrence is
\[
 (\mathcal A_{\epsilon,p}v)(u)
    =\sum_{r=-3}^{3}b_{r,p}(u,\epsilon)
                                v(u+2\pi r\epsilon),
 \tag{21}
\]
with \(p\) specifying the parity formula in (20). These are the
actual coefficient functions of
[the constant-mode source theorem, Section 3](research_mixed_next_outer_constant_mode_symbol.md).
In particular they include the exact ratio
\[
 \frac{\mu_{j-r,N}}{\mu_{j,N}}
 =(-1)^r e^{3iru+3\pi i\epsilon r^2}
                      \frac{\omega_N(u+2\pi r\epsilon)}{\omega_N(u)}.
 \tag{22}
\]
Thus its constant-character leading multiplier is
\(\zeta=-e^{3iu}\), including the original physical half-step.

For any real frequency \(b\), put \(\nu=b/N\). Exact conjugation
by its character gives
\[
\begin{split}
 (\mathcal A_{\epsilon,p,\nu}v)(u)
  &:=e^{-ibu}\mathcal A_{\epsilon,p}(e^{ibu}v)(u)\\
  &=\sum_{r=-3}^{3}b_{r,p}(u,\epsilon)e^{2\pi ir\nu}
                                  v(u+2\pi r\epsilon).
\end{split}
 \tag{23}
\]
The right side defines this family independently for real
\(\nu\); no singular expression \(b=\nu/\epsilon\) is needed
to continue its coefficients. Its leading multiplication is
\[
 d_\nu(u):=
 d\bigl(u,-e^{i(3u+2\pi\nu)}\bigr)\ge4
 \qquad(0<u<\pi,\ \nu\in\mathbb R).
 \tag{24}
\]
Indeed each term of index shift \(r\) in (22) acquires exactly
the extra factor \(e^{2\pi ir\nu}\).

This is the relevant carrier convention for the original
Chebyshev insertion: since \(c_j=-2\cos u_{j,N}\),
\[
 T_b(c_j/2)=(-1)^b\cos(bu_{j,N})
          =\frac{(-1)^b}{2}
             \left(e^{ibu_{j,N}}+e^{-ibu_{j,N}}\right)
 \tag{25}
\]
for nonnegative integer \(b\). Both signs of \(\nu=b/N\)
are therefore included. In particular (24) covers every actual
mode of the outgoing polynomial of degree less than \(N/3\).
No estimate for its coefficients is required for this symbol
statement.

## 3. Uniform analytic coefficients for the actual mode range

**Corollary 2.** Fix a compact interval \(J\Subset(0,\pi)\).
There are a fixed \(R>0\), an \(\epsilon_0>0\), and a constant
\(C_J\), common to both parities and every real
\(|\nu|\le1/3\), such that the coefficients of (23) are
holomorphic for \(u\in J_R\), \(|\epsilon|<\epsilon_0\), and
\[
 |d_\nu(u)|\ge2\quad(u\in J_R).
 \tag{26}
\]
After a fixed shrink of this chart, they satisfy
\[
 \|(\mathcal A_{\epsilon,p,\nu}-d_\nu)v\|_{J_s}
       \le C_J\frac{|\epsilon|}{\delta}
                              \|v\|_{J_{s+\delta}}
 \tag{27}
\]
whenever \(0<s<s+\delta<R\), \(0<\delta\le1\), and
\(12\pi|\epsilon|\le\delta\).
Here \(J_s\) denotes the complex distance neighborhood of \(J\).

*Proof.* The original coefficients in (21) are finite sums and
products of the regular angular coefficients
\[
 A_\epsilon(u)=
 \frac{4\cos^4((u-\pi\epsilon)/2)}
                 {\sin u\sin(u-\pi\epsilon)},\qquad
 C_\epsilon(u)=A_\epsilon(-u),
 \tag{28}
\]
their fixed \(O(\epsilon)\) translates, and the exact ratios
(22). All denominators remain nonzero on a fixed interior
chart. Formula (23) merely multiplies each of these seven
coefficients by \(e^{2\pi ir\nu}\), of modulus one for real
\(\nu\). Their analytic bounds and their \(O(\epsilon)\)
differences from the values at \(\epsilon=0\) are therefore
uniform in the stated parameter range.

The leading sum is (24). Its continuous dependence on the
compact real set \(J\times[-1/3,1/3]\), together with (4),
allows one common complex neighborhood where (26) holds.
Shrink the neighborhood once more to obtain uniform
coefficient bounds on its closure.

Subtract the leading coefficient sum in (23). The coefficient
differences cost \(C|\epsilon|\|v\|\). Each remaining
translation has length at most \(6\pi|\epsilon|\le\delta/2\).
Integrating \(v'\) on that segment and applying Cauchy's
estimate on the remaining \(\delta/2\) margin costs
\(C|\epsilon|\delta^{-1}\|v\|\). Summing the seven terms and
using \(\delta\le1\) proves (27). \(\square\)

In this estimate the rapid character is part of the exact
conjugated operator. One need not bound \(e^{ibu}\) as an
analytic amplitude by \(e^{|b||\operatorname{Im}u|}\).
Converting a probe for (23) back to the original observation
still requires its character and the exact finite boundary
terms. The coefficient conclusion alone does not perform
that conversion or estimate those terms.

For completeness the same symbol result is independent of the
fixed outer twist power. If the inner operator (1) is retained
but the observation uses \(\beta_{j,N}R(c_j)^n\), with a fixed
signed integer \(n\), its exact weight ratio is
\[
 (-1)^r e^{inru+\pi in\epsilon r^2}
                 \frac{\omega_N(u+2\pi r\epsilon)}{\omega_N(u)}.
 \tag{29}
\]
This follows from
\(\beta_{j,N}=(-1)^{U+j}\omega_N(u_{j,N})\) and
\(R(c_j)=\kappa_N(-1)^jq^{j(j+1)}\).
The leading character with frequency \(\nu\) is now
\(-e^{i(nu+2\pi\nu)}\), still on the unit circle for real
parameters. Theorem 1 and the same fixed-interior argument
apply, with constants allowed to depend on \(n\). This
corollary changes only the observation of the fixed inner
source; it asserts no general filling theorem.

## 4. Scope

The exact full-source recurrence, its even forcing
\(4\kappa_N^3/N^2\), its zero odd forcing, and all the finite
adjoint boundary terms remain those of the seven-term theorem.
Their normalization and coalescing endpoint data have not
been replaced by the principal symbol.

Equations (24)--(27) supply uniform interior coefficient
hypotheses for character-dependent analytic probe
constructions, including the actual high-degree Chebyshev
carriers. They do not extend an interior chart uniformly to
the physical endpoints. They do not supply a global inverse,
pay a boundary current, or compare an eventual exponential
residual rate with the required outer budget
\(B_f=77/50+\pi/50\).

### Source hashes

- Exact seven-term source and adjoint:
  49cd08c5759bd6669d3cbf1a7e661d60188639c9added0c973659c4723d0a21a.
- Actual constant-mode coefficients and phase convention:
  ef07c25bb23cf52763d8ef19d145be14b4abd69445df321b6cdb6d78697ee7cc.
- Original Casimir observation:
  see [its exact weights and insertion](research_mixed_next_three_outer_casimir_observation.md).
