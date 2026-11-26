# Local derivatives for raising a common minimum

Research note, 4 November 2026. This note concerns the original unselected
phase on the minimum-neighbor contour. Finite-source estimates and selected
outer Fourier terms are separate inputs.

Write
\[
 \rho(t)=\frac{t-1/10}{3/25},\qquad 1/10\le t\le11/50,
 \quad I_3=[-.03,.02],\quad I_4=[-.057,-.02],\quad \kappa=3/2.
 \tag{1}
\]
The original allocated block phase is
\[
 \phi_{\eta\epsilon}(a,b)=Q_\epsilon(s_*(a,b);a,b)
 -(1+\eta/2)g(a)-(1+\epsilon/2)g(b),\qquad \eta,\epsilon\in\{0,1\}.
 \tag{2}
\]
Here
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad
 Q_\epsilon(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias.
\]
Types three and four correspond to indicators zero and one. All roots and
logarithms are the original zero-lift branches. The [global cotangent theorem](research_mixed_global_cotangent_roots.md)
and the [minimum-neighbor polygon bounds](research_mixed_minimum_neighbor_contour.md) supply their holomorphy before the
inequalities below are considered.

## 1. The finite family of local inequalities

Take type indicators \(o,n,c\in\{0,1\}\), a minimum \(t\in[.1,.22]\), a neighboring
real coordinate \(x\in[t,.45]\), and \(h_c\in I_{3+c},h_n\in I_{3+n}\).
Set
\[
 z_c=t+i\rho(t)h_c,\qquad z_n=x+i\rho(t)h_n.
 \tag{3}
\]
The outer coordinate lies in \(\Omega_{3+o}(t)\), where
\[
 \begin{split}
 \Omega_3(t)&=\operatorname{conv}\{t-.03i\rho(t),\ .22-.03i,
 .45-.03i,\ .45+.02i,\ .22+.02i,\ t+.02i\rho(t)\},\\
 \Omega_4(t)&=\operatorname{conv}\{t-.057i\rho(t),\ .22-.057i,
 .45-.057i,\ .45-.02i\rho(t),\ t-.02i\rho(t)\}.
 \end{split}\tag{4}
\]
For switches \(\chi,\xi\in\{0,1\}\), put
\[
 \begin{split}
 L_{\chi\xi}={}&\Re\left[(1+i\chi h_c/.12)
  \{\partial_2\phi_{nc}(z_n,z_c)+i\kappa\}
  +i\xi h_n/.12\{\partial_2\phi_{on}(z_o,z_n)
                    +\partial_1\phi_{nc}(z_n,z_c)\}\right],\\
 R_{\chi\xi}={}&\Re\left[(1+i\chi h_c/.12)
  \{\partial_1\phi_{cn}(z_c,z_n)-i\kappa\}
  +i\xi h_n/.12\{\partial_2\phi_{cn}(z_c,z_n)
                    +\partial_1\phi_{no}(z_n,z_o)\}\right].
 \end{split}\tag{5}
\]
Subscripts on \(\phi\) denote the type indicators.

**Theorem 1.** Both expressions in (5) are nonnegative throughout
(1)--(4), for every type and switch choice.

For fixed \(t,x,h_c,h_n\), (5) is harmonic in \(z_o\). Thus it is
enough to check every polygon edge. When \(\xi=0\), the outer variable
and its type disappear entirely. This leaves 16 inner cases and
\(16(6+5)=176\) edge cases, or 192 domains in total. Each edge case
has the five real parameters
\[
 t=.1+.12v_0,\quad x=t+(.45-t)v_1,\quad
 z_o=(1-v_2)w_j(t)+v_2w_{j+1}(t),\quad
 h_c=\inf I_{3+c}+|I_{3+c}|v_3,\quad h_n=\inf I_{3+n}+|I_{3+n}|v_4,
 \quad v\in[0,1]^5.
 \tag{6}
\]
Degenerate edges at \(t=.22\) are retained. The inner cases are independent
of \(v_2\).

## 2. Why this family includes every minimum-neighbor configuration

Suppose position \(i\) is a global minimum \(t\le.22\). Its two
neighbors have height exactly \(\rho(t)h_j\). An outer position
\(i\pm2\) has real part \(y\in[t,.45]\), and its minimum-neighbor
height fraction lies in \([\rho(t),\rho(y)]\). For type three this
implies
\(-.03\rho(y)\le\Im z_o\le.02\rho(y)\). For type four it gives
\(-.057\rho(y)\le\Im z_o\le-.02\rho(t)\). These are precisely
the polygon inclusions (4). Discarding any further restriction imposed
by the adjacent neighbor enlarges the domain safely.

Let \(G_j=\partial_2\phi_{j-1}+\partial_1\phi_j\) be the original
cyclic gradient, retaining both incidences. Define
\[
 D_i=\Re G_i+\sum_{j\in(i-1,i,i+1)}
               \min\{-h_j\Im G_j/.12,0\},
 \tag{7}
\]
where the three positions are counted with multiplicity. For a fixed
center switch, minimizing the left and right expressions in (5) over
independent neighbor switches gives their negative neighbor costs.
The opposite imaginary constants cancel. Therefore
\[
 D_i=\min_{\chi,\xi_L,\xi_R\in\{0,1\}}
       \{L_{\chi\xi_L}+R_{\chi\xi_R}\}.
 \tag{8}
\]
The center height and center switch must agree in the two summands.
Uniform nonnegativity of each half is sufficient even though its
independent verification allows a larger parameter set.

