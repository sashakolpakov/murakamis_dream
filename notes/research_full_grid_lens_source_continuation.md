# An exact full-grid lens for the original charged source

Private written proof, 15 November 2026.

The full original Hermite trace can be represented by a lower angular
arc whose endpoints are the real grid midpoints \(-\pi,\pi\).
There is then no separate vertical term and no discarded physical row.
This gives an exact family of joint source contours through any
supplied path in the lower canonical strip. It does not show that the
geometric contribution of those contours is nonzero, or bound their
remaining parts at the geometric rate.

## 1. The original finite source and its angular representative

Fix \(N\ge2\), and put
\[
 D=N-1,\qquad q=e^{\pi i/N},\qquad
 \eta=(-1)^D,\qquad C_{N,n}=q^{nD^2/4},
 \qquad \tau_a=\frac{\pi(D-2a)}N.
 \tag{1}
\]
Use the original algebra and closing
\[
 \mathcal A_N=\mathbb C[z]/(P_N),\qquad
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(F)=\eta N^2[z^D]\operatorname{rem}_{P_N}F .
 \tag{2}
\]
All powers of \(q\) use the logarithm in (1). Let \(n\) be any
signed integer and let \(A(z)\) be an arbitrary ordinary polynomial.
Its coefficients may be polynomials in other untraced boundary
variables; no reduction of those variables is made.

For \(\chi\in\mathbb C\), write \(L=N(1-\chi)\). The canonical
degree-less-than-\(N\) coupon \(\mathcal C_{N,\chi}\) has the full
physical data
\[
 \begin{split}
 \mathcal C_{N,\chi}(-2\cos\tau)&=\cos(L\tau),\\
 \mathcal C_{N,\chi}'(-2\cos\tau)
       &=-\frac{L\sin(L\tau)}{2\sin\tau}
                  \quad\text{at every double root}.
 \end{split}
 \tag{3}
\]
At the odd simple root \(-2\), its prescribed value is one and
there is no normal condition. The two choices \(\tau,-\tau\)
at a double root give the same data. Finite Hermite interpolation
therefore defines the coupon uniquely, with coefficients entire
in \(\chi\).

The original scalar is
\[
 Z_{n,N,\chi}[A]=\phi_N(R^n\mathcal C_{N,\chi}A).
 \tag{4}
\]
The exact Gaussian physical jets give the derivative-sampling formula
\[
 Z_{n,N,\chi}[A]
   =\eta C_{N,n}\sum_{a=0}^{N-1}g'(\tau_a),\qquad
 g(t)=\sin t\,A(-2\cos t)
        \exp\!\left(\frac{inNt^2}{4\pi}\right)\cos(Lt).
 \tag{5}
\]
The function \(g\) is odd and entire. Neither the Gaussian nor
\(\cos(Lt)\) is being asserted periodic. The formula uses their
original physical values and first normals only. At odd \(N\),
the single point \(\tau=0\) contributes \(g'(0)=A(-2)\), with
the displayed original scalar \(C_{N,n}\).

The pinned trace source states its calculation for \(N\ge3\).
The same residue and full-Hermite argument applies at \(N=2\):
there is one double Casimir root, represented by the two angular
points \(\pm\pi/2\), and no simple-root term. Thus (5) and the
arguments below include that level.

## 2. The full-grid lens identity

Define the exact double-pole kernel
\[
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2},
 \qquad
 K_N^{\rm grid}(t)=\frac{iNe^{iNt}}{e^{iNt}-\eta}.
 \tag{6}
\]
Then
\[
 (K_N^{\rm grid})'=N^2\eta W_N,\qquad
 W_N(-t)=W_N(t),\qquad
 W_N(\pi)=W_N(-\pi)=-\eta/4.
 \tag{7}
\]
In particular the two endpoints are not poles at either parity.
The nearest physical points are \(\pm(\pi-\pi/N)\).

Let \(\Gamma\) be a piecewise smooth arc from \(-\pi\) to \(\pi\)
whose interior lies in the open lower half-plane. It may be chosen
inside \(|\operatorname{Re}t|<\pi\). The integrals at its endpoints
are ordinary convergent integrals.

**Theorem 1.** For every such arc,
\[
 \boxed{\quad
 Z_{n,N,\chi}[A]
 =-\frac{N^2C_{N,n}}{\pi i}
       \int_\Gamma g(t)W_N(t)\,dt .
 \quad}
 \tag{8}
\]
This is an exact finite-\(N\) identity, with every original physical
row and every first normal retained.

