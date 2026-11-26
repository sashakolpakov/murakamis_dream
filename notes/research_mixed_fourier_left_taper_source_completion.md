# The complete low retained source on the left Fourier taper

Research completion, 7 November 2026. The proved left-taper
derivative signs control the entire truncated conditional source,
including its physical low rows, both retained horizontal aliases
and every retained join. They also give a fixed outgoing vertical
collar around the real endpoint. The original finite cardinal
coefficient, incoming allocation and both parity cuts are retained.

The remaining middle part of the outgoing vertical current is
not bounded here. In particular this is not yet a complete
Fourier right-cap asymptotic.

## 1. The proved derivative premise and original finite source

Use the references and notation of
[the real-seam contour theorem](research_mixed_fourier_real_seam_contour.md),
including
\[
 \begin{gathered}
 \eta\in\{0,1\},\quad a=x+i h_a,\quad x\in P=[11/50,9/20],\\
 h_s=\Im s_*,\quad h_q=\Im q_*,\quad
 -.102\le h_s,h_q\le-.001,\quad |h_a|\le.108,\\
 B_\eta(x)=M_\eta+p_\eta(x-\Re a_*)
                         -\kappa(x-\Re a_*)^2,\qquad
 \kappa=1/2500000.
 \end{gathered}
 \tag{1}
\]
The incoming height and halfweight are original. When \(\eta=1\)
the incoming height is negative and unselected.
Put \(c=11/50\), \(\lambda=-h_q/c\), and
\[
                  q(t)=t-i\lambda t,\qquad 0\le t\le c .
 \tag{2}
\]
The geometric output is the original \(y=x_0\),
\(Y=e^{2\pi iy}\).

The sole prescribed
[taper certificate](../repro/results/research-mixed-fourier-left-taper.json)
passed, with SHA-256
55a7c56f33f576c9e6b13b015fd69a448c269ccda82166682675e06d76bcc4c9.
It retains all \(512\times256\) closed cells and both outward
dyadic bounds on each cell. The minimum certified lower bound is
\[
              \frac{5917819973}{274877906944}>\frac1{50}.
 \tag{3}
\]
Its complete fixed analytic inventory and 29 before/after bindings
agree. It uses the full original \(Y\) enclosure; it does not
solve a root or evaluate a quantum source. The writer and protocol
are those in the
[fixed certificate protocol](research_mixed_fourier_left_taper_protocol.md).
The record and metadata were inspected after the sole run without
replaying its analytic operations.

Together with the already proved near-zero Lemma 2 in
[the derivative reduction](research_mixed_fourier_left_taper_reduction.md),
this discharges its two-function positivity premise. Therefore,
for \(1/8\le\Re s\le1/2\) and \(h_s\le\Im s\le0\),
\[
 \Re\mathscr F_\eta(s,a,q(t))
       \le \Re\mathscr F_\eta(s,a,c+i h_q).
 \tag{4}
\]
At \(t=0\) the stronger loss \(3/400\) from the first
hundredth is retained, as in the seam theorem.

Write \(M_N=\lceil N/2\rceil-1\), \(X=e^{-2\pi ia}\), and
\[
 \begin{split}
 C_N^<(X,Z)&=\sum_{j=0}^{M_N}
                       \frac{X^{-j}p_j(X)p_j(Z)}{P_j^3},\\
 S_N^<(q)&=C_N^<(X,e^{-2\pi iq})\widehat f_N(q;y).
 \end{split}
 \tag{5}
\]
The cardinal is the original global factorial-suffix
interpolation. It agrees with every physical cardinal value.
No off-grid equality with a different interpolation is asserted.

## 2. The full retained alias strip along the taper

The original allocated phase is
\[
 \mathscr F_\eta(s,a,q)=
 g(s+a)+g(s+q)-3g(s)-(1+\eta/2)g(a)-g(q)
                          +2\pi ias+\ell_q(y).
 \tag{6}
\]
All \(s\)-dependent arguments stay in their original regular
real strips. For every finite retained height \(v\), with
\(s=u+iv\), \(1/8\le u\le1/2\), and \(0\le t\le c\),
\[
 -\frac{181\pi}{100}
       <\Im\mathscr F_{\eta,s}(s,a,q(t))
       <\frac{33\pi}{20}.
 \tag{7}
\]
The phase is continuous at \(q=0\); only its \(s\) derivative
is used in (7).

