# Growing cap observations of an actual geometric source

Research deduction, 8 November 2026. No numerical evaluation is used.

The original geometric crossing source remains exponentially small
under every bounded observation supported on its entire distinct-node
half together with a growing window at the opposite endpoint. The
window may have sublinear width, or a sufficiently small fixed
positive fraction of all indices. This is a statement about the
actual source line, rather than a failure of coercivity somewhere
in the full space.

The sharp original coefficient profile also identifies the exact
macroscopic threshold. Below it the projection has a strictly
negative exponential rate; above it the projection recovers the
normalized source with exponentially small error. At the threshold
itself only the exponential rate is determined here.

It strengthens the fixed-polynomial obstruction in
[original almost-invariance and observation](research_original_almost_invariance_and_observation.md),
Theorem 2. It does not exclude a composition argument with a different,
proved observation of the full source.

## 1. Exact source and inherited inputs

Fix an integer \(k\ge2\), independently of \(N\), and put
\[
 D=N-1,\qquad q=e^{\pi i/N},\qquad
 S_h=\prod_{\nu=1}^h2\sin(\pi\nu/N),\quad S_0=1,\qquad
 \kappa=e^{\pi iD^2/(2N)}.
 \tag{1}
\]
Use the complete original Newton algebra
\(\mathbb C[z]/(2T_N(z/2)+2)\), with crossing matrix \(M_N\),
coordinate vectors \(\mathbf e_j\), and Casimir multiplication \(C_N\).
Set
\[
 \alpha_N=M_N^{2k}\mathbf e_0,\qquad
 a_N=\frac{\alpha_N}{\|\alpha_N\|_2},\qquad
 \chi_k=\frac{\operatorname{Vol}(S^3\setminus\mathcal K_k)}{4\pi}>0,
 \quad \mathcal K_k=C(R^{-2k}T(R^{2k})).
 \tag{2}
\]
The [reflected volume theorem](research_reflected_even_kashaev_volume_theorem.md),
equations (3)--(5), and the
[Casimir insertion theorem](research_even_reflected_casimir_insertions.md),
Theorem 3, give
\[
 \|\alpha_N\|_2=e^{N\chi_k+o(N)},\qquad
                  \|(C_N-z_k)a_N\|_2\longrightarrow0 .
 \tag{3}
\]
Both statements concern the entire original column, through all
integer levels. The latter is not a unitary-representation assertion.

The exact backward source of
[the endpoint theorem](research_even_run_backward_source_growth.md),
equations (2)--(5) and Theorem 1, is
\[
 \alpha_{N,D-h}=\kappa^{2k}\mathbf e_k^T u_{D-h},\qquad
 g_h=S_h^2u_{D-h},\qquad
 g_0=u_D,\qquad g_h=H_{N-h}g_{h-1}.
 \tag{4}
\]
Its complete initialized endpoint satisfies
\(\|u_D\|_2\le C_kN^{3/2}\), and \(\|H_j\|_2\le4\).
The last bound is the original tridiagonal bound used in
[the reflected Stein theorem](research_reflected_laurent_stein_energy.md),
Section 2. In particular no free homogeneous solution replaces
\(u_D\) in (4). Consequently,
\[
 |\alpha_{N,D-h}|
       \le C_kN^{3/2}\frac{4^h}{S_h^2},
                       \qquad 0\le h\le D.
 \tag{5}
\]
The original low-color theorem, equation (15) of
[the full distinct-node calculation](research_original_low_color_bound.md),
also gives
\[
 |\alpha_{N,j}|\le \csc\frac{\pi}{2N}\le N,
                \qquad 0\le j\le \left\lfloor\frac D2\right\rfloor.
 \tag{6}
\]
Its odd last distinct node is included. None of (4)--(6) deletes
the original first normals at the remaining double roots.

## 2. Observation on the actual source line

For \(0\le L\le D\), let \(P_{L,N}\) be the
Euclidean orthogonal projection onto
\[
 W_{L,N}
  =\operatorname{span}\{\mathbf e_j:0\le j\le\lfloor D/2\rfloor\}
       +\operatorname{span}\{\mathbf e_{D-h}:0\le h\le L\}.
 \tag{7}
\]
The first summand is deliberately the whole distinct-node half,
not just the first cap.

