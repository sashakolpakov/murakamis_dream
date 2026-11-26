# Overlapping spectral windows and their exact seam transport

Private written proof, 16 November 2026.

Short spectral repairs use one holomorphic function on both angular
sides. Enlarging their repair windows beyond the cells assigned to the
trace gives an additional exact property: neighboring representatives
have the same values and normals on the shared rows. Their difference
is divisible by the shared-node factor of the original relation.
The original seam density consequently has no pole at those rows,
and its two-sided estimate retains the usual filling-density decay.

This permits local seam transport through a real overlap without a
physical-pole residue. All endpoint connectors and additional faces
remain. The statement does not construct a global deformation to a
parent-height slice or bound the untouched spectators along one.

## 1. Source data and enlarged repair windows

Use
\[
 N\ge2,\quad \eta=(-1)^{N-1},\quad
 c_j=2\cos((2j+1)\pi/N),\quad
 0\le j\le J_N=\lfloor(N-1)/2\rfloor,
 \quad P_N(z)=2T_N(z/2)+2.
 \tag{1}
\]
The multiplicity \(\nu_j\) is two except for the odd-level simple
node \(c_{J_N}=-2\), where it is one. Retain the original rows
\[
 F_j(w)=K_N(c_j,w),\qquad
 G_j(w)=\partial_zK_N(c_j,w)
 \tag{2}
\]
and the pinned pole-free normal \(\widehat G_j\) at double rows.
It has all the required physical second-endpoint jets of \(G_j\).
At a free complex endpoint the two functions are not identified.

Fix buffered product domains and compacts on which the short spectral
repair theorem applies. For an edge \(e=vw\), write its representatives
as \(\mathcal K^e_{I_v,I_w,N}\), with the original phase \(\Psi_e\).
Their repair windows have been chosen short enough after the actual
baseline error exponent. For every fixed finite collection using the
same edge baseline \(h_{e,N}\), that theorem gives
\[
 \mathcal K^e_{I_v,I_w,N}
       =e^{N\Psi_e}\{h_{e,N}+O(e^{-c_eN})\},\qquad
 |h_{e,N}|\le e^{o(N)}.
 \tag{3}
\]
This holds on the entire fixed smaller product compact, on both
angular sides, with buffered derivatives. Each representative is
spectral and obeys exactly
\[
 \begin{split}
 \mathcal K^e_{I_v,I_w,N}(c_j,w)&=F_j(w),\\
 \partial_z\mathcal K^e_{I_v,I_w,N}(c_j,w)&=\widehat G_j(w)
                                      \quad(\nu_j=2)
 \end{split}
 \tag{4}
\]
for \(j\in I_v\), and the analogous identities at \(I_w\).
At a joint selected physical pair, all required mixed jets are the
original ones.

Assign a trace cell \(B_v\) to a smaller consecutive block inside
its repair window \(I_v\). Adjacent trace cells may be disjoint,
while their enlarged repair windows overlap in a fixed interval
of rows. All real intervals and their buffers are chosen before
\(N\); midpoint rounding changes their endpoints by \(O(N^{-1})\).
There is only a fixed finite number of cells. Only rows in the
eligible intervals of the short-repair theorem are included.
Uncovered physical rows remain in the original source.

**Proposition 1.** For any fixed finite network and a fixed tuple
of assigned trace cells, simultaneous replacement of internal edges
by these representatives preserves the original tensor cell trace.
Every crossing and shared-vertex product normal is retained.

**Proof.** At each physical tuple in the cells, apply at most one
spectral derivative in each variable belonging to a double node.
An edge then receives its value, one first normal, or its mixed
first normal. All are unchanged by (4) and its joint-jet assertion.
The ordinary product rule therefore preserves the full tensor jet
of the source, including the original crossings and any other
spectators. The tensor of the original finite local residue
functionals gives the same cell trace.

This argument precedes every contour or magnitude estimate. It
also applies to repeated edges and to an identified shared variable,
provided the original endpoint tensor jets are retained before
the identification. A simple spectral node contributes only its
original value. No normal is added there.
\(\square\)

Only edges whose prescribed endpoints are subsequently traced on
their selected windows are replaced in Proposition 1. Factors at
genuinely free external colors stay as their original ordinary
polynomials. For a single first-window trace with a still-complex
second endpoint, the exact contour instead represents
\(\Phi^\sharp\), as in the pinned repair theorem; agreement with
the original follows after the required subsequent second trace.
No off-grid free-boundary equality is inferred.

## 2. The shared-node ideal

