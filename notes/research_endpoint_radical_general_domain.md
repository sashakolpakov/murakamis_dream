# An explicit general domain for the endpoint half-character amplitude

Private research note, 16 November 2026. Written proof only.

The analytic interpolation of the original endpoint's entire high
coupon extends to an explicit complex domain. Its exact physical-row
identity and its domain of uniform asymptotics remain different
assertions. No original low coupon, spectator, or contour side term
is discarded.

The sole direct proof source is
[the endpoint half-character amplitude theorem](research_endpoint_radical_half_character_amplitude.md),
SHA256 85c866a031d1293a1cc896a172ab465a52f469a19a4326219856d52ed3970ac8.
Its entire proof was read at this version. The adopted file is unchanged.

## 1. The exact interpolation with a general cutoff

Retain the source's notation
\[
 D=N-1,\quad m=\lfloor N/2\rfloor,\quad\eta=(-1)^D,\quad
 \theta=\pi/N,\quad w_N(\alpha)=2\cosh(\alpha/N),
 \qquad \tau_a=(D-2a)\theta.
 \tag{1}
\]
Thus, with the original local normal consumed exactly,
\[
 \phi_N(B^{\rm high}_{N,\alpha}f)
       =\eta\sum_{a=0}^{m-1}(-1)^a
                         \gamma_{a,N}(\alpha)f(c_a).
 \tag{2}
\]
Fix \(0<\delta<1/2\), put \(L_N=\lfloor\delta N\rfloor\), and take
\(N\) large enough that \(L_N<m\). Define
\[
 (A_l,B_l)=
 \begin{cases}
 ((l+\tfrac12)\theta,(l+1)\theta),&N\ {\rm even},\\
 ((l+1)\theta,(l+\tfrac32)\theta),&N\ {\rm odd},
 \end{cases}
\]
\[
 \rho_{l,N}(\alpha,t)=
 \frac{[\cos^2 A_l+\sinh^2(\alpha/(2N))]
          [\sin^2(t/2)-\sin^2 A_l]}{\cos^4 B_l},
 \qquad
 H_N^\delta(\alpha,t)=
       \sum_{l=0}^{L_N}\prod_{j=0}^{l-1}\rho_{j,N}(\alpha,t).
 \tag{3}
\]
All denominators are nonzero. With the exact base factor
\[
 T_{0,N}(\alpha,t)=
 \begin{cases}
 \displaystyle\frac{\cosh(\alpha/2)}N\sin t,&N\ {\rm even},\\[3pt]
 \displaystyle
 \frac{\cosh(\alpha/2)\cosh(\alpha/(2N))}
      {N\cos^4(\theta/2)}\sin t\sin(t/2),&N\ {\rm odd},
 \end{cases}
 \qquad \Gamma_N^\delta=T_{0,N}H_N^\delta,
 \tag{4}
\]
one has, for each fixed \(b<2\pi\delta\) and all sufficiently large \(N\),
\[
 \Gamma_N^\delta(\alpha,\tau_a)=\gamma_{a,N}(\alpha)
                         \qquad(0<\tau_a\le b).
 \tag{5}
\]
This holds for every complex \(\alpha\). Indeed the actual lowering
chain stops at \(p_a=m-1-a\), where the next ratio contains the zero
\(\sin^2(\tau_a/2)-\sin^2 A_{p_a}\). Here \(p_a=(N\tau_a/\pi-1)/2\)
at even levels and \(p_a=N\tau_a/(2\pi)-1\) at odd levels. The strict
window bound gives \(p_a<L_N\), so every extra product vanishes
exactly. No analytic estimate is used in (5).

## 2. The exact limiting contraction domain

