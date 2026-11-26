# The first Fourier selection in an arbitrary mixed open chain

Research theorem, 6 November 2026.

For every fixed chain of the two treated block types, with at least
three blocks, the first retained Fourier selection is exponentially
smaller than the geometric contribution on the entire plateau.
Selections sufficiently far from the two ends may occur at the same
time. The result follows from the two completed boundary-product
estimates and the original stationary equations. It places no bound
on the length of the chain.

The theorem still concerns specified regions of the source integral.
Other boundary selections and the regions outside the plateau are
not included.

## 1. The exact source and the permitted contours

Fix \(n_j=3+\epsilon_j\), \(1\le j\le m\), with \(m\ge3\) and
\(\epsilon_j\in\{0,1\}\). Put
\[
 h=m-1,\qquad k_4=\sum_{j=1}^m\epsilon_j,\qquad
 P=[.22,.45],\qquad I_m=\{j:6\le j\le m-5\}.
 \tag{1}
\]
Let \(r_j=a_j+ic_j\), \(1\le j\le h\), be the original retained
critical coordinates, and let
\(M_{\mathrm{open}}=\Re\mathcal F_m(z_*)\) be the calibrated
reference action.

The exact Fourier summand for
\(S\subseteq\{j\le h:\epsilon_j=1\}\) is
\[
 \begin{split}
 \mathscr J_{S,N}={}&U_{\epsilon_1,N}(w_L,X_1)
       \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
       \mathcal V_{\epsilon_m,N}(w_R,X_h)\\
 &\hspace{8mm}\cdot
       \prod_{j=1}^{h}d_N(X_j)^{\epsilon_j}
                              X_j^{-N\mathbf1_{j\in S}},
       \qquad X_j=e^{-2\pi iz_j}.
 \end{split}
 \tag{2}
\]
These are the complete finite kernels of
[the unselected plateau theorem](research_mixed_full_unselected_plateau.md).
The terminal factor already sums its own private indices and Fourier
alternatives.

We permit
\[
                  S\subseteq\{1\}\cup I_m
                  \quad\text{at type-four positions only}.
 \tag{3}
\]
If \(1\in S\), set \(T=S\setminus\{1\}\) and use the plateau
with real coordinates \(\mathbf x\in P^h\) and heights
\[
 \begin{split}
 \Im z_1&=H_1,\qquad
 H_1=
 \begin{cases}
 7/625,&\epsilon_2=0,\\
 1/100,&\epsilon_2=1,
 \end{cases}\\
 \Im z_j&=
 \begin{cases}
 7/500,&j\in T,\\
 c_j,&j\notin T,
 \end{cases}
 \qquad 2\le j\le h .
 \end{split}
 \tag{4}
\]
In particular \(z_2\) is unselected. For \(1\notin S\), use
the contours of
[the interior-selection theorem](research_mixed_interior_selected_plateau.md):
selected coordinates have height \(7/500\), and other coordinates
have their reference heights. All these plateau parametrizations
have constant heights and Jacobian one.

Each exact Laurent-polynomial Fourier summand permits its own
contour choice in the full torus formula. We do not identify
individual plateau integrals at different heights. The complements
of the regions just defined remain part of the full source and
still require estimates.

## 2. The two completed boundary estimates

Suppose \(1\in S\), so \(\epsilon_1=1\). Write \(\eta=\epsilon_2\).
The modulus assigned to the first two factors is
\[
 \mathcal B_{12,N}
   =\left|U_{1,N}(w_L,X_1)C_{\eta,N}(X_1,X_2)
                      d_N(X_1)X_1^{-N}\right|
                        |d_N(X_2)|^{\eta/2}.
 \tag{5}
\]
For \(\eta=0\), the
[next-three theorem](research_mixed_selected_four_three_full_product.md)
bounds (5); for \(\eta=1\), use the
[next-four theorem](research_mixed_selected_four_four_full_product.md).
Both give, for every positive tolerance,
\[
 \mathcal B_{12,N}
 \le C N^A
 \exp N\left\{M_{12}+\Re p_\eta(x_2-a_2)-1/2000+\tau_{12}\right\}.
 \tag{6}
\]
The real targets \(x_1,x_2\) range independently over all of \(P\).
All finite summation rows, the original endpoint coefficient and
the complete selected weight are included.

For clarity, the original allocated phase and its outgoing derivative
are
\[
 \begin{split}
 \mathcal F_{12,\eta}
   &=\Psi(e,z_1)+Q_{3+\eta}(s;z_1,z_2)
                         -g(z_1)-\tfrac{\eta}{2}g(z_2),\\
 Q_{3+\eta}(s;z,b)
   &=g(s+z)+g(s+b)-(2+\eta)g(s)-g(z)-g(b)+2\pi izs,\\
 M_{12}&=\Re\mathcal F_{12,\eta}(e_*,s_*;r_1,r_2),\\
 p_\eta&=g'(s_*+r_2)-(1+\eta/2)g'(r_2).
 \end{split}
 \tag{7}
\]
The original critical equations make the reduced \(z_1\) derivative
zero. Hence (6) is the original affine tangent for this whole prefix,
minus its strict gap. The only remaining derivative is \(p_\eta\)
at the unselected coordinate \(z_2\).

