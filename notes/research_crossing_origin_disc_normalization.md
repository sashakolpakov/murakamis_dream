# Actual source normalization on a fixed small activity disc

Written research proof, 22 November 2026.

The zero-activity normalization extends to a fixed small activity
disc. The disc radius depends on the remaining parameter compact
set, and is independent of the level. The proof bounds the exact
source polynomial by a finite Fourier inverse and keeps the
canonical origin branch. No closing row or physical coordinate
is removed.

## 1. The original scalar and the assertion

Use the full centered Frobenius algebra of [O,J], with
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad
 p=e^{-2\pi i/N},\quad \eta=(-1)^d,\quad
 \kappa=q^{d^2/2},\qquad U_t=\sum_{a=0}^d t^af_a .
 \tag{1}
\]
The source is the original polynomial
\[
 \Phi_N(C,H,K)=\phi(f_0U_{-C}U_{-H}U_{-K}),\qquad
 H=e^{-2\pi ih},\quad K=e^{-2\pi ik}.
 \tag{2}
\]
Write
\[
 \begin{split}
 J(t)&=\int_0^t\log|2\sin\pi u|\,du,\\
 V(h,k)&=J(h+k)-2J(h)-2J(k),\\
 \Omega&=\{h,k>0:\ h+k<1,\ V(h,k)>0\}.
 \end{split}
 \tag{3}
\]
Let \(\Gamma_N(C,H,K)\) be the canonical Gamma section of [J].
Its continued value at activity zero is
\[
 \Gamma_{0,N}(h,k)=\frac{\kappa^2}{N^2}
 \frac{\mathfrak F_N(N(1-h)-1/2)^2
       \mathfrak F_N(N(1-k)-1/2)^2}
      {\mathfrak F_N(N(1-h-k))}.
 \tag{4}
\]
The factorial, phase and marks in this formula are fixed in [J].

**Theorem.** For every compact \(\mathcal K\subset\Omega\),
there are a fixed complex neighborhood \(\mathcal U\) of
\(\mathcal K\), a radius \(r>0\), and \(\delta>0\) such that
\[
 \boxed{\quad
 \frac{\Phi_N(C,e^{-2\pi ih},e^{-2\pi ik})}
      {\Gamma_N(C,e^{-2\pi ih},e^{-2\pi ik})}
       =1+O(e^{-\delta N})
 \quad}
 \tag{5}
\]
uniformly on \((h,k)\in\mathcal U\) and \(0<|C|\le r\) on
each fixed bounded-argument marked sector. At \(C=0\) the
ratio is defined by its continuous limit, and (5) holds there
as well. The constants may depend on the argument bound.
The source is nonzero on this domain for all sufficiently
large \(N\), including both parities and composite levels.

The comparison has its specified canonical branch. It need
not be holomorphic at the disc center: its first possible
nonanalytic term is \(C^N\Log C\). In particular (5) does not
identify an ordinary holomorphic Gamma germ to all orders.

## 2. Exact origin factors and coefficient packets

We record the identities from [J] that the estimates use.
Set \(Z=C^N\), \(x=H^N\), \(y=K^N\). Then
\[
 \begin{split}
 A_N(C)&=\exp\sum_{\substack{n\ge1\\N\nmid n}}
    \frac{2q^{-n}-H^n-K^n}{n(p^n-1)}C^n,\\
 M_N(Z)&=\frac{(1-xZ)(1-yZ)}{(1+Z)^2},\\
 \Gamma_N(C)&=\Gamma_{0,N}A_N(C)B_N(C),\\
 B_N(C)&=Z_N(C^N)
       \exp\left[-\frac{\Log M_N(C^N)\Log C}{2\pi i}\right].
 \end{split}
 \tag{6}
\]
Here \(A_N\) is a nonzero analytic unit on
\(|C|<\min(1,|H|^{-1},|K|^{-1})\), and
\[
 \begin{split}
 \log Z_N(Z)={}&\Log(1+Z)
 -\left(\tfrac12-h+\tfrac1{2N}\right)\Log(1-xZ)\\
 &-\left(\tfrac12-k+\tfrac1{2N}\right)\Log(1-yZ)
 +\frac{2\operatorname{Li}_2(-Z)
       -\operatorname{Li}_2(xZ)-\operatorname{Li}_2(yZ)}
       {2\pi iN}.
 \end{split}
 \tag{7}
\]
All logarithms except \(\Log C\) are power series at zero.
These identities retain the complete canonical normalization;
there is no unknown periodic factor.

