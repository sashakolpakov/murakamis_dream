# The actual contribution near a mixed cyclic critical point

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The complete conditional sums now have proved asymptotics near every
mixed cyclic critical configuration. Consequently one can integrate
the original finite source on a small part of its outer torus and
prove that this part has a nonzero leading coefficient. This note
records that contribution, including its normalization, and defines
the complementary integrals that a global theorem must still bound.

No arbitrary cyclic matrix word is identified here with a knot
complement. The full cyclic asymptotic, and its use in an original
open knot source, remain separate assertions.

## 1. The original finite integral

Fix a word of length \(m\ge1\), with entries \(3+\epsilon_v\),
where \(\epsilon_v\in\{0,1\}\); put \(k=\sum_v\epsilon_v\).
All indices below are cyclic. Let \(A_n=JM^n\) be the original
Newton matrices, and let \(\kappa\) be their original unit scalar.

Use the exact Laurent kernels and interpolation polynomial
\[
 \begin{split}
 C_{\epsilon,N}(X,Y)
   &=\sum_{j=0}^{N-1}
       \frac{X^{-j}(rX;r)_j(rY;r)_j}{P_j^{2+\epsilon}},\\
 r&=e^{-2\pi i/N},\qquad P_j=(r;r)_j,\qquad
 d_N(r^a)=P_a^{-1}\quad(0\le a<N),\quad\deg d_N<N.
 \end{split}
 \tag{1}
\]
Here \((z;r)_j=\prod_{h=0}^{j-1}(1-zr^h)\).
For the outer logarithmic variables \(t_v\), write
\(X_v=e^{-2\pi i t_v}\). A convenient cyclic indexing of the
exact torus identity is
\[
 \operatorname{tr}(A_{3+\epsilon_1}\cdots A_{3+\epsilon_m})
  =\sum_{S\subseteq E_4} I_{S,N},\qquad
                    E_4=\{v:\epsilon_v=1\},
 \tag{2}
\]
where
\[
 \begin{split}
 I_{S,N}
  &=\int_{[0,1]^m+i\mathbf y} f_{S,N}(\mathbf t)\,d\mathbf t,\\
 f_{S,N}
  &=\kappa^{m+k}N^{m+k}
    \prod_v C_{\epsilon_v,N}(X_{v-1},X_v)
    \prod_{v\in E_4}d_N(X_v)
    \prod_{v\in S}e^{2\pi iNt_v}.
 \end{split}
 \tag{3}
\]
Each height \(y_v\) is arbitrary, independently for each integral.
The integrands are entire periodic functions of the logarithmic
variables. All shifts in (3) are therefore exact deformations of
complete periods. The apparent reversal of circle orientation under
\(X=e^{-2\pi it}\) is canceled by \(dX/(2\pi iX)=-dt\).

The only additional terms are the subsets in (2); there is one
possible extra frequency \(N\) at each four-type variable. Equation
(2) is the [exact torus-composition theorem](research_mixed_conditional_torus_composition.md),
with its original scalar and all finite summands retained.

## 2. Phase, coefficient and the inner sums

Put
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad L(z)=\sqrt{2\sin\pi z}.
\]
Use the branches on \(0<\Re z<1\) from the original factorial
interpolation. The full contracted phase is
\[
 \mathcal F(\mathbf s,\mathbf t)
 =\sum_v\{g(s_v+t_v)+g(t_v+s_{v+1})
 -(2+\epsilon_v)[g(s_v)+g(t_v)]+2\pi i t_vs_{v+1}\}.
 \tag{4}
\]
Its coefficient is
\[
 a(\mathbf s,\mathbf t)=
 e^{(i\pi/2)\sum_v\epsilon_v(s_v+t_v)}
 \frac{\prod_v L(s_v+t_v)L(t_v+s_{v+1})}
      {\prod_v[L(s_v)L(t_v)]^{2+\epsilon_v}} .
 \tag{5}
\]
These are the phase and coefficient of the
[original contracted summand](research_mixed_contracted_phase.md).
In particular (4) has the same absolute phase constant.

Let \(z_*=(\mathbf s^*,\mathbf t^*)\) be the unique original
critical point in the common region from the
[cyclic localization theorem](research_mixed_cyclic_critical_localization.md).
It satisfies
\[
 H_*=-\mathcal F''(z_*),\qquad \Re H_*\succ(\pi/4)I_{2m}.
 \tag{6}
\]
The matrix is complex symmetric. In (6), \(\Re H_*\) is also
its Hermitian real part.

