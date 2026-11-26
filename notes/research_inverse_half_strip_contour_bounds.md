# Polynomial-distance contours for the inverse halfwire

Private written proof, 16 November 2026.

The inverse halfwire from the additive regularization has an arbitrarily
small exponential rate on an entire thin wire band, outside polynomially
small disks around its actual poles. Consequently its detours, grouped
residues and endpoint connectors have the same rate. The number of
contour pieces and parameter charts needed below is polynomial in the
level. This bounds the inverse pieces in a finite relative contour
calculation; it does not bound the main-half angular primitives.

## 1. Exact source and the contours being estimated

Use the original canonical factorial and put
\[
 h=N^{-1},\quad D=N-1,\quad \eta=(-1)^D,\quad
 a_N=-h/2,\quad b_N=(1-h)/2,\quad \mathcal R x=D/N-x,
\]
\[
 P_t=P_N(-2\cos t),\qquad P_N(z)=2T_N(z/2)+2.
 \tag{1}
\]
Write
\[
 A_t=D/2-Nx+Nt/(2\pi),\quad B_t=D/2-Nx-Nt/(2\pi),
\]
\[
 B_N(x,t)=\frac{N}{G_N(A_t)G_N(B_t)G_N(Nx)^2},
 \qquad F_N(x;t,u)=B_N(x,t)B_N(x,u).
 \tag{2}
\]
The inverse half is the exact function
\[
 I_N(x;t,u)=\frac4{N^6}(1-\cos(2\pi Nx))^2G_N(Nx)^4
       \prod_{v\in\{t,u\}}G_N(A_v-1)G_N(B_v-1).
 \tag{3}
\]
In particular it is not a formal reciprocal with its poles suppressed.
The additive source theorem proves the meromorphic identity
\[
 F_N(\mathcal R x;t,u)-I_N(x;t,u)
 =\frac{-(1-\cos(2\pi Nx))(P_t+P_u)/2+P_tP_u/4}
 {N^4d_t(x)d_u(x)F_N(x;t,u)},
 \quad d_t(x)=\cos t+\cos(2\pi x+\pi h).
 \tag{4}
\]
For \(\gamma_H^-=[a_N,b_N]-iH\), oriented left to right, set
\[
 L_H=N\int_{\gamma_H^-}I_N\,dx,
 \qquad M_H=N\int_{[a_N,b_N]+iH}F_N\,dx.
 \tag{5}
\]
On the common strip \(|\Im t|,|\Im u|<2\pi H\), the exact
representative \(K_H=M_H+L_H\) has the original two-endpoint
Hermite class. All first spectral normals and their mixed product
are retained. Its interpretation outside this strip requires the
actual continuation, residues and boundary terms, not merely its
local physical class.

Fix an angular compact set \(\mathcal K\) with
\(|\Re t|,|\Re u|<\pi\) and bounded imaginary parts. Fix a slightly
larger compact neighborhood first. Constants below may depend on it.
Choose \(C>2\), put \(\rho_N=N^{-C}\), and then choose a small
fixed \(\epsilon>0\). All assertions are for sufficiently large
\(N\), with this order of choices. Use the enlarged lower band
\[
 \mathcal S_{N,\epsilon}=
 \{a_N-40\rho_N\le\Re x\le b_N+40\rho_N,
       \epsilon-40\rho_N\le-\Im x\le2\epsilon+40\rho_N\}.
 \tag{6}
\]
Its conjugate upper-band version follows from the same proof.

The possible poles in this band are the four actual lattices
\[
 x=b_N\pm t/(2\pi)+r/N,\qquad
 x=b_N\pm u/(2\pi)+r/N,\qquad r=0,1,2,\ldots .
 \tag{7}
\]
There are \(O_{\mathcal K}(N)\) eligible points. Each individual
factorial pole is simple here, and a collision has order at most
four before the numerator is included. For large \(N\), the small
enlargement in (6) introduces no pole of \(G_N(Nx)\): its first
negative pole remains at \(-1/N\). These facts follow either
directly from \(\operatorname{ord}_{z=k}G_N(z)=\lfloor k/N\rfloor\)
or from the complete divisor calculation in the additive source.

## 2. The polynomial-distance bound

