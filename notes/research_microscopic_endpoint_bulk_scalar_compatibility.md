# Scalar compatibility of the actual microscopic endpoint in the physical bulk

Private written proof, 16 November 2026.

The actual value and first spectral normal of a microscopic endpoint
kernel admit one polynomially bounded holomorphic scalar representative
on every buffered physical bulk interval. The two source coefficients
in the prior normal-defect transport are exponentially small. The
argument combines its moderate separate channels with an exact
alternating analytic expression for their difference; both parity
subgrids are essential.

Locally the scalar representative can be chosen to be an actual
partial Newton sum. Its bounded complex neighborhood can be thin.
No endpoint extension, whole-period representative, contour connector
estimate, or filled-source rate follows.

## 1. Original data and the assertion

Put
\[
 D=N-1,\quad \eta=(-1)^D,\quad \theta=\pi/N,\quad
 m=\lfloor N/2\rfloor,\quad J=\lfloor(N-1)/2\rfloor,\quad
 k_0=\lceil N/2\rceil=J+1,
\]
\[
 c_j=2\cos((2j+1)\theta),\quad
 e_k(Z)=S_k^{-2}\prod_{a<k}(c_a-Z),\quad
 S_k=\prod_{a=1}^k2\sin(a\theta),\quad S_0=1,
\]
\[
 K_N(w,Z)=\sum_{k=0}^{D}e_k(w)e_k(Z),\qquad
 w_N(\alpha)=2\cosh(\alpha/N),\qquad B_N(Z,\alpha)=K_N(w_N(\alpha),Z).
 \tag{1}
\]
The distinct physical nodes are \(c_0,\ldots,c_J\). All are double
roots of \(P_N(Z)=2T_N(Z/2)+2\), except the odd simple node \(c_J=-2\).
Use the normalized index and its angular coordinates
\[
 x_j=j/N,\quad \nu_N(x)=2\pi x+\pi/N,\quad
 \tau_N(x)=\pi-\nu_N(x),\quad c_N(x)=2\cos\nu_N(x),
\]
\[
 c_N'(x)=-4\pi\sin\nu_N(x),\qquad
 F_j=B_N(c_j,\alpha),\quad G_j=\partial_ZB_N(c_j,\alpha).
 \tag{2}
\]
Fix nested nondegenerate closed intervals
\[
 I_0\Subset\operatorname{int}I_1,\qquad
 I_1\Subset\operatorname{int}I_2,\qquad I_2\Subset(0,1/2).
 \tag{3}
\]
All parameters are allowed in an arbitrary fixed bounded complex
disk. Larger fixed disks and smaller spatial domains are used for
derivative estimates.

Call \(f_N(x,\alpha)\) admissible if it is holomorphic on a fixed
neighborhood of \(I_2\) and a larger parameter disk, has a bound
\(\lVert f_N\rVert\le CN^p\), and satisfies
\[
                         f_N(x_j,\alpha)=F_j(\alpha)
                              \quad(x_j\in I_2).
 \tag{4}
\]
The two-channel source supplies such a family and, separately, a
polynomially bounded holomorphic \(\mathcal G_N\) with
\(\mathcal G_N(x_j,\alpha)=G_j(\alpha)\). Intersect its domain with
that of any chosen admissible \(f_N\).

**Theorem 1.** For every admissible \(f_N\), there are a fixed
complex neighborhood \(U\) of \(I_0\) and constants \(C,P,c>0\)
such that, for all sufficiently large \(N\),
\[
 d_N(x,\alpha):=c_N'(x)\mathcal G_N(x,\alpha)-\partial_xf_N(x,\alpha)
                         =O_{\rm hol}(N^Pe^{-cN})\quad(x\in U).
 \tag{5}
\]
Here and below fixed derivatives are bounded on smaller spatial
and parameter domains. In particular the actual nodal defect
\[
 \Delta_{j,N}=c_N'(x_j)G_j-\partial_xf_N(x_j)
 \tag{6}
\]
is exponentially small on \(I_0\). Both actual anchor coefficients
of the two-mode normal-defect theorem are exponentially small.

