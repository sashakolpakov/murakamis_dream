# Independent check of the root half-twist contour and circle exposure

1 November 2026. Private report; no repository file is changed.

I checked both complete written arguments:
`/private/tmp/md-half-twist-root-chirp-and-far-color-gap.md` and
`/private/tmp/md-separated-hub-far-color-rerooting.md`.
The derivation below records the normalization, contour, and source interfaces on which the conclusion depends.

## 1. The actual crossing lift and the paired residues

Let \(d=N-1\), \(a_s=d/2+s\), and \(\tau_r=2\pi(a_s-r)/N\). Then
\(-2\cos\tau_r=2\cos((2r+1-2s)\pi/N)\), exactly the prescribed moving equal-color Casimir node. Also \(e^{iN\tau_r}=(-1)^d e^{2\pi is}\). Writing \((-1)^r=q^{Nr}\) in the original stripped crossing value gives
\[
 (-1)^r q^{r(r+1)-2sr}
 =q^{-a_s^2}\exp(iN\tau_r^2/(4\pi)).
\]
The integer correction in the exponent is \(2Nr\), not an unretained branch constant. Multiplication by the original Cartan scalar \(q^{(d+s)^2/2}\) gives
\[
 q^{d^2/4-s^2/2}\exp(iN\tau_r^2/(4\pi)).
\]
Raising this to \(\epsilon=0,\pm1\) yields precisely the stated full root chirp. Its scalar and inverse have bounded modulus on any fixed \(s\)-disk.

The physical auxiliary pivot gives
\(L_j(-2\cos\tau)=\sin(j\tau)/\sin\tau\). For generic \(s\), the monic relation satisfies
\[
 P_s'(-2\cos\tau_r)=N\sin(2\pi s)/\sin\tau_r.
\]
Consequently the top-coefficient trace has the factor
\((-1)^dN/\sin(2\pi s)\), as in equation (13) of the contour proof.

For \(z=e^{iN\tau}\), \(a=(-1)^d e^{2\pi is}\), and \(b=(-1)^d e^{-2\pi is}\), direct subtraction gives
\[
 \frac{iNz}{z-a}-\frac{iNz}{z-b}
 =-2(-1)^dN\sin(2\pi s)\frac{z}{(z-a)(z-b)}.
\]
The function \(B(\tau)=\sin(j\tau)\exp(i\epsilon N\tau^2/(4\pi))E(-2\cos\tau)\) is odd. The reflected grid identity is exactly
\(\tau_{d-r}(-s)=-\tau_r(s)\), so the contour of the difference of logarithmic derivatives gives twice the original grid sum. Combining these facts gives the stated sign and prefactor \(-N^2C_{N,\epsilon}/(2\pi i)\). No additional factor two, parity sign, or modified dimension remains.

This uses the crossing chirp only at its exact spectral roots. It does not identify the chirp with the canonical crossing polynomial away from those roots. The continuation to a double root is justified through the meridian parameter and retains the actual Hermite coordinate.

## 2. Uniformity on the complex parameter disk

For \(|s|\le R<1/2\), both reflected grids lie strictly inside the vertical sides \(\operatorname{Re}\tau=\pm\pi\), with separation at least \(\pi(1-2R)/N\). Their imaginary heights are at most \(2\pi R/N\). Thus a fixed positive rectangle height contains all roots for sufficiently large \(N\).

The horizontal kernel is \(O_R(e^{-Ny})\). On a vertical side it is reduced to
\[
 \frac{t}{(t+e^{2\pi is})(t+e^{-2\pi is})},\qquad t=e^{-Nv}>0.
\]
Both complex constants have argument in \([-2\pi R,2\pi R]\) and modulus between \(e^{-2\pi R}\) and \(e^{2\pi R}\). The elementary angle inequality gives
\(|t+a|\ge\cos(\pi R)(t+|a|)\). Hence the kernel is \(O_R(e^{-N|v|})\), including \(v=0\). This proves uniformity on a genuinely complex disk, rather than merely on real parameters.

