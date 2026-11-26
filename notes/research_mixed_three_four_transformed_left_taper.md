# The complete retained-leg source on the left incoming taper

Research deduction, 7 November 2026. Fixing the outgoing boundary
removes the terminal private contour. The remaining conditional
polynomial still contains all its physical transform rows, including
rows that would terminate at a physical outgoing index. This note
retains those rows and proves a strict bound for the whole left taper.
No numerical evaluation is used.

## 1. Original source, normalization and reference

Let
\[
\begin{split}
 r&=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\\
 U_{0,N}(w,X)&=\sum_{j<N}H_N(w,r^{-j})p_j(X)/P_j,\\
 C_{1,N}(X,Y)&=\sum_{j<N}X^{-j}p_j(X)p_j(Y)/P_j^3.
\end{split}                                                     \tag{1}
\]
These are the literal polynomials of
[the inverse boundary transform](research_mixed_three_four_transformed_complement.md).
The retained-leg prefix is \(N\operatorname{CT}_X(U_0C_1)\),
before its final Gram contraction. We do not add a retained
halfweight or select a Fourier sector.

Keep the original ordinary pair reference and its saved consequences:
\[
\begin{split}
 a_*&=A+ic,\quad .278<A<.391,\quad -7/200<c<0,\\
 z_*&=E+iv,\quad .349<E<.350,\quad -137/4000<v<-1/30,\\
 M&=\Re\{T_0(a_*)+P_1(a_*)\},\\
 M&=\Re\mathcal P_{34}(-2,z_*)+\Re E_{\rm end}(z_*),\qquad
 \Re\mathcal P_{34}(-2,z_*)>181/100.
\end{split}                                                     \tag{2}
\]
The action and its additive constant are those in
[the transformed calibration](research_mixed_three_four_transformed_complement_calibration.md).
No new critical value is computed. Write
\[
 a(x)=x+ic(x-.1)/.12,\qquad X(x)=e^{-2\pi ia(x)},
                    \qquad .1\le x\le.22.               \tag{3}
\]

**Theorem 1.** On sufficiently small fixed neighborhoods of
\((w,z)=(-2,z_*)\), the entire product in (1) satisfies,
for every fixed \(k,\ell\),
\[
\sup_{.1\le x\le.22}
\left|\partial_w^k\partial_z^\ell
\left[e^{-N\mathcal P_{34}(w,z)}
 U_{0,N}(w,X(x))C_{1,N}(X(x),e^{-2\pi iz})\right]\right|
 \le C_{k,\ell}e^{-N/400000}.                           \tag{4}
\]
The same assertion holds for the original oriented contribution
\[
 N\int_{.1}^{.22}
    U_{0,N}(w,X(x))C_{1,N}(X(x),e^{-2\pi iz})a'(x)\,dx .
                                                               \tag{5}
\]
Both level parities and every finite transform index are included.
The theorem estimates this exact incoming segment, not a partial
root average.

## 2. The exact one-index interpolation

Define directly from the prescribed factorial interpolants
\[
 Q_N(t;a,z)=e^{2\pi iNat}
   \Pi_N(a+t)\Pi_N(z+t)E_N(a)E_N(t)^3E_N(z).
                                                               \tag{6}
\]
At every retained physical \(t=j/N\) in the regular factorial
chart, the factorial difference equation gives exactly
\[
 Q_N(j/N;a,z)=X^{-j}p_j(X)p_j(e^{-2\pi iz})/P_j^3.
                                                               \tag{7}
\]
It imposes no condition \(j+Nz<N\). We use this interpolation
only for the central rows; the outer physical rows below are
estimated in their literal finite-product form (1).
Its original phase is
\[
 Q(t;a,z)=g(a+t)+g(z+t)-3g(t)-g(a)-g(z)+2\pi iat.
                                                               \tag{8}
\]

For comparison with the previously calibrated terminal source, put
\[
 D_N(z)=\Delta_N(z)^{-1}C_N(z,-2),\qquad
 E_{\rm end}(z)=S(z)-\frac{\pi i}{2}(z-z^2).
                                                               \tag{9}
\]
The exact identity with equation (3) of
[the reduced-current theorem](research_mixed_terminal_four_reduced_currents.md)
is
\[
 \widehat{\mathcal J}_N(a;z,t,-2)=D_N(z)Q_N(t;a,z),
 \qquad \Phi(a;t,z)=E_{\rm end}(z)+Q(t;a,z).
                                                               \tag{10}
\]
The complete endpoint theorem makes \(D_N\) nonzero on a fixed
neighborhood of \(z_*\), for all sufficiently large \(N\), with
its original nonzero packet and fixed mixed derivatives.
Equation (10) is an identity of individual exact interpolants.
We never divide an estimate for the coherently summed terminal
polynomial \(V_1\).

