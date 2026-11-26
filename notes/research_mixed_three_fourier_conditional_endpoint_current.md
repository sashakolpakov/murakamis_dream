# The complete endpoint correction for the twice-crossed conditional source

Research deduction, 7 November 2026. The literal conditional polynomial
obtained after two negative crossings has an exact whole-period
factorial interpolation. Both horizontal aliases vanish at infinite
height. The two remaining endpoint currents, including all their
unbounded parts, have an absolute upper bound at the genuine last-row
forcing rate. For the actual original incoming references, the existing
endpoint comparison pays this entire correction.

A zero-mode integral survives. This note does not bound that integral
by a selected saddle, nor infer a crossed-source asymptotic from the
new critical-point criterion. No numerical evaluation is used.

## 1. The literal whole-period interpolation

Let \(N\ge2\), \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\[
 X=e^{-2\pi ia},\qquad W=e^{-2\pi iy},\qquad
 0<\Re a,\Re y<1/2,\qquad \Im y>0.
\tag{1}
\]
The parameters range over a fixed compact subset of this domain.
Set
\[
 C_N=C_{0,N}(X,W)
   =\sum_{j=0}^{N-1}
      \frac{X^{-j}(rX;r)_j(rW;r)_j}{P_j^2}.
\tag{2}
\]
This is precisely the source in
[the complete negative-crossing identity](research_mixed_fourier_negative_crossing_full_sources.md),
equation (14).

Use the original marked factorial \(\Pi_N\) and its reciprocal
continuation \(E_N\). Their domains and zeros are proved in
[the joint global chart](research_mixed_fourier_right_cap_joint_global_chart.md),
Section 1, and
[the global cardinal chart](research_mixed_fourier_global_factorial_cardinal.md).
Define
\[
 T_N(s;a,y)=e^{2\pi iNas}
       \Pi_N(s+a)\Pi_N(s+y)E_N(a)E_N(y)E_N(s)^2.
\tag{3}
\]
Its physical values are exactly the summands in (2), including
\(j=0\). Put
\[
 \alpha_N=-\frac1{2N},\qquad \beta_N=\alpha_N+1.
\tag{4}
\]
The function (3) is holomorphic on a neighborhood of every finite
rectangle with real sides \(\alpha_N,\beta_N\). Indeed
\(\Re(s+a),\Re(s+y)>-1/N\), while \(\Re s<1\).
Every positive factorial wall in a numerator remains a zero, not
a pole. There is no periodic identification of an upper shifted
factorial.

For finite \(H_-,H_+>0\), the exact counterclockwise cotangent
identity, with coefficient \(N/(2i)\), gives
\[
 C_N=I_N+L_{N,H_-}+U_{N,H_+}+J_{N,H_-,H_+},
\tag{5}
\]
where
\[
 \begin{split}
 I_N&=N\int_{\alpha_N}^{\beta_N}T_N(u)\,du,\\
 L_{N,H}&=N\int_{\alpha_N}^{\beta_N}
       T_N(u-iH)\frac{e^{-2\pi iN(u-iH)}}
                         {1-e^{-2\pi iN(u-iH)}}\,du,\\
 U_{N,H}&=N\int_{\alpha_N}^{\beta_N}
       T_N(u+iH)\frac{e^{2\pi iN(u+iH)}}
                         {1-e^{2\pi iN(u+iH)}}\,du,\\
 J_{N,H_-,H_+}
   &=iN\int_{-H_-}^{H_+}w_{N,0}(v)
       [T_N(\beta_N+iv)-T_N(\alpha_N+iv)]\,dv,\\
 w_{N,0}(v)&=\frac1{1+e^{2\pi Nv}}-\boldsymbol1_{\{v<0\}}.
 \end{split}
\tag{6}
\]
Its signs and orientations are those of
[exact vertical regrouping](research_exact_vertical_current_regrouping.md).
The value assigned to \(w_{N,0}\) at zero has no effect.
In particular the zero mode in (5) has the positive density \(N\).

## 2. Both aliases vanish, with the original upper branch

