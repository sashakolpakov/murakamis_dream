# A soft-cut parameter separates the regular endpoint types

Private written proof, 18 November 2026.

For a fixed complete hyperbolic knot holonomy and a fixed finite
braid presentation, a generic
binomial cut parameter separates every finite row-alignment endpoint
from every finite column-alignment endpoint on its framing line.
On the chart where all actual prefix minors are units, these are
respectively the physical \(e=0\) and \(f=0\) branches. Consequently
every vanishing Euler interaction there has one quadratic zero,
not two vanishing factors.

The parameter changes an exact presentation of the original unmarked
scalar. It does not identify marked sources, remove their currents,
or put the original integration cycle on this framing line.
Prefix-zero and infinite framing strata are excluded throughout
the endpoint conclusion.

## 1. The actual finite list and its framing lines

Use the complete-color conventions of M and S. At every stage of
the actual signed braid, let \(H_j\) be minus the physical strand
meridian and let
\[
 P_j=H_j\cdots H_1,\qquad P_0=I.
 \tag{1}
\]
All occurrences at all stages are retained as a finite list.
The complete meridians are noncentral, so
\[
 \operatorname{tr}H_j=-2,\quad \det H_j=1,\qquad
 H_j+I=a_jb_j^t,\quad b_j^ta_j=0,
 \tag{2}
\]
with nonzero constant columns \(a_j,b_j\). The kernel of \(b_j^t\)
is exactly \(\mathbb C a_j\). Repeated meridians and repeated flags
are permitted.

Fix the selected complete meridian as
\(J_1=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)\).
Put \(c_0=2\pi i\) and use the actual selected-flag frames
\[
 F(r,s)=
 \begin{pmatrix}r&1-r\\s&-s\end{pmatrix},\qquad
 v_r=(r,s)^t,\qquad
 \alpha_r=(1,(1-r)/s),\qquad s\ne0.
 \tag{3}
\]
Thus \(\alpha_rv_r=1\), and \(F(r,s)(1,1)^t=(1,0)^t\).
The cut clock is \(A_{\rm cut}=(1+s)^{-1}\). In the binomial
presentation of F,
\[
 s=s(\theta)=e^{-c_0\theta}-1,\qquad
 A_{\rm cut}=e^{c_0\theta}.
 \tag{4}
\]
Near \(\theta=1/2\), both \(s\) and \(1+s\) are nonzero.
F supplies a regular midpoint frame \((r_0,-2)\). Shrink a
neighborhood of \(\theta=1/2\) so that all prefix minors at
\((r_0,s(\theta))\) remain units.

For a retained prefix \(P\), write
\[
 Q_P(r,s)=s\,\alpha_rPv_r.
 \tag{5}
\]
S proves its explicit degree-at-most-two polynomial formula.
On the open set where every \(Q_P\) is nonzero, the actual Gauss
inverse gives
\[
 K_j=\frac{Q_{P_j}}{Q_{P_{j-1}}},\qquad
 A_j=-\frac{Q_{P_{j-1}}}{Q_{P_j}},\qquad
 A_j-1=-\frac{s(\alpha_ra_j)(b_j^tP_{j-1}v_r)}{Q_{P_j}}.
 \tag{6}
\]
This is the original wall equation with its multiplicity, not a
replacement by a reduced divisor.

## 2. Which factor is the physical \(e\)- or \(f\)-zero?

Here is the branch identification directly from M's lower Gauss
prefix. Set
\[
 \widetilde H=F^{-1}H_jF,\quad
 \widetilde P=F^{-1}P_{j-1}F=(p_{\mu\nu}),\quad
 B_-=
 \begin{pmatrix}1&0\\-p_{21}&p_{11}\end{pmatrix}.
 \tag{7}
\]
The physical matrix at this wire is
\[
 G_j=B_-\widetilde H B_-^{-1}
 =\begin{pmatrix}K_j&e_j\\K_jf_j&K_j^{-1}+e_jf_j\end{pmatrix}.
 \tag{8}
\]
Every denominator in (7)--(8) is a unit on the stated prefix chart.

