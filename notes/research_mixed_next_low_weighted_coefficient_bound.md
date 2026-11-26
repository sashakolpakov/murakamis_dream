# The actual weighted low-node coefficient vector

Research deduction, 7 November 2026. The uniform low-node packet,
combined with the original low Newton coefficient estimate for the
prefix, bounds the entire actual weighted coefficient vector below
the next conditional action. The exterior cardinal evaluation of
its leading multiplier has the same original prefix bound.

This pays every coefficient observation of unit Euclidean norm.
The prescribed outgoing Newton row has a larger norm, so this
conclusion is not suppression of a complete Fourier sector.
The exact remaining norm expense is stated below. No numerical
evaluation is used.

## 1. The finite source and both coefficient vectors

Put
\[
 D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
 \kappa=q^{D^2/2},\quad P_j=(r;r)_j,\quad S_j=|P_j|,
 \quad p_j(Y)=(rY;r)_j .
 \tag{1}
\]
Use the complete original prefix
\[
 F_N(w,Y)=N\operatorname{CT}_X
       [U_{0,N}(w,X)C_{1,N}(X,Y)]
 \tag{2}
\]
and the original sector functionals
\[
 \mathcal S_{\sigma,\beta}[E](Z)
     =N[Y^{\sigma N}]\{E(Y)d_N(Y)C_{\beta,N}(Y,Z)\},
 \quad \sigma,\beta\in\{0,1\},\qquad
 C_{\beta,N}(Y,Z)=\sum_{j=0}^{D}
              \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}} .
 \tag{3}
\]
The exact source and its subsequent ordinary observation scalars
are those of the
[next-attachment theorem](research_mixed_three_four_next_conditional_attachment.md).
No final Gram factor is inserted in (3).

For a fixed small \(\delta>0\), set
\[
 \begin{gathered}
 I_N=\{0,\ldots,\lfloor\delta N\rfloor\},\quad B_b=r^b,\quad
 w_{b,N}(w)=F_N(w,B_b),\\
 \mathfrak l_b(Y)=\frac1N\sum_{\nu=0}^{D}(Yr^{-b})^\nu,\qquad
 E_{\mathrm{low},N}(w,Y)=\sum_{b\in I_N}w_{b,N}(w)\mathfrak l_b(Y).
 \end{gathered}
 \tag{4}
\]
These are the actual prefix values, not chosen test weights.
The [lowered-word identity](research_mixed_next_lowered_word_dual_observation.md)
gives exactly
\[
 w_{b,N}(w)=\frac{(-q)^bP_b}{\kappa^2N}\ell_{b,N}(w),\qquad
                    \ell_{b,N}(w)=(v(w)^TA_3^2)_b .
 \tag{5}
\]
Thus every original ordinary normal is already in \(\ell_{b,N}\).

Let \(a_j^{(1)}(B)=a_j(B)\) and \(a_j^{(0)}(B)\) be the two
complete coefficient families of the
[low-node packet](research_mixed_next_low_node_family_packet.md),
equations (2) and (62). In particular the selected coefficients
use the entire divided difference
\[
 a_j(B)=\frac1{P_j}\operatorname{CT}_Y
       \left[\frac{B\{d_N(Y)-d_N(B)\}}{Y-B}Y^{-j}p_j(Y)\right],
 \tag{6}
\]
and the other family is
\[
                a_j^{(0)}(B)
                   =\frac{B^{-j}p_j(B)}{P_bP_j}-a_j(B).
 \tag{7}
\]
The physical zeros in (7), the diagonal derivative in (6),
and the reset at \(j=N-b\) all remain.

Define the actual weighted vectors by
\[
 c_{\sigma,N,j}(w)=\sum_{b\in I_N}
                         w_{b,N}(w)a_j^{(\sigma)}(B_b),
 \qquad \mathbf c_{\sigma,N}(w)=(c_{\sigma,N,j}(w))_{j=0}^{D}.
 \tag{8}
\]
Then the whole sector is exactly
\[
 \boxed{\quad
 \mathcal S_{\sigma,\beta}[E_{\mathrm{low},N}](w,Z)
      =\sum_{j=0}^{D}c_{\sigma,N,j}(w)
                         \psi_{\beta,j}(Z),\qquad
 \psi_{\beta,j}(Z)=p_j(Z)/P_j^{1+\beta}.
 \quad}
 \tag{9}
\]
There is no additional \(N\) in (8)--(9). In particular (8)
does not discard either sector or combine the outgoing sum
with a physical root average.

