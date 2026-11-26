# The complete central own-three source at deeper shared heights

Private research proof, 8 November 2026. For shared radius
\(|Y|\le7/10\), the remaining positive own-three upper rows
reduce to their actual last rate or to the continuous boundary
of the already bounded band. This reduction is independent of
the preceding factor. With the established first-factor profile
bounds it pays the complete central source on the whole lower-left
shared interval.

The proof uses explicit new inequalities for convergent radial
and alternating series. These are written symbolic bounds, not
numerical evaluations of a primitive or a replay of a saved
record. Earlier notes and public manuscripts are unchanged.

## 1. Actual source and a factor-independent rate reduction

Keep the original ordinary-next own-three references of
[the enlarged-band theorem](research_mixed_next_own_three_upper_band_old_face.md).
In particular
\[
\begin{gathered}
a=x+ih_a,\quad y=q+ih_y,\quad z=u+ih_z,\qquad
x,u\in P=[11/50,9/20],\quad 0\le q\le11/50,\\
-.072<h_a<0,\quad -.102<h_s,h_y<-.001,\quad
-.065<h_z<.068,\\
X=e^{-2\pi ia},\quad Y=Re^{-2\pi iq},\quad
Z=\rho e^{-2\pi iu},\qquad
13/25<R\le7/10,\quad 13/20<\rho<43/28 .
\end{gathered}                                                   \tag{1}
\]
All actual reference correlations and the original following
plane \(\Lambda_{123}(z)\) remain fixed. The lower outgoing
radius is the original own-three height witness in
[the inward-seam branch theorem, Section 2](research_mixed_next_own_three_inward_seam_branches.md);
the sharper upper radius is retained in the enlarged band.

Write
\[
T=R^{-1},\qquad L_0=-\log R+\log_+\rho,\qquad b=q+1/5 .
\tag{2}
\]
The original physical rate is
\[
E_0(t;y,z)=
\int_0^t\log|1-Ye^{-2\pi is}|\,ds+
\int_0^t\log|1-Ze^{-2\pi is}|\,ds
-2J(t)-2\pi h_y t .
\tag{3}
\]
In particular \(E_0(1;y,z)=L_0\), with the positive
outgoing-height carrier included.

**Rate theorem.** On (1), every reflected index \(0\le v<b\)
satisfies
\[
\boxed{\quad
E_0(1-v;y,z)\le
\max\{L_0,E_0(4/5-q;y,z)\}.
\quad}                                                         \tag{4}
\]
Consequently
\[
\max_{1/2\le t\le1}E_0(t;y,z)
=\max\left\{L_0,\quad
       \max_{1/2\le t\le4/5-q}E_0(t;y,z)\right\}.
\tag{5}
\]
This is a comparison of the literal row rates. It neither
extracts a summand from a bounded coherent sum nor divides
by a terminal coefficient.

## 2. A centered envelope through reflected index \(3/10\)

The exact reflection, retaining both carriers, is
\[
\begin{split}
\Phi(v)&:=E_0(1-v;y,z)-L_0\\
 &=2J(v)-\int_{q-v}^{q}\log|T-e^{2\pi is}|\,ds
             -\int_{u-v}^{u}\log|1-\rho e^{2\pi is}|\,ds .
\end{split}                                                     \tag{6}
\]
Suppose \(0\le v\le3/10\) and \(u\ge v\). The incoming
arc lies inside \([-3/10,11/50]\). Its even integrand
increases with distance from zero on this interval and
with \(T\ge1\). Centering the arc at zero, and then using
\(T\ge10/7\), gives
\[
\int_{q-v}^{q}\log|T-e^{2\pi is}|\,ds
\ge\int_0^v\log|10/7-e^{\pi is}|\,ds .
\tag{7}
\]
The outgoing arc lies in \([0,1/2]\). The original radial
primitive bound and translation of that arc to start at zero
give
\[
\int_{u-v}^{u}\log|1-\rho e^{2\pi is}|\,ds\ge J(v).
\tag{8}
\]
For \(\rho>1\), first take out \(v\log\rho\) and use
the reciprocal radius, which only improves this lower bound.
These are the same exact arc arguments as Sections 2--3 of
[the deeper upper-end theorem](research_mixed_next_own_three_deep_radius_upper_end.md),
now used only where the displayed condition \(u\ge v\) holds.

