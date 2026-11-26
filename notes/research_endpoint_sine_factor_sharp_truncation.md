# Sine-factor endpoint modes with the sharp truncation rate

Private written proof, 16 November 2026.

The normalized factorial interpolation gives exact first-order
sine-ratio factors for the unturned endpoint equation. Their ordinary
lowering relation produces a finite approximate homogeneous basis.
On a buffered bulk rectangle of any fixed height this basis is
bounded, and its optimally truncated residual has the sharp real
product rate \(J_*\). Its two coefficients can be fixed by an actual
physical value packet. The independent normal packet is retained
separately; no sharper source-normal compatibility is inferred.

## 1. The normalized first-order factors

Put \(h=N^{-1}\), \(\theta=\pi h\), and
\[
 s_\zeta=2\sin(\pi h\zeta),\qquad
 c_\zeta=2\cos(\pi h(2\zeta+1)),\qquad
 c_N(x)=2\cos(2\pi x+\pi h).
 \tag{1}
\]
The ordinary source operator is
\[
 \mathscr J_N f=(c_0+A_N+B_N)f-A_Nf(x+h)-B_Nf(x-h),
\]
\[
 A_N(x)=\frac{s_{Nx+1}^4}{s_{2Nx+1}s_{2Nx+2}},\qquad
 B_N(x)=\frac{s_{Nx}^4}{s_{2Nx}s_{2Nx+1}}.
 \tag{2}
\]
We use the factorial source's specified zero-free interpolation
\[
 G_N(t)=\left(\frac{2\pi}{N}\right)^t\Gamma(t+1)
 \prod_{k\ge1}
 \frac{\Gamma(Nk+t+1)}
      {\Gamma(Nk-t)(Nk)^{2t+1}},
 \qquad -1<\Re t<N.
 \tag{3}
\]
Its logarithm is fixed by the positive real normalization. The
convergent product proves, without a periodic multiplier,
\[
 G_N(t+1)=2\sin(\pi(t+1)/N)G_N(t),\qquad G_N(0)=1.
 \tag{4}
\]
Define
\[
 \mathcal F_{\zeta,N}(x)
     =4^{-\zeta}\frac{G_N(Nx+\zeta)}{G_N(Nx-\zeta)}.
 \tag{5}
\]
The power of \(4\) uses its real logarithm. For bounded \(\zeta\)
and any fixed compact subset of \(0<\Re x<1\), (5) is holomorphic
and nonzero for all sufficiently large \(N\). Its exact ratio is
\[
 \frac{\mathcal F_{\zeta,N}(x+h)}{\mathcal F_{\zeta,N}(x)}
   =\frac{\sin\pi(x+(\zeta+1)h)}
          {\sin\pi(x+(1-\zeta)h)}=:R_{\zeta,N}(x).
 \tag{6}
\]

On the same compact sets, the factorial source proves
\[
 \log G_N(Nx)
 =N\mathcal J(x)+\tfrac12\Log(2N\sin\pi x)
              +\frac{\pi\cot\pi x}{12N}+O_{\rm hol}(N^{-3}),
 \quad \mathcal J'(x)=\Log(2\sin\pi x).
 \tag{7}
\]
The logarithm is continued from \(0<x<1\). Substituting
\(x\pm\zeta h\) in (7) gives
\[
 \mathcal F_{\zeta,N}(x)
 =(\sin\pi x)^{2\zeta}
       \{1+\zeta\pi h\cot\pi x+O_{\rm hol}(h^2)\}
 =(\sin\pi(x+h/2))^{2\zeta}\{1+O_{\rm hol}(h^2)\}.
 \tag{8}
\]
All fixed parameter and spatial derivatives have the corresponding
bounds on smaller compact sets. The exact function in (5), rather
than its asymptotic, is used below.

## 2. Ordinary lowering and finite cancellation

