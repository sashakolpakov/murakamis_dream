# Calibrated transport and the actual q-Hahn normal amplitude

Written proof, 24 November 2026.

The actual paired q-Hahn normal has a nonzero leading amplitude on
each fixed strict physical compact when its scaled channel separation
is sufficiently small. The allowed separation is a fixed positive
number depending on that compact. This improves the shrinking-window
upper bound to an amplitude theorem for the original generic derivative.

The proof uses its two exact source equations, an analytic inverse
with a controlled remainder, and one small original physical prefix.
A convergent closed-walk expansion computes the prefix trace and fixes
the normalization constant. No boundary uniformity is inferred from
an interior compact estimate. The conclusion is a local packet theorem,
not a lower bound for the original closed knot source.

## 1. The source and the leading coefficient

Let \(N\ge3\), \(h=N^{-1}\), \(d=N-1\), \(q_0=e^{\pi i/N}\).
Take actual integers
\[
 0\le j<l,\qquad j+l=d,\qquad s=l-j,\qquad \xi=j/N.
 \tag{1}
\]
For \(q=q_0e^\epsilon\) set
\[
 Q=q^2,\quad B=Q^{-N},\quad x=q^d,\quad
 t=N\tau,\quad u=N\nu,\quad T=Q^t,\quad U=Q^u.
 \tag{2}
\]
All powers use \(\log q=\pi i/N+\epsilon\). The actual generic source is
\[
 C_m(q;t,u)=x^u\sum_{k=0}^m
 \frac{(Q^{-m};Q)_k(B^2Q^{m+1};Q)_k(U^{-1};Q)_kQ^k}
 {(BQ;Q)_k(T^{-1};Q)_k(Q;Q)_k},
 \quad (a;Q)_k=\prod_{r=0}^{k-1}(1-aQ^r).
 \tag{3}
\]
Retain its original divided derivative
\[
 w_{j,l}=\frac{D C_j(q_0;t,u)-D C_l(q_0;t,u)}
 {-2N\Delta_j},\qquad
 D=q\partial_q,\quad
 \Delta_j=q_0^{2j+1}-q_0^{-2j-1},\quad
 R_{N,j}(\tau,\nu)=\frac{w_{j,l}}{C_j(q_0;t,u)}.
 \tag{4}
\]
The derivative fixes \(N,t,u\). Both generic highest-weight-\(d\)
columns, including the large partner, remain in this definition.

Write
\[
 {\cal P}=\{(\tau,\nu)\in\mathbb C^2:
        \tfrac12<\Re\tau<1,\quad 0<\Re\nu<\Re\tau\}.
 \tag{5}
\]
The following quantities are limiting coefficient functions, not a
complex interpolation of the finite integer channel:
\[
 \begin{gathered}
 \sigma=e^{\pi i\tau},\quad c=\cos(\pi\tau),\quad
 z=e^{\pi i(\tau-2\nu)},\quad
 b_\xi=\sin(\pi\xi),\quad d_\xi=\cos(\pi\xi),\\
 W_\xi=1-2cz+d_\xi^2z^2,\quad V=1-2cz+z^2,\\
 Y_\xi=\frac{(b_\xi z+i\sqrt{W_\xi})^2}{V},\qquad
 H_\xi=-4ib_\xi\sqrt{W_\xi}/z .
 \end{gathered}
 \tag{6}
\]
For real \(0<\xi\le1/2\), [J,P] prove that \(W_\xi,V\) do not
vanish on \({\cal P}\). The square root is their source branch,
positive at real centers \(\nu=\tau/2\).
Define the normalized primitive
\[
 {\cal F}_\xi(\tau,\nu)
       =\int_0^1\frac{\nu}{H_\xi(\tau,\theta\nu)}\,d\theta .
 \tag{7}
\]
The integrand has a regular limit at \(\theta=0\).
Section 5 proves its holomorphy and both transport derivatives.
At the folded endpoint it simplifies to the explicit unit
\[
 {\cal F}_{1/2}={\cal F}_0
       =\frac{\sqrt{1-2cz}+i\sigma}{8\pi c}.
 \tag{8}
\]
The subscript \(0\) in \({\cal F}_0\) denotes the folded formula.

