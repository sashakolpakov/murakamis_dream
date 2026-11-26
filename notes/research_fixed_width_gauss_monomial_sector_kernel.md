# Actual fixed-width Gauss monomial kernels on initialized sectors

Private written proof, 18 November 2026.

The exact suffix-Casimir equations propagate the actual initialized
column to a full monomial kernel at any fixed width. The initial output
domain is a separated winning sector of W, not a disk about the
vacuum. A finite input-degree estimate, with an explicit output-shift
budget, pays the entire remaining input cap. Compatibility of the
transport equations is obtained from the actual finite solutions.

The ordinary-binomial input is not transformed in this theorem.
Inactive input phase slopes vanish. Its Cauchy interfaces can therefore
carry new exponential phases, and cannot be replaced by repetitions
of the two-head Bessel saddle.

## 1. Original finite matrices and the initialized domain

Use
\[
 c_0=2\pi i,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1},\quad d=N-1,\quad f_n=(Q;Q)_n.
 \tag{1}
\]
Fix \(r\ge2\), put \(s=r-1,\ p=r-2\), and restrict the actual
\(r\)-head space to degree \(0\le T\le d\). Write its basis as
\[
 |\beta\rangle=|\beta_1,\ldots,\beta_s,T-|\beta|\rangle,
 \qquad \beta\in{\mathbb Z}_{\ge0}^s,\quad |\beta|\le T.
\]
The chamber and exact clocks are
\[
 \sigma_N=(T+1)/N\in I\Subset(1/2,1),\quad
 C=Q^{-T-1},\quad K_{r,T}=x^rQ^{-T},\quad c_i=x^{r-i}.
 \tag{2}
\]
The single-head actions are
\[
 Ew_a=(Q^{-a}-1)w_{a-1},\quad
 Fw_a=(1-Q^{a+1})w_{a+1},\quad Kw_a=xQ^{-a}w_a,
\]
with the actual zero endpoint arrows. The ordered totals satisfy
\(E_{AB}=E_AK_B+E_B\), \(F_{AB}=F_A+K_A^{-1}F_B\).
G's literal Gauss operator is
\[
 A_N^{(r)}=(-1)^dN\sum_{n=0}^d
       \frac{(-1)^nq^{n^2}}{f_n^2}F^nE^nK^{d-n}.
 \tag{3}
\]
It is a polynomial in the total \(K,\Omega\). Every consecutive
partial Casimir commutes with (3), by its centrality on the
corresponding interval and the ordered coproduct.

These matrices are symmetric in the original bilinear basis.
Indeed on one head \(E^t=x^{-1}KF\), \(F^t=xEK^{-1}\).
The coproduct gives the same identities for any interval. Hence
\((FE)^t=KFEK^{-1}=FE\), and every interval Casimir is symmetric.
Equation (3), or its Casimir-polynomial form in G, is consequently
symmetric on each fixed degree.

Let \(a_{00}^{(r)}=(A_N^{(r)})_{\mathbf0,\mathbf0}\). W proves
that it is nonzero for all large \(N\) in (2). Retain it exactly,
and define the full monomial kernel
\[
 {\cal K}_N(\rho,\zeta)
  =\sum_{|\alpha|,|\beta|\le T}
       \frac{(A_N^{(r)})_{\alpha\beta}}{a_{00}^{(r)}}
       \prod_{i=1}^s c_i^{-\alpha_i-\beta_i}
                         \rho^\alpha\zeta^\beta.
 \tag{4}
\]
Its original homogeneous factors are
\[
 v_{\mathbf w}A_N^{(r)}
       \sum_\beta
       \left(\prod_{i=1}^s z_i^{\beta_i}\right)z_r^{T-|\beta|}
                              |\,\beta,T-|\beta|\,\rangle
  =a_{00}^{(r)}(w_rz_r)^T{\cal K}_N(\rho,\zeta),
 \quad \rho_i=c_iw_i/w_r,\quad \zeta_i=c_iz_i/z_r.
 \tag{5}
\]
The input on the left is monomial; it has no inserted binomial weights.

