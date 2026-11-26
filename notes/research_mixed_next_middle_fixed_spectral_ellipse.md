# A fixed spectral ellipse for the exact outgoing polynomial

Private written proof, 8 November 2026. The exact finite amplitude
is bounded on a spectral ellipse of fixed height \(1/2\), throughout
the outgoing contours used in the original conditional sum.
The small physical outgoing indices require a separate comparison;
they are included below. Consequently the coefficients of the
outgoing polynomial have exponential decay in their Fourier degree.

This improves the remaining sufficient operator estimate. It does
not prove that estimate or exclude cancellation in the full transfer.

## 1. Objects and statements

Retain the original notation
\[
 q=e^{\pi i/N},\quad r=q^{-2},\quad D=N-1,\quad
 M=\lceil N/2\rceil,\quad U=D-M,\quad
 L=\lfloor N/6\rfloor,\quad d=U-L<N/3,
\]
\[
 s_n=2\sin(\pi n/N),\quad
 c_n=2\cos((2n+1)\pi/N),\quad
 P_k=(r;r)_k,\quad p_k(Z)=(rZ;r)_k,\quad K=\lfloor N/4096\rfloor .
 \tag{1}
\]
Every statement is for sufficiently large \(N\), of either parity.
The exact products and amplitude from
[the polynomial amplitude theorem](research_mixed_next_middle_casimir_polynomial_amplitude.md)
are
\[
 \widehat P_{\ell,N}(\xi,T)
 =\prod_{n=U-\ell+1}^{U}
       q\,\frac{(\xi-c_n)(q^n-Tq^{-n})}{i s_n^3},
 \qquad
 \mathscr A_N(\xi,T)=\sum_{\ell=0}^{d}\widehat P_{\ell,N}(\xi,T).
 \tag{2}
\]
The empty product is one. No asymptotic replacement is made in (2).

Let \(\mathcal E\) be the filled ellipse in the \(\xi\)-plane whose
boundary is
\[
             \xi=2\cos(\theta+i/2),\qquad \theta\in\mathbb R.
 \tag{3}
\]
Its semiaxes are \(2\cosh(1/2)\) and \(2\sinh(1/2)\).
Put \(a=3/20\) and \(\alpha=5103/47600\).

**Theorem 1.** Uniformly for \(\xi\in\mathcal E\),
\(a\le v\le1/2\), \(y\in\mathbb R\), and \(0\le\ell\le d\),
\[
 |\widehat P_{\ell,N}(\xi,e^{2\pi i(v+iy)})|
 \le C N^A e^{-\ell/400}
                    \max\{1,e^{-2\pi y\ell}\}.
 \tag{4}
\]
In particular
\[
 |\mathscr A_N(\xi,e^{2\pi i(v+iy)})|
 \le C N^A\max\{1,e^{-2\pi yd}\}.
 \tag{5}
\]
For real \(0\le v\le a\), the complementary estimate is
\[
 |\mathscr A_N(\xi,e^{2\pi iv})|
 \le C N^A
   \exp\!\left\{\frac N3\bigl(\alpha+\log\cos(\pi v)\bigr)_+\right\}.
 \tag{6}
\]
Here \(x_+=\max(x,0)\). All constants in these statements are
independent of the spectral point and of \(\ell\).

For the actual complete reference of the
[weighted outgoing theorem](research_mixed_next_middle_weighted_outgoing_kernel.md),
write \(Z=Z_*\), \(\Lambda=\Re\mathcal P_*>419/200\), and
\[
 B_0=2383/1500,\qquad
 E_*=\Lambda-B_0-1/50 .
 \tag{7}
\]
This reference concerns the specified words in powers three and
four beginning \(343\), of length at least five. Its output has
\(Z=e^{-2\pi i z}\), \(z=u+ih_z\), with
\(3/10\le u\le39/100\) and \(4/5<|Z|<8/7\).
Define the two exact outgoing polynomials
\[
\begin{split}
 H_N^{\rm all}(\xi,Z)
  &=\sum_{k=0}^{U}
     \frac{r^{-Mk}p_k(r^M)p_k(Z)}{P_k^2}
                           \mathscr A_N(\xi,e^{2\pi ik/N}),\\
 H_N(\xi,Z)
  &=\sum_{k=K+1}^{U}
     \frac{r^{-Mk}p_k(r^M)p_k(Z)}{P_k^2}
                           \mathscr A_N(\xi,e^{2\pi ik/N}).
\end{split} \tag{8}
\]

