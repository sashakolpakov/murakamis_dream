# A four-leg reference test for the third selection

Research reduction and fixed diagnostic, 6 November 2026. Selection at
position 3 can be tested using two ordinary vertices and four unknown
reference legs. A nine-variable endpoint prefix is unnecessary for this
larger reference family. Existing comparisons remove every last row
and the outgoing left cut; they do not remove the incoming left and
half cuts on the enlarged ordinary incoming-height domain.

## 1. The literal two-factor comparison

Fix a positive mixed open word of length \(m\ge5\), select position
3, and leave positions 2 and 4 unselected. Write
\[
 (\epsilon_2,\epsilon_3,\epsilon_4)=(\alpha,1,\beta),\qquad
 (a,u,z,v,b)=(t_2,s_3,t_3,s_4,t_4),\quad c=s_5.
 \tag{1}
\]
All four unknown legs \(u,z,v,b\) are ordinary, including at
\(m=5\), when the right external leg \(c\) is attached. The left
external leg \(a\) is ordinary of type \(3+\alpha\). The
[window identification theorem](research_mixed_open_word_window_inheritance.md)
and [universal ordinary-window lemma](research_mixed_cyclic_critical_height_bounds.md),
Lemma 2, identify these legs with the unique original holomorphic
window root for inputs \((a,c)\). Its full four-leg Hessian satisfies
\(-\Re\mathcal W''\succ(\pi/4)I\) on the common convex product.
No particular finite suffix is inferred from an arbitrary input pair.

Use the original bare phase
\[
 Q_\epsilon(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)
                          -g(a)-g(b)+2\pi ias.
 \tag{2}
\]
The allocated reference phase and its two marginals are
\[
 \begin{split}
 F&=Q_1(u;a,z)+Q_\beta(v;z,b)
                       -\tfrac\alpha2g(a)-g(z)-\tfrac\beta2g(b),\\
 p_L&=g'(a+u)-(1+\alpha/2)g'(a)+2\pi iu,\\
 p_R&=g'(v+b)-(1+\beta/2)g'(b),\\
 \Lambda&=\Re F_*+\Re\{p_L(a-a_*)+p_R(b-b_*)\}.
 \end{split}
 \tag{3}
\]
Its three internal derivatives in \(u,z,v\) vanish. Put
\(P=[.22,.45]\), \(H=.01\), \(z=x+iH\), and keep the original
heights of both boundary arguments. The literal allocated modulus is
\[
 |C_{1,N}(X_a,X_z)C_{\beta,N}(X_z,X_b)d_N(X_z)X_z^{-N}|
             |d_N(X_a)|^{\alpha/2}|d_N(X_b)|^{\beta/2}.
 \tag{4}
\]
These halfweights are only moduli. No polynomial is divided out.
Both alternatives \(-\Re g(z)-2\pi H\) and zero are retained.

## 2. Twelve or six profiles suffice on the full ordinary domain

Write \(R_i^L,R_j^R\) for the bare main, left, half and full last-row
profiles of the two ordinary factors. Their main index intervals are
\([.125,.5]+i\Im u_*\) and
\([\ell_\beta,.5]+i\Im v_*\), with \(\ell_0=.15,\ell_1=.125\).
The real cuts have height zero. Define
\[
 \mathcal J_0=\{0,R\},\quad\mathcal J_1=\{0\},\qquad
 D_{\alpha,\beta}=
 \max_{\substack{i\in\{0,L,R\},\ j\in\mathcal J_\beta\\\nu\in\{0,1\}}}
 \{R_i^L+R_j^R-\tfrac\alpha2\Re g(a)-\tfrac\beta2\Re g(b)
                     -\nu\Re g(z)-2\pi H\nu-\Lambda\}.
 \tag{5}
\]
There are twelve terms for \(\beta=0\), six for \(\beta=1\).

**Proposition 1.** For every actual reference in (1), the complete
finite product (4) has rate at most
\[
        \Lambda+\max\{-1/400,D_{\alpha,\beta}\}+\tau
 \tag{6}
\]
up to a polynomial prefactor, for every \(\tau>0\). Both parities
and all original currents are retained.

*Proof.* The [finite-profile compiler](research_mixed_plateau_window_concave_profiles.md)
gives the original complete contour reduction on these heights.
The completed [incoming full last-row domination](research_mixed_selected_outgoing_four_last_row_domination.md)
uses the containing incoming interval \([-.108,.068]\), so it
applies to either ordinary type here and replaces its last row by
its main profile with loss \(1/50\).

