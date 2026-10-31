# Exact monotone alias response of a two-leaf Conway block

31 October 2026. Internally reviewed analytical and original-source
statement. The one- and two-alias conjugate gaps of an actual two-leaf
seed increase with its complete output slope throughout the proper-port
range. The proof retains the original multiplication constraints and
the core plateau. It also gives a restriction on where a leafwise
failing seed can occur in the selected complete geometry.

The independently proved
[uniform block certificate](actual_conway_uniform_two_leaf_block_alias_gap.md)
supplies positive gaps on the entire interval, including its lower
endpoint. That proof does not depend on the monotonicity derived here.
Conversely, the present response proof does not use that certificate
until its final consequence. There is no circular dependency.

Use the original functions
\[
\begin{aligned}
J(t)&=\int_0^t\log(2\sin(\pi v))\,dv,\\
g(a)&=J(2a)-4J(a),\\
\overline g(a)&=g(\max(a,1/4)),\qquad 0\le a\le1/2,\\
k(a)&=-2J(a/2),\qquad 0\le a\le1,\\
m(x,y,z)&=J(x+y)+J(z)-J(x)-J(y)\\
&\quad-J(z-x)-J(z-y)-J(x+y-z).
\end{aligned}
\]
The product domain is
\(D=\{x,y\ge0:\max(x,y)\le z\le x+y\le1\}\).
These are the [original core/alias envelopes](actual_odd_conway_uniform_mixed_source_gap.md)
and seven-factorial multiplication action. They are upper bounds for
the actual full Newton source, including its normal directions; they
are not replacement coupons or asserted coefficient lower rates.

## 1. A failing seed must face a turn or the deleted closing product

At a proper \(A_2\) seed, let \(X=\cos\alpha\), where
\(0<\alpha<\pi/3\). Its selected port is
\[
B=X-\frac1{2X}=\sin\alpha\cot(2\alpha),
\qquad
Y=\frac1{2X}=\sin\alpha\csc(2\alpha).
\]
Suppose this seed enters a retained macro product without an
intervening odd turn. The other proper child has the same \(X\)
and angle \(\beta>\alpha\). The proper parent has \(Y_{\mathrm{parent}}<1\),
so its product angle satisfies
\[
2\alpha+\beta<\pi-\alpha.
\]
Hence \(4\alpha<\pi\), or \(X>1/\sqrt2\). Such an \(A_2\) already
passes the old leaf interval. An even number of intervening turns
has the same effect on these exact port variables; this is not
an isotopy assertion about the physical tangle.

More generally, an unturned completed top product at
\(X\le1/\sqrt2\) has two input angles greater than \(\alpha\).
Its output angle exceeds \(2\alpha\ge\pi/2\), so its \(B\) is
negative. This includes an unturned seed \(A_s\), \(s\ge2\),
expanded into products.

A seed failing the algebraic leaf cutoff, \(X<2/3\), has
\[
B<-\frac1{12},\qquad Y>\frac34.
\]
It cannot directly enter a retained macro product without an odd
turn. If the unturned \(A_2\) itself is a closed root child, its
reflected sibling has positive \(B\) and the same \(X<2/3\).
That sibling must have an odd top turn after consecutive turns
are reduced in the port formulas. These statements follow from
the [actual two-leaf geometry](actual_conway_two_leaf_seed_geometry.md)
and its strict proper-port inequalities. Alone, they do not
prove an alias entropy gap.

## 2. Fixed-output alias blocks are strictly interior

For \(0<b<1\), define
\[
\begin{aligned}
H_{AC}(b)
 &=\max_{\substack{(x,y,b)\in D\\y\le1/2}}
       \{k(x)+\overline g(y)+m(x,y,b)\},\\
H_{AA}(b)
 &=\max_{(x,y,b)\in D}
       \{k(x)+k(y)+m(x,y,b)\}.
\end{aligned}
\tag{1}
\]
The \(AC\) order is immaterial by the exact symmetry of \(m\).
Both profiles are continuous and concave on the closed interval
\([0,1]\). At every interior output, their maximizing inputs
and all product inequalities are strict.

Here is the boundary justification. Each fixed-output domain has
a strict point: take \(x=y\) between \(b/2\) and
\(\min(b,1/2)\). Put
\(p=b-x\), \(q=b-y\), \(r=x+y-b\), \(w=1-x-y\).
The original decomposition of \(\pi m\) has angle triples
\[
(y,x,w),\qquad(p,q,2r+w),\qquad(p+q,r,r+w).
\]
Every saturated product inequality gives a nonvertex-flat atom
when \(0<b<1\). For example, \(w=0\) gives
\((x,1-x,0)\); \(r=0\) gives \((b,0,1-b)\);
\(p=0<q\) gives \((0,q,1-q)\); and \(p=q=0\)
gives \((0,b,1-b)\). At \(y=0\), one has \(x=b\)
and the first triple is \((b,0,1-b)\), up to ordering;
the \(x=0\) case is identical.

