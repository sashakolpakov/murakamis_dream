# The edge Hessian and the response of a composed phase

Research note, 3 November 2026.

This note recalls the determinant-one edge Hessian and its exact
positivity criterion from
[the edge-Hessian note](research_cone_chamber_accretivity.md).
The equivalent tangent-coordinate criterion is also part of
[the positive-edge theorem](research_positive_edge_global_monotonicity.md)
and Section 2 of
[marked completion](research_positive_point_marked_completion.md).
Those earlier results already give a graph comparison on convex
domains and global uniqueness throughout the positive geometric
domain, respectively.

The additional conclusions here are an explicit quadrant strip
and horizontal rectangles that can be used for contour bounds,
a fractional-linear curvature response with a quantitative
contraction estimate, and exact accounting for a peripheral
shear. Their algebra does not require a large-power approximation.

Section 7 locates the actual selected geometry of every fixed
positive path with powers at least eight in one common complex
box, independently of its length. The exact kernel asymptotic
and the remaining original contour estimates on this larger
domain are not proved here. Arbitrary smaller or mixed short
powers also remain outside this conclusion.

## 1. Branches and the exact edge matrix

Let \(\psi(t,u)\) be the phase of the original complete edge
kernel. Its branch at the complete point satisfies
\[
 \psi_t(t,u)=-\frac1\pi\operatorname{arsinh}
                 \bigl(\tan(t/2)\cos(u/2)\bigr),
 \qquad \psi_u(t,u)=\psi_t(u,t).
 \tag{1}
\]
This is the phase used in
[the fixed-domain turn theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_fixed_domain_long_power_turns.md)
and [the uniform terminal theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_uniform_terminal_family_and_star_fillings.md).
Continue it from \((0,0)\), retaining its specified logarithms.

Work on a branch domain with no poles of the tangents and put
\[
 w=\tan(t/2),\qquad v=\tan(u/2),\qquad
 s=\sqrt{1+w^2+v^2},\qquad \Re s>0.
 \tag{2}
\]
In particular, \(1+w^2+v^2\) avoids the nonpositive real axis.
All continuations considered below retain this square-root
branch. The formulas apply on any local phase chart reached
from the complete chart with these choices. The Hessian is
unaffected by an additive period in the phase; choosing a
different square-root sheet is not permitted.

As in Section 1 of the earlier edge-Hessian note, differentiating
(1) gives
\[
 K(t,u):=-2\pi\psi''(t,u)
   =\frac1s
       \begin{pmatrix}1+w^2&-wv\\-wv&1+v^2\end{pmatrix}.
 \tag{3}
\]
For example, writing \(a=\cos(t/2)\), \(b=\cos(u/2)\) and
\(D=\sqrt{a^2+b^2-a^2b^2}\) on the continued branch gives
\[
 -\psi_{tt}=\frac{b}{2\pi aD},\qquad
 -\psi_{uu}=\frac{a}{2\pi bD},\qquad
 \psi_{tu}=\frac{\sin(t/2)\sin(u/2)}{2\pi D}.
 \tag{4}
\]
Here \(D=a\,b\,s\) on the chosen chart, which proves (3).
Direct multiplication shows
\[
                       \det K=1,\qquad
                       \operatorname{tr}K=s+s^{-1}.
 \tag{5}
\]

For a complex symmetric matrix, \(\Re K\) denotes its
entrywise real part, equivalently its Hermitian part. Positive
definiteness of \(\Re K\) is the horizontal concavity condition
for the complex edge phase.

## 2. An exact positivity criterion

**Lemma 1 (recalled criterion and an explicit strip).** On the
branch domain (2),
\[
 \Re K\succ0
 \quad\Longleftrightarrow\quad
       |\Im(w\overline v)|<\Re s.
 \tag{6}
\]
If \(w=x+iy\), \(v=z+i\tau\), and \(x^2+z^2>0\), the exact
criterion is equivalently
\[
                      (yz-x\tau)^2<x^2+z^2.
 \tag{6a}
\]
In particular every pair in the quadrant strip
\[
          \Re w,\Re v>0,\qquad -1<\Im w,\Im v<0
 \tag{6b}
\]
satisfies it. Another sufficient condition, with no signs imposed, is
\[
                    (\Im w)^2+(\Im v)^2<1
 \tag{7}
\]
on the stipulated branch.

