# The seam collar for every actual next-three and next-four output

Research corollary, 8 November 2026. Retaining the sign of the
actual next-three output height completes the seam estimate on
all ordinary-next reference families. Together with the terminal
cases already proved, this covers both original Fourier densities
for both next letters. The collar is still a fixed small
neighborhood of \(Y=1\), not a full coefficient contour.
No numerical evaluation is used.

## 1. The original action when the ordinary next-three output is above zero

Use the actual coordinates \(y=t_2,\ s=s_3,\ z=t_3\), with
\(y=q_{34}(s)\), and the original conditional action
\(\mathcal P_0^+\) from
[the local next-source theorem](research_mixed_three_four_next_local_source.md).
Write \(x_v=\Re v\), \(h_v=\Im v\). The original action identity
is
\[
 \mathcal P_0^+(-2,z)-\mathcal P_{34}(-2,y)
       =W(y,s)+W(s,z)-g(y)-2\pi isz.
 \tag{1}
\]
The two pair lower bounds in
[the physical end-sector theorem, equations (17)--(22)](research_mixed_three_four_next_physical_end_sector.md)
and the retained incoming-factorial bound in
[the low-index kernel margin, Section 3](research_mixed_next_low_index_kernel_margin.md)
give
\[
 \Re\mathcal P_0^+(-2,z)>
 \frac74+\frac25+\chi+
       \pi\{h_s(x_z-x_y)+x_s(h_z-h_y)\},
 \qquad \chi=\frac{117}{800\pi}>\frac9{200}.
 \tag{2}
\]
Here the complete old prefix has real action greater than \(7/4\);
all primitives and the conditional output gauge are unchanged.

For the ordinary-next-three family the established typed ranges are
\[
 \begin{gathered}
 x_y\in[.24,.36],\qquad h_y<0,\\
 x_s,x_z\in[.267,.433],\qquad
 h_s\in[-13/200,17/250].
 \end{gathered}
 \tag{3}
\]
Suppose \(h_z\ge0\). Then \(x_s(h_z-h_y)>0\), so this term
can be dropped favorably. Also
\[
 x_z-x_y\in[-93/1000,193/1000].
 \tag{4}
\]
If the product with \(h_s\) is negative, its two possible
opposite-sign cases give respectively
\[
 h_s(x_z-x_y)\ge
 -\frac{13}{200}\frac{193}{1000}
       =-\frac{12545}{10^6},
 \qquad
 h_s(x_z-x_y)\ge
 -\frac{17}{250}\frac{93}{1000}
       =-\frac{6324}{10^6}.
 \tag{5}
\]
Nonnegative products satisfy the same common lower bound.
Since \(\pi<22/7\) and \(12545\cdot22=275990<280000\),
\[
 \frac{12545\pi}{10^6}<\frac1{25}.
 \tag{6}
\]
Substituting (5)--(6) into (2) proves the actual action estimate
\[
 \boxed{\quad
 \Re\mathcal P_0^+(-2,z)>
 \frac{43}{20}+\frac9{200}-\frac1{25}
                  =\frac{431}{200},
       \qquad h_z\ge0 .
 \quad}
 \tag{7}
\]
This uses the correlation between the sign of the actual output
height and the original chirp contribution. It does not claim (7)
on an independent output box or for negative output height.

## 2. Complete finite source consequence

Keep the exact functions, the original \(+N\) extraction measure,
and both densities
\[
 D_{\sigma,\beta,N}(w,Y,Z)
   =F_{34,N}(w,Y)d_N(Y)Y^{-\sigma N}C_{\beta,N}(Y,Z),
       \qquad \sigma,\beta\in\{0,1\},
 \tag{8}
\]
from [the complete-source seam theorem](research_mixed_next_complete_source_seam_collar.md).
Its full-row bound on the typed next-three disk
\(|Z|\le e^{17\pi/125}\) has limiting rate
\[
       \frac{31621}{15000}<\frac{211}{100}.
 \tag{9}
\]
The additional cost on \(|Y-1|\le\varepsilon\) is the explicit
quantity \(3\Omega(\varepsilon)-2\log(1-\varepsilon)\to0\),
with \(\Omega\) as in that theorem. Equations (7)--(9) leave
the strict reserve
\[
                  \frac{431}{200}-\frac{211}{100}
                            =\frac9{200}>0.
 \tag{10}
\]
Thus the complete seam theorem applies to ordinary-next-three
outputs with \(h_z\ge0\). Outputs with \(h_z\le0\) already satisfy
its unit-disk comparison. Both closed subfamilies have strict
reserves at \(h_z=0\); compactness gives fixed local neighborhoods,
without requiring a height sign for nearby complex parameters.

Consequently one sufficiently small fixed collar works for
**every actual ordinary and terminal next-three or next-four
reference**. It gives the all-real ordinary-color bounds with the
complete-color action as normalization, both level parities, and
the same normalized fixed mixed-derivative loss \(1/2000\) on
smaller complete-color and actual-output neighborhoods.
The terminal-third graph is covered by its own already proved
typed action comparison, not by an ordinary-next supporting plane.

The conclusion also holds for the specific older \(11/12\)
filtered prefix \(F_N^{\rm mid}\). For the additional ordinary-three
subfamily, its complete correction density has the smaller limiting
rate \(5121/2500<17/8<431/200\), by Section 5 of the seam theorem.
Hence the exact subtraction \(F_N^{\rm mid}=F_N-E_N^{\rm all}\)
preserves the collar estimate with the same scope.
No later \(8/9\) filtering bound is imported.

All original factors, including \(d_N\)'s polynomial forcing and
the selected multiplier \(Y^{-N}\), remain in (8). Integrals over
fixed paths contained in the collar retain their original factor
\(N\) and have the same exponential gap. The collar is not
asserted to reach either the prescribed selected height \(1/100\)
or an actual negative critical height. Long paired-contour sides,
the transitions to the central paths, and the remaining middle
source still require their own estimates. No full next-transfer
or short-filling knot theorem is asserted.
