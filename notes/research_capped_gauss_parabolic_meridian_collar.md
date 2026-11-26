# The capped Gauss scalar near the complete meridian

23 November 2026. The meridian parameter is scaled as \(M=\exp(v/\sqrt N)\).

The actual capped Gauss initializer admits a scalar-relative asymptotic
on the meridian scale \(M=\exp(v/\sqrt N)\). Its ordinary quantum-dimension
zeros are retained and divided removably. The remaining transport factor
has an explicit nonzero Gaussian limit, jointly with the original
binomial cap on its complex Gaussian activity collar.

The quantum root and the physical Fourier frames are fixed throughout.
This is a statement about the specified initialized period, not the
original marked knot closing or an arbitrary Conway exterior.

## 1. Actual source and the statement

Use the adopted whole-meridian terminal row of (MC1)--(MC7). Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad x_0=-q^{-1},
 \qquad \ell=d-T\ge1,\quad t=N-2\ell>0,\quad
 \alpha_N=\ell/N\in I\Subset(0,1/2).
 \tag{PC1}
\]
The limit is through these admissible levels. On the physical degree
\(T\) basis \(|a,T-a\rangle\), \(0\le a\le T\), let \(A(M)\) be the
actual capped operator \(q_F(M)E_\Sigma(M)^di_d\). In particular its
meridian family includes the original lowering coefficients
\(E(M)w_a=(MQ^{-a}-M^{-1})w_{a-1}\), with bottom zero, and all its
ordered Cartan factors. This is not a generic lift chosen from \(A(1)\).

Write \(A_0=A(1)\), \(a_*=\lfloor\ell/2\rfloor\), and
\[
 \begin{gathered}
 D_{aa}=x_0^a q^{-Ta},\qquad
 (F_c)_{ab}=N^{-1/2}Q^{(a-T/2)(b-T/2)},\\
 \beta_b=\binom db\binom d{T-b},\qquad
 c_T(z)=\sum_{b=0}^T\beta_bz^b|b,T-b\rangle,\\
 \mathscr S_N(u,z)
   =e_T^{\mathsf T}\bar D A(e^{u/N})\bar D F_c c_T(z),\\
 f_N(u)=\frac{A(e^{u/N})_{T,a_*}}{(A_0)_{T,a_*}},\qquad
 d_N(u)=\frac{\sinh u}{N\sinh(u/N)} .
 \end{gathered}
 \tag{PC2}
\]
Values at zero are removable. The bars in \(\bar D\) refer to the
fixed root frame; neither \(D\) nor \(F_c\) is differentiated.
In particular \(\beta_b\) are the ordinary capped binomials, without
square roots or a new gauge.

For \(0<\alpha<1/2\), define
\[
 \begin{gathered}
 A_\alpha=\pi\cot(\pi\alpha/2),\qquad
 V_\alpha=(1-\alpha^2)/8,\qquad
 H_\alpha=A_\alpha+2\pi^2V_\alpha,\\
 \kappa_\alpha
   =2+i\{\cot(3\pi\alpha/2)-2\cot(\pi\alpha/2)\},\\
 \mathcal E_\alpha(v,\zeta)=
 \exp\left\{\frac{\kappa_\alpha^2v^2}{4H_\alpha}
             +\frac{i\pi V_\alpha\kappa_\alpha v\zeta}{H_\alpha}\right\}.
 \end{gathered}
 \tag{PC3}
\]
Here \(A_\alpha,V_\alpha,H_\alpha\) are positive real numbers.
For every fixed \(0<V,Z<\infty\), the following quotient is holomorphic
after removal of its ordinary zeros, for all sufficiently large
admissible levels:
\[
 \boxed{\quad
 \frac{\mathscr S_N(\sqrt N\,v,\,
                         q^{t-1}e^{\zeta/\sqrt N})}
      {f_N(\sqrt N\,v)\,
             \mathscr S_N(0,q^{t-1}e^{\zeta/\sqrt N})}
   =\mathcal E_{\alpha_N}(v,\zeta)+o_{I,V,Z}(1),
 \qquad |v|\le V,\quad|\zeta|\le Z .
 \quad}
 \tag{PC4}
\]
Convergence is uniform on these complex disks. It holds with every
fixed derivative on smaller disks. In particular the divided quotient
is nonzero there for large \(N\). Its scale is \(\mu=v/\sqrt N\);
an order-\(j\) original \(\mu\)-derivative carries the factor \(N^{j/2}\).
No relative error rate beyond \(o(1)\) is asserted.

