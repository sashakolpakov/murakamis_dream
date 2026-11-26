# Own-four high rows and the complete early first 3,4 pair

Research deduction, 10 November 2026. At every actual fixed early
height, the entire upper physical row block of an adjoining type-four
factor is bounded by its continuous half-row or last-row rate. This
holds with either first type. The additional own-four factorial pays
the nonzero reflected drift; no unimodality or choice of a stationary
row is assumed.

For an initial \(3,4\) pair, both endpoint rates can be calibrated
with the complete cap. The already proved low and central estimates
then give a strict bound for the literal complete first pair. The
remaining word, selected first weights and changing-height outer
joins are separate.

## 1. Literal source and actual height range

Fix an actual positive three/four open word of length at least three.
Let its first two types be \(3+\alpha,4\), \(\alpha=0,1\). Keep the
original reference coordinates
\[
 a_*=a_0+ic,\qquad b_*=b_0+id,\qquad s_*=s_0+ih_0,
\tag{1}
\]
where the second vertex is ordinary and \(s_*\) is its private index.
The actual endpoint and ordinary-image bounds, with the attached-four
height improvement, give
\[
 c>-39/500,\quad c<21/1000,\qquad d<0,\quad h_0<0.
\tag{2}
\]
First type three has the stronger \(c>-9/125\). First type four has
\(c<-1/50\). These are necessary bounds on the same actual geometric
reference. No arbitrary point of an independent containing box is
used as a reference.

Set
\[
 a=x+ic,\quad b=z+id,\qquad
 1/10\le x\le11/50,\quad 11/50\le z\le9/20.
\tag{3}
\]
The heights in (3) are unchanged. Write
\[
\begin{gathered}
 r_N=e^{-2\pi i/N},\quad X=e^{-2\pi ia},\quad Y=e^{-2\pi ib},
 \qquad P_j=(r_N;r_N)_j,\\
 R_{j,N}(a,b)=X^{-j}
       \frac{(r_NX;r_N)_j(r_NY;r_N)_j}{P_j^3},
 \qquad
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}R_{j,N}(a,b).
\end{gathered}
\tag{4}
\]
These are the original complete ordinary rows. Their signs, chirp,
denominator and stopping index have not been altered.

