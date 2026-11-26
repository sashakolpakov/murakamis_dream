# The geometric branch at a short internal vertex

Research note, 2 November 2026. The circle-tree construction supplies
an edge phase and an ordered collection of eight tetrahedra for each
edge. This note studies the geometry obtained by filling one vertex
while leaving all its neighbors complete. It proves a uniform
existence criterion for the selected geometric branch, including
zero crossing power. It does not estimate the corresponding finite
quantum sum.

## 1. The local filling problem

Let \(d\geq1\) be the number of edges incident to the vertex. In this
note \(d\) denotes that valence, not the quantum index \(N-1\).
Write \(n\in\mathbb Z\) for its original signed crossing power,
\(t\) for its boundary angle, and \(u_1,\ldots,u_d\) for the
angles at its neighbors. The edge phase is normalized by

\[
\psi(0,0)=\frac{v_{\rm oct}}\pi,
\qquad
\psi_t(t,u)=-\frac1\pi\operatorname{arsinh}
                  \bigl(\tan(t/2)\cos(u/2)\bigr).
\tag{1}
\]

Here \(v_{\rm oct}\) is the volume of a regular ideal octahedron.
All logarithms start at the complete structure \(t=u_j=0\).
The selected unit-charge phase at complete neighbors is

\[
F_{d,n}(t)=d\psi(t,0)+\frac{in}{4\pi}t^2-it.
\tag{2}
\]

For a cone deformation replace the last term by \(-i\lambda t\),
where \(0\leq\lambda\leq1\). Thus the primitive cone angle is
\(2\pi\lambda\). The original geometric marking is retained:
if \(n=\eta-2p\), with the original carrier
\(\eta\in\{-1,0,1\}\), the filled curve is
\(\mu+p\lambda_{\rm long}\). The subscript on
\(\lambda_{\rm long}\) distinguishes this longitude from the
cone parameter.

The equations below describe the branch in

\[
|\Re t|<\pi,\qquad \Im t<0.
\tag{3}
\]