Define
\[
H(v)=J(v)-\int_0^v\log|10/7-e^{\pi is}|\,ds.
\tag{9}
\]
Then \(\Phi(v)\le H(v)\). Put \(T_0=10/7\) and
\(c=\cos\pi v\). The sign of \(H'(v)\) is the sign of
\[
3-T_0^2+2T_0c-4c^2.
\tag{10}
\]
On \(0\le v\le3/10\), \(c\ge\cos(3\pi/10)>1/2\).
The derivative of (10) in \(c\) is therefore negative.
Since \(c\) decreases with \(v\), (10) increases with
\(v\), starting at \(-(T_0-1)^2<0\).
Thus \(H'\) can change sign only from negative to positive.
The maximum of \(H\) is at zero or at \(3/10\).

We now prove the strict endpoint bound
\[
                         H(3/10)<-\frac3{10625}.
\tag{11}
\]
Every new series bound needed for this assertion is explicit
in the next section. Since \(H(0)=0\), (10)--(11) imply
\[
E_0(1-v;y,z)\le L_0
\qquad(0\le v\le3/10,\quad u\ge v).
\tag{12}
\]

## 3. Exact radial and sine-integral witnesses

For \(0<r<1\), let
\[
G_r(x)=\int_0^x\log|1-r e^{2\pi is}|\,ds
=-\frac1{2\pi}\sum_{n=1}^{\infty}
                   \frac{r^n\sin(2\pi nx)}{n^2}.
\tag{13}
\]
The equality follows by integrating the uniformly convergent
logarithmic power series. The original primitive constant is
zero at \(x=0\). Thus (9), with \(r=7/10\), becomes
\[
H(v)=J(v)-v\log(10/7)-2G_{7/10}(v/2).
\tag{14}
\]
No relative finite-factorial approximation is used here.

At \(v=3/10\), put
\[
\mathcal S=\sum_{n=1}^{\infty}
               \frac{(7/10)^n\sin(3n\pi/10)}{n^2}.
\]
The first three terms satisfy
\[
\begin{split}
(7/10)\sin(3\pi/10)&<567/1000,\\
(7/10)^2\sin(3\pi/5)/4&<147/1250,\\
(7/10)^3\sin(9\pi/10)/9&<13/1000.
\end{split}                                                     \tag{15}
\]
For the first, use
\(\sin(3\pi/10)=(1+\sqrt5)/4<81/100\), since
\(\sqrt5<56/25\). For the second,
\[
\sin(3\pi/5)=\cos(\pi/10)
 <1-\frac{25}{512}+\frac1{1944}<\frac{24}{25},
\]
using \(5/16<\pi/10<1/3\) and the quartic cosine upper
bound. For the third, \(\sin(\pi/10)<11/35<1/3\);
the resulting \(343/27000\) is less than \(13/1000\).

Terms four through six of \(\mathcal S\) are negative.
The absolute tail from term seven satisfies
\[
\sum_{n\ge7}\frac{(7/10)^n}{n^2}
\le\frac{(7/10)^7}{49(1-7/10)}
<\frac1{147}<\frac7{1000}.
\tag{16}
\]
Indeed \((7/10)^4<1/4\) and \((7/10)^3<2/5\).
Dropping the three negative terms and using (15)--(16) gives
\[
\mathcal S<\frac{3523}{5000}<\frac{141}{200},
\qquad
-2G_{7/10}(3/20)=\frac{\mathcal S}{\pi}<\frac{141}{625},
\tag{17}
\]
where \(\pi>25/8\).

For the original real sine integral, its same Fourier
normalization gives
\[
-J(1/4)=\frac{G}{2\pi},\qquad
G=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)^2}.
\tag{18}
\]
This is the Catalan normalization already used in
[the half-interval source, equation (21)](research_repeated_two_block_half_interval_packet.md).
Retaining six alternating terms yields the following sharper
written lower witness:
\[
\begin{split}
G&>1-\frac19+\frac1{25}-\frac1{49}
                  +\frac1{81}-\frac1{121}\\
 &=\frac89+\frac{24}{1225}+\frac{40}{9801}
 >\frac89+\frac{23}{1000}
 =\frac{8207}{9000}>\frac{319}{350}.
\end{split}                                                     \tag{19}
\]
The last cross-product difference is \(1450>0\).
Using \(\pi<22/7\), (18)--(19) give
\[
                              -J(1/4)>29/200.
\tag{20}
\]
On \([1/4,3/10]\), \(J'\) increases to
\(\log(2\sin(3\pi/10))<1/2\).
For this strict logarithmic bound, use \(\sqrt5<9/4\),
so \(2\sin(3\pi/10)<13/8\), and
\[
e^{1/2}>1+\frac12+\frac18+\frac1{48}
          =\frac{79}{48}>\frac{13}{8}.
\]
Consequently
\[
-J(3/10)>29/200-1/40=3/25.
\tag{21}
\]
Finally the elementary bound
\(\log(10/7)>2((10/7)-1)/((10/7)+1)=6/17\)
gives \((3/10)\log(10/7)>9/85\).
Substitution in (14),(17),(21) proves
\[
H(3/10)<-\frac3{25}-\frac9{85}+\frac{141}{625}
                         =-\frac3{10625},
\]
as claimed. This completes the centered-envelope argument.

## 4. Increasing rows when the reflected index passes the output

It remains to handle \(u<v\le3/10\) within \(v<b=q+1/5\).
In this region
\[
11/50\le u<v\le3/10,\qquad 0<v-u\le2/25.
\tag{22}
\]
The exact derivative, including the folded incoming carrier, is
\[
\frac d{dv}E_0(1-v;y,z)
=\log\frac{\{2\sin(\pi v)\}^2}
 {|T-e^{2\pi i(v-q)}|\,|1-Ze^{2\pi iv}|}.
\tag{23}
\]
There is no outgoing zero removal; any such zero gives its
integrable positive logarithmic singularity.

We first record the elementary angular bound
\[
                         \cos(4\pi/25)>7/8.
\tag{24}
\]
For an explicit witness set \(\theta=4\pi/25\). Then
\(1/2<\theta<101/200<51/100\), and
\(\theta^6<(27/100)^3<1/50\).
The degree-six cosine lower bound gives
\[
\cos\theta>
1-\frac{10201}{80000}+\frac1{384}-\frac1{36000}
=\frac78+\frac{23}{360000}.
\]
By (22),(24), the outgoing squared modulus is at most the
larger endpoint value of the convex quadratic
\(1+\rho^2-7\rho/4\) on \([13/20,43/28]\). Hence
\[
|1-Ze^{2\pi iv}|^2
<\max\{57/200,263/392\}<7/10.
\tag{25}
\]
The incoming factor has the bound from
[fixed-shared transport, equation (9)](research_mixed_next_own_three_upper_band_fixed_shared.md):
\[
|T-e^{2\pi i(v-q)}|^2<599/169,
\tag{26}
\]
since \(0<v-q<1/5\) and \(T<25/13\).
Also \(v\ge11/50\) and \(v\le3/10\), so
\[
\{2\sin(\pi v)\}^2=2-2\cos(2\pi v)>8/5,
\tag{27}
\]
using \(\cos(11\pi/25)=\sin(3\pi/50)<1/5\).
Therefore the square of the multiplier in (23) exceeds
\[
\frac{64/25}{(599/169)(7/10)}
                   =\frac{21632}{20965}>1.
\]
In fact the same elementary logarithmic inequality as before gives
\[
\frac d{dv}E_0(1-v;y,z)
>\frac{667}{43264}>\frac1{100}.
\tag{28}
\]

Increase \(v\), keeping \(q,u\) and all heights fixed.
The condition \(u<v\) persists. If the path reaches
\(v=b\) before \(3/10\), (28) pays the whole path.
Otherwise continue from \(3/10\) to \(b\) using the
already proved derivative \(>1/20\) in fixed-shared transport.
It follows in either case that
\[
E_0(1-v;y,z)\le E_0(4/5-q;y,z)
       \qquad(u<v\le3/10,\quad v<b).
\tag{29}
\]
Rows with \(v\ge3/10\) and \(v<b\) satisfy the same
inequality directly by that theorem.

Combining (12),(29) proves (4). Every row on the right
side of (5) belongs to the full upper interval, and its
remaining rows satisfy (4), proving the equality (5).

## 5. Zero-safe finite form, before any first factor is attached

Let \(r=e^{-2\pi i/N}\), \(D=N-1\),
\(P_j=(r;r)_j\), and \(p_j(W)=(rW;r)_j\). Put
\[
J_b=\lfloor N(4/5-q)\rfloor,\qquad
\mathcal U_{0,N}^{>b}
=\sum_{J_b<j\le D}
       \left|\frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2}\right|.
\tag{30}
\]
For every fixed prescribed \(\tau>0\), (4) and the
original uniform product and sine-factorial estimates give
\[
\boxed{\quad
\mathcal U_{0,N}^{>b}
\le C_\tau N^{B_\tau}
 \exp N\{\max(L_0,E_0(4/5-q;y,z))+\tau\}.
\quad}                                                         \tag{31}
\]
The endpoint is the exact continuous physical rate, not a
finite sample at a nonexistent nonintegral row. Each actual
index \(j>J_b\) has \(v=1-j/N<b\), as required.
The zero-safe estimates keep all numerator zeros; their
endpoint-uniform \(O(\log N)\) costs include \(j=D\).
Both parities and arbitrary subsets of (30) are retained.

