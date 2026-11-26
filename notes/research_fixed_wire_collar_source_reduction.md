# Fixed-wire collars in the original relative source

Private written proof, 16 November 2026.

An internal same-index edge admits a source-equivalent representation
whose two wire endpoint pieces have arbitrarily small local exponential
rate on buffered angular sets. The original factorial integrand remains
on a fixed interior wire segment. The right collar is reflected and
replaced by the actual inverse integrand, with its poles retained.

This replacement also holds on joint relative chains: its angular
primitive contains every wire differential and therefore vanishes on
coordinate-fixed wire interfaces, even when the angular variables vary
there. This removes the primitive on those interfaces. It does not
remove arbitrary angular patch faces or bound the remaining interior
connecting contour, spectators, or whole filled graph.

## 1. The literal collar decomposition

Fix \(N\ge2\), \(h=N^{-1}\), \(D=N-1\), and
\[
 a=-h/2,\qquad b=(1-h)/2,\qquad
 \mathcal R x=D/N-x=2b-x,\qquad
 A_N=\pi-\frac{\pi}{2N}.
 \tag{1}
\]
The original angular variable is \(w_t=-2\cos t\), and
\(P_t=P_N(w_t)\), where \(P_N(z)=2T_N(z/2)+2\). Use the
unchanged canonical factorial and functions
\[
 \begin{split}
 A_t(x)&=D/2-Nx+Nt/(2\pi),\\
 B_t(x)&=D/2-Nx-Nt/(2\pi),\\
 B_N(x,t)&=\frac{N}{G_N(A_t(x))G_N(B_t(x))G_N(Nx)^2},\\
 F_N(x;t,u)&=B_N(x,t)B_N(x,u),\\
 I_N(x;t,u)&=\frac4{N^6}(1-\cos2\pi Nx)^2G_N(Nx)^4
       \prod_{v=t,u}G_N(A_v(x)-1)G_N(B_v(x)-1).
 \end{split}
 \tag{2}
\]
Thus \(B_t(x)\) is a factorial argument, not the halfwire function.
Put \(d_t(x)=\cos t+\cos(2\pi x+\pi h)\). The exact additive
identity is
\[
 F_N(\mathcal R x;t,u)-I_N(x;t,u)
 =\frac{-(1-\cos2\pi Nx)(P_t+P_u)/2+P_tP_u/4}
 {N^4d_t(x)d_u(x)F_N(x;t,u)}.
 \tag{3}
\]
All equalities involving this expression are meromorphic identities
with the actual factorial divisors. There is no division by a formal
nonzero kernel.

For \(H>0\), the adopted full-source representative is
\[
 K_H(t,u)=N\int_{[a,b]+iH}F_N(y;t,u)\,dy
                +N\int_{[a,b]-iH}I_N(x;t,u)\,dx.
 \tag{4}
\]
Every displayed horizontal segment is oriented left to right. Choose
\(0<\delta<1/4\), independently of \(N\). Define
\[
 \begin{split}
 M_{H,\delta}(t,u)&=N\int_{[a+\delta,b-\delta]+iH}F_N(y;t,u)\,dy,\\
 R_{H,\delta}(t,u)&=
 N\int_{[a,a+\delta]+iH}F_N(y;t,u)\,dy
 +N\int_{[a,b+\delta]-iH}I_N(x;t,u)\,dx,\\
 K_{H,\delta}&=M_{H,\delta}+R_{H,\delta}.
 \end{split}
 \tag{5}
\]
The second term of \(R_{H,\delta}\) is one extended inverse
segment. Its extension past \(b\) has positive orientation. Indeed,
\[
 \int_{[b-\delta,b]+iH}F_N(y)\,dy
 =\int_{[b,b+\delta]-iH}F_N(\mathcal R x)\,dx,
 \tag{6}
\]
since reflection reverses both the parameter direction and the
differential. Consequently the exact ordinary difference is
\[
 K_H-K_{H,\delta}
   =N\int_{[b,b+\delta]-iH}
           [F_N(\mathcal R x)-I_N(x)]\,dx.
 \tag{7}
\]
We do not set this ordinary holomorphic function to zero.

