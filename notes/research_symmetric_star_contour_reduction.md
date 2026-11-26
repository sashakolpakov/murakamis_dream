# Reducing a symmetric star contour estimate to two variables

Research note, 2 November 2026. This is a conditional reduction of the
dimension of a contour certificate, together with a counterexample to
one proposed contour. It does not assert the required global bounds.

## 1. The shared filling variable

Put \(A(x,t)=b(x,t)+b(x,0)\) and
\(C_n(t)=in t^2/(4\pi)-it\), with the canonical factorial branches
specified in [the terminal phase proof](research_terminal_three_central_phase.md).
The degree-\(d\) joint phase and its two-variable counterpart are
\[
 \mathcal F(\mathbf x,t)=\sum_{j=1}^d A(x_j,t)+C_n(t),
 \qquad \Phi_{d,n}(x,t)=dA(x,t)+C_n(t).
\]
They satisfy the exact averaging identity
\[
 \mathcal F(\mathbf x,t)=\frac1d\sum_{j=1}^d\Phi_{d,n}(x_j,t).
 \tag{1}
\]
If wire piece \(j\) has an exponential kernel penalty \(p_j\), then
\[
 \Re\mathcal F-\sum_jp_j
 =\frac1d\sum_j\bigl(\Re\Phi_{d,n}(x_j,t)-d\,p_j\bigr).
 \tag{2}
\]
Thus a lower-wire penalty \(2\pi h\) must be multiplied by \(d\)
in the corresponding two-variable certificate. If every such quantity
is at most \(M_{d,n}\), and one is at most \(M_{d,n}-\delta\),
the joint rate is at most \(M_{d,n}-\delta/d\). This is a strict
gap for each fixed degree.

The angle \(t\) and its contour height are shared by all wires.
An angular endpoint current or an extra angular Fourier penalty is
counted once, in the shared phase or outside (2). It must not be
multiplied by the number of wires. All product pieces on an angular
current must use the same angular height parameter.

## 2. The local Hessian

At the symmetric selected point, set
\(a=\Re A_{xx}\), \(b=\Re A_{xt}\), \(c=\Re A_{tt}\).
The chirp has purely imaginary second derivative on real directions.
The real Hessians of the two-variable and full phases are respectively
\[
 \begin{pmatrix}da&db\\db&dc\end{pmatrix},
 \qquad
 \begin{pmatrix}aI_d&b\mathbf1\\b\mathbf1^{\mathsf T}&dc\end{pmatrix}.
\]
By the Schur-complement criterion, both are negative definite exactly
when \(a<0\) and \(dc-db^2/a<0\). Uniform one-wire Hessian bounds
on a neighborhood therefore give the needed joint local bound.
Small complex free boundary angles can subsequently be admitted by
continuity after reducing that neighborhood and every strict gap.

## 3. The remaining hypotheses of a contour certificate

The [action-gap lemma](research_isolated_vertex_action_gap.md) proves
\(M_{d,n}>(d-1)M_\infty\) for every positive geometric integer pair
except \((2,\pm1),(3,0)\). It provides rational cutoffs near zero
and one half outside which the original wire terms, including high
wires and normal derivatives, have a strict gap. Common cutoffs can
be used for a finite collection of nonexceptional pairs.

The remaining task is to specify exact central wire and angular
deformations and prove all their two-variable inequalities. Equation
(2) then controls their finite products. Neither the strict action
gap nor the local Hessian proves those central inequalities.

## 4. A copied flat rectangle fails at degree two

At \(d=n=2\), the selected point is
\[
 x_*=\frac14+\frac{i\log3}{4\pi},\qquad
 t_*=\frac\pi2-i\log(2+\sqrt3).
\]
Put \(h_x=\Im x_*\), \(h_t=-\Im t_*\).
On the proposed flat contour at these heights, the point
\[
 x_0=\frac{21}{80}+ih_x,\qquad t_0=\frac{2\pi}{3}-ih_t
\]
satisfies
\[
 \Re\Phi_{2,2}(x_0,t_0)-\Re\Phi_{2,2}(x_*,t_*)>\frac1{100}.
 \tag{3}
\]
The bound by the selected action is therefore false on that rectangle.
Its excess is approximately \(0.01388572948\).

The rigorous ball-arithmetic calculation is reproduced by

    python3 experiments/audit_internal_flat_contour_obstruction.py

The script uses exact algebraic and logarithmic inputs at 160 bits,
retains both specified factorial branches, and proves the displayed
strict inequality. It does not infer a failure of the desired volume
limit. A wire contour following the varying complex wire critical
point, or a different exact source formula, can retain cancellation
that the flat contour loses.
