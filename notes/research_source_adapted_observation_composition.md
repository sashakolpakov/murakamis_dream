# A composition criterion for the original marked observation

Research deduction, 5 November 2026. A small residual along a proposed
source line is insufficient for a lower bound after composition.
One must also control feedback from its complement and the actual
closing row. This note gives an exact sufficient criterion, including
branching contractions, without positivity of the original matrices.
The criterion is not asserted for general short fillings.

## 1. The observation and the allowed exact maps

At level \(N\), let \(M\) be the original Newton crossing, \(J\) index
reversal, and \(v(z)\) the full ordinary Newton evaluation column.
For a chain with arbitrary fixed integer powers, put
\[
 A_n=JM^n,\qquad H=M^*M,\qquad
 W=A_{n_1}\cdots A_{n_m},\qquad
 C_N(z,w)=v(z)^TWv(w).
 \tag{1}
\]
Here \(^*\) denotes the Hilbert-space adjoint; the physical closing
functional uses \(^T\), not \(^*\). The exact
[positive-three similarity](research_positive_three_crossing_cycle.md)
implies, for every integer \(n\),
\[
 M A_nM^{-1}=\kappa H M^{n-3},\qquad |\kappa|=1.
 \tag{2}
\]
Indeed \(A_n=A_3M^{n-3}\) and \(M\) is invertible. Thus (1) is an
exact observation \(\ell T_m\cdots T_1x_0\), with
\[
 x_0=Mv(w),\qquad \ell=v(z)^TM^{-1},\qquad
 T_j=\kappa HM^{\,n_{m+1-j}-3}.
 \tag{3}
\]
The order in (3) is the order of application to the input.
Both parities and all physical normal directions remain present.
The [Casimir mark](research_mixed_ordinary_boundary_casimir_mark.md)
and [modified-vertex contraction](research_mixed_marked_vertex_contraction.md)
are alternative exact representations of this same observation.
They do not change \(\ell\) into a positive quadratic observation.

More generally, the
[arbitrary-power compiler](research_arbitrary_power_source_compilation.md),
Sections 1--2, expresses a fixed partially filled circle-tree source
as a finite expression tree of linear maps
\[
 T_v:\bigotimes_{i\in{\rm ch}(v)}\mathcal H_i\longrightarrow\mathcal H_v.
 \tag{4}
\]
These maps contain the actual multiplication tensor, turns and signed
crossings. The root is followed by the prescribed linear observation.
One may choose positive Hilbert norms on the finite coefficient
spaces for estimates; the maps and observation themselves are unchanged.
An unreduced free ordinary polynomial is kept in its full coefficient
space. In particular (4) does not reduce a free high-degree polynomial
modulo the physical relation.

## 2. Exact line and complement decomposition

Choose a unit vector \(r_i\in\mathcal H_i\) in each output space.
These are proposed source directions, not asserted eigenvectors.
At a node \(v\), let
\[
 u_v=\bigotimes_{i\in{\rm ch}(v)}r_i,\qquad
 P_v=r_vr_v^*,\quad Q_v=I-P_v,\quad Q_v^{\rm in}=I-u_vu_v^*.
 \tag{5}
\]
Define the four blocks and their nonnegative bounds by
\[
\begin{split}
 a_v&=r_v^*T_vu_v,&
 b_v&=\|r_v^*T_vQ_v^{\rm in}\|,\\
 c_v&=\|Q_vT_vu_v\|,&
 d_v&=\|Q_vT_vQ_v^{\rm in}\|.
\end{split}
 \tag{6}
\]
No sign or phase restriction is imposed on \(a_v\).

Suppose the actual child vectors have decompositions
\[
 x_i=A_i(r_i+e_i),\qquad r_i^*e_i=0,\qquad
 A_i\ne0,\quad \|e_i\|\le\rho_i.
 \tag{7}
\]
Their tensor product is
\[
 \bigotimes_i x_i=\left(\prod_i A_i\right)(u_v+\zeta_v),
 \quad u_v^*\zeta_v=0,\quad
 \|\zeta_v\|\le t_v:=
       \sqrt{\prod_i(1+\rho_i^2)-1}.
 \tag{8}
\]
To verify (8), the coefficient along \(u_v\) is exactly one, and
the squared norm of the product of \(r_i+e_i\) is exactly
\(\prod_i(1+\|e_i\|^2)\). Orthogonality then gives its complementary
squared norm. Thus branching does not require adding the phases or
absolute values of the child amplitudes.

**Theorem 1.** At every internal node assume
\[
 L_v:=|a_v|-b_vt_v>0,\qquad
 c_v+d_vt_v\le \rho_v L_v.
 \tag{9}
\]
Then the actual output again has the form (7), and
\[
 L_v\prod_i|A_i|\le |A_v|
       \le (|a_v|+b_vt_v)\prod_i|A_i|.
 \tag{10}
\]

