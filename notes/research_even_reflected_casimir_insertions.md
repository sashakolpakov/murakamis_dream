# Fixed Casimir insertions in an even reflected knot

Fix \(k\ge2\). The original reflected source is
\[
 \mathcal E_{k,N}
   =\phi_N(R^{-2k}T(R^{2k}))
   =\sum_{j=0}^{N-1}|\alpha_{N,j}|^2,
       \qquad \alpha_N=M^{2k}e_0 .
 \tag{1}
\]
Here \(R\) is the original positive crossing, \(M\) its
multiplication matrix in the normalized Newton basis, and
\(T\) the physical quarter-turn. The
[sharp growth theorem](research_even_run_sharp_reflected_growth.md)
retains the whole column \(\alpha_N\), including every
repeated-root normal.

We prove that inserting a fixed polynomial in the Casimir evaluates
that polynomial at the geometric critical value after division by
(1). The insertion stays in its stated original crossing box.
The conclusion also gives the characters of fixed colors on the
two filled cores, in their original disk framings. The polynomial
degree and the colors are fixed before \(N\) tends to infinity.

## 1. The exact Casimir and the inserted source

Put
\[
 \begin{gathered}
 D=N-1,\qquad q=e^{\pi i/N},\qquad
 c_j=2\cos((2j+1)\pi/N),\\
 \sigma_j=2\sin(\pi j/N),\qquad
 S_j=\prod_{\nu=1}^j\sigma_\nu,\qquad S_0=1,\\
 e_j(z)=S_j^{-2}\prod_{\nu=0}^{j-1}(c_\nu-z)
                  \quad(0\le j\le D).
 \end{gathered}
 \tag{2}
\]
These are coordinates in the full original quotient
\(\mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2)\).
Let \(\mathsf C_N\) denote multiplication by \(z\) in this
basis. The defining Newton product gives exactly
\[
 (\mathsf C_N v)_j=c_jv_j-\sigma_j^2v_{j-1},
       \qquad v_{-1}=0,\qquad
                         \|\mathsf C_N\|_2\le6 .
 \tag{3}
\]
At the final basis element the next Newton product is zero
in the quotient. Thus (3) holds at both ends as well.
The subdiagonal uses the elementary sine \(\sigma_j^2\),
not the factorial \(S_j^2\).
The norm bound follows by adding a diagonal matrix of norm
at most two and a weighted shift of norm at most four.

For a polynomial \(P\), put
\(P^\sharp(z)=\overline{P(\overline z)}\).
The exact Newton pairing is
\[
 \phi_N(f^\sharp T(g))
                =\langle \mathbf f,\mathbf g\rangle_{\ell^2},
 \tag{4}
\]
where \(\mathbf f,\mathbf g\) are the full Newton coefficient
columns. In particular \(R^\sharp=R^{-1}\).
These identities are proved in
[the original Newton Gram calculation](actual_newton_turn_positive_gram.md),
Sections 2--4, and in the
[Newton-calculus paper](../papers/newton-calculus/finite.tex).
Consequently, for fixed polynomials \(P,Q\),
\[
 \begin{split}
 \mathcal I_{P,Q,N}
   &:=\phi_N\!\left(P^\sharp(z)R^{-2k}
                              T(Q(z)R^{2k})\right)\\
   &=\left\langle P(\mathsf C_N)\alpha_N,
                            Q(\mathsf C_N)\alpha_N\right\rangle .
 \end{split}
 \tag{5}
\]
This specifies the actual placement of each insertion.
No multiplication has been moved through the turn.
Such a movement would replace its coefficient matrix by
the conjugate under index reversal, rather than leaving
the multiplication operator unchanged.

## 2. Concentration of the whole original column

Retain the spectral notation of the sharp growth theorem:
\[
 \begin{gathered}
 H(\theta)=2\cos\theta\,I-T_k-e^{-i\theta}E_{11}-E_{kk},
 \qquad \delta(\theta)=2-2\cos\theta,\\
 \lambda_*(0)=4\cos^2(\pi/(2k)),\qquad
                  x_k=\theta_k/(2\pi)\in(0,1/4).
 \end{gathered}
 \tag{6}
\]
The selected eigenvalue \(\lambda_*(\theta)\) is simple,
nonzero and strictly dominant on an interval containing
\([0,\theta_k]\) and extending a fixed distance beyond it.
Its modulus equals \(\delta\) exactly at \(\theta_k\).
Write \(E_k(x)\) for the all-mode upper envelope in that
theorem and
\[
                        B_*=E_k(x_k)>0.
 \]