There is a polynomially bounded holomorphic scalar \(h_N\) on a
fixed smaller bulk neighborhood, jointly holomorphic in \(\alpha\),
such that at every physical node in \(I_0\)
\[
                    h_N(x_j)=F_j,\qquad h_N'(x_j)=c_N'(x_j)G_j.
 \tag{7}
\]
It differs from \(f_N\) by an exponentially small holomorphic
function on that neighborhood. All assertions hold at both
parities and uniformly on bounded complex parameter sets, including
zeros of \(\cosh(\alpha/2)\).

## 2. A polynomially bounded distinct-root quotient

Let \(L_N(Z,\alpha)\) be the ordinary degree-\(J\) interpolation of
the \(F_j\)'s at all distinct physical nodes. It is exactly the low
Newton part of \(B_N\). Indeed the remaining Newton polynomials
vanish at all distinct nodes, and the degree-\(J\) interpolation is
unique. The endpoint-product source proves, on every bounded complex
parameter disk,
\[
                       \sup_{Z\in[-2,2]}|L_N(Z,\alpha)|\le CN^p.
 \tag{8}
\]
Its proof uses the actual physical row values and ordinary
Chebyshev interpolation; it does not require the endpoint parameter
to stay below its first imaginary zero.

Write \(\mathcal P_N\) for the monic distinct-root polynomial.
Its exact formulas are
\[
 \begin{array}{ll}
 N=2m:&\mathcal P_N(Z)=2T_m(Z/2),\\
 N=2m+1:&\mathcal P_N(Z)=2T_{m+1}(Z/2)+2T_m(Z/2).
 \end{array}
\]
Consequently
\[
 \mathcal P_N(c_N(x))=-a_N(x)\sin(\pi Nx),\qquad
 a_N(x)=
 \begin{cases}
 2,&N\text{ even},\\
 4\cos(\pi x+\pi/(2N)),&N\text{ odd}.
 \end{cases}
 \tag{9}
\]
On a sufficiently small fixed bulk neighborhood \(a_N\) is a
uniform unit.

Define
\[
 g_N(x,\alpha)=
 \frac{L_N(c_N(x),\alpha)-f_N(x,\alpha)}
                         {\mathcal P_N(c_N(x))}.
 \tag{10}
\]
All its apparent poles on a buffered bulk domain are removable:
the sine zeros there are precisely \(x_j=j/N\), and (4) makes
the numerator zero at each. Division is jointly holomorphic in
the parameter. There are no additional zeros from \(a_N\).

Here it is important that this quotient has polynomial norm,
despite the ordinary interpolant's possible off-real growth.
From (8), each Chebyshev coefficient of \(L_N\) has modulus at
most twice its real norm. Thus, for \(x=X+iY\),
\[
             |L_N(c_N(x),\alpha)|
                       \le CN^{p+1}e^{2\pi J|Y|},\qquad 2J<N.
 \tag{11}
\]
Choose a rectangle enclosing a fixed neighborhood of \(I_1\),
whose closure lies in the common analytic domain over \(I_2\).
Its horizontal sides have fixed heights \(\pm h_0\). Move its
vertical sides by \(O(N^{-1})\) so their real parts are
\((j+1/2)/N\), retaining fixed buffers. On either vertical side,
\[
 |\sin(\pi Nx)|=\cosh(\pi NY)\ge\tfrac12e^{\pi N|Y|};
\]
on either horizontal side it is at least
\(\sinh(\pi Nh_0)\ge c_0e^{\pi Nh_0}\) for large \(N\).
Equations (9)--(11), \(2J<N\), and the polynomial bound for \(f_N\)
therefore bound \(g_N\) by a fixed power of \(N\) on the whole
boundary. The maximum principle gives the same bound inside.
Cauchy's formula gives polynomial bounds for its fixed derivatives
on a fixed smaller rectangle. This argument is uniform in the
larger parameter disk.

