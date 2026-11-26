# The complete early first three/three pair on a negative-height interval

Private written proof, 10 November 2026. The wrapped ordinary high-row
rate decreases uniformly when the first retained radius is between
seven eighths and one. This extends the nonnegative-first-height result
by an explicit interval of negative heights. The second retained height
can have either sign. No root selection, numerical evaluation, or
change of the original fixed heights is used.

## 1. The actual finite source and the new radius interval

Fix an actual positive three/four open word of length at least three
beginning with types three and three. Keep the reference, allocations,
and targets of the first33 outer-row theorem:
\[
 a_*=a_0+ic,\quad b_*=b_0+id,\qquad
 a=x+ic,\quad b=z+id,\qquad
 1/10\le x\le11/50,\quad11/50\le z\le9/20.
\tag{1}
\]
In this note assume
\[
              7/8\le r=e^{2\pi c}\le1,
       \qquad13/20<t=e^{2\pi d}<31/20.
\tag{2}
\]
The second bounds are the original ordinary-image consequences.
The first is an additional restriction on the same actual reference,
equivalently \(\log(7/8)/(2\pi)\le c\le0\).
It does not replace the coupled reference by an arbitrary point of a
containing box.

With \(q_N=e^{-2\pi i/N}\), retain exactly
\[
 R_{j,N}(a,b)=X^{-j}
 \frac{(q_NX;q_N)_j(q_NY;q_N)_j}{(q_N;q_N)_j^2},
 \quad X=e^{-2\pi ia},\quad Y=e^{-2\pi ib},\quad0\le j<N,
\tag{3}
\]
\[
 C_{0,N}(X,Y)=\sum_{j=0}^{N-1}R_{j,N}(a,b).
\]
The first factor is the complete cap \(U_{0,N}(w,X)\). There is
no type-four Fourier weight in this first pair. Its original external
scalar, phases and following factors are unchanged.

Let \(E_0(s;a,b)\) be the continuous absolute row rate, including
the chirp \(X^{-j}\), in the outer-row source. For
\[
 s=1-v,\quad x<v<z,\quad Q=2\sin\pi v,
\]
put
\[
 N_s=|1-r e^{2\pi i(v-x)}|,\qquad
 N_b=|1-t e^{-2\pi i(z-v)}|.
\]
The original derivative identity is
\[
                 e^{\partial_sE_0}=\frac{N_sN_b}{rQ^2}.
\tag{4}
\]
At a numerator zero the logarithm has its integrable one-sided limit;
the continuous rate retains every revived row.

## 2. A uniform wrapped-row inequality

**Lemma 1.** On (1)--(2), throughout \(x<v<z\),
\[
                 \left(\frac{N_sN_b}{rQ^2}\right)^2
                                      <\frac{497}{500}<1.
\tag{5}
\]

*Proof.* Write \(\rho=1/r\), so \(1\le\rho\le8/7\), and
\(q=\cot\pi v\). Use the endpoint angles \(x_0=1/10\),
\(z_0=9/20\), and define
\[
 f(q)=(\cos\pi x_0-q\sin\pi x_0)^2,\qquad
 g(q)=(q\sin\pi z_0-\cos\pi z_0)^2,
 \qquad U=1+q^2.
\tag{6}
\]
The unsquared factors in (6) are nonnegative on the actual interval.
The angle differences lie between zero and \(7/20\), where sine
is increasing. Moving the first angle down to \(x_0\) and the
second up to \(z_0\) therefore gives
\[
 \frac{N_s^2}{r^2Q^2}\le\frac87 f(q)+\frac{U}{196},
 \qquad
 \frac{N_b^2}{Q^2}\le\frac{31}{20}g(q)+\frac{121U}{1600}.
\tag{7}
\]
Here \((\rho-1)^2/4\le1/196\) and
\((t-1)^2/4<121/1600\). These are bounds on the full factors,
not on a critical or selected branch.

The elementary guards proved in the nonnegative-height note are
\[
 \sqrt{fg}<65/98,\quad fU<425/256,\quad g\le q^2,
\tag{8}
\]
\[
 \cos(\pi/10)<20/21,\quad \sin(\pi/10)>4/13,
 \quad\cos(9\pi/20)>3/20,
 \quad q\le\cot(\pi/10)<65/21<25/8.
\tag{9}
\]
For clarity, the first bound in (8) is the maximum of the concave
unsquared quadratic between its two zeros:
\[
 \sqrt{fg}\le
 \frac{\sin^2(7\pi/20)}{4\sin(\pi/10)\sin(9\pi/20)}<65/98.
\]
It uses \(\sin^2(7\pi/20)<4/5\),
\(\sin(\pi/10)>4/13\), and \(\sin(9\pi/20)>49/50\).
Also \(f\le1\) and
\(q\sqrt f\le\cos^2(\pi/10)/(4\sin(\pi/10))<13/16\),
giving the second bound in (8). The guards in (9) follow from the
sine lower polynomial, the cosine half-angle identity and
\(157/50<\pi<22/7\), with the written rational witnesses in that
source. None is an evaluation of a source enclosure.

