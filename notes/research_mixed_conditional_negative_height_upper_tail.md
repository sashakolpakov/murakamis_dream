# A complete physical upper tail at negative incoming height

Research deduction, 7 November 2026. Every original conditional row
with index at least \(27N/50\) is exponentially below the actual
conditional critical action on the full displaced incoming rectangle.
The estimate retains the incoming chirp and both numerator products.
It is an absolute bound for this complete finite row group, not an
asymptotic for the remaining conditional sum.

No numerical evaluation, source replay, or frozen-note edit is used.
The rows between the incoming wall and \(27N/50\), and the real upper
cut needed to close a retained contour, remain separate.

## 1. Exact source, action and physical rate

Use
\[
 \begin{gathered}
 r=e^{-2\pi i/N},\qquad P_j=(r;r)_j,\qquad
 p_j(X)=(rX;r)_j,\qquad D=N-1,\\
 C_{1,N}(X,Y)=\sum_{j=0}^{D}
                   X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 a=x+ih,\quad \frac12\le x\le\frac7{10},\quad
                  -\frac9{125}\le h\le0,\\
 y=z+iH,\quad \frac{11}{50}\le z\le\frac9{20},\quad
                         0\le H\le\frac1{100},\\
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad
 \rho=e^{2\pi h}\le1,\quad R=e^{2\pi H}\ge1,\quad
                         \delta=-2\pi h.
 \end{gathered}                                                    \tag{1}
\]
The original critical point and zero logarithmic lift are those of
[the negative-height branch theorem](research_mixed_conditional_negative_height_branch.md).
Write
\[
 \Theta(a,y)=Q(t(a,y);a,y),\quad
 Q(t;a,y)=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat .
 \tag{2}
\]
The [height-action theorem](research_mixed_conditional_height_action_monotonicity.md)
proves on precisely (1)
\[
                         \Re\Theta(a,y)>\frac{13}{24}.          \tag{3}
\]
In particular the additive constant in (2) is fixed by the original
source; it is not chosen for the comparison below.

Let \(J(u)=\int_0^u\log(2|\sin\pi s|)\,ds\) on the real line,
with its continuous periodic extension. The zero-safe real-row
rate of the literal \(j\)-th summand, at \(t=j/N\), is
\[
 \begin{split}
 \mathcal R(t;a,y)
   &=I_{x,\rho}(t)+I_{z,R}(t)-3J(t)+\delta t,\\
 I_{x,\rho}(t)&=\int_0^t
                      \log|1-\rho e^{-2\pi i(x+s)}|\,ds .
 \end{split}                                                     \tag{4}
\]
The same notation defines the second numerator integral.
The last term is the exact modulus of \(X^{-j}\).

For every prescribed \(\tau>0\), the uniform product bounds give
\[
 \left|X^{-j}p_j(X)p_j(Y)/P_j^3\right|
       \le C_\tau N^{B_\tau}
                      e^{N\{\mathcal R(j/N;a,y)+\tau\}},
                         \qquad 0\le j<N.                    \tag{5}
\]
These are the complete finite-product bounds used in
[the joint source continuation](research_mixed_half_face_joint_source_packet.md)
and [the moving-cut source proof](research_mixed_next_incoming_staircase_transport.md).
The upper comparison is valid through every numerator zero;
denominator estimates retain the uniform endpoint \(O(\log N)\)
error. No physical-grid termination is imposed at a nonphysical
incoming argument.

## 2. An incoming complementary arc is nonnegative

For \(0<\rho\le1\), put
\[
 f_\rho(s)=\log|1-\rho e^{-2\pi is}|,\qquad
 A_\rho(x,v)=\int_{x-v}^{x}f_\rho(s)\,ds .
 \tag{6}
\]
The logarithmic zeros at \(\rho=1\) are integrable.

**Lemma 1.** If \(1/2\le x\le7/10\) and \(0\le v\le1/2\), then
\[
                              A_\rho(x,v)\ge0.                \tag{7}
\]

