# A complete concave profile envelope for either terminal source

Research deduction, 6 November 2026. The complete terminal source has
a common finite envelope on the full incoming tube
\(\mathcal A=[.22,.45]+i[-.12,.12]\). There are 25 regular
two-index profiles, one real entropy profile, and one constant profile.
Each profile is horizontally concave and vertically convex in the
incoming coordinate. This extends the
[ordinary window compiler](research_mixed_plateau_window_concave_profiles.md)
to the original terminal source. It supplies no new comparison sign.
No source calculation or numerical certificate is run here.

## 1. The literal source and its two regular phases

Put \(r=e^{-2\pi i/N}\), \(q=e^{\pi i/N}\),
\(P_i=(r;r)_i\), \(p_i(X)=(rX;r)_i\), and
\(X=e^{-2\pi ia}\). For terminal type \(3+\epsilon\), the
[exact reversed-cap identity](research_mixed_reversed_cap_assembly.md)
is
\[
 \mathcal V_{\epsilon,N}(w,X)=
 \sum_{i=0}^{N-1}\frac{X^{-i}p_i(X)}{P_i^{1+\epsilon}}
                  \mathcal U_{\epsilon,N}(w,r^i).
 \tag{1}
\]
This includes the terminal diagonal and its entire Fourier polynomial.
It is not a cap with its arguments transposed. The adjacent retained
weight has not been inserted into (1).

