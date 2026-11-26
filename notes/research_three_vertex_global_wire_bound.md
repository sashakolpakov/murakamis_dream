# A global modulus bound for the retained three-crossing vertex

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

After the exact corner deletion, the homogeneous wire is the unique
maximum of the absolute summand entropy over the entire Fourier torus,
not just over its local wire chart. This gives an exponential bound
for the absolute complementary cyclic integral and for the full-period
retained chain with fixed homogeneous Fourier endpoints. Actual
complete ordinary-color caps still require their own contour estimates.

## 1. The original finite density and its global real envelope

Use the exact matrices, cardinal functions and corner deletion from
[the traced-vertex proof](research_traced_three_vertex_endpoint.md),
Sections 1--2 and 7. In particular
\[
 \widetilde V_N(x,y)=h(x)^T\widetilde A h(y),\qquad
 \widetilde A=JM^3-M^TP_LJM P_LM,\qquad L=\lfloor N/50\rfloor.
 \tag{1}
\]
Every physical value and first normal is included in this original
trace identity. Its exact finite sum is
\[
 \widetilde V_N(x,y)=\kappa c_xc_y
 \sum_{\substack{i,j\ge0,\ i+j<N\\\max(i,j)>L}}
 \frac{X^iY^j(Q^{-1};Q^{-1})_{i+j}}
 {(X;Q^{-1})_{i+1}(Y;Q^{-1})_{j+1}},
 \quad X=e^{2\pi ix},\ Y=e^{2\pi iy},
 \quad c_x=\frac{e^{-\pi i(N-1)x}(1-X^N)}N.
 \tag{2}
\]
The source has not been replaced by a value-only interpolation.
The factorial products and cardinal factors in (2) are the literal
finite ones, including their parity carriers and finite endpoints.

Fix the common height and the selected wire
\[
 Y_*:=\frac{\log2}{2\pi},\qquad
 x_*:=\frac16+iY_*,\qquad r:=\frac12,\qquad
 c:=2\mathcal J(5/6)=-3\mathcal J(1/3),
 \quad\mathcal J(s)=\int_0^s\log(2\sin\pi u)\,du.
 \tag{3}
\]
Write \(x=\xi+iY_*\), \(y=\eta+iY_*\), with real phases
\(\xi,\eta\) modulo one. Define
\[
 f(v)=\log|1-r e^{2\pi iv}|,\qquad
 I(s,\xi)=\int_0^s f(\xi-u)\,du,\qquad
 \ell(s)=\int_{-s/2}^{s/2}f(v)\,dv.
 \tag{4}
\]
The function \(f\) is smooth, periodic, even, and strictly
increasing on \((0,1/2)\). For \(0<s<1\), a translated
interval of length \(s\) has its unique minimal integral when
centered at zero modulo one. More explicitly,
\(I_\xi=f(\xi)-f(\xi-s)\) vanishes only at
\(\xi=s/2\) and \(\xi=(1+s)/2\) modulo one; the first is
the strict minimum and the second the strict maximum. Therefore
\[
 I(s,\xi)\ge\ell(s),
 \qquad I(s,\xi)=\ell(s)\iff\xi=s/2\pmod1
                            \quad(0<s<1).
 \tag{5}
\]
At \(s=0,1\), equality is understood without the uniqueness claim.

Put \(\epsilon=1/50\) and
\[
 \begin{split}
 \mathcal D&=\{s,t\ge0:s+t\le1,\ \max(s,t)\ge\epsilon\},\\
 \mathcal H(s,t)&=\mathcal J(s+t)+(s+t)\log r-\ell(s)-\ell(t).
 \end{split}
 \tag{6}
\]
The uniform finite-endpoint sine-factorial bound and the uniform
Riemann-sum estimate for the nonvanishing denominator products give,
for each summand in (2), an absolute upper bound
\[
 CN^a\exp N\{\log2+\mathcal J(s+t)+(s+t)\log r
                    -I(s,\xi)-I(t,\eta)\},\qquad s=i/N,\ t=j/N.
 \tag{7}
\]
The exponent includes both outside cardinal factors. Indeed
\(|X|=|Y|=r\), while their product has rate \(-\log r=\log2\).
All derivative bounds for \(f\) are uniform on the circle because
\(|1-r e^{2\pi iv}|\ge1-r\), so the denominator error is
\(O(1)\). The numerator has the usual \(O(\log N)\) logarithmic
error through both endpoints. The retained lattice lies in
\(\mathcal D\) exactly, since \(\max(i,j)>\lfloor\epsilon N\rfloor\)
implies \(\max(s,t)>\epsilon\).