**Proof.** First suppose the arc is simple. Reflection \(t\mapsto-t\)
gives an upper arc \(-\Gamma\), directed from \(\pi\) to \(-\pi\).
The resulting positively oriented lens encloses exactly the \(N\)
physical grid points in (5). At each, \(K_N^{\rm grid}\) has residue
one. The residue theorem and integration by parts give
\[
 \begin{split}
 Z_{n,N,\chi}[A]
 &=\frac{\eta C_{N,n}}{2\pi i}
              \oint K_N^{\rm grid}(t)g'(t)\,dt\\
 &=-\frac{\eta C_{N,n}}{2\pi i}
              \oint (K_N^{\rm grid})'(t)g(t)\,dt .
 \end{split}
 \tag{9}
\]
The integrands are regular at the two lens endpoints. Oddness of
\(g\) and evenness of \(W_N\) make the upper integral equal to
the lower one, with the reflected orientation. Equations (7) and
(9) prove (8). A general arc has the same integral by a
fixed-end homotopy in the lower half-plane, where \(gW_N\) has
no poles. Equivalently, use the corresponding oriented chains.
\(\square\)

Here is the endpoint audit in the original rectangle formulation.
For height \(y>0\), its exact vertical contribution is
\[
 \frac{\eta N^2C_{N,n}}{\pi}
  \int_{-y}^{y}
   \frac{g(\pi+iv)}{4\cosh^2(Nv/2)}\,dv .
 \tag{10}
\]
For fixed \(N,\chi,A\), the integrand is analytic near \(v=0\),
and \(g(\pi)=0\). The integral tends to zero; its symmetric
Taylor expansion is in fact \(O_{N,\chi,A}(y^3)\).
Individually, short endpoint connectors have size
\(O_{N,\chi,A}(\epsilon^2)\), because
\[
                  g(t)W_N(t)=O_{N,\chi,A}(|t\mp\pi|)
                     \quad(t\longrightarrow\pm\pi).
 \tag{11}
\]
Thus the fixed-\(N\) limit \(y\downarrow0\) produces precisely
(8), without an endpoint half-residue. The constants in (11)
are not asserted uniform in \(N\); this exact limit is taken
before any asymptotic estimate. No interchange of limits is used.

## 3. Spectral branches, half crossings and all aliases

The endpoints map to \(z=2\), where the canonical function
\(\operatorname{arccosh}(-z/2)^2\) has a branch. This causes
no endpoint pole in the proof: (5)--(11) are angular identities
of entire functions and the explicit grid kernel. Moreover
\(P_N(2)=4\), so \(z=2\) is not an original spectral pole.
No contour is moved across the spectral branch cut in this argument.

The connection with the adopted even split is exact. Write
\(n=m+\epsilon\), with \(m\) even and \(\epsilon\in\{0,\pm1\}\),
and retain the physical factor \(\kappa^n\), where
\(\kappa=q^{D^2/2}\). Here
\[
 \hbar=2\pi i/N,\qquad
 F_j(z)=q^{-jD^2/4}
       \exp\!\left(\frac{j\,\mathfrak K(z)}{2\hbar}\right),
 \qquad \mathfrak K(z)=\operatorname{arccosh}(-z/2)^2
\]
uses the canonical branch on \(\mathbb C\setminus[2,\infty)\),
with its removable value at \(-2\). In the open canonical strip
\(|\operatorname{Re}t|<\pi\),
\[
 \kappa^n F_m(-2\cos t)F_\epsilon(-2\cos t)
    =C_{N,n}\exp\!\left(\frac{inNt^2}{4\pi}\right).
 \tag{12}
\]
Hence an interior deformation staying in this strip crosses no
half-crossing seam. At its angular endpoints the entire right
side and its product with \(\sin t\) have the regular limits
already used in (11). A spectral derivative of \(F_\epsilon\)
at \(z=2\) is neither needed nor substituted for an original normal.

For continuous \(\chi\), the coupon representative \(\cos(Lt)\)
may have different values on lifts differing by \(2\pi\).
The proof of (8) compares \(t\) with \(-t\), where it is even;
it never compares \(t\) with \(t+2\pi\). Thus its possible
nonperiodicity creates no omitted endpoint term. Subsequent
logarithmic lattice translations still require the actual
canonical coupon or its exact wrap corrections.

The complete Fourier-alias kernel is retained:
\[
 W_N(t)\cos(N(1-\chi)t)
  =\frac12e^{-iN\chi t}
       \frac{1+e^{-2iN(1-\chi)t}}
                 {(1-\eta e^{-iNt})^2}.
 \tag{13}
\]
At \(\chi=1\) the numerator is two, giving the original
unit-charge coefficient one. At \(\chi=0\), the coupon in
the finite algebra is \(\eta\); this is not a known scalar
initializer. Near the real endpoints, (13) is used exactly.
No estimate that discards its other terms is asserted there.

## 4. Joint original sources and an explicit continuation candidate

