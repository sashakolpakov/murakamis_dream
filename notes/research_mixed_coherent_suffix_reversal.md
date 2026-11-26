# Coherent contraction and reversal of an arbitrary mixed suffix

Research deduction, 7 November 2026.

A suffix can be contracted before taking absolute values, including
every retained Fourier alternative inside it. The result belongs to
the same exact finite boundary-function space, and is a generalized
cap for the reversed suffix followed by one explicit terminal
transform. This identity avoids estimating a selected retained
sector separately. It does not by itself bound the new coherent
coefficient or establish its nonzero leading term.

The example \((4,3,3+\epsilon)\) contains the four unresolved
comparisons of the
[penultimate-four/following-three reduction](research_mixed_penultimate_four_followed_by_three_reduction.md).
Here those comparisons are replaced by a whole boundary-source
problem, with their cancellation retained. No source evaluation,
new critical-point calculation or numerical assertion is used.

## 1. Original finite functions and the shared-node identity

Use the original conventions
\[
 \zeta=e^{-2\pi i/N},\qquad P_j=(\zeta;\zeta)_j,\qquad
 p_j(X)=(\zeta X;\zeta)_j,\qquad
 C_{\alpha,N}(X,Y)=
 \sum_{j=0}^{N-1}\frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\alpha}}.
 \tag{1}
\]
All \(P_j\), \(j<N\), are nonzero. Let
\[
 W_{\alpha,N}(X)=
 \{d_N(X)(1+X^{-N})\}^{\alpha},\qquad \alpha\in\{0,1\},
 \tag{2}
\]
with the literal degree-less-than-\(N\) interpolant
\(d_N(\zeta^k)=P_k^{-1}\). The original whole ordinary-color
boundary polynomial is \(\mathcal H_N(w,Y)\).
These are the functions of
[conditional torus composition](research_mixed_conditional_torus_composition.md),
including its finite forcing and both level parities.

For all \(i,j<N\),
\[
 \sum_{k=0}^{N-1}
 \frac{\zeta^{-jk}p_i(\zeta^k)p_j(\zeta^k)}{P_k^\alpha}
       =P_iP_j C_{\alpha,N}(\zeta^j,\zeta^i).
 \tag{3}
\]
Indeed \(p_i(\zeta^k)=P_{i+k}/P_k\) on \(i+k<N\);
it is zero otherwise. On the common surviving support the
summands on both sides are
\(\zeta^{-jk}P_{i+k}P_{j+k}/P_k^{2+\alpha}\).
The zeros outside that support agree. This is a finite identity;
neither the phase of \(P_k\) nor the original chirp is removed.

## 2. An exact reversal intertwiner

For a polynomial \(f\) of degree less than \(N\), and a Laurent
polynomial \(h\) of band \([-N+1,0]\), retain the normalized
literal transfers from
[the exact message-space theorem](research_mixed_literal_transfer_norm_obstruction.md):
\[
 \begin{split}
 (\mathsf T_{\alpha\beta}f)(Y)
   &=\sum_{k<N}\frac{f(\zeta^k)}{P_k^\alpha}
                           C_{\beta,N}(\zeta^k,Y)
     =N\operatorname{CT}_X[f(X)W_{\alpha,N}(X)C_{\beta,N}(X,Y)],\\
 (\mathsf S_\alpha h)(X)
   &=\sum_{k<N}C_{\alpha,N}(X,\zeta^k)
                           \frac{h(\zeta^k)}{P_k^\alpha}
     =N\operatorname{CT}_Y[C_{\alpha,N}(X,Y)W_{\alpha,N}(Y)h(Y)].
 \end{split}
 \tag{4}
\]
The first output again has degree less than \(N\), the second
again has band \([-N+1,0]\). Define the finite transform
\[
 (\mathsf L_\alpha f)(X)
    =\sum_{j<N}\frac{X^{-j}p_j(X)}{P_j^{1+\alpha}}
                                      f(\zeta^j).
 \tag{5}
\]
It has the same negative band. For the literal first cap,
\(\mathsf L_\alpha\mathcal U_{\alpha,N}=\mathcal V_{\alpha,N}\);
this is exactly the
[original terminal contraction](research_mixed_reversed_cap_assembly.md),
not a new continuation of its physical values.

