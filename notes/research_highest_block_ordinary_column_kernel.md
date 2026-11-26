# An actual ordinary-column unit from an analytic highest-block seed

Private written proof, 19 November 2026.

At the fixed root, physical highest-block completion propagates an
already estimated coherent seed through a small ordinary first-head
output disk. The phase is selected by the exact capped lowering row.
The proof first controls its low logarithm and then recovers every
remaining physical coefficient. The seed estimate is an explicit
hypothesis; no estimate for an unspecified knot seed is inferred.

The complete directs are H and A, pinned below. H supplies the actual
completion and its coefficient norm bound. A supplies the analytic
padding method for finite clock rotations. The operator rows, their
principal symbols, the noncharacteristic equation, and their application
to this different completion are proved here.

## 1. The precise gauge and seed assumptions

Fix the number \(r\ge1\) of remaining heads. Put
\[
 c=2\pi i,\quad \varepsilon=N^{-1},\quad Q=e^{c\varepsilon},
 \quad x=-e^{-c\varepsilon/2},\quad d=N-1,\quad
 f_a=\prod_{j=1}^a(1-Q^j).
 \tag{1}
\]
All assertions below are at \(M=1\). On each physical head,
\[
 K w_a=xQ^{-a}w_a,\quad
 E w_a=(Q^{-a}-1)w_{a-1},\quad
 Fw_a=(1-Q^{a+1})w_{a+1},
 \tag{2}
\]
with both outward arrows zero. Let \(E,K,F\) denote the ordered
remaining-head coproducts. The coefficient occupation basis is
orthonormal when an operator norm is used.

For an actual remaining-head matrix \(H_N\), define its kernel by
\[
 h_N(z,w)=\sum_{\alpha,\beta\in\{0,\ldots,d\}^r}
       z^\alpha(H_N)_{\alpha\beta}
       \prod_{j=1}^r\binom d{\beta_j}w^\beta .
 \tag{3}
\]
Thus the remaining output is physical monomial output and the
remaining input has ordinary binomial weights. Choose nested
polydisks with compact inclusions in \(\mathbb C^{2r}\), with
all \(z_j\ne0\) on their closures. All data below are holomorphic
on the largest of these polydisks, denoted \(\mathcal U\).
Smaller polydisks provide fixed analytic buffers.

Assume that \([K,H_N]=0\), and that there are nonzero scalars
\(\gamma_N\), holomorphic functions \(S,a\), and a constant \(C\)
independent of \(N\), such that
\[
 a\ne0,\qquad
 h_N=\gamma_N e^{NS}a(1+\rho_N),\quad
 \sup_{\mathcal U}|\rho_N|\le C/N,\qquad
 \|H_N\|\le |\gamma_N|e^{CN}.
 \tag{4}
\]
The functions \(S,a\) and their analytic bounds are fixed as \(N\)
varies. The scalar \(\gamma_N\), including any specified physical
scalar, is retained. A uniform version permits parameters ranging
over a compact analytic family with these same bounds. Exact integer
degree preservation may additionally be imposed on \(H_N\).

Let \(W_{H_N}\) be H's unique actual total \(E,F,K\) intertwiner
with physical highest block \((W_{H_N})_{00}=H_N\), and put
\[
 C_{a,N}=(W_{H_N})_{a0},\qquad
 \Psi_N(t,z,w)=\sum_{a=0}^d t^a\mathcal K_{C_{a,N}}(z,w).
 \tag{5}
\]
The new first head has input occupation zero and **ordinary physical
output** \(t^a\). In particular (5) has neither a factor \(f_a^{-1}\)
nor an additional first-head binomial weight.

