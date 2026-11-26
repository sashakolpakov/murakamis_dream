# Complete conditional sources on independent central rectangles

Research proof, 4 November 2026. Frozen manuscripts and completed
critical-image certificates are unchanged.

This theorem supplies the entire canonical conditional sums on a
product region large enough to move every outer real coordinate
independently through \([1/4,2/5]\). Both the original critical
heights and the upward alias heights are included. It does not
bound the remaining outer integration complement.

## 1. Independent parameter domains and the original root

Define
\[
 B_3=[.25,.40]+i[-.030,.020],\qquad
 B_4=[.25,.40]+i[-.057,.0141].
 \tag{1}
\]
The ordered conditional families are
\[
 (\epsilon,\alpha,\beta)\in
 (0,B_3,B_3),\ (0,B_4,B_3),\
 (1,B_3,B_4),\ (1,B_4,B_4).
 \tag{2}
\]
Here \(\beta\) is the vertex's own outer leg and \(\alpha\)
is its left neighbor. Use the original primitive and phase
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad
 Q_\epsilon(z;\alpha,\beta)
 =g(z+\alpha)+g(z+\beta)-(2+\epsilon)g(z)+2\pi i\alpha z.
 \tag{3}
\]
All logarithms below retain their lift in the regular strip
\(0<\Re z<1\).

**Lemma 1.** On every whole parameter product (2), the original
equation \(Q_{\epsilon,z}=0\) has a unique holomorphic root in
\[
                  D=[.10,.49]+i[-.15,.15].
 \tag{4}
\]
The branch is defined on a neighborhood of the closed product.

*Proof.* On \([.15,.49]+i[-.15,.15]\), the existing
[conditional curvature bound](research_mixed_conditional_image_contours.md)
gives \(-\Re Q_{zz}>1/8\). To extend it through the small strip
\(.10\le x\le.15\), put
\[
 c(x)=\frac{\sin(2\pi x)}{\cosh(.30\pi)-\cos(2\pi x)}.
\]
The own-index cotangent is at least
\(\min\{c(.10),c(.15)\}\). Indeed, its derivative in this
interval changes sign at most once, from positive to negative.
Each shifted real cotangent is at most \(\cot(.35\pi)\): a
positive cotangent decreases when its imaginary magnitude increases,
and a negative one is already below this positive upper bound.
Consequently
\[
  -\Re Q_{zz}\ge
  2\pi\bigl(\min\{c(.10),c(.15)\}-\cot(.35\pi)\bigr)>1/8.
 \tag{5}
\]
The additional type-four own-index term is positive.

For each of the four families, the checker verifies the four
strict pointing inequalities on \(D\):
\[
 \begin{array}{ll}
 \Re Q_z(.10+iy)>1/50,&\Re Q_z(.49+iy)<-1/50,\\
 \Im Q_z(x-.15i)>1/50,&\Im Q_z(x+.15i)<-1/50.
 \end{array}
 \tag{6}
\]
Each face has 128 exact slabs. Each parameter contribution is
separately harmonic, so its extrema on its rectangle lie on the
four sides; each side is covered by 32 exact intervals. This proves
(6) on the full products, without a midpoint-root assumption.
Poincaré--Miranda gives a zero of the original real and imaginary
equations. Strict negativity of the real derivative on the convex
rectangle gives complex-gradient injectivity and simplicity. The
implicit function theorem, uniqueness, and compact strict margins
give the global holomorphic branch. \(\square\)

## 2. A full canonical packet, including every revived row

For \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), the finite source is
\[
 \mathcal L_{\epsilon,N}(\alpha,\beta)=
 \widehat P_N(N\alpha)\widehat P_N(N\beta)
 \sum_{j=0}^{N-1}
 \frac{e^{2\pi i\alpha j}
 (r^{N\alpha+1};r)_j(r^{N\beta+1};r)_j}{P_j^{2+\epsilon}}.
 \tag{7}
\]
No row is deleted when a physical root-of-unity zero disappears
off grid. Let \(A_\epsilon\) be the original factorial symbol in
(4) of the [critical-image theorem](research_mixed_conditional_critical_images.md).

**Theorem 2.** Uniformly on all four independent products (2), for
both parities,
\[
 \mathcal L_{\epsilon,N}
 =N^{(1-\epsilon)/2}
 \frac{\sqrt{2\pi}A_\epsilon(z_*;\alpha,\beta)}
      {\sqrt{-Q_{\epsilon,zz}(z_*;\alpha,\beta)}}
 e^{NQ_\epsilon(z_*;\alpha,\beta)}(1+O(N^{-1})).
 \tag{8}
\]
The coefficient is holomorphic and nonzero, with the original
Gaussian branch. The normalized symbol has all fixed holomorphic
derivatives and all fixed asymptotic orders on smaller products.

