# Complementary Gauss boundary branches and the retained vacuum interference

Private written proof, 19 November 2026.

The actual opposite-source sewing needs complementary total occupations.
Conjugating its high-degree Gauss factor by the exact turnover/degree
coupon gives a low-degree operator with reversed normal ordering.
Its first column reduces, at every fixed width, to an effective
highest-weight factor and one physical head. In two tail heads its
vacuum is an explicit difference of two marked terms. The vacuum
can vanish at infinitely many levels even in a strict angle chamber.
It is therefore not used as a normalizing unit.

The result below is a controlled two-branch boundary in two tails
and a selected complementary boundary sector at every fixed width,
with every finite cap retained.
Neither the vacuum nor the difference of the two branches is
assumed nonzero. In two tails each branch is selected on an
explicit nonempty activity sector. At general fixed width a
separated positive-rate branch is selected; every competing
branch remains on the equal-rate set.
This is a first-column theorem, not an estimate for the entire
complementary coherent kernel.
The complete direct sources are G and R, listed at the end.

## 1. The complementary factor is an actual conjugated operator

Set
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1},\quad f_n=(Q;Q)_n,\quad H_d=(-1)^dN.
 \tag{1}
\]
The meridian is fixed at one throughout this proof.
Let \(r\ge2\) be the number of tails and let \(\mathsf n\)
be their total integer occupation. R proves the exact coupon
\[
 L=D_{\rm top}\mathscr C_r=\kappa^r\mathsf W_r q^{\mathsf n},
 \qquad
 \mathsf W_r|\mathbf a\rangle
    =|d-a_r,\ldots,d-a_1\rangle .
 \tag{2}
\]
It sends \(U_T\) to \(U_{rd-T}\). Its coherent kernel and all
binomial caps are the literal product in R, not an interpolated
degree transformation.

On one head the unsigned complement sends \(E\) to \(-F\),
\(F\) to \(-E\), and \(K\) to \(K^{-1}\). Tensor reversal restores
the original coproduct order. Since \(q^{\mathsf n}E q^{-\mathsf n}
=q^{-1}E\), direct conjugation gives
\[
 L^{-1}EL=-q^{-1}F,\qquad L^{-1}FL=-qE,\qquad
 L^{-1}KL=K^{-1}.
 \tag{3}
\]
The commutator
\([E,F]=(q-q^{-1})(K-K^{-1})\) then verifies
\(L^{-1}\Omega L=\Omega\), where
\(\Omega=FE+qK+q^{-1}K^{-1}\).
Consequently the high-degree factor has the exact low-degree form
\[
 \boxed{\quad
 A^\vee_T=L^{-1}A_N|_{U_{rd-T}}L
     =A_N(K^{-1},\Omega)|_{U_T}
     =H_d\sum_{n=0}^d
       \frac{Q^{n(n-1)/2}x^{-n}}{f_n^2}
                     E^nF^nK^{-d+n}\Big|_{U_T}.
 \quad} \tag{4}
\]
The two factors \(E^n,F^n\) are in the displayed order. Equation
(4) follows from G's literal polynomial, using
\(H_n(1)=Q^{-n(n+1)/2}f_n\). It preserves every upper-head cap.

This complementary factor is necessary in the paired source.
Each opposite kernel reverses integer degree, while the intervening
braid and Cartan rows preserve it. The two Gauss degrees in a closed
sector are therefore \(T\) and \(rd-T\). Their parameters obey
\[
 \frac{T+1}{N}+\frac{rd-T+1}{N}
                    =r-\frac{r-2}{N}\ge2.                 \tag{5}
\]
The two existing strict upper strips \(1/2<\Re\sigma<1\) cannot
contain both factors. This is an exact grading constraint, including
the original meridian jets, not a claim that any geometric coefficient
vanishes. Equation (4) specifies the required complementary operator
instead of trying to deform both factors into the same strip.

## 2. All-width first-column reduction and its entire finite sum

Fix \(T=d-H\), \(0\le T\le d\). Separate the first \(r-1\) heads,
denoted \(A\), from the last head. Their vacuum is \(|0_A\rangle\).
Put
\[
 k_A=x^{r-1},\qquad
 v_a=\frac{F_A^a}{f_a}|0_A\rangle,\quad 0\le a<N,\qquad
 M_A=-qk_A=(-1)^r q^{2-r}.
\]
These vectors are nonzero: the component putting all \(a\) raisings
on a fixed first head is nonzero for \(a<N\).
The commutator and the highest-weight equation \(E_A|0_A\rangle=0\)
give, by induction,
\[
 K_Av_a=k_AQ^{-a}v_a,\quad
 F_Av_a=(1-Q^{a+1})v_{a+1},\quad
 E_Av_a=(M_AQ^{-a}-M_A^{-1})v_{a-1}.             \tag{6}
\]
The nonexistent bottom and top arrows are zero. Thus the entire
first column of (4) lies in the actual subspace spanned by
\(v_a\otimes w_{T-a}\). No spectral-channel sum or scalar Casimir
specialization is used.

