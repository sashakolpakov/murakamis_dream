# The actual reduced braid network and its resolved critical scheme

Private written proof, 18 November 2026.

The exact constant-prefix quotient has a finite Euler network.
Its regular exponentiated generating correspondence is the
Hamiltonian reduction of the original braid correspondence at
total lowering coordinate zero. The central first head on that
level retains its eigenflag. Discarding that flag would give a
different reduction.

For a regular semisimple total product, a fixed point of the
reduced correspondence lifts to an actual braid fixed point:
there is no additional upper-unipotent closing seam. Under the
positive complete gluing certificate specified below, the
geometric fixed germ, after the common momentum quotient, is a
reduced point. For complete discrete faithful holonomy, the
needed resolved charts exist after the source-preserving
presentation changes in R.

These are statements about the actual finite coefficients and
their principal rational correspondence. A uniform Fourier
integral description on the first-head vacuum, a nonvanishing
local amplitude there, and an original-cycle coefficient are
not asserted. The three complete proof directs are R, M and H,
pinned at the end.

## 1. The finite reduced source and the Euler factors

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\(x=-M/q\). The quantum parameter is fixed at this root while
the common meridian \(M\) varies. Put
\[
 f_a=\prod_{\ell=1}^a(1-Q^\ell),\qquad f_0=1,\qquad
 Lw_a=w_{a-1}\ (a>0),\quad Lw_0=0.
 \tag{1}
\]
The actual \(F\) raises occupation with coefficient
\(1-Q^{a+1}\), except that its top arrow is zero.

For \(m\) original heads, R proves the exact algebra map
\[
 \mathcal B_m(W)=p_0S_m^{-1}Wi_0,\qquad
 S_m=\sum_{n=0}^{d}\frac{(x^{-1}L_1F_{\rm r})^n}{f_n}.
 \tag{2}
\]
It retains the original pointed and pivotal source through R's
explicit meromorphic Cartan kernel and its removable meridian
limit. On braid generators its values are
\[
 \mathcal B_m(R_i)=R_{i-1}\quad(i\ge2),\qquad
 \mathcal B_m(R_1)=\kappa S_{m-1}D,
 \quad
 Dw_a=(-1)^aQ^{a(a-1)/2}x^{-2a}w_a .
 \tag{3}
\]
The negative generators are the exact inverses. The \(R_i\)
and \(\kappa\) in this equation have their original Cartan,
flip and scalar conventions. Every external framing line and
the first-meridian-jet source functional remain those of R.

Here is a finite local factorization of the new operator.
On \(r\) heads, write
\[
 F_{\rm tail}=\sum_{j=2}^rK_2^{-1}\cdots K_{j-1}^{-1}F_j,
 \qquad
 Z_j=x^{-1}L_1K_2^{-1}\cdots K_{j-1}^{-1}F_j .
 \tag{4}
\]
For \(i<j\), the literal weight relations give
\(Z_iZ_j=Q^{-1}Z_jZ_i\). The finite product identity is
\[
 S_r=\prod_{j=2}^r e_Q(Z_j),\qquad
 e_Q(Z)=\sum_{n=0}^{d}\frac{Z^n}{f_n},
 \tag{5}
\]
with increasing \(j\) from left to right. To prove (5), expand
the power of the sum in (4), moving the \(Z_i\)'s into this
order. The recursion for the resulting coefficients is the
finite Gaussian-binomial recursion; its coefficient of
\(Z_2^{n_2}\cdots Z_r^{n_r}\) is
\(f_{\sum n_j}/\prod f_{n_j}\). All terms of total degree
\(\ge N\) vanish because of the common \(L_1\). Thus only the
nonzero denominators \(f_n\), \(n<N\), occur. This also proves
the identity at even or composite levels.

