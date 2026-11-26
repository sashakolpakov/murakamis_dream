# The complete 44 message on the far real second arc

Private written proof, 11 November 2026. This estimates the complete
first contraction on the whole real second interval \([7/8,1]\).
The two second Fourier alternatives, the first diagonal polynomial,
and all finite rows remain in the source. The comparison is to the
original three-factor affine action.

The argument uses a correlated small-index estimate for the incoming
numerator, and the existing complete disk norms for the other indices.
It is not a continuation of a local packet or a physical terminating
sum. It does not connect the second plateau heights to this real arc.

## 1. Source, allocations, and statement

Fix an actual positive three/four open word of length \(m\ge4\)
beginning with \(443\) or \(444\), with flags \((1,1,\beta)\).
Keep its original coupled reference, logarithmic lifts, and ordinary
incoming color \(w\). Put
\[
 P=[11/50,9/20],\qquad z=v+ic_3,\quad v\in P,\qquad
 Z=e^{-2\pi iz},\quad c_3=\Im r_3,
 \tag{1}
\]
where the actual reference bounds are
\[
 \begin{cases}
 -13/200\le c_3\le17/250,&\beta=0,\\
 -51/500\le c_3\le-1/1000,&\beta=1.
 \end{cases}
 \tag{2}
\]
These are the same actual families as in the complete-message seam
theorem, including the ordinary third incidence when its following
leg is attached at \(m=4\).

With \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), \(S_j=|P_j|\), and
\(p_j(X)=(rX;r)_j\), retain
\[
\begin{split}
 U_{1,N}(w,X)&=\sum_{i<N}H_N(w,r^{-i})p_i(X)/P_i^2,\\
 C_{\epsilon,N}(X,Y)&=\sum_{j<N}
                  X^{-j}p_j(X)p_j(Y)/P_j^{2+\epsilon},\\
 f_N(w,Y)&=N\operatorname{CT}_X
       [U_{1,N}(w,X)d_N(X)(1+X^{-N})C_{1,N}(X,Y)]\\
 &=\sum_{a<N}\frac{U_{1,N}(w,r^a)}{P_a}C_{1,N}(r^a,Y).
\end{split}
 \tag{3}
\]
Here \(f_N=f_{44,N}\) is the complete first polynomial, not its
restricted plateau contribution. The last equality is the original
finite coefficient identity. The two first Fourier coefficients
produce one unnormalized physical sum, with no extra factor two.

For \(\sigma=0,1\), the second density and outgoing allocation are
\[
 \mathscr D_{\sigma,\beta,N}(w,Y,Z)
       =f_N(w,Y)d_N(Y)Y^{-\sigma N}C_{\beta,N}(Y,Z),
 \qquad
 D_{\beta,N}(Z)=
 \begin{cases}1,&\beta=0,\\ |d_N(Z)|^{1/2},&\beta=1.\end{cases}
 \tag{4}
\]
The original second measure is \(+N\,dy\), for
\(Y=e^{-2\pi iy}\).

