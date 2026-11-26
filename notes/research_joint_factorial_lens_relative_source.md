# Joint factorial lenses for the original finite source

Private written proof, 15 November 2026.

The restored Newton network has an exact joint integral in its wire
indices and angular variables. This note places that integral on
lower angular lenses in a common holomorphic factorial domain. It
also gives an explicit relative primitive for the difference between
the factorial and finite-band polynomial representatives. Thus
compact joint deformations with the specified coordinate faces fixed
preserve the full original source. No edge kernel is replaced by a
single asymptotic branch.

The result does not establish the geometric coefficient or an
exponential bound on the remainder of such a joint contour.

## 1. Original source and the common domain

Fix \(N\ge2\), \(D=N-1\), \(\eta=(-1)^D\), and
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f .
 \tag{1}
\]
Use the original Newton polynomials \(e_j\), physical crossing \(R\),
and kernels
\[
 K_T(z,w)=\sum_{j=0}^D e_j(z)e_j(w),\qquad
 K_I(z,w)=\sum_{j=0}^D e_j(z)e_{D-j}(w).
 \tag{2}
\]
Take any finite network compiled from these operations as in the
pinned source compiler. Let \(V\) be its traced vertices and \(E\)
its paired wire indices. Loops and repeated edges are permitted.
Every wire index occurs in precisely two halfwire factors. Each
halfwire uses either \(x_e\) or \(D/N-x_e\), according to its
original direct or reversed index. Free spectral variables are
ordinary polynomial variables and are not reduced.

At a traced vertex \(v\), allow any fixed signed power \(R^{n_v}\)
and the canonical full-Hermite coupon \(\mathcal C_{N,\chi_v}\)
of the pinned lens theorem. Here \(\chi_v\) may be complex; its
value at \(z=-2\cos t\) is represented by
\(\cos(N(1-\chi_v)t)\), with its prescribed first normals.
The original source is recovered when every \(\chi_v=1\).
Any additional specified polynomial spectators are retained.

Write
\[
 \begin{split}
 B_N(x,t)&=\frac{N}{
 G_N(D/2-Nx+Nt/(2\pi))G_N(D/2-Nx-Nt/(2\pi))G_N(Nx)^2},\\
 \widetilde B_N(x,z)&=\sum_{j=0}^D
       \frac{\sin(\pi N(x-j/N))}{N\sin(\pi(x-j/N))}\,e_j(z).
 \end{split}
 \tag{3}
\]
The removable values in the second line are used. Its frequencies
in \(x\) are \(-D/2,-D/2+1,\ldots,D/2\). The full Hermite class
of \(B_N(x,t)\), with \(z=-2\cos t\), equals that of
\(\widetilde B_N(x,z)\). At \(x=j/N\), both equal \(e_j(z)\)
as an ordinary polynomial identity.

Put
\[
 a_N=\pi-\frac{\pi}{2N},\qquad
 I_N=[-1/(2N),\,1-1/(2N)] .
 \tag{4}
\]
Use \(\Re x_e\in I_N\) and \(|\Re t_v|\le a_N\).
The compiler's direct divisor check applies simultaneously to
both halfwire orientations: the two shifted factorial arguments
in (3) have real parts in
\[
 [-N+1/4,\,N-1/4],\qquad
                 \Re(Nx_e)\in[-1/2,N-1/2].
 \tag{5}
\]
Consequently all factorial halfwires are holomorphic on a
neighborhood of any compact subset of this product strip,
at arbitrary fixed finite imaginary heights. The reflection
\(x\mapsto D/N-x\) preserves \(I_N\).

At a free spectral endpoint use \(\widetilde B_N(x,z)\), not
\(B_N(x,t)\). This distinction preserves the entire boundary
polynomial. At traced endpoints either representative is allowed.

## 2. A full-grid lens inside the factorial domain

Set
\[
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2},\qquad
 C_{N,n}=q^{nD^2/4},\qquad q=e^{\pi i/N}.
 \tag{6}
\]
The physical grid is
\(\tau_j=\pi-(2j+1)\pi/N\), \(0\le j\le D\).
All these points lie strictly between \(-a_N\) and \(a_N\);
neither endpoint is a pole of \(W_N\).

Let \(A(t)\) be even and holomorphic on a vertical strip containing
\([-a_N,a_N]\), and let \([A]\) denote its full spectral Hermite
class. This class exists because an even function near \(t=0\)
is holomorphic in \(z=-2\cos t\) there; elsewhere the physical
angular-to-spectral map is unramified. If \(\Gamma\) runs from
\(-a_N\) to \(a_N\), with interior in the lower half-plane and
inside that strip, then
\[
 \boxed{\quad
 \phi_N(R^n\mathcal C_{N,\chi}[A])
 =-\frac{N^2C_{N,n}}{\pi i}
   \int_\Gamma
   \sin t\,e^{inNt^2/(4\pi)}
        \cos(N(1-\chi)t)A(t)W_N(t)\,dt .
 \quad}
 \tag{7}
\]

