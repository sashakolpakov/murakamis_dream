# Fractional boundary data with an original crossing leaf

22 November 2026. Written research proof. Earlier author-final notes
and public manuscripts remain unchanged.

We put one coherent input exactly at zero, where it is the original
positive crossing element divided by \(\sqrt N\). The fractional
boundary packet then has two numerator families instead of three.
Its infinite upper end has a nonzero limiting rate. We retain that
end and prove a relative estimate only where it has a strict gap.
The result supplies two adjacent initial values on every fractional
boundary orbit in this region.

## 1. Original source and statement

Use the full Frobenius algebra and centered basis of [B]:
\[
 \begin{gathered}
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^d,\quad\kappa=e^{\pi i d^2/(2N)},\\
 U_x=\sum_{j=0}^d x^jf_j,\qquad U_0=f_0=R^+/\sqrt N .
 \end{gathered}
 \tag{1}
\]
No quotient of the repeated-root directions is taken. The functional
\(\phi\), multiplication and all phase carriers are the original ones.
Write
\[
 \mathcal L(v)=\int_0^v\log|2\sin\pi t|\,dt ,
\]
extended oddly and periodically. Fix a compact set in
\[
 c,R>0,\qquad c+R<1,\qquad
                  \Delta=\mathcal L(c+R)-\mathcal L(R)>0 .
 \tag{2}
\]
This is an open nonempty region; for example
\(1/6<R<c+R<5/6\) implies its last inequality. Define
\[
 \begin{gathered}
 z=-e^{-2\pi ic},\quad r=e^{-2\pi iR},\quad
 p=NR,\quad L=N-p,\quad
 a\in\mathcal A=[a_-,a_+]\Subset(0,\infty),\\
 s_a=-e^{-2\pi i(a-1/2)/N},\quad t_a=r/s_a,\qquad
             \Phi_a^0=\phi(f_0U_zU_{s_a}U_{t_a}),\\
 M_0=\mathcal L(c+R)-\mathcal L(c)-\mathcal L(R)>0,\\
 g_0=e^{-\pi iR}
        \frac{\sin^2(\pi R)\sin(\pi c)}
             {\pi^2\sin(\pi(c+R))}.
 \end{gathered}
 \tag{3}
\]
The strict positivity of \(M_0\) follows by fixing \(c\): its
derivative in \(R\) is
\(\log[\sin\pi(c+R)/\sin\pi R]\), which changes from positive
to negative once, and its values at \(R=0,1-c\) are zero.
All constants below are uniform on the chosen compact sets.
Enlarge \(\mathcal A\) to contain \(1\), if necessary.

**Theorem.** For all sufficiently large \(N\), the actual scalar
\(\Phi_1^0\) is nonzero and
\[
 \boxed{\quad
 \frac{\Phi_a^0}{\Phi_1^0}
     =\frac{N^{2a-2}}{\Gamma(a)^2}
                  g_0^{\,a-1}(1+O(N^{-1})).
 \quad}
 \tag{4}
\]
Here \(\log g_0\) has imaginary part \(-\pi R\).
In particular, this whole fractional boundary layer is nonzero.
The baseline is exactly the original three-input source
\[
 \Phi_1^0=\kappa\sqrt N\,\mathcal C_N(0,z,-qr).
 \tag{5}
\]
The norm of \(f_0\) is one and the other three coherent inputs have
norm \(\sqrt N\). Normalizing all four inputs divides (4)'s two
scalars by \(N^{3/2}\). Replacing \(f_0\) by \(R^+\) multiplies
both by \(\sqrt N\). Neither operation changes (4).
The statement includes both parities, composite levels and all
internal first Hermite normals. It makes no assertion outside (2).

## 2. Exact finite source and retained moving poles

