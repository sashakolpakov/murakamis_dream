# Positive geometry for a connected set of short fillings

Research note, 2 November 2026. The
[joint source theorem](research_connected_short_filling_clusters.md)
estimates the whole finite polynomial of a connected selected
subtree. This note identifies its selected action with the original
primitive geometric filling in an explicit range. The proof includes
edges whose two endpoints are both selected. It does not treat them
as independent terminal blocks.

## 1. A larger explicit positive coordinate chart

Use the two-octahedron coordinates and ordered tetrahedra of the
[circle-tree geometry paper](../papers/circle-tree-geometry/main.tex).
For boundary angles \(t,u\), put

\[
y=\tan(t/2),\quad z=\tan(u/2),\quad
k=(1+y^2+z^2)^{-1/2},\quad k(0,0)=1,
\]

\[
E=\frac{1+ik}{1-ik},\qquad
H_0=\frac{1-ky}{1+ky},\qquad
H_1=\frac{1-kz}{1+kz},
\]

\[
R=\frac{1+z^2}{2+y^2+z^2},\qquad R_1=1-R,
\qquad Z_j=\frac{1+E}{1+H_j}.
\tag{1}
\]

The two octahedra have common equatorial tuple
\((0,\infty,1,R)\) and apices

\[
(A_+,B_+)=\left(Z_0,\frac{RZ_1}{Z_1-R_1}\right),
\qquad
(A_-,B_-)=\left(\frac{Z_0}{E},
                         \frac{RZ_1}{Z_1-ER_1}\right).
\tag{2}
\]

The order of the minus tetrahedra is reversed as specified in that
paper. At \(t=u=0\), all eight oriented shapes are \(i\).

**Lemma 1.** On the closed complex bidisk
\(|t|,|u|\leq1/64\), every denominator in (1)--(2) is nonzero.
All eight original oriented tetrahedron shapes \(w\) satisfy

\[
                         |w-i|<1/8.
\tag{3}
\]

In particular every tetrahedron is positive, and the original
face maps and edge returns continue holomorphically throughout
this bidisk.

**Proof.** The following rational bounds suffice. Set

\[
r=\frac1{127},\quad h=\frac1{16000},\quad
e=\frac1{15000},\quad z_0=\frac1{175},\quad
r_0=\frac1{32000},\quad a_0=\frac3{500}.
\]

First, \(|y|,|z|<r\). Indeed, for \(|v|\leq1/128\),
the power series for sine and cosine give
\(|\tan v|\leq |v|/(1-|v|^2)\leq128/16383<1/127\).
The binomial series then gives

\[
|k-1|\leq(1-2r^2)^{-1/2}-1<h.
\]

The last inequality follows by squaring the positive quantities:
\((1+h)^2(1-2r^2)>1\). Also

\[
|E-i|\leq\frac{h}{1-h/\sqrt2}
          <\frac{h}{1-5h/7}<e.
\]

The identities
\(Z_0=(1+E)(1+ky)/2\) and
\(Z_1=(1+E)(1+kz)/2\) therefore imply

\[
\left|Z_j-\frac{1+i}{2}\right|
<\frac{e+(10/7+e)(1+h)r}{2}<z_0.
\tag{4}
\]

Direct subtraction in the formula for \(R\) gives
\(|R-1/2|<r^2/(2(1-r^2))<r_0\). The four apex
perturbations are all less than \(a_0\). For \(A_+\) this
follows from (4), and for \(A_-\) the bound is

\[
\frac{z_0+(5/7)e}{1-e}<a_0.
\]

For \(B_+\), subtract its complete value \((1-i)/2\)
before estimating the numerator of the quotient in (2).
The resulting bound is

\[
\frac{z_0/2+r_0+r_0z_0}{1/2-z_0-r_0}<a_0.
\tag{5}
\]

For \(B_-\), subtract \((1+i)/2\). The corresponding bound is

\[
\frac{z_0/2+r_0+(5/14)e+r_0z_0+(5/7)er_0}
     {1/2-z_0-r_0-e/2-er_0}<a_0.
\tag{6}
\]

The denominators in (5)--(6) are positive. These estimates
also verify the required nonvanishing denominators in (1)--(2).

Within either original octahedron, every nonzero difference
between complete finite vertices occurring in a tetrahedron
has modulus at least \(1/2\). The finite vertices have moved
by less than \(a_0\), so each such difference has changed
by relative size less than
\(\delta=4a_0=3/125\). A cross ratio is a quotient of two
products of these differences. Since its complete value is
\(i\),

\[
|w-i|\leq\frac{4\delta+2\delta^2}{(1-\delta)^2}<\frac18.
\]

Factors involving infinity simply omit one of the differences.
This proves (3). The rational face formulas are regular, and
the positive oriented shape branch is fixed by continuation
from the complete point. \(\square\)

## 2. The selected connected subtree

Let \(S\) be a nonempty connected proper set of vertices of a
fixed ordered circle tree. Put \(k_S=|S|\), and let \(E_S\)
contain the original edges with at least one endpoint in \(S\).
Write \(m=|E_S|\). Every edge in \(E_S\), including an
edge joining two selected vertices, is counted once.

Retain the original degree \(d_v\), signed power \(n_v\),
carrier \(\eta_v\), and integer filling coefficient \(p_v\)
at each selected vertex, with

\[
n_v=\eta_v-2p_v.
\tag{7}
\]

All other vertex angles are zero for now. The incident-edge phase is

\[
\Psi_S(\mathbf t)
=\sum_{vw\in E_S,\ v,w\in S}\psi(t_v,t_w)
 +\sum_{vw\in E_S,\ v\in S,\ w\notin S}\psi(t_v,0).
\tag{8}
\]

