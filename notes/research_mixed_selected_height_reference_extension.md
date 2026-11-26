# Extending a reference bound when selected heights are prescribed separately

Research lemma, 4 November 2026. This is an analytic extension principle.
It allows different coordinates to retain different fractions of their
reference heights, while other coordinates have prescribed heights.
The reference phase and the target phase may differ. No numerical support
gap or new finite-source estimate is asserted here. The earlier
[common-height lemma](research_mixed_height_coupled_reference_extension.md)
and all of its artifacts remain unchanged.

## 1. Fixed parameters and holomorphic branches

Let \(\mathcal R=\prod_{\ell=1}^k R_\ell\), where
\[
 R_\ell=[a_\ell,b_\ell]+i[c_\ell,d_\ell],\qquad
 L_\ell=d_\ell-c_\ell>0.
\]
Suppose \(z:\mathcal R\longrightarrow\mathbb C^n\) is holomorphic
on a neighborhood of this closed product. Let \(F\) be holomorphic
near its image. Fix real vectors \(x,\beta\), nonnegative numbers
\(\kappa_1,\ldots,\kappa_n\), a real constant \(C_0\), and a real diagonal
matrix
\[
 \Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n),
 \qquad 0\le\lambda_j\le\lambda_*.
\]
All of these are held fixed while differentiating the reference
parameters. Define
\[
 w=x+i\beta+\frac12\Lambda(z-\bar z)
       =x+i\{\beta+\Lambda\Im z\}.                        \tag{1}
\]
Let \(\Psi\) be holomorphic on a neighborhood of the entire target
image in (1), with
\[
                    -\Re\Psi''(w)\succeq0.                 \tag{2}
\]
Here the real part is entrywise, giving a real symmetric matrix.
The branch and domain assumptions precede every maximum principle
below; a boundary root calculation alone does not supply them.

