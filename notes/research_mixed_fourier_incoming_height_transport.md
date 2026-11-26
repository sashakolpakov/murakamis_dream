# Exact incoming height transport for the contracted Fourier cap

Research deduction, 7 November 2026. Raising an unselected negative
incoming height decreases every physical incoming Newton carrier.
This exact finite inequality transports the already paid, coherently
contracted high retained rows through the entire incoming height
reset. A real-direction monotonicity also covers the full right
taper, with the original plane kept at its plateau endpoint.

The low retained source is not estimated by subtracting this group
from a modulus bound. Selected positive heights and the remaining
joint compensated comparison stay separate.

## 1. A finite inequality retaining every carrier zero

Keep
\[
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 a=x+ih,\quad X=e^{-2\pi ia},\quad
 b_j(a)=X^{-j}(rX;r)_j
       =\prod_{k=1}^{j}(e^{2\pi ia}-r^k).
 \tag{1}
\]
For every \(0\le j<N\), every real \(x\), and
\(h_1\le h_2\le0\),
\[
 \boxed{\quad
 |b_j(x+ih_2)|
       \le e^{-\pi j(h_2-h_1)}|b_j(x+ih_1)|.
 \quad}
 \tag{2}
\]
Indeed, for \(|\zeta|=1\),
\[
 \frac{|R-\zeta|^2}{R}=R+R^{-1}-2\Re\zeta
 \tag{3}
\]
is increasing for \(R\ge1\). Apply this with
\(R_i=e^{-2\pi h_i}\), after rotating each factor in (1).
Since \(1\le R_2\le R_1\), each squared factor at \(h_2\)
is at most \(R_2/R_1\) times its squared factor at \(h_1\).
Multiplication proves (2). This proof divides by no source
factor and includes all zeros at height zero, as well as \(j=0\).

For \(j\ge\lceil N/2\rceil\), preserve the literal outgoing sum
\[
 H_{j,N}(y)=
       \sum_{l=0}^{N-j-1}\frac{P_{j+l}}{P_l}f_l(y),
 \qquad
 V_N^{\rm hi}(y,a)=
       \sum_{j=\lceil N/2\rceil}^{N-1}
                     \frac{b_j(a)}{P_j^3}H_{j,N}(y).
 \tag{4}
\]
Thus the entire outgoing cancellation within \(H_{j,N}\) is
retained. Formula (2) is not a comparison between moduli of the
complete sums at two heights.

## 2. The true allocated rate through a height reset

Fix the actual correlated reference of
[the high-tail payment theorem](research_mixed_fourier_right_cap_coherent_high_tail_payment.md),
with incoming flag \(\eta\in\{0,1\}\), output \(y=x_0\),
and incoming reference height
\[
             c=\Im a_*\le0,\qquad -.108\le c,\qquad
             P=[11/50,9/20].
 \tag{5}
\]
In particular (5) holds for every incoming type-four reference.
Write \(B_\eta(x)\) for its original action, marginal and quadratic
plane in that theorem, equation (15), with
\(\kappa_*=1/2500000\). The complete original
high-row rate is
\[
 \mathcal E_\eta(s;x+ih)
  =I_{x+ih}(s)-3J(s)-2\pi hs
       +\Re\Phi(s;y)-\frac{\eta}{2}\Re g(x+ih),
 \quad \frac12\le s\le1,
 \tag{6}
\]
where
\[
 I_a(s)=\int_0^s\log|1-e^{-2\pi ia}e^{-2\pi it}|\,dt.
 \tag{7}
\]
The outgoing Wall action \(\Phi(s;y)\) is independent of \(a\).
The logarithmic zeros of (7) remain integrable.

The same one-factor inequality (3), integrated in \(t\), gives
\[
 I_{x+ih}(s)-2\pi hs
 \le I_{x+ic}(s)-2\pi cs-\pi s(h-c)
                            \qquad(c\le h\le0).
 \tag{8}
\]
For \(0<x\le1/2\) and \(h\le0\), the original lower-half-plane
branch satisfies
\[
 g'(x+ih)=\Log(1-e^{2\pi h}e^{-2\pi ix}),\qquad
 0\le\Im g'(x+ih)\le\pi(1/2-x).
 \tag{9}
\]
The argument increases from zero to \(\pi(1/2-x)\) as its
radius increases from zero to one. Equivalently, this follows
by differentiating that argument with respect to the radius.
Consequently
\[
 -\frac{\eta}{2}\Re g(x+ih)
 \le-\frac{\eta}{2}\Re g(x+ic)
       +\frac{\eta\pi}{2}(1/2-x)(h-c).
 \tag{10}
\]
Equations (8)--(10) imply
\[
 \mathcal E_\eta(s;x+ih)
 \le\mathcal E_\eta(s;x+ic)
       -\pi\{s-\tfrac{\eta}{2}(1/2-x)\}(h-c).
 \tag{11}
\]
In particular the coefficient of \(h-c\) is at least
\(9\pi/25\) for \(x\in[.22,.5]\) and \(s\ge1/2\).

The true Fourier-polynomial upper rate on this whole compact
nonpositive-height strip is
\[
 \max\{-\Re g(x+ih),0\}=-\Re g(x+ih).
 \tag{12}
\]
Here \(\Re g(x+ih)\le0\) for \(0<x\le1/2,h\le0\), including
the tie at \(x=1/2\). The original zero-safe Fourier upper
bound, also used in Section 2 of
[the unselected taper theorem](research_mixed_unselected_right_taper_products.md),
therefore supplies (10) with any prescribed rate tolerance
for the actual incoming halfweight. It is not a relative
factorial formula at height zero. In particular no value
of \(d_N(e^{-2\pi i(x+ic)})\) is divided out.