More explicitly, the entry from \((a,b_2,\ldots,b_r)\) to
\((a-n,b_2+n_2,\ldots,b_r+n_r)\), \(n=\sum n_j\), is
\[
 \prod_{j=2}^r
 x^{-(j-1)n_j}Q^{\,n_j\sum_{2\le i<j}b_i}
       \frac{f_{b_j+n_j}}{f_{b_j}f_{n_j}},
 \quad
 n_j\ge0,\quad n\le a,\quad b_j+n_j\le d .
 \tag{6}
\]
The rightmost factor in (5) acts first, which explains the
unshifted earlier \(b_i\)'s in its phase. The entry of
\(S_r^{-1}\) has the same expression multiplied by
\((-1)^nQ^{n(n-1)/2}\). Indeed this is the inverse coefficient
in degree \(n\) of the finite series in the sum (4).
Outside the displayed support both entries are zero.
In particular \(S_ri_0=i_0\). None of these identities replaces
the physical finite projectors by a cyclic or infinite series.

## 2. The generating correspondence derived from (6)

In this and subsequent classical equations write \(x=-M\)
for the principal value. Use the factorial coordinates
\[
 K_j=x/A_j,\qquad
 e_j=(M/A_j-M^{-1})p_j,\qquad
 f_j=(1-A_j)/p_j .
 \tag{7}
\]
They are precisely M's coordinates, including the selected
inverse-meridian eigenflag. On a unit logarithmic chart put
\(b_j=\Log A_j\), \(c_j=\Log C_j\). The principal expression
read from (6) is
\[
 \mathcal S_S=\sum_{j=2}^r\left[
 -(j-1)\Log x\,c_j+c_j\sum_{2\le i<j}b_i
 +\operatorname{Li}_2(A_j)+\operatorname{Li}_2(C_j)
 -\operatorname{Li}_2(A_jC_j)-\operatorname{Li}_2(1)
 \right].
 \tag{8}
\]
Its input positions are \(A_1,A_2,\ldots,A_r\) and its output
positions are \(A_1/\prod C_j,A_2C_2,\ldots,A_rC_r\).
For the inverse entry add
\(\pi i\sum c_j+\tfrac12(\sum c_j)^2\), on the sheet of the
actual sign. The exact half powers, \(\kappa\), and the
quantum-to-principal \(x\) shift remain in (3) and (6).
No marked primitive constant is discarded by these statements.

The convention is
\(d\mathcal S=\sum_{\rm out}\log p'\,d\log A'
 -\sum_{\rm in}\log p\,d\log A\).
