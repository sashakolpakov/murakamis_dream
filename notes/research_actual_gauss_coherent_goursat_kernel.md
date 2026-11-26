# An actual Gauss coherent kernel from its finite Goursat problem

Private written proof, 18 November 2026.

The two-head Gauss operator has an actual nonzero local kernel in the
strict upper-half degree chamber. This follows from its exact Jacobi
commutator and its initialized first column. The proof controls the
finite logarithmic recurrence and the entire remaining coefficient cap;
it does not infer an analytic kernel from a formal characteristic equation.
The literal ordinary-binomial input is then composed on its original
coefficient circle. Its selected saddle has coefficient one and a nonzero
mixed derivative.

This is a fixed-root statement for this full operator block. The exterior
factors of the opposite source remain, as do other degree blocks. No
meridian-normal estimate, geometric-point membership, or closed-source
coefficient follows. Complete directs H, G, B and V are pinned below.

## 1. Actual normalization and the exact finite equation

Put
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad x=-q^{-1},
 \quad c_0=2\pi i,\quad f_a=(Q;Q)_a.
 \tag{1}
\]
On the two remaining physical heads restrict to total degree
\(0\le T\le d\), in the original basis \(|a,T-a\rangle\).
Throughout the analytic theorem
\[
 \sigma_N=(T+1)/N\in I\Subset(1/2,1),\qquad
 C=Q^{-T-1}=e^{-c_0\sigma_N},\qquad \tau_N=T/N.
 \tag{2}
\]
The letter \(C\) is an exact \(N\)-dependent parameter. In particular
\(C-1\) and \(C+1\) are uniformly nonzero. The case \(T=d\) is excluded.

G defines the actual operator \(A_N=q_FE_\Sigma^d i_d\), and proves
that it is a polynomial in the commuting actual \(K,\Omega\). At the
root its ordered formula is
\[
 A_N=(-1)^dN\sum_{n=0}^d
       \frac{(-1)^nq^{n^2}}{f_n^2}F^nE^nK^{d-n}.
 \tag{3}
\]
On this degree block \(K=C\). H's matrix \(J_T=\Omega|_T\) is
complex symmetric, so \(A_N|_T\) is symmetric and commutes with \(J_T\).
This is bilinear matrix symmetry, not Hermitian positivity. B proves
the exact nonzero vacuum entry and the complete initialized column:
\[
 a_{00}:=(A_N)_{00}=(-1)^dC^d f_T^2,\qquad
 G_T(\rho)=\sum_{a=0}^T x^{-a}\frac{(A_N)_{a0}}{a_{00}}\rho^a.
 \tag{4}
\]
Define the whole finite, symmetric monomial kernel
\[
 \mathcal K(\rho,\zeta)=
 \sum_{a,b=0}^T x^{-a-b}\frac{(A_N)_{ab}}{a_{00}}
                                      \rho^a\zeta^b.
 \tag{5}
\]
Thus \(\mathcal K(\rho,0)=G_T(\rho)\),
\(\mathcal K(0,\zeta)=G_T(\zeta)\), and \(\mathcal K(0,0)=1\).
No channel sum or inverse spectral measure occurs in (5).

H's literal Jacobi entries, after elementary simplification, are
\[
 A_a^{\rm Jac}=(Q^{a-T}-1)(1-Q^{a+1}),\qquad
 D_a=2(q+q^{-1}Q^{-T})Q^a-(q+q^{-1})Q^{-T}Q^{2a}.
 \tag{6}
\]
Set missing endpoint arrows equal to zero. For a vector \(v\), write
\(\mathcal L_v(t)=\sum_{a=0}^T x^{-a}v_a t^a\), and set
\[
 \begin{split}
 \mathscr D_t^0L={}&C(1-Qt)(1-Q^2t)L(Q^2t)\\
 &-(1+C)(1-Qt)^2L(Qt)+(1+Qt^2)L(t).
 \end{split}\tag{7}
\]
Comparison of the coefficients in (6) gives the exact identity
\(\mathscr D_t^0\mathcal L_v=qt\mathcal L_{J_Tv}\).
The apparent degree-\(T+2\) coefficient is zero because
\(CQ^{T+1}=1\); the degree-\(T+1\) coefficient is precisely the last
Jacobi row. This verifies the identity at both endpoints as well as in
the interior. Consequently the actual commutator gives
\[
 \boxed{\quad
 \zeta\mathscr D_\rho^0\mathcal K
       -\rho\mathscr D_\zeta^0\mathcal K=0.
 \quad}\tag{8}
\]
Equation (8) is an identity of finite polynomials, with all caps intact.

