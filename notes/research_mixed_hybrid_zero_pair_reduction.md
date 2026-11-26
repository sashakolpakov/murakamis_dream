# Grouping the two blocks at the hybrid contour's zero seam

Research reduction, 4 November 2026. The complete-source reductions in
Sections 1--3 are proved from existing finite estimates. The geometric
comparison in Section 4 is diagnostic only: its full distinguished-
boundary cover has not been certified. No new universal support bound
or whole-period theorem is asserted.

## 1. The exact local contour and original pair

On the [periodic hybrid contour](research_mixed_split_cutoff_hybrid_contour.md),
a low coordinate \(x\in[0,\varepsilon]\) has height zero. The
slow and fast neighboring cutoffs both take the value
\(\lambda=1-x/\varepsilon\) there. If its neighbors and the next
two coordinates lie in the plateau \(P=[.22,.45]\), the two
neighbors have heights \(\lambda c_a,\lambda c_c\), where
\(c_j=\Im r_j\) if unselected and \(c_j=H=.014\) if selected.
The next two heights remain at their prescribed values. More general
configurations can attenuate a neighbor further; they must not be
identified with this isolated configuration.

Let the actual consecutive critical reference legs be \((a,b,c)\),
of types \((3+\alpha,3+\beta,3+\gamma)\), and write
\[
 F(a,b,c)=\phi_{\alpha\beta}(a,b)+\phi_{\beta\gamma}(b,c),
 \quad P_L=F_a,\quad P_R=F_c,\quad
 C=F-P_La-P_Rc.                                             \tag{1}
\]
The phases retain the original primitive, logarithmic lifts and
half-factorial allocations. The original middle critical equation is
\(F_b=0\). Hence the sum of the two full complex tangent planes at
targets \((z_L,x,z_R)\) is exactly
\[
                         C+P_Lz_L+P_Rz_R,                   \tag{2}
\]
independently of the real low angle \(x\). The existing five-vertex
open-window theorem establishes this equation and a holomorphic branch
on each full external typed reference product before any boundary
maximum principle is used. Every fixed cyclic word appears in such a
window after period repetition if necessary.

The actual finite kernels are
\[
 C_{e,N}(X,Y)=\sum_{j=0}^{N-1}
          \frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+e}},\qquad
 p_j(X)=(r_NX;r_N)_j,\quad P_j=(r_N;r_N)_j,
\]
with the original polynomial \(d_N\), its selected factors
\(X^{-N\sigma}\), and both parities unchanged. At the seam,
\(p_j(1)=P_j\) and \(d_N(1)=1\) exactly. The middle Fourier
allocation thus contributes no exponential rate at \(x=0\).

## 2. Constant endpoint source ceilings on full height bands

The height-zero and nonzero endpoint support grids already bound all
original rows and all other real angles. Only their certified
\(\kappa=0\) entries are needed here. The full target bands are
\[
 \begin{array}{c|c|c}
 \text{type indicator}&\sigma&h\\\hline
 0&0&[-.03,.02]\\
 1&0&[-.057,0]\\
 1&1&[0,.014].
 \end{array}                                               \tag{3}
\]
The negative and positive type-four bands have different selected
factors and are treated separately before taking a common ceiling.

More explicitly, number the arguments zero and one and put the
endpoint in argument \(c\). The exact moving
row is
\[
 R^{(c)}_{e,j}(X)=X^{-cj}\frac{p_j(X)}{P_j^{1+e}}.
                                                               \tag{4a}
\]
Thus a complex first argument retains the nonunit factor
\(|X^{-j}|=e^{-2\pi h j}\). Its full raw exponent, with the
moving halfweight, is
\[
 I_h(u,y)-(1+e)J(u)-2\pi c h u
 +\frac d2\{\max(\nu_h(y),2\pi h_+)-2\pi\sigma h\},
                                                               \tag{4b}
\]
where \(I_h\) is the original product integral and
\(\nu_h=-\Re g\). This is exactly the expression bounded by
the source grids. Both alternatives of the actual \(d_N\) remain,
including at real angles zero and one. The selected factor
\(X^{-N\sigma}\) is retained in (4b).

For an endpoint in the second argument, the following constants
bound the raw rate, including the moving argument's halfweight:
\[
 \begin{array}{c|cc}
 A_{e,d}&d=0&d=1\\\hline
 e=0&.360050&.447948\\
 e=1&.485081&.551147 .
 \end{array}                                               \tag{4}
\]
Here \(e\) is the block's own type indicator and \(d\) the moving
first argument's type indicator. For an endpoint in the first
argument, the moving type equals the own type, and the constants are
\[
                         B_0=.347548,\qquad B_1=.515591.    \tag{5}
\]
They are simply maxima of the certified endpoint entries at the
ends of each band (and height zero), not values proposed by numerical
optimization. The \((e,d)=(0,1)\) entries come from the
[original endpoint grid](research_mixed_endpoint_support_grid.md);
the other entries come from the
[all-endpoint source grid](research_mixed_all_endpoint_support.md).

Here is why the endpoint heights control the entire bands in (3).
For each row, square its modulus with its allocated halfweight.
The result is the modulus of the actual finite Laurent function
\[
             (R^{(c)}_{e,j}(X))^2 d_N(X)^d X^{-Nd\sigma}.
                                                               \tag{5a}
\]
There is no holomorphic square-root choice. On the two circles
corresponding to the band endpoints, the established full-row source
estimates hold uniformly in the real angle and row index. Hadamard's
three-circles theorem bounds every intermediate radial maximum by the
geometric interpolation of those two bounds. Taking square roots and
summing the \(N\) rows adds only a polynomial factor. This argument
applies on an annulus away from zero, where all Laurent factors are
holomorphic. It retains the forcing term in \(d_N\) and the exact
selected normalization.

