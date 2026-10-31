# Exact Hardy-forest residue reduction of the original selected cycle

28 October 2026. All Hardy/reset variables in
[the continuous-Gaussian cyclic period](actual_continuous_gaussian_cyclic_network.md)
admit a simultaneous ordinary-residue reduction. The surviving
cycle is specified explicitly. Every other annulus component is
retained first and then proved zero against the original source
by a one-way negative-index barrier.

The normal residue coefficient is exactly $+1$. This is the
coefficient of the Hardy pole graph, **not** a computed
intersection number with a hyperbolic thimble.

The [exact audit](../experiments/audit_actual_hardy_forest_residue.py)
and [results](../experiments/actual_hardy_forest_residue_results.json)
check eight original whole-word pivotal matrices with no
intermediate Hardy/head projection, 360 signed head columns,
812 negative-current subsets, nonzero surviving negative
outputs before the original source, the pole-forest Jacobian,
and reduced radius chambers.

## 1. Hardy poles form a forest

Keep the fully telescoped physical braid word, with its
boundary pair fusions and original monomial input/output.
Every Hardy factor connects consecutive variables of ONE
head in word time:

$$
 K_e=\frac1{1-g_e z_{\mathrm{out}}/z_{\mathrm{in}}}.
$$

Here $g_e=1$, except at an actual Gaussian dilation where
$g_e=c_se^{\alpha_s\xi}$. Transfer multiplication does not
identify different heads. An active factorial kernel
breaks the path; its input and output variables remain
independent. The monomial source adds no closing Hardy
edge. Thus the Hardy pole graph is a forest of head-time
segments.

Choose one terminal variable per segment and set

$$
 u_e=\frac{z_{\mathrm{in}}}{g_ez_{\mathrm{out}}}.                \tag{1}
$$

The logarithmic incidence matrix is triangular/unimodular.
Using path normals followed by the terminal coordinate
gives determinant one with the induced orientation.
The base-only $d\log g_e$ terms vanish when wedged with
all Gaussian $d\xi$ variables. Consequently

$$
 K_e\,\frac{du_e}{2\pi i u_e}
       =\frac{du_e}{2\pi i(u_e-1)}.                  \tag{2}
$$

Every normal pole is now independent, with residue $+1$.
No scalar $g_e$, determinant root, meridian factor, or
Gaussian Jacobian is removed. Such factors remain in the
substituted source and cyclic arguments.

## 2. A reduced cycle before taking the residues

The pole graph sets $u_e=1$:

$$
 z_{\mathrm{in}}=g_ez_{\mathrm{out}}.                          \tag{3}
$$

After imposing it, retain one complex variable per
head-time segment and every real Gaussian variable.
Equivalently, one may retain the initial coordinate of
each head and a new coordinate after each active
factorial. Moving the retained coordinate within a
segment multiplies it by a known nonzero product of
$g_e$; its logarithmic Jacobian is one.

There are $b+6m$ complex coordinates for the displayed
strict $m$-crossing physical word on $b$ heads. The
two boundary pair-fusion frames of a $2k$-plat add
$6k$, giving $6m+8k$ in the unshortened presentation.
Further exact simplifications may reduce this count.
All counts are independent of $N$.

### Explicit radii without resets

Take $\rho_0=1/64$ and $0<\lambda\le1$ below all active
color moduli. The following construction works for
every fixed Gaussian tuple and every signed word.

For one crossing, let its input head radii be $R_1,R_2$,
and put $G=|c_se^{\alpha_s\xi}|$. The inverse-fusion
part is realized by

$$
\begin{split}
 b&=\min(\rho_0R_2/2,\ \rho_0\lambda R_1/2),\\
 a&=\rho_0R_1/2,\\
 c&=\max(2b/\rho_0,\ 2aG_*/(\rho_0\lambda)),
\end{split}                                                   \tag{4}
$$

where $G_*=1$ for the positive crossing and
$G_*=\max(1,G)$ for the negative crossing.

The first reciprocal factorial updates head two to $b$.
Its following $V_-$ transfer has argument modulus
at most $\rho_0/2$. The reciprocal factorial on head
one updates it to $a$, and the positive factorial
on head two updates it to $c$.

Positively, the central transfer uses radii $a,c$,
then the Gaussian graph changes head two to $c/G$.
Negatively, that Gaussian graph comes first and the
central transfer uses $a,c/G$. Formula (4) makes its
argument small in either order.

