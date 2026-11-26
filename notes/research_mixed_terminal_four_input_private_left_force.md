# Private-left force contraction on the whole type-four input disk

Research deduction, 6 November 2026. The completed correlated affine
certificate encloses the canonical suffix with preceding ordinary type
four and terminal type four over its entire type-four external disk.
One exact posterior step improves its error radii enough to prove that
flattening the private left face contracts the negative terminal-index
force throughout that disk. This needs no new logarithm, primitive,
root, inverse, or parameter evaluation.

## 1. Certified family and an exact posterior step

Let \(q=(e,\xi,t,a,s)\) be the original canonical family, with
external flag \(\beta=1\), terminal flag \(\epsilon=1\), and
\[
 D_4=\{|b-(.30-.052i)|\le8/125\}.
 \tag{1}
\]
Use case \((1,1)\), radius multiplier one, of the completed
[correlated affine record](../repro/results/research-mixed-terminal-correlated-affine-family.json),
SHA256 51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1.
Its validation rule is the
[correlated affine theorem](research_mixed_terminal_correlated_affine_family_certificate.md).
It proves, simultaneously for every \(b\in D_4\),
\[
 q_*(b)=q^0+u(b-b_0)+\zeta(b),\qquad
 |\zeta_i(b)|<\rho_i,\quad
 \rho=(1/500,1/1000,1/200,1/200,1/100).
 \tag{2}
\]
The exact Gaussian-rational \(q^0,u,B\), nonnegative residual bounds
\(\mathcal R_i\), and nonnegative matrix bounds \(\mathcal E_{ij}\)
are the saved data of this same case and candidate. They retain the
shared complex parameter until after the primitive Taylor bounds.

The fixed-point equation and the already certified tube give
\[
 |\zeta_i(b)|\le\widehat\rho_i:=
       \mathcal R_i+\sum_j\mathcal E_{ij}\rho_j<\rho_i.
 \tag{3}
\]
This is one application of the original contraction inequality, not a
new contraction test on a smaller box. All derivative bounds continue
to use the old certified tube; no circular radius improvement is made.
Exact fraction comparison of the saved quantities gives
\[
 (\widehat\rho_e,\widehat\rho_\xi,\widehat\rho_t,
   \widehat\rho_a,\widehat\rho_s)
 <10^{-6}(655,281,2119,3804,9592).
 \tag{4}
\]
Let \(w_i\) be the saved outward upper bound for \((8/125)|u_i|\).
The rectangle
\[
 \Re q_i^0\pm(w_i+\widehat\rho_i),\qquad
 \Im q_i^0\pm(w_i+\widehat\rho_i)
 \tag{5}
\]
contains the full canonical image. Exact comparisons give the following
deliberately rounded containing rectangles:

| Coordinate | Real part | Imaginary part |
|---|---|---|
| \(e_*\) | \((.3443,.3473)\) | \((-.0394,-.0364)\) |
| \(t_*\) | \((.3022,.3131)\) | \((-.0707,-.0599)\) |
| \(a_*\) | \((.2996,.3212)\) | \((-.0631,-.0416)\) |

The [saved-only checker](../experiments/check_mixed_terminal_four_input_private_left_force.py)
records the exact posterior radii and unrounded rectangles, verifies
the original case and candidate association, and checks every rational
comparison below. It does not revalidate a root or reevaluate a primitive.
Its execution is separate from the proof.

## 2. Uniform strict sign from the original terminal-index equation

Write \(a_*=A+ic,\ t_*=x+ih\), and retain \(.01\le H\le.014\).
The original forces are
\[
 A_t=\Re\{g'(t_*+A+iH)-g'(t_*+a_*)\}-2\pi(H-c),\qquad
 d_L=\Re\{g'(t_*+.27)-g'(t_*+e_*)\}.
 \tag{6}
\]
The endpoint rectangles in (5) imply \(d_L>0\), by Lemma 1 of
[the uniform force theorem](research_mixed_terminal_private_left_uniform_force.md).
The original zero-lift terminal-index equation gives
\[
 e^{2(A_t+d_L)}
 =\frac{(R^2+r^2-2Rr\cos2\pi(x+A))
          (1+r^2-2r\cos2\pi(x+.27))}
         {(1+r^2-2r\cos2\pi x)^3},
 \quad r=e^{2\pi h},\quad R=e^{-2\pi H}.
 \tag{7}
\]
Stationarity is used only at the canonical reference. No point of the
enclosing Cartesian box is assumed stationary.