The exact cyclotomic formula and reflection in
[factorial alias elimination](research_mixed_fourier_factorial_alias_elimination.md),
equations (2)--(7), give at fixed \(N\)
\[
 \begin{split}
 \Pi_N(z)&=\sqrt N e^{i\pi\gamma_N}(1+o(1)),
                                   &&\Im z\longrightarrow-\infty,\\
 \Pi_N(z)&=\sqrt N e^{-i\pi\gamma_N}
       e^{i\pi[N(z-z^2)-z]}(1+o(1)),
                                   &&\Im z\longrightarrow+\infty.
 \end{split}
\tag{7}
\]
These are uniform in bounded real strips, with the specified
Gamma-product normalization. Thus
\[
 \begin{split}
 T_N(s)&=E_N(a)E_N(y)e^{2\pi iNas}(1+o(1)),
                                      &&\Im s\longrightarrow-\infty,\\
 T_N(s)&=D_N(a,y)e^{-2\pi iNys}(1+o(1)),
                                      &&\Im s\longrightarrow+\infty,
 \end{split}
\tag{8}
\]
where the nonzero fixed-level constant is exactly
\[
 D_N(a,y)=E_N(a)E_N(y)
  \exp\{i\pi[N(a+y-a^2-y^2)-(a+y)]\}.
\tag{9}
\]
For the second line, the polynomial identity used before taking
moduli is
\[
 [N(s+a-(s+a)^2)-(s+a)]
 +[N(s+y-(s+y)^2)-(s+y)]
 -2[N(s-s^2)-s]+2Nas
 =N(a+y-a^2-y^2)-(a+y)-2Nys.
\tag{10}
\]
Consequently the complete lower and upper aliases have respective
fixed-level decay rates
\[
 e^{-2\pi N(1-\Re a)H},\qquad
 e^{-2\pi N(1-\Re y)H}.
\tag{11}
\]
Both are strictly decaying. No interchange of \(N\) and \(H\)
is used to send these two horizontal integrals to infinity.

## 3. The exact monodromy and the finite-height endpoint bounds

Write
\[
 x=\Re a,\quad h=\Im a,\quad \xi=\Re y,\quad \upsilon=\Im y,
 \qquad
 \mathcal F(a,y)=2\pi(-h)_++2\pi\upsilon .
\tag{12}
\]
The original one-period factorial recurrence yields, with
\(A=X^N\), \(B=W^N\), \(t=e^{-2\pi iNs}\),
\[
 T_N(s+1)=
 \frac{(1-At)(1-Bt)}{A(1-t)^2}\,T_N(s).
\tag{13}
\]
On \(s=\alpha_N+iv\), \(t=-e^{2\pi Nv}\), so the denominator
never vanishes. Possible numerator zeros remain in this identity.
In particular the exact difference multiplier is
\[
 \frac{(1-A)+(A-B)t+A(B-1)t^2}{A(1-t)^2}.
\tag{14}
\]
This is the original conditional critical polynomial in the
\(N\)-th powers, but its occurrence here is an exact finite-level
identity, not a stationary approximation.

Use the original regular-strip primitive \(g\) to define
\[
 L(v)=
  \Re\{g(a+iv)+g(y+iv)-g(a)-g(y)\}-2\pi xv.
\tag{15}
\]
Every argument in (15) has real part strictly between zero and
one half, at every real \(v\). On this strip
\[
 0<\Im g'(z)<\pi-2\pi\Re z.
\]
To see the branch directly, \(1-Re^{-2\pi i\Re z}\), \(R>0\),
lies in the upper half-plane and its argument increases from zero
to \(\pi-2\pi\Re z\). Hence, at all heights,
\[
              -2\pi(1-\xi)<L'(v)<-2\pi x,\qquad L(0)=0.
\tag{16}
\]
This estimate does not use a conditional critical point.

Fix any finite height interval. The original regular-strip
factorial expansion, including the shift \(\alpha_N=-1/(2N)\),
and the exact midpoint identity
\[
       |\Pi_N(\alpha_N+iv)|^2=\frac{N}{1+e^{2\pi Nv}}
\tag{17}
\]
give, uniformly on that interval for large \(N\),
\[
 |T_N(\alpha_N+iv)|
       \le \frac{C}{N}(1+e^{2\pi Nv})e^{NL(v)}.
\tag{18}
\]
Equation (17) is the original Gamma-reflection identity in
[lower-half continuation](research_lower_half_factorial_continuation.md),
equation (6). It holds also at \(v=0\), where a nonuniform
endpoint Stirling approximation must not be substituted.

