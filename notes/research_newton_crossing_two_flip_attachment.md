# Two diagonal flips at an actual Conway boundary

Research note, 2 November 2026. The two Newton crossing
tetrahedra admit a complete attachment table at an actual
four-punctured boundary assembled from two all-white
Conway output faces. The calculation retains the original
white transitions and every old auxiliary peripheral
curve. It can be iterated for a signed crossing word.

There is a necessary restriction. A general intermediate
Conway quadrilateral is a gluing face, not the physical
four-punctured boundary of a tangle. At a masked side,
one of the recorded matrices is only a completion map.
Such a matrix cannot be used as an existing face
identification. The theorem below therefore requires
an actual all-white interface. It does not assert that
every masked output can be replaced by this interface.

## 1. When the doubled quadrilateral is an actual boundary

Use the ordered Conway output face
\(Q=(C_0,C_1,C_2,C_3)\) and its boundary mask from
[the strict geometric assembly](../papers/strict-conway-geometry/complete.tex).
Assume that its mask is zero: the faces adjacent to
all four edges of \(Q\) are actual white faces.
Every type-\(A\) output has this property.

At the strict original geometry, the mask invariant
also says that \(Q\) is a maximal, nondegenerate
supported quadrilateral. Its four adjacent maximal
white faces are distinct. Indeed the supporting
plane of a different face meets the plane of \(Q\)
in one line. It cannot contain two distinct edges
of this nondegenerate quadrilateral; if the planes
coincided, maximality would merge that face with
\(Q\). This remains true after all earlier
white-face mergers.

In each original projection copy take the output disk
and a thin band along each of its four adjacent white
faces. The four bands are disjoint away from the four
main ends: their cores are the four distinct edges of
the nondegenerate output quadrilateral. The actual
white identifications join the two copies along these
bands. The resulting surface is the double of a disk
with four boundary points removed, hence a sphere
with four punctures.

The supporting-plane argument is used to choose the
embedded bands in this strict reference cut. Their
subsequent transport is topological, through the
same marked cell decomposition. We do not assert
that a deformed or crossing-modified boundary
quadruple remains a planar convex face. At later
steps the actual boundary strips are given by the
attachment table itself.

This construction takes place in the original reversible
cut. The four output corners are the four active terminal
singletons; each puncture links one original main end.
The other main vertices are consumed terminal pairs,
and every auxiliary apex and its disk collar lie on
the retained side of the output. Thus the doubled
surface is embedded, has the original four end labels,
and is disjoint from the auxiliary torus collars.
It is an actual separating boundary of the retained
piece. The argument uses the zero mask at every side.

At a masked side there is instead a shaded face, and
the corresponding completion matrix is supplied only
after an additional piece has been attached. Doubling
the two output quadrilaterals across that matrix would
invent a strip that is not present in the cut. The
general warning in the geometric paper therefore
still applies to such an output.

## 2. The two copies in one developed frame

Use the coordinates proved in
[the marked-flag calculation](research_newton_crossing_marked_flags.md):
\[
 Y=E,\qquad V=(1-R)/R,\qquad
 p=\frac{V}{(V+1)(Y-1)},\qquad d=\frac1{Y-1}.
 \tag{1}
\]
The input change of frame
\[
                         N(w)=\frac{w-1}{1-E}
                         \tag{2}
\]
puts the original cyclic quadruple
\((0,\infty,1,R)\) in the order
\[
                              Q=(d,\infty,0,p).
                              \tag{3}
\]
Let \(W_j\) be the four original white matrices and put
\(S_j=NW_jN^{-1}\). Convenient projective representatives
are
\[
 \begin{aligned}
 S_0&=\begin{pmatrix}1&1\\0&Y\end{pmatrix},&
 S_1&=\begin{pmatrix}1&0\\0&Y\end{pmatrix},\\
 S_2&=\begin{pmatrix}
 V/(V+1)&0\\-(Y-1)^2&VY/(V+1)
 \end{pmatrix},&
 S_3&=\begin{pmatrix}
 (VY-V+Y)/(V+1)&-V/(V+1)\\
 (Y-1)^2&(-VY+V+1)/(V+1)
 \end{pmatrix}.
 \end{aligned}
 \tag{4}
\]
Each \(S_j\) goes from the first projection copy to
the second along its indicated white side. Both
copies use the same four normalized corner flags.
In particular
\[
                         S_0^{-1}(w)=Yw-1
                         \tag{5}
\]
fixes \(d,\infty\) and takes \(0\) to \(-1\).

Triangulate each output quadrilateral across the
diagonal \(d0\), which is \(C_0C_2\) in the original
order. This is the diagonal already used for the
leaf volume calculation. If the adjacent cut cells
have another retained boundary subdivision, use a
common subdivision of their actual topological
faces; it is not permissible to omit the resulting
cell-chain terms in a regulator computation.

## 3. The complete local face attachment

