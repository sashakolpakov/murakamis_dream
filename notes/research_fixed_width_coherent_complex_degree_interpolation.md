# Fixed-width coherent Gauss kernels on a marked complex-degree bundle

Private written proof, 18 November 2026.

The complete physical coherent Gauss kernels have an exact analytic
interpolant at every fixed width on a bounded complex-degree strip.
The construction first continues the entire capped binomial input and
the actual width recursion. It then continues the low logarithmic
output equations and pays the remaining physical coefficients by an
explicit cardinal correction. The resulting local amplitude is nonzero
and its full mixed phase is nondegenerate.

The input coordinates form a specified bundle over the degree strip.
This qualification is necessary: a fixed input coordinate need not stay
in the growing boundary sector along an arbitrarily tall strip. Both
the nodal correction and the final residue contour retain this coordinate
change. No finite representation at noninteger occupation, exact
off-grid integrability, or closed-source coefficient is asserted.

Complete directs are I, W, B and K, pinned below. Their frozen files
are unchanged.

## 1. Physical data, the strip, and the input bundle

Use
\[
 c_0=2\pi i,\quad Q=e^{c_0/N},\quad q=e^{c_0/(2N)},\quad
 d=N-1,\quad x=-q^{-1},\quad \epsilon=N^{-1}.
 \tag{1}
\]
Fix the number of tail heads \(r\ge2\), and put \(s=r-1,p=r-2\).
The actual matrices and coherent normalization are those of K:
\[
 U_{N,T}(\rho,\xi)=
 \sum_{|\alpha|,|\beta|\le T}
 \frac{A_{\alpha\beta}}{a_{00}^{(r)}}c^{-\alpha-\beta}
 \rho^\alpha\xi^\beta
 \frac{\binom d{T-|\beta|}\prod_i\binom d{\beta_i}}{\binom dT},
 \qquad c_i=x^{r-i}.
 \tag{2}
\]
Thus
\[
 v(w)A_N^{(r)}c_T(z)
 =a_{00}^{(r)}(w_rz_r)^T\binom dT\,U_{N,T},\qquad
 \rho_i=c_iw_i/w_r,\quad \xi_i=c_iz_i/z_r .
 \tag{3}
\]
No coefficient or cap in this finite polynomial is changed.

Choose a rectangle and several slightly larger buffered rectangles
\[
 \mathscr R=\{a\le\Re\sigma\le b,\ |\Im\sigma|\le H\},\qquad
 \tfrac12<a<b<1,\quad H<\infty ,
 \tag{4}
\]
all with real part strictly between \(1/2\) and \(1\). Set
\[
 C=e^{-c_0\sigma},\quad \tau=\sigma-\epsilon,\quad
 a_0^{\rm lin}=2/c_0,\quad b_\sigma=\frac{\sigma}{1-\sigma}.
 \tag{5}
\]
The superscript on \(a_0^{\rm lin}\) distinguishes this fixed slope
from activity radii. Both \(C-1\) and \(C+1\) are separated from zero
on every such compact rectangle.

Take a compact input-coordinate domain, with successively larger
domains, in
\[
 \eta=(a_*,\vartheta),\qquad
 0<|a_*|<a_{\max},\quad |\arg a_*|<\theta_0<\pi/3,\qquad
 \sum_{i=1}^s\vartheta_i=1 .
 \tag{6}
\]
Shapes are bounded and each \(\vartheta_i\) is nonzero on the
domains used for propagation. Define the principal, \(N\)-independent
bundle map
\[
             \xi_i(\sigma,\eta)
       =\frac{\vartheta_i a_*^2}{a_0^{\rm lin}b_\sigma}.
 \tag{7}
\]
It is locally invertible in the \(s\) input variables. On compact
subdomains its Jacobian and inverse Jacobian are bounded. The exact
binomial formulas below still use \(\tau=\sigma-\epsilon\), not
\(\sigma\). Consequently their sector parameter differs from \(a_*\)
by \(1+O(\epsilon)\); the buffered sector in (6) contains it.

