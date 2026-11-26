# A nonzero Fourier window after the next crossing

Research note, 3 November 2026.

The Fourier estimate for the three-crossing column survives a turn
followed by one more original crossing. This note proves that assertion
for a specified phase correction and specified Fourier observations.
It does not replace the final boundary evaluation by one of those
observations. That additional pairing remains an analytic problem.

## 1. The vector and the two endpoint solutions

Fix an integer \(N\ge2\), and put
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad D=N-1,\quad
 \kappa=e^{\pi iD^2/(2N)},\quad
 S_j=\prod_{r=1}^j2\sin(\pi r/N),\quad S_0=1.
 \tag{1}
\]
The original crossing matrix and the turn are
\[
 M_{kj}=\kappa(-1)^kq^{k(j+1)}\frac{S_k}{S_jS_{k-j}}
 \quad(0\le j\le k<N),\qquad
 (Jv)_j=v_{D-j}.
 \tag{2}
\]
Entries above the diagonal of \(M\) are zero. We study
\[
             \alpha=M^3e_0,\qquad \gamma=MJ\alpha.
 \tag{3}
\]
Here \(e_0\) is the first coordinate vector, not a boundary evaluation.
The [endpoint and dominant-profile theorem](research_three_crossing_next_crossing_dominant_profile.md)
retains the exact endpoint values
\[
 \gamma_0=\kappa\alpha_D,\qquad \gamma_D=N,\qquad
 |\gamma_0|=N^{3/2}(1+O(N^{-1})).
 \tag{4}
\]
Its normalized left and right solutions are
\[
 y_j=\frac{(-q)^{-j}S_j^2\gamma_j}{\gamma_0},\qquad
 P_r=\frac{(-q)^r(Q;Q)_r\gamma_{D-r}}{N},
 \tag{5}
\]
where \((Q;Q)_r=\prod_{s=1}^r(1-Q^s)\). The first normalization
is used for sufficiently large \(N\), for which (4) ensures that
its denominator is nonzero. Both solve second-order recurrences
with their actual initial conditions:
\[
 \begin{split}
 y_{j+1}&=[3-(1+Q^{-1})Q^{-j}]y_j
          -d_j(1-Q^{-j})y_{j-1},\\
 y_0&=1,\qquad y_1=2-Q^{-1}-\kappa^2/\gamma_0,\\
 P_{r+1}&=[3-(1+Q)Q^r]P_r-d_r(1-Q^r)P_{r-1},\\
 P_0&=1,\qquad P_1=2-Q,
 \end{split}\qquad d_j=4\sin^2(\pi j/N).
 \tag{6}
\]
In particular the first equation has not been supplied with a freely
chosen solution of dominant growth. Its initial coefficient is fixed
by the original quantum sum.

For \(0\le x<1/2\), set
\[
 \begin{split}
 X(x)&=e^{-2\pi ix},\qquad d(x)=2-X(x)-X(x)^{-1},\\
 \lambda(x)&=\frac{3-2X(x)+\sqrt{4/X(x)-3}}2,\\
 \mu(x)&=\frac{3-2X(x)-\sqrt{4/X(x)-3}}2.
 \end{split}
 \tag{7}
\]
The square root continues from \(+1\) at \(x=0\). On this interval
the two roots are distinct and \(|\lambda|>|\mu|\). The logarithm
of \(\lambda\) is continued from zero. Define
\[
 \begin{split}
 I(x)&=\int_0^x\log\lambda(t)\,dt,\\
 G(x)&=\sqrt{\frac{\lambda(x)}{\lambda(x)-\mu(x)}},
                   \qquad G(0)=1,\\
 J_0(x)&=\int_0^x\log(2\sin\pi t)\,dt,\\
 A(x)&=\operatorname{Re}I(x)-2J_0(x),\qquad
 B(x)=\operatorname{Re}I(x)-J_0(x).
 \end{split}
 \tag{8}
\]
The notation \(J_0\) here denotes a real integral; the matrix \(J\)
in (2) still denotes index reversal. Both \(G\) and \(\lambda\)
are nonzero on every compact subinterval of \([0,1/2\)).
The endpoint theorem gives, for each fixed \(b<1/2\),
\[
 y_j=G(j/N)e^{NI(j/N)}(1+O_b(N^{-1}))
              \qquad(0\le j\le bN).
 \tag{9}
\]
For the right solution, its conjugate satisfies the same formula.
The absence of the small forcing term in its first ratio changes
the error in (9), not its leading factor. In particular,
\[
 \begin{split}
 N^{-1}\log|\gamma_j|&=A(j/N)+O_b(\log N/N),
                         &&j\le bN,\\
 N^{-1}\log|\gamma_{D-r}|&=B(r/N)+O_b(\log N/N),
                         &&r\le bN.
 \end{split}
 \tag{10}
\]
The second line uses \(|(Q;Q)_r|=S_r\), not \(S_r^2\).
This distinction is necessary for the global comparison below.