Attach the tetrahedron
\[
                         T_0=(p,\infty,d,0)
                         \tag{6}
\]
to the two triangles of the first copy. It replaces
the diagonal \(d0\) by \(p\infty\). Its two new
triangles are
\((p,\infty,0)\) and \((p,\infty,d)\).

The second copy has a triangle with original vertices
\((\infty,d,0)\). Develop it across side \(0\) using
\(S_0^{-1}\). Its vertices become
\((\infty,d,-1)\). It is adjacent to the new first-copy
triangle \((p,\infty,d)\) along the edge \(d\infty\).
Attach
\[
                         T_1=(p,-1,d,\infty)
                         \tag{7}
\]
to these two triangles. This replaces that edge by
\(p(-1)\).

For precision, face numbers below denote the omitted
vertex in the orders (6)--(7).

| Tetrahedron face | Its developed vertices | Attachment or remaining face |
| --- | --- | --- |
| \(T_0,0\) | \((\infty,d,0)\) | First input-copy triangle |
| \(T_0,1\) | \((p,d,0)\) | Other first input-copy triangle |
| \(T_0,2\) | \((p,\infty,0)\) | Retained output triangle |
| \(T_0,3\) | \((p,\infty,d)\) | Joined to \(T_1,1\), with opposite face orientation |
| \(T_1,0\) | \((-1,d,\infty)\) | Second input-copy triangle, developed by \(S_0^{-1}\) |
| \(T_1,1\) | \((p,d,\infty)\) | Joined to \(T_0,3\) |
| \(T_1,2\) | \((p,-1,\infty)\) | New output triangle |
| \(T_1,3\) | \((p,-1,d)\) | New output triangle |

The unused triangle of the second input copy is
carried unchanged. Thus all six exterior faces of
the two-tetrahedron ball are accounted for: three
attach to the old boundary and three belong to
the changed boundary.

Each step attaches a ball along the disk formed by
two adjacent boundary triangles. Topologically this
is a diagonal exchange in a boundary collar; it
does not create a handle or an auxiliary cusp.
The unchanged portion of the boundary has its
identity collar. The two exchanges, together with
the ordered output labeling below, specify the
marked crossing collar.

The common triangular face cancels as an oriented
chain because
\[
       -(p,\infty,d)-(p,d,\infty)=0.
       \tag{8}
\]
The ordered tetrahedron shapes are respectively
\(-V\) and \(-U\), where
\[
               X=Y+(Y-1)/V,\qquad U=-Y(1+V).
               \tag{9}
\]
These are precisely the original Newton crossing
equations. Their positivity on a particular real
triangle is proved in the marked-flag note; no
positivity of an assembled word is assumed here.

## 4. Every output white transition

The two new triangles from \(T_1\) form a quadrilateral
with ordered vertices
\[
                              Q'=(d,-1,\infty,p).
                              \tag{10}
\]
This is one output copy. To assemble the other, retain
the triangle \((p,\infty,0)\) of the original first
copy. Develop the unused original second-copy triangle
\((p,d,0)\) across side \(2\), using \(S_2^{-1}\).
It joins the retained triangle along \(p0\).

The following affine change of frame sends that entire
second output quadrilateral to the same four flags
as (10):
\[
                         M(w)=\frac{p+1}{p}w-1.
                         \tag{11}
\]
Indeed \(M\) fixes \(p,\infty\), sends \(0\) to \(-1\),
and
\[
                         M S_2^{-1}(d)=d.
                         \tag{12}
\]
This is an equality of the fourth flags as well as
the first three.

Following the four actual side strips now gives the
entire output white-transition table:
\[
 \begin{array}{c|c|c}
 j&\text{output side}&\text{transition from first to second copy}\\ \hline
 0&d\,(-1)&M S_2^{-1}S_0\\
 1&(-1)\,\infty&M S_1^{-1}S_0\\
 2&\infty\,p&M\\
 3&p\,d&M S_2^{-1}S_3 .
 \end{array}
 \tag{13}
\]
For example, at side \(0\), first return to the old
second-copy frame by \(S_0\), then develop that frame
across old side \(2\), and finally apply (11).
Side \(1\) first returns by \(S_0\) and crosses
old side \(1\) to the retained first-copy triangle.
Side \(2\) lies between the new quadrilateral and
that retained triangle in the same old frame.
Side \(3\) crosses the original side \(3\) and is
then put in the second output frame. These are
compositions of actual face maps.