Let \(\sigma_T=(T+1)/N\), and let \(\mathcal T_N\) be the physical
nodes in the real interval of (4). The theorem constructs
\(\mathfrak U_N(\sigma;\rho,\eta)\), holomorphic on buffered versions
of (4),(6) and a small output polydisk, such that
\[
 \mathfrak U_N(\sigma_T;\rho,\eta)
       =U_{N,T}(\rho,\xi(\sigma_T,\eta)) .
 \tag{8}
\]
For any prescribed \(L>0\), the output radius can be chosen so that
\[
 \mathfrak U_N=\widehat U_N\{1+O(e^{-LN})\}
   =N^{-p-1/2}e^{N\mathscr S(\rho,\eta;\sigma)}
        \mathscr A(\rho,\eta;\sigma)\{1+O(N^{-1})\},
 \qquad \mathscr A\ne0 .
 \tag{9}
\]
The surrogate \(\widehat U_N\) is an explicitly specified finite
low-log exponential. The relative estimates hold with every fixed
derivative on smaller domains. The phase has nonzero full mixed
determinant in output and input coordinates. Radii depend on the
prescribed strip and compact punctured input domain.

## 2. A finite binomial adapter at every complex degree

Write \((z)_{\underline k}\) and \((z)_k\) for falling and rising
ordinary products. Define the finite polynomial
\[
 \mathfrak B_{s,N}(z;\tau)=
 \sum_{0\le\beta_i\le d}
   \left(\prod_i\binom d{\beta_i}\right)
   \frac{(N\tau)_{\underline{|\beta|}}}
        {[N(1-\tau)]_{|\beta|}}z^\beta .
 \tag{10}
\]
Its degree is at most \(sd\). Its denominators are units because
\(\Re(1-\tau)>0\). At a physical node the falling numerator
vanishes for \(|\beta|>T\), so exactly
\[
 \mathfrak B_{s,N}(z;T/N)
 =\binom dT^{-1}[u^T](1+u)^d\prod_i(1+uz_i)^d .
 \tag{11}
\]
In particular the total cap and all individual head caps are present.

Put \(D_i=z_i\partial_{z_i}\), \(D=\sum_iD_i\). Coefficient comparison
gives the exact compatible equations
\[
 D_i[N(1-\tau)+D-1]\mathfrak B_{s,N}
       =z_i(d-D_i)(N\tau-D)\mathfrak B_{s,N}.
 \tag{12}
\]
For a coefficient of degree \(k\), the ratio is
\[
 \frac{[\!z^\beta\!]\mathfrak B}{[\!z^{\beta-e_i}\!]\mathfrak B}
 =\frac{d-\beta_i+1}{\beta_i}
          \frac{N\tau-k+1}{N(1-\tau)+k-1}.
 \tag{13}
\]
At a zero coefficient use the cross-multiplied identity in (13).
The factor \(d-D_i\) also kills the possible coefficient beyond
\(\beta_i=d\), so (12) holds as a whole polynomial identity.

Here is an actual complex-parameter estimate for (10). It does not
continue B's real-degree error. Formally let \(W=N^{-1}\log\mathfrak B\),
\(P=DW\), \(p_i=D_iW\), with \(W(0)=0\). Summing (12) gives
\[
 (1-\tau)P+P^2+\epsilon(DP-P)
 =\sum_i z_i\{(1-p_i)(\tau-P)
                       +\epsilon(D_iP-\tau+P)\}.
 \tag{14}
\]
The new coefficient of total degree \(k\) has diagonal
\[
                 k[1-\tau+\epsilon(k-1)],
 \qquad |\,\cdot\,|\ge c k .
 \tag{15}
\]
All other terms have lower total degree. On the band \(k\le\delta N\),
the additional \(\epsilon z_iD_iP\) is bounded coefficientwise by
a constant times the corresponding first-derivative term: its extra
index costs \(\epsilon k\le\delta\). With \(z=\sum_i|z_i|\), a positive
majorant for the divided equation can therefore be chosen as
\[
 U_z=C_1(1+z)\{1+zU_z+zU_z^2\},\qquad U(0)=0 .
 \tag{16}
\]
Increase \(C_1\) to include the bounded \(\tau\)-coefficients and
the finite number of heads. Its analytic root at zero exists because
every occurrence of the unknown derivative on the right has a factor
\(z\). Positive coefficient induction using (15) bounds the low
logarithm by a common convergent series, uniformly on the full
complex rectangle.

