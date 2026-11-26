# Two-square radial limits and a regular lifted primitive system

Private written proof, 16 November 2026.

For a proper selected subset of an original circle tree, finite
two-square degenerations along a positive radial approach have a
restricted form. At a charge strictly between zero and one they are
internal matching edges, their endpoint real angles are zero, and
both endpoints have another strictly positive original edge. The
original period equations are nonsingular at every such limit after
retaining a vanishing edge square root as an independent variable.
This includes the square-root fold, not only the regular imaginary
square-root values.

The classification uses integer original powers, a common radial
charge, complete outside angles, and a supplied positive unit-charge
solution. The resulting local implicit-function theorem permits
independent nearby complex charges, but it does not assert this
classification for limits of arbitrary charge paths. Nor does it
complete a cone metric at a two-square corner or select a quantum
cycle.

## 1. Original data and the admitted limit

Let \(G\) be a finite connected original ordered circle tree with at
least one edge, and let
\(\varnothing\ne S\subsetneq V(G)\). Include every edge incident to
\(S\), once. Outside angles are complete: \(t_b=0\). Fix the actual
integer powers and their original marking,
\[
 n_v=\eta_v-2p_v\in\mathbb Z,\qquad v\in S.
 \tag{1}
\]
No change of these powers, carriers or peripheral curves will be
made. Write the original radial equations as
\[
 \mathcal P_v(t)=\sum_{e\ni v}r_{v,e}
                    -\frac{i n_vt_v}{2}=-\pi i\chi,
 \qquad 0<\chi\le1.
 \tag{2}
\]
Assume a positive solution at \(\chi=1\). Let \(I\) be the positive
radial set of the pinned compactness theorem. It is not assumed
connected. Consider a sequence \(\chi_j\in I\cap(0,1]\) approaching
a limit with at least one corner square.

We use the complete normalization of the original returns. At each
endpoint put
\[
 t_v=s_v-iH_v,\qquad
 r_{v,e}=k_{v,e}+ig_{v,e}.
 \tag{3}
\]
The radial theorem gives a jointly convergent subsequence of all
these coordinates and their square covectors. Throughout this note
their unadorned symbols denote that limit. It has
\[
 0<\chi_*<1,\quad H_v>0\ (v\in S),\quad
 |s_v|\le\pi,\quad |g_{v,e}|\le\pi/2.
 \tag{4}
\]
Outside \(s_b,H_b,r_{b,e}\) are zero. The strict inequalities in the
charge follow from the complete limit at zero and the unique
strictly positive closed minimizer at one. The uniform positive
height bound holds on every closed positive-charge interval, so
every selected height in (4) is strictly positive.

There are no open-side squares. Each boundary square is a finite
sharp corner, with its signed covectors \(U,V>0\) satisfying
\(\sinh(2U)\sinh(2V)=1\). All original affine rows survive:
\[
 \sum_{e\ni v}k_{v,e}=\frac{n_vH_v}{2},\qquad
 \sum_{e\ni v}g_{v,e}-\frac{n_vs_v}{2}=-\pi\chi_*.
 \tag{5}
\]
These conclusions are applied only to a limit of actual positive
solutions, not to an arbitrary corner KKT certificate.

For an ordered edge \(e=(v,w)\), the square coordinates are
\[
 \begin{aligned}
 A_P&=s_v/4-g_{w,e}/2,& A_Q&=s_v/4+g_{w,e}/2,\\
 y_P&=g_{v,e}/2+s_w/4,& y_Q&=g_{v,e}/2-s_w/4.
 \end{aligned}
 \tag{6}
\]
Thus the weak edge inequalities are
\[
 |s_v|+2|g_{w,e}|\le\pi,\qquad
 |s_w|+2|g_{v,e}|\le\pi.
 \tag{7}
\]
The original tangent and square-root coordinates and return
identities are
\[
 a_v=\tan(t_v/2),\quad a_w=\tan(t_w/2),\quad
 q_e^2=1+a_v^2+a_w^2,
 \tag{8}
\]
\[
 \begin{aligned}
 e^{r_{v,e}}&=\cos(t_w/2)(q_e+a_v),&
 e^{-r_{v,e}}&=\cos(t_w/2)(q_e-a_v),\\
 \sinh r_{v,e}&=a_v\cos(t_w/2),&
 \cosh r_{v,e}&=q_e\cos(t_w/2).
 \end{aligned}
 \tag{9}
\]
The symmetric identities hold at \(w\). The square root is the
one continued along the supplied positive sequence.
Positive heights keep every selected half-angle cosine nonzero;
outside cosines equal one. Bounded angles and returns therefore
allow (8)--(9) to pass to the limit, with no inverse-function
branch reset.

