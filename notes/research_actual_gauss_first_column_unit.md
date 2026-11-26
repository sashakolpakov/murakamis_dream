# The actual Gauss first column as a zero-free analytic boundary kernel

18 November 2026. Private written proof.

This note estimates an initialized column of the actual operator \(A_N\)
in [G], including its finite transfer sum, vacuum normalization and both
factorial caps. The result is a full small-disk phase and nonzero
amplitude. It supplies boundary data for a two-variable kernel problem;
it does not estimate that entire kernel or its original closed source.

The quantum parameter and meridian are fixed at completeness. All
occupations remain integers. The chamber is
\((T+1)/N\) in a compact subset of \((1/2,1)\).

## 1. Actual column, normalization and statement

Put
\[
 c_0=2\pi i,\quad h=c_0/N,\quad Q=e^h,\quad q=e^{h/2},
 \quad d=N-1,\quad x=-q^{-1},\quad f_n=(Q;Q)_n.
\]
Take two remaining heads in [G]'s actual \(A_N=q_FE_\Sigma^d i_d\).
On their integer degree \(0\leq T\leq d\), use the physical basis
\(|a,T-a\rangle\), \(0\leq a\leq T\), and put
\[
 H=d-T,\qquad \sigma_N=(T+1)/N,\qquad
 C=Q^H=Q^{-T-1}=e^{-c_0\sigma_N}.
                                                               \tag{1}
\]
Thus the total tail Cartan on this degree is \(K_T=C\). Matrix indices
in this note are physical indices in that basis. Let
\[
 G_T(\rho)=\sum_{a=0}^T x^{-a}\frac{(A_N)_{a0}}{(A_N)_{00}}\rho^a.
                                                               \tag{2}
\]
For \(2T+1\geq N\), its normalization is exactly
\[
                    (A_N)_{00}=(-1)^d C^d f_T^2\ne0.             \tag{3}
\]
In particular \(G_T(0)=1\). If the output evaluation sends
\(|a,T-a\rangle\) to \(w_1^a w_2^{T-a}\), then the actual column is
\[
 v_{\mathbf w}A_N|0,T\rangle
       =(A_N)_{00}w_2^T\,G_T(xw_1/w_2).                          \tag{4}
\]
Any original input binomial coefficient or dual extraction is still
outside (4); it has not been absorbed into the normalization.

Here are the phase and amplitude. For auxiliary
\(\sigma\) near a compact interval \(I\Subset(1/2,1)\), put
\(C=e^{-c_0\sigma}\). Let \(Y(0)=1\) solve
\[
                  CY^2-(1+C-\rho)Y+1-C\rho=0.                 \tag{5}
\]
The derivative in \(Y\) at zero is \(C-1\), uniformly nonzero.
With \(D=\rho\partial_\rho\), define
\[
 Z=-\frac{CY\,DY+\rho Y-C\rho}{2CY-(1+C-\rho)}.                  \tag{6}
\]
Use the logarithms zero at \(\rho=0\), and set
\[
\begin{split}
 \phi_G(\rho;\sigma)
   &=\frac{\operatorname{Li}_2(\rho)}{c_0}
                   +\frac1{c_0}\int_0^\rho\frac{\log Y(t)}t\,dt,\\
 {\cal A}_G(\rho;\sigma)
   &=(1-\rho)^{-1/2}
       \exp\left\{\int_0^\rho\frac{Z(t)}{tY(t)}\,dt
                                     -\frac12\log Y(\rho)\right\}.
\end{split}                                                     \tag{7}
\]
All integrands are regular at zero. These definitions fix
\(\phi_G(0)=0\), \({\cal A}_G(0)=1\).
The dilogarithm in (7) is its power-series germ at zero.

