# Periodic inverse-phase probes and their trace cancellation

Private written proof, 16 November 2026.

On the high-wire domain of the moving-seam theorem, the canonical
factorial phases admit a globally holomorphic, angularly even inverse
probe. An explicit parity character repairs its wire periods. The
weighted factorial and cardinal periods then agree exactly, including
on the admitted nonconstant even seams, and the weighted absolute
integral has a polynomial bound for a closed network.

For a closed network the weighted period itself is exponentially small.
The proof uses the original full Hermite trace, not a value-only replacement. Thus this
particular inverse-phase probe does not certify a nonzero geometric
contribution. Its weighted observation is not the unweighted source.

## 1. Fixed source, domain and phase

Use the original compiled network of the joint-lens theorem, at unit
charge. Put
\[
 D=N-1,\quad \eta=(-1)^D,\quad
 a_N=\pi-\frac{\pi}{2N},\quad b_N=-\frac1{2N},\quad I_N=[b_N,b_N+1],\quad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2},\qquad N\ge2.
 \tag{1}
\]
Let \(V\ne\varnothing\) be the traced vertices and \(E\) the paired
wire indices. Each wire occurs in two halfwires, each direct or
reflected. At every free spectral endpoint retain the cardinal
polynomial \(\widetilde B_N\); its variable is not reduced. Write
\(F_{\partial,N}\) for their product, with any specified polynomial
factors involving only free variables. Initially there are no further
angular spectators; their extension is stated in Section 5.

At a traced halfwire use the actual function
\[
 B_N(y,t)=\frac{N}{
 G_N(D/2-Ny+Nt/(2\pi))G_N(D/2-Ny-Nt/(2\pi))G_N(Ny)^2}.
 \tag{2}
\]
Its argument is \(y=x_e\) or \(y=D/N-x_e\), exactly as prescribed
by the source. Let \(H\) count the traced halfwires and let \(r_e\)
count the traced ends of wire \(e\); thus \(H=\sum_e r_e\).
The original top forms and prefactor are
\[
 \begin{split}
 \Omega_{\rm fac}&=F_{\partial,N}\prod_{h\ {\rm traced}}B_N(y_h,t_{v(h)})
       \prod_{v\in V}\left\{\sin t_v\,W_N(t_v)
              e^{in_vNt_v^2/(4\pi)}\right\}\,d\mathbf x\,d\mathbf t,\\
 \mathfrak c_N&=N^{|E|}\prod_{v\in V}
       \left(-\frac{N^2C_{N,n_v}}{\pi i}\right),\qquad
 C_{N,n}=e^{\pi i nD^2/(4N)} .
 \end{split}
 \tag{3}
\]
Here every \(n_v\) is a fixed signed integer. The cardinal form
\(\Omega_{\rm car}\) replaces only the traced factors by their
original full-Hermite cardinal representatives. All external framing
scalars, if specified, remain outside (3).

Fix \(T,\delta>0\), and choose positive wire heights
\[
 h_e>T/(2\pi)+\delta.
 \tag{4}
\]
The angular domain is the symmetric rectangle
\(|\Re t_v|<\pi,\ |\Im t_v|<T\), together with neighborhoods of
the compact sets used below. Constant wires are
\(x_e=b_N+s_e+ih_e\), \(0\le s_e\le1\). Also allow
\[
 X_e=b_N+s_e+ih_e+\varepsilon f_e(\mathbf t),\qquad
 |\varepsilon|\sup_e\|f_e\|_\infty<\delta/2,
 \tag{5}
\]
where each \(f_e\) is bounded, holomorphic and even in every angular
variable on the full product rectangle. The straight homotopy from
zero perturbation is retained. All real wire translations are allowed.
For frozen wire values on (5), all angular primitive paths in this
rectangle are allowed too. The moving-seam source proves that the
denominator factorials are holomorphic units on this domain: the
three imaginary-part signs for a direct halfwire are \((+,-,-)\),
and for a reflected halfwire they are \((-,+,+)\), each with magnitude
greater than \(N\delta/2\).