Let \(D_a\) denote its coefficient:
\[
 A^\vee(v_0\otimes w_T)
       =\sum_{a=0}^T D_a\,v_a\otimes w_{T-a},\qquad
 K=k_AxQ^{-T}.                                  \tag{7}
\]
Expansion of the two ordered coproducts gives the full finite formula
\[
 \boxed{\begin{split}
 D_a={H_dK^{-d}k_A^a\over f_Tf_{T-a}}
 \sum_{k=0}^H
 {Q^{(k+a)(a-1-2T)}f_{T+k}^2\over f_kf_{k+a}}
 \sum_{b=0}^{d-a-k}
 { (Q^{a+r-1};Q)_b\over f_b}\,Q^{-(2T+r)b}.
 \end{split}}                                                   \tag{8}
\]
An empty inner range is interpreted as zero.

Here is the complete cap and phase calculation. Write
\(n=k+a+b\). In \(F^n\), choose \(a+b\) raisings on factor \(A\)
and \(k\) on the last head. Its coefficient is
\[
 {n\brack a+b}_Q\,k_A^{-k}f_{a+b}
                                  {f_{T+k}\over f_T}.
\]
The intermediate state is \(v_{a+b}\otimes w_{T+k}\).
The last upper cap is exactly \(k\le H\); the total expansion
has \(n\le d\), hence \(b\le d-a-k\).
Only the term \(E_{\rm last}^{k+a}(E_AK_{\rm last})^b\)
returns to \(v_a\otimes w_{T-a}\). Its coefficient is
\[
 {n\brack b}_Q x^b
 Q^{-n(T+k)+(k+a)(k+a-1)/2}
 {f_{T+k}\over f_{T-a}}\,
 M_A^b Q^{-[(a+b)(a+b+1)-a(a+1)]/2}
                   (M_A^{-2}Q^{a+1};Q)_b .
\]
Multiplication by the \(n\)-th coefficient in (4) cancels the
two \(f_n\)'s. Use \(xM_A=k_A\),
\(M_A^{-2}Q^{a+1}=k_A^{-2}Q^a=Q^{a+r-1}\), and
\(k_A^2=Q^{-(r-1)}\). The remaining exponent is precisely
\((k+a)(a-1-2T)-(2T+r)b\), proving (8).
This also proves the invariant-subspace assertion in (7) directly.

The lift from (7) back to all physical first-head occupations is
the finite vector \(F_A^a|0_A\rangle/f_a\), with its original
coherent evaluation. It has not been changed to a freely chosen
symmetric tensor or a single complex occupation.

## 3. The two-tail vacuum and exact cancellation levels

Now set \(r=2\), so \(k_A=x\) and \(K=Q^{-T-1}\), and assume
\[
                         1\le H<N/2.                            \tag{9}
\]
At \(a=0\) the numerator \((Q;Q)_b\) in (8) cancels \(f_b\).
Thus the actual vacuum is
\[
 {D_0\over H_dK^{-d}}
 =\sum_{k=0}^H Q^{-k(2T+1)}
      \left({f_{T+k}\over f_Tf_k}\right)^2
                          \sum_{b=0}^{d-k}Q^{-(2T+2)b}.          \tag{10}
\]
This is a double finite sum of actual returning matrix paths.

Since \(T=d-H\), the inner ratio is \(Q^{2H}\ne1\).
Its complete orbit is zero. Therefore
\[
 \sum_{b=0}^{d-k}Q^{2Hb}
      =-Q^{-2H}\sum_{j=0}^{k-1}Q^{-2Hj},                         \tag{11}
\]
including \(k=0\), when both sides vanish.
The exact root reflection gives
\[
 Q^{-k(2T+1)}
       \left({f_{T+k}\over f_Tf_k}\right)^2
            ={Q^{k^2}f_H^2\over f_k^2f_{H-k}^2}.                \tag{12}
\]
There is no denominator singularity in (9).

For completeness put \(w_k=Q^{k^2}{H\brack k}_Q^2\).
The finite Gaussian binomial identity gives
\[
 \sum_{k=0}^H w_k={2H\brack H}_Q,\qquad
 w_{H-k}=Q^{H^2-2Hk}w_k.                                        \tag{13}
\]
The first equation follows by extracting \(t^H\) from
\((-t;Q)_H(-tQ^H;Q)_H=(-t;Q)_{2H}\).
Use the finite geometric sum in (11) and the second equation in
(13) to obtain
\[
 \sum_k w_k\sum_{j<k}Q^{-2Hj}
       ={1-Q^{-H^2}\over1-Q^{-2H}}{2H\brack H}_Q.
\]
Equations (10)--(13) now prove
\[
 \boxed{\quad
 D_0=H_dK^{-d}(1-Q^{-H^2})\,{f_{2H-1}\over f_H^2}.
 \quad}                                                        \tag{14}
\]
All factors except the displayed difference are nonzero.

In particular fix an integer \(b\ge3\), let \(N\) run through
multiples of \(b^2\), and put \(H=N/b\), \(T=d-H\).
Then \(H/N=1/b\) and \((T+1)/N=1-1/b\) remain in strict compact
chambers, but \(Q^{-H^2}=1\). The literal vacuum (14) is zero
at every such level. A boundary theorem cannot normalize by it
or infer a uniform zero-free disk from strict angles.

