# The complete early first three/three pair at nonnegative first height

Private research proof, 10 November 2026. The ordinary high-row rate
strictly decreases throughout the interval where only its second
numerator has crossed a period, provided the first retained height is
nonnegative. This supplies the missing interval in the first-three/three
outer-row estimate. The second retained height may have either sign.
Together with the previously established lower and central bounds, the
result controls the entire first pair at its original fixed heights.

The proof is a uniform polynomial inequality for the derivative of the
original row rate. It uses no numerical evaluation of a critical point,
source value, or polynomial maximum.

## 1. The unchanged source

Fix an actual positive three/four open word of length at least three
beginning with powers three and three. Retain the reference and notation
of [the first33 outer-row theorem](research_mixed_early_three_outer_high_blocks.md):
\[
 a_*=a_0+ic,\quad b_*=b_0+id,\qquad
 a=x+ic,\quad b=z+id,\quad
 1/10\le x\le11/50,\quad11/50\le z\le9/20.
\tag{1}
\]
Here the actual heights are fixed. Assume additionally that \(c\ge0\).
The original endpoint and ordinary images then give
\[
 1\le r=e^{2\pi c}<23/20,\qquad
 13/20<t=e^{2\pi d}<31/20.
\tag{2}
\]
In particular no sign restriction is placed on \(d\).

The exact ordinary rows, with \(q_N=e^{-2\pi i/N}\), are
\[
 R_{j,N}=X^{-j}
 \frac{(q_NX;q_N)_j(q_NY;q_N)_j}{(q_N;q_N)_j^2},
 \quad X=e^{-2\pi ia},\quad Y=e^{-2\pi ib},\quad0\le j<N.
\tag{3}
\]
Write \(C_{0,N}=\sum_{j=0}^{N-1}R_{j,N}\), and let
\(U_{0,N}(w,X)\) be the complete first cap. Neither factor has a
type-four Fourier weight. Their original phases, branches, external
scalar and later factors are unchanged.

Let \(E_0(s;a,b)\) be the absolute continuous row rate from that source,
including the chirp \(X^{-j}\). On the wrapped interval put
\[
 s=1-v,\quad x<v<z,\qquad
 Q=2\sin\pi v,
\]
\[
 N_s=|1-r e^{2\pi i(v-x)}|,\qquad
 N_b=|1-t e^{-2\pi i(z-v)}|.
\]
Exact differentiation gives
\[
             \exp(\partial_s E_0)=\frac{N_sN_b}{rQ^2}.
\tag{4}
\]
The primitive is continuous through all integrable logarithmic zeros.

## 2. A uniform derivative bound on the whole wrapped interval

**Lemma 1.** Under (1)--(2), for every \(x<v<z\),
\[
       \left(\frac{N_sN_b}{rQ^2}\right)^2<\frac{399}{400}<1.
\tag{5}
\]

*Proof.* Put \(\rho=1/r\), \(x_0=1/10\), \(z_0=9/20\), and
\(q=\cot\pi v\). Thus \(20/23<\rho\le1\).
The two angle differences lie in \([0,7/20]\), where \(u\mapsto\sin\pi u\)
is nonnegative and increasing. Decreasing \(x\) to \(x_0\) and increasing
\(z\) to \(z_0\) therefore only enlarges the numerator bounds. Since
\(Q^2=4/(1+q^2)\),
\[
 \frac{N_s^2}{r^2Q^2}
 =\frac{(1-\rho)^2}{4}(1+q^2)
       +\rho\frac{\sin^2\pi(v-x)}{\sin^2\pi v}
 \le f(q)+\frac9{2116}(1+q^2),
\tag{6}
\]
\[
 \frac{N_b^2}{Q^2}
 =\frac{(1-t)^2}{4}(1+q^2)
       +t\frac{\sin^2\pi(z-v)}{\sin^2\pi v}
 \le\frac{31}{20}g(q)+\frac{121}{1600}(1+q^2),
\tag{7}
\]
where
\[
 f(q)=(\cos\pi x_0-q\sin\pi x_0)^2,\qquad
 g(q)=(q\sin\pi z_0-\cos\pi z_0)^2.
\tag{8}
\]
The unsquared factors in (8) are nonnegative because
\(x_0\le v\le z_0\). All bounds below concern the resulting product
of (6) and (7), before any square root is taken.