Use the unchanged action and affine marginal
\[
\begin{split}
 F_{123}&=\Psi(e,z_1)+Q_1(s_2;z_1,z_2)
       +Q_\beta(s_3;z_2,z_3)-g(z_1)-g(z_2)-\frac{\beta}{2}g(z_3),\\
 \Lambda_{123}(z)&=\Re F_{123,*}+\Re\{p_R(z-r_3)\},\\
 p_R&=g'(s_3^*+r_3)-(1+\beta/2)g'(r_3).
\end{split}
 \tag{5}
\]
Every star and primitive is that of the same actual word. In
particular \(g(z)=J(z)+i\pi(z-z^2)/2\), with the original analytic
primitive \(J'(z)=\operatorname{Log}(2\sin\pi z)\), \(J(0)=0\),
on each stated source strip.

**Theorem 1.** There are a fixed ordinary-color disk \(\mathcal D\)
about \(-2\), constants \(C,B,N_0\), and, for every fixed ordinary
derivative order \(k\), constants \(C_k,B_k\), such that at both level
parities and \(N\ge N_0\),
\[
 |\mathscr D_{\sigma,\beta,N}(w,e^{-2\pi iy},Z)|D_{\beta,N}(Z)
 \le C N^B e^{N\{\Lambda_{123}(z)-1/500\}},
 \quad 7/8\le y\le1,\quad w\in[-2,2]\cup\mathcal D,
 \tag{6}
\]
uniformly over (1) and both \(\sigma\). The same exponential rate
holds for \(k\) derivatives in \(w\), on the real interval and on
smaller color disks, with \(C_kN^{B_k}\).
The outgoing nonnegative multiplier is neither divided out nor
differentiated.

Thus the literal second currents on this entire real arc have a
strict gap, with their original \(N\) density. No second height
connection, remaining real shoulder, complete second coefficient,
or nonzero asymptotic for that coefficient is asserted.

## 2. A uniform quotient profile near the final real endpoint

Let \(J\) denote the continuous one-periodic real primitive
\[
 J'(u)=\log(2|\sin\pi u|),\qquad J(0)=0,\qquad
 J(1-u)=-J(u).
 \tag{7}
\]
On \((0,1)\), \(J''(u)=\pi\cot\pi u\).
Write
\[
 y=1-\varepsilon,\quad 0\le\varepsilon\le1/8,\qquad
 A_\varepsilon(t)=\int_0^t
       \log|1-e^{-2\pi i(y+v)}|\,dv-J(t).
 \tag{8}
\]
Periodicity gives the exact expressions
\[
 A_\varepsilon(t)=
 \begin{cases}
 J(\varepsilon)-J(\varepsilon-t)-J(t),&0\le t\le\varepsilon,\\
 J(t-\varepsilon)-J(t)+J(\varepsilon),&\varepsilon\le t\le1.
 \end{cases}
 \tag{9}
\]
Every endpoint and logarithmic zero is interpreted continuously.

For the second range,
\[
                         A_\varepsilon(t)\le0.
 \tag{10}
\]
Indeed \(D(a)=J(a+\varepsilon)-J(a)\), for
\(0\le a\le1-\varepsilon\), increases and then decreases:
the derivative has the sign of
\(\sin\pi(a+\varepsilon)-\sin\pi a\).
Both endpoint values are \(J(\varepsilon)\). Hence its minimum is
\(J(\varepsilon)\), which proves (10).

For the first range let
\[
 \mathsf h(s)=-s\log s-(1-s)\log(1-s),\qquad 0\le s\le1.
\]
Then
\[
             A_\varepsilon(t)\le
                      \varepsilon\mathsf h(t/\varepsilon).
 \tag{11}
\]
For \(0<t<\varepsilon\), the inequality
\(\pi\cot\pi u\le1/u\) gives
\[
 A_\varepsilon''(t)\ge-\frac1t-\frac1{\varepsilon-t}
           =\{\varepsilon\mathsf h(t/\varepsilon)\}''.
\]
The difference is convex and vanishes at both endpoints, proving
(11). When \(\varepsilon=0\), use \(A_0=0\).

The uniform zero-safe numerator estimate and uniform sine-factorial
estimate imply, for every \(\tau>0\),
\[
 \frac{|p_j(e^{-2\pi i(1-\varepsilon)})|}{S_j}
 \le C_\tau N^{B_\tau}
       e^{N\{A_\varepsilon(j/N)+\tau\}},
 \quad j<N,\quad 0\le\varepsilon\le1/8.
 \tag{12}
\]
This is the same product argument as equation (4) of the transformed
real-initial source, applied to the present real interval. Explicitly,
replace the numerator logarithm by
\(\log(|1-e^{-2\pi i(y+v)}|+\delta)\). For fixed \(\delta>0\),
its Riemann-sum error is uniform in \(y,t\). The integral excess
tends uniformly to zero with \(\delta\), since its real zeros are
simple and the local excess is \(O(\delta(1+|\log\delta|))\).
The denominator has its original uniform \(O(\log N)\) endpoint
error for every \(j<N\). This proves (12), including exact zeros
and both parities. In particular (10) is used as a rate bound;
no pointwise finite inequality \(|p_j(Y)|\le S_j\) is claimed.

## 3. Small indices of either own-four source

For \(|W|\le1\), the exact numerator satisfies
\(|p_j(W)|\le2^j\). Set
\[
 F(t)=t\log2-2J(t),\qquad m=\log(25/8).
 \tag{13}
\]
On \(0<t\le1/8\),
\[
 F'(t)=\log2-2\log(2\sin\pi t)>m>0,
 \tag{14}
\]
because \(2\sin(\pi/8)=\sqrt{2-\sqrt2}<4/5\).
The latter radical inequality follows from
\(\sqrt2>34/25\).
Consequently, for \(0\le t\le\varepsilon\),
\[
 F(t)\le F(\varepsilon)-m(\varepsilon-t).
\]
The binary-entropy maximum therefore gives
\[
\begin{split}
 \max_{0\le t\le\varepsilon}
    \{F(t)+\varepsilon\mathsf h(t/\varepsilon)\}
 &\le F(\varepsilon)+\varepsilon\log(1+e^{-m})\\
 &\le F(1/8)+\frac18\log(33/25).
\end{split}
 \tag{15}
\]
This elementary identity follows by differentiating
\(\mathsf h(s)-m(1-s)\); its maximum is
\(\log(1+e^{-m})\). It also holds at \(\varepsilon=0\).

For \(0<u\le1/8\), the sine series and
\(\log(1-v)\ge-v/(1-v)\) imply
\[
 \log(2\sin\pi u)\ge\log(2\pi u)-\frac{\pi^2u^2}{5}.
 \tag{16}
\]
Indeed \(\sin x\ge x(1-x^2/6)\), and \(x^2<1\) here.
Integration yields
\[
 J(1/8)\ge\frac18\{\log(\pi/4)-1\}-\frac{\pi^2}{7680}.
 \tag{17}
\]
Using \(\pi>25/8\), \(\pi^2<10\), and
\(\log(32/25)<7/25\), we obtain
\[
\begin{split}
 F(1/8)+\frac18\log(33/25)
 &\le\frac14+\frac18\log(66/25)
                 -\frac14\log(\pi/4)+\frac{\pi^2}{3840}\\
 &<\frac38+\frac7{100}+\frac1{384}
       =\frac7{15}-\frac{61}{3200}.
\end{split}
 \tag{18}
\]
Here \(\log(66/25)<1\), since
\(e>1+1+1/2+1/6=8/3>66/25\).
All the estimates are inequalities, not evaluations of an action.

Consider first \(C_{1,N}(X,Y)\), where \(|X|=1\) and \(Y\) is
as in (8). Each small-index row \(j/N\le\varepsilon\) is bounded
by the product of \(|p_j(X)|/S_j^2\) and (12); its chirp has
modulus one. Equations (11), (15), and (18) bound this block at
rate strictly below \(7/15\).
For \(j/N\ge\varepsilon\), (10), (12), and the existing complete
disk norm give
\[
 \sup_{|W|\le1}\sum_{j<N}\frac{|p_j(W)|}{S_j^2}
       \le C_\tau N^{B_\tau}e^{N(7/15+\tau)}.
 \tag{19}
\]
Thus
\[
 \sup_{|X|=1}|C_{1,N}(X,Y)|
       \le C_\tau N^{B_\tau}e^{N(7/15+\tau)}
                       \quad(7/8\le y\le1).
 \tag{20}
\]
The identical split applies to \(C_{1,N}(Y,Z)\) for \(|Z|\le1\),
because its incoming chirp also has modulus one. In particular,
every actual type-four target in (2) is covered:
\[
 |C_{1,N}(Y,Z)|\le C_\tau N^{B_\tau}e^{N(7/15+\tau)}.
 \tag{21}
\]
The tolerances in the separate factors can be chosen to sum to
the displayed \(\tau\). All indices through \(N-1\) are retained.

## 4. Attach an ordinary three

For a type-three output put \(C=\log_+|Z|\).
By (2),
\[
             C\le17\pi/125<3/7,\qquad
             |p_j(Z)|\le(2e^C)^j.
 \tag{22}
\]
The small-index part of \(C_{0,N}(Y,Z)\) therefore has rate at most
\[
\begin{split}
 t\log2-J(t)+Ct+A_\varepsilon(t)
 &\le2\varepsilon\log2-J(\varepsilon)+C\varepsilon\\
 &\le\frac14\log2-J(1/8)+\frac{3}{56}.
\end{split}
 \tag{23}
\]
Here \(\mathsf h\le\log2\), and \(J\) is decreasing on
\([0,1/8]\). Equations (17), \(\log2<7/10\), and the same
rational bounds used above show that (23) is less than
\[
 \frac7{40}+\frac18+\frac7{200}+\frac1{768}+\frac3{56}
 <\frac25.
 \tag{24}
\]
For clarity, the last positive difference is
\(2/175-1/768=1361/134400\).
The bound \(\log2<7/10\) follows from the positive exponential
series, as in the low-index kernel source.

The other indices again have quotient rate at most zero. Section 2
of that source supplies the complete disk bound
\[
 \sup_{|Z|\le e^{17\pi/125}}
       \sum_{j<N}\frac{|p_j(Z)|}{S_j}
       \le C_\tau N^{B_\tau}e^{N(1271/2500+\tau)}.
 \tag{25}
\]
Its proof concerns every row on the output disk. No physical
incoming support or termination from its separate low-index
statement is used. Since \(2/5<1271/2500\), (23)--(25) give
\[
 |C_{\beta,N}(Y,Z)|
 \le C_\tau N^{B_\tau}e^{N(m_\beta+\tau)},\qquad
 m_0=1271/2500,\quad m_1=7/15,
 \tag{26}
\]
for the whole actual output families and \(7/8\le y\le1\).

## 5. Complete first contraction and both second weights

The complete-message seam theorem, Sections 2--3, proves on the
entire first circle
\[
\begin{split}
 |U_{1,N}(w,X)|&\le C_\tau N^{B_\tau}
                  e^{N(b_1+c_{\rm b}+\tau)},\\
 |d_N(X)|&\le CN^B e^{Nc_{\rm b}/2},\\
 b_1&=433/500,\qquad c_{\rm b}=-2J(1/6)<13/40.
\end{split}
 \tag{27}
\]
These estimates retain the coherent endpoint coefficients,
their true endpoint groups, and all first Fourier weights.
The cap bound holds on the full real ordinary-color interval and
on a sufficiently small fixed complete-color disk, with any
prescribed rate allowance.

Evaluate the coefficient (3) on the full real first period.
Then \(|1+X^{-N}|\le2\), and (20), (27), including the original
first \(N\) density, imply
\[
 |f_N(w,Y)|\le C_\tau N^{B_\tau}e^{N(B_{44}+\tau)},\qquad
 B_{44}=b_1+\frac32c_{\rm b}+\frac7{15},
 \quad 7/8\le y\le1.
 \tag{28}
\]
The factor two used in this upper estimate does not alter the
exact physical identity (3).

The whole diagonal polynomial obeys, for every \(\tau>0\),
\[
             |d_N(e^{-2\pi iy})|
                    \le C_\tau N^{B_\tau}e^{N\tau},
                         \qquad 7/8\le y\le1.
 \tag{29}
\]
On each compact subinterval away from one, the absolute Fourier
bound gives rate \(\max\{-J(y),0\}=0\), since \(J(y)\ge0\).
At the endpoint use the exact identities from the seam theorem
\[
 d_N(Y)=\frac1N\sum_{j<N}\frac{p_j(Y)}{P_j},\qquad
 \frac{|p_j(Y)|}{S_j}\le e^{N\Omega(\delta)}
                         \quad(|Y-1|\le\delta),
 \tag{30}
\]
where
\[
 \Omega(\delta)=\log(1+\delta/2)
              +\frac{\delta}{2}\log(1+2/\delta)\longrightarrow0.
\]
Choose \(\delta\) for the prescribed allowance and cover the
remaining compact arc. This proves (29) including \(Y=1\),
without assuming a relative factorial approximation there.
Both second monomials have exactly unit modulus on the real arc:
\(|Y^{-\sigma N}|=1\).

Equations (26), (28), and (29) now bound the entire density (4):
\[
 |\mathscr D_{\sigma,\beta,N}(w,Y,Z)|
 \le C_\tau N^{B_\tau}e^{N(B_{44}+m_\beta+\tau)},
                         \qquad 7/8\le y\le1.
 \tag{31}
\]
Every row is present before taking this upper bound. In particular,
the proof neither takes a modulus of a truncated first message nor
substitutes its local asymptotic for the complete polynomial.

## 6. Original calibration and integrated arc

The adopted three-factor affine-floor theorem gives, on exactly (1),
\[
             \Lambda_{123}(z)+\frac{\beta}{2}\Re g(z)>\frac73.
 \tag{32}
\]
The original cap constants and (26) satisfy
\[
 B_{44}+m_\beta
 <\frac{433}{500}+\frac{39}{80}+\frac7{15}
                       +\frac{1271}{2500}
 =\frac73-\frac{143}{30000},\qquad
 \frac{143}{30000}>\frac1{250}.
 \tag{33}
\]
For \(\beta=1\), the actual third height is negative and
\(\Re g(z)<0\). The full Fourier absolute bound therefore gives
\[
 D_{1,N}(Z)\le C_\tau N^{B_\tau}
                    e^{N\{-\Re g(z)/2+\tau\}}.
 \tag{34}
\]
For \(\beta=0\), its multiplier is identically one.
Choose a common fixed ordinary-color disk and all finite-source
tolerances so that their total allowance is less than \(1/1000\).
Equations (31)--(34) imply (6), since
\[
             \frac{143}{30000}-\frac1{1000}>\frac1{500}.
\]
All choices precede \(N\). Fixed ordinary derivatives follow by
Markov's inequality on the real color interval and Cauchy's
formula on smaller fixed disks; the color degree is at most \(N-1\).
These arguments change only polynomial prefactors.

Integration on this real interval with the original \(+N\,dy\)
also changes only a polynomial prefactor. The first \(N\) was
already retained in (28); no new sampling or Gram factor is
introduced. Both second currents, and hence their sum on this
arc, satisfy the same gap.

This closes the real second interval \([7/8,1]\) with the complete
\(f_{44,N}\) in either second sector. It does not bound a join from
the old selected or unselected second height to this interval,
nor the intervening real interval to its left. The original
action, marking, and remaining contour obligations are unchanged.

## Direct source versions

The proof uses the following directly checked implications:

* Pointwise prefix replacement, Section 1: the original complete
  first coefficient, its physical identity, degree and scalar.
* Complete-message seam collar, Sections 1--5: actual third
  domains, the original allocation, complete cap/first diagonal
  bounds (27), exact endpoint bound (30), color scope and parity.
* Transformed real-initial interval, equation (4) and equations
  (13)--(15): the zero-safe product method and the complete
  own-four disk norm. Its small-angle profile is not imported.
* Low-index kernel margin, Section 2 and equation (7): both
  all-row disk norms and typed radii. Its physical terminating
  input hypothesis is not used.
* Fourier-weight continuation, Section 5: absolute whole diagonal
  bounds and the original negative-height sign of \(\Re g\).
* Three-factor affine floor, Theorem and complete proof:
  the original action inequality (32), with the outgoing
  halfweight on its original side.

| Source | SHA-256 |
|---|---|
| research_mixed_four_four_pointwise_prefix_replacement.md | 2a4a86ced4bb326baa2ca24bfd6f9c6846103070f4a0731f663ef6d2303a89b7 |
| research_mixed_complete44_second_period_seam_collar.md | e203f8041ddcc3c002d09de0a5d94a458f2499a3f55325fce27126c3c7b66a6c |
| research_mixed_transformed_real_initial_interval.md | c6b2ae80f47dfcc113a823f8c883fed54c7c1d06d6dfb8ed945bbb16744bcc9c |
| research_mixed_next_low_index_kernel_margin.md | 35de8662e57070a4f19aef409f82c921283493ba3f0e17268f1c11a7eac1738c |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_complete44_three_factor_affine_floor.md | 112f3b5a8d40c7a3bb770b8deae7b189c4729235851d8a2036f8869edc332b7d |

Author full proof readback and all six direct-source implication
reads and hash checks are complete. Independent full proof and
direct-source review is required before adoption. No mathematical
numerical evaluation, test, import, compilation, or frozen-source
edit is used.
