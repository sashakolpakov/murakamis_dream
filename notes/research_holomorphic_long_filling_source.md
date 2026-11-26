# A connected holomorphic chamber of the original filling source

Written proof, 24 November 2026.

The entire original filling source has a nonzero asymptotic on a
connected complex chamber containing all sufficiently long real signed
tuples. The chamber also contains arbitrarily large positive imaginary
powers. Uniformity is local on its compact subsets, before parameter
differentiation. This gives an actual source logarithm and a calibrated
leading logarithmic differential, rather than only formal saddle data.
It does not continue the source to an arbitrary short real filling.

## 1. The exact source and the chamber theorem

Fix one strict Conway construction of [M], with \(b\ge2\) circles.
Retain all original products, turns, marks, disk framings, peripheral
conventions and finite affine wire offsets. For integers \(N\ge3\), put
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \kappa=e^{\pi i d^2/(2N)},\qquad
 \Gamma_N(s)=\exp\!\left({\pi i d^2\over4N}\sum_js_j\right).
 \tag{1}
\]
All powers of \(\kappa\) mean this exponential lift.
At \(c_k=q^{2k+1}+q^{-2k-1}\), \(0\le k\le d\), the full crossing family is
\[
 R_s(c_k)=\kappa^s h_k(s),\quad
 h_k(s)=\exp\!\left({\pi i s\over N}k(k-d)\right),\quad
 (w\partial_w)R_s(w+w^{-1})|_{w=q^{2k+1}}
       =-{s\over2}(d-2k)R_s(c_k).
 \tag{2}
\]
The normal is imposed only at double nodes. At the odd simple node
its displayed value is zero and adds no condition.
The exact symmetry \(h_{d-k}=h_k\), with opposite reflected normals,
makes (2) consistent. Full Hermite interpolation in
\(\mathbb C[z]/(2T_N(z/2)+2)\), where \(T_N\) is the Chebyshev
polynomial of the first kind, defines an entire family with
\(R_sR_t=R_{s+t}\), agreeing with every original signed integer power.
This is the specified logarithmic lift of [R], not a numerical choice
of a fractional power.

Let \(Z_N(s)\) be the original unframed reduced tensor evaluation with
these coupons at its filling disks. It is entire in \(s\in\mathbb C^b\).
At allowed integers it is the original tensor source before the writhe
correction of [M]. Write \(\widehat Z_N=\Gamma_N^{-1}Z_N\).
Noninteger parameters define an analytic source, not a topological move.

The strict pure Fourier polynomial of [P,W] is
\[
 \mathcal F_N(z)=\sum_{|h_j|\le H_N}C_N(h/N)e^{2\pi i h\cdot z}
 =N^{3/2+b/2}B(z)e^{N\Psi(z)}(1+O(N^{-1})).
 \tag{3}
\]
The expansion is uniform holomorphically near zero, \(B\) is a unit,
\(\Psi(0)=F_0\), and
\(\Psi''(0)=-2\operatorname{diag}(g_j)\), \(g_j=\pi/X_j>0\).
The action is separately even and real on real arguments. The same
exact polynomial has a shared spectral gap on the entire real cube
and a fixed complex strip away from zero. The full physical color
source differs from its retained pure corridor by at most
\(e^{N(F_0-\gamma_*)}\), with a fixed \(\gamma_*>0\), before folding.
These are the complete-source estimates of [F,P,W].

