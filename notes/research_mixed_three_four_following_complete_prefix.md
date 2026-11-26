# The complete transformed prefix on the actual following family

Research assembly, 7 November 2026. The entire retained-leg
three/four polynomial has a nonzero asymptotic expansion at the
outgoing references selected by the four actual following
families. Every part of one incoming contour is included:
the real initial interval, left taper, central stationary
region, right interval, height connector and fixed complement.

The theorem concerns a complete finite polynomial and its original
absolute pre-Gram action. It does not evaluate a subsequent
Fourier coefficient or assert a new three/four/three,
three/four/four, or arbitrary short-filling knot theorem.

## 1. The literal finite polynomial and the selected action

Retain the original definitions
\[
 r=e^{-2\pi i/N},\qquad P_j=(r;r)_j,\qquad
 p_j(X)=(rX;r)_j ,
\]
and the complete finite sources
\[
 \begin{split}
 U_{0,N}(w,X)&=\sum_{j=0}^{N-1}
                     H_N(w,r^{-j})\,p_j(X)/P_j,\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}
                     X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 f_{34,N}(w,Y)&=N\operatorname{CT}_X
                       [U_{0,N}(w,X)C_{1,N}(X,Y)].
 \end{split}                                                   \tag{1}
\]
The last expression is a polynomial of degree less than \(N\)
in both \(w\) and \(Y\). All coherent coefficients, numerator
zeros, initially vanishing or revived rows, and both level
parities are retained.

The normalization is the exact inverse-boundary transform in
[transformed-complement Lemma 1](research_mixed_three_four_transformed_complement.md).
In particular the complete ordinary pair is recovered by
\[
 E_{34,N}(w,w_R)
  =\kappa_N^3N\sum_{b=0}^{N-1}
                 f_{34,N}(w,r^b)\,b_b(w_R),\qquad
                  b_b(w_R)=H_N(w_R,r^{-b})/P_b .
 \tag{2}
\]
Thus (1) has no extra \(\kappa_N\), no final Gram incidence
and no outgoing Fourier halfweight or selected sector.
Equation (2) still differentiates the original ordinary
polynomials when normals are observed.

Let \(K\) be any of \(O_3,O_4,A_3,A_4\). These are the
original compact typed domains in
[actual last-row references](research_mixed_actual_last_row_reference_domains.md).
For \(c\in K\), use the unique original-log cap-initialized
root
\[
          (u(c),e(c),a(c),p(c),q(c)).
 \tag{3}
\]
The [global following curve](research_mixed_three_four_following_critical_curve.md)
and [all-word pre-Gram theorem](research_mixed_arbitrary_prefix_pregram_curve.md)
give the holomorphic sheet, the univalent last leg \(q\), and
the absolute action
\[
 \begin{split}
 \mathscr P(c)&=H_{34}(c)-G(q(c),c),\\
 G(z,c)&=g(z+c)-2g(z)-2g(c)+2\pi izc .
 \end{split}                                                   \tag{4}
\]
The constant in (4) is the original stationary action constant;
it is not a new primitive or a post-Gram normalization.
On the actual family,
\[
 \begin{gathered}
 a(c)\in A_3,\qquad p(c),q(c)\in O_4,\qquad
                   (p(c),q(c))=F_4(a(c),c),\\
 .278\le\Re a\le.391,\quad -.072<\Im a<.021,\\
 .24\le\Re p,\Re q\le.36,\quad
                    -.102\le\Im p,\Im q\le-.001 .
 \end{gathered}                                                \tag{5}
\]
Their correlations are retained; the theorem is not asserted
on an independent containing box.

Locally in the ordinary color and outgoing coordinate, write
\[
 \begin{split}
 Q(t;a,z)&=g(a+t)+g(z+t)-3g(t)-g(a)-g(z)+2\pi iat,\\
 \psi(a,z)&=\operatorname{stat}_t Q(t;a,z),\\
 \mathcal P(w,z)&=\operatorname{stat}_a
                         [\mathcal T_0(a,w)+\psi(a,z)] .
 \end{split}                                                   \tag{6}
\]
The branches pass through \(a(c),p(c)\) at \(w=-2,z=q(c)\).
Exactly as in the following plateau theorem,
\[
                         \mathcal P(-2,q(c))=\mathscr P(c).
 \tag{7}
\]
The first-cap action already eliminates its original private
and endpoint variables. No endpoint action is silently removed
from or added to (6).

## 2. Seven oriented segments, with one fixed base

