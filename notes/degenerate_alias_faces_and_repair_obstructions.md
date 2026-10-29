# Degenerate alias faces: a general bound and two exact obstructions

Research note, 28 October 2026.

This note concerns the remaining **classical wrong-edge faces** of
`general_legendre_rivin_contour.md`. It proves a uniform bound for a
combinatorially specified class of triangulations. Two tempting routes to
an unconditional bound fail on actual positive knot triangulations:
repairing only the flat tetrahedra, and giving the complete edge
multipliers an automatic favorable sign.

Neither counterexample disproves volume domination. Neither the bound nor
the counterexamples identify an original quantum wall with a classical
face. That source comparison remains necessary.

The reproducible exact/Arb audit is
`experiments/audit_degenerate_alias_faces.py`, with fixture
`experiments/degenerate_alias_face_fixture.json` and results
`experiments/degenerate_alias_face_results.json`.

## 1. A uniform star bound for all wrong-edge faces

Let an ideal triangulation of a one-cusped knot exterior have (t)
tetrahedra and (t) global edges. Let (E) be its nonnegative edge-angle
incidence matrix. Its three columns per tetrahedron count the two
opposite local edges, so every column sums to two. Consider a weak nonnegative
alias angle locus

\[
 \alpha_{ja}\geq0,\qquad \sum_{a=0}^2\alpha_{ja}=\pi,
 \qquad E\alpha=2\pi k,\qquad k\in\mathbb Z_{\geq0}^t.
 \tag{1}
\]

Summing all edge equations gives \(\sum_e k_e=t\). Consequently, if the
edge winding differs from the original vector \(\mathbf1\), at least one
edge has (k_e=0). All angle summands incident to that edge are then zero.
Every tetrahedron meeting it has at least one zero angle, and its
continuous volume

\[
 V_j=\Lambda(\alpha_{j0})+\Lambda(\alpha_{j1})
       +\Lambda(\alpha_{j2})
\]

is zero: \(\Lambda(0)=0\) and
\(\Lambda(\pi-a)=-\Lambda(a)\).

Write (s_e) for the number of **distinct tetrahedra** incident to edge
(e), and (v_3) for the volume of the regular ideal tetrahedron. Since
every other tetrahedron has volume at most (v_3),

\[
 \boxed{\quad V(\alpha)\leq(t-s_e)v_3
   \quad\text{whenever }k_e=0.\quad}                 \tag{2}
\]

In particular, put \(s_{\min}=\min_e s_e\). If a positive complete
triangulation satisfies

\[
 \boxed{\quad\operatorname{Vol}(M)>(t-s_{\min})v_3,\quad} \tag{3}
\]

**every wrong-edge weak nonnegative alias locus has a common strict volume gap**

\[
 \operatorname{Vol}(M)-V(\alpha)
 \geq\operatorname{Vol}(M)-(t-s_{\min})v_3>0.        \tag{4}
\]

This is a bound on the whole cell, including all its corners, with no
stationarity or repair assumption. For several zero edges, replace
(s_e) by the size of the union of their tetrahedron stars. Linear
constraint propagation can force still more tetrahedra to be flat.

The bound applies to an actual face integral once that integral has the
specified phase, a uniform subexponential density bound, and a chain of
subexponential mass. It then gives the corresponding exponential loss.
These quantum hypotheses are not inferred from the angle equations.

Condition (3) is a useful sufficient criterion, not an assertion about
all geometric triangulations. It becomes weak for triangulations with
many thin tetrahedra.

## 2. Flat-only repair can fail on an actual positive triangulation

A proposed universal argument was: retain every positive tetrahedron,
change only flat tetrahedra, and restore the original edge winding. Such
a repair would preserve or increase volume. The following exact example
shows that the repair need not exist.

Use the six-tetrahedron standard (7_4) triangulation with undecorated
isomorphism signature `gLvQQbefdfefmexnaxk`. Its explicit face gluings and
edge matrix are saved in the fixture. Index tetrahedra and edges from
zero and write a tetrahedron's angles in units of \(\pi\) as
\((a_j,b_j,c_j)\). The edge matrix, displayed in three-column blocks, is

\[
E=\begin{pmatrix}
100&110&110&000&001&000\\
011&011&000&001&010&001\\
001&100&010&010&100&100\\
010&000&001&100&010&000\\
100&001&001&110&000&011\\
000&000&100&001&101&110
\end{pmatrix}.                                      \tag{5}
\]

Here `110` denotes the row block \((1,1,0)\). The audit reconstructs this
matrix from the individual face permutations; it does not trust a
transcribed gluing matrix.

Consider the rational alias point

\[
\begin{array}{c|ccc}
j&a_j&b_j&c_j\\\hline
0&3/10&0&7/10\\
1&1/30&19/30&1/3\\
2&1/3&2/3&0\\
3&0&1&0\\
4&29/30&0&1/30\\
5&19/30&1/30&1/3
\end{array}                                         \tag{6}
\]

Direct multiplication gives

\[
 E\alpha=2(1,1,2,0,1,1)^T.                         \tag{7}
\]

Exactly tetrahedra (0,2,3,4) are flat; tetrahedra (1,5) are strictly
positive. Every ORIGINAL angle structure, satisfying the local sums one
and \(E\alpha=2\mathbf1\), obeys the identity

\[
 3(a_1+a_5)+b_1+2b_5-3
       =c_0+b_3+2c_3+b_4\ \geq0.                  \tag{8}
\]