Differentiating (8), including all monomials, gives
\[
 p_1'=p_1,\qquad
 \frac{p_j'}{p_j}
  =\left(\prod_{\ell>j}C_\ell\right)
       \frac{1-A_jC_j}{1-A_j},
 \qquad
 \frac{p_j'}{p_1}
  =x^{-(j-1)}\left(\prod_{2\le i<j}A_i\right)
       \frac{1-A_jC_j}{1-C_j}.
 \tag{9}
\]
Thus these are equations of the literal coefficient graph,
not an assumed symbol of the whole triangular matrix.

Put
\[
 u=p_1/x,\quad
 z_j=uK_2^{-1}\cdots K_{j-1}^{-1}f_j,\quad
 T_j=1-\sum_{\ell\ge j}z_\ell,\quad T_{r+1}=1,\quad C=T_2 .
 \tag{10}
\]
Eliminating the momenta in (9) gives, successively from the
last recipient,
\[
 C_j=T_j/T_{j+1},\quad
 A_1'=A_1/C,\quad p_1'=p_1,\qquad
 K_j'=K_jT_{j+1}/T_j,\quad f_j'=f_j/T_{j+1}.
 \tag{11}
\]
Equivalently,
\(p_j'=p_j(T_{j+1}-A_jT_j)/(1-A_j)\).
All identities first hold where the factors used in (9) are
units; their rational forms (10)--(11) specify their extension.
The total recipient \(F\) and \(p_1\) are unchanged. The inverse
entry's additional derivative therefore gives the inverse
recipient conjugator \(g^{-1}\) in (13), with the donor
\(A_1\) multiplied by \(C\); substitution checks the inverse
of (11). For \(D\) in (3) the map is
\[
               A_1'=A_1,\qquad p_1'=-A_1p_1/x^2 .
 \tag{12}
\]
This includes the actual sign in \(D\).

For later use there is a matrix form of (11). Form the dressed
meridians of the recipient tuple by M's lower Gauss prefixes,
and let \(P_j\) be its product through recipient \(j\). Then
\[
 P_j'=gP_jg^{-1},\qquad
 g=\begin{pmatrix}C&u\\0&1\end{pmatrix}.
 \tag{13}
\]
Here is a direct verification, without a whole-matrix
semiclassical assertion. For a recipient prefix write its
ordered totals as \(K,F,E\), so
\[
 P=\begin{pmatrix}K&E\\KF&K^{-1}+EF\end{pmatrix}.
 \tag{14}
\]
The sum of its terms in (10) is \(uF\), hence
\(T=C+uF\). Equation (11) telescopes to
\[
 K'=KT/C,\quad F'=F/T,\quad
 E'=TE+u/K-uKT/C .
 \tag{15}
\]
The last equality follows by substitution in (7) for one
recipient and induction using
\(E_{\le j}=K_jE_{\le j-1}+e_j\) and
\(F_{\le j}=F_{\le j-1}+K_{\le j-1}^{-1}f_j\).
These are the entries of \(gPg^{-1}\), proving (13).
The ratios of consecutive prefixes give the same conjugation
for each dressed meridian.

## 3. The first-head flag at total lowering zero

At completeness \(M=1,x=-1\), use the resolved first-head chart
\[
 A_1=1+p_1t,\qquad
 K_1=-(1+p_1t)^{-1},\quad
 f_1=-t,\quad e_1=-p_1^2t/(1+p_1t).
 \tag{16}
\]
The selected eigenline is \([p_1:1]\). This chart remains
regular at \(p_1=0\), and
\[
 d\log A_1\wedge d\log p_1
                     =\frac{dt\wedge dp_1}{1+p_1t}.
 \tag{17}
\]
At \(t=0\) its meridian matrix is central, but its selected
flag is still present. In particular the equation
\(A_1-1=0\), by itself, would add the component \(p_1=0\);
the resolved lowering-zero equation is \(t=0\).
The actual first-head vacuum selects the zero logarithm
of \(A_1=1\). Other integer logarithmic sheets are not
identified with that physical endpoint by this equation.

Write \(F_{\rm r},K_{\rm r},E_{\rm r}\) for the new remaining
totals and \(C=1-p_1F_{\rm r}/x\). Applying the map (11) from
new to original variables gives
\[
 K_{1,\rm old}=\frac{xC}{1+p_1t},\qquad
 f_{1,\rm old}=-\frac{t+F_{\rm r}/x}{C}.
 \tag{18}
\]
Its original total lowering coordinate is exactly \(-t\):
substitute (11) in
\(F_\Sigma=f_{1,\rm old}+K_{1,\rm old}^{-1}F_{\rm r,old}\).
Thus the chart implements \(F_\Sigma=0\) as \(t=0\).
All \(K\)'s, \(C\) and the recipient \(T_j\)'s are required
to be units. A recipient with \(A_j=1,p_j=0\) is represented
by its own version of (16); when \(f_j\) is a unit, (11)
extends in its regular \((K_j,f_j)\) chart.

The entire framing motion on this level can be checked
explicitly. At the section \(p_1=0,t=0\), set
\[
 H_1^0=\begin{pmatrix}x&0\\-F_{\rm r}&x^{-1}\end{pmatrix},
 \qquad
 h_0=\begin{pmatrix}1&0\\-F_{\rm r}/x&1/x\end{pmatrix}.
 \tag{19}
\]
If \(H_j^{\rm r}\) are the dressed remaining meridians, then
the original ones are
\(H_{j+1}^0=h_0H_j^{\rm r}h_0^{-1}\).
For arbitrary \(p_1\) on the level, all original meridians are
\[
 H_i(p_1)=U(p_1)H_i^0U(p_1)^{-1},\qquad
 U(p)=\begin{pmatrix}1&p\\0&1\end{pmatrix}.
 \tag{20}
\]
Indeed the product of the original first lower-Gauss inverse
and (13) is
\[
 b_{-,1}^{-1}g
  =\begin{pmatrix}C&p_1/x\\-F_{\rm r}/x&1/x\end{pmatrix}
  =U(p_1)h_0 ,
 \tag{21}
\]
and direct conjugation verifies the first meridian as well.
Consequently, on \(F_\Sigma=0\),
\[
 K_\Sigma=xK_{\rm r},\qquad
 E_\Sigma=E_{\rm r}+p_1(K_\Sigma^{-1}-K_\Sigma).
 \tag{22}
\]
The Hamiltonian lowering flow is this upper-unipotent motion,
up to the choice of Poisson sign in (17). Its quotient is
therefore the remaining tuple. This statement retains the
flag coordinate; it is not a coadjoint-orbit calculation at
a central point with the flag forgotten.

## 4. The reduced boundary generator is the actual quotient map

We verify the nontrivial generator with arbitrary tails.
Use the section in (19), and let the first remaining physical
head have \(K_2,e_2,f_2,p_2\). Write \(F_T\) for the total
lowering coordinate on all later heads. Thus
\(F_{\rm r}=f_2+K_2^{-1}F_T\).
The original first head has
\(K_1=x,e_1=0,f_1=-F_{\rm r}/x\).
M's positive crossing equations have \(1-e_1f_2=1\) and give
\[
 \begin{split}
 &K_{1,R}=K_2,\quad K_{2,R}=x,\quad
 e_{1,R}=e_2/x,\quad e_{2,R}=0,\\
 &f_{1,R}=xf_2,\qquad
 f_{2,R}=f_R=-xK_2f_2-F_T/x .
 \end{split}
 \tag{23}
\]
Undoing the first-head map (11) uses
\[
 p_{1,\rm new}=p_2/x,\qquad
 g_m=\begin{pmatrix}K_2/x&p_2/x^2\\0&1\end{pmatrix}.
 \tag{24}
\]
The resulting first remaining coordinates are
\[
 K_{2,\rm new}=K_2+p_2F_T/x^2,\qquad
 p_{2,\rm new}=-p_2/(xK_2).
 \tag{25}
\]
They are exactly (12), followed by \(S_{m-1}\): after \(D\)
the donor momentum is \(p_D=-p_2/(xK_2)\), and its new
\(C_T=1-p_DF_T/x\) is \(K_{2,\rm new}/K_2\).

This also checks every later meridian, not just the first
remaining head. Define
\[
 g_T=\begin{pmatrix}C_T&-p_2/(x^2K_2)\\0&1\end{pmatrix},
 \quad
 b_{-,2,\rm new}=
   \begin{pmatrix}1&0\\-K_2f_R&K_{2,\rm new}\end{pmatrix},
 \quad
 b_{-,2,R}=\begin{pmatrix}1&0\\-xf_R&x\end{pmatrix}.
 \tag{26}
\]
The exact identity
\[
 g_T^{-1}b_{-,2,\rm new}
 =b_{-,2,R}g_m
 =\begin{pmatrix}K_2/x&p_2/x^2\\-K_2f_R&K_{2,\rm new}\end{pmatrix}
 \tag{27}
\]
identifies their lower-Gauss conjugations. It proves equality
of the full quotient maps for arbitrary later heads.
For \(i\ge2\), the physical crossing preserves the ordered
remaining \(K,F,E\), so its map commutes with the first-head
construction; its quotient is the physical \(R_{i-1}\).
Inverse generators follow by inversion. Equations
(23)--(27) initially use units and then extend on the resolved
charts of Section 3 as rational identities with unit
denominators.

We have thus proved the correspondence directly from the
finite reduced coefficients (3), (6): their regular canonical
graph is the quotient of \(R_\beta\) on the original
\(F_\Sigma=0\) by (20), equivalently the quotient of
\(S_m^{-1}R_\beta S_m\) on the new level \(t=0\).
No asymptotic action of the whole
matrix \(S_m\) on its physical vacuum was used.

## 5. Fixed schemes and the single common momentum

Assume \(K_\Sigma^2\ne1\) on this level. A reduced fixed point
lifts to an equation
\[
                         R_\beta(z)=U(s)\cdot z .
 \tag{28}
\]
The original braid preserves the exact ordered total \(E\)
and \(K\). Equations (20)--(22) consequently imply
\[
                      s(K_\Sigma^{-1}-K_\Sigma)=0.
 \tag{29}
\]
The second factor is a unit, so \(s=0\). Conversely any
original fixed point on this level gives a reduced fixed
point. The same calculation works over every local Artin
algebra. Thus the reduced fixed scheme is precisely the
original fixed scheme on \(F_\Sigma=0\), divided by the
upper-unipotent action. It has no additional closing seam.

For clarity, passing to independent occupation variables
removes one further, specified common momentum. Regard an
\(S_r\) factor as a vertex with \(r\) inputs and \(r\) outputs.
Its positions have the sole linear conservation equation;
inputs and \(r-1\) transfers give its \(2r-1\) coordinates.
Equations (9) recover all its momentum ratios. The physical
crossings have the same property by M; a \(D\) vertex has
one incoming and one outgoing wire and (12).

The resulting closed network is connected for a braid whose
closure is a knot. For \(m>2\), the word must use \(R_1\) or
its inverse, since otherwise its first strand closes as a
separate component. Its \(S_{m-1}\) vertex joins all remaining
heads. For \(m=2\) there is one remaining wire. Identity
pieces may be omitted. The conservation matrix \(L\) of
this network therefore has rank one less than the number
of vertices.

On the vector space of conserved wire positions, the same
linear argument as H gives
\[
 0\longrightarrow\mathbb C\longrightarrow\mathbb C^{V}
 \mathop{\longrightarrow}^{L^t}\mathbb C^{E}
 \longrightarrow(\ker L)^*\longrightarrow0.
 \tag{30}
\]
The differential of the sum of the actual local primitives
is the list of momentum mismatches restricted to \(\ker L\).
Vertex constants can remove that list exactly when the
derivative vanishes; their only ambiguity is one global
constant. A spanning tree supplies a fixed right inverse,
so this is an equality of local schemes, not just tangents.
The Fourier integer covector is extended from chord edges
and assigned to incident local primitives, as in H. This
retains its additive derivative while changing no
exponentiated graph. Original pivotal turns are treated
in the same fashion.

Thus, on a regular logarithmic coefficient chart, the
actual occupation gradient scheme is the reduced fixed
scheme divided by the single common momentum
\(p_j\mapsto\lambda p_j\). On a resolved boundary chart the
preceding rational fixed-scheme assertion still makes
sense; (30) does not assert that a singular logarithmic
primitive has become holomorphic or that a hard projector
has disappeared.

## 6. The geometric resolved chart and its local rigidity

R permits at most three source-preserving positive
stabilizations and an actual braid conjugation so that
the complete total product \(P\) is regular semisimple.
Suppose first the holonomy is complete, discrete and
faithful. In a torsion-free discrete group a nonparabolic
noncentral semisimple element is loxodromic: a finite-order
elliptic would be torsion, and the powers of an infinite-order
elliptic accumulate at the identity. A loxodromic element
cannot share a fixed point with a nontrivial parabolic
element. In coordinates putting that point at infinity,
conjugating the nontrivial translation by appropriate
powers of the loxodromic multiplier produces distinct
elements converging to the identity. This contradicts
discreteness.

Choose an eigenline \(v\) of \(P\) and the selected
eigenline \(w\) of the first meridian. They are distinct.
In the basis \((v,w)\), the total \(P\) is upper triangular
and the first meridian has the form (19), with
\(F_{\rm r}\ne0\). Every stage prefix \(P_j\) has nonzero
upper-left entry. Otherwise \(P_jv\) would be proportional
to \(w\), making \(v\) the fixed point of a conjugate of
the first parabolic meridian, which was just excluded.
Likewise a physical \(f_j=0\) would make \(v\) an eigenline
of \(P_{j-1}^{-1}H_jP_{j-1}\), again a conjugate meridian.
This proof applies to every prefix in the finite braid
and to each reselected first-meridian flag used in (19).

At the section (19), the full prefixes satisfy
\[
                P_j^{\rm full}
                  =h_0P_{j-1}^{\rm r}\operatorname{diag}(x,1).
 \tag{31}
\]
In particular their \((1,1)\) entries are \(x\) times
those of the remaining prefixes. The new remaining
physical heads are exactly the old heads numbered
\(2,\ldots,m\) on this section. All their \(K\)'s and
\(f\)'s are therefore units at every quotient stage.
For an \(S_{m-1}\) generator the input and output \(K\)'s
in (11) are units. Starting at \(T_{r+1}=1\) shows
successively that all its \(T_j\)'s are units. Its
recipients have unit \(f_j\). The donor may have
\(p_j=0,A_j=1\); its chart is then (16), with \(t_j=-f_j\)
retained. This proves existence of a regular resolved
correspondence chart at the geometric point.

It does not prove that every new three-factorial shape
in (8) avoids one. In particular repeated parabolic
flags can force zero transfers. Such points remain
resolved correspondence points, not automatically
ordinary nonzero-factorial amplitude charts.

Now additionally supply the actual exterior's positive
complete gluing certificate in H. Its exact selected
meridian-eigenvalue theorem makes the unframed geometric
representation germ a reduced point. Before quotienting
frames, the germ is therefore a smooth conjugation orbit
of dimension three. Its projective stabilizer is trivial:
a lift of a projective centralizer must conjugate each
lifted meridian to itself or its negative; the nonzero
parabolic trace excludes the negative. It then centralizes
all generators and is scalar by irreducibility, as in H.
The exact eigenflag is retained, as
in (16), including over Artin rings.

The equation \(P_{21}=0\), equivalently \(F_\Sigma=0\),
is transverse to that orbit when \(P\) is regular
semisimple: infinitesimal lower-unipotent conjugation
changes \(P_{21}\) by a nonzero multiple of
\(K_\Sigma-K_\Sigma^{-1}\). It leaves a smooth
two-dimensional germ. Quotienting the free upper
unipotent action (20) leaves the diagonal framing
direction, and the common momentum in (30) is exactly
that diagonal conjugation. This action is free locally:
if every remaining \(p_j\) were zero, their unit \(f_j\)
would give every \(A_j=1\) and hence \(K_\Sigma^2=1\),
contrary to the stated unit condition. Consequently the geometric
resolved reduced fixed germ modulo the common momentum
is a reduced point, on each choice of the eigenline \(v\).
There are two discrete eigenline choices, not an
additional continuous gauge.

Whenever an actual regular logarithmic generating chart
represents this point, (30) identifies its gradient
scheme with that reduced point. Its Hessian is therefore
invertible: the kernel is the Zariski tangent of the
gradient scheme. This last holomorphic-phase statement
requires that chart; the resolved rational result does
not manufacture it at singular factorial/projector
faces.

## 7. Source and action scope

All finite support inequalities in (6), the actual
negative coefficients, the prescribed pivots, framing
scalars and meridian derivatives remain in (2)--(3).
The proof does not differentiate the root reduction
as an off-root quantum-normal identity. Such normals
retain the prefix carry from R's complete sources.

The original scalar source is still the specified
Cartan-weighted first-meridian-jet functional of the
finite reduced network. The geometric correspondence
does not estimate that matrix or its spectral radii.
In particular a physical-basis reduced matrix norm
is not identified with representation volume.

Equation (8) records the literal principal primitive,
its three-factorial part, and the inverse's marked
quadratic term. Equality of the rational canonical
maps proves no equality of marked primitive constants.
No reduced regulator/volume calibration is claimed
here. Nor does a reduced isolated geometric germ
determine a nonzero local amplitude, a thimble
coefficient, or the original relative period.

## Complete proof-source pins

* R: notes/research_actual_reduced_braid_source.md,
  SHA256 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* M: notes/marked_braid_holonomy.md,
  SHA256 eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.
* H: notes/research_positive_certificate_braid_morse_bott.md,
  SHA256 6ef5423e542170ffe3b5464753613ae042341d9c2ee20a2fa94fd0d828738410.

All three complete sources were freshly read nontruncated in
this author sequence, and every used implication was checked.
The finite Euler, resolved-flag, generator and quotient
calculations above are written proofs. No mathematical programs
were run. Frozen and public files were not edited.
