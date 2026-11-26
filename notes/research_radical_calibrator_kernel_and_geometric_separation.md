# The radical source calibrator and its inverse-meridian boundary

Private written proof, 19 November 2026.

The explicit source-one correction of P obeys exact root pair
annihilators. Their quantum Gauss product is the identity on its
image. The corresponding classical boundary subvariety is disjoint
from the faithful locus of an ordinary cooriented braid: it requires
two positive meridians to have product one. This is an algebraic
boundary statement. Its implication for a characteristic branch
requires the actual regular symbol calculus specified below.

Separately, the coefficient-Euclidean coherent kernel is an explicit
polynomial, with exponential decay on compact real sets away from
its pair-antipodal and spectator-matching relation. No complex-cycle
estimate or nonzero geometric source follows from this real estimate.
The only complete directs are P and M, pinned at the end.

## 1. The literal root coupon

Fix integers \(m,N\ge2\), and put
\[
 d=N-1,\qquad q=e^{\pi i/N},\qquad Q=q^2,
 \qquad x=-q^{-1}.
 \tag{1}
\]
Thus \(|x|=1\), \(x^2=Q^{-1}\). All arrows in this note are at
the root color \(M=1\). The physical coefficient basis
\(w_0,\ldots,w_d\) is orthonormal, and the capped arrows are
\[
 Kw_a=xQ^{-a}w_a,\quad
 Ew_a=(Q^{-a}-1)w_{a-1}\ (a>0),\quad Ew_0=0,
\]
\[
 Fw_a=(1-Q^{a+1})w_{a+1}\ (a<d),\qquad Fw_d=0.
 \tag{2}
\]
On two successive heads write
\[
 E_{12}=E_1K_2+E_2,\quad
 F_{12}=F_1+K_1^{-1}F_2,\quad K_{12}=K_1K_2.
 \tag{3}
\]
P gives the rank-one radical matrix
\[
 r=|\psi\rangle\langle\varphi|,
 \quad |\psi\rangle=\sum_{u=0}^d x^{u-d}|u,d-u\rangle,
 \quad \langle\varphi|=\sum_{v=0}^d x^v\langle v,d-v|.
 \tag{4}
\]
The covector is algebraic, not the adjoint of \(\psi\). The equality
with P's covector uses \(x^{-v}Q^{-v}=x^v\). In particular its
nonzero entry is \(r_{u,v}=x^{u+v-d}\), and \(r^2=0\).

The full source calibrator is P's ordered chain
\(T_0=r_{12}r_{23}\cdots r_{m-1,m}\). Its exact action is
\[
 T_0|a_1,\ldots,a_{m-2},v,d-v\rangle
 =\sum_{u=0}^d x^{u+v-d}|u,d-u,a_1,\ldots,a_{m-2}\rangle,
 \tag{5}
\]
and it vanishes on all other inputs. Thus it is one pair matrix
and a tensor permutation, with no dualization of any head. All
occupation ranges in (4)--(5) are the original finite ranges.

For the original pointed functional
\[
 Q_{\rm pt}=|0\rangle\langle0|\otimes
                     K_2^{-d}\otimes\cdots\otimes K_m^{-d},
 \qquad \Phi(C)=\operatorname{Tr}(Q_{\rm pt}C),
 \tag{6}
\]
P proves \(\Phi(T_0)=1\), \(\|T_0\|_{\rm op}=N\), and
\(\|T_0\|_{\rm HS}=N^{m/2}\). No pivot is added to the opened
head. Any original external scalar still multiplies the original
source; (6) does not reset it.

## 2. Exact annihilators and quantum Gauss boundary

One has, entrywise and at every integer level,
\[
 E_{12}r=F_{12}r=0,\quad K_{12}r=r,
 \qquad rE_{12}=rF_{12}=0,\quad rK_{12}=r.
 \tag{7}
\]
Here is a direct cap-sensitive check. In \(E_{12}\psi\), the
coefficient at \((u,d-1-u)\) is the sum
\(x^{u-d}(1-Q^{u+1})+x^{u-d}(Q^{u+1}-1)=0\).
In \(F_{12}\psi\), the coefficient at \((u,d+1-u)\) is
\(x^{u-1-d}(1-Q^u)+x^{u-1-d}(Q^u-1)=0\).
Forbidden boundary terms have their literal zero coefficients in
(2). The Cartan is \(x^2Q^{-d}=1\) on degree \(d\).

