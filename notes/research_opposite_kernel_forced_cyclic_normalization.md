# The opposite kernel's finite Gauss row and forced cyclic normalization

Private written proof, 18 November 2026.

The actual opposite-polarization operator contains a finite balanced
hypergeometric polynomial. Its clock contiguity has an explicit
extreme-tail source. Going once around the finite clock solves the
resulting forced recurrence. On the actual tensor module its assembled
denominator is a uniformly bounded analytic unit on a scaled meridian
collar. No individual clock denominator or endpoint source is removed.

This identifies the literal normalization, including its meridian
normals. The scalar polynomial away from the finite spectrum has an
additional norm row, displayed below. Substituting a geometric scalar
argument into the finite central relation would lose that row. No
coherent phase, amplitude estimate, geometric occurrence, or vanishing
relative-window defect is inferred.

The two complete directs are J and R, pinned at the end. All finite
summations, contiguities, and cyclic estimates used here are proved
below.

## 1. An actual top-head factor of the opposite kernel

Use J's conventions
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 m\ge2,\quad r=m-1,\quad x=-M/q,\quad f_n=(Q;Q)_n.
 \tag{1}
\]
The quantum root is fixed and the common meridian \(M\) varies near
one. Thus \(f_d=N\). On the \(r\) remaining heads write
\[
 K=K_{\rm r},\quad E=E_{\rm r},\quad F=F_{\rm r},\qquad
 \Omega=FE+qK+q^{-1}K^{-1}.
\]
These are the actual ordered totals; \(E^N=F^N=0\). In particular
\(K^{2N}=M^{2rN}I\). Put
\[
 H_n(M)=\prod_{j=1}^n(MQ^{-j}-M^{-1}),\qquad H_0=1.
 \tag{2}
\]
This \(H_n\) is a finite lowering product, not J's source
normalization \(D_N(MK)\).

Retain the actual maps
\[
 q_F=p_0S_m^{-1},\qquad
 S_m=\sum_{n=0}^d\frac{(x^{-1}L_1F)^n}{f_n},\qquad
 T=q_FE_\Sigma^d\mathscr C_m i_0,\qquad
 J=D_N(MK)^{-1}T.
 \tag{3}
\]
All scalar factors, the original cut, and the full balanced turnover
\(\mathscr C_m\) have their meanings in J. Introduce the finite
tail operator
\[
                         A_N(M)=q_FE_\Sigma^d i_d,
 \qquad i_dv=w_d\otimes v.
 \tag{4}
\]
It is a literal factor of \(T\), not an independently chosen scalar
interpolant.

Here is the exact routing. Let
\(\tau=R_1R_2\cdots R_r\), with the rightmost crossing acting first,
and let \(\mathsf n\) be total remaining occupation. R's positive
crossing is \(\kappa\mathsf P D\Theta\). When its second input is
\(w_d\), every positive transfer vanishes because the recipient
raising arrow is zero. Its remaining scalar is
\(\kappa x^{-a-d}Q^{ad}\). Hence, with \(i_{{\rm last},d}\) inserting
the last top head,
\[
 W_\tau i_{{\rm last},d}=i_dD_{\rm top},\qquad
 D_{\rm top}=\kappa^r x^{-rd}(x^{-1}Q^{-1})^{\mathsf n}.
 \tag{5}
\]
Also \(\mathscr C_m i_0=i_{{\rm last},d}\mathscr C_r\).
The actual braid intertwines \(E_\Sigma\), and the quotient row
\(q_FW=\mathcal B_m(W)q_F\) is R's exact row. Therefore
\[
 \boxed{\quad
 T=\mathcal B_m(W_\tau^{-1})\,A_N(M)\,D_{\rm top}\,
                                  \mathscr C_r(M).
 \quad}\tag{6}
\]
The order and every factor in (6) are retained.

There is a useful direct normalization check. J's identity
\(\mathscr C_m F_\Sigma(M^{-1})=E_\Sigma(M)\mathscr C_m\)
and \(F_1^di_0=Ni_d\) give
\[
                  T=Nq_F\mathscr C_m S_m(M^{-1})i_d.
 \tag{7}
\]
On the all-top remaining vector, \(S_m(M^{-1})\) fixes the full
all-top vector. Turnover sends it to
\(\gamma_N(M)^m\) times the all-bottom vector, where
\(\gamma_N=(-1)^dD_N(M)/N\). The quotient fixes the latter.
Thus the actual extreme entry is
\[
 T_{\boldsymbol0,\boldsymbol d}=N\gamma_N(M)^m,\qquad
 J_{\boldsymbol0,\boldsymbol d}
       =\frac{N\gamma_N(M)^m}{D_N(M^m\chi)},\quad
 \chi=(-q^{-1})^r.
 \tag{8}
\]
This is a fixed finite kernel datum. It does not assert a nonzero
contraction with an exterior or a geometric cycle.