Let \(\Pi_{<N}\) denote Taylor truncation to degrees below \(N\).
The exact source identity in [J] is
\[
 \Phi_N(C)=\Phi_{0,N}P_N(C)+j_{0,N}\mathcal Q_N(C),\qquad
 P_N=\Pi_{<N}A_N,\quad
 j_{0,N}=\frac{\eta}{N}(2+H^N+K^N),
 \tag{8}
\]
where \(\Phi_{0,N}=\Phi_N(0,H,K)\).
We next give an explicit form of the second packet and bound
it without dividing by any source value or forcing.

In \(\mathbb C[C]/(C^N)\), put
\[
 \begin{split}
 W_N(C)&=\Pi_{<N}
     \frac{C}{(1-HC)(1-KC)A_N(C)}
           =\sum_{n=1}^d w_n C^n,\\
 D_N(C)&=\sum_{n=1}^d\frac{w_n}{p^n-1}C^n,\qquad
 \mathcal Q_N=\Pi_{<N}(P_ND_N).
 \end{split}
 \tag{9}
\]
Indeed the exact source equation, modulo \(C^N\), reads
\[
 (1-C/q)^2\Phi_N(pC)-(1-HC)(1-KC)\Phi_N(C)=Cj_{0,N}.
 \tag{10}
\]
Equation (6) gives the same homogeneous equation for \(A_N\)
modulo \(C^N\), because \(M_N(C^N)^{-1/N}=1\) there.
Dividing by the unit \(A_N\) in this finite jet algebra reduces
(10) to
\[
 (\sigma-I)(\Phi_N/A_N)=j_{0,N}W_N,\qquad
 \sigma C=pC.
 \tag{11}
\]
On positive degrees below \(N\), \(\sigma-I\) is diagonal
with nonzero entries \(p^n-1\). Its zero-constant inverse is
exactly \(D_N\); the constant is \(\Phi_{0,N}\). This proves
(9), and no \(N\)-dimensional boundary space is replaced by
these two coefficient packets.

## 3. Hardy bounds for the exact source packet

Shrink a fixed complex neighborhood \(\mathcal U\) of
\(\mathcal K\) so that, for constants \(B,v>0\) and \(L\ge1\),
\[
 \begin{split}
 |\Gamma_{0,N}|&\ge N^{-B}e^{Nv},&
 |\Phi_{0,N}/\Gamma_{0,N}-1|&\le C e^{-\delta_0N},\\
 |H|,\ |K|&\le L,&
 \mu:=\log L&<v/4 .
 \end{split}
 \tag{12}
\]
The first two assertions are [O]'s canonical complex
asymptotic and source normalization. The remaining conditions
hold by shrinking the neighborhood of the real compact set.

Choose \(R>0\) with
\[
 R<\frac1{2L},\qquad
 a:=(1+L)R<\min(\log2/8,v/12),\qquad
 s=R/2,\quad r=R/4 .
 \tag{13}
\]
If \(N\nmid n\), then
\(|p^n-1|\ge2\sin(\pi/N)\ge4/N\).
Thus on the outer circle \(|C|\le R\),
\[
 |\log A_N(C)|
 \le\frac N2[-\log(1-R)-\log(1-LR)]
 \le Na,\qquad |A_N^{\pm1}|\le e^{Na}.
 \tag{14}
\]
Taylor coefficient bounds on that circle give on \(|C|\le s\)
\[
 |P_N-A_N|\le2e^{Na}2^{-N},\qquad
 |P_N|\le3e^{Na}.
 \tag{15}
\]

