# Exponential real characteristic concentration of the actual edge source

Private written proof, 23 November 2026.

The exact same-index edge equation gives exponential, rather than
only algebraic, concentration away from a fixed real symbol gap.
For a graph with arbitrary coupled channel weights, the bound is
\(CE N^2e^{-cN\delta^2}\) times its full Fourier energy.
Normalized angular jets satisfy the same estimate as a complete vector.

The proof iterates the adjoint equation on explicit Gaussian test
functions. Only those known test functions are continued to fractional
Weyl displacements. No continuation or asymptotic expression for the
unknown source is used. All incidence variables remain separate until
the original vertex and marked-closing operations are applied.

## 1. Exact source and the quantitative statement

Use the complete source conventions of [A] and its complete original
source direct [F]. Put \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\),
\(Q=q^2\), and
\[
 B_k(z)=\frac{q^{-k^2}(-qz;Q)_k(-q/z;Q)_k}{S_k^2},
 \qquad S_k=\prod_{j=1}^k2\sin(\pi j/N),\quad 0\le k\le d.
 \tag{1}
\]
In particular \(B_k(z)=e_k(-z-z^{-1})\), with the actual common
Newton basis and no discarded endpoint channels. For a graph with
\(E\ge1\) edges, keep two separate incidence variables per edge and
any finite complex coefficient array:
\[
 F_N=\sum_{\mathbf k\in\{0,\ldots,d\}^E}
          \mu_{\mathbf k,N}\prod_{e=1}^E B_{k_e}(z_e)B_{k_e}(y_e).
 \tag{2}
\]
The weights may be arbitrarily coupled and level-dependent; they must
be independent of the incidence activities. This includes the actual
edge insertion weights and their activity-independent normal weights
where defined. Each individual Fourier exponent lies in \([-d,d]\).

Let \(\mathscr D_j=z_j\partial_{z_j}\), with all incidence variables
included. Let \(\mathcal A\) be a finite downward-closed set of
multiindices containing zero, and put
\[
 p=\max_{\alpha\in\mathcal A}|\alpha|,\qquad
 u_\alpha=N^{-|\alpha|}\mathscr D^\alpha F_N .
 \tag{3}
\]
The scalar case is \(\mathcal A=\{0\}\). The integer \(p\) is fixed;
it is unrelated to the growing physical occupation degree.

Use the exact Gaussian Fourier analysis \(\mathcal F_N\) of [A](8)
on all \(2E\) coordinates, with a fixed width \(\sigma>0\).
At edge \(e\), write \(z=e^{i\theta_z}\), \(y=e^{i\theta_y}\),
\(Y_z=e^{2\pi i\xi_z}\), \(Y_y=e^{2\pi i\xi_y}\), and set
\[
 p_{e,0}=
 \frac{(1+z)(1+y)}{zy}
 \{(z-y)(Y_zY_y-1)+(1-zy)(Y_z-Y_y)\}.
 \tag{4}
\]
The prefactor, including its zeros at \(z=-1\) or \(y=-1\), is
retained. Define \(\mathcal B_\delta=\{\max_e|p_{e,0}|\ge\delta\}\).
There are positive constants \(C_{\sigma,p},c_{\sigma,p}\),
independent of the coefficient array and the number of edges, such that
\[
 \boxed{\quad
 \int_{\mathcal B_\delta}
       \sum_{\alpha\in\mathcal A}|\mathcal F_Nu_\alpha|^2d\nu
 \le C_{\sigma,p} E N^2 e^{-c_{\sigma,p}N\delta^2}
             \sum_{\alpha\in\mathcal A}\|u_\alpha\|_2^2,
 \qquad 0<\delta\le1 .
 \quad}
 \tag{5}
\]
The norm and measure are exactly the Laurent coefficient norm and
full Gaussian-frame measure. For every fixed \(\delta>0\), the
right side is also \(C_{\sigma,p,\delta}E e^{-c_{\sigma,p,\delta}N}\)
times that energy. This is an off-characteristic estimate, not an
exponentially small bound on the entire weighted second moment.

## 2. Exact equations and Weyl ordering

