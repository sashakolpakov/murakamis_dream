# A fixed certificate for the two roots of the Wall degree recurrence

Research protocol, 7 November 2026. This protocol is written before the
checker is executed. It concerns an explicit polynomial inequality on
the full original parameter enclosure. It does not evaluate a quantum
sum, locate a new critical point, or test a new parameter value.

The [initialized recurrence proof](research_mixed_fourier_right_cap_wall_endpoint_strip.md)
already controls the actual finite solution on a fixed interval near
degree zero. The proposed certificate would supply the uniform root
separation needed to continue that proof through half the degree range.
The comparison with the final geometric rate remains a separate problem.

## 1. The inequality and its consequence

Write \(Y=p+iv\), \(k=p^2+v^2\), and \(u=k-p\). For
\(w=e^{-2\pi it}=c-is\), \(0\le t\le1/2\), put
\[
 A=w(1-Yw),\qquad C=Yw(1-w),\qquad D=A+C-Y.
\]
The limiting degree recurrence has characteristic polynomial
\[
                         P(R)=AR^2-DR+C.
\]
Define
\[
 h=|A|^2-|C|^2,\qquad B=A\overline D-D\overline C.
\]
Direct expansion, using \(c^2+s^2=1\), gives
\[
 \begin{split}
 h&=1-k+2uc-2vs,\\
 \Re B&=1-k+3uc-vs,\\
 \Im B&=vc+(p+k)s-4kcs.
 \end{split}                                                    \tag{1}
\]
The fixed target is the strict inequality
\[
                       \mathcal Q=|B|^2-h^2>0                    \tag{2}
\]
over the entire closed lower unit semicircle and the entire saved
complex enclosure of \(Y\).

Here is a direct root-count argument. If \(|R|=1\) and \(P(R)=0\),
then
\[
 P^*(R)=\overline C R^2-\overline D R+\overline A
                         =R^2\overline{P(R)}=0.
\]
Consequently
\[
             \overline A P(R)-C P^*(R)=R(hR-\overline B)=0,
\]
so \(|h|=|B|\), contradicting (2). At \(w=1\) the two roots are
\(0\) and \((1-2Y)/(1-Y)\). The elementary bounds
\[
                   |Y|<1,\qquad 3|Y|^2-2\Re Y>0                 \tag{3}
\]
make the second root strictly exterior to the unit circle. Since
\(A\ne0\) throughout, continuity and the exclusion of unit roots
give exactly one root inside and one outside for every \(t\).
The two roots are simple. Compactness gives a uniform bound
\[
                 |R_{\rm in}/R_{\rm out}|\le\vartheta<1.        \tag{4}
\]
The derivative of the ratio recurrence at its exterior fixed point
is exactly \(C/(AR_{\rm out}^2)=R_{\rm in}/R_{\rm out}\).
Thus (4) is the contraction needed by the initialized finite-solution
argument. Small complex parameter neighborhoods and the finite
\(r=e^{-2\pi i/N}\) perturbation preserve it. No conclusion about
an uninitialized formal solution is used.

## 2. The two fixed rational charts

Use \(x\in[0,1]\), \(d=1+x^2\), and precisely these two charts:
\[
 \begin{array}{c|cc}
     &c_{\rm num}&s_{\rm num}\\ \hline
 0&1-x^2&2x\\
 1&-2x&1-x^2
 \end{array}
 \qquad c=c_{\rm num}/d,\quad s=s_{\rm num}/d.
\]
They cover \(w=1\) through \(-i\) to \(-1\), including the
endpoints. Form the degree-at-most-four polynomials
\[
 \begin{split}
 H&=(1-k)d^2+2u c_{\rm num}d-2v s_{\rm num}d,\\
 E&=(1-k)d^2+3u c_{\rm num}d-v s_{\rm num}d,\\
 F&=v c_{\rm num}d+(p+k)s_{\rm num}d
                                      -4k c_{\rm num}s_{\rm num}.
 \end{split}
\]
Then the degree-at-most-eight polynomial
\[
                       Q_{\rm num}=E^2+F^2-H^2=d^4\mathcal Q  \tag{5}
\]
is built by exact rational interval arithmetic. Each occurrence of
\(p,v\) uses the original closed rectangular enclosure, without a
center substitution. Interval dependence may weaken a bound but
cannot invalidate it. The common chart variable is retained as a
polynomial variable throughout construction.

