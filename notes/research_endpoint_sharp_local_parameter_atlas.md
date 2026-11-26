# Sharp endpoint representatives on a finite local parameter atlas

Private written proof, 16 November 2026.

The sharp sine-factor construction extends to every bounded complex
microscopic parameter set by a finite collection of local analytic
bases. A terminating zero removes the odd index resonances. At an
even resonance, an explicit reflected tail removes the pole, with
the same spectral eigenvalue and sharp residual rate. Reflection
then gives the actual physical value and first-normal estimate on
each chart. The exact one-sided repair retains its original
interface and exterior currents.

No single global basis, transition estimate between charts, or bound
for a filled closing is asserted.

## 1. Statement and conventions

Put \(h=N^{-1}\), and retain
\[
 s_z=2\sin(\pi hz),\qquad c_z=2\cos(\pi h(2z+1)),\qquad
 C_N(x)=2\cos(2\pi x+\pi h),\qquad w_N(\alpha)=2\cosh(\alpha h).
 \tag{1}
\]
The ordinary kernel is the original
\[
 K_N(w,C)=\sum_{k=0}^{N-1}e_k(w)e_k(C),\qquad
 e_k(C)=S_k^{-2}\prod_{j<k}(c_j-C),\qquad
 S_k=\prod_{j=1}^k s_j,\quad S_0=1.
\]
Write \(P_N(C)=2T_N(C/2)+2\), with \(T_N\) the Chebyshev
polynomial.
The operator \(\mathscr J_N\), its ordinary source, and all
physical normals have the conventions of the sharp connection
source. Fix \(x_0\in(0,1/2)\), and set
\[
 \delta=\frac1\pi\arcsin\frac{\sin(\pi x_0)}{\sqrt2},\qquad
 m=\lfloor\delta N\rfloor,\qquad
 I_\delta(X)=\int_0^\delta
       \log\frac{\sin^2(\pi X)-\sin^2(\pi v)}{\sin^2(\pi v)}\,dv.
 \tag{2}
\]
Thus \(I_\delta(x_0)=J_*(\pi-2\pi x_0)>0\).
Choose small buffered intervals
\[
                 \delta<a<x_0<b<b_*<1/2,\qquad I_\delta(a)>0.
 \tag{3}
\]
The symmetric interval \([a,1-a]\) has fixed larger buffers
inside \((\delta,1-\delta)\). Any finite prescribed imaginary
heights are allowed on the corresponding buffered rectangles.

**Theorem.** For every compact \(\mathcal A\subset\mathbb C\),
there is a finite cover of \(\mathcal A\) by parameter charts,
with larger chart neighborhoods reserved for derivatives, on each
of which the following assertions hold for all sufficiently large
\(N\). There is a holomorphic pair of moderate approximate modes,
and its two-value normalization \(V_N(x,\alpha)\) at a fixed
physical anchor \(x_{j_*}\in[b,b_*]\) has polynomial norm at the
prescribed heights. At all physical \(x_j=j/N\in[a,b]\),
\[
 \left|\partial_\alpha^q[K_N(w_N(\alpha),C_N(x_j))-V_N(x_j,\alpha)]\right|
 +\left|\partial_\alpha^q[
    \partial_xK_N(w_N(\alpha),C_N(x_j))-\partial_xV_N(x_j,\alpha)]\right|
       \le C_qN^{p_q}e^{-NI_\delta(x_j)}.
 \tag{4}
\]
Here the derivative of the kernel means that of its displayed
composition with \(C_N\). The same form holds for fixed original
endpoint spectral derivatives, with polynomial losses.
The ordinary residual satisfies
\[
 |\partial_x^r\partial_\alpha^q
                    (\mathscr J_N-w_N)V_N(x,\alpha)|
       \le CN^p e^{-NI_\delta(\Re x)}.
 \tag{5}
\]
All constants can be chosen uniformly over the finite cover.
The scalar and its representatives are chosen locally, rather
than identified on chart overlaps.