**Theorem 1.** Uniformly for \(0\le L\le\lfloor N/6\rfloor\),
\[
 1\le\|P_{L,N}\alpha_N\|_2
       \le C_k N^{3/2}\sqrt{L+1}\frac{4^L}{S_L^2}.
 \tag{8}
\]
If \(L_N=o(N)\), then
\[
 \boxed{\quad
 \lim_{N\to\infty}\frac1N
       \log\|P_{L_N,N}a_N\|_2=-\chi_k .
 \quad}
 \tag{9}
\]
In particular this is the exact exponential rate of the norm of
the restriction of \(P_{L_N,N}\) to the actual one-dimensional
source space \(\mathbb C\alpha_N\).

For a fixed \(0<\delta<1/6\) and \(L_N=\lfloor\delta N\rfloor\),
\[
 \limsup_{N\to\infty}\frac1N
       \log\|P_{L_N,N}a_N\|_2
    \le \Phi_k(\delta)-\chi_k,\qquad
 \Phi_k(\delta):=\delta\log4-2J(\delta),
 \quad J(x)=\int_0^x\log(2\sin\pi t)\,dt .
 \tag{10}
\]
The notation \(\Phi_k\) keeps its use with the fixed source;
the displayed function itself is independent of \(k\).
There is a fixed \(\delta_k>0\) for which the right side of
(10) is less than \(-\chi_k/2\).

*Proof.* The lower bound in (8) is exact:
\(\alpha_{N,0}=\kappa^{2k}\), since \(M_N\) is lower triangular
with first diagonal entry \(\kappa\). The squared sum in (6) is
at most \(N^3\). For \(h\le L\le N/6\), all the factors of
\(S_h\) are at most one, so \(4^h/S_h^2\) is increasing in \(h\).
Sum (5) over the other window and absorb the first squared sum
in the same right side. This proves (8).

For clarity, sublinear widths do not require a fixed-index
factorial asymptotic. On \(0\le t\le1/2\),
\(2\sin\pi t\ge4t\). Therefore, for \(L\ge1\),
\[
 S_L\ge(4/N)^L L!,\qquad
 \frac{4^L}{S_L^2}
   \le\left(\frac{eN}{2L}\right)^{2L}.
 \tag{11}
\]
Here \(L!\ge(L/e)^L\) follows by integrating \(\log t\).
If \(L_N=o(N)\), the logarithm of the last bound is \(o(N)\),
because \(x\log(e/(2x))\to0\) as \(x\downarrow0\).
For \(L=0\) the quotient equals one. Equations (8), (11)
and (3) prove both sides of (9).

For fixed \(\delta\), the elementary sine-product Riemann sum gives
\[
 \frac1N\log S_{\lfloor\delta N\rfloor}\longrightarrow J(\delta).
 \tag{12}
\]
One can verify (12) by writing
\(\log(2\sin\pi t)=\log t+
 \log(2\sin\pi t/t)\): the second summand is continuous at zero,
and the first is an integrable logarithm, whose product is a factorial.
Thus (8) proves (10) without an evaluation of \(J\).
Finally \(\delta\log4-2J(\delta)\to0\) at zero, whereas
\(\chi_k>0\); this proves the last assertion. \(\square\)

For any rows \(\ell_N=\ell_NP_{L_N,N}\) with
\(\|\ell_N\|_2\le e^{o(N)}\), (9) implies
\[
 \limsup_N N^{-1}\log|\ell_Na_N|\le-\chi_k.
 \tag{13}
\]
This holds even if the rows are chosen using knowledge of the
particular source. Zeros have logarithm \(-\infty\).
The same statement holds for maps to any finite-dimensional
Hilbert space whose operator norm is subexponential. Thus changing
the basis of observations within this window cannot remove the
loss at subexponential cost.

## 3. A growing family of original Casimir cap tests