**Theorem.** For every compact \(K\Subset{\cal P}\), there is a
fixed \(\delta_K>0\) such that, uniformly over the actual pairs (1)
with \(1\le s\le\delta_KN\), as \(N\to\infty\),
\[
 \boxed{\quad
 w_{j,l}(N\tau,N\nu)
    =N{\cal F}_{\xi}(\tau,\nu)\,
       C_j(q_0;N\tau,N\nu)(1+o_K(1)).
 \quad}
 \tag{9}
\]
The relative error tends to zero with every fixed holomorphic
derivative on smaller compacts. After decreasing \(\delta_K\),
\({\cal F}_\xi\) is uniformly separated from zero on \(K\).
In particular, for large \(N\), the actual normal is nonzero there and
\[
 c_KN\le |R_{N,j}|\le C_KN,\qquad
 \frac1N\bigl(\log|w_{j,l}|-\log|C_j(q_0)|\bigr)
                         =O_K(\log N/N).
 \tag{10}
\]
The constants and the allowed positive scaled window depend on \(K\).

For every prescribed \(S_N=o(N)\), (9) consequently gives, uniformly
for all actual \(s\le S_N\) on each fixed physical compact,
\[
             w_{j,l}=N{\cal F}_0 C_j(q_0)(1+o(1)).
 \tag{11}
\]
This includes Gaussian and logarithmically enlarged Gaussian windows.
No rate for the \(o(1)\) is asserted.

## 2. A common generic magnetic operator and actual confluence

For \(X=U^{-1}\), let \(\mathscr T f(X)=f(QX)\), and put
\[
 \begin{split}
 a(X)&=(1-X^{-1})(BQ-(TX)^{-1}),\\
 b(X)&=(B^{-1}-Q/X)(1-(TX)^{-1}),\\
 {\cal L}&=a(X)(\mathscr T-I)+b(X)(\mathscr T^{-1}-I)
                                      +(B^{-1}+BQ)I .
 \end{split}
 \tag{12}
\]
This operator preserves polynomials. Its apparent negative powers
cancel on constants and linear polynomials; higher monomials have
no negative powers. On \(P_k(X)=(X;Q)_k\) it has the exact action
\[
 {\cal L}P_k=\Lambda_kP_k+\eta_kP_{k-1},\quad
 \Lambda_k=B^{-1}Q^{-k}+BQ^{k+1},\quad
 \eta_k=(B^{-1}-Q^k)(1-Q^{k-1}/T)(1-Q^{-k}).
 \tag{13}
\]
For \(k\ge1\), subtract the leading term. The remainder has degree
at most \(k-1\) and vanishes at \(1,Q^{-1},\ldots,Q^{2-k}\).
At \(X=Q^{1-k}\), only the \(\mathscr T^{-1}\) term remains, with
\(P_k(X/Q)/P_{k-1}(X)=1-Q^{-k}\). This proves the lower coefficient;
constants are immediate. Comparing consecutive coefficients in (3)
now gives \({\cal L}(x^{-u}C_m)=\Lambda_m(x^{-u}C_m)\), with the
same finite coefficient ratio as [C].

The physical common operator and its eigenvalue are
\[
 \Omega_q=q^{-1}x^u{\cal L}x^{-u},\qquad
 \lambda_m(q)=q^{-1}\Lambda_m
       =q^{2N-1-2m}+q^{-2N+1+2m}.
 \tag{14}
\]
At the root, \(\lambda_j=\lambda_l\) and \(C_j=C_l\) by [C].
Also \(D(\lambda_j-\lambda_l)(q_0)=-2N\Delta_j\).
Differentiate their two common operator equations and subtract.
The operator derivative cancels against their vanishing root
difference. The actual divisor in (4) therefore gives
\[
                    (\Omega_{q_0}-\lambda_j)w_{j,l}=C_j .
 \tag{15}
\]
There is no additional scalar in this forcing.

