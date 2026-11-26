# Retaining the outgoing pair and the actual height in the next-four budget

Research deduction, 6 November 2026.

The frozen [next-four endpoint budget](research_mixed_first_four_next_four_endpoint_budget.md)
has a useful analytic improvement. The outgoing pair gives a quantitative
contribution to its ordinary-node cost, and the vertical reset need not
be charged at the worst permitted reference height. A finite family of
forced-coordinate ceilings also retains the actual ordinary height.
These give the explicit sufficient test (15) below. Its uniform sign
has not been proved. No cover or source calculation is run in this note.

Keep the original first-four/next-four reference, word length at least
three, the original outgoing tangent, and \(H=1/100\). Use all notation
and the final factorial rectangle of the frozen note. In particular
\[
 \begin{gathered}
 -.078<c<-.020,\quad -.102<h_s,h_b<-.001,\\
 .24<s_{*,R},b_{*,R}<.36,\qquad
 s_R\in[.22,.44],\quad b_R\in[.22,.45],\\
 d=\ell-B>0,\quad q=\Re(s_*+z_*)-1/2\in(.045,.21).
 \end{gathered}
 \tag{1}
\]

## 1. A quantitative contribution from the outgoing pair

Write \(g_h(t)=\Re g(t+ih)\), and retain
\[
 W_{sb}(s_R,b_R)=g_{h_s}(s_R)+g_{h_b}(b_R)
                         -g_{h_s+h_b}(s_R+b_R).
 \tag{2}
\]
All Bregman costs below are centered at the same actual reference.
The whole outgoing ordinary cost in the frozen decomposition is
\[
 \mathcal D_{sb}=D_{2g_{h_s}}+D_{g_{h_b}/2}+D_{W_{sb}}.
 \tag{3}
\]
Let
\[
 a_*=\Re\cot(\pi s_*),\qquad
 \mu_* =\min(a_*,7/16),\qquad
 \gamma_* =\frac1{2(2a_*+\mu_*)}.
 \tag{4}
\]
The cotangent bound in the frozen proof gives \(a_*>2/5\),
and hence \(\gamma_*<5/12\).

**Lemma 1.** At every nonpositive ordinary-node force \(-a\),
with zero outgoing force,
\[
 \sup_{s_R,b_R}\{-a(s_R-s_{*,R})-\mathcal D_{sb}\}
                      \le\frac{\gamma_*}{\pi}a^2,
                           \qquad a\ge0.
 \tag{5}
\]
The supremum is over the full final rectangle in (1).

For targets with \(s_R>s_{*,R}\), the objective is nonpositive:
the three costs in (3) are nonnegative on their connecting domains.
For \(s_R\le s_{*,R}<.36\), write at any point of the connecting
segment
\[
 a_s=\Re\cot\pi s,\qquad a_b=\Re\cot\pi b,
                         \qquad C_{sb}=\Re\cot\pi(s+b).
\]
The normalized Hessian of \(W_{sb}+g_{h_b}/2\) is
\[
 \pi^{-1}\nabla^2(W_{sb}+g_{h_b}/2)
 =\begin{pmatrix}a_s-C_{sb}&-C_{sb}\\
                 -C_{sb}&(3/2)a_b-C_{sb}\end{pmatrix}.
 \tag{6}
\]
The real cotangent decreases in its real coordinate throughout the
present intervals. Thus \(a_s\ge a_*\), and \(a_b>0\).
If \(C_{sb}\le0\), (6) is the sum of
\(\operatorname{diag}(a_s,(3/2)a_b)\) and a nonnegative
multiple of the all-ones matrix. Its Schur complement in the outgoing
coordinate is therefore at least \(a_s\ge a_*\).

If \(C_{sb}>0\), then \(s_R+b_R<.5\), so each real
coordinate is below \(.28\). The elementary bounds
\[
 \sin(.56\pi)>49/50,\quad
 -\cos(.56\pi)<1/5,\quad \cosh(.204\pi)<49/40
\]
give \(a_s,a_b>196/285\). Also
\(C_{sb}\le\cot(.44\pi)=\tan(.06\pi)<1/5\).
The outgoing diagonal is positive, and its Schur complement exceeds
\[
 \frac{196}{285}-\frac15
   -\frac{1/25}{(3/2)(196/285)-1/5}
 =\frac{9898}{22515}
 =\frac7{16}+\frac{763}{360240}>\frac7{16}.
 \tag{7}
\]
The sine, cosine and tangent constants follow from the elementary
Taylor bounds at \(.06\pi<33/175\); the hyperbolic constant is
already proved in the frozen note.

