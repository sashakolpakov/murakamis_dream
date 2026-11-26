# Extending the initial 3,4 boundary interval and adjoining the remaining factors

Research deduction, 10 November 2026. The complete first-pair estimate
can be joined to every following unselected ordinary factor. This
extends the first integration interval of the known plateau contribution
from \([.22,.45]\) to \([.1,.45]\), while all other retained real
coordinates stay in \([.22,.45]\). The added integral is exponentially
smaller than the original geometric contribution. Its addition therefore
preserves the nonzero coefficient, not merely the upper exponential rate.

There is also a boundary estimate that can be joined to the already
controlled unrestricted middle. Both assertions concern the original
finite source. They leave the other boundary intervals, selections and
contour joins to be estimated separately.

## 1. Source, reference and intervals

Fix a positive three/four open word of length \(m\ge3\) beginning
with \(3,4\). Write \(n_j=3+\epsilon_j\), so
\(\epsilon_1=0\), \(\epsilon_2=1\), and let
\[
 h=m-1,\qquad k_4=\sum_{j=1}^m\epsilon_j,
 \qquad r_j=a_j+ic_j,\qquad X_j=e^{-2\pi iz_j}.
\tag{1}
\]
The \(r_j\) are the retained coordinates of the original geometric
solution, with its original logarithmic lifts. Contract the terminal
coordinate exactly, as in the whole unselected plateau theorem. The
unselected integrand is
\[
 \mathscr J_N(\mathbf z;w_L,w_R)=
 U_{0,N}(w_L,X_1)
 \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
 \mathcal V_{\epsilon_m,N}(w_R,X_h)
 \prod_{j=1}^{h}d_N(X_j)^{\epsilon_j}.
\tag{2}
\]
Here \(U\) is the complete first cap, \(C\) the complete ordinary
finite sum, \(d_N\) the reciprocal-factorial interpolation polynomial,
and \(\mathcal V\) the complete terminal transform. The transform
already includes every terminal row, weight and Fourier alternative.
At the retained coordinates, (2) uses the unselected term. Its original
external scalar is
\[
 \kappa_N^{m+k_4}N^{m+k_4-1},\qquad |\kappa_N|=1.
\tag{3}
\]
The variables \(w_L,w_R\) are the ordinary boundary colors, with
complete colors \((-2,-2)\).

Put
\[
 P=[11/50,9/20],\quad E=[1/10,11/50],\quad
 \kappa_0=1/2500000,\quad
 \gamma=\kappa_0(a_1-11/50)^2>0.
\tag{4}
\]
The strict inequality uses the actual first-three bound \(a_1>.278\).
All targets in this note retain their original heights unless the
middle or right-boundary theorem explicitly specifies a different one.
For the rectangular domains below, \(z_j=x_j+ic_j\) and
\(u_j=x_j-a_j\).

## 2. The added rectangular integral is exponentially smaller

Let \(L_0\), \(\phi_j\) and \(\Pi\) denote the allocated cap,
ordinary and terminal phases of the whole unselected plateau theorem.
One half of each type-four weight belongs to each of its two incident
factors. The original phase identity and critical equations give
\[
 \begin{split}
 M&=\Re\left\{L_0(r_1)+\sum_{j=2}^{h}
                  \phi_j(r_{j-1},r_j)+\Pi(r_h)\right\},\\
 L_0'(r_1)+\partial_1\phi_2(r_1,r_2)&=0,\\
 \partial_2\phi_j+\partial_1\phi_{j+1}&=0\quad(2\le j<h),\\
 \partial_2\phi_h+\Pi'(r_h)&=0.
 \end{split}
\tag{5}
\]
Derivatives without displayed arguments are evaluated at the original
reference. The number \(M\) is the real part of the original full
geometric action.

**Proposition 1.** For every \(\tau>0\), both level parities obey
\[
 |\mathscr J_N|\le C_{m,\tau}N^{A_{m,\tau}}
 \exp N\left\{M-\gamma-2\kappa_0\sum_{j=2}^{h}u_j^2+\tau\right\}
\tag{6}
\]
on \(E\times P^{h-1}\), at the fixed reference heights. The
ordinary colors may vary in sufficiently small fixed complex disks
about \((-2,-2)\). Every fixed derivative in those colors satisfies
the same upper rate on smaller disks.

