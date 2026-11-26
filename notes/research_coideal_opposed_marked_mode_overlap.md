# A signed lower bound for the opposed marked mode

24 November 2026. Written research proof.

The original marked boundary has explicit left and right modes in the
coideal height frame. With the same crossing sign their pairing is an
elementary cap slide. With the opposite sign it is a quadratic oscillatory
sum. This note proves that the latter pairing has a positive real part
after one specified, label-independent phase is removed, at every height
and all sufficiently large levels. The lower bound is polynomial.

The estimate also solves the opposite-sign normal equation in the gauge
specified by the original marked row. It does not give a lower bound
for contraction against an arbitrary coherent exterior or for the
original closed knot scalar.

## 1. Actual modes, source factors and the statement

Use the complete conventions of [N,C,H,S,K]:
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \delta=\pi/N,\quad\theta=\delta/2,\quad c=1+q,\quad
 \kappa=q^{d^2/2},\quad F_a=(Q;Q)_a .
 \tag{1}
\]
All fractional powers have these exponential branches. The distinct
coideal roots are \(\mu_j=Q^j+qQ^{-j}\), \(0\le j<N\).
They are a permutation of
\(\lambda_r=2\sqrt q\cos((r+\tfrac12)\delta)\).
The continuants, their trailing minor and their generating polynomial are
\[
 \begin{split}
 D_{-1}&=0,\qquad D_0=1,\\
 D_{a+1}(\lambda;\rho)
   &=(\lambda+qQ^a\rho)D_a(\lambda;\rho)
                         -q(1-Q^a)^2D_{a-1}(\lambda;\rho),\\
 \Phi_{\lambda,\rho}(z)
   &=\sum_{a=0}^dD_a(\lambda;\rho)z^a/F_a,\qquad
 E_d(\lambda;\rho)=\text{trailing continuant}.
 \end{split}                                                   \tag{2}
\]
Here \(F_d=N\), and \(p_N\) is the monic polynomial with roots \(\mu_j\).
No denominator \(F_a\) with \(a\ge N\) is used.

