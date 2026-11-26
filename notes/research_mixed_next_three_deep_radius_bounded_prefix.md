# Attaching a type-three block at deeper shared heights

Private research proof candidate, 8 November 2026. A preceding factor
whose exponential rate is at most \(2383/1500\) remains below the
original next action after attachment of the complete type-three
kernel, when the shared radius is at most \(7/10\). The comparison
allows the next private height to have either sign.

The upper-row reduction used in Section 5 is a separate input:
[the complete central deep-radius theorem](research_mixed_next_own_three_deep_radius_complete_central.md).
This note is not adopted until that input and the present proof have
completed their source and proof reviews. No numerical evaluation
or modification of a frozen input is used.

## 1. Actual source and the claim

Keep the actual ordinary-next references of types \((3,4,3)\),
the original primitive \(g\), and the action bound
\(\Lambda_{123}(z)\) from
[the low-cardinal localization theorem, Section 2](research_mixed_next_low_cardinal_paired_localization.md).
The targets and fixed reference heights satisfy
\[
\begin{gathered}
y=q+ih_y,\quad 0\le q\le q_0=11/50,\qquad
z=u+ih_z,\quad u\in P=[11/50,9/20],\\
-.102<h_y<-.001,\quad -.065<h_z<.068,\qquad
-.108\le h_t\le.068,\\
Y=e^{-2\pi iy}=R e^{-2\pi iq},\quad
Z=e^{-2\pi iz},\qquad 13/25<R\le7/10 .
\end{gathered}
\tag{1}
\]
Every actual reference correlation remains imposed. The height
\(h_t\) is the original next private-index height. In particular
\[
A:=e^{-2\pi h_t}>13/20,\qquad |Z|<43/28,
\tag{2}
\]
by the original own-three height bounds used in
[the complete-first lower-half theorem](research_mixed_next_own_three_below_half_complete_first.md).

For \(r=e^{-2\pi i/N}\), let
\[
P_j=(r;r)_j,\quad p_j(W)=(rW;r)_j,\qquad
C_{0,N}(Y,Z)=\sum_{j=0}^{N-1}
                 \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2}.
\tag{3}
\]
The Fourier polynomial is the original one:
\(\deg d_N\le N-1\) and \(d_N(r^b)=P_b^{-1}\).
There is no outgoing halfweight for this next type.

Set \(B_0=2383/1500\). Let \(V_N\) be any preceding factor for
which, for every \(\tau>0\),
\[
|V_N|\le C_\tau N^{B_\tau}e^{N(B_0+\tau)}
\tag{4}
\]
uniformly on the domain being considered. It may depend on other
parameters, provided the bound is uniform and those parameters do
not change the reference or its action.

**Theorem.** Under (1)--(4), at both level parities,
\[
\boxed{\quad
 |V_N d_N(Y)C_{0,N}(Y,Z)|
 \le C N^B e^{N\{\Lambda_{123}(z)-1/200\}} .
\quad}
\tag{5}
\]
This is an upper bound for the complete next sum and the complete
forced Fourier weight. No holomorphy assumption on \(V_N\) is
needed for (5). Derivative assertions require the corresponding
neighborhood hypothesis on that factor.

## 2. The old shared boundary has an explicit reserve

The original bare phase and physical real-row rate are
\[
\begin{split}
Q_0(t;y,z)
 &=g(y+t)+g(z+t)-2g(t)-g(y)-g(z)+2\pi iyt,\\
E_0(t;y,z)
 &=\int_0^t\log|1-Ye^{-2\pi ib}|\,db
   +\int_0^t\log|1-Ze^{-2\pi ib}|\,db
   -2J(t)-2\pi h_y t .
\end{split}
\tag{6}
\]
At \(q=q_0\), the original main profiles, real cuts \(3/20,1/2\),
and last row have their actual ordinary supporting bounds.
For an upper real row the complete right-tail theorem reduces
it to the half or last row. These are profile inequalities in
[ordinary source assembly, Sections 1--2](research_mixed_three_row_source_assembly.md);
no term is extracted from a coherently bounded sum.