The exact original matrix is
\[
 (C_Nv)_j=2\cos((2j+1)\pi/N)v_j
             -4\sin^2(\pi j/N)v_{j-1},
 \qquad v_{-1}=0,\qquad \|C_N\|_2\le6 .
 \tag{14}
\]
For an integer \(0\le L\le D\), define the complete two-cap observation
map and its positive Gram matrix by
\[
 \mathcal O_{L,N}v
    =\big(\mathbf e_0^\dagger C_N^jv,
                 \mathbf e_D^\dagger C_N^jv\big)_{j=0}^{L},
 \qquad G_{L,N}=\mathcal O_{L,N}^\dagger\mathcal O_{L,N}.
 \tag{15}
\]
These are actual Casimir insertions at the two specified caps.
They are not closing-twist observations or a moving ordinary color.

For \(j\le L\), the last row of \(C_N^j\) is supported on
\(D-L,\ldots,D\), while its first row is a multiple of
\(\mathbf e_0^\dagger\). Hence
\[
 \mathcal O_{L,N}=\mathcal O_{L,N}P_{L,N},\qquad
 \|\mathcal O_{L,N}\|_2\le\sqrt{2(L+1)}\,6^L .
 \tag{16}
\]
The zero-th first-cap component still equals \(\kappa^{2k}\)
when applied to \(\alpha_N\).

**Corollary 2.** For every \(L_N=o(N)\),
\[
 \boxed{\quad
 \lim_N\frac1N\log\|\mathcal O_{L_N,N}a_N\|_2=-\chi_k,
 \qquad
 \lim_N\frac1N\log(a_N^\dagger G_{L_N,N}a_N)=-2\chi_k .
 \quad}
 \tag{17}
\]
For fixed \(0<\delta<1/6\) and \(L_N=\lfloor\delta N\rfloor\),
\[
 \limsup_N\frac1N\log\|\mathcal O_{L_N,N}a_N\|_2
       \le \delta\log24-2J(\delta)-\chi_k.
 \tag{18}
\]
In particular a fixed sufficiently small positive observation
fraction still gives a strictly negative rate.

*Proof.* Combine (8), (16) and (3) for the upper bounds.
The retained zero-th first-cap observation gives the lower bound
needed for (17). Taking the squared norm proves its Gram statement.
Continuity at \(\delta=0\) proves the last assertion. \(\square\)

The same upper bound applies to any polynomial family
\(P_N(C_N)\) of degree at most \(L_N\), tested at either cap,
provided its cap-row norm is at most \(e^{o(N)}\).
This is not a claim about arbitrary growing polynomial coefficients:
a large coefficient norm is an observation cost and must be retained.

## 4. The required cost of source reconstruction

Let \(L_N=o(N)\), and suppose a linear reconstruction map
\(R_N:W_{L_N,N}\to\mathbb C^N\) satisfies, for a fixed
\(0\le\varepsilon<1\),
\[
       \|R_NP_{L_N,N}\alpha_N-\alpha_N\|_2
                          \le\varepsilon\|\alpha_N\|_2 .
 \tag{19}
\]
Then, even though (19) is required only on this one actual source,
\[
 \|R_N\|_2\ge
        \frac{1-\varepsilon}{\|P_{L_N,N}a_N\|_2},
 \qquad
 \liminf_N N^{-1}\log\|R_N\|_2\ge\chi_k .
 \tag{20}
\]
The proof is the reverse triangle inequality followed by the
operator norm bound. Replacing \(P_{L_N,N}\) by
\(\mathcal O_{L_N,N}\) gives the same conclusion by (17).
For fixed \(\delta\), the lower exponent supplied by (20)
is respectively \(\chi_k-\Phi_k(\delta)\) or
\(\chi_k-\delta\log24+2J(\delta)\), when positive.

The exact recurrence (4) can reconstruct the source from its full
initialized endpoint data. There is no contradiction: its accumulated
amplification is exponential. In particular small endpoint errors
cannot be transported at polynomial cost merely because the
channel dimension \(k\) is fixed or the local selected mode is known.

