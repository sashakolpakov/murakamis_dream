# Quantitative transport of the actual three-crossing source through its next crossing

Research note, 3 November 2026.

The factorial approximation to the original three-crossing column can
be transported through its next turn and crossing. The conclusion
requires an exact scalar taken from the original finite sum. With that
choice the absolute input remainder is polynomial in the level. A
specified coefficient of the actual output has an exponential lower
bound strictly larger than the exponential norm of the crossing
matrix. Consequently the transported remainder is exponentially
small relative to that coefficient, and therefore relative to the
whole output norm.

This is a statement about the next original column
\(MJ M^3\mathbf e_0\), at both level parities. It does not yet
control the remaining two crossings and free-boundary evaluation in
\(JM^3JM^3\mathbf e_0\). Complex conjugation gives the corresponding
negative-power statement.

## 1. An exact scalar makes the entire input remainder polynomial

Use the original full Newton algebra, including its double-root
normals:
\[
 \begin{gathered}
 N\ge2,\quad D=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^D,\quad \kappa=e^{\pi iD^2/(2N)},\\
 d_j=4\sin^2(\pi j/N),\qquad
 S_j=\prod_{r=1}^j2\sin(\pi r/N),\qquad S_0=1,\\
 c_j=qQ^j+q^{-1}Q^{-j},\qquad
 e_j(z)=S_j^{-2}\prod_{r=0}^{j-1}(c_r-z),\qquad
 P_N(z)=2T_N(z/2)+2 .
 \end{gathered}                                                   \tag{1}
\]
The coordinate vector \(\mathbf e_0\) represents the unit. The
crossing and turn are the original matrices
\[
 M_{ij}=\kappa(-1)^i q^{i(j+1)}
               \frac{S_i}{S_jS_{i-j}}\quad(0\le j\le i<N),
 \qquad (Jv)_j=v_{D-j}.                                           \tag{2}
\]
Set
\[
 \alpha=M^3\mathbf e_0,\qquad
 h_j=q^{j(j+2)}S_j^2,\qquad
 A_j=\sum_{\ell=0}^j
             \frac{(-1)^\ell q^{-\ell(\ell-1)}}{S_\ell^2}.
                                                                    \tag{3}
\]
The [full coefficient formula](research_three_crossing_full_coefficient_profile.md),
equations (3)--(6), gives exactly
\[
 \alpha_j=\kappa^3h_j A_j,\qquad
 A_D=N^{-1/2}\omega_N+O(N^{-3/2}),\qquad
 \omega_N=e^{i\pi(1/4+1/(4N)-N/12)}.                               \tag{4}
\]
The error in (4) holds at both parities.

Choose any maximizer \(j_*\) of \(S_j^2\) on
\(\lceil N/2\rceil\le j\le D\), and define
\[
                  A_N=A_{j_*},\qquad
                  \delta=\alpha-\kappa^3 A_Nh.                    \tag{5}
\]
This index interval is nonempty for every \(N\ge2\), and
\(j_*/N\longrightarrow5/6\). Plateaus in the maximum are harmless.

**Lemma 1.** The exact scalar in (5) satisfies
\[
 A_N=N^{-1/2}\omega_N(1+O(N^{-1})),\qquad
 \max_{0\le j<N}|\delta_j|=O(N),\qquad
 \|\delta\|_2=O(N^{3/2}).                                         \tag{6}
\]
In particular \(A_N\ne0\) for all sufficiently large levels.

*Proof.* The first assertion follows either from (4) and the reflected
factorial tail, or from equation (14) of the cited full coefficient
profile on a fixed compact interval about \(5/6\).

On the upper half, \(S_j^2\) increases to its maximum and then
decreases: its consecutive ratio is \(d_{j+1}\), which decreases
there through one. For every index \(\ell\) strictly between \(j\)
and \(j_*\), and also at the endpoint included in the difference of
the sums in (3), one has \(S_\ell^2\ge S_j^2\). Hence
\[
 \begin{split}
 |\delta_j|
 &=S_j^2|A_j-A_{j_*}|\\
 &\le
 S_j^2\sum_{\ell=\min(j,j_*)+1}^{\max(j,j_*)}S_\ell^{-2}
 \le N\qquad(j\ge\lceil N/2\rceil).                              \tag{7}
 \end{split}
\]
On the lower half, the
[original distinct-node coefficient bound](research_original_low_color_bound.md),
equation (15), gives \(|\alpha_j|\le\csc(\pi/(2N))\le N\).
The sine factorial first decreases and then increases on this half;
its endpoint values show \(S_j^2\le2N\). This also follows from the
factorial estimates in the full coefficient profile. Thus
\[
 |\delta_j|\le N+2N|A_N|=O(N)
       \qquad\left(j\le\left\lfloor\frac{N-1}{2}\right\rfloor\right).
\]
These two ranges cover every index at both parities. Summing the
squared bound proves (6). \(\square\)