For each outer parameter near \(\mathbf t^*\), solve the
independent inner equations
\[
 Q_{\epsilon_v,s}(s_v;t_{v-1},t_v)=0,\qquad
 Q_\epsilon(s;\alpha,\beta)
   =g(s+\alpha)+g(s+\beta)-(2+\epsilon)g(s)+2\pi i\alpha s.
 \tag{7}
\]
The [complete conditional-sum theorem](research_mixed_conditional_critical_images.md)
supplies nonzero asymptotics on open neighborhoods of precisely these
independent neighbor pairs. Its local inverse-function argument is
essential: knowledge of values only on a correlated parameter set
would not suffice here.

Write the resulting inner branch as \(\mathbf s(\mathbf t)\), and
define
\[
 \Phi(\mathbf t)=\mathcal F(\mathbf s(\mathbf t),\mathbf t).
\]
Let \(H_{ss}(\mathbf t)=-\mathcal F_{ss}(\mathbf s(\mathbf t),\mathbf t)\);
this matrix is diagonal. On a fixed neighborhood of \(\mathbf t^*\),
the exact integrand of the empty subset has the expansion
\[
 f_{\varnothing,N}(\mathbf t)
  =\kappa^{m+k}N^{m/2}(2\pi)^{m/2}
    \frac{a(\mathbf s(\mathbf t),\mathbf t)}
         {\sqrt{\det H_{ss}(\mathbf t)}}
    e^{N\Phi(\mathbf t)}(1+O(N^{-1})).
 \tag{8}
\]
The normalized error is holomorphic, with all fixed derivatives on
smaller neighborhoods.

Here is the normalization directly. A conditional factor has power
\(N^{(1-\epsilon_v)/2}\). Passing from that factor to \(C_{\epsilon_v,N}\)
divides by two marked factorials, giving power
\(N^{-(1+\epsilon_v)/2}\). Each of the \(k\) outer Fourier weights
has power \(N^{-1/2}\). Combining these with the original
\(N^{m+k}\) in (3) leaves \(N^{m/2}\).
The corresponding \(m\) inner Gaussian coefficients give
\((2\pi)^{m/2}/\sqrt{\det H_{ss}}\); the remaining factors are
exactly (5). At every four-type outer critical coordinate the
[Fourier-weight comparison](research_mixed_fourier_weight_continuation.md)
has exponentially small relative error. It therefore preserves (8).

## 3. A nonzero local contribution of the actual finite source

Let \(x_*=\Re\mathbf t^*\) and \(y_*=\Im\mathbf t^*\).
For sufficiently small fixed \(\rho>0\), define
\[
 B_\rho=\{\mathbf x:|x_v-x_v^*|\le\rho\text{ for every }v\},\qquad
 I^{\mathrm{loc}}_{\varnothing,N}
 =\int_{B_\rho+i y_*}f_{\varnothing,N}(\mathbf t)\,d\mathbf t .
 \tag{9}
\]
The box is interpreted modulo one in each outer coordinate.

**Theorem 1.** For every fixed word there is such a \(\rho>0\)
for which
\[
 I^{\mathrm{loc}}_{\varnothing,N}
 =\kappa^{m+k}
   \frac{(2\pi)^m a(z_*)}{\sqrt{\det H_*}}\,
     e^{N\mathcal F(z_*)}(1+O(N^{-1})).
 \tag{10}
\]
The coefficient multiplying the unit scalar is nonzero. The result
holds along both level parities. It concerns the original finite
conditional sums, not merely their formal local symbols.

