# The original source has an exact cyclic-dilogarithm and ordinary-Gaussian period

28 October 2026. The remaining finite marked Gaussian in
[the exact cyclic/Hardy network](actual_cyclic_hardy_dilog_network.md)
can also be removed. The original knot period is an exact integral
of the literature cyclic dilogarithm and its inverse, ordinary
Cauchy kernels, and ordinary continuous Gaussian weights.
There are no finite Dirichlet, finite Euler, or finite Gaussian
scalar kernels in this presentation.

The cycle is a specified **fibered torus over real Gaussian
variables**, with Gaussian-dominated absolute convergence.
It is not a fixed product of circles interchanged formally
with an unbounded Gaussian integral. All original source,
peripheral, Cartan and framing factors are retained.

The [audit](../experiments/audit_actual_continuous_gaussian_network.py)
and [results](../experiments/actual_continuous_gaussian_network_results.json)
check 660 exact both-sign phase identities, eight whole
original pivotal word matrices with joint Gaussian moments
and no finite Gaussian kernel, ten real-Gaussian quadratures,
and the fibered radius bounds.

## 1. The exact Gaussian moment, with both signs fixed

Put $h=2\pi i/N$, $Q=e^h$. For the original equal-color
Gaussian,

$$
 d_a=(-1)^a x^{-2a}\exp\{h(a^2-a)/2\}.
$$

For $s\in\{+1,-1\}$ set

$$
 c_s=-x^{-2s}e^{-sh/2},\qquad
 \alpha_s=\sqrt{\pi}(1+is),\qquad \alpha_s^2=2\pi is.
                                                            \tag{1}
$$

Then exactly

$$
 \boxed{\quad
 d_a^s=
 \sqrt{\frac{N}{2\pi}}\int_{\mathbb R}
 e^{-N\xi^2/2}
       (c_se^{\alpha_s\xi})^a\,d\xi.
 \quad}                                                       \tag{2}
$$

Indeed the centered Gaussian of variance $1/N$ has complex
moment $\exp(\alpha_s^2a^2/(2N))=\exp(sh a^2/2)$.
Multiplication by $c_s^a$ gives the original linear phase
and meridian powers. For $s=-1$, the sign is still $(-1)^a$,
as required by the inverse Gaussian.

For a typed unequal-color crossing replace $x^{-2s}$ by
$(xy)^{-s}$ in (1). Nothing else changes. No common Cartan
factor is incorporated into this replacement.

For every polynomial $f$, (2) gives an exact operator identity

$$
 \mathsf D_sf(z)=
 \sqrt{\frac{N}{2\pi}}\int_{\mathbb R}
        e^{-N\xi^2/2}
        f(c_se^{\alpha_s\xi}z)\,d\xi.                 \tag{3}
$$

Each integrand is a dilation, so it preserves polynomial
degree. Before every original Gaussian its active head
lies below $N$. Thus (3) equals the original finite marked
Gaussian on every actual input. This is an equality of
whole operators on those inputs, not an assumed selected
Gaussian branch.

The active scalar Cauchy kernel for the dilation is

$$
 \frac1{1-c_se^{\alpha_s\xi}z/w}.                     \tag{4}
$$

All spectator heads retain their ordinary Hardy kernels.
There is one independent $\xi$ for each original Gaussian
factor, hence one for each signed crossing in the specified
strict presentation.

## 2. A common fibered cycle

Retain the norm-one literature functions

$$
 \mathcal V_N(t)=(1-t^N)^{(N-1)/(2N)}
       \prod_{\ell=1}^{N-1}(1-Q^\ell t)^{-\ell/N},
 \qquad \mathcal U_N(t)=\mathcal V_N(t)^{-1},           \tag{5}
$$

on their branches equal to one at zero. All non-Gaussian
kernels and reflected monomials are exactly those in the
previous theorem.

Choose $\rho=1/16$. On a fixed color chart choose
$0<\lambda\le1$ with $\lambda\le|x_j|$ and choose

$$
 C_c\ge\max(1,\sup|x_j|^2,\sup|x_j|^{-2}).
$$

The same bound covers the typed products $(x_jx_{j+1})^{\pm1}$.
Insert a Hardy identity-reset layer before every elementary
factor. Given preceding output radii $R_j$, first put
$r_j=\rho R_j/2$. Before a transfer decrease its numerator
radius, if needed, so $r_{\rm num}/r_{\rm den}
\le\rho\lambda/2$.

For the factor's output radii use

$$
 s_j=\rho r_j/2
$$

except at a positive factorial, where
$s_i=2r_i/\rho$, and at a Gaussian, where use

$$
 \boxed{\quad
 s_i=\frac{\rho}{2C_c}e^{-2|\xi|}r_i.
 \quad}                                                       \tag{6}
