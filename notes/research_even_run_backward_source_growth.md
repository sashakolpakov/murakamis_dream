# Actual backward modes and positive growth for every fixed even run

Research note, 3 November 2026.

For every fixed even crossing power, the original source has a
nonzero projection onto the largest backward endpoint mode, at
all sufficiently large levels and both parities. This follows
from its full fixed-rank Gaussian boundary data and an exact
Jacobi observability matrix. It gives a nonzero coefficient
profile on a fixed backward interval and a strictly positive
exponential lower bound for the reflected closed source.
A spectral-radius envelope also bounds every original color.
The middle-color contraction further localizes the reflected norm,
up to a fixed multiplicative constant, to the two outer color
quarters. Forward and backward envelopes can then be combined on
those intervals. The lower and upper rates are not asserted to
coincide globally.

No interior mode-switch theorem or geometric volume identity
is inferred from these results.

## 1. Exact source and backward regularization

Fix \(k\ge2\), \(p=2k\), and \(N\ge2\). Set
\[
 D=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \kappa=\exp\!\left(\frac{\pi iD^2}{2N}\right),\quad
 S_h=\prod_{\nu=1}^h2\sin(\pi\nu/N),\quad S_0=1.
 \tag{1}
\]
Let \(\alpha_j=(M^{2k}\mathbf e_0)_j\) be the entire original
Newton coefficient column. The
[resonant source construction](research_resonant_crossing_run_source.md)
gives \(k\)-channel vectors \(u_j\), with prescribed
\[
 (u_0)_a=q^{k-a},\qquad
 \alpha_j=\kappa^{2k}\mathbf e_k^Tu_j,\qquad
 H_ju_j=d_ju_{j-1}\quad(1\le j\le D),
 \tag{2}
\]
where
\[
 \begin{split}
 H_j&=C_k(qQ^j)-q^{-1}E_{kk},\\
 C_k(r)&=(r+r^{-1})I_k-T_k-rE_{11},\\
 d_j&=4\sin^2(\pi j/N).
 \end{split}                                                    \tag{3}
\]
Here \(T_k\) is path adjacency. These are the original
pole-canceled source equations, with all Newton indices and
Casimir normals retained.

Define
\[
             g_h=S_h^2u_{D-h}\quad(0\le h\le D).
 \tag{4}
\]
Since \(d_{N-h}=4\sin^2(\pi h/N)\), (2) gives exactly
\[
                g_0=u_D,\qquad g_h=H_{N-h}g_{h-1}.
 \tag{5}
\]
No forcing or endpoint term is omitted in (5); the full
original endpoint is \(g_0\).

The classical backward matrix is
\[
 H(\theta)=2\cos\theta\,I_k-T_k-e^{-i\theta}E_{11}-E_{kk},
 \qquad
 L_k=H(0)=2I_k-T_k-E_{11}-E_{kk}.
 \tag{6}
\]
Uniformly for \(1\le h<N\), the exact matrix \(H_{N-h}\)
differs from \(H(2\pi h/N)\) by \(O_k(N^{-1})\).
Both families are uniformly smooth in the scaled color.

## 2. The original endpoint resolves every nonzero path mode

The eigenvalues of the real Neumann path Laplacian \(L_k\) are
\[
 \lambda_j=4\sin^2\!\left(\frac{\pi j}{2k}\right),
                      \qquad 0\le j\le k-1.
 \tag{7}
\]
Choose real orthonormal eigenvectors \(v_j\), with
\[
 (v_0)_a=k^{-1/2},\qquad
 (v_j)_a=\sqrt{2/k}\,
       \cos\!\left(\frac{\pi j(a-\tfrac12)}{k}\right)
                  \quad(1\le j\le k-1).
 \tag{8}
\]
Every last coordinate \(\mathbf e_k^Tv_j\) is nonzero.

Retain the exact normalization from the
[full Gaussian endpoint theorem](actual_twist_endpoint_gaussian_certificate.md):
\[
 C_{N,2k}=(-1)^N
       e^{-i\pi(2k)/(4N)}
       \left(-\frac{i\sqrt{2k}}2\right)e^{i\pi/4},
                  \qquad |C_{N,2k}|=\sqrt{k/2}.
 \tag{9}
\]
For \(1\le j\le k-1\), set
\[
 w_j(N)=2(-1)^j(1-j/k)\sin(\pi j/k)
                            e^{-i\pi Nj^2/(2k)}.
 \tag{10}
\]
Its modulus is strictly positive and independent of \(N\).

