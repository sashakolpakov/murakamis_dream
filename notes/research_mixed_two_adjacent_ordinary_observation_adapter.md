# The prescribed ordinary observation of the adjacent Fourier kernel

Research deduction, 7 November 2026. The complete local Fourier
kernel is now known for two independent boundary parameters. This
note gives its exact ordinary-color and filling observations, including
all original first normals. It also proves a concrete mismatch of
critical points: at odd levels, the ordinary-complete two-boundary
adapter makes the combined phase nonstationary at the proved Fourier
center. A fixed-order Fourier jet is therefore not an automatic
ordinary closing formula.

The ordinary two-boundary source of this same-sign block is already
proved by the internal-chain theorem. The comparison here does not
reopen that result. The arbitrary-short obligation concerns the
prescribed additional context, after the exact boundary crossing
shifts have been retained.

The formulas are finite identities at every level unless a parity
restriction is stated explicitly. No numerical evaluation is used.

## 1. The exact ordinary adapter and its two full periods

Use the original Newton basis \(e_j(w)\), evaluation vector
\(v(w)=(e_j(w))_{j=0}^{D}\), and matrices
\[
 D=N-1,\qquad A_n=JM^n,\qquad
 V_N(x,y)=h(x)^TA_2^2h(y),\qquad N\ge2.
 \tag{1}
\]
The complete joint packet for \(V_N\) is
[the independent-endpoint outer theorem](research_mixed_two_adjacent_joint_outer_packet.md).
All matrix scalars, including the crossing scalar in \(M\), remain
inside (1).

The original cardinal vector is
\[
 h_j(x)=\frac1N\sum_{\nu\in\Lambda_N}
                 e^{2\pi i\nu(x-j/N)},\qquad
 \Lambda_N=\{-D/2,-D/2+1,\ldots,D/2\}.
 \tag{2}
\]
For every positively oriented horizontal period \(\Gamma\),
\[
 h(j/N)=\mathbf e_j,\qquad
              N\int_\Gamma h(x)h(x)^T\,dx=I_N.
 \tag{3}
\]
Here \(\mathbf e_j\) is a coefficient vector, not a Newton
polynomial. Equation (3) is bilinear and includes even levels:
the individual half-band functions can be antiperiodic, but their
products are periodic. This is the exact duality in
[the closing-interface theorem](research_mixed_fourier_boundary_closing_interface.md),
Section 1.

Define
\[
 \mathscr B_N(x,w)=h(x)^Tv(w)=\sum_{j=0}^{D}h_j(x)e_j(w).
 \tag{4}
\]
It is precisely the canonical entire Newton interpolation
\(\widetilde B_N\) of
[the finite Fourier-band theorem](research_newton_interpolation_finite_fourier_band.md),
equation (12). In particular it has the original Newton values
and first normals, not only its values at distinct spectral roots.

The two-free-ordinary-boundary source of this block is
\[
                 \mathscr P_N(w,z)=v(w)^TA_2^2v(z).
 \tag{5}
\]
It is already covered by
[the full internal-chain theorem](research_internal_two_crossing_chain.md),
Sections 1--3, as explained in Section 5 below. The one-sided
capped polynomial \(\mathbf e_0^TA_2^2v(z)\) also has the
separate [adjacent boundary theorem](research_adjacent_two_crossing_boundary_theorem.md).

**Proposition 1.** For arbitrary ordinary colors and all fixed
nonnegative derivative orders \(p,q\),
\[
\begin{split}
 \partial_w^p\partial_z^q\mathscr P_N(w,z)
 &=\sum_{j,k=0}^{D}e_j^{(p)}(w)e_k^{(q)}(z)
                              V_N(j/N,k/N)\\
 &=N^2\int_{\Gamma_x}\int_{\Gamma_y}
   \partial_w^p\mathscr B_N(x,w)\,
            V_N(x,y)\,\partial_z^q\mathscr B_N(y,z)\,dy\,dx .
\end{split}
 \tag{6}
\]
The two periods have arbitrary fixed heights and increasing real
orientation.

*Proof.* The first equality is the coefficient expansion, using
\(h(j/N)=\mathbf e_j\). Insert (3) on each side of \(A_2^2\)
for the second. Differentiation is of the actual finite
ordinary polynomials. No extra transpose, conjugation, reversal,
or parity scalar is introduced. \(\square\)