Equation (31) is independent of a preceding factor.
It may be multiplied by any such factor, but still requires
that factor's own comparison with the two displayed rates.
It does not use a lower bound for the finite band or for
the terminal row.

## 6. The complete central finite source

The proof of
[the enlarged band, equations (24),(30)](research_mixed_next_own_three_upper_band_old_face.md)
pays, source by source, every first main, real-low,
real-half and last profile at the continuous boundary
\(v=q+1/5\). Its rate deficit exceeds \(10^{-10}\).
The cap plane and the entire shared weight are retained.
This applies to the second alternative in (31).

For its first alternative, Sections 3--4 of
[the upper-end theorem](research_mixed_next_own_three_upper_end_last_reduction.md)
pay every same first profile with \(L_0\) attached on
\(R\le7/10\). Its actual own-three last certificate is
used only for its sign; the first conditional quadratic
and real-cut reserves supply the explicit deficit.
The first last alternative has the stronger all-typed
double-last bound.

Use these profile bounds before the exact first-source
assembly. The first low physical rows increase to their
real cut, the complete middle interpolation retains both
horizontal aliases, all four weighted sides and both
unweighted joins, and the positive first upper rows retain
their half and last alternatives. Multiplication by an
index-independent next physical row changes none of those
comparisons. Applying (31), and choosing the finite
tolerances within the profile reserves, therefore pays
the positive next tail (30) with the complete first factor.
The previously bounded positive band supplies all other
next upper rows.