For one incidence pair put
\[
 \begin{gathered}
 a_z=1+qz,\quad b_z=1+q^{-1}/z,\quad T_zf(z)=f(Qz),\\
 A_z=a_zT_z-b_z,\quad D_z=b_zT_z-a_z,\quad
 P_N=A_zD_y-D_zA_y .
 \end{gathered}
 \tag{6}
\]
The cleared product identity in [A](4) gives
\(A_zB_k=-Q^kD_zB_k\). Consequently \(P_{e,N}F_N=0\) for
every edge of (2). Its exact normal order is
\[
 P_N=(a_zb_y-b_za_y)(T_zT_y-1)
                    +(b_zb_y-a_za_y)(T_z-T_y).
 \tag{7}
\]
Its exponent set and coefficient bounds are fixed independently of
\(N\). All these are full Laurent identities, including all low and
high channels. No finite output compression occurs.

On the full Fourier lattice \(\ell^2(\mathbb Z^2)\), let
\((Z^af)_m=f_{m-a}\) and \((T^bf)_m=Q^{b\cdot m}f_m\).
Thus \(T^bZ^a=Q^{a\cdot b}Z^aT^b\). The symmetric Weyl operator is
\[
 \begin{split}
 W_N(a,b)&=Q^{a\cdot b/2}Z^aT^b,\\
 (W_N(a,b)f)_m
    &=e^{2\pi ib\cdot(m-a/2)/N}f_{m-a},\\
 W_N(a,b)W_N(c,e)
    &=e^{\pi i(b\cdot c-a\cdot e)/N}W_N(a+c,b+e).
 \end{split}
 \tag{8}
\]
Here \(Q^{a\cdot b/2}=e^{\pi ia\cdot b/N}\), and
\(W_N(a,b)^\dagger=W_N(-a,-b)\).
A normal coefficient \(c_{ab,N}\) becomes
\(c_{ab,N}Q^{-a\cdot b/2}\) in this Weyl order.
No ordering phase is silently discarded.

We will use a Hilbert-valued version. Suppose
\(\mathbb P_N=\sum_t C_{t,N}W_N(a_t,b_t)\) on
\(\ell^2(\mathbb Z^2;\mathcal H)\), with a fixed finite set of
bounded integer displacements and \(\sum_t\|C_{t,N}\|\le A\).
The coefficient operators act only on \(\mathcal H\). Its Weyl symbol is
\[
 \mathfrak p_N(\theta,\xi)
   =\sum_t C_{t,N}e^{i(a_t\cdot\theta+2\pi b_t\cdot\xi)}.
 \tag{9}
\]
Assume \(\|\mathfrak p_N-p_0I_{\mathcal H}\|\le A/N\), uniformly
on this real phase space. For (7) this follows by \(q\to1\) and
the ordering phase in (8), with exactly the scalar (4).
Constants in the test-function estimates may depend on the fixed
displacement set. For the edge operators and their prolongations
that set is absolute and independent of the graph.

## 3. Analytic Gaussian tests on the full lattice

For \(\theta\in\mathbb T^2\), \(\xi\in\mathbb R^2\), write
\[
 g_{\theta,\xi}(m)=c_N
  e^{-|m-N\xi|^2/(2\sigma N)}e^{-im\cdot\theta},
 \qquad c_N=(N/(\pi\sigma))^{1/2}.
 \tag{10}
\]
Then \(\mathcal F_Nf=\langle g_{\theta,\xi},f\rangle\) and the
frame is an exact isometry, also for Hilbert-valued coefficients.
Its individual test-vector norm is at most \(C_\sigma N\).
These vectors need not be individually normalized.