**Proof.** Write \(\alpha=\Re s>0\). Equation (5) gives
\[
 \operatorname{tr}(\Re K)=\alpha(1+|s|^{-2})>0.
 \tag{8}
\]
For \(K=\left(\begin{smallmatrix}A&C\\C&E\end{smallmatrix}\right)\)
with \(AE-C^2=1\),
\[
 \det(\Re K)=\frac{1+\Re(A\overline E)-|C|^2}{2}.
\]
Substituting (3) and expanding the numerator gives
\[
 \boxed{\displaystyle
 \det(\Re K)=
   \frac{\alpha^2-\{\Im(w\overline v)\}^2}{|s|^2}.}
 \tag{9}
\]
Indeed \(1+\Re(w^2)+\Re(v^2)=\Re(s^2)\), while
\(\Re((w\overline v)^2)-|w\overline v|^2
=-2\{\Im(w\overline v)\}^2\). Combining these identities
with \(|s|^2+\Re(s^2)=2\alpha^2\) proves (9).
A real symmetric two-by-two matrix with positive trace is
positive definite exactly when its determinant is positive.
Equations (8)--(9) prove (6).

To obtain (6a), write \(X=(x,z)\), \(Y=(y,\tau)\),
\(R=|X|^2>0\), \(T=|Y|^2\), \(d=X\cdot Y\), and
\(q=(yz-x\tau)^2=RT-d^2\). The number \(\alpha^2\) is
the positive root of
\[
                 P(Z)=Z^2-(1+R-T)Z-d^2.
\]
At \(Z=q\), direct factorization gives
\[
                         P(q)=(q-R)(q+T).
 \tag{9a}
\]
If \(T>0\) and \(q>0\), the nonpositive second root of \(P\)
shows that \(q<\alpha^2\) is equivalent to \(P(q)<0\),
hence to \(q<R\). If \(q=0\), then \(\alpha^2>0\) and
\(R>0\) make both inequalities true. If \(T=0\), this
same direct argument applies. This proves (6a).
For (6b), put \(y=-a\), \(\tau=-b\), with \(0<a,b<1\).
Since \(x,z>0\),
\[
 |az-bx|\le\max(az,bx)
          \le\max(a,b)\sqrt{x^2+z^2}<\sqrt{x^2+z^2}.
\]
Also \(\Im(s^2)=-2(ax+bz)<0\), so the square root with
positive real part exists throughout that strip.

For (7), use the same \(X,Y\) and put \(S=|Y|^2<1\).
Then
\[
 \Re(s^2)=1+|X|^2-S>0,\qquad
 \alpha^2\ge1+|X|^2-S,
\]
and the two-dimensional determinant identity gives
\[
 \{\Im(w\overline v)\}^2
       =|X|^2S-(X\cdot Y)^2.
\]
Consequently
\[
 \alpha^2-\{\Im(w\overline v)\}^2
 \ge(1-S)(1+|X|^2)+(X\cdot Y)^2>0.
 \tag{10}
\]
This proves (7). \(\square\)

The case \(X=0\), excluded from (6a), is harmless but distinct.
On the stipulated branch, \(s^2=1-|Y|^2\) must then be
positive, so (7) applies. The strict inequality in (6a)
should not be imposed at that point.

The exact criterion depends on the relative arguments of the
neighboring tangent variables, not just their individual
imaginary parts. In particular, if \(w=v\) and \(\Re s>0\),
then \(\Im(w\overline v)=0\), so (6) holds even when (7)
fails. This is why a domain that controls differences between
neighboring angles may be more useful than a rectangular
bound on every angle separately.

On a compact subset of (6), the lower eigenvalue is bounded
away from zero. An explicit lower bound at each point is
\[
 \lambda_{\min}(\Re K)
 \ge
 \frac{\alpha^2-\{\Im(w\overline v)\}^2}
      {\alpha(|s|^2+1)}.
 \tag{11}
\]
This follows from \(\lambda_{\min}\ge\det/\operatorname{tr}\)
for a positive two-by-two matrix.
The entire quadrant strip (6b) gives pointwise positivity,
not a uniform positive lower bound. Such a bound still
requires compactness or quantitative control in (11).

