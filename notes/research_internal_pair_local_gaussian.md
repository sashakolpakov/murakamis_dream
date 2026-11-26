# Actual local Gaussian preparation for every positive internal pair

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

For every fixed pair of integer powers \(n,p\ge3\), the original
mixed wire and trace density with its low-index complete outside
edges has a nonzero Gaussian component at its geometric critical
point, through both level parities. At odd levels those outside
edges equal the full original kernels.
Section 6 upgrades the local conclusion to the full original
complete-end factors at both parities on the actual pair domain.
Sections 1–6 obtain its norm and relative annihilation residual from
the exact physical-row normalization. Section 7 uses the sharper edge
packet to compute a fixed, nonzero leading amplitude and the precise
power \(N^{-3/2}\). It also allows both outside colors to vary in
fixed complex neighborhoods. Neither argument assumes an asymptotic
for the filled pair.

This is a local source theorem. It neither identifies the coefficient
of this local contour in the whole original cycle nor bounds that
cycle's complement. The free-boundary statement in Section 7 includes
all fixed ordinary boundary derivatives, but still concerns only the
localized contour.

## 1. The exact density and the geometric point

Put \(D=N-1\), \(\eta=(-1)^D\), and
\[
 C_{N,k}=\exp\!\left(\frac{\pi i kD^2}{4N}\right).
 \tag{1}
\]
Use the original Newton kernel and full Frobenius trace. Write
\(L_N^{\rm ind}=N-1-\lfloor N/2\rfloor\), and retain the literal
low-index complete-end factor
\[
 \mathcal K_N(t)
   =\sum_{j=0}^{L_N^{\rm ind}}e_j(-2\cos t)e_j(-2).
\]
At odd levels \(\mathcal K_N(t)=K_N(t,0)\) exactly: every removed
radical polynomial vanishes at the simple physical node \(-2\).
At even levels only the low-index sector is used. The source
under consideration is
\[
 \mathcal P^{\rm low\,out}_{n,p,N}
  =\phi_N^{(t)}\phi_N^{(r)}
       [R(t)^nR(r)^p\mathcal K_N(t)K_N(t,r)\mathcal K_N(r)].
 \tag{2}
\]
In particular the two selected vertices have degree two, each with
its literal complete outside edge. The original first normal at
every double physical root remains in each trace.

The [exact wire averaging theorem](research_internal_wire_exact_circle_averaging.md)
gives
\[
 \begin{split}
 \mathcal P^{\rm low\,out}_{n,p,N}
   &=N\int_{iY}^{1+iY}W_{n,N}(x)W_{p,N}(x)\,dx,\\
 W_{k,N}(x)&=\phi_N[R^k\mathbf B_N(x)\mathcal K_N].
 \end{split}
 \tag{3}
\]
The half-band quotient-valued \(\mathbf B_N(x)\) retains all physical
jets. Its exact factorial representative at those jets is
\[
 B_N(x,t)=
 \frac{N}{
 G_N(N(1/2-x+t/(2\pi))-1/2)
 G_N(N(1/2-x-t/(2\pi))-1/2)G_N(Nx)^2}.
 \tag{4}
\]
Here \(G_N\) is the original
[canonical sine factorial](exact_factorial_interpolation_and_complex_contours.md).
The numerator \(N\) follows from its exact reflection identity.
Formula (4) is not asserted to equal the canonical polynomial at
arbitrary angular points. Agreement of the full physical jets is
the reason it is legitimate in the original residue trace.

Write \(z=(x,t,r)\). In a regular lower-horizontal trace chart define
the exact holomorphic density
\[
 \begin{split}
 I_N(z)={}&B_N(x,t)B_N(x,r)\mathcal K_N(t)\mathcal K_N(r)\sin t\sin r\\
 &{}\times
 \frac{\exp\{iN(nt^2+pr^2)/(4\pi)-iN(t+r)\}}
 {(1-\eta e^{-iNt})^2(1-\eta e^{-iNr})^2}.
 \end{split}
 \tag{5}
\]
The [original trace formula](research_exact_complete_trace_contour.md)
has lower-horizontal scalar \(iN^2C_{N,k}/\pi\) for each selected
vertex. Thus the corresponding three-dimensional density, including
the wire factor in (3), is
\[
 -\frac{C_{N,n}C_{N,p}N^5}{\pi^2}\,I_N(z)\,dx\,dt\,dr.
 \tag{6}
\]
No first normal or higher charge in the rational denominators has
been discarded. Other trace segments, physical rows, and any
interpolation-divisor currents are not represented by (5); their
place in a global deformation is a separate problem.

