# Local minimum-level inequalities with constant selected heights

Research note, 4 November 2026. This is a local phase-derivative result.
The wholly unselected inequalities, the enlarged finite-source cap and
the global selected transport implication are separate inputs; none is
inferred from this 78-domain calculation.

This note treats real coordinates in \([.12,.45]\). It does not treat
the earlier selected rise \((.10,.12)\), or import old right-half support
bounds onto a changed contour.

## 1. The local problem

Let \(P=[.22,.45]\), \(H=7/500\), and \(r_t=(t-.10)/.12\).
The current minimum is \(t\in[.12,.22]\). Unselected type-three
height coefficients range through \([-.03,.02]\); unselected type-four
coefficients range through \([-.057,-.02]\). Selected type-four targets
have height exactly \(H\), independent of \(t\). Their height
**derivative** is zero. This distinction is retained everywhere below.

The phase is the original sum of allocated block phases
\(\Phi=\sum_j\phi_j(z_j,z_{j+1})\), and \(G_j=\partial_j\Phi\).
This note proves only local inequalities for its derivatives. Exact
coupled-contour deformation, the genuine Fourier maximum, and the
whole selected transport consequence are separate arguments.

## 2. The new local inequalities

Use states \(0,1,2\) for unselected type three, unselected type four,
and selected type four. Set \(b_j=c_j\) in states zero and one, and
\(b_j=0\) in state two. The latter is a **height derivative
coefficient**, not the actual selected height, which remains \(H\).
For a coordinate \(i\) at the current minimum \(t\in[.12,.22]\), put
\[
 D_i^S=\Re G_i+
       \sum_{j\in(i-1,i,i+1)}
             \min\{-(25/3)b_j\Im G_j,0\}.                    \tag{1}
\]
The sum retains multiplicity. Let \(\kappa=3/2\),
\(\gamma_i=\mathbf1_{i\in S}/10\), and define the left and right
half expressions, for switches \(\chi,\xi\in\{0,1\}\), by
\[
\begin{split}
 L_i(\chi,\xi)={}&\Re\left[
 (1+i\chi b_i/.12)(\partial_2\phi_{i-1}+i\kappa)
       +i\xi b_{i-1}G_{i-1}/.12\right]+\gamma_i,\\
 R_i(\chi,\xi)={}&\Re\left[
 (1+i\chi b_i/.12)(\partial_1\phi_i-i\kappa)
       +i\xi b_{i+1}G_{i+1}/.12\right]-\gamma_i.
\end{split}                                                     \tag{2}
\]
A selected center needs only \(\chi=0\), and a selected neighbor needs
only \(\xi=0\). Both the imaginary gauge \(\pm i\kappa\) and the
new real gauge \(\pm\gamma_i\) cancel exactly. In particular
\[
 D_i^S=\min_{\chi,\xi_-,\xi_+}
          \{L_i(\chi,\xi_-)+R_i(\chi,\xi_+)\}.                \tag{3}
\]

The released outer coordinate in each half has real part between
\(t\) and \(.45\). Write \(r_t=(t-.10)/.12\). Its allowed polygon is
\[
\begin{array}{ll}
 0:&\operatorname{conv}\{(t,-.03r_t),(.22,-.03),(.45,-.03),
                         (.45,.02),(.22,.02),(t,.02r_t)\},\\
 1:&\operatorname{conv}\{(t,-.057r_t),(.22,-.057),(.45,-.057),
                         (.45,-.02r_t),(t,-.02r_t)\},\\
 2:&[t,.45]+iH.
\end{array}                                                       \tag{4}
\]
The center and adjacent neighbor have respective real parts \(t\) and
\(x_n\in[t,.45]\). Their unselected heights are \(r_t c_c,r_t c_n\);
a selected one has height \(H\). The intervals for \(c_c,c_n\) are
independent. Actual minimum-neighbor configurations are contained in
these released sets.

For fixed center and neighbor the half expression is the real part of
a holomorphic function of the released outer coordinate. Its minimum
therefore lies on a polygon edge. There is no harmonic reduction in the
other four real parameters. All old unselected polygons lie in the
proved cotangent chamber. The added selected horizontal segment lies
there too: its worst imaginary cotangent occurs at \(.12+iH\), and
\[
 \frac{\sinh(2\pi H)}{\cosh(2\pi H)-\cos(.24\pi)}<\frac12.    \tag{5}
\]
Thus the original zero-lift conditional phase is holomorphic throughout
the required products, before this boundary reduction is used.

