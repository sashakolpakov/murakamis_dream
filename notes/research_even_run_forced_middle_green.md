# The original input forcing in a middle-color Green estimate

Research note, 3 November 2026.

The all-column middle contraction gives a stable backward Green
estimate for an even run with arbitrary input. Its diagonal sources
must be retained: they are original resonant nullvectors, rather
than errors in a homogeneous recurrence. Subtracting those sources
gives an exact inhomogeneous equation whose propagated forcing
cancels after one step. The same equation forces quantitative
forward amplification of the prescribed input colors.

These estimates control an exact average of original outputs over
input-clock phases. They do not assert that a single coherent output
localizes for arbitrary input. A literal turn preserves the unweighted
input norm but reverses exponentially inequivalent response weights.
This identifies the additional estimate needed at a joined source.

## 1. Original fields and diagonal sources

Fix \(p=\sigma2k\), \(k\ge2\), \(\sigma\in\{1,-1\}\), and a
level \(N\ge2\). Put
\[
 D=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 q_\sigma=q^\sigma,\quad Q_\sigma=Q^\sigma,\quad
 \kappa=q^{D^2/2}.
 \tag{1}
\]
The original Newton crossing and turn are \(M,J\); the latter
reverses coefficient colors. For \(0\le j,\ell<N\), set
\[
 \begin{split}
 r_j&=q_\sigma Q_\sigma^j,\qquad
 d_j=4\sin^2(\pi j/N),\\
 C_j&=(r_j+r_j^{-1})I_k-T_k-r_jE_{11},\\
 \Lambda_\sigma&=\operatorname{diag}(Q_\sigma^{-\ell})_{\ell=0}^D,\\
 H_{j,\ell}&=C_j-q_\sigma^{-1}Q_\sigma^{-\ell}E_{kk},\\
 \mu_\ell&=\kappa(-1)^\ell q^{\ell(\ell+1)},\qquad
 (v_\ell)_a=r_\ell^{k-a}\quad(1\le a\le k).
 \end{split}                                                   \tag{2}
\]
Here \(T_k\) is adjacency on the channel path. The diagonal
crossing factor is \(\mu_\ell^p\), with its original phase.

For an arbitrary input \(h\in\mathbb C^N\), use the complete
two-color fields from the
[original word system](research_rational_word_local_source_system.md):
\[
 u_{\ell,\ell}=\mu_\ell^p v_\ell h_\ell,\qquad
 H_{j,\ell}u_{j,\ell}=d_j u_{j-1,\ell}\quad(\ell<j\le D),
 \qquad u_{j,\ell}=0\quad(j<\ell).
 \tag{3}
\]
Their last coordinates satisfy
\[
           e_k^Tu_{j,\ell}=(M^p)_{j\ell}h_\ell,\qquad
           (M^ph)_j=\sum_{\ell=0}^j e_k^Tu_{j,\ell}.
 \tag{4}
\]
In particular these fields retain the entire coefficient matrix
and all original repeated-root normals. Negative powers conjugate
the channel coefficients and crossing units, not the arbitrary
input \(h\).

Let \(U_j\) be the \(k\times N\) matrix with columns \(u_{j,\ell}\).
Separate its diagonal source from its strictly triangular part:
\[
 I_j=\mu_j^p v_jh_j e_j^T,\qquad V_j=U_j-I_j.
 \tag{5}
\]
The last \(e_j\) in (5) is the input-color coordinate, numbered
from zero; the channel coordinate \(e_k\) is numbered from one.
The columns supporting \(V_j\) and \(I_j\) are disjoint, and
\[
 \|I_j\|_F^2=k|h_j|^2,\qquad
 \|U_j\|_F^2=\|V_j\|_F^2+k|h_j|^2.
 \tag{6}
\]
The subscript \(F\) denotes the Frobenius norm on channel fields.

## 2. A forced Green formula with exact reset cancellation

For \(1\le j<N\), define a linear operator on \(k\times N\)
fields by
\[
 \mathscr B_j F=
       \frac{C_jF-q_\sigma^{-1}E_{kk}F\Lambda_\sigma}{d_j}.
 \tag{7}
\]
It acts separately on every input column, with its actual
physical boundary clock. The nullvector identity
\(H_{j,j}v_j=0\) gives
\[
 \boxed{\quad
 \mathscr B_jI_j=0,\qquad
 U_{j-1}=\mathscr B_jU_j,\qquad
 V_{j-1}=\mathscr B_jV_j-I_{j-1}.
 \quad}                                                        \tag{8}
\]
Thus the diagonal data have not been set to zero. They appear
as the prescribed forcing in the last equation of (8), and as
the nonzero matching constraints in (3).