For the source-line composition criterion in
[the marked observation note](research_source_adapted_observation_composition.md),
take its proposed direction to be the actual \(a_N\) and its final
row to be the original first cap. Its closing quantities are exactly
\[
 \gamma_N=|\mathbf e_0^\dagger a_N|
             =e^{-N\chi_k+o(N)},\qquad
 \beta_{\partial,N}
    =\|\mathbf e_0^\dagger(I-a_Na_N^\dagger)\|
             =\sqrt{1-\gamma_N^2}.
 \tag{21}
\]
Thus its sharp observation condition
\(\gamma_N>\beta_{\partial,N}\rho_N\) requires an exponentially
small complementary radius. This remains true for a vector which
is already a geometric quasimode by (3); a merely vanishing
Casimir residual does not verify that closing condition.

These conclusions use the actual initialized crossing source and
preserve both level parities. Reversing the crossing sign conjugates
the full column and gives the same norm statements. They do not
assert that a dense further crossing or turn has its observation
supported in (7), do not bound an arbitrary mixed-word closing
coefficient from below, and do not enlarge a knot-family theorem.
A successful source-specific propagation may use a different
observation with proved nonzero coupling, or retain the exponential
amplification and control its phase and boundary forcing. The present
result rules out replacing that work by subexponentially conditioned
endpoint-window reconstruction of this actual geometric source.

## 5. The exact macroscopic projection threshold

The preceding elementary cutoff bound can be made sharp using
the already proved original coefficient profile. Retain the
classical matrix and selected branch of
[sharp reflected growth](research_even_run_sharp_reflected_growth.md),
Sections 1--4:
\[
 \begin{split}
 H_k(\theta)&=2\cos\theta\,I-T_k-e^{-i\theta}E_{11}-E_{kk},\\
 \lambda_*(0)&=4\cos^2(\pi/(2k)),\\
 x_k&=\theta_k/(2\pi)\in(0,1/4),\qquad
        |\lambda_*(\theta_k)|=2-2\cos\theta_k,\\
 B_k(x)&=\int_0^x\log|\lambda_*(2\pi t)|\,dt-2J(x),
                                      \qquad 0\le x\le x_k .
 \end{split}
 \tag{22}
\]
Here \(T_k\) is path adjacency, and \(\theta_k\) is the unique
unit-growth crossing on the original selected branch.
The same theorem proves
\[
 B_k(0)=0,\qquad B_k'(x)>0\quad(0<x<x_k),\qquad
                             B_k(x_k)=\chi_k .
 \tag{23}
\]
The last equality follows by comparing its full reflected norm
limit with (3), with no new normalization or evaluation.

**Theorem 3.** If \(0\le L_N\le D\) and \(L_N/N\to\delta\in[0,1]\),
then
\[
 \boxed{\quad
 \lim_{N\to\infty}\frac1N\log\|P_{L_N,N}a_N\|_2
       =B_k\bigl(\min\{\delta,x_k\}\bigr)-B_k(x_k).
 \quad}
 \tag{24}
\]
If \(\delta>x_k\), there are \(c>0\) and \(N_0\) such that
\[
 \|(I-P_{L_N,N})a_N\|_2\le e^{-cN}\quad(N\ge N_0),
 \qquad
                  \|P_{L_N,N}a_N\|_2\longrightarrow1 .
 \tag{25}
\]
At \(\delta=x_k\), (24) asserts rate zero; it does not specify
a limiting mass fraction or assert (25).

*Proof.* We record the exact scope of the inherited estimates.
Let
\[
 E_k(x)=\int_0^x\log\rho(H_k(2\pi t))\,dt-2J(x),
                                    \qquad 0\le x\le1/4.
 \tag{26}
\]
The sharp-growth theorem proves that \(E_k=B_k\) on \([0,x_k]\)
and that this function is strictly increasing there. The uniform
all-mode product estimate used in that theorem, also recorded in
equation (8) of the
[Casimir insertion note](research_even_reflected_casimir_insertions.md),
gives
\[
 \log|\alpha_{N,D-h}|
      \le N E_k(h/N)+o(N),\qquad 0\le h\le\lfloor N/4\rfloor,
 \tag{27}
\]
with one error uniform over these indices, including \(h=0\).
The nonzero actual initialized coefficient estimate, equation (28)
of the sharp-growth theorem, gives
\[
 \log|\alpha_{N,D-h}|
        =N B_k(h/N)+O_k(\log N)
 \tag{28}
\]
uniformly on every fixed compact subinterval of
\((0,x_k+\varepsilon_k)\), for some fixed \(\varepsilon_k>0\).
Here the implicit constant may depend on the compact interval.
The branch in (22) extends to that interval as in the cited proof.
Both (27) and (28) concern the original column with its actual
nonzero endpoint-mode coefficient, not an independently chosen
solution of the recurrence.