For the following calculation only, extend the known Gaussian (10)
to an entire function of its argument. For complex vectors \(A,B\)
define its centered displacement by
\[
 (\mathcal C_{\theta,\xi}(A,B)h)(z)=
 e^{-iA\cdot\theta-2\pi iB\cdot\xi}
 e^{2\pi iB\cdot(z-A/2)/N}h(z-A).
 \tag{11}
\]
At integer \(A,B\), this is the centered version of (8) on the
sampled Gaussian. No fractional shift of the source \(f\) is defined.
For \(t=m-N\xi\), direct substitution gives
\[
 (\mathcal C(A,B)g)(m)=c_N e^{-im\cdot\theta}
 \exp\left\{-\frac{(t-A)\cdot(t-A)}{2\sigma N}
       +\frac{2\pi iB\cdot t}{N}-\frac{\pi iA\cdot B}{N}\right\}.
 \tag{12}
\]
All dependence on the real center cancels except in the translated
lattice \(t=m-N\xi\). Completing the real square proves
\[
 \|\mathcal C(A,B)g\|_{\ell^2}
 \le C_\sigma N
       \exp\{C_\sigma(|A|^2+|B|^2)/N\}.
 \tag{13}
\]
Indeed its squared modulus is a real translated Gaussian times
an exponential bounded by \(e^{C_\sigma(|A|^2+|B|^2)/N}\).
The uniform bound
\(\sum_{m\in\mathbb Z^2}e^{-|m-c|^2/(\sigma N)}\le C_\sigma N\)
follows by a sum--integral comparison in each coordinate.
Together with \(c_N^2=O_\sigma(N)\) it gives (13).
This proof is uniform over all real \(\theta,\xi\).

For any ordered list of \(m\) bounded displacements, consider
\(\prod_{j=1}^m\mathcal C(s_ja_j,s_jb_j)g\).
The product law (8) extends algebraically to these complex parameters.
Its scalar phase has logarithmic modulus at most
\(Cm^2(1+r)^2/N\) when \(|s_j|\le1+r\), and both summed
displacements have size at most \(Cm(1+r)\).
Equation (13) therefore gives the uniform bound
\[
 \left\|\prod_{j=1}^m
           \mathcal C(s_ja_j,s_jb_j)g\right\|_{\ell^2}
       \le C_\sigma N\exp\{C_\sigma m^2(1+r)^2/N\}.
 \tag{14}
\]
The product is an entire Hilbert-space-valued function of the
\(m\) parameters: its sampled entries are entire and the Gaussian
bound is locally summable. This continuation concerns explicit
test functions only.

## 4. High differences give an exponential estimate

Suppose \(\mathbb P_N f=0\). At a phase point where
\(|p_0|\ge\delta\) and \(A/N\le\delta/2\), the matrix symbol is
invertible with \(\|\mathfrak p_N^{-1}\|\le2/\delta\).
Keep this symbol fixed at that point and define
\[
 \mathbb Q=I-\mathbb P_N^\dagger(\mathfrak p_N^\dagger)^{-1}.
 \tag{15}
\]
The inverse in (15) is on the right. Thus
\(\mathbb Q^\dagger f=f\) even when the coefficient matrices do
not commute. For any \(h\in\mathcal H\),
\(\langle g\otimes h,f\rangle
  =\langle\mathbb Q^m(g\otimes h),f\rangle\).

Put \(w_t=e^{i(a_t\cdot\theta+2\pi b_t\cdot\xi)}\).
Exactly,
\[
 \mathbb Q=\sum_t D_t(I-V_t),\quad
 D_t=C_{t,N}^\dagger\bar w_t(\mathfrak p_N^\dagger)^{-1},
 \quad V_t=w_tW_N(-a_t,-b_t),\quad
 \sum_tD_t=I,\quad\sum_t\|D_t\|\le2A/\delta .
 \tag{16}
\]
The matrices \(D_t\) commute with the physical displacements, not
necessarily with one another.
The analytic interpolation of \(V_t\) is
\(\mathcal C(-sa_t,-sb_t)\), equal to \(I\) at \(s=0\).

