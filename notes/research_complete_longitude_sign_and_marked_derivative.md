# Complete longitude sign and the marked meridian derivative

Private research note, 18 November 2026.

For every complete hyperbolic knot exterior in \(S^3\), the preferred
longitude has eigenvalue \(-1\) in **every** lift of the geometric
holonomy to \(\mathrm{SL}_2(\mathbb C)\). This includes the actual
source convention \(\mu=-H\). Consequently the marked logarithmic
action of Q has a nonzero complete meridian derivative. This statement
does not select a geometric contribution of the original period.

The topological sign is classical; the proof below is included in full
to fix its relation to the actual cut flag and quantum character. M
and Q, listed at the end, are the complete proof directs for those
source conventions. No result about a reduced coherent amplitude or
an original integration cycle is used.

## 1. Statement in the actual peripheral convention

Let \(X=S^3\setminus\operatorname{int}\nu K\) be the exterior of a
hyperbolic knot, with its complete oriented hyperbolic structure.
Write \(\mu,\lambda\) for the meridian and preferred longitude, with
\(\lambda\) oriented as in Q. The complete faithful projective holonomy
is denoted \(\bar\rho\), and let \(\rho\) be any of its determinant-one
lifts. Then

\[
\operatorname{tr}\rho(\lambda)=-2,\qquad
\operatorname{spec}\rho(\lambda)=\{-1,-1\}.
\tag{1}
\]

The matrix is noncentral: in a cusp normalization it is
\(-\left(\begin{smallmatrix}1&\tau\\0&1\end{smallmatrix}\right)\)
with \(\tau\ne0\). Reversing the orientation of \(\lambda\) leaves
the sign in (1) unchanged.

In M and Q the actual meridians are \(\mu_j=-H_j\), with trace
\(M+M^{-1}\). The cut's selected flag has meridian eigenvalue
\(M^{-1}\), whereas Q's marked peripheral pair
\((M,\ell_{\mathrm{intr}})\) uses the opposite flag. At \(M=1\)
both flags coalesce, and (1) gives

\[
\ell_{\mathrm{intr}}(1)=-1.
\tag{2}
\]

For any retained logarithmic geometric branch to which Q's action
identity applies, put \(u=\Log M\), \(u=0\) at completeness. Then

\[
\left.\frac{dS_{\mathrm{flat}}}{du}\right|_{u=0}
 =2(2k+1)\pi i\ne0
\quad\text{for some }k\in\mathbb Z.
\tag{3}
\]

This concerns the reduced zero-framed source of Q. Its explicitly
different full ADO gauge must not be substituted without its
meridian factor.

## 2. The frame cover reads the sign of a cusp translation

The orientation-preserving isometry group
\(\mathrm{PSL}_2(\mathbb C)\) acts freely and transitively on the
oriented orthonormal frames of \(\mathbb H^3\): a frame specifies a
base point and an oriented orthonormal basis there, and determines
the isometry carrying a fixed reference frame to it. Thus the frame
bundle of the complete interior of \(X\) is

\[
\mathcal F(X)=
\bar\rho(\pi_1X)\backslash\mathrm{PSL}_2(\mathbb C).
\]

The given lift, rather than an independently chosen spin convention,
provides the double cover

\[
\widetilde{\mathcal F}(X)=
\rho(\pi_1X)\backslash\mathrm{SL}_2(\mathbb C)
\longrightarrow\mathcal F(X).
\tag{4}
\]

There is no \(-I\) in \(\rho(\pi_1X)\): its projection would be the
identity under the faithful projective holonomy. Hence (4) is indeed
a double cover, with deck transformation multiplication by \(-I\).
On a fiber it restricts to
\(\mathrm{SU}(2)\to\mathrm{SO}(3)\). A rotation through angle
\(\theta\) about a fixed axis lifts from \(I\) to
\(\operatorname{diag}(e^{i\theta/2},e^{-i\theta/2})\), after a fixed
conjugation. A full \(2\pi\) rotation therefore has deck sign \(-1\).
Only this elementary property of the frame cover is needed.

Normalize a cusp in the upper half-space model. Its torus is a
quotient of a horizontal horosphere by a lattice of translations.
For a peripheral loop with translation \(a\ne0\), write

\[
n(a)=\begin{pmatrix}1&a\\0&1\end{pmatrix},\qquad
\rho(\gamma)=\epsilon_\gamma n(a),\quad
\epsilon_\gamma\in\{1,-1\}.
\tag{5}
\]

Follow the straight segment representing \(\gamma\), carrying a
frame whose components in the horizontal and vertical directions
are constant. Its frame path is \(n(ta)\), \(0\le t\le1\), up to
one fixed right multiplication. The path starting at \(I\) in the
cover ends at \(n(a)\). In the quotient (4), comparison with the
starting point multiplies this endpoint by
\(\rho(\gamma)^{-1}\), leaving \(\epsilon_\gamma I\).
Consequently

