# Finite quantum sums at small Fourier charges

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

This note proves a nonzero leading asymptotic for a family of finite
quantum sums. Start with the original edge kernels and traces, and
insert the Chebyshev factor \(T_{N-j_v}(-w_v/2)\) at each traced
vertex. We call this inserted factor a coupon. Its Fourier charge is
\(\chi_v=j_v/N\); at \(j_v=N\), the factor is \(T_0=1\), so the
insertion disappears.

For every fixed finite graph, with no isolated traced vertex, and
arbitrary fixed integer crossing powers, the sum has a unique leading
critical point when all charges belong to
\([1/4000,1/2000]\). Its coefficient is explicit and nonzero for both
parities of \(N\). Loops and repeated edges are allowed. For paths
whose powers are positive and at least three, the same conclusion holds
on the larger interval \([1/640,1/320]\).

Sections 1–6 prove the positive-path result. Section 7 allows negative
and zero powers, and Section 8 proves the graph extension. These are
statements about the specified finite sums: an arbitrary graph is not
asserted to represent a knot invariant. The proof initializes charge
continuation near the complete point; it does not continue the
nonzero coefficient to charge one.

## 1. The finite source

Let \(\Gamma=(V,E)\) be a nontrivial finite path with the original
same-index edge kernels. Choose a nonempty set \(I\subseteq V\) of
selected vertices. Every unselected vertex has complete angle zero.
Let \(m=|I|\), \(e=|E|\), and let \(d_v\in\{1,2\}\) be the original
degree of a selected vertex, including its incidences to complete
vertices. Fix integer powers \(n_v\ge3\).

At level \(N\), use the original kernel, crossing, and full Hermite
trace
\[
 \begin{split}
 K_N(t,u)&=\sum_{r=0}^{N-1}e_r(-2\cos t)e_r(-2\cos u),\\
 e_r(w)&=S_r^{-2}\prod_{a<r}
              \bigl(2\cos((2a+1)\pi/N)-w\bigr),\qquad
 S_r=\prod_{a=1}^r2\sin(\pi a/N),\\
 \phi_N(f)&=(-1)^{N-1}N^2[w^{N-1}]
                      \operatorname{rem}_{2T_N(w/2)+2}f.
 \end{split}
 \tag{1}
\]
Here \(T_r\) denotes the ordinary Chebyshev polynomial.
Set
\[
 \chi_0=\frac1{320},\qquad
 j_v\in\mathbb Z,\qquad
 \chi_v=\frac{j_v}{N}\in[\chi_0/2,\chi_0].
 \tag{2}
\]
Define the actual finite source
\[
 Z_{\Gamma,I,N}(\mathbf j)=
 \left(\prod_{v\in I}\phi_N^{(w_v)}\right)
 \left[
   \prod_{v\in I}R(w_v)^{n_v}T_{N-j_v}(-w_v/2)
   \prod_{\{v,w\}\in E}K_N(t_v,t_w)
 \right],\qquad w_v=-2\cos t_v.
 \tag{3}
\]
Powers of \(R\) and all products in a traced variable are taken in
the original quotient with its first normals. No free boundary
polynomial is reduced. Formula (3) fixes the source independently
of an asymptotic model.

The original calibrated edge phase satisfies
\[
 \psi(0,0)=M_\infty=\frac{4G}{\pi},\qquad
 \psi_t(t,u)=-\frac1\pi
       \operatorname{arsinh}\bigl(\tan(t/2)\cos(u/2)\bigr).
 \]
All branches continue from the complete edge. Put
\[
 \Phi_{\boldsymbol\chi}(\mathbf t)
 =\sum_{\{v,w\}\in E}\psi(t_v,t_w)
   +\sum_{v\in I}\left(\frac{in_vt_v^2}{4\pi}
                                             -i\chi_vt_v\right).
 \tag{4}
\]
Unselected angles in (4) remain zero.

## 2. Uniform geometry on the small charge cube

The following estimates also apply when some selected charges are zero.
They are uniform in the number of vertices and the fixed powers.

