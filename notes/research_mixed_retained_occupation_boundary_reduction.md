# Keeping the original interior loss in a finite boundary comparison

Research deduction, 6 November 2026. The finite-window argument optimizes
two long intervals before fixing their central coordinates at the
reference point. Some deviations of the original configuration disappear
during this operation. A useful strengthening is to reserve a fixed
fraction of the original occupation loss before optimizing. The resulting
boundary comparison retains that loss at the original configuration,
including on coordinates which the optimization later changes.

This is a sufficient comparison theorem. The global signs of the new
boundary functions are not asserted. Their local maximum at the geometric
reference is verified below, so the strengthening does not introduce a
new local obstruction there.

## 1. The source estimate and the two configurations

Use the notation and hypotheses of
[the finite boundary-window theorem](research_mixed_open_finite_boundary_windows.md).
The same argument applies after the
[exact terminal contraction](research_mixed_contracted_boundary_collar_completion.md),
Sections 1 and 3: the boundary products then contain the whole terminal
polynomial \(\mathcal V_N\), while the ordinary middle rates and their
closing terms are unchanged. No estimate of an uncontracted modulus is
substituted for that polynomial.

Let \(I\) be the safe interval of ordinary symbols. The real coordinates
are \(x_j\), their original reference values are \(a_j\), and
\(\sigma_j\) records the permitted Fourier selection. Set
\[
 P=[.22,.45],\qquad
 p_j=\min\{1,\sigma_j+
          400(\operatorname{clamp}_{P}x_j-a_j)^2\},\qquad
 \mathcal O(\mathbf q)=\sum_{j\in I}p_j,\qquad
 \kappa=\frac1{20000}.
 \tag{1}
\]
The symbol \(\mathbf q\) denotes the original configuration, before
any optimization. All penalties outside \(I\) are defined to be zero.
The complete middle defect \(D_I\) and the two literal boundary
functions satisfy
\[
 D_I(\mathbf q)\ge\kappa\mathcal O(\mathbf q),\qquad
 F_N(\mathbf q)=B_{L,N}+B_{R,N}-D_I(\mathbf q).
 \tag{2}
\]
Both original boundary derivatives and all allocated weights are
included in \(B_{L,N},B_{R,N}\). The previously proved source bound is
\[
 N^{-1}\log|\mathscr J_N|-M_{\rm open}
       \le F_N+\tau+O_m(\log N/N)
 \tag{3}
\]
for any prescribed total rate tolerance \(\tau>0\). The word is fixed
when \(N\) tends to infinity.

Fix \(\eta\ge0\) and a uniform bound
\(B_{L,N}+B_{R,N}\le K\). Write
\[
 B=\left\lfloor\frac{K+\eta}{\kappa}\right\rfloor,\qquad
 d=352,\quad \ell=2d+7,\quad R=(B+1)\ell .
 \tag{4}
\]
Assume \(|I|\ge6+2R\), with the safe reference halo required by the
finite-window theorem. If \(F_N>-\eta\), (2) implies that at most
\(B\) symbols are selected or outside \(P\). The two groups of
\(B+1\) blocks therefore contain disjoint unselected plateau blocks
of length \(\ell\), one near each end. The first and last three
symbols of \(I\) remain protected.

Optimize the interior of each chosen block and then fix its central
three coordinates at their reference values, as in that theorem.
Let \(D_L,D_M,D_R\) be the three resulting residual energies. They
refer to the modified configuration; they are not substituted into
the definition of \(\mathcal O(\mathbf q)\). Let \(\xi_L,\xi_R\)
be the displacements of the two outer fixed endpoints of these
blocks. The relative pinning estimate gives
\[
 F_N\le
 [B_{L,N}-D_L+a_d\xi_L^2]
 +[B_{R,N}-D_R+a_d\xi_R^2]
 -\frac{\kappa}{2}\mathcal O_M^{\rm pin},\qquad
 a_d=1000(99/101)^{2d}.
 \tag{5}
\]
Here \(\mathcal O_M^{\rm pin}\) is the occupation of the resulting
middle component. The two boundary products have not changed.

## 2. Reserve part of the loss before optimizing

Fix \(0<\theta<1\). For each permitted block position define the
two expressions
\[
 \begin{split}
 T_{L,N}^{\theta}
   &=B_{L,N}-(1-\theta)D_L+(1-\theta)a_d\xi_L^2,\\
 T_{R,N}^{\theta}
   &=B_{R,N}-(1-\theta)D_R+(1-\theta)a_d\xi_R^2 .
 \end{split}
 \tag{6}
\]
Let \(\mathcal T_{L,N}^{\theta},\mathcal T_{R,N}^{\theta}\) be
their suprema over the same bounded-width boundary domains and
block positions used in the finite-window theorem. The original
reference data remain admissible data from the actual open word.
Taking the two suprema independently is a sufficient relaxation;
it does not assert independent realizability of their reference data.

