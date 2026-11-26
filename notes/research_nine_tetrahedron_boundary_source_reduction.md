# The literal nine-tetrahedron source and its paired-face quotient

Private written proof, 17 November 2026. This records the complete
incidence, a charge lift, and an exact six-variable reduction of the
nine-cell crossing source specified in [K, Section 4]. In the explicit
charge lift, for every crossing sector, the actual boundary tensor lies
in the paired-face adapter image proved in [A]. Its inverse loses no boundary
data. The recovered four-index tensor is **not yet identified** with
Kashaev's crossing weight. Neither the printed identity (4.25) nor a
closed contraction of it is a premise.
An ordered-decoration limit also proves a normalization obstruction:
with the explicit 1994 scalars used here, one actual boundary entry
has leading coefficient \(q\), whereas the unit-coefficient printed
crossing expression has \(N^2q\). This does not evaluate the recovered
array globally.

## 1. Conventions and the nine cells

Let \(N>2\) be odd, \(q\) a primitive \(N\)-th root, and let
\(\epsilon=1/2\) in \(\mathbb Z/N\mathbb Z\). All indices, charges,
and exponents of \(q\) below are in that ring. Choose six distinct
complex vertex decorations \(z_0,\ldots,z_5\), and compatible fixed
roots
\[
 s_{ij}^{\,N}=z_i-z_j\qquad(i<j).
\]
Work on a lifted regular domain for those roots and the normalization
square roots in [B]. For a sorted tetrahedron \(T=abcd\), put
\[
 X_T=s_{ad}s_{bc},\qquad Y_T=s_{ab}s_{cd},\qquad
 Z_T=s_{ac}s_{bd}.
\]
Then \(X_T^N+Y_T^N=Z_T^N\), and all three entries are nonzero.
Write
\[
 W_T(n)=\prod_{j=1}^{[n]}\frac{Y_T}{Z_T-X_Tq^j},
 \qquad
 \overline W_T(n)=
       \prod_{j=1}^{[n]}\frac{Y_T}{Z_T-(X_T/q)q^j}.       \tag{1}
\]
These are nonzero periodic functions. The bar in this notation is
a label and does not mean complex conjugation.

The scalars \(\rho_T,\bar\rho_T\) are the literal finite
normalizations of [B, (2),(5)], with
\[
 (P,Q,R,B,C,H)=(s_{ab},s_{bc},s_{cd},s_{ac},s_{bd},s_{ad}).
                                                               \tag{2}
\]
In particular all normalization sums and their shared root choices
remain present.
The 1995 paper refers to the earlier paper for these scalar functions,
without displaying a scalar-conversion formula there. Our normalization
is the explicit one in (2); a different conversion must be stated and
checked, rather than supplied by assuming its printed contraction.

For the sorted tetrahedron let \(\alpha_i\) denote the face omitting
local vertex \(i\). The local charges are written \((a,b,c)\) on
the opposite pairs
\[
 ab|cd,\qquad ac|bd,\qquad ad|bc,
 \quad\text{with }a+b+c=\epsilon,
\]
where the letters in the pairs denote the vertices, not the charges.
The parameters in the tensor are the first and third charges.
To avoid an implicit matrix convention, define the positive and
negative tensors directly from [K, (4.6),(4.7)]:
\[
\begin{split}
 T_T(a,c)_{\alpha,\beta}^{\gamma,\delta}
 &=\rho_T\,
 q^{c(\gamma-\alpha)+\alpha\delta+ac/2+\alpha^2/2}
 W_T(\gamma-a-\alpha)\,
 \delta_{\beta,\gamma+\delta},\\
 \bar T_T(a,c)_{\gamma,\delta}^{\alpha,\beta}
 &=\bar\rho_T\,
 q^{c(\gamma-\alpha)-\alpha\delta-ac/2-\alpha^2/2}
 \overline W_T(\gamma+a-\alpha)^{-1}
 \delta_{\beta,\gamma+\delta}.
\end{split}                                                     \tag{3}
\]
For either orientation the four face slots are
\((\alpha,\beta,\gamma,\delta)=(\alpha_3,\alpha_1,\alpha_2,\alpha_0)\).