For \(i<j\), use the original backward ordering
\[
 \mathscr G_{i,j}
        =\mathscr B_{i+1}\mathscr B_{i+2}\cdots\mathscr B_j,
       \qquad \mathscr G_{i,i}=I.
 \tag{9}
\]
The rightmost factor acts first.

**Theorem 1.** For every input \(h\) and \(0\le i<j<N\),
the inhomogeneous Green formula is exactly
\[
 \begin{split}
 V_i
 &=\mathscr G_{i,j}V_j
             -\sum_{t=i}^{j-1}\mathscr G_{i,t}I_t\\
 &=\mathscr G_{i,j}V_j-I_i.
 \end{split}                                                    \tag{10}
\]
In particular there is no accumulated bound on discarded
diagonal sources: their cancellation in (10) is an identity.

Put
\[
 L_N=\lceil N/4\rceil,\quad R_N=\lfloor3N/4\rfloor,\qquad
 \varrho_k=1-\frac1{64k^2}.
 \tag{11}
\]
For \(N\ge2048k^2\) and \(L_N-1\le i<j\le R_N\),
\[
 \boxed{\quad
 \|V_i\|_F^2+k|h_i|^2
       \le4\varrho_k^{\,2\lfloor(j-i)/2\rfloor}\|V_j\|_F^2.
 \quad}                                                        \tag{12}
\]
This estimate is uniform over all physical input columns, both
signs, and both parities of \(N\).

*Proof.* For \(\ell<j\), the middle identity in (8) is (3).
At \(\ell=j\) it is the exact nullvector identity; at
\(\ell>j\) both sides vanish. Subtract (5) to obtain the
last identity in (8), and iterate it to get the first line
of (10). If \(t>i\), the product \(\mathscr G_{i,t}\)
ends on the right with \(\mathscr B_t\), which annihilates
\(I_t\). Only \(t=i\) survives.

For each input column, (9) is the backward product in
[the all-column contraction](research_even_run_middle_color_contraction.md),
Theorem 3, with its boundary parameter of modulus one.
The indicated color range is exactly its closed middle interval,
with the order of the colors reversed. Therefore
\[
 \|\mathscr G_{i,j}\|_{F\to F}
       \le2\varrho_k^{\lfloor(j-i)/2\rfloor}.
 \tag{13}
\]
The same constant holds for the direct sum over all columns.
Equation (10) says \(U_i=\mathscr G_{i,j}V_j\).
The orthogonality in (6) proves (12). \(\square\)

The upper field \(V_j\) in (12) is the actual field selected
by all input constraints. The theorem does not bound that field
by a polynomial multiple of \(\|h\|\). In fact the same equations
force substantial amplification of those constraints.

## 3. Quantitative propagation of the prescribed input

Write \(\mathscr E_j(h)=\|U_j\|_F^2\) and
\(\beta_N=1+\pi/N\).

**Theorem 2.** Under the level assumption of Theorem 1, for
\(L_N+1\le j\le R_N\),
\[
 \boxed{\quad
 \mathscr E_j(h)\ge
       \varrho_k^{-2}\mathscr E_{j-2}(h)
       +k|h_j|^2+k\beta_N^{-2}|h_{j-1}|^2.
 \quad}                                                        \tag{14}
\]
Consequently, if \(A=L_N-1\), \(J=A+2T\le R_N\), then
\[
 \mathscr E_J(h)\ge
 \varrho_k^{-2T}\mathscr E_A(h)
 +k\sum_{\nu=1}^T\varrho_k^{-2(T-\nu)}
       \bigl(|h_{A+2\nu}|^2+\beta_N^{-2}|h_{A+2\nu-1}|^2\bigr).
 \tag{15}
\]
Every forcing weight in these inequalities comes from the
original diagonal coefficient \(\mu_\ell^p h_\ell\); no
input distribution or generic projection is substituted.

*Proof.* In \(U_j\), separate columns \(\ell\le j-2\),
\(\ell=j-1\), and \(\ell=j\). They are orthogonal in
Frobenius norm. On the first group the two-step backward
operator has norm at most \(\varrho_k\), without the
single-step prefactor two in (13). It produces exactly
\(U_{j-2}\). Hence the squared norm of that group is at
least \(\varrho_k^{-2}\mathscr E_{j-2}(h)\).
The last column has squared norm \(k|h_j|^2\).
For the remaining column,
\[
 \frac{H_{j,j-1}}{d_j}\,u_{j,j-1}
       =\mu_{j-1}^p v_{j-1}h_{j-1}.
 \tag{16}
\]
The one-step comparison in the contraction proof gives
\(\|H_{j,j-1}/d_j\|_2\le\beta_N\), while the right side
has norm \(\sqrt{k}|h_{j-1}|\). This proves (14).
Iteration at \(j=A+2,\ldots,A+2T\) gives (15).
\(\square\)