The physical arguments in the first line of (6) run through the
entire real grid. They are not in a sufficiently small bidisk about
\(x_0\), whose imaginary part is positive. The second line can be
put on periods through that height, but then only a small part
of each period belongs to the proved local kernel domain.

## 2. The original filling functional and a concrete two-sided path

For a fixed signed integer \(n\), put
\[
 t_{n,j}=\phi_N(R^ne_j),\qquad
 t_n=(t_{n,j})_{j=0}^{D}=(M^n)^T\mathbf e_D .
 \tag{7}
\]
The original Frobenius identity \(M^TJ=JM\) implies
\(A_n^T=A_n\), including negative powers. Therefore
\[
                         t_n=A_n\mathbf e_0.
 \tag{8}
\]
The two ordinary filling operations on (5) give the actual
four-vertex path observation
\[
\begin{split}
 \mathscr O_{n,m,N}
 &:=\phi_w\phi_z\{R(w)^nR(z)^m\mathscr P_N(w,z)\}\\
 &=t_n^TA_2^2t_m
   =\mathbf e_0^TA_nA_2^2A_m\mathbf e_0 .
\end{split}
 \tag{9}
\]
This retains the original powers in their prescribed order.
It does not assert that every such marked path gives a knot.

For explicit first-normal data, let
\[
\begin{gathered}
 \eta=(-1)^D,\quad
 \theta_r=(2r+1)\pi/N,\quad c_r=2\cos\theta_r,\quad
 d_r=4\sin^2\theta_r,\quad 0\le r<\lfloor N/2\rfloor,\\
 \lambda_r=\kappa(-1)^rq^{r+r^2},\qquad
 \alpha_r=\frac{i(D-2r)}{4\sin\theta_r},\qquad
 q=e^{\pi i/N},\quad\kappa=q^{D^2/2}.
\end{gathered}
 \tag{10}
\]
At odd levels write \(\lambda_*=\lambda_{D/2}\) for the simple
node \(-2\). The exact trace from
[original twist tomography](research_original_twist_observation_tomography.md),
equations (3)--(5), gives
\[
 t_{n,j}=
 \eta\sum_{r<\lfloor N/2\rfloor}\lambda_r^n
 \{d_re_j'(c_r)+(n d_r\alpha_r-c_r)e_j(c_r)\}
 +\mathbf1_{N\ {\rm odd}}\lambda_*^ne_j(-2).
 \tag{11}
\]
This formula applies to every signed \(n\), including zero.
In particular the derivative of the crossing itself has not
been deleted.

Define the full adapter
\[
 \mathscr K_{n,N}(x)=h(x)^Tt_n=h(x)^TA_n\mathbf e_0.
 \tag{12}
\]
Equations (6)--(11) give the two exact alternatives
\[
 \boxed{\quad
 \mathscr O_{n,m,N}
 =\sum_{j,k=0}^{D}t_{n,j}t_{m,k}V_N(j/N,k/N)
 =N^2\int_{\Gamma_x}\int_{\Gamma_y}
       \mathscr K_{n,N}(x)V_N(x,y)\mathscr K_{m,N}(y)\,dy\,dx.
 \quad}
 \tag{13}
\]
No modulus has been taken inside either contraction. Formula
(11), or equivalently the original finite matrix (12), is the
prescribed adapter. Replacing it by a favorable local evaluation
would change the observation.

The existing internal-chain identity also reduces this observation
exactly:
\[
 A_2^2=\kappa^3M^{-1}A_{-3}(M^{-1})^T,\qquad
 \mathscr O_{n,m,N}
    =\kappa^3\mathbf e_0^TA_{n-1}A_{-3}A_{m-1}\mathbf e_0 .
 \tag{13a}
\]
Indeed \(A_nM^{-1}=A_{n-1}\), while
\((M^{-1})^TA_m=JM^{-1}M^m=A_{m-1}\).
Both boundary shifts, the full signed powers, and the exact
scalar survive. The same matrix proof applies when the two
outer rows come from larger prescribed contexts. The marked
geometric interpretation must still retain the rotations and
disk frames specified by the internal-chain theorem.

## 3. An exact local-jet formula, and its growing order

The actual Fourier derivatives also give an exact finite formula,
but generally require orders growing with the level. Fix any
complex base point \(x_b\). For a coefficient column \(b\), define
\[
 \check b_\nu=\sum_{j=0}^{D}b_j e^{2\pi i\nu j/N},\qquad
 p_{b,x_b}(Z)=
 \sum_{\nu\in\Lambda_N}e^{-2\pi i\nu x_b}\check b_\nu
     \prod_{\substack{\mu\in\Lambda_N\\\mu\ne\nu}}
                   \frac{Z-2\pi i\mu}{2\pi i\nu-2\pi i\mu}.
 \tag{14}
\]
The displayed polynomial has degree at most \(D\), and
\[
             p_{b,x_b}(\partial_x)h(x)\big|_{x=x_b}=b.
 \tag{15}
\]
Indeed the operator multiplies the \(\nu\)-frequency of (2)
by \(e^{-2\pi i\nu x_b}\check b_\nu\). Finite Fourier
orthogonality then gives the \(j\)-th component \(b_j\),
with the same proof for half-integer frequencies.

Consequently, for any prescribed columns \(\ell,b\),
\[
 \ell^TA_2^2b=
 \left[
 p_{\ell,x_b}(\partial_x)p_{b,y_b}(\partial_y)V_N(x,y)
 \right]_{x=x_b,\ y=y_b}.
 \tag{16}
\]
This includes \(b=v^{(k)}(w)\), both twist adapters in (13),
and the unchanged original normal columns.

The need for a growing jet is concrete even for the cap.
For \(b=\mathbf e_0\), the coefficient of \(Z^D\) in (14) is
\[
 [Z^D]p_{\mathbf e_0,x_b}(Z)
   =\frac{e^{\pi iDx_b}(e^{-2\pi ix_b}-1)^D}
                   {(2\pi i)^D D!}.
 \tag{17}
\]
This follows by taking the \(D\)-th finite difference of
\(e^{\pi iDx_b}e^{-2\pi ijx_b}\) on the frequency nodes
\(-D/2+j\), whose spacing after multiplication by \(2\pi i\)
is \(2\pi i\). At \(x_b=x_0\) this coefficient is nonzero,
so the exact required order is \(N-1\).

Thus the fixed mixed-derivative statement of the joint kernel
theorem cannot simply be substituted into (16). It supplies
no uniform error bound for this level-dependent differential
operator. Equation (16) remains an exact identity, not an
assertion that the observation is small or nonzero.

## 4. The ordinary-complete center already moves the stationary point

There is a direct analytic obstruction to using the unchanged
Fourier center in (6). This subsection restricts to odd levels,
so that the ordinary complete color \(-2\) is a physical simple
node. At that node, the exact finite-band theorem gives
\[
 \mathscr B_N(x,-2)
 =\frac{N}
   {G_N(D/2-Nx)^2G_N(Nx)^2},
 \qquad N\ {\rm odd}.
 \tag{18}
\]
Here \(G_N\) is the original sine factorial. At even levels
\(-2\) is not a physical node, and (18) is not asserted for
the canonical adapter (4).

Near \(x_0\), both \(x\) and \(1/2-x\) stay in their regular
strips, at strictly nonzero imaginary heights. The original
shifted factorial expansion from
[uniform factorial continuation](research_factorial_uniform_halfplane_continuation.md),
equations (4)--(5), therefore proves
\[
 \mathscr B_N(x,-2)
 =\frac{1}{2N\sin\pi x}\,e^{N\beta(x)}
                                    (1+O(N^{-1})),
 \qquad
 \beta(x)=-2J(1/2-x)-2J(x).
 \tag{19}
\]
All branches and the offset \(D/2=N/2-1/2\) are retained.
The prefactor in (19) follows because that offset cancels
the factor \(2\sin\pi(1/2-x)\) in the squared first
factorial. The errors are holomorphic with fixed jets.
Sine duplication gives equivalently
\[
 \beta(x)=J(2x)-4J(x),\qquad
             e^{\beta'(x)}=\cot^2(\pi x).
 \tag{20}
\]

Write the complete Fourier action of the joint outer theorem as
\(\mathcal S(x,y)\), and set
\[
                 \Psi(x,y)=\mathcal S(x,y)+\beta(x)+\beta(y).
 \tag{21}
\]
This is the phase of the actual integrand in (6) at
\(w=z=-2\), locally near \((x_0,x_0)\), along odd levels.
The outside chirp is already in \(\mathcal S\).

**Proposition 2.** At the original Fourier center,
\[
                  \Re\Psi_x(x_0,x_0)>\log3,\qquad
                  \Re\Psi_y(x_0,x_0)>\log3.
 \tag{22}
\]
In particular it is not a stationary point of the prescribed
ordinary-complete integral. On a sufficiently small bidisk
about that center, the combined phase has no critical point.

*Proof.* Put
\[
 P=\cot(\pi x_0)=q_0-i\beta_0,\qquad
 T=\cot(\pi a_*)=u-iv.
 \tag{23}
\]
The original critical-corridor bounds are
\[
 q_0>127/100,\quad \beta_0>17/25,\qquad
 1/3<u<3/7,\quad 1/5<v<1/4.
 \tag{24}
\]
Stationarity of the two internal variables permits
differentiating the critical action without their derivatives:
\[
 \mathcal S_x=g'(a_*+x_0)-g'(x_0)+\pi i.
 \tag{25}
\]
Since \(e^{g'(z)}=1-e^{-2\pi iz}\), the exact cotangent
addition identity gives
\[
 e^{\mathcal S_x}
       =-\frac{T+P}{T+i},\qquad
 e^{\Psi_x}=-P^2\frac{T+P}{T+i}.
 \tag{26}
\]
There is no lift issue for its modulus. The rational bounds give
\[
\begin{split}
 |P|^2&>(127/100)^2+(17/25)^2>2,\\
 |T+P|&>\Re(T+P)>1/3+127/100>3/2,\\
 |T+i|^2&<(3/7)^2+(4/5)^2=1009/1225<1 .
\end{split}
 \tag{27}
\]
Thus \(|e^{\Psi_x}|>3\), proving the first inequality.
The second follows by symmetry. Holomorphic continuity
proves the last assertion. \(\square\)

This is a critical-location statement for a specified original
observation. It does not rule out its complete asymptotic, a
contributing critical point elsewhere, or a different exact
representation. In particular it does not compare the ordinary
action with a knot volume.

## 5. Existing ordinary coverage and the actual context obligation

For clarity, there is no missing ordinary packet for (5).
The internal-chain theorem, equation (14) with \(k=2,\sigma=1\),
already proves
\[
\begin{split}
 \mathscr P_N(-2\cos u,-2\cos v)
  ={}&\kappa^2\epsilon_{-3,N}N^{-3/2}
          A_{-3}(u,v)\\
   &\quad\cdot
    \exp N\left\{S_{-3}(u,v)-\frac{i}{4\pi}(u^2+v^2)\right\}
                    (1+O(N^{-1})).
\end{split}
 \tag{28}
\]
Its coefficient is nonzero, its full two-boundary strip is
controlled, and all tensor Hermite normals, including the
mixed first normal, are retained. It canonically multiplies
the original degree-two \(-3\) source by \(R^{-1}\) on each
boundary. It also proves the corresponding statement for
every fixed same-sign two-crossing run. Proposition 2 above
is consistent with (28): it explains why this ordinary packet
cannot be inferred by keeping the unchanged Fourier saddle.

For a prescribed additional short context, the exact operation
is (13), or its general-row version from (6), and equivalently
the shifted original observation (13a). The already proved
long-remainder and marked-reduction cases are not being
declared open. To use the new Fourier theorem for fixed
assignments outside those established cases, one sufficient
estimate would deform this prescribed complete cycle into a
contributing critical chain \(\mathcal C_{\rm loc}\) and its
retained complementary chain \(\mathcal C_{\rm rem}\), and prove
\[
 \left|N^2\int_{\mathcal C_{\rm rem}}
    \mathscr K_{n,N}(x)V_N(x,y)\mathscr K_{m,N}(y)\,dy\,dx\right|
 \le C N^A e^{N\{\Re\Omega_{n,m}-\delta\}},
                  \qquad\delta>0,
 \tag{29}
\]
together with a nonzero leading coefficient and the same
calibrated action \(\Omega_{n,m}\) on \(\mathcal C_{\rm loc}\).
Every connector and any residue of a chosen representation
belongs to the complementary chain. The original powers
are fixed before the limit and are not averaged. For a
general surrounding word, replace (12) by its actual
matrix row or column; (3) gives the same exact formula.

The complete physical-grid formula is exact, but its grid
is outside the local Fourier bidisk. The finite-jet formula
is exact, but its required order already grows as \(N-1\)
for a cap. Proposition 2 gives a further concrete reason
that the ordinary-complete observation cannot be settled
by keeping the same local Fourier saddle.

The new joint theorem removes the complete-source and
nonzero-coefficient hypothesis for the two-free-Fourier
adjacent block itself. The ordinary version was already
supplied by (28). Neither theorem asserts (29) for every
fixed short context or supplies its geometric calibration.
The
[finite-exception reduction](research_finite_exceptions_under_partial_fillings.md),
Sections 3--4 and 8, still requires iteration through the
prescribed partial fillings, including their degenerate
intermediate contexts. No all-but-finitely-many knot
claim follows from the local kernel alone.

## 6. The exact turned operation for every adjacent pair

There is a concrete way to pass from the covered block to a
genuinely mixed adjacent source. Put
\[
       \mathscr P_{p,q,N}(w,z)=v(w)^TA_pA_qv(z)
                         \qquad(p,q\in\mathbb Z).
 \tag{30}
\]
The exact identity, with both transpose conventions fixed, is
\[
                  A_pA_q=(M^{p-2})^TA_2^2M^{q-2}.
 \tag{31}
\]
Indeed its right side is
\(JM^{p-2}J(JM^2JM^2)M^{q-2}=JM^pJM^q\).
No scalar, inverse, or turn has been suppressed.

On a Newton coefficient column, canonical multiplication
by \(R^r\) has matrix \(M^r\), while
\(\mathsf T\mathsf R^r\mathsf T\) has matrix
\((M^r)^T=JM^rJ\). Right multiplication of a tensor
coefficient matrix by \(M^r\) is the latter operation
on its second tensor variable. Thus (31) says exactly
\[
 \mathscr P_{p,q,N}
   =(\mathsf T_w\mathsf R_w^{p-2}\mathsf T_w)
     (\mathsf T_z\mathsf R_z^{q-2}\mathsf T_z)
                               \mathscr P_{2,2,N}.
 \tag{32}
\]
Both operations are in the full Hermite algebra. The
proved preservation theorem for \(\mathsf R^r\) does
not assert preservation by the turned operation in (32);
see also the exact one-boundary distinction in
[ordinary-color transport](research_mixed_terminal_color_transform.md).

For an explicit full-source version, define
\[
              \mathscr K_{r,N}(u,w)=v(u)^TJM^rv(w).
\]
If \(f(u)=v(u)^Tc\), the original pairing gives
\(\phi_u(f\mathscr K_{r,N})=c^TM^rv(w)\).
Consequently the positive mixed pair \((3,4)\) is
\[
 \mathscr P_{3,4,N}(w,z)
   =\phi_u\phi_v\{
       \mathscr P_{2,2,N}(u,v)
                  \mathscr K_{1,N}(u,w)\mathscr K_{2,N}(v,z)\}.
 \tag{33}
\]
This keeps the raw products until the two prescribed
traces are applied.

Let \(\mathscr Q_N(u)=2T_N(u/2)+2\). The exact trace
\(\phi_N(f)=(-1)^DN^2(2\pi i)^{-1}
\oint f(u)/\mathscr Q_N(u)\,du\) therefore gives
\[
 \mathscr P_{3,4,N}(w,z)
   =\frac{N^4}{(2\pi i)^2}
       \oint_{\Gamma_u}\oint_{\Gamma_v}
       \frac{\mathscr P_{2,2,N}(u,v)
                   \mathscr K_{1,N}(u,w)\mathscr K_{2,N}(v,z)}
            {\mathscr Q_N(u)\mathscr Q_N(v)}\,dv\,du .
 \tag{34}
\]
Both contours enclose all original nodes positively.
The two signs \((-1)^D\) cancel. Double poles retain
both first normals and their mixed contribution; the
odd simple node is included. Every fixed free-color
derivative is preserved.

Equivalently, set
\(\mathscr D_{r,N}(s,w)=h(s)^TM^rv(w)\). The same exact
bilinear duality proves
\[
 \mathscr P_{3,4,N}(w,z)
   =N^2\int_{\Lambda_s}\int_{\Lambda_t}
       \mathscr D_{1,N}(s,w)V_N(s,t)
                      \mathscr D_{2,N}(t,z)\,dt\,ds .
 \tag{35}
\]
Both integration chains are complete horizontal periods.
The crossing scalars remain inside \(M,M^2\). The local
bidisk theorem for \(V_N\) does not place the combined
critical point of (35) inside that bidisk or estimate
its complete adapters.

For this particular mixed word, the original local
unaliased Gaussian and the unselected plateau sector
\(\mathscr P_{3,4,N}^{\,P}\) already exist, with their
original ordinary action \(\mathcal W_{3,4}(w,z)\);
see [the local mixed theorem](research_mixed_open_local_gaussian.md)
and [open-source stability](research_mixed_open_source_stability_reduction.md),
Section 2. One concrete remaining sufficient inequality is
\[
 \left|
 \frac{N^4}{(2\pi i)^2}
       \oint_{\Gamma_u}\oint_{\Gamma_v}
       \frac{\mathscr P_{2,2,N}(u,v)
                   \mathscr K_{1,N}(u,w)\mathscr K_{2,N}(v,z)}
            {\mathscr Q_N(u)\mathscr Q_N(v)}\,dv\,du
                 -\mathscr P_{3,4,N}^{\,P}(w,z)
 \right|
 \le C N^A e^{N\{\Re\mathcal W_{3,4}(w,z)-\gamma\}},
                   \qquad \gamma>0,
 \tag{36}
\]
uniformly on a fixed ordinary-color bidisk about
\((-2,-2)\). Formula (35) can replace the double integral
without changing this target. Every deformation must
retain all side currents, residues, and complementary
colors of its chosen representation.

The separate whole-source real outside-color gap of the
same stability note, equation (3), is also needed for
the later long-filling theorem. Its already proved
ordinary-color Hessian then gives the quadratic strip
bound. For this actual positive \((3,4)\) word, marked
geometric compatibility is already proved by
[the boundary-germ theorem](research_mixed_geometric_boundary_germ.md);
it is not an additional missing premise here.
Thus (32)--(36) identify a genuine turned-boundary
transport problem, while the ordinary same-sign
two-crossing family stays classified as covered.

## 7. Positive turned multiplication does not preserve the whole class

A source-specific proof for (36) is necessary: an unrestricted
preservation theorem for the turned operation is false even for
positive exponent one and actual original sources.

Let \(H_{p,N}=\mathsf T(R^p)\) be the original terminal
polynomial, with a fixed \(p\ge2\), and set
\[
                 F_N=\operatorname{can}(R H_{p,N}).
 \tag{37}
\]
The complete terminal theorem gives \(H_{p,N}\) its
nonzero local packet and strict whole-period quadratic
strip bound. Ordinary boundary-multiplication preservation
then gives those same classes of estimates for \(F_N\).
Taking \(p=2\) alone suffices.

The original modular identity is
\[
            \mathsf T\mathsf R\mathsf T
                  =\kappa\,\mathsf R^{-1}
                                  \mathsf T\mathsf R^{-1}.
 \tag{38}
\]
It is the matrix equality \(JMJ=\kappa M^{-1}JM^{-1}\)
used in the internal-chain theorem. Hence, in the full
Hermite algebra,
\[
       (\mathsf T\mathsf R\mathsf T)F_N
           =\kappa\,\operatorname{can}(R^{p-1}).
 \tag{39}
\]
Every equality is canonical; no value-only reduction
has been taken.

The right side of (39) cannot have both a nonzero local
packet and strict whole-angle decay of the original
concentrated class. Indeed its modulus at every physical
spectral angle is one. If a local packet at angle zero
and a global bound
\[
       |G_N(t)|\le C N^A
                     e^{N\{M-c(1-\cos t)\}},\qquad c>0,
 \tag{40}
\]
held with the same rate \(M\), use a physical angle
\(t_N\) with \(|t_N|\le\pi/N\). The packet and its
nonzero amplitude imply \(M=0\). Now use physical
angles tending to any fixed \(t_0\in(0,\pi)\).
Their unit modulus contradicts (40), whose right side
tends to zero exponentially. This includes both level
parities. It is the physical-node argument of
[boundary-multiplication preservation](research_boundary_crossing_packet_preservation.md),
Section 7, applied to the exact turned source (39).

Thus even the positive operation \(\mathsf T\mathsf R\mathsf T\)
cannot preserve all actual concentrated packets. This
does not disprove preservation on a narrower class that
contains the particular tensor \(\mathscr P_{2,2,N}\),
nor does it prove failure of (36). Any such narrower
criterion must explicitly exclude (37), or include a
separate output regime for its nonconcentrated crossing
source. No failure of a hyperbolic knot volume identity
is inferred.
