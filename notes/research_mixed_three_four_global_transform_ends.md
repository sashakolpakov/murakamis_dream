# A uniform bound for the extreme transform rows of the ordinary three/four source

Research deduction, 7 November 2026. The extreme transform rows are
exponentially smaller than the geometric contribution throughout the
entire incoming circle and its required range of radii. The first
factor is kept complete. The proof combines a finite binomial identity
with the bounds for sums of moduli of complete endpoint coefficients.
It uses no new numerical evaluation.

## 1. The finite functions being estimated

Use the conventions of
[the ordinary three/four source](research_mixed_three_four_ordinary_pair_target.md):
\[
\begin{gathered}
 r=e^{-2\pi i/N},\qquad P_j=\prod_{s=1}^j(1-r^s),\qquad
 p_j(X)=\prod_{s=1}^j(1-r^sX),\qquad S_j=|P_j|,\\
 U_{\alpha,N}(w,X)=
 \sum_{j=0}^{N-1}\frac{H_N(w,r^{-j})p_j(X)}{P_j^{1+\alpha}},
 \qquad \alpha=0,1,\\
 V_{1,N}(w,X)=
 \sum_{i=0}^{N-1}\frac{X^{-i}p_i(X)}{P_i^2}U_{1,N}(w,r^i).
\end{gathered}                                                    \tag{1}
\]
Here \(H_N\) is the original complete endpoint polynomial, including
all its Newton terms. In particular, a bound for \(H_N\) is not
silently replaced by a bound for an arbitrary part of its sum.
All factorial denominators in (1) are nonzero.

The exact ordinary contraction is
\[
 Z_{34,N}(w_L,w_R)=
 \kappa_N^3N^2\oint U_{0,N}(w_L,X)V_{1,N}(w_R,X)
                                      \frac{dX}{2\pi iX},
 \qquad |\kappa_N|=1.                                    \tag{2}
\]
There is no additional diagonal or halfweight in (2).

Write
\[
 X=e^{-2\pi i(x+ih)},\qquad
 0\le x\le1,\qquad -9/125\le h\le21/1000.                 \tag{3}
\]
Thus \(|X|=e^{2\pi h}\). This compact annulus includes both the
actual constant-height contour and its left taper.

