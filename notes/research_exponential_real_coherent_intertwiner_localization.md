# Exponential localization of the actual root intertwiners on the compact coherent cycle

Private written proof, 18 November 2026.

Exact intertwining by a bounded family of trace observables gives
an exponential estimate on the original real compact coherent cycle.
Two configurations with separated observable values have an
exponentially small kernel entry, relative to the norm of the full
intertwiner. The estimate applies to the actual root operator
\(T(1)\) and the Laurent residue of the opposite-polarization
kernel. It does not apply to its inhomogeneous finite part without
retaining the normal forcing.

This is a relative norm estimate. Neither the norm on the right
nor continuation to a complex geometric saddle is estimated here.
Consequently it is not a new volume-conjecture case.

The sole complete direct is S, the finite trace-separator proof,
pinned below. The analytic estimate is proved directly from the
finite matrices; no coherent-kernel asymptotic theorem is imported.

## 1. The finite Hilbert spaces and the assertion

Put \(d=N-1\), \(q=e^{\pi i/N}\), and \(Q=q^2\).
On one actual head use the basis \(w_a\), \(0\le a\le d\),
with squared norms \(\binom da^{-1}\). Thus
\[
 u_a=\sqrt{\binom da}\,w_a
\]
is orthonormal. The normalized coherent vector is
\[
 \psi_z=(1+|z|^2)^{-d/2}
                 \sum_{a=0}^d\sqrt{\binom da}\,z^a u_a.
 \tag{1}
\]
Use tensor products on a fixed number of heads. All norms below
are these actual binomial Hilbert norms.

A bounded word family means a fixed finite sum of words in
\(E_i,F_i,K_i^{\pm1}\), of degree bounded independently of \(N\),
whose scalar coefficients are holomorphic in \(h=1/N\) near zero.
The \(M=1\) head matrices are
\[
 Ew_a=(Q^{-a}-1)w_{a-1},\quad
 Fw_a=(1-Q^{a+1})w_{a+1},\quad
 Kw_a=-q^{-1}Q^{-a}w_a,
 \tag{2}
\]
with the actual zero extreme arrows. For a bounded word \(O_N\),
write \(o(z)\) for its principal coherent value on the real cycle
\(w=\bar z\), as computed in S. Its substitution is
\[
 p=\frac{|z|^2}{1+|z|^2},\qquad
 E=\bar z^{-1}(e^{-2\pi ip}-1),\quad
 F=\bar z(1-e^{2\pi ip}),\quad K=-e^{-2\pi ip}.
 \tag{3}
\]
For several heads this substitution is made on each head.

**Proposition.** Fix compact parameter sets in
\((\mathbb C^\times)^{r_+}\) and
\((\mathbb C^\times)^{r_-}\), and bounded word families
\(O_{+,N},O_{-,N}\). Suppose an arbitrary finite matrix \(L_N\)
between the corresponding head spaces satisfies
\[
                       O_{+,N}L_N=L_NO_{-,N}.
 \tag{4}
\]
For every fixed \(\eta>0\) there are \(C,c>0\), independent
of \(N,L_N,y,z\), such that
\[
 |o_+(y)-o_-(z)|\ge\eta
 \quad\Longrightarrow\quad
 |\langle\psi_y,L_N\psi_z\rangle|
                  \le C e^{-cN}\|L_N\|.
 \tag{5}
\]
The compact sets avoid the coordinate poles, not a hidden
state-index cutoff. Their closure lies in finite affine
coherent charts. No self-adjointness of \(O_\pm\) or
positivity of \(L_N\) is required.

## 2. Conjugating a bounded word to analytic finite differences

For a fixed coherent vector set \(t=a/N\) and \(h=1/N\).
Represent a vector as \(\psi_z(a)H(a/N)\), where \(H\)
is holomorphic on a neighborhood of \([0,1]\).
Taking ratios of consecutive coefficients in (1) gives
the following exact action on the actual sampled vector:
\[
 \begin{split}
 \mathcal E_{z,h}H(t)
   &=z\,\frac{(1-h-t)(e^{-2\pi i(t+h)}-1)}{t+h}
                                                   H(t+h),\\
 \mathcal F_{z,h}H(t)
   &=z^{-1}\frac{t(1-e^{2\pi it})}{1-t}H(t-h),\\
 \mathcal K_{z,h}H(t)
   &=-e^{-\pi ih}e^{-2\pi it}H(t).
 \end{split}
 \tag{6}
\]
The quotients in this display have removable singularities
at \(t=-h\) and \(t=1\), respectively. They are uniformly
holomorphic and bounded on any fixed bounded complex
neighborhood of the real interval for small \(h\).
At the top sample \(t=d/N\) the first coefficient is zero;
at the bottom sample \(t=0\) the second is zero. Thus no
sample outside the actual finite interval is used, whatever
holomorphic extension of \(H\) is chosen.