Write \(\mathscr F=\mathscr F_N\) for the canonical factorial
of [F, section 2]. We use its proved identities
\[
 \begin{gathered}
 \mathscr F(j)=(Q;Q)_j,\quad
 \mathscr F(w+1)=(1-Q^{w+1})\mathscr F(w),\\
 \mathscr F(w+N)=(1-e^{2\pi iw})\mathscr F(w),\\
 \mathscr F(w)\mathscr F(d-w)=Nq^{w(w-d)},\qquad
 \mathscr F'(N+k)=-2\pi i\,\mathscr F(k)\quad(0\le k<N).
 \end{gathered}
 \tag{6}
\]
Let \(f,h\) be its canonical Stirling functions. Thus
\[
 f'(w)=\operatorname{Log}(1-e^{2\pi iw}),\quad
 \Re f(v)=\mathcal L(v),\quad
 h(w)^2=i(1-e^{2\pi iw}),
 \tag{7}
\]
and, uniformly on full strict vertical strips and bounded real shifts,
\[
 \mathscr F(Nw+\tau)
  =\sqrt N\,h(w)(1-e^{2\pi iw})^\tau
                         e^{Nf(w)}(1+O(N^{-1})).
 \tag{8}
\]
The endpoint half-lines and Gamma comparisons needed below are also
proved in [F, section 2]. In particular, for bounded real part greater
than \(-1\) and \(|\Im v|\le\epsilon N\),
\[
 \mathscr F(v)=(-2\pi i/N)^v\Gamma(v+1)
                   \exp\{O((1+|v|)^2/N)\}.
 \tag{9}
\]
All branches here are the canonical ones, not new principal choices
on the negative imaginary endpoint half-line.

Put
\[
 \begin{gathered}
 B=N(1-c)-\tfrac12,\qquad D=L-Nc+\tfrac12,\\
 W_0(w)=\frac{\mathscr F(w)\mathscr F(B)}
                         {\mathscr F(w+1+B)},\\
 K_a(w)=
 \frac{\mathscr F(w+a-1)}
      {\mathscr F(a-1)\mathscr F(w)}
 \frac{\mathscr F(w+p-a)\mathscr F(p)}
      {\mathscr F(p-a)\mathscr F(w+p)},\qquad
                         T_a(w)=Q^wW_0(w)K_a(w).
 \end{gathered}
 \tag{10}
\]
Specializing the exact finite formula [B, equations (9)--(10)]
at its first coherent parameter equal to zero gives
\[
 \Phi_a^0=\frac{\kappa^2D_N(z)G_N(r)}N
                         \sum_{j=0}^dT_a(j),\qquad
 D_N(z)=1-\eta z^N,\quad G_N(r)=\sum_{j=0}^dr^j .
 \tag{11}
\]
Equivalently the finite sum in (11) has terms
\[
 T_a(j)=
 \frac{Q^j(Q^a,Q^{1-a}/r;Q)_j}
             {(1+qz)(-q^3z,Q/r;Q)_j}.
 \tag{12}
\]
As throughout [B], quotients at exceptional parameters have their
polynomial interpretation. We first prove contour identities off
collisions and then continue the canceled identities.

Choose \(\zeta\) exactly as in [F]: if
\(\delta_*=\min(1/8,a_-/8)\), choose
\(\zeta\in\{-\delta_*,-3\delta_*\}\) with
\(\operatorname{dist}(p+\zeta,\mathbb Z)\ge\delta_*/2\).
Then \(\zeta>-a_-\), and put \(K=\lfloor p+\zeta\rfloor\).
The sample-preserving differential is
\[
 \Omega_a(w)=\frac{\kappa^2G_N(r)}N\,2\pi i
     \frac{1-\eta z^N\tau}{\tau-1}T_a(w)\,dw,
                         \qquad \tau=e^{2\pi iw}.
 \tag{13}
\]
Use \(\zeta<\Re w<N+\zeta\). Its periodic numerator cancels
the entire old outer family from \(\mathscr F(w+1+B)\).
The remaining moving poles are exactly
\[
                       w=L+k,\qquad 0\le k\le K .
 \tag{14}
\]
They are the first zero block of \(\mathscr F(w+p)\).
The first negative pole of \(\mathscr F(w+a-1)\) is \(-a\),
to the left; the other numerator poles are farther left.
There is no second zero block inside this width-\(N\) rectangle.

The horizontal sides vanish. After cancellation of \(\mathscr F(w)\),
the numerator-minus-denominator shift sum in \(T_a\) is
\(-N(1-c)-3/2\). Below, including \(Q^w\), the decay is
\[
             e^{-2\pi(1-c)|\Im w|}e^{-\pi|\Im w|/N}.
 \tag{15}
\]
The degree-one periodic numerator divided by \(\tau-1\) is bounded
there. Above, the decay is \(e^{-2\pi|\Im w|/N}\).
Thus no additional periodic denominator or pole orbit is needed.