For the right lowering identity, the only possible input degree
is \(d+1=N\). At input \((a,b)\) of that degree the result is
\(x^a[Q^{-b}(Q^{-a}-1)+(Q^{-b}-1)]=0\).
For the right raising identity the only possible input degree is
\(d-1\); its coefficient is
\(x^{a+1}[1-Q^{a+1}+Q^{a+1}(1-Q^{b+1})]=0\).
Indeed \(a+b+2=N\). This proves all of (7), including the caps.

Consequently
\[
 E_{12}T_0=F_{12}T_0=0,\quad (K_{12}-I)T_0=0,
\]
\[
 T_0E_{m-1,m}=T_0F_{m-1,m}=0,\quad
 T_0(K_{m-1,m}-I)=0.
 \tag{8}
\]
These are output first-pair and input last-pair identities, with
the spectator permutation in (5) retained.

An exact auxiliary-matrix form makes the relevant ordering explicit.
Define matrices with operator entries
\[
 \mathsf L_{+,j}=\begin{pmatrix}K_j&E_j\\0&I\end{pmatrix},
 \qquad
 \mathsf L_{-,j}=\begin{pmatrix}I&0\\-K_jF_j&K_j\end{pmatrix},
 \qquad
 \mathsf L_{-,j}^{-1}=\begin{pmatrix}I&0\\F_j&K_j^{-1}\end{pmatrix}.
 \tag{9}
\]
Multiplication, using only commutation between different heads, gives
\[
 \mathsf L_{+,2}\mathsf L_{+,1}
  =\begin{pmatrix}K_{12}&E_{12}\\0&I\end{pmatrix},\qquad
 \mathsf L_{-,2}\mathsf L_{-,1}
  =\begin{pmatrix}I&0\\-K_{12}F_{12}&K_{12}\end{pmatrix}.
 \tag{10}
\]
Both matrices act as the auxiliary identity on \(r\). Hence, with
\[
 \mathsf D=(\mathsf L_{-,2}\mathsf L_{-,1})^{-1}
                (\mathsf L_{+,2}\mathsf L_{+,1})-I_2,
 \qquad \mathsf D_{ab}T_0=0\quad(1\le a,b\le2).
 \tag{11}
\]
The right last-pair version follows in the same order from (7).
No classical multiplication of covariant symbols was used in (11).

This also gives a direct fact about P's scalar repair. At the root
write its repaired matrix as \(W^\sharp=W+\lambda_NT_0\), with
the exact scalar \(\lambda_N\) prescribed there. Then
\[
                 \mathsf D_{ab}W^\sharp=\mathsf D_{ab}W.
 \tag{12}
\]
There is no bound or nonvanishing hypothesis on \(\lambda_N\) in
this identity. Local inversion of an entry of \(\mathsf D\) would
require a justified local calculus; (12) does not assert it.

## 3. Dressed positive meridians

Consider commuting physical coordinates \((k_j,e_j,f_j)\), with
\(k_j\ne0\), in M's Gauss chart. Set
\[
 b_{+,j}=\begin{pmatrix}k_j&e_j\\0&1\end{pmatrix},\qquad
 b_{-,j}=\begin{pmatrix}1&0\\-k_jf_j&k_j\end{pmatrix},\qquad
 G_j=b_{-,j}^{-1}b_{+,j}.
 \tag{13}
\]
Put \(B_{-,j}=b_{-,j}\cdots b_{-,1}\), \(B_{-,0}=I\), and
\[
       H_j=B_{-,j-1}^{-1}G_jB_{-,j-1},\qquad \mu_j=-H_j.
 \tag{14}
\]
These are M's actual dressed meridians. In particular adjacent
products are not obtained by simply multiplying the raw \(G_j\).
Cancelling the intermediate prefix gives
\[
 H_{j+1}H_j=B_{-,j-1}^{-1}
   (b_{-,j+1}b_{-,j})^{-1}(b_{+,j+1}b_{+,j})B_{-,j-1}.
 \tag{15}
\]
The pair boundary subvariety dictated by (7) is
\[
 k_jk_{j+1}=1,\qquad e_jk_{j+1}+e_{j+1}=0,\qquad
                  f_j+k_j^{-1}f_{j+1}=0.
 \tag{16}
\]
The two products of triangular matrices in (15) are both the
identity on (16). Therefore
\[
                    H_{j+1}H_j=I,
              \qquad \mu_{j+1}\mu_j=I.
 \tag{17}
\]
The central minus signs cancel. These equations hold at any
regular prefix; they are not limited to a bare two-head tuple.

