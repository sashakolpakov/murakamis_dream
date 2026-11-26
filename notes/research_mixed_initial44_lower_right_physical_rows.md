# Initial four/four: the complete real-row errors beyond one half

Private written deduction, 10 November 2026. Every real ordinary row
already paid at the right half endpoint remains paid when the first
coordinate moves to real part \(7/10\), at its original negative
height. This includes the full low and high physical blocks and both
real cuts of the conditional middle integral. The regular cap profiles
and its true endpoint groups require different arguments. No estimate
for the remaining complex ordinary main integral is inferred here.

## 1. Literal source and calibration

Use the actual initial four/four reference, source and notation of
[the right-half theorem](research_mixed_initial44_right_half_interval.md):
\(m\ge3\), \(a_*=a_0+ic\), \(b=z+id\), with
\[
 .246<a_0<.350,\quad -.078<c<-.020,\quad
 z\in[11/50,9/20],\quad -.102\le d\le-.001 .
\]
Put \(a=x+ic\), \(1/2\le x\le7/10\), \(X=e^{-2\pi ia}\),
\(Y=e^{-2\pi ib}\), and \(r=|X|\). The original functions are
\[
 U_{1,N}(w,X)=\sum_{i=0}^{N-1}
 H_N(w,q_N^{-i})\frac{(q_NX;q_N)_i}{(q_N;q_N)_i^2},
\qquad
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
 \frac{X^{-j}(q_NX;q_N)_j(q_NY;q_N)_j}{(q_N;q_N)_j^3},
\tag{1}
\]
where \(q_N=e^{-2\pi i/N}\). Retain the full first weight
\(d_N(X)\) and outgoing modulus halfweight \(|d_N(Y)|^{1/2}\).
There is no selected first monomial.

Let \(E(t;a,b)\) be the complete physical-row rate (14) of the
right-half theorem. Write its original affine pair action as
\(\Lambda(z)\), put \(\kappa=1/2500000\), and set
\[
 \delta_R=\kappa(9/20-a_0)^2>0.
\]
That theorem, before finite summation, pays every high row
\(1/2\le t\le1\), the left cut \(t=1/8\), and all lower
rows by
\[
 \Lambda(z)-\kappa(z-b_0)^2-2\delta_R .
\tag{2}
\]
It also pays a fixed collar immediately below the half row, with
\(2\delta_R\) replaced by \(3\delta_R/2\).
These are original row/profile bounds, not bounds deduced from the
absolute value of a signed sum.

**Theorem 1.** Uniformly on this actual reference family, every regular
cap profile multiplied by any of those physical-row profiles retains
its bound (2), or the stated collar version, on \(1/2\le x\le7/10\).
The genuine true cap endpoint groups have the same bounds with an
additional reserve \(1/200\). Consequently the original low block
\(0\le j\le\lfloor2N/25\rfloor\), high block
\(\lceil N/2\rceil\le j\le N-1\), and real cuts tending to
\(2/25,1/2\), after multiplication by the complete cap and both
original weight allocations, have a common rate at most
\[
 \Lambda(z)-\kappa(z-b_0)^2-\delta_R+\tau
\tag{3}
\]
for every prescribed \(\tau>0\), with polynomial factors. The statement
holds at both parities and all real ordinary colors, and on sufficiently
small fixed ordinary-color disks with fixed derivatives and a separately
reserved arbitrarily small allowance.

## 2. Every regular cap profile contracts jointly with a real row

