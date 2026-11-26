# Fractional-source rigidity for the original crossing Gamma section

22 November 2026. Written research proof.
Earlier author-final notes and public manuscripts remain unchanged.

The fixed-order conclusion and the uniform-order conclusion below are
separate. Polynomial rigidity alone proves the former. The latter uses
the graded strong remainder estimates in Sections 3--5. In particular,
vanishing formal coefficients are not used as a substitute for a
quantitative remainder.

## 1. Original source, exact normalizer, and two conclusions

Use the original finite source and canonical factorial of [P,F,E,G].
Put
\[
 \epsilon=N^{-1},\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \kappa=e^{\pi i(N-1)^2/(2N)},\qquad r=e^{-2\pi iR},\
 C=e^{-2\pi ic}.
 \tag{1}
\]
Fix compact sets in
\[
 c,R>0,\quad c+R<1,\quad
 \Delta=L(c+R)-L(R)>0,\qquad
 a\in\mathcal A\Subset(0,\infty),
 \tag{2}
\]
where \(L(x)=\int_0^x\log|2\sin\pi t|\,dt\), with its odd periodic
continuation. Enlarge \(\mathcal A\) when a finite comparison requires
this. Define
\[
 \begin{gathered}
 h=(a-\tfrac12)/N,\quad k=R-h,\quad z=-C,\quad
 s_a=-e^{-2\pi ih},\quad t_a=r/s_a,\\
 \Phi_a=\phi(f_0U_zU_{s_a}U_{t_a}),\qquad f_0=R^+/\sqrt N .
 \end{gathered}
 \tag{3}
\]
This is the original scalar. All its Hermite directions, carriers,
finite support, and Frobenius closing remain.

Write \(\mathfrak F=\mathfrak F_N\) for the canonical factorial and
define the exact meromorphic section
\[
 \Gamma_N(c,h,k)=\frac{\kappa^2}{N^2}
 \frac{\prod_{x\in\{c,h,k\}}\mathfrak F(N(1-x)-\tfrac12)^2}
      {\prod_{\{x,y\}\subset\{c,h,k\}}\mathfrak F(N(1-x-y))}.
 \tag{4}
\]
Products count labelled entries. Let \(\Gamma_N(a)\) denote (4) at
(3), and set \(R_N(a)=\Phi_a/\Gamma_N(a)\).

The conclusions hold for all sufficiently large \(N\), uniformly on
the fixed compact sets:

* for every fixed integer \(p\), uniformly on the compact sets (2),
  \(R_N(a)=1+O_p(N^{-p})\);
* there exist \(A,d,c_0>0\) and \(N_0\) such that, for
  \(N\ge N_0\) and \(1\le p\le c_0N\),
  \[
    |R_N(a)-1|\le A^{p+1}p!N^{-p}+N^A e^{-dN}.
    \tag{5}
  \]
  Consequently \(R_N(a)=1+O(N^A e^{-d_1N})\) for some \(d_1>0\).

The main estimates concern the boundary layer (3). Section 7 deduces
real-orbit propagation using the separate exact result [G, Section 6].
No complexification or arbitrary component-gluing theorem is used.

## 2. Exact packet and a simpler normalization identity

The complete retained packet of [P] is
\[
 \Phi_a=\mathcal A_N(a)S_N(a)+I_N(a),\qquad
 S_N(a)=\sum_{j=0}^{K_*}
 \frac{Q^j(Q^{1-a},rQ^a;Q)_j}{(Q,q^3rC;Q)_j}.
 \tag{6}
\]
Here \(\mathcal A_N\) is the pole-free amplitude in [P, (22)],
and \(K_*=\lfloor NR+\zeta\rfloor\), with the separated left-side
choice there. The source current is retained, not reset.
Put
\[
 \begin{gathered}
 B=N(1-c)-\tfrac12,\quad L_0=N(1-R),\quad
 D=N(1-c-R)+\tfrac12,\\
 \chi=-e^{\pi ic}\frac{\sin\pi R}{\sin\pi(c+R)},\qquad
 1+\chi=e^{-\pi iR}\frac{\sin\pi c}{\sin\pi(c+R)}.
 \end{gathered}
 \tag{7}
\]
The prescribed branch has \(-\pi<\arg\chi<0\) and
\(\arg(1+\chi)=-\pi R\). They stay away from zero and their cuts
on each fixed compact set.