Put
\[
 a_\delta=\sin^2(\pi\delta),\quad c_\delta=\cos(2\pi\delta),\quad
 z=\sin^2(t/2),
\]
\[
 \mathcal D_\delta
 =\{t:|z-a_\delta|<1-a_\delta\}
 =\{t:|\cos t-c_\delta|<1+c_\delta\}.
 \tag{6}
\]
Equivalently \(\Re\sec^2(t/2)>1/[2\cos^2(\pi\delta)]\):
write \(w=1-z\), square \(|w-(1-a_\delta)|<1-a_\delta\),
and divide by \(|w|^2\). In particular the displayed domain excludes
\(w=0\).
In the exponential coordinate \(\zeta=e^{it}\ne0\), this is the
explicit real algebraic inequality
\[
 |\zeta^2-2c_\delta\zeta+1|^2
                   <4(1+c_\delta)^2|\zeta|^2.
 \tag{7}
\]
The limiting ratio indexed by \(v\in[0,a_\delta]\) is
\(r_v(z)=(z-v)/(1-v)\). The disks \(\{|z-v|<1-v\}\) are nested.
More precisely \(r_v(z)=1+(z-1)/(1-v)\) traverses the straight
segment from \(z\) to \((z-a_\delta)/(1-a_\delta)\). Therefore
\[
 \max_{0\le v\le a_\delta}|r_v(z)|
       =\max\left\{|z|,\frac{|z-a_\delta|}{1-a_\delta}\right\}.
 \tag{8}
\]
This maximum is less than one exactly on (6). The criterion is
sharp for contraction of the individual limiting ratios; its
failure does not rule out another description of the finite sum.

**Theorem 1.** On every compact \(\mathcal K\Subset\mathcal D_\delta\)
and every compact set of complex \(\alpha\)'s, there are \(q<1\)
and \(N_0\) such that, for every \(N\ge N_0\),
\[
 |\rho_{l,N}(\alpha,t)|\le q\quad(0\le l<L_N),\qquad
 H_N^\delta(\alpha,t)=\sec^2(t/2)+O_{\rm hol}(N^{-2}).
 \tag{9}
\]
Every fixed derivative in \(\alpha,t\) has the same error bound
on compact subsets. The exact factors \(H_N^\delta\) are eventually
nonzero on these compacts.

*Proof.* Write \(v_l=\sin^2 A_l\). For \(l<L_N\),
\(0\le A_l\le\pi\delta\), \(B_l=A_l+\theta/2\), and \(\cos B_l\)
is uniformly bounded away from zero. Uniformly in \(l\),
\[
 \rho_{l,N}=\frac{z-v_l}{1-v_l}+O(N^{-1}).
 \tag{10}
\]
This includes the denominator shift and the \(O(N^{-2})\) term
\(\sinh^2(\alpha/(2N))\). Equation (8) proves the contraction
bound in (9), also with \(|z|\le q\) after increasing \(q<1\).
The stronger elementary estimate
\[
 |\rho_{l,N}-z|\le C(l+1)^2N^{-2}
 \tag{11}
\]
follows by expanding the sine and cosine factors at zero, with
their denominators bounded away from zero and
\(A_l,B_l=O((l+1)/N)\). Telescoping products gives
\[
 \left|\prod_{j<l}\rho_{j,N}-z^l\right|
                  \le C N^{-2}l^3q^{l-1}.
 \tag{12}
\]
Summing this bound and the exponentially small geometric tail
beyond \(L_N\) proves (9), since \(\sum z^l=(1-z)^{-1}\).
Cauchy's formula on slightly larger compact neighborhoods proves
the derivative assertion. Finally \((1-z)^{-1}\) is nonzero and
bounded away from zero on each compact, proving eventual
nonvanishing. A bound \(q<1\) alone would not prove this last
assertion when \(q\) is close to one. \(\square\)

Consequently the exact amplitudes have the normalized profiles
\[
 \Gamma_N^\delta(\alpha,t)=
 \begin{cases}
 \displaystyle\frac{\cosh(\alpha/2)}N\sin t
 [\sec^2(t/2)+O_{\rm hol}(N^{-2})],&N\ {\rm even},\\[3pt]
 \displaystyle\frac{\cosh(\alpha/2)}N\sin t\sin(t/2)
 [\sec^2(t/2)+O_{\rm hol}(N^{-2})],&N\ {\rm odd}.
 \end{cases}
 \tag{13}
\]
Derivatives are controlled after factoring the displayed exact
zeros. The whole amplitude is a unit only where those factors
are nonzero; in particular \(\cosh(\alpha/2)=0\) is an exact
obstruction. Bounds and identities allow arbitrary bounded complex
\(\alpha\)-sets, including these zeros. Evenness in \(\alpha\)
also retains the source's \(O(N^{2j})\) cost for \(j\) ordinary
derivatives in the microscopic endpoint color \(w\).

