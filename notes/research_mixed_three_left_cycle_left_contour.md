# The transformed finite source and its paid left endpoint

Research deduction, 7 November 2026. The exact initialized finite
source has a holomorphic reciprocal-factorial interpolation on its
whole true summation interval. Its interior critical point is the
negative of the second-period critical index, with exactly the
original left action. Both horizontal residue corrections vanish
at infinite height. The complete weighted left endpoint current
and its joining segment are strictly below that action.

The remaining right endpoint current and the main portion past
\(\Re t=\Re y\) are retained. This is not a whole-source asymptotic.
No numerical evaluation is used.

## 1. Exact interpolation on the true finite interval

Use the notation of
[the initialized finite source](research_mixed_three_left_cycle_initialized_source.md).
Let \(a=b/N\) be physical, with
\[
       267/1000\le a\le433/1000,\qquad y=x_0,\qquad
       \xi=\Re y,\quad \upsilon=\Im y>0 .
 \tag{1}
\]
Small fixed output neighborhoods will be used only where the strict
inequalities below persist. Define
\[
\begin{split}
 \mathscr T_{N,b}(t;y)
   ={}&N\exp\{\pi iNa-\pi iN[(a-t)^2+t^2]-\pi ia\}\\
      &\hspace{12mm}\cdot E_N(a-t)E_N(t)^2E_N(y-t).
\end{split}
 \tag{2}
\]
Its exact values at \(t=k/N\), \(0\le k\le b\), are the terms in
equation (6) of that theorem. In particular
\[
                         J_N(b/N,y)=\sum_{k=0}^b
                                       \mathscr T_{N,b}(k/N;y).
 \tag{3}
\]
The sign \((-1)^b=e^{\pi iNa}\), the remaining factor \(e^{-\pi ia}\),
and every power of \(N\) in (2) are literal.

Put
\[
             \alpha_N=-1/(2N),\qquad \beta_{N,b}=a+1/(2N).
 \tag{4}
\]
On this whole real interval, each of \(a-t,t,y-t\) has real
part less than one. The global reciprocal-factorial theorem
therefore makes (2) holomorphic at all finite heights, including
across \(\Re(y-t)=0\). The reciprocal zeros are retained; no
regular-strip formula is extrapolated across that wall.

## 2. The regular critical chart and its exact action

For \(0<\Re t<\min(a,\xi)\), put
\[
 \mathcal F(t;a,y)
   =-g(a-t)-2g(t)-g(y-t)
                         +\pi i\{a-(a-t)^2-t^2\}.
 \tag{5}
\]
All primitives here are on their original strips.
On compact subcharts the exact factorial packet gives
\[
 \mathscr T_{N,b}
   =N^{-1}\mathcal B(t;a,y)e^{N\mathcal F(t;a,y)}
                                    (1+O(N^{-1})),
 \quad
 \mathcal B=
 \frac{e^{-\pi ia}}
 {\mathfrak a(a-t)\mathfrak a(t)^2\mathfrak a(y-t)}\ne0 .
 \tag{6}
\]
This expansion has the inherited fixed normalized derivatives.
It is a statement about the regular row, not the whole finite sum.

Let \(z_2\) be the proved second-period root, and let
\(\Psi_2(s;a,y)\), \(\Phi_1(a,y)\), and \(\Omega(a,y)\) be the
original actions of
[the calibrated observation](research_mixed_three_fourier_calibrated_homogeneous_observation.md).
Original factorial reflection gives, throughout the strip in (5),
\[
                 \mathcal F(t;a,y)=\Omega(a,y)-\Psi_2(-t;a,y).
 \tag{7}
\]
Indeed \(g(t)+g(1-t)=\pi it(1-t)\), with its original constant,
and substitution into (5) proves (7) directly.
Consequently
\[
 t_*=-z_2,\quad
 0<\Re t_*<\min(a,\xi),\quad h_*=\Im t_*>0,\quad
 \mathcal F_t(t_*)=0,\quad \mathcal F(t_*)=\Phi_1 .
 \tag{8}
\]
The logarithmic lift in (8) is zero by (7), not merely by
exponentiating the stationary equation. Also
\[
 \mathcal F_{tt}
   =-\pi\{\cot\pi(a-t)+2\cot\pi t+\cot\pi(y-t)\}.
 \tag{9}
\]
Every cotangent on the right has strictly positive real part on
the entire real strip of (5), at every height. Thus the real
phase on the line \(\Im t=h_*\) is strictly concave there and
has its unique maximum at \(t_*\).
The local lattice density \(N\) and the one-dimensional Gaussian
combine with the row power \(N^{-1}\) in (6) to give \(N^{-1/2}\).
No contributing-current conclusion follows from this local count.

