# The true Fourier endpoint pays a complete coherent tail

Research deduction, 7 November 2026. The cardinal action at every
actual outgoing reference exceeds its value at the true physical
endpoint by a fixed positive amount. The completed inner last-row
estimate therefore pays the actual final retained row. The exact
Wall endpoint-tail theorem transfers that payment to a positive-width
strip of the original two-index source, with its outgoing cancellation
retained. All comparisons below are analytic; no function or saved
source certificate is evaluated.

## 1. A uniform cardinal-action surplus

Keep the original \(y=x_0\), \(Y=e^{2\pi iy}=\rho e^{i\phi}=p+iv\),
and the original lifted cardinal phase
\[
 \ell_q(y)=2\pi iy(q-\tfrac12)
 -\frac{\operatorname{Li}_2(Ye^{-2\pi iq})-\operatorname{Li}_2(Y)}
                 {2\pi i}.
 \tag{1}
\]
The inherited bounds used here are
\[
 \frac{121}{200}<\rho<\frac{123}{200}<\frac58,\qquad
 \frac25<\cos\phi<\frac{21}{50},\qquad
 \sin\phi>\frac9{10},\qquad \frac87<\phi<\frac76.
 \tag{2}
\]
They were proved in the
[allocation-curvature](research_mixed_fourier_allocation_curvature.md)
and [half-plane branch](research_mixed_fourier_endpoint_halfplane_branch.md)
notes. In particular \(p>6/25\), \(v>27/50\).
We will also use
\[
                         \log\rho>-\frac{51}{100}.
 \tag{3}
\]
Indeed the positive exponential series gives
\[
 e^{51/100}>
 1+\frac{51}{100}+\frac{(51/100)^2}{2}
       +\frac{(51/100)^3}{6}
 =\frac{3324317}{2000000}>\frac{200}{121};
 \tag{4}
\]
the last cross-product difference is
\(402242357-400000000>0\).

**Lemma 1.** If \(1/4\le x\le1/3\) and \(h\le0\), then
\[
            \Re\ell_{x+ih}(y)>\Re\ell_0(y)+\frac1{200}
                           =\pi\Im y+\frac1{200}.
 \tag{5}
\]

*Proof: reduction to two real endpoints.* Put
\(Z=Ye^{-2\pi i(x+ih)}\). Its argument is in \((-\pi,0)\),
and \(|Z|\le\rho<5/8\). The disk of radius \(5/8\)
centered at \(1\) lies strictly inside the sector
\(|\arg w|<\pi/4\), because \(5/8<1/\sqrt2\). Thus
\[
 0<\arg(1-Z)<\pi/4<\phi,\qquad
 \partial_h\Re\ell_{x+ih}(y)
                =-\Im\{\Log Y-\Log(1-Z)\}<0.
 \tag{6}
\]
Decreasing the height from zero increases the real action.
On the real interval \([1/4,1/3]\),
\[
              \frac{d^2}{dx^2}\Re\ell_x(y)
                   =\frac{2\pi\Im(Ye^{-2\pi ix})}
                          {|1-Ye^{-2\pi ix}|^2}<0.
 \tag{7}
\]
A concave function on an interval is at least the smaller of its
endpoint values. It remains to prove (5) at \(x=1/4,1/3\).

The absolutely convergent dilogarithm series gives, with
\(\theta=2\pi x\),
\[
 2\pi\{\Re\ell_x(y)-\Re\ell_0(y)\}
 =\theta\log\rho+
       \sum_{n=1}^{\infty}
       \frac{\Im\{Y^n(1-e^{-in\theta})\}}{n^2}.
 \tag{8}
\]
For either endpoint the remainder from index \(m\) is bounded by
\[
 \left|\sum_{n=m}^{\infty}
       \frac{\Im\{Y^n(1-e^{-in\theta})\}}{n^2}\right|
 \le \frac{2\rho^m}{m^2(1-\rho)}.
 \tag{9}
\]

At \(x=1/4\), the first two terms of (8) sum to
\[
 p+v+pv>\frac6{25}+\frac{27}{50}
                      +\frac6{25}\frac{27}{50}
          =\frac{1137}{1250}>\frac9{10}.
 \tag{10}
\]
The third term is
\((p+v)(4pv-p^2-v^2)/9>0\), since
\(4pv/(p^2+v^2)=4\cos\phi\sin\phi>36/25\).
The fourth term is zero. The remaining tail satisfies
\[
 \frac{2\rho^5}{25(1-\rho)}
              <\frac{125}{6144}<\frac1{49},
 \tag{11}
\]
where the final comparison is \(6125<6144\).
Using (3) and \(\pi<22/7\), equation (8) now gives
\[
 2\pi\{\Re\ell_{1/4}-\Re\ell_0\}
 >\frac9{10}-\frac1{49}-\frac{51\pi}{200}
 >\frac{383}{4900}>\frac{11}{350}.
 \tag{12}
\]

At \(x=1/3\), the first two terms sum to
\[
 \frac32v+\frac{\sqrt3}{2}p+\frac34pv
                               +\frac{\sqrt3}{8}(v^2-p^2).
 \tag{13}
\]
Since \(\sqrt3>17/10\) and
\[
 v^2-p^2=\rho^2(1-2\cos^2\phi)
                   >\frac9{25}\frac{809}{1250},
 \]
