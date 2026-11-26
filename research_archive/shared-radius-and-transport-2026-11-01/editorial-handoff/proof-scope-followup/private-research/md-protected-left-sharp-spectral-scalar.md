# The exact protected left coefficient, its zero rate, and the sewn difference identity

This note concerns the actual homogeneous Casimir numerator at the protected quartet
\((x,b,c,y)=(x,0,c,0)\). It retains the original one-sided row cutoff, every unused spectral factor, and both value and derivative data at the physical nodes. The sharp scalar spectral rate is zero at every permitted load. Consequently its local weighted estimate cannot improve the shared-radius envelope. The last sections give an exact signed regrouping and explain which inverse norms are polynomial and which are exponentially large.

## 1. Original finite polynomial

Let
\[
 N\ge2,\quad d=N-1,\quad m=\lfloor N/2\rfloor,\quad M=m-1,
 \quad q=e^{\pi i/N},\quad Q=q^2,
 \tag{1}
\]
and set
\[
 c_r=q^{2r+1}+q^{-2r-1},\quad
 s_r=2\sin(\pi r/N),\quad S_j=\prod_{r=1}^j s_r,\quad
 \chi_N(\sigma)=2T_N(\sigma/2)+2.
 \tag{2}
\]
Here \(S_0=1\), \(s_0=s_N=0\), and \(T_N(\cos\theta)=\cos(N\theta)\). The symbols \(c_r\) are spectral nodes, whereas \(c\) without a subscript is the output-middle face variable.

The original face operator is
\[
 C(x,y)z^r=c_rz^r-s_r^2(x+y)z^{r-1}-s_rs_{r-1}xy z^{r-2}.
 \tag{3}
\]
Its polynomial numerator is
\[
 V_N(\sigma;C)=\frac{\chi_N(\sigma)-\chi_N(C)}{\sigma-C}.
 \tag{4}
\]
Division in (4) is polynomial division. At the root \(\chi_N(C)=0\), but the quotient still records all first normals at repeated roots. The homogeneous source convention is
\[
 H_V(x,b,c,y;\sigma)
   =\sum_{0\le i\le j\le d}b^ic^{d-j}
             V_N(\sigma;C(x,y))_{i,j}.
 \tag{5}
\]
This is the actual source convention in `actual_homogeneous_casimir_face_source.md`, §1, extended to the original Morse cut in `research_matched_sphere_morse_source.md`, §§5–6. Nothing is replaced by a positive model.

Setting \(b=y=0\) forces \(i=0\), eliminates every two-step arrow, and leaves the unique one-step path from \(j\) to zero. Its coefficient is therefore exactly
\[
 v_j(\sigma)=(-1)^jS_j^2\prod_{r=j+1}^{d}(\sigma-c_r),
 \qquad
 H_{V,L}(x,0,c,0;\sigma)=\sum_{j=0}^{M}v_j(\sigma)x^jc^{d-j}.
 \tag{6}
\]
The unused product includes the entire omitted half of the original level-\(N\) matrix. The cutoff is \(j\le m-1\) at both parities; at odd level the central row is in the central sector instead. Formula (6) is a polynomial identity, including spectral collisions.

## 2. Exact real-spectral supremum

For \(n=N-2j-2\ge0\), put
\[
 B_n(w)=\prod_{r=0}^{n-1}(w+q^{2r-n+1})
       =\sum_{k=0}^n\frac{S_n}{S_kS_{n-k}}w^k.
 \tag{7}
\]
Its coefficients are positive, because \(n<N\). One elementary proof expands the product and uses the finite sine-binomial recursion, or inducts with
\[
 B_{n+1}(w)=(q^n w+1)B_n(q^{-1}w).
 \tag{8}
\]
No assumption about the signs of an uncombined resolvent expansion enters here.

Since
\(\chi_N(w+w^{-1})=w^{-N}(w^N+1)^2\), the removed rows \(0,\ldots,j\) use \(2j+2\) distinct roots of one factor \(w^N+1\). Their complement is precisely (7). It follows that
\[
 v_j(w+w^{-1})
 =(-1)^jS_j^2w^{j+1-N}(w^N+1)B_{N-2j-2}(w).
 \tag{9}
\]
After removal of \((-1)^j\), every Laurent coefficient is positive. For \(|w|=1\), the triangle inequality is attained at \(w=1\). Thus the exact maximum on the entire real interval is
\[
 \max_{-2\le\sigma\le2}|v_j(\sigma)|=|v_j(2)|=:U_j,
 \quad
 U_j=\frac{4S_j^2}{\prod_{r=0}^j(2-c_r)},
 \quad v_j(2)=(-1)^jU_j.
 \tag{10}
\]
This single spectral value works for every left index simultaneously, at both parities.