**Lemma 1.** For \(\boldsymbol\chi\in[0,\chi_0]^I\), equation (4)
has a unique critical point in the small box constructed below.
Its original edge shapes are positive, and it satisfies
\[
 |t_v^*|\le\frac{21}{10}\chi_v,\qquad
 0<H_v=-\Im t_v^*\le\frac32\chi_v
                  \quad(\chi_v>0),\qquad
 t_v^*=0\quad(\chi_v=0).
 \tag{5}
\]
If \(S\subseteq I\) and \(\boldsymbol\chi^S\) sets the charges
on \(S\) to zero, then, with
\(M(\boldsymbol\chi)=\Re\Phi_{\boldsymbol\chi}(\mathbf t^*)\),
\[
 0\le M(\boldsymbol\chi^S)-M(\boldsymbol\chi)
                  \le\frac34\sum_{v\in S}\chi_v^2.
 \tag{6}
\]

*Proof.* Set \(r=1/100\). On the polydisk \(|t_v|\le2r\),
define the holomorphic functions
\[
 C_v(\mathbf t)=
       2\sum_{w\sim v}
       \frac{\operatorname{arsinh}(\tan(t_v/2)\cos(t_w/2))}
                         {t_v}.
 \tag{7}
\]
The quotient has its removable value at \(t_v=0\). A complete
neighbor has \(t_w=0\). At the origin \(C_v=d_v\).

For \(|t|,|u|\le2r\), the elementary disk estimates
\[
 \begin{split}
 |\tan(t/2)-t/2|&\le |t|^3/16,\qquad
 |\tan(t/2)|\le(51/100)|t|,\\
 |\cos(u/2)-1|&\le |u|^2/7,\qquad |\cos(u/2)|\le101/100,\\
 |\operatorname{arsinh}z-z|&\le |z|^3/5\quad(|z|\le1/50)
 \end{split}
 \tag{8}
\]
follow by integrating the tangent derivative and the binomial series.
Their proofs are also given in
[the small-height calculation](research_pair_activation_small_height.md),
Section 2. Every argument of the inverse hyperbolic sine here is
smaller than \(1/50\). Consequently each summand in (7) differs
from one by at most
\[
 \left[\frac18+\frac25
                \left(\frac{51}{100}\frac{101}{100}\right)^3\right]
                    |t|^2+\frac{51}{350}|u|^2
 \le\frac13\max(|t|,|u|)^2 .
 \tag{9}
\]
The sum of the two rational coefficients is strictly less than
\(1/3\). Thus on \(|t_v|\le r\),
\[
 |C_v-d_v|\le\frac{d_vr^2}{3}\le\delta,\qquad
 \delta=\frac1{15000}.
 \tag{10}
\]
On the larger polydisk the bound is \(4d_vr^2/3\).
Cauchy's estimate, varying one coordinate by a circle of radius
\(r\), bounds each derivative on the smaller polydisk by
\(4d_vr/3\). There are at most three relevant coordinates, so
the absolute row sum of the derivative of \(C_v\) is at most \(8r\).

The stationary equations are precisely the fixed-point equations
\[
 t_v=\mathcal T_v(\mathbf t)
          =\frac{2\pi\chi_v}{n_v+iC_v(\mathbf t)}.
 \tag{11}
\]
Since \(n_v\ge3\), (10) gives
\[
 |\mathcal T_v|\le\frac{2\pi\chi_v}{3-\delta}
                         <\frac{21}{10}\chi_v<r,\qquad
 \|D\mathcal T\|_\infty
        \le\frac{2\pi\chi_0\,8r}{(3-\delta)^2}<\frac1{1000}.
 \tag{12}
\]
Banach's theorem constructs a unique small solution. The fixed point
depends analytically on the charges locally. At a real charge vector,
write \(C_v=A_v+iB_v\). Equations (10)--(11) give
\[
 \Re t_v=\frac{2\pi\chi_v(n_v-B_v)}
                       {(n_v-B_v)^2+A_v^2}>0,\qquad
 H_v=\frac{2\pi\chi_v A_v}
                       {(n_v-B_v)^2+A_v^2}
 \le\frac{2\pi(2+\delta)}{(3-\delta)^2}\chi_v
                         <\frac32\chi_v
 \tag{13}
\]
when \(\chi_v>0\). A zero charge forces \(t_v=0\).
The positivity assertion can be checked directly, without a global
existence theorem. For an edge put
\(a=\tan(t_v/2)\), \(b=\tan(t_w/2)\), and
\(q_e=\sqrt{1+a^2+b^2}\), continued from \(q_e=1\).
On the small box, \(|a|,|b|<1/100\), so
\(\Re q_e>99/100\) and
\(\sqrt{(\Re a)^2+(\Re b)^2}<1/50\).
The [original edge criterion](research_positive_edge_global_monotonicity.md),
Theorem 1, proves that all eight original shapes are positive.
The small branch is connected to completeness by its fixed-point
construction, so its logarithmic normalization is the original one.
When there is a complete outside end, uniqueness identifies this
point with the solution of the
[global fractional-charge theorem](research_positive_path_fractional_charge_cube.md).
When \(I=V\), only the directly constructed small-charge branch is
used here; the global cube theorem is not invoked in that scope.