First shrink W's seed disk to lie inside the output disk of L's
two-head analytic phase. Choose a winning index \(j\) and a small simply connected output
polydisk \(D\), with a larger polydisk \(D^+\), on which W's
coordinates are distinct, nonzero, and
\[
 \Re\phi(\rho_j;C)\ge\eta,\qquad
 \Re\phi(\rho_j;C)\ge
       \max_{i\ne j}\{0,\Re\phi(\rho_i;C)\}+\eta.
 \tag{6}
\]
Assume the same inequalities with a smaller fixed gap hold on a
neighborhood of \(\overline {D^+}\), uniformly for the chosen compact
parameter arc in (2). Such polydisks exist by W. Its exact boundary
theorem gives
\[
 N^p{\cal K}_N(\rho,0)
     =e^{N\phi(\rho_j;C)}{\cal A}_{\rm in}(\rho;C)
                                      (1+O(N^{-1})),
 \tag{7}
\]
with holomorphic relative error and fixed derivatives, where
\[
 {\cal A}_{\rm in}
 =\frac{\rho_j^p}{\prod_{i\ne j}(\rho_j-\rho_i)}
       \frac{p!\,A_G(\rho_j;C)W(\rho_j;C)^p}
                    {[a(C^{-1}-1)]^p},
 \quad a=2/c_0,\quad W(t;C)=\frac{C^{-1}-Y_B(t;C)}t.
 \tag{8}
\]
Here \(\phi,A_G,Y_B\) are the actual two-head functions specified in
W and L. Every factor in (8) is a unit on the chosen domain.
The losing boundary branches remain inside the actual left side of
(7); W estimates their full complement.

## 2. An exact triangular system at every width

For \(1\le i\le s\), write \(\Omega_i=\Omega_{[i,r]}\),
\(K_i=xQ^{-J_i}\), and
\(\Omega_{r}=-2I\). The consecutive totals on \([i+1,r]\) are
denoted \(E_t,F_t,K_t\). Define
\[
 D_i=\Omega_i-K_i^{-1}\Omega_{i+1}.
 \]
Direct expansion, with the displayed operator order, gives
\[
 D_i=K_t[F_iE_i+q(K_i-K_i^{-1})]
                  +F_iE_t+K_i^{-1}F_tE_iK_t.
 \tag{9}
\]
For a physical input \(\beta\), put \(k_i(\beta)=xQ^{-\beta_i}\).
Since \(\Omega_{i+1}\) preserves \(\beta_i\), the actual two
commutators give the exact column identity
\[
 A_ND_i|\beta\rangle
       =[\Omega_i-k_i(\beta)^{-1}\Omega_{i+1}]A_N|\beta\rangle.
 \tag{10}
\]
There is just one term of \(D_i|\beta\rangle\) which increases
\(|\beta|\):
\[
 a_i^+(\beta)|\beta+e_i\rangle,\qquad
 a_i^+(\beta)=(1-Q^{\beta_i+1})(Q^{-\beta_r}-1),
 \quad \beta_r=T-|\beta|.
 \tag{11}
\]
It comes from the last-head summand of \(F_iE_t\), so there is no
additional tail clock. The other terms of \(F_iE_t\) preserve
\(|\beta|\); the last-head recipient of \(F_tE_iK_t\) lowers it,
and its other recipients preserve it. The first term of (9) is
diagonal. Thus every other input column in (10) has degree at most
\(|\beta|\). Formula (10) determines the column \(\beta+e_i\)
from columns of lower input degree. Different choices of a predecessor
are compatible because these are identities of the same actual matrix.
All endpoint zeros in (9)--(11) are retained.

Choose a fixed small \(\delta>0\). For \(|\beta|\le\delta N\),
\[
       |a_i^+(\beta)|\ge c(\beta_i+1)/N.
 \tag{12}
\]
The first factor has this lower bound on the short root arc, while
the second stays away from zero by (2).