Keep the original primitives \(J\),
\(g(z)=J(z)+i\pi(z-z^2)/2\), with
\(J'(x)=\log(2\sin\pi x)\) and \(J(0)=0\) on the real
strip, and their prescribed holomorphic continuations. The regular
phases, at complete ordinary color, are
\[
\begin{split}
 \Phi_0(a;t,u)={}&-2J(1/2-u)-2J(u)+g(t+a)+g(t+u)\\
 &-3g(t)-2g(u)-g(a)+i\pi u+2\pi iat,\\
 \Phi_1(a;t,e)={}&S(e)+g(t+a)+g(t+e)-3g(t)-g(e)-g(a)\\
 &-i\pi(e-e^2)/2+2\pi iat.
\end{split}
 \tag{2}
\]
Here \(S(e)\) is the original complete endpoint action, including
its auxiliary stationary branch. The
[type-three interpolation](research_mixed_terminal_three_joint_zero_mode.md)
retains the literal Newton factor \(N\), the lift of
\((-q)^{-l}\), and the support \(i+l<N\). The
[type-four interpolation](research_mixed_terminal_four_reduced_currents.md),
equations (1)--(8), retains the **whole** endpoint coefficient
\(\mathcal C_N(e,w)\) before either remaining contour is moved.
Off-grid Newton terms revived by that motion remain in the source.

Use the products
\[
\begin{array}{c|c|c}
 &t&\text{second index }v\\ \hline
 \epsilon=0&[.15,.50]+i[-.12,.12]&u\in[.10,.40]+i[-.12,.12]\\
 \epsilon=1&[.15,.50]+i[-.12,.12]&e\in[.27,.49]+i[-.055,.04].
\end{array}
 \tag{3}
\]
All summed arguments in (2) are regular on a fixed neighborhood of
\(\mathcal A\) times these products. The enlarged type-three
Hessian theorem, equation (10a), and the type-four reduced-current
Lemma 1 prove
\[
                  -\Re\Phi_\epsilon''\succ(\pi/100)I_3.
 \tag{4}
\]
This includes the incoming variable \(a\). For type four the bound
is the accretive Schur pullback through the original auxiliary branch,
not a separate independently enlarged auxiliary rectangle.

## 2. Five states per residue index

For an index rectangle \([L,R]+i[h_-,h_+]\) in (3), choose
any fixed main height \(h_*\in[h_-,h_+]\). Its five states are
\[
\begin{array}{c|c|c}
 \text{state}&\text{coordinate}&\text{penalty}\\ \hline
 0&x+ih_*,\quad L\le x\le R&0\\
 L&L&0\\ R&R&0\\
 -&x+ih_-,\quad L\le x\le R&2\pi|h_-|\\
 +&x+ih_+,\quad L\le x\le R&2\pi h_+ .
\end{array}
 \tag{5}
\]
Actual reference heights are the intended main-height choice; the
source reduction itself does not require stationarity. At a cut the
index is real, with no remaining free real coordinate.

For each of the 25 pairs \(\sigma=(\sigma_t,\sigma_v)\), set
\[
 F_{\epsilon,\sigma}(a;x_t,x_v)=
 \Re\Phi_\epsilon(a;t_{\sigma_t},v_{\sigma_v})
       -\operatorname{pen}(\sigma_t)-\operatorname{pen}(\sigma_v).
 \tag{6}
\]
Unused variables at cuts are omitted. By (4) each function is
strictly concave in its free real coordinates, including \(\Re a\).
Its dependence on any one free height is convex. Constants subtracted
in (6) do not change these properties.

**Lemma 1.** These 25 profiles bound the complete regular double
rectangle, including every zero-mode join and every residue alias.

*Proof.* At the inward half-grid cuts the exact one-index summation
functional is \(N(I+A)\), with
\(K_N(z)=(1-e^{-2\pi iNz})^{-1}\). The lower alias contour
carries \(K_N-1\), the upper carries \(K_N\). Thus the
two-index source is exactly \(N^2(I_t+A_t)(I_v+A_v)\) applied
to its original holomorphic interpolant. This is
[the original double-cycle identity](research_mixed_terminal_three_alias_reduction.md),
equations (5)--(8); it also holds for the asymmetric type-four rectangle.

Deform every unaliased interval to its main height and its two vertical
joins, also when the other coordinate lies on an alias. This is valid
on the full product (3); the other residue kernel is independent of
the coordinate being deformed. On an ordinary join, vertical convexity
reduces the phase to its endpoints: a real cut or an endpoint of the
main segment. On a half-grid alias side,
\[
 |K_N(c_N+ih)|\le e^{-2\pi Nh}\ (h\ge0),\qquad
 |K_N(c_N+ih)-1|\le e^{-2\pi N|h|}\ (h\le0).
 \tag{7}
\]
The kernel is bounded at zero height. On each sign half the penalty
is linear, so convexity reduces that side to its real cut and its
outer horizontal alias. Applying this in both coordinates gives
exactly restrictions of (6). In particular, an unaliased coordinate
at height zero and with a free real part is deformed; it is not
silently replaced by a free zero-height whole rectangle. All side
orientations are retained in the identity before taking absolute values.

There are finitely many currents. Their lengths and kernels contribute
only polynomial factors. Half-grid displacements change regular rates
by \(O(N^{-1})\). The fixed ordinary-color germ and every fixed jet
are controlled on smaller neighborhoods with an arbitrary prescribed
positive exponential tolerance. This proves the lemma. \(\square\)

## 3. The physical complement and the two additional profiles

The complete physical source is reduced to these same anchors before
any comparison with a reference action. The following source inputs
are uniform for every \(a\in\mathcal A\), not only at its
actual reference height.

* Remove the whole coherent transform end rows first. Lemma 2 of
  [the terminal tail theorem](research_mixed_terminal_transform_tails.md)
  gives raw rate \(217/250\) for both terminal types. It bounds the
  positive outer-row majorant with the **entire** cap in each row;
  it is never restricted to a subsequent private-index sub-sum.
* For type three, remove the positive
  [low Newton](research_mixed_terminal_three_low_newton.md),
  [high Newton](research_mixed_terminal_three_high_newton.md), and
  [near-half Newton](research_mixed_terminal_three_newton_exterior_strips.md)
  majorants, all with raw rate \(879/1000\). Positive restriction
  to the remaining outer rows is legitimate. The remaining
  [left strip](research_mixed_terminal_three_left_strip.md) transports
  \(t\) to \(.15\). The exterior-strip Lemma 1 transports
  \(u\) to \(.1\) or \(.4\); its Proposition 4 transports the
  left real corners to the same anchors. Their derivative inequalities
  hold throughout the other index's contour rectangle. Therefore
  Lemma 1 applies to the resulting anchor and any surviving residue.
* For type four, the
  [private-tail theorem](research_mixed_terminal_four_private_tails.md)
  transports the entire private physical complements to real
  \(e=.27,.49\), retaining the complete ordinary polynomial.
  The [left-strip theorem](research_mixed_terminal_four_left_strip.md)
  transports the remaining left rows and corner sectors to real
  \(t=.15\). These estimates again hold on the entire other-index
  contour rectangle, with unchanged incoming target and alias penalty.

These are rate transport statements preceding the old supporting-plane
comparisons; no old calibrated sign is being imported at a new incoming
height. The exhaustive partitions are
[type-three rectangle completion, Section 2](research_mixed_terminal_three_rectangle_completion.md)
and [type-four full completion, Section 1](research_mixed_terminal_four_full_completion.md).
The strip of width \(O(N^{-1})\) at the inward upper transform cut,
including the even-level half row, is covered by its real \(t=.5\)
anchor: use the one-index residue in the other central index and its
real-cut transports, as in the type-three upper-cut-column Lemma 2.
This gives states \((R,\sigma_v)\) in (6) with \(O(N^{-1})\)
rate error. No even row is omitted.

It remains to cover the physical right triangle. Put \(L=-J\)
on \([0,.5]\), with its continuous endpoint values, and define
\[
\begin{split}
 Q(a)&=\Re\{g(a+1/2)-g(a)+\pi ia\},\\
 E_0(u)&=3L(1/2-u)+4L(u),\qquad 0\le u\le1/2,\\
 E_1(e,u)&=2L(1/2-u)+3L(u)+L(e-u)\\
 &\hspace{17mm}+L(1/2-e)+L(e),\qquad0\le u\le e\le1/2,\\
 R_\epsilon(a;\mathbf y)&=Q(a)+E_\epsilon(\mathbf y),
 \qquad C(a)=879/1000.
\end{split}
 \tag{8}
\]
The [type-three](research_mixed_terminal_three_right_triangle.md)
and [type-four](research_mixed_terminal_four_right_triangle.md)
right-triangle theorems give, for every supported row with \(t\ge.5\),
\[
 \text{raw row rate}\ \le
 \max_{\mathbf y}R_\epsilon(a;\mathbf y)
            -\log(80/63)(t-.5).
 \tag{9}
\]
This is a positive-majorant statement even at zeros and the support
wall. It uses no continuation of \(g(a+t)\) through a divisor.
At the half face in (8) all external arguments are regular, and the
identity for \(Q\) retains the original chirp. Also
\(J(.5)=0\), so there is no omitted real constant in (8).

Both entropy functions are concave on their convex closed domains.
In the interiors,
\[
\begin{split}
 -E_0''/\pi&=3\tan\pi u+4\cot\pi u>0,\\
 -d^2E_1/\pi&=(2\tan\pi u+3\cot\pi u)du^2
 +\cot\pi(e-u)(de-du)^2\\
 &\quad+(\tan\pi e+\cot\pi e)de^2>0.
\end{split}
 \tag{10}
\]
Continuity extends concavity to the endpoints. Moreover
\(Q_{\Re a\Re a}=\pi\Re\{\cot\pi(a+.5)-\cot\pi a\}<0\)
on \(\mathcal A\). Thus \(R_\epsilon\) is jointly concave in
the incoming real target and its entropy variables, and convex in the
incoming height. The constant profile has both properties as well.

## 4. Complete finite-source envelope and assembly rule

Let
\[
 \mathcal E_\epsilon(a)=\max\left\{
 C(a),\ \max_{\mathbf y}R_\epsilon(a;\mathbf y),\
 \max_{\sigma\in\{0,L,R,-,+\}^2}\ \max_{\mathbf x}
                  F_{\epsilon,\sigma}(a;\mathbf x)\right\}.
 \tag{11}
\]
**Theorem 2.** For every \(\tau>0\), there is a fixed sufficiently
small ordinary-color disk about \(-2\) such that the complete original
terminal source satisfies
\[
 |\mathcal V_{\epsilon,N}(w,e^{-2\pi ia})|
       \le C_\tau N^{A_\tau}
                    e^{N\{\mathcal E_\epsilon(a)+\tau\}}
       \qquad(a\in\mathcal A).
 \tag{12}
\]
The same conclusion holds for every prescribed fixed number of color
and incoming-coordinate derivatives, with enlarged polynomial factors
and the same arbitrary tolerance. It includes both level parities,
all physical support zeros, the entire terminal ordinary polynomial,
and all terminal Fourier alternatives. The proof is Lemma 1, the
exhaustive transports above, and (9). The small complex neighborhoods
needed for Cauchy estimates are supplied by the original regular
interpolants and zero-safe finite-product bounds; no modulus profile
is itself differentiated as a holomorphic function.

This is a maximum over **27 labeled profiles**, not an assertion of
concavity of their maximum in \(\Re a\). Each individual profile
has a valid affine tangent upper bound at any legal interior trial.
For the entropy profile, maximize that affine function on its interval
or triangle (the latter has vertices \((0,0),(.5,0),(.5,.5)\)).
The regular profiles use their rectangular free-index domains.

Consequently a terminal factor can be joined to any ordinary plateau
window from the compiler by adding one of these 27 profiles, retaining
the original reference value and complex affine marginal at the join.
Allocate each retained diagonal exactly once, or in matching halves.
Choose a Fourier alternative from each **complete** selected weight
before splitting its rate between adjacent factors. A term
\(-c\Re g(a)\), \(c\ge0\), and the corresponding affine
height penalty preserve horizontal concavity. Thus the same exact
tangent-support method applies to each combined labeled profile.
No Fourier weight is divided out.

For fixed main heights the envelope (11) is convex in incoming height:
each profile has this property, and suprema preserve it. This is a
common envelope on the whole tube \(\mathcal A\), suitable for
height-corner or convex-height contour arguments. Choosing the minimum
of envelopes obtained from different main heights does not retain
this property automatically.

Neither (12) nor concavity proves that a combined profile lies below
the actual open-word action. In particular the positive imaginary
terminal marginal in
[the terminal height sign theorem](research_mixed_terminal_height_tangent_sign.md)
remains part of the complex affine comparison and must be paid jointly.
The remaining task is a calibrated joint comparison for this finite
alphabet, followed by the original outer-cycle assembly. No reversed
chart identification, terminal nonzero coefficient, or whole-invariant
asymptotic is deduced here.

## 5. The last selected leg: one concrete joint comparison

For a word of length \(m\ge3\), suppose \(n_{m-1}=4\).
Write \(\beta=n_{m-2}-3\), \(\epsilon=n_m-3\),
\(b=z_{m-2}\), \(a=z_{m-1}\). Keep \(b\) at its original
unselected height and place the selected \(a\) at height
\(H\in[0,.014]\). The literal allocated modulus is
\[
 \mathcal K_N=
 |C_{1,N}(X_b,X_a)\mathcal V_{\epsilon,N}(w,X_a)
                     d_N(X_a)X_a^{-N}|
                      |d_N(X_b)|^{\beta/2}.
 \tag{13}
\]
No incoming square root is inserted into the holomorphic source.
The actual incoming height has modulus less than \(.108\), so the
ordinary seven-label theorem applies.

Let \(T_{\epsilon,\sigma}(a;\mathbf x)\) denote any of the
27 terminal profiles, including its indicated real maximization
variables and penalties. With an ordinary label \(\rho\) and
\(\nu\in\{0,1\}\), define
\[
 f_{\rho,\sigma,\nu}=
 \Re Q_1^\rho(s;b,a)+T_{\epsilon,\sigma}(a;\mathbf x)
 -\frac\beta2\Re g(b)-\nu\Re g(a)-2\pi\nu H.
 \tag{14}
\]
All 378 labeled functions are horizontally concave. Equations
(12)--(14), the ordinary compiler and the complete selected Fourier
bound give
\[
 \mathcal K_N\le CN^A
 \exp N\left\{\max_{\rho,\sigma,\nu}\max_{\rm active\ indices}
                       f_{\rho,\sigma,\nu}+\tau\right\}.
 \tag{15}
\]
The retained real variables \(\Re b,\Re a\) remain independent
in \(P\); the maximum in (15) is only over internal active indices.
For \(H\le.01\) the forced alternative \(\nu=0\) need only
be considered at \(\Re a\ge.4\), and for \(H\le.014\) at
\(\Re a\ge.36\), by the exact
[selected-weight branch-domain lemma](research_mixed_selected_weight_branch_domains.md).
The factorial alternative retains all of \(P\); this is a bound
for the additive complete weight, not a deletion of source summands.

The correct reference action and the one remaining marginal are
\[
\begin{split}
 M_*&=Q_1(s_*;b_*,a_*)+P_\epsilon(a_*)
                         -g(a_*)-\tfrac\beta2g(b_*),\\
 p_*&=g'(b_*+s_*)-(1+\beta/2)g'(b_*)+2\pi i s_*.
\end{split}
 \tag{16}
\]
Here \(P_\epsilon\) is the original stationary terminal action
in the [terminal source theorem](research_mixed_terminal_transform_tails.md),
and all starred coordinates are the actual coupled open-word reference.
Its full internal terminal derivatives vanish. The ordinary index
equation gives \(Q_{1,s}=0\), and the shared retained-leg equation is
\[
 Q_{1,a}(s_*;b_*,a_*)+P_\epsilon'(a_*)-g'(a_*)=0.
 \tag{17}
\]
Thus subtracting \(\Re\{M_*+p_*(b-b_*)\}\) from every profile
in (14) is the exact joint affine comparison. It has no unpaired
terminal marginal in \(a\). The change of height of \(a\) is
still present in the target phases; (17) does not assert its cost is
zero. This supplies a concrete finite, concave comparison problem
for the last retained selection without reversing the source chart.
Its uniform negative signs and the outer-cycle comparison remain
unproved.
