# Weighted transport and actual coherent windows for the opened generator

Private written proof, 19 November 2026.

Every protected interior point of the physical opened-generator triangle
can be made its unique global modulus maximum by explicit input and
output diagonal frames. A phased occupation packet then has a nonzero
Gaussian image and achieves the full weighted operator-norm exponent.
Consequently two original annular coherent resolutions have an
exponentially small transport current on this packet, relative to its
actual image. No partial inverse or spectral projector is used.

The packet is an ordinary physical occupation packet. Membership in the
complementary Gauss Fourier band is not asserted. The diagonal frames
are retained, and their compatibility at shared ports of a word remains
a separate condition. The sole complete direct is R, pinned below.

## 1. The literal finite matrix and its retained phase

Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1},\quad f_n=(Q;Q)_n.
\]
Keep the root meridian \(M=1\). On the actual degree-\(T\) space
\[
 U_T=\operatorname{span}\{|a,T-a\rangle:0\le a\le T\},
 \qquad 0\le T\le d,
\]
R gives the positive opened generator, including its original scalar,
\[
 X=\mathcal B_3(R_1)=\kappa S_2D,\qquad
 S_2=\sum_{n=0}^{d}\frac{(x^{-1}L_1F_2)^n}{f_n},\qquad
 D_a=(-1)^a q^{a(a+1)}.                                      \tag{1}
\]
The shift \(L_1\) has zero vacuum arrow, and \(F_2\) has its actual
zero top arrow. A transfer from input \(a\) to output \(c\) requires
\(n=a-c\). Hence, with
\(\mathfrak s_n=\prod_{j=1}^n2\sin(\pi j/N)>0\),
\[
 X_{c,a}=
 \begin{cases}
 \displaystyle
 \kappa(-1)^c q^{(T+c+2)a-(T+1)c}
       \frac{\mathfrak s_{T-c}}
            {\mathfrak s_{a-c}\mathfrak s_{T-a}},
       &0\le c\le a\le T,\\
 0,&\text{otherwise}.
 \end{cases}                                                 \tag{2}
\]
Indeed the transfer coefficient before \(D_a\) is
\(x^{-(a-c)}f_{T-c}/(f_{a-c}f_{T-a})\). Substituting
\[
 f_n=(-i)^nq^{n(n+1)/2}\mathfrak s_n
\]
gives (2). In particular its remaining phase is bilinear in the two
occupations, not an unspecified oscillatory amplitude. All caps in
(2) are physical.

All operator and vector norms below are Euclidean norms in this
displayed occupation basis. The coherent-window matrices constructed
in Section 4 are diagonal positive contractions in this norm as well
as in the original binomial norm.

## 2. A global maximum at any protected interior point

Let
\[
 \tau=T/N,\qquad \xi=c/N,\qquad \eta=a/N,\qquad
 J(t)=\int_0^t\log(2\sin\pi s)\,ds.
\]
The modulus exponent of (2), apart from \(\kappa\), is
\[
 \begin{split}
 R_\tau(\xi,\eta)
 &=J(\tau-\xi)-J(\tau-\eta)-J(\eta-\xi)\\
 &=-J(u)-J(v)-J(w),\\
 u&=\eta-\xi,\qquad v=\tau-\eta,\qquad
 w=1-\tau+\xi,\qquad u+v+w=1.                              \tag{3}
 \end{split}
\]
Here \(J(1-t)=-J(t)\). Fix a compact subset of
\[
        0<\xi<\eta<\tau<1.                                \tag{4}
\]
For each sufficiently large \(N\), choose an actual integer output
\(c_*\), an integer \(a_0\), and \(L=\lfloor\delta_0N\rfloor\), where
\(\delta_0>0\) is fixed and sufficiently small, such that
\[
 \xi_*=\frac{c_*}{N},\qquad
 \eta_*=\frac{a_0+L/2}{N},\qquad \delta=L/N                  \tag{5}
\]
stay in that compact set together with \(\tau\), and
\([a_0,a_0+L]\subset[0,T]\). Taking \(\delta_0\) smaller than a fixed
interior buffer permits rounding any prescribed points in (4) this
way, enlarging the compact subset within (4) if necessary.
Every formula uses the exact parameters (5), including a possible
half-integer input center and the exact \(T\le N-1\).

