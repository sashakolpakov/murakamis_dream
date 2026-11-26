# The central total-index packet at every finite height

Research deduction, 7 November 2026. The symmetric central finite
source has its unique inner maximum at the midpoint for every finite
total height and every total real part from \(1/2\) to the support
edge. The criterion is an elementary strict bound on the external
radius and angle, satisfied by the original \(x_0\). Every factorial
argument stays in the original regular strip, including on lower
total contours.

The resulting complete central-source packet retains both parity
interpolants and all normalized mixed derivatives. Its identification
with the original physical central rows is exact. Payment of the
discarded physical rows at the final outer action remains a separate
estimate; no full outer signed sum is evaluated here.

## 1. Exact source and the regular all-height domain

Use the original row
\[
\begin{split}
 T_N(a;c,x)={}&e^{2\pi iNa(c-a)}
 \Pi_N(c)\Pi_N(a+x)\Pi_N(c-a+x)\\
 &\qquad\cdot E_N(a)^2E_N(c-a)^2E_N(x)^2
\end{split}
 \tag{1}
\]
and the fixed finite sources
\[
 \mathcal H_{\sigma,N}(c,x)
  =\sum_{\substack{d\in\mathbb Z+\sigma\\|d|\le N/5}}
                         T_N(c/2+d/N;c,x),
                  \qquad \sigma\in\{0,1/2\}.
 \tag{2}
\]
These are exactly the central sources of
[the earlier central theorem](research_mixed_two_adjacent_central_total_index_packet.md),
now on a larger proved domain.

They are holomorphic on
\[
 \mathcal V=\left\{(c,x):
       \frac25<\Re c<1,\quad \frac16<\Re x<\frac14\right\},
 \tag{3}
\]
with arbitrary finite imaginary parts. Indeed for \(|t|\le1/5\),
both own arguments \(c/2\pm t\) have real parts in \((0,7/10)\).
Their shifts by \(x\) have real parts strictly between zero and
\(19/20\). The remaining arguments \(c,x\) are regular.
Every factor in (1) is therefore in its original regular strip;
there is no numerator pole or reciprocal zero in this chart.

Define the external domain
\[
 \mathcal X=
 \left\{x:\frac16<\Re x<\frac14,\quad
       1<S:=e^{2\pi\Im x},\quad S\cos(2\pi\Re x)<1\right\}.
 \tag{4}
\]
This is an open neighborhood condition at \(x_0\):
the proved bounds \(1<S<33/20\) and
\(\cos(2\pi\Re x_0)<41/100\) imply the last strict inequality.
All parameter estimates below are uniform on fixed compact sets;
no uniformity as an imaginary part tends to infinity is assumed.

## 2. A stronger numerator-to-denominator comparison

Put
\[
 \begin{gathered}
 c=C+iH,\quad \frac12\le C<1,\quad H\in\mathbb R,\quad
 x=\xi+i\upsilon\in\mathcal X,\\
 \theta=\pi C,\quad \vartheta=2\pi\xi,\quad
 R=e^{\pi H}>0,\quad S=e^{2\pi\upsilon}>1.
 \end{gathered}
 \tag{5}
\]
For \(a=c/2+t\), let \(\delta=2\pi t\) and define
\[
 \begin{split}
 D_\pm&=|1-R e^{-i(\theta\pm\delta)}|^2,\\
 N_\pm&=|1-RS e^{-i(\theta+\vartheta\pm\delta)}|^2.
 \end{split}
 \tag{6}
\]
All these factors are nonzero for \(|t|\le1/5\), by the
regular real arguments from section 1.

For the original phase
\[
 F_c(a;x)=g(c)+g(a+x)+g(c-a+x)
           -2g(a)-2g(c-a)-2g(x)+2\pi ia(c-a),
 \tag{7}
\]
the exact real derivative is
\[
 \frac{d}{dt}\Re F_c(c/2+t;x)
       =\frac12\log\frac{N_+}{N_-}
                          -\log\frac{D_+}{D_-}.
 \tag{8}
\]
The chirp derivative is purely imaginary. For \(0<t\le1/5\),
\[
          D_+-D_-=4R\sin\theta\sin\delta>0,
          \qquad z:=\cos\delta\ge\cos(2\pi/5)>0.
 \tag{9}
\]

If \(\theta+\vartheta\ge\pi\), then
\(\theta+\vartheta<3\pi/2\), so
\(N_+-N_-=4RS\sin(\theta+\vartheta)\sin\delta\le0\).
Equation (8) is strictly negative.

For the remaining range
\(\pi/2\le\theta\le\pi-\vartheta\), direct expansion gives
\[
                 N_+D_--N_-D_+
                         =-4R\sin\delta\,\mathcal E,
 \tag{10}
\]
where
\[
\begin{split}
 \mathcal E={}&
 \sin\theta\{(1-S\cos\vartheta)
                       +R^2S(S-\cos\vartheta)\}\\
 &-S\cos\theta\sin\vartheta(1+R^2)
                       +2RS\sin\vartheta\,z.
\end{split}
 \tag{11}
\]
Every term in (11) is nonnegative and its first line is
strictly positive. Indeed \(\cos\theta\le0\),
\(S\cos\vartheta<1\), \(S>1>\cos\vartheta\), and \(z>0\).
This works for every \(R>0\), without a sign restriction
on the total height. Thus
\[
        \frac{N_+}{N_-}<\frac{D_+}{D_-},
 \qquad
 \frac{d}{dt}\Re F_c(c/2+t;x)
             <-\frac12\log\frac{D_+}{D_-}<0.
 \tag{12}
\]
The automatic case above satisfies the same weaker final
upper bound. Symmetry gives the positive derivative on
the left half.

