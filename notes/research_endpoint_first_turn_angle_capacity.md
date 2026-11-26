# The first-turn angle capacity of an endpoint product

Private written proof, 16 November 2026.

The first original turn of a microscopic endpoint product has a
zero-power unit-charge row. Its literal positive square-incidence
expansion has no closed feasible assignment. The obstruction remains
through every fixed-size shrinking real-angle collar. This is a
criterion for that particular geometric presentation, not a vanishing
statement or a growth obstruction for the exact quantum turn.

## 1. Exact placement of the first turn

Put \(N\ge2\), \(q=e^{\pi i/N}\),
\(\kappa=q^{(N-1)^2/2}\), and let \(\operatorname{can}\) denote
the ordinary remainder of degree at most \(N-1\).
Retain the original full algebra, kernel and turn:
\[
 \mathcal A_N=\mathbb C[Z]/(P_N),\quad
 P_N(Z)=2T_N(Z/2)+2,\quad
 K_N(W,Z)=\sum_{j=0}^{N-1}e_j(W)e_j(Z),
\]
\[
 \phi_N(e_i e_j)=\mathbf1_{i+j=N-1},\qquad
 Te_j=e_{N-1-j},\qquad
 (TF)(Z_t)=\phi_{Z_u}[K_N(Z_u,Z_t)F(Z_u)].
 \tag{1}
\]
Fix an ordinary endpoint product with \(r\ge1\) factors,
\[
 Q_N(Z_u)=\prod_{i=1}^r K_N(w_i,Z_u).
 \tag{2}
\]
Then the first \(T\) in
\[
 V_n\operatorname{can}Q_N
       =\kappa^nTR^{-n}T\operatorname{can}Q_N
 \tag{3}
\]
is exactly
\[
 (T\operatorname{can}Q_N)(Z_t)
  =\phi_{Z_u}
       \left[K_N(Z_u,Z_t)\prod_{i=1}^rK_N(w_i,Z_u)\right].
 \tag{4}
\]
The input \(u\) has no crossing factor in (4). The power \(-n\)
is subsequently inserted at \(t\), so it cannot alter the row at
\(u\). All first normals and the odd simple value remain in (4).
Canonical reduction is used only in its traced variable.

The original lower trace kernel has the exact expansion
\[
 W_N(u)=\frac{e^{-iNu}}{(1-\eta e^{-iNu})^2}
       =\sum_{\ell\ge1}\ell\eta^{\ell-1}e^{-iN\ell u},
 \qquad \eta=(-1)^{N-1}.
 \tag{5}
\]
In a chosen original edge-phase chart the \(\ell\)-sector of (4)
therefore has the lifted imaginary row
\[
       \sum_{i=1}^r g_{u,i}+g_{u,t}=-\pi\ell.
 \tag{6}
\]
In particular the selected unit sector has \(\ell=1\).
Equation (5) does not remove any other sector or the vertical
currents from the full trace.

## 2. Exact local capacity with fixed real angles

Fix real angles \(s_u,s_t,s_1,\ldots,s_r\in[-\pi,\pi]\).
The \(r\) endpoint edges and the one new edge at \(u\) obey the
original closed square-incidence inequalities
\[
 |s_i|+2|g_{u,i}|\le\pi,\qquad
 |s_t|+2|g_{u,t}|\le\pi,
 \tag{7}
\]
and, at their opposite incidences,
\[
 |s_u|+2|g_{i,u}|\le\pi,\qquad
 |s_u|+2|g_{t,u}|\le\pi.
 \tag{8}
\]
Hold all the opposite incidence values in (8) fixed and assume
they already satisfy (8). Only the \(r+1\) values on the left
side of (6) are free in the following statement. Define
\[
             \epsilon_i=\pi-|s_i|\ge0,\qquad
             B=\frac{\sum_i\epsilon_i+\pi-|s_t|}{2}.
 \tag{9}
\]

**Proposition 1.** With precisely these fixed and free variables,
the local row (6) is feasible under (7) if and only if
\[
                    2\pi|\ell|
                         \le\sum_i\epsilon_i+\pi-|s_t|.
 \tag{10}
\]
If \(|s_i|<\pi\) for every \(i\), \(|s_t|<\pi\), and the
fixed opposite inequalities (8) are strict, strict feasibility
in (7) is equivalent to the strict version of (10).

*Proof.* The independent row variables range over the intervals
\[
 g_{u,i}\in[-\epsilon_i/2,\epsilon_i/2],\qquad
 g_{u,t}\in[-(\pi-|s_t|)/2,(\pi-|s_t|)/2].
 \tag{11}
\]
Their sum ranges over exactly \([-B,B]\). One can see surjectivity
without selecting signs separately: if \(B>0\), assigning each
variable its interval radius times \(a/B\) realizes any sum
\(a\in[-B,B]\); if \(B=0\), only the zero sum is possible.
This proves (10). For the open intervals the sum is \((-B,B)\),
with all radii positive under the stated strict hypotheses.
The same construction with \(|a|<B\) proves the strict claim.
The inequalities (8) were held fixed and introduce no coupling
between these row variables. \(\square\)

