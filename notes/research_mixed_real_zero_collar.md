# A zero-uniform real collar for one small outer angle

Research proof, 4 November 2026. The 256-bit author certificate passes
all 64 reference products on 1,650 cells, 18 scalar comparisons and two
current source-record validations. The full written and acceptance-code
audit passes. This note leaves all completed source artifacts unchanged.

Both target heights are zero. One target angle may approach zero with
the level or equal zero exactly; the other ranges over the closed
interval \([.22,.5]\). The proof uses the literal original rows and a
forced Fourier recurrence, not a compact saddle asymptotic at the small
angle.

## 1. Statement and original normalization

Retain the original kernel and Fourier polynomial
\[
 \begin{split}
 C_{\epsilon,N}(X,Y)
  &=\sum_{j=0}^{N-1}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\epsilon}},\\
 p_j(X)&=(r_NX;r_N)_j,\qquad
 P_j=(r_N;r_N)_j,\qquad r_N=e^{-2\pi i/N},\\
 d_N(r_N^j)&=P_j^{-1},\qquad\deg d_N<N.
 \end{split}                                                   \tag{1}
\]
Let \(\eta,\epsilon\in\{0,1\}\), and let the independent complex
reference pair \(r=(a,b)\) range over
\[
 R_{3+\eta}\times R_{3+\epsilon},\qquad
 R_3=[.30,.39]+i[-.03,.02],\quad
 R_4=[.27,.33]+i[-.057,-.02].                                 \tag{2}
\]
Use the original zero-lift conditional root and allocated phase
\[
 \begin{split}
 g(z)&=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},\\
 \Phi(a,b)&=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias
               -(1+\eta/2)g(a)-(1+\epsilon/2)g(b),\\
 \Gamma_r(t)&=\Phi(r)+\Phi_a(r)(t_1-a)+\Phi_b(r)(t_2-b).
 \end{split}                                                   \tag{3}
\]
The reference branch is the one from the
[full endpoint theorem](research_mixed_all_endpoint_support.md).

Set \(L=1/1000\). The targets are real and belong to
\[
 {\cal C}=\bigl([0,L]\times[.22,.5]\bigr)
                 \cup\bigl([.22,.5]\times[0,L]\bigr).
 \tag{4}
\]

**Theorem 1.** Uniformly over (2) and (4), both parities satisfy
\[
 \begin{split}
 &|C_{\epsilon,N}(e^{-2\pi it_1},e^{-2\pi it_2})|\,
   |d_N(e^{-2\pi it_1})|^{\eta/2}
   |d_N(e^{-2\pi it_2})|^{\epsilon/2}\\
 &\hspace{15mm}\le C N^A
        \exp N\{\Re\Gamma_r(t)-3/50\}.
 \end{split}                                                   \tag{5}
\]
The same assertion holds after replacing the kernel modulus by the
sum of the moduli of all its original rows. Every selected outer factor
has modulus one at these real target points, so (5) includes every
selection. Neither endpoint in (4) is omitted.

This is a uniform upper bound, not a nonzero packet or a derivative
statement at zero. Together with separate compact real-source bounds
it supplies the small-angle collar needed for an upper estimate.
It does not itself enlarge those compact bounds at the other
half-period endpoint or assert a whole-word asymptotic.

## 2. A uniform perturbation of every endpoint row

Let \(J(u)=\Re g(u)\) on \([0,1]\), extended periodically. Its
derivative almost everywhere is \(\log(2|\sin\pi u|)\), and its
periodic mean derivative is zero. For every \(0\le u\le1\) and
\(0\le x\le L\),
\[
 \begin{split}
 J(u+x)-J(u)-J(x)
 &\le x\log2-J(x)\\
 &\le L\log2-J(L)=:\Delta_L .
 \end{split}                                                   \tag{6}
\]
The first inequality integrates the global upper bound
\(\log(2|\sin\pi u|)\le\log2\), including intervals crossing a
period endpoint. The second uses that \(J\) is decreasing on
\([0,L]\subset[0,1/6]\).

The zero-uniform truncated-log product estimate therefore gives
\[
 \frac{|p_j(e^{-2\pi ix})|}{|P_j|}
                       \le C N^A e^{N\Delta_L},
 \qquad 0\le j<N,\quad 0\le x\le L.                           \tag{7}
\]
Indeed its logarithmic upper rate is the left side of (6), and
the error is \(O(\log N)\) uniformly in both variables. This includes
every upper row and every product zero. At \(x=0\), the ratio is
exactly one. The proof is the same truncated-log Riemann estimate
used in the [both-low raw theorem](research_mixed_both_low_raw_support.md);
no division by a vanishing denominator occurs because \(j<N\).

Since the targets are real, the original chirp has modulus one.
Replacing either low-angle factor in each row by its endpoint
factor \(P_j\) therefore costs at most the uniform factor (7).

## 3. The actual low Fourier weight, including its forcing

Put \(\nu_L=-J(L)>0\). Then
\[
 \sup_{0\le x\le L}|d_N(e^{-2\pi ix})|
                         \le C_L N^A e^{N\nu_L}.              \tag{8}
\]
This is not inferred from the single value \(d_N(1)=1\).