The whole polynomial has a separate bound. For \(k\le sd\), every
factor \(|N\tau-j|/[N\Re(1-\tau)+j]\) is bounded by a uniform
constant. The binomial factors and the polynomially many indices
then bound (10) by \(e^{C_2N}\) on a fixed comparison polydisk.
The exponential of its low logarithm has the same bound and agrees
with it through degree \(\lfloor\delta N\rfloor\). Cauchy's tail
estimate, on a smaller polydisk, is
\[
 C(k_N+1)^{s-1}e^{C_3N}
       \frac{(r/R)^{k_N+1}}{(1-r/R)^s},\qquad k_N=\lfloor\delta N\rfloor .
 \tag{17}
\]
Shrinking \(r\) after \(\delta,R\) pays this error relatively. This
proves a genuine zero-free disk for the actual polynomial (10).

The explicit phase and amplitude are B's algebraic functions, now
on the complex rectangle. Namely \(u\) is the analytic root at
\(u=b_\tau=\tau/(1-\tau)\) of
\[
 \frac{u}{1+u}+\sum_i\frac{uz_i}{1+uz_i}=\tau ,
 \tag{18}
\]
and
\[
 \begin{split}
 S_B&=\log(1+u)+\sum_i\log(1+uz_i)-\tau\log u
                 +\tau\log\tau+(1-\tau)\log(1-\tau),\\
 D_B&=\frac{u}{(1+u)^2}+\sum_i\frac{uz_i}{(1+uz_i)^2},\\
 A_B&=\frac{\sqrt{\tau/(1-\tau)}}
            {(1+u)\prod_i(1+uz_i)\sqrt{D_B}} .
 \end{split}
 \tag{19}
\]
Marks continue from \(z=0\), where \(S_B=0,A_B=1\).
The implicit derivative there is \(\tau(1-\tau)\ne0\).
One can verify the first two orders in (14) directly. Equivalently,
their recursively determined coefficients are holomorphic in \(\tau\)
and agree with (19) on the real interval by B's coefficient-circle
proof, hence agree throughout the rectangle. This identifies the
formal coefficients; it does not continue an asymptotic error.

Substitution of \(S_B+\epsilon\log A_B\) in (14) leaves a uniformly
analytic \(O(\epsilon^2)\) residual. Subtraction uses the same diagonal
(15); nonlinear differences have a factor \(z\), and the scaled
second derivatives have the same low-band bound as before. The
linear version of (16) gives \(O(\epsilon^2)\) logarithmic error.
Together with (17) this proves
\[
 \mathfrak B_{s,N}=e^{NS_B}A_B(1+O(N^{-1}))
 \tag{20}
\]
uniformly on a whole small polydisk and the complex rectangle, with
fixed derivatives on smaller domains. Every high coefficient of
(10) was included in (17).

## 3. Exact continued boundary and its selected circle

Take I's explicitly cardinal-corrected two-tail monomial interpolant
on a larger rectangle, and restrict it to its first axis:
\[
                   \mathfrak G_{2,N}(\sigma;t)
                     =\mathfrak K_N(\sigma;t,0).
 \tag{21}
\]
It has value one at \(t=0\), equals the actual \(G_{2,N,T}\) at every
specified physical node, and has the whole-disk unit
\(e^{N\phi(t;C)}A_G(t;C)(1+O(N^{-1}))\). I proves these estimates
directly on the complex rectangle, including all caps and its
cardinal correction.

Define \(\mathfrak V_2=\mathfrak G_{2,N}\) and, successively,
\[
 t\mathfrak V_{j+1}(t)=
 (t-Q^{-1})\mathfrak V_j(Qt)+Q^{-1}C^{-1}\mathfrak V_j(t)
       +(Q^{-1}-Q^{-1}C^{-1})\mathfrak V_j(0).
 \tag{22}
\]
The numerator vanishes at zero; division is its holomorphic divided
difference. Put \(\nu_j=\mathfrak V_j(0)\) and
\(\mathfrak G_j=\mathfrak V_j/\nu_j\). At a physical node (22) is
W's exact width recursion, so
\[
 \mathfrak V_j(\sigma_T;t)=\mathcal V_{j,N,T}(t)/v_{2,N,T},
 \qquad \nu_j(\sigma_T)=v_{j,N,T}/v_{2,N,T}.
 \tag{23}
\]

