# The actual Gauss first column and its forced meridian-normal sectors

Private written proof, 18 November 2026.

The full finite first column has two different first-normal regimes.
Where its root phase grows, the true meridian normal has that phase
with a nonzero \(N\log N\) multiplier. On the opposite small activity
sector the root column decays exponentially, but its normal, divided
by the original vacuum, tends to \(1/\rho\). The latter is an actual
inhomogeneous contribution. The negative-frequency Fourier aliases,
bottom source and final cap are retained before estimating them.

This is a first-normal theorem at fixed quantum root. It does not
assert a whole meridian-disk asymptotic or estimate the full opposite
kernel, an exterior, or the original closing functional.

## 1. The actual family and the statement

Use the complete directs V and B pinned below. Put
\[
 c_0=2\pi i,\quad Q=e^{c_0/N},\quad q=e^{c_0/(2N)},\quad d=N-1,
 \quad x=-M/q,\quad \mu=\Log M,
\]
\[
 f_j=(Q;Q)_j,\quad g_j(M)=(M^{-2}Q;Q)_j,\quad
 H_j(M)=M^jQ^{-j(j+1)/2}g_j(M).
 \tag{1}
\]
Primes on meridian-dependent finite quantities mean
\(\partial_\mu|_{\mu=0}\), with \(q\) fixed; derivatives of the
activity phase are explicitly with respect to its argument.
For an actual integer degree \(T\le d\), set
\[
 b=d-T,\quad \alpha=b/N\in I\Subset(0,1/2),\quad
 C=Q^b=Q^{-T-1},\quad K_T(M)=M^2C.
 \tag{2}
\]
On the physical basis \(|a,T-a\rangle\), V proves the whole-germ row
\[
 (A_N(M))_{a0}=x^aK_T(M)^dH_d(M)V_a(M),
\]
\[
 V_a(M)=g_T(M)f_{T-a}
 \sum_{n=a}^T
 \frac{M^{-4n}Q^{n(n+1)}}
 {g_n(M)g_{T-n}(M)f_{n-a}f_{T-n}},\qquad 0\le a\le T.
 \tag{3}
\]
In particular every transfer cap is still finite. Define
\[
 \mathcal V_N(\rho,M)=\sum_{a=0}^T V_a(M)\rho^a,\quad
 v_N=V_0(1)=f_T^2/N,
\]
\[
 G_N(\rho)=\mathcal V_N(\rho,1)/v_N,\qquad
 \mathcal H_N(\rho)=\mathcal V_N'(\rho,1)/v_N.
 \tag{4}
\]
The normalization \(v_N\) is fixed when differentiating.

B gives on a fixed disk a holomorphic unit representation
\[
 G_N=e^{N\phi(\rho;C)}A_N^{\mathrm{bd}}(\rho;C),\qquad
 A_N^{\mathrm{bd}}=\mathcal A_G(1+O(N^{-1})),\quad
 G_N(0)=1,\quad \phi'(0)=c_*:=2/c_0.
 \tag{5}
\]
The amplitude and its inverse, with every fixed derivative, are
uniformly bounded on smaller disks. Here B's exact parameter is
\(\sigma_N=(T+1)/N=1-\alpha\). To fix the phase without ambiguity,
let \(Y_B(0)=1\) solve
\[
 CY_B^2-(1+C-\rho)Y_B+1-C\rho=0,\qquad
 Y=\frac{Y_B}{1-\rho}=\exp(c_0D\phi),\quad D=\rho\partial_\rho.
 \tag{6}
\]
All logarithms defining \(\phi\) are zero at the origin.

Fix \(0<\epsilon<1\). After reducing \(r>0\), define the two sectors
\[
 \mathcal S_\pm=\{0<|\rho|<r:
       \ \pm\Re(c_*\rho)>\epsilon |c_*\rho|\}.
 \tag{7}
\]
The plus sector lies around the positive imaginary axis. The
minus sector lies around the negative imaginary axis. Statements
below are uniform on compact subsets of these punctured sectors,
and in \(\alpha\in I\).