## 2. The global entropy maximum, including every cut face

**Lemma 1.** On \(\mathcal D\), the unique maximum of
\(\mathcal H\) is at \(s=t=1/3\), and its value is
\[
              \mathcal H_* =2c-\log2>-3/50.
 \tag{8}
\]

*Proof.* Direct differentiation gives
\[
 \ell'(s)=\log|1-r e^{\pi is}|,\qquad
 \ell''(s)=\frac{\pi r\sin\pi s}{1+r^2-2r\cos\pi s}>0
                                          \quad(0<s<1).
 \tag{9}
\]
At an interior stationary point, equality of the two first
derivatives of \(\mathcal H\) therefore forces \(s=t\).
For \(0<s<1/2\), write \(v=\cos\pi s\in(0,1)\).
The remaining stationary equation is
\(\sin(2\pi s)=\sqrt{5/4-\cos\pi s}\), equivalently
\[
 16v^4-16v^2-4v+5
       =(2v-1)(8v^3+4v^2-6v-5)=0.
 \tag{10}
\]
The cubic decreases and then increases on \((0,1)\), is negative
at zero and at \(1/2\), and is positive at one. It has just one
root in \((1/2,1)\). Along the diagonal the derivative of
\(\mathcal H\) has the opposite sign to the polynomial in
(10). That cubic root therefore gives a strict diagonal minimum,
which cannot be an interior maximum. The only possible interior
maximum is \(v=1/2\), namely \(s=t=1/3\).

We check the full boundary of the retained domain. On an axis,
\[
 \partial_s\mathcal H(s,0)
  =\log\frac{\sin\pi s}{\sqrt{5/4-\cos\pi s}}\le0,
 \quad
 \sin^2\pi s-(5/4-\cos\pi s)
                    =-(\cos\pi s-1/2)^2.
 \tag{11}
\]
Hence every retained axis point has value at most
\(\mathcal H(\epsilon,0)\le\mathcal J(\epsilon)<-3/50\).
For the middle inequality use \(\ell(\epsilon)\ge\epsilon\log r\).
The last bound follows from
\(\mathcal J(\epsilon)\le[\log(\pi/25)-1]/50\) and
\(\pi e^2<25\).

The two new corner-cut faces are
\(s=\epsilon,\ 0\le t\le\epsilon\) and its transpose.
On the first,
\[
 \partial_t\mathcal H(\epsilon,t)
 =\log\frac{\sin\pi(\epsilon+t)}{|1-r e^{\pi it}|}
 \le\log\{2\sin(2\pi\epsilon)\}<0.
 \tag{12}
\]
Its maximum is therefore exactly the already controlled axis
endpoint. This retains the whole corner boundary, not only its
intersection with the diagonal.

On the remaining top edge \(s+t=1\), the Fourier series
\[
 \ell(s)=-\frac1\pi\sum_{k\ge1}
                              \frac{2^{-k}\sin(\pi ks)}{k^2}
 \tag{13}
\]
gives \(|\ell(s)|\le\operatorname{Li}_2(1/2)/\pi<3/(5\pi)\).
Thus its entropy is less than
\(-\log2+6/(5\pi)<-4/15<-3/50\).
All boundary pieces have been covered.

At \(s=t=1/3\), the minimizing wire phases in (5) are
\(\xi=\eta=1/6\). The exact calibrated value in
[the positive-cycle calculation](research_positive_three_crossing_cycle.md),
(14a)--(14b), is \(\mathcal H_*=2c-\log2\).
The established inequalities \(c>8/25\) and \(\log2<7/10\)
give the strict comparison in (8). The boundary and stationary-point
classification now prove uniqueness. \(\square\)

For completeness the scalar inequalities above require no numerical
maximization. The first three positive blocks of
\(D_3=\sum_{j\ge0}[(3j+1)^{-2}-(3j+2)^{-2}]\), together
with \(\sqrt3>19/11\), \(\pi<22/7\), give
\(c=3\sqrt3 D_3/(4\pi)>8/25\).
The first five terms of \(e^{7/10}\) exceed two. Also
\(\operatorname{Li}_2(1/2)\le1/2+1/16+1/36<3/5\),
\(\log2>2/3\), and the positive exponential series with a
geometric remainder gives \(e^2<15/2\), hence
\(\pi e^2<(22/7)(15/2)<25\).
These exact comparisons are checked in the reproduction below.