There are a fixed \(t_0>0\) and a smaller remaining-head polydisk
on which
\[
 \boxed{\quad
 \Psi_N=\gamma_N e^{NV}\,b\,(1+R_N),\qquad
 b\ne0,\qquad \sup|R_N|\le C/N.
 \quad}\tag{6}
\]
Here \(V,b\) are holomorphic, \(V(0,z,w)=S\), and
\(b(0,z,w)=a\). The actual finite polynomial is consequently a
unit there for sufficiently large \(N\). Every fixed derivative
of the normalized remainder \(R_N\) in \(t,z,w\) is \(O(N^{-1})\)
on smaller buffered domains. This last statement is not a ratio
claim for derivatives of (6) whose leading derivative vanishes.

## 2. Exact finite column and its nilpotent Euler row

On remaining-head matrices set
\[
                    \mathcal L(X)=K^{-1}[E,X].
 \tag{7}
\]
If \(A(X)=K^{-1}EX\), \(B(X)=K^{-1}XE\), then
\(AB=QBA\). The actual relation \(E^N=0\), including all physical
caps, gives \(A^N=B^N=0\). The root quantum binomial identity
therefore gives \(\mathcal L^N=(A-B)^N=0\), for every \(N\),
including even and composite levels. H's first-column recursion is
\[
 C_{0,N}=H_N,\qquad
 C_{a,N}=-\frac{\mathcal L C_{a-1,N}}{Q^{-a}-1}
  =\frac{(-1)^aQ^{a(a+1)/2}}{f_a}\mathcal L^aH_N.
 \tag{8}
\]
Thus, writing \(E_N(X)=\sum_{a=0}^dX^a/f_a\), the operator-valued
column is exactly
\[
       \sum_{a=0}^dt^aC_{a,N}=E_N(Qt\mathcal L)^{-1}H_N.
 \tag{9}
\]
The inverse in (9) is its finite nilpotent inverse, not a scalar
kernel inverse. Equivalently, its kernel satisfies
\[
             \Psi_N(t/Q)-\Psi_N(t)+t\mathscr L_N\Psi_N(t)=0.
 \tag{10}
\]
The coefficient at \(t^N\) is zero because \(\mathcal L^NH_N=0\).
Hence (10) is the full capped identity, not a low-degree replacement.

## 3. Literal remaining-head coherent operators

Write \(D_{z_j}=z_j\partial_{z_j}\), and let
\(T_{z_j}f=f(z_1,\ldots,Qz_j,\ldots,w)\); use analogous
notation for \(w\). Direct comparison in (3) gives left actions
\[
 E_j^L=z_j^{-1}(T_{z_j}^{-1}-1),\qquad
 K_j^L=xT_{z_j}^{-1},
 \tag{11}
\]
and right actions
\[
 \begin{split}
 E_j^R&=w_j\frac{d-D_{w_j}}{D_{w_j}+1}
                      (Q^{-D_{w_j}-1}-1),\\
 K_j^R&=xT_{w_j}^{-1}.
 \end{split}\tag{12}
\]
For (12), set the new input index to \(b=j+1\) and use
\(\binom d{j+1}/\binom dj=(d-j)/(j+1)\).
The factor \(d-D\) retains the top input cap. There is no inverse
Euler singularity: the exact short-arc expressions are
\[
 E_j^L=-c\varepsilon z_j^{-1}D_{z_j}
                    \int_0^1T_{z_j}^{-v}\,dv,\qquad
 E_j^R=-c\varepsilon w_j(d-D_{w_j})
                    \int_0^1Q^{-v}T_{w_j}^{-v}\,dv.
 \tag{13}
\]
Both formulas hold at every physical endpoint. Define the ordered
total actions
\[
 E^L=\sum_jE_j^L\prod_{k>j}K_k^L,\quad
 E^R=\sum_jE_j^R\prod_{k>j}K_k^R,\quad
 \mathscr L_N=x^{-r}\prod_jT_{z_j}\,(E^L-E^R).
 \tag{14}
\]
Products on distinct heads commute; the displayed order of a
coefficient and a same-head shift is kept. Equation (14) is exactly
\(\mathcal K_{\mathcal L X}=\mathscr L_N\mathcal K_X\).
It consists of a bounded finite number of short clock arcs and
first derivatives with coefficients of order \(\varepsilon\),
or the bounded combinations \(\varepsilon(d-D)\).