## 2. Real angular endpoints cannot occur

**Lemma 1.** Every selected endpoint in the limit satisfies
\[
                              |s_v|<\pi.
 \tag{10}
\]

**Proof.** Suppose \(s_v=\varepsilon\pi\), where
\(\varepsilon\in\{-1,1\}\). By (7), \(g_{w,e}=0\) on every
adjacent endpoint. Thus \(A_P=A_Q=\varepsilon\pi/4\). Since
neither square can lie on an open side, both \(y_P,y_Q\) are
endpoints of their intervals. Formula (6) implies
\[
 s_w\in\{0,\pi,-\pi\},\qquad
 \begin{cases}
 g_{v,e}\in\{-\pi/2,\pi/2\},&s_w=0,\\
 g_{v,e}=0,&|s_w|=\pi.
 \end{cases}
 \tag{11}
\]
At \(v\) the exact half-angle values are
\[
 a_v=-i\coth(H_v/2),\qquad
 \cos(t_v/2)=\varepsilon i\sinh(H_v/2).
 \tag{12}
\]

First let \(s_w=0\), allowing a complete outside endpoint. The
sinh identity in (9) is a negative imaginary number of modulus
strictly greater than one. Hence
\[
                         g_{v,e}=-\pi/2.
 \tag{13}
\]
Meanwhile \(g_{w,e}=0\) makes \(\cosh r_{w,e}\) strictly
positive real. By its cosh identity, \(q_e=-\varepsilon iQ\)
for some \(Q>0\). The other cosh identity now reads
\[
 -i\sinh k_{v,e}
          =-\varepsilon iQ\cosh(H_w/2).
 \tag{14}
\]
Consequently \(k_{v,e}\) is nonzero with sign \(\varepsilon\).

Next suppose \(s_w=\delta\pi\). Both returns have imaginary
part zero. Their positive real coshes in (9), and
\(\cos(t_w/2)=\delta i\sinh(H_w/2)\), force
\(\delta=\varepsilon\). Thus opposite signed angular endpoints
cannot be adjacent. The sinh identity at \(v\) gives
\[
 \sinh k_{v,e}
       =\varepsilon\coth(H_v/2)\sinh(H_w/2),
 \tag{15}
\]
again nonzero with sign \(\varepsilon\).

Consider a maximal connected component of vertices with
\(s=\varepsilon\pi\). Every adjacent vertex outside this component
has real angle zero. At every vertex in the component all its real
returns have sign \(\varepsilon\), so (5) gives
\(\operatorname{sgn}n_v=\varepsilon\). In particular integrality
gives \(|n_v|\ge1\).

The component is contained in \(S\). Connectedness of \(G\) and
properness of \(S\) provide a component vertex \(v\) with at least
one neighbor outside it. Let \(d_0(v)\ge1\) be the number of its
zero-real-angle neighbors. Equations (11), (13) and the imaginary
row in (5) give the exact equality
\[
                         2\chi_*=|n_v|+d_0(v)\ge2.
 \tag{16}
\]
This contradicts \(\chi_*<1\). \(\square\)

The integer-power restriction is substantive in this proof:
\(|n_v|\ge1\) need not hold for arbitrary real powers. The endpoint
argument only needs each relevant limiting charge to be below one;
it does not itself require them to be equal. The common radial
charge will be used in Theorem 3 to exclude a degree-one endpoint
of a two-square edge. Equation (16) does not contradict a charge
at or above one.

**Corollary 2.** For every \(\chi_0>0\) there is
\(\epsilon>0\), depending on the fixed data and supplied unit
solution, such that all positive radial solutions satisfy
\[
 |s_v|\le\pi-\epsilon
 \qquad(v\in S,\ \chi\in I\cap[\chi_0,1]).
 \tag{17}
\]

