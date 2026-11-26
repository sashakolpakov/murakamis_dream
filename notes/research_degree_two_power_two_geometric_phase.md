# The marked geometric phase for a degree-two two-crossing filling

Research proof, 2 November 2026. The
[two-boundary source theorem](research_degree_two_power_two_boundary_theorem.md)
proves the asymptotic of the original finite polynomial for a
degree-two vertex with power \(2\) or \(-2\). This note fixes
its exact additive phase relative to the original primitive
geometric filling. It then gives a volume theorem after independent
long fillings of the remaining vertices.

## 1. The two stationary actions

Let \(b(x,t)\) and \(J\) have the normalization of the
[exact factorial formula](research_degree_two_power_two_formula.md).
Write

\[
W_0(x,y)=J(x+y)-2J(x)-2J(y)
             +\frac{i\pi}{2}\bigl((x-y)^2+x+y\bigr).
\tag{1}
\]

The direct two-index source phase is

\[
W(x,y;u,v)=W_0(x,y)+b(x,u)+b(y,v).
\tag{2}
\]

Its selected point at \(u=v=0\) is

\[
x=y=z=\frac14+\frac{i\log3}{4\pi}.
\tag{3}
\]

The original degree-two geometric action is

\[
G(u,v)=\operatorname{stat}_{t}
 \left[\psi(t,u)+\psi(t,v)+\frac{it^2}{2\pi}-it\right],
\tag{4}
\]

with its original cone branch and primitive slope. At zero boundary,

\[
t_*=\frac\pi2-2i\operatorname{arsinh}(1/\sqrt2).
\tag{5}
\]

The selected wire points for its two edge blocks are both (3).
This follows from
\(x=\pi^{-1}\arctan(\cos(t_*/2))\) and
\(\cos(t_*/2)=e^{i\pi/6}\).

**Proposition 1.** On a fixed complex neighborhood of \((u,v)=(0,0)\),
the selected stationary value of (2) satisfies

\[
\operatorname{stat}_{x,y}W(x,y;u,v)=G(u,v)+\frac{i\pi}{2}.
\tag{6}
\]

The constant is exactly as displayed; no multiple of
\(2\pi i\) or boundary-dependent term is suppressed.

## 2. Eliminate the central angle with its logarithms retained

Put \(A=e^{2\pi ix}\), \(B=e^{2\pi iy}\). Near the
selected point there is a unique holomorphic choice of \(t=t(x,y)\),
equal to (5) at (3), such that

\[
2\cos t=-A^{-1}-B^{-1}.
\tag{7}
\]

The derivative of its left side is nonzero at the selected point.
The elementary identity

\[
2(\cos(2\pi x)+\cos t)
=i e^{i\pi(x-y)}\,2\sin\pi(x+y)
\tag{8}
\]

then gives

\[
b_x(x,t)=(W_0)_x(x,y),\qquad
b_y(y,t)=(W_0)_y(x,y).
\tag{9}
\]

These are identities of the continued logarithms, not just of
their exponentials. To calibrate them, at (3) the sine
\(\sin(2\pi z)\) is positive real, while the left side of
(8) is \(4i/\sqrt3\). Both sides therefore have argument
\(\pi/2\) in the original continued branches. The nonzero
factors in (8) preserve that logarithmic equality nearby.

The other derivative is

\[
b_t(x,t)=\frac1{2\pi}
 \log\frac{\cos(\pi x+t/2)}{\cos(\pi x-t/2)}.
\tag{10}
\]

For example, this follows from the factorial expression

\[
b(x,t)=J(1/2+t/(2\pi))+J(1/2-t/(2\pi))
 -J(1/2-x+t/(2\pi))-J(1/2-x-t/(2\pi))-2J(x),
\tag{11}
\]

where the first two terms sum to zero on their original branches.
If \(T=e^{it}\), the ratio in (10) is
\((AT+1)/(A+T)\). Equation (7) implies

\[
AB(T^2+1)+(A+B)T=0,
\]

and hence

\[
\frac{AT+1}{A+T}\frac{BT+1}{B+T}=T^{-2}.
\tag{12}
\]