**Theorem.** For each \(I\Subset(1/2,1)\) there is a fixed \(r>0\)
such that, for \(\sigma_N\in I\) and all sufficiently large \(N\),
the literal polynomial (2) is zero-free on \(|\rho|\leq r\) and
\[
 G_T(\rho)=e^{N\phi_G(\rho;\sigma_N)}
               {\cal A}_G(\rho;\sigma_N)(1+O(N^{-1})).           \tag{8}
\]
The relative error is holomorphic, with all fixed \(\rho\)-derivatives
\(O(N^{-1})\) on smaller disks. The amplitude is nonzero. In particular
\[
             \partial_\rho\phi_G(0;\sigma)=2/c_0.               \tag{9}
\]
The accompanying normalization is
\(\partial_\rho\log{\cal A}_G(0;\sigma)=1/(1-C)\).
Indeed (5),(6) give \(Y'(0)=1\), \(Z'(0)=1/(1-C)\);
the exact first coefficient from (16),(17) is
\[
 G_T'(0)=-\frac{Q}{1-Q}
                \left(1+\frac{1-C}{1-QC}\right)
          =\frac{2N}{c_0}+\frac1{1-C}+O(N^{-1}).                \tag{9a}
\]
The phase retains \(\sigma_N=(T+1)/N\) exactly. The theorem neither
interpolates \(T\) nor differentiates a root-reflection formula in the
meridian or quantum parameter.

## 2. Complete finite first-column calculation

For clarity we derive the column from the actual [G, (9)] formula,
rather than selecting a scalar Casimir node. On one complete head,
\[
 Ew_a=(Q^{-a}-1)w_{a-1},\quad
 Fw_a=(1-Q^{a+1})w_{a+1},\quad Kw_a=xQ^{-a}w_a,
\]
with the literal missing bottom/top arrows. The two-head totals are
\(E=E_1K_2+E_2\), \(F=F_1+K_1^{-1}F_2\).
Only \(E_2^n\) survives on \(|0,T\rangle\). The coefficient of
\(|a,T-a\rangle\) in \(F^nE^n|0,T\rangle\), for \(a\leq n\leq T\), is
\[
 {n\brack a}_Q x^{-(n-a)}
 \frac{f_a f_{T-a}}{f_{T-n}}\,
 Q^{-nT+n(n-1)/2}\frac{f_T}{f_{T-n}}.                            \tag{10}
\]
Indeed the ordered coproduct expansion is
\(F_1^a(K_1^{-1}F_2)^{n-a}\) with coefficient \({n\brack a}_Q\);
its right factor acts while the first occupation is zero.

At \(M=1\), [G]'s lowering products are
\(H_n=Q^{-n(n+1)/2}f_n\), \(H_d=(-1)^dN\).
Insert (10) in [G, (9)] and keep the ordered \(K_T^{d-n}\).
The powers \(x^{-2n}=Q^n\), \(K_T^{-n}=Q^{n(T+1)}\)
give exactly
\[
 (A_N)_{a0}=(-1)^dNC^d x^a V_a,\qquad
 V_a=\sum_{n=a}^T Q^{n(n+1)}
                   {T\brack n}_Q{T-a\brack n-a}_Q.              \tag{11}
\]
This is an actual matrix entry with its full scalar.

The finite binomial product, proved by its coefficient recursion, gives
\[
 V_a=Q^{-T(T-1)/2}[t^T]\,
            (-tQ^{T+1};Q)_T\,(-t;Q)_{T-a}.                     \tag{12}
\]
The exponent of the coefficient indexed by \(n\) is
\(n(n+1)+T(T-1)/2\), which verifies every phase in (12).
Since \(2T+1\geq N\), put \(L=T-H=2T+1-N\geq0\). The product in
(12) is identically
\[
 (1-(-t)^N)\,
          \frac{(-t;Q)_L}{(-tQ^{T-a};Q)_{a+1}}.                 \tag{13}
\]
This is an identity of rational functions with polynomial left side.
Only inside \([t^T]\), where \(T<N\), may the first factor in (13)
be replaced by one.

