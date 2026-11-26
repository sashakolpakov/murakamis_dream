# The complete conditional polynomial on the two real upper arcs

Private written proof, 11 November 2026. Author-frozen after complete
proof and direct-source readback. Independent full review is required
before adoption.

The two numerator zeros determine the end of the central index
interval. Both remain outside the contour. The rows beyond either
zero are estimated directly, with their original finite products.
A finite upper sampling height suffices; an arbitrarily tall upper
rectangle would not have the required decay.

## 1. The original polynomial and the two comparison rates

Set
\[
 \zeta=e^{-2\pi i/N},\qquad
 P_j=(\zeta;\zeta)_j,\qquad p_j(V)=(\zeta V;\zeta)_j,
\]
and retain every term of
\[
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
          \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
 \tag{1}
\]
The parameters are real and satisfy
\[
 \frac12\le a\le\frac78,\qquad
 \frac12\le q\le\frac{18}{25},\qquad
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iq}.
 \tag{2}
\]
The original primitive has
\[
 g'(w)=\operatorname{Log}(1-e^{-2\pi iw}),\quad
 0<\Re w<1,\qquad g(0)=0.
\]
Write
\[
\begin{split}
 Q(s;a,q)&=g(a+s)+g(q+s)-3g(s)-g(a)-g(q)+2\pi ias,\\
 d&=\min(1-a,1-q),\qquad \ell=2/25.
\end{split}                                                    \tag{3}
\]
The [zero-lift branch theorem](research_mixed_real_unit_pair_zero_lift_branch.md)
gives a unique critical point \(s_*=t_*+ih_*\) in \(0<\Re s<d\).
It has \(h_*<0\), is simple, and uses precisely these logarithms.
Put \(\Theta(a,q)=Q(s_*;a,q)\).

For real arguments define the continuous periodic function
\[
 J(t)=\int_0^t\log(2|\sin\pi v|)\,dv,\qquad
 J(0)=J(1/2)=J(1)=0,
\]
and
\[
\begin{split}
 I_x(t)&=J(x+t)-J(x),\\
 E_a(t;q)&=I_a(t)+I_q(t)-3J(t),\\
 L(q)&=E_{1/2}(1/8;q).
\end{split}                                                    \tag{4}
\]
All integrated numerator zeros are retained in these definitions.
In particular \(E_a\) is the upper exponential rate of a literal
absolute row of (1), not the rate of a selected subseries.

**Theorem.** For every \(\tau>0\), constants \(C_\tau,A_\tau\),
uniform on (2), give
\[
 |C_{1,N}(X,Y)|
 \le C_\tau N^{A_\tau}
       \exp N\{\max(\Re\Theta(a,q),L(q))+\tau\}.
 \tag{5}
\]
The assertion includes both level parities and all indices.
It is an upper estimate only. An adjoining cap, Fourier weights,
and the third conditional factor require their separate comparisons.

## 2. A common left cut before the critical point

The branch theorem already gives \(h_*<0\).
Let \(\rho=e^{2\pi h_*}\in(0,1)\).
If \(\rho\le1/2\), each argument of
\(1-\rho e^{-2\pi iu}\) has magnitude at most \(\pi/6\).
The imaginary part of the critical equation
\[
 g'(a+s_*)+g'(q+s_*)-3g'(s_*)+2\pi ia=0
\]
would consequently be at least
\(\pi-5\pi/6>0\). Thus \(\rho>1/2\).

Suppose \(0<t_*\le\ell\). Put
\[
\begin{split}
 A&=|1-\rho e^{-2\pi i(a+t_*)}|^2,\qquad
 B=|1-\rho e^{-2\pi i(q+t_*)}|^2,\\
 D&=|1-\rho e^{-2\pi it_*}|^2.
\end{split}
\]
The elementary incoming and own estimates in Section 2 of
[the positive-output finite-source proof](research_mixed_four_conditional_positive_output_real_arc.md)
use only \(a\le7/8,t_*\le2/25\), and give
\[
 A>(1-\rho)^2+\rho/16\ge63/1024,\qquad
 D<(1-\rho)^2+\rho/4\le3/8.
 \tag{6}
\]
Here the quadratic minimum in the first inequality is at
\(\rho=31/32\); the maximum in the second on \([1/2,1]\)
is at \(\rho=1/2\).

