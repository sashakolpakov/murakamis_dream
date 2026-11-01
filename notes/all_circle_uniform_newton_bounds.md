# Uniform estimates for a tree whose junctions all carry crossing circles

This note proves two uniform estimates used in the [quantitative filling limit](actual_all_circle_curvature_filling_limit.md). It does not identify a complex critical value with the volume of a filled complement. The latter still requires the original marked geometry and smooth completion.

Fix a finite ordered tree. Every vertex carries its actual crossing-circle operator, including the degree-one vertices. Write \(d_v\) for a vertex degree and \(a_v=d_v/(2\pi)\). All graph data and integer crossing powers are fixed before the level \(N\) tends to infinity. Constants in polynomial prefactors may depend on these fixed data. The exponential constants below do not depend on the tree.

## 1. A uniform loss outside the retained interval

Use the fixed complete Newton basis, the physical diagonal edge factors, the full value-and-first-derivative norm, and the fixed-power crossing bounds from [the full polynomial trace bounds](actual_main_meridian_source_bounds.md). A low basis element has norm at most a polynomial times \(\exp(Ng(k/N))\); a high basis element has polynomial norm. Here
\[
g(x)=J(2x)-4J(x),\qquad
J(x)=\int_0^x\log(2\sin\pi u)\,du,
\]
\[
g'(x)=2\log\cot(\pi x),\qquad
g''(x)=-\frac{4\pi}{\sin(2\pi x)}\le-4\pi.
\]
Thus, with \(G_0=g(1/4)\),
\[
g(x)\le G_0-2\pi(x-1/4)^2.
\]

Each physical edge index occurs at its two ends. Quotient multiplication, a fixed crossing power, and the trace cost only a polynomial in the full norm. Consequently the absolute scalar sum is bounded by a polynomial times the sum of the products of the squared basis bounds. There are only polynomially many edge-index assignments for a fixed tree. Its complete maximum is \(F_0=2|E|G_0\).

Retain the interval \(I=[1/5,3/10]\) on every edge. A low edge outside \(I\) loses at least \(\pi/100\) in this rate. A high edge loses \(2G_0\), which is larger. The sum of every discarded assignment therefore has upper rate at most
\[
F_0-\pi/100+o(1).
\]
Equivalently, any fixed loss strictly smaller than \(\pi/100\), such as \(\pi/200\), holds with a polynomial prefactor for all sufficiently large levels. This statement retains both level parities and every first normal. It uses no comparison with a complete tensor at the same high index.

## 2. An elementary Gaussian bound on the complex angular strip

Let \(N\ge160\) and \(k/N\in I\). Put
\[
r_j=\cos\frac{(2j+1)\pi}{N},\qquad
Q_r(z)=\frac{r+\cos z}{1+r}.
\]
The exact normalized basis value is
\[
\frac{e_k(-2\cos z)}{e_k(-2)}=\prod_{j=0}^{k-1}Q_{r_j}(z).
\]
Although some individual factors have a negative constant Laurent coefficient, those factors can be paired before taking absolute values.

Reserve the first \(m=\lfloor N/32\rfloor\) factors. Their parameters satisfy \(r_j\ge\cos(\pi/16)>9/10\). There are at most \(h\le N/20+1\) negative parameters, all greater than \(\cos(3\pi/5)>-2/5\). Pair each of these with a different parameter from the next \(h\) positions after the reserved ones. These positions are disjoint from the negative ones and have parameter at least \(\cos(\pi/4)>7/10\), because \(m+h\le N/8\). Every remaining unpaired parameter is nonnegative.

For a pair \(r>-2/5\), \(s>7/10\), the reciprocal polynomial
\[
(u^2+2ru+1)(u^2+2su+1)
\]
has coefficients \(1,2(r+s),2+4rs,2(r+s),1\), all nonnegative. After division by its value at \(u=1\) and multiplication by \(u^{-2}\), these are the weights of a symmetric probability measure supported on \(\{-2,-1,0,1,2\}\). A remaining single nonnegative factor has the analogous interpretation on \(\{-1,0,1\}\). For such a factor of Laurent degree \(b\),
\[
|Q(t+iy)|\le\cosh(by)\le\exp(b^2y^2/2).
\]

The reserved factors supply the real angular decay. If \(r\ge9/10\) and \(w=\sin^2(t/2)\), then
\[
|Q_r(t)|=\left|1-\frac{2w}{1+r}\right|\le1-w/2.
\]
For \(|y|\le1/4\), the identity
\[
|r+\cos(t+iy)|^2=(r+\cos t)^2
 +2r\cos t(\cosh y-1)+\sinh^2 y
\]
and \(2(\cosh y-1)+\sinh^2 y\le4y^2\) give
\[
|Q_r(t+iy)|^2\le1-w/2+4y^2,
\qquad
|Q_r(t+iy)|\le\exp(-w/4+2y^2).
\]
Since \(m\ge N/40\), multiplication gives the deliberately conservative bound
\[
\boxed{\displaystyle
\left|\frac{e_k(-2\cos(t+iy))}{e_k(-2)}\right|
\le\exp N\left\{-\frac{\sin^2(t/2)}{160}+4y^2\right\}.}
\]
For \(|t|\le\pi\), use \(\sin^2(t/2)\ge t^2/\pi^2\). Multiply the bound over the incidence factors of the original finite packet, retain the bounded physical edge factors, and sum its polynomially many indices. One obtains
\[
|B_N(\mathbf t+i\mathbf y,s)|
\le C N^A\exp N\left\{
F_0-\frac1{400}\sum_v a_vt_v^2
       +70\sum_v a_vy_v^2\right\},
\qquad |s|\le R<1.
\]
Indeed the stronger constants from the preceding calculation are \(1/(80\pi)\) and \(8\pi\). The displayed constants leave room for the physical translated endpoints of size \(O_R(N^{-1})\), which change the exponent by a bounded amount for a fixed graph and fixed strip. No assertion here concerns a growing graph as \(N\) tends to infinity.

## 3. The explicit action of one edge

The two-ended Newton action is the critical value in \(x\) of
\[
R(x,t)+R(x,u),\qquad
R(x,t)=\int_0^x\log(2\cos(2\pi v)+2\cos t)\,dv-2J(x).
\]
The logarithm is continued from \((x,t,u)=(1/4,0,0)\). Put \(p=\tan(t/2)\), \(q=\tan(u/2)\). The wire critical equation gives
\[
\tan^2(\pi x)=\frac1{1+p^2+q^2}.
\]
If \(\psi(t,u)\) denotes the selected critical value, direct differentiation of the integral yields
\[
\psi_t=-\frac1\pi\operatorname{arsinh}
               \frac{p}{\sqrt{1+q^2}},
\]
\[
\psi''(t,u)=\frac1{2\pi\sqrt{1+p^2+q^2}}
\begin{pmatrix}-(1+p^2)&pq\\pq&-(1+q^2)\end{pmatrix},
\qquad \det\psi''=\frac1{4\pi^2}.
\]
All square roots and inverse functions use their branches at the origin. The full packet action is the sum over its physical edges. Its Hessian at zero is therefore \(-\operatorname{diag}(d_v/(2\pi))\). On the real angular chamber the edge Hessian is strictly negative definite. For the complex contours, this real statement must be supplemented by an explicit holomorphic bound; it does not prove global complex nondegeneracy or the geometric filling assertion.