The stationary derivative is
\(\partial M/\partial\chi_v=\Im t_v=-H_v\).
Lower the charges in \(S\), one at a time, keeping all others in the
same small cube. Integrating (13) gives (6).
\(\square\)

All constants in this proof use only \(\pi<22/7\) and exact
rational comparisons. The
[scalar checker](../experiments/check_small_charge_path_source.py)
and its [saved comparisons](../repro/results/research-small-charge-path-source.json)
record these bounds and the current and outer-row margins used
below. In particular
\[
 \Re t_v^*\le21/3200,\qquad
                  H_v\le3/640<1/200.
 \tag{14}
\]
On the compact box (2), each \(H_v\) also has a strictly positive
lower bound depending on its fixed \(n_v\). For example replace
\(A_v\) by \(d_v-\delta\) in the numerator of (13) and bound its
denominator above by \((n_v+\delta)^2+(d_v+\delta)^2\).

## 3. The exact coupon contour and every competing charge

Put \(\eta=(-1)^{N-1}\) and
\(C_{N,n}=\exp(\pi in(N-1)^2/(4N))\). Choose the largest physical
midpoint \(T_N\le T=19/20\). Thus
\(e^{iNT_N}=-\eta\), \(T_N\to T\), and \(T_N\ge94/100\)
at all sufficiently large levels.

For an even spectator \(f(t)\), insert the coupon
\(\cos((N-j)t)\) in the
[exact retained trace](research_exact_complete_trace_contour.md).
Its lower horizontal integral has prefactor \(iN^2C_{N,n}/\pi\)
and kernel
\[
 \begin{split}
 \frac{e^{-iNt}\cos((N-j)t)}
              {(1-\eta e^{-iNt})^2}
  =\frac12 e^{-i\chi Nt}
       \frac{1+e^{-2i(N-j)t}}{(1-\eta e^{-iNt})^2}.
 \end{split}
 \tag{15}
\]
On a lower line of fixed height \(H>0\), its quotient by
\(\tfrac12e^{-i\chi Nt}\) is \(1+O(e^{-cN})\), uniformly
for (2). This follows directly by bounding the two exponentials
in (15); one can take any smaller positive constant than
\(\min(H,2(1-\chi_0)H)\). Thus all other Fourier charges have
been estimated together, rather than deleted from the finite source.
The exact coefficient of the surviving term is \(1/2\).

The vertical term remains
\[
 \frac{\eta N^2 C_{N,n}}{\pi}
 \int_{-H}^{H}
  \frac{\sin(T_N+ih)f(T_N+ih)
        e^{inN(T_N+ih)^2/(4\pi)}
        \cos((N-j)(T_N+ih))}
       {4\cosh^2(Nh/2)}\,dh .
 \tag{16}
\]
Its kernel is bounded by
\[
 \frac{|\cos((N-j)(T_N+ih))|}
             {4\cosh^2(Nh/2)}
       \le e^{-j|h|}=e^{-N\chi|h|}.
 \tag{17}
\]
This includes \(h=0\). The upper and lower horizontal sides have
already been combined in the retained trace identity: its
integrand is odd before multiplication by the even residue kernel,
and the coupon is even. Their two reflected contributions are
equal with their contour orientations. The leading factor in (15)
is therefore part of one exact lower integral, not an unexamined
sum of leading terms whose coefficients might cancel.

## 4. Uniform estimates for all mixed vertical terms

The full kernel theorem
[on the thin rectangle](research_bare_kernel_thin_rectangle.md)
applies whenever
\[
             |\Re t|,|\Re u|\le1,\qquad
             |\Im t|,|\Im u|\le1/200.
 \]
It gives its nonzero holomorphic expansion and the upper bound
\[
 K_N(t,u)=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}(1+O(N^{-1})),
 \qquad |K_N(t,u)|\le CN^A e^{N\Re\psi(t,u)} .
 \tag{18}
\]
It retains all original Newton rows and all fixed ordinary normals.
On the larger classical box of heights at most \(1/3\), the
[edge Hessian calculation](research_path_mixed_trace_currents.md),
equations (4)--(5), gives
\[
 K_e=-2\pi\psi''(t,u),\qquad
                   \Re K_e\succeq\tfrac15 I,\qquad \|K_e\|<2.
 \tag{19}
\]

