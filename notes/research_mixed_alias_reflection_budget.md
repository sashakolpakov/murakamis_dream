# A local height budget for every wrapped outer alias

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

Reflecting the heights of any nonempty subset of the four-weighted outer
variables gives a strict local rate loss for the original factorial
density, even after retaining the actual Fourier weight \(d_N\).
The estimate concerns that local density. It does not control the full
conditional kernels or the complementary part of an outer torus.

## 1. The exact density and the selected geometric point

Use the contracted phase \(\mathcal F\) and exact interpolant
\(\mathcal T_N\) of
[the full contracted source](research_mixed_contracted_phase.md). In its
regular strip, with cyclic indices,
\[
 \mathcal F(\mathbf s,\mathbf t)
 =\sum_v\{g(s_v+t_v)+g(t_v+s_{v+1})
          -(2+\epsilon_v)[g(s_v)+g(t_v)]
                                  +2\pi i t_vs_{v+1}\},
 \quad
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}.
 \tag{1}
\]
This equals the previously calibrated \(H+i\Theta\) exactly, with
the same logarithmic lifts. Let \((\mathbf s^*,\mathbf t^*)\) be the
actual cyclic critical point and write \(M=\Re\mathcal F(\mathbf s^*,\mathbf t^*)\).
The [height theorem](research_mixed_cyclic_critical_height_bounds.md) gives,
at every four-type outer leg,
\[
 t_v^*=x_v-iH_v,\qquad .27<x_v<.33,\qquad .001<H_v<.057.
 \tag{2}
\]
Every internal real index lies in \((.23,.45)\).

For a subset \(S\) of the four-type outer variables, the exact local
factorial interpolation of its term in the
[torus identity](research_mixed_conditional_torus_composition.md) is
\[
 \mathcal D_{S,N}
 =N^m\mathcal T_N(\mathbf s,\mathbf t)
   \prod_{\epsilon_v=1}
       \{\widehat P_N(Nt_v)d_N(e^{-2\pi it_v})\}
   \prod_{v\in S}e^{2\pi iNt_v}.
 \tag{3}
\]
The outer factor \(N^m\) is the exact root-average factor. All
\(\kappa\), level powers, and the order-one carrier remain in
\(\mathcal T_N\). To verify (3), write each conditional kernel row
as its ratio of three marked factorials, multiply the kernels, and
replace exactly one reciprocal factorial at each four-weighted outer
variable by \(d_N\). This is an identity before asymptotics on the
regular local index chart. It is not an asymptotic for the full sum over
the internal indices.

## 2. The reflected phase cost

Reflect only the variables in \(S\): keep all internal coordinates and
all other outer coordinates fixed at the critical point, and send
\(t_v^*=x_v-iH_v\) to \(t_v^+=x_v+iH_v\) for \(v\in S\).
The regular factorial strips persist along the straight height paths.
There are no outer--outer Hessian entries in (1), including for a
one-vertex cycle; the two incident terms are still counted separately.
For a moving four-type coordinate,
\[
 \mathcal F_{t_vt_v}
  =\pi\cot\pi(s_v+t_v)+\pi\cot\pi(t_v+s_{v+1})
                                      -3\pi\cot\pi t_v+i\pi.
 \tag{4}
\]
Both incident real sums belong to \([.50,.78]\), while
\(\Re t_v\in[.27,.33]\). The formula for the real part of a cotangent
therefore gives, at every intermediate height,
\[
 -\Re\mathcal F_{t_vt_v}
 \le \pi\{3\cot(.27\pi)+2\cot(.22\pi)\}<16.
 \tag{5}
\]
The first variation vanishes at the actual critical point. Integrating
the diagonal second variation over the simultaneous height change gives
\[
 \Re\mathcal F(\mathbf s^*,\mathbf t^+)-M
                              \le32\sum_{v\in S}H_v^2.
 \tag{6}
\]
This bound is independent of the length and of the number or placement
of reflected variables.

## 3. Retaining the true Fourier weights

