# A prescribed Fourier packet for the full cumulative response

Research deduction, 7 November 2026. The original second-order
column recurrence supplies a smooth next-order backward ratio.
A corrected cumulative telescoper, with both actual boundary values,
gives the nonzero row asymptotic on every fixed compact interval in
\((0,1/2)\). It controls the full initialized first-node coefficient
vector to relative error \(O(N^{-1})\) in norm. Its explicit phase
correction has a nonzero prescribed zero Fourier coefficient and
the full Gaussian Fourier window.

The coefficient index Fourier transform is distinct from the
outgoing Newton evaluation in the original selected sector.
All endpoint and top-index contributions remain in the source.
No numerical evaluation is used.

## 1. Original recurrence and its attracting ratio

Use the exact source and notation of the
[peak-window theorem](research_mixed_next_low_cardinal_peak_window.md):
\[
 \begin{gathered}
 D=N-1,\quad r=e^{-2\pi i/N},\quad
 \kappa=e^{\pi iD^2/(2N)},\quad
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\\
 \gamma=MJM^3e_0,\qquad v_j=(-q)^{-j}\gamma_j,\qquad q=e^{\pi i/N},\\
 a_0=1-\frac{\gamma_0}{\kappa^2N^2},\qquad
 a_j-a_{j-1}=-\frac{v_j+c(j/N)v_{j-1}}{\kappa^2N^2},
 \qquad c(t)=\frac{X(t)}{1-X(t)},\quad X(t)=e^{-2\pi it}.
 \end{gathered}
 \tag{1}
\]
The original analytic functions on \(0<t<1/2\) are
\[
 \begin{gathered}
 d(t)=4\sin^2\pi t,\qquad
 \lambda(t)=\frac{3-2X(t)+\sqrt{4/X(t)-3}}2,\qquad
 \mu(t)=\frac{3-2X(t)-\sqrt{4/X(t)-3}}2,\\
 I(t)=\int_0^t\log\lambda(s)\,ds,\qquad
 J(t)=\int_0^t\log(2\sin\pi s)\,ds,\qquad
 A(t)=\Re I(t)-2J(t),\\
 G(t)=\sqrt{\frac{\lambda(t)}{\lambda(t)-\mu(t)}},
 \qquad \rho(t)=\frac{d(t)}{\lambda(t)},\qquad
 u(t)=\frac{1-\sqrt{4/X(t)-3}}2,\qquad F(t)=\frac1{1-u(t)} .
 \end{gathered}
 \tag{2}
\]
The branches continue from the original \(+1\) square root,
zero logarithm, and \(G(0)=1\). Their identities include
\[
 \lambda+\mu=3-2X,\quad
 \lambda\mu=d(1-X),\quad
 1+c\rho=F(1-\rho),\quad
 \lambda-d=(1-u)^2\ne0.
 \tag{3}
\]
The original profile has its unique nondegenerate maximum
\(x_*\in(1/3,1/2)\); put \(\alpha=-A''(x_*)>0\).

Fix \(0<a<x_*<b<1/2\), and write \(\epsilon=N^{-1}\).
The [original Fourier-column theorem, equations (6) and (9)](research_three_crossing_next_crossing_fourier.md)
gives both the exact recurrence and its actual initialized solution:
\[
 \begin{split}
 d(t_j+\epsilon)v_{j+1}
   &=A_\epsilon(t_j)v_j-(1-X(t_j))v_{j-1},
       \qquad A_\epsilon(t)=3-(1+e^{-2\pi i\epsilon})X(t),\\
 v_j&=\gamma_0 S_j^{-2}G(t_j)e^{NI(t_j)}
                          (1+O_b(N^{-1})),\qquad t_j=j/N,\\
 |\gamma_0|&=N^{3/2}(1+O(N^{-1})).
 \end{split}
 \tag{4}
\]
The recurrence is obtained by dividing the original normalized
\(y_j=S_j^2v_j/\gamma_0\) equation by \(S_j^2\). No leading
solution is substituted for the actual column.