**Theorem 1.** The full original backward endpoint satisfies
\[
 \boxed{\quad
 \frac{u_D}{C_{N,2k}N^{3/2}}
    =\sum_{j=1}^{k-1}
         \frac{w_j(N)}{\mathbf e_k^Tv_j}\,v_j
                                  +O_k(N^{-1/2}).
 \quad}                                                        \tag{11}
\]
The zero mode \(v_0\) has leading coefficient zero. Every
nonzero mode, including the unique largest one \(v_{k-1}\),
has a leading coefficient bounded away from zero at all
levels. In particular
\[
 \lim_{N\to\infty}\frac{\|u_D\|_2^2}{N^3}
       =4\sum_{r=1}^{k-1}r^2
                          \cos^2\!\left(\frac{\pi r}{2k}\right)>0.
 \tag{12}
\]

*Proof.* Write \(e_h\) for the original normalized Newton
basis element. The full Frobenius pairing gives
\[
       \alpha_{D-h}=\phi_N(R^{2k}e_h),\qquad
       \mathbf e_k^Tg_h
              =S_h^2\phi_N((R/\kappa)^{2k}e_h).
 \tag{13}
\]
For each fixed \(0\le h\le k-1\), the fixed-insertion
Gaussian theorem and its paired-mode formula in
[the endpoint vector calculation](actual_newton_run_endpoint_vectors.md),
equations (6) and (9)--(12), give
\[
 \frac{S_h^2\phi_N((R/\kappa)^{2k}e_h)}
                    {C_{N,2k}N^{3/2}}
       =\sum_{j=1}^{k-1}\lambda_j^h w_j(N)+O_k(N^{-1/2}).
 \tag{14}
\]
Indeed \(S_h^2=(2\pi/N)^{2h}(h!)^2[1+O_h(N^{-2})]\);
its factor \(4^h\) converts the Gaussian moments
\(\sin^{2h}(\pi j/(2k))\) into \(\lambda_j^h\).
The fixed vector of errors in (14) is uniform over the
indicated \(h\)'s and all level residue classes.

First control \(u_D\) without replacing its matrices by limits.
For \(N\ge k\), let \(\mathcal O_N\) have rows
\[
 (\mathcal O_N)_{h,\cdot}
      =\mathbf e_k^TH_{N-h}\cdots H_{N-1}
                     \quad(0\le h\le k-1),
 \tag{15}
\]
where the row for \(h=0\) is \(\mathbf e_k^T\).
In row \(h\) its leftmost nonzero entry is in column \(k-h\),
with value \((-1)^h\), because every factor has off-diagonal
entries \(-1\). Reversing its columns makes it triangular.
The two determinant signs cancel, giving
\(\det\mathcal O_N=1\) exactly. Its entries are uniformly
bounded for fixed \(k\), so its cofactor inverse is uniformly
bounded as well. It converges to the likewise invertible
\(\mathcal O_0\), whose rows are \(\mathbf e_k^TL_k^h\).

Equations (5), (13), and (14) are the exact system
\(\mathcal O_Nu_D=\) its known endpoint moment vector.
They prove \(\|u_D\|=O_k(N^{3/2})\) before any error of the
form \(O(N^{-1})\|u_D\|\) is used. Now
\(\mathcal O_N=\mathcal O_0+O_k(N^{-1})\) permits replacement
by the limiting observation matrix in the normalized system.
In its eigenbasis, (14) reads
\[
 \sum_{j=0}^{k-1}\lambda_j^h
       (\mathbf e_k^Tv_j)\,
       v_j^T\frac{u_D}{C_{N,2k}N^{3/2}}
    =\sum_{j=1}^{k-1}\lambda_j^h w_j(N)
                                  +O_k(N^{-1/2}).
 \tag{16}
\]
The \(k\) distinct eigenvalues have an invertible fixed
Vandermonde matrix. Solving (16) proves (11), including
the missing zero-mode coefficient.

Finally orthonormality removes all interference between the
resolved endpoint modes when taking the vector norm. Since
\[
 \frac{|w_j(N)|^2}{|\mathbf e_k^Tv_j|^2}
     =8k(1-j/k)^2\sin^2\!\left(\frac{\pi j}{2k}\right),
 \tag{17}
\]
equations (9) and (11) give (12). \(\square\)

