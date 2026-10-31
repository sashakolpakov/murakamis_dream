# All odd demands: the projected flux and a concave comparator rate

31 October 2026. Internally reviewed analytical theorem. Root and coherent completed
full independent internal proof/source reviews. This concerns only the
original fixed cap/CROSS spectral pair. It proves a subexponential
comparison to the actual odd endpoint reference, not a polynomial
bound or a uniform statement for nearby spectra.

## 1. Statement and retained source

Let \(N=2m+1\ge3\), \(d=2m\), \(M=m-1\). Keep the original pair
\(E=(A,0,C,Z)\), \(F=(0,A,0,C)\), its \(A^d\) demand, raw spectral
values \((-2,+2)\), and all unused factors. Define
\[
 T_n=\sum_{j=\max(0,n-m)}^{\min(M,n)}
       (-1)^jU_jC_{j,n-j},\qquad
 D_n^o=\sum_{j=\max(0,n-m)}^{\min(M,n)}
       V_j^o\overline C_{j,n-j}.
                                                               \tag{1}
\]
Here \(\overline C,V^o\) are exactly the CROSS/RIGHT coefficients
of the actual odd regularizer
\(F_N=V_N(-2)-N^{-2}\partial_\sigma V_N(-2)\).
The scalar definitions and continuant are those of the
[original-demand source](research_two_port_main_cap_original_demand_convolution.md),
sections 1–2; their odd extension, including the zero unused factor,
is proved in the [odd raw-source theorem](research_cap_cross_odd_low_demand_subexponential_extension.md),
section 1. The numerator remains raw. The ranges in (1) are the original
finite ranges, not complete sums introduced above the low cutoff.

**Theorem.**
\[
 \limsup_{\substack{N\to\infty\\N\ \mathrm{odd}}}
 \frac1N\log\max_{0\le n\le N-2}
                     \frac{|T_n|}{D_n^o}\le0.          \tag{2}
\]
All denominators are positive in this range. The empty degree \(n=d\)
is not included in the ratio.

The already reviewed
[odd low-demand theorem](research_cap_cross_odd_low_demand_subexponential_extension.md)
proves (2) for \(n\le M\). The original
[all-parity high-demand theorem](research_cap_cross_high_demand_signed_contraction.md)
gives \(|T_n|\le4N D_n^o\) for
\[
             n\ge n_H:=\lceil3N/4-3/2\rceil .
\]
It remains to bridge \(m\le n<n_H\).

## 2. Exact recurrence of the projected source

Use the genuine Newton polynomial
\[
 F^P(z)=\sum_{j=0}^{M}(-1)^jU_j\widehat B_j(z).
\]
At the protected cap it has exactly its original RIGHT monomials.
The literal Newton multiplication rule gives
\[
 (2-z)F^P(z)=4+K_N\widehat B_m(z),\qquad
 K_N=(-1)^M s_m^2U_M.                                 \tag{3}
\]
Indeed all intermediate coefficients cancel using
\(\gamma_jU_j=s_j^2U_{j-1}\), and the omitted top coefficient is
exactly the second term of (3).

At odd level the raw E coefficient \(C_{j,h}\) vanishes for \(h>m\)
because its unused suffix contains \(a_m=0\).
Thus using full raw E with \(F^P\) is precisely (1), including its
moving lower cutoff. The exact physical three-port adapter identifies
the \(\widehat B_m\) insertion with \(C_{m,n-m}\), and therefore
\[
 \boxed{\gamma_nT_n+s_n^2T_{n-1}
       =4C_{0,n}+K_N C_{m,n-m},}
 \quad T_{-1}=0,                                      \tag{4}
\]
where out-of-range \(C\)'s are zero.
The [literal Newton source adapter](research_cap_cross_low_demand_newton_contraction.md),
section 2, and its [raw odd extension](research_cap_cross_odd_low_demand_subexponential_extension.md),
section 1, prove this with all original turns and demands: inserting
\(\widehat B_m\) at the cap inserts exactly the monomial
\(A^{d-m}C^m\), and hence gives the single coefficient
\(C_{m,n-m}\). Multiplying the resulting Newton row by
\(2I-Z_N\) proves (4). No projected tensor covariance is assumed.
For \(n\ge m+1\), \(C_{0,n}=0\). At \(n=m\), \(C_{0,m}=N^2\).
Also \(s_m^2U_M=4N\), by the exact odd endpoint products.
Thus the forcing prefactors are polynomial and no central zero is
divided out.