Let \(J(0)=0\), \(J'(t)=\log(2\sin\pi t)\) on \(0<t<1\).
The full unallocated absolute row rate is
\[
\begin{split}
 E_1(s;a,b)={}&
 \int_0^s\log|1-e^{-2\pi i(a+t)}|\,dt
 +\int_0^s\log|1-e^{-2\pi i(b+t)}|\,dt\\
 &-3J(s)-2\pi cs,\qquad 0\le s\le1.
\end{split}
\tag{5}
\]
All logarithmic zeros are integrated. Original Fourier allocations
add constants independent of \(s\), so the row comparisons below
retain them exactly.

Use the original radial primitive
\[
 G_H(t)=\Re g(t-iH),\qquad
 G_H'(t)=f_H(t)=\log|1-e^{-2\pi H-2\pi it}|,\quad H\ge0.
\tag{6}
\]
As proved in the
[right-tail reflection source](research_mixed_right_tail_reflection.md),
\(G_H\) is odd and one-periodic,
\[
 J(t)\le G_H(t)\le0\quad(0\le t\le1/2),
\tag{7}
\]
and \(f_H\) is even and increases with \(|t|\) on
\([-1/2,1/2]\). The original reciprocal-radius identity gives
\[
\begin{split}
 \Phi_1(v)&:=E_1(1-v)-E_1(1)\\
 &=G_{|c|}(x-v)-G_{|c|}(x)
   +G_{|d|}(z-v)-G_{|d|}(z)+3J(v)-\lambda v,\\
 \lambda&=2\pi\{(-c)_++d_+\}=2\pi(-c)_+,\qquad E_1(1)=\lambda.
\end{split}
\tag{8}
\]
In particular the actual heights imply
\[
 0\le\lambda<\frac{39\pi}{250}
                  <\frac{429}{875}<\frac12.
\tag{9}
\]
Here only \(\pi<22/7\) and the rational height bound (2) are used.
The drift is neither omitted nor varied independently of the radii.

## 2. A complete half/last-row principle

**Theorem 1.** Under (2)--(3),
\[
 \max_{1/2\le s\le1}E_1(s;a,b)
             =\max\{E_1(1/2;a,b),E_1(1;a,b)\}.
\tag{10}
\]
The proof uses only \(d\le0\), \(c>-39/500\), and the real
intervals in (3), so it applies to either first type.

*Proof.* Put \(v_0=11/50\). First take \(0\le v\le v_0\).
Among intervals of length \(v\) contained in \([-1/2,1/2]\),
the integral of the even increasing function \(f_H\) is minimized
by the centered interval. For a direct proof, translate an interval
by its center; the derivative of its integral is the difference
of the endpoint values, and has the sign of the center.
The interval \([x-v,x]\) in (3) is in this domain. Thus
\[
\begin{split}
 G_{|c|}(x-v)-G_{|c|}(x)
 &=-\int_{x-v}^{x}f_{|c|}(t)\,dt\\
 &\le-2G_{|c|}(v/2)\le-2J(v/2).
\end{split}
\tag{11}
\]
Also \(v\le v_0\le z\le1/2\), so monotonicity on the positive
half-period gives
\[
 G_{|d|}(z-v)-G_{|d|}(z)
 \le-G_{|d|}(v)\le-J(v).
\tag{12}
\]
These arguments remain valid at zero height by integration through
the logarithmic zero. Inserting (11)--(12) in (8) gives
\[
             \Phi_1(v)\le2[J(v)-J(v/2)]-\lambda v.
\tag{13}
\]
The function \(\log(2\sin\pi t)\) is strictly concave on \((0,1)\).
Jensen's inequality on \([v/2,v]\) therefore gives, for \(v>0\),
\[
 J(v)-J(v/2)
 \le\frac v2\log\bigl(2\sin(3\pi v/4)\bigr)<0,
\tag{14}
\]
because \(v\le11/50<2/9\). At \(v=0\) the expression is zero.
Thus the whole range \(0\le v\le v_0\) is bounded by the last rate.

For \(v_0\le v\le1/2\), use the separately proved all-angle
leg inequality,
\[
 G_H(x-v)+J(v)+G_H(1/2-x)\le0,
 \qquad 0<x<1/2,\quad0\le v\le1/2.
\tag{15}
\]
This is Lemma 1 of the
[all-angle high-row source](research_mixed_all_angle_high_row_sign_class.md);
its proof has no height-sign restriction. Subtracting the half-row
instance of (8) and applying (15) to both legs yields
\[
 \Phi_1(v)-\Phi_1(1/2)
               \le J(v)+\lambda(1/2-v).
\tag{16}
\]
The remaining \(J(v)\) is exactly the contribution of the third
own factorial.

Since \(J''(v)=\pi\cot\pi v\ge0\) on \((0,1/2]\) and
\(J(1/2)=0\), the chord bound is
\[
 J(v)\le\frac{1/2-v}{1/2-v_0}\,J(v_0).
\tag{17}
\]
Here the size of the negative chord is sufficient for every drift
in (9). To prove this without a numerical value, \(J\) increases
on \([1/6,1/2]\), and \(v_0<1/4\), whence
\[
 -J(v_0)>-J(1/4)
 =\frac1{2\pi}\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)^2}
 >\frac4{9\pi}.
\tag{18}
\]
The equality follows by integrating the radial logarithm Fourier
series and taking its Abel limit. The integrated series is absolutely
convergent. Its alternating-series lower bound is the first two
terms \(1-1/9\); no value of the sum has been evaluated. Therefore
\[
 -\frac{J(v_0)}{1/2-v_0}
 >\frac{100}{63\pi}>\frac{50}{99}>\frac12>\lambda.
\tag{19}
\]
Equations (16)--(19) bound the second range by the half-row rate.
Both endpoints \(s=1/2,1\) belong to the continuous interval, proving
(10). No derivative or nondegeneracy of a maximizing row was used.
\(\square\)

