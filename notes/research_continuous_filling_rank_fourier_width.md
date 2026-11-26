# Differential order and Fourier width of the actual continuous filling

With the fixed Gaussian logarithm and original Frobenius closing,
even the constant-input scalar family cannot have exact differential
equations of bounded order and bounded Fourier width as the level
grows. The variable here is the continuous filling, not the main color.

## 1. The specified source

Let \(N\ge3\), \(D=N-1\), \(m=\lfloor N/2\rfloor\), and

\[
 \eta=(-1)^D,\qquad
 c_a=2\cos((2a+1)\pi/N),\qquad
 \tau_a=\pi(D-2a)/N.
 \tag{1}
\]

For \(0\le a<m\), the physical node \(c_a\) is double and

\[
 \gamma_a=\frac{D-2a}{4\sin((2a+1)\pi/N)}>0,\qquad
 \omega_a=\frac{\pi D^2}{4N}+\frac{N\tau_a^2}{4\pi}.
 \tag{2}
\]

At odd level \(N=2m+1\), there is also the simple node

\[
 c_m=-2,\qquad \tau_m=0,\qquad \omega_m=\frac{\pi D^2}{4N}.
\]

There is no normal datum at that node. The fixed full-Hermite
logarithm \(\mathscr G_N\) has values \(\omega_a\) and double-node
derivatives \(\gamma_a\). The original algebra and closing are
\(\mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2)\) and
\(\phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f\), where
\(P_N(z)=2T_N(z/2)+2\). Set

\[
 R_s=\exp(is\mathscr G_N),\qquad
 Z_N(s)=\phi_N(R_s),\qquad s\in\mathbb C.
 \tag{3}
\]

This is the actual constant spectator \(1\). At signed integer \(s\),
\(R_s=R^s\); noninteger \(s\) uses this specified logarithm. The exact
source formula [R, (18)--(19)] is

\[
 Z_N(s)=\sum_{a=0}^{m-1}e^{is\omega_a}(A_a+isB_a)
       +\mathbf1_{\text{odd }N}e^{is\omega_m},
 \quad
 A_a=-\eta c_a,\quad
 B_a=\eta(4-c_a^2)\gamma_a\ne0.
 \tag{4}
\]

Dephase only by its prescribed scalar and put

\[
 t=e^{\pi is/N},\qquad f(a)=a(a-D),\qquad
 \widehat Z_N(s)=e^{-is\omega_0}Z_N(s).
\]

Since \(\omega_a-\omega_0=\pi f(a)/N\),

\[
 \widehat Z_N(s)=\sum_{a=0}^{m-1}(A_a+isB_a)t^{f(a)}
       +\mathbf1_{\text{odd }N}t^{f(m)}.
 \tag{5}
\]

All operations below act on this entire scalar function. In
particular, no physical normal or original closing is omitted.

## 2. Isolated frequencies

Fix a nonnegative integer Fourier half-width \(B\), and write

\[
                        K=\max(m-B-1,0).
 \tag{6}
\]

For every \(a\in\{0,\ldots,K-1\}\), every \(|k|\le B\), and every
physical frequency index \(b\),

\[
       f(a)+k=f(b)+k',\quad |k'|\le B
              \quad\Longrightarrow\quad b=a,\ k'=k.
 \tag{7}
\]

Indeed, the frequencies are strictly decreasing, with consecutive
gaps

\[
                     f(a)-f(a+1)=N-2a-2.
 \tag{8}
\]

