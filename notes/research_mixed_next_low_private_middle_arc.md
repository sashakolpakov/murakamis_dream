# Removing the lower private rows on the middle incoming arc

Research deduction, 7 November 2026. The private indices \(j/N\le1/8\)
have an exponential gap on the remaining real first-coordinate arc
\([1/2,7/10]\). The estimate couples the incoming angle with the
complete endpoint-coefficient profile before maximizing. It retains
the conditional polynomial's degree less than \(N/2\), which reduces
the cost of the selected outgoing radius.

This is a bound for an original finite index region. It introduces
no contour deformation and pays no unweighted connecting segment.
The remaining private indices and the initial vertical incoming
connector are separate. No numerical evaluation is used.

## 1. The literal source and its two retained index sets

Put \(D=N-1\), \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\(p_j(X)=(rX;r)_j\). On

\[
 \frac12\le a\le\frac7{10},\qquad
 v=1-a\in[3/10,1/2],\qquad X=e^{-2\pi ia},
 \tag{1}
\]

keep the exact conditional cuts of
[the end-range theorem, Section 3](research_mixed_next_selected_first_wall_rows.md):

\[
 \begin{split}
 L_N&=\lfloor N/16\rfloor+1,\qquad
 K_N(a)=\lceil N(v-\varepsilon)\rceil,\\
 C_{1,N}^{\rm mid}(X,Y)
   &=\sum_{k=L_N}^{K_N(a)-1}
             \frac{X^{-k}p_k(X)p_k(Y)}{P_k^3}.
 \end{split}
 \tag{2}
\]

The fixed \(\varepsilon>0\) is that source's wall collar.
All statements below concern sufficiently large levels, when the
cuts are ordered. The omitted conditional rows already have a
gap with the whole original cap retained.

Define the lower private part by

\[
 U_{0,N}^{\rm low}(w,X)
   =\sum_{j=0}^{\lfloor N/8\rfloor}
                  H_N(w,r^{-j})\,\frac{p_j(X)}{P_j}.
 \tag{3}
\]

Every \(H_N\) in (3) is the entire coherent endpoint polynomial.
Its internal Newton sum is not replaced by a positive sum.
This distinction is essential to the rate used below.

For every real \(q\), \(\lceil q\rceil-1<q\). Hence, also at
integer cut locations,

\[
 \deg_Y C_{1,N}^{\rm mid}
       \le K_N(a)-1<N(v-\varepsilon)<Nv\le N/2.
 \tag{4}
\]

The private factor is independent of \(Y\). Neither (3) nor (4)
uses physical termination at the continuous incoming coordinate \(a\).
Both parities, the constant private row and all numerator zeros remain.

## 2. A joint bound before taking the private maximum

Let \(J\) be the continuous one-periodic real primitive of
\(\log(2|\sin\pi e|)\), normalized by \(J(0)=0\). Use the original
endpoint action \(S\), and put

\[
 \begin{split}
 h(e)&=\Re S(e)+J(e),\qquad b_0=101/125,\\
 B_v(e)&=J(e-v)+J(v)-J(e),\\
 A(v)&=J(v)-2J(v/2),\qquad
 d_v=\pi\cot(\pi v/2).
 \end{split}
 \tag{5}
\]

The source and curvature statements in
[the coherent cap theorem, Sections 1--3](research_mixed_next_coherent_cap_far_arc.md)
give

\[
 \begin{split}
 h(e)&\le b_0-\frac95(1/2-e)^2,\qquad 0\le e\le1/2,\\
 B_v(e)&\le A(v)-d_v(e-v/2)^2,\qquad 0\le e\le v.
 \end{split}
 \tag{6}
\]

On compact physical private intervals the complete row in (3) has
upper rate \(h(e)+B_v(e)\), with an arbitrarily small fixed
tolerance. The all-real color and local complex-color scope follows
from the whole-coefficient bounds cited in that theorem; it is not
a comparison of the signed values of the cap at different colors.

The same continuous numerator and sine-factorial estimates give
the positive conditional-row bound

\[
 \sup_{|Y|\le1}|C_{1,N}^{\rm mid}(X,Y)|
       \le C_\tau N^{A_\tau}
             e^{N\{A(v)+7/15+\tau\}}.
 \tag{7}
\]

In (7), the constant \(7/15\) bounds the full profile
\(L(t)-2J(t)\), \(L(t)=-2J((1-t)/2)\), on all \(0\le t\le1\).
The incoming chirp has modulus one. In particular (7) bounds
the positive sum of the retained conditional rows, without an
assumption about their signs.

Thus the joint compact-row rate is at most