Theorem 1 does not assert that the finite last row has index \(N\),
or that the finite half-row is nonzero. Its endpoints are continuous
absolute rates of the unchanged full products.

## 3. Every finite high row, including the true ends

**Corollary 2.** For every \(\tau>0\), uniformly on the actual
parameter families in (1)--(3), both parities satisfy
\[
 \sum_{j=\lceil N/2\rceil}^{N-1}|R_{j,N}(a,b)|
 \le C_\tau N^{A_\tau}
       \exp N\{\max(E_1(1/2;a,b),\lambda)+\tau\}.
\tag{20}
\]

*Proof.* Use the full-index product estimate in Section 2 of the
[contour-allowance source](research_mixed_conditional_contour_allowance.md),
with the zero-safe extension written out in Corollary 3 of the
all-angle source. Replace each numerator logarithm by
\(\log(|1-e^{-2\pi i(a+t)}|+\delta)\), and likewise for \(b\).
For fixed \(\delta>0\) its Riemann-sum error is uniform. The
integral error tends uniformly to zero as \(\delta\downarrow0\);
only simple real zeros are possible, with local error
\(O(\delta(1+|\log\delta|))\). The original sine-factorial denominator
has uniform endpoint error \(O(\log N)\) for all \(j<N\).
The chirp contributes exactly the last term of (5).

Consequently every physical row has upper rate \(E_1(j/N)+\tau/2\)
with a polynomial prefactor. Apply (10) and sum at most \(N\) rows.
The physical supports and the estimates are unchanged at odd level.
There is no division by a vanishing Newton or Fourier factor.
\(\square\)

## 4. Calibrating both rates for the first 3,4 pair

Now assume \(\alpha=0\). Use the original complete cap
\(U_{0,N}(w,X)\) and reciprocal-factorial polynomial \(d_N\).
Keep the original phase definitions
\[
\begin{split}
 \Xi_0(e,a)&=S(e)+J(e+a)-J(a)-i\pi ea,\\
 F_{01}(s;a,b)&=
 g(s+a)+g(s+b)-3g(s)+2\pi ias-g(a)-\tfrac32g(b),\\
 L_0(a)&=\operatorname{stat}_e\Xi_0(e,a),\qquad
 \phi_{01}(a,b)=\operatorname{stat}_s F_{01}(s;a,b).
\end{split}
\tag{21}
\]
Here \(S\), \(g\), all critical sheets, and their additive constants
are exactly those in the
[joint low- and half-index theorem](research_mixed_early_joint_low_tail.md).
In particular
\[
             L_0'(a_*)+\partial_a\phi_{01}(a_*,b_*)=0.
\tag{22}
\]
Put \(\kappa=1/2500000\) and
\[
\begin{split}
 \Gamma(z)={}&\Re L_0(a_*)+\Re\phi_{01}(a_*,b_*)\\
 &+\Re\partial_b\phi_{01}(a_*,b_*)(z-b_0)
                                      -\kappa(z-b_0)^2,\\
 \gamma_*&=\kappa(a_0-11/50)^2>0.
\end{split}
\tag{23}
\]
The actual first-three interval has \(a_0> .278>11/50\) and
\(a_0<.391\). In particular \(2\gamma_*<1/2000\).
Neither the remaining slope nor the action in (23) is adjusted to
fit this comparison.

The complete cap profile plus the continuous allocated half-row
rate is already at most \(\Gamma(z)-1/2000\), by equation (23)
of the joint low-/half-row theorem. That statement includes all
five complex cap profiles, its true index ends and the possible
positive-height upper-row allowance. It is a rate statement,
not a comparison to a finite half-row value.

