# The actual Jacobi generating polynomial on a uniform Casimir disk

18 November 2026. This is a fixed-root analytic estimate for the literal
continuant columns of [H]. It proves a zero-free generating disk, an
explicit phase and nonzero amplitude, and the actual Casimir-derivative
partner on that disk. The finite last-row forcing is retained throughout.
There is no interpolation of the integer occupation or of the channel.

The parameter \((T+1)/N\) stays in a compact subset of \((0,1)\). In
particular this proof does not apply to \(T=N-1\). It is not a meridian
normal theorem, an estimate for the inverse Clebsch measure, or a claim
about a closed-source coefficient.

## 1. Literal polynomial and the theorem

Put
\[
 c_0=2\pi i,\quad h=c_0/N,\quad Q=e^h,\quad q=e^{h/2},
 \quad d=N-1,\quad x=-q^{-1}.
\]
For \(0\leq T\leq d\), use exactly the Jacobi entries and continuants of
[H, §§1–2]. In a form convenient for the generating row they are
\[
\begin{split}
 A_a&=(Q^{a-T}-1)(1-Q^{a+1}),\qquad 0\leq a<T,\\
 D_a&=2(q+q^{-1}Q^{-T})Q^a
             -(q+q^{-1})Q^{-T}Q^{2a},\\
 p_0&=1,\quad p_1=\lambda-D_0,\quad
 p_{a+1}=(\lambda-D_a)p_a-A_{a-1}^2p_{a-1},\\
 f_a(\lambda)&=\frac{p_a(\lambda)}{A_0\cdots A_{a-1}},
 \qquad f_0=1.
\end{split}                                                     \tag{1}
\]
The expression for \(D_a\) follows by expanding [H, (2)]; its two
constant terms cancel against the two Cartan terms. Define
\[
 L_T(\rho;\lambda)=\sum_{a=0}^T x^{-a}f_a(\lambda)\rho^a,\qquad
 \sigma_N=\frac{T+1}{N},\qquad c=e^{-c_0\sigma_N}=Q^{-T-1}.
                                                                  \tag{2}
\]
Fix a real compact interval \(I\Subset(0,1)\) and a compact Casimir disk
\(\Lambda\Subset\mathbb C\). All estimates below hold for
\(\sigma_N\in I\), sufficiently large \(N\), and \(\lambda\in\Lambda\).
They also hold on a slightly larger Casimir disk when needed for Cauchy
estimates. Constants may depend on these compact sets.

For an auxiliary \(\sigma\) near \(I\), put \(c=e^{-c_0\sigma}\).
Let \(Y(\rho;\lambda,\sigma)\) be the analytic solution, \(Y(0)=1\), of
\[
 (1-\rho)^2(1-Y)(1-cY)+(2-\lambda)\rho=0.              \tag{3}
\]
It exists on a common disk because the \(Y\)-derivative at \(\rho=0\)
is \(c-1\), bounded away from zero. Write \(D=\rho\partial_\rho\), and set
\[
\begin{array}{lll}
 a_0=c(1-\rho)^2,&b_0=-(1+c)(1-\rho)^2,
     &d_0=1-\lambda\rho+\rho^2,\\
 a_1=-3c\rho(1-\rho),&
 b_1=2(1+c)\rho(1-\rho),&
 d_1=\rho^2-\lambda\rho/2.
\end{array}
\]
Define the analytic function \(Z\), with \(Z(0)=0\), by
\[
 Z=-\frac{a_0Y\,DY+a_1Y^2+b_1Y+d_1}{2a_0Y+b_0}.       \tag{4}
\]
Its denominator is again \(c-1\) at zero. Use the logarithm of \(Y\)
equal to zero there, and define
\[
\begin{split}
 \phi(\rho;\lambda,\sigma)
   &=\frac1{c_0}\int_0^\rho\frac{\log Y(t)}t\,dt,\\
 {\cal A}(\rho;\lambda,\sigma)
   &=\exp\left\{\int_0^\rho\frac{Z(t)}{tY(t)}\,dt
                                  -\frac12\log Y(\rho)\right\}.
\end{split}                                                     \tag{5}
\]
Both apparent singularities at zero are removable. Thus
\(\phi(0)=0\), \({\cal A}(0)=1\), and \({\cal A}\) is nonzero.