**Lemma 1.** For every fixed \(\delta>0\), (4)--(5) are upper
exponents with tolerance \(\delta\) for the complete original
endpoint row sums, uniformly over all real moving angles and the
corresponding band (3). Combining the two incident edges gives the
constant source ceiling
\[
                              A_{\beta,\alpha}+B_\gamma.    \tag{6}
\]
This statement needs neither an off-grid saddle packet near the seam
nor a relation between the two moving heights.

## 3. Transfer to a fixed nonzero real collar

Let \(\ell\in(0,1/1000]\) be fixed independently of \(N\), and
write
\[
 J(u)=\Re g(u),\qquad \nu_\ell=-J(\ell),\qquad
 \Delta_\ell=\ell\log2-J(\ell).
\]
The [zero-collar argument](research_mixed_real_zero_collar.md),
Sections 2--3, applies unchanged with this fixed \(\ell\). For
\(0\le x\le\ell\), uniformly through every row and product zero,
\[
 \frac{|p_j(e^{-2\pi ix})|}{|P_j|}
           \le C N^A e^{N\Delta_\ell},\qquad
 |d_N(e^{-2\pi ix})|\le C N^A e^{N\nu_\ell}.                \tag{7}
\]
The second estimate retains the exact downward forcing recurrence;
its starting compact interval may depend on the fixed \(\ell\).
The proof does not let \(\ell\) shrink with \(N\).

Replace the low factor by its endpoint factor in each of the two
rows using (7). In the left block the complex first-argument chirp
is unchanged and remains in \(A_{\beta,\alpha}\). In the right
block the first argument is the low real angle, so changing its chirp
from \(1\) to \(e^{2\pi ijx}\) has modulus one. There is therefore
no unrecorded chirp perturbation cost. The two middle halfweights recombine into power
\(\beta\), and any middle selected factor also has modulus one.
Therefore the actual pair of allocated kernel moduli has upper rate
\[
 A_{\beta,\alpha}+B_\gamma+
                     2\Delta_\ell+\beta\nu_\ell+2\delta.   \tag{8}
\]
This bound is also valid with each kernel replaced by its absolute
row sum. Because \(2\Delta_\ell+\nu_\ell\to0\) as
\(\ell\downarrow0\), any strict geometric reserve for (6) can
absorb a fixed sufficiently small collar and the Fourier tolerances.
Equation (2) introduces no additional low-angle tangent error.

## 4. The remaining geometric test and bounded evidence

The intended grouped comparison retains the complete exterior debit
\[
                 Q(a,c)=\frac{151}{20}(\Im a)^2
                              +\frac{11}{2}(\Im c)^2.       \tag{9}
\]
The proposed inequality is
\[
 \Re(C+P_Lz_L+P_Rz_R)
       -A_{\beta,\alpha}-B_\gamma-Q(a,c)>\zeta>0.           \tag{10}
\]
The moving targets may be tested either on plateau real parts or on
the whole real period, with their full independent height bands (3).
For fixed references, the expression involving the targets is affine
in all their real and imaginary components. Its minimum is at the
four corners of each target rectangle. For a fixed target corner,
the negative of the left side of (10) is the real part of a
holomorphic reference function plus the positive height squares in
(9). It is separately subharmonic in the two external reference
parameters. Thus full reference-boundary products suffice after the
independently established window holomorphy. There is no
reference-dependent target-height substitution in this reduction.

The floating diagnostic `/tmp/diagnose_hybrid_zero_pair_constant.py`
used all 32 five-vertex words and all 64 typed external reference
corner pairs. It retained every neighbor selection, independent full
height bands and both target-angle domains. Its 9,216 comparisons
have observed minimum margin approximately .429532 on plateau targets
and .326661 on whole-period targets. The output is
`/tmp/hybrid-zero-pair-constant-diagnostic.json`.
This is reference-corner evidence only, not a certified boundary
cover or a proof of (10).

An earlier floating optimization retained the common hybrid fraction
and the sharper fraction-dependent exterior costs directly. Its
private script and output are `/tmp/diagnose_hybrid_zero_pair.py` and
`/tmp/hybrid-zero-pair-diagnostic.json`. It also found a reserve on
sampled reference centers. The simpler constant-ceiling route above
avoids relying on those numerical source extrema or on a
height-coupled reference maximum principle.

For the exterior interpretation of (9), the two neighboring real
coordinates and the next two coordinates must lie in the plateau;
the farther heights must remain prescribed. An unselected neighbor
at any fraction of its reference height costs at most its full
oriented reset charge. A selected neighbor at any fraction of \(H\)
has the same ceiling by the partial-selected-height theorem; a
selected farther coordinate improves the bound. Outside these
hypotheses, (9) is only a reserved numerical cost, not an estimate
for an unproved adjacent block. Overlapping stars and the short-cycle
incidence cases require explicit assembly. No arbitrary low-region
or whole-cycle conclusion is asserted here.

The focused checker validates the exact source-table extraction,
endpoint row normalization, Fourier allocation and the collar budget
\(2\Delta_{1/1000}+\nu_{1/1000}<1/50\). It checks no geometric
support comparison:

```sh
python3 experiments/check_mixed_hybrid_zero_pair_reduction.py
```
