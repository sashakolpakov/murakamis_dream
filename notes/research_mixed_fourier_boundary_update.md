# An original boundary update for a fixed Fourier output

Research deduction, 7 November 2026. The last Fourier boundary equation
can be imposed by an explicit holomorphic update of one auxiliary
inverse leg. Its zeros, poles and logarithmic lift are controlled
analytically on the entire original type-four disk. One strict disk
inclusion remains to be checked before this gives existence for every
ordinary-cap prefix ending in four. No numerical evaluation is used.

## 1. Original disks and the update

Keep the original disks
\[
 D_3=\{|b-(.35-.01i)|\le .09\},\qquad
 D_4=\{|q-(.30-.052i)|\le .064\}.
 \tag{1}
\]
They and the original endpoint and two-leg maps are those of
[open-word localization](research_mixed_open_word_critical_localization.md).
Let \(x_0=x_{34}\), \(K=e^{2\pi ix_0}\), with the original
calibration and certified bounds
\[
 .18299<\Re x_0<.18301,\qquad .07871<\Im x_0<.07873
 \tag{2}
\]
from [the mixed interface](research_three_four_source_interface.md).
For an output \(y\) near \(x_0\), put \(Y=e^{2\pi iy}\).
Retain the original incidence and contracted edge
\[
\begin{split}
 \ell_q(y)&=2\pi iqy-
 \frac{\operatorname{Li}_2(Ye^{-2\pi iq})-\operatorname{Li}_2(Y)}
      {2\pi i}-\pi iy,\\
 G(q,b)&=g(q+b)-2g(q)-2g(b)+2\pi iqb .
\end{split}
 \tag{3}
\]
All derivatives in this note keep their original logarithmic lifts.

Set \(Q=e^{-2\pi iq}\). The exponentiated equation
\(G_q(q,b)=\partial_q\ell_q(y)\) solves exactly for
\[
 B_Y(q)=e^{-2\pi ib}
       =\frac{1-YQ}{Y+(1-2Y)Q}.
 \tag{4}
\]
Indeed the exponentials of its two sides are
\((1-QB)/(B(1-Q)^2)\) and \(Y/(1-YQ)\). Clearing denominators
gives (4), without a root choice.

There is a useful equivalent form:
\[
 Z_Y=-\frac{2iY}{1-Y}=\cot(\pi y)+i,\qquad
 C_Y(q)=Z_Y-\cot(\pi q),\qquad
 B_Y(q)=\frac{C_Y(q)-i}{C_Y(q)+i}.
 \tag{5}
\]
Here the convention is
\(\cot(\pi q)=i(1+Q)/(1-Q)\).

## 2. Whole-disk regularity and the zero logarithmic lift

**Lemma 1.** At \(y=x_0\), throughout the closed disk \(D_4\),
\[
                   \Re C_K(q)>\frac3{260}.
 \tag{6}
\]
Consequently \(B_K\) has no zero or pole there, takes its values
strictly in the lower half-plane, and
\[
 \beta_K(q)=-\frac{\operatorname{Log}B_K(q)}{2\pi i}
 \tag{7}
\]
is holomorphic on a neighborhood of \(D_4\), with
\(0<\Re\beta_K(q)<1/2\). The logarithm in (7) is the
principal one. These conclusions persist on a fixed output
neighborhood of \(x_0\).