The remaining denominator has the distinct poles
\(t_r=-Q^{-T+r}\), \(0\leq r\leq a\).
If the partial fraction decomposition has a polynomial part, its
degree is at most \(L-a-1<T\), so it has no effect on \([t^T]\).
The numerator at \(t_r\) is
\[
 (Q^{H+1+r};Q)_L
 =\begin{cases}
 \displaystyle
 \frac{N(-1)^{H-r}Q^{(H-r)(H-r+1)/2}}{f_{H-r}f_{H+r}},
                                  &0\leq r\leq H,\\
 0,                               &H<r\leq a.
 \end{cases}                                                     \tag{14}
\]
For the second case the product contains a full-root factor.
For the first use the exact reflection
\[
                  f_{d-b}=\frac{N(-1)^bQ^{b(b+1)/2}}{f_b}.
\]
The other denominator factors evaluated at \(t_r\) have product
\[
             (-1)^{a-r}Q^{-(a-r)(a-r+1)/2}f_r f_{a-r}.
\]
Taking \([t^T]\) of \(1/(1+tQ^{T-r})\), and simplifying these
displayed powers, gives
\[
\begin{split}
 V_0&=f_T^2/N,\\
 \frac{V_a}{V_0}
   &=(-1)^aQ^{a(a+1)/2}f_H^2
       \sum_{r=0}^{\min(a,H)}
          \frac{Q^{r(r-a)}}{f_r f_{a-r}f_{H-r}f_{H+r}}.
\end{split}                                                       \tag{15}
\]
The first line also follows from (12) at \(a=0\); reflection identifies
\((-1)^TQ^{T(T+1)/2}f_T/f_H\) with \(f_T^2/N\).
Equations (11),(15) prove (3).

Define the actual finite polynomials
\[
\begin{split}
 {\cal E}_N(\rho)
   &=\sum_{k=0}^{d}
            \frac{(-1)^kQ^{k(k+1)/2}}{f_k}\rho^k,\\
 B_H(\rho)
   &=\sum_{r=0}^H
       \frac{(Q^{-H};Q)_r(Q^{H+1}\rho)^r}
                         {f_r(Q^{H+1};Q)_r}.
\end{split}                                                       \tag{16}
\]
There are no zero denominators: \(2H\leq d\).
The \(r\)-th coefficient of \(B_H\) is exactly
\[
       \frac{(-1)^rQ^{r(r+1)/2}f_H^2}
                        {f_r f_{H-r}f_{H+r}}.
\]
Writing \(a=r+k\) in (15), the mixed \(rk\) phase cancels.
Thus the exact initialized-column identity is
\[
             \boxed{\quad G_T=
                   \operatorname{trunc}_{\leq T}({\cal E}_N B_H).
                         \quad}                                 \tag{17}
\]
Both finite caps and the final truncation are part of (17).
No noninteger occupation or omitted full-root factor is implicit.

## 3. Exact rows and uniform low-degree logarithms

With \(Sg(\rho)=g(Q\rho)\), coefficient ratios in (16) give
\[
 {\cal E}_N(\rho)-(1-Q\rho){\cal E}_N(Q\rho)
                                      =\rho^N/N,                 \tag{18}
\]
and
\[
 CB_H(Q^2\rho)-(1+C-Q\rho)B_H(Q\rho)
                                    +(1-CQ\rho)B_H(\rho)=0.       \tag{19}
\]
The top term in (18) uses
\((-1)^dQ^{d(d+1)/2}/f_d=1/N\).
In (19) the degree \(H+1\) term vanishes because \(C=Q^H\);
this is the literal terminating equation, not an infinite-series
specialization.

Choose \(k_N=\lfloor\delta N\rfloor\) with small fixed \(\delta>0\).
Uniformly for \(\sigma_N\in I\), it can be chosen so that \(k_N<H\),
\(k_N<T\), and, for \(1\leq n\leq k_N\),
\[
          |CQ^n-1|\geq b>0,\qquad |Q^n-1|\geq b n/N.             \tag{20}
\]
This uses \(H/N=1-\sigma_N\) in a compact subset of \((0,1/2)\).

