# Cancellation of the real boundary force after the first collar

Research proof, 5 November 2026. The horizontal completion previously
left a scalar force at the second coordinate. That force is paid on
the already admitted source domain: the original first-pair lower
bound is uniform in the second real coordinate, and concavity places
it below the original tangent line. The next part of the chain has
the opposite tangent. This removes the extra scalar inequality from
the completion theorem. It does not enlarge the domain on which
the complete finite-source estimates have been proved.

## 1. The comparison and its hypotheses

Use the complete-color open reference \(r_j=a_j+ic_j\), fixed
cut at position \(h\ge3\), and compact horizontal domain
\(\mathcal D\) of the
[horizontal completion theorem](research_mixed_first_collar_horizontal_completion.md),
Section 1. In particular, the segment from the reference to each
target belongs to that domain. The complete conditional factors on
edges \(3,\ldots,h\) have their stated source upper bounds;
their original critical branches and all three arguments stay in
the common Hessian rectangle. Edge three also has the stated fixed
contour, tail and additional-frequency bounds required for the full
height transport.

The first coordinate is in its real collar \([0,\rho]\). All
coordinates from three to the fixed cut are unselected, with their
reference heights. The second coordinate has either its unselected
height between \(c_2\) and zero, or, for type four, its selected
height in \([0,.014]\). Its horizontal comparison target is
\(y_2+ic_2\), before that height transport. The existing domain
requires
\[
 y_2\in I_3=[.267,.433]\quad\hbox{for type three},\qquad
 y_2\in I_4=[.24,.363]\quad\hbox{for type four}.
 \tag{1}
\]
Endpoints in (1) cause no problem for the phase comparisons below.
The complete-source hypotheses are still imposed only where the
cited theorem supplies them; (1) by itself is not a source theorem.

Write the first two types as \(3+\alpha,3+\beta\), with
\(\alpha,\beta\in\{0,1\}\), and put
\[
 \begin{split}
 F(y)&=\Re\{\mathcal T_\alpha(r_1,-2)
              +\phi_{0\beta}(r_1,y+ic_2)-\alpha g(r_1)\},\\
 M_{12}&=F(a_2),\qquad p=F'(a_2)=\Re P_2.
 \end{split}
 \tag{2}
\]
Here \(\mathcal T_\alpha\) is the complete cap phase,
\(g\) is the original logarithmic-factorial primitive, and
\(\phi_{0\beta}\) is the original conditional critical phase
with one half of the second Fourier weight. Thus (2) retains the
full first weight and exactly the first half of the second weight.
The actual first reference \(r_1\) stays fixed throughout this
comparison. It is not replaced by a critical point for the new
second target.

## 2. Concavity supplies the missing tangent bound

**Lemma 1.** The original branch in (2) exists throughout the
appropriate interval (1), is strictly horizontally concave, and satisfies
\[
                         F(y)\le M_{12}+p(y-a_2).
 \tag{3}
\]

*Proof.* The actual first-coordinate rectangles are
\[
 \begin{array}{c|cc}
 \alpha&\Re r_1&\Im r_1\\\hline
 0&(.278,.391)&(-.072,.021)\\
 1&(.246,.350)&(-.108,-.020).
 \end{array}
 \tag{4}
\]
The second coordinate is ordinary because \(h\ge3\). Its
actual height lies in \((-.065,.068)\) for type three or
\((-.102,-.001)\) for type four. These are the domains already
used in the complete vertical transport estimates.

For a three-three pair, both outer cotangents belong to the
[closed half-square chamber](research_mixed_closed_cotangent_roots.md),
uniformly for every \(y\in I_3\). For a four-three pair,
the first cotangent has positive imaginary part less than \(.61\)
and the second has imaginary modulus less than \(.37\). The
[asymmetric quadratic chamber](research_mixed_four_three_cap_collar.md),
Lemma 1, therefore applies, since
\[
                  .61+.37+(.61-.37)^2/4=1243/1250<1.
 \tag{5}
\]
For either pair ending in four, the first cotangent has imaginary
part between \(-1\) and \(2/3\), and the second between
zero and \(.61\). The
[one-sided cubic chamber](research_mixed_second_four_cap_collar.md),
Lemma 1, applies throughout \(I_4\). In every case both
outer cotangents have positive real part. Uniqueness identifies these
branches with the actual reference branch and preserves its original
logarithmic lift along the horizontal segment.