Indeed the numerator other than \(W_N\) is odd, and \(W_N\) is
even. Adjoin the reflected upper arc \(-\Gamma\) to form the
positively oriented lens around the entire physical grid.
The exact derivative-sampling residue calculation of the lens
theorem gives (7), with the two reflected integrals equal.
Only evenness and holomorphy of \(A\), and its physical values
and first normals, are used. It need not be a polynomial.
The odd-level simple spectral node at \(t=0\) has precisely its
original contribution; no extra normal is imposed.

Unlike the endpoints \(\pm\pi\), the present endpoints need not
annihilate the sine factor. Short endpoint connectors are therefore
generally \(O_N(\varepsilon)\), which still tends to zero at fixed
\(N\). There is no endpoint residue or half-weight. No uniform
large-\(N\) connector estimate is asserted.

## 3. The exact joint integral

Fix horizontal wire intervals \(I_N+i h_e\) and lower angular
arcs \(\Gamma_v:-a_N\to a_N\) as above. Let \(d=|E|+|V|\),
and order the complex coordinates once and for all.

Let \(F_{\rm car}\) be the product of all halfwire factors, using
\(\widetilde B_N(x,-2\cos t)\) at traced endpoints and the same
polynomial representative at every free endpoint. Retain the
specified polynomial spectators in this product. Let \(F_{\rm fac}\)
replace the traced halfwires by (3), with their actual direct or
reversed arguments; the free endpoints remain polynomial.
Both functions are even in every angular coordinate.

Define the two top forms, with the same chosen coordinate order, by
\[
 \Omega_\bullet=
 F_\bullet(\mathbf x,\mathbf t;\mathbf u)
 \prod_{v\in V}
 \left\{\sin t_v\,W_N(t_v)
       e^{in_vNt_v^2/(4\pi)}
       \cos(N(1-\chi_v)t_v)\right\}
 \,d\mathbf x\,d\mathbf t ,
 \qquad \bullet\in\{{\rm car},{\rm fac}\}.
 \tag{8}
\]
Here \(\mathbf u\) denotes all unreduced free spectral variables.
For the product chain
\(\mathcal L=\prod_e(I_N+i h_e)\times\prod_v\Gamma_v\),
the exact compiled source is
\[
 \boxed{\quad
 Z_N(\mathbf u)=
 N^{|E|}\prod_{v\in V}
       \left(-\frac{N^2C_{N,n_v}}{\pi i}\right)
                  \int_{\mathcal L}\Omega_{\rm fac}
 =
 N^{|E|}\prod_{v\in V}
       \left(-\frac{N^2C_{N,n_v}}{\pi i}\right)
                  \int_{\mathcal L}\Omega_{\rm car}.
 \quad}
 \tag{9}
\]

For the cardinal representative, each paired index has integer
frequencies in \([-D,D]\), so its original \(N\)-point sum is
exactly \(N\) times the period integral. Apply (7) at every
traced vertex. This proves the second expression in (9).
The factorial expression follows either by equality of every
full Hermite trace, or by the explicit relative identity below.
All integrations are over compact chains, and all free-variable
coefficients remain unchanged. Thus (9) also holds after any
finite number of free-boundary derivatives.

## 4. The relative primitive of the representative correction

The exact identity
\[
 \boxed{\quad P_N(-2\cos t)\,W_N(t)=(-1)^N \quad}
 \tag{10}
\]
follows by expanding
\[
 P_N(-2\cos t)
       =(-1)^N e^{iNt}(1-\eta e^{-iNt})^2 .
 \tag{11}
\]
It retains both parities and every repeated root.

Telescope the replacement \(F_{\rm car}\to F_{\rm fac}\) one
traced vertex at a time. The difference at vertex \(v\) is
divisible by \(P_N(-2\cos t_v)\), so
\[
 F_{\rm fac}-F_{\rm car}
       =\sum_{v\in V}P_N(-2\cos t_v)A_v(\mathbf x,\mathbf t;\mathbf u),
 \tag{12}
\]
where each \(A_v\) is jointly holomorphic in the common product
strip and even in every angular variable.

To verify holomorphic division, at a paired angular root the
full-Hermite identity gives value and first angular derivative
zero, matching the double zero of \(P_N(-2\cos t)\).
When \(N\) is odd, its simple spectral root \(-2\) pulls back
to a double angular zero at \(t=0\); evenness and value equality
give that same order. There are no further zeros of \(P_N\)
inside the angular strip. The quotient consequently has no
pole there, including at \(N=2\).

After multiplying the \(v\)-th summand of (12) by the factors
in (8), use (10). The resulting top-form coefficient is
holomorphic in \(t_v\), odd in \(t_v\), and may retain only
the original \(W_N(t_w)\) poles in the other variables.
Write that coefficient as \(H_v\). Define its primitive by
\[
 Q_v(\mathbf x,\mathbf t;\mathbf u)
       =\int_{-a_N}^{t_v}
          H_v(\mathbf x,t_1,\ldots,\tau,\ldots;\mathbf u)\,d\tau .
 \tag{13}
\]
The integration in the \(v\)-th strip is path independent:
its coefficient is holomorphic there, including at the
physical nodes. It is holomorphic in all remaining variables
off their original angular poles. Oddness gives
\[
                 Q_v|_{t_v=-a_N}=Q_v|_{t_v=a_N}=0 .
 \tag{14}
\]