W's microscopic proof works uniformly on the present complex
rectangle. To spell out the point at the origin, substitute \(t=z/N\)
in (22), divide the \(j\)-th term by \(N^{j-2}\), and compare on
nested fixed \(z\)-disks. The limiting operation is
\((C^{-1}-1)[F(z)-F(0)]/z\). The error numerator vanishes exactly
at zero and is \(O(N^{-1})\) on a larger disk; Cauchy's divided
difference makes its quotient \(O(N^{-1})\) on the next disk.
There are only \(p\) such operations. Thus
\[
 \nu_r=N^p\frac{[a_0^{\rm lin}(C^{-1}-1)]^p}{p!}(1+O(N^{-1})).
 \tag{24}
\]
It is a holomorphic unit. The same finite recursion, split into
\(|t|\le1/N\) and \(|t|\ge1/N\), proves
\[
 |\mathfrak G_r(t)|\le C_r(1+e^{N\Re\phi(t;C)}).
 \tag{25}
\]
On the second region each division costs at most \(N\), canceled
by (24), and \(\exp N[\phi(Qt)-\phi(t)]\) is bounded. On the first,
the microscopic divided-difference estimate applies. This proof
uses complex \(C\) directly.

On compact growing sectors the same recursion gives the actual unit
\[
 \mathfrak G_r(t)
   =N^{-p}e^{N\phi(t;C)}A_r^\partial(t;C)(1+O(N^{-1})),\quad
 A_r^\partial=\frac{p!A_G(t;C)}{[a_0^{\rm lin}(C^{-1}-1)]^p}
                  \left(\frac{C^{-1}-Y_B(t;C)}t\right)^p .
 \tag{26}
\]
The retained vacuum terms in (22) have polynomial size and are
exponentially smaller only on that sector.

The exact continued coherent boundary is now
\[
 \mathfrak C_{r,N}(\sigma;\xi)
  =\operatorname{CT}_t\,\mathfrak G_r(\sigma;t)
                         \mathfrak B_{s,N}(\xi/t;\tau).
 \tag{27}
\]
This is a finite coefficient extraction because (10) is finite.
At every physical node it is exactly B's complete coherent boundary,
including its true binomial weights and all total-degree caps.

Equations (20),(25),(26) pay the same original outer circle as B.
Set \(F(t)=\phi(t;C)+S_B(\xi/t;\tau)\), and let \(t_*\) be its
critical point near \(a_*/a_0^{\rm lin}\). Uniformly in the bundle,
\[
 \Psi=F(t_*)=2a_*+O(a_*^2)+O(\epsilon a_*),\qquad
 \mathcal H=D_t^2F(t_*)=2a_*+O(a_*^2)+O(\epsilon a_*).
 \tag{28}
\]
On the complete circle \(t=t_*e^{i\theta}\) the combined phase loses
\([2\Re a_*-O(|a_*|^2+\epsilon|a_*|)](1-\cos\theta)\).
The separate vacuum envelope in (25) has maximum at most
\(|a_*|+O(|a_*|^2+\epsilon|a_*|)\). Hence the strict gap
\(2\cos\theta_0-1>0\) pays that entire competing contribution.
The central circle coefficient is one, with the Gaussian root
continued from positive \(a_*\). Consequently
\[
 \mathfrak C_{r,N}
 =N^{-p-1/2}e^{N\Psi(\xi;C,\tau)}
     B_\partial(\xi;C,\tau)(1+O(N^{-1})),
 \quad
 B_\partial=(2\pi\mathcal H)^{-1/2}A_r^\partial(t_*;C)A_B(\xi/t_*;\tau).
 \tag{29}
\]
The error is holomorphic on a larger bundle. This is an actual
estimate of (27), not a continued physical-node error.

Before pulling back (7), keep physical \(\xi\) fixed and set
\[
 \psi(\xi;\sigma)=\Psi(\xi;e^{-c_0\sigma},\sigma),\qquad
 B_0(\xi;\sigma)=B_\partial(\xi;C,\sigma)
                    e^{-\partial_\tau\Psi(\xi;C,\sigma)} .
 \tag{30}
\]
The derivative fixes \(C,\xi\). This retains the exact
\(\tau=\sigma-\epsilon\) correction. The boundary logarithm of
\(N^{p+1/2}\mathfrak C_{r,N}\) is
\(\psi+\epsilon\log B_0+O(\epsilon^2)\), uniformly on the bundle.

## 4. Canonical low-log continuation without off-grid integrability