For an explicit next coefficient put
\[
 a=C(1-\rho)^2,\quad d_0=1-C\rho,
\]
\[
 \ell_1=-4C(1-\rho)^2Y^2+
       [2C+4-(2C+10)\rho+6\rho^2]Y-2,
\]
\[
 P=-\frac{\ell_1}{aY^2-d_0},\qquad
 W=\frac{(1-C)(2-\rho)}{aY-d_0}.
 \tag{8}
\]
Both denominators equal \(C-1\) at zero. Thus these are
holomorphic on a common small disk, with \(P(0)=2,W(0)=-2\).
Define
\[
 \begin{split}
 \kappa_0(\alpha)&=2\alpha-2+
             \frac{i}{\pi}\log(8\sin^2\pi\alpha),\\
 \kappa(\rho;\alpha)&=\kappa_0(\alpha)
       +\frac2{c_0}\{\gamma+\Log(c_*\rho)\}
       +\frac1{c_0}\int_0^\rho\frac{P(t)-2}{t}\,dt .
 \end{split}
 \tag{9}
\]
The logarithm in the plus sector is the right-half-plane branch.

**Theorem.** For the literal normal (4),
\[
 \boxed{\quad
 \frac{\mathcal H_N}{G_N}
       =\frac{2N}{c_0}\log N+N\kappa(\rho;\alpha)+O(1)
                 \quad\hbox{on }\mathcal S_+,
 \quad}
 \tag{10}
\]
whereas
\[
 \boxed{\quad
 |G_N|\le Ce^{-cN},\qquad
 \mathcal H_N(\rho)=\frac1\rho+O(N^{-1})
                 \quad\hbox{on }\mathcal S_-.
 \quad}
 \tag{11}
\]
All fixed activity derivatives of the errors have the same orders
on smaller compact subsets. In particular both actual normals
are nonzero there for large \(N\). No uniform assertion at
\(N|\rho|=O(1)\), or across the sector boundaries, is made.

## 2. The negative-frequency aliases are present exactly

Let
\[
 P_b(y)=(Qy;Q)_b,\quad R_n(M)=g_n(M^{-1})/g_n(M).
\]
Apply the complementary products in V to (3). The result for every
physical \(a\) is
\[
 V_a(M)=
 \frac{(-1)^aQ^{ab+a(a+1)/2}}{g_b(M^{-1})f_{b+a}}
 \sum_{n=0}^{d}(M^{-6}Q^{-2b})^n R_n(M)
             P_b(M^2Q^n)P_{b+a}(Q^{n-a}).
 \tag{12}
\]
The terms \(n<a\) and \(n>T\) vanish by the last polynomial.
Thus (12) is an exact whole-germ finite reflection, not a
differentiated root-only identity.

Here is its explicit Fourier normal. Write
\[
 \Sigma_j=\sum_{s=1}^j\frac{Q^s}{1-Q^s},\quad
 F(t)=\prod_{s=1}^b(1-Q^{-s}t)^2,\quad
 P_a^*(t)=F(t)(t;Q)_a=\sum_k p_{a,k}t^k,
\]
\[
 Z_0=\sum_{n=0}^{d}(-6n-4\Sigma_n),\qquad
 d_a=\frac{Q^{a(b+1)+b(b+1)}}{f_bf_{b+a}}.
 \tag{13}
\]
Reversing the root polynomial in (12) gives
\[
 V_a(1)=Nd_a p_{a,a},
\]
\[
 \begin{split}
 V_a'(1)=d_a\bigg\{&
 (2N\Sigma_b+Z_0)p_{a,a}
 +N[t^a](2bF-DF)(t;Q)_a\\
 &+\sum_{j=1}^{2b}
          \frac{2N+4j}{1-Q^{-j}}p_{a,a+j}
 +\sum_{s=1}^{a}
          \frac{6N-4s}{1-Q^{s}}p_{a,a-s}\bigg\}.
 \end{split}
 \tag{14}