Normalize (10) to the usual order \((0,\infty,1,R')\)
by
\[
                   L(w)=\frac{w-d}{w+1},\qquad
                   R'=L(p)=\frac1{1+U}.
                   \tag{14}
\]
Let \(S'_j\) denote the entries in the last column
of (13). Direct substitution gives
\[
                         LS'_jL^{-1}\sim W_j(X,R')
                         \quad(j=0,1,2,3),
                         \tag{15}
\]
where \(\sim\) means equality of projective matrices.
Using the displayed representatives, their scalar
ratios to \(W_j(X,R')\) are
\[
 \frac{V+1}{V},\quad
 1,\quad
 \frac{VY+Y-1}{Y(V+1)},\quad
 -\frac{VY+Y-1}{V},
 \tag{16}
\]
respectively. Every ratio is nonzero in this regular
chart. Thus the output has exactly the original
white-table form, including translations and shears.
All four sides are actual white strips, so another
crossing layer can be attached.

## 5. The crossing word and the auxiliary primitive curves

The layer changes the based main meridians by
\[
 (a,b,c,d_{\rm mat})
       \longmapsto(a^{-1}ba,a,c,d_{\rm mat}).
       \tag{17}
\]
This holds already for the based side paths, before
specializing them to matrices. In the input order
they are
\[
 a=S_1^{-1}S_0,\qquad b=S_2^{-1}S_1,\qquad
 c=S_3^{-1}S_2,\qquad d_{\rm mat}=S_0^{-1}S_3.
 \tag{17a}
\]
Using \(S'_0,\ldots,S'_3\) from (13) gives
\[
 \begin{aligned}
 (S'_1)^{-1}S'_0
    &=S_0^{-1}S_1S_2^{-1}S_0=a^{-1}ba,\\
 (S'_2)^{-1}S'_1&=S_1^{-1}S_0=a,\\
 (S'_3)^{-1}S'_2&=S_3^{-1}S_2=c,\\
 (S'_0)^{-1}S'_3&=S_0^{-1}S_3=d_{\rm mat}.
 \end{aligned}
 \tag{17b}
\]
All intermediate changes of frame cancel in these
words. Thus the assertion uses the actual side
identifications, not faithfulness of a particular
matrix representation.
The under-end is developed from \(0\) to \(-1\)
by the original \(a^{-1}\) transport; the over-end
keeps its fixed flag and the other two end labels
are retained. This fixes the crossing sign relative
to the original ordered strand convention. The
inverse crossing is the same collar read backwards.
Physical turns transport its whole ordered boundary;
they are not erased as trivial endpoint permutations.

All old auxiliary torus collars are disjoint from
the attaching surface in Section 1. The two boundary
exchanges therefore extend by the identity on those
collars. In particular an old disk longitude
\(\lambda\) and its once-crossing meridian \(\mu\)
are transported as the original two curves. There
is no slope shear, multiple longitude, or additional
meridian winding at an old auxiliary circle.

One can record their full based holonomies explicitly.
If their basepoint is carried through the retained
old first-copy triangle, the change from the original
geometric frame to the normalized second output frame
is
\[
                              K=L M N.
                              \tag{18}
\]
Thus for either \(\gamma=\mu,\lambda\),
\[
               \rho_{\rm out}(\gamma)
                       =K\rho_{\rm in}(\gamma)K^{-1}.
                       \tag{19}
\]
The selected eigenflag is transported by the same
\(K\). If the basepoint lies on the retained old
second-copy triangle, use \(K=LMS_2^{-1}N\).
The two prescriptions differ by exactly the old
based side path, not by a peripheral shear.

Consequently the similarity multipliers, selected
logarithms and primitive period normalizations
of every old auxiliary cusp are retained. This
conclusion uses the literal collar identification,
not just conjugacy of a reduced character. If a
new auxiliary leaf is attached outside the word,
its own original shaded maps and carrier are
inserted there once; (19) does not create an
extra carrier at the old circles.

**Proposition.** Starting from an actual all-white
output of the original cut, any finite signed
crossing word can be attached by the two-flip
collars above and their inverses, provided its
developed charts remain regular. This gives its
actual ordered face maps and transports all old
auxiliary primitive curves. It is a statement
about the marked idealized cell complex and its
representation. It does not assert that all its
tetrahedra are positive.

## 6. What this says about a folded short region

The construction supplies an alternative to treating
the crossing phase only as a rational Bloch symbol.
At an eligible interface its two tetrahedra now
have all face attachments and a marked peripheral
transport. A regular geometric representation of
the literal word can therefore be developed on
this actual cell complex.

It does not yet resolve the strict-corner example
with adjacent powers \((2,-2)\). Two additional
points must be established for that application.
First, the proposed source rearrangement must be
realized with eligible actual interfaces; a
completion matrix at a masked leaf cannot supply
one. An equality of finite boundary tensors alone
does not prove this topological rearrangement.
Second, the assembled equations must be solved
on the geometric branch. The old strict KKT
subgradient is not a solution of the new shape
equations and cannot be substituted for one.

Even when those geometric conditions hold, a
nonzero dominant contribution in the original
coherent finite sum requires its own analytic
argument. This note neither drops the exact
crossing phases and first normals nor derives
their asymptotics from the existence of a
topological collar.

The exact matrix part can be replayed with

~~~sh
python3 experiments/verify_newton_crossing_marked_flags.py
~~~

The [saved result](../repro/results/research-newton-crossing-marked-flags.json)
includes the original meridians, all four conjugated
output matrices, the unfolded second-copy flag,
the fourth-flag identity (12), all four complete
white transitions (15), and the common-face
orientation. The topological zero-mask condition
is part of the written proof, not a condition
established by a symbolic matrix check.