The original rational sine identity for the Newton lowering rule
continues in its index \(\zeta\). Substitution of (6) and its backward
ratio in (2) gives
\[
 \frac{\mathscr J_N\mathcal F_{\zeta,N}}{\mathcal F_{\zeta,N}}
 =c_\zeta-
       \frac{s_\zeta^4}{s_{Nx+\zeta}s_{Nx-\zeta+1}}.
 \tag{9}
\]
This can also be checked by the source's denominator-cleared identity,
with its variable \(q^{2k}\) replaced by \(q^{2\zeta}\).
By (4),
\[
 \frac{\mathcal F_{\zeta-1,N}}{\mathcal F_{\zeta,N}}
       =\frac4{s_{Nx+\zeta}s_{Nx-\zeta+1}}.
\]
Consequently the exact ordinary lowering equation is
\[
 \boxed{\quad
 \mathscr J_N\mathcal F_{\zeta,N}
       =c_\zeta\mathcal F_{\zeta,N}
                         -\frac{s_\zeta^4}{4}\mathcal F_{\zeta-1,N}.
 \quad} \tag{10}
\]
No quotient or restriction to physical values occurs in this identity.

Fix \(A<\infty\) and \(0<\epsilon<\pi\), and take the parameter set
\[
 |\Re\alpha|\le A,\qquad |\Im\alpha|\le\pi-\epsilon,\qquad
 z_\pm=-\tfrac12\pm\frac{i\alpha}{2\pi},\qquad
 w=2\cosh(\alpha h)=c_{z_\pm}.
 \tag{11}
\]
Slightly larger parameter sets of the same kind are reserved for
derivatives. In particular \(-1<\Re z_\pm<0\), with uniform margins.
For either \(z=z_\pm\), let
\[
 a_0(z)=1,\qquad
 \frac{a_k(z)}{a_{k-1}(z)}
   =\frac{s_{z-k+1}^4}{4(c_{z-k}-c_z)}
   =\frac{s_{z-k+1}^4}{4s_k s_{2z+1-k}},
 \qquad
 U_{m,N}(z,x)=\sum_{k=0}^m a_k(z)\mathcal F_{z-k,N}(x).
 \tag{12}
\]
For \(m\le\delta N\) with fixed \(\delta<1/2\), these denominators
are nonzero for all large \(N\), uniformly on (11). Indeed \(k\ge1\)
and \(\Re(2z+1)\) stays strictly between \(-1\) and \(1\).
The finite sum telescopes under (10):
\[
 \boxed{\quad
 (\mathscr J_N-w)U_{m,N}(z,x)
       =-\frac{a_m(z)s_{z-m}^4}{4}\mathcal F_{z-m-1,N}(x).
 \quad} \tag{13}
\]
The individual mode construction is not extended here across its
other complex-index resonances. Coalescence at \(\alpha=0\) is
regular and is handled in section 4.

## 3. The sharp product estimate at arbitrary fixed height

Fix \(x_0\in(0,1/2)\), and put
\[
 \delta=\delta(x_0)
       =\frac1\pi\arcsin\frac{\sin(\pi x_0)}{\sqrt2},\qquad
 m=\lfloor\delta N\rfloor.
 \tag{14}
\]
Thus \(0<\delta<x_0\). Choose a sufficiently small real interval
\([a,b]\) about \(x_0\), with larger fixed buffers, such that
\(\delta<a<b<1/2\). The interval will be shrunk once below.
The imaginary coordinate may range over any fixed bounded interval,
with additional buffers for derivatives.
Since \(\delta<a\) and \(b+\delta<1\), all arguments
\(Nx\pm(z-k)\), \(0\le k\le m+1\), remain in the zero-free strip
of (3) for large \(N\). Thus every function in the finite sum and
its final lowering term is defined there by the same normalization.

Write \(T_k=a_k(z)\mathcal F_{z-k,N}(x)\). The exact summand ratio is
\[
 \frac{T_k}{T_{k-1}}
 =\frac{s_{z-k+1}^4}
 {s_k s_{2z+1-k}
  s_{Nx+z-k+1}s_{Nx-z+k}}.
 \tag{15}
\]
For \(0\le v<X<1/2\), define
\[
 \mathcal I_v(X)=
  \int_0^v\log\frac{\sin^2(\pi X)-\sin^2(\pi u)}
                         {\sin^2(\pi u)}\,du.
 \tag{16}
\]
The logarithmic singularity at zero is integrable.
For \(x=X+iY\), the unshifted spatial denominator has the exact bound
\[
 \begin{split}
 &|\sin\pi(X-v+iY)\sin\pi(X+v+iY)|^2\\
 &\quad=
 [\sin^2\pi(X-v)+\sinh^2\pi Y]\,
 [\sin^2\pi(X+v)+\sinh^2\pi Y]\\
 &\quad\ge[\sin^2(\pi X)-\sin^2(\pi v)]^2.
 \end{split} \tag{17}
\]
Both spatial sine factors are uniform units when \(v\le\delta\)
on the chosen rectangle. Their bounded \(z h\) shifts change
their product by a factor bounded by \(e^{Ch}\).

