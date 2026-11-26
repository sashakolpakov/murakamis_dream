# Boundary-color estimates for the central region of an open chain

Research deduction, 5 November 2026.

The central region, including the interior Fourier selections already
controlled, now has both a nonzero local asymptotic and a bound over the
whole real boundary-color interval. These imply the quadratic complex
boundary estimate used in the filling argument. The result is for a
specified part of the original integral. Replacing the whole source by
that part still requires a bound for its complement.

## 1. A polynomial defined by fixed integration regions

Fix a mixed word of length \(m\ge2\), and retain the notation of
[the interior-selection theorem](research_mixed_interior_selected_plateau.md).
Let \(Z_N^{\mathrm{int}}(w_L,w_R)\) be its original normalized
integral over \(P^{m-1}\), summed over precisely the selections
\(S\subseteq I_m\) allowed by the types, where
\[
 P=[.22,.45],\qquad I_m=\{6,\ldots,m-5\}.
 \tag{1}
\]
The set \(I_m\) is empty when its lower endpoint exceeds its
upper endpoint. The two ordinary boundary colors are \(w_L,w_R\).
For each selection the contour heights are fixed by the complete-color
critical point and by the prescribed selected height \(7/500\).
Neither the contour nor the integration domain moves with the colors.

The endpoint factors \(U_{\epsilon_1,N}\) and
\(V_{\epsilon_m,N}\) have ordinary degree less than \(N\).
All other factors and the original scalar are color independent.
Termwise integration of this finite polynomial therefore proves that
\(Z_N^{\mathrm{int}}\) is an entire polynomial, of degree at most
\(N-1\) in each ordinary color. This argument applies to a restricted
integration region as well as to a complete constant term.

Write its original critical action as
\(\mathcal W(w_L,w_R)\), and put
\[
 M=\Re\mathcal W(-2,-2),\qquad
 Q_N(\theta_L,\theta_R)=
 Z_N^{\mathrm{int}}(-2\cos\theta_L,-2\cos\theta_R).
 \tag{2}
\]
The original local asymptotic, including its normalization, is
\[
 Z_N^{\mathrm{int}}(w_L,w_R)
 =\kappa_N^{m+k_4}N^{-3/2}
 A(w_L,w_R)e^{N\mathcal W(w_L,w_R)}(1+O(N^{-1})),
 \qquad A(-2,-2)\ne0,
 \tag{3}
\]
on a fixed complex neighborhood of the complete colors. Both the
amplitude and action are the ones supplied by the unselected plateau
theorem; the interior-selection theorem adds an exponentially small
error there. Their original logarithmic and Gaussian branches are
unchanged, and \(|\kappa_N|=1\). Shrinking the neighborhood makes
\(A\) nonzero throughout it.

## 2. A real estimate on the entire boundary-color period

Put \(D(\theta)=1-\cos\theta\). The
[complete first-cap color estimate](research_mixed_endpoint_real_color_decay.md),
equation (14), and the
[complete terminal color estimate](research_mixed_terminal_real_color_decay.md),
equation (3), give positive constants \(c_L,c_R\) with upper rates
\[
 B_L(x_1)-c_LD(\theta_L),\qquad
 B_R(x_{m-1})-c_RD(\theta_R).
 \tag{4}
\]
Here \(B_L,B_R\) are their allocated complete-color supporting
planes, including their nonpositive quadratic terms. These estimates
hold for the entire exact endpoint factors and for independent real
arguments in \(P\) at their reference heights. Those heights are
unchanged for every selection included in \(Z_N^{\mathrm{int}}\).

An ordinary factor incident to a selected position has its calibrated
complex affine upper rate with loss \(1/200\). Every other ordinary
factor has its completed unselected supporting plane with any prescribed
positive tolerance. The kernels have no ordinary-color dependence.
As in the interior-selection proof, the full complex affine terms
cancel at the actual open critical point; no imaginary displacement
term is dropped.

Consequently, with \(c_0=\min(c_L,c_R)>0\), for every fixed
\(\tau>0\) the complete sum of these region integrals satisfies
\[
 |Q_N(\theta_L,\theta_R)|
 \le C_\tau N^{A_\tau}
 \exp N\{M+\tau-c_0[D(\theta_L)+D(\theta_R)]\},
 \quad (\theta_L,\theta_R)\in[-\pi,\pi]^2.
 \tag{5}
\]
The proof takes absolute values only after applying the complete
factor estimates. Their halfweights restore the original integer
weights exactly. The scalar, integration over a fixed bounded region,
and the finite number of selections change only the polynomial
prefactor. For nonempty selections their additional negative rate
may be discarded in (5). No positivity of the original integrand is
assumed.

