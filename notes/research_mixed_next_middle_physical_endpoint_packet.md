# A uniform endpoint packet for the coupled physical-index sum

Private written source proof, 8 November 2026. No mathematical
numerical evaluation or frozen-source edit is used.

For every outgoing index bounded below by a fixed fraction of the
level, the actual coupled physical-index sum has a nonzero endpoint
factor. Its exponential size is exactly that of its last positive
amplitude. This identifies where the remaining cancellation must
occur, without asserting a bound for the further coupled sums.

## 1. The original finite quantity

Use the original notation and exact source identity in
[coupled phases, equations (2), (7)--(8)](research_mixed_next_middle_insertion_coupled_phases.md):
\[
\begin{gathered}
q=e^{\pi i/N},\quad s_a=2\sin(\pi a/N),\quad
S_a=\prod_{\nu=1}^a s_\nu,\\
L=\lfloor N/6\rfloor,\quad U=\lfloor N/2\rfloor-1,
\quad m_{jk}=\max\{L,j,k\},\\
a_n^{j,k}=\frac{S_n^3}{S_{n-j}S_{n+j+1}S_{n-k}},\qquad
W_{jk,N}=\sum_{n=m_{jk}}^U q^{-(k+1)n}a_n^{j,k}.
\end{gathered}                                                     \tag{1}
\]
All denominator indices in (1) are below \(N\), with \(S_0=1\).
The index \(n=D-b\) is the original physical-node index in
reversed order. Both the lower cutoff \(L\) and the upper cutoff
\(U\) remain as prescribed by the actual middle right band.

Fix any \(0<\varepsilon<1/2\). For
\[
0\le j\le U,\qquad \varepsilon N\le k\le U,
\quad \eta=j/N,\quad t=k/N,
\]
put
\[
 r(\eta,t)=\cos^2(\pi\eta)\cos(\pi t),\qquad
 \mathfrak b(\eta,t)=
       \frac1{1-e^{i\pi t}r(\eta,t)} .
                                                                  \tag{2}
\]
Here \(0\le r(\eta,t)\le\cos(\pi\varepsilon)<1\).

**Theorem.** Uniformly over these exact indices and both parities,
\[
 \boxed{\quad
 W_{jk,N}=q^{-(k+1)U}a_U^{j,k}
                 \{\mathfrak b(\eta,t)+O_\varepsilon(N^{-1})\}.
 \quad}                                                          \tag{3}
\]
The error in (3) is absolute after division by \(a_U^{j,k}\).
Equivalently it is a relative \(O_\varepsilon(N^{-1})\) error,
since
\[
\frac1{1+\cos(\pi\varepsilon)}
 \le|\mathfrak b(\eta,t)|
 \le\frac1{1-\cos(\pi\varepsilon)} .                           \tag{4}
\]
In particular, for sufficiently large \(N\),
\[
 \frac14a_U^{j,k}\le|W_{jk,N}|\le C_\varepsilon a_U^{j,k}.
                                                                  \tag{5}
\]
This is a packet for the specified finite \(n\)-sum only.

## 2. Positive amplitude growth and a uniform reverse-ratio bound

For \(m_{jk}\le n<U\), the exact forward ratio is
\[
\frac{a_{n+1}^{j,k}}{a_n^{j,k}}
 =\frac{s_{n+1}^3}
        {s_{n-j+1}s_{n+j+2}s_{n-k+1}} .                        \tag{6}
\]
It is strictly greater than one whenever \(k\ge1\).
To see this, put
\(x=\pi(n+1)/N\), \(\alpha=\pi j/N\),
\(\beta=\pi k/N\), and \(d=\pi/N\).
The function
\[
\sin(x-\alpha)\sin(x+\alpha+d)
 =\tfrac12\{\cos(2\alpha+d)-\cos(2x+d)\}
\]
decreases with \(\alpha\) throughout the stated index range.
It is therefore at most \(\sin x\sin(x+d)\).
Since \(\beta\ge d\) and \(0<x<\pi/2\), the remaining
denominator factor is at most \(\sin(x-d)\). Thus the
product of the three denominator sines is at most
\[
 \sin x\sin(x+d)\sin(x-d)
       =\sin x\{\sin^2x-\sin^2d\}<\sin^3x .
\]
All factors are nonnegative. This proves (6)'s assertion
without a limiting argument.

