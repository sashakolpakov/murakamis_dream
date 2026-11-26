# Outer conditional rows at ordinary following-tangle coordinates

Research deduction, 7 November 2026. The endpoint comparison for the
three-factorial conditional sum extends to the entire outgoing angle
range needed by an ordinary type-four vertex. It also permits both
signs of the incoming height. This removes the angular restriction in
the earlier left-taper theorem. The comparison is independent of a
critical-point equation and retains the original first-argument chirp.
The lower physical rows also increase to the original central cut
throughout these actual following-coordinate domains.

## 1. The rate and the enlarged domain

For \(a=x+ih_a\), \(z=Z+ih_z\), with \(h_z\le0\), put
\[
 \begin{split}
 R&=e^{-2\pi|h_a|},\qquad R_z=e^{2\pi h_z},
       \qquad \lambda=2\pi(-h_a)_+,\\
 J(u)&=\int_0^u\log(2\sin\pi s)\,ds,\\
 E(u;a,z)&=\int_0^u\log|1-e^{-2\pi i(a+s)}|\,ds
       +\int_0^u\log|1-e^{-2\pi i(z+s)}|\,ds
       -3J(u)-2\pi h_a u .
 \end{split}                                                   \tag{1}
\]
The height \(h_a\) may be positive, zero, or negative. In every
case \(0\le\lambda\le-\log R\). Logarithmic zeros in (1)
are interpreted by their integrable limits.

**Theorem 1.** Suppose
\[
 1/10\le x\le11/30,\qquad 1/5\le Z\le11/30,
 \qquad 5/8\le R\le1,
 \qquad 0<R_z\le1.                                    \tag{2}
\]
Then
\[
 \max_{1/2\le u\le1}E(u;a,z)
       =\max\{E(1/2;a,z),E(1;a,z)\},
 \qquad E(1;a,z)=\lambda.                              \tag{3}
\]
Any row-independent allocation can be added to both sides. No
comparison between different conditional types is asserted.

## 2. Reflection with the incoming height of either sign

Let
\[
 f_R(s)=\log|1-Re^{-2\pi is}|,
 \qquad G_R(t)=\int_0^t f_R(s)\,ds.
\]
The radial facts used in
[the earlier upper-row theorem](research_mixed_transformed_left_upper_rows.md)
are: \(f_R\) is even and periodic, increases on \([0,1/2]\),
has zero integral over a full period, and
\(G_R(t)\ge J(t)\) for \(0\le t\le1/2\).

If \(h_a>0\), factor the radius out of the first numerator:
\[
 \log|1-e^{2\pi h_a-2\pi i(x+s)}|
       =2\pi h_a+f_R(x+s).
\]
Its added linear term cancels the chirp in (1). If \(h_a\le0\),
the numerator already has radius \(R\) and the chirp contributes
\(\lambda u\). These observations prove, in both cases,
\[
 F(v):=E(1-v;a,z)-E(1;a,z)
  =-\int_{x-v}^{x}f_R(s)\,ds
   -\int_{Z-v}^{Z}f_{R_z}(s)\,ds
   +3J(v)-\lambda v.                                  \tag{4}
\]
They also prove the last-row identity in (3). The drift \(\lambda\)
has therefore been retained, rather than independently reset.

For \(0<v\le1/5\), the minimum-integral arc of length \(v\)
for the first numerator is centered at an integer. For the second,
\(v\le Z\le1/2\) allows its interval to be shifted left to
\([0,v]\), lowering its integral. It follows that
\[
 \begin{split}
 F(v)&\le2[J(v)-J(v/2)]-\lambda v\\
 &\le v\{\log(4\pi v)-1\}-\lambda v<0 .
 \end{split}                                                   \tag{5}
\]
The second inequality integrates \(\log(2\sin\pi s)
\le\log(2\pi s)\) from \(v/2\) to \(v\). The strict sign
uses \(4\pi/5<88/35<8/3<e\). Thus the whole short reflected
interval is bounded by the last row. This step does not restrict
the incoming angle.

## 3. Three intervals on which the reflected rate increases

Set \(S(v)=2\sin\pi v\). For \(0\le r\le1\),
\[
 |1-re^{-2\pi is}|\le\max\{1,2|\sin\pi s|\}.           \tag{6}
\]
Away from numerator zeros, differentiating (4) gives
\[
 F'(v)=3\log S(v)-f_R(x-v)-f_{R_z}(Z-v)-\lambda.
                                                               \tag{7}
\]
Throughout \(v\ge1/5\), we may use \(-\lambda\ge\log R\).

First let \(1/5\le v\le4/15\). The domain (2) implies
\(|x-v|,|Z-v|\le1/6\); both moduli in (7) are at most one.
Consequently
\[
 F'(v)\ge\log\{R S(v)^3\}
   >\frac12\log\frac{33275}{32768}>0.                 \tag{8}
\]
For the strict witness,
\[
 S(1/5)^2=(5-\sqrt5)/2>11/8,
 \qquad (5/8)^2(11/8)^3=33275/32768>1.
\]
The first comparison follows from \(\sqrt5<9/4\).