It remains to calibrate the last-row alternative when \(c\le0\).
The [fixed-height complete cap source](research_mixed_cap_early_fixed_height_full_source.md)
has five profiles: the main private horizontal, the two real cuts,
and the two horizontal aliases. Each is a value or maximum of
\(\Re\Xi_0(e,a)\) minus an \(x\)-independent alias penalty, with
\[
                  e\in E_c=[.27,.49]+i[-.055,.04].
\tag{24}
\]
Its possible extra physical-tail allowance is zero when \(c\le0\).
The allocated ordinary last-row rate is
\[
                       \lambda-\tfrac12\Re g(b),
\tag{25}
\]
which is independent of \(x\).

Write \(r=e^{2\pi c}\le1\), \(R=e^{2\pi\Im e}>2/3\),
\(u=\Re e\), \(N_e=|1-rR e^{-2\pi i(u+x)}|\), and
\(D=|1-r e^{-2\pi ix}|\). The original primitive, without
changing its lift, gives
\[
       \partial_x\Re\Xi_0(e,a)=\log(N_e/D)>0.
\tag{26}
\]
For completeness, the strict inequality follows from the original
angular bounds on (3), (24):
\[
\begin{split}
 N_e^2&>1+\tfrac49r^2+\tfrac8{25}r=:A_0,\qquad
 D^2<1+r^2-\tfrac9{25}r=:B_0,\\
 A_0-B_0&=r\left(\tfrac{17}{25}-\tfrac59r\right)>0.
\end{split}
\tag{27}
\]
These use
\(\cos(2\pi(u+x))<-6/25\), \(\cos(2\pi x)>9/50\),
proved in the joint low-row source by the rational sine witnesses.
Since \(r\le1\), the last expression is strictly positive.
The maximum over the fixed private interval therefore also increases
with \(x\). Thus each of the five cap profiles combined with (25)
is no greater than its value at \(x=11/50\).

The cap's true-end profile must be treated separately. At first
type three it is
\[
 E_{\rm end}(c)=3/5+2\pi c_++(\log4)/100.
\tag{28}
\]
It has no \(x\)-dependence, and neither does (25). Their sum
therefore transports unchanged. This conclusion does not follow
by applying (26) to an endpoint row.

At the comparison point \(x=11/50\), the
[complete cap-plane theorem](research_mixed_first_cap_plateau_completion.md)
bounds each of its five profiles and its true ends by the original
cap plane. The completed ordinary last-row comparisons in
[ordinary-source assembly](research_mixed_three_row_source_assembly.md)
bound (25), including every revived carrier, by its original ordinary
plane. The actual attached first input and ordinary or attached
right input lie in the domains stated there; in particular this
includes the length-three word.

Adding the two planes and using (22) retains both first-coordinate
quadratic losses. Their sum is
\[
                         \Gamma(z)-2\gamma_*.
\tag{29}
\]
No numerical last-row margin is used. Equations (26)--(29) prove
the same upper bound for every complete cap profile plus (25)
throughout the early interval, when \(c\le0\).

If \(c\ge0\), then \(d<0\) and the all-angle zero-drift theorem
already bounds the whole high block by its half-row rate. Its
complete joint cap calibration includes the positive-height
allowance. Thus the last-row comparison is not needed in that
case. This also covers \(c=0\) continuously.

## 5. The complete early first pair

**Theorem 3.** For an actual positive three/four word of length
at least three beginning \(3,4\), every \(\tau>0\) admits constants
and a fixed ordinary-color neighborhood of \(w=-2\) such that,
uniformly on (3) and at both level parities,
\[
\begin{split}
 &|U_{0,N}(w,X)|\,|d_N(Y)|^{1/2}
        \sum_{j=\lceil N/2\rceil}^{N-1}|R_{j,N}(a,b)|\\
 &\hspace{12mm}\le C_\tau N^{A_\tau}
                     e^{N\{\Gamma(z)-\gamma_*+\tau\}},
\end{split}
\tag{30}
\]
and
\[
 |U_{0,N}(w,X)C_{1,N}(X,Y)|\,|d_N(Y)|^{1/2}
 \le C_\tau N^{A_\tau}e^{N\{\Gamma(z)-\gamma_*+\tau\}}.
\tag{31}
\]
Every fixed derivative in the ordinary incoming color has the same
rate on a smaller neighborhood. All original external scalar factors
and any later cut halfweights remain exactly as in the original
source.

