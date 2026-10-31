# Independent long twists: monotonicity of the local charge critical value

The [whole-source local packet](general_full_spectral_numerator_geometric_packet.md) now assembles these results for the actual full numerator. The original global spectral filling period remains open.

The [localized original spectral period](general_localized_unit_charge_filling_period.md)
now supplies the separate contour and nonvanishing proof. Combining it
with the comparison below proves dominance within a finite local charge
sector. The complete global remainder remains open.

31 October 2026. Internally reviewed. This is a local analytic
statement about the actual normalized source action. It compares
critical VALUES; it does not prove intersection with an original
integration cycle, a nonzero amplitude, or control of remote charges.

## 1. The actual even action and a general analytic lemma

Let $A_0(\boldsymbol\delta)$ be the original face-stationary complete CROSS action
without the retained quadratic half-twist phase. The two original
marked faces remain zero. The cofactor action identity gives each
triangle as a holomorphic function of
$w_i=-4\sin^2(\pi\delta_i)$. The unique ordinary-face IFT branch is
therefore unchanged under reversal of ANY individual $\delta_i$.
Consequently $A_0$ is even in EACH coordinate. Its coefficients are real,
because the selected face/action germs are real on the real locus.
The actual complete normalization and local curvature give

$$
A_0(0)=\Phi_D,\qquad \operatorname{Hess}A_0(0)=-2\operatorname{diag}(C_1,\ldots,C_R),\qquad C_i>0.
$$

Spectral-independent source phases remain outside this normalized
action. They do not change any derivative below.

More generally assume exactly these analytic hypotheses. There are
holomorphic functions $B_i$ of $\mathbf z=(\delta_1^2,\ldots,\delta_R^2)$, with real
coefficients, such that

$$
\partial_i A_0(\boldsymbol\delta)=-2\delta_i B_i(\boldsymbol\delta^2),\qquad B_i(0)=C_i.\qquad (1)
$$

This follows coefficient by coefficient from separate evenness; the
quotient at $\delta_i=0$ is removable. In particular $B_i$ is NOT inferred
from only the diagonal Hessian without that evenness hypothesis.

For independent nonzero REAL slopes $n_i$ and real charges $\ell_i$ define

$$
\Phi(\boldsymbol\delta;\mathbf n,\boldsymbol\ell)=A_0(\boldsymbol\delta)+\pi i\sum_i n_i\delta_i^2+2\pi i\sum_i\ell_i\delta_i.
$$

In the actual source $n_i=\epsilon_i-2p_i$ are the fixed signed integer
crossing powers, and the surviving $\ell_i$ are integer charges. The
analytic statement first allows real charges in order to differentiate.

## 2. Uniform existence and uniqueness in the scaled box

There are $a>0$ and $n_0>0$, depending only on the fixed analytic germ,
such that if all $|n_i|\geq n_0$ and $|\ell_i/n_i|\leq a$, $\Phi$ has a unique
critical point in the fixed polydisc $\|\boldsymbol\delta\|_\infty\leq2a$.
It depends holomorphically on

$$
t_i=\frac{\ell_i}{n_i},\qquad e_i=\frac1{n_i},
$$

in corresponding complex neighborhoods. No ratio between different
$|n_i|$ is required. Its Hessian is nondegenerate.

Indeed the critical equations are exactly

$$
\delta_i\left[1+\frac{i e_i B_i(\boldsymbol\delta^2)}{\pi}\right]+t_i=0,\qquad \delta_i=-\frac{t_i}{1+i e_i B_i(\boldsymbol\delta^2)/\pi}.\qquad (2)
$$

Choose a small polydisc $\|\boldsymbol\delta\|_\infty\leq2a$ on which
$|B_i-C_i|\leq C_i/8$. Let $M$ bound all $|B_i|$ and $L$ bound the sum of the
absolute values of the $\boldsymbol\delta$-derivatives of every $B_i(\boldsymbol\delta^2)$.
Choose $e_0>0$ such that

$$
\frac{e_0M}{\pi}\leq\frac18,\qquad \frac{64}{49}\frac{a e_0L}{\pi}\leq\frac12.
$$

The right side of (2) maps $\|\boldsymbol\delta\|_\infty\leq2a$ into $\|\boldsymbol\delta\|_\infty\leq8a/7$
and has sup-norm derivative at most $1/2$, uniformly for $|t_i|\leq a$,
$|e_i|\leq e_0$. Uniform contraction proves existence and uniqueness;
uniform iteration, or the analytic IFT, proves holomorphy on a
slightly larger box after shrinking the displayed one if needed.
Take $n_0\geq1/e_0$. Every critical point in the specified $\boldsymbol\delta$ polydisc
satisfies this fixed-point equation, so the uniqueness is genuine
there, not merely uniqueness within a chosen numerical iteration.

The derivative of the left side of (2) is invertible, since it equals
an invertible diagonal matrix times $I$ minus the contraction derivative.
The original Hessian is this Jacobian multiplied on the left by
$2\pi i\operatorname{diag}(n_i)$, hence is nondegenerate. Its conditioning in unscaled
coordinates may depend on the slopes; no uniform unscaled condition
number is asserted.

## 3. Exact derivative and relative control for disparate slopes

Let $S(\mathbf n,\boldsymbol\ell)=\Phi(\boldsymbol\delta(\mathbf n,\boldsymbol\ell);\mathbf n,\boldsymbol\ell)$ be the selected critical value.
For real $n_i$,$\ell_i$, envelope differentiation gives