For the final fusion choose

$$
 e=\min(\rho_0(c/G)/2,\ \rho_0\lambda a/2),\quad
 f=2a/\rho_0,\quad q=2e/\rho_0.                      \tag{5}
$$

Its reciprocal second-head diagonal updates to $e$,
its positive first-head factorial to $f$, its
$U_-$ multiplier leaves these coordinates unchanged,
and its final factorial updates head two to $q$.
Every cyclic argument has modulus below $\rho_0$.
Spectator coordinates are simply identified, rather
than being constrained by an extra radius inequality.

For a boundary fusion use its three diagonal updates
and the same preparation of its one transfer; no
Gaussian compensation is needed. The inverse boundary
fusion is handled in the same way.

The full complex Gaussian relation in (3), including
its phase, is imposed; (4)--(5) give its radii.
All logarithms of the chosen radii satisfy

$$
 |\log r_j|\le C_{\mathrm{word}}
                  \left(1+\sum_\ell|\xi_\ell|\right). \tag{6}
$$

Indeed each update is a minimum/maximum of one preceding
logarithm plus a fixed constant and, at most, a term
$\pm\log G$. There is no multiplicative recursion of
logarithms. This gives a specified reduced fibered torus
cycle, not separate incompatible local circles.

## 3. An exact simultaneous annulus decomposition

Let $H$ be the number of Hardy edges. Starting from the
reduced radii above, choose

$$
 \eta=\frac{\log2}{4(H+1)}.
$$

In the normal coordinates (1), allow
$e^{-\eta}\le|u_e|\le e^\eta$ independently.
Each unreduced head coordinate is a retained coordinate
times a product of path normals and Gaussian factors.
Each cyclic argument therefore changes in modulus by
at most $e^{2H\eta}<\sqrt2$. Since its reduced value
is below $1/64$, it remains below $1/16$ throughout
this complete polyannulus.

In particular NO cyclic norm divisor is crossed.
Every cyclic root has its original anchored lift.
Only the explicit independent poles $u_e=1$ occur
in these annuli.

The outer torus $|u_e|=e^\eta$ has every Hardy argument
strictly below one. It can be reached from the original
reset-cycle chamber without crossing a pole or norm
divisor: all radius constraints are affine strict
inequalities in logarithmic radii, so interpolate
linearly. Both cycles have cyclic arguments below
$1/16$ and Hardy arguments below one. Estimate (6)
and the Gaussian majorant hold uniformly in this
homotopy.

Now apply the ordinary annulus identity in each
independent $u_e$:

$$
 \int_{|u_e|=e^\eta}\frac{F\,du_e}{2\pi i(u_e-1)}
  =F|_{u_e=1}
    +\int_{|u_e|=e^{-\eta}}
                  \frac{F\,du_e}{2\pi i(u_e-1)}.       \tag{7}
$$

The other variables are retained. Iteration gives
a finite sum of $2^H$ relative components: the full
pole graph and all possible nonempty sets of inner
circuits.

Nothing is shrunk to zero or infinity. Any information
inside an inner circuit, including possible distant
branch divisors, is still represented by that circuit.
The assertion below is that its original source
pairing is zero, not that it is zero in unpointed
twisted homology.

On each inner circle,

$$
 K_e=-\sum_{a<0}(g_ez_{\mathrm{out}}/z_{\mathrm{in}})^a.         \tag{8}
$$

It is precisely the negative-Laurent current at that
head-time edge. Residue edges implement ordinary
coordinate identification/dilation. All these
series converge absolutely in their stated chambers.

Every branch cycle has the same type of joint bound

$$
 C N^B\exp\{C_0N+C_1N\sum|\xi_\ell|
                        -N\|\boldsymbol\xi\|^2/2\}.
$$

For the absolute coefficient expansion, bound cyclic
coefficients on a slightly larger disk still below
one; the resulting absolute series has the same
exponential-in-$N$ bound. Hardy series have a fixed
geometric ratio $e^{-\eta}$. Thus Fubini/Tonelli
and coefficient routing are justified, including
the noncompact Gaussian base and the radius homotopy.

## 4. Every nonempty inner-current component is source-null

Use signed integer head indices; do NOT impose a
Hardy projection. The exact scalar kernels have
these elementary support properties:

- a reciprocal factorial has only nonnegative
  diagonal coefficients, so it kills a negative
  active index;
