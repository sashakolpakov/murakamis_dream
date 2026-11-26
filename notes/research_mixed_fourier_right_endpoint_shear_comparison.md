# The right endpoint of the coupled contour displacement

Research deduction, 7 November 2026. At the right outgoing endpoint,
the exact period identities express the upper retained contour as
two contours at the left endpoint. The first retains its Fourier
kernel. The second has no retained Fourier kernel and can be moved
to the original negative critical height. Both have controlled
initial rates. Along the subsequent coupled displacement their
rates can increase by less than \(1/80\), which is smaller than
the already proved endpoint reserve.

The finite-height bound below includes both terms and every
original scalar. Passing to infinite height uses the separate
uniform factorial-tail estimate, not a fixed-level limit.

## 1. The exact period identity on the complete retained path

Use the original row \(T_N(s,q)\), cardinal \(\widehat f_N\),
and incoming halfweight from
[the joint chart](research_mixed_fourier_right_cap_joint_global_chart.md).
Let
\[
 \alpha_N=-1/(2N),\quad\beta_N=\alpha_N+1,\qquad
 -.102\le h_q\le-.001,\qquad
 q_L(t)=\alpha_N+i(h_q-t),\quad q_R(t)=q_L(t)+1.
 \tag{1}
\]
Here \(t\ge0\) is the displacement parameter. Define
\[
 Z_q=e^{-2\pi iNq_L(t)},\quad
 R_q=\frac{Y^N}{1-Y^NZ_q},\quad
 A_q=\frac{Z_q}{1-Z_q},\quad
 k_N^+(s)=\frac{e^{2\pi iNs}}{1-e^{2\pi iNs}}.
 \tag{2}
\]
Every denominator in (2) involving \(q\) is nonzero:
\(|Z_q|=e^{2\pi N(h_q-t)}<1\) and \(|Y|<1\).
The factorial and cardinal period relations give the exact identity
\[
 T_N(s,q_R)=R_qT_N(s,q_L)
        \frac{1-e^{-2\pi iNs}Z_q}{1-Z_q}.
 \tag{3}
\]
Since \(e^{-2\pi iNs}k_N^+(s)=1+k_N^+(s)\), this becomes
\[
 \boxed{\quad
 k_N^+(s)T_N(s,q_R)
     =R_q\{k_N^+(s)T_N(s,q_L)-A_qT_N(s,q_L)\}.
 \quad}
 \tag{4}
\]
Equation (4) uses the same cardinal interpolation at both
endpoints. In particular its factor \(Y^N\) is retained.

Let \(\Gamma(b)\) be the oriented path
\[
 \sigma_-\longrightarrow\sigma_-+ib
       \longrightarrow\sigma_++ib\longrightarrow\sigma_+,
                    \qquad b>0.
 \tag{5}
\]
It represents the upper horizontal retained term together with
its two positive-height sides. The cuts \(\sigma_\pm\) are
the original half-grid cuts. Choose \(0<b<-h_q\).
At each fixed \(t\), the first path integral on the right of
(4) may be taken over \(\Gamma(5/4)+it\) instead of
\(\Gamma(b)+it\). The paths have identical endpoints and
their difference encloses no pole of \(k_N^+T_N\): the only
kernel poles lie on the physical real retained nodes, below
the intervening region. At \(t=0\) the vertical sides meet
the real axis only at the half-grid cuts.

The second term in (4) has no retained kernel. Its path may
therefore be replaced by \(\Lambda(h_s)+it\), where
\[
 \Lambda(h_s):\quad
 \sigma_-\longrightarrow\sigma_-+ih_s
      \longrightarrow\sigma_++ih_s\longrightarrow\sigma_+,
                \qquad -.102\le h_s\le-.001.
 \tag{6}
\]
This deformation is legitimate because \(T_N(s,q_L)\) is
holomorphic throughout the intervening strip. In particular
\(\Re(s+q_L)\) remains strictly between zero and one for
large \(N\). The poles of the shifted interpolation do not
occur in (4)--(6).