**Proof.** Otherwise choose a sequence approaching an angular
endpoint. The radial compactness theorem gives a finite limit
with positive heights. If its charge is one, its primal assignment
is the supplied positive minimizer; an interior limit at any other
charge is also positive. A corner limit at a charge in \((0,1)\)
contradicts Lemma 1. These exhaust the possibilities. \(\square\)

## 3. The complete two-square subgraph

Call an edge *two-square* if both of its square factors are corners
at the admitted limit. Denote the set of these edges by \(T\).

**Theorem 3.** The following statements hold.

1. Every edge \(e=(v,w)\in T\) has both endpoints in \(S\), with
\[
 s_v=s_w=0,\qquad
 g_{v,e}=g_{w,e}=-\pi/2.
 \tag{18}
\]
Writing \(A_v=\tanh(H_v/2)\) and \(A_w=\tanh(H_w/2)\),
\[
 0<A_v,A_w<1,\quad a_v=-iA_v,\quad a_w=-iA_w,\quad
 q_e=iQ_e,\quad Q_e^2=A_v^2+A_w^2-1\ge0.
 \tag{19}
\]
In particular \(|Q_e|<\min(A_v,A_w)<1\).

2. The edges in \(T\) form a matching. If \(T\ne\varnothing\),
then \(\chi_*>1/2\). Both endpoints of each edge in \(T\) have
another original edge, and every such other edge is strictly
positive.

3. Every included edge outside \(T\) is positive or a regular
single-square corner. On a two-square edge the factors
\[
 a_v\pm i,\ a_w\pm i,\ q_e\pm a_v,\ q_e\pm a_w,\ q_e\pm i
 \tag{20}
\]
are all nonzero. The only possible square-root ramification is
\(q_e=0\). It is not excluded.

**Proof.** A finite sharp corner places its disk coordinate on the
unit circle away from \(1,-1,i,-i\). If both disk coordinates
\(\zeta,\xi\) are on that circle, their finite tangent coordinates
satisfy
\[
 q=\frac{1+\zeta\xi}{1-\zeta\xi},\quad
 a=\frac{\zeta+\xi}{1-\zeta\xi},\quad
 b=\frac{\zeta-\xi}{i(1-\zeta\xi)}.
 \tag{21}
\]
Here \(\zeta\xi\ne1\). Indeed finite \(q\), supplied by (8),
and \((q+1)(1-\zeta\xi)=2\) exclude that value. Formula (21)
then makes \(q,a,b\) purely imaginary. In the closed canonical
angular strip a purely imaginary tangent has real angle zero or
\(\pm\pi\). Lemma 1 leaves only zero. Thus the endpoint tangents
have the form in (19).

At any selected vertex with \(s_v=0\), every incidence obeys
\[
 \Im\sinh r_{v,e}
       =-A_v\cos(s_w/2)\cosh(H_w/2)<0,
 \tag{22}
\]
since all neighboring real angles are strictly between
\(-\pi\) and \(\pi\), including outside angles zero. As
\(\Im\sinh(k+ig)=\cosh k\sin g\), the canonical closed range
implies
\[
                              g_{v,e}<0
                   \quad\hbox{on every incidence at }v.
 \tag{23}
\]
For a two-square edge, (6) with \(s_v=s_w=0\) requires
both \(|g_{v,e}|=|g_{w,e}|=\pi/2\); (23) fixes the signs in
(18). Equations (8) and (21) give (19). An outside endpoint would
have \(A_w=0\), contradicting \(A_v^2+A_w^2\ge1\). The strict
bound on \(|Q_e|\) follows because both \(A_v,A_w<1\). It
also proves all the nonvanishings in (20).

At a vertex incident to \(d_T(v)\) two-square edges, the imaginary
row has no carrier term because \(s_v=0\). Therefore (18), (23)
give
\[
                           \chi_*\ge d_T(v)/2.
 \tag{24}
\]
Since \(\chi_*<1\), one has \(d_T(v)\le1\), proving the matching
assertion. For any edge of this matching at least one endpoint
has another original edge: otherwise connectedness would make
the whole original tree this two-vertex edge, contrary to proper
selection. Its additional strictly negative incidence in (23)
implies \(\chi_*>1/2\). A degree-one endpoint at the other end
would force \(\chi_*=1/2\) by its own row. The common radial
charge therefore excludes that leaf also.