**Theorem.** There is a radius \(r>0\), independent of \(N,T,\lambda\)
in the stated ranges, such that the actual polynomial (2) is zero-free
on \(|\rho|\leq r\), and
\[
 L_T(\rho;\lambda)
 =e^{N\phi(\rho;\lambda,\sigma_N)}
       {\cal A}(\rho;\lambda,\sigma_N)(1+\epsilon_{N,T}(\rho,\lambda)),
 \qquad |\epsilon_{N,T}|\leq C/N.                    \tag{6}
\]
The relative error is holomorphic on a larger disk than any final
closed disk under consideration. Its fixed \(\rho,\lambda\) derivatives
are \(O(N^{-1})\) on smaller compact sets. In particular
\[
 \partial_\rho\phi(0;\lambda,\sigma)
       =\frac{\lambda-2}{c_0(e^{-c_0\sigma}-1)}.        \tag{7}
\]
The exact shift \(\sigma_N=(T+1)/N\) is part of (6), including its
amplitude. Replacing it by \(T/N\) without expanding the resulting
phase change would alter the displayed amplitude.

## 2. Exact row and its forced partner

Let
\[
 s_b=|(Q;Q)_b|,\quad
 B_T=A_0\cdots A_{T-1}=(-1)^Ts_T^2,\quad
 P_T(\lambda)=\prod_{j=0}^T
               (\lambda-q^{2j+1}-q^{-2j-1}).
                                                                  \tag{8}
\]
The last-row residual in [H] is
\((J_T-\lambda)f=-P_T(\lambda)e_T/B_T\). Summing it with the weights
\(x^{-a}\rho^{a+1}\) and using (1) gives
\[
\begin{split}
 &c(1-Q\rho)(1-Q^2\rho)L_T(Q^2\rho)
 -(1+c)(1-Q\rho)^2L_T(Q\rho)\\
 &\hspace{35mm}
 +(1-q\lambda\rho+Q\rho^2)L_T(\rho)
       =-\frac{q^{T+1}P_T(\lambda)}{s_T^2}\rho^{T+1}.
\end{split}                                                     \tag{9}
\]
For completeness, before multiplication by \(q\) the three
coefficients on the left are respectively
\[
 Q^{-T}q^{-3}(1-Q\rho)(1-Q^2\rho),\quad
 -q^{-3}(Q+Q^{-T})(1-Q\rho)^2,\quad
 q^{-1}-\lambda\rho+q\rho^2.
\]
The right side is \(-P_Tx^{-T}\rho^{T+1}/B_T\).
Since \(x^{-T}=(-1)^Tq^T\), this is exactly (9), with its sign and
top coefficient. All endpoint terms are thus included.

