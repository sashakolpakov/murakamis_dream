# An exact finite formula for the factorized contour

Research deduction, 7 November 2026. The factorized homogeneous
representative has a canonical initial value, fixed by the original
factorial normalization rather than by physical interpolation alone.
At every physical incoming index its complete free-output function
then reduces to one explicit finite sum of shifted reciprocal
factorials. The proof retains the true last summation row: its forcing
cancels the forcing of the contour moments exactly.

This is a complete finite-source identity for every \(N\ge2\), including
both parities. It supplies no large-level dominance or noncancellation
claim for that new finite sum. Ordinary normal adapters and outgoing
cardinal reconstruction remain necessary; raw derivatives of this
representative are not substituted for the original normals.
No numerical evaluation is used.

## 1. Original source, period, and the representative

Put
\[
 r=e^{-2\pi i/N},\quad \delta=1/N,\quad D=N-1,\quad
 P_j=(r;r)_j,\quad p_j(U)=(rU;r)_j,\quad W=e^{-2\pi iy}.
 \tag{1}
\]
Use the same canonical \(\Pi_N\) and its reciprocal \(E_N\) as in
[the full-node extension](research_mixed_three_homogeneous_period_full_node_composition.md).
They obey the original recurrence, and \(E_N\) is holomorphic on
\(\Re z<1\). It is nonzero on
\[
                  \mathcal S_N=\{-1/(2N)<\Re z<1\}.
 \tag{2}
\]
The complete homogeneous remainder is \(H_N\); the second period is
\(Z_N=\mathcal I_{2,N}\), with no outside factor \(N\):
\[
\begin{split}
 T_N(s;a,y)&=e^{2\pi iNas}\Pi_N(s+a)\Pi_N(s+y)
                         E_N(a)E_N(y)E_N(s)^2,\\
 Z_N(a,y)&=\int_{\alpha_N-i\infty}^{\alpha_N+i\infty}
                      k_{2,N}(s)T_N(s;a,y)\,ds,\\
 \alpha_N&=-1/(2N),\qquad
 k_{2,N}(s)=\frac{t}{(1-t)^2},\qquad t=e^{-2\pi iNs}.
\end{split}
 \tag{3}
\]
Every vertical line is oriented upward. These are the same periods
and contours as in
[the homogeneous-period theorem](research_mixed_three_fourier_conditional_homogeneous_period.md);
their fixed-level domain includes \(\mathcal S_N^2\).

For \(X=e^{-2\pi ia}\), set
\[
 a_0=X^{-N}-1,\quad b_0=W^N-1,\quad
 c_+=a_0-b_0-\tfrac12a_0b_0,\qquad
                  J_N=H_N-Nc_+Z_N.
 \tag{4}
\]
At a physical incoming value \(a=b/N\), \(0\le b<N\), the exact
particular forcing vanishes, so
\[
 \boxed{\quad
 J_N(b/N,y)=C_{0,N}(r^b,W)+Nb_0 Z_N(b/N,y).
 \quad}
 \tag{5}
\]
The free output \(y\) is not specialized in (5).

**Theorem 1.** For every \(N\ge2\), \(0\le b<N\), and \(y\in\mathcal S_N\),
\[
\boxed{\begin{split}
 J_N(b/N,y)
  ={}&N(-1)^b\sum_{k=0}^{b}
   \frac{r^{\{(b-k)(b-k+1)+k(k+1)\}/2}}
        {P_{b-k}P_k^2}\,E_N(y-k/N)\\
  ={}&N E_N(y)L_{b,N}(W),
\end{split}}
 \tag{6}
\]
where the explicit polynomial is
\[
 L_{b,N}(W)=(-1)^b\sum_{k=0}^{b}
 \frac{r^{\{(b-k)(b-k+1)+k(k+1)\}/2}
                    (W;r^{-1})_k}{P_{b-k}P_k^2}.
 \tag{7}
\]
Its degree is exactly \(b\); its leading coefficient is \(r^b/P_b^2\).
In particular
\[
 J_N(0,y)=N E_N(y),\qquad
 J_N(1/N,y)
   =-\frac{Nr(2-r-W)}{(1-r)^2}E_N(y).
 \tag{8}
\]
Every denominator displayed in (6)--(8) is nonzero. The arguments
\(y-k/N\) can leave the original zero-free strip; the global
reciprocal, including all its zeros, is retained.

