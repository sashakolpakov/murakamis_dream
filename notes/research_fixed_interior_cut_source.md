# A fixed interior cut for the original physical scalar

Private written proof, 18 November 2026.

The original unmarked invariant can be evaluated at one interior cut
occupation, instead of at the highest vector. The exact Ward current
between the two probes has polynomial size in the level, including
every fixed meridian derivative on a specified shrinking disk.
In the existing classical cut chart, an interior occupation selects
a noncentral complete meridian. This provides a possible regular
presentation of the same scalar. It does not identify its stationary
scheme or cycle with that of the highest-cut Borel source.

## 1. Exact finite cut identities

Keep the original finite knot word, framing and pivotal partial trace.
Let \(C_N(M)\) be its resulting endomorphism on the remaining head, in
the factorial basis of [M]. Write
\[
 N\ge2,\quad Q=e^{2\pi i/N},\quad
 \mathcal E e_{r+1}=\epsilon_r(M)e_r,\quad
 \epsilon_r(M)=M Q^{-r-1}-M^{-1},
 \quad 0\le r<N-1.
 \tag{1}
\]
The final wrap arrow is zero. Total occupation conservation makes
\(C_N\) diagonal. Actual quantum-group intertwining gives
\([\mathcal E,C_N]=0\), with the original pivots included [W].
For generic \(M\), every \(\epsilon_r(M)\ne0\). Thus
\[
 \epsilon_r(M)\bigl((C_N)_{r+1,r+1}-(C_N)_{rr}\bigr)=0
\]
forces all diagonal entries to be equal. The entries are Laurent
functions of the retained meridian; continuation gives the whole
matrix identity at exceptional values as well. Consequently, with
the unchanged original scalar normalization,
\[
 C_N(M)=F_N(M)I,\qquad
 \operatorname{Tr}(T_a C_N(M))=F_N(M),\quad
 T_a=e_ae_a^*,\quad 0\le a<N .
 \tag{2}
\]
At \(M=1\) this is the original physical Kashaev scalar. No framing
factor or additional circle normalization is inserted.

For \(a>0\), define the actual finite current
\[
 B_{N,a}(M)=-\sum_{r=0}^{a-1}
                  \epsilon_r(M)^{-1}E_{r+1,r}.
 \tag{3}
\]
It is initially defined off its displayed poles. Direct matrix
multiplication telescopes to
\[
 [\mathcal E,B_{N,a}]=T_a-T_0 .
 \tag{4}
\]
The negative sign is fixed: the diagonal at zero is \(-1\),
at \(a\) it is \(+1\), and all intermediate terms cancel.
For an arbitrary marked cut endomorphism \(C_N^{\rm mark}\),
ordinary cyclicity gives the exact identity
\[
 \operatorname{Tr}((T_a-T_0)C_N^{\rm mark})
       =\operatorname{Tr}
                 (B_{N,a}[C_N^{\rm mark},\mathcal E]).
 \tag{5}
\]
For the unmarked knot the right side is zero. For inserted clocks
or other coupons it remains the prescribed defect current. Equation
(5) does not assert unchanged marked families.

There is an exact coefficient presentation too. Define the literal
cut grading \(D_N(z)e_a=z^ae_a\). Then
\[
 \operatorname{Tr}(D_N(z)C_N(M))
                  =F_N(M)\sum_{a=0}^{N-1}z^a,\qquad
 [z^a]\operatorname{Tr}(D_N(z)C_N)=F_N(M).
 \tag{6}
\]
This finite polynomial identity puts no pivot on the open head.
It does not replace \(D_N(z)\) by a single matrix entry \(z\).

## 2. A polynomial bound for the current and its meridian jets

Declare the factorial basis orthonormal for this estimate. A matrix
with one weighted subdiagonal has operator norm the largest weight.
At \(M=1\),
\[
 |\epsilon_r(1)|=
     2\left|\sin\frac{\pi(r+1)}N\right|\ge\frac4N .
 \tag{7}
\]
Here the minimum occurs at an end of \(1,\ldots,N-1\), and
\(\sin x\ge2x/\pi\) on \([0,\pi/2]\).
For \(|M-1|\le1/(4N)\), one has \(|M|\ge7/8\) and
\[
 |\epsilon_r(M)-\epsilon_r(1)|
 \le |M-1|+|M^{-1}-1|
 <3|M-1|\le\frac{3}{4N}.
 \tag{8}
\]
Thus all denominators in (3) are bounded below by \(3/N\) on
that disk, independently of \(a\), and
\[
                       \|B_{N,a}(M)\|\le N/3 .
 \tag{9}
\]
On the smaller disk \(|M-1|\le1/(8N)\), the Cauchy formula
therefore gives, for every fixed \(j\ge0\),
\[
                \|\partial_M^jB_{N,a}(M)\|
                            \le C_j N^{j+1}.
 \tag{10}
\]
The constants do not depend on \(a\) or \(N\). This bound includes
the retained meridian normals; it is not merely a value at \(M=1\).
The disk shrinks with the level, and no estimate on a fixed-radius
meridian disk is claimed.