## 2. Initialized phase and amplitude

We use B's entire-disk first-column theorem with the exact \(C\) in
(2). To specify the data, let \(Y_B(0)=1\) be the analytic root
\[
 CY_B^2-(1+C-\rho)Y_B+1-C\rho=0,
 \qquad D=\rho\partial_\rho,
 \tag{9}
\]
and put
\[
 Z_B=-\frac{CY_BDY_B+\rho Y_B-C\rho}
                {2CY_B-(1+C-\rho)}.
\]
On a fixed disk, with logarithms calibrated at zero, B proves
\[
 \begin{split}
 \phi_G(\rho)&=\frac{\operatorname{Li}_2(\rho)}{c_0}
                  +\frac1{c_0}\int_0^\rho\frac{\log Y_B(t)}t\,dt,\\
 \mathcal A_G(\rho)&=(1-\rho)^{-1/2}
       \exp\left(\int_0^\rho\frac{Z_B(t)}{tY_B(t)}\,dt
                          -\tfrac12\log Y_B(\rho)\right),\\
 G_T(\rho)&=e^{N\phi_G(\rho)}\mathcal A_G(\rho)(1+O(N^{-1})).
 \end{split}\tag{10}
\]
The relative error and every fixed holomorphic derivative are uniform
on smaller disks. Both factors equal one at zero except
\(\phi_G(0)=0\). In particular
\[
 \phi_G'(0)=2/c_0,\qquad
 (\log\mathcal A_G)'(0)=1/(1-C).
 \tag{11}
\]
B obtains (10) from the literal column, including its final truncation.

Define the removable analytic function
\[
 \Lambda(t,p)=2+\frac{(1-t)^2
               (1-e^{c_0tp})(1-Ce^{c_0tp})}{t}.
 \tag{12}
\]
It has \(\Lambda(0,p)=2+c_0(C-1)p\). There is a unique local analytic
solution of
\[
 \Lambda(\rho,S_\rho)=\Lambda(\zeta,S_\zeta),\qquad
                         S(\rho,0)=\phi_G(\rho).
 \tag{13}
\]
Here and below the domains and bounds are uniform for (2). An explicit
analytic existence construction, also used for the finite estimates,
is given in the next section; the noncharacteristic coefficient is
\(c_0(C-1)\).

We specify the subprincipal amplitude instead of leaving a free unit.
For either variable \(t\), let \(D_t=t\partial_t\),
\(Y=e^{c_0D_tS}\), and put
\[
 \begin{array}{lll}
 a_0=C(1-t)^2,&b_0=-(1+C)(1-t)^2,&d_0=1+t^2,\\
 a_1=-3Cc_0t(1-t),&b_1=2(1+C)c_0t(1-t),&d_1=c_0t^2.
 \end{array}
\]
Define, with removable value at \(t=0\),
\[
 \mathcal R_t(S)=\frac{a_1Y^2+b_1Y+d_1
       +c_0^2D_t^2S(2a_0Y^2+\tfrac12b_0Y)}{t}.
 \tag{14}
\]
Let \(\alpha\) solve the analytic linear transport equation
\[
 \begin{split}
 \Lambda_p(\rho,S_\rho)\alpha_\rho
 -\Lambda_p(\zeta,S_\zeta)\alpha_\zeta
       &=-\mathcal R_\rho(S)+\mathcal R_\zeta(S),\\
 \alpha(\rho,0)&=\log\mathcal A_G(\rho).
 \end{split}\tag{15}
\]
Its transverse coefficient is nonzero near zero, so the same
characteristic construction applies. Put \(\mathcal A=e^\alpha\);
then \(\mathcal A\) is a specified analytic unit with
\(\mathcal A(0,0)=1\).

