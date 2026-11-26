# Correlated primitive Taylor bounds for the canonical terminal family

Research protocol, 6 November 2026. This replaces the independent-box
Jacobian enclosure of the preceding affine diagnostic by the exact
rank-one primitive decomposition of the original gradient. It reuses
the same saved rational center, inverse proposal, response proposal and
sixteen error-radius candidates. No new proposal, root solve, source
evaluation, subdivision or adaptive retry is allowed. This protocol
states a validation rule, not its outcome.

## 1. The original gradient as eleven shared arguments

Use \(q=(e,\xi,t,a,s)\), \(j(z)=\Log(2\sin\pi z)\), and the
canonical equations in
[the original suffix theorem](research_mixed_terminal_horizontal_envelope_diagnostic.md).
Write
\[
 f(q;b)=\sum_{\ell=1}^{11}\sigma_\ell v_\ell j(z_\ell)
                      +i\pi(M_\epsilon q+n b+c_\epsilon),
 \qquad z_\ell=v_\ell^{\mathsf T}q+w_\ell b+d_\ell.
 \tag{1}
\]
The complete inventory is:

| Argument \(z_\ell\) | \(\sigma_\ell\) | \(v_\ell^{\mathsf T}\) | \(w_\ell\) | \(d_\ell\) |
|---|---:|---|---:|---:|
| \(e-\xi\) | \(-1\) | \((1,-1,0,0,0)\) | 0 | 0 |
| \(e+t\) | \(1\) | \((1,0,1,0,0)\) | 0 | 0 |
| \(e\) | \(-\epsilon\) | \((1,0,0,0,0)\) | 0 | 0 |
| \(1/2-\xi\) | \(-2\) | \((0,-1,0,0,0)\) | 0 | \(1/2\) |
| \(\xi\) | \(-3\) | \((0,1,0,0,0)\) | 0 | 0 |
| \(t+a\) | \(1\) | \((0,0,1,1,0)\) | 0 | 0 |
| \(t\) | \(-(2+\epsilon)\) | \((0,0,1,0,0)\) | 0 | 0 |
| \(a+s\) | \(1\) | \((0,0,0,1,1)\) | 0 | 0 |
| \(a\) | \(-3\) | \((0,0,0,1,0)\) | 0 | 0 |
| \(s+b\) | \(1\) | \((0,0,0,0,1)\) | 1 | 0 |
| \(s\) | \(-3\) | \((0,0,0,0,1)\) | 0 | 0 |

The constant chirp data are
\[
 M_\epsilon=
 \begin{pmatrix}
 \epsilon&1&-1&0&0\\
 1&0&0&0&0\\
 -1&0&\epsilon&1&0\\
 0&0&1&1&-1\\
 0&0&0&-1&1
 \end{pmatrix},\quad
 n=(0,0,0,0,1)^{\mathsf T},\quad
 c_\epsilon=(-\epsilon/2,0,-\epsilon/2,-1/2,-1/2)^{\mathsf T}.
 \tag{2}
\]
Expanding (1) gives the five original, unscaled gradient components.
In the auxiliary row the three logarithmic coefficients have total
degree zero in the factor 2:
\(2\log2+\log2-3\log2=0\).
Also \(2\sin\pi(1/2-\xi)=2\cos\pi\xi\).
On the original strips these are identities on the principal
continuations, not identities only after exponentiation.

All \(z_\ell\) used below must satisfy \(0<\Re z_\ell<1\).
There \(\Re\sin\pi z_\ell>0\), so \(j\) is holomorphic on the
whole strip with precisely the original branch. This also verifies
the cosine branch through the fourth argument. The zero coefficient
when \(\epsilon=0\) does not change the declared inventory.

## 2. Correlated affine and full argument disks