At the root the magnetic equation for the original ordinary column is
\[
 A_+C(\tau,\nu+h)+A_-C(\tau,\nu-h)+(D_h-\lambda_j)C=0,
 \tag{16}
\]
\[
 A_+=(U-T)(1-QU)/T,\quad A_-=(U-QT)(1-U)/(QT),\quad
 D_h=(U/T)[2(q_0^{-1}+q_0T)-(q_0+q_0^{-1})U].
\]
Here \(Q=Q_0\). The shift \(X\mapsto QX\) is \(u\mapsto u-1\);
conjugating (12) by \(x^u\), with \(x=-q_0^{-1}\), gives precisely
these coefficients and checks the physical \(q^{-1}\) in (14).

## 3. The second generic shift and the normalized equations

The coproduct shift is also generic and common to both partners.
The equivalent finite Newton form in [C] is
\(C_m=x^uH_m(U,V)/D_m(UV)\), \(V=Q^{t-u}\),
\(D_m(T)=\prod_{r<m}(T-Q^r)\).
Its numerator is a linear combination, with coefficients depending
only on \(Q,B\), of
\[
 B_a(U,V)=V^a\prod_{r<a}(U-Q^r)\prod_{r<m-a}(V-Q^r).
 \tag{17}
\]
Each basis term satisfies the polynomial identity
\[
 (1-Q^{-m}UV)B_a
    =(1-U)B_a(U/Q,V)+U(1-V)B_a(U,V/Q).
 \tag{18}
\]
Its two shifted ratios are \(Q^{-a}(U-Q^a)/(U-1)\) and
\(Q^{-m}(V-Q^{m-a})/(V-1)\); the weighted sum is
\(1-Q^{-m}UV\). Replace \(V\) by \(QV\), and use
\(D_m(QT)/D_m(T)=(1-QT)/(1-Q^{1-m}T)\). This proves exactly
\[
 (1-QT)C_m(t+1,u)
       =x(1-U)C_m(t,u-1)+(U-QT)C_m(t,u).
 \tag{19}
\]
No restriction to the small channel or to the root entered the
argument. Subtract the partners, differentiate their root collision,
and divide by the actual gap. The derivatives of the common
coefficients again cancel. Thus \(w\) satisfies the homogeneous
version of (19), with its root coefficients.

For \(C=C_j(q_0;N\tau,N\nu)\), define
\[
 p_\pm=A_\pm C(\tau,\nu\pm h)/C,\quad
 p_\tau=(1-QT)C(\tau+h,\nu)/C,\quad
 p_b=x(1-U)C(\tau,\nu-h)/C .
 \tag{20}
\]
The full physical theorem makes these holomorphic on fixed compacts
for large \(N\). Dividing (15),(19) by the ordinary column gives
the source-exact normalized equations
\[
 \begin{split}
 p_+[R(\nu+h)-R]+p_-[R(\nu-h)-R]&=1,\\
 p_\tau[R(\tau+h,\nu)-R]&=p_b[R(\tau,\nu-h)-R].
 \end{split}
 \tag{21}
\]
The suppressed first coordinate in the first line is \(\tau\).

## 4. An exponentially effective analytic inverse

Fix a real channel interval \(\Xi=[3/8,1/2]\).
The ordinary amplitude [J,P] gives, uniformly for \(\xi\in\Xi\)
and with all fixed derivatives on physical compacts,
\[
 p_+-p_-=H_\xi+O(h),\qquad
 p_b/p_\tau=r_\xi+O(h),\qquad
 r_\xi=\frac{(U-1)Y_\xi^{-1}}
                  {(U-1)Y_\xi^{-1}+U-T}.
 \tag{22}
\]
Indeed \(A=(U-T)(1-U)/T=-V/z^2\), so
\(A(Y_\xi-Y_\xi^{-1})=-4ib_\xi\sqrt{W_\xi}/z=H_\xi\).
The limiting coproduct coefficient is nonzero by the simple second
characteristic in [J,P]. Thus \(p_\tau\), \(p_+-p_-\), and the
triangular multiplication matrix below have bounded inverses,
uniformly on fixed compacts and \(\xi\in\Xi\).

