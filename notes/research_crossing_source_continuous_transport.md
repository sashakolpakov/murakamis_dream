# Noncancellation for a source containing an original crossing

22 November 2026. Written research proof. Author-final. Earlier final notes and public
manuscripts remain unchanged.

The source below contains a literal signed-crossing element. Its
boundary recurrence is complex, so the earlier positive recurrence
does not apply directly. A rescaled first difference instead has a
stable complex ratio. We prove that this ratio stays close to an
explicit function with positive real part, uniformly through the
central fold. This gives a lower bound on the original scalar,
with every phase and the original closing retained.

## 1. Source, parameter region, and result

Use the complete Frobenius algebra and centered orthonormal basis
of [B]. Thus
\[
 \begin{gathered}
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\qquad
 \kappa=e^{\pi i d^2/(2N)},\\
 U_x=\sum_{j=0}^d x^j f_j,\qquad R^+=\sqrt N f_0.
 \end{gathered}
 \tag{1}
\]
All value and first-derivative directions at repeated Casimir roots
remain in this algebra. Its multiplication and Frobenius functional
\(\phi\) are the original ones.

Write
\[
 L(x)=\int_0^x\log|2\sin\pi v|\,dv,
 \tag{2}
\]
with its odd one-periodic extension. Fix a compact set \(\mathcal K\)
in the open region
\[
 c,R>0,\qquad c+R<1,\qquad
                         \Delta=L(c+R)-L(R)>0.
 \tag{3}
\]
For every real \(0<h<R\), set \(k=R-h\) and
\[
 \begin{gathered}
 z=-e^{-2\pi ic},\qquad s=-e^{-2\pi ih},\qquad
 t=-e^{-2\pi ik},\qquad r=st=e^{-2\pi iR},\\
 \Phi_N^+(c,h,k)=\phi(f_0U_zU_sU_t),\\
 \mathcal A(c,h,k)
     =L(c+h)+L(c+k)+L(h+k)-2[L(c)+L(h)+L(k)].
 \end{gathered}
 \tag{4}
\]
The condition on \(\Delta\) is a proved source-contour restriction.
It is not inferred from hyperbolicity or from the sign of the
action. It holds, for example, when \(1/6<R<c+R<5/6\).

**Theorem.** There are constants \(C_{\mathcal K},N_{\mathcal K}\)
such that for every \(N\ge N_{\mathcal K}\), every
\((c,R)\in\mathcal K\), and every real \(0<h<R\),
\[
 \boxed{\quad
 \Phi_N^+(c,h,R-h)\ne0,\qquad
 \left|\log|\Phi_N^+|-N\mathcal A(c,h,R-h)\right|
                                      \le C_{\mathcal K}\log N.
 \quad}
 \tag{5}
\]
The estimate is uniform at level-dependent approaches to either
endpoint and to the central fold. Both parities and composite
levels are included.

The four input norms are \(1,\sqrt N,\sqrt N,\sqrt N\).
Their original normalized closing is therefore
\(\Phi_N^+/N^{3/2}\). Replacing \(f_0\) by the actual crossing
\(R^+\) multiplies the scalar by \(\sqrt N\) and the product
of input norms by the same factor, leaving this normalized
closing unchanged. In particular, at any fixed parameters in (3),
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
          \log\left|\frac{\Phi_N^+(c,h,R-h)}{N^{3/2}}\right|
                       =2\pi\mathcal A(c,h,R-h).
 \tag{6}
\]
No norm is substituted for the scalar in (5).

There is also an explicit relative asymptotic on compact subsets
with \(c,h,k>0\), \(c+h+k<1\), and
\(L(c+h+k)-L(h+k)>0\). Put
\[
 \begin{split}
 \mathcal S(c,h,k)&=\mathcal A(c,h,k)-\pi i(ch+ck+hk),\\
 \mathcal B(c,h,k)&=
 \frac{e^{\pi i(c+h+k)}}
 {2\sqrt{2\sin\pi(c+h)\sin\pi(c+k)\sin\pi(h+k)}}.
 \end{split}
 \tag{6a}
\]
The denominator uses its positive real square root. Uniformly on
every such compact set, including its points with \(h=k\),
\[
 \boxed{\qquad
 \Phi_N^+=\kappa^2 N^{-1/2}\mathcal B(c,h,k)
                  e^{N\mathcal S(c,h,k)}(1+O(N^{-1})).
 \qquad}
 \tag{6b}
\]
In particular the leading coefficient is nonzero. Unlike the
logarithmic estimate (5), (6b) is not asserted uniformly in
level-dependent approaches to \(h=0\) or \(k=0\); those boundary
layers have their own Gamma factors in (8).

