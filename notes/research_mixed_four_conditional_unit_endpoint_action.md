# The original conditional action has zero endpoint constant

Private written proof, 10 November 2026. The critical action of the
original type-four conditional source tends to zero as the real
incoming coordinate approaches its periodic endpoint from below.
This fixes the integration constant in its endpoint expansion.
Together with the whole-unit-arc multiplier theorem, it also
proves strict positivity of the real action before that endpoint.

No action is evaluated numerically. This concerns the original
phase, not a complete finite-source asymptotic at the endpoint.

## 1. Original phase and continuous primitive endpoints

Keep the original normalization in
[the incoming-action source](research_mixed_four_conditional_positive_incoming_action.md):
\[
 g(z)=J(z)+\frac{i\pi}{2}(z-z^2),\qquad
 J'(z)=\Log(2\sin\pi z),\qquad J(0)=0,
 \tag{1}
\]
continued from the positive real sine interval. In the regular
strip \(0<\Re z<1\),
\[
                    g'(z)=\Log(1-e^{-2\pi iz}).
 \tag{2}
\]
In particular its prescribed lower endpoint value is \(g(0)=0\).

Both strip endpoints are continuous for this primitive.
Here is a direct branch check. Near zero write
\[
 1-e^{-2\pi iz}=2\pi iz\,A_0(z),\qquad A_0(0)=1,
 \tag{3}
\]
with \(A_0\) holomorphic and nonzero. On the right half-neighborhood,
the original logarithm in (2) is
\[
 g'(z)=\Log z+\log(2\pi)+i\pi/2+\log A_0(z).
 \tag{4}
\]
The identity follows first on the positive real interval and then
by continuation. The local logarithm of \(A_0\) is zero at zero.
Integrating, with the original value in (1), gives
\[
 g(z)=z\Log z+\{\log(2\pi)+i\pi/2-1\}z+O(z^2).
 \tag{5}
\]
Thus \(g(z)\to0\) for \(z\to0\) from the original strip.

Similarly, for \(\zeta=1-z\) in a small right half-neighborhood,
\[
 1-e^{2\pi i\zeta}=-2\pi i\zeta\,A_1(\zeta),\qquad A_1(0)=1.
 \tag{6}
\]
The original branch gives
\[
 g'(1-\zeta)=\Log\zeta+\log(2\pi)-i\pi/2+\log A_1(\zeta).
 \tag{7}
\]
The integrability of this logarithm along the real interval
defines a finite constant \(g_1\), and the local antiderivative
then yields
\[
 g(1-\zeta)=g_1-\zeta\Log\zeta
       -\{\log(2\pi)-i\pi/2-1\}\zeta+O(\zeta^2).
 \tag{8}
\]
This proves continuity at the upper endpoint from every approach
inside the strip. No value for \(g_1\) is needed or assigned.
The two occurrences of that same constant will cancel.

## 2. The original critical action tends to zero

Let \(K\) be any compact subset of
\[
                     \{Y:\Im Y<0,\ \Re Y<1\},
 \tag{9}
\]
and put
\[
 X=e^{-2\pi ia},\quad 1/2\le a<1,\qquad
 y=-\frac{\Log Y}{2\pi i},\quad-\pi<\Arg Y<0.
 \tag{10}
\]
Use the original critical point and phase
\[
\begin{split}
 v(v-X)(v-Y)&=X(v-1)^3,\qquad t=\frac{\Log v}{2\pi i},\\
 \Theta(a,y)&=Q(t;a,y),\\
 Q(t;a,y)&=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat .
\end{split}
\tag{11}
\]
The [unit incoming branch theorem](research_mixed_four_conditional_unit_incoming_branch.md)
retains the original zero logarithmic lift and
\(0<\Re t<1-a\).
The [endpoint factorization](research_mixed_four_conditional_unit_endpoint_factorization.md)
gives, uniformly for \(Y\in K\), with \(\delta=1-a\),
\[
                         t=\delta+O_K(\delta^3).
 \tag{12}
\]
Consequently \(t\to0\), \(a+t\to1\), and \(a\to1\).
The two approaches to one are inside the same original strip.
Equations (5) and (8) therefore imply
\[
                 g(a+t)-g(a)\longrightarrow g_1-g_1=0,
                 \qquad g(t)\longrightarrow0 .
 \tag{13}
\]
The set of \(y\) corresponding to \(K\) is a compact subset of
the regular outgoing strip. Hence
\(g(y+t)-g(y)\to0\) uniformly there. Also \(at\to0\).
All terms in (11) now give
\[
                       \lim_{a\uparrow1}\Theta(a,y)=0
                         \quad\hbox{uniformly for }Y\in K .
 \tag{14}
\]
This is the original complex phase itself, without a new additive
normalization. The endpoint values of \(g\), its original \(g(0)=0\),
and the same logarithmic lift are essential to (14).

