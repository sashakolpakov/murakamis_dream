# Polynomial ray transport and the complex-normal endpoint

The original full-dilogarithm ray transfer has a polynomially bounded
inverse. Its Fourier conjugate transports arbitrary exterior rows with
logarithmic norm loss, independently of the diagonal weights in an
actual beta transform. These finite estimates coexist with zeros of
the actual top-degree Mellin-normal ray coefficient at distance
\(O(1/\log N)\) from its physical value. The original marked observation
is retained throughout; an invertible transport is not a lower bound
for its final scalar pairing.

## 1. Consecutive moments and the polynomial inverse

Use the full function, branch, and signs of [R]. Put
\[
 N\ge2,\quad d=N-1,\quad Q=e^{2\pi i/N},\quad
 \epsilon\in\{1,-1\},\qquad
 I_b=\int_0^1\Psi_\epsilon(\log r+i\epsilon\pi)r^{b-1}\,dr.
 \tag{1}
\]
Initially \(b\) is a positive integer. The actual coefficients are
\[
 j_{\epsilon,a}=-\frac{\epsilon(-1)^{N-a}}{2\pi i}I_{N-a},
 \qquad 0\le a<N.
 \tag{2}
\]
The analytic input, including its full quantum remainder, is [R,(5)]:
\[
 \Psi_\epsilon(\log r+i\epsilon\pi)
 =A(r)e^{i\epsilon N\phi(r)}(1+e_N(r)),\quad
 A(r)=\sqrt{1+r},\quad
 \phi(r)=-\frac{\operatorname{Li}_2(-r)}{2\pi},
\]
\[
 |e_N(r)|+|r e_N'(r)|\le C/N,
 \qquad c\le\phi'(r)\le c_0,
 \quad c=\frac{\log2}{2\pi},\quad c_0=\frac1{2\pi}.
 \tag{3}
\]
The derivatives of \(A,\phi\) used below extend boundedly to
\([0,1]\). No bounded ordinary derivative of \(e_N\) at zero is
assumed. The exact modulus is \(|\Psi_\epsilon|=A\).

For every \(2\le b\le N-1\),
\[
                         |I_b-I_{b+1}|\le C N^{-2}.
 \tag{4}
\]
Here and below constants do not depend on the physical index.
To prove this, put \(f_b(r)=r^{b-1}(1-r)\). It vanishes at both
endpoints. For \(b\ge3\),
\[
 f_b''=(b-1)(b-2)r^{b-3}(1-r)-2(b-1)r^{b-2},
\]
and the integrals of the absolute values of the two displayed terms
are respectively one and two. The case \(b=2\) is direct. Also
\[
 |f_b'(0)|+|f_b'(1)|+\|f_b'\|_1+\|f_b\|_1\le C,
 \qquad \int_0^1\frac{f_b(r)}r\,dr=\frac1{b(b-1)}.
 \tag{5}
\]
Consequently the endpoint first derivatives and second-derivative
\(L^1\) norm of \(f_b A\) are uniformly bounded. Two integrations
by parts against \(e^{i\epsilon N\phi}\) bound its integral by
\(C/N^2\); the first endpoint term vanishes.

