# Actual fixed-width Gauss coherent kernels from reverse propagation

Private written proof, 18 November 2026.

The complete ordinary-binomial first row in B initializes reverse
suffix-Casimir propagation. At the fixed root both apparent inverse
Euler factors in the binomial-conjugated generators are exactly short
clock-rotation integrals. This permits an analytic estimate of the
actual low output coefficients, followed by recovery of the entire
finite cap. The resulting full coherent kernel has a nonzero amplitude
and a nondegenerate mixed phase on the specified small input sectors.

This proof does not transform the relative error of a monomial kernel.
The input sum is paid first, and the new error estimate is propagated
with its literal binomial weights.

## 1. Actual kernel and coherent initialization

Use the root conventions
\[
 c_0=2\pi i,\quad Q=e^{c_0/N},\quad q=e^{c_0/(2N)},\quad
 x=-q^{-1},\quad d=N-1,\quad \epsilon=N^{-1},\quad h=c_0/N.
 \tag{1}
\]
Fix \(r\ge2,\ s=r-1,\ p=r-2\) and integer degree \(T\le d\), with
\[
 \sigma=(T+1)/N\in I\Subset(1/2,1),\quad
 C=e^{-c_0\sigma}=Q^{-T-1},\quad \tau=T/N=\sigma-\epsilon,
 \quad c_i=x^{r-i}.
 \tag{2}
\]
The actual matrix \(A=A_N^{(r)}\), the simplex basis
\(|\alpha\rangle=|\alpha_1,\ldots,\alpha_s,T-|\alpha|\rangle\),
and its nonzero vacuum \(a_{00}^{(r)}\) are those of the complete
directs M and B. Retain these finite objects exactly. Write
\[
 b_\beta=\binom d{T-|\beta|}\prod_{i=1}^s\binom d{\beta_i},
 \qquad b_{\mathbf0}=\binom dT.
 \tag{3}
\]
Our normalized full coherent kernel is
\[
 U_N(\rho,\xi)=
 \sum_{\substack{|\alpha|\le T\\|\beta|\le T}}
   \frac{A_{\alpha\beta}}{a_{00}^{(r)}}
    c^{-\alpha-\beta}\rho^\alpha\xi^\beta
                        \frac{b_\beta}{b_{\mathbf0}}.
 \tag{4}
\]
For the original monomial output and ordinary-binomial coherent input,
\[
 v(w)A c_T(z)=
  a_{00}^{(r)}(w_rz_r)^T\binom dT\, U_N(\rho,\xi),\qquad
 \rho_i=c_iw_i/w_r,\quad \xi_i=c_iz_i/z_r.
 \tag{5}
\]
All caps and physical phases in (4),(5) remain.

Choose an input polydisk \(D\) with compact closure, with
successively larger polydisks inside B's punctured sector, avoiding
each coordinate \(\xi_i=0\). The sector has bounded shapes and
\[
 a_*^2=a\,b\,\sum_i\xi_i,\quad
 a=2/c_0,\quad b=\tau/(1-\tau),\qquad
 |\arg a_*|<\theta_0<\pi/3.
 \tag{6}
\]
Choose the same branches on the larger domains, uniformly for (2).
The avoidance of coordinate zero is used only for analytic
coefficients of the dehomogenized operator rows; it is a genuine
nonempty open subdomain of B's chart.

B proves the actual boundary asymptotic, with all complementary
terms estimated,
\[
 U_N(0,\xi)=N^{-p-1/2}
   e^{N\Psi(\xi;C,\tau)} B_\partial(\xi;C,\tau)
                         (1+O(N^{-1})).
 \tag{7}
\]
Its explicit unit is
\[
 B_\partial=
 (2\pi\mathcal H)^{-1/2}
   A_r^\partial(t_*;C) A_B(\xi/t_*;\tau).
 \tag{8}
\]
Here \(t_*\) is the actual outer saddle,
\(\Psi=\phi(t_*;C)+S_B(\xi/t_*;\tau)\), and all functions are
exactly those of B. In particular its Gaussian coefficient is one.