The small tolerance in (5) cannot be set to zero without an argument.
It is enough to choose it once after fixing a neighborhood of the
complete colors. Specifically, for any fixed \(0<\rho<\pi\),
\[
 \max(|\theta_L|,|\theta_R|)\ge\rho
 \quad\Longrightarrow\quad
 D(\theta_L)+D(\theta_R)\ge1-\cos\rho.
 \tag{6}
\]
Choose \(\tau=c_0(1-\cos\rho)/2\). Then (5) gives a strict
calibrated gap
\[
 |Q_N(\theta_L,\theta_R)|
 \le C N^A e^{N(M-\delta_\rho)},
 \qquad \delta_\rho=\tfrac12c_0(1-\cos\rho)>0
 \tag{7}
\]
on the set in (6). The choice of tolerance is independent of \(N\).

## 3. The quadratic complex boundary bound

Define
\[
 W(\theta_L,\theta_R)
 =\mathcal W(-2\cos\theta_L,-2\cos\theta_R).
 \tag{8}
\]
It is separately even and holomorphic near zero. The actual endpoint
marginals, recorded in
[the stability reduction](research_mixed_open_source_stability_reduction.md),
equations (10)--(11), give
\[
 W''(0,0)=\operatorname{diag}
 \left(-\frac{\tan(\pi u_L)}{2\pi},
       -\frac{\tan(\pi u_R)}{2\pi}\right),
 \qquad -\Re W''(0,0)\succ0.
 \tag{9}
\]
Here \(u_L,u_R\) are the original auxiliary endpoint coordinates.
Their real parts lie strictly between zero and one half. The strict
sign follows directly from
\[
 \Re\tan(\pi u)=
 \frac{\sin(2\pi\Re u)}{\cos(2\pi\Re u)+\cosh(2\pi\Im u)}>0.
 \tag{10}
\]

**Theorem 1.** For every fixed mixed word there are constants
\(c,B,h>0\) and a polynomial prefactor such that
\[
 \begin{split}
 |Q_N(\mathbf x+i\mathbf y)|
 &\le C N^A\exp N\left\{
 M-c\sum_{j=L,R}(1-\cos x_j)+B\sum_{j=L,R}y_j^2\right\},\\
 &\hspace{18mm}\mathbf x\in[-\pi,\pi]^2,\quad |y_j|\le h.
 \end{split}
 \tag{11}
\]
It holds along the full sequence of sufficiently large integer levels,
including both parities. Its local holomorphic asymptotic remains
(3), with its original nonzero coefficient and fixed normalized
derivative estimates on smaller neighborhoods.

*Proof.* Choose \(\rho\) sufficiently small for (3) and the
strict local horizontal concavity following from (9). The polynomial
degree bound in Section 1, the local packet (3), and the real gap (7)
are precisely the three hypotheses of Lemma 1 in the stability
reduction. That lemma applies with two outside angles and proves (11).
It uses the degree bound to extend the real estimate to a thin complex
strip, and the local action to improve the linear imaginary-height
cost to a quadratic one near the complete colors. The two regions
overlap. This proves (11) without taking \(\tau\) to zero in (5),
and without continuing a local packet to distant real colors.
\(\square\)

## 4. What is still needed for the whole open source

Theorem 1 supplies both analytic boundary requirements for
\(Z_N^{\mathrm{int}}\). It does not supply them for the original
whole polynomial \(Z_N\). The difference includes every integration
region outside the plateau and every plateau selection meeting a
boundary position excluded by (1).

For example, the following two additional bounds would suffice to
transfer the result to the whole source. Near the complete ordinary
colors one needs
\[
 |Z_N-Z_N^{\mathrm{int}}|
 \le C N^A e^{N\{\Re\mathcal W(w_L,w_R)-\gamma\}},
 \qquad \gamma>0,
 \tag{12}
\]
on a fixed complex neighborhood. On the real outside-color period
away from a fixed small angular neighborhood of zero, one needs
\[
 |Z_N-Z_N^{\mathrm{int}}|
 \le C N^A e^{N(M-\gamma')},\qquad\gamma'>0.
 \tag{13}
\]
The constants may depend on the fixed word. Combining (12) with
(3) gives the whole local packet, and combining (13) with (7) gives
the whole real gap. The same stability lemma would then apply to
\(Z_N\). Neither (12) nor (13) is inferred from the estimates of
the retained region. The marked geometric boundary deformation and
arbitrary short partial fillings also remain separate requirements.