It remains to check the stronger assertion that the other edges
are positive. Let such an edge meet \(v\), with
\(a_v=-iA_v,\ 0<A_v<1\). If \(b=a_w\) has nonzero real part
\(x\), the exact positive-edge criterion uses
\[
 X=(\Re a_v)^2+(\Re b)^2=x^2,\qquad
 D_0^2=\{\Im(a_v\overline b)\}^2=A_v^2x^2<X.
 \tag{25}
\]
It is therefore strictly positive on the limiting branch, whose
square root has nonnegative real part. The strict inequality makes
that real part positive.

If \(\Re b=0\), Lemma 1 gives \(s_w=0\); put
\(b=-iA_w\), allowing \(A_w=0\) outside. When
\(A_v^2+A_w^2<1\) the edge is strictly positive by the other
case of the same criterion. Otherwise (9) gives
\[
 |\sinh r_{v,e}|=
     \frac{A_v}{\sqrt{1-A_w^2}}\ge1,
 \tag{26}
\]
a negative imaginary value. Hence \(g_{v,e}=-\pi/2\), and
the symmetric identity gives \(g_{w,e}=-\pi/2\).
Both squares would be corners. This is a second matching edge at
\(v\), a contradiction.

Finally there are no open-side squares, and every finite sharp
single corner is regular by the pinned corner classification.
This proves all alternatives in part 3. \(\square\)

The theorem does not rule out a two-square edge. It identifies the
entire such subgraph at the limit and the positive edges attached
to it. In particular, it distinguishes a finite regular imaginary
root \(q_e\ne0\) from the genuine fold \(q_e=0\), rather than
discarding the latter.

## 4. Coercivity after omitting the fold edges

For a nonfold edge the derivative of its original return pair is
\[
 J_e=\frac1{2q_e}
 \begin{pmatrix}
 1+a_v^2&-a_va_w\\
 -a_va_w&1+a_w^2
 \end{pmatrix},\qquad \det J_e=1/4.
 \tag{27}
\]
Its Hermitian part is positive definite on a positive edge.
At a regular single-square corner it is nonnegative of rank one,
and its real kernel line has two nonzero coordinates. The latter
statement means a zero endpoint variation forces the other endpoint
variation to vanish.

On a nonfold two-square edge, (19) gives instead
\[
 J_e=\frac1{2iQ_e}
 \begin{pmatrix}
 1-A_v^2&A_vA_w\\
 A_vA_w&1-A_w^2
 \end{pmatrix},\qquad \Re J_e=0.
 \tag{28}
\]
Here \(\Re\) denotes the Hermitian part; for these symmetric
matrices it equals the entrywise real part.

Let \(F=\{e\in T:q_e=0\}\). For each remaining included edge,
let \(\iota_e\) insert a selected variation into its two endpoint
slots, using zero at an outside endpoint. Define
\[
 J_{\rm rest}
   =\sum_{e\notin F}\iota_e^T J_e\iota_e
                         -\frac i2\operatorname{diag}(n_v).
 \tag{29}
\]

**Lemma 4.** At the admitted limit,
\[
                            \Re J_{\rm rest}>0.
 \tag{30}
\]
In particular, if there are no fold edges, the ordinary selected
primitive Jacobian is nonsingular, even when \(T\ne\varnothing\).

**Proof.** All included Hermitian forms in (29) are nonnegative.
A vector in their joint kernel vanishes at every selected endpoint
incident to a positive edge. Theorem 3 therefore pins both
endpoints of every two-square edge, including every omitted fold
edge. Extend the vector by zero outside \(S\).

Along a single-square corner edge zero propagates to the other
endpoint. A positive edge pins both endpoints; the endpoints of a
two-square edge are already pinned. Follow an original graph path
from any selected vertex to an outside vertex. These three facts
propagate zero along it, so the entire vector is zero. The proof
applies to complex variations as well, since each real kernel line
is complexified and every Hermitian form is nonnegative. \(\square\)