The selected logarithmic lift in (12) is important. Put
\(\beta=\operatorname{arsinh}(1/\sqrt2)\).
At (3)--(5) each ratio in (10) equals \(i e^{-2\beta}\),
and its continued logarithm is \(-2\beta+i\pi/2\).
Thus their logarithms sum to \(2\pi i-2it\), and

\[
b_t(x,t)+b_t(y,t)+\frac{it}{\pi}-i=0
\tag{13}
\]

on the selected branch. An unmarked principal logarithm of the
product in (12) would lose this calibration.

Define

\[
Q(x,y,t)=b(x,t)+b(y,t)+\frac{it^2}{2\pi}-it.
\]

Equations (9) and (13) imply that

\[
W_0(x,y)-Q(x,y,t(x,y))
\tag{14}
\]

has zero derivative in both \(x\) and \(y\). It is therefore
constant near the selected point. We now determine that constant
on the same continued branches.

## 3. A path fixing the constant

For \(0<\theta\le\pi/2\), put

\[
s(\theta)=\operatorname{arsinh}(\sqrt3\sin\theta),
\qquad t(\theta)=\theta-is(\theta),
\]

\[
x(\theta)=y(\theta)
=-\frac{\log(-\cos t(\theta))}{2\pi i}.
\tag{15}
\]

Choose \(\arg(-\cos t)\) between \(-\pi\) and
\(-\pi/2\). At \(\theta=\pi/2\), these values are
exactly (3)--(5). As \(\theta\downarrow0\), they approach
\(x=y=1/2\), \(t=0\). Equation (7) holds along the entire
path.

Here is explicit control of the factorial branches along it.
Write

\[
\varphi=\arg\cos t,\qquad L=\log|\cos t|.
\]

For \(0<\theta<\pi/2\),

\[
0<\varphi<\theta,\qquad 0<L<s,
\qquad x=\frac{\pi-\varphi}{2\pi}+\frac{iL}{2\pi}.
\tag{16}
\]

Indeed
\(\tan\varphi=\tan\theta\tanh s\), and
\(|\cos t|^2=1+2\sin^2\theta\); also
\(|\cos t|\leq\cosh s<e^s\). The potentially delicate
arguments in (11) are

\[
w_+=\frac12-x+\frac{t}{2\pi},\qquad
w_-=\frac12-x-\frac{t}{2\pi}.
\]

By (16), \(w_+\) has positive real part and negative
imaginary part. The point \(w_-\) has negative real part
and positive imaginary part; it never passes through zero.
At the selected endpoint \(w_-\) is purely imaginary and
positive. It therefore continues into the upper side of the
negative-real half-plane, using the logarithm obtained by
passing above zero. This is the same branch reached from
the original positive factorial strip in the geometric cone
deformation. All the other arguments in (11), and \(x,2x\),
stay inside their original strips until the limiting endpoint.

No sine or cosine factor in (8)--(12) vanishes for
\(\theta>0\). For example,
\(A=B=-1/\cos t\), so
\(2(\cos(2\pi x)+\cos t)=-\sin^2t/\cos t\ne0\).
Also \(AB\ne1\), and the arguments \(w_\pm\) above
avoid the zeros of sine. Thus (9) and (13), already calibrated
at the selected point, continue without an integer jump.
Expression (14) remains the same constant along (15).

As \(\theta\downarrow0\), the two points \(w_\pm\)
tend to zero on the finite branches just described. The
local expansion
\(J(w)=w\log(2\pi w)-w+O(w^3)\) shows that
\(J(w_\pm)\to0\). Furthermore \(J(1/2)=J(1)=0\).
These values follow directly by integrating the sine
double-angle identity on \([0,\pi/2]\).
It follows from (11) that \(b(x,t)\to0\).
The polynomial terms in \(Q\) also tend to zero, whereas
(1) tends to \(i\pi/2\). Hence

\[
W_0(x,y)-Q(x,y,t(x,y))=\frac{i\pi}{2}.
\tag{17}
\]

## 4. Recover the actual stationary geometric action

Add \(b(x,u)+b(y,v)\) to both sides of (17). The right
side is the original joint phase with the central angle
eliminated on its selected branch. At the selected stationary
point, (9) and (13) give all three original equations:

\[
\begin{aligned}
b_x(x,t)+b_x(x,u)&=0,\\
b_y(y,t)+b_y(y,v)&=0,\\
b_t(x,t)+b_t(y,t)+it/\pi-i&=0.
\end{aligned}
\]