## 3. A nonzero backward coefficient profile

Let \(\lambda_*(\theta)\) be the analytic eigenvalue of
\(H(\theta)\) through
\(\lambda_*(0)=\lambda_{k-1}>0\).
There is a constant \(\theta_k^0>0\), depending only on
the fixed \(k\), such that on \(0\le\theta\le\theta_k^0\):
all eigenvalues admit a smooth bounded eigenframe,
\(\lambda_*\ne0\) is strictly largest in modulus with a
uniform relative gap, and its right eigenvector has nonzero
last coordinate. These assertions follow by perturbation
of the simple real spectrum (7), after reducing
\(\theta_k^0\) if necessary. They assert a small fixed
interval, not continuation across a modulus switch.

Define
\[
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad
 B_k(x)=\int_0^x\log|\lambda_*(2\pi t)|\,dt-2J(x).
 \tag{18}
\]

**Theorem 2.** On every compact interval
\(I\subset(0,\theta_k^0/(2\pi))\), uniformly for \(h/N\in I\),
\[
 \boxed{\quad
       \log|\alpha_{D-h}|=N B_k(h/N)+O_{k,I}(\log N).
 \quad}                                                        \tag{19}
\]
In particular these actual original coefficients are nonzero
for all sufficiently large \(N\). The conclusion holds
through all integers \(N\), without a parity or coprimality
subsequence.

*Proof.* Diagonalize \(H(\theta)\) smoothly on the chosen
small interval, using the real orthonormal frame at zero.
In this moving frame the exact transfer in (5) is
the classical diagonal transfer plus \(O_k(N^{-1})\),
uniformly in the scaled index. The change of frame between
successive indices also costs \(O_k(N^{-1})\).
After division by the nonzero dominant eigenvalue, it has
block form
\[
             \begin{pmatrix}1&0\\0&\Lambda_h\end{pmatrix}
                         +O_k(N^{-1}),\qquad
             \|\Lambda_h\|\le r_k<1.
 \tag{20}
\]
Theorem 1 gives a dominant initial coordinate of modulus
at least \(c_kN^{3/2}\), while all complementary coordinates
are \(O_k(N^{3/2})\). This is the actual initial vector,
not a selected free solution.

For clarity, the usual contraction estimate can be applied
without assuming the complement is initially small.
Write \(a_h,b_h\) for the dominant and complementary
coordinates after division by the cumulative dominant
eigenvalues. If \(\|b_{h-1}\|/|a_{h-1}|\le R\), then
\[
 \frac{\|b_h\|}{|a_h|}
 \le
 \frac{r_k\|b_{h-1}\|/|a_{h-1}|
              +(C_k/N)(1+\|b_{h-1}\|/|a_{h-1}|)}
      {1-(C_k/N)(1+\|b_{h-1}\|/|a_{h-1}|)} .
 \tag{21}
\]
Choose \(R\) above the uniformly bounded initial ratio.
For large \(N\), this preserves that bound and improves it
to \(O_k(N^{-1})\) after \(O_k(\log N)\) steps.
Throughout, the dominant coordinate is multiplied by
\(1+O_k(N^{-1})\), hence stays nonzero and changes in
modulus by bounded factors over \(O(N)\) steps.
The last-coordinate observation of its eigenvector is
uniformly nonzero. After the initial logarithmic number
of steps the complementary observation is \(O(N^{-1})\)
relative to it and cannot cancel it.
Consequently, uniformly on \(I\),
\[
 \log|\mathbf e_k^Tg_h|
       =\frac32\log N+
          \sum_{\nu=1}^h\log|\lambda_*(2\pi\nu/N)|+O_{k,I}(1).
 \tag{22}
\]
The smooth Riemann sum has \(O_k(1)\) error. The uniform
sine-factorial estimate gives
\(\log S_h^2=2NJ(h/N)+O(\log N)\), including the original
factorial normalization. Equation (4), (2), and
\(|\kappa|=1\) now prove (19). \(\square\)

## 4. Positive exponential growth and an all-color upper bound