## 3. Uniform real-action expansion and positivity

The endpoint factorization, on the original root, gives
\[
 v=X+(1-X)^3f(X,Y),\qquad f(1,Y)=\frac1{Y-1},
 \qquad
 \frac{v-X}{1-X}=(1-X)^2f(X,Y).
 \tag{15}
\]
The function \(f\) is uniformly bounded and bounded away from zero
on a fixed neighborhood of \(\{1\}\times K\).
Its already proved stationary derivative formula is
\[
 \partial_a\Re\Theta(a,y)
 =2\log\bigl(2\sin(\pi\delta)\bigr)
               -\log|1-Y|+O_K(\delta).
 \tag{16}
\]
Set \(F(\delta,Y)=\Re\Theta(1-\delta,y)\). By (14), \(F(0,Y)=0\).
Since \(\sin(\pi\delta)/(\pi\delta)=1+O(\delta^2)\),
equation (16) gives the uniformly integrable derivative
\[
 \partial_\delta F
       =-2\log(2\pi\delta)+\log|1-Y|+O_K(\delta).
 \tag{17}
\]
Integrate from zero, using (14). The result is
\[
 \boxed{\quad
 \Re\Theta(a,y)
   =-2\delta\log(2\pi\delta)+2\delta
                  +\delta\log|1-Y|+O_K(\delta^2),
       \qquad\delta=1-a\downarrow0 .
 \quad}
 \tag{18}
\]
The error estimate is uniform on \(K\). The constant in this
formula is fixed by (11)--(14); it is not chosen by integrating
the derivative with an unspecified constant.

Finally the
[whole-unit-arc multiplier theorem](research_mixed_four_conditional_unit_multiplier.md)
proves, on the entire domain (9)--(10),
\[
        \partial_a\Re\Theta=\log\left|\frac{v-X}{1-X}\right|<0 .
 \tag{19}
\]
A strictly decreasing function with terminal limit zero is
strictly positive before that endpoint. Thus
\[
                       \Re\Theta(a,y)>0,\qquad 1/2\le a<1.
 \tag{20}
\]
Its positive lower bound is uniform on every compact parameter
family whose incoming coordinate stays below one.
Neither (18) nor (20) compares a finite conditional sum, physical
end block, cap profile, Fourier alternative or contour connector
with a geometric supporting plane. Those source obligations remain
separate, as does any whole-period or whole-word conclusion.

## Direct source versions

| Direct source | SHA-256 |
|---|---|
| research_mixed_four_conditional_positive_incoming_action.md | e8608019efbd73b2c05e6ede084b4781182259dc0e32be12b4610c66f352d371 |
| research_mixed_four_conditional_unit_incoming_branch.md | b6c8fdaffd436ec82670ec864629d93d36e7c7a8ae7e81033b684e3f86e92e43 |
| research_mixed_four_conditional_unit_endpoint_factorization.md | 7eeb4d3188955e37029875d8612cb235dbf9fc0118828b5818c52ed0e8fad33d |
| research_mixed_four_conditional_unit_multiplier.md | 4d73d90557948056413ef0445cb7754569cbbc03e7ff3f35ecab0f3e9fe8f66f |

The whole written proof and all directly used source implications
were read in full; all four source bindings were checked.
Independent proof/direct-source review is required before adoption.
No mathematical numerical evaluation, saved-value
arithmetic, test, import, compilation or frozen-source edit is used.
