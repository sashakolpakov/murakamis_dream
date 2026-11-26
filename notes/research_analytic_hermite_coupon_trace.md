# Analytic Hermite coupons on the original positive coefficient circle

Private written proof, 17 November 2026.

The fixed-degree restriction on inserted coupons can be removed for
functions holomorphic on the entire coefficient disk. Their full
Hermite interpolants have degree as large as \(N-1\), but their
original trace is governed by the value of the analytic function at
the actual coefficient saddle, with an explicit analytic-norm error.
Slowly varying exponential coupons have a relative estimate and
remain in this class under any fixed number of ordinary products.

A function given only on a slit or near the saddle is different:
its poles, cut banks, and endpoint currents remain in an exact
formula below. In particular this theorem does not discard the
original crossing's cut at \(C\ge2\), and does not prove closure
under the physical turn.

## 1. Actual product, coefficient circle, and full Hermite interpolation

Use the original conventions
\[
 N\ge3,\quad D=N-1,\quad J=\lfloor D/2\rfloor,\quad
 \eta=(-1)^D,\quad c_a=2\cos((2a+1)\pi/N),
\]
\[
 P_N(C)=2T_N(C/2)+2,\qquad
 \phi_N(f)=\eta N^2[C^D]\operatorname{rem}_{P_N}f,\qquad
 F_j(C)=K_N(c_j,C).
 \tag{1}
\]
Fix \(m\ge3\) and \(\varepsilon>0\). Consider all physical
tuples \(0\le j_i\le J\) with
\[
 s=\sum_i j_i,\qquad k=s-D\ge\varepsilon N,\qquad
 f_N(C)=\prod_{i=1}^mF_{j_i}(C),\qquad
 \Gamma_N=\phi_N(f_N)>0.
 \tag{2}
\]
Every trace below includes canonical reduction and all repeated-root
normals, even when the ordinary degree of \(f_N\) exceeds \(D\).

The positive coefficient source supplies positive Jacobi eigenvalues
\(r_{j,b}>0\), \(d_a=c_0-c_a\ge0\), and
\[
 \mathfrak a_N=\prod_{i,b}r_{j_i,b}^{-1},\qquad
 H_N(x)=
 \frac{\prod_{i,b}(1+r_{j_i,b}x)}
      {\prod_{a=0}^{N-1}(1-d_ax)},\qquad
 \Gamma_N=N^2\mathfrak a_N[x^k]H_N .
 \tag{3}
\]
Let \(\rho_N\) be its unique mean-\(k\) saddle. Uniformly in
(2), for sufficiently large \(N\),
\[
 0<a\le\rho_N\le b<1/4,\qquad cN\le V_N\le CN,
 \tag{4}
\]
where \(V_N\) is the exact tilted variance. Define
\[
 \zeta_N=c_0-\rho_N^{-1},\qquad
 C_N(\theta)=c_0-\rho_N^{-1}e^{-i\theta},
                      \quad-\pi\le\theta\le\pi .
 \tag{5}
\]
The circle in (5) contains every physical root strictly inside,
since \(d_a<4<\rho_N^{-1}\). All these circles and their interiors
lie in one fixed disk centered at \(2\).

Choose a closed disk \(\Omega_0=\{|C-2|\le R_0\}\) with
\(R_0>1/a+2\), and a larger open disk \(\Omega_1\) with a
fixed positive buffer around \(\Omega_0\). Every coefficient
circle has a fixed positive distance from \(\partial\Omega_0\);
the Cauchy estimates below use this interior margin and norms
on \(\Omega_0\), not an uncontrolled norm on \(\Omega_1\).
For a function
\(a_N\) holomorphic on \(\Omega_1\), let \(q_N\) be its unique
polynomial of degree at most \(D\) matching the following data:
\[
 q_N(c)=a_N(c),\quad q_N'(c)=a_N'(c)
               \quad(c\text{ a double physical root}),
 \tag{6}
\]
and only the value at the odd simple root. This is ordinary
confluent interpolation with exactly \(N\) conditions.
Equivalently, \((q_N-a_N)/P_N\) is holomorphic throughout
\(\Omega_1\). The polynomial \(q_N\) is an actual coupon in the
original algebra, with its original spectral normals.