First suppose \(q\le2\). Completing a square, or maximizing a concave
quadratic between its two zeros, gives
\[
 \sqrt{f(q)g(q)}\le
 \frac{\sin^2\pi(z_0-x_0)}{4\sin\pi x_0\sin\pi z_0}<\frac23.
\tag{9}
\]
For the strict bound use
\(\sin^2(7\pi/20)<4/5\), \(\sin(\pi/10)>4/13\), and
\(\sin(9\pi/20)>49/50\); their quotient is less than
\(65/98<2/3\).
Moreover \(f\le1\), and
\[
 q\sqrt f=q\cos\pi x_0-q^2\sin\pi x_0
 \le\frac{\cos^2\pi x_0}{4\sin\pi x_0}<\frac{13}{16}.
\]
Consequently
\[
 f(1+q^2)<1+169/256<7/4,
 \qquad g(1+q^2)\le q^2(1+q^2)\le20.
\tag{10}
\]
Expanding the product of (6)--(7), its four terms are bounded by
\[
 \frac{31}{45}<\frac7{10},\qquad
 \frac{847}{6400}<\frac2{15},\qquad
 \frac{279}{2116}<\frac2{15},\qquad
 \frac{27225}{3385600}<\frac1{100},
\tag{11}
\]
respectively. Their sum is less than \(293/300<399/400\).

Now suppose \(q\ge2\). The elementary guards
\[
 \cos(\pi/10)<20/21,\quad \sin(\pi/10)>4/13,
 \quad\cos(9\pi/20)>3/20,
\tag{12}
\]
and the positive factors in (8) imply
\[
 f\le(20/21-4q/13)^2,\qquad g\le(q-3/20)^2.
\]
The first upper linear factor is positive on the actual domain:
\(q\le\cot(\pi/10)<65/21<25/8\).
Set
\[
 A(q)=(20/21-4q/13)^2+\frac9{2116}(1+q^2),
\]
\[
 B(q)=\frac{31}{20}(q-3/20)^2+\frac{121}{1600}(1+q^2).
\tag{13}
\]
The polynomial \(A\) is convex, and \(B\) increases for \(q\ge2\).
Thus it suffices to bound \(A\) at both endpoints of each interval
and \(B\) at its right endpoint. The following rational bounds give
\[
\begin{array}{c|c|c|c}
q\text{ interval}&A\text{ upper bound}&B\text{ upper bound}
                                      &AB\text{ upper bound}\\ \hline
[2,11/5]&7/50&7&49/50\\
[11/5,5/2]&21/200&19/2&399/400\\
[5/2,11/4]&7/100&12&21/25\\
[11/4,25/8]&1/20&15&3/4 .
\end{array}
\tag{14}
\]
For completeness, all entries follow from these direct endpoint
inequalities:
\[
\begin{array}{c|c}
q&A(q)\text{ is less than}\\ \hline
2&289/2500+11/500<7/50\\
11/5&49/625+1/40<21/200\\
5/2&9/256+1/32<7/100\\
11/4&9/784+3/80<1/20\\
25/8&1/10000+47/1000<1/20.
\end{array}
\tag{15}
\]
For example, the corresponding absolute linear factors are bounded by
\(17/50,7/25,3/16,3/28,1/100\); the second summands in
\(A\) have the displayed bounds separately. Also
\[
 B(11/5)=278221/40000<7,
 \quad B(5/2)=291461/32000<19/2,
\]
\[
 B(11/4)<21/2+2/3<12,
 \qquad B(25/8)<14+1=15.
\tag{16}
\]
Convexity in (14) is used only for \(A\); no convexity claim for the
quartic product is needed. Equations (14)--(16) prove (5) on this range.

Here are elementary witnesses for the trigonometric guards.
The sine lower polynomial and \(157/50<\pi<22/7\) give
\[
 \sin(\pi/10)>157/500-1331/257250>4/13.
\]
Since \(\pi<4\),
\(\sin(9\pi/20)=\cos(\pi/20)>1-\pi^2/800>49/50\).
The exact identities
\(\cos^2(\pi/10)=(5+\sqrt5)/8\) and
\(\sin^2(\pi/5)=(5-\sqrt5)/8\), with
\(11/5<\sqrt5<9/4\), imply
\(\cos^2(\pi/10)<29/32<400/441\) and
\(\sin(\pi/5)<3/5\).
Thus \(\sin^2(7\pi/20)=(1+\sin(\pi/5))/2<4/5\).
Finally
\(\cos(9\pi/20)=\sin(\pi/20)>157/1000-1/1000>3/20\),
where the cubic sine remainder is less than \(1/1000\) because
\(\pi/20<11/70\). This proves all guards without a source evaluation.
\(\square\)

## 3. All high rows and the complete first pair