The full finite-kernel conclusion is
\[
 \boxed{\quad
 \mathcal K(\rho,\zeta)
   =e^{NS(\rho,\zeta;C)}\mathcal A(\rho,\zeta;C)
                                    (1+O(N^{-1})).
 \quad}\tag{16}
\]
It holds on an actual fixed complex bidisk, including both axes,
uniformly with all fixed derivatives after shrinking that bidisk.
In particular the actual kernel is zero-free there for all large \(N\).

## 3. Finite logarithmic majorants and the whole cap

Here is a proof of (16) from (8). It supplies the finite stability
estimate as well as analytic existence, rather than assuming that the
formal equation (13) describes the polynomial.
Unspecified positive constants in estimates and majorants below are
uniform comparison constants, distinct from the exact clock \(C\).

Write \(\epsilon=N^{-1}\). Initially define
\(V_N=\epsilon\log\mathcal K\) only as a formal series with constant
zero. For \(\Delta_{t,k}V=V(\ldots,Q^kt,\ldots)-V\), division of
(8) by \(\rho\zeta\mathcal K\) gives
\[
 F_{\epsilon,\rho}(V_N)-F_{\epsilon,\zeta}(V_N)=0,
\quad
 F_{\epsilon,t}(V)=
 \frac{a_\epsilon(t)e^{N\Delta_{t,2}V}
       +b_\epsilon(t)e^{N\Delta_{t,1}V}+d_\epsilon(t)}{t},
 \tag{17}
\]
where
\(a_\epsilon=C(1-Qt)(1-Q^2t)\),
\(b_\epsilon=-(1+C)(1-Qt)^2\),
\(d_\epsilon=1+Qt^2\). The numerator is divisible by \(t\) as a
formal series. Choose a sufficiently small fixed \(\delta>0\), and
set \(k_N=\lfloor\delta N\rfloor<T\). Uniformly for
\(1\le n\le k_N\),
\[
 m_n=(Q^n-1)(CQ^n-1),\qquad c n\le|Nm_n|\le C_1n.
 \tag{18}
\]
Indeed the second factor stays away from zero, and the first is
comparable to \(n/N\) on this short arc.

If \(v_{ab}\) are the coefficients of \(V_N\), the only terms of
total logarithmic degree \(i+j+1\) in the coefficient
\(\rho^i\zeta^j\) of (17) are
\[
        Nm_{i+1}v_{i+1,j}-Nm_{j+1}v_{i,j+1}.
 \tag{19}
\]
All other terms involve smaller total logarithmic degree. Thus the
known first axis determines each low-degree diagonal successively.
No division at a resonant high index is used.

We give a uniform convergent majorant for this induction. For low
degrees, \(N|Q^{ka}-1|\le C_k a\). Therefore the increment series
in (17) are coefficientwise dominated by \(CtU_t\), where \(U\)
has nonnegative coefficients. After the exact linear row (19) has
been removed, the constant source in the difference of the two
operators is bounded by \(C(\rho+\zeta)\); its constant term cancels.
The nonconstant linear terms are bounded by \(C(t+t^2)U_t\), and
the nonlinear exponential remainder divided by \(t\) is bounded by
\(C(1+t)^2(e^{CtU_t}-1-CtU_t)/t\). This is analytic at \(t=0\)
and has an explicit factor \(t\).