For each ordered word, the mixed fundamental theorem of calculus
expresses \(\prod_{j=1}^m(I-V_{t_j})g\), up to its sign, as
the integral over \([0,1]^m\) of the mixed derivative
\(\partial_{s_1}\cdots\partial_{s_m}\prod_j
\mathcal C(-s_ja_{t_j},-s_jb_{t_j})g\).
Apply multivariate Cauchy at radius \(r>0\) in each variable to (14).
Every variable is differentiated once, so there is no factor \(m!\).
One obtains
\[
 \left\|\prod_{j=1}^m(I-V_{t_j})g\right\|
       \le C_\sigma N r^{-m}
                     e^{C_\sigma m^2(1+r)^2/N}.
 \tag{17}
\]
The same estimate follows by scalar Cauchy after testing against
each unit vector, so no finite-dimensional truncation is involved.
Expand \(\mathbb Q^m\), bound the matrix words by the products of
their norms, and sum using (16). With \(1\le m\le N\) and
\(r=\sqrt{N/m}\), (17) gives
\[
 \|\mathbb Q^m(g\otimes h)\|
 \le C_\sigma N
       \left(\frac{C_{\sigma,A}}{\delta}\sqrt{\frac mN}\right)^m
              e^{C_\sigma m^2/N}\|h\|.
 \tag{18}
\]
Here \(m^2(1+\sqrt{N/m})^2/N\le C(m+m^2/N)\);
the factor \(e^{Cm}\) has been included inside the parentheses.

Choose a fixed sufficiently small \(\varepsilon>0\), depending
only on the coefficient and displacement bounds and \(\sigma\),
and put \(m=\lfloor\varepsilon N\delta^2\rfloor\).
When \(N\delta^2\) exceeds a sufficiently large fixed constant,
the symbol inverse exists, \(m\ge\varepsilon N\delta^2/2\), and
the parenthesized factor times \(e^{C_\sigma m/N}\) is below
\(e^{-2}\). Equations (15)--(18), followed by supremum over
\(\|h\|=1\), imply
\[
 \|\mathcal F_N f(\theta,\xi)\|_{\mathcal H}
      \le C_\sigma N e^{-c_{\sigma,A}N\delta^2}\|f\|_2
                \quad\text{on }\{|p_0|\ge\delta\}.
 \tag{19}
\]
This estimate is uniform in the center.

To integrate it, assume the Fourier support of \(f\) in these two
coordinates is in \([-d,d]^2\). On \(|\xi|_\infty\le2\), the
measure has finite volume, and (19) gives the desired
\(CN^2e^{-cN\delta^2}\) bound. On its complement, angular Parseval
and (10) give directly
\[
 \int_{\{|\xi|_\infty>2\}}\|\mathcal F_Nf\|_{\mathcal H}^2d\nu
                    \le C_\sigma e^{-c_\sigma N}\|f\|_2^2 .
 \tag{20}
\]
For every supported index, at least one Gaussian coordinate is a
distance \(N\) from its center on that region; splitting half its
Gaussian exponent proves (20) by elementary integration.
Since \(0<\delta\le1\), this tail is absorbed by the same bound.
In the remaining regime of bounded \(N\delta^2\), isometry gives
the bound after increasing its fixed constant. We have proved
\[
 \int_{\{|p_0|\ge\delta\}}\|\mathcal F_Nf\|_{\mathcal H}^2d\nu
           \le C_{\sigma,A}N^2e^{-c_{\sigma,A}N\delta^2}\|f\|_2^2
 \tag{21}
\]
for every exact null vector of the operator in (9).

## 5. Coupled channels and the full angular-jet vector

First apply (21) to (2) and one edge. Regard all other Fourier
coordinates as a Hilbert-valued coefficient. The coefficients of
(7) are uniformly bounded, and (9) differs from (4) by \(O(N^{-1})\).
The source Fourier support on that edge is in \([-d,d]^2\).
Analysis in the other coordinates is an exact isometry and preserves
the integrated partial-frame norm. The constants are therefore
independent of the number of other coordinates and of their coupled
channel weights. Taking the union of the \(E\) bad sets proves (5)
in the scalar case.

For the jets (3), the exact equations in [A](17) are
\[
 P_{e,N}u_\alpha+
 \sum_{\beta<\alpha}\binom\alpha\beta
     N^{-(|\alpha|-|\beta|)}
       (\mathscr D^{\alpha-\beta}P_{e,N})u_\beta=0 .
 \tag{22}
\]
Coefficient derivatives only are meant in the second term. These
are homogeneous equations for the whole prolonged vector, not
separate homogeneous equations for its individual jets.

