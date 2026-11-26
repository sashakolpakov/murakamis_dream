# The exact coupled amplitude on a fixed complex neighborhood

Private written source proof, 8 November 2026. No mathematical numerical
evaluation, saved-value calculation, or frozen-source edit is used.

The entire normalized physical-index sum, with its exact lower cutoff,
extends as a uniformly bounded holomorphic amplitude on a fixed complex
neighborhood of its two remaining scaled indices. This includes every
finite tail. The proof uses a global logarithmic comparison, since
individual off-grid ratios can grow after a physical stopping zero.
It does not estimate the remaining two-index observation.

## 1. Exact source and fixed-end expression

Keep the original middle physical range and notation in
[the coupled-phase identity](research_mixed_next_middle_insertion_coupled_phases.md):
\[
\begin{gathered}
q=e^{\pi i/N},\quad s_a=2\sin(\pi a/N),\quad
S_a=\prod_{\nu=1}^a s_\nu,\\
L=\lfloor N/6\rfloor,\quad U=\lfloor N/2\rfloor-1,
\quad m_{jk}=\max\{L,j,k\},\\
a_n^{j,k}=\frac{S_n^3}{S_{n-j}S_{n+j+1}S_{n-k}},\qquad
W_{jk,N}=\sum_{n=m_{jk}}^U q^{-(k+1)n}a_n^{j,k}.
\end{gathered}                                                   \tag{1}
\]
Fix \(0<\varepsilon<1/2\). For independent complex variables
\((\eta,t)\), define the entire functions
\[
\begin{split}
\zeta_N(t)&=e^{i\pi(t+1/N)},\\
\rho_{n,N}(\eta,t)&=
\frac{\sin\pi(n/N-\eta)\,
      \sin\pi(n/N+\eta+1/N)\,
      \sin\pi(n/N-t)}{\sin^3(\pi n/N)},\\
\mathfrak G_N(\eta,t)
&=\sum_{\ell=0}^{U-L}\zeta_N(t)^\ell
                    \prod_{h=0}^{\ell-1}\rho_{U-h,N}(\eta,t).
\end{split}                                                     \tag{2}
\]
An empty product is one. Every denominator in (2) is a fixed
nonzero real number for the indicated levels and indices.

At the original integer indices \(\eta=j/N,t=k/N\),
\[
\boxed{\quad
W_{jk,N}=q^{-(k+1)U}a_U^{j,k}\,
                         \mathfrak G_N(j/N,k/N).
\quad}                                                         \tag{3}
\]
Indeed \(\rho_{n,N}=a_{n-1}^{j,k}/a_n^{j,k}\) when that ratio
is physically defined. If \(m_{jk}=j\) or \(m_{jk}=k\), the
factor at \(n=m_{jk}\) is exactly zero. Every later product in
(2) then vanishes, reproducing the actual stopping point without
introducing a negative-index factorial. If \(m_{jk}=L>j,k\),
the prescribed sum ends there. Thus (3) keeps both parity cutoffs
and the genuine lower physical endpoint.

Write
\[
\mathscr D_\varepsilon=[0,1/2]\times[\varepsilon,1/2],\qquad
r(\eta,t)=\cos^2(\pi\eta)\cos(\pi t),\qquad
\mathfrak b(\eta,t)=\frac1{1-e^{i\pi t}r(\eta,t)}.
\tag{4}
\]

**Theorem.** There is a fixed open complex neighborhood
\(\mathscr U_\varepsilon\) of \(\mathscr D_\varepsilon\), and
constants independent of the level and its parity, such that
\[
\sup_{\mathscr U_\varepsilon}|\mathfrak G_N|\le C_\varepsilon,
\qquad
\mathfrak G_N=\mathfrak b+O_\varepsilon(N^{-1})
\quad\hbox{uniformly on }\mathscr U_\varepsilon .
\tag{5}
\]
The denominator in (4) has no zero on this neighborhood. On a
smaller fixed neighborhood every fixed derivative of
\(\mathfrak G_N\) is bounded uniformly. For sufficiently large
levels \(\mathfrak G_N\) is also bounded away from zero there.