**Theorem 2.** For every \(\tau>0\),
\[
 \sup_{\xi\in\mathcal E}
       \bigl(|H_N^{\rm all}(\xi,Z_*)|+|H_N(\xi,Z_*)|\bigr)
       \le C_\tau N^{A_\tau} e^{N(E_*+\tau)}.
 \tag{9}
\]
Thus, in the exact Chebyshev expansion
\[
                  H_N(\xi,Z_*)=\sum_{b=0}^{d}h_{b,N}T_b(\xi/2),
 \tag{10}
\]
one has
\[
 |h_{b,N}|\le C_\tau N^{A_\tau}
          e^{N(E_*+\tau)-(1/2+1/400)b},\qquad 0\le b\le d.
 \tag{11}
\]
The constant includes the normalization of the constant
coefficient. These are bounds for the actual coefficients
after the outgoing summation.

## 2. A logarithmic potential on an upper sector

Use the real primitive
\[
 J(x)=\int_0^x\log|2\sin(\pi s)|\,ds,\qquad J(1/2)=0,
\]
and, for \(1/6\le x\le1/2\), define
\[
 K_T(x)=\int_x^{1/2}
         \log\frac{|1-Te^{-2\pi is}|}{2\sin(\pi s)}\,ds .
 \tag{12}
\]
We prove
\[
 K_T(x)\le(1/2-x)\log\cos(\pi a),
 \quad
 T=\rho e^{2\pi iv},\quad 0\le\rho\le1,\quad a\le v\le1/2 .
 \tag{13}
\]
At \(\rho=0\) the argument \(v\) is immaterial.

First fix \(\rho>0\), writing \(\rho=e^{-2\pi y}\), \(y\ge0\).
Differentiation of the integrated sine formula gives
\[
 \partial_v K_T(x)
  =\log\frac{|\sin\pi(x-v-iy)|}{|\cos\pi(v+iy)|}.
 \tag{14}
\]
Its sign is the sign of
\(\sin^2\pi(x-v)-\cos^2\pi v\); the two terms
\(\sinh^2(\pi y)\) cancel. For \(v<x\) this sign is
nonpositive. For \(v>x\) it changes from negative to positive
only at \(v=(x+1/2)/2\). Therefore the maximum over
\(a\le v\le1/2\) occurs at an endpoint. At \(y=0\), the
integrable logarithmic singularities in (14) give the same
monotonicity by continuity.

We next show that at either endpoint the radial maximum occurs
at \(\rho=0\) or \(1\). For \(v=a\), the part depending on
\(\rho\) is
\[
 F(\rho)=\frac1{2\pi}\int_\beta^\gamma
                  \log|1-\rho e^{i\theta}|\,d\theta,\qquad
 \beta=2\pi(x-a),\quad \gamma=2\pi(1/2-a).
\]
Here \(0\le\beta\le\gamma<\pi\).
For \(0<\rho<1\), put \(D_\theta=1+\rho^2-2\rho\cos\theta\).
Differentiation in \(\log\rho\) gives
\[
 \frac{d^2 F}{d(\log\rho)^2}
 =\frac{\rho}{2\pi}
       \left(\frac{\sin\beta}{D_\beta}
                          -\frac{\sin\gamma}{D_\gamma}\right).
 \tag{15}
\]
Its sign is that of
\[
 A(1+\rho^2)+2B\rho,\qquad
 A=\sin\beta-\sin\gamma,\quad B=\sin(\gamma-\beta)\ge0 .
 \tag{16}
\]
If \(A\ge0\), (15) is nonnegative and \(dF/d\log\rho\)
increases from zero. If \(A<0\), the expression in (16)
can change sign only from negative to positive on \(0<\rho<1\):
divide by \(2\rho\) and use the strict decrease of
\((1+\rho^2)/(2\rho)\). The first derivative then first
decreases from zero and subsequently increases. In either
case \(F\) has no interior maximum.