For completeness set \(Z=z^N,\rho=r^{-N},a_0=e^{2\pi ia}\).
The exact monodromy is
\[
 \frac{T_a(w+N)}{T_a(w)}
  =\frac{(1-a_0\tau)(1-\rho\tau/a_0)}
          {(1-\eta Z\tau)(1-\rho\tau)} .
 \tag{16}
\]
Consequently the whole paired vertical current is
\[
 \begin{split}
 I_a^0={}&\frac{\kappa^2G_N(r)}N
 \int_{\zeta-i\infty}^{\zeta+i\infty}
 \frac{\tau(A_a+B_a\tau)}{(\tau-1)(1-\rho\tau)}
                                           T_a(w)\,dw,\\
 A_a={}&\eta Z+\rho-a_0-\rho/a_0,\qquad
 B_a=\rho(1-\eta Z).
 \end{split}
 \tag{17}
\]
The coefficient \(B_a\) in this display is distinct from the
factorial argument \(B\). Its numerator is never divided out.

## 3. The current is polynomial and the geometric baseline grows

Here are explicit rate bounds, including the infinite ends. Set
\(\beta=1-c\). The rate of \(W_0(\zeta+iNY)\) is
\[
 R_0(Y)=\Re[f(iY)+f(\beta)-f(\beta+iY)],\qquad R_0(0)=0.
 \tag{18}
\]
The endpoint value uses the canonical continuation in (8)--(9).
For \(k=e^{-2\pi Y}\) put
\(Z_k=1-ke^{-2\pi ic}\), with its continuous argument
in \((-\pi,\pi)\). Direct differentiation gives
\[
 R_0'(Y)=
 \begin{cases}
 \arg Z_k,&Y>0,\\
 \pi+\arg Z_k,&Y<0,
 \end{cases}
 \quad
 R_0(+\infty)=-\mathcal L(c),\qquad
                 R_0(Y)<0\quad(Y<0).
 \tag{19}
\]
Above, the sign of the derivative is the sign of \(\sin2\pi c\).
Below, \(\pi+\arg Z_k\) is uniformly positive on compact \(c\)-sets.
In particular
\[
           R_0(Y)\le\max(0,-\mathcal L(c))\quad(Y\in\mathbb R).
 \tag{20}
\]
The kernel in (17) has bound \(Ce^{-2\pi NY}\) above and \(C\)
below. Since \(|\arg Z_k|<\pi\), its upper rate is at most
\(-\pi Y\); its lower rate is at most \(-c_K|Y|\) for a
compact-dependent \(c_K>0\). Bounded-shift comparisons (8)--(9)
cost only a power of \(N\) and a fixed polynomial in \(|Y|\)
on the finite transition interval. At infinity their powers can
be counted directly: above \(Q^wK_1(w)\) gives \(e^{-2\pi Y}\);
below the residual amplitude is \(e^{\pi Y}\). Thus (17) has a
quantitative integrable majorant
\[
 C N^C(1+|Y|)^C
                    e^{-c_KN|Y|+C|Y|}.
 \tag{21}
\]
The small fixed-shift deformation from \(a=1\) has the same bound,
by (8)--(9). This proves \(I_a^0=O(N^C)\).

Using every residue in (14), (6) gives the exact identity
\[
 \begin{gathered}
 \Phi_a^0=\mathcal G_a^0 S_{N,a}^0+I_a^0,\qquad
 S_{N,a}^0=\sum_{k=0}^K R_k,\\
 R_k=\frac{Q^k(Q^{1-a},rQ^a;Q)_k}
                  {(Q,-q^3rz;Q)_k},\qquad
 \mathcal G_1^0=
           \frac{\kappa^2\mathscr F(B)\mathscr F(L)}{\mathscr F(D)},\\
 \frac{\mathcal G_a^0}{\mathcal G_1^0}
 =-\frac r{1-r}\frac{\mathscr F(p)}{\mathscr F(p-a)}
      \frac{\mathscr F(L+a-1)}{\mathscr F(L)}
      \frac{q^{(N-a)(1-a)}}{\mathscr F(a-1)^2}.
 \end{gathered}
 \tag{22}
\]
The source sign follows from the negative derivative in (6) and
moving the moving-pole residues to the other side of the rectangle.
Before simplification the \(k=0\) factor contains
\((1-e^{-2\pi ia})\mathscr F(-a)\); replace it by
\(\mathscr F(N-a)\), and then reflect with (6). Also cancel
\(G_N(r)/(r^N-1)=-1/(1-r)\). This proves (22) without poles
at positive integer \(a\) or \(r^N=1\). The sole old outer family
was canceled before residues were computed, so collisions with it
also have their full family continuation.