## 2. The weighted vector has a strict action reserve

Let \(\mathcal W(w)\) be the original pendant \(33\) action,
\(M_{\mathrm{pend}}=\Re\mathcal W(-2)\), and let \(A_*\) be
the original next-crossing column maximum. The
[low Newton coefficient theorem](research_three_crossing_low_newton_coefficients.md)
proves, for a function \(\epsilon(\delta)\to0\),
\[
 |\ell_{b,N}(-2\cos u)|
   \le C_{\delta,\tau}N^{C_{\delta,\tau}}
      e^{N\{M_{\mathrm{pend}}-(1-\cos u)/4000
                                      +\epsilon(\delta)+\tau\}},
                \qquad -\pi\le u\le\pi,\quad b\in I_N .
 \tag{10}
\]
On a fixed small ordinary complex disk it proves the same
estimate after normalizing by \(e^{N\mathcal W(w)}\), with
the angular term omitted.
These are complete-source bounds: their proof keeps the
preparation forcing, the coherent outer removals and every
retained current.

Choose \(\delta\) also within the range of the low-node packet,
and require \(\delta<1/6\). Then every factor in \(S_b\) is
at most one, so
\[
                          |P_b|=S_b\le1\quad(b\in I_N).
 \tag{11}
\]
The new family theorem gives, for both sectors,
\[
       \sup_{b\in I_N}\|\mathbf a_N^{(\sigma)}(B_b)\|_2
                           \le C N^{-5/4}e^{NA_*}.
 \tag{12}
\]
The homogeneous vector in (7) is exponentially smaller than
this rate, including the portion past its physical termination.

Apply the triangle inequality to the exact sum (8), using
(5) and (10)--(12). The finite \(b\)-count costs only a
polynomial. This proves
\[
 \boxed{\quad
 \|\mathbf c_{\sigma,N}(-2\cos u)\|_2
  \le C_{\delta,\tau}N^{C_{\delta,\tau}}
     e^{N\{M_{\mathrm{pend}}+A_*-(1-\cos u)/4000
                                      +\epsilon(\delta)+\tau\}} .
 \quad}
 \tag{13}
\]
On the fixed small complex disk,
\[
 \left\|e^{-N\mathcal W(w)}\mathbf c_{\sigma,N}(w)\right\|_2
       \le C_{\delta,\tau}N^{C_{\delta,\tau}}
                           e^{N\{A_*+\epsilon(\delta)+\tau\}} .
 \tag{14}
\]
The original bounds used no modulus cancellation among the
weights, so the estimate holds even if their leading scalar
vanishes.

The previously proved constants are
\[
 M_{\mathrm{pend}}<\frac{769}{500},\qquad
 A_*<\frac{23}{50},\qquad
       \Re\mathcal P_\beta^+(-2,z)>\frac{51}{25}
 \tag{15}
\]
on the matched next-three and next-four ordinary and terminal
reference families. The first bound is recalled in
[the low-index kernel margin, Section 3](research_mixed_next_low_index_kernel_margin.md);
the second is the accepted original bound in
[the cap-seed theorem, Section 2](research_positive_three_crossing_cap_seed.md),
which records both certified bounds and their original source.
The last bound, including its exact reference scope, is
[the common next-action floor, equations (29)--(30)](research_mixed_next_high_cardinal_whole_sectors.md).
No independent product of containing rectangles is substituted
for those families.

Consequently the available uniform reserve before the small
\(\delta\) and finite-estimate tolerances is
\[
      \frac{51}{25}
       -\left(\frac{769}{500}+\frac{23}{50}\right)
                       =\frac{21}{500}>0 .
 \tag{16}
\]
For every fixed \(\eta<21/500\), choose \(\delta>0\) and
\(\tau>0\) sufficiently small, then reduce fixed neighborhoods
of the compact matched families and the complete-color disk.
Continuity of the original holomorphic actions and (14)
give
\[
 \left\|e^{-N\mathcal P_\beta^+(w,z)}
                      \mathbf c_{\sigma,N}(w)\right\|_2
                          \le C_\eta N^{C_\eta}e^{-N\eta}.
 \tag{17}
\]
One may spend a further positive part of the reserve to absorb
the polynomial. Cauchy's formula on smaller fixed neighborhoods
gives the same conclusion, with that smaller exponent, for
every fixed \(w,z\) derivative of the normalized vector.
The vector is holomorphic in \(w\); its \(z\)-dependence in
(17) is only the displayed action normalization.