The defect to be extended is
\[
 D=\Re\{\Psi(w)-F(z)-F'(z)\cdot(w-z)\}
                  +\sum_j \kappa_j(\Im z_j)^2+C_0.         \tag{3}
\]
In particular, \(D\) need not be subharmonic. Neither the target
height in (1) nor the affine subtraction is holomorphic in the
reference parameters.

## 2. Exact Laplacian and the extension bound

Fix one complex parameter \(p_\ell\) and write
\(q=\partial_{p_\ell}z\). With all other parameters fixed, the
exact identity is
\[
 \begin{split}
 \Delta_\ell D={}&
 -\Re\{q^T\Lambda\Psi''(w)\Lambda\bar q\}
 +2\Re\{q^TF''(z)\Lambda\bar q\}
 +2\sum_j\kappa_j|q_j|^2.                                 \tag{4}
 \end{split}
\]
To verify it, use
\(\partial_pw=\Lambda q/2\) and
\(\partial_{\bar p}w=-\Lambda\bar q/2\).
The target term in (3) gives the first term of (4). For the affine
remainder, write
\(-F'(z)\cdot w+F'(z)\cdot z-F(z)\). Its
\(\bar p\)-derivative is \(F'(z)\Lambda\bar q/2\);
applying \(\partial_p\), taking the real part and multiplying by
four gives the second term. Finally,
\(\Delta(\Im z_j)^2=2|q_j|^2\).

For a complex symmetric matrix \(H\) and \(q=u+iv\),
\[
 \Re(q^TH\bar q)=u^T\Re(H)u+v^T\Re(H)v.
\]
Thus (2) makes the first term of (4) nonnegative. The last term is
also nonnegative. Define
\[
 B_\ell(p;\Lambda)
   =\sum_{i,j}\lambda_j
       |q_iq_j F''_{ij}(z)|.
                                                               \tag{5}
\]
It follows that
\[
                  \Delta_\ell D\ge-2B_\ell(p;\Lambda).
                                                               \tag{6}
\]
Each summand in (5) is the modulus of a holomorphic function.
Consequently \(B_\ell\) is separately subharmonic on the closed
reference product. A uniform bound
\(B_\ell\le\mathcal B_\ell\) on its distinguished boundary
therefore holds throughout the product. The simpler bound
\[
 B_\ell(p;\Lambda)\le\lambda_*
                \sum_{i,j}|q_iq_jF''_{ij}(z)|                 \tag{7}
\]
is often sufficient.

**Theorem 1.** Under the preceding hypotheses, suppose on the full
distinguished boundary \(\prod_\ell\partial R_\ell\) that
\(D\le-\gamma\) and \(B_\ell\le\mathcal B_\ell\) for every
\(\ell\). Then throughout \(\mathcal R\),
\[
 D\le-\gamma+
   \sum_\ell\mathcal B_\ell
       (\Im p_\ell-c_\ell)(d_\ell-\Im p_\ell)
 \le-\gamma+\frac14\sum_\ell\mathcal B_\ell L_\ell^2.
                                                               \tag{8}
\]

**Proof.** Let
\(v_\ell=\mathcal B_\ell(y_\ell-c_\ell)(d_\ell-y_\ell)\).
Then \(v_\ell\ge0\),
\(\Delta_\ell v_\ell=-2\mathcal B_\ell\), and
\(v_\ell\le\mathcal B_\ell L_\ell^2/4\).
The function \(D-\sum v_\ell\) is separately subharmonic by
(6). Successive maximum principles reduce it to the distinguished
boundary. There it is at most \(-\gamma\), because every
\(v_\ell\) is nonnegative, including on the vertical sides of a
rectangle. Adding the barriers gives (8). \(\square\)

The same conclusion holds uniformly over any compact collection of
the fixed target parameters, provided the stated branch, curvature,
boundary-defect and response bounds are uniform. It is enough to apply
the theorem separately with each parameter fixed; no differentiation
of a target optimizer or a selection maximum is required.

## 3. The exact expression for a selected right-transition pair

This section identifies an application of the lemma, rather than
asserting its quantitative hypotheses. Use the original normalization
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}.
\]
For three consecutive reference legs \(z=(z_0,z_1,z_2)\), let
\[
 F(z)=\phi_{\alpha\beta}(z_0,z_1)
                     +\phi_{\beta\gamma}(z_1,z_2).
\]
The phases and their original logarithmic lifts are those of the
[unselected paired theorem](research_mixed_paired_right_transition_support.md).
Let \(\sigma_j\in\{0,1\}\) indicate a selected type-four leg;
selection is forbidden on a type-three leg. Put
\(a=(1/2,1,1/2)\), \(H=7/500\), and for each choice
\(f_j\in\{0,\ldots,\sigma_j\}\) set
\[
 \Psi_f(w)=F(w)+\sum_{j=0}^2a_j
       \{f_jg(w_j)+2\pi i(\sigma_j-f_j)w_j\}.              \tag{9}
\]
The middle coefficient is one because its two allocated Fourier
halfweights have been combined. Taking the maximum over (9) retains
both actual Fourier branches at every selected leg. In particular,
the forcing branch is not discarded when a height reaches zero.

**Corollary 2 (target curvature).** Every branch in (9) has
\(-\Re\Psi_f''>0\) on the auxiliary target box
\(\Re w_j\in[.22,.5]\), \(|\Im w_j|\le.063\).
This assertion concerns phase and curvature only.