After pairing the grids, the contour has no \(\sin(2\pi s)\) denominator. Its boundary remains pole-free on the whole disk. The integral is holomorphic through \(s=0\), and the established physical crossing polynomial has the same removable collision. Analytic continuation therefore recovers the full confluent trace at completeness. The proof does not need to estimate the two separated singular grid formulas there.

## 3. The strict loss and the endpoint sides

Assume the actual remaining raw polynomial has the stated Gaussian
\[
 |E(-2\cos(t+iv))|\le N^K
 \exp N(F-ct^2+Cv^2+o(1)),\qquad c>0.
\]
The chirp has modulus \(\exp(-\epsilon Ntv/(2\pi))\), and the circle sine has modulus at most \(e^{j|v|}\). If \(j\le(1-\delta)N\), the horizontal exponent is at most
\[
 F-ct^2+|t|y/(2\pi)+Cy^2-\delta y+o(1)
 \le F+\bigl(C+(16\pi^2c)^{-1}\bigr)y^2-\delta y+o(1).
\]
A sufficiently small fixed \(y>0\) gives a strict loss. On the two vertical sides the estimate is at most
\[
 F-c\pi^2+Cy^2+y/2+o(1),
\]
which has a strict loss after shrinking the same \(y\). Both requirements are compatible. This checks the endpoint currents directly; no periodic gluing of the chirp is assumed. The contour length and \(N^2\) prefactor have only polynomial cost.

For an opposite-color root, use the constant relation and its complete full crossing polynomial. The same contour at kernel parameter zero is the continued complete Hermite identity. The reverse mixed crossing differs by the already known bounded monodromy scalar. The typed root-adjunction ratios and the single final \(H_N(s)\) factor are also bounded, so they do not consume the strict rate loss.

## 4. Why every original circle can be exposed at the same action

The source exposure uses the exact fixed Frobenius metric and
\[
 \langle T_{\gamma_1}f,g\rangle
   =(\gamma_1/\gamma_2)\langle f,T_{\gamma_2}g\rangle.
\]
Both applicable turn types and their scalar ratio are retained. Normalized carrier composition and consecutive dual turns justify the change of recursive evaluation; no knot isotopy or arbitrary open-coupon permutation is needed.

For a selected physical circle there are three possibilities.

1. If its leaf is flagged, the remaining source is the raw product of the other outgoing L/A modules. Each has a fresh Gaussian; the raw product has a Gaussian at the sum of their intrinsic pressures. The original flagged-root identity makes this sum exactly \(F_0\).

2. If its ordinary leaf is incident to a flagged hub, transfer that leaf's closing turn. The remaining operator is one decorated module, formed from the hub's different distinguished coupon and all its other branches. Its Gaussian pressure is \(2G_0+\sum\Omega_{\mathrm{other}}\). In the earlier flagged-root accounting the selected ordinary leaf contributed exactly \(2G_0\), so this is again \(F_0\).

3. If its ordinary leaf is incident to a bare hub, transfer the closing turn. All other incoming branches are L modules, because no bare hubs are adjacent. The remaining operator is one whole bare-hub output, with \(B=d_v-1\ge2\). Its Gaussian pressure is \(\widehat\omega_B+\sum c_b\), exactly the original closing probe action with this existing physical leaf. It equals \(F_0\); no new leaf is inserted.

These cases are exhaustive. Rerooted descendant branches still satisfy the separation condition. In particular each bare hub is still fed only L cones, and every intervening flagged hub restores such a cone from its spectral inputs. This is the crucial structural hypothesis; the proof would not apply to arbitrary adjacent bare hubs.

In each case the remaining polynomial is independent of the selected auxiliary color. Its bound is uniform over all other physical colors. A product is kept raw when its Gaussian is used; canonical quotient reduction is not presumed to preserve that Gaussian. The separately treated strict two-leaf case leaves one decorated module at pressure \(2G_0=F_0\).

There are only finitely many original circles, so the minimum of the resulting positive losses gives a uniform loss whenever any original color is at most \((1-\delta)N\). The conclusion holds at both parities on each fixed \(|s|\le R<1/2\), at the original augmented action. It does not prove a filled-knot rate or a regular microscopic profile limit.