Denote the difference operator on the left of (9) by
\({\cal D}_{T,\lambda}\). Differentiation gives, for \(k\geq1\),
\[
 {\cal D}_{T,\lambda}(\partial_\lambda^k L_T)
 =kq\rho\,\partial_\lambda^{k-1}L_T
       -\frac{q^{T+1}P_T^{(k)}(\lambda)}{s_T^2}\rho^{T+1}.
                                                                  \tag{10}
\]
At a double Casimir node \(P_T'=0\), the \(q\rho L_T\) term remains.
The true partner is not a second homogeneous solution of (9).
Indeed its coefficients are exactly \(x^{-a}f_a'(\lambda)\);
[H, §2] proves that these are the literal confluent Clebsch columns.

## 3. Low-degree analytic control of the ratio

Initially all ratios and logarithms in this section are formal
series at \(\rho=0\); \(L_T(0)=1\) makes them unambiguous. Put
\[
 R_N(\rho)=\frac{L_T(Q\rho)}{L_T(\rho)},\qquad R_N(0)=1,
\]
and
\[
 a_h=c(1-Q\rho)(1-Q^2\rho),\quad
 b_h=-(1+c)(1-Q\rho)^2,\quad d_h=1-q\lambda\rho+Q\rho^2.
\]
Dividing (9) by \(L_T(\rho)\) yields
\[
 a_hR_N(\rho)R_N(Q\rho)+b_hR_N(\rho)+d_h
   =-\frac{q^{T+1}P_T(\lambda)}{s_T^2}
                               \frac{\rho^{T+1}}{L_T(\rho)}.
                                                                  \tag{11}
\]
Choose a small fixed \(\delta>0\) and put \(k_N=\lfloor\delta N\rfloor\).
It can be chosen so that \(k_N<T+1\) and, for all \(1\leq n\leq k_N\),
\[
 |cQ^n-1|\geq b>0,\qquad |Q^n-1|\geq b\,n/N.          \tag{12}
\]
For example first choose \(\delta\) smaller than one fourth of the
distance of \(I\) to the endpoints of \((0,1)\). The arguments
\(n/N-\sigma_N\) then stay away from integers. Decrease \(\delta\)
further below whenever required. The right side of (11) has no
coefficient in these degrees; it has not been set equal to zero
as a function.

Here is a coefficient-majorant proof with a common analytic radius.
Write \(R_N=1+r_N\), \(a_h=c+\alpha_h\),
\(b_h=-(1+c)+\beta_h\). Both \(\alpha_h,\beta_h\) have zero constant
term, with uniformly bounded degree-two coefficients. If \(S f=f(Q\rho)\),
the homogeneous low-degree equation is
\[
 (cS-1)r_N=-(a_h+b_h+d_h)
       -\alpha_hSr_N-(\alpha_h+\beta_h)r_N
       -a_hr_NSr_N.                                \tag{13}
\]
The first term on the right also has zero constant term.
Because \(|Q|=1\), replacing every coefficient by its absolute value
does not change a shift majorant. Division in degree \(n\leq k_N\)
costs at most \(b^{-1}\). A scalar series \(\bar r(0)=0\) solving
\[
 b\bar r=C\frac{\rho}{1-\rho}(1+2\bar r)
                         +\frac{C}{1-\rho}\bar r^2   \tag{14}
\]
with \(C\) enlarged if necessary therefore dominates every coefficient
of \(r_N\) through degree \(k_N\), by induction. The analytic implicit
function theorem at \((\rho,\bar r)=(0,0)\) supplies a common radius.
On a smaller radius \(\bar r<1/2\), so the same coefficient argument
for \(\log(1+r_N)\) gives
\[
 |[\rho^n]\log R_N|\leq C R^{-n},
             \qquad 1\leq n\leq k_N,                \tag{15}
\]
with fixed \(R>0\). The statements are uniform on the enlarged
Casimir disk. They make no assertion about the later coefficients
of the formal ratio, which can detect the top row.

Let \(g_{N,n}=[\rho^n]\log R_N\). The identity
\(\log R_N=\log L_T(Q\rho)-\log L_T(\rho)\) gives the exact low-degree
coefficients
\[
 \ell_N(\rho)=\sum_{n=1}^{k_N}
                    \frac{g_{N,n}}{Q^n-1}\rho^n,\qquad
 [\rho^n]e^{\ell_N}=[\rho^n]L_T\quad(0\leq n\leq k_N).
                                                                  \tag{16}
\]
Equations (12),(15) imply \(|\ell_N(\rho)|\leq CN|\rho|\) on a
fixed smaller disk. Thus \(e^{\ell_N}\) is a genuine analytic unit;
it remains to compare it to the whole finite polynomial.

## 4. The entire finite cap is exponentially small relative to that unit

The continuant recurrence in (1) gives \(|p_a(\lambda)|\leq C^a\),
uniformly on the enlarged Casimir disk: \(|A_a|\leq4\) and
\(|D_a|\leq8\) suffice. Its exact denominator satisfies
\[
 |A_0\cdots A_{a-1}|=\frac{s_a s_T}{s_{T-a}}.           \tag{17}
\]
There is an elementary global constant \(C\) such that
\[
 e^{-CN}\leq s_j\leq e^{CN},\qquad 0\leq j<N.
                                                                  \tag{18}
\]
For the upper bound use \(2\sin(\pi k/N)\leq2\). For the lower bound
use \(2\sin(\pi k/N)\geq4\min(k,N-k)/N\), discard factors at least
one, and sum the remaining negative logarithms. There are at most
two copies of \(\sum_{k\leq N/4}\log(N/(4k))=O(N)\);
the latter bound follows by comparing \(\sum\log k\) with
\(\int_1^n\log t\,dt\). This proves (18), including the endpoints.
Consequently
\[
 |x^{-a}f_a(\lambda)|\leq e^{CN},\qquad0\leq a\leq T. \tag{19}
\]
No individual factorial lower bound of size \(N^{-O(N)}\) is used.

Choose a fixed comparison radius \(R_1<\min(R,1)\). Both \(L_T\)
and \(e^{\ell_N}\) have supremum at most \(e^{C_1N}\) there.
They agree through degree \(k_N\), so the Cauchy coefficient bound
and geometric summation give, for \(|\rho|<R_1\),
\[
 |L_T-e^{\ell_N}|
 \leq 2e^{C_1N}
   \frac{(|\rho|/R_1)^{k_N+1}}{1-|\rho|/R_1}.         \tag{20}
\]
On a final disk of sufficiently small fixed radius \(r_1\), the
factor \(\delta\log(R_1/r_1)\) exceeds \(C_1\) and the cost in
\(|e^{-\ell_N}|\leq e^{CNr_1}\). Hence, for some \(\epsilon>0\),
\[
 L_T=e^{\ell_N}(1+O(e^{-\epsilon N})),
                         \qquad |\rho|\leq r_1.      \tag{21}
\]
The proof works first on a slightly larger disk than any chosen
closed final disk. This proves actual zero-freeness for large \(N\).
In particular the omitted high degrees, and thus the entire original
top forcing, have been estimated as part of the original polynomial.
There is no deletion or alteration of its physical support.

## 5. Actual phase and amplitude with a transported error

Taylor expansion in \(h\), keeping \(c=e^{-c_0\sigma_N}\) exact,
gives \(a_h=a_0+ha_1+O(h^2)\), and the corresponding expansions for
\(b_h,d_h\) recorded above (4). On a fixed common disk the functions
\(Y,Z\) of (3),(4) are analytic and uniformly bounded. Since
\[
 Y(Q\rho)=Y(\rho)+hDY(\rho)+O(h^2),
\]
the analytic approximant \(R_{\rm app}=Y+hZ\) satisfies
\[
 a_hR_{\rm app}(\rho)R_{\rm app}(Q\rho)
              +b_hR_{\rm app}(\rho)+d_h=O(h^2).      \tag{22}
\]
The residual is analytic on a fixed larger disk, has zero constant
term, and its degree-\(n\) coefficients are bounded by
\(C|h|^2R_2^{-n}\). Equation (3) cancels its constant order in \(h\);
(4) cancels the order-\(h\) term, including the shifted \(Y\,DY\).

We spell out the stability step. Subtract (22) from the low-degree
equation (13), and write \(e=R_N-R_{\rm app}\).
The constant diagonal multiplier is still \(cQ^n-1\).
Every other linear coefficient in \(e,Se\) has zero constant term
and a common analytic majorant. The quadratic difference is linear
in the error after writing, for the zero-constant parts,
\[
 r_NSr_N-r_{\rm app}Sr_{\rm app}
       = e\,Sr_N+r_{\rm app}Se.
\]
The known factors on the right have the common majorants from
§3 and the analytic bound for \(R_{\rm app}\). Thus the coefficient
induction is dominated by
\[
 b\,\bar e=C|h|^2\frac{\rho/R_2}{1-\rho/R_2}
                                  +K(\rho)\bar e,\qquad K(0)=0,
                                                                  \tag{23}
\]
where \(K\) is a fixed convergent series with nonnegative coefficients.
Shrinking the radius makes \(K<b/2\). The convergent solution of
(23) proves, through degree \(k_N\),
\[
 |[\rho^n](R_N-Y-hZ)|\leq C|h|^2R_3^{-n}.             \tag{24}
\]
All of this is finite coefficient induction; it does not require an
inverse of the full difference operator at its later resonant degrees.
Taking the logarithm on a smaller disk yields
\[
 g_{N,n}=(\log Y)_n+h(Z/Y)_n+O(|h|^2R_4^{-n}),
                    \qquad1\leq n\leq k_N.          \tag{25}
\]

Decrease \(\delta\) if necessary so \(|hn|\) stays in a fixed small
disk for \(n\leq k_N\). The analytic Bernoulli expansion then gives
\[
 \frac1{Q^n-1}=\frac1{hn}-\frac12+O(|h|n).
\]
Substitution in (16),(25) shows that the degree-\(n\) coefficient of
\(\ell_N\) equals
\[
 \frac{(\log Y)_n}{hn}+\frac{(Z/Y)_n}{n}
             -\frac12(\log Y)_n
                    +O\!\left(|h|(n+1)R_5^{-n}\right).
                                                                  \tag{26}
\]
The error is summable on a fixed smaller disk. The tails above \(k_N\)
of the three analytic main series cost at most
\(CN(r/R_5)^{k_N+1}\), hence are exponentially small after a further
fixed decrease of \(r\). Equations (5),(26) give
\[
 \ell_N=N\phi(\rho;\lambda,\sigma_N)
             +\log{\cal A}(\rho;\lambda,\sigma_N)+O(N^{-1}).         \tag{27}
\]
Together with the exponentially relative estimate (21), this proves
(6). Formula (7) follows by differentiating (3) at zero.
Every normalization in (5) is fixed at zero; no free scalar phase or
amplitude was introduced.

## 6. Genuine Casimir partners and precise scope

The proof was performed on larger complex \(\rho,\lambda\) domains.
Cauchy estimates applied to the holomorphic relative error in (6)
therefore prove its fixed derivative bounds. In particular
\[
 \frac{\partial_\lambda L_T}{L_T}
   =N\partial_\lambda\phi+
                 \partial_\lambda\log{\cal A}+O(N^{-1}),            \tag{28}
\]
and the equivalent normalized transport statement is
\[
 e^{-N\phi}
       (\partial_\lambda L_T-N\phi_\lambda L_T)
                           ={\cal A}_\lambda+O(N^{-1}).             \tag{29}
\]
Here \(\sigma_N,\rho\) are held fixed. Higher fixed Casimir derivatives
follow by the same argument. At any double node of [H], this estimates
the actual partner \(\sum x^{-a}f_a'(\lambda)\rho^a\), including the
inhomogeneous row (10). It does not assert that the partner is
nonzero at every point; for example it vanishes at \(\rho=0\).

There is no branch coalescence in this selected germ at a special
finite value of \(\lambda\), including \(\lambda=-2\). The relevant
nondegeneracy is \(c-1\ne0\), uniform only because \(\sigma_N\) stays
away from \(0,1\). At \(T=d\), \(c=1\), the uniform lower bound for the
degree-one multiplier fails. That case is outside the theorem. These
are fixed-root Casimir derivatives, not \(q\)-derivatives, meridian
derivatives, or derivatives of an interpolated integer channel.

The theorem estimates the actual magnetic generating polynomial.
Applying it to a binomial dual contour still requires that contour's
normalization and saddle estimate. It supplies neither a bound for
the full inverse Hermite frame nor a geometric closing-cycle
coefficient.

## Complete direct and author protocol

The sole complete proof direct is:

- **H:** [actual_complete_casimir_hermite_packet.md](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_complete_casimir_hermite_packet.md),
  321 lines, SHA256
  a4e96738a3a093d963fe13cc03585085951fa8699a506ade4e2e7a47c17b3f4c.

H supplies the literal finite Jacobi block, its complete continuants,
last-row residual and actual confluent partners. All analytic
majorants, high-degree estimates and transported errors used here are
proved in this note. No numerical checks or mathematical programs are
used.

Author freeze protocol: the entire matching final and the sole complete
H direct were read nontruncated in this author sequence, every used
implication was checked, and both file hashes were renewed. Independent
matching-final/direct review and parent adoption remain separate.

