# Function norms for the exact outgoing response

Research deduction, 7 November 2026. The outer factor in the complete
first-cardinal outgoing equation has a polynomial function-norm inverse
after retaining its exact homogeneous component. The actual component
is a derivative of the original reciprocal-factorial polynomial, so it
does not introduce an unspecified boundary datum.

The remaining type-three inverse has an explicitly determined
exponential norm on disks of radius below two. Its local contracting
direction on the actual output arc does not remove the complete orbit
or its source terms. All estimates below concern complete polynomials;
no numerical evaluation is used.

## 1. The outer factor and its homogeneous term

Use \(D=N-1\), \(r=e^{-2\pi i/N}\), and the exact operators of
[the outgoing equation](research_mixed_next_low_cardinal_outgoing_equation.md):
\[
 T_\pm f(Z)=f(r^{\pm1}Z),\qquad
 \mathcal L=Z^{-1}(I-T_-),\qquad
 \mathcal D=T_+(I-\mathcal L),\qquad
 \mathcal A=I-r\mathcal D .
 \tag{1}
\]
The quotients at zero are removable on polynomials. For
\(K(Z)=(1-Z)H(Z)\), direct substitution gives
\[
                 \mathcal AH(Z)=\frac{K(rZ)-K(Z)}Z.
 \tag{2}
\]
Thus \(\mathcal A\) maps polynomials of degree at most \(D\)
onto polynomials of degree at most \(D-1\). Its kernel is
\[
        \operatorname{span}\{p_D(Z)\},\qquad
        p_D(Z)=\frac{1-Z^N}{1-Z}=\sum_{j=0}^{D}Z^j.
 \tag{3}
\]

For \(R>0\), write
\(\|f\|_R=\max_{|Z|\le R}|f(Z)|\).

**Theorem 1.** Let \(W(Z)=\sum_{k=0}^{D-1}w_kZ^k\). Every
polynomial solution of \(\mathcal AH=W\), of degree at most \(D\),
is exactly
\[
 \begin{split}
 H(Z)&=H_W(Z)+c\,p_D(Z),\\
 H_W(Z)&=-\sum_{\ell=1}^{D}
       \frac{w_{\ell-1}}{r^\ell-1}
                          \sum_{j=0}^{\ell-1}Z^j,\qquad
 c=[Z^D]H .
 \end{split}
 \tag{4}
\]
For every \(R\ge1\),
\[
 \|H_W\|_R\le\frac{N^3}{8}\|W\|_R,\qquad
 \|H\|_R\le\frac{N^3}{8}\|W\|_R+N R^D|c|.
 \tag{5}
\]
Every fixed outgoing derivative has only additional polynomial
cost in \(N\), uniformly for \(R\) in compact subsets of \([1,\infty)\).

*Proof.* Multiplication of (4) by \(1-Z\) gives
\[
 (1-Z)H_W(Z)
    =\sum_{\ell=1}^{D}
       \frac{w_{\ell-1}}{r^\ell-1}(Z^\ell-1).
 \tag{6}
\]
Equation (2) now proves \(\mathcal AH_W=W\), and
\(\deg H_W\le D-1\). The only coefficients of a degree-\(N\)
polynomial killed by \(K(rZ)-K(Z)\) are the constant and \(N\)-th
ones. Its additional condition \(K(1)=0\) gives (3), proving (4).

For \(1\le\ell<N\), the sine chord gives
\[
          |1-r^\ell|\ge2\sin(\pi/N)\ge4/N.
 \tag{7}
\]
Cauchy's coefficient inequality gives
\(|w_{\ell-1}|\le R^{1-\ell}\|W\|_R\).
Because \(R\ge1\),
\(\|\sum_{j<\ell}Z^j\|_R\le\ell R^{\ell-1}\).
Therefore
\[
 \|H_W\|_R
   \le\frac N4\sum_{\ell=1}^{D}\ell\,\|W\|_R
   \le\frac{N^3}{8}\|W\|_R.
 \tag{8}
\]
Also \(\|p_D\|_R\le NR^D\). Polynomial Bernstein inequalities
on the circle, iterated for each fixed derivative, prove the final
claim. All these are function norms, not norms of Newton coefficients.
\(\square\)

## 2. The actual complete intermediate response

For \(\beta=0,1\), let
\[
 \psi_{\beta,j}=p_j/P_j^{1+\beta},\qquad
 \mathcal L_\beta=\mathcal A^\beta\mathcal L,\qquad
 S_{\beta,N}=\sum_{j=0}^{D}a_j\psi_{\beta,j},\qquad
 V_{\beta,N}=\sum_{j=0}^{D}v_j\psi_{\beta,j}.
 \tag{9}
\]
These are precisely the complete selected correction and the driving
column in the outgoing equation, with
\(V_{\beta,N}=\kappa^2\mathcal F_{\beta,N}^{\mathrm{opp}}\).
Define the intermediate source
\[
                      H_{\beta,N}=(I-\mathcal L_\beta)S_{\beta,N}.
 \tag{10}
\]
Its entire forcing is
\[
 \mathcal A H_{\beta,N}
   =W_{\beta,N}
   =\frac1{\kappa^2N^2}
        \{\mathcal A\mathcal L_\beta V_{\beta,N}
              +r\mathcal D V_{\beta,N}
              -v_D\psi_{\beta,D}\},
 \qquad v_D=N(-q)^{-D}.
 \tag{11}
\]
The top-row subtraction makes \(\deg W_{\beta,N}\le D-1\).