**Lemma 1.** On the full central interval \(|t|\le1/5\),
the unique real maximum of (7) is at \(t=0\), for every
parameter in (5). Its actual inner derivative is zero
by symmetry. Its inner Hessian
\[
 \mathcal K(c,x)
     =2\pi\cot\pi(c/2+x)-4\pi\cot(\pi c/2)-2\pi i
 \tag{13}
\]
obeys
\[
        \Re\mathcal K(c,x)
          \le-2\pi\Re\cot(\pi c/2)<0.
 \tag{14}
\]

For the explicit limiting bound, as \(t\to0^+\),
\[
 \frac1t\log\frac{D_+}{D_-}
       \longrightarrow
       \frac{8\pi R\sin\theta}{1+R^2-2R\cos\theta}
       =4\pi\Re\cot(\pi c/2).
 \tag{15}
\]
Equations (12) and (15) imply (14). The last strict sign
uses \(0<C/2<1/2\). Compact parameter sets therefore
have a uniform negative Hessian floor and a uniform
strict phase loss outside any fixed neighborhood of
the center.

## 3. The complete finite Gaussian and mixed derivatives

Set
\[
\begin{split}
 \Phi(c,x)&=g(c)+2g(c/2+x)-4g(c/2)-2g(x)
                                      +\frac{\pi i}{2}c^2,\\
 \mathcal A(c,x)&=
 \frac{\sqrt{2\pi}\,\mathfrak a(c)\mathfrak a(c/2+x)^2}
 {\mathfrak a(x)^2\mathfrak a(c/2)^4\sqrt{-\mathcal K(c,x)}}.
\end{split}
 \tag{16}
\]
The square root has positive real part. The original
regular symbol \(\mathfrak a\) is nonzero, and (14)
makes this the nonzero, consistently continued Gaussian
coefficient on the stated parameter family.

**Theorem 2.** For every compact set
\[
       K\subset\{(c,x):1/2\le\Re c<1,\quad x\in\mathcal X\},
 \tag{17}
\]
with arbitrary finite total heights, there is an open
neighborhood \(U_K\Subset\mathcal V\) such that
\[
 \boxed{\quad
 \mathcal H_{\sigma,N}(c,x)
       =N^{-1}\mathcal A(c,x)e^{N\Phi(c,x)}
                                      (1+O(N^{-1})),
                  \qquad \sigma\in\{0,1/2\}.
 \quad}
 \tag{18}
\]
The estimate is uniform on smaller compact subsets
of \(U_K\), for both level parities. Every fixed mixed
\(c,x\) derivative of its normalized error is
\(O(N^{-1})\) there.

*Proof.* The exact finite row has its original
\(N^{-3/2}b_c(a;x)e^{NF_c(a;x)}(1+O(N^{-1}))\)
packet uniformly on the entire central interval,
since all arguments are regular. Lemma 1 gives a
uniform quadratic loss near the center and a fixed
strict loss on the rest of that interval. These
bounds persist on a small open neighborhood of \(K\),
including just below \(\Re c=1/2\).

Both phase and symbol are exactly even in
\(t=a-c/2\). Writing \(t=d/N\), the central phase is
\[
          \Phi(c,x)+\mathcal K(c,x)d^2/(2N^2)
                                     +O(d^4/N^4).
 \tag{19}
\]
For either centered lattice,
\[
 \sum_{d\in\mathbb Z+\sigma}
      e^{\mathcal K d^2/(2N)}
    =\frac{\sqrt{2\pi N}}{\sqrt{-\mathcal K}}
                                     (1+O(e^{-\gamma N})).
 \tag{20}
\]
Uniformity follows from the positive real parts of
\(-\mathcal K\) and its reciprocal on compact sets.
The even Taylor expansion and Gaussian moments give
relative \(O(N^{-1})\) from the quartic phase,
quadratic symbol, and original row errors. Lemma 1
pays all other terms of the actual finite source.
Multiplying \(N^{-3/2}\) by the \(\sqrt N\) Gaussian
density gives precisely (18).

The finite source, phase, and nonzero coefficient
are holomorphic on \(U_K\). Nested Cauchy estimates
give the normalized mixed derivatives. No imaginary
height restriction is used beyond the compactness
needed for uniform constants. \(\square\)

At a physical \(c=m/N\in[1/2,1)\), with
\(\sigma\equiv m/2\pmod1\), the exact identity remains
\[
 \mathcal H_{\sigma,N}(m/N,x)
  =\sum_{\substack{0\le j\le m\\|j-m/2|\le N/5}}
        \frac{r^{-j(m-j)}P_m p_j(X)p_{m-j}(X)}
                            {P_j^2P_{m-j}^2}.
 \tag{21}
\]
All its selected rows are legal because \(m/2\ge N/4>N/5\).
The remaining physical rows are precisely the omitted
terms of the original finite sum, with all phases intact.

Equation (18) is a complete all-height packet for
that exact central source. It does not by itself pay
the omitted physical rows below the final outer
critical action, identify the two off-grid parity
sources, or remove any outer parity alias. It also
does not assert a uniform estimate when a contour
height tends to infinity at fixed level. Those
finite-level tail and outer-contour steps retain
their original source factors and separate proofs.