At a grid point, differentiation of (10) now gives exactly
\[
 \partial_x[L_N(c_N(x))-f_N(x)]_{x=x_j}
                 =-\pi N(-1)^j a_N(x_j)g_N(x_j).
 \tag{12}
\]

## 3. An exact analytic high normal on every local bulk chart

We recall enough of the general-domain source to verify both its
normalization and its applicability throughout the physical bulk.
For \(0<\delta<1/2\), let \(L=\lfloor\delta N\rfloor\) and
\[
 (A_\ell,B_\ell)=
 \begin{cases}
 ((\ell+\tfrac12)\theta,(\ell+1)\theta),&N\text{ even},\\
 ((\ell+1)\theta,(\ell+\tfrac32)\theta),&N\text{ odd},
 \end{cases}
\]
\[
 \rho_{\ell,N}(\alpha,t)=
 \frac{[\cos^2A_\ell+\sinh^2(\alpha/(2N))]
             [\sin^2(t/2)-\sin^2A_\ell]}{\cos^4B_\ell},
 \qquad
 \Gamma_N^\delta(\alpha,t)
       =T_{0,N}(\alpha,t)\sum_{\ell=0}^{L}\prod_{r<\ell}\rho_{r,N},
 \tag{13}
\]
\[
 T_{0,N}(\alpha,t)=
 \begin{cases}
 N^{-1}\cosh(\alpha/2)\sin t,&N\text{ even},\\[2pt]
 \displaystyle
 \frac{\cosh(\alpha/2)\cosh(\alpha/(2N))}
 {N\cos^4(\theta/2)}\sin t\sin(t/2),&N\text{ odd}.
 \end{cases}
 \tag{14}
\]
Let \(B_N^{\rm high}=B_N-L_N\). Its exact physical normal is
\[
 \eta(4-c_j^2)(B_N^{\rm high})'(c_j,\alpha)
                    =\eta(-1)^j\gamma_{j,N}(\alpha).
 \tag{15}
\]
For every fixed \(b<2\pi\delta\), the source proves, at all
sufficiently large levels,
\[
 \Gamma_N^\delta(\alpha,\tau_N(x_j))
       =\gamma_{j,N}(\alpha)\qquad
                         (0<\tau_N(x_j)\le b).
 \tag{16}
\]
This is exact for every complex \(\alpha\): a factor in the finite
lowering product vanishes when its actual physical chain stops.
It is not an asymptotic interpolation.

Put \(a_\delta=\sin^2(\pi\delta)\). On every compact subset of
\[
 \mathcal D_\delta
       =\{t:|\sin^2(t/2)-a_\delta|<1-a_\delta\},
 \tag{17}
\]
all the ratios in (13) have modulus at most a common \(q<1\) for
large \(N\), uniformly for bounded complex \(\alpha\).
Thus \(\Gamma_N^\delta=O_{\rm hol}(N^{-1})\) there. No division by
the base factors in (14) is needed.

Every fixed physical bulk point admits both (16) and (17) on the
same local chart. To see this, fix \(x_0\in(0,1/2)\), and put
\(\tau_0=\pi-2\pi x_0\), \(z_0=\sin^2(\tau_0/2)<1\).
Choose \(\delta\) so that
\[
                 z_0<a_\delta<(1+z_0)/2.
 \tag{18}
\]
Then \(\delta>\tau_0/(2\pi)\), while
\(|z_0-a_\delta|<1-a_\delta\). There is therefore a fixed complex
neighborhood of \(\tau_0\), compactly contained in (17), whose real
angles lie in \(0<t<b<2\pi\delta\). A fixed local \(x\)-disk and
all sufficiently large \(N\) satisfy these conditions under
\(t=\tau_N(x)\). The \(O(N^{-1})\) offset has been absorbed into
fixed margins. A finite collection of such charts covers \(I_0\).

In particular a cutoff larger than \(1/4\), when needed, causes no
problem: its symbol domain need not contain zero, but it does
contain the local angle in (18). This is the domain fact that
allows the argument on arbitrary compact physical bulk intervals.