Use the original primitives
\[
 \begin{split}
 J'(v)&=\Log(2\sin\pi v),\qquad J(0)=0,\\
 b(x,t)&=-J(1/2-x+t/(2\pi))
         -J(1/2-x-t/(2\pi))-2J(x),\\
 \Phi(z)&=b(x,t)+b(x,r)+\psi(t,0)+\psi(r,0)
                 +\frac{i(nt^2+pr^2)}{4\pi}-i(t+r).
 \end{split}
 \tag{7}
\]
The \(J\) branch is continued from \(0<v<1\) in
\(0<\Re v<1\); the edge phase has its original complete constant.

Let \(z_*=(x_*,t_*,r_*)\) be the positive geometric point of this
internal pair at unit charges. Its existence is supplied by the
[positive charge-cube theorem](research_positive_path_fractional_charge_cube.md).
The [internal-pair angle bound](research_internal_pair_angle_bound.md)
gives
\[
 0<\Re t_*,\Re r_*<\pi/2,\qquad
 \Im t_*,\Im r_*<0.
 \tag{8}
\]
The [actual wire-order theorem](research_positive_path_real_wire_order.md)
places \(x_*\) and both sets of shifted arguments in the regular
factorial strips and fixes the zero logarithmic lift of the wire
equation. The unexponentiated filling equations then give
\[
 \nabla\Phi(z_*)=0,\qquad
 \mathcal H=-\Phi''(z_*),\qquad R=\Re\mathcal H>0.
 \tag{9}
\]
Indeed the [mixed-phase concavity theorem without height ordering](research_mixed_phase_height_extension_and_wire_order.md)
applies to the two complete-end-compensated terms in (7).
Its real change of coordinates from \((x,s_1,s_2)\) to
\((x,t,r)\), where \(s_i=1/2-t_i/(2\pi)\), preserves strict
definiteness. Consequently there are a fixed real ball \(U\)
about zero and \(c>0\) such that
\[
 \Re\{\Phi(z_*+v)-\Phi(z_*)\}\le-c|v|^2
                         \quad(v\in U\subset\mathbb R^3).
 \tag{10}
\]
All these statements concern the actual coupled geometric point,
not arbitrary independent endpoint parameters.

## 2. A nonzero source normalization from the last physical row

Put \(w(t)=-2\cos t\), and let \(N\) tend to infinity through
both parities.
By (8), both \(w(t_*)\) and \(w(r_*)\) have negative real part.
Choose a fixed complex neighborhood \(\mathcal U\) of \(z_*\)
where their real parts stay below \(2-\gamma\), for some
\(\gamma>0\), and every factorial argument stays in a compact
subset of its regular strip.

The [last-physical-row theorem](research_last_physical_row_riccati.md),
Corollary 2, proves the odd-level assertion below. At even levels
the [exact low-index comparison](research_even_complete_low_kernel.md),
Theorem 1 and (21), proves the same assertion for the prescribed
low factor: its ratio to the last physical row is
\(1+O(N^{-1/2})\), with all fixed derivatives. Thus at both parities
\[
 \begin{split}
 \mathcal K_N(t)&=\exp\{N\psi(t,0)+e_N(t)\},\\
 |\partial_t^\ell e_N(t)|&\le C_\ell\log N
                    \qquad(\ell\text{ fixed}),
 \end{split}
 \tag{11}
\]
and likewise for \(r\). Its logarithm is fixed by the original
row \(F_{0,N}=1\), through the sum of the right-half-plane ratio
logarithms. It is not a principal logarithm chosen independently
for the final polynomial. At even levels add the logarithm near
zero of the last-row quotient \(1+O(N^{-1/2})\); this changes
none of the bounds in (11).

Define the exact nonzero scalar
\[
 Q_N=\exp\{e_N(t_*)+e_N(r_*)\}
  =\mathcal K_N(t_*)\mathcal K_N(r_*)
       e^{-N(\psi(t_*,0)+\psi(r_*,0))}.
 \tag{12}
\]
Thus, after increasing a fixed constant \(C\),
\[
                         N^{-C}\le |Q_N|\le N^C.
 \tag{13}
\]
This normalization uses two independently estimated original
low-index complete-end factors. It does not divide by the unknown filled
pair (2).