For use in the full source, the principal conclusion is the first
bound in (5) for the **exact** function (2). Its exponentially
small long-product tail is included before any subsequent
observation or contour estimate. No replacement by the second
formula of (5) is required.

## 2. The real global product rate

Put
\[
f(x)=\log|2\sin\pi x|,\qquad J(x)=\int_0^x f(s)\,ds
\quad(x\in\mathbb R).
\tag{6}
\]
This is the original real logarithmic primitive. It is continuous,
odd and one-periodic; \(J(1/2)=0\), and
\(J(x)<0\) for \(0<x<1/2\).
For real \(0\le\eta\le1/2\), \(\varepsilon\le t\le1/2\), define
\[
\Psi(x;\eta,t)=3J(x)-J(x-\eta)-J(x+\eta)-J(x-t)
                                      +J(1/2-t).
\tag{7}
\]
This is the integral of the logarithm of the absolute reverse
product from \(x\) to \(1/2\). There is no change of logarithmic
lift in (7); it is only a real product modulus.

The established
[real-period Newton comparison, Lemma 2](research_three_crossing_real_period_newton_bound.md)
gives
\[
V_{\pi-2\pi\eta}(x)
 =J(x+\eta)+J(x-\eta)-2J(x)\ge0,
                 \qquad 0\le x\le1/2.
\tag{8}
\]
The identity follows as well by factoring
\(2\cos(2\pi s)-2\cos(2\pi\eta)\) into its two sines.
Consequently
\[
\Psi(x;\eta,t)
\le G(x,t):=J(x)-J(x-t)+J(1/2-t).
\tag{9}
\]
This upper bound is strictly negative whenever
\(0<x<1/2\) and \(0<t\le1/2\). If \(x\ge t\),
\[
J(x)-J(x-t)=\int_{x-t}^x f(s)\,ds
 <\int_{1/2-t}^{1/2}f(s)\,ds=-J(1/2-t),
\tag{10}
\]
because \(f\) is strictly increasing on \((0,1/2)\), the
intervals have the same positive length, and \(x<1/2\).
Integrable endpoint singularities preserve the comparison.
If \(x<t\), oddness instead gives
\[
G(x,t)=J(x)+J(t-x)+J(1/2-t)<0.
\tag{11}
\]
Every term is nonpositive, and the first is strictly negative.

In particular, for any fixed \(0<d<1/12\), compactness supplies
\(\kappa_{\varepsilon,d}>0\) such that
\[
\Psi(x;\eta,t)\le-\kappa_{\varepsilon,d},\qquad
1/7\le x\le1/2-d,\quad(\eta,t)\in\mathscr D_\varepsilon.
\tag{12}
\]
This controls complete products even when individual ratios have
changed sign or grown in modulus below a physical stopping zero.
Those phenomena do not invalidate the strict integrated bound.

## 3. Uniform finite products, including zeros and complex shifts

We record the finite estimate needed to use (12). For a mesh
interval \([a/N,b/N]\) of bounded length, a bounded complex shift
\(z\), and samples at its right endpoints,
\[
\sum_{n=a+1}^{b}\log|2\sin\pi(n/N+z)|
\le N\int_{a/N}^{b/N}\log|2\sin\pi(s+z)|\,ds+C\log N.
\tag{13}
\]
The constant is uniform in the shift and endpoints on the compact
sets used here. This is the same zero-safe argument as
[the complex Newton envelope, Section 2](research_mixed_next_physical_three_kernel_fourier_bound.md),
and it does not require a lower bound on a numerator factor.

Here is the direct mesh justification. Outside the bounded number
of cells within \(2/N\) of a real sine zero, the real derivative
of the logarithmic modulus is at most a constant divided by the
distance to that zero, uniformly in the imaginary shift. The
successive cell errors are \(O(1/m)\), whose sum is \(O(\log N)\).
In the remaining cells, if \(|\Im z|\ge1/N\), the logarithmic
derivative is \(O(1/|\Im z|)\), giving bounded cell error.
If \(|\Im z|<1/N\), the sampled logarithm is at most
\(-\log N+C\), while the cell average is at least
\(-\log N-C\). For the latter lower bound use
\(|\sin\pi(x+ih)|\ge|\sin\pi x|\) and rescale the real
integrable singularity. An exact sampled zero only lowers the
left side. This proves (13), for endpoint as well as midpoint
sampling.