The complete cap contour uses private points
\[
 e=u+ih_e,\qquad .27\le u\le.49,\quad -.055\le h_e\le.04 .
\]
This includes the main, cuts, aliases and joining segments; their
cotangent penalties are independent of \(x\).
The [cap transport theorem](research_mixed_first_four_cap_lower_right_horizontal.md)
retains both exact numerator alternatives when \(a+e\) crosses its
period wall. On either alternative its bare cap derivative is
\(\log(N_e/D)\), where
\[
 D=|1-re^{-2\pi ix}|,\quad
 N_e=|1-rq e^{-2\pi i(x+u)}|,\quad q=e^{2\pi h_e}.
\]
The exact ordinary physical-row derivative is
\(\log(N_t/D)\), with
\(N_t=|1-re^{-2\pi i(x+t)}|\le1+r\).
On this lower horizontal \(\Re g(a)\ge0\), so the complete
first Fourier upper rate is zero. Therefore the joint derivative is
\[
                  \log(N_eN_t/D^2).
\tag{4}
\]
The outgoing halfweight is independent of \(x\).

The original height bounds imply
\[
             3/5<r<9/10,\qquad 7/10<q<13/10.
\tag{5}
\]
For example \(\log(5/3)>1/2>.156\pi\),
\(\log(10/7)>6/17>.11\pi\), and
\(\log(13/10)>6/23>.08\pi\), from the positive atanh
series and \(\pi<22/7\). The upper bound on \(r\) follows
from \(.04\pi>1/9>\log(10/9)\).

We prove \(N_e(1+r)<D^2\) in two overlapping closed ranges.
For \(1/2\le x\le13/20\),
\[
 -\cos2\pi x>7/12,\qquad \cos2\pi(x+u)>1/8,
\]
so
\[
 D^2>1+r^2+7r/6,\qquad
 N_e^2<1+169r^2/100-7r/40.
\]
The first cosine inequality follows from
\(\sin^2(\pi/5)=(5-\sqrt5)/8>49/144\).
For the second, the least cosine on \(x+u\in[.77,1.14]\)
is \(\sin(\pi/25)>1/8\). Indeed the standard rational
bounds \(157/50<\pi<22/7\) and \(\sin t>t-t^3/6\) give
\[
 \sin(\pi/25)>157/1250-1/2058>1/8.
\]
Subtracting the squared bounds and dividing by \(r\) gives
\[
\begin{split}
 &\frac{(1+r^2+7r/6)^2
 -(1+r)^2(1+169r^2/100-7r/40)}r\\
 &=\frac{61}{120}+\frac{919}{900}r
       -\frac{523}{600}r^2-\frac{69}{100}r^3\\
 &>\frac12+r-\frac9{10}r^2-\frac7{10}r^3>0.
\end{split}
\tag{6}
\]
The final polynomial is concave on \(r\ge0\); its values at
\(3/5,9/10\) are \(781/1250,1607/10000\).

For \(13/20\le x\le7/10\),
\[
 -\cos2\pi x>4/13,\qquad \cos2\pi(x+u)>9/25.
\]
Here \(\cos(2\pi/5)=(\sqrt5-1)/4>4/13\).
The least other cosine is \(\sin(3\pi/25)>9/25\):
use \(3\pi/25>3/8\), \(3\pi/25<2/5\), and
\(3/8-4/375>9/25\).
Convexity in \(q\in[7/10,13/10]\), followed by
\(r>3/5>9/25\), shows that the endpoint \(q=13/10\)
gives the larger upper bound. Thus
\[
 D^2>1+r^2+8r/13,\qquad
 N_e^2<1+169r^2/100-117r/125.
\]
The squared difference divided by \(r\) equals
\[
 \frac{271}{1625}
 +\left(\frac{591}{500}+\frac{64}{169}\right)r
 -\frac{3943}{3250}r^2-\frac{69}{100}r^3
 >
 \frac16+\frac{39}{25}r-\frac{61}{50}r^2-\frac{69}{100}r^3.
\tag{7}
\]
The polynomial on the right is concave, with endpoint values
\(19291/37500,23837/300000\), both positive.
Equations (6)--(7) prove that (4) is strictly negative for
every physical \(t\in[0,1]\). No stationary-row selection is used.

Integrating (4) from one half transports the complete calibrated
regular profiles. At a numerator wall the exact two-branch upper
rate is continuous and both one-sided derivatives are (4);
integrate that rate rather than differentiating a vanishing finite
symbol. The compact physical cap tails need an additional check,
given next; an old anchor-cut bound alone would not justify
multiplying them by a moving ordinary row.

