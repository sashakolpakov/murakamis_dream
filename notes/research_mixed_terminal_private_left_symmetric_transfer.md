# The private left face retains the symmetric terminal costs

Research deduction, 6 November 2026.

Fixing the terminal-four private variable at its real left cut
\(e_0=27/100\) still permits the sharper terminal-index restriction
\(.22<t_R<.4\). This supplies the missing domain hypothesis for the
symmetric pair costs. Consequently the completed whole-\(D_4\) main
budget transfers to this face on the original admissible source
references, with the additional bare-face reserve. No private action,
logarithm, reference, optimizer or parameter evaluation is needed.

## 1. The literal cut and its index derivative

Keep the normalization, complete selected weight and incoming complex
marginal of the
[original private-left identity](research_mixed_terminal_private_left_joint_transfer.md).
The incoming flag and terminal flag are \(\beta=\epsilon=1\).
Write \(a=y+iH,\ t=x+ih\), and consider
\[
 y\in P=[11/50,9/20],\qquad
 x\in[3/20,1/2],\qquad
 -27/250\le h\le-1/50,\qquad
 0\le H\le7/500,\qquad e=e_0=27/100.
 \tag{1}
\]
The height interval is the full original terminal-four interval,
not a newly optimized height. The reduced terminal phase is
\[
 \begin{split}
 \Phi_1(a;t,e_0)={}&S(e_0)+g(a+t)+g(e_0+t)-3g(t)
       -g(e_0)-g(a)\\
 &-i\pi(e_0-e_0^2)/2+2\pi iat .
 \end{split}
 \tag{2}
\]
Its original logarithmic derivative is
\[
 \Phi_{1,t}=g'(a+t)+g'(e_0+t)-3g'(t)+2\pi ia.
 \tag{3}
\]
Put \(r=e^{2\pi h}\), \(R=e^{-2\pi H}\). Since
\(g'(z)=\log(1-e^{-2\pi iz})\) on the original strip,
\[
 e^{2\Re\Phi_{1,t}}=
 \frac{\{R^2+r^2-2Rr\cos2\pi(x+y)\}
       \{1+r^2-2r\cos2\pi(x+e_0)\}}
      {\{1+r^2-2r\cos2\pi x\}^3}.
 \tag{4}
\]
The first factor retains the original chirp: its real contribution
\(-2\pi H\) is exactly the factor \(R\) in (4).
This identity is pointwise on the whole target product (1).
It uses no stationarity or equation for an enclosing midpoint.

**Proposition 1.** Uniformly on (1),
\[
 \Re\Phi_{1,t}(a;.22+ih,e_0)>\frac{279}{31808}>0,\qquad
 \Re\Phi_{1,t}(a;.4+ih,e_0)<-\frac{21}{82}<0.
 \tag{5}
\]
Therefore every maximum of this terminal face, and every joint profile
whose other terms are independent of \(t\), occurs with
\(.22<t_R<.4\).

*Proof.* The elementary bounds
\[
                     \frac12<r<1,\qquad \frac9{10}<R\le1
 \tag{6}
\]
hold throughout (1). For the first, use
\(.216\pi<17/25\) and
\[
 e^{17/25}\le 1+\frac{17}{25}
        +\frac{(17/25)^2}{2(1-17/75)}
       =\frac{5739}{2900}<2.
 \tag{7}
\]
For the second, \(R\ge e^{-.028\pi}>1-.028\pi>
114/125>9/10\).

At \(x=.22\), the two summed real parts lie in
\([.44,.67]\) and at \(.49\). Thus
\[
 -\cos2\pi(x+y)>\frac25,\qquad
 -\cos2\pi(x+e_0)>\frac{99}{100},\qquad
 \cos2\pi x>0.
 \tag{8}
\]
For explicit rational witnesses, using \(\pi<22/7\),
\[
 \begin{split}
 1-\frac12(187/175)^2-\frac25&=\frac{1781}{61250}>0,\\
 1-\frac12(11/175)^2-\frac{99}{100}
     &=\frac{983}{122500}>0.
 \end{split}
 \tag{9}
\]
The minimum of the first negative cosine is
\(\cos(.34\pi)\); the second is \(\cos(.02\pi)\).
Let \(X=1+r^2\). The first numerator in (4) exceeds
\(81/100+r^2+(18/25)r\). On \(r\in[1/2,1]\),
\[
 81/100+r^2+(18/25)r-\frac{142}{125}(1+r^2)
 =-\frac{17}{125}r^2+\frac{18}{25}r-\frac{163}{500}
 \ge0.
 \tag{10}
\]
This polynomial is concave; its endpoint values are \(0\) and
\(129/500\). The second numerator exceeds
\(X+(99/50)r\). Since
\[
 \frac{r}{1+r^2}\ge\frac25
 \quad\Longleftrightarrow\quad
 -2r^2+5r-2=(2r-1)(2-r)\ge0,
 \tag{11}
\]
it is at least \((224/125)X\). The denominator is less
than \(X^3\). Therefore
\[
 e^{2\Re\Phi_{1,t}}>
 \frac{(142/125)(224/125)}{X}
 \ge\frac{15904}{15625}>1.
 \tag{12}
\]
The inequality \(\log(1+u)>u/(1+u)\), \(u>0\),
gives the first strict bound in (5).

At \(x=.4\), the summed real parts lie in \([.62,.85]\)
and at \(.67\). Consequently
\[
 -\cos2\pi(x+y)<\frac34,\qquad
 -\cos2\pi(x+e_0)<\frac12,\qquad
 -\cos2\pi x>\frac45.
 \tag{13}
\]
Indeed \(.24\pi>3/4\), and
\[
 \frac34-\left(1-\frac{(3/4)^2}{2}
                      +\frac{(3/4)^4}{24}\right)
       =\frac{37}{2048}>0.
 \tag{14}
\]
This bounds \(\cos(.24\pi)\), the maximum of the first
negative cosine. The second is \(\cos(.34\pi)<1/2\)
because \(.34>1/3\). Finally
\[
 1-\frac12(22/35)^2-\frac45=\frac3{1225}>0
 \tag{15}
\]
bounds \(\cos(.2\pi)\) from below.
With \(D=X+(8/5)r\), equations (4), (6) and (13) imply
\[
 e^{2\Re\Phi_{1,t}}
 <\frac{(X+(3/2)r)(X+r)}{D^3}
 <\frac1D<\frac{20}{41}.
 \tag{16}
\]
Both numerator factors are smaller than \(D\), while
\(D>1+1/4+4/5=41/20\).
Now \(\log u\le u-1\) proves the second bound in (5).

The [full reduced-current Hessian](research_mixed_terminal_four_reduced_currents.md),
Lemma 1, applies to \(e=e_0\) real and the whole product (1).
In particular \(\Re\Phi_{1,tt}<0\). Thus for \(x\le.22\)
increasing \(x\) raises the phase, and for \(x\ge.4\)
decreasing it raises the phase. The ordinary factor, complete selected
weight and incoming affine subtraction are independent of \(t\).
This proves the asserted joint optimizer restriction. \(\square\)

## 2. Curvature after the private coordinate is fixed

We now set the selected height to the single value \(H=1/100\).
Retain the original canonical heights and references used in
[the uniform main comparison](research_mixed_terminal_uniform_main_comparison.md).
The ordinary-index barrier is unchanged because (2) is independent of
\(s\). Together with Proposition 1 it gives the containing target product
\[
 b_R,a_R\in P,\qquad s_R\in[.22,.5],\qquad
 t_R\in[.22,.4],\qquad e=e_0.
 \tag{17}
\]
The incoming height satisfies \(|h_b|\le.12\), and the certified
ordinary and terminal heights satisfy
\(|h_s|,|h_t|\le.108\). The stronger ordinary-index height hypotheses
are those already verified for the same canonical family in the main
comparison. Its reference real parts belong to the containing intervals
in (17), so every segment from the lifted reference stays inside them.

Write \(g_h(x)=\Re g(x+ih)\), and define
\(\phi_h(x;x_*)=g_h(x)-g_h(x_*)-g_h'(x_*)(x-x_*)\).
For the literal cut defect \(D_\nu^L\) of the original private-left
note, in variable order \((b_R,s_R,a_R,t_R)\),
\[
 - (D_\nu^L)''\succeq
 \operatorname{diag}\bigl(g_{h_b}'',\,2g_{h_s}'',
                          (\nu+1)g_H'',\,2g_{h_t}''\bigr).
 \tag{18}
\]
Here both \(\nu=0,1\) retain all \(a_R\in P\).

To prove (18), use exactly
\[
 Q_1=V(s,b)+V(s,a)-g(s)+2\pi ibs,\qquad
 \Phi_1=V(t,a)+V(t,e_0)-g(t)+R_1(e_0)+2\pi iat,
 \tag{19}
\]
where \(V(z,w)=g(z+w)-g(z)-g(w)\).
The [symmetric pair lemma](research_mixed_terminal_symmetric_pair_costs.md)
applies to all four pairs in (19). In particular it applies to the
altered pair \(V(t,e_0)\): both real parts are at least \(.22\),
their sum is at most \(.67\), and the heights are \(h_t,0\).
Restricting its matrix inequality to the fixed \(e_0\) retains
\(\tfrac12g_{h_t}''\) in the \(t\) entry. This is the extra
half curvature that force contraction by itself does not supply.
The pair \(V(t,a)\) retains another half, and \(-g(t)\) a full
unit, giving \(2g_{h_t}''\). The other rows and the incoming
halfweight give (18) exactly as in the main allocation.
All original imaginary quadratics remain; their real horizontal
Hessians vanish. The term \(R_1(e_0)\) is constant, so no
estimate for \(S''(e_0)\) is needed.

## 3. Transfer of the completed uniform main budget

At the same lifted reference as before, fixing \(e=e_0\) changes
the value to \(T_\nu+E_L\) and the force vector to
\((0,A_s,A_{a,\nu},A_t+d_L)\). These are the exact identities
of the original private-left note, with its unchanged marginal.
Let the exact symmetric-cost gains be
\[
 \begin{split}
 \widetilde G_s(q)&=\sup_{x\in[.22,.5]}
       \{q(x-\Re s_*)-2\phi_{h_s}(x;\Re s_*)\},\\
 \widetilde G_{a,\nu}(q)&=\sup_{x\in P}
       \{q(x-\Re a_*)-(\nu+1)\phi_H(x;\Re a_*)\},\\
 \widetilde G_t(q)&=\sup_{x\in[.22,.4]}
       \{q(x-\Re t_*)-2\phi_{h_t}(x;\Re t_*)\}.
 \end{split}
 \tag{20}
\]
Integrating (18) from the lifted trial, and discarding only the
nonnegative incoming cost whose force is zero, proves
\[
 \sup D_\nu^L\le T_\nu+E_L+\widetilde G_s(A_s)
       +\widetilde G_{a,\nu}(A_{a,\nu})
       +\widetilde G_t(A_t+d_L).
 \tag{21}
\]
The [whole-\(D_4\) private-force theorem](research_mixed_terminal_four_input_private_left_force.md)
proves \(A_t<0\) and \(0<d_L<-A_t\) for these same
canonical references. For any negative force, convexity permits the
last supremum in (20) to be restricted to \(x\le\Re t_*\);
the reference itself is an admissible target. Increasing that force
toward zero decreases every remaining affine term. Hence
\[
                \widetilde G_t(A_t+d_L)\le\widetilde G_t(A_t).
 \tag{22}
\]
This monotonicity concerns the exact scalar supremum. It does not
assume that a rounded gain routine or a sum of independently rounded
outputs is monotone.

The three exact gains on the right of (21), after (22), are precisely
those bounded by the completed symmetric-cost main budget. Its cubic
coefficients are \(88/5,(\nu+1)49/5,88/5\). The uniform-main
proof bounds their common trial value plus their sum by a number
strictly below \(-1/400\), for both full-\(P\) alternatives.
This uses its actual three-cost upper bounds, not an inference from
the sign of the optimized main phase alone.

On the original oriented and inverse-feasible actual source domain,
the old bare private-left source reserve gives
\(E_L\le U_L<-1/20000\), at the same reference. Therefore
\[
                    \sup D_\nu^L<-\frac{51}{20000},
                    \qquad \nu=0,1 .
 \tag{23}
\]
The force theorem and main budget hold on the whole auxiliary \(D_4\);
the source-reserve premise in (23) retains its original admissible
\(K_4\) source scope. No eligibility of an independent containing
rectangle is inferred here.

The inherited finite-current estimates consequently give the literal
ordinary-main times private-left/terminal-main current, with the full
\(d_N(X_a)X_a^{-N}\) and incoming \(|d_N(X_b)|^{1/2}\), an upper
bound by a polynomial prefactor times
\[
 \exp N\{\Re[M_*+p_*(b-b_*)]-51/20000+\tau\}.
 \tag{24}
\]
For a sufficiently small fixed tolerance and all sufficiently large
\(N\), the finite rate gap \(1/800\) follows. This keeps the original
compact source hypotheses, small ordinary-color neighborhood, fixed
jets and both level parities. It is a bound for this face, not a
complete terminal-kernel or whole-word theorem.

## 4. Fixed exact verification protocol

The new checker
[check_mixed_terminal_private_left_symmetric_transfer.py](../experiments/check_mixed_terminal_private_left_symmetric_transfer.py)
checks the rational witnesses (7), (9)--(16), the degree-two identity
and endpoint argument in (10), and the arithmetic in (23).
It binds this proof and the frozen source, pair-cost, force and main
proofs, including the completed saved force and vertex records.
All recorded inherited input hashes are checked before and after.
It does not reevaluate those records, a primitive, a reference or a
source. The analytic inequalities and their source scopes are proved
above; the checker is a fixed rational witness verification, not a new
parameter cover. Its sole output is a fresh record, after review.