## 2. Actual initial values on every offset

The fractional boundary theorem [P] supplies the initial values.
Put \(\varepsilon=N^{-1}\) and
\[
 \begin{split}
 M_0&=L(c+R)-L(c)-L(R)>0,\\
 g_0&=e^{-\pi iR}
       \frac{\sin^2\pi R\,\sin\pi c}{\pi^2\sin\pi(c+R)}.
 \end{split}
 \tag{7}
\]
Let \(V_a=\Phi_N^+(c,(a-\tfrac12)/N,R-(a-\tfrac12)/N)\).
Uniformly for \(a\) in any fixed compact subset of \((0,\infty)\),
[P] proves for the actual scalar
\[
 \frac{V_a}{V_1}
       =\frac{N^{2a-2}g_0^{a-1}}{\Gamma(a)^2}
                           (1+O_{\mathcal K}(N^{-1})),\qquad
 \log|V_1|=NM_0+O_{\mathcal K}(\log N).
 \tag{8}
\]
The branch of \(\log g_0\) has imaginary part \(-\pi R\).
The baseline in (8) includes its retained source current;
it is not replaced by the geometric Gamma quotient alone.

For \(2/N\le h\le R/2\), choose
\[
 J=\lfloor Nh-1\rfloor,\qquad
 a_0=Nh+\tfrac12-J\in[3/2,5/2),\qquad
 h_j=(a_0+j-\tfrac12)\varepsilon,\quad k_j=R-h_j.
 \tag{9}
\]
Define
\[
 H_j=V_{a_0+j},\quad \mathcal D_j=H_j-H_{j-1},\quad
 \delta_j=k_j-h_j,\quad
 \alpha_j=\sin\pi(\delta_j+\varepsilon),\quad
 E_j=\mathcal D_j/\alpha_j.
 \tag{10}
\]
The two adjacent instances of (8) give
\[
 \frac{H_{-1}}{H_0}
   =\frac{(a_0-1)^2}{N^2g_0}(1+O_{\mathcal K}(N^{-1})),\qquad
 \log|H_0|=NM_0+O_{\mathcal K}(\log N).
 \tag{11}
\]
Thus \(H_0,E_0\ne0\). Their ratio satisfies
\[
                    w_0:=H_0/E_0
                        =\alpha_0(1+O_{\mathcal K}(N^{-2})).
 \tag{12}
\]
All these are complex identities. No positive real carrier is
assumed for \(H_j\).

## 3. The original complex recurrence

Specialize the exact equation of [B] to its first coherent
parameter equal to zero:
\[
 \begin{gathered}
 B(\sigma\Phi-\Phi)+D(\sigma^{-1}\Phi-\Phi)=\lambda_N\Phi,\\
 \sigma(s,t)=(Qs,Q^{-1}t),\qquad \lambda_N=Q-1,\\
 B=\frac{(t+q)^2(1-Qzs)}{(t-s)(t-Qs)},\qquad
 D=\frac{(s+q)^2(1-Qzt)}{(Qt-s)(t-s)}.
 \end{gathered}
 \tag{13}
\]
It is an identity for the original polynomial source. The chosen
offset does not change it, and \(\sigma\) lowers \(j\) by one.

