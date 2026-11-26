# An endpoint bound for a type-three block with a type-four left leg

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The 192-bit author passes all 16 reference boundary products with 18,981
cells. The independent 256-bit positive-frequency/sine-cotangent replay
passes with 20,584 cells after exact refinements, in addition to replaying
the complete source grids and reference-slope cover. This note concerns
one exterior family, not the full mixed-word source estimate.

The left leg has type four and the own block has type three; write this
ordered type pair as \((4,3)\). Use the
original zero-lift phase \(\Phi(a,b)\) in
[the support-grid theorem](research_mixed_endpoint_support_grid.md), on
\[
 a\in[.27,.33]+i[-.057,-.02],\qquad
 b\in[.30,.39]+i[-.03,.02].
 \tag{1}
\]
These are geometric reference domains. The target left variable runs through
a larger height range:
\[
 z=x+ih,\quad0\le x\le1,\qquad
 \begin{cases}-.057\le h\le0,&\sigma=0,\\
              0\le h\le.014,&\sigma=1.
 \end{cases}
 \tag{2}
\]
The right target is the tapered period endpoint \(e=0\) or \(e=1\).
Both have \(Y=e^{-2\pi ie}=1\); both original supporting planes are retained.

## 1. Statement in the original source normalization

**Theorem 1.** Uniformly for all references (1), targets (2), and both
\(e\in\{0,1\}\), the whole finite expression satisfies, for sufficiently
large \(N\),
\[
 \begin{split}
 &|C_{0,N}(e^{-2\pi iz},1)|\,
 |d_N(e^{-2\pi iz})e^{2\pi iN\sigma z}|^{1/2}\\
 &\qquad\le C N^A
 \exp N\left\{
  \Re[\Phi(a,b)+\Phi_a(a,b)(z-a)+\Phi_b(a,b)(e-b)]
                              -\frac1{2000}\right\}.
 \end{split}
 \tag{3}
\]
Every original row, Fourier forcing term, and selected-alias weight is
retained. The square root denotes a nonnegative modulus only.

The inequality persists with a smaller positive gap when the right target
lies in a sufficiently small fixed complex neighborhood of either endpoint.
This is the tapered-endpoint neighborhood, rather than an assertion about
a fixed nonzero right endpoint height. Derivatives in the right target preserve the same weighted bound. In the
left variable, derivative bounds concern the literal holomorphic product
\(C_{0,N}(X,Y)^2d_N(X)X^{-N\sigma}\), or complete contractions
with their original integer Fourier weights. No derivative is asserted
for the half-modulus expression in (3), and no Fourier factor is divided out.

## 2. Horizontal target heights and exact reference covers

Write \(\kappa=\Re\Phi_a\) and
\[
 C_e=\Phi-a\Phi_a+(e-b)\Phi_b+ih\Phi_a.
 \tag{4}
\]
For each fixed target height in the source grid, the full row-source
upper defect is \(S_h(\kappa)-\Re C_e\). The source-grid certificate
bounds it by local affine chords \(L_j(\kappa)=\alpha_j\kappa+\beta_j\).
Only chords whose certified intervals intersect a reference cell's
slope enclosure are considered.

The source defect is separately subharmonic in reference \(a,b\), as
proved in the support-grid theorem. Hence it suffices to check the
sixteen products of reference rectangle edges. On each parameter cell,
the checker encloses the exact selected quadratic root and its zero
logarithmic lift before evaluating the following holomorphic quantities.

For clarity let \(H\) be the condensed Hessian of \(\Phi\). The negative
of the chord-adjusted supporting plane has exact reference derivatives
\[
 \begin{split}
 \partial_a(L_j(\Phi_a)-C_e)
    &=(\alpha_j+a-ih)H_{aa}-(e-b)H_{ab},\\
 \partial_b(L_j(\Phi_a)-C_e)
    &=(\alpha_j+a-ih)H_{ab}-(e-b)H_{bb}.
 \end{split}
 \tag{5}
\]
Here \(L_j(\Phi_a)=\alpha_j\Phi_a+\beta_j\); its real part is
the required chord. The finite supporting scalar is bounded by its
midpoint value plus the exact edge-direction derivatives from (5)
times their parameter radii, with all derivatives enclosed on the
whole cell. This retains the correlated complex tangent terms.

The Hessian used in (5) is the exact Schur complement of the original
one-row phase:
\[
 \begin{split}
 T&=g''(s+a)+g''(s+b)-2g''(s),\\
 A&=g''(s+a)+2\pi i,\qquad B=g''(s+b),\\
 H_{aa}&=g''(s+a)-\tfrac32g''(a)-A^2/T,\\
 H_{ab}&=-AB/T,\qquad
 H_{bb}=g''(s+b)-g''(b)-B^2/T .
 \end{split}
 \tag{6}
\]
No positive-real replacement of this complex Hessian is made.

For each local slope interval intersecting the cell, the checker bounds
its chord defect on the entire parameter cell. This may overestimate
the relevant subset, but it remains an upper bound there. The intersecting
intervals cover the cell's slope range. No chord is asserted to bound
the source outside its own slope interval. Every accepted bound is
strictly less than \(-1/1000\), for both endpoint representatives and
all horizontal target heights needed in (2). Prefix-free exact binary
covers include every boundary parameter.

## 3. The target seam verticals

