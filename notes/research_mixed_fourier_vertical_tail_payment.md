# A uniform gap on the two infinite outgoing boundary tails

Research deduction, 7 November 2026. The exact vertical current left
after removing the outgoing aliases has exponentially small upper
and lower tails, uniformly in the level. The upper tail uses the
already proved coherent half-index comparison; taking its height
large then controls all smaller retained indices. The lower tail
has a uniform damping proportional to the level throughout.

The proof gives the existence of a fixed height \(H\), without
evaluating or optimizing it. It leaves the compact vertical segment
\([-H,H]\) and the complete main path unestimated. No numerical
evaluation, new source certificate or replay is used.

## 1. The actual source and the tail to be bounded

Keep the actual canonical references and incoming targets from the
[completed high-index theorem](research_mixed_fourier_right_cap_coherent_high_tail_payment.md):
\[
 \eta\in\{0,1\},\quad a_*\in K_{3+\eta},\quad
 a=x+i\Im a_*,\quad x\in P=[11/50,9/20],\quad
 y=x_0=\xi+i\upsilon,\quad Y=e^{2\pi iy}.
 \tag{1}
\]
Write \(h=\Im a_*\) and \(X=e^{-2\pi ia}\). The reference,
action, marginal and incoming halfweight are unchanged.
When \(\eta=1\) the incoming height is negative and
unselected, as in the completed bare-source theorem; no independent
height enlargement is made. Retain its original plane
\[
 B_\eta(x)=M_\eta+p_\eta(x-\Re a_*)
                          -\kappa(x-\Re a_*)^2,
 \qquad \kappa=1/2500000.
 \tag{2}
\]
All uniform statements below concern this compact canonical family
and its real target interval, with the two types as a finite union.

Use the exact functions from the
[alias-elimination theorem](research_mixed_fourier_factorial_alias_elimination.md):
\[
 \begin{gathered}
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad p_j(Z)=(rZ;r)_j,\quad
 M_N=\lceil N/2\rceil-1,\\
 A_{j,N}=X^{-j}p_j(X)/P_j^3,\qquad
 \widehat S_N(q)=
    \sum_{j=0}^{M_N}A_{j,N}p_j(e^{-2\pi iq})\widehat f_N(q;y),\\
 \alpha_N=-1/(2N),\quad\beta_N=\alpha_N+1,\qquad
 w_{N,h_0}(v)=\frac1{1+e^{2\pi Nv}}-\boldsymbol1_{\{v<h_0\}},
 \quad h_0=\Im q_*<0.
 \end{gathered}
 \tag{3}
\]
The global factorial chart specifies \(\widehat f_N\) exactly,
including its zeros. For \(H>1\), define the nonnegative tail majorant
\[
 \mathcal V_{N,H}=
 N|d_N(X)|^{\eta/2}
 \int_{|v|\ge H}|w_{N,h_0}(v)|
  \bigl\{|\widehat S_N(\alpha_N+iv)|
                 +|\widehat S_N(\beta_N+iv)|\bigr\}\,dv .
 \tag{4}
\]
It bounds the modulus of the actual signed vertical tail, without
dividing by a monodromy factor or a Fourier weight.

**Theorem 1.** There exist a fixed \(H>1\) and \(N_0\) such that,
for all \(N\ge N_0\), both parities and every parameter in (1),
\[
                   \mathcal V_{N,H}
                \le \exp\{N(B_\eta(x)-1/100)\}.
 \tag{5}
\]
The proof establishes existence of these constants only.

## 2. Uniform finite-source bounds along the vertical ends

Put
\[
 \begin{split}
 I_a(s)&=\int_0^s\log|1-Xe^{-2\pi iu}|\,du,\qquad J(s)=\Re g(s),\\
 A(s;a)&=I_a(s)-3J(s)-2\pi hs,\qquad 0\le s\le1/2,\\
 D_+(y)&=\Re g(1-y)-2\pi\xi\upsilon,\qquad
 D_-(y)=\Re g(1-y)+\pi\upsilon.
 \end{split}
 \tag{6}
\]
The logarithmic zeros of \(I_a\) are integrable. The original
[uniform product bound](research_mixed_right_half_source_reduction.md),
equations (6)--(7), gives
\[
 |A_{j,N}|\le C N^b e^{NA(j/N;a)}
                         \qquad(0\le j\le M_N).
 \tag{7}
\]
Its constants are uniform on (1), including polynomial zeros and
\(|X|=1\). The full finite factorial bound is
\(\log|P_j|=NJ(j/N)+O(\log N)\), including \(j=0\).
The allocated actual Fourier factor satisfies, for any fixed
\(\tau>0\),
\[
 |d_N(X)|^{\eta/2}
       \le C_\tau N^{b_\tau}
            e^{N(-\eta\Re g(a)/2+\tau)}.
 \tag{8}
\]
This is precisely the halfweight statement used in the
[coherent retained-rate theorem](research_mixed_fourier_right_cap_coherent_retained_rate.md).
No outgoing halfweight is added.

