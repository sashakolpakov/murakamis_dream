# Sublinear-degree observations of the full coherent output

Written research proof, 22 November 2026.

The full coherent product admits an exact rational Newton calculus.
Recovering the observation coefficients costs at most an exponential
in their degree, uniformly in the quantum level. Interpolation on
actual rows near the positive energy maximum then gives a lower
bound with an explicit degree-dependent loss. Every observation of
degree \(o(N)\), with normalized polynomial coefficients, preserves
the full output energy rate.

This is a statement in the original positive Newton coefficient norm,
equivalently the centered coefficient norm. It does not concern the
uniform physical Hilbert--Schmidt metric or a final scalar closing.

## 1. Exact source data

Fix \(N\ge2\) and put
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^d,\quad \kappa=q^{d^2/2},\qquad
 P_N(\zeta)=2T_N(\zeta/2)+2,\quad
 \mathcal H_N=\mathbb C[\zeta]/(P_N).
 \tag{1}
\]
Here \(T_N\) is the Chebyshev polynomial of the first kind, and
fractional powers mean their displayed exponentials. The full
Hermite algebra, including first normals at double roots, is retained.
Use the orthonormal Newton basis \(e_j\) and centered basis \(f_a\)
of the [compiler](research_centered_fourier_conway_compiler.md).
For \(|t|<1\) define
\[
 Z_N(t)=\sum_{a=0}^d|t|^{2a},\qquad
 u_N(t)=Z_N(t)^{-1/2}\sum_{a=0}^dt^af_a,\qquad
 w_N(y,z)=u_N(y)u_N(z).
 \tag{2}
\]
All products below are the actual algebra multiplication.

The [coherent energy theorem](research_centered_coherent_product_energy.md)
gives the exact Newton coefficients
\[
 \alpha_j=
 \frac{\kappa^2(-q)^jD_N(y)D_N(z)}
 {N\sqrt{Z_N(y)Z_N(z)}}\,
 \frac{(Q;Q)_j(Qyz;Q)_j}
 {(-qy;Q)_{j+1}(-qz;Q)_{j+1}},
 \qquad D_N(t)=1-\eta t^N .
 \tag{3}
\]
We use \((a;Q)_j=\prod_{r=0}^{j-1}(1-aQ^r)\), with empty
product one. Every \(\alpha_j\) is nonzero on the open input bidisk.
In particular, with \(b=yz\) and \(v=Q^j\),
\[
 \frac{\alpha_{j-1}}{\alpha_j}
 =-q^{-1}\frac{(1+qvy)(1+qvz)}{(1-v)(1-bv)}
 \qquad(1\le j<N).
 \tag{4}
\]
The source phases in this ratio have not been replaced by magnitudes.

Let \(\mathsf Z\) denote multiplication by \(\zeta\). In Newton
coordinates the compiler gives
\[
 (\mathsf Zx)_j=(qQ^j+q^{-1}Q^{-j})x_j+
             (Q^j+Q^{-j}-2)x_{j-1},
 \tag{5}
\]
where the second term is absent at \(j=0\). The original upper
endpoint also has no outgoing row \(N\). Since the diagonal entries
have modulus at most two and the shifted entries at most four,
\[
                            \|\mathsf Z\|_{\rm op}\le6 .
 \tag{6}
\]
These are full coefficient identities, not a distinct-root model.

## 2. An exact rational Newton transform

