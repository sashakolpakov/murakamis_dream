# The boundary alias has exactly the geometric exponential rate

Research note, 2 November 2026.

In the contour problem for two adjacent powers equal to two, the
phase on one boundary at infinity is
\[
 V(v)=-6J(v)+J(2v)+i\pi v^2-i\pi/6.
 \tag{1}
\]
The [exact cyclotomic normalization](research_adjacent_pair_cyclotomic_gauge.md)
derives this phase from the first coefficient of the original
lower correction kernel; it also distinguishes that kernel
from its single-valued normalization.
Here \(J\) has the same canonical branch as in
[the adjacent-pair calculation](research_adjacent_two_crossing_pair.md).
This note proves an exact identity between the real critical
values of \(V\) and the original two-variable phase \(W\).
The equality is a consequence of four elementary five-term
dilogarithm identities.

Thus this boundary contribution cannot be discarded by a strict
inequality between the two real actions. The result does not
determine its coefficient in the actual contour decomposition,
the power of \(N\) multiplying it, or its cancellation with other
contributions.

## 1. The two critical points

To avoid using the quantum parameter for an algebraic number, put
\[
 \delta=i\sqrt7,\qquad
 z=\frac{1+\delta}{4},\qquad
 X=\frac{5+\delta}{16},\qquad Y=\frac{\delta}{7}.
 \tag{2}
\]
Then
\[
 2z^2-z+1=0,\qquad X=-z^3=\frac{1+z}{4},
 \qquad Y=\frac{z}{2-z}.
 \tag{3}
\]
The finite critical point is
\[
 x_*=\frac{\log X}{2\pi i},\qquad
 y_*=\frac{\log Y}{2\pi i},
 \tag{4}
\]
with arguments in \((0,\pi)\). Its unexponentiated critical
equations have already been checked in the adjacent-pair
calculation.

The boundary phase has a critical point
\[
 v_*=\frac{\log z}{2\pi i}.
 \tag{5}
\]
To check its logarithmic lift, use
\[
 V'(v)=2\bigl[
       \log z+\log(1+z)-2\log(1-z)-i\pi\bigr],
 \qquad z=e^{2\pi iv}.
 \tag{6}