The [joint outgoing last-row proof](research_mixed_second_selected_outgoing_last_rows.md)
then applies verbatim to the three remaining incoming profiles.
Its unselected baseline comes from the individual ordinary-current
planes for these same two factors, whose internal selected-coordinate
tangents cancel. Its height derivative is independent of the incoming
argument \(a\), and its only selected-reference hypothesis is
\(\Im z_*<0\). Thus all six right-last terms have gap \(1/400\).
This argument does not import a moved-height unselected plane.

The outgoing left cut is dominated on its full ordinary domain by
[the type-three comparison](research_mixed_selected_three_left_rows.md)
or [the type-four comparison](research_mixed_second_selected_outgoing_four_left_cut.md).
For \(\beta=1\), the completed
[type-four half-row comparison](research_mixed_second_selected_outgoing_four_half_row_completion.md)
also removes the outgoing half row. All these comparisons are
pointwise in their two real targets and preserve every common
allocation and affine subtraction. This proves (6). \(\square\)

The old incoming left/half-row reductions used
\(\Im a_*\in[-.078,.021]\). Ordinary inputs here instead allow
\([-.065,.068]\) for type three and \([-.102,-.001]\) for type
four. Those smaller-domain theorems cannot remove \(i=L,R\) in (5).
The existing narrow interior selected-support theorem likewise does
not cover these full incoming reference domains.

Each term in (5) is concave on its original real product by the
compiler. Any exact trial therefore gives its rigorous affine-support
upper bound. The same original \(F_*,p_L,p_R\) must be used for
all labels. The finite maximum itself need not be concave.

## 3. Exactly eight prescribed reference centers

The diagnostic uses all eight triples \((\alpha,\beta,\sigma)\in
\{0,1\}^3\), with exact external inputs
\[
 a_0=\begin{cases}.35-.01i,&\alpha=0,\\.30-.052i,&\alpha=1,\end{cases}
 \qquad
 c_0=\begin{cases}.35-.01i,&\sigma=0,\\.30-.052i,&\sigma=1.\end{cases}
 \tag{7}
\]
These are the centers of the original typed disks. The four reference
unknowns are \((u,z,v,b)\), initialized at their own typed centers.
One Newton proposal uses at most twenty steps at fifty decimal digits;
there is no alternate seed, extra input, refinement or retry.
Its output is rounded to forty decimal places. The original gradient is
\[
 \begin{pmatrix}
 g'(u+z)+g'(a_0+u)-3g'(u)+2\pi ia_0\\
 g'(u+z)+g'(z+v)-3g'(z)+2\pi iv\\
 g'(z+v)+g'(v+b)-(2+\beta)g'(v)+2\pi iz\\
 g'(v+b)+g'(b+c_0)-(2+\beta)g'(b)+2\pi ic_0
 \end{pmatrix}.
 \tag{8}
\]
The Jacobian is its symmetric tridiagonal derivative; the middle
shared entry is \(g''(z+v)+2\pi i\). Every logarithm is on the
original regular strip. No exponential equation is substituted.

The existing canonical existence theorem, independently of the
proposal, supplies a unique root \(q_*\in Q^4\), where
\(Q=[.23,.45]+i[-.12,.12]\). If the rounded proposal \(q_0\)
also lies in \(Q^4\), the accretive Hessian gives
\[
 \|q_*-q_0\|_2\le\frac4\pi\|\nabla\mathcal W(q_0)\|_2
           \le\frac8\pi\max_i|\nabla\mathcal W(q_0)_i|.
 \tag{9}
\]
The program evaluates the final maximum with Arb at 192 bits and
uses an outward rational upper radius. Every real and imaginary
coordinate receives that radius. Full typed height and real-domain
checks precede the profile evaluations; failure remains recorded.
This is a certified reference at each of eight fixed input pairs,
not a cover of the external product or a finite-word realization.

For every retained reference, one deterministic bounded numerical
optimization proposes a rational real trial for each term in (5).
The incoming cuts and any outgoing half row are exactly real.
The program records optimizer failures without retuning. It evaluates
the original phase, both marginals and all five real derivatives on
the certified reference box. The exact support formula is
\[
 f(y)^+ +\sum_i\max\{d_i^-(l_i-y_i),d_i^+(r_i-y_i)\}.
 \tag{10}
\]
Both rational endpoint products for each sign are saved. All five
target coordinates remain in their original boxes, except the
specified fixed cuts. No forced-branch restriction is imposed.

At most seventy-two target proposals and seventy-two interval support
bounds are evaluated. A positive trial lower endpoint would obstruct
uniform negativity on this enlarged canonical family; it would not
be an actual-word counterexample. Negative supports establish only
the eight prescribed center comparisons. No full-domain sign is
claimed from this diagnostic.