The nine ordered cells and their orientations are
\[
\begin{array}{c|rrrrrrrrr}
T&1234&1245&2345&0123&0134&0125&0235&0345&0145\\ \hline
\operatorname{sign}(T)&+&+&+&+&+&-&-&-&+
\end{array}.                                                     \tag{4}
\]
Indeed, starting with positive \(1234\), the four first attachments
are positive. Their remaining octahedral faces are filled by the last
four cells with the signs in (4). This can also be checked by cancelling
the oriented boundaries occurrence by occurrence.

Here is every internal face pairing; the number in parentheses is
the omitted local vertex:
\[
\begin{array}{c|ll}
123&1234(3)&0123(0)\\
124&1234(2)&1245(3)\\
134&1234(1)&0134(0)\\
234&1234(0)&2345(3)\\
013&0123(2)&0134(3)\\
245&1245(0)&2345(1)\\
012&0123(3)&0125(3)\\
125&1245(2)&0125(0)\\
023&0123(1)&0235(3)\\
235&2345(2)&0235(0)\\
034&0134(1)&0345(3)\\
345&2345(0)&0345(0)\\
014&0134(2)&0145(3)\\
145&1245(1)&0145(0)
\end{array}.                                                     \tag{5}
\]
Each map preserves the displayed vertex labels. The four edges
\(05\) belonging to the four last cells remain distinct.

Write \(p_m=\alpha_m^+\) and \(m_m=\alpha_m^-\) for the two
boundary faces \(0m5\). The actual boundary slots are
\[
\begin{array}{c|cc}
0125&015=p_1&025=m_2\\
0235&025=p_2&035=m_3\\
0345&035=p_3&045=m_4\\
0145&015=m_1&045=p_4 .
\end{array}                                                     \tag{6}
\]
The sign here uses [K]'s right/left face convention: in a positive
sorted tetrahedron faces \(3,1\) are right, and faces \(2,0\) are
left. A right face has the negative sign in the oriented simplicial
boundary. This explains the apparent reversal between (4) and (6).

There are no interior vertices. The interior edges are
\(12,13,14,23,24,34\); the specified tangle consists of \(13,24\).
Consequently the only interior edge weights in [K, (4.19)] are
\[
                \mathfrak e=(s_{12}s_{23}s_{34}s_{14})^{-(N-1)}.
                                                               \tag{7}
\]
There is no interior-vertex power of \(N\) in this crossing ball.
These statements follow directly from (5),(6), rather than from
an Euler-characteristic argument about a different cellulation.

## 2. An explicit charge lift

Let the four distinct \(05\) charges, in collar order, be
\((x,y,z,w)\), with \(x+y+z+w=1\). Let \(h_m\) be the total
charge on the boundary edge \(m5\), with \(\sum_m h_m=2\).
The following opposite-pair triples give an actual charge lift:
\[
\begin{array}{c|ccc}
1234&0&\epsilon&0\\
1245&0&\epsilon&0\\
2345&1&\epsilon-1&0\\
0123&-y&x+y-\epsilon&1-x\\
0134&1-z&\epsilon-w&-x-y\\
0125&y+z-h_1&h_1+w-\epsilon&x\\
0235&1+z-h_1-h_2&h_1+h_2-y-z-\epsilon&y\\
0345&h_4-1&1+\epsilon-h_4-z&z\\
0145&0&\epsilon-w&w .
\end{array}                                                     \tag{8}
\]
Every row sums to \(\epsilon\). The four non-link interior totals
are one, and the two link totals are zero. For example the totals
on \(13,24\) are respectively
\[
 \epsilon+(x+y-\epsilon)-x-y=0,\qquad
 \epsilon+0+(\epsilon-1)=0.
\]
On \(14\) the total is
\(\epsilon+(\epsilon-w)+w=1\); the totals on \(12,23,34\)
are respectively \(1-x+x,1-y+y,1-z+z\).
Substitution also gives
\[
 c_{\rm tot}(m5)=h_m,\qquad c_{\rm tot}(0m)=1-h_m.       \tag{9}
\]
Thus the boundary conditions used here are exactly specified.

