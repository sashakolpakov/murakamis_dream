# Contraction of the original even-run equation on the middle colors

Research note, 3 November 2026.

The backward equation for an even crossing run contracts on the
middle half of the color circle. This statement holds for every
initial vector and every physical input column. It does not require
choosing an eigenvalue branch. The proof uses a definite loss in
the first row of a short matrix product and propagates that loss
through the original channel path. The strongest estimate below
uses two-step Euclidean contraction, with loss \(1/(64k^2)\)
for the varying matrices and the explicit level threshold
\(N\ge2048k^2\). The earlier maximum-norm estimate is retained
as an independent argument.

The result removes this middle interval as a place where a
backward-propagated channel vector can acquire further growth.
It does not compare the two remaining end intervals or identify
their largest growth rate with hyperbolic volume.

## 1. The original equation and its boundary parameter

Let \(k\ge1\) be fixed and let the crossing power be \(2k\).
At level \(N\ge2\), put
\[
 q=e^{\pi i/N},\qquad Q=q^2,\qquad D=N-1,\qquad
 C_k(r)=(r+r^{-1})I_k-T_k-rE_{11},
 \tag{1}
\]
where \(T_k\) is adjacency on the path with \(k\) vertices.
The [original resonant source equation](research_resonant_crossing_run_source.md)
has the form
\[
 [C_k(qQ^j)-q^{-1}\lambda E_{kk}]u_j
     =4\sin^2(j\pi/N)\,u_{j-1}.
 \tag{2}
\]
For the original source column, \(\lambda=1\). For input column
\(\ell\), it is \(\lambda=Q^{-\ell}\), and (2) holds for
\(j>\ell\). Its initial residue vector and original scalar
are those in the cited source theorem. The estimates below
apply to any solution of (2); they do not change those data.

Put \(y_l=u_{D-l}\) and \(\theta_l=2\pi l/N\). Wherever (2)
holds and its sine factor is nonzero, the exact backward step is
\[
 y_l=\mathcal B_{N,l}(\lambda)y_{l-1},\qquad
 \mathcal B_{N,l}(\lambda)=
 \frac{C_k(e^{-i(\theta_l-\pi/N)})
                      -q^{-1}\lambda E_{kk}}
      {\,2-2\cos\theta_l\,}.
 \tag{3}
\]
In particular no inverse channel matrix appears in this
backward equation. Entrywise conjugation gives the corresponding
statement for a negative even power.

We use the matrix norm induced by the maximum norm on vectors:
\(\|A\|_\infty=\max_i\sum_j|A_{ij}|\).

## 2. A uniform loss for a frozen channel matrix

For real \(\theta\) and complex \(s\), define
\[
 w(\theta)=2-2\cos\theta,\qquad
 A_k(\theta,s)=
       \frac{C_k(e^{-i\theta})-sE_{kk}}{w(\theta)}.
 \tag{4}
\]
The boundary parameter \(s\) is held fixed when powers of this
matrix are taken.

**Lemma 1.** If \(k\ge2\), \(|s|\le1\), and
\(\pi/2\le\theta\le3\pi/2\), then
\[
 \|A_k(\theta,s)\|_\infty\le1,\qquad
 \|A_k(\theta,s)^{k+1}\|_\infty\le1-\delta_k,\qquad
                  \delta_k=\frac{4^{\,1-k}}9.
 \tag{5}
\]
The estimates include the two endpoints of the interval.

*Proof.* Write \(c=\cos\theta\le0\), \(w=2-2c\), and
\(A=A_k(\theta,s)\). Before division by \(w\), its first
diagonal entry is \(e^{i\theta}\), its interior diagonal
entries are \(2c\), its last diagonal entry is \(2c-s\),
and every adjacent entry is \(-1\). Thus its row sums in
absolute value are bounded respectively by
\[
       2,\qquad 2|c|+2=w,\qquad |2c-s|+1\le w .
 \tag{6}
\]
This proves the first assertion.