In both cases (6) is at least
\(\mu_*\operatorname{diag}(1,0)\) as a quadratic form.
Adding \(2g_{h_s}\) gives a lower Hessian
\(\pi(2a_*+\mu_*)\operatorname{diag}(1,0)\) on the entire
segment to the target. Integration yields
\[
 \mathcal D_{sb}\ge\frac\pi2(2a_*+\mu_*)
                             (s_R-s_{*,R})^2.
 \tag{8}
\]
Maximizing the resulting quadratic proves (5). This argument retains
every outgoing target and its correlation with the ordinary index;
it imposes no outgoing stationarity or interior-face condition.

## 2. A stronger horizontal endpoint majorant

Keep the explicit edge bound \(T_q\) from equation (27) of the
frozen note, including its negative summed-angle target. For
\(0\le\theta\le1\), define
\[
 \begin{split}
 h_\theta&=3C-B-\theta d,\qquad
 m_\theta=A-\frac{163}{298}h_\theta,\\
 \widehat{\mathcal N}_\theta
 &=\gamma_*(1-\theta)^2d^2
   +\frac{45}{298}h_\theta^2+\frac12m_\theta^2
   +\pi T_q(\theta d).
 \end{split}
 \tag{9}
\]
Then
\[
                        \pi L_*\le\widehat{\mathcal N}_\theta
                                  \le\mathcal N_\theta.
 \tag{10}
\]
Indeed retain the same private and incoming-edge flows as in the
frozen proof, but apply (5) jointly to the ordinary-node force
\(-(1-\theta)d\) and the zero outgoing force. The other two
node estimates, private-edge estimate and free private-flow minimum
are unchanged. Replacing \(\gamma_*\) by \(5/12\) gives a
weaker bound that still improves its former coefficient \(5/8\).

## 3. Reference-dependent forced ceilings

Set \(R=e^{2\pi H}\), \(T=e^{-2\pi h_s}\), and \(r_e=8/9\).
For \(t\in[.4,.42]\), put
\[
 \begin{gathered}
 a_e(t)=-\cos2\pi(.306+t),\quad
 a_s(t)=-\cos2\pi(.22+t),\quad
 a_z(t)=-\cos2\pi t,\\
 \mathcal P_t=(1+2r_ea_e(t)R+r_e^2R^2)
                 (T^2+2Ta_s(t)R+R^2),\\
                   \mathcal Q_t=(1+2a_z(t)R+R^2)^2.
 \end{gathered}
 \tag{11}
\]
These three trigonometric constants are positive.

**Lemma 2.** If \(\mathcal P_t<\mathcal Q_t\), every forced
maximizer at the chosen height satisfies \(z_R<t\).

The existing positive-height barriers give
\(e_R>.306\), \(s_R>.22\), \(e_R<.4\), and \(s_R<.44\)
at every forced maximum. Suppose \(t\le x=z_R\le.45\).
Both summed real parts lie in \((.5,1)\), where their cosine
increases with the summed coordinate. Thus their cosines are bounded
below by \(-a_e(t),-a_s(t)\), respectively. On the other hand
\(\cos2\pi x\le-a_z(t)\). Since \(|E|<r_e\) and the
ordinary inverse radius is exactly \(T\), the squared original
forced derivative ratio is strictly less than or equal to
\(\mathcal P_t/\mathcal Q_t\). A strict test therefore makes
that derivative negative at every proposed maximum with \(x\ge t\).
Decreasing the original real coordinate is an admissible improvement,
which proves the claim. The factor \(T\) retains the original chirp.

For a finite explicit choice, let
\[
 \mathcal T=\{2/5,81/200,41/100,83/200,21/50\},\qquad
 \mathcal T_* =\{t\in\mathcal T:\mathcal P_t<\mathcal Q_t\}.
 \tag{12}
\]
This set is nonempty at every actual reference: \(t=.42\) passes
by the uniform rational estimate in the frozen note. Its constants
majorize the exact factors in (11), with \(T<19/10\).