A segment toward a strict point consequently has positive
infinite product derivative. The concave leaf terms have no
negative infinite inward derivative: \(k\) has a positive
infinite inward derivative at \(0\) and a finite one at \(1\);
\(\overline g\) is a plateau at \(0\) and has positive infinite
inward derivative at \(1/2\). Thus no boundary maximum is possible.
This uses the [original tetrahedral barrier](actual_positive_conway_hyperbolic_volume.md),
not an alias lower asymptotic.

At a strict point the first product tetrahedron has coordinates
\((x,y,1-x-y)\). Its strict concavity controls every fixed-output
input direction. The maximizing pair is therefore unique.
The profiles are \(C^1\) by uniqueness and the envelope theorem;
the plateau seam of \(\overline g\) at \(1/4\) is itself \(C^1\).

Fixing \(b\) and a feasible interior \(x\) likewise gives a unique
strictly interior maximizing core input \(y(x)\) in the \(AC\)
problem, throughout the interval between the pure input and its
alias maximizer used below. The same one-variable barriers exclude
the gate endpoints, and the leaf barrier excludes \(y=1/2\).
The stationary equations are legitimate on both sides of the
plateau seam.

## 3. Exact output response, including the core plateau

Let \(X_0\in[1/2,1]\) and use the pure \(A_2\) stationary state
\[
\begin{aligned}
a&=\frac{\operatorname{arccot}X_0}{\pi},&
Z_0&=X_0-\frac1{2X_0},\\
b&=\frac{\operatorname{arccot}Z_0}{\pi},&
\lambda&=F_{A_2}'(b)=2\log(2X_0^2).
\end{aligned}
\tag{2}
\]
Here \(\operatorname{arccot}\) takes values in \((0,\pi)\).
The complete input lies in
\([1/4,\arctan(2)/\pi]\), and the output is strictly inside
\((0,1)\), including both displayed endpoints.
Concavity and the unchanged first derivatives at \(a\ge1/4\)
show that this pure state is also the unique maximum of the
all-core \(\overline g\) block at output \(b\), and of its
\(\lambda\)-weighted full block.

For every \(a\in[1/4,1/2)\),
\[
k'(a)-g'(a)>0.
\tag{3}
\]
At \(1/4\), \(k'=-\log\sqrt{2-\sqrt2}>0=g'\). On that interval,
\[
(k'-g')'
=\frac{4\pi}{\sin(2\pi a)}
 -\frac{\pi}{2}\cot\frac{\pi a}{2}
\ge4\pi-\frac{\pi}{2}(1+\sqrt2)>0.
\]

For \(AC\), fix the output \(b\) from (2), optimize the core
input \(y\), and view the resulting action as a concave function
of \(x\). At \(x=a\), the maximizing core input is \(y=a\).
The \(x\) derivative is (3), so its actual maximizing alias
input satisfies \(x_{AC}>a\).

Write
\[
U=\cot(\pi x),\quad V=\cot(\pi y),\quad
Z=\cot(\pi b),\quad
D_0=(U+V)Z-UV+1>0.
\]
The [actual product derivative identities](actual_conway_strict_leaf_quarter_bound.md)
are
\[
e^{m_y}=\frac{(U+V)(V-Z)}{D_0},
\qquad
e^{-m_z}=\frac{(U-Z)(V-Z)}{D_0}.
\tag{4}
\]