Uniformly for \(1\le k\le m\), the first two denominator factors
in (15) give
\[
 \left|\frac{s_{z-k+1}^4}{s_k s_{2z+1-k}}\right|
      \le s_k^2(1+C/k).
 \tag{18}
\]
For large fixed \(k\), this follows from the sine mean-value estimate,
\(s_k\ge c k/N\), and bounded \(z\). The finitely many smaller \(k\)
are covered by the nonresonance margins in (11), increasing \(C\).
Equations (15)--(18) imply
\[
 \left|\frac{T_k}{T_{k-1}}\right|
 \le (1+C/k)e^{Ch}
       \frac{\sin^2(\pi k h)}
            {\sin^2(\pi X)-\sin^2(\pi k h)}.
 \tag{19}
\]
The base term \(\mathcal F_{z,N}\) and its reciprocal are uniformly
bounded on every chosen fixed-height rectangle.
The logarithm of the last ratio is \(2\log u\) plus a smooth
function on \(0\le u\le\delta\). Summing \(2\log(k/N)\) using the
elementary factorial bounds, and using a Riemann sum for the smooth
part, yields uniformly for \(0\le k\le m\)
\[
 |T_k(x)|\le C N^p\exp\{-N\mathcal I_{kh}(X)\}.
 \tag{20}
\]
The floor, the product of \(1+C/k\), and the endpoint factorial
error cost only powers of \(N\).

The integrand in (16) decreases through zero once, at
\(v=\delta(X)\). Therefore \(v\mapsto\mathcal I_v(X)\) first
increases and then decreases. At \(X=x_0\), its value at
\(v=\delta\) is strictly positive. Shrink the real interval so that
\(\mathcal I_\delta(X)>c>0\) throughout it. It follows that
\(\mathcal I_v(X)\ge0\) for every \(0\le v\le\delta\).
Equation (20) bounds the whole finite sum polynomially.

In fact,
\[
                    U_{m,N}(z,x)=\mathcal F_{z,N}(x)
                                      +O_{\rm hol}(h^2).
 \tag{21}
\]
To prove this stronger statement, choose a small fixed \(\rho>0\)
below every \(\delta(X)\) in the real interval. The first summand
ratio is \(O(h^2)\); for \(k\le\rho N\), the exact ratios are bounded
by \(C(k+C)^2/N^2\), and hence by a fixed \(q<1\) after reducing
\(\rho\). This part of the sum is \(O(h^2)\).
For \(\rho\le kh\le\delta\), (16) has a uniform positive lower
bound, so (20) makes the rest exponentially small. Apply Cauchy's
formula on larger fixed rectangles and parameter sets to obtain
every fixed derivative in (21).

The multiplier relating the last term in (13) to \(T_m\) is
\[
          \frac{s_{z-m}^4}{s_{Nx+z-m}s_{Nx-z+m+1}},
 \tag{22}
\]
which is bounded on those same rectangles. Consequently, for all
fixed nonnegative \(r,s\),
\[
 \boxed{\quad
 |\partial_x^r\partial_\alpha^s
          [(\mathscr J_N-w)U_{m,N}(z_\pm,x)]|
       \le C_{r,s}N^{p_{r,s}}
                    e^{-N\mathcal I_\delta(\Re x)}.
 \quad} \tag{23}
\]
For spatial derivatives, apply the preceding bounds on disks of
radius \(c/N\). The rate in (16) is smooth on the real buffer,
so its variation on such a disk costs only a bounded factor.
Parameter derivatives use a larger fixed set as in (11).
This preserves the displayed exponential rate.

