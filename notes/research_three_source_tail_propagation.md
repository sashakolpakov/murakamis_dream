# A quantitative source propagation criterion after finite preparation

Research note, 4 November 2026. Frozen manuscripts are unchanged.

This gives a conditional theorem with explicit, testable global
inequalities. The analytic phase class, the retained input-rectangle
packet, and both global kernel envelopes are proved inputs. An
entrance source packet and envelope in the small-gradient class
specified below must still be supplied.
In particular, three contractions of a phase do not by themselves
prove three contractions of an original quantum source.

## 1. Constants and the required original-source bounds

Keep \(x_h,k_0,\rho\) and the exact retained phase \(\Phi\)
from [the analytic phase theorem](research_three_phase_graph_transform.md).
Set
\[
 R=1/200,\quad r=1/100,\quad H_*=1/2500,\quad
 A=29/20,\quad a=3/2,\quad B=13,
 \qquad v(t)=\min\{\operatorname{dist}(t,\mathbb Z),r\}.
 \tag{1}
\]
Use exactly the \(L=\lfloor N/40\rfloor\) retained kernel
\(K_N=\widetilde V_N^{(40)}\). Its proved
[input-rectangle packet](research_three_vertex_input_rectangle.md)
supplies the original nonzero \(\kappa N^{-1/2}a_K e^{N\Phi}\)
packet on real input displacement at most \(r\), imaginary input
displacement at most \(R\), and complex output displacement at most
\(R\). All its finite indices, currents, and parity factors remain
in that theorem.

The [global capped Gaussian theorem](research_three_vertex_capped_gaussian_bound.md)
and the [joint weighted-height theorem](research_three_vertex_weighted_height_bound.md)
prove the following two **joint kernel bounds**. In the first one
we weaken the proved coefficient \(8/5\) to \(a=3/2\):
\[
 \begin{split}
 |K_N(x_h+t,x_h+u)|&\le CN^q
 e^{N[2c-a\{v(t)^2+v(u)^2\}]},\\
 |K_N(x_h+t,x_h+w)|&\le CN^q
 e^{N[2c+B(\Im w)^2-a v(t)^2]},
 \qquad t,u\in\mathbb R,\quad |w|\le R.
 \end{split}
 \tag{2}
\]
The second bound cannot be obtained by adding the separate real-angle
loss and the unweighted height bound. It is a joint assertion about
the exact kernel, including its mixed angle-height terms.

An entrance source is an actual finite half-band function \(F_N\),
with the same period sign as \(h(x)\), satisfying these two conditions.
First it has a nonzero holomorphic packet
\[
 F_N(x_h+z)=\omega_N N^\nu b(z)e^{NS(x_h+z)}(1+O(N^{-1})),
 \quad |z|\le R,
 \tag{3}
\]
on a neighborhood of the closed disk. The unit factor \(\omega_N\),
ordinary boundary parameters, and original first normals are retained.
Its actual phase satisfies
\[
 S'/k_0=-\sqrt{21}z+h(z),\qquad
 |h(0)|\le H\le H_*,\qquad \sup|h'|\le9/50.
 \tag{4}
\]
Second, on the full real wire period it obeys the explicit envelope
\[
 |F_N(x_h+t)|\le CN^q
       e^{N[M+|k_0|H v(t)-A v(t)^2]},\qquad M=\Re S(x_h).
 \tag{5}
\]
The number \(H\) is a certified upper bound, not necessarily the
exact gradient magnitude. These conditions are not an assumption that a desired Fourier
coefficient is nonzero: (3) is a local original-source packet, while
(5) is a prescribed global upper bound with fixed constants.

## 2. The normalization drift