For a fixed original circle tree, let \(S\) be the traced vertices.
Keep the original full turn kernels
\(\mathcal K_N(t_v,t_w)=\sum_{j=0}^D
e_j(-2\cos t_v)e_j(-2\cos t_w)\), all ordinary outside
polynomials, and all original integer powers. Applying (8) at
each selected vertex gives exactly
\[
 \begin{split}
 Z_{\boldsymbol\chi,N}
 ={}&\prod_{v\in S}\left(-\frac{N^2C_{N,n_v}}{\pi i}\right)
 \int_{\prod_{v\in S}\Gamma_v}
 \prod_e\mathcal K_N(t_v,t_w)\\
 &\qquad\cdot
 \prod_{v\in S}\left[
  \sin t_v\,
  e^{in_vNt_v^2/(4\pi)}
  W_N(t_v)\cos(N(1-\chi_v)t_v)\,dt_v
 \right].
 \end{split}
 \tag{14}
\]
The identical statement applies to compiled identity or turn kernels
and further polynomial spectators, with those actual factors left
in place. Fubini is legitimate for these finite compact integrals.
The identity is coefficientwise in the untraced ordinary variables,
so subsequent boundary derivatives retain the original normals.

Compact joint deformations are also exact when their interiors stay
in the product lower domain and each boundary face stays in its original
hyperplane \(t_v=\pm\pi\). The holomorphic top form is closed.
On the side of such a deformation belonging to that boundary face,
the pullback of \(dt_v\) is zero. Stokes' theorem therefore adds
no face integral. This statement uses the full integrand in (14),
not a selected exponential summand.

There is an explicit contour family through any supplied continuous
path
\[
 t_v^*(\chi)=s_v(\chi)-iH_v(\chi),\qquad
 |s_v(\chi)|<\pi,\quad H_v(\chi)>0,
 \tag{15}
\]
on a compact parameter interval. Choose a radius \(r>0\) smaller
than a quarter of the distance of all \(s_v(\chi)\) from the ends.
Let a smooth bump \(\beta\) equal one on \([-r,r]\), vanish
outside \([-2r,2r]\), and take values in \([0,1]\).
For any fixed \(h_0>0\), set
\[
 h_{v,\chi}(s)
 =\beta(s-s_v(\chi))H_v(\chi)
  +(1-\beta(s-s_v(\chi)))h_0(\pi^2-s^2),\qquad
 \Gamma_{v,\chi}(s)=s-i h_{v,\chi}(s).
 \tag{16}
\]
These arcs have the required fixed real endpoints, stay in the
lower canonical strip, and are horizontal near the selected points.
Equation (14) holds on them for every parameter and every \(N\).
For a piecewise smooth supplied path they form a piecewise smooth
fixed-end isotopy. No existence of the path (15) is proved here.

The small-charge theorem supplies a nonzero initial asymptotic for
the same original source with complete outside angles, arbitrary
fixed signed powers, and the stated same-index graph kernels.
Its proof also applies to the real continuous coupons (3) on its
small charge box: on physical real angles the coupon has modulus
at most one and first angular derivative at most \(N\), and its
exact reflected contour formula requires evenness, not periodicity.
All its strict estimates are unchanged. Formula (14) represents
that initialized source and its exact continuation to unit charge.

This removes neither the analytic continuation problem for the
geometric projection nor the need for a whole-source estimate.
The full edge kernels have not been replaced by their geometric
packets. A local descending classical collar can be inserted only
as an exact chain deformation with its remaining connecting chain
retained. This note gives no bound on that chain, no source-compatible
projection onto the local geometric block, and no noncancellation
conclusion. The split-current action gap applies when the actual
remaining operation is the specified Ward deletion; a general
part of the lens integrand has not been identified with such a
deletion.

## Direct written sources

Full source readbacks were retained at the matching pinned versions,
and the directly used implications were reread.

* [Exact original trace](research_exact_complete_trace_contour.md),
  SHA256 a63c66e8078457fa84e8044dc876beca36126348e816de9c6997d2a2610474e8:
  derivative sampling, residue normalization, complete double-pole
  kernel and exact vertical sides.
* [Analytic coupon family](research_dominant_saddle_transport.md),
  SHA256 413940497a23e884d726b91f9c0ebc01994fef8216811ed2c6fb0838fc80bb04:
  Section 9 defines the canonical full-Hermite family and its
  nonperiodic angular representative and retained aliases.
* [Original source compiler](research_arbitrary_power_source_compilation.md),
  SHA256 55e2de84870cfd20dac5922791dbc2bed54909439dfbf4663f17c70a1089445f:
  actual turn/identity kernels, arbitrary signed powers and
  unreduced free-boundary source.
* [Even-factor reduction](research_even_twist_ward_source_reduction.md),
  SHA256 7cd055df1b070ecc8a5f4a4b62e821e37c616e1bbb935aa274939cf44e8e0b18:
  canonical analytic units, original \(\kappa^n\), total-power
  Gaussian and the distinction from unwrapped seam transport.
* [Small-charge initializer](research_small_charge_path_source.md),
  SHA256 c6d0ce2a4ecf1412aa3752cb8a94c6933bb47acab5d96d879c6f1b17b2db2a90:
  its original finite source, both-parity initial asymptotic,
  arbitrary fixed signed powers, full kernel and endpoint estimates.

Only written reasoning, text reads and file hashes were used.
No mathematical code, numerical evaluation, tests or compilation
were run. Frozen notes, public documents and manuscripts were not edited.
