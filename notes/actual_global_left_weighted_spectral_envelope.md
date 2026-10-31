# The global LEFT weighted spectral envelope

Independently reviewed theorem, 31 October 2026. This bounds the actual triangular-face LEFT sector at fixed positive face moduli. It is not a coefficientwise inequality or an optimized shared-capacity theorem. All original unused prefix and suffix rows are retained.

## 1. The original finite sector and its continuum upper envelope

Put $A=x+y>0$, $P=xy\geq0$, $d=N-1$, $m=\lfloor N/2\rfloor$, and

$$
\alpha_r(\delta)=4\cos^2\!\left(\frac{\pi(r+1/2)}N\right)-4\sin^2(\pi\delta),
\qquad s_j=2\sin(\pi j/N).
$$

The LEFT sector has $0\leq i\leq j\leq m-1$. Up to its recorded overall sign, its [exact start/end summand](actual_cross_cofactor_factorization.md) is

$$
A_{\mathrm{rest}}(\delta)b^ic^{d-j}
\left(\prod_{r<i}\alpha_r\right)
\left(\prod_{j<r<m}\alpha_r\right)K_{i,j},\tag{1}
$$

where $K_{i,i}=1$ and

$$
K_{i,j}=s_j^2AK_{i,j-1}+s_js_{j-1}\alpha_{j-1}PK_{i,j-2}.
$$

The omitted-half product $A_{\mathrm{rest}}$ is retained. For even $N$ it is $2T_m(\sigma/2)$, up to a sign, and has real-interval modulus at most $2$. For odd $N=2m+1$ it is $(\sigma+2)P_m(\sigma)$, up to a sign, with

$$
P_m(2\cos\theta)=\frac{\cos((m+1/2)\theta)}{\cos(\theta/2)}.
$$

The quotient is a finite alternating cosine sum, bounded by $N$ on the real interval. Thus $|A_{\mathrm{rest}}|\leq4N$ at odd levels, including its removable endpoint. These exact factors have zero exponential upper rate.

The uniform transfer estimate in the [global CROSS proof](actual_global_cross_spectral_gap.md) applies to $K_{i,j}$ with any interval endpoints, by the same fixed-block matrix power argument. Together with uniform upper Riemann bounds for both unused prefix and suffix, it gives the upper action

$$
F_L(\mu,\nu,\delta)
=\mu\log b+(1-\nu)\log c+\int_\mu^\nu\log L_\delta(t)\,dt,
\qquad0\leq\mu\leq\nu\leq\frac12,\tag{2}
$$

where

$$
\begin{aligned}
\alpha(t)&=4\bigl(\cos^2(\pi t)-\sin^2(\pi\delta)\bigr),\\
\Lambda(t)&=2\sin(\pi t)
\left[A\sin(\pi t)+\sqrt{(x-y)^2\sin^2(\pi t)+4P\cos^2(\pi\delta)}\right],\\
L_\delta(t)&=\frac{\Lambda(t)}{|\alpha(t)|}.
\end{aligned}
$$

This rewriting uses $\int_0^{1/2}\log|\alpha(t)|\,dt=0$ only after bounding the actual two outside products. It makes no finite division by $\alpha$ and includes sampled spectral zeros. Logarithmic singularities are uniformly integrable. The $O(1/N)$ endpoint shifts and at most $N^2$ start/end pairs cost $o(N)$, uniformly in endpoints and real $\delta$.

If $b=0$, only $\mu=0$ is allowed. If $c=0$, the finite LEFT polynomial vanishes identically because its $c$ exponent is at least $\lfloor N/2\rfloor>0$.

The sharp envelope identity is

$$
\sup_{\substack{\delta\in[0,1/2]\\0\leq\mu\leq\nu\leq1/2}}F_L(\mu,\nu,\delta)
=\max\left\{\log c,Q_b(0)+\frac12\log c\right\},\tag{3}
$$

for $c>0$ and $b\geq0$. Here $Q_b$ is the same absolutely normalized [original triangle action](actual_cross_cofactor_marked_action.md). Equality in (3) concerns the continuum upper envelope; it does not claim that every oscillatory finite polynomial realizes that rate.

## 2. Exact endpoint optimization

First suppose $b>0$ and $0<\delta<1/2$. Set

$$
z=\sin^2(\pi\delta),\qquad k=\cos(\pi\delta),\qquad
D=A^2-4Pz>0,\qquad t_c=\frac12-\delta.
$$

$L_\delta$ increases from $0$ to infinity before $t_c$ and decreases from infinity to

$$
L_{\mathrm{end}}=\frac{A+\sqrt D}{2z}
$$

after $t_c$. The endpoint derivatives in (2) are