Evaluate \(u_*,v_*,w_*\) by (3), and put
\[
 \lambda=\log\frac{\sin\pi u_*}{\sin\pi v_*},\qquad
 \mu=\log\frac{\sin\pi w_*}{\sin\pi u_*},\qquad
 Y=D_{\rm out}XD_{\rm in},                                \tag{6}
\]
\[
 (D_{\rm in})_{a,a}=e^{\lambda a},\qquad
 (D_{\rm out})_{c,c}=e^{\mu c}.
\]
These are actual positive diagonal source frames, not scalar
renormalizations. The weighted exponent is
\[
 S(\xi,\eta)=R_\tau(\xi,\eta)+\lambda\eta+\mu\xi,\qquad
 S_*=S(\xi_*,\eta_*).                                     \tag{7}
\]
It has its unique global maximum on
\(\{0\le\xi\le\eta\le\tau\}\) at \((\xi_*,\eta_*)\).

Here are the global details. In the open triangle,
\[
 R_\eta=\log\frac{\sin\pi v}{\sin\pi u},\qquad
 R_\xi=\log\frac{\sin\pi u}{\sin\pi w}.
\]
Write
\[
 \alpha=\pi(\cot\pi u+\cot\pi v)
             =\frac{\pi\sin\pi w}{\sin\pi u\sin\pi v}>0,
 \quad
 \beta=\frac{\pi\sin\pi v}{\sin\pi u\sin\pi w}>0,\quad
 \chi=\pi\cot\pi u .
\]
Then
\[
 \operatorname{Hess}_{(\xi,\eta)}R_\tau
       =\begin{pmatrix}-\beta&\chi\\\chi&-\alpha\end{pmatrix},
       \qquad \alpha\beta-\chi^2=\pi^2.                 \tag{8}
\]
The last identity follows by expanding
\(\sin\pi(u+v)=\sin\pi w\), or the cotangent addition formula.
Thus the exponent is strictly concave. The chosen weights cancel
its gradient at the designated point. Continuity on the closed
triangle, integration along segments from that point, and (8) prove
the unique global maximum, including the edges. Uniformly over the
compact parameters,
\[
 S_*-S(\xi,\eta)\ge c\bigl((\xi-\xi_*)^2+
                                  (\eta-\eta_*)^2\bigr). \tag{9}
\]
For (9), use (8) on a common small neighborhood, and the strict
maximum and compactness on its complement. No assertion about an
uncontrolled continuation outside the physical triangle is used.

There is an entire-matrix bound with the correct power of \(N\):
\[
 |Y_{c,a}|
 \le C|\kappa|N^{-1/2}e^{NS_*}
       \exp\!\left[-c\frac{(c-N\xi_*)^2+
                              (a-N\eta_*)^2}{N}\right]. \tag{10}
\]
To prove it, uniformly for all \(0\le n<N\),
\[
 \log\mathfrak s_n=NJ(n/N)+O(\log N).                    \tag{11}
\]
Factor \(\log(2\sin\pi t)\) as
\(\log t+\log(1-t)+\log(2\sin\pi t/[t(1-t)])\).
The last term is smooth on the closed interval, with its removable
endpoint values. Its Riemann-sum error is bounded. Integral
comparison for the two monotone logarithms gives \(O(\log N)\),
including \(n=0,d\). This proves (11).
On a protected bulk interval the same factorization, Stirling's
formula and the trapezoidal remainder give the sharper estimate
\[
 \mathfrak s_n
   =\sqrt{2N\sin(\pi n/N)}\,e^{NJ(n/N)}(1+O(N^{-1})).
                                                               \tag{12}
\]
For indices in a common neighborhood of the maximum, (12) gives
(10) directly with the \(N^{-1/2}\) prefactor. Outside that
neighborhood, (11) and (9) give a fixed exponential loss; reducing
the constant in (10) absorbs its polynomial factor and \(N^{1/2}\).
This proves (10) on the whole capped matrix.
Summing its rows and columns and using the elementary Schur bound
now gives
\[
                   \|Y\|_2\le C|\kappa|e^{NS_*}.          \tag{13}
\]
For completeness that bound follows from
\(\|Yv\|_2^2\le
(\sup_c\sum_a|Y_{c,a}|)(\sup_a\sum_c|Y_{c,a}|)\|v\|_2^2\).
The Gaussian sums in (10) are \(O(\sqrt N)\).

