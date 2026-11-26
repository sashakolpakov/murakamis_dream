# Original cap critical points at the alternating Fourier boundary

Research theorem, 7 November 2026. Every nonempty positive three/four
prefix ending in four has a unique original critical point with its
complete ordinary left cap and outgoing Fourier parameter \(x_0\).
The fixed boundary-update inclusion has now been proved on its entire
input disk. For the prepared word \(34\), the inherited typed
images also put this point strictly inside the regular source rectangle,
giving its own nonzero local current. Physical-tail and alias comparisons
are still needed to identify that current with the whole prepared cap.

## 1. The completed whole-disk inclusion

Keep
\[
 D_3=\{|b-(.35-.01i)|\le.09\},\qquad
 D_4=\{|q-(.30-.052i)|\le.064\},
\tag{1}
\]
and the original alternating \(K=e^{2\pi ix_0}\). The
[boundary-update theorem](research_mixed_fourier_boundary_update.md)
defines the single original branch
\[
 \beta_K(q)=-\frac1{2\pi i}
  \operatorname{Log}\frac{1-Ke^{-2\pi iq}}
                          {K+(1-2K)e^{-2\pi iq}}.
\tag{2}
\]
Its analytic proof establishes regularity on a neighborhood of the
entire closed disk \(D_4\), the lower-half-plane logarithm branch,
and the original, unexponentiated identity
\[
              G_q(q,\beta_K(q))=\ell_{q,q}(x_0).
\tag{3}
\]
These conclusions do not rely on the inclusion calculation.

The sole run of
[the fixed evaluator](../experiments/check_mixed_fourier_boundary_update.py)
under [its prescribed protocol](research_mixed_fourier_boundary_update_protocol.md)
has the immutable record
[research-mixed-fourier-boundary-update.json](../repro/results/research-mixed-fourier-boundary-update.json),
SHA-256
`5d4cb057cb82ca4fff826ad768012480fd6f51afe66d3f5c632e48983cf17514`.
Its evaluator, protocol and analytic theorem hashes are, respectively,

```
5017a53b6417630f1cab1e9c4be3f71d3ad24256af1ca67a8edd8faf0be0b1cc
cc8176390334bf39e0c9cf1894fbba0ed520eee811eaf26835f3010e4e6feffd
9ff05c7f6eb759d53a3717e57b475c58904ccd35d5c232e1abdbe8b35ec49f74
```

All 512 prescribed closed arcs passed, with every domain guard true,
both independent squared-distance tests passing, no failed or
inconclusive arc, and all 20 input bindings unchanged. The calculation
used exactly 512 circular exponentials, 512 shape exponentials, 512
principal logarithms and one \(\pi\) enclosure at 256 bits.
It propagated the whole previously certified root square into
\(K=(1+2a-4a^2)^{-1}\). There was no new root solve, optimizer,
refinement, alternate branch, retry or gain evaluation.

Inspection of the stored rational upper endpoints gives
\[
 \max_{0\le j<512}U_j
 <\frac{1342213}{200000000}
 <\left(\frac{41}{500}\right)^2
 <\left(\frac9{100}\right)^2.
\tag{4}
\]
The largest saved upper is on arc 194. This comparison uses only
the recorded fractions; no analytic function is reevaluated. Each
\(U_j\) bounds the whole original arc, including its endpoints.
The maximum-modulus principle applied to the holomorphic function
\(\beta_K(q)-(.35-.01i)\) therefore proves
\[
 \boxed{\quad
 \beta_K(D_4)\subset
 \{|b-(.35-.01i)|<41/500\}
                  \subset\operatorname{int}D_3.
 \quad}
\tag{5}
\]
Compactness preserves the last strict inclusion, and the original
logarithmic identity (3), on a fixed Fourier-output neighborhood
of \(x_0\).

## 2. Every prefix ending in four

Let \(\epsilon_1,\ldots,\epsilon_m\in\{0,1\}\),
\(m\ge1\), with \(\epsilon_m=1\). The literal complete-cap
phase before eliminating its auxiliary coordinate is
\[
\begin{split}
 \mathcal H_{\boldsymbol\epsilon}(z;y)
 ={}&E(s_1,u)+\sum_{j=1}^m V_{\epsilon_j}(s_j,t_j)
       +\sum_{j<m}G(t_j,s_{j+1})+\ell_{t_m}(y),\\
 E(e,u)={}&-2J(1/2-u)-3J(u)-J(e-u)
                  +i\pi eu-\frac{i\pi}{2}(e-e^2),\\
 V_\epsilon(s,t)={}&g(s+t)-\epsilon\{g(s)+g(t)\},\\
 G(t,b)={}&g(t+b)-2g(t)-2g(b)+2\pi itb.
\end{split}
\tag{6}
\]
The original \(g,\ell,J\), chirps and additive constants are
unchanged. Write
\[
 E_0=[.33,.47]+i[-.09,.08],\quad
 U_0=[.21,.25]+i[.01,.10],\quad
 Q_0=[.23,.45]+i[-.12,.12].
\tag{7}
\]
These are the old private, auxiliary and common leg rectangles;
their notation here is distinct from the Fourier exponential \(K\).