## 2. The unique maximum and a bound for the middle indices

**Lemma 1.** The function \(A\) has exactly one critical point
\(x_*\in(0,1/2)\). It is a nondegenerate maximum. If \(z_*\)
is the unique real root of
\[
                  z^3-2z^2-z+3=0,
 \tag{11}
\]
then \(2\cos(2\pi x_*)=z_*\). Moreover \(B\) is strictly
increasing on \((0,1/2)\), and
\[
           B(1/2)=A(1/2)<A(x_*).
 \tag{12}
\]
Values at \(1/2\) mean one-sided continuous limits.

*Proof.* Put \(\rho_+=\lambda/d\) and \(\rho_-=\mu/d\).
The characteristic equation and its reciprocal conjugate are
\[
 d\rho^2-(3-2X)\rho+1-X=0,
 \qquad d-(3-2X^{-1})\rho+(1-X^{-1})\rho^2=0.
 \tag{13}
\]
Their resultant, computed by eliminating \(\rho\), is
\[
 \begin{split}
 R&=-d\,[z^3-2z^2-z+3],\qquad z=X+X^{-1},\\
 R&=d^4(1-|\rho_+|^2)(1-|\rho_-|^2)
                    |1-\rho_+\overline{\rho_-}|^2.
 \end{split}
 \tag{14}
\]
The cubic has discriminant \(-31\), so it has one real root;
its values at \(-2,-1\) have opposite signs. Thus the root
lies in \((-2,-1)\).

