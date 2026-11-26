# Positive edge geometry and global uniqueness of the filling equations

Research note, 2 November 2026. The eight original tetrahedra of a
circle-tree edge determine a domain on which its peripheral-period
map is globally strictly monotone. This statement compares any two
points of the domain; it does not require the segment between them
to remain positive. Summing the comparison over the original graph
proves uniqueness of a positive solution of the primitive filling
equations, for arbitrary signed powers.

Existence is a different question. The last section identifies what
can obstruct continuation of the positive solution. Neither
uniqueness nor existence by itself determines the coefficient of its
cycle in the original quantum period.

## 1. The original shapes in rational coordinates

Retain the notation of
[the Hessian calculation](research_cone_chamber_accretivity.md):

\[
 a=\tan(t/2),\qquad b=\tan(u/2),\qquad q^2=1+a^2+b^2,
 \qquad q(0,0)=1.
 \tag{1}
\]

The original meridian increments are

\[
 r_t=\operatorname{arsinh}\bigl(\tan(t/2)\cos(u/2)\bigr),
 \qquad
 r_u=\operatorname{arsinh}\bigl(\tan(u/2)\cos(t/2)\bigr).
 \tag{2}
\]

They satisfy \(\psi_t=-r_t/\pi\) and \(\psi_u=-r_u/\pi\).
All logarithms initially vanish at completeness. Their global
positive branches will be specified below.

The ordered cross-ratio calculation in Section 3 of
[the adjacent-pair geometry note](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_adjacent_two_crossing_pair.md)
gives the eight original shapes as

\[
       (A,B,-1/A,-1/B),\qquad(C,D,-1/C,-1/D).
 \tag{3}
\]

The four distinct expressions have the following rational form:

\[
 A=\frac{q+a}{b-i},\qquad
 C=\frac{q-a}{b-i},\qquad
 B=-\frac{q-b}{a+i},\qquad
 D=-\frac{q+b}{a+i}.
 \tag{4}
\]

To check the conventions, the original formulas are
\(A=i e^{r_t}e^{-iu/2}\),
\(C=i e^{-r_t}e^{-iu/2}\),
\(B=i e^{it/2}e^{-r_u}\), and
\(D=i e^{it/2}e^{r_u}\).
The identities
\(e^{r_t}=\cos(u/2)(q+a)\),
\(e^{r_u}=\cos(t/2)(q+b)\), and
\((q-a)(q+a)=1+b^2\) give (4).
Every expression is \(i\) at completeness. Thus these are the
original oriented tetrahedra, with the original two-octahedron
subdivision.

Throughout the proof a positive shape means a shape with strictly
positive imaginary part. Since \(z\mapsto-1/z\) preserves the upper
half-plane, positivity of (3) is equivalent to positivity of the
four expressions in (4).

## 2. Positivity is an exact matrix inequality

Put

\[
 L=\begin{pmatrix}q+a&b\\b&q-a\end{pmatrix},
 \qquad \det L=1.
 \tag{5}
\]

For a complex symmetric matrix, \(\Re L\) is both its entrywise
real part and its Hermitian part.

**Theorem 1.** At a regular configuration in (1)--(4), all eight
original tetrahedra are positive if and only if

\[
                  \Re L>0,
 \quad\hbox{equivalently}\quad
                  \Re q>\sqrt{(\Re a)^2+(\Re b)^2}.
 \tag{6}
\]

This is also equivalent to
\(\Re[-2\pi\psi''(t,u)]>0\) on the branch continued from the
positive complete configuration.

**Proof.** Write \(r=q+a\) and

\[
       k=(\Re r)(\Im b)-(\Im r)(\Re b).
\]

The determinant identity in (5) gives
\(q-a=(1+b^2)/r\). In particular
\(C=(b+i)/r\). Direct division in (4) gives

\[
 \Im A=\frac{\Re r-k}{|b-i|^2},
 \qquad
 \Im C=\frac{\Re r+k}{|r|^2}.
 \tag{7}
\]