Since \(4-c_j^2=4\sin^2\nu_N(x_j)\), (2), (15), and (16) give
\[
 c_N'(x_j)(B_N^{\rm high})'(c_j)
       =(-1)^{j+1}
          \frac{\pi\Gamma_N^\delta(\alpha,\tau_N(x_j))}
               {\sin\nu_N(x_j)}.
 \tag{19}
\]
Combining (12) and (19) proves the exact local identity
\[
 \Delta_{j,N}=(-1)^j\mathcal A_N^\delta(x_j,\alpha),
 \qquad
 \mathcal A_N^\delta(x,\alpha)=
 -\pi N a_N(x)g_N(x,\alpha)
 -\frac{\pi\Gamma_N^\delta(\alpha,\tau_N(x))}
                         {\sin\nu_N(x)}.
 \tag{20}
\]
The function \(\mathcal A_N^\delta\) has polynomial norm on a
fixed local chart. The factor \(\sin\nu_N\) is a uniform unit
there. Equation (20) retains the actual first spectral normal
and its parity sign.

## 4. Two dense subgrids force the actual defect to be small

We use the following elementary analytic observation. Suppose \(d_N\)
and \(a_N^\circ\) are holomorphic on a fixed disk about a real point,
have a polynomial norm bound, and
\[
                  d_N(j/N)=(-1)^j a_N^\circ(j/N)
 \tag{21}
\]
at every grid point in its central real interval. Then
\(d_N-a_N^\circ\) vanishes on the even subgrid and
\(d_N+a_N^\circ\) on the odd subgrid.

For an explicit estimate, take a closed disk of radius \(R\)
within the domain. The real interval of radius \(R/8\) contains
at least \(RN/16\) nodes of each parity for large \(N\).
For \(|z-x_0|\le R/8\) and a zero \(a\) in that same interval,
the disk Blaschke factor is bounded by
\[
 \left|\frac{R(z-a)}{R^2-\overline{(a-x_0)}(z-x_0)}\right|
                              \le\frac{16}{63}<\frac13.
 \tag{22}
\]
Dividing by all those factors and applying the maximum principle
gives \(CN^P3^{-RN/16}\) for each of \(d_N\pm a_N^\circ\)
on the smaller disk. Hence both \(d_N\) and \(a_N^\circ\)
are exponentially small there. Fixed derivatives have the same
type of estimate on a smaller disk by Cauchy's formula. The
argument is uniform in holomorphic parameters when the original
norm bounds are uniform on a larger parameter domain.

Apply this observation to \(d_N\) from (5) and
\(a_N^\circ=\mathcal A_N^\delta\) from (20). The separate normal
interpolant gives \(d_N(x_j)=\Delta_{j,N}\), so (21) is exact.
Both functions are polynomially bounded on a common fixed disk.
The finite cover from Section 3 now gives a common positive
exponential rate and a fixed complex neighborhood of \(I_0\).
This proves (5)--(6), as well as exponential smallness of each
local \(\mathcal A_N^\delta\). In particular no approximate
oscillatory Fourier transform has been used.

Here is the consequence for the prior two-mode transport in its
exact normalization. At a bulk node let
\[
 D_j^f=
 \begin{pmatrix}
 \Delta_{j,N}\\
 N(\Delta_{j,N}-\Delta_{j-1,N})
 \end{pmatrix}.
 \tag{23}
\]
At an anchor in the interior of \(I_0\), both components are
\(O(N^Pe^{-cN})\), increasing \(P\) if necessary. In the pinned
transport theorem the actual source coefficients are
\[
             \mathbf a_N^f(\alpha)
                 =\Phi(x_{*,N},\alpha)^{-1}D_{j_*}^f.
 \tag{24}
\]
Its regular fundamental matrix has columns generated by
\[
 \frac{\cos((\alpha/\pi)\log\sin\pi x)}{\sin\pi x},
 \qquad
 \frac{\sin((\alpha/\pi)\log\sin\pi x)}
                  {(\alpha/\pi)\sin\pi x},
 \tag{25}
\]
and their derivatives. The second expression has its removable
logarithmic value at \(\alpha=0\). Its determinant is
\(\pi\cos(\pi x)/\sin^3(\pi x)\), a bulk unit. Thus \(\Phi^{-1}\)
is uniformly bounded on the fixed compact domains. Equation
(24) proves exponential smallness of both actual coefficients,
also at the coalescing parameter. These coefficients have not
been selected or reset.