The literal reflected closing source is
\[
 \mathcal E_{k,N}
      =\phi_N(R^{-2k}T(R^{2k}))
      =\sum_{j=0}^{D}|\alpha_j|^2.
 \tag{23}
\]
Its positivity is the established original Gram identity;
the new information here is an exponential growth estimate
for the coherent original column inside that norm.

**Corollary 3.** For every fixed \(k\ge2\), there is an
explicitly specified constant \(c_k>0\) such that
\[
          \liminf_{N\to\infty}N^{-1}\log\mathcal E_{k,N}
                             \ge c_k>0.
 \tag{24}
\]
More precisely, the lower bound is \(2B_k(x)\) for every
\(0<x<\theta_k^0/(2\pi)\).

*Proof.* Choose \(\theta_k^0\) additionally so that
\(|\lambda_*(\theta)|\ge\lambda_{k-1}/2\), and set
\[
 x_k=\min\left\{\frac{\theta_k^0}{4\pi},
                \frac{\sqrt{\lambda_{k-1}/2}}{4\pi}\right\}>0.
 \tag{25}
\]
Using \(2\sin\pi t\le2\pi t\) gives
\[
 B_k(x_k)\ge x_k\!
       \left[\log(\lambda_{k-1}/2)
                     -2\log(2\pi x_k)+2\right]
                  \ge x_k(\log4+2)>0.
 \tag{26}
\]
A rounded color in (19) contributes one nonnegative
summand to (23), proving (24) with
\(c_k=2x_k(\log4+2)\). \(\square\)

There is also an unconditional upper envelope over the
entire original color range. Put
\[
 \rho_k(\theta)=\rho(H(\theta)),\qquad
 E_k(x)=\int_0^x\log\rho_k(2\pi t)\,dt-2J(x).
 \tag{27}
\]
The spectral radius is bounded away from zero on
\([0,2\pi]\): away from its endpoints,
\(\det H(\theta)=e^{ik\theta}(1-e^{-i\theta})\ne0\);
at the endpoints \(L_k\) has a positive eigenvalue.
Thus \(E_k\) is continuous on \([0,1]\).
The fixed-rank spectral-radius product estimate proved in
[the folded source calculation](actual_newton_rank_three_folded_packet.md),
Section 2, applies to (5), using the polynomial initial
bound from Theorem 1. It yields uniformly for \(0\le h<N\)
\[
 \log|\alpha_{D-h}|
        \le N E_k(h/N)+o_k(N),\qquad
 \limsup_{N\to\infty}N^{-1}\log\mathcal E_{k,N}
                \le2\max_{0\le x\le1}E_k(x).
 \tag{28}
\]
Zeros of a coefficient are interpreted as \(-\infty\)
on the left. The estimate allows all eigenvalue collisions
and modulus switches; it uses the full spectral radius,
not continued dominance of \(\lambda_*\).

For recall, the product estimate freezes blocks of
\(L=\lfloor N^{1/(2k)}\rfloor\) steps. The powers of a
bounded \(k\)-dimensional matrix of spectral radius at
most one have uniform bound \(C_k(\nu+1)^{k-1}\), by
confluent divided differences. The smooth step errors
then cost only \(O(N\log L/L+L^k)=o(N)\) in the logarithm.
This remains uniform for partial final blocks. Uniform
sine-factorial errors and the \(N\) nonnegative summands
give (28).

For \(k=1\), the exact source is
\(|\alpha_j|=S_j\), and the known factorial maximum already
gives a positive sharp norm exponent; no zero-gap endpoint
argument is needed. Negative even runs are entrywise
conjugates and have the same estimates. The reflected
closures in (23) are knots by the original endpoint
pairing test, but no identification of (24) or (28)
with their hyperbolic volume is asserted.

The results retain the complete original source column.
They do not turn its open-boundary evaluations into positive
sums: a whole-boundary packet, a sharp global norm rate, and
survival through any later mode switch are separate questions.

## 5. Coefficient localization and a two-ended upper envelope

The [middle-color contraction](research_even_run_middle_color_contraction.md),
Theorem 3, controls the entire backward channel vector. To use it
for the original reflected source one must also bound that vector
by actual coefficient observations. This can be done without
choosing a phase or excluding cancellations in a coefficient.