Reflection and single steps of the canonical factorial give the useful
exact identity
\[
 \boxed{\quad
 \frac{\Gamma_N(a)}{\mathcal A_N(a)}
 =\mathcal P_N(a):=
 r^{a-1}Q^{a(a-1)}
 \frac{\mathfrak F(B)\mathfrak F(D)}
      {\mathfrak F(B+1-a)\mathfrak F(D+a-1)} .
 \quad}
 \tag{8}
\]
The power of \(r\) means \(\exp(-2\pi iR(a-1))\).
For verification, the single arguments of (4) are
\(B,N-a,L_0+a-1\); its pair arguments are
\(B+1-a,D+a-1,L_0\). Use
\(\mathfrak F(N-a)\mathfrak F(a-1)
 =Nq^{(N-a)(1-a)}\) in (4), then divide by the explicit amplitude
in [P, (22)]. Reflect the remaining \(NR-a\) factor against
\(L_0+a-1\). The scalar reduces to
\(r^{a-1}Q^{a(a-1)}\), giving (8).
At \(a=1\), (8) is exactly one.

Only macroscopic shifted factorials occur in (8). Their leading ratio is
\((1+\chi)^{a-1}\): its lifted logarithm is
\[
 (a-1)\{\log r+\log(1-C)-\log(1-Cr)\}
                  =(a-1)\log(1+\chi).
 \tag{9}
\]
The arguments in this equation have the marks just specified.
Let
\[
 \mathcal D_N(a)=\mathcal P_N(a)/(1+\chi)^{a-1}.
 \tag{10}
\]
First-order strip estimates give \(\mathcal D_N=1+O(\epsilon)\);
its logarithm tending to zero is therefore well-defined.

[P] supplies uniform bounds
\[
 |I_N(a)|\le N^A,\qquad
 |\Gamma_N(a)|\ge N^{-A}e^{NM_0},\qquad
 M_0=L(c+R)-L(c)-L(R)>0 .
 \tag{11}
\]
The latter also follows directly from (4), reflection at \(N-a\),
and bounded-argument Gamma comparison. Thus the current divided by
\(\Gamma_N(a)\) is exponentially small.

Choose a fixed integer \(\ell\ge a_+\). The exact interpolation used
in [P, (30)] is
\[
 T_N(v)=Q^v
 \frac{\mathfrak F(v+\ell-a)\mathfrak F(\ell)}
      {\mathfrak F(\ell-a)\mathfrak F(v+\ell)}
 \frac{\mathfrak F(L_0+a+\ell-1+v)}
      {\mathfrak F(L_0+a+\ell-1)}
 \frac{\mathfrak F(D+\ell)}{\mathfrak F(D+\ell+v)} .
 \tag{12}
\]
It is defined by this expression even when the finite coefficient
at \(\ell\) is zero. More explicitly, let \(R_k\) denote the \(k\)-th
summand of (6), and put
\[
 \begin{gathered}
 \mathcal B(v)=\frac{2\pi i}{e^{2\pi iv}-1},\qquad
 J_{\rm line}=\frac1{2\pi i}\int_{\rm line}
                                      \mathcal B(v)T_N(v)\,dv,\\
 \Re v=\gamma=-1/4\quad\hbox{or}\quad
 \Re v=\beta_N=NR+\zeta-\ell .
 \end{gathered}
 \tag{12a}
\]
Both lines are oriented upward. For all sufficiently large \(N\),
\(K_*\ge\ell\), and the exact splitting in [P] is
\[
 S_N(a)=\sum_{k=0}^{\ell-1}R_k+
                         R_\ell(J_{\rm right}-J_{\rm left}),
 \qquad R_\ell T_N(k)=R_{\ell+k}.
 \tag{12b}
\]
Neither the interpolation nor this identity is defined by dividing
by \(R_\ell\). On \(v=-1/4+iT\), its ordinary-Gamma model is
\[
 T_0(v)=e^{i\pi v}\chi^v
 \frac{\Gamma(v+\ell+1-a)\Gamma(\ell+1)}
      {\Gamma(\ell+1-a)\Gamma(v+\ell+1)}.
 \tag{13}
\]
Together with the Barnes kernel \(2\pi i/(e^{2\pi iv}-1)\), this
model has a bound
\[
 C(1+|T|)^C e^{-d|T|}.
 \tag{14}
\]
Here \(d>0\) is uniform because the compact \(\chi\)-set lies in the
open lower half-plane. All ordinary Gamma arguments on this line
have positive real parts: \(\ell+1-a\ge1\) and
\(\Re(v+\ell+1-a)\ge3/4\).