Equation (5) holds throughout its physical window, whereas the
estimates require the angles also to lie in a compact subset of
(6). In particular \(0\in\mathcal D_\delta\) if and only if
\(\delta<1/4\). A larger exact cutoff need not give symbol control
near the complete angle.

## 3. A useful closed rectangle

Take \(\delta=1/8\), so \(c_\delta=1/\sqrt2=:c\). Then
\[
 \mathcal R=\{t:|\Re t|\le\pi/4,\ |\Im t|\le\log3\}
                         \Subset\mathcal D_{1/8}.
 \tag{14}
\]
Indeed put \(C=\cos(\Re t)\in[c,1]\) and
\(u=\cosh(\Im t)\in[1,5/3]\). One has
\[
 |\cos t-c|^2=C^2+u^2-1-2cCu+c^2.
 \tag{15}
\]
This increases in \(u\) and is convex in \(C\). Its maximum is
at \(u=5/3\), \(C=c\) or \(1\). These values are \(10/9\) and
\((5/3-c)^2<10/9\), respectively. Thus
\[
 \frac{|z-a_\delta|}{1-a_\delta}
       \le\frac{\sqrt{10}}{3(1+c)}<\frac23,\qquad
 |z|=\frac{\cosh(\Im t)-\cos(\Re t)}2
       \le\frac{5/3-c}{2}<\frac12.
 \tag{16}
\]
The limiting ratios are uniformly below \(2/3\); for bounded
complex \(\alpha\), the finite ratios are at most \(3/4\) on
\(\mathcal R\) for large \(N\). All conclusions of Theorem 1
hold on a neighborhood of this closed rectangle. Exact physical
termination still uses \(0<\tau_a\le b<\pi/4\).
This is an analytic scale statement, not a geometric existence
theorem or a claim about a new knot class.

## 4. Exact contour identity versus uniform estimates

Choose positive midpoints \(b_N\le b<2\pi\delta\) with
\(e^{iNb_N}=-\eta\), and let \(H>0\). For any even spectator
representative \(F\), holomorphic near the closed rectangle
\([-b_N,b_N]+i[-H,H]\), put
\[
 A_N(t)=\Gamma_N^\delta(\alpha,t)F(t),\qquad
 \mathcal S_N=\eta i^{-D}
       \sum_{0<\tau_a<b_N}A_N(\tau_a)e^{iN\tau_a/2}.
 \tag{17}
\]
For large \(N\), (5) makes this the actual central high-coupon sum.
The exact identity is
\[
 \begin{split}
 \mathcal S_N={}&\frac{N i^{-D}}{2\pi}
       \int_{-b_N-iH}^{b_N-iH}
       \frac{A_N(t)e^{-iNt/2}}{1-\eta e^{-iNt}}\,dt\\
 &+\frac{\eta N i^{-D}e^{iNb_N/2}}{4\pi i}
       \int_{-H}^{H}\frac{A_N(b_N+ih)}{\cosh(Nh/2)}\,dh.
 \end{split}
 \tag{18}
\]
The source's residue proof applies unchanged: \(\Gamma_N^\delta\)
is entire in \(t\), has parity \(\eta\), and vanishes at the odd
zero-angle node. The residue-one kernel
\(iN\eta/(e^{iNt}-\eta)\), reflection, and the midpoint phase
give (18), with no contraction assumption on the rectangle.

Uniform use of (13) along the contours, in contrast, requires
them to lie in a common compact subset of \(\mathcal D_\delta\).
For example \(\delta=1/8\), fixed \(b<\pi/4\), and
\(0<H\le\log3\) meet that condition. The horizontal aliases,
paired vertical integral, noncentral physical rows, low coupon,
and original spectator all remain. Neither (18) nor the larger
symbol domain proves a gap for their combined contribution.