**Proposition 1.** The unit-charge equation
\(F'_{d,n}(t)=0\) has a unique solution in (3) if and only if

\[
d+|n|>2.
\tag{4}
\]

When (4) holds, this solution is joined to the complete structure
by a unique positive cone branch for every
\(0<\lambda\leq1\). The derivative of the stationary equation
with respect to \(t\) never vanishes on that branch. All eight
tetrahedra in each of the \(d\) incident edge blocks have positive
imaginary shape parameter.

For internal vertices, therefore, the only failure of this selected
positive geometric branch is \(d=2,n=0\). The assertion is about
this branch and this decomposition. It does not assert that every
filling with a degenerate branch is nonhyperbolic.

## 2. Proof of the existence criterion

First suppose \(n>0\) and put

\[
t=2a-2ib,\qquad 0<a<\pi/2,\qquad b>0.
\]

For \(z=a-ib\), define

\[
R(z)=\sec z+\tan z
    =\frac{\cos a-i\sinh b}{\cosh b-\sin a}.
\]

Its real part is positive. On the logarithm continued from zero,

\[
\log R(z)=A-iB,
\qquad
A=\operatorname{artanh}\frac{\sin a}{\cosh b},
\qquad
B=\arctan\frac{\sinh b}{\cos a}.
\tag{5}
\]

The stationary equation is equivalent to

\[
nb=dA,
\qquad
na+dB=\pi\lambda,
\tag{6}
\]

or, equivalently,

\[
\sin a=\cosh b\tanh\left(\frac nd b\right),
\qquad
na+d\arctan\frac{\sinh b}{\cos a}=\pi\lambda.
\tag{7}
\]

For each \(a\in(0,\pi/2)\), the first equation in (7)
determines a unique \(b=b(a)>0\): its right side is strictly
increasing from zero to infinity as \(b\) increases. Moreover
\(b(a)\) is strictly increasing. The left side of the second
equation is then strictly increasing in \(a\). Its limits are
zero and \((n+d)\pi/2\). The upper limit follows because
\(b(a)\) tends to a finite positive number as
\(a\to\pi/2\), while the arctangent tends to \(\pi/2\).
This proves existence and uniqueness exactly when
\(0<\lambda<(n+d)/2\).

There is no additional solution in the negative-real half of (3).
The real part of the stationary equation there would require
\(nb=dA\), with \(nb>0\) and \(A<0\).

For \(n=0\), the real equation forces \(a=0\), and the
imaginary equation becomes

\[
d\arctan(\sinh b)=\pi\lambda.
\]

Consequently

\[
t_{d,0}(\lambda)
=-2i\operatorname{arsinh}\tan\frac{\pi\lambda}{d},
\qquad 0<\lambda<d/2.
\tag{8}
\]

At unit charge this is finite exactly when \(d>2\). In the
exceptional internal case \(d=2,n=0\), the imaginary part tends
to \(-\infty\) as \(\lambda\uparrow1\). For negative crossing
power use

\[
t_{d,-n}(\lambda)=-\overline{t_{d,n}(\lambda)}.
\tag{9}
\]

Finally,

\[
F_{d,n,\lambda}''(t)
=\frac{-d\sec(t/2)+in}{2\pi}.
\tag{10}
\]

The real part of \(\sec(t/2)\) is positive throughout (3).
Thus (10) has strictly negative real part and cannot vanish.
The branch extends holomorphically in small changes of all the
neighboring angles.

## 3. The original shapes and primitive periods

Let \(w=e^{it/2}=e^{b+ia}\). At complete neighboring angle, each
incident original edge block has the shapes

\[
(iR,iw,i/R,i/w),\qquad(i/R,iw,iR,i/w).
\tag{11}
\]

Both \(w\) and \(R\) have positive real part on the branch just
constructed. Their reciprocals do as well. Hence every shape in
(11) has positive imaginary part. Formula (9) replaces \(w\) by
\(\overline w\) and \(R\) by \(1/\overline R\), preserving
the same positivity. Formula (8) also gives positive shapes at
every \(d\geq3\).

The ordered face pairings and the primitive collar words are those
in the [circle-tree geometry paper](../papers/circle-tree-geometry/main.tex),
equations `ctg:pants`, `ctg:primitive-words`, and `ctg:increment`.
Their use here does not require the small bidisk estimate in that
paper. On the slice with neighboring angle zero, put
\(k=\cos(t/2)\). Its rational coordinates become

\[
E=\frac{1+ik}{1-ik},\qquad
R_{\rm eq}=\frac{k^2}{1+k^2},\qquad
H_0=\frac{1-\sin(t/2)}{1+\sin(t/2)},\qquad H_1=1,
\]

\[
Z_0=\frac{1+\sin(t/2)}{1-ik},\qquad
Z_1=\frac1{1-ik}.
\]

Here \(R_{\rm eq}\) is the equatorial vertex coordinate, distinct
from \(R=\sec(t/2)+\tan(t/2)\) in (11).
The denominators are nonzero because \(\Re k>0\) and
\(\Im\sin(t/2)<0\). The two additional apex denominators are
nonzero multiples of \(k(k+i)\) and \(k(k-i)\), respectively.
Thus the face formulas continue without singularities along the
whole cone branch. The shapes (11) remain positive; the products
of shapes at original interior edges remain one. Their total
angles are therefore constant multiples of \(2\pi\), and equal
\(2\pi\) by continuation from the complete end.

Concatenating the \(d\) original edge contributions gives

\[
U=-2\pi d\psi_t(t,0)-i\eta t,
\qquad V=2it,
\]

\[
U+pV=-2\pi\left(d\psi_t(t,0)+\frac{in}{2\pi}t\right)
     =-2\pi i\lambda.
\tag{12}
\]

These are full continued logarithmic periods. Their integer
winding ambiguity is zero at the complete end and stays constant
along the positive branch, by the log-link construction and the
period-limit argument in that paper. The core translation has
length

\[
\Re V=-2\Im t=4b>0.
\tag{13}
\]

The neighboring periods remain complete because
\(\psi_u(t,0)=0\). Thus the positive edge blocks fit the original
unfilled neighboring blocks. At \(\lambda=1\), (12) is the
original primitive filling with cone angle \(2\pi\).

The absolute volume normalization is fixed along this same path.
Set

\[
M_{d,n}(\lambda)
=\Re\left[d\psi(t(\lambda),0)
       +\frac{in}{4\pi}t(\lambda)^2
       -i\lambda t(\lambda)\right].
\]

Stationarity gives

\[
M_{d,n}'(\lambda)=\Im t(\lambda)=-2b(\lambda).
\tag{14}
\]

Schläfli's formula for the original positive block chain gives
the volume derivative
\(-\tfrac12(4b)(2\pi)=-4\pi b\), equal to
\(2\pi M_{d,n}'\). At \(\lambda=0\) there are \(2d\)
complete regular ideal octahedra. Therefore the volume contributed
by these blocks after the filling is

\[
2\pi M_{d,n}(1).
\tag{15}
\]

This calibration uses the original primitive slope, not merely the
exponentiated critical equation.

## 4. Uniform estimates as the valence grows

For \(d\geq3\), (6) implies

\[
b(\lambda)\leq
\operatorname{arsinh}\tan\frac{\pi\lambda}{d}
\leq\frac{\pi\lambda}{d}\sec\frac\pi d.
\tag{16}
\]

For the first inequality use
\(\arctan(\sinh b)\leq B\leq\pi\lambda/d\).
For the second use
\((\operatorname{arsinh}\tan x)'=\sec x\) on
\([0,\pi/d]\). Equality in the first inequality holds for
\(n=0\); it is strict for \(n\ne0\) and \(\lambda>0\).
Integrating (14) proves the all-power estimate

\[
0<d\psi(0,0)-M_{d,n}(1)
\leq \frac\pi d\sec\frac\pi d.
\tag{17}
\]

In particular, the complete-to-filled action loss is largest at
zero crossing power when \(d\geq3\). This comparison is uniform
over every signed integer \(n\).

There is also a simple uniform small-angle bound. If \(n\geq d\),
then \(a<\pi\lambda/n\leq\pi/d\). If \(0<n\leq d\), the
first equation in (7) gives
\(\sin a\leq\sinh b\leq\tan(\pi/d)\). Hence for
\(d\geq5\),

\[
|t_{d,n}(\lambda)|
\leq2\sqrt{
 \arcsin^2\!\left(\tan\frac\pi d\right)
 +\operatorname{arsinh}^2\!\left(\tan\frac\pi d\right)}.
\tag{18}
\]

For \(n=0\), the same inequality follows from (8). The bound
also holds for negative powers by (9). In particular, for every
\(d\geq256\), every signed \(n\), and every
\(0\leq\lambda\leq1\),

\[
|t_{d,n}(\lambda)|<\frac9d,
\qquad
d\psi(0,0)-M_{d,n}(1)<0.01228.
\tag{19}
\]

These constants follow from \(\pi/d<1/80\): both inverse
functions in (18) are less than
\((1001/1000)\pi/d\). The elementary inequalities
\(\pi<22/7\) and \(\sqrt2<10/7\) then give the first bound.
The second follows directly from (17). These bounds place every
crossing power at high valence in one fixed small geometric chart.

## 5. What happens to the remaining boundary variables

Near the selected point let \(t(\mathbf u)\) solve the stationary
equation for

\[
\sum_{j=1}^d\psi(t,u_j)+\frac{in}{4\pi}t^2-it,
\]

and let \(G_{d,n}(\mathbf u)\) be its stationary value. Evenness
in each \(u_j\) implies \(t_{u_j}(0)=0\). Consequently

\[
\frac{\partial^2 G_{d,n}}{\partial u_j\partial u_k}(0)
=-\delta_{jk}\frac{\cos(t_{d,n}(1)/2)}{2\pi}.
\tag{20}
\]

Its real part is negative definite, since
\(\Re\cos(t/2)>0\). Thus the geometric stationary action has
the boundary curvature needed for a further filling argument.
A whole-source theorem must still prove that this action actually
occurs in the original finite polynomial with nonzero amplitude,
and that its other contributions are smaller. Equation (20) alone
does not prove either statement.

## 6. A symmetry of the stationary equations

For positive \(d,n\), the equations have an exact symmetry under
interchanging these two integers. With the notation (5), put

\[
z'=B-iA=-i\overline{\log R(z)}.
\tag{21}
\]

On the continued branches,

\[
\log R(z')=b-ia,
\qquad
\cos z'=\frac1{\overline{\cos z}}.
\tag{22}
\]

For example, the second identity follows from
\(\cosh(\log R(z))=\sec z\). The first follows from
\(\tanh(\log R(z))=\sin z\), together with the specified
quadrant of each logarithm. Now (6) becomes

\[
dA=nb,
\qquad dB+na=\pi\lambda,
\]

which is the same system with degree \(n\), power \(d\), and
half-angle \(z'\). Uniqueness therefore identifies the selected
solutions. This is a symmetry of the local stationary equations.
No equivalence of quantum sums or of knot complements is asserted.

## 7. Two small internal vertices need a different factorial chart

The canonical joint edge interpolation has wire stationary point

\[
x=\frac1\pi\arctan k,
\qquad k=\cos(t/2),
\]

continued from \(k=1\). One of its original factorial bulk
conditions is

\[
\Re x+\frac{\Re t}{2\pi}<\frac12.
\tag{23}
\]

Positive shapes do not imply (23). For degree two and power one,
the selected solution has

\[
k=1+i.
\tag{24}
\]

This also follows from (22) and the two-crossing terminal value
\(k=(1+i)/2\). Here \(\Re\arctan k>\pi/4\), because
\(|k|>1\) and \(\Re k>0\). Also \(a=\Re(t/2)>\pi/4\),
since \(\Re\cos(2a-2ib)=\Re(2k^2-1)=-1\).
Thus (23) fails strictly.

For degree two and power two, uniqueness under (21) gives
\(a=\pi/4\) and \(\sinh b=1/\sqrt2\). Hence

\[
k=\frac{\sqrt3+i}{2},
\qquad \Re\arctan k=\frac\pi4.
\tag{25}
\]

This point lies exactly on the real boundary in (23). It is not a
degeneration of the positive hyperbolic tetrahedra. It is a failure
of that particular open factorial bulk condition. Conjugation
gives the corresponding statements for negative powers.

The degree-two powers \(\pm1\) also admit an exact finite-algebra
reduction, discussed in
[the two-boundary reduction note](research_degree_two_short_reductions.md).
That algebraic identity and the local symmetry (21) are separate
facts. Neither should be substituted for a global contour estimate
without checking how it acts on the full source and its marking.

## 8. Several nonadjacent short fillings

The geometric construction above can be made simultaneously at
any set \(S\) of pairwise nonadjacent original vertices, provided
\(d_s+|n_s|>2\) for each \(s\in S\). Keep every other original
vertex angle equal to zero. The stationary equation at a selected
vertex is then exactly its equation (7) or (8); no selected angle
appears in another selected equation. Every original edge belongs
to at most one selected star.

Allow the cone parameters \(\lambda_s\) to vary independently
in \([0,1]\). The full original face-pairing formulas apply on
this product of branches. Every tetrahedron stays positive. At an
unselected vertex all incident contributions to its meridian
equation vanish, since \(\psi_t(0,t_s)=0\). Its longitude period
also vanishes. Thus those cusps remain complete while the selected
primitive slopes are filled. This proves the geometric assembly
with the original circle-tree marking; it does not infer completeness
from a scalar stationary value alone.

Let \(E_0\) be the edges with neither endpoint in \(S\). At the
end of these short fillings, the complete partially filled exterior
has volume

\[
\operatorname{Vol}(Y')
=2|E_0|v_{\rm oct}
 +2\pi\sum_{s\in S}M_{d_s,n_s}(1).
\tag{26}
\]

Each original edge block is counted once. Equation (26) follows
either by summing the original positive fundamental chains or by
integrating Schläfli's formula over the product cone path, starting
at the original complete exterior. The full logarithmic periods
are transported along that same path, so no new winding choice is
made at its endpoint.

The geometric action for the remaining angles \(\mathbf u\) is

\[
P(\mathbf u)
=\sum_{vw\in E_0}\psi(u_v,u_w)
 +\sum_{s\in S}G_{d_s,n_s}((u_v)_{v\sim s}).
\tag{27}
\]

It is separately even and holomorphic near zero. Its Hessian there
is diagonal, with

\[
-\Re P_{u_vu_v}(0)
=\frac1{2\pi}\left(
 \deg_{E_0}(v)
 +\sum_{s\in S:\,s\sim v}\Re\cos(t_{d_s,n_s}(1)/2)
 \right)>0.
\tag{28}
\]

The strict inequality uses connectedness of the original tree and
the presence of at least one remaining vertex. Every remaining
vertex meets either an edge in \(E_0\) or a selected star.

If a subsequent long-filling argument constructs sufficiently
small remaining angles \(\mathbf u(c)\), for
\(0\leq c\leq1\), the selected angles extend by the implicit
function theorem using (10). They remain close to the already
short-filled points. Positivity therefore persists. Differentiating
the stationary values in (27) gives the original remaining
peripheral derivatives: the derivatives through the selected
angles vanish by their stationary equations. Hence the subsequent
primitive cone equations, logarithmic periods and volume
differential are the original ones on this deformed partially
filled exterior. Their additive volume constant is (26).

This supplies the geometric part of a further-filling theorem.
The separate analytic requirement is a whole finite-source
asymptotic for every selected star and a global estimate in all its
unfilled angles. The high-valence range is treated in
[the short internal-vertex source theorem](research_high_degree_short_internal_vertex.md).