Continue the coefficients of K's exact weighted suffix rows with
\(T=N\sigma-1\). This is unambiguous: the ordered clock arcs have
\(Q^{tT}=e^{c_0t(\sigma-\epsilon)}\), and all last-head coefficients
are explicit functions of this parameter and of the integer low
indices. In particular the binomial generators remain the expressions
\[
 \widehat E=h z^{-1}D\int_0^1e^{c_0t}Q^{-tD}dt,\qquad
 \widehat F=-h z(d-D)\int_0^1e^{ht}Q^{tD}dt,\quad h=c_0/N.
 \tag{31}
\]
After dehomogenization \(D_r=N\sigma-1-\sum_{i<r}D_i\).
We use these as analytic coefficient operators. We do not identify
them with a finite physical head at noninteger last occupation.

For the conjugated logarithmic equations in K, the new degree-\(n\)
coefficient \(v_\gamma\) has diagonal
\[
       c_iN(1-Q^{\gamma_i})(CQ^n-1),\qquad n=|\gamma|.
 \tag{32}
\]
Choose \(k_N=\lfloor\delta N\rfloor\) with \(\delta\) small. Uniformly
on the buffered rectangle,
\[
 |CQ^n-1|\ge c,\qquad
 |c_iN(1-Q^{\gamma_i})(CQ^n-1)|\ge c\gamma_i,
 \quad n\le k_N .
 \tag{33}
\]
The angle of \(C Q^n\) stays away from one, regardless of its
bounded positive modulus.

For each \(\gamma\ne0\), choose an index \(i(\gamma)\) where
\(\gamma_i\) is maximal, using a fixed tie rule. Define the new
coefficient by that one conjugated logarithmic equation, initialized
by the exact boundary (27). All other terms have smaller output
degree. This defines a polynomial \(V_N^{[k]}\) in the output
variables, whose coefficients are holomorphic in \(\sigma,\eta\).
At every physical node it is the exact low logarithm of
\(N^{p+1/2}U_{N,T}\), because there all the original rows hold.

The choice is made in the logarithmic equations themselves.
We do not first solve one linear kernel path and then assume that
its logarithm solves the other finite rows. Nor does finite nodal
agreement prove off-grid compatibility of all the continued rows.
No such finite compatibility is required here.

