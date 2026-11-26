# Almost-invariant original vectors and their marked observations

An almost-invariant vector can give a lower bound for a specified
source if its observation at the original closing row is also
controlled. The finite Newton representation makes that requirement
quite explicit. It has genuine geometric Casimir quasimodes whose
overlaps with both original cap directions are exponentially small.
For the forced three-crossing operator there is an exact adjoint
quasimode whose endpoint overlap loses precisely the entire gain
from its small residual.

There is also a natural self-adjoint form of the adjacent
three-crossing problem. Its inertia is known exactly, and the
closing scalar is an off-diagonal Green entry. Thus this change
of form retains the original source without turning it into a
positive norm.

All statements below concern the full original finite algebra,
including first normals at double roots. They do not contradict
unitarity of the different ordinary-color representations.

## 1. Original operators and the unitarization obstruction

Fix \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\).
Use the original normalized Newton basis of
\[
 {\cal A}_N=\mathbb C[z]/(2T_N(z/2)+2).
\]
Write \(C\) for multiplication by \(z\), \(M\) for the
original positive crossing, and \(J\) for index reversal.
Their exact relations include
\[
 \begin{split}
 (Cv)_j&=c_jv_j-d_jv_{j-1},\\
 c_j&=2\cos((2j+1)\pi/N),\qquad
 d_j=4\sin^2(\pi j/N),\\
 J^2&=I,\qquad C^\dagger=JCJ,\qquad
                      M^\dagger JM=J .
 \end{split}                                                    \tag{1}
\]
The missing lower-end term is zero. These are identities
on the entire original quotient. The positive Newton
inner product is the ordinary coefficient inner product.
The two original cap observations are
\[
       e_0^\dagger\mathbf f=f(c_0),\qquad
       e_D^\dagger\mathbf f=\phi_N(f).
 \tag{2}
\]
Both rows have norm one. The first is the original
turned cap, equivalently evaluation at the first
physical Casimir node; the second is the unturned
closing functional.