We first show that row one of \(A^2\) has sum at most
\(1-1/9\). If \(c\le-1/2\), row one of \(A\) has sum
\(2/w\le2/3\), and multiplication by the contraction \(A\)
preserves this bound. If \(-1/2\le c\le0\), examine the
two paths contributing to entry \((1,1)\) of the square.
Their sum before normalization is
\[
                         e^{2i\theta}+1 .
 \tag{7}
\]
Its modulus is \(2|c|=-2c\), whereas the sum of the two
individual moduli is two. The triangle inequality for
every other entry therefore gives
\[
 \sum_j |(A^2)_{1j}|
    \le \sum_j(|A|^2)_{1j}-\frac{2+2c}{w^2}
    \le 1-\frac19 .
 \tag{8}
\]
Here \(|A|\) means entrywise absolute value; its row sums
are at most one by (6). In the case considered,
\(2+2c\ge1\) and \(w\le3\), which proves (8).
This calculation remains valid for \(k=2\): the first and
last diagonal entries are distinct, and (7) is unchanged.

For row \(j\), the unique path of length \(j-1\) from
channel \(j\) to channel one uses every intervening
off-diagonal entry once. Consequently
\[
                  |(A^{j-1})_{j1}|=w^{1-j}\ge4^{1-j}.
 \tag{9}
\]
Use \(A^{j+1}=A^{j-1}A^2\), apply (8) to its first
intermediate row, and apply the contraction bound to all
other intermediate rows. The result is
\[
 \sum_t|(A^{j+1})_{jt}|
       \le 1-\frac{4^{1-j}}9 .
 \tag{10}
\]
Multiplying on the right by \(A^{k-j}\) cannot increase a
row sum. Equation (10), for \(1\le j\le k\), proves the
second assertion of (5). No eigenvector or eigenvalue
separation has been used. \(\square\)

The small constant in (5) is only a uniform certificate.
No optimality is claimed for it.

## 3. The varying original matrices

The next statement supplies explicit, deliberately conservative
constants. The lower bound on \(N\) concerns the quantum level,
not the number of twists.

**Theorem 2.** Fix \(k\ge2\), write \(m=k+1\), and set
\[
 N_0(k)=216m(4m+2)4^{k-1}.
 \tag{11}
\]
For \(N\ge N_0(k)\), \(|\lambda|\le1\), and integers
\(a<b\) for which every step \(a<l\le b\) satisfies
\[
                       N/4\le l\le3N/4 ,
 \tag{12}
\]
one has
\[
 \boxed{\quad
 \|\mathcal B_{N,b}(\lambda)\cdots
                  \mathcal B_{N,a+1}(\lambda)\|_\infty
 \le
 2(1-\delta_k/2)^{\lfloor(b-a)/(k+1)\rfloor}.
 \quad} \tag{13}
\]
In particular this is uniform in every physical input-column
clock \(Q^{-\ell}\), on the part of its homogeneous equation
where \(j>\ell\).

*Proof.* Hold \(s=q^{-1}\lambda\) fixed. It has modulus at
most one. On the interval in (12), \(w(\theta_l)\ge2\).
Changing \(e^{-i\theta_l}\) to
\(e^{-i(\theta_l-\pi/N)}\) changes the first diagonal
entry of \(C_k\) by at most \(\pi/N\) and every other
diagonal entry by at most \(2\pi/N\). Therefore
\[
 \|\mathcal B_{N,l}(\lambda)-A_k(\theta_l,s)\|_\infty
                    \le\pi/N .
 \tag{14}
\]
Also, directly differentiating (4) and using (6) gives
\[
       \|\partial_\theta A_k(\theta,s)\|_\infty\le2
 \tag{15}
\]
on this entire interval, uniformly for \(|s|\le1\).

Freeze the first angle of any block of \(m\) steps.
Equations (14)--(15) show that every matrix in the block
differs from the frozen matrix by at most
\[
                      e_N=\frac{\pi(4m+1)}N.
 \tag{16}
\]
The product telescoping identity bounds the difference
between the varying block and the \(m\)-th power of the
frozen matrix by
\[
                    m e_N(1+e_N)^{m-1}.
 \tag{17}
\]
The explicit choice (11), using \(\pi<4\), ensures
\(e_N\le\delta_k/(6m)\). Thus
\((1+e_N)^{m-1}<3\) and (17) is at most
\(\delta_k/2\). Lemma 1 proves that every full block is
bounded by \(1-\delta_k/2\).