Let \(q^0,B,u\) be the exact Gaussian-rational data saved by the
[earlier affine diagnostic](research_mixed_terminal_affine_family_certificate.md).
For the prescribed parameter disk \(K=\{|b-b_0|\le r\}\), put
\[
 \delta=b-b_0,\qquad q=q^0+u\delta+\zeta,\qquad
 |\zeta_i|\le\rho_i.
 \tag{3}
\]
Compute the following quantities before taking absolute values:
\[
 z_\ell^0=v_\ell^{\mathsf T}q^0+w_\ell b_0+d_\ell,\qquad
 \lambda_\ell=v_\ell^{\mathsf T}u+w_\ell,\qquad
 h_{\ell i}=(Bv_\ell)_i.
 \tag{4}
\]
They are exact Gaussian rationals. In particular
\[
 z_\ell=z_\ell^0+\lambda_\ell\delta+v_\ell^{\mathsf T}\zeta.
 \tag{5}
\]
The relevant complex disks have radii
\[
 R_\ell^{\rm aff}=r|\lambda_\ell|,\qquad
 R_\ell^{\rm full}=r|\lambda_\ell|
                                 +\sum_j|v_{\ell j}|\rho_j.
 \tag{6}
\]
Outward rational upper bounds may enlarge these radii. They must not
be replaced by \(r\sum_j|v_{\ell j}u_j|+r|w_\ell|\) in the
intended sharp test: that would discard the shared-parameter cancellation.
No coordinate image is clipped using the desired conclusion.

For either disk with radius \(R\), require
\[
 d=\min\{\Re z_\ell^0-R,\ 1-\Re z_\ell^0-R\}>0 .
 \tag{7}
\]
Since \(d\le1/2\), the elementary identity
\(|\sin\pi(x+iy)|^2=\sin^2\pi x+\sinh^2\pi y\) gives
\[
 |j''(z)|=\frac{\pi^2}{|\sin\pi z|^2}
                     \le m(d):=\frac{\pi^2}{\sin^2(\pi d)}.
 \tag{8}
\]
Thus a single outward evaluation at the exact rational \(d\) supplies
each bound \(m_\ell^{\rm aff},m_\ell^{\rm full}\).
Every connecting segment stays in its declared argument disk.

The original common uniqueness domain is
\[
 \mathcal D=
 ([.33,.47]+i[-.09,.08])
 \times([.21,.25]+i[.01,.10])
 \times([.23,.45]+i[-.12,.12])^3.
 \tag{9}
\]
Full containment of the affine-plus-error tube in (9) is recorded,
but is not required by this new test. Instead, require the old
certified enclosure of \(q_*(b_0)\) to lie strictly inside the
central error polydisk \(q^0+\{|\zeta_i|\le\rho_i\}\).
For a saved Cartesian enclosure, it suffices to compare the sum
of the two squared farthest coordinate distances from \(q_i^0\)
with \(\rho_i^2\), using exact rational endpoints.
The regular-log condition (7) is required on the full tube.
This separates branch regularity from identification with the
already proved canonical family.

## 3. Residual and contraction bounds

At the one fixed rational center evaluate
\[
 f_0=f(q^0;b_0),\qquad
 J_0=\sum_\ell\sigma_\ell v_\ell v_\ell^{\mathsf T}j'(z_\ell^0)
                                      +i\pi M_\epsilon,\qquad
 L_0=j'(s^0+b_0)+i\pi .
 \tag{10}
\]
Set \(c=Bf_0\), \(v=B(J_0u+L_0{\bf e}_s)\), and
\(E^0=I-BJ_0\). Taylor expansion of each shared primitive
argument, followed by the fixed preconditioner, proves
\[
 \left|(Bf(q^0+u\delta;b_0+\delta))_i\right|
 \le \mathcal R_i :=
 |c_i|+r|v_i|
 +\frac{r^2}{2}\sum_\ell|\sigma_\ell h_{\ell i}|
                         m_\ell^{\rm aff}|\lambda_\ell|^2.
 \tag{11}
\]
The constant chirp is exactly linear, so has no Taylor remainder.
The squared moduli \(|\lambda_\ell|^2\) can be computed exactly as
rationals, rather than by squaring an already rounded modulus bound.

Similarly the exact rank-one Jacobian formula gives, throughout (3),
\[
 |(I-BJ(q;b))_{ij}|
 \le \mathcal E_{ij}:=
 |E^0_{ij}|+
 \sum_\ell|\sigma_\ell h_{\ell i}|
                       m_\ell^{\rm full}R_\ell^{\rm full}|v_{\ell j}|.
 \tag{12}
\]
Here \(j'(z_\ell)-j'(z_\ell^0)\) is bounded by (8) times
the full radius. All entries of \(Bv_\ell\) are taken from the
same exact preconditioner; no natural interval matrix product
over independent coordinate boxes is used.

