# A positive two-state transfer for the actual spectral tail

31 October 2026. **Internally reviewed local theorem.** The complete
analytical proof received independent review; this is not external peer review.
This is an exact model of the original normalized tail, including negative
recurrence coefficients in its usual two-term form. It gives compact-interior
Perron and outer-angular estimates. It is not yet an exponentially accurate
interpolation in the starting and ending rows or a global sign-cancellation
theorem.

## 1. Exact normalization and word expansion

Use the original one-sided tail from the
[relative-energy theorem](actual_one_sided_relative_spectral_energy.md).
For fixed actual rows \(0\le i\le j\), let \(r=j-i\),
\(\theta=\pi/N\), and

$$
s_a=2\sin(a\theta),\qquad
\lambda=\cos\theta+\cos(2\pi\delta),\qquad
\eta_a=\frac{\lambda}{\cos\theta-\cos((2a-1)\theta)}.
$$

The denominator occurs only at \(a\ge i+2\), so no zero row denominator
is used. Put

$$
Q_r=\frac{K_{i,j}}{\prod_{a=i+1}^j s_a^2},\qquad
Q_0=1,\quad Q_1=x+y,\quad
Q_l=(x+y)Q_{l-1}+(\eta_{i+l}-1)xyQ_{l-2}.\tag{1}
$$

For \(r\ge1\), initialize \((X_1,Y_1)=(x,y)\), and set

$$
\begin{pmatrix}X_l\\Y_l\end{pmatrix}
=M_l\begin{pmatrix}X_{l-1}\\Y_{l-1}\end{pmatrix},\qquad
M_l=\begin{pmatrix}x&\eta_{i+l}x\\y&y\end{pmatrix},
\qquad 2\le l\le r.\tag{2}
$$

Then \(Q_l=X_l+Y_l\) exactly: \(Y_{l-1}=yQ_{l-2}\), and summing (2)
gives (1). Equivalently,