Consequently, enlarging positive constants if necessary, the following
positive implicit equation dominates every step of (19):
\[
 \begin{split}
 U_\zeta&=C_2U_\rho+C_2(\rho+\zeta)
                +F(\rho,U_\rho)+F(\zeta,U_\zeta),\\
 F(t,p)&=C_3(1+t)^2\frac{e^{C_3tp}-1-C_3tp}{t}
                                      +C_3(t+t^2)p,\\
 U(\rho,0)&=C_4\rho/(R-\rho).
 \end{split}\tag{20}
\]
The initial row dominates the low coefficients of
\(N^{-1}\log G_T\) by (10) on a smaller disk. To verify the comparison,
divide (19) by its lower bound \(c(j+1)\). The other linear term is
at most \(C(i+1)/(j+1)\) times the preceding coefficient on the same
diagonal. These are precisely the derivative coefficients on the two
sides of (20). Every nonlinear term uses lower total degrees, since
its increments have zero constant and its exponential remainder starts
quadratically. Induction on total degree, then on the second index,
therefore proves the asserted domination.

For completeness (20) has a genuine analytic solution on a fixed
bidisk. On bounded \(p\), its rightmost term has \(p\)-derivative
\(O(\zeta)\). Solve for \(U_\zeta=\mathcal H(\rho,\zeta,U_\rho)\)
by uniform contraction in a bounded complex disk. Positive Picard
iteration shows that its formal coefficients are nonnegative. To
solve this explicit first-order equation, start on \(\zeta=0\) and
integrate
\[
 \dot\rho=-\mathcal H_p,\qquad
 \dot p=\mathcal H_\rho,\qquad
 \dot U=\mathcal H-p\mathcal H_p.
 \tag{21}
\]
The analytic vector field and its first derivatives are uniformly
bounded on a fixed slightly larger polydisk. Successive integral
approximations converge geometrically for a fixed short complex time:
the difference of consecutive approximations is bounded by a constant
times \((L|\zeta|)^n/n!\). Their derivatives converge on smaller
polydisks by Cauchy. The initial projection derivative is
\(\partial\rho/\partial\rho_0=1\), hence remains uniformly close to
one; its analytic inverse gives \(U(\rho,\zeta)\). Its coefficient
recursion is positive. This proves convergence of the majorant, and
uniform low-coefficient bounds \(C_5R_1^{-a-b}\).
The same construction proves analytic existence and uniqueness in
(13), by first solving for \(S_\zeta\) using
\(\Lambda_p(0,p)=c_0(C-1)\); it also solves (15).

We next pay the entire finite cap. In the original finite basis the
two-head \(E,F,K^{\pm1}\) at the root have uniformly bounded operator
norms: they are sums of a fixed number of shifts with entries of
modulus at most two and unit-modulus clocks. Uniformly in \(n<N\),
\(e^{-C_6N}\le |f_n|\le e^{C_6N}\). For example the lower bound
follows by applying
\(2\sin(\pi j/N)\ge4\min(j,N-j)/N\) and factorial bounds to
each initial segment; the upper bound follows from \(2\sin\le2\).
Formula (3) and (4) then give
\[
 \left|x^{-a-b}(A_N)_{ab}/a_{00}\right|\le e^{C_7N}
                         \quad(0\le a,b\le T).
 \tag{22}
\]
Polynomial factors in \(N\) have been absorbed into \(C_7\).

Let \(V_N^{[k]}\) be the total-degree-\(k_N\) truncation of the
exact formal logarithm. The functions
\(\mathcal K\) and \(\exp(NV_N^{[k]})\) agree through degree \(k_N\).
On a fixed comparison bidisk both are bounded by \(e^{C_8N}\), using
(22) for the former and the analytic majorant for the latter. On a
smaller bidisk of radius \(r\), Cauchy's coefficient estimate gives
\[
 |\mathcal K-e^{NV_N^{[k]}}|
 \le C_9(k_N+2)e^{C_8N}
       \frac{(r/R_2)^{k_N+1}}{(1-r/R_2)^2}.
 \tag{23}
\]
Also \(|V_N^{[k]}|\le C_{10}r\). Choosing a fixed \(r>0\) sufficiently
small makes (23) exponentially small relative to
\(e^{NV_N^{[k]}}\): the gain
\(\delta\log(R_2/r)\) beats \(C_8+C_{10}r\). This proves actual
zero-freeness and recovery of the entire polynomial from its controlled
low logarithm. It does not delete any finite coefficient.