## 4. Which original output norm is controlled

Let \(X=\operatorname{diag}(Q^\ell)\) be the original Newton
clock. For a set of output colors \(\mathcal A\), define
\[
 \begin{split}
 \Gamma_p^{\mathcal A}(h)
   &=\sum_{\substack{j\in\mathcal A\\0\le\ell<N}}
                   |(M^p)_{j\ell}h_\ell|^2\\
   &=\frac1N\sum_{m=0}^{N-1}
                     \|P_{\mathcal A}M^pX^m h\|_2^2 .
 \end{split}                                                    \tag{17}
\]
The second equality is exact finite Fourier orthogonality,
not random-phase replacement. Thus this norm averages actual
full original outputs with specified input clocks. Write
\(\Gamma_p=\Gamma_p^{\{0,\ldots,D\}}\).

The local observation matrices used for
[the original coefficient theorem](research_even_run_backward_source_growth.md),
Section 5, extend to every input column. For any \(j\ge k-1\)
their rows are
\[
 e_k^TH_{j-h+1,\ell}\cdots H_{j,\ell},
                           \qquad 0\le h\le k-1.
 \tag{18}
\]
Their determinant is exactly one, including columns whose
diagonal color lies in the observation window. At that diagonal,
the nullvector identity supplies the zero observations below it.
All matrix row sums are at most four. The same cofactor proof gives
\[
 \mathscr E_j(h)\le K_k^2
          \Gamma_p^{\{j-k+1,\ldots,j\}}(h),\qquad
             K_k=k\,4^{k(k-1)/2+k-1}.                         \tag{19}
\]

**Corollary 3.** Define
\[
 \mathcal W_N=\{R_N-k+1,\ldots,R_N\},\qquad
 \mathcal Q_N=\{0,\ldots,L_N-2\}
                   \cup\{R_N-k+1,\ldots,D\}.
 \tag{20}
\]
For every arbitrary input and \(N\ge2048k^2\),
\[
 \boxed{\quad
 \Gamma_p^{\mathcal Q_N}(h)
 \le\Gamma_p(h)
 \le(1+512k^2K_k^2)\Gamma_p^{\mathcal Q_N}(h).
 \quad}                                                        \tag{21}
\]
Moreover, for \(J=A+2T\) as in (15), the actual output window
satisfies the forced lower bound
\[
 \begin{split}
 \Gamma_p^{\{J-k+1,\ldots,J\}}(h)
 &\ge K_k^{-2}\varrho_k^{-2T}\mathscr E_A(h)\\
 &\quad+\frac{k}{K_k^2}
       \sum_{\nu=1}^T\varrho_k^{-2(T-\nu)}
       \bigl(|h_{A+2\nu}|^2+\beta_N^{-2}|h_{A+2\nu-1}|^2\bigr).
 \end{split}                                                    \tag{22}
\]
In particular input at a fixed positive scaled distance from
the last middle color forces exponentially large amplification
in this clock-averaged output window, relative to that squared
input amplitude. No Gaussian endpoint selection is needed for (22).

*Proof.* Applying (13) to \(U_i\), then (19) at \(R_N\),
gives
\[
 \sum_\ell |(M^p)_{i\ell}h_\ell|^2
 \le4K_k^2\varrho_k^{\,2\lfloor(R_N-i)/2\rfloor}
                                     \Gamma_p^{\mathcal W_N}(h),
 \quad L_N-1\le i<R_N.
 \tag{23}
\]
The sum of its geometric factors is at most \(128k^2\).
All other rows belong to \(\mathcal Q_N\), proving (21).
Equations (15) and (19) prove (22). \(\square\)

There is also a rigorous coherent upper bound, with the cost of
the input-color sum displayed. For \(g=M^ph\), Cauchy--Schwarz
gives
\[
 \|P_{\mathcal A}g\|_2^2\le N\Gamma_p^{\mathcal A}(h),
 \qquad
 \|g\|_2^2\le
 N(1+512k^2K_k^2)\Gamma_p^{\mathcal Q_N}(h).
 \tag{24}
\]
Equation (23) supplies exponential suppression for a middle
subinterval in this upper bound. Neither (22) nor (24) changes
the clock average into a lower bound on its unaveraged term.