$$

Since $\operatorname{Re}\alpha_s=\sqrt\pi<2$,

$$
 |c_se^{\alpha_s\xi}|\,s_i/r_i
 \le\frac\rho2e^{\sqrt\pi\,\xi-2|\xi|}
 \le\rho/2.                                           \tag{7}
$$

Thus every cyclic atom argument and every Cauchy-kernel
argument has modulus at most $\rho/2$. At a positive
factorial the reflected argument has modulus
$|Qw_i/z_i|=\rho/2$; its full scalar kernel is still
$N(z_i/w_i)^{N-1}\mathcal V_N(Qw_i/z_i)$.

These inequalities hold simultaneously for every
$\boldsymbol\xi\in\mathbb R^m$. The number of layers is fixed
by the word. There is no inequality closing terminal
radii back to initial radii, because the fused source is
monomial. The construction uses no $N$-dependent radius
constant on the fixed color chart.

For each $\boldsymbol\xi$, take the product of the
positively oriented circles of these radii and its uniquely
anchored lift through (5). Denote it by $\Gamma(\boldsymbol\xi)$.
The full integration chain is the union of these tori over
the oriented base $\mathbb R^m$.

The radii are continuous and piecewise smooth because of
the minima and absolute values. Their strata glue without
additional internal boundary. When the logarithmic torus
volume form is wedged with all $d\xi_j$, its
$d\log r(\boldsymbol\xi)$ terms vanish. Equivalently one
integrates the fibers with their usual $dz/(2\pi iz)$
measure. There is **no extra radius Jacobian**.

## 3. Absolute convergence on the full fibered chain

The following bounds are uniform in $N$ and in the real
Gaussian variables; constants depend on the fixed word
and color chart.

First, all radii can be chosen at most one. A positive
factorial's increase after its reset never exceeds its
preceding radius. If $L$ is the number of elementary
factors, put

$$
 c_{\rm reset}=\min(\rho/2,\rho^2\lambda/4),\qquad
 c_* =c_{\rm reset}\rho/(2C_c)>0.
$$

An induction gives, at every layer,

$$
 -\log r_j\le C_{\rm word}
                 +2\sum_{\ell=1}^{m}|\xi_\ell|.        \tag{8}
$$

One may take $C_{\rm word}$ to be a fixed multiple of
$L|\log c_*|$. Minima in the radius construction only
replace one radius by a fixed constant times another;
they do not introduce products of previously accumulated
logarithms.

Second, the exact logarithm of (5) gives on $|t|\le\rho$

$$
 |\log\mathcal V_N(t)|,\ |\log\mathcal U_N(t)|
 \le-\frac N4\log(1-\rho).                            \tag{9}
$$

Here $|Q^r-1|\ge4/N$ for every nontrivial root, and the
resonant logarithmic coefficients cancel exactly. All
Hardy and Gaussian-dilation kernels are bounded by
$(1-\rho)^{-1}$.

Every reflected factorial contributes its ORIGINAL factor
$N$ and a monomial whose radius ratio is fixed at $2/\rho$.
Every source exponent has magnitude at most $N-1$.
Consequently the absolute scalar density, apart from the
unchanged external line $\chi_{\beta,N}$ and the normalized
Gaussian measure, is bounded by

$$
 C N^B
 \exp\left\{C_0N+C_1N\sum_\ell|\xi_\ell|\right\}.       \tag{10}
$$

Thus the full pullback is dominated by

$$
 C N^B
 \exp\left\{C_0N+C_1N\sum_\ell|\xi_\ell|
                   -\frac N2\sum_\ell\xi_\ell^2\right\}.
                                                            \tag{11}
$$

This is integrable for every $N$. With the normalized
Gaussian measures its integral is at most
$C'N^B e^{C_2N}$. We make no additional growth assertion
about the retained external $\chi_{\beta,N}$.
These estimates prove Fubini and the disappearance of
Gaussian boundary terms at real infinity.

## 4. Exact original-source identity, with no finite scalar kernels

Let $\mathcal H_{\ell,N}(\boldsymbol\xi)$ be the kernels of
the cyclic/Hardy network with each finite Gaussian replaced
by (4). Let $m$ be their Gaussian count. The ORIGINAL
full fused-plat period is exactly

$$
\begin{split}
 P_{\beta,N}
 ={}&\chi_{\beta,N}N^{1-k}
          \left(\frac N{2\pi}\right)^{m/2}
       \int_{\mathbb R^m} e^{-N\|\boldsymbol\xi\|^2/2}\\
 &\quad\cdot
       \int_{\Gamma(\boldsymbol\xi)}
       (z^0)^{a_{\rm in}}(z^L)^{-a_{\rm out}}
         \prod_{\ell=1}^{L}
             \mathcal H_{\ell,N}(\boldsymbol\xi)
         \prod_{\ell,j}\frac{dz_j^\ell}{2\pi iz_j^\ell}
       \,d\boldsymbol\xi .