## 2. The finite polynomial and its transfer forcing

The two terms in \(E_\Sigma=E_1K+E\) \(Q\)-commute. Order the
degree-\(d\) binomial term as
\(E^nE_1^{d-n}K^{d-n}\). At the root
\[
 {d\brack n}_Q=(-1)^nQ^{-n(n+1)/2}.
\]
The degree-\(n\) term of \(p_0S_m^{-1}\), on first occupation \(n\),
has coefficient
\((-1)^nQ^{n(n-1)/2}x^{-n}F^n/f_n\).
The first lowering product from \(d\) to \(n\) is \(H_d/H_n\).
Multiplication, in that order, proves
\[
 \boxed{\quad
 A_N(M;K,\Omega)=
 \sum_{n=0}^d
 \frac{Q^{-n}x^{-n}}{f_n}\frac{H_d}{H_n}
                         F^nE^nK^{d-n}.
 \quad}\tag{9}
\]
The quotient \(H_d/H_n\) in this formula is its finite product
from \(n+1\) to \(d\), so (9) is analytic near \(M=1\).
The commutation relations give
\[
 F^nE^n=\prod_{j=0}^{n-1}
           (\Omega-qQ^jK-q^{-1}Q^{-j}K^{-1}).
 \tag{10}
\]
Thus \(A_N\) is a Laurent polynomial in \(K,M\) and a polynomial
of degree \(d\) in the full commuting Casimir \(\Omega\). Its
leading \(\Omega\)-coefficient is
\[
                            \frac{Qx^{-d}}{N}.
 \tag{11}
\]
No scalar specialization of the tail Casimir was made.

For scalar algebra only, put \(\Omega=z+z^{-1}\), and define
\[
 a=qKz,\quad b=qK/z,\quad c=M^{-2}Q,\quad
 t=M^{-2}K^{-2}=\frac{c}{ab}.
 \tag{12}
\]
Indeed
\[
 \Omega-qQ^jK-q^{-1}Q^{-j}K^{-1}
 =-q^{-1}Q^{-j}K^{-1}(1-aQ^j)(1-bQ^j),
\]
and \(H_n=M^nQ^{-n(n+1)/2}(c;Q)_n\). Substitution in (9) yields
\[
 A_N=H_dK^d\mathcal F_N(a,b;c;t),\qquad
 \mathcal F_N(a,b;c;s)=
 \sum_{n=0}^d\frac{(a;Q)_n(b;Q)_n}{f_n(c;Q)_n}s^n.
 \tag{13}
\]
The right side is a finite polynomial. The variable \(s\) in the
second formula is independent; it is set equal to \(t\) only in
the first formula.

Let \(\mathcal Q_s f(s)=f(Qs)\). Comparison of consecutive
coefficients, including the last coefficient, proves the exact row
\[
 \boxed{\begin{split}
 &\big[(1-\mathcal Q_s)(1-cQ^{-1}\mathcal Q_s)
        -s(1-a\mathcal Q_s)(1-b\mathcal Q_s)\big]\mathcal F_N\\
 &\hspace{20mm}
       =-\frac{s^N(1-a^N)(1-b^N)}{N(c;Q)_d},
 \qquad \mathcal F_N(0)=1.
 \end{split}}\tag{14}
\]
For degrees \(1,\ldots,d\), this is precisely the coefficient
ratio in (13). At degree \(N\), the first bracket contributes
zero because \(Q^N=1\); the last summand supplies the displayed
forcing, using \(f_d=N\). Nothing beyond degree \(N\) occurs.
This proves (14) without an infinite-series identity.