The ratios are
\[
 \frac{U_j}{U_{j-1}}
  =\frac{\sin^2(j\pi/N)}{\sin^2((j+1/2)\pi/N)}\le1
                         \qquad(1\le j\le M).
 \tag{11}
\]
The two exact last-index values are
\[
 U_M=\begin{cases}
 N,&N=2m,\\
 N\sec^2(\pi/(2N)),&N=2m+1.
 \end{cases}
 \qquad U_0=\csc^2(\pi/(2N))\le N^2.
 \tag{12}
\]
For the even identity use \(S_{m-1}^2=N/2\) in (9), where \(B_0=1\). For the odd identity use \(S_m^2=N\), \(s_m=2\cos(\pi/(2N))\), and \(B_1(1)=2\). The final inequality follows from the chord bound \(\sin(\pi/(2N))\ge1/N\). Consequently
\[
 \boxed{\quad N\le\max_{[-2,2]}|v_j|=U_j\le N^2
                 \quad(0\le j\le M).\quad}
 \tag{13}
\]
In particular, uniformly over every allowed index and every sequence \(j/N\to u\in[0,1/2]\),
\[
             \frac1N\log\max_{[-2,2]}|v_j|\longrightarrow0.
 \tag{14}
\]
This proves the sharp coefficientwise uniform rate, not merely an upper bound for a sum.

## 3. Spectral normals and the positive reference

The factorization (6) retains every node. At any paired node \(c_a=c_{d-a}\), with \(0\le a\le\lfloor d/2\rfloor\), it gives
\[
 v_j(c_a)=0,\qquad
 v_j'(c_a)=\begin{cases}
 (-1)^jS_j^2\displaystyle\prod_{\substack{r>j\\r\ne d-a}}(c_a-c_r),&a\le j,\\
 0,&a>j.
 \end{cases}
 \tag{15}
\]
The first case removes the sole unused copy; in the second both copies are unused. At odd \(N=2m+1\), the simple node \(-2=c_m\) also satisfies
\[
 v_j(-2)=0,\qquad
 v_j'(-2)=(-1)^jS_j^2
             \prod_{\substack{r>j\\r\ne m}}(-2-c_r)\ne0.
 \tag{16}
\]
The node \(a=m\) in this odd case is simple and is treated by (16), not by (15). Differentiating the polynomial identity is legitimate; no product is divided by a vanishing sampled factor. Markov's inequality on \([-2,2]\) also gives the uniform finite bound
\[
 \max_{[-2,2]}|v_j'|
       \le\frac{(d-j)^2}{2}U_j\le\frac12N^4.
 \tag{17}
\]
Higher fixed derivatives have only fixed polynomial costs.

The positive reference is the actual even endpoint or the odd regularized endpoint:
\[
 p_{N,j}=\begin{cases}
 -v_j(-2),&N\text{ even},\\
 v_j(-2)-N^{-2}v_j'(-2),&N\text{ odd}.
 \end{cases}
 \tag{18}
\]
Both quantities are positive on left support. The exact unused products and uniform logarithmic sine sums give
\[
 \frac1N\log p_{N,j}=-2f(j/N)+O(\log N/N),\qquad
 f(u)=\frac{\Lambda(\pi u)+\Lambda(\pi/2-\pi u)}\pi.
 \tag{19}
\]
This is the \(i=0\) case of `actual_protected_outer_spectral_energy.md`, §§1–4, which derives the product before taking its rate and treats the odd removed central zero. Combining (13),(19) gives the exact relative-energy rate
\[
 \frac1N\log\frac{\max_{[-2,2]}|v_j|^2}{p_{N,j}}
                  =2f(j/N)+O(\log N/N).
 \tag{20}
\]
Thus the reference rate and relative-energy rate cancel in their half-sum. They give the same sharp scalar answer zero.

For the physical filling functional \(\mathcal L_N^n\), node-vanishing rather than derivative-vanishing is relevant. Every \(v_j\) vanishes at the entire node grid, so the proved finite Hermite norm in `actual_uniform_filling_supremum_bound.md`, §§3–5, gives
\[
          |\mathcal L_N^n v_j|\le\frac dN U_j\le N^2
                 \qquad(n\in\mathbb Z).
 \tag{21}
\]
The functional still retains the original crossing polynomial, Cartan factor and first-normal terms. Equation (21) is independent of the fixed signed power; it does not say those normal terms vanish or supply a lower bound after filling.

## 4. The weighted envelope is locally exact