Initially form \(R_N=B_H(Q\rho)/B_H(\rho)\) as a formal series.
Its exact Riccati equation is
\[
 CR_N(\rho)R_N(Q\rho)
                   -(1+C-Q\rho)R_N(\rho)+1-CQ\rho=0.             \tag{21}
\]
For \(r_N=R_N-1\), this becomes
\[
             (CS-1)r_N=-Q\rho(1-C)-Q\rho r_N-Cr_NSr_N.
                                                                    \tag{22}
\]
In degrees at most \(k_N\), the inverse of \(CS-1\) has coefficient
cost \(b^{-1}\). The quadratic positive majorant
\[
             b\bar r=C_1\rho(1+\bar r)+C_1\bar r^2,
             \qquad\bar r(0)=0
\]
therefore bounds its low coefficients by a common geometric sequence.
The analytic implicit function theorem proves convergence of the
majorant on a fixed disk; on a smaller disk it is less than \(1/2\).
Consequently the low coefficients of \(\log R_N\) also have a common
analytic bound. This is the finite coefficient argument in [U, §3],
with the exact multiplier (20).

Set
\[
 \ell_{B,N}=\sum_{n=1}^{k_N}
       \frac{[\rho^n]\log R_N}{Q^n-1}\rho^n.
\]
Its exponential agrees with \(B_H\) through degree \(k_N\), and
\(|\ell_{B,N}|\leq C_2N|\rho|\) on a fixed disk.
Likewise (18), divided formally by its unit at zero, shows that
\[
 \ell_{E,N}=\sum_{n=1}^{k_N}
                 \frac{Q^n}{n(Q^n-1)}\rho^n                     \tag{23}
\]
is the exact logarithm of \({\cal E}_N\) through that degree.
It too satisfies \(|\ell_{E,N}|\leq C_2N|\rho|\).
By (17), \(e^{\ell_{E,N}+\ell_{B,N}}\) agrees with the actual \(G_T\)
through degree \(k_N\).

## 4. Transport and the full finite-tail comparison

For \(C\) held exact, substitute \(Y+hZ\) into (21).
The constant order in \(h\) is (5); the coefficient of \(h\) is
\[
       [2CY-(1+C-\rho)]Z+CY\,DY+\rho Y-C\rho.
\]
Equation (6) cancels it. On a fixed common disk the residual is
\(O(h^2)\), with zero constant coefficient. Subtract its equation
from (22). All error terms other than \((CS-1)e\) have
zero-constant analytic coefficients; the quadratic difference is
\(e\,Sr_N+r_{\rm app}Se\), times \(C\).
The same positive coefficient majorant as in [U, §5], or directly
\(b\bar e=C_3|h|^2\rho/(R-\rho)+K(\rho)\bar e\) with \(K(0)=0\),
proves
\[
 [\rho^n]\log R_N=(\log Y)_n+h(Z/Y)_n
                         +O(|h|^2R_1^{-n}),\quad n\leq k_N.    \tag{24}
\]
Here one first shrinks the comparison disk so \(K<b/2\).
Thus only finite coefficient inversion below the multiplier wall
has been used.

For \(n\leq k_N\), shrink \(\delta\) if needed and use
\[
 (Q^n-1)^{-1}=(hn)^{-1}-1/2+O(|h|n).
\]
Summation of (24), with the analytic tails above \(k_N\), gives
\[
 \ell_{B,N}
   =\frac{N}{c_0}\int_0^\rho\frac{\log Y(t)}t\,dt
       +\int_0^\rho\frac{Z(t)}{tY(t)}\,dt
                               -\frac12\log Y(\rho)+O(N^{-1}).
                                                                    \tag{25}
\]
For the other factor, \(Q^n/(Q^n-1)=(hn)^{-1}+1/2+O(|h|n)\).
Equation (23) therefore gives
\[
       \ell_{E,N}
       =\frac{N}{c_0}\operatorname{Li}_2(\rho)
                              -\frac12\log(1-\rho)+O(N^{-1}). \tag{26}
\]
All errors are uniform and analytic on a fixed smaller disk.
The \(Q\)-shift in the actual reciprocal Euler factor is essential
for the sign of the one-half logarithm in (26).

