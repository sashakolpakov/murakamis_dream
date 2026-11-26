# Reflection, angular deck currents, and integer charge coupons

Private written proof, 16 November 2026.

These identities fix the original orientations at angular faces of the
restored wire source. Reflection gives a doubled spectral chain, whereas
a full angular deck turn has a signed Gaussian current. Neither operation
converts the original wire residue into its edge-deleting extreme
coefficient. All statements retain physical first normals, the odd
simple node, and the prescribed closing functional.

## 1. Reflection preserves the full forms and adds their images

Fix \(N\ge2\), \(D=N-1\), \(\eta=(-1)^D\), and
\[
 P_N(z)=2T_N(z/2)+2,\quad z(t)=-2\cos t,\quad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2},\quad
 C_{N,n}=e^{\pi i nD^2/(4N)},\quad \kappa=C_{N,1}^2.
 \tag{1}
\]
Here \(a_N=\pi-\pi/(2N)\), \(c_j=2\cos((2j+1)\pi/N)\), and
\(\phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f\).
The original Newton polynomials are
\(e_j(z)=S_j^{-2}\prod_{\ell<j}(c_\ell-z)\), with
\(S_j=\prod_{\ell=1}^j2\sin(\pi\ell/N)\) and empty products one.
Thus \(K_T(z,z')=\sum_{j=0}^D e_j(z)e_j(z')\).
Use the exact joint forms of the pinned lens theorem, with their original
prefactor \(N^{|E|}\prod_v[-N^2C_{N,n_v}/(\pi i)]\). At traced
vertices they contain
\[
 \sin t_v\,W_N(t_v)e^{i n_vNt_v^2/(4\pi)}
                \cos(N(1-c_v)t_v)\,dt_v.
 \tag{2}
\]
Free endpoints remain ordinary cardinal polynomials. A reflection
\(\mathcal R_v:t_v\mapsto-t_v\) keeps all other coordinates fixed.
On a common reflected admissible chart,
\[
 \mathcal R_v^*\Omega_{\rm fac}=\Omega_{\rm fac},\qquad
 \mathcal R_v^*\Omega_{\rm car}=\Omega_{\rm car}.
 \tag{3}
\]
Indeed both halfwire representatives and every factor in (2) except
\(\sin t_v\) are even. The signs from that sine and \(dt_v\) cancel.
This applies to the actual compiled spectral spectators, whose angular
dependence is also even.

The same identity holds for the exact relative primitive and seam currents:
\[
 \Omega_{\rm fac}-\Omega_{\rm car}=d\Theta,\qquad
 J_e=(\tau_e^*-1)\Theta,\qquad
 \mathcal R_v^*\Theta=\Theta,\quad \mathcal R_v^*J_e=J_e,
 \tag{4}
\]
where \(\tau_e:x_e\mapsto x_e+1\). To check this directly, the coefficient
\(Q_v\) of \(\Theta_v\) is the primitive of an odd function of \(t_v\)
from \(-a_N\), with values zero at both \(\pm a_N\). It is therefore
even in \(t_v\), whose differential is omitted. For \(w\ne v\), the
coefficient of \(\Theta_w\) is odd in \(t_v\), and its wedge contains
\(dt_v\). Those two signs again cancel. Wire translations commute
with reflection. This proof uses the full primitive paths and the
admissible charts of the source theorem; meromorphic continuation alone
does not supply a chart.

If \(\Gamma\) is the lower arc from \(-a_N\) to \(a_N\), then
\(\mathcal R\Gamma\) is the upper arc from \(a_N\) to \(-a_N\).
The sum is the positively oriented full lens. In particular
\[
 \int_{\mathcal R\Gamma}\omega=\int_\Gamma\omega,\qquad
 z_*(\mathcal R\Gamma)=z_*\Gamma
 \tag{5}
\]
for the invariant source form. The spectral chains and their boundaries
coincide with induced orientation: they add, rather than cancel. The
factor \(1/2\) in the logarithmic double-cover trace is exactly the
corresponding normalization, including the odd ramified node.

For comparison only, the classical reflection changes the corresponding
primitive row from \((u_v,c_v)\) to \((-u_v,-c_v)\). Formula (3) retains
the same exact cosine coupon; it does not replace it by the polynomial
coupon of charge \(-c_v\).

## 2. Partial deck faces and complete residue windows

For deck transport first keep every spectator, including the charge
coupon, as its original polynomial in \(z\). For
\(\epsilon\in\{1,-1\}\), put
\(\mathcal D_\epsilon:t\mapsto t-2\pi\epsilon\). The cardinal
angular source form then obeys the exact pointwise multiplier
\[
 \mathcal D_\epsilon^*\omega=M_{n,\epsilon}(t)\omega,\qquad
 M_{n,\epsilon}(t)=(-1)^{nN}e^{-inN\epsilon t}.
 \tag{6}
\]
Here \(n\) is a signed integer. All polynomial spectators, \(W_N\),
and \(\sin t\,dt\) are periodic; (6) follows by subtracting the two
Gaussian squares. On the actual face \(t=\epsilon\pi+ih\),
\[
                         M_{n,\epsilon}(t)=e^{nN\epsilon h}.
 \tag{7}
\]
Thus, when the oriented face pair is
\(\mathcal D_\epsilon F-F\), its defect is
\(\int_F(M_{n,\epsilon}-1)\omega\). Reversing that convention reverses
the sign. This is not a pointwise parity multiplier.