For principal momenta \(p_j=z_jV_{z_j}\),
\(q_j=w_jV_{w_j}\), put
\[
 \begin{array}{ll}
 k_j^L=-e^{-cp_j},&e_j^L=z_j^{-1}(e^{-cp_j}-1),\\
 k_j^R=-e^{-cq_j},&
 e_j^R=w_j(1-q_j)(e^{-cq_j}-1)/q_j.
 \end{array}\tag{15}
\]
The last quotient has its entire value \(-c\) at \(q_j=0\).
The principal symbol of (14) is
\[
 \ell(z,w,dV)=\left(\prod_jk_j^L\right)^{-1}
 \left(\sum_je_j^L\prod_{k>j}k_k^L
       -\sum_je_j^R\prod_{k>j}k_k^R\right).
 \tag{16}
\]
In particular the remaining Cartan symbol is a unit. No smallness
of these remaining-head momenta is assumed.

## 4. The selected phase and transport

Equation (10) gives the principal initial-value problem
\[
 e^{-ctV_t}-1+t\ell(z,w,dV)=0,\qquad V|_{t=0}=S.
 \tag{17}
\]
The branch at \(t=0\) is fixed equivalently by
\[
 V_t=-\frac1{ct}\log(1-t\ell(z,w,dV)),
             \qquad V_t|_0=\ell(z,w,dS)/c.
 \tag{18}
\]
Its right side is analytic at \(t=0\). It involves remaining-head
derivatives, not \(V_t\); thus the initial surface is
noncharacteristic with coefficient one. After shrinking \(t_0\),
\(1-t\ell\) is a unit on the buffered domain.

The first transport is also fixed by the actual row. Define the
linear differential operator \(\mathscr L_{1,V}\) by Taylor
expanding the explicit operators (11)--(14):
\[
 e^{-NV}\mathscr L_N(e^{NV}b)
   =\ell(z,w,dV)b+\varepsilon\mathscr L_{1,V}b
                              +O(\varepsilon^2).
 \tag{19}
\]
This is an unambiguous finite Taylor rule, with \(x=-e^{-c\varepsilon/2}\)
and \(\varepsilon d=1-\varepsilon\) retained. It is first order
in \(b\); its coefficients involve derivatives of \(V\) of order
at most two. All arc parameters lie in fixed compact cubes, so
the remainder is uniform on smaller domains. The equation for \(b\) is
\[
 b_t=\frac c2(V_t+tV_{tt})b
            +c^{-1}e^{ctV_t}\mathscr L_{1,V}b,
                     \qquad b|_0=a.
 \tag{20}
\]
Indeed the first-head shift contributes
\(e^{-ctV_t}[-ctb_t+\frac{c^2}2(tV_t+t^2V_{tt})b]\)
at order \(\varepsilon\). This proves (20), including its half-step
and \(d=N-1\) corrections. It is a linear analytic transport
equation on the phase (18). Its initialized solution is a unit
after shrinking the same domain.

## 5. Low logarithm, stability, and recovery of the entire cap

Here are the estimates that turn (17)--(20) into a statement about
the actual finite kernel. Choose \(0<\delta<1/2\) sufficiently small
for all remaining-head analytic buffers and put
\(k_N=\lfloor\delta N\rfloor\). The exact seed is a unit on a
buffered polydisk for large \(N\). Choose its logarithm there and
formally expand \(V_N=N^{-1}\log(\Psi_N/\gamma_N)\) in \(t\).
Its initial value is
\[
                 V_N(0)=S+\varepsilon\log a+O(\varepsilon^2).
 \tag{21}
\]
In the conjugated equation (10), the coefficient of the new
degree-\(n\) logarithm is exactly \(N(Q^{-n}-1)\). For
\(1\le n\le k_N\),
\[
                   |N(Q^{-n}-1)|\ge4n.
 \tag{22}
\]
Every other term at this degree uses lower \(t\) degrees. In
particular \(t\mathscr L_N\) uses degree at most \(n-1\);
the nonlinear part of the first exponential contains at least two
positive \(t\) degrees. Division therefore costs only \(C/n\).

