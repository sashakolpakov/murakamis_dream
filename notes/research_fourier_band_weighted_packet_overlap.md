# A physical Fourier-band state in the weighted generator chart

Private written proof, 19 November 2026.

The weighted occupation packet for the actual opened generator can be
replaced by a vector in the exact complementary Gauss image, with an
exponentially small error in the retained source frame. The replacement
uses the ordinary unitary Fourier projector on the full finite cycle,
followed by physical restriction. Its carrier condition and diagonal
conditioning cost are explicit. The nonzero Gaussian image, norm
comparison, and both original annular-window currents then persist.

This is a local overlap theorem for a universal source brick. Neither
an arbitrary window preserving the Gauss range nor a bounded inverse
of a Gauss factor is asserted. The complete directs are W for weighted
generator transport and F for the exact Fourier-band image.

## 1. The actual matrix, frames, and original packet

Use
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad x=-q^{-1},
 \quad T=d-H,\quad 1\le H<N/2.
\]
Suppose \(H/N\) lies in a fixed compact subset of \((0,1/2)\).
All spaces, matrices, and norms are the physical occupation spaces
and Euclidean norms used in W and F. On degree \(T\), W gives the
actual positive reduced generator
\[
 X_{c,a}=\kappa(-1)^c q^{(T+c+2)a-(T+1)c}
     \frac{\mathfrak s_{T-c}}
          {\mathfrak s_{a-c}\mathfrak s_{T-a}},
 \quad0\le c\le a\le T,
 \quad\mathfrak s_j=\prod_{b=1}^j2\sin(\pi b/N),
 \tag{1}
\]
and zero otherwise. The original crossing scalar \(\kappa\)
and every finite cap remain.

Choose W's protected interior parameters
\[
 \tau=T/N,\quad \xi_*=c_*/N,\quad
 \eta_*=(a_0+L/2)/N,\quad L=\lfloor\delta_0N\rfloor,
 \quad\delta=L/N,
 \qquad0<\xi_*<\eta_*<\tau<1.
 \tag{2}
\]
The triples lie in one fixed compact interior subset, and
\(\delta_0>0\) is sufficiently small as in W. All indices
\(a_0,\ldots,a_0+L\) are physical. Set
\[
 u_*=\eta_*-\xi_*,\quad v_*=\tau-\eta_*,\quad
 w_*=1-\tau+\xi_*,\quad
 \lambda=\log\frac{\sin\pi u_*}{\sin\pi v_*},\quad
 \mu=\log\frac{\sin\pi w_*}{\sin\pi u_*}.
 \tag{3}
\]
The letter \(\mu\) here denotes W's real output weight, not a
meridian parameter. Define the retained diagonal frames and packet
\[
 D_{\rm in}(a)=e^{\lambda a},\quad D_{\rm out}(c)=e^{\mu c},
 \quad Y=D_{\rm out}XD_{\rm in},
\]
\[
 b_{a_0+j}=\frac{2^{-L}\binom Lj}{\nu_L}
             q^{-(T+c_*+2)(a_0+j)},\quad
 \nu_L^2=4^{-L}\binom{2L}{L},\quad0\le j\le L,
 \tag{4}
\]
with all other coefficients zero. Thus \(\|b\|_2=1\).

For explicit reference write \(J(t)=\int_0^t\log(2\sin\pi s)ds\),
\[
 S_*=-J(u_*)-J(v_*)-J(w_*)+\lambda\eta_*+\mu\xi_*.
 \tag{5}
\]
W proves \(\|Y\|\le C|\kappa|e^{NS_*}\) and
\(\|Yb\|\ge c|\kappa|e^{NS_*}\), as well as its full
Gaussian output and exact annular-current estimates. These
are estimates of the whole physical matrix, not of one
selected entry. This norm comparison will pay the replacement.

## 2. The exact carrier and a quantitative overlap condition

