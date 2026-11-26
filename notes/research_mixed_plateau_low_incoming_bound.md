# Retaining an exact real edge in a low incoming bound

Research deduction, 5 November 2026. When the first terminal symbol is
already on the plateau, the established transport leaves its real edge
to the low middle symbol unchanged. Retaining that edge's actual
deficit gives a sharper explicit incoming upper bound than replacing
both marked edges by a uniform constant. The first terminal coordinate
is restricted to the plateau; this is not a uniform right-interface
comparison.

## 1. The marked edges remain fixed

Use the actual periodic reference, original allocated weights \(w_j\),
occupation \(\omega_j\), and incoming \(t^\theta\)-potential of
the [low-terminal theorem](research_mixed_low_terminal_incoming_bound.md).
An edge \(j\) joins \(j-1,j\), and a state at layer \(i\) has
positions \(i-2,i-1,i\). Set
\[
 d=\frac1{10},\qquad P=[.22,.45],\qquad
 \kappa=\frac1{4000},\qquad q_0=\frac{11}2,\qquad
 q_1=\frac{151}{20},\qquad c_j=\Im r_j.
 \tag{1}
\]
For two real targets define the unselected residual
\[
 W_j(u,v)=f_{\epsilon_{j-1},\epsilon_j}(u,v)
                            -\Re\Gamma_j(u,v).
 \tag{2}
\]
This is also the complete selected residual whenever both targets
are real in the half-period: their true corrections \(\chi\) vanish.

Consider a cyclic target having a marked coordinate \(x_{i-1}=d\)
and adjacent real coordinates
\[
                         x_{i-2}=y\in P,\qquad x_i=a_i=\Re r_i.
 \tag{3}
\]
Both edges \(i-1,i\) are real, since the marked coordinate has
left cutoff zero for every row. These two real coordinates and the
marked coordinate stay fixed throughout the proof of the original
cyclic occupation bound. Raising deeper coordinates to \(d\)
does not move (3). Right clamping moves only coordinates above .45.
The subsequent fixed-early transport leaves early positions fixed
and raises only other coordinates below .22; a plateau coordinate
already in \(P\) stays fixed. If one of these plateau positions
is an isolated position between two early ones, it is explicitly
fixed as well. Heights on the two marked edges remain zero throughout.

The completed real one-small comparison gives
\[
                     W_{i-1}(y,d)<-\frac{11}{200},\qquad
                     W_i(d,a_i)<-\frac{11}{200}.
 \tag{4}
\]
In the old early/plateau charging argument, each marked edge is used
only for loss \(1/100\) and its possible oriented plateau reset
credit. Thus its additional available surplus can be retained as
\[
 \begin{split}
 b^-_i(y)&=-W_{i-1}(y,d)-\frac1{100}-q_1c_{i-2}^2,\\
 b^+_i&=-W_i(d,a_i)-\frac1{100}-q_0c_i^2.
 \end{split}
 \tag{5}
\]
These are positive by (4) and the established height bounds. If the
corresponding plateau reset credit is unnecessary, reserving it in
(5) only makes the retained surplus smaller.

Compared with the surpluses already retained by the low-terminal
theorem, the gains in (5) are exactly
\[
 -W_{i-1}(y,d)-\frac{11}{200}>0,\qquad
 -W_i(d,a_i)-\frac{11}{200}>0.
 \tag{6}
\]
No old charge is enlarged or reassigned. In particular the full
early reserve and every clean plateau loss still pay precisely the
same occupations. Because the marked edge values themselves have
not changed during transport, (5) is available in the initial
cyclic inequality, not just at its final configuration.

## 2. The explicit incoming bound

Fix \(0<\rho\le.001\) and \(0<\theta<1\), and let
\[
 v=((y,\tau),(x,\sigma),(z,\zeta)),\qquad
 y\in P,\quad \rho\le x\le d,\quad \rho\le z\le1/2.
 \tag{7}
\]
Every selection is permitted by its type. Define the fixed real/complex
exit-edge residual
\[
 Z_i=\Re\!\left[
       \phi_{\epsilon_i,\epsilon_{i+1}}(a_i,r_{i+1})
                         -\Gamma_{i+1}(a_i,r_{i+1})\right].
 \tag{8}
\]
The first argument in (8) is real; the second is the full complex
reference. Both are unselected on this auxiliary exit.

**Theorem 1.** For every incoming history and every state (7),
\[
 \begin{split}
 H_i(v)\le\;&W_{i-1}(y,x)-Z_i+\frac1{50}
       +q_1c_{i-2}^2+q_0c_i^2\\
       &-\left(1-\frac\theta2\right)\kappa
                            -(1-\theta)\omega_{i-2}(y,\tau).
 \end{split}
 \tag{9}
\]
This retains the real first terminal coordinate and its actual
reference tangent. Its last symbol is arbitrary.

**Proof.** First take \(x=d\) and the last symbol equal to its
unselected baseline. Close any incoming history by appending three
baseline symbols, then enough baseline padding to align the original
period. Padding also makes the two marked edges distinct in the
closed repeated cycle, even for primitive periods one and two.
Apply the unchanged cyclic occupation proof while retaining (5).
The incoming weight plus its literal exit is at most
\[
 -(1-\theta)\sum_{\rm cycle}\omega-b^-_i(y)-b^+_i.
 \tag{10}
\]
The complete terminal occupation is at least
\(\omega_{i-2}(y,\tau)+\kappa\). The literal three-step exit is
\[
               E_i^{[3]}=W_i(d,a_i)+Z_i+\frac\theta2\kappa.
 \tag{11}
\]
Subtract (11) in (10), insert (5), and cancel the exact
\(W_i(d,a_i)\) term. This gives (9) at \(x=d\).
Taking the supremum over histories is legitimate because every
history has the same bound.

