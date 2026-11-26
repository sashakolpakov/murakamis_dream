# Exact conditional cancellation of one index family

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The original cyclic three/four source permits exact summation of all
left leg indices while the right leg indices remain fixed. For a
three-vertex, the oscillatory sum becomes one polynomial coefficient
and then a positive Hermitian Gram matrix. For a four-vertex it becomes
a weighted finite Gram matrix with an explicit forced difference law.
The remaining word still carries its original oscillation.

## 1. Original conditional kernel and normalization

Put \(r=e^{-2\pi i/N}\), \(Q=r^{-1}\),
\(q=e^{\pi i/N}\), \(P_j=(r;r)_j\), and let
\(S_j=\prod_{h=1}^j2\sin(\pi h/N)>0\), \(S_0=1\).
For \(0\le a,b<N\), \(\epsilon\in\{0,1\}\), define
\[
 L_\epsilon(a,b)=
 \sum_{i=0}^{N-1-\max(a,b)}
       \frac{r^{-ai}P_{i+a}P_{i+b}}{P_i^{2+\epsilon}},
 \qquad
 T_\epsilon(a,b)=\frac{L_\epsilon(a,b)}{P_a^2P_b^\epsilon}.
 \tag{1}
\]
These sums follow directly from the exact matrices of the
[Fourier contraction](research_mixed_wire_exact_contraction.md):
\[
       \Gamma B_3=\kappa T_0,\qquad
       \Gamma B_4=\kappa^2N T_1.
 \tag{2}
\]
Indeed the conditional variable \(i\) occurs in
\(\Gamma_{a i}(B_{3+\epsilon})_{i b}\), whose two triangle
supports are exactly the upper limit in (1). The denominator is
\(P_a^2P_i^{2+\epsilon}P_b^\epsilon\).

Consequently every cyclic word \(n_v=3+\epsilon_v\), with
\(m\) vertices and \(k=\sum_v\epsilon_v\), satisfies
\[
 \operatorname{tr}(A_{n_1}\cdots A_{n_m})
   =\kappa^{m+k}N^k\operatorname{tr}(T_{\epsilon_1}\cdots
                                                T_{\epsilon_m}).
 \tag{3}
\]
This is exact at every level and both parities. It sums one whole
index family of the original finite source; it does not discard
any endpoints or first-normal information.

## 2. A full-period coefficient identity for the three-vertex

For \(0\le a<N\), set
\[
                        p_a(z)=(rz;r)_a=\prod_{h=1}^a(1-r^hz).
 \tag{4}
\]
At a physical node \(z=r^i\), \(p_a(r^i)=P_{i+a}/P_i\)
when \(i+a<N\), and \(p_a(r^i)=0\) otherwise. The latter
zero is exact because the product contains \(1-r^N\).
Therefore (1) extends without an error to
\[
 L_\epsilon(a,b)=\sum_{i=0}^{N-1}
            \frac{r^{-ai}p_a(r^i)p_b(r^i)}{P_i^\epsilon}.
 \tag{5}
\]

**Theorem 1.** The original three-vertex conditional sum is
\[
                     L_0(a,b)=N[z^a]p_a(z)p_b(z).
 \tag{6}
\]
There is no root-of-unity alias in this coefficient.

*Proof.* A monomial \(z^d\) in (5) contributes
\(\sum_{i=0}^{N-1}r^{(d-a)i}\), which is \(N\) if
\(d\equiv a\pmod N\), and zero otherwise. The product has
degree \(a+b\). Since \(a<N\) and \(b<N\), the only
possible such degree in \([0,a+b]\) is \(d=a\): a degree
\(a+N\) would require \(b\ge N\), and \(a-N<0\).
This proves (6) while retaining the original physical cutoff.
\(\square\)

This provides a finite coefficient evaluation of the terminating
conditional sum. No generic infinite basic-hypergeometric summation
or continuation at the root of unity is needed.

## 3. The exact Gram form and the residual linear phase

Let
\[
 \delta_a=i^a q^{-a(a+1)/2},\qquad
 \tau_a=\delta_a^2=(-1)^a q^{-a(a+1)},\qquad P_a=\delta_a S_a,
 \tag{7}
\]
and use the ordinary positive circle inner product
\(\langle f,g\rangle=(2\pi)^{-1}\int_0^{2\pi}
\overline{f(e^{i\theta})}g(e^{i\theta})\,d\theta\).
On that circle,
\[
                     z^{-a}p_a(z)=\tau_a\overline{p_a(z)}.
 \tag{8}
\]
For example each conjugated factor is
\(1-r^{-h}z^{-1}=-r^{-h}z^{-1}(1-r^hz)\), proving (8).

**Corollary 2.** With \(D=\operatorname{diag}(S_a^2)\),
\[
 L_0(a,b)=N\tau_a\langle p_a,p_b\rangle,\qquad
 T_0(a,b)=\frac{N}{S_a^2}\langle p_a,p_b\rangle,
 \qquad DT_0=N(\langle p_a,p_b\rangle)_{a,b}>0.
 \tag{9}
\]
The last matrix is positive definite because the polynomials
\(p_0,\ldots,p_{N-1}\) have distinct degrees and nonzero leading
coefficients. Thus \(T_0\) is positive Hermitian in the exact
metric \(D\). This recovers the known single-three-operator
positivity by performing the conditional cancellation explicitly;
it is not a new common positivity statement for mixed words.