Put \(Z_\nu=h\partial_\nu R\), \(Z_\tau=h\partial_\tau R\).
For analytic functions let
\[
 {\cal A}_\pm f=\int_0^1 f(\tau,\nu\pm th)\,dt,\qquad
 {\cal A}_\tau f=\int_0^1 f(\tau+th,\nu)\,dt .
 \tag{23}
\]
The fundamental theorem of calculus converts (21) exactly into
\[
 (p_+{\cal A}_+-p_-{\cal A}_-)Z_\nu=1,\qquad
 p_b{\cal A}_-Z_\nu+p_\tau{\cal A}_\tau Z_\tau=0.
 \tag{24}
\]
Write this as \((M_N+E_N)Z=(1,0)^T\), where
\[
 M_N=\begin{pmatrix}p_+-p_-&0\\p_b&p_\tau\end{pmatrix}.
 \tag{25}
\]
Every entry of \(E_N\) is a bounded multiplier times an averaging
operator minus the identity. All its coefficient bounds are uniform
on the fixed buffered compacts just specified.

Here the analytic inverse must suppress an exponentially growing
initial bound, not merely a polynomial one. Fix an inner compact
and an outer neighborhood at distance \(\rho>0\) in the maximum
coordinate norm, both inside \({\cal P}\).
Use \(m=\lfloor aN\rfloor\) nested neighborhoods with successive
distances \(\rho/m\). Cauchy's estimate and shifts of length at most
\(h\) give
\[
 \|({\cal A}-I)f\|_{\rm inner}
        \le\frac{Ch}{\rho/m-h}\|f\|_{\rm next}.
 \tag{26}
\]
For \({\cal B}_N=M_N^{-1}E_N\), choose a fixed \(a>0\) sufficiently
small. Its norm at each such step is then at most a fixed
\(q_*<1/2\), since \(m h\le a<\rho\).
Products of these estimates apply also to variable coefficients:
\[
 \|{\cal B}_N^r f\|_{K_0}\le q_*^r\|f\|_{K_r},
                       \qquad 0\le r\le m.
 \tag{27}
\]
The neighborhoods and the outer coefficient bounds are fixed before
the subdivision; no derivative constant growing with \(m\) is omitted.

On a further fixed outer compact, [U] gives
\[
 \|R\|\le C N^A\exp(C s^2/N),\qquad s\le\eta N.
 \tag{28}
\]
Cauchy's estimate gives the same exponential bound, times a
polynomial, for \(Z\) on the outer neighborhood in (26).
For \(s\le\delta N\), choose \(\delta>0\) small enough that
\(C\delta^2\) is less than half the exponential decay rate of
\(q_*^m\). Also take \(\delta<\eta\) and small enough that the
actual \(\xi\) lies in \(\Xi\).
The exact finite Neumann identity, with
\(v_N=M_N^{-1}(1,0)^T\), is
\[
 Z=\sum_{r=0}^{m-1}(-{\cal B}_N)^r v_N
                         +(-{\cal B}_N)^m Z .
 \tag{29}
\]
The geometric sum is bounded. By (27),(28), the remainder tends
to zero exponentially, uniformly in the allowed channels.
Therefore \(Z=O(1)\) on the inner compact.

Run this bound on a slightly larger inner neighborhood.
In the exact identity \(Z=v_N-{\cal B}_NZ\), a single ordinary
fixed-distance Cauchy estimate now makes the second term \(O(h)\).
Consequently
\[
 h\partial_\nu R=H_\xi^{-1}+O(h),\qquad
 h\partial_\tau R=-r_\xi/H_\xi+O(h).
 \tag{30}
\]
All fixed derivatives follow by buffering and Cauchy's formula.
For any prescribed finite collection of connecting paths and
compacts, one positive \(\delta\) can be chosen for their union.

## 5. The closed primitive and its folded normalization

The one-form
\[
             \omega_\xi=H_\xi^{-1}\,d\nu
                          -r_\xi H_\xi^{-1}\,d\tau
 \tag{31}
\]
is closed. One source-based verification uses the ordinary action
\(\Phi_\xi\) in [J,P]. Its two characteristic equations are
\[
 A(e^{\Phi_\nu}+e^{-\Phi_\nu})+D-\mu_\xi=0,\quad
 (1-T)e^{\Phi_\tau}=(U-1)e^{-\Phi_\nu}+U-T,\quad
 \mu_\xi=2\cos(2\pi\xi),
 \tag{32}
\]
where \(D=2U(1+T-U)/T\).
For \(\xi<1/2\), differentiating their analytic coefficient
functions with respect to \(\mu_\xi\) gives precisely the two
coefficients of (31). Hence
\(\omega_\xi=\partial_{\mu_\xi}(d\Phi_\xi)\) is closed.
The formulas in (6),(22) extend regularly to \(\xi=1/2\),
so closedness holds there by continuity as well.
This differentiates the limiting action, not a finite complex channel.

