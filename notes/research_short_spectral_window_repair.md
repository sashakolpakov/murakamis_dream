# A single spectral representative on short physical windows

Private written proof, 16 November 2026.

The common positive-product baseline has exponentially small errors in
its actual physical value and normal data. On sufficiently short windows,
ordinary spectral Hermite interpolation repairs those errors throughout
the fixed complex product domain. Its exponential cost tends to zero
with the number of rows divided by the level. This gives one separately
even representative with the original action bound on both angular
sides. Its closed window trace has no real repair interface.

This does not remove exterior window sides. Adjacent choices have
exponentially small normalized differences, whose actual shared
spectators must still be included in any estimate of the seam.

## 1. The baseline and its spectral symmetry

Fix a positive pair and the symmetric buffered product domains of the
pinned product-gluing theorem. Work on a fixed smaller product, retaining
a larger symmetric product for every estimate. All these choices precede
the level \(N\). Write
\[
 z=-2\cos t,\qquad w=-2\cos u,\qquad
 \psi(t,u)=\psi(-t,u)=\psi(t,-u).
 \tag{1}
\]
The phase is the original one, on its single branch from completeness.
Let \(H_N(t,u)\) be the phase-normalized common baseline:
\[
 U_N=e^{N\psi}H_N,\qquad
 \sup_K|H_N|\le e^{o_K(N)} .
 \tag{2}
\]
The bulk seed intervals are chosen inside the small complete disk, as
in the pinned fold extension. Its complete-disk comparison gives
\[
 H_N-e^{-N\psi}K_N(-2\cos t,-2\cos u)=O(e^{-cN})
 \tag{3}
\]
on a fixed smaller complete bidisk, with all fixed buffered derivatives.
Only in that bidisk is the canonical off-grid kernel used.

