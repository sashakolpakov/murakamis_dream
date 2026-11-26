# Transporting the original conditional source after a type-four coordinate

Research deduction, 5 November 2026. The complete conditional source on
the full height path after a second type-four coordinate has an upper
rate within \(13/2000\) of its original reference rate, plus an
arbitrarily small finite-source tolerance. The central proof keeps the
contour through the original reference root fixed; the complementary
real-tail lemma retains every original row. No assertion about the
location of a moving root is needed.

## 1. Original source, allocation, and reference contours

Consider an actual complete-color open word of length at least three.
Its second retained coordinate is type four. Put
\[
 a_0=x+ic,\qquad .24<x<.363,\quad -.102<c<-.001,
 \qquad a_k=x+ik,\quad H=7/500.
 \tag{1}
\]
The unselected path has \(c\le k\le0\); the selected path has
\(0\le k\le H\). These are the actual open hybrid height intervals
in the [ending-four collar theorem](research_mixed_second_four_cap_collar.md).
Keep the third retained reference \(b\) unchanged and unselected,
and let its type be \(3+\epsilon\). Thus
\[
 \begin{cases}
 .267<\Re b<.438,\quad -.065<\Im b<.068,&\epsilon=0,\\
 .24<\Re b<.363,\quad -.102<\Im b<-.001,&\epsilon=1.
 \end{cases}
 \tag{2}
\]
Use the original primitive and conditional phase
\[
 Q_\epsilon(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,
 \qquad g'(z)=\log(1-e^{-2\pi iz}).
 \tag{3}
\]
All central arguments use the original regular-strip branches.

Let \(s_0\) be the original conditional index at \((a_0,b)\).
For an ordinary third vertex, the
[universal image bounds](research_mixed_cyclic_critical_height_bounds.md)
give \(\Im s_0>-.102\). At length three the index is instead the
**attached** leg of the terminal endpoint, while \(b\) is its private
leg. The [endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
give \(\Im s_0>-.072\) for type three and \(\Im s_0>-.108\)
for type four. Consequently the common bounds needed here are
\[
 .23<\Re s_0<.45,\qquad -.108<\Im s_0<.068.
 \tag{4}
\]
In particular the terminal index is not bounded using the private-leg
height or a cyclic interior refinement.

The [reduced-disk source theorem](research_mixed_reduced_disk_conditional_packets.md)
at an ordinary third vertex and the
[terminal conditional theorem](research_mixed_terminal_conditional_packet.md)
at length three provide the same original reference contour. Its real
cuts tend to \(\ell=.15\), \(u=.49\); the horizontal aliases are
at heights \(\pm.20\). Write
\[
 \begin{split}
 F_k(s)&=\Re\{Q_\epsilon(s;a_k,b)-\tfrac32g(a_k)
                                -(1+\epsilon/2)g(b)\},\\
 M_0&=F_c(s_0).
 \end{split}
 \tag{5}
\]
The subtraction in (5) is exact: the literal kernel divides by the two
marked factorials, and the first and second Fourier weights contribute
their allocated halves. It does not divide by an actual Fourier polynomial.

At the reference the horizontal segment through \(s_0\) and its two
vertical joins from the real cuts have rate at most \(M_0\). The real
cuts have loss greater than \(1/1000\). Both horizontal aliases, after
their penalty \(2\pi/5\), have loss greater than \(1/10\).
These are the established complete-source inequalities, not consequences
of root uniqueness alone.

For selected \(k\ge0\), retain both original Fourier upper branches:
\[
 F_k^{\rm fac}(s)=F_k(s)-\pi k,\qquad
 F_k^{\rm force}(s)=F_k(s)+\tfrac12\Re g(a_k).
 \tag{6}
\]
The general absolute bound for the
[actual Fourier polynomial](research_mixed_fourier_weight_continuation.md)
gives precisely their maximum, with one arbitrary rate tolerance.
For \(k\le0\), \(-\Re g(a_k)>0\) and the forcing rate is
\(2\pi k_+=0\), so the factorial rate (5) suffices.

## 2. Negative-height transport on the fixed contour

For every \(s=v+iy\) in
\(K=[.15,.49]+i[-.20,.20]\), the function \(k\mapsto F_k(s)\)
is strictly convex on \([-.102,0]\). Indeed
\[
 \frac{d^2}{dk^2}F_k(s)
 =\pi\{\tfrac32\Re\cot\pi a_k-\Re\cot\pi(s+a_k)\}>0.
 \tag{7}
\]
On the first rectangle \(\Re\cot\pi a_k>1/3\).
One elementary verification is
\(\sin(.726\pi)>3/4\), \(\cosh(.204\pi)<5/4\),
so the cotangent numerator is greater than \(3/4\) and its
denominator less than \(9/4\). If \(\Re(s+a_k)<1/2\), its
real cotangent is at most \(\cot(.39\pi)<1/2\); otherwise it
is nonpositive. This proves (7) on the whole rectangle.

Put \(t=x+v\) and
\(A(t,y)=\arg(1-e^{2\pi y-2\pi it})\), with its original
argument in \((-\pi,\pi)\). At \(k=0\),
\[
 F'_0(s)=\tfrac32\pi(1/2-x)-2\pi v-A(x+v,y).
 \tag{8}
\]
If \(t\ge1/2\), then
\(A(t,y)>\pi(1-2t)\) for \(t>1/2\), and \(A(1/2,y)=0\).
Consequently (8) is at most \(\pi(x/2-1/4)<0\).

Suppose \(t<1/2\). The argument \(A(t,y)\) increases with \(y\).
For \(y=-.108\) its real-radius parameter is below one and
\[
 \partial_t A(t,-.108)=\pi\{\Im\cot\pi(t-.108i)-1\}>-\pi.
 \tag{9}
\]
After setting \(y=-.108\), the partial derivatives of the right
side of (8) with respect to \(x\) and \(v\) are respectively
strictly less than \(-\pi/2\) and \(-\pi\), by (9).
It follows that the right side of (8), with \(y\ge-.108\),
is maximized at \(x=.24,v=.15,y=-.108\). At that point it is
\[
 .09\pi-\arg(1-e^{-.216\pi-.78\pi i})<11/175.
 \tag{10}
\]
Here is a rational check of the angle bound used in (10).
The usual \(3.14<\pi<22/7\) gives
\[
 e^{-.216\pi}>1/2,\qquad
 \sin(.22\pi)>63/100,\qquad \cos(.22\pi)<39/50.
 \tag{11}
\]
For the first inequality, the first three terms of the positive
\(2\operatorname{atanh}(1/3)\) series give \(\log2>.69\).
For the other two use the alternating sine and cosine bounds at
\(.69\), since \(.22\pi>.69\). Hence the angle in (10) is
greater than
\(\arctan(63/278)>63/278-(63/278)^3/3>11/50\).
This proves (10). The scalar comparisons in (7) follow just as
elementarily: \(.274\pi>.86\) and
\(.86-.86^3/6)>3/4\), while \(.204\pi<.65\) and the
cosh series through degree four, with its geometric remainder,
is less than \(5/4\). Finally
\(\cot(.39\pi)=\tan(.11\pi)<.35/(1-.35^2/2)<1/2\).

Convexity (7) now yields, on the original zero-mode segment and joins,
\[
 F_k(s)-F_c(s)
 \le(k-c)F'_0(s)
 <\frac{51}{500}\frac{11}{175}
 =\frac{561}{87500}<\frac{13}{2000},
 \qquad c\le k\le0.
 \tag{12}
\]
The join heights lie between zero and \(\Im s_0\), so (4) is
exactly the condition needed for this application.

On the larger alias contour, use only \(A(t,y)>0\) when
\(t<1/2\). Equations (7)--(8) give the coarser bound
\[
 F_k(s)-F_c(s)<\frac{51}{500}\frac{9\pi}{100}<3/100.
 \tag{13}
\]
Thus each horizontal alias still has rate less than \(M_0-7/100\).
At a real cut, the exact specialization of (8) is
\(F'_0(v)=\pi(1/4-x/2-v)<0\), so neither real cut increases.

## 3. Both selected branches decrease on the same contour

For \(0\le k\le H\), set
\(A_0=\arg(1-e^{2\pi k-2\pi ix})\) and
\(A_1=\arg(1-e^{2\pi(y+k)-2\pi i(x+v)})\).
The derivative of the forced branch is
\[
 \frac d{dk}F_k^{\rm force}(s)=A_0-A_1-2\pi v.
 \tag{14}
\]
If \(x+v\le1/2\), then \(A_1\ge0\). The already certified
\(\cot(.24\pi)<11/10\), together with
\(\partial_k A_0=\pi\Re\cot\pi a_k\), gives
\[
 A_0\le\pi\{.26+.014(1.1)\}<.30\pi\le2\pi v.
 \tag{15}
\]
If \(x+v\ge1/2\), use
\(A_0<\pi(1-2x)\) and
\(A_1\ge\pi(1-2x-2v)\), with the latter strict away
from \(x+v=1/2\). In both cases (14) is strictly negative.
The factorial branch derivative is (14) plus
\(A_0/2-\pi<0\), and is therefore negative as well.
At zero, the forced branch is below the factorial branch because
\(J(x)<0\). Thus both selected central branches are bounded by
the unselected rate at zero, at every point of the fixed contour.

## 4. Exhaustion of the central source

Keep the exact original factorial interpolation for the central rows,
and the counterclockwise cotangent rectangle with heights \(\pm.20\).
Its constant part is exactly \(+N\) times the real integral.
Deform that integral to the **reference** height \(\Im s_0\),
retaining both joins. Equations (12) and (14)--(15) bound the
resulting three integrals by the reference allocated rate plus
\(13/2000\). No stationary point on the transported contour is
required for this upper estimate.

Both horizontal aliases obey (13). For the vertical half-grid aliases,
one must not replace their old gap by the horizontal gap \(1/10\).
Instead use the unchanged full-index curvature
\(-\Re Q_{ss}>1/8\) from the
[original contour lemma](research_mixed_conditional_image_contours.md).
It still applies because both transported outer arguments lie in
\(\mathcal Q\). On either vertical half-side, the new allocated
rate minus \(2\pi|\Im s|\) is convex in \(\Im s\).
Its maximum is consequently at the new real-cut rate or the new
horizontal-alias rate. Both were just bounded. This accounts for
every vertical current and every corner, with the original chirp
and the two Fourier branches retained.

**Central-source conclusion.** For either level parity and every
\(\eta>0\), the central part of the literal conditional kernel,
with its actual first selected or unselected halfweight and its
unchanged unselected second halfweight, is at most
\[
 C_\eta N^A\exp N\{M_0+13/2000+\eta\}.
 \tag{16}
\]
Here \(M_0=\Re\phi_{1\epsilon}(a_0,b)\), with the original
reference allocation. The central part means the original rows between
the two half-grid cuts, not a new interpolating polynomial. All central
factorial arguments stay in compact regular strips throughout this
transport. Uniform symbol estimates, half-grid rounding, and the
original actual-Fourier upper estimate cost only the single tolerance
in (16). There is no division by a possibly zero finite factor.

## 5. The complete finite source and first-collar consequence

The [real-tail transport lemma](research_mixed_four_first_vertical_source_transport.md),
equations (7)--(12), bounds every original real row outside the two
cuts by the same reference rate plus \(1/250\). Its proof uses
the exact Poisson-kernel derivative of each full product integral,
including intervals that wrap across an integer, and both selected
Fourier alternatives. The initial tail is reduced to its cut by
the unchanged positive real-row slope. Thus neither a revived row
nor a physical endpoint is omitted. The tail allowance combines
with (16) by taking a maximum, not by addition.

**Theorem 1.** Put \(Y_k=e^{-2\pi ia_k}\),
\(Z=e^{-2\pi ib}\). For either level parity, every
\(\eta>0\), and both physical height intervals in (1),
\[
 |C_{\epsilon,N}(Y_k,Z)|
 |d_N(Y_k)Y_k^{-N\sigma}|^{1/2}|d_N(Z)|^{\epsilon/2}
 \le C_\eta N^A
       \exp N\{\Re\phi_{1\epsilon}(a_0,b)+13/2000+\eta\}.
 \tag{17}
\]
Here \(\sigma=0\) on \([c,0]\), \(\sigma=1\) on
\([0,H]\), and the third coordinate is unchanged and unselected.
The estimate is uniform over the actual reference families described
above. It retains the entire literal kernel and the true Fourier
polynomials; it asserts no nonzero asymptotic on the transported path.

For precision, this is an upper bound relative to the **fixed** reference
phase. It does not prove the stronger moving-phase upper bound (18) of
the [phase theorem](research_mixed_four_first_vertical_phase.md).
That stronger estimate is unnecessary for this first-collar comparison.

The ending-four collar proof, equations (23)--(24), bounds its actual
first-pair rate by \(M_\alpha-1/20\) before the favorable second
supporting tangent is added. Combining it with (17) therefore gives
the following useful consequence. For prefixes \((3,4)\) or \((4,4)\)
of length at least three, retain both first selections allowed by the
first type, either second selection at its physical height, and the
unchanged unselected third reference. The complete product of the
first cap and first two conditional kernels, with the full first and
second Fourier weights and the allocated third halfweight, has finite
loss \(1/25\) relative to
\(M_\alpha+\Re\phi_{1\epsilon}(a_0,b)\).
Indeed
\(1/20-13/2000=87/2000>1/25\); choose the remaining total
source tolerance smaller than \(7/2000\).
The two second-coordinate halfweights are each used once. Equivalently,
the original opposite second tangents cancel, retaining the unused
pair credit as explained in the real-tail lemma's equation (16).
No small reset condition or exclusion of the selected second branch
is required for this consequence.

The existing cap estimate is uniform on a fixed ordinary-color
neighborhood and for its fixed ordinary derivatives. The next conditional
factor in (17) has no ordinary-color argument, so those same statements
hold with its reference parameters fixed. This does not assert a new
ambient relative packet, a comparison after moving the third coordinate,
or global open-word noncancellation. All previously frozen source and
phase proofs remain unchanged.