Put
\[
 r_k=1-\frac1{64k^2},\qquad
 K_k=k\,4^{k(k-1)/2+k-1}.                                    \tag{29}
\]
For \(N\ge2048k^2\), define
\[
 \begin{split}
 a_N&=\lceil N/4\rceil-1,\qquad b_N=\lfloor3N/4\rfloor,\\
 j_N&=D-a_N=N-\lceil N/4\rceil,\\
 \mathcal W_N&=\{j_N-k+1,\ldots,j_N\},\\
 \mathcal Q_N&=\{0,\ldots,D-b_N-1\}
                   \ \cup\ \{j_N-k+1,\ldots,D\}.
 \end{split}                                                  \tag{30}
\]
The set \(\mathcal Q_N\) consists of the two outer color
quarters, with a fixed \(k\)-dependent enlargement of one endpoint.
Write
\(\mathcal E_N(\mathcal A)=\sum_{j\in\mathcal A}|\alpha_j|^2\).

**Theorem 4.** Every original middle coefficient satisfies
\[
 |\alpha_{D-l}|
 \le2K_k r_k^{\lfloor(l-a_N)/2\rfloor}
                         \mathcal E_N(\mathcal W_N)^{1/2},
              \qquad a_N<l\le b_N.                           \tag{31}
\]
In particular the complete reflected source obeys
\[
 \boxed{\quad
 \mathcal E_N(\mathcal Q_N)
 \le\mathcal E_{k,N}
 \le(1+512k^2K_k^2)\mathcal E_N(\mathcal Q_N).
 \quad}                                                       \tag{32}
\]
These are bounds for the actual original coefficients at every
sufficiently large level, with no restriction on its parity.

*Proof.* For any \(j\ge k-1\), form the \(k\)-row observation
matrix
\[
 (\mathcal O_{N,j})_{h,\cdot}
      =\mathbf e_k^TH_{j-h+1}\cdots H_j,\qquad
                         0\le h\le k-1.                     \tag{33}
\]
The empty product is the row \(\mathbf e_k^T\).
As in (15), the leftmost entry of row \(h\) is
\((-1)^h\) in column \(k-h\). Thus
\(\det\mathcal O_{N,j}=1\) exactly, at every color.
The matrices \(H_j\) are symmetric and have maximum absolute
row sum at most four. Hence the Euclidean norm of row \(h\)
in (33) is at most \(4^h\). Hadamard's inequality for
every cofactor gives
\[
 \|\mathcal O_{N,j}^{-1}\|_2
                          \le k\,4^{k(k-1)/2}.                \tag{34}
\]
The original source equations give the exact observation vector
\[
 (\mathcal O_{N,j}u_j)_h
    =\kappa^{-2k}
        \left(\prod_{\nu=0}^{h-1}d_{j-\nu}\right)\alpha_{j-h}.
                                                                    \tag{35}
\]
Since \(0<d_i\le4\), (34)--(35) prove
\[
 \|u_j\|_2
       \le K_k\left(\sum_{h=0}^{k-1}|\alpha_{j-h}|^2\right)^{1/2}.
                                                                    \tag{36}
\]
This is a uniform bound on the full vector by a fixed window of
original scalar observations, not the converse inequality alone.

Apply (36) at \(j=j_N\), followed by the two-step contraction
to \(y_l=u_{D-l}\) starting at \(l=a_N\).
Every step lies in its closed middle interval. The last-coordinate
observation in (2) now proves (31). Finally,
\[
 \sum_{t=1}^{\infty}r_k^{2\lfloor t/2\rfloor}
       =\frac{1+r_k^2}{1-r_k^2}
       \le\frac2{1-r_k}=128k^2.                              \tag{37}
\]
All colors outside the contracted interval already belong
to \(\mathcal Q_N\). Its overlap with \(\mathcal W_N\)
only overcounts nonnegative terms. Squaring (31), summing,
and using \(\mathcal W_N\subset\mathcal Q_N\) gives (32).
The lower bound is immediate. \(\square\)

More quantitatively, for \(0<\varepsilon<1/2\) the part of
the middle interval at backward distance at least
\(\lceil\varepsilon N\rceil\) from its beginning satisfies
\[
 \sum_{\substack{a_N+\lceil\varepsilon N\rceil\le l\le b_N}}
             |\alpha_{D-l}|^2
 \le
 \frac{8K_k^2}{1-r_k^2}\,
 r_k^{2\lfloor\lceil\varepsilon N\rceil/2\rfloor}
                    \mathcal E_N(\mathcal W_N).              \tag{38}
\]
Thus this interior portion is exponentially smaller than a
fixed observation window at the first middle color. This
conclusion is about the original reflected norm; it does not
require a separate lower bound on any particular middle entry.