**Proposition 1.** On the full degree-less-than-\(N\) space,
\[
                  \mathsf S_\alpha\mathsf L_\beta
                    =\mathsf L_\alpha\mathsf T_{\beta\alpha}.
 \tag{6}
\]

*Proof.* Expand the left side using (1) and (5), with conditional
index \(j\), transform index \(i\), and physical node \(k\).
Its inner node sum is the left side of (3), multiplied by
\[
 \frac{X^{-j}p_j(X)f(\zeta^i)}
                         {P_j^{2+\alpha}P_i^{1+\beta}}.
\]
After (3), the result is
\[
 \sum_{j<N}\frac{X^{-j}p_j(X)}{P_j^{1+\alpha}}
          \sum_{i<N}\frac{f(\zeta^i)}{P_i^\beta}
                                   C_{\alpha,N}(\zeta^i,\zeta^j),
\]
which is the right side of (6). All sums are finite. \(\square\)

This also gives an operation-preserving generalized-cap class.
For an arbitrary coefficient vector \(v=(v_i)_{i<N}\), put
\[
 U_\alpha[v](X)=\sum_{i<N}\frac{v_i p_i(X)}{P_i^{1+\alpha}}.
\]
Then the same calculation proves
\[
 \mathsf T_{\alpha\beta}U_\alpha[v]=U_\beta[v^+],
 \qquad
 v_j^+=\sum_{i<N}\frac{C_{\alpha,N}(\zeta^j,\zeta^i)}{P_i^\alpha}v_i.
 \tag{7}
\]
The original cap has \(v_i=\mathcal H_N(w,\zeta^{-i})\).
Equation (7) keeps the entire coherent coefficient as its input.
It gives an exact finite class, not a uniform analytic estimate
for every vector in that class.

## 3. Arbitrary suffixes and the exact outside scalar

Let \(\boldsymbol\delta=(\delta_1,\ldots,\delta_\ell)\) list a
suffix from left to right. Define its whole boundary polynomial
\[
 \mathcal B_{\boldsymbol\delta,N}(w,X)=
       \mathsf S_{\delta_1}\cdots\mathsf S_{\delta_\ell}
                  [\mathcal H_N(w,X^{-1})].
 \tag{8}
\]
It has band \([-N+1,0]\) in \(X\), and degree at most \(N-1\)
in the original ordinary color \(w\). The original terminal
identity and (6) give
\[
 \mathcal B_{\boldsymbol\delta,N}
  =\mathsf L_{\delta_1}
      \mathsf T_{\delta_2\delta_1}
      \mathsf T_{\delta_3\delta_2}\cdots
      \mathsf T_{\delta_\ell\delta_{\ell-1}}
                          \mathcal U_{\delta_\ell,N}.
 \tag{9}
\]
For \(\ell=1\) the transfer product is empty and this is
\(\mathcal V_{\delta_1,N}\). Formula (9) reverses the whole
suffix, with all its source coefficients. It does not reverse
the two arguments of one conditional kernel pointwise.

In an original word of length \(m\), take \(1\le\ell\le m-1\),
put \(q=m-\ell\), and set \(\delta_j=\epsilon_{q+j}\).
If \(k_4=\sum_{j=1}^m\epsilon_j\), the literal whole source is
\[
 \begin{split}
 \mathcal Z_N={}&\kappa_N^{m+k_4}N^{m+k_4-\ell}
 \operatorname{CT}_{X_1,\ldots,X_q}
 \left[
 \mathcal U_{\epsilon_1,N}(w_L,X_1)
 \prod_{j=2}^{q}C_{\epsilon_j,N}(X_{j-1},X_j)\right.\\
 &\left.\hspace{24mm}\cdot
 \mathcal B_{\boldsymbol\delta,N}(w_R,X_q)
 \prod_{j=1}^{q}W_{\epsilon_j,N}(X_j)
 \right].
 \end{split}
 \tag{10}
\]
Every constant term is an integral on an arbitrary positive
circle radius. Each application of \(\mathsf S\) replaces one
constant-term integral by \(\mathsf S/N\), so removes exactly
one factor \(N\) from the original scalar \(N^{m+k_4}\).
This proves (10), including the case \(q=1\) with no conditional
factor left in the product.

