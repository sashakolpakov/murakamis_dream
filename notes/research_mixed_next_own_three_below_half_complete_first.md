# The own-three lower half with the complete first factor

Private research proof, 8 November 2026. The first last-row
alternative is below the first real low row once the shared
coordinate is at least \(1/10\). Before that point, its product
with every next own-three main profile increases toward
\(1/10\), including when the actual next main height is positive.
This pays the missing first-upper by next-below-half combinations.

All original finite currents, physical low rows, both parities,
and the complete shared Fourier polynomial are retained. The
theorem is central-first and ordinary-next only. No numerical
evaluation or modification of a frozen input is used.

## 1. Literal finite source and existing controlling profiles

Use the actual ordinary-next own-three references and original
planes of
[the complete-first wedge theorem](research_mixed_next_own_three_upper_wedge_complete_first.md).
In particular
\[
\begin{gathered}
a=x+ih_a,\quad y=q+ih_y,\quad z=u+ih_z,\qquad
x,u\in P=[11/50,9/20],\quad 0\le q\le11/50,\\
-.072<h_a<0,\qquad -.102<h_y<-.001 .
\end{gathered}
\tag{1}
\]
All actual typed-reference correlations and the original next
index height \(h_t\) are retained. The own-three height \(h_t\)
may have either sign. Put
\[
X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz},
\quad R=e^{2\pi h_y}\in(13/25,1),\quad
\delta_a=-2\pi h_a.
\]
The original radial bounds used in
[the joint-profile proof, Section 3](research_mixed_next_lower_left_joint_main_profiles.md)
give
\[
e^{2\pi h_t}<8/5,\qquad e^{-2\pi h_t}>13/20.
\tag{2}
\]

Let \(r=e^{-2\pi i/N}\), \(D=N-1\), \(P_j=(r;r)_j\),
and \(p_j(W)=(rW;r)_j\). Define the literal next lower half
and the positive first upper block by
\[
\begin{split}
C_{0,N}^{<1/2}(Y,Z)
 &=\sum_{j=0}^{\lceil N/2\rceil-1}
              \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2},\\
\mathcal V_{1,N}^{\ge1/2}(X,Y)
 &=\sum_{i=\lceil N/2\rceil}^{D}
              \left|\frac{X^{-i}p_i(X)p_i(Y)}{P_i^3}\right|.
\end{split}
\tag{3}
\]
The first complete kernel is the original \(C_{1,N}(X,Y)\).
The next own flag is zero, so there is no outgoing halfweight.
The complete shared weight remains \(d_N(Y)\).

**Theorem.** Uniformly on (1), for all real ordinary colors
and all sufficiently large levels of both parities,
\[
\begin{split}
&|U_{0,N}(w,X)d_N(Y)|\,
 \mathcal V_{1,N}^{\ge1/2}(X,Y)
 \,|C_{0,N}^{<1/2}(Y,Z)|
 \le C N^B e^{N\{\Lambda_{123}(z)-10^{-11}\}},\\
&|U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)
                   C_{0,N}^{<1/2}(Y,Z)|
 \le C N^B e^{N\{\Lambda_{123}(z)-10^{-11}\}} .
\end{split}
\tag{4}
\]
Arbitrary subsets of the first positive block obey its bound.
No arbitrary-subset assertion is made for the next middle sum.
The central first incoming integral has the same exponential
bound with its original measure \(+N\,da\). Fixed-base signed
partial sums and that integral have normalized local mixed
jets with gap \(10^{-12}\).

We recall the precise profile inputs. Write
\[
\begin{split}
Q_0(t;y,z)
 &=g(y+t)+g(z+t)-2g(t)-g(y)-g(z)+2\pi iyt,\\
E_\gamma(v;b,c)&=\Re Q_\gamma(v;b,c),\qquad v\ \hbox{real}.
\end{split}
\]
The complete cap plane is \(B_U(x)\), and the final affine plane
\(\Lambda_{123}(z)\) has no target \(q\) dependence. Sections
3 and 6 of the joint-profile theorem pay
\[
B_U(x)+E_1(1/8;a,y)+\Re Q_0(t;y,z)-\Re g(y)
 <\Lambda_{123}(z)-10^{-10}
\tag{5}
\]
for the next main at its actual height and for its real low
and half cuts \(t=3/20,1/2\), on the entire interval (1).
The theorem also pays the first real half alternative paired
with those next profiles. These are profile inequalities;
neither is inferred from cancellation in a finite sum.