\[
\text{deck sign of the parallel cusp frame along }\gamma
 =\epsilon_\gamma.
\tag{6}
\]

This fixes which of the two unipotent signs is being measured.

## 3. A single Seifert boundary has odd frame monodromy

Choose a connected oriented Seifert surface \(\Sigma\subset X\),
of genus \(g\), whose single boundary is the preferred longitude.
It can be obtained by smoothing an oriented knot diagram, spanning
the resulting Seifert circles by disks, attaching the crossing
bands, and taking the connected component with knot boundary.
Near the cusp torus, isotope its boundary to the straight
longitude slope and choose the surface collar to run in the
inward horospherical normal direction. This changes no slope or
peripheral word.

The oriented tangent bundle of \(\Sigma\) has a global oriented
frame. One direct construction uses a disk with \(2g\) attached
one-handles: equivalently it is a thickening of a graph. Choose
frames over the vertices, extend along its edges using the
connectedness of the oriented frame group, then across the
thickening. Applying Gram--Schmidt gives an orthonormal frame
\((e_1,e_2)\). Append the oriented surface normal \(n_\Sigma\)
to obtain a section \(b=(e_1,e_2,n_\Sigma)\) of \(\mathcal F(X)\)
over \(\Sigma\).

Pulling (4) back along \(b\) gives a double cover of \(\Sigma\).
Its monodromy is a homomorphism
\(\pi_1\Sigma\to\{1,-1\}\). The oriented boundary is the product
of the \(g\) handle commutators, so its monodromy in this abelian
group is \(+1\). This holds for every cover (4), without choosing
a distinguished spin structure on \(\Sigma\).

Let \(t\) be the positively oriented unit tangent to
\(\partial\Sigma\), and \(v\) the inward unit tangent normal to
the boundary within \(\Sigma\). Then
\((t,v,n_\Sigma)\) is a positive frame. Its first two vectors
rotate relative to \((e_1,e_2)\) by a map of degree

\[
\deg_{\partial\Sigma}(t,v)=1-2g=\chi(\Sigma).
\tag{7}
\]

For clarity, the turning count in (7) has the following elementary
index proof. On the disk-and-handles presentation choose a tangent
field outward along the boundary, with one disk zero of index \(+1\)
and one saddle of index \(-1\) in each of the \(2g\) handles.
Such a field is obtained from a handle height function: near the
disk zero use its radial gradient and near a handle saddle use
\((x,-y)\); its nonsingular collar fields match the attaching
strips and the final outward boundary. Remove small disks around
the zeros and express its normalized direction in the fixed frame
\((e_1,e_2)\). This is a map to the circle, so the sum of its
oriented boundary degrees is zero. Therefore its degree on the
outer boundary is the sum of its local indices, \(1-2g\).
Changing outward normal to the boundary tangent is a fixed
quarter-turn in the oriented tangent plane and leaves that degree
unchanged. Changing the global tangent frame also leaves it
unchanged: the change is a map \(\Sigma\to\mathrm{SO}(2)\), whose
degree on the single boundary is zero.

The relative frame rotation in (7) is a loop in the
\(\mathrm{SO}(2)\) subgroup of \(\mathrm{SO}(3)\). Section 2 shows
that its lifted sign is \((-1)^{1-2g}=-1\). The background frame
\(b\) has sign \(+1\) along the boundary. Hence the adapted boundary
frame has sign

\[
\operatorname{mon}_{\partial\Sigma}(t,v,n_\Sigma)=-1.
\tag{8}
\]

Finally, on the collar chosen above, \(t\) is the constant
horizontal longitude direction, \(v\) is the inward vertical
direction, and \(n_\Sigma\) is the corresponding constant
horizontal perpendicular direction. Thus this adapted frame
differs from the parallel cusp frame in Section 2 by a **fixed**
rotation, not by an unrecorded loop of rotations. Equations
(6) and (8) prove \(\epsilon_\lambda=-1\), and hence (1).
Faithfulness makes its cusp translation nonzero.

This proof uses the existence of the actual determinant-one lift,
not a theorem asserting a preferred lift. In particular it also
proves lift independence directly. Alternatively, two lifts
differ by a character \(\pi_1X\to\{1,-1\}\), and every such
character is trivial on the boundary of \(\Sigma\).

## 4. The actual word, opposite flag, and logarithmic character

M proves that the source's classical meridians are
\(\mu_j=-H_j\), and that the selected cut vector has
\(M^{-1}\)-eigenvalue. Q supplies the sign-sensitive word adapter,
which we recall to avoid replacing an eigenvalue by its square.
If \(W\) is its left-ordered underpass transport and \(w\) the
writhe, the preferred word and the selected-flag eigenvalue are