## 3. A uniform absolute bound over the full wire torus

**Theorem 2.** At both parities, for all real \(\xi,\eta\),
\[
 |\widetilde V_N(\xi+iY_*,\eta+iY_*)|
                                      \le CN^a e^{2cN}.
 \tag{14}
\]
For every fixed neighborhood \(U\) of \((1/6,1/6)\) in the
two-dimensional real torus, there is \(\delta_U>0\) such that
\[
 \sup_{(\xi,\eta)\notin U}
 |\widetilde V_N(\xi+iY_*,\eta+iY_*)|
                      \le C_U N^{a_U}e^{N(2c-\delta_U)}.
 \tag{15}
\]

*Proof.* By (5) and Lemma 1, the continuous exponent in (7)
has its unique maximum \(2c\) on
\(\mathcal D\times(\mathbb R/\mathbb Z)^2\) at
\((s,t,\xi,\eta)=(1/3,1/3,1/6,1/6)\).
Its maximum on the compact set with \((\xi,\eta)\notin U\)
is therefore strictly smaller. Apply the uniform finite bound (7)
and sum at most \(N^2\) terms. This proves both statements.
No cancellation in the retained sum is needed for these upper
bounds. All original finite normals are present because (2) was
an exact full-trace identity before any estimate. \(\square\)

## 4. Consequences for complete wire periods and the remaining cap issue

Choose the local interval \(I_d=x_*+[-d,d]\) from
[the local-composition theorem](research_three_vertex_local_composition.md),
with \(0<d<1/12\). In a cyclic chain of fixed length \(m\),
every complementary point to \(I_d^m\) has at least one wire
outside \(I_d\), hence at least one adjacent vertex pair outside
\(I_d^2\). Equations (14)--(15) give
\[
 N^m\int_{([0,1]+iY_*)^m\setminus I_d^m}
       \prod_{j=1}^m|\widetilde V_N(x_j,x_{j+1})|
                         |d\mathbf x|
             \le CN^a e^{N(2mc-\delta_d)},\quad x_{m+1}=x_1.
 \tag{16}
\]
This is an absolute exponential bound for the actual retained
finite integrand, stronger than a bound for its signed total.
It includes the loop \(m=1\) and the two parallel incidences
at \(m=2\). Combining it with the local Gaussian calculation
and then the already-proved cyclic corner-error bound yields
\[
 \operatorname{Tr}((JM^3)^m)
 =\kappa^m e^{2mcN}
       \frac{\rho^{m/2}}{1-\rho^m}(1+O_m(N^{-1})),
 \qquad \rho=(5-\sqrt{21})/2.
 \tag{17}
\]
This does not identify the cyclic network with a marked knot.

The same argument for \(m-1\) internal wires, with both Fourier
endpoints fixed at \(x_*\), proves the full-period retained
kernel formula
\[
 h(x_*)^T\widetilde A^m h(x_*)
 =\kappa^m N^{-1/2}e^{2mcN}
             \frac{a_0}{\sqrt{D_{m-1}}}(1+O_m(N^{-1})),
 \tag{18}
\]
where \(a_0\) and the positive continuant \(D_{m-1}\) are
exactly those in the local-composition theorem. For \(m=1\)
there is no intermediate integral. For fixed \(m\), the same
full-period packet holds on a sufficiently small complex neighborhood
of the two Fourier endpoints: the uniform finite-product exponents
are continuous there and preserve the complementary gap, while the
local critical point and its contours move holomorphically. All fixed
Fourier-endpoint derivatives follow by Cauchy's formula.

The word “retained” in (18) is essential. Raw Fourier endpoint
observations can see a larger corner contribution; the full original
one-vertex counterexample already proves this. The separate corner
error theorem applies to the actual ordinary-color end vectors,
not to arbitrary Fourier endpoint vectors. Consequently (16)--(18)
do not yet estimate the whole complete-ended ordinary-color chain.
Its first and last cap functions, their displaced stationary wires,
and their complementary contour pieces remain to be controlled.

## 5. Unequal radii and a positive modulus excess