The changed outgoing range is handled explicitly:
\(q+t_*\in[1/2,4/5]\), so
\[
 \cos(2\pi(q+t_*))\le\cos(2\pi/5)
       =(\sqrt5-1)/4<1/3.
\]
Consequently
\[
 B>1+\rho^2-\tfrac23\rho\ge8/9.
\]
Together with (6), this gives
\[
 AB>\frac7{128}>\frac{27}{512}>D^3,
\]
contrary to \(|e^{Q_s(s_*)}|^2=AB/D^3=1\).
Hence \(t_*>\ell\) on the whole rectangle.

Compactness and the branch theorem now give positive uniform
distances of \(t_*\) from both \(\ell\) and \(d\), and a uniform
bound on \(|h_*|\). These are fixed margins, independent of \(N\).

## 3. Every physical row outside the central interval

For \(0\le t\le1/2\) and \(1/2\le x\le1\),
\[
                         I_x(t)\le I_{1/2}(t).                 \tag{7}
\]
One direct proof differentiates in \(x\).
The sign of
\(\log|\sin\pi(x+t)/\sin\pi x|\) changes only from negative
to positive on this interval, with the integrated zero retained.
The two endpoint values are
\(I_{1/2}(t)=-J(1/2-t)\ge0\) and \(I_1(t)=J(t)\le0\).
Thus the maximum is the first endpoint. This is also equation (29)
of the positive-output source, whose proof does not use its outgoing
parameter.

The half-input row \(E_{1/2}(t;q)\) increases for
\(0<t\le1/8\). Indeed,
\[
 e^{\partial_tE_{1/2}(t;q)}
   =\frac{2\cos(\pi t)\,2|\sin\pi(q+t)|}{(2\sin\pi t)^3}>1:
 \tag{8}
\]
the two numerator factors exceed \(9/5\) and \(4/5\),
respectively, while \(2\sin\pi t<4/5\).
The outgoing estimate uses
\(q+t\in[1/2,169/200]\); the elementary sine bound at its
right endpoint is written in Section 3 of
[the far-real-first proof](research_mixed_443_far_real_first_arc.md).
Thus every low row \(0\le t\le\ell\) is bounded by \(L(q)\).

If \(x\in[1/2,1]\), \(\delta_x=1-x\), and
\(\delta_x\le t\le1\), the entropy inequality is
\[
 I_x(t)=J(\delta_x)+J(t-\delta_x)\le J(t).
 \tag{9}
\]
For \(\delta_x=0\) there is equality. Otherwise the difference
\(J(t)-J(\delta_x)-J(t-\delta_x)\) vanishes at
\(t=\delta_x,1\). Its derivative is positive before
\((1+\delta_x)/2\) and negative afterwards, since
\(\sin\pi t-\sin\pi(t-\delta_x)\) has exactly that sign.
This proves (9), including both endpoints.

For every \(t\ge d\), at least one of the two legs satisfies
(9). If \(d\le t\le1/2\), bound the other leg by \(t\log2\):
\[
 E_a(t;q)\le t\log2-2J(t)<7/15.
 \tag{10}
\]
The function on the right has its maximum at \(t=1/4\).
The analytic bounds \(\log2<7/10\) and
\(-4J(1/4)<7/12\), used and sourced in Section 4 of the
positive-output proof, give
\((\log2)/4-2J(1/4)<7/40+7/24=7/15\).
For \(1/2\le t\le1\), use \(J(t)\ge0\) and
\(|J(u)|<1/6\) instead:
\[
                         E_a(t;q)<1/3.                       \tag{11}
\]
The last elementary bound follows from the minimum of \(J\) at
\(1/6\), and \(2\sin\pi u\ge6u\) on \([0,1/6]\).
It is included in the same source proof.

The benchmark is strictly larger than either ceiling. Its explicit
lower bound, proved term by term in Section 3 of the far-real-first
proof, is
\[
 L(q)>\frac{93}{200}+\frac1{14}-\frac1{32}>\frac12.
 \tag{12}
\]
This is a bound for the function (4), not a lower estimate for (1).