Indeed, the cotangent estimate (8) of the paired theorem gives
\(\Re\cot(\pi w_j)\ge0\) and
\(|\Im\cot(\pi w_j)|<1/2\). The
[closed-cotangent theorem](research_mixed_closed_cotangent_roots.md)
therefore supplies the original simple conditional roots and positive
triangle forms, including the outer face at real part .5. Before
eliminating a block's inner coordinate, its phase is
\[
 V(s,a)+V(s,b)-\epsilon g(s)
                -\frac\eta2 g(a)-\frac\epsilon2 g(b)
                +2\pi ias,
 \qquad V(s,a)=g(s+a)-g(s)-g(a).
\]
Adding that block's share of (9) changes the two extra outer
coefficients to \((\eta-f_a)/2\) and
\((\epsilon-f_b)/2\). They remain nonnegative, since
\(f_a\le\sigma_a\le\eta\) and
\(f_b\le\sigma_b\le\epsilon\). The inner coefficient
\(\epsilon\) is unchanged. The additional frequency terms have
zero Hessian; the original chirp has zero real Hessian.
The positive triangle forms plus these nonnegative own-factorial
terms have positive real Hessian with the negative sign. The exact
complex Schur identity preserves positivity after eliminating the
inner coordinate. Adding the two condensed blocks proves the
corollary. In particular, no new numerical curvature cover is needed.

Fix \(p,q\in[.22,.45]\), \(t\in[.45,.5]\), and
\(\tau=20(.5-t)\). The corresponding target is
\[
 w=(p,t,q)+i\tau\{(1-\sigma)\Im z+H\sigma\}.              \tag{10}
\]
Thus (1) applies with
\(\Lambda=\tau\operatorname{diag}(1-\sigma)\) and
\(\beta=\tau H\sigma\). All of these parameters are fixed during
reference differentiation, even though they vary in the eventual
target comparison.

The two exterior plateau blocks may be charged by the existing
[oriented reset](research_mixed_oriented_height_reset.md) and
[partial selected-height](research_mixed_partial_selected_heights.md)
bounds. With \(q_0=151/20\), \(q_2=11/2\), and
\(\delta=1/100\), their total upper debit is
\[
 C_\sigma(z;\tau)=\sum_{j\in\{0,2\}}
 \begin{cases}
 (1-\tau)^2q_j(\Im z_j)^2,&\sigma_j=0,\\
 (1-\tau)q_j(\Im z_j)^2-\tau\delta,&\sigma_j=1.
 \end{cases}                                                \tag{11}
\]
The exterior coordinate of each such block is required to remain at
its prescribed height: its reference height if unselected, or \(H\)
if selected. In the latter case a neighboring selection only improves
the bound in (11). No claim for overlapping transition stars is made.

Subtract the original complex tangent
\(F(z)+F'(z)\cdot(w-z)\) from (9) and add (11).
This is exactly (3), with nonnegative quadratic coefficients
\[
 \kappa_j=q_j\{(1-\sigma_j)(1-\tau)^2+\sigma_j(1-\tau)\}
 \quad(j=0,2),\qquad \kappa_1=0,
\]
and \(C_0=-\tau\delta(\sigma_0+\sigma_2)\).
If the target branches have (2), and the unweighted reference
response sums are at most \(B_\ell\), their extension cost is
at most
\[
                        \frac\tau4\sum_\ell B_\ell L_\ell^2.
                                                               \tag{12}
\]
The quadratic debit contributes a favorable Laplacian; it does not
add a new extension cost. For example, two reference rectangles of
imaginary width at most \(1/20\), and bounds \(B_\ell\le1/5\),
give a cost at most \(1/4000\).

This algebra does not establish the missing boundary support estimate
for (9)--(11). Nor does it turn a holomorphic phase on auxiliary
reference images into a finite-source packet there. To obtain an
actual selected-pair theorem one must still prove the full boundary
comparison and use a complete finite-source theorem on the actual
target domain. Corollary 2 supplies (2) on the displayed auxiliary
box; the reference image and response bounds must also be retained.

## 4. Reproduction

The general proof is the Wirtinger calculation above. The following
checker independently verifies its algebra on nonlinear holomorphic
reference maps with unequal diagonal factors, different target and
reference cubics, and nonzero prescribed heights. It also checks the
matrix identity, barriers, specialization and exact debit bookkeeping.
These symbolic checks are not a numerical support certificate.

```sh
python3 experiments/check_mixed_selected_height_reference_extension.py
```