There is a useful generating version of its highest-input term.
Let \(T_i f(\zeta)=f(\zeta_1,\ldots,Q\zeta_i,\ldots)\) and
\(T_{\rm all}=\prod_iT_i\). The term (11), in (4), is
\[
       \frac{c_i}{\zeta_i}(1-T_i)(CT_{\rm all}-1){\cal K}_N.
 \tag{13}
\]
The numerator is divisible by \(\zeta_i\). On the formal logarithm
\(V_N=N^{-1}\log(N^p{\cal K}_N)\), the coefficient of a new
input multi-index \(\gamma\), \(|\gamma|=n\), has exact linear
factor
\[
       c_iN(1-Q^{\gamma_i})(CQ^n-1),\qquad \gamma_i>0.
 \tag{14}
\]
Its modulus is comparable to \(\gamma_i\) for \(n\le\delta N\).
All other terms use lower input degree, with finite output clock
shifts. This follows either by expanding (13), whose input increments
have no constant term, or by taking the logarithm of (10).
There is no extracted-vacuum term in these full-kernel equations.
Reindexing an input lowering or transfer pairs each negative input
monomial with its vanishing zero-occupation clock difference. The
potential degree-\(T+1\) raising term in (13) is killed by
\(CQ^{T+1}-1=0\). Thus all normalized exponentials below are
differences of the logarithm at nearby clock arguments, rather than
an uncontrolled quotient of a separately extracted column by the
whole kernel.

## 3. Actual analytic estimates with an output-shift budget

We record the estimate in sufficient detail to distinguish it from
formal multi-variable Cauchy data. Initially \(V_N\) is a formal
input series whose coefficients are holomorphic on \(D^+\); the
constant coefficient is the calibrated logarithm of (7).

All output operators in (10) have a fixed finite shift alphabet,
depending only on \(r\). In homogeneous coordinates their actions
are obtained from
\[
 E_i=w_i^{-1}(T_i^{-1}-1),\quad
 F_i=w_i(1-QT_i),\quad K_i=xT_i^{-1}.
 \tag{15}
\]
After setting \(w_r=1\) and keeping total degree \(T\), their
coefficients are analytic on \(D^+\) and their shifts are
\(\rho\mapsto Q^\nu\rho\), with integer vectors \(\nu\) in a
fixed finite set. Factors \(Q^{\pm T}=Q^{\mp1}C^{\mp1}\) are kept
exact. No large coefficient depending on an unscaled occupation is
introduced.

Expand output coefficients about the center of \(D^+\), and
majorize absolute Taylor coefficients by a positive scalar variable
\(y\), which dominates the sum of coordinate displacements. There
is a constant \(L_r\) such that each output shift is majorized by
\[
 \varphi_h(y)=e^{L_rh}(1+y)-1,\qquad h=1/N.
 \tag{16}
\]
For a positive analytic majorant \(F\), the integral of the derivative
along the short rotation also gives
\[
 N\,|f(Q^\nu\rho)-f(\rho)|
       \preccurlyeq L_r(1+y)F'(\varphi_h(y)).
 \tag{17}
\]
Here \(\preccurlyeq\) refers to absolute Taylor coefficient
domination, with constants enlarged for the fixed alphabet.
One can verify (17) directly by differentiating
\(f(e^{t\nu}\rho)\) and majorizing its Taylor series on
\(|t|\le |c_0|/N\).

Use the input majorant variable \(z=\zeta_1+\cdots+\zeta_s\).
An input coefficient of total degree \(n\) is bounded by the
coefficient of \(z^n\), with its multinomial factor \(n!/\gamma!\).
Under this convention division by (14) is bounded by a constant
times division by \(n\): indeed
\(\gamma_i n!/\gamma!=n(n-1)!/(\gamma-e_i)!\).