The two vertical target edges \(x=0,1\) admit an exact source bound.
For \(h<0\), put \(R=e^{-2\pi h}>1\). The literal row modulus at
\(Y=1\) is
\[
 \frac{|X^{-j}p_j(X)|}{S_j}
       =\prod_{k=1}^j\frac{|R-r^k|}{|1-r^k|},\qquad
 \frac{|R-r^k|^2}{|1-r^k|^2}
       =R+\frac{(R-1)^2}{|1-r^k|^2}>1.
 \tag{7}
\]
Thus the last row dominates, and its exact product is
\[
             \frac{R^N-1}{N(R-1)}.
 \tag{8}
\]
Its upper rate is \(\log R=-2\pi h\), uniformly including \(h=0\)
by the elementary geometric-sum bound. The true half Fourier
weight has zero upper rate at the negative-height seam, by its
retained forced recurrence.

For \(h\ge0\) and \(\sigma=1\), the coherent identity
\[
 C_{0,N}(X,1)=N\overline{d_N(1/\overline X)}
 \tag{9}
\]
would give kernel rate zero at the seam. That cancellation-only estimate
does not bound the raw row sum, so it is not used for the following
subharmonic extension or endpoint thickening.

Instead put
\[
 R_0=e^{-.028\pi},\quad \delta=1-R_0,\quad
                 \alpha=\operatorname{arsinh}(\delta/2)<1/20 .
 \tag{9a}
\]
Indeed \(\delta<.028\pi<.088\), and \(\operatorname{arsinh}x<x\)
for \(x>0\). For \(R=e^{-2\pi h}\in[R_0,1]\), every raw row factor
obeys
\[
 \frac{|R-r^k|^2}{|1-r^k|^2}
 =R+\frac{(1-R)^2}{D_k}
 \le1+\frac{\delta^2}{D_k},\qquad D_k=|1-r^k|^2.
 \tag{9b}
\]
The majorant factors are at least one, so each partial product is at most
their full product. The exact cyclotomic product identity gives
\[
 \prod_{k=1}^{N-1}\sqrt{1+\frac{\delta^2}{4\sin^2(\pi k/N)}}
        =\frac{\sinh(N\alpha)}{N\sinh\alpha}.
 \tag{9c}
\]
To verify it, use \(\delta=2\sinh\alpha\) and write each numerator as
\(e^{2\alpha}|1-e^{-2\alpha}r^k|^2\), then apply
\(\prod_{k=1}^{N-1}(1-zr^k)=(1-z^N)/(1-z)\) and
\(\prod_{k=1}^{N-1}|1-r^k|=N\).

Thus every raw row, and its sum, has upper rate at most
\(\alpha<1/20\), uniformly on the selected height interval.
The selected normalized half Fourier weight has zero seam rate, including
\(h=0\), by the retained forced recurrence. Equivalently the same
factorwise inequality, integrated in the row variable, bounds the
whole continuous raw entropy by \(\alpha\); it does not require a
cancellation of rows.

Consequently the seam row-source upper rate is \(-2\pi h\) on the
unselected interval and is bounded by \(1/20\) on the selected interval.
Subtracting the original plane gives an affine upper bound in \(h\)
in each case. The certificate checks these seam bounds at their height
endpoints, preserving both \(x=0,1\) and \(e=0,1\). Each bound is again
less than \(-1/1000\).

For every fixed original row, its source entropy minus the target plane
is subharmonic in \(z\); the Fourier part is the maximum of its harmonic
factorial and forcing branches. Maximizing over the compact row interval
preserves this property. The horizontal and vertical estimates therefore
bound the whole target rectangles (2). Applying the separate reference
maximum principles then bounds every reference in (1). The small
Fourier-envelope tolerance and polynomial prefactors fit inside the
reserve from \(1/1000\) to \(1/2000\), proving (3).

## 4. Thickening the tapered endpoint

If the right target logarithmic coordinate lies within \(\delta\) of \(e\),
the full finite-product regularization gives, uniformly in every row,
\[
 |p_j(Y)|\le S_j\,N^A e^{N\omega(\delta)},\qquad
                         \omega(\delta)\longrightarrow0 .
 \tag{10}
\]
It retains all finite-product zeros and high rows; this is the proved
regularization in the boundary-strip note. The other factors in (1)
are unchanged. The right geometric tangent changes by \(O(\delta)\)
uniformly on the compact reference domains. Choose a fixed \(\delta\)
so these costs are smaller than the remaining strict gap. This proves
the endpoint-neighborhood assertion with a smaller positive margin.
Cauchy's estimates in the right target apply while the left modulus weight
is fixed. Squaring (3) gives the bound for the displayed integer-weight
holomorphic product; Cauchy's estimates on smaller parameter neighborhoods
then give its derivatives and those of complete holomorphic contractions.
This argument does not divide by a possibly vanishing Fourier polynomial.

## 5. Reproduction and remaining scope

    python3 experiments/check_mixed_endpoint_support_grid.py --precision 192
    python3 experiments/check_mixed_43_endpoint_support.py --precision 192
    python3 experiments/replay_mixed_43_endpoint_support.py --precision 256

The independent replay imports no author routines. It uses the
positive-frequency primitive, sine/cotangent derivatives, and the
complementary reciprocal quadratic formula. It verifies both original
and refined binary covers and input immutability.

The source and reference optimizations are separate two-parameter covers.
The result does not establish the other endpoint families, the intervening
outer region, or a full mixed-word finite-sum asymptotic.
