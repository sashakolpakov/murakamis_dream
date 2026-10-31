# A modulus-only switch on the independently derived 6_1 longitude curve

28 October 2026. This note tests the remaining classical inequality in
[the macroscopic actual-source spectral upper bound](actual_macroscopic_a_spectral_upper_bound.md).
It proves that the largest-modulus longitude root switches between two
distinct analytic branches already on the 6_1 two-bridge curve. The
switch is exact and transverse. Consequently, a theorem that simply
identifies the pointwise largest-modulus root with one distinguished
geometric branch cannot hold for this curve.

This does **not** invalidate the spectral upper bound, which makes no
such identification. An actual all-level quantum annihilator with this
classical companion has not been verified here. The integral values
below are labelled numerical diagnostics; no rigorous volume
calibration or general sharp upper bound is claimed.

## 1. The curve from the two meridians, without a polynomial table

Use the p=9,q=5 two-bridge presentation, with alternating exponents
`(+,-,-,+,+,-,-,+)`, and matrices

\[
A=\begin{pmatrix}M&1\\0&M^{-1}\end{pmatrix},\qquad
B=\begin{pmatrix}M&0\\-z&M^{-1}\end{pmatrix},\quad
W=(AB^{-1}A^{-1}B)^2.
\]

The relation is \(WA=BW\). Setting \(t=M^2+M^{-2}\), direct matrix
multiplication gives

\[
WA-BW=\begin{pmatrix}0&R\\zR&0\end{pmatrix},\qquad
R=z^4+(5-2t)z^3+(t^2-6t+11)z^2+(t^2-7t+12)z+5-2t.       \tag{1}
\]

Let \(W^{\mathrm{rev}}=(BA^{-1}B^{-1}A)^2\). The exponent sum is zero,
so the usual peripheral word has no meridian-power correction:
\(\Lambda=WW^{\mathrm{rev}}\). It commutes with B modulo R. Its chosen
eigenvalue is \(L=\Lambda_{11}\). An explicitly checked simplification is

\[
L=-\frac{W_{12}(M,z)}{W_{12}(M^{-1},z)},\qquad
W_{12}=-\frac{(-M^2+z+1)(-M^4z+M^2z^2+2M^2z+2M^2-z)}{M^3}. \tag{2}
\]

Equation (2) holds on the regular open set and its cleared numerator
vanishes modulo R. Eliminating z gives, up to a nonzero meridian factor,
the following normalized longitude polynomial. Put \(Y=M^2\):

\[
F(Y,L)=L^4+a(Y)L^3+b(Y)L^2+c(Y)L+1,                       \tag{3}
\]

\[
\begin{aligned}
a&=-Y^4+Y^3+3+3Y^{-1}-2Y^{-2},\\
b&=Y^4-3Y^3-Y^2+3Y+6+3Y^{-1}-Y^{-2}-3Y^{-3}+Y^{-4},\\
c&=-2Y^2+3Y+3+Y^{-3}-Y^{-4}.
\end{aligned}
\]

For \(|Y|=1\), b is real and \(c=\bar a\), so F is self-inversive.
The defining matrices, cleared relation, peripheral commutation,
rational longitude, and resultant are checked symbolically by
[the independent audit](../experiments/audit_six_one_spectral_envelope.py).
Swapping A and B gives the equivalent reversed convention; no table identity is used in the proof.

## 2. Exact transverse switch, without numerical branch tracking

Use the same meridian path as the actual-source spectral theorem:
\(M(x)=-e^{\pi i x}\), \(Y(x)=e^{2\pi i x}\), \(1/2\le x\le1\).
At \(x_*=5/6\), \(Y^2-Y+1=0\), and (3) becomes

\[
F=L^4+5L^3+15L^2+5L+1.
\]

Writing \(w=L+L^{-1}\) reduces it to

\[
w^2+5w+13=0,\qquad w=\frac{-5\pm3i\sqrt3}{2}.             \tag{4}
\]

The four roots are distinct. The two outside the unit circle are
conjugates, approximately

\[
L_\pm=-2.325158539755156\ \pm2.809324795549955i,
\qquad |L_\pm|=3.646733886903201.
\]

They therefore define two different analytic eigenvalue branches near
\(x_*\). Implicit differentiation gives the exact radical expression

\[
\frac{d}{dx}\log|L|
=\Re\left(-2\pi i\,\frac{Y F_Y}{L F_L}\right).             \tag{5}
\]

Substitution of (4) into (5), evaluated using certified 192-bit Arb
balls, gives

\[
\begin{aligned}
\partial_x\log|L_-|&\in(-7.2708825660,-7.2708825659),\\
\partial_x\log|L_+|&\in( 3.6119136194, 3.6119136195),\\
\partial_x\log|L_-|-\partial_x\log|L_+|
&\in(-10.8827961855,-10.8827961853).
\end{aligned}                                                   \tag{6}
\]

The root modulus ordering thus reverses across \(x_*\). On a sufficiently
small left interval \(|L_-|>|L_+|>1\); on the right
\(|L_+|>|L_-|>1\). This is a **modulus crossing, not an eigenvalue
collision**. No root-selection numerical algorithm is needed for (6).
In particular, the pointwise spectral envelope is locally a splice of
two distinct analytic branches. Its integral across any small interval
containing the switch strictly exceeds the integral of either one of
these two branches across the same interval.

## 3. Labelled numerical diagnostic and its limits

The Riley discriminant is exactly

\[
5t^6-32t^5+26t^4+42t^3-55t^2+226t-23.                     \tag{7}
\]

Its two roots in \([-2,2]\) are approximately
\(-1.68654658027416\) and \(0.104189696631736\). On the meridian
path they occur near \(x=0.590312770945900\) and
\(x=0.758294907395908\). Numerical continuation of the four Riley
roots, using (2), gives the following **uncertified** diagnostics:

\[
\begin{array}{c|c}
\text{classical coherent branch integral }2\pi\int_{1/2}^1\log|L|\,dx
 &\text{approximately}\\ \hline
\text{one expanding branch}&3.16396\\
\text{other expanding branch}&1.41511\\
\text{pointwise maximum of all four branches}&3.44499
\end{array}
\]

These numbers suggest that the spectral-radius estimate loses a
positive amount by switching branches. The rigorous result of this
note is the local transverse switch (6), not a certified comparison of
the last row with hyperbolic volume. To turn that diagnostic into a
volume obstruction still requires a checked regulator calibration of
the coherent branches, or an independent certified volume comparison.

The next analytic question is therefore phase-aware transport of the
actual recurrence. Since the expanding eigenvalues remain distinct at
the modulus switch, a product of slowly varying companion matrices need
not follow the pointwise larger modulus by arbitrary switching. This
note proves no adiabatic estimate and no lower bound for the selected
original source.

Reproduce the exact proof and optional diagnostic with

```sh
python3 experiments/audit_six_one_spectral_envelope.py --points 20001
```

The JSON output keeps the certified statements and numerical diagnostics
in separate fields. Omitting `--points` runs only the exact algebra and
certified switch.