For a polynomial or analytic series \(F(C)=\sum F_nC^n\),
use the circle Hardy norm
\[
 \|F\|_s^2=\frac1{2\pi}\int_0^{2\pi}
                  |F(se^{i\theta})|^2\,d\theta
          =\sum_n|F_n|^2s^{2n}.
 \tag{16}
\]
Truncation is an orthogonal projection for this norm.
The analytic function truncated to form \(W_N\) has modulus
at most \(4R e^{Na}\) on the outer circle. Therefore
\[
 \|W_N\|_s\le4R e^{Na},\qquad
 \|D_N\|_s\le\frac N4\|W_N\|_s\le NR e^{Na},
 \qquad
 \|\mathcal Q_N\|_s\le3NR e^{2Na}.
 \tag{17}
\]
For the last inequality, multiplication by \(P_N\) has Hardy
operator norm at most \(\sup_{|C|=s}|P_N(C)|\), after which
truncation has norm one.
On the smaller disc \(|C|\le r=s/2\), Cauchy--Schwarz gives
\[
 |\mathcal Q_N(C)|
 \le(1-(r/s)^2)^{-1/2}\|\mathcal Q_N\|_s
 \le6NR e^{2Na}.
 \tag{18}
\]
These estimates are made in a Taylor coefficient norm on a
specified auxiliary circle. They are not a bound on the
condition number of multiplication by \(A_N\) in the
original boundary norm.

## 4. The source comparison and the central branch

Equations (14)--(15) give on the final disc
\[
 |P_N/A_N-1|\le2e^{-N(\log2-2a)} .
 \tag{19}
\]
In particular \(P_N/A_N\) is uniformly bounded for large \(N\).
Since \(|j_{0,N}|\le4L^N/N\), (12), (14), and (18) give
\[
 \left|\frac{j_{0,N}\mathcal Q_N}{\Gamma_{0,N}A_N}\right|
 \le24R N^B e^{-N(v-\mu-3a)}.
 \tag{20}
\]
The exponent is positive by (12)--(13). Combining (8),
(12), and (19)--(20) proves
\[
        \Phi_N(C)/(\Gamma_{0,N}A_N(C))
                         =1+O(e^{-\delta_1N})
                         \quad(|C|\le r)
 \tag{21}
\]
for some \(\delta_1>0\), uniformly on \(\mathcal U\).
Polynomial factors in \(N\) are absorbed by decreasing
\(\delta_1\).

Finally, \(|xC^N|,|yC^N|\le(L|C|)^N\).
The coefficients in (7) are bounded uniformly on
\(\mathcal U\), so its power series and those of \(M_N\) imply
\[
 |\log B_N(C)|
 \le C(L|C|)^N(1+|\Log C|)
 \le C_r(Lr)^N,\qquad 0<|C|\le r,
 \tag{22}
\]
on every fixed bounded-argument sector. The last step uses
\(\sup_{0<t\le r}t^N|\log t|\le C_r r^N\).
The apparent logarithm at the origin has thus been retained
and estimated, not removed by declaring a new analytic unit.
Equation (22), together with \(Lr<1\), proves that
\(B_N=1+O(e^{-\delta_2N})\) and that its continuous value
at zero is one. Using the exact factorization (6) in (21)
proves (5).

All fixed derivatives on smaller pole-free marked domains
away from \(C=0\) satisfy the corresponding exponential
bound by Cauchy's formula. The theorem makes no
all-orders holomorphic assertion at \(C=0\).

## Complete proof sources and scope

Both complete proof sources were read at renewed matching pins:

| Label | Complete source | SHA-256 |
|---|---|---|
| O | [Origin normalization, 385 lines](research_crossing_origin_fourier_normalization.md) | 6a516e08422f1645b6bea4281662b4c6db1465114de8eed610fb775607e6d3c8 |
| J | [Origin jets and cap connector, 388 lines](research_crossing_origin_jet_and_cap_adapter.md) | b804ff01db1fec35851fec8b0f875aef742a71d60cade31d61b4684899f1ad9a |

The source normalization is now controlled on a fixed small
activity disc, including its actual zero-activity value. The
inverse Fourier multiplier in (9) and its norm bound are
elementary finite-dimensional facts, proved here for this
specific source. No general novelty claim for that method is made.
The original phase, all \(N\) coefficients, and all Hermite
directions are retained. This does not give a source-relative
bound for an arbitrary closing row, a general internal
Conway gluing, or a filled-knot volume or finite-exception theorem.

Only written mathematics and text/hash inspection were used.
No mathematical program, experiment, test, build, git action,
or earlier-final file edit was performed.