Suppose now that the tuple is obtained from a faithful
\(\mathrm{PSL}_2(\mathbb C)\) representation of the knot group of
an ordinary cooriented braid closure. At any stage every head is
a positively oriented meridian. M's Hurwitz rule preserves this
property by conjugation. Each such meridian has abelianization
one in \(H_1\cong\mathbb Z\); the product of two has abelianization
two and is not the identity of the knot group. Faithfulness
excludes its image being projectively the identity. Thus (16)
is disjoint from this faithful locus, on input or output tuples.

In particular the conclusion applies to the complete faithful
hyperbolic holonomy in every regular Gauss frame. It uses the
matrix equation (17), not just a trace-two equation. Repeated
meridians or coinciding flags do not change the abelianization
argument. On a compact set of such regular tuples the norm of
\(H_{j+1}H_j-I\) has a positive minimum; locally one of its entries
is a unit.

The output side of a matrix kernel does not reverse a physical
head's meridian. A plat cup with a separately dual-oriented leg
is a different convention: there an inverse pair is allowed.
Neither that convention nor a dualization is present in (5),
(8), or the ordinary braid assertion above.

## 4. What a characteristic interpretation requires

There is an exact ordinary-output realization of (2). On
\(p(z)=\sum_{a=0}^d c_a z^a\), let
\((T_Qp)(z)=p(Qz)\). Then
\[
 E=z^{-1}(T_{Q^{-1}}-1),\qquad
 F=z(1-QT_Q),\qquad K=xT_{Q^{-1}}.
 \tag{18}
\]
The apparent pole in \(E\) is removable, and the degree \(d+1\)
coefficient in \(F\) vanishes because \(Q^N=1\). These are
literal finite-matrix equations, including both caps.

For example, suppose an actual ordinary-output local branch has
\(p_N=\exp(NS)(a+O(N^{-1}))\) on a fixed regular logarithmic chart,
with a nonzero analytic amplitude and uniform holomorphic error
on the neighborhoods needed for the shifts in (18). Write
\(c_0=2\pi i\), \(A_j=\exp(c_0z_j\partial_{z_j}S)\).
The actual shift ratios then give the commuting principal symbols
\[
 k_j=-A_j^{-1},\qquad
 e_j=z_j^{-1}(A_j^{-1}-1),\qquad
 f_j=z_j(1-A_j).
 \tag{19}
\]
These are the commuting physical symbols, not their \(N\)-th-power
central characters. They satisfy \(k_j+k_j^{-1}+e_jf_j=-2\), as
required by M at the root color. Applying (18) directly to the pair equations
(8) proves (16) for such a branch of \(T_0\). Equivalently,
the principal Gauss product of (11) is \(H_2H_1-I\).
This identifies the regular characteristic boundary of the
annihilator equations, and excludes a branch at a faithful
ordinary-braid point under the stated symbol calculus.

Existence of that branch has not been asserted. In particular,
an incident endpoint or a change to a factorial or normalized
mixed polarization needs its own exact transformation and
asymptotic control. The finite equations alone do not justify
replacing symbols of products by products of normalized
coherent symbols there. Nor does the unit entry in the classical
Gauss defect prove a global inverse or a contour estimate.

## 5. Exact Euclidean kernel and real concentration

Use the normalized coefficient-Euclidean vectors
\[
 \psi_z=(1+|z|^2)^{-d/2}
                   \sum_{a=0}^d\sqrt{\binom da}\,z^a w_a.
 \tag{20}
\]
Equation (5) and the binomial theorem give the exact kernel
\[
 \langle\psi_{\mathbf y},T_0\psi_{\mathbf z}\rangle
 =x^{-d}
 \frac{[(\bar y_2+x\bar y_1)(z_m+xz_{m-1})]^d
       \prod_{j=3}^m(1+\bar y_jz_{j-2})^d}
 {\prod_{j=1}^m(1+|y_j|^2)^{d/2}(1+|z_j|^2)^{d/2}}.
 \tag{21}
\]
The two pair sums have binomial, rather than square-root-binomial,
weights because \(\sqrt{\binom du\binom d{d-u}}=\binom du\).
The spectator sums are ordinary coherent overlaps. The formula
includes \(m=2\), with empty spectator product.