The bare last rate is
\[
L_0=-\log R+2\pi(h_z)_+ .
\tag{7}
\]
In particular a positive outgoing height remains present.
The next supporting plane allocates exactly \(-\Re g(y)/2\).
The second shared halfweight remains outside that plane.

The original marginal cancellation is
\[
A_*+p(q-\alpha)+B_3(q,u)\le\Lambda_{123}(z),
\qquad \alpha=\Re y_* .
\tag{8}
\]
The two explicit comparisons in
[the original low-block theorem, equations (9)--(11)](research_mixed_conditional_lower_output_low_block.md)
apply to either next own type. At \(q_0\) they give the reserves
\[
\begin{array}{c|c}
p\le0& 7/4-B_0-11/80=143/6000>1/50,\\[1mm]
p\ge0&7/4+1/45-B_0-1/12-801/10000
                         =1811/90000>1/50 .
\end{array}
\tag{9}
\]
The second line uses its original \(A_*>7/4+819/35200\).
It follows that each of
\[
\mathcal A(t;q)=B_0+\Re Q_0(t;y,z)-\Re g(y),
\qquad
\mathcal A_{\rm last}(q)=B_0+L_0-\Re g(y)
\tag{10}
\]
is less than \(\Lambda_{123}(z)-1/50\) at \(q=q_0\), for its
stated controlling profiles. The same is true of
\(B_0+E_0(t;y,z)-\Re g(y)\) for every upper real row there.

## 3. Transport the main and real low profiles

The original own-three lower clipping increases any main profile
with \(3/20\le\Re t<1/6\) to its value at \(1/6+ih_t\).
This is Section 3 of
[the joint-profile theorem](research_mixed_next_lower_left_joint_main_profiles.md).
We retain its full remaining range \(1/6\le t_R\le1/2\), with
the actual height \(h_t\). No own-four upper clipping is used.

At a fixed such index the exact derivative, including the chirp, is
\[
\partial_q\mathcal A
=\log|A-R e^{-2\pi i(q+t_R)}|-2\log|1-Y|.
\tag{11}
\]
Write \(D_q=|1-Y|^2\). On \(0\le q\le1/10\), the proof of the
complete-first lower-half theorem gives \(D_q<9/20\) and
the numerator modulus in (11) greater than \(13/25\).
Thus (11) is positive, even when \(h_t>0\).
For the real low cut \(t=3/20\), its numerator exceeds \(1/2\),
so that derivative is positive as well.

On \(1/10\le q\le3/20\), the shifted main real part lies in
\([4/15,13/20]\), where its cosine is negative. Hence its
numerator square is greater than
\[
(13/20)^2+(1/2)^2=269/400>16/25.
\]
The real low cut has the same nonpositive cosine and a larger
radial lower bound. Since \(\cos(2\pi q)>7/12\), convexity in
\(R\in[1/2,7/10]\) gives
\[
D_q\le\max\{2/3,101/150\}=101/150<7/10.
\]
Both derivatives are again positive.

On the last two intervals use the following squared numerator
and denominator bounds:
\[
\begin{array}{c|c|c|c}
q\text{ range}&D_q\le D(R)&
|A-R e^{-2\pi i(q+t_R)}|^2\ge U(R)&
\text{ratio lower bound}\\ \hline
[3/20,1/5]&1+R^2-3R/5&
169/400+R^2+39R/100&9/10\\
[1/5,11/50]&1+R^2-9R/25&
169/400+R^2+117R/500&4/5 .
\end{array}
\tag{12}
\]
The shifted cosines are respectively less than \(-3/10\)
and \(-9/50\), while the unshifted cosines are greater than
\(3/10\) and \(9/50\). For the first interval all main and
real-low shifted coordinates lie in \([3/10,7/10]\).
For the second they lie in \([7/20,18/25]\).
The endpoint witnesses are the pentagon cosine bound and
\(\sin(3\pi/50)>37/200>9/50\), already used in the enlarged
band proof. The squared moduli increase with \(A>0\) when
these shifted cosines are negative, so (2) proves (12) for
the main; \(A=1\) proves it also for the real low cut.