The first upper-row theorem,
[Section 2](research_mixed_next_lower_left_own_four_upper_rows.md),
gives for any fixed tolerance \(\tau>0\)
\[
\mathcal V_{1,N}^{\ge1/2}
 \le C_\tau N^{B_\tau}
 e^{N\{\max(E_1(1/2;a,y),\delta_a)+\tau\}} .
\tag{6}
\]
Its domain is exactly the first and shared domain in (1).
Thus only the first last alternative \(\delta_a\) is new.

## 2. Same-point domination of the first last alternative

For \(q\ge1/10\), we prove the uniform comparison
\[
                     E_1(1/8;a,y)-\delta_a>3/2000.
\tag{7}
\]
The exact original physical rate, including its incoming chirp, is
\[
E_1(1/8;a,y)-\delta_a
=I_a(1/8)+I_y(1/8)-3J(1/8)-\tfrac78\delta_a,
\qquad
I_b(\ell)=\int_0^\ell
       \log|1-e^{-2\pi i(b+v)}|\,dv .
\tag{8}
\]
No factorial or Fourier allocation has been absorbed into \(I_b\).

For any nonnegative radius \(\rho\),
\[
|1-\rho e^{-2\pi is}|
\ge
\begin{cases}
\sin(2\pi s),&0<s\le1/4,\\
1,&1/4\le s<1/2.
\end{cases}
\tag{9}
\]
This is the minimum of the squared modulus as a quadratic
in \(\rho\). On \(0\le v\le1/40\), the real part \(q+v\)
is at least \(1/10\), so (9) gives a modulus greater than
\(1/2\). On \(1/40\le v\le1/8\), it is at least \(1/8\),
so the modulus is at least \(1/\sqrt2\). All these real parts
are at most \(11/50+1/8=69/200<1/2\).
Consequently, using \(\log2<7/10\),
\[
I_y(1/8)>-\left(\frac1{40}+\frac1{20}\right)\log2
                       >-\frac{21}{400}.
\tag{10}
\]

The other three terms in (8) have the exact elementary bounds
recorded in
[central-four completion, equations (11)--(12)](research_mixed_next_lower_left_central_four_completion.md):
\[
I_a(1/8)>0,\qquad -J(1/8)>3/20,\qquad
\delta_a<18\pi/125 .
\tag{11}
\]
For clarity, the first bound uses \(e^{2\pi h_a}>5/8\),
\(x+v\in[.22,.575]\), and
\[
|1-e^{2\pi h_a-2\pi i(x+v)}|^2>73/64>1.
\]
The sine-integral bound in (11) is the same printed
elementary bound used there; it is not a new action evaluation.
Since \(\pi<22/7\), (8)--(11) give
\[
E_1(1/8;a,y)-\delta_a
>\frac9{20}-\frac{63\pi}{500}-\frac{21}{400}
>\frac{27}{500}-\frac{21}{400}
=\frac3{2000}.
\]
This proves (7). Every next factor and every outside weight
may remain attached: this is a same-point comparison in the
first index only.

## 3. Transport on the remaining initial tenth

Keep the first last alternative attached and define
\[
\mathcal A(t;x,q,u)
=B_U(x)+\delta_a+\Re Q_0(t;y,z)-\Re g(y).
\tag{12}
\]
At any fixed next index height \(\sigma\), its exact derivative is
\[
\partial_q\mathcal A
=\log|e^{-2\pi\sigma}-R e^{-2\pi i(q+t_R)}|
                         -2\log|1-Y|.
\tag{13}
\]
The factor \(e^{-2\pi\sigma}\) comes from the original
incoming chirp. In particular (13) does not replace a
positive-height main by a negative-height one.

First consider the next main \(\sigma=h_t\).
The own-three lower clipping in the joint-profile theorem,
Section 3, increases any main value with
\(3/20\le t_R<1/6\) until \(t_R=1/6\), at its unchanged
height and current \(q\). This is its own-three force proof
with two own factorials; no own-four upper clipping is used.
Thus it suffices to keep a fixed main index
\[
                         1/6\le t_R\le1/2.
\tag{14}
\]

For \(0\le q\le1/10\), convexity in \(R\in[1/2,1]\) and
\(\cos(2\pi q)\ge\cos(\pi/5)>4/5\) give
\[
D_q:=|1-Y|^2
 <1+R^2-\tfrac85R\le9/20 .
\tag{15}
\]
Put \(A=e^{-2\pi h_t}>13/20\).
The shifted real part in (13) lies in \([1/6,3/5]\).
If its cosine is nonpositive, the numerator modulus is
at least \(A\). Otherwise its real part lies in \([1/6,1/4)\);
minimizing the squared modulus over \(R\ge0\) gives
\[
|A-R e^{-2\pi i(q+t_R)}|
\ge A\sin(2\pi(q+t_R))
\ge A\sqrt3/2>13/25 .
\tag{16}
\]
The last inequality uses \(\sqrt3/2>4/5\).
Equations (13)--(16) therefore prove, for either sign of \(h_t\),
\[
                       \partial_q\mathcal A>\log(52/45)>0.
\tag{17}
\]
Transport the fixed clipped index to \(q=1/10\).
There (7) replaces the first last alternative by the first
real low row, and (5) applies at the same actual main height.
Thus every original main profile obeys
\[
              \mathcal A<\Lambda_{123}(z)-10^{-10}
                       \qquad(0\le q\le11/50).
\tag{18}
\]
For \(q\ge1/10\), this follows directly from (7) and (5).
For \(q\le1/10\), it follows from the clipping, (17),
and the same endpoint comparison. No reference is moved.