Let \(\mathcal H_N=\mathbb C^{\{0,\ldots,N-1\}}\), and let
\(E_T:U_T\to\mathcal H_N\) extend a vector by zero. Its adjoint
\(R_T\) is physical restriction. On \(\mathcal H_N\) the unitary
Fourier matrix adapted to F is
\[
 (\mathcal U_N)_{a,s}=N^{-1/2}x^aQ^{-sa}.
\]
Define the genuine orthogonal cyclic projector
\[
 \Pi_H=\mathcal U_N\operatorname{diag}({\bf1}_{0\le s<H})
                       \mathcal U_N^*.
 \tag{6}
\]
F proves
\[
 R_T\operatorname{im}\Pi_H
       =\operatorname{im}A^\vee
       =\operatorname{span}\{x^aQ^{-sa}:0\le s<H\}_{a=0}^T.
 \tag{7}
\]
The projector (6) is not identified with a Casimir Riesz projector
on the physical space.

Retain the half-integral carrier
\[
                         s_*=(c_*-H)/2.
 \tag{8}
\]
It is exact: since \(T=N-H-1\),
\[
 q^{-(T+c_*+2)a}=x^aQ^{-s_*a}
 \qquad(a\in\mathbb Z).
 \tag{9}
\]
Indeed the quotient of the two sides is
\((-1)^a q^{-Na}=1\). No rounding of \(s_*\) or of the
\(+2\) in the actual crossing is made.

Assume, for one fixed \(0<g<1/2\),
\[
                   gN\le s_*\le H-gN.
 \tag{10}
\]
Thus every integer frequency outside \([0,H-1]\) has circular
distance at least \(gN\) from \(s_*\). In terms of actual
output occupations this requires
\(H+2gN\le c_*\le3H-2gN\), as well as the protected physical
constraints in (2). This is an explicit restriction of the chart;
no coverage of every weighted triangle is asserted.

Put \(p_\lambda=e^\lambda/(1+e^\lambda)\). The quantitative
conditioning condition is
\[
 2\delta p_\lambda(1-p_\lambda)\sin^2(\pi g)
                  -|\lambda|\tau\ \ge\epsilon>0
 \tag{11}
\]
with \(\epsilon\) fixed. It always holds with a positive uniform
gap when \(\lambda=0\). It also includes a fixed open collar:
for large \(N\), \(\delta\ge\delta_0/2\), and
\(p_\lambda(1-p_\lambda)\ge1/8\) for \(|\lambda|\le1\).
For example
\[
 |\lambda|\le\min\{1,\delta_0\sin^2(\pi g)/16\}
 \tag{12}
\]
implies (11) with \(\epsilon=\delta_0\sin^2(\pi g)/16\).

With \(g>0\) chosen sufficiently small for the degree compact,
these conditions are nonempty uniformly. Choose \(\xi_*\) strictly between
\(H/N\) and \(\min(3H/N,\tau)\), with fixed margins,
then \(\eta_*=(\tau+\xi_*)/2\). This gives \(u_*=v_*\),
hence \(\lambda=0\), and leaves all triangle angles positive.
The interval of choices has positive width on a compact degree
range. When exact integer choices are wanted on this balanced
subfamily, choose the bounded rounding of \(c_*\) with parity
\(T+c_*-L\) even, and put \(a_0=(T+c_*-L)/2\). All margins
persist. Small changes of the interior input location give the
open regime (11); no continuous occupation has replaced the finite
indices.

## 3. Project first, then restrict: the actual range vector

Define the physical band vector and its weighted representative by
\[
 v^{\rm band}=R_T\Pi_HE_TD_{\rm in}b,
 \qquad b^{\rm band}=D_{\rm in}^{-1}v^{\rm band}.
 \tag{13}
\]
Then (7) gives exact membership in \(\operatorname{im}A^\vee\).
The intermediate cyclic vector may have nonzero occupations above
\(T\); (13) explicitly restricts them. There is no assertion
that \(R_T\Pi_HE_T\) is an idempotent on the physical space.

