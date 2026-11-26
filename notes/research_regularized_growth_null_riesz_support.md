# Null Riesz support on the regular characteristic region

Research deduction, 6 November 2026.

The [vertical regularity theorem](research_regularized_growth_vertical_regularity.md)
also has a consequence for any finite number of modulus classes.
First an ordered-rectangle argument supplies area-zero support of
the Riesz measure. Adding the zero-growth branch and covering the
modulus equality sets then gives the same conclusion throughout
the regular-root disk for \(V=\max(U,0)\). It does not bound all
integer lifts or prove a locally finite two-dimensional action
decomposition.

## 1. The regular positive rectangle

Use the actual logarithmic meridian envelope \(U\). By continuity
of its positive part, work on a rectangle \(R\) where \(U>0\).
Suppose the simple nonzero characteristic roots split into classes
\[
 L_{jr}=e^{2\pi i a_{jr}}L_j,\qquad
 a_{jr}\in\mathbb R,\qquad 1\le j\le k,
 \tag{1}
\]
with each class finite. Suppose their modulus functions satisfy
\[
 b_1(z)<\cdots<b_k(z),\qquad
 b_{j+1}(z)-b_j(z)\ge\gamma>0,\qquad
 b_j=\frac{\log|L_j|}{2\pi}.
 \tag{2}
\]
Shrink to a smaller rectangle when taking a uniform gap.
Put
\[
 p_j=\frac{\Log L_j}{2\pi i},\qquad
 H_j=\Re\int^z p_j(\zeta)\,d\zeta,\qquad
                    \Lambda_j=\bigcup_r(a_{jr}+\mathbb Z).
 \tag{3}
\]
Every vertical slice has at most \(k-1\) switches, and its class
index is nondecreasing. These are the precise conclusions of
the vertical theorem on a rectangle with no modulus crossings.

## 2. A pure vertical interval persists as an open piece