Replacing \(A_N\) by only its leading term
\(N^{-1/2}\omega_N\) would not give the polynomial absolute
remainder in (6). The exponentially large vector \(h\) multiplies
that scalar error. The exact finite sum in (5) is therefore part of
the theorem.

## 2. The original next-step equation and both endpoint data

Let
\[
 \gamma=MJ\alpha,\qquad
 (\mathsf Cv)_j=c_jv_j-d_jv_{j-1},\qquad
 \mathsf X=\operatorname{diag}(Q^j),\qquad
 L=J\mathsf CJ=\mathsf C^T.                                      \tag{8}
\]
Missing endpoint terms in these finite matrices are zero. The
primitive coordinate
\[
 K=-q^{-1}\mathsf X^{-1}+(I-\mathsf X^{-1})E
                                                                    \tag{9}
\]
is lower bidiagonal; the cyclic shift \(E\mathbf e_j=\mathbf
e_{j+1\bmod N}\) has a zero wrap coefficient in (9).

**Lemma 2.** The actual column \(\gamma\) satisfies
\[
 \boxed{\quad
 q^{-1}d_{j+1}\gamma_{j+1}
 +a_j\gamma_j+q(1-Q^{-j})\gamma_{j-1}
       =\kappa^2\mathbf1_{\{j=0\}},\qquad
 a_j=3-(1+Q^{-1})Q^{-j}.
 \quad}                                                         \tag{10}
\]
The first term is absent at \(j=D\), and the last is absent at
\(j=0\). Its original endpoint values are
\[
 \gamma_0=\kappa\alpha_D,\qquad \gamma_D=N,                         \tag{11}
\]
where
\[
 \alpha_D=\kappa^3(-1)^N
 e^{i\pi/4-3\pi i/(4N)-\pi iN/12}
                N^{3/2}+O(N^{1/2}).                              \tag{12}
\]
In particular \(|\gamma_0|=N^{3/2}(1+O(N^{-1}))\).

*Proof.* The source equation, with its actual forcing, is
\[
 (\mathsf C-q\mathsf X)\alpha
                  =\kappa^2q^{-1}M\mathbf e_0.                   \tag{13}
\]
The original turn identity \(JM\mathbf e_0=M^{-1}\mathbf e_0\)
gives \(MJ M\mathbf e_0=\mathbf e_0\). The
[primitive-coordinate conjugations](research_quantum_cap_primitive_source.md),
equation (9), give
\[
 (MJ)(\mathsf C-q\mathsf X)(MJ)^{-1}
       =MLM^{-1}+K.
                                                                    \tag{14}
\]
Indeed \(J\mathsf XJ=Q^{-1}\mathsf X^{-1}\) and
\(M\mathsf X^{-1}M^{-1}=-qK\). Thus
\[
                    (MLM^{-1}+K)\gamma
                            =\kappa^2q^{-1}\mathbf e_0.           \tag{15}
\]
For an explicit entry check, write \(L_1=M^{-1}LM\). Its diagonal
is \(4qQ^j-q(1+Q)Q^{2j}\), and its two entries across the edge
\(j,j+1\) are \(-(1-Q^{j+1})^2\). The exact trace-algebra
identity \(MLM^{-1}=JL_1J\), as recorded in
[crossing transport](research_current_free_aw_crossing_transport.md),
then gives (10) after multiplying row \(j\) of (15) by
\(qQ^j\). In particular the lower entry becomes
\[
 qQ^j\{-(1-Q^{-j})^2+(1-Q^{-j})\}
                         =q(1-Q^{-j}),
 \]
