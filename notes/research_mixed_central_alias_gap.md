# Every nonempty alias is smaller on the whole central outer box

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This proves an absolute upper bound for every nonempty wrapped term
throughout the full central real product region. Both the conditional
inner saddles and all outer real coordinates are allowed to readjust.
The original polynomial Fourier weights are retained, including their
forcing branch near the right edge. The remaining outer complement
outside this product region is not estimated here.

## 1. The complete conditional phase

Use the four independent products \(B_3,B_4\) in
[the central conditional-source theorem](research_mixed_central_conditional_rectangles.md):
\[
 B_3=[.25,.40]+i[-.030,.020],\qquad
 B_4=[.25,.40]+i[-.057,.0141].
 \tag{1}
\]
Their original conditional root \(s=s_\epsilon(a,b)\) is
holomorphic on a neighborhood of the whole products. Define
\[
 \Phi_\epsilon(a,b)
   =Q_\epsilon(s_\epsilon(a,b);a,b)-g(a)-(1+\epsilon)g(b).
 \tag{2}
\]
The four ordered families are \((0,3,3),(0,4,3),(1,3,4),(1,4,4)\).
The extra \(-\epsilon g(b)\) in (2) accounts for the reciprocal
factorial belonging to a four-type outer variable. Thus for a cyclic
word, with indices understood modulo its length,
\[
             \Psi(\mathbf t)
       =\sum_v\Phi_{\epsilon_v}(t_{v-1},t_v)
 \tag{3}
\]
is exactly the critical action after summing all inner conditional
indices. This retains the absolute phase of the original contracted
source; no new calibration constant or scalar is inserted.

The complete source packets give (3) with a nonzero holomorphic
symbol. The remaining factors in each exact wrapped density are
the original level powers and carriers, together with
\(\widehat P_N(Nt)d_N(e^{-2\pi it})\) at each four-variable and
\(e^{2\pi iNt}\) at each wrapped variable. These factors are not
replaced by an assumed small interpolation error.

## 2. A quadratic inequality that includes real optimization

Let \(H=\Phi_\epsilon''\) and set
\[
 A=-\Re H,\qquad B=\Im H,\qquad K=A+BA^{-1}B.
 \tag{4}
\]
These are real symmetric two-by-two matrices. The following bound
is on the whole products (1), not only at an actual geometric pair.

**Lemma 1.** For every real \(u=(u_a,u_b)\) and every real
\(v=(v_a,v_b)\) with nonnegative components, imposing
\(v_a=0\) when the left type is three and \(v_b=0\) when the
own type is three, one has
\[
 \Re\bigl[(u+iv)^TH(u+iv)\bigr]
                 \le 10v_a^2+15v_b^2.
 \tag{5}
\]
The zero components in this formula are essential: only four-type
outer variables are shifted upward.

*Proof.* First consider the distinguished boundary of each parameter
product. Its 64 pieces are covered by exact dyadic two-parameter
cells. The outward certificate proves \(A>0\) on every cell and
the applicable bounds
\[
 K_{aa}<10\quad\hbox{if the left type is four},\qquad
 K_{bb}<15\quad\hbox{if the own type is four},\qquad
 K_{ab}<0\quad\hbox{in the four--four family}.
 \tag{6}
\]
The Hessian is computed directly from the original conditional
root, using its Schur complement. Specifically, with
\[
 p=g''(s+a),\ q=g''(s+b),\ d=p+q-(2+\epsilon)g''(s),
 \quad U=p+2\pi i,\ V=q,
\]
its entries are
\[
 H_{aa}=p-g''(a)-U^2/d,\qquad
 H_{bb}=q-(1+\epsilon)g''(b)-V^2/d,\qquad
 H_{ab}=-UV/d.
 \tag{7}
\]
Rational affine Newton witnesses verify the original zero logarithmic
lift on every parameter cell. The inverse in (4) is evaluated by
the exact two-by-two determinant formula, with strict positivity
checked before division.

Completing the real quadratic gives
\[
 \begin{split}
 \Re[(u+iv)^TH(u+iv)]
 &=-u^TAu-2u^TBv+v^TAv\\
 &\le v^T(A+BA^{-1}B)v.
 \end{split}
 \tag{8}
\]
Bounds (6) imply (5) on the distinguished boundary. When both
components of \(v\) can be nonzero, the cross term is nonpositive.
When neither can be nonzero, positivity of \(A\) suffices.