Consider two neighboring cell labels differing at just one vertex
\(v\). All other repair-window labels are held fixed. Let
\(A_N\) and \(A_N'\) be the two products of repaired internal
edge factors, including their common unchanged repaired edge
factors subject to (3). Any further original or unbounded source
factor belongs to the spectator \(S_N\) in Section 4, rather
than to this bounded product. Put
\[
 \Delta_N(z_v,\mathbf z')=A_N-A_N',\qquad
 O_{v,N}=I_v\cap I_v',\qquad
 Q_{v,N}(z)=\prod_{j\in O_{v,N}}(z-c_j)^{\nu_j}.
 \tag{5}
\]

**Proposition 2.** On the admitted product domain,
\[
                   \Delta_N=Q_{v,N}B_{v,N}
 \tag{6}
\]
with \(B_{v,N}\) jointly holomorphic. Consequently
\[
 \frac{\Delta_N}{P_N}
     =\frac{B_{v,N}}{P_N/Q_{v,N}}
 \tag{7}
\]
has no pole at any shared row, including the odd simple node.
All required derivatives in the remaining parameters preserve
this removability.

**Proof.** At a shared first row, (4) is independent of the
chosen repair-window label. It is an identity as a function
of every other complex endpoint. Hence every changed incident
edge has the same value and, when required, first normal in
the two products. The product rule gives
\[
 \Delta_N(c_j,\mathbf z')=0,\qquad
 \partial_{z_v}\Delta_N(c_j,\mathbf z')=0
                                      \quad(\nu_j=2).
 \tag{8}
\]
At the odd simple node only the first equality is used.
Ordinary holomorphic division by these distinct linear factors
gives (6), jointly in the parameters. It also proves (7).
Since the node factors are independent of the other variables,
their fixed derivatives retain the division.
\(\square\)

If several vertex labels change, telescope one vertex at a time.
Proposition 2 applies to each resulting seam with the other labels
fixed. It does not assert divisibility at \(v\) for an arbitrary
simultaneous change of unrelated factors.

The finite product estimate in (3) also gives, on the fixed compact,
\[
 \Delta_N=e^{N\Psi_{\rm rep}}r_N,\qquad
 |r_N|\le e^{-cN+o(N)},\qquad
 \Psi_{\rm rep}=\sum_{e\ {\rm represented}}\Psi_e,\quad c>0.
 \tag{9}
\]
No inverse amplitude or nonzero lower bound is used: telescope
the finite product, put one exponentially small difference in
each term, and use the \(e^{o(N)}\) bounds on the other factors.
An unreplaced or otherwise unbounded spectator is not included
in the right side of (9); its actual size remains a supplied factor.

## 3. The trace-kernel estimate through the shared grid

Use \(z=-2\cos t\). Choose a real angular interval
\([a_N,b_N]\) whose physical nodes all belong to the shared
window, with a fixed larger shared-row buffer. Its endpoints
are midpoints of the full angular grid, so
\[
                 (-1)^N\cos(Na_N)
                  =(-1)^N\cos(Nb_N)=1.
 \tag{10}
\]
For a fold window it may be the single symmetric interval
containing zero. Away from the fold it may be one member of
a pair of reflected intervals. Fix \(H>0\) such that a buffered
rectangle \([a_N,b_N]+i[-H,H]\) and the retained parameter
compacts lie in the source domain for (9). The estimates below
are for sufficiently large \(N\).

**Theorem 3.** On a slightly smaller such rectangle, including
its removable physical points,
\[
 \left|
 e^{-N\Psi_{\rm rep}(t,\mathbf z')}
       \frac{\Delta_N(-2\cos t,\mathbf z')}
            {P_N(-2\cos t)}
 \right|
 \le \exp\{-cN-N|\Im t|+o(N)\}.
 \tag{11}
\]
The positive constant \(c\) may be decreased once. The estimate
is uniform in the buffered remaining parameters; fixed
derivatives have polynomial losses after the stated buffers.

**Proof.** The quotient is holomorphic through every real
node in this rectangle by (7). In the odd case, a simple
spectral zero pulls back to a double angular zero at \(t=0\);
no spectral normal is needed for that conclusion.

Exactly,
\[
 P_N(-2\cos t)=2+2(-1)^N\cos Nt.
 \tag{12}
\]
On either vertical midpoint side its modulus equals
\(2+2\cosh(N\Im t)\). For \(|\Im t|\ge N^{-1}\), the
factorization of (12) gives
\[
 |P_N(-2\cos t)|
 \ge e^{N|\Im t|}(1-e^{-N|\Im t|})^2
 \ge (1-e^{-1})^2e^{N|\Im t|}.
 \tag{13}
\]
This proves (11) off the central thin rectangle.

On the thin rectangle of height \(N^{-1}\), apply the maximum
principle to the holomorphic quotient \(r_N/P_N\).
The vertical boundary denominator is at least four, and
(13) supplies a fixed lower bound on its horizontal boundary.
Equation (9) thus bounds this quotient by \(e^{-cN+o(N)}\)
throughout. Since \(e^{-N|\Im t|}\ge e^{-1}\) there,
this is also (11), after a fixed constant. The argument is
uniform in the other parameters.

Use a slightly larger shared-row rectangle for derivative
estimates. Angular Cauchy disks of radius a fixed multiple
of \(N^{-1}\) cost powers of \(N\), and change the height
factor in (11) by only a constant. Buffered derivatives in
the other parameters are handled by their fixed Cauchy
neighborhoods. At the fold, the quotient is spectral:
ordinary spectral derivatives are obtained using disks of
radius a fixed multiple of \(N^{-2}\). The physical
quadratic spacing and the larger shared buffer keep these
disks in the removable region; their angular preimages
change height by \(O(N^{-1})\). This again costs only powers
of \(N\), without adding a simple-node datum.
\(\square\)

For the literal angular trace density retain
\[
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2},\qquad
 P_N(-2\cos t)W_N(t)=(-1)^N.
 \tag{14}
\]
Thus Theorem 3 gives its usual \(e^{-N|\Im t|}\) loss,
with the additional \(e^{-cN}\) saving for the seam.
It has no opposite-half growth factor from a one-sided repair.
The original sine, crossing carrier, charge coupons and
entire remaining spectator still multiply this estimate.

## 4. Exact transport, with its endpoint currents

Let \(S_N(z,\mathbf z')\) be the actual remaining spectator,
holomorphic on the proposed transport region; otherwise
retain its poles and their residues explicitly. The first
spectral seam form is
\[
 \omega_{v,N}
   =\frac{\eta N^2}{2\pi i}
        S_N(z,\mathbf z')\frac{\Delta_N(z,\mathbf z')}{P_N(z)}
                                                            \,dz.
 \tag{15}
\]
Its apparent poles at the shared rows are removable by
Proposition 2. Other original trace kernels, free boundary
polynomials and shared parameters remain in \(S_N\), or in
the remaining original differential forms.

Take two oriented paths \(\gamma_0:a_0\to b_0\) and
\(\gamma_1:a_1\to b_1\), with endpoint connectors
\(\alpha:a_0\to a_1\) and \(\beta:b_0\to b_1\).
Suppose their homotopy stays in the stated holomorphic
region except for any explicitly listed crossed poles.
With the boundary orientation
\(\gamma_0+\beta-\gamma_1-\alpha\), exactly
\[
 \int_{\gamma_0}\omega_{v,N}-\int_{\gamma_1}\omega_{v,N}
  =\int_\alpha\omega_{v,N}-\int_\beta\omega_{v,N}
     +2\pi i\sum_p {\rm wind}_p\,
                             {\rm Res}_p\omega_{v,N}.
 \tag{16}
\]
There is no residue term from a shared physical node.
If no other pole is crossed, the displayed sum is empty.
The endpoint connectors are not set to zero.

**Proof.** This is Cauchy's theorem for (15), after the
actual removable division (7). At a remaining pole use
its original residue, with the winding of the displayed
boundary. Holomorphic parameter dependence allows the
same identity before applying every remaining original
trace and fixed derivative. No product of independently
closed bounds is substituted for that shared closing.
\(\square\)

For a joint chain the same statement has the usual relative
form. Integrate the coefficient of the seam form in its
designated variable on a common simply connected admitted
domain, retaining all remaining differentials. If
\(\omega=d\Theta\), then
\[
                 \int_\Gamma\omega=\int_{\partial\Gamma}\Theta .
 \tag{17}
\]
Only faces whose pullbacks actually vanish can be removed.
Every additional angular, parameter, slit, or exterior face
remains in (17). Freezing the other variables and using
(16) is sufficient when no joint primitive is supplied.
No equality of bulk integrals alone follows from (17)
in the presence of an unestimated boundary current.

If a proposed path lies in the rectangle of Theorem 3,
its seam integral is bounded by its actual spectator norm
times the phase weight in (11), its length and polynomial
normalizations. A parent-action conclusion requires an
inequality for that entire weight along the path and its
connectors. In particular a calibration on a prescribed
positive horizontal slice supplies no estimate for all
intermediate heights or all real angles.

## 5. A single lower-lens formula for even spectral cells

There is an exact simplification independent of the seam
estimate. Let \(\mathcal I\) be the symmetric union of
angular intervals representing a selected spectral cell.
Away from the fold it consists of \([a,b]\) and
\([-b,-a]\), \(0<a<b<\pi\). A cell meeting the fold gives
one self-paired interval \([-b,b]\). Endpoints are
nonphysical midpoint angles. Unions of such cells are
handled component by component.

Let \(A_N(t)\) be the angular pullback of the selected
spectral source and every spectral spectator. It is even,
with the other variables frozen. Retain the literal
original even carrier
\[
 E_N(t)=e^{inNt^2/(4\pi)}\cos(N(1-\chi)t),\qquad
 C_{N,n}=e^{\pi i n(N-1)^2/(4N)},
 \tag{18}
\]
with the original signed integer \(n\), charge and all
normalization conventions. Put
\[
                       q_N(t)=\sin t\,W_N(t)E_N(t)A_N(t).
 \tag{19}
\]
Since \(W_N(-t)=W_N(t)\), this is an odd meromorphic
function with the original physical poles.

For each component interval \(L\) of \(\mathcal I\), choose
a lower path \(\Gamma_L^-\), oriented left to right, below
the selected real poles with the original winding. Define
its upper partner by
\[
                  \Gamma_L^+=R\Gamma_{-L}^-,
                        \qquad R(t)=-t .
 \tag{20}
\]
It runs right to left above \(L\). All paths and
spectators must remain in the admitted domains.

**Theorem 4.** The original restricted sharp cell trace is
\[
 \begin{split}
 \mathfrak L^\sharp_{n,\chi,N,\mathcal I}[A_N]
 &=-\frac{N^2C_{N,n}}{2\pi i}
          \sum_L\int_{\Gamma_L^-+\Gamma_L^+}q_N(t)\,dt\\
 &=-\frac{N^2C_{N,n}}{\pi i}
          \sum_L\int_{\Gamma_L^-}q_N(t)\,dt .
 \end{split}
 \tag{21}
\]
It has no real closing interface. It retains all lower
exterior paths and their endpoints. Both disjoint
reflected cells and the fold cell have their original
spectral multiplicities.

**Proof.** The first line is the original closed angular
residue formula. One can obtain its factor directly from
the spectral contour in the short-repair theorem: the
symmetric angular contour covers the spectral contour
twice, \(dz=2\sin t\,dt\), and
\(\eta/P_N=-W_N\). The original carrier in (18) and its
physical normals are exactly those of the pinned lens
source.

Oddness gives the one-form identity
\[
                          R^*(q_N(t)\,dt)=q_N(t)\,dt .
 \tag{22}
\]
Thus the upper integral for \(L\) equals the lower
integral for its partner \(-L\). Summing over all
components doubles the lower sum and proves (21).
There is no sign cancellation of that lower sum.

For clarity, at a double physical angle the principal
part of \(W_N\) is \(-\eta/[N^2(t-\tau)^2]\).
The two angular lifts together give exactly the
original spectral value/first-normal residue. At odd
level the central angle is zero, \(\eta=1\), and
\[
             q_N(t)=-\frac{E_N(0)A_N(0)}{N^2t}+O(1).
 \tag{23}
\]
The closed prefactor in (21) gives the single central
value \(C_{N,n}E_N(0)A_N(0)\). No spectral normal is used.
The reflected lower formula gives that same value.
This also explains why no unregularized real integral
through a physical pole is needed in the argument.
\(\square\)

If a chosen contour decomposition introduces real
closing arcs, their cancellation must use this paired
orientation and its pole convention. Treating a real
path through the physical grid as an ordinary integral,
or halving the simple-node residue again, would change
the trace. Equation (21) avoids both ambiguities.

## 6. Assembly scope and direct sources

The results combine in a finite fixed network as follows:
tensor cell replacements are exact; neighboring labels
have a genuine shared-node ideal; their original seam
densities can cross those shared real nodes without a
new residue; and each even spectral cell uses one lower
lens without a real repair interface. Every assertion
retains full normals and the actual shared products.

The remaining task is geometric and analytic: choose the
whole coupled contour, retain its unmatched rows and all
boundary faces, and bound the actual spectators and
connectors at the required parent action. Theorem 3
does not supply that global inequality. Neither does
the zero local repair interface identify a nonzero
geometric scalar coefficient.

Complete direct sources used in this proof are:

* [Short spectral window repair](research_short_spectral_window_repair.md),
  SHA256 581ccd3ec9232a6aa1f42172fcff856f94a6d76efccc001bd411cf2243de2550:
  exact two-line spectral data, both-sided action estimates,
  common baselines, sharp trace and odd-node conventions.
* [Original joint factorial/lens source](research_joint_factorial_lens_relative_source.md),
  SHA256 a14ca148bd55b36b1eea9de8be8a63025532c3bbbb928482b0d7cb8edae56e54:
  original signed and charged lens normalization, full physical
  normals, free polynomial scope and relative boundary bookkeeping.

Only written mathematics, source reads and metadata hashes are used.
No mathematical program, numerical computation, test or compilation
is run. Frozen notes and public manuscripts are unchanged.