The normalization in (7) is justified at the boundary explicitly.
At \(\nu=0\), \(z=\sigma\), \(W_\xi=-b_\xi^2\sigma^2\), and the
source branch is \(\sqrt{W_\xi}=-ib_\xi\sigma\).
This follows first along real physical \(\tau,\nu\), where the
square root has positive real part, and then by continuation in
the strip \(1/2<\Re\tau<1\).
Thus
\[
 H_\xi(\tau,0)=-4b_\xi^2=\mu_\xi-2,\qquad
 r_\xi(\tau,\nu)\longrightarrow0\quad(\nu\longrightarrow0).
 \tag{33}
\]
For the second limit, \(Y_\xi^{-1}
=V/(b_\xi z+i\sqrt{W_\xi})^2\) vanishes at \(\nu=0\);
its denominator is nonzero, while \(U-T\to1-T\ne0\).
The coefficients extend holomorphically across this boundary
locally, and the \(\tau\) coefficient of (31) is zero there.
Closedness therefore gives
\[
 {\cal F}_{\xi,\nu}=H_\xi^{-1},\qquad
 {\cal F}_{\xi,\tau}=-r_\xi/H_\xi,\qquad
 {\cal F}_\xi(\tau,0)=0 .
 \tag{34}
\]
The integral (7) is along a segment inside \({\cal P}\) except
its regular endpoint; it proves holomorphy and continuous analytic
dependence on the real parameter \(\xi\), up to the fold.

At \(\xi=1/2\), direct differentiation shows that (8) has
these two derivatives and its boundary value is zero.
For the \(\tau\) derivative one may check
\[
 {\cal F}_{0,\nu}=\frac{i z}{4\sqrt W},\qquad
 {\cal F}_{0,\tau}=
       \frac{i(\sqrt W+i\sigma)^2}{16c^2\sigma\sqrt W},
 \quad W=1-2cz.
 \tag{35}
\]
The identities
\(2c(z-\sigma)=-(\sqrt W-i\sigma)(\sqrt W+i\sigma)\) and
\(2c(z-i\sqrt W)=-(\sqrt W+i\sigma)(\sqrt W+i\sigma^{-1})\)
give \(r_{1/2}=-(\sqrt W+i\sigma)^2/(4c^2\sigma z)\),
which verifies the second transport derivative.

## 6. One original physical prefix calibrates the constant

Fix \(\tau_*=3/4\), a sufficiently small fixed
\(\varepsilon_0>0\), and the interior anchor
\(p_0=(\tau_*,\varepsilon_0)\).
Let \(t_N\) be the nearest integer to \(3N/4\), and
\(u_N=\lfloor\varepsilon_0N\rfloor\).
For \(s\le\delta N\) and a small fixed \(\delta\),
\(l\le t_N\le d\) for large \(N\).
These are complete original physical slices.

The root Casimir matrix on degree \(t_N\) is symmetric tridiagonal
with entries from (16):
\[
 D_{N,r}=\frac{U_r}{T_N}
 [2(q_0^{-1}+q_0T_N)-(q_0+q_0^{-1})U_r],\quad
 A_{N,r}=(U_r-T_N)(1-Q_0U_r)/T_N,
 \tag{36}
\]
\(U_r=Q_0^r\), \(T_N=Q_0^{t_N}\).
Let \(J_{[u]}\) be its leading \(u\)-by-\(u\) prefix.
For \(f_0(z)=1\),
\(f_u(z)=\det(zI-J_{[u]})/(A_{N,0}\cdots A_{N,u-1})\),
the actual source identity in [G] is
\[
 C_{j,u}=f_u(c_j),\qquad w_{j,u}=f_u'(c_j),\qquad
 R_{N,j}(t_N/N,u/N)=
                 \operatorname{Tr}(c_jI-J_{[u]})^{-1},
 \quad c_j=2\cos((2j+1)\pi/N).
 \tag{37}
\]
Indeed the two generic columns are the same normalized forward
solution at \(\lambda_j(q),\lambda_l(q)\).
Their common matrix derivative cancels at confluence, with exactly
the eigenvalue-gap derivative in (4). The ordinary scalar
normalization \(C_m(q;t,0)=1\) is unchanged.

