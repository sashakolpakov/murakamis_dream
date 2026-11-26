# The original closing operation beyond the Fourier boundary equations

Research deduction, 7 November 2026. The complete Fourier right cap
has a nonzero holomorphic packet and an exact finite difference
system selecting its normalized finite source. Its ordinary-output
contraction is nevertheless a different operation. This note writes
that operation with its full original kernel and proves a specific
obstruction to replacing a crossing by functional calculus of the
new diagonal boundary mark.

No numerical evaluation is used. The obstruction concerns that
commuting substitution, not general noncommuting difference operators
or the volume identity for an actual filled knot.

## 1. The bilinear Fourier dual at both level parities

Fix \(N\ge2\), put \(D=N-1\), and use
\[
 q=e^{\pi i/N},\qquad r=q^{-2},\qquad
 P_j=(r;r)_j,\qquad \kappa=q^{D^2/2}.
 \tag{1}
\]
The original half-band cardinal vector is \(h(t)=(h_j(t))_{j=0}^D\),
where
\[
 h_j(t)=\frac{\sin\pi N(t-j/N)}{N\sin\pi(t-j/N)}
       =\frac1N\sum_{\nu\in\{-D/2,\ldots,D/2\}}
                         e^{2\pi i\nu(t-j/N)}.
 \tag{2}
\]
All removable values are understood. This is the original basis of
[the traced vertex](research_traced_three_vertex_endpoint.md),
equation (3), not its complex conjugate.

For every complete horizontal period \(\Gamma\), oriented in the
increasing real direction,
\[
                         N\int_\Gamma h(t)h(t)^T\,dt=I_N.
 \tag{3}
\]
Indeed only the frequency pairs \(\mu=-\nu\) survive integration
of (2). The remaining finite sum is
\(N^{-1}\sum_\nu e^{2\pi i\nu(k-j)/N}=\delta_{jk}\).
This proof includes half-integer frequencies: when \(N\) is even,
\(h(t+1)=-h(t)\), but each product in (3) is periodic.
At odd levels \(h\) is itself periodic. Holomorphy and periodicity
make the integral independent of the starting point and height.
There is no reversal \(t\mapsto-t\), conjugation, or extra parity
factor in (3).

Use the original Newton crossing \(M\), reversal \(J\), and
ordinary evaluation column \(v(w)=(e_j(w))_j\). The exact common
basis in [wire contraction](research_mixed_wire_exact_contraction.md),
equations (3), (13), is
\[
 \begin{split}
 f_j(t)&=\frac{e^{-\pi iDt}}N
       Y^j\prod_{k=j+1}^{N-1}(1-Yr^k),\qquad Y=e^{2\pi it},\\
 f(t)&=S h(t),\qquad
 S=\operatorname{diag}\!
       \left(\frac{\kappa^{-1}(-q)^{-j}}{P_j}\right)M .
 \end{split}
 \tag{4}
\]
Every \(P_j\) here is nonzero, and \(S\) is invertible.
Its factors, including their phases and powers of \(N\), are
retained exactly.

## 2. Exact ordinary-output contraction of the complete cap

Let \(X=e^{-2\pi ia}\) and put
\[
 c_N(a)_l=C_{1,N}(X,r^l),\qquad
 Z_N(a,t)=V_N^{\rm F}(t,X)=c_N(a)^T f(t).
 \tag{5}
\]
Equation (5) is the literal last-node identity (5) of
[Fourier-ended windows](research_mixed_fourier_ended_boundary_windows.md).
It includes the outgoing cardinal \(1/N\) and the entire
conditional source. In particular no modulus is taken before
the outgoing sum.

For any original finite matrix \(B_N\), define
\[
 K_{B,N}(t,w)=h(t)^T B_N v(w),\qquad
 \mathcal O_{B,N}(a,w)=c_N(a)^T S B_N v(w).
 \tag{6}
\]
The ordinary variable \(w\) is the original Newton color.
The matrices and vector in (6) use their full repeated-root
normal data.

