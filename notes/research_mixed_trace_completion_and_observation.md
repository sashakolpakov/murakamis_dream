# Positive cyclic completions and the ordinary boundary observation

Research deduction, 5 November 2026. The completed cyclic theorem can
be used for an ordinary closure through a finite set of positive-word
completions, provided an explicit boundary residual is small. Fourier
orthogonality gives an exact residual norm, but that norm is a
mixed-sign trace. The original matrix algebra also has unbounded
dimension as the level grows. These facts prevent replacing the
missing observation by a fixed-size trace reconstruction without
another estimate. An explicit finite-dimensional example shows that
all exact positive-word traces, all unitarily invariant norms and the
existence of exactly invariant dominant lines do not ensure a nonzero
prescribed observation.

## 1. The unchanged finite source and what is already known

At level \(N\), use the original Newton crossing \(M\), reversal
\(J\), \(A_n=JM^n\), and full ordinary vector \(v(z)\). For a fixed
positive \(3/4\) word set
\[
 W=A_{n_1}\cdots A_{n_m},\qquad
 Q_N(z,w)=v(w)v(z)^T,\qquad
 C_N(z,w)=\operatorname{tr}(WQ_N)=v(z)^TWv(w).
 \tag{1}
\]
All entries retain the repeated-root first normals. The physical
functional uses transpose, including at complex ordinary colors.
At complete real colors \(v(-2)\) is real, but \(W\) is not thereby
a positive operator.

The [full cyclic theorem](research_mixed_full_cyclic_period.md)
supplies a nonzero asymptotic for \(\operatorname{tr}(WV)\) whenever
\(V\) is another *fixed* positive \(3/4\) word. It does not give
uniformity for a completion whose length grows with \(N\).

The exact rank-one insertion and the failure of homogeneous-three
buffer tomography are already in
[marked-trace observation](research_mixed_marked_trace_observation.md).
At odd levels the
[Casimir-mark theorem](research_mixed_ordinary_boundary_casimir_mark.md)
identifies the ordinary closure with a Fejér idempotent mark; at even
levels it retains a forced resolvent observation. Carrying that mark
through a vertex gives the original endpoints again, by
[marked-vertex contraction](research_mixed_marked_vertex_contraction.md).
None of those identities is replaced here by an unmarked trace.

## 2. What exact Fourier orthogonality controls

The original identities \(M^{-1}=\overline M\) and \(M^T=JMJ\)
give, for every integer \(n\),
\[
                         A_n^*=JM^{-n}=A_{-n}.
 \tag{2}
\]
Consequently the squared Hilbert--Schmidt norm of the actual word is
the exact nonnegative scalar
\[
 \|W\|_{\rm HS}^2
 =\operatorname{tr}\left(
 A_{-n_m}\cdots A_{-n_1}A_{n_1}\cdots A_{n_m}\right).
 \tag{3}
\]
This is a mixed-sign trace, not a word covered by the positive
cyclic theorem. Positivity in (3) follows from the adjoint identity,
not from deleting the negative powers.

For an explicit Fourier version, let \(X,Z\) be the unitary shift
and clock on \(\mathbb C^N\), and \(U_{ab}=Z^aX^b\),
\(0\le a,b<N\). Their trace orthogonality gives
\[
 \begin{split}
 W&=\frac1N\sum_{a,b}\operatorname{tr}(U_{ab}^*W)U_{ab},\\
 C_N(z,w)
 &=\frac1N\sum_{a,b}
       \operatorname{tr}(U_{ab}^*W)\operatorname{tr}(U_{ab}Q_N),\\
 \sum_{a,b}|\operatorname{tr}(U_{ab}^*W)|^2
 &=N\|W\|_{\rm HS}^2 .
 \end{split}
 \tag{4}
\]
The ordinary boundary Fourier profile in the second line is
\(v(z)^TU_{ab}v(w)\); it is retained in every mode. The unmarked
trace is only the \((0,0)\) mode. Plancherel gives a norm and an
upper bound for this weighted observation, not a lower bound for
the particular complex sum.

## 3. A finite-completion criterion using only fixed positive traces