It remains to compare with the complete column, not just its low
formal coefficients. The elementary global sine bound proved in
[U, §4] is
\[
                   e^{-C_4N}\leq |f_j|\leq e^{C_4N},
                   \qquad0\leq j<N.
\]
It applies to every index in (16). Hence every coefficient of
\({\cal E}_N\), \(B_H\), their product and its truncation \(G_T\)
is at most \(e^{C_5N}\), increasing \(C_5\) to absorb the finite
convolution sum. On a fixed comparison circle of radius \(R_2<1\),
both \(G_T\) and \(e^{\ell_{E,N}+\ell_{B,N}}\) are bounded by
\(e^{C_6N}\). Their first \(k_N+1\) coefficients agree exactly, so
\[
 |G_T-e^{\ell_{E,N}+\ell_{B,N}}|
 \leq 2e^{C_6N}
       \frac{(|\rho|/R_2)^{k_N+1}}{1-|\rho|/R_2}.                 \tag{27}
\]
Choose the final fixed radius so that
\(\delta\log(R_2/|\rho|)\) beats this exponential constant and
the inverse-unit cost \(e^{C_2N|\rho|}\).
Then (27) is exponentially small relative to the constructed unit.
Combining (25),(26) proves (8), including zero-freeness and every
fixed derivative by Cauchy on smaller disks.

This estimates the full polynomial (17). In particular the three
finite boundaries—the cap of \({\cal E}_N\), the termination of
\(B_H\), and the truncation at \(T\)—were all retained before the
tail estimate. No operator or scalar endpoint was dropped.

## 5. Actual characteristic boundary data and limits

Equation (5) gives \(Y'(0)=1\). The selected logarithmic ratio of
the first-column phase is
\[
          Y_G=\exp(c_0D\phi_G)=\frac{Y}{1-\rho}.                 \tag{28}
\]
For the actual Jacobi characteristic in [U, (3)], define its Casimir
argument by
\[
 \lambda_G(\rho)
 =2+\frac{(1-\rho)^2(1-Y_G)(1-CY_G)}{\rho}.
\]
The expression has a removable singularity at zero. Substituting
(5) gives the exact analytic identity
\[
              \lambda_G(\rho)=C(1+Y(\rho))+\rho,\qquad
              \lambda_G(0)=2C,\quad
              \lambda_G'(0)=1+C.                              \tag{29}
\]
Thus these boundary data are initialized by the actual contracted
operator column. They are not an arbitrarily supplied spectral
leg or a chosen eigenvalue on the physical real channel grid.
For \(I\Subset(1/2,1)\), \(C\ne-1\), so the derivative in (29) is
nonzero on each such compact interval. This is a local
characteristic-projection statement, not a proof of the full
two-variable kernel or a closed-source contour.

Equations (3),(4) keep the actual normalization and the output
monomial. All remaining factors of the opposite kernel in [G, (6)]
remain to be applied. No bound for those factors, meridian normal,
inverse frame, relative closing window or geometric contribution
is inferred here.

## Complete directs and author protocol

- **G:** [research_opposite_kernel_forced_cyclic_normalization.md](research_opposite_kernel_forced_cyclic_normalization.md),
  489 lines, SHA256
  42e6d6c3a5039859c241a2832de56301eff49d749db86d67868f3534c89aaaaa.
- **U:** [research_actual_jacobi_generating_unit.md](research_actual_jacobi_generating_unit.md),
  400 lines, SHA256
  ab3760dd38817c2345c231d8ef67c8a7fa8bb03e3b26d4ef1de1b87182f6728d.

G supplies the actual \(A_N\), its ordered finite formula and its
place in the original opposite kernel. U supplies the proved
finite-coefficient analytic method and the literal Jacobi
characteristic. The column factorization and all phase/amplitude
modifications are proved explicitly here. Only written mathematics
and text/hash operations are used.

Author freeze protocol: the entire matching final and both complete
directs were read nontruncated in this active author sequence, every
used implication was checked, and all three hashes were renewed.
Independent matching-final/direct review and parent adoption remain
separate.

