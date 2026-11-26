# A convexity criterion for the original edge phase

Research note, 2 November 2026. This note gives an exact test for
the real part of the Hessian of the circle-tree edge phase. A
simple sufficient condition can be checked without solving any
filling equations. The test is unchanged by arbitrary signed
filling powers.

The conclusion is a uniqueness and comparison theorem inside a
specified convex complex region. It does not assert that every
critical point of the original source lies in that region. In
particular, it does not supply the global hypothesis in
[the dominant-saddle transport theorem](research_dominant_saddle_transport.md).

## 1. The original phase and its branches

Use the edge phase of
[the circle-tree geometry paper](../papers/circle-tree-geometry/main.tex),
with its normalization

\[
 \psi(0,0)=\frac{v_{\rm oct}}{\pi},\qquad
 \psi_t(t,u)=-\frac1\pi\operatorname{arsinh}
                  \bigl(\tan(t/2)\cos(u/2)\bigr).
 \tag{1}
\]

The formula for \(\psi_u\) is obtained by interchanging \(t,u\).
Here \(v_{\rm oct}\) is the volume of a regular ideal octahedron.
The logarithms initially have their values at \(t=u=0\), and
are then continued along the specified geometric path. When a
larger domain is used, a single-valued lift of this phase is part
of the data. The Hessian calculated below does not forget that
choice; it is the continuation of the Hessian in (1).

Put

\[
 a=\tan(t/2),\qquad b=\tan(u/2),\qquad
 q=\sqrt{1+a^2+b^2},\qquad q(0,0)=1.
 \tag{2}
\]

We work where \(\cos(t/2)\), \(\cos(u/2)\), and \(q\) are
nonzero. In the test below the continued root is required to
satisfy \(\Re q>0\). This specifies a root, rather than just
the equation for its square.

Differentiating (1) on its original branch gives

\[
 -2\pi\,\psi''(t,u)
 =H(t,u)
 =\frac1q
 \begin{pmatrix}
  1+a^2&-ab\\
  -ab&1+b^2
 \end{pmatrix}.
 \tag{3}
\]

For example, the square root in the derivative of
\(\operatorname{arsinh}(a\cos(u/2))\) is
\(q\cos(u/2)\), by continuation from completeness. This gives
the first diagonal entry in (3); differentiating with respect
to \(u\) gives the off-diagonal entry. Equivalently, with

\[
 \Delta=q\cos(t/2)\cos(u/2),
\]

the same matrix is

\[
 H=\frac1\Delta
 \begin{pmatrix}
 \cos(u/2)/\cos(t/2)&-\sin(t/2)\sin(u/2)\\
 -\sin(t/2)\sin(u/2)&\cos(t/2)/\cos(u/2)
 \end{pmatrix}.
 \tag{4}
\]

In particular,

\[
                  \det H=1,\qquad \operatorname{tr}H=q+q^{-1}.
 \tag{5}
\]

All these are identities for the original edge phase. They do
not use an approximation to it.

## 2. The exact positivity test

For a complex symmetric matrix \(H\), its Hermitian part is the
real symmetric matrix obtained by taking the real part of each
entry. We write this matrix as \(\Re H\).

**Proposition 1.** Suppose that the branch in (2) has \(\Re q>0\).
Then

\[
 \Re H>0
 \quad\Longleftrightarrow\quad
             \Re q>\bigl|\Im(a\overline b)\bigr|.
 \tag{6}
\]

Here \(>0\) means positive definite. More explicitly,

\[
 \det(\Re H)
   =\frac{(\Re q)^2-\bigl(\Im(a\overline b)\bigr)^2}{|q|^2},
 \qquad
 \operatorname{tr}(\Re H)
   =\Re q\,(1+|q|^{-2}).
 \tag{7}
\]

**Proof.** Write
\(H=\left(\begin{smallmatrix}A&B\\B&C\end{smallmatrix}\right)\).
The identity \(AC-B^2=1\) gives

