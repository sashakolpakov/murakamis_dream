# Slit domains and exact full-trace comparison of inverse-half heights

Private written proof, 16 November 2026.

The small-height inverse-half representatives have explicit common
holomorphic angular domains. They are slit domains, not rectangles.
Finite intersections remain simply connected and contain the entire
physical angular interval. Finite Hermite interpolation then constructs
the global endpoint-polynomial ideal decomposition on their products.
The original full angular traces annihilate the complete height-change
period exactly, without estimating its main-half primitives.

This is a comparison of complete original periods. It neither deletes
individual faces of a patched geometric contour nor bounds the main
halfwire and its endpoints. Angular paths must keep their slit detours
and original winding.

## 1. The actual angular pole union

Fix \(N\ge2\), \(h=N^{-1}\), \(D=N-1\), and put
\[
 a_N=-h/2,\quad b_N=(1-h)/2,\quad
 A_N=\pi-\frac{\pi}{2N},\quad
 \mathcal S=\{t:|\Re t|<\pi\},\quad w_t=-2\cos t.
 \tag{1}
\]
Use exactly the additive source's functions
\[
 F_N(x;t,u)=B_N(x,t)B_N(x,u),
\]
\[
 I_N(x;t,u)=\frac4{N^6}(1-\cos(2\pi Nx))^2G_N(Nx)^4
 \prod_{v\in\{t,u\}}
 G_N(D/2-Nx+Nv/(2\pi)-1)
 G_N(D/2-Nx-Nv/(2\pi)-1).
 \tag{2}
\]
For a fixed \(H>0\), define the two closed relative slits in
\(\mathcal S\) by
\[
 \Sigma_H^+=\{s+2\pi iH:0\le s<\pi\},\qquad
 \Sigma_H^-=\{s-2\pi iH:-\pi<s\le0\},
\]
\[
                  \mathcal D_H=\mathcal S\setminus
                                  (\Sigma_H^+\cup\Sigma_H^-).
 \tag{3}
\]

**Lemma 1.** For every frozen \(x\in[a_N,b_N]-iH\), the
function \(I_N(x;t,u)\) is jointly holomorphic on
\(\mathcal D_H\times\mathcal D_H\). On compact subsets the
assertion holds on a uniform neighborhood of the entire wire
segment, so its integral is holomorphic there. It is even in
each angle. The main half \(F_N\) on
\([a_N,b_N]+iH\) is holomorphic throughout \(\mathcal S^2\).

**Proof.** The actual possible wire poles from the additive
source are
\[
 x=b_N\pm t/(2\pi)+r/N,\quad r=0,1,2,\ldots,
 \tag{4}
\]
and similarly for \(u\). Set \(x=s-iH\), \(a_N\le s\le b_N\).
Solving (4) for \(t\) gives
\[
 t=2\pi(s-b_N-r/N)-2\pi iH,\qquad
 t=2\pi(b_N-s+r/N)+2\pi iH.
 \tag{5}
\]
Inside \(\mathcal S\), these lie respectively on the left lower
and right upper slits (3). Already \(r=0\) sweeps their full
real ranges; removable points do not invalidate their exclusion.
The unshifted \(G_N(Nx)\) is regular because \(x\) is nonreal.
This proves the first assertion from the complete factorial divisor.
Compactness and the same distance check give the uniform neighborhood.
The paired factors give evenness. The original reciprocal-factorial
divisor criterion gives the last assertion on the whole original
period strip, and hence on its main half. \(\square\)

For any finite nonempty set of heights \(\mathscr H\), write
\[
                 \mathcal D_{\mathscr H}=\bigcap_{H\in\mathscr H}
                                                   \mathcal D_H.
 \tag{6}
\]

**Lemma 2.** This domain is connected, simply connected and invariant
under \(t\mapsto-t\). It contains the entire real interval
\((-\pi,\pi)\), including every physical angle and \(\pm A_N\).

**Proof.** There are finitely many disjoint horizontal slits: each
upper slit is attached to the right boundary of the strip and each
lower slit to the left. No slit joins both boundaries. In the upper
half-plane a vertical corridor of negative real part connects all
heights; the lower half has a corresponding positive-real corridor.
Horizontal segments away from the finitely many slit heights connect
every point to these corridors. At a slit height, the allowed side
connects directly to its corridor. This proves connectedness.

For simple connectedness, exhaust the strip by rectangles whose
horizontal boundaries lie beyond all slit heights. Inside each such
rectangle the removed arcs run from its boundary to interior tips,
are disjoint, and create no hole. Equivalently, thicken the finitely
many slits slightly, avoiding a given compact loop; the resulting
polygonal domain has no interior boundary component and contracts
that loop. This also proves simple connectedness of the exhaustion
and its union. The two slit families are exchanged by negation.
All lie off the real axis, which proves the remaining statements.
\(\square\)