## 2. Common slit domains and the full source

Let \(\mathcal S=\{t:|\Re t|<\pi\}\). The necessary extended
slits are
\[
 \begin{split}
 \Sigma_{H,\delta}^+
   &=\{s+2\pi iH:-2\pi\delta\le s<\pi\},\\
 \Sigma_{H,\delta}^-
   &=\{s-2\pi iH:-\pi<s\le2\pi\delta\},\\
 \mathcal D_{H,\delta}
   &=\mathcal S\setminus(\Sigma_{H,\delta}^+\cup
                                      \Sigma_{H,\delta}^-).
 \end{split}
 \tag{8}
\]
For \(\delta=0\), this is the adopted height-comparison domain.

**Lemma 1.** The functions in (5) are holomorphic and even in each
angle on \(\mathcal D_{H,\delta}^2\). Every finite intersection
of these domains is connected, simply connected, invariant under
negation, and contains \((-\pi,\pi)\), including every physical
angle and \(\pm A_N\).

**Proof.** The actual possible shifted-factor poles of \(I_N\) are
\[
 x=b\pm t/(2\pi)+r/N,\quad
 x=b\pm u/(2\pi)+r/N,\qquad r=0,1,2,\ldots.
 \tag{9}
\]
At \(x=s-iH\), \(a\le s\le b+\delta\), their angular union
in \(\mathcal S\) is contained in (8): the lower family has
real coordinate \(2\pi(s-b-r/N)\le2\pi\delta\), and the upper
family has coordinate \(2\pi(b-s+r/N)\ge-2\pi\delta\).
The \(r=0\) segments already cover the relevant ranges inside
the strip. The unshifted factorial \(G_N(Nx)\) has no pole on
this nonreal segment. The original \(F_N(y)\) is holomorphic
on the admitted original wire strip and \(\mathcal S^2\), including
the left cap and core in (5). Compactness supplies neighborhoods
of the paths, proving holomorphy of their integrals. The paired
arguments give evenness.

After repeated heights are combined, a finite intersection removes
finitely many disjoint horizontal arcs attached to the right boundary
above the real line and to the left boundary below it. Their tips
remain strictly interior because every \(\delta<1/4\). An upper
corridor with real part below all upper tips and a lower corridor
above all lower tips connect every point to the real interval.
Thickening the arcs slightly away from any compact loop gives a
polygonal exhaustion with no interior boundary component. This
proves simple connectedness as well as connectedness. Negation
exchanges the two slit families, and no slit meets the real axis.
\(\square\)

**Proposition 2.** The full two-endpoint physical Hermite class of
\(K_{H,\delta}\) is the original
\(K_T(z,w)=\sum_{j=0}^{N-1}e_j(z)e_j(w)\). It retains the mixed
first spectral normal, both parities, and the odd simple-node
convention. Any fixed finite collection of internal same-index
edges may be replaced by (5) inside the original complete traces,
using the common vertex domains from Lemma 1 and full lower lenses
from \(-A_N\) to \(A_N\). All free endpoints remain their original
ordinary polynomial variables.

**Proof.** In a neighborhood of the entire real physical angular
grid, the coefficients in (3) are holomorphic on the reflected
collar: its wire imaginary part is \(-H\), while all physical
angles are real. Equation (7) therefore belongs to \((P_t,P_u)\)
there, including all mixed physical jets. The adopted additive
theorem identifies the full class of \(K_H\), proving the first
claim.

For the global source statement, apply the actual finite Hermite
interpolation operators \(\mathsf H_t,\mathsf H_u\). On the
domains in Lemma 1 every even holomorphic \(f\) satisfies
\[
 (1-\mathsf H_t)f=P_t\mathsf Q_t f,
 \tag{10}
\]
with a holomorphic even quotient. At a double spectral root this
is full value/normal division; at the odd simple root the angular
zero is double and evenness supplies the required angular order.
There are no other zeros of \(P_t\) in \(\mathcal S\). Thus,
for \(\Delta=K_H-K_{H,\delta}\), the literal finite formula
\[
 \Delta=(1-\mathsf H_t)\Delta+
               \mathsf H_t(1-\mathsf H_u)\Delta=P_tA+P_uB
 \tag{11}
\]
has holomorphic even coefficients on the full product domain.