Let \(C_N\) be the monic polynomial specified by
\(C_N(z+z^{-1})=z^N+z^{-N}\), and set
\[
 \begin{split}
 \mathcal W_N(K,\Omega)
   &=\prod_{\ell=0}^d
          (\Omega-qQ^\ell K-q^{-1}Q^{-\ell}K^{-1})\\
   &=C_N(\Omega)+K^N+K^{-N},\\
 \mathcal V_N(K,\Omega)
   &=\prod_{\ell=1}^d
          (\Omega-qQ^\ell K-q^{-1}Q^{-\ell}K^{-1}).
 \end{split}\tag{15}
\]
The second equality follows by the roots and leading coefficient,
first for generic \(K\) and then identically. The elementary
recursion \(C_{j+1}(v)=vC_j(v)-C_{j-1}(v)\), \(C_0=2,C_1=v\),
also defines these polynomials. Equations (10) and its reversed
version give, on the actual tail,
\[
 \mathcal W_N=F^NE^N=0,\qquad
 \mathcal V_N=E^dF^d,\qquad
 (\Omega-qK-q^{-1}K^{-1})\mathcal V_N=0.
 \tag{16}
\]
Before that module specialization,
\((1-a^N)(1-b^N)=K^N\mathcal W_N\). Thus (14) retains exactly
the same off-spectrum norm row as (15).

## 3. Balanced contiguity, with its complete polynomial defect

Write
\[
 \begin{split}
 D(K)&=(1-t/Q)(1-t/Q^2),\\
 P(K,\Omega)&=1-M^{-2}q^{-1}K^{-1}\Omega
                         +M^{-4}Q^{-1}K^{-2},\\
 \alpha_N(M)&=\frac{(-1)^NqM^{-N-1}}{N}.
 \end{split}\tag{17}
\]
In \(A_N(M;QK,\Omega)\), only the Laurent variable \(K\) is
replaced. This notation does not change the tail module or its
meridian. The full polynomial identity is
\[
 \boxed{\begin{split}
 QD(K)A_N(QK,\Omega)-P(K,\Omega)A_N(K,\Omega)
 ={}&\frac{\alpha_N}{qK}\mathcal W_N(K,\Omega)\\
 &+\alpha_N(1-t/Q)(1-K^{-2}/Q)\mathcal V_N(K,\Omega).
 \end{split}}\tag{18}
\]
All quantities in this identity include their \(M\) dependence.

Here is a finite proof. For \(0\le l<N\), the elementary identity
\[
 \sum_{n=0}^l
 \frac{(Q^{-l};Q)_n(b;Q)_n}{f_n(c;Q)_n}
                (cQ^l/b)^n
                  =\frac{(c/b;Q)_l}{(c;Q)_l}
 \tag{19}
\]
can be proved without importing a summation theorem. Multiply
by \((c;Q)_l\), put \(y=c/b\), and rewrite the left side as
\[
 L_l(b,y)=\sum_{n=0}^l {l\brack n}_Q
       (-y)^nQ^{n(n-1)/2}(b;Q)_n(byQ^n;Q)_{l-n}.
\]
The Gaussian Pascal identity gives
\[
 L_{l+1}(b,y)=(1-byQ^l)L_l(b,y)
                  -yQ^l(1-b)L_l(bQ,y).
\]
Starting with \(L_0=1\), induction gives
\(L_l=(y;Q)_l\), proving (19). Only products of length less
than \(N\) have been divided.

For generic \(K,M\), evaluate at
\(\Omega_l=qKQ^l+q^{-1}K^{-1}Q^{-l}\), \(0\le l<N\).
Then \(a=Q^{-l}\), and (19) gives
\[
 \frac{A_N(K,\Omega_l)}{H_dK^d}
              =\frac{(tQ^{-l};Q)_l}{(c;Q)_l}.
 \tag{20}
\]
For \(l\ge1\), shifting \(K\) to \(QK\) replaces \(l\) by
\(l-1\). The ratio in (20) is exactly
\[
 \frac{(1-cQ^{l-1})(1-tQ^{-l-1})}
                   {(1-t/Q)(1-t/Q^2)}
              =\frac{P(K,\Omega_l)}{D(K)}.
 \tag{21}
\]
The prefactor \(K^d\) changes by \(Q^{-1}\). Consequently the
left side of (18) vanishes at the \(d\) nodes \(l=1,\ldots,d\).