For fixed positive \(x,c\), the exact phase-uniform weighted supremum is
\[
 \sup_{\substack{\sigma\in[-2,2]\\|X|=x,\ |C|=c}}
     |H_{V,L}(X,0,C,0;\sigma)|
        =\sum_{j=0}^{M}U_jx^jc^{d-j}.
 \tag{22}
\]
The upper bound follows from (13). Equality follows at \(\sigma=2\), \(X=-x\), \(C=c\), because the actual sign is \((-1)^j\). Since there are at most \(N\) terms and \(N\le U_j\le N^2\),
\[
 \lim_{N\to\infty}\frac1N\log\sup |H_{V,L}|
       =\max\{\log c,\tfrac12(\log x+\log c)\}.
 \tag{23}
\]
At the protected singleton the existing envelope is therefore sharp. It was not enlarged by an unnecessarily positive recurrence or a nonoptimal scalar spectral estimate.

For the R54 source, \(x=L_0\), \(c=L_{16}\), and the finite target remains \(d\) on both faces. The rational witness in `actual_singleton_sector_envelope_obstruction.md` assigns left load \(u=\lambda/2\); its remaining loads belong to actual central triangles. Replacing its left scalar bound by (14), or its reference/energy half-sum by (19),(20), leaves that contribution equal to zero. It does not turn the existing envelope obstruction into a strict source bound. A separate shared-array argument is required to interpret the other coefficients; no signed source lower bound is inferred here.

## 5. An exact difference equation with both boundary currents

Define the finite generating polynomial
\[
 G_N(z;\sigma)=\sum_{j=0}^{M}v_j(\sigma)z^j,
 \qquad \mathscr D_\sigma F(z)
   =(\sigma+2z)F(z)-(q+q^2z)F(Qz)
                       -(q^{-1}+q^{-2}z)F(Q^{-1}z).
 \tag{24}
\]
The unique-path coefficients satisfy
\[
 (\sigma-c_0)v_0=\chi_N(\sigma),\qquad
 (\sigma-c_j)v_j=-s_j^2v_{j-1}\quad(1\le j\le M).
 \tag{25}
\]
Multiplying by \(z^j\), summing, and retaining the last omitted arrow proves the exact polynomial identity
\[
 \boxed{\quad\mathscr D_\sigma G_N
       =\chi_N(\sigma)+s_m^2v_M(\sigma)z^m.\quad}
 \tag{26}
\]
There is no sum beyond the physical left cutoff. At \(\sigma=2\), equations (12) imply \(s_m^2U_M=4N\) at both parities. With \(F_N(z)=\sum_{j=0}^M U_jz^j=G_N(-z;2)\), equation (26) becomes
\[
 2(1-z)F_N(z)+(q^2z-q)F_N(Qz)
             +(q^{-2}z-q^{-1})F_N(Q^{-1}z)
                         =4-4Nz^m.
 \tag{27}
\]
This is a terminating basic hypergeometric recurrence, stated as a polynomial identity so no notation for a hypergeometric continuation is needed. It has two explicit currents. Dropping either one would change the original source.

## 6. Exact sewing against the remaining source

In R54, extract all ordinary targets except at faces \(0,16\) from the original product of the other \(53\) central coupons. The result \(B_N(x,c)\) is homogeneous of degree \(d\): its original degree \(53d\) has lost exactly \(52d\). Its coefficients retain all other spectral variables and every original orientation. Write \(B_N(x,c)=c^d B_N(x/c)\). The original singleton source is exactly
\[
 [x^dc^d]\,H_{V,L}(x,0,c,0;\sigma)B_N(x,c)
       =[z^d]G_N(z;\sigma)B_N(z).
 \tag{28}
\]
This includes the alternating \((-1)^j\) at \(\sigma=2\). No spectator face targets have been reset.

For any polynomial \(B\) of degree at most \(d\), coefficient extraction gives
\[
 [z^d]G_N(Qz)B(z)=Q^d[z^d]G_N(z)B(Q^{-1}z).
 \tag{29}
\]
For the terms multiplied by \(z\), the character is \(Q^{d-1}\) instead. Since \(Q^{d+1}=1\), these two identities show that the complete operator in (24) is self-adjoint for the coefficient pairing:
\[
 [z^d](\mathscr D_\sigma F)B=[z^d]F(\mathscr D_\sigma B).
 \tag{30}
\]
Equivalently, on monomials it is the finite bidiagonal operator
\[
       \mathscr D_\sigma z^k=(\sigma-c_k)z^k+s_{k+1}^2z^{k+1};
 \tag{31}
\]
the final raising coefficient is zero because \(s_N=0\). The identities \(c_{d-k}=c_k\), \(s_{d-k}=s_{k+1}\) prove the same adjoint statement directly.