All these chambers have the same positive triangle forms. If the
conditional cotangent is \(u+iv\) and an outer cotangent is
\(q+i\gamma\), their determinant is
\[
 \frac{(u+q)^2-(qv-u\gamma)^2}{(u+q)^2+(v+\gamma)^2}>0,
 \qquad u,q>0,\quad |v|,|\gamma|<1.
 \tag{6}
\]
The diagonal entries are positive as well. The additional factorial
terms have nonnegative real diagonal coefficients. Taking the complex
Schur complement gives \(-\Re\phi_{0\beta}''>0\), exactly
as in Section 3 of the closed chamber proof. This also establishes
the curvature assertion for the asymmetric quadratic chamber; no
half-square restriction is needed for (6). Consequently \(F''<0\).
Its tangent at \(a_2\) lies above its graph, proving (3).
\(\square\)

This argument uses a phase branch at the comparison points. It does
not require an asymptotic expansion of the first conditional finite
sum at those points: that sum will be bounded by its full absolute
row estimate instead.

## 3. The lower bound is uniform in the comparison coordinate

Put \(t=\Im r_1\), \(c=c_2\), and \(x_+=\max(x,0)\).
The existing phase estimates give the following lower bounds for
every \(y\) in (1):
\[
 \begin{array}{c|c}
 (\alpha,\beta)&F(y)>L_{\alpha\beta}\\\hline
 (0,0)&1+11/25-(\pi/2)\{t_++(-c)_+\}\\
 (1,0)&1+11/25-(\pi/2)(-c)_+\\
 (0,1),(1,1)&17/10-(\pi/2)\{t_++(63/50)(-c)\}.
 \end{array}
 \tag{7}
\]
In the last row \(c<0\), and \(t_+=0\) for \(\alpha=1\).

Here is why the previous estimates give (7) uniformly, rather than
only at the reference. For the pairs ending in three, the real phase
is greater than \(11/25\) throughout the six-vertex convex
region in the
[three-three comparison](research_mixed_three_cap_collar_comparison.md),
Section 2. Both rectangles formed by (4) and \(I_3\) lie
in that region. Its vertical comparison gives the first row of (7).
For a first type four, lowering its negative first height increases
the conditional phase, as proved in the
[four-three comparison](research_mixed_four_three_cap_collar.md),
Section 3; this removes \(t_+\), which is already zero.
For the pairs ending in four, the real phase is greater than
\(7/10\) on the whole rectangle
\([.246,.391]\times[.24,.363]\). The vertical supporting
bound in the ending-four proof is
\[
 \Re\phi_{01}(r_1,y+ic)
 >7/10-(\pi/2)\{t_++(3/2-y)(-c)\}.
 \tag{8}
\]
Since \(y\ge.24\), replacing \(3/2-y\) by \(63/50\)
gives (7).

Finally, the complete cap has \(\Re\mathcal T_\alpha(r_1,-2)>1\)
at the unchanged actual first reference. If \(\alpha=1\),
the retained contribution \(-\Re g(r_1)\) is positive. These
are the same cap and weight estimates used in the previous pair
comparisons. No cap theorem is extended to a new first coordinate.

Combining (3) and (7) now gives the bound that was lost when the
pair was replaced by its reference value alone:
\[
                      M_{12}+p(y-a_2)>L_{\alpha\beta}
                      \quad(y\in I_{3+\beta}).
 \tag{9}
\]

## 4. The complete finite source fits below this tangent

Let \(\mathcal B_N\) denote the modulus of the first cap and
first conditional factor, with the full first Fourier weight and
one half of the second, as in (11) of the
[angle-profile note](research_mixed_first_collar_angle_profiles.md),
but retaining the selected second halfweight when \(\beta=1\).
Let \(U_{\alpha\beta}(k)\) be the old angle-independent
upper rate before the one final tolerance. These are bounds for all
original finite rows:
\[
 \begin{split}
 U_{\alpha0}(k)&=b_\alpha+M_0(2\pi k_+)+C_\alpha(\rho),\\
 U_{\alpha1}(k)&=b_\alpha+.57+C_\alpha(\rho),\\
 b_0&=.808,\qquad b_1=.866,\qquad
 C_\alpha(\rho)=2\Delta_\rho+\alpha\omega(\rho).
 \end{split}
 \tag{10}
\]
The functions \(M_0\), \(\Delta_\rho\), and
\(\omega(\rho)\) are those in the pair proofs. The second
bound covers both selections, using the original polynomial on both
sides of the unit circle. It includes the second halfweight once.

The next conditional source has the complete vertical allowances
\[
 A_0(c,k)=
 \begin{cases}0,&c\le k\le0,\\\pi(c-k),&0\le k\le c,
 \end{cases}
 \qquad A_1(c,k)=13/2000.
 \tag{11}
\]
For type four the second allowance covers both height choices.
These are the proved
[type-three transport](research_mixed_three_first_source_transport.md)
and [type-four fixed-contour transport](research_mixed_four_fixed_contour_transport.md)
applied on the unchanged source domain of Section 1.