\]
Equation (3) gives \(z(1+z)/(1-z)^2=-1\).
The argument of \(z\) and that of \(1+z\) lie in \((0,\pi/2)\),
whereas the argument of \(1-z\) lies in \((-\pi/2,0)\).
The argument sum in the brackets before subtraction of \(i\pi\)
is therefore strictly between zero and \(2\pi\), and must equal
\(\pi\). Its real part is zero. This proves \(V'(v_*)=0\) on
the actual canonical branches.
The second derivative is
\[
 V''(v_*)=\frac{\pi}{2}(-5\sqrt7+7i),
 \tag{7}
\]
so this one-variable critical point is nondegenerate.

**Proposition.** With these branches,
\[
 \boxed{\operatorname{Re}V(v_*)
       =\operatorname{Re}W(x_*,y_*).}
 \tag{8}
\]
The equality concerns the actual real values, with no unspecified
additive real constant.

## 2. Reduction of critical actions to the Bloch--Wigner function

Define
\[
 D(w)=\operatorname{Im}\operatorname{Li}_2(w)
               +\log|w|\arg(1-w).
 \tag{9}
\]
The continuous extension is single-valued on
\(\mathbb C\setminus\{0,1\}\) and zero on the real axis.
For arguments in the unit disk, the dilogarithm in (9) is its
convergent power series; the formula elsewhere is its continuous
Bloch--Wigner extension.

At the critical points above,
\[
 \begin{aligned}
 2\pi\operatorname{Re}W(x_*,y_*)
       &=3D(X)+6D(Y)-D(Y^2)-D(XY),\\
 2\pi\operatorname{Re}V(v_*)
       &=6D(z)-D(z^2).
 \end{aligned}
 \tag{10}
\]
In the first line \(Y^2=-1/7\), so its \(D\)-term vanishes.
We give the normalization check, since an identification only
of derivatives would be insufficient here.

Write \(x=\xi+ih,\ y=\eta+ik\), and set
\(a_w=\arg(1-w)\). The canonical expansion
\[
 J(t)=\frac{i\pi}{2}t(1-t)
       +\frac{\pi^2/6-\operatorname{Li}_2(e^{2\pi it})}{2\pi i}
 \tag{11}
\]
gives
\[
 \begin{split}
 2\pi\operatorname{Re}W
 ={}&3\operatorname{Im}\operatorname{Li}_2(X)
       +6\operatorname{Im}\operatorname{Li}_2(Y)
       -\operatorname{Im}\operatorname{Li}_2(Y^2)
       -\operatorname{Im}\operatorname{Li}_2(XY)\\
 &+2\pi\bigl[(-4\pi h+2\pi k)\xi
              +(2\pi h-2\pi k)\eta+\pi k\bigr].
 \end{split}
 \tag{12}
\]
The imaginary parts of the two actual critical equations are
\[
 a_{XY}-3a_X+2\pi(2\xi-\eta)=0,\qquad
 a_{XY}-6a_Y+2a_{Y^2}+2\pi(-\xi+\eta)-\pi=0.
 \tag{13}
\]
Multiply them by \(\log|X|=-2\pi h\) and
\(\log|Y|=-2\pi k\), respectively. The resulting logarithmic
corrections in (9) are precisely the second line of (12).
This proves the first line of (10).

For \(v=\theta+i\ell\), expansion (11) gives
\[
 2\pi\operatorname{Re}V
 =6\operatorname{Im}\operatorname{Li}_2(z)
      -\operatorname{Im}\operatorname{Li}_2(z^2)
      -4\pi^2\ell(2\theta-1).
 \tag{14}
\]
The imaginary part of \(V'(v_*)=0\) is
\[
 6a_z-2a_{z^2}=2\pi(2\theta-1).
 \tag{15}
\]
Multiplication by \(\log|z|=-2\pi\ell\) supplies exactly the
last term of (14), proving the second line of (10).

## 3. Four five-term relations

We use the symmetries
\[
 \begin{gathered}
 D(\bar w)=-D(w),\qquad D(1-w)=-D(w),\qquad
 D(1/w)=-D(w),\\
 D(w)=D(1/(1-w))=D((w-1)/w),
 \end{gathered}
 \tag{16}
\]
and the five-term identity in the form
\[
 D(r)+D(s)=D(rs)
       +D\!\left(\frac{r(1-s)}{1-rs}\right)
       +D\!\left(\frac{s(1-r)}{1-rs}\right).
 \tag{17}
\]
Only instances with all denominators nonzero are used.
These identities can be checked without any arithmetic
rigidity theorem. Indeed
\[
 dD(w)=\log|w|\,d\arg(1-w)
                   -\log|1-w|\,d\arg w.
 \tag{18}
\]
Substitution of the three rational arguments in (17) cancels
all derivatives. The constant is zero on letting \(s\) tend
to zero. Continuity gives the identity throughout the connected
complement of the exceptional algebraic sets. The symmetries
in (16) follow from the same differential calculation and
evaluation on the real axis.

Put
\[
 E=\frac{-1+\delta}{2},\qquad
 F=\frac{-5+\delta}{2},\qquad
 G=\frac{-3+\delta}{4}.
 \tag{19}
\]
Apply (17) to the following four ordered pairs. Each displayed
relation follows by substituting (2) and using (16).

| \(r\) | \(s\) | Relation |
| --- | --- | --- |
| \((7+\delta)/8\) | \((5-\delta)/4\) | \(D(Y)-2D(E)+D(F)+D(G)=0\) |
| \((7+\delta)/8\) | \(2\) | \(2D(Y)-D(G)-D(z)=0\) |
| \(\bar X\) | \(\bar X\) | \(-2D(X)+D(XY)+2D(F)=0\) |
| \(\bar X\) | \(2z\) | \(-D(X)+2D(z)-2D(E)=0\) |

For explicit verification, the three arguments on the
right-hand side of (17), in the same row order, are
\[
 \begin{array}{c|ccc}
 &rs&r(1-s)/(1-rs)&s(1-r)/(1-rs)\\ \hline
 1&(21-\delta)/16&(7-\delta)/4&(-1+\delta)/2\\
 2&(7+\delta)/4&(7-\delta)/8&(1+\delta)/4\\
 3&(9-5\delta)/128&(7-\delta)/28&(7-\delta)/28\\
 4&(3+\delta)/8&(1-\delta)/4&(-1+\delta)/2 .
 \end{array}
 \tag{20}
\]
This table also makes every denominator and symmetry check
finite and explicit.

The fourth relation gives \(D(E)=D(z)-D(X)/2\); the second
gives \(D(G)=2D(Y)-D(z)\). Inserting both in the first gives
\[
 D(F)=3D(z)-D(X)-3D(Y).
 \]
The third now yields
\[
 D(XY)=4D(X)+6D(Y)-6D(z).
 \tag{21}
\]
Finally,
\[
 \frac1{\overline{z^2}}=\frac{X-1}{X},
 \]
so (16) implies \(D(z^2)=D(X)\). Equation (21) becomes
\[
 3D(X)+6D(Y)-D(XY)=6D(z)-D(z^2).
 \tag{22}
\]
Equations (10) and (22) prove (8).

## 4. Consequence and remaining phase question

The finite saddle and the boundary alias have the same real
action by an exact identity. Therefore a proposed estimate
that assigns this entire boundary a strictly smaller
exponential rate needs additional cancellation; a comparison
of the two critical values cannot provide it.

Equation (8) does not determine the imaginary difference of
the two actions. The Bloch--Wigner identities deliberately
discard that information. In particular, this note does not
use a numerical value of that difference to infer a phase
factor in the finite quantum sum. A full comparison of the
complex phases would require lifting the four relations with
their logarithmic branches and retaining the corresponding
constants.

The algebraic witness is independently reproducible with
[this exact-arithmetic script](../experiments/verify_adjacent_alias_bloch_identity.py).
It checks the four pentagon substitutions, their reductions
under (16), and the linear combination giving (22), without
numerically evaluating a dilogarithm. Its saved output is
[here](../repro/results/research-adjacent-alias-bloch-identity.json).