For \(r\le u_N\), (36) gives
\[
 D_{N,r}=2+O(\varepsilon_0+h),\quad
 A_{N,r}=O(\varepsilon_0+h),\quad
 \|E_N\|\le C(\varepsilon_0+h),\qquad
 E_N=J_{[u_N]}-2I.
 \tag{38}
\]
The norm follows from tridiagonal row and column sums, without a
dimension factor. Choose \(\varepsilon_0\) so this norm is less
than one for large \(N\). Uniformly for \(\xi\in\Xi\),
\(c_j=\mu_\xi+O(h)\) and \(|c_j-2|\ge3\).
Thus the resolvent in (37) has the uniformly convergent expansion
\[
 \frac1N\operatorname{Tr}(c_jI-J_{[u_N]})^{-1}
    =\sum_{k=0}^{\infty}
       \frac{N^{-1}\operatorname{Tr}E_N^k}{(c_j-2)^{k+1}} .
 \tag{39}
\]
Its tails are bounded by a fixed geometric series, since
\(u_N/N\le\varepsilon_0\).

We compute its limit directly. At \(v=r/N\) the limiting coefficients are
\[
 A(v)=\frac{(e^{2\pi iv}-T_*)(1-e^{2\pi iv})}{T_*},\quad
 D(v)=\frac{2e^{2\pi iv}(1+T_*-e^{2\pi iv})}{T_*},\quad
 T_*=e^{2\pi i\tau_*}.
 \tag{40}
\]
For every fixed \(k\), the diagonal of \(E_N^k\) is a finite sum
over closed length-\(k\) walks with steps \(-1,0,1\).
Away from the at most \(2k\) boundary rows, coefficients in each
walk differ from their value frozen at \(r/N\) by \(O_k(h)\).
The boundary rows contribute \(O_k(h)\) after division by \(N\).
Consequently the Riemann sums give
\[
 \frac1N\operatorname{Tr}E_N^k\ \longrightarrow\
 \int_0^{\varepsilon_0}
   \operatorname{CT}_\zeta
       [D(v)-2+A(v)(\zeta+\zeta^{-1})]^k\,dv .
 \tag{41}
\]
Here \(\operatorname{CT}\) denotes the Laurent constant coefficient.
The convergence is uniform in \(\xi\in\Xi\); the matrix coefficients
do not depend on \(\xi\), and \(c_j-\mu_\xi=O(h)\) uniformly.
Choose \(\varepsilon_0\) still smaller if needed so the absolute
sum of the three limiting coefficients is also less than one.
The same geometric domination then applies to the limiting series.
This justifies first taking the limit for finitely many \(k\)
and then letting the geometric tail decrease.

The sum of (41), with the denominators in (39), is
\[
 \int_0^{\varepsilon_0}
 \operatorname{CT}_\zeta
 \frac{dv}{\mu_\xi-D(v)-A(v)(\zeta+\zeta^{-1})}
       =\int_0^{\varepsilon_0}\frac{dv}{H_\xi(\tau_*,v)}
       ={\cal F}_\xi(p_0).
 \tag{42}
\]
For the first equality, expand the denominator geometrically.
Only even powers of \(\zeta+\zeta^{-1}\) contribute, with constant
coefficient \(\binom{2k}{k}\). The resulting expression is
\[
 \frac1{\mu_\xi-D}
       \left(1-\frac{4A^2}{(\mu_\xi-D)^2}\right)^{-1/2}.
 \tag{43}
\]
Its branch at \(v=0\) is \(1/(\mu_\xi-2)\), negative real.
The characteristic (32) gives
\(H_\xi^2=(\mu_\xi-D)^2-4A^2\), with the same value
\(H_\xi(\tau_*,0)=\mu_\xi-2\).
The uniformly gapped small prefix keeps both branches regular,
so (43) is exactly \(1/H_\xi\), with the original selected sign.
Equations (39)--(43) prove the actual anchor limit
\[
 R_{N,j}(t_N/N,u_N/N)/N
                         ={\cal F}_\xi(p_0)+o(1),
 \tag{44}
\]
uniformly for the channel family, at one fixed positive
\(\varepsilon_0\). No limit of interior estimates toward \(\nu=0\)
is used to calibrate the finite source.

