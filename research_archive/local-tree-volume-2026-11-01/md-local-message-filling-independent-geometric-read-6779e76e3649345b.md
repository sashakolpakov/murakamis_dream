# The exact subtree induction and its geometric interface

1 November 2026. This is a private independent derivation concerning
md-all-circle-local-message-filling-criterion.md, SHA-256
945769c4a8b36a66616c8a271661a275af80029ff32cad2dcdffe7dbdf63b3c1.
It makes no change to the published sources.

The full argument closes under the stated local condition. In particular,
its use of complex parent angles does not require a child phase to be
real, and its error normalization does not spend the total filling loss
of a subtree at every ancestor. The individual checks below identify the
finite-source and analytic ingredients needed for those assertions.

## 1. The outgoing polynomial and the actual typed functional

Let \(X=-2\cos t\) and \(Y=-2\cos u\). After the original compatible
Hom carriers have been lowered at the product junction, the outgoing
message is exactly
\[
 M_v(u)=\sum_{k=0}^{N-1}\gamma_{e_v}\frac{H_N}{W_k}
 \mathcal D_v\!\left(e_k(X)\prod_w M_w(t)\right)e_k(Y).
 \tag{1}
\]
The functional \(\mathcal D_v\) takes the remainder in its prescribed
moving or constant Casimir quotient and then the full trace, including
the derivative coordinates at a repeated root. The degree of its
argument in \(X\) can exceed \(N-1\); this does not affect linearity.
Every occurrence of \(Y\) in (1) is displayed. Thus no parent-angle
factor is introduced by the trace, a quotient operation, or a normal
limit. Its trigonometric degree in \(u\) is at most \(N-1\).

The edge scalar is assigned once. The full crossing polynomial and the
reference scalar remain in their original locations. Changing the
order in which (1) is evaluated reassociates a finite typed tensor
contraction; it does not reinterpret a reversed edge as a different
forward physical turn.

This statement was checked against the current filled-volume source
equations (13), (16a)--(16e) and the all-circle source contraction.
The identity
\(\phi_\sigma(e_i e_j)=\mathbf1_{i+j=N-1}\) is valid in the fixed
complete coordinates: the relevant product has degree at most \(2N-2\),
so a constant change of the defining monic quotient cannot change its
top remainder coefficient.

## 2. The finite kernel has the required complex domain

The published curvature note, Section 5, proves the retained finite
edge-sum expansion on the entire \(|t|,|u|\le1/4\) bidisk. This is
stronger than a formal bound on the selected action. On the retained
index interval \(I=[1/5,3/10]\), it supplies
\[
 |A_{xx}|<44,\qquad \Re A_{xx}<-12,\qquad
 |x_*(t,u)-1/4|<0.003.
 \tag{2}
\]
The finite cotangent contour has height \(1/500\). Its vertical
endpoint loss exceeds \(0.002\), and the horizontal nonconstant
cotangent loss \(\pi/250\) exceeds the possible translated action
gain \(77/30000\). The canonical Gamma interpolation remains in its
regular bulk domain. Hence the nonzero Gaussian expansion used in
the local-message proof is available as a finite-sum statement.

The discarded kernel indices have real spectral loss \(\pi/200\).
The polynomial ellipse estimate spends only
\(|\Im t|+|\Im u|\), which is absorbed on the stated small parent
disk and strip. This proves the full-kernel local expansion, including
its high indices as an exponentially smaller term.

For the far real angular part, the low Newton product bound supplies
\[
 |e_k(-2\cos(t+iy))|
 \le e^2e_k(-2)e^{N[-\alpha\sin^2(t/2)+11y^2]},
 \qquad \alpha>1/250.
 \tag{3}
\]
For the other, small complex endpoint, write each normalized factor
as
\[
 1-\frac{\sin^2(u/2)}
          {\cos^2((j+1/2)\pi/N)}.
 \tag{4}
\]
The denominator is at least \(1/3\) on \(I\), for sufficiently large
levels. This is the denominator intended in the draft's brief
product estimate. Multiplying (4) gives the asserted \(e^{Nr^2}\)
bound. The explicit margins in the draft then preserve the stronger
conditional normalization \(\Re\psi(0,u)\), rather than adding an
uncontrolled \(O(r^2)\) error at every vertex.

## 3. Complex parents preserve the sign and the phase class

