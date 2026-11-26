# Conditional contours on correlated mixed-block images

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The universal two-leg block domain is useful for holomorphic continuation,
but is too large for a termwise absolute estimate of all revived rows of
the canonical conditional source. We give an explicit interior example.
We also record three contour reductions that remain valid on smaller
domains containing the actual cyclic critical points. No mixed-word
asymptotic or failure of cancellation is asserted.

## 1. The canonical source and its block branch

Use the canonical finite conditional functions from the
[type-three](research_mixed_three_canonical_conditional.md) and
[type-four](research_mixed_four_conditional_complex_neighbors.md) proofs:
\[
 \mathcal L_{\epsilon,N}(\alpha,\beta)
 =\widehat P_N(N\alpha)\widehat P_N(N\beta)
 \sum_{j=0}^{N-1}
 \frac{e^{2\pi i\alpha j}
 (r^{N\alpha+1};r)_j(r^{N\beta+1};r)_j}{P_j^{2+\epsilon}},
 \quad r=e^{-2\pi i/N},\quad P_j=(r;r)_j.
 \tag{1}
\]
Here \(\epsilon=0,1\), and
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad
 Q_\epsilon(s;\alpha,\beta)
   =g(s+\alpha)+g(s+\beta)-(2+\epsilon)g(s)
                         +2\pi i\alpha s.
 \tag{2}
\]
All displayed central arguments have real part strictly between zero and
one. Thus these are the original fixed logarithmic lifts.

The [universal block theorem](research_mixed_cyclic_critical_localization.md)
supplies holomorphic roots \((s(a,b),t(a,b))\) on each product of the
closed typed disks
\[
 D_3=\{|z-(.35-.01i)|\le .09\},\qquad
 D_4=\{|z-(.30-.052i)|\le .064\}.
 \tag{3}
\]
For a block of type \(3+\epsilon\), its first equation is exactly
\(\partial_sQ_\epsilon(s;a,t)=0\). The opposite orientation uses
\((\alpha,\beta)=(b,s)\) and critical index \(t\); it must also be
included. Both internal roots lie in the block's own typed disk and in
\(\mathcal Q=\{.23<\Re z<.45,\ |\Im z|<.12\}\).

The compact closed disks have a neighborhood on which these branches
remain holomorphic: the block Hessian is nonsingular throughout
\(\mathcal Q\), and uniqueness glues the local implicit branches.

## 2. A distinguished-boundary reduction

**Lemma 1.** Let \(\Omega_a,\Omega_b\) be disks, or bounded Jordan
domains, whose closures lie in the domains of this block branch.
Suppose the selected conditional phase and its Gaussian coefficient are
holomorphic on a neighborhood of
\(\overline\Omega_a\times\overline\Omega_b\), and the coefficient is
nonzero. A uniform relative packet for (1), composed with
\((\alpha,\beta)=(a,t(a,b))\), on
\(\partial\Omega_a\times\partial\Omega_b\) extends with the same
relative error bound to the whole product. The same holds in the
opposite orientation.

*Proof.* Divide the finite holomorphic source by its nonzero proposed
leading term and subtract one. Apply the maximum-modulus principle first
in \(a\), and then in \(b\). No continuation through a variable cutoff
or agreement only at physical indices is used. The same argument applies
after subtracting any specified holomorphic higher-order symbol.
Fixed derivatives follow on smaller products by Cauchy's formula.
\(\square\)

In the central rectangle below these phase and coefficient conditions
hold automatically. Indeed the conditional Hessian has negative real
part, and the coefficient is
\[
 \frac{\sqrt{2\pi}}{\sqrt{-Q_{\epsilon,ss}}}
 \frac{e^{\pi i(\epsilon s-\alpha-\beta)/2}
       \sqrt{2\sin\pi(s+\alpha)}\sqrt{2\sin\pi(s+\beta)}}
      {(2\sin\pi s)^{1+\epsilon/2}},
 \tag{4}
\]
with the usual analytic square roots. It is nonzero and the source power
is \(N^{(1-\epsilon)/2}\). Lemma 1 requires an actual boundary-source
estimate; holomorphy alone supplies none.

## 3. Uniform central curvature and real-tail tests

**Lemma 2.** For \(\alpha,\beta\in\overline{\mathcal Q}\) and
\(.15\le\Re s\le .49,\ |\Im s|\le .2\),
\[
                     -\Re Q_{\epsilon,ss}>\frac18.
 \tag{5}
\]

*Proof.* Write
\(C(x,y)=\sin(2\pi x)/(\cosh(2\pi y)-\cos(2\pi x))\).
The real part of each shifted cotangent is nonpositive if its real
argument is at least \(1/2\), and otherwise it is at most
\(\cot(.38\pi)\). For \(.15\le x\le .27\),
\(C(x,y)\ge\min\{C(.15,.2),C(.27,.2)\}\): it decreases in
\(|y|\), and as a function of \(x\in(0,1/2)\) it has only one
critical point, a maximum. For \(x\ge .27\), both shifted cotangents
are nonpositive and \(C(x,y)\ge C(.49,.2)\). The exact scalar bounds
\[
 \begin{split}
 2\pi\{\min(C(.15,.2),C(.27,.2))-\cot(.38\pi)\}&>1/8,\\
 2\pi C(.49,.2)&>1/8
 \end{split}
 \tag{6}
\]
prove (5); the extra type-four cotangent is favorable. The imaginary
quadratic in (2) changes no real Hessian. \(\square\)

