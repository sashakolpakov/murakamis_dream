# Two consequences of the small-parameter source bounds

Research proof, 4 November 2026. The first consequence removes the
entire all-small box from the remaining outer integral, uniformly
through its zero faces. The second pays for the two neighboring height
changes around one isolated small real coordinate, with its two
exterior arguments held fixed. Neither evaluates the whole period.

## 1. The all-small box in every cyclic word

Fix a cyclic word of length \(m\ge1\), whose types are
\(3+\epsilon_j\), \(\epsilon_j\in\{0,1\}\). Let
\(r_j\) be its original complex geometric critical coordinates and put
\[
 \Psi(z)=\sum_{j=1}^m
      \phi_{\epsilon_{j-1},\epsilon_j}(z_{j-1},z_j),
 \qquad M=\Re\Psi(r),\qquad \Psi'(r)=0.                 \tag{1}
\]
The phase \(\phi\), reference rectangles and original zero logarithmic
lifts are those of the
[both-low source bound](research_mixed_both_low_raw_support.md).
Subscripts are cyclic and repeated incidences are retained.

For each original Fourier selection \(S\), use its already defined
independent quadratic graph: in the interval \([0,.10]\), an
unselected coordinate has height
\(\Im r_j(x_j/.22)^2\), while a selected four-type coordinate has
height \(.014(x_j/.22)^2\). These graphs are pieces of the complete
periodic contours, not independently closed pieces of contour.

**Theorem 1.** The contribution of \([0,.10]^m\) on each such graph
has absolute value at most
\[
                 C_m N^{A_m}\exp N(M-m/100).                \tag{2}
\]
The same holds after summing all original Fourier selections, with a
different constant. All integer levels, zero faces and cyclic lengths
one and two are covered.

To prove this, write \(\Gamma_j\) for the complex tangent plane of
the \(j\)-th block at \((r_{j-1},r_j)\). Every block has both target
real parts in \([0,.10]\), with permitted heights. Its complete
allocated finite modulus is at most a polynomial times
\(\exp N(\Re\Gamma_j-1/100)\), by the both-low theorem. The
half-weights at each outer variable recombine into exactly one
original Fourier weight, including its selected factor when present.
Multiplication therefore bounds the literal cyclic finite density.

The tangent terms cancel exactly:
\[
 \sum_j\Gamma_j(z_{j-1},z_j)
       =\Psi(r)+\sum_j\Psi_j(r)(z_j-r_j)=\Psi(r).           \tag{3}
\]
This is the original logarithmic stationarity equation, not merely
an exponentiated gluing equation. At lengths one and two, differentiating
the repeated arguments gives exactly the same incidence counts.
The graph derivative, its integration volume, the original carrier
and level powers, and the finitely many selections cost at most a
fixed polynomial in \(N\). In particular
\(\kappa_N=q^{(N-1)^2/2}\) has modulus one. Equation (2) follows
for all sufficiently large levels; enlarging \(C_m\) covers the
finitely many remaining levels. The estimate concerns
the integral over this part of an already deformed full period, so it
introduces no new joining contours.

Together with the earlier theorem on \([.22,1]^m\), this leaves a
remainder contained in configurations with some coordinate below .22
and some coordinate above .10. It does not estimate those mixed
configurations.

## 2. Four blocks around an isolated real coordinate

Take five independent typed reference points \(r_0,\ldots,r_4\)
in their respective \(R_3,R_4\) rectangles. For \(j=1,\ldots,4\),
let \(\phi_j\) be the allocated phase of the block with arguments
\((z_{j-1},z_j)\), and \(\Gamma_j\) its plane at
\((r_{j-1},r_j)\). Put
\[
 z_0=r_0,\qquad z_1=x_1,\qquad z_2=t,\qquad
 z_3=x_3,\qquad z_4=r_4,
 \quad 0<t\le.10,\quad .22\le x_1,x_3\le.50.             \tag{4}
\]
Thus the central coordinate and its two neighbors are real, while
the two exterior arguments have not moved from their references.

**Theorem 2.** For every one of the 32 possible type strings,
\[
 \Re\sum_{j=1}^4\{\phi_j(z_{j-1},z_j)
                   -\Gamma_j(z_{j-1},z_j)\}<-3/50.          \tag{5}
\]
On every compact range \(\delta\le t\le.10\), the product of
the four complete allocated finite blocks is at most
\[
 C_\delta N^A
 \exp N\left\{\Re\sum_{j=1}^4\Gamma_j(z_{j-1},z_j)-1/20\right\}.
                                                               \tag{6}
\]
Original selections are allowed at the four-type real internal
variables; their factors have modulus one. The exterior complex
variables are unselected.

Blocks 2 and 3 have one small real argument. The
[one-small real comparison](research_mixed_real_one_small_support.md)
gives phase loss \(11/200\) for each. The phase inequality also
holds at \(x_1=.5\) or \(x_3=.5\): its affine certificate already
bounds those endpoints, and the selected root and phase extend
continuously there by the
[half-endpoint theorem](research_mixed_half_endpoint_conditional_packet.md).
For the finite upper bound, use that theorem's uniform nonzero packet
on \([\delta,.10]\times[.22,.5]\), and the original Fourier upper
rate at the half endpoint. Its rate is zero there. This justifies the
same smaller loss \(1/20\), without assuming a relative Fourier
asymptotic at the endpoint.

Blocks 1 and 4 have one argument fixed at its reference. The
[single-height reset theorem](research_mixed_single_height_reset.md)
charges at most \(7(\Im r_1)^2\) and \(7(\Im r_3)^2\).
Consequently the total phase defect is at most
\[
 14(.057)^2-2\frac{11}{200}
       =-.064514<-3/50.                                    \tag{7}
\]
For the finite blocks, use their losses \(1/20\) and give each
reset block an additional exponential tolerance \(1/1000\).
The resulting defect is at most
\[
 14(.057)^2+\frac2{1000}-\frac2{20}
        =-.052514<-1/20.                                   \tag{8}
\]
This proves (6). All remaining scalar factors are uniformly polynomial
on the stated compact target range.

The restriction \(z_0=r_0,z_4=r_4\) is essential to the reset-cost
input used here. Theorem 2 is not an estimate on a general outer box
in which the exterior real coordinates also move. It also supplies no
uniform one-small estimate at \(t=0\). A whole-word assembly must
address those two issues and the intervening interval \((.10,.22)\).