For all indices between \(M\) and \(n_H\), both \(s_n^2\) and
\(\gamma_n\) are bounded above and below by positive absolute constants
for sufficiently large \(N\). Furthermore
\[
 r_n:=\frac{s_n^2}{\gamma_n}
    =\frac{\sin^2(n\theta)}{\sin^2((n+1/2)\theta)},
 \qquad |\log r_n|\le C/N.                             \tag{5}
\]
Hence every forward or backward product over a subinterval of these
indices is bounded by a fixed constant. This is the raw recurrence;
the much larger normalized coefficient \(t_n\) is not used here.

## 3. Actual two-sided endpoint coefficient asymptotics

Put
\[
 f(t)=-\int_0^t\log\tan(\pi s)\,ds,\quad0\le t\le1/2,
 \qquad u=n/d,\quad v=j/d.
\]
The genuine odd cap-reference product is
\[
 V_j^o=\frac{\prod_{r=1}^j s_r^2}
                    {\prod_{r=0}^j a_r},\qquad j\le M.
                                                               \tag{6}
\]
The exact noncentral product \(\prod_{r\ne m}a_r=N^2\) proves
(6), without dividing by \(a_m\). Uniform sine/cosine logarithmic
sums give
\[
                  N^{-1}\log V_j^o=-2f(v)+o(1)         \tag{7}
\]
uniformly up to both endpoints.

The needed E estimate is a genuine CLOSED upper and lower theorem:
[odd regularized full numerator](actual_fejer_odd_regularized_full_numerator.md),
section 3, equations (8)--(11), proves the exact raw factorization
\[
 H_{V_N(-2)}=N^2D_m(A,0,Z)D_m(A,C,Z)
\]
on these protected inputs. Each positive \(D_m\) coefficient has
uniform closed triangle entropy
\(\mathcal C(\alpha)=\sum_i f(\alpha_i)\), with total load \(1/2\).
Its proof retains the actual positive first term in its equation (9)
and the trim/fill lower estimates; it is not the general upper-only
sharp LIMSUP theorem. Equations (3),(7) of that reference also compare
the actual regularized CROSS coefficient to this raw positive
factorization by uniform constant factors.

For \(C_{j,h}\), let \(k\) be the first triangle's A-degree.
The original positive convolution has precisely the integer interval
\[
 \max(0,j+h-m)\le k\le\min(m,j).                        \tag{8}
\]
Its two normalized triangle loads are
\[
 (a,0,\tfrac12-a),\qquad
 (v-a,u-v,\tfrac12-u+a),\qquad a=k/d.
\]
Thus the E entropy is
\[
 \mathcal{H}_E(u,v)=
 \max_{\max(0,u-1/2)\le a\le\min(1/2,v)}
 \{2f(a)+f(v-a)+f(u-v)+f(u-a)\}.                       \tag{9}
\]
The third f in the second triangle was reflected using
\(f(1/2-t)=f(t)\).
The positive convolution, its polynomial number of terms, and
rounding \(k\) within (8) prove uniform matching logarithmic upper
and lower estimates for (9). This includes a zero middle load and
the original central-row boundary. Replacing d-normalization by
N-normalization changes every argument by \(O(1/N)\); uniform CLOSED
continuity absorbs it.

For \(u\ge1/2\), write \(t=u-1/2\). Combining (7),(9), the limiting
reference objective is
\[
 E(a,v;u)=2f(a)+f(v-a)+f(u-v)+f(u-a)-2f(v),
       \qquad t\le a\le v\le1/2.                      \tag{10}
\]
In the interior,
\[
 \partial_v E=
 \log\frac{\tan(\pi(u-v))\tan^2(\pi v)}
                 {\tan(\pi(v-a))}>0.                 \tag{11}
\]
Indeed \(u-v\ge1/2-v\), and \(v-a\le v\), with strictness except
the harmless boundary \(u=1/2,a=0\). Therefore the closed maximum
is attained at \(v=1/2\), and its value is
\[
 J(u)= f(t)+\max_{t\le a\le1/2}
                     \{3f(a)+f(a-t)\}.               \tag{12}
\]

