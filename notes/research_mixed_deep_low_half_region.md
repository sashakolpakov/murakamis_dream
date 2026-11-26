# Raising real low coordinates on the original contour

Research theorem, 5 November 2026. This extends the proved half-period
region down to the fixed near-zero collar. It permits arbitrary mixtures
of low, transition and plateau coordinates. The collar itself and
coordinates in the right half of the period remain outside this result.
The manuscripts are unchanged.

The new argument is an elementary derivative calculation for the
complete conditional action. It requires no additional interval cover.
It compares actions at two points of the existing contour; it does not
change variables in the integral or compare individual summands.

## 1. A monotonicity property of the conditional action

For type indicators \(\eta,\epsilon\in\{0,1\}\), let
\[
\begin{split}
 g(z)&=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},\\
 Q_\epsilon(s;a,b)&=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,\\
 \phi_{\eta\epsilon}(a,b)&=Q_\epsilon(s_*;a,b)
              -(1+\eta/2)g(a)-(1+\epsilon/2)g(b),\\
 f_{\eta\epsilon}(a,b)&=\Re\phi_{\eta\epsilon}(a,b).
                                                        \tag{1}
\end{split}
\]
Throughout this section \(0<a,b\le1/2\). The conditional critical
point \(s_*\) is the original zero-logarithmic-lift root. The
[closed real half-period theorem](research_mixed_half_endpoint_conditional_packet.md),
Lemma 1, proves that
\[
 S=\cot(\pi s_*)=u+iv,\qquad u>0,\quad -1<v<1.             \tag{2}
\]
This includes either neighbor equal to \(1/2\).

**Lemma 1.** Holding the other real coordinate fixed, the action in (1)
is strictly increasing in either coordinate while that coordinate lies
in \((0,1/6]\).