Next let \(4/15\le v\le11/30\). Here \(|x-v|\le v\),
\(|Z-v|\le1/6\), and \(S(v)>1\). The first modulus in (7)
is at most \(S(v)\), and the second at most one. Since
\(v\ge4/15>1/4\),
\[
                 F'(v)\ge\log\{R S(v)^2\}
                                   >\log(5/4)>0.       \tag{9}
\]

Finally let \(11/30\le v\le1/2\). The first modulus is still
at most \(S(v)\); bound the second by two. We have
\[
 S(v)^2\ge4\cos^2(2\pi/15)>81/25.
\]
Indeed \(2\pi/15<3/7\), and the cosine Taylor inequality gives
\(\cos(2\pi/15)>1-9/98=89/98>9/10\). Therefore
\[
             F'(v)\ge\log\{R S(v)^2/2\}
                                  >\log(81/80)>0.      \tag{10}
\]
At a possible zero the derivative has an integrable logarithmic
singularity. Integrating (8)--(10) on the complementary intervals
and taking limits proves strict increase on \([1/5,1/2]\).
Together with (5) and \(F(0)=0\), this proves (3).

## 4. Coverage of ordinary following-coordinate domains

The ordinary type-four enclosure in
[the actual-reference theorem](research_mixed_actual_last_row_reference_domains.md)
is
\[
 O_4=P_4\cap\{-51/500\le\Im z\le-1/1000\},
 \qquad P_4=\{|z-(.30-.052i)|\le.060\}.                \tag{11}
\]
In particular \(.24\le\Re z\le.36\), strictly inside the
outgoing real range in (2). Its height is strictly negative. The
attached type-four enclosure \(A_4\) is contained in the same
real range and also has negative height. Both sets satisfy the
outgoing conditions in Theorem 1.

Every incoming height with \(|h_a|\le9/125\) satisfies its
radius condition. In fact \(2\pi(9/125)<23/50\), and the
positive-series estimate gives
\[
 e^{23/50}\le1+\frac{23}{50}
    +\frac{(23/50)^2}{2(1-23/150)}
       =\frac{20129}{12700}<\frac85.                   \tag{12}
\]
Thus \(R>5/8\). This includes the entire attached type-three
height range \((-9/125,21/1000)\).

In particular Theorem 1 applies throughout every left transition
\[
 a(x)=x+ic(x-.1)/.12,\qquad .1\le x\le.22,
       \qquad -9/125<c<21/1000,                         \tag{13}
\]
and every independent outgoing point in \(O_4\) or \(A_4\).
No endpoint-map correlation is needed for this assertion.
For incoming \(.22\le x\le.5\), the endpoint theorem of
[the upper-row extension](research_mixed_transformed_upper_rows.md),
Lemma 1, covers the same outgoing sets: their real parts are in
\([.22,.5]\), and their heights and the incoming heights have
modulus at most \(.108\). Thus the high physical rows have an
endpoint-only comparison on the full incoming interval \([.1,.5]\)
with the indicated transition followed by the constant height \(c\).

## 5. The complete finite upper sum and its last branch

Retain the literal polynomial part
\[
 C^{\rm up}_{1,N}(X,Y)=
 \sum_{j=\lceil N/2\rceil}^{N-1}
      \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},
 \quad X=e^{-2\pi ia},\quad Y=e^{-2\pi iz}.              \tag{14}
\]
The zero-safe product and uniform factorial estimates used in
Section 4 of the earlier upper-row theorem apply unchanged on any
compact parameter set above. Hence, for any \(\tau>0\),
\[
 \sum_{j=\lceil N/2\rceil}^{N-1}
   \left|\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}\right|
 \le C_\tau N^{B_\tau}
       \left(e^{N(E(1/2;a,z)+\tau)}
                        +e^{N(\lambda+\tau)}\right).    \tag{15}
\]
This includes all restored terms and the even half row. It also
includes unit-radius zeros; no numerator lower bound or terminating
support is used.

The last exponential can be combined with a uniform bound for the
complete first cap. Its degree in \(X\) is less than \(N\),
and its disk ceiling is
\[
 |U_{0,N}(w,X)|\le C_\tau N^{B_\tau}
       e^{N(433/500+1/3+\tau)},\qquad |X|\le1,
 \quad w\in[-2,2].                                    \tag{16}
\]
This is the whole coherent cap bound in
[the original upper-row theorem](research_mixed_transformed_upper_rows.md),
equation (14). Polynomial growth outside the disk adds at most
\(2\pi(h_a)_+\) to its rate. The combined last-branch rate is
therefore
\[
 \frac{433}{500}+\frac13+2\pi(h_a)_++\lambda
     =\frac{433}{500}+\frac13+2\pi|h_a|
     <\frac{3469}{2100}
     =\frac53-\frac{31}{2100},                         \tag{17}
\]
when \(|h_a|\le9/125\), using \(\pi<22/7\).