For the selected unit row, (10) is
\[
                         \sum_i\epsilon_i\ge\pi+|s_t|.
 \tag{12}
\]
This is a local criterion, not an assertion that a surrounding
network satisfying (12) is feasible. Other vertex rows, any
prescribed totals or incidences, and imaginary-angle matching
remain additional conditions. In any full network containing
the literal block (4), however, (10) is a necessary condition
for its closed angle assignment. If some variables in (11)
are prescribed rather than free, necessity still holds but
the stated sufficiency need not hold.

## 3. Microscopic endpoints and the missing geometric replacement

For bounded real microscopic parameters,
\[
 w_i=2\cosh(\alpha_i/N)
        =-2\cos(\pi-i\alpha_i/N),
 \qquad \alpha_i\in\mathbb R.
 \tag{13}
\]
Their original endpoint lifts have real angle \(\pi\);
the reflected lifts have real angle \(-\pi\). Either gives
\(\epsilon_i=0\). The closed inequalities force
\(g_{u,i}=0\) for all \(i\), whereas the unit row would need
\(g_{u,t}=-\pi\). The last inequality of (7) permits at most
\(|g_{u,t}|\le\pi/2\).

**Corollary 2.** The literal first-turn block (4) at (13) has
no closed square-angle assignment in any lower horizontal
sector \(\ell\ge1\). This holds for every fixed \(r\), every
signed \(n\) in (3), either parity, and any surrounding marked
network that keeps the indicated block and row.

More generally, if \(r\) is fixed and real endpoint angles
satisfy
\[
          \max_i(\pi-|s_i|)\longrightarrow0,
 \tag{14}
\]
then its unit-row closed fiber is empty for all sufficiently
large levels, uniformly for every \(s_t\in[-\pi,\pi]\).

*Proof.* At saturation the right side of (10) is at most
\(\pi\), while its left side is at least \(2\pi\).
Under (14), \(\sum_i\epsilon_i<\pi\) eventually, which
contradicts (12) for every \(s_t\). The proof uses only
the real-angle inequalities, so prescribed imaginary
endpoint heights cannot repair this local failure.
The same necessary bound applies to a sector with negative
integer charge by the absolute value in (10). \(\square\)

For complex \(\alpha_i\), the angular lift in (13) does not
in general have real part exactly \(\pi\). The corollary applies if the chosen real
angles lie in the stated original closed body and satisfy
(14); it does not silently move an angle outside that body
back by a different logarithmic lift.

The empty geometric fiber is compatible with a nonzero exact
source. For example, with \(D=N-1\), \(c_0=q+q^{-1}\), and the
original Newton definition,
\[
 K_N(w,c_0)=1,\qquad Q_N(c_0)=1.
 \tag{15}
\]
Thus \(Q_N\) is a nonzero class and \(T\operatorname{can}Q_N\)
is nonzero because \(T^2=1\). For one factor the exact ordinary
representative is the dualizing divided difference
\[
 (TK_N(w,\cdot))(Z)
       =\frac{P_N(Z)-P_N(w)}{\eta N^2(Z-w)}.
 \tag{16}
\]
This includes all physical normals and is not a positive
angle minimizer of (4). Equations (15)--(16) do not give a
source rate for a general product.

The prior affine shear preserves the boundary Legendre energy
on its transformed domain. But attempting to realize the
two turns by successively minimizing the original square
energy with row (6) encounters an empty first fiber here,
even before a corner-minimum or Schur-complement issue arises.
Consequently that literal positive infimal-convolution
construction cannot identify the transformed endpoint-product
boundary domain with the original one. A different exact
recoupling or geometric representation is needed for such
an identification. No assertion about the growth of (4),
its later turn, or the whole closed source follows from
this capacity failure.

## 4. Coverage and direct-source readback

The general incidence-capacity criterion is already proved
in the original variational theorem. The added statement is
its application to the exact first turn of the endpoint
product, with its zero power, unit Fourier lift and genuine
fixed/free-variable scope. Sections 1--2 of the reduced-angle
inverse-period note and the complete recursive marked-block
note were read for coverage. Their interior fiber or
positive-branch hypotheses do not
resolve this empty local fiber.

All three complete direct sources were read at these
versions, the used implications checked, and hashes verified:

* [Original square variation and capacity](research_positive_filling_convex_variation.md),
  SHA256 2777b2bcb149d64a79757ba64ccb16be5438cf37ce820ad50c5f532afd8fc6c0.
  Complete fresh read: exact square inequalities, independent
  incidence intervals, primitive row and feasibility scope.
* [Lifted turn and boundary-work covariance](research_unit_turn_boundary_action_covariance.md),
  SHA256 bf536f6188b1ec915ca03a31dbfcdb4b797862b0cc61f412cde23b9aa957dd77.
  Complete final author read retained unchanged: exact two-turn
  source, selected Fourier rows and the transformed-domain limitation.
* [Exact original endpoint turn](research_full_endpoint_unit_turn_identities.md),
  SHA256 e2f69aaff28080b9dd9e11365ce18d68a9d738667917204714556681c50789e8.
  Complete fresh read retained from this review sequence:
  kernel normalization and full-normal divided difference (16).

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical experiment, test or build
was run. Frozen notes and public manuscripts are unchanged.