**Proposition 1.** At every level and for either parity,
\[
 \boxed{\quad
 \mathcal O_{B,N}(a,w)
       =N\int_\Gamma Z_N(a,t)K_{B,N}(t,w)\,dt .
 \quad}
 \tag{7}
\]
This holds for every complete horizontal period.

*Proof.* Substitute (4)--(6) and use (3):
\[
 N\int_\Gamma c_N(a)^T S h(t)h(t)^T B_Nv(w)\,dt
                     =c_N(a)^T S B_Nv(w).
\]
The two factors in the integrand have the same half-band parity,
so their product is periodic even when each is antiperiodic.
There is no Hermitian pairing in this calculation. \(\square\)

For \(B_N=I\), (7) changes this particular Fourier output to its
ordinary evaluation. For a fixed short path, take exactly
\[
 B_N=A_{n_1}\cdots A_{n_k},\qquad
                    A_n=JM^n,\quad n_i\in\mathbb Z.
 \tag{8}
\]
The order in (8) is the actual path order. Its crossing scalars
are inside \(M^{n_i}\), so no additional scalar is to be supplied
to (7). Changing a vertex power inside an existing word and
appending (8) are different operations; see
[the original interface](research_three_four_source_interface.md),
equations (4)--(5).
Any outside scalar belonging to a larger source before this
contraction remains unchanged.

For an actual partially filled tree, the original operation is
instead the appropriate contraction network. If \(F_N(z)\) is
the source at one filled vertex, its signed integer power \(n\)
is applied by
\[
 \mathcal L_N^n F_N=\phi_N(R^nF_N).
 \tag{9}
\]
For a canonical Newton coefficient column \(b\), this is
\[
 \phi_N(R^nF_N)=\mathbf e_D^T M^n b
                         =\mathbf e_0^T A_n b .
 \tag{10}
\]
The coefficient vectors \(\mathbf e_j\) in (10) are not the
Newton polynomials \(e_j(z)\). At an unfilled vertex its full
ordinary polynomial is retained until the prescribed trace is
applied. These are exactly the conventions of
[arbitrary-power compilation](research_arbitrary_power_source_compilation.md),
Sections 1--2.

## 3. A crossing cannot be a scalar function of the diagonal mark

The actual Fourier-output mark in
[the exact boundary difference system](research_mixed_fourier_exact_boundary_difference_system.md)
is
\[
 (\mathsf E_ZG)(t)
   =Y G(t)-q^{-1}(1-Y/r)G(t+1/N).
 \tag{11}
\]
It satisfies
\(\mathsf E_Z f_l=r^{-l}f_l\).
Thus on the \(N\)-dimensional half-band Fourier space it has
the \(N\) distinct eigenvalues \(r^{-l}\).
Every scalar polynomial or holomorphic functional calculus
of \(\mathsf E_Z\) is diagonalizable. This includes rational
functions whose denominators do not vanish on its spectrum,
and arbitrary prescriptions at its \(N\) eigenvalues.

The original crossing on the same space is
\[
 (\mathcal M_n G)(y)
   =N\int_\Gamma G(t)h(t)^T M^n h(y)\,dt .
 \tag{12}
\]
For \(G=\ell^T h\), (3) gives
\(\mathcal M_nG=\ell^T M^n h\).
Consequently \(\mathcal M_n\) has the Jordan form of
\((M^n)^T\), equivalently that of \(M^n\).

**Proposition 2.** For every \(N\ge2\) and every nonzero
integer \(n\), \(\mathcal M_n\) is not a scalar function of
\(\mathsf E_Z\), nor can an invertible change of coordinates
make it one.

*Proof.* The original algebra is
\[
 \mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2).
 \tag{13}