The prior high-tail proof establishes the individual rate bound
\[
       \mathcal E_\eta(s;x+ic)
              <B_\eta(x)-1/35000
                  \quad(x\in P,\ 1/2\le s\le1).
 \tag{13}
\]
Combining (11) and (13), then using the original uniform Wall
packet and zero-safe incoming product upper bounds, proves:
for every \(\tau>0\),
\[
 \begin{split}
 &|d_N(e^{-2\pi i(x+ih)})|^{\eta/2}
           |V_N^{\rm hi}(x_0,x+ih)|\\
 &\quad\le C_\tau N^{A_\tau}
 \exp N\{B_\eta(x)-1/35000
                         -(9\pi/25)(h-c)+\tau\},
       \quad x\in P,\ c\le h\le0.
 \end{split}
 \tag{14}
\]
The degree-zero outgoing endpoint in (4) and its overlapping
exact endpoint estimate are the same ones used for (13).
All coefficients, the cardinal \(1/N\), both parity cuts and
the entire outgoing physical sum in each row are unchanged.
After one smaller tolerance the finite gap is \(1/70000\),
even when the incoming height has been fully reset to zero.

## 3. The high rows on the entire right taper

At a fixed \(h\le0\), differentiation of the incoming integral
with respect to \(x\) gives, almost everywhere,
\[
 \partial_x\mathcal E_\eta(s;x+ih)
 =\log\frac{|1-e^{2\pi h}e^{-2\pi i(x+s)}|}
                 {|1-e^{2\pi h}e^{-2\pi ix}|}
       -\frac{\eta}{2}\log|1-e^{2\pi h}e^{-2\pi ix}|.
 \tag{15}
\]
For \(1/4\le x\le1/2\) and \(1/2\le s\le1\),
\[
 x+s\in[1-x,1+x],\qquad
 \cos(2\pi(x+s))\ge\cos(2\pi x).
 \tag{16}
\]
The ratio in (15) is at most one. Also \(\cos(2\pi x)\le0\),
so its denominator exceeds one. Thus (15) is nonpositive.
At an incoming zero its logarithmic divergence is integrable;
the integral representation (7) proves the same monotonicity
by absolute continuity, including \(h=0\).

Set \(b=9/20\). Equations (11), (13) at \(b\), and (15) give
\[
 \mathcal E_\eta(s;x+ih)
 <B_\eta(b)-1/35000-(9\pi/25)(h-c),
 \quad b\le x\le1/2,\quad c\le h\le0.
 \tag{17}
\]
The finite-source bound (14) consequently also holds on this
entire rectangle with \(B_\eta(b)\) in place of \(B_\eta(x)\).
In particular it holds on the actual quadratic right taper
\[
                   h=400(.5-x)^2c.
 \tag{18}
\]
This is a quantitative bound for an actual complete outgoing
group on the full taper, not iteration of a small complex
neighborhood bound.

The comparison plane in (17) is deliberately retained at \(b\).
If \(P_\eta=\partial_a\Pi_\eta^{\rm F}(a_*;x_0)\) denotes the
original complex marginal, then the exact difference from the
full tangent at the new target is
\[
 \begin{split}
 B_\eta(b)
 &-\Re\{\Pi_\eta^{\rm F}(a_*;x_0)+P_\eta(x+ih-a_*)\}\\
 &=-\Re P_\eta(x-b)+\Im P_\eta(h-c)
                           -\kappa_*(b-\Re a_*)^2 .
 \end{split}
 \tag{19}
\]
These terms must be combined with the adjacent ordinary factor
and synthetic completion. They do not have an asserted sign
in isolation.

## 4. The nonpositive retained contours have the same height direction

There is a separate exact phase inequality useful for the low
retained source. Its entire incoming dependence is
\[
 \mathcal J_\eta(s,a)
       =g(s+a)-(1+\eta/2)g(a)+2\pi ias.
 \tag{20}
\]
For \(s=u+iv\), \(u\in[1/8,1/2]\), \(v\le0\), and
\(a=x+ih\), \(x\in[.45,.5]\), \(h\le0\), the original
arguments give
\[
 \Arg(1-e^{-2\pi i(s+a)})\ge\pi(1/2-u-x),\qquad
 0\le\Arg(1-e^{-2\pi ia})\le\pi(1/2-x).
 \tag{21}
\]
Indeed \(u+x\in[.575,1]\); its first argument runs between
\(\pi(1/2-u-x)\) and zero at radii at most one. Differentiating
(20) in \(h\) and using (21) yields
\[
 \partial_h\Re\mathcal J_\eta
 =-\Arg(1-e^{-2\pi i(s+a)})
       +(1+\eta/2)\Arg(1-e^{-2\pi ia})-2\pi u
 \le-\pi u+\frac{\eta\pi}{2}(1/2-x)
 \le-\frac{\pi}{10}.
 \tag{22}
\]
At \(u=x=1/2\), \(v=h=0\), use the continuous lower-half
limit of the integrated inequality rather than a nonexistent
logarithmic derivative at the factorial zero.
The other phase terms and the retained-index alias penalties
are independent of \(h\). Hence every explicit main, lower-alias,
and negative-join profile decreases by at least
\(\pi(h-c)/10\) under this incoming height raise, wherever its
original finite-source upper profile is being used.

Equation (22) supplies no estimate for positive retained heights,
and does not itself extend a calibrated real-direction supporting
plane past \(x=.45\). Equations (14)--(18) pay the high physical
group only; they are not a modulus-subtraction argument for the
low group. The joint compensation and the complete low retained
current remain the separate steps needed for a full terminal-taper
bound.