For reverse ratios inside the actual range, write
\[
 r_n^{j,k}=\frac{a_{n-1}^{j,k}}{a_n^{j,k}}
 =\frac{\sin\frac{\pi(n-j)}N
        \sin\frac{\pi(n+j+1)}N
        \sin\frac{\pi(n-k)}N}
        {\sin^3\frac{\pi n}N},\qquad m_{jk}<n\le U .
                                                                  \tag{7}
\]
The same pair comparison, now with \(x=\pi n/N\), gives
\[
 r_n^{j,k}\le
  \frac{\sin(x+d)}{\sin x}\cos(\pi t)
 \le\{1+d\cot(\pi\varepsilon)\}\cos(\pi\varepsilon).
                                                                  \tag{8}
\]
Here \(x\ge\pi t\ge\pi\varepsilon\), and
\(\sin(x-\pi t)\le\sin x\cos(\pi t)\).
Let
\[
 r_\varepsilon=\tfrac12\{1+\cos(\pi\varepsilon)\}<1 .
\]
For all sufficiently large \(N\), (8) is at most
\(r_\varepsilon\). The threshold depends only on
\(\varepsilon\), not on \(j,k\).
Thus all valid backward amplitudes satisfy
\[
             a_{U-l}^{j,k}/a_U^{j,k}\le r_\varepsilon^l .
                                                                  \tag{9}
\]
The physical lower cutoff has not been extended to an infinite sum.

## 3. Endpoint expansion with the actual stopping conditions

Whenever \(n\ge N/4\), the right side of (7), viewed as a
function of its scaled arguments, has uniformly bounded first
derivatives: its own denominator is bounded away from zero.
Since \(U/N=1/2+O(N^{-1})\), this gives
\[
 r_{U-l+1}^{j,k}
   =r(\eta,t)+O((l+1)/N),                                    \tag{10}
\]
uniformly while that ratio exists and its index is at least
\(N/4\). The assertion follows by evaluating the three numerator
sines at \(n/N=1/2\); their product becomes
\(\cos^2(\pi\eta)\cos(\pi t)\).

There are two types of lower endpoint.
If \(m_{jk}=j\) or \(m_{jk}=k\), the formula on the right of
(7), evaluated at \(n=m_{jk}\), is exactly zero. We may use
that zero for the stopping ratio without introducing a factorial
at a negative index. If this endpoint is at least \(N/4\),
(10) still holds for that zero; if it is smaller, its normalized
amplitude is already exponentially small by (9).
If \(m_{jk}=L>\max(j,k)\), its missing next ratio is a genuine
cutoff term. Its amplitude satisfies
\[
 a_L^{j,k}/a_U^{j,k}
          \le r_\varepsilon^{U-L},\qquad U-L=N/3+O(1).
                                                                  \tag{11}
\]
Thus this original endpoint term is exponentially small, with
no fictitious wrap or zero imposed upon it. Ties with \(j\) or
\(k\) fall in the preceding zero-factor case.

