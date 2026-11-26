# An odd-level whole-hub bound at the original probe action

Private theorem, 1 November 2026. No repository file is changed.

This proves a full output estimate for one unturned multiplication hub of any fixed valence. The inputs are arbitrary complex coefficient arrays in the established effective-leaf cone. The estimate is at the original intrinsic action of the turned product, not at an enlarged absolute return envelope. Its clean low-coordinate part has the old positive coefficient majorant, while every other contribution has a strict spectral-norm deficit. The theorem is at odd levels. It does not reset a general type-A child to an effective-leaf cone or automatically iterate a component with further internal turns.

The exact signed low-hub input is `/private/tmp/md-odd-level-low-newton-hub-trace-comparison.md`. The complete geometric pressure comparison is Appendix A of `notes/actual_conway_unflagged_probe_geometry.md`. The old high-sector comparison is `notes/actual_conway_unflagged_core_probe_bound.md`. All three roles are distinguished below.

## 1. Inputs, output, and the two intrinsic pressures

Let \(N\) tend to infinity through odd integers, \(d=N-1\), \(M=d/2\), and fix \(R<1\). The fixed complete Newton polynomials are \(e_0,\ldots,e_d\), and the multiplication relation is
\[
P_s=P_0+\Delta_s,\qquad \Delta_s=2\cos(2\pi s)-2,
\qquad |s|\le R.
\]
Use the full complete spectral-jet norm \(\|\cdot\|_{\mathrm J}\). Define
\[
J(u)=\int_0^u\log(2\sin\pi v)\,dv,
\qquad g(u)=J(2u)-4J(u),\qquad G_0=g(1/4)>0.
\tag{1}
\]
Here \(g\) is used on \([0,1/2]\), where its maximum is \(G_0\).

Fix an integer \(B\ge2\). Suppose
\[
F_{b,N}(s)=\sum_{r=0}^d f_{b,N,r}(s)e_r,
\qquad 1\le b\le B,
\]
are arbitrary complex arrays satisfying, uniformly in the specified parameters,
\[
|f_{b,N,r}(s)|\le
\begin{cases}
\exp\{N(c_b+g(r/N)+\epsilon_N)\},&r\le M,\\
\exp\{N(c_b+\epsilon_N)\},&r>M,
\end{cases}
\qquad \epsilon_N\longrightarrow0.
\tag{2}
\]
The constants \(c_b\) are fixed. No sign, root location, or physical alias identity is assumed for these arrays. Their product and its actual fixed-frame turn are
\[
A_N(s)=F_{1,N}*_s\cdots *_sF_{B,N},\qquad
Q_N(s)=\mathscr T_s^{\mathrm{fix}}A_N(s).
\tag{3}
\]
The typed turn is the proved weighted reversal, with its scalar retained.

The positive complete reference uses
\[
h_N=\sum_{r=0}^{M}\frac{N^2S_{2r}}{S_r^4}e_r,
\qquad A^0_{B,N}=h_N^B,
\qquad Q^0_{B,N}=T_0(h_N^B)=\sum_{r=0}^d q^0_{B,N,r}e_r.
\tag{4}
\]
The product in (4) is in the complete quotient. Every coefficient \(q^0_{B,N,r}\) is nonnegative. Let \(f_B(x)\) be the original positive coefficient action of the unturned product \(h^B\), including the exact old support. Define
\[
\begin{aligned}
\omega_B&=\max_{0\le x\le1/2}\{f_B(x)+g(x)\},\\
\widehat\omega_B&=\max_{0\le x\le1/2}\{f_B(1-x)+g(x)\},\\
\Omega_A&=\sum_bc_b+\omega_B,\qquad
\Omega_Q=\sum_bc_b+\widehat\omega_B.
\end{aligned}
\tag{5}
\]
Thus \(\Omega_Q\) is the original intrinsic low-probe action of the turned hub, equivalently the complete closing action of \(C(hh^B)\), with all effective-leaf constants added. It is not a newly chosen norm budget.

The exact classical comparison needed below is
\[
\omega_B=2BG_0,\qquad
\widehat\omega_2=4G_0,\qquad
\delta_B:=\widehat\omega_B-2BG_0>0\quad(B\ge3).
\tag{6}
\]
A proof is given in Section 2.

**Theorem.** There is \(\gamma_{B,R}>0\) and a uniform error \(o(1)\) such that
\[
\|Q_N(s)\|_{\mathrm J}\le\exp\{N(\Omega_Q+o(1))\}.
\tag{7}
\]
More precisely, let \(Q_N^{\mathrm{clean,lo}}\) be the low-coordinate part of the output when every input in (3) is restricted to its low coordinates. Then
\[
\left|[e_r]Q_N^{\mathrm{clean,lo}}\right|
\le \exp\{N(\sum_bc_b+o(1))\}\,q^0_{B,N,r}
\quad(0\le r\le M),
\tag{8}
\]
and
\[
\|Q_N-Q_N^{\mathrm{clean,lo}}\|_{\mathrm J}
\le\exp\{N(\Omega_Q-\gamma_{B,R})\}.
\tag{9}
\]
Thus all high outputs and every contribution with a high input have a strict deficit. The clean term has an actual old positive coordinate majorant, not merely a spectral norm bound.