- a positive factorial has only diagonal indices
  at most $d=N-1$; its negative Laurent coefficients
  are retained and may be nonzero;
- a transfer has order $h\ge0$ and changes indices
  by $(a,b)\mapsto(a-h,b+h)$ or $(a+h,b-h)$;
- a Gaussian dilation preserves every signed index.

Consider the actual fully ordered crossing
$C\,D\,U_+\,C^{-1}$ or $C\,V_+\,D^{-1}C^{-1}$.

1. In $C^{-1}$, a new negative first index is
   lowered further before the reciprocal first-head
   factorial kills it. A negative second input is
   killed immediately by its first reciprocal
   second-head diagonal.
2. A negative second index created by the central
   transfer survives any dilation, then is killed
   by $C$'s first reciprocal second-head diagonal.
3. The last $U_-$ in $C$ can emit a negative FIRST
   head. Its other head is nonnegative and at most
   $d$ after the last positive factorial. At the
   next crossing touching the negative head, that
   head is killed in $C^{-1}$: immediately if it
   is second, or after further lowering if it is
   first. An untouched negative head cannot heal.

Diagonal negative Laurent coefficients never change
an index and therefore cannot repair it. This proof
uses no cancellation of coefficients and is
independent of colors or Gaussian values.

The original cup input is nonnegative. A boundary
fusion applied to $(d,0)$ produces no negative
survivor, since its last positive factorial
requires $h\le d$. The terminal inverse-fusion
frames kill any negative head. Alternatively, an
original finite nonnegative output coefficient or
pivotal cut kills any untouched negative output.

Thus there is NO supported route from any nonempty
negative-current component in (7) to the original
output source. Its exact pairing is zero. Arbitrary
Laurent-healing coupons inserted inside the word
are outside this statement; original finite coupons
may be extended by zero outside their heads.

This is a route-support proof on the actual kernels,
not reconstruction and evaluation of an entire
prefix polynomial. Infinite cyclic tails are handled
by the convergence argument in Section 3.

Combining (7)--(8), the original selected period equals
the **pure all-pole graph integral with coefficient
exactly $+1$**. All other circuits have been retained
and explicitly proved source-null.

## 5. Explicit reduced scalar phase and cycle coordinates

After the residues:

- each transfer is multiplication by its cyclic
  function in the two current head coordinates;
- every spectator/reset coordinate is identified;
- an active factorial retains a new complex
  coordinate and its cyclic convolution kernel;
- a Gaussian identifies its input/output by
  $w=g_s(\xi)z$, and its ordinary Gaussian variable
  remains integrated on $\mathbb R$.

There are no rational Hardy poles left. The surviving
cycle is exactly the fibered product of circles in
(4)--(5), with the anchored cyclic roots, not an
arbitrary positive-angle chain.

Here is the variable-dependent leading phase of
one positive crossing explicitly. Let its input
coordinates be $z_1,z_2$, its six successive active
factorial output coordinates be $u_1,\ldots,u_6$,
and put $g=-(xy)^{-1}e^{\sqrt{\pi}(1+i)\xi}$.
The output coordinates are $u_5,u_6$. With limiting
marked colors $x,y$ and phase convention
$\exp(W/h)$,

$$
\begin{split}
 W_+={}&-\operatorname{Li}_2(u_1/z_2)
 +\operatorname{Li}_2(u_1/(xz_1))
 -\operatorname{Li}_2(u_2/z_1)
 +\operatorname{Li}_2(u_1/u_3)\\
 &-\operatorname{Li}_2(u_2/(xu_3))
 -\operatorname{Li}_2(gu_4/u_3)
 +\operatorname{Li}_2(u_2/u_5)
 -\operatorname{Li}_2(u_4/(yu_5))
 +\operatorname{Li}_2(u_4/u_6)\\
 &+2\pi i\left[
       \log(u_3/u_1)+\log(u_5/u_2)+\log(u_6/u_4)
             \right]-\pi i\xi^2 .                    \tag{9}
\end{split}
$$

For a negative crossing use
$g=-(xy)e^{\sqrt{\pi}(1-i)\xi}$ and replace its
central term $-\operatorname{Li}_2(u_2/(xu_3))$
by $+\operatorname{Li}_2(gu_2/(yu_3))$.
All other terms follow the same strict order.

