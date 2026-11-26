# Uniform lattice asymptotics through the unit-charge faces

Private written proof, 16 November 2026.

The two exact Fourier companions of the original cosine closing must
both be retained near charge one. Their stationary contributions have
positive leading coefficients at complete outside angles. Keeping the
finite sum gives a uniform nonzero asymptotic through every regular
unit-charge face, including \(J_v=N-O(1)\) and mixed interior and
endpoint coordinates. The full Hermite normal weights and higher
Fourier aliases remain in the proof.

The statement concerns the actual all-low source. Where an adopted
high-sector estimate applies, it transfers to the whole original
source. The error is uniform to every fixed inverse-level order.
No growing-order or exponentially accurate reconstruction error is
inferred from those fixed-order estimates. The missing zero-charge
sample region and off-lattice source currents remain separate.

## 1. Source and the regular charge face

Let \(T\) be a fixed finite tree and \(S\) a nonempty connected proper
selected set, with all selected powers zero and original degrees
\(d_v\ge3\). Write
\[
 s=|S|,\qquad e=|E_S|,\qquad b=|\partial S|,\qquad
 e=s-1+b,\qquad p=\frac{3(b-1)}2.
 \tag{1}
\]
Every edge incident to \(S\) is retained once. Outside angles
\(\mathbf u=(u_e)_{e\in\partial S}\) remain independent ordinary
polynomial variables.

Use the exact original Newton algebra and trace
\[
 D=N-1,\quad\eta=(-1)^D,\quad
 P_N(z)=2T_N(z/2)+2,\quad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f,
\]
\[
 e_a(z)=
 \frac{\prod_{j<a}(2\cos((2j+1)\pi/N)-z)}
 {\prod_{j=1}^a(2\sin(\pi j/N))^2},\qquad
 K_N^{\rm low}(t,u)=\sum_{2a<N}e_a(-2\cos t)e_a(-2\cos u).
 \tag{2}
\]
For lattice charges \(c_v=J_v/N\), \(1\le J_v\le N\), the literal
coupon is
\[
 \mathcal C_{N,c_v}=T_{N-J_v}(-z_v/2).
 \tag{3}
\]
It has the full spectral values and normals of
\(\cos((N-J_v)t_v)\). Define \(Z_N^{\rm low}(\mathbf c;\mathbf u)\)
by inserting (3) at every selected vertex, using (2) on every original
edge, and applying all original selected traces. No physical normal
or odd simple node is removed.

Choose a set \(E\subseteq S\) of endpoint coordinates and put
\(I=S\setminus E\). Let \(K_I\Subset(0,1)^I\) be compact.
Assume that all anchor charge vectors
\[
             c_v=1\ (v\in E),\qquad \mathbf c_I\in K_I
 \tag{4}
\]
have regular positive zero-power height minima. The charge-cube
theorem verifies this except for the selected trivalent pair with
both charges one. If \(E=S\), condition (4) is precisely the regular
unit endpoint hypothesis. Empty \(I\) or empty \(E\) is allowed.

For a real charge vector \(\boldsymbol\lambda\) in a small neighborhood
of (4), let \(\mathbf H(\boldsymbol\lambda)>0\) be the continued regular
height minimum, and let
\[
 M(\boldsymbol\lambda)=
 \sum_{vw\in E_S}V(H_v,H_w)-\sum_{v\in S}\lambda_vH_v,
                  \qquad H_w=0\quad(w\notin S).
 \tag{5}
\]
Here \(V\) is the original maximized low edge potential, and
\(\mathcal L_{\boldsymbol\lambda}(\mathbf H)
=\sum_eV(H_v,H_w)-\sum_v\lambda_vH_v\) denotes the functional
before evaluation at its minimum. The original
phase and its selected critical value are
\[
 F_{\boldsymbol\lambda}(\mathbf t,\mathbf u)
    =\sum_{vw\in E_S}\psi(t_v,t_w)
                        -i\sum_{v\in S}\lambda_vt_v,
\]
\[
 \mathbf t^*(\boldsymbol\lambda,\mathbf0)=-i\mathbf H(\boldsymbol\lambda),
 \qquad
 W(\boldsymbol\lambda,\mathbf u)
     =F_{\boldsymbol\lambda}
           (\mathbf t^*(\boldsymbol\lambda,\mathbf u),\mathbf u).
 \tag{6}
\]
The phase uses the actual positive-height continuation from complete
angles, with every edge constant retained. In particular
\(W(\boldsymbol\lambda,\mathbf0)=M(\boldsymbol\lambda)\).

