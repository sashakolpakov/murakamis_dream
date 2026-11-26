# An actual Gauss normal Green current and its uniform boundary family

Private written proof, 18 November 2026.

The first-column normal in N has an extra forced sector. This note
does not propagate it as a homogeneous copy of the root phase.
It constructs an exact finite Green formula for the whole matrix
normal, and proves a uniform phase/amplitude estimate for the
boundary-ratio family that occurs in its harmonic current. The
family includes both the actual Gauss matrix and the identity.
All finite endpoints and the reflected integral are retained.

The complete directs are K, N, and G, pinned below.

## 1. Finite commutant extension without a spectral frame

Put \(c_0=2\pi i,\ Q=e^{c_0/N},\ q=e^{c_0/(2N)},\
d=N-1,\ \mathsf x=-q^{-1}\), and \(f_j=(Q;Q)_j\).
Fix an actual degree \(T\) with
\[
 (T+1)/N\in I\Subset(1/2,1),\qquad C=Q^{-T-1},\qquad b=d-T.
 \tag{1}
\]
Use the original basis \(e_a=|a,T-a\rangle,\ 0\le a\le T\).
K's symmetric Jacobi matrix \(J\) has diagonal and arrows
\[
 \beta_a=2q(1+C)Q^a-qC(1+Q)Q^{2a},\qquad
 \alpha_a=(CQ^{a+1}-1)(1-Q^{a+1}),\quad 0\le a<T.
 \tag{2}
\]
Both missing endpoint arrows are zero. Every displayed interior
arrow is nonzero. Define normalized continuants by
\[
 f^{J}_0(\lambda)=1,\quad f^{J}_{-1}=0,\qquad
 \alpha_n f^{J}_{n+1}
 =(\lambda-\beta_n)f^{J}_n-\alpha_{n-1}f^{J}_{n-1}.
 \tag{3}
\]
The recurrence is used through \(n=T-1\). Direct induction gives
\(f^{J}_n(J)e_0=e_n\). Thus \(e_0\) is cyclic.

For a polynomial \(p(\rho)=\sum_{a=0}^T p_a\rho^a\), write
\(v[p]=\sum_a\mathsf x^a p_ae_a\). Define the matrix and its kernel
\[
 \mathscr E_N[p]e_n=f^{J}_n(J)v[p],\qquad
 \mathcal E_N[p](\rho,\zeta)
 =\sum_{a,n=0}^T\mathsf x^{-a-n}
       (\mathscr E_N[p])_{an}\rho^a\zeta^n.
 \tag{4}
\]
For analytic \(p\), (4) means its degree-\(T\) Taylor truncation.
There is a unique polynomial \(r\) of degree at most \(T\) with
\(r(J)e_0=v[p]\), by cyclicity. Consequently
\(\mathscr E_N[p]=r(J)\). In particular it is symmetric, commutes
with \(J\), and has precisely the boundary \(p\).
This proves the last-row equation as well as the interior rows.

