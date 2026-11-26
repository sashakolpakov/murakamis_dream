# Actual reduced-generator transport of a Fourier packet

Private written proof, 19 November 2026.

The opened positive generator on two remaining heads sends a specified
physical Fourier packet to a nonzero Gaussian packet. Its exponential
gain, scalar amplitude, chirps, and physical endpoints can all be retained.
This is a statement about the actual reduced generator, with its original
crossing scalar. It does not estimate a closed braid source or claim that
the output remains in the incoming Fourier band.

The complete directs are R for the actual reduced generator and F for
the physical Fourier band and its packet normalization. Every additional
finite-product and asymptotic argument is given below.

## 1. The exact finite transport matrix

Put
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad x=-q^{-1},
 \qquad f_j=\prod_{b=1}^j(1-Q^b),\quad f_0=1.
\]
Work at the actual root meridian \(M=1\). Let
\(T=d-H\), \(1\le H<N/2\), and use the physical degree-\(T\)
basis \(|a,T-a\rangle\), \(0\le a\le T\). R gives
\[
 X=\mathcal B_3(R_1)=\kappa S_2D_{\rm red},\quad
 S_2=\sum_{n=0}^d\frac{(x^{-1}L_1F_2)^n}{f_n},\quad
 D_{\rm red}(a)=(-1)^a q^{a(a+1)}.
 \tag{1}
\]
Here \(L_1\) is the literal lowering shift, with zero vacuum arrow.
The original scalar \(\kappa\) is not removed from the operator.

For \(0\le s<H\), put \(u_s(a)=x^aQ^{-sa}\). Since
\(D_{\rm red}u_s(a)=q^{a^2}Q^{-sa}\), the output row \(c\) is
\[
 \begin{split}
 (\kappa^{-1}Xu_s)_c
 &=q^{c^2}Q^{-sc}
   \sum_{n=0}^{T-c}{T-c\brack n}_Q
        (-1)^nQ^{n(n-1)/2}(Q^{c-s+1})^n\\
 &=q^{c^2}Q^{-sc}(Q^{c-s+1};Q)_{T-c}.
 \end{split}                                                    \tag{2}
\]
Indeed the transfer \(n\) starts at first occupation \(c+n\),
and its coefficient is
\(x^{-n}f_{T-c}/(f_nf_{T-c-n})\). This gives the first row;
expanding the finite product gives the second. All intermediate
occupations lie in the physical interval. For the indicated band,
\[
 (\kappa^{-1}Xu_s)_c=
 \begin{cases}
 0,&c<s,\\
 q^{c^2}Q^{-sc}f_{T-s}/f_{c-s},&s\le c\le T.
 \end{cases}                                                    \tag{3}
\]
The zero in the first case is the literal factor \(1-Q^0\).
There is no cyclic replacement of an endpoint.

Write \(\mathfrak s_j=\prod_{b=1}^j2\sin(\pi b/N)>0\) for
\(0\le j<N\). The identity
\(f_j=(-i)^j q^{j(j+1)/2}\mathfrak s_j\) turns (3) into
\[
 (\kappa^{-1}Xu_s)_c
   =\omega_c q^{-(T+c)s}
                      \frac{\mathfrak s_{T-s}}{\mathfrak s_{c-s}},
 \quad
 \omega_c=(-i)^{T-c}
            q^{c^2+(T-c)(T+c+1)/2},\qquad c\ge s.
 \tag{4}
\]
In particular the remaining phase is exactly affine in the
frequency \(s\), while the displayed quotient is positive.

## 2. Uniform choice of physical packets

Fix \(0<\eta_-<\eta_+<1/2\) and suppose
\(\eta_-\le H/N\le\eta_+\). Choose a sufficiently small fixed
\(\delta_0>0\), depending only on this compact interval, and set
\[
 s_0=\lfloor H/3\rfloor,\quad L=\lfloor\delta_0N\rfloor,
 \quad \sigma_0=s_0/N,\quad\delta=L/N,\quad\tau=T/N.
 \tag{5}
\]
All assertions below hold for sufficiently large \(N\). The
choice can ensure that \([s_0,s_0+L]\) has a proportional margin
inside \([0,H-1]\), and that
\[
 \tau-\sigma\in U\Subset(1/6,1)
 \quad(\sigma_0\le\sigma\le\sigma_0+\delta)
 \tag{6}
\]
for one fixed interval \(U\). In fact its limiting endpoints
are near \(1-4H/(3N)\). The exact \(d=N-1\) is retained in \(\tau\).

