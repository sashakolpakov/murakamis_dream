# The odd-level half-charge observation and its normal defect

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The ordinary value interpolation at odd levels has a simple physical
endpoint in addition to its double roots. Its angular Cauchy kernel
is a sine kernel. The ramified angular pole at zero supplies exactly
the original simple-node contribution. With this term retained, the
same half-charge saddle as at even levels gives a nonzero observation
and a locally dominant normal defect at every positive internal pair.

This note uses the full distinct-node interpolation, not the different
weighted odd space on which a positive crossing form was proved.
The original trace's top-degree correction is retained in Section 3.

## 1. The full-node polynomial and exact angular contour

Let \(N=2m+1\ge3\). The distinct physical roots are
\[
 c_a=2\cos((2a+1)\pi/N),\qquad 0\le a\le m,
 \qquad c_m=-2.
 \tag{1}
\]
Write
\[
 \begin{split}
 Q_{\mathrm d}(w)&=U_m(w/2)-U_{m-1}(w/2),\\
 Q_{\mathrm o}(w)&=(w+2)Q_{\mathrm d}(w),\qquad
 P_N(w)=(w+2)Q_{\mathrm d}(w)^2,\\
 Q_{\mathrm o}(-2\cos z)&=4(-1)^m\sin(z/2)\sin(Nz/2).
 \end{split}
 \tag{2}
\]
Here \(U_{-1}=0\). These are monic polynomials in \(w\).
The last identity follows from the elementary sine formula for \(U_j\)
and holds as an entire identity in \(z\).

