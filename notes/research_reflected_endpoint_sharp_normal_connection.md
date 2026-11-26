# Reflection gives the sharp physical normal connection

Private written proof, 16 November 2026.

The sine-factor approximate modes admit a regular divided-color frame
through the middle fold. Exact reflection of that frame, together with
the original recurrence, determines the derivative of the actual
connection coefficients to the sharp truncation accuracy. Thus the
same two-value normalization now approximates both physical values and
first spectral normals at that rate. The result concerns the actual
physical jets; it does not compare an unrelated off-grid baseline or
estimate a filled current.

## 1. Parameters, modes and statement

Put \(h=N^{-1}\), \(N\ge2\), and
\[
 s_z=2\sin(\pi hz),\quad c_z=2\cos(\pi h(2z+1)),\quad
 C_N(x)=2\cos(2\pi x+\pi h),\quad
 w=2\cosh(\alpha h),\quad P_N(C)=2T_N(C/2)+2.
 \tag{1}
\]
Here \(T_N\) is the Chebyshev polynomial. The ordinary kernel is
\[
 K_N(w,C)=\sum_{k=0}^{N-1}e_k(w)e_k(C),\qquad
 e_k(C)=\frac{\prod_{j<k}(c_j-C)}{\prod_{j=1}^k s_j^2},
 \qquad u_N(x)=K_N(w,C_N(x)).
 \tag{2}
\]
Fix a compact parameter rectangle
\[
 |\Re\alpha|\le A,\qquad |\Im\alpha|\le\pi-\epsilon,
 \quad 0<\epsilon<\pi,
 \qquad z_\pm=-\tfrac12\pm\frac{i\alpha}{2\pi}.
 \tag{3}
\]
Larger rectangles of the same kind are reserved for derivatives.
This includes coalescence at zero. No continuation of the individual
mode coefficients through their other index resonances is assumed.

Fix \(x_0\in(0,1/2)\), and let
\[
 \delta=\frac1\pi\arcsin\frac{\sin(\pi x_0)}{\sqrt2},
 \qquad m=\lfloor\delta N\rfloor,
\]
\[
 I_\delta(X)=\int_0^\delta
       \log\frac{\sin^2(\pi X)-\sin^2(\pi v)}
                     {\sin^2(\pi v)}\,dv,
                 \qquad \delta<X<1-\delta.
 \tag{4}
\]
Choose \(\delta<a<x_0<b<b_*<1/2\), sufficiently close to
\(x_0\), with fixed larger buffers such that \(I_\delta(a)>0\).
All intervals below have those buffers. In particular the symmetric
extension around \([a,1-a]\) remains inside \((\delta,1-\delta)\)
and has a positive minimum of \(I_\delta\).

Use the specified Gamma-product factorial
\[
 G_N(t)=\left(\frac{2\pi}{N}\right)^t\Gamma(t+1)
 \prod_{k\ge1}\frac{\Gamma(Nk+t+1)}
                      {\Gamma(Nk-t)(Nk)^{2t+1}},
                         \qquad -1<\Re t<N,
 \tag{5}
\]
and the finite modes of the sharp truncation source:
\[
 F_z(x)=4^{-z}\frac{G_N(Nx+z)}{G_N(Nx-z)},\qquad
 a_0(z)=1,\quad
 \frac{a_k(z)}{a_{k-1}(z)}
             =\frac{s_{z-k+1}^4}{4(c_{z-k}-c_z)},
\]
\[
 U(z,x)=\sum_{k=0}^{m}a_k(z)F_{z-k}(x),\quad \nu=\alpha/\pi,
\]
\[
 H_0(x)=\frac{U(z_+,x)+U(z_-,x)}2,\qquad
 H_1(x)=\frac{U(z_+,x)-U(z_-,x)}{2i\nu}.
 \tag{6}
\]
The last quotient has its removable value at zero.

Define the divided-color state and mode frame by
\[
 \Delta_N(x)=C_N(x)-C_N(x-h)
                         =-4\sin(2\pi x)\sin(\pi h),
\]
\[
 \mathcal V_f(x)=
    \binom{f(x)}{[f(x)-f(x-h)]/\Delta_N(x)},\qquad
 \mathcal F_N(x)=
    \bigl(\mathcal V_{H_0}(x),\mathcal V_{H_1}(x)\bigr).
 \tag{7}
\]
The removable meaning at the fold is proved below. Choose a physical
anchor \(x_{j_*}=j_*/N\in[b,b_*]\), and put
\[
 \mathbf a_* =\mathcal F_N(x_{j_*})^{-1}\mathcal V_{u_N}(x_{j_*}),
 \qquad V_N(x)=(H_0(x),H_1(x))\mathbf a_*.
 \tag{8}
\]
This is exactly the two-value normalization: the two rows in (7)
are obtained from the two values by an invertible change of basis
at this anchor, which is separated from the fold.