If the unwrapped cosine in (2) is retained instead of its polynomial
representative, its additive paired-face factor is instead
\[
 M_{n,\epsilon}(t)
       \cos\!\bigl(N(1-c)(t-2\pi\epsilon)\bigr)
                  -\cos\!\bigl(N(1-c)t\bigr).
 \tag{8}
\]
No division by the cosine is used. Equality of physical Hermite data
does not identify these partial-face continuations. At \(c=1\), (8)
reduces to \(M_{n,\epsilon}-1\).

The complete-window identity is different. Write
\[
 y=i(\pi-t),\quad \hbar=2\pi i/N,\quad
 G_n(y)=e^{-\pi i nD^2/(4N)}
           e^{\,n(y-\pi i)^2/(2\hbar)}.
 \tag{9}
\]
Let \(\mathcal C\) be the sum of positively oriented small circles
around \(y_j=(2j+1)\pi i/N\), \(0\le j<N\). For any original
polynomial spectator \(A\), define
\[
 I_n^{[r]}(A)=\frac{\eta N^2}{4\pi i}
   \int_{\mathcal C+2\pi i r}
       \frac{G_n(y)A(e^y+e^{-y})(e^y-e^{-y})}
            {P_N(e^y+e^{-y})}\,dy,\qquad r\in\mathbb Z .
 \tag{10}
\]
The pinned residue identity is \(I_n^{[0]}(A)=\phi_N(f_nA)\),
where \(R=\kappa r_N\) and \(f_n\) represents \(r_N^n\).
All full jets and the simple odd node are included.

**Proposition 1.** For every integer \(r\),
\[
 I_n^{[r]}(A)=(-1)^{nr}I_n^{[0]}(A).
 \tag{11}
\]
Consequently the single-window difference is
\((1-(-1)^n)I_n^{[0]}(A)\), and the sum of the two opposite
full-turn differences is
\[
             2(1-(-1)^n)I_n^{[0]}(A).
 \tag{12}
\]

**Proof.** Pull (10) back to \(\mathcal C\). Its only change is
\[
 G_n(y+2\pi i r)/G_n(y)
   =e^{nNr y}e^{\pi i nN r(r-1)}=e^{nNr y}.
 \tag{13}
\]
The reflection \(y\mapsto2\pi i-y\) preserves \(\mathcal C\) with
its induced orientations, the Gaussian, and the residue differential.
It replaces this multiplier by \(e^{-nNr y}\). Averaging the two
expressions gives \(T_{nrN}(z/2)\). In the full quotient,
\[
 T_{nrN}(z/2)=T_{nr}(T_N(z/2))\equiv(-1)^{nr}\pmod{P_N}.
 \tag{14}
\]
This is an ideal identity, not just equality of reduced values.
It includes first normals at every double root and the value at the
odd simple root. Equations (11)--(12) follow. \(\square\)

The physical source has the unchanged additional factor \(\kappa^n\).
The proof works coefficientwise with other original polynomial
variables retained, so complete turns at several vertices give
\((-1)^{\sum_v n_vr_v}\). It gives no replacement of the partial-face
factor (7) by that sign.

## 3. Wire residue and angular transport commute