This is not a zero theorem for a knot source. The other first-column
entries and all exterior operators remain. The two terms in (14)
have the same root-modulus prefactor; their difference retains an
extensive oscillatory character. Writing
\(f_{2H-1}=f_{2H}/(1-Q^{2H})\) exhibits the usual strict triangle
\((H/N,H/N,1-2H/N)\) in the factorial ratio, but this positivity
does not discard \(1-Q^{-H^2}\).

## 4. A finite recurrence through the entire physical cap

First allow every fixed width. Put \(p=r-2\), assume \(H\ge p+1\)
and \(2H<N\), and define
\[
 C=Q^H,\quad \chi=Q^{-H^2},\quad
 Z_a={D_a\over H_dK^{-d}k_A^a},\quad
 I_{a,k}=\sum_{b=0}^{d-a-k}{a+p+b\brack a+p}_Q
                                      (C^2Q^{-p})^b,
\]
\[
 w_{a,k}={Q^{k(k+a)}\over f_kf_{k+a}f_{H-k}^2},\qquad
 Y_a=\sum_{k=0}^H w_{a,k}I_{a,k},\qquad
 P_a=(-1)^a C^aQ^{a(a+1)/2}f_Hf_{H+a}.
 \tag{15}
\]
Root reflection in (8) gives \(Z_a=P_aY_a\).
When an upper Gaussian index exceeds \(N\), its meaning is its
finite product with the displayed bottom index below \(N\);
no quotient of two vanishing root factorials is used.
All these are finite quantities. In particular a geometric
denominator \(1-Q^{2H+\ell-p}\) is never introduced.

For every \(1\le a\le T\), the exact recurrence is
\[
\boxed{\begin{split}
 (1-CQ^a)Z_a+CQ^aZ_{a-1}
 ={}&(-1)^{p+1}\chi Q^{p(p+1)/2}(Q^{p+1}/C)^a\\
 &\quad{}\times {f_{H+a-1}f_{2H-p-1}\over
                  f_{a+p}f_Hf_{H-p-1}^2}.
\end{split}}                                                   \tag{16}
\]
The top coefficient \(a=T\) is included. The initial value \(Z_0\)
is always the actual finite sum (8). If \(F_a\) denotes the
displayed right side and \(\mathcal Z=\sum_{a=0}^TZ_a\rho^a\),
the entire polynomial row is
\[
 \mathcal Z-C(1-Q\rho)\mathcal Z(Q\rho)
       =(1-C)Z_0+\sum_{a=1}^TF_a\rho^a+Z_T\rho^{T+1}.
\]
Here \(CQ^{T+1}=1\) fixes the retained top term.

Here is a finite summation proof with its boundary terms.
Gaussian Pascal gives
\[
 I_{a-1,k}=I_{a,k-1}-Q^aC^2I_{a,k}.
\]
Set \(R_k=(1-Q^{a+k})w_{a,k}\), and set both
\(R_{H+1}\) and \(w_{a-1,H+1}\) equal to zero.
The exact telescoping certificate is
\[
 w_{a-1,k+1}-Q^aC^2w_{a-1,k}
       -(1-CQ^a)^2w_{a,k}=R_{k+1}-R_k.                         \tag{17}
\]
After dividing by \(w_{a,k}\), this is the elementary identity
\[
 uv(1-C/u)^2+(1-vC^2/u)(1-vu)-(1-Cv)^2=0,
 \qquad u=Q^k,\quad v=Q^a.
\]
At the bottom \(R_0=w_{a-1,0}\). The term
\(I_{a,-1}-I_{a,0}\) is
\({N+p\brack a+p}_Q(C^2Q^{-p})^{N-a}=0\).
Indeed \(1\le a\le T\), \(H\ge p+1\), so its denominator
has no zero and its numerator contains \(1-Q^N\).
Summation by parts therefore gives
\[
 Y_{a-1}-(1-CQ^a)^2Y_a
   =-\sum_{k=1}^H R_k(I_{a,k}-I_{a,k-1}).                      \tag{18}
\]