Choose a finite list \(V_1,\ldots,V_r\) of positive \(3/4\) word
matrices, possibly including the identity. The words and \(r\) are
independent of \(N\). For specified coefficients \(c_{j,N}(z,w)\),
define the exact residual
\[
 E_N=Q_N-\sum_{j=1}^r c_{j,N}V_j.
 \tag{5}
\]
There is no requirement that the coefficients be constant in \(N\).
The exact finite comparison is
\[
 \begin{split}
 C_N&=\sum_{j=1}^r c_{j,N}\operatorname{tr}(WV_j)
                                      +\operatorname{tr}(WE_N),\\
 |\operatorname{tr}(WE_N)|
 &\le
 \left[
 \operatorname{tr}\left(
 A_{-n_m}\cdots A_{-n_1}A_{n_1}\cdots A_{n_m}\right)
 \right]^{1/2}\|E_N\|_{\rm HS}.
 \end{split}
 \tag{6}
\]
The inequality is Hilbert--Schmidt Cauchy--Schwarz. A sharper direct
bound on the actual residual observation can replace its right side.

Let \(t_{j,N}\ne0\) be the explicit leading term supplied by the
cyclic theorem for \(WV_j\), including its original level scalar,
Gaussian coefficient and action, and put
\[
                         S_N=\sum_{j=1}^r c_{j,N}t_{j,N}.
 \tag{7}
\]
**Proposition 1.** Suppose, on a specified fixed ordinary-color
domain, that
\[
 \sum_j|c_{j,N}t_{j,N}|\le C|S_N|,\qquad
 |\operatorname{tr}(WE_N)|\le\varepsilon_N|S_N|,
 \qquad S_N\ne0,\quad\varepsilon_N\longrightarrow0,
 \tag{8}
\]
uniformly. Then
\[
                         C_N/S_N=1+O(N^{-1})+O(\varepsilon_N).
 \tag{9}
\]
In particular the actual ordinary observation is eventually nonzero.
If \(S_N\) has a known exponential rate, it is the rate of \(C_N\).
If the source, coefficients and nonzero model \(S_N\) are holomorphic
on that color neighborhood, the corresponding quotient convergence
and every fixed derivative of \(C_N/S_N-1\) tend to zero on smaller
neighborhoods. This is not a bound for absolute derivatives of \(C_N\).

*Proof.* There are only finitely many fixed cyclic completions, so
their relative \(O(N^{-1})\) errors have a common constant. Multiply
each by its exact coefficient and sum. The first inequality in (8)
prevents that error from becoming large relative to the combined
leading term; the second bounds the remainder in (6). This proves
(9). Holomorphy and Cauchy's formula give the final assertion.
\(\square\)

This is a concrete sufficient use of the completed cyclic result.
All phases remain in (7). It requires neither common positivity nor
a dominant eigenline, but it does require the specified residual and
combined-leading-term bounds. No such completion or residual estimate
is asserted for the ordinary vector. A trace theorem with fixed-word
constants cannot be used in this argument with an unbounded list of
level-dependent words without additional uniform estimates.

## 4. The original word algebra has no level-independent finite basis

Let \(\mathcal B_N\) be the unital complex algebra generated by the
two original matrices \(A_3,A_4\).

**Proposition 2.** At every odd prime level \(N\), the minimal
polynomial of the original crossing \(M\) has degree \(N\).
Consequently \(\dim\mathcal B_N\ge N\).

*Proof.* The original eigenvalues are
\[
 \lambda_j=\kappa(-1)^j e^{\pi i(j+j^2)/N},
                       \qquad 0\le j<N.
 \tag{10}
\]
If \(\lambda_j=\lambda_k\), reduction of the exponent modulo \(N\)
gives
\((j-k)(j+k+1)=0\pmod N\). Primality implies \(j=k\) or
\(j+k=N-1\). Conversely the reflected pair has exactly equal
eigenvalues, including its sign. Thus there are \((N+1)/2\)
distinct eigenvalues.