The first row of \(B_-\) is \((1,0)\), and the second column of
\(B_-^{-1}\) is \((0,p_{11}^{-1})^t\). Hence
\(e_j=\widetilde H_{12}/p_{11}\).
For a noncentral determinant-one matrix of trace \(-2\),
vanishing of that upper-right entry is equivalent to the coordinate
covector \((1,0)\) being a left eigenline of eigenvalue \(-1\).
Returning to the fixed frame and using (2) proves
\[
                 e_j=0\quad\Longleftrightarrow\quad
                              \alpha_ra_j=0.
 \tag{9}
\]
For the other branch, \(f_j=0\) is equivalent to
\(G_j(1,0)^t=-(1,0)^t\). Moreover
\[
 F B_-^{-1}(1,0)^t
        =F(1,p_{21}/p_{11})^t
        =P_{j-1}v_r/p_{11}.
 \tag{10}
\]
Thus the same unique eigenline calculation gives
\[
                 f_j=0\quad\Longleftrightarrow\quad
                              b_j^tP_{j-1}v_r=0.
 \tag{11}
\]
These equivalences hold for every retained stage occurrence,
including both input and output wires of negative crossings.
They do not use a factorial momentum coordinate at its pole.

The factors in (6) cannot vanish simultaneously on this prefix
chart. Indeed the column condition would put \(P_{j-1}v_r\)
in \(\mathbb Ca_j\), and the row condition would then give
\(\alpha_rP_{j-1}v_r=0\), contradicting (5).
Equivalently, a noncentral complete \(G_j\) cannot have both
\(e_j=f_j=0\).

## 3. The complete finite exceptional set of cut parameters

For each row flag with \((a_j)_2\ne0\), put
\[
                       \xi_j=(a_j)_1/(a_j)_2.
 \]
Its unique finite row root is
\[
                          r=1+s\xi_j.
 \tag{12}
\]
If \((a_j)_2=0\), the row factor is the nonzero constant
\((a_j)_1\), so it has no finite root.

For each column flag put \(u_j=P_{j-1}^{-1}a_j\). If
\((u_j)_2\ne0\), define \(\eta_j=(u_j)_1/(u_j)_2\).
Since \(\ker(b_j^tP_{j-1})=\mathbb Cu_j\), its unique finite
column root is
\[
                              r=s\eta_j.
 \tag{13}
\]
If \((u_j)_2=0\), it has no finite root: \(v_r\) has the
nonzero second component \(s\).
These alternatives include flags at infinity without assigning
them spurious finite roots.

Let \(\Xi\) and \(\mathcal H\) be the two finite lists of finite
ratios just defined. Introduce the finite set
\[
 \mathcal E=
 \left\{\frac1{\eta-\xi}:
               \xi\in\Xi,\ \eta\in\mathcal H,\ \eta\ne\xi\right\}.
 \tag{14}
\]
A row root and a column root, possibly belonging to different
crossings or stages, coincide exactly when
\[
                         s(\eta-\xi)=1.
 \tag{15}
\]
If \(\eta=\xi\), there is no collision. Thus for \(s\notin\mathcal E\)
the entire row-root set and column-root set are disjoint.
No pairwise separation within either individual set is required.
If there are \(w\) retained wire occurrences, then
\(|\mathcal E|\le w^2\); repetitions only reduce this bound.

The holomorphic function \(s(\theta)\) has nonzero derivative near
\(1/2\). Consequently one can avoid (14) with a fixed \(\theta\)
arbitrarily close to \(1/2\), while preserving the regular seed
specified after (4). This proves the asserted generic separation.
One can even choose real \(\theta\in(0,1)\) arbitrarily close to
\(1/2\): finitely many forbidden values cannot exhaust that arc.
This real-parameter statement is only separation. It does not
assert that all factorial lengths simultaneously lie in F's slit
domain on a fixed real-\(\theta\) slice.

## 4. Endpoint multiplicities and signed Euler interactions

Fix such a parameter and a finite value \(r_*\) where all retained
prefix minors remain units. Suppose some physical wire clock is
one. All vanishing wires at \(r_*\) then have the same branch type:
either every such wire has \(e_j=0,f_j\ne0\), or every such wire
has \(f_j=0,e_j\ne0\). Otherwise (12)--(15) would give an excluded
row/column collision.

