# Real cut gaps for both original first-cap sums

Research lemma, 5 November 2026. The result concerns the correlated
endpoint critical points already constructed for every open three/four
word. It supplies the two real-cut inequalities in the
[outer-contour criterion](research_mixed_cap_outer_contour_reduction.md),
and a lower bound for the selected cap rate. It does not estimate the
horizontal Fourier contributions or all discarded real rows.

## 1. Phase and parameter set

Retain the original normalized sine primitive \(J\) and put
\[
 \begin{split}
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 g(e)&=J(e)+i\pi(e-e^2)/2,\\
 P_\epsilon(e,t,u)&=F(e,u)+J(e+t)-J(t)-i\pi et-\epsilon g(e).
                                                               \tag{1}
 \end{split}
\]
Here \(\epsilon=0,1\) means an original three- or four-crossing
block, \(e\) is its private leg, \(t\) its outgoing attached
leg, and \(u\) its ordinary endpoint coordinate.

For every external input in either original typed disk, use the
correlated triple \((e_*,t_*,u_*)\) of the
[four endpoint maps](research_mixed_open_word_critical_localization.md).
Include also the two one-vertex solutions, where \(t_*=e_*\).
In each case \(u_*=u_c(e_*)\), and the selected cap rate is
\[
                  M_\epsilon=\Re P_\epsilon(e_*,t_*,u_*). \tag{2}
\]
The full complex phase is unchanged. In particular the type-four
reciprocal factorial belongs to the private variable \(e\).

**Theorem 1.** On all these correlated endpoint images,
\[
 M_\epsilon>1,\qquad
 M_\epsilon-
 \Re P_\epsilon(c,t_*,u_c(c))>\frac1{2000}
       \quad(c=27/100,49/100).                            \tag{3}
\]
The two cuts are those of the
[proved endpoint rectangle](research_mixed_endpoint_cap_rectangle.md).
The theorem holds for either endpoint and every fixed word length.
It makes no claim on the entire independent product of the private
and attached rectangles.

## 2. A Taylor bound that retains the critical cancellation

Each of the 5,258 original endpoint witnesses encloses the actual
triple in a product of complex disks of radius \(\rho\), centered
at an exact rational triple \((e_0,t_0,u_0)\). The same description
applies to the two one-vertex witnesses after repeating the leg center
in the \(e\) and \(t\) positions.

For a holomorphic function \(A\) on this product, its value at any
point \(z_0+\delta\), \(|\delta_j|\le\rho\), satisfies
\[
 \Re A(z_0+\delta)\ge
 \Re A(z_0)-\rho\sum_j|A_j(z_0)|
        -\frac{\rho^2}{2}\sum_{j,k}\sup|A_{jk}|.          \tag{4}
\]
This is the integral Taylor formula on the segment
\(z_0+s\delta\), \(0\le s\le1\). It uses the actual
complex disk radii. Replacing them by independent real-coordinate
errors, or bounding the dilogarithms separately on a large rectangle,
unnecessarily loses the small cut margin.

Apply (4) first to \(A=P_\epsilon\), then to
\[
 A_c(e,t,u)=P_\epsilon(e,t,u)-P_\epsilon(c,t,u_c(c)).       \tag{5}
\]
All primitives in these formulas remain on their original regular
sine strips. Their exact first derivatives are
\[
 \begin{split}
 P_e&=-J'(e-u)+i\pi u+J'(e+t)-i\pi t-\epsilon g'(e),\\
 P_u&=2J'(1/2-u)-3J'(u)+J'(e-u)+i\pi e,\\
 P_t&=J'(e+t)-J'(t)-i\pi e,\\
 (A_c)_t&=J'(e+t)-J'(c+t)-i\pi(e-c).
 \end{split}                                               \tag{6}
\]
The \(e\) and \(u\) derivatives of \(A_c\) equal those
of \(P\). They vanish at the actual critical triple, but (4)
retains their computed residuals at the rational centers.

For the Hessian, abbreviate
\[
 B=\pi\cot\pi(e-u),\quad C=\pi\cot\pi(e+t),\quad
 H=\pi(2\tan\pi u+3\cot\pi u).
\]
In the order \((e,t,u)\), the common entries are
\[
 \begin{split}
 P_{ee}&=-B+C-\epsilon\pi\cot\pi e+i\epsilon\pi,&
 P_{et}&=C-i\pi,\\
 P_{eu}&=B+i\pi,&P_{uu}&=-H-B,\qquad P_{tu}=0.
 \end{split}                                               \tag{7}
\]
The remaining diagonal entry is
\[
 P_{tt}=C-\pi\cot\pi t,\qquad
 (A_c)_{tt}=C-\pi\cot\pi(c+t).                           \tag{8}
\]
The two off-diagonal nonzero entries are counted twice in the sum
in (4). These formulas give direct outward Hessian bounds on the
Cartesian squares containing each certified complex disk.

## 3. Complete extraction from the existing witnesses

The checker binds the author and saved replay of the original
endpoint maps, and the exact
[endpoint-rectangle extraction](research_mixed_open_word_endpoint_rectangles.md).
That extraction has already checked the four complete parameter
trees and every rational output disk. The present checker evaluates
(4), (6)--(8) on every one of those disks, and on both separate
one-vertex disks. It does not propose roots, shrink output disks,
subdivide parameter cells, or discard a difficult boundary input.

Every disk passes \(M>1\) and both cut losses \(>1/2000\).
The original critical-point theorem supplies the actual root in each
disk and identifies every open-word endpoint with one of the four
maps. Therefore (4) proves (3) on the entire correlated images.
Strict margins and compactness also retain the cut inequalities on
a small neighborhood of those images. This proves Theorem 1.

Run

```sh
python3 experiments/check_mixed_cap_real_cut_gaps.py --precision 256
```

A replay at higher precision reevaluates the same witnesses. Its
input record is bound to this proof, the checker and all mathematical
dependencies. The nonzero full cap asymptotic still requires the
remaining hypotheses of the outer-contour criterion.