The remainder in the exact cyclotomic factorial formula makes the
large-height bounds uniform in \(N\). To spell this out, let
\(\upsilon_{\max}<1\) contain the fixed original height. For
\(t>1+\upsilon_{\max}\), set
\[
 r_t=e^{-2\pi(t-\upsilon_{\max})},\qquad
 b(t)=(2+t)\frac{r_t^2}{1-r_t^2}
                           +\frac12\frac{r_t}{1-r_t},
 \qquad
 \epsilon(H)=\sup_{t\ge H}b(t)+\frac12e^{-2\pi H}.
 \tag{9}
\]
Then \(\epsilon(H)\to0\). Indeed the exact factorial remainder
\(\mathcal E_N(z)\) in equations (2)--(3) of the alias note satisfies
\[
 \frac{|\mathcal E_N(z)|}{N}
 \le (2+t)\frac{r_t^2}{1-r_t^2}
                         +\frac12\frac{r_t}{1-r_t}
 \tag{10}
\]
for all \(N\ge2\), at the lower-half-plane arguments used in either
vertical end with \(|v|=t\). Here \(|\Re z|<1\),
\(|\Im z|\ge t-\upsilon_{\max}\), and \(|z|\le2+t\).
To obtain (10), use \(|e^{-2\pi iz}|^N\le r_t^2\),
\((N-1)/(2N)\le1/2\), and the explicit bound in that note.

The retained finite polynomial is bounded directly:
\[
 \begin{split}
 |p_j(e^{-2\pi i(u+iv)})|
     &\le e^{2\pi jv}(1+e^{-2\pi v})^j &&(v\ge H),\\
 |p_j(e^{-2\pi i(u+iv)})|
     &\le (1+e^{2\pi v})^j &&(v\le-H).
 \end{split}
 \tag{11}
\]
Its extra logarithmic cost divided by \(N\) is at most
\(\tfrac12e^{-2\pi H}\). Thus (9) controls both the exact factorial
remainder and this product cost, at every height beyond \(H\).

The original regular-strip expansion at \(1-y-1/N\) gives
\[
 \frac{|\Pi_N(1-y-1/N)|}{N^{3/2}}
                 \le C N^b e^{N\Re g(1-y)}
 \tag{12}
\]
for all sufficiently large \(N\); the shift \(1/N\) costs only a
uniform constant. Equations (7)--(12) and the exact marked
factorial formulas now imply the following row bounds.
For \(v\ge H\), \(s=j/N\), at the left edge,
\[
 \begin{split}
 &|w_{N,h_0}(v)|\,|d_N(X)|^{\eta/2}
       |A_{j,N}p_j(e^{-2\pi i(\alpha_N+iv)})
                         \widehat f_N(\alpha_N+iv;y)|\\
 &\quad\le C_\tau N^{b_\tau}
   \exp N\left\{ A(s;a)+D_+(y)-\frac{\eta}{2}\Re g(a)
             -\pi(1-2s)v+\epsilon(H)+\tau\right\}.
 \end{split}
 \tag{13}
\]
At the right edge there is the additional factor \(e^{-2\pi Nv}\),
apart from the same uniformly bounded remainder estimates.
The cancellation of the half-grid shift with the finite \(N-1\)
cardinal phase is exact: its upper modulus at the left edge is
proportional to \(e^{\pi Nv}\). The factors \(p_j\) and \(w\)
then give \(e^{-\pi(N-2j)v}\).

For \(v\le-H\), the corresponding left-edge bound is
\[
 \begin{split}
 &|w_{N,h_0}(v)|\,|d_N(X)|^{\eta/2}
       |A_{j,N}p_j(e^{-2\pi i(\alpha_N+iv)})
                         \widehat f_N(\alpha_N+iv;y)|\\
 &\quad\le C_\tau N^{b_\tau}
   \exp N\left\{ A(s;a)+D_-(y)-\frac{\eta}{2}\Re g(a)
            +2\pi(1-\xi)v+\epsilon(H)+\tau\right\}.
 \end{split}
 \tag{14}
\]
The right edge has the additional factor \(e^{-2\pi N\upsilon}\),
with the same error allowance. In (14), the prefactor
\(e^{\pi(N-1)\upsilon}\) and the left half-grid displacement
combine to \(e^{\pi N\upsilon}\); this explains the constant
\(D_-\). These bounds use the original \(\widehat f_N\), rather
than a limiting symbol continued through its zeros.

## 3. The half-index comparison pays the upper limiting rate

