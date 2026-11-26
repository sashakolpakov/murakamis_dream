# Even-twist Ward transport with the original half crossing retained

Private written proof, 15 November 2026.

Every original integer crossing power can be split into its even twist
and a retained half crossing. Applying the Ward operation to the even
factor gives scalar endpoint deletion on an arbitrary circle tree,
without the odd-power derivative coupons. The retained half crossing
has a canonical zero-free analytic representative, so its conjugated
Ward operator has an explicit local symbol with the original total
power. A rank-two endpoint formula records exactly what changes if
the canonical spectral sheet is replaced by an unwrapped Gaussian.

This organizes an available even-twist factorization into an all-exterior
operator and simultaneous-current statement. It does not establish a
global contour deformation or the original geometric cycle coefficient.

## 1. Original algebra, normalization and factorization

Fix \(N\geq2\) and write
\[
 D=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \hbar=2\pi i/N,\quad \rho=q-q^{-1},\quad
 \eta=(-1)^D,\quad \sigma=(-1)^N=-\eta,
 \qquad \kappa=q^{D^2/2}.
 \tag{1}
\]
Every fractional power of \(q\) uses this displayed logarithm. The
original algebra, trace and crossing are
\[
 \mathcal A_N=\mathbb C[z]/(P_N),\quad
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N=\eta N^2[z^D]\operatorname{rem}_{P_N},\qquad
 R=\kappa r_N.
 \tag{2}
\]
Let \(f_j\) be the degree-below-\(N\) representative of \(r_N^j\).
For all signed integers, multiplication in \(\mathcal A_N\) gives
\(f_a f_b=f_{a+b}\). In particular every \(f_j\) is a unit.

Choose
\[
             n=m+\epsilon,\qquad m=2P\in2\mathbb Z,
                      \quad\epsilon\in\{0,1,-1\}.
 \tag{3}
\]
Keep the half crossing specified by the original marking: when the
physical convention is \(n=\epsilon-2p\), take \(P=-p\).
No change of the primitive peripheral basis is being made.

Set \(c_0=q+q^{-1}\). Let \(\Pi_0\) be its spectral idempotent and
\(\Xi_0\) its first-normal element: their respective value/derivative
data at \(c_0\) are \((1,0)\) and \((0,1)\), with all other physical
data zero. These include the double node at \(N=2\). The original
crossing data give
\[
 f_j(c_0)=1,\qquad f_j'(c_0)=-\frac{jD}{2\rho},\qquad
 f_j\Xi_0=\Xi_0,\qquad
 \phi_N(\Xi_0 A)=\sigma\rho^2 A(c_0).
 \tag{4}
\]
The last formula is the full Hermite residue, not a reduced-spectrum
evaluation rule for arbitrary insertions.

## 2. An exact conjugated Ward operator and scalar current

Put \(z(x)=e^x+e^{-x}\). For \(k\geq1\), define the original two
adjoint spectral shifts
\[
 (\mathcal T_k u)(z(x))=u(z(x+k\hbar))+u(z(x-k\hbar)),
 \tag{5}
\]
\[
 (\mathcal L_k A)(z(x))=
 \sum_{\delta=\pm1}
  \frac{\sinh(x+\delta k\hbar)}{\sinh x}
                 A(z(x+\delta k\hbar)).
 \tag{6}
\]
Their apparent singularities are removable. Both preserve the full
ideal \((P_N)\), and
\(\phi_N(A\mathcal T_k u)=\phi_N(u\mathcal L_k A)\).
Define, in this full algebra,
\[
 \begin{split}
 \mathcal T_k^\epsilon&=M_{f_\epsilon}\mathcal T_kM_{f_\epsilon}^{-1},\\
 \mathcal L_k^\epsilon&=M_{f_\epsilon}^{-1}\mathcal L_kM_{f_\epsilon},\\
 \mathcal D_{m,k}^\epsilon
       &=\mathcal L_k^\epsilon
                          -2q^{mk^2}M_{T_{mk}(z/2)}.
 \end{split}
 \tag{7}
\]
Here \(M_f\) means multiplication by \(f\). The inverse and the
adjoint have opposite conjugation orders; they have not been identified.