and the upper entry becomes \(q^{-1}d_{j+1}\).
This calculation includes both finite endpoints.

The first identity in (11) is row zero of (2). For the second,
the original Frobenius pairing and turn give
\[
 \gamma_D=\phi_N(R\,T(R^3))
          =\phi_N(T(R)\,R^3)
          =\phi_N(R^2)=N,
 \]
using \(T(R)=R^{-1}\) and the exact two-crossing closing value.
Finally (12) is the full Gaussian endpoint formula (5) in the
coefficient profile. It is an original normal trace, not a value
assigned to a homogeneous recurrence. \(\square\)

For comparison with local transfer estimates, the nonsingular
normalization
\[
 y_j=(-q)^{-j}S_j^2\gamma_j/\gamma_0
                                                                    \tag{16}
\]
obeys
\[
 \begin{split}
 y_0&=1,\qquad y_1=2-Q^{-1}-\kappa^2/\gamma_0,\\
 y_{j+1}
   &=[3-(1+Q^{-1})Q^{-j}]y_j
                 -d_j(1-Q^{-j})y_{j-1}\quad(1\le j<D).
 \end{split}                                                       \tag{17}
\]
The estimate below uses (10) directly; no spectral dominance
assumption is needed.

## 3. A specified original coefficient has a strict exponential lower bound

Put
\[
 \mathcal J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad
 t(x)=2\sin\pi x,\qquad m_N=\lfloor N/4\rfloor,
                                                                    \tag{18}
\]
and define the convergent integral
\[
 \mathcal L=
 \int_0^{1/4}
 \log\frac{\sqrt{1+6t(x)^2}-t(x)}{t(x)^2}\,dx .
                                                                    \tag{19}
\]

**Theorem 1.** For all sufficiently large \(N\), every
\(\gamma_j\), \(0\le j\le m_N\), is nonzero, and
\[
 |\gamma_{j+1}|\ge|\gamma_j|\quad(0\le j<m_N).
                                                                    \tag{20}
\]
More precisely,
\[
 \liminf_{N\to\infty}\frac1N\log|\gamma_{m_N}|
                        \ge\mathcal L>\frac13.                   \tag{21}
\]
The limit inferior is over all integer levels.

*Proof.* Let \(\theta=\pi/N\) and \(t_j=2\sin(j\theta)\).
For \(0\le j\le N/4\), one has \(0\le t_j\le\sqrt2\) and
\[
 \big||a_j|-\sqrt{1+6t_j^2}\big|\le2\theta,\qquad
                  d_{j+1}-d_j\le4\theta.                          \tag{22}
\]
The first bound follows by comparison with \(3-2Q^{-j}\).
For \(0\le t\le\sqrt2\),
\[
 \begin{split}
 \sqrt{1+6t^2}-t-t^2
 &=\frac{1+5t^2-2t^3-t^4}
           {\sqrt{1+6t^2}+t+t^2}\\
 &\ge\frac1{\sqrt{13}+\sqrt2+2}=:\Delta>0.                         \tag{23}
 \end{split}
\]
Here \(2t^3+t^4\le(2\sqrt2+2)t^2<5t^2\).
Consequently, for sufficiently large \(N\),
\[
                   |a_j|-t_j-d_{j+1}\ge\Delta-6\pi/N>0.           \tag{24}
\]
The first row of (10) and (12) give
\[
 \left|\frac{\gamma_1}{\gamma_0}\right|
   \ge \frac{|a_0|-|\gamma_0|^{-1}}{d_1}>1.                        \tag{25}
\]
If \(|\gamma_j|\ge|\gamma_{j-1}|>0\), the reverse triangle
inequality in the homogeneous row \(j\) gives
\[
 \left|\frac{\gamma_{j+1}}{\gamma_j}\right|
       \ge\frac{|a_j|-t_j}{d_{j+1}}>1.                            \tag{26}
\]
This proves (20) without replacing the oscillatory recurrence by
an equality for absolute values. Multiplication of the inequalities
also gives the finite bound
\[
 |\gamma_{m_N}|\ge
 \frac{|\gamma_0|}{S_{m_N}^2}
       (|a_0|-|\gamma_0|^{-1})
       \prod_{j=1}^{m_N-1}(|a_j|-t_j).                            \tag{27}
\]
The factors in the product have a fixed positive lower bound.
Their logarithms therefore have the ordinary Riemann-sum limit
specified in (19). The uniform sine-factorial estimate
\(\log S_j=N\mathcal J(j/N)+O(\log N)\), including endpoints,
handles the denominator in (27); (12) handles its initial factor.
This proves the first inequality in (21).