\[
 \det(\Re H)
 =\frac{1+\Re(A\overline C)-|B|^2}{2}.
 \tag{8}
\]

For (3), the difference in the numerator is

\[
 \begin{aligned}
 \Re(A\overline C)-|B|^2
 &=|q|^{-2}
   \left[\Re\{(1+a^2)(1+\overline b^{\,2})\}-|ab|^2\right]\\
 &=|q|^{-2}
   \left[\Re(q^2)-2\{\Im(a\overline b)\}^2\right].
 \end{aligned}
\]

Since \(|q|^2+\Re(q^2)=2(\Re q)^2\), substitution into
(8) proves the determinant formula. The trace formula follows
from (5). Its right-hand side is positive. A real symmetric
two-by-two matrix with positive trace is positive definite
exactly when its determinant is positive. This proves (6).
\(\square\)

The test is strict. At equality in (6), the real part of the
Hessian has a zero eigenvalue, even though the complex
determinant in (5) is still one.

## 3. An explicit sufficient region

Define

\[
 \mathcal C=
 \left\{(t,u):
 |\Re t|<\pi,\quad |\Re u|<\pi,\quad
  \{\Im\tan(t/2)\}^2+\{\Im\tan(u/2)\}^2<1
 \right\}.
 \tag{9}
\]

On this region \(1+a^2+b^2\) has positive real part.
Consequently its principal square root is holomorphic and has
positive real part. It agrees with the complete branch wherever
that branch is continued inside this region.

**Corollary 2.** The matrix \(\Re H(t,u)\) is positive definite
throughout \(\mathcal C\).

**Proof.** Write \(a=A+iC\), \(b=B+iD\), and set

\[
 X=A^2+B^2,\qquad Y=C^2+D^2<1,\qquad Z=AC+BD.
\]

Then \(q^2=1+X-Y+2iZ\), so

\[
 (\Re q)^2
 =\frac{|1+X-Y+2iZ|+1+X-Y}{2}
 \ge 1+X-Y.
\]

Also \(\{\Im(a\overline b)\}^2=(BC-AD)^2\le XY\), whereas

\[
                (1+X-Y)-XY=(1-Y)(1+X)>0.
\]

Thus (6) holds strictly. \(\square\)

Condition (9) is sufficient, not necessary. For example, take

\[
                  t=\frac{2\pi}{3}-2i\log2,\qquad u=0.
 \tag{10}
\]

Then \(\Im\tan(t/2)=-15/13\), so (9) fails. Nevertheless

\[
                  H(t,0)=
             \operatorname{diag}\bigl(\sec(t/2),\cos(t/2)\bigr)
 \tag{11}
\]

has positive real part. In fact (11) has positive real part
on the entire strip \(|\Re t|<\pi\), at every imaginary height.
Its branch is \(q=\sec(t/2)\).

The example also lies in the positive single-edge geometric
chart: \(e^{it/2}\), its reciprocal, and
\(\sec(t/2)+\tan(t/2)\) and its reciprocal all have positive
real part. The eight shapes in Section 3 of
[the isolated-vertex geometry note](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_isolated_internal_vertex_geometry.md)
therefore have positive imaginary part. Thus (9) is not being
proposed as a characterization of positive tetrahedra. No
equivalence between positivity of all eight shapes and (6)
is claimed here.

## 4. Arbitrary powers and arbitrary connected sets of vertices

Let \(S\) be a finite set of selected vertices in an original
circle tree. Include each original edge incident to \(S\)
once. At an endpoint outside \(S\), fix the boundary angle at
zero. Let

\[
 \Psi_S(\mathbf t)=\sum_{vw}\psi(t_v,t_w),
 \qquad
 F_{\mathbf n,\boldsymbol c}(\mathbf t)
 =\Psi_S(\mathbf t)
   +\frac{i}{4\pi}\sum_{v\in S}n_vt_v^2
   -i\sum_{v\in S}c_vt_v,
 \tag{12}
\]