## 2. Exact meridian products and the cap phases

The literal root terminal row, including its support, is
\[
 (A_0)_{Ta}=c_*q^{a^2}{\ell\brack a}_Q
       =c_*q^{\ell a}B_a,\quad
 B_a=\frac{S_\ell}{S_aS_{\ell-a}}>0\quad(0\le a\le\ell),
 \qquad (A_0)_{Ta}=0\quad(a>\ell),
 \tag{PC5}
\]
where \(S_j=\prod_{h=1}^j2\sin(\pi h/N)\) and
\(c_*=(-1)^{\ell+1}Nq^{2\ell^2+\ell+1}\).
This is the evaluated terminal column followed by the actual generic
transpose adapter, not differentiation of root symmetry.

For \(a\le\ell\), set \(R_a(u)=A(e^{u/N})_{Ta}/(A_0)_{Ta}\).
The exact row product (MC6) gives
\[
 \begin{split}
 R_a(u)&=d_N(u)g_a(u),\\
 g_a(u)&=
 e^{u[\,2d-3(T-a)\,]/N}
 \prod_{j=T+1}^{T+a}\frac{1-e^{-4u/N}Q^j}{1-Q^j}
 \prod_{j=T-a+1}^{T}\frac{1-Q^j}{1-e^{-2u/N}Q^j}.
 \end{split}
 \tag{PC6}
\]
Thus \(f_N=d_Ng_{a_*}\). On any disk \(|u|\le C\sqrt N\),
all factors of \(g_{a_*}\) are units for sufficiently large \(N\):
their indices remain a fixed fraction of \(N\) from zero modulo \(N\).
The same holds for \(g_a\) on
\(\ell/4\le a\le3\ell/4\). Logarithms there are continued from \(u=0\).

Let \(k=t-1=T-\ell\), \(x_a=(a-\ell/2)/\sqrt N\), and put
\[
 H_N(w)=\sum_{b=0}^T\beta_b
                   \exp\{w(b-T/2)/\sqrt N\},\qquad
 C_N=\frac{c_*\bar D_{TT}}{\sqrt N}
                      q^{(T^2-\ell T)/2}.
 \tag{PC7}
\]
The part of the actual period with \(a\le\ell\) is exactly
\[
 C_Nd_N(u)e^{\zeta T/(2\sqrt N)}
       \sum_{a=0}^\ell B_ag_a(u)H_N(\zeta+2\pi i x_a),
 \qquad z=q^ke^{\zeta/\sqrt N}.
 \tag{PC8}
\]
Indeed \(q^{\ell a}\bar D_{aa}=1\), since
\(q^{\ell+T}\bar x_0=q^d\bar x_0=1\).
The remaining Fourier phase is
\[
 Q^{(a-T/2)(b-T/2)}q^{kb}
  =q^{(T^2-\ell T)/2}
       \exp\{2\pi i(a-\ell/2)(b-T/2)/N\}.
 \tag{PC9}
\]
The expression (PC8) has a separate \(a>\ell\) tail when \(u\ne0\).
That tail is estimated below, not set to zero.

At \(\zeta=0\), the head weights in (PC8) are positive and even about
\(\ell/2\): the palindromic negative-root polynomial (NR3) has positive
centered character at \(\theta=(2a-\ell)\pi/N\), \(|\theta|<\pi\).
The proof below uses the exact complex-\(\zeta\) expression (PC8)
and proves its needed nonzero Gaussian limit directly.

## 3. The two actual Gaussian limits

Choose \(a_*=\lfloor\ell/2\rfloor\). Uniformly on \(I\), the root
sine-binomial ratios give
\[
 \frac{B_{a+1}}{B_a}
   =\frac{\sin((\ell-a)\pi/N)}{\sin((a+1)\pi/N)},\qquad
 \frac{B_a}{B_{a_*}}\le C_Ie^{-c_Ix_a^2},\qquad
 \frac{B_a}{B_{a_*}}\longrightarrow e^{-A_\alpha x^2}
 \tag{PC10}
\]
when \(x_a\to x\) and \(\alpha_N\to\alpha\).
For completeness the derivative of the logarithm of this ratio is
negative with magnitude at least \(c_I/N\) on the entire index interval,
by sine addition. At the center that derivative is
\(-2A_\alpha/N+O_I(N^{-2})\). Summation proves both claims, including half-integer
centers. Also \(B_{a_*}\ge e^{c_IN}\) for large \(N\):
its logarithm divided by \(N\) tends to
\(J(\alpha)-2J(\alpha/2)>0\), where
\(J(s)=\int_0^s\log(2\sin\pi y)\,dy\).
Strict positivity follows from strict convexity of \(J\) on \((0,1/2)\).