For any \(0<\ell<J_*(\pi-2\pi x_0)\), shrink the fixed real
window so that \(I_\delta\ge\gamma:=J_*(\pi-2\pi x_0)-\ell\)
on its larger buffer. On each chart there are exact one-sided
representatives of all physical values and first normals, whose
corrections and weighted real interface are bounded by
\(CN^p e^{-N\gamma}\). This holds for fixed shared products as
well, with their original crossing and joint spectator retained.
The exact contour statement is specified in section 6.

## 2. The finite coefficient family away from its resonances

Use the specified factorial interpolation
\[
 G_N(t)=\left(\frac{2\pi}{N}\right)^t\Gamma(t+1)
    \prod_{k\ge1}
       \frac{\Gamma(Nk+t+1)}{\Gamma(Nk-t)(Nk)^{2t+1}},
 \qquad -1<\Re t<N,
\]
\[
 F_z(x)=4^{-z}\frac{G_N(Nx+z)}{G_N(Nx-z)},\qquad
 U_{M,N}(z,x)=\sum_{k=0}^M a_k(z)F_{z-k}(x),
\]
\[
 a_0=1,\qquad
 \frac{a_k(z)}{a_{k-1}(z)}
    =\frac{s_{z-k+1}^4}{4s_ks_{2z+1-k}}.
 \tag{6}
\]
All powers and factorial logarithms have the fixed real
normalization of the source. We use \(M=m-d\), where \(d\)
belongs to a fixed finite set of nonnegative integers. All
growing-index factorial arguments in (6), and in the final
lowering term below, stay in its zero-free strip on the
buffered rectangles, since \(a>\delta\) and
\(1-a+\delta<1\). This assertion is uniform for bounded \(z\)
and all large \(N\).

The exact ordinary identities are
\[
 \mathscr J_NF_z=c_zF_z-\frac{s_z^4}{4}F_{z-1},\qquad
 (\mathscr J_N-c_z)U_{M,N}(z,x)
       =-\frac{a_M(z)s_{z-M}^4}{4}F_{z-M-1}(x).
 \tag{7}
\]
Also \(c_{-z-1}=c_z\) identically, and each finite sum has
the exact reflection
\[
                         U_{M,N}(z,1-h-x)=U_{M,N}(z,x).
 \tag{8}
\]
This follows from \(G_N(t)G_N(N-1-t)=N\), with the
normalization fixed by the Gamma product.

On a bounded \(z\)-set, the only possible coefficient poles for
\(1\le k\le m\) and large \(N\) occur at
\[
                         2z+1=k,\qquad k\in\mathbb Z_{>0}.
 \tag{9}
\]
Indeed \(s_k\ne0\), and \(s_{2z+1-k}=0\) requires
\(2z+1-k\in N\mathbb Z\). Bounded \(z\) and \(m<N/2\)
exclude every nonzero multiple of \(N\). Thus only finitely
many fixed positive integers in (9) meet the parameter set.

For compact parameter sets avoiding (9), the exact summand ratio
from the source is
\[
 \frac{a_kF_{z-k}}{a_{k-1}F_{z-k+1}}
 =\frac{s_{z-k+1}^4}
 {s_ks_{2z+1-k}s_{Nx+z-k+1}s_{Nx-z+k}}.
 \tag{10}
\]
The proof there does not otherwise require \(-1<\Re z<0\).
For large fixed \(k\), bounded \(z\) gives the first-factor
bound \(s_k^2(1+C/k)\); the finitely many smaller \(k\)
are uniformly controlled by the distance from (9).
The unshifted spatial sine product has modulus at least
\(\sin^2(\pi\Re x)-\sin^2(\pi k/N)\); the bounded \(zh\)
shifts change its estimate by a factor \(e^{Ch}\).
Summing logarithms therefore gives
\[
 |a_kF_{z-k}(x)|\le CN^p e^{-NI_{k/N}(\Re x)}.
 \tag{11}
\]
The first ratio is \(O(h^2)\), a fixed initial fraction of
the ratios is a contraction, and the remaining terms have a
positive exponential saving. Consequently
\[
 U_{M,N}(z,x)=F_z(x)+O_{\rm hol}(h^2)
       =\{\sin\pi(x+h/2)\}^{2z}+O_{\rm hol}(h^2).
 \tag{12}
\]
Equations (7) and (11) give every fixed residual derivative
the bound
\[
 |\partial_x^r\partial_z^q
               (\mathscr J_N-c_z)U_{M,N}(z,x)|
             \le CN^p e^{-NI_\delta(\Re x)}.
 \tag{13}
\]
Changing \(m\) to \(m-d\) costs only a bounded exponential
factor: \(d\) is fixed and the integrand at the positive
endpoint \(\delta\) is uniformly smooth. Spatial derivatives
use disks of radius \(c/N\); parameter derivatives use fixed
larger neighborhoods. These preserve the exponent in (13).