\[
 \mathcal R(v,e)=
 b_0+2A(v)+\frac7{15}
       -\frac95(1/2-e)^2-d_v(e-v/2)^2,
 \quad 3/10\le v\le1/2,\quad 0\le e\le1/8.
 \tag{8}
\]

**Lemma 1.** On this whole rectangle,

\[
                        \mathcal R(v,e)<\frac{99587}{64000}.
 \tag{9}
\]

*Proof.* First fix \(e\). Write
\(\theta=\pi v/2\) and \(b=v/2-e\), so \(b>0\).
Direct differentiation and completion of a quadratic give

\[
 \begin{split}
 \frac{d}{dv}\{d_vb^2\}
   &=d_vb-\frac{\pi^2}{2}\csc^2\theta\,b^2\\
   &\le\frac{d_v^2}{2\pi^2\csc^2\theta}
      =\frac12\cos^2\theta\le\frac12.
 \end{split}
 \tag{10}
\]

Meanwhile

\[
 A'(v)=\log(2\cos(\pi v/2)),\qquad
             2A'(v)\ge\log2>\frac12.
 \tag{11}
\]

Therefore (8) is strictly increasing in \(v\), and its maximum
is bounded by its value at \(v=1/2\). At that endpoint \(d_v=\pi\);
both negative squares in

\[
 b_0+2A(1/2)+7/15-\frac95(1/2-e)^2-\pi(e-1/4)^2
 \tag{12}
\]

increase as \(e\) runs from zero to \(1/8\).
Their maximum on the required range is at \(e=1/8\).
The already proved bound
\(A(1/2)=b_2/2<7/24\) is recorded with its rational witnesses in
[the wrapped-private theorem, equation (13)](research_mixed_next_wrapped_private_sector.md).
Together with \(\pi>25/8\), it gives

\[
 \begin{split}
 \mathcal R(v,e)
 &<\frac{101}{125}+\frac7{12}+\frac7{15}
                   -\frac{81}{320}-\frac{25}{512}\\
 &=\frac{929}{500}-\frac{773}{2560}
   =\frac{99587}{64000}.
 \end{split}
 \tag{13}
\]

All bounds in this argument are analytic or rational; no new scalar
evaluation is involved. \(\square\)

The compact private-row estimate must not be extrapolated to \(j=0\).
Choose the fixed small true-end width from
[the complementary real-color theorem, Section 2](research_mixed_three_four_complementary_real_colors.md).
Its positive lower-end bound on the entire disk \(|X|\le1\) is

\[
 \sum_{j/N\le\delta_0}
       |H_N(w,r^{-j})|\,|p_j(X)|/|P_j|
                       \le CN^A e^{3N/5}.
 \tag{14}
\]

Shrink \(\delta_0\) below \(1/8\) if necessary; every subset retains
this positive bound. Multiplying (14) by (7), and using
\(A(v)<7/24\), gives the smaller rate

\[
                 \frac35+\frac7{24}+\frac7{15}
                      =\frac{163}{120}<\frac{99587}{64000}.
 \tag{15}
\]

Apply (6)--(9) only to the remaining compact private range
\([\delta_0,1/8]\). Its finite row count costs a power of \(N\).
We have proved, for every fixed small \(\tau>0\),

\[
 \sup_{|Y|\le1}
 |U_{0,N}^{\rm low}(w,X)C_{1,N}^{\rm mid}(X,Y)|
 \le C_\tau N^{A_\tau}
           e^{N\{99587/64000+\tau\}}.
 \tag{16}
\]

The proof bounds the positive sum over complete private rows and
conditional rows. Thus it also applies to any subsets of those
index ranges. It holds for every real ordinary color and on a
sufficiently small fixed disk about complete color, at both parities.

## 3. The original selected radius and action comparison

Retain the ordinary-next canonical family and the original absolute
affine action \(\Lambda_{123}(z)\) from
[the full selected-plateau comparison, equations (3)--(8)](research_mixed_next_filtered_selected_plateau.md).
Its flags are \((0,1,\beta)\), \(\beta=0,1\), and its following
ordinary parameter is \(c=s_4^*\in K_3\cup K_4\). Put

\[
 P=[.22,.45],\quad
 y=x+i/100,\quad x\in P,\quad Y=e^{-2\pi iy},\qquad
 z=u+i\Im z_*,\quad u\in P,\quad Z=e^{-2\pi iz}.
 \tag{17}
\]

This does not substitute a terminal third-vertex graph.
By (4) and the exterior polynomial maximum principle, (16) gives

\[
 |U_{0,N}^{\rm low}(w,X)C_{1,N}^{\rm mid}(X,Y)|
 \le C_\tau N^{A_\tau}
         e^{N\{99587/64000+\pi/100+\tau\}}.
 \tag{18}
\]