\end{split}                                                   \tag{12}
$$

Every source exponent, factor $N$, monomial, norm root,
half-character and original external scalar is retained.
No finite $\Gamma_{\pm,N}$, finite Euler polynomial, or
finite Dirichlet numerator occurs in its scalar integrand.

For a fixed $\boldsymbol\xi$, the torus contraction is
the original completed polynomial word with its Gaussian
factors replaced by independent dilations. Each head is
still polynomial and all previous support/barrier
arguments remain valid. The contraction is a finite sum
of products of the dilation moments. Integration of each
independent variable gives (2), in its original operator
order, and therefore the exact original word.

Estimate (11) also justifies this as an equality of
absolutely convergent multiple integrals, rather than
only an iterated polynomial calculation.

The full original Ward corner is fixed BEFORE expanding
the Gaussian factors. A fixed-$\boldsymbol\xi$ word need
not be a Hopf intertwiner. We do not reapply the Ward
corner reduction to such an individual word or replace
its transported co-source by a newly chosen cap.
Linearity of the already proved full-source functional
is what is used in (12).

Any specified root-specialized quantum A-annihilator of
the original meridian function therefore annihilates
(12) as well. No identification of a classical symbol
or selected geometric component is inferred.

## 5. Uniform leading symbols on the INITIAL cycle

There is now a direct uniform phase comparison for the
actual scalar functions on this cycle, without a finite
Taylor-remainder sector. For every fixed $\rho<1$,

$$
\begin{split}
 \mathcal V_N(t)
   &=(1-t)^{1/2}
       \exp\{\operatorname{Li}_2(t)/h\}
          (1+O_\rho(N^{-1})),\\
 \mathcal U_N(t)
   &=(1-t)^{-1/2}
       \exp\{-\operatorname{Li}_2(t)/h\}
          (1+O_\rho(N^{-1})).
\end{split}                                                   \tag{13}
$$

The normalized errors are analytic and admit the same
bound with any fixed number of derivatives on smaller
disks. All logarithms are the anchored branches.

For a direct proof split the logarithmic series
$\log\mathcal V_N(t)=\sum_{N\nmid m}t^m/[m(Q^m-1)]$
at $m=N/2$. On the lower
range,

$$
 \frac1{e^{hm}-1}=\frac1{hm}-\frac12+O(|h|m).
$$

For example the remainder bound on $|hm|\le\pi$ follows
from the elementary sine/cotangent formula, with its
removable value at zero. Summation gives $O_\rho(1/N)$.
The upper range is exponentially small in $N$, using
$|Q^m-1|^{-1}\le N/4$. The omitted resonant coefficients
are exponentially small too. Thus

$$
 \log\mathcal V_N(t)
 =\operatorname{Li}_2(t)/h+\tfrac12\operatorname{Log}(1-t)
                      +O_\rho(N^{-1}),
$$

and Cauchy estimates give the derivative version.

The exact Gaussian weight in (12) is $e^{-N\xi^2/2}$.
On the original color charts, the remaining $q$ phases
shift the small cyclic arguments by $e^{\beta h}$ for
fixed half-integer or integer $\beta$. Their change is
an explicit nonzero amplitude:

$$
 \mathcal V_N(e^{\beta h}t)
 =(1-t)^{1/2-\beta}e^{\operatorname{Li}_2(t)/h}
                  (1+O_\rho(N^{-1})),                \tag{14}
$$

with the inverse formula for $\mathcal U_N$.
The dilation Cauchy kernel has the same type of
uniform nonzero density correction, since its
argument stays below $\rho$.

Thus (12) has actual dilogarithm/Gaussian leading
symbols and a specified nonzero leading density on
its INITIAL fibered cycle. This is a pointwise
integrand comparison. It does not imply a relative
asymptotic for a cancelling total period, geometric
dominance, or a nonzero intersection with a Rivin
critical cycle.

## 6. The remaining global theorem

The finite scalar endpoints have been replaced by
global anchored functions and a specified convergent
cycle, with exact equality to the original invariant.
Their boundary information has not been discarded:
it is carried by that cycle, the norm-root branches,
the original affine charges and the Cauchy pole data.

To prove a broad volume theorem one must still
transport this cycle to the geometric ideal-angle
chain, retaining norm-divisor residues, compatible
root frames, Cauchy-pole contributions and the
original pointed source. The oversized weak alias
example shows why an unmarked choice of every
nonnegative angle locus would be incorrect.
No global transport or volume limit is claimed here.