For a subset \(S\subseteq I\), take a vertical side at vertices
in \(S\), with \(t_v=T_N+ih_v\), \(-H_v\le h_v\le H_v\).
All other variables run horizontally at height \(-H_v\).
The full exponential upper functional from (15)--(17) is
\[
 \mathcal E_S=
 \Re\!\left(\sum_e\psi+
                    \sum_v\frac{in_vt_v^2}{4\pi}\right)
       -\sum_{v\notin S}\chi_vH_v
       -\sum_{v\in S}\chi_v|h_v|
          \le\Re\Phi_{\boldsymbol\chi}(\mathbf t).
 \tag{20}
\]
The last inequality uses \(-|h_v|\le h_v\).

Here is the mixed-current comparison, with its constants written
for the small charges. Put
\(\mathbf t-\mathbf t^*=\mathbf a+i\mathbf b\),
\(A_2=\sum_vd_va_v^2\), \(B_2=\sum_vd_vb_v^2\).
Outside \(S\), \(b_v=0\). On \(S\), equations (14) and the
choice of \(T_N\) give
\[
 a_v=T_N-\Re t_v^*>\frac7{12},\qquad
       0\le b_v\le2H_v\le3\chi_0,\qquad
                   n_va_v\ge21d_vb_v .
 \tag{21}
\]
For the final comparison it is enough that
\(3(94/100-21/3200)>126\chi_0\).
The straight segment to the critical point stays in the box
of (19). Taylor's formula there, Cauchy--Schwarz over the edges,
and \(4\sqrt{A_2B_2}\le A_2/10+40B_2\), give exactly
\[
 \begin{split}
 \Re\Phi_{\boldsymbol\chi}(\mathbf t)-M(\boldsymbol\chi)
 &\le-\frac{A_2}{40\pi}
       +\frac{42B_2}{4\pi}
       -\frac1{2\pi}\sum_{v\in S}n_va_vb_v\\
 &\le-\frac1{40\pi}\sum_{v\in S}d_va_v^2
                         <-\frac{|S|}{400}
                                  \quad(S\ne\varnothing).
 \end{split}
 \tag{22}
\]
The first line is the integral-Hessian calculation
(10)--(13) of the mixed-current note; the linear charge term
has zero Hessian, so that calculation is unchanged.
The middle two terms have nonpositive sum by (21).
Finally \(49/(5760\pi)>1/400\).
There is no factor depending on the number of other vertices.

## 5. Every removed physical-row subset has a strict gap

The original finite trace is first split according to the vertices
whose physical grid points lie outside \((-T_N,T_N)\).
Fix a nonempty such set \(S\), and retain all their original value
and first-normal terms. In the other variables use (15)--(16)
at the heights belonging to \(\boldsymbol\chi^S\).
Vertices in \(S\) now have zero stationary angle; they are not
subjected to a zero-height contour.

The centered full-kernel bounds in
[the mixed-current note](research_path_mixed_trace_currents.md),
Lemma 2, give, for an outer real angle \(u\) and a retained
complex angle \(z\),
\[
 |K_N(u,z)|\le CN^A
   e^{N[\Re\psi(0,z)-\gamma(1-\cos u)]},\qquad
 \gamma=\frac1{200}.
 \tag{23}
\]
For two outer real arguments the losses add and the phase is
\(\psi(0,0)\). First normals in the outer spectral variables obey
the same estimate at polynomial cost with loss
\(\gamma(1-\cos(9/10))\) per endpoint.
These bounds include mixed normals when both ends are traced.

The original crossing values at every removed row have modulus
one; their normal terms have polynomial cost for fixed \(n_v\).
The coupon has modulus at most one there, and its first angular
derivative has modulus at most \(N\). Converting any required
spectral derivative at a physical double root costs at most a
further polynomial, since its nonzero sine has a polynomial
reciprocal. The simple odd-level root is retained as a value.
Thus the coupons introduce no exponential cost in these rows.

After (23), the remaining exponential phase is exactly (4) with
the vertices in \(S\) set to zero. The retained components have
the same degrees, with their new complete boundary incidences.
Their all-horizontal upper estimate follows from (19), and
every mixed current obeys (22). Hence their total upper rate is
at most \(M(\boldsymbol\chi^S)\).