The full-cycle Fourier coefficients of \(E_TD_{\rm in}b\) are
the literal binomial polynomial
\[
 (\mathcal U_N^*E_TD_{\rm in}b)_s
  =\frac{e^{\lambda a_0}Q^{(s-s_*)a_0}}
               {\sqrt N\,\nu_L}
       \left(\frac{1+e^\lambda Q^{s-s_*}}2\right)^L.
 \tag{14}
\]
This is valid also for a half-integral \(s_*\). The finite packet
support in (4) proves it directly. For circular distance at least
\(gN\),
\[
 \left|\frac{1+e^\lambda Q^{s-s_*}}{1+e^\lambda}\right|^2
 =1-4p_\lambda(1-p_\lambda)
                    \sin^2\!\frac{\pi(s-s_*)}{N}
 \le e^{-4p_\lambda(1-p_\lambda)\sin^2(\pi g)}.
 \tag{15}
\]
Moreover
\(e^{\lambda a_0}((1+e^\lambda)/2)^L\le
e^{\max(\lambda,0)T}\), since it is a positive convex
combination of \(e^{\lambda a}\) on the actual packet support.
Using \(\nu_L^{-1}\le CN^{1/4}\), summing the at most \(N\)
omitted squared coefficients, and using full Plancherel gives
\[
 \|(I-\Pi_H)E_TD_{\rm in}b\|
 \le CN^{1/4}
       e^{\max(\lambda,0)T-2Lp_\lambda(1-p_\lambda)
                                      \sin^2(\pi g)}.
 \tag{16}
\]
Physical restriction is a contraction and
\(\|D_{\rm in}^{-1}\|=e^{\max(-\lambda,0)T}\).
Consequently (11),(13),(16) prove
\[
 \boxed{\quad
 \|b^{\rm band}-b\|\le CN^{1/4}e^{-\epsilon N}
                         \le Ce^{-\epsilon N/2},\qquad
 \|b^{\rm band}\|=1+O(e^{-\epsilon N/2}).
 \quad}                                                       \tag{17}
\]
This explicitly pays the diagonal condition number rather than
discarding it. The norm of the unweighted physical vector
\(v^{\rm band}\) is not asserted to be one.

## 4. Gaussian transport and both original annular currents

The complete matrix norm in Section 1 and (17) give
\[
 \|D_{\rm out}Xv^{\rm band}-Yb\|
       =\|Y(b^{\rm band}-b)\|
       \le Ce^{-cN}\|Yb\|.
 \tag{18}
\]
Thus the full nonzero Gaussian in W persists. Explicitly put
\[
 \alpha=\frac{\pi\sin\pi w_*}{\sin\pi u_*\sin\pi v_*},\quad
 \beta=\frac{\pi\sin\pi v_*}{\sin\pi u_*\sin\pi w_*},\quad
 \chi=\pi\cot\pi u_*,\quad\sigma=\alpha+4/\delta,
\]
\[
 \Gamma=\beta-(\chi+i\pi)^2/\sigma,\qquad
 \mathcal A=(\pi\delta)^{-1/4}\sqrt{2\alpha/\sigma},
 \quad z_c=(c-c_*)/\sqrt N.
\]
For bounded \(z_c\), (18) has exponentially small error even
relative to an individual \(N^{-1/4}e^{NS_*}\) central entry.
W's formula therefore gives
\[
 (D_{\rm out}Xv^{\rm band})_c
 =\kappa(-1)^c q^{-(T+1)c}e^{i\pi(c-c_*)\eta_*}
 N^{-1/4}e^{NS_*}\mathcal A e^{-\Gamma z_c^2/2}
                            (1+O_R(N^{-1/2})),
 \tag{19}
\]
where \(\operatorname{Re}\Gamma>0\). Also
\[
 \|D_{\rm out}Xv^{\rm band}\|
 =|\kappa|e^{NS_*}\mathcal A
          (\pi/\operatorname{Re}\Gamma)^{1/4}(1+o(1)).
 \tag{20}
\]
The whole output tail estimate follows from W's Gaussian bound
and (18); in particular macroscopic occupation tails are
exponentially small relative to (20). No cap is omitted in (18).

