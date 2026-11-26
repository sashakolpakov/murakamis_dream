# The direct physical-node three-kernel bound and its absolute-trace cost

Private static source deduction, 8 November 2026. No mathematical
numerical evaluation or change to a frozen source is used.

The high-Newton contraction can be bounded on the real spectral
interval without a complex-strip norm. The resulting trace operator
cost is polynomial. Its positive input envelope, however, has exact
rate \(4b_2\) at a physical node which remains in the unresolved right
band. The absolute physical sampling formula has the same rate there.
Thus this particular direct absolute-trace argument does not supply
the required action comparison. This is not a lower bound for the
coherent single-three kernel or for the actual right observation.

## 1. Original kernel and a complete real-interval estimate

Keep the conventions of the
[high-coefficient source](research_mixed_next_high_coefficients_terminal_insertion.md),
equations (1)--(5):
\[
\begin{gathered}
D=N-1,\qquad q=e^{\pi i/N},\qquad \kappa=q^{D^2/2},\\
S_k=\prod_{a=1}^k2\sin(\pi a/N),\qquad
c_j=2\cos((2j+1)\pi/N),\\
e_k(z)=S_k^{-2}\prod_{a<k}(c_a-z),\qquad
K_N(z,t)=\sum_{k=0}^D e_k(z)e_k(t),\\
\mathcal K_{3,N}(w,z)
 =\phi_N^{(t)}[\mathcal R_N(t)^3K_N(w,t)K_N(z,t)].
\end{gathered}                                                    \tag{1}
\]
Here \(\mathcal R_N\), \(\phi_N\), and every ordinary polynomial
are the original full Hermite-algebra objects. In particular the
trace retains the first normal at each repeated physical root.

For every polynomial \(B\) of degree at most \(L\), the complete
[trace estimate, equation (1)](research_mixed_next_three_complete_trace_bound.md)
is
\[
 |\phi_N(\mathcal R_N^pB)|
 \le \{N(L+1)+|p|N^2/2\}\,
                  \sup_{-2\le t\le2}|B(t)| .                    \tag{2}
\]
It applies to the displayed unreduced product. Consequently, since
\(\deg_t(K_N(w,t)K_N(c_j,t))\le2D\),
\[
\boxed{\quad
 |\mathcal K_{3,N}(w,c_j)|
 \le (7N^2/2-N)
       \sup_{-2\le t\le2}|K_N(w,t)K_N(c_j,t)| .
\quad}                                                          \tag{3}
\]
There is no strip enlargement or change of physical observation in
(3). Physical termination gives \(e_k(c_j)=0\) for \(k>j\) when
\(0\le j<\lfloor N/2\rfloor\), so \(L=D+j\) can instead be
used for a slightly smaller polynomial prefactor.

Put
\[
 J(x)=\int_0^x\log(2\sin\pi s)\,ds,
 \qquad b_2=-4J(1/4)=2G_{\rm Cat}/\pi.
                                                               \tag{4}
\]
The full real Newton theorem, including its upper half and every
zero, proves
\[
 \sup_{-2\le w\le2}|e_k(w)|
       \le CN^A e^{Nb_2}\qquad(0\le k<N).
                                                               \tag{5}
\]
See [real-period Newton, Lemmas 1--3](research_three_crossing_real_period_newton_bound.md).
Summing the original finite kernels and applying (3) therefore gives
the genuine full-source upper bound
\[
 |\mathcal K_{3,N}(w,c_j)|\le CN^A e^{4Nb_2},
 \qquad w\in[-2,2],\quad 0\le j<\lfloor N/2\rfloor .          \tag{6}
\]
All fixed real ordinary-color derivatives have the same rate, by
Markov's inequality on the complete polynomial. A sufficiently small
fixed complex color neighborhood costs an arbitrarily small positive
rate allowance by the same polynomial continuation used in the cited
source. Neither assertion discards a repeated-root normal.

## 2. The positive input envelope has exactly this rate

Take the first retained right physical node and its largest
radical evaluation index:
\[
 M_N=\lceil N/2\rceil,\qquad n_N=D-M_N
       =\lfloor N/2\rfloor-1,\qquad k_N=\lfloor N/4\rfloor.
                                                               \tag{7}
\]
For all sufficiently large levels, \(k_N\le n_N\). Define
\[
 B_N(t)=K_N(-2,t)K_N(c_{n_N},t).
                                                               \tag{8}
\]
Then
\[
 \lim_{N\to\infty}\frac1N\log\|B_N\|_{[-2,2]}=4b_2.
                                                               \tag{9}
\]
The upper bound follows from (5). For the lower bound, the regular
quarter-index factorial estimate gives
\[
 e_{k_N}(-2)=\exp\{Nb_2+O(\log N)\}.
                                                               \tag{10}
\]
Also \(c_{n_N}=-2+O(N^{-2})\). Every numerator factor of
\(e_{k_N}(-2)\) is bounded below by a fixed positive constant.
Comparing its factors with those at \(c_{n_N}\) therefore gives
\[
 e_{k_N}(c_{n_N})
          =e_{k_N}(-2)\{1+O(N^{-1})\}>0 .                      \tag{11}
\]
At \(t=-2\), the first kernel in (8) is a sum of squares. In
the second, every surviving \(e_k(c_{n_N})\) and \(e_k(-2)\)
is nonnegative. Keeping just index \(k_N\) in each proves
\(B_N(-2)\ge e_{k_N}(-2)^3e_{k_N}(c_{n_N})\), which with
(10)--(11) proves (9).

