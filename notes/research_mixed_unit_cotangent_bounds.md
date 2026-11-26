# Cotangent bounds for the geometric unit solution

Research proof, 5 November 2026. Every inverse leg of a positive unit
path with powers three and four satisfies
\[
 0<\Re\cot\pi s<2,\qquad |\Im\cot\pi s|<1.
 \tag{1}
\]
The proof uses the coupled equations and a continuation with one charge
fixed. It is not an assertion about independent parameter rectangles.
The resulting bounds also give a useful range for the original leg
coordinate. They do not estimate a finite quantum sum.

## 1. The actual unit equations in cotangent coordinates

Use the positive path family, its inverse legs and original logarithms
from the [source lift theorem](research_mixed_geometric_source_log_lifts.md).
Every selected vertex has two incidences, including complete outside
edges. At one incidence write
\[
 u=\cot\pi s,\qquad a=\cot\pi s_{\rm across},\qquad
 v=\cot\pi t,
 \tag{2}
\]
where \(t\) is the other leg of the same vertex. The inverse-leg
half-plane theorem gives positive real parts for all three cotangents.
On an outside edge, include the inverse leg at the complete outside
vertex when defining \(a\). The
[endpoint cotangent barrier](research_mixed_endpoint_cotangent_barrier.md)
proves that each such outside cotangent has imaginary part in \((0,1)\).

Let \(A=\cos^2(\tau/2)\) at the own vertex and \(q\) be the
original wire cotangent. Its inverse formulas give
\[
 q=u+a-i,\qquad A^{-1}=(u-i)(u+a).
 \tag{3}
\]
The unit vertex and shared-wire equations are equivalent to
\[
\begin{array}{ll}
 (u+a)(u+v)=(a-i)(v+i),& n=3,\\[2mm]
 (u+i)(u+a)(u+v)=2i(a-i)(v+i),& n=4.
\end{array}
 \tag{4}
\]
These are the exact equations in the endpoint note; their denominators
are nonzero because the cotangents have positive real parts.
The own cosine square is in the upper-right quadrant. In particular
\(\Im A^{-1}<0\).

## 2. No unit leg can cross the lower horizontal boundary

For type three this follows directly from
\(A=(1-U)(1-V)/4\), where
\(U=e^{-2\pi is}\), \(V=e^{-2\pi it}\) lie below the real
axis. Both \(1-U\) and \(1-V\) are in the upper half-plane.
Their product is in the upper-right quadrant, so the sum of their
principal arguments is in \((0,\pi/2)\). Therefore
\(\Re U,\Re V<1\), equivalently
\[
                       \Im u,\Im v>-1.
 \tag{5}
\]

For type four we first exclude a crossing at \(u=x-i\), \(x>0\).
Write the cotangent across the wire as \(a=b+ic\), \(b>0\),
with no restriction on the real number \(c\). Put
\[
 C=(u+i)(u+a),\qquad
 D=C-2i(a-i),\qquad R=-Cu-2(a-i).
 \tag{6}
\]
The type-four equation gives \(Dv=R\). At \(u=x-i\), exact
algebra yields the strictly positive sum of squares
\[
\begin{split}
 -\frac{\Re(R\overline D)}x
 ={}&(x^2+4)\left[b^2+
           \left(c-\frac4{x^2+4}\right)^2\right]\\
 &+2bx(x^2+2)+\frac{x^4(x^2+3)}{x^2+4}>0.
\end{split}
 \tag{7}
\]
This also excludes \(D=0\). It would follow that
\(\Re v=\Re(R\overline D)/|D|^2<0\), contradicting the
inverse-leg half-plane theorem.