Now \(A'=\log(|\lambda|/d)\). It is positive near zero,
where \(\lambda\to1\) and \(d\to0\), and has limit
\(-\tfrac12\log2<0\) at \(1/2\). Every zero must occur at
the single candidate (11), by (14). Hence this candidate is
the only zero. At that point \(d>3\), \(|\rho_+|=1\), and
\(|\rho_-|=d^{-1/2}<1\), since
\(|\lambda\mu|=d^{3/2}\). The other factors in the second
line of (14) are nonzero. The first line has a simple zero
as a function of \(x\). Therefore \(A'\) has a simple zero;
the sign change proves \(A''(x_*)<0\).

Finally \(B'=\log(|\lambda|/\sqrt d)\). A zero would force
\(|\mu|=d\), and therefore again force (11). But at the
unique candidate, \(|\lambda|=d>\sqrt d\). Thus \(B'\)
has no zero. It is positive near zero, proving monotonicity.
The classical sine integral \(J_0(1/2)=0\) gives (12).
For completeness, this identity follows from the change of
variables \(t\mapsto\pi/2-t\) and the double-angle formula
in the integral of \(\log\sin t\) on \([0,\pi/2]\).
\(\square\)

**Lemma 2.** For any fixed neighborhood \(U\) of \(x_*\)
whose closure lies in \((0,1/2)\), there is \(c_U>0\) such
that
\[
 \max_{j/N\notin U}|\gamma_j|
           \le \exp\bigl(N[A(x_*)-c_U]+O(\log N)\bigr).
 \tag{15}
\]

*Proof.* The left estimate (10) and Lemma 1 give the claim
up to \(j/N=1/2-\varepsilon\), outside \(U\). The right
estimate and monotonicity of \(B\) bound the part beyond
\(1/2+\varepsilon\) by the rate \(B(1/2)\).

It remains to estimate the middle interval. The exact equation
for the original coefficients is
\[
 q^{-1}d_{j+1}\gamma_{j+1}
   +[3-(1+Q^{-1})Q^{-j}]\gamma_j
   +q(1-Q^{-j})\gamma_{j-1}=0\qquad(j\ge1).
 \tag{16}
\]
On \(2/5\le j/N\le3/5\), its two-dimensional transfer
matrices have norm at most a constant \(K\), independently
of \(N\). This follows immediately because \(d_{j+1}\)
is bounded away from zero there and all numerators are bounded.
Starting at \(j/N=1/2-\varepsilon+O(N^{-1})\), at most
\(2\varepsilon N+O(1)\) steps therefore give a middle rate
at most
\[
          A(1/2-\varepsilon)+2\varepsilon\log K+o(1).
 \tag{17}
\]
As \(\varepsilon\downarrow0\), this tends to \(A(1/2)\),
which is strictly below \(A(x_*)\). Choose a sufficiently
small fixed \(\varepsilon\). Compactness then gives a
positive gap in all three regions. No choice of a dominant
branch is made across the equality of moduli at \(1/2\).
\(\square\)

## 3. A positive approximation and its actual Fourier coefficients

Put \(a=-A''(x_*)>0\), and fix \(b\in(x_*,1/2)\). For
\(0\le j\le bN\), define a unit scalar using the nonzero
functions in (8):
\[
 \chi_{N,j}=\frac{\gamma_0}{|\gamma_0|}(-q)^j
              \frac{G(j/N)}{|G(j/N)|}
              \exp\bigl(iN\operatorname{Im}I(j/N)\bigr).
 \tag{18}
\]
For the other indices set \(\chi_{N,j}=1\). This arbitrary
extension affects only exponentially small tails. Set
\[
 v_{N,j}=\frac{\chi_{N,j}^{-1}\gamma_j}{\|\gamma\|_2},
 \qquad
 \widehat v_N(m)=N^{-1/2}\sum_{j=0}^{N-1}v_{N,j}e^{-2\pi imj/N}.
 \tag{19}
\]

**Theorem 3.** For every fixed \(T<\infty\), uniformly for
integer representatives \(|m|\le T\sqrt N\),
\[
 \widehat v_N(m)=
 \left(\frac{4\pi}{a}\right)^{1/4}N^{-1/4}
 e^{-2\pi imx_*}
 \exp\left(-\frac{2\pi^2m^2}{aN}\right)
                     (1+O_T(N^{-1/2})).
 \tag{20}
\]
In particular \(|\widehat v_N(0)|\ge cN^{-1/4}\) for
all sufficiently large integer levels. If \(\mathsf S\)
denotes the cyclic shift \((\mathsf Sv)_j=v_{j-1\bmod N}\),
then
\[
 \|\mathsf Sv_N-v_N\|_2=\sqrt{\frac{a}{2N}}+O(N^{-1}).
 \tag{21}
\]
The norm of the original vector has the explicit equivalent
\[
 \|\gamma\|_2=
 |\gamma_0|N^{-3/4}
 \frac{|G(x_*)|}{2\sin(\pi x_*)}
 \left(\frac{\pi}{a}\right)^{1/4}
 e^{NA(x_*)}(1+O(N^{-1/2})).
 \tag{22}
\]

*Proof.* Equations (5), (9), and (18) give the positive
comparison sequence
\[
 h_{N,j}=\frac{|\gamma_0|}{S_j^2}|G(j/N)|
                 e^{N\operatorname{Re}I(j/N)}
                 \quad(0\le j\le bN),
 \tag{23}
\]
extended by zero. The relative error there is \(O(N^{-1})\).
Lemma 2 bounds the other indices by an exponentially smaller
quantity. Consequently
\[
 \left\|v_N-\frac{h_N}{\|h_N\|_2}\right\|_2=O(N^{-1}).
 \tag{24}
\]
Near \(x_*\), the elementary uniform sine-product expansion
\[
 S_j^2=2N\sin(\pi j/N)e^{2NJ_0(j/N)}(1+O(N^{-1}))
 \tag{25}
\]
shows that (23) has smooth positive prefactor
\(|\gamma_0|\,|G(x)|/[2N\sin(\pi x)]\) multiplying
\(e^{NA(x)}\). The expansion (25) follows by subtracting
\(\log(2\pi t)\) from \(\log(2\sin\pi t)\), applying
Euler--Maclaurin to the resulting smooth function, and
applying Stirling to the factorial.

Write \(s=(j-Nx_*)/\sqrt N\). Taylor expansion at the
nondegenerate maximum gives a leading factor \(e^{-as^2/2}\).
The error in the local approximation is bounded by
\(C N^{-1/2}(1+|s|^3)e^{-c s^2}\), after reducing the fixed
neighborhood if necessary. Lemma 2 controls its complement.
The lattice spacing in \(s\) is \(N^{-1/2}\), so Gaussian
Riemann sums give (22) and
\[
 \int_{\mathbb R}e^{-as^2/2}e^{-2\pi its}\,ds
            =\sqrt{2\pi/a}\,e^{-2\pi^2t^2/a}.
 \tag{26}
\]
Dividing by the Gaussian norm gives the constant in (20)
for the normalized positive sequence. Its error is uniform
for \(|t|\le T\). Unitarity of the Fourier transform and
(24) change each coefficient by \(O(N^{-1})\), smaller
than the \(O(N^{-3/4})\) error already in (20).

For (21), the logarithm of the ratio of adjacent terms
in (23) is
\[
 \log(h_{N,j-1}/h_{N,j})=-A'(j/N)+O(N^{-1})
               =a s/\sqrt N+O((1+s^2)/N)
 \tag{27}
\]
near the maximum. The squared normalized weights converge
to \(\sqrt{a/\pi}e^{-as^2}\,ds\), including their fixed
polynomial moments by the same Gaussian bounds. Thus
the squared shift residual is
\(a^2N^{-1}(2a)^{-1}+O(N^{-3/2})\).
The truncation and cyclic seam contribute exponentially
small errors. Finally (24) changes the residual norm by
\(O(N^{-1})\), proving (21). \(\square\)

The original-coordinate unitary operator is
\(\operatorname{diag}(\chi_N)\mathsf S\operatorname{diag}(\chi_N)^{-1}\).
The proved Fourier observations are the explicit unit vectors
\(N^{-1/2}\chi_{N,j}e^{2\pi imj/N}\). Equations (20)--(22)
therefore bound actual linear functionals of \(\gamma\),
not a separate positive model.

The negative crossing word is obtained by complex conjugation.
Conjugating the phase (18) gives the same positive comparison
and the same norm, shift, and Fourier-window conclusions.

## 4. What this does and does not settle

The nonzero coefficient here comes from the original endpoint
\(\gamma_0\), propagation in a region with a strict eigenvalue
modulus gap, and a positive Gaussian approximation after the
explicit phase correction. No group-theoretic spectral-gap
assumption supplies that coefficient. The almost invariance
in (21) follows from this proved profile.

The final adjacent-three-crossing boundary polynomial is still
\(F_N(w)=(M^3\mathbf e(w))^{\mathsf T}(M^3e_0)\), where
\(\mathbf e(w)\) is the Newton evaluation vector. The new
Fourier observations are not that row. A lower bound for its
coherent contraction is still required. In particular (22)
is not asserted to equal the hyperbolic volume rate for the
closed short-pair problem.

The [original-source checker](../experiments/check_three_crossing_next_crossing.py)
computes both crossing signs by original multiplication and
triangular inverse solves. Its
[140-digit record](../repro/results/research-three-crossing-next-crossing.json)
checks 4,088 finite identities and the two symbolic eliminations
used above. It also records finite norm and localization data;
these data are diagnostics, not hypotheses of the proofs.
The algebraic peak is approximately \(x_*=0.3472947207\);
numerical integration gives \(A(x_*)\approx0.4530362239\).
Neither decimal is used in the argument.

Reproduction:

    python3 experiments/check_three_crossing_next_crossing.py --precision 140