For completeness the analytic bounds are uniform on the strip.
The inverse (32) is at most \(C s/n\) for the selected index.
Every continued suffix operator is a finite compact-cube integral
of bounded analytic coefficients times
\(N^{-|\nu|}\partial_\xi^\nu f(\Phi_{\epsilon,t}\xi)\),
\(|\nu|\le2\), where \(\Phi_{\epsilon,t}\) is an \(O(\epsilon)\)
clock displacement. In the bundle coordinates it is still an
analytic \(O(\epsilon)\) displacement on buffered compact domains.
K's positive padding
\(\varphi_\epsilon(y)=e^{L\epsilon}(1+y)-1\) therefore applies.
In particular
\(\epsilon F''(y)\preccurlyeq C F'(\varphi_\epsilon(y))\)
for positive majorants. Each whole row application consumes one
padding step, and products obey
\(\max(n_j+1)\le\sum n_j+1\).
Choose \(\delta\) so that all padded domains remain buffered.

After enlarging constants for the complex parameter set and the
factor \(s\), K's positive first-order majorant is unchanged:
its right side is analytic in \(U,U_y,zU_z\), its dependence on
the unknown \(U_z\) is \(O(z)\), and its initial datum is the
bounded boundary logarithm from (29),(30). Solving for \(U_z\)
and using its analytic characteristic ODE gives a fixed analytic
radius. The same proof with a linearized row bounds errors with
\(O(\epsilon^j)\) forcing and initial data by \(O(\epsilon^j)\),
for \(j=1,2\). All constants are uniform on the buffered complex
bundle. Thus
\[
 |[\rho^\gamma]V_N^{[k]}|\le C R^{-|\gamma|},\qquad
 |V_N^{[k]}|\le C
 \tag{34}
\]
there. This is a finite low-band estimate, not an assumption of
analytic integrability.

The selected limiting and first transport recursions define analytic
functions \(S(\rho,\xi;\sigma)\), \(\alpha(\rho,\xi;\sigma)\), with
boundary \(\psi,\log B_0\). Their compatibility with the remaining
principal and transport rows has a separate proof. For real
\(\sigma\) in the interval, take physical sequences
\((T_N+1)/N\to\sigma\). Uniform low coefficient bounds and the
selected recursion give these same limits from K's actual kernel.
Every remaining row therefore vanishes at each real \(\sigma\).
Its coefficients are holomorphic in \(\sigma\) on the connected
rectangle, so the identity theorem makes each limiting row vanish
throughout it. Uniform analytic bounds sum these coefficient
identities. This argument applies to the first transport as well;
it does not assert finite off-grid compatibility.

Substituting \(S+\epsilon\alpha\) into the selected exact log rows
leaves \(O(\epsilon^2)\) residual, including the short-arc second
derivatives and physical half-shifts. The boundary error has that
order by (30). The linear majorant just proved gives
\[
 V_N^{[k]}=S+\epsilon\alpha+O(\epsilon^2)+O(e^{-cN})
 \tag{35}
\]
on a smaller output disk. Pull back (7) to obtain
\(\mathscr S,\log\mathscr A\). All \(\sigma\)-derivatives of this
pullback retain its explicit input-coordinate derivative.

## 5. Entire physical cap and exact bundle cardinal correction

Put
\[
 \widehat U_N(\sigma;\rho,\eta)
       =N^{-p-1/2}\exp[N V_N^{[k]}(\sigma;\rho,\eta)].
 \tag{36}
\]
At a physical node it agrees with the actual (2) through output
degree \(k_N\), including the entire binomial input. K's actual
matrix bound, its vacuum lower bound, and the finite binomial
coefficients give \(e^{C_4N}\) bounds for both functions on a fixed
comparison output polydisk, uniformly over the real nodes and
the buffered input bundle. Cauchy's full tail estimate is
\[
 |U_{N,T}(\rho,\xi(\sigma_T,\eta))-\widehat U_N(\sigma_T;\rho,\eta)|
 \le C(k_N+1)^{s-1}e^{C_5N}
             \frac{(r_0/R_0)^{k_N+1}}{(1-r_0/R_0)^s}.
 \tag{37}
\]
The reciprocal surrogate costs only \(N^{p+1/2}e^{C_6N}\) by
(34). After the input bundle, \(\delta\), and \(R_0\) have been
fixed, shrinking the output radius makes the relative nodal error
at most \(e^{-\gamma N}\) for any chosen \(\gamma\).
Every high physical coefficient is retained in this comparison.

Now define the actual interpolant
\[
 \boxed{\begin{split}
 \mathfrak U_N(\sigma;\rho,\eta)=\widehat U_N(\sigma;\rho,\eta)
  +\sum_{T\in\mathcal T_N}
  \bigl[U_{N,T}(\rho,\xi(\sigma_T,\eta))
             -\widehat U_N(\sigma_T;\rho,\eta)\bigr]\,
                   \operatorname{sinc}(N\sigma-T-1).
 \end{split}}
 \tag{38}
\]
All brackets keep the same bundle coordinates \(\eta\), not the
target physical coordinate \(\xi(\sigma,\eta)\). This distinction
keeps every nodal error inside its proved growing sector.
The finite formula proves (8) exactly.

The sinc factors are bounded by \(e^{\pi N|\Im\sigma|}\).
By (34), the ratio of a nodal surrogate to the target surrogate
costs at most \(e^{C_7N}\), including the nonzero boundary phase.
Thus
\[
 \left|\mathfrak U_N/\widehat U_N-1\right|
     \le C N e^{-N(\gamma-\pi H-C_7)} .
 \tag{39}
\]
Choose \(\gamma>L+\pi H+C_7+1\) on the buffered rectangle, using
(37). This proves the first estimate in (9); (35) proves the
second. Cauchy on larger domains proves every fixed derivative.
No nodal-only asymptotic error was analytically continued.

## 6. Mixed rank, original scalars, and the exact degree contour

The full rank calculation in K continues with the initialized
phase, not by scalar functional calculus. Its axis identities
are analytic in \(C,\sigma\). With
\(P=\sum p_i=t\phi'(t)\), their radial sum has the expansion
\[
 \sum_i S_{\rho_i}(0,\xi)
 =\frac2{c_0}+\frac{C+1}{2(C-1)}P+O(P^2).
 \tag{40}
\]
The prefix-product differences give rank \(s-1\) at fixed \(P\).
The coefficient in (40) is nonzero uniformly on the rectangle.
The input map has
\[
 \det\frac{\partial\xi}{\partial p}
       =2\left(\frac{P}{a_0^{\rm lin}b_\sigma}\right)^s(1+O(P)).
 \tag{41}
\]
These identities hold throughout the strip by the limiting-row
argument of §4. For sufficiently small nonzero balanced inputs,
they prove \(\det S_{\rho\xi}\ne0\); the invertible bundle map (7)
also gives \(\det\mathscr S_{\rho\eta}\ne0\).
Shrinking the output domain preserves this determinant.

I supplies the marked exact factorial \(\widehat F_N\), with
\(\widehat F_N(T)=f_T\). Keep the following scalar factors exactly:
\[
 \begin{split}
 \mathfrak a_{00,N}^{(r)}(\sigma)
   &=(-1)^d(x^r Q C)^d\,\widehat F_N(N\sigma-1)^2\,\nu_r(\sigma),\\
 \mathfrak b_N(\sigma)
   &=\frac{\Gamma(N)}
        {\Gamma(N\sigma)\Gamma(N(1-\sigma)+1)},\\
 \mathfrak P_N(\sigma;\rho,\eta)
   &=\mathfrak a_{00,N}^{(r)}e^{(N\sigma-1)\ell}
                        \mathfrak b_N\,\mathfrak U_N,\qquad
                  \ell=\Log(w_rz_r).
 \end{split}
 \tag{42}
\]
They are holomorphic units on the buffered strip for large \(N\).
At every node (23),(42) recover (3) literally, at its specified
input \(\xi(\sigma_T,\eta)\). The width normalization (24), the
factorial extensive phase, the actual \(c_i=x^{r-i}\), and the
\(d=N-1\) binomial correction remain. Changing \(\ell\) by \(2\pi i j\)
multiplies the interpolant by \(e^{2\pi i jN\sigma}\), a retained
contour character equal to one at physical nodes.

For a holomorphic spectator with specified nodal values, the finite
degree sum at fixed bundle coordinates has the exact representation
\[
 \sum_{T\in\mathcal T_N}\mathfrak P_N(\sigma_T;\rho,\eta)h_N(\sigma_T)
 =\frac1{2\pi i}\int_{\Gamma_N}
       \frac{c_0N}{e^{c_0N\sigma}-1}
                \mathfrak P_N(\sigma;\rho,\eta)h_N(\sigma)\,d\sigma .
 \tag{43}
\]
The contour surrounds precisely these nodes, inside the buffered
strip. Each pole has residue one. Half-grid vertical sides, both
horizontal pieces, and all external connectors retain their
orientations. No bound on an unknown spectator follows from (9).

For an original degree sum with physical \(\xi\) fixed, the required
pullback is explicit:
\[
 a_*(\sigma)^2=a_0^{\rm lin}b_\sigma\sum_i\xi_i,\qquad
 \vartheta_i=\xi_i/\sum_j\xi_j .
 \tag{44}
\]
Equations (38),(42),(43) then represent that fixed-input nodal data
only on a contour whose marked lift (44) stays in the proved bundle.
For a tall strip this condition can fail. A degree-dependent change
of the exterior coherent contour or frame is not supplied here.
In particular a fixed-bundle sum is not silently identified with
a fixed-external-variable word or trace.

This theorem pays a source-exact local complex-degree continuation
of the complete all-width coherent factor, with all finite caps,
an actual amplitude and its initialized mixed rank. It does not
estimate its exterior braid, turnover, inverse-Cartan coupon,
meridian normal, excluded degree blocks or closed source. It does
not establish geometric-chart membership or a contributing
geometric cycle.

## Complete proof directs and protocol

* **I:** notes/research_actual_gauss_complex_degree_interpolation.md,
  528 lines, SHA256
  86899fd343dd288979353f4f74c0ac512d39a865898a37939ebbf9a26fcc8318.
* **W:** notes/research_fixed_width_gauss_boundary_branches.md,
  427 lines, SHA256
  cdcb82d2bd48948ff45baaec65a71f639607e10a9bc12acff344e34ae972d404.
* **B:** notes/research_fixed_width_gauss_coherent_boundary.md,
  383 lines, SHA256
  03e0969c7b7c80d80b6cdb728661f125c15fee33b806dbd81f100bbb89b417c4.
* **K:** notes/research_fixed_width_gauss_coherent_sector_kernel.md,
  599 lines, SHA256
  725f11b37640abd36b89ae0f1f6f47464ed6b588ccc8b7709d32e62a502045ec.

Only written mathematics and text operations are used. All four
complete directs were freshly read nontruncated in this author
sequence, and every used implication was checked. The entire
matching final was freshly reread nontruncated and all five hashes
were renewed. Independent matching review and parent adoption
remain separate.
