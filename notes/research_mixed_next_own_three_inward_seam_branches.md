# Exact upper-row reversal and the own-three inward-seam branches

Private research deduction, 8 November 2026. The next own-three
source has an exact reflected finite upper sum. At the original
inward seam, its ratio equation has two simple roots in the
upper physical index half. One is a zero-lift critical point of
the original conditional phase, with all its exponential
arguments strictly inside the unit disk.

This is a finite algebra and critical-domain theorem. It does
not identify a contributing contour, compare the critical
action with the following reference action, or prove a packet
for the upper block. No numerical evaluation is used.

## 1. Exact finite reversal, including the terminal factor

Put \(r=e^{-2\pi i/N}\), \(D=N-1\),
\(P_j=(r;r)_j\), and \(p_j(W)=(rW;r)_j\). For the original
own-three row write
\[
a_j(Y,Z)=\frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2}.
\tag{1}
\]
The original upper physical block consists of
\(\lceil N/2\rceil\le j\le D\). Its reflected index is
\[
k=D-j,\qquad 0\le k\le K_N:=\lfloor N/2\rfloor-1.
\]
The elementary root-of-unity products give
\[
\begin{split}
P_D&=N,\qquad
P_{D-k}=N(-1)^k r^{k(k+1)/2}/P_k,\\
p_{D-k}(W)&=\frac{p_D(W)}
 {\prod_{\ell=1}^k(1-r^{-\ell}W)},\\
\prod_{\ell=1}^k(1-r^{-\ell}W)
 &=(-W)^k r^{-k(k+1)/2}p_k(W^{-1}).
\end{split}
\tag{2}
\]
Consequently
\[
\boxed{\quad
a_{D-k}(Y,Z)=a_D(Y,Z)
\frac{Z^{-k}P_k^2}{p_k(Y^{-1})p_k(Z^{-1})},
\qquad
a_D(Y,Z)=\frac{Y^{-D}p_D(Y)p_D(Z)}{N^2}.
\quad}
\tag{3}
\]
All phases and powers in (3) are literal; there is no
additional factor of \(N\). In particular
\[
\sum_{j=\lceil N/2\rceil}^{D}a_j(Y,Z)
=a_D(Y,Z)\sum_{k=0}^{K_N}
\frac{Z^{-k}P_k^2}{p_k(Y^{-1})p_k(Z^{-1})}.
\tag{4}
\]
Equations (3)--(4) are meromorphic identities with the original
polynomial continuation understood at removable cancellations.
They follow first away from the displayed denominators, and then
by clearing those denominators. One must not estimate the terminal
factor and the reciprocal sum separately at a zero of \(p_D(Z)\).
For example a physical \(Z\) can make \(p_D(Z)=0\) while the
original upper block is not identically zero.

For the reflected term without \(a_D\), the exact consecutive
ratio is
\[
\frac{b_{k+1}}{b_k}
=Z^{-1}
\frac{(1-r^{k+1})^2}
 {(1-r^{k+1}/Y)(1-r^{k+1}/Z)}.
\tag{5}
\]
Its unit-ratio equation, with \(w=r^{k+1}\), is
\[
(w-Y)(w-Z)=Y(w-1)^2.
\tag{6}
\]
The same equation follows directly from the original row
ratio after the reciprocal change of its exponential variable.
There is no infinite hypergeometric summation in this deduction.

## 2. Actual inward-seam parameter domain

Use the original ordinary-next lower-left coordinates
\[
y=ih_y,\quad -.102<h_y<-.001,\qquad
z=u+ih_z,\quad u\in[.22,.45],
\quad -.065<h_z<.068 .
\tag{7}
\]
Thus
\[
Y=R=e^{2\pi h_y}\in(13/25,1),\qquad
Z=\rho e^{-2\pi iu},\qquad 13/20<\rho<8/5 .
\tag{8}
\]
These are the original source bounds and elementary radial
witnesses used in
[the joint-profile theorem, equations (12),(17)](research_mixed_next_lower_left_joint_main_profiles.md)
and
[the central first-block theorem, equation (14)](research_mixed_next_lower_right_shoulder_central_prefix.md).
In particular
\[
\Im Z<0,\qquad \Re Z<\rho/5<8/25.
\tag{9}
\]
For the cosine witness,
\(\cos(11\pi/25)=\sin(3\pi/50)<3\pi/50<1/5\);
the cosine decreases through the present interval of arguments.
No independent replacement of a geometric reference is made:
(7) contains every actual ordinary-next seam target in this lane.

At \(Y=R\), equation (6) is the quadratic
\[
(1-R)w^2+(R-Z)w+R(Z-1)=0 .
\tag{10}
\]
Neither \(w=R\) nor \(w=0,1,Z\) solves it on (8)--(9).
Solving it for \(Z\) yields the exact rational map
\[
Z=\mathcal Z_R(w)
=(1-R)w+R(2-R)-\frac{R(1-R)^2}{w-R}.
\tag{11}
\]
Its imaginary part is
\[
\Im\mathcal Z_R(w)=
\left(1-R+\frac{R(1-R)^2}{|w-R|^2}\right)\Im w .
\tag{12}
\]
Therefore both roots of (10) lie strictly in the lower
\(w\)-half-plane whenever \(\Im Z<0\).

## 3. Two simple separated branches

Fix \(1/2<R<1\), and first allow the larger connected domain
\(\Im Z<0,\ \Re Z<8/25\).
The only possible double roots of (10) are the critical points
of (11):
\[
w=R\pm i\sqrt{R(1-R)},\qquad
Z=R(3-2R)\pm2i\sqrt{R(1-R)^3}.
\tag{13}
\]
Their \(Z\)-real part exceeds one, since
\[
R(3-2R)-1=(2R-1)(1-R)>0 .
\]
Thus both roots are simple on the stated domain.