The finite upper-cap difference is
\[
 I_{a,k}-I_{a,k-1}
 =-(C^2Q^{-p})^{N-a-k}{N+p-k\brack a+p}_Q.
 \tag{19}
\]
It vanishes for \(k\le p\). For \(k\ge p+1\), reflect every
factor in this Gaussian coefficient. Multiplication by \(R_k\)
leaves, in the positive sum on the right of (18),
\[
 {(-1)^{a+p}C^{-2a}
       Q^{-a(a-1)/2+pa+p(p+1)/2}\over f_{a+p}}\,
 {Q^{k^2-2Hk}\over f_kf_{k-p-1}f_{H-k}^2}.                     \tag{20}
\]
The remaining finite sum is
\[
 \sum_{k=p+1}^H
 {Q^{k^2-2Hk}\over f_kf_{k-p-1}f_{H-k}^2}
       =\chi\,{f_{2H-p-1}\over f_H^2f_{H-p-1}^2}.              \tag{21}
\]
For a direct verification set \(j=H-k\), \(L=H-p-1\).
The left side becomes
\(\chi\sum_{j=0}^{L}Q^{j^2}/(f_{H-j}f_{L-j}f_j^2)\).
Extracting the appropriate coefficient from
\((-t;Q)_H(-tQ^H;Q)_L=(-t;Q)_{H+L}\), exactly as in (13),
gives \(f_{H+L}/(f_H^2f_L^2)\). This proves (21).
Finally
\[
                    {P_a\over P_{a-1}}
                           =-CQ^a(1-CQ^a).
 \tag{22}
\]
Multiplying (18)--(21) by \(P_a/(1-CQ^a)\), and keeping the
minus sign when reversing the left side, proves (16).
Thus the recurrence retains the entire finite cap even at the
indices where a split geometric sum would have a resonant ratio.

## 5. Exact two-branch connection and its Cauchy cap

Return to \(r=2\). Use the nonzero normalization
\[
 \mathcal P_N=H_dK^{-d}{f_{2H-1}\over f_H^2},\qquad
 g_a={D_a\over\mathcal P_Nx^a},\qquad
 G_T(\rho)=\sum_{a=0}^Tg_a\rho^a,\qquad \rho=xw_1/w_2 .
 \tag{23}
\]
The original monomial-output first column is exactly
\(\mathcal P_N w_2^TG_T(xw_1/w_2)\). The scalar
\(\mathcal P_N\) is a unit; the vacuum
\(\mathcal P_NG_T(0)\) can vanish.

Equations (14),(16) give
\[
 g_0=1-\chi,\qquad
 (1-CQ^a)g_a+CQ^ag_{a-1}
       =-(1-C)\chi\,{(Q/C)^a(C;Q)_a\over f_a},
             \quad 1\le a\le T.                              \tag{24}
\]
Equivalently the full polynomial row, with its top term, is
\[
 \boxed{\quad
 G_T(\rho)-C(1-Q\rho)G_T(Q\rho)
 =(1-C)\left[1-\chi\sum_{a=0}^T
                {(Q/C)^a(C;Q)_a\over f_a}\rho^a\right]
                                      +g_T\rho^{T+1}.
 \quad}                                                       \tag{25}
\]
Here \(g_T\) on the right denotes the last coefficient of \(G_T\).
The top coefficient is \(CQ^{T+1}g_T=g_T\), not zero.

Define the auxiliary finite polynomial and reciprocal product
\[
 \mathfrak g_T(\rho)=\sum_{a=0}^T
       {(-1)^aQ^{a(a+1)/2}\over(Q^{H+1};Q)_a}\rho^a,
 \qquad P_H(\rho)=(Q^{1-H}\rho;Q)_H.                            \tag{26}
\]
The first vanishing denominator of the displayed coefficients
would be at \(a=T+1\); that coefficient is never defined.
Writing \(u_T=[\rho^T]\mathfrak g_T\), direct comparison of
consecutive finite coefficients proves
\[
 \mathfrak g_T(\rho)+(Q\rho-C)\mathfrak g_T(Q\rho)
                 =1-C+Q^{T+1}u_T\rho^{T+1}.                   \tag{27}
\]
Also
\[
 {P_H(Q\rho)\over P_H(\rho)}
                  ={1-Q\rho\over1-QC^{-1}\rho},\qquad
 [\rho^a]P_H^{-1}={(Q/C)^a(C;Q)_a\over f_a}
                  \quad(0\le a<N).                           \tag{28}
\]
The coefficient formula follows by multiplying the finite factors
of \(P_H\), or by their first-order ratio equation at zero.
It does not require an infinite root-factorial series.

The coefficient row (24) is noncharacteristic through \(a=T\),
since \(1-CQ^a\ne0\) there. Equations (27),(28) and the initial
value consequently prove the exact connection
\[
 \boxed{\quad
 G_T(\rho)=
  \left[\mathfrak g_T(C\rho)
           -\chi\,{\mathfrak g_T(\rho)\over P_H(\rho)}
  \right]_{\le T}.
 \quad}                                                       \tag{29}
\]
The square bracket means literal Taylor truncation. No cap has
been discarded, and (29) is valid through the full physical
range, including \(a+2H\ge N\).

There is a useful exact rational continuation of these finite
coefficients. Iterate (27) \(H\) times modulo \(\rho^{T+1}\).
The resulting product is
\(\prod_{\ell=1}^H(C-Q^\ell\rho)=Q^{H^2}P_H(\rho)\).
Hence
\[
 G_T=[\mathscr R_N]_{\le T},\qquad
 \mathscr R_N(\rho)=
 {-\,\chi(1-C)\displaystyle\sum_{j=0}^{H-1}
                     \prod_{\ell=0}^{j-1}(C-Q^{\ell+1}\rho)
       \over P_H(\rho)}.                                     \tag{30}
\]
The numerator has degree at most \(H-1\), and every pole of this
specified rational function lies on \(|\rho|=1\).
The finite column is therefore the exact coefficient contour
\[
 G_T(\rho)={1\over2\pi i}\oint_{|z|=R}
       \mathscr R_N(z)\,
             {1-(\rho/z)^{T+1}\over z-\rho}\,dz,\qquad0<R<1 .
 \tag{31}
\]
The apparent singularity at \(z=\rho\) is removable. The second
term in its numerator is the finite cap; it remains in (31).
This rational continuation is only a coefficient adapter for
the actual finite column, not a new physical infinite module.