At \(l=0\), the unshifted finite sum is one and the shifted
terminating length is \(d\). The two root products give
\[
 \mathcal F_N(Q,Q^2K^2;c;t/Q^2)
 =\frac{(1-t^N)(1-c/Q)}
        {(1-t/Q^2)(1-c^N)}.
 \tag{22}
\]
Hence the left side of (18), at \(\Omega_0\), equals
\[
 H_dK^d P(K,\Omega_0)\frac{c^N-t^N}{1-c^N}.
 \tag{23}
\]
Here
\[
 \begin{split}
 H_d&=(-1)^dM^d\frac{1-M^{-2N}}{1-M^{-2}},\\
 P(K,\Omega_0)&=(1-M^{-2})(1-t/Q),\\
 \mathcal V_N(K,\Omega_0)
       &=Nq^dK^d\frac{1-K^{-2N}}{1-Q^{-1}K^{-2}}.
 \end{split}
 \tag{24}
\]
Equations (23)--(24) show that its quotient by \(\mathcal V_N\)
at this node is
\(\alpha_N(1-t/Q)(1-K^{-2}/Q)\).

Finally (11) shows that the degree-\(N\) coefficient of the
left side of (18) is \(\alpha_N/(qK)\). Subtract that multiple
of the monic \(\mathcal W_N\); the remainder has degree at most
\(d\), vanishes at the \(d\) nodes \(l=1,\ldots,d\), and has
the value just computed at \(l=0\). This proves (18).
The argument was on a generic set only to divide displayed
factors and separate nodes. Polynomial/Laurent continuation
proves the full identity, including all coincident nodes.

On the actual tail module, (16) reduces (18) to
\[
 \boxed{\quad
 QD(K)A_N(QK)-P(K,\Omega)A_N(K)
       =\alpha_N(1-t/Q)(1-K^{-2}/Q)E^dF^d.
 \quad}\tag{25}
\]
The endpoint on the right is a specified finite operator.
It has not been discarded as a homogeneous normalization.

## 4. The forced cyclic Green row on the full tail module

For \(j=0,\ldots,N-1\), put
\[
 K_j=Q^jK,\quad t_j=M^{-2}K_j^{-2},\quad
 \mathscr A_j=A_N(M;K_j,\Omega),\quad
 \mathcal V_j=\mathcal V_N(K_j,\Omega),
\]
and, where the displayed denominators are invertible, define
\[
 \rho_j=\frac{P(K_j,\Omega)}{QD(K_j)},\qquad
 \eta_j=\frac{\alpha_N(1-t_j/Q)(1-K_j^{-2}/Q)}
                            {QD(K_j)}\mathcal V_j.
 \tag{26}
\]
All these are commuting functions of the actual \(K,\Omega\).
Since \(K_N=K\) and \(\mathcal W_N(K_j,\Omega)=0\), (25) is
\[
 \mathscr A_{j+1}=\rho_j\mathscr A_j+\eta_j,\qquad
                          \mathscr A_N=\mathscr A_0.
 \tag{27}
\]
There is no assumption of diagonalizability of \(\Omega\).

The full orbit can be multiplied exactly. With
\(b_0=M^{-2N}\) and \(k=K^N\), one has
\[
 \begin{split}
 \prod_jD(K_j)&=(1-b_0k^{-2})^2,\\
 \prod_jP(K_j,\Omega)
     &=(1+b_0k^{-1}z^N)(1+b_0k^{-1}z^{-N})
                \quad(\Omega=z+z^{-1}).
 \end{split}\tag{28}
\]
The first formula is valid also for even \(N\). In that case the
two half-orbit products are
\((1+t^{N/2})^2\) and \((1-t^{N/2})^2\), whose product is
\((1-t^N)^2\). The second formula follows by factoring \(P\)
as
\((1-M^{-2}q^{-1}K^{-1}z)
 (1-M^{-2}q^{-1}K^{-1}z^{-1})\)
and using \(q^N=-1\).

Before module specialization their difference is
\[
 \prod_jD(K_j)-\prod_jP(K_j,\Omega)
 =b_0(1-k^{-2})(1-b_0k^{-2})
                       -b_0k^{-1}\mathcal W_N(K,\Omega).
 \tag{29}
\]
Thus the off-spectrum row is still explicit. On the actual
module, \(\mathcal W_N=0\), and (28) yields the scalar
\[
 \mathcal R_N(M):=\prod_{j=0}^{N-1}\rho_j
       =\frac{1-M^{-2N}}{1-M^{-2N}K^{-2N}}
       =\frac{1-M^{-2N}}{1-M^{-2mN}}.
 \tag{30}
\]
Iterating (27) and using periodicity now gives the exact row
\[
 \boxed{\quad
 \mathscr A_0=\frac{1}{1-\mathcal R_N(M)}
       \sum_{j=0}^{N-1}
             \left(\prod_{\ell=j+1}^{N-1}\rho_\ell\right)\eta_j.
 \quad}\tag{31}
\]
The empty product is one. This is an operator identity on the
whole actual tail module, including its Casimir Jordan blocks.
It initially holds on the generic meridian set of (26), and
its continuation is the analytic finite polynomial (9).
Individual \(D(K_j)\) inverses at completeness are not thereby
declared defined; their cancellations occur in the full row.

