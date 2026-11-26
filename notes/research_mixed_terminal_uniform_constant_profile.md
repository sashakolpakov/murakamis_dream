# A height-sensitive reserve for the terminal constant profile

Research deduction and fixed saved-data protocol, 6 November 2026.

The terminal constant profile has a larger allocated reserve when
the original incoming reference height is closer to zero. Retaining
that height in the existing halfweight comparison suffices to pay
the present whole-\(D_4\) joined-plane ceilings. The deduction keeps
both selected Fourier alternatives, the complete original source,
and the original complex boundary marginal. It needs no new source,
primitive, reference or parameter evaluation.

## 1. Both halfweight alternatives

Let
\[
 y\in P=[11/50,9/20],\qquad c<0,\qquad H\ge0,\qquad
 G(k)=\Re g(y+ik),\qquad J(y)=G(0),
 \tag{1}
\]
with the original regular-strip primitive and logarithmic lift.
The old negative-height halfweight and the selected halfweight rates are
\[
 q_0(c)=-G(c)/2,\qquad
 q_1(H)=\max\{-G(H)/2-\pi H,\ 0\}.
 \tag{2}
\]
In particular the forced alternative in (2) is retained.

**Lemma 1.** Pointwise on (1),
\[
 q_1(H)-q_0(c)
 \le\frac{\pi(-c)(1/2-y)}2
 \le\frac{7\pi}{50}(-c)
 <\frac{11}{25}(-c).
 \tag{3}
\]

