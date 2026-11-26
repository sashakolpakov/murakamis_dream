# Two complete incident blocks near the hybrid zero seam

Research proof, 5 November 2026. The complete 256-bit author cover
passed all 2,048 boundary products on 18,988 accepted cells, testing
all sixteen target corners on every cell. The source reduction and
window geometry are established inputs. Completed input artifacts
remain unchanged.

## 1. Original geometric comparison

Use the exact phases, source constants and normalization of the
[grouped seam reduction](research_mixed_hybrid_zero_pair_reduction.md).
For three consecutive actual critical legs \((a,b,c)\), with
type indicators \((\alpha,\beta,\gamma)\), put
\[
 F=\phi_{\alpha\beta}(a,b)+\phi_{\beta\gamma}(b,c),\qquad
 P_L=F_a,\quad P_R=F_c,\quad C=F-P_La-P_Rc,
\]
\[
 Q(a,c)=\frac{151}{20}(\Im a)^2+\frac{11}{2}(\Im c)^2.
                                                               \tag{1}
\]
The original middle equation is exactly \(F_b=0\); it is not a
numerically small gradient assumption. The original zero lifts and
the additive constant of \(g\) remain in \(F\).

Define the target rectangles
\[
 T_3=[0,1]+i[-.03,.02],\qquad
 T_4=[0,1]+i[-.057,.014].                                    \tag{2}
\]
These are geometric comparison domains. The physical type-four
source states remain separate: unselected heights are in
\([-.057,0]\), selected heights in \([0,.014]\).
No source continuation of a fixed selection through the opposite-sign
band is claimed.

**Theorem 1.** For every fixed finite cyclic type-three/type-four word,
every actual consecutive critical triple, and every
\(z_L\in T_{3+\alpha}\), \(z_R\in T_{3+\gamma}\),
\[
 \Re(C+P_Lz_L+P_Rz_R)
       -A_{\beta,\alpha}-B_\gamma-Q(a,c)>\frac14.             \tag{3}
\]
The constants are the literal complete endpoint-source ceilings
\[
 (A_{00},A_{01},A_{10},A_{11})
   =(.360050,.447948,.485081,.551147),\qquad
 (B_0,B_1)=(.347548,.515591).
                                                               \tag{4}
\]
The references need not be distinct. The ordered pair and its
incidences retain their original multiplicities in short cycles.

## 2. Complete reference-boundary certificate

Use a five-vertex original open window, numbered zero through four,
whose right legs are \(t_0,\ldots,t_4\). Set
\((a,b,c)=(t_1,t_2,t_3)\); its two conditional roots are the
original \(s_2,s_3\). The window equation at \(t_2\) is precisely
\(F_b=0\). The existing
[window theorem](research_mixed_cyclic_critical_height_bounds.md)
proves the holomorphic branch on a neighborhood of each full external
reference product. Its external rectangles are
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].                                \tag{5}
\]
Every actual cyclic reference configuration is included, also after
repeating a period of length one or two.

For fixed references, the left side of (3) is affine in the real and
imaginary parts of both targets. Its minimum is at one of the sixteen
products of target corners in (2). For a fixed such corner, the
negative of that expression is a real part of a holomorphic function
of the two external reference parameters plus the positive multiples
of squared imaginary parts in \(Q\). It is separately subharmonic.
The established whole-product branch therefore permits successive
maximum principles to reduce the comparison to the distinguished
boundary. No boundary argument is used to prove branch existence.

There are 32 ordered window words, four external type pairs and sixteen
external-side products, giving exactly 2,048 boundary domains. Each
domain has two real parameters. The checker encloses the original
ten-variable logarithmic zero with the frozen affine Newton primitive.
It recomputes the two external derivatives using the checked residual,
four Neumann corrections and a \(\rho^5/(1-\rho)\) weighted-norm
tail. Global norm maxima use explicit outward upper endpoints.

At each cell midpoint, a fresh Newton enclosure supplies the phase
and tangent coefficients. The full-cell derivative used for the
mean-value error is exactly
\[
 \begin{split}
 d\mathcal G={}&
 \Re\{(z_L-a)\,dP_L+(z_R-c)\,dP_R\}\\
 &-\frac{151}{10}\Im a\,\Im da-11\Im c\,\Im dc,
 \end{split}                                               \tag{6}
\]
where \(\mathcal G\) denotes the left side of (3). Equation (6)
uses \(F_b=0\) and retains both complex target-height terms and
both exterior debits. The condensed block Hessians and the full
window response give \(dP_L,dP_R\). Each of the sixteen target
corners is checked outward on every accepted cell.

Every domain requires an exact prefix-free binary cover of total area
one. The full 2,048-element case set is checked for uniqueness and
completeness. Saved-cover replay reevaluates each cell and never uses
its former bound as evidence. Source constants, proof, code, helper,
input record and inherited bindings are immutable during the run.
The complete run used 35,928 cell visits and 206.95 seconds, within
the declared 900-second limit. Its smallest outward lower bound was
greater than (0.30347868), above the required (1/4).
Together these comparisons and the maximum principles prove (3).

