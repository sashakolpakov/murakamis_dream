# Independent check of the vertex-scaled local-volume criterion

1 November 2026.

## 1. Conclusion

The proposed strengthening of the local-message theorem is valid by
the displayed proof, with the original fixed-tree interpretation.
For some chosen order-of-evaluation root \(r_*\), the sufficient
conditions are
\[
 d_v^2+n_v^2\ge2^{82}\quad\text{for every vertex},\qquad
 \frac{d_v}{d_v^2+n_v^2}\le2^{-47}\quad(v\ne r_*).
\]
In particular all fixed signed powers \(|n_v|\ge2^{46}\) suffice.
The main-parameter radius remains any fixed \(R<1\), and no graph or
power is allowed to grow with the level.

This check follows the fresh source audit in
md-local-volume-fresh-audit.md. It does not use an earlier approval
of the original numerical condition. No public file was changed.

There is one scalar-description precision: the exact contraction
(1a) must leave outside the original **closing/framing, opposite-order
reference, and reduced-cut factors**. The source treats the mixed
reference factors separately from the closing scalar. They must not
disappear in the wording of the reordered contraction. This does not
change any bound or require a mathematical alteration of the argument.

## 2. Exact rerooting does not change the typed source

The lower-index source is a finite sum of a product of vertex tensors
and diagonal edge tensors:
\[
 \sum_{\mathbf k}
 \prod_e\left(\gamma_e(s)\frac{H_N(s)}{W_{k_e}(s)}\right)
 \prod_v
 \phi_{\sigma_v}\left(R_{\sigma_v}^{n_v}
                    \prod_{e\ni v}e_{k_e}\right).
\]
Here every \(\sigma_v\), crossing reference, edge scalar and external
closing factor is the one already assigned by the original physical
compiler. No type is reassigned when the sum is evaluated in another
order.

The edge contraction matrix is diagonal, hence symmetric. Evaluating
the finite sum from any selected vertex therefore gives exactly the
same kernel recursion with that vertex evaluated last. In particular
one must keep an edge's original \(\gamma_e\), rather than replacing
it by the scalar for a newly imagined physical inverse turn.
The root's trace is its original vertex tensor, not a new physical
closure functional. The original marked cut and its one \(H_N\)
factor stay outside unchanged.

Thus the proposal is algebraic Fubini for an already compiled tensor
network. It uses neither ambient isotopy nor a physical half-turn
identity. At the final root there is no parent angle and no outgoing
polynomial whose real envelope must be regenerated.

## 3. Saddle size and the current-vertex drop

Put
\[
 a_v=\frac{d_v}{2\pi},\qquad
 D_v=\frac{d_v-in_v}{2\pi},\qquad R_v=\sqrt{d_v^2+n_v^2}.
\]
Since \(R_v\ge2^{41}\) and \(2\pi<8\),
\[
 |D_v|>2^{38}.
\]
Consequently the first saddle lies deeply inside the fixed disk and
the retained cutoff
\(\lfloor2^{-16}|D_v|\rfloor\) is at least one, in fact much larger.
The phase-class contraction and all charge inequalities use
\(|D_v|\ge a_v\), so they remain valid at a large-degree zero-power
root, where equality holds.

The exact first-drop estimate is
\[
 \Delta_v\le\frac{210}{361}\frac{a_v}{|D_v|^2}
 <2^{-76}a_v.
\]
The strict inequality follows from \(|D_v|^2>2^{76}\) and
\(210/361<1\). With \(\eta_v=2^{-75}a_v\), this gives
\(\Delta_v<\eta_v/2\), including at the exempt root. For nonroot
vertices the independent estimate \(\Delta_v<4\kappa_v\) is retained
for the outgoing envelope.

## 4. Every absolute conditional error keeps the factor \(a_v\)

The relevant errors in the actual finite trace are:

* Infinite charge tail:
  \(\tfrac12 A_0t_0^2a_v=2^{-74}a_v\).
* Real complement of the local interval:
  \(2^{-20}a_v\rho^2=2^{-48}a_v\).
* Local vertical connectors:
  \(a_v\rho^2/8=2^{-31}a_v\).
