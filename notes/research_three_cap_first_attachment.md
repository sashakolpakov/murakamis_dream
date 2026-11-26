# The first attachment of a complete cap to a retained vertex

Research calculation and local proof, 4 November 2026. Frozen manuscripts
are unchanged. The critical point below is certified for the actual cap
phase, rather than obtained by identifying its end with a homogeneous
Fourier variable. The Gaussian conclusion concerns a restricted wire
integral. It does not bound the rest of the wire period.

## 1. The exact two-variable system

Let
\[
 y=x_*={1\over6}+{i\log2\over2\pi},\qquad
 X=e^{2\pi ix},\quad Y=e^{2\pi iy}.
 \tag{1}
\]
Use the complete-cap packet and its selected angle \(t_c(x)\) from
[the complete-cap theorem](research_homogeneous_wire_complete_cap.md),
including its quantified directed domain. Its phase is
\[
 S(x)=b(x,t_c)+\psi(t_c,0)+{3it_c^2\over4\pi}-it_c,
 \quad
 f(t,x)=3t+2i\log(z+\sec(t/2))
        +i\log(q+z)-i\log(q-z)-2\pi=0,
 \tag{2}
\]
where \(z=\tan(t/2)\) and \(q=\cot\pi x\). All logarithms
are the continued branches specified by that theorem.

For the retained vertex use the exact selected branch from
[the central-index chart](research_three_vertex_central_index_chart.md):
\[
 \begin{split}
 \alpha&=X^{-1}-1,\qquad \beta=Y^{-1}-1,\qquad
 R=\sqrt{1-2(\alpha+\beta)+(\alpha-\beta)^2},\\
 U&={1+\alpha-\beta-R\over2},\qquad
 V={1-\alpha+\beta-R\over2},\\
 \Phi_x(x,y)&=-\Log U+\log(1-XU)-\log(1-X)-\pi i.
 \end{split}
 \tag{3}
\]
The square root continues from \(R=2+i\sqrt3\) at \(x=y=x_*\).
In the neighborhood used here its real part is positive; \(U,V\)
are in the lower-left quadrant. Thus (3) is the derivative of the
actual logarithmic critical value, not merely its exponential.

The stationary equations for the composed phase
\(\Theta(x;y)=S(x)+\Phi(x,y)\) are exactly
\[
 f(t,x)=0,\qquad
 b_x(x,t)+\Phi_x(x,y)=0,
 \quad
 b_x=\log\cos(\pi x+t/2)+\log\cos(\pi x-t/2)
                       -2\log\sin\pi x.
 \tag{4}
\]

**Proposition 1.** At \(y=x_*\), (4) has a simple zero in the
complex polydisk of radius \(10^{-8}\) about the following exact
rational centers, in the order \((x,t)\):
\[
 \begin{split}
 x_0&=.177337918569469382175948562048
                  +.101358689576302370861575311618i,\\
 t_0&=1.533800710765884206016520588964
                  -.978955098405739999074096803416i.
 \end{split}
 \tag{5}
\]
The zero is unique in this polydisk. Its wire coordinate is strictly
inside the directed cap domain
\[
 x={1\over6}+r+i\left({\log2\over2\pi}-{4r\over5}+s\right),
 \qquad 0<r<{13\over1000},\quad
             -{3\over2000}<s<{1\over1000}.
 \tag{6}
\]
Its cap angle belongs to the cap theorem's common rectangle. Its
retained index pair satisfies the central-index branch test and lies
strictly in that theorem's quantitative index chart.

*Proof.* The [outward checker](../experiments/check_three_cap_first_attachment.py)
uses the exact Jacobian of (4). For clarity, put
\(t_\pm=\tan(\pi x\pm t/2)\). The required cap derivatives are
\[
 \begin{split}
 f_t&=3+i\left(\sec(t/2)+{q\sec^2(t/2)\over(q-z)(q+z)}\right),\\
 f_x&={2\pi i z(1+q^2)\over(q-z)(q+z)},\\
 b_{xx}&=-\pi(t_++t_-+2q),\qquad
 b_{xt}={t_--t_+\over2},\qquad F_{tt}={if_t\over2\pi}.
 \end{split}
 \tag{7}
\]
The retained derivatives are elementary differentiations of (3):
\[
 \begin{split}
 \alpha_x&=-{2\pi i\over X},\qquad
 U_x={\alpha_x\over2}
           \left(1-{\alpha-\beta-1\over R}\right),\\
 \Phi_{xx}&=-{U_x\over U}
   -{2\pi i XU+XU_x\over1-XU}+{2\pi i X\over1-X}.
 \end{split}
 \tag{8}
\]
Hence the Jacobian in the order \((x,t)\) is
\[
 J=\begin{pmatrix}f_x&f_t\\ b_{xx}+\Phi_{xx}&b_{xt}\end{pmatrix}.
 \tag{9}
\]
The checker stores an exact rational complex matrix \(C\), approximating
the inverse at (5). On the whole polydisk it proves, in the maximum
complex-coordinate norm,
\[
 \|I-CJ\|_\infty<{1\over1000},\qquad
 |(Cf(x_0,t_0))_j|+
       10^{-8}\sum_k|(I-CJ)_{jk}|<10^{-8},
 \tag{10}
\]
where in the second formula \(f\) denotes the two-component system
(4). The map \((x,t)\mapsto(x,t)-C f(x,t)\) is a contraction
of the closed complex polydisk into itself. The first inequality also
makes \(C\) and \(J\) invertible. This proves existence, simplicity,
and uniqueness there.

