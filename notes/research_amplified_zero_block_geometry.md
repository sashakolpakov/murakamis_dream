# Primitive geometry after many zero-filled blocks meet one circle

Research note, 2 November 2026. A fixed zero-filled Conway block has
a positive geometric deformation for small boundary angles. When
many copies meet one original crossing circle, their meridian
increments add. The primitive longitude is still traversed once.
This identifies the small critical point of the amplified source
with the original signed filling, uniformly over its integer power.

The input concerning the critical point is the bound proved in the
companion source argument. The geometric assertions below follow
from the already established zero-subtree Conway construction.
No positivity hypothesis about the former, possibly folded
two-octahedron subdivision is introduced.

## 1. The fixed block and its original boundary curves

Let \(\mathcal B\) be one of the actual all-zero subtree pieces in
[the zero-subtree boundary theorem](research_all_zero_subtree_newton_packet.md)
and
[its marked Conway geometry](research_zero_subtree_conway_geometry.md).
Its selected original vertices have degree at least three.
Distinguish one free boundary circle, with angle \(t\), and write
\(\mathbf u\) for its other free boundary angles. Its carrier-free
source phase is
\[
                            W(t,\mathbf u).
 \tag{1}
\]

The cited geometric construction proves the following facts,
which fix the meaning of this phase.

- Literal deletion of the selected zero boxes gives a strict
  Conway decomposition of the same marked partially filled parent.
- Its complete cells are positive, its complete volume is
  \(2\pi W(0,\mathbf0)\), and their full face maps continue
  holomorphically for small complex boundary angles.
- On every free reference circle the pure logarithmic periods are
  \(U=-2\pi W_t\), \(V=2it\), in its original meridian and disk
  longitude. Corresponding formulas hold for the other variables.
- The phase is real on small real boundary angles and separately
  even in every boundary variable. At completeness its boundary
  Hessian is diagonal and strictly negative:
  \[
                     W_{tt}(0,\mathbf0)=-\lambda,\qquad \lambda>0.
  \tag{2}
  \]

In particular one can choose a radius \(\rho>0\), depending only
on the fixed block, such that \(|t|\le\rho\), \(\mathbf u=0\)
lies in this positive marked cell chart and
\[
                         \Re W_{tt}(t,\mathbf0)<-\lambda/2.
 \tag{3}
\]
Shrink \(\rho\) if necessary so that, for real \(|t|\le\rho\),
\(W_t(t,\mathbf0)=0\) only at \(t=0\). This last assertion also
follows directly from the real version of (3).

## 2. Gluing the copies before filling the common circle

Take \(m\) copies of \(\mathcal B\) and identify their distinguished
reference-circle sectors in the original cyclic order at one
original crossing circle \(v\). Their other boundary variables
remain independent for now. The prescribed interface maps in
Section 5 of the Conway geometry note are
\[
 (-Q^{-1},-Q,-Q^{-1}),\qquad
 (-Q,-Q^{-1},-Q),\qquad Q=e^{it},
 \tag{4}
\]
on their ordered edges. They depend on the common boundary angle,
not on the internal Newton coordinates of a particular copy.
The incoming and outgoing maps therefore agree as complete
labelled triangle maps, including their translations and shears.

Topologically each reference torus was cut along its primitive
disk longitude. Cyclically joining these annular sectors restores
one original torus. Their common longitude is its original
longitude, while the meridian crosses all sectors once.
The pure periods at \(v\) are consequently
\[
              U_v=-2\pi\sum_{j=1}^m W_t(t,\mathbf u_j),
              \qquad V_v=2it.
 \tag{5}
\]
The second formula is not \(2mit\). This is the original
intersection-one peripheral basis, not a cover of it.

At \(t=\mathbf u_j=0\), the canonical unit horocyclic decorations
on the shaded triangles match under (4). Thus the sectors give
complete auxiliary cusp tori with no dilation. The main cusps
are those of the same strict Conway pieces, and remain complete.
The resulting parent has complete volume
\[
                           2\pi mW(0,\mathbf0).
 \tag{6}
\]
If fixed additional pieces are attached elsewhere, their complete
volumes are added to (6); they are not counted again in \(W\).

An original retained carrier \(\eta\in\{-1,0,1\}\) contributes
once at the distinguished disk seam. For the original integer
filling coefficient \(p\), put \(n=\eta-2p\). The actual periods are
\[
 U_v=-2\pi\sum_jW_t(t,\mathbf u_j)-i\eta t,\qquad V_v=2it,
\]
\[
 U_v+pV_v
       =-2\pi\left(\sum_jW_t(t,\mathbf u_j)
                                      +\frac{in}{2\pi}t\right).
 \tag{7}
\]
No carrier term is inserted separately in each copy.

## 3. The central cone path

