# Exact wrapped entries in a geometric row window

Research proof, 4 November 2026. Frozen manuscripts and the completed
wrapped-factorization artifact are unchanged.

The relative wrapped insertion has a closed finite entry formula.
Its first superdiagonal and every fixed superdiagonal have a nonzero
symbol. In particular, compressing this operator to the dominant row
window of the original three-crossing matrix does not make its norm
exponentially small. This concerns the relative operator itself;
the coherent product with the original surrounding matrices remains
a different estimate.

## 1. Original normalization and the forced coefficients

Use the notation of the
[exact wrapped factorization](research_mixed_wrapped_operator_factorization.md).
Thus \(q=e^{\pi i/N}\), \(r=q^{-2}\), \(D=N-1\),
\(P_a=(r;r)_a\), \(S_a=|P_a|\), and
\[
 M A_4^{\mathrm{wrap}}M^{-1}=\kappa^2M^*\mathcal E M,\qquad
 \mathcal E=\operatorname{diag}(\overline{P_a})M\mathcal R M^{-1}.
 \tag{1}
\]
The matrix \(\mathcal E\) is strictly upper triangular. Retain the
literal original weight \(d_N(X)=\sum_{h=0}^{D}d_hX^h\), and put
\(c_k=d_{N-k}\), \(1\le k<N\). Its exact forced recurrence gives
\[
 c_1=N^{-2},\qquad
 c_{k+1}=(1-r^k)c_k+N^{-2},\qquad
 c_k=\frac{P_{k-1}}{N^2}\sum_{\ell=0}^{k-1}\frac1{P_\ell}.
 \tag{2}
\]
No homogeneous replacement of this sequence is used.

**Proposition 1.** For \(0\le i<j<N\), put \(d=j-i\). Then
\[
 \mathcal E_{ij}
 =-(-q)^{-d}r^{-j}\overline{\left(\frac{P_i^2}{P_j}\right)}
   \sum_{h=0}^{d-1}(-1)^h
      r^{(1-j)h+h(h-1)/2}
      {d-1\brack h}_r\,c_{h+1}.
 \tag{3}
\]
Here the Gaussian binomial is \(P_{d-1}/(P_hP_{d-1-h})\);
none of its denominators vanishes. In particular,
\[
       \mathcal E_{i,i+1}
          =\frac{\mathrm i q^i\overline{P_i}}
                 {2N^2\sin(\pi(i+1)/N)}.
 \tag{4}
\]
Here \(\mathrm i\) denotes the imaginary unit.

*Proof.* Let \(T_{ab}=[X^b](rX;r)_a\), and let \(Z\) be the
nilpotent lower shift, with \(Z_{a,a-1}=1\). Division of a polynomial
minus its constant term by \(X\) gives
\[
 K:=TZT^{-1},\qquad K_{ab}=-r^{b+1}\quad(a>b),\qquad K_{ab}=0
                    \quad(a\le b).
 \tag{5}
\]
Indeed \(((rX;r)_a-1)/X=-\sum_{b=0}^{a-1}r^{b+1}(rX;r)_b\).
For \(A>B\), every strictly decreasing path in \(K^k\) contributes
one product of the intermediate phases, so
\[
 (K^k)_{AB}
   =(-1)^k r^{B+1}
       e_{k-1}(r^{B+2},\ldots,r^A).
 \tag{6}
\]
The elementary symmetric polynomial is the Gaussian binomial
times \(r^{(B+2)(k-1)+(k-1)(k-2)/2}\).

The strict Toeplitz factor is \(\sum_{k=1}^{D}c_kZ^k\).
Use \(L=\operatorname{diag}(S_a)^{-1}T\) and the unitary reversal
\(\mathcal U\) from the preceding note in
\(\mathcal E=\operatorname{diag}(\overline P)\mathcal U
 L(\sum c_kZ^k)L^{-1}\mathcal U^*\).
Putting \(A=D-i\), \(B=D-j\) in (6), the diagonal and unitary
factors combine to
\((-q)^{-d}\overline{P_i^2/P_j}\). Since
\(r^{B+1}=r^{-j}\), this proves (3). Its single term at \(d=1\),
together with \(P_{i+1}=P_i(1-r^{i+1})\), gives (4).
\(\square\)

## 2. A nonzero symbol on every fixed superdiagonal