Partition the indicated product into such blocks. There
are fewer than \(m\) remaining steps. Each has norm at
most \(1+\pi/N\), by (14), and
\((1+\pi/N)^m<2\) under (11). Multiplying these bounds
proves (13). \(\square\)

For the one-channel source \(p=2\), \(\lambda=1\), the
exact backward multiplier has modulus
\[
        |\mathcal B_{N,l}(1)|
             =\frac1{2|\sin(\pi l/N)|}\le\frac1{\sqrt2}
 \tag{18}
\]
on (12), with no lower bound on \(N\) beyond the existence
of those steps. For arbitrary \(|\lambda|\le1\), its
modulus is at most \(2/w(\theta_l)\le1\); on
\(N/3\le l\le2N/3\) it is at most \(2/3\).

## 4. Two-step contraction with polynomial dependence on the rank

The symmetric channel structure improves the length and constants
of the preceding contraction. Write \(\|\cdot\|_2\) for the
Euclidean operator norm.

**Theorem 3.** For every \(k\ge2\), \(|s|\le1\), and
\(\pi/2\le\theta\le3\pi/2\), the frozen matrix satisfies
\[
 \boxed{\qquad
 \|A_k(\theta,s)^2\|_2\le1-\frac1{32k^2}.
 \qquad}                                                     \tag{19}
\]
Consequently, for \(N\ge2048k^2\), \(|\lambda|\le1\),
and the original varying steps in (12),
\[
 \boxed{\quad
 \|\mathcal B_{N,b}(\lambda)\cdots
                \mathcal B_{N,a+1}(\lambda)\|_2
 \le
 2\left(1-\frac1{64k^2}\right)^{\lfloor(b-a)/2\rfloor}.
 \quad}                                                       \tag{20}
\]
The boundary clock is arbitrary in the closed unit disk, so this
again applies to every physical input column on its homogeneous
range.

*Proof.* Set \(A=A_k(\theta,s)\), \(c=\cos\theta\le0\),
\(w=2-2c\), and \(S=|A^2|\), with absolute values taken
entrywise. Since \(A\) is complex symmetric, \(S\) is a real
symmetric nonnegative matrix. Lemma 1 shows that it is
substochastic and that its first row has deficit at least \(1/9\).
For every vector \(x\),
\[
 x^*(I-S)x
  =\sum_i\left(1-\sum_j S_{ij}\right)|x_i|^2
        +\sum_{i<j}S_{ij}|x_i-x_j|^2.                         \tag{21}
\]

Suppose first that \(k\ge3\). For \(1\le i\le k-2\)
there is a unique length-two channel path from \(i\) to
\(i+2\), and hence
\[
 S_{i,i+2}=w^{-2}\ge1/16,\qquad
 S_{12}=\frac{|e^{i\theta}+2c|}{w^2}
       =\frac{\sqrt{1+8c^2}}{w^2}\ge1/16.                    \tag{22}
\]
The edges in (22) form a tree: the two parity chains are
joined by the edge \(1\)--\(2\). Let \(\mathcal T\) denote
this tree. Along its path from vertex one to any vertex \(j\),
Cauchy--Schwarz gives
\[
 |x_j|^2\le k\left(
       |x_1|^2+\sum_{\{i,t\}\in\mathcal T}|x_i-x_t|^2\right).
\]
After summing over \(j\), (21)--(22) imply
\[
                 I-S\ \ge\ \frac1{16k^2}I.                \tag{23}
\]
Because \(S\) is real symmetric and nonnegative, its Euclidean
norm equals its Perron spectral radius. Also
\(|A^2x|\le S|x|\) entrywise. Thus (23) gives the stronger
bound \(\|A^2\|_2\le1-1/(16k^2)\) for \(k\ge3\).

