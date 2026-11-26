# One-sided spectral factors change the filled stationary equation

The exact LEFT and RIGHT numerators carry oscillatory factors that have zero exponential rate on the real spectrum but nonzero leading logarithmic derivatives on their analytic modes. They cannot be omitted in a direct filled-period argument.

This note proves the charge shift before any saddle or representation is assigned. It isolates the extra geometric and contour work needed to apply the [fixed-complement representation-volume gap](/private/tmp/md-filled-complement-representation-gap.md). No bound for the full complementary period is asserted.

## 1. The exact factor in every one-sided numerator

Let \(N\ge3\), \(d=N-1\), \(m=\lfloor N/2\rfloor\), and
\[
 q=e^{\pi i/N},\qquad
 c_r=q^{2r+1}+q^{-2r-1},\qquad
 \sigma=-2\cos(2\pi\delta),\qquad
 \alpha_r=c_r-\sigma.
 \tag{1}
\]
The literal LEFT interval is \(0\le i\le j\le m-1\). Its exact original numerator is
\[
 (-1)^dH_{\mathrm L}
 =A_N^{\mathrm{half}}(\delta)
   \sum_{0\le i\le j<m}
       b^ic^{d-j}
       \left(\prod_{r<i}\alpha_r\right)
       \left(\prod_{j<r<m}\alpha_r\right)K_{i,j},
 \qquad
 A_N^{\mathrm{half}}=\prod_{r=m}^{d}\alpha_r .
 \tag{2}
\]
The active continuant \(K_{i,j}\), both unused products, and every endpoint remain those of [the original four-state transfer](/private/tmp/murakamis_dream-publication/notes/research_original_one_sided_four_state_transfer.md), §§1–3. Define the polynomial after \(A_N^{\mathrm{half}}\) in (2) by the displayed sum; do not define it by dividing a sampled zero.

The exact product is
\[
 A_N^{\mathrm{half}}(\delta)=
 \begin{cases}
 2\cos(N\pi\delta),&N\text{ even},\\
 -4\sin(\pi\delta)\sin(N\pi\delta),&N\text{ odd}.
 \end{cases}
 \tag{3}
\]
This identity holds holomorphically in \(\delta\). For even \(N=2m\), the omitted product is the monic polynomial \(2T_m(x/2)\) at \(x=2\cos(2\pi\delta)\): its roots are the original \(m\) distinct omitted nodes with their minus signs, and both leading coefficients are one. For odd \(N=2m+1\), put \(w=e^{i\pi\delta}\), so \(x=w^2+w^{-2}\). The Laurent expression \((w-w^{-1})(w^N-w^{-N})\) is a monic polynomial in \(x\) of degree \(m+1\), with roots \(2\cos(2\pi k/N)\), \(0\le k\le m\). These are exactly \(-c_r\), \(m\le r\le2m\), with their multiplicities. This proves (3), including its signs. Reflection sends \(r\) to \(d-r\), and \(c_{d-r}=c_r\); hence the reflected RIGHT numerator has the same scalar, with its own reflected remaining polynomial and face order.

For \(\varepsilon\in\{-1,1\}\), write
\[
 A_N^{\mathrm{half}}(\delta)
   =\sum_{\varepsilon=\pm1}
          a_{N,\varepsilon}(\delta)e^{i\varepsilon N\pi\delta},
 \qquad
 a_{N,\varepsilon}(\delta)=
 \begin{cases}
 1,&N\text{ even},\\
 2i\varepsilon\sin(\pi\delta),&N\text{ odd}.
 \end{cases}
 \tag{4}
\]
At odd levels the two modes cancel at the complete endpoint. Their derivatives also must be combined before applying the original spectral normal functional. The formula has not removed or regularized that endpoint.

## 2. Shared coefficient extraction does not remove these modes

Fix an arbitrary finite sector choice \(\mathfrak s\in\{\mathrm C,\mathrm L,\mathrm R\}^{E}\). Let \(J\subset E\) be its set of one-sided boxes. The scalar (3) is independent of every face variable. Consequently its exact shared coefficient factors as
\[
 C_{N,\mathfrak s}(\boldsymbol\delta)
   =\left(\prod_{e\in J}A_N^{\mathrm{half}}(\delta_e)\right)
            B_{N,\mathfrak s}(\boldsymbol\delta).
 \tag{5}
\]
Here \(B_{N,\mathfrak s}\) is the original coefficient of the product of CROSS numerators and the polynomial remaining in each one-sided numerator. It retains the common face variables, protected zeros, original degree demands, and all raw signs. No face radius or exterior degree is optimized independently.

This statement is valid for every actual matched-sphere Morse source. In particular it applies to every fixed even opposite-offset bipyramid with its literal marked edge and ordered quartets. It is not a reduction to a scalar two-box kernel.

## 3. Exact half-charge form of the filling functional