For each fixed positive integer \(d\), uniformly when \(i/N\)
lies in a compact subinterval of \((0,1)\),
\[
 \mathcal E_{i,i+d}
 =\frac{(-q)^{-d}\overline{P_i}}
        {N^2(1-r^{i+d})}\{1+O_d(N^{-1})\}.
 \tag{7}
\]
To prove this, (2) gives
\(c_k=N^{-2}(1+O_d(N^{-1}))\) for \(k\le d\).
With \(c_k\) replaced by \(N^{-2}\), the sum in (3) is exactly
\(N^{-2}(r^{1-j};r)_{d-1}\), by the finite q-binomial theorem.
Its factors stay uniformly away from zero for fixed \(d\) on the
specified compact interval. Multiplication by the prefactor in (3)
then gives exactly the leading expression in (7).
The finitely many errors are uniformly relative \(O_d(N^{-1})\).

Thus the insertion has a conjugate-factorial phase and amplitude
on these bands; its leading coefficient does not vanish. Formula
(7) is not a summation over an unbounded number of bands.

## 3. The exact exponential norm rate in shrinking row windows

Let
\(J(x)=\int_0^x\log(2\sin\pi t)\,dt\).
Fix \(x_0\in(0,1)\), and let \(\eta_N\to0\) with
\(N\eta_N\to\infty\). Let \(\Pi_N\) be the orthogonal coordinate
projection onto \(|a/N-x_0|\le\eta_N\).

**Theorem 2.** Along all integer levels,
\[
       \lim_{N\to\infty}\frac1N
            \log\|\Pi_N\mathcal E\Pi_N\|_2=J(x_0).
 \tag{8}
\]

*Proof.* For \(k\le2N\eta_N+2\), eventually
\(|1-r^k|\le2\pi k/N<1/2\). Induction in the exact recurrence
(2) gives \(|c_k|\le2/N^2\). Every phase in (6) has unit modulus,
so its elementary symmetric polynomial is bounded by
\(\binom{d-1}{k-1}\). Consequently (3) gives
\[
 |\mathcal E_{ij}|
       \le \frac{2^d}{N^2}\frac{S_i^2}{S_j}
          \quad(i<j\hbox{ in the window}).
 \tag{9}
\]
The uniform sine-factorial estimate
\(\log S_a=NJ(a/N)+O(\log N)\) holds on a fixed compact
neighborhood of \(x_0\). Also \(d\le2N\eta_N\).
The maximum entry bound (9), multiplied by the dimension \(N\),
therefore has upper exponential rate at most \(J(x_0)\).

The window contains consecutive indices \(i,i+1\) with \(i/N\to x_0\).
By (4), the operator norm is at least
\(S_i/[2N^2\sin(\pi(i+1)/N)]\), whose rate is \(J(x_0)\).
This proves the matching lower bound and (8). \(\square\)

For the original three-crossing dominant output row, \(x_0=2/3\).
The standard normalization gives
\(J(2/3)=-J(1/3)=c/3>0\), with \(c\) from the
[positive-three theorem](research_positive_three_crossing_cycle.md).
Thus even compression to a shrinking geometric row window has a
positive exponential rate. Its lower bound uses a coordinate
direction, not an actual geometric boundary vector. It proves no
lower bound for a prescribed scalar source.

The unresolved estimate is the coherent contraction in (1), or its
observed words, with the conjugate-factorial phase retained.
Neither (8) nor the nilpotence of \(\mathcal E\) settles that
contraction. In particular this note supplies no bound for the
exterior part of the original mixed outer contour.

## 4. A finite prefix with geometrically decreasing terms

The alternating binomial expression (3) has the exact reduction
\[
 \mathcal E_{ij}
 =\frac{(-q)^{i-j}\overline{P_i}}{N^2(1-r^j)}
   \sum_{\ell=0}^{j-i-1}
     \frac{P_{j-i-1}P_{j-1-\ell}}
          {P_{j-i-1-\ell}P_{j-1}} .
 \tag{10}
\]
In particular, the factor multiplying its first term is a single
finite prefix, not a sum over uncontrolled Fourier modes.

To prove (10), expand (2) as
\(N^2c_{h+1}=\sum_{\ell=0}^hP_h/P_{h-\ell}\) in (3).
For each fixed \(\ell\), the binomial sum over \(h-\ell\)
is another terminating q-binomial product. Divide by the product
at \(\ell=0\), and use
\[
 (r^{1-j};r)_\ell
  =(-1)^\ell r^{(1-j)\ell+\ell(\ell-1)/2}
       \frac{P_{j-1}}{P_{j-1-\ell}}.
\]
All alternating phases cancel in this ratio, giving (10).
The ratio of consecutive terms in its prefix is exactly
\[
 q^i\,
 \frac{\sin(\pi(j-i-1-\ell)/N)}
      {\sin(\pi(j-1-\ell)/N)}.
 \tag{11}
\]