## 2. Exact source integral and the degree-free estimate

Let \(S_{\rho_N}\) be the exact sum of independent Bernoulli and
geometric variables in the coefficient source, and put
\[
 \chi_N(\theta)=
 e^{-ik\theta}\frac{H_N(\rho_Ne^{i\theta})}{H_N(\rho_N)},
 \qquad
 p_N=\mathbb P(S_{\rho_N}=k).
 \tag{7}
\]
The same source proves, uniformly,
\[
 |\chi_N(\theta)|\le e^{-cN\sin^2(\theta/2)},\qquad
 p_N=(2\pi V_N)^{-1/2}(1+O(N^{-1})),
 \tag{8}
\]
\[
 \mathbb P(S_{\rho_N}=k+h)/p_N=1+O_h(N^{-1})
                         \quad(h\text{ fixed}).
 \tag{9}
\]
These are statements about this actual finite product, not a
probability model replacing the original source.

**Theorem 1.** For the full Hermite coupon (6),
\[
 \boxed{\quad
 \frac{\phi_N(q_Nf_N)}{\Gamma_N}
 =\frac1{2\pi p_N}\int_{-\pi}^{\pi}
      \chi_N(\theta)a_N(C_N(\theta))\,d\theta
 =a_N(\zeta_N)+O(N^{-1}M_N),
 \quad}
 \tag{10}
\]
where \(M_N=\sup_{\Omega_0}|a_N|\). The constant is uniform
in (2) and \(a_N\); no bound on the degree or on the polynomial
coefficient norm of \(q_N\) is imposed.

**Proof of the exact formula.** On the positively oriented spectral
circle \(|C-c_0|=\rho_N^{-1}\), the original trace is
\[
 \phi_N(q_Nf_N)=\frac{\eta N^2}{2\pi i}
               \oint \frac{q_N(C)f_N(C)}{P_N(C)}\,dC.
 \tag{11}
\]
The residues are precisely the full physical trace. Replacing
\(q_N\) by \(a_N\) changes the integrand by a holomorphic
function: the quotient in (6) times the ordinary polynomial
\(f_N\). Its contour integral is exactly zero.

Set \(z=c_0-C\), then \(x=1/z\). The spectral circle is
positive in \(z\) and negative in \(x\); this reversal and
the sign \(P_N(c_0-z)=(-1)^N\prod_a(z-d_a)\), together
with \(\eta=(-1)^{N-1}\), give
\[
 \phi_N(q_Nf_N)=
 \frac{N^2\mathfrak a_N}{2\pi i}
       \oint_{|x|=\rho_N}^{+}
       H_N(x)a_N(c_0-x^{-1})x^{-k-1}\,dx .
 \tag{12}
\]
Only values on this circle are used; no analytic extension of
\(a_N(c_0-x^{-1})\) to \(x=0\) is asserted.
Divide by the exact uninserted coefficient (3) to obtain (10).