At \(v=1/2\), the same representation has
\(\beta=0\), \(\gamma=2\pi(1/2-x)\), by the evenness of
the circle logarithm. Expression (16) becomes
\(-\sin\gamma(1-\rho)^2\le0\). Thus \(F\) is decreasing
and its maximum is at \(\rho=0\).
Continuity at radial endpoints, including integrated zeros
at \(\rho=1\), proves the radial assertion.

It remains to compare the resulting boundary values.
At \(T=0\), \(K_0(x)=J(x)\). The increasing function
\(\log(2\sin\pi s)\) on \([1/6,1/2]\) has its least
tail average at \(x=1/6\). Its integral there is greater
than \((1/6)\log\sqrt3>1/12\), by retaining just
\([1/3,1/2]\). Hence
\[
                 K_0(x)\le-\tfrac14(1/2-x).
 \tag{17}
\]
Also \(\cos(\pi a)>\sqrt3/2>4/5>e^{-1/4}\).
Thus (17) is stronger than (13).

At \(T=e^{2\pi ia}\), every integration variable satisfies
\(s\ge1/6>a\), and
\[
 \frac{\sin\pi(s-a)}{\sin\pi s}
             =\cos\pi a-\cot\pi s\,\sin\pi a
             \le\cos\pi a.
\]
Integration proves (13) at this last radial endpoint.
The angular and radial reductions prove (13) everywhere
in its stated sector. This argument bounds the potential;
it does not assume pointwise monotonicity of its integrand
in the radius.

## 3. Spectral displacement and finite products

For \(z=\theta-ih\), \(h\ge0\), let
\[
 V_z(x)=\int_0^x
          \log|2\cos(2\pi s)+2\cos z|\,ds-2J(x).
 \tag{18}
\]
The full-circle identity gives \(V_z(1/2)=h/2\).
For \(0<x<1/2\), \(h>0\), and \(0\le\theta\le\pi\),
\[
 \partial_\theta V_{\theta-ih}(x)
 =-\frac1{2\pi}\operatorname{artanh}
   \frac{\sin(2\pi x)\sin\theta}
        {\cosh h+\cos(2\pi x)\cos\theta}
 \le0 .
 \tag{19}
\]
The denominator is positive and the quotient lies in
\([0,1)\). Formula (19) follows by factoring the two
cosines and integrating the angular derivative; it is also
the derivative used in
[the physical three-kernel bound, Section 3](research_mixed_next_physical_three_kernel_fourier_bound.md).
The limiting assertion at \(h=0\) follows by continuity
of the integrated logarithm.

Consequently the largest spectral contribution on an ellipse
of height \(h\) occurs at \(\xi=2\cosh h\). More precisely,
for every point \(\xi=-2\cos(\theta-ih)\),
\[
\begin{split}
 \int_x^{1/2}
       \log\frac{|\xi-2\cos(2\pi s)|}{4\sin^2(\pi s)}\,ds
 &=h/2-V_{\theta-ih}(x)\\
 &\le h/2-V_{\pi-ih}(x)\\
 &=\int_x^{1/2}
       \log\left(1+\frac{\cosh h-1}{1-\cos(2\pi s)}\right)\,ds\\
 &\le\frac{\cosh h-1}{2\pi}\cot(\pi x).
\end{split} \tag{20}
\]
Symmetry covers the remaining angular arguments.