For all real ordinary colors, fixed \(w\)-derivatives retain
(13) with the angular term omitted and a polynomial cost.
Indeed the vector has degree at most \(D\) in \(w\).
Apply scalar Markov to every unit dual vector and then take
the supremum. No off-grid differentiation of the incoming
physical index is involved.

In particular every coefficient-index observation of Euclidean
norm at most one is bounded by (13) and (17). This includes
the prescribed phase-corrected Fourier observations of the
low-node theorem. It does not yet include the unnormalized
row \((\psi_{\beta,j}(Z))_j\) in (9).

## 3. The actual exterior cardinal evaluation

For every \(u\) off the unit root set, the cardinal identity
gives
\[
 \boxed{\quad
 G_{\mathrm{low},N}(w,u)
    :=\sum_{b\in I_N}w_{b,N}(w)\frac{B_b}{B_b-u}
       =\frac{N E_{\mathrm{low},N}(w,u)}{1-u^N}.
 \quad}
 \tag{18}
\]
On every fixed exterior compact set \(|u|\ge1+\rho\),
the rational multiplier and each of its fixed \(u\)-derivatives
are uniformly bounded. Equations (5), (10)--(11) therefore prove
\[
 |G_{\mathrm{low},N}(-2\cos v,u)|
    \le C_{\rho,\delta,\tau}N^{C_{\rho,\delta,\tau}}
       e^{N\{M_{\mathrm{pend}}-(1-\cos v)/4000
                                      +\epsilon(\delta)+\tau\}} .
 \tag{19}
\]
The corresponding small-complex-color bound uses
\(\Re\mathcal W(w)\) in place of \(M_{\mathrm{pend}}\).
Fixed mixed \(w,u\) derivatives have the same normalized
scope by the same source bounds and Cauchy.

This exterior set is eligible for the actual leading symbol.
At the original peak, write
\[
 u_*=\frac{1-\sqrt{4/X(x_*)-3}}2 .
 \tag{20}
\]
The original branch has \(\Re u_*<1/2\), and its reciprocal
ratio satisfies \(\rho=-u^2/(1-u)\), \(|\rho(x_*)|=1\).
Thus
\[
                |u_*|^4-|u_*|^2=1-2\Re u_*>0,
                       \qquad |u_*|>1 .
 \tag{21}
\]
By continuity a fixed complex neighborhood of \(x_*\) maps
under \(u(t)\) into one of the exterior sets used in (19).
This is a statement about the analytic symbol, not an incoming
interpolation of the discrete coefficient vector.

For physical \(j/N\) in that neighborhood, the complete
low-node row packet gives
\[
 \begin{split}
 c_{1,N,j}(w)=-\frac{v_j}{\kappa^2N^2}\bigg[
       G_{\mathrm{low},N}(w,u(t_j))
        +\frac1N\sum_{b\in I_N}w_{b,N}(w)F_{B_b,1}(t_j)\\
       \hspace{38mm}
           +O\!\left(N^{-3/2}\sum_{b\in I_N}|w_{b,N}(w)|\right)
                                      \bigg].
 \end{split}
 \tag{22}
\]
Here \(F_{B,1}\) is exactly the corrected symbol in the
low-node theorem. The multiplier in its leading term is
\(F_B(t)=B/(B-u(t))\), so (18) identifies that term with the
actual exterior prefix projection.
Equation (22) is an absolute-error formula; it does not
divide by \(G_{\mathrm{low},N}\) or assert that it is nonzero.

For the asymptotically parallel coefficient vectors, the
leading incoming scalar in equation (64) of the low-node
theorem is correspondingly
\[
       \sum_{b\in I_N}w_{b,N}(w)
                \frac{B_b(1-u_*)}{B_b-u_*}
          =(1-u_*)G_{\mathrm{low},N}(w,u_*).
 \tag{23}
\]
Thus (19) controls this specified source scalar; it is not
an assumption about arbitrary scalar noncancellation.