**Proposition 3.** Uniformly over all physical integer pairs
\[
                  3/5\le i/N<j/N\le3/4,
\]
the original relative insertion has the packet
\[
 \mathcal E_{ij}
   =\frac{(-1)^{j-i}q^j\overline{P_i}}
          {2\mathrm i\,N^2\sin(\pi i/N)}
                                  \{1+O(N^{-1})\}.
 \tag{12}
\]
This includes every superdiagonal, even \(j-i=1\).

*Proof.* Write \(x=i/N\), \(y=j/N\), \(d=j-i\), and
\(z=q^i\sin(\pi d/N)/\sin(\pi j/N)\).
All moduli in (11), as well as \(|z|\), are bounded by the fixed
number
\(\rho=\sin(3\pi/20)/\sin(3\pi/4)<1\).
The ratios decrease in modulus as \(\ell\) increases: their
numerator decreases, and their denominator increases on the
specified interval above \(1/2\).
They differ from \(z\) by at most \(C(\ell+1)/N\).
The difference between a product of \(\ell\) such ratios and
\(z^\ell\) is therefore at most
\(C\ell^2\rho^{\ell-1}/N\).
Its sum is \(O(N^{-1})\), uniformly in the upper limit \(d-1\).
The omitted infinite geometric tail is also \(O(N^{-1})\):
\(|z|\le Cd/N\) gives
\(|z|^d\le Cd\rho^{d-1}/N\).
Thus the prefix in (10) is
\((1-z)^{-1}+O(N^{-1})\).
It is uniformly nonzero, and the error is relative as well.

Finally
\[
 1-e^{\pi ix}\frac{\sin\pi(y-x)}{\sin\pi y}
       =e^{-\pi i(y-x)}\frac{\sin\pi x}{\sin\pi y}.
\]
Substitution in (10) gives exactly (12). \(\square\)

The leading upper-triangular kernel in (12) separates into a row
factor and the column chirp \(b_j=(-q)^j\). This chirp has the exact
original identity
\[
 b^TM=\kappa^{-1}e_D^T,\qquad
 \sum_{j>i}b_jM_{jk}
    =\kappa^{-1}\mathbf1_{k=D}-\sum_{j\le i}b_jM_{jk}.
 \tag{13}
\]
Indeed it is the complex conjugate of
\(u^TM^{-1}=\kappa e_D^T\), where \(u_j=(-q^{-1})^j\).
The retained prefix on the right of (13) is essential, and it has
its own exact original-source reduction. For \(0\le k\le i<D\),
\[
 \begin{split}
 \sum_{j=k}^i(-q)^jM_{jk}
   &=\kappa q^{k^2+2k}{i+1\brack k+1}_Q\\
   &=(-1)^{i+1}q^{-i-2}M_{i+1,k+1},\qquad Q=q^2 .
 \end{split}
 \tag{14}
\]
The sum is zero for \(k>i\). In fact the original matrix entry
is \(M_{jk}=\kappa(-1)^j q^{j+k^2}{j\brack k}_Q\).
The q-Pascal difference
\({j+1\brack k+1}_Q-{j\brack k+1}_Q
=Q^{j-k}{j\brack k}_Q\) then telescopes to (14).
The full prefix at \(i=D\) is precisely (13); the Gaussian
binomial has value zero unless \(k=D\).
Differences of these prefix identities retain both ends of a
coordinate window, with no omitted boundary term.

Moreover the relative \(O(N^{-1})\) in (12) is an entrywise
source estimate; it cannot be discarded after a cancellation
without a bound on its coherent contraction. Formula (10) retains
the entire original remainder for that purpose.

## 5. Reproduction

    python3 experiments/check_mixed_wrapped_geometric_window.py

The exact checks verify the forced coefficients, backward-shift
conjugation, full finite entries, first superdiagonal and the
constant-coefficient q-binomial reduction, exact finite prefix,
and original complete and truncated chirp identities at levels two, three,
four and six. The window-rate and uniform-prefix assertions are analytic proofs
above, not an extrapolation of finite norms.