*Proof.* Put
\(A(y,k)=\arg(1-e^{2\pi k-2\pi iy})\) on the original lift.
For \(0<y<1/2\), the argument is positive, and differentiation
with respect to the positive radius shows that it increases
monotonically with that radius. At radius one its value is
\(\pi(1/2-y)\); its limiting value at infinite radius is
\(\pi(1-2y)\). Thus
\[
 0<A(y,k)\le\pi(1/2-y)\quad(k\le0),\qquad
 0<A(y,k)<\pi(1-2y)\quad(k\ge0).
 \tag{4}
\]
These are the original bounds in
[selected-height transport, equation (4)](research_mixed_terminal_selected_height_rows.md).
Since \(G'(k)=-A(y,k)\), the derivative of the factorial
alternative for \(k\ge0\) is \(A(y,k)/2-\pi<0\). Hence
that alternative is at most \(-J(y)/2\).

The original normalization \(J(1/2)=0\) gives
\[
 J(y)=-\int_y^{1/2}\log(2\sin\pi x)\,dx<0,
 \tag{5}
\]
because \(1/6<y<1/2\). Therefore the forced value zero is
also at most \(-J(y)/2\), proving \(q_1(H)\le-J(y)/2\)
for the maximum of both alternatives. Finally
\[
 G(c)-J(y)=\int_c^0 A(y,k)\,dk
             \le\pi(-c)(1/2-y).
 \tag{6}
\]
Equations (2), (5)--(6) give the first inequality in (3).
Use \(y\ge11/50\) and \(\pi<22/7\) for the remaining
two. No estimate of \(J(y)\) by numerical quadrature is used.
\(\square\)

## 2. The original bare plane and the constant label

Keep an original eligible terminal reference \(a_*=A+ic\),
the terminal action \(P_\epsilon\), and its bare horizontal plane
\[
 B_0(y)=\Re P_\epsilon(a_*)
          +\Re P_\epsilon'(a_*)(y-A)-\kappa(y-A)^2,
 \qquad \kappa=1/2500000.
 \tag{7}
\]
The original type-four-input source theorem proves
\(B_0(y)>99/100\), for both terminal types; see
[the end-index argument, Section 2](research_mixed_terminal_three_selected_height_completion.md).
The allocated plane is
\[
 B_T(y)=\Re(P_\epsilon-g/2)(a_*)
       +\Re(P_\epsilon'-g'/2)(a_*)(y-A)-\kappa(y-A)^2.
 \tag{8}
\]
Horizontal convexity of \(\Re g(y+ic)\) gives
\(B_0(y)+q_0(c)\le B_T(y)\).
The complete terminal alphabet has the constant profile
\(C=879/1000\), on its full incoming tube, by
[the finite-source envelope](research_mixed_terminal_concave_profile_envelope.md).
Combining these facts with Lemma 1 yields
\[
 C+q_1(H)
 <B_T(y)-\rho(c),\qquad
 \rho(c)=\frac{111}{1000}-\frac{11}{25}(-c).
 \tag{9}
\]
This bounds the whole coherent end sectors and the positive exterior
majorants represented by that constant label. It does not split a
coherent source row and then apply its whole-row bound to a sub-sum.

If a canonical family has \(c\ge c_{\min}<0\), the uniform
reserve supplied by (9) is
\[
 \rho_{\min}=\frac{111}{1000}+\frac{11}{25}c_{\min}.
 \tag{10}
\]
For illustration, the prescribed coarse negative-height floors give
the following exact rational arithmetic:
\[
 \begin{array}{c|c}
 c_{\min}&\rho_{\min}\\ \hline
 -531/10000&21909/250000=.087636\\
 -60711/1000000&2107179/25000000=.08428716.
 \end{array}
 \tag{11}
\]
The fixed checker below verifies these floors against the saved
whole-image endpoints, and also retains the sharper endpoint-specific
values (10).

## 3. Join at the same original marginal and height

Now take external flag \(\beta=1\), terminal flag
\(\epsilon=0,1\), and the original canonical families on \(D_4\).
For the finite source restrict the external parameter to \(K_4\).
The [source-domain lemma](research_mixed_terminal_canonical_source_domain.md)
supplies the original source hypotheses throughout this reduced domain;
it does not assert them for independent points of a containing rectangle.

Set \(H=1/100\). Let \(E_{\epsilon,\nu}^+\) be the completed
uniform joined-plane upper for complete-weight alternative \(\nu\),
with the original reference action and incoming affine marginal, from
[the uniform joined-plane calculation](research_mixed_terminal_uniform_joined_plane.md).
Its two selected halves are allocated exactly as in
[the reserved-plane theorem](research_mixed_terminal_reserved_plane_transfer.md).
Equation (9) therefore gives, for the constant-profile joint defect,
\[
 \sup D_{\epsilon,\nu,C}
 <E_{\epsilon,\nu}^+-\frac{111}{1000}
                    -\frac{11}{25}c_{\epsilon,\min},
 \qquad \nu=0,1.
 \tag{12}
\]
Both alternatives retain all independent incoming real targets in
\(P\); the incoming modulus halfweight and full
\(d_N(X_a)X_a^{-N}\) remain in the literal product.

The prescribed coarse ceilings are
\[
 E_{0,\nu}^+<617/10000,\qquad
 E_{1,\nu}^+<709/10000.
 \tag{13}
\]
Together with (11), they give deficits greater than
\(6484/250000\) and \(334679/25000000\), respectively,
both larger than \(1/100\). The new saved-only checker must verify
(11), (13), and the four sharper comparisons (12) from the exact
saved fractions before this numerical corollary is recorded as complete.

After those checks, the constant label has common raw joint gap
\(1/100\) and, with the inherited small ordinary-color tolerance,
polynomial prefactors, fixed jets and both level parities, finite gap
\(1/200\) for sufficiently large levels. This is a constant-profile
comparison. It does not by itself control the other 26 terminal
labels, a complete terminal kernel, or a whole-word invariant.

## 4. Fixed saved-only verification

The checker
[check_mixed_terminal_uniform_constant_profile.py](../experiments/check_mixed_terminal_uniform_constant_profile.py)
binds this note, the source-domain and halfweight proofs, the frozen
quadratic-residual result with SHA256
2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331,
and the completed joined-plane result with SHA256
4bfa03e1c61a4e34d9b6d549b5e9d666b15df606078d02258dae340055e3ee88.
It verifies every inherited input hash before and after.

For the two \(\beta=1\) cases it matches the exact saved refinement
case hash used by the plane record, reads the unchanged whole-image
height endpoint, and recombines each plane ceiling from its saved
vertex totals. It verifies the predeclared coarse guards and the
four exact inequalities (12) at gap \(1/100\), saving every
operand and the resulting deficit. No old gain, analytic function,
root, source, parameter or target optimizer is evaluated.

The sole prospective output is
repro/results/research-mixed-terminal-uniform-constant-profile.json.
The checker is unrun when this protocol is frozen. No modification
of the separate alias-extraction protocol is made.