On compact intervals away from zero, (4) ensures that consecutive
values are nonzero for large \(N\), and gives
\(R_j:=v_{j-1}/v_j=\rho(t_j)+O(\epsilon)\).
Its exact evolution is
\[
 R_{j+1}=\mathcal T_{\epsilon,t_j}(R_j),\qquad
 \mathcal T_{\epsilon,t}(z)
       =\frac{d(t+\epsilon)}
                    {A_\epsilon(t)-(1-X(t))z}.
 \tag{5}
\]
At \(\epsilon=0,z=\rho(t)\), its denominator is \(\lambda(t)\)
and
\[
 \partial_z\mathcal T_{0,t}(\rho(t))
             =\frac{d(t)(1-X(t))}{\lambda(t)^2}
             =\frac{\mu(t)}{\lambda(t)} .
 \tag{6}
\]
The original column theorem proves \(|\mu|<|\lambda|\) throughout
\(0<t<1/2\). Thus (6) has a uniform modulus gap on any fixed
compact interval containing \([a/4,b]\). This remains true
through \(x_*\), where it is \(|\rho|\), not \(|\mu/\lambda|\),
that reaches one.

## 2. The next-order ratio follows from the recurrence

Define the smooth function
\[
 \rho_1(t)=
   \frac{\rho(t)\{\lambda'(t)-2\pi iX(t)\}}{\lambda(t)-\mu(t)}
   =\frac{\rho(t)\{\lambda'(t)-\mu'(t)\}}
                         {2\{\lambda(t)-\mu(t)\}} .
 \tag{7}
\]
The second equality follows from
\((\lambda+\mu)'=4\pi iX\). All its denominators stay nonzero
on the stated compact intervals.

This next-order control is also contained in the original
[dominant-profile proof, equation (18)](research_three_crossing_next_crossing_dominant_profile.md),
after converting its forward \(y_j/y_{j-1}\) ratio to the present
backward \(v_{j-1}/v_j\) normalization. We give the recurrence
calculation here to specify that conversion and its initialized
error. The new application is the corrected cumulative telescoper.

**Lemma 1.** Uniformly for
\(\lfloor aN/2\rfloor\le j\le bN\),
\[
                    R_j=\rho(t_j)+\epsilon\rho_1(t_j)
                                              +O(\epsilon^2).
 \tag{8}
\]

*Proof.* Put \(R_{\rm app}(t)=\rho(t)+\epsilon\rho_1(t)\).
Uniform Taylor expansion on the fixed compact interval gives
\[
 \begin{split}
 A_\epsilon(t)&=3-2X(t)+2\pi i\epsilon X(t)+O(\epsilon^2),\\
 R_{\rm app}(t+\epsilon)
        &=\mathcal T_{\epsilon,t}(R_{\rm app}(t))+O(\epsilon^2).
 \end{split}
 \tag{9}
\]
For the second identity the coefficient equation is exactly
\[
 (1-\mu/\lambda)\rho_1
       =d'/\lambda-\rho'-2\pi i\rho X/\lambda
       =\rho(\lambda'-2\pi iX)/\lambda ,
 \tag{10}
\]
which is (7).

Choose a fixed radius about \(\rho(t)\) so small that, for
sufficiently large \(N\), the rational map (5) has nonzero
denominator and complex derivative of modulus at most
\(q_0<1\) on each such disk. Equation (6), compactness, and
continuity justify one radius and one \(q_0\) for all \(t\).
Both the actual ratio and \(R_{\rm app}\) lie in these disks
by the original \(O(\epsilon)\) ratio estimate. The disk is
convex, so the derivative bound gives
\[
 |R_{j+1}-R_{\rm app}(t_{j+1})|
   \le q_0|R_j-R_{\rm app}(t_j)|+C\epsilon^2 .
 \tag{11}
\]
Start at \(j_-=\lceil aN/4\rceil\), where (4) gives an
\(O(\epsilon)\) error. Iterating (11) to \(j\ge\lfloor aN/2\rfloor\)
costs no arbitrary restart or new initial condition:
\[
 |R_j-R_{\rm app}(t_j)|
        \le C\epsilon q_0^{j-j_-}
                          +C\epsilon^2/(1-q_0)=O(\epsilon^2).
 \tag{12}
\]
The first term is exponentially small there. This proves
the lemma from the actual recurrence, rather than by
differentiating the error in (4). \(\square\)

## 3. A corrected exact cumulative telescoper

Set
\[
 F_1(t)=\frac{\{c(t)+F(t)\}\rho_1(t)-\rho(t)F'(t)}
                                      {1-\rho(t)},\qquad
 F_\epsilon(t)=F(t)+\epsilon F_1(t).
 \tag{13}
\]
The identity \(\lambda-d=(1-u)^2\) keeps this denominator
nonzero through the peak. The functions and their fixed
derivatives are uniformly bounded on the chosen compact interval;
\(F_\epsilon\) is bounded away from zero for large \(N\).

Let \(k_0=\lfloor aN/2\rfloor\). Define exact quantities
\[
 \begin{split}
 \varepsilon^{(2)}_{k,N}
   &=v_k+c(t_k)v_{k-1}
       -\{F_\epsilon(t_k)v_k-F_\epsilon(t_{k-1})v_{k-1}\},\\
 H_N^{(2)}
   &=\kappa^2N^2a_{k_0-1}
                      +F_\epsilon(t_{k_0-1})v_{k_0-1}.
 \end{split}
 \tag{14}
\]
The same finite sum of the original increments gives
\[
       \kappa^2N^2a_j
        =-F_\epsilon(t_j)v_j+H_N^{(2)}
                          -\sum_{k=k_0}^j\varepsilon^{(2)}_{k,N}.
 \tag{15}
\]
The initialized homogeneous constant is retained exactly.

**Lemma 2.** On \(k_0\le k\le bN\),
\[
                    |\varepsilon^{(2)}_{k,N}|
                                  \le CN^{-2}|v_k|.
 \tag{16}
\]

*Proof.* Divide the first line of (14) by \(v_k\), substitute
(8), and expand \(F_\epsilon(t-\epsilon)\).
The order-zero term is
\(1+c\rho-F(1-\rho)=0\). The coefficient of \(\epsilon\) is
\[
             (c+F)\rho_1-\rho F'-(1-\rho)F_1=0
 \tag{17}
\]
by (13). All remaining terms have uniform order
\(\epsilon^2\), since the actual ratio error in (8) does.
This proves (16). \(\square\)

The actual early-source argument in the peak-window theorem
applies unchanged, because \(F_\epsilon\) is bounded:
\[
 |H_N^{(2)}|\le CN^C e^{NA(a/2+1/N)}.
 \tag{18}
\]
For \(a\le t_j\le x_*\), that theorem's absolute backward-sum
estimate gives \(\sum_{k=k_0}^j|v_k|\le C\sqrt N|v_j|\).
This controls the left part of the desired interval.

For the right part, use the exact source theorem
[terminal anchor, Proposition 3](research_mixed_next_low_cardinal_terminal_anchor.md).
Its proof retains \(a_D=d_N'(1)/N\), the full forced polynomial
\(d_N\), and the original global column. It gives, for every
fixed \(b_0\in(x_*,1/2)\),
\[
       \max_{j/N\ge b_0}|a_j|
                      \le C_{b_0}N^{C_{b_0}}e^{NA(b_0)}.
 \tag{18a}
\]
The endpoint rate is strictly below \(1/6<A(1/2)\), as proved
there; it has not been discarded.

Choose \(b<b_0<1/2\), put \(m_0=\lceil b_0N\rceil\), and
apply Lemmas 1--2 on a slightly larger fixed compact interval.
Summing the same exact increments backwards gives
\[
 \begin{split}
 \kappa^2N^2a_j
   &=-F_\epsilon(t_j)v_j+\widetilde H_N^{(2)}
                     +\sum_{k=j+1}^{m_0}\varepsilon^{(2)}_{k,N},\\
 \widetilde H_N^{(2)}
   &=\kappa^2N^2a_{m_0}+F_\epsilon(t_{m_0})v_{m_0},\\
 |\widetilde H_N^{(2)}|
   &\le CN^C e^{NA(b_0)} .
 \end{split}
 \tag{18b}
\]
The last bound follows from (18a), the compact column packet,
and decrease of \(A\) beyond its maximum.

On a fixed interval \([x_*,b_1]\), with \(b_0<b_1<1/2\),
strict decrease and nondegeneracy give
\(-A'(s)\ge c_0(s-x_*)\). The same integrated Gaussian
comparison as on the left therefore gives
\[
                \sum_{k=j+1}^{m_0}|v_k|
                              \le C\sqrt N|v_j|,
                         \qquad x_*\le t_j\le b .
 \tag{18c}
\]
The quotient \(\widetilde H_N^{(2)}/v_j\) is exponentially
small there because \(A(b_0)<A(b)\). The original \(H_N^{(2)}\)
is likewise exponentially small relative to \(v_j\) on the
left interval. Equations (15)--(18c) now prove the actual-row
formula on the entire fixed compact interval:
\[
 a_j=-\frac{v_j}{\kappa^2N^2}
        \{F(t_j)+N^{-1}F_1(t_j)+O_{a,b}(N^{-3/2})\},
                         \qquad a\le j/N\le b .
 \tag{19}
\]
Both boundary constants in this proof are fixed by the actual
source. In particular the original leading row symbol now has
relative error \(O(N^{-1})\) on every compact subinterval of
\((0,1/2)\), by enlarging that compact to such an \([a,b]\).
Multiplication by the original holomorphic factorial packet
extends the complete outgoing row formula (31) of the
[endpoint theorem](research_mixed_next_low_cardinal_endpoint_packet.md)
to the same interval, with its original nonzero symbol,
\(O(N^{-1})\) relative error and fixed outgoing jets.
No continuous incoming interpolation or incoming derivatives
of \(a_j\) are inferred.

## 4. Uniform control of the whole coefficient vector

Write \(\mathbf a_N=(a_j)_{j=0}^{N-1}\) and define
\[
 p^{(s)}_{N,j}=
 \begin{cases}
 -F_s(t_j)v_j/(\kappa^2N^2),&a\le t_j\le b,\\
 0,&\text{otherwise},
 \end{cases}
 \qquad F_0=F,\quad F_2=F_\epsilon .
 \tag{20}
\]
The superscript labels these two comparison vectors, not a
different source sector.

**Theorem 1.** The complete actual vector satisfies
\[
 \begin{split}
 \|\mathbf a_N-p^{(2)}_N\|_2
                          &\le CN^{-11/4}e^{NA(x_*)},\\
 \|\mathbf a_N-p^{(0)}_N\|_2
                          &\le C N^{-1}\|p^{(0)}_N\|_2,\\
 \|\mathbf a_N\|_2
   &=H_*\left(\frac{\pi}{\alpha}\right)^{1/4}
       N^{-5/4}e^{NA(x_*)}(1+O(N^{-1/2})),\\
 H_*&=\frac{|F(x_*)G(x_*)|}{2\sin(\pi x_*)}.
 \end{split}
 \tag{21}
\]

*Proof.* Inside the fixed interval \([a,b]\), equation (19) and
the fact that \(F\) is bounded away from zero give
\[
                 |a_j-p^{(2)}_{N,j}|
                           \le CN^{-3/2}|p^{(0)}_{N,j}|.
 \tag{22}
\]
For every fixed neighborhood \(U\) of \(x_*\) with closure
inside \((a,b)\), the terminal-anchor theorem proves
\[
        \max_{j/N\notin U}|a_j|
                   \le CN^C e^{N\{A(x_*)-\eta_U\}},
                          \qquad \eta_U>0.
 \tag{23}
\]
Its proof sums the exact increments from the appropriate actual
boundary. In particular it retains the terminal derivative of
\(d_N\), rather than choosing the homogeneous component.
Outside \([a,b]\), both comparison vectors vanish, so (23)
bounds their difference from the actual vector exponentially.
Consequently
\[
 \|\mathbf a_N-p^{(2)}_N\|_2
       \le CN^{-3/2}\|p^{(0)}_N\|_2
                        +CN^C e^{N\{A(x_*)-\eta_U\}}.
 \tag{24}
\]

The compact Gaussian computation already proved for the simple
particular vector gives
\[
 \|p^{(0)}_N\|_2
   =H_*\left(\frac{\pi}{\alpha}\right)^{1/4}
        N^{-5/4}e^{NA(x_*)}(1+O(N^{-1/2})).
 \tag{25}
\]
Since \(F\) is bounded away from zero,
\(\|p^{(2)}_N-p^{(0)}_N\|_2\le CN^{-1}\|p^{(0)}_N\|_2\).
Equation (25) inserted in (24) proves the first line of (21);
its relative error is \(O(N^{-3/2})\).
This proves the second line as well, and (25) proves the norm
formula. \(\square\)

## 5. The prescribed full zero mode and almost invariance

Use the same explicit unit phase as in the peak-window theorem,
on \(a\le t_j\le b\):
\[
 \sigma_{N,j}
   =-\frac{\gamma_0}{\kappa^2|\gamma_0|}
       \frac{F(t_j)G(t_j)}{|F(t_j)G(t_j)|}
                           e^{iN\Im I(t_j)}.
 \tag{26}
\]
Outside that interval choose any unit phase, for example one.
Define the whole normalized vector and its Fourier transform by
\[
 \zeta_{N,j}=\sigma_{N,j}^{-1}a_j/\|\mathbf a_N\|_2,\qquad
 \widehat\zeta_N(m)=N^{-1/2}\sum_{j=0}^{N-1}
                              \zeta_{N,j}e^{-2\pi imj/N}.
 \tag{27}
\]
The phase depends only on the original endpoint and the fixed
column branch. It does not depend on a chosen maximizing Fourier
index or on the values of the cumulative coefficients.

**Theorem 2.** For every fixed \(0\le T<\infty\), uniformly for integer
representatives \(|m|\le T\sqrt N\),
\[
 \boxed{\quad
 \widehat\zeta_N(m)
  =\left(\frac{4\pi}{\alpha}\right)^{1/4}
      N^{-1/4}e^{-2\pi imx_*}
         \exp\left(-\frac{2\pi^2m^2}{\alpha N}\right)
                            (1+O_T(N^{-1/2})).
 \quad}
 \tag{28}
\]
In particular the prescribed mode \(m=0\) satisfies
\(|\widehat\zeta_N(0)|\ge cN^{-1/4}\).
For the cyclic shift \((\mathsf Sz)_j=z_{j-1\bmod N}\),
\[
             \|\mathsf S\zeta_N-\zeta_N\|_2
                   =\sqrt{\frac{\alpha}{2N}}+O(N^{-1}).
 \tag{29}
\]

*Proof.* On \([a,b]\), put
\[
 h_{N,j}=\frac{|\gamma_0|}{N^2S_j^2}
             |F(t_j)G(t_j)|e^{N\Re I(t_j)},
 \tag{30}
\]
and extend it by zero. Normalize this positive model to
\(h_N^\circ\). The original \(O(N^{-1})\) column packet in
(4), together with Theorem 1 and normalization, yields
\[
                         \|\zeta_N-h_N^\circ\|_2=O(N^{-1}).
 \tag{31}
\]
The Gaussian computation for this same model is given in the
peak-window theorem. Its smooth, nonzero prefactor has the same
leading Fourier Gaussian as the original column, namely the
right side of (28) with \(O_T(N^{-1/2})\) error. Unitarity of
the Fourier transform changes each coefficient by at most
\(O(N^{-1})\) in (31). This is smaller than the
\(O_T(N^{-3/4})\) absolute error already allowed in (28).

For the shift, the logarithm of an adjacent positive-model ratio
near the peak is
\[
 \log(h_{N,j-1}/h_{N,j})
       =-A'(t_j)+O(N^{-1})
       =\alpha s_j/\sqrt N+O((1+s_j^2)/N),
       \qquad s_j=(j-Nx_*)/\sqrt N .
 \tag{32}
\]
The normalized squared weights have limiting Gaussian density
\(\sqrt{\alpha/\pi}e^{-\alpha s^2}\), with their fixed moments.
Thus the model's squared shift residual is
\(\alpha/(2N)+O(N^{-3/2})\), just as in the original column
proof. Its two truncation boundaries have a strict profile gap.
Taking the square root and then using (31) proves (29).
The same strict gap removes the cyclic seam. \(\square\)

Both parities and the actual initial forcing are retained in
these theorems. The complementary vector \((1-a_j)_j\) has the
same conclusions after replacing \(\sigma_N\) by \(-\sigma_N\):
its difference from \(-\mathbf a_N\) has norm \(\sqrt N\),
exponentially smaller than (21).

## 6. The prescribed observation and its remaining limitation

The nonzero zero mode in (28) is the explicit linear functional
\[
        N^{-1/2}\sum_{j=0}^{N-1}\sigma_{N,j}^{-1}a_j .
 \tag{33}
\]
It is unwindowed and applies to the complete initialized vector.
The improved recurrence estimate is essential: the earlier
relative \(O(N^{-1/4})\) whole-vector error was of the same
order as a single Fourier coefficient and did not prove (33).

In original coefficient coordinates, (29) is almost invariance
under the explicit unitary
\(\operatorname{diag}(\sigma_N)\mathsf S
\operatorname{diag}(\sigma_N)^{-1}\).
Neither this operator nor (33) is identified with the prescribed
outgoing Newton row
\(\sum_j a_jp_j(Z)/P_j^{1+\beta}\). The exact outgoing equation
and its boundary data remain the relevant source for that
different observation. The present result therefore does not
prove suppression or nonvanishing of either full selected sector,
or a new ordinary boundary asymptotic.