Also

\[
       \det(\Re L)=
           \frac{(\Re r)^2-k^2}{|r|^2}.
 \tag{8}
\]

For completeness, write \(r=x+iy\), \(b=B+iD\). Then
\[
 |r|^2\left[x\,\Re\frac{1+b^2}{r}-B^2\right]
                  =x^2-(xD-yB)^2,
\]
which is (8).

Equations (7)--(8) show that \(A,C\) are both positive
exactly when the first diagonal entry of \(\Re L\) and its
determinant are positive. This is equivalent to \(\Re L>0\).
Applying the same calculation with \((a,b)\) replaced by
\((-b,-a)\) gives \(B,D\). The real matrices in the two
calculations have the same eigenvalues

\[
             \Re q\ \pm\sqrt{(\Re a)^2+(\Re b)^2}.
\]

Thus positivity of \(A,C\) also implies positivity of \(B,D\),
and proves (6).

To compare with the Hessian, write
\(P=\Re q\), \(Q=\Im q\),
\(X=(\Re a)^2+(\Re b)^2\),
\(Y=(\Im a)^2+(\Im b)^2\), and
\(Z=(\Re a)(\Im a)+(\Re b)(\Im b)\).
The identity \(q^2=1+a^2+b^2\) gives

\[
 P^2-Q^2=1+X-Y,\qquad PQ=Z.
\]

Since \(\{\Im(a\overline b)\}^2=XY-Z^2\), it follows that

\[
 P^2-\{\Im(a\overline b)\}^2
                 =(P^2-X)(1+X+Q^2).
 \tag{9}
\]

The determinant formula in Proposition 1 of the Hessian note
therefore reads

\[
 \det\Re[-2\pi\psi'']
       =\frac{(P^2-X)(1+X+Q^2)}{|q|^2}.
 \tag{10}
\]

The corresponding trace is \(P(1+|q|^{-2})\).
Consequently its real part is positive definite exactly when
\(P>\sqrt X\), proving the last assertion. \(\square\)

## 3. Global coordinates: two disks and two strips

The Cayley transform of (5) is

\[
 C_L=(L-I)(L+I)^{-1}
       =\frac1{q+1}\begin{pmatrix}a&b\\b&-a\end{pmatrix}.
 \tag{11}
\]

The notation \(C_L\) distinguishes this matrix from the
tetrahedron shape \(C\). Direct multiplication gives

\[
 I-C_L^*C_L
       =4(L+I)^{-*}(\Re L)(L+I)^{-1}.
 \tag{12}
\]

Set

\[
       \zeta=\frac{a+ib}{q+1},\qquad
       \xi=\frac{a-ib}{q+1}.
 \tag{13}
\]

The two eigenvalues of \(C_L^*C_L\) are
\(|\zeta|^2,|\xi|^2\): its equal diagonal entries are
\((|a|^2+|b|^2)/|q+1|^2\), and the off-diagonal entry is
\((\overline a b-\overline b a)/|q+1|^2\).
Thus (6) is exactly

\[
                           |\zeta|<1,\qquad|\xi|<1.
 \tag{14}
\]

Conversely, any pair in these two disks gives

\[
 q=\frac{1+\zeta\xi}{1-\zeta\xi},\qquad
 a=\frac{\zeta+\xi}{1-\zeta\xi},\qquad
 b=\frac{\zeta-\xi}{i(1-\zeta\xi)}.
 \tag{15}
\]

The denominator never vanishes, and (12) proves positivity.
This parametrizes the entire positive edge domain, not only a
neighborhood of completeness.

Now use the principal strip coordinates

\[
            P=\operatorname{artanh}\zeta,\qquad
            Q=\operatorname{artanh}\xi,\qquad
            |\Im P|,|\Im Q|<\frac{\pi}{4}.
 \tag{16}
\]