**Theorem.** For all large \(N\), (8) is defined and holomorphic
in (3). Its coefficients are polynomially bounded in \(N\).
For every fixed nonnegative parameter derivative order \(q\),
there are \(C,p\), uniform on the specified windows, such that
at every physical \(x_j=j/N\in[a,b]\),
\[
 \boxed{\quad
 |\partial_\alpha^q(u_N(x_j)-V_N(x_j))|
 +|\partial_\alpha^q(u_N'(x_j)-V_N'(x_j))|
             \le CN^p e^{-NI_\delta(x_j)}.
 \quad}                                                     \tag{9}
\]
Primes mean ordinary \(x\)-derivatives. Since \(C_N'\) is a
uniform unit on this target bulk interval, (9) gives the same
bound for the original first spectral normal, with
\(V_N'(x_j)/C_N'(x_j)\) as its comparison.

On every fixed-height buffered rectangle over \([a,b]\),
\(V_N\) and its fixed derivatives are polynomially bounded,
and its ordinary residual obeys
\[
 |\partial_x^r\partial_\alpha^q
                 (\mathscr J_N-w)V_N(x)|
       \le CN^p e^{-NI_\delta(\Re x)}.
 \tag{10}
\]
At \(x_j=x_0+O(N^{-1})\), the exponent in (9) is
\[
        I_\delta(x_j)=J_*(\pi-2\pi x_0)+O(N^{-1}).
 \tag{11}
\]
Thus both physical jets have the sharp optimized rate at the target.

## 2. Exact reflection and extension of the mode estimates

The normalized factorial has the exact reflection identity
\[
                         G_N(t)G_N(N-1-t)=N.
 \tag{12}
\]
For completeness, the canonical factorial source proves
\[
 \frac{G_N'(t)}{G_N(t)}
    =\frac{\pi}{N^2}\sum_{k=0}^{N-1}
                       (t-k)\cot\frac{\pi(t-k)}N.
\]
Its right side is unchanged under \(t\mapsto N-1-t\), by
reversing \(k\). Hence the logarithmic derivative of the product
in (12) vanishes. At \(t=0\), the normalization and the exact
shift law give \(G_N(0)G_N(N-1)=N\). Meromorphic continuation
proves (12) with no undetermined periodic multiplier.

Let \(R_Nx=1-h-x\). Applying (12) to the numerator and
denominator of each \(F_z\) gives
\[
 F_z(R_Nx)=F_z(x),\qquad H_l(R_Nx)=H_l(x),\qquad
 C_N(R_Nx)=C_N(x),\qquad u_N(R_Nx)=u_N(x).
 \tag{13}
\]
The cutoff in (6) is identical for both modes and is fixed
throughout the symmetric interval.

Here are the estimates from the truncation proof on that extended
interval. All factorial arguments remain in the zero-free strip:
their scaled real parts lie between \(a-\delta+O(h)>0\) and
\(1-a+\delta+O(h)<1\). For \(x=X+iY\), \(v\le\delta\),
\[
 |\sin\pi(X-v+iY)\sin\pi(X+v+iY)|
                 \ge \sin^2(\pi X)-\sin^2(\pi v)>0.
 \tag{14}
\]
This is the same product inequality as on the left half; it
holds throughout \(\delta<X<1-\delta\).
The exact summand ratio is
\[
 \frac{a_kF_{z-k}}{a_{k-1}F_{z-k+1}}
  =\frac{s_{z-k+1}^4}
  {s_ks_{2z+1-k}s_{Nx+z-k+1}s_{Nx-z+k}}.
 \tag{15}
\]
The parameter margins in (3), (14), and the factorial estimate
therefore give uniformly for \(0\le k\le m\)
\[
             |a_kF_{z-k}(x)|
                  \le CN^p e^{-NI_{kh}(\Re x)}.
 \tag{16}
\]
As a function of its upper endpoint, \(I_v(X)\) first increases
and then decreases. Its values at zero and \(\delta\) are
nonnegative on the chosen buffered interval. The proof of the
source thus applies unchanged: the first summand ratio is
\(O(h^2)\), the ratios for \(k\le\rho N\) are bounded by a
fixed contraction after choosing small \(\rho>0\), and the
remaining terms have a uniform positive exponential saving.
It follows, on any fixed-height rectangle in this symmetric strip,
that
\[
 U(z,x)=F_z(x)+O_{\rm hol}(h^2),\qquad
 F_z(x)=\{\sin\pi(x+h/2)\}^{2z}(1+O_{\rm hol}(h^2)).
 \tag{17}
\]
The ordinary telescoping identity is still
\[
 (\mathscr J_N-w)U(z,x)
                  =-\frac{a_m(z)s_{z-m}^4}{4}F_{z-m-1}(x).
 \tag{18}
\]
Its final multiplier relative to the last term in (16) is bounded.
Small disks of radius \(c/N\) preserve the smooth exponent,
while Cauchy estimates in \(\alpha\) use a larger rectangle
of type (3). Thus, writing \(r_l=(\mathscr J_N-w)H_l\),
\[
       |\partial_x^r\partial_\alpha^q r_l(x)|
                       \le CN^p e^{-NI_\delta(\Re x)}.
 \tag{19}
\]
The removable combination at \(\alpha=0\) has the same bounds.
Finally, \(I_\delta(X)=I_\delta(1-X)\), and it increases
on \(\delta<X<1/2\): differentiating its integrand gives
\(\pi\sin(2\pi X)/(\sin^2(\pi X)-\sin^2(\pi v))>0\).
Its minimum on \([x,1-x]\), for \(a\le x\le b_*\), is
therefore \(I_\delta(x)\).

## 3. A uniform spectral frame through the fold

Put \(\xi=x+h/2\). On a fixed complex neighborhood of the
real spectral interval traversed by \([a,1-a]\), choose
\[
 L(C)=\tfrac12\log\frac{2-C}{4},\qquad
 S_0(C)=e^{-L(C)}\cos(\nu L(C)),\qquad
 S_1(C)=e^{-L(C)}\frac{\sin(\nu L(C))}{\nu}.
 \tag{20}
\]
The neighborhood avoids \(C=2\), and the logarithm is real
on its real interval. The sine quotient is regular at zero.
Equations (17) and (6) show
\[
                     H_l(x)=S_l(C_N(x))+O_{\rm hol}(h^2).
 \tag{21}
\]
This estimate descends uniformly in the spectral variable even
at the fold \(\xi=1/2\). Here is the needed justification.
By (13), its remainder is an even holomorphic function of
\(y=\xi-1/2\) on a fixed disk. Its even power series, or the
holomorphic local coordinate theorem, makes it a holomorphic
function of \(y^2\). Since
\(C_N(x)+2=4\sin^2(\pi y)\), the change from \(y^2\) to
\(C+2\) is a local biholomorphism with uniform fixed disks.
The descended remainder has norm \(O(h^2)\) there. Cauchy's
formula on smaller spectral disks gives the same bound for all
fixed spectral derivatives. Away from the fold, \(C_N'\) is
a unit and ordinary inverse charts suffice. A finite cover gives
a common spectral neighborhood of the full real interval, with
these uniform bounds. No estimate was divided by a vanishing
angular derivative.

Accordingly each row quotient in (7) is the ordinary spectral
divided difference of a holomorphic function. At
\(x=1/2\), where \(C_N(x)=C_N(x-h)\), it equals its
spectral derivative. In particular it has a holomorphic extension.
Direct differentiation of (20) gives
\[
             S_0S_{1,C}-S_1S_{0,C}=-\frac2{(2-C)^2}.
 \tag{22}
\]
Since \(C_N(x)-C_N(x-h)=O(h)\), (21)--(22) imply
\[
 \det\mathcal F_N(x)
                =-\frac2{(2-C_N(x))^2}+O(h).
 \tag{23}
\]
It is a uniform unit on a fixed smaller neighborhood of
\([a,1-a]\), including the fold and the parameter coalescence.
Both the frame and its inverse, with every fixed derivative,
are uniformly bounded there.

The actual kernel is an ordinary polynomial in \(C\). The
pinned endpoint-product estimate gives
\(\|K_N(w,\cdot)\|_{[-2,2]}\le CN^p\) uniformly on larger
bounded complex parameter sets. Markov's inequality gives
polynomial bounds for its fixed spectral derivatives. Hence its
divided-color state on this real interval is polynomially bounded,
including coincident colors. It follows that
\[
 \mathbf a_N(x)=\mathcal F_N(x)^{-1}\mathcal V_{u_N}(x)
                                      \quad\hbox{satisfies}\quad
       \|\mathbf a_N(x)\|\le CN^p
 \tag{24}
\]
on the real interval. The vector is holomorphic on the common
neighborhood; no small off-real norm of the canonical kernel
is used.

## 4. The exact regular recurrence and coefficient reflection

Write the original operator as
\[
 \mathscr J_N f=(c_0+A_N+B_N)f-A_Nf(x+h)-B_Nf(x-h),
\]
\[
 A_N=\frac{s_{Nx+1}^4}{s_{2Nx+1}s_{2Nx+2}},\qquad
 B_N=\frac{s_{Nx}^4}{s_{2Nx}s_{2Nx+1}}.
\]
Set
\[
 q_N^\sharp=\left(\frac{\sin\pi x}{\sin\pi(x+h)}\right)^4,
 \quad
 b_N^\sharp=\frac1{A_N\Delta_N(x+h)}
       =-\frac{\sin(2\pi x+\pi h)}
                    {16\sin(\pi h)\sin^4\pi(x+h)},
\]
\[
 T_N^\sharp=
 \begin{pmatrix}
 1+(c_0-w)/A_N&q_N^\sharp\Delta_N(x+h)\\
 (c_0-w)b_N^\sharp&q_N^\sharp
 \end{pmatrix},\qquad
 \mathbf b_N=\binom{1/A_N}{b_N^\sharp}.
 \tag{25}
\]
Solving the ordinary equation for its forward value gives exactly
\[
 \mathcal V_f(x+h)=T_N^\sharp(x)\mathcal V_f(x)
                              -\mathbf b_N(x)(\mathscr J_N-w)f(x).
 \tag{26}
\]
Indeed \((B_N/A_N)\Delta_N(x)/\Delta_N(x+h)=q_N^\sharp\).
All expressions in (25) are holomorphic through the fold.
On the fixed neighborhood under consideration,
\[
 T_N^\sharp=I+O(h),\quad (T_N^\sharp)'=O(h),\qquad
                 \|\mathbf b_N\|+\|\mathbf b_N'\|\le CN.
 \tag{27}
\]
These follow from \(c_0-w=O(h^2)\),
\(q_N^\sharp=1+O(h)\), and the explicit canceled formula
for \(b_N^\sharp\). Thus the separate poles of the original
angular coefficients create no singular transfer in this frame.

Reflection of the frame is slightly shifted from reflection of
the scalar. For every function in (13),
\[
 \mathcal V_f(1-x)=
       \begin{pmatrix}1&-\Delta_N(x)\\0&1\end{pmatrix}
                                                 \mathcal V_f(x).
 \tag{28}
\]
The first value is \(f(x-h)\); the spectral divided difference
is unchanged when its two arguments are exchanged. Formula (28)
holds also at the fold by holomorphic continuation. Applying it
to both the actual state and the mode frame proves the exact law
\[
                \mathbf a_N(1-x)=\mathbf a_N(x),\qquad
                \mathbf a_N'(1-x)=-\mathbf a_N'(x).
 \tag{29}
\]

## 5. The physical source fixes the derivative coefficient

Let \(\mathbf r_N=(r_0,r_1)\) denote the row of mode residuals
from (19), and let \(r_K=(\mathscr J_N-w)u_N\). The original
ordinary source, with its sign retained, is
\[
 r_K(x)=-\frac{P_N(w)P_N(C_N(x))}{N^4(C_N(x)-c_0)},\qquad
                         P_N(C_N(x))=4\sin^2(\pi Nx).
 \tag{30}
\]
The denominator is a unit throughout the real interval being
used. At every physical point there,
\[
                            r_K(x_j)=r_K'(x_j)=0.
 \tag{31}
\]
This includes the odd middle point in its ordinary angular
interpretation. No extra spectral normal at the odd simple root
is prescribed.

Using (26) for the actual state and both columns of the frame
gives the exact coefficient equation
\[
 \mathbf a_N(x+h)=(I+M_N(x))\mathbf a_N(x)-\ell_N(x)r_K(x),
\]
\[
 \ell_N=\mathcal F_N(x+h)^{-1}\mathbf b_N(x),\qquad
                         M_N=\ell_N\mathbf r_N.
 \tag{32}
\]
Uniform frame bounds, (19), and (27) imply
\[
              \|M_N(x)\|+\|M_N'(x)\|
                         \le CN^p e^{-NI_\delta(x)}
 \tag{33}
\]
on the real interval. Differentiating (32) before evaluation,
then using both equalities in (31), yields at every such grid row
\[
 \mathbf a_{j+1}=(I+M_j)\mathbf a_j,\qquad
 \mathbf a_{j+1}'=(I+M_j)\mathbf a_j'+M_j'\mathbf a_j.
 \tag{34}
\]
Thus the independent first normal is retained in its own exact
equation. A values-only recurrence would not justify (34).

Fix any physical \(x_j\in[a,b_*]\). Propagate (34) from \(j\)
to \(N-j\). All rows lie in the symmetric buffered interval,
and \(I_\delta(x_l)\ge I_\delta(x_j)\) along this run.
There are at most \(N\) factors, and their errors are uniformly
exponentially small. Consequently the exact products give
\[
 \mathbf a_{N-j}'=P_j\mathbf a_j'+Q_j\mathbf a_j,\qquad
 \|P_j-I\|+\|Q_j\|\le CN^p e^{-NI_\delta(x_j)}.
 \tag{35}
\]
For example \(P_j\) is the product of \(I+M_l\), and
\(Q_j\) is the finite sum with one factor \(M_l'\) and the
ordinary products on either side. This proves (35) without any
assumed bound on \(\mathbf a_j'\).
By (29), its left side is \(-\mathbf a_j'\). The matrix
\(I+P_j=2I+o(1)\) is uniformly invertible. Combining (24)
and (35) therefore proves
\[
 \boxed{\qquad
                  \|\mathbf a_N'(x_j)\|
                      \le CN^p e^{-NI_\delta(x_j)}.
 \qquad}                                                    \tag{36}
\]
At the even coincident-color row, the frame itself is already
regular; at the odd simple row only its ordinary canonical
continuation was used. Neither case introduces a reset datum.

For \(x_j\in[a,b]\), the first equation of (34), propagated to
the right anchor in (8), similarly gives
\[
                    \|\mathbf a_N(x_j)-\mathbf a_*\|
                         \le CN^p e^{-NI_\delta(x_j)}.
 \tag{37}
\]
Now \(u_N=(H_0,H_1)\mathbf a_N\) identically on the real
neighborhood. Differentiate this identity and use (36)--(37),
together with the bounded modes and their derivatives. This
proves (9). Cauchy's formula on larger rectangles of type (3)
gives its fixed parameter derivatives without changing the rate.
The polynomial anchor bound and (19) prove (10); the sharp
truncation identity in the source gives (11).

All functions in (8)--(9) are even in \(\alpha\). On smaller
parameter sets they descend holomorphically to \(\alpha^2\),
and \(w_N-2\) is an analytic coordinate with derivative
\(N^{-2}(1+O(N^{-2}))\) in that variable. Thus fixed original
endpoint spectral derivatives cost only further powers of \(N\).
The same estimates consequently retain fixed outside normals
and finite products by the ordinary product rule. No division
by a possibly zero kernel value is involved.

## 6. Scope and complete direct sources

The scalar in (8) is the explicitly normalized approximate
homogeneous basis combination, anchored by two actual physical
values. The new estimate (36) supplies its previously retained
normal mismatch. It gives a moderate representative with sharply
small full physical-jet error; it does not make that error zero,
remove an exterior or interface current, or estimate a scalar
closing with arbitrary spectators.

The construction does not compare this scalar to the old
modified-differential-equation baseline on fractional grids.
Such a comparison is unnecessary for (9), and no statement about
the old Green boundary packet is inferred. Exact one-sided
Hermite repair of the new physical-jet error remains a subsequent
source operation with its own retained interface and sides.

The following complete direct sources were read at unchanged
pins, and their directly used implications checked:

* [Sharp sine-factor approximate modes](research_endpoint_sine_factor_sharp_truncation.md),
  SHA256 c731b1ccc3ea05f65b1227bff048b4e8a32cf36832289a1ed6e390232cc210bd.
* [Specified factorial and its logarithmic derivative](research_exact_cyclotomic_factorial.md),
  SHA256 0f989261f53747266ac62dba40ca7548138012b266521e98a03bd94b450c657b.
* [Actual polynomial endpoint bounds](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194.
* [Original ordinary kernel source](research_edge_kernel_difference_and_endpoint_bound.md),
  SHA256 5d0d07d4d97d82cca66e0e0c3bf2cecad8e5f58ef8329178278b297cf0d6c5da.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build or
compilation was run. Adopted notes and public manuscripts remain
unchanged.