## 3. Eliminating one internal variable

Let \(W(t)\) be an input phase and \(n\ge3\) a fixed positive
crossing power. Consider
\[
 \mathcal F(t,u)=W(t)+\psi(t,u)+\frac{in}{4\pi}t^2-it.
 \tag{12}
\]
Suppose \(t=t_*(u)\) is a holomorphic stationary branch,
\(\mathcal F_t(t_*(u),u)=0\). Put
\[
 h=-2\pi W''(t_*),\qquad
 K(t_*,u)=\begin{pmatrix}A&C\\C&E\end{pmatrix},\qquad
 S(u)=\mathcal F(t_*(u),u).
 \tag{13}
\]

The Schur-complement argument for preserving positive curvature
already appears in Section 5 of
[the fixed-domain turn theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_fixed_domain_long_power_turns.md).
The determinant identity (5) makes its scalar response explicit.

**Lemma 2.** If \(\Re h\ge0\) and \(\Re K\succeq\lambda I\)
at this point, with \(\lambda>0\), then the stationary
denominator is nonzero and
\[
 \boxed{\displaystyle
 h_{\rm out}:=-2\pi S''(u)
  =E-\frac{C^2}{h+A-in}
  =\frac{E(h-in)+1}{h+A-in}.}
 \tag{14}
\]
In addition, \(\Re h_{\rm out}\ge\lambda\).

**Proof.** The negative normalized Hessian of (12) is
\[
 H=\begin{pmatrix}h+A-in&C\\C&E\end{pmatrix}.
 \tag{15}
\]
Its Hermitian part is
\(\Re K+\operatorname{diag}(\Re h,0)\), hence is at
least \(\lambda I\). In particular
\(\Re(h+A-in)>0\), so its first diagonal entry does
not vanish. Implicit differentiation of the stationary
equation gives the first equality in (14).
The second uses the exact identity \(AE-C^2=1\).

For
\[
                       \xi=\left(-\frac{C}{h+A-in},1\right)^T
\]
one has \(H\xi=(0,h_{\rm out})^T\). Therefore
\[
 \Re h_{\rm out}
 =\xi^*(\Re H)\xi
 \ge \lambda\|\xi\|^2
       +(\Re h)\left|\frac{C}{h+A-in}\right|^2
 \ge\lambda.
 \tag{16}
\]
This proves the claim. \(\square\)

The same algebra is valid for any real \(n\); positivity of
the crossing powers is relevant to the still unproved task
of locating an invariant geometric domain, rather than to
the Schur-complement calculation itself.