The corresponding coefficient in the actual high-Newton contraction
is not exponentially small. Precisely, its diagonal is
\[
 b_{n_Nn_N}=\frac{S_{n_N}^2}{S_{2n_N}}>0,
 \qquad \log b_{n_Nn_N}=O(\log N).
                                                               \tag{12}
\]
The exact diagonal formula is in
[radical contraction, Proposition 4](research_high_newton_radical_contraction.md).
The logarithmic assertion follows either from factorial reflection
at the bounded distance of \(2n_N\) from \(N\), or the exact
half-factorial formulas in
[insertion recoupling, Section 3](research_mixed_next_right_insertion_recoupling_and_norm.md).
Thus (9) is relevant to an original retained pair of indices, not a
new test polynomial unrelated to the source.

## 3. Absolute Hermite sampling has the same obstruction

This cost is not merely a loose estimate of the supremum in (3).
Use the complete derivative sampling formula from the
[trace estimate, equations (2)--(4)](research_mixed_next_three_complete_trace_bound.md):
\[
\begin{gathered}
 \tau_a=\frac{2\pi}{N}(D/2-a),\qquad
 b_N(\theta)=B_N(-2\cos\theta),\\
 g_N(\theta)=\sin\theta\,b_N(\theta)
                   e^{3iN\theta^2/(4\pi)},\\
 \phi_N(\mathcal R_N^3 B_N)
       =(-1)^D q^{3D^2/4}\sum_{a=0}^{N-1}g_N'(\tau_a).
\end{gathered}                                                    \tag{13}
\]
The absolute sampling sum obeys
\[
 \lim_{N\to\infty}\frac1N
           \log\sum_{a=0}^{N-1}|g_N'(\tau_a)|=4b_2.
                                                               \tag{14}
\]
For the upper bound use trigonometric Bernstein and (9), exactly as
in the proof of (2). At odd levels the grid contains zero and
\(g_N'(0)=B_N(-2)\), giving the lower bound immediately.
At even levels its nearest positive point is \(\tau=\pi/N\),
and \(-2\cos\tau=c_{n_N}\). Since \(b_N,b_N'\) are real on
the real line,
\[
 |g_N'(\tau)|
 \ge \frac{3N\tau}{2\pi}\sin\tau\,B_N(c_{n_N})
 =\frac32\sin(\pi/N)B_N(c_{n_N}).                            \tag{15}
\]
Both kernels in \(B_N(c_{n_N})\) again have nonnegative surviving
terms. Keeping \(k_N\) gives rate \(4b_2\) by (10)--(11).
The sine in (15) costs only a polynomial factor. This proves (14)
at both parities, retaining the actual simple or double-node term.

For a standalone rational witness, the alternating Catalan series gives
\[
 G_{\rm Cat}>1-\frac19+\frac1{25}-\frac1{49}
       =\frac{10016}{11025}>\frac9{10}.
\]
Together with \(\pi<22/7\), this proves \(b_2>63/110\), hence
\[
 4b_2>126/55>419/200,
 \qquad \frac{126}{55}-\frac{419}{200}
                     =\frac{431}{2200}>0 .                    \tag{16}
\]
Here \(419/200\) is the available uniform actual next-three action
floor in the
[actual high-band source, equation (19)](research_mixed_next_right_insertion_actual_high_band.md).
Thus replacing the inner trace by its absolute sampling sum already
exceeds this certified budget before taking positive upper bounds for
the outgoing rows. The latter contain their original zeroth row one.
This comparison does not assert that the actual action equals its
floor, nor that the complete outgoing kernel has modulus at least one.

## 4. The coherent quantity still required

The exact retained source remains
\[
 \ell_b(w)=\sum_{j=0}^{D-b}b_{D-b,j}\mathcal R_N(c_j)^3
                                  \mathcal K_{3,N}(w,c_j),
                                                               \tag{17}
\]
followed by \((-q)^b C_{0,N}(r^b,Z)/(\kappa^2N)\), with the
original physical band and ordinary output. No new \(+N\) is added
to that already normalized observation.

The loss in (14) is compatible with strong cancellation in (13).
For example the continuous zero-frequency integral is exactly
\(\int_{-\pi}^{\pi}g_N'(\theta)\,d\theta=0\), because
\(\sin(\pm\pi)=0\). A positive estimate of the samples does not
retain this derivative cancellation. The terminal contour estimate
does retain it, but its extension to the present two-boundary input
still requires the inserted kernel on all original trace contours.

Consequently (3) is a valid direct bound which removes the complex
strip norm, while (9) and (14) identify why its absolute implementation
does not close the unresolved middle insertion using the current
uniform action floor. They do not prove failure of a sharper bound
for \(\mathcal K_{3,N}\), of coherent cancellation across (17), or of
the original full transfer. No full-source noncancellation statement
is inferred from positivity of the physical Newton evaluations.