The original binomials have a second, different Gaussian limit:
\[
 \frac{H_N(w)}{H_N(0)}
       \longrightarrow \exp(V_\alpha w^2/2),
 \tag{PC11}
\]
locally uniformly for complex \(w\), uniformly on \(I\).
Here is an elementary justification. Their exact consecutive ratio is
\[
 \frac{\beta_{b+1}}{\beta_b}
    =\frac{(d-b)(T-b)}{(b+1)(\ell+b+1)}.
 \tag{PC12}
\]
The coefficients \(\beta_b\) are symmetric about \(T/2\).
Summing the central logarithmic
expansion gives
\(\beta_b/\beta_{\lfloor T/2\rfloor}\to
\exp[-y^2/(2V_\alpha)]\), \(y=(b-T/2)/\sqrt N\).
The four linear factors in (PC12) give a global upper bound
\(C_Ie^{-c_Iy^2}\). These estimates normalize the Riemann sums,
give convergence of every exponential moment on compact \(w\)-sets,
and prove (PC11). In particular, for real \(x\) and \(|\zeta|\le Z\),
\[
 |H_N(\zeta+2\pi ix)|\le C_{I,Z}H_N(0).
 \tag{PC13}
\]
This bound controls all real \(x\), not merely a fixed central interval.

The meridian ratio has the matching local limit
\[
 \frac{g_a(\sqrt N\,v)}{g_{a_*}(\sqrt N\,v)}
       \longrightarrow \exp(\kappa_\alpha vx)
 \tag{PC14}
\]
for bounded complex \(v\) and bounded \(x_a\to x\).
In fact the exact logarithmic consecutive quotient from (PC6) is
\[
 \frac{3u}{N}
 +\log\frac{1-e^{-4u/N}Q^{T+a+1}}{1-Q^{T+a+1}}
 -\log\frac{1-e^{-2u/N}Q^{T-a}}{1-Q^{T-a}} .
 \tag{PC15}
\]
For \(u=\sqrt N\,v\) its first term in \(u/N\), at \(a=\ell/2+O(\sqrt N)\),
has coefficient
\(3-4/(1-e^{i\pi\alpha})+2/(1-e^{3i\pi\alpha})
=\kappa_\alpha\).
The quadratic remainder per step is \(O_{I,V}(N^{-1})\);
the variation of the first coefficient over \(O(\sqrt N)\) steps
is \(O_{I,V}(N^{-1/2})\) after summation.
This proves (PC14). On the whole central fraction one also obtains
\[
 \left|\frac{g_a(\sqrt N\,v)}{g_{a_*}(\sqrt N\,v)}\right|
                  \le C_{I,V}e^{C_{I,V}|x_a|}.
 \tag{PC16}
\]
All logarithms used for these estimates are of actual central units.

## 4. Growing ordinary zeros and the remaining coordinates

We justify division before taking the head limit. The Laurent row
formula (MC7), with \(k_a=T-a\), has, apart from a unit monomial
and a nonzero constant, the factors
\[
 (M^{-2}Q;Q)_{k_a}
 (M^{-2}Q^{T+1};Q)_\ell
 (M^{-4}Q^{T+1};Q)_a .
 \tag{PC17}
\]
At \(M=q^{-j}\), \(1\le j\le\ell\), the middle factor vanishes.
At \(M=q^j\), \(t\ge3j+1\), either \(k_a\ge j\) and the first
factor vanishes, or \(k_a<j\) and
\(T+a\ge2T-j+1=N+t-j-1\ge N+2j\), so the last factor vanishes.
It contains \(1-M^{-4}Q^{2j}\), hence the simple divisor
\(1-M^{-2}Q^j\). These statements apply to every physical row entry.
Since \(\ell,t\) grow proportionally to \(N\), they cover every
\(u=i\pi j\), \(|u|\le C\sqrt N\), for any fixed \(C\), at large \(N\).
Thus division by \(d_N(u)\), and then by the central unit
\(g_{a_*}(u)\), is holomorphic on each such disk.