Here is a direct check retaining the original logarithmic lifts.
The derivative is
\[
 g'(s+a)+g'(s+q)-3g'(s)+2\pi ia .
 \tag{8}
\]
For an argument with real part \(z_R\le1/2\), the imaginary
part of \(g'\) lies between \(0\) and \(\pi(1-2z_R)\)
at every height. For \(z_R\ge1/2\), it lies between
\(\pi(1-2z_R)\) and zero.
Since \(t\le x\), there are only three cases.
If \(u+x\le1/2\), both shifted real parts are below \(1/2\).
The lower bound is
\(-3\pi(1-2u)+2\pi x\ge-181\pi/100\);
the upper bound is \(\pi(2-4u-2t)\le3\pi/2\).
If \(u+t\le1/2\le u+x\), the lower bound is
\(-2\pi(1-2u)\ge-3\pi/2\), and the upper bound is
\(2\pi x+\pi(1-2u-2t)\le33\pi/20\).
If \(u+t\ge1/2\), both shifted real parts are above \(1/2\).
The lower bound is \(\pi(-1+2u-2t)\ge-4\pi t\ge-22\pi/25\);
the upper bound is \(2\pi x\le9\pi/10\).
These bounds prove (7).

Use the unchanged retained heights \(h_-=-1/5\), \(h_+=5/4\).
Integration of (7) gives, uniformly along the taper,
\[
 \begin{split}
 \Re\mathscr F_\eta(u+i h_-,a,q)-2\pi/5
    &<\Re\mathscr F_\eta(u+i h_s,a,q)-7\pi/100,\\
 \Re\mathscr F_\eta(u+i h_+,a,q)-5\pi/2
    &<\Re\mathscr F_\eta(u+i h_s,a,q)-661\pi/12500.
 \end{split}
 \tag{9}
\]
The upper remainder is
\(-19\pi/80-(181\pi/100)h_s
 \le-661\pi/12500\).
At either real retained cut, the paid vertical derivatives obey
\[
 \begin{split}
 \partial_v(\Re\mathscr F_\eta+2\pi v)&>7\pi/20
                                                     &&(v<0),\\
 \partial_v(\Re\mathscr F_\eta-2\pi v)&<-19\pi/100
                                                     &&(v>0).
 \end{split}
 \tag{10}
\]
Thus every penalized vertical piece is bounded by its own real
cut. No Fourier debit is assigned to an unpenalized join.

## 3. Paying the central sheet, cuts, joins and physical low rows

The original outgoing reference has \(\Re q_*\ge.24\).
Consequently the completed central sheet at \(q=c+i h_q\)
has the fixed loss
\[
 \delta_c=\kappa(.24-.22)^2=\frac{\kappa}{2500}>0:
 \qquad
 \Re\mathscr F_\eta(u+i h_s,a,c+i h_q)
                         \le B_\eta(x)-\delta_c .
 \tag{11}
\]
Transport (4) gives the same bound at every \(q(t)\).
Both original real retained cuts \(b=1/8,1/2\) satisfy
\[
 \Re\mathscr F_\eta(b,a,q(t))
          <B_\eta(x)-1/35000 .
 \tag{12}
\]
For the unpenalized joins \(h_s\le v\le0\), first use
(4) at each fixed \(v\), and then use the old vertical
convexity at \(q=c+i h_q\). Its endpoint losses are
\(1/35000\) and
\(\kappa(b-\Re s_*)^2\), respectively.
Since \(.24\le\Re s_*\le.36\), both losses exceed
\(\delta_c\). Therefore every such join is paid by
\(B_\eta-\delta_c\). Equations (9)--(10) now pay all
horizontal and vertical aliases too.

It remains to retain the physical rows below the lower cut.
For \(0<u\le1/8\), let \(\mathcal T_\eta(u;a,q(t))\)
be the literal real-row rate, including its chirp, cardinal
and incoming allocation. Its \(u\) derivative equals the
seam derivative plus
\[
 \log\frac{|1-e^{-2\pi\lambda t}e^{-2\pi i(u+t)}|}
                   {|1-e^{-2\pi iu}|}.
 \tag{13}
\]
This extra term is nonnegative. Indeed, put
\(\theta=2\pi(u+t)\), \(r_t=e^{-2\pi\lambda t}\).
The derivative in \(t\) of the squared numerator in (13)
has the sign of
\[
 \sin\theta+\lambda(\cos\theta-r_t)
       \ge\sin\theta-\lambda(1-\cos\theta)>0.
 \tag{14}
\]
Here \(0<\theta\le.69\pi\) and
\(\cot(\theta/2)>\cot(.35\pi)>1/2>\lambda\).
For the middle elementary inequality,
\(\sin(\pi/5)<3/5\) implies
\(\sin^2(3\pi/20)>1/5\), hence
\(\tan(3\pi/20)>1/2\).
At \(t=0\) the numerator in (13) is its denominator.

The seam theorem proves its physical derivative exceeds
\(\log(3/2)\) throughout this interval. Thus
\[
 \partial_u\mathcal T_\eta(u;a,q(t))>\log(3/2)>0,
                  \qquad 0<u\le1/8 .
 \tag{15}
\]
The continuous \(u=0\) rate is included. Every physical low
row is therefore bounded by the already paid lower cut (12).
There is no use of the coherently paid high-\(j\) group in
this physical-row argument.

## 4. Uniform finite control, including the factorial endpoint

Put \(L_N=\lceil N/8\rceil\) and use the exact half-grid cuts
\(\sigma_\pm\) of the seam theorem. For every fixed taper
point \(q\), use the literal central interpolation
\[
 F_N(s,q)=
 \widehat f_N(q;y)e^{2\pi iNas}
   \Pi_N(s+a)E_N(a)\Pi_N(s+q)E_N(q)E_N(s)^3,
 \qquad E_N=1/\Pi_N .
 \tag{16}
\]
At \(s=j/N\), this is exactly the \(j\)-th summand in (5).
The four retained groups are precisely
\[
 \begin{split}
 Z_N(q)&=N\int_{\sigma_-}^{\sigma_+}F_N(u+i h_s,q)\,du,\\
 L_N(q)&=N\int_{\sigma_-}^{\sigma_+}F_N(u+i h_-,q)
                  \frac{e^{-2\pi iN(u+i h_-)}}{1-e^{-2\pi iN(u+i h_-)}}\,du,\\
 U_N(q)&=N\int_{\sigma_-}^{\sigma_+}F_N(u+i h_+,q)
                  \frac{e^{2\pi iN(u+i h_+)}}{1-e^{2\pi iN(u+i h_+)}}\,du,\\
 V_N(q)&=iN\int_{h_-}^{h_+}w_{N,h_s}(v)
           [F_N(\sigma_++iv,q)-F_N(\sigma_-+iv,q)]\,dv .
 \end{split}
 \tag{17}
\]
The exact central physical sum is \(Z_N+L_N+U_N+V_N\).
The function \(w_{N,h_s}\), its signed subtraction, both
alias denominators and the \(+N\) zero mode are unchanged.
The \(1/N\) cardinal coefficient is already inside (16).

All \(s\)-dependent factorial arguments in (16) lie in
fixed regular real strips, uniformly along the whole taper.
The only endpoint factor needing separate treatment is
\(E_N(q)\) as \(q\to0\). Choose an integer \(m_N\) with
\(m_N/N\) close to \(1/4\), and use the exact identity
\[
 E_N(q)=
 \frac{\prod_{k=1}^{m_N}(1-e^{-2\pi i(q+k/N)})}
                           {\Pi_N(q+m_N/N)} .
 \tag{18}
\]
The denominator is in a fixed regular strip. The numerator
is a finite product with its original zeros. The uniform
truncated-logarithm/Riemann-sum upper bound, including the
endpoint \(q=0\), gives
\[
 |E_N(q)|\le C N^b e^{-N\Re g(q)}
                         \qquad(q=q(t),\ 0\le t\le c).
 \tag{19}
\]
Indeed its integrated logarithm is
\(\Re[g(q+m_N/N)-g(q)]\), and the denominator cancels
the first primitive. The logarithmic endpoint costs only
\(O(\log N)\). This is an upper bound on the literal product,
not a two-sided packet at \(q=0\).
The global cardinal has its uniform original phase
\(\ell_q(y)\) here: its shifted argument \(q-y\) stays
in a fixed negative-height compact set. Its finite scalar
and symbol are retained.

Equations (11)--(19), the original physical-product bounds,
and an aggregate source tolerance therefore prove the
following finite statement.

**Theorem 1.** There are \(N_0\) and uniform constants such
that, for every \(N\ge N_0\) of either parity,
\[
 \boxed{\quad
 |d_N(X)|^{\eta/2}\sup_{0\le t\le c}|S_N^<(q(t))|
                    \le e^{N(B_\eta(x)-\delta_c/2)} .
 \quad}
 \tag{20}
\]
For example choose the aggregate finite tolerance below
\(\delta_c/4\), and then absorb the polynomial factors.
Each of the four groups (17), as well as the physical low
tail, has the same upper rate before that absorption.
Consequently the outgoing zero-mode integral along this
fixed taper also has an exponential gap:
\[
 |d_N(X)|^{\eta/2}
   \left|N\int_{q([0,c])}S_N^<(q)\,dq\right|
                    \le e^{N(B_\eta(x)-\delta_c/4)}
 \tag{21}
\]
for all sufficiently large \(N\). Its exact \(+N\) and
the length factor of the prescribed contour have been
absorbed, not omitted.
The short segment from \(\alpha_N=-1/(2N)\) to zero is
already paid by the seam theorem with the larger finite
gap \(1/1000\). Thus (21) covers the actual left endpoint
of a bent outgoing main path.

## 5. A fixed vertical collar at that endpoint

There is also a uniform, unevaluated \(\delta>0\) for which
the part of the real-endpoint vertical current with
\(|v|\le\delta\) is exponentially small. This assertion
preserves the coherent central retained contour.

At the left half-grid endpoint the exact Gamma reflection
identity from
[lower-half factorial continuation](research_lower_half_factorial_continuation.md),
equation (6), says
\[
 |\Pi_N(\alpha_N+iv)|^2=\frac{N}{1+e^{2\pi Nv}},
 \qquad
 |E_N(\alpha_N+iv)|
       \le\sqrt{2/N}\,e^{\pi Nv_+}.
 \tag{22}
\]
This is uniform through \(v=0\); no singular Stirling
approximation is used there.

For \(q=\alpha_N+iv\), \(|v|\le\delta<\Im y/2\), compare
the central interpolation (16) with its seam version.
On the complete fixed retained contours (17), the ratio
\(\Pi_N(s+q)/\Pi_N(s)\) has rate
\[
                    \Re[g(s+iv)-g(s)]+O(\log N/N).
 \tag{23}
\]
All its arguments remain in fixed regular real strips.
The cardinal has rate \(K(v)\) from
[the real-endpoint vertical envelope](research_mixed_fourier_real_endpoint_vertical_envelope.md),
with \(K(0)=\pi\Im y\). It is smooth on this smaller
height interval. Combining (22)--(23), the change from
the seam profile is bounded above by
\[
 \omega(\delta)=
 \sup_{\substack{s\text{ on the fixed retained contours}\\|v|\le\delta}}
 \bigl|\Re[g(s+iv)-g(s)]\bigr|
 +\pi\delta+\sup_{|v|\le\delta}|K(v)-K(0)|,
 \qquad \omega(\delta)\longrightarrow0 .
 \tag{24}
\]
The half-grid cut displacements remain \(O(1/N)\) and cost
only uniform finite prefactors. Incoming parameters range
over their original compact family.

The seam theorem pays each central retained group by the
raw loss \(3/400\). Choose one fixed
\(\delta<\Im y/2\) with \(\omega(\delta)<3/800\).
Repeating those same four exact contours at each
\(\alpha_N+iv\) therefore preserves a raw loss at least
\(3/800\). No finite coherent sum is replaced by the sum
of the moduli of its central physical rows.

The physical rows \(j<L_N\) require no new interpolation
comparison. The zero-safe vertical envelope bounds their
whole absolute boundary integral by their real-seam
maximum, with an arbitrary fixed tolerance and a polynomial
prefactor. Equations (9), (21) of the seam theorem pay
that maximum by \(B_\eta-3/400-1/35000\).
In fact this pays these physical low rows on the entire
vertical line, not only the collar.

For the right endpoint \(\beta_N=\alpha_N+1\), periodicity
of \(p_j\) and the exact cardinal monodromy give, on the
present collar,
\[
 S_N^<(\beta_N+iv)
   =\frac{Y^N}{1+Y^N e^{2\pi Nv}}\,
                          S_N^<(\alpha_N+iv).
 \tag{25}
\]
The denominator is safe here:
\(|Y^N e^{2\pi Nv}|\le e^{-\pi N\Im y}\).
For large \(N\) the right multiplier is at most
\(2|Y|^N\). Equation (25) is used only on this stated
zero-free collar; it is not division by a monodromy
factor elsewhere on the vertical line.

It follows, after one aggregate tolerance and polynomial
absorption, that
\[
 \boxed{\quad
 |d_N(X)|^{\eta/2}
 \left|iN\int_{-\delta}^{\delta}w_{N,0}(v)
     [S_N^<(\beta_N+iv)-S_N^<(\alpha_N+iv)]\,dv\right|
                 \le e^{N(B_\eta(x)-1/1000)} .
 \quad}
 \tag{26}
\]
The proof also bounds the integral with an absolute value
inside. Here
\(w_{N,0}=1/(1+e^{2\pi Nv})-\boldsymbol1_{\{v<0\}}\).
It has modulus at most one on the collar, including both
one-sided limits at zero.

The outgoing current is the real-endpoint one, so the old
unpenalized \(h_q\)-to-zero segment has not disappeared:
it is included exactly in the bent main path. The source
identity, before any modulus, remains
\[
 V_N^<
   =N\int_\Gamma S_N^<(q)\,dq
       +iN\int_{\mathbb R}w_{N,0}(v)
          [S_N^<(\beta_N+iv)-S_N^<(\alpha_N+iv)]\,dv .
 \tag{27}
\]
The prescribed left portion of \(\Gamma\) is paid by
(21) and the short endpoint segment. Other parts of
\(\Gamma\) retain their own proofs and correction terms.

The already proved infinite vertical tails have a fixed
exponential gap. Together with (26), this leaves only a
fixed middle range \(\delta\le|v|\le H\), with the central
retained indices, in this outgoing vertical source.
No bound for that remaining middle current, no
noncancellation of the whole cap, and no attachment theorem
is inferred from the results above.
