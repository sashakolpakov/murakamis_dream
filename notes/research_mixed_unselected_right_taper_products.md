# Original-source bounds for all unselected right-taper products

Research proof, 4 November 2026. The author outward covers, independent written/code reviews and
fresh 320-bit replays have passed.
The reviewed one-taper result and all earlier artifacts are unchanged.

This extends the original conditional packet to the full independent
square of outer real arguments \([.22,.50]^2\). A two-tilt estimate then
proves a geometric supporting-plane bound when either or both
unselected target coordinates lie on the right taper. Selected aliases
are not included in this comparison.

## 1. The complete source on the larger square

Keep the exact primitive, phase and canonical finite function from the
[right-guard theorem](research_mixed_right_guard_conditional_packets.md):
\[
 \begin{split}
 g(z)&=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},\\
 Q_\epsilon(s;a,b)&=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,\\
 \mathcal L_{\epsilon,N}(a,b)
 &=\widehat P_N(Na)\widehat P_N(Nb)
   \sum_{j=0}^{N-1}
   \frac{e^{2\pi iaj}(r^{Na+1};r)_j(r^{Nb+1};r)_j}
        {(r;r)_j^{\,2+\epsilon}},\qquad r=e^{-2\pi i/N}.
 \end{split}
 \tag{1}
\]
Set
\[
 B_3=[.22,.50]+i[-.03,.02],\qquad
 B_4=[.22,.50]+i[-.057,.0141].
 \tag{2}
\]
The four families are \(a\in B_{3+\eta}\), \(b\in B_{3+\epsilon}\),
where \(\eta,\epsilon\in\{0,1\}\).

**Theorem 1.** On a neighborhood of each closed product (2), the
original equation \(Q_{\epsilon,s}=0\) has a unique holomorphic root
in \([.10,.49]+i[-.17,.17]\). For both parities the full original
source has the uniform packet
\[
 \mathcal L_{\epsilon,N}=
 N^{(1-\epsilon)/2}
 \frac{\sqrt{2\pi}A_\epsilon(s_*;a,b)}
      {\sqrt{-Q_{\epsilon,ss}(s_*;a,b)}}
 e^{NQ_\epsilon(s_*;a,b)}(1+O(N^{-1})).
 \tag{3}
\]
The symbol and Gaussian branch are the original nonzero ones. The
statement has every fixed order and all fixed derivatives on smaller
neighborhoods. For the literal Laurent kernel \(C_{\epsilon,N}\),
division by the two factorial interpolants gives phase
\(Q_\epsilon(s_*)-g(a)-g(b)\) and power \(N^{-(1+\epsilon)/2}\).

Here are the new certificate premises and their analytic reduction.
The [transition curvature majorant](research_mixed_transition_conditional_rectangles.md)
still gives \(-\Re Q_{ss}>1/8\) on
\([.10,.49]+i[-.20,.20]\). Its smallest shifted real argument remains
.32, its typed height intervals are unchanged, and every new shifted
argument lies below .99. Positive real cotangents decrease with their
real argument on the relevant positive interval; those beyond .50
are nonpositive. Thus enlarging both upper real endpoints to .50
does not enlarge that majorant.

The checker proves original pointing signs of magnitude \(>1/50\)
on the four faces with real endpoints .10,.49, upper height .15,
and lower height -.15 for \(\epsilon=0\), -.17 for \(\epsilon=1\).
There are sixteen faces and 2,048 exact slabs. Harmonic parameter
extrema are covered on all four sides of both rectangles.
Poincaré--Miranda and strict negative real derivative give existence,
uniqueness, simplicity and whole-product holomorphy before any
distinguished-boundary source argument.

The sixty-four parameter-side products have exact rational binary
covers. Their original logarithmic affine self-maps give
\[
 .20<\Re s_*<.46,\quad |\Im s_*|<.17,\quad
 \begin{cases}
 M-\Re Q(.10)>10^{-4},\\
 M-\Re Q(.49)>10^{-4},\\
 M-H_\epsilon(1)>10^{-4},\\
 M-\Re Q(x\pm .20i)+.40\pi>10^{-3},
                    &.10\le x\le.49,
 \end{cases}
 \tag{4}
\]
where \(M=\Re Q(s_*)\). All four periodic last-row branches are
included. The right-tail polynomial is below one up to its two
quadratic vertices, so the entire right real tail reduces to .49
and 1. On the left real tail, the shifted sine arguments lie in
\([.22,.60]\), and the unchanged bound
\[
 \Re Q_s(s)\ge
 2\log\frac{\sin(.22\pi)}{\sin(.10\pi)}-.08\pi>1
                         \qquad(0<s\le.10)
 \tag{5}
\]
applies. Each horizontal segment in (4) is bounded by its midpoint
concavity tangent, retaining the whole interval.