## 2. Why these are the original pressures

At odd levels, \(-2\) is the simple complete Casimir node. All high Newton polynomials vanish there, and all low ones are positive. Consequently the exact equality
\[
\sum_{r=0}^{M}[e_r]A^0_{B,N}\,e_r(-2)
=A^0_{B,N}(-2)=h_N(-2)^B.
\tag{10}
\]
retains only the original low coefficient sum. The uniform low coefficient and basis rates are both \(g\). The positive sum for \(h_N(-2)\) therefore has rate \(2G_0\). Applying the established positive coefficient Laplace principle to the left side of (10) gives \(\omega_B=2BG_0\). This also follows directly from the same finite positive state sum; no deformed norm is used to calibrate it.

For the pressure comparison, associate the last binary gate of the unturned product as \(h^{B-1}\cdot h\). For \(B=2\), its two inputs have rigid type L. For \(B\ge3\), the first is a completed type-A product and the second is type L. The original product equations give
\[
f_B'(x)\ge f_2'(x)\quad(0<x<1),
\tag{11}
\]
strictly when \(B\ge3\). To recall the actual geometric inequality, write \(B_x=\cot\pi x\) for the output cotangent and \(X,Y\) for the positive boundary parameters. The unsquared product relation is
\[
Y^2=(B_1-B_x)(B_2-B_x)\le(X-B_x)^2,
\qquad B_x<B_i\le X.
\]
Together with \(Y^2=1+B_x^2-X^2\), it gives
\[
X\ge X_2(B_x)=\frac{B_x+\sqrt{B_x^2+2}}2,
\qquad f_B'(x)\ge2\log(2X_2(B_x)^2)=f_2'(x).
\tag{12}
\]
One inequality is strict if an input is type A. All additive constants differentiate to zero and have already been retained in (5).

Since \(X_2(B)X_2(-B)=1/2\), the two-leaf profile is symmetric:
\(f_2(x)=f_2(1-x)\). Integrating (11) between \(x\) and \(1-x\) therefore proves
\[
f_B(1-x)\ge f_B(x)\quad(0<x<1/2),
\tag{13}
\]
strictly for \(B\ge3\). The intrinsic positive probe has a maximizer in \((0,1/2)\): its value at zero is zero and it has positive interior values, while the logarithmically negative derivative of \(g\) excludes the upper endpoint (the profile \(f_B\) is regular there). Evaluating the left-hand pressure at this maximizer proves strict \(\widehat\omega_B>\omega_B\) for \(B\ge3\). For \(B=2\), symmetry gives equality. This proves (6).

## 3. Low outputs with all inputs low: preserve the signed hub

The exact odd-level Fourier trace theorem gives, for any fixed number of low-coordinate arrays,
\[
\left|\phi_s\left(e_r\prod_bF_{b,N}^{\mathrm{lo}}\right)\right|
\le C_{B,R}\phi_0\left(e_r\prod_b(F_{b,N}^{\mathrm{lo}})^{\mathrm{abs}}\right),
\qquad r\le M.
\tag{14}
\]
The left product is reduced in the moving quotient only for taking the trace. This estimate sums all return contributions before the absolute value. Its proof uses the nonnegative symmetric unimodal Laurent coefficients of each low Newton basis factor and the exact finite Fourier formula; it does not compare individual return terms.

The positive reference coefficients in (4) have the uniform closed rate \(g(r/N)+O(\log N/N)\). Equation (2) therefore gives
\[
(F_{b,N}^{\mathrm{lo}})^{\mathrm{abs}}
\le N^{C}\exp\{N(c_b+\epsilon_N)\}\,h_N.
\tag{15}
\]
coefficientwise. The old multiplication and trace are positive. Apply (15) to the right side of (14), and use the exact coefficient extractor for the fixed-frame turn:
\[
[e_r]Q_N^{\mathrm{clean,lo}}
=\frac{\gamma_N(s)W_{d-r}(s)}{H_N(s)}
 \phi_s\left(e_r\prod_bF_{b,N}^{\mathrm{lo}}\right).
\tag{16}
\]
The paired scalar in (16) is uniformly bounded on \(|s|\le R<1\). Since \(B\) is fixed, all polynomial factors and \(B\epsilon_N\) can be absorbed in one uniform \(o(1)\). This proves (8).