Let
\[
 J(t)=\int_0^t\log(2\sin\pi v)\,dv,\qquad
 h(p)=-p\log p-(1-p)\log(1-p).
\]
For \(\sigma=\sigma_0+\delta p\), \(0\le p\le1\), define
\[
 F(\xi,\sigma)=\delta[h(p)-\log2]
                +J(\tau-\sigma)-J(\xi-\sigma),
 \qquad \sigma\le\xi\le\tau.
 \tag{7}
\]
The function \(J\) has its unique minimum on \([0,1]\) at
\(1/6\): its derivative is negative on \((0,1/6)\), positive
on \((1/6,5/6)\), negative on \((5/6,1)\), and
\(J(0)=J(1)=0>J(1/6)\). Thus maximizing first in \(\xi\)
sets \(\xi=\sigma+1/6\). The remaining second derivative is
\[
 -\frac1{\delta p(1-p)}+\pi\cot(\pi(\tau-\sigma)).
 \tag{8}
\]
For sufficiently small \(\delta_0\) this is uniformly negative.
The first derivative tends to opposite infinities at the two
ends, so there is one maximum, characterized by
\[
 \sigma_* =\sigma_0+\delta p_*,\quad
 p_*=\frac1{1+2\sin\pi(\tau-\sigma_*)},\quad
 \xi_* =\sigma_*+\frac16,\quad F_*=F(\xi_*,\sigma_*).
 \tag{9}
\]
All these quantities may depend on \(N\); no limiting grid
parameter is substituted. They stay in protected interior
compacts. Shrinking \(\delta_0\) again gives \(F_*\ge c>0\):
on \(U\), \(J(u)-J(1/6)\) has a positive minimum, whereas
the entropy loss has modulus at most \(\delta\log2\).

Choose \(a_0\) to be a nearest integer to
\(N(\tau+\xi_*)/2\), and define the unit frequency vector
\[
 b_{s_0+j}=
 \frac{2^{-L}\binom Lj Q^{a_0(s_0+j)}}{\nu_L},\quad
 \nu_L^2=4^{-L}\binom{2L}{L},\quad0\le j\le L.
 \tag{10}
\]
All other frequencies vanish. Let \(v\) be its full unitary
Fourier transform followed by \(x^a\), and restrict it to
the actual physical interval:
\[
 v^{\rm phys}_a=\frac1{\sqrt N}\sum_s b_s x^aQ^{-sa},
 \qquad0\le a\le T.
 \tag{11}
\]
The center \(a_0\) is a proportional distance from both physical
ends by (6),(9). F's exact cosine formula, or its proof applied
to (10), gives
\[
 \|v^{\rm phys}\|_2^2=1+O(e^{-cN}),\qquad
 v^{\rm phys}\in\operatorname{im}A^\vee.
 \tag{12}
\]
The second assertion uses precisely F's actual Fourier image;
no orthogonal spectral projector is identified with it.

## 3. Exact packet formula and its nonzero Gaussian limit

Put \(w=Xv^{\rm phys}\). Equations (3)--(4) give the exact sum
\[
 w_c=\frac{\kappa\omega_c}{\sqrt N\,\nu_L}
 \sum_{\substack{0\le j\le L\\s=s_0+j\le c}}
       2^{-L}\binom Lj
       \frac{\mathfrak s_{T-s}}{\mathfrak s_{c-s}}
       q^{(2a_0-T-c)s},\qquad0\le c\le T.
 \tag{13}
\]
In particular the deleted part of the frequency range is
specified exactly even for rows near the lower physical end.

