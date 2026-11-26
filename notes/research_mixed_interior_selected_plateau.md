# Fourier selections in the interior of an open chain

Research deduction, 5 November 2026.

The completed endpoint estimates allow a useful part of the cyclic
argument to be applied to an open chain. On the central integration
region, every nonempty Fourier selection supported sufficiently far
from the two ends is exponentially smaller than the geometric
contribution. The number of positions excluded from this argument is
bounded independently of the length of the chain. This statement uses
the actual open critical point throughout.

## 1. The finite integral and the permitted selections

Fix a word \(n_j=3+\epsilon_j\), \(1\le j\le m\), where
\(m\ge2\) and \(\epsilon_j\in\{0,1\}\). Put
\[
 h=m-1,\qquad k_4=\sum_{j=1}^m\epsilon_j,\qquad
 P=[.22,.45],\qquad H=7/500.
 \tag{1}
\]
The exact terminal contraction in
[the unselected plateau theorem](research_mixed_full_unselected_plateau.md),
Section 2, leaves the variables \(X_1,\ldots,X_h\). Its summand
for a selected set \(S\subseteq\{j\le h:\epsilon_j=1\}\) is
\[
 \begin{split}
 \mathscr J_{S,N}={}&
 U_{\epsilon_1,N}(w_L,X_1)
 \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
 V_{\epsilon_m,N}(w_R,X_h)\\
 &\hspace{8mm}\cdot
 \prod_{j=1}^{h}d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j},
 \qquad \sigma_j=\mathbf 1_{j\in S}.
 \end{split}
 \tag{2}
\]
The terminal factor \(V\) already contains its entire private sum
and its original Fourier alternatives. There is no additional
selection at position \(m\) in (2).

Write the retained coordinates of the actual open critical point as
\(r_j=a_j+ic_j\). On the plateau the original contour is
\[
 z_j=x_j+i\bigl((1-\sigma_j)c_j+\sigma_jH\bigr),
 \qquad x_j\in P,\qquad X_j=e^{-2\pi iz_j}.
 \tag{3}
\]
All cutoff functions are one there. Thus these heights are constant
on the integration region, and its graph Jacobian is one.

Define the interior index set
\[
 I_m=\{j:6\le j\le m-5\}.
 \tag{4}
\]
It is empty when \(m\le10\). In the theorem below selections
are allowed only at type-four positions in \(I_m\). Every other
retained coordinate remains unselected, but its real coordinate is
free to range over all of \(P\). In particular the endpoint
coordinates are not fixed at their critical values.

## 2. Why the selected-block estimates apply to this open reference

The [open-window inheritance theorem](research_mixed_open_word_window_inheritance.md),
Theorem 1, places both legs of every vertex with
\(5\le j\le m-4\) in its final reference rectangle
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].
 \tag{5}
\]
This follows from the ordinary equations on finite windows of the
open word. It does not replace the open word by a periodic word.

An ordinary conditional factor indexed by \(j\) has retained
arguments \((r_{j-1},r_j)\). A selected position \(k\in I_m\)
is incident to precisely the factors \(j=k\) and \(j=k+1\).
Both their reference coordinates lie in the range of (5), and both
are ordinary factors. The
[selected plateau theorem](research_mixed_selected_plateau_support.md),
Theorem 1, is proved for every independent pair in (5), so it
applies to these actual open pairs. Its original conditional root
and logarithmic branch agree with those of the open word by the
uniqueness used in the inheritance theorem.

Let
\[
 E(S)=\{j\in\{2,\ldots,h\}:j-1\in S\text{ or }j\in S\}.
 \tag{6}
\]
For each \(j\in E(S)\), the entire allocated finite factor has
upper rate
\[
 \Re\Gamma_j(z_{j-1},z_j)-\frac1{200},
 \tag{7}
\]
where \(\Gamma_j\) is its full complex affine tangent at
\((r_{j-1},r_j)\). The two halfweights in this assertion are
exactly
\[
 |d_N(X_{j-1})^{\epsilon_{j-1}}X_{j-1}^{-N\sigma_{j-1}}|^{1/2}
 |d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j}|^{1/2}.
 \tag{8}
\]
Both branches of the selected Fourier bound and every finite row
are retained by that theorem. A factor with both arguments selected
is covered by the same theorem, rather than counted twice.

For every remaining ordinary factor, both arguments are unselected.
The [completed ordinary source theorem](research_mixed_three_row_source_assembly.md),
Theorem 1, bounds it by its horizontal affine tangent, with a
nonpositive quadratic remainder and any prescribed positive rate
tolerance. Because its two target heights are unchanged, this
horizontal tangent equals \(\Re\Gamma_j\). These factors need
only their proved ordinary or attached input domains; the narrow
rectangles (5) are not imposed near the two ends.