Attach to each degree-\(n\) coefficient the output padding
\(\varphi_{nh}(y)\). A subsequent output shift consumes one further
step. In a product with input degrees \(n_1,\ldots,n_k\), every
shifted factor fits inside the degree budget because
\[
             \max_\ell(n_\ell+1)\le\sum_\ell n_\ell+1.
 \tag{18}
\]
The same inequality includes arbitrarily many degree-zero boundary
factors. Analytic coefficient majorants may also be evaluated at
the enlarged argument. Choose \(\delta\) so that every
\(\varphi_{nh}\), \(n\le\delta N+1\), stays within the enlarged
winning domain. This is where the fixed gap in (6) is used.

We spell out a convergent positive majorant for the resulting
logarithmic induction. After removing the exact coefficient (14),
output increments are bounded by a constant times
\((1+y)U_y\), and input increments by a constant times \(zU_z\).
The finite coefficients in (9),(15) have a positive analytic
majorant \(B(y)\). Input terms preserving degree carry at least one
input variable after removable division. Their linear differences
are bounded by \(B(y)zU_z\). A product of two such differences is
bounded by \(B(y)zU_z^2\), multiplied by an exponential of
\(B(y)zU_z\). For the linear double differences the coefficient
bound \(n/N\le\delta\) reduces \(N^{-1}n^2\) to a constant times
\(n\). All output terms are bounded by an exponential of the
output increment and the input increment. Thus, with positive
constants enlarged, one may use
\[
 \begin{split}
 U_z=B(y)\{&1+U+U_y+zU_z\\
          &+\exp[B(y)((1+y)U_y+zU_z)]\\
          &+zU_z^2\exp[B(y)zU_z]\},\qquad U(y,0)=U_0(y).
 \end{split}\tag{19}
\]
Here \(U_0\) dominates the calibrated boundary logarithm on a
larger output domain. The estimates above, with (18), prove
coefficientwise domination by induction on total input degree;
they do not require that output derivatives be bounded by a fixed
number independently of their order.

Equation (19) is analytic with a genuine local solution. Its
right side has derivative \(O(z)\) with respect to the unknown
\(U_z\). Solve for \(U_z=H(y,z,U,U_y)\) by positive analytic
iteration on a bounded polydisk. Integrate its characteristic
system
\[
 \dot y=-H_P,\quad
 \dot U=H-PH_P,\quad
 \dot P=H_y+H_U P.
 \tag{20}
\]
The initial projection derivative is one. Uniform analytic
Picard iteration for a small fixed complex time, followed by its
analytic inverse, constructs the solution. All coefficients are
nonnegative, since the implicit iteration and input-degree recursion
are positive. This proves convergence, and bounds the degree-\(n\)
logarithmic coefficient by a fixed geometric sequence on a smaller
output domain, with the padding (16). The constants are uniform in
\(N,T\); no resonance beyond the low band is inverted.

The same argument gives stability. Subtract two logarithmic rows
with uniformly bounded positive backgrounds. Factor each exponential
difference by the increment difference. After the normal term (14)
has been removed, the new majorant is linear:
\[
 E_z=B_1(y,z)(E+E_y)+zB_2(y,z)E_z+\varepsilon^kB_3(y,z),
 \quad E(y,0)=O(\varepsilon^k),\quad \varepsilon=1/N.
 \tag{21}
\]
The coefficients are fixed positive analytic functions on smaller
domains. The output padding remains (18). Invert \(1-zB_2\) and
use (20) in its linear form. It follows that the low logarithmic
error is \(O(\varepsilon^k)\), uniformly on a still smaller
output domain and input polydisk. This estimate applies in particular
for \(k=1,2\).

