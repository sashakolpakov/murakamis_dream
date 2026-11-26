# The actual Gauss vacuum and its first meridian normal

Private written proof, 18 November 2026.

The actual two-tail Gauss vacuum has a nonzero first meridian normal
with the same exponential rate as its root value. Its multiplier is
of order \(N\), not an exponentially larger sector hidden by the root
summation. The proof starts from the whole meridian-dependent matrix
entry. A finite Fourier transform turns its harmonic insertion into
an exact real-interval integral; both its reflected part and its
endpoint divided difference are retained.

This supplies a scalar boundary initialization, not a meridian-normal
theorem for the whole output column or a closed source. The sole
complete direct G supplies the actual ordered operator. Every finite
summation and estimate used below is proved here.

## 1. The whole actual column

Fix
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad c_0=2\pi i,\quad d=N-1,\quad
 f_n=(Q;Q)_n,\quad x=-M/q,\quad \mu=\Log M.
 \tag{1}
\]
The quantum root stays fixed. Put
\[
 g_n(M)=(M^{-2}Q;Q)_n,\qquad
 H_n(M)=\prod_{j=1}^n(MQ^{-j}-M^{-1})
       =M^nQ^{-n(n+1)/2}g_n(M).
 \tag{2}
\]
All products in denominators below have indices less than \(N\),
and are nonzero on a sufficiently small fixed-\(N\) neighborhood
of \(M=1\). Their quotients mean these actual holomorphic germs.

On two remaining heads use the physical degree-\(T\) basis
\(|a,T-a\rangle\), \(0\leq a\leq T\leq d\). Its total Cartan is
\[
 K_T(M)=M^2Q^{-T-1}.
 \tag{3}
\]
G defines \(A_N=q_FE_\Sigma^d i_d\), and proves the exact ordered
formula
\[
 A_N=\sum_{n=0}^{d}
       \frac{Q^{-n}x^{-n}}{f_n}\frac{H_d}{H_n}
                         F^nE^nK^{d-n}.
 \tag{4}
\]
Here \(E=E_1K_2+E_2\), \(F=F_1+K_1^{-1}F_2\), with their actual
missing extreme arrows. Only \(E_2^n\) survives on \(|0,T\rangle\).
In the raising coproduct the term ending at \(|a,T-a\rangle\) is
\(F_1^a(K_1^{-1}F_2)^{n-a}\), with coefficient
\({n\brack a}_Q\). Thus its coefficient in \(F^nE^n|0,T\rangle\) is
\[
 {n\brack a}_Q x^{-(n-a)}
       \frac{f_af_{T-a}}{f_{T-n}}\frac{H_T}{H_{T-n}},
                  \qquad a\leq n\leq T.
 \tag{5}
\]
The rightmost raising factor acts while the first occupation is
zero, which fixes the Cartan power in (5).

Substituting (5) in (4), and using
\(Q^{-n}x^{-2n}K_T^{-n}=M^{-4n}Q^{n(T+1)}\), gives
\[
 \boxed{\quad
 (A_N(M))_{a0}=x^aK_T(M)^dH_d(M)V_a(M),\qquad
 V_a(M)=g_T(M)f_{T-a}
 \sum_{n=a}^{T}
 \frac{M^{-4n}Q^{n(n+1)}}
 {g_n(M)g_{T-n}(M)f_{n-a}f_{T-n}} .
 \quad} \tag{6}
\]
This is a finite original matrix entry, with both caps and its full
normalization. In particular the factor \(M^{-4n}\) is present before
any root simplification.