On \(1/6\le x\le1/2\),
\[
                 \frac{\cot(\pi x)}{1/2-x}\le3\sqrt3 .
 \tag{21}
\]
Indeed \(\tan t/t\) is increasing for \(0<t<\pi/2\);
apply it at \(t=\pi(1/2-x)\le\pi/3\).
At \(h=1/2\), the positive series gives
\[
 \cosh(1/2)-1
 \le\frac18+\frac{1/384}{1-1/120}
 =\frac{243}{1904}.
\]
Using \(\sqrt3<7/4\) and \(\pi>25/8\), equations
(20)--(21) therefore give
\[
                  h/2-V_{\theta-ih}(x)
                  \le\alpha(1/2-x),\quad
                  \alpha=\frac{5103}{47600}.
 \tag{22}
\]
On the other hand, \(-\log\cos t\ge t^2/2\) for
\(0\le t<\pi/2\), since \(\tan t\ge t\). Thus
\[
 -\log\cos(\pi a)>\frac{225}{2048},\qquad
 \frac{225}{2048}-\frac{5103}{47600}>\frac1{400}.
 \tag{23}
\]
The second inequality is rational; after adding \(1/400\)
to the second fraction it is equivalent to
\(5\,355\,000>5\,347\,328\).

For a product in (2), put \(x=(U-\ell)/N\).
The uniform upper finite-product estimate gives
\[
 \log|\widehat P_{\ell,N}(\xi,T)|
 \le N\left\{
   \int_x^{1/2}
       \log\frac{|\xi-2\cos(2\pi s)|}{4\sin^2(\pi s)}\,ds
        +K_T(x)\right\}+C\log N .
 \tag{24}
\]
Here (24) is an upper bound, not a relative asymptotic.
For completeness, each numerator factors into shifted circle
logarithms. Away from its nearest mesh cell to a zero, the
summed derivative bound is \(O(\log N)\). In that cell,
rescaling gives the same one-sided error; an exact sampled
zero improves the upper bound. The denominator is regular
on the integration range. This is the same uniform
finite-product argument used in the polynomial amplitude
theorem, and it is uniform for \(\xi\) on the fixed ellipse
and \(T\) in the compact upper unit sector.

The shift in \(c_n\), the difference between \(U/N\) and
\(1/2\), and the possible interval \(L/N<1/6\) all have
width \(O(N^{-1})\). The uniform integrated-log modulus of
continuity costs at most another \(C\log N\).
Thus the comparisons (13),(22),(23) apply in (24) with
this same polynomial cost. Since \(N(1/2-x)\ge\ell\),
they prove
\[
 |\widehat P_{\ell,N}(\xi,T)|\le CN^A e^{-\ell/400}
 \tag{25}
\]
on the boundary of \(\mathcal E\) and in the upper unit
sector. Each product is polynomial in \(\xi\), so maximum
modulus extends (25) throughout \(\mathcal E\).

Each outgoing factor in (2) has its zero on the unit circle.
Therefore the exact reflection identity is
\[
 |\widehat P_{\ell,N}(\xi,T)|
   =|T|^\ell
      |\widehat P_{\ell,N}(\xi,1/\overline T)|.
 \tag{26}
\]
It holds for the same complex \(\xi\). Reflection preserves
the outgoing angular sector. Equations (25)--(26) prove
(4), and summing proves (5).

For real \(0\le v\le a\), one still has \(v\le x\), up to
the already paid mesh shifts, so the pointwise sine comparison
instead gives
\[
                K_{e^{2\pi iv}}(x)
                   \le(1/2-x)\log\cos(\pi v).
\]
Together with (22),(24), this bounds a product by
\(CN^A\exp\{\ell(\alpha+\log\cos\pi v)\}\), with a fixed
factor absorbing \(N/2-U\). Maximizing over \(0\le\ell< N/3\)
and summing proves (6). This completes Theorem 1.

## 4. The low physical rows retain their original bound

The previous outgoing proof bounded its low rows
\(0\le k\le\lfloor3N/20\rfloor\) on the real spectral
interval. To use the fixed ellipse, the extra rate in (6)
must be included.