*Proof.* The function \(f_\rho\) is symmetric about \(1/2\), increases
on \([0,1/2]\), and decreases on \([1/2,1]\). Its period integral
is zero, as follows from the elementary logarithmic mean for
\(0<\rho<1\) and its integrable limit at \(\rho=1\).
Consequently its half-period integral is zero.

For \(v\le1/5\), the whole interval \([x-v,x]\) lies in
\([3/10,7/10]\). The doubled-angle cosine there is nonpositive,
so \(|1-\rho e^{-2\pi is}|\ge1\) and (7) follows.

Suppose \(1/5\le v\le1/2\). Then
\(x\in[1/2,1/2+v]\). On this interval the arc integral
\(A_\rho(x,v)\) increases to its centered arc at
\(x=(1+v)/2\), then decreases, because
\[
               \partial_x A_\rho=f_\rho(x)-f_\rho(x-v).
 \tag{8}
\]
Symmetry gives equal values at the two endpoints. Thus
\[
 A_\rho(x,v)\ge A_\rho(1/2,v)
                  =-\int_0^{1/2-v} f_\rho(s)\,ds\ge0.          \tag{9}
\]
For the last inequality, an increasing function on \([0,1/2]\)
with integral zero has every initial integral nonpositive.
The claims extend to the integrable zero by continuity.
This proves (7). \(\square\)

For the outgoing radius \(R\ge1\), the pointwise inequality
\[
                      |1-Re^{i\theta}|\ge|1-e^{i\theta}|
 \tag{10}
\]
follows by differentiating its squared modulus in \(R\).
Among arcs of length \(v\le1/2\), the integral of
\(\log(2|\sin\pi s|)\) is minimized by the arc centered at an
integer. The same monotonicity and symmetry argument as in
(8) proves this even when the arc crosses the zero. Hence
\[
       \int_{z-v}^{z}\log|1-Re^{-2\pi is}|\,ds
                                     \ge 2J(v/2) .           \tag{11}
\]
No outgoing angle is changed in the finite source; (11) is an
upper-envelope comparison for its complementary integral.

## 3. Reflection to the last-row rate

The incoming period integral in (4) is zero and the outgoing
one is \(\log R=2\pi H\). Thus the continuous rate at one is
\[
                      \mathcal R(1;a,y)=2\pi H+\delta .        \tag{12}
\]
This is the limiting last-row rate, not a new finite index \(j=N\).
For \(v=1-t\in[0,1/2]\), periodicity gives the exact difference
\[
 \begin{split}
 \mathcal R(1-v;a,y)-\mathcal R(1;a,y)
   ={}&-A_\rho(x,v)
       -\int_{z-v}^{z}\log|1-Re^{-2\pi is}|\,ds\\
      &+3J(v)-\delta v .
 \end{split}                                                     \tag{13}
\]
In particular Lemma 1 and (11) imply
\[
 \mathcal R(1-v;a,y)
       \le 2\pi H+\delta(1-v)+D(v),\qquad
                  D(v)=3J(v)-2J(v/2).                        \tag{14}
\]