All macroscopic arguments \(B,L,D,p\), with their bounded shifts,
stay strictly between \(0\) and \(N\). Equation (8) therefore gives
\[
 |\mathcal G_1^0|\asymp\sqrt N\,e^{NM_0}.
 \tag{23}
\]
At \(a=1\), \(R_0=1\) and \(R_k=0\) for \(k>0\);
here \(R_0\) denotes the packet coefficient, not the rate (18).
Consequently the baseline actual source differs from the geometric
term by the retained polynomial current. Formula (23) and \(M_0>0\)
prove its nonvanishing. The exact three-input identity is (5);
the Gamma quotient alone is not substituted for that actual source.

## 4. The left packet has a strict upper-end gap

The central packet ratio is
\[
 \mathscr R(v)=\frac{1-v}{1+zv},\qquad
 \chi=-\mathscr R(r)
    =-e^{\pi ic}\frac{\sin\pi R}{\sin\pi(c+R)},\qquad
 1+\chi=e^{-\pi iR}\frac{\sin\pi c}{\sin\pi(c+R)}.
 \tag{24}
\]
Thus \(\arg\chi=-\pi(1-c)\), uniformly away from the negative-real
cut on the chosen compact set. The branch of
\(\log\mathscr R(r)\) is \(i\pi+\log\chi\), of imaginary part
\(\pi c\). The last expression in (24) has argument \(-\pi R\).

Write \(u=1-R,\nu=1-R-c\). The normalized left-line rate is
\[
 V(Y)=\Re[f(u+iY)-f(\nu+iY)-f(u)+f(\nu)]
                                      +2\pi Y\,1_{\{Y<0\}}.
 \tag{25}
\]
Its value at zero is zero, while its upper end is
\[
                         V(+\infty)=-\Delta<0 .
 \tag{26}
\]
To control the entire line, let \(k=e^{-2\pi Y}\) and
\[
 \mathscr R_k=
 \frac{1-ke^{-2\pi iR}}{1-ke^{-2\pi i(R+c)}} .
 \]
