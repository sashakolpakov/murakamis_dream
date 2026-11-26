# Bounding the positive part of the outer contour

Private research note, 9 November 2026. The complete inner asymptotic
on the positive rectangle now bounds the portions of the outer
horizontal contour between the imaginary axis and real part \(8/7\),
apart from the selected stationary point. Combined with the previously
proved central-segment bound, this leaves precisely three integrals
to estimate. This is a written deduction from the exact finite source;
no numerical evaluation is used.

## 1. Contours and statement

Use the observation \(\mathcal O_{N,k}\), normalized integral
\(\mathcal I_{N,k}(\gamma)\), and midpoint \(T_N\) defined in
[the local Gaussian decomposition](research_mixed_next_outer_local_gaussian_and_remaining_currents.md),
equations (3), (9), and (11). In particular, the integrand is
\[
 \mathcal I_{N,k}(\gamma)
 =\frac{\chi_N C_{N,3}N}{4\pi}
   \int_\gamma H_N(u)a_N(u)Q_N^{\rm sh}(u)
     e^{N(3iu^2/(4\pi)-i\delta u)}(1+e^{-2iku})\,du,
 \qquad \delta=\frac12-\frac{k}{N}.
 \tag{1}
\]
Here \(H_N(u)=(1-(-1)^{N-1}e^{-iNu})^{-1}\), and the parity
factors \(a_N,\chi_N,C_{N,3}\) are unchanged. The shortened
source in (1) is licensed by the exact finite-node identity; it
is not substituted for the full source at arbitrary complex points.

Fix \(\delta_1>0\) and restrict to the integer frequencies with
\(\delta\in[\delta_1,1/2]\). Write the selected point as
\(u_\delta=\beta_\delta-iK_\delta\), and put
\[
 \beta_- =\min\beta_\delta>0,\qquad
 \beta_+ =\max\beta_\delta<8/7,
 \qquad K_- =\min K_\delta>0.
 \tag{2}
\]
All extrema here and below are over that fixed compact interval.

Choose the Gaussian radius \(r>0\) to satisfy all conditions
of the local Gaussian theorem and also
\[
                  r<\beta_-/4,\qquad 2r<8/7-\beta_+.
 \tag{3}
\]
Shrinking that radius preserves its theorem. Choose the central
width \(\epsilon>0\) as in
[the central-segment theorem](research_mixed_next_outer_central_block_payment.md),
so \(\epsilon<\beta_-/4\). Set \(b=8/7\).

Let \(J_{N,k}^{-}\), \(J_{N,k}^{+}\), and \(J_{N,k}^{v}\)
be the integrals (1) over the following oriented paths:
\[
 \begin{aligned}
  \gamma^- &: -T_N-iK_\delta\longrightarrow-\epsilon-iK_\delta,\\
  \gamma^+ &: b-iK_\delta\longrightarrow T_N-iK_\delta,\\
  \gamma^v &: T_N-iK_\delta\longrightarrow T_N+iK_\delta.
 \end{aligned}
 \tag{4}
\]
The first two are horizontal and oriented to the right. The third
is vertical and oriented upwards. It lies on the same midpoint line
as before and meets no sampling pole.

**Theorem.** At both parities, uniformly in these frequencies,
\[
 \mathcal O_{N,k}
       =G_{N,k}+J_{N,k}^{-}+J_{N,k}^{+}+J_{N,k}^{v}+E_{N,k},
 \qquad
 |E_{N,k}|\le C e^{N\{\Gamma(\delta)-\eta\}},
 \tag{5}
\]
for a fixed \(\eta>0\). Here \(\Gamma\) is the real part of
the selected outer action. The local integral \(G_{N,k}\) has the
same nonzero asymptotic and the same original coefficient as in
the local Gaussian theorem, with the radius chosen in (3).

## 2. Estimate on the positive horizontal segments

Consider the two intervals
\[
 [\epsilon,\beta_\delta-r]-iK_\delta,
       \qquad [\beta_\delta+r,b]-iK_\delta.
 \tag{6}
\]
They are nonempty by (2)--(3). Both lie in the closed rectangle
\(0\le\Re u\le8/7\), \(-2/5\le\Im u\le0\).
[The complete inner theorem](research_mixed_next_positive_rectangle_inner_packet.md)
therefore gives the uniform bound
\[
 |Q_N^{\rm sh}(u)|\le C N^{-3/2}e^{N\Re S(u)}.
 \tag{7}
\]
This is a bound on the entire finite inner source. The relative
asymptotic is not integrated through any cancellation to obtain it.

Let \(\Psi_\delta(u)=S(u)+3iu^2/(4\pi)-i\delta u\).
[Horizontal descent](research_mixed_next_charged_curve_two_sided_descent.md)
gives on both intervals
\[
 \Re\Psi_\delta(u)
 \le\Gamma(\delta)-\frac{(\Re u-\beta_\delta)^2}{100\pi}
 \le\Gamma(\delta)-\frac{r^2}{100\pi}.
 \tag{8}
\]
The exact remaining factors satisfy
\[
 |H_N(u)|\le(1-e^{-NK_-})^{-1},\qquad
 |1+e^{-2iku}|\le2.
 \tag{9}
\]
The parity amplitude \(a_N\) is uniformly bounded on this
compact rectangle. The lengths in (6) are bounded, and the
factor \(N\) in (1) combines with \(N^{-3/2}\) in (7).
Consequently the sum of the two absolute integrals is at most
\[
             C N^{-1/2}
                  e^{N\{\Gamma(\delta)-r^2/(100\pi)\}}.
 \tag{10}
\]
Every reflected charge and sampling correction remains in this
estimate. In particular it also covers \(k=0\).

## 3. Exact assembly and remaining task

Split the original bottom contour at
\[
 -\epsilon-iK_\delta,\quad \epsilon-iK_\delta,\quad
 u_\delta-r,\quad u_\delta+r,\quad b-iK_\delta.
\]
This creates no residues or new connector integrals. Its central
segment has absolute bound
\(C e^{N\{\Gamma(\delta)-\beta_-^2/(200\pi)\}}\), by the
central-segment theorem. The two segments in (6) satisfy (10).
The original excluded-node sum has bound
\(C e^{N\{\Gamma(\delta)-1/100\}}\).

Define \(E_{N,k}\) to be exactly these four contributions: the
central integral, the two positive integrals, and the excluded-node
sum. Their bounds prove (5), for example with
\[
 \eta=\min\left\{\frac{r^2}{200\pi},
                        \frac{\beta_-^2}{200\pi},\frac1{100}\right\}>0.
\]
The three integrals in (4) are all the remaining terms.

To obtain a nonzero asymptotic for the whole observation, it would
suffice to prove that their sum is exponentially smaller than
\(e^{N\Gamma(\delta)}\). No such estimate is asserted here.
The further comparison after the outgoing coefficients are attached,
and stability under arbitrary fixed short fillings, remain separate
requirements for the finite-exceptions theorem.

## Source versions

- Complete positive-rectangle inner theorem:
  a1520474da2d389cb9cf67e92618f6ca9c552d499f35a039e842f9fc4e5075eb.
- Exact outer decomposition and local nonzero coefficient:
  6f2b155eee54cfd8a930d9af146ab96c3de277aac70d2de51b5f8318523f45ab.
- Central-segment bound:
  585b5a97a559735ea4ea3d98647d8e945000fdb144f2cae56ebf38dfa889d5e6.
- Horizontal descent of the original phase:
  102daa403519833ca13414ca2e0e20f351c572a5740ab9ca6ffb1c204d2eda7f.

