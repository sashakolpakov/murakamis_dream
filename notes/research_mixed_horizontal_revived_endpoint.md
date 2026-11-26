# Horizontal optimization of the revived conditional endpoint

Research deduction, 5 November 2026. The complete revived-endpoint
rate separates into two scalar functions after subtracting the original
outer supporting plane. Their maxima are explicit. There is also a
uniform favorable-direction subset on which the inherited endpoint gap
is preserved, including the small quadratic loss of the fixed zero-mode
bound. No unrestricted endpoint allowance or complete real-tail bound
is inferred.

## 1. Exact allocation and reference data

Use the actual original reference, types and normalization from the
[real-cut reduction](research_mixed_horizontal_real_cut_optimization.md):
\(a_0=x_0+ih_a\), \(b_0=z_0+ih_b\), original conditional
index \(s_0\), and
\[
 \begin{split}
 F(s;a,b)&=g(s+a)+g(s+b)-(2+\epsilon)g(s)
 -(1+\eta/2)g(a)-(1+\epsilon/2)g(b)+2\pi ias,\\
 M&=\Re F(s_0;a_0,b_0),\qquad
 p_a=\Re F_a(s_0;a_0,b_0),\quad
 p_b=\Re F_b(s_0;a_0,b_0),\\
 I&=[11/50,9/20],\qquad
 G_h(x)=\Re g(x+ih).
 \end{split}
 \tag{1}
\]
Here \(\eta,\epsilon\in\{0,1\}\), all reference and target
real coordinates belong to \(I\), and the fixed heights satisfy
\(|h_a|,|h_b|\le3/25\). Retain the actual unselected
negative reference heights at type-four coordinates. The primitive,
its original branches and its additive constant are unchanged.

The exact allocated endpoint rate of the whole real-row envelope is
\[
 \begin{split}
 L(h_a,h_b)&=2\pi(-h_a)_++2\pi(h_b)_+,\\
 E_1(x,z)&=L(h_a,h_b)
                    -\frac\eta2G_{h_a}(x)-\frac\epsilon2G_{h_b}(z).
 \end{split}
 \tag{2}
\]
This is the \(u=1\) endpoint of the full entropy rate in the
[asymmetric-contour theorem](research_mixed_horizontal_asymmetric_contour.md).
The first line is the maximum of the four literal revived-row carrier
branches \(2\pi(-v h_a+w h_b)\), \(v,w\in\{0,1\}\).
All four remain; their maximum is constant during horizontal motion.
Both allocated Fourier halfweights in the second line remain as well.

Put
\[
 \delta_1=M-E_1(x_0,z_0).
 \tag{3}
\]
When the reference lies in one of the completed original conditional
source images, its saved last-row comparison gives
\(\delta_1>1/1000\). This is a reference inequality. It is
not an assertion about every independently chosen plateau target.

## 2. Factorial energy and the precise boundary force

For one coordinate let \(\tau\in\{0,1\}\) be its type flag,
let \(p\) be its original real marginal, and write
\[
 \begin{split}
 B_h(x,x_0)&=G_h(x)-G_h(x_0)-G_h'(x_0)(x-x_0),\\
 q&=p+\frac\tau2G_h'(x_0),\qquad d=x-x_0,\\
 A_\tau(x)&=-\frac\tau2\{G_h(x)-G_h(x_0)\}-pd
           =-qd-\frac\tau2 B_h(x,x_0).
 \end{split}
 \tag{4}
\]
On the full plateau and height rectangle,
\[
 G_h''(x)=\pi\Re\cot\pi(x+ih)>\frac{9\pi}{70},
 \qquad B_h(x,x_0)\ge\frac{9\pi}{140}d^2.
 \tag{5}
\]
The cotangent bound is proved in the
[fixed zero-mode theorem](research_mixed_horizontal_zero_mode_support.md).
Thus a type-four coordinate contributes a strictly concave scalar
gain; a type-three coordinate contributes only the linear gain
\(-pd\).

The two forces in (4) have an exact source interpretation. Substituting
the original derivatives in (1) cancels precisely the Fourier
halfweight derivative:
\[
 \begin{split}
 q_a&=\Re\{g'(s_0+a_0)-g'(a_0)\}-2\pi\Im s_0,\\
 q_b&=\Re\{g'(s_0+b_0)-g'(b_0)\}.
 \end{split}
 \tag{6}
\]
These are the original bare conditional marginals. The asymmetric
first chirp is essential. The cancellation in (6) identifies the
force; it does not delete either halfweight from the value (2).

