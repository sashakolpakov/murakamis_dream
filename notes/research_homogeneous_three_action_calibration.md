# The exact geometric action of the homogeneous three-crossing point

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The positive homogeneous point of a degree-two path with power three
has geometric action
\[
 \operatorname{Re}\left\{\psi(t_*,t_*)+
                  \frac{3it_*^2}{4\pi}-it_*\right\}=2c,
 \qquad
 c=2\int_0^{5/6}\log(2\sin\pi x)\,dx.
 \tag{1}
\]
This is an identity for the original geometric phase. Its proof uses
the eight original tetrahedron shapes and the five-term identity for
the Bloch--Wigner dilogarithm. No quantum asymptotic or numerical
comparison of actions is used.

## 1. The original positive point and its shapes

Use the positive point and logarithmic calibration proved in Section 2
of the [bare-kernel calculation](research_bare_kernel_power_three_obstruction.md).
Write
\[
 t_*=a-iH,\quad
 \cos t_*=-\frac14+\frac{3\sqrt3}{4}i,\quad
 \frac{\pi}{2}<a<\frac{2\pi}{3},\quad H>0,
 \qquad v=\tan(t_*/2),\quad q=\sqrt{1+2v^2}.
 \tag{2}
\]
Its original branches satisfy
\[
 v^2=-\frac13-\frac{2i}{\sqrt3},\qquad
 q=\frac2{\sqrt3}-i,\qquad
 r=\operatorname{asinh}(\sin(t_*/2))
     =\frac{3H}{4}+i\left(\frac{3a}{4}-\frac{\pi}{2}\right).
 \tag{3}
\]
In particular \(3t_*+4ir=2\pi\) as an unexponentiated equation.

The four distinct original shapes are
\[
 A=\frac{q+v}{v-i},\quad
 B=-\frac{q-v}{v+i},\quad
 C=\frac{q-v}{v-i},\quad
 D_0=-\frac{q+v}{v+i}.
 \tag{4}
\]
The eight ordered tetrahedra have shapes
\[
             (A,B,-1/A,-1/B),\qquad
             (C,D_0,-1/C,-1/D_0).
 \tag{5}
\]
They are all positive by the cited positive-point proof. Put
\(\zeta=(1+i\sqrt3)/2\). Exact algebra in (3)--(4) gives
\[
 B=-1/A,\qquad D_0=-1/C,\qquad
 C=\frac{A-1}{A+1},\qquad A-\frac1A=\zeta.
 \tag{6}
\]
For the last relation, eliminating \(v\) from
\(A(v-i)=q+v\) and \(q^2=1+2v^2\) gives
\[
 A-\frac1A=\frac{2(q+i)}{q-i}
           =\frac2{1-i\sqrt3}=\zeta.
 \tag{7}
\]
The equation for \(C\) follows by cross multiplication and
\(q^2-2v^2=1\). Thus no root choice is inferred from a decimal
approximation.

## 2. The dilogarithm reduction

Let \(D(z)\) be the Bloch--Wigner dilogarithm, normalized by
\[
 D(z)=\operatorname{Im}\operatorname{Li}_2(z)
                        +\log|z|\arg(1-z),\qquad
 H_0(z)=D(z)-D(-z).
 \tag{8}
\]
The subscript distinguishes this function from the positive height
\(H\) in (2). The identities used below are
\[
 D(1/z)=-D(z),\qquad
 D(1/(1-z))=D(z),
 \tag{9}
\]
and
\[
 D(x)+D(y)=D(xy)
 +D\!\left(\frac{x-xy}{1-xy}\right)
 +D\!\left(\frac{y-xy}{1-xy}\right).
 \tag{10}
\]
These identities can be checked with the differential
\[
 dD(z)=\log|z|\,d\arg(1-z)-\log|1-z|\,d\arg z.
 \tag{11}
\]
For (10), substitute the three rational arguments into (11);
the coefficients of the logarithms of \(x,y,1-x,1-y,1-xy\)
cancel. The difference is constant on the connected complement
of their zero and pole divisors in \(\mathbb C^2\). It is zero
at \(0<x,y<1\), where all five dilogarithms are real and have
Bloch--Wigner value zero. Formula (9) follows by the same
one-variable calculation. The identities extend through other
real arguments by continuity.

Apply (10) with \(x=A\) and \(y=\zeta/A\). Equation (6), together
with \(\zeta(1-\zeta)=1\) and \(\zeta^3=-1\), gives
\[
 xy=\zeta,\qquad
 \frac{x-xy}{1-xy}=\frac{\zeta}{A}=y,\qquad
 \frac{y-xy}{1-xy}=\frac1{1+A}.
 \tag{12}
\]
For example, the product of the last fraction with \(1+A\) is
\(\zeta^2(1/A-A)=-\zeta^3=1\). Cancelling \(D(y)\) in (10)
and using (9) at \(-A\) proves
\[
                         H_0(A)=D(\zeta).
 \tag{13}
\]

The transformation \(w=(z-1)/(z+1)\) preserves \(H_0\) on the
upper half-plane. Here is its normalization as well as its
differential: equation (11) gives
\[
 dH_0(z)=\log|z|\,d\arg w-\log|w|\,d\arg z.
 \tag{14}
\]
Applying the transformation twice gives \(-1/z\), so substitution
in (14) shows \(dH_0(w)=dH_0(z)\). Both sides agree at \(z=i\),
where \(w=i\). Connectedness of the upper half-plane proves
the equality everywhere there. In particular, (6) gives
\(H_0(C)=H_0(A)\).

Using (5)--(6) and (9), the original volume is therefore
\[
 V_*=2H_0(A)+2H_0(C)=4D(\zeta).
 \tag{15}
\]
The tetrahedron of shape \(\zeta\) is regular and ideal. This
volume identity does not replace the original face identifications
by a new triangulation; it evaluates the original volume sum.

## 3. The action and its absolute constant

The [positive-edge volume identity](research_positive_edge_volume_identity.md)
retains the original complete constant and gives, at this point,
\[
 \begin{split}
 V_*
 &=2\pi\operatorname{Re}\psi(t_*,t_*)+4H\,\operatorname{Im}r\\
 &=2\pi\operatorname{Re}
           \left\{\psi(t_*,t_*)+\frac{3it_*^2}{4\pi}-it_*\right\},
 \end{split}
 \tag{16}
\]
by (3). Thus this is the actual stationary action, without an
undetermined additive real constant.

For completeness, put
\(\Lambda(\theta)=-\int_0^\theta\log|2\sin s|\,ds\).
On the unit circle (11) gives
\[
             D(e^{i\theta})=2\Lambda(\theta/2)
                         \quad(0\le\theta\le2\pi).
 \tag{17}
\]
Both sides vanish at \(\theta=0\), fixing the integration constant.
Also \(\Lambda(\pi-\theta)=-\Lambda(\theta)\), since the integral
of \(\log(2\sin s)\) over \([0,\pi]\) is zero. Consequently
\[
 \pi c=-2\Lambda(5\pi/6)=2\Lambda(\pi/6)=D(\zeta).
 \tag{18}
\]
Combining (15)--(18) proves (1).

The [exact algebra checker](../experiments/check_homogeneous_three_action_calibration.py)
verifies (6)--(7) and all rational substitutions in (12), using
polynomial remainders over the exact field containing \(i,\sqrt3\).
Its [record](../repro/results/research-homogeneous-three-action-calibration.json)
does not use numerical dilogarithm values. The differential and
normalization arguments above supply the functional identities.