Here are uniform bounds for the omitted indices. Choose radii
\[
 R_N=\pi(k_N+1/2),\qquad R_N/\sqrt N\longrightarrow V+1 .
 \tag{PC18}
\]
Every point of \(|u|=R_N\) is at distance at least \(\pi/2\) from
\(i\pi\mathbb Z\). On these circles, any interval product of
the nonzero-root factor ratios in (PC6), or their needed inverse
denominator ratios, is at most
\(\exp[C_{I,V}\sqrt N\log(N+1)]\).
Indeed numerator ratios are bounded by
\(1+C_V\sqrt N/\min(j,N-j)\).
For inverse ratios, the \(O_V(\sqrt N)\) indices nearest the endpoints
are bounded individually by a polynomial in \(N\), using the circle
separation. On all other indices the relative perturbation is small;
summing its harmonic bound gives the same estimate.
Moreover
\[
 |d_N(u)|^{-1}\le C_V\sqrt N,\qquad
 |g_{a_*}(u)|+|g_{a_*}(u)|^{-1}\le e^{C_{I,V}\sqrt N}
 \quad (|u|=R_N).
 \tag{PC19}
\]
The first follows from the separated zeros of \(\sinh u\);
the second follows by expanding only the central unit products.

For \(a\le\ell\) outside the central fraction, (PC10) has an
exponential loss relative to \(B_{a_*}\). It absorbs all the losses
above. For \(a>\ell\), extract the unique zero factor \(1-M^{-4}\)
in (PC17). The exact first-normal tail (MC10)--(MC11) bounds
the remaining root product by a polynomial in \(N\).
Comparison of its nonzero factors with their root values therefore
gives only \(\exp[C_{I,V}\sqrt N\log(N+1)]\), times a polynomial.
The factor \(|1-e^{-4u/N}|\) is \(O_V(N^{-1/2})\) on the circle.
After division by (PC19), this is still exponentially smaller than
the root scale \(B_{a_*}\). The original tail is fully retained here.

Multiplication by the cap costs no new relative exponential:
\(\|c_T(q^{t-1}e^{\zeta/\sqrt N})\|_2
\le C_{I,Z}e^{\operatorname{Re}\zeta\,T/(2\sqrt N)}\|\beta\|_2\),
by the Gaussian bound from (PC12). The frozen Fourier matrix is a
compression of a unitary matrix, and \(\bar D\) is unitary.
Also \(\|\beta\|_2/H_N(0)\) is polynomially bounded by (PC12).
Consequently, after the common normalization in (PC8) and division
by \(g_{a_*}\), both omitted parts are
\(\exp[-c_IN+C_{I,V}\sqrt N\log(N+1)]\) on the circles,
up to fixed powers of \(N\).
Their divided expressions are holomorphic by (PC17).
The maximum principle, for each fixed \(\zeta\) and uniformly on
its disk, gives the same vanishing bound on \(|u|\le V\sqrt N\).
No path bypasses an ordinary zero and no cap coordinate is removed.

## 5. Evaluation of the relative limit

Apply (PC10)--(PC16) to the central part of (PC8).
The Gaussian bound times \(e^{C_V|x|}\) is integrable, uniformly
on the stated complex parameter disks. Dominated Riemann sums give
\[
 \frac{1}{\sqrt N B_{a_*}H_N(0)}
 \sum_{a=0}^\ell
 B_a\frac{g_a(\sqrt N\,v)}{g_{a_*}(\sqrt N\,v)}
                     H_N(\zeta+2\pi ix_a)
 \longrightarrow
 I_\alpha(v,\zeta)
 :=\int_{\mathbb R}
 e^{-A_\alpha x^2+\kappa_\alpha vx
                     +V_\alpha(\zeta+2\pi ix)^2/2}\,dx .
 \tag{PC20}
\]
The omitted-coordinate estimates make this the limit of the
entire divided actual period, with the same normalization.
The convergence is uniform for \(\alpha=\alpha_N\in I\), by the
same uniform estimates or compactness in \(\alpha\).