At the target real part, the exponent is exactly the archived
optimized product rate:
\[
 \boxed{\quad
 \mathcal I_{\delta(x_0)}(x_0)
             =J_*(\pi-2\pi x_0).
 \quad} \tag{24}
\]
For a direct verification, let \(I(X)=\mathcal I_{\delta(X)}(X)\).
The endpoint term in its derivative is zero. Substitution
\(y=\tan(\pi u)\) gives
\[
 I'(X)=2\operatorname{atanh}
        \frac{\cos(\pi X)}{\sqrt{1+\cos^2(\pi X)}}
       =2\operatorname{asinh}(\cos\pi X).
 \tag{25}
\]
Also \(I(X)\to0\) as \(X\downarrow0\), by scaling \(u=Xv\)
in its integrable logarithm. The pinned diagnostic has
\[
 J_*(t)=\frac1\pi\int_t^\pi\operatorname{asinh}(\sin(s/2))\,ds,
\]
which proves (24), including its constant.

## 4. A basis regular at the parameter coalescence

Let \(\nu=\alpha/\pi\), and use the same cutoff for both signs:
\[
 H_{0,N}=\frac{U_{m,N}(z_+,x)+U_{m,N}(z_-,x)}2,\qquad
 H_{1,N}=\frac{U_{m,N}(z_+,x)-U_{m,N}(z_-,x)}{2i\nu}.
 \tag{26}
\]
The second expression is defined by its removable value at zero.
The functions are jointly holomorphic. Equations (8) and (21) give
\[
 H_{0,N}=\frac{\cos(\nu\log\sin\pi x)}{\sin\pi x}+O_{\rm hol}(h),
 \qquad
 H_{1,N}=\frac{\sin(\nu\log\sin\pi x)}
                      {\nu\sin\pi x}+O_{\rm hol}(h).
 \tag{27}
\]
The sine quotient has its logarithmic value at \(\nu=0\).
Cauchy's formula in \(\alpha\) proves the uniform removable bounds
in (27) and (23). Since both modes have the same \(w\), their
residuals still obey (23).

The limiting Wronskian is
\[
 W(H_{0,N},H_{1,N})
             =\frac{\pi\cos\pi x}{\sin^3\pi x}+O_{\rm hol}(h),
 \tag{28}
\]
which is a uniform unit on each of the fixed rectangles above.
The corresponding balanced frame
\[
 \mathcal Y_N(x)=
 \begin{pmatrix}
 H_{0,N}(x)&H_{1,N}(x)\\
 h^{-1}(H_{0,N}(x)-H_{0,N}(x-h))&
 h^{-1}(H_{1,N}(x)-H_{1,N}(x-h))
 \end{pmatrix}
 \tag{29}
\]
and its inverse are uniformly bounded on smaller rectangles.
This gives two genuine, explicitly normalized analytic approximate
modes. No diagonal Floquet eigenline, periodic scalar continuation,
or exact homogeneous correction is being asserted.

## 5. An actual two-value connection and the retained normal packet

Let \(F_j=K_N(w,c_j)\) on the physical bulk, and put
\[
 X_j=(F_j,h^{-1}(F_j-F_{j-1}))^t.
 \tag{30}
\]
Choose a right physical anchor \(j_*\) in the real buffer and define
the actual coefficients and scalar comparison by
\[
 \mathbf a_N(\alpha)=\mathcal Y_N(x_{j_*})^{-1}X_{j_*},
 \qquad
 V_N(x,\alpha)=(H_{0,N}(x),H_{1,N}(x))\mathbf a_N(\alpha).
 \tag{31}
\]
The original physical-row bounds give \(\|\mathbf a_N\|\le CN^p\),
uniformly on (11); these coefficients are holomorphic there.
Both values \(F_{j_*}\) and \(F_{j_*-1}\) are matched exactly.