## 6. Actual branch estimates on a fixed activity disk

Fix \(0<\alpha_-<\alpha_+<1/2\) and restrict
\[
                 \alpha_-\le H/N\le\alpha_+ .
 \tag{32}
\]
Put \(c_0=2\pi i\), retain \(C=Q^H\) exactly, and use the
logarithms and dilogarithms analytic at \(\rho=0\). Define
\[
 \begin{split}
 a_1(\rho;C)&={1-C\over1-C+C\rho},\\
 \psi(\rho;C)&={\operatorname{Li}_2(\rho)
                    -\operatorname{Li}_2(C^{-1}\rho)\over c_0},\\
 a_2(\rho;C)&={1-C\over1-C+\rho}
                     \sqrt{{1-C^{-1}\rho\over1-\rho}} .
 \end{split}                                                  \tag{33}
\]
The square root is one at zero. For a sufficiently small fixed
disk these two amplitudes are holomorphic units uniformly in (32).

For every prescribed \(\gamma>0\), there is \(r_\gamma>0\)
such that on \(|\rho|\le r_\gamma\)
\[
 \boxed{\quad
 G_T(\rho)=a_1(\rho;C)(1+\epsilon_{1,N}(\rho))
       -\chi e^{N\psi(\rho;C)}
                       a_2(\rho;C)(1+\epsilon_{2,N}(\rho))
       +\mathcal E_N(\rho),
 \quad}                                                       \tag{34}
\]
where the errors are holomorphic,
\[
 \|\epsilon_{j,N}\|\le C/N,\qquad
                  \|\mathcal E_N\|\le C_\gamma e^{-\gamma N}.
 \tag{35}
\]
Every fixed activity derivative has the same estimates on a
smaller disk. These are additive estimates for the two retained
branches, not a relative estimate for their possibly vanishing
difference.

Here is a complete low/high proof. If \(u_a=[\rho^a]\mathfrak g_T\),
then
\[
 {u_a\over u_{a-1}}={-Q^a\over1-CQ^a},\qquad
                         u_a=(-1)^aQ^{a(a+1)/2}{f_H\over f_{H+a}} .
 \tag{36}
\]
Choose a fixed \(\delta>0\) so that \(H+a\) stays a positive
distance from \(N\) for \(a\le\delta N\). On this band both
the ratios in (36) and their limits \(-1/(1-C)\) are bounded
by a common constant. Their difference is \(O(a/N)\).
Telescoping the products, without a small-\(a\) asymptotic
assumption, gives
\[
 \left|u_a-\left({-1\over1-C}\right)^a\right|
                         \le A^a a^2/N,\qquad a\le\delta N .
 \tag{37}
\]
Every root factorial obeys
\[
 |f_j|\le2^N,\qquad |f_j|\ge N2^{-N},\qquad 0\le j<N.
 \tag{38}
\]
The lower bound follows from
\(|f_jf_{d-j}|=N\); thus it includes both endpoints.
Consequently \(|u_a|\le4^N\) for all \(a\le T\).
On a sufficiently small fixed disk, the sum of the high terms
\(a>\delta N\) is exponentially small, whereas (37) sums to
\(O(N^{-1})\). The geometric-series tail is also exponentially
small there. This proves
\[
 \mathfrak g_T(\rho)
       ={1-C\over1-C+\rho}(1+O(N^{-1})),                        \tag{39}
\]
as a holomorphic relative estimate, and proves the analogous
formula at \(C\rho\). No coefficient beyond \(T\) is used.

For \(P_H\), apply the elementary trapezoid remainder to
\(f(v)=\Log(1-\rho e^{c_0v})\) on \([-H/N,0]\). Its first two
derivatives are bounded uniformly on every disk \(|\rho|\le R<1\).
The mesh consists of the right endpoints, so
\[
 \Log P_H(\rho)
 =-N\psi(\rho;C)
    +\tfrac12\Log{1-\rho\over1-C^{-1}\rho}+O(N^{-1}).             \tag{40}
\]
The same estimate holds for fixed activity derivatives.
Exponentiation gives the square root and the second amplitude
in (33), with a holomorphic relative \(O(N^{-1})\) error.