At \(k=1\) its continued argument is \(\pi c\), and
\[
 \operatorname{Im}\mathscr R_k
 =\frac{2k\sin\pi c\,[k\cos\pi c-\cos\pi(2R+c)]}
                  {|1-ke^{-2\pi i(R+c)}|^2}.
 \tag{27}
\]
For \(0<k<1\) there is at most one zero of this imaginary part.
If it occurs, it is on the positive real axis: for \(k<1\)
both \(1-ke^{-2\pi iR}\) and \(1-ke^{-2\pi i(R+c)}\) lie
in the open right half-plane, so their argument difference cannot
equal \(\pm\pi\). The affine numerator in (27) is positive at
\(k=1\); a crossing as \(k\) decreases can only change its sign
from positive to negative. Thus as \(Y\) increases the argument
changes from positive to negative there. Since
\(V'=-\arg\mathscr R_k\), this is a minimum, never a maximum.
Otherwise \(V\) is decreasing. These assertions also follow
directly when \(\cos\pi c=0\). For \(k>1\), the continued
argument stays in \((0,2\pi)\), tending to \(2\pi c\):
at any real crossing the real numerator after clearing the
denominator in (27) is \(1-k^2<0\), so no positive-real
crossing can leave that argument interval.
Hence \(V'=2\pi-\arg\mathscr R_k>0\) below zero.
Together with (26), this proves
\[
 V(Y)<0\ (Y\ne0),\qquad
 \sup_{|Y|\ge\epsilon}V(Y)\le-\delta_\epsilon<0 .
 \tag{28}
\]
The last bound is uniform on the fixed compact sets. Below, \(V\)
also decreases at least linearly toward negative infinity.
The condition \(\Delta>0\) is used exactly at the upper infinite
end; it has not been inferred merely from \(M_0>0\).

## 5. Finite Barnes evaluation, with the right connector retained

Choose an integer \(\ell\ge a_+\). For fixed \(0\le k\le\ell\),
\[
 R_k=r_k+O(N^{-1}),\qquad
 r_k=\frac{(1-a)_k(-\chi)^k}{k!}
                              =\binom{a-1}{k}\chi^k .
 \tag{29}
\]
This holds uniformly at the integer zeros of the finite products.
Remove the first \(\ell\) terms and define explicitly
\[
 T_N(v)=Q^v
 \frac{\mathscr F(v+\ell-a)\mathscr F(\ell)}
      {\mathscr F(\ell-a)\mathscr F(v+\ell)}
 \frac{\mathscr F(L+a+\ell-1+v)}{\mathscr F(L+a+\ell-1)}
 \frac{\mathscr F(D+\ell)}{\mathscr F(D+\ell+v)}.
 \tag{30}
\]
Then \(R_{k+\ell}=R_\ell T_N(k)\), including when \(R_\ell=0\);
the displayed interpolation is not defined by division by that
coefficient.

With \(\gamma=-1/4,\ \beta_N=p+\zeta-\ell\), use
\(\mathcal B(v)=2\pi i/(e^{2\pi iv}-1)\) on the rectangle
\(\gamma<\Re v<\beta_N\). Its only poles are samples
\(0,\ldots,K-\ell\). The first negative pole of the light
numerator is at \(a-\ell-1\le-1\). The other numerator poles
are farther left. Both denominator zero blocks start strictly
to the right of this rectangle. The numerator-minus-denominator
shift sum is \(Nc-3/2\). Below, the Barnes kernel and \(Q^v\)
leave decay
\[
             e^{-2\pi(1-c)|\Im v|}e^{-\pi|\Im v|/N};
 \tag{31}
\]
above the decay is \(e^{-2\pi|\Im v|/N}\).
Thus the exact finite identity, with both vertical integrals upward, is
\[
 \begin{gathered}
 S_{N,a}^0=\sum_{k=0}^{\ell-1}R_k+
                  R_\ell(J_{\rm right}-J_{\rm left}),\\
 J_{\rm line}=\frac1{2\pi i}\int_{\rm line}
                                     \mathcal B(v)T_N(v)\,dv .
 \end{gathered}
 \tag{32}
\]

On the central left line, for \(|\Im v|\le\epsilon N\),
(8)--(9) give
\[
 T_N(v)=e^{i\pi v}\chi^v
 \frac{\Gamma(v+\ell+1-a)\Gamma(\ell+1)}
      {\Gamma(\ell+1-a)\Gamma(v+\ell+1)}
                  \exp\{O((1+|v|)^2/N)\}.
 \tag{33}
\]
After multiplication by \(\mathcal B\), the model is bounded by
\(C(1+|\Im v|)^C e^{-\delta|\Im v|}\), uniformly since
\(-\pi<\arg\chi<0\). Choose \(\epsilon\) sufficiently small.
The error exponential is absorbed by half this decay, and its
integrated error is \(O(N^{-1})\).

For \(v=\gamma+iNY,\ |Y|\ge\epsilon\), full-strip estimates give
the quantitative bound
\[
 |\mathcal B(v)T_N(v)|
 \le C N^C e^{NV(Y)}
 \begin{cases}
 e^{-\pi Y},&Y\ge\epsilon,\\
 e^{\pi Y/2},&Y\le-\epsilon .
 \end{cases}
 \tag{34}
\]
Here is the fixed-shift count behind the integrable factors.
Above, all factorial height amplitudes tend to constants and
\(Q^v\) supplies \(e^{-2\pi Y}\). Below, the light ratio supplies
\(e^{2\pi aY}\), the macroscopic shifted ratio supplies
\(e^{-2\pi(a-3/2)Y}\), and \(Q^v\) supplies \(e^{-2\pi Y}\).
Their product is \(e^{\pi Y}\). The Barnes exponential below
is already included in (25). Reducing these decay constants by
one half absorbs bounded-height transitions and uniformly bounded
Stirling remainders. Equations (28), (34) bound this whole left
tail by \(CN^Ce^{-\delta_\epsilon N}\), including \(dv=iN\,dY\).

The right line has \(v=p+\zeta-\ell+iNY\).
Its sole macroscopic numerator crossing \(N\) is
\(\mathscr F(N+a+\zeta-1+iNY)\). Shift it once by \(N\)
using (6). Above its periodic factor has zero rate; below
its rate is \(-2\pi Y\), exactly canceled by the Barnes
kernel's rate \(2\pi Y\). The remaining normalized rate on
**both** half-lines is therefore
\[
                            R_0(Y)-M_0 .
 \tag{35}
\]
By (20) it is at most
\[
 -\gamma_0,\qquad
 \gamma_0=\min(M_0,M_0+\mathcal L(c))
                         =\min(M_0,\Delta)>0 .
 \tag{36}
\]
For \(|Y|\ge\epsilon\), the same fixed-shift count as in
(34) gives its integrable majorant with
\(e^{-\gamma_0N}\) in place of \(e^{NV}\).
For \(|Y|\le\epsilon\), the sole endpoint numerator has real
shift \(a+\zeta-1>-1\); (9) and its fixed-shift Gamma comparison
give a cost \(N^C(1+N|Y|)^Ce^{C|Y|}\).
The remaining factors use (8), still with rate (35).
Thus the whole connector satisfies
\[
                         |J_{\rm right}|
                             \le CN^Ce^{-\gamma_0N}.
 \tag{37}
\]
This is a relative exponential gap, not an assertion that the
un-normalized connector is a polynomial error.

The central model evaluates without a restriction on \(|\chi|\).
Reflection of the ordinary Gamma factor gives
\[
 \begin{split}
 -J_{\rm left}
  &=\frac1{2\pi i}\int_{\gamma-i\infty}^{\gamma+i\infty}
 \frac{\Gamma(-v)\Gamma(v+\ell+1-a)\Gamma(\ell+1)\Gamma(v+1)}
      {\Gamma(\ell+1-a)\Gamma(v+\ell+1)}
                                  \chi^v\,dv+O(N^{-1})\\
  &=\ell\int_0^1(1-x)^{\ell-1}
                    (1+\chi x)^{a-\ell-1}\,dx+O(N^{-1}).
 \end{split}
 \tag{38}
\]
First prove this at \(|\chi|<1\) by the ordinary binomial residues
and the beta integral. Continue the identity through the lower
half-plane, where the Gamma Barnes integral has uniform vertical
decay on compact sets. The Euler integral has its usual larger
domain \(\mathbb C\setminus(-\infty,-1]\). Our \(\chi\) stays
in a compact subset of the lower half-plane, so this proves (38)
with its specified branch. Taylor's integral remainder now gives
\[
 \sum_{k=0}^{\ell-1}r_k+
 r_\ell\ell\int_0^1(1-x)^{\ell-1}(1+\chi x)^{a-\ell-1}\,dx
                                  =(1+\chi)^{a-1}.
 \tag{39}
\]
No division by an integer-zero coefficient occurs. Combining
(29), (32)--(39) proves
\[
                 S_{N,a}^0=(1+\chi)^{a-1}(1+O(N^{-1})).
 \tag{40}
\]
The model is complex but bounded away from zero on our compact
sets, and at \(a=1\) the packet identity is exactly one.

## 6. Prefactor, source-relative error, and scope

The pole-free amplitude ratio in (22), with (8)--(9), is exactly
the one evaluated in [F]. For clarity, its two macroscopic factors
give \((1-r^{-1})^a(1-r)^{a-1}\); the endpoint factor is
\[
 \mathscr F(a-1)=(-2\pi i/N)^{a-1}\Gamma(a)(1+O(N^{-1})).
 \]
Use \(-r(1-r^{-1})/(1-r)=1\). The remaining endpoint phase is
canceled by \(q^{(N-a)(1-a)}\). Consequently
\[
 \frac{\mathcal G_a^0}{\mathcal G_1^0}
 =\frac{N^{2a-2}}{\Gamma(a)^2}
          \left(\frac{\sin\pi R}{\pi}\right)^{2a-2}
                                         (1+O(N^{-1})).
 \tag{41}
\]
Equations (21)--(23), (40)--(41) control every error relative to
the growing actual baseline. The packet contributes the factor
\((1+\chi)^{a-1}\), whose phase is \(-\pi R(a-1)\), by (24).
This proves (4), including its full phase, not just its modulus.
The prefactor and current identities continue through integer
\(a\), the roots \(r^N=1\), and all old outer-pole collisions.

The strict upper-end loss in (26) is essential to this proof.
No result is claimed when \(\Delta\le0\), nor is a signed packet
replaced by its termwise modulus. The result is boundary-layer
data for a literal crossing-leaf observation. It does not by
itself transport to a fixed positive boundary angle, evaluate
an arbitrary short component, or prove a knot-volume or
finite-exception theorem.

The complete direct proof texts are:

| Label | Complete source | SHA-256 |
|---|---|---|
| B | notes/research_four_coherent_boundary_polynomial_source.md | 93241074830ff4b844ba5baafd06a15bf08ec6bddc3a1498727f110ebe297d84 |
| F | notes/research_four_coherent_fractional_boundary_source.md | 8126481cadaa4b1b0ba287495de14cb3263baf8343fbfca9aa4d5b6d962595b1 |

Both entire matching proof texts are retained at their renewed pins.
The earlier zero-radius three-input source is already treated in
research_single_leg_radial_turn_source.md; the present proof computes
the additional fractional four-input packet and both of its currents.
Only written mathematics and text operations were used.