Three exact boundary exclusions label them. If
\(\Re w=R\), then (11) gives
\(\Re Z=R(3-2R)>1\).
If \(\Re w=0\), then
\[
\Re Z=R(2-R)+
\frac{R^2(1-R)^2}{R^2+(\Im w)^2}
>R(2-R)>\frac34 .
\tag{14}
\]
Finally suppose \(|w|=1\) and \(c=\Re w>R\).
From
\[
\mathcal Z_R(w)-1
=(1-R)\frac{w(w-1)}{w-R}
\]
one obtains
\[
\Re Z-1=
\frac{(1-R)(1-c)(2Rc+R-1)}{|w-R|^2}>0 .
\tag{15}
\]
Here \(c<1\) by (12), and
\(2Rc+R-1>2R^2+R-1=(2R-1)(R+1)>0\).

At the boundary value \(Z=0\), the two roots are real:
one is negative, and the other is strictly between \(R\)
and one. This follows by evaluating (10) at \(0,R,1\);
the values are respectively \(-R,-R(1-R)^2,1-R\).
Continue from \(Z=0\) into the lower half-plane.
Equations (12)--(15), simplicity, and connectedness show that
the two branches satisfy throughout the domain
\[
\Re w_-<0,\qquad
\Re w_+>R,\qquad R<|w_+|<1,\qquad
\Im w_\pm<0.
\tag{16}
\]
Equivalently, root counting in these separated regions is
constant along every path; no permutation of the branches
is possible across their displayed boundaries.

For the actual radial domain (8)--(9), Vieta's identity gives
\[
|w_-w_+|=\frac{R|Z-1|}{1-R}.
\tag{17}
\]
Since \(\rho>13/20>2/5\) and \(\Re Z<\rho/5\),
\[
|1-Z|^2>1+\rho^2-\frac25\rho>1 .
\]
Together with \(|w_+|<1\) and \(R/(1-R)>1\), this proves
\(|w_-|>1\). Moreover
\[
\begin{split}
R^2|1-Z|^2-(1-R)^2|Z|^2
&=R^2(1-2\Re Z)+(2R-1)\rho^2\\
&>R^2(1-2\rho/5)+(2R-1)\rho^2>0,
\end{split}
\]
because \(\rho<8/5\). Hence (17) also proves
\[
\boxed{\qquad |w_-|>\max\{1,|Z|\}.\qquad}
\tag{18}
\]

## 4. Original zero lift and the reflected contour location

Choose the logarithm of \(w_-\) with argument in
\((\pi,3\pi/2)\), and set
\[
t_-=\frac{\log w_-}{2\pi i}.
\]
Then (16),(18) give
\[
\frac12<\Re t_-<\frac34,\qquad
\Im t_-<\min\{0,-h_z\}.
\tag{19}
\]
All three exponential arguments
\[
e^{-2\pi it_-}=w_-^{-1},\qquad
e^{-2\pi i(t_-+y)}=R/w_-,\qquad
e^{-2\pi i(t_-+z)}=Z/w_-
\]
are strictly inside the unit disk. Therefore the original
inward primitive
\[
g'(s)=\operatorname{Log}(1-e^{-2\pi is})
\]
has its principal, single-valued logarithm at all three arguments,
including an argument whose real part crosses one.

For the literal phase
\[
Q_0(t;y,z)=g(t+y)+g(t+z)-2g(t)-g(y)-g(z)+2\pi iyt
\]
its derivative is
\[
Q_{0,t}=
\operatorname{Log}(1-R/w_-)
+\operatorname{Log}(1-Z/w_-)
-2\operatorname{Log}(1-1/w_-)-\log R .
\tag{20}
\]
The exponent of (20) is one by (6).
Since \(w_-\) is in the lower left quadrant, both the first
and third logarithms have arguments in \((-\pi/2,0)\).
The second has argument in \((-\pi/2,\pi/2)\).
The imaginary part of (20) is consequently in
\((-\pi,3\pi/2)\). The only multiple of \(2\pi\) in that
interval is zero, proving
\[
\boxed{\quad Q_{0,t}(t_-;y,z)=0.\quad}
\tag{21}
\]
The critical point is nondegenerate because (10) has a simple
root and none of the divisors in (20) vanishes.
On compact subsets of the actual domain, these strict guards
persist on a fixed complex parameter neighborhood.

In the reflected coordinate \(v_-=1-t_-\), (19) becomes
\[
\frac14<\Re v_-<\frac12,\qquad
\Im v_->\max\{0,h_z\}.
\tag{22}
\]
Thus the coherent reflected upper-row saddle lies above the
real \(k/N\) interval. If \(h_z>0\), it also lies above the
outgoing logarithmic divisor \(v=z\) of the reciprocal-product
continuation. This statement does not replace that continuation
by a guessed periodic phase or discard its finite zero
cancellations.

## 5. What is still needed for a finite estimate

Equations (3)--(5) retain the complete upper block, both parities,
and the original terminal scalar. Equations (19)--(21) locate
an actual zero-lift critical point of its original conditional
phase at the inward seam, using only domains satisfied by the
ordinary targets. They rule out an argument that would exclude
all upper-index critical points by those domains alone.

They do not show that the original finite integration cycle
passes through this point, determine its intersection number,
or compare its action with the unchanged following plane.
A coherent upper-row proof must retain the terminal
cancellations in (3), the reciprocal-product divisors, all
physical rows, and the exact aliases and boundary currents.
The first factor and full shared Fourier weight remain attached
in the desired lower-left estimate. No whole-kernel
noncancellation, suppression, or new knot theorem follows here.
