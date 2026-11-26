# Logarithmic germ truncation and the original turn remainder

Research deduction, 6 November 2026. The local geometric datum need
not have a level-independent finite dimension. On a fixed regular
chart, logarithmic Taylor order preserves its nonzero Gaussian
contribution. The outstanding condition concerns the original
complementary source after transport, rather than the number of
coefficients used to represent the local phase.

## 1. A constructive local compression

Let \(D_R\subset\mathbb C^b\) be a polydisk about a fixed center,
and fix \(0<r<r_1<R\). Suppose \(W,A\) are holomorphic on a
neighborhood of its closure, \(|W|,|A|\le M\), and
\(|A|\ge a>0\) on \(D_{r_1}\). Let \(P_K\) retain the Taylor
coefficients whose degree in each coordinate is at most \(K\).
For \(\rho=r_1/R<1\), the coefficient Cauchy bound gives
\[
 \|f-P_Kf\|_{D_{r_1}}
 \le {bM\rho^{K+1}\over(1-\rho)^b},\qquad f=W,A.       \tag{1}
\]
Indeed, sum the geometric coefficient majorant over the union of
the \(b\) sets on which one coordinate degree exceeds \(K\).
Cauchy's derivative estimate between \(D_r\) and \(D_{r_1}\)
then bounds every derivative of order at most two by a constant
times \(\rho^{K+1}\). All constants are independent of \(N,K\).

**Proposition 1.** For every fixed \(q>0\), choosing
\[
 K_N=\left\lceil{(q+2)\log N\over|\log\rho|}\right\rceil
                                                                  \tag{2}
\]
gives, uniformly on \(D_r\),
\[
 \left\|N(W-P_{K_N}W)\right\|_{C^2}=O(N^{-q-1}),
 \qquad
 { (P_{K_N}A)e^{NP_{K_N}W}\over Ae^{NW}}
       =1+O(N^{-q-1}).                                  \tag{3}
\]
The number of retained coefficients is \(2(K_N+1)^b\).
In particular it is \(O(\log N)\) for one boundary variable,
and \(O((\log N)^2)\) for two. This is a coefficient count,
not a bound on the bit precision needed to store those coefficients.

The amplitude denominator is legitimate by its lower bound.
Equation (3) follows directly from (1), Cauchy, and
\(e^\zeta=1+O(\zeta)\) near zero. A packet
\(\epsilon_NN^\alpha Ae^{NW}(1+O(N^{-1}))\) consequently has
the same leading packet after this replacement. Any fixed number
of already known higher amplitude coefficients can be truncated
in the same way when a specified higher asymptotic order is wanted.

There is also a useful local contraction consequence. Suppose an
already justified local stationary integral has an interior critical
point, nonzero leading coefficient, and a horizontal Gaussian bound
\[
 \Re\Phi(x)\le\Re\Phi(x^*)-\kappa|x-x^*|^2/2,
 \qquad \kappa>0.                                      \tag{4}
\]
If the truncated packet charts contain that contour with a fixed
buffer, (3) changes its integrand by a relative \(O(N^{-q-1})\).
Its absolute integral is \(O(e^{N\Re\Phi(x^*)}N^{-d/2})\),
apart from the unchanged prescribed scalar powers. The original
Gaussian integral has a nonzero coefficient at this same scale.
Thus its leading coefficient and calibrated action survive the
replacement. This argument uses the same local contour; it requires
neither a new critical point nor a new choice of logarithmic lift.
For a fixed finite product the relative errors add at the same order.

For every fixed positive mixed open word, the
[original local Gaussian theorem](research_mixed_open_local_gaussian.md)
already supplies precisely such a nonzero packet with holomorphic
ordinary-color phase and amplitude. On smaller color bidisks,
Proposition 1 therefore represents that proved local contribution
by \(O((\log N)^2)\) coefficients. Where the
[finite-kernel closure theorem](research_finite_two_boundary_kernel_closure.md)
proves a local contraction on retained charts, the preceding
contraction argument applies as well. Constants here may depend on
the fixed word and its charts; no uniformity in word length or in
shrinking charts is asserted. No complementary Fourier current has
been included by this compression.

## 2. Why the transported remainder is separate

This distinction can be made exact in the original source algebra.
Write \(D=N-1\), let \(\mathsf T e_j=e_{D-j}\) be the
original Newton turn, and fix a signed integer \(|p|\ge2\).
Put
\[
 r_N=\operatorname{can}(R^p),\qquad
 H_N=\mathsf T r_N.                                    \tag{5}
\]
The [complete terminal theorem](research_uniform_terminal_family_and_star_fillings.md)
gives a nonzero packet for \(H_N\), with positive complete rate
\(M_p\). Its even angular phase and amplitude descend to
holomorphic ordinary-color germs near \(z=-2\).