Conversely, the two sum conditions are necessary for any such
charge assignment. Each of vertices \(1,\ldots,4\) occurs in six
tetrahedra. Subtracting its three prescribed interior-edge totals
from its total vertex charge \(6\epsilon=3\) gives
\(c_{\rm tot}(0m)+c_{\rm tot}(m5)=1\).
The sum of all nine tetrahedral edge-charge sums is nine.
Subtracting the four non-link interior totals leaves boundary sum
five, hence \(x+y+z+w=1\). Vertex \(5\) then gives
\(\sum_mh_m+(x+y+z+w)=3\), or \(\sum_mh_m=2\).
No division other than the legitimate odd-level \(1/2\) is used.

For the rest of the finite reduction fix the canonical sector
\[
                  (x,y,z,w)=(1,0,0,0),               \tag{10}
\]
while retaining all four \(h_m\) and all eight boundary face indices.
This is one local charge sector, not permission to choose all sectors
canonically in a global diagram whose region totals are prescribed.

## 3. Eliminating every Kronecker symbol

Give the internal faces the following names:
\[
\begin{array}{c|rrrrrrrrrrrrrr}
\text{face}&123&124&134&234&013&245&012&125&023&235&034&345&014&145\\ \hline
\text{index}&A&B&C&D&E&F&G&H&I&J&K&L&M&V .
\end{array}
                                                               \tag{11}
\]
The letter \(V\) here is the index on face \(145\).
The nine deltas in (3) say
\[
\begin{gathered}
 C=B+D,\quad V=H+F,\quad F=J+L,\quad
 I=E+A,\quad K=M+C,\\
 H=m_2-p_1,\quad J=m_3-p_2,\quad L=m_4-p_3,\quad
 V=p_4-m_1.                                           \tag{12}
\end{gathered}
\]
The last four determine \(H,J,L,V\); the first three then impose
one boundary condition,
\[
 \sum_m(m_m-p_m)=0.                                   \tag{13}
\]
When it holds, the six free internal indices are \(A,B,D,E,G,M\).
Every eliminated sum contributes exactly one. In particular no
factor \(N\) may be inserted for a redundant boundary delta.

Set
\[
 k_m=m_m-p_m+h_m.
\]
Condition (13) is equivalent to \(\sum_m k_m=2\).
Make the following invertible affine change of the six free indices:
\[
 u=B-A,\quad v=H-B,\quad t=J-1-D,\quad
 r=E-G,\quad s=M-1-E,\quad z=m_1-M.                    \tag{14}
\]
Here \(z\) is a finite summation index, not a vertex decoration.
For example the inverse gives
\[
 B=H-v,\ A=H-v-u,\ D=J-1-t,\ M=m_1-z,\ 
 E=m_1-1-z-s,\ G=m_1-1-z-s-r.
\]
Thus (14) is a bijection over every odd \(\mathbb Z/N\mathbb Z\),
including composite levels.

