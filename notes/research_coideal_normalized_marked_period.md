# An initialized coideal period has a flat abelian framing

24 November 2026. Written research proof.

The actual coideal crossing has a canonical polynomial column away
from its physical roots. Its endpoint defect selects one source,
and the original marked row selects one unit residue of that source.
Changing the neighboring height gives an explicit commuting
unipotent comparison, preserving both the source and the marked row.
All statements are finite algebra at the specified level.
No knot peripheral variable or geometric selected cycle is identified.

## 1. Original finite matrices

Use the complete conventions of N, T and K in the source table:
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \sqrt q=e^{\pi i/(2N)},\quad \kappa=e^{i\pi d^2/(2N)}.
\]
Write
\[
 F_a=(Q;Q)_a,\quad F_0=1,\quad F_d=N,\qquad
 \alpha_t=(t+\tfrac12)\pi/N,\quad
 \lambda_t=2\sqrt q\cos\alpha_t,\quad \mu_t=\sin\alpha_t.
\]
All physical height indices lie in \(0,\ldots,d\).
The monic polynomial and its normalized version are
\[
 p_N(z)=2q^{N/2}T_N(z/(2\sqrt q)),\qquad
 \pi_N(\zeta)=2T_N(\zeta/2),\qquad
 p_N(\sqrt q\,\zeta)=q^{N/2}\pi_N(\zeta).
 \tag{1}
\]
Its roots are \(\lambda_t\), and
\[
 p_N'(\lambda_t)=Nq^{d/2}(-1)^t/\mu_t,\qquad
 \zeta_t=\lambda_t/\sqrt q=2\cos\alpha_t.
 \tag{2}
\]