The estimates concern the current, not a relative error in a scalar
pairing. In particular they do not bound (5) relative to the possibly
small value \(\operatorname{Tr}(T_0 C_N^{\rm mark})\).

## 3. One fixed bulk choice has a regular complete meridian

Choose once and for all \(0<\theta<1\), and take
\[
                  a_N=\lfloor\theta N\rfloor
 \tag{11}
\]
for sufficiently large \(N\). The midpoint choice \(\theta=1/2\)
is available at both parities. The exact identities (2)--(6)
apply for every such level.

The discrete position is \(A_N=Q^{a_N}\). In the actual regular
classical cut chart of [M,J], the position and framing coordinates
satisfy
\[
 A_{\rm cut}=\frac{M}{M+s},\qquad
 A_N\longrightarrow A_\theta=e^{2\pi i\theta}.
 \tag{12}
\]
Thus the selected classical position is \(A_{\rm cut}=A_\theta\).
This statement does not drop any finite Weyl shift from the
matrices in Section 1. At the complete value \(M=1\), it selects
\[
                    s_\theta=e^{-2\pi i\theta}-1\ne0 .
 \tag{13}
\]
On the existing \(p_{\rm cut}=1\) framing chart, its meridian is
\[
 \mu_{s_\theta}
   =\begin{pmatrix}1+s_\theta&-s_\theta\\
                    s_\theta&1-s_\theta\end{pmatrix}.
 \tag{14}
\]
This is noncentral parabolic: its determinant is one, its trace
is two, and \(\mu_{s_\theta}-I\ne0\).
For \(\theta=1/2\), \(s_\theta=-2\).
The frame
\[
 F(r,s)=\begin{pmatrix}r&1-r\\s&-s\end{pmatrix},\qquad
 \mu_s=F^{-1}\begin{pmatrix}1&1\\0&1\end{pmatrix}F
 \tag{15}
\]
has determinant \(-s\). With \(s\) near \(s_\theta\) and \(r\)
in a fixed compact set, both this matrix and its inverse are
bounded independently of the level.

Thus the selected noncentral geometric framing itself need not
escape merely because the complete eigenvalues coincide. This
is an explicit change of the finite cut presentation, not a
regularization of all matrices in the old highest-cut chart.
It does not put every source configuration or the remaining
centralizer coordinate \(r\) in a compact set.

## 4. What remains to justify in the new presentation

Equations (2)--(11) justify using the fixed interior probe to compute
the original unmarked invariant. Its cut occupation grows with \(N\).
It is therefore a new semiclassical source presentation; it is not
the fixed-occupation \(h\)-expansion of the old highest-cut germ.

At a known geometric critical configuration, (12) fixes the
coadjoint framing parameter \(s\), leaving the centralizer
parameter \(r\). Fixing a cut occupation also removes a
stationarity equation. The equivalence of the entire new critical
scheme with the original geometric representation scheme has
not followed from (2). The exact interior Ward recurrence is
available, but turning it into that scheme or a relative-chain
map requires its actual source analysis.

Likewise (5) retains every marked defect. It cannot be used to
carry a previously defined marked Borel period unchanged into the
new presentation. A new phase, amplitude, endpoint analysis and
normalization must be derived from its literal coefficient
extraction. No geometric coefficient or volume limit is claimed.

## 5. Complete proof sources

| Label | Complete source | SHA256 |
|---|---|---|
| W | notes/coherent_cut_obstruction_and_ward_relative_class.md | 28141e28d4bc08a8acfa4cef9a8549ed7aadb1344f8796617e68282f7b351e4d |
| M | notes/marked_braid_holonomy.md | eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f |
| J | notes/regular_meridian_centralizer.md | 4f7d55c89b067ec75f201ff7ccb05bfd636f35159ab0c6053cbb3a8e8c8bae0f |

All three complete unchanged texts were read in the current research
sequence, their used implications checked, and their matching pins
renewed. W already proves arbitrary normalized diagonal Ward
transgression; there is no novelty claim for (4)--(5). M supplies
the literal finite module and scalar normalization, J the actual
classical position/frame relation. The fixed bulk choice, bounds
and geometric scope are explicit above. No mathematical program,
numerical test or build was used. Frozen/public files are unchanged.