*Proof.* The complete early first-pair theorem bounds
\[
 |U_{0,N}(w_L,X_1)C_{1,N}(X_1,X_2)|\,|d_N(X_2)|^{1/2}
\]
by a polynomial times the exponential with rate
\[
 \Re L_0(r_1)+\Re\phi_2(r_1,r_2)
 +\Re\partial_2\phi_2(r_1,r_2)u_2
                  -\kappa_0u_2^2-\gamma+\tau_2.
\tag{7}
\]
It includes all low, central and high ordinary rows at all actual
heights. Its own-four private-height condition is automatic.

For \(j=3,\ldots,h\), use the complete ordinary supporting
planes at \((x_{j-1},x_j)\in P^2\). Finally use the complete
terminal plane at \(x_h\in P\). Their factors carry precisely
the remaining halfweights in (2). Equation (5) cancels every
linear term and adds the constants to \(M\). Each coordinate
\(j\ge2\) receives two quadratic losses. For \(h=2\), the
second loss at coordinate two comes directly from the terminal
plane; there is no intervening ordinary factor. Thus the same
argument includes length three.

Choose the finitely many source tolerances to total at most
\(\tau\). The weight identities hold also at their zeros,
without division. Intersect the finitely many ordinary-color disks
and use Cauchy's formula on smaller disks for the derivative
assertion. This proves (6). \(\square\)

Let \(\mathcal Z_N^+\) be the scalar (3) times the integral
of (2) over
\[
 [1/10,9/20]\times P^{h-1}
\tag{8}
\]
at these fixed heights and the original angular orientation. Let
\(\mathcal Z_N^P\) be the already proved integral over \(P^h\).
Their difference is exactly the integral over \(E\times P^{h-1}\);
the common boundary has measure zero. Hence (6), with its fixed
domain volume and the polynomial scalar (3), gives
\[
 |\mathcal Z_N^+-\mathcal Z_N^P|
       \le C N^A e^{N(M-\gamma+\tau)}.
\tag{9}
\]

**Corollary 2.** The enlarged integral has the original nonzero
asymptotic
\[
 \mathcal Z_N^+(\mathbf w)=
 \kappa_N^{m+k_4}N^{-3/2}A_m(\mathbf w)
 e^{N\mathcal F_m(\mathbf w)}
                  \{1+O_{\rm hol}(N^{-1})\},
 \qquad A_m(\mathbf w)\ne0,
\tag{10}
\]
on sufficiently small fixed ordinary-color disks, through both
level parities. The action, Gaussian branch and coefficient are
those of the whole unselected plateau theorem. In particular all
fixed ordinary-color jets retain their previously proved leading
terms.

*Proof.* That theorem gives (10) for \(\mathcal Z_N^P\).
Take \(\tau<\gamma/8\) in (9), and shrink the fixed color
disks so that \(\Re\mathcal F_m(\mathbf w)>M-\gamma/8\)
and the original amplitude is bounded away from zero. The quotient
of (9) by the leading term in (10) is then exponentially small,
even after its polynomial prefactor. The quotient is holomorphic;
Cauchy's formula preserves this conclusion for every fixed jet
on smaller disks. Thus the addition leaves the relative error in
(10) and its nonzero coefficient unchanged. \(\square\)

This constructs and estimates the larger restricted integral (8).
It does not assert that (8) is the entire torus period, or deform
the unestimated portions of the original contour into it.

## 3. The same first pair supplies a boundary estimate for an unrestricted middle