For \(a\le m-B-2\), its forward gap is at least \(2B+2\),
and its backward gap, when present, is larger. All other distances
are still larger. The same argument includes the odd simple
frequency \(f(m)\). Since \(|k'-k|\le2B\), (7) follows.

We will also use exponential independence over \(\mathbb C(s)\):
if the \(\mu_j\) are distinct and
\(\sum_j r_j(s)e^{\mu_js}=0\) with rational \(r_j\), then every
\(r_j=0\). To prove it, clear the rational denominators and choose
a ray \(s=e^{i\theta}x\) on which the numbers
\(\Re(e^{i\theta}\mu_j)\) are distinct. The term with largest
exponential growth cannot be canceled by the others: its nonzero
polynomial coefficient cannot decay exponentially along that ray.
Remove it and repeat. The identity theorem permits this argument
even when the given identity was initially stated on an open set.

## 3. Constant-coefficient differential blocks

**Theorem 1.** Suppose the nonzero differential operator

\[
 \mathcal L_N=\sum_{|k|\le B}t^kP_{k,N}(\partial_s),\qquad
                  P_{k,N}\in\mathbb C[\xi],
 \tag{9}
\]

annihilates \(\widehat Z_N\). Coefficients may depend arbitrarily
on \(N\). If \(r=\max_k\deg P_{k,N}\), then

\[
                         r\ge2K.
 \tag{10}
\]

Here and below the normal ordering in the displayed operator is
part of its definition: multiplication by \(t^k\) is on the left.

*Proof.* Put \(\mu_a=i\pi f(a)/N\). For a polynomial \(P\),

\[
 P(\partial_s)\{(A_a+isB_a)e^{\mu_as}\}
 =e^{\mu_as}\bigl[(A_a+isB_a)P(\mu_a)+iB_aP'(\mu_a)\bigr].
 \tag{11}
\]

For \(a<K\), (7) isolates this contribution at the frequency
\(f(a)+k\) in \(\mathcal L_N\widehat Z_N\). Exponential
independence makes its coefficient zero. Its linear and constant
terms in \(s\), together with \(B_a\ne0\), give

\[
                    P_{k,N}(\mu_a)=P'_{k,N}(\mu_a)=0.
 \tag{12}
\]

Thus every nonzero \(P_{k,N}\) has the \(K\) distinct double roots
\(\mu_0,\ldots,\mu_{K-1}\). Its degree is at least \(2K\).
This proves (10), including the vacuous case \(K=0\). \(\square\)

For width zero, (4) gives the sharper exact order \(N\): all
double frequencies occur with nonzero linear coefficient, and
the odd simple frequency occurs with coefficient \(1\).
The new estimate (10) allows different frequencies to be coupled
by the Fourier coefficients in (9).

## 4. Rational dependence on the filling variable

**Theorem 2.** Suppose a nonzero operator

\[
 \mathcal L_N=\sum_{|k|\le B}t^kP_{k,N}(s,\partial_s),\qquad
 P_{k,N}(s,\partial_s)=\sum_{j=0}^{r}p_{k,j,N}(s)\partial_s^j,
 \quad p_{k,j,N}\in\mathbb C(s),
 \tag{13}
\]

annihilates \(\widehat Z_N\) meromorphically. Then

\[
                              r\ge K.
 \tag{14}
\]

*Proof.* After applying (13) to (5), every frequency coefficient
is rational in \(s\). Equations (7) and exponential independence
therefore imply, for every \(a<K\),

\[
        P_{k,N}(s,\partial_s)
                      \{(A_a+isB_a)e^{\mu_as}\}=0.
 \tag{15}
\]

Choose any nonzero \(P_{k,N}\), of order \(r_k\le r\), and a point
where its coefficients have no pole and its leading coefficient
does not vanish. An order-\(r_k\) ordinary differential equation
there has at most \(r_k\) independent analytic solution germs.
Indeed, derivatives of orders \(0,\ldots,r_k-1\) at that point
determine every later Taylor coefficient recursively; a solution
with all those initial data zero has zero Taylor series. The map
to those data is injective. Order zero has only the zero solution.

The \(K\) functions in (15) are linearly independent: exponential
independence applied to a constant linear relation proves this,
since \(A_a+isB_a\) is not the zero polynomial. Their germs are
independent as well, by analytic continuation. Hence
\(K\le r_k\le r\). \(\square\)

This includes coefficients rational jointly in \(s,t\) whenever
left multiplication by a common denominator puts the operator in
(13). The width is measured after that chosen clearing; no
intrinsic width of a rational presentation is asserted. A nonzero
polynomial denominator in \(s,t\) is not identically zero after
\(t=e^{\pi is/N}\), by the same exponential-independence argument.
Clearing it changes neither the differential order nor the
meromorphic annihilation identity. Arbitrary meromorphic
coefficients in \(s\), which could themselves hide exponential
frequencies, are not covered.

## 5. Source scope

Conjugation by \(e^{is\omega_0}\) replaces \(\partial_s\) by
\(\partial_s+i\omega_0\), preserving order and Fourier width.
Both theorems therefore hold for the original scalar \(Z_N\) too.
Their bounds imply respectively

\[
                    r+2B\ge2m-2,\qquad r+B\ge m-1.
 \tag{16}
\]

Thus fixed order and fixed cleared Fourier width cannot coexist
for exact continuous-filling equations of this actual constant
source as \(N\to\infty\). This is a scalar differential-order
statement, not a general matrix-rank theorem.

The argument imposes no restriction on a main-color quantum
difference equation, an equation whose cleared width grows with
\(N\), or an asymptotic quotient isolating a geometric mode with
a proved remainder. It supplies neither a scalar lower bound nor
an identification of the original relative cycle with such a mode.
The finite family and its fixed logarithm are those in [R]; changing
the logarithm independently at the physical nodes changes the
problem.

## Direct source

**[R]** [A full-Hermite real-power interpolation of the original crossing](research_real_power_source_transport.md),
§§1--3, especially (2)--(8) and (18)--(21).
SHA-256: `7dac43d1a5fac6b4602a3aab12bfe977cb42a61b36d40a2fb8517e29566df8ea`.
