# Newton evaluation on the real boundary period

Research proof, 3 November 2026.

The Newton evaluation vector has its largest exponential growth at the
complete boundary value. This comparison holds for every original
color, including the upper half of the color range and both level
parities. It gives an upper bound for the adjacent three-crossing
source on the far part of its real boundary period. It also supplies
a smaller color cutoff for the remaining intermediate angles.

These are upper bounds. Their use does not require a lower bound for
the signed source, a contributing saddle, or positivity of its
coefficients.

## 1. The real Newton entropy

Let \(N\ge2\), \(D=N-1\), and
\[
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\qquad
 c_\nu=2\cos((2\nu+1)\pi/N),\qquad
 e_j(w)=S_j^{-2}\prod_{\nu<j}(c_\nu-w).
 \tag{1}
\]
The ordinary boundary variable is \(w=-2\cos u\), with
\(-\pi\le u\le\pi\). Write
\[
 J(y)=\int_0^y\log(2\sin\pi t)\,dt\quad(0\le y\le1),
 \qquad
 L(t)=\int_0^t\log|2\cos\pi s|\,ds\quad(t\in\mathbb R).
 \tag{2}
\]
The second integral defines the continuous odd, one-periodic
primitive; the logarithmic singularities are integrable.
For \(a=|u|/(2\pi)\), set
\[
 V_u(y)=L(y+a)+L(y-a)-2J(y),\qquad 0\le y\le1.
 \tag{3}
\]
Indeed \(L\) is odd, and the elementary product of two cosines gives
\[
 L(y+a)+L(y-a)
   =\int_0^y\log|2\cos(2\pi t)+2\cos u|\,dt.
 \tag{4}
\]

**Lemma 1.** Uniformly over all real \(u\), all \(0\le j<N\), and
both parities,
\[
 |e_j(-2\cos u)|\le C N^A\exp\{N V_u(j/N)\},
 \tag{5}
\]
with constants independent of \(u,j,N\).

**Proof.** For \(f(t)=\log|2\sin\pi t|\), the midpoint sum on any
initial segment of a mesh of size \(1/N\) satisfies
\[
 \sum_{\nu=0}^{j-1}f((\nu+1/2)/N+\theta)
 \le N\int_0^{j/N}f(t+\theta)\,dt+C\log N,
 \tag{6}
\]
uniformly in the real shift \(\theta\). Here and below a zero
sample factor makes the left side \(-\infty\).