**Theorem.** There exist \(L>1\) and \(\eta>0\), depending on this
fixed construction, such that on the connected open domain
\[
 \Omega_{L,\eta}
   =\{s\in\mathbb C^b:\ |s_j|>L,\ \Im s_j>-\eta
                                      \text{ for every }j\}
 \tag{4}
\]
there is a unique nearby holomorphic unit-charge critical point
\[
 \nabla\Psi(z(s))+2\pi i\operatorname{diag}(s)z(s)
                         +2\pi i\mathbf1=0.
 \tag{5}
\]
Every \(z_j(s)\) has positive imaginary part. Define
\[
 \begin{split}
 S(s)&=\Psi(z(s))+\pi i\sum_js_jz_j(s)^2+2\pi i\sum_jz_j(s),\\
 \mathcal Q(s)&=-\Psi''(z(s))-2\pi i\operatorname{diag}(s),\\
 D(s)&={(-2i)^b(2\pi)^{b/2}B(z(s))\prod_j\sin(2\pi z_j(s))
                              \over\sqrt{\det\mathcal Q(s)}} .
 \end{split}\tag{6}
\]
The Gaussian root is the branch on matrices with positive real part.
The functions \(S,D\) are holomorphic on \(\Omega_{L,\eta}\), \(D\)
is nowhere zero and has a specified holomorphic logarithm. The
holomorphic normalized error defined by
\[
 \widehat Z_N(s)=N^{3/2}D(s)e^{NS(s)}(1+E_N(s))
 \tag{7}
\]
satisfies, for every compact \(K\Subset\Omega_{L,\eta}\) and fixed
multi-index \(\alpha\),
\[
 \sup_K|\partial_s^\alpha E_N|\le C_{K,\alpha}/N .
 \tag{8}
\]
For every such \(K\), the actual source is nonzero on a buffered
neighborhood of \(K\) for all sufficiently large \(N\). A logarithm
there can be fixed so that, with all fixed derivatives on \(K\),
\[
 \begin{split}
 \log\widehat Z_N&=\tfrac32\log N+NS+\log D+O_K(N^{-1}),\\
 {1\over N}d\log\widehat Z_N
    &=dS+{1\over N}d\log D+O_K(N^{-2}),\qquad
 dS=\pi i\sum_jz_j(s)^2\,ds_j .
 \end{split}\tag{9}
\]
The action has the absolute anchor \(S(s)\to F_0\) as
\(\min_j|s_j|\to\infty\) inside (4).
Both level parities and composite levels are included.
The level threshold and constants depend on \(K\): no one threshold
gives zero-freeness on the whole unbounded domain, and no estimate for
parameters growing with \(N\) is asserted.

## 2. The complete complex-power source budget

Set \(\widetilde R_s=\kappa^{-s/2}R_s\) and
\(z_k=(k+1/2)/N-1/2\). Its physical value and angular normal are
\[
 \widetilde R_s(c_k)=e^{\pi i sNz_k^2},\qquad
 (w\partial_w)\widetilde R_s|_{w=q^{2k+1}}
                         =sNz_k e^{\pi i sNz_k^2}.
 \tag{10}
\]
They have moduli at most \(E\) and \(|s|NE/2\), respectively, where
\(E=\exp[(\pi N/4)(-\Im s)_+]\).
Writing the canonical polynomial as
\(a_0+\sum_{a=1}^{N-1}a_a(w^a+w^{-a})\), finite Fourier-Hermite inversion gives
\[
 a_0=H_0,\qquad a_a={D_a+(N-a)H_a\over N}\quad(1\le a<N).
 \tag{11}
\]
Here \(H_a=N^{-1}\sum_k\widetilde R_s(c_k)w_k^{-a}\) and
\(D_a=N^{-1}\sum_ksNz_k\widetilde R_s(c_k)w_k^{-a}\),
with \(w_k=q^{2k+1}\).
This retains the middle Fourier slot and the odd simple node.
The ordinary-circle coefficients are
\(\beta_j=(-1)^j(a_j-a_{j+2})\), \(a_N=a_{N+1}=0\); hence
\[
 \sum_{j<N}|\beta_j(s)|\le
       2N(1+|s|/2)e^{(\pi N/4)(-\Im s)_+}.
 \tag{12}
\]
In particular the normalized values are contractive for \(\Im s\ge0\).
Applying this actual polynomial expansion before contracting the
physical source error gives
\[
 |\widehat Z_N-\widehat Z_N^{\rm cor}|
 \le\prod_j2N(1+|s_j|/2)
 \exp N\left\{F_0-\gamma_*+{\pi\over4}
                                      \sum_j(-\Im s_j)_+\right\}.
 \tag{13}
\]
The full-minus-core and macroscopic-color errors were estimated
before even folding. No alias is declared even here.

## 3. Exact charges and uniform control of their infinite tail

The finite midpoint calculation of [F,O] extends to every complex
\(s\), using (10). In one register put
\(U_{N,s}(z)=e^{\pi i sNz^2}\sinh(2\pi iz)\mathcal F_N(z)\).
Exactly,
\(U_{N,s}(\pm1/2)=0\) and
\(U_{N,s}'(1/2)=U_{N,s}'(-1/2)\).
This uses equal endpoint chirps and the periodic Fourier polynomial;
the Gaussian representative itself is not made periodic.
Three integrations by parts give locally uniform absolute charge
convergence in \(s\) for each fixed \(N\), followed by
\[
 \begin{split}
 \widehat Z_N^{\rm cor}(s)
 ={}&(-1)^{bd}(-i)^b
 \sum_{\ell\in(\mathbb Z\setminus\{0\})^b}
       \Bigl(\prod_j\ell_j\Bigr)(-1)^{(N+1)\sum_j\ell_j}\\
 &\quad\cdot\int_{[-1/2,1/2]^b}\mathcal F_N(z)
       \prod_j\sin(2\pi z_j)
       e^{N\{\pi i\sum_js_jz_j^2+2\pi i\ell\cdot z\}}\,dz .
 \end{split}\tag{14}
\]
The first normals and zero-deficit half weight are included. Reflection
of \((\ell_j,z_j)\) preserves each weighted term and its parity,
for every complex \(s\); all \(2^b\) unit-sign terms therefore add.