The adjoint matrices also have exact analytic rows:
\[
 \begin{split}
 \mathcal E^*_{z,h}H(t)&=
                  z^{-1}(e^{2\pi it}-1)H(t-h),\\
 \mathcal F^*_{z,h}H(t)&=
                  z(1-e^{-2\pi i(t+h)})H(t+h),\\
 \mathcal K^*_{z,h}H(t)&=
                  -e^{\pi ih}e^{2\pi it}H(t).
 \end{split}
 \tag{7}
\]
Again the coefficients vanish at the forbidden samples.
These formulas follow directly from the orthonormal
matrix coefficients, rather than from a formal transpose
of an infinite difference operator.

By composing (6), or (7) in reversed word order, any
bounded word and its adjoint act on amplitudes as
\[
 \mathcal O_{z,h}H(t)
       =\sum_{s\in\mathcal S}b_s(t,z,h)H(t+hs).
 \tag{8}
\]
In several heads, \(s\) is an integer vector and \(t\)
lies in a fixed-dimensional cube. The finite set
\(\mathcal S\) is fixed independently of \(N\).
The coefficients are uniformly holomorphic and bounded
on one fixed complex neighborhood of that cube, uniformly
for \(z\) in the specified compact set. This follows
from the removable formulas (6)--(7); it does not require
a long-word symbol bound.

Set
\[
 a_z(t)=\sum_s b_s(t,z,0),\qquad
 p_z=\left(\frac{|z_i|^2}{1+|z_i|^2}\right)_i.
 \tag{9}
\]
Substitution into (6) shows \(a_z(p_z)=o(z)\).
For the adjoint it gives \(\overline{o(z)}\).
The latter is verified for each generator in (6)--(7);
products follow because the shifts tend to the identity
and the principal values commute. Also, uniformly on a
slightly smaller fixed complex neighborhood,
\[
 \left|\sum_s b_s(t,z,h)-a_z(p_z)\right|
                            \le C(|t-p_z|+h).
 \tag{10}
\]
Here and below coordinate distances may be taken in
the maximum norm.

## 3. Analytic powers near the binomial mean

Let \(\mathcal D=\mathcal O_{z,h}-o(z)\).
Fix an integer \(1\le k\le\delta N\), and put
\[
                         \rho=A\sqrt{k/N}.
 \tag{11}
\]
The constants \(A\) will be chosen large and then
\(\delta\) small. Choose them so that the polydisk of
radius \(2\rho\) about \(p_z\) lies in the fixed
coefficient neighborhood. Between radii \(2\rho\)
and \(\rho\), use \(k\) nested polydisks with radius
decrement \(\rho/k\).

Write (8) as its multiplication part plus
\(\sum_s b_s(t)(H(t+hs)-H(t))\). If
\(h\max_s|s|\le\rho/(2k)\), the segment of each shift
stays within half of the next radius decrement.
Cauchy's derivative estimate and (10) therefore give,
from one such polydisk to the next,
\[
 \|\mathcal D H\|
       \le C\left(\rho+h+\frac{k}{N\rho}\right)\|H\|.
 \tag{12}
\]
The constants are uniform in \(z,N,k\).
The shift condition and all domain inclusions hold
for \(k/N\le\delta\), once \(\delta\) is small
depending on \(A\) and the fixed word.
Consequently, for every \(0\le j\le k\),
\[
 \sup_{|t-p_z|\le\rho}|\mathcal D^j1(t)|
       \le q_\delta^{\,j},\qquad
 q_\delta=C(A+A^{-1}+1)\sqrt\delta.
 \tag{13}
\]
For \(j<k\) the same nested domains with \(k\)
steps are used, so this is a common bound on
the same final polydisk for every \(j\).

There is a separate global bound. On a fixed
complex tube about the whole cube, all coefficients
in (8) are bounded. Shrink this tube by
\(h\max_s|s|\) at each application. For
\(k\le\delta N\) the full shrinkage fits in
a fixed larger tube. The triangle inequality gives
\[
                \sup_{t\in[0,1]^r}
                       |\mathcal D^j1(t)|\le C_0^j
                              \quad(0\le j\le k).
 \tag{14}
\]
The constant \(C_0\) is fixed before \(A,\delta\)
are chosen. It can also bound all the adjoint
and left/right families under consideration.