Choose a fixed \(\varepsilon>0\) small enough that
\[
 t_*<r(a,q):=d-\varepsilon
\]
throughout (2), and that the real collar \([d-\varepsilon,d]\)
has rate less than \(1/2\). The latter follows from (10)--(11)
and uniform continuity of the integrated rates, including their
logarithmic zeros. Also require \(r>\ell\).
Every physical row outside \([\ell,r]\) is now bounded by \(L(q)\).

## 4. A finite upper sampling height

Set
\[
 H=\frac{\log2}{2\pi},\qquad
 G_H(u)=\Re g(u-iH)
       =-\frac1{2\pi}\sum_{n\ge1}\frac{2^{-n}\sin(2\pi nu)}{n^2}.
 \tag{13}
\]
The series converges absolutely, with its derivatives needed below.
The original primitive and its reciprocal-radius identity give
\[
                    \Re g(u+iH)=G_H(u)+\pi H(2u-1),
                         \qquad 0<u<1.                       \tag{14}
\]
This constant can be checked without a dilogarithm continuation:
differentiate both sides in \(u\), use the reciprocal identity
for the modulus, and evaluate at \(u=1/2\).
Both sides are zero there because \(g'(1/2+iv)\) is real
and \(J(1/2)=0\). The lower-height Fourier series in (13)
follows by integrating the absolutely convergent logarithm series
and fixing the same midpoint value.

For \(\ell\le t\le r\), all of \(t,a+t,q+t\) lie in \((0,1)\).
With \(F(t,\eta)=\Re Q(t+i\eta;a,q)\), (14) gives the exact
upper weighted rate
\[
\begin{split}
 W(t)&:=F(t,H)-2\pi H\\
 &=G_H(a+t)+G_H(q+t)-3G_H(t)-J(a)-J(q)
                       +(q-t-1/2)\log2 .
\end{split}                                                    \tag{15}
\]
The incoming contribution decreases with \(a\) throughout the
present prewall region. Indeed, putting \(c=\cos2\pi a\),
\[
\begin{split}
 \partial_a[G_H(a+t)-J(a)]
 &=\log\frac{|1-\tfrac12e^{-2\pi i(a+t)}|}
                   {|1-e^{-2\pi ia}|}\le0,\\
 |1-e^{-2\pi ia}|^2
   -|1-\tfrac12e^{-2\pi i(a+t)}|^2
 &\ge (1-\tfrac12)(1+\tfrac12-2c)>0 .
\end{split}                                                    \tag{16}
\]
Here cosine increases on \([1/2,1]\), and
\(c\le\cos(7\pi/4)=1/\sqrt2<3/4\).
For every intermediate incoming angle between \(1/2\) and \(a\),
the same \(t\) remains prewall. Thus
\[
                  G_H(a+t)-J(a)\le G_H(1/2+t).                \tag{17}
\]

The remaining estimate uses only elementary Fourier tails.
Equation (13) gives
\[
\begin{split}
 G_H(1/2+t)-3G_H(t)
 &\le \frac{\sin2\pi t}{\pi}+\frac{17}{144\pi},\\
 G_H(q+t)&\le\frac{85}{288\pi}.
\end{split}                                                    \tag{18}
\]
For the first line the \(n=1\) coefficient is \(1/\pi\),
the absolute \(n=2\) term is \(1/(16\pi)\), and the tail is
at most
\[
 \frac2\pi\sum_{n\ge3}\frac{2^{-n}}{n^2}
 \le\frac2{9\pi}\sum_{n\ge3}2^{-n}=\frac1{18\pi}.
\]
For the second line,
\(\sum_{n\ge1}2^{-n}/n^2\le1/2+1/16+1/36=85/144\).

For every \(0\le t\le1/2\),
\[
                 \frac{\sin2\pi t}{\pi}-t\log2<\frac15.
 \tag{19}
\]
On \(0\le t\le1/4\), use the tangent to the concave sine
at \(t=1/6\):
\[
 \frac{\sin2\pi t}{\pi}-t\log2
 \le\frac{\sqrt3}{2\pi}-\frac16+(1-\log2)t
 <\frac7{25}-\frac16+\frac1{12}<\frac15.
\]
Here \(\pi>25/8,\sqrt3<7/4,\log2>2/3\), and
\(1-\log2>0\).
For \(t\ge1/4\), bound sine by one and use
\(1/\pi-(\log2)/4<8/25-1/6<1/5\).

Finally,
\[
\begin{split}
 (q-1/2)\log2-J(q)
   &=-\int_0^{q-1/2}\log\cos(\pi v)\,dv\\
   &<\frac{11}{50}\log(4/3)<\frac{11}{150}.
\end{split}                                                    \tag{20}
\]
For \(0\le v\le11/50\), one has
\(\pi v<7/10\), hence
\(\cos\pi v>1-(7/10)^2/2>3/4\).

Combining (15)--(20), with \(\pi>25/8\), proves uniformly
\[
 W(t)
 <\frac15+\frac{17}{450}+\frac{17}{180}
                         +\frac{11}{150}
 =\frac{73}{180}<\frac12<L(q).                               \tag{21}
\]
The upper correction is therefore paid at a fixed finite height.
No upper infinite-height limit is used.

## 5. The central zero mode and every vertical current

In the complete prewall strip \(0<t<d\), at every finite height,
\[
 \Re Q_{ss}
  =\pi\Re\{\cot\pi(s+a)+\cot\pi(s+q)-3\cot\pi s\}<0.
 \tag{22}
\]
The own cotangent is positive in real part, and both shifted
cotangents are negative. This is the all-height inequality in
the zero-lift theorem; it also follows directly from its
cotangent formula.

Consequently the horizontal restriction at height \(h_*\)
is strictly concave and has its maximum \(\Re\Theta\) at \(t_*\).
At either real cut, \(F\) is convex in height.
Moving the unweighted central integral from height zero to \(h_*\)
therefore bounds each of its two joins by the larger of
\(\Re\Theta\) and its real-cut rate. Section 3 bounds those
real-cut rates by \(L(q)\).

For \(\eta\le0\), both shifted logarithm arguments have
nonpositive imaginary part, and the own argument has
nonnegative imaginary part. Hence
\[
             \Im Q_s(t+i\eta;a,q)\le2\pi a\le7\pi/4.
 \tag{23}
\]
It follows that
\[
              \partial_\eta\{F(t,\eta)+2\pi\eta\}\ge\pi/4.
 \tag{24}
\]
Choose a sufficiently tall but fixed lower height \(-T<h_*\),
uniformly on (2). Compactness and (24) make its entire weighted
horizontal rate smaller than
\(\min_{(a,q)}\Re\Theta(a,q)-1\).
Every lower weighted vertical half is bounded by its real endpoint
by (24).

On the upper half \(0\le\eta\le H\), the function
\(F(t,\eta)-2\pi\eta\) is convex by (22).
At a real cut its two endpoint bounds are the real rate,
at most \(L(q)\), and the upper rate (21).
Thus both upper weighted vertical halves are bounded by \(L(q)\).
Together these statements retain all four weighted vertical halves,
the two horizontal sampling corrections, and both unweighted joins.

## 6. The exact finite contour and the numerator walls

Use the original negative-root factorial from Section 6 of the
positive-output source:
\[
 \Pi_N(w)=G_N(Nw)
  \exp\{\tfrac{\pi i}{2}[N(w-w^2)-w]\},\qquad E_N(w)=1/\Pi_N(w).
 \tag{25}
\]
Here \(G_N\) is the normalized sine factorial, and
\(\Pi_N(j/N)=P_j\). The exact interpolated summand is
\[
 T_N(s)=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(q+s)
                         E_N(a)E_N(q)E_N(s)^3.               \tag{26}
\]
Its value at \(s=j/N\) is exactly the summand of (1),
including the incoming carrier.
Every factorial argument in the rectangle
\([\ell,r]+i[-T,H]\) stays in a fixed compact subset of the
original regular strip. In particular both shifted real parts
are at most \(1-\varepsilon\).
The canonical complex factorial expansion gives, with any
prescribed allowance, the upper rate \(F(t,\eta)\) for (26).
The normalization is exactly (3).

Choose inward half-grid cuts \(\ell_N,r_N\) tending to \(\ell,r\).
For sufficiently large \(N\) they enclose \(t_*\), stay before both
walls, and preserve every strict regularity margin.
The exact split-cotangent identity is
\[
\begin{split}
 \sum_{j/N\in(\ell_N,r_N)}T_N(j/N)
 ={}&N\int_{\ell_N}^{r_N}T_N(s)\,ds\\
 &+\frac{N}{2i}\left\{
 \int_{\partial R^+_{\rm off}}T_N(s)(\cot\pi Ns+i)\,ds+
 \int_{\partial R^-_{\rm off}}T_N(s)(\cot\pi Ns-i)\,ds
 \right\}.
\end{split}                                                    \tag{27}
\]
The boundaries have their induced orientations. This is the
identity (46) in the positive-output proof: the zero mode has
coefficient \(+N\), and both off-real horizontal sides and all
four vertical halves remain present.
On an exact half-grid vertical side the matching cotangent factor
has modulus at most \(2e^{-2\pi N|\Im s|}\); on the horizontal
sides a bound with constant four holds for large \(N\).
Sections 4--5 therefore estimate every current of (27).

Every index outside the central block is retained on the real
axis. Section 3 estimates its integrated physical rate, including
indices at or beyond either numerator zero.
For clarity, the uniform finite-product upper estimate follows
by replacing each numerator logarithm by
\(\log(|1-e^{-2\pi i(x+v)}|+\delta)\), first with fixed
\(\delta>0\). Its upper Riemann sums are uniform in the compact
parameter set. The integral error tends uniformly to zero as
\(\delta\downarrow0\), because these are simple logarithmic zeros.
The own factorial has
\(\log|P_j|=NJ(j/N)+O(\log N)\), uniformly for \(j<N\).
Thus every actual row has rate \(E_a(j/N;q)\) with an arbitrarily
small allowance. No zero is divided out and no row is removed.
This is precisely the zero-safe argument in the conditional
contour-allowance source, applied directly to (1).

The moving minimum \(d=\min(1-a,1-q)\) is continuous; no derivative
of that minimum is used. The collar, rectangle heights, and
regularizers are fixed before \(N\). Their rates are uniformly
continuous, so half-grid displacement has an arbitrarily small
total cost. There are finitely many contour pieces and at most
\(N\) physical rows. Assigning the prescribed allowance once
proves (5).

The proof uses no period continuation across a numerator wall:
the contour stops before both walls and the complete later row
block is estimated in its original polynomial form. It therefore
needs neither a choice between the two upper polynomial roots
nor a discarded alias on another logarithmic lift.

## Direct source versions

| Direct source | SHA-256 | Implication used |
|---|---|---|
| research_mixed_real_unit_pair_zero_lift_branch.md | 4e22a14247e7b11340d9b9ade4774760cd93722f82feb16c12ff2faa1c2b4d1a | Original zero-lift critical point, compact strict margins and all-height prewall concavity |
| research_mixed_four_conditional_positive_output_real_arc.md | f3c971ea0c2c24f82c2250db5c8c1196a9700b6d3bb57849cf4130f4353cc0c2 | Incoming/own lower-cut inequalities, elementary real-row constants, and exact normalized finite summand and residue identity |
| research_mixed_443_far_real_first_arc.md | 21170ee7d4fbeb0c01e7fe440d31a3f356480b68c249f51efa1bd68bc068e6c3 | The explicit lower bound for \(L(q)\) and its outgoing sine estimate |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 | Uniform complex factorial expansion on original regular strips |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 | Uniform zero-safe finite-product upper estimate through numerator zeros |

The changed outgoing domain is checked explicitly above. No finite
theorem requiring an outgoing lower semicircle is applied on (2).
The entire final proof and all five directly used source implications
were read in full, and all five source hashes match. Separate full
proof and direct-source review is required before adoption.
No mathematical numerical evaluation, saved-value arithmetic, test,
import, compilation, or frozen-source edit is used.