*Proof.* For \(c\le0\), combine Corollary 2 with the complete cap
envelope. The half-rate branch is below \(\Gamma-1/2000\);
the last-rate branch is below \(\Gamma-2\gamma_*\).
Since \(2\gamma_*<1/2000\), this proves (30), with room for
finite-product, contour and color tolerances. For \(c\ge0\), use
the calibrated zero-drift high block, whose deficit \(1/2000\)
is stronger than the displayed one.

The original ordinary sum decomposes into the disjoint blocks
\[
\begin{array}{ll}
 0\le j\le\lfloor N/8\rfloor,&\text{low},\\
 \lfloor N/8\rfloor+1\le j\le\lceil N/2\rceil-1,
       &\text{central},\\
 \lceil N/2\rceil\le j\le N-1,&\text{high}.
\end{array}
\tag{32}
\]
The joint low-row theorem pays the first with deficit \(1/2000\).
The [complete joint central theorem](research_mixed_early_joint_central_source.md)
pays the second with deficit \(\gamma_*\). Its hypothesis
\(h_0\le0\) is automatic for own type four. It retains the original
central interpolation, both downward joins, both horizontal Fourier
corrections and all four vertical half-sides. The third block is (30).
Adding these exact blocks proves (31); no finite index range or
normalization is changed.

The cap envelope holds for the whole real ordinary-color interval.
Its regular profiles have a favorable angular loss, which may be
discarded, while its true-end estimate is uniform there. The row
sum and all Fourier weights are independent of this color. Thus
the same proof first gives the estimates for all real colors.
The cap has degree less than \(N\), so interval Bernstein--Walsh
continuation supplies a fixed complex neighborhood of \(-2\)
at any prescribed additional rate cost. Cauchy's formula supplies
every fixed color derivative on a smaller neighborhood. One may
apply the polynomial bound directly to the full product; if a
color-independent multiplier vanishes, the assertion is immediate.
No division at a zero or square-root choice for a finite weight
is involved. Choose all tolerances within the single prescribed
\(\tau\). This proves the theorem. \(\square\)

The endpoint principle and finite row bound (10), (20) also apply
to an initial \(4,4\) pair. Its complete joint conclusion is not
asserted here: the allocated cap/last profile has an additional
first-coordinate weight, and its separate transport has not been
used in this proof.

Theorem 3 is a complete first-pair upper bound on a fixed early
horizontal with the original actual heights. It is not a whole-word
bound, a statement about selected first Fourier monomials or moving
outer heights, a signed lower bound, a closed-knot theorem, or a
short-partial-filling stability result.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_right_tail_reflection.md | e3928f2d9549159f6955c654b202dc87198137f4cfdb80f85151af567a976ce1 |
| research_mixed_all_angle_high_row_sign_class.md | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |
| research_mixed_open_word_endpoint_rectangles.md | ac5603badc00d42e98d17a1c5948cae011a6abd991d5249fa61d4224a829ad07 |
| research_mixed_first_four_attached_height_bound.md | 42329b71c8af492823bb5fd5a74b2a472eab8b4f0ecdf2b25cb83ae7f09d7bfe |
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_first_cap_plateau_completion.md | 4b1a55000a114835ce4b2868b79f4bec63ee781d6d997f7fa6b37f7896e4e87d |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_early_joint_central_source.md | f19a7b5c42a4f372e9671c95dec5670f501065802fa96279b542efaa5005aec3 |

All directly used source statements and proof portions were read.
Only written inequalities and the original finite-source estimates
are used. No mathematical numerical evaluation, saved-value
arithmetic, test, import, compilation, or frozen-source edit was
performed.