The original Fourier functional of [the Morse period theorem](/private/tmp/murakamis_dream-publication/notes/actual_morse_cross_filling_period.md), equation (2), is linear in its spectral numerator. Its derivation is the original trace identity, so the same functional applies to each polynomial sector. Write its common exterior scalar as
\[
 \mathcal Q_{N,\mathbf n}=q^{d^2\sum_e n_e/4}(-i)^{|E|}.
\]
Extend \(\varepsilon_e=0\) outside \(J\). For a fixed finite cutoff on the original integer charge lattice, substitute (4)–(5) into that functional. This gives exactly
\[
\begin{split}
 I_{N,\mathbf n}^{\mathfrak s}
={}&\mathcal Q_{N,\mathbf n}
 \sum_{\boldsymbol\ell\in(\mathbb Z\setminus\{0\})^E}
       \left(\prod_e\ell_e\right)
       (-1)^{(N+1)\sum_e\ell_e}
 \sum_{\boldsymbol\varepsilon\in\{\pm1\}^{J}}
 \int_{[-1/2,1/2]^E}
 B_{N,\mathfrak s}(\boldsymbol\delta)
       \prod_e\sin(2\pi\delta_e)\\
&\quad\cdot
       \prod_{e\in J}a_{N,\varepsilon_e}(\delta_e)
 \exp\left\{
 N\sum_e\bigl(\pi i n_e\delta_e^2
                 +2\pi i\kappa_e\delta_e\bigr)\right\}
 d\boldsymbol\delta,\qquad
 \kappa_e=\ell_e+\frac{\varepsilon_e}{2}\mathbf1_{e\in J}.
\end{split}
 \tag{6}
\]
For the infinite expression, equality is understood with the same cutoff or boundary-value convention as the original Fourier formula. The inner mode sum is finite, so it commutes with that linear regularization. This statement does not assert separate absolute convergence of the half-charge periods.

The prefactor is still \(\prod_e\ell_e\), not \(\prod_e\kappa_e\). The parity character still uses the original integers \(\ell_e\). Replacing either by a new half-integer-lattice formula would change the original trace. All endpoint currents are still part of (6).

In particular, a non-CROSS box with original charge \(\ell_e=1\) produces magnitudes \(1/2\) and \(3/2\). This is an exact finite source fact, independent of any large-\(N\) interpretation.

## 4. The actual derivative missing from a modulus envelope

Suppose on one regular chart a remaining coefficient has an analytic action
\[
 B_{N,\mathfrak s}(\delta)
       =e^{N A_{\mathfrak s}(\delta)+o(N)}
\]
with enough uniformity to differentiate its leading phase. This is an additional analytic hypothesis; the positive transfer envelope does not supply it. A mode of (6) has leading phase
\[
 S_{\mathfrak s,\boldsymbol\ell,\boldsymbol\varepsilon}
   =A_{\mathfrak s}(\delta)
      +\pi i\sum_e n_e\delta_e^2
      +2\pi i\sum_e\kappa_e\delta_e .
 \tag{7}
\]
Its spectral stationary equation is
\[
 \partial_e A_{\mathfrak s}
         +2\pi i n_e\delta_e+2\pi i\kappa_e=0.
 \tag{8}
\]
The omitted-half mode has contributed
\[
 \partial_{\delta_e}\bigl(i\varepsilon_e\pi\delta_e\bigr)
                   =i\varepsilon_e\pi.
 \tag{9}
\]
It had zero real exponential rate on the real \(\delta_e\)-axis, but its derivative is a leading term.

To see the marking issue precisely, suppose one attempted to reuse the CROSS assignments
\[
 \widetilde U_e
       =\partial_e A_{\mathfrak s}
                    +2\pi i\epsilon_e\delta_e,\qquad
 V_e=-4\pi i\delta_e,\qquad n_e=\epsilon_e-2p_e .
 \tag{10}
\]
Then (8) gives
\[
 \widetilde U_e+p_eV_e=-2\pi i\kappa_e.
 \tag{11}
\]
At a one-sided box, exponentiating (11) gives \(-1\), not \(1\). It is not the original smooth primitive filling equation. If instead the geometrically correct auxiliary meridian were
\[
 U_e=\widetilde U_e+i\varepsilon_e\pi
                    \mathbf1_{e\in J},
 \tag{12}
\]
then (8) would give \(U_e+p_eV_e=-2\pi i\ell_e\), as required at the original integer charge. But (12) changes the meridian similarity by a sign. It requires an actual marked matrix/collar proof, not a choice of logarithm differing by \(2\pi i\). An SL central sign does not change a projective similarity and cannot repair this sign.

Thus this computation is not a claim that one-sided terms necessarily represent a cone manifold. It proves that the CROSS peripheral identification cannot be transferred to their reduced action while omitting (9). The phase may be restored by a different genuine boundary representation or by the coupled sum of modes; neither has been proved for the whole complementary source.

The stationary real absolute-value classification uses derivatives of
\(\log|\alpha|\), \(Q_q\), and \(J_q\). Its Green condition and odd face-cycle obstruction concern that real envelope. They do not by themselves provide the analytic \(A_{\mathfrak s}\), its full fundamental chain, or the meridian in (12).