Set
\[
 c_r=qQ^r+q^{-1}Q^{-r},\qquad
 \Pi_k(\zeta)=\prod_{r=0}^{k-1}(\zeta-c_r),\qquad 0\le k<N.
 \tag{7}
\]
Repeated values among the \(c_r\) are retained. These monic
polynomials form a basis through every degree less than \(N\).
Define
\[
 \psi_k(v)=\prod_{r=0}^{k-1}
                   \frac{v-Q^r}{1-bQ^{-r}v},\qquad
 \gamma_k=q^k\prod_{r=0}^{k-1}
             (1+q^{-1}Q^{-r}y)(1+q^{-1}Q^{-r}z).
 \tag{8}
\]
The exact multiplier on every output row is
\[
 \boxed{\qquad
       (\Pi_k(\mathsf Z)w_N)_j
                  =\alpha_j\gamma_k\psi_k(Q^j),
       \qquad 0\le j<N,\quad 0\le k<N .
 \qquad}
 \tag{9}
\]
All denominators are nonzero for \(|y|,|z|<1\).

Here is a direct proof, including the endpoints. If an output has
coefficients \(\alpha_jr(Q^j)\), (4)--(5) give the next multiplier
\[
 \mathcal T r(v)=
 (qv+q^{-1}v^{-1})r(v)+
 q^{-1}\frac{(v-1)(1+qvy)(1+qvz)}
                    {v(1-bv)}r(Q^{-1}v).
 \tag{10}
\]
At \(j=0\) the shifted coefficient vanishes because \(v=1\).
The apparent predecessor there creates no cyclic arrow. Formula
(5) likewise retains the missing upper row.
For the rational functions in (8),
\[
 \frac{\psi_k(Q^{-1}v)}{\psi_k(v)}
   =Q^{-k}\frac{v-Q^k}{v-1}
                   \frac{1-bv}{1-bQ^{-k}v}.
 \tag{11}
\]
Substitute (11) into (10) and subtract \(c_kr(v)\).
Cancellation of the quadratic terms leaves
\[
 (\mathcal T-c_k)(\gamma_k\psi_k)
 =q(1+q^{-1}Q^{-k}y)(1+q^{-1}Q^{-k}z)
       \frac{v-Q^k}{1-bQ^{-k}v}\,\gamma_k\psi_k.
 \tag{12}
\]
This is \(\gamma_{k+1}\psi_{k+1}\), proving (9) by induction.
One first clears the zero factors in these rational calculations;
no division by a vanishing \(\psi_k(Q^j)\) is required.

For a polynomial \(P\) of degree at most \(D<N\), expand
\[
 P=\sum_{k=0}^Dd_k\Pi_k,\qquad
 r_P(v)=\sum_{k=0}^Dd_k\gamma_k\psi_k(v)
                  =\frac{B_P(v)}{\mathcal D_D(v)},\qquad
 \mathcal D_D(v)=\prod_{r=0}^{D-1}(1-bQ^{-r}v).
 \tag{13}
\]
The numerator has degree at most \(D\). Equation (9) gives exactly
\[
 \frac{\|P(\mathsf Z)w_N\|^2}{\|w_N\|^2}
   =\sum_{j=0}^{N-1}\mu_{N,j}|r_P(Q^j)|^2,\qquad
              \mu_{N,j}=\frac{|\alpha_j|^2}{\|w_N\|^2}.
 \tag{14}
\]
Thus the following lower bound uses the actual positive row weights
of the original packet.

## 3. Coefficient control for every degree below the level

For polynomial coefficients in the ordinary monomial basis write
\(\|P\|_2^2=\sum|p_k|^2\), and use the same convention for \(B_P\).
Fix \(0<\rho<1\). There is \(C_\rho\ge1\) such that
\[
             \boxed{\quad
             \|B_P\|_2\ge C_\rho^{-D}\|P\|_2
             \quad(|y|,|z|\le\rho,\ D<N).
             \quad}
 \tag{15}
\]
In particular this is not an approximation for a fixed \(D\) as
\(q\) tends to one.