The canonical factorial expansion, with its half-integer shifts
retained, gives uniformly on \(\mathcal U\)
\[
 B_N(x,t)=
        \frac{e^{Nb(x,t)}}{2N\sin(\pi x)}
                         (1+O(N^{-1})).
 \tag{14}
\]
Every fixed derivative of the relative error obeys the same
bound on smaller neighborhoods. In fact
\(G_N(Nv-1/2)=N^{1/2}e^{NJ(v)}(1+O(N^{-1}))\), while
\(G_N(Nx)^2=2N\sin(\pi x)e^{2NJ(x)}(1+O(N^{-1}))\);
substitution in (4) proves (14) with its precise factor.

The heights in (8) are strictly positive. On a smaller
\(\mathcal U\), both rational trace denominators in (5) are
\(1+O(e^{-c_0N})\), including every fixed derivative after
decreasing \(c_0>0\). Equations (11)--(14) therefore give
\[
 I_N(z)=N^{-2}a(z)
       \exp\{N\Phi(z)+e_N(t)+e_N(r)\}
                              (1+O(N^{-1})),
 \qquad
 a(z)=\frac{\sin t\sin r}{4\sin^2(\pi x)}.
 \tag{15}
\]
In particular \(a_*=a(z_*)\ne0\). All factors in this calculation
come from the original finite density (5).

## 3. Local preparation and its observed Gaussian coefficient

Choose \(\zeta\in C_c^\infty(U)\), equal to one near zero,
with \(0\le\zeta\le1\). For \(\xi\in\mathbb R^3\), set
\[
 G_N(\xi)=
 \zeta(\xi/\sqrt N)\,
 N^2 Q_N^{-1}e^{-N\Phi(z_*)}
                      I_N(z_*+\xi/\sqrt N),
 \qquad
 \mathscr D_{\mathcal H}=\nabla_\xi+\mathcal H\xi .
 \tag{16}
\]
The function is extended by zero outside the cutoff chart.
All norms in the following theorem use real Lebesgue measure
in \(\xi\).

**Theorem 1.** For every fixed integer pair \(n,p\ge3\), along
all sufficiently large integer levels,
\[
 \begin{split}
 \|G_N-a_*e^{-\xi^T\mathcal H\xi/2}\|_{L^1}
 +\|G_N-a_*e^{-\xi^T\mathcal H\xi/2}\|_{L^2}
      &=O\!\left(\frac{\log N}{\sqrt N}\right),\\
 \|\mathscr D_{\mathcal H}G_N\|_{L^2}
      &=O\!\left(\frac{\log N}{\sqrt N}\right),\\
 \|G_N\|_{L^2}
      &=|a_*|\frac{\pi^{3/4}}{(\det R)^{1/4}}
                +O\!\left(\frac{\log N}{\sqrt N}\right).
 \end{split}
 \tag{17}
\]
In particular the norm is bounded below by a positive constant,
and the relative annihilation residual tends to zero.
The same \(L^2\) error holds after multiplication by any fixed
power of \(1+|\xi|\).