Here is a direct check of the last column, retaining the common
radius. For the first row \(U-(81/100)D^2\) is strictly concave
on \([1/2,7/10]\): the second derivative of \(D^2\) is at least
\(103/25\), whereas \(U''=2\).
Its endpoint values are
\[
5459/40000,\qquad 258131/1000000 .
\]
For the second row, \(U-(16/25)D^2\) is also strictly concave:
the second derivative of \(D^2\) is at least \(3187/625\).
Its endpoint values are
\[
14191/250000,\qquad 596299/6250000 .
\]
All four values are positive. Thus the derivatives in (11)
are greater than \(-\log(10/9)\) and \(-\log(5/4)\), respectively.
The total possible increase when transporting a target back
from \(q_0\) is therefore less than
\[
\frac1{20}\log(10/9)+\frac1{50}\log(5/4)
<\frac1{180}+\frac1{200}=\frac{19}{1800}.
\tag{13}
\]
We used only \(\log(1+x)<x\).
Combining with (9), every main and real low profile satisfies
\[
\mathcal A(t;q)<\Lambda_{123}(z)-17/1800 .
\tag{14}
\]

The real half profile has the stronger monotone comparison on
this radial domain. Its derivative is
\[
\frac12\log(1+R^2+2R\cos2\pi q)
-\log(1+R^2-2R\cos2\pi q)>0.
\tag{15}
\]
Section 2, equations (9)--(10), of
[the complete-first upper-wedge theorem](research_mixed_next_own_three_upper_wedge_complete_first.md)
proves this sign on \(R\le7/10\) using a concave polynomial
with endpoint values \(2851/10000\) and \(52339/250000\).
That calculation concerns the displayed derivative itself;
its preceding factor is constant in \(q\). Hence the present
half profile keeps its full \(1/50\) reserve.

## 4. The last profile and the already bounded upper band

Only \(-\Re g(y)\) in \(\mathcal A_{\rm last}\) depends on \(q\).
The exact weight comparison in Section 4 of
[the bounded-prefix type-four theorem](research_mixed_next_lower_left_bounded_prefix_four.md)
is independent of the next own flag and of \(h_z\).
It proves
\[
\max_{0\le q\le q_0}\{-\Re g(q+ih_y)+\Re g(q_0+ih_y)\}<1/125 .
\tag{16}
\]
Its proof maximizes at \(q_R=(2\pi)^{-1}\arccos(R/2)\)
and bounds the increase by the tangent to
\(\log(2\sin\pi q)\) at \(q=1/6\).
The fixed positive-height term in (7) is unchanged.
Equations (9),(16) give
\[
\mathcal A_{\rm last}(q)<\Lambda_{123}(z)-3/250 .
\tag{17}
\]

For an upper real row set \(v=1-t\), and suppose
\(q+1/5\le v\le1/2\). Increase \(q\) and \(v\) together,
holding \(v-q\) fixed, until \(q=q_0\) or \(v=1/2\).
The exact rate including the shared weight has multiplier
\[
\exp\frac{d}{dq}\{B_0+E_0(1-v;y,z)-\Re g(y)\}
=\frac{R(2\sin\pi v)^2}{D_q|1-Ze^{2\pi iv}|}.
\tag{18}
\]
This is the original first-last multiplier, with its constant
preceding factor replaced by \(B_0\).
The proof of
[the enlarged band, Section 5](research_mixed_next_own_three_upper_band_old_face.md)
makes (18) greater than one for \(q\le1/10\).

