# Global real-spectral gap of the actual all-CROSS source

, 31 October 2026. This estimates the original
CROSS path sectors on the entire real spectral interval. The local bound
is a weighted VALUE bound, not a coefficientwise strict inequality.
The original face Cauchy period and its previously proved angular gap
are retained when sewing. No moving one-sided sector is included.

## 1. Original cofactors and a uniform slow-transfer upper bound

Put $h=1/N$, $s_j=2\sin(\pi jh)$,

$$
\alpha_r(\delta)=4\cos^2\!\left(\pi(r+\tfrac12)h\right)-4\sin^2(\pi\delta),
\qquad A=x+y>0,\quad P=xy\geq0.
$$

where every nonzero face weight lies in a fixed positive compact and
protected zeros stay EXACTLY zero. The terminal indices $n$ below satisfy
$n=N/2+O(1)$ and $n\leq N/2$, with a fixed bound on the $O(1)$. The [literal cofactor](actual_cross_cofactor_factorization.md) has its exact start decomposition

$$
\begin{aligned}
R_n(b,\delta)&=\sum_{i=0}^n b^i\left(\prod_{r=0}^{i-1}\alpha_r(\delta)\right)K_{i,n},\\
K_{i,i}&=1,\qquad K_{i,i-1}=0,\\
K_{i,j}&=s_j^2A K_{i,j-1}+s_js_{j-1}\alpha_{j-1}(\delta)P K_{i,j-2}.
\end{aligned}\tag{1}
$$

This is the original cleared cofactor, without a changed starting row.
For $b=0$ only $i=0$ occurs. Negative $\alpha$ factors are not replaced in the
tail recurrence by their absolute values.

Set $L_{i,j}=K_{i,j}/\prod_{r=i+1}^j s_r$. Its exact transfer matrix is

$$
T_h(t,\delta)=\begin{pmatrix}
2A\sin(\pi t)&4P\left[\cos^2\!\left(\pi(t-h/2)\right)-\sin^2(\pi\delta)\right]\\
1&0
\end{pmatrix},\qquad t=jh.\tag{2}
$$

For real $0\leq\delta\leq1/2$ its limiting spectral radius is

$$
\begin{aligned}
\rho(t,\delta)&=A\sin(\pi t)+\sqrt{4P\cos^2(\pi\delta)+(x-y)^2\sin^2(\pi t)},\\
\Lambda(t,\delta)&=2\sin(\pi t)\rho(t,\delta).
\end{aligned}\tag{3}
$$

Indeed the discriminant simplifies to
$4[4P\cos^2(\pi\delta)+(x-y)^2\sin^2(\pi t)]\geq0$. The eigenvalues
are real and the positive root has magnitude at least that of the
other root. In particular

$$
ct\leq\rho(t,\delta)\leq C,\qquad ct^2\leq\Lambda(t,\delta)\leq C,
\qquad0<t\leq\tfrac12.\tag{4}
$$

uniformly in $\delta$, including $x=y$ and $\delta=1/2$. There the limiting
matrix can be defective; no eigenbasis is inverted.

For every $\varepsilon>0$, uniformly in all $i,n$, real $\delta\in[0,1/2]$, and
all large $N$,

$$
|K_{i,n}|\leq\exp\!\left\{N\int_{i/N}^{1/2}\log\Lambda(t,\delta)\,dt+\varepsilon N\right\}.\tag{5}
$$

The same bound, with another $\varepsilon N$ allowance, holds for all face
weights in a sufficiently small FIXED complex neighborhood of their
reference values, with protected zeros still zero, and $\delta$ in a
sufficiently thin FIXED complex strip around the real interval.
The reference $\Lambda$ on the right is evaluated at the real weights
and $\operatorname{Re}\delta$. All choices depend on $\varepsilon$ and the positive compact,
not on the starting row or $N$.

Here are details sufficient to include the degeneracy in this claim.
First restrict $t$ to $[\eta,1/2]$. The spectral radius is bounded below there.
For EVERY real reference matrix $T=T_0(t,\delta)$, Cayley--Hamilton gives

$$
\|T^k\|\leq C_\eta(k+1)\rho(t,\delta)^k,\qquad k\geq1.\tag{6}
$$