For each \(x\in[0,L]\), choose an integer \(k\ge0\) such that
\(y=x+k/N\in[L,L+1/N]\). At the starting point \(y\), the
[relative Fourier-weight theorem](research_mixed_fourier_weight_continuation.md),
Theorem 1, applies on a fixed compact interval containing
\([L,2L]\). Its factorial symbol is bounded there, and
\[
            -J(y)\le -J(L)+O_L(N^{-1}).
 \tag{9}
\]
Hence \(|d_N(e^{-2\pi iy})|\le C_L N^A e^{N\nu_L}\).

Now iterate the exact forced recurrence downward in the real angle:
\[
 d_N(r_N^{-1}X)=(1-X)d_N(X)
                           +\frac{X}{N^2}\sum_{q=0}^{N-1}X^q.
 \tag{10}
\]
For sufficiently large \(N\), all intermediate angles lie in
\([0,2L]\), and
\[
              |1-X|\le2\sin(2\pi L)<1/2,\qquad
       \left|\frac{X}{N^2}\sum_{q=0}^{N-1}X^q\right|\le1/N.
 \tag{11}
\]
The forcing contributions sum to at most \(2/N\). Combining this
with the starting estimate proves (8), uniformly through \(x=0\).
All selected frequency factors again have unit modulus.

## 4. Reuse of the complete endpoint source bounds

Let \(\alpha\) be the low target type and \(\beta\) the other target
type, with zero meaning type three. After (7), the row denominator
has power \(1+\epsilon\). The already certified height-zero,
slope-zero endpoint source bounds are
\[
 \begin{array}{c|rrrr}
 (\epsilon,\beta)&(0,0)&(0,1)&(1,0)&(1,1)\\ \hline
 B_{\epsilon\beta}&.325066&.386681&.460764&.515591 .
 \end{array}                                                   \tag{12}
\]
The \((0,1)\) entry is from the original
[endpoint support grid](research_mixed_endpoint_support_grid.md);
the other entries are from the
[full endpoint source grid](research_mixed_all_endpoint_support.md).
These are complete row/other-angle bounds, not values at proposed
optimizers. At height zero the two orientations have the same
source expression, because their chirp moduli agree.

For clarity, their continuum expression is
\[
 \sup_{0\le u,y\le1}
 \left\{J(y+u)-J(y)-(1+\epsilon)J(u)
                  +\frac\beta2\max(-J(y),0)\right\}
                                      <B_{\epsilon\beta}.     \tag{13}
\]
The actual other target lies in the compact interval \([.22,.5]\).
The absolute Fourier-weight theorem applies there, including
the forcing branch at \(y=.5\), with an arbitrarily small fixed
exponent tolerance. Choose it so that the allocated tolerance is
at most \(10^{-5}\). The other finite products have only polynomial
costs. Thus (7), (8) and (12) give the raw exponent
\[
           B_{\epsilon\beta}+\Delta_L+
                       \frac{\alpha}{2}\nu_L+10^{-5}.
 \tag{14}
\]
There is no compact-away-from-zero hypothesis on the low target.

Write \(c=0\) when the low angle is the first argument and \(c=1\)
when it is the second. Then
\((\alpha,\beta)=(\eta,\epsilon)\) for \(c=0\), and
\((\alpha,\beta)=(\epsilon,\eta)\) for \(c=1\).
The exact scalar checks and new reference cover give
\[
 \begin{array}{cc|cc|cc}
 \eta&\epsilon&
 \text{source},\,c=0&\text{plane},\,c=0&
 \text{source},\,c=1&\text{plane},\,c=1\\ \hline
 0&0&<.332&>.50&<.332&>.50\\
 0&1&<.523&>.585&<.471&>.76\\
 1&0&<.335&>.55&<.394&>.56\\
 1&1&<.526&>.64&<.526&>.83
 \end{array}                                                   \tag{15}
\]
Every plane-minus-source difference in (15) is strictly greater
than \(3/50\).

## 5. The reference comparison and scope

For a fixed reference the real plane is affine in both real targets.
Its minimum on each target rectangle in (4) is attained at one of
the four corners. For each such corner,
\(\Gamma_r(t)\) is separately holomorphic in both references.
The existing global reference branch therefore reduces the minimum
over (2) to its sixteen boundary-side products.

The new checker covers all sixty-four typed reference boundary
products, checking both orientations and all eight target corners
in every cell. It uses original logarithmic affine Newton enclosures
and the exact derivative
\[
       d_r\Gamma_r(t)=
         \sum_{j,k}\Phi_{jk}(r)(t_j-r_j)\,dr_k.                \tag{16}
\]
Every accepted bound is a full-cell mean-value bound. The exact
prefix-free covers have total area one. Their lower thresholds are
the plane columns of (15). Affinity and the harmonic minimum
principle recover the whole closed target and reference domains.
Combining those lower bounds with (14) proves (5).

No selected Fourier factor, high row, endpoint forcing, or original
chirp is removed. The only new source argument is the uniform
collar transfer (6)--(11); the complete endpoint scalar grids are
validated as current inputs. Nonzero target heights are outside
this theorem.

## Reproduction

    python3 experiments/certify_mixed_real_zero_collar.py --precision 256

The checker validates both inherited endpoint-source records, their
proof/script/dependency bindings, the scalar collar budgets, and all
new geometric reference comparisons.
