# The inner three-critical branch on a fixed central rectangle

Private written phase continuation, 8 November 2026. No mathematical
numerical evaluation, saved-value calculation, or frozen-source edit
is used.

The selected critical point of the original inner three-kernel extends
through a fixed outer angular rectangle. A cubic gives its branch,
strict domain guards, original logarithmic charge, and nonzero reduced
Hessian. One existing complete edge packet applies on this critical
family. The full inner three-kernel on the enlarged rectangle is not
proved by this phase calculation.

## 1. Original phase and the continuation domain

Keep the original edge phase and its complete additive constant:
\[
 \psi_t(t,u)=-\frac1\pi
       \operatorname{arsinh}\{\tan(t/2)\cos(u/2)\}.
 \tag{1}
\]
This is the branch derived from the canonical Newton critical point
in [the edge-kernel proof, Section 1](research_bare_kernel_thin_rectangle.md).
Near the complete outer value the selected inner phase is
\[
 \Phi(t,u)=\psi(0,t)+\psi(t,u)+\frac{3it^2}{4\pi}-it.
 \tag{2}
\]
The original
[full single-three theorem, Sections 2 and 5](research_all_nonzero_degree_two_fillings.md)
fixes its critical point \(t_3=t(0)\), its action
\(S_3(0,0)\), and its finite-source coefficient on a small bidisk.
In particular that proof gives
\[
 0<\Re t_3<\pi/2,\quad \Im t_3<0,\quad
                    |\cos(t_3/2)|<1.
 \tag{3}
\]
The last inequality is the written cone-path consequence in its
Section 2, not a new evaluation of the saved root.

Consider the fixed closed outer rectangle
\[
 \mathcal U=\{u:|\Re u|\le\pi/2,\ |\Im u|\le1/2\},
 \qquad C=\cos(u/2).
 \tag{4}
\]
Its image lies in the rectangle
\[
 \mathcal C=\{C:1/\sqrt2\le\Re C\le17/16,\ |\Im C|\le1/4\}.
 \tag{5}
\]
Indeed \(\Re C=\cos(\Re u/2)\cosh(\Im u/2)\ge1/\sqrt2\);
\(\cosh(1/4)<17/16\); and
\[
 |\Im C|\le\frac1{\sqrt2}\sinh(1/4)<\frac14.
\]
For explicit elementary witnesses,
\[
 \cosh(1/4)\le1+\frac1{32}
            +\frac{1/6144}{1-1/480}<\frac{17}{16},
 \qquad
 \sinh(1/4)\le\frac14+\frac{1/384}{1-1/320}<\frac13,
\]
and \(1/\sqrt2<3/4\). The rational upper bounds are strict.
The branch guards proved below are also strict, so the conclusions
extend to a neighborhood of \(\mathcal U\).

**Theorem.** The original selected inner critical branch has a
holomorphic continuation \(t(u)\) to a neighborhood of \(\mathcal U\).
It satisfies
\[
 0<\Re t(u)<\pi/2,\qquad -1<\Im t(u)<0,\qquad
                         |\cos(t(u)/2)|<1.
 \tag{6}
\]
The original zero logarithmic charge is retained:
\[
 \operatorname{arsinh}(\tan(t/2))
 +\operatorname{arsinh}(C\tan(t/2))
                  =i(3t/2-\pi).
 \tag{7}
\]
The reduced critical Hessian \(\Phi_{tt}(t(u),u)\) is nonzero
throughout this compact family. The calibrated stationary action
continues holomorphically, with
\[
 \frac{d}{du}S_3(0,u)
       =-\frac1\pi\operatorname{arsinh}
                   \left(\frac{v(u)}2\tan(u/2)\right),
 \qquad v(u)=2\cos(t(u)/2).
 \tag{8}
\]
Its constant at zero is the original \(S_3(0,0)\).

These are statements about the original phase branch and its
nondegenerate critical point. They are not an extension of the full
finite three-kernel packet to \(\mathcal U\).