## 3. Exact residue decomposition, including both true ends

Define on the half-grid line
\[
 w_{N,0}(v)=\frac1{1+e^{2\pi Nv}}-\mathbf1_{\{v<0\}} .
 \tag{10}
\]
The original factorial formulas show, for fixed \(N\), uniformly
in bounded real intervals,
\[
 \mathscr T_{N,b}(t)\sim
 \begin{cases}
 C_{+,N}\exp\{2\pi i[N(a-1)+1]t\},&\Im t\to+\infty,\\
 C_{-,N}\exp\{2\pi i[N(1-y)-1]t\},&\Im t\to-\infty.
 \end{cases}
 \tag{11}
\]
The constants are nonzero; their values are not replaced by one.
For the upper formula, only \(E_N(t)^2\) uses the upper quadratic
factorial exponent. At the lower end the upper exponents are
those of \(E_N(a-t)\) and \(E_N(y-t)\). In both cases their
quadratic terms cancel the quadratic chirp in (2).

The upper residue correction has decay rate \(2\pi(b+1)\),
and the lower one has decay rate \(2\pi(N\xi+1)\).
Both therefore vanish when the rectangle height tends to infinity.
Applying the original lattice residue formula on (4) gives exactly
\[
\begin{split}
 J_N(b/N,y)={}&N\int_{\alpha_N}^{\beta_{N,b}}
                              \mathscr T_{N,b}(t;y)\,dt\\
 &+iN\int_{\mathbb R}w_{N,0}(v)
 \{\mathscr T_{N,b}(\beta_{N,b}+iv;y)
                  -\mathscr T_{N,b}(\alpha_N+iv;y)\}\,dv .
\end{split}
 \tag{12}
\]
The two endpoint currents converge absolutely at fixed level.
This identity uses the actual finite interval \(0,\ldots,b\);
it does not extend the physical support to a full period.

Moving only the zero-mode segment to height \(h_*\) is legal
in the same holomorphic chart. It adds
\[
       iN\int_0^{h_*}
       \{\mathscr T_{N,b}(\alpha_N+iv;y)
                    -\mathscr T_{N,b}(\beta_{N,b}+iv;y)\}\,dv .
 \tag{13}
\]
Thus both true endpoint joins are still present, with their signs.

## 4. The complete weighted left current is paid

The exact midpoint identity is
\[
       |E_N(\alpha_N+iv)|^2=\frac{1+e^{2\pi Nv}}N .
 \tag{14}
\]
For physical real \(a\), substituting this into (2) gives
\[
\begin{split}
 &|w_{N,0}(v)\mathscr T_{N,b}(\alpha_N+iv;y)|\\
 &\quad=
 e^{-2\pi Nav-2\pi v+2\pi N\min(v,0)}
 |E_N(a+1/(2N)-iv)E_N(y+1/(2N)-iv)|.
\end{split}
 \tag{15}
\]
In particular the full kernel denominator has canceled exactly,
including at \(v=0\), rather than being discarded.