## 5. Explicit local scalars and a scalar on the full compact interval

On a chart with its chosen \(\delta\), define
\[
 h_N^\delta(x,\alpha)=L_N(c_N(x),\alpha)
       -\frac{\Gamma_N^\delta(\alpha,\tau_N(x))}
                   {N\sin\nu_N(x)}\sin(\pi Nx).
 \tag{26}
\]
At grid nodes its second term has value zero. Its derivative there
is exactly the high-normal correction (19). Thus (26) matches
both original channels on the chart without an approximation.
Equations (9), (10), and (20) also give the exact identity
\[
               h_N^\delta-f_N
                   =\frac{\sin(\pi Nx)}{\pi N}\mathcal A_N^\delta.
 \tag{27}
\]
The exponential estimate just proved beats the sine growth on a
sufficiently thin fixed strip. Therefore (26) is polynomially
bounded there and exponentially close to \(f_N\).

There is also a literal polynomial interpretation. With
\(L=\lfloor\delta N\rfloor\) and large \(N\),
\[
        h_N^\delta(x,\alpha)
          =\sum_{k=0}^{k_0+L}e_k(w_N(\alpha))e_k(c_N(x)).
 \tag{28}
\]
To check the constants, at even \(N=2m\), \(S_m^2=2N\), so
\[
 e_m(w)e_m(Z)=\frac{\cosh(\alpha/2)}{2N^2}\mathcal P_N(Z).
 \tag{29}
\]
At odd \(N=2m+1\), \(S_{m+1}^2=4N\cos^2(\theta/2)\), and
\[
 e_{m+1}(w)e_{m+1}(Z)
 =\frac{\cosh(\alpha/2)\cosh(\alpha/(2N))}
        {4N^2\cos^4(\theta/2)}\mathcal P_N(Z).
 \tag{30}
\]
These follow directly from the products in (1), the monic
distinct-root formulas, and \(S_{N-1}=N\).
For \(Z=-2\cos t\), the ratio of successive products beginning
at \(k=k_0\) is precisely \(\rho_{\ell,N}(\alpha,t)\).
Indeed their numerator is
\(16[\cos^2A_\ell+\sinh^2(\alpha/(2N))]
[\sin^2(t/2)-\sin^2A_\ell]\) and their denominator
is \(16\cos^4B_\ell\). Summing and using (9), (13)--(14)
gives (28). The bound is on the thin local domain supplied by
(27); it asserts nothing about this polynomial at a larger height.

For one scalar covering all of \(I_0\), the exact repair in the
pinned two-mode theorem can be used directly:
\[
 h_N(x,\alpha)=f_N(x,\alpha)+
 \sum_{j:\,x_j\in I_0}
 \Delta_{j,N}(\alpha)(x-x_j)\operatorname{sinc}^2(Nx-j),
 \quad \operatorname{sinc}z=\frac{\sin\pi z}{\pi z}.
 \tag{31}
\]
Each term has zero value at every grid point, derivative
\(\Delta_{j,N}\) at its own point, and a double zero at the
others. This proves (7) exactly. There are \(O(N)\) terms and
\(|\operatorname{sinc}^2(Nx-j)|\le e^{2\pi N|\Im x|}\).
Thus the correction is at most
\(CN^{P+1}e^{-cN+2\pi N|\Im x|}\). Choose a fixed strip height
less than \(c/(4\pi)\) within the common domain. The correction
is exponentially small and \(h_N\) has polynomial norm.
This proves all scalar assertions of Theorem 1.