The selected-plateau proof uses its first two factors only through
their selected-radius ceiling \(77/50+\pi/50\).
It retains the actual marginal of the first pair, both factorial
and polynomial-forcing alternatives of \(d_N(Y)Y^{-N}\), the
entire third conditional factor, and its original outgoing halfweight.
The improvement in (18) relative to that ceiling is

\[
 \frac{\pi}{100}
        -\left(\frac{99587}{64000}-\frac{77}{50}\right)
 =\frac{\pi}{100}-\frac{1027}{64000}
 >\frac{973}{64000}.
 \tag{19}
\]

Adding the original raw gap \(1/500\) leaves more than

\[
          \frac{973}{64000}+\frac1{500}
              =\frac{1101}{64000}>\frac1{60}.
 \tag{20}
\]

**Theorem 2.** Uniformly on (1), (17), the original finite product
obeys

\[
 \begin{split}
 &|U_{0,N}^{\rm low}(w,X)C_{1,N}^{\rm mid}(X,Y)
       d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)|\,|d_N(Z)|^{\beta/2}\\
 &\hspace{12mm}\le C_\tau N^{A_\tau}
          e^{N\{\Lambda_{123}(z)-1/60+\tau\}} .
 \end{split}
 \tag{21}
\]

This holds for both parities, every real ordinary color and a
sufficiently small fixed complete-color neighborhood, with an
arbitrarily small prescribed additional tolerance. For \(\beta=0\)
there is no outgoing weight. A finite gap \(1/120\) remains after
the common tolerances and polynomial factors.

For real ordinary derivatives apply Markov to each complete endpoint
polynomial before the positive private sum. Fixed complex derivatives
follow on smaller color disks. For outside-parameter derivatives,
hold each base contour and its integer cut sets fixed. The finite
Laurent products and their zero-safe bounds admit fixed complex
neighborhoods with arbitrarily small extra exponential allowance;
Cauchy's formula then applies. Near the actual outgoing reference,
the original nonzero type-four weight, when present, has its
factorial asymptotic and can be converted to the original local
conditional action. Every fixed normalized mixed derivative may
be bounded with gap \(1/240\) on smaller neighborhoods. On the
independent outgoing plateau (21) remains a weighted estimate,
with no division through a possible zero of \(d_N(Z)\).

## 4. Exact contribution and the remaining source

The removed part of the original selected double integral is

\[
 N^2\int_{P+i/100}\int_{1/2}^{7/10}
 U_{0,N}^{\rm low}(w,e^{-2\pi ia})
 C_{1,N}^{\rm mid}(e^{-2\pi ia},Y)
 d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)\,da\,dy .
 \tag{22}
\]

The original two factors \(N\), both increasing orientations and
every change of the integer upper cut \(K_N(a)\) are retained.
Bounded integration lengths and finite sums cost only polynomial
factors. Equation (22) is not a subset of a root-of-unity average.

The real-main reduction in
[the conditional-alias theorem](research_mixed_next_far_half_conditional_aliases.md)
can be made after the split (3). Its alias bounds use a positive
cap-row majorant. Here the private subset has such a majorant:
from (6), (10)--(11), or simply \(B_v\le A(v)\),

\[
 h(e)+B_v(e)
 \le b_0-\frac{81}{320}+\frac7{24}
 <\frac{1549}{1500}\qquad(0\le e\le1/8),
 \tag{23}
\]

and the true lower end has the still smaller rate (14).
Thus the alias proof's original cap ceiling applies to this
subset directly. It is not inferred by subtracting bounds for
signed complete caps. Replacing the retained conditional polynomial
in (22) by
\(N\int_{\ell_N}^{u_N(a)}T_N(t;a,y)\,dt\) leaves only its already
paid alias error, with both half-grid cuts unchanged.
No additional unweighted connector is thereby paid.

Combining (21) with the wrapped-private theorem removes the two
disjoint private ranges

\[
                e\le1/8,\qquad e\ge1-a-\delta_* .
 \tag{24}
\]

They are disjoint because \(1-a\ge3/10\) and \(\delta_*<1/20\).
After the previously paid conditional end ranges, the remaining
real joint source has

\[
 \boxed{\qquad
  \frac12\le a\le\frac7{10},\qquad
  \frac18<e<1-a-\delta_* ,\qquad
  \frac1{16}<t<1-a-\varepsilon .
 \qquad}
 \tag{25}
\]

In a real-main representation, the conditional integration endpoints
are its actual half-grid cuts, differing from the displayed lower
endpoint by \(O(N^{-1})\); both cuts are retained. The original
initial vertical segment from \(1/2+i\Im a_*\) to \(1/2\), all
later unweighted deformations, and the other second-coordinate
pieces remain outside the conclusion.