Finally, both endpoint arguments are unselected. Their entire
finite factors, with their remaining halfweights, have the upper
planes from the
[completed cap](research_mixed_first_cap_plateau_completion.md)
and [completed terminal assembly](research_mixed_full_unselected_plateau.md).
They allow independent endpoint real coordinates throughout \(P\).

## 3. The selected interior is exponentially smaller

Use the allocated endpoint phases
\[
 L(z)=\mathcal T_{\epsilon_1}(z,-2)-\frac{\epsilon_1}{2}g(z),
 \qquad
 \Pi(z)=P_{\epsilon_m}(z)-\frac{\epsilon_h}{2}g(z),
 \tag{9}
\]
and the ordinary allocated phases \(\phi_j\). Put
\[
 \Phi(\mathbf z)=L(z_1)+\sum_{j=2}^{h}\phi_j(z_{j-1},z_j)
                  +\Pi(z_h),
 \qquad M=\Re\Phi(\mathbf r).
 \tag{10}
\]
These are the action, allocation and original logarithmic constants
of the unselected plateau theorem. At the actual reference,
\(\nabla\Phi(\mathbf r)=0\). Consequently the sum of all the
complex affine tangents in (10) has real part exactly \(M\) at
every target (3). This cancels the imaginary displacement terms
at selected coordinates as well as the real displacement terms.

**Theorem 1.** For every fixed word and every nonempty permitted
\(S\subseteq I_m\), on all of \(P^h\),
\[
 |\mathscr J_{S,N}|
 \le C N^A\exp\!\left[N\left(M-\frac1{200}\right)\right].
 \tag{11}
\]
The bound holds for all sufficiently large integer levels of either
parity. It also holds on fixed sufficiently small ordinary-color
disks at both ends. Every fixed ordinary-color derivative has the
same rate on smaller disks, with its own polynomial factor.

*Proof.* Multiply the complete bounds just described, allocating
each retained weight in (2) once between its two incidences.
Stationarity cancels their affine terms. Choose the sum of all
unselected-factor and ordinary-color tolerances smaller than
\(1/400\). Before discarding any further quadratic losses, the
resulting exponent is at most
\[
 M-\frac{|E(S)|}{200}+\frac1{400}.
 \tag{12}
\]
Every component of \(S\) in the path with \(\ell\) vertices
meets \(\ell+1\) distinct edges. Different components meet
disjoint edge sets. Thus
\(|E(S)|=|S|+\#\{\text{components of }S\}\ge2\).
The strict loss in (12) exceeds \(1/200\), proving (11).

Only the two endpoint factors depend on the ordinary colors.
Their complete bounds already hold on small fixed color disks
with the chosen rate tolerances. Cauchy's formula on smaller disks
therefore proves the derivative assertion. No derivative of a
halfweight modulus is taken. All parity statements are inherited
from the literal finite-source bounds. \(\square\)

Let \(Z_N^{\mathrm{int}}\) be the sum of the plateau integrals
over all \(S\subseteq I_m\) permitted by the types, including
\(S=\varnothing\), multiplied by the original scalar
\(\kappa_N^{m+k_4}N^{m+k_4-1}\). Here \(|\kappa_N|=1\).
The number of selections is finite for the fixed word. Integrating
(11) and multiplying by this scalar changes only its polynomial
factor. Therefore
\[
 |Z_N^{\mathrm{int}}-Z_N^P|
       \le C N^B e^{N(M-1/200)},
 \tag{13}
\]
where \(Z_N^P\) is the complete unselected plateau contribution.
In particular \(Z_N^{\mathrm{int}}\) has its same nonzero
leading coefficient, unit scalar, action and power \(N^{-3/2}\).
For the uniform holomorphic asymptotic at nearby ordinary colors,
shrink their disks so that the real part of the original critical
action differs from \(M\) by less than \(1/400\). Equation
(13) is then an exponentially smaller relative error there too.
When \(I_m\) is empty this statement reduces to the unselected
plateau theorem.

## 4. The remaining plateau problem is at the ends

For \(m\ge11\), every selection not covered by Theorem 1 meets
\[
 \{1,2,3,4,5\}\ \cup\ \{m-4,m-3,m-2,m-1\}.
 \tag{14}
\]
There are nine such retained positions, independently of \(m\).
The asymmetry comes from having summed the last private coordinate
into the terminal factor before making the retained selections.
At smaller lengths all retained positions belong to a bounded
boundary block.

This localization does not bound a term with a selected boundary
position. Such a term can also have arbitrarily many interior
selections, and the unproved boundary cost must still be compared
with their losses. In particular the completed terminal bound at a
selected incoming height cannot be treated as a free replacement
for its complex affine tangent. The first cap also needs a bound
at its changed height. Finally, coordinates outside \(P\), the
whole outside-color estimate, and stability under arbitrary short
partial fillings remain separate requirements for the requested
finite-exception theorem.