Define the fully retained normalization
\[
 \mathfrak n=\mathfrak e\,
 \rho_{1234}\rho_{1245}\rho_{2345}\rho_{0123}\rho_{0134}
 \bar\rho_{0125}\bar\rho_{0235}\bar\rho_{0345}\rho_{0145}.
                                                               \tag{15}
\]
Let \(\mathcal B(\mathbf m,\mathbf p)\) be the literal sum of
the nine tensors (3), over all fourteen internal faces (5),
multiplied by (7). Then it is zero unless \(\sum k_m=2\).
On that support it is exactly
\[
\begin{split}
 \mathcal B(\mathbf m,\mathbf p)=\mathfrak n
 \sum_{u,v,t,r,s,z}
 &q^{\,\Xi(u,v,t,r,s,z;\mathbf k,h_1)}
 W_{1234}(u)W_{1245}(v)W_{2345}(t)\\
 {}\cdot&
 W_{0123}(r)W_{0134}(s)W_{0145}(z)\\
 {}\cdot&
 \left[
 \overline W_{0125}(1-k_1+r+s+z)\,
 \overline W_{0235}(2-k_1-k_2+u+v+s+z)\,
 \overline W_{0345}(k_4+t+v+z)
 \right]^{-1},
\end{split}                                                     \tag{16}
\]
where every sum runs independently over \(\mathbb Z/N\mathbb Z\), and
\[
 \Xi=u(1+t+r)+v(1+r+s)+(1+t)(1+s)+z+r-k_1
                                      +(3h_1-1)/2.              \tag{17}
\]
All denominators in (16) are units on the specified regular domain.

For completeness, the phase calculation is as follows. Before the
deltas are substituted, the explicit non-Gaussian tensor phases sum to
\[
 AD+BF+DL+GA+EC-IJ-KL+MV-GH-M+E+p_1-G+(h_1-1)/2.
\]
The Gaussians inside the two-index \(w\)'s contribute
\[
 (A^2+B^2+D^2+E^2-I^2-K^2+M^2)/2
                  =-EA-MB-MD-BD.
\]
Use (12), then (14). The terms containing \(H,J\) cancel, and
the result is precisely (17). The six numerator arguments become
the six variables in (14). The three denominator arguments become
the ones displayed in (16). This proves (16) from the literal source,
without a tetrahedral move identity or an assumed crossing formula.

## 4. General sectors, the actual paired-face image, and its inverse

The same calculation also transports the specified charge lift to
every sector \(\chi=(x,y,\zeta,w)\), with \(x+y+\zeta+w=1\).
Here \(\zeta\) is the third sector charge, distinguished from the
summation variable \(z\). Let \(\mathcal B_\chi\) denote the source
with the full table (8), and let \(\mathcal B_0\) denote (16).
Then
\[
 \mathcal B_\chi(\mathbf m,\mathbf p)
       =q^{D_\chi(\mathbf k,\mathbf h)}
                       \mathcal B_0(\mathbf m,\mathbf p),       \tag{17a}
\]
where
\[
\begin{split}
 D_\chi={}&(\zeta+w)k_1-y k_2+\zeta k_4+d_\chi,\\
 d_\chi={}&\zeta-2y+w/2
 -\tfrac32(\zeta+w)h_1+\tfrac32y h_2-\tfrac32\zeta h_4 .
\end{split}                                                     \tag{17b}
\]
This is an exact charge-gauge formula for the particular table (8).

To verify it, keep the variables (14) before translation. The two
changed numerator arguments are \(r+y,s+\zeta\). The first and
second denominator arguments acquire respectively \(y+\zeta\)
and \(\zeta\); the third is unchanged. Thus the bijection
\(r'=r+y,s'=s+\zeta\) restores exactly the canonical arguments.
Collecting the changed \(c(\gamma-\alpha)\) and \(ac/2\) terms in
(3), and subtracting the corresponding change in (17), leaves
(17b). More explicitly, the change from the \(c(\gamma-\alpha)\)
terms before translation is
\[
 yu+(y+\zeta)v+\zeta t
 +(\zeta+w)k_1-y k_2+\zeta k_4
 +\zeta-(\zeta+w)h_1+y h_2-\zeta h_4.
\]
The remaining constant from the \(ac/2\) terms is
\[
 \zeta+w/2-y-\tfrac12(\zeta+w)h_1
                     +\tfrac12y h_2-\tfrac12\zeta h_4.
\]
The change of the canonical phase under \(r,s\mapsto r+y,s+\zeta\)
is \(yu+(y+\zeta)v+\zeta t+\zeta+y\).
Subtracting it proves (17a),(17b), including every constant.