At each traced vertex retain the exact original density
\[
 W_N(t)=\frac{e^{-iNt}}{(1-(-1)^{N-1}e^{-iNt})^2},\qquad
 E_v(t)=e^{in_vNt^2/(4\pi)}\cos(N(1-\chi_v)t),
 \qquad P_tW_N(t)=(-1)^N.
 \tag{12}
\]
The traced factor is \(\sin t_v W_N(t_v)E_v(t_v)\), with its
unchanged multiplier \(-N^2 C_{N,n_v}/(\pi i)\). Wire multipliers
are exactly the \(N\)'s in (4)--(7). Signed crossings, charge
coupons, other halfwires, and polynomial spectators are unchanged.
Telescoping the edge replacements, followed by finite Hermite
division at the traced vertices, expresses the difference as
\(\sum_vP_{t_v}A_v\) on their common product domain. After (12)
its designated \(t_v\)-coefficient is odd and holomorphic. Its
primitive from \(-A_N\) is path independent and vanishes at
\(A_N\). Hence its integral on the complete original lower lens
is zero. The other variables and all original prefactors remain
untouched. Loops and repeated edges retain the mixed tensor jets
before restriction to shared variables. The argument includes
\(N=2\) and is coefficientwise in the unreduced free polynomials.
\(\square\)

Angular paths keep the slit detours and the original winding. A
thin common lower lens exists for every finite set of height/collar
labels. Proposition 2 does not allow removing an arbitrary slit
crossing or replacing an untraced ordinary polynomial by (5).

## 3. Why a fixed wire interface has no primitive current

The local statement needed for a joint contour is stronger than
equality after product integration. Use the original upper collar
coordinate \(y\), so the two local edge densities are
\(F_N(y;t,u)\,dy\) and \(I_N(\mathcal R y;t,u)\,dy\). At every
frozen \(y\) near its collar their difference has zero full
two-endpoint Hermite class. Finite division as in (11) makes its
ideal coefficients jointly holomorphic in \(y\) and the angles on
the admitted common product domains. No inverse integral is needed
for this pointwise source statement.

Here are precise relative-chain hypotheses. Work on a common open
domain where all local edge representatives and unchanged source
factors are holomorphic, apart from the original angular trace poles.
Require that each frozen designated angular primitive is defined on
one of the connected, simply connected even domains of Lemma 1,
containing the entire real physical interval. Use compact piecewise
smooth joint chains and homotopies in this domain, away from the
remaining original trace poles. Keep all angular endpoint faces at
\(t_v=\pm A_N\). Keep the wire faces at which representatives are
patched at their stated constant complex wire coordinates. Other
original wire seams are also fixed; if moved, their original
transgression currents must instead be retained explicitly.
These are the designated relative boundary faces. Any additional
angular slit, patch, or exterior face is retained in Stokes' formula;
its primitive integral is not set to zero.

**Theorem 3.** Under these relative-chain hypotheses, let
\(\partial_{\rm extra}\Gamma\) be the oriented sum of the boundary
faces of the joint chain \(\Gamma\) other than its designated
coordinate-fixed wire and angular endpoint faces. The literal identity is
\[
 \int_\Gamma(\Omega_{\rm old}-\Omega_{\rm new})
       =\int_{\partial_{\rm extra}\Gamma}\Theta.
 \tag{13a}
\]
Thus the replacement preserves the complete original source with
these boundary currents retained. Its two bulk integrals are equal
when there are no extra faces, or when the sum on the right vanishes.
In particular the primitive has zero pullback on the fixed cut
\(y=b-\delta+iH\) and on \(y=b+iH\), even if the angular coordinates
and other wire coordinates vary along those faces. The same holds
for any further coordinate-fixed wire cuts.