This is an elementary linear combination of the original tetrahedron
and edge equations. At (6), its left side is \(-3/10\). Hence
**no modification of just tetrahedra (0,2,3,4) can restore the original
edge equations while retaining tetrahedra (1,5)**.

For a second exact verification, let (A=(L;E)), where (L) records
local sums. Let (F\) be the twelve columns belonging to the four flat
tetrahedra and (P\) the other six columns. If (q\) denotes (6), a repair
would require

\[
 A_F x=(\mathbf1,2\mathbf1)^T-A_Pq_P=:b_F,
 \qquad x\geq0.
\]

The rational vector

\[
y=(0,-1,2/3,2/3,2/3,-1;
       -1/3,1,-1/3,-1,1/3,-1/3)^T
\]

satisfies

\[
 A_F^Ty=(0,0,2/3;\ 0,0,0;\ 0,2/3,4/3;\ 0,2/3,0)^T
       \geq0,
 \qquad y^Tb_F=-1/5.                               \tag{9}
\]

Thus nonexistence is certified by rational arithmetic, with no numerical
optimization used in the proof.

### This is genuinely positive complete geometric input

The shape certificate uses the upper-half-plane root (a) of

\[
 a^3+2a-1=0,
 \qquad a\approx-0.2266988257582+1.4677115087102i.
\]

The six positively oriented shapes are

\[
 \left(\frac{1+a-a^2}{2},\ a,\ \frac{1+a}{2},\
            2+a+a^2,\ 3+a+a^2,\ a\right).        \tag{10}
\]

The audit verifies, by exact polynomial reduction, every edge product
and both peripheral products. Arb root isolation proves positivity and
the marked logarithmic equations: edge angles (2\pi\), peripheral
angles zero. These give the complete cusp and complete metric. The
Bloch--Wigner sum is rigorously enclosed by

\[
 5.13794120187341776984134833947484503
  <\operatorname{Vol}(7_4)<5.13794120187341776984134833947484504.
\]

The face permutations have one ideal vertex and torus vertex link.
An optional independent Regina/SnapPy comparison verifies validity,
orientability, and the stated knot label and isomorphism signature.

The star sizes of (5) are \((4,5,6,4,5,4)\). Therefore (2), unlike the
failed repair, bounds **all** weak wrong-edge loci for this triangulation:

\[
 V_{\mathrm{wrong\ edge}}\leq2v_3
   =2.02988321281930725004240510854904057\ldots
   <\operatorname{Vol}(7_4).                       \tag{11}
\]

Thus (6) is an obstruction to a proposed proof mechanism, not a
counterexample to volume domination.

## 3. Complete edge multipliers need not have the favorable sign

Concavity at the complete geometric point gives the valid inequality

\[
 V(\alpha)\leq V_g+2\pi\sum_e\mu_e(k_e-1),       \tag{12}
\]

where \(-\log(2\sin\alpha_{ja,g})\) is expressed as a tetrahedron
multiplier plus the incident edge multipliers. Decoration changes do not
change the pairing with feasible defects. However, its sign is not
automatically nonpositive.

Use the independently audited three-tetrahedron (5_2) chart. Its
complete triples are

\[
 (A,B,C),(A,B,C),(B,C,A),\qquad
 (A,B,C)=(\pi-3\theta,2\theta,\theta),\quad
 0<\theta<\pi/3.
\]

Set

\[
 b=-\log(2\sin2\theta),\qquad c=-\log(2\sin\theta).
\]

Stationarity gives \(-\log(2\sin A)=(2b+c)/3\). For the exact edge matrix

\[
 E=\begin{pmatrix}
 200&011&110\\
 010&110&101\\
 012&101&011
 \end{pmatrix},
\]

one can take the edge multipliers

\[
 \mu=((b-c)/3,\ b-c,\ 0),                        \tag{13}
\]

up to their common additive ambiguity. The alias assignment

\[
 (0,0,1),(1,0,0),(0,0,1)
\]

has winding (k=(0,1,2)). Consequently,

\[
 \boxed{\quad \sum_e\mu_e(k_e-1)
     =\frac{c-b}{3}
     =\frac{\log(2\cos\theta)}{3}>0.\quad}        \tag{14}
\]

All its tetrahedra are flat. Their actual volume is zero; (12) simply
has the wrong sign to prove the desired bound. The positive defect is
rigorously enclosed near (0.14059978716148\).

## 4. What the compact Legendre contour does and does not supply here

For the original marked potential, clamped radial minimization on the
whole angle cube gives the compact positive contour and its unique
geometric maximum. An alias changes that potential by

\[
 W_m(x)=W(x)+2\pi i\,m^Tx,
 \qquad \operatorname{Im}W_m
       =\operatorname{Im}W+2\pi m^T\rho.
\]

The same convex/concave construction can be applied to (W_m), but it
then minimizes a different function and has a different angle cell.
The original upper bound cannot be transferred by dropping the linear
term. Formula (14) demonstrates concretely why comparison at the fixed
geometric radius need not have the desired sign. Clipping makes the
contour compact; it does not, by itself, compare distinct winding cells.

The surviving general routes are therefore substantive: control the
actual wall charges by source/Ward cancellation, prove a stronger
topological volume comparison, or use a verifiable gap such as (3).
The present note proves the third route when its stated criterion holds
and rules out two universal shortcuts to the second.