Here are two useful quantitative facts. First,
\[
 \prod_{a=0}^{n-1}\alpha_a
   =Q^{-n(2T-n+1)/2}\frac{f_Tf_n}{f_{T-n}}.
 \tag{5}
\]
The all-index sine bounds in K give upper and lower bounds
\(e^{\pm cN}\) for each factorial in (5). Monic continuants
have coefficients bounded by \(c^n\): expand their tridiagonal
determinants, or apply their recurrence with bounded entries.
Since \(J\) has bounded norm, (3)--(5) show that boundary
coefficients bounded by \(e^{cN}\) give every matrix coefficient
in (4) a bound \(e^{c'N}\), uniformly in (1).
No eigenvector or Hermite condition number occurs.

Second, if \(p_a=0\) for \(a\le k\), then
\[
             (\mathscr E_N[p])_{an}=0\quad\hbox{when }a+n\le k.
 \tag{6}
\]
Indeed a degree-\(n\) polynomial in a tridiagonal matrix moves an
index by at most \(n\). This exact triangular matching, rather
than a norm estimate at a shrinking radius, will recover the cap.

## 2. A uniform actual family from the Gauss matrix to the identity

Let \(A_0=A_N(1)|_T\), and retain the exact vacuum
\[
 a_{00}=(-1)^dC^df_T^2,\qquad \bar A=A_0/a_{00}.
 \]
K and N supply the actual polynomial
\[
 G_N(\rho)=\sum_a\mathsf x^{-a}\bar A_{a0}\rho^a
     =e^{N\phi(\rho;C)}A_N^{\rm bd}(\rho;C),\qquad
 A_N^{\rm bd}=\mathcal A_G(1+O(N^{-1})).
 \tag{7}
\]
The amplitudes and their inverses are uniformly analytic on a
fixed disk. Choose a bounded complex neighborhood \(\mathcal X\)
of \([0,1]\), and shrink that disk so that \(t\rho\) stays in
the common zero-free seed disk for all \(t\in\mathcal X\).
Define the actual family
\[
 \mathcal P_{N,t}
       =\mathcal E_N\!\left[\frac{G_N(\rho)}{G_N(t\rho)}\right],
 \quad
 \psi_t(\rho)=\phi(\rho)-\phi(t\rho),\quad
 a_t(\rho)=\frac{\mathcal A_G(\rho)}{\mathcal A_G(t\rho)}.
 \tag{8}
\]
There is a fixed bidisk, independent of \(N,t\), on which
\[
 \boxed{\quad
 \mathcal P_{N,t}(\rho,\zeta)
   =e^{NS_t(\rho,\zeta;C)}
       \mathcal A_t(\rho,\zeta;C)(1+O(N^{-1})),
       \qquad \mathcal A_t\ne0.
 \quad}                                                     \tag{9}
\]
The estimate and all fixed derivatives are uniform for \(t\)
on smaller neighborhoods of \([0,1]\) and for (1).

Here the phase and amplitude are fixed, not free choices.
With K's removable function
\[
 \Lambda(z,p)=2+
       \frac{(1-z)^2(1-e^{c_0zp})(1-Ce^{c_0zp})}{z},
 \tag{10}
\]
\(S_t\) is the unique small analytic solution of
\[
 \Lambda(\rho,\partial_\rho S_t)
       =\Lambda(\zeta,\partial_\zeta S_t),\qquad
 S_t(\rho,0)=\psi_t(\rho).
 \tag{11}
\]
Its transport is K's exact first transport row, initialized by
\(\log a_t\). In particular all \(Q,q,d=N-1\) corrections in
that row remain. The coefficient
\(\Lambda_p(0,p)=c_0(C-1)\) is independent of \(p\), and is
uniformly nonzero. The compact family of initial derivatives
therefore has one common analytic characteristic neighborhood.

We give the finite estimate behind (9). The boundary in (8),
before truncation, is a uniform unit with phase \(\psi_t\) and
amplitude \(a_t(1+O(N^{-1}))\). Its coefficients have \(e^{cN}\)
bounds on a fixed comparison circle. Truncation through \(T\)
has an exponentially small relative error on a smaller disk.
Formula (5) then bounds the entire matrix cap by \(e^{c'N}\).

The exact kernels (4) obey K's finite equation
\[
 \zeta\mathscr D_\rho^0\mathcal P
       -\rho\mathscr D_\zeta^0\mathcal P=0,
 \]
\[
 \mathscr D_z^0=
 C(1-Qz)(1-Q^2z)\mathsf T_z^2
 -(1+C)(1-Qz)^2\mathsf T_z+1+Qz^2,\quad
 \mathsf T_z f(z)=f(Qz).
 \tag{12}
\]
For its logarithm divided by \(N\), the degree-\((i+j+1)\)
diagonal row is exactly
\[
 N m_{i+1}v_{i+1,j}-Nm_{j+1}v_{i,j+1},\qquad
 m_n=(Q^n-1)(CQ^n-1),\quad |Nm_n|\asymp n
 \tag{13}
\]
for \(n\le\delta N\). The boundary logarithms in (8) have common
analytic coefficient bounds on \(\mathcal X\).
The positive majorant in K therefore applies with constants
independent of \(t\): the nonlinear exponential remainders
have a factor \(\rho\) or \(\zeta\), and division by the new
coefficient in (13) gives the derivative factors
\((i+1)/(j+1)\). Solving the positive implicit first-order
equation by its characteristic ODE gives one fixed radius.

For clarity, the stability step is also uniform. After substituting
\(S_t+N^{-1}\log\mathcal A_t\), the conjugated residual and
boundary error are \(O(N^{-2})\). Differences of exponentials
factor by their increment difference. Their remaining analytic
multipliers have a factor \(\rho\) or \(\zeta\), so the error is
dominated by
\[
 E_\zeta=cE_\rho+K_1E_\rho+K_2E_\zeta+N^{-2}F,\qquad
 E(\rho,0)=N^{-2}E_0,\quad K_1(0,0)=K_2(0,0)=0.
 \tag{14}
\]
The linear characteristic solution is uniformly \(O(N^{-2})\).
All parameter derivatives follow by Cauchy on a larger
\(\mathcal X\); no derivative of a merely pointwise estimate is used.

The low logarithm and the actual finite kernel agree through
degree \(\lfloor\delta N\rfloor\). Their coefficients on a
comparison bidisk have \(e^{cN}\) bounds. Cauchy's tail bound,
with a smaller fixed bidisk chosen after \(\delta\), makes the
remaining cap exponentially smaller than the bounded low-log
exponential. This proves (9) for the whole actual matrix.
It also proves stability under boundary replacements matching
through that low degree, by (6) and the same cap bound.
Thus no exponentially conditioned global norm is applied to
an error known only on a shrinking disk.

The endpoints are exact:
\[
 \mathcal P_{N,0}=\mathcal K_0,\qquad
 \mathcal P_{N,1}
      =\sum_{a=0}^T Q^a(\rho\zeta)^a,\qquad
 S_1=0,\quad \mathcal A_1=(1-\rho\zeta)^{-1},
 \tag{15}
\]
where \(\mathcal K_0\) is K's normalized Gauss kernel.
The second identity is (4) applied to the boundary \(1\),
whose matrix is \(I\). No mixed-rank assertion is made at
\(t=1\), and no identification with an abelian holonomy follows.

We will also use a linear version of (9). If \(w_N(\rho,t)\)
is uniformly analytic and bounded, with
\(w_N=w+O(N^{-1})\), then
\[
 \mathcal E_N\!\left[w_N(\rho,t)
                 \frac{G_N(\rho)}{G_N(t\rho)}\right]
   =e^{NS_t}\{\mathcal A_{t,w}+O(N^{-1})\}.                    \tag{16}
\]
The error is absolute after removing \(e^{NS_t}\);
\(\mathcal A_{t,w}\) can vanish. To prove this without dividing
by \(w\), add a constant larger than its uniform bound, apply
the unit proof to \(w_N+c\) and \(c\), and subtract. The
transport amplitude is linear in its initial amplitude.
The same argument gives uniform analytic bounds when only
boundedness, rather than an expansion, is supplied.

## 3. The actual symmetric normal and its finite Green forcing

Write \(M=e^\mu\), keeping \(q\) fixed, and
\(g_j(M)=(M^{-2}Q;Q)_j\).
The literal one-head arrows are
\(Ew_a=(MQ^{-a}-M^{-1})w_{a-1}\) for \(a>0\), \(Ew_0=0\),
\(Fw_a=(1-Q^{a+1})w_{a+1}\) below the top, and
\(Kw_a=(-M/q)Q^{-a}w_a\).
Multiplying the ordered two-head coproduct gives, for \(v=T-a\),
\[
 J(M)_{a+1,a}=MQ^{-v}(1-M^{-2}Q^v)(1-Q^{a+1}),
 \]
\[
 J(M)_{a,a+1}=MQ^{-v}(1-M^{-2}Q^{a+1})(1-Q^v),
 \]
\[
 J(M)_{aa}
 =q\{(M^2+1)C+1+M^{-2}\}Q^a-qC(1+Q)Q^{2a}.
 \tag{17}
\]
Both finite endpoints are still absent. The analytic diagonal
gauge, with its square root fixed to one at \(M=1\), is
\[
 S_a(M)^2=
 \frac{g_T(M)f_{T-a}}{g_{T-a}(M)f_T}
                  \frac{f_a}{g_a(M)},\qquad S_0=1.
 \tag{18}
\]
It makes \(\widetilde J=S^{-1}J(M)S\) symmetric.
If \(\Sigma_a=\sum_{j=1}^aQ^j/(1-Q^j)\), then
\[
 s_a:=S_a'(1)=\Sigma_T-\Sigma_{T-a}-\Sigma_a.
 \]
The average of the two logarithmic arrow derivatives in
(17), and its displayed diagonal derivative, give
\[
 (J_1)_{a+1,a}=(J_1)_{a,a+1}=(C-1)Q^{a+1},\qquad
 (J_1)_{aa}=2q(C-1)Q^a,\quad J_1=\widetilde J'(1).
 \tag{19}
\]
Primes here and below mean \(\partial_\mu|_0\).

G's whole-meridian polynomial \(A_N(M;K,\Omega)\) commutes
with \(J(M)\). Set
\[
 B=a_{00}^{-1}(S^{-1}A_N(M)S)'|_0.
 \]
It is symmetric, and
\[
 [J,B]=[\bar A,J_1],\qquad
 B e_0=v[b_N],\qquad
 b_N=\mathcal H_N+(2d+D-s(D))G_N,\quad D=\rho\partial_\rho.
 \tag{20}
\]
Here \(\mathcal H_N\) is N's true normal with its fixed vacuum
normalization. The \(2d\) term is the derivative of \(K_T(M)^d\),
and \(DG_N\) is the derivative of the actual \(x(M)^a\).
Thus (20) is not obtained by differentiating a root-only identity.

For \(n>j\), define the finite Green polynomials
\[
 \Gamma_{n,j}(\lambda)=
 \frac{\det(\lambda-J[j+1:n-1])}
                       {\alpha_j\alpha_{j+1}\cdots\alpha_{n-1}},
 \tag{21}
\]
with empty determinant one. Let
\[
 \mathscr Q_Ne_0=0,\qquad
 \mathscr Q_Ne_n=\sum_{j=0}^{n-1}
       \Gamma_{n,j}(J)(J_1\bar A-\bar A J_1)e_j .
 \tag{22}
\]
Then the exact whole-matrix answer is
\[
 \boxed{\qquad B=\mathscr E_N[b_N]+\mathscr Q_N.\qquad}       \tag{23}
\]
Indeed its \(n\)-th column recurrence is
\[
 \alpha_n B_{n+1}
 =(J-\beta_n)B_n-\alpha_{n-1}B_{n-1}
                     +(J_1\bar A-\bar A J_1)e_n,
 \tag{24}
\]
and (21) is its elementary finite variation-of-constants solution.
In particular the sign of the forcing and its order are fixed.

The last row in (24) is also paid, not imposed as a new hypothesis.
Write \(\bar A=p_N(J)\), using G's finite polynomial and reducing
its degree if necessary. The finite insertion derivative
\[
 Dp_N(J)[J_1]=\sum_{\ell\ge1}p_{N,\ell}
                   \sum_{i=0}^{\ell-1}J^iJ_1J^{\ell-1-i}
 \tag{25}
\]
satisfies \([J,Dp_N(J)[J_1]]=[\bar A,J_1]\).
Subtract its first-column extension (4). The result has zero
first column, satisfies every commutator row, and hence equals
(22) by (24). This proves the terminal identity, symmetry,
and absence of an unrecorded outward state.
Both (22) and (25) are finite physical formulas, including all
Jordan effects; neither uses scalar Casimir interpolation.

## 4. An exact combined boundary current, including reflection

We spell out how (23) uses only the paid root column and explicit
normal forcing. This keeps the microscopic axis layers.
Use N's exact scalar operator \(L_1=a\mathsf T^2+\beta\mathsf T+\delta\),
\[
 a=C(1-Q\rho)(1-Q^2\rho),\quad
 \beta=-C-1+Q(C+2)\rho-Q^2\rho^2,\quad
 \delta=1-QC\rho,
 \]
and its true coefficient derivatives
\[
 \dot a=-4a,\quad
 \dot\beta=2C+4-Q(2C+10)\rho+6Q^2\rho^2,\quad
 \dot\delta=-2.
 \tag{26}
\]
It obeys \(L_1G_N=0\) and
\[
 L_1\mathcal H_N=-\dot L\,G_N+\mathcal S_N,\qquad
 \mathcal S_N=-QC\{2Q^{-1}(1-C^{-1})
 +\rho[2/v_N-(C^{-1}-1)v_{-1,N}]
 -2Q^{T+1-b}\rho^{T+2}V_T(1)/v_N\}.                           \tag{27}
\]
Every datum is finite: \(v_N=f_T^2/N\),
\(V_T(1)=Q^{T(T+1)}\), and N's auxiliary normal is
\[
 v_{-1,N}=Q^{-b-1}(1-Q^b)
       [2\mathcal S_N^{\,q}(P)+(4/N)\mathcal S_N^{\,q}(DP)],
 \quad
 P(t)=\frac{t\prod_{j=1}^b(1-Q^{-j}t)^2}{1-Q^{-1}t},
 \]
\[
 \mathcal S_N^{\,q}(P)=
           \sum_{k\ge1}[t^k]P/(1-Q^{-k}).
 \tag{28}
\]
The quotient in (28) is a polynomial. In particular neither
\(v_{-1,N}\) nor \(1/v_N\) is replaced by its limiting value.
The last monomial in (27) is the actual top current.

Let \(r_N=G_N(Q\rho)/G_N(\rho)\). Define a polynomial \(F_N\)
through degree \(T\) by the triangular equation
\[
 a r_Nr_N(Q\rho)F_N(Q\rho)-\delta F_N
      =-\dot L\,G_N/G_N+\mathcal S_N/G_N
                    \pmod{\rho^{T+1}}.
 \tag{29}
\]
Its diagonal at degree \(n\) is \(CQ^n-1\), nonzero for
\(0\le n\le T\). Its constant is zero. The exact factorization
of \(L_1(G_NU)\) in N proves
\[
 F_N=[\,U(Q\rho)-U(\rho)\,]_{\le T},
               \qquad U=\mathcal H_N/G_N.
 \tag{30}
\]
Thus (29), with (27),(28), determines \(F_N\) without assuming
the unknown full normal. If \(u_0=\mathcal H_N(0)\), then
\[
 \mathcal H_N=
 \left[G_N\left(u_0+
       \sum_{n=1}^T\frac{[\rho^n]F_N}{Q^n-1}\rho^n\right)\right]_{\le T}.
 \tag{31}
\]
The constant \(u_0\) is the exact finite vacuum derivative in N.

For any polynomial \(F\) of degree below \(N\), with \(F(0)=0\),
its finite inverse difference has the exact integral
\[
 \sum_{n\ge1}\frac{[\rho^n]F}{Q^n-1}\rho^n
 =-\frac12F(\rho)+\frac N{c_0}\int_0^1F(x\rho)\frac{dx}{x}
 +\frac N{c_0}\int_0^1
       \frac{x^{N-1}[F(x\rho)-F(\rho/x)]}{1-x^N}\,dx.
 \tag{32}
\]
This is N's finite cotangent identity, using
\((Q^n-1)^{-1}=(1-Q^{-n})^{-1}-1\).
At \(x=0\) the reflected polynomial has net exponent at least
\(N-1-T=b\ge1\). At \(x=1\) the displayed difference is kept
as one divided difference. Both integrals therefore converge
as actual finite polynomial currents.

Applying the linear finite extension (4) to (20),(31),(32)
now gives the requested exact Green current:
\[
 \boxed{\begin{split}
 \mathcal K_B={}&\mathcal K_{\mathscr Q_N}
 +\mathcal E_N[(u_0+2d+D-s(D))G_N-\tfrac12G_NF_N]\\
 &+\frac N{c_0}\int_0^1
                 \mathcal E_N[G_N(\rho)F_N(x\rho)]\,\frac{dx}{x}\\
 &+\frac N{c_0}\int_0^1
   \frac{x^{N-1}}{1-x^N}
     \mathcal E_N[G_N(\rho)\{F_N(x\rho)-F_N(\rho/x)\}]\,dx .
 \end{split}}                                                \tag{33}
\]
The extension in each term includes the physical Taylor truncation.
It commutes with these integrals because it is finite dimensional.
No logarithm is inserted on an axis, no cap is removed, and no
reflected large argument is assigned a small-activity asymptotic.

## 5. What the uniform family pays, and the remaining integral

N's low-band factorization gives, through \(k_N=\lfloor\delta N\rfloor\),
\[
 F_N=P_N+W_N/G_N,\qquad P_N(0)=2,\quad W_N(0)=-2,
 \tag{34}
\]
where \(P_N,W_N\) are uniformly analytic on a fixed disk and
converge there to the explicit analytic functions in N.
Consequently the main harmonic integrand in (33), in that low band,
is the sum of
\[
 G_N(\rho)P_N(x\rho),\qquad
     \frac{G_N(\rho)}{G_N(x\rho)}\,W_N(x\rho).
 \tag{35}
\]
The first is a weighted \(t=0\) family; the second is exactly
the weighted \(t=x\) family of (16). Both have uniform analytic
propagation, including \(x=0,1\). Their values at \(x=0\)
are \(2\mathcal K_0\) and \(-2\mathcal K_0\), so their sum
must be kept before division by \(x\). The equality through
degree \(k_N\) propagates through total degree \(k_N\) by (6).
All larger physical coefficients retain the \(e^{cN}\) bound;
the same fixed-bidisk tail argument pays them. This is the
precise sense in which the uniform family controls the main
current without a conditioned error amplification.
For this comparison under the main integral, keep the pair in
(35) together: its \(x\)-constant is exactly zero. Integrating
each finite Taylor coefficient then only divides by a positive
integer. Equivalently use its analytic divided difference at
\(x=0\). This preserves both the matching low triangle and the
exponential coefficient bound for the complementary cap.

The estimate (9) is not an estimate of the integral of its
individual endpoint limits. In particular \(x\asymp N^{-1}\)
can carry the cancellation at the first endpoint, while
\(1-x\asymp N^{-1}\) can carry the identity endpoint in (15).
The reflected current and the inhomogeneous Green term in
(33) remain in the answer. A full normal asymptotic now asks
for the asymptotic of this specified combined current,
including its cancellation with \(\mathcal K_{\mathscr Q_N}\);
it is not a problem of choosing a homogeneous normal phase.
No such cancellation or lower bound is asserted here.

Finally the actual physical normal, before symmetrizing, is
\[
 \mathcal K_{A'}=
          \mathcal K_B+[s(D_\rho)-s(D_\zeta)]\mathcal K_0 .
 \tag{36}
\]
For the optional diagonal \(D_a(M)=(f_a/g_a(M))^{1/2}\), define
the congruenced matrix explicitly as
\(a_{00}^{-1}D(M)^{-1}S(M)^{-1}A_N(M)S(M)D(M)^{-1}\).
Since \(D_a'(1)=-\Sigma_a\), its normal kernel is
\(\mathcal K_B+[\Sigma(D_\rho)+\Sigma(D_\zeta)]\mathcal K_0\).
This identity records its moving gauge; cancellation of leading
axis terms alone does not prove a bounded relative family.

For the original binomial input, K's exact conversion still reads
\[
 v(w)A_N'(1)c(z)=a_{00}(w_2z_2)^T\binom dT
     \operatorname{CT}_{\zeta}
          \mathcal K_{A'}(\rho,\zeta)\mathcal B_T(\eta/\zeta),
 \tag{37}
\]
with \(\rho=\mathsf xw_1/w_2,\ \eta=\mathsf xz_1/z_2\) and the
literal finite binomial polynomial \(\mathcal B_T\) of K.
Equation (37) is exact, not a new estimate of its whole circle.
The exterior braid, turnover, inverse Cartan coupon, cut and
closing finite-part normals in G's routing are unchanged.
There is no quantum-parameter normal, geometric incidence,
closed-source noncancellation, or filling conclusion.

## Complete proof directs

* K: notes/research_actual_gauss_coherent_goursat_kernel.md,
  552 lines, SHA256
  37ade960cb7938372b7854b00aebc1df82e648144f850fcd4a356f68a00159e1.
* N: notes/research_actual_gauss_first_column_meridian_normal.md,
  695 lines, SHA256
  6315ba61735d2f37363f59037fa4c0cb59f1cb729a20c6159a9e1b54d40f46d4.
* G: notes/research_opposite_kernel_forced_cyclic_normalization.md,
  489 lines, SHA256
  42e6d6c3a5039859c241a2832de56301eff49d749db86d67868f3534c89aaaaa.

Only written mathematics and text operations are used.
All three complete directs were freshly read nontruncated in this
author sequence. The entire matching final was then reread
nontruncated, every used implication checked, and all four pins
renewed. Independent matching review and adoption remain separate.