The same calculation checks every logarithm denominator and branch:
\(q\pm z,\sec(t/2)+z,\cos(\pi x\pm t/2),\sin\pi x\)
have positive real parts; \(R\) has positive real part; \(U,V\)
have negative real and imaginary parts; and
\(|XU|,|YV|<1\). It checks (6), the common cap rectangle, and
\(1/4<\Re(i\Log U/(2\pi)),\Re(i\Log V/(2\pi))<49/100\),
with both index heights of absolute value below \(3/100\).
Thus the cap root is its already proved branch, and the retained
derivatives are the actual branch from the central-index lemma.
No root or branch is selected from a numerical residual alone.
\(\square\)

## 2. Effective derivatives and the restricted source integral

The outgoing derivative is \(\Theta_y=\Phi_y\). Eliminating first
the cap angle and then the attached wire gives
\[
 \begin{split}
 S_{xx}&=b_{xx}-{b_{xt}^2\over F_{tt}},\qquad
 \Theta_{xx}=S_{xx}+\Phi_{xx},\\
 x_c'(y)&=-{\Phi_{xy}\over\Theta_{xx}},\qquad
 \Theta_{\rm eff}''(y)=\Phi_{yy}
                            -{\Phi_{xy}^2\over\Theta_{xx}}.
 \end{split}
 \tag{11}
\]
The outward certificate proves at the point (5)
\[
 -\Re\Theta_{xx}>21,\qquad
 -\Re\Theta_{\rm eff}''>9,\qquad
 |\Theta_{{\rm eff},y}|<{2\over25},\qquad
 |x_c'(y)|<{21\over100}.
 \tag{12}
\]
For reference, the certified enclosures give the approximate values
\[
 \begin{split}
 \Theta_{xx}&\simeq-21.11412997+15.82722731i,\\
 \Theta_{{\rm eff},y}&\simeq .01127680830-.07457086638i,\\
 \Theta_{\rm eff}''&\simeq-9.80186322+8.19534083i.
 \end{split}
 \tag{13}
\]
These are quantitative statements about the first attachment. They do
not establish an invariant family under arbitrarily many attachments.
The same outward calculation evaluates the original continued phases
in (2)--(3), using their sine and denominator primitives, and proves
\(\Re\Theta(x_c;x_*)>19113/10000\). This is the actual critical
action, including both original additive constants.

The [directed retained-packet theorem](research_three_vertex_directed_packet.md),
Theorem 1, proves the exact retained source packet on a fixed
neighborhood of the same domain (6). Write the two original
packets, with their original level-dependent unit phases, as
\[
 W_N(x,0)=C_{N,3}N^{-1}A_c(x)e^{NS(x)}(1+O(N^{-1})),\qquad
 \widetilde V_N(x,y)=\kappa N^{-1/2}a(x,y)e^{N\Phi(x,y)}
                                        (1+O(N^{-1})).
 \tag{14}
\]
Both assertions in (14) are therefore proved on a fixed neighborhood
of the certified wire point. The retained theorem includes its actual
complementary index contour and aliases; this is the source input
beyond the central-index Hessian.

For sufficiently small fixed \(d>0\), define only the restricted
wire integral through the certified point:
\[
 B_N^{\rm loc}(y)=N\int_{x_c(y)+[-d,d]}
                      W_N(x,0)\widetilde V_N(x,y)\,dx.
 \tag{15}
\]
**Corollary 2.** At both parities and uniformly
for \(y\) in a fixed neighborhood of \(x_*\),
\[
 B_N^{\rm loc}(y)=C_{N,3}\kappa N^{-1}
 {\sqrt{2\pi}\,A_c(x_c(y))a(x_c(y),y)
       \over\sqrt{-\Theta_{xx}(x_c(y);y)}}
 e^{N\Theta(x_c(y);y)}(1+O(N^{-1})).
 \tag{16}
\]
The coefficient is holomorphic and nonzero. The Gaussian square root
is the branch with positive real part. Indeed (12) persists on a
smaller fixed neighborhood, gives strict real concavity along the
short horizontal interval, and supplies a strict endpoint gap.
Insert the actual holomorphic packets (14), and apply the one-variable
Gaussian expansion there. The powers are
\(N\cdot N^{-1}\cdot N^{-1/2}\cdot N^{-1/2}=N^{-1}\).
The first odd Gaussian correction integrates to zero, giving relative
\(O(N^{-1})\). Outside ordinary colors can be continued locally by
the same implicit-function and source-packet arguments, with their
fixed ordinary derivatives retained.

No assertion in (15)--(16) moves the full wire cycle into this short
interval or estimates its complement. That remains necessary for an
open-chain lower bound.

## 3. Reproduction

Run

    python3 experiments/check_three_cap_first_attachment.py

The [saved record](../repro/results/research-three-cap-first-attachment.json)
contains 44 outward comparisons at 192 bits, the exact rational
preconditioner, the contraction bounds, and source hashes. It checks
the analytic critical point and its local derivatives, not the
complementary original wire cycle.