Suppose at \(x_0\) the interval \([a,d]\) of one vertical slice
has only class \(j\). Thus \(U-H_j\) is constant there.
Choose \(a<a'<d'<d\). Continuity of \(U-H_j\) at the four
buffer endpoints gives, for \(x\) sufficiently close to \(x_0\),
\[
 \begin{split}
 |(U-H_j)(x,a')-(U-H_j)(x,a)|&<\gamma(a'-a),\\
 |(U-H_j)(x,d)-(U-H_j)(x,d')|&<\gamma(d-d').
 \end{split}
 \tag{4}
\]
If a class larger than \(j\) occurred at an interior point of
\([a',d']\), monotone vertical class order would force classes
larger than \(j\) throughout \([d',d]\), up to irrelevant
switch points. Its upper-buffer increment would then be at
least \(\gamma(d-d')\), contrary to (4). A class smaller than
\(j\) similarly forces a lower-buffer increment at most
\(-\gamma(a'-a)\). A switch exactly at an inner endpoint is
handled by its adjacent interval and the same bounds.

Consequently the nearby inner slices have only class \(j\).
Every interior point of a vertically pure interval therefore
has an actual two-dimensional neighborhood on which
\[
                             U=H_j+c(x).
 \tag{5}
\]
Using two separate buffer increments is essential. A single
increment spanning both sides could have cancellation between
smaller and larger classes.

Let \(\Omega_j\) be the set of all points admitting such a
vertically pure interval of class \(j\). The argument proves
that \(\Omega_j\) is open. The complement
\[
                           E=R\setminus\bigcup_j\Omega_j
 \tag{6}
\]
has at most \(k-1\) points on each vertical slice. It is relatively
closed, hence measurable, and Fubini's theorem gives
\(\operatorname{area}(E)=0\).

## 3. Local seams inside a pure piece

On a rectangle contained in \(\Omega_j\), equation (5) and
subharmonicity give \(c''\ge0\). At a differentiability point of
this convex function, its upper-contact slope must satisfy
\[
                               c'(x)\in\Lambda_j .
 \tag{7}
\]
The other classes have different vertical derivatives by (2).
Interior chord bounds and local finiteness of \(\Lambda_j\)
give, on smaller rectangles,
\[
                     U(z)=H_j(z)+
                              \max_{1\le r\le m}(\lambda_r x+C_r),
                 \qquad \lambda_r\in\Lambda_j,\quad m<\infty .
 \tag{8}
\]
Thus the support of \(\Delta U\) inside that smaller rectangle
is contained in finitely many vertical seams and has area zero.

Take a countable cover of \(\bigcup_j\Omega_j\) by these smaller
rectangles. There is no missing closure step: every point of a
pure open piece has its own neighborhood in which the support
is exactly restricted by (8). Any accumulation outside the pure
pieces lies in the relatively closed null set \(E\).
It follows that
\[
                           \operatorname{area}
                                  (\operatorname{supp}\Delta U)=0
                                      \quad\hbox{in }R .
 \tag{9}
\]
This is a statement about the support of the measure, not merely
singularity of the measure.

## 4. The remaining integer-lift issue

Off \(\operatorname{supp}\Delta U\), the actual continuous
subharmonic representative is harmonic. Each component is
therefore a region of classical differentiability, so the
whole-period contact theorem applies at every point there.
Continuity of the harmonic derivative selects one characteristic
root and one integer logarithmic lift on each connected component.
Locally on that component,
\[
                    U=H_j+\lambda\,\Re z+C,\qquad
                   \lambda\in\Lambda_j,\quad C\in\mathbb R .
 \tag{10}
\]
In particular the characteristic relation holds at classical
differentiability points covering \(R\) up to an area-zero set.

The integers in (10) are locally bounded inside each pure piece,
but may not yet have a common bound on components accumulating
at \(E\). Nor have their additive constants been shown to come
from a finite set on a neighborhood of \(E\).

Equation (9) supplies the \(SH_0\) hypothesis in
[Björk, Borcea and Bøgvad, *Subharmonic Configurations and
Algebraic Cauchy Transforms of Probability Measures*, Theorem 1](https://arxiv.org/pdf/0912.4650).
That theorem also assumes a finite holomorphic derivative family.
The possible integer translates in (10) leave that hypothesis
unproved here. It cannot be replaced by countability.

For two strictly separated modulus classes, the
[two-modulus theorem](research_regularized_growth_two_moduli.md)
already controls both sides of every switch and proves a local
finite harmonic maximum. With three or more classes, a missing
middle class can appear in a thin nearby band; the open-piece
argument above does not produce a uniform strip for that class
at a point of \(E\).

## 5. Modulus crossings and zero growth do not destroy null support

Let \(D\) now be a disk in the entire regular-root region of the
actual stable characteristic. Its simple nonzero roots
\(L_1,\ldots,L_s\) are holomorphic there. Adjoin the analytic
function \(L_0=1\), and retain
\[
                             V=\max(U,0).
 \tag{11}
\]
At a positive upper-contact point, the actual characteristic
constrains its slope. At a zero point, every upper-contact
slope is zero. Thus every upper-contact slope of \(V\) is
among those allowed by the enlarged list \(L_0,L_1,\ldots,L_s\).
Allowing all integer logarithmic lifts of \(L_0\) merely enlarges
this list; no new exact operator or source equation is asserted.
The vertical theorem proves that \(V\) is finite, continuous
and subharmonic on \(D\).

Group the functions \(b_j=\log|L_j|/(2\pi)\) which coincide
identically. Their root ratios are constant unit phases.
Let \(Z\) be the union of equality sets of the remaining
distinct modulus functions. Each nonzero difference \(b_i-b_j\)
is harmonic and real analytic, so its zero set has area zero.
Locally at a zero this follows by taking a harmonic conjugate
and writing the resulting nonconstant holomorphic function in
the form \(w^m\) in a local analytic coordinate: its real part
vanishes on finitely many analytic arcs. Hence
\[
                             \operatorname{area}(Z)=0.
 \tag{12}
\]

Every point of \(D\setminus Z\) has a rectangle with strict
modulus ordering and a uniform gap. Apply Sections 2--3 to
\(V\) there, using the enlarged root list. Their proof uses
only continuity, subharmonicity and the allowed upper-contact
slopes; positivity was previously needed only to invoke the
original contact theorem and is no longer needed for this
enlarged family.
Choose a countable cover of \(D\setminus Z\) by such rectangles.
On each one the support of \(\Delta V\) is null, and all
remaining support points lie in \(Z\). Therefore
\[
                   \boxed{\quad
                    \operatorname{area}(\operatorname{supp}\Delta V)
                                      =0\quad\hbox{on }D.
                         \quad}
 \tag{13}
\]

The open components of \(D\setminus\operatorname{supp}\Delta V\)
are harmonic regions covering \(D\) up to an area-zero set.
On a connected component, the nonnegative harmonic function
\(V\) is either identically zero or strictly positive. In the
second case \(V=U\), so the **original**, unenlarged
characteristic applies at every point. Its continuous harmonic
derivative selects one actual root and one fixed logarithmic
integer on that component. After choosing primitives on \(D\),
\[
       V=0
       \quad\hbox{or}\quad
       V(z)=\Re\int^z\frac{\Log L_j(\zeta)}{2\pi i}\,d\zeta
                                +n\Re z+C,\qquad n\in\mathbb Z.
 \tag{14}
\]
This does not introduce a spurious positive component from the
artificial root. The constants and integers in different
components have not been shown to range over finite sets on
a neighborhood. Thus the finite derivative-family premise of
the cited piecewise-harmonic theorem remains missing even
though (13) supplies its null-support premise.

This local branch description is restricted to the regular-root region.
It does not resolve a degenerate meridian fiber, a zero characteristic
root, or an unproved geometric component or coefficient.
No numerical source calculation is used.

## 6. Repeated characteristic factors and the exceptional meridians

The same null-support conclusion does not require generic simplicity
of the original polynomial itself. The whole-period theorem gives a
nonzero Laurent polynomial \(B_{\rm cl}(Y,L)\). View it over
\(\mathbb C(Y)\), remove its power of \(L\), and take the squarefree
part of the remaining nonconstant polynomial in \(L\). These
operations describe its nonzero root set; they do not define a new
exact quantum operator.

There is a finite exceptional set \(\mathcal E\subset\mathbb C^*\)
outside which this reduced polynomial has the same nonzero roots as
the original characteristic, constant degree, and nonzero discriminant
and constant coefficient. Include in \(\mathcal E\) all zeros and
poles introduced by this rational factorization, the zeros of the
original common meridian coefficient factor, and all required leading
and trailing coefficient zeros. Squarefreeness in characteristic zero
ensures that the discriminant is a nonzero rational function, so only
finitely many further meridians are excluded. On a small disk avoiding
\(\mathcal E\), all roots admit simple nonzero holomorphic branches.
More explicitly, if \(f\) is the monic polynomial before squarefree
reduction and \(q\) its squarefree part, then \(q\mid f\) and
\(f\mid q^M\) in \(\mathbb C(Y)[L]\) for some fixed integer \(M\).
Include the poles of these quotient polynomials in \(\mathcal E\).
The two specialized divisibilities then prove equality of root sets
there, without assuming that squarefree reduction always commutes
with specialization.

Every upper-contact slope of the actual positive growth still belongs
to this root set there. The regularity proofs use that contact
constraint and subharmonicity, not an exact equation for the reduced
polynomial. Hence Sections 1--5 apply on every such disk, including
when the unreduced characteristic has repeated factors everywhere.

The positive envelope \(V\) is locally bounded and subharmonic on
the entire logarithmic meridian plane by the tail-envelope argument
in the vertical regularity note. The inverse image of
\(\mathcal E\) under \(z\mapsto e^z\) is discrete. Cover its
complement by countably many regular disks and use (13) on each.
The remaining possible support points lie in this discrete set.
Consequently, for every fixed knot covered by the whole-period
operator construction,
\[
             \operatorname{area}(\operatorname{supp}\Delta V)=0
                    \quad\hbox{on the logarithmic meridian plane}.
\tag{15}
\]
Continuity has been proved off the exceptional set; it is not
inferred at an exceptional meridian from this support argument.

If removal of the \(L\)-power leaves a constant polynomial over
\(\mathbb C(Y)\), there are no nonzero characteristic roots away
from finitely many meridians. The whole-period theorem's approximating
positive contacts then rule out every positive envelope value there.
Thus \(V=0\) off the exceptional set. Its submean inequality forces
\(V=0\) at those isolated points too, and (15) holds in this case
as well.

No common meridian factor has been discarded at an exceptional
fiber. In particular this reduction gives neither a regular
recurrence at \(Y=1\) nor a pointwise estimate of \(R_N(1)\).
It also leaves the integer lifts, additive constants and possible
accumulation of harmonic components unresolved.