**Theorem 1.** Every original configuration satisfies
\[
 F_N(\mathbf q)\le
 \max\left\{-\eta,\,
   \mathcal T_{L,N}^{\theta}+\mathcal T_{R,N}^{\theta}
                    -\theta\kappa\mathcal O(\mathbf q)\right\}.
 \tag{7}
\]
For configurations with \(F_N>-\eta\), the stronger pointwise bound
is
\[
 F_N\le T_{L,N}^{\theta}+T_{R,N}^{\theta}
       -\theta\kappa\mathcal O(\mathbf q)
       -(1-\theta)\frac{\kappa}{2}\mathcal O_M^{\rm pin}.
 \tag{8}
\]

*Proof.* Before making any change to the configuration, (2) gives
\[
 F_N\le B_{L,N}+B_{R,N}
            -(1-\theta)D_I(\mathbf q)
            -\theta\kappa\mathcal O(\mathbf q).
 \tag{9}
\]
Apply the same two optimizations and pins to the term
\((1-\theta)D_I\). Its pinning fees and all three resulting
energies are multiplied by \(1-\theta\). The two inner fees are
still paid by half of the middle occupation, because both the
fee and the available bound have been multiplied by the same
positive number. This gives (8).

The discarded term in (9) still refers to the original
configuration. No invariance of occupation under optimization
is assumed. Drop the last nonpositive term in (8) and take the
two finite suprema to obtain (7) when \(F_N>-\eta\).
The other configurations already satisfy its first alternative.
\(\square\)

For example, suppose the new boundary comparison gives
\[
 \mathcal T_{L,N}^{\theta}+\mathcal T_{R,N}^{\theta}
                         \le C\log N/N .
 \tag{10}
\]
On any region with \(\mathcal O(\mathbf q)\ge\rho>0\), (7)
then gives the uniform upper rate
\[
 \limsup_{N\to\infty}\sup_{\mathcal O\ge\rho}F_N
                \le-\min\{\eta,\theta\kappa\rho\}.
 \tag{11}
\]
Take \(\eta>0\) to obtain a strict loss. Equation (3), with a
sufficiently small prescribed tolerance, transfers a smaller strict
loss to the finite source. Integration and the finite sum of
selections cost only polynomial factors for a fixed word.
This conclusion includes deviations which the optimization or
pinning has removed.

## 3. The stronger boundary test is compatible with the local saddle

The new comparison (10) is stronger than the old boundary test;
its sign does not follow from the old sign. Nevertheless it has
the same strict local maximum at the reference if \(\theta\)
is small enough, with an explicit choice independent of word length.

Consider one pinned boundary component at complete ordinary colors,
with no selected coordinates and all free coordinates in a
sufficiently small plateau neighborhood of the reference. Write
\(\xi\) for their real displacements. Section 6 of the finite-window
theorem proves that the leading rate of its old bracket obeys
\[
 \operatorname{rate}(B_{\partial,N}-D_\partial
                         +a_d\xi_\partial^2)
                           \le-\frac16\|\xi\|_2^2 .
 \tag{12}
\]
This bound includes the literal endpoint phase and the exact
remaining boundary derivative.

On this unselected plateau, \(D_\partial\) is a sum of the original
safe ordinary edge energies. Each energy and its gradient vanish
at its reference pair. The
[plateau Hessian bound](research_mixed_plateau_boundary_forgetting.md),
equation (3), bounds its Hessian above by \(20I_2\). Taylor's
formula therefore bounds each edge energy by ten times the sum
of its two squared displacements. Each coordinate meets at most
two of these original edges, so
\[
                  0\le D_\partial\le20\|\xi\|_2^2 .
 \tag{13}
\]
Fixed coordinates outside this component have zero displacement.
No estimate of an endpoint Hessian is needed in (13).

The new bracket differs from the old one by
\(\theta D_\partial-\theta a_d\xi_\partial^2\).
Choose \(\theta=1/240\). Equations (12)--(13) give
\[
 \operatorname{rate}T_{\partial,N}^{1/240}
             \le-\left(\frac16-\frac{20}{240}\right)\|\xi\|_2^2
             =-\frac1{12}\|\xi\|_2^2 .
 \tag{14}
\]
At this choice the retained original occupation coefficient is
\[
                         \theta\kappa=\frac1{4800000}.
 \tag{15}
\]
These are statements about the leading rate. The exact finite
logarithms retain their polynomial prefactors, as in (3) and (10).

The global comparison (10) remains to be proved outside this
local neighborhood, including selected boundary states. Also,
\(\mathcal O\) counts only the safe middle: deviations confined
to the physical boundary regions still require the boundary
functions themselves to have the appropriate strict gap.
No whole-source asymptotic, short-filling stability, or
finite-exceptions theorem follows without those remaining signs.