\]
At its double physical node \(c_0=2\cos(\pi/N)\), the
original crossing value and first logarithmic normal are
\[
 R(c_0)=\kappa,\qquad
 \frac{R'(c_0)}{R(c_0)}
          =\frac{i(N-1)}{4\sin(\pi/N)}\ne0 .
 \tag{14}
\]
These are the full Hermite formulas in
[the original twist observation](research_original_twist_observation_tomography.md),
equation (3). Multiplication by \(R^n\) on the local
length-two algebra at \(c_0\) is therefore
\[
 \kappa^n\left(1+
       n\,\frac{i(N-1)}{4\sin(\pi/N)}(z-c_0)\right)
                            \pmod{(z-c_0)^2}.
 \tag{15}
\]
The nilpotent coefficient is nonzero for every signed
\(n\ne0\). Thus \(M^n\) has a nontrivial Jordan block,
which is impossible for a scalar function of the simple-spectrum
mark (11). Jordan form is preserved by similarity.
At \(N=2\), the defining polynomial is \(z^2\), so \(c_0=0\)
is still a double root and the coefficient in (14) is \(i/4\).
There is no small-level exception. \(\square\)

This is a precise obstruction to a commuting-mark replacement
of the short crossing. It does not prohibit representing that
crossing using noncommuting shifts and multiplications, or
estimating the original kernel (12). It also says nothing
adverse about the actual filled invariant.

## 4. The remaining estimate is for the original observation

The holomorphic cap packet controls \(Z_N(a,t)\) on a fixed
neighborhood of its actual Fourier reference. Equation (7)
uses a complete period and the specific kernel \(K_{B,N}\).
For a deformation of that period into a local contour
\(\gamma_{B,N}\) and its retained complementary chain
\(\mathcal R_{B,N}\), the exact missing source estimate is
of the form
\[
 \left|N\int_{\mathcal R_{B,N}}
          Z_N(a,t)h(t)^TB_Nv(w)\,dt\right|
 \le C N^A e^{N\{\Re\Phi_B(a,w)-\delta\}},
                         \qquad\delta>0,
 \tag{16}
\]
where the local integral over \(\gamma_{B,N}\) must itself
have a nonzero coefficient and the same calibrated action
\(\Phi_B\). All connectors and any residues of a chosen
representation belong to \(\mathcal R_{B,N}\).
Neither the location of that new stationary contour nor
(16) follows from the old local cap packet.
For a branching short piece, (16) is replaced by the
corresponding original multilinear trace network (9).

The exact rank-one difference system determines the finite
function \(Z_N\) uniquely after its coefficient normalization.
It is therefore stronger than knowledge of a phase and fixed
jets alone. The modified-germ construction in
[the turn-remainder note](research_source_germ_truncation_and_turn_remainders.md)
must not be claimed to preserve this exact difference system.
What remains separate is an asymptotic estimate for its
specified new observation, not uniqueness of its finite source.

Finally the original padding equivalence retains its full force.
In [original tree padding](research_original_tree_padding_equivalence.md),
equations (9)--(11), the zero-filled middle vertex gives
\[
 (p_a,p_v,p_b,\mathbf p)=(r,0,p_s-r,\mathbf p)
 \quad\longmapsto\quad
                 \hbox{the same fixed filled knot for every }r.
 \tag{17}
\]
Thus even a two-free-coordinate long-remainder theorem on
all such fixed short strata would settle every represented
hyperbolic core. A local Fourier-cap packet, its algebraic
shift equations, or an unresolved core counted once cannot
discharge these infinite original assignment fibers.
No new knot-family or finite-exception theorem is asserted here.

## 5. Exact noncommuting crossing transport with its endpoint projector

The obstruction in Proposition 2 leaves a concrete alternative.
The finite \(q\)-binomial factorization of
[terminal powers](research_terminal_powers_qbinomial.md), Section 2,
can be written in the actual Fourier basis (4). The following is
that existing factorization in these boundary coordinates, not a
new asymptotic method. Related original Newton-clock conjugations
are given in
[crossing-run quantum continuants](research_crossing_run_quantum_continuants.md),
Sections 1--2.

Put \(Q=r^{-1}\), and define operators on the span of the \(f_j\) by
\[
 \begin{split}
 \mathsf E&=\mathsf E_Z,\qquad \mathsf E f_j=Q^j f_j,\\
 \mathsf B f_j&=f_{j-1}\quad(j\ge1),\qquad \mathsf Bf_0=0,\\
 \mathsf\Gamma f_j&=\kappa\nu_j f_j,\qquad
                 \nu_j=(-1)^jq^{j(j+1)},\\
 \mathscr P_N(\mathsf B)
   &=\sum_{k=0}^{N-1}\frac{\mathsf B^k}{(Q;Q)_k}
     =\sum_{k=0}^{N-1}
       \frac{(-1)^kr^{k(k+1)/2}}{P_k}\mathsf B^k .
 \end{split}
 \tag{18}
\]
The denominators in (18) are nonzero. These operators satisfy
\[
 \mathsf E\mathsf B=r\mathsf B\mathsf E,\qquad
 \mathsf B^N=0,\quad \mathsf B^{N-1}\ne0,\qquad
 \mathsf\Gamma\mathsf B\mathsf\Gamma^{-1}=-\mathsf B\mathsf E^{-1}.
 \tag{19}
\]
All identities include \(j=0\). In particular, this lowering
operator has no cyclic wrap.

**Proposition 3.** The original one-crossing operator (12) is
\[
                 \boxed{\ \mathcal M_1
                         =\mathscr P_N(\mathsf B)\mathsf\Gamma.\ }
 \tag{20}
\]
Moreover, its lowering operator is exactly
\[
 \begin{split}
 \Pi_0&=\frac1N\sum_{k=0}^{N-1}\mathsf E^k,\\
 \mathsf B&=(Y^{-1}-\mathsf E^{-1})(I-\Pi_0).
 \end{split}
 \tag{21}
\]
Here \(Y^{-1}\) denotes multiplication. The rightmost projector
in (21) is part of the formula.

*Proof.* Write \(S=D_0M\), with the diagonal \(D_0\) given in
(4). Acting on an individual basis function in (12) gives
\(\mathcal M_1f_j=(SM S^{-1}f)_j\). Since
\(SM S^{-1}=D_0M D_0^{-1}\), the original crossing entries
\[
 M_{jl}=\kappa(-1)^j q^{j+l^2}{j\brack l}_Q
                  \quad(0\le l\le j<N)
\]
and
\(P_j=(-1)^jq^{-j(j+1)}(Q;Q)_j\) yield
\[
 (D_0M D_0^{-1})_{jl}
       =\frac{\kappa(-1)^jq^{j(j+1)}}{(Q;Q)_{j-l}}
       =\frac{\kappa\nu_j}{(Q;Q)_{j-l}}.
 \tag{22}
\]
Thus \(\mathcal M_1f_j\) is the sum of the right side of
(22) times \(f_l\), which is precisely (20). This uses the
row action on basis functions; transposing this convention
would interchange the two factors incorrectly.

The eigenvalues of \(\mathsf E\) show that \(\Pi_0\) projects
onto \(f_0\). For \(j\ge1\), (4) gives
\[
       (1-Yr^j)f_j=Yf_{j-1},
       \qquad
       (Y^{-1}-\mathsf E^{-1})f_j=f_{j-1}.
 \tag{23}
\]
On the lowest basis function, the same expression instead is
\[
 (Y^{-1}-\mathsf E^{-1})f_0
     =\frac{e^{-\pi iDt}}{NY}(1-Y^N),
 \tag{24}
\]
which is not identically zero and does not lie in the original
half-band. Equations (23)--(24) prove (21), including its
endpoint correction. Finally (19) follows directly on each
\(f_j\), using
\(\nu_{j-1}/\nu_j=-r^j\). \(\square\)

Every factor in (20) is explicit in the mark and the corrected
lowering operation. For example, the spectral projectors
\[
 \Pi_j=\frac1N\sum_{k=0}^{N-1}r^{jk}\mathsf E^k,
       \qquad \mathsf\Gamma=\kappa\sum_{j=0}^{N-1}\nu_j\Pi_j
 \tag{25}
\]
retain the full diagonal crossing phase, including \(\kappa\).
Since \(\mathscr P_N(\mathsf B)=I+\text{nilpotent}\), it is
invertible. Thus for every signed integer \(n\),
\[
 \mathcal M_n=(\mathscr P_N(\mathsf B)\mathsf\Gamma)^n,\qquad
 \mathcal M_{-1}=\mathsf\Gamma^{-1}\mathscr P_N(\mathsf B)^{-1}.
 \tag{26}
\]
The composition agrees with (12) by (3), so (26) transports
the actual finite source rather than only its critical equations.

There are also exact ordered coordinate substitutions. In the
nilpotent algebra generated by \(\mathsf B\),
\[
 \mathscr P_N(\mathsf B)
       =(I-r\mathsf B)\mathscr P_N(r\mathsf B),
 \qquad
 \mathsf E\mathscr P_N(\mathsf B)
       =\mathscr P_N(r\mathsf B)\mathsf E.
 \tag{27}
\]
For the first identity, put \(p_k=1/(Q;Q)_k\).
The coefficient of \(\mathsf B^k\), \(1\le k<N\), on the
right is \(r^k(p_k-p_{k-1})=p_k\); the remaining degree-\(N\)
term vanishes by (19). The second identity follows from the
first commutation relation in (19). As \(\mathsf\Gamma\) commutes
with \(\mathsf E\), (19), (20), and (27) give
\[
 \boxed{\begin{split}
 \mathcal M_1\mathsf E\mathcal M_1^{-1}
                  &=(I-r\mathsf B)\mathsf E,\\
 \mathcal M_1\mathsf B\mathcal M_1^{-1}
                  &=-\mathsf B\mathsf E^{-1}(I-r\mathsf B)^{-1}.
 \end{split}}
 \tag{28}
\]
The inverse in the second line is the finite sum
\(\sum_{k=0}^{N-1}r^k\mathsf B^k\). Its position is essential:
the second line is obtained as
\(-\mathsf B(\mathcal M_1\mathsf E\mathcal M_1^{-1})^{-1}\).
There is no division by a scalar value \(1-B\) in (28).

Formally taking commuting symbols and \(r\to1\) gives the
rational coordinate map
\[
          E\longmapsto(1-B)E,\qquad
          B\longmapsto-\frac{B}{E(1-B)}
                    \quad\text{on }E(1-B)\ne0.
 \tag{29}
\]

The original ordinary multiplication coordinate has a precise
dictionary in the same operators. Let \(Z\) denote multiplication
by the original variable \(z\) in (13), and define its action
on Fourier functions by
\[
 (\mathsf ZG)(y)
       =N\int_\Gamma G(t)h(t)^T Z h(y)\,dt .
 \tag{30}
\]
The original Newton recurrence, stated also in
[the elementary cap calculation](research_elementary_cap_path_laplacian.md),
equation (1), gives
\[
 Z_{jj}=qQ^j+q^{-1}Q^{-j},\qquad
 Z_{j,j-1}=Q^j+Q^{-j}-2 \quad(j\ge1).
 \tag{31}
\]
All other entries vanish. Since the original crossing is
multiplication by \(R(z)\), \(MZ=ZM\), as proved directly
with the full normal data in
[the Newton calculus](../papers/newton-calculus/finite.tex).
Consequently \(SZS^{-1}=D_0ZD_0^{-1}\). Its subdiagonal is
\[
 \frac{-q^{-1}}{1-r^j}(Q^j+Q^{-j}-2)
                   =-q^{-1}(Q^j-1).
\]
Using the same row convention as in (22) proves the exact identity
\[
 \boxed{\quad
 \mathsf Z=q\mathsf E+q^{-1}\mathsf E^{-1}
                         -q^{-1}\mathsf B(\mathsf E-I),
 \qquad
 \mathcal M_1\mathsf Z\mathcal M_1^{-1}=\mathsf Z .
 \quad}
 \tag{32}
\]
For an independent ordered check of the second assertion,
put \(C=I-r\mathsf B\) and substitute (28) into the first:
\[
 qC\mathsf E
   +q^{-1}(I-\mathsf B)\mathsf E^{-1}C^{-1}
   +q^{-1}\mathsf B
   =qC\mathsf E+q^{-1}\mathsf E^{-1}+q^{-1}\mathsf B
   =\mathsf Z.
 \tag{33}
\]
Here \((I-\mathsf B)\mathsf E^{-1}=\mathsf E^{-1}C\)
and \(qr=q^{-1}\) were used. Thus the commuting invariant
of (29) is
\[
                         z=E+E^{-1}-B(E-1).
 \tag{34}
\]
It is the original ordinary coordinate (or Casimir) in this
boundary representation. It has not been identified with a
meridian or longitude of a knot.

This operator identity does not turn ordinary evaluation at
an arbitrary \(w\) into an eigenvector assertion. Indeed the
same Newton recurrence gives
\[
 Z^T v(w)=w\,v(w)+(c_D-w)e_D(w)\mathbf e_D,
              \qquad c_D=qQ^D+q^{-1}Q^{-D}.
 \tag{35}
\]
The last term is the original quotient-boundary forcing; it
cannot be dropped for a general ordinary color. Equations
(30)--(34) concern the full finite algebra and retain this
distinction.

The endpoint projection after one crossing has an equally
explicit original observation.
For every function \(G=\sum_{l=0}^{N-1}g_lf_l\) in the finite
Fourier band,
\[
             \boxed{\quad
             \Pi_0\mathcal M_1G(y)=\kappa G(0)f_0(y).
             \quad}
 \tag{36}
\]
Indeed \(P_{N-1}=N\), so (4), evaluated at \(t=0\), gives
\(f_l(0)=P_{N-1}/(NP_l)=1/P_l\).
By (22), the coefficient of \(f_0\) in \(\mathcal M_1f_l\)
is
\(\kappa\nu_l/(Q;Q)_l=\kappa/P_l\).
Summing over \(l\) proves (36), at both parities and with
the original crossing scalar intact. For the actual cap,
\[
 \Pi_0\mathcal M_1Z_N(a,y)
       =\kappa Z_N(a,0)f_0(y),\qquad
 Z_N(a,0)=\sum_{l=0}^{N-1}\frac{C_{1,N}(X,r^l)}{P_l}.
 \tag{37}
\]
This is a different source observation from
\(\Pi_0Z_N(a,y)=f_0(y)C_{1,N}(X,1)\).
The proved
[zero-index projection gap](research_mixed_fourier_zero_index_projection_gap.md)
controls the latter near the actual output \(y=x_0\).
It does not estimate the former coefficient \(Z_N(a,0)\).
Consequently that gap cannot be iterated through even one
crossing from the local packet alone: the specific additional
observation in (37) must be controlled. Nothing here asserts
that its desired gap fails.

Equation (29) is only the commuting shadow of the exact ordered
identities (28). It is not a proved asymptotic transport of the
cap phase. At finite level, (21) retains the endpoint projector,
the nilpotence index is exactly \(N\), and (18), (25) have
level-dependent degree. This does not supply a uniformly
bounded-order replacement as \(N\) grows.
No conditioning estimate, noncancellation after an arbitrary
short filling, or bound on the closing complement (16) follows
from these exact formulas alone.