Define the positive quantities and complex Gaussian parameter
\[
 \begin{split}
 u_*&=\tau-\sigma_*,\qquad b=\pi\sqrt3,\\
 a&=\frac1{\delta p_*(1-p_*)}-\pi\cot(\pi u_*)+b,\\
 \Gamma&=b-\frac{(b-i\pi)^2}{a},\\
 A_*&=\pi^{1/4}\delta^{-1/4}
      \sqrt{\frac{2\sin\pi u_*}{a p_*(1-p_*)}}.
 \end{split}                                                    \tag{14}
\]
Our choice of \(\delta_0\) ensures \(a>2b\), so
\(\operatorname{Re}\Gamma>0\) uniformly. Also \(A_*\) and
its inverse are uniformly bounded. Set
\(z_c=(c-N\xi_*)/\sqrt N\). For every fixed \(R>0\),
uniformly for the actual integer rows with \(|z_c|\le R\),
\[
 \boxed{\quad
 w_c=\kappa\omega_c
       e^{i\pi(2a_0-T-c)\sigma_*}
       N^{-1/4}e^{NF_*}A_*
       e^{-\Gamma z_c^2/2}\bigl(1+O_R(N^{-1/2})\bigr).
 \quad}                                                        \tag{15}
\]
Both phases in front have modulus one. The bounded rounding
\(2a_0-T-N\xi_*\) is retained in the displayed phase; its
effect inside the Gaussian sum is part of the stated error.

Here is a proof including the prefactor. For \(\xi,\sigma\)
in a fixed neighborhood of their maximum, the endpoints of
the sine product are away from zero and one. The elementary
Euler--Maclaurin estimate for its logarithm gives
\[
 \frac{\mathfrak s_{T-s}}{\mathfrak s_{c-s}}
 =e^{N[J(\tau-\sigma)-J(\xi-\sigma)]}
  \sqrt{\frac{\sin\pi(\tau-\sigma)}
                    {\sin\pi(\xi-\sigma)}}(1+O(N^{-1})).
 \tag{16}
\]
Stirling's formula, uniformly for \(p\) in an interior
compact, gives
\[
 2^{-L}\binom Lj=\frac{e^{N\delta[h(p)-\log2]}}
                  {\sqrt{2\pi N\delta p(1-p)}}(1+O(N^{-1})),
 \quad \nu_L=(\pi N\delta)^{-1/4}(1+O(N^{-1})).
 \tag{17}
\]
The Hessian of \(F\), in the ordered variables \((\xi,\sigma)\),
at the maximum is
\[
                 \begin{pmatrix}-b&b\\b&-a\end{pmatrix}.
 \tag{18}
\]
Writing \(s=N\sigma_*+y\sqrt N\), the phase remaining after
the one displayed in (15) is
\(e^{-i\pi z_c y}(1+O_R((1+|y|)/\sqrt N))\).
The limiting Gaussian integral is therefore
\[
 \int_{\mathbb R}e^{-ay^2/2+(b-i\pi)z_cy-bz_c^2/2}\,dy
     =\sqrt{2\pi/a}\,e^{-\Gamma z_c^2/2}.
 \tag{19}
\]
Combining (16)--(19), including \(N^{-1/2}\nu_L^{-1}\)
from (13) and the \(\sqrt N\) sum spacing, yields exactly
\(N^{-1/4}A_*\). Taylor's cubic remainder is bounded by
\(C(1+|y|^3)/\sqrt N\) on a growing central range; splitting
off its Gaussian tails makes the integrated error
\(O_R(N^{-1/2})\). The sum-to-integral error has that bound
by integrating the absolute derivative of the Gaussian
summand. These estimates are uniform in the compact parameters.
The nonzero Gaussian in (19) is bounded away from zero for
\(|z_c|\le R\), so the displayed error is relative.

## 4. Entire-cap control and the transported norm