\]
No division by \(V_a(1)\) is used. To verify (14), the reversed
frequency is \(j=k-a\), so \(-a\le j\le2b\), with no nonzero
multiple of \(N\) in this interval. V's exact finite transforms
give \((2N+4j)/(1-Q^{-j})\) for \(1\le j<N\).
For \(j=-s\), its actual representative is \(N-s\), giving
\((6N-4s)/(1-Q^s)\). This includes the additional
\(4N/(1-Q^s)\); replacing it by a formal negative-index formula
would change the normal. The moving first polynomial in (12)
reverses to \(2bF-DF\), which supplies the second term.
Equations (12)--(14) retain the entire alias source.

## 3. A finite Pearson row, including both ends

It is more efficient to estimate the whole column by its exact
finite recurrence than to estimate the terms in (14) separately.
Put
\[
 \nu_n(M)=(M^{-6}Q^{-2b})^n R_n(M)
                     P_b(M^2Q^n)P_b(Q^n),\quad 0\le n\le T.
 \tag{15}
\]
Then
\[
 \frac{\nu_{n+1}}{\nu_n}
 =M^{-6}Q^{-2b}
 \frac{(1-M^2Q^{b+1}Q^n)(1-Q^{b+1}Q^n)}
 {(1-M^{-2}Q^{n+1})(1-Q^{n+1})}.
 \tag{16}
\]
Let \(m_a=\sum_n\nu_n(Q^n;Q^{-1})_a\). The identity
\(P_{b+a}(Q^{-a}y)=P_b(y)(y;Q^{-1})_a\) gives (12) from these
moments. In the Pearson summation use the polynomial
\((y;Q^{-1})_a/(1-y)\) for \(a\ge1\).
Its value after \(y\mapsto Qy\) is \((y;Q^{-1})_{a-1}\).
The bottom factor \(1-y\) and the top factor
\(1-Q^{b+1}y\) cancel the boundary terms exactly.
Using \(y(y;Q^{-1})_a=Q^a[(y;Q^{-1})_a-(y;Q^{-1})_{a+1}]\)
twice gives
\[
 \alpha_aV_{a+1}+\beta_aV_a+\gamma_aV_{a-1}=0,\quad 1\le a\le T,
 \tag{17}
\]
\[
 \begin{split}
 \alpha_a&=M^{-2}Q^a(1-M^{-2}Q^{a+1})(1-Q^{-b-a-1}),\\
 \beta_a&=1-M^{-2}Q^a-(M^{-4}+M^{-6})Q^{a-b}
                                      +M^{-4}(1+Q)Q^{2a},\\
 \gamma_a&=M^{-6}Q^{a-b}(1-M^2Q^{b+a}).
 \end{split}
 \tag{18}
\]
In particular \(\alpha_T=0\), with no auxiliary outgoing state.

For the bottom equation define only the auxiliary finite moment
\[
 V_{-1}(M)=
 -\frac{Q^{-b}}{g_b(M^{-1})f_{b-1}}
       \sum_{n=0}^T\frac{\nu_n(M)}{1-Q^{n+1}}.
 \tag{19}
\]
All denominators are nonzero since \(T<d\). Using \(1/(1-y)\)
in the same finite summation leaves its missing bottom value:
\[
       \alpha_0V_1+\beta_0V_0+\gamma_0V_{-1}=1-M^{-2}.
 \tag{20}
\]
Indeed its unnormalized value is
\((1-M^{-2})\nu_0=(1-M^{-2})g_b(M^{-1})f_b\).
This term is not zero before differentiation.

Let \(\mathsf T f(\rho)=f(Q\rho)\). Multiplying (17),(20) by
the appropriate powers of \(\rho\) and summing gives
\[
 L_M\mathcal V_N=-QC\left\{
 A_M(1)V_0+\rho(1-M^{-2}-\gamma_0V_{-1})
                    +\rho^{T+2}\gamma_{T+1}V_T\right\},
 \tag{21}
\]
where \(L_M=a_M\mathsf T^2+b_M\mathsf T+d_M\) and
\[
 \begin{split}
 a_M&=M^{-4}C(1-Q\rho)(1-Q^2\rho),\\
 b_M&=-M^{-2}C-M^{-4}
    +Q\rho(M^{-2}C+M^{-4}+M^{-6})-M^{-6}Q^2\rho^2,\\
 d_M&=M^{-2}-QC\rho,\\
 A_M(1)&=M^{-2}Q^{-1}(1-M^{-2})(1-C^{-1}),\\
 \gamma_{T+1}&=M^{-6}Q^{T+1-b}(1-M^2),\quad
 V_T=M^{-4T}Q^{T(T+1)}.
 \end{split}
 \tag{22}
\]
For example, the coefficient of \(\rho^{T+2}\) comes from the
last \(\gamma\) term; it remains explicitly on the right.
This verifies the actual finite top in (21).