Fix \(c_0\in K\), and put \(h_0=\Im a(c_0)\),
\(z_0=q(c_0)\). Let \(h_{\rm pair}\) be the original
ordinary-pair height used by the proved complementary contour;
it is fixed, with \(-7/200<h_{\rm pair}<0\). Define the
following seven successive oriented segments:

| Segment | Path |
|---|---|
| \(\Gamma_0\) | the real interval \(0\longrightarrow .1\) |
| \(\Gamma_L^{c_0}\) | \(a_0(x)=x+ih_0(x-.1)/.12\), \(.1\le x\le.22\) |
| \(\Gamma_P^{c_0}\) | \(.22+ih_0\longrightarrow .45+ih_0\) |
| \(\Gamma_R^{c_0}\) | \(.45+ih_0\longrightarrow .5+ih_0\) |
| \(\Gamma_V^{c_0}\) | \(.5+ih_0\longrightarrow .5+ih_{\rm pair}\) |
| \(\Gamma_{+,v}\) | \(.5+ih_{\rm pair}\longrightarrow .5\) |
| \(\Gamma_{+,r}\) | the real interval \(.5\longrightarrow1\) |

The two last segments are exactly the fixed
\(\Gamma_+=\Gamma_{+,v}+\Gamma_{+,r}\) in the completed
following-remainder theorem. The connector \(\Gamma_V^{c_0}\)
may have either orientation or zero length. Possible geometric
overlaps remain oriented contour chains.