Equation (16) depends on the eight boundary indices only through
the four \(k_m\). Therefore simultaneous translation of \(m_m,p_m\)
leaves the actual tensor unchanged, independently for every leg.
Equations (17a),(17b) prove the same conclusion for all sectors.
This proves its membership in the fourfold diagonal-translation
invariant image in [A]. It is a property of the calculated source,
not merely of a proposed right-hand expression.

Put
\[
 f_m(k)=s_{0m}^{[k-1]}s_{m5}^{[-k]}.
\]
Let \(b_\chi(\mathbf k)\) denote (16) multiplied by (17a), extended
by zero off \(\sum k_m=2\). The inverse adapter yields the unique array
\[
 \mathcal R^\chi_{\mathbf i}
 =\frac1{s_{05}^{N-1}N^4}
   \sum_{\mathbf k\in(\mathbb Z/N\mathbb Z)^4}
     b_\chi(\mathbf k)\prod_{m=1}^4\frac{q^{-i_mk_m}}{f_m(k_m)}.
                                                               \tag{18}
\]
Finite Fourier inversion gives the exact all-boundary identity
\[
 \mathcal B_\chi(\mathbf m,\mathbf p)
 =s_{05}^{N-1}\sum_{\mathbf i}\mathcal R^\chi_{\mathbf i}
            \prod_{m=1}^4 q^{i_m k_m}f_m(k_m).          \tag{19}
\]
Equation (19) defines and recovers the array (18); it does not
identify it with the published \(R\).
All boundary rows must be transported by the inverse from [A],
rather than by a newly chosen Hermitian adjoint.

The support already proved implies
\[
 \mathcal R^\chi_{i_1+\ell,\ldots,i_4+\ell}
                        =q^{-2\ell}\mathcal R^\chi_{\mathbf i}. \tag{20}
\]
The literal planar definition [K, (2.8)] has the same covariance:
its four difference arguments are unchanged and its explicit phase
changes by \(q^{-2\ell}\). This is a verified consistency condition,
not a uniqueness statement.

The complete sector transport of the recovered array is also explicit:
\[
 \mathcal R^\chi_{\mathbf i}
  =q^{d_\chi}
   \mathcal R^0_{\,i_1-\zeta-w,\ i_2+y,\ i_3,\ i_4-\zeta}.
                                                               \tag{20a}
\]
For comparison, direct substitution in the *specified* planar
definition gives
\[
 R(i_1,i_2,i_3,i_4\mid x,y,\zeta,w)
 =q^{\zeta+w}
 R(i_1,i_2+1-x,i_3+\zeta+w,i_4+w\mid1,0,0,0).         \tag{20b}
\]
The four finite-product arguments agree term by term; the displayed
phase is the remaining explicit prefactor. Using (20), the shifts
in (20a),(20b) agree up to a common translation.
Thus a canonical identification, if proved with scalar \(C_N\),
would give scalar \(C_Nq^{d_\chi+\zeta+w}\) in this particular
charge lift. This records a calibration to check; it does not assume
the canonical identification or discard the root phase.

The construction is an equality of finite holomorphic functions
on the same lifted regular domain. Fixed-order decoration derivatives
retain (16)--(19), including the normalizations and inverse adapters.
No off-root quantum deformation or original meridian-normal
identification is implied.

## 5. The retained 1994/1995 charge phase and the open identity