**Proof.** Put \(p=\cot(\pi a)\), \(q=\cot(\pi b)\).
Stationarity \(Q_{\epsilon,s}(s_*;a,b)=0\) removes the derivative
of \(s_*\) from the first derivative of the critical value. Since
\(g'(z)=\log(1-e^{-2\pi iz})\) on the original strip, elementary
cotangent identities give
\[
\begin{split}
 f_a&=\log\frac{|S+p|}{|S-i|}
                      -\frac\eta2\log(2\sin\pi a),\\
 f_b&=\log\frac{|S+q|}{|S+i|}
                      -\frac\epsilon2\log(2\sin\pi b).
                                                        \tag{3}
\end{split}
\]
The denominators differ because the original chirp is \(2\pi ias\).
For example, with \(U=e^{-2\pi is_*}=(S-i)/(S+i)\) and
\(A=e^{-2\pi ia}=(p-i)/(p+i)\),
\[
 \frac{1-UA}{1-A}=\frac{S+p}{S+i}.
\]
The real part of the chirp derivative subtracts
\(2\pi\Im s_* =\log|U|\), replacing \(|S+i|\) by
\(|S-i|\) in the first line of (3).

If \(a\le1/6\), then \(p\ge\sqrt3\) and
\[
 |S+p|^2-|S-i|^2
   =2up+p^2+2v-1
   =2up+(p^2-3)+2(v+1)>0.                                 \tag{4}
\]
Also \(0<2\sin\pi a\le1\). Both terms in the first line of
(3) are therefore nonnegative, and the first is strictly positive.
For \(b\le1/6\) the corresponding identity is
\[
 |S+q|^2-|S+i|^2
   =2uq+q^2-2v-1
   =2uq+(q^2-3)+2(1-v)>0.                                 \tag{5}
\]
This proves the second assertion. All logarithmic moduli are finite
by (2). No boundary root at a zero coordinate is invoked. \(\square\)

## 2. Raising the low coordinates leaves every height unchanged

Fix a cyclic word of length \(m\ge1\), its actual geometric reference
\(r\), and an allowed selection \(\sigma\). Use exactly the
[periodic hybrid contour](research_mixed_split_cutoff_hybrid_contour.md),
with a fixed collar width \(0<\rho\le1/1000\). On
\([\rho,1/2]\), its row-dependent left cutoff is
\[
 L_b(x)=\begin{cases}
 0,&\rho\le x\le1/10,\\
 (x-1/10)/(b-1/10),&1/10\le x\le b,\\
 1,&b\le x\le1/2.
 \end{cases}                                               \tag{6}
\]
Here \(b=11/50\) in an unselected row and \(b=3/25\) in a
selected row. If \(h_j\) is the prescribed reference height in an
unselected row, or \(7/500\) in a selected row, its actual target is
\[
 z_j=x_j+i h_jR_\rho(x_j)
       \min\{L_{b_j}(x_{j-1}),L_{b_j}(x_j),L_{b_j}(x_{j+1})\}.
                                                        \tag{7}
\]
The function \(R_\rho\) is the unchanged right and near-zero factor
of the hybrid definition. Its value below \(1/10\) will not enter
the argument, because the minimum there is zero.

Define \(\widehat x_j=\max\{x_j,1/10\}\). Every coordinate
that moves from \(x_j\) to \(\widehat x_j\) stays inside the
zero interval of every left cutoff in (6). Its own target and both
neighboring targets consequently have height zero throughout that
motion. All other targets retain their heights. Thus the initial and
final points, and the intermediate motions, lie on the same prescribed
hybrid graph with exactly the same vector of heights.

Let
\[
 \mathcal E_\sigma(x)=
   \Re\sum_j\phi_{\epsilon_{j-1},\epsilon_j}(z_{j-1},z_j)
   +\sum_j\sigma_j\chi(z_j),\qquad
 \chi(z)=\max\{\Re g(z),-2\pi\Im z\}.                    \tag{8}
\]
This is the original complete upper phase, retaining both selected
Fourier alternatives. At a real coordinate in \((0,1/2]\),
\(\Re g(x)\le0\), so \(\chi(x)=0\).

Raise the low coordinates successively. Only the two incident blocks
change, and both of their arguments are real. Each relevant derivative
is positive by Lemma 1, since the moving coordinate is at most
\(1/10<1/6\). No selected correction changes. Hence
\[
             \mathcal E_\sigma(x)
                \le \mathcal E_\sigma(\widehat x).          \tag{9}
\]
For a one-cycle, the derivative is the sum of the two partial
derivatives of its single diagonal block. For a two-cycle the two
original edges remain distinct. Thus (9) includes both short periods.

## 3. The additive phase bound on the larger region

Write \(a_j=\Re r_j\), \(P=[11/50,9/20]\), and
\[
 y_j=\max\{11/50,\min\{x_j,9/20\}\},\qquad
 p_j=\min\{1,\sigma_j+400(y_j-a_j)^2\},\qquad
 \omega_j=\frac{p_j}{4000}+\frac1{10}(x_j-9/20)_+.          \tag{10}
\]
Let \(M=\Re\sum_j\phi_j(r_{j-1},r_j)\). The established
[additive phase theorem](research_mixed_nonlow_occupation_loss.md),
with the sharper constant in the
[curvature extraction](research_mixed_extracted_plateau_curvature.md),
applies to \(\widehat x\in[1/10,1/2]^m\). The operation
\(x\mapsto\widehat x\) changes none of the quantities in (10).
Together with (9), this proves
\[
 \mathcal E_\sigma(x)\le M-\sum_j\omega_j,
                  \qquad x\in[\rho,1/2]^m.                \tag{11}
\]
In particular, a selected coordinate or a coordinate outside \(P\)
supplies a loss of at least \(1/4000\). This uses the proved
reference bounds \(.27<a_j<.39\): a coordinate clamped to the
left endpoint of \(P\) is more than \(.05\) from \(a_j\),
and one clamped to the right endpoint is more than \(.06\) away.

## 4. Consequence for the original finite integral

Let \(\mathcal Z_N(D)\) denote the sum of the original selected
integrals restricted to a real parameter region \(D\) on this hybrid
graph. Let \(\mathcal I_{N,\varnothing}(P^m)\) be its unselected
central integral. These are the same normalizations as in the
[nonlow half-period theorem](research_mixed_full_nonlow_half_region.md).

**Theorem 2.** For every fixed word and fixed collar \(\rho\),
there are finite constants \(C,A\) such that, at all sufficiently
large integer levels of either parity,
\[
 \left|\mathcal Z_N([\rho,1/2]^m)
                -\mathcal I_{N,\varnothing}(P^m)\right|
       \le C N^A e^{N(M-1/8000)}.                           \tag{12}
\]
Thus this larger restricted integral retains the central nonzero
coefficient and its original exponential action.

**Proof.** A block incident to a coordinate below \(1/10\) has
two real targets in the fixed compact square \([\rho,1/2]^2\).
The half-period conditional packet cited in Section 1 applies on that
entire square, including \(1/2\). Divide by its two original
factorial interpolants and use the
[Fourier-polynomial upper bound](research_mixed_fourier_weight_continuation.md).
It gives the complete allocated block modulus at rate
\(\Re\phi_j\), with a polynomial factor and any prescribed
positive exponential tolerance. At \(1/2\), where the Fourier
exponents tie, only the proved absolute upper bound is used; a relative
Fourier expansion is unnecessary.

Every other block has its four-coordinate height data inside the
previously proved nonlow source domains. Indeed replacing a low halo
coordinate by \(1/10\) leaves its cutoff equal to zero and leaves
both target heights unchanged. The complete source estimates used in
the nonlow half-period theorem therefore apply to these blocks, with
the true selected corrections in (8). All bounds are uniform on the
finitely many closed pieces for this fixed \(\rho\) and word.

Multiply the allocated moduli, restoring every original Fourier
weight once. Outside the unselected plateau, (11) gives loss at least
\(1/4000\). Choose the tolerance for each of the \(m\) blocks
strictly below \(1/(8000m)\). The full product then has finite loss
at least \(1/8000\). The hybrid Jacobian is bounded for fixed
\(\rho\), and its remaining normalization factors have only
polynomial size. Integration over a bounded parameter set and summation
over the finitely many selections prove (12). \(\square\)

This proof never asserts that the individual rows increase with the
low coordinate. Lemma 1 concerns the critical value of the complete
conditional sum, whose finite upper estimate is an established input.
The comparison map is not used as an integral substitution.

The constants in (12) may depend on \(\rho\). This is not a uniform
argument as \(\rho\downarrow0\). Near-zero seam configurations and
configurations containing a coordinate above \(1/2\) still require
their own estimates. In particular, (12) proves neither survival over
the entire period nor stability under arbitrary short partial fillings.

Reproduction:

```sh
python3 experiments/check_mixed_deep_low_half_region.py
```

The checker verifies the cotangent identities, exact cutoff and loss
arithmetic, and current source provenance. The general monotonicity,
height-preservation and integral arguments are the written proofs above.