The loss from outer incidences is greater than
\((1/600)\sum_{v\in S}d_v\). On the other hand (6) gives
\[
 M(\boldsymbol\chi^S)-M(\boldsymbol\chi)
 \le\frac34\chi_0^2|S|
                   <\frac1{800}\sum_{v\in S}d_v .
 \tag{24}
\]
Consequently every nonempty removed-row subset has rate at most
\[
             M(\boldsymbol\chi)
                       -\frac1{2400}\sum_{v\in S}d_v .
 \tag{25}
\]
Only polynomial factors and finitely many subsets occur for a
fixed path. This proof controls the original full source and
does not replace a remaining oscillatory trace by the sum of
its absolute physical color contributions.

## 6. The surviving coefficient

**Theorem 2.** For the exact source (3) and charges (2), put
\[
 \varepsilon_N=\prod_{v\in I}C_{N,n_v},\qquad
 \mathcal H_{\boldsymbol\chi}
                    =-\Phi_{\boldsymbol\chi}''(\mathbf t^*).
 \]
Uniformly over these integer charge choices, along both parities,
\[
 \boxed{\quad
 Z_{\Gamma,I,N}(\mathbf j)
 =\varepsilon_N N^{3(m-e)/2}
        A_\Gamma(\boldsymbol\chi)
        e^{N\Phi_{\boldsymbol\chi}(\mathbf t^*)}
                           (1+O(N^{-1})),
 \quad}
 \tag{26}
\]
where
\[
 A_\Gamma(\boldsymbol\chi)=
 \left(\frac{i}{2\pi}\right)^m(2\pi)^{m/2}
 \frac{\displaystyle
       \prod_{v\in I}\sin t_v^*
       \prod_{\{v,w\}\in E}a_e(t_v^*,t_w^*)}
      {\sqrt{\det\mathcal H_{\boldsymbol\chi}}}\ne0 .
 \tag{27}
\]
The square root is the Gaussian branch on complex symmetric
matrices with positive definite real part. The absolute amplitude
has a positive lower bound on the compact box (2), for each fixed
path and powers. There is an expansion to every fixed inverse-power
order.

*Proof.* Equations (22) and (25) leave the all-horizontal central
term. On its rectangle (19) implies
\[
 \Re\mathcal H_{\boldsymbol\chi}
       \succeq\frac1{10\pi}\operatorname{diag}(d_v)>0.
 \tag{28}
\]
The same inequality along horizontal segments makes the real
part of (4) strictly concave, with unique maximum at the full
complex critical point. Every fixed complement of a neighborhood
of that point consequently has a uniform strict gap.

The heights have a positive uniform lower bound on (2). Formula
(15) therefore replaces all its rational kernels by their first
terms with exponentially small relative error. This contributes
exactly \(2^{-m}\); no companion term at the same rate remains
on the small charge box. Formula (18) supplies every original
edge amplitude. Each is nonzero, as is \(\sin t_v^*\), by (13).
The resulting Gaussian integral is
\[
 \int_{\mathbb R^m}
      e^{-x^T\mathcal H_{\boldsymbol\chi}x/2}\,dx
       =\frac{(2\pi)^{m/2}}
                   {\sqrt{\det\mathcal H_{\boldsymbol\chi}}}\ne0 .
 \tag{29}
\]
Its branch follows by diagonalizing the real symmetric imaginary
part after conjugation by the square root of the positive real
part. This also proves nonvanishing without a choice of a favorable
phase for the integrand.

The exact trace prefactors give \(N^{2m}(i/\pi)^m\varepsilon_N\);
the coupons give \(2^{-m}\); the edges give \(N^{-3e/2}\);
and the \(m\) saddle integrations give \(N^{-m/2}\).
This proves (26)--(27). Taylor expansion and (28) give the
uniform \(O(N^{-1})\) error and further orders. Compactness of
the charge box and the nonzero factors in (27) give its uniform
positive modulus bound. All uses of the original trace and
kernel retain both level parities and their first normals.
\(\square\)

In particular, if \(\boldsymbol\chi_N\) tends to a point of
the small box, then
\[
 \lim_{N\to\infty}\frac1N
              \log|Z_{\Gamma,I,N}(\mathbf j_N)|
                         =M(\boldsymbol\chi_\infty).
 \tag{30}
\]
The actual charges \(\mathbf j_N/N\), rather than their limits,
are used in the exponent of (26). Rounding a charge can change
its bounded leading phase.