Put \(a=d_v/(2\pi)\), \(b=n_v/(2\pi)\), \(D=a-ib\). If the
normalized child phases have curvature within \(a_0/20\) of
\(-a_0\), the conditional phase is
\[
 A(t,u)=\psi(0,u)-at^2/2+E(t,u),\qquad
 |E_{tt}|,\ |E_t/t|\le a/20.
 \tag{5}
\]
Both estimates hold for complex \(u\). The equation
\[
 Dt=-i\ell+E_t(t,u)
 \tag{6}
\]
contracts the prescribed disk, and \(E_t=tQ\), \(|Q|\le a/20\),
gives
\[
 t_\ell=-\frac{i\ell}{D-Q}.
 \tag{7}
\]
In particular \(\Re(D-Q)>0\); this gives the lower-half-plane sign
without any assertion that \(Q\) is real. Bounding numerator and
denominator in (7) yields precisely
\[
 \frac{380}{441}\frac{\ell a}{|D|^2}
 \le-\Im t_\ell\le
 \frac{420}{361}\frac{\ell a}{|D|^2}.
 \tag{8}
\]

For the first-charge outgoing phase, the stationary chain rule gives
\[
 h''(u)=\psi_{uu}
       -\frac{\psi_{ut}^2}{A_{tt}+ib}.
 \tag{9}
\]
The denominator has modulus at least \(19|D|/20\). The two edge
derivative bounds imply
\[
 |h''+a_0|
 \le a_0\left(\frac1{50}+\frac{20}{19\cdot2500}\right)
 <a_0/20.
 \tag{10}
\]
No factor depending on degree or depth enters (10).

Differentiation with respect to the real charge gives
\(\partial_\ell\Re C_\ell=\Im t_\ell\), also for a complex parent.
Integrating (8) proves the charge ordering and the current vertex's
drop
\[
 0\le\Re\psi(0,u)-\Re C_1(u)
 \le\frac{420\pi}{361}\frac{d_v}{d_v^2+n_v^2}.
 \tag{11}
\]
This is a local conditional drop, not the sum of the drops of the
descendant vertices.

## 4. The finite child logarithm does not accumulate exponential loss

Uniform relative asymptotics with a nonzero analytic amplitude imply
that the exact normalized child polynomial has no zeros on every
fixed smaller angular disk, for sufficiently large \(N\). Its
logarithm, chosen to vanish at zero, therefore satisfies
\[
 \frac1N\log\frac{M_w(t)}{M_w(0)}
 =h_w(t)+\frac1N\log\frac{\alpha_w(t)}{\alpha_w(0)}
       +O(N^{-2}).
 \tag{12}
\]
The derivative bounds follow by Cauchy's formula on nested disks.
The later saddle lies in a much smaller disk than the zero-free
one. Thus (12) is available wherever it is used.

There are finitely many children at a fixed vertex. Their sum in
(12) modifies an analytic amplitude and contributes only
\(O(N^{-1})\) to the local relative expansion. The exact constants
\(\prod_wM_w(0)\) are factored out before taking any absolute values.
Consequently neither their phases nor their accumulated filling
losses are replaced by a complete-source bound.

The scalar ledger \(\Omega_{v,N}\) in the updated draft is useful:
the full crossing scalar need not converge with \(N\), but it cancels
from \(M_v(u)/M_v(0)\). The leading normalized amplitude is independent
of the microscopic parameter because the first Fourier coefficient
is exactly one and the paired edge insertion has leading value one.

## 5. The full strip estimate uses only the proved degree

If the real envelope is \(e^{-Nc(1-\cos t)}\), apply the subharmonic
maximum principle to \(z^{N-1}M_v(z)/M_v(0)\) and its reciprocal.
It gives
\[
 \left|\frac{M_v(t+iy)}{M_v(0)}\right|
 \le CN^A
 e^{N[-c(1-\cos t)+(1+c)|y|]}.
 \tag{13}
\]
Zeros away from the local disk cause no problem in this argument.
For \(|t|\ge r/2\), the explicit height \(y_0=2^{-56}\) spends
less than half the real angular loss. For \(|t|<r/2\), the local
phase class gives
\[
 \Re h(t+iy)\le-19a_0t^2/40+21a_0y^2/40.
 \tag{14}
\]
These two regions cover the strip. The resulting bound is uniform
in depth at the exponential level, while its polynomial constants
may depend on the fixed subtree.

## 6. The tail and connector estimates are conditional