For \(\eta=1\), the suffix receives the other factor
\(|d_N(X_2)|^{1/2}\). Multiplying the prefix and suffix estimates
restores the modulus of the integer power \(d_N(X_2)\) in (2).
No holomorphic square root of that finite polynomial is introduced,
and no division by it is needed at a zero.

## 3. Cancellation of boundary derivatives and the chain estimate

Use the allocated ordinary phases \(\phi_j\) and terminal phase
\(\Pi\) of the unselected theorem. They satisfy the exact action
identity
\[
 \mathcal F_m(z_*)=
 \mathcal F_{12,\eta}(e_*,s_*;r_1,r_2)
       +\sum_{j=3}^{h}\phi_j(r_{j-1},r_j)+\Pi(r_h).
 \tag{8}
\]
The original outgoing derivative in (7) cancels the incoming
suffix derivative:
\[
 p_\eta+\partial_1\phi_3(r_2,r_3)=0\quad(h\ge3),\qquad
 p_\eta+\Pi'(r_2)=0\quad(h=2).
 \tag{9}
\]
The second equality covers length three, when the ordinary suffix
product is empty. For \(\eta=1\), the terminal allocated phase
there is its bare phase minus \(g(z_2)/2\), as required by (5).

If \(T\subseteq I_m\) is nonempty, its incident ordinary factors are
\[
 E(T)=\{j\in\{3,\ldots,h\}:j-1\in T\ \text{or}\ j\in T\}.
 \tag{10}
\]
They have indices at least six and do not overlap the prefix (5).
The interior-selection proof supplies their complete finite-factor
bounds with loss \(1/200\) and their original complex affine
tangents. Every other suffix factor has unselected arguments and
uses the completed horizontal supporting-plane bound.
The terminal coordinate is unselected. Stationarity cancels all
internal affine terms, including imaginary displacement terms at
the selected interior coordinates.

**Theorem 1.** For every fixed word above, every permitted
\(S=\{1\}\cup T\), and every \(\tau>0\), uniformly on (4),
\[
 |\mathscr J_{\{1\}\cup T,N}|
 \le C_{\tau,m}N^{A_{\tau,m}}
 \exp N\left\{
 M_{\mathrm{open}}-\frac1{2000}-\frac{|E(T)|}{200}+\tau
 \right\}.
 \tag{11}
\]
Both level parities are included. The estimate holds on sufficiently
small fixed ordinary-color disks, with fixed ordinary-color derivatives
on smaller disks.

*Proof.* Multiply (6) by the complete suffix estimates with their
assigned weight moduli. Equations (8)--(9) add the calibrated action
values and cancel the prefix boundary derivative. The remaining
stationary equations cancel all later affine terms. Each incident
selected factor contributes the loss in (10); the other quadratic
remainders are nonpositive. For the fixed word, choose the sum of all
local tolerances at most \(\tau\). The two endpoint color estimates
are uniform on fixed neighborhoods, so Cauchy's formula supplies
the fixed derivatives. No halfweight modulus is differentiated.
\(\square\)

The detailed next-three assembly is written in
[the earlier suffix theorem](research_mixed_first_selected_three_suffix_plateau.md).
Equations (5)--(9) supply the additional weight allocation needed for
next type four. They use the same original reference, rather than a
reference from a periodic chain.

## 4. The nonzero coefficient survives the expanded set of selections

Take \(\tau<1/4000\). Equation (11) gives a gap \(1/4000\)
for every permitted selection containing the first position.
For a nonempty permitted selection not containing that position,
the interior-selection theorem gives the larger gap \(1/200\).

Let \(\mathcal Z_N^{\mathrm{first+int}}\) be the sum of the plateau
integrals for all allowed sets (3), including the empty set, multiplied
by the exact original scalar
\(\kappa_N^{m+k_4}N^{m+k_4-1}\). There are finitely many such sets
for each fixed word, and the scalar has polynomial modulus.
The unselected plateau asymptotic and the strict gaps therefore give
\[
 \mathcal Z_N^{\mathrm{first+int}}(-2,-2)
   =\kappa_N^{m+k_4}N^{-3/2}A_m
       e^{N\mathcal F_m(z_*)}(1+O(N^{-1})),
                     \qquad A_m\ne0.
 \tag{12}
\]
The action, orientation, coefficient, and power of \(N\) are unchanged.
If the first type is three, position one cannot be selected and (12)
is precisely the previous interior-selection consequence.

The gap in (11) does not shrink as the chain gets longer.
The constants, color neighborhoods and sufficiently-large-level
threshold may depend on the fixed word.

Any selection not covered here must meet
\[
 B_m=\{1,\ldots,m-1\}\setminus(\{1\}\cup I_m).
 \tag{13}
\]
For \(m\ge11\), this is
\(\{2,3,4,5\}\cup\{m-4,m-3,m-2,m-1\}\), containing eight positions.
For \(3\le m\le10\), it has \(m-2\le8\) positions.
This localizes the remaining plateau problem but does not bound
those selections, including terms where the first and second
positions are both selected. Regions outside the plateau, length
two, the whole-source outside-color estimate, arbitrary short
partial fillings and the requested finite-exception theorem remain
separate obligations.