For clarity, the balanced original transfer and forcing vector are
\[
 T_N=\begin{pmatrix}1+d_N&h q_N\\d_N/h&q_N\end{pmatrix},
 \quad q_N=B_N/A_N,\quad d_N=(c_0-w)/A_N,\quad
 b_N=A_N^{-1}(1,h^{-1})^t.
 \tag{32}
\]
Thus \(X_f(x+h)=T_N(x)X_f(x)-b_N(x)(\mathscr J_N-w)f(x)\).
On the buffered real interval, \(T_N^{\pm1}=I+O(h)\).
The actual physical values satisfy the homogeneous recurrence,
whereas \(V_N\) has residual \(r_V=(\mathscr J_N-w)V_N\)
bounded by (23) with a polynomial loss from (31).
Backward variation of constants from the exact two-value anchor gives
\[
 \boxed{\quad
 \|X_j-X_{V_N}(x_j)\|
           \le CN^p e^{-N\mathcal I_\delta(x_j)}
                      \qquad(x_j\in[a,b],\ j\le j_*).
 \quad} \tag{33}
\]
Indeed the balanced propagators are bounded, there are \(O(N)\)
forcing terms, and \(\mathcal I_\delta(X)\) is increasing in \(X\)
for \(\delta<X<1/2\), directly from (16).

The corresponding first-normal statement retains additional data.
Use the ordinary \(x\)-derivative of the full kernel for the actual
normal state, and set \(Z_f=(X_f,\partial_xX_f)^t\).
At bulk physical rows the ordinary kernel source and its first
derivative vanish. With
\[
 \mathcal T_N=\begin{pmatrix}T_N&0\\T_N'&T_N\end{pmatrix},
 \qquad
 \mathcal R_N(r)=\binom{b_Nr}{b_N'r+b_Nr'},
\]
the exact difference \(E=K_N(w,c_N(\cdot))-V_N\) therefore obeys
\[
 Z_E(x_j)=\Phi_{j,j_*}Z_E(x_{j_*})
             -\sum_{l=j}^{j_*-1}\Phi_{j,l+1}\mathcal R_N(r_V)(x_l).
 \tag{34}
\]
Here \(\Phi_{j,k}\) is the homogeneous propagator of
\(\mathcal T_N\), with inverse products for \(j<k\); all neighboring
arguments stay inside the fixed real buffer.
Its first two anchor entries vanish by (31); its last two entries
are the actual independent normal mismatch. Consequently
\[
 \|Z_E(x_j)\|\le C\|Z_E(x_{j_*})\|
                       +CN^p e^{-N\mathcal I_\delta(x_j)}.
 \tag{35}
\]
Division by the bulk unit \(c_N'(x_j)\) translates this to spectral
normals. Formula (35) neither resets nor estimates its normal anchor.
It also does not control the actual fractional-grid packet of a
separately normalized baseline. In particular (23), (33), and (35)
do not supply that baseline's optimized full-normal Green budget.

All currents, endpoint rows, shared spectators, and source coefficients
outside these stated comparisons remain unchanged. There is no
filled-action estimate, scalar noncancellation claim, or assertion
that the approximate basis has the full physical jets.

## 6. Coverage and direct sources

The continuum sine-power modes and their leading value connection
constants were already known. The exact factorial interpolation was
also available. The additional step here is its ordinary descending
index expansion (12), the uniform tall-rectangle estimate for that
specific finite sum, and the identity of its optimal residual rate
with \(J_*\). The actual two-value normalization (31) retains the
normal datum that the sharp residual alone does not determine.

The following complete source texts were read, with their used
identities and final pins checked:

* [Normalized factorial interpolation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/exact_factorial_interpolation_and_complex_contours.md),
  SHA256 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72.
* [Ordinary edge-kernel lowering and source](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_edge_kernel_difference_and_endpoint_bound.md),
  SHA256 5d0d07d4d97d82cca66e0e0c3bf2cecad8e5f58ef8329178278b297cf0d6c5da.
* [Actual complex baseline and optimized product diagnostic](research_unturned_endpoint_complex_baseline_and_window.md),
  SHA256 9d233d9bb11c2842e62d5523f97e9621a3bd22532e3b527ceaab8125782c1cc1.
* [Retained full-normal Green budget](research_partial_endpoint_green_boundary_budget.md),
  SHA256 a1bbfaa8f64abca96d2b97078a9d87fbc60877b4f4791612b1e8e2d822be286e.

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical experiment, test, build or
compilation was run. Existing adopted and public notes are unchanged.