## 4. From analytic powers to Hilbert-space powers

The squared coefficients of \(\psi_z\) in (1)
are independent binomial probabilities on the
different heads:
\[
 \mathbb P(a_i=b)
    =\binom db p_i^b(1-p_i)^{d-b}.
 \tag{15}
\]
Their means as variables \(a_i/N\) are
\((1-h)p_i\). For completeness an exponential
tail bound follows from the Bernoulli generating
function. The second derivative of
\(\log(1-p+pe^\lambda)\) is at most \(1/4\)
for real \(\lambda\). Integrating twice shows
that the centered generating function of a
sum of \(d\) Bernoulli variables is at most
\(e^{d\lambda^2/8}\). Markov's inequality,
optimized in \(\lambda\), and a union bound
over the fixed number of heads imply
\[
 \mathbb P\bigl(|a/N-p_z|>\rho\bigr)
                     \le C_1e^{-c_1N\rho^2},
 \tag{16}
\]
provided \(h\le\rho/2\), after reducing \(c_1>0\)
if necessary. The \(O(h)\) shift of the mean
has thus been included.

Equations (13)--(16), applied to the exact
sampled vector, prove
\[
 \|(O_N-o(z))^j\psi_z\|
    \le q_\delta^{\,j}
          +C_2 C_0^j e^{-c_2 A^2 k},
                        \qquad 0\le j\le k .
 \tag{17}
\]
The same statement holds for
\((O_N^*-\overline{o(z)})^j\).
By choosing \(A\) sufficiently large, the
second term is bounded by \(C_2e^{-Bk}\)
for any prescribed fixed \(B>0\).
After that choice, taking \(\delta>0\)
sufficiently small makes \(q_\delta\)
arbitrarily small. All choices are uniform
on the compact coherent parameter sets.

## 5. Proof of the intertwiner estimate

Put \(a=o_+(y)\), \(b=o_-(z)\),
\(A_N=O_{+,N}-aI\), and
\(B_N=O_{-,N}-bI\). Equation (4) gives
\[
             (a-b)L_N=L_NB_N-A_NL_N.
\]
Left and right multiplication commute.
Iterating this identity exactly and then
taking the coherent matrix entry gives
\[
 \begin{split}
 |a-b|^k|\langle\psi_y,L_N\psi_z\rangle|
 \le \|L_N\|\sum_{j=0}^k\binom kj
       \|(A_N^*)^j\psi_y\|\,
       \|B_N^{k-j}\psi_z\|.
 \end{split}
 \tag{18}
\]
There has been no division by a matrix spectrum.

Use (17) simultaneously on both sides.
For one common constant \(C_3\), the sum
in (18) is at most
\[
 (2q_\delta)^k
   +C_3e^{-Bk}(1+q_\delta)^k
   +C_3e^{-2Bk}2^k.
 \tag{19}
\]
First choose \(B\) large compared with
\(\log(1+\eta^{-1})\); choose \(A\)
accordingly in (17). Then choose
\(\delta>0\) small enough that
\(q_\delta<\min(1/4,\eta/4)\), as well as all
the preceding domain conditions.
With \(k=\lfloor\delta N\rfloor\),
(18)--(19), divided by \(\eta^k\),
prove (5) for large \(N\).
The finitely many remaining levels are
absorbed in \(C\).

This proof supplies exponential rather
than only inverse-polynomial localization.
Its exponential constant depends on the
fixed observable gap and the compact
charts; it is not asserted to exceed any
hyperbolic volume or global norm exponent.

## 6. Separated real windows

There is an operator version of (5).
On one coherent sphere let
\[
 d\mu(z)=\frac{d\Re z\,d\Im z}{\pi(1+|z|^2)^2}.
\]
It has total mass one and satisfies
\[
                         N\int |\psi_z\rangle
                                      \langle\psi_z|\,d\mu(z)=I.
 \tag{20}
\]
Indeed the angular integral makes its matrix diagonal.
The radial integral for its \(a\)-th diagonal entry is
\(\binom da\int_0^\infty t^a(1+t)^{-d-2}\,dt=1/N\).
Repeated integration by parts gives this beta
integral directly. Tensor products prove (20) on
any fixed number of heads.