Writing path integrals with their usual complex differentials,
the exact outgoing right face is consequently
\[
 \begin{split}
 Q_{R,N}(T)&:=N^2\int_0^T
       \int_{\Gamma(b)+it}k_N^+(s)T_N(s,q_R(t))\,ds\,dt\\
 &=N^2\int_0^T R_q\left\{
       \int_{\Gamma(5/4)+it}k_N^+(s)T_N(s,q_L(t))\,ds
       -A_q\int_{\Lambda(h_s)+it}T_N(s,q_L(t))\,ds
                          \right\}\,dt .
 \end{split}
 \tag{7}
\]
The orientation factor multiplying this face in Stokes' theorem
does not change its modulus. The factors \(N^2\), the cardinal
normalization within \(T_N\), and the incoming weight are not
changed by (7).

## 2. A bound for the possible increase along the left endpoint

It suffices first to work at limiting outgoing real coordinate
zero. Keep the original incoming parameter \(a\) and output
\(Y=\rho e^{i\phi}\), with \(\rho<5/8\), \(\phi<7/6\).
For a fixed point \(s_0=u+iv_0\) on either path, put
\[
 s(t)=u+i(v_0+t),\qquad q(t)=i(h_q-t),\qquad
 1/8\le u\le1/2,\quad -.102\le v_0\le5/4.
 \tag{8}
\]
Use the original phase
\[
 F_\eta=g(s+a)+g(s+q)-3g(s)
             -(1+\eta/2)g(a)-g_-(q)+2\pi ias+\ell_q(y).
 \tag{9}
\]
Here the shared argument \(s+q=u+i(v_0+h_q)\) is fixed
and belongs to the original regular real strip. Define
\[
 W(t)=\Re F_\eta(s(t),a,q(t))-2\pi(v_0+t).
 \tag{10}
\]

**Lemma 1.** For every \(t\ge0\),
\[
                         W(t)<W(0)+1/80.
 \tag{11}
\]
The same bound holds if the constant \(-2\pi v_0\) in
(10) is replaced by any other constant.

*Proof.* Write \(H=v_0+t\), \(r=e^{-2\pi H}\),
and \(R=e^{2\pi(h_q-t)}\). The exact argument calculation
in the
[original upper-shear theorem](research_mixed_fourier_original_upper_shear.md)
now gives
\[
 -W'(t)=P
   =4\pi u-\phi+3A_r(u)-A_{r e^{-2\pi h_a}}(u+x)
                                   +A_{\rho R}(-\xi).
 \tag{12}
\]
The outgoing argument \(A_R(0)\) is zero because \(R<1\).
The last argument is the disk determination, equivalently
at real coordinate \(1-\xi\).

If \(H\ge0\), equations (8)--(10) of that theorem imply
\[
 4\pi u+3A_r(u)-A_{r e^{-2\pi h_a}}(u+x)
                 \ge\pi/2+3b(r)-\arctan\frac{5r}{3(1+r)}
                 \ge\pi/2.
 \tag{13}
\]
Indeed
\[
 b'(r)=\frac{\sqrt2}{2-2\sqrt2r+2r^2}
                         \ge1/\sqrt2>7/10\quad(0\le r\le1),
\]
so \(3b(r)\ge21r/10>5r/3\ge\arctan(5r/[3(1+r)])\)
when \(r>0\). Also
\(A_{\rho R}(-\xi)>-7R/10\ge-(7/10)e^{-2\pi t}\).
The elementary bounds \(\pi>157/50\), \(\phi<7/6\)
give \(\pi/2-\phi>2/5\). Thus
\[
                   P>2/5-(7/10)e^{-2\pi t}
                           \qquad(H\ge0).
 \tag{14}
\]

