# The second selection for an open chain beginning with three four-type blocks

Research theorem, 6 November 2026.

The completed central comparison and the earlier pointwise row
comparisons give a strict bound for the whole two-ordinary-factor
product incident to the second selected coordinate. When the first
three block types are four, this product joins the unselected cap and
suffix with their original tangents. Arbitrary eligible interior
selections may occur simultaneously. The resulting restricted plateau
sum has the same nonzero geometric coefficient as the unselected
plateau. This is not an estimate for the entire open source.

## 1. The entire finite product at the second coordinate

Fix a positive mixed three/four word of length \(m\ge4\), with
\(\epsilon_1=\epsilon_2=\epsilon_3=1\). Let
\(r_j=a_j+ic_j\) be its original retained critical coordinates,
\(P=[.22,.45]\), and set
\[
 z_1=x_1+ic_1,\qquad z_2=x_2+i/100,\qquad
 z_3=x_3+ic_3,\qquad (x_1,x_2,x_3)\in P^3,
 \qquad X_j=e^{-2\pi iz_j}.
 \tag{1}
\]
The first and third coordinates are unselected. Both adjacent
indices \(u=s_2^*\), \(v=s_3^*\) are ordinary indices,
including when \(m=4\). The next external coordinate \(c=s_4^*\)
is attached at length four and ordinary at greater lengths. In either
case it belongs to one of the proved domains \(K_3,K_4\).

Use the original bare phase
\[
 Q_1(s;a,b)=g(s+a)+g(s+b)-3g(s)-g(a)-g(b)+2\pi ias
 \tag{2}
\]
and the allocated phase
\[
 \begin{split}
 F_{23}&=Q_1(u;z_1,z_2)+Q_1(v;z_2,z_3)
              -\tfrac12g(z_1)-g(z_2)-\tfrac12g(z_3),\\
 M_{23}&=\Re F_{23,*},\qquad
 p_L=\partial_{z_1}F_{23,*},\quad
 p_R=\partial_{z_3}F_{23,*},\\
 \Lambda_{23}&=M_{23}+
       \Re\{p_L(z_1-r_1)+p_R(z_3-r_3)\}.
 \end{split}
 \tag{3}
\]
All stars refer to the same original word reference. The original
stationary equations eliminate the two index derivatives and the
internal \(z_2\) derivative. The retained marginals are
\[
 p_L=g'(r_1+u_*)-\tfrac32g'(r_1)+2\pi iu_*,
 \qquad
 p_R=g'(v_*+r_3)-\tfrac32g'(r_3).
 \tag{4}
\]
In particular the asymmetric chirp and both allocated halfweights
remain in the comparison.

The [completed central theorem](research_mixed_second_selected_central_completion.md)
has first flag one and both possible third flags. In the present
third-flag-one case it gives the common raw gap \(1/3200\) for
the two main/main Fourier alternatives, uniformly on the full target
product. Its boundary calculation covers all eighteen chart/flag
cases, and its response-corrected gaps on \(K_3,K_4\) are strictly
larger than \(1/3200\). The
[completed record](../repro/results/research-mixed-second-selected-external-boundary-attempt01.json)
has SHA-256
2b720b596209b1c2f86f2a40d6cc4e946b3470e3e905a609a54bfe42ffbff5d7.
It has 3,072 visited nodes, 1,431 accepted boundary leaves,
114 geometrically excluded leaves and no unresolved or pending leaves.

The exact finite product to be bounded is
\[
 \mathcal B_{23,N}=
 |C_{1,N}(X_1,X_2)C_{1,N}(X_2,X_3)d_N(X_2)X_2^{-N}|
                 |d_N(X_1)|^{1/2}|d_N(X_3)|^{1/2}.
 \tag{5}
\]
These are nonnegative square roots of moduli. No holomorphic square
root or division by a Fourier polynomial is used.