For any fixed small \(\eta>0\), [P, Sections 4--5] bounds the actual
left tail \(|T|\ge\eta N\) and right connector by \(N^A e^{-d_\eta N}\).
The right-connector loss is \(\min(M_0,\Delta)>0\).
Those estimates include the infinite ends. They are not replaced by
an asymptotic for the central model.

## 3. A graded strong logarithmic estimate

Use \(b_+=\max(b,0)\), so \(b_+!\) means \(\max(b,0)!\).
For a polynomial \(P(v)=\sum_m p_mv^m\), the useful coefficient
grading at order \(j\) is
\[
 \deg P\le j+1,\qquad |p_m|\le C^{j+1}(j-m)_+! .
 \tag{15}
\]
The high-degree coefficients have no extra \(j!\).

**Lemma 1.** After decreasing fixed positive constants \(\eta,c_0\),
the actual logarithm
\[
 L_N(v,a)=\log(T_N(v)/T_0(v))-\log\mathcal D_N(a)
 \tag{16}
\]
has polynomials \(l_j(v,a)\) satisfying (15), uniformly for real
\(a\in\mathcal A\), and, for
\(|T|\le\eta N,\ 1\le p\le c_0N\),
\[
 \begin{split}
 L_N&=\sum_{j=1}^{p-1}\epsilon^jl_j+\mathcal R_{N,p},\\
 |\mathcal R_{N,p}(v,a)|
 &\le C^{p+1}\epsilon^p
       \sum_{m=0}^{p+1}(p-m)_+!(1+|v|)^m,\\
 |L_N(v,a)|&\le C\epsilon(1+|v|^2).
 \end{split}
 \tag{17}
\]
The coefficients are polynomial in \(a\) as well. The last bound
does not concern a truncated logarithmic series.

We give the endpoint and macroscopic proofs separately. The following
elementary bound will be used for their exact integral kernels.
If a function \(b\) is bounded for real \(t\ge0\) and analytic on
\(|t|<r\), its Taylor coefficients and global real Taylor remainder
satisfy, for a constant \(A\),
\[
 |b_j|\le A^{j+1},\qquad
 \left|b(t)-\sum_{j<p}b_jt^j\right|\le A^{p+1}t^p
                \quad(t\ge0,\ p\ge1).
 \tag{17a}
\]
On \(t<r/2\) this is the Cauchy remainder. On \(t\ge r/2\),
divide the bounded function and its Taylor polynomial by \(t^p\);
the geometric sum of the coefficient bounds is at most
\(C(2/r)^p\). This proves (17a) globally.

### 3.1. Endpoint factors and their strong remainder

The exact Gamma product of [E] gives, for
\(-1+\rho\le\Re x\le M\) with fixed \(\rho>0,M\),
\[
 \log\mathfrak F_N(x)
 =x\log(-2\pi i\epsilon)+\log\Gamma(1+x)
       +\frac{\pi i\epsilon}2x(x+1)+\sum_{n\ge1}E_{Nn}(x),
 \tag{18}
\]
where
\[
 E_z(x)=\int_0^\infty\frac{e^{-zt}}t
 \left[2x+1-\frac{\sinh((x+1/2)t)}{\sinh(t/2)}\right]dt.
 \tag{19}
\]
To verify (19), differentiate in \(z\) using the elementary digamma
integral. The result is the derivative of
\(\log\Gamma(z+x+1)-\log\Gamma(z-x)-(2x+1)\log z\);
both expressions tend to zero as \(z\to+\infty\).
All Gamma logs here have positive-real-part arguments when \(N\)
is large. Their branches are fixed by continuation from bounded real
\(x\), not reset on the negative imaginary half-line.
Equivalently, summing the convergent Laplace factors before expanding
gives the exact single-integral formula
\[
 \sum_{n\ge1}E_{Nn}(x)=
 \int_0^\infty
 \frac{2x+1-\sinh((x+1/2)\epsilon u)/\sinh(\epsilon u/2)}
      {u(e^u-1)}\,du .
 \tag{19a}
\]
The cancellation of orders zero and one makes this integrable at zero.