## 3. The complete compact physical cap tails

For a real cap index \(e\in(0,1)\), its original coherent rate is
\[
 R_1(e,x)=\lambda(e)+
 \int_0^e\log|1-re^{-2\pi i(x+t)}|\,dt-J(e).
\tag{8a}
\]
The complete real-color coefficient bound and every finite compact
index are retained as in the cap transport theorem. The upper tail
\(e\ge.49\) is below the current row \(e=.49\), by that
theorem's strict inequality \(\partial_eR_1<0\). That row is
already covered by Section 2.

For \(2/25\le e\le.27\), put
\[
 \delta=\pi(x-1/2),\quad a=2\pi/25,\quad
 A=\sin^2\delta,\quad k=\frac{4r}{(1+r)^2}\ge\frac{15}{16}.
\]
The first numerator of the physical cap row has
\[
 N_e^2=(1+r)^2-4r\sin^2(\delta+\pi e),\qquad
 D^2=(1+r)^2-4rA.
\]
Here \(0\le\delta\le\pi/5\) and
\(\delta+\pi e\le47\pi/100<\pi/2\). Hence it suffices to prove
\[
 \sin^2(\delta+a)>2\sin^2\delta-\frac{15}{16}\sin^4\delta.
\tag{8b}
\]
Let \(t=\tan\delta<3/4\). The bounds
\(\tan a>a>1/4\) and \(\sin a<1/4\) give
\[
 \sin^2(\delta+a)>
 \frac{15(t+1/4)^2}{16(1+t^2)}.
\]
For completeness, \(a<44/175<1/3\), and the alternating
sine bound yields
\[
 \sin a<44/175-1/384+1/29160<1/4.
\]
The last comparison follows from
\(44/175-1/4=1/700\) and
\(1/700+1/29160<41/24000<1/384\).
Also \(\tan(\pi/5)<3/4\) follows from
\(\tan^2(\pi/5)=5-2\sqrt5<9/16\).

After clearing \(256(1+t^2)^2\), the sufficient difference
in (8b) is
\[
 P(t)=-32t^4+120t^3-257t^2+120t+15.
\]
It is strictly concave:
\[
 P''(t)=-384(t-15/16)^2-353/2<0,
 \qquad P(0)=15,\quad P(3/4)=15/16.
\]
Thus (8b) holds. Since \(k\ge15/16\), it implies
\(N_e(1+r)<D^2\). The exact joint derivative of (8a) and
any ordinary physical row is consequently negative on this entire
compact lower-cap interval as well.

For \(0<e\le2/25\), the original endpoint-profile inequalities
in [the complete cap envelope](research_mixed_boundary_window_real_color_envelopes.md)
give
\(\lambda'(e)>\lambda'(.27)>27/50\) and
\(J'(e)<J'(.27)<41/100\).
Since \(x+e\in[.5,.78]\), its cosine is less than \(1/5\);
\(r>3/5\) therefore gives \(N_e>1\). It follows that
\[
                 \partial_eR_1(e,x)>13/100.
\tag{8c}
\]
Every such compact lower row is below the current \(e=2/25\)
row, which has just been transported jointly. At \(x=1/2\)
all of these physical cap rows are bounded by the old lower
real-cut profile, with its original calibration. This completes the
compact cap inventory, without replacing a coherent endpoint
coefficient by the moduli of its Newton summands.

## 4. Separate true cap endpoint groups

The cap transport theorem proves a genuine common ceiling
\[
                             C=3/5
\tag{8}
\]
for its true endpoint groups on the new horizontal. It is independent
of \(x\). The joint endpoint/physical-row rate is consequently
\[
             C+E(t;a,b)-\tfrac12\Re g(b).
\tag{9}
\]
Its derivative is \(\log(N_t/D)\), which need not be negative.

