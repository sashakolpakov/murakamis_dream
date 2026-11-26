# A selected small-activity saddle of the actual factorial coupon

Private written proof, 18 November 2026.

The residual last-head coupon in U has an actual nonzero complex
asymptotic on a small open sector. Its finite polynomial is represented
by its original constant-term circle. A direct Taylor-cap estimate and
a single saddle on that circle give the coefficient, including the
binomial half-density. No complex occupation interpolation or assumed
saddle occurrence is used.

This evaluates the coupon factor only. Its convolution with the
quotient, turnover, resolvent, and original source remains as in U.
In particular it does not select a geometric contribution to that
larger period.

The sole complete direct U is pinned below. It identifies the actual
coupon and its source interfaces. All finite recurrences, contour
identities, estimates, and saddle calculations are proved here.

## 1. The literal polynomial, including its top row

Set
\[
 N\ge2,\quad d=N-1,\quad c_0=2\pi i,\quad
 Q=e^{c_0/N},\quad f_a=\prod_{j=1}^a(1-Q^j),\quad f_0=1.
 \tag{1}
\]
U's retained coupon is \(ZG^{-1}\), where
\(Zw_a=(-1)^aw_a\) and \(Gw_a=f_aw_a\).
In the original binomial coherent convention its exact kernel is
\[
 \boxed{\quad
 H_N(s)=\sum_{a=0}^d\binom da\frac{(-s)^a}{f_a},
                  \qquad s=wz.
 \quad}\tag{2}
\]
There is no omitted overall factor in (2). The factors outside this
coupon in U's opposite-source interface remain outside it.

Let \(D_s=s\partial_s\) and \(\mathcal Q_sH(s)=H(Qs)\).
Consecutive coefficients in (2) give
\[
 \boxed{\quad
 [D_s(1-\mathcal Q_s)+s(d-D_s)]H_N=0,\qquad H_N(0)=1 .
 \quad}\tag{3}
\]
Indeed, for \(1\le a\le d\),
\(a(1-Q^a)h_a=-(N-a)h_{a-1}\).
The potential degree-\(N\) term on the right also vanishes:
\(d-D_s\) kills the degree-\(d\) coefficient. Thus the physical
upper endpoint has been used, not deleted.