**Proposition 2.** Along odd levels, for any integer sequence
\(K_N=O(\log N)\), there are canonical polynomials \(E_N\)
such that:

* all ordinary-color jets of \(E_N\) through order \(K_N\)
  vanish at \(-2\);
* on one fixed complex disk about \(-2\), \(E_N/H_N\)
  is exponentially small;
* nevertheless \((\mathsf T E_N)(-2)=H_N(-2)\).

To prove this, let \(P_N\) be the degree-\(K_N\) Taylor
polynomial of \(r_N\) at \(-2\), and set
\(E_N=r_N-P_N\). For sufficiently large odd \(N\),
\(K_N<L=(N-1)/2\). Every polynomial of degree at most \(K_N\)
lies in \(\operatorname{span}(e_0,\ldots,e_{K_N})\).
Since \(c_L=-2\), every \(e_j(-2)\) with \(j>L\) vanishes.
Consequently
\[
 (\mathsf T P_N)(-2)=0,
 \qquad(\mathsf T E_N)(-2)=H_N(-2).                    \tag{6}
\]
These statements retain the full algebra and its repeated-root
normal data; they do not replace the turn by evaluation on its
semisimple quotient.

The original full-Hermite norm bounds in
[the finite-source estimates](../papers/circle-tree-volume/finite-bounds.tex)
give \(\|r_N\|_{[-2,2]}\le CN^A\) for fixed \(p\).
Iterated Markov inequalities therefore give
\[
 |r_N^{(k)}(-2)|\le CN^{A+2k},\qquad
 \|P_N\|_{|z+2|\le\delta}
          \le\exp(O(K_N\log N+\log N))=\exp(o(N))       \tag{7}
\]
for every fixed \(\delta\). For completeness the small complex
disk estimate for \(r_N\) follows from its Chebyshev expansion:
its coefficients are bounded by \(2CN^A\), and
\[
 |T_j(z/2)|\le e^{jG(z)},\qquad
 G(z)=\log\max\{|\xi|:\xi+\xi^{-1}=z\}.               \tag{8}
\]
Here \(G\) is continuous and \(G(-2)=0\). For any
\(0<\varepsilon<M_p/3\), choose a fixed disk on which
\(G<\varepsilon\), the terminal packet is valid, and its
phase has real part greater than \(M_p-\varepsilon\).
Equations (7)--(8) prove
\(|E_N/H_N|\le\exp(-(M_p-2\varepsilon)N+o(N))\).
This proves Proposition 2.

In particular \(H_N\) and \(H_N+E_N\) have identical
\(K_N\)-jets and the same local asymptotic phase, amplitude and
every already established algebraic-order expansion. Their turned
complete values have different exponential rates:
\[
 (\mathsf T H_N)(-2)=r_N(-2),\quad |r_N(-2)|=1,
 \qquad
 (\mathsf T(H_N+E_N))(-2)=r_N(-2)+H_N(-2).             \tag{9}
\]
The rates are respectively \(0\) and \(M_p\). The unit
physical crossing value and \(\mathsf T^2=I\) are the original
[crossing and turn identities](research_boundary_crossing_packet_preservation.md),
Section 7. The level-dependent Taylor modification is not claimed
to be the source of a fixed literal tangle. Thus (9) obstructs an
inference from the abstract packet and finite jets; it is not an
adverse knot or short-filling example.

## 3. The next source estimate

Local optimization, Schur concavity and logarithmic germ compression
can preserve a geometric packet on a retained chart. To propagate
its dominance through a short original operation \(\mathcal C_N\),
one still needs a bound on its complementary source \(E_N\) of
the form
\[
 |\mathcal C_N E_N(w)|
       \le N^A\exp N\{\Re W_{\rm new}(w)-\gamma\},
 \qquad\gamma>0,                                      \tag{10}
\]
on the required output chart or after the actual prescribed closing
functional, together with the nonzero local coefficient at that
same calibrated action. At a branch, (10) must bound the complete
sum of terms containing at least one complementary factor.
An input-chart bound for \(E_N\) alone is insufficient by (6).
The [finite boundary-window reduction](research_mixed_open_finite_boundary_windows.md)
retains exactly these literal end sources and currents. Establishing
their joint inequalities, or an operation-specific version of (10),
is the next analytic step. No fixed-dimensional exact compression
is needed for the already proved local contribution.