$$
\partial_{\ell_i}\operatorname{Re}S=-2\pi\operatorname{Im}\delta_i.
$$

Taking the imaginary part of (2), with the FULL generally complex
$B_i$ evaluated at this coupled saddle, gives the exact formula

$$
\begin{aligned}\operatorname{Im}\delta_i&=\frac{\ell_i}{n_i^2}\frac{\operatorname{Re}B_i/\pi}{|1+iB_i/(\pi n_i)|^2},\\ \partial_{\ell_i}\operatorname{Re}S&=-2\frac{\ell_i}{n_i^2}\frac{\operatorname{Re}B_i}{|1+iB_i/(\pi n_i)|^2}.\end{aligned}\qquad (3)
$$

In particular all cross-coordinate effects remain inside a MULTIPLICATIVE
positive factor. They do not produce an additive error which could
dominate $\ell_i/n_i^2$ when that individual slope is very large.
The bounds selected above imply, for $\ell_i\geq0$,

$$
-4C_i\frac{\ell_i}{n_i^2}\leq\partial_{\ell_i}\operatorname{Re}S\leq-C_i\frac{\ell_i}{n_i^2}.\qquad (4)
$$

For example $\operatorname{Re}B_i/C_i$ lies in $[7/8,9/8]$, while the denominator in
(3) lies in $[49/64,81/64]$. Their ratio lies strictly between $1/2$ and $2$,
which proves (4). Hence every derivative is STRICTLY negative when
$\ell_i>0$, regardless of the independent signs and magnitudes of $n_i$.

There is also the uniform sharper asymptotic, with $n_{\min}=\min_i|n_i|$,

$$
\partial_{\ell_i}\operatorname{Re}S=-2C_i\frac{\ell_i}{n_i^2}\left[1+O\!\left(a^2+n_{\min}^{-2}\right)\right].\qquad (5)
$$

To verify it rather than hide a phase error, (2) first gives
$\delta_i=-t_i[1+O(e_0)]$, with the bound proportional to $|t_i|$.
Thus $\delta_i^2-t_i^2=O(e_0|t_i|^2)$. Since $B_i$ has real coefficients,
$B_i(t_1^2,\ldots,t_R^2)$ is real, and the bounded $\mathbf z$-derivatives give
$\operatorname{Im}B_i(\boldsymbol\delta^2)=O(e_0a^2)$. Therefore

$$
\left|1+\frac{i e_iB_i}{\pi}\right|^2=1-\frac{2e_i\operatorname{Im}B_i}{\pi}+\frac{e_i^2|B_i|^2}{\pi^2}=1+O(e_0^2),
$$

while $\operatorname{Re}B_i=C_i+O(a^2)$. Use $e_0=1/n_{\min}$ in these estimates (the
existence threshold remains its previously fixed upper bound).
All constants depend only on the fixed germ and chosen coordinate
neighborhood, not on relative slope sizes or charge ratios. The exact
formula (3) also covers $\ell_i=0$ by continuity.

## 4. Unit charge is the unique largest LOCAL positive-integer value

Increase $n_0$ if necessary so $a|n_i|\geq1$. In the local positive integer
box

$$
1\leq\ell_i\leq a|n_i|,
$$

the all-unit vector is the unique maximizer of $\operatorname{Re}S$. More precisely,
integrate (4) along successive coordinate segments from $1$ to $\ell_i$;
every intermediate vector remains in the same scaled box. Then

$$
\sum_i\frac{C_i}{2n_i^2}(\ell_i^2-1)\leq\operatorname{Re}S(\mathbf n,\mathbf1)-\operatorname{Re}S(\mathbf n,\boldsymbol\ell)\leq\sum_i\frac{2C_i}{n_i^2}(\ell_i^2-1).\qquad (6)
$$

For positive REAL charges there is strict coordinate monotonicity,
not a claim that charge $1$ maximizes the interval $(0,1)$. Separate evenness
and uniqueness also imply that reversing any individual $\ell_i$ reverses
that $\delta_i$ alone and leaves $S$ unchanged. This is a symmetry of
critical values; signs of amplitudes and cycle multiplicities require
their actual source identities.

For the original half-twist convention, define explicitly

$$
A_{\boldsymbol\epsilon}=A_0+\pi i\sum_i\epsilon_i\delta_i^2,\qquad U_i=\partial_i A_{\boldsymbol\epsilon},\qquad V_i=-4\pi i\delta_i,\qquad n_i=\epsilon_i-2p_i.
$$

The half-twist phase is therefore included exactly once. At the
selected saddle these actual primitive logs satisfy
$U_i+p_iV_i=-2\pi i\ell_i$. The already proved Gaussian boundary-term
cancellation identifies $2\pi\operatorname{Re}S$ with its representation volume.
For unit charges and sufficiently long fixed twists, the existing
marked filling theorem identifies this with the actual smooth filling.
The monotonicity proved here compares LOCAL critical values within the
specified box only. It neither bounds charges outside that box nor
proves any critical point contributes to the original Gaussian period.
Charge $0$ remains exactly absent from the original total-derivative
source formula despite the existence of the formal local saddle there.
In the intended asymptotic application the signed twists are fixed
before $N$ grows; no joint growing-twist/level limit follows from this
comparison of the limiting critical action.