$$
\partial_\mu F_L=\log b-\log L_\delta(\mu),\qquad
\partial_\nu F_L=\log L_\delta(\nu)-\log c.\tag{4}
$$

Before $t_c$, the $\mu$ dependence has its unique maximum at $\mu_b$, defined by

$$
\sin^2(\pi\mu_b)=\frac{k^2b^2}{(b+x)(b+y)}.\tag{5}
$$

A stationary $\nu$ before $t_c$ is a minimum; a stationary $\mu$ after $t_c$ is a minimum. Thus the only candidates beyond the diagonal $\mu=\nu$ have $\mu=\mu_b$ and either $\nu=1/2$ or a post-sign-change stationary $\nu_c$. The boundary $\mu=0$ is included by $b\to0$; for positive $b$, the initial positive derivative rules it out unless $\mu=\nu=0$. These observations also cover the boundaries of the ordered endpoint triangle.

The diagonal contributes at most $\max\{\log c,(\log b+\log c)/2\}$. The terminal endpoint $\nu=1/2$ gives

$$
Q_b(\delta)+\frac12\log c.\tag{6}
$$

The proved derivative $Q_b'=-\log(E_b/\sqrt D)$, with

$$
E_b=A+2bz+2\sqrt z\sqrt{bA+P+b^2z},
$$

is nonpositive, strictly negative unless $b=P=0$. Hence (6) never exceeds $Q_b(0)+\tfrac12\log c$. Also $Q_b(0)\geq\tfrac12\log b$, so the two quantities in (3) already cover every diagonal candidate.

A post-sign-change maximum exists only when $c\geq L_{\mathrm{end}}$. If $c>\max(x,y)$, this is precisely $\delta\geq\delta_c$, where

$$
\sin^2(\pi\delta_c)=\frac Ac-\frac P{c^2},\qquad
\sin^2(\pi\nu_c)=\frac{k^2c^2}{(c-x)(c-y)}.\tag{7}
$$

At $\delta=\delta_c$, $\nu_c=1/2$; for $\delta>\delta_c$, $t_c<\nu_c<1/2$. If $c\leq\max(x,y)$, there is no such interior branch.

## 3. The straddling branch has only spectral minima

Define the post-sign-change stationary action

$$
J_c(\delta)=\nu_c\log c+\int_0^{\nu_c}\log|\alpha(t)|\,dt
+\int_{\nu_c}^{1/2}\log\Lambda(t)\,dt.
$$

Then the straddling value is exactly

$$
S_L(\delta)=Q_b(\delta)+\log c-J_c(\delta).\tag{8}
$$

There is no new additive action constant: (8) follows by subtracting the integrals and using the same complete prefix integral zero as in (2). Put

$$
T_c^-=\sqrt{c^2z-cA+P},\qquad H_c=2cz-A+2\sqrt z\,T_c^-.
$$

On the strict branch $c>L_{\mathrm{end}}$, the exact derivative is

$$
J_c'(\delta)=-\log\frac{H_c}{\sqrt D}.\tag{9}
$$

A direct normalization proof avoids guessing a complex sheet. The envelope rule gives $\partial_{\log c}J_c=\nu_c$. Differentiating (7) gives $\partial_\delta\nu_c=-c\sin(\pi\delta)/T_c^-$. Direct algebra gives $\partial_{\log c}\log H_c=c\sin(\pi\delta)/T_c^-$. Thus the difference between the two sides of (9) is independent of $c$ for each fixed $\delta$.

As $c$ decreases to $L_{\mathrm{end}}$, $\nu_c$ tends to $1/2$. At that endpoint the complete prefix integral has derivative zero, so $J_c'$ tends to zero. The vanishing tail is regular because $\alpha(1/2)=-4z\ne0$. Simultaneously $T_c^-$ tends to zero and $H_c$ tends to $\sqrt D$. This fixes the difference to zero and proves (9). Moving interior logarithmic zeros are handled by uniform-integrability and principal-value differentiation of the explicit log-cosine primitive; no finite sampled quotient is used.

Consequently

$$
S_L'(\delta)=\log\frac{H_c}{E_b}.\tag{10}
$$

The two positive numbers are larger roots with the same product $D$:

$$
\begin{aligned}
E_b&=C_b+\sqrt{C_b^2-D},& C_b&=A+2bz,\\
H_c&=C_c+\sqrt{C_c^2-D},& C_c&=2cz-A.
\end{aligned}
$$

Both $C_b,C_c\geq\sqrt D$ on this branch, and the larger-root function is strictly increasing in $C$. Hence

$$
\operatorname{sign}S_L'
=\operatorname{sign}(C_c-C_b)
=\operatorname{sign}[(c-b)z-A].\tag{11}
$$