The low-coordinate norm satisfies the original positive-probe bound
\[
\|Q_N^{\mathrm{clean,lo}}\|_{\mathrm J}
\le\operatorname{poly}(N)\sum_{r\le M}e_r(-2)
             |[e_r]Q_N^{\mathrm{clean,lo}}|
\le\exp\{N(\Omega_Q+o(1))\}.
\tag{17}
\]
The reference weighted sum has precisely the second action in (5).

## 4. The other sectors and the exceptional two-input cases

The canonical sup norm, complete spectral-jet norm, and Chebyshev coefficient norm are polynomially equivalent at degree less than \(N\). Fixed-valence quotient multiplication modulo \(P_s\) has polynomial norm cost on every bounded parameter disk, by exact Chebyshev folding. The top-coefficient functional also has polynomial cost. These facts give, for any specified input-band assignment with \(h\) high inputs,
\[
\|A_{N,\mathrm{band}}(s)\|_{\mathrm J}
\le\exp\left\{N\left[\sum_bc_b+2(B-h)G_0+o(1)\right]\right\}.
\tag{18}
\]
Indeed a low input has norm at most \(\exp\{N(c_b+2G_0+o(1))\}\), while a high input has norm at most \(\exp\{N(c_b+o(1))\}\). The latter uses the polynomial full-normal norm of every high complete Newton basis element, not its zero node values alone.

For a high output \(r>M\), insert the polynomially bounded \(e_r\) in the exact trace extractor. The basis element at that output also has polynomial norm. Summing the finitely many coordinates gives
\[
\|Q_{N,\mathrm{band}}^{\mathrm{hi}}\|_{\mathrm J}
\le\exp\left\{N\left[\sum_bc_b+2(B-h)G_0+o(1)\right]\right\}.
\tag{19}
\]
For a low output, the trace insertion and the subsequent reconstruction each cost at most \(\exp(NG_0)\). Hence
\[
\|Q_{N,\mathrm{band}}^{\mathrm{lo}}\|_{\mathrm J}
\le\exp\left\{N\left[\sum_bc_b+2(B-h+1)G_0+o(1)\right]\right\}.
\tag{20}
\]
These estimates retain signs within the polynomial products; no positive moving-Newton multiplication majorant is used.

If \(B\ge3\), (19) with \(h=0\) has rate \(\Omega_A<\Omega_Q\). If \(h\ge1\), (20) has rate at most \(\Omega_A\), and (19) is even smaller. Thus every sector covered by (9) has a fixed loss at least \(\delta_B\) before absorbing its uniform errors. The finitely many band choices cost no exponential factor.

When \(B=2\), \(\Omega_A=\Omega_Q\), so two cases require their actual source support rather than this strict pressure comparison.

1. If both inputs are low, their ordinary polynomial product has degree at most \(2M=d<N\). There is no return correction. The high-output positive majorant is exactly the old high-probe sector, with the outgoing paired factors bounded coefficientwise. The established isolated three-leaf high-probe estimate has a fixed strict gap below \(4G_0+\sum c_b\).

2. If exactly one input is high and the output is low, the cubic trace has two low incident indices. A return vertex requires all pair sums at least \(N\), whereas those two low indices have sum at most \(2M=d\). Thus this particular scalar has no return term. Its remaining complete positive majorant is an old sector with one high effective input, which has the established strict high-sector gap. This statement concerns low output only.

3. If exactly one input is high and the output is high, returns are allowed. They are controlled by (19), which saves \(2G_0\) relative to \(\Omega_Q\). They are not excluded by the preceding two-low support observation.

4. If both inputs are high, (20) is at most \(\sum c_b+2G_0\), again strictly below \(\Omega_Q=\sum c_b+4G_0\); (19) is smaller still.

The old two-input gaps invoked in cases 1–2 are upper statements for arbitrary coefficient-cone arrays. They use the exact complete positive kernel and the isolated three-leaf comparison, including its true target and both finite support endpoints. No physical alias relation is assumed for the present arrays.

Choose a smaller fixed gap than the positive minima just obtained, and absorb the uniform errors and fixed number of sectors. This proves (9), and then (7).

## 5. The usable invariant and its limit

The conclusion has two separate parts: an old positive low-coordinate majorant (8), and a spectrally small remainder (9). The usual original low-output localization of the reference probe therefore passes to the clean majorant without changing its maximizing interval. This is stronger than the whole output norm alone.

It is not a free replacement of an arbitrary completed child by an effective leaf with profile \(g+c\). A general type-A output has its own old boundary coefficient profile, and a \(\mathrm J\)-small remainder need not save a full \(2G_0\) when inserted at a later hub. Iteration through an arbitrary connected unflagged component needs an invariant that tracks that old low-coordinate profile and the remaining error budget across the next product and turn. No such iteration is asserted here. Even-level all-low low-output comparison is also a separate Fourier-sign problem; all other estimates above are parity-independent once their original complete profiles are supplied.