For distinct eigenvalues use the power divided difference, a sum of $k$
terms each bounded by $\rho^{k-1}$; the same polynomial identity includes
repeated eigenvalues by its derivative limit. Uniformly bounded $\|T\|$
and $\rho\geq c_\eta$ supply the displayed constant. This is valid even on
the entire coalescing line $x=y$, $\delta=1/2$.

Choose a FIXED block length $k$ so $\log[2C_\eta(k+1)]/k$ is small. On each
block, the exact product differs from the reference constant product
by $O_k(h)$, uniformly in the row and $\delta$. The same finite product
estimate applies after a sufficiently small fixed perturbation of the
face weights and $\delta$. Decrease that perturbation until its error is
at most $C_\eta(k+1)\rho^k$. Multiplying the block estimates and using the
uniform continuity of $\log\rho$ on $[\eta,1/2]$ gives the integral of $\log\rho$
plus the prescribed small per-row error. The finitely many incomplete
blocks cost $o(N)$. Thus no modulus gap, eigenvector condition number,
or n-dependent perturbation disk is used.

On $t<\eta$ use the bounded transfer entries directly, at cost $C^{\eta N}$.
The missing logarithmic integral is bounded in absolute value by
$C\eta\log(2/\eta)$, uniformly, by (4). The additional exact factors $s_j$
have the same elementary endpoint bound. First choose $\eta$ small,
then $k$ large, then the fixed complex perturbation small, and finally
$N$ large. This proves (5). Replacing $n/N$ by $1/2$ costs $o(N)$, since $n$ differs
from $N/2$ by only $O(1)$ and $\Lambda$ is bounded away from zero at $1/2$.

## 2. Uniform prefix sums and the exact maximization

For real $\delta$ the prefix logarithm obeys the uniform upper Riemann bound

$$
\sum_{r<i}\log|\alpha_r(\delta)|
\leq N\int_0^{i/N}\log|4\cos(\pi(t+\delta))\cos(\pi(t-\delta))|\,dt+o(N).\tag{7}
$$

A zero sampled factor makes that summand zero, so it causes no upper
bound problem. To justify uniformity even near the endpoints, truncate
the logarithm from below. The truncated function is jointly continuous
on the compact $(t,\delta)$ rectangle. Its integrals converge uniformly
to the untruncated integrals: the two shifted cosine logarithms have
uniformly integrable singularities. Equivalently the level sets of
$|4\cos(\pi(t+\delta))\cos(\pi(t-\delta))|$ below $r$ have length $O(\sqrt r)$;
integrating their distribution gives the uniform truncation error.
The same argument with $\log(|\alpha|+r)$ proves an arbitrarily small
additional integral error for a sufficiently small fixed COMPLEX
spectral perturbation. No lower bound on the distance to a physical
node is assumed. If $b>0$ is perturbed in a small fixed complex face
neighborhood, $\lvert b_{\mathrm{complex}}\rvert^i/b^i\leq e^{O(\theta N)}$ for $i\leq N$, with $\theta$
the relative neighborhood size. This is absorbed in the same $\varepsilon N$
allowance. A protected $b=0$ stays exactly zero and has only start $0$.

Combining (1), (5), (7), and at most $N+1$ starts gives the uniform
weighted upper rate

$$
\begin{aligned}
\limsup_{N\to\infty}\frac1N\log\lvert R_n(b,\delta)\rvert
&\leq\max_{0\leq\mu\leq1/2}F_{\mathrm{abs}}(\mu,\delta),\\
F_{\mathrm{abs}}(\mu,\delta)&=\mu\log b+\int_0^\mu\log|a(t)+u|\,dt
+\int_\mu^{1/2}\log\Lambda(t,\delta)\,dt,\\
a(t)&=4\cos^2(\pi t),\qquad u=-4\sin^2(\pi\delta).
\end{aligned}\tag{8}
$$

For $b=0$ the right side means its sole allowed start $\mu=0$. The proof
above yields an explicit UNIFORM $\varepsilon N$ version of (8), also in
the fixed small face/spectral neighborhoods described after (5).
No rate of convergence stronger than that is needed for a strict gap.

For $b>0$ put $c=\cos(\pi\delta)$, $z=\sin^2(\pi\mu)$, $w=c^2/z$ and
$D_0=(x-y)^2$. At a regular interior point,