Finally substitute \(V_{\rm app}=S+\epsilon\alpha\) into (17).
Uniform Taylor expansion on a larger bidisk gives
\[
 F_{\epsilon,t}(S+\epsilon\alpha)
   =\Lambda(t,S_t)+\epsilon
        [\Lambda_p(t,S_t)\alpha_t+\mathcal R_t(S)]
            +O(\epsilon^2).
 \tag{24}
\]
Indeed
\(N\Delta_{t,k}S=kc_0D_tS+\epsilon k^2c_0^2D_t^2S/2
+O(\epsilon^2)\), and the first derivatives of the three explicit
coefficients are exactly those in (14). All remainders after division
by \(t\) are analytic and uniformly bounded, since the corresponding
numerators vanish at \(t=0\). Equations (13) and (15) cancel the
first two orders. By (10) the boundary logarithmic error is
\(O(\epsilon^2)\).

The same finite diagonal induction controls the interior error. Here
are the details of stability. Subtract the two exponential equations
and retain the exact linear coefficients \(Nm_n\). Factoring each
remaining exponential difference by its increment difference expresses
it as a convergent analytic multiplier times that difference. After the
constant linear part is removed, every such multiplier has an explicit
factor \(\rho\) or \(\zeta\); both background logarithms have the
uniform analytic majorants already proved. On smaller polydisks these
multipliers are dominated by fixed nonnegative analytic series.
Thus the low absolute error coefficients are dominated by the solution
of a positive linear equation of the form
\[
 E_\zeta=C_{11}E_\rho+K_1(\rho,\zeta)E_\rho
       +K_2(\rho,\zeta)E_\zeta+\epsilon^2F_0(\rho,\zeta),
 \quad E(\rho,0)=\epsilon^2E_0(\rho),
 \tag{25}
\]
where the displayed series are fixed analytic positive series and
\(K_1(0,0)=K_2(0,0)=0\). The residual's coefficients are bounded by
\(\epsilon^2F_0\) by Cauchy applied to (24). Invert \(1-K_2\) on a
smaller bidisk and use the linear instance of (21). Its solution is
\(\epsilon^2\) times a uniformly bounded analytic function. The
coefficient comparison is exactly the total-degree/second-index
induction following (20), so no high-index inverse is introduced.
We obtain a logarithmic error \(O(N^{-2})\) on the final bidisk;
the tails of the analytic approximate solution past \(k_N\) and (23)
are exponentially smaller there. Exponentiation proves (16).
Cauchy on a slightly larger final bidisk proves every asserted fixed
derivative. This completes the actual finite stability argument.

## 4. The initialized mixed derivative