## 2. The exact cubic and its distinguished root

Set \(v=2\cos(t/2)\). Equation (7) implies
\[
 \boxed{\qquad
   v^3-2iv^2-3v+2i-2C=0.
 \qquad} \tag{9}
\]
Here is a derivation that also records its possible logarithmic
ambiguity before the lift is checked. Write
\[
 w=e^{it/2},\quad T=\tan(t/2),\quad
 A=\operatorname{arsinh}T,\quad
 B=\operatorname{arsinh}(CT).
\]
On the original branch,
\[
 T=-i\frac{w^2-1}{w^2+1},\qquad
 e^A=-i\frac{w+i}{w-i}.
\]
Exponentiating (7) gives \(e^{A+B}=-w^3\). Therefore
\[
 e^B=-i w^3\frac{w-i}{w+i},\qquad
 C=\frac12(w^3+w^{-3})-i(w^2+1+w^{-2})
   =\frac12(v^3-3v)-i(v^2-1).
 \tag{10}
\]
The divisions are nonzero on the eventual domain (6).
Section 4 will establish the converse on the selected branch,
including the original logarithmic lift.

The only critical values of the cubic projection to \(C\) are
\[
 v_\pm=\frac{2i\pm\sqrt5}{3},\qquad
 C_\pm=\mp\frac{5\sqrt5}{27}+\frac{8i}{27}.
 \tag{11}
\]
They lie strictly to the left of \(\Re C=1/2\), since
\(10\sqrt5<27\). Thus all three roots are simple over the
simply connected half-plane \(\Re C>1/2\), and each admits
single-valued holomorphic continuation there.

There is exactly one root with \(\Re v>3/2\). To see that no
root crosses the boundary line, write \(v=x+ib\). Equation (10)
has real part
\[
 \Re C=\frac{x}{2}
       \left\{x^2-3(b-2/3)^2-\frac53\right\}.
 \tag{12}
\]
At \(x=3/2\) this is at most \(7/16<1/2\).
For large positive real \(C\), exactly one of the three cubic
roots is to the right of that line; the other two have negative
real parts. Root continuation and the exclusion of the boundary
line prove the count on the whole half-plane.

The original root in (3) is this distinguished root. It has
\(x>0\) and solves (9). For \(0<x\le3/2\), the right side of
(12) is at most \(7/16\): the upper cubic
\(x(x^2-5/3)/2\) has its maximum on this interval at its right
endpoint or at zero. It therefore cannot equal \(C=1\).
This identifies the continued root without selecting a different
algebraic sheet.

## 3. Explicit branch guards

We first prove, for the distinguished root over \(\mathcal C\),
\[
             \frac32<x<\frac{15}{8},\qquad
                         \frac13<b<\frac23.
 \tag{13}
\]
The imaginary part of (10) is
\[
 2\Im C=(3b-2)x^2-b^3+2b^2-3b+2.
 \tag{14}
\]
At \(b=1/3\), its right side is
\[
 -x^2+\frac{32}{27}<-\frac{115}{108}<-\frac12.
\]
At \(b=2/3\), it is \(16/27>1/2\). Neither boundary is
possible for \(|\Im C|\le1/4\).

At the original point \(C=1\), (3) gives \(b>0\),
\(x^2-b^2>2\), and \(x^2+b^2<4\), hence \(b<1\).
For \(2/3\le b<1\), the right side of (14) is greater than or
equal to \(2b^3+3b-2>0\), contradicting \(\Im C=0\).
For \(0\le b\le1/3\), that right side is increasing in \(b\)
when \(x>3/2\), and at \(b=1/3\) it is negative.
Thus the original point is between the two boundaries.
Connected continuation through \(\mathcal C\) proves the
two strict \(b\)-bounds.