**Theorem 1.** Suppose (7) holds on the full tube, the saved central
root is contained in its central polydisk as just specified, and
\[
 \mathcal R_i+\sum_j\mathcal E_{ij}\rho_j<\rho_i
                                      \quad(1\le i\le5)
 \tag{13}
\]
hold with outward bounds, then for every \(b\in K\) the original
canonical root satisfies
\[
             |q_{*,i}(b)-q_i^0-u_i(b-b_0)|<\rho_i.
 \tag{14}
\]

For fixed \(b\), the map \(q\mapsto q-Bf(q;b)\) maps the
closed error polydisk strictly into itself by (11)--(13).
Its Lipschitz constant in the weighted maximum norm is at most
\(\max_i\rho_i^{-1}\sum_j\mathcal E_{ij}\rho_j<1\).
The contraction theorem gives a fixed point. The same bound makes
\(BJ\) invertible by its Neumann series, hence \(B\) invertible;
the fixed point is an actual zero of \(f\).
For parameters in the open disk, this new root is holomorphic:
the original holomorphic gradient is regular throughout the tube,
its Jacobian is invertible at the fixed point, and uniform contraction
gives continuous dependence on the parameter. The local implicit
roots therefore agree with these fixed points. The same contraction
also gives continuity up to the closed parameter boundary.

At \(b_0\), the old certified root belongs to the central polydisk,
so fixed-point uniqueness identifies it with the new root.
The implicit function theorem then identifies the two branches on
a neighborhood of \(b_0\). Both are holomorphic on the connected
open input disk: the original branch exists there by the prior
canonical theorem, independently of this test. The identity theorem,
component by component, identifies them throughout that disk,
and continuity gives equality at its boundary. This proves (14)
without assuming that the full new tube lies in (9).
Failure of a condition is only an inconclusive certificate.

## 4. Fixed bounded implementation

The new standalone implementation is
[certify_mixed_terminal_correlated_affine_family.py](../experiments/certify_mixed_terminal_correlated_affine_family.py).
It imports no old evaluator and no floating proposal package.
Its only proposal source is the frozen
[first affine result](../repro/results/research-mixed-terminal-affine-family.json),
SHA256 908232a2fc15d731c13803cd503c7b0d70c579f9cbf1896543f7233df2196370.
All four original \((\beta,\epsilon)\) cases, exact \(q^0,B,u\),
parameter centers and radii are preserved. The original reference
record and its saved audit, all inherited input hashes, and both
old and new proof/script identities are checked before and after.

Use 256-bit outward arithmetic, the same disks \(D_3,D_4\), and
exactly the four multipliers \(1/4,1/2,1,2\) applied to
\[
              (1/500,1/1000,1/200,1/200,1/100).
 \tag{15}
\]
All sixteen candidates are retained, even after a successful one.
Every failed domain guard, negative inclusion margin, nonfinite
calculation or unexpected error remains visible. There is no
subdivision, alternate center, inverse, response, radius or precision,
and no automatic follow-up.

The record saves the exact decomposition, center primitive values,
point Jacobian, preconditioned central/linear defects, exact
\(\lambda_\ell,Bv_\ell\), outward disk radii, strip distances and
sine/curvature enclosures. Every summand of (11)--(12), all five
inclusion margins, central-root containment witnesses and the
weighted contraction factor are retained. Whether the larger
coordinate tube lies in (9) is saved separately and never substituted
for the required original-log strip tests.
Only strict rational endpoint comparisons can certify a candidate.
The fresh output path is
repro/results/research-mixed-terminal-correlated-affine-family.json.

A successful result would enclose critical coordinates, not prove a
uniform terminal-source gap or nonzero coefficient. Existing
type-four source comparisons retain their reduced, inverse-feasible
domain restrictions. This certificate does not extend them to a
larger input annulus merely by establishing root existence there.