Put \(z=x+1/2\) and \(d(t)=t/(2\sinh(t/2))\). The bracket in
(19) is exactly
\[
            2z\left[1-d(t)\frac{\sinh(zt)}{zt}\right].
 \tag{20}
\]
The function \(d\) is bounded on the positive real axis and analytic
at zero, so (17a) applies. Also
\(\sinh(zt)/(zt)=\int_0^1\cosh(uzt)\,du\).
Taylor's integral remainder for the exponentials in this integral
has bound
\[
       \frac{|z|^m t^m}{(m+1)!}e^{M t}
                  \quad (|\Re z|\le M).
 \tag{21}
\]
The exponential is independent of \(\Im z\). The same assertion
holds for an odd truncation by using its missing even coefficient.

Truncate the product (20) at total degree \(p-1\), expanding one
factor at a time. The global remainder (17a), the coefficient
bound for \(d\), and (21) give, on all real \(t\ge0\),
\[
 C^{p+1}t^p
       \sum_{m=0}^{p}\frac{(1+|z|)^{m+1}}{(m+1)!}e^{Mt}.
 \tag{22}
\]
The constant and linear terms vanish. Use the exact single integral
(19a) and choose \(N\ge2M+2\). Its remainder, for \(p\ge2\), is
bounded by
\[
 C^{p+1}\epsilon^p(p-1)!
       \sum_{m=1}^{p+1}\frac{(1+|z|)^m}{m!}.
 \tag{23}
\]
Indeed
\(\int_0^\infty u^{p-1}e^{M\epsilon u}/(e^u-1)\,du
\le C^p(p-1)!\) for \(p\ge2\), by geometric expansion or
comparison at zero and infinity. For \(m\le p-1\),
\((p-1)!/m!\le2^p(p-m)!\); the two remaining terms obey the
same bound with \(0!=1\). This proves precisely the graded estimate.

This estimate already covers the infinite integration interval;
there is no \(p\)-dependent unestimated tail. Its coefficient
polynomials have degree at most \(j+1\), by (20). Their degree-\(m\)
coefficient is bounded by \(C^{j+1}(j-1)!/m!\), which converts to
(15). The explicit quadratic term in (18) has the same grading.

For \(p=1\), (19) starts at \(t^2(1+|x|)^3\).
It is \(O(\epsilon^2(1+|x|)^3)\), which is
\(O(\epsilon(1+|x|)^2)\) when \(\epsilon|x|\le2\eta\).
The explicit quadratic term in (18) has the same bound.
This proves the endpoint part of (17).

The four endpoint terms in (12) are obtained from (18) at
\(x=v+\ell-a,v+\ell,\ell,\ell-a\), with their displayed signs.
Their leading powers of \(-2\pi i\epsilon\) cancel and their
ordinary Gamma quotient is exactly the one in (13).
Thus the calculation applies to the actual endpoint factors.

### 3.2. Macroscopic factors and their strong remainder