For the rows actually used, \(0\le j<J\),
\[
 \delta_j=\delta_J+2(J-j)\varepsilon\ge2\varepsilon.
 \tag{14}
\]
All denominators in (13) are therefore nonzero there. Put
\[
 \begin{split}
 b_j&=\sin^2\pi(k_j+\varepsilon/2)\sin\pi(c+h_j-\varepsilon),\\
 d_j&=\sin^2\pi(h_j+\varepsilon/2)\sin\pi(c+k_j-\varepsilon).
 \end{split}
 \tag{15}
\]
Direct substitution in (13) gives
\[
 B=\frac{2i e^{\pi i(\varepsilon-c+h_j)}b_j}
             {\sin\pi\delta_j\,\alpha_j},\qquad
 D=\frac{2i e^{\pi i(\varepsilon-c+k_j)}d_j}
             {\sin\pi\delta_j\,\alpha_{j+1}}.
 \tag{16}
\]
Consequently the exact equations for the flux and its scalar ratio are
\[
 \begin{gathered}
 E_{j+1}=a_jE_j(1+\beta_jw_j),\\
 w_{j+1}=\alpha_{j+1}
                      +\frac{w_j}{a_j(1+\beta_jw_j)},\\
 a_j=e^{-\pi i\delta_j}\frac{b_j}{d_j},\qquad
 \beta_j=\frac{e^{\pi i(c-h_j)}\sin(\pi/N)\sin\pi\delta_j}{b_j}.
 \end{gathered}
 \tag{17}
\]
At this stage \(w_j=H_j/E_j\) is defined whenever \(E_j\ne0\).
The proof below establishes that condition at every step.
Uniformly on all the used rows,
\[
                        b_j\ge c_{\mathcal K}>0,\qquad
 |\beta_j|\le C_{\mathcal K}\varepsilon\delta_j.
 \tag{18}
\]
Indeed \(k_j+\varepsilon/2\) and \(c+h_j-\varepsilon\)
stay in fixed strict sine intervals.

## 4. Growth and a uniformly nonzero comparison ratio

There is a useful estimate without any restriction \(R<1/2\).
For positive \(u<v\), \(u+v<1\), and \(C>0\) with \(C+v<1\),
the function
\[
       F_C(u,v)=
       \frac{\sin^2\pi v\,\sin\pi(C+u)}
            {\sin^2\pi u\,\sin\pi(C+v)}
 \tag{19}
\]
is increasing in \(C\). Its logarithmic derivative is
\(\pi[\cot\pi(C+u)-\cot\pi(C+v)]>0\).
At \(C=0\) it is \(\sin\pi v/\sin\pi u\).
Apply this with
\(u=h_j+\varepsilon/2\), \(v=k_j+\varepsilon/2\), and
\(C=c-3\varepsilon/2\). For all sufficiently large \(N\),
\[
 |a_j|-1\ge
 2\cos\!\left(\frac{\pi(R+\varepsilon)}2\right)
                   \sin\!\left(\frac{\pi\delta_j}2\right)
                \ge c_{\mathcal K}\delta_j.
 \tag{20}
\]
Here \(\sin\pi u\le1\) was used in subtracting one.

Define the classical transfer factor on \(0<h<R/2\) by
\[
 a_{\rm cl}(h)
  =e^{-\pi i(R-2h)}
       \frac{\sin^2\pi(R-h)\sin\pi(c+h)}
            {\sin^2\pi h\sin\pi(c+R-h)} .
 \tag{21}
\]
For \(\delta=R-2h\), its modulus \(A(\delta)\) is greater
than one by the same comparison as (19). Define
\[
 \overline w(\delta)=
       \frac{\sin\pi\delta}{1-e^{\pi i\delta}/A(\delta)},
                         \qquad 0<\delta<R.
 \tag{22}
\]
The bar denotes a comparison function, not complex conjugation.
Its continuous endpoint values are
\[
 \overline w(R)=\sin\pi R,\qquad
 \overline w(0)=\frac{\pi}{\gamma-i\pi},\qquad
 \gamma=\pi\left[2\cot\frac{\pi R}2
                          -\cot\pi(c+R/2)\right]>0.
 \tag{23}
\]
The second value follows by differentiating \(\log A\) at
\(\delta=0\). The inequality holds because \(R/2<1/2\),
and \(\cot\pi(R/2)-\cot\pi(c+R/2)>0\).

The function \(\overline w\) is smooth on the entire closed
interval, uniformly on the shape compact set. For \(0<\delta<R\),
its denominator in (22) has positive real part and negative
imaginary part. Equations (23) then give, by compactness,
\[
             \Re\overline w(\delta)\ge c_{\mathcal K}>0,\qquad
             |\overline w(\delta)|+|\overline w'(\delta)|
                         +|\overline w''(\delta)|
                                      \le C_{\mathcal K}.
 \tag{24}
\]
This is the comparison that will prevent cancellation in the
actual scalar.

## 5. Tracking through the central fold

Let
\[
       \mathscr T_j(w)=\alpha_{j+1}
                                 +\frac{w}{a_j(1+\beta_jw)}.
 \tag{25}
\]
On any fixed disk containing a unit neighborhood of every
\(\overline w(\delta)\), (18), (20) imply for large \(N\)
\[
       |\mathscr T_j'(w)|
          =\left|\frac1{a_j(1+\beta_jw)^2}\right|
                         \le e^{-c_{\mathcal K}\delta_j}.
 \tag{26}
\]
The denominator does not vanish on this disk. A segment between
two points in it therefore gives the same Lipschitz bound.