Fix \(\rho=\mu_l\), put \(m=\lfloor N/2\rfloor\), and set
\[
 t(j)=
 \begin{cases}[m-j]_N,&N\text{ even},\\[m+j]_N,&N\text{ odd},
 \end{cases}
 \qquad I_l=\{j:l\le t(j)\le d\}.
 \tag{3}
\]
The actual marked row and right mode from [N] are
\[
 r_{l,j}=\Phi_{\mu_j,\rho}(-q),\qquad
 s_{l,j}=\kappa\,\frac{E_d(\mu_j;\rho)}{p_N'(\mu_j)}\,r_{l,j}.
 \tag{4}
\]
Both vanish off \(I_l\). The rows and columns below use these raw
height coordinates and their counting Euclidean norm.
If \(B^\pm_{c,\rho}\) are the actual crossing matrices in this unchanged
frame, [N,S] give
\[
 B^-=\overline{B^+}=(B^+)^{-1},\qquad
 s_l=B^+e_*,\qquad
 r_ls_l=\frac{2\kappa}{1-q^3},\qquad
 \mu_*=-q^{-1}-q^2 .
 \tag{5}
\]
The star labels the root \(\mu_*\), not an adjoint.

The new scalar is the literal opposed-mode coefficient
\[
 \boxed{\quad
 \gamma_l=r_lB^-e_*=r_l\overline{s_l}
    =\bar\kappa\sum_{j\in I_l}
       \overline{\frac{E_d(\mu_j;\rho)}{p_N'(\mu_j)}}\,|r_{l,j}|^2 .
 \quad}                                                        \tag{6}
\]
For example, the cap-straddling boundary row of [C] is
\(\beta_Nr_l\), where its original factor satisfies
\[
 \beta_N=\frac{T_*}{A_c}\frac{\kappa(1-q)}2,\qquad
 |\beta_N|=\frac1{N^2\sin3\theta}\asymp N^{-1}.
 \tag{7}
\]
Its opposed coefficient is \(\beta_N\gamma_l\).
Any original external scalar \(\chi_N\) is retained as a further factor.

**Theorem.** There are universal constants \(N_0,c_0,C>0\) such that
for every \(N\ge N_0\) and every \(0\le l<N\),
\[
 \boxed{\qquad
 \operatorname{Re}(\kappa\gamma_l)\ge c_0N^{-3},
 \qquad c_0N^{-3}\le|\gamma_l|\le CN^4 .
 \qquad}                                                       \tag{8}
\]
Consequently \(|\beta_N\gamma_l|\ge c_0N^{-4}\).
The phase removed in the real-part inequality is the same for all labels.
For nonnegative real numbers \(a_l\),
\[
 \operatorname{Re}\!\left(\kappa\sum_l a_l\gamma_l\right)
                        \ge c_0N^{-3}\sum_l a_l .               \tag{9}
\]
This last assertion assumes those actual nonnegative coefficients;
it does not assign that sign to an arbitrary attached packet.

On any fixed bulk interval \(\varepsilon N\le l\le(1-\varepsilon)N\),
the more precise, uniform estimate is
\[
 \kappa\gamma_l=
 \frac{1}{2\sin^2((l-\tfrac12)\delta)}
                  \bigl(1+O_\varepsilon(N^{-1/2})\bigr).
 \tag{10}
\]
The error in (10) is complex. In particular the principal amplitude
is positive and has zero exponential rate.

## 2. Exact reduction to one quadratic tail

The cumulative kernel of [C] supplies
\[
 U_t=\prod_{k=1}^t\frac{1-Q^{-k}}{1-q^{2k-1}},\quad U_0=1,\qquad
 V_l=\frac2{U_l(1-q^{2l-1})},\qquad W_t=|U_t|^2 .
 \tag{11}
\]
Thus \(r_{l,j}=\overline{U_{t(j)}V_l}\) on \(I_l\), and
\[
 W_t=\prod_{k=1}^t
       \frac{\sin^2(k\delta)}{\sin^2((k-\tfrac12)\delta)},\qquad
 1\le W_t\le CN,\qquad |V_l|^2\ge c_0/N .
 \tag{12}
\]
The endpoint \(l=0\) still has the denominator \(1-q^{-1}\) in \(V_0\).
It is not replaced by a missing factor.

We record the phase needed from the continuants, rather than using
their modulus alone. On the selected support, write \(t=t(j)\),
\(A=t-l\), \(B=d-A\). The exact finite product is
\[
 \Phi_{\mu_j,\mu_l}(z)
       =(-qQ^lz;Q)_A(-q^2Q^{-l}z;Q)_B .
 \tag{13}
\]
Its leading coefficient is
\[
 \frac{D_d(\mu_j;\mu_l)}N
 =q^{A^2+B^2+B+2l(A-B)}
 =(-1)^d q^{2t^2+t-2l^2+l}.
 \tag{14}
\]
For the second equality substitute \(A=t-l\), use \(d=N-1\),
and remove the integer multiple \(2Nt\) from the exponent.
This computation works at both level parities.
The cyclic derivative of
\(p_N(s+q/s)=s^N-s^{-N}\), at \(s^N=1\), similarly gives
\[
 p_N'(\mu_j)=(-1)^N\frac{2NQ^t}{qQ^{2t}-1}.
 \tag{15}
\]
Indeed \(Q^j=-Q^{-t}\) at even \(N\), and \(Q^j=-qQ^t\) at odd \(N\).

Continuant reflection gives
\(E_d=q^d\overline{D_d}\), while
\(\overline{p_N'}=q^{-d}p_N'\) on these roots. Hence
\(\overline{E_d/p_N'}=D_d/p_N'\).
Equations (6),(11),(14),(15) now give the exact identity
\[
 \boxed{\quad
 \gamma_l=\bar\kappa\,\frac{|V_l|^2}{2}\,\overline{E_l}\,H_l,
 \qquad E_t=q^{2t^2-t},\qquad
 H_l=\sum_{t=l}^d(E_t-E_{t+1})W_t,\qquad E_N=-1 .
 \quad}                                                        \tag{16}
\]
Here \(q^{-2l^2+l}=\overline{E_l}\) is precisely the phase that
arises from (14); it is not an independently chosen row rephasing.
In particular
\[
 \operatorname{Re}(\kappa\gamma_l)
          =\frac{|V_l|^2}{2}\operatorname{Re}(\overline{E_l}H_l).
 \tag{17}
\]
The problem is therefore a signed scalar tail with all endpoint factors kept.

## 3. An exact positive identity on the decreasing half

The ratio \(W_t/W_{t-1}\) crosses one once. More precisely \(W_t\)
increases up to \(t=m\) and decreases thereafter. Its endpoint is
\[
                         W_d=N^2\sin^2\theta\ge1 .
 \tag{18}
\]
For \(l\ge m\), put \(a_t=W_{t-1}-W_t\ge0\), \(t>l\).
Summation by parts in (16) gives
\[
 \operatorname{Re}(\overline{E_l}H_l)
   =\frac{W_d}{2}|1+E_l|^2
       +\frac12\sum_{t=l+1}^d a_t|E_t-E_l|^2 .
 \tag{19}
\]
To verify the constants, before taking the real part the same identity is
\(H_l=E_lW_l+W_d-\sum_{t>l}a_tE_t\);
use \(W_l=W_d+\sum_{t>l}a_t\).

For \(N\ge3\), the last decrement satisfies
\[
 a_d=W_d\,\frac{\sin5\theta\,\sin\theta}{\sin^22\theta}
                                                     \ge\frac14 .
 \tag{20}
\]
Here \(\theta\le\pi/6\), \(\sin5\theta\ge\sin\theta\), and
\(\sin2\theta\le2\sin\theta\).
If \(l<d\), retain only the first and last terms in (19).
Since \(E_d=-q^3\), the triangle inequality gives
\[
 \operatorname{Re}(\overline{E_l}H_l)
 \ge\frac1{16}|1+E_d|^2
 =\frac1{16}|1-q^3|^2\ge\frac1{4N^2}.
 \tag{21}
\]
The same bound follows directly from (19) for \(l=d\).
At \(N=2\), \(m=d=1\), and the only decreasing-half tail
has \(\operatorname{Re}(\overline{E_1}H_1)=2\).
Thus (21) holds on this half at every level, after no finite-level exclusion.

## 4. Uniform Wallis estimates and the Abel reduction

For the other half we first prove, uniformly over every \(0\le t<N\),
\[
 \boxed{\quad
 W_t=N\sin(t\delta)+O(1),\qquad
 W_t-W_{t-1}=\pi\cos(t\delta)
                    +O\!\left(\frac1t+\frac1{N-t}\right)
                  \quad(1\le t<N).
 \quad}                                                        \tag{22}
\]
These estimates do not treat the two endpoints as bulk points.

For \(1\le t\le N/2\), let
\[
 W_t^{(0)}=\prod_{k=1}^t\left(\frac{k}{k-\tfrac12}\right)^2,
 \qquad f(x)=\log(\sin x/x),\quad f(0)=0.
 \tag{23}
\]
The elementary Wallis bounds are
\(\pi t\le W_t^{(0)}\le\pi(t+\tfrac12)\).
For completeness, if \(I_n=\int_0^{\pi/2}\sin^n x\,dx\), then
\(I_{2t}=\pi/(2\sqrt{W_t^{(0)}})\),
\(I_{2t+1}=\sqrt{W_t^{(0)}}/(2t+1)\), and
\(I_{2t-1}=\sqrt{W_t^{(0)}}/(2t)\).
The inequalities \(I_{2t+1}\le I_{2t}\le I_{2t-1}\) prove the bounds.

On \([0,\pi/2]\), \(f''\) is bounded. Comparing the two halves
of each interval of length \(\delta\) gives
\[
 2\sum_{k=1}^t
       [f(k\delta)-f((k-\tfrac12)\delta)]
                          =f(t\delta)+O(N^{-1}).
 \tag{24}
\]
Indeed each difference from
\(f(k\delta)-f((k-1)\delta)\) is \(O(\delta^2)\), and there are
at most \(N/2\) intervals.
Therefore \(W_t=W_t^{(0)}e^{f(t\delta)+O(1/N)}
=N\sin(t\delta)+O(1)\) on this half.
It also gives \(W_t=N\sin(t\delta)(1+O(1/t))\) for \(t\ge1\).

The exact reflection identity is
\[
                   W_tW_{d-t}=N^2\sin^2((t+\tfrac12)\delta).
 \tag{25}
\]
It follows by reversing the full sine products in (12).
For \(s=d-t\ge1\), insert the preceding lower-half estimate for \(W_s\).
The relative error \(O(1/s)\) contributes only \(O(1)\), since
\(\sin((s+\tfrac12)\delta)/\sin(s\delta)\) is bounded.
Use also
\[
 \sin^2((s+\tfrac12)\delta)
       -\sin(s\delta)\sin((s+1)\delta)=\sin^2\theta .
 \tag{26}
\]
This proves the first estimate in (22) on the upper half as well.
For \(s=0\), (18) gives the required \(O(1)\) endpoint bound directly.

For the difference estimate use the exact formula, \(x=t\delta\),
\[
 W_t-W_{t-1}
       =W_t\,\frac{\sin\theta\,\sin(2x-\theta)}{\sin^2x}.
 \tag{27}
\]
Substitute the first estimate of (22).
Its main term is \(\pi\cos x+O(1/(N\sin x))\), since
\(N\sin\delta=\pi+O(N^{-2})\).
The \(O(1)\) remainder contributes
\(O((N\sin x)^{-1}+(N\sin x)^{-2})\), using
\(|\sin(2x-\theta)|\le2\sin x+\sin\theta\).
Finally \(N\sin(t\delta)\ge c_0\min(t,N-t)\), proving (22).

Abel summation, \(W_d=O(1)\), and the summable error in (22) yield
\[
 H_l=E_lW_l+\frac\pi2\sum_{t=l+1}^d(A_t+B_t)+O(\log N),
 \quad
 A_t=e^{2\pi it^2/N},\quad B_t=e^{2\pi i(t^2-t)/N}.
 \tag{28}
\]
Indeed \(E_t\cos(t\delta)=(A_t+B_t)/2\).
The constant in this error is universal, including \(l=0,d\).

## 5. Quadratic sums with their exact common phase

We need two elementary facts:
\[
 \sup_{a\le b}\left|\sum_{t=a}^b A_t\right|
 +\sup_{a\le b}\left|\sum_{t=a}^b B_t\right|\le C\sqrt N,
 \qquad 0\le a\le b<N,
 \tag{29}
\]
and
\[
 \sum_{t=0}^{N-1}A_t+\sqrt q\sum_{t=0}^{N-1}B_t
                        =(1+i)\sqrt N .
 \tag{30}
\]
We include the phase proof because a modulus estimate alone is insufficient.

For (29), the consecutive phase increments are
\(2\pi(2t+1)/N\) and \(4\pi t/N\), respectively.
Remove intervals of \(O(\sqrt N)\) indices around their at most
three aliases \(0,2\pi,4\pi\). Their contribution is \(O(\sqrt N)\).
The remaining \(O(1)\) intervals have monotone phase increments modulo
\(2\pi\), at distance at least \(c_0/\sqrt N\) from \(2\pi\mathbb Z\).
For \(z_t=e^{i\phi_t}\), write
\[
 z_t=d_t(z_t-z_{t+1}),\qquad
 d_t=(1-e^{i(\phi_{t+1}-\phi_t)})^{-1}
     =\tfrac12+\tfrac i2\cot((\phi_{t+1}-\phi_t)/2).
 \tag{31}
\]
On each such interval \(\sup|d_t|+\operatorname{Var}(d_t)\le C\sqrt N\).
Summation by parts proves (29), for every truncated subinterval too.
This argument has no logarithmic loss.

To prove (30), first set
\(G(M)=\sum_{n=0}^{M-1}e^{2\pi in^2/M}\), \(M=4N\).
For \(\epsilon>0\), group the absolutely convergent sum
\[
 S_\epsilon=\sum_{n\in\mathbb Z}
              e^{-(\epsilon-2\pi i/M)n^2},\qquad
 \lim_{\epsilon\downarrow0}\sqrt\epsilon\,S_\epsilon
                              =\frac{\sqrt\pi}{M}\,G(M).
 \tag{32}
\]
The asymptotic follows separately on each residue class modulo \(M\)
from the ordinary Gaussian Riemann sum.
Gaussian Fourier transformation and periodization give, exactly,
\[
 S_\epsilon=
 \sqrt{\frac{\pi}{\epsilon-2\pi i/M}}\,
 \sum_{k\in\mathbb Z}
       \exp\!\left(-\frac{\pi^2k^2}{\epsilon-2\pi i/M}\right).
 \tag{33}
\]
All square roots are continued from the right half-plane.
This identity follows by integrating the Gaussian Fourier transform
and summing its absolutely convergent Fourier series; it first holds
for positive real Gaussian parameter and then by analyticity for
positive real part.

Put \(a=2\pi/M\). The exponent in the last sum is
\[
 -b_\epsilon k^2-i\pi Mk^2/2+i c_\epsilon k^2,\qquad
 b_\epsilon=\frac{\pi^2\epsilon}{\epsilon^2+a^2}
                  \sim M^2\epsilon/4,\quad
 c_\epsilon=\frac{\pi^2\epsilon^2}{a(\epsilon^2+a^2)}
                  =O_M(\epsilon^2).
 \tag{34}
\]
The middle exponential is one because \(M\) is divisible by four.
Replacing \(e^{ic_\epsilon k^2}\) by one costs at most
\(O_M(\epsilon^2\sum k^2e^{-b_\epsilon k^2})=O_M(\sqrt\epsilon)\).
The remaining sum is asymptotic to
\(2\sqrt\pi/(M\sqrt\epsilon)\), and the prefactor tends to
\((1+i)\sqrt M/2\).
Comparison with (32) proves the exact phase
\[
                         G(4N)=(1+i)\sqrt{4N}.
 \tag{35}
\]
Here \(N\) was fixed during the auxiliary \(\epsilon\) limit,
so no uniform regularization error has been assumed.

The even terms of \(G(4N)\) equal twice the full \(A\) sum.
The odd terms equal twice \(\sqrt q\) times the full \(B\) sum
(replace \(t\) by \(-t\) in the odd quadratic). This proves (30).
Finally difference orthogonality gives
\[
 \left|\sum_{t=0}^{N-1}B_t\right|^2
  =N\sum_{\substack{0\le h<N\\2h=0\ {\rm mod}\ N}}
                   e^{2\pi i(h^2-h)/N}\le2N .
 \tag{36}
\]
The expression is real and nonnegative before the last bound.
Since \(1-\sqrt q=O(N^{-1})\), (30),(36) imply the parity-free formula
\[
             \sum_{t=0}^{N-1}(A_t+B_t)
                     =(1+i)\sqrt N+O(N^{-1/2}).
 \tag{37}
\]
These are the classical Gaussian-Poisson mechanisms, with the exact
normalization needed here; see the primary coverage in
[DLMF 20.11(i)](https://dlmf.nist.gov/20.11#i).

## 6. The endpoint symbol is uniformly positive

Equations (28),(29) first show, uniformly in every label,
\[
                         H_l=E_lW_l+O(\sqrt N).
 \tag{38}
\]
For \(l\) in a bounded square-root layer put \(a=l/\sqrt N\).
For each fixed \(A>0\), ordinary Riemann sums give, uniformly for \(0\le a\le A\),
\[
 \frac1{\sqrt N}\sum_{t=0}^l(A_t+B_t)
          =2\int_0^a e^{2\pi ix^2}\,dx+O_A(N^{-1/2}).
 \tag{39}
\]
The derivative of the fixed-interval integrand is bounded.
Also \(B_t/A_t=e^{-2\pi it/N}=1+O_A(N^{-1/2})\) on this range,
whose accumulated normalized error is \(O_A(N^{-1/2})\).
Together with (22),(28),(37), this proves
\[
 \frac{H_l}{\sqrt N}
 =\pi\left[
       a e^{2\pi ia^2}+C_F+I(a)\right]
                    +O_A\!\left(\frac{\log N}{\sqrt N}\right),
 \quad C_F=\frac{1+i}{4},\quad
 I(a)=\int_a^\infty e^{2\pi ix^2}\,dx .
 \tag{40}
\]
The Fresnel integral has its usual improper meaning.
Its value \(I(0)=C_F\) follows by letting the positive real part
of the Gaussian parameter tend to zero. Integration by parts
controls the improper tail in that limit.
Definitions and the classical values are recorded in
[DLMF 7.2(iii)](https://dlmf.nist.gov/7.2#iii).

The real symbol after the actual phase is removed is
\[
 \mathcal F(a)=
       a+\operatorname{Re}(e^{-2\pi ia^2}C_F)
                     +\operatorname{Re}(e^{-2\pi ia^2}I(a)).
 \tag{41}
\]
It obeys the explicit lower bound
\[
                 \mathcal F(a)\ge
                    \frac{2-\sqrt2}{6}(1+a)>0
                              \qquad(a\ge0).
 \tag{42}
\]
Here is a direct proof of the sign, including the oscillatory tail.
Rotation along a quadrant centered at \(a\) gives
\[
 e^{-2\pi ia^2}I(a)
            =i\int_0^\infty e^{-4\pi ay}e^{-2\pi iy^2}\,dy .
 \tag{43}
\]
For \(a>0\) the vertical integral is absolutely convergent; the
connecting quarter-circle tends to zero, since its magnitude is
\(\exp[-4\pi aR\sin u-2\pi R^2\sin2u]\).
At \(a=0\) use the improper limit, or the same endpoint arc estimate.
Consequently the last real term of (41) is
\[
 T(a)=\int_0^\infty e^{-4\pi ay}\sin(2\pi y^2)\,dy>0 .
 \tag{44}
\]
Indeed \(u=2\pi y^2\) turns it into a positive constant times
\(\int_0^\infty u^{-1/2}e^{-2\sqrt{2\pi}a\sqrt u}\sin u\,du\).
The weight is strictly decreasing. Pairing successive positive
and negative half-periods gives a strictly positive sum, with
convergence by Dirichlet's test. This includes \(a=0\), where
the value is \(1/4\).

For \(0\le a\le1/2\),
\(\operatorname{Re}(e^{-2\pi ia^2}C_F)
=(\cos(2\pi a^2)+\sin(2\pi a^2))/4\ge1/4\).
For \(a\ge1/2\), its absolute value is at most \(\sqrt2/4\).
Thus \(\mathcal F(a)\ge a+1/4\) on the first range and
\(\mathcal F(a)\ge a-\sqrt2/4\) on the second.
These two inequalities imply (42).

Since \(E_l=e^{2\pi ia^2}(1+O_A(N^{-1/2}))\), (40) gives
\[
 \frac{\operatorname{Re}(\overline{E_l}H_l)}{\sqrt N}
            =\pi\mathcal F(a)
                       +O_A\!\left(\frac{\log N}{\sqrt N}\right).
 \tag{45}
\]
The error is uniform on every fixed compact \(a\)-interval.
This uniformity, rather than a pointwise endpoint limit, is used next.

## 7. Joining the ranges and the bulk amplitude

For \(1\le l\le m\), the lower-half proof of (22) also gives
\(W_l\ge c_1l\), with a universal \(c_1>0\).
Choose a fixed \(A\) larger than twice the constant in (38) divided
by \(c_1\). Then (38) implies
\[
 \operatorname{Re}(\overline{E_l}H_l)\ge c_2\sqrt N
                         \qquad(A\sqrt N\le l\le m).
 \tag{46}
\]
On \(0\le l\le A\sqrt N\), (42),(45) give the same lower bound
for all sufficiently large \(N\), uniformly in \(l\).
This includes \(l=0\). The threshold depends only on the fixed
universal \(A\); it is independent of the selected channel.

Thus the entire left half has a positive lower bound \(c_2\sqrt N\)
eventually. The exact right-half estimate (21) gives \(1/(4N^2)\).
Use (12),(17) to obtain (8) at every label.
The upper bound in (8) also follows directly from (6), since
[N] gives \(\|r_l\|_2,\|s_l\|_2\le CN^2\).
Multiplication by the exact nonzero factor (7) proves the stated
original-boundary lower bound. No claim about \(\chi_N\) is needed.

For (10), (22) gives \(W_l\ge c_\varepsilon N\) on the bulk,
so (38) yields
\(\overline{E_l}H_l/W_l=1+O_\varepsilon(N^{-1/2})\).
But (11) gives the exact cancellation
\[
             |V_l|^2W_l=
                 \frac1{\sin^2((l-\tfrac12)\delta)} .
 \tag{47}
\]
Equations (16),(47) prove (10).
If \(l/N\to a\in(0,1)\), its limiting amplitude is
\(1/(2\sin^2\pi a)\). With the auxiliary variable \(z=e^{2\pi ia}\)
this is \(-2z/(1-z)^2\), which has no zero away from \(z=1\).
This \(z\) is a height parameter, not a peripheral knot eigenvalue.
The endpoint proof above handles the poles without extending a
bulk relative error into either boundary layer.

## 8. An opposed normal equation in the original marked gauge

Let \(J_l\) be the selected actual path operator of [N], and
\[
 T_l=J_l-\mu_*I,\qquad
 T_l^{\rm opp}=q\,\overline{T_l}=q\overline{J_l}-\mu_*I .
 \tag{48}
\]
The last equality uses \(q\overline{\mu_*}=\mu_*\).
Thus the opposed operator has right kernel \(\mathbb C\bar s_l\)
and left kernel \(\mathbb C\bar r_l\). The original observation
is still \(r_l\), rather than its conjugate.
The new scalar estimate supplies the explicit projector
\[
 \Pi_l^{\rm opp}=\frac{\bar s_l r_l}{\gamma_l},\qquad
 r_l\Pi_l^{\rm opp}=r_l,\quad
 T_l^{\rm opp}\Pi_l^{\rm opp}=0,\quad
 \|\Pi_l^{\rm opp}\|_2\le CN^7 .
 \tag{49}
\]
Its norm bound follows from (8) and the two mode norms.
Equivalently the actual two-line overlap satisfies
\[
 \frac{|r_l\bar s_l|}{\|r_l\|_2\|s_l\|_2}\ge c_0N^{-7}.
 \tag{50}
\]
This is a statement about these specified source modes.

Conjugating [N]'s raw normal gap gives
\(\operatorname{dist}_2(w,\mathbb C\bar s_l)
\le CN^{11}\|T_l^{\rm opp}w\|_2\).
Apply \(I-\Pi_l^{\rm opp}\) after choosing a best approximation
on that line. It follows that
\[
 \|(I-\Pi_l^{\rm opp})w\|_2\le CN^{18}\|T_l^{\rm opp}w\|_2,
 \qquad
 \|(I-\Pi_l^{\rm opp})w\|_{\rm ht}
                    \le CN^{19}\|T_l^{\rm opp}w\|_{\rm ht}.
 \tag{51}
\]
The last height norm is exactly [H]'s real positive diagonal norm
on the selected block. Its condition number is at most \(CN\);
the comparison costs at most \(C\sqrt N\).
For every compatible forcing \(\bar r_l f=0\), there is therefore
a unique solution
\[
                T_l^{\rm opp}w=f,\qquad r_lw=0 ,
 \tag{52}
\]
with the same polynomial bound.
Existence follows by subtracting \(\Pi_l^{\rm opp}\) from any
compatible solution supplied by the conjugated [N] construction;
uniqueness follows from \(r_l\bar s_l=\gamma_l\ne0\).
For a singleton the compatible forcing is zero.
The projector in (49) is not asserted to commute with
\(T_l^{\rm opp}\): the preserved row \(r_l\) differs from its left null row.

## 9. Source scope and coverage

The new assertion is a signed scalar lower bound for the actual
opposed marked modes, uniformly over all their height channels
eventually, and the resulting local normal equation with the
original marked gauge. Its bulk leading amplitude is explicit.
The Gaussian, Wallis, Abel and Fresnel tools themselves are classical.
The proofs above retain their phases and endpoint normalizations.

The normal residual in (51) is transverse to a vector line.
It is not a pair-Casimir derivative or a moving-level first normal.
The full physical height frames retain those original normal channels.
At larger fixed width the original earlier ordinary caps, their
Kronecker constraints and their source factors remain exactly [C,H]'s.
The factor \(\beta_N\) in (7), and any original \(\chi_N\), must
be restored when reading (6) as a boundary coefficient.

The row is observed at the literal marked boundary.
As in [N], \(r_l=r_lP_l\) permits selecting its support only at
that final observation. The path \(I_l\) is not declared invariant
under an arbitrary preceding crossing word.
Neither (8) nor (51) assigns nonnegative coefficients to an
arbitrary coherent exterior. The remaining marked amplitude after
general transport is not controlled by a normal residual alone.
No geometric gluing cycle, original whole-knot lower bound or
finite-exception volume theorem follows from this local estimate.

## Complete inputs and closest coverage

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| N | [Marked boundary normal gap](research_coideal_marked_boundary_normal_gap.md) | 512 | bb9bd6d04480ae8733c0fd1c5901834bdf2ea3e8c7eb3617fb8eb58e66e57956 |
| C | [Cap-straddling cumulative kernel](research_coideal_cap_straddling_cumulative_kernel.md) | 450 | 3ff48e5998f325e1391c088b688a01388f5b8e21d3c8ce53f9ed556e9b289c71 |
| H | [Height pairing and original boundary](research_coideal_height_pairing_and_marked_boundary.md) | 543 | bed81fcb12b20d16d41c55b476b13d8d69b1fe79d0d0620c31230ba652b1d82f |
| S | [Signed crossing and exact phases](research_coideal_crossing_signed_volume_chamber.md) | 634 | 7bf6fb943d2c8080875375c4529776159fc72fbde2e5d8a7d0742e0cbdb10fc0 |
| K | [Continuant source kernel](research_coideal_continuant_source_kernel.md) | 365 | 3ea997e5258c9413fd7c771a6a1475b90b39bf731ac55c0902fd136943b26f44 |

Only written mathematics, source reads and text/hash operations were used.
Earlier final notes, the ledger and public manuscripts are unchanged.
