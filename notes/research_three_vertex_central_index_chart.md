# A quantitative central index chart for the retained three-crossing vertex

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The two-index phase of the exact retained vertex has an explicit
critical-point equation and a uniform accretivity domain. The domain
below is substantially larger than an unspecified infinitesimal
neighborhood. It controls the central index contour and excludes the
other algebraic critical branch from the original triangular support.
It does not yet bound the complementary low-index strips, finite
endpoints or cotangent aliases for every parameter in the domain.

## 1. Exact critical branches and their logarithms

Use the index phase and exact analytic interpolation from
[the retained-vertex theorem](research_traced_three_vertex_endpoint.md),
Section 9, and
[the root-product interpolation](research_root_pochhammer_interpolation.md).
Thus
\[
 \begin{split}
 F(s,t;X,Y)={}&\mathcal J(s+t)
  +\frac{i\pi}{2}\{s+t-(s+t)^2\}
  +s\log X+t\log Y-I_X(s)-I_Y(t),\\
 I_X(s)={}&\int_0^s\log(1-Xe^{-2\pi iu})\,du,
 \qquad U=e^{-2\pi is},\quad V=e^{-2\pi it}.
 \end{split}
 \tag{1}
\]
The branches continue from
\(X=Y=(1+i\sqrt3)/4\), \(s=t=1/3\).
The exact derivative equations are
\[
 e^{F_s}=\frac{X(1-UV)}{1-XU},\qquad
 e^{F_t}=\frac{Y(1-UV)}{1-YV}.
 \tag{2}
\]
Put \(\alpha=X^{-1}-1\), \(\beta=Y^{-1}-1\). At an
exponentiated critical point,
\[
 U(1-V)=\alpha,\qquad V(1-U)=\beta,
 \quad U-V=\alpha-\beta,
 \quad
 \Delta=1-2(\alpha+\beta)+(\alpha-\beta)^2.
 \tag{3}
\]
The two solutions, counted with multiplicity, are
\[
 U_\pm=\frac{1+\alpha-\beta\pm\sqrt\Delta}{2},
 \qquad
 V_\pm=\frac{1-\alpha+\beta\pm\sqrt\Delta}{2}.
 \tag{4}
\]
At the homogeneous point, \(\sqrt\Delta=2+i\sqrt3\), and
the selected solution is the minus sign.

**Lemma 1.** Suppose a solution \((U,V)\) of (3) lies in the
open lower-left quadrant in each coordinate, while \(X,Y\) lie
in the open first quadrant and
\(|X|,|Y|,|XU|,|YV|<1\). Define
\[
 s=\frac{i}{2\pi}\Log U,\qquad
 t=\frac{i}{2\pi}\Log V,
 \qquad -\pi<\arg U,\arg V<-\pi/2.
 \tag{5}
\]
Then \(1/4<\Re s,\Re t<1/2\), and the equations are
\(F_s=F_t=0\) with the actual logarithmic branches, not just
modulo \(2\pi i\). The other algebraic solution is
\((1-V,1-U)\). It has no logarithmic lift in the open original
index triangle \(\Re s>0,\Re t>0,\Re(s+t)<1\).
The selected solution is simple.

*Proof.* Subtracting the equations in (3) and solving the resulting
quadratic proves (4). Replacing \((U,V)\) by \((1-V,1-U)\)
preserves both equations, so gives its other solution.
The two solutions cannot agree when \(U,V\) have negative real
parts, because equality would require \(U+V=1\).

For (5), \(UV\) is in the upper half-plane and \(XU,YV\)
are in the lower half-plane. Consequently the continuous logarithms
in (2) have argument ranges
\[
 0<\arg X,\arg Y<\pi/2,\quad
 -\pi<\arg(1-UV)<0,\quad
 0<\arg(1-XU),\arg(1-YV)<\pi/2.
 \tag{6}
\]
The last bounds also use \(|XU|,|YV|<1\). These branches
agree with (1): \(\Re(s+t)\in(1/2,1)\) and
\(1-e^{-2\pi i(s+t)}=2i e^{-\pi i(s+t)}\sin\pi(s+t)\)
fix the numerator branch by continuation. Hence the imaginary
parts of \(F_s,F_t\) lie strictly between \(-3\pi/2\)
and \(\pi/2\). Equations (2)--(3) force them to be integer
multiples of \(2\pi\), so both are zero.

The other solution has both coordinates in the upper-right quadrant.
Their only logarithmic lifts with real parts in \((0,1)\) have
real parts in \((3/4,1)\). Their sum exceeds one, excluding
that branch from the original triangle. \(\square\)