The same argument gives connected simply connected lower-half
domains after intersection with \(\Im t<0\). Thus a lower lens
from \(-A_N\) to \(A_N\) may reach any prescribed finite set of
lower-half target points off the slits, by going around the tips.
These detours are part of the actual contour. No slit is crossed
or silently filled. A thin standard lower lens is available for
every finite collection of positive heights.

## 2. Global full-Hermite source identity on the slit domains

Define the actual fixed-path representative
\[
 K_H(t,u)=N\int_{[a_N,b_N]+iH}F_N(x;t,u)\,dx
           +N\int_{[a_N,b_N]-iH}I_N(x;t,u)\,dx.
 \tag{7}
\]
Lemma 1 makes it an even holomorphic function on \(\mathcal D_H^2\).
Its full two-variable physical Hermite class is the original
\(K_T(z,w)=\sum_{j=0}^{D}e_j(z)e_j(w)\), by the additive theorem:
that theorem applies on a neighborhood of the entire real grid.
The source identity is not inferred solely from values.

Here is a finite global ideal decomposition, with no sheaf existence
argument. Let \(\mathsf H_t\) denote interpolation in \(w_t\)
by the original canonical polynomial of degree at most \(D\),
using every physical value and first spectral normal and the original
odd simple-node convention. It is applied with all other arguments
held as parameters. It is a finite linear combination of these
evaluations and derivatives, with fixed polynomial cardinal factors.
For even holomorphic functions on \(\mathcal D_{\mathscr H}\),
\[
              (1-\mathsf H_t)f=P_N(w_t)\,\mathsf Q_t f
 \tag{8}
\]
with \(\mathsf Q_t f\) holomorphic and even on that entire domain.
At ordinary physical angles this is double-zero division. At the
odd ramified angle \(t=0\), evenness and the required value give
the double angular zero. There are no other zeros of \(P_N(w_t)\)
in \(\mathcal S\). This proves (8) globally, including \(N=2\).