## 3. Odd resonances terminate; even resonances have one reflected pole

Fix a resonance \(L=2z_0+1\in\mathbb Z_{>0}\), and take a
small fixed disk around \(z_0\) containing no other resonance.
For all large \(N\), \(m\ge L\).

If \(L=2b+1\) is odd, \(z_0=b\) is a nonnegative integer.
The numerator factor at \(k=b+1\) has a zero of order four.
The sole vanishing denominator factor is at \(k=L\), with
a simple zero. For \(b=0\) they occur in the same factor;
the remaining zero has order three. For \(b\ge1\) the
numerator zero occurs first. It follows directly from the
product in (6) that every \(a_k\) extends holomorphically,
and
\[
                         U_{m,N}(b,x)=
                           \sum_{k=0}^{b}a_k(b)F_{b-k}(x).
 \tag{14}
\]
Thus this family terminates at the resonance.
The estimates (12)--(13) on the disk boundary extend inside
by the maximum principle, applied respectively to the
holomorphic error and the ordinary residual. Their fixed
derivatives follow on smaller disks.

Suppose instead that \(L\) is even. Then \(z_0=(L-1)/2\)
is a positive half-integer. No numerator factor in (6)
vanishes at \(z_0\); precisely the denominator at \(k=L\)
does. All coefficients with \(k\ge L\) have a simple pole.
Since
\[
 \partial_z(c_{z-L}-c_z)\big|_{z=z_0}=4\pi h s_L,
\]
its first residue is exactly
\[
 \boxed{\quad
 R_{N,L}:=\operatorname*{Res}_{z=z_0}a_L(z)
      =\frac{a_{L-1}(z_0)s_{z_0-L+1}^4}{16\pi h s_L}
      =\frac{\prod_{j=1}^L s_{z_0-j+1}^4}
                   {4^L S_LS_{L-1}(4\pi h)},
 \quad S_k=\prod_{j=1}^k s_j .
 \quad}                                                     \tag{15}
\]
It is positive for all sufficiently large \(N\), and
\[
                  0<R_{N,L}\le C_L h^{2L}.
 \tag{16}
\]
In fact \(h^{-2L}R_{N,L}\) has a positive finite limit:
all numerator arguments in (15) are fixed nonzero
half-integers, and all denominator indices are fixed positive
integers. Counting their powers of \(h\) gives \(4L-2L=2L\).
Thus (16) does not hide a parameter-dependent exponential factor.

Put \(z_0^*=-z_0-1=z_0-L\). For each \(l\ge1\), the
ratio of consecutive residues is
\[
 \frac{\operatorname{Res}a_{L+l}}{\operatorname{Res}a_{L+l-1}}
       =\frac{s_{z_0^*-l+1}^4}{4(c_{z_0^*-l}-c_{z_0^*})}.
 \tag{17}
\]
Here \(c_{z_0}=c_{z_0^*}\) is essential. This is precisely
the coefficient recurrence for the reflected index. Hence
the complete residue, including its cutoff, is
\[
 \boxed{\quad
 \operatorname*{Res}_{z=z_0}U_{m,N}(z,x)
                  =R_{N,L}\,U_{m-L,N}(-z_0-1,x).
 \quad}                                                     \tag{18}
\]