Compactness and the regular Hessian give a fixed \(\varepsilon>0\)
such that every vector obtained from
\[
 \mathbf c_I\in K_I,\qquad 1-\varepsilon\le c_v\le1\quad(v\in E)
 \tag{7}
\]
by replacing any endpoint coordinate \(c_v\) by \(2-c_v\) is still
regular, with uniformly positive finite heights and uniformly
interior original wire maxima. The same is true of the intervening
coordinate segments. Shrink \(\varepsilon\) whenever needed below.
For \(\omega\in\{0,1\}^E\), denote these reflected effective charges by
\[
 \lambda_v^\omega=
 \begin{cases}
 c_v+2\omega_v(1-c_v),&v\in E,\\
 c_v,&v\in I .
 \end{cases}
 \tag{8}
\]
All the critical germs in (6) are holomorphic on a common neighborhood
of this compact family and of \(\mathbf u=0\).

## 2. Uniform finite companion sum

**Theorem 1.** For the fixed data above, there are a complex boundary
polydisk \(U\), a constant \(\delta>0\), and holomorphic
coefficients \(A_r(\boldsymbol\lambda,\mathbf u)\), independent of
the level and its parity, such that for every fixed integer \(L\ge1\)
there are \(C_L,N_L\) for which, at all \(N\ge N_L\) and every
lattice charge vector in (7),
\[
 \begin{split}
 Z_N^{\rm low}(\mathbf c;\mathbf u)
   ={}&2^{-s}N^{-p}
       \sum_{\omega\in\{0,1\}^E}
       e^{NW(\boldsymbol\lambda^\omega,\mathbf u)}
       \sum_{r=0}^{L-1}\frac{A_r(\boldsymbol\lambda^\omega,\mathbf u)}
                              {N^r}
       +R_{N,L}(\mathbf c;\mathbf u),\\
 |R_{N,L}|
   \le{}& C_L N^{-p}e^{N\Re W(\mathbf c,\mathbf u)}
            \left(N^{-L}+e^{-\delta N}\right).
 \end{split}
 \tag{9}
\]
The bounds are uniform on \(U\) and, on smaller polydisks, with every
fixed boundary derivative after the reference exponential is
extracted. Each coefficient is bounded uniformly on the indicated
compact charge family and boundary polydisk:
\[
                    \sup |A_r|\le C_r<\infty.
 \tag{10}
\]

At complete outside angles the leading coefficient is
\[
 A_0(\boldsymbol\lambda,\mathbf0)=
 (2/\pi)^{s/2}
 \frac{\prod_{v\in S}\sinh H_v\,
       \prod_{vw\in E_S}a_e(-iH_v,-iH_w)}
 {\sqrt{\det\nabla_{\mathbf H}^2\mathcal L_{\boldsymbol\lambda}}}>0.
 \tag{11}
\]
The \(a_e\) are the original positive low-edge Gaussian amplitudes.
The factor \(2^{-s}\) is outside (11) and is already present in (9).

Define the leading normalized companion sum
\[
 B_N(\mathbf c,\mathbf u)=
 2^{-s}\sum_{\omega\in\{0,1\}^E}
 A_0(\boldsymbol\lambda^\omega,\mathbf u)
 e^{N\{W(\boldsymbol\lambda^\omega,\mathbf u)
                         -W(\mathbf c,\mathbf u)\}}.
 \tag{12}
\]
After reducing \(U\), constants \(b_-,b_+>0\), independent of the
lattice charge tuple and level, satisfy
\[
                     b_-\le |B_N|\le b_+.
 \tag{13}
\]
Consequently
\[
 Z_N^{\rm low}
  =N^{-p}e^{NW(\mathbf c,\mathbf u)}
                  B_N(\mathbf c,\mathbf u)(1+O(N^{-1}))
 \tag{14}
\]
is a uniform nonzero actual-source asymptotic. Its leading factor is
allowed to depend on \(N\) through the companion exponentials.
At \(E=S\) and \(\mathbf c=\mathbf1\), every reflected charge is
identical, so (12) is exactly \(A_0(\mathbf1,\mathbf u)\).