There is an exact summed Borel integral here, not only a formal
Stirling series. Put
\[
 b(t)=\frac{1/(e^t-1)-1/t+1/2}{t},\qquad
 K_w(u)=\frac{e^{-wu}-e^{-(1-w)u}}{1-e^{-u}} .
 \tag{25a}
\]
The function \(b\) is analytic for \(|t|<2\pi\), with \(b(0)=1/12\),
and is bounded for real \(t\ge t_0>0\). On \(0<\Re w<1\),
use the canonical functions
\[
 J(w)=\int_0^w\operatorname{Log}(2\sin\pi t)\,dt,\quad
 \mathfrak f(w)=J(w)+\tfrac{\pi i}{2}(w^2-w),\quad
 \mathfrak h(w)=\sqrt{2\sin\pi w}\,e^{\pi iw/2},
\]
with the roots and primitive continued from the positive real strip.
Then
\[
 \boxed{\quad
 \log\mathfrak F_N(Nw)
 =N\mathfrak f(w)+\tfrac12\log N+\log\mathfrak h(w)
                   +\epsilon\int_0^\infty b(\epsilon u)K_w(u)\,du .
 \quad}
 \tag{25}
\]
To derive it, write ordinary Gamma as its elementary Stirling part
plus its exact Binet remainder
\(R(z)=\int_0^\infty b(t)e^{-zt}\,dt\).
The canonical product [E] has remainder
\[
 R(Nw)+\sum_{n\ge1}
          \{R(N(n+w))-R(N(n-w))\}.
\]
Its Laplace kernel sums exactly:
\[
 e^{-Nwt}+
 \frac{e^{-Nwt}-e^{Nwt}}{e^{Nt}-1}=K_w(Nt).
\]
The sum and integral may be interchanged: the paired difference has
an integrable bound \(CN|w|\,t e^{-N(n-\Re w)t}\), summable after
integration. The elementary Stirling parts sum to
\(NJ(w)+\tfrac12\Log(2N\sin\pi w)\), by the sine product and
its primitive, as in [E]. Adding the explicit marking phase gives
\(\mathfrak f,\mathfrak h\) in (25). This fixes the constant and its branch.

For the actual bounded shift \(s\), substitute
\(w=u_0+\epsilon(s+v)\), where
\(\delta\le u_0\le1-\delta\). The integrand in the last term is
\[
 \epsilon b(\epsilon u)
 \frac{e^{-u_0u}e^{-\epsilon(s+v)u}
       -e^{-(1-u_0)u}e^{\epsilon(s+v)u}}{1-e^{-u}} .
 \tag{26}
\]
Its term with no \(u\)-power retains the difference of the two
exponentials; this cancels the apparent singularity at \(u=0\).
All other terms have at least one \(u\)-power.

Expand \(b(\epsilon u)\) and the two exponentials to total order
\(p-2\). The order-\(j\) coefficient, \(j\ge2\), with degree \(m\)
in \(s+v\), has \(m\le j-1\) and a bound
\[
 \frac{C^{j-m}}{m!}
   \int_0^\infty
       \frac{u^{j-1}e^{-\delta u}}{1-e^{-u}}\,du
       \le C_1^{j+1}(j-1)!/m!.
 \tag{27}
\]
The integral is finite for \(j\ge2\), and is bounded by the sum of
two elementary Gamma moments. The order-one coefficient is the
finite integral \(b(0)\int K_{u_0}\), independent of \(v\).
Thus (27) converts to the deficit bound (15).

The same calculation gives a strong remainder on the entire
positive integration axis. Use (17a) for \(b\) and the exponential
integral remainder. Since
\(\Re(s+v)\) is bounded, its modulus is \(e^{C\epsilon u}\),
independent of \(T\). The total-order-\((p-1)\) remainder of the
product in (26) is bounded by the corresponding sum of moments
in (27), at \(j=p\); no derivative bound introduces a second
factorial. The \(p=1\) bound is immediate from (25), uniformly
for the shifted \(w\) in a smaller strict strip.

To spell out convergence in this strong estimate, each exponential
remainder is multiplied by \(e^{-u_0u}\) or \(e^{-(1-u_0)u}\).
For \(N\) large its product with \(e^{C\epsilon u}\) is bounded
by \(e^{-\delta u/2}\). For total order at least one, its
near-zero moment is integrable after division by \(1-e^{-u}\);
the order-zero term retains the cancellation in \(K_{u_0}\).
Thus the Gamma moments used in (27) integrate the full remainder.
There is no appeal to a fixed-order asymptotic outside its domain.

Finally expand the analytic principal term \(N\mathfrak f\), subtracting
its constant and linear model. At order \(j\) its degree is at
most \(j+1\), with coefficient \(O(C^j)\); its convergent
Taylor remainder is
\(C^{p+1}\epsilon^p(1+|v|)^{p+1}\).
The logarithmic amplitude is analytic and has degree at most \(j\)
at order \(j\), with the same type of convergent remainder.
These are exactly the top-degree terms permitted in (17).
This completes the macroscopic strong estimate directly from
the exact integral, without an unproved uniform-order Stirling step.