Define on this chart
\[
 W_{0,N}(z,x)=U_{m,N}(z,x)
             -\frac{R_{N,L}}{z-z_0}U_{m-L,N}(-z-1,x),
 \qquad
 W_{1,N}(z,x)=U_{m-L,N}(-z-1,x).
 \tag{19}
\]
The moving reflected family is analytic on the entire disk,
because \(2(-z_0-1)+1=-L<0\). Equations (18)--(19)
therefore remove the pole exactly. In an \(\alpha\)-coordinate,
the residue is \(R_{N,L}/(dz/d\alpha)\); formula (19) already
includes this change correctly through \(z-z_0\).

On the fixed parameter circle the subtraction in (19) is
\(O(h^{2L})\), hence \(O(h^4)\). Equations (12)--(13),
including the fixed cutoff loss \(L\), apply to both terms.
The equality \(c_{-z-1}=c_z\) for every \(z\), not just at
the center, shows that the same subtraction regularizes the
ordinary residual. Maximum principles on the disk thus give
\[
 W_{0,N}(z,x)=\{\sin\pi(x+h/2)\}^{2z}+O_{\rm hol}(h^2),
\]
\[
 W_{1,N}(z,x)=\{\sin\pi(x+h/2)\}^{-2z-2}+O_{\rm hol}(h^2),
 \tag{20}
\]
and (13) for both residuals with their common eigenvalue \(c_z\).
Every mode in (19) retains (8). No assertion of an exact
homogeneous solution is made.

## 4. The finite atlas and its regular spectral frames

Use \(z_+(\alpha)=-1/2+i\alpha/(2\pi)\) and
\(z_-(\alpha)=-z_+(\alpha)-1\).
Outside a small neighborhood of zero and the finitely many
resonances of either index, use the two ordinary sums.
Near a nonzero resonance choose the index having \(2z+1=L>0\).
For odd \(L\) use its holomorphic terminating extension and
the analytic reflected sum. For even \(L\) use (19).
At zero use the source's coalesced pair
\[
 \frac{U_{m,N}(z_+)+U_{m,N}(z_-)}2,\qquad
 \frac{U_{m,N}(z_+)-U_{m,N}(z_-)}{2i\alpha/\pi}.
 \tag{21}
\]
The second quotient is removable. A sufficiently small disk
around zero contains no other resonance.

These choices cover any bounded parameter set by finitely many
fixed charts. The estimates may use smaller chart interiors
whose union still covers \(\mathcal A\). A common sufficiently
large \(N\), polynomial exponent, and constant work on their
closures. The possible resonances from nonzero multiples of
\(N\) were excluded in (9); none is missed by this cover.

The centered leading modes in a nonzero chart are the spectral
functions
\[
 \Phi_z(C)=\left(\frac{2-C}{4}\right)^z,\qquad
 \Phi_{-z-1}(C)=\left(\frac{2-C}{4}\right)^{-z-1},
\]
\[
       \Phi_z\Phi_{-z-1,C}-\Phi_{-z-1}\Phi_{z,C}
                          =\frac{4(2z+1)}{(2-C)^2}.
 \tag{22}
\]
The logarithm is real on the traversed real spectral interval
and holomorphic on a fixed neighborhood avoiding \(C=2\).
Equation (22) is a uniform unit on each nonzero chart.
For (21) the corresponding determinant is
\(-2/(2-C)^2\), including \(\alpha=0\).

All the exact modes are invariant under \(x\mapsto1-h-x\).
Their \(O_{\rm hol}(h^2)\) remainders therefore descend
uniformly to the spectral variable at the fold, by the even
power-series argument of the reflected source. For the
divided-color state
\[
 \mathcal V_f(x)=
   \binom{f(x)}{[f(x)-f(x-h)]/[C_N(x)-C_N(x-h)]},
 \tag{23}
\]
the two mode columns form a uniformly invertible holomorphic
frame through the fold, with the quotient read by continuation
at coincident colors. Equations (20)--(22) prove this without
division by a vanishing angular derivative.