The actual remainder needs only one integration by parts. The
amplitude \(f_b A e_N\) tends to zero at both ends, and (3),(5) give
\[
 \int_0^1\left|\left(\frac{f_b A e_N}{\phi'}\right)'\right|dr
 \le C/N.
\]
All terms are integrable at zero, including \(f_b e_N'\).
Integration first over a truncated interval and then taking its
lower endpoint to zero proves (4) for the full function.

Retain the exact normalization of [R]:
\[
 \zeta_{\epsilon,N}
 =-\frac{\epsilon(-1)^N\sqrt2}{2\pi i}e^{i\epsilon N\pi/24},
 \qquad h_a=\frac{N(-1)^a j_{\epsilon,a}}{\zeta_{\epsilon,N}}
          =\frac{N I_{N-a}}{\sqrt2 e^{i\epsilon N\pi/24}}.
 \tag{6}
\]
The uniform lower and upper bounds in [R,(4)] imply
\(c_*\le|h_a|\le C_*\) for all sufficiently large \(N\).
Equation (4) improves the bulk differences to
\[
 |h_a-h_{a-1}|\le C/N\quad(1\le a<d),\qquad
 |h_d-h_{d-1}|\le C.
 \tag{7}
\]
The second bound retains the original \(b=1\) endpoint; it is not
replaced by the first bound.

Let \(T\) act on any finite-dimensional Hilbert space with
\(\|T\|_2\le1\) and \(T^N=0\). Then
\[
 \mathcal J_{\epsilon,N}(T)=\sum_{a=0}^d j_{\epsilon,a}T^a,
 \qquad
 \boxed{\|\mathcal J_{\epsilon,N}(T)\|_2\le C,
        \quad\|\mathcal J_{\epsilon,N}(T)^{-1}\|_2\le CN.}
 \tag{8}
\]
This holds for all sufficiently large levels, without normality of
\(T\). For completeness put \(H(S)=\sum h_aS^a\), so that
\(\mathcal J(T)=\zeta H(-T)/N\). Modulo \(S^N\),
\[
 (1-S)H(S)=h_0\left(1+\sum_{a=1}^d b_aS^a\right),
 \qquad b_a=(h_a-h_{a-1})/h_0.
\]
For \(a<d\), \(|b_a|\le\eta_N=C/N\). The coefficient of degree
\(n\ge1\) in \((1+\sum_{a<d}b_aS^a)^{-1}\) has absolute value
at most
\[
 \sum_{k=1}^n {n-1\choose k-1}\eta_N^k
       =\eta_N(1+\eta_N)^{n-1}.
 \tag{9}
\]
The degree-\(d\) seam adds exactly \(-b_dS^d\) to that inverse.
Its products with positive powers have degree at least \(N\).
Thus the inverse coefficient sum is bounded by
\((1+C/N)^d+C\le C'\). Multiplication by \(1-S\) and division by
\(h_0\) prove the inverse estimate (8). The direct estimate follows
from \(|j_{\epsilon,a}|\le C/N\).

Unit multiples of \(T\) preserve (8), including the actual
\(u\)-ray \(\mathcal J_{-,N}(Q^{-1}T)\) and \(v\)-ray
\(\mathcal J_{+,N}(T)\). The reciprocal-factorial and reflected
factorial rays retain respectively the diagonal coefficients
\(Q^{-a}j_{-,a}\) and \(NQ^{d-a}j_{+,d-a}\) of [R,(19)].
Their norm/inverse bounds remain \(C/N,CN\) and \(C,C\).
Every fixed composable product of these actual maps and unitary
maps therefore has polynomial norm and inverse norm. Cups,
projections, and marked covectors are not inverted by this statement.

## 2. Fourier transport of the actual co-source

Let \(\mathsf F_{Ka}=N^{-1/2}Q^{Ka}\), and set
\[
 J_\epsilon=\operatorname{diag}(j_{\epsilon,a}),\qquad
 \mathcal K_\epsilon=\mathsf FJ_\epsilon\mathsf F^{-1}.
\]
The norms on finite arrays in this section use counting measure,
and the inverse estimates are for all sufficiently large levels.
Besides the immediate Hilbert-space bounds, there are
\[
 \boxed{\|\mathcal K_\epsilon\|_{\ell^1\to\ell^1},
        \|\mathcal K_\epsilon\|_{\ell^\infty\to\ell^\infty}
                      \le\frac{C\log(eN)}N,}
\]
\[
 \boxed{\|\mathcal K_\epsilon^{-1}\|_{\ell^1\to\ell^1},
        \|\mathcal K_\epsilon^{-1}\|_{\ell^\infty\to\ell^\infty}
                      \le CN\log(eN).}
 \tag{10}
\]
Indeed (7) bounds the total variation of both \((h_a)\) and
\((h_a^{-1})\) by a constant. For either array \(u_a\) and
\(z=-Q^\ell\), the exact finite identity
\[
 (1-z)\sum_{a=0}^d u_az^a
   =u_0-u_dz^N+\sum_{a=1}^d(u_a-u_{a-1})z^a
 \tag{11}
\]
bounds its right side by a constant. By (6), the convolution kernel
\(k_\ell=N^{-1}\sum_a j_{\epsilon,a}Q^{\ell a}\) consequently obeys
\[
 |k_\ell|\le\frac{C}{N^2|1+Q^\ell|}\quad(Q^\ell\ne-1).
 \tag{12}
\]
At the exact resonance for even \(N\), use \(|k_{N/2}|\le C/N\).
For odd \(N\) the two nearest terms are at half-integer distance
from \(N/2\); they also satisfy this bound. The elementary sine
bound gives
\(\sum_{Q^\ell\ne-1}|1+Q^\ell|^{-1}\le CN\log(eN)\).
For the inverse kernel, (6),(11) give the bound
\(C/|1+Q^\ell|\), with \(CN\) at exact resonance.
Summing the kernels proves (10). In particular no half-period shift
at odd level is silently replaced by an integer cyclic shift.

The actual beta transform [B,(3)] has the form
\(B_L=\sqrt N\mathsf F\operatorname{diag}(g_a)\), with all
\(g_a\ne0\). Therefore, exactly and for every retained \(L\),
\[
 B_LJ_\epsilon B_L^{-1}=\mathcal K_\epsilon.
 \tag{13}
\]
The possibly large weights \(g_a\) cancel before taking any norm.
This application retains the odd-level scope of [B]; the Fourier
estimate itself also covers even levels.
Here the diagonal is on the beta transform's own input index. This
does not identify a physical crossing degree with an internal beta
index. A ray supplied in another head must first pass through its
actual coupon map; (13) applies only when the resulting input coupon
is the displayed diagonal. A general transported matrix need not
commute with the beta weights.
The same conclusion applies to the inverse and to the original
unit clock factors or index reflection in the two factorial rays.
Such operations merely translate or reverse the Fourier kernel,
with the stated explicit factor \(N\) for the reflected factorial.

For a bilinear exterior row \(\nu\), a change \(v'=\mathcal K v\)
retains its observation as \(\nu v=(\nu\mathcal K^{-1})v'\).
Equation (10) bounds this actual inverse-dual row transport, including
point rows. It does not conjugate the co-source, replace its original
evaluation row, or give a lower bound for \(\nu v\). The affine
evaluation rows and shared index attachments in [B, Section 4]
must still be carried with the transform.

## 3. The holomorphic degree domain and its boundary scale

The integral (1) defines a holomorphic function for \(\Re b>0\),
by its exact modulus and locally integrable domination. For every
compact \(K\subset\{\Re\beta>0\}\),
\[
 I_{N\beta}
 =\frac{\sqrt2 e^{i\epsilon N\pi/24}}
             {N(\beta+i\epsilon c)}\bigl(1+O_K(N^{-1})\bigr).
 \tag{14}
\]
The estimate holds holomorphically, with every fixed \(\beta\)
derivative on smaller compact sets. To prove it, write the phase
as \(\Phi_\beta=\beta\log r+i\epsilon\phi(r)\), and put
\(\ell(r)=r\phi'(r)=\log(1+r)/(2\pi)\). The integration-by-parts
factor is
\[
 \frac{A(r)(1+e_N(r))}{\beta+i\epsilon\ell(r)}.
\]
Its derivative is bounded by \(C_K(1+1/(Nr))\). Since
\(|e^{N\Phi_\beta}|\le r^{N\delta}\), where
\(\delta=\min_K\Re\beta>0\), the remainder is \(O_K(N^{-2})\).
The zero endpoint vanishes. The upper endpoint and (3) give (14).
Cauchy's estimate on a larger compact set gives the derivative
assertion. Thus (14) is zero-free for large \(N\) on each such set.

If a nonintegral degree is defined using the same logarithmic lip,
its ray coefficient includes the additional exact factor
\(-\epsilon e^{i\epsilon\pi b}/(2\pi i)\). This linear exponential
is part of the source, not part of the bounded symbol in (14).

There is a different scale near the imaginary boundary of this
domain. Fix \(b_0\) in a compact subset of \(\Re b_0>0\), and
\(\theta\) in a compact subinterval of \((0,c)\). Set
\[
 b=b_0-i\epsilon N\theta,\qquad
 r_*=e^{2\pi\theta}-1,\qquad
 \psi_\theta(r)=\phi(r)-\theta\log r.
\]
Then
\[
 I_b=\frac{2\pi r_*^{b_0-1/2}(1+r_*)}{\sqrt N}
  e^{i\epsilon N\psi_\theta(r_*)+i\epsilon\pi/4}
     +O(N^{-1}).
 \tag{15}
\]
All powers use the real logarithm of \(r_*\). Here
\(\psi_\theta'=(\ell(r)-\theta)/r\) has its sole zero at \(r_*\),
and \(\psi_\theta''(r_*)=1/[2\pi r_*(1+r_*)]>0\).
Near that point the smooth change of variable
\(u=\operatorname{sgn}(r-r_*)\sqrt{2(\psi_\theta(r)-
\psi_\theta(r_*))}\) reduces the leading integral to the Gaussian
integral \(e^{i\epsilon\pi/4}\sqrt{2\pi/N}\); subtracting its
constant amplitude and integrating the remainder gives \(O(N^{-1})\).
Away from it, one integration by parts gives the same error.
At zero its differentiated amplitude is bounded by a constant times
\(r^{\Re b_0-1}\), which is integrable. The actual error from (3)
has absolute integral \(O(N^{-1})\). This proves (15), including
its nonzero coefficient, without replacing the ray by another cycle.
In particular (14) is not a uniform \(N^{-1}\) symbol up to this
boundary segment. No geometric angle buffer is asserted here.

## 4. The top Mellin normal and its actual zeros

Define the normal by multiplying the original integrand by
\(r^{-\sigma}\), while keeping its integer prefactor. At the top
physical degree this gives
\[
 \widetilde j_{\epsilon,a}(\sigma)
       =-\frac{\epsilon(-1)^{N-a}}{2\pi i}I_{N-a-\sigma},
 \qquad
 \widetilde j_{\epsilon,d}(\sigma)
       =\frac{\epsilon}{2\pi i}I_{1-\sigma},
       \qquad \Re\sigma<1.
 \tag{16}
\]
This is a specified Mellin normal of the ray. It is not a claimed
knot-meridian parameter. If the logarithmic lip factor is continued
as well, the resulting coefficient is
\(e^{-i\epsilon\pi\sigma}\widetilde j_{\epsilon,d}(\sigma)\).
That unit must be retained when comparing the two conventions.

For bounded complex \(s\), uniformly on compact sets,
\[
 N I_{1-s/\log N}
  =i\epsilon\left(\frac{e^s}{c_0}
          -\frac{\sqrt2 e^{i\epsilon N\pi/24}}c\right)
            +O(1/\log N).
 \tag{17}
\]
Here is an elementary two-end proof. Put \(L=\phi(1)=\pi/24\)
and use \(u=\phi(r)\), with inverse \(r=\rho(u)\). For
\(|\sigma|\le1/4\), the classical leading integral becomes
\[
 \int_0^L u^{-\sigma}B_\sigma(u)e^{i\epsilon Nu}\,du,
 \quad B_\sigma(u)=\left(\frac{\rho(u)}u\right)^{-\sigma}
                         A(\rho(u))\rho'(u).
\]
This amplitude is smooth through zero, with uniformly bounded fixed
derivatives, and \(B_\sigma(0)=c_0^{\sigma-1}\).
Separate the two ends by smooth cutoffs. At the upper end two
integrations by parts give \(\sqrt2 e^{i\epsilon NL}/(i\epsilon Nc)
+O(N^{-2})\). At the lower end subtract \(B_\sigma(0)\).
The constant term has the Abel-regularized elementary Laplace integral
\[
 \int_0^\infty u^{-\sigma}e^{i\epsilon Nu}\,du
    =\Gamma(1-\sigma)e^{i\epsilon\pi(1-\sigma)/2}N^{\sigma-1}.
\]
It follows by evaluating the integral with
\(e^{-(\delta-i\epsilon N)u}\), \(\delta>0\), and taking
\(\delta\downarrow0\). The difference made by the cutoff is
\(O(N^{-2})\), by two integrations by parts in the Abel limit;
its second derivative is integrable, uniformly for \(|\sigma|\le1/4\).
The subtracted amplitude is \(u^{1-\sigma}\) times a bounded smooth
function. Splitting at \(1/N\) and integrating twice on the other
interval bounds its integral by \(C N^{-7/4}\log(eN)\), hence by
\(C N^{-3/2}\). All artificial cutoff endpoints cancel.
Consequently
\[
 I_{1-\sigma}^{\rm classical}
 =\frac{\sqrt2 e^{i\epsilon N\pi/24}}{i\epsilon Nc}
  +\Gamma(1-\sigma)e^{i\epsilon\pi(1-\sigma)/2}
                          (Nc_0)^{\sigma-1}+O(N^{-3/2}).
 \tag{18}
\]
For \(\sigma=s/\log N\), the quantum error is
\(O_s(\log N/N^2)\). Indeed split at \(N^{-2}\); the lower
integral of the error in (3) is \(O_s(N^{-3})\), while on the
upper interval the error amplitude and its variation are
\(O_s(N^{-1})\) and \(O_s(\log N/N)\). One integration by parts
gives the assertion, with the same original endpoints.
Finally \(N^\sigma=e^s\) and
\(\Gamma(1-\sigma)c_0^\sigma e^{-i\epsilon\pi\sigma/2}
=1+O_s(1/\log N)\). This proves (17) holomorphically in \(s\).

Write \(A_*=\sqrt2/\log2>1\), and choose a representative
\(\vartheta_{\epsilon,N}\in[-\pi,\pi]\) of
\(\epsilon N\pi/24\) modulo \(2\pi\). The finite set of these
representatives has no level-dependent growth. The limiting function
in (17) has a simple zero at
\(s_{\epsilon,N}^0=\log A_*+i\vartheta_{\epsilon,N}\).
On a small circle around each of these finitely many points, (17)
and Rouché's theorem give a zero of the actual integral. Its location is
\[
 \boxed{\displaystyle
 \sigma_{\epsilon,N}
 =\frac{\log A_*+i\vartheta_{\epsilon,N}}{\log N}
                         +O((\log N)^{-2}),\qquad
 \widetilde j_{\epsilon,d}(\sigma_{\epsilon,N})=0.}
 \tag{19}
\]
The stated error follows by taking circles of radius
\(C/\log N\) in the \(s\)-plane. These zeros lie in
\(\Re\sigma<1\) for all sufficiently large \(N\). Thus the
uniform nonzero physical values do not extend to a zero-free
complex-normal disk of fixed radius.

There is an exact original-source realization of this statement.
The positive Markov cell [M,(1)] has, for every diagonal \(r\),
\[
 \operatorname{Tr}_2[(I\otimes g)\kappa C D U_+
                         (I\otimes r)C^{-1}]
             =\kappa x^{-d}r_0 I.
 \tag{20}
\]
Replace its specified factorial slot by the negative-lip ray with
the Mellin insertion \(r^{-\sigma}\). Its head-\(k\) coefficient
is \(NQ^{d-k}\widetilde j_{+,d-k}(\sigma)\), where the tilde
means that the corresponding integer prefactor is retained as in
(16). Divide by the original nonzero factorial coefficient to
obtain the diagonal in (20). Its pointing is exactly
\[
 h_N(\sigma)=NQ^{-1}\widetilde j_{+,d}(\sigma),
 \qquad
 h_N(s/\log N)
 =Q^{-1}\left(e^s-A_*e^{iN\pi/24}\right)+O(1/\log N).
 \tag{21}
\]
Thus the whole selected ray group is \(h_N(\sigma)\) times the
unchanged arbitrary exterior, with the original Markov scalar
retained as in [M]. Its zeros (19) are zeros of this actual
normalization group. The complementary full source is not declared
zero, and this normal is not identified with a meridian deformation.

The polynomial finite transports (8),(10), the buffered holomorphic
profile (14), and the endpoint phenomena (15),(19) have different
domains. None removes an original fixed-cut postselection or supplies
a geometric-cycle coefficient for an arbitrary mixed pattern.

## Complete direct sources

- [R] [Uniform full-dilogarithm ray transport](research_uniform_full_dilogarithm_ray_transport.md),
  SHA256 5585095f56c1015cabab1409b181eabff4b4dc8fb003191881e97a38a9adf256.
- [B] [Literal beta current and stationary flags](research_literal_beta_current_and_stationary_flags.md),
  SHA256 54d157389fb1b501bd6971fa480f04702372aab692c97006b5f581f18b881b7f.
- [M] [Actual Markov normalization and pruning](actual_markov_ray_normalization_and_pruning.md),
  SHA256 d1572a6b99f9974a7186f2a95cba706d056bb2f693fe49d847d6a7cc68da454a.

The complete direct texts were read and their used implications checked.
No mathematical program or numerical experiment was used.