## 3. A packet attaining this exponent

Define the physical unit vector supported in the indicated interval by
\[
 b_{a_0+j}
   =\frac{2^{-L}\binom Lj}{\nu_L}\,
                q^{-(T+c_*+2)(a_0+j)},\qquad 0\le j\le L,
 \quad
 \nu_L^2=4^{-L}\binom{2L}{L}.                             \tag{14}
\]
The identity \(\sum_j\binom Lj^2=\binom{2L}{L}\) proves its norm
is exactly one. This packet uses occupation coefficients, not
the Fourier coefficients of a complementary Gauss image.
The chosen carrier cancels the full input phase of (2) at \(c_*\).
Set \(w=Yb\) and \(z_c=(c-c_*)/\sqrt N\).

In the following formulas \(\alpha,\beta,\chi\) are (8) at the
designated point. Put
\[
 \sigma=\alpha+4/\delta,\qquad
 \Gamma=\beta-\frac{(\chi+i\pi)^2}{\sigma},\qquad
 \mathcal A=(\pi\delta)^{-1/4}\sqrt{\frac{2\alpha}{\sigma}}.
                                                               \tag{15}
\]
These are uniform analytic coefficients on a small complex
neighborhood of the protected real parameters, with their
positive real square-root conventions. In particular
\[
 \operatorname{Re}\Gamma
   =\frac{4\beta/\delta+2\pi^2}{\sigma}>0.                \tag{16}
\]
Uniformly for the actual rows \(|z_c|\le R\), for any fixed \(R\),
\[
 \boxed{\quad
 w_c=\kappa(-1)^c q^{-(T+1)c}
       e^{i\pi(c-c_*)\eta_*}
       N^{-1/4}e^{NS_*}\mathcal A
       e^{-\Gamma z_c^2/2}
                  (1+O_R(N^{-1/2})).
 \quad}                                                       \tag{17}
\]
In particular the coefficient is nonzero.

We spell out the Gaussian normalization. The exact sum for \(w_c\),
after its displayed row phase, has the positive factors in (2),
the diagonal weights (6), and the remaining phase
\(q^{(c-c_*)a}\). Its real exponent is
\[
 S(\xi,\eta)+\delta[h(p)-\log2],\qquad
 p=(a-a_0)/L,\quad h(p)=-p\log p-(1-p)\log(1-p).
                                                               \tag{18}
\]
Its unique maximum is the same point, at \(p=1/2\). Its Hessian
is the matrix in (8) with the last diagonal replaced by \(-\sigma\).
On writing \(a_{\rm ind}=N\eta_*+y\sqrt N\), the remaining phase,
after the one displayed in (17), is exactly \(e^{i\pi z_cy}\).
The matrix prefactor from (12) at the saddle is
\[
 N^{-1/2}\sqrt{\frac{\sin\pi w_*}
                         {2\sin\pi u_*\sin\pi v_*}}
       =N^{-1/2}\sqrt{\alpha/(2\pi)}.
 \]
