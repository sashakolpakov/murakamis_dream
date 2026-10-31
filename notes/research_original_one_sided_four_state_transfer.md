# Exact original before, active and after transfer

31 October 2026. An exact source identity: no asymptotic branch is selected and no unused row is deleted.

Put \(N\ge3\), \(d=N-1\), \(m=\lfloor N/2\rfloor\), \(M=m-1\), and
\(\sigma=-2\cos(2\pi\delta)\). Define
\[
 c_r=2\cos\frac{(2r+1)\pi}{N},\qquad
 \alpha_r=c_r-\sigma,\qquad s_r=2\sin\frac{\pi r}{N},
 \quad A=x+y,\quad P=xy,
\]
\[
 \beta_r=s_r^2,\qquad
 \gamma_r=s_rs_{r-1}\alpha_{r-1},\qquad
 A_{\mathrm{rest}}^\alpha=\prod_{r=m}^{d}\alpha_r.
\]
At \(r=0,1\), set \(\gamma_r=0\); these are the original absent
negative-row term and the factor \(s_0=0\). All products retain level \(N\).

## 1. The exact original polynomial

The [original one-sided coefficient expansion](actual_one_sided_relative_spectral_energy.md)
has the sign-adjusted form
\[
 (-1)^dH_{V,\mathrm{LEFT}}
 =A_{\mathrm{rest}}^\alpha
   \sum_{0\le i\le j\le M}
    b^i c^{d-j}
    \prod_{r<i}\alpha_r\prod_{j<r\le M}\alpha_r\,K_{i,j},
 \tag{1}
\]
where \(K_{i,i}=1\), \(K_{i,i+1}=\beta_{i+1}A\), and
\[
 K_{i,j}=\beta_j A K_{i,j-1}+\gamma_jP K_{i,j-2}.
\]
The raw resolvent sign is independent of the endpoints. The path sign
\((-1)^{j-i}\), followed by changing the \(d-j+i\) outside factors from
\(\sigma-c_r\) to \(-\alpha_r\), gives exactly \((-1)^d\).

Set \(B_{-1}=1\) and \(R_{-1}=R_{-2}=Z_{-1}=0\). For \(0\le r\le M\), let
\[
 \begin{aligned}
 B_r&=b\alpha_r B_{r-1},\\
 R_r&=B_{r-1}+\beta_r A R_{r-1}+\gamma_r P R_{r-2},\\
 Z_r&=R_r+c\alpha_rZ_{r-1}.
 \end{aligned}\tag{2}
\]
Induction, first on the last active step and then on the last inactive
step, gives
\[
 B_r=\prod_{u=0}^{r}b\alpha_u,\qquad
 R_r=\sum_{i=0}^{r}b^i\prod_{u<i}\alpha_u\,K_{i,r},
\]
\[
 Z_r=\sum_{0\le i\le j\le r}
 b^ic^{r-j}\prod_{u<i}\alpha_u\prod_{j<u\le r}\alpha_u\,K_{i,j}.
\]
In particular the diagonal \(i=j\) is retained, and
\[
 \boxed{(-1)^dH_{V,\mathrm{LEFT}}
       =A_{\mathrm{rest}}^\alpha c^{d-M}Z_M.}\tag{3}
\]

For the full numerator, the original path expansion runs over
\(0\le i\le j\le d\). Take \(M=d\) and the empty omitted-half product
\(A_{\mathrm{rest}}^\alpha=1\). The same induction gives
\((-1)^dH_V=Z_d\), with every unused diagonal factor still present.
The half-grid scalar formula in §3 is specific to the half-row restriction.

## 2. Four literal states

Equations (2) are the polynomial transfer
\[
 \begin{pmatrix}B_r\\R_r\\R_{r-1}\\Z_r\end{pmatrix}
 =T_r\begin{pmatrix}B_{r-1}\\R_{r-1}\\R_{r-2}\\Z_{r-1}\end{pmatrix},
 \qquad
 T_r=\begin{pmatrix}
 b\alpha_r&0&0&0\\
 1&\beta_rA&\gamma_rP&0\\
 0&1&0&0\\
 1&\beta_rA&\gamma_rP&c\alpha_r
 \end{pmatrix}.
 \tag{4}
\]
The initial vector is \((1,0,0,0)^T\). The direct before-to-after entry
\(1\) accounts for starting and ending at the same row. There is no
denominator at the initial rows or a sampled spectral zero.

The diagonal blocks are the before scalar \(b\alpha_r\), the original
active companion
\[
 C_r=\begin{pmatrix}\beta_rA&\gamma_rP\\1&0\end{pmatrix},
\]
and the after scalar \(c\alpha_r\). Reversing the block order makes (4)
upper triangular. On a strict compact row and spectral chart its active
eigenvalues have limits
\[
 \Lambda_\pm(t)=2s\left[As\pm
  \sqrt{s^2(x-y)^2+4xy\cos^2(\pi\delta)}\right],
 \qquad s=\sin(\pi t).
 \tag{5}
\]
For positive \(x,y\), \(0<t<1/2\), and \(0<\delta<1/2\), the positive
root is separated from the other root. The latter can vanish at the pole
and must not be inverted. On the post-pole side \(\alpha(t)<0\), the
after scalar is negative for positive \(c\), so it is separated from
\(\Lambda_+\) even where their moduli coincide. The phase change
\(c\mapsto-c\) can restore resonance.

This identifies a possible input to the
[analytic switching theorem](research_analytic_switching_suppression.md).
It alone does not prove suppression where a genuine eigenvalue crossing
remains, and separation from the secondary eigenvalue must also be checked.

## 3. The omitted-half scalar stays exact

For the product convention \(\alpha_r=c_r-\sigma\),
\[
 A_{\mathrm{rest}}^\alpha=
 \begin{cases}
  2\cos(N\pi\delta),&N\text{ even},\\
  -4\sin(\pi\delta)\sin(N\pi\delta),&N\text{ odd}.
 \end{cases}\tag{6}
\]
The exact product definition fixes the signs, which would differ in the
alternative \(\sigma-c_r\) convention. The odd central factor is included.
Neither scalar is assumed nonzero; its oscillatory modes stay in (3).
RIGHT follows by the literal original row reflection and middle interchange.

A full-source application must still retain the original shared targets,
half-twist and framing characters, and Fourier endpoint currents. An
absolute-switch maximum with no actual eigenvalue resonance is only a
candidate for suppression: a boundary-branch gap and a uniform analytic
gauge estimate are additional hypotheses. No global source bound is claimed.

The [focused audit](../experiments/audit_research_original_four_state_transfer.py)
and its [results](../experiments/research_original_four_state_transfer_results.json)
check the finite transfer against the independent start/end expansion at
both parities and the exact scalar modes: 10 levels, 49 spectral values,
196 transfer/path comparisons and 85 scalar-mode identities. The original matrix interface is
inherited from the local numerator formula; these checks are not
advertised as a new independent audit of the physical matrix.