The denominator of (2) has indices between \(L+1\) and \(U\).
It stays in a fixed smooth real interval bounded away from the
integer zeros, so its two-sided mesh error is bounded.
Shifting an integration endpoint or a real numerator shift by
\(O(1/N)\) changes an integral of \(f\) by at most
\(C(\log N)/N\), uniformly through its logarithmic zeros.
Thus at real parameters, if \(x=(U-\ell)/N\), (13) gives
\[
\log\left|\prod_{h=0}^{\ell-1}\rho_{U-h,N}(\eta,t)\right|
\le N\Psi(x;\eta,t)+C\log N,
                       \qquad 0\le\ell\le U-L.
\tag{14}
\]
The displacements \(U/N-1/2=O(1/N)\) and the explicit
\(1/N\) in the second sine are both included in this error.

Complex shifts add a controlled rate before any further sum.
For real \(s\) and \(h\),
\[
\log|2\sin\pi(s+ih)|-f(s)\ge0,
\quad
\int_0^1\{\log|2\sin\pi(s+ih)|-f(s)\}\,ds=\pi|h|.
\tag{15}
\]
The first assertion follows from the squared-modulus identity;
the second follows by factoring the sine into its circle factor
of radius \(e^{-2\pi|h|}\), whose mean logarithm is zero.
Because the difference is nonnegative and periodic, its integral
over any interval of length at most one is at most \(\pi|h|\).
Applying (13) to the complex factors therefore gives
\[
\begin{split}
\log\left|\zeta_N(t)^\ell
                \prod_{h=0}^{\ell-1}\rho_{U-h,N}(\eta,t)\right|
\le{}&N\Psi(x;\Re\eta,\Re t)\!+
N\pi\{2|\Im\eta|+\tfrac32|\Im t|\}+C\log N.
\end{split}
\tag{16}
\]
Here \(\ell/N\le1/2\), so the additional phase modulus
\(|\zeta_N(t)|^\ell\) costs at most
\(N\pi|\Im t|/2\). Formula (16) does not use a physical
zero after moving the parameters off their integer grid.

The continuous function (7) is uniformly continuous on any fixed
compact real enlargement of the sets in (12). Shrinking that
enlargement, and then the allowed imaginary widths in (16),
preserves a strict negative upper rate, for example
\(-\kappa_{\varepsilon,d}/2\). The constants in the mesh
estimates remain uniform on these fixed complex neighborhoods.

## 4. Local contraction plus the entire finite tail

At \(n/N=1/2\) and in the limit \(1/N=0\), the weighted
ratio in (2) is
\[
e^{i\pi t}\cos^2(\pi\eta)\cos(\pi t).
\tag{17}
\]
Its modulus on \(\mathscr D_\varepsilon\) is at most
\(\cos(\pi\varepsilon)<1\). Uniform continuity therefore
allows a fixed \(d\in(0,1/12)\), a fixed complex
neighborhood of \(\mathscr D_\varepsilon\), and a number
\(r_\varepsilon<1\), such that for large \(N\),
\[
|\zeta_N(t)\rho_{n,N}(\eta,t)|\le r_\varepsilon
                 \quad\hbox{if }1/2-2d\le n/N\le1/2.
\tag{18}
\]
First make these choices, then shrink only the neighborhood so
that (16) and (12) apply to all longer products. The real
\(x\)-range there starts at \(L/N\ge1/7\) for large \(N\).

For \(0\le\ell\le dN\), every ratio lies in (18), giving
an absolute bound \(r_\varepsilon^\ell\). For \(\ell>dN\),
one has \(x\le1/2-d\); the complete product bound (16) gives
\[
\left|\zeta_N(t)^\ell
                \prod_{h=0}^{\ell-1}\rho_{U-h,N}(\eta,t)\right|
\le C N^C e^{-N\kappa_{\varepsilon,d}/2}.
\tag{19}
\]
There are at most \(N\) such terms. Their **entire** sum is
included in (2), and remains exponentially small uniformly on
the fixed neighborhood. Together (18)--(19) prove the first
assertion of (5).