## 3. Exact aliases and independent branch contours

The exact derivative-sampling formula for an even Laurent polynomial
\(f(t)=\sum a_re^{irt}\) is
\[
 \begin{split}
 \phi_N(f\mathcal C_{N,J/N})
 =\frac{N^2}{2}\sum_{\ell\ge1}\ell\eta^{\ell+1}
 \big[&a_{(\ell-1)N+J-1}-a_{(\ell-1)N+J+1}\\
      &+a_{(\ell+1)N-J-1}-a_{(\ell+1)N-J+1}\big].
 \end{split}
 \tag{15}
\]
In particular the multiplier is \(\ell N\), not \(J\).
The coefficient differences retain the original normal channel.

Equivalently, on any full lower angular circle \(t=\tau-ih\),
\[
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2},\qquad
 W_N(t)\cos((N-J)t)
 =\frac12
 \frac{e^{-iJt}+e^{-i(2N-J)t}}
      {(1-\eta e^{-iNt})^2}.
 \tag{16}
\]
The exact zero-power trace is
\[
 \phi_N(f\mathcal C_{N,J/N})
 =-\frac{N^2}{\pi i}
   \int_{-\pi-ih}^{\pi-ih}
       \sin t\,f(t)\,W_N(t)\cos((N-J)t)\,dt.
 \tag{17}
\]
The polynomial cosine is \(2\pi\)-periodic, so the two vertical
sides cancel exactly. These identities tensorize before any kernels
are separated; all shared indices and other variables stay in place.

Expand the two numerator terms in (16) at every vertex. Retain both
terms for \(v\in E\), and only \(e^{-iJ_vt_v}\) for \(v\in I\).
This gives the \(2^{|E|}\) branches (8), each with the common literal
factor \(2^{-s}\). On a retained branch all \(N\lambda_v^\omega\)
are integers. Hence its integrand, including the denominator in
(16), is separately periodic. Each branch can therefore be moved
to its own lower circles
\[
                         t_v=\tau_v-iH_v(\boldsymbol\lambda^\omega).
 \tag{18}
\]
There is no pole between two strictly lower circles, and their
vertical sides cancel. The outside variables may be complex during
this exact deformation.

The nonconstant denominator modes are
\[
 (1-\eta e^{-iNt})^{-2}
           =\sum_{r\ge0}(r+1)\eta^r e^{-irNt}.
 \tag{19}
\]
The heights in (18) have a fixed positive minimum. All nonconstant
modes therefore have a uniform exponential loss. Summing their
polynomial weights preserves that loss.

For a discarded numerator choice at some \(v\in I\), use instead
the original heights \(\mathbf H(\mathbf c)\). The extra exponent
there is at most
\[
             -2N(1-c_v)H_v(\mathbf c)\le-\delta_I N
 \tag{20}
\]
for a fixed \(\delta_I>0\), because \(K_I\Subset(0,1)^I\).
Other numerator choices have nonnegative added charges and cannot
increase this modulus. The coefficientwise positive low-kernel
majorant and the uniform product profiles bound the whole discarded
sum by a polynomial times \(e^{N(M(\mathbf c)-\delta_I)}\).
For \(I=\varnothing\) there is no such discarded numerator.
This argument does not require a saddle for a far reflected
interior charge.

For each retained branch, discard low indices outside fixed compact
intervals around its regular maxima. The same coefficientwise
Fourier majorant, now with penalty
\(-\sum_v\lambda_v^\omega H_v\), gives a fixed loss.
A finite cover of the compact branch family makes all constants
uniform. The retained index sums have the original holomorphic
factorial interpolation, the exact index-cotangent rectangles, and
the strict angular estimate of the regular low-source theorem.
Their unique angular maximum on (18) is \(\boldsymbol\tau=0\).
All complementary angular regions and index connectors have fixed
losses.

These bounds were obtained for complete or real outside variables.
Each such finite-source difference has boundary Laurent degree at
most \(D\); polynomial continuation preserves a smaller fixed loss
on a common small complex outside polydisk. Near its local maximum
the retained branch contour is deformed through the holomorphic
critical point in (6). Its heights remain strictly positive, so no
angular trace pole is crossed.