The packet prefactor from Stirling's formula and
\(\nu_L=(\pi L)^{-1/4}(1+O(N^{-1}))\) is
\(N^{-1/4}\sqrt2(\pi\delta)^{-1/4}\).
The sum has spacing \(N^{-1/2}\) in \(y\), and its Gaussian integral is
\[
 \int_{\mathbb R}e^{-\sigma y^2/2+(\chi+i\pi)z_cy-\beta z_c^2/2}\,dy
       =\sqrt{2\pi/\sigma}\,e^{-\Gamma z_c^2/2}.          \tag{19}
\]
Combining these factors gives precisely (17).
Taylor's cubic remainder on a growing central range, followed by
Gaussian tail bounds, gives \(O_R(N^{-1/2})\). The sum-to-integral
error has that order by integrating the absolute derivative of the
Gaussian summand. The limiting integral is uniformly nonzero on
bounded \(z_c\), so the error is relative.

The full caps obey, as well,
\[
 |b_a|\le CN^{-1/4}e^{-c(a-N\eta_*)^2/N},\qquad
 |w_c|\le C|\kappa|N^{-1/4}e^{NS_*}
                                  e^{-c(c-c_*)^2/N}.    \tag{20}
\]
For the first inequality use Stirling on a central binomial interval
and \(h(p)<\log2\) on its complement, retaining both endpoints.
For the second, multiply this bound by (10) and sum over \(a\).
Thus (17), dominated by (20) on the whole physical interval, proves
\[
 \boxed{\quad
 \|Yb\|_2=|\kappa|e^{NS_*}\mathcal A
            \left(\frac{\pi}{\operatorname{Re}\Gamma}\right)^{1/4}
            (1+o(1)),\qquad
       c|\kappa|e^{NS_*}\le\|Yb\|_2\le\|Y\|_2
                              \le C|\kappa|e^{NS_*}.
 \quad}                                                       \tag{21}
\]
The norm limit follows by first summing on \(|z_c|\le R\), then
using (20) as \(R\) increases. No claim about a far oscillatory
sum is needed. The constants are uniform on the protected compacts.

## 4. The original annular partial resolutions and their current

Use the actual one-head compact coherent resolution with \(d=N-1\).
Its radial coordinate is \(p=|z|^2/(1+|z|^2)\). The cap
\(0\le p\le p_0\) has the literal diagonal partial-resolution matrix
\[
 (W_{p_0})_{a,a}
 =N\binom da\int_0^{p_0}t^a(1-t)^{d-a}\,dt
 =\sum_{j=a+1}^{N}\binom Njp_0^j(1-p_0)^{N-j}.           \tag{22}
\]
The angular integral eliminates the off-diagonal entries. The
second equality follows by differentiating the finite binomial
tail and checking the value at zero. At \(p_0=1\) the matrix is
the identity. Consequently an annulus has
\[
 W_{[p_-,p_+]}=W_{p_+}-W_{p_-},\qquad 0\le W\le I.       \tag{23}
\]
On two heads take this annulus in the first head and the full
compact resolution in the second, then restrict to \(U_T\).
This gives exactly the same diagonal entries (22), with no
change of the second-head cap or of total degree.

Choose incoming and outgoing annuli whose radial intervals contain
\(\eta_*\) and \(\xi_*\), respectively, with fixed positive margins.
All four endpoints stay strictly between zero and one. Denote their
matrices by \(W_{\rm in},W_{\rm out}\). Equations (22),(20) imply
\[
 \|(I-W_{\rm in})b\|_2\le Ce^{-cN},\qquad
 \|(I-W_{\rm out})Yb\|_2\le Ce^{-cN}\|Yb\|_2.             \tag{24}
\]
Indeed, on a smaller fixed occupation interval around each center,
the two omitted binomial probabilities in (22) have a fixed
proportional deviation from their means, hence are \(O(e^{-cN})\).
One elementary bound follows from the fact that the second
derivative of \(\log(1-p+pe^t)\) is at most \(1/4\) for real
\(t\): center, integrate twice, and optimize the exponential Markov
bound. On the complementary occupation interval (20) gives the
required exponential tail. This proves both assertions in (24)
on the entire actual caps.

