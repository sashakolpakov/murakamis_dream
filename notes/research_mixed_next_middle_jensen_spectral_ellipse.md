# Jensen improvement of the outgoing spectral coefficient bound

Private written extension, 8 November 2026. Jensen's inequality
improves the spectral penalty in the adopted variable-ellipse
theorem. Every original outgoing row and current is retained.
The highest-degree coefficient is controlled by a fixed-height
truncation chosen from the rate tolerance, not by sending uniform
finite-source constants to an infinite ellipse.

No mathematical numerical evaluation, saved-value calculation,
or frozen-source edit is used. The remaining outer observation
is not estimated here.

## 1. Exact objects and the improved weight

Retain every definition and actual-reference hypothesis in
[the variable-ellipse theorem, equations (1)--(4)](research_mixed_next_middle_variable_spectral_ellipse.md).
Thus the actual complete word begins \(343\), has length at least
five, and is evaluated at its original complete outside parameters;
\[
 E_*=\Lambda-\frac{2383}{1500}-\frac1{50}
       >\frac{1459}{3000},\qquad
 d=U-L<N/3,
 \tag{1}
\]
with \(M=\lceil N/2\rceil\), \(U=N-1-M\), \(L=\lfloor N/6\rfloor\),
and the original removed outgoing cut \(K=\lfloor N/4096\rfloor\).
Keep the exact polynomials
\[
\begin{split}
 \widehat P_{\ell,N}(\xi,T)
  &=\prod_{n=U-\ell+1}^{U}
      q\,\frac{(\xi-c_n)(q^n-Tq^{-n})}{i s_n^3},\\
 B_{\ell,N}^{\rm all}(\xi)
  &=\sum_{k=0}^{U}
      \frac{Y_N^{-k}p_k(Y_N)p_k(Z_*)}{P_k^2}
                  \widehat P_{\ell,N}(\xi,e^{2\pi ik/N}),\\
 B_{\ell,N}^{>}(\xi)
  &=\sum_{k=K+1}^{U}
      \frac{Y_N^{-k}p_k(Y_N)p_k(Z_*)}{P_k^2}
                  \widehat P_{\ell,N}(\xi,e^{2\pi ik/N}),\\
 H_N^{\rm all}&=\sum_{\ell=0}^{d}B_{\ell,N}^{\rm all},
 \qquad H_N=\sum_{\ell=0}^{d}B_{\ell,N}^{>}.
\end{split} \tag{2}
\]
All symbols, phases, parity shifts and normalization factors in
(2) are literal those of the cited theorem. No new interpolant
or approximate amplitude is introduced.

For the filled ellipse \(\mathcal E_h\) with boundary
\(\xi=2\cos(\theta+ih)\), put
\[
 c=\frac{3\sqrt3}{2\pi},\qquad
 \lambda=-\log\cos(3\pi/20),\qquad
 \beta(h)=\log(1-c+c\cosh h),\qquad
 g_J(h)=\beta(h)-\lambda .
 \tag{3}
\]
The already proved elementary bounds are
\[
 \frac{35}{44}<c<1,\qquad0<\lambda<\frac14.
 \tag{4}
\]
In particular the logarithm in (3) has a positive real argument.

**Theorem.** For every fixed \(H_{\max}<\infty\) and \(\tau>0\),
uniformly for \(0\le h\le H_{\max}\), \(0\le\ell\le d\), and
both level parities,
\[
 \sup_{\mathcal E_h}
 \bigl(|B_{\ell,N}^{\rm all}|+|B_{\ell,N}^{>}|\bigr)
 \le C_{\tau,H_{\max}}N^{A_{\tau,H_{\max}}}
                 e^{N(E_*+\tau)+\ell g_J(h)} .
 \tag{5}
\]
For either exact polynomial \(H\) in (2), write
\[
 H(\xi)=\sum_{b=0}^{d}h_{b,N}T_b(\xi/2).
 \tag{6}
\]
Define on \(0\le\rho\le1\)
\[
 I_J(\rho)=
  \sup_{h\ge0}\{\rho h-(\beta(h)-\lambda)_+\}.
 \tag{7}
\]
Then, for every \(\tau>0\),
\[
 \boxed{\quad
 |h_{b,N}|\le C_\tau N^{A_\tau}
                  e^{N(E_*+\tau)-d I_J(b/d)},
 \qquad 0\le b\le d .
 \quad} \tag{8}
\]
The constants in (8) use only a fixed bounded ellipse-height
range depending on \(\tau\).