Fix a compact \(K\Subset\Omega_{L,\eta}\), using a slightly larger
compact buffer for every estimate. Write \(s_j=A_j+iV_j\).
In one positive charge coordinate, shift its whole interval upward
by a fixed \(0<\tau<1/2\), inside the source endpoint strip.
For \(H_i(z)=\sin(2\pi z)e^{\pi i s_iNz^2}
\mathcal F_N(z,z_{\ne i})\), its exact paired endpoint difference is
\[
 H_i(1/2+iv)-H_i(-1/2+iv)
 =2i\sinh(2\pi v)\sinh(\pi s_iNv)
   e^{\pi i s_iN(1/4-v^2)}
                      \mathcal F_N(1/2+iv,z_{\ne i}).
 \tag{15}
\]
For \(0\le v\le\tau\),
\[
 |\sinh(\pi s_iNv)|\le\pi|s_i|Nv e^{\pi|A_i|Nv},
 \qquad
 |e^{\pi i s_iN(1/4-v^2)}|\le e^{\pi\eta N/4}.
 \tag{16}
\]
Thus the quadratic endpoint zero survives. Three integrations by
parts in real spectators give \(\prod_{j\ne i}|\ell_j|^{-2}\).
Their chirps cost at most \(e^{\pi(b-1)\eta N/4}\); fixed
derivatives cost only powers of \(N\) on \(K\). The weighted vertical
bound is consequently at most
\[
 C_KN^C\ell_i\prod_{j\ne i}|\ell_j|^{-2}
 e^{N(F_0-\gamma_e+\pi b\eta/4)}
 \int_0^\tau v^2e^{-2\pi N(\ell_i-|A_i|/2)v}\,dv.
 \tag{17}
\]
For large enough \(\ell_i\) its sum converges by the inverse-cube
integral estimate. On the translated horizontal interval, the
Bernstein estimate of [O] instead bounds the rate by
\[
 F_0+o(1)+2\pi b\tau+\pi\eta/4
                  +\pi(V_i)_+\tau^2
                     -2\pi\tau(\ell_i-|A_i|/2),
 \tag{18}
\]
in addition to the spectator cost. Choose a fixed cutoff on \(K\)
larger than
\(\sup_K\{|A_i|/2+(V_i)_+\tau/2\}+D_0\), where \(D_0\) depends
only on the source strip and its desired gap. First choose \(D_0\)
large, then \(\eta\) small. The complete distant-charge tail has
rate at most \(F_0-\gamma_\infty\), with a positive source-dependent
gap. Reflect negative charges and sum over the distinguished
coordinate. Only a fixed finite set remains on \(K\).
No infinite series has been sharply cut on an inner contour, and no
individual endpoint current has been deleted.

## 4. Complex critical points and the simultaneous contour translation

