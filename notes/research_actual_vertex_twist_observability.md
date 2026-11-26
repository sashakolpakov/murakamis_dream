# Actual vertex sources avoid the twist-observation kernel

Research deduction, 6 November 2026. This is a source-specific
consequence of the original physical-row and first-normal estimates.
It uses no source evaluation, new certificate, or manuscript change.

The grouped twist observations can be degenerate on arbitrary
original polynomials at composite levels. They are nevertheless
polynomially coercive on the actual untraced vertex sources below,
at every level. The hypothesis is preserved by fixed signed crossing
multiplication and by multiplying these sources. A physical turn is
not asserted to preserve it. The resulting observation norm has the
unfilled action; its difference from a prescribed filled observation
is a genuine calibrated filling-action decrease.

## 1. An actual source family and its physical jets

Use the full original Newton algebra, trace, crossing \(R\), and
kernel \(K_N\). Fix an integer \(a\) and a nonnegative integer \(d\).
For real ordinary boundary colors \(w_\ell\in[-2,c_0]\), put
\[
 F_N(z)=\prod_{\ell=1}^d K_N(z,w_\ell),\qquad
 f_N=\operatorname{can}(R^aF_N),\qquad
                         c_0=2\cos(\pi/N).
 \tag{1}
\]
The empty product is allowed. Equation (1) is the literal filled
vertex input in the [arbitrary-power compiler](research_arbitrary_power_source_compilation.md),
before its trace. Only the contracted variable \(z\) is reduced.
Every outside variable remains an unreduced ordinary polynomial.
The estimates here specialize those variables to the stated real
interval; no complex geometric-color extension is inferred.

At each distinct double physical node \(c_j\), write
\[
 F_j=F_N(c_j),\qquad
 d_j=4-c_j^2,\qquad
 \beta_j=(N-1-2j)\sin((2j+1)\pi/N)>0,\qquad
 \lambda_j=R(c_j).
 \tag{2}
\]
The [physical-row and normal bounds](research_physical_normal_lift.md),
equations (3)--(4), give
\[
 K_N(c_j,w_\ell)\ge1,\qquad
 \left|\frac{\partial_z K_N(c_j,w_\ell)}
                   {K_N(c_j,w_\ell)}\right|\le N^{11}.
 \tag{3}
\]
Thus \(F_j\ge1\), its logarithmic derivative is real, and
\[
                         |F_N'(c_j)/F_j|\le dN^{11}.
 \tag{4}
\]
All derivatives in (3)--(4) are the full first normals, not
derivatives of a truncated physical-index formula.