Use the canonical half-plane primitives \(J_\sigma\), \(\sigma=\pm1\),
with the original normalization and exact shifts
\[
 J_\sigma(z+k)=J_\sigma(z)-\sigma\pi i\{kz+k(k-1)/2\},\qquad
 J_\sigma'(z+k)=J_\sigma'(z)-\sigma\pi i k.
 \tag{6}
\]
For a direct halfwire put \(y_0=x_e,\ c=0\); for a reflected one put
\(y_0=1-x_e,\ c=-1\). Thus its exact argument is \(y=y_0+c/N\).
Set \(\sigma=\operatorname{sgn}\Im y_0\) and
\[
 \alpha_\pm=\frac12-y_0\pm\frac{t}{2\pi},\qquad
 b_h(y_0,t)=-J_{-\sigma}(\alpha_+)-J_{-\sigma}(\alpha_-)
                         -2J_\sigma(y_0),
 \qquad
 F_{\rm ev}=\sum_h b_h+\sum_v\frac{in_vt_v^2}{4\pi}.
 \tag{7}
\]
These are single-valued holomorphic functions on the specified tube,
even in every angular variable. The complementary offset \(-1/N\)
has not been changed to zero: it enters the exact amplitudes below.
No assertion identifies this branch with a geometric branch reached
from another contour.

## 2. Exact wire periods and the weighted relative identity

Equation (6) gives
\[
 b_h(y_0+1,t)-b_h(y_0,t)=-\sigma\pi i.
 \tag{8}
\]
When \(x_e\) increases by one, a reflected \(y_0\) decreases by one
and has \(\sigma=-1\); a direct \(y_0\) increases by one and has
\(\sigma=1\). Both therefore contribute \(-\pi i\). Consequently
\[
 F_{\rm ev}(\mathbf x+\mathbf e_e,\mathbf t)-F_{\rm ev}(\mathbf x,\mathbf t)
       =-r_e\pi i.
 \tag{9}
\]
Choose \(\epsilon_{e,N}\in\{0,1\}\) congruent to \(Nr_e\) modulo two,
and define
\[
 \zeta_N(\mathbf x)=e^{i\pi\sum_e\epsilon_{e,N}x_e},\qquad
 p_N=\zeta_N e^{-NF_{\rm ev}}\prod_{v\in V}2\cos(Nt_v).
 \tag{10}
\]
This is holomorphic, angularly even, and exactly periodic under every
wire deck translation. On a closed fully traced network \(r_e=2\),
so \(\zeta_N=1\) at both parities. The repair is uniformly bounded
above and below on every fixed compact wire tube; it has no
exponential cost in \(N\).

Define the weighted observation by
\[
 \mathcal O_N=\mathfrak c_N\int_{\mathcal L}p_N\Omega_{\rm fac},
 \tag{11}
\]
where \(\mathcal L\) is the product of constant wire intervals and
full lower angular lenses from \(-a_N\) to \(a_N\).

**Proposition 1.** The factorial and cardinal expressions for (11)
agree exactly. Their common weighted period is preserved by the
admitted homotopies (5), and the factorial bulk alone suffices there.
All statements hold coefficientwise in the free boundary polynomial.

**Proof.** The original vertexwise representative difference is
\(\sum_vP_N(-2\cos t_v)A_v\), with every \(A_v\) holomorphic and even.
The identity \(P_N(-2\cos t_v)W_N(t_v)=(-1)^N\) cancels the entire
\(v\)-th trace kernel, including its double poles. Multiply by
\(p_N\) before taking the primitive in \(t_v\). Its new coefficient
is still odd and holomorphic in that variable. Its primitive from
\(-a_N\) vanishes at both endpoints. This constructs a new relative
primitive for \(p_N(\Omega_{\rm fac}-\Omega_{\rm car})\); it is not
obtained by dropping \(dp_N\wedge\Theta\) from the old primitive.

The product \(p_N\Omega_{\rm car}\) is pointwise wire-periodic:
each paired cardinal wire already has multiplier one. Stokes therefore
preserves its period under the paired-face homotopy. For the new
primitive, the moving-seam proof applies verbatim: its coefficient is
even in its own angle, while the seam Jacobian column differentiated
in that angle is odd. Its integrated seam current is zero. Frozen-wire
primitive paths stay in (4)--(5), as required. This proves the claims.
The full-Hermite removable division also covers the odd simple spectral
node, whose angular pullback is double, and \(N=2\). \(\square\)