Write \(\partial_j\Psi(z)=-2z_jB_j(z)\). Shrink the fixed disk so that
\(|B_j-g_j|\le g_j/8\) and \(-\Re\Psi''\ge cI\).
For nonnegative real charges with \(\ell_j/|s_j|\le2a_0\),
the critical equation and its exact imaginary part are
\[
 z_j=-{\ell_j\over s_j+iB_j(z)/\pi},\qquad
 \Im z_j={\ell_j(V_j+\Re B_j(z)/\pi)
                              \over|s_j+iB_j(z)/\pi|^2}.
 \tag{19}
\]
Choose \(a_0\) small, \(L\) large and
\(\eta<\min\{c/(4\pi),\min_jg_j/(4\pi),1\}\). The fixed-point map has derivative
\(O(a_0/L)\), remains in the fixed disk and is a contraction.
Its unit-charge branch is globally holomorphic on (4).
For positive charges \(z=p+iy\), every \(y_j>0\), and
\[
 {c'\ell_j\over|s_j|^2}\le y_j
       \le {C\ell_j(1+(V_j)_+)\over|s_j|^2},\qquad
 \Re\mathcal Q\ge cI-2\pi\eta I>0.
 \tag{20}
\]
Stationarity and integration successively in real charges give
\[
 \Re S_{\mathbf1}-\Re S_\ell
       \ge c'\sum_j{\ell_j^2-1\over|s_j|^2},\qquad
 0\le F_0-\Re S_{\mathbf1}\le C\sum_j|s_j|^{-1}.
 \tag{21}
\]
Thus every nonunit local charge has a positive uniform gap on \(K\).
Also \(z_j=O(|s_j|^{-1})\) at unit charge, which directly gives
the absolute anchor \(S(s)-F_0=O(\sum_j|s_j|^{-1})\).

An additional argument is needed for connecting faces when \(V_j\)
is large and positive: bounding all imaginary displacements by a
free rectangle would lose their cancellation. On a fixed real cube
\([-B,B]^b\) use the straight simultaneous translation
\(x\mapsto x+i\theta y\), \(0\le\theta\le1\).
Put \(f=\Psi+\pi i\sum_js_jz_j^2+2\pi i\ell\cdot z\), and
\[
 \mathscr H(\theta)=\max_{x\in[-B,B]^b}\Re f(x+i\theta y).
 \tag{22}
\]
Its horizontal Hessian is
\(A=\Re\Psi''-2\pi\operatorname{diag}(V_j)\), uniformly negative.
Its interior maximizer exists by a separate contraction. Put
\(\mathsf D=2\operatorname{diag}(g_j+\pi V_j)\) and
\(\rho_\theta(x)=\Re\Psi'(x+i\theta y)+2\operatorname{diag}(g_j)x\).
Reality and separate evenness give \(\rho_\theta(0)=0\).
Shrinking the source disk makes
\(\|\mathsf D^{-1}D\rho_\theta\|_\infty<1/4\).
The exact zero-gradient map is
\(x\mapsto\mathsf D^{-1}\{\rho_\theta(x)-2\pi\theta(A_jy_j)_j\}\).
Its driving term is \(O(a_0)\); it maps a fixed \(O(a_0)\) cube
strictly into itself and contracts. Thus its fixed point obeys
\[
 \|x_\theta\|_\infty
    \le C\max_j{|A_j|y_j\over1+(V_j)_+}
    \le Ca_0 < B/2 .
 \tag{23}
\]
Choose \(a_0\) so that this cube lies inside \((-B,B)^b\).
Strict concavity makes this point the unique maximizer on the whole
cube. For \(\mathcal B=\Im f''\), the envelope rule yields
\[
 \mathscr H''(\theta)
   =-y^{\mathsf T}Ay
       -y^{\mathsf T}\mathcal B A^{-1}\mathcal B y\ge0 .
 \tag{24}
\]
At \(\theta=1\), \(x_\theta=p\), hence \(\mathscr H'(1)=0\).
At zero, strict real concavity gives \(\mathscr H(0)=F_0\).
Consequently \(\mathscr H(\theta)\le F_0\).
Every swept side face has one real coordinate fixed at \(\pm B\);
its distance from \(x_\theta\) gives a fixed strict loss below \(F_0\).
Stokes' theorem for this single homotopy therefore supplies the
translated cube with coefficient one and only lower connecting
faces. This assertion is for the simultaneous path, not an
unproved bound on every mixed imaginary displacement.

On the translated cube the real phase has its unique maximum at
\(z_\ell\), with uniformly negative real Hessian. Insert (3) and
rescale by \(N^{-1/2}\). The accretive complex Gaussian, vanishing
odd first corrections, and the uniform holomorphic source error
give a relative \(O_K(N^{-1})\) local expansion. All sine factors
are nonzero because their arguments are in the small upper disk.

## 5. Bounded nonlocal charges, full source, and the logarithm

For any remaining bounded charge that is not local, reflect one
coordinate positive with \(\ell_i/|s_i|>a_0\).
Use an inner real cube of radius \(0<B_0<a_0/4\) and translate
only that coordinate by \(iB_0/|s_i|\). Absorb the real spectator
negative-collar costs into a smaller fixed \(c>0\).
For \(0\le v\le B_0/|s_i|\), the real phase is then bounded by
\[
 F_0-c|x|^2+Cv^2
 -2\pi(\ell_i-|A_i|B_0)v-\pi V_i x_i^2+\pi V_i v^2 .
 \tag{25}
\]
The negative part of \(V_i\) costs at most \(\pi\eta x_i^2\),
absorbed by the source Hessian. Its positive part satisfies
\((V_i)_+v^2\le B_0^2/|s_i|\), so large \(L\) controls the
remaining term. The horizontal and connecting vertical faces have
a fixed gap below \(F_0\), as in [O]. Outside this inner cube use
the shared source gap and the real chirp cost at most
\(\pi b\eta/4\). The local estimates hold through ratios \(2a_0\),
whereas this nonlocal estimate already applies above \(a_0\).
These margins overlap, so a finite cover of \(K\) may fix the
finite charge classifications.

Choose \(\eta\) below the source, endpoint and Hessian margins,
and \(L\) large enough that the unit drop in (21) is less than
one quarter of all fixed tail, side and nonlocal gaps, including
\(\gamma_*\). Shrink \(\eta\) further if necessary so that
\(\pi b\eta/4\) preserves these gaps in (13), (17) and (25).
The only leading terms of (14) are the unit-sign charges.
Their equality gives \(D(s)\) in (6), since the exact two parity
factors multiply as \((-1)^{bd+(N+1)b}=1\).
The level power is \(3/2+b/2-b/2=3/2\).
Equation (13) lies exponentially below the same action, proving
(7)--(8) for the entire original source.

The normalized error is holomorphic on (4). Run all estimates on
a compact buffer of \(K\); Cauchy's formula proves every derivative
in (8), not an analytic continuation of pointwise real estimates.
For large \(N\), \(|E_N|<1/2\) on that buffer, so its principal
\(\log(1+E_N)\) is holomorphic there.
There is an explicit global logarithm of \(D\): \(B\) is a unit
on the fixed small disk, every \(z_j\) is in the upper half-disk,
and \(\sin(2\pi z_j)/(2\pi z_j)\) is a unit near zero.
Use those logarithms and the canonical accretive log determinant
of \(\mathcal Q\). This proves (9). Its last identity is the
envelope rule at the critical point. The domain (4) is connected:
each coordinate can be moved outside a larger circle and then
above it, without entering the removed disk or lower half-plane.

## 6. Coverage and scope

[R] gives the entire Hermite family, [E] the integer endpoint and
Fourier analysis, and [C] long integer powers with a complex boundary
phase. [A] continues formal geometric coefficients but leaves its
actual normalized-source upper estimate open. Here the actual
complex-power source is estimated on one connected chamber,
including all finite-source errors, endpoints, aliases and fixed jets.

At allowed integers restore the original writhe and peripheral
conventions of [M]; no factor has been reset. There is no claimed
topological interpretation for noninteger points. Although (4)
connects the long real signs through large positive imaginary powers,
it does not reach arbitrary fixed short real powers. The chamber
does not identify a geometric cycle after such a short partial filling,
and gives no new finite-exception or knot-volume theorem.

## Complete chosen texts

All nine complete matching texts were read; their pins were renewed
after the reads. The new complex estimates are proved above.

| Label | Complete text | Lines | SHA-256 |
| --- | --- | ---: | --- |
| M | [Strict original construction](../papers/conway-asymptotics/main.tex) | 135 | 98d34dcfe31f89e5c7c7f904da93f375386e9a94a113972fb0a8e78e08b0ca7b |
| F | [Full powers and filling](../papers/conway-asymptotics/filling.tex) | 237 | 215c5d27ef5c0d1e8abbeaae379ef6bdfbbb63ae92a654722b222f685b0c6036 |
| P | [Exact Fourier source and gap](../papers/conway-asymptotics/packet.tex) | 207 | d56dea193c14c60d08c8c9305716102388100e5a9848fe03f1442db344740dff |
| W | [Strict pure source](../papers/conway-asymptotics/pure-window.tex) | 177 | 2832ccd4ad37a43f9f63c28124832d21c7242401fd0906f0b9f35c07829a45b8 |
| O | [Whole filling sum](../papers/oscillatory-fillings/main.tex) | 830 | 275d76a8e12d963c6a4fc45bb828e0b7742761c94e4242272f15c64b56f3f203 |
| R | [Exact real-power source](research_real_power_source_transport.md) | 394 | 7dac43d1a5fac6b4602a3aab12bfe977cb42a61b36d40a2fb8517e29566df8ea |
| E | [Actual Fourier endpoints](actual_filling_source_fourier_endpoint_gap.md) | 467 | 1f03f69212b1fee6dceb6315b9582acb56aa647e4893ee3483113eff142ad982 |
| A | [Formal coefficient continuation](research_positive_source_formal_continuation.md) | 429 | 288d2bbd2910ce43571129d9c18697a263897162842a7f7070ec4d29ca44a4ae |
| C | [Complex boundary phase](research_long_fillings_complex_boundary_phase.md) | 622 | bffa5dfe8da7268c65d5e96bf1b1cdfa0328b084af01b713ac00571b26835618 |

Only written mathematics, complete text reads and metadata operations
were used. No mathematical program, numerical test, build, git command,
prior-final edit or public-manuscript change was made.