For clarity, the analytic majorant argument is recorded explicitly.
Use a positive variable \(y\) to majorize displacements in all
remaining coordinates, and choose
\(\varphi_\varepsilon(y)=e^{L\varepsilon}(1+y)-1\).
Increase \(L\) to cover one entire application of (14), including
its finite products of clocks and its short arcs. Conjugated clock
increments \(N\Delta V_N\) are bounded by first derivatives on
this padded domain; the scaled derivatives in (13) give bounded
first-gradient factors. Pad a degree-\(n\) majorant by
\(\varphi_{n\varepsilon}\). An application raising the degree
uses at most one extra padding step. Products use no more than
their total degree, so \(n\le\delta N\) stays inside the original
buffer after \(\delta\) is fixed small enough.

After (22), a positive implicit majorant may be enlarged to
\[
 U_t=B(y)\{1+U+(1+U_y)e^{B(y)(1+y)U_y}
               +tU_t^2e^{B(y)tU_t}\},\qquad U|_0=U_0(y).
 \tag{23}
\]
Here \(B,U_0\) are fixed positive analytic majorants for all initial
data and coefficients. The final term covers the nonlinear
first-head exponential after its linear term is removed. Its
dependence on the unknown \(U_t\) has a factor \(t\), so the
analytic implicit function theorem solves (23) for
\(U_t=\mathcal H(y,t,U,U_y)\) near the initial line.
Analytic characteristics solve this first-order equation: use
\(\dot y=-\mathcal H_p\),
\(\dot U=\mathcal H-p\mathcal H_p\), and
\(\dot p=\mathcal H_y+\mathcal H_U p\).
The initial projection is the identity. Local analytic ODE
existence and inversion give a common domain. Its positive
coefficient recursion dominates every low coefficient of \(V_N\).
This is the short-arc padding argument of A, here with only first
remaining-head derivatives.

Subtracting two conjugated rows gives a linear positive error
majorant of the form
\[
 E_t=B_1(E+E_y)+tB_2E_t+\varepsilon^jB_3,
                       \qquad E|_0=O(\varepsilon^j).
 \tag{24}
\]
The \(B_i\) are uniformly bounded analytic positive series on
smaller domains. Clock-exponential differences factor by their
increment differences; (22) and the same padding apply. Invert
\(1-tB_2\) and use the linear characteristic equation. The error
is \(O(\varepsilon^j)\) on a fixed smaller domain.

The degreewise limits in the bounded low recursion give (18).
Its first correction gives (20). Taylor substitution of
\(V+\varepsilon\log b\) in the exact row has
\(O(\varepsilon^2)\) conjugated residual, with the same boundary
error by (21). Equation (24), for \(j=2\), proves
\[
       V_N^{\mathrm{low}}=V+\varepsilon\log b
                                +O(\varepsilon^2)
 \tag{25}
\]
on a smaller domain, up to an exponentially small truncation tail.
The principal and transport Taylor tails beyond \(k_N\) are
exponentially small there by the fixed analytic radius. Thus this
argument does not require convergence of a merely formal WKB series.