For each fixed real pair \((u,v)\), the left side of (5) is the
real part of a holomorphic function of \((a,b)\). Successive
harmonic maximum principles therefore extend (5) from the
distinguished boundary to the entire product. This argument does
not assert that the nonlinear matrix \(K\) itself is harmonic.
It applies for every fixed \((u,v)\), which proves the full
quantified inequality. \(\square\)

## 3. Arbitrary real displacements on the central box

Let \(\mathbf t^*\) be the outer coordinates of the original
cyclic critical point and put \(M=\Re\Psi(\mathbf t^*)\).
The original logarithmic equations give
\(\Psi'(\mathbf t^*)=0\). Choose a nonempty subset \(S\) of
four-type outer variables and set \(h=7/500\). For \(v\in S\),
write \(t_v^*=x_v^*-iH_v\), where \(.001<H_v<.057\), and put
\[
 \delta_v=H_v+h<.071\quad(v\in S),\qquad
 \delta_v=0\quad(v\notin S).
 \tag{9}
\]
For any independent real coordinates \(x_v\in[.25,.40]\),
let \(u_v=x_v-x_v^*\) and
\(\mathbf t=\mathbf t^*+\mathbf u+i\boldsymbol\delta\).
The full straight segment between these points lies in the typed
products (1), by the proved actual critical-height bounds.

Apply (5) to each conditional factor along that segment. Every
shifted coordinate appears once as a left parameter and once as
an own parameter. Taylor's integral remainder and stationarity give
\[
 \begin{split}
 \Re\Psi(\mathbf t)-M
 &=\int_0^1(1-r)
    \Re[(\mathbf u+i\boldsymbol\delta)^T
       \Psi''(\mathbf t^*+r(\mathbf u+i\boldsymbol\delta))
       (\mathbf u+i\boldsymbol\delta)]\,dr\\
 &\le \frac{25}{2}\sum_{v\in S}\delta_v^2
 <\frac{25}{2}(.071)^2|S|.
 \end{split}
 \tag{10}
\]
This already maximizes over every possible real displacement. It
does not assume that the shifted maximum remains near the old
critical real coordinates. Repeated incidences at cyclic lengths
one and two are counted by the same two occurrences per variable.

## 4. The actual Fourier weights leave a uniform gap

Put \(\nu(z)=-\Re g(z)\). At the positive height \(h\),
\[
 \partial_x\nu(x+ih)
       =-\log|1-e^{2\pi h-2\pi ix}|<0
                         \qquad(.25\le x\le.40),
 \tag{11}
\]
because the cosine in the squared modulus is nonpositive. The
minimum is therefore at \(x=.40\). The outward scalar checks give
\[
 \nu(.40+.014i)>.0721,\qquad 2\pi h>.0721.
 \tag{12}
\]
The whole-strip bound from
[the exact Fourier-weight theorem](research_mixed_fourier_weight_continuation.md)
now gives each wrapped factor the rate
\[
 -\min\{\nu(x+ih),2\pi h\}+\eta
                         \le -.0721+\eta.
 \tag{13}
\]
In particular the forcing branch near \(x=.40\) has been retained.
For unwrapped four-variables the height is negative and the real
coordinate belongs to \([.25,.40]\). The same theorem gives the
uniform relative reciprocal-factorial expansion there, since
\(\nu>0\) on that compact lower strip. Those factors incur no
exponential cost.

Take \(\eta=1/1000\). The remaining margin is the exact rational
comparison
\[
 .0721-\frac{25}{2}(.071)^2-\frac1{1000}-\frac1{125}
                         =\frac7{80000}>0.
 \tag{14}
\]
Consequently, for every fixed cyclic word and every nonempty wrapped
subset, the **complete original conditional density** throughout
the whole central real product box obeys
\[
       |\mathcal D_{S,N}(\mathbf t)|
          \le \operatorname{poly}(N)e^{N(M-|S|/125)}.
 \tag{15}
\]
All conditional sums, their finite tails, original scalars, and true
Fourier polynomials are included. Integrating its absolute value over
that central product box preserves (15). The finitely many wrapped
subsets for a fixed word may therefore be summed with the same
strict exponential conclusion.

This disposes of the entire **central** part of each nonempty alias.
It leaves the exact outer complements, where at least one real
coordinate exits \([.25,.40]\), unchanged as the remaining problem.
It asserts no mixed-word knot-volume theorem.

## 5. Reproduction

    python3 experiments/certify_mixed_central_alias_gap.py

The record retains the complete 64-piece dyadic cover, rational
conditional-root witnesses, every matrix comparison in (6), and
the scalar comparisons (12)--(14). The all-parameter harmonic
extension and exact Taylor identity are written proofs, not
conclusions inferred from sampled words.