Finally
[the complete-first below-half theorem](research_mixed_next_own_three_below_half_complete_first.md)
supplies the entire signed next lower block, including its
own physical ends and canonical currents. The three next
index ranges partition \(0\le j<N\) exactly at either
parity. Thus
\[
\boxed{\quad
|U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)C_{0,N}(Y,Z)|
\le CN^B e^{N\{\Lambda_{123}(z)-10^{-11}\}}
\quad}                                                         \tag{32}
\]
on all of (1), for all real ordinary colors and all
sufficiently large integer levels. Here \(C_{0,N}(Y,Z)\)
is the literal sum of \(Y^{-j}p_j(Y)p_j(Z)/P_j^2\)
over every \(0\le j<N\).
The upper physical part alone satisfies the corresponding
positive-sum bound, with arbitrary subsets permitted there.
No arbitrary-subset assertion is made for the signed
next middle block.

The actual first central incoming integral keeps \(+N\,da\)
and the same exponential gap. At the actual output, fixed-base
signed sums and integrals have normalized local mixed jets
with gap \(10^{-12}\), by the all-real color and logarithmic-arc
polynomial continuation used in the input theorems, followed
by Cauchy's formula. The original full forced \(d_N\) estimate
and the distinct canonical factorial continuation remain
valid through \(q=0\). No outgoing halfweight exists for
own type three. Base paths, reference labels and any partial
index sets are fixed before outside differentiation.

The theorem covers the central first incoming interval
\(x\in P\), the whole \(q\in[0,11/50]\), and only
the deeper shared-radius range \(R\le7/10\).
It does not supply the other first incoming paths,
shallower shared heights, the old-filter correction or
the remaining Fourier contour bounds. A complete next
transfer and arbitrary short compositions remain open.