For \(|x|=1\) the elementary identities
\[
 \frac{|b+xa|^2}{(1+|a|^2)(1+|b|^2)}
 =1-\frac{|1-xa\bar b|^2}{(1+|a|^2)(1+|b|^2)},
\]
\[
 \frac{|1+\bar y z|^2}{(1+|y|^2)(1+|z|^2)}
 =1-\frac{|y-z|^2}{(1+|y|^2)(1+|z|^2)}
 \tag{22}
\]
show that the modulus in (21) is the product of
\((1-\Delta)^{d/2}\), for the corresponding nonnegative deficits.
All these deficits lie in \([0,1]\). If one is at least
\(\delta>0\), then the modulus is at most
\((1-\delta)^{d/2}\). Equality in every factor requires
\[
 x\bar y_1y_2=1,\qquad xz_{m-1}\bar z_m=1,\qquad
                         y_j=z_{j-2}\quad(j\ge3).
 \tag{23}
\]
The formulas extend in homogeneous coordinates across zero and
infinity. Since \(x\to-1\), (23) tends to pair antipodality on
both ends and shifted spectator matching. Every compact real
set disjoint from this limiting relation has a uniform positive
deficit for all sufficiently large \(N\), hence exponential
decay by (22). No unrecorded power of \(N\) is needed.

Replacing \(\bar y\) by independent variables \(\zeta\) and
omitting the positive normalization in (21) gives the exact
holomorphic polynomial section
\[
 x^{-d}[(\zeta_2+x\zeta_1)(z_m+xz_{m-1})]^d
                         \prod_{j=3}^m(1+\zeta_jz_{j-2})^d.
 \tag{24}
\]
It has a logarithm on any simply connected chart avoiding these
factors' zeros, with its displayed finite phases retained.
This is not a uniform estimate on a complex integration chain,
nor an identification of that polarization with (18).
In particular we do not divide by an identity coherent kernel
on its incidence divisor.

## 6. Scope of the source consequence

The new information about the source repair is the exact root
identity (12) and its inverse-meridian boundary equations.
They locate a specific correction direction, rather than an
arbitrary Hilbert--Schmidt projection. They do not bound its
contraction with a geometric cycle, prove phase preservation
of the repaired word, or select a nonzero geometric coefficient.
Real pointwise decay (22) cannot be substituted for any of those
complex or source-relative estimates.

In particular \(\lambda_N\) can retain the whole word's exponential
growth. The calibrator defines a different correspondence, so its
closed correction cannot be treated as another branch of the
original braid graph when applying representation-volume rigidity.
Boundary disjointness alone does not bound that correction's action
or closing contribution.

P's whole-meridian coupon is obtained by an exact lowering frame.
That frame does not simultaneously trivialize \(F\). Accordingly
the pair \(E,F,K\) annihilators, the Gauss defect (11), and the
separation proved here are root statements; no assertion about
their true meridian derivatives is made. The exact whole-meridian
source repair and its retained pivot derivatives remain those
of P. No new volume-conjecture case is proved.

## Complete directs and author verification

* P: [research_source_preserving_commutant_projection_and_window_repair.md](research_source_preserving_commutant_projection_and_window_repair.md),
  543 lines, SHA256
  `ff75410cfbba220c17bfd8153f27f901f21f1d98077b186945ebe502f24032e2`.
* M: [marked_braid_holonomy.md](marked_braid_holonomy.md),
  529 lines, SHA256
  `eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f`.

Both complete directs were freshly read nontruncated in this author
sequence, and every used implication was checked. The finite
annihilator, kernel, and ordered Gauss calculations above are written
proofs. Coverage of plat cup constraints was checked separately;
the present ordinary coorientation and source-calibrator application
do not import a plat orientation convention. No mathematical
programs, numerical tests, builds, git operations, or frozen-file
edits were used. The entire matching final was freshly reread
nontruncated, and all three pins renewed before author freeze.
Independent matching-final/direct review and parent adoption are
separate gates.