The inverse exact transfer factor has no singular initial endpoint:
\[
 a_j^{-1}
  =e^{\pi i\delta_j}
   \frac{\sin^2\pi(h_j+\varepsilon/2)\sin\pi(c+k_j-\varepsilon)}
        {\sin^2\pi(k_j+\varepsilon/2)\sin\pi(c+h_j-\varepsilon)}.
 \tag{27}
\]
Its denominator is uniformly separated from zero, so it is smooth
in \(\varepsilon,\delta\) down to \(h=0\). Let
\(G(\varepsilon,\delta)\) be the right side of (27), with
\(h=(R-\delta)/2\). It has the exact identity
\(G(\varepsilon,0)=1\) for every small \(\varepsilon\).
Integrating its bounded mixed derivative therefore gives
\[
 G(\varepsilon,\delta)-G(0,\delta)=O_{\mathcal K}(\varepsilon\delta).
 \tag{27a}
\]

There is a second cancellation at the fold. Extend the classical
formula locally to negative \(\delta\). Then
\(a_{\rm cl}(-\delta)=a_{\rm cl}(\delta)^{-1}\) and (22) imply
\[
 \overline w(\delta)-\overline w(-\delta)=\sin\pi\delta,
 \qquad \overline w'(0)=\pi/2.
 \tag{27b}
\]
Consequently
\(\overline w'(\delta)-(\pi/2)\cos\pi\delta=O_{\mathcal K}(\delta)\).
Using
\(\overline w=\sin\pi\delta+\overline w/a_{\rm cl}\),
the uniform one-step defect is now
\[
 \left|\overline w(\delta_{j+1})
                  -\mathscr T_j(\overline w(\delta_j))\right|
                             \le C_{\mathcal K}\varepsilon\delta_j.
 \tag{28}
\]
To see the extra factor, the two leading changes are
\[
 \overline w(\delta-2\varepsilon)-\overline w(\delta)
               +\sin\pi\delta-\sin\pi(\delta-\varepsilon)
 =\varepsilon[-2\overline w'(\delta)+\pi\cos\pi\delta]
                                      +O_{\mathcal K}(\varepsilon^2).
\]
They are \(O_{\mathcal K}(\varepsilon\delta+\varepsilon^2)\).
The remaining changes are \(O_{\mathcal K}(\varepsilon\delta)\)
by (18), (27a). Every used row has \(\delta\ge2\varepsilon\),
so the quadratic remainder is absorbed.
Equations (12), (23) give initial error \(O_{\mathcal K}(\varepsilon)\).

Write \(e_j=|w_j-\overline w(\delta_j)|\). Equations (26)--(28)
give, while the actual ratio stays in the chosen disk,
\(e_{j+1}\le e^{-c\delta_j}e_j+C\varepsilon\delta_j\).
Since \(1-e^{-c\delta}\ge c'\delta\) on the compact interval,
choose a fixed \(M\) larger than the initial-error constant and
\(C/c'\). A direct induction then gives
\[
                    |w_j-\overline w(\delta_j)|\le M\varepsilon
                      \qquad(0\le j\le J).
 \tag{29}
\]
For large \(N\), this lies inside the unit neighborhood used
in (26). It therefore closes the induction. In particular,
\(1+\beta_jw_j\ne0\) keeps every \(E_j\) nonzero, and (24)
gives
\[
 \Re w_j\ge c_{\mathcal K}/2,\qquad
                   c_{\mathcal K}\le|H_j/E_j|\le C_{\mathcal K}.
 \tag{30}
\]
This includes the target fold. Every recurrence row used still
satisfies (14); the singular target row is never imposed.

Taking absolute logarithms in the first equation of (17) yields
\[
 \begin{split}
 \log|E_J/E_0|
   &=\sum_{j<J}\log|a_j|
                     +O_{\mathcal K}\!\left(\sum_{j<J}
                                            \varepsilon\delta_j\right)\\
   &=\sum_{j<J}\log|a_j|+O_{\mathcal K}(1).
 \end{split}
 \tag{31}
\]
Equations (30)--(31) prove the corresponding original-scalar estimate
\[
             \log|H_J/H_0|=\sum_{j<J}\log|a_j|+O_{\mathcal K}(1).
 \tag{32}
\]
The lower comparison in (30), not the flux growth alone, is what
makes this a noncancellation theorem.

## 6. The rate, small angles, and the second half

The explicit sine factors in (17) give, uniformly for the
bounded offsets in (9),
\[
 \sum_{j<J}\log|a_j|
       =N\int_0^h\log|a_{\rm cl}(v)|\,dv+O_{\mathcal K}(\log N).
 \tag{33}
\]
To justify the endpoint uniformly, separate
\(\log\sin\pi v=\log v+\log(\sin\pi v/v)\) near zero.
All remaining factors have bounded derivatives on fixed strict
intervals. Integral comparison for the shifted logarithmic sum
gives \(O(\log N)\); the omitted initial interval of length
at most \(2/N\) has the same bound.

Direct integration of the logarithm in (21) gives
\[
 M_0+\int_0^h\log|a_{\rm cl}(v)|\,dv
           =L(c+h)+L(c+k)+L(h+k)-2[L(c)+L(h)+L(k)]
           =\mathcal A(c,h,k).
 \tag{34}
\]
The derivative is positive before the fold, by (19), so
\(\mathcal A\ge M_0>0\) on the first half.
Equations (11), (32)--(34) prove (5) for \(2/N\le h\le R/2\).

For \(0<h\le2/N\), apply (8) directly with
\(a=Nh+1/2\in[1/2,5/2]\). It gives a nonzero actual
scalar with logarithmic modulus \(NM_0+O_{\mathcal K}(\log N)\).
Since \(\log|a_{\rm cl}(v)|=-2\log v+O_{\mathcal K}(1)\)
near zero,
\[
     N|\mathcal A-M_0|
         \le C_{\mathcal K}Nh(1+|\log h|)
                                   =O_{\mathcal K}(\log N).
 \tag{35}
\]
The estimate includes arbitrarily fast approaches to zero.
Finally, interchanging \(s,t\) leaves the original scalar
unchanged, and \(\mathcal A(c,h,k)=\mathcal A(c,k,h)\).
This covers every \(R/2<h<R\) and completes the proof.

## 7. An explicit nonzero leading coefficient

In this section the three positive angles stay in a fixed compact
set inside (3). The fold is allowed; the endpoints \(h=0,k=0\)
are excluded from this relative estimate.

The exact initial Gamma quotient in [P, equation (22)] and its
canonical strip estimates give
\[
 \begin{split}
 V_1&=\kappa^2\sqrt N\,b_1(c,R)e^{N\mathcal S_b(c,R)}
                                       (1+O(\varepsilon)),\\
 b_1(c,R)&=e^{i\pi/4}\frac{\sqrt{1-r}}{1-Cr},\qquad
 C=e^{-2\pi ic},\\
 \mathcal S_b(c,R)&=M_0-\pi i cR.
 \end{split}
 \tag{R1}
\]
The square root is
\(\sqrt{1-r}=\sqrt{2\sin\pi R}\,
e^{i\pi/4-\pi iR/2}\).
For a direct check, the numerator factorial arguments of that
quotient are \(N(1-c)-1/2,N(1-R)\), and its denominator argument
is \(N(1-c-R)+1/2\). Their canonical amplitudes give exactly
\(b_1\). Their exponential is
\[
 f(1-c)+f(1-R)-f(1-c-R)
 =-\frac{i\pi}{12}
  +\frac{i}{2\pi}
       [\operatorname{Li}_2(C)+\operatorname{Li}_2(r)
                                -\operatorname{Li}_2(Cr)].
\]
The unit-circle real and imaginary parts give \(\mathcal S_b\)
in (R1). The polynomial current in [P] is exponentially smaller
than this term since \(M_0>0\).

First evaluate the small correction product in (17). On the
closed first half-interval, (18), (29) give
\[
 \begin{split}
 \prod_{j<J}(1+\beta_jw_j)
 &=\exp\{I(h)+O(\varepsilon)\},\\
 I(h)&=\int_0^h b_0(v)\overline w(R-2v)\,dv,\\
 b_0(v)&=
 \frac{\pi e^{\pi i(c-v)}\sin\pi(R-2v)}
      {\sin^2\pi(R-v)\sin\pi(c+v)}.
 \end{split}
 \tag{R2}
\]
Indeed \(\beta_j=\varepsilon b_0(h_j)+O(\varepsilon^2\delta_j)\).
Replacing \(w_j\) by its comparison function, taking the logarithm,
and replacing the smooth sum by its integral each cost
\(O(\varepsilon)\). The omitted initial interval has length
at most \(2\varepsilon\).

This integral has an exact primitive. Put
\[
 H=e^{-2\pi ih},\quad K=e^{-2\pi ik},\quad
 v_*=\frac{H+K-1-Cr}{1-C},\quad F=2-C-H-K+Cr.
\]
Then
\[
 b_0(h)\overline w(R-2h)
      =\frac{2\pi i(H-K)}{F}
      =\partial_h\log F,\qquad
 e^{I(h)}=\frac{1-v_*(h)}{1-r}.
 \tag{R3}
\]
The logarithm is continued from \(h=0\).
The denominator \(F\) never vanishes on the strict angle domain.
For example \(v_*=1\) would make the critical term ratio of [G]
at \(v=1\) equal to one, whereas that ratio is
\[
 -e^{\pi ic}\frac{\sin\pi h\sin\pi k}{\sin\pi c\sin\pi(h+k)},
\]
which has nonzero imaginary part. The formulas in (R3) therefore
extend through the fold. The identities also follow directly
from
\(B_{\rm cl}-D_{\rm cl}=F/(H-K)\) and
\(\overline w=\sin\pi(k-h)B_{\rm cl}/(B_{\rm cl}-D_{\rm cl})\),
with the removable values understood there.

It remains to approximate the explicit finite product of \(a_j\).
Here are its endpoint corrections so that all offset constants
can be checked. Write \(A=a_0\), \(n=J\), and
\(\ell_0(x)=\log\sin\pi x\). In each of the following four sums
the error is \(O(\varepsilon)\):
\[
 \begin{aligned}
 \sum_{j<n}\ell_0(R-(A+j-1)\varepsilon)
 &=N\int_k^R\ell_0
          +(3/2-A)\ell_0(R)-\ell_0(k)+O(\varepsilon),\\
 \sum_{j<n}\ell_0((A+j)\varepsilon)
 &=N\int_0^h\ell_0
       +(A-1/2)\log(N/\pi)+\tfrac12\log(2\pi)
                              -\log\Gamma(A)+O(\varepsilon),\\
 \sum_{j<n}\ell_0(c+(A+j-3/2)\varepsilon)
 &=N\int_c^{c+h}\ell_0
           +(2-A)\ell_0(c)-\tfrac32\ell_0(c+h)+O(\varepsilon),\\
 \sum_{j<n}\ell_0(c+R-(A+j+1/2)\varepsilon)
 &=N\int_{c+k}^{c+R}\ell_0
           +\tfrac12\ell_0(c+k)-A\ell_0(c+R)+O(\varepsilon).
 \end{aligned}
 \tag{R4}
\]
The first, third, and fourth follow from the elementary
Euler--Maclaurin estimate with a bounded second derivative.
For the second, split \(\ell_0(x)=\log x+
\log(\sin\pi x/x)\). The first sum is
\(n\log\varepsilon+\log\Gamma(A+n)-\log\Gamma(A)\),
where \(A+n=Nh+1/2\). Stirling's formula and the same smooth
estimate for the second part give exactly (R4). All errors
are uniform for \(A\in[3/2,5/2]\).

The exact phase of the product is equally explicit:
\[
 \sum_{j<n}\delta_j
   =Nhk+h-(A-1/2)R
                 +\varepsilon[(A-1/2)^2-(A-1/2)].
 \tag{R5}
\]
Multiply twice the first sum in (R4), subtract twice the
second, add the third, and subtract the fourth. Combine this
with (R5) and the full complex initializer (8). Every occurrence
of \(A\), \(\Gamma(A)\), and its phase cancels, giving
\[
 \begin{split}
 V_A\prod_{j<J}a_j
 ={}&\frac{V_1}{2N}
   \frac{\sin\pi R\sin\pi c\sin\pi(c+R)}
        {\sin^2\pi k\,\sin^{3/2}\pi(c+h)\sin^{1/2}\pi(c+k)}
      e^{\pi i(k-h)/2}\\
 &\qquad{}\times
      e^{N[\mathcal A-M_0-\pi i hk]}(1+O(\varepsilon)).
 \end{split}
 \tag{R6}
\]
This cancellation uses the marked phase
\(g_0^{A-1}/|g_0|^{A-1}=e^{-\pi iR(A-1)}\).
No periodic function of the fractional offset is left over.

Finally \(H_J/H_0=(w_J/w_0)\prod a_j\prod(1+\beta_jw_j)\),
and (12), (29) give
\(w_J/w_0=\overline w(k-h)/\sin\pi R\,(1+O(\varepsilon))\).
The following exact simplification in (R3) is useful:
\[
 \overline w(k-h)e^{I(h)}
       =\frac{e^{\pi ih}\sin^2\pi k\sin\pi(c+h)}
                      {\sin\pi c\sin\pi R}.
 \tag{R7}
\]
For instance,
\(\overline w(1-v_*)=
 e^{\pi iR}(1-K)^2(1-CH)/[2i(1-C)]\);
writing the factors as sines proves (R7).
Substitute (R1), (R6), (R7). The remaining amplitude is
\[
 \frac{e^{\pi iR/2}b_1(c,R)\sin\pi(c+R)}
      {2\sin\pi R\sqrt{\sin\pi(c+h)\sin\pi(c+k)}}
 =
 \frac{e^{\pi i(c+h+k)}}
      {2\sqrt{2\sin\pi(c+h)\sin\pi(c+k)\sin\pi(h+k)}}.
 \tag{R8}
\]
This proves (6b) through the fold from the first half-interval.
Its action and amplitude are both symmetric in \(h,k\).
Exact symmetry of the original scalar therefore proves the
same formula on the second half, with the same coefficient.
The positive real square root in (R8) fixes its phase explicitly.

## 8. The local classical polynomial

This source selects a branch of its original polynomial boundary
equation; it is not the peripheral A-polynomial of a knot.
Put
\[
 C=e^{-2\pi ic},\qquad H=e^{-2\pi ih},\qquad K=r/H.
 \tag{36}
\]
At \(Q=1\), the coefficients of (13) are
\[
 B_{\rm cl}=\frac{(H-r)^2(1-CH)}{(H^2-r)^2},\qquad
 D_{\rm cl}=\frac{H(1-H)^2(H-Cr)}{(H^2-r)^2},
 \qquad\lambda_{\rm cl}=0.
 \tag{37}
\]
Let \(\ell\) denote the symbol of the forward shift
\(h\mapsto h+1/N\). Multiplication of the classical equation
by \(\ell\) gives
\((\ell-1)(D_{\rm cl}\ell-B_{\rm cl})\).
After clearing the displayed denominators its polynomial is
\[
 \mathscr A_{\rm cross}(H,\ell;C,r)
  =(\ell-1)\left[
       H(1-H)^2(H-Cr)\ell-(H-r)^2(1-CH)\right].
 \tag{38}
\]
The factor \(\ell-1\) is retained. On the growing component,
\[
 \ell_{\rm cross}
    =\frac{(1-K)^2(1-CH)}{(1-H)^2(1-CK)}
    =a_{\rm cl}(h).
 \tag{39}
\]
The two components meet at \(h=k\). The source estimates above
remain valid at this meeting point.

The nonvanishing statement concerns the actual finite period.
Equations (37)--(39) alone would not prove it. Nor does this
local polynomial become a knot A-polynomial without the full
marked gluing and elimination.

## 9. The regulator limit of the actual scalar

The marked-regulator calculation [G] identifies the same original
critical graph; it does not require assigning a knot manifold
to this local source. With \(v_*\) as in Section 7 it defines
\[
 \beta_\times=
 [Cv_*]+[v_*/r]-[v_*/H]-[v_*/K]
             +[H^{-1}]+[K^{-1}]-[C]-[r^{-1}].
 \tag{40}
\]
All arguments avoid zero and one. In the reduced pre-Bloch
convention stated in [G], exact five-term relations give
\[
 \begin{split}
 \beta_\times
   &=[CH]+[CK]+[HK]-2[C]-2[H]-2[K]\\
   &=\sum_{\{a,b\}\subset\{c,h,k\}}
                         ([z_{ab}]-[\overline{z_{ab}}]),\\
 z_{ab}&=\frac{1-e^{-2\pi ib}}{1-e^{-2\pi i(a+b)}}.
 \end{split}
 \tag{41}
\]
Each \(z_{ab}\) is a positive ideal-tetrahedron shape with
angles \(\pi(a,b,1-a-b)\). For the Bloch--Wigner regulator \(D\),
\[
 D(\beta_\times)=2\sum_{\{a,b\}}D(z_{ab})=2\pi\mathcal A.
 \tag{42}
\]
Thus (6) becomes a limit identity for the actual original scalar:
\[
 \boxed{\quad
 \lim_{N\to\infty}\frac{2\pi}{N}
       \log\left|\frac{\Phi_N^+}{N^{3/2}}\right|
                  =D(\beta_\times)
                  =2\sum_{\{a,b\}}\operatorname{Vol}(\mathcal T_{ab}).
 \quad}
 \tag{43}
\]
Here \(\mathcal T_{ab}=(\infty,0,1,z_{ab})\); the right side
is a positive tetrahedral chain volume. No claim that these
three tetrahedra form one convex cell or a knot complement is
used in (43).

The logarithmic marking is also tied to the finite scalar.
The full relative formula (6b) has the action
\[
 \mathcal S=\frac{\sum_{\{a,b\}}\operatorname{Li}_2(e^{-2\pi i(a+b)})
             -2\sum_a\operatorname{Li}_2(e^{-2\pi ia})
             +3\operatorname{Li}_2(1)}{2\pi i}
 \tag{44}
\]
with the unit-circle source branches of [G]. The prefactor
\(\mathcal B\) is a fixed analytic function of the angles,
and \(\kappa^2\) remains separate. Equation (R6) checks the
fractional offsets as a continuum; the marking is not inferred
only from the exponentiated equation (38) or from its value
at one boundary point. An added \(2\pi i m h\) in the action
would leave a nonconstant offset phase, contrary to that
explicit cancellation. The reduced-class equality in (41)
does not supply this phase information by itself.

## 10. The original negative crossing

The full coefficient reflection of [C] satisfies
\(f_0^\sharp=f_d\), \(\phi(X^\sharp)=\overline{\phi(X)}\),
and \(U_x^\sharp=x^{-d}U_x\) when \(|x|=1\). Put \(p=zst=-CHK\).
The source with the negative crossing is consequently exactly
\[
 \Phi_N^-:=\phi(f_dU_zU_sU_t)
                         =p^d\,\overline{\Phi_N^+}.
 \tag{45}
\]
It has the same nonvanishing and rate (5), (43). Its relative
asymptotic is
\[
 \Phi_N^-=p^d\kappa^{-2}N^{-1/2}
                    \overline{\mathcal B}\,
                    e^{N\overline{\mathcal S}}(1+O(N^{-1})).
 \tag{46}
\]
This retains the original carrier \(p^d\). It uses neither
positive unitarization of the crossing nor multiplicativity
of the turn. Replacing \(f_d\) by \(R^-=\sqrt N f_d\)
has the same normalization effect as for \(R^+\).

## 11. Scope and proof sources

This proves an original scalar growth estimate with one actual
crossing insertion and generic real coherent boundary angles
in (3). No anchored grid or fixed fold margin remains.
The restriction \(\Delta>0\) comes from the original boundary
packet and has not been removed.

The relative formula is symmetric in the three remaining
angles. It therefore patches, on compact subsets, over the union
of their three permuted gap regions. For example this union
contains every positive triple with \(1/4<c+h+k<5/6\):
the largest pair sum is at least two thirds of the total and
is greater than \(1/6\), while \(L\) is strictly increasing
between \(1/6\) and \(5/6\). This is a symmetry extension of
the same source estimate.

An arbitrary attached short tangle is not replaced by one
coherent input or by a norm. Its general noncancellation and
the finite-exception knot-volume theorem remain open.

| Label | Complete direct proof source | SHA-256 |
|---|---|---|
| P | [Fractional data with the original crossing leaf](research_four_coherent_zero_radius_boundary_source.md) | f74a6b951936f29f5cf66e4b34cfc84b2c890b1ba5464f472ca023aa70c5c621 |
| B | [Original polynomial boundary source](research_four_coherent_boundary_polynomial_source.md) | 93241074830ff4b844ba5baafd06a15bf08ec6bddc3a1498727f110ebe297d84 |
| G | [Original critical graph and marked Bloch regulator](research_one_crossing_marked_bloch_regulator.md) | 5851858e3a10ed61f7fd2819cb554dc387911b9f46e2ecb70f4a31ea49871c0d |
| C | [Complete centered compiler and coefficient reflection](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |

All four whole matching direct proof texts were read. All estimates
above use written mathematics; no mathematical programs, numerical
experiments, tests, builds, or git operations were run.
This research proof is author-final.
