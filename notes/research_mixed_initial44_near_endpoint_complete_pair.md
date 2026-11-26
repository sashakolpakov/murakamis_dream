# The complete initial44 pair on a real interval near the endpoint

Private written deduction, 10 November 2026. The middle physical
rows of the next-four kernel admit a strict comparison with the
already calibrated left-cut rate at the real half face. Together
with the complete positive cap bound and the low/high row
reductions, this pays the original full pair on
\([7/8,1-\rho]\), for each fixed \(0<\rho<1/8\).
The proof uses every physical row of the conditional polynomial;
no conditional contour or critical-point approximation is needed
on this interval.

The estimate does not cover the intervening real interval from
\(7/10\) to \(7/8\), the endpoint \(x=1\) in the Fourier
estimate, or later-coordinate departures from the plateau.

## 1. Literal source and available calibration

Fix the actual initial44 family and reference in
[the far-right physical-envelope theorem](research_mixed_initial44_far_right_physical_envelope.md).
Thus the positive three/four word has length \(m\ge3\), begins
with four and four, and retains
\[
 a_*=a_0+ic,\quad b_*=b_0+id,\qquad
 .246<a_0<.350,\quad -.078<c<-.020,\quad
 -.102\le d\le-.001.
 \tag{1}
\]
Write \(\kappa=1/2500000\),
\(\delta_R=\kappa(9/20-a_0)^2\), and retain its original affine
pair action \(\Lambda(z)\). The targets of the present estimate are
\[
 a=x,\quad \frac78\le x\le1-\rho,\qquad
 b=z+id,\quad z\in P=[11/50,9/20].
 \tag{2}
\]
Let \(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\),
\(p_j(X)=(q_NX;q_N)_j\), \(X=e^{-2\pi ix}\),
and \(Y=e^{-2\pi ib}\). In particular \(|Y|\le1\).
The exact pair consists of
\[
 \begin{split}
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}
             H_N(w,q_N^{-i})\,\frac{p_i(X)}{P_i^2},\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}R_{j,N}(X,Y),\qquad
 R_{j,N}(X,Y)=\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
 \end{split}
 \tag{3}
\]
Its first weight is the whole \(d_N(X)X^{-N\epsilon}\),
\(\epsilon=0,1\); its outgoing allocation is
\(|d_N(Y)|^{1/2}\). All these factors remain literal.