**Theorem 1 (new half stencils).** Every half in
(2) whose retained local variables contain a selected state is positive
on (4). There are exactly 78 new edge products: 10 with a selected
neighbor and no neighbor-height derivative, four with selected center
and an unselected neighbor but no neighbor-height derivative, 48 with
selected center and a neighbor-height derivative, and 16 with only the
released outer coordinate selected. The other halves are precisely the
wholly unselected hypotheses from the
[minimum-level half-stencil theorem](research_mixed_minimum_level_half_stencils.md),
restricted to the smaller interval for \(t\).

## 3. What the saved-cover checker proves

Each new domain is parametrized by \([0,1]^5\), for \(t\), neighbor
real part, released outer edge, and the two unselected height
coefficients. Selected coefficients are replaced by zero only in the
derivative terms; their target imaginary parts are always \(H\).
Inactive parameters cause no loss of coverage.

At each cell midpoint a rational complex Newton witness encloses the
root of the original logarithmic equation. A rational affine predictor
and a complex-disk remainder verify a self-map over the entire cell;
the enclosing coordinate square is used only for interval evaluation.
The midpoint root is separately enclosed. The selected cotangent
chamber and all three regular factorial real strips are checked.
The effective derivatives are computed by the exact Schur formula
\[
\begin{gathered}
 Q_{sa}=g''(s+a)+2\pi i,\qquad Q_{sb}=g''(s+b),\qquad Q_{ss}=Q''(s),\\
 \phi_{ab}=-Q_{sa}Q_{sb}/Q_{ss},\qquad
 \phi_{aa}=g''(s+a)-(1+\eta/2)g''(a)-Q_{sa}^2/Q_{ss},
\end{gathered}                                                    \tag{6}
\]
with the analogous \(bb\) entry and the original gradients.
Real first-order automatic differentiation retains the moving polygon
vertices, both height coefficients, and every gauge term.

A leaf is accepted only when its full mean-value lower bound or its
direct interval lower bound is positive. A monotonicity node discards
a parameter direction only after its derivative has one strict sign on
the **whole** cell, and retains the minimizing endpoint. Split nodes
partition a parameter interval into its two exact rational halves.
The complete recorded tree reconstructs the initial cube, checks every
root witness and monotonicity decision, and consumes every recorded
node exactly once. No floating optimizer or numerical minimum is an
acceptance test. The final record binds this proof, the checker, the
saved cover and every imported arithmetic file.

The complete cover has 78 domains, 817,218 accepted leaves,
1,637,584 visited nodes and 3,226 monotonicity reductions. The separate
[replayer](../experiments/replay_mixed_constant_selected_height_transport.py)
imports no author arithmetic. It uses the original sine-log root
identity, real-coordinate cotangent formulas and explicit derivatives
of every parameter map. For gradient values, exact rectangle extrema of
\(\log|1-Re^{-2\pi ix}|\) and its argument replace the author's direct
complex logarithm enclosure. The modulus extrema occur at the nearest
allowed radius to the largest cosine, or at radius endpoints for the
maximum. Argument extrema occur at radius/angle endpoints or at
\(\cos(2\pi x)=R<1\), with values \(\pm\arcsin R\). The strip
\(0<x<1\) has no branch crossing. Thus the independent implementation
retains the original phase lift and all five parameter derivatives.

The reproduction commands are

```sh
python3 experiments/certify_mixed_constant_selected_height_transport.py --precision 256 --input repro/results/research-mixed-constant-selected-height-transport.json --output /tmp/research-mixed-constant-selected-height-transport-review.json
python3 experiments/replay_mixed_constant_selected_height_transport.py --precision 320
```

## 4. Scope

The two gauges in (2) cancel, so the new inequalities and the wholly
unselected half-stencil theorem together imply \(D_i^S\ge0\) for all
local configurations with \(t\in[.12,.22]\). The independent released
sets include repeated cyclic variables, so this local conclusion also
applies to loops and two-vertex cycles; the global multiplicity argument
is the one in the minimum-level transport proposition.

This is a phase-derivative certificate. It supplies neither a new finite
source packet nor, by itself, a selected outer-integral bound. In
particular it does not treat the early height rise \((.10,.12)\),
right taper, or a full outer period. The enlarged positive source cap
and the exact selected graph/assembly are separate inputs.