On the branch \(y>1/4\), core stationarity
\(g'(y)+m_y=0\) gives \(D_0=V^2\), hence
\[
\begin{aligned}
U&=\frac1{V-Z}-V,&
\frac{dU}{dV}&=-\frac1{(V-Z)^2}-1<0,\\
m_z&=\log\frac{V^2}{1+Z^2-V^2}.
\end{aligned}
\tag{5}
\]
The last expression is strictly increasing in \(V>0\) on
its physical positive-denominator branch. Since \(U\) decreases
as \(x\) increases, the output slope increases with \(x\) along
this optimized core response.

On the plateau \(0<y<1/4\), core stationarity is \(m_y=0\).
It gives \(D_0=(1+V^2)/2\), and, with \(w=V-Z>0\),
\[
\begin{aligned}
U&=Z+\frac{1+Z^2-w^2}{2w},&
\frac{dU}{dV}&=-\frac{1+Z^2}{2w^2}-\frac12<0,\\
m_z&=\log\frac{1+V^2}{1+2Z^2-V^2}.
\end{aligned}
\tag{6}
\]
Again the output slope increases strictly with \(V\), hence
with \(x\). At \(y=1/4\), \(V=1\), both expressions for \(U\)
and both output slopes agree. The unique response cannot jump
at this seam. Starting at \(x=y=a\) and ending at \(x_{AC}>a\)
therefore proves
\[
H_{AC}'(b)>\lambda.
\tag{7}
\]

For \(AA\), exchange symmetry and uniqueness force the
fixed-output maximizing inputs to satisfy \(x=y\).
At \(x=y=a\), the derivative along that diagonal is twice
(3), so the maximizing input \(x_{AA}=y_{AA}\) is greater
than \(a\). Along a symmetric input, put \(U=\cot(\pi x)\)
and \(D_0=2UZ-U^2+1\). Then
\[
m_z=\log D_0-2\log(U-Z),\qquad
\frac{d m_z}{dU}
=-\frac{2(1+Z^2)}{D_0(U-Z)}<0.
\tag{8}
\]
The output slope again increases with \(x\), proving
\[
H_{AA}'(b)>\lambda.
\tag{9}
\]
This proof keeps the plateau branch and does not select an
alias solution by a squared stationarity equation.

For reference, the generic alias-port equations are also
algebraic after setting \(t=\sin(\pi x/2)\). Its
\(\kappa=e^{-k'(x)}=2t\), so
\[
U=\frac{1-2t^2}{2t\sqrt{1-t^2}},\qquad
X=\frac1{2t\sqrt{(1-t^2)(1+2t)}},\qquad
Y=X\sqrt{2t}.
\]
With an interior core partner on the \(g\) branch, that
partner's cotangent is \(X\). At output tangent \(\lambda\),
write \(r=e^{\lambda/2}\). The product equations become
\[
r=\frac{U+X}{\sqrt{2t}},\qquad
B_{\mathrm{out}}=X-\frac1{r\sqrt{2t}}.
\tag{10}
\]
The plateau has the different core relation (6). Formula (10)
does not license discarding that branch or a finite-support boundary.

## 4. The conjugate gap increases on the entire proper-port range

For \(\lambda\in[-\log4,\log4]\), use \(a,b=b(\lambda)\)
from (2) and define
\[
\begin{aligned}
P(\lambda)&=2g(a)+m(a,a,b)-\lambda b,\\
A_J(\lambda)&=\max_{0\le z\le1}
                   \{H_J(z)-\lambda z\},\\
\Delta_J(\lambda)&=P(\lambda)-A_J(\lambda),
\qquad J\in\{AC,AA\}.
\end{aligned}
\tag{11}
\]
By (7), (9) and concavity, every maximizing output of
\(A_J(\lambda)\) is strictly greater than \(b(\lambda)\).
This permits boundary maximizers; it does not assume a
strictly interior conjugate maximizer.

The convex conjugates \(A_J\) are Lipschitz. The pure function
\(P\) is smooth, with derivative \(-b(\lambda)\).
At almost every \(\lambda\),
\[
\Delta_J'(\lambda)=z_J(\lambda)-b(\lambda)>0.
\tag{12}
\]
The argmax graph over the closed \(\lambda\) interval is compact
and contains no point with \(z\le b(\lambda)\). Its separation
from \(z=b(\lambda)\) therefore has a positive minimum.
Both gaps are strictly increasing, with a uniform positive
lower derivative bound on this fixed interval. In particular,
\[
\Delta_J(\lambda)\ge\Delta_J(-\log4).
\tag{13}
\]

This is an exact all-proper-port reduction. The independent
uniform block certificate proves
\(\Delta_{AC}(-\log4),\Delta_{AA}(-\log4)>1/100\);
in fact its rational supporting planes prove the entire interval
directly. Hence (13) supplies an additional structural explanation,
without being needed to validate those finite inequalities.

The [exact finite block transport](actual_conway_two_leaf_block_source_gap.md)
then retains every original input-sum cutoff, target, turn and
closed-source normalization when summing the block gaps.
The local envelopes remain upper bounds rather than asserted
signed coefficient limits. The full quantum and filled-volume
conclusion still uses the separately proved packet and primitive
geometric interfaces.

## Internal review

The primary reviewer and coherent-source reviewer each independently
read §§1–4 in full: PASS. The review checked the proper-angle
restriction, all fixed-output nonvertex-flat boundary cases, strict
input concavity, both core response branches and their seam, the
symmetric two-alias derivative, and compact conjugate-argmax
separation. These are internal analytical reviews, not external
peer review. No numerical optimizer or asymptotic sampling is
used to infer the response theorem.