The crossing is not unitary for a different positive
inner product. At a double root \(c_j\), its restriction
to the original two-dimensional local algebra is
\[
 M_j=\lambda_j(I+K_j),\qquad K_j^2=0,\quad K_j\ne0,
                      \qquad |\lambda_j|=1 .
 \tag{3}
\]
For example, in the basis \(1,\epsilon\), with
\(\epsilon=z-c_j\), its nonzero nilpotent entry is
\[
 \frac{R'(c_j)}{R(c_j)}
   =\frac{i(D-2j)}{4\sin((2j+1)\pi/N)} .
 \tag{4}
\]
The pair \(j=0,D\) is double and has nonzero entry at
every \(N\ge2\). Formula (4), including its original
normalization, is proved in
[the arbitrary-power compilation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_arbitrary_power_source_compilation.md),
Section 6.

If \(H>0\) satisfied \(M^\dagger HM=H\), then
\(H^{1/2}MH^{-1/2}\) would be unitary and hence
diagonalizable. This contradicts (3). The same
argument excludes making \(C\) self-adjoint while
retaining its double-root Jordan blocks.

There is a more precise conclusion for an actual
positive average of crossing transports.

**Proposition 1.** Let \(G_1,\ldots,G_r\) be original
invertible word matrices with \(|\det G_i|=1\), with
positive weights summing to one. Suppose the list
contains \(M\). The completely positive average
\[
       {\cal P}(\rho)=\sum_i p_iG_i\rho G_i^\dagger
 \tag{5}
\]
has no positive definite stationary trace metric:
there is no \(H>0\) satisfying
\({\cal P}^\dagger(H)=H\).
In particular this applies to the symmetric average
of \(M,M^{-1},J\).

**Proof.** Put
\(A_i=H^{-1/2}G_i^\dagger HG_iH^{-1/2}\).
Each \(A_i>0\), \(\det A_i=1\), and
\(\sum p_iA_i=I\). The arithmetic-geometric mean
inequality for its eigenvalues gives
\(\operatorname{tr}A_i\ge N\), with equality only
at \(A_i=I\). Taking traces of the average forces
equality for every \(i\). In particular
\(M^\dagger HM=H\), which (3) excludes.
\(\square\)

This does not exclude a Perron rescaling, a degenerate
stationary form, or a different source-adapted unitary
operator. Such a change must retain its scaling and
the original test row; (5) is not already a
trace-preserving quantum channel in a faithful
positive metric.

Even the simplest symmetric crossing average retains
the normal obstruction explicitly. On the invariant
local plane (3), use any positive inner product and
its adjoint. Its restriction to positive matrices is
\[
 \tfrac12\{M_j\rho M_j^\dagger+
                  M_j^{-1}\rho M_j^{-\dagger}\}
                      =\rho+K_j\rho K_j^\dagger.
 \tag{6}
\]
The added map is nonzero and square-zero. Its \(m\)-th
iterate is \(\rho+mK_j\rho K_j^\dagger\).
Thus this actual positive average has a Jordan
direction at eigenvalue one, rather than a mixing
gap to a stationary projector. Passing to the
semisimple quotient would remove precisely that
original normal direction.

## 2. A geometric quasimode invisible to the original caps

Fix \(k\ge2\), and let
\[
 \alpha_N=M^{2k}e_0,\qquad
 a_N=\alpha_N/\|\alpha_N\|_2.
 \tag{7}
\]
The reflected volume theorem and the fixed-insertion
theorem give
\[
 \begin{split}
 \|(C-z_k)a_N\|_2&\longrightarrow0,\\
 \lim_{N\to\infty}\frac1N\log\|\alpha_N\|_2
                &=\frac{V_k}{4\pi}>0,
 \end{split}                                                    \tag{8}
\]
where \(z_k=-2\cos t_k\) is the actual geometric
core value and \(V_k\) is the volume of the original
closed reflected knot. See
[the Casimir insertion theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_even_reflected_casimir_insertions.md)
and [the reflected volume theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_reflected_even_kashaev_volume_theorem.md).

**Theorem 2.** The actual geometric quasimodes (7)
satisfy
\[
 \lim_{N\to\infty}\frac1N\log|e_0^\dagger a_N|
                              =-\frac{V_k}{4\pi}.
 \tag{9}
\]
For every fixed polynomial \(P\),
\[
 \limsup_{N\to\infty}\frac1N
     \log|e_D^\dagger P(C)a_N|
                         \le-\frac{V_k}{4\pi},
 \tag{10}
\]
where a zero value has logarithm \(-\infty\).
The same upper bound holds at the first cap.

**Proof.** The original crossing is lower triangular
and \(M_{00}=\kappa\), \(|\kappa|=1\). Thus
\[
                   e_0^\dagger\alpha_N=\kappa^{2k}.
 \tag{11}
\]
This and (8) prove (9). Moreover
\[
       e_0^\dagger P(C)\alpha_N=P(c_0)\kappa^{2k},
 \tag{12}
\]
because the first row of \(C\) is \(c_0e_0^\dagger\).
Fixed polynomials are bounded on \(c_0\in[-2,2]\).

For the other cap retain the actual backward channel
of [the even-run endpoint theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_even_run_backward_source_growth.md):
\[
 \alpha_{N,j}=\kappa^{2k}e_k^Tu_j,\qquad
 g_h=S_h^2u_{D-h},\qquad
 g_0=u_D,\quad g_h=H_{N-h}g_{h-1}.
 \tag{13}
\]
Here \(\|u_D\|=O_k(N^{3/2})\) is the proved original
endpoint estimate, and \(\|H_j\|\le4\). For each fixed
integer \(h\ge0\),
\[
 S_h^2\asymp_h N^{-2h},\qquad
                  |\alpha_{N,D-h}|=O_{k,h}(N^{2h+3/2}).
 \tag{14}
\]
If \(m=\deg P\), the last row of \(P(C)\) uses only
indices \(D-m,\ldots,D\), and its norm is bounded
independently of \(N\) since \(\|C\|\le6\).
Equations (13)--(14) therefore make
\(e_D^\dagger P(C)\alpha_N\) polynomially bounded
in \(N\). Divide by (8) to obtain (10).
\(\square\)

This is an original source vector and an original
geometric approximate eigenvalue. The small overlaps
are not obtained by choosing an artificial orthogonal
test row. In particular any fixed collection of
Casimir observations at the first cap has the exact
observation Gram matrix
\[
 \sum_{\ell=0}^{m}(C^\dagger)^\ell
                e_0e_0^\dagger C^\ell
       =\left(\sum_{\ell=0}^{m}|c_0|^{2\ell}\right)e_0e_0^\dagger.
 \tag{15}
\]
It cannot provide full-space coercivity.

The same example already exists on the doubled
positive space. Put \(\rho_N=a_Na_N^\dagger\), and
use the actual Casimir transport
\[
                 {\cal C}_{z_k}(\rho)
                      =|z_k|^{-2}C\rho C^\dagger.
 \tag{16}
\]
If \(\epsilon_N=\|(C-z_k)a_N\|\), then
\[
 \|{\cal C}_{z_k}(\rho_N)-\rho_N\|_1
       \le\frac{2\epsilon_N}{|z_k|}
                    +\frac{\epsilon_N^2}{|z_k|^2}
                         \longrightarrow0.
 \tag{17}
\]
This follows by expanding the two rank-one products;
\(\|xy^\dagger\|_1=\|x\|\|y\|\).
Nevertheless
\[
 \operatorname{tr}(e_0e_0^\dagger\rho_N)
                   =\exp\{-NV_k/(2\pi)+o(N)\}.
 \tag{18}
\]
Map (16) is completely positive; it has not been
asserted to preserve trace or to possess a mixing
gap. Doubling preserves positivity but does not
repair the specified observation.

## 3. The exact adjoint test for a forced boundary source

For an invertible original operator \(A_N\) and its
specified source
\[
                  A_Nf_N=\zeta_N e_D,\qquad |\zeta_N|=1,
 \tag{19}
\]
every trial vector \(v\) gives
\[
 \boxed{\quad
 \|f_N\|\ge
        \frac{|v_D|}{\|A_N^\dagger v\|}.
 \quad}                                                        \tag{20}
\]
Indeed
\(\zeta_N\overline{v_D}
 =\langle A_N^\dagger v,f_N\rangle\).
For normalized trials, an exponentially small
adjoint residual is useful only after comparing
its rate with that of \(v_D\).

The original free polynomial is
\(F_N(w)=\mathbf e(w)^Tf_N\), where
\(\mathbf e(w)=(e_0(w),\ldots,e_D(w))^T\) is the full
Newton evaluation column. If
\[
        A_N^\dagger v=\overline{\mathbf e(w)}+r_N,
\]
then the exact identity and its useful lower bound are
\[
 \begin{split}
 F_N(w)&=\zeta_N\overline{v_D}-\langle r_N,f_N\rangle,\\
 |F_N(w)|&\ge |v_D|-\|r_N\|\,\|f_N\|.
 \end{split}                                                    \tag{21}
\]
Thus a dual approximate solution can prove the
specified lower bound without positive unitarization.
It must retain the actual endpoint observation and
make the residual smaller than that observation
after multiplication by a proved upper bound for
\(\|f_N\|\).

The following exact original operator shows why the
residual alone is insufficient. Put
\[
 T=C-q\mathsf X,\qquad
 \mathsf X=\operatorname{diag}(Q^j),\qquad
 h_j=q^{j(j+2)}S_j^2.
 \tag{22}
\]
The exact three-crossing equation gives
\[
             Th=q^{-1}e_0,\qquad T^\dagger=JTJ.
 \tag{23}
\]
For \(v=Jh/\|h\|\), therefore,
\[
 \|T^\dagger v\|=\frac1{\|h\|},\qquad
                       |v_D|=\frac1{\|h\|}.
 \tag{24}
\]
These are exponentially small: the uniform
sine-factorial estimate, with
\(\mathcal J(x)=\int_0^x\log(2\sin\pi s)\,ds\), gives
\[
 \lim_{N\to\infty}\frac1N\log\|h\|
   =2\max_{0\le x\le1}\mathcal J(x)
   =2\mathcal J(5/6)>0 .
 \tag{25}
\]
The bound (20) for the endpoint-forced equation
\(Tx=e_D\) is exactly one. That is sharp:
\[
                           x=q^{-1}e_D,\qquad \|x\|=1.
 \tag{26}
\]
Indeed \(T\) is lower bidiagonal and \(T_{DD}=q\).
This does not replace the original adjacent-pair
operator by \(T\); it demonstrates, within its
actual original factor, the exact loss from the
wrong endpoint overlap.

## 4. The natural self-adjoint form of the adjacent pair

For the actual pendant \(JM^3JM^3e_0\), retain the
exact factorization from
[the boundary-current theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_three_crossing_boundary_current.md):
\[
 A_N=B S T S^{-1},\qquad S=JM^3J,\qquad
 A_Nf_N=\zeta_Ne_D,\qquad \det A_N=-(-1)^D.
 \tag{27}
\]
Here \(f_N=JM^3JM^3e_0\),
\(\kappa=\exp(\pi iD^2/(2N))\), and
\(\zeta_N=(-1)^D\kappa^2q^{-1}\).
Here \(T\) is (22), and the original upper bidiagonal
matrix \(B\) has
\[
                 B_{jj}=-qQ^j,\qquad
                 B_{j,j+1}=1-Q^{j+1}.
 \tag{28}
\]
All absent entries are zero. In particular
\[
             B^\dagger=JBJ,\qquad
             S^\dagger=JS^{-1}J .
 \tag{29}
\]

**Theorem 3.** The original matrix
\[
                           H_N=A_NBJ                           \tag{30}
\]
is Hermitian and invertible, with inertia
\[
              (n_+,n_-,n_0)
                   =(\lfloor N/2\rfloor,\lceil N/2\rceil,0).
 \tag{31}
\]
The unturned original closing scalar is exactly
\[
       \phi_N(F_N)=(f_N)_D
            =-\zeta_Nq^{-1}e_0^\dagger H_N^{-1}e_D.
 \tag{32}
\]
The full free-boundary source is
\[
        F_N(w)=\zeta_N\mathbf e(w)^T BJH_N^{-1}e_D .
 \tag{32a}
\]

**Proof.** Relations (23), (27), and (29) give the
exact congruence
\[
                 H_N=(BS)(TJ)(BS)^\dagger.
 \tag{33}
\]
Since \(T^\dagger=JTJ\), the middle matrix is
Hermitian. It remains invertible if its strictly
lower diagonal is multiplied by any
\(\lambda\in[0,1]\): before multiplying by \(J\)
the matrix is triangular, with unchanged nonzero
diagonal \(q^{-1}Q^{-j}\). The relation
\(T_\lambda^\dagger=JT_\lambda J\) also persists.
Thus the inertia stays constant along this path.

At \(\lambda=0\), paired indices \(j,D-j\) give
Hermitian blocks with zero diagonal and conjugate
off-diagonal entries of modulus one. Each has
eigenvalues \(1,-1\). If \(N\) is odd, the unpaired
central entry is
\(q^{-1}Q^{-(N-1)/2}=q^{-N}=-1\).
This proves the inertia of \(TJ\), and (33) gives
the same inertia for \(H_N\).

Finally \(A_N^{-1}=BJH_N^{-1}\), and the last row
of \(B\) is \(-q^{-1}e_D^\dagger\). Applying this
to (19) proves (32); applying the complete Newton
evaluation row gives (32a).
\(\square\)

The Hermitian matrix in (30) is built from the
original finite source operators. No geometric
projector has been substituted. Its fixed inertia
precludes a positive-energy interpretation of its
inverse. Formula (32) is an off-diagonal Green
entry; it can involve cancellations between
positive and negative spectral subspaces.
For this turned pendant, its particular unturned
cap is already simple:
\[
              (f_N)_D=\kappa^3(M^3e_0)_D.
\]
This follows from the first row of \(M^3\). Its
endpoint asymptotic is known. It must not be
confused with the unresolved retained-boundary
value \(F_N(-2)\), whose actual Green formula is
(32a). That formula has a boundary-dependent
left observation, not a matching positive
quadratic observation.
For the negative pendant, conjugate the original
matrices and source, as in the boundary-current
theorem. The congruence, inertia and conjugated
closing identity hold with that same convention.

## 5. What remains to obtain a lower bound

The rational geometric curve of the adjacent
\((-3,-3)\) pendant is now identified with its
original peripheral germ in
[the geometric branch theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_three_crossing_pendant_geometric_branch.md).
That identifies a candidate phase for a local
adjoint construction. It does not supply an
adjoint vector with exponentially accurate
residual and a controlled overlap at row \(D\).
The end rows, the repeated-root directions and
the phase through the intervening indices still
have to be matched.

Equations (20)--(21) state a precise sufficient
target. A local frozen-symbol root or a
first-order bulk approximation does not yet
verify it. The sharp counterexamples (9) and
(24) show that the overlap condition cannot
be omitted even for actual geometric or
exponentially accurate original quasimodes.

The reflected Stein equation remains a useful
positive special case: its observation Gram
matrix has the proved polynomial lower bound
in [the original Stein-energy theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_reflected_laurent_stein_energy.md).
There the source itself is the matching
nonnegative observation sum. The retained
adjacent-pair boundary value (32a) has a
different observation, which that theorem
does not estimate.

## 6. Focused finite replay

[The original-matrix checker](../experiments/check_original_almost_invariance_observation.py)
constructs \(A_N\) from its band entries and independently
constructs the literal source from \(M,J\). At levels
\(2,\ldots,10\), for both crossing signs, it compares
the Hermitian congruence, inertia, endpoint equations,
and the complete Green formula (32a), including first
normals. The boundary tests include \(-2\), a nonreal
point and the repeated physical node \(c_0\).
It also checks the exact residual/overlap equality
in (24) and the norm-one solution (26).

[The saved 100-digit record](../repro/results/research-original-almost-invariance-observation.json)
retains the script, note and original-matrix dependency
hashes. An independent output can be selected with
\(\texttt{--output}\). The finite eigenvalue checks
are diagnostics; the all-level inertia is the
nonsingular Hermitian-path proof in Theorem 3.
No source-asymptotic rate or uniform spectral gap
is inferred from these computations.