The full trace input has the bound
\[
 CN^A e^{N[\Re\psi(0,u)-2^{-20}at^2+128ay^2]}.
 \tag{15}
\]
For \(y=A_0t_0a/|D|\), the chirp cost is at most
\(2^{18}|D|^2y^2/a\). The first omitted charge is larger than
\(t_0|D|\). Since \(2^{18}A_0<1/2\), the total omitted tail
loses at least \(2^{-74}a>2^{-77}\). The fixed-parameter Chebyshev
coefficient growth is absorbed by the extra-charge geometric series
for sufficiently large \(N\). This starting level may depend on the
fixed powers; the theorem permits that dependence.

The real endpoints retain their angular loss. The zero Fourier mode
and the translated-grid endpoint currents have the same loss; they
are not omitted by treating the chirp as a periodic function.
For a retained charge, the connector quadratic expression is bounded
using (8). Its decisive dimensionless factor is
\[
 \frac{420}{361}
 \max\left\{\frac{21}{40},\frac{2}{14/5}\right\}
 =\frac{300}{361}<\frac78.
 \tag{16}
\]
The remaining connector term is therefore at most \(-\ell v/8\).
On the horizontal segment through the saddle, the real Hessian is
negative and the saddle is inside the interval. The factor
\(\sin t_\ell\) cannot vanish: \(\ell>0\), equation (6), and the
small disk exclude all its possible zeros.

The common absolute conditional error \(\eta=2^{-80}\) lies below
the first conditional action because \(4\kappa<\eta/2\).
There is no need to prove a relative expansion at each of the lower
nonminimal charges.

For parameter collisions the argument extends the whole analytic
difference between the finite trace and its first-charge
approximation. It does not claim that separately divided endpoint
currents are removable. The same argument applies to the constant
opposite-color trace by its actual normal limit.

## 7. The real envelope is regenerated without discarding high indices

For a real outgoing angle, the exact kernel and the inductive real
child bounds give a polynomial full-norm bound for the trace input.
The canonical polynomial degree in each child variable is less than
\(N\). Multiplication, the fixed crossing power, Chebyshev folding
in the prescribed quotient, and the top coefficient functional have
only polynomial costs for a fixed valence and fixed power.

This proves the fresh numerator estimate with exponent
\(2G_0-c_K(1-\cos u)\). The just-proved nonzero denominator has
exponent \(2G_0-\Delta_v\), with \(\Delta_v<4\kappa\). Away from
the local angular disk the fixed real angular gap absorbs this
single drop. Inside the disk the new phase class gives the stronger
quadratic estimate. This closes the induction and includes the
empty child product at a terminal vertex.

## 8. Root action, metric and quantifiers

At the root there is no outgoing kernel. Its incoming messages
still give exactly \(d_0\) incidences and the same phase class,
trace tails and nonzero first charge. Back-substitution of the
stationary child phases produces the original simultaneous system
\[
 \sum_{e\sim v}\psi_{e,\tau_v}
       +\frac{in_v\tau_v}{2\pi}=i.
 \tag{17}
\]
No independently optimized caps are introduced. The edge count
gives \(N^{-3|E|/2}N^{3|V|/2}=N^{3/2}\); the original reduced
closing factor is retained once.

Under the local condition the simultaneous charge path stays far
inside the positive angular chart. Its lower-half-plane sign follows
from the same factored nonlinear derivative used in (7). The already
proved ordered decomposition and primitive logarithmic completion
therefore identify \(2\pi\Re\mathcal C(\mathbf1)\) with the volume of
the original filled knot complement. This uses the actual geometry;
it is not inferred from the polynomial message identity.

The tree, its signed powers and every degree are fixed before \(N\).
No constant multiplying a polynomial, no amplitude bound and no
starting level is asserted uniform over growing trees. The numerical
sufficient condition is independent of the number of vertices.
This distinction is retained throughout the proof.

## 9. Input versions

The current published copies inspected in this derivation were:

* actual_all_circle_curvature_filling_limit.md:
  f57a6b01197fe3ea715bb6c92495c73306f24440c58c0c8eaea1258f792cba6b;
* all_circle_uniform_newton_bounds.md:
  61bd06eb04ea6fd26bba52095300ce8de892553d0ea1702e698184f5a4c0a919;
* actual_main_meridian_filled_volume.md:
  9f526145e18930c2db8db9e8d8c8eaa2cd91a5ec1304312b952ba74813d4f6d3.

The only suggested wording refinement is to name the denominator
in (4) explicitly. It does not change the bound or the theorem.