It remains to justify the finite cut in (29). On a fixed
circle \(|\rho|=R<1\), (38) gives
\[
 \left|{\mathfrak g_T(\rho)\over P_H(\rho)}\right|
              \le (T+1)4^N(1-R)^{-H}\le e^{B_RN}.
 \tag{41}
\]
The Taylor tail above \(T\), on a smaller radius \(r<R\),
is at most
\[
 {e^{B_RN}\over1-r/R}(r/R)^{T+1}.
 \tag{42}
\]
Since \((T+1)/N=1-H/N\ge1-\alpha_+>1/2\), shrinking \(r\)
after fixing \(R\) makes (42) smaller than \(e^{-\gamma N}\)
for any prescribed \(\gamma\). Equations (39)--(42) prove
(34),(35) for the original finite column. Cauchy estimates
on nested disks prove the derivative claims.

## 7. Selected sectors and the exact scope of the estimate

On any compact activity sector inside the disk of (34) with
\(\Re\psi\ge\eta>0\), the second branch is selected:
\[
 G_T=-\chi e^{N\psi}a_2
                  (1+O(N^{-1})+O(e^{-\eta N})).
 \tag{43}
\]
On a compact sector with \(\Re\psi\le-\eta<0\), the first branch
is selected:
\[
 G_T=a_1(1+O(N^{-1})+O(e^{-\eta N})).
 \tag{44}
\]
In particular the actual column is nonzero on these sectors for
all sufficiently large \(N\), with its original prefactor
\(\mathcal P_Nw_2^T\) retained.

Both types of sector exist uniformly in (32). Indeed
\[
 \Re\psi'(0;C)={\sin(2\pi H/N)\over2\pi}>0 .
 \tag{45}
\]
It has a positive uniform lower bound on (32). A sufficiently
narrow fixed cone about the positive real axis, with activity
bounded away from zero, satisfies the positive condition;
the reflected cone about the negative real axis satisfies the
negative one. At \(\Re\psi=0\), and in the microscopic
neighborhood of zero, the two terms in (34) must both remain.
The exact vacuum zeros in §3 are compatible with (34).

The statements concern a literal monomial-output first column
of the complementary operator. Applying the original binomial
input/coherent resolution is an additional exact convolution.
It is not estimated by merely inserting the small-activity
phase into that convolution. For example a finite identity
kernel can have phase zero in a small monomial bidisk while its
binomial transform has a nondegenerate mixed phase, supplied by
a Cauchy pole outside that bidisk. Neither a regular coherent
graph nor its absence follows from the phase of (34) alone.
The Cauchy adapter (31), its cap, all outer routing coupons and
their complementary chains remain available for that next step.

The root is fixed throughout. No meridian derivative is taken
through (4), (14), or (29); the original source still has its
separate meridian-normal rows. No \(q\)-normal, exterior pairing,
geometric occurrence, or closed-source noncancellation is claimed.

## 8. The exact fixed-width connection