For \(b\) in this interval, (12) gives
\[
 \Re C>\frac{x}{2}(x^2-2).
\]
If \(x\ge15/8\), the right side is at least
\(1455/1024>17/16\). This proves the \(x\)-bound in (13).
More usefully, (12), \(x>3/2\), and \(\Re C\le17/16\)
give
\[
 x^2<\frac{37}{12}+3(b-2/3)^2,\qquad
 |v|^2<4b^2-4b+\frac{53}{12}\le\frac{127}{36}<4.
 \tag{15}
\]
The quadratic has its maximum at the two endpoints of
\([1/3,2/3]\). In particular \(v/2\) stays strictly inside
the unit disk and in its first quadrant.

Define \(t=2\arccos(v/2)\) on its principal branch.
It has \(0<\Re t<\pi\), \(\Im t<0\), and agrees with the
original \(t_3\). In fact \(\Re t<\pi/2\). If
\(\Re t\ge\pi/2\), then \(x^2-b^2\le2\). Equation (12)
would imply
\[
 \Re C\le\frac{\sqrt{2+b^2}}2
                  \{1-2(b-1)^2\}
 \le\frac{7\sqrt{22}}{54}<\frac23<\frac1{\sqrt2}.
 \tag{16}
\]
The middle expression increases on \(1/3\le b\le2/3\);
both positive factors do. The comparison
\(7\sqrt{22}<36\) follows by squaring. This contradicts (5).

We next prove the useful strict height bound
\(H=-\Im t<1\). Put \(s=\sinh^2(H/2)\).
The exact cosine formulas give
\[
                  x^2=4(1+s)-(1+s^{-1})b^2.
 \tag{17}
\]
If \(H\ge1\), then
\[
 s>s_0=(25/48)^2=625/2304,
\]
because \(\sinh(1/2)>1/2+(1/2)^3/6=25/48\).
The right side of (17) increases with \(s\), so
\[
 x^2>A(b):=4(1+s_0)-(1+s_0^{-1})b^2 .
\]
This function decreases in \(b\), and
\[
 A(2/3)=\frac{9727209}{3240000}>3.
\]
Set \(Q(b)=A(b)-3b^2+4b-3\).
Its derivative is \(4-2(4+s_0^{-1})b<0\) for \(b\ge1/3\),
using \(s_0^{-1}>2\). Thus \(Q(b)>Q(2/3)>4/3\).
Returning to (12) gives
\[
 2\Re C=x(x^2-3b^2+4b-3)
       >\sqrt{A(b)}Q(b)>\frac{4\sqrt3}{3}.
\]
But \(2\sqrt3/3>17/16\), contradicting (5).
This proves \(H<1\) and all guards in (6).

## 4. Original logarithms and the reduced Hessian

The principal values
\[
                 A=\operatorname{arsinh}T,\qquad
                 B=\operatorname{arsinh}(CT),\quad T=\tan(t/2),
 \tag{18}
\]
are analytic on a neighborhood of the entire family.
Indeed \(T\) has positive real and negative imaginary parts.
Writing \(t=a-iH\), the guard \(|\cos(t/2)|<1\) gives
\(\sinh(H/2)<\sin(a/2)\), and hence
\[
 \frac{\Re T}{-\Im T}
  =\frac{\sin a}{\sinh H}
  >\frac{\cos(a/2)}{\cosh(H/2)}
  >\frac{7}{8\sqrt2}>\frac12.
 \tag{19}
\]
Here \(a<\pi/2\), \(H<1\), and
\(\cosh(1/2)<8/7\); the last inequality also follows from
the positive series witness in the fixed-ellipse proof.
Consequently
\[
 \Re(CT)\ge\frac{\Re T}{\sqrt2}
                  -\frac{-\Im T}{4}>0.
 \tag{20}
\]
Neither inverse hyperbolic sine meets a principal cut.

