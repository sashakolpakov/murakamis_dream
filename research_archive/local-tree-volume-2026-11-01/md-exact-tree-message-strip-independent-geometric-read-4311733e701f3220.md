# Exact tree messages: source and strip comparison

1 November 2026. Private independent derivation of the interfaces in
md-exact-tree-message-poisson-strip-lemma.

## 1. The actual typed functional has no parent-angle dependence

I reopened the current all-circle curvature note, Section 3, and
actual_main_meridian_filled_volume, Section 2, equations (13) and
(16a)--(16e). The latter fixes the compatible mixed-order carriers
before any evaluation root is chosen. Lowering a product junction
with its compatible reverse morphism makes the reference carriers
cancel cyclically. Its tensor is the actual normalized linear
functional
\[
 D_v(P)=\phi_{\sigma_v}\bigl(R_{\sigma_v}^{n_v}P\bigr),
 \qquad \sigma_v\in\{0,s,-s\},
\tag{1}
\]
with the prescribed opposite-order scalar retained separately.
The actual crossing polynomial remains inside (1), including inverse
powers. The choice of a different evaluation root only reassociates
this same tensor network.

Let \(X=-2\cos t\), \(Y=-2\cos u\), and let
\(P_v(X)=\prod_{w\text{ child}}M_{w\to v}(t)\).
The exact parent-edge evaluation is
\[
 M_{v\to p}(u)=
 \sum_{k=0}^{N-1}
 \gamma_{vp}\frac{H_N}{W_k}\,
        D_v\bigl(e_k(X)P_v(X)\bigr)\,e_k(Y).
\tag{2}
\]
The moving or constant quotient acts only on \(X\); its coefficients
depend on the main-meridian parameter and the prescribed type, not
on \(u\). Its repeated-root normal evaluation is linear for the
same reason. Thus even when the input degree in \(X\) is large,
the remaining \(Y\) degree is at most \(N-1\).
The result is an even trigonometric polynomial of degree at most
\(N-1\).

No physical reverse crossing is substituted for a coherent inverse
carrier here. If one rewrites a reversed edge using a different
forward physical turn, its known scalar ratio must remain. Keeping
the original edge tensor in (2) already does that. Its \(\gamma_{vp}\)
is assigned once. The opposite-order reference factors and the
single main closing/framing factor do not depend on the parent
angle and do not alter the degree statement.

This exact degree assertion does not prove nonvanishing of the
message or a bound on its normalized coefficients.

## 2. The subharmonic estimate

For a trigonometric polynomial \(f(t)=F(e^{it})\) supported in
\([-m,m]\), the function \(P(z)=z^mF(z)\) is holomorphic on the
closed unit disk. The assumed real envelope bounds
\(\log|P|\) on its boundary by the harmonic function
\(\log B+NA-Nc+Nc\operatorname{Re}z\).
The subharmonic maximum principle applies also when \(P\) has zeros.
At \(z=e^{-y+it}\), \(y\ge0\), division by \(|z|^m\) gives
\[
 |f(t+iy)|\le
 B\exp\{N[A-c(1-e^{-y}\cos t)]+my\}.
\tag{3}
\]
For \(y<0\), apply the same proof to \(z^mF(z^{-1})\) and evaluate
at \(z=e^{y-it}\). The boundary cosine is unchanged. This proves
the displayed estimate for both signs of \(y\), without reality
or positivity of the coefficients.

If \(m\le\kappa N\), the difference from the real exponent is
\(-c(1-e^{-|y|})\cos t+\kappa|y|\), bounded above by
\((c+\kappa)|y|\). This proves the stated coarser linear-strip
estimate. Its use of a degree bound is independent of the depth
of the subtree.

## 3. Near and far regions

One hypothesis should explicitly be written as \(C\ge0\) in the
local bound
\[
 |f(t+iy)|\le B_*\exp N[A-at^2+Cy^2].
\tag{4}
\]
This entails no restriction: replace any supplied \(C\) by
\(\max(C,0)\), which only enlarges an upper bound.
The far-region conclusion otherwise need not follow from the
formula as written if \(C<0\).

With this harmless convention, set
\[
 c_*=\min(c/2,2a),\qquad
 y_0\le\min\left(y_*,
          \frac{c(1-\cos\rho)}{2(c+\kappa)}\right).
\tag{5}
\]
For \(\rho\le|t|\le\pi\), the linear imaginary cost is at most
\(c(1-\cos t)/2\). This gives the desired exponent
\(-c_*(1-\cos t)+Cy^2\), since \(c_*\le c/2\) and \(C\ge0\).
For \(|t|\le\rho\), use \(t^2\ge2(1-\cos t)\) in (4) and
\(c_*\le2a\). Finally
\(1-\cos t\ge2t^2/\pi^2\) gives the global quadratic real decay.
The two regions cover the whole specified strip, including their
common boundary.

The proof is uniform in auxiliary parameters when its two input
bounds and degree estimate are uniform. Applying it to
\(M(u;s)/M(0;s)\) additionally requires the nonzero denominator and
the stated normalized envelopes. Nonvanishing alone does not bound
those envelopes polynomially in \(N\). The root report correctly
retains these as separate induction hypotheses and does not infer
the completed quantum theorem from this lemma.