If \(H<0\), then \(r>1\). Monotonicity in radius gives
\(A_r(u)\ge A_1(u)=\pi/2-\pi u\), so
\(4\pi u+3A_r(u)\ge13\pi/8\).
The incident argument is nonpositive when \(u+x\ge1/2\).
Otherwise its bound at any radius is
\(\pi(1-2u-2x)\le31\pi/100\).
Consequently
\[
                P>263\pi/200-28/15>2.
 \tag{15}
\]
Equations (14)--(15) imply, on the entire motion,
\[
 W'(t)\le\bigl((7/10)e^{-2\pi t}-2/5\bigr)_+ .
 \tag{16}
\]
Its integral on \([0,\infty)\) is
\[
 \frac1{2\pi}\left\{\frac3{10}
                         -\frac25\log\frac74\right\}<\frac1{80}.
 \tag{17}
\]
This last comparison has a rational verification:
\[
 \log(7/4)=2\operatorname{arctanh}(3/11)
       >6/11+18/1331=744/1331>5/9.
\]
The braces in (17) are therefore less than \(7/90\),
and \(\pi>28/9\) gives (17). Integrating (16) proves
(11). \(\square\)

## 3. Initial data from the real seam

Let \(B_\eta(x)\) be the original supporting plane. The
[completed real-seam proof](research_mixed_fourier_real_seam_contour.md),
whose premise is discharged by the left-taper theorem, bounds
every point of \(\Lambda(h_s)\) by its seam phase
\(\Psi_\eta\le B_\eta-3/400\). It bounds every point of
\(\Gamma(5/4)\), with its upper Fourier debit, by
\[
                  \Re\Psi_\eta(s,a)-2\pi\Im s
                                      \le B_\eta-3/400.
 \tag{18}
\]
These are pointwise contour estimates, including the vertical
sides; no bound on individual central physical summands is
being inferred from a canceled sum.

At \(t=0\), replacing the left real seam by the left height
\(h_q\) and retaining the right cardinal factor \(Y^N\)
changes either profile by less than \(-1/50\). This is
exactly the all-retained-height comparison (24) in
[the outgoing vertical-current proof](research_mixed_fourier_right_cap_vertical_current_completion.md):
\[
 \Re F_\eta(s,a,ih_q)-2\pi\upsilon
      <\Re\Psi_\eta(s,a)
               +(\pi+\phi)|h_q|-2\pi\upsilon
      <\Re\Psi_\eta(s,a)-1/50.
 \tag{19}
\]
It applies at all the starting heights on (5)--(6).

For the first term of (7), combine (18)--(19) with Lemma 1,
keeping the retained Fourier debit. For the second term,
the outgoing factor \(A_q\) has rate \(2\pi(h_q-t)\).
Its variation in \(t\) is the same \(-2\pi t\) as in
Lemma 1, while its additional initial term \(2\pi h_q\)
is negative. Thus both full integrands have rate at most
\[
 B_\eta-3/400-1/50+1/80
                            =B_\eta-3/200.
 \tag{20}
\]
No large multiplier on the original upper path is discarded:
the unpenalized term was moved to (6) before applying (19).

## 4. The finite-height consequence and the infinite-end obligation

Fix \(T<\infty\). On \(0\le t\le T\), all factorials
on the replaced paths lie in fixed regular strips or fixed
compact subsets of the lower half-plane. The replacement
of the limiting outgoing real coordinate zero by
\(\alpha_N\), and of the limiting retained cuts by
\(\sigma_\pm\), changes their rates by \(O(1/N)\).
The shared argument stays away from its real endpoints.

On the positive vertical sides, the exact kernel satisfies
\(|k_N^+(\sigma_\pm+iH)|\le e^{-2\pi NH}\).
On the upper horizontal part it has the same bound up to
\((1-e^{-2\pi N(5/4)})^{-1}\). Also
\[
 |R_q|\le\frac{\rho^N}{1-\rho^N},\qquad
 |A_q|\le\frac{e^{2\pi N(h_q-t)}}{1-e^{2\pi Nh_q}}.
 \tag{21}
\]
Their denominators are uniformly bounded for sufficiently
large \(N\), using \(-h_q\ge.001\).
The original incoming weight uses its unchanged arbitrary
rate-tolerance upper bound. It is never divided out.