First take \(q\le3/2\). Then
\(gU\le117/16\), \(U^2\le169/16\). Expanding the product
in (7), its four terms are respectively less than
\[
 \frac{130975}{168070}<\frac{39}{50},\qquad
 \frac{2057}{14336}<\frac{29}{200},\qquad
 \frac{3627}{62720}<\frac{29}{500},\qquad
 \frac{20449}{5017600}<\frac{21}{5000}.
\tag{10}
\]
Their sum is less than \(4936/5000<497/500\).

Now take \(q\ge3/2\). The positive factors and (9) give
\[
 f(q)\le(20/21-4q/13)^2,\qquad
 g(q)\le(q-3/20)^2.
\]
The first upper linear factor is positive on the actual interval
\(q<65/21\). Thus the product in (7) is bounded by \(A(q)B(q)\),
where
\[
 A(q)=\frac87(20/21-4q/13)^2+\frac{1+q^2}{196},
\]
\[
 B(q)=\frac{31}{20}(q-3/20)^2+\frac{121}{1600}(1+q^2)
      =\frac{2601}{1600}q^2-\frac{93}{200}q+\frac{221}{2000}.
\tag{11}
\]
An especially convenient majorant for \(A\) is
\[
             A_0(q)=\frac{17}{150}q^2-\frac23q+\frac{521}{500}.
\tag{12}
\]
Indeed the exact coefficients of \(A\) are
\[
 \frac{3753}{33124},\quad-\frac{1280}{1911},\quad
 \frac{12863}{12348},
\]
and they are strictly below the respective coefficients in (12).
The positive cross-product differences for the first and last are
\(158\) and \(1808\); for the middle comparison use
\(3840>3822\). Since \(q\ge0\), this proves \(A<A_0\).

On \([3/2,21/10]\), set \(P=A_0B\). Direct multiplication gives
\[
 P''(q)=\frac{44217}{20000}q^2-\frac{68187}{10000}q
                                      +\frac{4839419}{1200000}
 <\frac94q^2-\frac{34}{5}q+\frac{81}{20}.
\tag{13}
\]
The last quadratic is convex. Its endpoint values are
\(-87/80\) and \(-123/400\), both less than \(-1/4\).
Consequently \(P''<-1/4\) on this entire interval.
At its interior point \(q_0=7/4\), the exact values are
\[
 P(q_0)=\frac{1460554201}{1536000000}<\frac{24}{25},
 \qquad
 P'(q_0)=\frac{297462}{38400000}\in(0,1/100).
\tag{14}
\]
Twice integrating (13) and completing the resulting real square
therefore gives
\[
 P(q)<\frac{24}{25}+2(1/100)^2
                     =\frac{4801}{5000}<\frac{497}{500}.
\tag{15}
\]

It remains to cover \([21/10,25/8]\), an interval slightly larger
than the actual one. The quadratic \(A_0\) is convex and \(B\)
is increasing there. Endpoint bounds therefore suffice:
\[
\begin{array}{c|c|c|c}
q\text{ interval}&A_0\text{ upper bound}&B\text{ upper bound}
                                            &A_0B\text{ upper bound}\\\hline
[21/10,11/5]&71/500&7&497/500\\
[11/5,47/20]&31/250&8&124/125\\
[47/20,5/2]&51/500&19/2&969/1000\\
[5/2,11/4]&17/200&45/4&153/160\\
[11/4,25/8]&33/500&15&99/100.
\end{array}
\tag{16}
\]
Every displayed bound is strict. The exact \(A_0\) endpoint values,
in the order used by this table, are
\[
 \frac{709}{5000},\quad\frac{929}{7500},\quad
 \frac{6073}{60000},\quad\frac{251}{3000},\quad
 \frac{263}{4000},\quad\frac{1047}{16000}.
\tag{17}
\]
The corresponding right-end \(B\) bounds follow from
\[
 B(11/5)=278221/40000<7,\quad
 B(47/20)=5116969/640000<8,
\]
\[
 B(5/2)=291461/32000<19/2,\quad
 B(11/4)=1424069/128000<45/4,\quad B(25/8)<14+1=15.
\tag{18}
\]
For the last inequality, bound the two summands in (11) separately
by \(14\) and \(1\). These written rational comparisons prove
(16), and (10), (15), (16) prove (5). \(\square\)

## 3. The whole finite high block and complete first pair