The function \(\operatorname{artanh} z=
\tfrac12\Log((1+z)/(1-z))\) maps the unit disk bijectively
onto this horizontal strip. Define

\[
                   f(P)=\arctan(\tanh P).
 \tag{17}
\]

Here the inverse tangent is the analytic branch at zero on the
unit disk. It satisfies

\[
             f'(P)=\frac1{\cosh(2P)},\qquad
             \Re f'(P)>0\quad (|\Im P|<\pi/4).
 \tag{18}
\]

Indeed \(\Re\cosh(2P)=\cosh(2\Re P)\cos(2\Im P)>0\),
and taking a reciprocal preserves the sign of the real part.

The original angles and meridian increments are exactly

\[
 \begin{aligned}
 t&=2\{f(P)+f(Q)\},&
 u&=-2i(P-Q),\\
 r_t&=P+Q,&
 r_u&=i\{f(Q)-f(P)\}.
 \end{aligned}
 \tag{19}
\]

One can verify the angle identities before taking logarithms:

\[
 e^{it}=
 \frac{(1+i\zeta)(1+i\xi)}
      {(1-i\zeta)(1-i\xi)},\qquad
 e^{iu}=
 \frac{(1+\zeta)(1-\xi)}
      {(1-\zeta)(1+\xi)}.
 \tag{20}
\]

All four one-variable factors in these quotients have analytic
logarithms on the disks. They fix (19) without an integer
ambiguity. Likewise
\[
 e^{2r_t}=\frac{(1+\zeta)(1+\xi)}
                    {(1-\zeta)(1-\xi)},\qquad
 e^{2r_u}=\frac{(1-i\zeta)(1+i\xi)}
                    {(1+i\zeta)(1-i\xi)}
\]
give the last two identities in (19).

These are the branches continued from \(t=u=0\).
They satisfy

\[
 |\Re t|,|\Re u|<\pi,\qquad
 |\Im r_t|,|\Im r_u|<\pi/2.
 \tag{21}
\]

For example, \(|\Re f(P)|<\pi/4\) because
\(f(P)=-i\operatorname{artanh}(i\tanh P)\).
This proves the first and the last bounds in (21); the other
two follow directly from (16).

The positive domain in the original \(t,u\) variables is not
convex. The two configurations

\[
                  (-4i\log3,0),\qquad (0,-4i\log3)
 \tag{22}
\]

are positive: the nonzero tangent is \(-40i/41\) and \(q=9/41\).
At their midpoint, however,
\(a=b=-4i/5\) and \(q^2=-7/25\), so (6) is impossible.
The strip coordinates, rather than a nonexistent convexity of
the \(t,u\) domain, are essential in the following comparison.

There is nevertheless a contraction to completeness in the
tangent variables. Write
\[
 X=(\Re a)^2+(\Re b)^2,\quad
 Y=(\Im a)^2+(\Im b)^2,\quad
 Z=(\Re a)(\Im a)+(\Re b)(\Im b),\quad
 D_0^2=XY-Z^2.
\]
For \(X>0\), condition (6) is equivalent to \(D_0^2<X\).
Indeed, writing \(q=P_0+iQ_0\), the identity
\[
 X-D_0^2=(P_0^2-X)(X+Q_0^2)
\]
proves the equivalence whenever the positive square root exists.
Conversely, \(D_0^2<X\) rules out a nonpositive real value of
\(q^2\): such a value would require \(Z=0\) and
\(Y\ge1+X\), hence \(D_0^2=XY\ge X\).
For \(X=0\), positivity is simply \(Y<1\).

Under \((a,b)\mapsto(sa,sb)\), \(0<s\le1\), the first
criterion becomes \(s^4D_0^2<s^2X\), and the second becomes
\(s^2Y<1\). Both are preserved. Thus simultaneously scaling
all original vertex tangents contracts the whole positive
network domain to completeness; outside angles zero remain
zero. Positive edges exclude the inverse-tangent cuts
\(a\in i[1,\infty)\cup-i[1,\infty)\), and similarly for
\(b\). For example, if \(\Re a=0\), \(|\Im a|\ge1\), and
\(\Re b\ne0\), then \(D_0^2\ge X\); if \(\Re b=0\),
then \(Y\ge1\). The contraction therefore gives continuous
principal angles \(t_v(s)=2\arctan(s\tan(t_v/2))\).