For \(q\ge1/10\), one has \(v\ge3/10\). Its correlated outgoing
inequality gives \((2\sin\pi v)^2/|1-Ze^{2\pi iv}|>2\).
Since \(R/(1+R^2-9R/25)\) increases on \(R\le1\),
\[
\frac{2R}{D_q}>
\frac{2(13/25)}{1+(13/25)^2-(9/25)(13/25)}
=\frac{650}{677}.
\tag{19}
\]
Thus the derivative along this part of the path is greater
than \(-27/650\). Its length is at most \(3/25\), so its
total possible loss is less than \(81/16250\).
The endpoint at \(q_0\) uses (9) and the original upper-row
endpoint theorem; the endpoint \(v=1/2\) uses (15).
Both have reserve \(1/50\). Therefore on this whole band,
\[
B_0+E_0(1-v;y,z)-\Re g(y)
<\Lambda_{123}(z)-122/8125 .
\tag{20}
\]
The endpoint \(v=q+1/5\) in (20) is a continuous rate value;
it is not an evaluation of a finite row at a noninteger index.

## 5. Complete finite assembly

The independent upper-rate assertion of
[the complete central deep-radius theorem](research_mixed_next_own_three_deep_radius_complete_central.md)
says that, at the targets (1), every remaining reflected index
\(0\le v<q+1/5\) has
\[
E_0(1-v;y,z)
\le\max\{L_0,E_0(4/5-q;y,z)\}.
\tag{21}
\]
It retains both height-dependent factors and numerator zeros.
This is a physical rate comparison before any first-factor
attachment. Equations (17),(20),(21) pay every upper physical
row by the same two bounds. The original zero-safe product
and endpoint-uniform factorial estimates then pay their
complete positive sum, including its last index.

For the lower half, use the literal positive low block through
\(\lfloor3N/20\rfloor\) and the canonical middle interpolation
from [the complete-current theorem](research_mixed_next_lower_left_complete_currents.md).
Its original half-grid cuts, two horizontal aliases, all four
weighted vertical halves and both unweighted joins reduce to
the main, real low and real half profiles in (14),(15).
That theorem permits either sign of the actual own-three
private height. Every multiplying factor here is independent
of that private index, so those same reductions apply.

The complete forced Fourier envelope, including \(q=0\), is
\[
|d_N(Y)|\le C_\tau N^{B_\tau}
                    e^{N\{-\Re g(y)+\tau\}}.
\tag{22}
\]
It is the bound in the lower-left low-physical theorem,
not a relative replacement of \(d_N\) by a reciprocal factorial.
The distinct canonical factorial continuation supplies the
middle-row interpolation at that seam.

The smallest of the profile reserves (14),(15),(17),(20) is
\(17/1800\). Choose the sum of all finite-product, interpolation
and preceding-factor tolerances below \(1/250\). The remaining
reserve exceeds
\[
\frac{17}{1800}-\frac1{250}=\frac{49}{9000}>\frac1{200}.
\tag{23}
\]
Polynomially many rows and the original factors of \(N\)
only change the polynomial prefactor. This proves (5) with
every finite index and both parities included.

## 6. Scope of the substitution

In (5), a bound for a positive preceding sum may be used as
the bound for \(V_N\). A bound for a coherent preceding sum
does not give a bound for each of its terms. Fixed-length
integration in additional parameters also preserves (5)
when (4) is uniform. Outside derivatives require their own
neighborhood hypotheses and are not inferred from (4) alone.

For example, the existing correction polynomial of disk rate
\(77/50\), the first far-real contribution of rate \(153/100\),
and the already bounded first low and upper groups with rate
at most \(B_0\) meet the hypothesis whenever their original
domains include (1). Their full next-type-three attachments
then satisfy (5) on \(R\le7/10\).
This does not bound the omitted first incoming main integrals
or any part for which (4) is unavailable.

The theorem has the full shared real interval but the stated
radial restriction. It gives neither a complete first-contour
assembly nor a lower bound for a signed Fourier coefficient.
The larger-radius source, the other shared-coordinate contours,
and arbitrary short compositions remain separate.