There is a literal convention difference which matters before a
global comparison. In the operator convention of [B, (17)], take
the lower indices of the uncharged \(\mathcal R_{\alpha,\beta}^{\gamma,\delta}\)
as matrix rows. This is the convention in the action on the CG-index
vector. Expanding the first line of that formula gives
\[
 T^{94}_{\alpha,\beta}{}^{\gamma,\delta}
 =\rho_T q^{c(\gamma-\alpha)+\alpha\delta-ac/2+\alpha^2/2}
 W_T(\gamma-a-\alpha)\delta_{\beta,\gamma+\delta}.      \tag{21}
\]
Indeed \(Y^{-a}\) selects row \(\alpha+a\) with factor
\(q^{-a\alpha-a^2/2}\), while the left \(Z^{-c}\) contributes
\(q^{-c(\alpha+a)}\). The right clocks contribute
\(q^{c\gamma-a\delta}\); the uncharged kernel contributes
\(q^{(\alpha+a)\delta+(\alpha+a)^2/2}\).
Together with \(q^{ac/2}\) these give (21).
Thus the explicit 1995 definition (3) obeys
\[
 T^{95}(a,c)=q^{ac}T^{94}(a,c),\qquad
 \bar T^{95}(a,c)=q^{-ac}\bar T^{94}(a,c).              \tag{22}
\]
The second equality follows by the same inverse/conjugate-index
calculation; its phase is inverse. Complementary-charge inverse
and bubble pairs in [B] consequently retain their exact scalar.

For the canonical charge lift (8),(10), the signed sum of \(ac\)
over the nine cells is \(h_1-1\). Therefore
\[
                 \mathcal B^{95}=q^{h_1-1}\mathcal B^{94}.        \tag{23}
\]
In particular the symmetric boundary choice \(h_m=1/2\), which
satisfies both \(\sum h_m=2\) and complementary wire charges,
has the recorded factor \(q^{-1/2}\). This factor is not suppressed.

The remaining crossing equation is the evaluation of (18) as the
specified planar tensor [K, (2.8)], with the precise chosen charge
gauge and root phase. Neither the shared covariance (20), the
existence of the inverse boundary adapter, nor the nonzero factors
in (15) proves that evaluation. It requires an additional finite
sum identity or a sufficient set of actual boundary intertwining
relations with their support and initialization proved.
This note does not assert pointwise nonvanishing of the recovered
array, invertibility, triangular support, or equality to a quantum-group
crossing. It makes no selected geometric-period or large-\(N\)
asymptotic claim.

## 6. A complete normalization test at every allowed level

Fix any odd \(N>2\). Take the admissible canonical data
\[
 (x,y,\zeta,w)=(1,0,0,0),\qquad
 \mathbf h=(1,0,0,1),\qquad
 \mathbf p=(0,0,0,0),\qquad
 \mathbf m=(0,1,0,-1).
                                                               \tag{24}
\]
Thus \(\mathbf k=(1,1,0,0)\), and all boundary constraints hold.
Let the real vertex decorations be
\[
 z_i=L^{5-i}\quad(0\le i\le5),\qquad L>1,\qquad L\longrightarrow\infty .
                                                               \tag{25}
\]
Choose every \(s_{ij}\) positive, and choose the normalization square
roots in [B] positive on this ordered real domain. All the data are
regular for every \(L>1\). This is a limit with \(N\) fixed; no
uniformity in \(N\) is asserted.

For each sorted tetrahedron put
\(\varepsilon_T=Y_T/Z_T\) and \(\xi_T=X_T/Z_T\).
Both are positive, \(\varepsilon_T\to0\), and
\(\xi_T=(1-\varepsilon_T^N)^{1/N}\to1\). Put
\[
 p_n=\prod_{j=1}^n(1-q^j),\qquad p_0=1.
 \]
For \(1\le n<N\), the literal finite products (1) give
\[
 W_T(n)\sim\frac{\varepsilon_T^n}{p_n},\qquad
 \overline W_T(n)^{-1}
       \sim\frac{\varepsilon_T^{N-n}}{N}\,p_{n-1}.      \tag{26}
\]
For the second formula, separate its \(j=0\) factor:
\[
 \overline W_T(n)^{-1}
 =\varepsilon_T^{-n}(1-\xi_T)
                       \prod_{j=1}^{n-1}(1-\xi_Tq^j),\qquad
 1-\xi_T=\frac{\varepsilon_T^N}
                         {1+\xi_T+\cdots+\xi_T^{N-1}}.
\]
Both functions at \(n=0\) are exactly one. Thus both \(W_T\) and
\(\overline W_T^{-1}\) converge to the zero-index delta, and no
summand in (16) diverges.

