# Uniform extreme-index bounds for the adjacent two-crossing source

Research lemma, 2 November 2026. The exact double sum for two adjacent
power-two fillings has a uniformly negligible high boundary-index
sector. Fixed strips along every outer edge of its triangular index
domain are negligible as well. These are absolute estimates for the
original finite polynomial, valid for every real boundary angle and
both level parities.

The proof also gives a rational lower bound for the real part of the
selected complex action. It does not deform the remaining compact
interior sum through that stationary point. Contributions from that
interior and its lattice corrections still require a contour argument.

## 1. Exact source and statement

Let \(D=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
\(F_r=(Q;Q)_r\), and
\[
 S_r=\prod_{k=1}^r2\sin(\pi k/N),\qquad S_0=F_0=1.
\]
The exact Newton polynomial is
\[
 e_j(z)=S_j^{-2}\prod_{r=0}^{j-1}
        \left(2\cos\frac{(2r+1)\pi}{N}-z\right).
\]
The exact original source is
\[
 Z_N(u)=N^2\sum_{\substack{i,j\ge0\\i+j<N}}
       q^{i^2+(i-j)^2}\frac{F_{i+j}}{F_i^3F_j^2}
                         e_j(-2\cos u).
 \tag{1}
\]
This is Proposition 1 of
[the adjacent-pair calculation](research_adjacent_two_crossing_pair.md).
Its proof uses the full original crossing and closing functional, with
the derivatives at double roots retained. All indices in denominators
are below \(N\).

The canonical phase on the regular low-index chart is
\[
 W(x,y;u)=J(x+y)-3J(x)-2J(y)+b(y,u)
        +i\pi(x^2-xy+y^2/2+x+y/2),
 \tag{2}
\]
where
\[
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,
 \qquad
 b(y,u)=\int_0^y\log(2\cos2\pi t+2\cos u)\,dt-2J(y).
\]
The logarithm in \(b\) starts with its real value for
\(0<y<1/2\), \(u=0\), and continues on the regular chart.
In particular \(b(y,0)=g(y)=J(2y)-4J(y)\).
Let
\[
 X=\frac{5+i\sqrt7}{16},\quad Y=\frac{i}{\sqrt7},\quad
 x_* =\frac{\log X}{2\pi i},\quad
 y_* =\frac{\log Y}{2\pi i},\quad
 M=\operatorname{Re}W(x_*,y_*;0),
 \tag{3}
\]
with exactly the branches fixed in that calculation.

An index \(j\) is high when \(2j\ge N\). Let
\(Z_N^{\mathrm{high}}\) be the sum of all such terms in (1).
For the fixed number \(\epsilon=10^{-6}\), let
\(Z_N^{\mathrm{tail}}\) be the sum of terms satisfying at least
one of
\[
 \frac iN\le\epsilon,\qquad
 \frac jN\le\epsilon,\qquad
 1-\frac{i+j}{N}\le\epsilon,\qquad
 \frac jN\ge\frac12-\epsilon.
 \tag{4}
\]
Each term is counted once even if several conditions hold.

**Proposition.** There are constants \(C,A\) independent of \(N\)
and the real angle \(u\) such that
\[
 \sup_{u\in\mathbb R}|Z_N^{\mathrm{high}}(u)|
                    \le CN^A e^{2N/3},
 \tag{5}
\]
\[
 M>\frac{1500409991957}{1956907128000}>\frac34,
 \tag{6}
\]
\[
 \sup_{u\in\mathbb R}|Z_N^{\mathrm{tail}}(u)|
                    \le CN^A e^{N(M-1/200)}.
 \tag{7}
\]
The same tail has the complex-strip bound
\[
 \sup_{\substack{\tau\in\mathbb R\\|v|\le1/400}}
 |Z_N^{\mathrm{tail}}(\tau+iv)|
                    \le CN^{A+1}e^{N(M-1/400)}.
 \tag{8}
\]
The constants may be enlarged to include the finitely many small levels.

## 2. The absolute rate of the exact summand

For real \(u\), the Newton basis satisfies
\[
 |e_j(-2\cos u)|\le e_j(-2)\quad(2j<N),
 \qquad
 \sup_{u\in\mathbb R}|e_j(-2\cos u)|\le CN^A\quad(2j\ge N).
 \tag{9}
\]
The first inequality follows from its positive Laurent coefficients.
The second is the full polynomial interval estimate in
[the complete-node norm proof](../papers/conway-source-bounds/norms.tex).
That proof controls the first derivatives at repeated nodes before
interpolation. Thus (9) does not infer a polynomial bound merely from
vanishing spectral values. At an odd level the remaining simple endpoint
is included as well.

In (1), \(|q|=1\) and \(|F_r|=S_r\). Taking absolute values
therefore leaves exactly
\[
 N^2\frac{S_{i+j}}{S_i^3S_j^2}|e_j(-2\cos u)|.
 \tag{10}
\]
The uniform estimate
\(\log S_r=NJ(r/N)+O(\log N)\), including \(r=0,D\),
retains all the factorial shifts in (10). For a low boundary index,
\(\log e_j(-2)=Ng(j/N)+O(\log N)\) uniformly on its full
range. Hence (10) is bounded by a fixed power of \(N\) times
\(e^{NH(x,y)}\), where \(x=i/N\), \(y=j/N\), and
\[
 H(x,y)=J(x+y)-3J(x)-2J(y)+\bar g(y),
 \tag{11}
\]
\[
 \bar g(y)=
 \begin{cases}
   g(y),&0\le y\le1/2,\\
   0,&1/2\le y\le1.
 \end{cases}
\]
This function is continuous on
\(\mathcal D=\{x,y\ge0:x+y\le1\}\), since \(g(1/2)=0\).
The polynomial bound for high indices has been used as a bound on the
entire original basis polynomial. No part of the root multiplicity data
or of the exact coefficient in (1) has been removed.

There are at most \(N^2\) summands. It will therefore suffice to bound
the continuous rate (11) on the specified parts of \(\mathcal D\).

## 3. Two elementary real bounds

On \([0,1/2]\), one has \(J\le0\). Its unique minimum occurs
at \(1/6\), since \(J'(t)=\log(2\sin\pi t)\). Put
\[
 c=-J(1/6)=\max_{0\le t\le1/2}(-J(t)).
\]
Strict concavity of the sine function gives
\(\sin\pi t>3t\) for \(0<t<1/6\), by comparison with the
chord from zero to \(1/6\). Consequently
\[
 c=-\int_0^{1/6}\log(2\sin\pi t)\,dt
   <-\int_0^{1/6}\log(6t)\,dt=\frac16.
 \tag{12}
\]

Also \(g'(t)=2\log\cot\pi t\), so \(g\) has its unique
maximum at \(1/4\). Its value is
\[
 g(1/4)=\frac{2\mathsf G}{\pi},\qquad
 \mathsf G=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)^2}.
\]
The first three terms of this alternating series give
\(\mathsf G<1-1/9+1/25=209/225\). Using \(\pi>157/50\)
yields the rational bound
\[
 \max g<\frac{836}{1413}.
 \tag{13}
\]
Only these deliberately coarse constants are needed.

## 4. A rigorous lower bound for the selected action

All the selected arguments \(x_*,y_*,x_*+y_*,2y_*\) have
positive imaginary part and real part in \((0,1)\). On exactly
these canonical branches,
\[
 J(z)=\frac{i\pi}{2}z(1-z)
       +\frac{\pi^2/6-\operatorname{Li}_2(e^{2\pi iz})}{2\pi i}.
 \tag{14}
\]
Its derivative is the chosen \(\log(2\sin\pi z)\), and its
constant is fixed by the limit \(J(0)=0\). Thus (14) has no
undetermined logarithmic winding or real additive constant.

Write \(a=\operatorname{Re}x_*\). The exact moduli in (3) give
\[
 \operatorname{Im}x_* =\frac{3\log2}{4\pi},\qquad
 \operatorname{Re}y_* =\frac14,\qquad
 \operatorname{Im}y_* =\frac{\log7}{4\pi}.
\]
Substitute (14) in (2). Since \(Y^2=-1/7\) has real
dilogarithm, the real part simplifies to
\[
 \begin{split}
 M={}&\frac{3\log2+\log7}{8}
       +a\left(-3\log2+\frac{\log7}{2}\right)\\
 &+\frac{-\operatorname{Im}\operatorname{Li}_2(XY)
          +3\operatorname{Im}\operatorname{Li}_2(X)
          +6\operatorname{Im}\operatorname{Li}_2(Y)}{2\pi}.
 \end{split}
 \tag{15}
\]

Here \(0<a<1/10\): its numerator argument is
\(\arctan(\sqrt7/5)<53/100<\pi/5\).
The elementary logarithmic bounds
\[
 \frac{69}{100}<\log2<\frac7{10},\qquad
 \log7>\frac{19}{10}
 \tag{16}
\]
give
\[
 \frac{3\log2+\log7}{8}
       +a\left(-3\log2+\frac{\log7}{2}\right)
        >\frac{397}{800}-\frac{23}{200}.
 \tag{17}
\]
For clarity, (16) needs no decimal approximation: the series
\(\log\frac{1+t}{1-t}=2\sum_{k\ge0}t^{2k+1}/(2k+1)\)
at \(t=1/3\) bounds \(\log2\) below by \(56/81\)
and above by \(25/36\). Its first four terms at \(t=3/4\)
already exceed \(19/10\).

The remaining bounds use the absolutely convergent dilogarithm series
\(\operatorname{Li}_2(z)=\sum_{n\ge1}z^n/n^2\).
The rational inequalities
\[
 \operatorname{Im}X>\frac{33}{200},\qquad
 |X|<\frac{177}{500},\qquad
 |XY|<\frac{67}{500},\qquad
 \sqrt7<\frac{53}{20}
\]
follow immediately by squaring the positive quantities. They give
\[
 \operatorname{Im}\operatorname{Li}_2(X)
 >\frac{33}{200}
       -\frac{(177/500)^2}{4(1-177/500)}=:L_X.
 \tag{18}
\]
Indeed \(1/n^2\le1/4\) for every omitted term \(n\ge2\).
For \(Y=i/\sqrt7\), the imaginary part is an alternating series
with decreasing terms, so
\[
 \operatorname{Im}\operatorname{Li}_2(Y)
 \ge\frac1{\sqrt7}-\frac1{9\cdot7\sqrt7}
 >\frac{1240}{3339}=:L_Y.
 \tag{19}
\]
Finally,
\[
 \left|\operatorname{Im}\operatorname{Li}_2(XY)\right|
 \le\left|\operatorname{Li}_2(XY)\right|
 <\frac{67}{433}=:U_{XY}.
 \tag{20}
\]
The rational number \(3L_X+6L_Y-U_{XY}\) is positive.
Since \(\pi<22/7\), inserting (17)–(20) into (15) gives
\[
 \begin{split}
 M&>\frac{397}{800}-\frac{23}{200}
          +\frac7{44}(3L_X+6L_Y-U_{XY})\\
  &=\frac{1500409991957}{1956907128000}
    =0.7667251912\ldots>\frac34.
 \end{split}
 \tag{21}
\]
The elementary bounds for \(\pi\) used here can themselves be
checked by rational arithmetic: apply the alternating arctangent
series to Machin's identity
\(\pi=16\arctan(1/5)-4\arctan(1/239)\), using two terms
for the first lower bound and three for the first upper bound.
They give \(157/50<\pi<22/7\).

This proves (6) for the actual logarithmic action. No numerical
evaluation of the saddle or inference from a Hessian is used.

## 5. High boundary indices and the three outer faces

For \(y\ge1/2\), put \(a=x\), \(b=1-y\). The triangular
support gives \(0\le a\le b\le1/2\). Reflection
\(J(1-t)=-J(t)\) turns (11) into
\[
 H(x,y)=-J(b-a)-3J(a)+2J(b)\le4c<\frac23,
 \tag{22}
\]
because \(J(b)\le0\). Together with (10) and the polynomial
state count, this proves (5). It also bounds the entire line
\(y=1/2\).

On the outer boundary of \(\mathcal D\), the low-index part of
(11) has the following exact restrictions:
\[
 \begin{array}{c|c|c}
 \text{face}&H&\text{upper bound}\\ \hline
 x=0&-J(y)+g(y)&c+\max g\\
 y=0&-2J(x)&2c\\
 x+y=1,\quad y\le1/2&J(y)+g(y)&\max g.
 \end{array}
 \tag{23}
\]
The remaining portions with \(y\ge1/2\) are already covered by
(22); on the diagonal one may also use \(-J(x)\le c\).
Equations (12)–(13) therefore give one common bound for all outer
faces and for \(y=1/2\):
\[
 H<\frac16+\frac{836}{1413}
    =\frac{2143}{2826}=:T_0.
 \tag{24}
\]
The selected-action lower bound in (21) exceeds \(T_0\) by the
positive rational number
\[
 \frac{7751110327747}{921703257288000}
                         =0.0084095507\ldots.
 \tag{25}
\]

## 6. Explicit strips, including the endpoint indices

Continuity would already give fixed strips with a strict gap. The
following modulus makes the choice \(\epsilon=10^{-6}\) explicit.
For \(0\le s,t\le1\) with \(|s-t|\le\eta\le1/2\),
\[
 |J(s)-J(t)|\le\omega(\eta),\qquad
 \omega(\eta)=\eta(3-2\log\eta).
 \tag{26}
\]
To see this, concavity gives
\(2\sin\pi v\ge4\min(v,1-v)\), and the positive part of
its logarithm is at most \(\log2<1\). Hence
\[
 |\log(2\sin\pi v)|\le1-\log v-\log(1-v).
\]
On an interval of length at most \(\eta\), each of the two
negative logarithms has integral at most
\(\eta(1-\log\eta)\). This proves (26), including the endpoints.

If \(x\le\epsilon\), compare with \((0,y)\); if
\(1-x-y\le\epsilon\), compare with \((1-y,y)\).
In either case the rate changes by at most \(4\omega(\epsilon)\).
If \(y\le\epsilon\), comparison with \((x,0)\) costs at most
\(7\omega(\epsilon)+\omega(2\epsilon)\).
For \(1/2-\epsilon\le y\le1/2\), compare with
\((\min(x,1/2),1/2)\). Both coordinates change by at most
\(\epsilon\), and their sum changes by at most \(\epsilon\).
The total cost is at most
\(10\omega(\epsilon)+\omega(2\epsilon)\).
The region \(y\ge1/2\) is already bounded by (22).

Since \(\log10<3\), the chosen \(\epsilon\) satisfies
\[
 10\omega(\epsilon)+\omega(2\epsilon)
                  <468\epsilon=\frac{117}{250000}.
 \tag{27}
\]
For example \(\log10<3\) follows from
\(e^3>1+3+9/2+27/6>10\).
Combining (24)–(27), every scaled state in (4) has
\[
 H(x,y)\le T_0+\frac{117}{250000}
       <\frac{1500409991957}{1956907128000}-\frac1{200}
       <M-\frac1{200}.
 \tag{28}
\]
The middle inequality is an exact rational comparison.
The uniform factorial error and the number of states contribute only
a power of \(N\). Equations (10) and (28) prove (7), including
\(i=0\), \(j=0\), \(i+j=D\), and indices immediately
adjacent to the low/high division. No fixed shift in (1) has been
replaced by a continuum convention in the finite bound.

The partial sum \(Z_N^{\mathrm{tail}}(u)\) is a trigonometric
polynomial of degree at most \(D\). Each Fourier coefficient is
bounded by its real-circle supremum. Thus
\[
 |Z_N^{\mathrm{tail}}(\tau+iv)|
 \le(2D+1)e^{D|v|}
                 \sup_{u\in\mathbb R}|Z_N^{\mathrm{tail}}(u)|.
\]
Taking \(|v|\le1/400\) proves (8).

## 7. The remaining contour problem

The estimates permit (1) to be restricted, with a proved exponential
error, to the fixed compact polygon
\[
 x\ge\epsilon,\qquad
 \epsilon\le y\le1/2-\epsilon,\qquad
 x+y\le1-\epsilon.
 \tag{29}
\]
Every factorial argument in its canonical interpolation is separated
from the real endpoints. The real parts of \((x_*,y_*)\) lie
inside this polygon. High boundary indices and extreme triangular
indices are therefore no longer an unresolved part of this test case.

The absolute real rate inside (29) can exceed the selected action.
Its cancellation has not been estimated here. A full theorem still
needs a contour through \((x_*,y_*)\), control of all connecting
faces of that deformation, and suppression or evaluation of the
nonconstant lattice modes. In particular, this note does not show
that the stationary coefficient in the adjacent-pair calculation is
the coefficient of the whole finite sum. The exact shifts and their
phases in (1) and (2) remain necessary in that remaining argument.

One candidate is the parallel horizontal contour
\[
 (x,y)=\left(a+\frac{3i\log2}{4\pi},
             b+\frac{i\log7}{4\pi}\right),
\]
with \((a,b)\) ranging over the retained polygon. It passes through
the selected critical point. No global maximum estimate on this
contour, or estimate for its connecting faces, is proved here.
