# Central contours and outer bounds for a larger three-crossing source class

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This proves the central contour, the adjacent real annulus, the far
input bound, and the real-period reset budget for a larger source
class. It deliberately leaves the intermediate input interval
\(.009\le |t|\le .02\) to its separate comparison. All integrals
below contain the original finite source and the literal L40 kernel.

## 1. Hypotheses and the actual critical phase

Use the established \(x_h,k_0,\rho,c\), and put
\[
 R=1/200,\quad W=9/1000,\quad L=1/50,\quad
 H_*=57/10000,\quad b=9/50,\quad A=29/20,\quad a=3/2,
 \qquad v(t)=\min\{\operatorname{dist}(t,\mathbb Z),3/100\}.
 \tag{1}
\]
Let \(F_N\) be an actual finite half-band function with a nonzero
holomorphic packet near the union of the disk \(|z|\le R\) and
the real interval \([-W,W]\):
\[
 F_N(x_h+z)=\omega_NN^\nu f(z)e^{NS(x_h+z)}(1+O(N^{-1})),
 \quad f\ne0,\quad
 S'(x_h+z)/k_0=-\sqrt{21}z+h(z),\quad
 |h(0)|\le H\le H_*,\quad |h'|\le b.
 \tag{2}
\]
Assume its actual whole-period bound is
\[
 |F_N(x_h+t)|\le CN^q
 e^{N[M+|k_0|H v(t)-A v(t)^2]},\qquad M=\Re S(x_h).
 \tag{3}
\]
These are source hypotheses, not consequences of a spectral norm.
They include any original boundary parameters and first normals for
which the hypotheses hold uniformly on fixed neighborhoods.

Let \(K_N=\widetilde V_N^{(40)}\). The
[union-domain packet](research_three_vertex_real_input_union.md)
supplies its actual nonzero \(\kappa N^{-1/2}a_Ke^{N\Phi}\)
packet for real input displacement at most \(.02\), with output
in the disk/interval union above. On complex input in the true disk
and real output in the interval, use the exact finite symmetry of
\(K_N\), including its symmetric deleted corner. The earlier
bidisk packet supplies two complex disk variables.