In the actual (12), take
\[
 u_1=1-R,\ s_1=a+\ell-1,\qquad
 u_2=1-R-c,\ s_2=\ell+\tfrac12.
 \tag{28}
\]
Its macroscopic log is
\[
 \log\frac{\mathfrak F(Nu_1+s_1+v)}{\mathfrak F(Nu_1+s_1)}
 -\log\frac{\mathfrak F(Nu_2+s_2+v)}{\mathfrak F(Nu_2+s_2)}.
 \tag{29}
\]
Its linear model is
\(v\{\log(1-r)-\log(1-rC)\}
 =v(i\pi+\log\chi)\).
The extra \(Q^v\) contributes \(2\pi i\epsilon v\).
The normalizer (10) uses only the macroscopic arguments in (8);
its constant model is zero by (9). Thus (18)--(29) give (17)
for exactly (16), not for a substitute integrand. All shifts are
affine in \(a\), so coefficient polynomiality in \(a\) is retained.
This proves Lemma 1.

## 4. Exponentiation without losing a factorial

**Lemma 2.** Integrating the expansion of \(e^{L_N}\) against the
model Barnes weight has a strong remainder
\[
                    C^{p+1}p!\epsilon^p,\qquad p\le c_0N.
 \tag{30}
\]
Its order-\(j\) coefficient is the integral of a polynomial in
\(v,a\) of \(v\)-degree at most \(2j\).

First truncate the exponential itself after \(p-1\) powers.
Its exact remainder is at most
\(|L_N|^p e^{|L_N|}/p!\). By (14), (17), and the choice of \(\eta\),
its integral is bounded by
\[
 \frac{(C\epsilon)^p}{p!}
       \int_{\mathbb R}(1+|T|)^{2p+C}e^{-d|T|/2}\,dT
 \le C_1^{p+1}\epsilon^p(2p+C)!/p!
 \le C_2^{p+1}p!\epsilon^p.
 \tag{31}
\]

For a finite power \(L_N^k\), expand to total order \(p-1\)
by successive substitution of the strong logarithmic expansion.
Each remainder term has formal factors, one logarithmic remainder,
and any remaining exact factors. Assign order one and degree at
most two to each exact factor using (17). The assigned total order
is \(p\). If there are \(k\) factors of orders \(j_i\) and selected
degrees \(m_i\), then
\[
 \sum j_i=p,\quad \sum m_i\le p+k,\quad
 q:=\sum(j_i-m_i)_+\le p+k-\sum m_i.
 \tag{32}
\]
The product of their deficit factorials is at most \(q!\).
The Barnes moment, including the exponential coefficient \(1/k!\),
is consequently bounded, after increasing \(C^p\), by
\[
 \frac{(\sum m_i)!\,q!}{k!}
 \le\frac{(p+k)!}{k!}
 \le\frac{(2p)!}{p!}\le4^pp!.
 \tag{33}
\]
The fixed polynomial factor in (14) changes only \(C^p\).
There are at most exponentially many order compositions, factor
positions, and degree choices: for each positive \(j_i\),
\(j_i+2\le3^{j_i}\). This proves (30) for the finite powers.
The same calculation proves the coefficient bound.

Finally extend each coefficient integral from \(|T|\le\eta N\)
to the whole line. On the omitted set,
\(e^{-d|T|}\le e^{-d\eta N/2}e^{-d|T|/2}\).
The coefficient moment estimate just proved, with \(d\) halved,
therefore bounds the order-\(j\) tail by
\(e^{-d\eta N/2}C_3^{j+1}j!\).
After multiplication by \(\epsilon^j\), the sum through \(p-1\)
is bounded by \(Ce^{-d\eta N/2}\) if \(C_3c_0<1/2\).
The true outer pieces retain their independent exponential bounds
from Section 2. This proves Lemma 2 for the whole retained packet.

## 5. Polynomial jets at generic fractional parameters