The maximum of \(E_k\) on \([0,1/4]\) is unique.

**Lemma 1.** For every fixed \(\varepsilon>0\), there are
\(\gamma_\varepsilon>0\) and \(N_\varepsilon\) such that
\[
 \sum_{\left|(D-j)/N-x_k\right|\ge\varepsilon}
                         |\alpha_{N,j}|^2
       \le e^{-\gamma_\varepsilon N}\mathcal E_{k,N}
                     \quad(N\ge N_\varepsilon).
 \tag{7}
\]

**Proof.** It suffices to take
\(\varepsilon<\min(x_k,1/4-x_k)\).
On the upper quarter of original indices, the uniform
backward bound is
\[
 \log|\alpha_{N,D-h}|
                  \le NE_k(h/N)+o_k(N).
 \tag{8}
\]
The remainder is uniform in \(h\), including the fixed
enlargement of the quarter used below. Uniqueness of the
maximum gives a strict exponential gap in (8) outside
the stated window.

The middle interval requires a separate argument; comparison
of its total norm with the whole upper quarter would not
suffice. Use the actual coefficient estimate (31) of
[the backward-source theorem](research_even_run_backward_source_growth.md).
With
\[
 a_N=\lceil N/4\rceil-1,\quad b_N=\lfloor3N/4\rfloor,\quad
 j_N=D-a_N,\quad
 \mathcal W_N=\{j_N-k+1,\ldots,j_N\},
 \]
that estimate gives
\[
 \sum_{a_N<h\le b_N}|\alpha_{N,D-h}|^2
                     \le C_k\sum_{j\in\mathcal W_N}
                                      |\alpha_{N,j}|^2 .
 \tag{9}
\]
The constant \(C_k\) is independent of \(N\); it is the
sum of the geometric contraction series in that proof.
Every member of \(\mathcal W_N\) has \(h/N=1/4+O_k(N^{-1})\).
Since \(E_k(1/4)<B_*\), (8) makes the right side of (9)
exponentially smaller than \(e^{2NB_*}\).

The remaining lower quarter has squared norm \(O(N)\), by
[the original low-color bound](research_original_low_color_bound.md),
Theorem 1. These three ranges cover every original index.
Finally the actual, nonzero dominant-mode coefficient at an
index nearest \(Nx_k\) has
\[
                \log|\alpha_{N,D-h}|=NB_*+O_k(\log N).
 \tag{10}
\]
Dividing the three upper bounds by this single nonnegative
summand in (1) proves (7). \(\square\)

The local ratio also retains its complex phase.
It is stronger than the logarithmic estimate (10).

**Lemma 2.** Uniformly on any sufficiently small fixed compact
interval \(I\) containing \(x_k\),
\[
 \frac{\alpha_{N,j-1}}{\alpha_{N,j}}
       =\frac{\lambda_*(\theta)}{\delta(\theta)}
                         +O_{k,I}(N^{-1}),
 \qquad
       \theta=2\pi(D-j)/N,\quad (D-j)/N\in I .
 \tag{11}
\]
In particular the denominator is nonzero for large \(N\).
More directly, on that interval,
\[
 \frac{(\mathsf C_N\alpha_N)_j}{\alpha_{N,j}}
       =\mu_*(e^{-i\theta})+O_{k,I}(N^{-1}),
 \quad
 \mu_*(e^{-i\theta})=2\cos\theta-\lambda_*(\theta).
 \tag{12}
\]

**Proof.** Use the original channel vectors from the
backward-source theorem:
\[
 \alpha_{N,j}=\kappa^{2k}e_k^Tu_j,\qquad
 g_h=S_h^2u_{D-h},\qquad
 g_{h+1}=H_{N-h-1}g_h,
 \tag{13}
\]
where \(|\kappa|=1\) and
\(H_{N-h-1}=H(2\pi h/N)+O_k(N^{-1})\).
The proof of its Theorem 2 tracks the actual initial vector
in a smooth eigenframe. The complementary coordinate,
divided by the nonzero dominant coordinate, is
\(O_k(N^{-1})\) after \(O_k(\log N)\) steps.
The actual initial dominant coefficient is bounded away from
zero after its explicit \(N^{3/2}\) normalization.
Strict dominance, already proved through and beyond
\(\theta_k\), lets the same argument apply on \(I\).