All selected and unselected alternatives at the contracted nodes
are already inside (8). In particular replacing a physical value
of \(W_1\) by \(2/P_k\) would be wrong: its two constant-term
sectors together correspond to the single physical-node sum in
(4), not to twice that sum. No Gram kernel, absolute value, or
additional source measure has been inserted in (8)--(10).
Finite linearity proves these identities also for all original
ordinary jets, including repeated-root normals.

For the suffix \((4,3,3+\epsilon)\), formula (8) becomes
\[
 \begin{split}
 \mathcal B_{1,0,\epsilon,N}(w,X)
   &=\sum_{j_b,j_a<N}
       \frac{C_{1,N}(X,\zeta^{j_b})}{P_{j_b}}\,
       C_{0,N}(\zeta^{j_b},\zeta^{j_a})
       \mathcal V_{\epsilon,N}(w,\zeta^{j_a})\\
   &=\sum_{j_r,j_s,j_t<N}
       \frac{X^{-j_r}p_{j_r}(X)}{P_{j_r}^{2}P_{j_t}^{\epsilon}}\,
       C_{1,N}(\zeta^{j_s},\zeta^{j_r})
       C_{0,N}(\zeta^{j_t},\zeta^{j_s})
       \mathcal U_{\epsilon,N}(w,\zeta^{j_t}).
 \end{split}
 \tag{11}
\]
The two lines use different physical summation coordinates.
Equation (3), applied twice, proves their equality. In (10)
this replacement has scalar
\(\kappa_N^{m+k_4}N^{m+k_4-3}\).
It sums the selected/unselected \(b\) alternatives, the full
unselected type-three \(a\) coordinate, and every alternative
already contained in the terminal \(\mathcal V_\epsilon\).
It is not a statement about a restricted subinterval of any of
those three contracted physical coordinates.

## 4. Original action and the surviving boundary derivative

The exact identities above require no critical point. To identify
their geometric local current, now fix an actual word and its
original critical reference. Write \(c=x_0\) for the retained
interface, \(x_1,\ldots,x_{\ell-1}\) for the suffix's other
retained coordinates, and \(y_1,\ldots,y_{\ell-1}\) for its
ordinary indices. Use the original lifts
\[
 Q_\alpha(y;x,z)=g(y+x)+g(y+z)-(2+\alpha)g(y)
                        -g(x)-g(z)+2\pi ixy.
\]
Let \(\mathcal P_{\delta_\ell}(x_{\ell-1},w)\) be the
original optimized terminal action, including its entire own
diagonal weight. The suffix action before eliminating the
displayed internal variables is
\[
 \mathcal F_{\boldsymbol\delta}
  =\sum_{j=1}^{\ell-1}Q_{\delta_j}(y_j;x_{j-1},x_j)
       -\sum_{j=1}^{\ell-1}\delta_j g(x_j)
       +\mathcal P_{\delta_\ell}(x_{\ell-1},w).
 \tag{12}
\]
For \(\ell=1\) it is simply \(\mathcal P_{\delta_1}(c,w)\).
At the actual reference every displayed internal derivative
vanishes. The original
[principal Hessian and local source theorem](research_mixed_open_word_hessian.md)
give a holomorphic stationary elimination near that reference.
Denote its action by \(\mathcal P_{\boldsymbol\delta}(c,w)\).

For an incoming flag \(\gamma\), the allocated action is
\(\Pi_{\boldsymbol\delta,\gamma}
=\mathcal P_{\boldsymbol\delta}-\gamma g(c)/2\).
For \(\ell\ge2\), its surviving marginal is exactly
\[
 \Pi_{\boldsymbol\delta,\gamma}'(c_*)
   =g'(y_{1,*}+c_*)-(1+\gamma/2)g'(c_*)+2\pi i y_{1,*}.
 \tag{13}
\]
There is no derivative of a moving optimizer in (13), because
the eliminated internal derivatives are zero. The allocated
suffix value plus the prefix value is the original open action,
and their complex marginals at \(c_*\) cancel.
The source identity has introduced no new phase constant.