Let
\[
                       F(v)=\Re Q(v;1/2,z_*),\quad 0\le v\le a,
 \tag{27}
\]
with the original conditional phase and its normalization,
as in equation (7) of the weighted outgoing theorem.
The finite row has upper rate \(F(k/N)\), uniformly
including the zero row, with polynomial cost. The physical
input \(M/N\) differs from \(1/2\) by \(O(N^{-1})\);
the original upper finite-product estimate absorbs that
difference.

For \(0<v\le a\),
\[
 F'(v)=\log
 \frac{2\cos(\pi v)\,|1-Z_*e^{-2\pi iv}|}{4\sin^2(\pi v)}
                       >\log2>\frac23 .
 \tag{28}
\]
Here \(2\cos(\pi v)\ge\sqrt3\) and
\(4\sin^2(\pi v)<1\). To check the remaining factor, write
\(\rho=|Z_*|\). The real coordinate \(u+v\) lies in
\([3/10,27/50]\), so \(\cos(2\pi(u+v))<-3/10\).
Since \(\rho>4/5\),
\[
 |1-Z_*e^{-2\pi iv}|^2
   >1+\frac{16}{25}+\frac{12}{25}
   =\frac{53}{25}>\frac{49}{25}.
\]
Thus this factor exceeds \(7/5\), and \(\sqrt3(7/5)>2\).
Finally \(\log2>2/3\) follows from
\(2\operatorname{artanh}(1/3)>2/3\).

We retain the product degree instead of taking the maximum
used in (6). For each \(0\le\ell\le d\), put
\[
             B_\ell(v)=\frac{\ell}{N}
                                  (\alpha+\log\cos\pi v).
\]
Since \(\ell/N<1/3\),
\[
 B_\ell'(v)=-\frac{\ell\pi}{N}\tan(\pi v)>-\frac{22}{35},
 \tag{29}
\]
using \(v\le3/20<1/6\), \(\tan(\pi/6)=1/\sqrt3<3/5\),
and \(\pi<22/7\). Equations (28)--(29) show that
\(F+B_\ell\) is increasing. Equation (23) therefore gives
\[
 F(v)+B_\ell(v)\le F(a)+B_\ell(a)
                         \le F(a)-\frac{\ell}{400N}.
 \tag{30}
\]
The finite-product estimate preceding (6) now bounds the
positive low-row sum with the individual insertion
\(\widehat P_{\ell,N}\) at the original real-cut rate,
with the additional factor \(e^{-\ell/400}\).
Continuity includes \(v=0\); no logarithmic derivative
is evaluated at its singular endpoint. Summing the
products also proves the corresponding amplitude bound.

## 5. The complete outgoing observation and its Fourier coefficients

For each \(\ell\), first define the outgoing observation
\[
 B_{\ell,N}^{\rm all}(\xi)
 =\sum_{k=0}^{U}
      \frac{r^{-Mk}p_k(r^M)p_k(Z_*)}{P_k^2}
                    \widehat P_{\ell,N}(\xi,e^{2\pi ik/N}),
\]
and let \(B_{\ell,N}^{>}(\xi)\) be the same sum over \(k>K\).
These are polynomials of degree at most \(\ell\).
We apply the exact contour proof of the weighted outgoing
theorem to each such product, retaining its canonical
interpolation, both half-grid cuts, main height
\(h_+=\max(h_t,0)\), alias heights \(-1/5,8\), all six
weighted currents, and both unweighted joins.

For every point of those contours, (4) supplies the same
upper or lower outgoing-height cost as the amplitude estimate
in that proof, together with the factor \(e^{-\ell/400}\).
The estimates are uniform on the whole fixed ellipse;
the lower-height factor \(e^{-2\pi y\ell}\) costs no more
than the original \(e^{-2\pi yd}\) when \(y<0\).
The exact cuts differ from \(a,1/2\) by \(O(N^{-1})\).
The same finite-product estimate in (24), or the corresponding
integrated-log continuity, gives only a polynomial change in
these bounds on the bounded-height contour rectangle.
The incoming canonical factor remains on its original
prewall branch; no contour or source normalization changes.