*Proof.* There are \(4\cdot4^2=64\) distinguished-boundary
pieces. The affine one-variable Newton and source-gap checks are
the same complete tests as in the
[shifted-source proof](research_mixed_shifted_conditional_packets.md),
now evaluated on (1)--(2). Each accepted exact dyadic parameter cell
retains a rational root center, external affine response, and
remainder radius. It proves
\[
                  .20<\Re z_*<.44,\qquad |\Im z_*|<.15.
 \tag{9}
\]
The original logarithmic equation, not merely its exponentiated
polynomial, fixes the lift.

Put \(M=\Re Q_\epsilon(z_*)\), \(\ell=.15\), \(u=.49\),
and \(h=.2\). The certificate proves, on every full cell,
\[
 \begin{split}
 M-\Re Q_\epsilon(\ell)&>10^{-4},\qquad
 M-\Re Q_\epsilon(u)>10^{-4},\\
 M-H_\epsilon(1)&>10^{-4},\\
 M-\Re Q_\epsilon(x\pm ih)+2\pi h&>10^{-3}
                                    \quad(\ell\le x\le u).
 \end{split}
 \tag{10}
\]
Here \(H_\epsilon\) is the full periodic product entropy, including
the revived endpoint. The four analytic last-row branches are all
checked. The exact right-tail polynomial is below one up to both
quadratic vertices, so the entire right tail has its maximum at
\(u\) or \(1\). The established left-tail slope remains positive.
Parameter mean-value bounds use stationarity to remove the root
response exactly; no cell is replaced by its midpoint action.

The unchanged counterclockwise cotangent decomposition gives
exactly \(+N\) times the zero mode. Both horizontal remainders
carry \(e^{-2\pi Nh}\); the vertical half-grid remainders carry
\(e^{-2\pi N|y|}\). The curvature on
\([\ell,u]+i[-h,h]\) gives height convexity and reduces each
vertical remainder to the certified real and horizontal endpoints.
The zero-mode joins at the selected height have gap at least
\((.05)^2/16=1/6400\), by (9), and their real endpoints are
already covered by (10). These strict gaps survive half-grid
rounding. Thus all real tails, revived rows, and contour currents
are retained in the estimate.

The exact factorial symbol is
\(N^{-\epsilon/2}A_\epsilon e^{NQ_\epsilon}\). Its Gaussian,
together with the original \(+N\), gives (8) on each distinguished
boundary. Lemma 1 supplies a holomorphic nonzero leading denominator
on the whole product. Applying the maximum-modulus principle twice
to the normalized finite-source error proves (8) everywhere in (2).
Strict compact margins also give a neighborhood of the closed products;
Cauchy estimates and higher stationary-phase symbols give the stated
derivative and order assertions. \(\square\)

For the actual Laurent kernel
\(C_{\epsilon,N}=\mathcal L_{\epsilon,N}/
[\widehat P_N(N\alpha)\widehat P_N(N\beta)]\), its level power
is \(N^{-(1+\epsilon)/2}\), its phase is
\[
              Q_\epsilon(z_*)-g(\alpha)-g(\beta),
 \tag{11}
\]
and its coefficient is the coefficient in (8) times
\(e^{\pi i(\alpha+\beta)/2}/
[\sqrt{2\sin\pi\alpha}\sqrt{2\sin\pi\beta}]\).
No extra scalar or branch is introduced by this division.

## 3. The central outer region now covered

The [new type-three strip](research_mixed_type_three_window_strip.md)
and the existing type-four height theorem place every actual cyclic
critical leg strictly in (1). Hold its original imaginary part fixed
and let every outer real coordinate range independently over
\([.25,.40]\). Every conditional factor is then one of (2).
The same remains true if any selected type-four heights are moved
through the entire interval from their original values to \(.014\).

Therefore the exact torus source has complete conditional packets
throughout this whole central real product region, with the true
Fourier weights and wrapped factors left unchanged. This is more
than a germ at a critical configuration. It still supplies no bound
on the outer region where a real coordinate leaves \([.25,.40]\),
nor does it alone evaluate the remaining oscillatory outer integral.
In particular, it does not promote a mixed-word knot-volume theorem.

## 4. Reproduction

    python3 experiments/certify_mixed_central_conditional_rectangles.py

The record contains the sixteen complete pointing faces, the exact
left-strip curvature comparison, every accepted boundary-source cell
and rational affine witness, and exact binary coverage of all 64
pieces. The geometric window certificate is an explicit separate
input; no diagnostic window sample is used in this theorem.
