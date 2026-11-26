# Geometric composition of rooted pieces with one free circle

Research note, 2 November 2026. A rooted piece here is an actual
partially filled ordered circle-tree region with one remaining
auxiliary boundary circle. All its other auxiliary circles have
their original fixed signed fillings. The main link cusps remain
complete. This note proves an inductive geometric statement:
joining such pieces to a new circle and retaining one outgoing
edge preserves the same marked boundary structure, provided the
new cone branch stays in their common parameter disk.

The small-branch hypothesis and the full finite-source estimates
must be proved separately. The result below does not infer
asymptotic stability from geometric composition.

## 1. The uniform data retained for each piece

Fix a disk \(D_r=\{u:|u|<r\}\). Each eligible piece \(B\)
has a separately even holomorphic phase \(W_B(u)\), a
positive marked cell and filled-tube realization on \(D_r\),
and the following properties.

* Its remaining interface has the original two-triangle
  ratio tables
  \[
       (-Q^{-1},-Q,-Q^{-1}),\quad
       (-Q,-Q^{-1},-Q),\qquad Q=e^{iu}.
       \tag{1}
  \]
* Its pure peripheral logarithms are
  \[
                    U_B=-2\pi W_B'(u),\qquad V_B=2iu.
                    \tag{2}
  \]
  The carrier of this still free original circle has not
  been inserted into \(W_B\).
* All its already filled primitive meridian periods are
  fixed at their original \(2\pi\) values, their core
  lengths are positive on \(D_r\), and their winding
  numbers are those of the original marked completion.
* Its complete-boundary volume is \(2\pi\Re W_B(0)\),
  and
  \[
                     -\Re W_B''(u)\ge a>0
                                      \quad (u\in D_r).
                     \tag{3}
  \]

These conditions hold for the terminal pieces of every
power \(|p|\ge2\) on one common disk, as proved in Section 6 of
[the common-block geometry note](research_amplified_marked_block_geometry.md).
The small core lengths at large \(|p|\) do not violate
the common-disk assertion.

Choose \(r\) small enough that the original edge phase
\(\psi(t,u)\) has its full positive marked realization
on \(D_r^2\), with
\[
                     -\Re\psi''(t,u)\succeq a_e I_2,
                     \qquad a_e>0.
                     \tag{4}
\]
Here the real part of a complex symmetric matrix is its
Hermitian part, which in this case is the entrywise real
matrix. Such a fixed \(r\) exists because at \((0,0)\)
the left side is \((2\pi)^{-1}I_2\).
Take \(a\le a_e\).

## 2. One actual composition

Let \(B_1,\ldots,B_m\) be eligible pieces. Attach their
distinguished sectors at one new original circle \(v\),
and attach one original unfilled edge from \(v\) to
the remaining outside circle. Thus \(v\) has exactly
these \(m+1\) incidences. Write \(t\) for its angle
and \(u\) for the outside angle.

The operation uses the prescribed cyclic order and the
entire interface maps (1). After cutting the reference
tori along their original disk longitudes, their annular
sectors join into the original torus at \(v\). Its
meridian traverses all sectors once and its longitude
is one common primitive longitude. It is not multiplied
by \(m+1\).

Put
\[
             P(t,u)=\sum_{j=1}^m W_{B_j}(t)+\psi(t,u).
             \tag{5}
\]
If \(\eta_v\) is its original carrier and \(p_v\) its
integer filling coefficient, the original signed power
is \(n=\eta_v-2p_v\). Insert this carrier once at \(v\).
Its primitive periods then satisfy
\[
 U_v=-2\pi P_t-i\eta_vt,\quad V_v=2it,\qquad
 U_v+p_vV_v=-2\pi\left(P_t+\frac{in}{2\pi}t\right).
 \tag{6}
\]
No carrier is inserted yet at the outside circle.

Assume that the branch through \(t=0\) solving
\[
                  P_t(t,u)+\frac{in}{2\pi}t=ic,
                      \qquad 0\le c\le1,
                  \tag{7}
\]
exists on all of \(D_r\), and remains in a fixed smaller
central disk \(|t|<r_0<r\).
For example the analytic composition argument may
give \(|t(c,u)|\le C/m<r_0\), uniformly in the fixed
signed power \(n\).

**Proposition 1.** Under this small-branch hypothesis,
the new filled piece has the actual original marked
geometry on \(D_r\). All the older fillings stay smooth,
and at \(c=1\) the new primitive filling is smooth.
Its one remaining boundary has the same interface (1)
and primitive basis (2).

**Proof.** Every child is evaluated at \(t(c,u)\in D_r\),
so its full positive geometry, its filled cores and all
its marked maps remain valid. The new edge is positive
by the choice of \(r\). Equation (1) glues the complete
triangle maps, including their translations and shears.
Equation (6) is the prescribed new primitive period,
not merely the exponentiated holonomy relation.

It remains to check the sign of the new core. At
charge zero, evenness gives \(t=0\), and
\[
 \partial_ct(0,u)=
       \frac{i}{P_{tt}(0,u)+in/(2\pi)}.
 \]