Take safe cuts \(p,\ldots,q\) and the protected triples of the
completed boundary propagation theorem, with \(p\ge3\) and the
first pair outside those triples. In the prefix through coordinate
\(p-1\), use \(x_1\in E\), \(x_2,\ldots,x_{p-1}\in P\),
all selections zero and all heights unchanged. Define its literal
modulus by
\[
 L_N=|U_{0,N}|\prod_{j=2}^{p-1}|C_{\epsilon_j,N}|
       \prod_{j=1}^{p-2}|d_N(X_j)|^{\epsilon_j}
       |d_N(X_{p-1})|^{\epsilon_{p-1}/2}.
\tag{11}
\]
Set
\[
 M_L=\Re\left\{L_0(r_1)+
                     \sum_{j=2}^{p-1}\phi_j(r_{j-1},r_j)\right\},
 \qquad P_{p,a}=\partial_1\phi_p(r_{p-1},r_p),
\]
and retain the original calibrated boundary rate
\[
 G_{L,N}=N^{-1}\log L_N-M_L+
                  \Re[P_{p,a}(z_{p-1}-r_{p-1})].
\tag{12}
\]
Use \(\log0=-\infty\). The same multiplication as in
Proposition 1, stopped at this cut, gives
\[
 G_{L,N}\le-\gamma-\kappa_0
       \left(2\sum_{j=2}^{p-2}u_j^2+u_{p-1}^2\right)
                     +\tau+O_m(\log N/N).
\tag{13}
\]
The last marginal cancels because
\(\partial_2\phi_{p-1}+P_{p,a}=0\). The other half of the
cut weight belongs to the middle factor.

The boundary propagation theorem has the exact middle inequality
\[
 N^{-1}\log|\mathscr J_{\sigma,N}|-M
 \le G_{L,N}+G_{R,N}-\kappa_I\sum_{i\in F}p_i
                            +\eta+O_m(\log N/N),
 \qquad\kappa_I=1/20000.
\tag{14}
\]
Here \(F\) is its free middle interval, and
\(p_i=\min\{1,\sigma_i+400(\operatorname{clamp}_P x_i-a_i)^2\}\).
The middle retains the original height rules and Fourier choices.
Every protected coordinate is unselected in \(P\); the original
safety halos and cut conditions are retained.

Choose either exact source chart and any right-boundary case proved
for that chart in the propagation theorem. If its calibrated rate
is \(G_{R,N}\le-\Delta_R-K_R+\eta+O_m(\log N/N)\),
then (13)--(14) imply
\[
 |\mathscr J_{\sigma,N}|\le C N^A
 \exp N\left\{M-\gamma-\Delta_R-K_R
                  -\kappa_I\sum_{i\in F}p_i+\tau\right\}.
\tag{15}
\]
For example, the contracted right part with every retained target
unselected in \(P\) has \(\Delta_R=K_R=0\). The other
completed right-boundary cases retain their own type, height and
selection requirements. The two source charts are not combined.

No middle estimate is reapplied to the first coordinate. The new
prefix is inserted only through its boundary quantity (12); all
synthetic closing losses and original middle tangents remain the
ones in (14). Thus (15) is a pointwise bound for the exact source
at the stated coordinates, and for its integrals over any specified
bounded pieces of this domain. It supplies no missing vertical join
between the fixed prefix heights and another contour. In particular
the small loss \(\gamma\) must be retained: it is not replaced by
the larger common loss for the older active-boundary cases.

## 4. Remaining scope

The nonzero coefficient in (10) belongs to the explicitly enlarged
rectangular contribution. Formula (15) permits arbitrary controlled
interior states behind this boundary, subject to the protected triples
and the existing right-boundary domains. Neither statement controls
every first boundary interval, arbitrary selected coordinates near
that boundary, or changing-height joins. They do not yet prove a
whole-word asymptotic, a new closed-knot family, or stability under
every short partial filling.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_early_own_four_high_rows.md | 62c3d5070d15c093ae8ab10cb373e9624a497d29743d6cd909bc5d7a33daebb6 |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_completed_boundary_state_propagation.md | cc7b2fc0db168d00e2b75b54ec3ff51496f178e819e4e5c8d5c6b53af563cb48 |
| research_mixed_clean_closing_edges_completion.md | cc5b75d521fe648ab5aa0974e162de02b14fb814fc628635a1126349df5dfca9 |

The proofs and source domains used above were read directly. This is
written theorem assembly, with no new numerical evaluation, replay,
saved-value arithmetic, import, test or compilation. Frozen sources
are unchanged.