$$
Q_r=\sum_{w\in\{x,y\}^r}x^{\#x(w)}y^{\#y(w)}
 \prod_{l=2}^r\eta_{i+l}^{\mathbf1_{\{w_{l-1}=y,\ w_l=x\}}}.
\tag{3}
$$

The initial state contains no transition weight. The empty word gives
\(Q_0=1\). This proof retains every actual row parameter. For real
\(\lambda\ge0\), all word weights are nonnegative even if
\(\eta_a-1<0\). No claim of positivity is made for the original unused
prefix/suffix factors or for negative \(\lambda\) in the final spectral cap.
The energy Cauchy theorem treats that cap separately without this positivity.

## 2. Uniform angular contraction in the relative outer phase

Suppose every entry of the real matrices (2) lies in \([m,M]\), with
\(0<m\le M<\infty\). This holds uniformly when \(x,y\) range in a compact
positive set, \(\delta\) stays a fixed distance below \(1/2\), and all rows
\((i+l)/N\) stay in a compact subinterval of \((0,1/2)\).

For phases \(\vartheta_x,\vartheta_y\), the matrix is obtained by multiplying
its two rows by their respective phases. In each entry of a two-step
product, the two intermediate states contribute positive weights
\(A,B\in[m^2,M^2]\) and relative phase
\(\vartheta=\vartheta_x-\vartheta_y\). Therefore

$$
\begin{aligned}
|Ae^{i\vartheta}+B|^2
 &=(A+B)^2-4AB\sin^2(\vartheta/2),\\
\frac{4AB}{(A+B)^2}&\ge(m/M)^4.
\end{aligned}\tag{4}
$$

Set \(\kappa=(m/M)^4\). Pair consecutive transfer matrices, apply (4)
entrywise, and then multiply nonnegative majorants. The unpaired transfer
and initial vector obey ordinary triangle inequalities. This gives the
exact bound

$$
|Q_r(xe^{i\vartheta_x},ye^{i\vartheta_y})|
\le\exp\!\left[-\frac\kappa2
 \left\lfloor\frac{r-1}{2}\right\rfloor
 \sin^2\!\frac{\vartheta_x-\vartheta_y}{2}\right]Q_r(x,y).
\tag{5}
$$

Thus a macroscopic interval has a uniform exponential outer-angular gap
away from equal phases. Equal phases are an essential exception:
\(Q_r(e^{i\vartheta}x,e^{i\vartheta}y)=e^{ir\vartheta}Q_r(x,y)\).
There is no independent contraction in both frequencies. If either outer
weight is zero, the surviving polynomial is a monomial and the relative
angular statement is vacuous. At \(\lambda=0\) strict matrix positivity
also fails; (5) is not extended there by assumption.

## 3. A compact-interior relative Perron product

Fix a compact positive set of outer weights, a compact real spectral set
with \(\delta<1/2\), and constants \(\epsilon>0\) such that

$$
\epsilon\le i/N<j/N\le1/2-\epsilon,\qquad (j-i)/N\ge\epsilon.
\tag{6}
$$

For all sufficiently large \(N\), the matrices (2) are uniformly strictly
positive, bounded, and vary by \(O(N^{-1})\) per row. Their Perron roots are

$$
\rho_l=\frac{x+y+\sqrt{(x-y)^2+4\eta_{i+l}xy}}2.\tag{7}
$$

The square root, \(\rho_l\), and the Perron eigenspaces extend analytically
to one fixed small complex neighborhood of the compact parameter set.
The second eigenvalue may vanish. Nevertheless the discriminant stays
nonzero and the modulus of its ratio to \(\rho_l\) is bounded by some
\(a<1\), also on a sufficiently small complex neighborhood. No division by
the second eigenvalue is used.

Choose right and left eigenvectors \(v_l,u_l\), normalized by
\(\mathbf1^Tv_l=1\) and \(u_l^Tv_l=1\). With \(z=(x,y)^T\), define

$$
A_{i,j,N}=(\mathbf1^Tv_r)(u_2^Tz)
          \prod_{l=3}^r(u_l^Tv_{l-1}).\tag{8}
$$

The empty products retain their usual meanings. Uniformly under (6),

$$
Q_r=A_{i,j,N}\prod_{l=2}^r\rho_l\,[1+O(N^{-1})].\tag{9}
$$

Here \(A_{i,j,N}\) is a nonvanishing analytic factor bounded above and
below uniformly, on a smaller fixed complex neighborhood. Indeed each
\(u_l^Tv_{l-1}=1+O(N^{-1})\), while the initial and terminal factors are
positive units on the real compact set.

For a proof, use the two instantaneous eigenvectors as a moving basis.
After dividing each matrix by \(\rho_l\), successive changes of basis
have diagonal entries \(1+O(N^{-1})\) and off-diagonal entries
\(O(N^{-1})\). The second coordinate contracts by at most \(a+O(N^{-1})\).
Its initial contribution feeds the first coordinate by a geometric sum of
size \(O(N^{-1})\). Thereafter the generated second coordinate is
\(O(N^{-1})\) of the first, so its feedback is \(O(N^{-2})\) per step,
with total \(O(N^{-1})\). The terminal second-coordinate error has the
same size. The diagonal main factors are exactly those in (8).
These estimates also hold uniformly for the complex neighborhood, and
Cauchy gives the corresponding fixed-parameter derivative estimates on
a smaller neighborhood.

The original tail is still \(K_{i,j}=(\prod s_a^2)Q_r\). In the limit
\(t=(i+l)/N\), multiplication of (7) by \(4\sin^2(\pi t)\) gives exactly

$$
2\sin(\pi t)\left[(x+y)\sin(\pi t)+
 \sqrt{(x-y)^2\sin^2(\pi t)+4xy\cos^2(\pi\delta)}\right],\tag{10}
$$

the original sharp weighted tail root. Thus no new scalar normalization
or absolute recurrence has entered.

## 4. A regular outer-coefficient saddle

In the regime (6), let \(k/r\) stay in a compact subinterval of \((0,1)\),
and set \(y=1\). There is a unique positive tilt \(x=e^{\ell_N}\) with

$$
\partial_\ell\log Q_r(e^\ell,1)\big|_{\ell_N}=k.\tag{11}
$$

These tilts lie in a fixed compact interval. To see this directly from
(3), condition on all states except one. The conditional ratio of an
\(x\) state to a \(y\) state equals \(e^\ell\) times at most two transition
ratios, which are uniformly bounded above and below. Small or large fixed
\(\ell\) therefore puts the expected \(x\) fraction uniformly near zero
or one. Positivity of every word makes the mean strictly increasing.

At compact tilts the variance \(V_N=\partial_\ell^2\log Q_r\) satisfies
\(cN\le V_N\le CN\). For the lower bound condition on all odd positions:
the even states become independent Bernoulli variables with probabilities
bounded away from zero and one. Conditional variance and the law of total
variance give a constant times \(r\). For the upper bound and all higher
fixed cumulants, (9) provides an analytic logarithm on a uniform complex
tilt neighborhood, with derivatives \(O(N)\).

Cauchy coefficient extraction, (5), and the Taylor expansion of that
analytic logarithm now give

$$
[x^ky^{r-k}]Q_r(x,y)
=\frac{Q_r(e^{\ell_N},1)e^{-k\ell_N}}
       {\sqrt{2\pi V_N}}[1+O(N^{-1})].\tag{12}
$$

For precision, outside a fixed small angular interval (5) is exponentially
small. Inside it, the variance lower bound and bounded higher derivatives
give Gaussian decay. On the shrinking central interval the cubic term is
odd and imaginary and integrates to zero; the quartic and squared cubic
terms contribute relative \(O(N^{-1})\). All constants are uniform on the
stated strict compact sets. Formula (12) is a coefficient theorem for the
actual tail, not for a separately chosen positive comparison polynomial.

## 5. Original factors and the remaining magnetic problem

A complete original one-sided coefficient includes the omitted-half factor,
all unused prefix and suffix rows, and \(\prod s_a^2\). They must multiply
(9) or (12) exactly. On a strict sign chamber the unused-row signs form the
recorded lattice character. The omitted-half factor retains its two
oscillatory modes and can vanish densely; it is not a nonzero analytic
amplitude that may be divided out on a fixed spectral disk.

These results control the outer relative frequency and give a relative
\(O(N^{-1})\) regular coefficient approximation. They do not give an
exponentially accurate analytic interpolation in \(i/N,j/N,k/N\).
The [literal four-state transfer](research_original_one_sided_four_state_transfer.md)
and [analytic switch theorem](research_analytic_switching_suppression.md)
now provide a separate route for the middle frequencies: the
[regular-window theorem](research_regular_spectral_window_phase_exclusion.md)
proves exponential loss outside the exact local alignment, retaining both
gauge boundary terms and every unused factor. On an inconsistent shared
sign system it improves the original Cauchy bound relative to the window
envelope. Compatible phase systems, irregular windows and comparison of
that envelope with complete volume remain open. Polynomial relative errors
or smooth integration by parts alone would not prove that exponential loss.

The exact recurrence/source interface is checked by the
[finite original-coefficient audit](../experiments/audit_actual_one_sided_relative_spectral_energy.py).
The new word, contraction and regular saddle arguments above are analytical;
no large-level numerical profile is used as their proof.