The global argument survives small unequal changes in the two wire
heights, but its maximum is not the real part of the actual critical
action. Here is the precise local distinction. Write
\[
 h_i=Y_*+v_i,\quad r_i=e^{-2\pi h_i},\quad
 \ell_r(s)=\int_{-s/2}^{s/2}\log|1-r e^{2\pi iw}|\,dw,
\]
\[
 \mathscr E(s,t;v)=\mathcal J(s+t)+s\log r_1+t\log r_2
 -\ell_{r_1}(s)-\ell_{r_2}(t)
 -\tfrac12(\log r_1+\log r_2),\qquad
 E(v)=\max_{\mathcal D}\mathscr E(s,t;v).
 \tag{19}
\]
The last term is the exact cardinal-factor rate. The same translated
interval argument as (5), for each \(r_i\), makes (19) the global
absolute summand envelope over the two real wire phases.

**Proposition 3.** For all sufficiently small real \(v\), the maximum
in (19) is unique, lies in the interior near \((1/3,1/3)\), and
depends real analytically on \(v\). Its maximizing real wire phases
are \((s(v)/2,t(v)/2)\). One has
\[
 \begin{split}
 \binom{s(v)}{t(v)}
 &=\binom{1/3}{1/3}
     -2\sqrt3\begin{pmatrix}2&1\\1&2\end{pmatrix}^{-1}v
       +O(|v|^2),\\
 E(v)&=2c+\frac{2\pi}{\sqrt3}\,
       v^T\begin{pmatrix}3&-1\\-1&3\end{pmatrix}v
       +O(|v|^3).
 \end{split}
 \tag{20}
\]
Let \(\Phi\) be the actual retained phase in the fixed local packet,
and maximize its real part over a sufficiently small fixed real-phase
neighborhood at these heights:
\[
 R(v)=\max_{u\ {\rm near}\ 0}
    \Re\Phi(x_*+u_1+iv_1,x_*+u_2+iv_2).
\]
This maximum is also unique near the origin and satisfies
\[
 \begin{split}
 u_{\rm crit}(v)&=-\frac{\sqrt3}{2}v+O(|v|^2),\\
 R(v)&=2c+\frac{\pi}{\sqrt3}\,
        v^T\begin{pmatrix}5&-2\\-2&5\end{pmatrix}v+O(|v|^3),\\
 E(v)-R(v)&=\frac{\pi}{\sqrt3}|v|^2+O(|v|^3)>0
                        \qquad(0<|v|\ \hbox{sufficiently small}).
 \end{split}
 \tag{21}
\]

*Proof.* The strict global maximum at \(v=0\) has a fixed gap outside
every small index neighborhood. All the functions in (19) are
uniformly continuous on the compact domain for \(r_i\) near \(1/2\).
Near its maximum they are real analytic. Direct differentiation at
\((s,t,v)=(1/3,1/3,0)\) gives
\[
 \mathscr E_v=0,\qquad
 \mathscr E_{(s,t)(s,t)}
       =-\frac{\pi}{\sqrt3}\begin{pmatrix}2&1\\1&2\end{pmatrix},
 \quad \mathscr E_{(s,t)v}=-2\pi I,\quad
 \mathscr E_{vv}=\frac{4\pi}{\sqrt3}I.
 \tag{22}
\]
For the last identity, the logarithmic modulus is harmonic in the
wire variable. Thus differentiating the interval integral twice in
height gives minus its two endpoint phase derivatives, namely
\(\ell_{hh}=-4\pi/\sqrt3\). For the mixed identity,
\(\ell_{sh}=2\pi(r\cos(\pi s)-r^2)/
(1+r^2-2r\cos(\pi s))=0\) at the center. Also
\(\ell_h=-2\arg(1-r e^{\pi is})=\pi/3\), which proves
\(\mathscr E_v=0\). The negative index Hessian in (22) and the
implicit-function theorem give the unique local maximum. The global
gap excludes all other maximizers for sufficiently small \(v\).
The real Schur complement of (22) is
\[
 E''(0)=\frac{4\pi}{\sqrt3}
                     \begin{pmatrix}3&-1\\-1&3\end{pmatrix},
 \tag{23}
\]
and yields (20).