Multiplying (18) by the exact kernel gives the left rate
\[
 L_{\mathrm L}(v)=L(v)+2\pi\min(v,0).
\tag{19}
\]
By (16), it increases on the negative half-line and decreases
on the positive half-line. Quantitatively,
\[
 L_{\mathrm L}(v)\le
 \begin{cases}
 -2\pi\xi|v|,&v\le0,\\
 -2\pi x v,&v\ge0.
 \end{cases}
\tag{20}
\]
The positive-height factor in (17) is essential: it agrees with
\(\Re g_+(iv)=-\pi v\) for \(v>0\), and is then canceled by
the positive-height kernel weight.

For the right side, (13) and \(|1+z|\le2e^{(\log|z|)_+}\)
give the upper rate
\[
 \begin{split}
 L_{\mathrm R}(v)=L_{\mathrm L}(v)-2\pi h
     +2\pi(v+h)_++2\pi(v+\upsilon)_+-4\pi v_+.
 \end{split}
\tag{21}
\]
Its value at zero is \(\mathcal F(a,y)\).
On each smooth piece with \(v<0\), its derivative is
\(L'(v)+2\pi\), \(L'(v)+4\pi\), or \(L'(v)+6\pi\);
all are greater than \(2\pi\xi\).
For \(v>0\), its derivative is \(L'(v)\),
\(L'(v)-2\pi\), or \(L'(v)-4\pi\);
all are less than \(-2\pi x\).
The function is continuous at every breakpoint, so
\[
 L_{\mathrm R}(v)\le \mathcal F(a,y)+
 \begin{cases}
 -2\pi\xi|v|,&v\le0,\\
 -2\pi x v,&v\ge0.
 \end{cases}
\tag{22}
\]
In particular the full forcing factor \(|W|^N>1\) has not
been discarded. The maximum is precisely its true real-endpoint
rate, rather than the rate of a periodically reset upper branch.

## 4. The unbounded tails and a uniform finite-source estimate

We justify using (20)--(22) for the whole infinite current.
Let \(d>0\) be a common lower bound for \(x,\xi\) on the
compact parameter set, and let \(H_0\) bound all its imaginary
parts in absolute value. The exact remainder in
[the cyclotomic factorial formula](research_exact_cyclotomic_factorial.md),
equations (8)--(9), implies the following uniform tail estimate.
For a sufficiently large fixed \(H>H_0+1\), every lower- or
upper-half factorial remainder appearing in (3), at heights
\(\pm v\) with \(v\ge H\), has modulus at most
\[
                        N\epsilon(v),
 \qquad \sup_{v\ge H}\epsilon(v)\longrightarrow0
                                  \quad(H\longrightarrow\infty).
\tag{23}
\]
Here no height is evaluated. For example take
\(\rho_v=e^{-2\pi(v-H_0)}\) and a fixed \(C_0\) bounding all
real parts and fixed shifts. The explicit positive expression
\[
 \epsilon(v)=
   \frac{(v+C_0+1)\rho_v^2}{2(1-\rho_v^2)}
                +\frac{\rho_v}{2(1-\rho_v)}
\tag{24}
\]
majorizes each normalized remainder for \(N\ge2\);
enlarging \(C_0\) if necessary covers every argument.
Its supremum on a tail tends to zero.

At the left endpoint all factorials are nonzero, since their
real parts remain in their original zero-free strips.
Comparison with the same left current at \(+H\) or \(-H\),
using (8), gives for \(v\ge H\)
\[
 \begin{split}
 |w_{N,0}(v)T_N(\alpha_N+iv)|
 &\le 2|w_{N,0}(H)T_N(\alpha_N+iH)|\\
 &\quad\cdot
 e^{-2\pi N(1-\xi)(v-H)+8N\epsilon_H},\\
 |w_{N,0}(-v)T_N(\alpha_N-iv)|
 &\le 2|w_{N,0}(-H)T_N(\alpha_N-iH)|\\
 &\quad\cdot
 e^{-2\pi N(1-x)(v-H)+8N\epsilon_H},
 \end{split}
\tag{25}
\]
where \(\epsilon_H=\sup_{v\ge H}\epsilon(v)\).
The factor \(8\) allows the two numerator and two reciprocal
remainders at both ends of the ratio. Constant parameter
factorials cancel in this same-source comparison.

For the right endpoint one need not divide by its possibly zero
numerator. In (13), for \(v\ge H\) both positive parts are
active, and for \(v\le-H\) both are inactive. Directly,
\[
 |T_N(\beta_N+iv)/T_N(\alpha_N+iv)|
 \le
 \begin{cases}
 4e^{2\pi N\upsilon},&v\ge H,\\
 4e^{-2\pi Nh},&v\le-H.
 \end{cases}
\tag{26}
\]
Both displayed exponents are at most \(N\mathcal F(a,y)\).
Choose one fixed \(H\) so large that
\(8\epsilon_H<\pi dH\).
Equations (20), (25), and (26) then pay the finite remainder
loss while preserving a strict tail reserve. They prove
absolute convergence and a uniform large-\(N\) tail bound.
There is no interchange based only on fixed-\(N\) convergence.

Integrating (18)--(22) on \([-H,H]\) costs \(O(N^{-1})\)
because \(d>0\). Integrating the tail exponentials in (25)
has the same cost. Including the original outside density
\(N\), we obtain the following full correction estimate.

**Theorem 1.** Uniformly on the compact parameter set in (1),
for sufficiently large \(N\) of either parity, the exact formula is
\[
 \boxed{\quad
 C_{0,N}(X,W)=I_N+J_N,\qquad
 J_N=iN\int_{\mathbb R}w_{N,0}(v)
    [T_N(\beta_N+iv)-T_N(\alpha_N+iv)]\,dv ,
 \quad}
\tag{27}
\]
and
\[
 \boxed{\qquad
 N\int_{\mathbb R}|w_{N,0}(v)|
  \{|T_N(\beta_N+iv)|+|T_N(\alpha_N+iv)|\}\,dv
       \le \frac{C}{N}e^{N\mathcal F(a,y)} .
 \qquad}
\tag{28}
\]
In particular (28) controls the entire paired correction before
any cancellation between the two sides is used.
The term \(I_N\) in (27) remains unchanged.

## 5. Payment for the actual twice-crossed boundary

Return to \(y=x_0\), \(\upsilon=\Im x_0>0\), and the actual
family
\[
 \eta\in\{0,1\},\qquad a_*\in K_{3+\eta},\qquad
 a=x+i\Im a_*,\quad x\in P=[11/50,9/20].
\tag{29}
\]
At \(\eta=1\) the incoming height is the original negative,
unselected height. Let \(B_\eta(x)\) be the unchanged allocated
supporting plane of the complete original Fourier cap.
The endpoint-payment theorem gives, with the original allocation,
\[
 2\pi(-\Im a)_++\pi\upsilon-\frac{\eta}{2}\Re g(a)
                  <B_\eta(x)-\frac{387}{70000}.
\tag{30}
\]
This is the genuine original final-row comparison in
[endpoint payment](research_mixed_fourier_right_cap_endpoint_payment.md),
not a comparison to a newly chosen crossed action.

By (14) of the complete negative-crossing identity,
\[
 \mathcal M_{-2}Z_N
       =\frac{\kappa^{-2}e^{\pi i(N-1)y}}N I_N
                         +\mathcal R_{-2,N},
 \qquad
 \mathcal R_{-2,N}
       =\frac{\kappa^{-2}e^{\pi i(N-1)y}}N J_N .
\tag{31}
\]
The absolute boundary estimate is therefore
\[
 |\mathcal R_{-2,N}|
       \le \frac{C}{N^2}
          e^{N\{2\pi(-\Im a)_++\pi\upsilon\}}.
\tag{32}
\]
The bounded factor \(e^{\pi\upsilon}\) has been included in \(C\).
The original Fourier-weight upper bound, used only at its admitted
negative height when \(\eta=1\), combines with (30) to give
\[
 \boxed{\quad
 |d_N(X)|^{\eta/2}|\mathcal R_{-2,N}|
              \le e^{N\{B_\eta(x)-1/200\}}
 \quad}
\tag{33}
\]
for sufficiently large \(N\). No finite Fourier weight is divided
out in this deduction.

This closes the complete endpoint/alias correction in (31).
The surviving zero-mode integral still contains its full real
period, all upper shifted-factor branches and numerator zeros.
The new
[cotangent-root criterion](research_mixed_three_conditional_root_criterion.md)
can identify a nondegenerate zero-lift critical point when its
inequality holds, but does not supply the missing comparison
for that integral. In particular (33) is neither an upper bound
for the whole crossed function nor a nonzero crossed asymptotic.