The scalar \(D\) has two useful elementary bounds:
\[
 \begin{array}{ll}
 D(v)\le0,&0\le v\le1/3,\\
 D(v)<\dfrac95(v-1/3),&1/3<v\le1/2 .
 \end{array}                                                     \tag{15}
\]
Indeed sine duplication and \(J(1-u)=-J(u)\) give
\[
           D(0)=D(1/3)=0,\qquad
 D''(v)=\frac{\pi(5\cos\pi v-1)}{2\sin\pi v}>0
                                      \quad(0<v\le1/3).
 \tag{16}
\]
Convexity proves the first line. On \([1/3,1/2]\),
\[
 e^{D'(v)}=\frac{(2\sin\pi v)^3}{2\sin(\pi v/2)} .
 \tag{17}
\]
Its maximum occurs at \(\cos\pi v=1/5\), by (16).
The square of that maximum is
\[
                         \frac{110592}{3125}<36 .
 \tag{18}
\]
Therefore \(D'(v)<\log6<9/5\). The latter bound uses only
\(\log2<7/10\) and \(\log3<11/10\); elementary positive-series
witnesses are given, for example, in
[the sectorwise first-end proof](research_mixed_three_four_next_sectorwise_first_end.md).
Integration from \(1/3\) proves the second line of (15).

For \(t\ge2/3\), (14)--(15) already show
\[
              \mathcal R(t;a,y)\le \mathcal R(1;a,y)
                       \le\frac{41\pi}{250}.                 \tag{19}
\]
For \(27/50\le t\le2/3\), one has
\(1/3\le v\le23/50\), \(2\pi H\le\pi/50\), and
\(0\le\delta\le18\pi/125\). Thus
\[
 \mathcal R(1-v;a,y)
  \le\frac{\pi}{50}+\frac{18\pi}{125}(1-v)
                          +\frac95(v-1/3).
 \tag{20}
\]
This affine upper bound increases with \(v\), since
\(18\pi/125<1/2<9/5\). At \(v=23/50\) it gives
\[
 \mathcal R(t;a,y)
       <\frac{611\pi+1425}{6250}
       <\frac{23417}{43750}.                                 \tag{21}
\]
The last inequality uses \(\pi<22/7\). The same rational
comparison gives
\[
 \frac{13}{24}-\frac{41\pi}{250}
       >\frac{551}{21000}>\frac1{40},\qquad
 \frac{13}{24}-\frac{23417}{43750}
       =\frac{3371}{525000}>\frac1{160}.                      \tag{22}
\]
It follows on the entire parameter set (1) that
\[
 \boxed{\quad
 \mathcal R(t;a,y)<\Re\Theta(a,y)-\frac1{160},
                            \qquad 27/50\le t\le1 .
 \quad}                                                       \tag{23}
\]
Every inequality concerns the original rate with the incoming
chirp, rather than a rate with the incoming height set to zero.

## 4. The complete finite tail and its fixed jets

Define exactly
\[
 C^{\rm up}_{1,N}(a,y)=
   \sum_{j=\lceil27N/50\rceil}^{N-1}
                  X^{-j}p_j(X)p_j(Y)/P_j^3 .
 \tag{24}
\]
Equations (5) and (23) give a positive-sum estimate for this
entire group. After choosing the common tolerance and absorbing
the finite number of rows into polynomial factors, one obtains
\[
 \sum_{j=\lceil27N/50\rceil}^{N-1}
 \left|X^{-j}p_j(X)p_j(Y)/P_j^3\right|
       \le C N^B e^{N\{\Re\Theta(a,y)-1/320\}}.               \tag{25}
\]
In particular (25) bounds any subset of these rows. Both level
parities, the final physical row, and every incoming or outgoing
numerator zero are retained.

The row sets in (24) are independent of the parameters. Uniform
zero-safe continuity of the numerator integrals, the denominator
bounds, and the proved holomorphic critical branch preserve a
strict part of (23) on a fixed complex neighborhood of the compact
set (1). One may choose that neighborhood and the finite tolerances
so that the normalized holomorphic tail
\[
                         e^{-N\Theta(a,y)}C^{\rm up}_{1,N}(a,y)
 \tag{26}
\]
and all of its fixed mixed derivatives, on smaller neighborhoods,
are bounded by a polynomial in \(N\) times \(e^{-N/320}\).
This follows by Cauchy's formula applied to the complete finite
sum after the source bounds; no floor or cutoff is differentiated.
Multiplication by the original outer residue density \(N\) changes
only the polynomial prefactor.

The theorem pays an actual complete physical row group at the full
incoming depth. It does not identify that group with an incoming
contour arc or with a Fourier coefficient. In particular the
remaining wall rows
\[
                         1-x\le j/N<27/50
 \tag{27}
\]
are not bounded by (25). A whole conditional packet on the displaced
rectangle still requires its real upper-cut comparison and the
remaining rows; the cap and the full ordinary-next affine comparison
are separate as well.