To use this barrier, keep the charge of the own type-four vertex
equal to one and scale all other charges from zero to their target
values. Equation (4) remains valid throughout this path. The other
vertices need not be at unit charge: only their positive cotangent
real parts are used in (7). At the initial isolated vertex, the
[calibrated cubic](research_mixed_geometric_action_calibration.md#3-fixing-the-two-vertex-constants)
gives \(|U|<1\). Thus
\(\Im u=(1-|U|^2)/|1-U|^2>0\) initially. Continuity and (7)
prevent a crossing of \(-1\). The same argument treats its opposite
leg. This proves (5) for every selected unit leg of either type.

## 3. The upper boundary is then excluded pointwise

Now every selected and complete outside cotangent has imaginary part
greater than \(-1\). Suppose a selected leg had
\(u=x+iy\), \(y\ge1\), and write \(a=b+ic\) across its wire.
Equation (3) gives
\[
 \Im A^{-1}=x(2y+c-1)+b(y-1)>0,
 \tag{8}
\]
because \(x,b>0\) and \(c>-1\). This contradicts
\(\Im A^{-1}<0\). Consequently every selected leg has
\(-1<\Im u<1\). No choice of a globally maximizing leg is needed.

We also have \(\Re u<2\). Indeed suppose \(x=\Re u\ge2\).
For its two neighboring cotangents in (4),
\[
 \left|\frac{a-i}{u+a}\right|<1,\qquad
 \left|\frac{v+i}{u+v}\right|<1.
 \tag{9}
\]
For example, if \(b=\Re a>0\), then
\(|a-i|<\sqrt{b^2+4}<b+2\le b+x\le|u+a|\).
The second inequality is identical. At type three (4) would require
the product of the ratios in (9) to be one. At type four it would
require that product to equal \((u+i)/(2i)\), whose modulus is
at least \(x/2\ge1\). Both are impossible. This proves (1).

## 4. A range sufficient for comparison with the source point

Write \(u=P+iy\), where (1) gives \(0<P<2\), \(-1<y<1\).
The original inverse relation is \(U=(u-i)/(u+i)\). Hence
\[
 2\pi\Re s
   =\arctan\frac{1-y}{P}+\arctan\frac{1+y}{P}
   >\arctan\frac2P>\frac\pi4.
 \tag{10}
\]
The sum in the middle is even in \(y\) and strictly decreases for
\(0<y<1\); its limiting value at \(y=1\) is the first arctangent
on the right. Thus
\[
                          1/8<\Re s<1/2.
 \tag{11}
\]

There is a coarse uniform bound on \(|U|\) in both directions.
The two angle rectangles in the
[wire-before-leg theorem](research_mixed_wire_before_inverse_leg.md#1-a-uniform-bound-for-the-original-wire-cotangent)
give \(|A|=(\cosh H+\cos\theta)/2\ge1/5\).
For either endpoint of a geometric edge, therefore,
\(|A^{-1}|,|B^{-1}|\le5\), including a complete endpoint.
Since \(q^2=A^{-1}+B^{-1}-1\), we have \(|q|^2\le11\).
An active edge has \(\Im q<0\), so
\[
 |q+i|^2<12,\qquad
 |U^{-1}|=|1+2iA(q+i)|<1+4\sqrt3,
 \tag{12}
\]
using the proved strict bound \(|A|<1\) at the selected endpoint.

For the other direction, at type three
\(|1-U||1-V|=4|A|<4\). Equation (11) puts
\(\arg V\in(-\pi,-\pi/4)\), so \(|1-V|>1/\sqrt2\).
It follows that
\[
                       |U|<1+4\sqrt2<7.
 \tag{13}
\]
At type four, write \(U=a-ib\), \(V=c-id\) with \(b,d>0\).
The already proved lower cotangent bound gives \(a,c<1\).
Since \(A=(2-U-V)/4\) is upper-right and \(|A|<1\),
\(a+c>-2\) and \(b+d<4\). Thus \(-3<a<1\), \(0<b<4\),
and \(|U|<5\). The same holds for its opposite leg.

Set \(K=1+4\sqrt3\). Since \(7<K\), (12)--(13) yield
\[
 \boxed{\quad K^{-1}<|U|<K,\qquad
       |\Im s|<\frac{\log K}{2\pi}.\quad}
 \tag{14}
\]
The constants have the useful strict comparison
\[
 K<\frac{175}{22}
       <\frac1{\cos(23\pi/50)}.
 \tag{15}
\]
For the first inequality, square \(\sqrt3<153/88\), using
\(153^2-3\cdot88^2=177>0\). For the second,
\(\cos(23\pi/50)=\sin(\pi/25)<\pi/25<22/175\).

The cone in (1) is not convex in \(s\). Its use for comparing two
critical points still requires control of the connecting segment;
mere membership of its two endpoints is not an injectivity proof.
No finite-source noncancellation statement is made here.