## 3. Complete finite pair on a fixed real collar

Put \(\ell=1/1000\), and let \(0\le x\le\ell\). The middle
target has height zero. The two other targets have arbitrary real
parts in \([0,1]\) and their physical typed height states described
after (2). Let \(\mathcal B_{\eta\epsilon,N}^{\sigma_0,\sigma_1}
(u,v)\) denote the original allocated kernel modulus with its two
actual Fourier halfweights and selected factors. It uses the same
literal \(C_{\epsilon,N}\) and \(d_N\) as the source reduction.

**Corollary 2.** Uniformly on these targets, both parities and every
allowed selection satisfy
\[
 \mathcal B_{\alpha\beta,N}^{\sigma_L,\sigma_b}(z_L,x)
 \mathcal B_{\beta\gamma,N}^{\sigma_b,\sigma_R}(x,z_R)
 \le C N^A\exp N\left\{
     \Re(C+P_Lz_L+P_Rz_R)-Q(a,c)-\frac15\right\}.           \tag{7}
\]
The estimate also holds when each kernel modulus is replaced by the
sum of its absolute original rows. It includes both periodic seam
representatives for each other angle and the exact middle endpoint
\(x=0\).

Indeed, the source reduction gives raw rate
\(A_{\beta,\alpha}+B_\gamma+2\Delta_\ell+\beta\nu_\ell\)
with an arbitrarily small fixed total Fourier tolerance. Its proved
collar cost is
\[
 2\Delta_\ell+\beta\nu_\ell
                  \le2\Delta_\ell+\nu_\ell<\frac1{50}.
\]
Choose the total tolerance below \(1/100\). Combining with (3)
leaves more than \(1/4-1/50-1/100=11/50>1/5\).
The sum of the two complex tangent planes is exactly
\(C+P_Lz_L+P_Rz_R\), since \(F_b=0\), so no low-angle tangent
error is omitted.

The complex first-argument chirp in the left block remains in
\(A_{\beta,\alpha}\). The changed first-argument chirp in the
right block has modulus one because \(x\) is real. The two middle
Fourier halves recombine into power \(\beta\); the selected middle
frequency factor also has unit modulus. Thus the collar budget retains
every row, forcing term and original normalization. No conditional
root or derivative at the zero target is used.

## 4. The limited exterior interpretation

The debit \(Q\) in (7) is always a reserved cost. It estimates actual
exterior blocks under the following additional hypotheses only.
Take four distinct consecutive blocks with five target coordinates.
The middle target is \(x\in[0,\ell]\); the other four real parts
belong to \(P=[.22,.45]\). The two neighbors may have arbitrary
fractions of their reference heights when unselected, or of \(H\)
when selected. The two farther exterior coordinates retain their
prescribed heights, reference heights when unselected and \(H\)
when selected.

For the left exterior block, changing only its second height costs
at most \((151/20)(\Im a)^2\). For the right exterior block,
changing only its first costs at most \((11/2)(\Im c)^2\).
These are the complete [oriented reset costs](research_mixed_oriented_height_reset.md),
allowing both real parts to readjust. A partially selected neighboring
height is bounded by the corresponding full debit through
[selected-height interpolation](research_mixed_partial_selected_heights.md).
A selected farther coordinate gives the stronger selected/reset or
selected/selected bound. Thus all selections are retained, with no
replacement of a fixed selection through an opposite-sign band.

**Corollary 3.** Under precisely these four-block hypotheses, the
product of the four original allocated finite blocks is at most
\[
 C N^A\exp N\left\{
                   \Re\sum_{v=1}^4\Gamma_v-\frac15\right\}.
                                                               \tag{8}
\]
Use (3) and the raw collar bound directly, and spend a total tolerance
below \(1/100\) over all four blocks together. The exterior debits
cancel \(Q\), and the remaining reserve is still greater than
\(11/50\). This budgets the tolerances once; it does not multiply
(7) by additional positive tolerances at its already rounded gap.

The four edges must be distinct, hence this interpretation requires
cycle length at least four. At length four the farther exterior
coordinates may coincide, while the four edges remain distinct.
The pair comparison (3)--(7) itself keeps short-cycle multiplicities.
The hybrid contour satisfies the stated isolated-plateau hypotheses
when the surrounding heights are unaffected by other low coordinates.
Overlapping seam stars, reset exteriors outside the plateau, or an
arbitrary low-region contribution require separate incidence/source
arguments. No such global conclusion is made here.

## Reproduction

```sh
python3 experiments/certify_mixed_hybrid_zero_pair_support.py --precision 256
python3 experiments/certify_mixed_hybrid_zero_pair_support.py --precision 320 --input repro/results/research-mixed-hybrid-zero-pair-support.json --output /tmp/research-mixed-hybrid-zero-pair-support-review.json
```

The author record transparently retains the proof hash used by its
complete numerical run. The subsequent proof-only refresh changes
validation status, records the counts, and repairs the displayed
cross-reference; it changes no hypothesis, inequality, source input,
or acceptance code. A saved-cover replay binds the final proof.