The original action obeys
\[
 \Re g(1-y)=\frac{\Im\operatorname{Li}_2(Y)}{2\pi}.
 \tag{15}
\]
This uses the original lower-half-plane primitive, since
\(\Im(1-y)<0\). With \(\rho=|Y|<5/8\), the absolutely
convergent series gives
\[
 D_+(y)<\frac{\operatorname{Li}_2(\rho)}{2\pi}
 \le\frac{\rho+\rho^2/[4(1-\rho)]}{2\pi}
 <\frac{85}{576}.
 \tag{16}
\]
Here \(\xi\upsilon>0\), and the last strict inequality uses
\(\pi>3\).
The original \(\rho<123/200\) and the elementary logarithm
witness in the
[upper outgoing collar theorem](research_mixed_fourier_right_cap_upper_outgoing_collar.md)
give
\[
 \pi\upsilon=-\tfrac12\log\rho>\frac{77}{400},
 \qquad
 \pi\upsilon-D_+(y)>
             \frac{647}{14400}>\frac1{25}.
 \tag{17}
\]

The completed Wall contraction has
\[
 \Phi(s;y)=g(s)-\pi iy+I_{\rm W}(1-s,Y),\qquad
 \Re I_{\rm W}(1/2,Y)=\int_0^{1/2}\log|R(t,0,Y)|\,dt>0.
 \tag{18}
\]
The strict positivity follows from the proved exterior degree root
\(|R|>1\), throughout the closed half-degree interval. Since
\(J(1/2)=0\), its actual coherent half-index rate is
\[
 \mathcal E_\eta(1/2;a)=
 A(1/2;a)+\pi\upsilon+\Re I_{\rm W}(1/2,Y)
                              -\frac{\eta}{2}\Re g(a).
 \tag{19}
\]
The [proved half-index comparison](research_mixed_fourier_right_cap_coherent_high_tail_payment.md),
equation (18), bounds this by \(B_\eta(x)-1/35000\).
Therefore the limiting upper boundary rate satisfies
\[
 A(1/2;a)+D_+(y)-\frac{\eta}{2}\Re g(a)
     <B_\eta(x)-\frac1{35000}-\frac{647}{14400}.
 \tag{20}
\]
This is a comparison with the original plane; no physical-height
reset or unallocated source bound is used.

The functions in (6) are jointly continuous in \(s,a\), including
their integrable logarithmic zeros. The actual reference family,
its plane and the target interval in (1) are compact. Hence there
is a fixed \(\delta>0\) such that
\[
 A(s;a)+D_+(y)-\frac{\eta}{2}\Re g(a)
       \le B_\eta(x)-\frac3{100},
                    \qquad 1/2-\delta\le s\le1/2.
 \tag{21}
\]
On the remaining compact set \(0\le s\le1/2-\delta\), the same
rate minus \(B_\eta(x)\) has a finite upper bound. Choose a fixed
height \(H\) sufficiently large that
\[
 A(s;a)+D_+(y)-\frac{\eta}{2}\Re g(a)
          -\pi(1-2s)H
       \le B_\eta(x)-\frac3{100}
                       \qquad(0\le s\le1/2).
 \tag{22}
\]
This is possible because \(1-2s\ge2\delta\) on the remaining
set; on (21) the extra term is nonpositive. No numerical height
or new comparison is selected.

## 4. Integrating the two tails

Enlarge that fixed \(H\) if needed so that
\(\epsilon(H)<1/200\). Compactness and \(1-\xi>0\) also permit
\[
 A(s;a)+D_-(y)-\frac{\eta}{2}\Re g(a)
                   -2\pi(1-\xi)H
       \le B_\eta(x)-\frac3{100},
                         \qquad 0\le s\le1/2.
 \tag{23}
\]
Choose \(\tau=1/200\) in (8).
For \(v\ge H\), split the damping in (13) at \(H\) and use
(22). Its remaining factor is
\[
 e^{-\pi(N-2j)(v-H)},\qquad
 N-2j\ge N-2M_N=
          \begin{cases}2,&N\text{ even},\\1,&N\text{ odd}.\end{cases}
 \tag{24}
\]
The integral of this factor is at most \(1/\pi\). The upper
tail of each row is consequently bounded by a polynomial in
\(N\) times \(e^{N(B_\eta(x)-1/50)}\).
The smaller right-edge contribution obeys the same bound.

For the lower tail, (14) and (23) leave the integrable factor
\[
              e^{-2\pi N(1-\xi)(|v|-H)}.
 \tag{25}
\]
Its integral is \(1/[2\pi N(1-\xi)]\).
The finite number of rows, the outside coefficient \(N\) in
(4), and all source constants change only the polynomial
prefactor. Thus uniformly on (1),
\[
            \mathcal V_{N,H}
             \le C N^b e^{N(B_\eta(x)-1/50)}.
 \tag{26}
\]
For all sufficiently large \(N\), \(C N^b\le e^{N/100}\).
This proves (5).

The argument bounds both tails absolutely while retaining the
whole finite polynomial at every step. It neither assigns a gap
to the compact vertical segment nor equates the distinct cardinal
interpolations off the lattice. In the exact two-group identity
of the alias-elimination theorem, only the portions \(|v|\ge H\)
are paid here. The original main path and \(|v|\le H\) still carry
their exact source and require separate analysis.