Let
\[
 \begin{split}
 \mathcal L_N(w)&=\sum_{j=0}^{m}e_j(w)e_j(-2)=K_N(w,-2),\\
 \tau_a&=\arccos(-c_a/2)=2\pi(m-a)/N,\qquad
 T_a=N\tau_a^2/(4\pi),\qquad F_a=\mathcal L_N(c_a),\\
 \sigma_a^{\mathrm o}&=\frac{N}{Q_{\mathrm o}'(c_a)},\qquad
 \mathcal O^{\mathrm o}_nF(w)
       =\sum_{a=0}^{m}
          \frac{\sigma_a^{\mathrm o}e^{inT_a}F_a}{w-c_a}.
 \end{split}
 \tag{3}
\]
The equality of the low and full complete-end kernels at odd levels
is the [exact simple-endpoint identity](research_last_physical_row_riccati.md).
For \(a<m\) the Chebyshev differential equation gives
\[
 (4-c_a^2)Q_{\mathrm o}'(c_a)^2=N^2(c_a+2),\qquad
 |\sigma_a^{\mathrm o}|=\sqrt{2-c_a}\le2.
 \tag{4}
\]
At the simple endpoint,
\[
 Q_{\mathrm o}'(-2)=Q_{\mathrm d}(-2)=(-1)^mN,\qquad
                         \sigma_m^{\mathrm o}=(-1)^m .
 \tag{5}
\]

For a real crossing time \(n\), set
\[
 h_{n,N}(w)=
 e^{inN\arccos(-w/2)^2/(4\pi)}\mathcal L_N(w).
 \tag{6}
\]
The squared inverse cosine is continued on
\(\mathbb C\setminus[2,\infty)\), holomorphically through \(w=-2\).
Let \(\mathcal I^{\mathrm o}_{n,N}\) be its ordinary value interpolant
of degree at most \(m\) at the nodes (1). Then
\[
 \mathcal O^{\mathrm o}_nF(w)
      =N\frac{\mathcal I^{\mathrm o}_{n,N}(w)}{Q_{\mathrm o}(w)},
 \qquad
 \mathscr D^{\mathrm o}_{n,N}(w)
      =\frac{h_{n,N}(w)-\mathcal I^{\mathrm o}_{n,N}(w)}
                   {Q_{\mathrm o}(w)}
 \tag{7}
\]
are exact identities. The normal defect is holomorphic through every
physical node.

Choose midpoint cuts \(T_N=(2k_N+1)\pi/N\) tending to \(\pi/2\).
Let \(\mathcal R_N\) be the positively oriented angular rectangle
with real ends \(\pm T_N\) and imaginary heights \(\pm H_0\).
For real \(w>2\), the retained physical observation is exactly
\[
 \frac{N}{4\pi i}\oint_{\partial\mathcal R_N}
 \frac{(-1)^m\cos(z/2)\,
             e^{inNz^2/(4\pi)}\mathcal L_N(-2\cos z)}
 {(w+2\cos z)\sin(Nz/2)}\,dz .
 \tag{8}
\]
It includes all nodes with \(\tau_a<T_N\), including \(\tau_m=0\).

Indeed (8) is the change of variables \(v=-2\cos z\) in
the Cauchy expression with denominator \(Q_{\mathrm o}(v)\).
Every nonzero positive angle has two preimages. At zero the
map is ramified, and
\[
 Q_{\mathrm o}(-2\cos z)=(-1)^mNz^2+O(z^4),\qquad
                          dv=(2z+O(z^3))\,dz .
\]
The integrand before multiplication by \(N/(4\pi i)\) therefore
has residue \(2(-1)^m h_{n,N}(-2)/(N(w+2))\).
The resulting term is exactly
\((-1)^m h_{n,N}(-2)/(w+2)\), as required by (5).
Thus neither an endpoint factor of two nor a physical source term
has been omitted.

## 2. The half-charge packet and the exterior residue

Use the notation of the
[even-level observation theorem](research_complete_source_pick_observation.md#5-a-nonzero-half-charge-observation):
\[
 \begin{split}
 nt_0+2i\operatorname{asinh}\tan(t_0/2)&=\pi,\qquad
 t_0=a_0-iH_0,\quad 0<a_0<\pi/3,\quad 0<H_0<2/5,\\
 S_n(z)&=\Psi(z)+inz^2/(4\pi)-iz/2,\qquad
 \mathcal S_n=S_n(t_0),\quad M_n=\Re\mathcal S_n,\\
 A_n&=\{\sec(t_0/2)-in\}/(2\pi).
 \end{split}
 \tag{9}
\]
Here \(n\ge3\) is fixed and real, and the square root of \(A_n\)
has positive real part. Define
\[
 b_n^{\mathrm o}(w)
   =\frac{\sqrt{2\pi}}{\pi}
      \frac{\cos(t_0/2)a_e(t_0,0)}
           {(w+2\cos t_0)\sqrt{A_n}} .
 \tag{10}
\]

**Theorem 1.** Uniformly for real \(w>2\), through odd levels,
\[
 \mathcal O^{\mathrm o}_nF(w)
   =(-1)^mN^{-1}b_n^{\mathrm o}(w)e^{N\mathcal S_n}
                                      (1+O(N^{-1})).
 \tag{11}
\]
The coefficient is nonzero and comparable in modulus to \(1/(w+1)\).
The same expansion holds locally in the crossing time and with fixed
holomorphic parameter derivatives, on smaller neighborhoods.

*Proof.* The angular integrand in (8) is odd, so its two horizontal
sides add after reflection. On the lower side,
\[
 \frac1{\sin(Nz/2)}
       =\frac{2i\,e^{-iNz/2}}{1-e^{-iNz}} .
\]
Thus its exact principal integral is
\[
 \frac{(-1)^mN}{\pi}
 \int_{-T_N-iH_0}^{T_N-iH_0}
 \frac{\cos(z/2)\mathcal L_N(-2\cos z)
              e^{inNz^2/(4\pi)-iNz/2}}
      {(w+2\cos z)(1-e^{-iNz})}\,dz .
 \tag{12}
\]
The denominator differs from one exponentially on this segment.
At a midpoint vertical side the sine denominator has modulus
\(\cosh(Nh/2)\); its reciprocal is at most \(2e^{-N|h|/2}\).
Consequently the horizontal and vertical upper exponents are
exactly the ones already proved in the even-level theorem.

For precision, \(\Re S_n(a-iH_0)\) is strictly concave for
\(|a|\le\pi/2\), with unique maximum at \(a_0\).
The lower right connector increases in height and is bounded
by its smaller horizontal endpoint value. The lower left
connector decreases in height and is bounded by \(\Psi(T_N)\).
The upper sides are their reflected copies.
All physical omitted values are at most the first omitted
complete-kernel value by the actual positive row recurrence.
Their rate is \(\Psi(\pi/2)\), and
\[
                    \Psi(\pi/2)<M_n-7/80.
 \tag{13}
\]
Their weights are bounded by (4), and
\((w-c_a)^{-1}\le N^2/(w+1)\). Thus every omitted part has a
fixed gap with a majorant integrable after squaring.
No off-grid estimate near the physical color \(2\) is substituted.

At \(t_0\), the original complete-edge packet is
\(\mathcal L_N(-2\cos z)=N^{-3/2}a_e(z,0)e^{N\Psi(z)}
(1+O(N^{-1}))\). The Gaussian integral in (12) contributes
\(\sqrt{2\pi/N}/\sqrt{A_n}\), proving (10)–(11).
The new factor \(\cos(t_0/2)\) is nonzero.
All rational amplitudes, after multiplication by \(w+1\), and
their derivatives are uniformly bounded with nonzero leading
value for \(w>2\). Strict gaps persist in a small complex
time neighborhood; Cauchy's formula proves the normalized
derivative statements. \(\square\)

Let \(\mathcal J^{\mathrm o}_{n,N}(w)\) denote (8), and
\(\mathcal T^{\mathrm o}_{n,N}(w)\) the omitted physical sum.
For a complex color \(w=-2\cos(a-iH)\), \(0<a<\pi/2\),
the exact continuation, away from the rectangle boundary, is
\[
 \begin{split}
 \mathcal J^{\mathrm o}_{n,N}(w)
  &=\mathcal O^{\mathrm o}_nF(w)-\mathcal T^{\mathrm o}_{n,N}(w)
            -N\nu_N(w)\frac{h_{n,N}(w)}{Q_{\mathrm o}(w)},\\
 \mathscr D^{\mathrm o}_{n,N}(w)
  &=(1-\nu_N(w))\frac{h_{n,N}(w)}{Q_{\mathrm o}(w)}
       -\frac{\mathcal J^{\mathrm o}_{n,N}(w)
                     +\mathcal T^{\mathrm o}_{n,N}(w)}{N}.
 \end{split}
 \tag{14}
\]
Here \(\nu_N=1\) if both angular evaluation poles are enclosed,
and zero otherwise. Each of the two additional angular poles
has residue \(-h_{n,N}(w)/Q_{\mathrm o}(w)\) before the
prefactor in the unsimplified Cauchy integrand, giving the
displayed factor \(-N\). Thus the interior case cannot be
obtained by ignoring this residue.

**Corollary 2.** At an actual unit-charge positive internal pair
of integer powers \(n,p\ge3\), on a fixed neighborhood of the
angle \(t\) at its power-\(n\) vertex, one has
\[
 \begin{split}
 \mathscr D^{\mathrm o}_{n,N}(-2\cos z)
 &=\frac{h_{n,N}(-2\cos z)}{Q_{\mathrm o}(-2\cos z)}
                     (1+O(N^{-1/2}e^{-\delta N}))\\
 &=i(-1)^mN^{-3/2}
       \frac{a_e(z,0)}{2\sin(z/2)}e^{NS_n(z)}
                                  (1+O(N^{-1}))\ne0
 \end{split}
 \tag{15}
\]
for some \(\delta>0\), at all large odd levels.
Every fixed ordinary spectral derivative has the corresponding
differentiated holomorphic expansion on smaller neighborhoods.

*Proof.* The [pair comparison theorem](research_pair_half_charge_action_gap.md)
gives \(H(t)>H_0\) and \(\Re S_n(t)>M_n\).
The color is therefore exterior to the rectangle. The contour
proof of (11) applies uniformly on a fixed neighborhood of this
color, because its Cauchy denominators stay away from zero on
the contour and at the physical nodes. It gives
\(\mathcal I^{\mathrm o}_{n,N}/Q_{\mathrm o}
=O(N^{-2}e^{NM_n})\).
Meanwhile (2) gives exactly, in the lower half-plane,
\[
 \frac1{Q_{\mathrm o}(-2\cos z)}
 =\frac{i(-1)^m e^{-iNz/2}}
        {2\sin(z/2)(1-e^{-iNz})}.
 \tag{16}
\]
The direct complete-edge packet and the strict action gap prove
(15). Cauchy's formula treats normalized remainders and ordinary
color derivatives; \(\sin t\ne0\) on the neighborhood.
The original crossing carrier is restored by multiplying by
\(C_{N,n}=\exp(\pi i n(N-1)^2/(4N))\).
No carrier has been included twice. \(\square\)

## 3. The original odd trace still has its top-degree term

The odd full-node normal defect must not be substituted for a
weighted positive trace. Let
\[
 Q_{j,N}(w)=\prod_{a=j}^{m}(w-c_a),\qquad
 S_{j,N}=\prod_{r=1}^{j}2\sin(r\pi/N),\qquad
 \ell_{n,N}=[w^m]\mathcal I^{\mathrm o}_{n,N}(w).
\]
For any contour in the slit plane enclosing the remaining
nodes, the exact original trace is
\[
 \begin{split}
 \phi_N[R^n\mathcal L_Ne_j]
  ={}&\frac{C_{N,n}N^2(-1)^j}{2\pi i S_{j,N}^2}
       \oint\frac{(w+2)\mathscr D^{\mathrm o}_{n,N}(w)}
                      {Q_{j,N}(w)}\,dw\\
 &\quad+\boldsymbol 1_{\{j=m\}}\,
               C_{N,n}N^2\ell_{n,N}\frac{(-1)^m}{S_{m,N}^2},
                       \qquad 0\le j\le m .
 \end{split}
 \tag{17}
\]
Indeed the original normal-defect formula gives
\(\sum_{a<m}(4-c_a^2)Q_{\mathrm o}'(c_a)
\mathscr D^{\mathrm o}_{n,N}(c_a)e_j(c_a)\), plus the product
of the two leading coefficients times \(N^2\).
Use (4) and
\(e_j/Q_{\mathrm o}=(-1)^j/(S_{j,N}^2Q_{j,N})\) to obtain
the contour term in (17). The factor \(w+2\) cancels the
simple endpoint pole, exactly as the first-normal trace
requires. The remaining rank-one term includes that original
endpoint and the top-degree polynomial coefficient.

For \(j=m\) the contour integrand is holomorphic, so this
entire term is zero, not an approximation. Since \(S_{m,N}^2=N\),
\[
 \phi_N[R^n\mathcal L_Ne_m]
       =C_{N,n}(-1)^mN\,\ell_{n,N},\qquad
 N\ell_{n,N}=\lim_{w\to+\infty}w\mathcal O^{\mathrm o}_nF(w).
 \tag{18}
\]
The uniform observation theorem gives its explicit nonzero
half-charge asymptotic
\[
 \phi_N[R^n\mathcal L_Ne_m]
   =C_{N,n}N^{-1}b^{\mathrm o}_{n,\infty}
                   e^{N\mathcal S_n}(1+O(N^{-1})),
 \quad
 b^{\mathrm o}_{n,\infty}
  =\frac{\sqrt{2\pi}}{\pi}
          \frac{\cos(t_0/2)a_e(t_0,0)}{\sqrt{A_n}}\ne0 .
 \tag{19}
\]
The limit in (18) can be taken directly in the bounded rational
amplitudes and finite sums of the contour proof.
In particular a two-vertex product of these top-index terms
has rate \(M_n+M_p<2M_\infty\).
The strict inequality follows by integrating the positive
height along each half-charge leaf from charge zero.
This does not estimate the other shared indices.

The identities and local packets above retain the actual odd
simple node, all first normals, and the full top-degree correction.
They do not establish a global signed internal-pair asymptotic or
a positive energy identity for this unweighted odd observation.

## 4. Independent finite normalization checks

The [focused checker](../experiments/check_odd_half_charge_observation.py)
constructs the crossing and its signed powers by multiplication
and division in the original Newton quotient. It compares those
traces with (17), including the simple endpoint and the top
coefficient. Separately, it integrates the sine contour and checks
both exterior and interior evaluation colors with their exact
residue correction.

~~~sh
.venv/bin/python experiments/check_odd_half_charge_observation.py --precision 100
~~~

The [saved record](../repro/results/research-odd-half-charge-observation.json)
contains the script, direct dependency, and proof hashes. These
finite checks test normalizations; no finite sample is used to
prove the asymptotic or its nonzero coefficient.