Choose a fixed radius \(R>1\) with \(\rho^2R<1\). To recover the
coefficients \(a_k=d_k\gamma_k\) from \(r_P\), put
\[
 F_0(v)=r_P(v),\qquad a_k=F_k(Q^k),\qquad
 F_{k+1}(v)=(1-bQ^{-k}v)
                  \frac{F_k(v)-a_k}{v-Q^k}.
 \tag{16}
\]
The apparent singularity is removable. The expansion (13) shows
inductively that these are precisely its rational Newton coefficients.
All \(F_k\) are holomorphic on \(|v|\le R\). On its boundary,
\[
 \|F_{k+1}\|_R
 \le \frac{2(1+\rho^2R)}{R-1}\|F_k\|_R,\qquad
 \|F_0\|_R
 \le\frac{\sqrt{D+1}\,R^D}{(1-\rho^2R)^D}\|B_P\|_2 .
 \tag{17}
\]
Here \(\|F\|_R=\sup_{|v|\le R}|F(v)|\); the maximum principle
also bounds \(|F_k(Q^k)|\) by this norm.
Moreover
\[
 |\gamma_k|\ge(1-\rho)^{2k},\qquad
 \|\Pi_k\|_{\text{coeff},1}\le3^k ,
 \tag{18}
\]
because \(|c_r|\le2\). Combining (16)--(18) gives
\(\|P\|_2\le C_\rho^D\|B_P\|_2\); factors polynomial in \(D\)
are absorbed into the constant to power \(D\).
For \(D=0\) the assertion is the exact equality \(B_P=P\).
This proves (15) without separating the possibly repeated Casimir
nodes or estimating small root-of-unity factorials.

## 4. A quantitative growing-degree observation bound

For this fixed \(\rho\), there are constants
\(\delta_\rho,c_\rho,C_\rho>0\) and \(N_\rho\) such that, whenever
\[
 N\ge N_\rho,\qquad 0\le D\le\delta_\rho N,\qquad
 |y|,|z|\le\rho,\qquad \deg P\le D ,
 \tag{19}
\]
one has
\[
 \boxed{\begin{aligned}
 &c_\rho N^{-1/2}
   \exp\!\left[-C_\rho D-C_\rho(D+1)^2/N\right]
       \left(\frac{D!}{N^D}\right)^2
       \|P\|_2^2\,\|w_N\|^2\\
 &\hspace{18mm}\le \|P(\mathsf Z)w_N\|^2
       \le (D+1)36^D\|P\|_2^2\,\|w_N\|^2 .
 \end{aligned}}
 \tag{20}
\]
We choose \(\delta_\rho<1/4\), so in particular \(D<N\).
The conventions \(0!=1\) and \(N^0=1\) include constant observations.
The constants do not depend on \(D,N,P,y,z\) in (19).

The upper bound follows at once from (6) and Cauchy--Schwarz:
\[
 \|P(\mathsf Z)\|_{\rm op}
              \le\sqrt{D+1}\,6^D\|P\|_2 .
 \tag{21}
\]
For the lower bound, the energy theorem gives a unique bulk maximum
\(u_*(y,z)\), uniformly separated from the endpoints, and a
nondegenerate real energy profile. Its exact bulk amplitude and full
norm asymptotic imply, on a uniform neighborhood of that maximum,
\[
 \mu_{N,j}\ge c_\rho N^{-1/2}
       \exp[-C_\rho N(u_j-u_*)^2],\qquad u_j=(j+1/2)/N .
 \tag{22}
\]
Indeed the profile is at least its maximum minus
\(C_\rho(u-u_*)^2\), and all bulk amplitude factors are bounded
above and away from zero.

Choose \(D+1\) consecutive indices \(j_0,\ldots,j_D\) centered as
closely as possible at \(Nu_*\). They obey
\[
 |u_{j_\ell}-u_*|\le(D+1)/N,\qquad
 \mu_{N,j_\ell}\ge c_\rho N^{-1/2}
                  e^{-C_\rho(D+1)^2/N}.
 \tag{23}
\]
Taking \(\delta_\rho\) small and \(N_\rho\) large ensures that all
these rows are in the uniform bulk neighborhood and in
\(\{0,\ldots,N-1\}\).