The finite binomial expansion can also be written entirely with
positive sine weights:
\[
 p_a(z)=\sum_{j=0}^a(-1)^j q^{-j(a+1)}
                   \frac{S_a}{S_jS_{a-j}}z^j,
 \tag{10}
\]
and hence
\[
 L_0(a,b)=N\tau_a
     \sum_{j=0}^{\min(a,b)}q^{j(a-b)}
       \frac{S_aS_b}{S_j^2S_{a-j}S_{b-j}}.
 \tag{11}
\]
The original quadratic oscillation in the conditional index has
become a linear Fourier phase. For \(a=b\) all terms in (11)
have exactly one common carrier and are nonzero positive weights.
For different neighbors the linear phase remains. Positivity of the
Gram form does not make its individual off-diagonal entries positive
or give a lower bound for an arbitrary mixed closing observation.

## 4. The four-vertex functional and its exact forcing

Define, for every Laurent polynomial \(f\),
\[
 \Lambda[f]=\sum_{i=0}^{N-1}\frac{f(r^i)}{P_i},\qquad
 E_N(z)=\sum_{i=0}^{N-1}\frac{z^i}{P_i}.
 \tag{12}
\]
The weights are generally complex. The identity (8) at each node
gives the exact weighted Gram form
\[
 L_1(a,b)=\tau_a\sum_{i=0}^{N-1}
        \frac{\overline{p_a(r^i)}p_b(r^i)}{P_i}.
 \tag{13}
\]
If \(p_a(z)p_b(z)=\sum_dc_dz^d\), an equivalent explicit
moment form is
\[
                   L_1(a,b)=\sum_{d=0}^{a+b}c_d E_N(r^{d-a}).
 \tag{14}
\]
Here the moment exponent is reduced modulo \(N\); unlike (6),
the nonconstant weight prevents Fourier orthogonality from
annihilating all but one coefficient.

**Theorem 3.** The functional and its moment polynomial obey
\[
 \boxed{\quad
 \Lambda[f(rz)]-\Lambda[(1-z)f(z)]=\frac{f(1)}N,
 \qquad
 E_N(rz)=(1-z)E_N(z)+\frac{z^N}{N}.
 \quad}
 \tag{15}
\]
In particular, for \(e_d=E_N(r^d)\),
\[
 e_{d+1}=(1-r^d)e_d+\frac1N,\qquad e_{d+N}=e_d,
 \quad e_1=\frac1N,
 \quad
 e_d=\frac{P_{d-1}}N\sum_{j=0}^{d-1}\frac1{P_j}\quad(1\le d\le N).
 \tag{16}
\]

*Proof.* The elementary full product is \(P_{N-1}=N\), by
evaluating \((z^N-1)/(z-1)\) at \(z=1\). In
\(\Lambda[(1-z)f(z)]\), the term \(i=0\) vanishes and
\((1-r^i)/P_i=1/P_{i-1}\) for \(i\ge1\). Shifting this
finite sum leaves exactly the \(i=N-1\) term of
\(\Lambda[f(rz)]\), namely \(f(1)/N\). This proves the first
identity, including Laurent polynomials and both level parities.
Coefficient comparison proves the second identity: all coefficients
of degree \(1,\ldots,N-1\) use the same product recurrence,
and the last coefficient is \(1/P_{N-1}=1/N\).
Evaluation on the root grid gives the recurrence in (16). Its
step at \(d=0\) gives \(e_1=1/N\), and induction gives the
displayed finite expression through \(d=N\). \(\square\)

The forcing in (15) is an actual endpoint contribution. Removing
it would already give the false conclusion \(e_1=0\). Although
the cyclic moment recurrence determines all moments uniquely
(its homogeneous multiplier contains \(1-r^0=0\)), this algebraic
uniqueness does not bound the oscillatory weighted Gram form at the
desired geometric exponential rate.

## 5. Consequence and remaining analytic problem

Equations (1)--(16) apply before any saddle approximation. They
preserve the full conditional support and every scalar in the
original cyclic trace. Three-vertex conditionals admit a positive
Gram interpretation; four-vertex conditionals retain a complex
weight and an explicit forced finite difference law. The known
[relative-operator obstruction](research_mixed_three_four_operator_obstruction.md)
prevents interpreting these formulas as simultaneous positivity
of the original three/four transfers in one metric.

The next analytic estimate must concern these exact conditional
kernels, including the nonconstant Fourier weight at four-vertices,
or their coherent products. No nonzero selected coefficient of a
full mixed word follows from (9) or the invertibility of the forced
moment recurrence. Original complete boundary vectors in an open
word also remain separate factors; they have not been replaced by
unmarked endpoint vectors in this cyclic calculation.

Run `python3 experiments/check_mixed_conditional_leg_sum.py`.
The checker compares the conditional sums, coefficient extractions,
both Gram identities, forced moments and original normalized matrix
traces in exact arithmetic at several levels. The all-level claims
follow from the finite algebraic proofs above.