The associated exponentiated principal row, with
\(H_N\) formally proportional to \(e^{N\Psi(s)}\) and
\(y=s\Psi'(s)\), is
\[
                    y(1-e^{c_0y})+s(1-y)=0.
 \tag{4}
\]
It includes the whole component \(y=1\), for every \(s\).
We will not divide this component out. The actual contour analysis
below selects a small branch \(y\sim\sqrt{s/c_0}\), away from it.

## 2. An exact circle and a controlled finite Euler cap

Define the finite polynomial
\[
 E_N(t)=\sum_{a=0}^d\frac{t^a}{f_a}.
\]
Its exact coefficient recurrence is
\[
 E_N(Qt)=(1-t)E_N(t)+\frac{t^N}{N},
                  \qquad f_d=N.
 \tag{5}
\]
Consequently the original coupon has the exact constant-term period
\[
 \boxed{\quad
 H_N(s)=\frac1{2\pi i}\oint
           (1+z)^d E_N(-s/z)\,\frac{dz}{z}.
 \quad}\tag{6}
\]
Any positively oriented circle about zero gives the same value.
This is a finite Laurent-polynomial identity. In particular the
forcing and finite cap in (5) are still present.

We next prove a local relative approximation for this actual
finite \(E_N\). Put
\[
 L_N(t)=\sum_{j=1}^{N-1}\frac{t^j}{j(1-Q^j)},\qquad P_N(t)=e^{L_N(t)}.
 \tag{7}
\]
The degree-\(d\) Taylor polynomial of \(P_N\) is exactly \(E_N\).
To see this, the coefficients below degree \(N\) in
\[
 L_N(Qt)-L_N(t)=-\sum_{j=1}^{N-1}t^j/j
\]
equal those of \(\log(1-t)\).
Hence \(P_N(Qt)=(1-t)P_N(t)+O(t^N)\) as formal series.
Its constant coefficient is one, and the recurrence determines
its next \(N-1\) coefficients to be \(1/f_a\).

For \(1\le j<N\),
\[
                  |1-Q^j|\ge4\min(j,N-j)/N.
 \tag{8}
\]
It follows that, for \(0<R\le1/4\),
\[
                       \sup_{|t|\le R}|L_N(t)|\le CNR
 \tag{9}
\]
with an absolute constant \(C\).
For \(j\le N/2\), sum \(NR^j/(4j^2)\).
For \(j>N/2\), the bound from (8) is at most a constant times
\(NR^{N/2}\sum_{k\le N/2}1/k\), which is bounded by \(CNR\)
uniformly in \(N\). This proves (9).

Choose a sufficiently small fixed \(\rho>0\), and apply Cauchy's
coefficient estimate on \(|t|=2\rho\). Since \(E_N\) is the exact
Taylor cap,
\[
 \sup_{|t|\le\rho}|E_N(t)-P_N(t)|
                     \le2^{1-N}e^{2CN\rho},
 \qquad
 \inf_{|t|\le\rho}|P_N(t)|\ge e^{-CN\rho}.
\]
Taking \(\rho\) so that \(3C\rho<\frac12\log2\) gives
\[
 \boxed{\quad E_N(t)=P_N(t)(1+O(e^{-\delta N})),\quad |t|\le\rho,
 \quad}\tag{10}
\]
for some \(\delta>0\). This is a relative estimate of the actual
finite polynomial, not an infinite-series replacement of it.
It also proves that \(E_N\) is zero-free there for large \(N\).

On a possibly smaller disk, with logarithms continued from zero,
\[
 L_N(t)=-\frac{N}{c_0}\operatorname{Li}_2(t)
                         -\frac12\log(1-t)+O(N^{-1}).
 \tag{11}
\]
For completeness, split the sum at \(j=N/2\). On the lower half,
\[
 \frac1{1-e^{h j}}=-\frac1{h j}+\frac12+O(|h|j),
                 \qquad h=c_0/N,
\]
uniformly; the remainder after multiplication by \(t^j/j\)
sums to \(O(N^{-1})\). The upper half is exponentially small
by (8). The corresponding tails of the dilogarithm and logarithm
series are exponentially small too. This proves (11).
Cauchy estimates on a larger small disk give every fixed
\(t\)-derivative of its remainder and of (10).

Combining (10)--(11) yields the actual local finite-cap estimate
\[
 \boxed{\quad
 E_N(t)=(1-t)^{-1/2}
          \exp[-N\operatorname{Li}_2(t)/c_0]\,(1+O(N^{-1})).
 \quad}\tag{12}
\]
All branches and the unit factor in this formula come from \(t=0\).

## 3. A single saddle on the original circle

Choose a number \(0<\vartheta<\pi/2\). There exists \(a_*>0\)
such that the following construction holds on
\[
 \mathcal A=\{a:0<|a|<a_*,\ |\arg a|<\vartheta\},
                         \qquad s=c_0a^2.
 \tag{13}
\]
This is an unambiguous chosen square-root sector in \(s\).
All asymptotic estimates below are uniform on compact subsets
of \(\mathcal A\), which stay away from \(a=0\).
If \(\vartheta>\pi/4\), this includes sufficiently small positive
real \(s\): its selected root is
\(a=e^{-i\pi/4}\sqrt{s/(2\pi)}\).

In (6) use the phase and amplitude
\[
 \Phi_s(z)=\log(1+z)-\operatorname{Li}_2(-s/z)/c_0,\qquad
 A_s(z)=(1+z)^{-1}(1+s/z)^{-1/2}.
 \tag{14}
\]
These have their small branches on the circles used below.
Write \(z_*(a)=a\,v(a)\). The critical equation is
\[
 z\partial_z\Phi_s(z)
             =\frac{z}{1+z}-\frac1{c_0}\log(1+s/z)=0.
 \tag{15}
\]
After division by \(a\), its left side becomes
\[
 \frac{v}{1+av}-\frac{\log(1+c_0a/v)}{c_0a}.
\]
At \(a=0\) this is \(v-v^{-1}\), whose derivative at \(v=1\)
is two. The analytic implicit-function theorem therefore gives
a unique analytic \(v(a)=1+O(a)\) near this branch.

Use exactly the circle
\[
                             z=z_*(a)e^{i\theta},
                       \qquad -\pi\le\theta\le\pi.
 \tag{16}
\]
For sufficiently small \(a_*\), it satisfies
\(|z|<1/2\) and \(|s/z|<\rho\). Thus the finite-cap estimate
(12) is valid everywhere on this original constant-term circle.
No endpoint or other residue has been crossed.

There is a strict global maximum of the real part of the phase
on this circle at \(\theta=0\). Indeed, uniformly in a fixed
complex \(\theta\)-strip,
\[
 \Phi_s(z_*(a)e^{i\theta})=2a\cos\theta+R(a,\theta),
 \qquad \partial_\theta^jR=O(|a|^2)
 \tag{17}
\]
for every fixed \(j\). This follows by expanding (14) and using
\(v(a)=1+O(a)\).
The exact critical equation implies \(\partial_\theta R(a,0)=0\).
Consequently, for real \(|\theta|\le\pi\),
\[
 |R(a,\theta)-R(a,0)|\le C|a|^2\theta^2.
\]
Since \(\Re a\ge|a|\cos\vartheta\), reducing \(a_*\) if necessary
gives
\[
 \boxed{\quad
 \Re[\Phi_s(z_*e^{i\theta})-\Phi_s(z_*)]
                                  \le-c|a|\theta^2.
 \quad}\tag{18}
\]
This proves uniqueness of the contributing circle maximum.
It also controls the region opposite the chosen saddle and
every other part of this actual circle. Their contributions
have not been dismissed solely from the formal characteristic
equation; no estimate for points off this circle is asserted.

Put
\[
 \Psi(s)=\Phi_s(z_*),\qquad
 B(s)=(z\partial_z)^2\Phi_s(z_*)=2a+O(a^2).
 \tag{19}
\]
Then the second \(\theta\)-derivative is \(-B(s)\), and
\(\Re B(s)>0\) after reducing the sector radius.
The square root is fixed by \(B(s)\sim2a\) on the positive
\(a\)-axis, then continued analytically.

## 4. The nonzero coefficient

On the circle (16), (6) and (12) give
\[
 H_N(s)=\frac1{2\pi}\int_{-\pi}^{\pi}
  e^{N\Phi_s(z_*e^{i\theta})}
             A_s(z_*e^{i\theta})(1+O(N^{-1}))\,d\theta.
 \tag{20}
\]
The relative error is holomorphic and uniformly controlled there.
The exponentially small Taylor-cap error in (10) gives an
exponentially small relative contribution after integration:
(18) bounds its absolute size by a constant times
\(e^{N\Re\Psi(s)-\delta N}\).

A direct Gaussian calculation in (20) now gives
\[
 \boxed{\quad
 H_N(s)=
   \frac{e^{N\Psi(s)}}{\sqrt{2\pi N B(s)}}\,
                    A_s(z_*)\,(1+O(N^{-1})).
 \quad}\tag{21}
\]
Here are the needed error details. On a compact subset of (13),
split the circle at \(|\theta|=N^{-2/5}\). Relative to
\(e^{N\Re\Psi}\), the complement is \(O(e^{-cN^{1/5}})\)
by (18). On the inner interval expand
the analytic phase through its cubic term and the amplitude
through its linear term. Their odd Gaussian terms integrate
to zero on the symmetric interval. The remaining errors are
bounded by Gaussian moments of
\(N\theta^4\), \(N^2\theta^6\), and \(\theta^2\), giving relative
\(O(N^{-1})\). The analytic \(O(N^{-1})\) error in (20) has the
same bound. Extending the Gaussian to the real line costs an
exponentially small error. Finally
\(\int_{\mathbb R}e^{-NB\theta^2/2}d\theta
=\sqrt{2\pi/(NB)}\), first for positive \(B\) and then by
holomorphic continuation with \(\Re B>0\). This proves (21)
uniformly on such compact sets. Cauchy estimates give all
fixed derivatives of its normalized error on smaller sectors.

The coefficient has a useful exact expression in the selected
occupation variable
\[
                         y(s)=\frac{z_*}{1+z_*}=a+O(a^2).
\]
Equation (15) fixes the logarithmic sheet
\[
 \log(1+s/z_*)=c_0y,\qquad
 -s/z_*=1-e^{c_0y}.
\]
Therefore
\[
 \begin{split}
 \Psi(s)&=-\log(1-y)
                -\operatorname{Li}_2(1-e^{c_0y})/c_0,\\
 B(s)&=y(1-y)+(1-e^{-c_0y})/c_0,\\
 A_s(z_*)&=(1-y)e^{-c_0y/2}.
 \end{split}\tag{22}
\]
The critical relation also gives
\[
 s=\frac{y(e^{c_0y}-1)}{1-y},\qquad
                         s\Psi'(s)=y.
 \tag{23}
\]
Writing \(A=e^{c_0y}=1+s/z_*\), the first line of (22) is
\(\Psi=-\operatorname{Li}_2(1-A)/c_0-\log(1-y)\).
Its integration constant is fixed by \(\Psi\to0\) as \(a\to0\)
on the chosen sector. This calibrates the actual coupon action only.
The division by \(1-y\) is used only on this small selected
branch, where \(|y|<1/2\). It is not a deletion of the
\(y=1\) component of the exact row (3)--(4).

In particular the actual coupon asymptotic is
\[
 \boxed{\displaystyle
 H_N(s)=
 \frac{(1-y)e^{-c_0y/2}}
      {\sqrt{2\pi N\,[\,y(1-y)+(1-e^{-c_0y})/c_0\,]}}\,
 e^{N\Psi(s)}(1+O(N^{-1})).
 }\tag{24}
\]
Every displayed factor is nonzero on a sufficiently small chosen
sector away from zero. Thus \(H_N\) itself is nonzero there for
all sufficiently large \(N\), uniformly on each compact subset.
This is a selected coefficient of the literal finite coupon
period, not merely a formal solution of (4).

## 5. Source and normal scope

Formula (2) is exactly the kernel of the retained \(ZG^{-1}\)
coupon in U. Pulling (24) back by \(s=wz\) gives an actual local
coherent-kernel asymptotic wherever \(wz\) lies in this sector.
The original binomial dual, the sign \(Z\), and the degree
\(d=N-1\) are all responsible for factors in (14),(22),(24);
none was absorbed into an unspecified amplitude.

There is a source-incidence restriction as well. In U's full
turnover formula, the residual last-head coupon corresponds to
the original donor, not automatically to a recipient coherent
identity kernel. Its contraction with the upper column must
therefore be retained. Formula (24) is the bare coupon kernel;
it is not substituted for that different composed matrix row.

At fixed quantum root this coupon is independent of the
meridian \(M\). Its meridian-normal burden in the full source
therefore lies in the other interfaces and in any prescribed
\(M\)-dependent arguments. Fixed derivatives of (24) may be
used for such arguments while they remain in compact subsets
of the proved domain. This is not a computation of the whole
opposite-source first jet.

Nor is the root reflection used in U differentiated in the
quantum parameter. Off the root, the reflected donor diagonal
contains its full finite products and is not automatically the
simplified coupon (2). No ordinary quantum-normal identification
is inferred from the present fixed-root saddle proof.

The upper-cap component, the finite Euler forcing, and the
source complements have not been discarded. The first two are
accounted for by the exact polynomial identities and the actual
circle estimate. Complements belonging to other factors or to
a larger paired-source contour remain as prescribed in U.
The result does not show that a loxodromic geometric source frame
has \(wz\) in this sector, or that the product of this coupon with
the upper resolvent and quotient has a nonzero geometric period.

## Complete proof direct

* U: notes/research_upper_euler_column_resolvent_chart.md,
  SHA256 14b9686f569f224b95df928f25f81456b339a019dd5800148ba30676c91fbce1.

The complete direct was freshly read nontruncated in the immediately
preceding active author sequence and retained unchanged here. Every
used implication was checked. Only written mathematics and text/hash
operations were used. Frozen and public files were not changed.