For measurable real windows \(\mathcal C,\mathcal D\)
inside the compact charts of the proposition, define
their actual positive partial resolutions by
\[
 P_{\mathcal C}
   =N^{r_+}\int_{\mathcal C}|\psi_y\rangle
                       \langle\psi_y|\,d\mu^{[r_+]}(y),
 \quad
 P_{\mathcal D}
   =N^{r_-}\int_{\mathcal D}|\psi_z\rangle
                       \langle\psi_z|\,d\mu^{[r_-]}(z).
 \tag{21}
\]
They are positive contractions by (20).
If the gap in (5) holds for every
\((y,z)\in\mathcal C\times\mathcal D\), then
\[
       \|P_{\mathcal C}L_NP_{\mathcal D}\|_1
       \le C N^{r_++r_-}e^{-cN}\|L_N\|.
 \tag{22}
\]
Here \(\|\cdot\|_1\) is the nuclear norm, also
for a rectangular map. To prove this, multiply
the two rank-one integrals in (21). Their
integrand is
\[
 |\psi_y\rangle\langle\psi_y,L_N\psi_z\rangle
                                                 \langle\psi_z|.
\]
Its nuclear norm is the modulus of its middle
scalar, since both outer vectors have norm one.
Integrating (5) proves (22); both window
measures are at most one. A finite trace
network containing this transition is therefore
bounded by the right side of (22) times the
norms of its other factors. Those other norms
are not estimated by this assertion.

## 7. Application to the actual source kernels and its limits

S supplies a finite family of bounded
reduced trace observables \(O_I,O_I^\vee\),
and the exact root rows
\[
 O_I L_N=L_NO_I^\vee,\qquad
 K_0L_N=L_NK_0^{-1}
 \tag{23}
\]
for both \(L_N=T(1)\) and
\(L_N=\operatorname{Res}_{u=0}J(e^u)\).
The last Cartan pair is also a bounded
word family. Applying (5) to a member
whose classical values have a fixed
gap proves exponential suppression
outside these character-matching
relations on the real compact charts.
On irreducible trace charts, S identifies
the matching tuples up to their one
common conjugation and states the
reciprocal selected total-product flag.

This does not require a Fourier-integral
phase for \(L_N\). It does not construct
one. A bound \(e^{-cN}\|L_N\|\) can
still be exponentially large if the
unknown norm exponent is larger than
\(c\). Nor does a bound on the real
compact cycle bound a continued kernel
on a complex geometric saddle.

In particular the proof has not
discarded the endpoint terms of a
meridian derivative. For the finite
part \(J_0\), S gives instead
\[
 O_{I,0}J_0-J_0O^\vee_{I,0}
       =-O_{I,1}\mathsf R-\mathsf R O^\vee_{I,1}.
 \tag{24}
\]
Those normal terms are not bounded-word
homogeneous equations. Formula (18)
would acquire their iterated forcing.
No estimate for them, for the original
source's full first jet, or for a
geometric relative-window coefficient
is inferred from (5).

The result is an analytic estimate for
the exact original root operator and
residue on their compact coherent
cycle. The finite-exception volume
theorem remains open.

There is an explicit reason that the real
estimate must not be used as a pointwise
complex-symbol estimate. On a single head
let \(P=|w_d\rangle\langle w_0|\).
It has norm one and \(FP=0\) exactly.
Its normalized algebraic coherent kernel is
\[
 \sigma_P(w,z)=\frac{w^d}{(1+wz)^d}
                      =(v+z)^{-d},\qquad v=1/w.
 \tag{25}
\]
On the resolved nonincident chart point
\((v,z)=(0,1)\), it equals one at every
level. Direct summation of the actual
\(F\) matrix gives
\[
 \sigma_F(w,z)
   =w\left[1-Q
       \left(\frac{1+Qwz}{1+wz}\right)^d\right],
 \qquad
 \left.\sigma_F\right|_{v=0}
                =\frac{d(1-Q^{-1})}{z}.
 \tag{26}
\]
For the second equality, expand the bracket
to first order in \(v\) and use \(Q^{d+1}=1\).
Its limit at \((v,z)=(0,1)\) is \(2\pi i\),
whereas \(\sigma_{FP}=0\). The limiting
bounded root symbols there have \(K=-1,E=0\)
and \(F=2\pi i\), a noncentral parabolic
row in the triangular holonomy coordinates.

Thus multiplying a bounded-observable
covariant symbol by this endpoint kernel
does not describe their operator product
at that complex point. This example does
not compute an actual geometric source
contribution. It shows why neither the
real-window estimate nor noncentrality
alone removes the actual endpoint
normal terms after complex continuation.

## Complete proof direct

S: notes/research_finite_trace_separator_and_opposite_characteristic.md,
SHA256 1d5abd4e14df7aa32f17405e27543a35d815c130903ed379ab9c60bec2eef0f6.

The complete matching direct was read
nontruncated in this active author
sequence. Only written mathematics
and text/hash operations were used.
Frozen and public files were not
changed.
