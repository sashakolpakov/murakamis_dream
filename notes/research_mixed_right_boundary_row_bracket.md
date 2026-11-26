# A fixed interior interval for every reduced right-boundary row

Research lemma, 5 November 2026. After the right angle has been fixed
at \(1/2\) in the complete raw envelope, its maximizing row stays in
\((1/5,2/5)\) whenever the other real coordinate is in \([.1,.5]\).
This includes the early selected rise and all admitted height bands.
It supplies an interval for the continuous row maximum, not a sign for
minimum transport or a lower bound for the finite kernel.

Use the normalized real primitives of the
[complete right-row reduction](research_mixed_complex_right_row_reduction.md):
\[
 J(t)=\Re\frac{\operatorname{Li}_2(e^{-2\pi it})-\pi^2/6}{2\pi i},
 \qquad
 G_H(t)=\Re\frac{\operatorname{Li}_2(e^{-2\pi H-2\pi it})-\pi^2/6}{2\pi i}.
 \tag{1}
\]
Let the other target be \(y+ih\), with
\[
 1/10\le y\le1/2,\qquad |h|\le57/1000,
 \qquad H=|h|,\quad R=e^{-2\pi H}.
 \tag{2}
\]
The own-factorial indicator is \(\epsilon\in\{0,1\}\), and
\(d=1\) means that this complex target is the first argument of the
original kernel. Up to terms independent of the row, the literal raw
rate at right angle \(1/2\) is
\[
 E(u)=J(u+1/2)+G_H(y+u)-(2+\epsilon)J(u)+\lambda u,
 \qquad \lambda=2\pi(h_+-dh),\qquad 0\le u\le1/2.
 \tag{3}
\]
In particular \(0\le\lambda\le2\pi H\). The true Fourier
alternatives, half allocations and selected monomials at the other
target are independent of \(u\). They do not change its maximizer.

**Theorem 1.** The complete continuous raw envelope has a unique
maximizing row \(u_*\), and
\[
                         1/5<u_*<2/5.
 \tag{4}
\]
More precisely,
\[
 E'(1/5)>\log\frac{25\sqrt{13}}{81}>0,
 \qquad
 E'(2/5)<\log\frac{50}{81}<0.
 \tag{5}
\]
The assertions include either orientation, both own types, either
sign of height, all actual selections and forcing branches, and the
closed other endpoint \(y=1/2\). No physical row or level parity is
discarded: the earlier complete-row theorem first bounds all upper
rows and puts the full continuous maximum in the lower half.

**Proof.** Proposition 2 of the cited right-row theorem proves
\(E''(u)\le-2\pi\), uniqueness of its interior maximum and the
endpoint derivative signs. It therefore suffices to verify (5).
For \(0<u<1/2\),
\[
 E'(u)=\log(2\cos\pi u)
       +\log|1-R e^{-2\pi i(y+u)}|
       -(2+\epsilon)\log(2\sin\pi u)+\lambda.
 \tag{6}
\]
The elementary bounds \(\pi<22/7\) and
\[
 e^x\le1+x+\frac{x^2}{2(1-x/3)}\quad(0\le x<3)
 \tag{7}
\]
give
\[
 2\pi H<9/25,\qquad
 e^{9/25}\le\frac{1577}{1100}<\frac32,
 \qquad R>\frac23.
 \tag{8}
\]
For (7), bound \(n!\ge2\,3^{n-2}\) for every \(n\ge2\)
in the exponential series and sum the resulting geometric series.

At \(u=1/5\), one has \(y+u\in[3/10,7/10]\subset(1/4,3/4)\).
Consequently its cosine in (6) is strictly negative and
\[
 |1-R e^{-2\pi i(y+1/5)}|^2>1+R^2>13/9.
 \tag{9}
\]
The exact trigonometric bounds
\[
 2\cos(\pi/5)>8/5,\qquad
 1<2\sin(\pi/5)<6/5
 \tag{10}
\]
and \(\lambda\ge0\) yield
\[
 E'(1/5)>
 \log\left(\frac85\frac{\sqrt{13}}3\left(\frac56\right)^3\right)
 =\log\frac{25\sqrt{13}}{81}>0.
 \tag{11}
\]
The final strict sign follows from \(8125>6561\).

At \(u=2/5\), use \(|1-R e^{it}|\le2\),
\[
 2\cos(2\pi/5)<2/3,\qquad 2\sin(2\pi/5)>9/5.
 \tag{12}
\]
Together with (8), these imply
\[
 E'(2/5)<\log\left(\frac23\,2\left(\frac59\right)^2\right)+\frac9{25}
 <\log\frac{50}{81}<0.
 \tag{13}
\]
All four trigonometric comparisons follow from the exact pentagon
values and \(11/5<\sqrt5<9/4\). Strict concavity now proves (4).
The row-independent Fourier terms can be restored unchanged.
\(\square\)

This bracket is uniform over the entire neighboring interval in (2),
not only at a moving minimum. It therefore also applies to a stationary
neighbor whose height changes during a coupled minimum flow. It does
not replace the stationarity equation by an arbitrary row in the bracket:
using that stronger relaxation in a subsequent derivative estimate would
require a separate proof.

The accompanying checker verifies the rational inequalities, exact
pentagon reductions, outward scalar signs and the current complete-row
input. There are no new critical roots, parameter covers or finite-word
enumerations. Reproduction:

    python3 experiments/check_mixed_right_boundary_row_bracket.py
