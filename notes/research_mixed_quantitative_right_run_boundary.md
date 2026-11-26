# Explicit boundary costs for long right runs

Research proof, 5 November 2026. This makes the cutoff in the
[direct replacement deduction](research_mixed_direct_right_run_replacement.md)
explicit. Every proper right run of length at least 552 is suppressed,
provided its other coordinates lie outside the fixed zero collar.
For the nonlow alphabet the cutoff is 352. These large constants are
not intended to settle the remaining short-run comparisons.

All phases, Fourier polynomials and finite kernels are the original
ones. No new critical-root or parameter cover is used.

## 1. A real connector floor uniform down to zero

Let \(f_{\eta\epsilon}=\Re\phi_{\eta\epsilon}\) on real arguments.
The other real argument \(t\) belongs to its actual typed interval
\[
 I_0=[.30,.39],\qquad I_1=[.27,.33].
 \tag{1}
\]
The 32 individual boundary corners in the frozen
[seam-run scalar certificate](research_mixed_seam_run_connector_lower.md)
all have real phase greater than \(11/25=.44\). These are the
recorded real phases themselves, without subtracting their old
height costs or raw ceilings. Joint real concavity therefore gives
\[
 f_{\eta\epsilon}(x,t)>11/25,\qquad
 f_{\eta\epsilon}(t,x)>11/25,\qquad .1\le x\le.5,
 \tag{2}
\]
in the corresponding typed orientation.

For \(0<x\le.1\), write \(p=\cot\pi x\) for the moving real cotangent
and \(q=\cot\pi t\) for the other one. Then \(p\ge3\) and \(0\le q\le1\).
The selected root \(S\) is a root of the original monic quadratic or
cubic in the [acute-gradient theorem](research_mixed_acute_gradient_height_transfer.md).
Every root of either polynomial has
\[
                         |S|\le3p+5.
 \tag{3}
\]
Indeed the quadratic coefficients have moduli at most \(p+1,p+2\).
The cubic has coefficients
\[
 p+q+i,\qquad pq+i(p+q),\qquad -ipq+2p-2q-2i,
 \tag{4}
\]
whose moduli are at most \(p+2,2p+1,3p+4\).
Cauchy's elementary monic-polynomial root bound proves (3).
The same estimates hold with the two outer cotangents interchanged.

The polynomial values at \(i\) and \(-i\) are
\[
 \begin{array}{c|cc}
 &i&-i\\ \hline
 F_0&-2+2iq&-2-2ip\\
 F_1&-4(q+i)&-2i(p-i)(q+i).
 \end{array}
 \tag{5}
\]
Each has modulus at least two. Factoring the polynomial over all
of its roots, using degree at most three and (3), gives
\[
 |S-i|,\ |S+i|\ge\frac2{(3p+6)^2}.
 \tag{6}
\]
Consequently either ratio in the original real gradient has modulus
at most
\[
 \frac{(4p+5)(3p+6)^2}{2}
                         \le\frac{425}{6}p^3 .
 \tag{7}
\]
Here \(4p+5\le17p/3\) and \(3p+6\le5p\), since \(p\ge3\).

Use \(\cot\pi x\le1/(\pi x)\), \(2\sin\pi x\ge4x\), and the
original own-halfweight coefficient, which is either zero or one half.
The real derivative in the moving coordinate satisfies
\[
 0<f_x\le C-\frac72\log x,\qquad
 C=\log(425/6)-3\log\pi-\log2 .
 \tag{8}
\]
The strict lower bound is the already proved real low-coordinate
monotonicity. The upper bound follows from (7); when the halfweight is
absent, adding \(-\tfrac12\log(4x)>0\) only enlarges it.
The focused scalar check verifies
\[
 \int_0^{1/10}\left(C-\frac72\log x\right)dx<119/100.
 \tag{9}
\]
The enclosed value is about \(1.169204069\).
Integrating (8) from \(x\) to .1 and using (2) proves
\[
 f_{\eta\epsilon}(x,t)>-3/4,\qquad
 f_{\eta\epsilon}(t,x)>-3/4,\qquad0<x\le.5.
 \tag{10}
\]
This also proves uniform continuous extension of these real phase
values as \(x\downarrow0\), by the common integrable derivative bound.
It does not extend a finite-kernel saddle packet to zero.

## 2. Repaired complex connectors and reference gradients