For the propagation parameter keep \(\sigma\) exact and put
\[
 \psi(\xi;\sigma)=\Psi(\xi;e^{-c_0\sigma},\sigma),\qquad
 B_0(\xi;\sigma)=
 B_\partial(\xi;e^{-c_0\sigma},\sigma)
 \exp[-\partial_\tau\Psi(\xi;e^{-c_0\sigma},\sigma)].
 \tag{9}
\]
The derivative in (9) keeps \(C,\xi\) fixed. These functions are
analytic on the chosen input domain. Taylor expansion in the exact
\(\tau=\sigma-\epsilon\), on a slightly larger domain, turns (7)
into
\[
 N^{p+1/2}U_N(0,\xi)
       =e^{N\psi(\xi;\sigma)}B_0(\xi;\sigma)
                       (1+O(N^{-1})).
 \tag{10}
\]
Thus the \(N-1\) degree correction is retained in the initialized
amplitude. No derivative of a root asymptotic in \(M\) or \(q\)
is involved.

## 2. The exact binomial generators are local clock arcs

For a single head let
\[
 R_v(z)=\sum_{a=0}^d\binom da v_a z^a,\qquad D=z\partial_z.
 \]
Using the actual zero endpoint arrows, direct coefficient comparison
gives
\[
 \begin{split}
 R_{Ev}&=z^{-1}\frac{D}{N-D}(Q^{-D}-1)R_v,\\
 R_{Fv}&=z\frac{d-D}{D+1}(1-Q^{D+1})R_v,\\
 R_{Kv}&=xQ^{-D}R_v.
 \end{split} \tag{11}
\]
Their displayed order is part of the identity. For example
\(\binom d{a-1}/\binom da=a/(N-a)\), while
\(\binom d{a+1}/\binom da=(d-a)/(a+1)\).

At this fixed root \(e^{hN}=1\). Hence both quotients in (11)
have the following exact integral forms:
\[
 \boxed{\begin{split}
 \widehat E&=
      h z^{-1}D\int_0^1 e^{c_0t}Q^{-tD}\,dt,\\
 \widehat F&=
      -h z(d-D)\int_0^1 e^{ht}Q^{tD}\,dt,\\
 \widehat K&=xQ^{-D}.
 \end{split}} \tag{12}
\]
Indeed
\[
 \frac{Q^{-D}-1}{N-D}
       =h\int_0^1e^{ht(N-D)}dt,\qquad
 \frac{1-Q^{D+1}}{D+1}
       =-h\int_0^1e^{ht(D+1)}dt.
 \tag{13}
\]
These identities hold on every physical monomial, including both
endpoints. They are not estimates obtained by replacing an inverse
Euler operator by its principal value. Every clock rotation in
(12) moves an argument by \(O(N^{-1})\).

Apply (12) separately to the heads and use the original ordered
coproduct. The binomial-conjugated suffix Casimirs
\(\widehat\Omega_i\), for the intervals \([i,r]\), are exact
operators on the weighted input polynomials. Dehomogenization is
literal:
\[
 D_r=T-\sum_{i<r}D_i,\qquad
 Q^{tD_r}=Q^{tT}\prod_{i<r}Q^{-tD_i}.
 \tag{14}
\]
All scalar \(Q^{tT}\) and all intermediate degree changes in ordered
products are retained. Multiplication by \(z_i/z_j\) becomes the
actual ratio \(c_j\xi_i/(c_i\xi_j)\). On the chosen nonzero-coordinate
polydisks every resulting coefficient is analytic and bounded.

More specifically, each such Casimir is a finite sum of terms
\[
 \int_{[0,1]^k} a_{\nu,N}(\xi,t)\,
       N^{-|\nu|}\partial_\xi^\nu
                 f(\Phi_{N,t}\xi)\,dt,\qquad |\nu|\le2.
 \tag{15}
\]
The coefficients, and their fixed derivatives on smaller domains,
are uniformly bounded and analytic in \(\epsilon\) at zero, with
\(\sigma\) on its stated compact real interval.
\(\Phi_{N,t}\) is a diagonal clock rotation; its displacement is
bounded by \(C\epsilon\), uniformly on the compact integration cube.
Formula (15) follows by multiplying the literal expressions (12);
derivatives of their coefficients contribute terms of lower order.
There is no unbounded radial integration or discarded cap in (15).

## 3. Reverse finite triangular propagation

Use the exact suffix notation of M:
\[
 \Omega_i=\Omega_{[i,r]},\qquad
 D_i=\Omega_i-K_i^{-1}\Omega_{i+1}.
 \]