**Theorem 1.** For every original polynomial spectator \(A\), including
coefficients in a retained boundary algebra,
\[
 \phi_N\bigl(f_n\mathcal D_{m,k}^\epsilon A\bigr)
                           =E_{m,k}(f_\epsilon A),
 \tag{8}
\]
where \(E_{m,k}\) is the original translated Gaussian contour current.
In particular,
\[
 \boxed{\quad
  \mathcal T_1^\epsilon f_n-2q^mT_m(z/2)f_n
                   =\frac{mN}{\rho}\Xi_0,
 \qquad
  \phi_N(f_n\mathcal D_{m,1}^\epsilon A)
                   =\sigma mN\rho\,A(c_0).
 \quad}
 \tag{9}
\]
At a full logarithmic turn,
\[
                       \mathcal D_{m,N}^\epsilon=0.
 \tag{10}
\]

**Proof.** The actual even Gaussian satisfies
\(\mathcal T_1f_m-2q^mT_mf_m=(mN/\rho)\Xi_0\).
Multiply by \(f_\epsilon\), use (4), and then take the original
adjoint pairing. This proves (9). More generally the original exact
current identity applied to the spectator \(f_\epsilon A\) gives
(8), since \(f_mf_\epsilon=f_n\). There is no division by an unknown
scalar and no change of the exterior.
For (10), \(\mathcal L_N=2I\), \(q^{mN^2}=1\), and
\(T_{mN}(z/2)=(-1)^m=1\) in the full quotient. \(\square\)

The physical current in (9) has the additional original factor
\(\kappa^n\). The scalar is therefore \(\kappa^n\sigma mN\rho\),
not \(\kappa^m\sigma mN\rho\). All external framing and cut lines
stay where they were. For fixed \(m\), its magnitude is bounded by
\(2\pi|m|\); it is zero when \(m=0\).

For the original circle-tree kernel
\[
 K_T(z,w)=\sum_{j=0}^D e_j(z)e_j(w),\qquad K_T(c_0,w)=1,
 \tag{11}
\]
equation (9) immediately has a simultaneous version. Replace the
crossing factor at every vertex in a set \(C\) by its split Ward
difference, before contracting any boundary variable. Then
\[
 \boxed{\quad
  \mathcal J^{\mathrm{even}}_{C,N}
    =\left(\prod_{v\in C}\kappa^{n_v}\sigma m_vN\rho\right)
                       Z_{G\setminus C,N}.
 \quad}
 \tag{12}
\]
The deleted forest keeps all surviving powers and original closures;
the displayed product retains the removed crossing carriers. Other
global scalar factors appear identically on both sides. All boundary
variables remain shared, and all their normals are retained. Indeed
each current is a value functional, so every incident turn kernel
contributes one and every internal edge contributes one only once.
There is no derivative matching polynomial and no \(T\Pi_0\) coupon.
For a more general compiled exterior the statement is the simultaneous
evaluation in (9); an identity kernel, for example, contributes
\(K_I(c_0,w)=e_D(w)\) and must not be silently deleted.

## 3. A canonical analytic unit, with no polynomial inverse zeros

Use the canonical branch
\[
 K(z)=\operatorname{arccosh}(-z/2)^2,
                 \qquad z\in\mathbb C\setminus[2,\infty),
 \tag{13}
\]
with its removable value at \(-2\). The original full-Hermite
functional calculus gives the holomorphic nonvanishing functions
\[
 F_j(z)=q^{-jD^2/4}\exp\!\left(\frac{jK(z)}{2\hbar}\right),
 \qquad [F_j]=f_j\text{ in }\mathcal A_N,\qquad F_aF_b=F_{a+b}.
 \tag{14}
\]
Square brackets mean the actual Hermite class. Thus \(F_\epsilon\),
rather than the polynomial \(f_\epsilon\), supplies a zero-free
analytic inverse on this cut plane.