Let
\[
 J(t)=\int_0^t\log(2\sin\pi s)\,ds,\qquad 0\le t\le1,
 \qquad c_{\mathrm b}=-2J(1/6).
                                                               \tag{4}
\]
The endpoint integrals are understood by continuity. Since
\(J'(t)=\log(2\sin\pi t)\), symmetry gives
\[
 \max_{0\le t\le1}(-J(t))=-J(1/6)=c_{\mathrm b}/2,
 \qquad c_{\mathrm b}<1/3.                               \tag{5}
\]
For the last inequality, strict concavity of sine on
\([0,\pi/6]\) gives \(2\sin\pi s>6s\) for \(0<s<1/6\).
Integrating yields \(J(1/6)>-1/6\).

## 2. A finite binomial bound on every radius

The finite \(r\)-binomial formula is
\[
 \frac{p_j(X)}{P_j}
  =\sum_{k=0}^j
       \frac{(-1)^kr^{k(k+1)/2}X^k}{P_kP_{j-k}},
       \qquad 0\le j<N.                                \tag{6}
\]
It follows either by multiplying the factors of \(p_j\), or by
induction with \(p_{j+1}(X)=(1-r^{j+1}X)p_j(X)\).
The upper limit \(j<N\) is essential for the nonvanishing
denominators; no limiting value of a vanishing factorial is used.

The uniform sine-product estimate is
\[
 \log S_k=NJ(k/N)+O(\log N),\qquad 0\le k<N.              \tag{7}
\]
Its error is uniform through both ends. It follows by the
monotone integral comparison on either side of \(1/2\), with
the two logarithmic endpoint intervals contributing \(O(\log N)\).
Equations (5)--(7) imply
\[
 \frac{|p_j(X)|}{S_j}
 \le C N^B
       \exp N\{c_{\mathrm b}+\log_+|X|\},\qquad j<N,      \tag{8}
\]
where \(\log_+R=\max(0,\log R)\). Indeed every summand in (6)
has denominator rate at most \(c_{\mathrm b}\), and
\(|X|^k\le\max(1,|X|)^N\). There are at most \(N\) summands.
This bound holds for all complex \(X\), including zeros of \(p_j\).

The previously proved coefficient bounds are
\[
 \sum_{j=0}^{N-1}\frac{|H_N(w,r^{-j})|}{S_j^\alpha}
 \le C_\epsilon N^{B_\epsilon}
                     e^{N(b_\alpha+\epsilon)},\qquad
 b_0=101/125,\quad b_1=433/500.                          \tag{9}
\]
For colors in a sufficiently small fixed complex neighborhood of
\(-2\), these are
[the cap seam bounds](research_mixed_cap_seam_source_bounds.md),
Theorem 1. The equality
\(|H_N(w,r^{-j})|=S_j|C_N(j/N,w)|\) explains the normalization.
For every real color \(w\in[-2,2]\), the same bounds follow from
[the real-color extension](research_mixed_terminal_real_color_decay.md),
Lemma 2. The tolerance \(\epsilon>0\) is arbitrary; a complex
color neighborhood may depend on it.

Multiplying (8) and (9) proves the global estimate
\[
 |U_{\alpha,N}(w,X)|
 \le C_\epsilon N^{B_\epsilon}
 e^{N\{b_\alpha+c_{\mathrm b}+\log_+|X|+\epsilon\}}.
                                                               \tag{10}
\]
Only the outer finite sum was bounded by its sum of moduli.
Each \(H_N\) in (9) remains its complete complex value.
On (3), \(\log_+|X|\le21\pi/500<33/250\), so in particular
\[
 |U_{0,N}(w,X)|
 \le C_\epsilon N^{B_\epsilon}
                  e^{N(191/150+\epsilon)}.             \tag{11}
\]
This is a deliberately coarse bound away from the geometric
critical point. It will be combined only with the much smaller
extreme transform rows.

## 3. The extreme rows are uniformly small on the annulus

For \(0<\delta<1/2\), define the positive outer-row majorant
\[
 E_{\delta,N}(w,X)=
 \sum_{\substack{0\le i<N\\i/N\le\delta\ \mathrm{or}\ i/N\ge1-\delta}}
       \left|\frac{X^{-i}p_i(X)}{P_i^2}\right|
                      |U_{1,N}(w,r^i)|.                \tag{12}
\]
The complete private and Newton sums stay inside each \(U_{1,N}\).
This is stronger than a bound for the modulus of the signed sum
of these rows.

**Lemma 1.** There is a fixed \(\delta>0\) for which
\[
 E_{\delta,N}(w,X)\le C N^B e^{217N/250}                 \tag{13}
\]
uniformly on (3), for all real colors \(w\in[-2,2]\), and also
on a sufficiently small fixed complex neighborhood of \(-2\).
Each fixed ordinary-color derivative has the corresponding
positive-row bound.

*Proof.* The proof of
[the original transform-end theorem](research_mixed_terminal_transform_tails.md),
Lemma 2, uses the incoming variable only through
\[
\begin{split}
 \chi(t,x+ih)
  &=I_{x+ih}(t)-2J(t)-2\pi ht,\\
 I_{x+ih}(t)
  &=\int_0^t\log|1-e^{-2\pi i(x+ih+s)}|\,ds.
\end{split}                                                    \tag{14}
\]
This is the zero-safe upper rate of the outer coefficient in
(12). It is continuous on the full compact domain (3) times
\([0,1]\), even when the integrand has a logarithmic zero.
Translation and radial motion of these integrable singularities
preserve continuity. Jensen's identity gives
\[
 \chi(0,x+ih)=0,\qquad
 \chi(1,x+ih)=2\pi(-h)_+\le18\pi/125.                    \tag{15}
\]
Neither identity restricts \(x\) to the original central interval.

For clarity, the uniform finite-product upper bound also extends
to the whole annulus. Truncate the logarithmic factor from below
at \(-A\). The truncated factor is continuous jointly in the
radius and angle, so its partial Riemann sums converge uniformly.
The integral error from truncation tends uniformly to zero as
\(A\) increases: the logarithmic singularities have uniformly
integrable negative parts on this compact annulus. Since
truncation only increases each finite logarithm, this proves
an upper bound with any prescribed rate tolerance, including at
an exact zero. Equation (7) handles the denominators.

For \(t=i/N\le\delta\le1/1000\), (9) and the original small
real outgoing-collar product bound give
\[
 |U_{1,N}(w,r^i)|
 \le C N^B e^{N(b_1+\Delta_\delta+\epsilon)},\qquad
 \Delta_\delta=\delta\log2-J(\delta)\longrightarrow0.
                                                               \tag{16}
\]
This statement retains the entire private sum.

For \(i/N\ge1-\delta\), exact termination instead gives
\[
 U_{1,N}(w,r^i)
  =\sum_{j=0}^{N-1-i}
          \frac{H_N(w,r^{-j})p_j(r^i)}{P_j^2}.           \tag{17}
\]
Every deleted term vanishes identically for all colors. If
\(s=j/N\) and \(u=\ell/N\) is its Newton index, the remaining
support has \(0\le u\le s\le1-t\). The original absolute upper
rate, before the outer coefficient, is at most
\[
 V_0(u)-J(u)-J(s-u)+J(t+s)-J(t)-J(s).                   \tag{18}
\]
Here \(V_0\) is the complete-color Newton rate. This bound also
holds for all real colors, because on this small support
\(V_\theta(u)\le V_0(u)\); see Lemma 2 of the cited
real-color extension. All functions in (18) have continuous
zero endpoint values on the shrinking support, so its supremum
tends to zero as \(t\uparrow1\). The original product
regularization gives the same statement near the complete
complex color, with an arbitrarily small rate tolerance.

Choose \(\delta\le1/1000\) such that each small quantity in
(16), the supremum of (18), and the two endpoint continuity
errors in (14)--(15) is less than \(1/2000\). Choose the
total remaining finite-product and color tolerances below
\(1/1000\). The lower end then has rate less than
\[
 433/500+1/500=217/250.
\]
The upper end has rate less than
\(18\pi/125+1/500<217/250\).
The number of outer rows changes only the polynomial prefactor.

For complex colors, Cauchy's formula on a smaller fixed disk
gives each fixed derivative, applied to the complete coefficient
in every row. For real colors, apply the polynomial Markov
inequality to each complete \(U_{1,N}(w,r^i)\), whose color
degree is at most \(N-1\). Summing their separate suprema costs
at most another factor \(N\). Thus fixed derivatives preserve
the exponent without a partial Newton estimate. \(\square\)

## 4. Comparison with the original geometric action

Let \(M\) be the real part of the actual complete ordinary
three/four critical action, with its original additive
normalization. The original two-vertex bound,
[equation (15)](research_mixed_two_vertex_first_collar.md),
gives
\[
 M>9/4-147\pi/20000>22269/10000.                         \tag{19}
\]
The last strict inequality uses \(\pi<22/7\).

**Theorem 2.** For the fixed \(\delta\) in Lemma 1, throughout
(3), the extreme transform rows multiplied by the whole
first factor satisfy
\[
 |U_{0,N}(w_L,X)|\,E_{\delta,N}(w_R,X)
       \le C N^B e^{N(M-1/20)}.                         \tag{20}
\]
The two colors may range independently over \([-2,2]\), or
over sufficiently small fixed complex neighborhoods of \(-2\).
The corresponding positive-row bounds hold for every fixed
mixed ordinary-color derivative and both level parities.

*Proof.* The sum of the ceilings in (11) and (13) is
\[
 191/150+217/250=803/375.
\]
Its distance below (19) is
\[
 22269/10000-803/375=2567/30000>2/25.                    \tag{21}
\]
Choose the tolerance in (11) small enough to retain \(1/20\).
The derivative assertions follow from the derivative versions
of (9), (11), and Lemma 1. Alternatively, for the real-color
assertion apply the Markov inequality before allocating the
fixed gap. All costs for a fixed derivative order are
polynomial in \(N\). \(\square\)

Consequently the extreme-row part of (2) has rate at most
\(M-1/20\) on any fixed piecewise smooth contour in (3) with
bounded length. The original factor \(\kappa_N^3N^2\) is
retained and only changes the polynomial prefactor. This is a
pointwise bound on that row sector; it does not justify
replacing a partial root-of-unity sum by a continuous arc.

No central transform row is estimated by Theorem 2. In particular,
the global first-factor bound (11) is not a replacement for
the geometric-phase estimates in the central part of the source.
The lower bound for the whole ordinary contraction still requires
those terms and all contour joins to be controlled separately.