The corresponding original-strip rate is
\[
 \mathcal B_L(v)
  =-\Re g(a-iv)-\Re g(y-iv)-2\pi av+2\pi\min(v,0).
 \tag{16}
\]
Its value at zero is \(\Re\Omega(a,y)\).
For \(0<x<1/2\), the original strip argument satisfies
\[
                0<\Im g'(x+iH)<\pi(1-2x)
                                      \qquad(H\in\mathbb R).
 \tag{17}
\]
Therefore
\[
 \mathcal B_L'(v)<-2\pi a\quad(v>0),\qquad
 \mathcal B_L'(v)>2\pi\xi\quad(v<0),
 \tag{18}
\]
and hence
\[
 \mathcal B_L(v)\le\Re\Omega
                    -2\pi\min(a,\xi)|v|.
 \tag{19}
\]
These inequalities hold at all heights, with no saddle
relation imposed on the endpoint.

Here are the uniform finite-source consequences, including the
infinite tails. On every fixed \(|v|\le H\), use the two regular
offset packets in (15). Their product contributes \(N^{-1}\);
all remaining amplitudes are bounded there. Equations (18)--(19)
then give
\[
 N\int_{-H}^H
 |w_{N,0}(v)\mathscr T_{N,b}(\alpha_N+iv;y)|\,dv
                         \le \frac C N e^{N\Re\Omega}.
 \tag{20}
\]
For the infinite ends use the same exact cyclotomic remainders
as in the second-period packet. There are now only two varying
reciprocals. Their logarithmic errors, compared between height
\(H\) and a larger height, are bounded by \(4N\varepsilon_H\)
with \(\varepsilon_H\to0\). At the positive end the exact leading
modulus has slope \(-2\pi(Na+1)\); at the negative end, as
\(|v|\) increases, it has slope \(-2\pi(N\xi+1)\).
These exact slopes include both half-grid offsets in (15).
In particular the negative end decays at least as fast as
\(e^{-2\pi N\xi|v|}\).
Choose one fixed \(H\) so that
\(4\varepsilon_H<\pi\min(a,\xi)H\), uniformly on the compact
family (1). The strict rate loss (19) at \(H\), followed by
these exact slopes, gives the same bound (20) for both
infinite tails. Thus
\[
 \boxed{\quad
 N\int_{\mathbb R}
 |w_{N,0}(v)\mathscr T_{N,b}(\alpha_N+iv;y)|\,dv
                         \le \frac C N e^{N\Re\Omega(a,y)}.
 \quad}
 \tag{21}
\]
This is a uniform large-level bound; unlike the alias limits
in Section 3, it controls the whole infinite current.

The complete second-period packet and its proved exponential
flatness imply \(\Re\Psi_2\le-\gamma\) on each smaller fixed
compact neighborhood, for some \(\gamma>0\).
By the absolute calibration \(\Phi_1+\Psi_2=\Omega\),
the rate in (21) is at most \(\Re\Phi_1-\gamma\).
Thus the entire weighted left endpoint in (12) is
exponentially below the selected left action.

## 5. The unweighted left join and the retained remainder

For \(v\ge0\), the raw left endpoint rate is
\(\mathcal B_L(v)+2\pi v\). By (17),
\[
       \frac d{dv}\{\mathcal B_L(v)+2\pi v\}>2\pi\xi>0.
 \tag{22}
\]
It increases through the interval \(0\le v\le h_*\).
At its upper endpoint it equals the right boundary value
\(\Re\mathcal F(ih_*;a,y)\).
The strict horizontal concavity in (9) and the interior
maximum (8) give
\[
                     \Re\mathcal F(ih_*;a,y)<\Re\Phi_1(a,y).
 \tag{23}
\]
Compactness makes this gap uniform. The same midpoint identity,
the bounded-height offset estimates, and (22) control the
half-grid displacement without a singular endpoint quotient.
Consequently the left contribution to (13) also has a strict
uniform exponential gap below \(\Phi_1\).

What remains in (12)--(13) is the full main segment at height
\(h_*\) and the combined right weighted current/right join.
The main segment \(0<\Re t<\min(a,\xi)\) has the original
strict critical maximum; the part \(\Re t\ge\xi\) requires
the global reciprocal continuation in (2).
No estimate for that part, or for the right endpoint current,
is inferred here. In particular the complete finite sum (3)
has not been replaced by its local Gaussian.