Choose the fixed collar to satisfy the previous pair requirements;
one may further decrease it so that \(C_1(\rho)<1/200\).
The previous numerical budgets, before the final finite-source and
ordinary-color tolerance, give
\[
 U_{\alpha\beta}(k)+A_\beta(c,k)
       <L_{\alpha\beta}-\delta_{\alpha\beta},\qquad
 \begin{array}{c|cccc}
 (\alpha,\beta)&(0,0)&(1,0)&(0,1)&(1,1)\\\hline
 \delta_{\alpha\beta}&3/100&3/125&87/2000&87/2000.
 \end{array}
 \tag{12}
\]
For the first two entries, these are precisely the scalar comparisons
in Section 3 of the
[type-three height comparison](research_mixed_three_first_vertical_phase.md):
\(M_0(2\pi k_+)+(\pi/2)(-c)_++A_0(c,k)\) is bounded
by \(.326+.073\pi\) or \(.326+.068\pi\), respectively.
For the last two, the ending-four proof has reserve greater than
\(3/50\) before the collar cost. Retaining a conservative
\(1/20\) and paying \(13/2000\) leaves \(87/2000\).
Thus no new scalar computation or root cover is needed for (12).

Equations (9) and (12) prove the uniform calibrated bound
\[
 U_{\alpha\beta}(k)+A_\beta(c,k)
   <M_{12}+p(y_2-a_2)-\delta_{\alpha\beta}.
 \tag{13}
\]
It covers the full permitted second real interval, not just a small
neighborhood of its reference. The tangent here is the horizontal
tangent at the original height. The entire physical height change
has already been paid in (11); it is not charged a second time.

## 5. Completion along the chain

Define
\[
 \Psi_h(y)=\sum_{j=3}^{h}
  \phi_{\epsilon_{j-1},\epsilon_j}
       (y_{j-1}+ic_{j-1},y_j+ic_j),\qquad y_h=a_h,
 \tag{14}
\]
where \(\epsilon_j\) is zero or one according to the type.
All its arguments are the horizontal comparison targets. Its weights
contain the other half of the second weight, the full subsequent
internal weights, and one half at the fixed cut. Set
\(M_h=M_{12}+\Re\Psi_h(a)\).

The source and Hessian hypotheses of Section 1 give, as proved in
the horizontal completion theorem,
\[
 \Re\Psi_h(y)-\Re\Psi_h(a)
 \le-p(y_2-a_2)-\frac\pi{16}
                  \sum_{j=2}^{h-1}(y_j-a_j)^2.
 \tag{15}
\]
The first term is fixed by original stationarity at position two;
all later free-coordinate tangents cancel between their incidences.

**Theorem 2.** On the complete-source domain of Section 1, the
literal first-collar product through the fixed cut satisfies, for any
prescribed total tolerance \(\eta>0\),
\[
 |\mathcal P_N|
 \le C_\eta N^B
 \exp\!\left[N\left\{M_h-\delta_{\alpha\beta}
       -\frac\pi{16}\sum_{j=2}^{h-1}(y_j-a_j)^2+\eta\right\}\right].
 \tag{16}
\]
Here \(\mathcal P_N\) consists of the first cap, all conditional
factors through the cut, and exactly the weights just specified.
The word and the cut are fixed. Constants and the ordinary-color
neighborhood may depend on them. Both integer parities, all allowed
first and second selections, and fixed ordinary-color derivatives
on a smaller neighborhood are included.

*Proof.* The complete finite-source upper rate is at most
\(U_{\alpha\beta}(k)+A_\beta(c,k)+\Re\Psi_h(y)+\eta\).
Insert (13) and (15). The two linear terms cancel. Apply the one
total tolerance after combining the factors. This proves (16).
\(\square\)

Since every \(\delta_{\alpha\beta}\ge3/125\), choosing
\(\eta<1/250\) leaves a common finite exponential loss
\(1/50\), in addition to the displayed quadratic loss.

There is no remaining boundary-force inequality on this domain.
The additional first-wire hypothesis and scalar criterion of the
[retained-energy estimate](research_mixed_horizontal_boundary_energy.md)
are unnecessary for this conclusion. Those estimates remain valid
and may be useful on other domains. The outstanding issue here is
the complete-source domain itself: the independent plateau and the
remaining contour pieces are not covered by (16). The conditions
on later unselected coordinates and the fixed cut also remain.
Consequently this theorem does not yet yield the full open-knot
contraction or stability under arbitrary short partial fillings.