At the data (24), only \(u=v=t=r=s=z=0\) survives in the finite
six-variable sum. Its three denominator arguments are zero and
its phase (17) is \(q\). Consequently
\[
                         \mathcal B/\mathfrak n\longrightarrow q.
                                                               \tag{27}
\]
This step includes all finite endpoint residues.

We also compute the full normalization, rather than discarding it.
Put \(\Lambda_i=z_i^{1/N}\). For \(T=abcd\) with \(a<b<c<d\),
the six roots in (2) satisfy
\[
 P\sim B\sim H\sim\Lambda_a,\qquad
 Q\sim C\sim\Lambda_b,\qquad R\sim\Lambda_c.
\]
The exact scalar formula in [B] therefore gives
\[
 \kappa_*^2=
 \frac{B^NQ^N(H-C)}
      {N^2(B-Q)(H-R)(C-R)}
 \sim\frac{(\Lambda_a\Lambda_b)^{N-1}}{N^2}.
                                                               \tag{28}
\]
The two finite sums defining \(\rho_T,\bar\rho_T\) both have
arguments tending to \((0,0\mid1)\). Every summand tends to one,
so each sum tends to \(N\). With the specified positive square roots,
\[
 \rho_T\sim\bar\rho_T
                \sim(\Lambda_a\Lambda_b)^{(N-1)/2}.    \tag{29}
\]
These formulas use the actual three-numerator/one-denominator
square-root prefactor, not a norm estimate.

In the nine cells the first two vertex labels have total multiplicities
\((6,6,4,2)\) at vertices \(0,1,2,3\), respectively.
Thus their scalar product contributes
\(\Lambda_0^{3d}\Lambda_1^{3d}\Lambda_2^{2d}\Lambda_3^d\),
where \(d=N-1\). The four edge weights (7) contribute
\(\Lambda_1^{-2d}\Lambda_2^{-d}\Lambda_3^{-d}\).
Writing
\[
 \mathfrak D=(s_{05}s_{15}s_{25}s_{03}s_{04})^d,
\]
we conclude
\[
 \mathfrak n\sim\Lambda_0^{3d}\Lambda_1^d\Lambda_2^d
                  \sim\mathfrak D,\qquad
                       \frac{\mathcal B}{\mathfrak D}\longrightarrow q.
                                                               \tag{30}
\]

The coefficient of the proposed planar expression can be calculated
independently from [K, (2.7),(2.8)]. Let
\(\bar p_n=\prod_{j=1}^n(1-q^{-j})\) and define
\[
 S_n(X)=\sum_{j=0}^n\frac{X^j}{p_j\bar p_{n-j}}\qquad(0\le n<N).
 \]
Direct coefficient comparison, including both endpoints, proves
\[
 (1-q^n)S_n(X)=(X-q^n)S_{n-1}(X),\qquad S_0=1.
\]
At coefficient \(X^j\), the two terms in the numerator are
\((1-q^j)-q^n(1-q^{-(n-j)})=1-q^n\).
Induction gives the exact finite formula
\[
                 S_n(X)=\frac{\prod_{j=1}^n(X-q^j)}{p_n}.        \tag{31}
\]
No binomial summation theorem is assumed.