To apply (21), group the jets by their multiindex outside edge \(e\).
Within each group, the two remaining indices form a downward-closed
set with at most \((p+1)^2\) members. The resulting block operator
has \(P_{e,N}\) on its diagonal and fixed-degree off-diagonal entries
of norm \(O_p(N^{-1})\). Its Weyl symbol is
\[
                        p_{e,0}I+O_p(N^{-1}).
 \tag{23}
\]
Its finite exponent set, coefficient sum, and error bound depend only
on \(p\), not on the outside multiindex or the number of edges.
Indeed a coefficient derivative outside the two edge coordinates
is zero; all remaining binomial factors have order at most \(p\).
The direct sum of these groups, with the other Fourier coordinates,
can be used as the Hilbert coefficient space in (9).
Apply (21) to this exact homogeneous block system, use isometry in
the other coordinates, and take the union over edges. This proves
the full assertion (5). No commutator forcing has been discarded.

## 6. A bound for the actual marked closing of the complementary piece

For the fixed template and vertex rules of [F], the original marked
closing is a known polynomially bounded linear functional on the
finite canonical incidence space. We prove the needed norm comparison,
rather than commuting a phase-space cutoff through that closing.

Let \(\mathcal V_N\) be the space of separately even Laurent polynomials
of band \([-d,d]\) in every one of the \(2E\) incidence variables.
The source (2) belongs to this space. Keep a compact parameter disk
\(|s|\le R<1\), the template's fixed signed crossing powers, its own
relations \(P_{\sigma_v}\), and its original full marked functional
\(\Lambda_{N,s}\). Then
\[
             |\Lambda_{N,s}(h)|\le C_{\mathrm{template},R}N^B
                                   \|h\|_2,\qquad h\in\mathcal V_N .
 \tag{24}
\]
Here \(B\) depends on the fixed template and powers, not on \(h\)
or any coefficient array in (2).

Indeed \(\|h\|_{\mathrm{Fourier}\,1}\le(2d+1)^E\|h\|_2\).
Group reciprocal monomial orbits using
\(z^j+z^{-j}=2(-1)^j C_j(X)\), \(X=-z-z^{-1}\).
Their Chebyshev coefficient sum equals their Fourier coefficient sum.
Identifying the incidence variables at a vertex cannot increase that
sum: \(2C_iC_j=C_{i+j}+C_{|i-j|}\).
The actual fixed crossing polynomial \(p_v\) has polynomial
Chebyshev coefficient sum by the complete normal-norm lemma in [F].
After multiplication, the vertex degree is at most \((d_v+1)d\).
Reduction in its proper relation costs at most a fixed power of
\(2\cosh(2\pi R)+1\), again by [F], so this is a template constant.
Finally \(\phi_{\sigma_v}=\eta N^2[X^d]\) extracts \(N^2/2\)
times the top Chebyshev coefficient. These bounds prove (24).
The actual external framing and \(H_N(s)\) factors in [F] are
uniformly bounded on the disk and remain included.
All quotient reductions and repeated-root normal directions stay
in this calculation. Fixed parameter derivatives obey the same
type of bound by Cauchy on a slightly larger disk inside \(|s|<1\);
no moving-quantum-parameter estimate is asserted.