### A quadratic test of the charge comparison

The sign of the omitted charge matters even before a geometric interpretation. Let a hypothetical regular coefficient action be \(A(\delta)=\Phi-C\delta^2\), \(C>0\), and retain the original chirp. Its charge-\(\kappa\) phase has critical value
\[
 S_\kappa=\Phi-\frac{\pi^2\kappa^2}{C-i\pi n},\qquad
 \operatorname{Re}S_\kappa
       =\Phi-\frac{\pi^2C\kappa^2}{C^2+\pi^2n^2}.
 \tag{12a}
\]
Therefore
\[
 \operatorname{Re}S_{1/2}-\operatorname{Re}S_1
       =\frac{3\pi^2C}{4(C^2+\pi^2n^2)}>0
 \tag{12b}
\]
for either sign of the fixed nonzero power \(n\). Thus the positive quadratic curvature and the usual ordering of integer charges do not bound a half-charge contribution below the unit-charge packet.

This is a test of the proposed inference, not a model asserted for the actual one-sided coefficient. Its \(A_{\mathfrak s}\), mode amplitudes, and cycles still have to be derived. In particular the two exact modes can cancel, and this calculation makes no lower claim for their sum.

## 5. The existing local geometric calculation and its remaining boundary chain

There is a substantive local input in [the mixed critical Green regulator](/private/tmp/murakamis_dream-publication/notes/research_actual_mixed_critical_green_regulator.md). It uses the true auxiliary color, rather than assigning complete color to every strand, and proves the local mixed Bloch sum and its differential on a regular real Green collar.

It also explicitly retains the remaining global problem: the nonunipotent auxiliary strand uses different eigenflags at over- and under-crossings. The cusp bridge chains and their peripheral decoration correction have not been sewn into the original relative fundamental class. A unit-modulus auxiliary eigenvalue does not make that correction zero. Protected-line limits, singular endpoints, and the complex filling deformation are additional interfaces.

For a direct filled-volume argument the needed upgrade is therefore concrete:

1. Continue the original one-sided coefficient with its exact modes and monomial phases.
2. Construct the corresponding full ordered matrix representation, including the original cups, caps, and mark.
3. Prove its primitive \(U_e,V_e\), with any correction such as (12), and prove the actual slope word is identity.
4. Identify its complete sewn regulator with the original filled fundamental class.
5. Exclude the geometric representation from the relevant complementary cycles and control every singular or endpoint current.

The representation gap then applies. It does not perform any of these source operations.

## 6. Why root Green identities do not remove the obligation

The exact root identity
\[
 \mathsf C(x,y)=c_0I-D(Z+xI)(Z+yI)D
\]
is self-adjoint for the top-coefficient bilinear pairing. But its product rule is
\[
 D(fg)=(Df)\,g(qz)+f(q^{-1}z)\,Dg.
 \tag{13}
\]
Consequently moving a derivative through the full sewn product shifts the other shared factors. It does not yield an unshifted cancellation of the two-box bulk. The complete finite calculation in [the sewn-current record](/private/tmp/md-cyclic-signed-global-current-results.json) has
\[
 N=3,\quad m=6,\quad
 Z=910845,\quad Z_{\mathrm{north}=I}=115587,\quad
 Z_{\mathrm{south}=I}=243,
\]
and the original unprojected Green bulk equals \(-2051892\). This is only an obstruction to that cancellation identity, not a counterexample to a filled-period estimate. The [root operator lemma](/private/tmp/md-root-face-operator-factorization-and-shifted-pairing.md) keeps the shifts exactly.

The new filled-period route remains logically possible and weaker than a uniform spectral sup-norm gap. What is now precise is the distinction between its available geometric gap and its missing signed source-to-representation and relative-cycle adapters.


## 7. Reproducible finite check

The standard-library script [the half-charge audit](/private/tmp/md-filled-complement-half-charge-audit.py) constructs the omitted products independently in \(\mathbb Z[q]/(\Phi_{2N}(q))\), retaining a formal Laurent variable \(w=e^{i\pi\delta}\). Its [recorded output](/private/tmp/md-filled-complement-half-charge-results.json) checks \(N=3,\ldots,18\), both reflected products, all Laurent coefficients, the even complete value, the odd zero and spectral first derivative, and the half-charge exponent arithmetic. It performs 440 exact checks. These finite checks support the all-level polynomial proof above; they do not estimate a period.

At odd \(N\), the exact polynomial factor has
\[
 A_N^{\mathrm{half}}(-2)=0,\qquad
 \left.\frac{dA_N^{\mathrm{half}}}{d\sigma}\right|_{\sigma=-2}=-N.
 \tag{14}
\]
For example this follows from \(A''(w)|_{w=1}=8N\) and \(\sigma''(w)|_{w=1}=-8\). This is a statement about the polynomial factor and its normal; it is not a claim that the odd simple node uses a double-node trace rule. Keeping the finite polynomial identity automatically preserves whichever value and normal data the original spectral functional requires.