The [exact low transport theorem](research_mixed_exact_low_transport.md)
now replaces \(d\) by \(x\): its difference is precisely
\(W_{i-1}(y,x)-W_{i-1}(y,d)\). It also removes any restriction
on the last symbol, without an occupation charge for that unevaluated
symbol. This proves (9). No selected correction is omitted: those
on the two marked real edges vanish, and the first terminal selection
is retained in its occupation. \(\square\)

At \(x=d\), the improvement over the old constant-surplus incoming
bound, with the same first terminal \(y\), is exactly the nonnegative
sum in (6). The bound remains valid if that improvement is small;
no numerical assumption about the location of a maximizing history
is used.

## 3. Eliminating the plateau coordinate by explicit scalar maxima

The dependence on the first terminal real coordinate can also be
bounded without a grid of incoming histories. Fix its selection
\(\tau\), put \(a=\Re r_{i-2}\), \(s=1-\theta>0\), and define
\[
 C_i=-Z_i+\frac1{50}+q_1c_{i-2}^2+q_0c_i^2
                              -\left(1-\frac\theta2\right)\kappa,
 \qquad F_i(y)=W_{i-1}(y,d)-s\,\omega_{i-2}(y,\tau).
 \tag{12}
\]
After the exact low-interface reduction to \(x=d\), Theorem 1
is \(H_i\le C_i+F_i(y)\), for \(y\in P\).

The [real outer-support theorem](research_mixed_real_outer_support.md)
proves concavity of \(f(u,v)\) on the whole real half-square.
For any trial \(\xi\in(0,1/2)\), put
\[
 K_i(\xi)=
   f_{\epsilon_{i-2},\epsilon_{i-1},a}(\xi,d)
                  -\Re\phi_{\epsilon_{i-2},\epsilon_{i-1},a}
                                      (r_{i-2},r_{i-1}).
 \tag{13}
\]
This is the real derivative of \(W_{i-1}(\,\cdot\,,d)\) at
\(\xi\), with the actual complex reference tangent retained.
Concavity gives
\(F_i(y)\le W_{i-1}(\xi,d)+K_i(\xi)(y-\xi)
-s\omega_{i-2}(y,\tau)\).

Let \(I=[l,r]\subseteq P\). Define
\(\mathcal M(I;k)=\max_{y\in I}\{ky-s\omega_{i-2}(y,\tau)\}\).
It has the following exact evaluation. If \(\tau=1\), then
\(\omega=\kappa\) and
\(\mathcal M=\max\{kl,kr\}-s\kappa\).
If \(\tau=0\), split \(I\) at \(a-1/20,a+1/20\),
discarding empty pieces. On either outside piece the same affine
formula applies. On the central piece \(I_0=[l_0,r_0]\),
\[
 \begin{split}
 p&=\max\{l_0,\min\{r_0,a+5k/s\}\},\\
 \max_{y\in I_0}\{ky-s\omega(y,0)\}
      &=kp-\frac{s}{10}(p-a)^2.
 \end{split}
 \tag{14}
\]
Indeed \(\omega(y,0)=\min\{\kappa,(y-a)^2/10\}\) on \(P\),
and the derivative of the central quadratic is
\(k-s(y-a)/5\). The pieces agree in value at their boundaries.
Take the maximum of the at most three piece values. This procedure
also includes point intervals and a stationary point outside the
central piece; no division by a vanishing \(s\) occurs.

**Corollary 2.** Choose finitely many closed intervals \(I_\ell\)
covering \(P\), and one trial \(\xi_\ell\in(0,1/2)\) for each.
Then every state (7) with middle coordinate \(x=d\) satisfies
the uniform first-coordinate bound
\[
 H_i\le C_i+
  \max_\ell\left\{
    W_{i-1}(\xi_\ell,d)-K_i(\xi_\ell)\xi_\ell
                    +\mathcal M(I_\ell;K_i(\xi_\ell))\right\}.
 \tag{15}
\]
It is enough to apply the preceding tangent inequality on each
cover interval. All quantities in (15) are explicit scalar functions
of the actual reference and the chosen real trial values. Rational
trials can, for example, be chosen from the original one-small
real tangent certificate; their values and derivatives can be
enclosed using its completed real-root witnesses. Formula (15)
itself asserts no numerical enclosure for a right-interface
maximum. It retains every permitted first selection and applies
only to \(y\in P\).

## 4. Use in a right-interface comparison

If the low middle coordinate is the last A coordinate before an R-run,
combine (9) with the complete incident raw defect and any proved lower
value for the same incoming potential at the other end. The exact
transport and raw monotonicity already show that the low coordinate
can be set to \(d\). The resulting left contribution contains the
explicit real function \(W_{i-1}(y,d)\), with \(y\in P\), instead
of an uncomputed supremum over incoming histories.

The raw R terms retain all rows and both Fourier alternatives. The
auxiliary exit and incoming histories are phase comparisons only;
they do not introduce extra source factors or finite-source errors.
Any original finite integral application must still prove the remaining
interface inequality and spend a single tolerance over physical edges.
This note supplies no sign for arbitrary right interfaces, no bound
for a first terminal coordinate outside \(P\), and no whole-period
asymptotic or new knot-family theorem.

Reproduction:

    python3 experiments/check_mixed_plateau_low_incoming_bound.py

The focused checker verifies the retained-edge cancellation, the
scalar quadratic formula and the current completed inputs. It
does not recompute a root cover, optimize an incoming potential,
or test a uniform right-interface sign.