Write \(v_\ell=Q^{j_\ell}\). Since \(D<N/2\),
\[
 |v_\ell-v_m|
      =2\left|\sin\frac{\pi(\ell-m)}N\right|
                         \ge\frac{4|\ell-m|}{N}.
 \tag{24}
\]
Lagrange interpolation of the degree-\(D\) numerator on these
actual points has basis polynomials with coefficient norms bounded by
\[
 \left\|\prod_{m\ne\ell}
                  \frac{v-v_m}{v_\ell-v_m}\right\|_2
 \le\frac{2^D(N/4)^D}{\ell!(D-\ell)!}.
 \tag{25}
\]
The numerator coefficient sum is at most \(2^D\), since every
\(|v_m|=1\). Summing (25) gives
\[
       \|B_P\|_2\le\frac{N^D}{D!}
                     \max_{0\le\ell\le D}|B_P(v_\ell)|.
 \tag{26}
\]
On the unit circle \(|\mathcal D_D|\le(1+\rho^2)^D\).
Use in (14) just the largest numerator value among these rows.
Equations (15), (23), and (26) give the lower bound in (20),
after absorbing constants to power \(D\). No Gaussian vector
approximation has been divided by a small observation.

## 5. Sublinear degree and the original source scope

Let \(D_N=o(N)\), and let \(P_N^{\rm obs}\) be any sequence of
ordinary polynomials of degree at most \(D_N\), with coefficient
norm one. The superscript distinguishes an observation from the
characteristic polynomial in (1). Uniformly on compact input bidisks,
\[
 \boxed{\qquad
 \frac1N\log
 \frac{\|P_N^{\rm obs}(\mathsf Z)w_N(y,z)\|^2}
      {\|w_N(y,z)\|^2}\longrightarrow0 .
 \qquad}
 \tag{27}
\]
For \(D\ge1\), integral comparison gives
\(D!\ge(D/e)^D\). Hence the negative logarithm in (20) is at
most a constant times
\[
 \log N+D+(D+1)^2/N+2D\log(N/D),
 \tag{28}
\]
which is \(o(N)\) when \(D=o(N)\). The upper logarithm in
(20) is also \(o(N)\). Constants are handled directly when \(D=0\).
More generally the same rate conclusion holds if
\(\log\|P_N^{\rm obs}\|_2=o(N)\); an upper bound on that norm
alone would not exclude an exponentially small scalar multiplier.

The output energy theorem therefore yields the same positive
exponential rate for these observed packets as for \(w_N\).
This includes coefficient vectors chosen separately at every level.
It is a polynomial calculus on the full actual Hermite module, not
a quotient by one closing functional or an algebra of distinct-root
values. The characteristic polynomial is still an exact relation;
no estimate for all degree-\(N\) observations is asserted.

The restriction is on Casimir degree, not on the number of crossings
in a short word and not on degree four of a variational objective.
A fixed quantum crossing power can have canonical Casimir degree
\(N-1\), and neither (27) nor its proof includes such a general
sequence. Arbitrary further turns, nonlinear component composition,
and the prescribed original scalar closing require separate control.
No knot-volume identity or finite-exception conclusion follows here.

## Complete proof sources

Both complete matching proof texts were read:

| Source | SHA-256 |
|---|---|
| [Full coherent output energy, 393 lines](research_centered_coherent_product_energy.md) | 73152328a77ba5d63a2a8eaa17647ed38b7683c613e0947e3bda9e451dda76e2 |
| [Original centered compiler, 405 lines](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |

The first provides the exact nonzero output rows and their uniform
bulk probability profile. The second supplies the original Casimir
action, full algebra, and declared coefficient norm. The rational
Newton transform, uniform coefficient estimate, interpolation bound,
and growing-degree consequence are proved above. The prior
fixed-degree insertion theorem was checked for coverage; no estimate
from it is extended by substituting a growing degree into its constants.

Only written mathematics and text operations were used. Earlier finals
and public manuscripts remain unchanged.