**Theorem 1.** At \(y=x_0\), (6) has exactly one original-log
critical point in
\(U_0\times E_0\times Q_0^{2m-1}\). It has
\(u\in\operatorname{int}U_0\),
\(s_1\in\operatorname{int}E_0\), and every other leg lies
strictly inside its original typed disk \(D_{3+\epsilon_j}\).
It is simple, with
\[
       -\Re\mathcal H_{\boldsymbol\epsilon,zz}''
                        \succ(6\pi/49)I_{2m+1}.
\tag{8}
\]
The original critical branch is holomorphic for outgoing Fourier
parameters in a fixed neighborhood of \(x_0\). For each fixed
prefix it also has the original ordinary-color continuation near
the complete color. The assertion includes the one-letter prefix
\(4\); no all-three or last-type-three Fourier-end claim is made.

*Proof.* Equation (5) discharges exactly the sole inclusion hypothesis
of Theorem 3 of the boundary-update theorem. Explicitly, append an
auxiliary inverse leg \(b\in D_3\) to the old half-chain
construction. Keep each original ordinary endpoint or two-leg update,
and update the additional leg by \(b\mapsto\beta_Y(t_m)\).
All groups use old neighbors. The last leg has type four, so (5)
makes this a self-map of the full compact convex product. Brouwer's
theorem gives a fixed point.

The vertex updates solve the actual original logarithmic equations
with last incidence \(G(t_m,b)\). Identity (3) replaces just
its last-leg derivative by that of \(\ell_{t_m}(y)\).
No stationarity equation for the auxiliary \(b\) is imposed:
it is eliminated after imposing this boundary condition. The resulting
point therefore solves precisely (6), with the original logarithmic
lifts.

The one-ended Hessian allocation in Section 3 of the boundary-update
theorem proves (8) throughout the larger convex product (7), not merely
at this point. Its proof covers length one separately and keeps the
last type-four own term. Segment accretivity proves uniqueness and
nonsingularity. The strict map inclusions and the holomorphic
implicit-function theorem give continuation in \(y\), and branches
agree by uniqueness. The original complete-end action is holomorphic
in ordinary color locally; for a fixed prefix, its same nondegenerate
Hessian gives that continuation as well. \(\square\)

## 3. The actual prepared \(34\) root and its local current

For \((\epsilon_1,\epsilon_2)=(0,1)\), set
\((s,t,p,q)=(s_1,t_1,s_2,t_2)\). Eliminating
\(u=u_c(s)\) from (6) gives exactly the prepared phase
\(F=\mathcal F_{\mathrm{cap}}\), with no changed constant.
The [typed-height rectangle theorem](research_mixed_prepared_cap_typed_height_rectangle.md)
now applies unconditionally: the actual root \(z_*\) lies strictly
inside
\[
\begin{split}
 &[.27,.49]+i[-.055,.04],\qquad
   [.22,.5]+i[-.072,.021],\\
 &[.2,.42]+i[-.102,.015],\qquad
   [.2,.42]+i[-.102,.015].
\end{split}
\tag{9}
\]
This uses the already extracted endpoint images and the full-bidisk
type-four images, not a new root calculation or a cyclic five-window
bound. The full original source interpolation, strict Hessian and
gradient strips hold on the same rectangle.

Consequently its zero-frequency critical-height current has the
uniform local expansion
\[
 \mathcal M_{34,N}(y,w)
 =\kappa^3N^{-1}\mathcal B_{\mathrm{cap}}(y,w)
        e^{N\Phi_{\mathrm{cap}}(y,w)}(1+O(N^{-1})),
\tag{10}
\]
where
\[
 \Phi_{\mathrm{cap}}(y,w)=F(z_*(y,w);y,w),\qquad
 \mathcal B_{\mathrm{cap}}(y,w)=
 \frac{(2\pi)^2b_{\mathrm{cap}}(z_*(y,w);y,w)}
             {\sqrt{\det[-F''(z_*(y,w);y,w)]}}\ne0.
\tag{11}
\]
Here \(\mathcal M_{34,N}\) is precisely the current defined in
Section 3 of [the full-source criterion](research_mixed_prepared_cap_full_source_criterion.md),
before its physical and lattice corrections are added. Strict
horizontal concavity gives a unique maximum and a gap on that
current away from \(z_*\). The exact row has power \(N^{-3}\),
the lattice integral has \(N^4\), and the four-dimensional
Gaussian contributes \(N^{-2}\), giving \(N^{-1}\).
Every factor of its own symbol is nonzero on (9). The original
oriented Gaussian determines the square root in (11).
These assertions retain both parities and fixed ordinary/Fourier
derivatives of the normalized error on smaller neighborhoods.

The root also supplies the regular admitted preimage of the rational
Fourier closing map in
[the critical-curve theorem](research_mixed_prepared_three_four_cap_critical_curve.md),
with its chamber filter and the enlarged heights (9). The zero-lift
argument is unchanged because it uses only real ranges. Its
tridiagonal derivative proof still gives \(\mathcal Y'(U)\ne0\).
No value of this preimage or its action has been evaluated here.

## 4. The precise remaining source work

The critical-point hypothesis of the full-source criterion is now
proved. Its other two hypotheses remain open: the coherent physical-tail
bound, including the far ceiling \(146/75\) and eight real faces,
must be below \(\Re\Phi_{\mathrm{cap}}(x_0,-2)\); and the
eight enlarged-height alias maxima must be below that same actual
action. The common-height join and vertical-current arguments then
require no further comparison families.

Thus (10) is not yet an asymptotic for the whole
\(v(-2)^TA_3A_4h(y)\). Neither an outgoing whole-period
envelope, propagation of an arbitrary incoming message, a new
short-filling stability theorem, nor a knot-family conclusion follows
from critical existence. All frozen source, protocol and failed or
successful calculation records remain unchanged.