Let \(\Pi_N\) be the orthogonal projection onto \(\mathcal V_N\):
first retain the full band, then average independently under
\(z_j\leftrightarrow z_j^{-1}\). Those two projections commute.
Use the full \(2E\)-dimensional exact frame and define
\[
 Q_\Omega=\Pi_N\mathcal F_N^\dagger
                       \mathbf1_\Omega\mathcal F_N\Pi_N,\qquad
 F_{\mathrm{off}}=Q_{\mathcal B_\delta}F_N,\qquad
 F_{\mathrm{on}}=Q_{\mathcal B_\delta^c}F_N .
 \tag{25}
\]
Each \(Q_\Omega\) is a positive contraction on \(\mathcal V_N\), and
\[
 F_N=F_{\mathrm{on}}+F_{\mathrm{off}},\qquad
 \|F_{\mathrm{off}}\|_2^2
 \le\langle F_N,Q_{\mathcal B_\delta}F_N\rangle
 =\int_{\mathcal B_\delta}|\mathcal F_NF_N|^2d\nu .
 \tag{26}
\]
The inequality follows from \(0\le Q\le I\), hence \(Q^2\le Q\).
Applying (5) in its scalar case and then the actual functional (24)
gives the source-exact decomposition and estimate
\[
 \begin{gathered}
 \Lambda_{N,s}(F_N)=
       \Lambda_{N,s}(F_{\mathrm{on}})
                    +\Lambda_{N,s}(F_{\mathrm{off}}),\\
 |\Lambda_{N,s}(F_{\mathrm{off}})|
 \le C_{\mathrm{template},R,\sigma}\sqrt E\,N^{B+1}
           e^{-c_\sigma N\delta^2/2}\|F_N\|_2 .
 \end{gathered}
 \tag{27}
\]
Every functional and scalar is the original one. The complementary
source has been projected back to its full canonical polynomial space
before applying that functional. No cutoff is commuted through a
vertex, and no new cap replaces the marked closing.
This assertion concerns the base source and its activity-independent
insertion weights. An angular-jet closing must retain its own literal
functional and parity; (25) is not a prescription to evenize an
arbitrary differentiated closing.

## 7. Scope and complete sources

The exponential bound applies to the real unitary phase space of
the full free incidence variables. There is no alias identification,
discarded channel endpoint, or artificial finite output compression.
The full marked vertex operations and their normal coordinates remain
the original closing \(\Lambda_N\) of [A], with its full phases,
turns, reductions and scalars. The proved closing estimate is (27)
for that specific compiler and its canonical incidence norm; a
different compiler requires its actual adapter. This Fourier norm is
not identified with the original ordinary-color Plancherel energy.

The estimate is an exponential real complementary-region bound for
the actual pre-gluing source class, with the source-relative marked
remainder (27). The retained contribution still needs a nonzero
coherent lower estimate, and the pre-gluing norm still needs its
geometric rate. Neither (5) nor (27) selects a complex hyperbolic
characteristic or a nonzero geometric-cycle coefficient, or proves
a lower bound after arbitrary short fillings.
Moving-quantum-parameter jets and conversions to Casimir normals at
parabolic angles are not inferred from normalized angular jets.

The complete proof inputs are [A],
[the 302-line algebraic characteristic bound](research_same_index_edge_fourier_characteristic_bound.md),
SHA256 2e5788e51a5586966b53f0eb5a864b83415c134a083de939fca141cc7ae434ee;
and [F], the complete 227-line original source
papers/circle-tree-asymptotics/finite-bounds.tex,
e4cf66544703af6d9a78208deae971c4d9f4367ba4b2ad660694ee489ef67ea1.
The adjoint iteration, complex test bound, and matrix extension
needed here are all proved above.

Complete comparison texts, retained at their matching pins, are
papers/circle-tree-asymptotics/edge-packet.tex (268 lines),
53eb6dbfbda3ca639db35911ed50947c29655840337f9d1f1ce909d435013dbb;
notes/research_gaussian_frame_newton_transport.md (335 lines),
b6ed7fa19097323f76b0b22fb4fc7361b9d4e52c3f19d17c12d94c6fff623af9;
notes/research_finite_gabor_pointed_source_sewing.md (455 lines),
8a954f9f2bec9e0fc8971b08ea0ca493f712d4e2ace6bb9fc2c1fcf705699c37;
notes/actual_pointed_a_bulk_agmon_energy.md (199 lines),
df1bccf577f5732dd7697bf2ae03901077d63b48f85820544dba10395391effd;
and notes/actual_pointed_a_interval_observability.md (215 lines),
2e35ceb58d9488b7b383bbce4af123243270ddeff86570eff8ac20efb010b136.
No general novelty claim for analytic coherent-state methods is made.
Only written mathematics and source-text/hash operations were used.
