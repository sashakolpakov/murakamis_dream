# Finite charge polarizations retaining the original Hermite trace

Private written proof, 16 November 2026.

The canonical positive physical angles define a square root of the
full-Hermite squared-angle class. Its two algebra exponentials split
the original cosine coupon exactly. Each polarized family has the
same signed heat evolution and recovers the original source at unit
charge. Its charge reflection exchanges the two families instead of
forcing either family to have zero first derivative there.

This is a finite-source construction. A polarized initializer is not
inferred from the already proved cosine initializer. The earlier
one-sided angular representative changes representatives modulo the
angular Hermite ideal; the polarization here instead changes the
charge coupon in the original spectral algebra. These are different
operations.

## 1. The positive-angle class and its exponentials

Use the original data of the entire charged-source heat theorem:
\[
 D=N-1,\qquad \eta=(-1)^D,\qquad N\ge2,\qquad
 \mathcal A_N=\mathbb C[z]/(P_N(z)),\qquad
 P_N(z)=2T_N(z/2)+2,
\]
\[
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f.
 \tag{1}
\]
The distinct double nodes have positive angular lifts
\[
 c_a=-2\cos\tau_a,
 \qquad \tau_a=\frac{\pi(D-2a)}N>0,
 \qquad 0\le a<\lfloor N/2\rfloor.
 \tag{2}
\]
At odd levels the remaining node \(-2\) is simple. Define the unique
class \(L_N\in\mathcal A_N\) by
\[
 L_N(c_a)=\tau_a,\qquad
 L_N'(c_a)=\frac1{2\sin\tau_a},\qquad
 L_N(-2)=0\quad(N\text{ odd}).
 \tag{3}
\]
This is a choice of full finite jets, not an assertion that a single
inverse cosine is holomorphic across \(-2\). If \(\mathscr T_N\) is
the squared-angle class in the heat theorem, then
\[
                         L_N^2=\mathscr T_N.
 \tag{4}
\]
Indeed its double-node values are \(\tau_a^2\), its derivatives are
\(\tau_a/\sin\tau_a\), and its odd simple value is zero. These are
all the defining data of \(\mathscr T_N\).

For \(\sigma\in\{+1,-1\}\), put
\[
 Q_{N,\sigma}(\chi)
       =\exp_{\mathcal A_N}\bigl(\sigma iN(1-\chi)L_N\bigr).
 \tag{5}
\]
Its complete data are
\[
 \begin{split}
 Q_{N,\sigma}(\chi)(c_a)
     &=e^{\sigma iN(1-\chi)\tau_a},\\
 Q_{N,\sigma}(\chi)'(c_a)
     &=\frac{\sigma iN(1-\chi)}{2\sin\tau_a}
                         e^{\sigma iN(1-\chi)\tau_a},
 \end{split}
 \qquad Q_{N,\sigma}(\chi)(-2)=1\quad(N\text{ odd}).
 \tag{6}
\]
Thus all coefficients are entire in \(\chi\), and each coupon is an
algebra unit at every finite charge. The original entire cosine
coupon \(\mathcal C_{N,\chi}\) satisfies the exact identities
\[
 \frac{Q_{N,+}(\chi)+Q_{N,-}(\chi)}2=\mathcal C_{N,\chi},
 \qquad Q_{N,\sigma}(1)=1,
 \qquad Q_{N,\sigma}(2-\chi)=Q_{N,-\sigma}(\chi).
 \tag{7}
\]
The last reflection is a reflection of the charge. Each polynomial
\(Q_{N,\sigma}(-2\cos t)\) is individually even in \(t\); angular
reflection does not exchange the two fixed spectral classes.

Differentiation in charge gives, in the full algebra,
\[
 \partial_\chi Q_{N,\sigma}
       =-\sigma iN L_N Q_{N,\sigma},\qquad
 \partial_\chi^2 Q_{N,\sigma}
       =-N^2\mathscr T_NQ_{N,\sigma}.
 \tag{8}
\]
In particular (8) keeps the first normals, rather than just the
semisimple values. At \(\chi=0\) the values in (6) are \(\eta\),
but the double-node normals are generally nonzero. The polarized
zero-charge coupon is therefore not silently identified with
\(\eta\,1\).

## 2. Faithful one-sided charge observations and heat transport