where \(n_v\) are real numbers (in particular, any fixed signed
integer powers), and \(c_v\) are real cone charges. Each
selected vertex is assumed to have at least one incident edge.
All phases are on one specified lift.

Let \(\Omega\subset\mathbb C^S\) be an open convex region.
Suppose that at every point of \(\Omega\), each edge with both
endpoints selected satisfies (6) on the continued branch.
An edge with only one selected endpoint is required to satisfy
the corresponding positive real diagonal test. For instance,
these assumptions hold if every edge pair belongs to
\(\mathcal C\); for an outside endpoint zero, (11) gives the
larger strip directly.

**Theorem 3.** Under these assumptions,

\[
                       \Re[-F''_{\mathbf n,\boldsymbol c}]>0
                       \quad\hbox{on }\Omega.
 \tag{13}
\]

For every fixed choice of the powers and cone charges, there
is at most one critical point of \(F_{\mathbf n,\boldsymbol c}\)
in \(\Omega\). If that critical point is \(z_*\), its Hessian
is nonsingular. On every real horizontal segment
\(z_*+sx\subset\Omega\), \(x\in\mathbb R^S\), \(0\le s\le1\),
the real action is strictly smaller than at \(z_*\), unless
\(x=0\).

If \(\Re[-F'']\ge\gamma I\) on such a segment, then the
quantitative comparison is

\[
         \Re F(z_*+x)\le \Re F(z_*)-\frac{\gamma}{2}|x|^2.
 \tag{14}
\]

**Proof.** The Hessian of \(-\Psi_S\) is the sum of the edge
matrices \(H/(2\pi)\), inserted in their original vertex
coordinates. Each summand has positive real part on its
endpoint coordinates. Every nonzero vector has a nonzero
coordinate at a vertex incident to one of these edges, so
the sum is positive definite. The filling quadratic
contributes \(-i\operatorname{diag}(n_v)/(2\pi)\); this is
skew-Hermitian and contributes zero to the Hermitian part.
The charge term contributes no Hessian. This proves (13).

Put \(G=-\nabla F\). If \(z,w\in\Omega\) and \(v=z-w\ne0\),
convexity permits integration along the straight segment:

\[
 \Re\bigl(v^*[G(z)-G(w)]\bigr)
 =\int_0^1
      \Re\bigl(v^*DG(w+sv)v\bigr)\,ds>0.
 \tag{15}
\]

For a complex symmetric matrix the Hermitian part is its
entrywise real part, so (13) applies also to complex vectors
\(v\). Thus \(G(z)\ne G(w)\). In particular there cannot be
two critical points. If \(F''v=0\), (13) applied to \(v\)
would give a contradiction, proving nonsingularity.

Finally, along the real horizontal segment the first
derivative at \(s=0\) is zero and the second derivative is
\(\Re(x^TF''x)<0\). Twice integrating proves the strict
comparison and (14). \(\square\)

Convexity of \(\Omega\) is an actual hypothesis. Neither
\(\mathcal C\) nor the full locus (6) has been asserted to
be convex. One may use convex subsets of these loci, or
verify (6) directly on a specified convex region.

## 5. Which existing geometric paths satisfy the test?

For the regular all-zero subtree geometry, the selected
angles are \(t_v=-ih_v\), with \(h_v\ge0\). Write
\(r_v=\tanh(h_v/2)\). On an edge \(vw\), condition (9)
becomes

\[
                         r_v^2+r_w^2<1.
 \tag{16}
\]

This is exactly the regular-edge condition already used
there:

\[
 r_v^2+r_w^2<1
 \quad\Longleftrightarrow\quad
        \sinh(h_v/2)\sinh(h_w/2)<1.
 \tag{17}
\]

To verify the equivalence, square the nonnegative product
and use \(\sinh^2(h/2)=r^2/(1-r^2)\). The resulting
inequality is
\(r_v^2r_w^2<(1-r_v^2)(1-r_w^2)\), which is (16).