These checks are the exact contour premises of the right-guard proof:
both cotangent aliases, every half-grid vertical current and both
zero-mode joins are retained. Imaginary convexity controls the
connecting currents by their checked endpoint rates. Half-grid
rounding costs only a polynomial factor. The unchanged \(+N\)
cotangent coefficient, \(N^{-\epsilon/2}\) summand power and one
Gaussian give (3). Normalizing the error by its nonzero holomorphic
leading expression and applying the maximum principle twice extends
the boundary estimate over each whole product. The canonical finite
function in (1) is identical to the previous source; no revived row
or seam is discarded.

The source cover passed with 2,423 accepted cells and 3,822 visits.
The root faces are certified afresh; the unchanged curvature
certificate and its dependency bindings are validated as inputs.

## 2. Two simultaneous tilted directions

Use the original allocated phase and its full complex tangent plane
at an actual cyclic critical pair \(z^*=(a^*,b^*)\):
\[
 \begin{split}
 \phi(a,b)&=Q_\epsilon(s_*;a,b)
              -(1+\eta/2)g(a)-(1+\epsilon/2)g(b),\\
 \Gamma(z)&=\phi(z^*)+\phi_a(z^*)(a-a^*)+\phi_b(z^*)(b-b^*).
 \end{split}
 \tag{6}
\]
The actual reference enclosures are those in
[the one-taper theorem](research_mixed_right_taper_tilt.md), equation (3).
At the reference the original conditional root is the known inner
geometric coordinate, by the original logarithmic equations and
uniqueness in Theorem 1.

Each coordinate is independently of one of the following two forms:
\[
 z_j=y_j+i\Im z_j^*,\quad y_j\in[.22,.45],
 \qquad\text{or}\qquad
 z_j=t_j+400i(.5-t_j)^2\Im z_j^*,\quad t_j\in[.45,.50].
 \tag{7}
\]
At least one coordinate has the second form. Both are unselected.

**Theorem 2.** For every such product and every actual cyclic
reference, in all four type combinations,
\[
 \Re\phi(z)\le\Re\Gamma(z)
       -\frac{181}{24200}\|\Re(z-z^*)\|_2^2
       <\Re\Gamma(z)-\frac1{40000}.
 \tag{8}
\]
Consequently the full original allocated block has
\[
 |C_{\epsilon,N}(a,b)|\,|d_N(a)|^{\eta/2}|d_N(b)|^{\epsilon/2}
 \le\operatorname{poly}(N)
       \exp N\left(\Re\Gamma(z)-\frac1{80000}\right).
 \tag{9}
\]

The exact condensed Hessian \(H=-\phi''\), including both chirps and
half-factorial allocations, is (10)--(11) of the one-taper proof.
Put \(D=\operatorname{diag}(1+i\theta_a,1+i\theta_b)\).
For a coordinate of type three allow \(\theta\in[-.2,.3]\);
for type four allow \(\theta\in[0,.35]\).
The new outward certificate proves
\[
 \begin{split}
 \Re H_{11},\Re H_{22}&>1/100,\\
 \Re(D^THD)&>\tfrac{11}{100}I
       &&\text{if both real arguments lie in }[.22,.45],\\
 \Re(D^THD)&>-\tfrac7{20}I
       &&\text{if both lie in }[.22,.50].
 \end{split}
 \tag{10}
\]
The independent height intervals are \([-.03,.02]\) for each
type-three coordinate and \([-.057,0]\) for each type-four
coordinate. These larger products contain all straight segments
from the reference to (7).

For the four type choices and two real-square choices, all sixteen
parameter-side products are covered. At each original affine Newton
root enclosure, the four corners of the two-tilt rectangle satisfy
the positive diagonal and determinant tests for (10).
At each fixed tilt pair and real vector, the relevant quadratic
form is separately harmonic in the two complex parameters.
Theorem 1 supplies the whole-product holomorphic branch first;
two minimum principles then extend the boundary bounds to the
entire products.
As a function of either real tilt separately,
\[
 \partial_{\theta_j}^2\Re(D^THD)
       =-2\Re H_{jj}\,e_je_j^T\le0.
 \tag{11}
\]
Successive matrix concavity therefore extends the four tilt-corner
checks to all intermediate tilts, including zero for a plateau leg.
This is a complete 128-product cover, with 70,043 accepted cells and
138,038 visits; it does not sample the interior tilt parameters.