The assembled scalar inverse in (31) has uniform local control.
For \(u=N\Log M\),
\[
 \mathcal R_N(M)=\mathcal R(u)
          =\frac{1-e^{-2u}}{1-e^{-2mu}},\qquad
                  \mathcal R(0)=\frac1m.
 \tag{32}
\]
For fixed \(m\ge2\), choose \(\eta>0\) so that this removable
function is analytic on \(|u|\le\eta\) and
\(\lvert1-\mathcal R(u)\rvert\ge(m-1)/(2m)\). Then
\[
              |(1-\mathcal R(u))^{-1}|\le\frac{2m}{m-1}.
 \tag{33}
\]
Cauchy estimates on a smaller \(u\)-disk bound all fixed
\(u\)-derivatives independently of \(N\). Since
\(\partial_M u=N/M\), the corresponding fixed meridian
derivatives are \(O(N^j)\). These bounds concern only the
assembled scalar inverse. They do not bound the individual
clock transports, the endpoint kernels, or the norm of \(A_N\).
In particular (31) fixes the literal normalization from the
forced rows, rather than estimating its size.

## 5. Actual kernel and relative-window consequences

All matrices in (6), (9), and (31) are on J's original finite
spaces. Applying its compact kernel
\(K_B(\mathbf w,\mathbf z)=v(\mathbf w)B c(\mathbf z)\)
therefore gives exact finite coherent identities and exact
convolutions on the original compact resolutions. Every cap
\(\prod_i(1+w_i z_i)^d\), Cartan factor, factorial dual, and
meridian derivative remains. This does not replace an operator
kernel by the scalar evaluation in (13).

There is also an explicit relative row. For any two actual
partial-resolution matrices \(P_{\mathcal C},P_{\mathcal D}\)
from J, define
\(\Delta_j=P_{\mathcal C}\mathscr A_j-\mathscr A_jP_{\mathcal D}\).
Multiplying (27) on both sides, without commuting a window
past a coefficient, gives
\[
 \Delta_{j+1}
   =\rho_j\Delta_j+[P_{\mathcal C},\rho_j]\mathscr A_j
                         +P_{\mathcal C}\eta_j-\eta_jP_{\mathcal D}.
 \tag{34}
\]
Its periodic solution is the same ordered sum as (31), with
\(\eta_j\) replaced by the three retained terms after
\(\rho_j\Delta_j\) in (34). Thus the window comparison has
both a coefficient commutator and an explicit extreme-tail
source. J's boundary transgression applies to the two partial
resolutions, with their complementary chains retained. No
term in (34) is zero merely because the full trace is sewn.

The finite formulas are holomorphic or meromorphic in the
common meridian before taking their prescribed continuations.
They may consequently be differentiated with all displayed
normal terms. They are not ordinary quantum-parameter-normal
identities obtained by differentiating the root equations.

For clarity, the following distinction is essential. Equation
(30) used the actual operator relation \(\mathcal W_N=0\).
At a geometric scalar argument \((K,\Omega)\), even when
\(\Omega=z+z^{-1}\) comes from a loxodromic representation,
the polynomial \(\mathcal W_N\) in (15) need not vanish.
Equations (14), (18), and (29) retain its complete contribution.
Nor does the finite-node evaluation (20) define a preferred
complex interpolation of its integer label \(l\). The canonical
scalar continuation is the original polynomial (9).

The result is an actual factorization of the opposite kernel,
its explicit finite Gauss polynomial, and a forced cyclic
normalization with a controlled assembled meridian denominator.
The high-degree endpoint kernel and the relative row (34)
remain to be estimated in a proposed geometric chart. No
nonzero local amplitude, source-sector coefficient, or
geometric relative-cycle transport follows from these identities.

## Complete proof directs

* J: notes/research_opposite_polarization_source_kernel.md,
  SHA256 d52c6dd8e62f575a262fc7af460e258f7cb0e40b5a9c037ac46dd8d151002d44.
* R: notes/research_actual_reduced_braid_source.md,
  SHA256 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.

Both complete directs were freshly read nontruncated in this
active author sequence. Every used implication was checked.
Only written mathematics and text/hash operations were used.
Frozen and public files were not changed.