Consider the Fourier coefficient
\[
 \Phi_N=\sum_{i,j,k,l}
             R(i,j,k,l\mid1,0,0,0)\,q^{i+j}.          \tag{32}
\]
For every supported term of the specified planar weight set
\[
 u=[j-i-1],\quad v=[i-l],\quad t=[l-k],\quad h=[k-j].
\]
The two theta factors say \(u+t<N\) and \(v+h<N\).
Their total is congruent to \(N-1\) and at most \(2N-2\);
hence \(u+v+t+h=d\) as an ordinary integer.
Conversely every such composition and one free \(j\) give one
term, with
\[
 i=j-1-u,\qquad k=j+h,\qquad l=j+h+t \pmod N.
\]
Substitution in the literal weight, including its prefactor \(N\),
gives after multiplication by \(q^{i+j}\) the phase
\[
 q^{-(t+h)-(t+h+1)(u+h)}
\]
and denominator \(p_u\bar p_v p_t\bar p_h\).
The free \(j\)-sum therefore supplies a second factor \(N\).
Set \(m=t+h\) and \(X=q^{-m-1}\). Equation (32) becomes exactly
\[
 \Phi_N=N^2\sum_{m=0}^{d}
       q^{-m}X^m S_{d-m}(X)S_m(X^{-1}).               \tag{33}
\]
For \(m<d\), \(X=q^{d-m}\) is a root of the first polynomial
in (31). For \(m=d\), \(X=1\), \(S_d(1)=1\), and \(q^{-d}=q\).
Thus
\[
                              \Phi_N=N^2q.           \tag{34}
\]

At the boundary data (24), the four functions in [A] are
\[
 f_1(1)=s_{15}^d,\quad f_2(1)=s_{25}^d,\quad
 f_3(0)=s_{03}^d,\quad f_4(0)=s_{04}^d.
\]
Hence the right-hand crossing expression in [K, (4.25)], with
unit coefficient and the specified planar \(R\), is exactly
\(\mathfrak D\,N^2q\). Combining (30),(34) proves
\[
 \frac{\text{nine-cell tensor from (2),(3),(7)}}
 {\text{unit-coefficient planar crossing expression}}
                       \longrightarrow \frac1{N^2}.             \tag{35}
\]
There is no charged-convention phase in this test: \(h_1=1\)
also makes (23) equal to one.

Therefore the specified 1995 kernels together with the explicit
1994 scalar normalizations (2) cannot give the unit-coefficient
crossing expression on the whole regular decoration domain.
This is a normalization obstruction for that precise combination
of definitions. The 1995 reference to earlier scalar functions
does not itself specify every possible conversion; an unstated
conversion must be made explicit and verified. No global theorem
of either paper is refuted here.

Equation (35) does not prove
\(\mathcal R^\chi=N^{-2}R(\,\cdot\mid\chi)\) globally.
It fixes a necessary scalar in the phase-free canonical test if
an independently proved, decoration-independent scalar comparison
exists. It also proves that the calculated tensor is not identically
zero: for each fixed allowed \(N\) this boundary entry is nonzero
for sufficiently large \(L\). No all-decoration nonvanishing,
triangular support, or selected geometric coefficient follows.
The size \(N^{-2}\) is subexponential in \(N\), but that observation
does not supply the missing array or global source comparison.

## Complete direct sources

- [K] R. M. Kashaev, *A Link Invariant from Quantum Dilogarithm*,
  [q-alg/9504020v1](https://arxiv.org/pdf/q-alg/9504020).
  Complete primary text read; only its finite definitions and
  specified incidence/charge/weight data are used. Local PDF:
  research_archive/finite-source-identification-2026-11-01/md-kashaev-normalization-critical-audit/kashaev1995.pdf,
  SHA256 0baef40fa9934c9119af2c67252f8032e288c884da72eeaecf405bf91569cda9.
- [B] [Literal charged tetrahedron bubble](research_literal_charged_tetrahedron_bubble.md),
  SHA256 1dfe35f26137572235b1c3af66dcf410e0af758836baddaa8dd6d958c0f61d9b.
- [A] [Paired-face boundary adapter](research_kashaev_paired_face_boundary_adapter.md),
  SHA256 c430fd2714acdc7588003e1c18c60453e1ebe123bd7c0155d20a0eef639ec8ed.

The three complete direct texts were read and their used implications
checked. No mathematical program, numerical experiment, published
nine-tet contraction, or published global state-invariance theorem
was used.