This does not identify (11) with the unweighted scalar. In particular,
\(p_N\) need not have the finite wire Fourier band needed to turn its
weighted period into the original lattice sum. It is an exact analytic
observation of the specified original period, with a new inserted probe.

## 3. A polynomial bound on the weighted absolute integral

Define exact normalized halfwire amplitudes and their vertex products:
\[
 A_{h,N}=N B_N(y_0+c/N,t)e^{-Nb_h(y_0,t)},\qquad
 A_{v,N}=\prod_{h:\,v(h)=v}A_{h,N}.
 \tag{12}
\]
The uniform half-plane factorial theorem, including its actual bounded
offsets, proves \(A_{h,N}=A_h(1+O_{\rm hol}(N^{-1}))\) on each fixed
compact subset of this domain, where
\[
 A_h=
 \begin{cases}
 e^{-J_\sigma'(y_0)},&c=0,\\
 e^{J_\sigma'(y_0)-J_{-\sigma}'(\alpha_+)-J_{-\sigma}'(\alpha_-)},&c=-1.
 \end{cases}
 \tag{13}
\]
Indeed the shifted factorial offsets are \(-1/2,-1/2,0,0\) in the
direct case and \(1/2,1/2,-1,-1\) in the reflected case. This proves
uniform bounds for the exact amplitudes, not just for a formal symbol.
The finitely many initial levels are absorbed into the bound by
holomorphy on the same compacts.

Fix \(0<h<T\) and choose the tapered full lenses
\[
 t(s)=s-ih(1-s^2/a_N^2),\qquad -a_N\le s\le a_N.
 \tag{14}
\]
Their lengths are bounded independently of \(N\). Along them
\[
 |1-\eta e^{-iNt}|\ge
 c_h:=\min\{1/\sqrt2,\ 1-e^{-h/4}\}>0.
 \tag{15}
\]
To check this, put \(d=a_N-|s|\). For \(d\le\pi/(4N)\), the phase
of \(\eta e^{-iNs}\) stays at least \(\pi/4\) away from zero: its
endpoint phases are \(\pm\pi/2\). For \(d\ge\pi/(4N)\),
\(N|\Im t|\ge Nh d/a_N\ge h/4\). These two cases give (15).

The exact unit-charge identity is
\[
 2\cos(Nt)W_N(t)
 =\frac{1+e^{-2iNt}}{(1-\eta e^{-iNt})^2}
 =1+2\eta W_N(t).
 \tag{16}
\]
It follows that
\[
 p_N\Omega_{\rm fac}
 =N^{-H}\zeta_N F_{\partial,N}
       \prod_v\{\sin t_v\,A_{v,N}(1+2\eta W_N(t_v))\}
                       \,d\mathbf x\,d\mathbf t.
 \tag{17}
\]
All signed Gaussian factors in (3) have canceled exactly. Formula (15)
bounds the last factor in (17), including the endpoints.

Let \(\mathcal B_{\partial,N}\) bound the retained boundary polynomial
on the fixed wire compact, in any specified coefficient norm or on
a fixed compact set of free variables. It is one for a closed network.
Equations (12)--(17) give
\[
 |\mathfrak c_N|\int_{\mathcal L}|p_N\Omega_{\rm fac}|
 \le C N^{|E|+2|V|-H}\mathcal B_{\partial,N}.
 \tag{18}
\]
The same bound holds on (5): the full Jacobian in \((\mathbf s,\mathbf t)\)
is block triangular with determinant one. The compact amplitude bounds
remain uniform there. Constants depend on the fixed network, domain
and perturbation, not on \(N\). For a closed network \(H=2|E|\), so
the displayed power is \(2|V|-|E|\). No polynomial bound for an arbitrary
free-boundary factor is inferred; its size remains in (18).

## 4. The exact surviving observation and its full normal data

At constant wire coordinates, every term in the expansion of (17)
that omits \(W_N(t_v)\) at some vertex integrates to zero. Its integrand
in that angle is odd and holomorphic on the full symmetric rectangle.
This is an exact parity cancellation, not an estimate. The sole surviving
term keeps every original trace kernel.

For an even holomorphic function \(A(t)\), let \([A]\) be its original
spectral Hermite class. The lens trace formula is
\[
 \phi_N([A])=-\frac{N^2}{\pi i}\int_\Gamma\sin t\,A(t)W_N(t)\,dt
 =\eta\sum_{j=0}^{N-1}
       \left.\frac{d}{dt}(\sin t\,A(t))\right|_{t=\tau_j},
 \qquad \tau_j=\pi-(2j+1)\pi/N.
 \tag{19}
\]
The derivatives in (19) retain the first spectral normals. At odd
\(N\), its \(t=0\) summand is the original simple-node value \(A(0)\),
not an additional normal condition.

Using (19) in the surviving term of (17) yields the exact functional
\[
 \boxed{\quad
 \mathcal O_N=N^{|E|-H}(2\eta)^{|V|}
       \left(\prod_vC_{N,n_v}\right)
       \int_{\prod_e(I_N+ih_e)}
           \zeta_N F_{\partial,N}
                    \prod_v\phi_N([A_{v,N}])\,d\mathbf x .
 \quad}
 \tag{20}
\]
All aliases remain in (19). The crossing powers occur in (20) only
through their original unit scalars \(C_{N,n_v}\), because this
particular probe removed their full Gaussian factors. Proposition 1
makes (20) the value on the even moving seams too; it does not assert
that their integrands factor after substitution.

## 5. Exponential cancellation of the normalized traces

This conclusion uses an exact angular period law, not an inference
from an \(O(N^{-1})\) expansion. For one halfwire set
\[
 u_\pm=D/2-Ny\pm Nt/(2\pi),\qquad
 E_\pm=e^{-2\pi i\sigma u_\pm}.
 \tag{21}
\]
The exact factorial period \(G_N(z+N)=-2\sin(\pi z)G_N(z)\) and (6)
give
\[
 \begin{split}
 \frac{B_N(y,t+2\pi)}{B_N(y,t)}
     &=(-1)^N e^{-i\sigma Nt}\frac{1-E_-}{1-E_+},\\
 b_h(y_0,t+2\pi)-b_h(y_0,t)&=-i\sigma t-\pi i\sigma,\\
 \boxed{\quad A_{h,N}(t+2\pi)
       =A_{h,N}(t)\frac{1-E_-}{1-E_+}.\quad}
 \end{split}
 \tag{22}
\]
For the first identity, both \(u_\pm\) have imaginary-part sign
\(-\sigma\); express their sine ratio using that same sign. The
factors \((-1)^N e^{\pi i\sigma N}\) cancel in the last identity.
No complementary offset or parity multiplier remains unrecorded.

Fix a common positive margin \(\delta_0\) for
\(|\Im(u_\pm/N)|\) on \(|\Im t|\le h\) and the fixed wire compact;
one may take \(\delta_0=\delta/2\) in (4)--(5). Then
\[
 |E_\pm|\le e^{-2\pi N\delta_0},\qquad
 |A_{v,N}(\pi+is)-A_{v,N}(-\pi+is)|
                      \le C e^{-2\pi N\delta_0},\quad |s|\le h.
 \tag{23}
\]
All amplitudes are holomorphic and bounded on a neighborhood of the
rectangle \([-\pi,\pi]+i[-h,h]\). The high-wire condition also
justifies its endpoint neighborhoods; no real-part strip restriction
is imposed on their factorial arguments.

Apply the full residue formula to this rectangle, oriented positively:
\[
 \phi_N([A])=-\frac{N^2}{2\pi i}
         \oint\sin t\,A(t)W_N(t)\,dt.
 \tag{24}
\]
On its two horizontal sides \(|W_N|\le C_h e^{-Nh}\). On its paired
vertical sides, sine and \(W_N\) are exactly \(2\pi\)-periodic, and
\[
 W_N(\pi+is)=-\frac{\eta}{4\cosh^2(Ns/2)}.
 \tag{25}
\]
Their sum therefore contains precisely the amplitude difference in
(23). Since \(|\sin(\pi+is)|=|\sinh s|\le C_h|s|\) and
\[
 \int_{-h}^h |s|\cosh^{-2}(Ns/2)\,ds\le C N^{-2},
 \tag{26}
\]
the original \(N^2\) trace normalization is fully paid. Equations
(23)--(26) prove, uniformly in the retained wire coordinates,
\[
 |\phi_N([A_{v,N}])|
 \le C\{N^2e^{-Nh}+e^{-2\pi N\delta_0}\}
 \le C N^2e^{-\kappa N},\qquad
 \kappa=\min\{h,2\pi\delta_0\}>0.
 \tag{27}
\]
For an empty vertex product, \(A_{v,N}=1\) and its trace is exactly
zero; this also satisfies the estimate.

Combining (20) and (27) gives
\[
 \boxed{\quad
 |\mathcal O_N|\le
 C N^{|E|+2|V|-H}e^{-\kappa |V|N}\mathcal B_{\partial,N}.
 \quad}
 \tag{28}
\]
This includes both parities and \(N=2\), after enlarging the constant
for finitely many initial levels. It also holds on the even moving
seams by their exact weighted-period invariance.

A fixed polynomial spectator in the traced spectral variables can
be expanded into finitely many products of powers of \(-2\cos t_v\).
These factors are even, holomorphic and exactly \(2\pi\)-periodic.
The same proof applies term by term, with their coefficient and compact
norms retained. For a level-dependent family, those quantities must
be retained explicitly; no uniform bound is supplied by the argument.

Thus (18) and (28) describe the same observation: its absolute
integral has polynomial size, while its complete Hermite trace has
an exponential loss on a closed network. Equation (20), or equivalently
the derivative sampling (19), is the actual surviving boundary/alias
functional. It is not known to be nonzero, and (28) excludes a
polynomial lower bound for this normalized closed observation.

These statements do not show that every probe or every geometric
coefficient vanishes. They do not estimate the unweighted source,
whose phase was removed in (10), or a deformation through a geometric
point outside the high-wire tube. A different logarithmic mark is not
silently substituted into (7). The exact result is that periodicity,
evenness and a polynomial weighted absolute norm are compatible with
exponentially small original full-Hermite observation.

## Direct written sources

The five complete source texts and their directly used implications
were read at the following fixed versions.

* [Joint factorial source](research_joint_factorial_lens_relative_source.md),
  SHA256 a14ca148bd55b36b1eea9de8be8a63025532c3bbbb928482b0d7cb8edae56e54:
  original network, literal offsets, trace normalization, unreduced
  boundary factors and the full-Hermite relative primitive.
* [Moving seams](research_moving_wire_seam_source_descent.md),
  SHA256 2b632735243fc450e2ce0f276f339c9fad0b5524724364b83f15690b4896f33d:
  high-wire holomorphic domain, frozen-wire primitive paths and
  the determinant-parity proof of zero integrated seam current.
* [Half-plane factorial asymptotics](research_factorial_uniform_halfplane_continuation.md),
  SHA256 0514ffe3e13a887eccd9099b306117ee86553f0731d976315e2607b3e33493fa:
  canonical branches and uniform exact-amplitude bounds with offsets.
* [Factorial chamber atlas](research_newton_factorial_chamber_atlas.md),
  SHA256 34d6e0e4e82a98bf8e6063558ecafdedb0a58d6229fbe462e7e4bfff48f4db4c:
  exact integer shifts of the marked primitives and of the original
  gamma-product factorial.
* [Full-grid trace](research_full_grid_lens_source_continuation.md),
  SHA256 d141e6e8c23572bb13484807a2359395a0371d6a3d699198826a105b6dad5649:
  derivative sampling, rectangle/lens normalizations, all original
  normals and the odd simple node.

Only written arguments, source-text reads and hashes are used.
No mathematical code, numerical evaluation, tests or compilation
are run. Frozen notes, manuscripts and public documents are unchanged.