This fixes a common complete continuation of the positive
edge branches on the entire network. The contraction is
not generally a path of solutions of fixed filling
equations or a path with prescribed cone charges.

The original face chart has no further singularity hidden
by the simplified shapes. Its coordinates are
\[
 E=\frac{q+i}{q-i},\qquad
 R=\frac{1+b^2}{q^2+1},\qquad
 R_1=1-R=\frac{1+a^2}{q^2+1},\qquad
 Z_1=\frac{q+b}{q-i}.
\]
On the positive domain, \(q\), \(q\pm i\), \(q\pm a\),
and \(q\pm b\) are nonzero: the first follows from
\(\Re q>0\), and the last two pairs have positive real
parts by (6). The preceding exclusion of the inverse-tangent
cuts also gives \(a\pm i,b\pm i\ne0\).
The additional apex denominators factor as
\[
 Z_1-R_1=\frac{(q+b)(b+i)}{q^2+1},\qquad
 Z_1-E R_1=\frac{(q+b)(b-i)}{(q-i)^2}.
\]
They are therefore nonzero, as are the corresponding
expressions with the endpoints interchanged. Together
with the positive shapes, these identities verify that
the original ordered face formulas remain regular
throughout this continuation.

## 4. Global strict monotonicity of the edge periods

**Theorem 2.** Let \((t,u)\) and \((\widetilde t,\widetilde u)\)
be any two positive edge configurations, with the canonical
branches in (19). Use \(\delta\) to denote the difference of
the corresponding quantities. Then

\[
 \Re\{\delta r_t\,\overline{\delta t}
               +\delta r_u\,\overline{\delta u}\}>0
 \tag{23}
\]

unless the configurations are identical.

**Proof.** For any two points \(P,\widetilde P\) in the
convex strip (16), integration along their straight segment
and (18) give

\[
 \Re\{(P-\widetilde P)
              \overline{f(P)-f(\widetilde P)}\}
 =|P-\widetilde P|^2
      \int_0^1\Re f'(\widetilde P+s(P-\widetilde P))\,ds>0
 \tag{24}
\]

when \(P\ne\widetilde P\). The same holds for \(Q\).
Substitution of (19) into the left-hand side of (23)
gives the exact identity

\[
 \begin{split}
 &\Re\{\delta r_t\,\overline{\delta t}
               +\delta r_u\,\overline{\delta u}\}\\
 &\hspace{8mm}=4\Re\{\delta P\,\overline{\delta f(P)}
                         +\delta Q\,\overline{\delta f(Q)}\}.
 \end{split}
 \tag{25}
\]

The mixed terms cancel in their real parts. The right side
is strictly positive unless both strip coordinates agree.
Equations (15) and (19) then show that the edge configurations
agree. \(\square\)

Thus the period map is globally strictly monotone even
though its domain in the original angle coordinates is not
convex. The infinitesimal version of (25) recovers the
Hessian positivity in Theorem 1.

## 5. Arbitrary original signed filling powers

Let \(S\) be any selected set of vertices of the original
ordered circle tree. The argument also applies to any finite
network of these same edge blocks with the same peripheral
concatenation rules. Include each edge incident to \(S\) once,
and fix the angles at its outside endpoints. Every selected
vertex is assumed incident to at least one edge.

Orient each edge only to specify which endpoint is called
\(t\) in (19). At a selected vertex define

\[
                R_v(\mathbf t)=\sum_{e\ni v}r_{v,e}(\mathbf t).
 \tag{26}
\]