## 5. The original equations in a regular lifted fold chart

At an edge \(e=(v,w)\in F\), abbreviate
\[
 A=A_v,\qquad B=A_w,\qquad
 A,B>0,\quad A^2+B^2=1.
 \tag{31}
\]
Retain \(q_e\) as an independent complex variable and impose
\[
 f_e(t,q_e)=q_e^2-1-\tan^2(t_v/2)-\tan^2(t_w/2)=0.
 \tag{32}
\]
For nonfold edges use their locally holomorphic square roots with
the given limiting values. At a fold use the holomorphic returns
\[
 \begin{aligned}
 \widehat r_{v,e}(t,q_e)
     &=\log\{\cos(t_w/2)(q_e+\tan(t_v/2))\},\\
 \widehat r_{w,e}(t,q_e)
     &=\log\{\cos(t_v/2)(q_e+\tan(t_w/2))\}.
 \end{aligned}
 \tag{33}
\]
All logarithm arguments are nonzero near the limit by (20).
Choose their branches to have the original limiting values
\(-i\pi/2\). These values follow directly from (9), (18),
and \(A^2+B^2=1\): both arguments in (33) equal \(-i\).
On (32), (33) are exactly the original continued returns,
including their logarithmic lifts. The supplied positive sequence
lies in these branches when sufficiently close.

The full lifted system consists of \(|S|+|F|\) equations in the
same number of unknowns \((t_v)_{v\in S},(q_e)_{e\in F}\):
\[
 \begin{cases}
 \displaystyle\sum_{e\ni v}\widehat r_{v,e}
                    -\frac{i n_vt_v}{2}=-\pi i c_v,&v\in S,\\
 f_e(t,q_e)=0,&e\in F.
 \end{cases}
 \tag{34}
\]
On nonfold edges the hat denotes the ordinary original return.
The base charge is \(c_v=\chi_*\) for all \(v\).

**Theorem 5.** The Jacobian of (34) with respect to \((t,q_F)\)
is invertible at the admitted limit. Thus there is a unique local
holomorphic solution of the lifted original primitive equations
for all complex charge vectors \(c\) sufficiently near
\(\chi_*\mathbf1\), with the prescribed limiting values and
logarithmic branches.

**Proof.** We compute each fold block with the other variables
fixed. At \(q=0,a_v=-iA,a_w=-iB\),
\[
 df_e=iAB(B\,dt_v+A\,dt_w).
 \tag{35}
\]
The angular derivative and \(q\) column of its return pair in (33)
are respectively
\[
 C_e=
 \begin{pmatrix}
 iB^2/(2A)&iB/2\\
 iA/2&iA^2/(2B)
 \end{pmatrix},
 \qquad
 \partial_q
 \binom{\widehat r_{v,e}}{\widehat r_{w,e}}
        =\binom{i/A}{i/B}
        =\frac{i}{AB}\binom{B}{A}.
 \tag{36}
\]
For example,
\(\partial_{t_v}\log(q+a_v)=(1+a_v^2)/(2(q+a_v))\)
and
\(\partial_{t_w}\log\cos(t_w/2)=-a_w/2\),
giving the first row. Formula (35) is the direct derivative of
(32).

Let \((w,\nu)\) be in the kernel of the full Jacobian.
For each fold define the real selected vector \(\ell_e\) supported
at \(v,w\), with entries \(B,A\). The constraint equations imply
\[
                              \ell_e^T w=0.
 \tag{37}
\]
On the two endpoint slots this says \(w=(A,-B)z\) for some
complex \(z\), and direct multiplication in (36) gives
\(C_e(A,-B)^T=0\). Thus every fold's angular derivative
vanishes on the constrained tangent vector.

Let \(L\) have columns \(\ell_e\), and put
\(D=\operatorname{diag}(1/(A_eB_e))\). The remaining linearized
primitive equations reduce exactly to
\[
                       J_{\rm rest}w+iLD\nu=0,\qquad L^Tw=0.
 \tag{38}
\]
Since \(L\) is real, the second relation also gives \(w^*L=0\).
Multiply the first relation by \(w^*\), take real parts and use
Lemma 4. It follows that \(w=0\). Then \(LD\nu=0\).
The fold edges form a matching, so the columns of \(L\) have
disjoint nonempty supports and are linearly independent.
Every diagonal entry of \(D\) is nonzero; hence \(\nu=0\).
The square Jacobian is injective and therefore invertible.
The holomorphic implicit-function theorem proves the assertion.
\(\square\)