The homogeneous coefficient in Theorem 1 is known exactly:
\[
                 [Z^D]H_{\beta,N}
                       =\frac{d_N'(1)}{N^{2+\beta}}.
 \tag{12}
\]
Indeed \(\mathcal L_\beta\) lowers degree by at least one,
and \(p_D\) is monic with \(P_D=N\). Thus the left side is
\(a_D/N^{1+\beta}\). In the original moment formula,
\[
 a_D=\frac1N\operatorname{CT}_Y
       \left[\frac{d_N(Y)-1}{Y-1}\,Y^{-D}p_D(Y)\right]
            =\frac{d_N'(1)}N.
 \tag{13}
\]
The quotient has degree at most \(D-1\); since
\(Y^{-D}p_D(Y)=\sum_{j=0}^{D}Y^{j-D}\), the constant term
in (13) is the value of that quotient at one. This retains the
original forced \(d_N\), including its derivative.

**Corollary 2.** For \(R\ge1\), the complete intermediate response
has the explicit bound
\[
 \boxed{\quad
 \|H_{\beta,N}\|_R
 \le \frac{35}{8}N\|V_{\beta,N}\|_R
       +\frac18N^{2-\beta}R^D
       +N^{-\beta}R^D\|d_N\|_1 .
 \quad}
 \tag{14}
\]
It includes both parities and fixed outgoing derivatives with
polynomial cost.

*Proof.* On the circle of radius \(R\ge1\),
\[
 \|\mathcal Lf\|_R\le2R^{-1}\|f\|_R,\quad
 \|\mathcal Df\|_R\le3\|f\|_R,\quad
 \|\mathcal Af\|_R\le4\|f\|_R,\quad
 \|\mathcal L_\beta f\|_R\le2\cdot4^\beta\|f\|_R.
 \tag{15}
\]
All norms equal their boundary-circle suprema, so the removable
division at zero causes no loss. Also
\(\|\psi_{\beta,D}\|_R\le N^{-\beta}R^D\).
Consequently (11) gives
\[
 \|W_{\beta,N}\|_R
       \le35N^{-2}\|V_{\beta,N}\|_R
                         +N^{-1-\beta}R^D .
 \tag{16}
\]
Use (5), (12), and
\(|d_N'(1)|\le D\|d_N\|_1\le N\|d_N\|_1\).
This proves (14). \(\square\)

The already proved full cardinal bound
\[
 \|d_N\|_1\le C_\tau N^{A_\tau}
       \exp N\{c_{\mathrm b}/2+\tau\},\qquad
 c_{\mathrm b}=-2J(1/6)<1/3,\quad
 J(t)=\int_0^t\log(2\sin\pi s)\,ds
 \tag{17}
\]
is recorded in
[the high-cardinal whole-sector theorem, Section 3](research_mixed_next_high_cardinal_whole_sectors.md).
Thus (14) introduces no exponential norm loss beyond the actual
driving polynomial and the explicitly retained endpoint term of
rate \(c_{\mathrm b}/2+\log R\).

## 3. The sharp disk cost of the type-three remaining inverse

For \(\beta=0\), the remaining operator is \(I-\mathcal L\).
It is invertible on degree-\(D\) polynomials because
\(\mathcal L^N=0\). Its exact inverse is
\[
 \mathcal B_N=(I-\mathcal L)^{-1}
     =\sum_{k=0}^{D}\mathcal L^k,\qquad
 \mathcal L^k Z^j
   =\left\{\prod_{\nu=j-k+1}^{j}(1-r^{-\nu})\right\}Z^{j-k}
                       \quad(0\le k\le j).
 \tag{18}
\]
Define
\[
 \Xi(R)=\max_{0\le u\le v\le1}
       \{J(v)-J(u)-(v-u)\log R\},\qquad R>0.
 \tag{19}
\]

**Theorem 3.** For each fixed \(R>0\), the operator norm in
the polynomial function norm satisfies
\[
             \log\|\mathcal B_N\|_{R\to R}
                              =N\Xi(R)+O_R(\log N).
 \tag{20}
\]
If \(R\ge2\), then \(\Xi(R)=0\). If \(0<R<2\), let
\(a_R\in(0,1/2)\) be the unique solution \(2\sin(\pi a_R)=R\).
Then
\[
          \Xi(R)=-2J(a_R)-(1-2a_R)\log R>0.
 \tag{21}
\]
In particular \(\Xi(1)=c_{\mathrm b}\).

*Proof.* Put \(S_j=|P_j|\). The largest absolute monomial transfer
in (18), measured in the radius-\(R\) norm, is
\[
 M_N(R)=\max_{0\le\ell\le j\le D}
                          \frac{S_j}{S_\ell}R^{\ell-j}.
 \tag{22}
\]
Cauchy's coefficient bound on an arbitrary input polynomial gives
\(\|\mathcal B_N\|_{R\to R}\le N^2M_N(R)\).
Conversely, choose the input \(R^{-j}Z^j\). The coefficient of
\(Z^\ell\) in its image is the corresponding product in (18).
Cauchy's coefficient inequality for the image therefore gives
\(\|\mathcal B_N\|_{R\to R}\ge M_N(R)\).
The endpoint-uniform sine-factorial estimate
\(\log S_j=NJ(j/N)+O(\log N)\) proves (20) by (22).
For \(R<2\), the maximizers in (19) are interior and lattice
rounding has bounded logarithmic cost. For \(R\ge2\), every
individual factor in (22) is at most one and \(M_N(R)=1\).

Finally \(J'(t)-\log R=\log(2\sin\pi t/R)\).
For \(R<2\), this is positive precisely on
\((a_R,1-a_R)\). The largest interval integral is its integral
over that complete interval, giving (21) by
\(J(1-t)=-J(t)\). For \(R\ge2\), it is nonpositive and the
maximum is zero. \(\square\)

This is a function-norm obstruction with an explicit monomial
witness; it does not use a hypothetical loss of coherence.
It does not prove that the actual forcing (11) incurs this
worst-case cost.

## 4. Actual output transport and the complete orbit

The ordinary and terminal next-reference rectangles in
[the kernel-margin theorem](research_mixed_next_low_index_kernel_margin.md),
[the last-row domains](research_mixed_actual_last_row_reference_domains.md),
and [the endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
are all contained in the conservative box
\[
        .22\le\Re z\le.49,\qquad -.108\le\Im z\le.068 .
 \tag{23}
\]
For \(Z=e^{-2\pi iz}\), this gives
\[
                         \frac12<|Z|<2,\qquad
                         |1-Z|^2>\frac{21}{20}.
 \tag{24}
\]
Indeed \(.216\pi<\log2\) and \(.136\pi<\log2\), using
\(\pi<22/7\) and the already recorded
\(\log2>842/1215\). Also
\(\cos(2\pi\Re z)\le\sin(3\pi/50)<3\pi/50<1/5\).
Writing \(R=|Z|>1/2\) gives
\(|1-Z|^2=1+R(R-2\cos(2\pi\Re z))>1+1/20\).

For type three the exact equation \(S-\mathcal LS=H\) is
\[
                    S(r^{-1}Z)=(1-Z)S(Z)+ZH(Z).
 \tag{25}
\]
Its backward direction contracts on (23)--(24). This can be
iterated only while the rotated arguments remain in the paid arc
and while the same complete \(H\) is bounded there.
In particular the prescribed scalar
\(S(r^{-1})=a_0\) lies on the unit circle; rotation preserves
radius and does not supply boundary data on another radius.

More decisively, following the whole finite orbit
\(Z_k=r^{-k}Z\) retains the exact identity
\[
 \boxed{\quad
 Z^N S(Z)=\sum_{m=0}^{N-1}
       Z_m H(Z_m)\prod_{h=m+1}^{N-1}(1-Z_h).
 \quad}
 \tag{26}
\]
It follows by iterating (25), using \(S(Z_N)=S(Z)\) and
\(\prod_{k=0}^{N-1}(1-Z_k)=1-Z^N\).
The apparent quotient by \(Z^N\) is removable for the actual
polynomial solution. Its removal is a cancellation of the complete
right side, not a license to discard the complementary orbit.
The exact sharp disk estimate (20) measures this issue without
asserting it is attained by the present source.

For type four, the remaining equation
\((I-\mathcal L_1)S=H\) is exactly
\[
 \begin{split}
 &(1-Z)S(r^{-1}Z)\\
 &\quad=(Z^2+1+r^{-1}-2Z)S(Z)
              -(r^{-1}-Z)S(rZ)-Z^2H(Z).
 \end{split}
 \tag{27}
\]
At fixed \(Z\ne1\), its homogeneous two-state transfer matrix
converges as \(N\to\infty\) to a matrix with eigenvalues
\[
                              1-Z,\qquad (1-Z)^{-1}.
 \tag{28}
\]
On every compact subset of (23), one of these has modulus
strictly larger than one by (24). Hence this entire two-state
transport is not uniformly contracting there. A chosen stable
direction would require control of the actual boundary component;
it does not follow from (24) alone.

Theorem 1 and Corollary 2 therefore remove the outer inverse
as an exponential-loss issue, with its actual homogeneous coefficient
retained. A complete coherent estimate for the remaining outgoing
response on the next-reference domains is still needed. Neither
the ordinary opposite-color evaluation nor the local contracting
arc substitutes for the driving conditional polynomial and complete
orbit in (11), (26), and (27).