**Theorem 1.** For every \(\tau>0\), uniformly on (1),
\[
 \mathcal B_{23,N}\le C_\tau N^{A_\tau}
            \exp N\{\Lambda_{23}-1/3200+\tau\}.
 \tag{6}
\]
This holds for all sufficiently large integer levels of both parities
and retains every row and contour contribution of both finite kernels.
In particular \(\tau<1/6400\) gives a finite-source gap \(1/6400\)
after absorbing the polynomial prefactor into the strict spare
tolerance at sufficiently large \(N\).

*Proof.* Equation (8) of the
[outgoing-four half-row completion](research_mixed_second_selected_outgoing_four_half_row_completion.md)
bounds (5) by the upper rate
\(\Lambda_{23}+\max\{-1/400,D_2\}+\tau\).
Here \(D_2\) is precisely the supremum of the two original
main/main defects, with the two marginals (4).
The completed central theorem gives \(D_2<-1/3200\).
Since \(1/400>1/3200\), this proves (6).

For completeness, the underlying finite reduction starts with
\(4\cdot4\cdot2=32\) profile terms. The three non-main profiles
of factor 2 are pointwise dominated by its main profile. The right
left-cut and half-row profiles are likewise dominated by the right
main profile. The right last-row terms have the separate joint gap
\(1/400\). The two remaining central alternatives are now bounded.
Thus the implication uses the entire finite reduction, not only its
main horizontal currents. The two alternatives bound the sum coming
from the exact selected Fourier polynomial; neither is deleted.
\(\square\)

## 2. Joining the cap and the arbitrary suffix

Put
\[
 h=m-1,\qquad k_4=\sum_{j=1}^m\epsilon_j,\qquad
 I_m=\{j:6\le j\le m-5\}.
 \tag{7}
\]
Only type-four retained coordinates may be selected. For
\(T\subseteq I_m\) at such coordinates, let \(S=\{2\}\cup T\)
and use the plateau
\[
 \Im z_2=1/100,\qquad
 \Im z_j=7/500\ (j\in T),\qquad
 \Im z_j=c_j\ (j\notin S),\qquad
 \mathbf x\in P^h.
 \tag{8}
\]
The heights are constant on this plateau, so its parameter Jacobian
is one. Each exact Fourier summand permits its own contour choice in
the full torus identity. No equality between plateau integrals at
different heights is asserted.

The literal integrand is
\[
 \begin{split}
 \mathscr J_{S,N}={}&U_{1,N}(w_L,X_1)
      \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
      \mathcal V_{\epsilon_m,N}(w_R,X_h)\\
 &\hspace{8mm}\cdot\prod_{j=1}^{h}
       d_N(X_j)^{\epsilon_j}X_j^{-N\mathbf1_{j\in S}}.
 \end{split}
 \tag{9}
\]
The terminal factor already contains its whole private source and
its own Fourier alternatives. The original external scalar remains
\(\kappa_N^{m+k_4}N^{m+k_4-1}\), with \(|\kappa_N|=1\).

Let \(L,\phi_j,\Pi\) be the allocated phases of the
[whole unselected plateau](research_mixed_full_unselected_plateau.md).
At the original reference,
\[
 \mathcal F_m(z_*)=L(r_1)+F_{23,*}
             +\sum_{j=4}^{h}\phi_j(r_{j-1},r_j)+\Pi(r_h).
 \tag{10}
\]
The sum is empty at \(m=4\). The exact boundary matching equations
are
\[
 \begin{split}
 L'(r_1)+p_L&=0,\\
 p_R+\partial_1\phi_4(r_3,r_4)&=0\quad(h\ge4),\\
 p_R+\Pi'(r_3)&=0\quad(h=3).
 \end{split}
 \tag{11}
\]
The first cap takes the other half of \(|d_N(X_1)|\), and the
next ordinary factor, or the terminal factor when \(m=4\), takes
the other half of \(|d_N(X_3)|\). Multiplication with (5)
therefore restores every integer diagonal power in (9), even at its
zeros. No boundary halfweight is charged twice.