$$
\partial_\mu F_{\mathrm{abs}}=\log\frac{b\lvert a(\mu)+u\rvert}{\Lambda(\mu,\delta)},
\qquad\frac{b\lvert a+u\rvert}{\Lambda}=
\frac{2b\lvert w-1\rvert}{A+\sqrt{D_0+4Pw}}.\tag{9}
$$

When $0\leq\delta<1/2$, the sign-change point is $t_c=1/2-\delta$.
Before $t_c$, $w$ decreases from infinity to $1$ and the ratio in (9)
strictly decreases from infinity to $0$. For $w>1$ its derivative has
positive numerator

$$
A+\frac{D_0+2Pw+2P}{\sqrt{D_0+4Pw}},
$$

with the $P=0$ case interpreted directly. Thus there is one maximum,
at

$$
\sin^2(\pi\mu_*)=\frac{c^2b^2}{(b+x)(b+y)},\qquad0<\mu_*<t_c.\tag{10}
$$

After $t_c$, $w$ decreases from $1$ and the numerator $1-w$ increases while
the denominator decreases. The ratio is strictly increasing whenever
this interval is nonempty. Therefore every post-$t_c$ critical point
is a MINIMUM, and that part has its maximum at an endpoint.

The complete prefix integral is zero:

$$
\int_0^{1/2}\log|4\cos(\pi(t+\delta))\cos(\pi(t-\delta))|\,dt=0.\tag{11}
$$

This follows by shifting the two intervals and using the reflection
and period of $\log|2\cos|$; it also holds at $\delta=0,1/2$ by integrability.
Consequently $F_{\mathrm{abs}}(1/2,\delta)=\tfrac12\log b$. The pre-$t_c$ maximum is exactly
the original triangle action $Q_b(\delta)$, with its complete normalization.
Thus

$$
\max_\mu F_{\mathrm{abs}}(\mu,\delta)=\max\left\{Q_b(\delta),\tfrac12\log b\right\}.\tag{12}
$$

For $b=0$ it is $Q_0(\delta)$, without the second branch.
At $\delta=1/2$, the ratio (9) is the constant $b/\max(x,y)$, so the same
statement follows by its endpoint values. In particular
$Q_b(1/2)=\tfrac12\log\max(x,y)$, understood as the continuous limit.

For clarity, the action identification in (12) uses the proved [cofactor/marked-action identity](actual_cross_cofactor_marked_action.md) near $\delta=0$. The real integral at
$\mu_*$ has positive prefix factors and positive $\Lambda$, and is real
analytic on $0\leq\delta<1/2$. Its defining formulas have no zero or
branch crossing there. The identity therefore continues on this
connected real interval. Its endpoint value follows either from (3)
at $\delta=1/2$ or from uniform integrability in (8). The cases $P=0$ and
$b=0$ use the exact first-order/sole-start formulas and the same limit.

## 3. Strict local spectral decrease, with the monomial exception

The actual $Q$ action has the exact real derivative

$$
\begin{aligned}
\frac{dQ_b}{d\delta}&=-\log\frac{E_b}{\sqrt D},\\
E_b&=A+2b\sin^2(\pi\delta)
+2\sin(\pi\delta)\sqrt{bA+P+b^2\sin^2(\pi\delta)},\\
D&=A^2-4P\sin^2(\pi\delta).
\end{aligned}\tag{13}
$$

For $0<\delta<1/2$ this derivative is strictly negative whenever
$b>0$ or $P>0$. The possible logarithmic singularity at $\delta=1/2$,
$x=y$ is integrable. Also the interior maximum at $\delta=0$ proves
$Q_b(0)>\tfrac12\log b$ when $b>0$ and $A>0$. Therefore, for each $\eta>0$,

$$
\max\left\{Q_b(\delta),\tfrac12\log b\right\}
\leq Q_b(0)-\gamma_\eta,\qquad\eta\leq\delta\leq\tfrac12.\tag{14}
$$

with $\gamma_\eta>0$ on each fixed positive compact of the nonzero
weights, provided $b>0$ or $P>0$. For $b=0$ omit the second branch.
The sole exception $b=0$, $P=0$ is the literal one-variable monomial;
its cofactor is independent of $\delta$, and no false gap is claimed.

Every actual port has $A=x+y>0$: its outer pair is MATCHING, whereas
the two protected faces share the original MAIN edge. It has at
least one nonmonomial triangle. Indeed, if one outer face vanishes,
there remains only one other protected zero, so at least one middle
is positive. If both outers are positive, $P>0$ in both triangles.
Thus each port's product of two cofactors has a strict gap in (14)
when its spectral $\delta$ stays away from $0$.