For (21) use the already independently computed actual holomorphic
Hessian
\[
 -\Phi''=k_0 C,\quad
 k_0=\alpha-i\beta,\quad
 \alpha=\frac{8\pi\sqrt3}{21},\quad \beta=\frac{4\pi}{7},
 \quad C=\begin{pmatrix}5&-2\\-2&5\end{pmatrix}.
\]
Since the first derivatives vanish, its real Taylor expansion is
\[
 \Re\Phi(x_*+u+iv)
 =2c-\frac{\alpha}{2}u^TCu
       -\beta u^TCv+\frac{\alpha}{2}v^TCv
       +O((|u|+|v|)^3).
 \tag{24}
\]
Here the vector notation denotes the two arguments. Real concavity
and the implicit-function theorem give
\(u_{\rm crit}=-(\beta/\alpha)v+O(|v|^2)\).
The identities \(\beta/\alpha=\sqrt3/2\) and
\((\alpha^2+\beta^2)/(2\alpha)=\pi/\sqrt3\) prove (21).
In particular the positive excess is about the actual complex
critical value; it is not a change of normalization. \(\square\)

What persists globally is the complementary gap. For every fixed
real-phase neighborhood \(U\) of the homogeneous point, (15) and
compactness give, after reducing the allowed height shifts,
a uniform positive gap from \(E(v)\) outside \(U\). No numerical
width, including the larger directed cap tube, is inferred here.
The finite products remain uniformly regular for these radii, so
the bound is for the actual retained vertex at both parities.

For a fixed chain, write \(\Delta>0\) for its available complementary
entropy gap and let \(C_{\rm cap}\) be an independently proved upper
rate for its actual cap factors on that complementary contour.
If \(M_{\rm target}\) is the intended combined action, a sufficient
strict comparison is
\[
 \Delta>
 \sum_{\text{vertices}}(E(v^{(j)})-R(v^{(j)}))
 +\left(C_{\rm cap}+\sum_{\text{vertices}}R(v^{(j)})
                         -M_{\rm target}\right).
 \tag{25}
\]
This is just the actual absolute upper rate
\(C_{\rm cap}+\sum E-\Delta<M_{\rm target}\), with the positive
modulus excess exposed. It states what must be checked for a cap
attachment; neither cap control nor that comparison follows from
Proposition 3. The excess in (21) prevents replacing them by an
asserted equality of envelope and action.

## 6. A quantitative one-height bound for the first attachment joins

The small-shift assertion above admits a useful explicit width when
only one height moves. Let
\[
 h_2=Y_*,\qquad Y_*-9/1000\le h_1\le Y_*,
 \qquad r=e^{-2\pi h_1},\qquad r_2=1/2.
 \tag{26}
\]
Then \(1/2\le r<53/100\), since
\(\log(53/50)>9\pi/500\).

**Proposition 4.** Uniformly over both full real wire phases,
\[
 |\widetilde V_N(\xi+ih_1,\eta+iY_*)|
       \le CN^A e^{6474N/10000}.
 \tag{27}
\]
The sharper bound proved below for its global summand envelope is
\[
 E(h_1-Y_*,0)
 \le 2c+\frac{29}{2}(h_1-Y_*)^2
 <\frac{1294613}{2000000}<\frac{6474}{10000}.
 \tag{28}
\]