Each individual wire wall there is simple as a function of \(r\).
For a finite row root the row factor in (6) has nonzero derivative
\(-(a_j)_2/s\); its column factor is a unit. For a finite column
root the column factor is a nonconstant linear polynomial, and
its row factor is a unit. Equation (6) proves the claim in both
cases, even if several wire walls have the same root.

The complete Casimir identity from S is
\[
                       e_jf_j=\frac{(A_j-1)^2}{A_j}.
 \tag{16}
\]
Therefore the vanishing physical entry has order exactly two at
\(r_*\), while the other entry is a unit. Consider the actual
signed interactions
\[
 X_+=e_1f_2,\qquad
 X_-=(K_1/K_2)e_2f_1,\qquad
 C_+=(1-X_+)^{-1},\quad C_-=1-X_-.
 \tag{17}
\]
If one of these \(X_\pm\) vanishes at \(r_*\), exactly one of its
two physical factors vanishes. Its order is therefore exactly two;
the extra \(K\)-ratio is a unit. In particular no product in (17)
has the order-four contact obtained by combining an \(e\)-zero
with an \(f\)-zero. A transfer wall \(C_\pm=1\) is precisely such
an \(X_\pm=0\) and hence has this order-two contact.

This is a classification of regular classical endpoint branches.
It selects the one-vanishing-factor alternative for a separately
proved endpoint Euler estimate. It is not an operator convergence
estimate, a nondegeneracy assertion for the full phase, or an
estimate for a neighboring source packet. The exact finite upper
clock is still \(Q^{-1}\); complete-color contact does not erase
its displacement, its second marked divisor, or any quantum normal.

## 5. The original scalar and the retained marked current

The parameter is a source-compatible choice, not a new invariant.
For \(d=N-1\), retain F's exact diagonal cut
\[
 P_{N,\theta}=\sum_{a=0}^{d}\binom da
                 \theta^a(1-\theta)^{d-a}T_a.
 \tag{18}
\]
Its trace is one. For the original unmarked scalar cut operator
\(C_N=F_N I\) at the prescribed root, this gives exactly
\[
                       \operatorname{Tr}(P_{N,\theta}C_N)=F_N.
 \tag{19}
\]
Every original crossing, tail pivot, framing scalar and support
wall is retained. For a marked cut matrix \(C\), keep instead the
exact identity supplied by F:
\[
 \operatorname{Tr}((P_{N,\theta}-T_0)C)
             =\operatorname{Tr}(B_{N,\theta}[C,\mathcal E]),
 \quad
 B_{N,\theta}=-\sum_{r<d}
 \frac{\sum_{a>r}\binom da\theta^a(1-\theta)^{d-a}}
                  {M Q^{-r-1}-M^{-1}}E_{r+1,r}.
 \tag{20}
\]
The current and its parameter derivatives remain whole on their
stated unit domain. No marked equality to the highest cut is used.
Equation (19) is not used to reset a closed source away from the
root. Quantum or meridian differentiation retains (20) and the
actual chosen pivots; no identification with ordinary closed
Jones normals is asserted.
For complex \(\theta\), the exact total variation is
\[
               (|\theta|+|1-\theta|)^d.
 \tag{21}
\]
It can be made smaller than \(e^{\varepsilon d}\) for any prescribed
\(\varepsilon>0\), with a fixed choice avoiding (14). For real
\(\theta\in(0,1)\), the weights are positive and (21) is one.

Neither presentation controls the original source at a zero prefix
minor or at \(r=\infty\). Those strata can still mix endpoint types.
Nor does (19) provide a deformation, a framing period, or a
nonzero geometric coefficient. The result removes a finite list
of regular mixed-type collisions by an exact scalar presentation;
all other boundary and marked-source questions remain separate.

## Complete proof-source pins

* S: notes/research_actual_facet_seams_and_geometric_boundary.md,
  SHA256 ac250fc87e7bf1d4f6851c346ef08f7cd08d9e4566d1283981c03dee2427441c.
* M: notes/marked_braid_holonomy.md,
  SHA256 eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.
* F: notes/research_literal_factorial_common_slit_frame.md,
  SHA256 9764a2b77469c7fad402b9b8e609b304a79083bde18fb139031c06fd93650ca8.

All three complete direct texts were freshly read nontruncated in
this author sequence, and their used implications checked. Only
written mathematics and text/hash operations were used. Frozen and
public files are unchanged.