For each admissible ceiling define the positive credit
\[
 \mathcal C(t)=\frac{.5-t}{2}
          \{\log(2\sin\pi t)+\log2\}
                            +\pi H(.5-t).
 \tag{13}
\]
Concavity of \(J'(x)=\log(2\sin\pi x)\) bounds its integral
on \([t,.5]\) below by the endpoint trapezoid. The original
positive-height argument gives
\(\Re g(t+iH)\le J(t)-\pi H(.5-t)<-\mathcal C(t)\).
The real function \(\Re g(x+iH)\) increases on the original
plateau. Therefore every \(t\in\mathcal T_*\) gives
\(\max f_{\rm force}<G(H)-\mathcal C(t)\).

## 4. A combined sufficient inequality with the actual reset cost

Retain \(c\) rather than replacing it by its worst lower bound.
The proved fixed-line estimate gives
\[
 \pi\{G(H)-M\}
 <\frac{19\pi^2}{10}(H-c)^2
                   +\min_{\theta\in\Theta}\widehat{\mathcal N}_\theta,
 \qquad \Theta=\{0,1/4,1/2,3/4,1\}.
 \tag{14}
\]
Consequently a precise sufficient uniform test for both central gaps is
\[
 \boxed{\displaystyle
 \frac{19\pi^2}{10}(H-c)^2
   +\min_{\theta\in\Theta}\widehat{\mathcal N}_\theta
 \le\pi\min\left\{2\pi H,
                    \max_{t\in\mathcal T_*}\mathcal C(t)\right\}
                    -\frac\pi{500}.}
 \tag{15}
\]
All selections are over the displayed finite sets. The same actual
reference supplies every quantity, including \(c,h_s,a_*\), all
logarithmic increments and the outgoing tangent. A verification may
retain one strict ceiling test and one successful trial on each
reference region; it need not find a maximizing source point.
The strict vertical estimate makes (15) sufficient even with its
displayed weak inequality.

There is a simpler two-case version. If \(h_s\ge-.065\), the
forced ceiling \(z_R<.4\) from the next-three proof transfers
unchanged: the proof uses only the common private barrier, the lower
ordinary barrier, and \(|S|^{-1}<301/200\). All hold here under
this additional reference-height condition. Its forced credit is
\(133/2000+\pi/1000\), larger than the factorial credit
\(\pi/50\), because \(133-38\pi>0\).
If \(h_s<-.065\), retain the unconditional ceiling \(.42\)
and credit \(27/500+\pi/1250\), which is smaller than
\(\pi/50\), because \(48\pi-135>0\).
Thus the following scalar bound is also sufficient:
\[
 \min_{\theta\in\Theta}\widehat{\mathcal N}_\theta
 \le
 \begin{cases}
 \displaystyle\frac{\pi^2}{50}-\frac\pi{500}
              -\frac{19\pi^2}{10}(H-c)^2,&h_s\ge-.065,\\[4pt]
 \displaystyle\frac{13\pi}{250}+\frac{\pi^2}{1250}
              -\frac{19\pi^2}{10}(H-c)^2,&h_s<-.065.
 \end{cases}
 \tag{16}
\]
The exact credit in (13) and additional ceilings in (12) can improve
these coarse constants.

## 5. What the saved auxiliary obstruction does and does not show

The [saved rational auxiliary point](../repro/results/research-mixed-next-four-endpoint-budget-superset-point.json)
passes the implemented necessary reference filters but is not certified
as an actual word. Its five former trial values exceed the former
fixed threshold \(\pi^2/384\), so further subdivisions cannot
prove that particular test on the unchanged necessary superset.
This is not an obstruction to (15) or (16).

Indeed the saved intervals, without reevaluating the point, imply
\[
 h_s>-.065,\qquad c>-68563041/10^9,\qquad
                      \mathcal N_{1/4}<75236077/10^9.
 \tag{17}
\]
Using only \(157/50<\pi<22/7\), its first allowance in (16)
exceeds this old, larger trial value by at least
\[
 (157/50)^2\{1/50-(19/10)(78563041/10^9)^2\}
 -\frac{22/7}{500}-\frac{75236077}{10^9}
 =\frac{8017627195001527123}{175000000000000000000000}>0.
 \tag{18}
\]
Thus even the former horizontal trial pays this saved point once the
actual height and the conditional forced ceiling are retained. This
is exact rational arithmetic on saved intervals, not a new point or
source evaluation, and does not assert that the point is realizable.

The uniform signs of (15) and (16) remain open. The failed bounded
cover and its point record remain unchanged, as does their frozen
proof input. Nothing here supplies the omitted finite-source sectors,
the length-two comparison, or a filling-volume theorem.