Let \(W_{\rm in},W_{\rm out}\) be W's original annular coherent
partial resolutions, with fixed margins around \(\eta_*\) and
\(\xi_*\). Their actual diagonal entries are differences of
\[
 (W_p)_{a,a}=\sum_{j=a+1}^{N}\binom Njp^j(1-p)^{N-j},
 \qquad0\le a\le T.
 \tag{21}
\]
They are contractions and commute with both diagonal frames.
W proves the two currents on \(b\). The operator norms of
\(W_{\rm out}Y-YW_{\rm in}\) and
\(W_{\rm out}YW_{\rm in}-Y\) are at most \(2\|Y\|\).
Apply them to \(b^{\rm band}-b\), and use (17),(18), to get
\[
 \boxed{\quad
 \begin{split}
 &\|D_{\rm out}(W_{\rm out}X-XW_{\rm in})v^{\rm band}\|\\
 &\quad+\|D_{\rm out}(W_{\rm out}XW_{\rm in}-X)v^{\rm band}\|
       \le Ce^{-cN}\|D_{\rm out}Xv^{\rm band}\|.
 \end{split}\quad}                                           \tag{22}
\]
The incoming and outgoing omitted-window vectors separately
have the same exponential estimate in their respective frames.
This follows by applying their contractions to (17),(18).
Equation (22) concerns this exact band state. It does not say
that either annulus maps the entire band into itself.

## 5. Closing rows and meridian scope

An arbitrary specified physical closing row \(\ell_N\) retains
the exact absolute-error consequence
\[
 |\ell_NXv^{\rm band}-\ell_NXD_{\rm in}b|
 \le Ce^{-cN}\|\ell_ND_{\rm out}^{-1}\|\,\|Yb\|.
 \tag{23}
\]
The same bound holds for the two window currents, with (20)
in place of \(\|Yb\|\). The row and its output-frame norm
remain part of the source. No relative scalar statement is
inferred if that row kills the transported packet or has
uncontrolled exponential norm. Similarly, internal frame
matching and the common-degree scalar in W's two-wire frame
formula remain necessary when this brick is placed in a word.

All conclusions are at the root \(M=1\). Neither (13) nor its
norm estimate supplies a holomorphic preimage under a Gauss
factor, a bound for its first meridian normal, or a bound for
an adapted rank-one conjugation through that factor. Those
questions retain the actual two-step image lattice and its
moving normal data. The present result proves the local
overlap without taking such an inverse.

The reusable step is an exact vector in the original complementary
range, exponentially close in an explicitly controlled source frame
to a packet attaining the entire opened-generator norm exponent.
Both original annular currents are then controlled. There is no
claim of a geometric cycle, arbitrary real-carrier closure, or
noncancellation of the original pointed/pivotal invariant.

## Complete proof directs

* W: notes/research_weighted_reduced_generator_window_transport.md,
  SHA256 800cd02115245208e2f37e688590ad00b0a44b6a274d973cf8c12dd8df6cc2be.
* F: notes/research_dual_gauss_fourier_band_and_square.md,
  SHA256 3abc3ae81367e72bd56045292261c7eea1fb22ceeed379ad4cd64013f4148038.

The entire matching W was freshly read nontruncated in this author
sequence. The complete matching F was freshly whole-read in the
immediately preceding active author/formal sequence and is retained
unchanged. Every used implication was checked. Only written
mathematics and text/hash operations were used; frozen and public
files were not changed.