If \(B(z)=\sum b_kz^k\), equations (26),(30) therefore give
\[
 [z^d]G_N\left\{(\sigma+2z)B(z)
       -(q+q^2z)B(Qz)-(q^{-1}+q^{-2}z)B(Q^{-1}z)\right\}
       =\chi_N(\sigma)b_d+s_m^2v_M(\sigma)b_{d-m}.
 \tag{32}
\]
Every rescaled spectator argument is explicit. Equation (32) controls the pairing with \(\mathscr D_\sigma B\), not with \(B\) alone. In particular neither boundary coefficient is generally zero under the original targets.

## 7. Finite-orbit inverse and its conditioning

At \(\sigma=2\), all diagonal entries in (31) are positive. Thus \(\mathscr D_2\) is invertible on polynomials of degree at most \(d\). Its exact inverse, in the monomial basis, is
\[
 (\mathscr D_2^{-1})_{k,i}
 =\frac{(-1)^{k-i}\prod_{r=i+1}^{k}s_r^2}
          {\prod_{r=i}^{k}(2-c_r)}\quad(k\ge i),
 \qquad (\mathscr D_2^{-1})_{k,i}=0\quad(k<i).
 \tag{33}
\]
Define
\[
 E_i=\frac{\prod_{r=0}^{i-1}(2-c_r)}{S_i^2}.
 \tag{34}
\]
Then the absolute value in (33) is \(E_iU_k/4\), where (10) defines \(U_k\) for the full range \(0\le k\le d\). For this full range, the successive sine ratios first decrease and then increase. The endpoint values are \(U_0\le N^2\), \(U_d=N^2\), so \(U_k\le N^2\). Similarly \(E_0=1\), \(E_d=U_0/N^2\le1\), and the ratios for \(E_i\) also change from decrease to increase only once. Hence
\[
                    |(\mathscr D_2^{-1})_{k,i}|\le N^2/4.
 \tag{35}
\]
For any \(r>0\), evaluate polynomials at the exact finite orbit \(z_a=rQ^a\), \(0\le a<N\). The normalized discrete Fourier transform identifies these values with the coefficients multiplied by \(r^k\). Consequently the inverse on this orbit has coefficient matrix entries \(r^{k-i}(\mathscr D_2^{-1})_{k,i}\). There is no alias from (31), because the last raising arrow vanishes.

For \(0<r\le1\), every entry is still at most \(N^2/4\). In the normalized orbit Euclidean norm and the orbit supremum norm, respectively,
\[
 \|\mathscr D_2^{-1}\|_{2\to2}\le N^3/4,
 \qquad
 \|\mathscr D_2^{-1}\|_{\infty\to\infty}\le N^{7/2}/4.
 \tag{36}
\]
The first bound follows from the Frobenius norm of an \(N\)-by-\(N\) matrix; the second uses \(\|v\|_\infty\le\sqrt N\|v\|_2\) for the normalized orbit norm.

For \(r>1\), there is an exact obstruction to a polynomial inverse estimate. Its coefficient entry from zero to \(d\) is
\[
       |r^d(\mathscr D_2^{-1})_{d,0}|=\frac{N^2}{4}r^d.
 \tag{37}
\]
Thus even its orbit Euclidean operator norm is at least this exponential quantity. At spectral nodes the operator is singular and its normal data must instead be handled by the polynomial identities (15),(16),(26); no inverse bound through those nodes is asserted.

Finally, at \(\sigma=2\), let \(A=\mathscr D_2^{-1}B\). The actual signed source in (28) has the exact two-current expression
\[
 [z^d]G_N(z;2)B(z)=4[z^d]A(z)
               +4N(-1)^{m-1}[z^{d-m}]A(z).
 \tag{38}
\]
Although (36) has only polynomial cost on radii at most one, it does not bound the exponential size of the actual spectator \(B_N\), nor its indicated coefficients after inversion. Equations (32),(38) preserve a possible route to cancellation; they are not a proof that those currents are small. The R54 absolute-array obstruction and the original shifted-target obstructions prevent replacing this last source problem by independent positive norms.

## 8. Scope and checks

The exact monomer formula and its limiting zero profile agree with the published protected-outer coefficient theorem. The positive Laurent factorization extends the earlier private marked-row calculation to an explicit finite lower bound and the signed sewn identity. The all-level proofs above do not use finite numerical sampling.

A companion exact cyclotomic script independently constructs the original numerator from powers of its bidiagonal Casimir, then checks the unused-row product, Laurent identity, both node normals, difference equation, coefficient adjoint and endpoint inverse. Its scope is finite algebra only. No public files, source normalization, manuscript theorem or volume claim are changed by this note.