Expand a finite packet term first, carrying its integer-zero factor:
\[
 R_k=r_k\left(1+\sum_{j\ge1}\epsilon^jP_j(k,a)\right),\qquad
 r_k=\binom{a-1}{k}\chi^k .
 \tag{34}
\]
The factor multiplying \(r_k\) has a removable interpretation at
each zero of the binomial. Indeed
\((1-e^{2\pi i\epsilon x})/x\) is analytic at \(x=0\).
Expanding its logarithm and the nonzero macroscopic factors, then
summing powers of the finite product index, proves that \(P_j\)
is polynomial in \(k,a\). No parameter denominator from a zero
binomial is introduced.

Coefficient matching uses the whole term in (12b), not bare \(T_N\).
The finite prefactor has a factorization
\[
 R_\ell=r_\ell A_\ell(\epsilon,a),\qquad A_\ell(0,a)=1,
 \tag{34a}
\]
where \(A_\ell\) is a bounded analytic factor for \(\epsilon\) in a
fixed disk, uniformly on the \(a\)-compact. To see this at its
integer zeros, factor each light product by its linear term and use
the entire function \((1-e^{2\pi ix})/(-2\pi ix)\), whose value at
zero is one. All remaining finite macroscopic denominators are
nonzero in a fixed disk. This carries the zero in \(r_\ell\);
it does not divide the source by a zero coefficient.

Expand \(A_\ell\) as well as the raw correction \(T_N/T_0\).
After multiplying them, the order-\(j\) whole-term coefficient is
\[
                  r_{\ell+v}P_j(\ell+v,a),
                  \qquad r_{\ell+v}:=r_\ell T_0(v).
 \tag{34b}
\]
Indeed Section 3 gives polynomial correction coefficients in \(v,a\);
at every nonnegative integer \(v=k\), the exact second identity in
(12b) identifies them with the expansion of \(R_{\ell+k}\) in
(34). Equality at all these integers fixes the correction polynomial.
One may first verify this off the integer zeros of \(r_\ell\);
the factored whole expressions then continue through those zeros.
If the already-normalized logarithm \(L_N\) in (16) is used instead,
these are the raw polynomials convolved with the jets of
\(\mathcal D_N^{-1}\). They are not the raw polynomials of bare
\(T_N\). This also rules out an extra periodic interpolation term.
For \(|\chi|<1\), coefficientwise summation gives
\[
 \sum_{k\ge0}r_kP_j(k,a)
       =P_j(\chi\partial_\chi,a)(1+\chi)^{a-1}.
 \tag{35}
\]
The finite-head/Barnes splitting continues this identity throughout
the lower half-plane in \(\chi\). For this continuation treat the
coefficient parameters of \(P_j\) as fixed and \(\chi\) as the
independent model variable. Polynomial moments of \(v\) are
derivatives of the convergent model Barnes integral; its exponential
decay justifies those derivatives. The Taylor-remainder identity in
[P] then proves (35), including integer \(a\).

After division by \((1+\chi)^{a-1}\), the right side is polynomial
in \(a\), with rational \(\chi\)-denominators independent of \(a\).
The normalizer (10) has polynomial-in-\(a\) jets by Section 3.
The finite-head terms are finite products and have the same strong
remainder, also when their explicit binomial factor vanishes.
Indeed their removable analytic factors have a fixed convergence
radius in \(\epsilon\); multiplying their geometric coefficient bounds
by the Gevrey bound for \(\mathcal D_N^{-1}\) costs at most another
constant to the power \(p\), since \(j!(p-j)!\le p!\).
This statement applies in particular to the finite prefactor
\(R_\ell\) in (12b), using (34a). Thus its expansion and its
normalization have been included in the central remainder estimate.
Thus Lemmas 1--2 and the retained current give
\[
 R_N(a)=1+\sum_{j=1}^{p-1}C_j(a;c,R)N^{-j}
           +\mathcal E_{N,p}(a),\qquad
 |\mathcal E_{N,p}|
 \le A^{p+1}p!N^{-p}+N^Ae^{-dN}.
 \tag{36}
\]
Each \(C_j\) is polynomial in \(a\). The coefficient formula is
independent of the auxiliary fixed \(\ell\): changing \(\ell\)
is the exact finite-head/Barnes identity before expansion.
The cyclic characters in the current and right connector occur
only in the exponentially small term of (36).