The boundary in (9) fixes the phase, rather than merely its formal
Hamiltonian. Direct substitution in (12), using
\(e^{c_0\rho\phi_G'}=Y_B/(1-\rho)\), gives
\[
 \lambda_G(\rho):=\Lambda(\rho,\phi_G'(\rho))
                         =C(1+Y_B(\rho))+\rho.
 \tag{26}
\]
In particular \(\lambda_G(0)=2C\), \(\lambda_G'(0)=1+C\).
Evaluating (13) on the second axis therefore yields
\[
 S_\zeta(\rho,0)=\frac{\lambda_G(\rho)-2}{c_0(C-1)},
 \quad S_\rho(0,0)=S_\zeta(0,0)=2/c_0,
 \quad
 \boxed{S_{\rho\zeta}(0,0)=\frac{C+1}{c_0(C-1)}\ne0.}
 \tag{27}
\]
Thus the full actual monomial kernel has a nondegenerate mixed phase
on a fixed smaller bidisk. This fact was not assumed in obtaining (16).

## 5. The literal coherent input and its selected coefficient circle

Retain the actual output polynomial row
\(v(w)|a,T-a\rangle=w_1^aw_2^{T-a}\) and the original compact
ordinary-binomial input coefficients
\(\binom da\binom d{T-a}z_1^az_2^{T-a}\). On a chart where
\(w_2z_2\ne0\), set
\[
 \rho=xw_1/w_2,\qquad \eta=xz_1/z_2,\qquad
 \mathcal B_T(t)=\binom dT^{-1}
          \sum_{b=0}^T\binom db\binom d{T-b}t^b.
\]
The exact original kernel is
\[
 v(w)A_Nc(z)=a_{00}(w_2z_2)^T\binom dT\,
       \operatorname{CT}_{\zeta}
                 \mathcal K(\rho,\zeta)\mathcal B_T(\eta/\zeta).
 \tag{28}
\]
All powers, caps and factorial duals are still present. In particular
the right leg in (28) has not been replaced by the monomial left leg.

V proves a whole-disk unit for this exact binomial polynomial, with
\(d=N-1\) and \(\tau=\tau_N\) retained:
\[
 \mathcal B_T(t)=e^{NS_B(t;\tau)}\mathcal A_B(t;\tau)(1+O(N^{-1})).
 \tag{29}
\]
Explicitly let \(v=v(t)\) be the analytic solution near
\(\tau/(1-\tau)\) of
\(tv/(1+tv)+v/(1+v)=\tau\), and put
\[
 \begin{split}
 S_B&=\log(1+tv)+\log(1+v)-\tau\log v
                         +\tau\log\tau+(1-\tau)\log(1-\tau),\\
 D_B&=tv/(1+tv)^2+v/(1+v)^2,\\
 \mathcal A_B&=\frac{\sqrt{\tau/(1-\tau)}}
                       {(1+tv)(1+v)\sqrt{D_B}}.
 \end{split}\tag{30}
\]
Here \(S_B(0)=0\), \(\mathcal A_B(0)=1\), and
\(b:=S_B'(0)=\tau/(1-\tau)\). The square root is fixed by these
values. The factors in (30), rather than the \(d=N\) approximation,
are needed for the amplitude.

Let \(c(\rho)=S_\zeta(\rho,0)\), \(c_*=2/c_0\), and introduce
the fixed-reference square-root coordinate
\[
                  a^2=bc_*\eta.
 \tag{31}
\]
It is independent of the output variable \(\rho\). For \(\rho\)
sufficiently small and \(a\) in a sufficiently small sector
\(0<|a|<a_0\), \(|\arg a|<\theta_0<\pi/2\), the phase
\(S(\rho,\zeta)+S_B(\eta/\zeta)\) has a unique nearby saddle
\[
 \zeta_*=\frac{a}{\sqrt{c_*c(\rho)}}(1+O(a)),\quad
 \Psi(\rho,a)=S(\rho,\zeta_*)+S_B(\eta/\zeta_*),\quad
 \mathcal H=(\zeta\partial_\zeta)^2
          [S(\rho,\zeta)+S_B(\eta/\zeta)]_{\zeta_*}.
 \tag{32}
\]
All branches are continued from \(c(0)=c_*\). The implicit saddle
equation after scaling \(\zeta=a u\) has a nonzero derivative at
\(u=1/\sqrt{c_*c(\rho)}\). Thus
\[
 \Psi=\phi_G(\rho)+2a\sqrt{c(\rho)/c_*}+O(a^2),\qquad
 \mathcal H=2a\sqrt{c(\rho)/c_*}+O(a^2).
 \tag{33}
\]

The original constant-term circle can be taken to be
\(\zeta=\zeta_*e^{i\theta}\), with its usual positive orientation.
Both arguments then stay in the actual disks of (16) and (29).
The complete-circle estimate of V applies uniformly in \(\rho\):
the leading varying phase is
\(2a\sqrt{c(\rho)/c_*}\cos\theta\). The remaining periodic analytic
term has second derivative \(O(|a|^2)\), and its first derivative
at zero vanishes because \(\zeta_*\) is the exact saddle.
Consequently its real difference from the saddle is bounded above by
\[
 -[2\Re(a\sqrt{c(\rho)/c_*})-C_{12}|a|^2]
                                            (1-\cos\theta).
 \tag{34}
\]
Shrinking the output disk and \(a_0\) makes the bracket positive.
This controls the whole complementary circle, not merely a local
stationary equation. Taylor expansion on its central arc and (34)
give the actual Gaussian coefficient one. Uniformly on compact subsets
of this punctured sector and the smaller output disk, (28) becomes
\[
 \boxed{\begin{split}
 v(w)A_Nc(z)={}&a_{00}(w_2z_2)^T\binom dT
    \frac{e^{N\Psi(\rho,a)}}{\sqrt{2\pi N\mathcal H}}\,
       \mathcal A(\rho,\zeta_*)\mathcal A_B(\eta/\zeta_*)
                  (1+O(N^{-1})).
 \end{split}}\tag{35}
\]
The Gaussian square root is continued from positive real \(a\) at
\(\rho=0\). Fixed derivatives follow on smaller compact sets. In
particular the normalized actual coherent kernel is nonzero there.
No uniform punctured-sector estimate as \(N|a|\to0\), or full
\(\eta\)-disk zero-free assertion, is made.

Since (31) uses \(c_*\) rather than \(c(\rho)\), the mixed derivative
has its actual meaning in independent output and input coordinates.
Equations (27) and (33) give
\[
 \boxed{\quad
 \lim_{a\to0}\Psi_{\rho a}(0,a)
         =\frac{C+1}{2(C-1)}\ne0.
 \quad}\tag{36}
\]
After shrinking the sector this remains nonzero. For \(a\ne0\),
(31) is a locally invertible input chart. Thus (35) is a genuine
local coherent generating kernel with a nonzero amplitude and mixed
phase derivative, obtained after the entire channel contraction.

## 6. Source scope and complete directs

The normalization in (35) includes the exact vacuum scalar, the
homogeneous monomial, the ordinary-binomial coefficient and the
Gaussian \(N^{-1/2}\). Neither “symmetry” nor a choice of source frame
removes any of them. The proof concerns the actual \(A_N\) block,
not scalar evaluation of its Casimir polynomial or a termwise estimate
in an ill-conditioned spectral frame. Its whole finite cap was paid
by (22)--(25), and its whole coefficient circle by (34).

For the opposite kernel, G's exact routing still reads
\(T=\mathcal B_m(W_\tau^{-1})A_ND_{\rm top}\mathscr C_r\), followed
by \(J=D_N(MK)^{-1}T\). This note does not estimate those exterior
contractions, their meridian normals, or their original closed source.
It also does not identify the local chart above with a specified
geometric representation. Those distinctions are essential even though
the actual two-head operator, rather than separate spectral legs, now
has a controlled local kernel. Degrees outside (2), and in particular
the endpoint \(T=d\), require separate analysis.

Complete proof directs:

* H: notes/actual_complete_casimir_hermite_packet.md,
  SHA256 a4e96738a3a093d963fe13cc03585085951fa8699a506ade4e2e7a47c17b3f4c.
* G: notes/research_opposite_kernel_forced_cyclic_normalization.md,
  SHA256 42e6d6c3a5039859c241a2832de56301eff49d749db86d67868f3534c89aaaaa.
* B: notes/research_actual_gauss_first_column_unit.md,
  SHA256 ebe3b496a739d1734738e4b663c7a7fd6713e44549b72ee2e93ae90314a15047.
* V: notes/research_actual_clebsch_magnetic_generating_kernel.md,
  SHA256 9601b29b73caab6c4705efb36abcc5539f6b22ada43961cdbcc2da848aa1b1c6.

All arguments are written mathematics. No numerical experiment or
program supplies an implication. Frozen and public files are unchanged.
The complete H and G were freshly read nontruncated in this author
sequence. The complete matching B and V whole reads were retained
fresh and unchanged from the immediately preceding active author and
review sequence. Every used implication was checked and all four
source pins renewed.