The fold is regular in this lifted system even though \(q\) cannot
be a holomorphic function of two unconstrained endpoint angles
there. The projection of the charge-parametrized solution to the
angle coordinates need not be locally invertible. Neither
\(\det J_e\) away from zero nor interior nonsingularity alone would
justify Theorem 5; its proof uses the additional constraint and
the positive edges forced by the original radial rows.
In particular this theorem does not assert a nondegenerate scalar
phase Hessian in the lifted variables. A fold tangent may have
\(dt=0\) and \(dq_e\ne0\); the angular critical one-form alone
does not detect that direction in the same manner as the full
primitive-period map.

For the actual filling marking the full periods along the local
solution are still
\[
 U_v=2\sum_{e\ni v}\widehat r_{v,e}-i\eta_vt_v,\qquad
 V_v=2it_v,\qquad U_v+p_vV_v=-2\pi i c_v.
 \tag{39}
\]
This identity follows from (1) and (34), with the original local
logarithms. It makes no integer change to a return, carrier or
peripheral row.

## 6. Consequences and limits of the statement

For the supplied positive radial approach, every finite corner
alternative now has a regular local system of original primitive
equations: ordinary angle coordinates suffice when no \(q_e\)
vanishes, and the finitely many matching square roots give the
lifted coordinates in Theorem 5 otherwise. Close terms of the
approaching sequence lie on that unique local branch by the
implicit-function theorem.

This is local analytic control of the specified limit. It does not
show that the positive radial set is connected, that a continued
branch still consists of positive original cells, or that a
completed cone metric exists at a two-square limit. In particular
the previously proved uniform-end and marked-metric continuation
theorems have regular single-square hypotheses; those theorems
are not invoked at the two-square edges here. A metric attachment,
volume calibration there, and transport of the original relative
quantum cycle require additional arguments.

The classification is not asserted for arbitrary independent
charge approaches or arbitrary noninteger powers. Independent
charge variation occurs only after the common-charge integral
limit has been classified and its lifted Jacobian proved
invertible. No new class of short fillings satisfying the original
volume identity is claimed.

## Direct sources

The following four source texts were read in full, with their
directly used identities checked at the pinned versions.

* [Radial compactness and sharp corners](research_radial_charge_compactness_and_corners.md),
  SHA256
  \(\texttt{744d36368876f255df6e2b1f2ca15dd23e805d5d5a39b009f6983fec2c6243ec}\):
  unique closed minimizers, the zero and unit endpoints, bounded
  actual returns/covectors, no open-side limits, sharp corner
  equalities, and uniform positive heights.
* [Original positive edge periods](research_positive_edge_global_monotonicity.md),
  SHA256
  \(\texttt{da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500}\):
  exact tangent/disk formulas, canonical logarithmic ranges and
  return identities, the strict positive-edge criterion, and the
  original carrier and full peripheral periods.
* [Original square-corner geometry](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_square_corner_flat_geometry.md),
  SHA256
  \(\texttt{511c2c93d61482664cf62ed3b146c0af19ffbb149fa8772a4d1eb5ca7026eed0}\):
  finite sharp disk limits, regular single-square corners, and
  the distinct two-square singular products, including \(q=0\).
* [Regular corner period assembly](research_regular_corner_period_assembly.md),
  SHA256
  \(\texttt{7d551e90d04b7c45232074109581bf2a807569259f98ad81e00855bec7f51ce5}\):
  the literal edge Jacobian, positive and rank-one corner
  Hermitian forms, nonzero kernel gains and original incidence
  assembly. The new zero-Hermitian two-square blocks and the fold
  augmentation are proved above, not attributed to that theorem.

Only written mathematics, source-text reads and file hashes were
used. No mathematical program, numerical computation, test or
compilation was run. Frozen sources, manuscripts and public
documents were unchanged.