On \(\mathcal D_{\mathscr H}^2\), for any \(H,H'\in\mathscr H\),
let \(\Delta=K_H-K_{H'}\). The full tensor identity gives
\(\mathsf H_t\mathsf H_u\Delta=0\). Since these finite operators
commute, the literal formula
\[
 \Delta=(1-\mathsf H_t)\Delta
                   +\mathsf H_t(1-\mathsf H_u)\Delta
        =P_N(w_t)A(t,u)+P_N(w_u)B(t,u)
 \tag{9}
\]
has jointly holomorphic, even coefficients on the whole product.
The same construction applies to \(K_H-K_T(w_t,w_u)\).
No size estimate on the interpolation operators or on \(A,B\)
is asserted or required for this exact identity.

## 3. The original complete trace annihilates the height change

Take any fixed finite original network. Replace a specified subset
of its internal same-index kernels by (7), with any of finitely many
fixed positive heights at each edge. Leave every free spectral
variable as its original ordinary polynomial variable. Other kernels,
original fixed halfwire factors, polynomial spectators, signed
crossings and charge coupons remain unchanged.

At each traced vertex \(v\), let \(\mathscr H_v\) collect the
height labels incident to it in every representative being compared,
and use \(\mathcal D_v=\mathcal D_{\mathscr H_v}\); if the collection
is empty, use \(\mathcal D_v=\mathcal S\). Original fixed halfwires
on their admitted original period strips are holomorphic on these
smaller domains. Reflected halfwire arguments satisfy the same check.
The free cardinal polynomials are unchanged. Therefore all fixed
factors and all frozen angular primitive paths are simultaneously
admissible on the product \(\prod_v\mathcal D_v\).

For \(\eta=(-1)^{N-1}\), retain the exact original density
\[
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2},\qquad
 E_v(t)=e^{in_vNt^2/(4\pi)}\cos(N(1-\chi_v)t),
\]
\[
 \rho_N(\mathbf t)=\prod_v\sin t_v\,W_N(t_v)E_v(t_v),\qquad
 P_N(w_t)W_N(t)=(-1)^N.
 \tag{10}
\]
Every signed integer \(n_v\), original carrier \(C_{N,n_v}\),
optional charge \(\chi_v\), trace normalization and remaining
wire normalization keeps its original value.

**Theorem 3.** Let \(\Gamma_v\) be any full lower lens from
\(-A_N\) to \(A_N\) in \(\mathcal D_v\). The complete original
trace period is independent of all the specified height choices.
It equals the original network, coefficientwise in every unreduced
free boundary polynomial. This retains every original normal.

**Proof.** Let \(F\) and \(F'\) denote the two complete even
holomorphic numerator products. Their full tensor Hermite classes
agree, including when the graph has loops or repeated edges.
List the traced vertices once. The finite telescoping formula is
\[
 F-F'=\sum_v\left(\prod_{w<v}\mathsf H_w\right)
                       (1-\mathsf H_v)(F-F')
       =\sum_v P_N(w_{t_v})A_v(\mathbf t).
 \tag{11}
\]
All coefficients are jointly holomorphic and even on the product
domains. Formula (8) proves their removability at every physical
point. Diagonal restrictions for a loop are valid because the
original two-endpoint tensor identity retains the mixed jets.

Multiply (11) by (10). In the \(v\)-th summand the full \(v\)-th
trace kernel cancels exactly. Its coefficient is then odd and
holomorphic in \(t_v\) throughout the simply connected domain
\(\mathcal D_v\); the other trace kernels remain at their actual
parameters. Its primitive from \(-A_N\) is path independent.
Its value at \(A_N\) is zero, since the straight real-interval
integral of this odd holomorphic coefficient is zero. Consequently
its integral on \(\Gamma_v\) is exactly zero. Fubini, followed
by the original finite prefactors, proves equality of the complete
periods. The joint-lens source identifies their common value with
the original full trace. If some wire coordinates remain unintegrated,
this equality first holds at every admitted frozen value; their
original wire integrals and normalizations are then retained unchanged.
All operations are linear on the free polynomial coefficients.
\(\square\)

The hypotheses allow a lens with the required slit detours. They
do not allow crossing an artificial slit and retaining the same
integral without its continuation data. If a different contour is
used, its full reflected closed lens must retain the original
winding around the physical grid. Lower lenses as stated have
that winding: they deform to a thin lower lens in the slit domain
without crossing the real physical poles.

Different height choices may first use different lower lenses in
their own slit domains. Each can be compared to a thin lower lens
in their common intersection. This yields the same complete period
without constructing a homotopy that sweeps the wire height through
the moving pole walls.

## 4. Relative primitives, bounds and the remaining contour problem

The proof constructs the actual angular relative primitive, rather
than merely declaring the overlap class to be zero. After the
cancellation in (10), integrate each term of (11) in its designated
angle from \(-A_N\), with the usual omitted differential and its
orientation sign. On the explicit common product domains this gives
\[
 \Omega_i-\Omega_{\rm car}=d\Theta_i,\qquad
 J_{ij}=\Theta_j-\Theta_i,\qquad
 dJ_{ij}=\Omega_j-\Omega_i,\qquad
 J_{ij}+J_{jk}+J_{ki}=0.
 \tag{12}
\]
Every primitive has zero pullback on its two original angular
endpoint faces. The complete full-lens period of the difference
is zero by Theorem 3. Thus integrated height comparison does not
require an absolute bound on these main-half primitives.

On a compact portion of an angular contour separated by
\(N^{-C}\) from the appropriate slits, the horizontal inverse
wire is separated, up to the fixed factor \(2\pi\), from its
actual moving poles. The inverse-strip theorem therefore bounds
that inverse integral, its polynomial-distance detours and grouped
residues by
\[
 N^B\exp\{N[8\pi\epsilon+
                  C_{\mathcal K}\epsilon(1+|\log\epsilon|)]\}
 \tag{13}
\]
when its height lies in \([\epsilon,2\epsilon]\). Fixed derivatives
have polynomial losses on buffered charts. The exponent \(B\) is
fixed before \(\epsilon\). Angular slit detours, original endpoint
regions and all other source factors remain in the actual cycle;
(13) supplies no estimate for those other factors.

In particular, if a geometric contour is subdivided and different
height labels are used on its separate cells, Stokes still gives
the local bulk terms together with their oriented interface
primitive terms from (12). Theorem 3 does not set those individual
face integrals to zero. Replacing such a patched contour by one
of the complete periods above requires retaining its full relative
boundary and original winding. There is no bound here on the
main-half endpoints, no nonzero geometric coefficient theorem,
and no global steepest-descent estimate.

## Direct sources and author audit

The complete direct source texts were read in this author sequence,
with their used implications checked at these pins.

- `research_additive_half_wire_source_regularization.md`:
  `af8daf3eaa16303f8297b4a712ee9debe31cabc7326776fc34c9b185f0d216a0`;
  actual inverse integrand, complete divisors, full two-endpoint
  Hermite identity and exact additive source normalization.
- `research_joint_factorial_lens_relative_source.md`:
  `a14ca148bd55b36b1eea9de8be8a63025532c3bbbb928482b0d7cb8edae56e54`;
  original network, fixed halfwire domain, full trace normalization,
  finite Hermite division, relative primitives and free variables.
- `research_inverse_half_strip_contour_bounds.md`:
  `8f042172b3bed433f851d9197666c06f3d58e3be260d8fe21d3eb0b244339043`;
  polynomial-distance inverse bounds, grouped residues, connectors,
  fixed derivatives and their retained relative-cycle scope.

Only written mathematics, source reads and metadata hashes were used.
No mathematical program, numerical evaluation, test or compilation
was run. Adopted notes and public manuscripts were unchanged.