*Proof.* We first locate the global maximum of (19), for every
\(1/2\le r\le53/100\), without assuming a local root continues
to be maximal. Write \(p=s+t\). On \(p\le1/3\), the inequalities
\(\ell_r(s)\ge s\log(1-r)\), \(\ell_{1/2}(t)\ge t\log(1/2)\)
give
\[
 \mathscr E(s,t)\le \log2+\mathcal J(p)+g(r),\qquad
 g(r)=-\tfrac12\log(2r)+\tfrac13\log\frac r{1-r}.
 \tag{29}
\]
One has \(g(1/2)=0\) and
\(g'(r)=-1/(6r)+1/(3(1-r))<2/5\) on this interval.
The retained domain has \(p\ge1/50\), and
\(\max_{[1/50,1/3]}\mathcal J<-3/50\): the derivative changes
from negative to positive only at \(1/6\), and both endpoint
values have that bound. Using \(\log2<347/500\) proves
\(\mathscr E<323/500=.646\) here.
The first forty positive blocks of the \(D_3\) series give
\(c>323/1000\). At \(s=t=1/3\), the height derivative at
\(h_1=Y_*\) vanishes and the height second derivative is positive.
Thus this point has value at least \(2c>.646\) for all the
heights under consideration, excluding the region \(p\le1/3\).

For \(1/3\le p\le1/2\), increase the smaller index, which is at
most \(1/4\). Its exponential derivative is
\[
 \frac{2r_i\sin(\pi p)}
             {|1-r_i e^{\pi i s_i}|}>1,\qquad
              1/2\le r_i\le53/100.
 \tag{30}
\]
Indeed this ratio increases with \(r_i\); at \(r_i=1/2\) its
numerator is at least \(\sqrt3/2\) and its denominator is at most
\(\sqrt{5/4-\sqrt2/2}<\sqrt3/2\).
The variation stays in the retained triangle, so this region
contains no global maximum.

On the convex region \(p>1/2\), the index Hessian is strictly
negative:
\[
 -\mathscr E_{(s,t)(s,t)}
     =\operatorname{diag}(d_1,d_2)+k{\bf1}{\bf1}^T,\quad
 d_i=\frac{\pi r_i\sin(\pi s_i)}
               {1+r_i^2-2r_i\cos(\pi s_i)},\quad
 k=-\pi\cot(\pi p)>0.
 \tag{31}
\]
On each lower face of \([3/10,37/100]^2\), the corresponding
first derivative is positive; on each upper face it is negative.
These follow from the two scalar inequalities
\[
 \sin^2(67\pi/100)>5/4-\cos(3\pi/10),
\]
\[
 (106/100)^2\sin^2(67\pi/100)
 <1+(53/100)^2-(106/100)\cos(37\pi/100).
 \tag{32}
\]
Here \(\sin(\pi p)\) decreases for \(p>1/2\), and the ratio
in (30) increases with \(r_i\). Thus the maximum on this small
square is interior. Strict concavity makes it the unique maximum
on the entire region \(p>1/2\), including its continuous boundary
values. The preceding exclusions prove it is the global maximum.

We can therefore differentiate that unique maximum on the full
radius interval. Put
\[
 q_i=\frac{2\pi(1-r_i\cos(\pi s_i))}
                  {1+r_i^2-2r_i\cos(\pi s_i)},\qquad
 A=\operatorname{diag}(d_1,d_2)+k{\bf1}{\bf1}^T .
 \tag{33}
\]
The real Schur formula for a change of \(h_1\) alone gives
\[
 E_{h_1h_1}=4d_1+q_1^2(A^{-1})_{11}.
 \tag{34}
\]
On the square just proved, direct one-variable endpoint bounds give
\[
 \frac53<d_i<\frac{21}{10},\qquad q_i<\frac{27}{4},\qquad k>1.
 \tag{35}
\]
For clarity, \(d_i\) increases with \(r_i\) and decreases with
\(s_i\); \(q_i\) decreases in both. The latter signs follow from
\(\cos(\pi s_i)<3/5<2r_i/(1+r_i^2)\). Thus only the three
endpoint values \(d(.37,.5)\), \(d(.30,.53)\), \(q(.30,.5)\)
and \(k(3/5)\) are needed. The checker verifies (32), (35)
by outward scalar arithmetic, without parameter sampling.
Equation (35) implies
\[
 (A^{-1})_{11}
 =\frac1{d_1+kd_2/(d_2+k)}<\frac{24}{55},\qquad
 E_{h_1h_1}<\frac{42}{5}
                 +\left(\frac{27}{4}\right)^2\frac{24}{55}
             =\frac{3111}{110}<29.
 \tag{36}
\]
Now integrate twice from \(E(0)=2c,E'(0)=0\).
The certified bound \(c<161533/500000\) gives (28), and the
literal finite-product estimate (7) proves (27).
All bounds are symmetric in the two wire variables. \(\square\)

The first attachment has
\(0<Y_*-\Im x_c<9/1000\), by its certified root disk.
Thus (27) covers the two vertical wire joins at real parts
\(7/50\) and \(1/5\), with the other endpoint fixed at \(x_*\).
For example an independently proved cap bound \(6319/5000=1.2638\)
on those joins would give total rate below \(1.9112\), strictly
below the certified attachment action \(1.9113\), with margin
\(1/10000\). This last statement is a comparison budget, not an
assertion of that cap bound.

## 7. Exact algebra and scalar reproduction

Run `python3 experiments/check_three_vertex_global_wire_bound.py`.
The [checker](../experiments/check_three_vertex_global_wire_bound.py)
and its [record](../repro/results/research-three-vertex-global-wire-bound.json)
verify the critical polynomial, its derivative
classification, the axis square identity and the strict rational
scalar comparisons. Its record is a check of the written global
entropy proof, not a numerical sample of a quantum asymptotic.