If \(v_*(\theta)\) is a smooth right eigenvector, this says
\[
 \frac{g_h}{e_k^Tg_h}
    =\frac{v_*(\theta)}{e_k^Tv_*(\theta)}+O_k(N^{-1}).
 \tag{14}
\]
The last coordinate of the eigenvector is uniformly nonzero:
an eigenvector of this tridiagonal matrix cannot vanish at
its last coordinate, since all successive off-diagonals
are \(-1\). Compactness makes the lower bound uniform.
Equations (13)--(14) therefore give
\[
          \frac{e_k^Tg_{h+1}}{e_k^Tg_h}
                          =\lambda_*(\theta)+O_k(N^{-1}).
 \tag{15}
\]
The factor \(S_{h+1}^2/S_h^2=\sigma_{h+1}^2\) in (13)
proves (11). To obtain (12), observe the exact identity
\(\sigma_j^2=\sigma_{h+1}^2\) when \(j=D-h\).
Thus (3) gives
\[
 \frac{(\mathsf C_N\alpha_N)_j}{\alpha_{N,j}}
       =c_j-\frac{e_k^Tg_{h+1}}{e_k^Tg_h}.
 \tag{16}
\]
Since \(c_j=2\cos(\theta+\pi/N)\), (15) proves (12).
This derivation uses vector tracking, not a difference of
two \(O(\log N)\) coefficient estimates. \(\square\)

## 3. Polynomial insertion limits

Let \((\eta_k,\varphi_k)\) be the selected point from the
sharp growth theorem, and put
\[
        t_k=\varphi_k-i\eta_k,\qquad
        z_k=\mu_*(e^{-i\theta_k})=-2\cos t_k.
 \tag{17}
\]
The sign and conjugation in this equality matter. On the
conjugate classical clock \(e^{i\theta_k}\), the root is
\(e^{-\eta_k+i\varphi_k}\), giving
\(-2\cos(\varphi_k+i\eta_k)\). The actual positive-run
transfer (6) uses \(e^{-i\theta_k}\), so its value is the
complex conjugate displayed in (17).
The [geometric-point theorem](research_even_reflected_run_geometric_point.md)
identifies \(t_k\) with the original positive-power core angle.

**Theorem 3.** The normalized original column is an approximate
eigenvector of its actual Casimir:
\[
       \frac{\|(\mathsf C_N-z_k)\alpha_N\|_2}
                         {\|\alpha_N\|_2}\longrightarrow0 .
 \tag{18}
\]
For every pair of fixed polynomials \(P,Q\in\mathbb C[z]\),
\[
 \boxed{\quad
  \frac{\phi_N(P^\sharp R^{-2k}T(QR^{2k}))}
                         {\mathcal E_{k,N}}
           \longrightarrow\overline{P(z_k)}\,Q(z_k).
 \quad}
 \tag{19}
\]
In particular
\[
       \frac{\phi_N(R^{-2k}T(PR^{2k}))}{\mathcal E_{k,N}}
                            \longrightarrow P(z_k).
 \tag{20}
\]
All limits are through the full sequence of integer levels.

**Proof.** Fix a sufficiently small \(\varepsilon>0\).
On the index window \(|(D-j)/N-x_k|<\varepsilon\),
(12) and smoothness of \(\mu_*\) give
\[
 |((\mathsf C_N-z_k)\alpha_N)_j|
               \le (C_k\varepsilon+C_k/N)|\alpha_{N,j}|.
 \tag{21}
\]
Outside that window, the bidiagonal operator only sees
indices outside the window of radius \(\varepsilon/2\),
once \(N\) is large. Hence its contribution to the norm
is at most
\[
 (6+|z_k|)
   \left(\sum_{|(D-j)/N-x_k|\ge\varepsilon/2}
                          |\alpha_{N,j}|^2\right)^{1/2}.
 \tag{22}
\]
Lemma 1 makes (22) exponentially small relative to
\(\|\alpha_N\|_2\).
Take \(N\to\infty\) in (21), then let \(\varepsilon\to0\).
This proves (18).

For a fixed polynomial,
\[
         P(\mathsf C_N)-P(z_k)I
             =Q_P(\mathsf C_N)(\mathsf C_N-z_kI)
 \]
with another fixed polynomial \(Q_P\).
The bound \(\|\mathsf C_N\|_2\le6\) makes
\(\|Q_P(\mathsf C_N)\|_2\) uniformly bounded.
Thus
\[
 \|P(\mathsf C_N)\alpha_N-P(z_k)\alpha_N\|_2
                         =o(\|\alpha_N\|_2).
 \tag{23}
\]
Apply this to both vectors in the exact pairing (5);
Cauchy--Schwarz proves (19), and \(P=1\) there gives
(20). \(\square\)