*Proof.* The real coordinate of \(q\) lies in
\([59/250,91/250]\subset(0,1/2)\). The cotangent formula gives
\[
 0<\Re\cot(\pi q)\le\cot(59\pi/250)<6/5.
 \tag{8}
\]
For the last inequality, \(59\pi/250>18/25\), and
\(\tan x\ge x+x^3/3\) gives
\[
 \tan(59\pi/250)>
 \frac{18}{25}+\frac13\left(\frac{18}{25}\right)^3>\frac56.
\]
The tangent inequality follows by first using \(\tan x\ge x\)
and then integrating \(\tan' x=1+\tan^2x\).

Write \(\phi=2\pi\Re x_0\), \(\eta=2\pi\Im x_0\).
The original rational bounds (2), together with \(3.14<\pi<22/7\),
give
\[
 \sin\phi>\frac9{10},\qquad
 \cos\phi>\frac25,\qquad
 \cosh\eta<\frac87.
 \tag{9}
\]
Here are explicit elementary witnesses. One has
\(0<\pi/2-\phi<3/7\), so
\(\sin\phi>1-(3/7)^2/2=89/98>9/10\).
Also \(0<\phi<22/19\), and the alternating cosine bound yields
\[
 1-\frac{(22/19)^2}{2}
   +\frac{(22/19)^4}{24}-\frac{(22/19)^6}{720}-\frac25
       =\frac{40302128}{33873034320}>0 .
\]
Finally \(0<\eta<1/2\), and comparison of the positive series
with \(\sum_{j\ge0}(\eta^2/2)^j\) gives
\(\cosh\eta<(1-\eta^2/2)^{-1}<8/7\).
Thus
\[
 \Re Z_K=\Re\cot(\pi x_0)
   =\frac{\sin\phi}{\cosh\eta-\cos\phi}
       >\frac{9/10}{8/7-2/5}=\frac{63}{52}.
\]
Subtract (8); \(63/52-6/5=3/260\), proving (6).

In (5), neither \(C_K-i\) nor \(C_K+i\) can vanish, and
\[
       \Im B_K(q)=
       -\frac{2\Re C_K(q)}{|C_K(q)+i|^2}<0.
 \tag{10}
\]
This proves all branch assertions. Compactness and the strict
margin give a neighborhood, rather than only pointwise regularity.
\(\square\)

**Lemma 2.** The update satisfies the original equation
\[
        G_q(q,\beta_K(q))=\partial_q\ell_q(x_0)
                         \qquad(q\in D_4).
 \tag{11}
\]
The same identity holds on a fixed connected product neighborhood
of \(D_4\times\{x_0\}\), with \(K,\beta_K\) replaced by
\(Y,\beta_Y\).

*Proof.* Lemma 1 gives \(0<\Re b<1/2\). Therefore
\(0<\Re(q+b)<.864<1\); the arguments of every \(g'\) in
(11) stay in their original regular strips. Also the inherited
bound \(|K|e^{.024\pi}<.7\) gives \(|KQ|<.7\), so the
external logarithm \(\operatorname{Log}(1-KQ)\) is regular.
These properties persist on a neighborhood.

Equation (4) makes the exponential of the difference in (11)
equal to one. That analytic difference is consequently a constant
in \(2\pi i\mathbb Z\) on the connected disk. At the original
alternating pair \(q=q_4^*, b=q_3^*\), the calibrated shared-wire
identity from [the contracted phase](research_mixed_contracted_phase.md),
Section 5, makes it zero. The original pair belongs to
\(D_4\times D_3\); its exponential solves (4), and
\(0<\Re q_3^*<1/2\) identifies it with the branch (7).
This fixes the constant as zero. The same argument on a connected
product neighborhood proves the parameter assertion. No new
additive action constant or exponential root selection is used.
\(\square\)

## 3. The one remaining inclusion and its existence consequence

The additional sufficient condition is
\[
        \max_{q\in\partial D_4}
        |\beta_K(q)-(.35-.01i)|<.09 .
 \tag{12}
\]
This inequality is not proved by Lemma 1, and no sign for it is
asserted here. The maximum principle extends (12) to \(D_4\);
its strictness and compactness extend it to outputs near \(x_0\).
It is only a one-complex-variable boundary inclusion, with no
new canonical reference solve.

**Theorem 3, conditional only on (12).** Every nonempty positive
three/four prefix whose last type is four has an original-log
critical point with its ordinary left cap and Fourier output
\(y=x_0\). Its first private leg and endpoint auxiliary lie in the
original \(E,U\), all other legs lie in their original typed
disks, and it is unique even in the larger original convex product
\(E\times U\times Q^{2m-1}\). The critical point is simple and
continues holomorphically to a fixed output neighborhood.

*Existence.* Use the half-chain action and disjoint update groups
of [actual cap phase entrance](research_mixed_alternating_cap_phase_entrance.md),
Section 1, with an extra auxiliary external leg \(b\in D_3\).
Keep all original endpoint and interior vertex updates, using old
neighbor values, and append the update
\[
                           b\longmapsto\beta_Y(t_m).
 \tag{13}
\]
Its argument \(t_m\) belongs to \(D_4\), since the last type
is four. Condition (12) makes this a continuous self-map of the
compact convex product. Brouwer gives a fixed point. The vertex
updates give the original critical equations with a final
\(G(t_m,b)\) incidence. Lemma 2 replaces its \(t_m\)-derivative
by the derivative of \(\ell_{t_m}(y)\), exactly the desired
Fourier boundary equation. The auxiliary \(b\) is removed; no
stationarity in \(b\) is imposed or needed. At length one the
original ordinary-end map supplies its three unknowns and the
same added update, so no separate two-ordinary-end theorem is used.

*Uniqueness and simplicity.* The desired unreduced phase is
\[
 E(s_1,u)+\sum_{j=1}^m V_{\epsilon_j}(s_j,t_j)
       +\sum_{j<m}G(t_j,s_{j+1})+\ell_{t_m}(y),
 \tag{14}
\]
with the original \(E,V_\epsilon,G\) of the half-chain theorem.
On \(E\times U\times Q^{2m-1}\) at \(y=x_0\), its negative real
Hessian is greater than \((6\pi/49)I\).
Here is the exact allocation. Ignore quadratic imaginary chirps,
which contribute zero to this real Hessian, and write
\(V_J(z,z')=J(z+z')-J(z)-J(z')\).
For \(m\ge2\), the real-Hessian contributions in (14) are those of
\[
\begin{split}
 &B(s_1,u)+[J(s_1+t_1)-J(t_1)]
    +\sum_{j=2}^m V_J(s_j,t_j)
    +\sum_{j<m}V_J(t_j,s_{j+1})\\
 &\hspace{9mm}
   -\sum_{j<m}\epsilon_j[J(s_j)+J(t_j)]-J(s_m)
   +\ell_{t_m}(x_0).
\end{split}
 \tag{15}
\]
The last vertex has \(\epsilon_m=1\), so there is no leftover
positive own term at its unpaired last leg. The original
[open Hessian proof](research_mixed_open_word_hessian.md) gives
\(-\Re B''>(6\pi/49)I\),
\(-\Re V_J''>(\pi/8)I\) on \(Q^2\), and an attached-leg
cost \(>\pi/8\) from \(J(s_1+t_1)-J(t_1)\).
Every other nonlast leg has two pair incidences; the last leg has
its type-four vertex pair. All extra negative own terms are
nonnegative quadratic forms. Finally
\[
 -\Re\partial_q^2\ell_q(x_0)
 =-\frac{2\pi\Im(Ke^{-2\pi iq})}{|1-Ke^{-2\pi iq}|^2}>0
                      \qquad(q=t_m\in Q),
 \tag{16}
\]
because \(-1/2<\Re x_0-\Re q<0\). The argument
\(Ke^{-2\pi iq}\) stays in the lower half-plane throughout
\(Q\), so the original logarithm and dilogarithm stay regular
even where its modulus exceeds one. Thus the least available
cost is \(6\pi/49<\pi/8\).

For \(m=1\), the type is four and the phase is
\(E(s_1,u)+g(s_1+t_1)-g(s_1)-g(t_1)+\ell_{t_1}\).
The endpoint supplies the same \((s_1,u)\) cost. The summed
real coordinate exceeds \(1/2\), and the negative own \(J(t_1)\)
supplies \(>\pi/8\) on the last leg. This proves the same bound.
Straight-segment accretivity proves injectivity of the full complex
gradient. The implicit function theorem and uniqueness give its
holomorphic continuation. \(\square\)

## 4. Source scope

The theorem concerns the actual critical phase for every such
prefix. For the two-letter prefix \(34\) it supplies a candidate
actual phase for the exact
[prepared source](research_mixed_prepared_three_four_cap_source.md).
It does not yet place that root in the narrower source product
\(E_c\times T\times R^2\): the original private rectangle \(E\)
has heights outside \(E_c\), and the typed disks also exceed some
of those source-height ranges. An additional rigorous image
refinement would be needed for that particular packet domain.

Nor does critical existence pay any physical tail, revived endpoint,
vertical join or horizontal alias of the prepared finite source.
No whole prepared-message asymptotic, outgoing-period envelope,
cap nonvanishing or knot conclusion is inferred from (12).