The expansion with its original operator order is
\[
 D_i=K_t[F_iE_i+q(K_i-K_i^{-1})]
                      +F_iE_t+K_i^{-1}F_tE_iK_t.
 \tag{16}
\]
For an output index \(\alpha\), put \(k_i(\alpha)=xQ^{-\alpha_i}\).
The only term in \(D_i|\alpha\rangle\) that raises low degree
\(|\alpha|\) is
\[
 a_i^+(\alpha)|\alpha+e_i\rangle,\qquad
 a_i^+(\alpha)=
       (1-Q^{\alpha_i+1})(Q^{-T+|\alpha|}-1).
 \tag{17}
\]
Every other column \(\gamma\) has \(|\gamma|\le|\alpha|\).
This includes all diagonal and degree-preserving transfers; neither
endpoint is dropped.

The original matrices \(A,\Omega_i\) are symmetric. Transpose the
exact column equation in M, then use the literal binomial map on
its input variable. If \(U_\alpha(\xi)=[\rho^\alpha]U_N\), the
result is
\[
 \begin{split}
 c_i a_i^+(\alpha)U_{\alpha+e_i}
   ={}&[\widehat\Omega_i-k_i(\alpha)^{-1}
                         \widehat\Omega_{i+1}]U_\alpha\\
     &-\sum_{|\gamma|\le|\alpha|}
          (D_i)_{\gamma\alpha}c^{\gamma-\alpha}U_\gamma .
 \end{split} \tag{18}
\]
This is an exact row of the actual finite matrix. Every choice of
predecessor is compatible because they come from the same matrix,
not from an assumed integrable approximate system.

Choose \(\delta>0\) small depending on \(I\) and the input domains.
For \(|\alpha|\le\delta N\),
\[
                  |a_i^+(\alpha)|\ge c(\alpha_i+1)/N.
 \tag{19}
\]
The corresponding highest term in the output generating equation is
\[
 \frac{c_i}{\rho_i}(1-T_i)(CT_{\rm all}-1)U_N,
 \qquad T_i:\rho_i\mapsto Q\rho_i.
 \tag{20}
\]
For the new degree-\(n\) coefficient \(v_\gamma\) of a logarithm
divided by \(N\), its diagonal multiplier is therefore
\[
             c_iN(1-Q^{\gamma_i})(CQ^n-1),
             \qquad |\,\cdot\,|\ge c\gamma_i.
 \tag{21}
\]
Other terms involve lower output degrees, as in (18). Apparent
negative powers in (20) have the exact endpoint differences that
make the complete row analytic.

## 4. Uniform analytic low-degree estimate and the whole cap

Here is the analytic argument for (18), including the new second
input derivatives in (15). It proves an actual kernel estimate,
not just existence of a formal principal solution.

By (10) the exact boundary is a unit on the enlarged input domain
for large \(N\). Expand the formal output logarithm
\[
 V_N=N^{-1}\log[N^{p+1/2}U_N]
 \tag{22}
\]
there, starting with that boundary branch, and first retain output
degree at most \(k_N=\lfloor\delta N\rfloor\).
The division in (21) is bounded by a constant times \(1/\gamma_i\).
Multinomial majorants, with \(z=\sum_i|\rho_i|\), turn these
divisions into the usual \(1/n\) at output degree \(n\).