**Proof.** Multiply the pointwise ideal identity by every unchanged
source factor, including the shared angular factors, and telescope
if several edges are replaced. With one fixed order of all complex
coordinates, the resulting top-form difference is a sum of terms
whose coefficient, after (12), is odd and holomorphic in a designated
angle \(t_v\). Call that coefficient \(H_v\), and set
\[
 Q_v(\mathbf x,\mathbf t)=
 \int_{-A_N}^{t_v}H_v(\mathbf x,t_1,\ldots,\tau,\ldots)\,d\tau.
 \tag{13}
\]
This is jointly holomorphic off the retained other trace poles,
path independent, and zero at both designated angular endpoints.
Let \(\Theta_v\) be \(Q_v\) times the ordered wedge omitting only
\(dt_v\), with its usual exterior sign. Then
\[
       \Omega_{\rm old}-\Omega_{\rm new}=d\Theta,
       \qquad \Theta=\sum_v\Theta_v.
 \tag{14}
\]
Derivatives in every other coordinate wedge with an already present
differential and vanish. Crucially, every \(\Theta_v\) contains
every wire differential \(dx_e\).

On any face \(x_e=\zeta_e\) with \(\zeta_e\) a constant complex
number, the pullback of \(dx_e\) is zero. Therefore the entire
pullback of \(\Theta\) is zero there. Coupling the remaining
coordinates on the face does not change this fact. On an angular
endpoint face its own primitive vanishes; all other summands contain
that angular differential. Stokes applied to (14) leaves exactly
the extra-face sum in (13a). It applies cell by cell to multiple
fixed wire cuts, with the prescribed orientations. The exact
reflection (6) then gives the positive extended inverse segment in
(5). Hence the original period is the new bulk integral plus the
extra-face current in (13a); equality of bulk integrals alone requires
that current to vanish. This proves the assertion for the actual
relative chain, with all original normal data and scalar factors
retained. \(\square\)

For example the core and collar may undergo a joint deformation
while their common cut remains at \(y=b-\delta+iH\). The collar
can be compared to its inverse representative on that deformed
chain if the stated common-domain hypothesis persists. An arbitrary
angular cell interface is different: its omitted differential need
not be present in \(\Theta_v\), so its primitive integral remains.
Nor is a wire cut \(y=\zeta(\mathbf t)\) coordinate fixed.
No cancellation on either of those types of faces is asserted.

## 4. Small local rate of both endpoint pieces

Fix a buffered angular compact \(\mathcal K\subset\mathcal S^2\),
with bounded imaginary parts. Choose a slightly larger compact
neighborhood once and for all. Fix \(C>2\) and \(\rho_N=N^{-C}\).
Only afterward choose small fixed \(\epsilon,\delta>0\), with
\(0<\delta<1/4\), and \(H\in[\epsilon,2\epsilon]\).
All quantitative assertions below are for sufficiently large \(N\).
The exact source statements above apply already for \(N\ge2\).