On a sufficiently narrow bulk strip \(x\mapsto c_N(x)\) is
one-to-one, with derivative bounded away from zero. Equality of
two cosines requires \(x-y\in\mathbb Z\) or
\(x+y+1/N\in\mathbb Z\); the first gives \(x=y\), and the
second is excluded by the fixed buffers inside \((0,1/2)\).
Its inverse converts (26) locally, or (31) on the compact
interval, into a scalar spectral representative with exactly
the original value and first normal.

## 6. Shared products and original trace placement

For any fixed number of microscopic endpoint factors, take their
scalar representatives on a common smaller domain and multiply
them before tracing. Their product has polynomial norm and its
value and first spectral normal agree exactly with those of the
original shared product, by the ordinary product rule. All fixed
derivatives in the separate bounded complex endpoint parameters
are retained on smaller parameter sets.

For example, with an arbitrary actual joint spectator \(A(Z)\),
the original contribution of these bulk rows for one endpoint is
\[
 \eta\sum_{x_j\in I_0}
 \left[(4-c_j^2)\{G_jA(c_j)+F_jA'(c_j)\}
                              -c_jF_jA(c_j)\right].
 \tag{32}
\]
Replacing \(F_j,G_j\) by the value and spectral derivative of the
scalar representative leaves (32) exactly unchanged. A crossing,
its carrier and first normal, all shared graph kernels, all other
traces, and ordinary free boundary variables may remain in \(A\).
The assertion is coefficientwise in those uncontracted variables;
their growth is not bounded by the present theorem. Products at
several traced vertices preserve the full mixed normals by repeated
ordinary differentiation. No quotient reduction is imposed in a
free variable.

Only the covered bulk rows have been replaced. The odd simple node,
both physical endpoint regions, external connectors, and all
remaining source currents stay in the original expression.
Polynomial local scalar size does not supply a filled-action
estimate or prove a nonzero contribution. In particular there is
no conflict with the lower bound for a full-period even Hermite
representative: the domains and the required endpoint coverage
are different.

## 7. Coverage and direct sources

The prior two-channel theorem supplied moderate separate value and
normal interpolants, while the two-mode theorem isolated their
unknown true compatibility coefficients. The general radical-domain
theorem supplied exact high normals with analytic control, but had
not combined its locally varying cutoff with those two channels.
The new step is (18)--(22): exact physical termination on a suitable
chart at every bulk point, followed by the two dense parity subgrids.
It proves smallness of the actual compatibility coefficients and
gives the scalar representatives (26), (28), and (31).

All four complete direct source texts were freshly read in this
author sequence, and their used implications and hashes checked:

* [General endpoint radical domain](research_endpoint_radical_general_domain.md),
  SHA256 600ae0d78f29946272ed54b600cb1f5fdf170965985a08d6e3d9201303722074:
  exact finite lowering amplitude, both normal signs, physical
  termination, and the complex contraction domain.
* [Actual two-channel interpolation](research_microscopic_endpoint_two_channel_interpolation.md),
  SHA256 44f6db0f8afdf1205ab8b0935b95b8a4fd9fa16c6414be2467b8b40a123c0ffe:
  jointly holomorphic moderate interpolation of the actual values
  and normals, with bounded complex microscopic parameters.
* [Two half-plane endpoint-product source](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194:
  polynomial real norm of the ordinary low interpolation, original
  full-normal trace, and shared-product placement.
* [True two-mode normal-defect transport](research_endpoint_normal_defect_two_mode_transport.md),
  SHA256 91620d1ea26793157843f78fff32c7d3eca62509799114a2d3069af8b96b47dc:
  actual anchor normalization, bounded regular fundamental matrix,
  and exact scalar Hermite repair.

Only written mathematics, source-text reads, and file hashes were
used. No mathematical program, numerical experiment, test, or build
was run. Adopted notes and public manuscripts remain unchanged.