**Lemma 1.** On every fixed smaller symmetric product compact, the
separately even average
\[
 \overline H_N(t,u)=\frac14
     \sum_{\epsilon,\epsilon'\in\{1,-1\}}
                         H_N(\epsilon t,\epsilon'u)
 \tag{4}
\]
satisfies \(\overline H_N-H_N=O(e^{-c_KN})\), with fixed derivatives.
It descends to a holomorphic function \(h_N(z,w)\) on the corresponding
spectral product domain. The phase descends there to \(\Psi(z,w)\).

**Proof.** Each reflection difference is exponentially small on the
complete bidisk by (3), since the canonical kernel and phase are
separately even. It is holomorphic and bounded by \(e^{o(N)}\) on
every buffered compact of the common symmetric product by (2).
The finite complex-ball propagation argument in the pinned fold
extension therefore makes it exponentially small on any fixed smaller
product compact. Averaging proves the first assertion. This is an
estimate of the actual baseline's symmetry defect, not an assumed
symmetry of a one-sided repair.

Inside \(|\Re t|<\pi\), the fibers of \(-2\cos t\) are precisely
the pairs \(t,-t\), except for their meeting at zero. The domains
are symmetric. An even holomorphic function therefore descends;
at zero its even Taylor series is holomorphic in \(z+2\).
Apply this separately in both variables, also to the original even
phase. Compact spectral subsets have buffered preimages in the angular
domains, so spectral Cauchy estimates retain the stated bounds.
\(\square\)

Use the original physical nodes and relation
\[
 c_j=2\cos((2j+1)\pi/N),\quad
 0\le j\le J_N=\lfloor(N-1)/2\rfloor,\quad
 P_N(z)=2T_N(z/2)+2,\quad \eta=(-1)^{N-1}.
 \tag{5}
\]
A double node has multiplicity \(\nu_j=2\). The last node at odd
level is \(c_{J_N}=-2\) and has \(\nu_{J_N}=1\).
Let
\[
 F_j(w)=K_N(c_j,w),\qquad
 G_j(w)=\partial_zK_N(c_j,w)
 \tag{6}
\]
and retain the pole-free representative \(\widehat G_j\) only at
double nodes. It agrees with \(G_j\) in every required physical
second-endpoint jet. There is no first spectral normal at the odd
simple node.

Choose fixed eligible real row intervals: either the bulk intervals
of the product-baseline theorem or the fold neighborhoods of its pinned
extension. On each such interval, those theorems and Lemma 1 give
exponentially small normalized line errors, uniformly on a buffered
compact in the other spectral variable. In spectral coordinates the
targets are
\[
 T_{j,0}(w)=e^{-N\Psi(c_j,w)}F_j(w),
 \tag{7}
\]
\[
 T_{j,1}(w)=e^{-N\Psi(c_j,w)}
       \{\widehat G_j(w)-N\Psi_z(c_j,w)F_j(w)\},
             \qquad \nu_j=2.
 \tag{8}
\]
The errors \(T_{j,a}-\partial_z^a h_N(c_j,w)\), \(a<\nu_j\),
are \(O(e^{-cN})\). Define \(S_{k,b}(z)\) by exchanging the endpoints;
their errors have the same conclusion after taking the smaller exponent.
Every fixed derivative in the other spectral parameter is included.
Conversion from angular normals near a double fold node costs at most
a power of \(N\); the odd simple row is not divided by a vanishing
angular derivative. The exponent \(c>0\), chosen to cover the finitely
many value and first mixed errors used below, is fixed before selecting
the short subwindows.

## 2. The quantitative finite spectral interpolation bound

Let \(I_N=\{j_0,\ldots,j_0+m-1\}\) be consecutive distinct physical
rows, and retain their original multiplicities. Put
\[
 Q_I(z)=\prod_{j\in I_N}(z-c_j)^{\nu_j},\qquad
 q_j(z)=\frac{Q_I(z)}{(z-c_j)^{\nu_j}},\qquad
 \ell_j(z)=\frac{q_j(z)}{q_j(c_j)}.
 \tag{9}
\]
At a simple node define \(V_{j,0}=\ell_j\). At a double node define
\[
 V_{j,0}(z)=
      \{1-\ell_j'(c_j)(z-c_j)\}\ell_j(z),\qquad
 V_{j,1}(z)=(z-c_j)\ell_j(z).
 \tag{10}
\]
These polynomials have degree less than \(\deg Q_I\) and satisfy
\[
 \partial_z^aV_{j,b}(c_k)=\delta_{jk}\delta_{ab},
                      \qquad a<\nu_k,\quad b<\nu_j .
 \tag{11}
\]
Thus no additional derivative is imposed at a simple node.

**Lemma 2.** On every fixed spectral compact, with fixed derivative
order \(p\), the interpolation operator
\[
 \mathscr L_I d(z)=
           \sum_{j\in I_N}\sum_{a<\nu_j}d_{j,a}V_{j,a}(z)
 \tag{12}
\]
obeys
\[
 \|\partial_z^p\mathscr L_I d\|
 \le C_p N^{B_p}
       \exp\!\left\{C_Km\left(1+\log\frac Nm\right)\right\}
          \max_{j,a}|d_{j,a}|.
 \tag{13}
\]
The constants are uniform over the location of the consecutive window,
including windows meeting the fold. In particular, for
\(m\le\delta N\), \(0<\delta<1/4\), its exponential cost is at most
\[
 \omega_K(\delta)N,\qquad
 \omega_K(\delta)=C_K\delta(1+|\log\delta|)\longrightarrow0.
 \tag{14}
\]

**Proof.** For distinct physical indices \(j,k\), let \(d=|j-k|\).
The exact cosine identity and their index range give
\[
 |c_j-c_k|
 =4\sin((j+k+1)\pi/N)\sin(d\pi/N)
 \ge4\sin^2(d\pi/N)\ge16d^2/N^2 .
 \tag{15}
\]
Indeed \(d\le j+k+1\le N-d\) and \(d\le N/2\). For
\(r=j-j_0\), it follows that
\[
 \prod_{\substack{k\in I_N\\k\ne j}}|c_j-c_k|
 \ge (16/N^2)^{m-1}\{r!(m-1-r)!\}^{\,2}.
 \tag{16}
\]
Since all distances are at most four and each multiplicity is one or
two,
\[
 |q_j(c_j)|\ge
 4^{-(m-1)}
 \left(\prod_{k\ne j}|c_j-c_k|\right)^2 .
 \tag{17}
\]
On \(|z|\le R\), the numerator \(q_j(z)\) is bounded by
\(\max(1,R+2)^{2(m-1)}\). Also
\[
 r!(m-1-r)!\ge (m-1)!/2^{m-1}
              \ge\{(m-1)/(2e)\}^{m-1}.
 \tag{18}
\]
For \(m\ge2\), (16)--(18) bound \(\ell_j\) by
\(\exp\{C_Rm(1+\log(N/m))\}\), after changing the constant.
For \(m=1\), the cardinal polynomials are \(1\) and, when needed,
\(z-c_j\), so the same conclusion holds directly.

The remaining coefficient satisfies
\[
 |\ell_j'(c_j)|
 =\left|\sum_{k\ne j}\frac{\nu_k}{c_j-c_k}\right|
 \le C N^2\sum_{d\ge1}d^{-2}\le C'N^2 .
 \tag{19}
\]
Equations (10), (18)--(19), followed by the at most \(2m\) summands,
give (13) for values. Cauchy on a fixed larger disk gives every fixed
derivative with the same exponential rate. Finally
\(x(1+\log(1/x))\) is increasing for \(0<x\le1\), so (14) follows.
No separation assumption stronger than the actual grid has been used.
\(\square\)

## 3. One exact representative on both sides

Fix a buffered spectral product compact as in Section 1, enlarged
within the same domains to contain the eligible real row intervals
as well as the target. Let \(I_N\)
and \(J_N'\) be consecutive subwindows of the eligible row intervals,
with at most \(\delta_zN\) and \(\delta_wN\) distinct rows respectively.
The window widths are fixed positive numbers, independent of \(N\),
chosen only after the exponent \(c\) in Section 1. Require
\[
             \omega_z(\delta_z)+\omega_w(\delta_w)<c/4.
 \tag{20}
\]
Use the interpolation bases (9)--(10) in each variable; write
\(W_{k,b}(w)\) for the second basis. Set
\[
 d_{j,a}(w)=T_{j,a}(w)-\partial_z^ah_N(c_j,w),\qquad
 e_{k,b}(z)=S_{k,b}(z)-\partial_w^bh_N(z,c_k).
 \tag{21}
\]
The actual full mixed physical jets give exactly
\[
 c_{jk}^{ab}:=\partial_w^bd_{j,a}(c_k)
                   =\partial_z^ae_{k,b}(c_j),
                 \quad a<\nu_j,\ b<\nu_k .
 \tag{22}
\]
At a simple endpoint only the value index occurs. In particular (22)
does not complete that endpoint by an artificial spectral normal.

Define
\[
 \begin{split}
 E_z(z,w)&=\sum_{j,a}d_{j,a}(w)V_{j,a}(z),\\
 E_w(z,w)&=\sum_{k,b}e_{k,b}(z)W_{k,b}(w),\\
 E_{zw}(z,w)&=\sum_{j,k,a,b}c_{jk}^{ab}
                             V_{j,a}(z)W_{k,b}(w),\\
 \mathcal K_{I,J,N}(z,w)
   &=e^{N\Psi(z,w)}
           \{h_N(z,w)+E_z(z,w)+E_w(z,w)-E_{zw}(z,w)\}.
 \end{split}
 \tag{23}
\]
Every coefficient function is defined on the buffered spectral parameter
domain from Section 1; the polynomial bases introduce no extra poles.

**Theorem 3.** On the entire fixed smaller spectral product compact,
\[
 e^{-N\Psi}\mathcal K_{I,J,N}
                 =h_N+O(e^{-c'N}),\qquad
 |\mathcal K_{I,J,N}|
                 \le \exp\{N\Re\Psi+o(N)\}
 \tag{24}
\]
for some \(c'>0\), with all fixed buffered spectral derivatives of the
normalized error. This holds on both angular sides, without a designated
sign or a restriction to a thin opposite collar. Its exact line data are
\[
 \begin{split}
 \mathcal K_{I,J,N}(c_j,w)&=F_j(w),&
 \partial_z\mathcal K_{I,J,N}(c_j,w)&=\widehat G_j(w)
                                     \quad(\nu_j=2),\\
 \mathcal K_{I,J,N}(z,c_k)&=F_k(z),&
 \partial_w\mathcal K_{I,J,N}(z,c_k)&=\widehat G_k(z)
                                     \quad(\nu_k=2).
 \end{split}
 \tag{25}
\]
The angular pullback is separately even.

**Proof.** The coefficients in (21)--(22) are \(O(e^{-cN})\), with
the exponent fixed before (20). Lemma 2
controls \(E_z,E_w\); its two operator bounds control \(E_{zw}\).
There are only polynomially many terms. Equation (20) leaves a positive
exponential margin, proving (24), also on fixed derivative buffers.
The baseline satisfies (2).

At a first node, the first correction supplies its target error.
By (11) and (22), the jets of \(E_w\) are exactly those of \(E_{zw}\)
and cancel. The second-node argument is identical. Removing the
normalizing exponential in (7)--(8) proves (25). These are identities
as holomorphic functions of the other variable, not merely identities
at isolated physical pairs. The spectral construction proves evenness.
\(\square\)

The small-window choice is essential to the argument: the exponential
accuracy is established on a larger fixed row interval before its
short subwindow is selected. No assertion makes that accuracy exponent
independent of an interval simultaneously shrinking in its construction.
For a fixed finite collection of such choices using the same \(h_N\),
(24) also makes every normalized difference exponentially small on
the common compact. The smallest of their finitely many positive
exponents may be used.

## 4. Exact closed traces and the remaining boundary terms

Let \(\gamma_I\) be a closed positive spectral contour enclosing just
the selected first-window nodes, within the domain where (23) is
defined. Keep an original spectral spectator \(P(z;\ldots)\), including
all crossings, shared variables and its derivative. Then
\[
 \Phi^\sharp_{I,N}(w;\ldots)
 =\frac{\eta N^2}{2\pi i}
       \int_{\gamma_I}
       \frac{P(z;\ldots)\mathcal K_{I,J,N}(z,w)}{P_N(z)}\,dz .
 \tag{26}
\]
At a double node its contribution is exactly
\[
 \eta\{(4-c_j^2)
       [\widehat G_j(w)P(c_j)+F_j(w)P_z(c_j)]
                         -c_jF_j(w)P(c_j)\},
 \tag{27}
\]
and an odd simple selected node contributes \(F_{J_N}(w)P(-2)\).
These follow from the original relation:
for a double node,
\[
 \left.\frac{P_N(z)}{(z-c_j)^2}\right|_{z=c_j}
   =\frac{N^2}{4-c_j^2},\qquad
 \left.\partial_z\log\frac{P_N(z)}{(z-c_j)^2}\right|_{z=c_j}
   =\frac{c_j}{4-c_j^2},
 \tag{28}
\]
whereas \(P_N'(-2)=N^2\) at odd level.
For (28), evaluate
\((4-z^2)P_N''-zP_N'+N^2(P_N-2)=0\) at a double root and
differentiate it once. This gives
\(P_N''(c_j)=2N^2/(4-c_j^2)\) and
\(P_N'''(c_j)/P_N''(c_j)=3c_j/(4-c_j^2)\), which are exactly
the two Taylor coefficients in (28).

Thus (26) is the same sharp window expression as in the pinned sources.
Its difference from the original free-\(w\) window trace is
\(P_N(w)\) times a holomorphic slit function, and equality with the
original follows after the required subsequent complete second trace,
including every spectator normal. If both endpoints are traced on the
selected windows, (22) gives the original double-window functional
directly. No arbitrary unreduced free polynomial is replaced.

For a centered mirror angular window, (26) equivalently has the
prefactor \(-\eta/(4\pi^2i)\) against
\[
 D_h(X)\sin(2\pi X)
       P(C(X))\mathcal K_{I,J,N}(C(X),w)\,dX,
 \qquad D_h=(\pi N)^2\sec^2(\pi NX).
 \tag{29}
\]
It uses the same function on the lower and upper halves. Consequently
the real interface term is exactly zero. Both lifts of a double node
and the single odd central value have the multiplicity proved in the
fold source; no spectral normal is supplied at that center.

This cancellation concerns the repair interface only. The closed
contour still has all its exterior sides. If neighboring cells use
different short-window representatives, their common side contains
their actual difference. Equation (24) bounds that difference by
\(\exp\{N\Re\Psi-c'N+o(N)\}\), but it must be multiplied by the
entire original spectator, trace density, and any remaining factors.
A larger real boundary action need not be paid by \(c'\). No seam
is deleted without that further estimate.

The selected windows may cover a supplied compact set of rows inside
the eligible intervals by finitely many cells. This gives a finite
family of compatible estimates; it does not assert one exact
representative for the union with the same
bound, a complete grid near \(t=\pm\pi\), or a controlled global filled
cycle. In particular (25) prescribes only the selected short windows,
not the full data of an entire periodic angular strip.

## Direct sources and author audit

The proof uses these complete direct texts at their fixed versions:

* [Common positive-product baseline](research_positive_product_window_gluing.md),
  SHA256 ace4f667038c494e2690a77496ce32e8bc8538535356b78600e8ad8ced8183d5:
  common bounded baseline, bulk line accuracy, exact mixed data, and
  the sharp-trace versus free-color distinction.
* [Fold-window extension](research_positive_product_fold_window_extension.md),
  SHA256 3c37b5fbe1ec4c8d6ddc137fe22dcc43428c18f8a99203627bad7e5b64aead17:
  complete-disk comparison, uniform fold line accuracy and finite
  propagation, mirrored trace normalization and the odd simple value.

The finite spectral interpolation estimate is proved directly here.
Only written mathematics, source reads and metadata hashes are used.
No mathematical program, numerical computation, test or compilation
is run. Frozen notes and public manuscripts are unchanged.