Here is a direct error estimate retaining those endpoints.
Put \(J=U-m_{jk}\), \(A_l=a_{U-l}^{j,k}/a_U^{j,k}\),
\(\zeta=q^{k+1}\), and
\(F=\sum_{l=0}^J A_l\zeta^l\). Then exactly
\[
\begin{split}
(1-\zeta r)F=1
 &+\sum_{l=1}^J
        (r_{U-l+1}^{j,k}-r)A_{l-1}\zeta^l
       -rA_J\zeta^{J+1},\qquad r=r(\eta,t).
\end{split}                                                       \tag{12}
\]
At a zero-factor endpoint the last term is the same difference
with its stopping ratio zero. It is controlled by (10) whenever
that endpoint is in the upper quarter. At the cutoff endpoint
\(L\), it is controlled by (11).
For the other terms with index at least \(N/4\), (9)--(10)
bound their total by
\[
 \frac{C}{N}\sum_{l\ge1}(l+1)r_\varepsilon^{l-1}
                         =O_\varepsilon(N^{-1}).
\]
All remaining terms have \(l\ge N/4-O(1)\), so (9) bounds
their total exponentially. Since
\(|1-\zeta r|\ge1-\cos(\pi\varepsilon)>0\), (12) proves
\[
 F=\frac1{1-\zeta r}+O_\varepsilon(N^{-1})
  =\mathfrak b(\eta,t)+O_\varepsilon(N^{-1}).                  \tag{13}
\]
The last replacement uses only
\(\zeta=e^{i\pi t}e^{i\pi/N}\). Finally
\(W_{jk,N}=q^{-(k+1)U}a_U^{j,k}F\), which proves (3)--(5).

## 4. Exact parity amplitudes and exponential size

The last amplitude has particularly simple exact forms.
At \(N=2m\), \(U=m-1\), factorial reflection gives
\[
 S_{U-j}S_{U+j+1}=N,\quad S_U^2=N/2,
 \qquad
             a_U^{j,k}=\frac{S_U}{2S_{U-k}} .                 \tag{14}
\]
It is independent of \(j\). At \(N=2m+1\), \(U=m-1\),
\[
 S_{U-j}S_{U+j+1}=N/s_{m-j},\qquad
 S_U^2=\frac{N}{4\cos^2(\pi/(2N))},
\]
and therefore
\[
 a_U^{j,k}
   =\frac{S_U s_{m-j}}
          {4\cos^2(\pi/(2N))S_{U-k}} .                        \tag{15}
\]
The extra sine in (15) stays between a reciprocal polynomial
and an absolute constant for every retained \(j\).
With \(J(y)=\int_0^y\log(2\sin\pi x)\,dx\), the original
[uniform factorial estimates](research_three_crossing_real_period_newton_bound.md)
now give
\[
 \log|W_{jk,N}|=-N J(1/2-k/N)+O_\varepsilon(\log N),
                                                                  \tag{16}
\]
uniformly over the theorem's full index range. The
\(O(N^{-1})\) displacement of \(U/N\) from \(1/2\) costs
only \(O(\log N)\), including \(k=U\). No coefficient
near the parity-dependent endpoint has been dropped.

## 5. What this does and does not permit in the full source

The [small outgoing-index theorem](research_mixed_next_three_small_outgoing_indices.md)
leaves
\(k>\lfloor N/4096\rfloor\). The present result applies to
all these indices with \(\varepsilon=1/4096\), retaining every
\(j\), and shows that their \(n\)-sum has no exponential
cancellation relative to its last positive amplitude.
It still has the original endpoint phase
\(q^{-(k+1)U}\) and the nonconstant factor (2).

This does not lower-bound the remaining coupled \(j,k\)-sum.
In particular the error in (3) cannot simply be discarded inside
that sum: the error is only a relative polynomial-order estimate
for each individual coefficient, whereas further source cancellation
could be exponential. The exact coefficients (1), or a separately
controlled full remainder after their replacement, must remain in
the Fourier trace of the coupled-phase note.

The original factor \(\kappa(-q)^D/N\), the outgoing polynomials,
and every paired-contour current are unchanged. This theorem gives
a source-specific endpoint packet and a precise restriction on an
\(n\)-only cancellation strategy, not a full middle-insertion bound
or a noncancellation theorem for the \(343\) transfer.