## 6. Rigidity and optimal truncation

There are two ways to calibrate the polynomial coefficients.
The affine identity of [G] makes \(R_N(a+1)-R_N(a)\)
exponentially small on each fixed \(a\)-compact. Its explicit
forcing is polynomially bounded, while the Gamma denominator
grows as \(e^{NM_0}\). Hence \(C_j(a+1)=C_j(a)\);
a periodic polynomial is constant. At \(a=1\), the exact source
is \(\Gamma_N(1)+I_N(1)\), so the constant is zero.

One can instead use the integer packets of [G, Section 7].
For every fixed positive integer \(m\), their terminating identity
is exactly
\[
 S_N(m)=\mathcal P_N(m)
 \tag{37}
\]
once \(N\) is large enough that the actual packet cutoff includes
its \(m-1\) terms. The original current remains, but divided by
\(\Gamma_N(m)\) it is exponentially small. Thus \(C_j(m)=0\)
for every positive integer \(m\), and polynomiality again gives
\(C_j=0\). This argument compares one fixed integer at a time;
it does not assert packet termination up to every \(m<N\) at a
fixed \(R\).

For fixed \(p\), (36) now proves the fixed-order conclusion
without any choice of growing truncation order. For the stronger
claim choose
\[
 p=\lfloor c_1N\rfloor,\qquad
 0<c_1<\min(c_0,1/(2A)).
 \tag{38}
\]
Since \(p!\le p^p\), the first error in (36) is at most
\(A(Ap/N)^p\le A2^{-p}\). Together with the retained exponential
errors this proves (5) and its exponential corollary.
Formal rigidity enters only after the strong remainder (36).

## 7. Direct-sum real-orbit consequence and scope

Using only [G, Section 6], the exponential initializer also yields
an endpoint-uniform real-orbit estimate. For \(0\le h\le R\), choose
\[
 h_0=\{Nh\}/N,\qquad a=Nh_0+\tfrac12\in[1/2,3/2).
\]
The initializer applies uniformly on the closed compact
\([1/2,3/2]\), which contains this half-open \(a\)-range.
There are at most \(N\) real steps from \(h_0\) to \(h\).
The exact affine identity and the uniform Gamma lower bound in
[G, (33b)--(33e)] therefore give
\[
 \frac{\Phi(c,h,R-h)}{\Gamma_N(c,h,R-h)}
          =1+O(N^A e^{-d_2N})\qquad(0\le h\le R),
 \tag{39}
\]
for a positive compact-dependent \(d_2\). This retains the exact
Gamma boundary layers rather than replacing them by the interior
WKB amplitude.

This is a real compact-parameter exponential initializer for the
original finite crossing source relative to its specified Gamma
section. It does not assert their exact equality, erase the Gamma
section's cyclic norm, discard another source channel, or replace
an arbitrary short component by this local source.
Orbit propagation uses the separately proved affine equation [G].
Complexification and general marked gluing are not proved here.

The quantitative step distinguishing the fixed-order and exponential
conclusions is Lemma 1 together with the exponentiation estimate in
Lemma 2. In particular no fixed complex tube at \(h=0\) follows
from (39): the nonzero factorial-strip margin there shrinks with
\(N\). Any fixed complex-tube assertion must instead start on
compact sets of strictly positive \(c,h,k\).

| Label | Complete direct proof source | SHA-256 |
|---|---|---|
| P | notes/research_four_coherent_zero_radius_boundary_source.md | f74a6b951936f29f5cf66e4b34cfc84b2c890b1ba5464f472ca023aa70c5c621 |
| F | notes/research_four_coherent_fractional_boundary_source.md | 8126481cadaa4b1b0ba287495de14cb3263baf8343fbfca9aa4d5b6d962595b1 |
| E | notes/exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| G | notes/research_crossing_exact_gamma_source_extension.md | f19221b384ae9c2de47beee8460df4eee30f3419df6cf0478c18569b3f464495 |

All four entire matching direct texts were read and their hashes renewed.
Only written mathematics and text operations were used. No mathematical
programs, numerical experiments, tests, builds, or git operations were run.