For the general-network extension this sum is over endpoint
incidences: a loop at \(v\) contributes both its endpoint
increments, and contributes two to \(d_v\). Original
circle trees have no loops.

The original primitive filling equations, with real powers
\(n_v\) and real cone charges \(c_v\), are

\[
                 R_v(\mathbf t)-\frac{i n_v}{2}t_v
                              =-\pi i c_v.
 \tag{27}
\]

For the original integer surgery data,
\(n_v=\eta_v-2p_v\), and

\[
 U_v=2R_v-i\eta_vt_v,\qquad V_v=2it_v,\qquad
                    U_v+p_vV_v=-2\pi i c_v.
 \tag{28}
\]

These are the full marked logarithmic periods, not merely
their exponentials.

**Theorem 3.** With the outside angles, powers, and charges
fixed, equations (27) have at most one solution for which
every original edge block is positive on the branches (19).
Any such solution has nonsingular complex Jacobian.

**Proof.** Suppose that two positive solutions exist.
Apply (23) to each edge and sum. At an outside endpoint
\(\delta t_v=0\), so its contribution vanishes. At selected
vertices the resulting sum is

\[
                       \Re\sum_{v\in S}
                           \delta R_v\,\overline{\delta t_v}.
 \tag{29}
\]

Subtracting (27) gives
\(\delta R_v=i n_v\delta t_v/2\).
Since \(n_v\) is real, every summand in (29) has zero real
part. On the other hand, Theorem 2 makes the sum strictly
positive if any edge configuration differs. Hence all edge
configurations, and therefore all selected angles, agree.

For the Jacobian, each edge derivative is \(H/2\), with
positive definite real part by Theorem 1. Insert these
matrices in the original vertex coordinates and sum.
The real part is positive definite because each selected
vertex is incident to an edge. Subtracting
\(i\operatorname{diag}(n_v)/2\) leaves that real part
unchanged. A complex matrix with positive definite
Hermitian part has no nonzero kernel. \(\square\)

The assertion permits adjacent selected vertices, arbitrarily
many of them, and powers of either sign and any magnitude.
It is a theorem about the actual primitive equations in this
positive edge decomposition. It does not assert that every
hyperbolic filling admits that decomposition with all its
original tetrahedra positive.

## 6. Eliminating a positive filled region preserves the comparison

Divide the vertices of an incident-edge network into interior
vertices \(S\), whose powers and charges are fixed, and boundary
vertices \(B\), whose angles are allowed to vary. Assume every
boundary vertex is incident to an included edge. Whenever the
interior equations have a positive solution, define the boundary
response by

\[
             \mathcal R_b(\mathbf t_B)
                =\sum_{e\ni b}r_{b,e}(\mathbf t_S(\mathbf t_B),
                                                    \mathbf t_B).
 \tag{32}
\]

Theorem 3 makes the interior solution unique. Its nonsingular
Jacobian makes it holomorphic locally. These local solutions
agree on overlaps, so (32) is a well-defined holomorphic response
on its realized positive domain.

**Corollary 4.** For any two different boundary assignments in
that domain,

\[
       \Re\sum_{b\in B}
          \delta\mathcal R_b\,\overline{\delta t_b}>0.
 \tag{33}
\]