The first two are exactly the original edge wire equations.
Their selected stationary values are \(\psi(t,u)\) and
\(\psi(t,v)\). The last equation is the original
degree-two primitive filling equation. Nondegeneracy and
the implicit function theorem identify this solution near
\((u,v)=(0,0)\) with the geometric branch (4).

For clarity, its continuation from the complete cone path
reaches the factorial branches used above. Along that path
\(t=2a-2ib\), one has
\(a=\pi\lambda/4\), \(\sinh b=\sin a\), and
\(|\cos(t/2)|=1\). Thus the selected wire has
\(\Re x=1/4\). The delicate argument
\(1/2-x-t/(2\pi)\) approaches its selected imaginary value
from the positive-real side, since its real part is
\((1-\lambda)/4\). It is nonzero at the endpoint.
This verifies the match with the upper continuation used
in Section 3. Equation (17) now proves (6).

The positive cone construction and its absolute volume
calibration are proved in
[the internal-vertex geometry note](research_isolated_internal_vertex_geometry.md).
For this degree-two star the complete anchor consists of
four original regular ideal octahedra. Thus the geometric
action in (4), with no further additive real constant,
has real part equal to the volume of its marked filled
blocks divided by \(2\pi\).

## 5. The corrected boundary asymptotic

Let \(A_+(u,v)\) be the nonzero amplitude in the
two-boundary source theorem. For \(\sigma=\pm1\),
write \(G_\sigma\) for the original geometric action at
power \(2\sigma\). Then

\[
P_{2\sigma,N}(u,v)
=e^{\sigma i\pi N/2}N^{-3/2}
 A_\sigma(u,v)e^{NG_\sigma(u,v)}(1+O(N^{-1})),
\tag{18}
\]

where
\(A_-(u,v)=\overline{A_+(\overline u,\overline v)}\).
The same conjugation relates the two geometric actions.
Their entire-boundary Gaussian estimates are those already
proved for the full polynomial in the source theorem,
since the correction in (6) is a purely imaginary constant.
Their boundary Hessians have entries
\(-e^{\sigma i\pi/6}/(2\pi)\), with strictly negative
real part.

The exact unit factor in (18) is
\(e^{\sigma i\pi N/2}\). It is not replaced by an
unidentified framing factor or by the crossing scalar from
a different contour representation.

## 6. A volume theorem with internal powers \(2\) and \(-2\)

Fix an original ordered circle-tree knot template and a
set of pairwise nonadjacent original degree-two vertices.
Give each selected vertex power \(2\) or \(-2\), in
its original disk frame, and keep every other original
marking. There is a finite threshold such that all
independently sufficiently long fixed signed powers at the
remaining vertices give

\[
\lim_{N\to\infty}\frac{2\pi}{N}\log|\langle K\rangle_N|
=\operatorname{Vol}(S^3\setminus K),
\tag{19}
\]

through all integer levels. The original parity pattern
must produce a knot, as in the other circle-tree theorems.

To prove this, sum each selected vertex exactly, retaining
both neighboring boundary variables. Equation (18) supplies
the nonzero local amplitude, the factor \(N^{-3/2}\),
the full boundary estimate and the marked geometric action.
Multiply these factors with the untouched original edge
kernels and apply the complex-phase long-filling theorem.
The source's boundary Hessian remains diagonal with
strictly negative real entries, and each free coordinate
retains positive angular loss. The original edge count
gives the final leading power \(N^{3/2}\).

The selected geometric cone fillings remain smooth as the
free angles vary near zero. Their original primitive slopes
are \(\mu-\sigma\lambda_{\rm long}\), because their
carrier is zero and their integer coefficient is
\(p=-\sigma\). The positive geometry and the two-stage
Schläfli argument identify the subsequent long-filling
action with the volume of the actual knot complement.
This proves (19), with the nonzero leading coefficient
required to take its logarithm.

The proof is also compatible with the other eligible
nonadjacent short fillings; they are collected in
[the enlarged nonadjacent-filling theorem](research_nonadjacent_short_fillings_and_long_remainder.md).
It does not permit treating adjacent short vertices as
independent factors.