For the central transform contour use the old real cuts \(.15,.5\)
and heights \(-.12,.12\). On the taper,
\(\Re(a+t)\in[.25,.72]\) and
\(\Re(z_*+t)\in(.499,.850)\). All marked factorial arguments
are therefore in the original regular strips. The exact
one-index residue identity has its original positive factor \(N\).
There are three unaliased currents, the horizontal line at the
actual height \(h_t=\Im t_*\in(-.108,-.020)\) and its two
joins, together with the six side/horizontal alias currents.
The original half-grid cut convention is retained.

## 3. Pointwise calibration of all central currents

The first factor is bounded as a whole by the complete cap envelope
used in [the ordinary left-taper completion](research_mixed_three_four_left_taper_source_completion.md),
Section 2. Its private aliases have already been paid against the
actual first private main height. The remaining regular profiles
and the true-index-end alternative are retained.

Every central estimate of Sections 3--4 of that completion is
pointwise on the right private main segment. The fixed value \(z_*\)
lies on that segment. In particular, no integration or maximization
over a replacement private coordinate is required here.
After applying (10), subtract the same constant
\(\Re E_{\rm end}(z_*)\) from each individual phase inequality.

Here is the full one-index ledger.

* On the actual transform height and both real cuts \(t=.15,.5\),
  the original fixed-cut incoming transport applies. Its coupled
  derivative for a regular first-cap profile with private coordinate
  \(e\) is
  \[
   \Re\{(1+ic/.12)
      [g'(e+a)+g'(t+a)-2g'(a)+2\pi it]\}.
                                                               \tag{11}
  \]
  The fixed \(z_*\) and its endpoint action do not occur in this
  derivative. The original theorem proves strict positivity for
  the regular profiles and nonnegativity for the cap true ends.
  It includes \(.15\le\Re t\le.5\), every nonpositive retained
  transform height, and the true endpoints of this interval.
* Lower aliases keep the same fixed sampling penalty and the same
  transport. The upper aliases use
  [the positive-alias theorem](research_mixed_three_four_left_positive_alias.md)
  with its original raw deficit \(1/125\). Its source inequality
  is also pointwise in the right private coordinate.
* At \(x=.22\), the cap profiles are below the original complete
  cap plane. The right phase has its original actual reference,
  so stationarity cancels the first marginals. The main horizontal
  loss is exactly the one in equation (9) of the ordinary taper
  completion:
  \[
   \text{coupled main rate}
   <\Re\mathcal P_{34}(-2,z_*)-\frac1{20000}.
                                                               \tag{12}
  \]
  Both flattened transform faces and the lower aliases retain
  at least that raw deficit by the original completed comparisons.

Only transform height now varies on the joins. At \(t=.15+i\eta\)
the old side inequality is
\[
 3\Re\cot\pi t-\Re\cot\pi(a+t)-\Re\cot\pi(z_*+t)>0.
                                                               \tag{13}
\]
It is precisely the side inequality in Section 4 of the ordinary
taper completion; at \(t=.5+i\eta\) the own real cotangent
vanishes and both shifted real cotangents are negative.
Thus the phase is convex in height on each side. A sampling
penalty is linear on either sign half of that height interval.
Every ordinary join and alias side therefore reduces to its
already controlled endpoints. All nine one-index currents are paid.
No convexity on a newly added small-transform rectangle is used.

Uniform finite-symbol bounds and the fixed half-grid displacements
turn these strict profile comparisons into bounds for the entire
central finite sum. The exact density (6), not an asymptotic
replacement, is used in the residue identity.

## 4. The entire lower physical sector

At real \(0<t<.15\), let
\[
 R=e^{-2\pi\Im a(x)}\ge1,\qquad k=e^{2\pi v}<1.
\]
The exact derivative of the absolute physical-row rate is
\[
 e^{\partial_t\Re Q(t;a(x),z_*)}
 =\frac{|R-e^{-2\pi i(x+t)}|\,
       |1-k e^{-2\pi i(E+t)}|}
       {(2\sin\pi t)^3}.                                \tag{14}
\]
For \(0<t\le.03\), \(x+t\in[.1,.25]\), and hence the first
factor is greater than \(3/5\): it is increasing in \(R\ge1\),
and \(2\sin(\pi/10)>3/5\).
The second factor exceeds one because
\(E+t\in(.349,.380)\), where the cosine is negative.
Also \(2\sin\pi t<.06\pi<1/5\). Thus the right side of
(14) exceeds \(75\).

For \(.03\le t\le.15\), the
[all-height low-transform force](research_mixed_three_four_left_low_transform_force.md)
gives \(\partial_t\Re Q>1/2000\); subtracting the fixed
endpoint phase in (10) does not change that derivative.
Consequently the entire lower absolute row rate is increasing
up to the original cut:
\[
 \Re Q(t;a(x),z_*)\le\Re Q(.15;a(x),z_*)
                         \quad(0\le t\le.15).           \tag{15}
\]
At \(t=0\) this uses the continuous limiting rate zero.
The uniform factorial estimates include the exact \(j=0\)
row and have only \(O(\log N)\) denominator loss there.
Therefore (15) bounds all lower physical rows, each multiplied
by the same complete first cap, by the pointwise paid \(.15\)
face of Section 3. No deleted private endpoint or Newton term
is needed for this reduction.

## 5. The revived upper physical sector

For real \(t\in[0,1]\) retain the exact absolute rate
\[
 \mathcal E(t;a,z)=I_a(t)+I_z(t)-3J(t)-2\pi\Im(a)t,\qquad
 I_a(t)=\int_0^t\log|1-e^{-2\pi i(a+u)}|\,du .
                                                               \tag{16}
\]
On the regular lower half it equals \(\Re Q\). The formula
(16), rather than a continuation across a chosen logarithmic cut,
is used for all upper physical rows.

The [asymmetric negative-height endpoint theorem](research_mixed_transformed_left_upper_rows.md)
applies to (2)--(3):
its inputs are
\[
 0\le\Re a\le2/5,\quad
 1/3\le\Re z_*\le11/30,\quad
 e^{2\pi\Im a}>4/5,\quad
 \Im a\le0,\quad\Im z_*<0.
                                                               \tag{17}
\]
It gives the complete upper-row comparison
\[
 \mathcal E(t;a(x),z_*)
 \le\max\{\mathcal E(.5;a(x),z_*),
                    \mathcal E(1;a(x),z_*)\},
                       \qquad .5\le t\le1.              \tag{18}
\]
The finite version retains every row of \(C_1\), including the
even half row and all rows revived by complex \(z_*\).

The first endpoint in (18) is the pointwise real transform face
already paid in Section 3. For the other endpoint, each numerator
radius is at most one, so its full-period logarithmic mean is zero:
\[
             \mathcal E(1;a(x),z_*)=-2\pi\Im a(x)<11/50.
                                                               \tag{19}
\]
At height zero the same identity holds with its integrable zero.
Use here the separate whole-disk cap estimate recorded in
[the transformed upper-row proof](research_mixed_transformed_upper_rows.md),
equation (14):
\[
 |U_{0,N}(w,X)|\le C_\tau N^{B_\tau}
             e^{N(433/500+1/3+\tau)},\qquad |X|\le1.
                                                               \tag{20}
\]
Its total with (19) is less than \(3/2\), strictly below
\(181/100\). The endpoint sum bound can be multiplied by the
same first cap and its two terms estimated separately by their
respective cap bounds. There is no comparison between two
different signed source values.

## 6. Exhaustion, neighborhoods and derivatives

Partition the original physical transform indices into
\(j/N<.15\), \(.15\le j/N<.5\), and \(j/N\ge.5\).
The first group is Section 4. The second uses the exact
one-index contour of Sections 2--3, with cuts halfway between
the adjacent indices. The third is Section 5. At even levels
the half row belongs to the last group; at odd levels the upper
central half-grid cut equals \(.5\). The actual lower cut is
within \(O(N^{-1})\) of \(.15\).
This is an exhaustive disjoint partition of all \(N\) rows.

The raw central, lower and half-row deficits are at least
\(1/20000\). The last-row deficit is much larger.
Allocate a common small tolerance to the exact coefficient bounds,
finite products, half-grid displacements, and parameter perturbations.
All relevant factorial domains have fixed margins. In the high
physical sector the numerator logarithms have uniform upper
Riemann bounds, including the integrable zero at the height-zero
incoming endpoint; the rate integrals are continuous uniformly on
the compact parameter sets. Thus a sufficiently small fixed
neighborhood of \(w=-2,z=z_*\) preserves a strict fraction of
all these gaps, including the original action calibration.

The total row count, exact residue factor \(N\), symbols and the
finite number of currents cost only powers of \(N\). Absorb those
powers from the strict reserve. The holomorphic normalized value
bound, followed by Cauchy's formula on a smaller fixed neighborhood,
proves (4) for all fixed mixed derivatives.
Finally \(a'(x)=1+ic/.12\) and the length in (5) are bounded;
the extra original factor \(N\) is polynomial. This proves (5).

This theorem does not identify the fixed outgoing coordinate with
an independently chosen ordinary reference. Its reference is the
original pair's actual private leg. It supplies one full source
piece of the transformed first path and preserves the subsequent
Gram, halfweight and two-sector observation as separate exact
operations.