For completeness the holomorphic limiting factor may also be
identified. Put \(A_\ell=\prod_{h=0}^{\ell-1}\rho_{U-h,N}\),
\(J_N=U-L\), and \(r=r(\eta,t)\). The exact identity is
\[
\begin{split}
(1-\zeta_Nr)\mathfrak G_N
=1+\sum_{\ell=1}^{J_N}
  (\rho_{U-\ell+1,N}-r)A_{\ell-1}\zeta_N^\ell
           -rA_{J_N}\zeta_N^{J_N+1}.
\end{split}
\tag{20}
\]
The last term is the genuine original \(L\)-endpoint, not a
discarded contour term. Near the upper endpoint, smoothness
gives \(\rho_{U-\ell+1,N}-r=O((\ell+1)/N)\).
Using (18), these errors sum to \(O_\varepsilon(N^{-1})\).
All farther terms and the endpoint in (20) are bounded by (19);
each additional ratio is uniformly bounded because its own
denominator stays away from zero. A term straddling the integer
split at \(dN\) is already exponentially small by (18).
The division in (20) is
uniformly permitted after the same neighborhood shrink.
Finally \(\zeta_N=e^{i\pi t}(1+O(N^{-1}))\), which proves
the second assertion of (5). Cauchy's formula on a smaller
fixed neighborhood proves the derivative bounds. The limiting
factor has modulus at least a positive constant there, so its
uniform approximation also proves the stated nonvanishing.

## 5. The full remaining observation and the changed physical cutoff

At the original grid, (3) may be inserted into the exact
coupled-phase identity without any error:
\[
\begin{split}
\mathscr S_N^{\rm mid}(w,Z)=\frac{\kappa(-q)^D}{N}
\sum_{j,k=0}^U
 &\frac{s_{2j+1}i^k q^{3j(j+1)+k(k-1)/2}}{S_k^2}\,
p_k(Z)\,q^{-(k+1)U}a_U^{j,k}\\
 &\hspace{8mm}\cdot\mathfrak G_N(j/N,k/N)
                         \mathcal K_{3,N}(w,c_j).
\end{split}
\tag{21}
\]
The present bound applies to \(k\ge\varepsilon N\); the
[small-outgoing estimate](research_mixed_next_three_small_outgoing_indices.md)
treats the omitted small \(k\) range when \(\varepsilon=1/4096\).
The theorem is uniform in all \(j\), so the separately paid
[small internal indices](research_mixed_next_three_small_internal_indices.md)
need no additional amplitude restriction.

The endpoint amplitudes \(a_U^{j,k}\), their
[two exact parity formulas](research_mixed_next_middle_physical_endpoint_packet.md),
the outgoing polynomials, the inner signed kernel and
all phases in (21) remain. Only the exact factor
\(\mathfrak G_N\) is now certified to have bounded analytic
continuation. In a subsequent valid two-index contour argument,
it may be kept intact and bounded there. This includes (19)
before the rest of the observation is estimated; it is not an
assertion that an independently removed tail stays negligible
after multiplying large source factors.

The physical near-half theorem now pays a fixed band
\[
\lceil N/2\rceil\le b\le\lfloor N(1/2+\delta)\rfloor.
\]
The remaining physical sum has upper \(n\)-cutoff
\(N-2-\lfloor N(1/2+\delta)\rfloor\), not \(U\).
No half-endpoint formula is applied to that new cutoff here.
Instead (21) is the old whole-middle identity; the complete
paid band is subtracted with all its outgoing factors, exactly
as in
[the physical continuation theorem](research_mixed_next_three_physical_half_band_from_vertical.md).
This is an eligible way to use (21) for the remaining problem,
because the subtracted full physical observation already has
its own exponential bound. That bound is not assigned to an
arbitrary partial \(j,k\) sum inside the band.

Finally the optional approximation in (5) cannot be substituted
into (21) and its error discarded: a coefficientwise relative
\(O(N^{-1})\) error need not survive further exponential
cancellation. The exact bounded amplitude (2) is the source
conclusion. It removes the unestimated analytic-tail obstruction
to retaining this amplitude in a joint contour, but does not
itself supply the required exponential bound for (21), its
remaining signed Fourier observations, or the complete transfer.