To prove (6), remove the bounded number of mesh cells within
distance \(2/N\) of an integer zero of the sine. On the remaining
cells, \(|f'(t)|\) is at most a constant divided by the distance
to the nearest zero. The midpoint error on a cell at distance
comparable to \(m/N\) is consequently \(O(1/m)\). Summing these
errors gives \(O(\log N)\). On each removed cell, the sampled
value is at most \(-\log N+C\), whereas the integral average is
at least \(-\log N-C\), by rescaling its integrable logarithmic
singularity. Its upper error is therefore bounded by a constant,
even if a sample is arbitrarily close to the zero.

Apply (6) to the two shifted cosine factors in
\[
 c_\nu+2\cos u
 =4\cos\!\left(\pi\frac{\nu+1/2}{N}+\frac u2\right)
     \cos\!\left(\pi\frac{\nu+1/2}{N}-\frac u2\right).
 \tag{7}
\]
The already proved uniform sine-factorial estimate
\(\log S_j=NJ(j/N)+O(\log N)\) controls the denominator in
(1). Equations (3)--(4) then give (5). \(\square\)

## 2. Monotonicity and the exact maximum

**Lemma 2.** For \(0\le y\le1/2\), \(V_u(y)\) decreases as
\(|u|\) increases from zero to \(\pi\), and
\[
 0\le V_u(y)\le V_0(y),\qquad
 V_u(1-y)=-V_u(y).
 \tag{8}
\]
For \(0\le u<\pi\), its unique maximum on \(0\le y\le1\)
occurs at
\[
 y_u=\frac1{2\pi}\arccos\!\left(\sin^2\frac u2\right)
                      \in(0,1/4].
 \tag{9}
\]

**Proof.** At regular points with \(0<y,a<1/2\),
\[
 \frac{\partial V}{\partial a}
   =\log\left|\frac{\cos\pi(y+a)}{\cos\pi(y-a)}\right|<0,
 \tag{10}
\]
because
\[
 \cos^2\pi(y-a)-\cos^2\pi(y+a)
                          =\sin(2\pi y)\sin(2\pi a)>0.
 \tag{11}
\]
The denominator in (10) is positive in this open rectangle.
The possible numerator zero gives an integrable negative
logarithm, so the strict monotonicity extends through it.
At \(u=\pi\), (4) is \(2J(y)\), and \(V_\pi(y)=0\).

The cosine integral in (4) is zero over a half period:
\(L(1/2+a)+L(1/2-a)=0\). This follows directly by writing
the two integrals on opposite sides of \(1/2\) as \(J(a)\)
and \(-J(a)\). Reflection about \(1/2\), together with
\(J(1-y)=-J(y)\), now gives the second part of (8).
In particular the upper half has nonpositive entropy.

For \(0<y<1/2\), put \(t=\cos(2\pi y)\) and \(d=\cos u\).
The derivative in \(y\) is
\[
 \partial_y V_u(y)=\log\frac{|t+d|}{1-t}.
 \tag{12}
\]
For \(d>-1\), the quotient is greater than one exactly when
\(t>(1-d)/2\). It is less than one on the rest of the interval,
apart from its integrable zero. This proves (9) and uniqueness.
The endpoint \(u=\pi\) has \(V_\pi\equiv0\). \(\square\)

Let
\[
 m(u)=\max_{0\le y\le1}V_u(y),\qquad
 b_2=m(0)=\frac{2G}{\pi},\qquad
 G=\sum_{n\ge0}\frac{(-1)^n}{(2n+1)^2}.
 \tag{13}
\]
The value of \(b_2\) is the same original two-crossing exponent
as in the
[global preparation-error theorem](research_three_crossing_global_preparation_error.md).

**Lemma 3.** For \(0<u<\pi\),
\[
 m'(u)=-\frac1\pi\operatorname{arsinh}(\sin(u/2)).
 \tag{14}
\]
In particular
\[
 m(0)-m(u)\ge\frac{1-\cos u}{2\pi},
 \qquad
 m(0)-m(\pi/3)\ge\frac{128-63\sqrt3}{72\pi}.
 \tag{15}
\]

**Proof.** At (9),
\[
 \tan(\pi y_u)=\frac{\cos(u/2)}{\sqrt{1+\sin^2(u/2)}}.
 \]
The ratio in (10) is therefore
\[
 \frac{\sqrt{1+s^2}-s}{\sqrt{1+s^2}+s}
                  =e^{-2\operatorname{arsinh}s},
 \qquad s=\sin(u/2).
 \]
The envelope derivative and \(da/du=1/(2\pi)\) give (14).
Since
\(\operatorname{arsinh}s\ge s/\sqrt{1+s^2}\ge s\sqrt{1-s^2}\)
for \(0\le s\le1\), integration proves the first bound in (15).
For the sharper second bound, use
\(\operatorname{arsinh}s\ge s-s^3/6\), obtained by integrating
\((1+t^2)^{-1/2}\ge1-t^2/2\). Its integral from zero to \(u\)
is
\[
 m(0)-m(u)\ge
 \frac{16-15c-c^3}{9\pi},\qquad c=\cos(u/2).
 \tag{16}
\]
Substitute \(c=\sqrt3/2\). \(\square\)

## 3. The far part of the original boundary source

Use the original adjacent source
\[
 F_N(w)=\mathbf e(w)^TJM^2\gamma_N,\qquad
 \gamma_N=MJM^3\mathbf e_0 .
 \tag{17}
\]
The full next-column theorem gives exponential rate
\(A_*<4531/10000\) for \(\|\gamma_N\|_2\), while
\(\|M^2\|_2\) has rate \(b_2<729/1250\).
Lemma 1 therefore yields the uniform upper rate
\[
 \limsup_{N\to\infty}\frac1N
       \log|F_N(-2\cos u)|\le m(u)+b_2+A_* .
 \tag{18}
\]
The upper bounds can be written with fixed polynomial prefactors;
the strict rational bounds below also absorb any subexponential
error in the quoted norm limits.

**Proposition 4.** Uniformly for \(\pi/3\le|u|\le\pi\),
\[
 |F_N(-2\cos u)|
 \le C N^A
      \exp\left\{\frac{24331441}{15840000}N\right\},
 \qquad
 \frac{24331441}{15840000}<\frac{1537}{1000}.
 \tag{19}
\]
Every fixed ordinary \(w\)-derivative obeys the same exponential
bound on the real interval \(-1\le w\le2\).

**Proof.** The exact constant bounds are
\[
 b_2<\frac{729}{1250},\quad
 A_*<\frac{4531}{10000},\quad
 m(0)-m(\pi/3)>
       \frac{1321439}{15840000}.
 \tag{20}
\]
The last follows from (15), \(\sqrt3<17321/10000\), and
\(\pi<22/7\). The first uses 65 terms of the alternating
Catalan series and \(\pi>31415/10000\); the second is already
enclosed by the real-tail certificate. Their exact combination
is (19). Markov's inequality on the fixed interval \([-1,2]\)
costs only a power of \(N\) for each derivative, because the
ordinary polynomial \(F_N\) has degree at most \(N-1\).
The inequality applies to complex coefficients as well: at the
point being estimated, rotate the derivative to the positive real
axis and apply the real polynomial inequality to that real part.
\(\square\)

The
[geometric action certificate](../repro/results/research-three-crossing-closing-action.json)
gives \(\Re W(0)>1537/1000\). Thus (19) is a strict
off-center gap at the actual geometric rate, independently of
whether that rate has already been proved to contribute.

The exact preparation error is also small on the entire real
period. Lemmas 1--2 give \(\|\mathbf e(w)\|_2\le
\operatorname{poly}(N)e^{Nb_2}\) uniformly for \(-2\le w\le2\).
Hence the original decomposition
\(\alpha=\kappa^3A_Nh+\delta_N\) satisfies
\[
 |\mathbf e(w)^TJM^3J\delta_N|
 \le \|\mathbf e(w)\|_2\|M^2\|_2\|M\|_2\|\delta_N\|_2
 \le \operatorname{poly}(N)e^{N(2b_2+c)},
 \qquad 2b_2+c<\frac32,
 \tag{21}
\]
with \(c\) the previously proved one-crossing norm exponent.
Coordinate projections do not change this estimate. Markov's
inequality retains all fixed ordinary derivatives on the same
real interval.

## 4. A smaller Newton cutoff for intermediate angles

For \(u\ge3/5\) and \(y\ge13/40\), Lemma 2 implies
\[
 V_u(y)\le V_{3/5}(13/40)<\frac{249}{500}.
 \tag{22}
\]
For \(y\le1/2\), this uses monotonicity in \(u\) and the fact
that \(V_u\) decreases in \(y\) beyond its maximum \(y_u\le1/4\).
For \(y\ge1/2\), it follows from \(V_u(y)\le0\).

Consequently the part of the original source (17) with
\(i/N\ge13/40\) has uniform upper rate, for \(3/5\le|u|\le\pi\),
\[
 \frac{249}{500}+\frac{729}{1250}
          +\frac{4531}{10000}
                    =\frac{15343}{10000}<\frac{1537}{1000}.
 \tag{23}
\]
This is a projection of the actual Newton row followed by
\(JM^2\gamma_N\); it does not estimate the summands of
\(\gamma_N\) separately. Replacing \(\gamma_N\) by its preparation
costs only (21). All fixed ordinary derivatives have the same
rate by Markov's inequality on the corresponding fixed real
\(w\) interval.

The inequality in (22) is certified by
[the exact real-period checker](../experiments/verify_three_crossing_real_period_constants.py)
and its
[saved result](../repro/results/research-three-crossing-real-period-constants.json).
It evaluates
\[
 V_{3/5}(13/40)=
 -J\!\left(\frac12-\frac{13}{40}+\frac{3}{10\pi}\right)
 -J\!\left(\frac12-\frac{13}{40}-\frac{3}{10\pi}\right)
 -2J(13/40)
 \tag{24}
\]
by the same outward dilogarithm series as the real-tail certificate.
All three arguments lie strictly between zero and one. The
checker also verifies every rational comparison in (20), (19),
and (23), and retains the input certificate and dependency hashes.

This cutoff keeps the shifted Newton factorials in their original
bulk strips up to \(u=\pi/3\):
\[
 \frac12-\frac{13}{40}-\frac{u}{2\pi}\ge\frac1{120}>0.
 \tag{25}
\]
The resulting contour has a new upper \(y\) face at \(13/40\).
Its mixed-current bounds are proved separately in the
[whole-period source theorem](research_three_crossing_whole_period_source.md).
Equation (23) estimates the omitted real lattice sum; it is
not itself an estimate for that complex face.

## 5. A moving cutoff for other original sources

The real cutoff mechanism does not depend on the three-crossing
core. The first shifted factorial reaches its boundary at
\[
 y_b(u)=\frac{\pi-u}{2\pi},\qquad 0\le u\le\pi .
 \tag{26}
\]
At that boundary, (3) gives
\[
 V_u(y_b(u))=J(2y_b(u))-2J(y_b(u))
                  \le -3J(1/3)=c,
 \qquad c=2J(5/6).
 \tag{27}
\]
To prove the inequality, differentiate \(J(2y)-2J(y)\):
its derivative is \(2\log(2\cos\pi y)\), so its maximum
on \([0,1/2]\) occurs at \(y=1/3\).
For the equality with \(c\), the sine duplication formula gives
\[
 J(1/3)=2J(1/6)+2L(1/6)
       =2J(1/6)-2J(1/3).
 \]
Thus \(-3J(1/3)=-2J(1/6)=2J(5/6)\).

Moreover \(y_b(u)>y_u\) for \(u<\pi\). Indeed the two
cosines to compare are \(-\cos u\) and
\((1-\cos u)/2\), and the former is strictly smaller.
The entropy therefore decreases beyond \(y_b(u)\).

**Proposition 5.** Suppose another original boundary source has
the form
\[
 f_N(w)=\mathbf e(w)^Tv_N,\qquad
       \|v_N\|_2\le\exp\{N(U+o(1))\},
 \tag{28}
\]
and a target rate satisfies \(M>U+c\).
On every compact angular interval \(I\subset(0,\pi)\), there
are finitely many subintervals and a fixed upper Newton cutoff
on each subinterval such that:

1. the cutoff lies strictly below \(y_b(u)\), so the shifted
   factorial real parts have a fixed positive margin;
2. the entire omitted real Newton row has source rate strictly
   below \(M\).

Near \(u=\pi\), the whole source already has rate below \(M\).

**Proof.** At the moving cutoff (26), Lemma 1 and (27) bound the
omitted row's entropy by \(c\). Choose
\(\eta>0\) with \(U+c+2\eta<M\).
Continuity of \(V_u(y)\), and the strict inequality
\(y_b(u)>y_u\), are uniform on the compact set \(I\).
The cutoff may consequently be lowered by a fixed small
amount while keeping it above \(y_u\) and retaining an
omitted-row entropy at most \(c+\eta\).
Uniform continuity then allows a fixed cutoff on a
neighborhood of each angle. A finite subcover gives the
stated finite list and retains a positive factorial margin.

The upper bound (5), followed by Cauchy--Schwarz with the
actual vector \(v_N\), gives omitted source rate
at most \(U+c+\eta<M\). No sign condition on \(v_N\) is
used. Finally \(m(u)\to0\) as \(u\to\pi\), by Lemma 3 and
continuity, and \(M>U\). Thus the full norm bound
\(|f_N(-2\cos u)|\le\|\mathbf e(-2\cos u)\|_2\|v_N\|_2\)
is strictly below \(M\) on a fixed neighborhood of \(\pi\).
\(\square\)

This proposition constructs real-color cutoffs and controls
their omitted original sums. The complex face currents
created by each cutoff still require estimates. It does
not supply a nonzero geometric coefficient or a whole-period
theorem for an arbitrary core.

## 6. A sufficient phase condition that requires no new contours

For a general original polynomial \(f_N=\mathbf e^Tv_N\), define
the absolute lower-half Newton sum
\[
 L_N=\sum_{0\le j<N/2}|v_{N,j}|\,e_j(-2).
 \tag{29}
\]
Every Newton factor in this sum is positive. The upper-half
factors have entropy at most zero, including the odd-level
zeros.

**Proposition 6.** Suppose that for fixed \(M>U\),
\[
 \|v_N\|_2\le C N^A e^{NU},\qquad
                 L_N\le C N^A e^{NM}.
 \tag{30}
\]
Then there are positive constants \(c,C_1,A_1\) such that
\[
 |f_N(-2\cos u)|\le C_1N^{A_1}
             e^{N[M-c(1-\cos u)]},\qquad -\pi\le u\le\pi.
 \tag{31}
\]

**Proof.** Choose a small fixed \(\varepsilon>0\). On the
central colors \(\varepsilon\le y\le1/2-\varepsilon\), the
same cosine-ratio estimate used in (10), or (9) of the
whole-period note at zero height, gives
\[
 V_u(y)-V_0(y)\le
       -\frac{\sin(2\pi\varepsilon)}{4\pi}(1-\cos u).
 \tag{32}
\]
The complete Newton product is uniformly bounded below
by \(N^{-B}e^{NV_0(j/N)}\) on this fixed central range:
its numerator stays away from its zero, and the sine
factorial estimate is two-sided. Combine this with (5)
to obtain the corresponding upper bound for
\(|e_j(-2\cos u)|/e_j(-2)\), with a polynomial prefactor.
Summing against \(|v_{N,j}|e_j(-2)\) and using (30)
therefore proves (31) for these central colors.

At both ends of the lower half, \(V_0(y)\) tends to zero.
Choose \(\varepsilon\) so small that the omitted lower-half
end ranges have entropy less than \((M-U)/2\).
Their \(V_u\) is no larger, by Lemma 2. The entire upper
half has \(V_u\le0\). Cauchy--Schwarz with \(\|v_N\|_2\)
then bounds the sum of these remaining colors at rate
at most \((M+U)/2\).
Taking
\[
 c\le\min\left\{\frac{\sin(2\pi\varepsilon)}{4\pi},
                         \frac{M-U}{4}\right\}
 \]
absorbs this remainder for every \(u\), since
\(1-\cos u\le2\). \(\square\)

Condition (30) says that the absolute Newton sum at completeness
does not grow faster than the proposed source rate. It follows
from a nonzero local source asymptotic when the lower-half
Newton coefficients have a common phase. More generally, it
has a direct formulation in terms of their actual phases.
When \(L_N>0\), put
\[
 \mu_{N,j}=\frac{|v_{N,j}|e_j(-2)}{L_N},\qquad
 z_{N,j}=\frac{v_{N,j}}{|v_{N,j}|}\quad(v_{N,j}\ne0),
 \qquad 0\le j<N/2 .
 \tag{33}
\]
The lower-half observation is
\(L_N\sum_j\mu_{N,j}z_{N,j}\).
If \(|f_N(-2)|\le\operatorname{poly}(N)e^{NM}\),
\(\|v_N\|_2\le\operatorname{poly}(N)e^{NU}\) with \(U<M\),
and the mean in (33) has modulus at least \(N^{-B}\),
then (30) follows. The omitted upper-half observation
has rate at most \(U\), so it cannot invalidate that
upper bound for \(L_N\).

This gives a precise possible use of almost-invariant phases.
Let \(P_N\) act on the support \(\{j:\mu_{N,j}>0\}\) and be
stochastic and reversible for \(\mu_N\), with spectral gap
\(\lambda_N>0\) on the orthogonal complement of the constants.
No laziness assumption is needed. For the actual
unit-modulus phase vector \(z_N\),
\[
 1-\left|\sum_j\mu_{N,j}z_{N,j}\right|^2
 \le\frac{\mathcal E_N(z_N)}{\lambda_N},\qquad
 \mathcal E_N(z)=\frac12\sum_{j,k}\mu_{N,j}(P_N)_{jk}
                                  |z_j-z_k|^2 .
 \tag{34}
\]
This is the spectral-gap inequality applied to the
mean-zero part of \(z_N\); for the standard variational
formulation see Levin and Peres,
[*Markov Chains and Mixing Times*, second edition,
Lemma 13.7 and Remark 13.8, p. 182](https://pages.uoregon.edu/dlevin/MARKOV/mcmt2e.pdf).
For complex \(z_N\), apply the real inequality to its real
and imaginary parts and add. An independently proved bound
\(\mathcal E_N(z_N)/\lambda_N\le1-N^{-2B}\)
therefore gives the required observation. In particular,
a ratio tending to zero makes the mean phase tend to
unit modulus.

The operator, gap, and phase-energy estimate must come
from the actual source. Choosing an unrelated gauge or
an auxiliary positive comparison state does not prove
(34) for its closing phases. The
[canonical polynomial counterexample](research_fourier_lower_bounds_and_almost_invariance.md)
shows that a local holomorphic source asymptotic and the
norm condition \(M>U+c\), without such further phase or
contour information, are insufficient.

**Corollary 7 (subexponential coherence).** Suppose \(M>U\),
\(L_N>0\) for all sufficiently large \(N\), and there are
nonnegative \(r_N,s_N=o(N)\) such that
\[
 \|v_N\|_2\le e^{NU+r_N},\qquad
 |f_N(-2)|\le e^{NM+r_N},\qquad
 \left|\sum_j\mu_{N,j}z_{N,j}\right|\ge e^{-s_N}.
 \tag{35}
\]
Then there are a fixed \(c>0\) and a nonnegative
\(q_N=o(N)\), independent of the real angle, such that
\[
 |f_N(-2\cos u)|
 \le \exp\{N[M-c(1-\cos u)]+q_N\},
                 \qquad -\pi\le u\le\pi.
 \tag{36}
\]
In particular every fixed closed angular set avoiding zero
has a strict exponential gap below \(M\).

Alternatively, suppose the norm and phase bounds in (35)
hold and \(N^{-1}\log L_N\to M\), without assuming the
complete-value upper bound in (35). Then
\[
             \lim_{N\to\infty}N^{-1}\log|f_N(-2)|=M,
 \tag{37}
\]
and (36) follows as well.

**Proof.** Write \(f_N(-2)=f_N^{\rm low}+f_N^{\rm up}\)
for its lower- and upper-half observations.
Lemma 1 and \(V_0\le0\) on the upper half give
\(|f_N^{\rm up}|\le e^{NU+o(N)}\).
Since
\[
 |f_N^{\rm low}|
       =L_N\left|\sum_j\mu_{N,j}z_{N,j}\right|,
 \]
(35) implies \(L_N\le e^{NM+o(N)}\).
The proof of Proposition 6 now applies with a scalar
\(o(N)\) in place of its logarithmic prefactors.
All Newton estimates are uniform in the angle and the
remaining losses depend only on \(M-U\) and a fixed
central cutoff. Their finitely many errors can therefore
be combined into one \(q_N=o(N)\), proving (36).

For the second assertion,
\(|f_N^{\rm low}|\ge e^{NM-o(N)}\), whereas its upper-half
remainder has strictly smaller rate \(U\).
The reverse triangle inequality gives the lower bound
in (37). The usual triangle inequality gives its upper
bound from \(L_N=e^{NM+o(N)}\).
This also supplies the complete-value upper bound needed
for the first part. \(\square\)

In the spectral-gap formulation, a sufficient hypothesis
for (35) is
\[
 \frac{\mathcal E_N(z_N)}{\lambda_N}
                     \le1-e^{-2s_N},\qquad s_N=o(N).
 \tag{38}
\]
The subexponential factor is sufficient for the exponential
rate; a polynomial lower bound for the mean phase is
stronger than necessary. Neither a gap nor (38) is
assumed for the original quantum sources.

**Lemma 8 (recovering a polynomial bound from a local expansion).**
Suppose \(\deg f_N\le N-1\), (36) holds, and on a fixed
complex neighborhood of zero,
\[
 f_N(-2\cos u)=
    \varepsilon_N N^\alpha A(u)e^{NW(u)}
                          (1+O(N^{-1})),
 \qquad |\varepsilon_N|=1.
 \tag{39}
\]
Here the error is holomorphic and uniform on smaller
closed neighborhoods, \(W,A\) are holomorphic, \(W\)
is even, \(A\) is nonzero, \(\alpha\) is fixed, and
\(\Re W(0)=M\). Then
\[
 |f_N(-2\cos u)|\le C N^d
             e^{N[M-\frac c2(1-\cos u)]},
                  \qquad -\pi\le u\le\pi.
 \tag{40}
\]
Also \(-\Re W''(0)\ge c\), and there are fixed
\(c_*,B,h>0\) for which
\[
 |f_N(-2\cos(x+iy))|
 \le C_1N^{d_1}e^{N[M-c_*(1-\cos x)+B y^2]},
             \qquad |x|\le\pi,\quad |y|\le h .
 \tag{41}
\]

**Proof.** At each fixed real \(u\) in the local chart,
take exponential rates in (36) and (39). This gives
\(\Re W(u)\le M-c(1-\cos u)\). The bounded local
amplitude in (39) therefore gives a polynomial
prefactor uniformly on a smaller real interval.
Choose its radius \(r>0\). For \(|u|\ge r\), the
uniform \(q_N=o(N)\) in (36) is eventually at most
\(cN(1-\cos r)/2\), and hence at most
\(cN(1-\cos u)/2\). This proves (40), after absorbing
the finitely many smaller levels into \(C\).
Evenness and the local phase inequality also give
\(-\Re W''(0)\ge c\).

Put \(c_r=c/2\) and \(z=e^{iu}\). Multiplying
the Laurent polynomial \(f_N(-(z+z^{-1}))\) by
\(z^{N-1}\) makes it holomorphic in the unit disk.
Apply the maximum principle after multiplying by
\(e^{-Nc_r z}\). The boundary majorant (40) yields
\[
 |f_N(-2\cos(x+iy))|
 \le C N^d\exp N[
      M-c_r+c_r e^{-|y|}\cos x+|y|].
 \tag{42}
\]
Evenness gives the same inequality in both half-strips.
Its cost over the real bound is at most
\((1+c_r)|y|\).

Locally, shrink the complex disk so that
\(\Re[-W''(u)]\ge a>0\), and bound \(|W''|\) there
by a constant \(L\). Taylor's formula, \(W'(0)=0\),
and Young's inequality give
\[
 \Re W(x+iy)\le
 M-\frac a4 x^2+
                  \left(\frac{L^2}{a}+\frac L2\right)y^2.
 \]
This and (39) give a local quadratic strip bound.
Away from a smaller real interval, choose \(h>0\)
so that the linear cost in (42) uses at most half
of the fixed angular gap. Combining these two
regions proves (41). \(\square\)

Thus subexponential coherence, together with an already
proved nonzero holomorphic local expansion, supplies
the analytic hypotheses of the
[fixed-source subsequent-turn theorem](research_uniform_large_power_turn.md).
Its original marking and geometric hypotheses must
still hold separately. This deduction constructs no
new local contribution and is not an application to
arbitrary signed tangle sources.

## 7. The local phase can force cancellation in the Newton coefficients

The sufficient conditions in Section 6 require information
about the actual phases. They are not automatic consequences
of the geometric saddle. In fact, the phase of the adjacent
three-crossing source prevents those conditions from holding
in its original Newton expansion.

The obstruction has an elementary formulation in the ordinary
boundary coordinate \(w\), rather than the angular coordinate
\(u\). Keep \(f_N(w)=\sum_{j=0}^{N-1}v_{N,j}e_j(w)\) and
the positive lower-half sum \(L_N\) from (29).

**Theorem 9 (a local obstruction to phase coherence).**
Suppose that
\[
 \limsup_{N\to\infty}N^{-1}\log\|v_N\|_2\le U<M
 \tag{43}
\]
and that on a fixed complex neighborhood of \(w=-2\),
\[
 f_N(w)=\eta_N N^\alpha A(w)e^{N\Theta(w)}(1+o(1)),
 \qquad |\eta_N|=1,\qquad \Re\Theta(-2)=M.
 \tag{44}
\]
Here \(A,\Theta\) are holomorphic, \(A\) is nonzero, \(\alpha\)
is fixed, and the error is uniform on smaller closed
neighborhoods. If \(\Im\Theta'(-2)\ne0\), then there is a
fixed \(\delta>0\) such that
\[
 \liminf_{N\to\infty}N^{-1}\log L_N\ge M+\delta,
 \qquad
 \limsup_{N\to\infty}N^{-1}\log
       \left|\sum_j\mu_{N,j}z_{N,j}\right|\le-\delta.
 \tag{45}
\]
The weights and phases are exactly those in (33). In particular,
neither a polynomial nor a subexponential lower bound for this
mean phase is possible.

Equivalently, under (43)--(44), an upper bound
\(L_N\le e^{NM+o(N)}\) requires \(\Im\Theta'(-2)=0\).
This is a necessary condition, not a sufficient one.

For any reversible Markov operator on these actual weights
with positive gap \(\lambda_N\), (34) and (45) also imply
\[
 \frac{\mathcal E_N(z_N)}{\lambda_N}
       \ge 1-\exp\{-2\delta N+o(N)\}.
\]
Thus the phase defect cannot be small relative to its gap
in this realization. The assertion concerns these weights
and the original observation, not every possible exact
representation of the source.

**Proof.** First control the colors near the ends of the lower
half, together with the entire upper half, in a small complex
disk. Choose \(0<\varepsilon<1/4\) so small that
\[
 V_0(y)\le \frac{M-U}{4}
 \quad\text{on}\quad
 [0,\varepsilon]\cup[1/2-\varepsilon,1].
 \tag{46}
\]
This is possible because \(V_0\) is continuous, vanishes at
\(0\) and \(1/2\), and is nonpositive on \([1/2,1]\).
For a fixed \(\rho>0\), the original product gives
\[
 \begin{split}
 |e_j(-2+\zeta)|
 &\le S_j^{-2}\prod_{\nu<j}(c_\nu+2+\rho)\\
 &\le C_\rho N^{B_\rho}
   \exp N\left[V_0(j/N)+
                    \operatorname{arcosh}(1+\rho/2)\right],
                 \qquad |\zeta|\le\rho .
 \end{split}
 \tag{47}
\]
The first inequality uses \(c_\nu+2\ge0\). For completeness,
the logarithm of its positive product is a smooth midpoint
sum with integrand
\(\log(2+\rho+2\cos2\pi t)\). The sine denominator has
the usual uniform \(O(\log N)\) error. The difference
from the \(\rho=0\) integral is nonnegative, and its
integral over a full period is
\[
 \int_0^1\log
       \frac{2+\rho+2\cos2\pi t}{2+2\cos2\pi t}\,dt
       =\operatorname{arcosh}(1+\rho/2).
 \]
One obtains this identity by differentiating in \(\rho\):
the derivative of the integral is
\(1/\sqrt{\rho(\rho+4)}\), and the integral tends to zero
as \(\rho\downarrow0\). This proves (47) for every original
row, including rows whose value at \(-2\) vanishes.
It is the same estimate used in the
[preparation-error proof](research_three_crossing_global_preparation_error.md).

Choose \(\rho\) small enough to remain inside the chart
in (44) and to have
\(\operatorname{arcosh}(1+\rho/2)<(M-U)/4\).
By (43), (46), (47), and Cauchy--Schwarz, all rows outside
\[
       \varepsilon\le j/N\le1/2-\varepsilon
 \]
have a combined exponential rate strictly below
\((M+U)/2<M\), uniformly on this complex disk. The strict
inequality follows from the strict choice of \(\rho\);
polynomial prefactors and the \(o(N)\) in (43) do not
change the rate.

On the retained central rows there is a stronger, exact
inequality. Put
\[
                a_\varepsilon=4\sin^2(\pi\varepsilon)>0 .
 \]
Every factor in their numerator satisfies
\[
 c_\nu+2=
 4\cos^2\!\left(\frac{\pi(\nu+1/2)}N\right)
                  \ge a_\varepsilon .
 \]
Consequently
\[
 |\zeta|^2\le2a_\varepsilon\Re\zeta
       \quad\Longrightarrow\quad
 |e_j(-2+\zeta)|\le e_j(-2)
 \tag{48}
\]
on every retained row. Indeed, for a real
\(a\ge a_\varepsilon\),
\(|a-\zeta|^2=a^2-2a\Re\zeta+|\zeta|^2\le a^2\).
The region in (48) is the closed disk with center
\(a_\varepsilon\) and radius \(a_\varepsilon\) in the
\(\zeta\)-plane. It touches the origin from the right.
No division by a possibly vanishing Newton factor has
been used.

Write \(q=\Im\Theta'(-2)\ne0\). For a small positive
number \(t\), set
\[
       \zeta(t)=\frac{t^2}{a_\varepsilon}
                           -i\,\operatorname{sign}(q)t .
 \tag{49}
\]
For \(t\le a_\varepsilon\) this lies in the disk (48).
For sufficiently small \(t\), it also lies in
\(|\zeta|<\rho\), and Taylor's formula gives
\[
 \Re\Theta(-2+\zeta(t))
       =M+|q|t+O(t^2)>M .
 \]
Fix such a \(t\), and let
\(\delta=\Re\Theta(-2+\zeta(t))-M>0\).
At this fixed point, (44) has exponential rate
\(M+\delta\). The omitted rows have rate below \(M\),
so the reverse triangle inequality shows that the
retained central sum has rate \(M+\delta\) as well.
By (48), its modulus is at most \(L_N\). This proves
the first inequality in (45).

At \(w=-2\), the entire upper-half observation has rate
at most \(U\), by Lemma 1 and \(V_0\le0\) there.
Equation (44) therefore implies that the lower-half
observation has rate exactly \(M\). Since it equals
\(L_N\sum_j\mu_{N,j}z_{N,j}\), the second inequality in
(45) follows. In particular \(L_N>0\) for all sufficiently
large \(N\), so these weights are defined. \(\square\)

For the original adjacent three-crossing source,
\[
 v_N=JM^3JM^3e_0=JM^2\gamma_N,\qquad
       \gamma_N=MJM^3e_0.
 \]
Here the \(M\) in the matrix powers is the original crossing
multiplication matrix; the scalar \(M\) in (43)--(45) is the growth rate.
The proved operator and prepared-column bounds give
\[
 \limsup N^{-1}\log\|v_N\|_2
       \le b_2+A_*<\frac{10363}{10000}=1.0363,
 \qquad M>\frac{1537}{1000}=1.537 .
 \tag{50}
\]
Thus the strict separation required by (43) is available
with a large margin.

The [local boundary theorem](research_three_crossing_full_boundary_asymptotic.md)
gives the nonzero expansion (44). To compute its derivative,
write \(W(u)=\Theta(-2\cos u)\), and let
\(Y=e^{2\pi i y_*}\) be the outer clock at the selected
complete saddle. Its certified positive height gives
\(|Y|<1\). Differentiating the Newton part of the phase,
\[
 b_u(y,u)=\frac1{2\pi}
       \operatorname{Log}\frac{1+Ye^{iu}}{Y+e^{iu}},
 \]
at \(u=0\) gives
\[
 W''(0)=\frac{i}{2\pi}\frac{Y-1}{Y+1},\qquad
 \Theta'(-2)=\frac{W''(0)}2
           =\frac{i}{4\pi}\frac{Y-1}{Y+1}.
 \tag{51}
\]
The stationary variables introduce no extra term:
\(b_u(y,0)=0\) for every \(y\), so its derivative in \(y\)
also vanishes at \(u=0\). The relation between the two
derivatives follows from
\(-2\cos u=-2+u^2+O(u^4)\).
In particular,
\[
 \Im\Theta'(-2)
       =\frac{|Y|^2-1}{4\pi|Y+1|^2}<0 .
 \tag{52}
\]
Complex conjugation reverses this sign and preserves its
nonvanishing. Theorem 9 therefore applies to the source
and its conjugate.

This conclusion concerns the original Newton coefficients,
after their internal color sums have already been performed.
Their absolute weighted sum grows strictly faster than the
source itself. The exponential cancellation is consequently
not confined to the unreduced triple sum. The phase
conditions of Section 6 cannot prove the result for this
pair in this basis; its proved whole-period estimate uses
the actual complex contour and its separate face bounds.

In particular, for any reversible operator on these actual
weights with positive spectral gap, (34) and (45) imply
\[
 \frac{\mathcal E_N(z_N)}{\lambda_N}
       \ge 1-\exp\{-2\delta N+o(N)\}.
 \]
Thus this realization of the phase vector cannot meet the
subexponential coherence condition (38). The conclusion is
about these weights and these phases; it does not exclude
a different exact representation of the invariant.

There is also a geometric interpretation, with the primitive
boundary curves kept fixed. The
[action-volume calculation](research_three_crossing_action_volume_calibration.md)
uses the logarithmic periods
\[
             U_0(u)=-2\pi W'(u),\qquad V(u)=2iu .
 \]
If \(\tau_{\rm cusp}=dV/dU_0\) denotes the cusp parameter
in precisely this basis, then
\[
 \tau_{\rm cusp}=-\frac{i}{\pi W''(0)},\qquad
 \Re\tau_{\rm cusp}
      =-\frac{\Im W''(0)}{\pi|W''(0)|^2}.
 \tag{53}
\]
Thus the nonzero imaginary derivative in Theorem 9 is
equivalent here to a nonzero real part of this cusp
parameter, or cusp shear. This is a statement in the
specified primitive basis. A boundary crossing or a
framing change alters the phase and the peripheral basis
together; (53) is not a coordinate-invariant obstruction.
It uses the directly established marked geometric branch
and does not assume an additional identification with an
\(A\)-polynomial.

## 8. Scope for the adjacent three-crossing source

The [local boundary theorem](research_three_crossing_full_boundary_asymptotic.md)
now proves its nonzero geometric contribution. The
[whole-period theorem](research_three_crossing_whole_period_source.md)
combines the estimates here with the separate current
certificates for the two retained domains. It proves the
whole real Gaussian bound and the thin complex strip
needed by the existing subsequent-turn theorem.

These conclusions concern the specified adjacent pair and
its conjugate. They do not establish the corresponding
source estimates for arbitrary connected short regions,
which remain part of the finite-exception objective.