## 2. Contour and finite moments have opposite exact forcings

Fix the incoming value zero and abbreviate
\[
 T_0(s;y)=\Pi_N(s+y)E_N(y)E_N(s),\qquad U=e^{-2\pi is}.
 \tag{9}
\]
For \(0\le k<N\), define
\[
 I_{-k}(y)=\int_{\alpha_N-i\infty}^{\alpha_N+i\infty}
                       U^{-k}k_{2,N}(s)T_0(s;y)\,ds,
 \quad
 K_{-k}(y)=\sum_{j=0}^{N-1}r^{-kj}\frac{p_j(W)}{P_j}.
 \tag{10}
\]
The integrals converge absolutely on \(\mathcal S_N\).
At the lower end their decay rate is \(2\pi(N-k)\);
at the upper end it is \(2\pi\{N(1-\Re y)+k\}\).
The additional moments \(I_1,K_1\) used below are defined by
replacing \(U^{-k}\) with \(U\); \(I_1\) initially requires
\(\Re y<1-1/N\).

The original row recurrence is the undivided equality
\[
          (1-rU)T_0(s+\delta;y)=(1-rWU)T_0(s;y).
 \tag{11}
\]
Multiply it by \(U^{-k}k_{2,N}(s)\) and shift the left integral
by \(1/N\). After the substitution, its integrand is
\[
                 r^k U^{-k}(1-U)k_{2,N}(s)T_0(s;y).
 \]
Between the two upward half-grid lines the only pole is at zero.
Its residue, before the factor \(r^k\), is
\[
 \operatorname*{Res}_{s=0}
       U^{-k}(1-U)k_{2,N}(s)T_0(s;y)
                         =\frac1{2\pi iN^2}.
 \tag{12}
\]
Here \(T_0(0;y)=1\); the reciprocal zeros and numerator factors
are the original ones. The upward right line equals the upward
left line plus \(2\pi i\) times this residue. The horizontal
connectors vanish: for \(1\le k<N\) their lower and upper
decay rates are \(2\pi(N-k)\) and
\(2\pi\{N(1-\Re y)+k-1\}\), respectively. For \(k=0\) the
same argument holds on \(\Re y<1-\delta\).
Consequently
\[
 \boxed{\quad
 (1-r^k)I_{-k}=(rW-r^k)I_{1-k}+\frac{r^k}{N^2}
                      \qquad(1\le k<N).
 \quad}
 \tag{13}
\]
The \(k=0\) case gives separately
\[
                         I_1=\frac1{N^2(1-rW)}.
 \tag{14}
\]
All statements are holomorphic on their stated domains.

The finite physical rows \(t_j=p_j(W)/P_j\) obey
\[
              (1-r^{j+1})t_{j+1}
                         =(1-r^{j+1}W)t_j\quad(0\le j<D).
 \tag{15}
\]
Their true final value is
\[
                (1-W)t_D=\frac{1-W^N}{N}=-\frac{b_0}{N}.
 \tag{16}
\]
Multiply (15) by \(r^{-kj}\), sum only over \(0\le j<D\),
and change index on the left. The omitted lower term vanishes
because \(1-r^0=0\), while the upper term is exactly (16).
This gives
\[
 \boxed{\quad
 (1-r^k)K_{-k}
       =(rW-r^k)K_{1-k}-\frac{r^kb_0}{N}
                         \qquad(1\le k<N),
 \quad}
 \tag{17}
\]
and its \(k=0\) counterpart is
\[
                         K_1=-\frac{b_0}{N(1-rW)}.
 \tag{18}
\]
No top row is deleted or replaced by periodicity in this summation.