*Proof.* Set
\[
 \alpha_v=a_v+r_v^*T_v\zeta_v,\qquad
 A_v=\alpha_v\prod_i A_i,\qquad
 e_v=\frac{Q_vT_vu_v+Q_vT_v\zeta_v}{\alpha_v}.
 \tag{11}
\]
The denominator has modulus at least \(L_v>0\). These equations
are the exact decomposition of \(T_v\bigotimes_i x_i\);
(9) bounds \(\|e_v\|\) by \(\rho_v\), and the two bounds on
\(|\alpha_v|\) give (10). Induction proves the assertion.
\(\square\)

An exact nonzero leaf vector may be taken as its own normalized
direction, with zero error. Useful proposed directions in subsequent
output spaces must be controlled independently of the unknown contracted
output; choosing every \(r_v\) to be that output would make the
criterion tautological.

## 3. The sharp closing condition and the resulting rate

Let \(o\) be the root, with its actual row \(\ell\). Put
\[
 \gamma=|\ell r_o|,\qquad \beta_\partial=\|\ell Q_o\|.
 \tag{12}
\]
The sufficient final condition is
\[
 \gamma>\beta_\partial\rho_o.
 \tag{13}
\]
Under (9) and (13), the original scalar \(Z=\ell x_o\) is nonzero,
and Theorem 1 gives
\[
\begin{split}
 |Z|&\ge(\gamma-\beta_\partial\rho_o)
       \prod_{\text{internal }v}(|a_v|-b_vt_v)
       \prod_{\text{leaves }i}|A_i|,\\
 |Z|&\le(\gamma+\beta_\partial\rho_o)
       \prod_{\text{internal }v}(|a_v|+b_vt_v)
       \prod_{\text{leaves }i}|A_i|.
\end{split}
 \tag{14}
\]
This is coercivity only on the specified set of vectors:
\[
 |\ell x_o|\ge
 \frac{\gamma-\beta_\partial\rho_o}{\sqrt{1+\rho_o^2}}\,
                  \|x_o\|.
 \tag{15}
\]
The criterion is sharp if only this radius and the row are known.
When \(\beta_\partial>0\) and
\(\gamma\le\beta_\partial\rho_o\), the complementary vector
\[
 e=-\frac{\ell r_o}{\beta_\partial^2}\,Q_o\ell^*
 \tag{16}
\]
has norm at most \(\rho_o\) and satisfies \(\ell(r_o+e)=0\).
Equation (16) is a linear-algebra obstruction, not an asserted
source produced by a particular filling.

More precisely, define
\[
 Z_0=(\ell r_o)\prod_{\text{internal }v}a_v
                         \prod_{\text{leaves }i}A_i,\qquad
 \varepsilon_v=\frac{b_vt_v}{|a_v|},\quad
 \varepsilon_\partial=\frac{\beta_\partial\rho_o}{\gamma}.
 \tag{17}
\]
The exact recursive equations yield complex numbers
\(\delta_v,\delta_\partial\) such that
\[
 \frac{Z}{Z_0}=(1+\delta_\partial)
                 \prod_{\text{internal }v}(1+\delta_v),
 \quad |\delta_v|\le\varepsilon_v,\quad
       |\delta_\partial|\le\varepsilon_\partial.
 \tag{18}
\]
All original scalar phases stay in \(Z_0\) and these factors;
none is replaced by its modulus in this identity.

For a fixed tree, if every error in (17) is bounded by one fixed
number less than one, then
\[
                 \log|Z|=\log|Z_0|+O(1).
 \tag{19}
\]
Consequently a known exponential rate of \(Z_0\) is the rate of
the actual marked source. If the errors tend uniformly to zero,
then \(Z/Z_0\to1\) uniformly. For increasing trees, the corresponding
sufficient rate condition is that the sum of the absolute logarithms
of \(1-\varepsilon\) and \(1+\varepsilon\) is \(o(N)\);
no such growing-tree uniformity is assumed here.

## 4. A reusable chain condition

For unary nodes, \(t_v=\rho_{v-1}\). Suppose that uniformly along
a chain, after division by \(|a_v|\),
\[
 b_v/|a_v|\le b,\quad c_v/|a_v|\le c,\quad
 d_v/|a_v|\le d,\qquad
 d<1,\quad \Delta=(1-d)^2-4bc>0.
 \tag{20}
\]
If \(c>0\), put
\[
 \rho=\frac{2c}{1-d+\sqrt{\Delta}}.
 \tag{21}
\]
Then \(b\rho<1\) and
\[
       c+d\rho=\rho(1-b\rho),
 \tag{22}
\]
so (9) propagates the same radius. The formulas include \(b=0\).
If \(c=0\), the zero-radius line is exactly transported.