There is no omitted finite tail. All entries of the original total
\(E,F,K^{\pm1}\) have uniformly bounded operator norms at fixed
width. As in L, \(e^{-cN}\le |f_n|\le e^{cN}\). Equations (3)
and W's nonzero normalization give an \(e^{cN}\) bound for every
coefficient of \(N^p{\cal K}_N\). On any fixed bounded output
domain, summing its finite output monomials changes only \(c\).
Let \(V_N^{[k]}\) retain input degrees at most
\(k_N=\lfloor\delta N\rfloor\). Then
\(e^{NV_N^{[k]}}\) and \(N^p{\cal K}_N\) agree through that input
degree. Both are bounded by \(e^{cN}\) on a fixed comparison
domain. Cauchy's coefficient estimate in \(s\) input variables gives
a tail bounded by
\[
       C(k_N+1)^{s-1}e^{cN}(\varrho/R)^{k_N+1}
                                      /(1-\varrho/R)^s.
 \tag{22}
\]
The inverse of \(e^{NV_N^{[k]}}\) costs at most \(e^{c'N}\).
Choose the fixed final input radius \(\varrho\) sufficiently small
after \(\delta\). Then (22) is exponentially relative. This
proves actual zero-freeness and whole-cap recovery on the chosen
output sector times that input polydisk.

## 4. Phase, compatible transport, and the actual kernel

Let \(S_2(u,v;C)\) be L's initialized two-head phase. The principal
solution on the winning branch is
\[
                        S(\rho,\zeta;C)=S_2(\rho_j,\zeta_j;C).
 \tag{23}
\]
This can be checked in every suffix row, not merely the total
Casimir. In the monomial principal symbols
\[
 e_i=w_i^{-1}(e^{-c_0t_i}-1),\quad
 f_i=w_i(1-e^{c_0t_i}),\quad k_i=-e^{-c_0t_i},
\]
every inactive momentum \(t_i\) is zero. Its head has
\(e_i=f_i=0,k_i=-1\). A suffix containing only such heads and
the last head has constant Casimir. A suffix containing the
active head reduces to a scalar sign times the active two-head
Casimir. If there are \(h\) inactive heads between \(j\) and \(r\),
rescaling its first coordinate by \((-1)^h\) produces precisely
the active two-head coproduct. The leading value of
\(c_j=x^{r-j}\) in (4) supplies this sign. Thus L's two-head
Hamiltonian identity proves all principal rows. The exact \(x\)
half shifts and \(Q^T=Q^{-1}C^{-1}\) remain for transport.

For clarity compatibility of the transport is not assumed. The
principal substitution (23) has residual \(O(N^{-1})\) in all
normalized logarithmic rows, and its boundary differs from the
actual logarithm by \(O(N^{-1})\), by (7). The stability estimate
(21), followed by (22), gives
\[
                         V_N-S=O(N^{-1}).
 \tag{24}
\]
Consequently \(W_N=N(V_N-S)\) is a uniformly bounded holomorphic
family on smaller domains. At each limiting clock \(C\) in the
compact arc, take integer degrees tending to it. Cauchy bounds on
Taylor coefficients and a diagonal subsequence give a uniformly
convergent subsequence on smaller polydisks. Its analytic limit
\(\alpha\) satisfies every first-order transport row, obtained by
expanding the exact shifts in (9),(10),(13), and
\[
                      \alpha(\rho,0)=\log{\cal A}_{\rm in}(\rho;C).
 \tag{25}
\]
At the initial input face the normal coefficient in the \(i\)-th
row is a nonzero scalar multiple of
\(c_0(C-1)\partial_{\zeta_i}\). More generally its formal
input-degree recursion is the limit of (14), so it determines
each next coefficient uniquely from the lower input degrees.
Thus the limit is unique and the transport rows are compatible.
Their coefficients and this recursion depend analytically on \(C\);
the Cauchy bounds just obtained are uniform on its compact arc.
This constructs a uniformly analytic transport solution without
assuming a globally noncharacteristic multi-time system.
Uniform analyticity here is in the output and input variables.
Analytic coefficient dependence on \(C\) follows from the recursion;
the real-arc limit argument does not assert a uniform complex-\(C\)
neighborhood.

Equivalently \(\alpha\) is specified completely by (25) and the
coefficient of \(N^{-1}\) in the exact logarithmic equations
(9),(10),(13), with \(q=e^{c_0/(2N)}\),
\(x=-e^{-c_0/(2N)}\), \(Q^T=Q^{-1}C^{-1}\) before expansion.
This definition retains every subprincipal clock and the
\(T=N\sigma_N-1\) offset. It leaves no freely chosen amplitude.

Substitute \(S+\alpha/N\) into the finite equations. Taylor
expansion of their fixed shift alphabet on larger polydisks gives
an analytic residual \(O(N^{-2})\), since the principal and all
transport rows vanish. The boundary error is \(O(N^{-2})\)
by (7). Applying (21) with \(k=2\), then recovering the entire
cap by (22), proves the actual result
\[
 \boxed{\quad
 {\cal K}_N(\rho,\zeta)
     =N^{-p}e^{NS_2(\rho_j,\zeta_j;C)}
            {\cal A}_r(\rho,\zeta;C)(1+O(N^{-1})),
 \qquad {\cal A}_r=e^\alpha .
 \quad}\tag{26}
\]
The amplitude is an analytic unit and equals (8) at \(\zeta=0\).
The relative error and all fixed output/input derivatives have the
same estimate on smaller domains. All losing branches of the
initialized column and every finite input coefficient were included
in the proof. No positivity or tame spectral frame was used.

## 5. Why the ordinary-binomial input remains a separate step

Equation (26) is a full matrix kernel in its stated monomial
polarization. It has only one active principal input slope:
\[
 S_{\zeta_i}(\rho,0)=0\quad(i\ne j).
 \tag{27}
\]
Thus L's nonzero-slope coefficient circle does not apply in all
input variables. The distinction is substantive. Already the
finite identity kernel in one such variable has
\[
 \sum_{a=0}^d(\rho\zeta)^a
       =\frac{1-(\rho\zeta)^N}{1-\rho\zeta};
\]
on a small product disk its principal phase is zero, while its
literal binomial input is
\(\sum_a\binom da(\rho\eta)^a=(1+\rho\eta)^d\).
Its exponential phase is recovered at the Cauchy interface, not
from a nonzero small-circle slope. An \(O(N^{-1})\) monomial
relative estimate alone does not justify that further transform.

The inactive dependence of \({\cal A}_r\), whose initial row (8)
contains explicit Cauchy factors, is therefore retained in full.
No pole is selected or deleted here. A later binomial theorem
would have to keep those interfaces, their caps and competing
branches on the actual extraction cycles.

Finally the original factors in (5), the exact \(a_{00}^{(r)}\),
and G's surrounding quotient braid, top Cartan and turnover
remain unchanged. Fixed real occupation sectors do not establish
a chart for a loxodromic geometric total moment. No meridian
normal, geometric-source coefficient, or closed-source lower
bound is asserted.

## Complete proof directs

* G: notes/research_opposite_kernel_forced_cyclic_normalization.md,
  SHA256 42e6d6c3a5039859c241a2832de56301eff49d749db86d67868f3534c89aaaaa.
* W: notes/research_fixed_width_gauss_boundary_branches.md,
  SHA256 cdcb82d2bd48948ff45baaec65a71f639607e10a9bc12acff344e34ae972d404.
* L: notes/research_actual_gauss_coherent_goursat_kernel.md,
  SHA256 37ade960cb7938372b7854b00aebc1df82e648144f850fcd4a356f68a00159e1.

Written mathematics only. Frozen and public files were not changed.
The entire matching final was reread nontruncated in this author
sequence. Complete G and L whole reads were explicitly retained fresh
and unchanged from the immediately preceding active author/review
sequence; complete W was freshly whole-read during its matching formal
peer. Every used implication was checked and all four pins renewed.
Independent matching peer review and parent adoption remain separate.