For the ACTUAL finite comparator, \(j=M\) is allowed and has
\(v=1/2-1/d\), tending to that maximizer. At this j, the genuine
latent interval (8) is \(n-m\le k\le M\). Rounding the limiting
maximizer into this interval moves a by at most \(O(1/d)\).
This proves the required lower estimate, not just an upper capacity.
Consequently, uniformly for \(m\le n\le n_H\), including the backward
initial endpoint \(n_H\),
\[
          N^{-1}\log D_n^o=J(n/d)+o(1).                \tag{13}
\]
The same statement extends to the adjacent low endpoint \(n=M\)
by continuity, with value \(J(1/2)+o(1)\).

The flux \(C_{m,n-m}\) has \(v=1/2\) exactly and no cap factor.
Its limiting E action in (9) is precisely (12). In particular the
uniform closed upper estimate gives
\[
        |4C_{0,n}+K_N C_{m,n-m}|
              \le\exp\{N[J(n/d)+o(1)]\}               \tag{14}
\]
on the middle interval. At \(n=m\), its extra \(4N^2\) term also
satisfies this estimate, since \(J(1/2)>0\).
All errors in (13)--(14) are uniform over the actual finite indices.

## 4. Concavity supplies the two propagation directions

The function
\[
                f(t)+3f(a)+f(a-t)
\]
is jointly concave on \(0\le t\le a\le1/2\).
Maximizing over a preserves concavity in t. The strict concavity
of \(f(t)\) makes J strictly concave on the open interval.
The maximizing a is uniquely interior for \(0<t<1/2\); it obeys
\(3f'(a)+f'(a-t)=0\). The envelope derivative is
\[
                    J'(u)=f'(t)-f'(a-t).              \tag{15}
\]
At \(t\downarrow0\), \(a\to1/4\) and this derivative tends to
\(+\infty\). At \(t=1/4\), the maximizer lies strictly between
\(1/4\) and \(1/2\), so (15) is negative. Thus J has one peak
\(u_*\in(1/2,3/4)\), increasing before it and decreasing after it.

Solve (4) forward from \(M\) for indices \(n/d\le u_*\).
The initial low theorem bounds \(|T_M|\) by
\(\exp\{N[J(1/2)+o(1)]\}\). Every forcing in the resulting finite
sum has rate at most \(J(n/d)+o(1)\), by (14) and monotonicity.
Equation (5) bounds the propagation factors and there are only
O(N) terms. Hence
\[
                 |T_n|\le e^{N[J(n/d)+o(1)]}           \tag{16}
\]
uniformly on that side.

On the other side, solve (4) BACKWARD from \(n_H\), using the
proved high-demand inequality \(|T_{n_H}|\le4N D_{n_H}^o\).
For all sufficiently large N, \(n_H/d>u_*\).
Every encountered forcing and the boundary term now has rate at
most \(J(n/d)+o(1)\), since J decreases on this side.
The inverse propagation products are also bounded by (5).
Thus (16) holds uniformly here as well. Integer rounding at the
single peak costs \(o(1)\) in rate by continuity.

Divide (16) by the actual lower estimate (13). This proves (2)
on the missing middle interval; combine it with the low and high
theorems to obtain every \(0\le n\le N-2\).

## Scope and review status

The proof uses the raw odd projected recurrence, a genuine positive
endpoint coefficient LOWER theorem, and a uniform two-sided
comparator rate. It does not replace the original cutoff sum by
its full auxiliary slice above M, use a norm bound, or infer
finite monotonicity of the individual comparator coefficients.

The even projected source has an additional E-boundary term and is
not covered by this argument. No spectral neighborhood, whole-source
dominance, or new filled-volume conclusion is asserted.
Root and coherent independently checked the complete source/flux
identity, actual uniform closed coefficient lower, comparator
concavity, and both propagation directions. These are internal
reviews, not external peer review. The
[all-parity theorem](research_cap_cross_all_demand_subexponential_contraction.md)
retains this result and proves the additional even cutoff-current bound.