The denominator has strictly negative real part by
(3)--(4), so \(\Im\partial_ct(0,u)<0\), including
for complex \(u\in D_r\). If the branch later met
the real \(t\)-axis at positive \(c\), the real part
of (7) would require \(\Re P_t(t,u)=0\). For real
\(t\), this function vanishes at zero and has
strictly negative derivative throughout the small
chart, again by (3)--(4). Therefore its only zero
is \(t=0\), which contradicts (7) when \(c>0\).
Hence \(-2\Im t(c,u)>0\).

The central meridian winding starts at the original
cusp marking and is unchanged along the positive
branch. At \(c=1\), (6) gives its full period
\(-2\pi i\), so the completion is the smooth marked
filled tube. Each child already holds all its old
primitive slopes fixed and its old core lengths
positive at every parameter in \(D_r\). No lower
bound for those lengths independent of the child
is needed.

The outside circle belongs only to the remaining
bare edge. Its triangle maps are (1); its disk
longitude remains \(V=2iu\). The main-cusp
parabolic identities are those of the children
and the original edge and continue under their
actual face identifications. \(\square\)

## 3. The new phase and its uniform curvature

The boundary phase of the new piece is
\[
 W_{\rm new}(u)
   =\operatorname{stat}_t
       \left[P(t,u)+\frac{in}{4\pi}t^2-it\right].
       \tag{8}
\]
It is even in \(u\), and the envelope rule gives
\[
                       W_{\rm new}'(u)=\psi_u(t(u),u).
                       \tag{9}
\]
At the outside boundary the old pure-period calculation
therefore yields exactly
\[
                      U=-2\pi W_{\rm new}'(u),\qquad V=2iu.
                      \tag{10}
\]
The absence of a child derivative in (9) expresses the
actual fact that the outside circle belongs to the one
remaining bare edge.

There is a useful exact estimate with no loss of
boundary radius. Define
\[
 H=
 -\begin{pmatrix}
   \sum_jW_{B_j}''(t)+\psi_{tt}(t,u)+in/(2\pi)&\psi_{tu}(t,u)\\
   \psi_{ut}(t,u)&\psi_{uu}(t,u)
  \end{pmatrix}
   =\begin{pmatrix}H_{11}&H_{12}\\H_{21}&H_{22}\end{pmatrix}.
 \tag{11}
\]
The chirp contributes nothing to its Hermitian real
part. Equations (3)--(4) imply
\[
                 \Re H\succeq
                    \begin{pmatrix}ma&0\\0&0\end{pmatrix}
                         +a_eI_2.
                         \tag{12}
\]
In particular \(H_{11}\ne0\), and differentiation of
(7) gives the exact Schur complement
\[
                -W_{\rm new}''
                  =H_{22}-H_{21}H_{11}^{-1}H_{12}.
                  \tag{13}
\]
For \(z=(-H_{11}^{-1}H_{12},1)^T\), the first
component of \(Hz\) is zero. Consequently
\[
 \Re(-W_{\rm new}'')
      =\Re(z^*Hz)
      \ge a_e\|z\|^2+ma|z_1|^2
      \ge a_e\ge a .
 \tag{14}
\]
Thus the same real-curvature constant holds on
the same disk \(D_r\), regardless of the number
of children, the depth of their constructions,
or any of their signed filling powers.

This does not by itself give uniform bounds on every
higher derivative or on quantum amplitudes. Those
are additional parts of a recursive source theorem.
It does remove a possible geometric loss of radius
or real curvature at every new level.

## 4. Absolute volume and iteration

At \(u=0,c=0\), the children and the bare edge glue
with the new central cusp still complete. Their
volumes add:
\[
          \operatorname{Vol}_{c=0}
               =2\pi\Re\left(\sum_jW_{B_j}(0)+\psi(0,0)\right).
               \tag{15}
\]
For the charge path define
\[
 S(c)=P(t(c,0),0)+\frac{in}{4\pi}t(c,0)^2-ic\,t(c,0).
 \]
Stationarity gives \(d\Re S/dc=\Im t(c,0)\). Every
old core angle stays fixed at \(2\pi\); only the
new central angle \(2\pi c\) varies. Schläfli's
formula and (15) yield
\[
                 \operatorname{Vol}(B_{\rm new},u=0)
                         =2\pi\Re W_{\rm new}(0).
                         \tag{16}
\]
Thus the absolute normalization required in Section 1
also closes. Exact imaginary source constants and
unit framing factors are retained separately; they
are not discarded when adding the calibrated phases.

**Corollary 2.** Suppose a fixed branching threshold
ensures the small-branch hypothesis (7), on one
common disk, for every new vertex formed from the
eligible rooted pieces. Then every finite recursively
formed rooted tree has the marked positive geometry,
pure peripheral response, positive old core lengths,
uniform real curvature, and absolute volume
normalization described above. These conclusions do
not require a bound on its depth.

The proof is induction using Propositions 1 and
(14)--(16). In particular, an old terminal core whose
length is arbitrarily small is not subjected to a
new independent perturbation estimate at every
level. Its immediate parent's parameter lies in
the disk on which that entire child's geometric
construction was already proved.

At the final root omit the outgoing bare edge and
close the original central circle with its chosen
fixed power. The same marked annular argument and
small-cone-path proof apply. After that filling,
only the original main cusps remain. If the original
component tracing gives a knot, the calibrated
geometric volume is its knot-complement volume.
An accompanying theorem for the full coherent
source is still required to deduce its volume
conjecture. The geometric induction alone makes
no such asymptotic assertion.