**Proof of the error.** A useful consequence of (8)--(9) is
\[
 \frac1{2\pi p_N}\int_{-\pi}^{\pi}\chi_N(\theta)
                  \sin\theta\,d\theta=O(N^{-1}),
 \qquad
 \frac1{p_N}\int_{-\pi}^{\pi}
          |\chi_N(\theta)|\theta^2\,d\theta=O(N^{-1}).
 \tag{13}
\]
The first identity is the difference of the probabilities at
\(k-1\) and \(k+1\), divided by \(2ip_N\).
The second follows from the Gaussian bound (8) and
\(p_N\asymp N^{-1/2}\).
On a fixed small arc put \(A_N(\theta)=a_N(C_N(\theta))\).
Cauchy's estimate on the circle's fixed buffer inside \(\Omega_0\) gives
\(|A_N'|+|A_N''|\le CM_N\), so
\[
 A_N(\theta)=A_N(0)+A_N'(0)\sin\theta+O(M_N\theta^2).
 \tag{14}
\]
Outside this arc, (8) is exponentially small, and
\(|A_N|\le M_N\). Equations (13)--(14) prove (10).
The polynomial quotient was canceled exactly before any
absolute estimate. \(\square\)

For later use, the same proof gives a local version which
does not require a holomorphic function on the whole disk.
Suppose \(A_N(\theta)\) is bounded and piecewise defined on
the outer circle, has one \(C^2\) branch on \(|\theta|\le\delta\)
for a fixed \(0<\delta<\pi\),
and let
\[
 M_{\rm out}=\sup_{[-\pi,\pi]}|A_N|,\quad
 M_1=|A_N'(0)|,\quad
 M_2=\sup_{|\theta|\le\delta}|A_N''(\theta)|.
\]
Then
\[
 \left|
 \frac1{2\pi p_N}\int\chi_N A_N-A_N(0)
 \right|
 \le C_\delta\left\{
 \frac{M_1+M_2}{N}
       +\sqrt N\,e^{-c_\delta N}M_{\rm out}\right\}.
 \tag{15}
\]
Subtract \(A_N(0)+A_N'(0)\sin\theta\) to prove this.
The tail containing \(M_1\) is absorbed into \(CM_1/N\).
Formula (15) estimates only the outer integral; the exact
source currents for a slit function are retained in section 4.

## 3. Slowly varying actual coupons and ordinary composition

**Theorem 2.** Suppose \(b_N\) is holomorphic on \(\Omega_1\)
and
\[
 L_N=1+\sup_{\Omega_0}|b_N|=o(\sqrt N),\qquad
 a_N=e^{b_N}.
 \tag{16}
\]
For its full Hermite coupon \(q_N\), uniformly in (2),
\[
 \boxed{\quad
 \frac{\phi_N(q_Nf_N)}
       {e^{b_N(\zeta_N)}\Gamma_N}
          =1+O(L_N^2/N).
 \quad}
 \tag{17}
\]
In particular the original observed trace is nonzero for large \(N\).
It has the same exponential rate as \(\Gamma_N\), since
\(|b_N(\zeta_N)|=o(N)\).

**Proof.** Fixed-buffer Cauchy estimates give, on a small
fixed angular arc,
\[
 B_N(\theta):=b_N(C_N(\theta))-b_N(\zeta_N),\quad
 |B_N(\theta)|\le CL_N|\theta|,\quad
 |B_N''(\theta)|\le CL_N .
\]
Taylor's formula for the exponential implies
\[
 \left|e^{B_N(\theta)}-1-B_N'(0)\sin\theta\right|
 \le C(L_N+L_N^2)\theta^2 e^{CL_N|\theta|}.
 \tag{18}
\]
Its normalized integral against (8) is \(O(L_N^2/N)\).
Indeed completing the square in
\(-cN\theta^2+CL_N|\theta|\) gives the bound
\[
 \frac1{p_N}\int\theta^2 e^{-cN\theta^2+CL_N|\theta|}
                \,d\theta
 \le \frac{C}{N}(1+L_N^2/N)e^{CL_N^2/N}=O(N^{-1}).
 \tag{19}
\]
The linear term in (18) is \(O(L_N/N)\) by (13).
On the complementary arc, the normalized integral is
at most \(C\sqrt N e^{-cN+2L_N}\), which is negligible.
Apply the exact formula (10) to obtain (17). \(\square\)

The hypothesis is on an analytic representative, not on the
coefficients of its degree-\(D\) interpolant. For example
\(b_N=\lambda_N b\), with \(b\) fixed holomorphic and
\(\lambda_N=o(\sqrt N)\), is allowed.

This class has an exact ordinary composition law. If
\(q_{N,1},\ldots,q_{N,r}\) interpolate \(e^{b_{N,1}},\ldots,
e^{b_{N,r}}\), then their canonical product interpolates
\(e^{\sum_\nu b_{N,\nu}}\), including every mixed product-rule
term at the repeated roots. For fixed \(r\), condition (16)
is preserved. Therefore (17) applies to this canonical product,
with its actual leading coefficient
\(\exp(\sum_\nu b_{N,\nu}(\zeta_N))\).
No physical turn or additional unspecified closing map occurs
in this composition assertion.

For three rows on a strict macroscopic compact, the common
characteristic theorem further identifies
\[
 \zeta_N=2-4/L(\mathbf j/N)+O(N^{-1}).
 \tag{20}
\]
Apply its exact observed-\(C\) asymptotic and the coefficient
source's observed-\(C\) formula to the same trace to prove (20).
For bounded analytic coupons this replacement changes (10)
by \(O(M_N/N)\); under (16) it changes the relative leading
factor in (17) by \(1+O(L_N/N)\).
It supplies no global continuation of the selected branch.

## 4. Poles, cuts, and the canonical remainder

There is an exact version retaining every obstruction to the disk
hypothesis. Let \(a_N\) be a selected holomorphic branch near all
physical roots, with its full jets defining \(q_N\) as in (6).
Suppose it continues to the interior of the coefficient circle
after removing specified poles and cuts. Cut banks and endpoint
arcs are oriented as inner boundaries of that punctured domain,
so that the domain lies on their left. Assume these contours
avoid the physical roots and their limiting integrals exist;
otherwise keep the finite excision contours themselves.

Write \(\mathscr B_N\) for the sum of the oriented inner
cut-bank and endpoint integrals, and let the indicated residues
be the isolated nonphysical poles. Then, exactly,
\[
 \boxed{\quad
 \phi_N(q_Nf_N)=
 \frac{\eta N^2}{2\pi i}\oint_{\rm outer}
                \frac{a_N f_N}{P_N}\,dC+\mathscr C_N,
 \quad}
 \tag{21}
\]
\[
 \mathscr C_N=
 \frac{\eta N^2}{2\pi i}\mathscr B_N
       -\eta N^2
          \sum_{\rm nonphysical\ poles}
                   \operatorname{Res}\frac{a_Nf_N}{P_N}.
 \tag{22}
\]
This is the residue theorem on the punctured disk: its physical
residues equal those of the full Hermite coupon. No external
coefficient or first normal has been substituted.

For a real slit \([u,v]\) directed toward the outer boundary,
the two banks contribute
\[
       \int_u^v
          \frac{(a_{N,+}-a_{N,-})(C)f_N(C)}{P_N(C)}\,dC
 \tag{23}
\]
with this orientation. Endpoint arcs remain unless their limits
are proved to vanish. There is no branch reset on the outer
circle; its successive arcs use the prescribed continued branch.

On a cut-free saddle arc, (15) gives the exact insertion criterion
\[
 \frac{\phi_N(q_Nf_N)}{\Gamma_N}
 =a_N(\zeta_N)
   +O_\delta\!\left(\frac{M_1+M_2}{N}
          +\sqrt N e^{-c_\delta N}M_{\rm out}\right)
   +\frac{\mathscr C_N}{\Gamma_N}.
 \tag{24}
\]
In the disk-holomorphic case the last term is exactly zero,
which is the substantive simplification in Theorems 1--2.
For a general slit representative it is an original source term,
not an interpolation error. A nonzero leading observation follows
only if the displayed errors and the actual current are small
relative to \(a_N(\zeta_N)\).

The original Gaussian representative of a fixed crossing has a
spectral cut at \(C\ge2\). Its canonical polynomial is entire,
but replacing that polynomial on the circle by one selected
Gaussian branch falls under (21)--(24), not the disk theorem.
No bound on its cut current, outer-circle growth, or subsequent
physical turn is supplied here.

## Complete direct sources

Both complete direct texts were read at the following pins, with
their used implications checked:

* [Positive physical-product coefficient saddle](research_physical_products_positive_coefficient_saddle.md),
  SHA256 e82fea1f786383a1cfe4529573805adf5fc75a77e433e38ea609024bdeed7824:
  the exact coefficient source, uniform circle/variance,
  characteristic-function decay, and adjacent probabilities.
* [Original common Jacobi characteristic](research_triple_row_common_characteristic.md),
  SHA256 8f1077d9d0db4797576fe039aff6621d5aa088a60fa309c661995703b23d280c:
  the actual observed-\(C\) asymptotic used in (20).

Only written mathematics, source reads, and metadata hashes were used.
No mathematical programs, tests, numerics, or builds were run.
Frozen notes and public manuscripts were not edited.