Thus the last branch in the full cap-weighted high-row bound has
a uniform ceiling below \(5/3\) on all these following-coordinate
domains. The other branch is the actual half-row rate and remains
explicit. An estimate of that half row relative to the composed
geometric action is still needed to claim a normalized gap there.
Equation (17) by itself does not lower-bound that action.

The same finite estimates hold with arbitrary prescribed small
rate tolerances on a fixed neighborhood of the actual outgoing
sets (11), which are strictly inside the angular and negative-height
conditions. Fixed outgoing derivatives then follow by Cauchy's
formula on smaller neighborhoods. Fixed ordinary-color derivatives
follow from the complete cap bound and polynomial derivative
estimates. None of these conclusions supplies a nonzero coefficient
for the next composed sum or discards either type-four Fourier term.

## 6. Every lower physical row increases to the original cut

The lower comparison has a direct proof on the full outgoing real
range of \(O_4\). Suppose
\[
 .1\le x\le.22,\qquad h_a\le21/1000,\qquad
 .24\le Z\le.36,\qquad h_z\le0.                         \tag{18}
\]
For the uniform finite consequence restrict heights to any fixed
compact set, such as the actual sets above. No incoming lower
height bound is needed for the scalar derivative inequality.

**Lemma 2.** On (18), the rate (1) satisfies
\[
 \partial_u E(u;a,z)>\log(400/361)>0,
                         \qquad 0<u\le3/20.            \tag{19}
\]
Consequently every lower physical row, including \(j=0\), is
bounded at the exponential scale by the original real cut \(u=.15\).

*Proof.* Write \(B=e^{-2\pi h_a}\). The exact chirp-aware
derivative is
\[
 e^{\partial_uE}=
 \frac{|B-e^{-2\pi i(x+u)}|
       |1-R_z e^{-2\pi i(Z+u)}|}{(2\sin\pi u)^3}.       \tag{20}
\]
We first show that the first modulus exceeds \(2\sin\pi u\)
for \(0\le u\le.15\). The height hypothesis implies
\(B>5/6\): indeed \(.042\pi<7/50\) and
\(e^{7/50}\le(1-7/50)^{-1}=50/43<6/5\).
Also \(\cos(\pi/5)<5/6\), from its exact value
\((1+\sqrt5)/4\) and \(\sqrt5<7/3\).

Since \(.1\le x\le.22\) and \(u\le.15\), the squared
modulus in (20) is smallest at \(x=.1\), then increases with
\(B\ge5/6\). Set \(B_0=5/6\). Its difference from
\((2\sin\pi u)^2\) is bounded below by
\[
 D(u)=B_0^2-1
       +2(1-B_0\cos(\pi/5))\cos(2\pi u)
       +2B_0\sin(\pi/5)\sin(2\pi u).                 \tag{21}
\]
Both trigonometric coefficients are positive. On \([0,.15]\),
the sine and cosine are nonnegative, so \(D''(u)<0\).
At zero, \(D(0)=|B_0-e^{-\pi i/5}|^2>0\). At the other end,
\[
 D(.15)=B_0^2-1+2\sin(\pi/5)>B_0^2>0,
\]
because \(\sin(\pi/5)>1/2\). Concavity proves positivity
throughout the interval, as required.

For \(.01\le u\le.15\), the shifted outgoing real part is
in \([.25,.51]\), where its cosine is nonpositive. The second
modulus in (20) is therefore at least one. Also
\(2\sin(3\pi/20)<3\pi/10<33/35<19/20\). Hence
\[
 e^{\partial_uE}>(2\sin\pi u)^{-2}>400/361.             \tag{22}
\]
For \(0<u<.01\), the first shifted real part lies in
\((.1,.23)\). The distance of \(e^{-2\pi i(x+u)}\)
from any real number is greater than \(1/2\). Thus the first
modulus exceeds \(1/2\). The outgoing shifted real part is in
\((.24,.37)\); minimizing over its nonnegative radius gives
a modulus greater than \(1/2\) as well. Its cosine-positive
portion lies below \(.25\), where its sine already exceeds
\(1/2\); on the remaining portion the modulus is at least one.
Finally \(2\sin\pi u<\pi/50<1/10\), so (20) exceeds
\(250>400/361\). This proves (19). \(\square\)

The rate is continuous at zero with value zero. Integrating (19)
therefore bounds the whole interval \([0,.15]\) by its right
endpoint, without deleting an initial physical layer. The uniform
zero-safe product estimates and denominator error \(O(\log N)\)
give, for every \(\tau>0\),
\[
 \sum_{0\le j/N<.15}
    \left|\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}\right|
 \le C_\tau N^{B_\tau}e^{N(E(.15;a,z)+\tau)}.           \tag{23}
\]
The actual half-grid displacement near the cut is absorbed by the
same tolerance. Combining (23) with (15) reduces both physical
outer ranges to the real cuts \(.15,.5\) and the explicit last
branch. The remaining central rows still require their exact
contour summation and comparison with the geometric action.