Consider a boundary between a real right coordinate and an A coordinate
in the direct replacement deduction. The repaired right coordinate has
real part \(t=\Re r_j\in I_{\epsilon_j}\), its selection is absent,
and its height is a fraction of its reference height.
The A target and its selection are unchanged.

If the A real coordinate is at least .1, both repaired arguments belong
to the proved polygons. The acute affine transfer, retaining the
frequency branch at a selected endpoint, bounds the total height loss
by
\[
                         .0609\pi<1/5.
 \tag{11}
\]
For clarity, a first endpoint costs at most \(.021\pi\):
the respective type-three, unselected type-four and selected type-four
costs are \(.01\pi,.0114\pi,.021\pi\). A second endpoint costs at
most \(.0399\pi\): its three costs are
\(.015\pi,.0399\pi,.014\pi\). These use
\(\pi(1/2-x)\le.4\pi\), \(|h_4|\le.057\),
\(h_3\in[-.03,.02]\), and selected \(h\in[0,.014]\).
Allowing both endpoints to be selected only enlarges this bound.
The true maximum of Fourier branches is no smaller than the frequency
branch used for this lower phase estimate.

Combining (2) and (11), the repaired selected coherent rate \(e^\#\)
on a boundary edge satisfies
\[
                    e^\#>6/25\quad(x_A\ge.1).
 \tag{12}
\]
If instead \(x_A\in[\rho,.1]\), both repaired heights are zero:
the A coordinate lies in the zero interval of every left cutoff,
including that of the repaired right row. Thus (10) gives, uniformly,
\[
                    e^\#>-3/4\quad(x_A\ge\rho).
 \tag{13}
\]
Selections at a real A coordinate have unit modulus.

Let \(P_j\) be either derivative of the original phase at its actual
complex reference pair. Its real part satisfies
\(\Re P_j\ge-1/5\), by the
[actual-reference slope theorem](research_mixed_geometric_support_slopes.md).
There is also the elementary bound
\[
                         |\Im P_j|<18/5.
 \tag{14}
\]
At the real parts of the reference pair the acute theorem bounds this
imaginary derivative by
\(\pi/2+(.23\pi)/2\) in absolute value. Along the straight reference
height segment, writing \(\phi''=-A+iB\), its imaginary derivative
changes by \(-A\,dh\). The
[full-reset theorem](research_mixed_full_height_reset.md) gives
\(0<A<20I\) throughout the segment. Both reference heights have
absolute value at most .057. Hence the additional change has modulus
at most \(20(.057)\sqrt2\). The focused scalar inequality
\[
 \pi/2+.115\pi+20(.057)\sqrt2<18/5
 \tag{15}
\]
proves (14). This argument uses the legitimate full-product bound on
\(A\), not harmonicity of a matrix eigenvalue. The real-slope premise
concerns actual cyclic references; no independent-box slope claim is made.

## 3. A complete raw boundary source ceiling

The full finite-product bound is
\[
 I_h(u,x)\le L(u)+2\pi h_+u,\qquad
 L(u)=-2J((1-u)/2)\le1/3,\qquad -J(u)\le1/6.
 \tag{16}
\]
It includes all angles, heights, row endpoints and product zeros;
see the [whole-product proof](research_mixed_boundary_strip_bounds.md).
Only one boundary endpoint can have nonzero height. Its combined
radial/chirp contribution is at most \(2\pi(.057)\):
if it is the first argument, \(h_+-h=(-h)_+\); if it is the second,
the contribution is \(h_+\). The denominator power is at most three.

The original Fourier halfweight at the real right argument has upper
rate zero, with arbitrary positive finite tolerance. At the other
endpoint the normalized halfweight has rate at most \(1/12\).
One exact finite proof uses \(\deg d_N<N\) and the completed unit-circle
bound \(\max|d_N|\le\operatorname{poly}(N)e^{N/6}\).
An unselected type-four target is inside that circle. A selected target
is outside it, but polynomial maximum modulus gives
\[
 |d_N(X)X^{-N}|\le |X|^{-1}\max_{|Y|=1}|d_N(Y)|
                         \le\operatorname{poly}(N)e^{N/6}.
 \tag{17}
\]
Taking its nonnegative modulus half-power proves the claim. Type-three
endpoints carry no such factor. This retains the actual polynomial,
its forcing and every original selection.

Equivalently the exact continuous raw envelope has the same bound:
on the left half-period \(\nu(x,h)=-\Re g(x+ih)\) is at most
 \(1/6\) for \(h\le0\), and at most \(1/6+\pi h\) for \(h\ge0\),
because \(0\le\Im g'(x+ih)\le\pi\). Thus the selected normalized
half rate \(\frac12\max(\nu,2\pi h)-\pi h\) is at most \(1/12\).
The endpoint statement also follows from (17), with no logarithm chosen
at a product zero.

Putting all terms together gives the uniform boundary raw rate
\[
 \mathscr F_j\le\frac23+\frac12+\frac1{12}
                         +\frac{57\pi}{500}
                  =\frac54+\frac{57\pi}{500}<\frac{13}{8}.
 \tag{18}
\]
All finite factors satisfy this ceiling with one arbitrarily small
positive total tolerance. Both level parities and all original rows
remain present.

## 4. Explicit boundary costs and run cutoffs

At a boundary the unchanged A argument cancels from
\(\Gamma(z)-\Gamma(z^\#)\). The changed right argument moves from
real \(x_R\in[.5,1]\) to \(t+ih^\#\), where \(t\ge.27\) and
\(|h^\#|\le.057\). Equations (14)--(15) and the real slope lower
bound imply
\[
 -\Re\{P_j(x_R-t-ih^\#)\}
 \le\frac15(1-.27)+\frac{18}{5}(.057)
                       =\frac{439}{1250}.
 \tag{19}
\]
This is the only remaining tangent term; no reference constant or
neighboring imaginary tangent is discarded.

The exact boundary quantity \(\mathcal B_j=D_j-W_j^\#\) from the
direct deduction consequently obeys
\[
 \begin{split}
 \mathcal B_j&<
       \frac{13}{8}+\frac34+\frac{439}{1250}<\frac{11}{4}
                                      &&(x_A\ge\rho),\\
 \mathcal B_j&<
       \frac{13}{8}-\frac6{25}+\frac{439}{1250}<\frac74
                                      &&(x_A\ge.1).
 \end{split}
 \tag{20}
\]
The exact residuals in these two rational comparisons are
\(119/5000\) and \(69/5000\). These are bounds for actual references of every cyclic
word; they do not depend on the collar width.

**Theorem 1.** Fix \(0<\rho\le.001\). On the original hybrid contour
with all nonright coordinates in \([\rho,.5]\), if every proper right
run has length at least 552, the complete raw/coherent rate is at most
\(M-|T|/100\). If all nonright coordinates lie in \([.1,.5]\), length
352 suffices. All-right cycles have loss \(m/50\), without a length
restriction.

Indeed every internal RR edge retains its proved raw loss \(1/50\),
and its repaired residual is nonnegative. A run of length \(k\) has
two boundary costs and \(k-1\) such internal edges. For the two cases
in (20), respectively,
\[
 2(11/4)-(k-1)/50\le-k/100\quad(k\ge552),\qquad
 2(7/4)-(k-1)/50\le-k/100\quad(k\ge352).
 \tag{21}
\]
The original tangent sum cancels, and all AA targets remain unchanged,
as proved in the direct deduction. This includes loops, parallel
incidences and multiple disjoint runs. For each fixed word, one total
finite-source tolerance less than \(1/200\) gives an integral upper
bound with rate \(M-|T|/200\), retaining the original scalar,
carriers, Fourier terms and bounded contour Jacobian.

## 5. The zero-contact limitation

The constants in (20)--(21) do not deteriorate as \(\rho\downarrow0\).
Nevertheless the theorem does not include the physical collar
\(0\le x_A<\rho\). There the periodic cutoff is
\(L_b(x_A)=1-x_A/\rho\), not zero. After right replacement the
middle height can remain nonzero, so the both-real premise of (13)
does not apply. At \(x_A=0\) no compact coherent packet is available
from the all-real source theorem. Continuity of a phase value is not
a uniform asymptotic for those original finite rows.

The already proved closed-half result handles zeros by literal raw
collar bounds and a separate replacement comparison. Combining those
bounds with an adjacent R component requires new boundary bookkeeping;
it is not obtained by putting \(\rho=0\) in Theorem 1.
Short right runs and these mixed zero/right contacts remain open.
No full-period or new knot-family theorem is asserted.

## Reproduction

    python3 experiments/check_mixed_quantitative_right_run_boundary.py --precision 256

The focused checker verifies the polynomial identities and scalar
inequalities, re-extracts all 32 real corner floors, and validates the
current inherited records. It proposes no roots and creates no new
parameter or source cover.