This theorem provides a nonzero finite quantum contribution near
the complete corner for paths of arbitrary fixed length, with no
large-power assumption beyond \(n_v\ge3\). It does not identify
the charge-zero scalar with a bare-edge value. Nor does it prove
that the coefficient remains nonzero on a path from this box to
charge one. That continuation still needs control of the actual
charge observations, their translated spectators and endpoint
terms, as described in
[the exact charge system](research_fourier_lower_bounds_and_almost_invariance.md#15-the-exact-finite-system-for-changing-a-fourier-charge).

## 7. Signed and zero powers near the complete corner

The initial source does not require a lower bound on the absolute
crossing powers if the charge interval is made smaller.

**Corollary 3.** Fix any integers \(n_v\), allowing unrelated signs
and \(n_v=0\), on the selected vertices of the same nontrivial
finite path. Put
\[
 \widehat\chi_0=\frac1{2000},\qquad
 \chi_v=j_v/N\in[\widehat\chi_0/2,\widehat\chi_0].
 \tag{31}
\]
For the original source (3), expansion (26) holds with exactly the
amplitude (27), phase (4), and crossing unit
\(\varepsilon_N=\prod_v C_{N,n_v}\). The leading coefficient is
nonzero, uniformly on this compact charge box for each fixed
path and fixed powers, through both level parities. No complete
outside endpoint is required.

This assertion concerns the directly constructed small branch.
It does not assert global signed-charge continuation or identify
the charge-one source of a zero-power presentation with a
hyperbolic knot invariant.

*Proof.* Keep \(r=1/100\), \(\delta=1/15000\), and the functions
\(C_v\) from (7). Their estimates do not involve the crossing
powers. Since \(d_v\ge1\), on the smaller polydisk
\[
 |n_v+iC_v|
 \ge\sqrt{n_v^2+d_v^2}-\delta\ge1-\delta.
 \tag{32}
\]
Thus the fixed-point map (11) satisfies
\[
 |\mathcal T_v|
   \le\frac{2\pi\chi_v}{1-\delta}
      <\frac{63}{10}\chi_v<r,\qquad
 \|D\mathcal T\|_\infty
   \le\frac{2\pi\widehat\chi_0\,8r}{(1-\delta)^2}
      <\frac1{1000}.
 \tag{33}
\]
Banach's theorem again gives the unique small stationary point.
With \(C_v=A_v+iB_v\), \(A_v\ge d_v-\delta>0\), its height obeys
\[
 0<H_v=\frac{2\pi\chi_v A_v}
              {(n_v-B_v)^2+A_v^2}
       \le\frac{2\pi\chi_v}{A_v}
       <\frac{63}{10}\chi_v.
 \tag{34}
\]
For nonzero \(n_v\), \(\Re t_v^*\) has the sign of \(n_v\),
because \(|B_v|\le\delta<1\). No sign for \(\Re t_v^*\) is needed
when \(n_v=0\). The same small-edge criterion used in Lemma 1
proves positivity of the original shapes and fixes the complete
logarithmic branch. Differentiating the stationary action as before
gives, for a removed set \(S\),
\[
 0\le M(\boldsymbol\chi^S)-M(\boldsymbol\chi)
            \le\frac{63}{20}\sum_{v\in S}\chi_v^2.
 \tag{35}
\]
These facts follow directly in the small cube and use no global
existence theorem for the signed powers.

All contour variables have heights at most
\[
 \frac{63}{10}\widehat\chi_0=\frac{63}{20000}<\frac1{200}.
 \tag{36}
\]
Thus the full thin-rectangle kernel theorem still applies. The
exact coupon identities (15)--(17) also remain valid for every
integer \(n_v\), including zero.

For a vertical coordinate choose the side
\[
 t_v=\sigma_vT_N+ih_v,\qquad
 \sigma_v=
 \begin{cases}\operatorname{sgn}(n_v),&n_v\ne0,\\
               1,&n_v=0,\end{cases}
 \qquad -H_v\le h_v\le H_v.
 \tag{37}
\]
Replacing the positive side by the negative side multiplies that
exact integral by \(-1\). Indeed its entire numerator remains an
odd function of \(t_v\), because the Gaussian, coupon, and
spectator are even. Reflection \(t_v\mapsto-t_v\), followed by
\(h_v\mapsto-h_v\), proves the same identity as
[the signed current formula](research_path_mixed_trace_currents.md),
equation (37). The factor \(\prod_{v\in S}\sigma_v\) is retained
in the exact mixed term. It does not affect its absolute bound.
The horizontal side remains below the real axis, with positive
charge \(\chi_v\).

Write \(t-t^*=a+ib\) as before. At a vertical coordinate,
\[
 |a_v|\ge\frac{94}{100}-\frac{63}{10}\widehat\chi_0,
 \qquad
 0\le b_v\le\frac{63}{5}\widehat\chi_0,\qquad
                         n_va_v\ge0.
 \tag{38}
\]
The last inequality includes \(n_v=0\). In the first line of
(22), discard the nonpositive filling term instead of using it
to absorb the height error. The remaining estimate is
\[
 \begin{split}
 \mathcal E_S-M(\boldsymbol\chi)
 &\le-\frac{A_2}{40\pi}+\frac{42B_2}{4\pi}\\
 &\le-\frac1\pi
  \left[
   \frac{(94/100-(63/10)\widehat\chi_0)^2}{40}
       -\frac{42}{4}\left(\frac{63}{5}\widehat\chi_0\right)^2
  \right]\sum_{v\in S}d_v\\
 &<-\frac{|S|}{400}\qquad(S\ne\varnothing).
 \end{split}
 \tag{39}
\]
The bracket divided by \(\pi\) is greater than \(1/400\);
the scalar checker verifies this using \(\pi<22/7\).
This comparison uses absolute norms in the mixed Hessian term,
so it does not require all real displacements to have the same sign.

The outer-row proof is unchanged. The physical values of every
signed crossing have modulus one and their first normals have
polynomial cost; for zero power the normal is zero. The coupons
have the same value and derivative bounds. Equation (35) gives
\[
 M(\boldsymbol\chi^S)-M(\boldsymbol\chi)
 \le\frac{63}{20}\widehat\chi_0^2|S|
                  <\frac1{800}\sum_{v\in S}d_v.
 \tag{40}
\]
The outer incidence loss therefore again leaves (25). At the
all-horizontal saddle the filling Hessian is purely imaginary
for every real integer \(n_v\). Consequently (28) and the
Gaussian calculation are unchanged. Every height is strictly
positive and has a positive uniform lower bound on (31) for
fixed powers, so the alias estimate and the nonvanishing sine
factors also hold when a power is zero. The same prefactor count
and compactness argument prove (26)--(27). \(\square\)

## 8. Initialization on any fixed graph with the same edge kernel

The small-charge construction uses bounds on individual incidences,
not a decomposition of a path into intervals. Its natural scope is
therefore larger than the path sources used above.

**Corollary 4.** Let \(\Gamma=(V,E)\) be any fixed finite
undirected graph carrying the same-index kernels (1). Repeated edges
are allowed. A loop carries \(K_N(t_v,t_v)\) and is counted twice
in \(d_v\). Choose a nonempty set \(I\) of selected vertices, none
isolated, and fix arbitrary integers \(n_v\), including zero.
Set every unselected angle to zero. Define the finite source
exactly by (3), with all the original products and first normals,
and choose the charges in (31).

Then (26)--(27) hold, with \(m=|I|\), \(e=|E|\), and the phase
(4) summed over this graph. Its critical point is the small branch
continued from completeness. The amplitude is nonzero uniformly
on the compact charge box for this fixed graph and these powers.
No graph-to-knot realization, global filling geometry, or
charge-one limit is asserted.

*Proof.* Let \(r=1/100\), and set
\[
                         \epsilon=\frac{r^2}{3}=\frac1{30000}.
 \tag{41}
\]
For one incidence, the function
\[
 f(t,u)=
      \frac{2\operatorname{arsinh}(\tan(t/2)\cos(u/2))}{t}-1
\]
is holomorphic at \(t=0\). Equation (9) gives
\(|f(t,u)|\le\max(|t|,|u|)^2/3\) on the bidisk of radius \(2r\).
Hence, on the graph polydisk of radius \(r\),
\[
 |C_v-d_v|\le d_v\epsilon,\qquad
       \sum_w|\partial_{t_w}C_v|\le\frac{8r}{3}d_v.
 \tag{42}
\]
For the derivative bound, apply Cauchy's estimate separately in
the two arguments of one incidence. Each derivative is at most
\(4r/3\), and summing over the incidences gives (42). Repeated
neighbors only add these bounds. On a loop both arguments are
the same variable; the chain rule adds their two derivative
bounds, as required.

For every integer \(n_v\),
\[
 |n_v+iC_v|\ge\sqrt{n_v^2+d_v^2}-d_v\epsilon
                         \ge d_v(1-\epsilon).
 \tag{43}
\]
The fixed-point map (11) consequently obeys
\[
 |\mathcal T_v|<\frac{63}{10}\frac{\chi_v}{d_v}<r,\qquad
 \|D\mathcal T\|_\infty
 \le\frac{2\pi\widehat\chi_0(8r/3)}{(1-\epsilon)^2}
                                      <\frac1{1000}.
 \tag{44}
\]
It has a unique small fixed point, with analytic local dependence
on the charges. Since \(\Re C_v\ge d_v(1-\epsilon)>0\), the
height formula gives
\[
 0<H_v<\frac{63}{10}\frac{\chi_v}{d_v}
                  \quad(\chi_v>0),\qquad
 M(\boldsymbol\chi^S)-M(\boldsymbol\chi)
       \le\frac{63}{20}\sum_{v\in S}\frac{\chi_v^2}{d_v}.
 \tag{45}
\]
The latter identity follows by integrating
\(\partial_{\chi_v}M=-H_v\) within this small cube. The small
edge criterion used earlier fixes all local shapes and logarithmic
branches. It is an assertion about these edge functions; no
manifold realization of the graph is needed.

All contour heights remain below \(63/20000<1/200\).
The original derivative-sampling identity applies to the entire
product of incident kernels at each selected vertex, regardless
of its degree. That product is even in that vertex's angle,
including a diagonal loop factor. Thus the exact coupon identity,
its coefficient \(1/2\), its aliases, and the reflected vertical
sign are unchanged.

On the thin rectangle the edgewise Hessian inequalities (19) give,
after restriction to the selected variables,
\[
 \Re K_\Gamma\succeq\frac15\operatorname{diag}(d_v),\qquad
 |a^{\mathsf T}K_\Gamma b|
       \le2\left(\sum_vd_v a_v^2\right)^{1/2}
             \left(\sum_vd_v b_v^2\right)^{1/2}
 \tag{46}
\]
for real vectors, with the same bound for either real or imaginary
part. This follows by applying the edge bound to the two endpoint
coordinates and then Cauchy--Schwarz over edges. On a loop the
coordinate occurs twice, matching its contribution to \(d_v\).

Choose the vertical side by (37). Even if the real part of a
critical angle has not been assigned a sign, for \(n_v\ne0\)
\[
 n_v(\sigma_vT_N-\Re t_v^*)
          \ge |n_v|(T_N-|\Re t_v^*|)>0;
 \tag{47}
\]
for zero power this expression is zero. The proof of (39) uses
only (46), the bounds \(|t_v^*|,H_v<6.3\widehat\chi_0\), and
(47). It therefore gives the same strict gap for every nonempty
vertical subset, without a factor depending on graph degree or
the number of other vertices.

For a removed physical-row subset, apply the centered kernel
bound edge by edge. Every removed incidence retains its loss
greater than \(1/600\). To include normals, apply multivariate
Markov inequalities to the entire kernel product on the fixed
removed spectral intervals. Its degree in a removed variable is
at most \(d_v(N-1)\), so all mixed first normals have only
polynomial cost for the fixed graph. This includes a loop:
its diagonal polynomial has degree at most \(2(N-1)\) and keeps
the losses of both endpoints. The crossing and coupon values
and normals have the bounds already used in Section 5.
No factorization into path components is required.

After centering the removed variables, the upper phase is again
the same graph phase with those variables zero. Its selected
degrees retain all incidences to the new complete vertices.
Equation (45) gives
\[
 M(\boldsymbol\chi^S)-M(\boldsymbol\chi)
 \le\frac{63}{20}\widehat\chi_0^2\sum_{v\in S}d_v^{-1}
              <\frac1{800}\sum_{v\in S}d_v.
 \tag{48}
\]
Thus (25) holds on this graph as well.

Finally (46) makes the all-horizontal phase strictly concave
with a nondegenerate full complex critical point. Every selected
variable has \(d_v\ge1\), so no null direction remains.
Its heights are uniformly positive on (31) for the fixed graph
and powers. The original kernel amplitudes, sine factors,
Gaussian determinant and coupon coefficients are all nonzero.
The same prefactor count gives \(N^{3(m-e)/2}\) and exactly
(27). This proves the corollary. \(\square\)

The graph is fixed before \(N\) tends to infinity. The constants
in the polynomial error bounds and the amplitude may depend on
it, while the displayed charge interval and elementary geometric
bounds do not. The result initializes the specified finite
same-index source. It does not replace a different edge kernel,
such as a reversed-index kernel, by this one.