## 4. The remaining Newton observation has an explicit cost

Let
\[
 \Lambda_{\beta,N}(Z)
        =\left(\sum_{j=0}^{D}
                     \frac{|p_j(Z)|^2}{S_j^{2+2\beta}}\right)^{1/2}.
 \tag{24}
\]
This is the exact Euclidean norm of the prescribed row in (9).
Cauchy--Schwarz gives, without suppressing any source term,
\[
 |\mathcal S_{\sigma,\beta}[E_{\mathrm{low},N}](w,Z)|
             \le\|\mathbf c_{\sigma,N}(w)\|_2
                                        \Lambda_{\beta,N}(Z).
 \tag{25}
\]
For a compact set of complex \(Z\), put
\[
 \mathcal M_\beta(Z)=\max_{0\le t\le1}
       \left\{\int_0^t\log|1-Ze^{-2\pi is}|\,ds
                                      -(1+\beta)J(t)\right\}.
 \tag{26}
\]
The zero-safe upper product estimate and the uniform factorial
bound give, for every fixed \(\tau'>0\),
\[
             \Lambda_{\beta,N}(Z)
                \le C_{\tau'}N^{C_{\tau'}}
                         e^{N\{\mathcal M_\beta(Z)+\tau'\}} .
 \tag{27}
\]
All physical termination zeros remain in (24); (27) is only
an upper envelope and does not revive them as source terms.
The potential normalized exponent obtained from this direct
norm argument is explicitly
\[
 M_{\mathrm{pend}}+A_*+\mathcal M_\beta(e^{-2\pi iz})
                              -\Re\mathcal P_\beta^+(-2,z),
 \tag{28}
\]
plus the small, already displayed tolerances.
No sign is asserted for (28).

There is also a simple source-domain lower bound on the norm
expense. The matched outgoing enclosures are contained in
\[
       \frac{11}{50}\le\Re z\le\frac{49}{100},\qquad
             -.108\le\Im z\le.068,\qquad Z=e^{-2\pi iz}.
 \tag{29}
\]
The [outgoing response theorem, equations (23)--(24)](research_mixed_next_outgoing_response_norms.md)
proves \(1/2<|Z|<2\) throughout this containing box.
For \(0\le s\le1/6\), the real angle \(\Re z+s\) lies in
\([11/50,197/300]\). On that interval
\[
 \cos(2\pi(\Re z+s))
       \le\sin(3\pi/50)<3\pi/50<\frac14 .
 \tag{30}
\]
The last inequality follows from \(\pi<22/7\).
Writing \(R=|Z|>1/2\), we obtain
\[
       |1-Ze^{-2\pi is}|^2
          =1+R^2-2R\cos(2\pi(\Re z+s))>1 .
 \tag{31}
\]
Take the single original row \(j_N=\lfloor N/6\rfloor\).
Every finite numerator factor in it has modulus greater
than one, by (31). Therefore, uniformly on the whole box,
\[
 \Lambda_{\beta,N}(Z)\ge S_{j_N}^{-1-\beta},\qquad
 \liminf_{N\to\infty}\frac1N\log\Lambda_{\beta,N}(Z)
           \ge (1+\beta)\frac{c_{\mathrm b}}2
                           >\frac{4(1+\beta)}{25}.
 \tag{32}
\]
The last strict inequality is the already proved
\(c_{\mathrm b}>8/25\) in
[the cap-seed theorem, equation (16)](research_positive_three_crossing_cap_seed.md).
No new action value is needed.

Already at \(\beta=0\), this generic row expense exceeds
the certified reserve \(21/500\) in (16) by more than
\(59/500\). Thus a uniform Euclidean row bound with cost
less than \(21/500\) cannot hold on the actual output box.
This comparison concerns the available bounds, not the
sign of the true deficit (28) or the value of the actual
signed contraction.

A completion would require a source-sensitive estimate of
the observation in (9), exploiting its phase or an exact
identity beyond the unrestricted norm (24). The exterior
bound (19), the small full-vector rate (13), and the common
Fourier packet do not supply that estimate by themselves.
Both original complete sectors, all ordinary boundary jets,
and both level parities remain in these conclusions.