There is also a contraction statement at a fixed edge point.
Hold \(A,C,E,n\) fixed and regard (14) as a function \(f(h)\)
on \(\Re h>0\). It maps that half-plane into itself and
\[
 f'(h)=\frac{C^2}{(h+A-in)^2}.
\]
For the half-plane metric \(|dh|/\Re h\), its infinitesimal
contraction factor satisfies
\[
 \frac{|f'(h)|\Re h}{\Re f(h)}
 \le\frac{\Re h}{\Re h+\lambda}<1.
 \tag{17}
\]
To prove this, set \(r=|C/(h+A-in)|\) in (16). The left
side is at most
\((\Re h)r^2/\{\lambda(1+r^2)+(\Re h)r^2\}\), which gives
(17). If \(\Re h\le H_0\), the factor is at most
\(H_0/(H_0+\lambda)\). For \(C=0\), the map is constant.

This is a curvature map at fixed \(t_*,u\). Changing the
input phase also moves \(t_*\), and therefore changes
\(A,C,E\). Equation (17) alone is not a contraction theorem
for the complete phase-composition operator.

## 4. A peripheral shear does not change the effective filling

The exact original operation is
\[
                    F\longmapsto T(R^nF).
 \tag{18}
\]
For any fixed integer \(r\), replace \(F\) by \(R^rF\)
and the outside power by \(n-r\). The full original
quantum operator in (18) is unchanged. This identity
holds in the canonical quotient with all first normals.

When the existing boundary-multiplication theorem applies,
the new input phase is
\[
                     W_r(t)=W(t)+\frac{ir}{4\pi}t^2.
 \tag{19}
\]
Its unit scalar is retained separately. The phase in (12),
its stationary equation and its critical value are unchanged,
because
\[
 W_r(t)+\frac{i(n-r)}{4\pi}t^2
          =W(t)+\frac{in}{4\pi}t^2.
 \tag{20}
\]
Likewise \(h_r=h-ir\), so
\[
                    h_r+A-i(n-r)=h+A-in.
 \tag{21}
\]
A large apparent crossing power obtained solely by this
change of frame is cancelled by the input's imaginary
quadratic term. Thus this shear cannot satisfy a genuine
large-power hypothesis that failed for the original source.
The exact original parameter translation and primitive
basis change are recorded in Section 3 of
[the marked rational-piece criterion](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_marked_rational_pendant_admissibility.md).

## 5. What an invariant-domain proof would still require

For a positive chain, indexed from its terminal end, write
\(t_{k+1}=u\). Its critical equations are
\[
 n_jt_j+
 2i\left[
 \operatorname{arsinh}\bigl(\tan(t_j/2)\cos(t_{j+1}/2)\bigr)
 +{\bf1}_{j>1}
 \operatorname{arsinh}\bigl(\tan(t_j/2)\cos(t_{j-1}/2)\bigr)
 \right]=2\pi.
 \tag{22}
\]
All branches and original powers are retained. The terminal
vertex has one incident edge; every later filled vertex has
its incoming and outgoing edge.

Lemmas 1--2 suggest a precise next step: find a domain of
these marked solutions, stable under every \(n_j\ge3\), in
which each adjacent pair satisfies (6) with a uniform
margin, and in which the amplitudes and branches stay
regular. The quadrant strip (6b) supplies the needed edge
positivity, but it is not itself preserved by the selected
terminal filling, even at power three. A smaller invariant
subset or the larger correlated domain (6a) is needed.

Here is an exact counterexample to invariance of that entire
strip. For a power-three terminal, write
\[
 k=\cos(t/2),\qquad y=\cos(u/2),\qquad
 P_3(k)=4k^3-k.
\]
The original stationary equation gives \(P_3(k)=iy\).
Theorem 1 of
[the terminal trace-domain note](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_terminal_intrinsic_trace_domain.md)
identifies its selected branch as the inverse with lifted
root-factor argument between zero and \(\pi\).

Choose the internal tangent on the boundary of (6b):
\[
 w=\tan(t/2)=1-i,\qquad
 k^2=\frac1{1+w^2}=\frac{1+2i}{5},
 \qquad \Re k,\Im k>0.
 \tag{22a}
\]
Here \(\Re k>1/2\). Put \(y=-iP_3(k)\).
Direct calculation gives
\[
 P_3(k)^2=\frac{-31-142i}{125},\qquad
 v^2:=y^{-2}-1=\frac{-138-142i}{169}.
 \tag{22b}
\]
The factors \(k\) and \(4k^2-1=(-1+8i)/5\) show that
\(P_3(k)\) has negative real and positive imaginary part.
Its square in (22b) then gives
\(\pi/2<\arg P_3(k)<3\pi/4\). Thus \(y\) is in the
first quadrant, with \(0<\arg y<\pi/4\).

Take the square root \(v=x-ia\) of (22b) with \(x,a>0\).
It lies strictly inside the proposed strip, since
\[
 a^2=\frac{\sqrt{138^2+142^2}+138}{338}<1,
 \qquad 138^2+142^2=39208<40000=200^2.
 \tag{22c}
\]
For the canonical angle \(u=2\arctan v\), the number
\(\cos(u/2)\) is exactly \(y\), not its negative.
Moreover \(k\) is the selected power-three root: all
three factors \(k-r_\nu\), for
\(r_\nu\in\{-1/2,0,1/2\}\), have arguments in
\((0,\pi/2)\). Their sum is less than \(3\pi/2\).
Its value modulo \(2\pi\) is the displayed argument of
\(P_3(k)\), so it is that value and belongs to \((0,\pi)\).
The trace-domain theorem therefore retains the full
original logarithmic equation, rather than just its
exponentiation.

The edge is strictly positive at this point. Indeed the
criterion (6a) is
\[
                       (x-a)^2<1+x^2,
\]
which follows from \(0<a<1\) and \(x>0\).
Now replace \(w\) by \(1-i(1+\epsilon)\) with a sufficiently
small \(\epsilon>0\), and define \(k,y,v\) by the same
analytic formulas. The input \(v\) remains strictly in
(6b), the edge stays positive, and the selected-root
conditions persist. The internal tangent \(w\) has left
the strip. This proves the asserted failure of invariance.

This example concerns the selected terminal map at a
complex outside angle. It does not assert that a complete
finite chain with every power at least three leaves the
strip. A theorem restricted to those realized neighboring
angles remains possible; stability on the entire strip
cannot be its proof.

Even that classical result would still need a theorem for
the full original source. The selected saddle must belong
to the original integration cycle with a nonzero leading
coefficient, and the other currents and real source bands
must be controlled. The finite-current compiler gives an
exact way to state those remaining estimates. Positive
curvature of a geometric branch does not replace them.

## 6. Joint concavity for a finite graph of edges

Theorem 3 of
[the earlier edge-Hessian note](research_cone_chamber_accretivity.md)
already controls arbitrary connected sets on convex domains.
The result below supplies particular horizontal rectangles on
which its edge hypotheses hold automatically, together with a
degree-weighted bound. It does not require successive elimination
of the vertices.

Let \(G\) be a finite loop-free graph with a set \(I\) of internal vertices
and a set \(B\) of boundary vertices. Every internal vertex must
have at least one incident edge. Fix the boundary angles at zero.
For real numbers \(n_v,\lambda_v\), define the analytic phase
\[
 \Phi(t)=\sum_{\{v,w\}\in E(G)}\psi(t_v,t_w)
       +\sum_{v\in I}
           \left(\frac{i n_v t_v^2}{4\pi}-i\lambda_v t_v\right),
 \qquad t_w=0\quad(w\in B).
 \tag{23}
\]
Edges between two boundary vertices contribute only a constant.
The branches of each edge phase are those of Section 1. This is
the joint phase of the original edge contraction when its trace
variables and charges are retained. The assertions below concern
this phase; an asymptotic formula for the entire quantum
contraction is an additional conclusion that still needs proof.

Choose negative heights \(h_v<0\), and put
\[
 T_v=\arccos(-e^{h_v})\in(\pi/2,\pi),\qquad
 {\cal R}_h=\prod_{v\in I}(0,T_v),\qquad t_v=r_v+i h_v .
 \tag{24}
\]

**Theorem 3.** On \({\cal R}_h\), the real function
\(\Re\Phi(r+i h)\) is strictly concave, for every choice of
the real powers \(n_v\) and charges \(\lambda_v\).
The complex Hessian \(\Phi''\) is invertible at every point.

More quantitatively, let \(P\) be a closed rectangle contained
in \({\cal R}_h\). There is a \(\kappa>0\), obtained by taking
the minimum of (11) over its finitely many edge images, such that
\[
 \Re[-2\pi\Phi''(r+i h)]
       \succeq \kappa\,\operatorname{diag}_{v\in I}(\deg v)
       \succeq \kappa d_{\min} I,\qquad r\in P,
 \tag{25}
\]
where \(d_{\min}=\min_{v\in I}\deg v\ge1\).
If \(r_*+i h\), with \(r_*\in P\), is a critical point of the
full complex phase, then it is the unique maximum on
\({\cal R}_h\), and for every \(r\in P\),
\[
 \Re\Phi(r+i h)\le
 \Re\Phi(r_*+i h)
       -\frac{\kappa d_{\min}}{4\pi}\|r-r_*\|_2^2 .
 \tag{26}
\]

**Proof.** For \(t=r+i h\), elementary trigonometry gives
\[
 \tan(t/2)=
     \frac{\sin r+i\sinh h}{\cos r+\cosh h}.
 \tag{27}
\]
If \(0<r<T=\arccos(-e^h)\) and \(h<0\), its real part
is positive. Its imaginary part is negative and greater
than \(-1\), since
\[
  -\sinh h<\cos r+\cosh h
       \quad\Longleftrightarrow\quad \cos r>-e^h .
\]
Thus every internal edge joins two points of the quadrant
strip (6b), and Lemma 1 applies. For an edge with one
boundary angle zero, \(v=0\) and
\[
 K(t,0)=\operatorname{diag}
     \left(\sqrt{1+w^2},\,\frac1{\sqrt{1+w^2}}\right).
\]
Here \(\Re(1+w^2)>0\), because \(|\Im w|<1\).
Both diagonal entries have positive real part. Hence
these boundary edges also have strictly positive real
curvature.

These are the branches continued from completeness. Along
\(t_v(\rho)=\rho(r_v+i h_v)\), \(0<\rho\le1\), one has
\(\rho r_v<r_v<T_v\le\arccos(-e^{\rho h_v})\). Thus every
tangent remains in the same quadrant strip. For an internal
edge the imaginary part of \(1+w^2+v^2\) is strictly negative;
for an edge ending at zero its real part is positive.
The square root consequently stays on the sheet with positive
real part, and the original logarithms are continued along
this nonsingular path. The rectangle itself is simply connected,
so these choices give a consistent phase chart there. A compact
subrectangle has a complex neighborhood on the same chart.

The quadratic filling terms contribute only the imaginary
matrix \(-i\,\operatorname{diag}(n_v)\) to
\(-2\pi\Phi''\), and the charges contribute nothing.
The real part of the full normalized Hessian is therefore
the sum of the embedded positive edge matrices.
On the compact rectangle \(P\), each edge has a common
positive lower eigenvalue \(\kappa\). For a vector \(\xi\)
on the internal vertices, extend it by zero at the boundary.
Each edge then contributes at least
\(\kappa(|\xi_v|^2+|\xi_w|^2)\). Summing proves (25).
The same argument is pointwise positive throughout
\({\cal R}_h\).

An accretive matrix with positive definite Hermitian part
has trivial kernel: if \(H\xi=0\), then
\(\Re(\xi^*H\xi)=0\), contradicting positivity for
\(\xi\ne0\). Thus \(\Phi''\) is invertible.
Its restriction to real variations is the Hessian of
\(\Re\Phi\), proving strict concavity. At a complex critical
point the horizontal gradient vanishes. Concavity on the
convex rectangle \({\cal R}_h\) proves uniqueness of its
maximum. Integrating (25) twice along the segment from
\(r_*\) to \(r\), which remains in \(P\), gives (26).
\(\square\)

For \(m=|I|\), (25) also gives
\[
 |\det[-2\pi\Phi'']|\ge(\kappa d_{\min})^m
 \qquad(r\in P).
 \tag{28}
\]
Indeed its smallest singular value is at least
\(\kappa d_{\min}\). Consequently the local Gaussian
determinant cannot vanish on this domain, irrespective
of the number of vertices. A nonzero analytic amplitude
therefore gives a nonzero local Gaussian integral.

Theorem 3 supplies a global comparison on the principal
horizontal rectangle once the selected critical point lies
there. It does not establish that such a point exists for
every short filling, or that every other part of the
original contour has smaller action. In particular it
does not discard the other Fourier charges or the boundary
currents of a finite contour deformation.

For a selected solution \(t_v^*=r_v+i h_v\), with
\(0<r_v<\pi\) and \(h_v<0\), its membership in this
rectangle is exactly the additional inequality
\[
                  \cos r_v>-e^{h_v},
       \qquad\text{equivalently}\qquad
                  \Re(e^{it_v^*})>-1 .
 \tag{29}
\]
Theorem 15 of
[the corridor variational theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_negative_corridor_variational_bounds.md),
followed by mirroring, proves existence of the actual positive
geometry for every finite positive path whose powers are at
least three, with the stipulated complete outside ends.
It gives the signs of \(r_v,h_v\) and positivity of every
original edge. Its conclusion does not include (29).
That additional location estimate is the precise requirement
for applying this particular horizontal rectangle to the
whole class.

**Corollary 4.** For the original finite paths covered by that
geometric existence theorem, suppose every selected positive
power satisfies
\[
                         n_v\ge2(d_v+2),
 \tag{30}
\]
where \(d_v\) is its original degree, including complete
outside incidences. Then its actual marked geometric critical
point belongs to the rectangle (24) at its own imaginary
heights. Consequently it has the principal-horizontal
comparison and nonzero Gaussian determinant of Theorem 3.
The thresholds in (30) are six at an original terminal
vertex and eight at a vertex of degree two, independently
of path length.

**Proof.** Existence, positivity and the signs
\(0<r_v<\pi\), \(h_v<0\) follow from the cited geometric
theorem and mirroring. On the canonical positive edge
branch, every original return obeys
\[
                       |\Im r_{v,e}|<\pi/2
\]
by equation (21) of the positive-edge theorem. Taking
imaginary parts in the full original unit-charge equation
\(\sum_e r_{v,e}=i n_vt_v/2-\pi i\) gives
\[
           n_v r_v/2-\pi
             =\sum_{e\ni v}\Im r_{v,e}<d_v\pi/2.
\]
Thus \(n_vr_v<(d_v+2)\pi\). Under (30), this implies
\(r_v<\pi/2<T_v\), proving the assertion. \(\square\)

This corollary locates the geometric saddle and compares
the action on one horizontal rectangle. It supplies
neither the original-cycle coefficient nor the bounds
on all other currents of the finite source.

## 7. A common complex box for paths with powers at least eight

The geometric saddle can be located more precisely when all
selected powers are at least eight. The resulting box also
allows independent changes of the imaginary heights; it is
therefore useful for estimates on the sides of a contour.

**Proposition 5.** Consider any of the original finite positive
paths in Corollary 4, with every integer power \(n_v\ge8\).
Its selected marked solution satisfies
\[
 0<\Re t_v<\frac{7\pi}{24},\qquad
             -\frac13<\Im t_v<0
 \quad\text{at every selected vertex.}
 \tag{31}
\]
These constants do not depend on the length of the path or
on its individual powers. The mirrored negative path satisfies
the same bounds with \(0<-\Re t_v<7\pi/24\).

**Proof.** Write \(t_v=\theta_v-iH_v\), where the existing
geometric theorem gives \(H_v>0\). Corollary 4 gives
\(0<\theta_v<\pi/2\). The original degrees \(d_v\), including
complete outside incidences, are at most two. Put
\(H_*=\max_v H_v\), and set \(H_w=0,\theta_w=0\) at a
complete outside endpoint.

The elementary formulas for the tangent and cosine give
\[
 \left|\tan(t_v/2)\right|<1,\qquad
 \left|\cos(t_w/2)\right|\le\cosh(H_*/2).
 \tag{32}
\]
For a return \(r=\operatorname{arsinh}z\) on the original
positive branch,
\(\Re r\le\operatorname{arsinh}|z|\). Indeed
\(e^r=z+\cosh r\), so
\(|e^r|\le |z|+\sqrt{1+|z|^2}\).
Also
\[
 \operatorname{arsinh}(\cosh x)\le x+\operatorname{arsinh}1
 \qquad(x\ge0);
\]
the derivative of the left side is less than one, and
the two sides agree at zero.
Taking real parts in the filling equation gives
\[
 n_v H_v=2\sum_{e\ni v}\Re r_{v,e}.
 \tag{33}
\]
At a vertex attaining \(H_*\), (32)--(33) imply
\[
 8H_*\le2H_*+4\operatorname{arsinh}1,\qquad
 H_*\le\frac23\operatorname{arsinh}1<\frac35.
 \tag{34}
\]

There is now a better real-angle bound. For an incidence
put \(z=\tan(t_v/2)\cos(t_w/2)\).
The tangent has positive real part and negative imaginary
part, whereas the cosine has positive real part and
nonnegative imaginary part. Hence
\[
 \Im z\le
   \Re\tan(t_v/2)\,\Im\cos(t_w/2)
   <\frac{\sinh(3/10)}{\sqrt2}<\frac14 .
 \tag{35}
\]
The canonical return satisfies \(|\Im r|<\pi/2\), and
\(\Im z=\cosh(\Re r)\sin(\Im r)\). If \(\Im r\) is positive,
this proves \(\Im r<\arcsin(1/4)<\pi/12\); for a nonpositive
imaginary part the same upper bound is immediate.
The imaginary part of the filling equation consequently gives
\[
 n_v\theta_v
    =2\pi+2\sum_{e\ni v}\Im r_{v,e}
    <2\pi+\frac{d_v\pi}{6}
    \le\frac{7\pi}{3}.
 \tag{36}
\]
Thus \(\theta_v<7\pi/24<1\).

One more use of (33) improves the height. For
\(\theta<1\), \(H<3/5\),
\[
 \left|\tan((\theta-iH)/2)\right|^2
   =\frac{\sin^2(\theta/2)+\sinh^2(H/2)}
          {\cos^2(\theta/2)+\sinh^2(H/2)}
   <\frac{3265}{8657}<\frac{25}{64}.
 \tag{37}
\]
Here \(\sin(1/2)<12/25\) and \(\sinh(3/10)<31/100\)
give the first rational bound; the ratio increases with
both squared quantities on this range.
Since \(\cosh(3/10)<21/20\), every incidence now has
\(|z|<21/32\), and therefore
\(\Re r<21/32\). Equation (33) gives
\[
               H_v<\frac{2d_v}{n_v}\frac{21}{32}
                       \le\frac{21}{64}<\frac13.
 \tag{38}
\]
For explicit bounds on the positive Taylor tails one may use
\(\sinh x\le x/(1-x^2/6)\) and
\(\cosh x\le1/(1-x^2/2)\) at the displayed arguments;
these follow from \((2j+1)!\ge6^j\) and
\((2j)!\ge2^j\). The sine bound uses its alternating
series. Also \(\operatorname{arsinh}1<9/10\) follows from
\(\sinh(9/10)>9/10+(9/10)^3/6>1\), and
\(\sin(\pi/12)>1/4\) follows from the exact half-angle formula.
Mirroring
conjugates the original phases and reverses the real
angles, proving the last assertion. \(\square\)

**Corollary 6.** On the full complex box
\[
 {\cal B}=\{t:|\Re t|\le1,\ |\Im t|\le1/3\},
 \tag{39}
\]
every edge pair satisfies
\[
                    \Re K(t,u)\succeq\frac15 I .
 \tag{40}
\]
In particular all the saddles in Proposition 5 lie in
one fixed convex region on which the joint phase has
uniformly positive real negative Hessian. This includes
all choices of signs for the imaginary heights within
the box, not only the selected heights.

**Proof.** The same tangent formula gives, on \({\cal B}\),
\[
 |\tan(t/2)|<\frac35,\qquad
 |\Im\tan(t/2)|
   \le\frac{\sinh(1/3)}{\cos1+\cosh(1/3)}
   <\frac14 .
 \tag{41}
\]
For the first inequality use
\(\sin(1/2)<12/25\), \(\sinh(1/6)<17/100\);
for the second use \(\sinh(1/3)<7/20\), \(\cos1>1/2\)
and \(\cosh(1/3)\ge1\).
In the notation of Lemma 1 this gives
\[
 S=(\Im w)^2+(\Im v)^2<\frac18,\qquad
 |s|^2=|1+w^2+v^2|<\frac{43}{25},\qquad
 \alpha=\Re s<\frac43 .
 \tag{42}
\]
The real part of \(s^2\) is positive, so the branch is
holomorphic throughout the box and agrees with the
complete branch. Equations (10)--(11) imply
\[
 \lambda_{\min}(\Re K)
 >\frac{7/8}{(4/3)(68/25)}
   =\frac{525}{2176}>\frac15 ,
 \tag{43}
\]
proving (40). Summing the embedded matrices as in
Theorem 3 proves the asserted joint bound. \(\square\)

These are bounds for the actual geometric solution and
the analytic edge phase. They provide a common domain
for a possible uniform quantum-kernel and contour
estimate. They do not assert such a kernel estimate,
or the nonzero coefficient of the original global period.