The inverse parameterization is particularly simple:
\[
          X=\frac1{1+U-UV},\qquad
          Y=\frac1{1+V-UV}.
 \tag{7}
\]
Thus Lemma 1 is a source-specific algebraic branch test. It is not
an assertion that every first-quadrant parameter pair passes that test.

## 2. Uniform horizontal concavity on a specified box

Consider parameters satisfying
\[
 \Re X,\Im X,\Re Y,\Im Y\ge\frac2{25},\qquad
                         |X|,|Y|\le\frac45,
 \tag{8}
\]
and index variables in the closed box
\[
 \frac14\le\Re s,\Re t\le\frac{49}{100},\qquad
                     |\Im s|,|\Im t|\le\frac3{100}.
 \tag{9}
\]
All assertions below persist on a slightly larger compact
neighborhood when a fixed strict margin is added to its edges.

**Theorem 2.** On (8)--(9), the exact summand interpolation is
holomorphic, has the uniform holomorphic asymptotic symbol of the
retained-vertex theorem, and satisfies
\[
                        -\Re F''(s,t)\succ\frac9{100}I_2.
 \tag{10}
\]
In particular its real phase is strictly concave on every horizontal
index plane in (9). If the explicit selected point (4)--(5) belongs
to the box, it is the unique maximum on its horizontal plane.

*Proof.* Since \(2\pi(3/100)<33/175\),
\[
 e^{2\pi|\Im s|},e^{2\pi|\Im t|}
 <\frac1{1-33/175}=\frac{175}{142}<\frac54.
 \tag{11}
\]
Thus \(|XU|,|YV|<1\), and the exact root-product interpolants
are holomorphic and nonzero on a neighborhood of the box. The
sine factorial is also holomorphic and nonzero there, because
\(1/2\le\Re(s+t)\le49/50<1\). Its existing uniform
Stirling estimate and the root-product expansion give the actual
analytic symbol, with no error introduced at the lattice values.

Differentiation of (2) gives the exact decomposition
\[
 -\Re F''
 =2\pi\Im\left(\frac{UV}{1-UV}\right)
       \begin{pmatrix}1&1\\1&1\end{pmatrix}
 -2\pi\begin{pmatrix}
  \Im\{XU/(1-XU)\}&0\\
 0&\Im\{YV/(1-YV)\}
 \end{pmatrix}.
 \tag{12}
\]
The first coefficient is nonnegative: \(UV\) has nonnegative
imaginary part when \(1/2\le\Re(s+t)<1\).
For the first diagonal term, put \(\theta=2\pi\Re s\).
Then \(\pi/2\le\theta<\pi\), and
\[
 -\Im(XU)
 =e^{2\pi\Im s}\{\Re X\sin\theta-\Im X\cos\theta\}
 >\frac45\frac2{25}.
 \tag{13}
\]
Here \(\sin\theta-\cos\theta\ge1\), and (11) bounds the
negative height as well. Since \(|1-XU|<2\),
\[
 -2\pi\Im\frac{XU}{1-XU}
 =\frac{-2\pi\Im(XU)}{|1-XU|^2}
 >\frac{4\pi}{125}>\frac{12}{125}>\frac9{100}.
 \tag{14}
\]
The other diagonal term has the same bound. Adding the nonnegative
rank-one term proves (10).

On the horizontal plane through an actual critical point, integrate
the Hessian along the straight segment from that point. This gives
\(\Re F(s,t)\le\Re F(s_c,t_c)
-(9/200)(|s-s_c|^2+|t-t_c|^2)\) for points on that plane
in the box, proving the maximum assertion. \(\square\)

## 3. What remains outside this chart

The inequalities (8)--(9) are quantitative, but no claim is made that
every complete-ended path satisfies them. That geometric enclosure
requires a separate proof; qualitative positivity and the localization
theorem alone do not supply these particular constants.

Even when the selected point passes this test, (10) bounds only the
central horizontal integral. The corner-deleted original sum still
contains low-index strips and an upper triangular boundary. A larger
packet theorem must bound those actual terms and the cotangent aliases
relative to the selected action. The existence of a unique algebraic
critical branch in the original triangle is not by itself that bound.

The [focused exact checker](../experiments/check_three_vertex_central_index_chart.py)
and its [record](../repro/results/research-three-vertex-central-index-chart.json)
verify the quadratic branch identities and the rational constants.
They do not infer a global contour or a path enclosure from samples.