Thus its lower-side decrease \(7\pi/30\), lower-horizontal
reserve \(37\pi/1500\), upper estimates, and unweighted
joining estimates remain valid. The only part not supplied
by (4) is the low physical group, which has just been paid
by (30), with the same product-degree gain.
The original calibration gives \(F(a)<E_*\) and bounds
every other profile by \(E_*\). It follows that, uniformly
in \(\ell\),
\[
 \sup_{\mathcal E}|B_{\ell,N}^{\rm all}|
       \le C_\tau N^{A_\tau}
                         e^{N(E_*+\tau)-\ell/400}.
\]

To remove \(0\le k\le K\), use the positive small-outgoing
bound from the weighted theorem, before inserting the
product. Its rate is at most \(1/200\).
The finite-product bound adds at most \(\alpha\ell/N\).
Since \(\ell<N/3\) and \(\alpha<3/25\),
\[
 \frac1{200}+\frac{\ell}{N}\left(\alpha+\frac1{400}\right)
 <\frac1{200}+\frac1{25}+\frac1{1200}
 =\frac{11}{240}<\frac1{20}<E_*.
\]
Thus subtraction preserves the same \(e^{-\ell/400}\)
bound for \(B_{\ell,N}^{>}\). Summing these bounds over
\(\ell\) proves (9) for both polynomials.

For (11), compose each degree-at-most-\(\ell\) polynomial
\(B_{\ell,N}^{>}\) with \(\xi=\zeta+\zeta^{-1}\).
The coefficient of \(\zeta^b\) is half its Chebyshev
coefficient for \(b\ge1\), and is zero if \(b>\ell\).
The circle \(|\zeta|=e^{1/2}\) maps to the boundary of
\(\mathcal E\). Cauchy's coefficient formula therefore
bounds that coefficient by
\[
        2C_\tau N^{A_\tau}
                    e^{N(E_*+\tau)-\ell/400-b/2}.
\]
Sum only over \(\ell\ge b\). The geometric sum contributes
at most \(e^{-b/400}/(1-e^{-1/400})\), proving (11).
The constant coefficient is covered with the same bound.
This completes Theorem 2.

## 6. The remaining operator estimate, with its actual weights

Keep the original functional from
[the exact outer observation](research_mixed_next_three_outer_casimir_observation.md):
\[
 \mathcal L_N(P)=
 \phi_N^{(x)}
   [\mathcal R_N(x)^3e_M(x)\mathcal K_{3,N}(-2,x)P(x)],
 \qquad
 \mathcal L_{N,b}=\mathcal L_N(T_b(\cdot/2)).
 \tag{31}
\]
Equation (11) gives the exact-source upper bound
\[
 |\mathcal L_N(H_N)|
 \le C_\tau N^{A_\tau} e^{N(E_*+\tau)}
             \sum_{b=0}^{d}e^{-(1/2+1/400)b}|\mathcal L_{N,b}|.
 \tag{32}
\]
It therefore suffices to prove
\[
 \max_{0\le b\le d} e^{-(1/2+1/400)b}|\mathcal L_{N,b}|
                   \le C N^B e^{NB_f},
 \qquad B_f=77/50+\pi/50 .
 \tag{33}
\]
This is weaker than the previously proposed bound without
the exponential degree weight. The factor is justified by the actual outgoing
coefficients; it is not a freely chosen norm.

Estimate (33) is not proved here. One can also estimate the
actual weighted combination directly instead of bounding its
modes separately. The present result supplies a fixed complex
domain and exponential coefficient decay before that final
observation. It does not establish full transfer asymptotics,
stability under arbitrary short fillings, or finite exceptions.
No mathematical numerical evaluation was used.