All identities remain valid with polynomial free-boundary inputs
\(h(z_1,\ldots,z_b)\). They preserve the original polynomial,
and every mixed normal derivative, before applying (17).
The estimates can be applied pointwise to each such derivative
or to any finite orthogonal direct sum of them. No uniform
boundary-domain estimate is asserted without a bound on the
corresponding input data.

## 5. The literal turn and the remaining coherent interface

The norm in (17) is diagonal in the input colors:
\[
 \Gamma_p(h)=\sum_{\ell=0}^D\omega_{p,N}(\ell)|h_\ell|^2,
 \qquad
 \omega_{p,N}(\ell)=\|M^pe_\ell\|_2^2.
 \tag{25}
\]
For the exact original turn \(Jh\), it transforms as
\[
 \Gamma_p(Jh)=
       \sum_{\ell=0}^D\omega_{p,N}(D-\ell)|h_\ell|^2,
       \qquad
 \sum_j\|I_j(Jh)\|_F^2=k\|h\|_2^2.
 \tag{26}
\]
Thus the diagonal injection norm is turn-invariant, whereas
the response norm for a subsequent run is reversed.
An output turn by itself has no norm cost: if
\(D-\mathcal A=\{D-j:j\in\mathcal A\}\), then exactly
\[
 \frac1N\sum_{m=0}^{N-1}
             \|P_{\mathcal A}J M^pX^mh\|_2^2
                 =\Gamma_p^{D-\mathcal A}(h),\qquad
                 JX^mJ=Q^{-m}X^{-m}.
 \tag{26a}
\]
Thus (21) also localizes the output with an appended literal
turn, with the two outer intervals reflected. The different
operation needed at an internal join is applying another run
to that turned output; its controlling norm is (26).
This is an exponential distinction,
not just a change in a fixed multiplicative constant:
\[
 \omega_{p,N}(D)=1,\qquad
 \omega_{p,N}(0)=\sum_j|(M^pe_0)_j|^2,\qquad
 \liminf_{N\to\infty}\frac1N\log\omega_{p,N}(0)>0.
 \tag{27}
\]
The first assertion follows from the original triangular
matrix and its unit diagonal; the last is the
[actual even-run growth theorem](research_even_run_backward_source_growth.md),
valid for both signs. For example \(h=e_D\) has
\(\Gamma_p(h)=1\) but \(\Gamma_p(Jh)=\omega_{p,N}(0)\).
Consequently no subexponential comparison
\(\Gamma_p(Jh)\le e^{o(N)}\Gamma_p(h)\) holds for all inputs.

One must also distinguish (21) from coherent output localization.
For any middle color \(m\notin\mathcal Q_N\), the legitimate
original input \(h=M^{-p}e_m\) gives \(M^ph=e_m\).
Its outer-quarter output vanishes identically. Thus no bound of
the form \(\|M^ph\|^2\le C_N\|P_{\mathcal Q_N}M^ph\|^2\),
with any finite \(C_N\), can hold for all inputs.
This counterexample does not assert failure for a fixed rational
word applied to its original cap.

For a joined word the next input is literally \(J M^{p_1}h\).
Equations (24)--(26) give a valid weighted upper estimate, but
they require the previous coherent output in the reversed weights
\(\omega_{p_2,N}(D-\ell)\). The current contraction theorem
does not control that weighted coherent quantity. A proof for
fixed joined short sources must supply this boundary pairing
estimate, or retain its cancellations in another exact cycle.
The Green formula above removes no physical input and no normal
current, but it does not by itself prove a full-word asymptotic.

## 6. Finite normalization checks

The [finite diagnostic](../experiments/check_even_run_forced_middle_green.py)
compares the full fields with original
matrix powers at both signs and both parities, tests the diagonal
nullvector and forced Green identities, and checks the exact
input-clock average and its transformation under the original turn.
At the proved level threshold it separately tests the finite-step
energy inequality with nonzero inputs at several middle colors.
These are normalization and index checks; the uniform bounds and
the exponentially inequivalent turn weights are proved above.

The [110-digit record](../repro/results/research-even-run-forced-middle-green.json)
passed 44 original-matrix cases with 4,724 full coefficient entries
and three arbitrary inputs per case, as well as eight short-channel
energy cases at \(N=2048k^2\) and \(N=2048k^2+1\).
The largest relative normalization residual was
\(2.083679361295542\cdot10^{-99}\). The large-level energy
checks use the exact local fields; they do not construct or
claim to test the full original matrices at those large levels.