Since $z$ increases with $\delta$, this sign can only pass from negative to positive. An interior spectral stationary point is therefore a minimum. At the branch entry the value is (6). As $\delta\to1/2$, both $\mu_b$ and $\nu_c$ tend to zero, and uniform integrability gives $S_L\to\log c$. The straddling branch is thus bounded by the right side of (3). The diagonal and terminal candidates were already bounded in Section 2. At $\delta=0$, their known maximization attains (3), proving the envelope identity.

The proof extends to $b=0$ by its sole-start limit and to $xy=0$ by the exact first-order recurrence and displayed formulas; $A$ stays positive. The possibly singular endpoint $D=0$ occurs only at $\delta=1/2$, $x=y$, and is handled by the same continuous endpoint value. The original protected faces are never replaced by positive radii.

## 4. All face phases and the final spectral cap

The [exact continuous-real positivity lemma](actual_continuous_real_tail_coefficient_positivity.md) supplies a finite strengthening. Normalize

$$
Q_r=\frac{K_{i,i+r}}{\prod_{v=i+1}^{i+r}s_v^2}.
$$

Then

$$
Q_r=(x+y)Q_{r-1}+\beta_jxyQ_{r-2},\qquad
\beta_j=\frac{\alpha_{j-1}}{s_js_{j-1}},\quad j=i+r.
$$

This recurrence is used only for $r\geq2$, hence $j\geq i+2$; $Q_1=x+y$ is handled separately, so no denominator $s_0$ is introduced. The identity

$$
\alpha_{j-1}+s_js_{j-1}
=4\cos^2(\pi\delta)-4\sin^2\!\left(\frac\pi{2N}\right)\tag{12}
$$

is independent of $j$. Thus $\beta_j\geq-1$ for $|\delta|\leq1/2-1/(2N)$, equivalently $\sigma\in[-2,2\cos(\pi/N)]$. Induction using

$$
Q_r-xQ_{r-1}
=y[Q_{r-1}-xQ_{r-2}]+(1+\beta_j)xyQ_{r-2}
$$

proves coefficientwise nonnegativity on this entire interval. The initial values are $Q_0=1$, $Q_1=x+y$. Arbitrary phases of $x,y$ therefore have modulus bounded by the same $K$ at their positive moduli. In (1), taking absolute values of $b,c$ and of the retained scalar prefix and suffix factors reduces all face phases to the same envelope (2). No one-sided angular gap or absolute-value replacement inside the signed recurrence is used.

The remaining real spectral cap $[2\cos(\pi/N),2]$ has width $O(N^{-2})$. For a polynomial $p$ of degree at most $d$ bounded by $M$ on $[-2,b_N]$, $b_N=2\cos(\pi/N)$, the exterior-circle maximum principle gives

$$
|p(2)|\leq M\exp\!\left[d\,\operatorname{arcosh}\frac{6-b_N}{b_N+2}\right]
\leq CM.
$$

The same bound holds throughout the cap; its exponent is $O(1)$ uniformly in $N\geq3$. Apply it to the actual LEFT polynomial at each fixed face-phase tuple. Thus (3) bounds the global real-spectral weighted absolute value at arbitrary face phases. The RIGHT version follows by reversing the original row and middle orientation. Applying the same polynomial argument on the full real interval extends the bound to a fixed complex $\delta$ strip, at additional cost $e^{2\pi d|\operatorname{Im}\delta|}$, uniformly in those face phases.

This is still not coefficientwise domination: the known $\sigma=\sqrt3$ individual-coefficient counterexample is compatible with summing at fixed moduli. Nor may the actual shared coefficient be replaced by an unproved infimum of sums of local maxima. At fixed moduli the weighted full upper rate is bounded by

$$
\max\{Q_b(0)+Q_c(0),\log b,\log c\},
$$

because $Q_b(0)\geq\tfrac12\log b$, $Q_c(0)\geq\tfrac12\log c$, and a geometric mean never exceeds the larger endpoint. Zero-middle terms are interpreted by the exact vanishing statements above. A [strict complete-radius balance condition](general_complete_radius_balance_filling_volume.md) permits a shared-source application; no general capacity equality follows here.

## Validation and scope

Root and an independent peer read the complete proof and reported PASS. The reviews checked both parity factors, the arbitrary-interval transfer bound and both unused outside products, the ordered endpoint maximum, the post-sign-change derivative constant, the larger-root sign test, protected limits, exact continuant positivity at all face phases, and the bounded-cost spectral cap. The recurrence is used only from its second step. This review establishes the weighted local theorem, not a coefficientwise comparison or an unproved shared capacity equality.