It follows that the exact combined moments
\[
                         Q_{-k}=K_{-k}+Nb_0 I_{-k}
 \]
have no forcing:
\[
 Q_{-k}
   =\frac{rW-r^k}{1-r^k}Q_{1-k}
   =\frac{(-1)^kr^{k(k+1)/2}(W;r^{-1})_k}{P_k}\,Q_0 .
 \tag{19}
\]

## 3. The canonical initial value, including the periodic factor

The outgoing recurrence gives
\[
 (1-rW)I_0(y+\delta)-I_0(y)=-rW I_1(y),\qquad
 (1-rW)K_0(y+\delta)-K_0(y)=-rW K_1(y).
 \tag{20}
\]
Equations (14) and (18) therefore imply exactly
\[
       (1-rW)Q_0(y+\delta)=Q_0(y).
 \tag{21}
\]
The factor \(b_0\) is unchanged by this shift.
For reference, \(K_0=N d_N(W)\): at each physical \(W=r^c\)
its value is \(N/P_c\), by the constant mode of \(p_c(U)/P_c\);
both sides are polynomials in \(W\) of degree less than \(N\).
Thus (21) retains precisely the original Fourier-polynomial
forcing of
[weight continuation](research_mixed_fourier_weight_continuation.md).

Since \(E_N(y+\delta)=E_N(y)/(1-rW)\), the holomorphic quotient
\[
                         V_N(y)=\frac{Q_0(y)}{N E_N(y)}
 \tag{22}
\]
is \(1/N\)-periodic on overlaps in \(\mathcal S_N\).
Physical agreement alone would not fix this periodic factor.
We fix it by the original fixed-level contour growth.

Work at fixed \(N\ge2\), on the fundamental real strip
\[
             -\frac1{4N}\le \xi=\Re y\le\frac3{4N},
       \qquad B=N(2\xi-1)<0,\quad \upsilon=\Im y.
 \tag{23}
\]
All moving numerator arguments on \(\Re s=\alpha_N\) have
real part at least \(-3/(4N)>-1/N\), and all parameter
arguments have real parts in \((-1/N,1)\).
The exact fixed-\(N\) upper/lower factorial estimates used in
Section 5 of
[the homogeneous-period theorem](research_mixed_three_fourier_conditional_homogeneous_period.md)
therefore apply also on (23). At \(a=0\) their upper exponent
for the absolute \(I_0\) integrand, divided by \(\pi\), is
\[
 -Nv_+ +B(v+\upsilon)_+-(B+1)\upsilon_+
                                      +2N\min(v,0).
 \tag{24}
\]
The constants may depend on \(N\); this is not a large-level
estimate near a moving endpoint.

If \(\upsilon\ge0\), use
\(B(v+\upsilon)_+\le B(v+\upsilon)\).
The resulting majorant has constant \(-\upsilon\), lower slope
\(B+2N=N(1+2\xi)>0\), and upper slope
\(B-N=2N(\xi-1)<0\).
If \(\upsilon\le0\), drop \(B(v+\upsilon)_+\le0\).
This leaves an integrable majorant independent of \(\upsilon\).
Hence uniformly on the real strip (23),
\[
 I_0(y)=
 \begin{cases}
 O_N(e^{-\pi\upsilon}),&\upsilon\to+\infty,\\
 O_N(1),&\upsilon\to-\infty.
 \end{cases}
 \tag{25}
\]
The degree bound for \(K_0\) and the factor \(b_0=W^N-1\) give
\[
 Q_0(y)=
 \begin{cases}
 O_N(e^{\pi(2N-1)\upsilon}),&\upsilon\to+\infty,\\
 O_N(1),&\upsilon\to-\infty.
 \end{cases}
 \tag{26}
\]
The same exact factorial formulas, with their nonzero constants,
give
\[
 |E_N(y)|\asymp_N e^{-\pi(B+1)\upsilon}
       \quad(\upsilon\to+\infty),\qquad
 |E_N(y)|\asymp_N1\quad(\upsilon\to-\infty).
 \]