For one- and two-vertex cycles the repeated target coordinates satisfy
additional equalities inside (3)--(4). The two block derivatives in each
\(G_j\) remain present. Equation (8) still counts exactly the three
height costs in (7), including their repeated occurrences. Thus no
lower bound depending on word length is introduced.

## 3. Outward verification of the local functions

Put \(E=(Q_{sa},Q_{sb})\) and \(q=Q_{ss}\). The derivatives used
in (5) and in its real-parameter mean-value bound are
\[
 \begin{split}
 \phi_a&=g'(s+a)+2\pi i s-(1+\eta/2)g'(a),\\
 \phi_b&=g'(s+b)-(1+\epsilon/2)g'(b),\\
 \phi''&=\operatorname{diag}\bigl(g''(s+a)-(1+\eta/2)g''(a),
     g''(s+b)-(1+\epsilon/2)g''(b)\bigr)-E^TE/q.
 \end{split}\tag{9}
\]
Every root enclosure is obtained from a rational affine approximation
and an original-logarithm Newton self-map. Its cotangent lies in the
selected strict strip. A separate midpoint self-map supplies the value
at the exact parameter midpoint. The affine centers, responses and
rational radii are retained as witnesses.

For a parameter box \(B\), interval automatic differentiation of the
literal polynomial map (6), followed by (9), encloses every partial
derivative of the real function \(f=L_{\chi\xi}\) or \(R_{\chi\xi}\).
If \(v_0\) is its midpoint and \(r_j\) its half-widths, the checker
uses the rigorous lower bound
\[
 f(v)\ge f(v_0)-\sum_j r_j\sup_B|\partial_j f|.
 \tag{10}
\]
A direct interval evaluation is an additional independent enclosure.
If one partial derivative has a strict sign on the whole box, its
minimum is instead bounded by the corresponding endpoint face. Such
a reduction is accepted only with its full-box root witnesses and
derivative sign; it is not inferred from sampled values.

The independent replay reconstructs (6) with explicit derivatives and uses
\(g'(z)=\log(2\sin\pi z)+i\pi(1/2-z)\) in its original root
self-maps. For gradient values it can enclose the exact scalar extrema on
the argument rectangle. If \(R=e^{2\pi\Im z}\) and
\(\theta=2\pi\Re z\), then
\[
 |1-Re^{-i\theta}|^2=1+R^2-2R\cos\theta,\qquad
 \partial_R\Arg(1-Re^{-i\theta})=
       \frac{\sin\theta}{1+R^2-2R\cos\theta},\qquad
 \partial_\theta\Arg(1-Re^{-i\theta})=
       \frac{R(\cos\theta-R)}{1+R^2-2R\cos\theta}.
 \tag{11}
\]
The modulus is minimized by the largest allowed cosine and the radius
nearest that cosine; its maximum is at a radius endpoint and the smallest
cosine. Argument extrema occur at radius endpoints and either angle
endpoints or \(\cos\theta=R<1\), whose argument is
\(\pm\arcsin R\). The strip \(0<\Re z<1\) contains no logarithmic
branch crossing in these calculations. These are finite interval extrema,
not sampled values.

Every domain is exhausted by an exact tree. A split has its two closed
rational midpoint children; a monotonic node has the certified minimizing
face; a leaf has a strictly positive outward lower bound. A replay must
consume precisely the complete tree from its full unit cube, with no
missing child, extra node, floating root proposal or numerical optimizer.
Consequently a passed complete record proves the stated nonnegativity.

The finite family has 192 complete trees, with 3,415,762 accepted leaves
and 6,854,206 visited nodes. The
[author checker](../experiments/certify_mixed_minimum_level_half_stencils.py)
and [independent replay](../experiments/replay_mixed_minimum_level_half_stencils.py)
retain every rational affine root witness. Identical witnesses may be
stored once in a per-domain pool; tree indices reference the unchanged
exact rational data. The numerical acceptance and coverage checks do not
depend on this storage convention.

The canonical commands are

```sh
python3 experiments/certify_mixed_minimum_level_half_stencils.py --precision 256 --jobs 4 --input repro/results/research-mixed-minimum-level-half-stencils.json --output /tmp/research-mixed-minimum-level-half-stencils-review.json
python3 experiments/replay_mixed_minimum_level_half_stencils.py --precision 320 --jobs 4
```

**Corollary 2.** For every finite cyclic word in types three and four,
the original unselected minimum-neighbor contour satisfies \(D_i\ge0\)
at every global minimum in \([.1,.22]\), with repeated incidences counted
as in (7).

Indeed, (8) and Theorem 1 apply to every such configuration. The
[minimum-level transport implication](research_mixed_minimum_level_transport.md)
therefore gives its uniform unselected phase loss on the left transition
region. Its finite-source corollary uses the separately proved complete
polygon packet, retaining the original central coefficient and the stated
off-plateau gap. This conclusion does not control selected heights,
right-region mixtures, or ordinary boundary parameters.