Use the original real primitive \(J(0)=J(1/2)=J(1)=0\),
\(J'(t)=\log|2\sin\pi t|\), with its continuous odd periodic
extension. Define
\[
 \begin{split}
 I_x(t)&=\int_0^t\log|1-e^{-2\pi i(x+v)}|\,dv,\\
 I_b(t)&=\int_0^t\log|1-Ye^{-2\pi iv}|\,dv,\\
 E_x(t)&=I_x(t)+I_b(t)-3J(t),\qquad 0\le t\le1.
 \end{split}
 \tag{4}
\]
This is exactly the physical-row rate, including the incoming
chirp, whose modulus is one on (2). In the notation of the
cited theorem, \(I_b(t)=G_{-d}(z+t)-G_{-d}(z)\).
No primitive constant has changed.

Put \(\ell=2/25\). Equations (18), (20), (29)--(30) of that
theorem give, respectively, the whole-cap ceiling \(223/240\),
the row comparisons
\[
 \begin{split}
 E_x(t)&\le E_{1/2}(t),&&0\le t\le\ell,\\
 E_x(t)&\le E_{1/2}(1/2),&&1/2\le t\le1,
 \end{split}
 \tag{5}
\]
and an original bare cap plane \(B_0\) satisfying
\[
 \begin{split}
 B_0+E_{1/2}(t)-\tfrac12\Re g(b)
 &\le \Lambda(z)-\kappa(z-b_0)^2-2\delta_R,
       &&t\in[0,\ell]\cup[1/2,1],\\
 B_0-\frac{223}{240}&>\frac1{400}.
 \end{split}
 \tag{6}
\]
These are continuous-rate comparisons with the original affine
action, not comparisons to a possibly zero finite half-row.

## 2. Every middle row is below the calibrated left-cut rate

**Lemma 1.** For every \(b\) in (2), every
\(\ell\le t\le1/2\), and \(7/8\le x\le1\),
\[
                    E_x(t)<E_{1/2}(\ell)-\frac{59}{47000}.
 \tag{7}
\]
The endpoint \(x=1\) is used here only in a continuous-rate
identity.

*Proof.* At \(x=1\), \(I_1(t)=J(t)\). Since \(|Y|\le1\),
\[
 E_1(t)=I_b(t)-2J(t)
       \le I_b(\ell)+(t-\ell)\log2-2J(t).
 \tag{8}
\]
The derivative of \(t\log2-2J(t)\) is
\(\log2-2\log(2\sin\pi t)\). It is positive before
\(t=1/4\) and negative after that point on \((0,1/2)\).
The interval \([\ell,1/2]\) contains \(1/4\).
With the original normalization \(b_2=-4J(1/4)\), subtracting
the exact \(E_{1/2}(\ell)\) therefore gives
\[
 E_1(t)-E_{1/2}(\ell)
 \le \frac{17}{100}\log2+\frac{b_2}{2}
                    +3J(\ell)-I_{1/2}(\ell).
 \tag{9}
\]
The outgoing factor \(I_b(\ell)\) has cancelled exactly;
it was not replaced by an independent outgoing action.

Here are sufficient written bounds for all terms in (9).
The [complete-column proof](research_mixed_symmetric_closing_complete_column_norm.md),
Sections 1 and 5, retains \(b_2=-4J(1/4)<7/12\).
Also \(\log2<7/10\), with the positive-series witness
\[
       \log2\le 2/3+2/81+1/540<7/10.
 \tag{10}
\]
The sine upper bound and \(\pi<10/3\) yield
\[
 J(\ell)\le\ell\{\log(2\pi\ell)-1\}<-\frac{16}{125}.
 \tag{11}
\]
Indeed \(2\pi\ell<8/15\), while
\(\log(15/8)>2(15/8-1)/(15/8+1)=14/23>3/5\).
The strict logarithm bound follows directly by integrating
\(2/(1-v^2)>2\) in the standard positive
\(\operatorname{atanh}\) formula.
For \(0\le v\le\ell\), one has \(\pi v<3/10\), so
\(\cos(\pi v)>3/4\). Consequently
\[
 I_{1/2}(\ell)
  =\int_0^\ell\log(2\cos\pi v)\,dv
  >\ell\log(3/2)>\frac4{125},
 \tag{12}
\]
using \(\log(3/2)>2/5\) from the same formula.
Substituting (10)--(12) into (9) gives the exact rational comparison
\[
 E_1(t)-E_{1/2}(\ell)
 <\frac{119}{1000}+\frac7{24}-\frac{52}{125}
                         =-\frac2{375}.
 \tag{13}
\]

Now let \(u=1-x\in[0,1/8]\). Oddness and periodicity give
\[
 I_x(t)=J(t-u)+J(u).
 \tag{14}
\]
If \(t\ge u\), the exact sine-binomial entropy inequality,
equation (13) of the far-right theorem, gives
\[
       J(u)+J(t-u)\le J(t),\qquad E_x(t)\le E_1(t).
 \tag{15}
\]
Thus (13) already pays this whole part of the middle interval.
For a direct proof of the entropy inequality in the present
range \(u\le t\le1/2\), integrate the increasing derivative
\(J'\) on \((0,1/2)\) to obtain
\(J(t)-J(t-u)\ge J(u)-J(0)\).

It remains to consider \(\ell\le t\le u\le1/8\).
In this case, before the incoming numerator wall,
\[
 I_x(\ell)=\int_{u-\ell}^{u}\log(2\sin\pi v)\,dv
       \le \ell\log\bigl(2\sin\pi(u-\ell/2)\bigr)
       < -\frac{52}{1175}.
 \tag{16}
\]
The middle inequality is Jensen's inequality for the strictly
concave logarithm of the sine, including its integrable endpoint.
Here \(u-\ell/2\le17/200\), so
\(2\sin\pi(u-\ell/2)<17\pi/100<17/30\).
Finally \(\log(30/17)>26/47\), again by the positive
\(\operatorname{atanh}\) formula, proves the last bound.

For \(\ell<t<u\), differentiate the original rate (4).
Since \(2\sin\pi t\ge6t\) for \(t\le1/8<1/6\),
\[
 \begin{split}
 E_x'(t)
 &\le \log2+\log\bigl(2\sin\pi(u-t)\bigr)
                         -3\log(2\sin\pi t)\\
 &\le \log\frac{4\pi(u-t)}{216t^3}
 \le \log\frac{625\pi}{384}<\frac53.
 \end{split}
 \tag{17}
\]
The last bound has entirely rational witnesses:
\[
 \frac{625\pi}{384}<\frac{6875}{1344}<\frac{41}{8},
 \qquad
 e^{5/3}>
  1+\frac53+\frac{25}{18}+\frac{125}{162}+\frac{625}{1944}
   =\frac{10009}{1944}>\frac{41}{8}.
 \tag{18}
\]
The first line of (17) uses \(u-t\le1/8-2/25=9/200\) and
\(t\ge2/25\). Integrating (17) up to \(u\) is legitimate
through the integrable logarithmic endpoint.
Equations (12), (16)--(18) therefore give
\[
 E_x(t)-E_{1/2}(\ell)
 < -\frac{52}{1175}-\frac4{125}
          +\frac53\left(\frac18-\frac2{25}\right)
 =-\frac{52}{1175}-\frac4{125}+\frac3{40}
 =-\frac{59}{47000}.
 \tag{19}
\]
Since \(2/375>59/47000\), this and (13)--(15) prove (7)
on the entire middle interval. All estimates were uniform in
the retained outgoing parameter \(b\). \(\square\)

## 3. The original full finite pair

**Theorem 2.** For every fixed \(0<\rho<1/8\), every
\(\tau>0\), both level parities, \(\epsilon=0,1\), and
all ordinary real incoming colors \(w\in[-2,2]\),
\[
 \begin{split}
 &|U_{1,N}(w,X)d_N(X)X^{-N\epsilon}|\,
       |d_N(Y)|^{1/2}
       \sum_{j=0}^{N-1}|R_{j,N}(X,Y)|\\
 &\qquad\le C_{\rho,\tau}N^{A_{\rho,\tau}}
 \exp N\{\Lambda(z)-\kappa(z-b_0)^2
                         -2\delta_R-1/400+\tau\}.
 \end{split}
 \tag{20}
\]
In particular the same bound holds with the complete
\(|C_{1,N}(X,Y)|\) in place of the sum in (20).
It also holds on sufficiently small fixed ordinary-color disks,
and for every fixed derivative in that ordinary color on smaller
disks, with its fixed derivative constant absorbed in \(C\).
The targets are exactly (2).

*Proof.* The low indices have \(j/N\le\ell\) and satisfy the
first line of (5). The high indices have \(j/N\ge1/2\) and
satisfy its second line. Every remaining index satisfies Lemma 1.
Apply (6), using \(t=\ell\) for the middle block. Thus every
original physical row is paid by the same original conditional
calibration, and the middle block has the additional \(59/47000\)
rate surplus.

For clarity, this covers all integers \(0\le j<N\):
the low block ends at \(\lfloor2N/25\rfloor\), the high block
starts at \(\lceil N/2\rceil\), and the remaining integers
are precisely the middle block. No exact half-integer row is
required at odd level.
The zero-safe finite-product proof in Section 3 of
[the all-angle row theorem](research_mixed_all_angle_high_row_sign_class.md)
bounds each such row by \(E_x(j/N)\), with a uniform arbitrary
rate allowance and a polynomial factor. Its argument regularizes
the numerator logarithms before taking upper Riemann sums and
uses the uniform sine-factorial endpoint error for \(j<N\).
It depends on neither the critical sheet nor an angular sign
restriction. Applied to (2), it remains uniform when a numerator
vanishes; it retains the true first and last rows.

Multiply these row bounds by the full positive cap ceiling in
equation (18) of the far-right theorem and use the second line
of (6). Sum at most \(N\) rows. The complete
[Fourier bound](research_mixed_fourier_weight_continuation.md),
Section 5, has rate \(\max\{-J(x),0\}=0\) on the fixed
compact interval (2), since \(J(x)\ge0\) there.
The selected monomial has modulus one.
The original outgoing halfweight has rate
\(-\Re g(b)/2\), already retained in (6).
Divide one total tolerance among these estimates to obtain (20).
No source factor or halfweight is divided out.

The triangle inequality for the exact sum (3) proves the claim
for \(C_{1,N}\). In particular there is no omitted conditional
main integral, alias, side, or endpoint correction to bound:
all of them, if one chose to introduce a contour representation,
represent the same already bounded full finite sum.
This is only an upper estimate; no noncancellation is inferred.

The exact cap degree in \(w\) is less than \(N\), while every
other factor is independent of \(w\). Apply the original
[polynomial continuation](research_mixed_horizontal_complex_extension.md)
to the bound on the full real-color interval, retaining those
factors as constant multipliers. If a multiplier vanishes the
bound is immediate; it is never divided out.
The fixed complex-color extension costs any prescribed small
rate tolerance, and Cauchy's formula gives the stated fixed
derivatives. This proves the final assertions. \(\square\)

For any subinterval of (2), multiplication by the original
outer density \(N\,dx\) and integration costs only a polynomial
factor. Thus (20) pays this actual outer real-path piece in
either first Fourier alternative, without changing its
normalization. It does not assert a full-period integral
asymptotic or alter the original scalar of the surrounding word.

All choices, including \(\rho\) and the ordinary-color disks,
are fixed before \(N\to\infty\). The continuous identity at
\(x=1\) in Lemma 1 does not assert a Fourier estimate uniform
as \(\rho\downarrow0\). The previously established periodic
endpoint collar is a separate source theorem.
The real interval from \(7/10\) to \(7/8\) and
later-coordinate sectors remain outside this deduction.

## Direct source versions

| Direct source | SHA-256 |
|---|---|
| research_mixed_initial44_far_right_physical_envelope.md | a676bfee21df1e78965bb6515a37e0aebd669b6fb4e4cecb2976a8c254cf778d |
| research_mixed_symmetric_closing_complete_column_norm.md | 4df2375a3ae9340b0137effb2d8193eed4a3ed090a0c1bde58fb9c434f3fe519 |
| research_mixed_all_angle_high_row_sign_class.md | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |

The full written proof and all directly used source implications
were read, and all five source hashes were checked. No mathematical
numerical evaluation, saved-value arithmetic, import, compilation,
test, source replay or frozen-note edit was used. Independent
review is required before adoption.