## 5. Application to the actual full physical jets

Let \(\mathcal F_N\) be any of the chart frames in (23), and
put \(u_N=K_N(w_N(\alpha),C_N(\cdot))\),
\[
 \mathbf a_N(x)=\mathcal F_N(x)^{-1}\mathcal V_{u_N}(x),
 \qquad
 \mathbf a_*=\mathbf a_N(x_{j_*}),\qquad
                  V_N(x)=(H_{0,N}(x),H_{1,N}(x))\mathbf a_* .
 \tag{24}
\]
The actual polynomial kernel bound and Markov bound in the
reflected source apply on every bounded complex parameter set.
Thus \(\mathbf a_N\) has polynomial real-interval norm, and
\(\mathbf a_*\) is holomorphic with that bound on each chart.

Here is why the full-normal proof applies also to the regularized
pair with unequal cutoffs. Its exact regular color transfer gives
\[
 \mathbf a_N(x+h)=(I+M_N(x))\mathbf a_N(x)-\ell_N(x)r_K(x),
\]
\[
 M_N=\mathcal F_N(x+h)^{-1}\mathbf b_N(x)\mathbf r_N(x),\qquad
 \|M_N\|+\|M_N'\|\le CN^p e^{-NI_\delta(\Re x)}.
 \tag{25}
\]
Here \(\mathbf r_N\) consists of the two ordinary residuals,
\(\mathbf b_N\) is the original regular forcing vector, and
\[
 r_K(x)=-\frac{P_N(w_N)P_N(C_N(x))}
                         {N^4(C_N(x)-c_0)},\qquad
                         P_N(C_N(x))=4\sin^2(\pi Nx).
 \tag{26}
\]
At the physical rows in the symmetric buffer, both \(r_K\)
and \(r_K'\) vanish. Every chart frame and the actual kernel
have the same reflection matrix in (23), so
\[
                  \mathbf a_N(1-x)=\mathbf a_N(x).
 \tag{27}
\]
Differentiate (25) before evaluating at physical rows.
Propagation from \(j\) to \(N-j\), followed by (27), gives
\[
 (I+P_j)\mathbf a_N'(x_j)=-Q_j\mathbf a_N(x_j),\qquad
 \|P_j-I\|+\|Q_j\|\le CN^p e^{-NI_\delta(x_j)}.
 \tag{28}
\]
The exponent is preserved because \(I_\delta\) has its
minimum at the endpoints of \([x_j,1-x_j]\).
Since \(I+P_j=2I+o(1)\), (28) bounds the actual derivative
coefficient sharply. The value equation in (25), propagated
to the right anchor, bounds \(\mathbf a_N(x_j)-\mathbf a_*\)
at the same rate. Differentiating \(u_N=H\mathbf a_N\)
now proves (4); (5) follows from the polynomial anchor and
the mode residuals.

The argument uses only reflection, the regular frame, common
eigenvalue, and the two residual bounds. It does not require
the two cutoffs to coincide. Both parities, including the odd
simple spectral row at the fold, have the same angular source
zeros in (26); no extra spectral normal is imposed there.

Cauchy estimates on the reserved chart neighborhoods prove fixed
parameter derivatives. Away from zero,
\(dw_N/d\alpha=2h\sinh(\alpha h)\) is a local coordinate
derivative of size comparable to \(h^2\), giving polynomial
cost for fixed \(w\)-derivatives. At zero, the coalesced
construction and its anchor are even in \(\alpha\); the
coordinate \(\alpha^2\) has
\(d(w_N-2)/d(\alpha^2)=h^2(1+O(h^2))\).
This proves the stated original endpoint derivative scope.

## 6. Exact local repair and retained currents

Take a consecutive physical window \(\mathcal W_N\) in the
small interval of the theorem. On any parameter chart let
\[
 e_j=u_N(x_j)-V_N(x_j),\qquad d_j=u_N'(x_j)-V_N'(x_j),
\]
\[
 C_N^\sigma(x)=\sum_{j\in\mathcal W_N}
 \left[e_j+\left(d_j-\frac{\sigma2\pi i}{h}e_j\right)(x-x_j)\right]
 e^{\sigma2\pi i(x-x_j)/h}\operatorname{sinc}^2((x-x_j)/h),
 \qquad H_N^\sigma=V_N+C_N^\sigma .
 \tag{29}
\]
The repair source proves exactly that \(H_N^\sigma\) has
both original jets at every covered node. On the designated
half-rectangle \(\sigma\Im x\ge0\), every fixed derivative
of \(C_N^\sigma\) is bounded by \(CN^p e^{-N\gamma}\).
For
\[
                         D_h(x)=(\pi/h)^2\csc^2(\pi x/h),
\]
its weighted real interface satisfies
\[
                |D_h(C_N^+-C_N^-)|\le CN^p e^{-N\gamma}.
 \tag{30}
\]
The exact removable formula and its signs are those of the
pinned repair theorem; it needs only the error estimate (4).
No opposite-height exponential bound is substituted for
the designated-half estimate.

For a fixed shared product use the product of its chartwise
baselines and, separately, the products of \(H_i^\sigma\).
The product rule preserves the full shared normal; telescoping
preserves the rate \(\gamma\), not \(r\gamma\).
In the notation \(P^\sigma=\prod_i H_i^\sigma\), put
\[
 g_\sigma(x)=\sin(2\pi x+\pi h)\,P^\sigma(x)
 e^{\pi i n(N-1)^2/(4N)}
 e^{inN(\pi-2\pi x-\pi h)^2/(4\pi)}
                      A_N(C_N(x);\mathbf y).
 \tag{31}
\]
Here \(n\) is the original signed power and \(A_N\) the
whole joint spectator, holomorphic on the two contour
half-rectangles. Other traces remain unapplied. With midpoint
window boundaries \(a_N,b_N\) and the original oriented exterior
halves, the restricted full trace is exactly
\[
 -\frac{(-1)^{N-1}}{2\pi^2i}
 \left\{\int_{E_-}D_hg_-\,dx+\int_{E_+}D_hg_+\,dx+
              \int_{a_N}^{b_N}D_h(g_+-g_-)\,dx\right\}.
 \tag{32}
\]
Both vertical half-sides, all grid aliases, the spectator
inside the interface estimate, and every outside physical
row remain. Thus extending the parameter set does not infer
a global current bound, a scalar seed, or a nonzero saddle
coefficient.

## 7. Coverage and direct sources

The sharp nonresonant modes, reflection argument for their
actual normal connection, and exact one-sided repair are
prior results. The additional step is the finite local
resonance removal (15)--(20), with its precise cutoff,
and its uniform application to arbitrary bounded complex
microscopic parameter sets. There is no claim that chart
representatives agree off the physical grid.

The complete direct sources were read at matching pins,
with all used implications checked:

* [Sharp sine-factor truncation](research_endpoint_sine_factor_sharp_truncation.md),
  SHA256 c731b1ccc3ea05f65b1227bff048b4e8a32cf36832289a1ed6e390232cc210bd.
* [Reflected sharp normal connection](research_reflected_endpoint_sharp_normal_connection.md),
  SHA256 a8a379d7b492d7d2487de3c1397408478f66242f153ac0cab8eb3d224f226916.
* [Sharp one-sided window assembly](research_sharp_endpoint_one_sided_window_assembly.md),
  SHA256 163d4cf2fc98648c0739152dbb463f2ad8f19d58b34b31d9184469847e60e541.
* [Specified factorial interpolation](exact_factorial_interpolation_and_complex_contours.md),
  SHA256 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build, or
compilation was run. Adopted notes and public manuscripts are unchanged.