Assume the joint analytic criterion (3) of the source theorem and,
in addition,

\[
\sqrt{d_v^2+n_v^2}\geq448\qquad(v\in S).
\tag{9}
\]

That theorem constructs the entire selected cone-charge branch,
starting at the complete structure, with

\[
(\Psi_S)_{t_v}+\frac{in_v}{2\pi}t_v=ic,
\qquad 0\leq c\leq1,
\]

\[
|t_v(c)|\leq\frac7{\sqrt{d_v^2+n_v^2}}\leq\frac1{64},
\qquad \Im t_v(c)<0\quad(c>0).
\tag{10}
\]

Lemma 1 applies simultaneously to every original incident edge.
The boundary face ratios of the geometric paper depend only on
the angle of their common vertex, so they identify the original
ordered pages exactly. Their products and all original internal
edge returns are the same rational identities as in the complete
configuration. Positivity fixes their winding numbers. Thus the
original edge gluings, rather than just their exponentiated
stationary equations, hold along the whole path.

At any outside vertex, the incident selected-edge derivative is
\(\psi_t(0,t_v)=0\). Its longitude period is zero as well.
Those auxiliary cusps remain complete. The main cusps have the
same complete puncture products and continued full periods as
in the original marked construction. The small positive
deformation preserves their complete cusp metrics.

## 3. Primitive slopes and absolute volume

The original ordered meridian and disk-longitude words give

\[
U_v=-2\pi(\Psi_S)_{t_v}-i\eta_v t_v,
\qquad V_v=2it_v.
\tag{11}
\]

The full logarithmic periods equal (11), because their possible
integer differences vanish at the complete end and are constant
under the positive continuation. Substitution of (7) and (10)
gives

\[
U_v+p_vV_v=-2\pi ic.
\tag{12}
\]

Each selected cusp therefore completes with its original
primitive filling curve, cone angle \(2\pi c\), and positive
core length \(-2\Im t_v(c)\). At \(c=1\) these are smooth
fillings. All unfilled auxiliary cusps and all main cusps remain
complete.

Define the stationary value

\[
\mathcal S(c)=\Psi_S(\mathbf t(c))
 +\frac{i}{4\pi}\sum_{v\in S}n_vt_v(c)^2
 -ic\sum_{v\in S}t_v(c).
\tag{13}
\]

Stationarity gives
\(\frac{d}{dc}\Re\mathcal S(c)=\sum_{v\in S}\Im t_v(c)\).
Schläfli's formula for the original positive tetrahedral chain
has exactly \(2\pi\) times this derivative, by (12) and the
displayed core lengths. At the complete end the edges in
\(E_S\) contribute \(2m\) regular ideal octahedra, while
\(\mathcal S(0)=m v_{\rm oct}/\pi\). It follows that the
volume contributed by the selected incident blocks after
filling is

\[
                         2\pi\Re\mathcal S(1).
\tag{14}
\]

For the full complete partially filled exterior \(Y'\), let
\(E_0\) be the edges with both endpoints outside \(S\).
Then

\[
\operatorname{Vol}(Y')
=2|E_0|v_{\rm oct}+2\pi\Re\mathcal S(1).
\tag{15}
\]

This proves the absolute normalization, including the constant
term. It identifies the action of the joint finite-source
theorem with the actual marked hyperbolic volume.

## 4. The all-power high-degree range

If \(k_S\geq2\) and

\[
d_v\geq256k_S\qquad(v\in S),
\tag{16}
\]

then the source theorem's joint criterion holds for every
fixed signed choice of \(n_v\), including zero powers.
Furthermore \(d_v\geq512>448\), so (9) also holds. Thus
(14)--(15) apply to the full all-power range (16).

For \(k_S=1\), the exact isolated-vertex geometry is stronger
and needs no small-chart assumption: see
[the isolated-vertex proof](research_isolated_internal_vertex_geometry.md).
In particular it supplies the geometric identification when
\(d_v\geq256\), which is the singleton instance of (16).

The general analytic criterion without (9) can reach a larger
geometric parameter range. Lemma 1 alone does not identify
that entire range, and no such additional conclusion is
claimed here.

## 5. Further fillings of the remaining cusps

The selected Hessian in the joint source proof is invertible.
Hence the already filled selected angles extend holomorphically
when the outside boundary angles \(\mathbf u\) vary near
zero, while keeping all selected primitive equations at
\(c=1\). The stationary value becomes the same separately
even holomorphic function \(S(\mathbf u)\) as in the source
theorem. Its second derivatives at zero are

\[
S_{u_iu_j}(0)
=-\delta_{ij}\frac{\cos(t_{v(i)}(1)/2)}{2\pi}.
\tag{17}
\]

Their real diagonal entries are strictly negative. An outside
vertex of a tree meets at most one vertex of a fixed connected
selected subtree, so the boundary labels in (17) are distinct.

For a sufficiently small subsequent cone path in these outside
angles, all original tetrahedra stay positive. The original
primitive period formulas continue along the same path.
Derivatives of the selected stationary value through the
selected angles vanish by their stationary equations, so
its derivatives in \(\mathbf u\) give precisely the
remaining original peripheral derivatives. The absolute
volume anchor for this second filling stage is (15).

Consequently a long-filling theorem applied to the joint
boundary polynomial uses the actual partially filled
exterior and its original primitive slopes. The geometric
comparison does not require replacing the internal edges
by independent one-vertex contributions.

## 6. Reproduction of the coordinate bounds

The rational inequalities in Lemma 1 are checked by

```sh
python3 experiments/audit_connected_short_geometry_chart.py
```

The script verifies every displayed rational comparison,
including denominator positivity and the shape bound.
The bounds come from the written analytic estimates;
they are not sampled tests of tetrahedron shapes.