For \(k=2\), put \(a=e^{i\theta}\), \(b=2c-s\), and
\(t=|a+b|\), so that \(wA\) has diagonal \(a,b\) and
off-diagonal entries \(-1\). If \(t\ge1/2\), then
\(S_{12}=t/w^2\ge1/32\). Equation (21) and
\(\|x\|_2^2\le3(|x_1|^2+|x_1-x_2|^2)\) give
\(I-S\ge I/96\).
If \(t\le1/2\), then \(|b|\le1+t\le3/2\), and row two
has sum at most
\[
 \frac{|b^2+1|+t}{w^2}
 \le\frac{|a^2+1|+|b^2-a^2|+t}{w^2}
 \le\frac{-2c+7/4}{(2-2c)^2}
 \le\frac7{16}.                                             \tag{24}
\]
The last inequality follows by differentiating
\((z+7/4)/(2+z)^2\) for \(z=-2c\ge0\); it is decreasing.
The first row remains bounded by \(8/9\), so in this case
\(\|S\|_2\le8/9\). Both cases imply (19), whose stated
constant for \(k=2\) is the weaker \(1/128\).

It remains to compare two successive actual steps with a frozen
square. Their differences in (14) are diagonal, so the same bound
\(\pi/N\) holds in Euclidean norm. The matrices
\(A_k(\theta,s)\) and their derivatives are symmetric, and the
maximum-row bounds (6) and (15) also bound their column norms.
Consequently
\(\|A_k(\theta,s)\|_2\le1\) and
\(\|\partial_\theta A_k(\theta,s)\|_2\le2\).
Holding \(s=q^{-1}\lambda\) fixed, comparison first with the
two unfrozen classical matrices and then with the frozen square
gives
\[
 \begin{split}
 \|\mathcal B_{N,l+1}\mathcal B_{N,l}
                         -A_k(\theta_l,s)^2\|_2
 &\le 2\pi/N+\pi^2/N^2+4\pi/N\\
 &<8\pi/N
 \le\frac1{64k^2},\qquad N\ge2048k^2.
 \end{split}                                                  \tag{25}
\]
Here the final inequality uses \(\pi<4\); both angles lie
in the closed middle interval. Equations (19) and (25) bound
each two-step block by \(1-1/(64k^2)\). A remaining single
step has norm at most \(1+\pi/N<2\).
Partitioning the original ordered product into these blocks
proves (20). \(\square\)

## 5. What this controls in the volume problem

Applied to the actual homogeneous source, (20) bounds the
whole channel vector at every intervening color by twice
its norm at the beginning of the backward interval, and
gives exponential decrease over a fixed positive fraction
of levels. The statement remains valid if the original
endpoint vector has cancellation in one of its entries.
It applies to the vector itself, rather than to a chosen
formal eigenmode.

Together with the
[backward boundary theorem](research_even_run_backward_source_growth.md),
it separates two tasks. The boundary theorem identifies
which modes the actual source supplies and proves growth
on a fixed short interval. The contraction theorem rules
out additional backward amplification on the middle
half. The remaining end intervals, the comparison of
their maxima, and a noncancellation estimate for a general
signed closing sum still require proof. In particular no
new volume equality or finite-exception assertion follows
from these contraction estimates alone. The backward boundary
note also gives a coefficient-level consequence: an exact
observation matrix transfers (20) to uniform localization of
the reflected norm to its two outer color quarters.

The [finite checker](../experiments/check_even_run_middle_color_contraction.py)
tests the first-row loss, shortest-path coefficient, and
two-step spectral and singular-norm bounds, then tests
blocks of the actual varying matrices at both level
parities and several physical input columns. Its
[120-digit record](../repro/results/research-even-run-middle-color-contraction.json)
contains 175 frozen cases, 126 earlier varying blocks, and
126 two-step blocks at \(N=2048k^2\) and \(N=2048k^2+1\).
The inequalities
on whole intervals and at all sufficiently large levels are
proved above, rather than inferred from these samples.