The candidate exponential for \(B\) in (10) satisfies
\(E-E^{-1}=2CT\). Its two roots are distinct, because
\(\Re(CT)>0\). The principal \(e^B\) agrees with that
candidate at \(C=1\), by the original critical equation.
It therefore agrees throughout the connected domain.
Thus \(e^{A+B}=-e^{3it/2}\).
The difference
\(A+B-i(3t/2-\pi)\) is a continuous integral multiple
of \(2\pi i\); it is zero at the original point and
therefore zero everywhere. This proves (7) on the original
logarithmic sheet, rather than only its exponential.

There is also no hidden loss of reduced nondegeneracy.
Write
\[
 \mathfrak C(v)=\tfrac12(v^3-3v)-i(v^2-1),\qquad
 D(t)=i(3t/2-\pi)-A(t).
\]
The algebra behind (10), valid near the critical family, gives
\[
 \sinh D(t)-C T(t)=T(t)\{\mathfrak C(v(t))-C\}.
 \tag{21}
\]
At a critical point, \(D=B\). Differentiating at fixed \(C\)
and using (1)--(2) gives exactly
\[
 \pi\cosh B\,\Phi_{tt}
          =T\,\mathfrak C'(v)\,v'(t),\qquad
                       v'(t)=-\sin(t/2).
 \tag{22}
\]
Every factor on the right is nonzero. The only zeros of
\(\mathfrak C'\) were excluded in (11); \(T\) and
\(\sin(t/2)\) are nonzero by (6); and \(\cosh B\ne0\)
by (20). This proves the claimed nonzero Hessian,
with uniform separation from zero on the compact family.

## 5. Calibrated stationary action and the available finite source

The other edge derivative also continues without crossing a cut.
For \(u\in\mathcal U\),
\[
 |\Re\tan(u/2)|\le1,\qquad |\Im\tan(u/2)|<1/2.
\]
Together with (13), these imply
\[
 \left|\Im\left\{\frac v2\tan(u/2)\right\}\right|
             <\frac{15}{32}+\frac13=\frac{77}{96}<1.
 \tag{23}
\]
Thus the principal inverse hyperbolic sine in (8) is
holomorphic on a neighborhood of \(\mathcal U\).
Integrate this holomorphic derivative on that simply connected
rectangle, fixing its constant to the original \(S_3(0,0)\).
Near zero the result is exactly the original stationary
action, by (1), stationarity, and the full single-three theorem.
It therefore gives its uniquely calibrated analytic continuation.
The continued phase is even; \(t(u)\) depends only on
\(\cos(u/2)\). At zero,
\[
 S_3''(0,0)=-\frac{v(0)}{4\pi}
          =-\frac{\cos(t_3/2)}{2\pi},
 \tag{24}
\]
which is the original boundary Hessian. No additive action
constant or logarithmic charge has been reset.

There is one complete finite-source consequence already licensed.
The critical image \(t(\mathcal U)\) is a compact subset of
\[
 \{t:0<\Re t<\pi/2,\ -107/100<\Im t<0,
                                      |\cos(t/2)|<1\}.
\]
Hence [the free pair-edge theorem, Theorem 1](research_pair_free_boundary_kernel.md)
applies uniformly on a neighborhood of that image. In particular,
the full original \(K_N(t,0)\), with every Newton row, has its
nonzero geometric packet there, at both parities. The theorem also
supplies a common small neighborhood of its second outside argument.
This is an actual use of a proved finite-source domain, not an
extrapolation of the original tiny bidisk.

That edge theorem does not supply \(K_N(t,u)\) for every
\(u\in\mathcal U\). The separate wide bare-kernel theorem has
height at most \(3/10\), which the new critical inner height need
not satisfy. Nor does locating and making the angular critical
point nondegenerate pay the full original three-kernel trace.
An extension still needs the second edge or an unreduced joint
wire representation, all its omitted Newton rows, the nonconstant
cotangent terms, and the angular endpoints and aliases on the
chosen outer family. No new bound for
\(\mathcal K_{3,N}(-2,-2\cos u)\), no coefficient of its continued
critical point, and no full transfer estimate is asserted here.