The norm matching in (21) now pays the current, including its
incoming term:
\[
 \boxed{\quad
 \|(W_{\rm out}Y-YW_{\rm in})b\|_2
       +\|W_{\rm out}YW_{\rm in}b-Yb\|_2
                 \le Ce^{-cN}\|Yb\|_2.
 \quad}                                                       \tag{25}
\]
For example the first difference is bounded by
\(\|(W_{\rm out}-I)Yb\|+\|Y\|\|(I-W_{\rm in})b\|\).
The second has the same bound because \(W_{\rm out}\) is a
contraction. Equations (21),(24) give (25).
In particular no exponential operator-norm loss is hidden when
an incoming window is inserted.

Both frames in (6) commute with these exact diagonal windows.
Thus (25) is equivalently the bound
\[
 \frac{\|D_{\rm out}(W_{\rm out}X-XW_{\rm in})
                         D_{\rm in}b\|_2}
      {\|D_{\rm out}XD_{\rm in}b\|_2}
                      \le Ce^{-cN}.                     \tag{26}
\]
This retains the actual \(X\), \(\kappa\), and the physical input
\(D_{\rm in}b\). It is a weighted norm assertion; the frames have
not been dropped when returning to physical coordinates.

## 5. What this proves for a source template

The triangle strict concavity used here is established coverage.
The additional assertion is its realization by the literal
opened-generator matrix, a nonzero packet with the full weighted
norm exponent, and the two original partial resolutions in (25).
The assertion is uniform at every protected interior triangle point,
not a list of degree or knot examples.

For a product of actual operators, compatible frames have the form
\(Y_i=D_{i+1}^{-1}X_iD_i\). Their internal diagonal factors cancel
exactly, including in a trace if the ending frame matches the
starting frame and the original pivot is retained. In the local
convention (6), this requires the outgoing weight of one brick
to be the negative of the incoming weight of its neighbor on
the same occupation. This note does not assert that those
conditions follow from a proposed geometric configuration.
For full two-wire frames, with input exponents \(q_1,q_2\) and
output exponents \(q'_1,q'_2\), the literal matrix factor is
\[
 e^{q_1a+q_2(T-a)-q'_1c-q'_2(T-c)}
   =e^{(q_2-q'_2)T}e^{\lambda a+\mu c},\qquad
 \lambda=q_1-q_2,\quad \mu=q'_2-q'_1.                    \tag{27}
\]
The common-degree scalar \(e^{(q_2-q'_2)T}\) must also remain.
If an additional actual routing condition identifies
\(q_1=q'_1\), then \(q_2-q'_2=-(\lambda+\mu)\).
Without that condition (27), rather than that specialization,
is the retained scalar. In particular it may not be discarded
when total degree is subsequently summed or continued.
Nor does (17) assert that the outgoing Gaussian is the required
incoming packet of the next factor. Those are actual shared-port
and carrier conditions, not consequences of separate local maxima.

The matrix (1) need not preserve a complementary Gauss primary
range, and (14) has not been put in that range. No orthogonal
Fourier projection is identified with a Casimir Riesz projection.
The theorem also gives no first-meridian normal, no partial
Gauss inverse, and no bound for a closed source solely from
the nonzero norm in (21).

When this brick occurs in the fused original source, the full
turnover/half-twist routing and all other partial resolutions
still have to be transported. The estimate (26) is a paid
local window-current estimate under explicit retained frames.
It is not a proof that a Rivin optimum belongs to these real
windows or that its original relative-cycle coefficient is nonzero.

## Complete proof direct and protocol

R: notes/research_actual_reduced_braid_source.md, 330 lines,
SHA256
9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.

Only written mathematics and text/hash operations are used.
Frozen and public files are unchanged. The entire matching final
and the sole complete R direct were freshly read nontruncated
in this author sequence. Every used implication was checked and
both pins renewed. Independent matching review and root adoption
remain separate.