At the next real low cut \(t=3/20\), the numerator in (13)
has \(A=1\). Its shifted real part is in \([3/20,1/4]\)
on the initial tenth, so the numerator is greater than
\(1/2\) by (9). Together with (15), this gives
\[
                 \partial_q\mathcal A(3/20)>\log(10/9)>0.
\tag{19}
\]
The identical endpoint argument proves (18) for this real cut.

For the next real half cut, Section 2 of the complete-first
wedge theorem already proves the stronger bound
\[
B_U(x)+\delta_a+E_0(1/2;y,z)-\Re g(y)
                       <\Lambda_{123}(z)-1/18000 .
\tag{20}
\]
It uses the actual own-three half-row certificate; it does not
borrow the own-four main-height or clipping hypotheses.

## 4. All finite pieces and the remaining next upper rows

The next positive low block is exactly
\(0\le j\le\lfloor3N/20\rfloor\). By
[the low-physical theorem](research_mixed_next_lower_left_low_physical_blocks.md),
its uniform factorial upper bound increases to the real
cut \(3/20\), including the exact zero row equal to one.
Thus (18)--(19) pay that whole positive block with the
first last alternative attached.

The remaining next indices are
\[
\lfloor3N/20\rfloor+1\le j\le\lceil N/2\rceil-1.
\]
Use the exact canonical interpolation and half-grid cuts of
[the complete-current theorem](research_mixed_next_lower_left_complete_currents.md).
Its two horizontal aliases have heights \(-1/5\) and \(4\).
Both aliases, all four weighted vertical halves, and both
unweighted main joins reduce at the same \(q\) to the main,
real-low and real-half profiles just paid. This reduction
already proves the needed vertical convexity for the actual
positive own-three height as well as for negative heights.
The first last alternative is independent of this next index,
so it remains attached throughout. No weighted or unweighted
piece is discarded.

The cuts differ from \(3/20\) and \(1/2\) by \(O(1/N)\).
The fixed strict margins above pay their regular bounded
changes, including the possible \(O(1/N)\) extension of the
main real interval. Both parities use the literal conventions
in (3). At \(q=0\) the canonical factorial symbol is supplied
by [the inward-seam theorem](research_factorial_symbol_across_inward_seam.md);
the full Fourier polynomial separately obeys the forced upper
bound of the low-physical theorem. No relative asymptotic
for \(d_N\), and no division by a vanishing finite weight,
is used.

Combining this next lower-half reduction with (6) proves the
first line of (4): the first half alternative is an original
paid joint profile, and the first last alternative is paid by
(18)--(20). The first-below-half by next-below-half product
was already completed by the joint-profile, low-physical and
complete-current theorems. Adding it proves the second line
of (4). Allocate the finitely many product tolerances inside
the displayed phase margins to retain the stated finite gap.
The original \(+N\) first integration, all-real color
derivatives, and fixed-base holomorphic Cauchy argument give
the claimed integral and normalized-jet scope.

There is a useful exact combined statement. At a fixed base
target \(q\), put
\[
J_N(q)=\lfloor N(18/25-q)\rfloor,\qquad
C_{0,N}^{\mathrm{ret}}(Y,Z;q)
 =\sum_{j=0}^{J_N(q)}
              \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2}.
\tag{21}
\]
For large \(N\), \(J_N(q)\ge\lceil N/2\rceil-1\).
Adding the already paid positive upper wedge to (4) gives
\[
|U_{0,N}C_{1,N}d_N(Y)C_{0,N}^{\mathrm{ret}}|
 \le C N^B e^{N\{\Lambda_{123}(z)-10^{-11}\}} .
\tag{22}
\]
For local jets the integer \(J_N(q)\) is frozen at the base
point; it is never differentiated. Only the next physical
indices \(J_N(q)<j<N\) remain outside this central-first
own-three partial-source bound. Noncentral first incoming
pieces and the other outgoing contour intervals are also
separate. No complete next own-three transfer is asserted.