Here \(p=r-2\) is fixed, \(h=H-p\ge1\), \(C'=Q^h\), and (32)
holds. Normalize the all-width scalar column by
\[
 P_p={f_{2H-p-1}\over f_H^2},\qquad
 G_{p,T}(\rho)=\sum_{a=0}^T{Z_a\over P_p}\rho^a .
 \tag{46}
\]
The normalization \(H_dK^{-d}P_p\) is nonzero. It is still not
the possibly zero vacuum.

The exact vacuum can be expressed using only \(p+1\) quantities.
Set \(R_0=1\) and determine \(R_1,\ldots,R_p\) by
\[
 (1-Q^j)R_{j-1}-2(1-C^{-1}Q^j)R_j
                +(1-C^{-2}Q^j)R_{j+1}=0,\quad 0\le j<p .
 \tag{47}
\]
The \(R_{-1}\) term drops at \(j=0\). Define
\[
 d_{p,N}=(Q^{2H-p};Q)_{p+1}
 \sum_{j=0}^p
 {(-1)^jQ^{j(j+1)/2}R_{p-j}\over
            f_jf_{p-j}(1-Q^{2H-p+j})}.
 \tag{48}
\]
Then the actual vacuum is
\[
                         G_{p,T}(0)=1-\chi d_{p,N}.            \tag{49}
\]
In particular \(d_{0,N}=1\).

To prove this directly, expand the Gaussian coefficient in
\(I_{0,k}\) as a product of length \(p\), then sum its finite
geometric series. Its \(j\)-th term is
\[
 {(-1)^jQ^{j(j+1)/2}\over f_jf_{p-j}}\,
 {1-C^{-2k}Q^{(p-j)k}\over1-Q^{2H-p+j}} .
 \tag{50}
\]
Keep the normalization \(Z_0=f_H^2Y_0\) explicit. The raw
weights in \(Y_0\) satisfy
\[
                 \sum_{k=0}^Hw_{0,k}={f_{2H}\over f_H^4}.
\]
After multiplication by \(f_H^2\), the actual constant-endpoint
moment is \(f_{2H}/f_H^2\). The constant endpoint of (50) therefore
gives \(P_p\), using the inner
partial-fraction identity
\(\sum_j(-1)^jQ^{j(j+1)/2}/
 [f_jf_{p-j}(1-zQ^j)]=(z;Q)_{p+1}^{-1}\).
This last identity follows by expanding near \(z=0\) and
applying finite Gaussian Pascal; rational continuation is
legitimate since the displayed divisors are nonzero here.

For the other endpoint put
\[
 \mathcal F(z)=\sum_{k=0}^H{(Q^{-H};Q)_k^2\over f_k^2}z^k .
 \]
Its exact coefficient row is
\([(1-T_z)^2-z(1-C^{-1}T_z)^2]\mathcal F=0\).
The top coefficient vanishes because \(1-C^{-1}Q^H=0\).
Finite reflection and (13) give
\(\mathcal F(Q)=\chi f_{2H}/f_H^2\ne0\).
At \(z=Q^j\), this row gives exactly (47) for
\(R_j=\mathcal F(Q^{j+1})/\mathcal F(Q)\).
For the other endpoint the corresponding raw moment is
\[
 \sum_{k=0}^H w_{0,k}C^{-2k}Q^{(p-j)k}
                    ={\mathcal F(Q^{p-j+1})\over f_H^2}.
\]
Multiplication by the same \(f_H^2\) makes its actual \(Z_0\)
moment \(\mathcal F(Q^{p-j+1})\). Substituting these two
prefactored moments proves (48),(49), with no omitted \(f_H^2\).
For fixed \(p\), all denominators in (47),(48) except the
displayed short factorials are uniformly separated from zero
under (32), and \(|f_jf_{p-j}|^{-1}=O(N^p)\).
Consequently
\[
                              |d_{p,N}|\le C_pN^p .             \tag{51}
\]

Use (26) with \(H\) replaced by \(h\), including its correct
cap \(T+p=d-h\), and set
\[
 F_h(\rho)={\mathfrak g_{T+p}^{\,C'}(\rho)\over P_h(\rho)},
 \qquad P_h=(Q^{1-h}\rho;Q)_h,\qquad
 U_p(\rho)={F_h(\rho)-[F_h]_{<p}(\rho)\over\rho^p},
\]
\[
 b_p=(-1)^pQ^{pH-p(p+1)/2}{f_H\over f_h},\qquad
 \delta_{p,N}=1-\chi d_{p,N}+\chi b_p[\rho^p]F_h .
 \tag{52}
\]
For \(p=0\) the subtracted polynomial is zero. The quotient
defining \(U_p\) is removable at zero. All factorials in (52)
have indices below \(N\); in particular the auxiliary polynomial
is cut just before its first zero denominator.

The exact connection through the entire physical cap is
\[
 \boxed{\quad
 G_{p,T}=
       [\,\delta_{p,N}\mathfrak g_T(C\rho)
                             -\chi b_pU_p(\rho)\,]_{\le T}.
 \quad}                                                       \tag{53}
\]
To check it, apply \(L_C=1-C(1-Q\rho)T_\rho\).
For every positive degree at most \(T\),
\[
 [\rho^a]L_CU_p=(1-C')[\rho^{a+p}]P_h^{-1}.
 \]
At degree zero the additional term is
\(-C[\rho^{p-1}]F_h\); this is retained through the initial
value in \(\delta_{p,N}\).
The explicit coefficient is
\[
 [\rho^{a+p}]P_h^{-1}
 ={(Q^{p+1}/C)^{a+p}(C';Q)_p(C;Q)_a\over f_{a+p}} .
 \]
Multiplication by \(b_p(1-C')\) gives exactly the right side of
(16), after division by \(P_p\) and removal of \(-\chi\).
The initial value of (53) is (49). Since \(1-CQ^a\ne0\)
for \(a\le T\), these checks prove (53).
The auxiliary top at \(T+p+1\) shifts to \(T+1\) after
division by \(\rho^p\), so no physical coefficient is lost.
This proof uses the exact finite recurrences, not an infinite
root series or a conjectural simplification of \(\delta_{p,N}\).

For example one can retain precisely two marked character terms
by writing (53) as
\[
 G_{p,T}=[\,B_{1,N}-\chi B_{2,p,N}\,]_{\le T},\qquad
 B_{1,N}=\mathfrak g_T(C\rho),\quad
 B_{2,p,N}=b_pU_p+
                (d_{p,N}-b_p[\rho^p]F_h)B_{1,N}.                \tag{54}
\]
Here \(B_{2,p,N}(0)=d_{p,N}\). No claim that
\(\delta_{p,N}=1\), or that either vacuum term is a normalized
unit at general width, is needed.

The analytic estimates already proved apply to \(F_h\), with
the exact shifted parameter \(C'=Q^{H-p}\). They give
\[
 F_h=e^{N\psi(\rho;C')}a_2(\rho;C')(1+O(N^{-1})),\qquad
 [\rho^j]F_h=O(N^j)\quad\hbox{for fixed }j.                     \tag{55}
\]
The fixed-coefficient estimate follows either from (52)'s
finite products or by differentiating their holomorphic
logarithms at zero. Equations (51),(52) imply
\(|\delta_{p,N}|\le C_pN^p\), and \(b_p\) is a uniformly
bounded nonzero unit. On a small punctured compact with
\(\Re\psi(\rho;C')\ge\eta>0\), the actual column therefore has
\[
 G_{p,T}=-\chi b_p\rho^{-p}
       e^{N\psi(\rho;C')}a_2(\rho;C')
                  (1+O(N^{-1})+O(N^pe^{-\eta N})).             \tag{56}
\]
The zero-phase terms and every Taylor subtraction are smaller
by the displayed exponential gap. The cap in (53) is paid by
the same Cauchy estimate (41),(42), with only fixed additional
powers of \(N\) and \(\rho^{-1}\); it can be made
\(O(e^{-\gamma N})\) by first fixing \(p,\delta,R\) and then
shrinking the activity disk. Thus (56) is an estimate for the
finite source column. It is not uniform as \(\rho\to0\).

## 9. The actual all-width lift and its retained competing branches

The lift in §2 is explicit. With \(s=r-1=p+1\) prefix heads,
expanding \(F_A^a/f_a\) in increasing coproduct order gives
\[
 v_a(\mathbf w)=
 \sum_{|\mathbf b|=a}x^{-\sum_{i=1}^{s}(i-1)b_i}\mathbf w^{\mathbf b}.
 \tag{57}
\]
The Gaussian multinomial cancels the individual raising
factorials. The earlier Cartans act on their vacuum before the
earlier raising terms, leaving exactly the powers in (57);
there is no unlisted quadratic chirp.
Put
\[
 z_i=k_Ax^{-(i-1)}w_i/w_r,\qquad
 \mathcal G_{p,T}(\mathbf z)
       =\sum_{a=0}^T[\rho^a]G_{p,T}\,h_a(\mathbf z).
 \]
The original output polynomial is precisely
\[
          H_dK^{-d}P_p w_r^T\,\mathcal G_{p,T}(\mathbf z).
 \tag{58}
\]
Here \(h_a\) is the complete homogeneous polynomial. No prefix
occupation or auxiliary channel has been interpolated.

For distinct \(z_i\), the finite identity is
\[
 \mathcal G_{p,T}(\mathbf z)
       =\sum_{i=1}^{s}{z_i^pG_{p,T}(z_i)\over
                                    \prod_{j\ne i}(z_i-z_j)}.
 \tag{59}
\]
It follows by partial fractions of
\(\prod_i(1-z_it)^{-1}\). Coincident variables have its unique
analytic divided-difference continuation.
Inserting (53), the \(z_i^{-p}\) in \(U_p\) cancels the
factor \(z_i^p\), and the Taylor polynomial of degree \(p-1\)
is killed exactly by the order-\(p\) divided difference.
Thus, up to the already bounded finite-cut error, the full
second endpoint is
\[
                -\chi b_p[z_1,\ldots,z_s]F_h.                  \tag{60}
\]
The first endpoint is \(\delta_{p,N}\) times the bounded lift
of \(\mathfrak g_T(C\rho)\); its leading bounded function is
\(\prod_i(1-Cz_i/(C-1))^{-1}\).
Uniform cap bounds, including near coincident variables, follow
by the fixed-order Cauchy formula for divided differences on a
slightly larger activity circle.

Consequently take any compact separated set of activities in the
small disk, and fix \(i_*\) with
\[
 \Re\psi(z_{i_*};C')\ge\eta>0,\qquad
 \Re\psi(z_{i_*};C')-\Re\psi(z_j;C')\ge\eta
                              \quad(j\ne i_*).
 \tag{61}
\]
The complete actual lifted boundary satisfies
\[
 \boxed{\quad
 \mathcal G_{p,T}(\mathbf z)=
 {-\,\chi b_p e^{N\psi(z_{i_*};C')}
                         a_2(z_{i_*};C')
       \over\prod_{j\ne i_*}(z_{i_*}-z_j)}
       (1+O(N^{-1})+O(N^pe^{-\eta N})).
 \quad}                                                       \tag{62}
\]
All displayed amplitude factors are nonzero on this compact.
Such domains are nonempty: choose distinct sufficiently small
positive real \(z_i\), with one strictly largest, using (45).
The exact \(p/N\) shift in \(C'\), the character \(\chi\), the
original factor (58), and all finite caps remain.

On ties or confluent faces use (59),(60), with all branches and
derivatives retained. No zero-free whole polydisk follows from
(62). This theorem initializes an actual complementary boundary
at arbitrary fixed width. It neither propagates a full two-sided
kernel nor evaluates the subsequent binomial-input, exterior,
or original relative-cycle pairing.

## Complete proof directs and author protocol

* G: notes/research_opposite_kernel_forced_cyclic_normalization.md,
  489 lines, SHA256
  42e6d6c3a5039859c241a2832de56301eff49d749db86d67868f3534c89aaaaa.
* R: notes/research_full_opposite_source_routing_graph.md,
  594 lines, SHA256
  17690199c1962987261b002afe7ecd359999ec1387f19ba2817663d22b52901d.

Both complete directs were freshly wholly reread, nontruncated,
in this author sequence. Every used implication was checked.
The entire matching final was reread nontruncated and all three
hashes renewed. Independent matching peer review and root adoption
remain separate. Only written mathematics and text/hash operations
were used. No frozen/public file was edited, and no mathematical
program or test was run.