Finally H's whole coefficient bound and (4) give
\(\|C_{a,N}\|\le|\gamma_N|e^{C_1N}\) for every \(a<N\).
Evaluation of (3) on a fixed remaining-coordinate compact adds
only an \(e^{C_2N}\) factor: there are polynomially many indices,
binomial sums are at most \(2^{rd}\), and coordinate powers have
fixed bases. Hence the entire actual polynomial \(\Psi_N/\gamma_N\)
is bounded by \(e^{C_3N}\) on a fixed \(t\) disk. The exponential
of the bounded low logarithm has the same type of bound and agrees
with that polynomial through degree \(k_N\). On a smaller disk,
their difference is bounded by
\[
       C e^{C_4N}
          \frac{(t_0/R_0)^{k_N+1}}{1-t_0/R_0}.
 \tag{26}
\]
Choose \(t_0/R_0\) only after the cap constants and \(\delta\).
Then (26) is exponentially small even relative to
\(e^{NV}b\), whose reciprocal costs at most \(e^{C_5N}\).
Combining (25),(26) proves (6). Cauchy's formula on buffered
domains proves the stated fixed coherent derivatives.

## 6. Exact gauge and source limitations

All physical first-head coefficients, including its upper cap,
occur in (5),(26). The remaining-head caps occur in (3),(11)--(14).
No transformed closing is introduced: H's original pointed source
still satisfies
\[
       \Phi_0(W_{H_N})=\operatorname{Tr}_U(K^{1-N}H_N).
 \tag{27}
\]
Equation (6) gives no nonzero assertion for this trace, no selected
geometric window, and no bound for its complementary regions.
It does not prove a new volume-conjecture case.

The factorial output column is a different finite kernel. If
\(Y_N(t)=\sum t^a\mathcal K_{C_{a,N}}/f_a\), its exact row is
\[
          (T_Q^{-1}-1)(1-T_Q)Y_N+t\mathscr L_NY_N=0.
 \tag{28}
\]
Its principal first-head term is \(2\cosh(ctV_t)-2\), rather
than the first-order term in (17). It cannot be included in (6)
by relabeling the output coordinate. Likewise a new first-head
ordinary-binomial weight changes the actual coefficient sum.

Even for the ordinary column, a chosen analytic seed family \(H_M\)
has the distinct exact fixed-\(q\) meridian operator row
\[
 M\Psi_M(t/Q)-(M^{-1}-t\mathcal L_M)\Psi_M(t)
                         =(M-M^{-1})H_M.
 \tag{29}
\]
Its endpoint forcing is absent only at the root. This note does
not differentiate (6) to estimate that family. H's finite
reconstruction and meridian estimates remain valid, but neither a
relative meridian unit nor its extra endpoint profile is proved here.

There is also an exact projective limitation. The reciprocal polynomial
\(\widehat\Psi_N(v)=v^d\Psi_N(v^{-1})\) satisfies
\[
 \mathscr L_N\widehat\Psi_N(v)
       +v\{Q\widehat\Psi_N(Qv)-\widehat\Psi_N(v)\}=0,
 \qquad \widehat\Psi_N(0)=\mathcal K_{C_{d,N}}.
 \tag{30}
\]
Unlike (10), its initial row is characteristic:
\(\mathscr L_N\mathcal K_{C_{d,N}}=0\). The seed needed there is
the actual extensive coefficient
\(C_{d,N}=(-1)^dQ^{d(d+1)/2}\mathcal L^dH_N/f_d\).
The local hypothesis (4) and H's upper bound do not supply its
analytic phase or a nonzero amplitude. In particular (6) is not
an estimate at ordinary-output infinity, and cannot identify a
resolved factorial-gauge flag whose transform reaches that endpoint.

Complete proof directs:

* **H:** notes/research_physical_highest_block_endpoint_coordinates.md,
  453 lines, SHA256
  deaadaa899cdb08aefbbcb1e1ca87a40f84a1ade608fceeeaba6426027bd9b1b.
* **A:** notes/research_fixed_width_gauss_coherent_sector_kernel.md,
  599 lines, SHA256
  725f11b37640abd36b89ae0f1f6f47464ed6b588ccc8b7709d32e62a502045ec.

Only written mathematics and text operations are used. Frozen
research and public manuscripts are unchanged. The complete matching
final was freshly read nontruncated after the last changes. Both
complete directs were freshly whole-read in this author sequence,
every used implication was checked, and all three pins were renewed.
Independent matching-final review and parent adoption remain separate.