At every double physical node represented by
\(0\le j<(N-1)/2\), the actual multiplication block has nonzero
nilpotent part:
\[
 \frac{R'(c_j)}{R(c_j)}
     =\frac{i(N-1-2j)}{4\sin((2j+1)\pi/N)}\ne0.
 \tag{11}
\]
This is the full-normal formula in
[the arbitrary-power compiler](research_arbitrary_power_source_compilation.md),
Section 6. Each of the \((N-1)/2\) distinct double-node
eigenvalues therefore has a size-two Jordan block. The remaining
complete node is simple. The minimal polynomial has degree
\(2(N-1)/2+1=N\).

Since \(A_3\) is invertible, its inverse is a polynomial in \(A_3\)
by Cayley--Hamilton. Hence
\[
                         M=A_3^{-1}A_4\in\mathcal B_N.
 \tag{12}
\]
The independent matrices \(I,M,\ldots,M^{N-1}\) belong to that
algebra, proving the dimension bound. \(\square\)

There are only \(2^{L+1}-1\) words of length at most \(L\),
including the empty word. No fixed \(L\) can therefore span the
whole original word algebra at all levels. This rules out a
level-independent finite *algebra-basis* reconstruction of every
marked observation. It does not prove that this particular \(Q_N\)
fails every special finite completion, or exclude a small residual
on the specified \(W\). Proposition 1 deliberately asks only for
that source-specific approximation.

## 5. All cyclic characters and exact dominant lines still miss a cap

The following exact example concerns a different four-dimensional
family; it is not a counterexample among the original Newton words.
Fix \(a,b>0\), \(a\ne b\), and use
\(J_0=\operatorname{diag}(1,1,-1,-1)\). Let \(G(t)\) act by
\[
 \begin{pmatrix}\cosh t&\sinh t\\ \sinh t&\cosh t\end{pmatrix}
 \quad\hbox{on }\operatorname{span}(e_1,e_3),
 \qquad -I\quad\hbox{on }\operatorname{span}(e_2,e_4).
 \tag{13}
\]
Put \(B_{3,N}=G(Na)\), \(B_{4,N}=G(Nb)\), and let \(P\)
exchange \(e_1,e_2\) and \(e_3,e_4\). Compare these matrices with
\(\widehat B_{j,N}=P^TB_{j,N}P\).
Both families consist of symmetric real \(J_0\)-unitary matrices
of determinant one. Every word of length \(m\), with total charge
\(s=a\,\#3+b\,\#4\), has in both families exactly the trace
\[
                         2\cosh(Ns)+2(-1)^m>0.
 \tag{14}
\]
Thus all positive \(3/4\)-word traces agree, not merely their leading
asymptotics. Their unitarily invariant norms also agree.
Every word has a simple dominant eigenvalue \(e^{Ns}\); the
dominant line in either family is exactly invariant under both
generators. There is no quasimode residual.

Nevertheless take the same real unit boundary vector in both families,
\[
 C=\cosh(Na),\qquad
               v_N=\frac{e_1+\sqrt C\,e_2}{\sqrt{1+C}}.
 \tag{15}
\]
It satisfies \(v_N^TJ_0v_N=1\), but the length-one observations are
\[
                  v_N^TB_{3,N}v_N=0,\qquad
                  v_N^T\widehat B_{3,N}v_N=C-1>0.
 \tag{16}
\]
Indeed their numerators are \(C-C\) and \(C^2-1\).
The overlap with the first family's dominant unit vector
\((e_1+e_3)/\sqrt2\) is \(1/\sqrt{2(1+C)}\), exponentially
small. In the conjugate family the overlap tends to \(1/\sqrt2\).

This example rules out inferring a specified cap observation from
all cyclic characters, Plancherel norms and existence of dominant
almost-invariant vectors alone, even with the extra properties just
listed. It does not satisfy every original crossing relation and
does not contradict the completed cyclic theorem. The actual
[original quasimode examples](research_original_almost_invariance_and_observation.md)
already exhibit the overlap scale problem on the genuine source.
The new completion criterion (6)--(8) states the additional,
quantitative observation information that a trace-based proof could
supply without revisiting every open contour.