*Proof.* On the cutoff chart (11) gives
\[
 \begin{split}
 |e_N(t_*+\xi_t/\sqrt N)-e_N(t_*)|
 +|e_N(r_*+\xi_r/\sqrt N)-e_N(r_*)|
              &\le C\frac{\log N}{\sqrt N}|\xi|,\\
 \big|\nabla_\xi(e_N(t)+e_N(r))\big|
              &\le C\frac{\log N}{\sqrt N}.
 \end{split}
 \tag{18}
\]
Together with (10), this bounds the normalized density by
\(C e^{-c|\xi|^2/2}\), since
\(-c|\xi|^2+C(\log N)|\xi|/\sqrt N\le
 -c|\xi|^2/2+C'(\log N)^2/N\).
Taylor expansion at the full critical point gives
\[
 \begin{split}
 N(\Phi(z_*+\xi/\sqrt N)-\Phi(z_*))
     &=-\tfrac12\xi^T\mathcal H\xi
                           +O(|\xi|^3/\sqrt N),\\
 \sqrt N\,\nabla\Phi(z_*+\xi/\sqrt N)+\mathcal H\xi
     &=O(|\xi|^2/\sqrt N).
 \end{split}
 \tag{19}
\]
The elementary integral formula for \(e^u-e^v\), applied with
the negative quadratic bounds for the two real parts, now gives
an integrable error bounded by
\[
 C\frac{\log N}{\sqrt N}
                  (1+|\xi|^3)e^{-c_1|\xi|^2}
 \tag{20}
\]
after decreasing \(c_1>0\). The amplitude variation costs
\(C|\xi|/\sqrt N\), and the relative error in (15) costs
\(C/N\). Outside the cutoff the limiting Gaussian has an
exponentially small tail. This proves both norm approximations
and their fixed polynomially weighted versions.

Differentiating (15) in the rescaled variables, equations
(18)--(19) give the same kind of integrable bound for
\(\mathscr D_{\mathcal H}G_N\). The derivative of the cutoff
has the factor \(N^{-1/2}\); its support has
\(|\xi|\ge c_2\sqrt N\), so its contribution is exponentially
small. Finally
\[
 \|a_*e^{-\xi^T\mathcal H\xi/2}\|_{L^2}
                  =|a_*|\pi^{3/4}(\det R)^{-1/4}>0.
 \]
This proves (17). \(\square\)

The [already proved oscillator inequality](research_shifted_gaussian_observation.md)
therefore applies to an independently normalized actual source:
if \(\Pi_{\mathcal H}\) projects onto its normalized Gaussian,
\[
 \|(I-\Pi_{\mathcal H})G_N\|_2^2
    \le
 \frac{\|\mathscr D_{\mathcal H}G_N\|_2^2}
                     {2\lambda_{\min}(R)}
    =O\!\left(\frac{(\log N)^2}{N}\right).
 \tag{21}
\]
The norm on the right has not been inferred from the unknown
integral (2). This is the additional source input that a
spectral gap alone could not supply.

There is also an explicit nonzero local observation. The Gaussian
branch of \(\sqrt{\det\mathcal H}\), continued through
\(\Re\mathcal H>0\), gives
\[
 \int_{\mathbb R^3}G_N(\xi)\,d\xi
   =\frac{(2\pi)^{3/2}a_*}{\sqrt{\det\mathcal H}}
               \left(1+O\!\left(\frac{\log N}{\sqrt N}\right)\right).
 \tag{22}
\]
This follows from the \(L^1\) estimate, not from an unbounded
constant test functional on \(L^2\).

For precision, define the localized contour piece with its
actual scalar (6) by
\[
 \mathcal P_{n,p,N}^{\rm loc}
  =-\frac{C_{N,n}C_{N,p}N^5}{\pi^2}
           \int_{\mathbb R^3}\zeta(v) I_N(z_*+v)\,dv.
 \tag{23}
\]
It has the nonzero expansion
\[
 \mathcal P_{n,p,N}^{\rm loc}
 =-\frac{C_{N,n}C_{N,p}(2\pi)^{3/2}}{\pi^2}
       N^{3/2}Q_N
       \frac{a_*}{\sqrt{\det\mathcal H}}\,
       e^{N\Phi(z_*)}
       \left(1+O\!\left(\frac{\log N}{\sqrt N}\right)\right).
 \tag{24}
\]
Consequently
\[
 N^{-C}e^{N\Re\Phi(z_*)}
       \le|\mathcal P_{n,p,N}^{\rm loc}|
       \le N^C e^{N\Re\Phi(z_*)}
 \tag{25}
\]
for a fixed \(C\), after increasing the lower level threshold.
At this stage the normalization \(Q_N\) is controlled only by (13).
Section 7 supplies its sharper asymptotic and hence the precise
\(N^{-3/2}\) power.

## 4. The omitted outside radical has a strict gap after the traces

Let \(\mathcal P^{\rm full}_{n,p,N}\) denote (2) with the two
outside factors replaced by their full original kernels. Write
\[
 D_N(t)=K_N(t,0)-\mathcal K_N(t).
 \tag{26}
\]
This is the radical complete-end factor. It vanishes identically
at odd levels, but need not vanish at even levels.

**Proposition 2.** For each fixed integer \(n,p\ge3\),
\[
 \left|\mathcal P^{\rm full}_{n,p,N}
           -\mathcal P^{\rm low\,out}_{n,p,N}\right|
                \le CN^A e^{2NM_\infty},
 \qquad M_\infty=4G/\pi .
 \tag{27}
\]
Moreover \(M_{n,p}:=\Re\Phi(z_*)>2M_\infty+1/100\).
Consequently the error in (27) is exponentially smaller than
the nonzero local piece (24).

*Proof.* The [radical Fourier theorem](research_high_newton_radical_contraction.md#7-fourier-bounds-for-the-original-radical-polynomials),
equations (34)--(36), proves
\[
 \sup_{w\in[-2,2]}|D_N(w)|\le N^2.
 \tag{28}
\]
Here \(D_N(w)\) denotes (26) in its ordinary spectral variable.
Indeed every radical \(e_j\) has real interval norm at most
\(\sqrt{N-1}\), and there are fewer than \(N\) terms in
\(\sum_j e_j(w)e_j(-2)\). Markov's polynomial derivative
inequality gives polynomial bounds for its ordinary first
normal as well, including both endpoint colors.

The [real Newton estimate](research_three_crossing_real_period_newton_bound.md),
equations (5), (8), and (13), gives
\[
 \sup_{w_1,w_2\in[-2,2]}|K_N(w_1,w_2)|
                  \le CN^A e^{NM_\infty}.
\]
The same statement, at polynomial additional cost, holds for
each first normal and mixed first normal by applying Markov's
inequality in each variable. Original fixed crossing powers,
the original trace, and multiplication of a fixed number of
physical value/normal arrays all cost only powers of \(N\);
this is the full Hermite-norm bound in
[the original finite estimates](../papers/circle-tree-volume/finite-bounds.tex).

The exact difference in (27) is the sum of the terms with
outside factors \(D_N(t)K_N(r,0)\) and
\(K_N(t,0)D_N(r)\), minus the term with \(D_N(t)D_N(r)\),
always retaining the middle full kernel and both original
traces. The first two have at most two exponentially sized
kernel factors; the last has at most one. The bounds just
proved give (27). This is an estimate of the traced terms,
not their value on an off-grid complex angular contour.

On the selected wire, the original branch identity
\(b(x_*,t_*)+b(x_*,r_*)=\psi(t_*,r_*)\) is fixed at
completeness and continued through the regular chart of the
wire-order theorem. Thus \(\Re\Phi(z_*)\) has precisely the
original three-edge stationary normalization. The
[complete-end pair energy gap](research_radical_path_sector_gap.md#6-a-uniform-estimate-for-every-positive-pair-of-powers-at-least-three),
Theorem 5, equation (23), is
\(M_{n,p}>2M_\infty+1/100\). Combine it with (13), (24),
and (27). \(\square\)

## 5. Exact scope of the advance

This theorem establishes local norm growth, Gaussian preparation,
and a nonzero local observed coefficient from the actual finite
low-outer-edge sector at every fixed positive integer internal pair,
at both level parities and complete outside ends. At odd levels
this is the full source before contour localization.
It is stronger than a formal
quadratic expansion of a proposed phase: the actual outer factors
in (5) are controlled by their original pinned recurrence and,
at even levels, the exact alternating interpolation identity, and
their possible \(N\)-dependent phase and magnitude are retained.
All traced normal directions and both full trace denominators
remain present.

The remaining step is global. Formula (23) defines a local
horizontal piece; it does not assert that this piece occurs with
coefficient one in a deformation of (3), or that the other
currents and regions have lower action. The exact high-index,
alias, and boundary terms of that deformation still need to be
controlled. The statements of Sections 1–6 fix the outside variables complete,
as in (2). Their extension to ordinary derivatives in both outside
variables is proved in Section 7. At even levels
the last physical row has not been mistaken for the complete
endpoint: the low factor is obtained by the separate exact
interpolation comparison. Proposition 2 controls the omitted
radical outside-edge sectors after their original traces.
It does not control the rest of the low-outer-edge cycle, so
it cannot by itself turn the local term into a full-source
lower bound.

No new universal lower bound for the original closing coefficient,
volume theorem, or finite-exception conclusion is asserted.

## 6. The full original local density at both parities

There is now a stronger pair-specific conclusion than the low-sector
argument alone. The
[complete-edge gap theorem](research_internal_pair_complete_edge_gap.md)
uses the actual pair equations to prove
\[
 0<\Re t_*,\Re r_*<\pi/2,\qquad
 0<-\Im t_*,-\Im r_*<107/100,
 \qquad \Re\psi(t,0)-|\Im t|>1/500
 \tag{29}
\]
on the closed pair box (with the last inequality interpreted there).
Its Corollary 3 then proves, on a fixed complex neighborhood
containing both selected angles,
\[
       \frac{K_N(t,0)}{\mathcal K_N(t)}
                         =1+O(e^{-cN})
 \tag{30}
\]
through both level parities, with every fixed derivative on smaller
neighborhoods. This comparison follows from the original radical
Fourier bound and the independently proved nonzero low kernel.
It does not estimate a radical polynomial by a geometric kernel
outside this domain.

Define \(I_N^{\rm full}\) by replacing both \(\mathcal K_N\) factors
in (5) by their full original kernels \(K_N(t,0)\), \(K_N(r,0)\).
Keep the same known scalar \(Q_N\) in (12). Then on the cutoff chart
\[
        I_N^{\rm full}/I_N=1+O(e^{-cN}).
 \tag{31}
\]
After the normalization (16), this and its first derivatives have
exponentially small \(L^1\), \(L^2\), and annihilation errors.
The Gaussian bounds used in (20) control these norms uniformly.
Consequently Theorem 1 and the nonzero local integral (24) hold
unchanged for the full original local density at both parities.

This conclusion uses two exactly complete outside arguments.
The normal data at the traced vertices are retained; fixed ordinary
derivatives in their selected spectral variables are allowed.
Section 7 extends this conclusion to fixed complex neighborhoods
in both outside colors. The coefficient of the local contour in
the whole source and all complementary low-sector currents remain
unresolved.


## 7. The explicit local packet with two free outside colors

Let \(u,v\) be the outside angles, so their ordinary colors are
\(-2\cos u,-2\cos v\). Replace the two outside factors in (5) by
the full original kernels \(K_N(t,u),K_N(r,v)\), and denote the
resulting exact local density by \(I_N(z;u,v)\). Its scalar remains
exactly (6). In particular neither an outside trace nor an
additional level-dependent normalization has been inserted.

The [free-boundary edge theorem](research_pair_free_boundary_kernel.md),
Theorem 1, applies at both selected angles. Its hypotheses hold by
(8), (29), and the strict inequality
\(|\cos(t_*/2)|,|\cos(r_*/2)|<1\) from the wire-order theorem.
It supplies the nonzero holomorphic amplitudes \(a_e\) in
\[
 K_N(t,u)=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}(1+O(N^{-1})),
 \qquad
 Q_N=N^{-3}a_e(t_*,0)a_e(r_*,0)(1+O(N^{-1})).
 \tag{32}
\]
The second equality uses (12) and the exponentially small
full-to-low comparison (30). Both statements hold through all
levels, with all fixed derivatives of their normalized errors.

Define
\[
 \begin{split}
 \Phi(z;u,v)&=b(x,t)+b(x,r)+\psi(t,u)+\psi(r,v)
                   +\frac{i(nt^2+pr^2)}{4\pi}-i(t+r),\\
 A(z;u,v)&=\frac{\sin t\sin r}{4\sin^2(\pi x)}
                              a_e(t,u)a_e(r,v).
 \end{split}
 \tag{33}
\]
The invertible Hessian in (9) and the holomorphic implicit-function
theorem give a unique local critical point \(z=z(u,v)\) with
\(z(0,0)=z_*\). After shrinking a fixed bidisk about zero, put
\[
 \mathcal S(u,v)=\Phi(z(u,v);u,v),\qquad
 \mathcal H(u,v)=-\Phi_{zz}(z(u,v);u,v),\qquad
 \Re\mathcal H(u,v)>0.
 \tag{34}
\]
All amplitudes below are nonzero on a sufficiently small bidisk.
The matrix square root is the Gaussian branch in the convex
space of complex symmetric matrices with positive real part.

Choose a real, even cutoff \(\zeta\), equal to one near zero,
with support sufficiently small for the uniform quadratic bound
on \(z(u,v)+\operatorname{supp}\zeta\). Define the localized source
by (23), using \(I_N(z(u,v)+w;u,v)\) in place of the complete-end
density there. This is a holomorphic family: the integration
variable \(w\in\mathbb R^3\) and its cutoff are fixed, and only
the center of the contour moves holomorphically.

**Theorem 3.** For every fixed integer pair \(n,p\ge3\), this
localized part of the original source has the expansion
\[
 \begin{split}
 \mathcal P_{n,p,N}^{\rm loc}(u,v)
   &=C_{N,n}C_{N,p}N^{-3/2}\mathcal A(u,v)
                   e^{N\mathcal S(u,v)}(1+O(N^{-1})),\\
 \mathcal A(u,v)
   &=-\frac{(2\pi)^{3/2}}{\pi^2}
      \frac{\sin t\sin r}{4\sin^2(\pi x)}
      \frac{a_e(t,u)a_e(r,v)}{\sqrt{\det\mathcal H(u,v)}}
             \bigg|_{(x,t,r)=z(u,v)}\ne0 .
 \end{split}
 \tag{35}
\]
The remainder has a holomorphic expansion to every fixed
inverse-power order, uniformly on smaller bidisks. The statement
includes both level parities and every fixed ordinary derivative
in the outside colors near \(-2,-2\).

*Proof.* Equations (14), (32), and the exponentially small trace
denominator errors give, with holomorphic relative remainders,
\[
 I_N(z;u,v)=N^{-5}A(z;u,v)e^{N\Phi(z;u,v)}(1+O(N^{-1})).
 \tag{36}
\]
The two Newton-factorial representatives contribute \(N^{-2}\),
and the two already normalized outside kernels contribute
\(N^{-3}\). Thus the original scalar \(N^5\) in (6) cancels the
amplitude power in (36). Integration in the three stationary
variables contributes \(N^{-3/2}\).

Taylor expansion at \(z(u,v)\), with the uniform strict real
quadratic bound from (34), proves the Gaussian integral and
its stated coefficient. The terms of order \(N^{-1/2}\) in
the rescaled expansion are odd polynomials times the even
Gaussian. Their integrals vanish because the cutoff is even.
The remaining relative error is \(O(N^{-1})\); the fixed-cutoff
tails are exponentially small. Repeating this argument with
the higher factorial and edge expansions proves every fixed
inverse-power order. The scalar and orientation are precisely
those of (6), including its minus sign.

Both edge kernels and their phases are even in their outside
angle. Uniqueness of the local critical point therefore makes
\(z(u,v)\), \(\mathcal S\), \(\mathcal A\), and the normalized
local remainder separately even. They descend holomorphically
through \(-2\cos u=-2+u^2+O(u^4)\) and the corresponding expression
for \(v\). Cauchy's formula on smaller ordinary-color bidisks
proves the assertions about normals. \(\square\)

This sharper source estimate also removes the logarithmic loss
in the local almost-invariance statement. Set
\[
 \widetilde G_N(\xi;u,v)=
 \zeta(\xi/\sqrt N)N^5e^{-N\mathcal S(u,v)}
 I_N(z(u,v)+\xi/\sqrt N;u,v).
 \tag{37}
\]
Uniformly on a smaller bidisk, the proof of Theorem 1 now gives
\[
 \begin{split}
 \|\widetilde G_N-A_*e^{-\xi^T\mathcal H\xi/2}\|_{L^1\cap L^2}
       +\|(\nabla_\xi+\mathcal H\xi)\widetilde G_N\|_2
       &=O(N^{-1/2}),\\
 \|\widetilde G_N\|_2
       &=|A_*|\pi^{3/4}(\det\Re\mathcal H)^{-1/4}
                                                  +O(N^{-1/2}),\\
 A_*&=A(z(u,v);u,v).
 \end{split}
 \tag{38}
\]
Here the \(L^1\cap L^2\) norm denotes the sum of the two norms.
Fixed polynomial weights in \(\xi\) are allowed as before.
The variation of \(A\) is now \(O(|\xi|/\sqrt N)\), rather than
the \(O((\log N)|\xi|/\sqrt N)\) variation used in (18).
The oscillator estimate consequently bounds the squared
non-Gaussian part by \(O(N^{-1})\), with a norm bounded below
independently of the unknown full pair integral.

Theorem 3 identifies an actual local coefficient and its exact
power of \(N\). It does not state the coefficient of this local
piece in the original global integration cycle. To obtain a
full-source asymptotic one must still deform that cycle with
its original residues and show that its remaining pieces have
smaller exponential rate. The new free outside neighborhood
and ordinary normals do not replace that global estimate.
