# A protected middle with strict outer loads cannot maximize at the spectral cap

31 October 2026. **Analytical research lemma; full internal reviews by root and a separate reader, PASS.** This is a calculus statement for the original sharp interval functional. It does not assert a cap-uniform finite coefficient limit, a relative asymptotic, or a contributing Fourier cycle.

## 1. The exact protected-start functional

Take a LEFT interval with its original protected input middle, so its start is exactly \(\mu=0\). Fix
\[
 0<\nu<\tfrac12,\qquad 0<\xi<\nu,\qquad \zeta=\nu-\xi>0.
\]
The original four face degrees \((\xi,0,1-\nu,\zeta)\) stay fixed. Put \(k=\cos(\pi\delta)>0\) and
\[
 \beta(t)=4\sin^2(\pi t),\qquad
 \alpha_\delta(t)=4[k^2-\sin^2(\pi t)],
\]
\[
 \rho_\eta(x)=\frac{1+x+\sqrt{(1-x)^2+4\eta x}}2,\qquad
 J_k(x)=\int_0^\nu\log\rho_{k^2/\sin^2(\pi t)}(x)\,dt.
\]
Normalize \(y=1\) only inside the coefficient Legendre transform. The [original sharp functional](research_global_sharp_coefficient_limsup_majorant.md) is
\[
 \begin{aligned}
 H_k(0,\nu,\xi)&=I_k(\nu)+J_k^*(\xi),\\
 I_k(\nu)&=\int_0^\nu\log\frac{\beta(t)}{|\alpha_\delta(t)|}\,dt,\\
 J_k^*(\xi)&=\inf_{x>0}\{J_k(x)-\xi\log x\}.
 \end{aligned}\tag{1}
\]
This is the actual unused-product plus positive-word normalization. The identities
\[
 \int_0^{1/2}\log|\alpha_\delta(t)|\,dt
 =\int_0^{1/2}\log\beta(t)\,dt=0
\]
incorporate both unused intervals. No omitted-half scalar is divided out. The logarithmic singularities are integrable. At the cap \(k=0\),
\[
 \rho_0(x)=\max(1,x),\qquad I_0=J_0^*=H_0=0.\tag{2}
\]
This equality holds for every closed outer split. The strict improvement below requires both outer loads positive.

## 2. A constant-transition lower bound

Since \(k^2/\sin^2(\pi t)\ge k^2\) and \(\rho_\eta(x)\) increases with \(\eta\), for every \(x>0\),
\[
 J_k(x)\ge\nu\log\rho_{k^2}(x).\tag{3}
\]
Define the constant-transition outer entropy by
\[
 F_k(p)=\inf_{\ell\in\mathbb R}
       \{\log\rho_{k^2}(e^\ell)-p\ell\},\qquad 0\le p\le1.\tag{4}
\]
It is concave in \(p\), as an infimum of affine functions. This uses only outer-degree concavity at fixed interval and transition; it makes no row-concavity or shared minimax assertion. The inequality \(\rho_{k^2}(x)\ge\max(1,x)\) gives \(F_k\ge0\), and the limits \(x\to0,\infty\) give \(F_k(0)=F_k(1)=0\). Also
\[
 \log\rho_{k^2}(e^\ell)-\frac\ell2
 =\log\!\left[\cosh\frac\ell2+
          \sqrt{\sinh^2\frac\ell2+k^2}\right]
 \ge\log(1+k),
\]
with equality at \(\ell=0\). Therefore the two concavity chords give
\[
 F_k(\tfrac12)=\log(1+k),\qquad
 F_k(p)\ge2\min(p,1-p)\log(1+k).\tag{5}
\]
Taking infima in the pointwise inequality (3), with \(p=\xi/\nu\), yields
\[
 J_k^*(\xi)\ge2a\log(1+k),\qquad
 a=\min(\xi,\nu-\xi)>0.\tag{6}
\]
This bound concerns the original sharp Legendre functional, not the fractional triangle perspective. The [exact positive eta-word](research_positive_eta_word_transfer.md) supplies the same interpretation: lower every transition weight to \(k^2\), whose balanced pressure is \(\log(1+k)\). No new finite-level coefficient theorem is needed here.

## 3. The monomer cost is quadratic

For \(k<\sin(\pi\nu)\), the exact half-interval integral identities give
\[
 I_k(\nu)=-\int_\nu^{1/2}
     \log\frac{\sin^2(\pi t)}{\sin^2(\pi t)-k^2}\,dt.\tag{7}
\]
Thus \(I_k\le0\). If \(k^2\le\sin^2(\pi\nu)/2\), the inequality \(-\log(1-z)\le2z\) for \(0\le z\le1/2\) gives
\[
 I_k(\nu)\ge-2k^2\int_\nu^{1/2}\csc^2(\pi t)\,dt
           =-\frac2\pi k^2\cot(\pi\nu).\tag{8}
\]
Consequently
\[
 H_k(0,\nu,\xi)\ge2a\log(1+k)-\frac2\pi k^2\cot(\pi\nu).\tag{9}
\]
For any positive \(k\) satisfying
\[
 k\le\min\left\{1,\frac{\sin(\pi\nu)}{\sqrt2},
                    \frac{\pi a}{4}\tan(\pi\nu)\right\},\tag{10}
\]
use \(\log(1+k)\ge k/2\) to conclude
\[
 H_k(0,\nu,\xi)\ge\frac{ak}{2}>0=H_0(0,\nu,\xi).\tag{11}
\]
The estimates are uniform on compact sets with \(\nu\) away from \(0,1/2\) and both outer degrees bounded below. Each fixed admissible pair has its own positive range (10). Fixed \(k>0\) satisfies the actual finite positive-word condition at all sufficiently large \(N\); no joint \(k_N\) limit is asserted.

The terminal half-interval has a separate immediate conclusion. If \(\nu=1/2\) and \(0<\xi<1/2\), (7) is empty, so \(I_k=0\) exactly and
\[
 H_k(0,\tfrac12,\xi)
 \ge2\min(\xi,\tfrac12-\xi)\log(1+k)>0,
 \qquad 0<k<1.\tag{12}
\]
Thus the cap is also excluded there in the closed sharp functional. This calculus observation asserts no stationarity in the terminal row, change of sector label, or finite support relabeling.

## 4. Reflection and the shared maximum

The [exact finite reflection](research_protected_middle_window_phase_exclusion.md) takes \((i,j)\) to \((d-j,d-i)\) and exchanges the middle variables while preserving the tail and all unused rows. Hence the same conclusion holds for a protected output middle, with interval \([1-\nu,1]\), strict outer loads \(\xi,\nu-\xi\), and \(0<\nu\le1/2\). The finite endpoint is \(j=d\), not \(N\); the recorded one-row shift in the limiting functional does not change a protected target or the reflected RIGHT support.

At a shared sharp-functional maximum with free real spectra, change only this port's \(\delta\) from \(1/2\) to \(\arccos(k)/\pi\). Every original face load, the fixed mark, and every other local term remain unchanged. Equations (11)–(12) therefore exclude this cap.

The strict outer hypothesis is essential. If \(\xi=0\) or \(\xi=\nu\), the word is monomial, \(J_k^*=0\), and (7) is nonpositive. No exclusion of that joint protected-outer corner is claimed. Zero-length intervals, simultaneous two-terminal intervals \([0,1]\), and cap-uniform finite coefficient bounds remain separate questions. The lemma gives no source growth lower bound or original-period contribution.

Both independent reviews checked the full proof and the separately stated terminal half-interval extension. The result is analytical; no numerical audit is needed or claimed.