The full word phase is the sum of these local
phases and boundary-fusion phases, together with
$2\pi i$ times the original initial-minus-terminal
source logarithms. The original external
$\chi_{\beta,N}$ is retained separately. Exact
$q$ half-steps and the difference between $N$
and $N-1$ contribute the specified nonzero
amplitude; they are not discarded normalization.

All logarithmic marks in (9) come from the
original reflected factorial monomials and
source. Norm roots retain the continuation
from the small-argument cycle.

## 6. Actual classical coordinates, rather than unnamed auxiliaries

Let $p$ be the momentum conjugate to $\log z$,
so $B=e^p$ is the physical clock $Q^a$.
The reduced elementary phase relations give:

$$
\begin{array}{c|c}
\text{kernel}&\text{canonical input/output relation}\\ \hline
\mathcal U(z/w)& B_{\mathrm{out}}=B_{\mathrm{in}}=B,\quad
                    z=w(1-B)\\
N(z/w)^d\mathcal V(Qw/z)&
 B_{\mathrm{out}}=B_{\mathrm{in}}=B,\quad z=w/(1-B)\\
\text{Gaussian}& B_{\mathrm{out}}=B_{\mathrm{in}}=B,\quad
                    w=c_sB^s z
\end{array}                                                   \tag{10}
$$

The positive-factorial momentum lift includes its
retained $2\pi i$. The transfer multipliers change
the momenta by the derivatives of their dilogarithms.
For example a $U_-$ multiplier with
$t=x^{-1}z_2/z_1$ sends

$$
 B_1\mapsto B_1/(1-t),\qquad
 B_2\mapsto B_2(1-t),
$$

and leaves the two position coordinates unchanged.
The Gaussian relation follows from
$\partial_\xi W=-2\pi i\xi+\alpha_s p=0$ and
$\alpha_s^2=2\pi is$.

This identifies concrete parts of the known actual
fusion chart. For a full $C_x$ put $A=B_1,J=B_2$ and

$$
 K=1-\frac{z_2}{xz_1}(1-A)(1-J).
$$

Composition of the elementary relations gives

$$
\begin{split}
 U&=A/K,\qquad V=JK,\\
 z'_1&=z_1/(1-A),\qquad
 z'_2=z_2(1-J)/(1-JK).                               \tag{11}
\end{split}
$$

With

$$
 p_A=z_1^{-1},\quad p_J=z_2^{-1},\quad
 p_U=(z'_1)^{-1},\quad p_V=(z'_2)^{-1},
$$

equation (11) is EXACTLY the previously proved
[actual rational fusion graph](fusion_canonical_chart_and_retained_source_wall.md),
including its inverse. Thus the remaining coordinates
are actual cotangent/head variables.

There is also a literal shared-flag dictionary on the
unwrapped Laurent realization:

$$
 Z_i=B_i,\quad S_i=z_i,\quad
 X=xz_2/z_1,\quad Z=B_1,\quad XZ=QZX.                 \tag{12}
$$

At the complete color,

$$
 (Q-B_1^{-1})X=q\,\mathcal E_1z_2.
$$

This is the actual tetrahedral factor in
[the middle five-point wall calculation](actual_middle_five_point_wall_factorization.md).
However $X^N=x^Nz_2^N/z_1^N$ is still a variable
central multiplication; no typed $X^N=1$ has been
imposed by renaming variables.

At $M=1$ the classical generators are
$F=(1-B)z$, $\mathcal E=z^{-1}(B^{-1}-1)$ and
$K=-B^{-1}$. Up to its specified scalar lift, the
actual shared meridian matrix is the usual
unipotent Gauss chart with $A=B$ and flag coordinate
$z^{-1}$. This gives an explicit comparison with
known classical flag variables, not a conclusion
that the reduced cycle is already a positive
Rivin-angle cycle.

## 7. What remains unproved

The selected auxiliary Hardy cycle has now been
pushed forward exactly, with its normal degree
$+1$, all inner currents accounted for, and an
explicit reduced phase and cycle. The unreduced
Hardy normal directions are no longer being
treated as ordinary geometric stationary variables.

The reduced cycle is still the small-argument
anchored cycle above. Its transport through
cyclic norm divisors and the actual five-term
flag atlas to a regular hyperbolic chart has
not been proved. Neither the normal residue
degree nor the existence of a geometric
critical representation computes its geometric
intersection number. In particular no volume
conjecture or hyperbolic noncancellation is
claimed here.