The factors incident to the additional selections are
\[
 E(T)=\{j\in\{4,\ldots,h\}:j-1\in T\ \text{or}\ j\in T\}.
 \tag{12}
\]
Their indices are at least six, so they are disjoint from factors
2 and 3. The
[interior-selection theorem](research_mixed_interior_selected_plateau.md)
supplies their whole finite-factor bounds with loss \(1/200\)
and the original complex affine tangents. All other factors use their
completed unselected planes. The endpoint real coordinates remain
free on \(P\); they are not fixed to their critical values.

**Theorem 2.** For every fixed word above and every \(\tau>0\),
uniformly on (8),
\[
 |\mathscr J_{\{2\}\cup T,N}|
 \le C_{m,\tau}N^{A_{m,\tau}}
 \exp N\left\{M_{\mathrm{open}}-\frac1{3200}
                    -\frac{|E(T)|}{200}+\tau\right\},
 \qquad M_{\mathrm{open}}=\Re\mathcal F_m(z_*).
 \tag{13}
\]
The assertion holds at both level parities, on sufficiently small
fixed ordinary-color disks, and for every fixed ordinary-color
derivative on smaller disks, with its own polynomial prefactor.

*Proof.* Multiply (6) by the complete cap, suffix and terminal
bounds with the allocation just specified. Equations (10)--(11)
cancel the two boundary tangents of the central block. Original
stationarity cancels every remaining affine term, including the
imaginary displacement terms at selected interior coordinates.
The unused quadratic remainders are nonpositive. For the fixed word,
choose all source and color tolerances with total at most \(\tau\).
Only the two endpoint factors depend on the ordinary colors; their
completed estimates hold on fixed disks with these tolerances.
Cauchy's formula on smaller disks is applied to the original
holomorphic integer-weighted source; no modulus halfweight is
differentiated. This gives the derivative assertion and proves (13).
\(\square\)

## 3. The restricted plateau sum retains its nonzero coefficient

Allow all type-compatible sets \(S\subseteq\{2\}\cup I_m\).
For sets containing 2 use (8); for sets not containing 2 use the
interior-selection contours. Let \(\mathcal Z_N^{\mathrm{second+int}}\)
be the sum of these plateau integrals, including the empty set,
multiplied by the exact scalar in Section 2.

For \(2\in S\), choose \(\tau<1/6400\) in (13).
For nonempty \(S\subseteq I_m\), the earlier interior theorem
gives the larger finite gap \(1/200\). There are only finitely
many sets for each fixed word, and the scalar is polynomial in
modulus. Hence all nonempty permitted selections are exponentially
smaller than the unselected plateau. Its completed asymptotic yields
\[
 \mathcal Z_N^{\mathrm{second+int}}(-2,-2)
   =\kappa_N^{m+k_4}N^{-3/2}A_m
          e^{N\mathcal F_m(z_*)}(1+O(N^{-1})),\qquad A_m\ne0.
 \tag{14}
\]
The original action, orientation, coefficient and power of \(N\)
are unchanged. The same local ordinary-color packet and every fixed
ordinary jet survive: shrink the color disks so the original critical
action varies by less than the strict gap, then compare the errors
uniformly and apply Cauchy's formula. The leading jet multipliers
are precisely those in the unselected plateau theorem.

The rate loss in (13) is independent of the word length. Its
constants, color disks and sufficiently-large-level threshold may
depend on the fixed word. One may also add the already controlled
plateau selections supported on \(\{1\}\cup I_m\), counting their
intersection only once; this still excludes every set containing
both positions 1 and 2.

The new complete product and plateau consequence require the first
three block types to be \(444\). The central comparison alone also
covers third type three, but its joint right half-row terms remain.
First type three, simultaneous selections at positions 1 and 2,
other boundary selections, regions outside the plateau, whole-source
outside-color estimates and arbitrary short partial fillings remain
separate obligations. Neither (6) nor (14) is a full open-source or
new knot-volume theorem.