The canonical analytic representatives of (7) are
\[
 (\mathcal T_{k,\mathrm{can}}^\epsilon u)(z(x))
  =F_\epsilon(z(x))
       \sum_{\delta=\pm1}
       \frac{u(z(x+\delta k\hbar))}
                        {F_\epsilon(z(x+\delta k\hbar))},
 \tag{15}
\]
\[
 (\mathcal L_{k,\mathrm{can}}^\epsilon A)(z(x))
  =\sum_{\delta=\pm1}
    \frac{\sinh(x+\delta k\hbar)}{\sinh x}
    \frac{F_\epsilon(z(x+\delta k\hbar))}{F_\epsilon(z(x))}
                            A(z(x+\delta k\hbar)).
 \tag{16}
\]
Wherever these arguments avoid the cut, they are holomorphic, with
removable differential singularities interpreted by continuation.
At every physical node their required jets are exactly those of (7):
each shifted argument is another physical node, and the chain rule
uses only its prescribed value and first normal. At the simple odd
node the ramification kills the unneeded derivative. Hence (15)--(16)
are source-specific lifts of the finite operators, with no arbitrary
spectator residual.

There is also an exact residue formulation. On the original logarithmic
window, put
\[
 G_j(x)=q^{-jD^2/4}e^{j(x-\pi i)^2/(2\hbar)},\qquad
 \mathcal C=\sum_{a=0}^{N-1}\gamma_{(2a+1)\pi i/N}.
 \tag{17}
\]
The circles are positively oriented and sufficiently small. For every
polynomial \(A\),
\[
 \phi_N(f_nA)
  =\frac{\eta N^2}{4\pi i}\int_{\mathcal C}
          \frac{G_m(x)F_\epsilon(z(x))A(z(x))z'(x)}{P_N(z(x))}\,dx.
 \tag{18}
\]
On this window \(F_\epsilon(z(x))=G_\epsilon(x)\), so the product
is exactly \(G_n\). The original factor \(1/2\) in the angular double
cover, including the ramified simple spectral node, has been retained.

## 4. Local symbol and the original total power

Fix a compact chart inside
\[
                 0<\Im x<2\pi,
 \qquad x=\pi i+it,\qquad |\Re t|<\pi.
 \tag{19}
\]
For a fixed \(k\), take \(N\) sufficiently large that the chart and
its \(\pm k\hbar\) translates remain in this strip. This is the
explicit common-chart hypothesis. In particular it holds on every
fixed compact positive proper-return chart. On this common chart,
\(K(z(x))=(x-\pi i)^2\), so (15)--(16) have the exact ratios
\[
 \frac{G_\epsilon(x+\delta k\hbar)}{G_\epsilon(x)}
       =q^{\epsilon k^2}e^{\delta\epsilon k(x-\pi i)}.
 \tag{20}
\]
Thus the retained half crossing is part of the leading action, not a
bounded spectator amplitude. In the original angular coordinate,
\[
 \kappa^nF_m(-2\cos t)F_\epsilon(-2\cos t)
       =q^{nD^2/4}\exp\!\left(\frac{i nNt^2}{4\pi}\right).
 \tag{21}
\]
Together with the original edge and trace factors, this restores the
selected primitive phase
\[
       \sum_e\psi(t_v,t_w)
             +\frac{i}{4\pi}\sum_v n_vt_v^2-i\sum_vt_v,
 \tag{22}
\]
with its original base-only carriers. Splitting \(n\) has not replaced
it by \(m\) in the filling equation or in the calibrated action.

For clarity, this is not equality of the entire split and unsplit
characteristic varieties. In the kernel orientation of (15), write
a trial local solution as \(e^{S(x)/\hbar}\), with momentum
\(p=S'(x)\). At \(k=1\), the principal split characteristic is
\[
        \cosh\bigl(p-\epsilon(x-\pi i)\bigr)=\cosh(mx).
 \tag{23}
\]
Since \(m\) is even, its two branches, with their logarithmic lifts,
are
\[
       p=n(x-\pi i)\quad\hbox{and}\quad
       p=(\epsilon-m)(x-\pi i)\pmod{2\pi i}.
 \tag{24}
\]
The first is the original selected total-power Gaussian branch;
indeed (15) applied to \(F_n\) satisfies the homogeneous Gaussian
equation exactly on the common chart. The other branch is generally
different from the unsplit opposite branch \(-n\). At \(m=0\) the
two split branches coincide. No exclusion of this other branch or
global cycle selection is claimed.

## 5. The canonical-sheet seam is an explicit endpoint operator

For \(\epsilon=\pm1\), define the *unwrapped* kernel operator
by using (20) everywhere, even beyond (19):
\[
 (\mathcal T_{1,\mathrm{unw}}^\epsilon u)(z(x))
 =q^{-\epsilon}\sum_{\delta=\pm1}
           e^{-\delta\epsilon(x-\pi i)}u(z(x+\delta\hbar)).
 \tag{25}
\]
For a polynomial \(u\), this is a symmetric Laurent polynomial in
\(e^x\), hence a polynomial in \(z\). It therefore has a full
Hermite class, but it is not the same finite operator as (15).
The sheet change itself is explicit. In the immediately adjacent
lower and upper logarithmic strips, respectively,
\[
 \frac{F_\epsilon(z(x))}{G_\epsilon(x)}
   =e^{\epsilon Nx}\quad(-2\pi<\Im x<0),\qquad
 \frac{F_\epsilon(z(x))}{G_\epsilon(x)}
   =e^{-\epsilon N(x-2\pi i)}\quad(2\pi<\Im x<4\pi).
 \tag{25a}
\]
These follow by replacing \(x\) by \(-x\) or \(4\pi i-x\) to
return to (19) in the quadratic defining \(G_\epsilon\).
The separating cut itself is excluded. At the first translated
physical endpoint the ratio is \(-1\); its derivative must also
be retained.

**Proposition 2.** In the original full algebra, for every polynomial
\(u\),
\[
 \boxed{\quad
 (\mathcal T_{1,\mathrm{can}}^\epsilon
          -\mathcal T_{1,\mathrm{unw}}^\epsilon)u
   =2u(c_0)\Pi_0+
       \left\{\frac{\epsilon(1-D)}{\rho}u(c_0)
                                         -2u'(c_0)\right\}\Xi_0.
 \quad}
 \tag{26}
\]
Equivalently the adjoint difference is
\[
 (\mathcal L_{1,\mathrm{can}}^\epsilon
          -\mathcal L_{1,\mathrm{unw}}^\epsilon)A
 =-2A(c_0)\Pi_0+
   \left\{2A'(c_0)+
      \left(\frac{4c_0}{\rho^2}+\frac{\epsilon(1-D)}\rho\right)
                                     A(c_0)\right\}\Xi_0,
 \tag{27}
\]
where \(\mathcal L_{1,\mathrm{unw}}^\epsilon\) is the original
Frobenius adjoint of (25), or (16) with the unwrapped ratios (20).

**Proof.** Interior logarithmic nodes and their first derivatives agree,
since both adjacent nodes stay in the original window. At
\(x_0=\pi i/N\), only the backward term differs. Its canonical inverse
half crossing has the value and logarithmic derivative at \(x_D\),
whereas the unwrapped inverse is evaluated at \(x_{-1}\). These data
are respectively
\[
       (1,-\epsilon D/2),\qquad
                     (-1,-\epsilon(N+1)/2).
 \tag{28}
\]
Their difference is \((2,\epsilon)\). Multiplying by the input
\(F_\epsilon(z(x))\), whose data are \((1,-\epsilon D/2)\), and
by \(u(z(x-\hbar))\), whose derivative is \(-\rho u'(c_0)\),
gives value \(2u(c_0)\) and logarithmic derivative
\(\epsilon(1-D)u(c_0)-2\rho u'(c_0)\).
Divide the latter by \(z'(x_0)=\rho\). At the paired endpoint both
logarithmic derivatives change sign, giving the same spectral normal.
All other required data vanish, proving (26).

For (27), take the original adjoint using
\(\phi_N(\Pi_0 A)=\sigma\{c_0A(c_0)+\rho^2A'(c_0)\}\)
and (4). Coefficients of \(u(c_0)\) and \(u'(c_0)\) give exactly
the displayed formula. This also proves that the differentiated
source has not lost a normal term. \(\square\)

In particular, applying (26) to \(f_n\) yields
\[
 \mathcal T_{1,\mathrm{unw}}^\epsilon f_n
                  -2q^mT_m(z/2)f_n
             =-2\Pi_0+\frac{m-\epsilon}{\rho}\Xi_0.
 \tag{29}
\]
Thus changing sheets reintroduces a value projector and a normal.
They are absent from the correctly retained canonical-sheet current
(9). Equation (29) is not the unsplit odd-power Ward identity, since
its operator is different.

There is no contradiction with (18): equality of original residues
does permit replacing the polynomial half crossing by its canonical
analytic unit. It does not permit replacing its values at translated
arguments by the unwrapped Gaussian after a logarithmic endpoint has
been crossed. Equations (26)--(29) quantify precisely that distinction.

## 6. Coverage and scope

The even Gaussian, the retained-half-crossing factorization, the even
scalar current, and its full-turn cancellation are prior results in
the sources below. The added organization is their exact conjugated
all-exterior operator, simultaneous scalar deletion on arbitrary circle
trees, zero-free canonical analytic lift, and explicit seam operator.

This removes the odd-current matching coupons from this particular
Ward implementation. It does not make every contour boundary a split
Ward current, prove that deleted-forest rates are smaller, or give a
nonzero original geometric coefficient. The canonical analytic lift
does not bound the original polynomial representative away from the
spectrum; such a bound is unnecessary for its exact initial residue
identity but cannot be assumed during a different contour comparison.
The common-chart symbol statement likewise supplies no global contour
across the cut or the endpoint seams.

## Direct sources

The complete source proofs were read; no numerical records or
computational instructions are used.

* [Original Gaussian and retained half crossing](actual_coherent_filling_gaussian_chirp.md),
  SHA256 `d72f50bf1e9af5b15da89784c198a3cb5060b9ee9c3e6cc04b901049be516522`: exact full-Hermite Gaussian and the original
  half-crossing/turn placement.
* [All signed analytic crossing powers](actual_direct_long_power_source.md),
  SHA256 `7c69dbee41401b1d46fa1db1e6046eca0dbde73429eecbead01e6a3bc6067df0`:
  canonical analytic branch of \(K\) and its original crossing scalar.
* [Signed endpoint packet](research_signed_gaussian_ward_endpoint_packet.md),
  SHA256 `6bdced1b01917e41631386a24b337b60dfe5b04d35d70007cb56badc511a0191`: endpoint values, first normals and the even
  Ward identity at both level parities.
* [Original logarithmic contour transport](research_gaussian_logarithmic_contour_transport.md),
  SHA256 `e7d62f6630dec31ac6c87f75baf1ff707ed7af9221ac4c5199549cdd4ee7f36f`:
  full-algebra adjoint, residue prefactor, exact translated currents
  and original identity/turn endpoint values.
* [Global marked proper-return phases](research_global_proper_return_phases.md),
  SHA256 `776df73f66a9d790c2ae6703caa365397e068d9b1a16c8cc5541fba93bd30a78`:
  original phase marking, positive proper-return charts and the scope
  of their local sewing.
* [Original primitive action and its calibration](research_positive_period_inverse_descent.md),
  SHA256 `b9b5c3d61c704700e9431315cf50591c921ebeb95becdf6a52877606bdbc4565`:
  the full total-power primitive phase (22), with the original edge,
  trace and outside-boundary conventions.

Only written mathematics, text reads and file hashes are used. No
mathematical execution, numerical evaluation, tests or compilation
were performed. Other notes and frozen or public files are unchanged.