Here is an elementary strict lower bound for the integral. Write
\(G=\sum_{r\ge0}(-1)^r/(2r+1)^2\) for Catalan's constant and
\(A=\sqrt6-1\). For every \(t\ge0\),
\[
 \sqrt{1+6t^2}-t\ge At,\qquad
 \sqrt{1+6t^2}-t\ge\sqrt{5/6}.                                   \tag{28}
\]
The second inequality follows by minimizing the left side; the
minimum occurs at \(t=1/\sqrt{30}\).
Use the first inequality on \(0\le x\le1/4\) and the second
instead on \(0\le x\le1/12\). Since
\(\mathcal J(1/4)=-G/(2\pi)\) and
\(\mathcal J(1/12)\le(\log(\pi/6)-1)/12\), this yields
\[
 \mathcal L\ge L_0:=
 \frac{\log(\sqrt6-1)}6+\frac{\log(5/6)}{24}
       +\frac G{2\pi}+\frac{1-\log(\pi/6)}{12}
                  >\frac{44449}{132000}>\frac13.                 \tag{29}
\]
For completeness, the strict rational bound follows from
\[
 \begin{gathered}
 \log(\sqrt6-1)>37/100,\qquad
 \tfrac12\log(5/6)>-23/250,\\
 G>183/200,\qquad
 \pi<22/7,\qquad -\log(\pi/6)>323/500 .
 \end{gathered}                                                    \tag{30}
\]
These small bounds require no numerical integration. The first
sixteen terms of the alternating Catalan series give its stated
lower bound. For the logarithms, use
\(\sqrt6-1>1449/1000\),
\(e^{37/100}<1448/1000\),
\(e^{323/500}<21/11\), and
\(e^{23/125}>6/5\).
The two exponential upper bounds follow by summing through degree
eight and bounding the remaining positive series by
\[
 \frac{x^9}{9!}\frac1{1-x/10};
 \]
the last lower bound follows from its cubic partial sum.
Substitution in (29) gives exactly \(44449/132000\).
The identity for \(\mathcal J(1/4)\) follows by integrating the
Abel-regularized Fourier series for \(\log(2\sin\pi x)\).
\(\square\)

## 4. The crossing operator has a smaller exponential norm

**Lemma 3.** For the original matrix (2),
\[
 \lim_{N\to\infty}\frac1N\log\|M\|_2
      =c:=2\mathcal J(5/6)
      <\frac{286009121}{861616000}<\frac13.                        \tag{31}
\]

*Proof.* The uniform sine-factorial estimate gives
\[
 \log|M_{ij}|=
 N\{\mathcal J(i/N)-\mathcal J(j/N)
                  -\mathcal J((i-j)/N)\}+O(\log N),               \tag{32}
\]
uniformly over the entire triangular index set.
For \(0<x<1\), the derivative in \(y\) of
\(\mathcal J(x)-\mathcal J(y)-\mathcal J(x-y)\) is
\(\log(\sin(\pi(x-y))/\sin(\pi y))\).
The sine subtraction formula makes this positive for \(y<x/2\)
and negative for \(y>x/2\).
The maximum for a fixed \(x\) is therefore at \(y=x/2\).
The derivative of the resulting function of \(x\) is
\(\log(2\cos(\pi x/2))\), so the global maximum is
\(-3\mathcal J(1/3)\), attained at \(x=2/3,y=1/3\).
The double-angle identity and
\(\mathcal J(1-x)=-\mathcal J(x)\) give
\(-3\mathcal J(1/3)=2\mathcal J(5/6)\).
The largest-entry lower bound for the operator norm and
\(\|M\|_2\le N\max_{ij}|M_{ij}|\) now prove its stated limit.