**Favorable-direction endpoint bound.** If
\[
              q_a(x-x_0)\ge0,\qquad q_b(z-z_0)\ge0,
 \tag{7}
\]
then (4) gives
\[
 \begin{split}
 E_1(x,z)-M-p_a(x-x_0)-p_b(z-z_0)
 \le-\delta_1-\frac{9\pi}{280}
       \{\eta(x-x_0)^2+\epsilon(z-z_0)^2\}.
 \end{split}
 \tag{8}
\]
For type three, \(q=p\), so (7) is exactly the favorable
linear direction. For type four it uses the force after retaining the
factorial energy. The statement is uniform over every reference for
which (3) is known, without releasing any coupled geometric datum.

The fixed zero-mode plane includes the additional loss
\(\{(x-x_0)^2+(z-z_0)^2\}/2500000\). On \(I^2\)
this loss is at most
\[
 \frac{2(23/100)^2}{2500000}
       =\frac{529}{12500000000}<\frac1{20000000}.
 \tag{9}
\]
Consequently, if \(\delta_1>1/1000\), (7) implies that the
revived-endpoint rate is below that full affine-quadratic bound by
more than \(1/2000\). This controls only this endpoint component;
the remaining real rows are not charged to its reserve.

## 3. The unrestricted maximum is explicit

Let \(A_\tau^*=\max_{x\in I}A_\tau(x)\). If \(\tau=0\),
the maximum is at the left endpoint when \(p>0\), at the right
endpoint when \(p<0\), and is zero everywhere when \(p=0\).

If \(\tau=1\), put
\[
 R=e^{2\pi h},\qquad T=e^{-4p},\qquad
 D_h(x)=1+R^2-2R\cos(2\pi x).
 \tag{10}
\]
Since \(G_h'(x)=\tfrac12\log D_h(x)\), the unique
maximizer is
\[
 x_*=
 \begin{cases}
 11/50,&T\le D_h(11/50),\\
 9/20,&T\ge D_h(9/20),\\
 \displaystyle\frac1{2\pi}\arccos\frac{1+R^2-T}{2R},
       &\text{otherwise}.
 \end{cases}
 \tag{11}
\]
The equation in the third case is exactly
\(|1-e^{2\pi h-2\pi ix}|=e^{-2p}\), with positive
quantities on both sides. Endpoint equalities are included. The
gain is evaluated using the full original value in (4), not only the
stationary equation.

Separation now gives the exact comparison
\[
 \max_{x,z\in I}
 \{E_1(x,z)-M-p_a(x-x_0)-p_b(z-z_0)\}
 =-\delta_1+A_\eta^*+A_\epsilon^*.
 \tag{12}
\]
In (12), each gain uses its own height, reference coordinate and
marginal. A sufficient all-directions endpoint bound with reserve
\(\gamma\) is therefore
\(A_\eta^*+A_\epsilon^*\le\delta_1-\gamma\).
No such universal inequality is asserted here.

For a type-four leg, (5) also gives the elementary upper bound
\[
 A_1^*\le
 \max_{d\in[11/50-x_0,\,9/20-x_0]}
       \left\{-qd-\frac{9\pi}{280}d^2\right\}
 \le\frac{70q^2}{9\pi}.
 \tag{13}
\]
The first maximum clips its vertex to the displayed interval. The
exact formula (11) usually retains more information than (13).

## 4. Scope of the remaining comparison

The inherited complete-source estimates supply (2) as an upper rate
for the actual endpoint and revived-row contributions, at both level
parities and with the original polynomial normalization. A sufficiently
small common finite-source tolerance may be assigned after any strict
reserve in (8) or (12) has been obtained. No nonzero contribution,
absence of cancellation, or lower bound follows from this rate
envelope. In particular a revived row can still vanish at a physical
parameter and level.

The favorable-direction statement is a proved subset of the missing
endpoint comparison. Outside it, (11)--(12) retain the exact scalar
obligation. The already saved reference gap alone does not bound its
two nonnegative gains. Their uniform payment on all actual references,
and the right-tail interior stationary candidates, remain separate
questions. Nothing here promotes a few tested references to a
whole-domain source bound or to an actual-word counterexample.

In particular the old distinguished-boundary source argument cannot
automatically be reused for a deficit whose reference tangent also
varies. In the scalar model \(\phi(a)=-a^2/2\), zero source
rate and fixed real target \(x=0\), the rate minus that moving
reference tangent is
\(-\Re\phi(a)-\Re\phi'(a)(0-\Re a)=-|a|^2/2\).
It is larger at the center of a disk than on its circle. This is
only a logical warning about the proposed maximum principle: it is
not an original conditional source and is not a knot or finite-kernel
counterexample. A new reference-domain argument is required before
values on the old distinguished boundary can control (12).