* Original vertical sides and zero-mode endpoint currents:
  at least \(\tfrac12\,2^{-20}\pi^2a_v\).

These follow directly from the full normalized input's Gaussian
\(-2^{-20}a_v t^2+128a_vy^2\), and not from an unnormalized
augmented action. Thus all exceed the selected \(\eta_v\). Fixed
polynomial prefactors and a fixed finite number of retained charges
are absorbed by the margin between \(2^{-74}a_v\) and
\(2^{-75}a_v\). The infinite tail is a geometric series once \(N\)
exceeds a threshold depending on its positive fixed height.

The source argument also has finite interpolation errors in the
local edge kernel. They do **not** invalidate this list. The complete
kernel has a uniform relative holomorphic saddle expansion on the
small bidisk. This is substituted on the local deformed contour,
where it multiplies the selected phase and amplitude. It is not
estimated as an arbitrary absolute error at \(2G_0\) on the original
real contour.

The same distinction applies to child messages. They are retained
exactly, divided by their exact nonzero values at zero, and represented
by a local logarithm plus an analytic amplitude correction.
Their normalized errors are not expanded into absolute augmented
remainders. On the selected local Gaussian contour the absolute
Gaussian integral is comparable to its nonzero leading term for the
fixed data. Therefore a uniform holomorphic relative error stays
relative there. This remains true even if \(a_v\) is so large that
\(\eta_v\) exceeds the fixed interpolation gap.

No other absolute error from the original local proof needs a
degree-independent subtraction. The translated endpoints differ by
\(O(1/N)\) and change only allowed fixed-data prefactors.

## 5. Outgoing-envelope regeneration

At nonroot vertices, the full polynomial trace norm gives
\[
 |M_v(u)|\le C N^A\left|\prod_wM_w(0)\right|
 e^{N(2G_0-c_K(1-\cos u))}.
\]
The lower asymptotic at zero has rate \(2G_0-\Delta_v(0)\).
For \(r=2^{-12}\), \(c_K=2^{-16}\), \(c=2^{-18}\),
\[
 (c_K-c)(1-\cos(r/2))
 \ge3\,2^{-18}\frac{2^{-26}}3=2^{-44}.
\]
Here \(1-\cos x\ge x^2/3\) for \(0\le x\le1\); Taylor's lower
bound \(x^2/2-x^4/24\) already proves it.
Meanwhile the nonroot condition gives
\[
 \Delta_v(0)<4\kappa_v\le2^{-45}.
\]
There is a factor-two margin in the required envelope comparison.
The small interval uses the stronger local phase Hessian, then the
exact degree bound and Poisson estimate regenerate the strip.

This is the only use of the additional \(\kappa_v\) condition.
The root only needs its incoming messages, conditional saddle and
tail comparison. It does not require its own version of this outgoing
envelope step.

## 6. Geometry, normalization, and scope

The bound \(R_v\ge2^{41}\) is stronger than the geometric radius
criterion \(R_v\ge630\). The same weighted simultaneous contraction
therefore gives the actual positive charge path
\[
 |\tau_v(c)|\le\frac{c}{(1-1/50)|D_v|}<10^{-2},
 \qquad \operatorname{Im}\tau_v(c)<0 \quad(c>0).
\]
The selected action, original primitive periods and unfilled main
cusp are unchanged. The stronger criterion does not introduce a new
scalar-to-volume inference.

Likewise the nonzero first coefficient, Gaussian power \(N^{3/2}\),
exact quadratic framing/reference scalar, and single reduced-cut
\(H_N\) are unchanged by the order of finite evaluation. Thus the
same \(O(N^{-1})\) profile and actual knot volume equality follow.
An optional higher-order profile statement still requires its
higher-order insertion expansion, not just this numerical improvement.

Finally \(d/(d^2+n^2)\le1/(2|n|)\), and \(|n|\ge2^{46}\) gives
\(\kappa\le2^{-47}\) and \(d^2+n^2\ge2^{92}>2^{82}\). This proves
the claimed universal sufficient integer bound. An exempt root can
also have a much shorter or zero power if its degree supplies the
first condition; it remains an actual crossing-circle vertex and
does not represent deleting or padding the original knot diagram.