There is also genuine forgetting inside this set. For the complex
projective error map in (11), two errors of norm at most \(\rho\)
satisfy
\[
 \|\mathcal F_v(e)-\mathcal F_v(f)\|
 \le q\|e-f\|,\qquad
 q=\frac{d+b\rho}{1-b\rho}<1.
 \tag{23}
\]
Indeed subtract the two exact fractions to obtain
\[
 \mathcal F_v(e)-\mathcal F_v(f)
 =\frac{(Q_vT_vQ_v^{\rm in}
          -\mathcal F_v(f)\,r_v^*T_vQ_v^{\rm in})(e-f)}
        {a_v+r_v^*T_v e}.
 \tag{24}
\]
The norm bound gives (23), while
\(1-d-2b\rho=\sqrt{\Delta}>0\).
This is a criterion for the actual transported source directions,
not a consequence of a spectral gap for a different operator.
It works for complex maps and requires no common positive invariant
inner product.

For a finite family of original blocks, uniform (20) and a uniform
closing condition (13) would handle every fixed chain made from that
family, with arbitrary length fixed before \(N\to\infty\).
For branching use the exact \(t_v\) in (8) instead. The degree and
the block norms enter this test explicitly.

## 5. What the current estimates do and do not supply

The residual of a line alone is \(c_v\) in (6). It controls neither
the feedback \(b_v\), the complementary evolution \(d_v\), nor (13).
For example,
\[
 T_\epsilon=\begin{pmatrix}1&-\epsilon^{-1}\\
                            \epsilon&0\end{pmatrix},
 \quad r=\binom10,\quad \ell=(1,0)
 \quad\Longrightarrow\quad
 \|T_\epsilon r-r\|=\epsilon,\qquad
                    \ell T_\epsilon^2r=0.
 \tag{25}
\]
This two-dimensional example is not an original word.
It exhibits exactly the missing feedback bound \(bc=1\).
The original-source examples in
[almost-invariance and observation](research_original_almost_invariance_and_observation.md)
give a separate actual obstruction: a geometric quasimode can have
an exponentially small physical cap overlap. Thus (13) cannot be
deleted on the ground that the line is geometric.

Even the proved homogeneous-three spectral gap does not resolve
that scale issue. If \(H/L\) has top projection \(P\) and
\(\|(H/L)-P\|\le\eta<1\), its powers shrink the complementary
radius by \(\eta^k\). But if the normalized cap overlap is
\(|\ell r|/\|\ell\|=\exp(-\sigma N+o(N))\), condition (13)
for a fixed positive initial radius requires a buffer length at
least \(\sigma N/|\log\eta|+o(N)\) using this bound.
The fixed-word cyclic theorem supplies no uniform asymptotic at
such a level-dependent length. No such overlap rate is asserted
here for its particular top vector.

The local open Hessian and Gaussian theorems identify the proposed
geometric directions and their local phase. The
[finite boundary-window reduction](research_mixed_open_finite_boundary_windows.md)
controls an upper rate and leaves the literal boundary source sign
open. Neither statement estimates the full blocks \(b_v,c_v,d_v\)
in (6), or the normalized physical cap angle in (13).
The [Gaussian observation estimate](research_shifted_gaussian_observation.md)
does prove an observation condition once its global residual and
complementary-cycle hypotheses are verified; a local quadratic
Hessian alone does not verify those hypotheses.

The full physical value/normal upper bounds in the
[marked-vertex note](research_mixed_marked_vertex_contraction.md)
can contribute to upper estimates of these blocks. The diagonal
far-color loss there is not a lower bound on \(a_v\) or
\(\ell r_o\). Likewise, nonnegative scalar Fejér weights do not
imply any condition in (9) or (13) for their complex marked trace.

## 6. The precise possible short-filling use

This gives a sufficient alternative to checking a separate boundary
comparison for every composite word: construct a family of source
directions for the original block maps, prove (9) and (13) uniformly
on the required boundary domains, and identify the product \(Z_0\).
The estimate includes arbitrary signed powers and branching because
the exact compiler includes them; their inequalities are new
hypotheses, not consequences of the \(3/4\) calculation.

For an open holomorphic packet, more than its rate is needed.
If the actual source and a zero-free model product \(Z_0\) are
holomorphic on a common boundary neighborhood and the errors in
(18) tend uniformly to zero there, then the exact quotient
\(Z/Z_0\) is holomorphic and tends to one. Cauchy's formula gives
the corresponding fixed-derivative statement on smaller domains.
A quantitative error rate in (18) gives that rate in this conclusion.
The chosen Hilbert-space directions themselves need not be
holomorphic if their scalar product \(Z_0\) has the asserted
holomorphic model.

Whole-boundary angular or strip losses must still be supplied,
for example by uniform upper bounds for the factors in (14) with
the desired loss. Finally the model phase must equal the original
geometric action with its marked primitive slopes and absolute
constant. Neither that identity for arbitrary partial fillings nor
the required block estimates is proved by this criterion.

The [finite-exception branching lemma](research_finite_exceptions_under_partial_fillings.md#3-a-finite-exception-lemma-for-one-template)
requires stability at every partial assignment visited by its finite
tree. It permits constants depending on that assignment. Therefore
one need not find a single metric, radius or threshold for all
integer fillings at once. One does need the original observed
source estimates to survive each required composition, including
any changed geometric class. Equations (9), (13) and (18) are an
explicit sufficient target for that task, with no positivity or
unmarked-trace substitution.