The exact even/odd central cofactor formulas contain two or three
products, each with BOTH triangle cofactors and terminal indices
$N/2+O(1)$. All central coefficients have bounded degree and bounded
size on the fixed face/spectral compact. Therefore (8)-(14) imply

$$
|P_{N,\mathrm{cross}}(\delta;\text{positive faces})|
\leq\exp\!\left\{N\left[Q_b(0)+Q_c(0)-\gamma_\eta+o(1)\right]\right\},
\qquad\eta\leq|\delta|\leq\tfrac12.\tag{15}
$$

Uniform $\varepsilon$ versions hold on a small fixed complex neighborhood
of the reference faces and a fixed thin complex $\delta$ strip. This
follows from the proof of (5),(7), not from coefficientwise domination
by the value at positive faces. For all $\delta$ the same estimate without
$-\gamma_\eta$ holds. In particular every other port has a controlled
endpoint rate while one separated port supplies a strict loss.

## 4. Sewing the original marked Cauchy period

Fix the actual positive complete ordinary radii, with both protected
variables zero. Their endpoint weighted exponent after the original
degree-$d$ targets is $\Phi_D$. Take the exact all-CROSS marked coefficient
$C_N(\boldsymbol\delta)$, with its original simultaneous-rotation quotient or,
equivalently, the full original Cauchy torus.

Outside a fixed neighborhood of the common ordinary-face phase, the
already proved [global cofactor angular theorem](actual_cross_cofactor_global_angular_gap.md) supplies a strict
exponential gap, uniformly for ALL real spectral deltas. Its proof
retains all terminal cofactors and every central summand; it also holds
in a sufficiently thin fixed complex spectral strip.

Inside a sufficiently small fixed common-phase neighborhood, use (15)
and its proved small complex FACE extension. If $\max_i|\operatorname{Re}\delta_i|\geq\eta$,
at least one port supplies $\gamma_\eta$, while all the other ports cost
only their endpoint rates and arbitrarily small chosen errors. Since
the graph is fixed, choose those errors so their sum is less than
half that loss. The common face phase cancels exactly by total degree
and original targets. No independent face radii are optimized.

It follows that for each fixed $\eta>0$ there exist $\tau,\gamma>0$, $N_0$ such that

$$
|C_N(\boldsymbol\delta)|\leq e^{N(\Phi_D-\gamma)}.\tag{16}
$$

for $N\geq N_0$, all $\operatorname{Re}\delta_i\in[-1/2,1/2]$ with $\max_i|\operatorname{Re}\delta_i|\geq\eta$,
and $|\operatorname{Im}\delta_i|\leq\tau$. To include boundary neighborhoods cleanly,
first prove the real decrease for $\eta/2$ and then shrink $\tau$. Every
fixed derivative has the same strict rate on a smaller strip by
Cauchy's estimate. Both level parities are included.

This is an actual GLOBAL spectral gap of the all-CROSS shared source,
away from the geometric point on the centered fold cover. It is not
a coefficientwise strict inequality and it is not a global FULL-V
theorem. Genuine moving one-sided paths can violate the corresponding
full coefficient bound, as the previously recorded $\sigma=\sqrt3$
example shows. Any use of (16) in the original Fourier period must
still retain whole-domain charge summation and its endpoint currents.
The [whole all-CROSS period theorem](general_all_cross_long_filling_volume.md)
performs that transfer and obtains the filled-volume asymptotic for this
sector. It does not identify the all-CROSS sector with the full invariant.

## Scope and focused finite checks

The equality in (12) concerns the absolute envelope. Equation (8) is a limsup bound for the actual cofactor; cancellation can make its rate smaller.

The [focused audit](../experiments/audit_actual_global_cross_spectral_gap.py)
and its [results](../experiments/actual_global_cross_spectral_gap_results.json) check four symbolic identities, 120 original recurrence/start-sum
identities, 26,880 rescaled tail entries and 240 finite characteristic
identities at 65 digits, across both parities and all stated zero
patterns. Author replay maximum relative identity error was 1.26e-64.
Its 120 finite weighted-rate comparisons are explicitly diagnostics.
They do not substitute for the uniform proof or numerically verify
the original shared coefficient gap.