By (4)--(5), the continuous row rate decreases throughout
\(1-z<s<1-x\). Hence
\[
                     E_0(s)\le E_0(1-z)
                            \quad(1-z\le s\le1-x).
\tag{19}
\]
At an integrable zero use continuity on the two adjoining intervals.
The unwrapped stationary-row theorem already bounds every complete
cap profile plus every row rate on \([1/2,1-z]\) by the original
combined plane, retaining both first-coordinate quadratic losses.
This includes the endpoint in (19). The outer-row theorem pays
\([1-x,1]\) by the calibrated last-row rate. Thus all continuous
high rates are paid with every cap profile and both true cap ends.
In the present nonpositive first-height class there is no additional
positive-height cap upper-row allowance.

Retain precisely the original phases, stationary actions and plane
\[
 \Gamma(z)=\Re L_0(a_*)+\Re\phi_{00}(a_*,b_*)
 +\Re\partial_b\phi_{00}(a_*,b_*)(z-b_0)-\kappa(z-b_0)^2,
\]
\[
             \kappa=1/2500000,\qquad
             \gamma_* =\kappa(a_0-11/50)^2>0.
\tag{20}
\]
The actual endpoint satisfies \(a_0>.278\). The original
zero-safe product majorant at every physical index gives
\[
 |U_{0,N}(w,X)|\sum_{j=\lceil N/2\rceil}^{N-1}|R_{j,N}(a,b)|
 \le C_\tau N^{A_\tau}e^{N\{\Gamma(z)-\gamma_*+\tau\}}.
\tag{21}
\]
Here \(\tau>0\) is arbitrary, and both parities are included.
The proof compares continuous rates and never divides by a finite
endpoint row, which might vanish. The regularized numerator-product
estimate retains all revived rows and the uniform denominator
endpoint error. Summing at most \(N\) rows costs only a polynomial.

**Theorem 2.** On (1)--(2),
\[
 |U_{0,N}(w,X)C_{0,N}(X,Y)|
 \le C_\tau N^{A_\tau}e^{N\{\Gamma(z)-\gamma_*+\tau\}}.
\tag{22}
\]
It holds uniformly at both level parities on a sufficiently small
fixed ordinary-color neighborhood of \(w=-2\), with the same rate
for every fixed derivative in that color on a smaller neighborhood.

*Proof.* Partition the literal finite indices at
\(\lfloor3N/20\rfloor\) and \(\lceil N/2\rceil\).
The joint low-row theorem pays the first block. The complete central
source pays the middle block for nonpositive private critical height;
the positive-height first33 theorem pays it for nonnegative private
height. Each retains the complete cap and every ordinary alias and
join. Equation (21) pays the final block. Their original allocations
and first-coordinate critical marginals agree with (20).
Choose all tolerances inside the prescribed \(\tau\) and sum.

The high-block estimate first holds for the whole real ordinary-color
interval: discard the favorable angular loss in each regular cap
profile and retain its uniform true-end bound. The cap degree is
less than \(N\). Interval polynomial continuation gives a fixed
complex neighborhood at arbitrarily small extra exponential cost;
Cauchy's formula gives the derivatives on a smaller neighborhood.
Intersect these disks with those of the low and central blocks.
No color-independent factor is divided out. This proves (22).
\(\square\)

Together with the nonnegative-first-height theorem, (22) covers every
actual first33 reference satisfying
\[
                         e^{2\pi c}\ge7/8.
\tag{23}
\]
The second retained height and the private critical height may have
either sign. This is a complete first-pair bound at fixed original
heights. It does not cover the rest of the actual negative-height
range, selected first weights, moving-height outer joins, a whole
open word, closed knot, or arbitrary short partial fillings.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_early_three_nonnegative_first_height.md | ffa42bf7baeafde8598b1ca87645e4a4069bd3381d80446db70e13d6cffeb5e8 |
| research_mixed_early_three_outer_high_blocks.md | ece4f34c6dbe288649ff45b54acb705e50b0dc0d63926263ff26eb644d694c3f |
| research_mixed_unwrapped_stationary_high_row_transport.md | 24210764f62ef04250a63dbcb5b5e82d4bdf59ede7eacb88889e5318dfc4d4aa |
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_early_joint_central_source.md | f19a7b5c42a4f372e9671c95dec5670f501065802fa96279b542efaa5005aec3 |
| research_mixed_early_three_positive_private_central.md | d7f54fc0a20c5ccce15b028d16dbcaee2ef0eefbea70795089da097c9730635e |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |

The complete proof and directly used source implications were read
back. Only written inequalities were used. No mathematical numerical
evaluation, saved-value arithmetic, import, compilation, test, or
frozen-source edit was performed.