Use a nonnegative scalar variable \(y\) to majorize input
displacements inside the larger input polydisk. Enlarge constants
to dominate every coefficient and every arc in (15), and put
\[
                  \varphi_\epsilon(y)
                    =e^{L\epsilon}(1+y)-1.
 \tag{23}
\]
An \(O(\epsilon)\) clock arc is dominated by this map. Its scaled
first difference is dominated by
\(L(1+y)F'(\varphi_\epsilon(y))\) for a positive analytic
majorant \(F\). The following elementary inequality pays the
additional derivatives:
\[
              \epsilon F''(y)
                  \preccurlyeq C F'(\varphi_\epsilon(y)).
 \tag{24}
\]
Indeed the Taylor expansion of \(F'(y+a)\), with nonnegative
coefficients, contains \(aF''(y)\), and
\(\varphi_\epsilon(y)-y\) coefficientwise dominates \(c\epsilon\).
The same argument handles any of the finitely many input coordinate
directions after increasing \(L,C\).

Conjugating (15) by \(e^{NV}\) gives analytic combinations of first
input derivatives of \(V\), clock increments \(N\Delta V\), and
\(\epsilon\) times second input derivatives of \(V\).
For example two scaled derivatives give a product of two first
derivatives plus \(\epsilon\partial^2V\).
Thus (24) is exactly the missing derivative budget, rather than
an estimate on an unscaled second derivative.

Pad a degree-\(n\) input majorant by \(\varphi_{n\epsilon}\).
Enlarge \(L\) once to include the combined displacements of every
arc and the extra Taylor translation in a whole application of
(15). That complete application then consumes one padding step
when an output degree is raised. In a product of previously available
coefficients, its required padding is bounded by the new total
degree: \(\max(n_j+1)\le\sum n_j+1\). Boundary factors have degree
zero and obey the same rule. Taking \(\delta\) smaller ensures
that all these padded domains remain inside the enlarged input
sector. This also controls a bounded continuum of arc parameters;
integration over its fixed cube only changes the majorant constant.

For completeness a positive implicit first-order majorant can be
chosen in the form
\[
 \begin{split}
 U_z=B(y)\{&
 1+U+(1+U_y)^2+
       e^{B(y)((1+y)U_y+zU_z)}\\
 &+zU_z+zU_z^2
                 e^{B(y)((1+y)U_y+zU_z)}\},
 \qquad U(y,0)=U_0(y).
 \end{split} \tag{25}
\]
Here \(B,U_0\) are fixed nonnegative analytic series dominating
the boundary logarithm and the finitely many operator coefficients.
The squared input gradient accounts for (15). Every dependence on
the unknown \(U_z\) has a factor \(z\), so (25) can be solved for
\(U_z=\mathscr H(y,z,U,U_y)\) on a neighborhood of the initial
line. An actual analytic solution follows from its characteristic
ordinary differential equations
\[
 \dot y=-\mathscr H_P,\qquad
 \dot U=\mathscr H-P\mathscr H_P,\qquad
 \dot P=\mathscr H_y+\mathscr H_U P .
 \tag{26}
\]
The initial projection has derivative one. Analytic ODE existence
and the inverse function theorem give a common small bidisk.
Its coefficient recursion is nonnegative and dominates the exact
degree-by-degree recursion (18),(21), with the padding just proved.
Thus the entire low logarithm has a uniform analytic bound.

The same construction controls errors. Subtract two conjugated rows.
An exponential difference factors as its increment difference times
a bounded analytic multiplier. A second-derivative difference is
\(\epsilon\partial^2\) of the error and is treated by (24).
After removal of the diagonal (21), the positive linear error
majorant has the form
\[
 E_z=B_1(E+E_y)+zB_2E_z+\epsilon^jB_3,\qquad
 E(y,0)=\epsilon^jE_0(y).
 \tag{27}
\]
All coefficients are bounded analytic series on smaller domains.
Invert \(1-zB_2\) and use the linear instance of (26).
Its solution is \(\epsilon^j\) times a uniformly bounded analytic
function. This gives stability for \(j=1,2\), without a high-degree
clock inverse or an uncontrolled analytic-radius loss.

The full finite cap is recovered separately. M supplies an
\(e^{C_1N}\) bound on the actual matrix coefficients divided by
\(a_{00}^{(r)}\). Multiplying by the finitely many binomial factors,
summing the polynomially many physical indices and evaluating on
the fixed input polydisk preserves an \(e^{C_2N}\) bound.
The harmless \(N^{p+1/2}\) normalization is included in it.
The exponential of the bounded low logarithm has the same type of
bound on a fixed output polydisk and agrees with the actual
polynomial through degree \(k_N\). Cauchy's estimate for their
remaining coefficients gives, on a smaller output polydisk,
\[
 C(k_N+1)^{s-1}e^{C_3N}
       \frac{(r_0/R_0)^{k_N+1}}{(1-r_0/R_0)^s}.
 \tag{28}
\]
Choose \(r_0/R_0\) after \(\delta\). This makes (28) exponentially
smaller than \(e^{N\Re V_N}\), whose reciprocal has an
\(e^{C_4N}\) bound from the low logarithm. Consequently the
actual kernel is a unit on the resulting output-input domain,
and its full logarithm obeys the same estimates. All original
coefficients above the low band have been retained in this step.

## 5. Phase, transport and the actual relative estimate

The principal equations are obtained from the exact rows (18) by
the following unambiguous substitution: on the output put
\(T_i=e^{c_0\rho_iS_{\rho_i}}\); in the weighted input use the
principal symbols of (11), with the homogeneous last momentum
\(\sigma-\sum_i\xi_iS_{\xi_i}\). Keep the displayed order until
this commuting principal substitution is made. Initialize
\[
                         S(0,\xi;\sigma)=\psi(\xi;\sigma).
 \tag{29}
\]
This defines the selected system; it is not an arbitrary Casimir
branch.

The estimates of Section 4 construct its analytic compatible
solution as follows. Every fixed output coefficient of the exact
low logarithm has a limiting recursion from (21), with nonzero
diagonal proportional to its new index. Starting with (29), this
determines it uniquely. The uniform analytic majorant makes these
limits a convergent analytic function \(S\), uniformly in the
stated real parameter interval. Compatibility of all the rows is
inherited from their exact finite identities. This argument also
gives the coefficientwise analytic dependence on \(C\).

Substitution of \(e^{NS}\) into the exact equations leaves a
conjugated residual \(O(\epsilon)\), including the
\(\epsilon\partial_\xi^2S\) terms and every physical half-shift.
The bound is uniform on smaller domains by Cauchy. Equation (27)
with \(j=1\) proves \(V_N-S=O(\epsilon)\).
The uniformly bounded functions \(N(V_N-S)\) now have coefficient
limits determined by the linear first transport recursion, with
boundary \(\log B_0\). Uniqueness at each new output coefficient
and the analytic majorant give a compatible analytic function
\(\alpha(\rho,\xi;\sigma)\).
Its constant exponential is fixed by (9), not freely chosen.

Inserting \(S+\epsilon\alpha\) cancels the first two orders of
every exact row. Taylor expansion of their short arcs and scaled
derivatives has uniform \(O(\epsilon^2)\) remainder on smaller
domains; the order-two operators in (15) cause no difficulty
because \(S,\alpha\) have uniform analytic derivative bounds there.
The boundary error is \(O(\epsilon^2)\) by (10). Apply (27) with
\(j=2\), then (28), to obtain
\[
 \boxed{\quad
 U_N(\rho,\xi)=N^{-p-1/2}
       e^{N S(\rho,\xi;\sigma)}
       \mathcal A(\rho,\xi;\sigma)(1+O(N^{-1})),
 \qquad \mathcal A=e^\alpha\ne0.
 \quad} \tag{30}
\]
Every fixed output and input derivative follows on smaller
domains. This is uniform analyticity in those variables. It does
not claim a uniform complex-\(C\) neighborhood merely from the
normal-family argument on the physical real arc.

## 6. The initialized full mixed rank

The phase in (30) has a nondegenerate full mixed Hessian, which
can be checked explicitly at the output axis. All quantities in
this section are principal quantities with
\(C=e^{-c_0\sigma}\); the actual \(\tau=\sigma-\epsilon\)
correction already belongs to (9) and the transport.

Use B's two saddles at \(\tau=\sigma\), called \(t,u\), and set
\[
 p_i=\frac{u\xi_i}{t+u\xi_i},\quad
 P=\sum_{i=1}^s p_i=t\phi'(t;C),\quad
 p_r=\sigma-P,\quad u=\frac{p_r}{1-p_r}.
 \tag{31}
\]
These are the boundary input occupation momenta, by differentiation
of its actual stationary phase. Put
\[
 A_i=e^{-c_0p_i},\quad R=e^{-c_0p_r}
       =\frac{C Y_B(t)}{1-t},\quad
 D_*=-\frac{(1-t)^2R(R-1)}{t c_0(C-1)C}.
 \tag{32}
\]
For a weighted head the principal symbols from (11) are
\[
 E=z^{-1}\frac{p}{1-p}(e^{-c_0p}-1),\quad
 F=z\frac{1-p}{p}(1-e^{c_0p}),\quad K=-e^{-c_0p}.
 \tag{33}
\]
At the boundary, (31) turns these, for \(i<r\), into
\[
 E_i=\frac{c_i^0u}{t z_r}(A_i-1),\qquad
 F_i=\frac{t z_r}{c_i^0u}(1-A_i^{-1}),\qquad
 c_i^0=(-1)^{r-i}.
 \tag{34}
\]
The last head has the same formulas with \(t=1,c_r^0=1\).
In the ordered suffix coproduct the alternating signs telescope.
Writing \(B_i=\prod_{k=i}^r A_k\), direct multiplication gives
\[
 \Omega_i=c_i^0\left[
       \frac{(1-t)^2R-1-t^2}{t}
       -\frac{(1-t)^2R(R-1)}{t B_i}\right].
 \tag{35}
\]
For \(i=r\) this is \(-2\), as it must be.

At output vacuum the diagonal part of (16) is \(O(\epsilon)\).
The leading coefficient in its raising row is
\(-c_0(C-1)c_i^0\), while its right side is
\(\Omega_i+\Omega_{i+1}\). Since \(B_1=C\), (35) gives
\[
 \boxed{\quad
 S_{\rho_i}(0,\xi)=
    D_*\left(\prod_{k=1}^i A_k-\prod_{k=1}^{i-1}A_k\right).
 \quad} \tag{36}
\]
This fixes the physical signs as well as the branch.

Let \(Y=Y_B(t)\). Summing (36), and using
\(e^{-c_0P}=(1-t)/Y\), gives
\[
 \sum_i S_{\rho_i}(0,\xi)
    =F(P)=\frac{(CY-1+t)(Y+t-1)}{t c_0(C-1)}.
 \tag{37}
\]
The boundary quadratic in B gives
\[
 Y=1+t-\frac{C+1}{C-1}t^2+O(t^3),\qquad
 P=\frac2{c_0}t+O(t^2).
 \]
Consequently
\[
 F(P)=\frac2{c_0}
            +\frac{C+1}{2(C-1)}P+O(P^2),\qquad F'(0)\ne0
 \tag{38}
\]
uniformly in the strict upper chamber.

For fixed nonzero small \(P\), variations of the \(p_i\) with
\(\sum p_i=P\) give rank \(s-1\) in the prefix-product differences
in (36): the cumulative sums recover each prefix product, whose
logarithmic derivatives are triangular and nonzero.
Their output sum is zero. Equation (38) supplies the remaining
radial rank. Hence the map \(p\mapsto(S_{\rho_i})_i\) is invertible
for sufficiently small nonzero \(P\) with bounded ratios \(p_i/P\).

Finally the actual input map in these variables is
\[
 \xi_i=k(P)\frac{p_i}{1-p_i},\qquad
 k(P)=t(P)/u(P)=\frac{P}{ab}(1+O(P)),
 \quad a=2/c_0,\quad b=\sigma/(1-\sigma).
 \tag{39}
\]
Its Jacobian determinant is exactly
\[
 k(P)^s\prod_i(1-p_i)^{-2}
       \left[1+\frac{k'(P)}{k(P)}
                         \sum_i p_i(1-p_i)\right]
        =2\left(\frac{P}{ab}\right)^s(1+O(P)).
 \tag{40}
\]
It is nonzero on the chosen small balanced input domains.
Combining (36)--(40) proves
\[
                   \det S_{\rho\xi}(0,\xi)\ne0.
 \tag{41}
\]
After shrinking the output neighborhood this remains nonzero.
The local canonical nondegeneracy is therefore initialized by the
actual contracted boundary, rather than assumed for the suffix system.

## 7. Original normalization and scope

Combining (5) and (30) gives the actual full kernel
\[
 v(w)A_N^{(r)}c_T(z)=
 a_{00}^{(r)}(w_rz_r)^T\binom dT\,
 N^{-p-1/2}e^{N S(\rho,\xi;\sigma)}
          \mathcal A(\rho,\xi;\sigma)(1+O(N^{-1})).
 \tag{42}
\]
It includes the complete physical matrix, its true binomial input,
its width-dependent vacuum normalization and every finite cap.
The \(N-1\) scalar and clock corrections are included in (9),(12)
and the transport. The inactive monomial input directions have not
been treated as independent Bessel saddles.

This is a fixed-root, physical-integer-degree theorem on a specified
small input sector and a small output neighborhood of the vacuum.
It does not estimate the exterior braid/turnover factors of the
original opposite kernel, its inverse Cartan coupon, its meridian
normal or its closed source. It does not identify this local chart
with a chosen geometric representation or continue the degree to a
nonreal total moment. Those are distinct composition and source
questions.

Complete proof directs:

* **M:** [research_fixed_width_gauss_monomial_sector_kernel.md](research_fixed_width_gauss_monomial_sector_kernel.md),
  482 lines, SHA256
  bf9bd5c282d478c9cfff7c93da5546a76177315724292c33dea528d5e1dd729f.
* **B:** [research_fixed_width_gauss_coherent_boundary.md](research_fixed_width_gauss_coherent_boundary.md),
  383 lines, SHA256
  03e0969c7b7c80d80b6cdb728661f125c15fee33b806dbd81f100bbb89b417c4.

The new short-arc binomial identities, reverse propagation estimate,
normalization conversion and initialized full mixed-rank calculation
are proved inline. Only written mathematics and text/hash operations
are used; frozen and public files are unchanged.

Author freeze protocol: the entire matching final was freshly reread
nontruncated. The complete direct M was freshly read in full in this
author sequence; the complete matching B whole read was retained fresh
and unchanged from the immediately preceding author/formal sequence.
Every used implication was checked, and all three hashes were renewed.
Independent matching review and parent adoption remain separate.