The original leading continuants and eigenmatrix are
\[
 D_{-1}=0,\quad D_0=1,\quad
 D_{a+1}(\lambda;\sigma)
  =(\lambda+qQ^a\sigma)D_a(\lambda;\sigma)
                         -q(1-Q^a)^2D_{a-1}(\lambda;\sigma),
\]
\[
 (U_\sigma)_{a,t}=q^{-a}D_a(\lambda_t;\sigma)/F_a.
 \tag{3}
\]
For an actual root \(\sigma\), this is the invertible physical
eigenmatrix of
\[
 (T_\sigma u)_a=(1-Q^a)u_{a-1}
       +q(1-Q^{a+1})u_{a+1}-qQ^a\sigma u_a.
\]
Both missing endpoint arrows are zero. For another actual root
\(\nu\), retain the actual reversed operator
\[
 (J_\nu'u)_a=(1-Q^{-a})u_{a-1}
       +q(1-Q^{-a-1})u_{a+1}-q^{-1}Q^{-a}\nu u_a,
\]
\[
 J_{\nu,\sigma}=U_\sigma^{-1}J_\nu'U_\sigma,\qquad
 B^+_{\nu,\sigma}
  =\kappa U_\sigma^{-1}\operatorname{diag}(q^{-a})
                                      \overline{U_\nu}.
 \tag{4}
\]
These are T's unchanged-frame crossing matrices. In particular
\(J_{\nu,\sigma}B^+_{\nu,\sigma}
   =B^+_{\nu,\sigma}\operatorname{diag}(\lambda_t)\).
No sorted-fold continuation or division by \(1+Q\) is used here.

## 2. The off-root endpoint defect fixes a polynomial source

Let
\[
 r_\nu(z)_a=(-1)^aD_a(\nu;z)/F_a,\quad
 w_t=1/p_N'(\lambda_t),\quad
 b_\sigma(z)=\kappa U_\sigma^{-1}r_\nu(z).
\]
Then the exact identities are
\[
 (J_\nu'-zI)r_\nu(z)=q\,p_N(z)e_d/N,\qquad
 (zI-J_{\nu,\sigma})b_\sigma(z)=\kappa p_N(z)w.
 \tag{5}
\]
For the first identity, the continuant recurrence cancels rows
\(0,\ldots,d-1\). The remaining endpoint row is a multiple of
\(p_N(z)\): it vanishes at every physical root by the conjugate
eigenvector identity in T. Its leading coefficient is \(q/N\),
since the leading coefficient of \(r_\nu(z)_d\) is
\((-1)^dq^{d^2}/N=-q/N\).
K's endpoint inverse row gives
\[
 (U_\sigma^{-1})_{t,d}=q^dN/p_N'(\lambda_t).
\]
Multiplying the first equation by \(\kappa U_\sigma^{-1}\)
therefore proves the second, including its sign \(q^N=-1\).

Finite reciprocity in T gives
\[
 r_\nu(\lambda_t)_a
     =q^{-a}\overline{(U_\nu)_{a,t}},\qquad
 b_\sigma(\lambda_t)=B^+_{\nu,\sigma}e_t.
 \tag{6}
\]
Thus this is a polynomial continuation of the actual columns,
not a newly chosen eigenline. Its off-root forcing is retained.
Since \(b_\sigma\) has degree at most \(d\), (5) also gives
\[
 b_\sigma(z)=\kappa\operatorname{adj}(zI-J_{\nu,\sigma})w.
 \tag{7}
\]
One may first prove this for \(p_N(z)\ne0\), then use polynomial
identity. In particular its leading coefficient is \(\kappa w\).

Define the original quadratic height phase and a diagonal gauge
\[
 f_t=e^{i\pi t(t+1)/(4N)},\qquad
 S=\operatorname{diag}((-1)^t\mu_t/f_t),\qquad f=(f_t)_t,
\]
\[
 L_{\nu,\sigma}=q^{-1/2}S^{-1}J_{\nu,\sigma}S,\qquad
 g_\sigma(\zeta)=S^{-1}b_\sigma(\sqrt q\,\zeta).
\]
Equations (1),(2),(5) now become
\[
 \boxed{\quad
 (\zeta I-L_{\nu,\sigma})g_\sigma(\zeta)
      =\frac{\kappa}{N}\pi_N(\zeta)f,\qquad
 g_\sigma(\zeta)=\frac{\kappa}{N}
          \operatorname{adj}(\zeta I-L_{\nu,\sigma})f .
 \quad}                                                     \tag{8}
\]
Indeed \(S^{-1}w=f/(Nq^{d/2})\). The vector \(f\) is universal:
it is independent of both actual neighboring heights.

At \(\zeta=\zeta_t\), (6) gives all the original crossing columns
after this specified gauge. For \(\pi_N(\zeta)\ne0\), (8) gives
\[
 (\zeta I-L_{\nu,\sigma})^{-1}f
                 =\frac{N\,g_\sigma(\zeta)}{\kappa\pi_N(\zeta)}.
 \tag{9}
\]
Consequently the spectral residue at \(\zeta_t\) is
\(N g_\sigma(\zeta_t)/(\kappa\pi_N'(\zeta_t))\).
These residues cannot be discarded when using the off-root response.

## 3. Primitive cyclicity over the cyclotomic lattice

Put \(\mathcal O_N=\mathbb Z[\sqrt q,1/(2N)]\subset\mathbb C\).
All the displayed roots, phases and matrix entries lie in this ring.
The factors \(1-Q^a\), \(1\le a<N\), are units, since their
product is \(N\). Also
\[
 \prod_{t=0}^d\mu_t=2^{1-N},
\]
The two products follow by evaluating \((x^N-1)/(x-1)\) and
\(x^N+1\) at one; rewriting the latter factors as sines gives
this half-grid product, with phases cancelling.
Thus every \(\mu_t\) is a unit. Equation (2) then shows that every
\(p_N'(\lambda_t)\), and every root difference, is a unit.
The same holds for the normalized roots \(\zeta_t\).
Thus the Vandermonde matrices are unimodular.

Each \(D_a(\lambda;\sigma)\) is monic of degree \(a\) in \(\lambda\).
Factoring \(U_\sigma\) into its row coefficient matrix and the
Vandermonde shows
\[
 U_\sigma,\ S\in\operatorname{GL}_N(\mathcal O_N).
 \tag{10}
\]
The leading row coefficient is \(q^{-a}/F_a\), a unit.
This argument applies to every actual \(\sigma\).

There is a particularly simple initialized cyclicity proof.
Polynomial interpolation gives
\[
 \sum_t D_a(\lambda_t;\sigma)/p_N'(\lambda_t)
     =\begin{cases}0,&a<d,\\1,&a=d.\end{cases}
\]
Writing \(W_\sigma=U_\sigma S\), it follows that
\[
 U_\sigma w=q^{-d}e_d/N,\qquad
 W_\sigma f=q^{-d/2}e_d.                                  \tag{11}
\]
The \(N\) vectors \(e_d,J_\nu'e_d,\ldots,(J_\nu')^de_d\)
form a unimodular basis: in reverse coordinate order their matrix
is triangular, with diagonal products of the nonzero upper arrows
\(q(1-Q^{-a})\), \(1\le a<N\), all units.
Conjugating by \(W_\sigma\) and multiplying by the unit powers of
\(\sqrt q\) proves
\[
 [f,L_{\nu,\sigma}f,\ldots,L_{\nu,\sigma}^df]
                   \in\operatorname{GL}_N(\mathcal O_N).
 \tag{12}
\]
In particular \(f\) is a primitive cyclic source, including \(N=2\).
This is stronger than a complex rank assertion. No norm estimate
or asymptotic comparison is inferred from unimodularity.

Let
\[
 \mathcal E_N=\mathcal O_N[\zeta]/(\pi_N(\zeta)).
\]
Equation (4) gives \(\pi_N(L_{\nu,\sigma})=0\).
Evaluation \(p\mapsto p(L_{\nu,\sigma})f\) is therefore an
isomorphism of free rank-\(N\) modules. The roots have unit
differences, so \(\mathcal E_N\cong\prod_t\mathcal O_N\).
The cyclic generators of this module form a torsor for
\(\mathcal E_N^\times\): \(p(L)f\) is a generator exactly when
\(p\) is a unit in \(\mathcal E_N\).
This is a finite-level module statement, with rank growing with \(N\).

## 4. The original marked row fixes a unit residue

Now specialize only \(\nu=c=1+q=\lambda_0\). Keep \(\sigma\)
arbitrary among the physical roots. The original row of N is
\[
 r_\sigma=(\Phi_{\lambda_t,\sigma}(-q))_t,\qquad
 \Phi_{\lambda,\sigma}(z)=\sum_{a=0}^d
                               D_a(\lambda;\sigma)z^a/F_a.
\]
Its exact source identities, with the original lift, are
\[
 r_\sigma J_{c,\sigma}=\lambda_*r_\sigma,\qquad
 r_\sigma B^+_{c,\sigma}
       ={2\kappa\over1-q^3}e_*^{\mathsf T},\qquad
 \lambda_*=-q^{-1}-q^2=\lambda_{N-2}.
 \tag{13}
\]
For completeness, put \(v_a=(-Q)^a\).
Then \(r_\sigma=v^{\mathsf T}U_\sigma\), and the second identity
reduces to the finite product evaluation of
\(\overline{\Phi_{\lambda_t,c}(-Q^{-1})}\).
Its product vanishes except at \(t=N-2\); there its value is
\(2/(1-q^3)\). This is N's literal same-sign cap-slide identity.

Interpolation of the degree-\(d\) polynomial \(r_\sigma b_\sigma(z)\)
using (6),(13) gives
\[
 r_\sigma b_\sigma(z)
   ={2\kappa\over1-q^3}
          {p_N(z)\over(z-\lambda_*)p_N'(\lambda_*)},\qquad
 r_\sigma w={2\over(1-q^3)p_N'(\lambda_*)}.                  \tag{14}
\]
Define
\[
 \ell_\sigma=r_\sigma S,\quad
 \zeta_*=\lambda_*/\sqrt q=-2\cos(3\pi/(2N)),\quad
 \omega_N=i(-1)^{N-2}q^{-3/2}.
\]
Then \(|\omega_N|=1\), \(\omega_N\in\mathcal O_N^\times\), and
\[
 \ell_\sigma f
 ={2(-1)^{N-2}\sin(3\pi/(2N))\over1-q^3}=\omega_N.
\]
Thus the initialized marked response is exactly
\[
 \boxed{\quad
 \ell_\sigma(\zeta I-L_{c,\sigma})^{-1}f
       ={\omega_N\over\zeta-\zeta_*},\qquad
 \ell_\sigma g_\sigma(\zeta)
       ={\kappa\omega_N\over N}
                       {\pi_N(\zeta)\over\zeta-\zeta_*}.
 \quad}                                                     \tag{15}
\]
The second expression is a polynomial, not a nonvanishing
function on the full spectral plane. It has the other \(N-1\)
physical roots as zeros; at \(\zeta_*\) its value is
\(2\kappa/(1-q^3)\).

Equivalently, on the full finite module,
\[
 \ell_\sigma p(L_{c,\sigma})f=\omega_N p(\zeta_*).
 \tag{16}
\]
The cyclic generators with marked value \(\omega_N\) are precisely
the units \(p\in\mathcal E_N^\times\) satisfying \(p(\zeta_*)=1\).
This describes the mark-normalized subtorsor without rescaling the row.

All identities include \(N=2\). For example, at \(\sigma=c\),
\[
 L_{c,c}=\begin{pmatrix}3\sqrt2&-4\\4&-3\sqrt2\end{pmatrix},
 \quad \ell_c=(\sqrt2,-1),\quad f=(1,\kappa)^{\mathsf T},
 \quad \omega_2=\overline\kappa.
\]
Equation (15)'s polynomial is \((\zeta+\sqrt2)/2\).
No argument has divided by \(1+Q\).
Here \(\ell_\sigma\) is the canonically normalized mode row.
For N's literal four-head row
\((\ell_{12}\otimes m_{34})R_{23}^+\), at fixed \(\sigma\),
the row after the \(S\) change is \(\beta_N\ell_\sigma\), where
\[
 \beta_N=\frac{T_*}{A_c}\frac{\kappa(1-q)}2 .
\]
The constants \(T_*,A_c\) are N's original marked and ordinary
boundary constants. Its physical residue is therefore
\(\beta_N\omega_N\), with any original \(\chi_N\) still external.
C's opposed local contraction retains this same stated \(\beta_N\);
that different contraction is not identified with (15)'s polynomial.

## 5. Exact commuting comparison under a neighboring-height change

Fix a physical reference root \(\sigma_0\), and work first in
\(\mathcal O_N[z]/(z^N)\). The recurrence (3) gives, below degree \(N\),
\[
 (1-\lambda z+qz^2)\Phi_{\lambda,\sigma}(z)
     =N_\sigma(z)\Phi_{\lambda,\sigma}(Qz),\qquad
 N_\sigma(z)=1+q\sigma z+qQz^2.                              \tag{17}
\]
Its constant-one solution is unique, since \(1-Q^m\) is a unit
for \(0<m<N\). The unique constant-one solution of
\[
 R_{\sigma,\sigma_0}(z)N_{\sigma_0}(z)
        =N_\sigma(z)R_{\sigma,\sigma_0}(Qz)\pmod {z^N}
\]
also has coefficients in \(\mathcal O_N\), by the same triangular
recursion. Uniqueness in (17) now proves
\[
 \Phi_{\lambda,\sigma}
      =R_{\sigma,\sigma_0}\Phi_{\lambda,\sigma_0}\pmod {z^N}
 \quad\hbox{for every }\lambda .
 \tag{18}
\]
The multiplier is independent of \(\lambda\).
If \(R=\sum_{m=0}^d R_mz^m\) and \(Z e_a=e_{a+1}\), with \(Ze_d=0\),
then (3),(18) give
\[
 A_\sigma:=U_\sigma U_{\sigma_0}^{-1}
       =\sum_{m=0}^d q^{-m}R_m Z^m.
 \tag{19}
\]
These are unit lower triangular Toeplitz matrices, all polynomials
in the same nilpotent shift. They commute, have determinant one,
and their inverses have the same form.

Over \(\mathbb C\) the finite logarithm makes the comparison explicit:
\[
 \log A_\sigma
 =\sum_{m=1}^d q^{-m}
  { [z^m](\log N_\sigma(z)-\log N_{\sigma_0}(z))
          \over1-Q^m}\,Z^m.                                \tag{20}
\]
No assertion that all denominators of this logarithm are units
in \(\mathcal O_N\) is needed; integral (18),(19) came first.

For fixed physical \(\nu\), put
\[
 H_{\sigma'\leftarrow\sigma}
  =S^{-1}U_{\sigma'}^{-1}U_\sigma S
  =S^{-1}U_{\sigma_0}^{-1}A_{\sigma'}^{-1}
                                    A_\sigma U_{\sigma_0}S .
\]
Then the full initialized comparisons obey
\[
 H_{\sigma'\leftarrow\sigma}L_{\nu,\sigma}
       =L_{\nu,\sigma'}H_{\sigma'\leftarrow\sigma},\quad
 H_{\sigma'\leftarrow\sigma}f=f,\quad
 H_{\sigma'\leftarrow\sigma}g_\sigma=g_{\sigma'},
\]
\[
 H_{\sigma''\leftarrow\sigma'}
 H_{\sigma'\leftarrow\sigma}=H_{\sigma''\leftarrow\sigma},\qquad
 \ell_{\sigma'}H_{\sigma'\leftarrow\sigma}=\ell_\sigma
                                      \quad(\nu=c).
 \tag{21}
\]
The first equations follow by conjugation and (11); the last follows
from \(r_\sigma=v^{\mathsf T}U_\sigma\). The comparisons are the
unique \(L\)-intertwiners fixing \(f\), by (12).
They lie in a single conjugate abelian unipotent group. This does
not assert a bound on matrix rank or nilpotency index independent of \(N\),
and is not a statement about the braid group.

## 6. Scope and prior coverage

K already supplies polynomial coideal kernels and their endpoint
normalization. N supplies the marked cap-slide row and its exact
scalar; T supplies the actual crossing and inverse frame.
C supplies a different scalar quantum connection on the finite
height clock, its initialized line and a specified off-cut rational
representative. None of its moving-variable or contour conclusions
is being extended here.

F's cyclic comparison principle is realized explicitly by (11),(21)
for this finite neighboring-height family. Its fixed-rank whole
quantum-lifting hypotheses are not inferred: the present rank is \(N\).
Nor is the neighboring-height coordinate a preferred knot meridian.
For example \(N_\sigma(z)=\det(I+q^{3/2}zM_\sigma)\), where
\(M_\sigma=\left(\begin{smallmatrix}\sigma/\sqrt q&-1\\1&0\end{smallmatrix}\right)\);
this identifies the explicit local Fricke matrix, not a knot A-component.

Every original root column and the marked functional are retained.
The off-root \(p_N\) forcing, the other polynomial zeros in (15),
and any literal boundary and exterior scalars remain.
No Bloch-regulator identification, geometric contour coefficient,
or arbitrary-short-filling scalar lower bound follows from this
source-algebraic period and its flat abelian framing.

| Key | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| N | [Actual marked difference equation](research_coideal_marked_boundary_normal_gap.md) | 512 | bb9bd6d04480ae8733c0fd1c5901834bdf2ea3e8c7eb3617fb8eb58e66e57956 |
| T | [Exact crossing transport](research_coideal_crossing_orthogonality_transport.md) | 595 | 4555fecc6377077dbdc4cfb3afac50f09d180efc5659716bac8497319310114c |
| K | [Original continuant kernel](research_coideal_continuant_source_kernel.md) | 365 | 3ea997e5258c9413fd7c771a6a1475b90b39bf731ac55c0902fd136943b26f44 |
| F | [Flat pointed comparison](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/flat_pointed_torsor_and_quantum_lifting.md) | 383 | 0508009a61d979391e9c2a91d3d25704a9cd3848d9048833f836a35f2acd8e20 |
| C | [Cyclic quantum connection](research_coideal_cyclic_quantum_connection.md) | 511 | 6a6c237c3ed1645394a6a0aea2e2f47d92bed416b230a9fef5263167ebb14178 |