The image bounds give
\[
 A>.299,\quad x>.302,\quad h>-.071,\qquad
 A<.36,\quad x<.35,\quad h<-.02,
 \tag{8}
\]
and consequently
\[
 r>.63,\quad R<47/50,\quad
 -\cos(2\pi x)>.32,\quad
 -\cos(2\pi(x+A))<.81,\quad
 -\cos(2\pi(x+.27))<.9.
 \tag{9}
\]
For exact elementary witnesses put
\[
 X=(.604-.5)(157/50),\quad
 Y=(2(.302+.299)-1)(157/50),\quad
 Z=(2(.302+.27)-1)(157/50),\quad W=2(.071)(22/7).
 \tag{10}
\]
Then
\[
 \begin{split}
 X-X^3/6-.32&=\frac{1107220079}{1464843750000},\\
 .81-(1-Y^2/2+Y^4/24)&=
                  \frac{41359056567086399}{9375000000000000000},\\
 .9-(1-Z^2/2+Z^4/24)&=\frac{368268659413}{762939453125000},\\
 \frac{100}{63}-1-W-\frac{W^2}{2(1-W/3)}
                  &=\frac{483193}{20110500}.
 \end{split}
 \tag{11}
\]
The alternating sine/cosine estimates and positive exponential series
prove (9), with the monotonicity directions of the uniform force theorem.
The existing \(R<47/50\) witness is
\(1+z+z^2/2-50/47=553503/587500000>0\),
where \(z=157/2500<.02\pi\).

Define
\[
 \begin{split}
 D(r)&=(1+r^2+(16/25)r)^3,\\
 N(r)&=(r^2+(47/50)^2+2(81/100)(47/50)r)
                                      (1+r^2+(9/5)r),\\
 P(r)&=D(r)-N(r).
 \end{split}
 \tag{12}
\]
The ratio in (7) is strictly less than \(N(r)/D(r)\).
On \(r=.63+.37y,\ 0\le y\le1\), the degree-six Bernstein
coefficients of \(P\), with denominator \(15000000000000\), have
numerators
\[
 (2461503846015,\ 6691602565740,\ 13102522533472,\
 22512461911476,\ 36025059204800,\ 55128208400000,\
 81831360000000).
 \tag{13}
\]
Every coefficient is at least the first, so \(P\ge b_0>0\).
Since \(D(r)\le(66/25)^3\), the inequality \(\log(1-u)\le-u\)
proves
\[
 A_t+d_L<
 -\frac{b_0}{2(66/25)^3}
 =-\frac{54700085467}{12266496000000}<0.
 \tag{14}
\]
Thus \(0<d_L<-A_t\) holds for every canonical reference in the
entire disk (1), uniformly over the stated selected heights.

## 3. What transfers to the original source

For actual references in the original oriented and inverse-feasible
source domain, the completed bare private-left comparison gives
\(E_L\le U_L<-1/20000\). Combining (14) with the original
[joint face transfer](research_mixed_terminal_private_left_joint_transfer.md)
gives, for both full-\(P\) alternatives,
\[
 \sup D_\nu^L\le
 T_\nu+G_s(A_s)+G_{a,\nu}(A_{a,\nu})+G_t(A_t)-1/20000.
 \tag{15}
\]
The actual outside input lies in \(K_4\), and its other inverse legs
must retain the original source restrictions. Equation (15) transfers
any valid same-height main three-cost upper budget there. It does not
assert that such a budget is already negative uniformly on \(K_4\).
The force conclusion (14) itself holds on all of \(D_4\), independently
of the narrower finite-source scope.

No bound at \(H=.01\) is combined with another branch at a different
height. The original boundary tangent, complete selected weight and
incoming modulus halfweight are retained. There is no assertion about
the unresolved type-three external family, whole-word suppression,
finite-word realization of every canonical point, or knot-volume growth.

The sole saved-data verification command, after review, is

~~~sh
python3 experiments/check_mixed_terminal_four_input_private_left_force.py --output repro/results/research-mixed-terminal-four-input-private-left-force.json
~~~

It checks exact saved fractions and the displayed polynomial identities
only; it imports no interval, root, source, or primitive evaluator.