The [larger analytic phase class](research_three_larger_phase_class.md)
defines the same selected transform
\[
 S_+(x_h+w)=S(x_h+z_c(w))+\Phi(x_h+z_c(w),x_h+w),
 \quad S_+'(x_h+w)/k_0=-\sqrt{21}w+h_+(w).
 \tag{4}
\]
It gives \(|h_+(0)|\le ZH\), \(|h_+'|<b\) on the union, where
\[
 D=5+\sqrt{21},\qquad
 Z=\frac{(21/20)\rho}{1-3\rho/10},\qquad
 C_0=\frac{|k_0|(D+3/5)}{2(D-3/5)^2},\qquad
 |\Re S_+(x_h)-M-2c|\le C_0H^2.
 \tag{5}
\]
The last estimate is the original critical-action drift from
[the source transport proof](research_three_source_tail_propagation.md),
and remains valid under the stronger hypotheses (2).

## 2. A uniform central contour and the near annulus

**Lemma 1.** For every output in the union, the true critical input
lies in the source disk. More precisely,
\[
 \begin{array}{ll}
 |z_c|<r_D:=7/4000,& |w|\le R,\\
 |z_c|<r_R:=27/10000,\quad
 |z_c-\rho w|<r_\Delta:=1/1250,&w\in[-W,W].
 \end{array}
 \tag{6}
\]
The two straight segments from \(-R\) to \(z_c\) and from
\(z_c\) to \(R\) give an oriented central saddle contour inside
the actual disk. Each real endpoint has action at least \(1/80000\)
below \(\Re S_+(x_h+w)\). The two adjacent real intervals
\(R\le |t|\le W\) retain that strict action loss.

*Proof.* Normalize the kernel gradient as
\(\Phi_x/k_0=-5z+2w+R_x(z,w)\). The exact critical equation is
\[
 z=\rho w+\frac\rho2\{h(z)+R_x(z,w)\}.
 \tag{7}
\]
On the bidisk, \(|R_x|\le.1(|z|+|w|)\) and its input
derivative is at most \(.1\). Thus (7) is a contraction of
the radius-\(r_D\) disk into itself: the exact scalar check is
\[
 \rho R+\frac\rho2\{H_*+br_D+.1(r_D+R)\}<r_D.
 \tag{8}
\]
For real \(|w|\le W\), the
[cubic phase estimate](research_three_vertex_input_rectangle.md#5-a-quantitative-cubic-bound-for-the-original-phase),
used with the variables exchanged, gives
\(|R_x|\le9(|z|+|w|)^2\). Its Hessian bound is at most
\(.26\) on the full input disk. The contractions and strict
scalar comparisons
\[
 \rho W+\frac\rho2\{H_*+br_R+9(r_R+W)^2\}<r_R,
 \qquad
 \frac\rho2\{H_*+br_R+9(r_R+W)^2\}<r_\Delta
 \tag{9}
\]
prove the real-output bounds in (6). Both contractions have norm
less than \(1/20\), and select the branch in (4).

Write \(T(z,w)=S(x_h+z)+\Phi(x_h+z,x_h+w)\).
On the central contour,
\[
 |-T_{zz}-k_0D|\le\epsilon|k_0|,
 \qquad \epsilon=.28\text{ for disk output},\quad
 \epsilon=.44\text{ for real output}.
 \tag{10}
\]
We give an explicit sector estimate rather than assuming a horizontal
contour works for every possible incoming gradient. Put
\[
 \Gamma(q)=\frac2{\sqrt7}(1-2q^2)
              -2\sqrt{\frac37}\,q\sqrt{1-q^2}.
 \tag{11}
\]
If \(d=d_0-\delta\), \(d_0\) is nonzero real and
\(|\delta|\le r<|d_0|\), then
\(|\arg(\operatorname{sgn}(d_0)d)|\le\arcsin(r/|d_0|)\).
Since \(\Re k_0/|k_0|=2/\sqrt7\) and
\(|\Im k_0|/|k_0|=\sqrt{3/7}\), it follows that
\[
 \Re(k_0D d^2)-\epsilon|k_0||d|^2
 \ge |k_0|(|d_0|-r)^2
       \{D\Gamma(r/|d_0|)-\epsilon\}.
 \tag{12}
\]
In the disk case take \(|d_0|=R,r=r_D\). In the real case
take \(d_0=\pm R-\rho w,r=r_\Delta\) and use
\(|d_0|\ge R-\rho W\). The right side decreases as the ratio
increases on these ranges. Outward scalar arithmetic gives the
respective lower bounds \(.00003115\) and \(.00004055\), both
strictly larger than \(1/40000\). Here and below the displayed
decimal lower bounds are rounded down; the checker retains the
full balls. Consequently, for \(d_\pm=\pm R-z_c\),
\[
 \Re[-T_{zz}(z,w)d_\pm^2]>1/40000
 \tag{13}
\]
throughout either straight segment. Twice integrating from the
critical point proves the endpoint loss and strict decrease along
each segment. The rays have opposite real displacements and lie
in opposite convergence sectors; local rounding therefore gives
the full oriented Gaussian coefficient.

The endpoint real derivatives point outward as well. Indeed
\(\Re(k_0D d_\pm^2)>0\),
\(\operatorname{sgn}(\Re d_\pm)=\pm1\), and
\(|\arg k_0|<\pi/4\) imply
\(|\arg(\pm k_0D d_\pm)|<3\pi/8\). Thus
\(\pm\Re(k_0D d_\pm)>D|k_0||d_\pm|/3\).
Integrating (10) once and using \(D/3>.44\) gives
\(\Re T_z(-R,w)>0\), \(\Re T_z(R,w)<0\).

For disk output and real \(|t|\le W\), the exact Hessian estimate
on the input rectangle gives
\[
 -\Re T_{tt}\ge(\Re k_0)D
           -|k_0|\{b+18(W+R)\}>18.
 \tag{14}
\]
For real output, (2) gives \(-\Re S''>9\), and the
[exact real-curvature cover](research_three_first_entrance_real_extension.md)
gives \(-\Re\Phi_{xx}>9.4\), hence again \(-\Re T_{tt}>18\).
The endpoint signs now imply monotone decrease on the two outward
real annuli. Both actual packets are valid there. Their original
polynomial factors and fixed derivatives retain the strict gap.
\(\square\)

In particular the central integral alone has the nonzero packet
\[
 N\int_{x_h-R}^{x_h+R}F_N(x)K_N(x,x_h+w)\,dx
 \sim\omega_N\kappa N^\nu
 \frac{\sqrt{2\pi}\,f(z_c)a_K(x_h+z_c,x_h+w)}
      {\sqrt{-(S''+\Phi_{xx})(x_h+z_c,x_h+w)}}e^{NS_+(x_h+w)},
 \tag{15}
\]
with relative error \(O(N^{-1})\) and the original square-root
branch. The literal measure \(N\), kernel power \(N^{-1/2}\),
and Gaussian power \(N^{-1/2}\) leave \(N^\nu\) unchanged.

## 3. The far original input and the real reset budget

**Lemma 2.** The part of the actual attachment with
\(\operatorname{dist}(t,\mathbb Z)\ge L=.02\) has upper rate
at least \(1/2500\) below \(\Re S_+(x_h+w)\), uniformly on
the output union.

*Proof.* Use (3) and the proved
[joint height bound with input cap .04](research_three_vertex_large_cap_height_bound.md).
Its input loss is at least \(a v(t)^2\). Since
\(|k_0|H_*-2(A+a)L<0\), the combined input loss is at least
\[
             Q=(A+a)L^2-|k_0|H_*L.
 \tag{16}
\]
For complex disk output the kernel also costs
\(13(\Im w)^2\); for real output this cost vanishes.
The actual outgoing phase in (4)--(5) obeys
\[
 \Re S_+(x_h+w)\ge M+2c-C_0H^2-|k_0|ZH|w|
 -\tfrac12\Re(k_0\sqrt{21}\,w^2)-\tfrac b2|k_0||w|^2.
 \tag{17}
\]
For disk output define
\[
 \Lambda=\frac{13+
  \sqrt{(\Re(k_0\sqrt{21})-13)^2+\Im(k_0\sqrt{21})^2}}2.
 \tag{18}
\]
This is exactly the largest eigenvalue of
\(13(\Im w)^2+\frac12\Re(k_0\sqrt{21}w^2)\)
relative to \(|w|^2\). The costs relative to (17) are bounded by
\[
 \begin{split}
 B_D&=C_0H_*^2+|k_0|ZH_*R+\tfrac b2|k_0|R^2+\Lambda R^2,\\
 B_R&=C_0H_*^2+|k_0|ZH_*W+
          \tfrac12\{\Re(k_0\sqrt{21})+b|k_0|\}W^2.
 \end{split}
 \tag{19}
\]
The exact scalar checks give
\(Q-B_D>.000563\) and \(Q-B_R>.000424\), both greater
than \(1/2500\). These estimates hold for the full original
period and any subset of the indicated far region. \(\square\)

**Lemma 3.** On outgoing real distances at least \(W\), the
literal full attachment already satisfies the prescribed outgoing
envelope with \(H_+=ZH\), center \(M_+=\Re S_+(x_h)\),
the same cap \(.03\), and coefficient \(A=1.45\).

*Proof.* The [two-wire real bound](research_three_vertex_two_wire_large_cap_bound.md)
and (3), followed by the input square completion and (5), give
\[
 \left|N\int F_N(x)K_N(x,x_h+u)\,dx\right|
 \le CN^q e^{N[M_++CH^2-a v(u)^2]},\qquad
 C=C_0+\frac{|k_0|^2}{4(A+a)}.
 \tag{20}
\]
It suffices that
\[
 CH^2\le |k_0|ZH W+(a-A)W^2\qquad(0\le H\le H_*).
 \tag{21}
\]
The difference of the left side and right side is convex in \(H\).
It is negative at zero, and at \(H_*\) the strict reserve exceeds
\(.00001061\). Thus (21) holds on the entire interval. The
right side increases with the outgoing distance, proving the claim.
The outgoing linear term is retained; dropping it would lose this
reset estimate. \(\square\)

The central coefficient (15) and Lemmas 1--3 do not yet estimate
the intermediate original input interval \(W\le |t|\le L\).
Once that separate comparison has been supplied, the local packet
also controls \(|u|\le W\) by its actual outgoing curvature, and
the pieces can be assembled. No such missing comparison is assumed
in the lemmas above.

## 4. Reproduction

```sh
python3 experiments/check_three_generic_source_outer_transport.py --precision 192
```

The [focused checker](../experiments/check_three_generic_source_outer_transport.py)
and [record](../repro/results/research-three-generic-source-outer-transport.json)
retain exact rational constants, outward self-map/sector/action
comparisons and the real-reset endpoints. The actual finite-kernel,
source and curvature premises have the independent proofs and
certificates linked above. This note changes none of those completed
artifacts and makes no full-chain or marked-volume assertion.