The full real-row entropy, including revived rows, is
\[
 \begin{split}
 H_\epsilon(u;\alpha,\beta)
  ={}&\Re g(\alpha)+\Re g(\beta)
   +\int_0^u\log|1-e^{-2\pi i(\alpha+x)}|\,dx
   +\int_0^u\log|1-e^{-2\pi i(\beta+x)}|\,dx\\
  &-(2+\epsilon)J(u)-2\pi u\Im\alpha .
 \end{split}
 \tag{7}
\]
It is continuous, with the usual integrable limits at a zero.
On \(0<u\le .15\), each ratio
\(|\sin\pi(u+\alpha)|/\sin\pi u\) is greater than two:
for a real shift the minimum occurs at an endpoint of
\([.23,.45]\), and decreases as \(u\) increases; an imaginary shift
increases the modulus. Since \(2\sin(.15\pi)<1\),
\[
             H_\epsilon'(u)\ge\log4-.24\pi>1/2.
 \tag{8}
\]
Thus the entire left real tail is bounded by its value at \(.15\).

There is a finite algebraic right-tail test. Put
\[
 c_z=\cos\pi z,\quad d_z=\sin\pi z,\quad
 q_z=\frac{\sin(2\pi\Re z)}
              {\cosh(2\pi\Im z)-\cos(2\pi\Re z)},
 \quad w=-\cot\pi u.
 \tag{9}
\]
Then \(q_z>0\) and
\[
 e^{2H_\epsilon'(u)}
 =4^{-\epsilon}e^{2\pi(\Im\beta-\Im\alpha)}
    |c_\alpha-wd_\alpha|^2|c_\beta-wd_\beta|^2
                                         (1+w^2)^\epsilon.
 \tag{10}
\]
The right side is a real polynomial of degree four or six in \(w\).
If it is strictly less than one on
\([ -\cot(.49\pi),\max(q_\alpha,q_\beta)]\), then
\[
 \max_{.49\le u\le1}H_\epsilon(u)
                    =\max\{H_\epsilon(.49),H_\epsilon(1)\}.
 \tag{11}
\]
Indeed each quadratic modulus in (10) is increasing after its vertex
\(q_z\), and \((1+w^2)^\epsilon\) is increasing for \(w>0\).
There is consequently exactly one later crossing of one. The entropy
first decreases and then increases. This test retains the endpoint
\(u=1\); it does not replace the revived tail by a decreasing branch.

For fixed real \(u\), (7) is separately subharmonic in the external
parameters \(a,b\) after substituting \((\alpha,\beta)=(a,t(a,b))\).
Each integral is an integral of logarithms of holomorphic moduli; its
integrable zeros cause no exception. Therefore the minimum of the
selected-action gap from this row also occurs on the distinguished
boundary. This is compatible with, but weaker than, the exact
finite-source statement of Lemma 1.

## 4. A genuine obstruction on the larger two-leg image

Take a type-three block with left external type four and right external
type three, at the rational interior inputs
\[
                   a=\frac{3131-1146i}{10000},\qquad
                   b=\frac{4028-828i}{10000}.
 \tag{12}
\]
The literal unsquared block equations have their unique selected root
near
\[
 s=.405812323751165+.020538477635504i,\qquad
 t=.337758049539820+.017916246413660i.
 \tag{13}
\]
The checker encloses this root by a complex two-variable Newton
self-map, verifies \((a,b)\in\operatorname{int}(D_4\times D_3)\),
and retains both original logarithmic equations. At this branch,
\[
 \begin{split}
 M&=\Re Q_0(s;a,t)\in(.6473,.6474),\\
 H_0(1;a,t)&=\Re g(a)+\Re g(t)-2\pi\Im a+2\pi\Im t
                                      \in(.6535,.6536),\\
                         H_0(1;a,t)-M&>1/200.
 \end{split}
 \tag{14}
\]

This endpoint is an actual term of (1), not just a formal entropy.
For every level \(N\), the last summand equals exactly
\[
 R_{\epsilon,N}
 =\frac{\widehat P_N(N\alpha)\widehat P_N(N\beta)}{N^{2+\epsilon}}
 e^{2\pi i\alpha(N-1)}
 \frac{(1-e^{-2\pi iN\alpha})(1-e^{-2\pi iN\beta})}
      {(1-e^{-2\pi i\alpha})(1-e^{-2\pi i\beta})}.
 \tag{15}
\]
This follows from the full root product and \(P_{N-1}=N\).
At \((\alpha,\beta)=(a,t)\), \(\Im a<0<\Im t\), so neither
factor in the numerator has an oscillatory zero asymptotic. The original
factorial symbol gives a nonzero coefficient \(c(a,t)\) with
\[
 |R_{0,N}|=|c(a,t)|N^{-1}
             e^{NH_0(1;a,t)}(1+O(N^{-1})).
 \tag{16}
\]
In particular no termwise absolute revived-row complement estimate below
the selected rate can hold on the whole two-leg image (3).

This does **not** show that the sum (1) lacks a geometric packet: its
rows can cancel. It does not show that (12) occurs in a cyclic critical
configuration. The improved actual type-three depth bound already
excludes the input \(b\), and the sharper type-four window bounds
exclude \(a\). A restricted image theorem or a coherent endpoint
cancellation remains possible. Lemmas 1--2 and the tail test (10)
remain applicable to those smaller domains.

## 5. Reproduction and computational scope

Run:

    python3 experiments/check_mixed_conditional_image_contours.py

The checker verifies the exact last-row algebra, the scalar inequalities
used in Lemma 2 and (8), and an outward enclosure of (12)--(14). It does
not certify a packet on all typed images, a cancellation among the
revived rows, or a global mixed-word source.