Put \(\nu(z)=-\Re g(z)\). The
[whole-strip weight bound](research_mixed_fourier_weight_continuation.md)
gives, on every fixed compact strip set and for every \(\eta>0\),
\[
 |d_N(e^{-2\pi iz})|
 \le C_\eta N^{-1/2}
       e^{N[\max\{\nu(z),2\pi\max(\Im z,0)\}+\eta]}.
 \tag{7}
\]
At unreflected four-type coordinates the proved relative comparison
with \(1/\widehat P_N(Nt_v)\) is valid on the entire containing
rectangle. Those factors in (3) are uniformly bounded, with no rate
cost. At a reflected coordinate (7), the factorial symbol, and the
wrapped factor give the extra rate
\[
 \max\{0,2\pi H-\nu(x+iH)\}-2\pi H+\eta
                    =-\min\{2\pi H,\nu(x+iH)\}+\eta.
 \tag{8}
\]
Thus this proof does not assume that the relative reciprocal-factorial
approximation survives the reflection.

The same weight proof gives the elementary bounds
\[
 \begin{split}
 \nu(x-iH)&\ge\frac{\sin(2\pi x)}{2\pi}
                          \log(1+e^{-2\pi H}),\\
 \nu(x+iH)&=\nu(x-iH)+\pi H(1-2x).
 \end{split}
 \tag{9}
\]
Since \(x\in[.27,.33]\) and
\(\log(1+e^{-2\pi H})\ge\log2-\pi H\), it follows that
\[
 \nu(x+iH)\ge c_0+c_1H,\qquad
 c_0=\frac{\sin(.66\pi)\log2}{2\pi},\qquad
 c_1=.34\pi-\frac{\sin(.66\pi)}2.
 \tag{10}
\]
For every \(0\le H\le.057\),
\[
             \min\{2\pi H,\nu(x+iH)\}-32H^2\ge H/2,
 \tag{11}
\]
with strict inequality when \(H>0\). For the first entry of the
minimum, divide by \(H\) and use
\(2\pi-1/2-32(.057)>0\). For the other, the concave quadratic
\(c_0+(c_1-1/2)H-32H^2\) has its minimum at an endpoint. At zero
it is positive; at \(.057\) its outward lower bound exceeds
\(.0001135\). This proves (11) on the whole interval.

**Proposition 1.** For every fixed cyclic mixed word and every nonempty
alias subset \(S\), the exact density (3) at the reflected geometric
coordinates satisfies
\[
 |\mathcal D_{S,N}(\mathbf s^*,\mathbf t^+)|
    \le C N^C e^{N[M-|S|/4000]}.
 \tag{12}
\]
The same bound with \(|S|/8000\) holds on a fixed small real
neighborhood of those coordinates on the reflected local chain.

*Proof.* Use (7) with \(\eta=1/8000\) only at the reflected weights.
Combine (6), (8), and (11). Since \(H_v\ge1/1000\), the resulting
loss is strictly greater than \(\sum_{v\in S}H_v/4\), hence at
least \(|S|/4000\). All remaining exact factorial symbols and
unreflected weight ratios cost only polynomial or bounded factors.
The rate functions are continuous on the compact regular chart, so a
fixed neighborhood retains half this strict loss. For a fixed word
there are finitely many subsets; its neighborhoods may be chosen
simultaneously. \(\square\)

## 4. Scope and reproduction

The reflected circles are legal radii for the exact Laurent torus
identity. Proposition 1 controls their selected local factorial
density with the actual Fourier weights. It does not control the rest
of those circles, the internal conditional tails at reflected outer
parameters, or the connectors of a truncated local decomposition.
Those estimates are required before concluding that a complete wrapped
alias integral is subdominant. No observed-word lower bound follows
from this local budget alone.

Run the focused exact/outward checks with:

    python3 experiments/check_mixed_alias_reflection_budget.py

They check the phase conversion, the absence of outer--outer quadratic
terms, and the uniform scalar reserves in (5) and (11). The source
identity and the global weight upper bound remain explicit proof
dependencies.
