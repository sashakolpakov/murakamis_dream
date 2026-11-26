# Two boundary rows retain the full coideal period

24 November 2026. Research note. Written proof.

The full actual coideal crossing has a two-row boundary presentation
with its original forcing, both sorted folds and literal observation.
The reconstruction is polynomial, even at every Dirichlet pole.
At physical neighboring heights each raw boundary evaluation needs
at most four spectral derivatives; a raw full-period evaluation needs
at most eight. A three-row variant isolates the controlled positive
cooriented interiors without making the whole boundary operator positive.
These are initialized source identities, not an arbitrary Schur model.

The matrices and their polynomial degrees still grow with the level.
A fixed number of boundary rows does not give a fixed-dimensional source,
close a whole-word displacement rank, or bound its marked scalar below.

## 1. The initialized full operator

Use the complete conventions of P,N,G,J. Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad\delta=\pi/N,\quad\sqrt q=e^{\pi i/(2N)},
 \quad\kappa=q^{d^2/2},
\]
\[
 \lambda_t=2\sqrt q\cos\alpha_t,\quad
 \alpha_t=(t+\tfrac12)\delta,\quad\mu_t=\sin\alpha_t,
 \quad f_t=e^{i\delta t(t+1)/4},\quad
 T=\operatorname{diag}((-1)^t\mu_t/f_t).
 \tag{1}
\]
Both physical neighboring parameters are actual roots:
\(\nu=\lambda_v,\sigma=\lambda_s\), \(0\le v,s\le d\).
Let \(U_\sigma\) be the full continuant eigenmatrix and retain
\[
 (J'_\nu h)_a=(1-Q^{-a})h_{a-1}
 +q(1-Q^{-a-1})h_{a+1}-q^{-1}Q^{-a}\nu h_a,
\]
\[
 J_{\nu,\sigma}=U_\sigma^{-1}J'_\nu U_\sigma,
 \qquad L=q^{-1/2}T^{-1}J_{\nu,\sigma}T,
 \qquad \pi_N(\zeta)=2T_N(\zeta/2).
 \tag{2}
\]
Absent physical endpoint arrows are zero. P proves
\(\det(\zeta I-L)=\pi_N(\zeta)\), whose roots
\(\zeta_r=2\cos\alpha_r\) are simple. Its initialized crossing column is
\[
 g(\zeta)={\kappa\over N}\operatorname{adj}(\zeta I-L)f,
 \qquad (\zeta I-L)g(\zeta)
             ={\kappa\over N}\pi_N(\zeta)f.
 \tag{3}
\]
Here \(f=(f_t)\) is the specified universal chirp, independent of
\(\nu,\sigma\). At physical input roots these are the actual crossing
columns in the stated gauge. No eigenvector can be rescaled freely.
For any prescribed transformed row \(\ell\), the observation is \(\ell g\).
Original physical cap scales and the external \(\chi_N\) remain unchanged.

## 2. All sorted arrows, including the folds

Write \(a=\cos\alpha_v,b=\cos\alpha_s\),
\(\theta=\alpha_t,x=\cos\theta\), and define
\[
 c_t^\pm={ (\cos(\theta\pm\delta)+a)
                 (\cos(\theta\pm\delta)+b)
                  \over\sin\theta\sin(\theta\pm\delta)},
 \qquad
 d_t={-2[x(1+ab)+(a+b)\cos\delta]
                    \over\sin^2\theta-\sin^2\delta}.
 \tag{4}
\]
All displayed denominators are nonzero half-grid factors.
For \(N\ge3\), the full source matrix has diagonal \(d_t\), ordinary
arrows \(L_{t,t+2}=c_t^+\), \(L_{t,t-2}=c_t^-\) when both indices
are in range, and the four additional folded arrows
\[
 L_{0,1}=c_0^-,\quad L_{1,0}=c_1^-,\qquad
 L_{N-2,d}=i c_{N-2}^+,\quad L_{d,N-2}=-i c_d^+.
 \tag{5}
\]
In particular the full operator is not declared real or positive.

Here is a source verification of the endpoint phases. Use N's sparse
entry calculation with \(c\) replaced by the actual external root \(\nu\),
as in T/P. On an ordinary forward edge it gives
\[
 (J_{\nu,\sigma})_{t,t+2}
 ={q^{t+2}(\cos((t+3/2)\delta)+a)
                 (\cos((t+3/2)\delta)+b)
        \over\mu_{t+2}\sin((t+3/2)\delta)}.
\]
For even \(t\), insert \(u=q^{-t-2},v=q^{t+3}\) in N's
\(a_jh_j\); for odd \(t\), swap them and use \(b_jh_{j-1}\).
Both substitutions give this same expression. Conjugating by T gives
(4). The physical roots repeat at reflected indices, while the continued
gauge satisfies
\[
 T_{-2}=T_1,\quad T_{-1}=T_0,\qquad
 T_N=-iT_d,\quad T_{N+1}=iT_{N-2}.
\]
Thus the reflected column entries are respectively
\(g_1,g_0,ig_d,-ig_{N-2}\), proving (5). The diagonal is unchanged.

At \(N=2\) define the matrix directly by (2); N's formula dividing by
\(1+Q\) is not used. With \(c=1+i\), the three cases are
\[
 L_{c,c}=\begin{pmatrix}3\sqrt2&-4\\4&-3\sqrt2\end{pmatrix},\quad
 L_{c,-c}=L_{-c,c}=\operatorname{diag}(\sqrt2,-\sqrt2),\quad
 L_{-c,-c}=\begin{pmatrix}3\sqrt2&4i\\4i&-3\sqrt2\end{pmatrix}.
 \tag{6}
\]
They follow from the literal two-by-two U and J' matrices and retain
\(\det(\zeta I-L)=\zeta^2-2\). No double-shift convention is needed.

## 3. Two boundary rows and exact polynomial reconstruction

Take \(B=\{0,d\}\), \(I=\{1,\ldots,d-1\}\), in that order.
For an empty I put \(D=1\) and omit all interior terms. Otherwise set
\[
 A=\zeta I-L_{II},\quad D=\det A,\quad C=\operatorname{adj}A,
\]
\[
 \widetilde H=D(\zeta I_2-L_{BB})-L_{BI}CL_{IB},\qquad
 \widetilde h=Df_B+L_{BI}Cf_I.
 \tag{7}
\]
Every entry is a finite polynomial. The exact determinant identity is
\[
                         \det\widetilde H=D\pi_N.
 \tag{8}
\]
Define the following quotients in the polynomial ring:
\[
 N_B=\operatorname{adj}(\widetilde H)\widetilde h,
 \qquad v_B=N_B/D,
\]
\[
 N_I=C[D\pi_N f_I+L_{IB}N_B],\qquad v_I=N_I/D^2.
 \tag{9}
\]
Both divisions are exact, including at all roots of D, and
\[
 g={\kappa\over N}(v_B,v_I),\qquad
 \ell g={\kappa\over N}(\ell_Bv_B+\ell_Iv_I).
 \tag{10}
\]
The ordering in (10) means the original B/I coordinates, not a physical
permutation of heads. All components have degree at most d.

For proof, first work where \(D\pi_N\ne0\). Ordinary block elimination
gives the Schur matrix \(\widetilde H/D\), forcing
\(\widetilde h/D\), and (8)--(10). There they equal the blocks of
\(\operatorname{adj}(\zeta I-L)f\). The latter are polynomial everywhere.
Polynomial identity therefore proves the exact divisibility in (9).
This does not assume a removable pole or choose a different solution.
Equivalently divide first for \(v_B\), then divide
\(C[\pi_Nf_I+L_{IB}v_B]\) by D for \(v_I\).

The interior forcing \(f_I\) occurs in BOTH (7) and (9). The prescribed
cap includes its \(\ell_Iv_I\) term. Neither can be deleted by replacing
the source with a homogeneous boundary eigenline. A boundary projection
may vanish on a mode; no boundary-coordinate faithfulness is asserted.

## 4. Every pole has a uniformly finite local evaluation

Removing 0 and d removes both folded edges. The remaining matrix is the
direct sum of two ordinary parity paths. Detailed balance gives
\[
 \mu_tc_t^+=\mu_{t+2}c_{t+2}^-,
\]
so \(\operatorname{diag}(\sqrt\mu)L_{II}
\operatorname{diag}(\sqrt\mu)^{-1}\) is real symmetric.
Negative or zero off-diagonal coefficients are retained.
Its only possible zero edges are at
\(t=N-v-2\) and \(t=N-s-2\), when these are interior edges.
Consequently there are at most four irreducible Jacobi components.
Each has simple real spectrum: an eigenvector is determined by its first
coordinate, which cannot vanish, and the symmetric matrix is diagonalizable.
Thus every root of D is real with multiplicity \(m\le4\).

At such a root \(\eta\), polynomial division gives componentwise
\[
 v_B(\eta)={N_B^{(m)}(\eta)\over D^{(m)}(\eta)},\qquad
 v_I(\eta)={N_I^{(2m)}(\eta)\over(D^2)^{(2m)}(\eta)}.
 \tag{11}
\]
These formulas require raw jets of order at most four and eight.
For a generic prescribed period, use the numerator
\(\ell_BN_BD+\ell_IN_I\) over \(D^2\), hence the same bound eight.
They apply unchanged when \(\pi_N(\eta)=0\). Sequential exact division
also works, but does not justify a raw full-state bound of four.
At N=2 there is no D-pole.
These are auxiliary \(\zeta\)-jets, not replacements for original
Casimir/Hermite normals or moving-color derivatives.

For the marked primitive \(\nu=c=1+q\), let \(\ell_\sigma^{\rm can}\)
be P's canonically normalized mode. Its physical marked row is
\(\beta_N\ell_\sigma^{\rm can}\), with the original \(\chi_N\) external.
Thus \(\beta_N\chi_N\) multiplies every period displayed for this
normalized mode; (10),(14) otherwise accept the prescribed physical row
without alteration. P gives
\[
 \ell_\sigma^{\rm can}g(\zeta)={\kappa\omega_N\over N}
       {\pi_N(\zeta)\over\zeta-\zeta_*},\quad
 \zeta_*=2\cos\alpha_{N-2},\quad
 \omega_N=i(-1)^{N-2}q^{-3/2},\quad |\omega_N|=1.
 \tag{12}
\]
At \(\zeta_*\) use \(\pi_N'(\zeta_*)\); at every other physical root
the normalized period is zero. It bypasses all D-poles while its physical
cap scale and external factor remain present.

## 5. Three rows expose the controlled positive interiors

Put \(S=\max(v,s)\), \(T_0=N-S-2\), \(u=T_0+1\).
If \(\mathcal C=\{0,\ldots,T_0\}\) is empty retain B={0,d}.
Otherwise take \(B_3=\{0,u,d\}\), removing duplicate indices.
The cooriented interior \(I_+=\{1,\ldots,T_0\}\) is separated from
the remaining interior by the exact cut \(T_0\leftrightarrow T_0+2\)
and by retaining u as a boundary row. The odd chain starts at row 1:
its actual incidence \(L_{1,0}=c_1^-\) is positive. The reverse folded
arrow \(L_{0,1}\) stays in the boundary data. Both folds remain explicit.

For the inequality only, order a,b numerically so that
\(a=\max(\cos\alpha_v,\cos\alpha_s)\), \(b=\cos\alpha_S\).
Equation (4) is symmetric in these scalars; no physical heads are swapped.
For each physical input \(r\in\mathcal C\), put \(y=\cos\alpha_r\).
The exact used-row identity is
\[
 \omega_t(y)=2\left[y+\cos\delta-
 {(1-a)(1-b)\over\cos\delta+\cos\alpha_t}\right]\ge cN^{-2}.
\]
With \(D_+=\operatorname{diag}(\sqrt{\mu_t})\), it follows that
\[
 cN^{-2}I\le D_+(2yI-L_{I_+I_+})D_+^{-1}\le CN^2I.
 \tag{13}
\]
Indeed its quadratic form is the sum of positive sine-conductance edge
squares, positive incident boundary squares, and
\(\sum\mu_t\omega_t|w_t|^2\), where \(w=D_+^{-1}z\).
The only boundary forcings are the original values at 0 and u.
This includes the positive row 1 omitted from J's chosen lower boundary.
For an off-root canonical column its known \(\pi_Nf_{I_+}\) forcing
must also remain. No positivity is asserted on the outside block or
on the full Schur matrix. At S=0, u=d and the unused upper fold is cut.
N=2 has empty controlled interior; N=3,S=0 has its single positive row 1.

The polynomial formulas work for any resulting boundary size b. Replace
\(I_2\) by \(I_b\) in (7). Then
\[
 \det\widetilde H=D^{b-1}\pi_N,\quad
 v_B={\operatorname{adj}(\widetilde H)\widetilde h\over D^{b-1}},
\]
\[
 v_I={C[D^{b-1}\pi_Nf_I+
 L_{IB}\operatorname{adj}(\widetilde H)\widetilde h]\over D^b}.
 \tag{14}
\]
Again these are exact polynomial quotients. Removing u can split only
one additional Jacobi component, so there are at most five; their root
multiplicities are at most five. The safe raw jet bounds for b=3 are
therefore ten at the boundary and fifteen for a full prescribed period.
Use the sharper four/eight bounds for the two-boundary presentation.
All empty-set and duplicate-boundary cases are covered by these conventions.

## 6. What is retained in a composition

The result gives the actual full crossing and prescribed observation from
small boundary matrices, with initialized interior forcing and exact
finite parts. More generally let \(\eta\) be any prescribed row independent
of \(\zeta\), including \(\eta=\ell A\) for a fixed actual short-component
composition \(A\) of compatible size. Equations (10),(11),(14) compute
its original period with the same raw jet bounds. The full \(A\),
complementary channels and external factors remain in \(\eta\);
no bound for \(\eta\) or its period is inferred.

The polynomial entries, Dirichlet spectra and path sizes still depend
on N and the actual neighboring heights. The real-spectrum and
multiplicity bounds require those physical root parameters; the
algebraic frame continuation in P does not extend them to complex heights.
The positive interior response is not a common positive braid metric.
A seam must transport source, boundary data, complementary channels and
marked row. No constant boundary-rank closure for overlapping faces,
phase alignment, global period lower bound or finite-exception theorem
is asserted. Full Casimir-normal data remain in the invertible source maps.

P supplies the initialized source and marked unit residue; N supplies
the actual sparse difference equation; G supplies its cooriented signs;
J supplies the common positive Jacobi response. The new content is the
full folded boundary presentation, source-preserving polynomial
reconstruction, and uniform local auxiliary pole order. No novelty for
abstract Schur complements or Jacobi spectral theory is claimed.

## Complete inputs

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| P | [Initialized marked period](research_coideal_normalized_marked_period.md) | 410 | e5e7ab88016f682411258ccab299f4b7bc2ab6e7052366729d59d993abf84d4b |
| N | [Actual source difference equation](research_coideal_marked_boundary_normal_gap.md) | 512 | bb9bd6d04480ae8733c0fd1c5901834bdf2ea3e8c7eb3617fb8eb58e66e57956 |
| G | [All cooriented amplitudes](research_coideal_cooriented_volume_kernel.md) | 613 | 78fabcccdd4eb8e2bf4064ec281880cc551443d2d36eb72750f27c77506bd597 |
| J | [Coherent Jacobi response](research_coideal_coherent_jacobi_cauchy_compiler.md) | 291 | c576185a591b325ed1a2e0a268d4a53bac5cccd8b77ef91b5f2ed84f87bdabd2 |

Only written mathematics, complete source reads and text/hash operations
were used. Earlier final notes, the ledger and public manuscripts remain unchanged.