For the trace-adapted pairs of
[twist tomography](research_original_twist_observation_tomography.md),
equations (3)--(4), the actual source (1) gives
\[
 \begin{split}
 a_j(f_N)&=\eta\lambda_j^a
        \{d_jF_N'(c_j)-c_jF_j+ia\beta_jF_j\},\\
 b_j(f_N)&=\eta i\lambda_j^a\beta_jF_j,
                  \qquad \eta=(-1)^{N-1}.
 \end{split}
 \tag{5}
\]
This retains the derivative of the crossing power. At odd levels
the simple coefficient is \(a_*=\lambda_*^a F_N(-2)\).

## 2. Coercivity on the actual source, including composite levels

Let \(\mathcal E_N\) be the grouped scalar-observation form of
tomography (8), and \(\widetilde{\mathcal E}_N\) its ungrouped
positive form (10a). If several nodes have the same crossing
eigenvalue \(\lambda\), (5) gives the exact identity
\[
 \left|\sum_{\lambda_j=\lambda}b_j(f_N)\right|^2
   =\left(\sum_{\lambda_j=\lambda}\beta_jF_j\right)^2
   \ge\sum_{\lambda_j=\lambda}|b_j(f_N)|^2.
 \tag{6}
\]
There is no relative phase inside this sum. Therefore
\[
             \mathcal E_N(f_N)\ge\sum_j|b_j(f_N)|^2.
 \tag{7}
\]
In particular no nonzero source (1) lies in the invisible
composite-level kernel. This conclusion uses its actual positive
physical values, rather than only a dimension or cyclicity statement.

The omitted simple-node coefficient at odd levels is controlled
by the actual last Jacobi row. For \(N=2m+1\), the bounds in
[physical normal reconstruction](research_physical_normal_lift.md),
equations (9)--(11), give, for every \(w\in[-2,c_0]\),
\[
 0<K_N(-2,w)\le4K_N(c_{m-1},w).
 \tag{8}
\]
Indeed the recurrence expresses the left side as a coefficient
less than four times the preceding positive row, minus a
nonnegative multiple of the row before it. At \(N=3\) the latter
term is absent. Consequently \(F_N(-2)\le4^d F_{m-1}\).

Set
\[
 C_{a,d}=(4d+|a|+2)^2+1+16^d.
 \tag{9}
\]
The elementary inequalities \(2/N\le\beta_j\le N\),
\(d_j\le4\), and \(|c_j|\le2\), together with (4), show
\[
 |a_j|^2+|b_j|^2
       \le\bigl((4d+|a|+2)^2+1\bigr)N^{22}F_j^2
       \le\frac{(4d+|a|+2)^2+1}{4}N^{24}|b_j|^2.
 \tag{10}
\]
At odd levels (8) gives
\[
                  |a_*|^2\le \frac{16^d}{4}N^2
                                      |b_{m-1}|^2.
 \tag{11}
\]
Equations (7), (10), and (11) prove the following all-level bound.

**Theorem 1.** Every source (1), uniformly in its stated real
boundary colors, satisfies
\[
 \boxed{\quad
 \widetilde{\mathcal E}_N(f_N)
          \le C_{a,d}N^{24}\mathcal E_N(f_N).
 \quad}
 \tag{12}
\]
The constant is independent of \(N\) and of the boundary colors.
No primality hypothesis is used.

For example, with the full physical-jet norm of tomography (10),
its all-level comparison and its two-block Fourier identity give
\[
 \max_{0\le n<4N}|\phi_N(R^nf_N)|
        \ge\frac{\|f_N\|_{\rm jet}}
                     {\sqrt{12C_{a,d}}\,N^{15}}.
 \tag{13}
\]
All original first normals and the odd simple node occur in this
estimate. The observation selected from the window may depend on
the level and on the source. Equation (13) does not specify a
fixed filling power.

The class (1) is closed under any fixed extra signed crossing:
\(R^kf_N\) has the same \(F_N\) and exponent \(a+k\).
It is also closed under quotient multiplication of two such
inputs: exponents add and the lists of bare kernels concatenate.
The constants in (12) may depend on these fixed data but remain
polynomial in \(N\). These are exact operations at an untraced
vertex. The statement does not replace a previously traced child
by a bare kernel or assert closure under \(J\).

## 3. Keeping one original carrier parity

The parity-specific form \(\mathcal E_N^{(\epsilon)}\) of
tomography (9a) groups nodes by \(\tau_j=(\lambda_j/\kappa)^2\).
Its normal coefficient before grouping is
\[
 b_j^{(\epsilon)}
     =2\eta i\kappa^a
          (\lambda_j/\kappa)^{a+\epsilon}\beta_jF_j,
                  \qquad \epsilon\in\{0,1\}.
 \tag{14}
\]
If \(a+\epsilon\) is even, the phase in (14) is identical
throughout each \(\tau\)-group. Hence
\(\mathcal E_N^{(\epsilon)}(f_N)\ge4\sum_j|b_j(f_N)|^2\).
The proof of Theorem 1 therefore also gives
\[
 \widetilde{\mathcal E}_N(f_N)
          \le C_{a,d}N^{24}\mathcal E_N^{(\epsilon)}(f_N),
                         \qquad a+\epsilon\text{ even}.
 \tag{15}
\]
Thus (13), with the same generous constant, holds using only
the \(2N\) added powers \(\epsilon+2r\), \(0\le r<2N\),
when the total filling exponent is even. This is a statement
inside that original carrier parity, not a change of carrier.

For an odd total exponent, two nodes whose crossing eigenvalues
differ by a sign contribute opposite phases to (14). The proof
above makes no all-level coercivity claim for that single parity.
At odd prime levels the general tomography theorem already
controls either parity; the additional all-level assertion here
is precisely (15). The full window (12)--(13) remains valid at
every level regardless of \(a\).

## 4. The calibrated action drop survives source-specific coercivity

The source-specific positive conclusion does not make the unfilled
and filled actions equal. This distinction can be stated for an
actual family with a completely proved scalar asymptotic.

Set every outside color in (1) to \(-2\), take \(d\ge1\), and
fix \(a\ge2\). Let \(M_\infty=4G/\pi\). The full bare-kernel
packet at the nearest complete physical row, together with the
real-period and Hermite bounds, gives
\[
                  \|f_N\|_{\rm jet}
                   =\exp\{NdM_\infty+O_{a,d}(\log N)\}.
 \tag{16}
\]
For the lower bound use that row, whose kernel value has rate
\(M_\infty\) through both parities, and whose crossing value
has modulus one. For the upper bound multiply the real kernel
bounds and use the full normal product rule. These are the same
inputs used in
[the actual source quotient calculation](research_current_free_aw_crossing_transport.md),
equations (62)--(66); taking a fixed product changes only its
exponential rate by the factor \(d\) and its polynomial prefactor.

Grouping at most \(N\) coefficient pairs gives
\(\mathcal E_N\le N\widetilde{\mathcal E}_N\). Together with
(12) and the polynomial jet comparison this yields
\[
            \mathcal E_N(f_N)^{1/2}
                 =\exp\{NdM_\infty+O_{a,d}(\log N)\}.
 \tag{17}
\]
On the other hand the
[whole isolated-vertex theorem](research_isolated_vertex_coverage_and_assembly.md),
Theorem 1 and Section 5, proves for the prescribed original
observation
\[
 |\phi_N(f_N)|=\exp\{NM_{d,a}+O_{a,d}(\log N)\},\qquad
 \delta_{d,a}:=dM_\infty-M_{d,a}>0.
 \tag{18}
\]
Both actions have their original geometric calibration. The
charge-zero blocks have volume \(2\pi dM_\infty\); filling the
original primitive slope gives volume \(2\pi M_{d,a}\).
Along the positive cone path \(t(\lambda)\),
the stationary action has derivative \(\Im t(\lambda)<0\).
Thus
\[
 \delta_{d,a}=-\int_0^1\Im t(\lambda)\,d\lambda,\qquad
 \frac{|\phi_N(f_N)|}{\mathcal E_N(f_N)^{1/2}}
       =\exp\{-N\delta_{d,a}+O_{a,d}(\log N)\}.
 \tag{19}
\]
The original carrier, primitive longitude, and absolute volume
anchor in that cited geometric theorem are unchanged.

Equation (19) is the calibrated filling-action decrease, not a
failure of the correct geometric-rate scalar: (18) already has
its nonzero coefficient. Nor is it a counterexample to the volume
conjecture. It shows why proving that an actual source avoids the
observation kernel, even with polynomial norm coercivity, does
not supply the particular filled coefficient at the unfilled
normalization. Quantitative transport through a new short turn
must account for its own action change and prove that its leading
observed coefficient remains nonzero.

The new exact implication is (12), including the physical
simple-node control and the parity scope (15). It removes the
arbitrary-vector collision obstruction for this actual source
class. It does not assert it for arbitrary turned child tangles,
nonreal geometric outside colors, or a general short component.