*Proof.* Shrink the outer neighborhood so that the full inner branch
stays in the common accretive chamber. The effective negative Hessian
is the Schur complement
\[
 H_{\mathrm{eff}}
     =H_{tt}-H_{ts}H_{ss}^{-1}H_{st}.
 \tag{11}
\]
It has Hermitian real part at least \((\pi/4)I_m\). Indeed, for any
complex vector \(v\), put \(w=-H_{ss}^{-1}H_{st}v\). Then
\[
 \Re(v^*H_{\mathrm{eff}}v)
 =\Re\bigl((w,v)^*H(w,v)\bigr)
 \ge(\pi/4)(\|w\|^2+\|v\|^2).
\]
The full first derivatives vanish at \(z_*\), so
\(\Phi'(\mathbf t^*)=0\). Integrating (11) on the horizontal box
gives a strict quadratic maximum at that point. Its boundary has
a fixed strict loss.

Insert the actual asymptotic (8) into (9) and apply Gaussian
stationary phase on this horizontal box. The outer Gaussian has
power \(N^{-m/2}\) and coefficient
\((2\pi)^{m/2}/\sqrt{\det H_{\mathrm{eff}}}\).
It cancels the power of \(N\) in (8). The determinant identity
\[
                 \det H_*=\det H_{ss}\det H_{\mathrm{eff}}
\]
gives (10). The square roots are the Gaussian branches, obtained
by continuous continuation from positive real symmetric matrices
in the convex space of symmetric matrices with positive Hermitian
real part. Equivalently, iterated Gaussian integration fixes them;
no independent principal square root of a high-dimensional
determinant is substituted. This also fixes the sign in (10).

The odd first Gaussian correction integrates to zero on the
symmetric box; the remaining error is \(O(N^{-1})\), with
exponentially small boundary terms. Every sine factor in (5) is
nonzero, and (6) makes its Gaussian determinant nonzero. This
proves the claimed nonvanishing. \(\square\)

## 4. The exact remaining outer integrals

Choose any permitted height vector \(\mathbf y^{(S)}\) for each
subset in (2), using \(y_*\) for the empty subset. Split each
complete period after that exact deformation into a small box
\(B_\rho+i\mathbf y^{(S)}\) and its complement in the period.
Let \(I^{\mathrm{loc}}_{S,N}\) and \(R_{S,N}\) be those integrals.
Then, exactly,
\[
 \operatorname{tr}(A_{3+\epsilon_1}\cdots A_{3+\epsilon_m})
 = I^{\mathrm{loc}}_{\varnothing,N}
   +\sum_{\varnothing\ne S\subseteq E_4} I^{\mathrm{loc}}_{S,N}
   +\sum_{S\subseteq E_4}R_{S,N}.
 \tag{12}
\]
There are no omitted joining currents: a complete Laurent period
is deformed before it is split.

For a nonempty subset, choose \(\mathbf y^{(S)}\) by moving
precisely its four-type variables to height \(7/500\), leaving
the other heights at \(y_*\). The
[reoptimized action estimate](research_mixed_reoptimized_alias_action.md)
and the [complete shifted conditional packets](research_mixed_shifted_conditional_packets.md)
then give, for every fixed word, a common sufficiently small
choice of \(\rho\) such that
\[
 |I^{\mathrm{loc}}_{S,N}|
 \le C N^C
       \exp\{N[\Re\mathcal F(z_*)-|S|/250]\}
                    \qquad(\varnothing\ne S\subseteq E_4).
 \tag{13}
\]
Indeed the shifted source theorem bounds the exact outer density
on a small real neighborhood of its specified center. Integrating
over a fixed box costs only a constant. There are finitely many
subsets for the fixed word, so their neighborhoods and the one
in Theorem 1 have a common positive radius. This step uses the
complete finite conditional sums at the shifted parameters,
including their revived rows and contour currents.

Define \(R_N=\sum_{S\subseteq E_4}R_{S,N}\) and
\[
 B_*=\frac{(2\pi)^m a(z_*)}{\sqrt{\det H_*}}\ne0,
 \qquad M_*=\Re\mathcal F(z_*).
\]
Equations (10)--(13) prove the precise reduction
\[
 \operatorname{tr}(A_{3+\epsilon_1}\cdots A_{3+\epsilon_m})
  =\kappa^{m+k}B_*e^{N\mathcal F(z_*)}(1+O(N^{-1}))
       +R_N+O(N^C e^{N(M_*-1/250)}).
 \tag{14}
\]
If \(E_4\) is empty, the last error term is absent.
All terms in \(R_N\) are explicit complementary integrals of
the original Laurent functions on the heights just specified.
A sufficient remaining estimate for the full cyclic asymptotic
is
\[
             \limsup_{N\to\infty}N^{-1}\log|R_N|<M_*.
 \tag{15}
\]
This estimate has not been proved. Nor does this note identify
an arbitrary cyclic matrix trace with a knot invariant.
The contribution (10) can still be canceled by the complementary
integrals until an adequate bound on \(R_N\) is established.