Write
\[
 \Sigma_n=\sum_{j=1}^n\frac{Q^j}{1-Q^j},\qquad \Sigma_0=0.
 \tag{7}
\]
Since \(g_n'(1)/g_n(1)=2\Sigma_n\), the true \(\mu\)-normal of
the summand in (6) has the insertion
\[
                    -4n+2(\Sigma_T-\Sigma_n-\Sigma_{T-n}).
 \tag{8}
\]
Here and henceforth a prime at one denotes \(\partial_\mu|_{\mu=0}\).
Also \(H_d(M)=(-1)^dD_N(M)\), where
\(D_N(M)=\sum_{j=0}^{d}M^{d-2j}\), so \(H_d'(1)=0\).
Consequently the additional outside derivative in (6) is \(a+2d\).
No root reflection identity has been differentiated in deriving (8).

## 2. Full-orbit reflection of the vacuum

Put
\[
 b=d-T,\qquad \alpha_N=b/N,\qquad
 P_b(y)=\prod_{j=1}^{b}(1-Q^j y).
 \tag{9}
\]
The asymptotic theorem assumes
\[
                  \alpha_N\in I\Subset(0,1/2).
 \tag{10}
\]
This is the strict upper-half degree chamber, with the \(d=N-1\)
offset retained. The following identities also apply whenever
\(2b<N\).

The complementary finite products obey the whole-\(M\) identities
\[
 g_{d-s}(M)=
 \frac{g_d(M)}
 {(-M^{-2})^sQ^{-s(s+1)/2}g_s(M^{-1})},\qquad
 f_{d-s}=\frac{N(-1)^sQ^{s(s+1)/2}}{f_s}.
 \tag{11}
\]
They follow by changing the last \(s\) factors to indices \(-1,\ldots,-s\).
Apply (11) to (6), at \(a=0\). With
\(R_n(M)=g_n(M^{-1})/g_n(M)\), the result is
\[
 \boxed{\quad
 V_0(M)=\frac{1}{g_b(M^{-1})f_b}
  \sum_{n=0}^{d}(M^{-6}Q^{-2b})^n R_n(M)
                      P_b(M^2Q^n)P_b(Q^n).
 \quad} \tag{12}
\]
The original terms have \(n\leq T=d-b\). Every newly displayed term
with \(T<n\leq d\) is exactly zero because \(P_b(Q^n)=0\).
Thus (12) is a whole-germ identity, not a replacement of a finite
cutoff by an infinite series.

At \(M=1\), \(P_b(y)^2\) has degree \(2b<N\). Its leading coefficient
is \(c_{2b}=Q^{b(b+1)}\). The finite Fourier identity therefore gives
\[
 V_0(1)=\frac{NQ^{b(b+1)}}{f_b^2}=\frac{f_T^2}{N},\qquad
 \boxed{(A_N(1))_{00}=(-1)^d(Q^{-T-1})^d f_T^2\ne0.}
 \tag{13}
\]
The factor \(f_b^{-2}\) in (13) remains part of the actual vacuum.
When its logarithmic normal is formed, that same outside factor
cancels from the weighted Fourier quotient. The quotient divides
by \(Nc_{2b}\), not by the exponentially small \(F(1)\).

For the exact normal define
\[
 F(t)=\prod_{j=1}^b(1-Q^{-j}t)^2=\sum_{k=0}^{2b}r_k t^k,
 \quad r_0=1,\quad
 Z_0=\sum_{n=0}^{d}(-6n-4\Sigma_n),
 \tag{14}
\]
and, on polynomials of degree less than \(N\), define
\[
 {\cal S}_N(F)=\sum_{k=1}^{\deg F}\frac{r_k}{1-Q^{-k}},
 \qquad D=t\partial_t.
 \tag{15}
\]
For \(1\leq k<N\), direct finite sums give
\[
 \sum_{n=0}^{d}nQ^{-kn}=-\frac{N}{1-Q^{-k}},\qquad
 \sum_{n=0}^{d}\Sigma_nQ^{-kn}
                         =\frac{N-k}{1-Q^{-k}}.
 \tag{16}
\]
For the second identity, sum (7) in the other order. The numerator
becomes
\(\sum_{j=1}^{d}(Q^{(1-k)j}-Q^j)/(1-Q^j)=N-k\).
This last equality follows by a finite geometric sum; equivalently,
\(\sum_{j=1}^{d}Q^{\ell j}/(1-Q^j)=\ell-(N+1)/2\) for
\(1\leq\ell\leq N\), and its value at \(\ell=0\) is \(d/2\).

Differentiate (12). Its weight derivative is \(-6n-4\Sigma_n\).
The moving first polynomial contributes \(2b\) to the selected
leading coefficient, and the outside denominator contributes
\(2\Sigma_b\). Reversing the coefficients of \(P_b^2\) produces
precisely the \(r_k\) in (14). Equations (16) prove the exact row
\[
 \boxed{\quad
 \frac{(A_N)_{00}'(1)}{(A_N(1))_{00}}
 =2d+2b+2\Sigma_b+\frac{Z_0}{N}
               +2{\cal S}_N(F)+\frac4N{\cal S}_N(DF).
 \quad} \tag{17}
\]
It retains the harmonic zero mode \(Z_0\); discarding it would
give an incorrect logarithmic normal.

## 3. An exact cotangent integral, including its reflected endpoint

For every polynomial \(F(t)=\sum_{k=0}^L r_k t^k\), \(L<N\),
the partial fractions of the cotangent give
\[
 \begin{split}
 {\cal S}_N(F)={}&\frac{F(1)-F(0)}2
   +\frac{N}{c_0}\int_0^1\frac{F(x)-F(0)}x\,dx\\
 &+\frac{N}{c_0}\int_0^1
       \frac{x^{N-1}\{F(x)-F(1/x)\}}{1-x^N}\,dx.
 \end{split} \tag{18}
\]
Indeed
\[
 \frac1{1-Q^{-k}}=\frac12+\frac{N}{c_0k}
 +\frac{N}{c_0}\sum_{\ell\geq1}
       \left(\frac1{k-\ell N}+\frac1{k+\ell N}\right).
 \tag{19}
\]
The paired series is absolutely convergent. Integrating the two
resolvents gives the last integral in (18), since
\(\sum_{\ell\geq1}x^{\ell N-1}=x^{N-1}/(1-x^N)\).
For an elementary proof of (19), integrate
\(\pi\cot(\pi z)/(z^2-y^2)\) around expanding squares whose real
sides pass through half-integers. The cotangent is uniformly bounded
on the contours and the boundary integral is \(O(1/R)\).
The residues at the integers and at \(\pm y\) give
\(\pi\cot(\pi y)=y^{-1}+\sum_{\ell\geq1}
[(y-\ell)^{-1}+(y+\ell)^{-1}]\).
Set \(y=k/N\) and use
\((1-e^{-2\pi i y})^{-1}=1/2-i\cot(\pi y)/2\).
At zero \(L<N\) guarantees integrability. At one the numerator is
its exact divided difference: it vanishes to first order and is
not separated into divergent endpoint integrals.

For the particular \(F\) in (14), the reflected polynomial has,
on \(0<x\leq1\), the exact modulus
\[
                    |F(1/x)|=x^{-2b}|F(x)|.
 \tag{20}
\]
This is a consequence of \(|x-Q^{-j}|=|1-xQ^{-j}|\), not a
bound in a conditioned eigenbasis.

We record the elementary uniform decay used in (18).
For \(\alpha\in I\), put
\[
 \ell_\alpha(x)=\int_0^\alpha
                      \log|1-xe^{-c_0t}|\,dt,\quad 0\leq x\leq1.
 \tag{21}
\]
For \(0<x<1\),
\[
 \partial_x\ell_\alpha(x)
       =\frac{\Arg(1-xe^{2\pi i\alpha})}{2\pi x}<0.
 \tag{22}
\]
The continuous limit at zero is
\(-\sin(2\pi\alpha)/(2\pi)\). The ratio in (22) is uniformly
negative on the indicated compact \(\alpha\)-range and \(0\leq x\leq1\).
Thus \(\ell_\alpha(x)\leq-cx\).

The discrete sum defining \(\log|F(x)|\) differs from
\(2N\ell_{\alpha_N}(x)\) by \(O(\log N)\), uniformly in \(x\).
One elementary verification uses the monotonicity in the angle of
\(\log|1-xe^{i\theta}|\) on \(0\leq\theta\leq2\pi\alpha<\pi\).
All cells except the first are bounded by adjacent integral sums;
the first cell has an integrable logarithmic singularity, with
error \(O(\log N)\), including \(x=1\). For \(x\) in a fixed small
interval at zero, the same comparison has error \(O(x)\), by the
convergent logarithmic power series. In particular
\[
 |F(x)|\leq C e^{-cNx}\quad(0\leq x\leq x_0),\qquad
 |F(x)|\leq N^C e^{-cN}\quad(x_0\leq x\leq1).
 \tag{23}
\]

These estimates also justify the endpoint derivative bounds needed
below. On a fixed small complex neighborhood of any compact
subinterval of \((0,1]\), the product has modulus \(O(e^{-c'N})\).
To see this without choosing a logarithm through its zeros, bound
each logarithm above by
\(\log(|1-xe^{-c_0t}|+\delta)\).
Its integral converges uniformly to (21) as \(\delta\downarrow0\);
choose \(\delta\) first, then use its bounded continuous Riemann
sums. Cauchy on smaller neighborhoods bounds fixed derivatives
by \(O(e^{-c''N})\).

Together with (20) and \(1-2\alpha_N\geq c>0\), this proves
\[
 \int_0^1
  \frac{x^{N-1}\{F(x)-F(1/x)\}}{1-x^N}\,dx=O(e^{-cN}).
 \tag{24}
\]
For \(x\leq1-\delta\), use \(x^{N-2b}\) and (23); the resulting
exponent is strictly negative on the whole interval. Near one,
the exact numerator is \(O((1-x)e^{-cN})\), by the derivative
bound just proved, while \(1-x^N\geq1-x\).
The same argument applies with \(F\) replaced by \(DF\).
For its reflected term differentiate the exact polynomial reflection;
it introduces at most \(2b\) and one derivative. Such polynomial
factors are absorbed by a smaller exponential constant.

## 4. The actual vacuum layer and the normal multiplier

Define the exact finite quantity
\[
 z_N=\frac2N\sum_{j=1}^{b}Q^{-j}.
 \tag{25}
\]
Uniformly under (10), \(\Re z_N\geq c>0\) for all large \(N\).
Near zero,
\[
                  \log F(x)=-Nz_Nx+O(Nx^2).
 \tag{26}
\]
Combining (23),(26), split at a small fixed \(x_0\). On the lower
interval the difference from \(e^{-Nz_Nx}\), divided by \(x\),
has integral \(O(N\int_0^\infty x e^{-cNx}dx)=O(N^{-1})\).
The upper interval is exponentially small in this comparison.
The elementary exponential-integral identity therefore gives
\[
 \int_0^1\frac{F(x)-1}x\,dx
             =-\log N-\gamma-\Log z_N+O(N^{-1}).
 \tag{27}
\]
The logarithm is the right-half-plane branch, and \(\gamma\) is
Euler's constant. The identity for \(e^{-Nz_Nx}\) follows, for
example, by differentiating in \(z_N\), and fixing the constant
on the positive real axis with the harmonic-number integral.

Equations (18),(24),(27) imply
\[
 {\cal S}_N(F)=-\frac12-\frac{N}{c_0}
                  (\log N+\gamma+\Log z_N)+O(1).
 \tag{28}
\]
Applying (18) to \(DF\), whose constant is zero, instead gives
\[
 {\cal S}_N(DF)=-\frac{N}{c_0}+O(e^{-cN}),
 \tag{29}
\]
because \(\int_0^1 DF(x)/x\,dx=F(1)-1\). A polynomial factor in
the exponentially small remainder is absorbed by reducing \(c\).

Here are the other terms in (17), with their branches specified.
Set
\[
 L(t)=\log\!\left(\frac{\sin\pi t}{\pi}\right)+i\pi t,\quad
 \overline L=\int_0^1L(t)\,dt=-\log(2\pi)+\frac{i\pi}{2}.
 \tag{30}
\]
Then elementary Euler--Maclaurin estimates give
\[
 \begin{split}
 \Sigma_b&=-\frac{N}{c_0}
            \{\log N+\gamma+L(\alpha_N)\}+O(1),\\
 \frac{Z_0}{N}&=-3d+\frac{4N}{c_0}
                   \{\log N+\gamma+\overline L\}+O(1).
 \end{split} \tag{31}
\]
For explicit regularization, put \(f(t)=e^{c_0t}/(1-e^{c_0t})\).
The function \(f(t)+1/(c_0t)\) is smooth up to zero on the
first interval, so subtracting the harmonic sum proves the first
formula with an \(O(1)\) remainder. For the second, use
\[
 \sum_{n=0}^{d}\Sigma_n
 =\sum_{j=1}^{d}(N-j)f(j/N)
 =-\frac{N^2}{c_0}{\mathsf H}_d
       +N\sum_{j=1}^{d}a(j/N),\quad
 a(t)=(1-t)f(t)+\frac1{c_0t}.
 \tag{32}
\]
Here \({\mathsf H}_d=\sum_{j=1}^d1/j\).
The function \(a\) extends smoothly to both endpoints,
and integration by parts using \(L'=-c_0f\) gives
\(\int_0^1a=-\overline L/c_0\).
The ordinary endpoint Euler--Maclaurin remainder is \(O(N^{-1})\)
in the sum of this smooth function. After the factors in (32)
are restored, it gives exactly the \(O(1)\) remainder in (31).
The identity \(\int_0^1\log(\sin\pi t)\,dt=-\log2\) follows
by the substitution \(t\mapsto1-t\) and the double-angle formula.
Thus no unproved summation constant is used.

Finally
\[
 z_N=\frac{2(1-e^{-c_0\alpha_N})}{c_0}(1+O(N^{-1})),
 \tag{33}
\]
with the same right-half-plane branch. Substitute (28)--(33)
in (17). All \(\log N+\gamma\) terms cancel. Since
\[
 2\overline L-L(\alpha)
 -\Log\!\left(\frac{2(1-e^{-c_0\alpha})}{c_0}\right)
                  =-\log(8\sin^2\pi\alpha)+i\pi,
 \tag{34}
\]
we obtain the actual normal asymptotic
\[
 \boxed{\quad
 \frac{(A_N)_{00}'(1)}{(A_N(1))_{00}}
 =N\left[\,2\alpha_N+
          \frac{i}{\pi}\log(8\sin^2(\pi\alpha_N))\,\right]+O(1).
 \quad} \tag{35}
\]
The real logarithm in (35) has a positive argument. Uniformity
holds for every compact interval in (10). In particular this
multiplier is an order-\(N\) nonzero unit there, and the actual
vacuum derivative has the same exponential rate as (13).

There is an independent exact sign and nonvanishing check.
At the root the weights in (6), for \(a=0\), are
\[
 w_n=Q^{n(n+1)}{T\brack n}_Q^2
     =e^{2\pi i(T+1)n/N}\,\beta(T,n)^2,
 \tag{36}
\]
where \(\beta(T,n)>0\) is the sine-factorial binomial and
\(\beta(T,n)=\beta(T,T-n)\).
After multiplication by \(e^{-\pi i(T+1)T/N}\), their sum is real
and nonzero by (13). The weighted mean of \(n-T/2\) is purely
imaginary. Also \(\Re\Sigma_j=-j/2\), so
\(\Sigma_T-\Sigma_n-\Sigma_{T-n}\) is purely imaginary and symmetric
under \(n\mapsto T-n\). Its weighted mean is purely imaginary.
Equation (8), together with the outside factor \(2d\), therefore gives
\[
 \boxed{\quad
 \Re\!\left(\frac{(A_N)_{00}'(1)}{(A_N(1))_{00}}\right)=2(d-T).
 \quad} \tag{37}
\]
This confirms the real part of (35) and proves nonvanishing directly.

## 5. Retained source scope

The theorem concerns the derivative of the literal matrix entry (6)
at fixed \(q\), with \(\partial_\mu=\partial_{\Log M}\).
At \(M=1\) it also equals \(\partial_M\).
For the scaled coordinate \(M=e^{u/N}\), the derivative is \(1/N\)
times (35). No uniform whole-\(u\)-disk asymptotic has been inferred
from this first derivative.

The whole first-column formula (6) and insertion (8) remain available,
but (35) does not estimate their generating function on a fixed output
disk. Nor does it estimate other meridian normals, a quantum-parameter
normal, or any exterior braid. In the actual opposite routing
\(T=\mathcal B_m(W_\tau^{-1})A_ND_{\rm top}\mathscr C_r\), every
factor and its derivative must still be retained, followed by the
source normalization \(J=D_N(MK)^{-1}T\). The root sewn product on
nonself weights can vanish, so this vacuum result does not remove
the source finite-part or relative-window comparison.

Complete proof direct:

* G: notes/research_opposite_kernel_forced_cyclic_normalization.md,
  SHA256 42e6d6c3a5039859c241a2832de56301eff49d749db86d67868f3534c89aaaaa.

The complete direct was freshly read nontruncated in this author
sequence. Every used implication was checked. Only written mathematics
and text/hash operations were used. Frozen and public files are unchanged.
