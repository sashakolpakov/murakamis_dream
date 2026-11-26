# A raw-row obstruction to replacing a right coordinate by its geometric real part

Research result, 5 November 2026. The focused checker below verifies the
original reference and both replacement roots. This concerns a proposed
comparison of an absolute-row envelope with a coherent replacement. It
does not contradict a finite-kernel asymptotic or a volume statement.

## 1. An actual alternating reference and exact targets

Use the calibrated allocated phases \(\phi_{\eta\epsilon}\) and
\(g(z)=(\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6)/(2\pi i)\).
Write \(J(x)=\Re g(x)\). Let \(\alpha\) be the already isolated root of

\[
4\alpha^4-6\alpha^3+4\alpha^2-2\alpha+1=0
\]

in the rational disk recorded by
[the original interface theorem](research_three_four_source_interface.md).
Set

\[
K=(1+2\alpha-4\alpha^2)^{-1},\quad U=1-2\alpha,\quad
V=(1-K)/(2K),\qquad r_3=-\frac{\log U}{2\pi i},\quad
r_4=-\frac{\log V}{2\pi i},\quad c=\Re r_3.
\tag{1}
\]

These are the actual alternating critical coordinates, not independent
reference-box corners. For completeness the checker freshly verifies the
quartic contraction, the two exact identities modulo its polynomial,

\[
(1-U^2)(1-UV)=V(1-U)^2,\qquad
(1-V^2)(1-UV)=U(1-V)^3,                         \tag{2}
\]

and the zero lifts of the original logarithmic equations

\[
\begin{split}
 g'(2r_3)+g'(r_3+r_4)-2g'(r_3)+2\pi i r_4&=0,\\
 g'(2r_4)+g'(r_3+r_4)-3g'(r_4)+2\pi i r_3&=0.
\end{split}                                                    \tag{3}
\]

The exponentials of (3) equal one by (2), and their imaginary parts lie
strictly between \(-\pi\) and \(\pi\). They are also the original outer
gradient equations when the eliminated inner coordinate equals its own
outer coordinate. The [cyclic uniqueness theorem](research_mixed_cyclic_critical_localization.md)
therefore identifies (1) with the actual period-two reference. Repetition
gives the actual alternating four-cycle. In particular
\(c\in(.3535,.3537)\).

Take the unselected target four-cycle

\[
(x_0,x_1,x_2,x_3)=(1/2,1/2,1/2,1/10),
\qquad\text{types }(3,4,3,4).                         \tag{4}
\]

Use the exact periodic [split-cutoff hybrid contour](research_mixed_split_cutoff_hybrid_contour.md).
All its hybrid heights are zero. The proposed replacement sends only
\(x_0\) to \(c\). Its new height is still zero because its left neighbor
is \(.1\); the other row heights are unchanged. Both adjacent neighbors
belong to the closed nonlow half-period. Thus this is an allowed isolated
right-center comparison, without independent-neighbor or reference-box
relaxation.

## 2. The original rows exceed the coherent replacement

On the left incident edge choose row fraction \(u=7/25\), and on the
right choose \(v=23/100\). The full real raw-row exponent, including the
original Fourier halfweights, is

\[
\begin{split}
\mathcal R={}&J(19/50)+J(39/50)-\tfrac32J(1/10)-2J(7/25)\\
 &+2J(73/100)-3J(23/100).
\end{split}                                                    \tag{5}
\]

Indeed the literal row exponent is
\(I_0(u,a)+I_0(u,b)-(2+\epsilon)J(u)\), where
\(I_0(u,a)=J(a+u)-J(a)\). The type-four halfweight at \(.1\)
adds \(-J(.1)/2\); at \(.5\) the factorial and forcing rates both
equal zero. Chirps and selected factors have unit modulus here. No
Fourier alternative has been discarded.

The proposed coherent replacement has rate

\[
\mathcal C=\Re\{\phi_{1,0}(1/10,c)+\phi_{0,1}(c,1/2)\}.
\tag{6}
\]

For each term in (6), the checker verifies a complex Newton disk for
the original logarithmic conditional equation, with its root in the
selected cotangent chamber and all three factorial arguments in their
original regular strips. It then evaluates (5)--(6) outward. The result is

\[
\boxed{\mathcal R-\mathcal C>3/50.}                    \tag{7}
\]

The enclosed difference is approximately \(.06589829625\).
Consequently even a non-strict universal inequality comparing this raw
two-edge envelope to the geometric-center replacement is false.
Continuity also gives strictly interior isolated-right targets near (4).
No such thickening is needed for (7).

This is an obstruction for the literal absolute-row envelope, not just
for an arbitrarily chosen interpolant. At levels \(N\) divisible by
100, the original two row indices are \(28N/100\) and \(23N/100\),
and the relevant physical outer indices are \(N/10,N/2\). All chosen
products are nonzero: their lengths stay strictly below the first
cyclotomic zero. Their logarithmic absolute rates are exactly (5), by
the ordinary finite-product Riemann limit. The actual physical weights,
with the original DFT definition in the
[Fourier-weight theorem](research_mixed_fourier_weight_continuation.md),
are \(d_N(r^a)=1/P_a\), including the half-index rate zero.
The [complete real half-endpoint packet](research_mixed_half_endpoint_conditional_packet.md)
gives rate (6) for the coherent replacement. Thus the product of these
two absolute rows, with their allocated weights, exceeds the coherent
replacement on an exponential scale along this subsequence. A signed
conditional sum can still cancel those rows. The full four-cycle also
contains the two unchanged edges; (7) does not compare the entire cycle
with its geometric critical rate.

```sh
python3 experiments/check_mixed_geometric_right_replacement_obstruction.py
```

The check is a fixed reference disk, two fixed conditional-root disks,
exact polynomial identities and outward scalar comparisons. It performs
no parameter search or interval cover.