If \(t_v\) is coordinate number \(j(v)\), let
\(\Theta_v=(-1)^{j(v)-1}Q_v\) times the ordered wedge of all
coordinate differentials except \(dt_v\). Then
\[
 \boxed{\qquad
       \Omega_{\rm fac}-\Omega_{\rm car}=d\Theta,\qquad
                         \Theta=\sum_v\Theta_v .
 \qquad}
 \tag{15}
\]
Every derivative of \(Q_v\) in another coordinate wedges with
the already present differential and vanishes. This proves
(15) directly, without an asymptotic argument.

The pullback of \(\Theta\) vanishes on every prescribed
coordinate face. On \(t_v=\pm a_N\), its own summand vanishes
by (14); every other summand contains \(dt_v\). On a wire
face \(x_e=-1/(2N)+ih_e\) or \(1-1/(2N)+ih_e\), every summand
contains \(dx_e\). This is the precise relative boundary
condition used here.

## 5. Joint deformation and its limits

**Theorem.** Let \(\mathcal L'\) be obtained from \(\mathcal L\)
by a compact piecewise smooth joint homotopy in the common product
domain, avoiding the physical angular poles. Require throughout
the homotopy that each angular endpoint face keeps its coordinate
\(t_v=\pm a_N\), and each wire seam face keeps its original
coordinate \(x_e=-1/(2N)+ih_e\) or \(1-1/(2N)+ih_e\).
Other coordinates may vary on these faces. Then (9) holds with
\(\mathcal L'\) in place of \(\mathcal L\), for either representative,
and the two representatives give the same integral on
\(\mathcal L'\).

**Proof.** The forms (8) are closed holomorphic top forms away
from their angular poles. On every side face of the homotopy
the fixed coordinate has zero differential, so the corresponding
top-form integral is zero. Stokes' theorem proves invariance.
Equation (15) and the relative boundary condition prove equality
of the two representatives on the deformed chain. All statements
are coefficientwise in the free polynomial variables. \(\square\)

This is a joint statement: angular and wire directions may move
together in the interior. It does not assert that the factorial
integrand is pointwise periodic. In fact its exact period defect
is
\[
 B_N(x+1,t)-\eta B_N(x,t)
   =\frac{(-1)^N P_N(-2\cos t)}
           {4\sin^2(\pi Nx)}B_N(x,t).
 \tag{16}
\]
The equality is meromorphic, with removable values interpreted.
In particular, a deformation of the wire seams depending on
angular coordinates is not covered by the coordinate-fixed-face
theorem. Its transgression must be retained or separately proved
to vanish. The cardinal representative is pointwise periodic
after paired halfwires are multiplied, but its geometric
asymptotics cannot be borrowed from the factorial representative
merely by discarding (15).

For a supplied compact family of positive angular points,
\(|\Re t_v|<\pi\) leaves a uniform margin, so these angular
points lie within (4) for all sufficiently large \(N\).
This statement supplies room for a deformation; it does not
prove positivity along a charge path or a global steepest-descent
cycle. The exact factors \(W_N\), both coupon exponentials,
all first normals and the canonical signed crossing factors
remain in (8). No Fourier alias is discarded.

The remaining source problem is to choose and estimate a
whole joint representative of this fixed relative class:
one must prove that its geometric local piece has a nonzero
net coefficient and that its remaining pieces have smaller
rate. The present exact primitive does not provide that
estimate. In particular, an arbitrary connecting chain in
(9) has not been identified with a scalar Ward deletion,
so a classical action gap for those specific deletions
does not by itself bound this chain.

## Direct sources

All four complete source texts and their directly used implications
were read, with the following fixed versions.

* [Full-grid lens](research_full_grid_lens_source_continuation.md),
  SHA256 d141e6e8c23572bb13484807a2359395a0371d6a3d699198826a105b6dad5649:
  exact derivative trace, reflection normalization, canonical
  signed Gaussian factors and complete coupon jets.
* [Arbitrary-power source compiler](research_arbitrary_power_source_compilation.md),
  SHA256 55e2de84870cfd20dac5922791dbc2bed54909439dfbf4663f17c70a1089445f:
  literal kernels, free-boundary convention, and common joint
  factorial domain (13).
* [Finite Fourier band](research_newton_interpolation_finite_fourier_band.md),
  SHA256 2e2d95184081ba6440b56268cb597624d97a5f1931e8c0df886fa754e6684304:
  exact full-Hermite equality of (3), entire cardinal interpolation
  and paired-index averaging.
* [Internal circle averaging](research_internal_wire_exact_circle_averaging.md),
  SHA256 0efa85a43da064197f25422d86ef37688971f2dface55da9d5efef3ccb0d08ef:
  arbitrary-network assembly, reflected wires and the distinction
  between trace periodicity and pointwise factorial periodicity.

Only written proofs, source-text reads and file hashes were used.
No mathematical code, numerical evaluation, test or compilation was
run. Frozen notes, manuscripts and public documents were unchanged.