For a direct paired wire use the exact cardinal expansion
\[
 F_N(w;z,z')=\widetilde B_N(x,z)\widetilde B_N(x,z')
       =\sum_{m=-D}^{D}A_m(z,z')w^{-m},\qquad w=e^{-2\pi ix}.
 \tag{15}
\]
For \(\sigma\in\{1,-1\}\), the adopted wire theorem gives
\[
 A_0=K_T/N,\quad
 A_{\sigma D}=\kappa^{-2\sigma}R^\sigma\otimes R^\sigma/N^2,
 \qquad
 F_N\,dx=-\frac{K_T}{2\pi iN}\frac{dw}{w}+d_wV_N,
 \quad
 V_N=\sum_{m\ne0}\frac{A_mw^{-m}}{2\pi im}.
 \tag{16}
\]
The original increasing \(x\)-period is clockwise in \(w\), giving
\(+K_T/N\). The usual wire factor \(N\) restores \(K_T\).
Free endpoints in (16) mean the ordinary polynomial representatives;
they are not silently traced.

Reflection, partial angular deck multiplication, and complete-window
transport each act coefficientwise on (15). None changes the wire
frequency \(m\). Thus angular transport commutes with extracting
\(A_0\), and \(d_wV_N\) has zero wire residue before and after it.
After multiplication by the remaining angular
forms, \(V_N\) is reflection invariant by exactly the sine/differential
parity in (3).

In particular the partial joint defect retains \(K_T\) times (6)--(8).
On a complete angular window the symmetric current insertion, with
physical crossing normalization restored, is exactly
\[
                         2(1-(-1)^n)R^nK_T
 \tag{17}
\]
inside the original spectator and closing contraction. For odd \(n\)
this is four times that original insertion; its scalar contraction
may still vanish. The parity change \(n\mapsto n+\sigma\) belongs
to the extreme coefficient in (16), not to its residue.

For factorial representatives this distinction persists through
\(\Omega_{\rm fac}-\Omega_{\rm car}=d\Theta\). The retained primitives
are \(V_N\) and \(\Theta\), with their actual seam defects. On a partial
angular patch or incomplete wire arc their boundary integrals need
not vanish. No global factorial deck chart or cancellation of those
terms is asserted here.

## 4. Exact integer charge shifts

Let \(C_c\) denote the full Hermite class of
\(\cos(N(1-c)t)\), for any complex \(c\). Define
\[
 D_c=\bigl[\eta^{-1}\sin(Nt)\sin(N(1-c)t)\bigr].
 \tag{18}
\]
The product is even in \(t\), so it defines the required holomorphic
spectral germ at the odd ramified point. At every double node
\(\tau_j=\pi(D-2j)/N\),
\[
 D_c(c_j)=0,\qquad
 D_c'(c_j)=\frac{N\sin(N(1-c)\tau_j)}{2\sin\tau_j}.
 \tag{19}
\]
Its value at the odd simple node is zero. Thus \(D_c\) lies in the
square-zero radical of this one-vertex algebra; in particular
\(D_cD_d=0\) for any \(c,d\).

**Proposition 2.** At every level, for each integer \(k\),
\[
                    C_{c+k}=\eta^k(C_c+kD_c).
 \tag{20}
\]

**Proof.** At a physical angle, \(N\tau_j=\pi D-2\pi j\).
The values of the two cosines differ by \(\eta^k\).
Differentiating them in \(z\), with \(dz/dt=2\sin t\), gives
precisely the additional term \(kD_c'\) in (19).
At the odd simple node both cosine values are one and \(\eta=1\).
These are all prescribed jets, including at \(N=2\), proving (20).
\(\square\)

In particular
\[
               D_1=0,\qquad C_{1+k}=\eta^k,\qquad
               C_{-c}=C_c+2D_c.
 \tag{21}
\]
The last equality also uses \(C_{2-c}=C_c\) and \(D_{2-c}=-D_c\).
It explains why reflection of a selected classical charge channel
cannot silently replace the fixed exact coupon by \(C_{-c}\).

At a classified \(q_e=\sigma i\) escape, the original lifted charge
integers satisfy \(k_v+k_w\) odd, with exactly one nonzero:
it is \(k=\sigma\epsilon\) at the endpoint \(s=\epsilon\pi\).
If both endpoints are traced, the charge-adjusted extreme coefficient,
including the original wire factor \(N\), is therefore exactly
\[
 \frac{\eta\kappa^{-2\sigma}}N R_v^\sigma R_w^\sigma
       (C_{c_v}+k_vD_{c_v})(C_{c_w}+k_wD_{c_w}).
 \tag{22}
\]
All other vertex powers and spectators multiply this expression.
At unit charges only its scalar \(\eta\) remains from the charge
change. Formula (22) is still an extreme-mode coefficient; it is
not the \(K_T\) residue. With a free endpoint one instead keeps
its ordinary extreme polynomial and imposes no charge row there.

The exact bookkeeping consequently supplies neither a joint
face cancellation nor an action bound. A further original-chain
identity or estimate must handle the retained kernel current and
the \(V_N,\Theta\) sides. No geometric cycle coefficient or filling
volume asymptotic is inferred.

## Pinned direct sources

All complete source texts and directly used implications were read
at these versions; unchanged complete reads in this review sequence
are retained.

* Joint factorial lenses:
  research_joint_factorial_lens_relative_source.md,
  SHA256 a14ca148bd55b36b1eea9de8be8a63025532c3bbbb928482b0d7cb8edae56e54.
  Exact form, charge coupon, full-normal trace, and relative primitive.
* Moving wire seams:
  research_moving_wire_seam_source_descent.md,
  SHA256 2b632735243fc450e2ce0f276f339c9fad0b5524724364b83f15690b4896f33d.
  Primitive parities, admissible domains, orientations, and seam currents.
* Gaussian logarithmic transport:
  research_gaussian_logarithmic_contour_transport.md,
  SHA256 e7d62f6630dec31ac6c87f75baf1ff707ed7af9221ac4c5199549cdd4ee7f36f.
  Full residue normalization and the existing symmetric full-turn
  current (21a). Proposition 1 records its individual-window refinement.
* Stationary wire escape:
  research_stationary_wire_escape_current.md,
  SHA256 03f902ea70818cf8432dd3d947822b49d1f762487552b20dac7e431b8222aa4e.
  Exact Laurent coefficients, primitive, crossing carriers, and the
  constrained limiting charge integers used in (22).

Only written proofs, source-text reads, and hashes were used.
No mathematical program, numerical evaluation, test or compilation
was run. Other authors' notes and frozen/public documents were unchanged.
