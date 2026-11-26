# The second selection for every mixed open chain beginning with two four-type blocks

Research theorem, 6 November 2026.

The completed central and half-row comparisons give a strict bound
for the whole two-ordinary-factor product incident to the second
selected coordinate. The first two block types are four; the third
may be three or four. This product joins the unselected cap and
arbitrary suffix with their original tangents. Arbitrary eligible interior
selections may occur simultaneously. The resulting restricted plateau
sum has the same nonzero geometric coefficient as the unselected
plateau. This is not an estimate for the entire open source.

## 1. The entire finite product at the second coordinate

Fix a positive mixed three/four word of length \(m\ge4\), with
\(\epsilon_1=\epsilon_2=1\), \(\epsilon_3=\beta\in\{0,1\}\). Let
\(r_j=a_j+ic_j\) be its original retained critical coordinates,
\(P=[.22,.45]\), and set
\[
 z_1=x_1+ic_1,\qquad z_2=x_2+i/100,\qquad
 z_3=x_3+ic_3,\qquad (x_1,x_2,x_3)\in P^3,
 \qquad X_j=e^{-2\pi iz_j}.
 \tag{1}
\]
The first and third coordinates are unselected. The reference values
\(u_*=s_2^*\), \(v_*=s_3^*\) belong to ordinary indices,
including when \(m=4\). The next external coordinate \(c=s_4^*\)
is attached at length four and ordinary at greater lengths. In either
case it belongs to one of the proved domains \(K_3,K_4\).

Use the original bare phase
\[
 Q_\epsilon(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)-g(a)-g(b)+2\pi ias
 \tag{2}
\]
and the allocated phase
\[
 \begin{split}
 F_{23}&=Q_1(u;z_1,z_2)+Q_\beta(v;z_2,z_3)
              -\tfrac12g(z_1)-g(z_2)-\tfrac\beta2g(z_3),\\
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
 p_R=g'(v_*+r_3)-(1+\beta/2)g'(r_3).
 \tag{4}
\]
The incoming halfweight is always present. The outgoing halfweight
is present exactly when \(\beta=1\); for \(\beta=0\) its exponent
is zero and \(p_R=g'(v_*+r_3)-g'(r_3)\). The asymmetric chirp
and the original allocations remain in the comparison.

The [completed central theorem](research_mixed_second_selected_central_completion.md)
bounds both main/main Fourier alternatives, with common raw gap
\(1/3200\). Its stronger type-three bound is \(1/100\).
The new [type-three half-row completion](research_mixed_second_selected_half_row_completion.md)
bounds both main/right-half-row alternatives by a raw gap \(1/20\)
when \(\beta=0\). These are bounds on the entire canonical reference
family, with all real targets free and both original boundary
tangents retained. They use the same original external domains
\(K_3,K_4\), rather than requiring the suffix to realize a particular
test reference.

When \(\beta=1\), the earlier
[outgoing-four half-row completion](research_mixed_second_selected_outgoing_four_half_row_completion.md)
already dominates the right half row by the right main profile.
For either \(\beta\), the original outgoing last-row comparison has
the separate joint gap \(1/400\).

The exact finite product to be bounded is
\[
 \mathcal B_{23,N}=
 |C_{1,N}(X_1,X_2)C_{\beta,N}(X_2,X_3)d_N(X_2)X_2^{-N}|
                 |d_N(X_1)|^{1/2}|d_N(X_3)|^{\beta/2}.
 \tag{5}
\]
The halfweights are nonnegative roots of moduli, with the outgoing
factor identically one when \(\beta=0\), including at a zero of
\(d_N\). No holomorphic square root or division by a Fourier
polynomial is used. Put
\[
 \delta_\beta=
 \begin{cases}
 1/400,&\beta=0,\\
 1/3200,&\beta=1.
 \end{cases}
 \tag{5a}
\]

**Theorem 1.** For every \(\tau>0\), uniformly on (1),
\[
 \mathcal B_{23,N}\le C_\tau N^{A_\tau}
            \exp N\{\Lambda_{23}-\delta_\beta+\tau\}.
 \tag{6}
\]
This holds for all sufficiently large integer levels of both parities
and retains every row and contour contribution of both finite kernels.
In particular \(\tau<1/6400\) gives a finite-source gap \(1/6400\)
after absorbing the polynomial prefactor into the strict spare
tolerance at sufficiently large \(N\).

*Proof.* For \(\beta=0\), Theorem 1 of the
[four-profile reduction](research_mixed_second_selected_four_profile_reduction.md)
bounds (5) by the upper rate
\(\Lambda_{23}+\max\{-1/400,D_4\}+\tau\).
The two main/main entries of \(D_4\) are smaller than \(-1/100\);
the two main/right-half-row entries are smaller than \(-1/20\).
Hence the displayed maximum is at most \(-1/400\).

For \(\beta=1\), equation (8) of the outgoing-four half-row
completion gives the rate
\(\Lambda_{23}+\max\{-1/400,D_2\}+\tau\).
Its two remaining central entries are smaller than \(-1/3200\).
This proves (6) for both flags.

The underlying finite reduction starts with
\(4\cdot4\cdot2=32\) profile terms. All three non-main profiles
of factor 2 are pointwise dominated by its main profile. For either
right type the left cut is dominated by the right main profile.
The right last-row terms have their separate joint gap \(1/400\).
For right type four its half row is dominated by its main profile;
for right type three the half-row joint defect is now separately
bounded. Thus every profile, join, alias and finite row in the
original reduction is retained. The two rates bound the additive
estimate for the complete selected Fourier polynomial; neither
alternative is deleted. \(\square\)

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
The first cap takes the other half of \(|d_N(X_1)|\).
At the right interface, the next ordinary factor, or the terminal
factor when \(m=4\), takes \(|d_N(X_3)|^{\beta/2}\).
Thus both incidences at coordinate 3 have exponent zero for
\(\beta=0\), and exponent \(1/2\) for \(\beta=1\).
In particular \(\Pi(z_3)=\mathcal P_{\epsilon_m}(z_3)
-\beta g(z_3)/2\) at \(m=4\).
Multiplication with (5) restores every integer diagonal power in (9),
even at its zeros. No boundary halfweight is inserted or counted twice.

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
 \exp N\left\{M_{\mathrm{open}}-\delta_\beta
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

The new complete product and plateau consequence cover prefixes
\(443\) and \(444\), with every fixed mixed suffix. They do not
include first type three, simultaneous selections at positions 1
and 2, other boundary selections, regions outside the plateau,
whole-source outside-color estimates or arbitrary short partial
fillings. Neither (6) nor (14) is a full open-source or new
knot-volume theorem. The previous
[\(444\)-only deduction](research_mixed_second_selected_four_plateau_completion.md)
is preserved as a separate earlier result.