Set all \(\mathbf u_j=0\), and prescribe central cone charge
\(c\in[0,1]\). The original stationary equation is
\[
             mW_t(t,\mathbf0)+\frac{in}{2\pi}t=ic.
 \tag{8}
\]

Suppose the companion analytic construction supplies its branch
through \(t(0)=0\), with the uniform estimate
\[
 |t(c)|\le
 \frac7{\sqrt{(2\pi m\lambda)^2+n^2}}
                           \qquad(0\le c\le1).
 \tag{9}
\]
Choose \(m\) above that construction's threshold and also large
enough that
\[
                              \frac7{2\pi m\lambda}<\rho.
 \tag{10}
\]
The extra geometric threshold depends only on the fixed block
and is independent of the signed integer \(n\).

**Theorem 1.** Under (9)--(10), the entire branch (8) is the
positive marked cone deformation of the parent in Section 2
along its original primitive slope. At \(c=1\) it gives the
smooth central filling. All other free cusps remain complete.

**Proof.** Bound (9) puts each copy inside its already proved
positive cell chart. The full interface identities (4) glue
these copies for every value of \(c\). All interior edge
relations are the original rational face identities; their
integer angle windings remain those at the complete end
because no positive tetrahedron or face chart degenerates.
The actual small logarithmic periods are therefore (7).
Equation (8) gives
\[
                            U_v+pV_v=-2\pi i c.
 \tag{11}
\]

The core length is positive for \(c>0\). To see its sign
without assuming it from a formal saddle, differentiation
at zero gives
\[
 t'(0)=\frac{i}{-m\lambda+in/(2\pi)},\qquad
 \Im t'(0)=
       -\frac{m\lambda}{(m\lambda)^2+(n/(2\pi))^2}<0.
 \tag{12}
\]
A later crossing of the real axis would give a real \(t\)
satisfying (8). Its real part would force
\(W_t(t,\mathbf0)=0\), hence \(t=0\) by the choice of
\(\rho\), which contradicts \(c>0\). Thus
\(\Im t(c)<0\) throughout the positive-charge interval,
and the primitive core length is
\[
                              \ell(c)=-2\Im t(c)>0.
 \tag{13}
\]

At another free boundary angle \(u\), separate evenness
gives \(W_u(t,\mathbf0)=0\). Its longitude is zero as well,
and a retained carrier contributes zero at \(u=0\).
Those full peripheral periods remain complete. The
main-puncture products and complete cusp matching are
the ones in the marked Conway deformation. The positive
cells therefore give the asserted cone metric, with
angle \(2\pi c\). At \(c=1\), (11) fills the original
primitive slope with angle \(2\pi\). \(\square\)

## 4. Absolute action and volume

Let
\[
 S_m(c)=mW(t(c),\mathbf0)
                  +\frac{in}{4\pi}t(c)^2-ic\,t(c).
 \tag{14}
\]
Stationarity in (8) gives
\[
                          \frac{d}{dc}\Re S_m(c)=\Im t(c).
 \tag{15}
\]
Schläfli's formula along the same primitive cone path gives
\[
 \frac{d}{dc}\operatorname{Vol}
       =-\frac12\ell(c)\,\frac{d(2\pi c)}{dc}
       =2\pi\Im t(c).
 \tag{16}
\]
The complete value (6) agrees with \(2\pi S_m(0)\).
Consequently the central filled parent has volume
\[
          2\pi\Re\left[
           mW(t(1),\mathbf0)
                +\frac{in}{4\pi}t(1)^2-it(1)\right].
 \tag{17}
\]

This is an absolute volume identity for the stated geometric
configuration. It uses the positive replacement after literal
zero deletion, so it does not continue through a degenerate
original eight-tetrahedron chart or assign its corner
subgradients a geometric meaning.

## 5. Remaining small boundary deformations

The central critical point continues holomorphically when
the other boundary angles are small. Its internal
derivative is
\[
              \sum_jW_{tt}(t,\mathbf u_j)+\frac{in}{2\pi}.
 \tag{18}
\]
At \(\mathbf u_j=0\) its real part is less than
\(-m\lambda/2\), by (3), so it is nonzero.
The implicit-function theorem applies with the original
central primitive period held fixed.

At zero outside angles, separate evenness gives
\(W_{tu_k}(t,\mathbf0)=0\). Thus the Schur-complement
correction to the outside Hessian vanishes there.
Its entries are the sums of the corresponding
\(W_{u_k u_l}(t,\mathbf0)\) from the actual copies.
They are diagonal when the outside variables are kept
independent, and have strictly negative real diagonal
entries after a further fixed shrinking of \(\rho\).
Identifying outside circles adds their incidence
contributions, with their own carrier added once.

The full face maps and positive chains also continue in
these small boundary variables. Hence this geometry is
available for the subsequent long-filling assembly once
the companion source theorem supplies its required
boundary estimates. This note establishes the geometric
identification and normalization; it does not replace
the coherent source estimate or its nonzero leading
coefficient.