## 7. Closing the local amplitude and its precise scope

Given the target compact \(K\), choose a buffered compact containing
its paths to \(p_0\). Apply section 4 there and choose the resulting
positive \(\delta_K\) once. Integrating (30),(34) gives
\[
 R_{N,j}/N={\cal F}_\xi+a_{N,j}+O_K(h)
 \tag{45}
\]
on that compact, where \(a_{N,j}\) is constant in \(\tau,\nu\).
The moving physical anchor in (44) is \(O(h)\) from \(p_0\);
(30) bounds the corresponding change in \(R/N\) by \(O(h)\).
Thus (44) fixes \(a_{N,j}=o(1)\), uniformly.

The folded coefficient (8) is nowhere zero on \({\cal P}\).
If \(\sqrt{1-2cz}+i\sigma=0\), squaring gives \(z=\sigma\),
because \(2c\sigma=1+\sigma^2\) and \(c\ne0\).
Then \(e^{-2\pi i\nu}=1\), contrary to
\(0<\Re\nu<\Re\tau<1\).
Continuous dependence in (7) therefore makes
\({\cal F}_\xi\) uniformly nonzero on \(K\) when \(\xi\) is
sufficiently close to \(1/2\). Decrease \(\delta_K\) accordingly.
Equation (45) now proves (9),(10); buffered Cauchy estimates
give every fixed derivative of their relative errors.

Using the ordinary amplitude from [J,P] yields the explicit form
\[
 w_{j,l}=N^{1/2}{\cal F}_{\xi}
          B_{\xi}e^{N\Phi_{\xi}}(1+o_K(1)).
 \tag{46}
\]
The actual discrete \(\xi=j/N\) remains in the action and amplitude.
For \(s=o(N)\), \({\cal F}_\xi\to{\cal F}_0\), giving (11).
Replacing the ordinary action by its folded value is not asserted
in this relative formula.

The allowed fixed scaled window depends on the chosen complex
compact. This is not an amplitude theorem for arbitrary
macroscopic separations on the entire tube with one uniform window.
It does not continue the finite channel to a complex parameter,
place every short-filled geometric boundary packet in this domain,
estimate the complete contracted coupon, or identify a contributing
geometric coefficient under the original closing.
No additional knot-volume case or finite-exception theorem follows
without those remaining source estimates.

The complete selected proof and closest-coverage texts are:

| Label | Complete text | SHA256 |
| --- | --- | --- |
| J | [Joint ordinary complex amplitude](actual_q_hahn_joint_complex_amplitude.md), 339 lines | a3b4ca41f0e9ecdee3f701c4d4adf9a1db48a8d5d2ca0f3f223e40ef95235cc6 |
| P | [Full strict physical packet](actual_q_hahn_full_physical_complex_packet.md), 338 lines | 28b7088c4cc947f05d2e395759b77c1232e150dba734d6dca3610548f15b1e0c |
| C | [Generic partner collision](actual_q_hahn_partner_normal_collision.md), 223 lines | afa5f4035f8cc4540da49ff0a4c9a279c67aba4fdaf3e3fc8d481798b2f1c268 |
| U | [Unipotent normal transport](research_q_hahn_unipotent_fold_transport.md), 359 lines | 96d2370f587e786f0cd69c5ce1277e658182ae43004d42c16db1d82925d946d7 |
| G | [Physical-grid partner normal](actual_q_hahn_physical_partner_normal_bound.md), 232 lines | 0725b210bd16899260533cf7a1a7aa9602a7ed0b0e18baf4831efb7a968e07d3 |

Only written mathematics, complete text reads, and metadata hashes
were used. No mathematical program, numerical experiment, test,
build, earlier-final edit, or manuscript change was made.