For the explicit strict upper bound, the same integrated Fourier
series gives
\[
 c=\frac{\sqrt3}{2\pi}
 \sum_{n=0}^{\infty}
 \left\{\frac1{(6n+1)^2}+\frac1{(6n+2)^2}
        -\frac1{(6n+4)^2}-\frac1{(6n+5)^2}\right\}.                \tag{33}
\]
The first bracket is \(459/400\). Every later bracket is at
most \(12/(6n+1)^3\), by the mean value bound on each of the
two reciprocal-square differences. Monotone integral comparison
therefore bounds the full sum by
\[
 \frac{459}{400}+\frac{12}{343}+\frac1{49}
                            =\frac{165037}{137200}.               \tag{34}
\]
Finally \(\sqrt3<1733/1000\) and \(\pi>157/50\) give precisely
the rational bound in (31). \(\square\)

## 5. Exponentially accurate transport through the next original crossing

**Theorem 2.** Retain the exact scalar \(A_N\) from (5).
Then
\[
 \limsup_{N\to\infty}\frac1N
 \log\frac{\|\gamma-\kappa^3A_NMJh\|_2}
                    {|\gamma_{m_N}|}
                          \le c-\mathcal L<0.                    \tag{35}
\]
If the numerator is zero, its logarithm is understood as
\(-\infty\). In particular, at all sufficiently large levels,
\[
 \frac{\|\gamma-\kappa^3A_NMJh\|_2}{|\gamma_{m_N}|}
                 \le e^{-N/250}.                                \tag{36}
\]
The same estimate holds with the larger denominator
\(\|\gamma\|_2\). The specified actual Newton coefficient is
nonzero and satisfies
\[
 \gamma_{m_N}=\kappa^3A_N(MJh)_{m_N}
                                     (1+O(e^{-N/250})).           \tag{37}
\]

*Proof.* Equations (5)--(6), the unitarity of the reversal \(J\),
and Lemma 3 give
\[
 \|\gamma-\kappa^3A_NMJh\|_2
     =\|MJ\delta\|_2
     \le\|M\|_2\,O(N^{3/2}),\qquad
 \limsup\frac1N\log\|MJ\delta\|_2\le c.
                                                                    \tag{38}
\]
Subtract the lower bound (21). The rational estimates in
(29) and (31) obey
\[
 \frac{44449}{132000}-\frac{286009121}{861616000}
                                                  >\frac1{250}.
 \]
This proves (35)--(36). Since an individual coefficient error
is bounded by the Euclidean error and \(\gamma_{m_N}\ne0\),
(37) follows, with a harmless adjustment of its constant.
\(\square\)

For the negative source, \(M^{-1}=\overline M\) and \(J\)
is real. Thus \(\gamma_-=M^{-1}JM^{-3}\mathbf e_0
=\overline\gamma\). Conjugating the complete statements gives
the identical estimates, with \(\overline{A_N}\),
\(\overline h\), and the original conjugate scalar. No parity
subsequence is used.

The estimate retains the original current in (13). It shows that
this current's exact contribution to the next column is smaller
than a nonzero specified coefficient after the exact scalar has
been extracted. It does not show that the current remains smaller
after arbitrary further operators or free-boundary tests.
Indeed the actual same-sign pendant vector is
\[
 JM^3JM^3\mathbf e_0=JM^2\gamma,
 \]
and its ordinary evaluation near \(w=-2\) is an additional
operation. Neither its marked overlap nor its exponential rate
is supplied by (35).

## 6. Verification scope

The original matrix formula (2), both endpoint identities (11),
and every row of (10) can be checked independently by forming
\(M^3\mathbf e_0\) and then applying the literal matrices \(J,M\).
The focused
[original-matrix checker](../experiments/check_three_crossing_next_crossing.py)
and its
[140-digit result](../repro/results/research-three-crossing-next-crossing.json)
record 4,088 numerical identities and two exact symbolic checks,
with maximum relative residual \(2.151\cdot10^{-82}\).
They include both signs and parities, both endpoint recurrences,
and the exact transported remainder decomposition.
The proof of (35) is the finite coefficient comparison
(24)--(27), the polynomial exact-scalar remainder (6), and the
entropy maximization (32). Numerical transfer trajectories and
the choice of a largest classical eigenvalue are not inputs.

The [local dominant-profile analysis](research_three_crossing_next_crossing_dominant_profile.md)
uses the smooth recurrence (17) for a sharper description on
fixed subintervals. The elementary estimate here is independent
of that refinement.