For completeness the local computation has a global positive
majorant. Uniformly for all physical rows,
\[
 |w_c|\le C|\kappa|N^{-1/4}e^{NF_*}
                   e^{-c_1(c-N\xi_*)^2/N}.
 \tag{20}
\]
We prove this with the actual truncated sum in (13). First,
for \(0\le k\le(1-\epsilon)N\), one has
\[
 \log\mathfrak s_k=NJ(k/N)+O(\log N).
 \tag{21}
\]
One direct proof factors each sine as
\((2\pi j/N)\,\sin(\pi j/N)/(\pi j/N)\). The second
factor has a smooth logarithm on the indicated interval;
the trapezoidal bound and the elementary factorial bounds
give (21), including \(k=0\). Also
\(\binom Lj\le e^{Lh(j/L)}\), by the binomial theorem at
its positive optimizing argument, including both endpoints.
Thus the whole sum is bounded by a fixed power of \(N\)
times the exponential of its maximum \(NF\).

The maximum established in (9) is unique on the compact
triangular domain in (7). At that maximum its Hessian is
uniformly negative definite. Consequently, on that entire domain,
\[
 F_* - F(\xi,\sigma)
       \ge c_2\bigl((\xi-\xi_*)^2+(\sigma-\sigma_*)^2\bigr).
 \tag{22}
\]
To see the global constant, use the Hessian on a common small
neighborhood; on its complement uniqueness and compactness
give a fixed gap, which bounds the squared distance there.
All parameter sets are compact after allowing the harmless
grid offsets. This also covers \(\xi=\sigma\), where \(J\)
is continuous but its derivative is singular.

In that common small neighborhood, (16)--(17) bounded above
and the elementary Gaussian lattice-sum bound give (20)
with its \(N^{-1/4}\) prefactor. Outside it, (21)--(22)
give a fixed exponential loss. Shrinking the constant in
the Gaussian exponent absorbs the polynomial prefactor
and the sum length. This proves (20) without extending any
physical cap. In particular every macroscopic output tail
has exponentially small norm relative to \(e^{NF_*}|\kappa|\).

Equations (15),(20) and a Gaussian Riemann sum now imply
\[
 \boxed{\quad
 \|Xv^{\rm phys}\|_2
  =|\kappa|e^{NF_*}A_*
        \left(\frac{\pi}{\operatorname{Re}\Gamma}\right)^{1/4}
        (1+o(1)).
 \quad}                                                        \tag{23}
\]
The error is uniform over the indicated compact degree range.
Indeed first sum on \(|z_c|\le R\), using (15); then (20)
makes the complementary squared norm uniformly small as
\(R\to\infty\). This argument needs no unproved relative
estimate on a far oscillatory sum. Dividing (15) by (23)
describes the normalized outgoing Gaussian packet, including
its exact chirps. Equation (12) supplies the incoming
normalization. Since \(F_*\ge c>0\), its gain after dividing
by the retained scalar \(|\kappa|\) is exponential on these
inputs of norm \(1+O(e^{-cN})\).

## 5. Source and parameter scope

The theorem concerns an opened generator in the original
finite reduced representation. Incoming packets belong to
the complementary Gauss image by F, but their images under
\(X\) have not been shown to lie in that same band. No
almost-invariance, control of a whole word, or nonzero closing
pairing follows from (15),(23). In particular the exact
pointed/pivotal row in R is not a positive squared norm.
All prescribed external framing scalars must still be
multiplied when this generator occurs in an invariant word.
The maximizing frequency \(\sigma_*\) need not be the center
\(\sigma_0+\delta/2\) of the incoming binomial weight: the actual
factorial quotient tilts that weight. No claim that an incoming
microscopic frequency window alone supplies (15) is made.

The phase cancellation in (4) and all estimates are at
\(M=1,q=e^{\pi i/N}\). No meridian or quantum normal is
obtained by differentiating this root statement. There is
also no identification with a geometric holonomy or a
contributing relative cycle. What is paid is actual finite
transport of a family of physical band packets, with both
endpoints, output localization, and nonzero scalar amplitude.

## Complete proof directs

* R: notes/research_actual_reduced_braid_source.md,
  SHA256 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* F: notes/research_dual_gauss_fourier_band_and_square.md,
  SHA256 3abc3ae81367e72bd56045292261c7eea1fb22ceeed379ad4cd64013f4148038.

Both complete directs were freshly whole-read in this author
sequence, with the matching F also read in the immediately
preceding formal review. Every used implication was checked.
Only written mathematics and text/hash operations were used.
Frozen and public files were not changed.