\[
\lambda=W^{-1}\mu^{-w},\qquad
\lambda|_{\text{cut flag}}
 =(-1)^c M^w T_{\mathrm{over}}
 =\ell_{\mathrm{intr}}^{-1}.
\tag{9}
\]

Here \(c\equiv w\pmod2\), and Q's exact integer-position
telescoping fixes the displayed sign. On the other flag the
eigenvalues are \((M,\ell_{\mathrm{intr}})\). At completeness
the longitude eigenvalue in (1) is its own inverse, so (9)
proves (2) without a Weyl ambiguity.

The convention \(\mu=-H\) is also harmless for (1): multiplying
every knot meridian by \(-1\) is the mod-two meridian character.
The preferred longitude has zero meridian exponent and is the
boundary of \(\Sigma\), so that character is \(+1\) on it.
No analogous assertion is made for a blackboard longitude
before the writhe correction.

Q derives, for the actual coefficient action after its recorded
internal Fourier correction,

\[
dS_{\mathrm{flat}}
 =2\Log\ell_{\mathrm{intr}}\,d\Log M.
\tag{10}
\]

A local logarithm of a nonzero holomorphic eigenvalue exists near
the complete point on the specified augmented/logarithmic branch.
By (2) its value is \((2k+1)\pi i\). Substitution into (10) proves
(3), and \(d/du=d/dM\) at \(M=1\). This is independent of the
orientation of the geometric representation and of which odd
logarithm was retained. It does not set that integer \(k\).

The distinction from a centered action is exact. Put
\(v_0=(2k+1)\pi i\). Subtracting \(2v_0u\) would change the
phase exponential, at \(h=2\pi i/N\), by

\[
\exp(-2v_0u/h)=M^{-(2k+1)N}.
\tag{11}
\]

Its value at \(M=1\) is one, but its first meridian derivative
there is \(-(2k+1)N\). Thus centering the longitude logarithm
removes a first-jet term of precisely the scale at issue. It is
an explicit meridian character, not one of Q's internal lattice
characters that equal one on every state throughout the meridian
germ. Likewise Q's full ADO gauge changes the classical shift
sign; that distinct exact source is not used to alter (10).

## 5. Consequence and limits for a local first jet

The exact phase identity implied by (3) is

\[
\left.\partial_M e^{S_{\mathrm{flat}}(M)/h}\right|_{M=1}
 =(2k+1)N\,e^{S_{\mathrm{flat}}(1)/h}.
\tag{12}
\]

If a separately justified local contribution has the form
\(I_N(M)=N^\alpha a_N(M)e^{S_{\mathrm{flat}}(M)/h}\), with
\(a_N(1)\to a_0\ne0\) and
\(\partial_M a_N(1)=o(N)\), then its first jet satisfies

\[
\partial_M I_N(1)
 =N^{\alpha+1}e^{S_{\mathrm{flat}}(1)/h}
   \bigl((2k+1)a_0+o(1)\bigr).
\tag{13}
\]

This follows by the product rule. In particular no
first-derivative cancellation occurs **within such a supplied
marked local phase/amplitude term**. The hypotheses of (13)
are not asserted for the original source, a reduced \(B_0\)
trace, or a Weyl-paired sum. Relating any of those sources to
this same marked action must retain its boundary terms and
meridian characters. Their cycle coefficients and possible
cancellation remain separate.

There are no exceptions to (1) among complete hyperbolic knots
in \(S^3\). The proof also works whenever the specified primitive
cusp curve bounds a connected orientable surface with that
single boundary. It does not assert the same sign for arbitrary
peripheral slopes, multiboundary link surfaces, nongeometric
representations, or a longitude that has been multiplied by a
central sign as part of a different quantum normalization.

## 6. Coverage and complete proof directs

The classical longitude-trace fact is already recorded in
[Calegari, *Real places and torus bundles*, §2](https://arxiv.org/abs/math/0510416).
This is coverage only. Sections 2--3 above prove the needed sign
from the frame cover and the Seifert boundary, rather than
importing that paper's Euler-class proof.

The complete source directs, read in full for this note, are:

* **M:** notes/marked_braid_holonomy.md, SHA256
  eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.
  Its actual meridian matrices, selected flag, and critical
  representation convention are used.
* **Q:** notes/quantum_longitude_and_regulator_action.md, SHA256
  e8ac5dc6bab05be0dad3810311dc3a8b169ad810b898aa3db75582087dbe8aa7.
  Its exact preferred-word/flag identification, internal Fourier
  correction, marked action differential, and distinct full ADO
  gauge are used.

No fundamental-cycle or volume comparison is needed for this
sign and derivative theorem. No numerical experiment is a premise.