For every fixed \(N,w,Y\), the incoming integrand
\[
                 U_{0,N}(w,e^{-2\pi ia})
                      C_{1,N}(e^{-2\pi ia},Y)
 \tag{8}
\]
is entire and one-periodic in \(a\), since it is a finite
Laurent polynomial in \(e^{-2\pi ia}\). The integral over
the seven-segment chain equals the integral from zero to one.
The latter extracts exactly \(\operatorname{CT}_X\), in
the increasing incoming orientation. Thus, if every component
integral includes the factor \(N\),
\[
 f_{34,N}=I_{0,N}+I_{L,N}^{c_0}+I_{P,N}^{c_0}
                    +I_{R,N}^{c_0}+I_{V,N}^{c_0}+I_{+,N}.
 \tag{9}
\]
The last term is the sum of the two fixed complementary
segments, not a sampled-root sum. The taper includes its
actual differential \(da=a_0'(x)\,dx\).

Every path in (9) is held fixed at \(c_0\) while \(w,z\)
vary about \((-2,z_0)\). In particular, differentiating
(9) differentiates holomorphic integrals on fixed contours,
not the endpoints of a parameter-dependent contour.
Individual base decompositions need not agree term by term;
their complete sums always equal the same polynomial (1).

## 3. Bounds on the pieces of the contour

The following source estimates apply on the actual correlated
family in (5), or on the larger full following disks where
stated.

| Component | Complete source estimate |
|---|---|
| \(I_{0,N}\) | [Following remainder gaps](research_mixed_three_four_following_remainder_gaps.md): the exact initial interval, uniform on both full following disks |
| \(I_{L,N}^{c_0}\) | [Complete following left taper](research_mixed_three_four_following_left_taper_source.md), with its [all-real corollary](research_mixed_three_four_following_left_real_colors.md) |
| \(I_{P,N}^{c_0}\) | [Following plateau source](research_mixed_three_four_following_plateau_source.md): the nonzero whole plateau expansion and complete supporting plane |
| \(I_{R,N}^{c_0}\) | [Following right segment](research_mixed_three_four_following_right_segment.md): all physical rows, central currents and numerator-wall continuation |
| \(I_{V,N}^{c_0}\) | [Following connector gap](research_mixed_three_four_following_connector_gap.md): the exact height join from the base reference to the unchanged complementary path |
| \(I_{+,N}\) | [Following remainder gaps](research_mixed_three_four_following_remainder_gaps.md): the exact unchanged complementary contour |

All nonplateau entries have positive exponential gaps at the
complete-color action, uniformly on each actual \(K\), with
all-real ordinary-color estimates and fixed derivatives.
They also have fixed-base holomorphic estimates near
the complete color.
The left source, for example, has gap \(1/1000000000\);
no numerical minimum among the source gaps is needed.

In particular the connector theorem gives a uniform
\(\delta_V>0\) for the exact integral on \(\Gamma_V^{c_0}\),
with the whole source (8) and its factor \(N\):
\[
 \left|e^{-N\mathcal P(w,z)}I_{V,N}^{c_0}(w,z)\right|
       \le CN^B e^{-\delta_VN}
 \tag{10}
\]
on fixed sufficiently small neighborhoods of
\((-2,q(c_0))\), with all fixed normalized mixed derivatives
on smaller neighborhoods. For all real \(w=-2\cos\theta\),
the same source has a uniform positive gap when normalized by
\(e^{-N\mathscr P(c_0)}\) at \(z=q(c_0)\), with fixed
ordinary-color derivatives. One may take
\(\delta_V=\mu_J/4\), where \(\mu_J>0\) is the symbolic
uniform margin in that theorem; no numerical minimum is
needed here.

The connector estimate compares its complete finite-source
ceiling with the original action on the same holomorphic
following sheet. Its boundary certificate and maximum-principle
argument prove both required height guards and the strict gap
on the full reduced disks. Its fixed-base version is precisely
(10): the path is not silently changed when the outgoing
parameter varies. The certificate and its provenance are
recorded in the cited connector theorem.

## 4. The whole-prefix asymptotic expansion

**Theorem 1.** There is a fixed open neighborhood
\(\mathcal U_K\) of
\(\{(-2,q(c)):c\in K\}\), with nonzero holomorphic
\(\mathcal A_{34}\) and the selected holomorphic action
\(\mathcal P\), such that
\[
 f_{34,N}(w,e^{-2\pi iz})
 =N^{-3/2}\mathcal A_{34}(w,z)e^{N\mathcal P(w,z)}
                    (1+\varepsilon_N(w,z)),\qquad
               \varepsilon_N=O_{\rm hol}(N^{-1}).
 \tag{11}
\]
The estimate is uniform on closed smaller neighborhoods,
at both parities. Every fixed mixed derivative of
\(\varepsilon_N\) is \(O(N^{-1})\) there. One may choose
the constants and local neighborhood radii uniformly for all
four actual \(K\). This is a theorem near their actual
outgoing images \(q(K)\), not on all independently prescribed
ordinary type-four outputs.

*Proof.* At each base \(c_0\), intersect the finitely many
fixed parameter neighborhoods for (9). The exact plateau
integral has the whole-source expansion from the following
plateau theorem:
\[
 I_{P,N}^{c_0}(w,z)
 =N^{-3/2}\mathcal A_{34}(w,z)e^{N\mathcal P(w,z)}
                              (1+O_{\rm hol}(N^{-1})).
 \tag{12}
\]
Explicitly, writing \(a^\#\) for the original incoming
critical branch and \(\psi\) as in (6),
\[
 \mathcal A_{34}(w,z)=
 \frac{\sqrt{2\pi}\,
       \mathcal B_0(a^\#,w)\mathcal B_C(a^\#,z)}
 {\sqrt{-\partial_a^2[
          \mathcal T_0(a,w)+\psi(a,z)]_{a=a^\#}}}\ne0 .
 \tag{13}
\]
Here \(\mathcal B_0,\mathcal B_C\) are the symbols of
the complete cap and complete conditional expansions,
respectively. The square root is the original accretive
Gaussian branch. Its denominator is the Schur complement
of the full original pre-Gram Hessian; the principal block
and its eliminated block are invertible on the selected
family. The exact scaling is
\[
                   N\cdot N^{-1}\cdot N^{-1}\cdot N^{-1/2}
                                      =N^{-3/2}.
 \tag{14}
\]

Every other term in (9), including (10), is exponentially
smaller in the same absolute normalization. Their finite
number, bounded path lengths and original \(N\) cost only
polynomial factors. On a smaller neighborhood the symbol
in (13) has a positive lower modulus bound. Dividing the
sum of these remainder bounds by the nonzero leading
term therefore gives \(O(e^{-\delta N})\) for some
\(\delta>0\), with polynomial factors absorbed by reducing
the positive exponent. It adds to the plateau's holomorphic
\(O(N^{-1})\) relative error. This proves (11) locally.
Nested fixed-radius Cauchy estimates prove every fixed
mixed derivative assertion.

The action at \(w=-2\) is the single global pre-Gram
function on \(q(\Omega)\) from the all-word theorem,
restricted here to \(q(K)\). The critical coordinates
are holomorphic functions on that selected sheet.
Uniform implicit-function neighborhoods of their compact
graph extend them for \(w\) near \(-2\); uniqueness near
that graph identifies these extensions on overlaps.
The original constants, roots and Gaussian branches
therefore identify (6) and (13) on those overlaps.
Compactness and a finite subcover give a fixed
\(\mathcal U_K\) and uniform constants.
No component integral from one fixed-base path is
substituted for a component integral from another.
\(\square\)

In particular, on every compact subset of a smaller
\(\mathcal U_K\), all sufficiently large levels satisfy
\[
 \tfrac12 N^{-3/2}|\mathcal A_{34}|e^{N\Re\mathcal P}
 \le |f_{34,N}(w,e^{-2\pi iz})|
 \le\tfrac32 N^{-3/2}|\mathcal A_{34}|e^{N\Re\mathcal P}.
 \tag{15}
\]
This lower bound follows from the nonzero coefficient and
control of every other contribution to the exact finite
source.

## 5. All-real angular loss and derivatives

**Theorem 2.** There is \(c_*>0\), uniform over
the actual following families, such that
\[
 |f_{34,N}(-2\cos\theta,e^{-2\pi iq(c)})|
 \le CN^B e^{N\{\Re\mathscr P(c)-c_*(1-\cos\theta)\}},
 \qquad c\in K,\quad -\pi\le\theta\le\pi .
 \tag{16}
\]
Every fixed ordinary-color derivative satisfies the same
rate with an appropriate polynomial prefactor.

*Proof.* The all-real cap plane supplies the plateau with
some uniform angular loss \(c_P(1-\cos\theta)\).
The precise polynomial-exponent source argument is given in
[the all-real left corollary, Section 4](research_mixed_three_four_following_left_real_colors.md):
keep the regular ordinary main density at its exact plane
and spend a fixed tolerance only inside the strict
nonprincipal gaps. Thus no fixed positive tolerance is
left in the plateau angular exponent.

By the bounds in Section 3, the sum of all other exact components
has a uniform complete-color gap \(\delta>0\) for all
real colors. Consequently their sum with the plateau
has deficit at least
\[
 \min\{c_P D,\delta\}\ge
       \min\{c_P,\delta/2\}D,\qquad D=1-\cos\theta\le2 .
 \tag{17}
\]
This proves (16) with \(c_*=\min(c_P,\delta/2)\), after
decreasing common constants if needed. The phase
\(\mathscr P(c)\) is held at complete color in this
estimate; no remote color-dependent saddle is postulated.

For the ordinary derivatives, the normalized finite
polynomial has degree less than \(N\) in \(w\).
The angular Laurent-polynomial maximum-principle argument
of endpoint real-color decay turns (16) into a bound on
ordinary-color circles of radius \(N^{-2}\), uniformly
including the two quadratic angle branch points.
Cauchy's formula then has polynomial cost while changing
the logarithmic exponent by only \(O(1)\). Equivalently,
use the existing angular derivative estimate on the
plateau and spend part of each regional gap after applying
Markov's inequality to its full source. No finite zero
is divided. \(\square\)

The mixed holomorphic derivative statement in Theorem 1
and the all-real ordinary derivative statement in
Theorem 2 are distinct. The former concerns the fixed
selected outgoing neighborhoods and the relative error;
the latter is a global real-color upper estimate at the
complete-color action. No uncontrolled complex-color
asymptotic expansion is inferred far from the complete color.

## 6. Consistency with the earlier isolated pair

The earlier
[complete transformed-prefix theorem](research_mixed_three_four_complete_transformed_prefix.md)
proves an asymptotic expansion for the very same polynomial (1), near
the original ordinary pair's right private coordinate.
That coordinate is not assumed here to belong to \(q(K)\).
Conversely, membership in an independent containing
type-four box is not used to transfer the earlier expansion
to the new references.

Both theorems use precisely the action formula (6),
with the same first-cap action, primitive and chirp.
At the old isolated pair the removed right endpoint
action satisfies the exact split
\[
        \mathcal A_{\rm pair}
          =\mathcal P_{\rm pair}(z_{\rm pair})
                              +E_{\rm end}(z_{\rm pair}),
 \tag{18}
\]
as checked in
[transformed-complement calibration](research_mixed_three_four_transformed_complement_calibration.md).
The following-family formula (4) instead removes the
explicit final Gram term from the original cap-initialized
action. These are their two stated closures; neither is
substituted for the other.

Whenever the two local descriptions are compared on a
common continuation of the selected critical branch,
their absolute actions and symbols agree by (6) and
(13), and their finite source is exactly (1). There is
no new \(\kappa_N\), power of \(N\), alternating gauge,
or lost normal adapter. Formula (2) remains the original
ordinary reconstruction.

The result provides a complete
retained-leg prefix on the actual outgoing sets \(q(K)\).
The next transfer still includes its final Gram incidence
and both type-four factors \(d_N(Y)(1+Y^{-N})\).
Its exact coefficient observation, noncancellation and
source control require their own proof. No three-letter
knot or arbitrary short-cluster conclusion is asserted.