For clarity the rate in (7) is finite, including at \(\rho=1\).
Let \(h_J>0\) be the unique solution \(\beta(h_J)=\lambda\),
and let \(\rho_J=\beta'(h_J)\). Then
\[
 h_J=\operatorname{arcosh}\!\left(1+\frac{e^\lambda-1}{c}\right),
 \qquad 0<\rho_J<1,
 \tag{9}
\]
\[
 I_J(\rho)=
 \begin{cases}
 \rho h_J,&0\le\rho\le\rho_J,\\
 \rho h_\rho-\beta(h_\rho)+\lambda,&\rho_J<\rho<1,
       \quad \beta'(h_\rho)=\rho,\\
 \lambda+\log(2/c),&\rho=1.
 \end{cases} \tag{10}
\]
This improves the previously adopted rate \(I(\rho)\) from
the variable-ellipse theorem: \(I_J(0)=I(0)=0\), and
\[
 I_J(\rho)>I(\rho)\quad(0<\rho\le1).
 \tag{11}
\]
In particular \(h_J>h_0>1/2+1/300\), where \(h_0\) is
the zero of \(c(\cosh h-1)-\lambda\).

## 2. The spectral Jensen estimate and the complete finite source

Let \(1/6\le x<1/2\), \(\delta=1/2-x\), and
\(A_h=\cosh h-1\ge0\). The original angular comparison,
equation (17) of the variable-ellipse theorem, first bounds
the spectral tail at any \(\xi\in\partial\mathcal E_h\) by
\[
 \int_x^{1/2}
  \log\frac{|\xi-2\cos(2\pi s)|}{4\sin^2(\pi s)}\,ds
 \le
 \int_x^{1/2}
  \log\left(1+\frac{A_h}{1-\cos(2\pi s)}\right)\,ds .
 \tag{12}
\]
Apply the concavity of the logarithm before linearizing its
argument. The average inside that logarithm is explicit:
\[
 \frac1\delta\int_x^{1/2}\frac{ds}{1-\cos(2\pi s)}
   =\frac{\cot(\pi x)}{2\pi\delta}
   \le\frac{3\sqrt3}{2\pi}=c .
 \tag{13}
\]
Consequently
\[
 \boxed{\quad
 \int_x^{1/2}
  \log\frac{|\xi-2\cos(2\pi s)|}{4\sin^2(\pi s)}\,ds
       \le\delta\log(1+c A_h)=\delta\beta(h).
 \quad} \tag{14}
\]
The limiting assertion at \(x=1/2\) is zero on both sides.
Equation (14) is valid at \(h=0\) by integrated-log continuity.

Use (14) in the same zero-safe mesh estimate for the exact
products (2), with \(x=(U-\ell)/N\). The outgoing potential
comparisons are unchanged: on the upper unit sector with
\(3/20\le\Re t\le1/2\) it contributes
\(-\lambda(1/2-x)\), and on the real interval
\(0\le v\le3/20\) it contributes at most
\((1/2-x)\log\cos(\pi v)\).
Thus, with constants uniform for \(h\) in a fixed bounded range,
\[
\begin{split}
 |\widehat P_{\ell,N}(\xi,e^{2\pi i(v+iy)})|
 &\le C N^A e^{\ell g_J(h)}
                  \max\{1,e^{-2\pi y\ell}\},
       &&3/20\le v\le1/2,\quad y\in\mathbb R,\\
 |\widehat P_{\ell,N}(\xi,e^{2\pi iv})|
 &\le C N^A e^{\ell\{\beta(h)+\log\cos(\pi v)\}},
       &&0\le v\le3/20 ,
 \qquad \xi\in\mathcal E_h .
\end{split} \tag{15}
\]
Here maximum modulus in \(\xi\) supplies the filled ellipse.
The exact unit-circle-root reflection in the outgoing variable
supplies the first bound at negative outgoing height, with the
same complex spectral variable.

The uniformity and rounding arguments are exactly those in
Sections 2--3 of the variable-ellipse theorem. Each numerator
zero contributes only a one-sided \(O(\log N)\) mesh error;
sampled zeros improve the upper bound. The denominator indices
stay in a regular interval. The \(c_n\) shift and the possible
sliver \(L/N<1/6\) have width \(O(N^{-1})\). Also
\(N/2-U\in\{1,3/2\}\), so converting \(N\delta\) to \(\ell\)
costs a uniform constant for either sign of \(g_J(h)\) on every
bounded height range. No claim of uniformity as \(h\to\infty\)
is needed in (15).

We specify how the entire outgoing source survives this
replacement. Its original low real rate \(F(v)\) satisfies
\(F'(v)>2/3\) for \(0<v\le3/20\). For each product degree,
\[
 \frac{d}{dv}
 \left[\frac{\ell}{N}\{\beta(h)+\log\cos(\pi v)\}\right]
       =-\frac{\ell\pi}{N}\tan(\pi v)>-\frac{22}{35}.
 \tag{16}
\]
Therefore all low physical rows, including the true zero row,
are still bounded at the original real cut with the common
factor \(e^{\ell g_J(h)}\). This includes their original
zero-safe \(M/N\) displacement.

On every remaining canonical current, (15) gives precisely
the old outgoing-height allowance after that common factor
has been extracted. The exact cuts are still
\[
 a_N=(\lfloor3N/20\rfloor+1/2)/N,\qquad
 b_N=(U+1/2)/N,\qquad M/N+b_N=1-\frac1{2N}.
 \tag{17}
\]
The \(+N\) main integral, both horizontal aliases at \(-1/5,8\),
all four weighted vertical parts, and both full unweighted
joins to \(h_+=\max(h_t,0)\) are retained. The lower-side
decrease \(7\pi/30\), lower-horizontal reserve \(37\pi/1500\),
upper-side decrease \(61\pi/50\), and original join convexity
remain exactly the ones proved in the weighted outgoing
theorem. The half-index numerator uses the original continuous
upper envelope, without division by a period factor. Every
source profile has its original \(E_*\) calibration; no bound
is inferred by recovering a profile from a coherent sum.
There is no physical row beyond \(U\), because the original
kernel terminates there at \(Y_N\).

Finally, the old positive \(k\le K\) estimate is at most
\(N e^{N/200}\). Inserting a product costs at most
\(C N^A e^{\ell\beta(h)}\). Relative to the required common
factor its rate is
\[
 \frac1{200}+\frac{\ell}{N}\lambda
       <\frac1{200}+\frac1{12}
       =\frac{53}{600}<\frac{1459}{3000}<E_* .
 \tag{18}
\]
This is independent of the ellipse height. Thus the complete
sum and its actual \(k>K\) version satisfy (5), with every
finite row and source normalization accounted for.

## 3. The rate function and a uniform finite-height truncation

The spectral penalty is the logarithm of a positive
three-term exponential sum:
\[
 \beta(h)=
 \log\left(\frac c2e^h+(1-c)+\frac c2e^{-h}\right).
 \tag{19}
\]
Direct differentiation gives
\[
 \beta'(h)=\frac{c\sinh h}{1-c+c\cosh h},\qquad
 \beta''(h)=
 \frac{c(1-c)\cosh h+c^2}{(1-c+c\cosh h)^2}>0.
 \tag{20}
\]
For finite \(h\ge0\), \(0\le\beta'(h)<1\), because the
denominator minus its numerator is \(1-c+c e^{-h}>0\).
Moreover \(\beta'(h)\to1\). This proves all existence and
uniqueness assertions in (9)--(10), except the endpoint value,
which follows below.

The degree-aware coefficient extraction in equation (31) of
the variable-ellipse theorem now gives
\[
 |h_{b,N}|
 \le C_{\tau,H_{\max}}N^{A_{\tau,H_{\max}}}
 \exp\!\left\{N(E_*+\tau)-hb+
                   \max_{b\le\ell\le d}\ell g_J(h)\right\}.
 \tag{21}
\]
When \(h\le h_J\), the degree-dependent exponent is
\(b(g_J(h)-h)\). Its derivative is
\(b(\beta'(h)-1)<0\) for \(b>0\), so its minimum on
that interval is at \(h_J\).
When \(h\ge h_J\), the exponent is \(d g_J(h)-bh\).
It follows that, on any height interval \([0,H]\) with
\(H\ge h_J\), the optimal negative exponent in (21) is
\[
 d\,I_J^{[H]}(b/d),\qquad
 I_J^{[H]}(\rho)=
      \sup_{0\le h\le H}
         \{\rho h-(\beta(h)-\lambda)_+\}.
 \tag{22}
\]
For \(b=0\), both sides have optimum zero directly.
This explains why the product-degree maximum cannot simply
be dropped on the negative-\(g_J\) part of the proof.

We now control the error of (22) uniformly through \(\rho=1\).
Put
\[
 A=\frac{2(1-c)}c>0,\qquad
 \varepsilon(H)=\log(1+A e^{-H}+e^{-2H}).
 \tag{23}
\]
The exact identity
\[
 \beta(h)=h+\log(c/2)+\varepsilon(h)
 \tag{24}
\]
shows that, for \(h\ge H\ge h_J\),
\[
\begin{split}
 [\rho h-\beta(h)+\lambda]
  -[\rho H-\beta(H)+\lambda]
  &=-(1-\rho)(h-H)+\varepsilon(H)-\varepsilon(h)\\
  &\le\varepsilon(H),\qquad 0\le\rho\le1.
\end{split} \tag{25}
\]
Therefore
\[
 0\le I_J(\rho)-I_J^{[H]}(\rho)
                  \le\varepsilon(H)
 \quad\hbox{uniformly for }0\le\rho\le1 .
 \tag{26}
\]
In particular \(I_J\) is finite. At \(\rho=1\), (24) and
the strict bound \(\beta'<1\) give
\(I_J(1)=\lambda+\log(2/c)\), proving (10).

For any prescribed \(\tau>0\), choose the fixed height
\[
 H_\tau=
 \max\left\{h_J,\,0,\,
               \log\frac{A+1}{\tau}\right\}.
 \tag{27}
\]
Since \(\log(1+t)\le t\) and \(H_\tau\ge0\),
\(\varepsilon(H_\tau)\le(A+1)e^{-H_\tau}\le\tau\).
Apply (21)--(22) with the source allowance \(\tau/2\)
and this one bounded height range. Equations (26)--(27)
then bound the additional coefficient cost by
\(d\tau<N\tau/3\). The total allowance is smaller than
\(N\tau\), proving (8) with fixed constants depending on
\(\tau\). This argument covers the maximal degree \(b=d\)
without claiming that its optimizer is a finite height.

To compare with the old rate, for every \(h>0\),
\[
 \beta(h)=\log(1+c(\cosh h-1))
                    <c(\cosh h-1).
 \tag{28}
\]
Thus \(h_J>h_0\). For \(0<\rho\le\rho_0\), where the
old rate is \(\rho h_0\), the candidate height \(h_J\)
already gives the strictly larger value \(\rho h_J\).
For \(\rho>\rho_0\), the old optimizer
\(\widetilde h_\rho=\operatorname{arsinh}(\rho/c)>h_0\)
has strictly positive old \(g(\widetilde h_\rho)\). At that same
finite height, replacing this penalty by
\((\beta(\widetilde h_\rho)-\lambda)_+\) strictly decreases it.
This proves (11), including \(\rho=1\), without comparing
approximate optimizer values.

## 4. Scope in the original remaining trace

For the exact outer functional
\[
 \mathcal L_N(P)=
 \phi_N^{(x)}
   [\mathcal R_N(x)^3e_M(x)\mathcal K_{3,N}(-2,x)P(x)],
 \qquad
 \mathcal L_{N,b}=\mathcal L_N(T_b(\cdot/2)),
 \tag{29}
\]
linearity and (8) give
\[
 |\mathcal L_N(H_N)|
 \le C_\tau N^{A_\tau}e^{N(E_*+\tau)}
          \sum_{b=0}^{d}e^{-dI_J(b/d)}|\mathcal L_{N,b}|.
 \tag{30}
\]
This is a stronger actual coefficient weight than the
previously adopted one. No estimate for the remaining
weighted mode sum is proved. Its constant mode is unchanged.

The original scalar \((-q)^M/(\kappa^2N)\), both Fourier
coefficients, full inner Hermite source, and every already
accounted contour/filter correction remain exactly as in
the outer observation theorem. The eligible exact low-edge
reduction of that outer functional may still be used.
The present result does not replace a bilinear trace by a
positive model and supplies no signed lower bound. It
proves no complete-transfer asymptotic, noncancellation,
outside-variable jet, or arbitrary-short-cluster theorem.