To calibrate (9), first use the same constant \(C\) as a formal
comparison at \(x=9/20\); no actual cap endpoint estimate with this
constant is required there. The complete cap supporting-plane theorem
has bare plane \(B_T>149/200\). Hence \(B_T-C>29/200\).
The original ordinary physical-row support and the allocated cap
identity imply
\[
 C+E(t;a,b)-\Re g(a)-\tfrac12\Re g(b)
 <\Lambda(z)-\kappa(z-b_0)^2-2\delta_R-29/200
\tag{10}
\]
for the high rows and left cut. The low rows are bounded by that cut.
For the half collar, shrink its fixed width if necessary. Uniform
continuity, the strict uniform inequality \(B_T-C>29/200\),
and the original \(2\delta_R\) row reserve preserve the displayed
\(29/200\) surplus together with the smaller \(3\delta_R/2\)
row reserve. No stronger property of the previously chosen collar
is assumed.

On \(9/20\le x\le1/2\), this formal rate decreases, because
its derivative is \(\log(N_t/D^2)<0\), as in (18) of the
right-half theorem. The same conclusion applies first to the cut and
high rows, and then to the low rows through their increasing real-row
ratio. At \(x=1/2\) the first factorial rate vanishes, so (10)
calibrates (9) exactly.

On \(1/2\le x\le7/10\), \(D>1\) and \(N_t\le1+r<2\).
The possible increase in (9) is therefore less than
\[
             \frac15\log2<\frac7{50}.
\tag{11}
\]
For a written witness \(\log2<7/10\), sum the positive
atanh series at \(1/3\):
\(\log2\le2/3+2/81+1/540<7/10\).
The difference \(29/200-7/50=1/200\) proves the asserted
remaining endpoint reserve. This comparison uses formal rate
functions only; it neither divides by nor lower-bounds a finite
cap profile.

## 5. Finite blocks, zeros and scope

The original physical rows are covered through the true last index
\(N-1\). Their continuous rates include the limiting row \(t=1\).
The low rows up to \(2N/25\) are among those below \(1/8\);
the original low-row comparison supplies their calibration before
transport. Every term is estimated before summing its at most \(N\)
indices. At half-grid cuts tending to \(2/25\) and \(1/2\),
the zero-safe integrated profiles give an arbitrarily small uniform
rate debit. The parity displacement is \(O(N^{-1})\), not a deleted
endpoint. This proves (3).

The cap source bounds hold for all real ordinary colors. Its exact
degree is less than \(N\), so polynomial continuation supplies fixed
ordinary-color disks with arbitrary prescribed added allowance;
Cauchy estimates give fixed derivatives on smaller disks. The outgoing
halfweight is a constant multiplier in this continuation and is never
divided out, including at its zeros. Both Fourier alternatives of the
first weight were retained; their maximum on this interval is zero.
All original residue factors and measures remain unchanged.

This theorem pays the physical end blocks and real-cut endpoints of a
future conditional contour deformation. It does not pay its complex
main, horizontal aliases or unweighted connecting sides by itself.
Those require their own finite-source argument. It asserts no
selected-height, height-reset, whole-period or whole-word conclusion.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_initial44_right_half_interval.md | 309d6869f7438a9ed0a407c43666198ce1a039db7545c404a5e97f4ba2538c9c |
| research_mixed_first_four_cap_lower_right_horizontal.md | 4d41a967edabf0710fc7b04b723bb3e2fb7a407d44bb5a0fc1678e3f9ee5ee6e |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_cap_upper_target_completion.md | 49292f204a86e08c48c5aa8fd29f98103f38a939bb88d523afdd8be741650c22 |
| research_mixed_boundary_window_real_color_envelopes.md | 727aa6b7b477e3a984da4241d3ac9356858553e8aae74752bcf930a74abecd4b |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |

No mathematical numerical evaluation, saved-value arithmetic, import,
test, compilation or frozen-source edit was performed.