One can also improve the upper envelope near the other end by
using the exact forward equation. Define the polynomial matrix
\[
 B_k(X)=\mathcal B_k(X;1)
       =(1-X)[C_k(X)-E_{kk}]^{-1},                            \tag{39}
\]
with its polynomial extension from
[the full-color transfer](research_two_run_source_transfer.md),
equation (4), and put
\[
 F_k(y)=J(y)+\int_0^y
                \log\rho\!\left(B_k(e^{2\pi it})\right)\,dt,
                         \qquad 0\le y\le1.                 \tag{40}
\]
The notation \(F_k\) here denotes an envelope, not a sine
factorial or a boundary polynomial. The matrix in (39) has
determinant \(X^k(1-X)^{k-1}\), so it is invertible on the
unit circle except at one. At one it is the all-ones matrix,
of spectral radius \(k\). Its spectral radius is therefore
continuous and bounded away from zero on the entire circle.

**Corollary 5.** Uniformly for all original colors,
\[
 \log|\alpha_j|
 \le N\min\{F_k(j/N),E_k(1-j/N)\}+o_k(N).                    \tag{41}
\]
Consequently
\[
 \boxed{\quad
 \limsup_{N\to\infty}\frac1N\log\mathcal E_{k,N}
 \le
 2\max_{y\in[0,1/4]\cup[3/4,1]}
                \min\{F_k(y),E_k(1-y)\}.
 \quad}                                                       \tag{42}
\]
This is no larger than the preceding whole-color bound (28).
No assertion that the global maxima are strictly different is
needed.

*Proof.* The exact forward transfer in the cited source theorem is
\[
 u_j=(1-Q^{-j})\mathcal B_k(qQ^j;q)u_{j-1}.                  \tag{43}
\]
Divide \(u_j\) by the nonzero scalar
\(\prod_{\nu=1}^j(1-Q^{-\nu})\), of modulus \(S_j\).
The resulting vector has bounded initial data and successive
matrices \(\mathcal B_k(qQ^j;q)\), uniformly within
\(O_k(N^{-1})\) of the smooth family \(B_k(e^{2\pi ij/N})\).
The same fixed-rank spectral-radius estimate used for (28)
now applies without a zero-radius endpoint. Multiplying back
the scalar and using the uniform factorial estimate gives
\[
                  \log|\alpha_j|\le NF_k(j/N)+o_k(N).
\]
The backward estimate (28), with \(h=D-j\), gives the other
term in (41). Uniform continuity of \(E_k\) absorbs the
shift \(1/N\) between \(h/N\) and \(1-j/N\).
Equation (32) reduces the full nonnegative sum to
\(\mathcal Q_N\); these sets converge to the two closed
outer quarters. Continuity of both envelopes and the
subexponential number of terms prove (42). \(\square\)

The forward estimate is strictly sharper than the backward
one on some fixed neighborhood of \(y=0\). Indeed
\(F_k(0)=0\), whereas \(E_k(1)>0\) for \(k\ge2\):
\[
 \log\rho_k(\theta)\ge\frac1k\log|\det H(\theta)|,\qquad
 \int_0^1\log|\det H(2\pi t)|\,dt=0.
 \tag{44}
\]
The inequality is strict on an interval near zero because
one eigenvalue tends to zero and another tends to
\(\lambda_{k-1}>0\). Both sides are integrable, and
\(J(1)=0\), proving the claim. This supplies a genuine
improvement of one endpoint envelope. Equations (32) and
(42) still leave the comparison of the two surviving end
maxima and their geometric identification open.

## 6. Finite normalization diagnostic

The [original-matrix diagnostic](../experiments/check_even_run_backward_source_growth.py)
checks the exact backward equations at every color in twelve
level/power cases, the fixed endpoint moment system, its determinant
one, and the limiting eigenbasis and normalization constants.
The [110-digit record](../repro/results/research-even-run-backward-source-growth.json)
passed 294 color checks and 36 fixed endpoint moments, with largest
relative residual \(8.28297658815\cdot10^{-103}\).
Finite Gaussian-mode errors are recorded separately; they are
not used to prove convergence or dominant-mode survival.