Write \(D=5+\sqrt{21}\), and let
\[
 Z=\frac{\rho(1+1/20)}{1-3\rho/10}<47/200,
 \qquad
 C_0=\frac{|k_0|(D+3/5)}{2(D-3/5)^2}<.174.
 \tag{6}
\]
For the exact transformed phase \(S_+\) of the analytic theorem,
\[
 |S_+(x_h)-S(x_h)-2c|\le C_0H^2,
 \qquad |h_+(0)|\le ZH.
 \tag{7}
\]
To prove the first inequality, let \(z_c\) be the central critical
wire. Its exact equation gives \(|z_c|\le H/(D-3/5)\).
For \(T(z)=S(x_h+z)+\Phi(x_h+z,x_h)\), integration using
\(T'(z_c)=0\) gives
\[
 T(z_c)-T(0)=-z_c^2\int_0^1 s\,T''(sz_c)\,ds.
 \tag{8}
\]
The exact Hessian bound \(|T''|\le|k_0|(D+3/5)\) proves (7).
Thus the accumulated absolute normalization drift is at most
\(C_0H^2/(1-Z^2)\). For the actual initially prepared phase,
\(H<.028\), this is less than \(.000144\).

This drift must be paid relative to the actual evolving action.
Replacing every action increment by \(2c\) would discard precisely
this source-dependent cost.

## 3. Conditional full-source propagation

**Theorem 1.** For the proved kernel bounds (2), the input-rectangle
packet and its exact cubic phase bound, assume an entrance source
satisfying (3)--(5).
Then the literal finite-source attachment
\[
 F_{N,+}(y)=N\int_{x_h-1/2}^{x_h+1/2}F_N(x)K_N(x,y)\,dx
 \tag{9}
\]
has a nonzero holomorphic packet on \(|y-x_h|\le R\), with the
actual phase \(S_+\), the same power \(N^\nu\), and amplitude
\[
 \omega_N\kappa\,
 \frac{\sqrt{2\pi}\,b(z_c)a_K(x_h+z_c,y)}
       {\sqrt{-(S''+\Phi_{xx})(x_h+z_c,y)}}.
 \tag{10}
\]
It satisfies (4)--(5) again, with the certified bound \(H_+=ZH\),
\(M_+=\Re S_+(x_h)\), and the same constants in (1).
The conclusion iterates for every fixed number of attachments.
All assertions retain both level parities and any ordinary boundary
parameters for which the hypotheses hold uniformly holomorphically.

*Proof.* We give explicit estimates for all the complementary pieces.
The analytic theorem gives \(H_+\le ZH\), \(\sup|h_+'|<9/50\),
and \(-\Re(S''+\Phi_{xx})>18\). Its critical wire on the output
disk satisfies \(|z_c|<1/800\). Set \(r_c=3/625=.0048\).
The rectangle with real ends \(\pm r_c\) and heights between zero
and \(\Im z_c\) lies strictly in the input disk because
\(r_c^2+(1/800)^2<R^2\).

The needed exact phase bound on the input annulus is
\[
 \left|\Phi(x_h+t,x_h+w)-2c+
             \frac{k_0}{2}(5t^2-4tw+5w^2)\right|
 \le3|k_0|(|t|+|w|)^3,
 \quad |t|\le r,\quad |w|\le R.
 \tag{11}
\]
It follows from the independently verified Hessian-remainder bound in
[the input-rectangle note, Section 5](research_three_vertex_input_rectangle.md#5-a-quantitative-cubic-bound-for-the-original-phase),
\(|E_{ab}(z,w)|\le18(|z|+|w|)\), by integrating twice.
This is an estimate for the actual retained phase on its proved
source rectangle; it is not the weaker real-index modulus envelope.

Here are explicit one-variable comparisons that bound the annulus.
Put \(\alpha=\Re k_0\), \(s=|t|\), \(\lambda=3s/R\), and
\[
 Q(s)=\lambda R^2+
       \frac{s^2|k_0|^2(\lambda-\rho\alpha)}
                         {\lambda^2-\rho^2|k_0|^2}.
 \tag{12}
\]
Completing a real positive quadratic form on \(|w|\le R\)
gives \(\Re(2k_0tw-\rho k_0w^2)\le Q(s)\), for either sign
of \(t\). Indeed use the positive matrix
\(\lambda I+\rho\bigl(\begin{smallmatrix}\alpha&-\Im k_0\\
-\Im k_0&-\alpha\end{smallmatrix}\bigr)\).

For \(A_0>0\), define
\[
 \begin{split}
 E_{A_0}(s)={}&C_0H_*^2+|k_0|H_*s+|k_0|ZH_*R
       +\frac9{100}|k_0|R^2
       -(A_0+5\alpha/2)s^2+Q(s)\\
       &+3|k_0|(s+R)^3.
 \end{split}
 \tag{13}
\]
Outward scalar interval bounds give
\[
 E_4(s)<-10^{-6}\quad(r_c\le s\le R),\qquad
 E_A(s)<-10^{-6}\quad(R\le s\le r).
 \tag{14}
\]
On the first interval use the actual packet and
\(-\Re S''>8\); on the second use (5). In both cases use the
actual kernel packet, (7), (11), and the lower bound
\[
 \Re S_+(x_h+w)\ge M_+
 -|k_0|ZH_*R-\tfrac12\Re(k_0\sqrt{21}\,w^2)
                              -\tfrac9{100}|k_0|R^2.
 \tag{15}
\]
Thus every real input in these two annuli has a strict gap relative
to the actual output phase, uniformly on the complex disk.

For the far input \(v(t)=r\), apply the second estimate in (2)
and (5). Let
\[
 \Lambda_B=\frac{B+
       \sqrt{(\Re(k_0\sqrt{21})-B)^2+\Im(k_0\sqrt{21})^2}}2.
 \tag{16}
\]
This is exactly the maximum of
\(B(\Im w)^2+\frac12\Re(k_0\sqrt{21}w^2)\) divided by
\(|w|^2\). The remaining gap is at least
\[
 (A+a)r^2-|k_0|H_*r-C_0H_*^2-|k_0|ZH_*R
         -\tfrac9{100}|k_0|R^2-\Lambda_BR^2
                         >2\cdot10^{-6}.
 \tag{17}
\]
This retains the complex output-height cost; a real-period estimate
alone would not prove (17).

It remains to deform only the central input segment. At its real
endpoints, (14) supplies the phase gap. At the endpoints translated
to height \(\Im z_c\), horizontal concavity supplies a gap at
least \(9(r_c-1/800)^2\). At fixed real endpoint, the real phase
is convex in the imaginary height, because its second height
derivative is \(-\Re T''>18\). The entire vertical join therefore
has a gap. This exact contour deformation takes place inside the
disk on which both original packets are valid. The horizontal
central segment has its unique maximum at \(z_c\); Gaussian
integration gives (10). The complement estimates above are absolute
upper bounds, so cannot cancel that coefficient.

The literal measure \(N\,dx\), the retained factor \(N^{-1/2}\)
and the wire Gaussian \(N^{-1/2}\) leave \(N^\nu\) unchanged.
The product in (9) is period one at both parities. No source factor,
first normal or exact deleted corner has been replaced.

Finally, on real output wires the first bound in (2), (5), and
completion of the square give
\[
 |F_{N,+}(x_h+u)|\le CN^q
 e^{N[M_++\{C_0+|k_0|^2/(4(A+a))\}H^2-a v(u)^2]}.
 \tag{18}
\]
For \(v(u)\ge R\), the reset reserve is
\[
 (a-A)R^2-\{C_0+|k_0|^2/(4(A+a))\}H_*^2>10^{-6}.
 \tag{19}
\]
For \(|u|\le R\), the newly proved packet and its phase curvature
give the stronger upper bound with \(-4u^2\). Together these
prove (5) for the outgoing source. Strict compact margins give the
holomorphic remainder and the ordinary boundary derivatives.
\(\square\)

## 4. What finite preparation still has to provide

The actual first prepared phase has \(|h_1(0)|<.028\).
Three analytic transforms give
\[
              .028Z^3<.000358<H_*,
 \tag{20}
\]
and the derivative bound \(9/50\) is already preserved after
the first transform. Thus there are only three entrance attachments
before this quantitative stable regime, **provided their original
source packets have been established**. Equation (20) is not that
source theorem. The slightly larger certified initial bound
\(H_1=.03\) also gives \(.03Z^3<H_*\).

At entrance, (5) requires approximately a \(3.08\cdot10^{-5}\)
gap at real displacement \(.005\), and a \(1.34\cdot10^{-4}\)
gap on the full period at displacements at least \(.01\), relative
to the actual center action. The current quantified initial cap
packet supplies the disk but does not by itself supply the real
annulus or the three intervening source identifications. A broad
exterior bound alone does not cover that annulus either.

The exact corner-transfer theorem remains a separate final step
when converting a complete-ended product of retained vertices back
to the undeleted original word. This note uses the precise retained
source in every attachment and does not silently replace it by
\(JM^3\) with a Fourier endpoint.

The [scalar checker](../experiments/check_three_source_tail_propagation.py)
and [record](../repro/results/research-three-source-tail-propagation.json)
verify the explicit drift, annulus and reset margins. They do not
recertify the separately proved global kernel bounds (2), or certify
the still-required entrance source envelope and source attachments.

```sh
python3 experiments/check_three_source_tail_propagation.py --precision 192
```