Write \(y=1-\chi\), \(\lambda_a=N\tau_a=\pi(D-2a)\), and let
\[
 \mathcal E_{N,\sigma}
   =\operatorname{span}\{e^{\sigma i\lambda_a y},
                            y e^{\sigma i\lambda_a y}\}_a
       +\operatorname{span}\{1\}\quad(N\text{ odd}),
 \tag{9}
\]
where the last summand is absent at even levels. Then
\[
 f\longmapsto\phi_N(fQ_{N,\sigma}(\chi))
 \quad\hbox{is an isomorphism}\quad
 \mathcal A_N\longrightarrow\mathcal E_{N,\sigma}.
 \tag{10}
\]
To see this directly, the original trace formula gives
\[
 \phi_N(fQ_{N,\sigma})
 =\sum_a\{A_a(f)+\sigma i B_a(f)y\}
                        e^{\sigma i\lambda_a y}
        +\mathbf1_{N\text{ odd}}f(-2),
 \tag{11}
\]
\[
 A_a(f)=\eta\{4\sin^2\tau_a f'(c_a)-c_af(c_a)\},
 \qquad B_a(f)=2\eta N\sin\tau_a f(c_a).
 \tag{12}
\]
The distinct nonzero frequencies and their first polynomial factors
are linearly independent, as is the optional constant. The coefficient
of \(y\) first recovers \(f(c_a)\), and the constant at that frequency
then recovers \(f'(c_a)\). Thus the dimension is exactly \(N\).

Let \(F_N\) be any original compiled numerator, with all kernels,
spectators and ordinary free boundaries retained. Distinct crossing
positions remain in their distinct contracted algebra copies. Define
\[
 Z_{N,\boldsymbol\sigma}(\mathbf n,\boldsymbol\chi)
 =\phi_N^{\otimes m}\!\left[
 F_N\prod_v R_{n_v}Q_{N,\sigma_v}(\chi_v)\right],
 \qquad
 \widetilde Z_{N,\boldsymbol\sigma}
 =\left(\prod_v C_{N,n_v}^{-1}\right)Z_{N,\boldsymbol\sigma},
 \tag{13}
\]
\[
 C_{N,n}=e^{\pi i nD^2/(4N)},\qquad
 R_n=C_{N,n}\exp_{\mathcal A_N}
                         \left(\frac{inN\mathscr T_N}{4\pi}\right).
 \tag{14}
\]
For arbitrary fixed signed real powers, and also as entire identities
in the powers,
\[
 \partial_{n_v}\widetilde Z_{N,\boldsymbol\sigma}
    =-\frac{i}{4\pi N}\partial_{\chi_v}^2
                              \widetilde Z_{N,\boldsymbol\sigma}.
 \tag{15}
\]
This follows from (8) and (14) inside the original trace. The
constant-coefficient equations preserve (9), so their solution is
unique in the tensor product of those finite spaces.

For a nonzero real step \(\delta\), set
\(v_\delta=e^{-i\operatorname{sgn}(\delta)\pi/4}\). The exact solution
in that coordinate is
\[
 \widetilde Z_{N,\boldsymbol\sigma}
             (\mathbf n+\delta\mathbf e_v,\boldsymbol\chi)
 =\sqrt{\frac N{|\delta|}}
   \int_{\mathbb R}e^{-\pi Nr^2/|\delta|}
       \widetilde Z_{N,\boldsymbol\sigma}
           (\mathbf n,\boldsymbol\chi+v_\delta r\mathbf e_v)\,dr.
 \tag{16}
\]
The Gaussian computation on \(e^{\lambda\chi}\) and its
\(\lambda\)-derivative proves (16), including every normal block.
The corresponding oriented charge line may be translated by any
finite complex amount, exactly as in the original heat theorem.
The Gaussian beats the linear exponential type of (9), so all these
integrals converge absolutely. Tensorization and ordinary
free-boundary derivatives commute with the identities.

For the fixed same-index graph sources covered by the local heat
theorem, the same physical-data argument gives
\[
 |\widetilde Z_{N,\boldsymbol\sigma}(\mathbf n,\boldsymbol\chi)|
 \le A N^p\prod_v(1+|\chi_v|)
       \exp N\left(C+\pi\sum_v|\Im\chi_v|\right).
 \tag{17}
\]
Here powers range over a bounded real box and free boundaries over
a fixed compact set. Indeed the values in (6) have modulus at most
\(e^{\pi D|\Im\chi|}\); their normals add only a polynomial factor,
since the smallest nonzero physical sine is bounded below by a
constant times \(N^{-1}\). The original kernel and mixed-normal
envelopes are otherwise unchanged. No filled-action estimate is
substituted for the constant \(C\).

Consequently the proved local heat estimate applies to (13) whenever
an actual uniform holomorphic nonzero initializer for this polarized
source is supplied. Equations (15)--(17) alone do not supply it.

## 3. Exact endpoint recovery and the Fourier projection

The symmetrization and endpoint recovery are literal source identities:
\[
 Z_N(\mathbf n,\boldsymbol\chi)
       =2^{-m}\sum_{\boldsymbol\sigma\in\{+,-\}^m}
                    Z_{N,\boldsymbol\sigma}(\mathbf n,\boldsymbol\chi),
 \qquad
 Z_{N,\boldsymbol\sigma}(\mathbf n,\mathbf1)
                      =Z_N(\mathbf n,\mathbf1).
 \tag{18}
\]
Reflecting one charge exchanges the corresponding signs. If a
polarized source has a uniquely specified holomorphic asymptotic
branch \(e^{NS_+(\chi)}a_+(\chi)\), its reflected branch is marked by
\(S_-(\chi)=S_+(2-\chi)\), \(a_-(\chi)=a_+(2-\chi)\). At unit
charge their actions and coefficients agree with those marks. The
factor \(1/2\) in their average then preserves the coefficient; it
does not create cancellation. Integer \(2\pi i\) action shifts give
the same exponential at integer levels but must not be inserted
without their marks. This assertion presupposes the actual branch
expansion; it is not its existence proof.

Unlike the cosine family, an individual family (13) is not forced by
charge reflection to have zero first derivative at unit charge. From
(8) that derivative is exactly the original trace with insertion
\(-\sigma iN L_N\). Thus the elementary single-branch symmetry
obstruction is removed, while the prescribed endpoint scalar remains
the same.

There is an exact way to obtain (13) from the whole cosine charge
function. In one variable let \(\Pi_+\), \(\Pi_-\), \(\Pi_0\) retain
respectively its generalized Fourier frequencies \(+\lambda_a\),
\(-\lambda_a\), and zero as a function of \(y=1-\chi\). Then
\[
 \phi_N(fQ_{N,\sigma})
       =(2\Pi_\sigma+\Pi_0)\phi_N(f\mathcal C_{N,\chi}).
 \tag{19}
\]
This follows by expanding the sine and cosine, including their
linear-in-\(y\) normal factors. At odd levels the constant must be
retained once, not doubled. The analogous operators in distinct
charges commute.

Projection (19) is a projection of the whole charge function. It can
be encoded on its finite space by a differential polynomial whose
order grows with \(N\), or by a one-sided Fourier projection. It is
not a fixed-order differentiation of a local asymptotic expansion.
The existing cosine initializer therefore does not automatically
give a polarized initializer.

## 4. The correct angular realization

For one traced variable let \(A(t)\) be an even holomorphic spectator
on neighborhoods of all physical angular nodes. Keep the canonical
crossing representative and set
\[
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2},\qquad
 h_n(t)=\sin t\,A(t)e^{inNt^2/(4\pi)}.
 \tag{20}
\]
Let \(\gamma_+\) be the union of small positively oriented circles
around precisely the positive physical angles \(\tau_a\). Then
\[
 \phi_N(R_n[A]Q_{N,\sigma})
  =-\frac{N^2 C_{N,n}}{\pi i}
      \int_{\gamma_+}h_n(t)e^{\sigma iN(1-\chi)t}W_N(t)\,dt
       +\mathbf1_{N\text{ odd}}C_{N,n}A(0).
 \tag{21}
\]
Near a physical angle, \(W_N(t)\) has double principal part
\(-\eta/[N^2(t-\tau_a)^2]\) and no simple-pole term. Its residue
in (21) therefore gives twice \(\eta\) times the derivative of
\(h_n(t)e^{\sigma iN(1-\chi)t}\), exactly the double-node value
and normal in the original trace. The remaining odd simple term
is exactly the last term displayed. Equivalently it is obtained by
adding one half of a small full angular circle around zero. Its
residue uses only the constant term of the exponential; no spurious
spectral derivative is prescribed there.

When the spectator is holomorphic on a symmetric lens neighborhood,
a literal exponential on the full symmetric closed lens is different.
With the original angular double-cover factor \(1/2\), its reflected
positive and negative preimages average the two exponential jets.
It consequently gives \(\phi_N(R_n[A]\mathcal C_{N,\chi})\), not
(21). A literal exponential on only a lower open arc defines yet
another entire period. Its average with the opposite exponential is
the original lower-lens cosine period, and each agrees with that
period at \(\chi=1\), but it retains separate open-arc connector
data. Neither identification erases those connectors.

Formula (21) gives the concrete remaining initializer problem: the
positive-half-grid cycle, its central connector and its outer
connectors must be estimated with the entire original spectator and
all normals. A nonzero initializer on a fixed complex charge domain
would then activate (16) and the already proved quantitative local
heat theorem, with its actual domain and tail conditions. No such
new half-grid estimate, arbitrary-filling propagation, or geometric
cycle coefficient is asserted here.

## Direct sources and versions

All directly used source implications were read in full, with earlier
complete readbacks retained only at unchanged hashes. The complete
final proof above was reread before freezing.

- [Entire charged-source heat reduction](research_entire_charged_source_heat_reduction.md),
  `33213425be9cac699860a48b23830399c82cd89bea3140cc776274aafe115fba`:
  original trace, squared-angle class, crossings, finite charge space,
  exact Gaussian heat transform and compiled-source placement.
- [Local charged-source heat propagation](research_charged_source_local_heat_propagation.md),
  `a924922b515aecdedef0c3877d69f0e50da030b9a111220f712a3f6d1bdb926e`:
  full-normal global envelope and the conditional quantitative local
  propagation theorem, without importing its cosine initializer.
- [Joint factorial lens relative source](research_joint_factorial_lens_relative_source.md),
  `a14ca148bd55b36b1eea9de8be8a63025532c3bbbb928482b0d7cb8edae56e54`:
  physical angular grid, double-cover normalization, odd simple node
  and full lower-lens source placement.
- [One-sided Hermite projection](research_one_sided_hermite_projection.md),
  `efa82935ada9aa9e06dcbd5d20d5e05357859986896b0b73a93eb78a4bb81cf4`:
  prior angular-representative coverage, distinguished from the new
  spectral charge polarization.