The real quadratic coefficient is \(H_\alpha>0\), so direct completion
of the square, continued holomorphically in \(v,\zeta\), yields
\[
 I_\alpha(v,\zeta)=
 \sqrt{\frac{\pi}{H_\alpha}}\,
 \exp\left\{\frac{V_\alpha\zeta^2}{2}
       +\frac{(\kappa_\alpha v+2\pi iV_\alpha\zeta)^2}
                    {4H_\alpha}\right\}.
 \tag{PC21}
\]
In particular \(I_\alpha(0,\zeta)\) never vanishes and is uniformly
bounded away from zero on each compact parameter set.
At \(u=0\) there is no \(a>\ell\) tail. Division of (PC20) by its
actual root counterpart therefore proves (PC4), since
\[
 \frac{I_\alpha(v,\zeta)}{I_\alpha(0,\zeta)}
       =\mathcal E_\alpha(v,\zeta).
 \tag{PC22}
\]
This also directly proves the needed nonzero root cap on the
Gaussian activity collar, with the original phases and binomials.

The quotient in (PC4) is holomorphic on slightly larger fixed disks,
including every removable ordinary zero. Cauchy gives all fixed
\(v,\zeta\) derivatives on smaller disks. Since the limiting
exponential is nonzero, the quotient is a unit there for large \(N\).
The only zeros of the actual period in this growing scaled-\(u\)
domain are consequently the simple ordinary zeros
\[
 v_j=i\pi j/\sqrt N,\qquad j\ne0,\quad |v_j|\le V,
 \tag{PC23}
\]
with the evident restriction to the chosen disk boundary.
Their divided normals are obtained by differentiating the retained
factor \(f_N(\sqrt N\,v)\); they are not deleted by normalization.

The gain over (QD11) is the genuine meridian scale \(N^{-1/2}\),
with an explicit nonconstant joint transport factor and all its
fixed scaled jets. A fixed meridian disk is still outside the result.
All outer routing factors, their meridian derivatives, further
crossings, turns, external scalars and the marked closing remain
as in the original source. No assertion about their noncancellation,
the degree of the original quantum cycle, or arbitrary short fillings
is made.

## Complete inputs and coverage

The adopted complete proof sections used are (MC1)--(MC23),
(FH1)--(FH21), and their exact source conventions in
notes/research_finite_exceptions_progress.md. The complete (QD1)--(QD12)
and (NR1)--(NR12) were also read; the growing-zero and Gaussian-cap
arguments needed here are written above. At author freeze the complete
ledger SHA256 is b7ba8e8229e4317029df825660b25466ede91f3f274756dd836610f09e91cb30.
Its preceding fixed-jet section is comparison coverage only.

The complete original-source proof texts were retained whole at their
renewed matching pins: C549 b4fb801a1482316aebb4799f1d0b80d5b43ced39138d903c04cfde811ca166b0;
F428 7589bb0f796a874608b9e558aac1f78699884f0003da4a73ba52778c1edba66e;
G489 42e6d6c3a5039859c241a2832de56301eff49d749db86d67868f3534c89aaaaa;
O639 d52c6dd8e62f575a262fc7af460e258f7cb0e40b5a9c037ac46dd8d151002d44;
I623 abd8009aa0e0e729efe82450a4f838fe1bdf250574cedf82a7c84a51e2e1de8e;
M482 bf9bd5c282d478c9cfff7c93da5546a76177315724292c33dea528d5e1dd729f;
L487 7f8c7c0be05331e7c0679c5a26374bbcb4b38b817c36a1f4ac4e16d4c1739095;
complementary640 9ebdf4611802b9091a1c3dc3194e6529ed867933008c3c3d0851212325673b19;
negative-root259 b697a6c47257c534ff08ca093a94f2a5a8a6c71cd46c2e823b00436a13032689.
Their exact filenames are those in the adopted MC/FH source footers.

Complete comparison texts retained matching are first-column415,
coherent-sector599, collective532, physical-row288, coherent-boundary383,
coefficient218, vacuum449, and meridian-frames506, at the exact pins
listed after (MC23). The root-capped Euler coproduct360 was freshly
read whole at e11f5f827f226ee93505e00aed3885a33abdbfc15ee71e023a67c048c9c17720:
its \(N^{-1/2}\) meridian estimate concerns fixed-denominator Euler
operators on a small activity disk, not this shifted-denominator capped
period. The complete factorial162, filling-Gram240, and quantum-jet241
coverage has pins 17fbb46d17b9678e35b9800e1c67cca24f846e8b5ccbcc540d360ec3189e1b18,
9345e275c4c086b5f18ff2ded0f78e41e700a58b601bebd4b5e953f64e1b0d88,
and aa338e19460ceaaac9aef7c387b5b2fb88ddfc0de706a5a6f6a937342628dde0.
Those texts do not give the scalar-relative limit (PC4).
Only written mathematics and text/hash operations were used.