Each chart is partitioned into exactly 64 closed cells
\([j/64,(j+1)/64]\), \(j=0,\ldots,63\). On a cell substitute
\(x=(j+t)/64\) and pad the resulting power coefficients to degree
eight. If these interval coefficients are \(a_0,\ldots,a_8\), the
degree-eight Bernstein coefficients are
\[
              b_j=\sum_{i=0}^j a_i
                         \frac{\binom ji}{\binom8i},
                         \qquad 0\le j\le8.                    \tag{6}
\]
Every lower endpoint of every \(b_j\) must be strictly positive.
The Bernstein basis is nonnegative and sums to one on \([0,1]\),
so this proves (5) positive on the full cell. There are exactly 128
cells and 1152 recorded Bernstein intervals. If \(m>0\) is the
least recorded coefficient lower endpoint, then
\(\mathcal Q\ge m/16\), since \(1\le d\le2\).

## 3. Original inputs and provenance

The source is
`repro/results/research-mixed-fourier-boundary-update.json`, SHA256
`5d4cb057cb82ca4fff826ad768012480fd6f51afe66d3f5c632e48983cf17514`.
Its writer is `experiments/check_mixed_fourier_boundary_update.py`,
SHA256 `5017a53b6417630f1cab1e9c4be3f71d3ad24256af1ca67a8edd8faf0be0b1cc`.
The parameter enclosure is exactly `constants.K`; its canonical JSON
SHA256 is
`00f030c9a079403c2811e9b1c0dcca898ca8d912f4c11c0e338b3cc655a89591`.
It encloses \(Y=1/(1+2a-4a^2)\) on the full original root square.

The original algebraic reference is
`repro/results/research-three-four-source-interface.json`, SHA256
`9218011f3f5d41ff15835f74ccf83ccfeb266beea112c67607fa1eaef96ba9dd`;
its writer is `experiments/check_three_four_source_interface.py`,
SHA256 `e9d009fdf8712a7577bd9220c8bbf6c2f8fd1d3eefece969cad45357d8a45f91`.
The canonical root-certificate SHA256 is
`f04e925c094ba2f2c6723d3321cb58ac4988255b52e3408c2895b662bcf1cf8f`.

The checker verifies both saved successes; the original boundary
inventory of 512 passed arcs with no failed or inconclusive arcs;
the root-center, radius, full-square and reference associations; and
all inherited input bindings. It verifies the finite rational interval
format, the saved nonzero denominator assertion, and the canonical
identities above. It checks (3), \(\Im Y>0\), and nonzero \(Y\)
directly from the full rational intervals. All inputs, the present
protocol, the initialized recurrence note and the checker itself are
hashed before and after the run. No source calculation is replayed.

## 4. Execution and acceptance

The standard-library checker is
`experiments/check_mixed_fourier_wall_degree_separation.py`. Its output
is a fresh, exclusively created file
`repro/results/research-mixed-fourier-wall-degree-separation.json`.
The checker and this protocol must have their hashes frozen after full
proof and code review, before the single root execution.

The output records both chart polynomials, every affine substituted
power polynomial, all 1152 Bernstein intervals, the minimum lower
endpoint, the elementary bounds, the source associations, and the
before/after hashes. Acceptance requires all 128 cells to pass, all
elementary and provenance checks to pass, the exact inventory to be
complete, and every input hash to remain unchanged.

A failed or inconclusive cell remains in the record. There is no
adaptive partition, alternative test, refinement, root re-enclosure,
parameter search, or retry. This test contains no transcendental
evaluation, quantum-source evaluation, root solve, gain optimization,
or source replay. A successful result proves only the separation
statement above. The actual finite-solution continuation and its
comparison with the geometric contribution require written proofs.