Suppose first \(0<\delta<x_k\). For large \(N\), every index
\(0\le h\le L_N\) is in the range of (27), and monotonicity gives
\[
 \sum_{h=0}^{L_N}|\alpha_{N,D-h}|^2
       \le (L_N+1)\exp\{2N B_k(L_N/N)+o(N)\}.
 \tag{29}
\]
The other half of the projection has squared norm at most \(N^3\)
by (6). Since \(B_k(\delta)>0\), this polynomial term does not
change the upper exponential rate in (29). For the lower bound
retain the single actual coefficient \(h=L_N\) in (28).
Continuity of \(B_k\), followed by division by (3), proves (24)
in this case. At \(\delta=0\), \(L_N=o(N)\), so (9) proves it.

At \(\delta=x_k\), the projection norm is at most one. For every
fixed \(x\in(0,x_k)\), an index \(h_N=\lfloor Nx\rfloor\) belongs
to the retained window for all sufficiently large \(N\). Formula
(28) at that index gives
\[
 \liminf_N N^{-1}\log\|P_{L_N,N}a_N\|_2
                             \ge B_k(x)-B_k(x_k).
 \tag{30}
\]
Let \(x\uparrow x_k\). This proves rate zero, including sequences
which approach the threshold from below, without a claim about
the finer distribution in its critical window.

Finally let \(\delta>x_k\). Choose a fixed \(\varepsilon>0\)
small enough that \(x_k+2\varepsilon<\delta\).
Every omitted index then has \(h=D-j>L_N\), and hence
\(|h/N-x_k|\ge\varepsilon\), for all large \(N\).
The complete-column concentration theorem, Lemma 1 of the
Casimir insertion note, proves
\[
 \sum_{|(D-j)/N-x_k|\ge\varepsilon}|\alpha_{N,j}|^2
                       \le e^{-\gamma_\varepsilon N}
                                  \|\alpha_N\|_2^2,
 \qquad \gamma_\varepsilon>0 .
 \tag{31}
\]
It includes all original indices, not just the first quarter of
the backward recurrence. Equation (31) proves (25), with
\(c=\gamma_\varepsilon/2\), and thus (24) for \(\delta>x_k\).
The argument also covers \(\delta=1\). \(\square\)

There is a sharp source-line reconstruction interpretation.
Let \(r_N\) be the least operator norm of a linear map
\(R:W_{L_N,N}\to\mathbb C^N\) satisfying
\(R P_{L_N,N}\alpha_N=\alpha_N\). Since the first coefficient
of the projected source is nonzero, this set of maps is nonempty.
Exactly,
\[
 r_N=\frac{\|\alpha_N\|_2}{\|P_{L_N,N}\alpha_N\|_2}
               =\frac1{\|P_{L_N,N}a_N\|_2},\qquad
 \lim_N\frac1N\log r_N
     =B_k(x_k)-B_k\bigl(\min\{\delta,x_k\}\bigr).
 \tag{32}
\]
The lower bound is (20) with zero error. It is attained by
\[
 Rv=\alpha_N\,
       \frac{(P_{L_N,N}\alpha_N)^\dagger v}
            {\|P_{L_N,N}\alpha_N\|_2^2}.
 \tag{33}
\]
This rank-one formula establishes the optimal conditioning on the
specified source line; it is not an algorithm reconstructing an
unknown source from its observed coordinates.

Thus the minimal exponential reconstruction cost drops to zero
exactly at the proved threshold \(x_k\). For \(\delta>x_k\),
the known coordinate inclusion \(W_{L_N,N}\hookrightarrow\mathbb C^N\)
already reconstructs the actual source with exponentially small
relative error by (25), and \(r_N\to1\). At equality only
\(r_N=e^{o(N)}\) is proved here. These conclusions concern the
coordinate projection (7); they do not assert that the unrescaled
Casimir Gram map (15) is well conditioned at that threshold.