By (4)--(5), \(E_0(s)\) strictly decreases on
\(1-z<s<1-x\). Continuity supplies the endpoint comparison
\[
 E_0(s)\le E_0(1-z),\qquad 1-z\le s\le1-x.
\tag{17}
\]
The [unwrapped high-row theorem](research_mixed_unwrapped_stationary_high_row_transport.md)
already controls the complete cap times every continuous rate on
\([1/2,1-z]\), including its endpoint. The outer-row theorem's
last-row calibration and the reflection lemma control
\([1-x,1]\). Adding (17) covers the entire interval \([1/2,1]\).
Every cap profile, its physical right-row allowance, and its true
index ends remain covered: (17) compares ordinary rates at the same
cap target and makes no change to the cap factor.

Retain the original plane and positive gap
\[
 \Gamma(z)=\Re L_0(a_*)+\Re\phi_{00}(a_*,b_*)
 +\Re\partial_b\phi_{00}(a_*,b_*)(z-b_0)
 -\kappa(z-b_0)^2,
\]
\[
 \kappa=1/2500000,\qquad \gamma_* =\kappa(a_0-11/50)^2.
\tag{18}
\]
The actual endpoint has \(a_0>.278\), so this gap is uniformly positive.
The zero-safe product estimate, valid uniformly at every index, now gives
\[
 |U_{0,N}(w,X)|\sum_{j=\lceil N/2\rceil}^{N-1}|R_{j,N}|
 \le C_\tau N^{A_\tau}e^{N\{\Gamma(z)-\gamma_*+\tau\}}.
\tag{19}
\]
Here and below \(\tau>0\) is arbitrary and both level parities are
included. Summing at most \(N\) rows costs a polynomial factor.
The continuous comparison is not a division by a finite half-row or
endpoint value, which might vanish.

**Theorem 2.** On (1)--(2), for every \(\tau>0\),
\[
 |U_{0,N}(w,X)C_{0,N}(X,Y)|
 \le C_\tau N^{A_\tau}e^{N\{\Gamma(z)-\gamma_*+\tau\}}.
\tag{20}
\]
It holds on a fixed sufficiently small ordinary-color neighborhood of
\(w=-2\), and for every fixed derivative in that color on a smaller
neighborhood, at both level parities.

*Proof.* Partition the exact indices into
\(0\le j\le\lfloor3N/20\rfloor\),
\(\lfloor3N/20\rfloor+1\le j\le\lceil N/2\rceil-1\),
and \(\lceil N/2\rceil\le j<N\).
The first block is the [joint low-row theorem](research_mixed_early_joint_low_tail.md),
with gap \(1/2000>\gamma_*\).
The second is covered at nonpositive private height by
[the original central theorem](research_mixed_early_joint_central_source.md),
and at nonnegative private height by
[the positive-height first33 theorem](research_mixed_early_three_positive_private_central.md).
Each retains every cap term and ordinary contour correction with gap
\(\gamma_*\). The third block is (19). Choose all source tolerances
within the prescribed \(\tau\) and add the three bounds.

The high-block argument first holds for the whole real ordinary-color
interval. The cap is a polynomial of degree less than \(N\); its interval
bound extends to a fixed complex neighborhood at arbitrarily small
additional exponential cost. Cauchy's formula then gives fixed color
derivatives on smaller neighborhoods. Intersect with the fixed disks of
the low and central estimates. No color-independent multiplier is
divided out. This proves the stated common scope. \(\square\)

The theorem removes the former sign restriction on the second retained
height in the complete first33 early-pair estimate. The first retained
height must still be nonnegative. It is an upper bound at fixed heights,
not a bound on moving-height joins, the rest of the first period, or a
whole open word. It supplies no new closed-knot or finite-exception
conclusion by itself.

## Direct source versions

The algebraic derivative estimate in Section 2 is proved above. The finite
source and assembly use these frozen notes:

| Source | SHA-256 |
|---|---|
| research_mixed_early_three_outer_high_blocks.md | ece4f34c6dbe288649ff45b54acb705e50b0dc0d63926263ff26eb644d694c3f |
| research_mixed_unwrapped_stationary_high_row_transport.md | 24210764f62ef04250a63dbcb5b5e82d4bdf59ede7eacb88889e5318dfc4d4aa |
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_early_joint_central_source.md | f19a7b5c42a4f372e9671c95dec5670f501065802fa96279b542efaa5005aec3 |
| research_mixed_early_three_positive_private_central.md | d7f54fc0a20c5ccce15b028d16dbcaee2ef0eefbea70795089da097c9730635e |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |

No mathematical numerical evaluation, saved-value arithmetic, test, import,
or compilation was used. Frozen manuscripts and source notes are unchanged.