the expression (13) is greater than
\[
 \frac{81}{100}+\frac{51}{250}+\frac{243}{2500}
       +\frac{17}{80}\frac9{25}\frac{809}{1250}
 =\frac{29}{25}+\frac{1777}{2500000}>\frac{29}{25}.
 \tag{14}
\]
The third term is zero. The remaining tail is bounded by
\[
 \frac{2\rho^4}{16(1-\rho)}
                  <\frac{625}{12288}<\frac1{19},
 \tag{15}
\]
using \(11875<12288\). Therefore
\[
 2\pi\{\Re\ell_{1/3}-\Re\ell_0\}
 >\frac{29}{25}-\frac1{19}-\frac{17\pi}{50}
 >\frac{129}{3325}>\frac{11}{350}.
 \tag{16}
\]
The last comparison has cross-products \(45150>36575\).
Finally \(2\pi/200<11/350\). Equations (12), (16),
concavity and (6) prove (5). Every action and logarithm is the
original one; no numerical dilogarithm value was used. \(\square\)

## 2. Payment of the true final row

Use the actual references and incoming allocation of the
[completed bare inner-source theorem](research_mixed_fourier_right_cap_bare_inner_completion.md):
\[
 a_*\in K_{3+\eta},\quad \eta=0,1,\quad
 a=x+i\Im a_*,\quad x\in P=[11/50,9/20].
 \]
Its outgoing coordinate satisfies
\(1/4<\Re q_*<1/3\), \(\Im q_*<0\), by the
[real-strip theorem](research_mixed_fourier_endpoint_real_strip.md).
Write the original incoming supporting plane as
\[
 B_\eta(x)=M_\eta+p_\eta(x-\Re a_*)
                   -\kappa(x-\Re a_*)^2,\qquad
 \kappa=1/2500000.
 \tag{17}
\]
The completed last-row bound evaluated at \(z=\Re q_*\) gives
\[
 2\pi(-\Im a_*)_+-\frac{\eta}{2}\Re g(a)+\Re\ell_{q_*}(y)
                <B_\eta(x)-\frac{37}{70000}.
 \tag{18}
\]
The true physical endpoint has the different, explicit rate
\[
 E_{\rm end}(a;y)
   =2\pi(-\Im a_*)_++\pi\Im y-\frac{\eta}{2}\Re g(a).
 \tag{19}
\]
Lemma 1 and (18) prove
\[
 \boxed{\quad E_{\rm end}(a;y)
           <B_\eta(x)-\frac{387}{70000}.\quad}
 \tag{20}
\]
Here \(37/70000+1/200=387/70000\).
This uses the exact endpoint rate, not a vertical reset of a
physical row or division by a finite outgoing halfweight.

## 3. A paid positive-width part of the original physical wedge

The [exact Wall endpoint-tail theorem](research_mixed_fourier_right_cap_wall_endpoint_tail.md)
gives fixed \(\delta>0,N_0\), uniform over these incoming
targets and heights. Put \(D=N-1\), \(J_N=D-\lfloor\delta N\rfloor\),
\(X=e^{-2\pi ia}\), and retain its exact rows
\[
 c_N(y)=\frac{e^{-\pi iDy}(1-Y^N)}{N(1-Y)},\qquad
 T_{j,N}(a,y)=
       \frac{X^{-j}(rX;r)_j}{P_j^2}W_{N-j-1,N}(Y;Y).
 \tag{21}
\]
Then
\[
 \left|c_N(y)\sum_{j=J_N}^{D}T_{j,N}\right|
 \le 2|c_N(y)T_{D,N}|,\qquad
 c_NT_{D,N}=
 \frac{e^{-\pi i(N-1)y}(1-Y^N)X^{-(N-1)}(1-X^N)}
 {N^3(1-Y)(1-X)}.
 \tag{22}
\]
Every \(T_{j,N}\) contains its entire original outgoing sum.
The exact zero-safe proof of (22) retains \(1-X^N\), including
its zeros, and gives the unallocated rate
\(2\pi(-\Im a_*)_++\pi\Im y\) with prefactor \(CN^{-3}\).

Multiplication by the original admissible incoming halfweight
preserves (22). Its established finite rate is
\(-\eta\Re g(a)/2\), with its uniform polynomial prefactor
and prescribed tolerance. Combining (20)--(22), for every
\(\tau>0\) the complete strip obeys
\[
 |d_N(X)|^{\eta/2}
 \left|c_N(y)\sum_{j=J_N}^{D}T_{j,N}\right|
 \le C_\tau N^{A_\tau}
       \exp N\left\{B_\eta(x)-\frac{387}{70000}+\tau\right\}.
 \tag{23}
\]
In particular its finite exponential gap can be taken to be
\(1/200\) after absorbing the polynomial prefactor at sufficiently
large \(N\). The statement is uniform on the stated actual compact
families and holds for both parities.

This pays an actual positive-width endpoint strip after coherent
outgoing contraction, including its portion of the high-inner-index,
low-outgoing-index wedge. It does not pay the whole high-index
range, the middle part of that wedge, or the remaining real outgoing
faces and retained-index contour currents. No whole right-cap
asymptotic or noncancellation is asserted.