Write \(\mathcal J=\Re J_{\rm side}\) for the original sine
primitive, \(J'=\Log(2\sin\pi z)\), \(J(0)=0\), with its actual
upper/lower continuation across the negative real axis. Their real
boundary values agree. On a fixed argument compact its continuity
modulus is at most \(Cs(1+|\log s|)\). Set
\[
 \mathcal B(x,t)=-\mathcal J(1/2-x+t/(2\pi))
                 -\mathcal J(1/2-x-t/(2\pi))-2\mathcal J(x).
 \tag{15}
\]
The adopted real-wire identity gives
\[
 \mathcal B(0,t)=0,\qquad
 \mathcal B(x,t)\ge0\quad(0\le x\le1/2)
 \tag{16}
\]
for every complex angular parameter under consideration.

**Theorem 4.** There is a finite polynomial exponent \(B\), chosen
independently of the later \(\epsilon,\delta\), such that the sum
of the absolute values of the two integrals in \(R_{H,\delta}\)
is bounded by
\[
 C_{\mathcal K,\epsilon,\delta,C}N^B
       \exp\{N\kappa_{\mathcal K}(\epsilon,\delta)\},
 \tag{17}
\]
provided the inverse path has distance at least \(\rho_N\) from
its actual poles. One may take
\[
 \kappa_{\mathcal K}(\epsilon,\delta)
 =8\pi\epsilon+
 C_{\mathcal K}(\epsilon+\delta)
                         (1+|\log(\epsilon+\delta)|).
 \tag{18}
\]
The same bound, after a polynomial change, holds for bounded-length
polynomial-distance detours and endpoint connectors in the enlarged
thin inverse band, and for the sum of the absolute values of the
grouped residues they cross. Endpoints must themselves be regular.
Fixed parameter derivatives on buffered pole-separated charts have
the same rate with polynomial loss.

**Proof.** For the left cap, the midpoint factorial estimates give
\[
 |N F_N(y;t,u)|\le C N^{B_0}
          e^{N[\mathcal B(y,t)+\mathcal B(y,u)]}.
 \tag{19}
\]
To include its left end, use the midpoint argument \(y+h/2\)
for \(G_N(Ny)\). Its real part is nonnegative along the cap.
The shifted arguments of the reciprocal factorials stay in a fixed
\([-1+\eta,1-\eta]\) once the angular buffer is fixed and \(\delta\)
is small. The uniform reciprocal estimate includes all its zeros.
The midpoint shifts cost \(O(\log N)\), by the stated continuity
modulus, so \(B_0\) is fixed before the small heights and lengths.
Since \(\mathcal B(0,v)=0\), every point of the left cap differs
from zero by at most \(\delta+2\epsilon+O(h)\). Equations
(15)--(16) prove (17)--(18) for that cap.

For the inverse segment allow an additional \(40\rho_N\) margin
around \([a,b+\delta]-i[\epsilon,2\epsilon]\). Each shifted
factorial midpoint argument has real part in a fixed
\([-1+\eta,1-\eta]\): at the new right end its smallest limiting
real part is greater than \(-1/2-\delta>-3/4\). The slightly
larger angular compact and sufficiently large \(N\) fix the margin.
The unshifted midpoint argument \(x+h/2\) stays near \([0,1/2+\delta]\)
at nonzero height. Thus the same exact reflection used in the
inverse-strip theorem applies to every factor. At polynomial distance
from a shifted factorial pole its normalized cosine denominator is
at least \(cN^{1-C}\). The four shifted factors cost at most four
such polynomial losses. This yields
\[
 |N I_N(x;t,u)|\le C N^{B_1}
 \exp N\{4\pi|\Im x|-\mathcal B(x,t)-\mathcal B(x,u)\}.
 \tag{20}
\]
All midpoint displacements again cost only \(O(\log N)\).

Project \(\Re x\) to \([0,1/2]\). Its displacement is at most
\(\delta+O(h+\rho_N)\). The height is at most \(2\epsilon+O(\rho_N)\).
Continuity and (16) bound the last two terms in (20) above by
\(C_{\mathcal K}(\epsilon+\delta)(1+|\log(\epsilon+\delta)|)\),
plus \(O(h\log N)\). The cosine numerator supplies at most
\(8\pi\epsilon\) in the rate. This proves (17)--(18) on the
extended inverse segment. No nonnegativity beyond \(x=1/2\) is used.

The extended band still has exactly the four possible pole lattices
(9), with \(O(N)\) eligible points. Each shifted pole is simple
for large \(N\); \(G_N(Nx)\) introduces none in this band.
Within each lattice the spacing is \(1/N\). Disks of radii between
\(3\rho_N\) and \(4\rho_N\) therefore have connected clusters
of at most four centers for large \(N\). Detouring along cluster
boundaries has total added length \(O(N\rho_N)\), keeps distance
at least \(2\rho_N\), and retains the exact winding. Integrating
(20) on these paths and the cluster loops gives the asserted sum
bound for grouped residues, including collisions. Every connector
and residue in the exact Cauchy transition is retained, with its
orientation; a residue is not deleted by this estimate.

Freeze these contours on parameter neighborhoods of radius
\(c\rho_N\). Separation and winding persist; Cauchy differentiation
costs \(N^{Ck}\) at fixed total order \(k\), using the initially
chosen larger compact. The compact parameter set admits polynomially
many such charts. This proves the derivative assertion and completes
the proof. \(\square\)

The five fixed heights in the additive theorem remain available:
the imaginary heights of the pole lattices have not changed on
extending the real segment. Thus at each parameter pair one of
five heights in \([\epsilon,2\epsilon]\) has a fixed \(c\epsilon\)
distance from both pole heights. It automatically supplies regular
endpoints and a local chart for (17). For other paths or transitions
the polynomial-distance and endpoint hypotheses must be checked.

## 5. Consequence and precise remaining obligation

Equations (5), (11), and Theorem 3 give a concrete relative source
with a fixed main interior segment and two controlled local endpoint
pieces. On a general admitted joint chain its additional angular,
slit, patch, or exterior boundary currents are exactly the right
side of (13a) and remain part of that source. Choosing
\(\delta,\epsilon\) after the buffered angular compact makes the
two local endpoint pieces' rate in (18) arbitrarily small; no
bound on the extra-face current is asserted. On a
compact positive edge set this may be chosen below the positive
minimum of the original \(\Re\psi\), using the adopted action
reserve. A local saddle that lies strictly inside the retained core
is unchanged by this representation.

For any fixed number of such edges, the product of their local
endpoint bounds has a polynomial prefactor and the sum of their
small rates. This statement concerns those factors only. The original
signed crossings, shared angular trace kernels, all other source
factors, and unreduced free variables remain in the actual joint
integrand. Their rate must be compared jointly; no low rate for the
whole graph or its spectators follows from (17).

The exact source comparison uses complete angular domains and full
physical traces. Its quantitative bound uses buffered angular
compacts. The angular endpoint regions of the original full lens,
slit detours, exterior faces, and any moved-seam currents are therefore
still present. General angular subdivisions retain their primitive
faces. Most importantly, no contour bound connecting the retained
main interior to a coherent geometric saddle, and no nonzero net
geometric coefficient, has been proved here.

## Direct sources and author audit

The complete five direct texts were read in this author sequence,
their used implications checked, and their hashes verified.

- `research_additive_half_wire_source_regularization.md`:
  `af8daf3eaa16303f8297b4a712ee9debe31cabc7326776fc34c9b185f0d216a0`;
  exact inverse/reflection identity, actual source and divisors,
  nonnegative real potential, five heights, positive action reserve.
- `research_inverse_half_strip_contour_bounds.md`:
  `8f042172b3bed433f851d9197666c06f3d58e3be260d8fe21d3eb0b244339043`;
  polynomial-distance factorial bound, finite detours, grouped
  collisions, retained connectors and derivative charts.
- `research_inverse_half_slit_domain_source_comparison.md`:
  `f48d39aa6e820660fbde64e31fce4c3570b15e198106af156a3f8f485ab7c868`;
  common slit domains, finite global Hermite division, complete
  signed/charged trace comparison and angular winding.
- `research_joint_factorial_lens_relative_source.md`:
  `a14ca148bd55b36b1eea9de8be8a63025532c3bbbb928482b0d7cb8edae56e54`;
  exact network normalization, joint angular primitives, all-wire
  differentials, coordinate-fixed relative boundaries and free scope.
- `research_uniform_factorial_and_boundary_decay.md`:
  `4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11`;
  midpoint estimates through zero, reciprocal estimates on both
  sides of moving zeros, and their original branch normalization.

Only written mathematics, source reads and metadata hashes were used.
No mathematical program, numerical evaluation, test or compilation
was run. Adopted notes and public manuscripts were unchanged.