Consequently the entire straight-height cone path in
[the regular zero-subtree geometry note](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_regular_zero_subtree_geometry.md)
satisfies (13) at its selected point. This includes its
uniform sufficient class

\[
                  \tan(\pi/d_v)\tan(\pi/d_w)\le1
 \tag{18}
\]

on each internal selected edge, in particular all selected
degrees at least four. The strict endpoint inequalities in
that note ensure (17) even when equality holds in (18).
This is a conclusion about that path and its small
neighborhoods. It does not put an entire period contour
inside one common convex region.

The small complex charts in
[the connected-filling geometry note](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_connected_short_filling_geometry.md)
also satisfy (9). For example, if \(|t|,|u|\le1/64\),
then \(|\tan(t/2)|,|\tan(u/2)|<1/127\), and the sum in
(9) is less than \(2/127^2\).

For an isolated selected vertex all its neighboring angles
are zero. Formula (11) supplies (13) on the entire convex
strip \(|\Re t|<\pi\), for every signed power \(n\).
The existence theorem in
[the isolated-vertex note](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_isolated_internal_vertex_geometry.md)
therefore supplies the unique selected critical point in
that strip whenever \(d+|n|>2\). No restriction to large
\(|n|\) or large degree is needed for this uniqueness.

## 6. The geometric value and what this comparison does not prove

The original peripheral formulas must still be retained.
With \(n_v=\eta_v-2p_v\), where \(\eta_v\) is the original
carrier and \(p_v\) is the integer filling coefficient,
they are

\[
 U_v=-2\pi(\Psi_S)_{t_v}-i\eta_vt_v,\qquad
 V_v=2it_v.
 \tag{19}
\]

The stationary equations for (12) give the full primitive
cone periods

\[
                         U_v+p_vV_v=-2\pi i c_v.
 \tag{20}
\]

Suppose a marked positive geometric path \(t(s)\), with
charges \(c_v(s)\), has actually been constructed, using the
original face pairings and the continued logarithms in
(19). Its core lengths are \(-2\Im t_v(s)\). Stationarity
then gives

\[
 \frac{d}{ds}\Re F_{\mathbf n,\boldsymbol c(s)}(\mathbf t(s))
       =\sum_v\Im t_v(s)\,c_v'(s).
 \tag{21}
\]

Schläfli's formula for this same cone path gives \(2\pi\)
times (21) as the volume derivative. Starting with its
complete octahedral volume fixes the additive constant.
This is the geometric calibration already proved for the
paths cited above. It is not a consequence of Hessian
positivity alone.

For \(0<c_v<1\), the meridian in (20) generally has
nontrivial elliptic holonomy. Its representation is a
representation of the unfilled exterior; it need not factor
through the group of the smoothly filled manifold.
An upper bound for volumes of representations of that
smoothly filled manifold therefore does not apply to this
intermediate path without another argument.

There are three distinct gaps between Theorem 3 and the
required dominant-saddle transport statement:

1. Other critical points need not lie in the convex region
   of Theorem 3. Positive shapes of the selected point do
   not place the other solutions of the gluing equations
   in the same positive angle domain or logarithmic lift.
2. A strictly concave horizontal action does not compare
   that action with critical values or endpoint
   contributions on other sheets. The
   [adjacent-pair alias identity](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_adjacent_alias_bloch_identity.md)
   gives an actual equal-real-action end. Its removal uses
   the exact source identities, not a strict inequality
   from geometry.
3. Even uniqueness of all finite critical points in a
   region does not prove that the original relative cycle
   can be deformed into it without additional divisors,
   residues, or ends. The nonzero coefficient of the
   selected cycle and estimates on the remaining chains
   are separate requirements.

Thus the result supplies a general, elementary criterion
for local and regional convexity that retains the actual
filling powers. For arbitrary fixed short partial fillings,
the still missing statement is a global comparison or an
exact reduction of the original period to a region where
such a comparison applies.