The resulting branch Gaussian has (11), including its positive
orientation, the exact factor \(N^{-p}\), and every source scalar.
The next section records the uniform fixed-order remainder. Its
constants are not asserted uniform as the truncation order grows.

## 4. Uniform fixed-order remainders

Use fixed complex neighborhoods of the compact regular index and
angle saddles. All normalized factorial arguments lie in compact
subsets of
\[
              \Omega=\mathbb C\setminus((-\infty,0]\cup[1,\infty)).
 \tag{21}
\]
Write \(J'(z)=\Log(2\sin\pi z)\), \(J(1/2)=0\), on \(\Omega\),
with the logarithm real on \(0<z<1\). The centered factorial theorem,
with its exact normalization, gives
\[
 \log G_N(Nz-1/2)
 =\tfrac12\log N+NJ(z)
  +\sum_{r=1}^R
   \frac{B_{2r}(1/2)J^{(2r)}(z)}{(2r)!\,N^{2r-1}}
  +O_R(N^{-2R-1})
 \tag{22}
\]
uniformly and holomorphically on those compacts. Its uncentered and
bounded-offset versions follow by Taylor translation. For each fixed
order \(L\), take sufficiently many terms in (22), multiply the
finitely many actual factorial factors, and exponentiate their
logarithmic expansions. This gives the uniform fixed-order symbol
expansion of the exact interpolated summands.

For each local edge index integral, use its analytic Morse coordinate
on a fixed neighborhood of the uniformly nondegenerate critical
point. The local phase becomes its critical value minus a positive
quadratic form on the chosen real contour. Taylor-expand the
transformed holomorphic amplitude to the finite degree needed for
order \(L\). Odd Gaussian moments vanish, and each even term of
degree \(2r\) contributes order \(N^{-r}\). The Taylor remainder
is bounded on a common smaller complex ball; its Gaussian integral
has the required fixed-order bound. Extending the finite Taylor
polynomials to full Gaussian space changes their integrals only
exponentially, because the local ball has fixed positive radius.
All nonlocal index connectors and cotangent modes have the fixed
exponential gaps established in Section 3.

Apply the same finite Taylor argument to the selected angular
Gaussian. Its uniformly positive definite real Hessian, the fixed
local coordinate radius, and the fixed complementary angular gap
give a uniform remainder. The exact Gaussian orientations give
(11), as in the original low-source theorem. There are only finitely
many factors and integrations. Consequently, for each fixed \(L\),
the resulting branch error is \(O_L(N^{-L})\) after its leading power
and critical exponential are extracted. Cauchy's estimates on
smaller parameter neighborhoods preserve each fixed derivative.

This constructs the holomorphic coefficients in (9) and proves
(10) for each fixed \(r\). Equations (19)--(20) and the discarded
index bounds add the exponential remainder. No estimate on the
growth of \(C_L\) as \(L\to\infty\) is used or claimed.

## 5. Comparison of the branches and noncancellation

The stationary-value derivative is exact:
\[
                    \partial_{\lambda_v}W=-i t_v^*.
 \tag{23}
\]
At complete outside data it equals \(-H_v<0\).
On a sufficiently small common complex boundary polydisk, along
every real charge segment between \(\mathbf c\) and a reflected
vector, uniform continuity therefore gives
\[
 \Re\partial_{\lambda_v}W\le-h_0<0.
 \tag{24}
\]
Since \(\lambda_v^\omega-c_v\ge0\),
\[
 \Re\{W(\boldsymbol\lambda^\omega,\mathbf u)-W(\mathbf c,\mathbf u)\}
              \le-h_0\sum_v(\lambda_v^\omega-c_v).
 \tag{25}
\]
All branch remainders are thus bounded relative to the single
reference exponential in (9). Exponentially small discarded terms
remain so after shrinking the outside polydisk to preserve their
fixed loss relative to \(\Re W(\mathbf c,\mathbf u)\).

The finite sum (12) is holomorphic in \(\mathbf u\) and uniformly
bounded on a fixed polydisk, by (25) and compact amplitude bounds.
At \(\mathbf u=0\) every summand is positive and the unreflected
summand is present. Thus
\[
 B_N(\mathbf c,\mathbf0)\ge
                   2^{-s}\inf_{\boldsymbol\lambda}A_0
                         (\boldsymbol\lambda,\mathbf0)>0.
 \tag{26}
\]
Cauchy's estimate on a smaller concentric polydisk gives a uniform
bound for the first boundary derivatives of \(B_N\), independent
of \(N\) and the lattice charges. Shrinking once more preserves
half the lower bound in (26). This proves (13), without estimating
the phases of exponentially small companions individually.
Taking \(L=1\) in (9) proves (14).

## 6. Full-source transfer and the reconstruction error scale

If a uniform full high-sector gap is available on the charge set
under consideration, it adds another exponentially small error to
(9). In particular:

* for \(E=S\) and a regular unit endpoint, the adopted near-unit
  theorem supplies that gap after reducing \(\varepsilon\);
* for original selected degrees at least twelve, the adopted
  whole-lattice high estimate supplies it on any compact mixed
  endpoint/interior set used here.

On such sets the full source has (9) and (13)--(14), with the
exponential remainder rate reduced if necessary.

For clarity about reconstruction, let \(M_{\max}\) be the maximum of
\(M(\mathbf c)\) on the compact charge set under consideration.
At complete outside angles, a fixed-order truncation in (9) supplies
the uniform absolute error
\[
                  C_L N^{-p-L}e^{N M_{\max}}
 \tag{27}
\]
for its endpoint and interior samples. If all regions of a complete
canonical cosine sample array were supplied with that bound, the
finite reconstruction theorem would give, at \(y_v=1-\chi_v\), a
polynomial factor times
\[
 C_L N^{-L}
 \exp N\left[M_{\max}+
             \pi\sum_v(-\sigma_v\Im y_v)_+\right].
 \tag{28}
\]
No fixed \(L\) cancels a strictly positive directional exponential
cost. A useful exponentially accurate reconstruction therefore needs
a separate growing-order remainder bound, or another actual
exponential sample estimate. Fixed-order uniformity alone does not
give it. The present note also leaves the zero-charge sample region
out: its charges stay a fixed distance from zero.

Neither the analytic coefficient germs in (9) nor exact values on the
lattice permit dropping the original off-lattice angular currents.

The construction is an exact contour proof for the stated all-low
lattice source. Its nonzero coefficient is not inferred from a local
density alone. It does not assert a polarized half-grid initializer,
arbitrary short-filling cycle participation, or a global volume
theorem.

## Direct sources

All proofs use written mathematics only. Direct source versions and
the complete author readback are checked before freezing.

- [Half-charge full-source theorem](research_zero_power_half_charge_high_gap.md),
  SHA256 fb2ffd3cfe32848d490bc866c70fb96505760cbe48344981a97c5abce131a0cd:
  exact charged derivative sampling, lattice lower-circle formula,
  charge-dependent low majorant and the degree-twelve high estimate.
- [Regular zero-power low source](research_regular_zero_subtree_low_source.md),
  SHA256 06e4b7c14e3a61616dea61642103e2d2803709fcd465ae9860258119db3299d1:
  exact all-low contours, index rectangles, strict complement gaps,
  amplitude and normalization, and boundary continuation.
- [Zero-power charge-cube geometry](research_zero_power_charge_cube_positivity.md),
  SHA256 91b0a03a677c9139bbfd04f9ef6b06b23e6c3fab435c1a974a2d243189925faf:
  regular compact height minima and the exceptional unit pair.
- [Canonical factorial amplitude](research_two_square_factorial_amplitude.md),
  SHA256 995c38d1cc6fcd5a1a1306601778ce6068b5f1d766364216e7cdd933f344290f:
  exact centered logarithmic sum, its normalization and all-order
  coefficients on the slit domain, used only at fixed truncation
  order in this note.
- [Near-unit high-sector gap](research_near_unit_charged_high_sector_gap.md),
  SHA256 dc707bc52cacc2ce507d9d6c55129b3a378c2a104b2116d14ff42ecc0d312637:
  uniform whole high-complement control through unit charge.
- [Finite quantitative charge reconstruction](research_finite_charge_quantitative_reconstruction.md),
  SHA256 5d13994e8b6d2dc3c54d1fcf15d1f9435efc2d26921046bca14b90d22e75bf23:
  full-normal sample inversion and the exact directional error cost.