## 4. The auxiliary normal and the forced root row

At the root \(V_{-1}(1)=0\): the polynomial
\(P_b(y)^2/(1-Qy)\) has degree \(2b-1<N\) and cannot supply its
selected Fourier coefficient of degree \(2b\). The same fact
kills the moving-polynomial contribution to its derivative.
For a polynomial \(P(t)=\sum p_kt^k\), of degree below \(N\), put
\(\mathcal S_N(P)=\sum_{k\ge1}p_k/(1-Q^{-k})\).
Reversing the remaining polynomial exactly as in (14) gives
\[
 v_{-1,N}:=\frac{V_{-1}'(1)}{v_N}
 =Q^{-b-1}(1-Q^b)
          \left[2\mathcal S_N(P)+\frac4N\mathcal S_N(DP)\right],
 \qquad P(t)=\frac{tF(t)}{1-Q^{-1}t}.
 \tag{23}
\]
The last expression is a polynomial of degree \(2b<N\), not a
meromorphic insertion at its removed factor.

V's exact cotangent formula is
\[
 \mathcal S_N(P)=\frac{P(1)-P(0)}2
 +\frac N{c_0}\int_0^1\frac{P(x)-P(0)}x\,dx
 +\frac N{c_0}\int_0^1
       \frac{x^{N-1}[P(x)-P(1/x)]}{1-x^N}\,dx.
 \tag{24}
\]
The endpoint difference in the final integral stays together.
V proves \(F(x)=\exp[-Nz_Nx+O(Nx^2)]\) near zero, with
\[
 z_N=\frac2N\sum_{j=1}^bQ^{-j},\qquad \Re z_N\ge c>0,
 \tag{25}
\]
and exponential product decay away from zero, including complex
neighborhoods. Removing the one factor in (23) changes these
bounds by at most a polynomial cost: near one
\(|1-Q^{-1}x|^{-1}\le CN\), and the literal remaining product
has the same strictly negative angular integral. Its fixed
derivatives have exponential bounds on smaller neighborhoods.
The reflected product is bounded by \(CNx^{-2b}|F(x)|\).
Since \(N-2b\ge cN\), the reflected integral in (24), including
its endpoint divided difference, is exponentially small.
This also applies to \(DP\).

Now \(P(0)=0\), and the vacuum layer gives
\[
 \mathcal S_N(P)=\frac1{c_0z_N}+O(N^{-1}),\qquad
 \mathcal S_N(DP)=O(e^{-cN}).
 \tag{26}
\]
For the first formula use \(P(x)/x=F(x)/(1-Q^{-1}x)\);
its integral is \(1/(Nz_N)+O(N^{-2})\).
For the second, \(\int_0^1DP(x)/x=P(1)\) is exponentially small.
Substitution into (23), and the exact geometric sum in (25), yields
\[
        v_{-1,N}=-\frac{N(1-Q^{-1})}{c_0}+O(N^{-1})
                        =-1+O(N^{-1}).
 \tag{27}
\]

Write \(a_N,b_N,d_N\) for (22) at \(M=1\). Then \(L_1G_N=0\).
The true coefficient derivatives are
\[
 \dot a_N=-4a_N,\quad
 \dot b_N=2C+4-Q\rho(2C+10)+6Q^2\rho^2,\quad
 \dot d_N=-2.
 \tag{28}
\]
Differentiating the whole finite row (21) gives
\[
 L_1\mathcal H_N=-\dot L\,G_N+S_N(\rho),
 \tag{29}
\]
\[
 \begin{split}
 S_N=-QC\bigg\{&
 2Q^{-1}(1-C^{-1})
 +\rho[\,2/v_N-(C^{-1}-1)v_{-1,N}\,]\\
 &-2Q^{T+1-b}\rho^{T+2}V_T(1)/v_N\bigg\}.
 \end{split}
 \tag{30}
\]
Thus \(S_N(0)=2(1-C)\) exactly. The factor \(1/v_N\) has not
been suppressed. In this chamber it is exponentially small:
\(v_N=NQ^{b(b+1)}/f_b^2\), and V's product bound gives
\(|f_b|^2\le N^Ce^{-cN}\). Hence, on a fixed small disk,
\[
 S_N(\rho)=(1-C)(2-\rho)+O(N^{-1}).
 \tag{31}
\]
The top term in (30) is included in this bound. V also supplies
\[
 \mathcal H_N(0)
 =N\kappa_0(\alpha)+O(1).
 \tag{32}
\]
This subtracts the outside derivative \(2d\) from V's actual
vacuum normal; it is the normalization in (4).

## 5. Exact low-band inversion and whole-cap recovery

Put \(r_N=G_N(Q\rho)/G_N(\rho)\). By (5),
\(r_N=Y+O(N^{-1})\), uniformly analytically on a fixed smaller
disk. If \(U_N=\mathcal H_N/G_N\) and
\(\Delta U_N=U_N(Q\rho)-U_N(\rho)\), direct multiplication gives
\[
 L_1(G_NU_N)
 =G_N\{a_Nr_Nr_N(Q\rho)\Delta U_N(Q\rho)-d_N\Delta U_N\}.
 \tag{33}
\]
No asymptotic factorization was used here.

Choose \(k_N=\lfloor\delta N\rfloor\), with fixed \(\delta>0\)
so small that \(k_N<b,T\), and
\[
       |CQ^n-1|\ge c,\qquad
       |Q^n-1|\ge c n/N\quad(1\le n\le k_N).
 \tag{34}
\]
Solve the following equations through degree \(k_N\):
\[
 \begin{split}
 a_Nr_Nr_N(Q\rho)P_N(Q\rho)-d_NP_N
                                      &=-\dot L G_N/G_N,\\
 a_Nr_N(Q\rho)W_N(Q\rho)-d_NW_N&=S_N.
 \end{split}
 \tag{35}
\]
Take \(P_N,W_N\) to be the resulting truncated polynomials.
Their constant coefficients are exactly \(2,-2\).
For every subsequent coefficient the diagonal multiplier is
\(CQ^n-1\), not the vanishing \(Q^n-1\).
All other coefficient factors vanish at zero. A positive
coefficient bound of the form
\[
 c\,\overline p=B/(1-\rho/R)+K(\rho)\overline p,\qquad K(0)=0,
 \tag{36}
\]
therefore bounds both solutions on a fixed disk, uniformly in \(N\).
Choose its radius so that \(K<c/2\). This is a finite triangular
coefficient argument, and inverts no resonant high multiplier.
Applying the same bound to the errors, using (28),(31) and the
analytic \(Q\)-shift expansion, proves on a smaller disk
\[
       P_N=P+O(N^{-1}),\qquad W_N=W+O(N^{-1}).
 \tag{37}
\]
The principal equations are precisely (8).

Equations (29),(33),(35) show that
\[
 \Delta U_N=P_N+W_N/G_N
                  \quad\text{through degree }k_N.
 \tag{38}
\]
The constant on the right is zero. Indeed the difference of the
two sides solves the first triangular equation with zero right
side through that degree, so (34) forces every coefficient zero.

Here is the needed whole-cap comparison. B's all-index sine
bound is \(e^{-C_1N}\le |f_j|\le e^{C_1N}\), \(j<N\).
Equation (3) and its actual derivative insertion
\(-4n+2(\Sigma_T-\Sigma_n-\Sigma_{T-n})\), with
\(|\Sigma_j|\le C_2N\log(N+1)\), bound every coefficient of
\(G_N,\mathcal H_N\) by \(e^{C_3N}\).
On the root-unit disk (5), \(G_N^{-1}\le Ce^{C_4N|\rho|}\).
Thus \(U_N\), \(P_N+W_N/G_N\), and their low-band antiderivatives
have bounds \(e^{C_5N}\) on a fixed comparison circle.
Cauchy's estimate for their exactly matching first \(k_N+1\)
coefficients now proves
\[
 U_N(\rho)=U_N(0)+
 \sum_{n=1}^{k_N}
 \frac{[\rho^n](P_N+W_N/G_N)}{Q^n-1}\rho^n
                         +O(e^{-BN})
 \tag{39}
\]
on a sufficiently small final disk. The constant \(B>0\) may
be chosen in advance by shrinking that disk. The factor \(O(N)\)
from (34) is harmless. This comparison retains every high
coefficient, the alias row (14), and both boundary terms (30).
It does not set them equal to zero.

## 6. A cancellation-preserving analytic multiplier estimate

We give the estimate used to evaluate (39), including its long
Taylor remainder. Suppose
\[
 F_N(\rho)=e^{N\psi(\rho)}a_N(\rho),\quad
 \psi(0)=0,\quad a_N,a_N^{-1}\text{ uniformly bounded analytic}.
 \tag{40}
\]
The phase and its fixed derivatives are uniformly analytic on
a common disk. Let \(m(z)\) be analytic on a fixed disk about zero.
For sufficiently small fixed \(\delta,r\), with \(k_N=\lfloor
\delta N\rfloor\),
\[
 \sum_{n=0}^{k_N}m(n/N)[\rho^n]F_N\,\rho^n
       =F_N(\rho)\{m(D\psi(\rho))+O(N^{-1})\}.
 \tag{41}
\]
This is uniform on \(|\rho|\le r\), with fixed derivatives.

To prove it, put \(y=D\psi(\rho)\). The exact centered generating
function is
\[
 e^{-ys}F_N(\rho e^{s/N})/F_N(\rho).
 \tag{42}
\]
For \(|s|\le\epsilon_0N\), its modulus is at most
\(C\exp(C|s|^2/N)\); the linear phase cancels. Cauchy on
\(|s|\asymp\sqrt{jN}\) gives centered moments
\[
 M_0=1,\quad M_1=O(N^{-1}),\quad
 |M_j|\le(Cj/N)^{j/2},\quad 2\le j\le\delta_1N.
 \tag{43}
\]
The first moment is \(N^{-1}D\log a_N\).
Expand \(m\) about \(y\) through degree \(L-1\),
\(L=\lfloor\delta_1N\rfloor\), on a disk of fixed radius \(R_0\).
Choose \(|y|<\delta\), \(4\delta<R_0\).
The moment sum of terms of degree at least two is \(O(N^{-1})\):
the majorants \(R_0^{-j}(Cj/N)^{j/2}\) have consecutive ratio
less than \(1/2\) after reducing \(\delta_1\).
The first-degree term has the same order.

For \(n\le k_N\), the Taylor remainder is bounded by
\(C(2\delta/R_0)^L\). On a small comparison circle \(|\rho|=R\),
\(|F_N|\le Ce^{CNR}\) and \(|F_N|^{-1}\le Ce^{CNR}\).
Choose \(R\) small after \(\delta,\delta_1\), so the long
remainder stays exponentially small after summing absolute
coefficients and dividing by \(F_N\).
Replacing truncated moments by the full moments (43) is also
legitimate. Cauchy bounds the omitted coefficient terms by
\[
 Ce^{CNR}\sum_{n>k_N}
       (|\rho|/R)^n(n/N+|y|)^j,\qquad j\le\delta_1N.
 \tag{44}
\]
For \(n\ge\delta N\), the final factor is at most
\(C^j e^{c_1n}\), with fixed \(c_1\).
Reduce \(r/R\) to make (44), including division by \(F_N\),
exponentially small uniformly for all these \(j\).
This proves (41) with the complete remainder and high tail.
The argument also covers uniformly bounded analytic \(a_N\)
with an \(O(N^{-1})\) analytic error.

Apply this with
\[
 m(z)=\frac1{e^{c_0z}-1}-\frac1{c_0z},\qquad m(0)=-1/2.
 \tag{45}
\]
This function is analytic for \(|z|<1\).
Write \(\mathscr F_N=P_N+W_N/G_N\), whose constant is zero.
Equations (39),(45) give
\[
 U_N=U_N(0)+\frac N{c_0}\int_0^1\mathscr F_N(x\rho)\,\frac{dx}{x}
       +\mathcal M_NP_N+\mathcal M_N(W_N/G_N)+O(e^{-BN}),
 \tag{46}
\]
where \(\mathcal M_N\) is the low multiplier (41).
The replacement of the low harmonic sum by its entire integral
has an exponentially small Cauchy tail as in (39).
For \(P_N\), the multiplier is uniformly bounded by its geometric
coefficient bounds. For the other term, \(W_N\) is a uniform
unit near zero by (37), so (41) with \(\psi=-\phi\) gives
\[
 \mathcal M_N(W_N/G_N)
       =\frac{W_N}{G_N}\{m(-D\phi)+O(N^{-1})\}.
 \tag{47}
\]
The zero-degree constants in the two multiplier terms cancel;
neither has been silently removed.

## 7. The two actual normal sectors

Reduce \(r\), depending on \(\epsilon\), so that along each radial
segment in (7) the real part of \(\rho\phi'(x\rho)\) has the
corresponding strict sign, uniformly on enlarged compact sectors.
This follows from \(\phi'(0)=c_*\) and its uniform analyticity.

On \(\mathcal S_+\), let
\(\widetilde F_N=-W_N/(2G_N)\). Its exact value at zero is one.
Its amplitude is a uniformly bounded analytic unit, and
\(\widetilde F_N(x\rho)=
\exp[-N\phi(x\rho)](1+O(x))\) near \(x=0\).
The endpoint comparison with \(\exp[-Nc_*\rho x]\) gives
\[
 \int_0^1\frac{1-\widetilde F_N(x\rho)}x\,dx
          =\log N+\gamma+\Log(c_*\rho)+O(N^{-1}).
 \tag{48}
\]
For completeness, the phase difference near zero is \(O(x^2)\);
after division by \(x\), its integral error is bounded by
\(CN\int_0^\infty xe^{-cNx}dx=O(N^{-1})\).
The amplitude error has the same bound. Away from zero both
comparison terms decay exponentially. The elementary identity
\(\int_0^1(1-e^{-zx})dx/x=\Log z+\gamma+O(e^{-c|z|})\)
on right-half-plane rays follows by differentiating in \(z\)
and fixing the constant with the harmonic-number integral.
Thus the exact value at zero fixes the constant in (48).

Now
\(\mathscr F_N=(P_N-2)+2(1-\widetilde F_N)\).
Use (32),(37),(47),(48) in (46). The multiplier term (47) is
exponentially small in this sector, and the other is \(O(1)\).
This proves (10), including its displayed \(\kappa\).

On \(\mathcal S_-\), (5) gives the exponential bound for \(G_N\).
In (46) the product with \(G_N(\rho)\) of the lower half of the
integral is exponentially small. At its apparent zero endpoint
use the exact difference
\(\mathscr F_N(x\rho)-\mathscr F_N(0)\), or its integral derivative.
The bound is \(CNx\,e^{-N\Re\phi(x\rho)}\); multiplying by
\(G_N(\rho)\) leaves a uniform exponential gap for \(x\le1/2\).
The \(P_N\), \(U_N(0)\) and \(\mathcal M_NP_N\) terms have the
same subordinate property.

Put \(y=D\phi(\rho)\), so \(\Re y<0\) on this compact sector.
At the upper endpoint of the remaining integral, with \(v=1-x\),
\[
 \phi(\rho)-\phi((1-v)\rho)=yv+O(v^2).
 \]
The bounded amplitude ratios and the strict radial decay give
\[
 G_N(\rho)\int_{1/2}^1\frac{W_N(x\rho)}{G_N(x\rho)}\,\frac{dx}{x}
             =-\frac{W_N(\rho)}{Ny}+O(N^{-2}).
 \tag{49}
\]
The proof is the usual direct endpoint comparison:
the amplitude error integrates \(v e^{-cNv}\), and the phase
error integrates \(Nv^2e^{-cNv}\). Multiplying (47) by \(G_N\)
and combining it with (49) yields
\[
 \mathcal H_N
 =W\left[-\frac1{c_0y}+m(-y)\right]+O(N^{-1})
 =\frac{W}{e^{-c_0y}-1}+O(N^{-1}).
 \tag{50}
\]
There is an exact simplification of this leading expression.
The characteristic equation for \(Y=e^{c_0y}\) is
\[
 aY^2+\{-C-1+(C+2)\rho-\rho^2\}Y+d_0=0.
 \]
Consequently
\[
 (aY-d_0)(1-Y)/Y=(1-C)\rho(2-\rho).
 \tag{51}
\]
By (8), \(W/(Y^{-1}-1)=1/\rho\). This proves (11).
Every estimate holds on enlarged compact sectors; Cauchy's
formula gives all asserted fixed activity derivatives.

## 8. Restoring the original column and its source scope

For a fixed physical output evaluation, write
\(\rho=x_0w_1/w_2\), \(x_0=-q^{-1}\).
The exact original column is
\[
 v_{\mathbf w}A_N(M)|0,T\rangle
 =K_T(M)^dH_d(M)w_2^T
             \mathcal V_N(x(M)w_1/w_2,M).
 \tag{52}
\]
Its root vacuum is \(a_{00}=(-1)^dC^df_T^2\).
Since \(H_d'(1)=0\), its true normal, divided by
\(a_{00}w_2^T\), is exactly
\[
              \mathcal H_N+2dG_N+DG_N.
 \tag{53}
\]
Thus in the plus sector its ratio to the root column is
\[
 \frac{2N}{c_0}\log N
       +N\{\kappa(\rho;\alpha)+2+D\phi(\rho)\}+O(1),
 \tag{54}
\]
and in the minus sector the normalized normal (53) is
\(1/\rho+O(N^{-1})\). Both outside scalar and argument derivatives
are present. For \(M=e^{u/N}\), all displayed first normals are
divided by \(N\). No quantum-parameter normal is asserted.

The sector (11) shows why a root-only column unit cannot be
differentiated by holomorphic perturbation without an actual
whole-family estimate: a larger normal sector is turned on.
Our proof does not assume such an estimate. It starts with (3)
and retains its Fourier aliases and finite boundary forcing.
All other factors in the actual routing
\(T=\mathcal B_m(W_\tau^{-1})A_ND_{\rm top}\mathscr C_r\), the
normalization \(J=D_N(MK)^{-1}T\), their derivatives, the original
cut, and the closing finite part remain separate.
No geometric entry into either activity sector, meridian-normal
estimate for a sewn product, or global noncancellation follows.

## Complete directs and author protocol

* **V:** notes/research_actual_gauss_vacuum_meridian_normal.md,
  449 lines, SHA256
  bfe1861c0219f2de8faca263b643508f8c5e4e71e10f1eb51e99c2ba0f20ba5a.
* **B:** notes/research_actual_gauss_first_column_unit.md,
  415 lines, SHA256
  ebe3b496a739d1734738e4b663c7a7fd6713e44549b72ee2e93ae90314a15047.

V supplies the whole actual column, exact finite cotangent integral,
product decay and vacuum normal. B supplies the root column unit
and its actual finite normalization. The full-column recurrence,
alias row, general analytic multiplier and sector estimates are
proved here. The earlier finite-Euler normal and opposite-kernel
notes were coverage reads, not additional imported proof inputs.
Only written mathematics and text/hash operations are used.
The entire matching final and both complete directs were freshly
read nontruncated in this author sequence. Every used implication
was checked and all three hashes renewed. Independent full
matching-final/direct review and parent adoption remain separate.