The type-dependent tilt bounds for a tapered leg are exactly the
rational inequalities (13)--(15) of the one-taper proof. A plateau
leg has tilt zero. Let \(v=\Re(z-z^*)\). On the straight segment
\(z^*+\lambda Dv\), let \(q\) be the length of the final part after
the first real coordinate reaches .45. For each tapered leg,
\[
 \frac{t_j-.45}{t_j-\Re z_j^*}\le\frac5{11},
 \qquad\text{hence}\qquad q\le\frac5{11}.
 \tag{12}
\]
Before that part both coordinates lie in the smaller square; after
it they remain in the larger one. The exact Taylor integral gives
\[
 \begin{split}
 \Re[\phi(z)-\Gamma(z)]
 &\le-\frac{\|v\|_2^2}{2}
    \left[\frac{11}{100}
      -\left(\frac{11}{100}+\frac7{20}\right)q^2\right]\\
 &\le-\frac{181}{24200}\|v\|_2^2.
 \end{split}
 \tag{13}
\]
At least one tapered leg has real displacement greater than .06,
and \(181(.06)^2/24200>1/40000\). This proves (8).
Pointwise concavity on the full larger square is not required.

For (9), Theorem 1 bounds the literal kernel with phase
\(Q_\epsilon(s_*)-g(a)-g(b)\). At every unselected four-type target
the height is nonpositive and the real part belongs to \((0,.5]\).
The true Fourier-polynomial bound, for any fixed tolerance
\(\delta>0\), has rate
\(\max\{-\Re g,0\}+\delta=-\Re g+\delta\).
The equality includes the seam .5, where both terms vanish.
The two allocated half-weights therefore cost at most \(\delta\).
Choosing \(\delta<1/80000\) proves (9); the forcing term has not
been replaced by a relative factorial approximation at its zero.
As in the one-taper theorem, derivative assertions concern only
the original holomorphic products with integer powers, using
small complex neighborhoods and Cauchy's inequality with a
slightly smaller strict gap.

## 3. A whole unaliased integration region

For a fixed cyclic word of length \(m\), let \(M=\Re\mathcal F_*\) be the real part of its original
critical action and let \(A_0\ne0\) be the coefficient in the
[central outer-integral theorem](research_mixed_central_outer_integral.md).
Use the exact periodic \(\chi_1\) graph from
[the right-half assembly](research_mixed_right_half_block_bound.md),
with no selected variables.

**Corollary 3.** The unaliased integral restricted to
\([.22,1]^m\) has the same central exponential and nonzero coefficient
as the central theorem.

Indeed partition each coordinate into the plateau \([.22,.45]\),
right taper \([.45,.5]\), and right half \([.5,1]\).
On the pure plateau box this is already proved. A box with a
right-half coordinate has an incident block with the right-half
gap \(1/2000\). Every other non-plateau block is either covered by
that theorem or by (9). A box without a right-half coordinate but
with a taper coordinate has at least one block covered by (9).
This statement remains literal for \(m=1,2\): blocks are counted
with their original incidences before identifying equal coordinates.

Plateau--plateau blocks are bounded by their own geometric tangent
planes, with an arbitrarily small per-block Fourier error
\(\delta_m\), by the plateau accretivity theorem. Choose
\[
                       0<\delta_m<\frac1{160000m}.
 \tag{14}
\]
The already fixed finite gaps of the other blocks do not consume
this tolerance. In the product, the allocated half-weights restore
the original integer Fourier powers, and all full complex linear
terms of the local planes cancel by the actual cyclic critical
equations. Thus every non-plateau box is bounded by
\[
                \operatorname{poly}(N)e^{N(M-1/160000)}.
 \tag{15}
\]
The graph Jacobian is bounded for this fixed word, and the finite
partition has only \(3^m\) boxes. The plateau contribution therefore
retains its original coefficient. No modified source or prepared
cycle is substituted.

The corollary concerns the unaliased part only. Coordinates in the
left region \([0,.22)\) and selected right-taper variables remain
outside this result. No full mixed-word asymptotic or knot statement
is inferred from it.

## 4. Reproduction

Run the source certificate before the Hessian certificate:

    python3 experiments/certify_mixed_right_square_conditional_packets.py --precision 256
    python3 experiments/certify_mixed_right_taper_products.py --precision 192

Both preserve original logarithmic branch tests, exact rational
binary covers and input immutability. The second validates the
first record and all its current proof/script/dependency bindings.
Completed right-guard and one-taper artifacts are not changed.