The local derivative \(\mathcal R'\) is complex symmetric and
has positive definite real part.

**Proof.** Sum (23) over the original edges for the two
interior solutions. At each interior vertex,
\(\delta R_v=i n_v\delta t_v/2\), so the real part of its
contribution is zero. The remaining terms give (33).
If any boundary angle differs, at least one incident edge
configuration differs, making the comparison strict.

For the infinitesimal assertion, order the variables as
interior followed by boundary. The derivative of the
interior equations and boundary response before elimination
is a complex symmetric matrix

\[
             H_{\rm all}=
             \begin{pmatrix}A&B_0\\B_0^T&D\end{pmatrix},
                       \qquad \Re H_{\rm all}>0.
 \tag{34}
\]

Here \(A\) includes the interior terms
\(-i\operatorname{diag}(n_v)/2\).
Implicit differentiation gives the Schur complement

\[
                      \mathcal R'=D-B_0^TA^{-1}B_0.
 \tag{35}
\]

For any nonzero boundary vector \(y\), put
\(x=-A^{-1}B_0y\). Direct multiplication gives

\[
 \Re\left[y^*(D-B_0^TA^{-1}B_0)y\right]
          =\Re\left[
             \begin{pmatrix}x\\y\end{pmatrix}^{\!*}
             H_{\rm all}
             \begin{pmatrix}x\\y\end{pmatrix}\right]>0.
 \tag{36}
\]

The Schur complement is symmetric, proving the assertion.
\(\square\)

An original boundary carrier contributes a purely imaginary
real-coefficient multiple of its own angle to the peripheral
period. Adding this term preserves (33) and the positive real
part in (35). Each original carrier is added once, rather than
once for each block incident to its circle.

Consequently any number of positive regions can be eliminated
and then joined through their original shared boundary angles:
their monotonicity comparisons add, and further real signed
filling powers contribute zero real energy. This is a closure
property of the actual geometric period equations. It does
not assert a corresponding closure theorem for the quantum
integration cycles, estimates on other critical points, or
nonvanishing leading coefficients.

## 7. Continuation and its remaining obstruction

At the complete point, with all outside angles zero and all
charges zero, \(R_v=0\) and the Jacobian of (27) is

\[
                   \frac12\operatorname{diag}(d_v-i n_v),
 \tag{37}
\]

where \(d_v\) is the original degree. It is invertible.
Thus any fixed real powers admit a unique positive
solution for sufficiently small cone charges.

More generally, follow a continuous prescribed charge path
through positive solutions. Theorem 3 rules out both an
interior collision of solutions and a singular Jacobian.
If the solutions stay in a compact subset of the positive
domain, the implicit-function theorem extends them past
any finite endpoint of the charge interval. Therefore a
maximal positive continuation can stop only by leaving
every compact subset of that domain. In the disk
coordinates this means approaching a boundary
\(|\zeta_e|=1\) or \(|\xi_e|=1\), possibly with divergent
logarithmic coordinates or degenerate peripheral data.

There are immediate necessary range conditions. From (21)
and (27),

\[
                       |c_v|<\frac{d_v+|n_v|}{2}.
 \tag{38}
\]

Indeed,
\(\pi|c_v|\le|\Im R_v|+|n_v|\,|\Re t_v|/2\),
and each incident meridian increment has imaginary part
strictly smaller than \(\pi/2\).
At unit charge (38) gives \(d_v+|n_v|>2\).
This condition is sufficient in the isolated-vertex theorem.
No sufficiency for a connected selected set is claimed here.

The comparison (23) concerns the positive geometric branch.
Other critical points of the complexified original source
can lie outside this positive domain or on different
logarithmic lifts. Neither Theorem 3 nor the continuation
statement compares their critical values. The global
relative-cycle and endpoint requirements in
[the persistence theorem](research_dominant_saddle_transport.md)
therefore remain to be proved separately.

## 8. Related variational results

Existence and uniqueness through geometric variational principles
have substantial precedent. Bobenko and Springborn,
[*Variational principles for circle patterns and Koebe's theorem*](https://arxiv.org/abs/math/0203250),
Trans. Amer. Math. Soc. **356** (2004), 659--689, establish
existence and uniqueness results for circle patterns with prescribed
intersection angles. Rivin's
[*Combinatorial optimization in geometry*](https://arxiv.org/abs/math/9907032)
provides related optimization background, including applications to
hyperbolic structures on three-manifolds.

The statements proved here retain the original complex primitive
periods and arbitrary real filling powers, and include the boundary
response after eliminating a filled region. Their proofs are the
explicit shape identities and monotonicity calculations above.
This brief coverage check does not establish a novelty claim or
identify these statements with a theorem in either cited work.