Let \(\mathcal J\) be the real part of the original primitive
\(J'=\Log(2\sin\pi z)\), with \(J(0)=0\), using its upper or
lower continuation at the negative real axis. Its two real boundary
values there agree. No angular carrier is reset.

**Lemma 1.** There is \(\kappa_{\mathcal K}(\epsilon)\to0\) as
\(\epsilon\downarrow0\) and a finite exponent \(B\), independent
of the chosen thin height \(\epsilon\), such that
\[
 |N I_N(x;t,u)|\le C_{\mathcal K,\epsilon,C}N^B
                     e^{N\kappa_{\mathcal K}(\epsilon)}
 \tag{8}
\]
on (6), whenever \((t,u)\in\mathcal K\) and the distance from
\(x\) to every pole in (7) is at least \(\rho_N\). One may take
\[
 \kappa_{\mathcal K}(\epsilon)
       =8\pi\epsilon+C_{\mathcal K}\epsilon(1+|\log\epsilon|).
 \tag{9}
\]
Fixed derivatives on parameter charts that preserve this separation
cost only additional powers of \(N\).

**Proof.** The midpoint estimate from the pinned factorial bound is
\[
 |G_N(Nz-1/2)|\asymp\sqrt N\,e^{N\mathcal J(z)}
 \quad(0\le\Re z\le1-\delta),
 \tag{10}
\]
uniformly on bounded height sets, including \(z=0\). For negative
real part its exact reflection is
\[
 G_N(Nz-1/2)=\frac{N}{2\cos(\pi Nz)G_N(-Nz-1/2)}.
 \tag{11}
\]
If \(z\) stays at least \(\rho_N\) from the negative half-grid
points where this factorial has poles, then
\[
 |2\cos(\pi Nz)|\ge c N^{1-C}e^{\pi N|\Im z|}.
 \tag{12}
\]
Indeed, for \(N|\Im z|\ge1\) the normalized cosine is bounded
below by \(1-e^{-2\pi}\). In the remaining region its distance
to a simple cosine zero gives \(c\min\{1,N\operatorname{dist}
(z,(\mathbb Z+1/2)/N)\}\). Only the negative zeros are relevant
when \(\Re z<0\); a neighborhood of zero contains no additional
exception. Equations (10)--(12), with the original side identity
\(\mathcal J(z)=-\mathcal J(-z)-\pi|\Im z|\), imply
\[
 |G_N(Nz-1/2)|\le C N^{C-1+1/2}e^{N\mathcal J(z)}
 \tag{13}
\]
on the negative part of the bounded argument range. There is no
such additional power on the nonnegative part.

All midpoint arguments in (3) have real parts in a fixed
\([-1+\delta,1-\delta]\). The four shifted arguments have slope
\(-1\) in \(x\), so their pole distance is exactly the distance
to the corresponding lattice (7). The unshifted midpoint argument
is \(x+h/2\); it has imaginary part bounded away from zero by
\(\epsilon/2\). Thus its small possible negative real part causes
no new polynomial-distance problem.

The eight factorial occurrences in (3) contribute the usual
\(N^4\), with at most four extra powers \(N^{C-1}\). The outside
factor \(N\) leaves \(N^{-1}\) before these losses. Their real
phase, after the midpoint shifts are included, is
\(-\mathcal B(x,t)-\mathcal B(x,u)\), up to \(O(h\log N)\), where
\[
 \mathcal B(x,t)=
 -\mathcal J(1/2-x+t/(2\pi))
 -\mathcal J(1/2-x-t/(2\pi))-2\mathcal J(x).
 \tag{14}
\]
For clarity, the shifted midpoint arguments are
\(1/2-x\pm t/(2\pi)-h\), and the unshifted one is \(x+h/2\).
On the fixed argument compact, \(\mathcal J\) has modulus of
continuity at most \(C s(1+|\log s|)\). This follows from its
\(z\log z\) expansion near zero and bounded derivatives elsewhere
on each side of the cut. The real values agree across that cut,
so splitting a short path at it gives the same bound. Consequently
the midpoint shifts cost \(O(\log N)\) in the logarithm, even
when an argument approaches zero.

On real \(0\le x\le1/2\), the additive source theorem proves
\(\mathcal B(x,t)\ge0\) for every angular parameter in question,
by its logarithmic-potential formula. Moving from (6) to that real
interval therefore costs at most
\(C_{\mathcal K}\epsilon(1+|\log\epsilon|)+O(h\log N)\).
Finally
\[
 |1-\cos(2\pi Nx)|^2\le4e^{4\pi N|\Im x|}
          \le C e^{8\pi N\epsilon},
 \tag{15}
\]
since \(N\rho_N\to0\). These estimates prove (8)--(9).

On a smaller parameter chart of radius \(c\rho_N\), fixed
contours at distance at least \(2\rho_N\) keep distance
\(\rho_N\) from every moving pole. Cauchy differentiation on
that chart costs \(N^{Ck}\) at fixed total order \(k\). Apply
(8) on the previously fixed larger angular compact. This proves
the derivative assertion. \(\square\)

## 3. Detours, collisions and exact connector identities

**Proposition 2.** Start with a fixed finite collection of horizontal
or vertical segments in the core band
\([a_N,b_N]-i[\epsilon,2\epsilon]\). Suppose their prescribed
endpoints have distance at least \(10\rho_N\) from the moving
pole set. They can be replaced by paths with the same endpoints,
in (6), at distance at least \(2\rho_N\) from all poles. Their
lengths stay bounded, their number of pieces is \(O(N)\), and
their inverse-half integrals satisfy (8), after a polynomial
change of the prefactor. The same holds for the sum of the
absolute values of all grouped residues crossed in the deformation.

**Proof.** Place disks of radius between \(3\rho_N\) and
\(4\rho_N\) at the eligible poles and group intersecting disks.
For large \(N\), a connected cluster has at most four centers:
a fifth center would repeat one of the four lattices, whereas
the diameter of a five-center chain is less than \(1/N\).
The centers in a single lattice are separated by exactly \(1/N\).
The radius may be chosen to avoid tangencies. Each cluster has
diameter at most \(32\rho_N\), and the boundary of its union
of disks is at distance at least \(3\rho_N\) from every pole.
Replace every intercepted piece of a segment by an arc of this
boundary, retaining the chosen side of the detour. The resulting
length is bounded by the original lengths plus \(O(N\rho_N)\).
This gives all geometric assertions; intersections and orientations
are retained as a finite chain if needed.

Integrate (8) on these paths and cluster loops. There are only
\(O(N)\) loops, each of length \(O(\rho_N)\). The residue theorem
therefore gives the claimed sum bound, without estimating individual
collision residues with singular parameter denominators. Freeze
these contours on a parameter neighborhood of radius \(c\rho_N\).
Their winding sets and pole separation persist, so their parameter
derivatives have the bounds in Lemma 1. A fixed angular compact
can be covered by polynomially many such neighborhoods. \(\square\)

Endpoint regularity is part of this statement. A prescribed endpoint
which itself is a pole cannot be retained in a regular contour. The
five admissible heights in the additive source theorem have a fixed
distance from both moving pole heights, so their horizontal endpoints
automatically meet the present hypothesis for large \(N\).

For example, let \(H_1<H_2\) be two admissible heights in
\([\epsilon,2\epsilon]\). Orient the endpoint connectors
\(v_a,v_b\) upward, from \(a_N-iH_2\) to \(a_N-iH_1\), and
from \(b_N-iH_2\) to \(b_N-iH_1\), with the chosen detours.
If \(R_\nu=(2\pi i)^{-1}\oint_{\ell_\nu}I_N\,dx\) denotes
a positively oriented grouped residue, Cauchy's theorem gives
the exact identity
\[
 L_{H_2}-L_{H_1}
   =N\left(\int_{v_a}I_N\,dx-\int_{v_b}I_N\,dx\right)
        +2\pi iN\sum_\nu m_\nu R_\nu .
 \tag{16}
\]
The integers \(m_\nu\) are the winding numbers of the retained
detoured rectangle; the construction above bounds them uniformly.
Both endpoint connectors occur. Every term
on the right, and the sum of their absolute values, obeys the
small-rate bound (8). The sign follows by traversing the lower
horizontal from left to right and the right connector upward.

On each fixed parameter neighborhood the original reflected
integrand is holomorphic inside these small clusters. Integrating
(4) proves
\[
 R_\nu=P_t A_\nu(t,u)+P_u B_\nu(t,u)
 \tag{17}
\]
with holomorphic coefficients, including all collisions. This
preserves its full mixed physical jets wherever the representative
is valid near the physical parameters. Formula (8) bounds the
residue itself; it does not assert the same bound for a chosen
pair of ideal coefficients in (17). Nor does a local statement
(17) authorize deleting its currents on an arbitrary angular
contour. The complete original trace and the actual continuation
remain part of that assertion.

For any fixed number of selected internal edges, products of the
bounded inverse pieces, detours and residues retain a polynomial
prefactor and the sum of their small rates. The unchanged other
halfwire factors, crossing carriers, angular trace kernels and
free polynomial variables remain as actual spectators. No bound
on those spectators is supplied here.

## 4. Placement in the actual relative contour calculation

The complete height transition is not (16) alone. With
\[
 C_H=N\int_{\gamma_H^-}[F_N(\mathcal R x)-I_N(x)]\,dx,
 \qquad K_H=\widehat K_H-C_H,
\]
where \(\widehat K_H=N\int_{a_N+iH}^{a_N+1+iH}F_N\,dx\),
the exact original period identity is
\[
 \widehat K_{H_2}-\widehat K_{H_1}
   =N\int_{a_N+iH_1}^{a_N+iH_2}
                   [F_N(x+1)-F_N(x)]\,dx.
 \tag{18}
\]
The period difference and (4) retain their explicit endpoint
polynomials. Thus the complete transition belongs to the original
Hermite ideal on its admitted parameter charts, with all its
connector terms present.

For precision, the existing relative descent can be used as follows.
Keep the original full angular density, including every signed
Gaussian, charge coupon and trace kernel. Cancel a displayed
\(P_N(-2\cos t_v)\) against that vertex's \(W_N(t_v)\), using
\(P_N(-2\cos t_v)W_N(t_v)=(-1)^N\), before taking its designated
angular primitive. On a common admitted product domain this gives
the actual forms \(\Theta_i\) for chart representatives
\(\Omega_i\), with
\[
 \Omega_i-\Omega_{\rm car}=d\Theta_i,
 \qquad J_{ij}=\Theta_j-\Theta_i,
 \qquad dJ_{ij}=\Omega_j-\Omega_i,
 \qquad J_{ij}+J_{jk}+J_{ki}=0.
 \tag{19}
\]
The primitives have the original symmetric angular endpoint
normalization. The moving-seam theorem gives these formulas and
their full-normal meaning; (19) is not an assumption that the
thin height charts already supply such a common product domain.

On an admitted cell subdivision, Stokes therefore represents the
original period by the sum of the local bulk integrals, minus
their oriented primitive differences on common faces, with every
original exterior face retained. The alternating corner terms
are zero by (19). There is no unknown higher-face correction.

Proposition 2 bounds all inverse wire pieces in that calculation.
It does not bound the main-half part of the angular primitives in
(19), nor prove that their face integrals vanish. The full-lens
parity cancellation in the moving-seam theorem requires the frozen
primitive paths on a common even holomorphic product domain.
Local source equivalence and the present finite atlas do not prove
that additional domain hypothesis. In particular this note supplies
no global bounded holomorphic representative, no untraced boundary
polynomial replacement, and no lower bound for the whole source.

## Direct sources and author audit

The following complete texts were read in this author sequence, and
their directly used implications were checked at the displayed pins.

- `research_additive_half_wire_source_regularization.md`:
  `af8daf3eaa16303f8297b4a712ee9debe31cabc7326776fc34c9b185f0d216a0`;
  exact source normalization, complete poles, grouped ideal identity,
  logarithmic potential and retained height transitions.
- `research_uniform_factorial_and_boundary_decay.md`:
  `4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11`;
  uniform two-sided midpoint estimate through zero and exact reflection.
- `research_moving_wire_seam_source_descent.md`:
  `2b632735243fc450e2ce0f276f339c9fad0b5524724364b83f15690b4896f33d`;
  original angular primitives, finite face compatibility and the precise
  common-domain hypothesis for integrated parity cancellation.

Only written mathematics, source reads and metadata hashes were used.
No mathematical program, numerical evaluation, test or compilation
was run. Public manuscripts and adopted notes were not edited.