In the example (11), (12) is precisely
\[
 Q_1(r;c,b)+Q_0(s;b,a)-g(b)+\mathcal P_\epsilon(a,w).
 \tag{14}
\]
Its \(\partial_a=0\) equation joins the earlier outgoing
ordinary marginal \(g'(s+a)-g'(a)\) to the terminal marginal.
After the full contraction this marginal is internal; only
(13) remains. For the actual suffix, \(c_*\in K_{3+\gamma}\),
\(r_*,b_*\in O_4\), \(s_*,a_*\in O_3\).
No root or sign from the different \((\epsilon,1,\beta)\)
reference banks is used.

The local unselected current has the original nonzero packet.
More precisely let \(k_{\boldsymbol\delta}=\sum_j\delta_j\).
Expand (8) using the terminal source, and restrict its
\(\ell-1\) retained variables to a small neighborhood of their
original unselected critical contour. The
[completed local packets](research_mixed_full_unselected_plateau.md)
and their accretive Gaussian give
\[
 \mathcal B^{\mathrm{loc}}_{\boldsymbol\delta,N}(w,e^{-2\pi ic})
   =N^{-1-k_{\boldsymbol\delta}}
       A_{\boldsymbol\delta}(c,w)
       e^{N\mathcal P_{\boldsymbol\delta}(c,w)}
                                      (1+O(N^{-1})),
 \qquad A_{\boldsymbol\delta}\ne0.
 \tag{15}
\]
The exact power is
\[
 (\ell-1)
 -\sum_{j<\ell}\frac{1+\delta_j}{2}
 -\sum_{j<\ell}\frac{\delta_j}{2}
 -(1+\delta_\ell)-\frac{\ell-1}{2}
       =-1-k_{\boldsymbol\delta}.
 \tag{16}
\]
The terms are respectively the physical contraction factors,
conditional packets, retained weights, terminal packet, and
retained-variable Gaussian. The original amplitudes and
accretive square roots are unchanged. Equation (15) is for this
specified local current, not an asymptotic for the whole (8).

## 5. The resulting whole-source task

For (11), a useful completed boundary theorem would estimate the
whole coherent polynomial, at independent \(x\in P\) and
\(c=x+i\Im c_*\), by
\[
 \begin{split}
 |\mathcal B_{1,0,\epsilon,N}(w,e^{-2\pi ic})|\,
 |d_N(e^{-2\pi ic})|^{\gamma/2}
 \le C_\eta N^{A_\eta}\exp N\bigl\{
 &\Re\Pi_{1,0,\epsilon;\gamma}(c_*)\\
 &+\Re\Pi_{1,0,\epsilon;\gamma}'(c_*)(x-\Re c_*)\\
 &-\kappa_*(x-\Re c_*)^2+\eta\bigr\},
 \end{split}
 \tag{17}
\]
with its actual input/reference and color scope stated explicitly.
The halfweight is an allocation in modulus; squaring makes the
finite holomorphic product integral without choosing a square root
of \(d_N\). To preserve a nonzero whole boundary packet, one must
also control the complement of the local current (15) sufficiently
to exclude cancellation of its leading coefficient.

This is a different proof route from separately bounding the four
selected-sector defects. Formula (11) allows cancellation between
the \(b\) sectors, and never requires a separate positive bound
for their high Fourier coefficient. But neither the unselected
plateau theorem nor the completed local terminal theorem supplies
(17) or its complementary-current assertion automatically.
They control their specified contours and reference heights, not
every physical input of the reversed generalized cap in (11).

The exact class (7) is therefore suitable for a coherent induction,
but its useful analytic subclass remains to be proved. Taking a
norm depending only on arbitrary node magnitudes loses precisely
that extra information, as the sharp norm identity in the
[literal-transfer theorem](research_mixed_literal_transfer_norm_obstruction.md)
shows. In particular a complete conditional estimate for
\(C_{1,N}\) cannot be applied termwise after flattening all the
other indices without paying that change of phase and contour.
No positivity, whole-source noncancellation, or volume conclusion
is inferred here.
