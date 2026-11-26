# Ordinary boundary response at the open-word critical point

Research deduction, 5 November 2026. For every fixed open word in three
and four, the critical point extends to a holomorphic function of the
two ordinary boundary colors. Its stationary action has strictly
negative real angular curvature at the complete colors, with a bound
independent of word length. This is a statement about the original
stationary action. A nonzero asymptotic of the full finite open source
still requires its global contour estimate.

## 1. The original color-dependent action

Let \(z_*\) be the unique original critical point supplied by
[open-word localization](research_mixed_open_word_critical_localization.md).
Retain all \(2m+2\) variables of
[the Hessian lemma](research_mixed_open_word_hessian.md), including the
endpoint coordinates \(u_L,u_R\). Introduce angular boundary
parameters \(\theta_L,\theta_R\), with ordinary colors
\(w_L=-2\cos\theta_L\), \(w_R=-2\cos\theta_R\).

The actual complete endpoint polynomial contributes the phase from
[the full-index endpoint theorem](research_complete_boundary_full_index_interval.md),
equation (26). Thus replace each endpoint term \(B(e,u)\) by
\[
 B(e,u;\theta)=
 -J(1/2-u+\theta/(2\pi))-J(1/2-u-\theta/(2\pi))
 -3J(u)-J(e-u).                                            \tag{1}
\]
All other terms, including \(i\pi eu\), remain as in the original
action. Denote the resulting holomorphic function by
\(\mathcal F_m(z;\theta_L,\theta_R)\). Equation (1) fixes
its absolute additive constant; it is not just an equation for a
derivative or an exponentiated gluing relation.

Since \(-\mathcal F_{m,zz}(z_*;0,0)\) is invertible, the
holomorphic implicit-function theorem gives a unique critical branch
\(z=z(\theta_L,\theta_R)\) through \(z_*\) on a small bidisk.
Define its stationary action
\[
 \Psi_m(\theta_L,\theta_R)
   =\mathcal F_m(z(\theta_L,\theta_R);\theta_L,\theta_R).
                                                               \tag{2}
\]
Both the action and its critical branch are separately even in the
two angles. Indeed (1) is separately even, and local uniqueness
identifies the two critical branches after changing either sign.
They are consequently holomorphic in \(\theta_L^2,\theta_R^2\).
Since \(w+2=\theta^2+O(\theta^4)\), they descend holomorphically
to the actual ordinary colors near \((-2,-2)\).

## 2. The boundary Hessian has no stationary correction at zero

At \(\theta=0\), the first angular derivative of (1) vanishes
identically as a function of all internal variables. Therefore
\(\mathcal F_{m,z\theta_L}=\mathcal F_{m,z\theta_R}=0\)
at the complete colors. Differentiating the stationary equations
gives \(z_{\theta_L}=z_{\theta_R}=0\) there. The stationary
Schur correction to the angular Hessian in (2) is thus zero.

Direct differentiation of (1), using
\(J''(v)=\pi\cot\pi v\), gives
\[
 \Psi_{m,\theta_L\theta_L}(0,0)
       =-\frac{\tan(\pi u_L^*)}{2\pi},\qquad
 \Psi_{m,\theta_R\theta_R}(0,0)
       =-\frac{\tan(\pi u_R^*)}{2\pi},\qquad
 \Psi_{m,\theta_L\theta_R}(0,0)=0.                          \tag{3}
\]
These formulas include a word of length one. Its two endpoint
coordinates remain distinct variables before stationary elimination.

Localization puts each endpoint coordinate in
\(U=[.21,.25]+i[.01,.10]\). The scalar estimate in Section 3
of the Hessian lemma proves \(\Re\tan\pi u>3/5\) on this
whole rectangle. Hence
\[
        -\Re\Psi_m''(0,0)\succ\frac{3}{10\pi}I_2.         \tag{4}
\]
For every fixed word, shrinking the real angular neighborhood if
necessary gives the quantitative local loss
\[
 \Re\Psi_m(\theta_L,\theta_R)
 \le\Re\Psi_m(0,0)
          -\frac{3}{40\pi}(\theta_L^2+\theta_R^2).         \tag{5}
\]
For example, continuity of the real Hessian preserves half the
bound (4); Taylor's integral formula then proves (5).
The radius of that neighborhood may depend on the word.

In ordinary colors, if \(\widehat\Psi_m(w_L,w_R)=\Psi_m(\theta_L,\theta_R)\),
the first derivatives are
\[
 \widehat\Psi_{m,w_L}(-2,-2)
       =-\frac{\tan(\pi u_L^*)}{4\pi},\qquad
 \widehat\Psi_{m,w_R}(-2,-2)
       =-\frac{\tan(\pi u_R^*)}{4\pi}.                    \tag{6}
\]
The vanishing mixed angular derivative in (3) does not assert that
the mixed derivative in the ordinary colors vanishes.

Thus ordinary-color holomorphy and the required local angular
curvature follow for every word from the original endpoint phase
and the general critical-point theorem. To use this response in a
short-filling theorem, one must still prove that the full original
finite open source has a nonzero coefficient multiplying
\(e^{N\widehat\Psi_m}\), together with its whole-boundary bound.
Neither conclusion follows from (3)--(6) alone.