Thus
\[
 V_N(y)=
 \begin{cases}
 O_N(e^{\pi(N+3/2)\upsilon}),&\upsilon\to+\infty,\\
 O_N(1),&\upsilon\to-\infty.
 \end{cases}
 \tag{27}
\]
Because \(N+3/2<2N\) for every \(N\ge2\), these rates allow
no nonconstant Laurent mode of the holomorphic periodic function,
viewed on the cylinder with coordinate \(W^N\).
Explicitly, the first bound grows slower than \(|W^N|\) at infinity
and the second is bounded at zero; Laurent coefficient estimates
kill every nonconstant mode. Periodicity on overlaps of (2)
supplies the whole cylinder; no unproved continuation of a growth
bound is used.

Finally \(Q_0(0)=K_0(0)=N\), because \(b_0(0)=0\), and \(E_N(0)=1\).
It follows that \(V_N\equiv1\), proving
\[
                              Q_0(y)=N E_N(y).
 \tag{28}
\]

## 4. Every physical incoming row and the remaining analytic task

For \(a=b/N\), the exact original recurrence, throughout the
midpoint contour, gives
\[
       T_N(s;b/N,y)=\frac{U^{-b}p_b(U)}{P_b}\,T_0(s;y).
 \tag{29}
\]
The same equality holds at every physical summation node.
All its Laurent powers lie between \(-b\) and zero, and their
contour moments converge because \(b<N\). The finite binomial formula is
\[
 \frac{U^{-b}p_b(U)}{P_b}
   =\sum_{j=0}^b
        \frac{(-1)^j r^{j(j+1)/2}}{P_jP_{b-j}}\,U^{j-b}.
 \tag{30}
\]
Apply (19) to each combined moment in (30), then use (28).
After the reindexing \(k=b-j\), this is (7).
The undivided reciprocal recurrence
\[
                  E_N(y-k/N)=(W;r^{-1})_k E_N(y)
 \tag{31}
\]
gives (6). It remains valid across every reciprocal zero.
The leading term in (7) comes only from \(k=b\) and is
\(r^bW^b/P_b^2\), which also proves the stated degree.
This completes the theorem.

The exact original source is consequently
\[
 \boxed{\quad
 C_{0,N}(r^b,W)
    =N E_N(y)L_{b,N}(W)-N(W^N-1)\mathcal I_{2,N}(b/N,y).
 \quad}
 \tag{32}
\]
For \(b/N\) in the actual type-three real interval and \(y\) near
\(x_0\), the second term has the already proved complete
[second-period packet](research_mixed_three_fourier_conditional_second_period_packet.md).
Its explicit multiplier \(W^N-1\) must still be included in every
action comparison. The first term is the entire new finite source
(6), not an inferred single saddle or a quotient by that multiplier.
Its large-level noncancellation remains to be proved.

At a physical output \(y=c/N\), (32) gives exactly the original
full node matrix. With a free output, the correction in (32) remains.
For example at a physical pair,
\[
 \partial_y[J_N(b/N,y)-C_{0,N}(r^b,W)]_{y=c/N}
                     =-2\pi iN^2 Z_N(b/N,c/N).
 \tag{33}
\]
Thus physical equality is not equality of raw analytic derivatives.
Substitution into actual adjacent finite blocks uses the full
node basis and the unchanged ordinary Hermite adapters from
[full-node composition](research_mixed_three_homogeneous_period_full_node_composition.md).
Likewise an off-grid contour use of (6) in the incoming index needs
an explicitly chosen interpolation and all its Fourier/residue
aliases. Neither is supplied silently by the finite identity.