Therefore, after allocating one fixed tolerance and absorbing
the polynomial prefactors, both replaced path integrals in
(7), integrated in absolute value over \(0\le t\le T\),
have the common finite gap \(1/200\) for all sufficiently
large \(N\) of either parity. In particular
\[
 |d_N(X)|^{\eta/2}|Q_{R,N}(T)|
                          \le e^{N(B_\eta(x)-1/200)}.
 \tag{22}
\]
Here the threshold may depend on the fixed \(T\).

For the infinite end, the uniform factorial-tail estimate
must be applied with the actual offsets \(s=s_0+it\),
\(q=q_L(0)-it\), including positive starting heights on
\(\Gamma(5/4)\). In the second term of (7),
\[
 Z_qT_N(s,q)=e^{-2\pi iN(s+q)}
                         e^{2\pi iNs}T_N(s,q),
 \tag{23}
\]
and the first factor is constant along the displacement.
It stays in every comparison to a fixed-height value.
Equations (21) retain the other two denominators.
Thus an offset version of the uniform tail lemma, compared
to (20) at one sufficiently large fixed height, extends
(22) to \(T=\infty\). This final use requires that lemma
with those offsets; compact estimates or fixed-level
convergence alone are not substituted for it here.

## 5. The uniform tail estimate completes the endpoint bound

The required estimate is now Lemma 3 of
[the uniform shear-connector proof](research_mixed_fourier_retained_side_shear_connectors.md).
It applies to all the offsets on (5)--(6), including
\(q_L\) with real part \(\alpha_N\). With
\(A_N^{\mathrm{off}}(t)=e^{2\pi iNs(t)}T_N(s(t),q_L(t))\),
it states
\[
 |A_N^{\mathrm{off}}(t)|\le |A_N^{\mathrm{off}}(T_1)|
  e^{12N\psi_{\mathrm{off}}(T_1)-\Lambda_N(u)(t-T_1)},
 \qquad t\ge T_1\ge1,
 \tag{24}
\]
where \(\psi_{\mathrm{off}}(T_1)\to0\) independently of
the level and \(\Lambda_N(u)>\pi N/10\).
The factor in (23) is independent of \(t\), so the same
comparison applies to the numerator of the second term.
Every remaining denominator in (2), (17), and (21) is
bounded uniformly on the tail. Its ratio to the corresponding
fixed-height denominator is also uniformly bounded.
There is consequently no loss of exponential rate from
these ratios. The factor \(\rho^N\) remains in the
calibrated value at \(T_1\).

Choose one fixed \(T_1\) with
\(12\psi_{\mathrm{off}}(T_1)<1/1000\). On
\([0,T_1]\) use (20) with a finite-source tolerance less
than \(1/1000\); use the same bound at \(T_1\) in
(24) for the infinite end. The latter integration costs
at most a constant times \(1/\Lambda_N(u)\).
The raw gap \(3/200\) absorbs both tolerances, all fixed
path lengths and polynomial factors, the outside \(N^2\),
and the sum of the two terms of (7).

**Theorem 2.** The original right outgoing face is absolutely
convergent at each fixed level. Uniformly on the original
actual family, for all sufficiently large \(N\) of either
parity,
\[
 \boxed{\quad
 |d_N(X)|^{\eta/2}N^2\int_0^\infty
  \left|\int_{\Gamma(b)+it}
           k_N^+(s)T_N(s,q_R(t))\,ds\right|dt
              \le e^{N(B_\eta(x)-1/200)}.
 \quad}
 \tag{25}
\]
The absolute bound is proved after the exact replacements
in (7). It does not assert that the original high-height
right profiles are individually small. Equation (25)
bounds the actual outgoing face in the coupled transport,
not the different vertical return on the outgoing main
contour.