Although the spectrum of each \(\mathsf C_N\) consists of real
physical nodes, the limiting value \(z_k\) is not real.
There is no self-adjoint spectral argument here:
\(\mathsf C_N\) is nonnormal in the specified Newton norm.
The conclusion concerns the particular original vector
selected by the crossing power, proved by (7) and (14).

## 4. Fixed colors on the two original filling cores

The original colored-circle identity is
\[
 L_m(z)=(-1)^{m-1}U_{m-1}(z/2),
                         \qquad m\ge1,
 \tag{24}
\]
where \(U_{m-1}\) is the Chebyshev polynomial of the second
kind. It includes the original auxiliary pivot, cup and cap.
For each fixed \(m\), it holds at every sufficiently large
level in the full quotient, with all normal derivatives.
See the circle identity in
[the Newton-calculus paper](../papers/newton-calculus/finite.tex).

In (20), insert this literal colored circle in the original
disk framing of the positive crossing box. Then
\[
       L_m(z_k)
        =U_{m-1}(\cos t_k)
        =\frac{\sin(mt_k)}{\sin t_k}.
 \tag{25}
\]
This is the character of the selected determinant-one core
holonomy with eigenvalues \(e^{it_k},e^{-it_k}\).
The original disk longitude has logarithmic period \(2it_k\).
Under filling along \(\mu+p\lambda\), the complementary
primitive curve \(\lambda\) is the core longitude.
The inserted loop is a longitude-parallel copy of the
surgery circle; its parallel annulus carries the specified
ribbon framing to the core.
Retaining the disk framing identifies the inserted
encircling circle with that filled core: the disk twist
restores \(R^{2k}\) and carries its longitude and ribbon
with it. No framing change is suppressed in (24).

For fixed colors \(m,n\), (19) therefore gives the two-core
formula
\[
 \frac{\phi_N(L_mR^{-2k}T(L_nR^{2k}))}
                          {\mathcal E_{k,N}}
   \longrightarrow
       \overline{\frac{\sin(mt_k)}{\sin t_k}}\,
                       \frac{\sin(nt_k)}{\sin t_k}.
 \tag{26}
\]
The negative-power core angle is
\(-\overline{t_k}\), so the conjugated factor is its own
selected holonomy character.
All factors in (25)--(26) are nonzero, since
\(\Im t_k<0\). These fixed-color insertions consequently
have the same exponential rate as the original reflected
source. The main component still has the single original
reduced cut; the fixed-color circles use their stated
ordinary pivotal traces.
In particular, by the
[reflected-knot volume theorem](research_reflected_even_kashaev_volume_theorem.md),
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
     \log\left|\phi_N(L_mR^{-2k}T(L_nR^{2k}))\right|
             =\operatorname{Vol}(S^3\setminus K_k),
 \quad K_k=C(R^{-2k}T(R^{2k})).
 \tag{27}
\]
The volume is that of the filled knot complement carrying
these fixed-color core observables.

The result is limited to fixed polynomials and fixed colors
at the stated two boxes. It gives neither estimates uniform
in a color growing with \(N\), nor a holomorphic free-boundary
packet, nor survival after an arbitrary further signed turn.
For a general polynomial with \(P(z_k)=0\), (20) gives a
zero normalized limit and makes no assertion about the
smaller exponential rate.

## 5. Reproducing the finite placement checks

Run the
[focused checker](../experiments/check_even_reflected_casimir_insertions.py)
with

    .venv/bin/python experiments/check_even_reflected_casimir_insertions.py \
      --precision 100 \
      --output repro/results/research-even-reflected-casimir-insertions.json

It constructs the literal original crossing matrix and applies its
powers by matrix-vector multiplication. The negative powers in the
original closing word are computed by triangular solves, independently
of the Gram identity. The
[saved record](../repro/results/research-even-reflected-casimir-insertions.json)
contains 64 inserted-trace comparisons at eight levels, including both
parities, for \(k=2,3\). It also checks Casimir commutation and reversal.
The maximum relative identity error at 100 decimal digits is less
than \(2.8\cdot10^{-75}\).
The [separate 140-digit replay](../repro/results/research-even-reflected-casimir-insertions-root.json)
checks the same 64 identities, with maximum relative error
less than \(3.4\cdot10^{-115}\).

The same record gives the normalized Casimir residual and the
fixed-moment differences at each level. Those entries are diagnostics;
the finite list proves neither a convergence rate nor monotonicity.
The concentration, vector tracking and fixed-polynomial limit are
proved above. The output includes the script hash and package versions,
and an independent replay may use a different output path.
