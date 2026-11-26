# The raised contour and the right endpoint of the finite source

Research deduction, 7 November 2026. The raised horizontal contour
of the initialized finite source has exactly one maximum of the real
part of its phase, at the prescribed critical point. The entire right
weighted current, including its infinite ends, and the right joining
segment are bounded by their limiting endpoint rate. These estimates
complete the contour comparisons left open in
[the left-contour calculation](research_mixed_three_left_cycle_left_contour.md).
No numerical evaluation is used.

## 1. The exact row and the height of its critical point

Let \(a=b/N\) be physical, with
\[
 \frac{267}{1000}\le a\le\frac{433}{1000},\qquad
 y=x_0=\xi+i\upsilon,\qquad
 .18299<\xi<.18301,\quad .07871<\upsilon<.07873.
 \tag{1}
\]
Retain the original reciprocal factorial \(E_N\), and set
\[
 \begin{split}
 \mathscr T_{N,b}(t;y)
   &=N e^{\pi iNa-\pi iN[(a-t)^2+t^2]-\pi ia}
                      E_N(a-t)E_N(t)^2E_N(y-t),\\
 \alpha_N&=-\frac1{2N},\qquad \beta_{N,b}=a+\frac1{2N},\\
 w_{N,0}(v)&=\frac1{1+e^{2\pi Nv}}-\mathbf1_{\{v<0\}}.
 \end{split}
 \tag{2}
\]
The initialized source is the literal sum of this row at
\(t=k/N,\ 0\le k\le b\). All contour identities below use its
true finite interval.

The critical point \(t_*=-z_2\), from the second-period theorem,
satisfies
\[
       0<\Re t_*<\xi<a,\qquad 0<h_*:=\Im t_*<\upsilon.
 \tag{3}
\]
The last inequality is proved, with a strict compact reserve, in
[the right-critical-sheet calculation](research_mixed_three_fourier_conditional_right_critical_sheet.md),
equation (21). It is also included in the
[right endpoint gap](research_mixed_three_left_cycle_right_endpoint_gap.md).
Thus, throughout the raised segment \(t=u+ih_*\),
the three factorial arguments have imaginary parts
\(-h_*,h_*,\upsilon-h_*\), all separated from zero.

The original upper and lower half-plane factorial phases are denoted
by \(g_+\) and \(g_-\); their normalizations and period increments
are those of
[the global phase calculation](research_mixed_complex_horizontal_obstruction.md),
equations (6)--(7). The phase of the row on the entire raised segment is
\[
 \widehat{\mathcal F}(t)
   =-g_-(a-t)-2g_+(t)-g_+(y-t)
                      +\pi i\{a-(a-t)^2-t^2\}.
 \tag{4}
\]
These are the actual nonreal branches. An upper factorial is not
made periodic when its real argument crosses zero.
On \(0<\Re t<\xi\), (4) is the regular phase of the left-contour
calculation. Its critical action is exactly \(\Phi_1\), and
\[
 \Re\mathcal F_{tt}
   =-\pi\Re\{\cot\pi(a-t)+2\cot\pi t+\cot\pi(y-t)\}<0
                     \qquad(0<\Re t<\xi).
 \tag{5}
\]

## 2. The rest of the raised segment decreases strictly

Put
\[
 X=e^{-2\pi ia},\quad W=e^{-2\pi iy},\quad
 T=R e^{-2\pi iu},\quad R=e^{2\pi v},\quad S=e^{2\pi\upsilon}.
 \tag{6}
\]
Exponentiating the actual derivative in (4) gives
\[
 e^{\widehat{\mathcal F}_t}
       =\frac{(T-X)(T-W)}{X(1-T)^2}.
 \tag{7}
\]
In particular, since \(a\) is real,
\[
 \Re\widehat{\mathcal F}_t(u+iv)
        =\log\frac{|T-X||T-W|}{|T-1|^2}.
 \tag{8}
\]
Equation (8) remains valid for the two continuations across the
shifted real wall. It is an identity for the real derivative, not
a choice of logarithmic lift.

**Lemma 1.** For \(\xi\le u\le a\) and every \(v\ge0\),
\[
                       |T-X||T-W|<|T-1|^2.
 \tag{9}
\]

*Proof.* The output bounds give
\[
          \frac{163}{100}<S<\frac{33}{20},\qquad
 \sin(2\pi\xi)>\frac{114}{125},\qquad
                       \cos(2\pi\xi)<\frac{41}{100}.
 \tag{10}
\]
The last two witnesses are in the actual-input theorem.
For the exponential bounds use \(.49<2\pi\upsilon<.495\):
the terms through degree four in \(e^{.49}\) exceed \(1.63\),
while
\[
 e^{.495}\le1+.495+\frac{(.495)^2}{2(1-.495/3)}<1.65.
 \tag{11}
\]
These are rational comparisons of positive series.

First suppose \(u\ge a/2\). Then
\[
 |T-X|^2=R^2+1-2R\cos2\pi(a-u)
                       \le R^2+1-2R\cos2\pi u=|T-1|^2.
 \tag{12}
\]
To compare the other factor, write
\[
 f(u)=S\cos2\pi(u-\xi)-\cos2\pi u.
 \tag{13}
\]
This function is positive on the larger interval
\([\xi,433/1000]\). Indeed, with
\(\theta=2\pi u,\ \phi=2\pi\xi\), it is
\((S\cos\phi-1)\cos\theta+S\sin\phi\sin\theta\).
The first coefficient is negative. For
\(\phi\le\theta\le\pi/2\), its derivative is positive and its
initial value is \(S-\cos\phi>1.22\).
For \(\pi/2\le\theta\le2\pi(433/1000)\), both displayed
terms are positive. Consequently \(f''=-4\pi^2f<0\).
Its minimum is therefore at one of the two endpoints. At the
right endpoint,
\[
 f(433/1000)>
       \cos(134\pi/1000)-\frac{33}{20}\frac1{10000}>
                                                        \frac{91}{100}.
 \tag{14}
\]
Here \(433/1000-\xi<.25001\) gives the cosine bound
\(\cos2\pi(433/1000-\xi)>-1/10000\), and
\(134\pi/1000<.423\) gives
\(\cos(134\pi/1000)>1-(.423)^2/2\).
Thus \(f(u)>.91\). It follows that
\[
 |T-1|^2-|T-W|^2=1-S^2+2Rf(u)
                         >-1.7225+1.82R>0,
 \tag{15}
\]
because \(R\ge1\). Equations (12)--(15) prove (9) in this case.

Now suppose \(\xi\le u<a/2\). In particular \(u<.2165\), and
\[
 \cos2\pi u<.41,\qquad
 \cos2\pi(a-u)>-.0001,\qquad
 \cos2\pi(u-\xi)>.97.
 \tag{16}
\]
For the second bound, \(a-u\le.25001\) and
\(\sin(\pi/50000)<\pi/50000<.0001\).
For the third, \(u-\xi<.03351\), so
\(2\pi(u-\xi)<.211\) and \(1-(.211)^2/2>.97\).
It follows that
\[
 \begin{split}
 |T-1|^2&>R^2+1-.82R,\\
 |T-X|^2&<R^2+1+.0002R,\\
 |T-W|^2&<R^2+2.7225-3.1622R .
 \end{split}
 \tag{17}
\]
The three polynomial bounds used here are positive for \(R\ge1\).
Expanding their product comparison gives
\[
 \begin{split}
 |T-1|^4-|T-X|^2|T-W|^2
 &>1.522R^3-1.04946756R^2+1.5216555R-1.7225\\
 &>1.522R^3-1.0501R^2+1.5216555R-1.7225>0 .
 \end{split}
 \tag{18}
\]
The last polynomial has value \(.2710555>0\) at one. Its
derivative is positive for \(R\ge1\), since
\(4.566R^2-2.1002R+1.5216555>0\) there.
All decimals in (11), (14), (16)--(18) denote exact terminating
rationals. This proves (9). \(\square\)

At \(v=h_*\), (8)--(9) prove strict decrease on \([\xi,a]\).
Together with (5), the unique maximum on the entire segment
\([0,a]+ih_*\) is therefore \(t_*\).
The nonreal factorial expansions are uniform on this whole
compact family of segments, including the shifted real wall.
The displacements to \(\alpha_N,\beta_{N,b}\) are \(O(N^{-1})\)
inside the same nonreal charts; they cannot remove the strict
endpoint gaps.

Consequently the complete raised zero mode has the nonzero Gaussian
\[
 N\int_{\alpha_N+ih_*}^{\beta_{N,b}+ih_*}
       \mathscr T_{N,b}(t;y)\,dt
 =N^{-1/2}\mathcal C_J(a,y)e^{N\Phi_1(a,y)}(1+O(N^{-1})),
 \tag{19}
\]
where
\[
 \mathcal C_J=
  \frac{\sqrt{2\pi}\,e^{-\pi ia}}
  {\mathfrak a(a-t_*)\mathfrak a(t_*)^2
     \mathfrak a(y-t_*)\sqrt{-\mathcal F_{tt}(t_*)}}\ne0 .
 \tag{20}
\]
The square root has positive real part, as supplied by (5);
the contour is oriented from left to right. The factor
\(\mathfrak a\) is the original regular-strip factorial symbol.
Only the local coefficient (20) uses regular-strip arguments.
The full segment comparison used (4), with its actual continuations.

## 3. The right vertical profile has its maximum at height zero

Write \(d=a-\xi\), and let
\[
 A(x,H)=\Im g'(x+iH)\qquad(0<x<1).
 \tag{21}
\]
The limiting unweighted rate at the true right endpoint is the
continuous function
\[
 \begin{split}
 \mathcal R(v)={}&2\pi av-2\Re g(a+iv)
       -\Re g(1+y-a-iv)\\
       &+\pi(-v)_++2\pi(\upsilon-v)_+ .
 \end{split}
 \tag{22}
\]
The two positive parts come from the midpoint reciprocal and the
exact period factor of \(E_N(y-t)\), respectively. In particular
\[
 E_R:=\mathcal R(0)
       =-2J(a)-\Re g_+(y-a),\qquad J(a)=\Re g(a).
 \tag{23}
\]
Let \(\mathcal R_w(v)=\mathcal R(v)-2\pi|v|\).

**Lemma 2.** Uniformly on (1),
\[
 \mathcal R_w(v)\le E_R-\frac{\pi}{10}|v|
                                  \qquad(v\in\mathbb R),
 \tag{24}
\]
and
\[
 \mathcal R(v)\le E_R-\frac{\pi}{50}v
                                  \qquad(0\le v\le h_*).
 \tag{25}
\]

*Proof.* For \(0<v<\upsilon\), the original upper continuation
at negative real part has argument at least \(\pi(1+2d)\).
Also, for \(p=\cot\pi a<9/10\),
\[
 A(a,v)\le\pi(1/2-a)+\pi p v.
 \tag{26}
\]
This follows by differentiating: \(A_H(a,H)=\pi\Re\cot\pi(a+iH)
\le\pi p\) for \(H\ge0\). Differentiating (22), with the
original upper lift retained, gives
\[
 \mathcal R'(v)\le2\pi(\xi-a+pv)<-\frac{\pi}{50}.
 \tag{27}
\]
Indeed \(a-\xi>.08399\), whereas \(p\upsilon<.070857\).
This proves (25) using (3). It also proves the required
decrease of \(\mathcal R_w\) on this interval.

For \(v>\upsilon\), the negative-real outgoing argument is
in the lower half-plane. Its argument is greater than
\(-\pi(1/2-d)\), whereas \(A(a,v)<\pi(1-2a)\). Hence
\[
 \mathcal R_w'(v)
     <\pi(1/2-3a+\xi)<-\frac{\pi}{10}.
 \tag{28}
\]

Finally let \(v=-h<0\). The exact argument reflection is
\[
 \Im g_+'(-d+i(\upsilon+h))
       =\pi(1+2d)+A(d,-\upsilon-h).
 \tag{29}
\]
The midpoint argument at \(ih\) is \(\pi\). Substitution into
the derivative of (22) gives
\[
 \mathcal R_w'(v)
      =2\pi\xi+2A(a,-h)-A(d,-\upsilon-h)
                              >\frac{\pi}{10}.
 \tag{30}
\]
For the last inequality, \(A(a,-h)>0\), and the complex number
\(1-\rho e^{-2\pi id}\), where
\(\rho=e^{-2\pi(\upsilon+h)}<100/163<1/\sqrt2\),
lies on a circle of radius less than \(1/\sqrt2\) about one.
Its positive argument is therefore less than \(\pi/4\).
Thus the right side of (30) is greater than
\(\pi(2\xi-1/4)>\pi/10\).

The rates in (22) are continuous at zero and at \(\upsilon\).
Combining (27)--(30) proves (24)--(25). No logarithm of a
possibly vanishing finite period factor was taken. \(\square\)

## 4. Uniform finite-level bounds, including the infinite ends

At \(\beta=\beta_{N,b}\), the needed identities are exact:
\[
 \begin{split}
 |E_N(a-\beta-iv)|^2&=\frac{1+e^{-2\pi Nv}}{N},\\
 E_N(y-\beta-iv)
    &=(1+W^N e^{-2\pi Nv})E_N(1+y-\beta-iv).
 \end{split}
 \tag{31}
\]
The chirp modulus in (2) is \(e^{2\pi Nav+2\pi v}\).
The remaining real arguments \(\beta\) and \(1+\xi-\beta\)
stay in compact subintervals of \((0,1)\) for large \(N\).
For every fixed \(|v|\le H\), their regular factorial expansions,
the midpoint identity, and
\[
                  |1+W^N e^{-2\pi Nv}|
                          \le2e^{2\pi N(\upsilon-v)_+}
 \tag{32}
\]
give
\[
 |\mathscr T_{N,b}(\beta+iv;y)|
                       \le C_H N^{-1}e^{N\mathcal R(v)} .
 \tag{33}
\]
This bound includes the outgoing zero line \(v=\upsilon\).
It uses an upper bound for its exact factor, so no zero is divided out.
The \(O(N^{-1})\) real offsets in the other arguments have bounded
effects on these compact intervals.

Since \(|w_{N,0}(v)|\le e^{-2\pi N|v|}\), (24)--(25) yield
\[
 \begin{split}
 N\int_{-H}^H
 |w_{N,0}(v)\mathscr T_{N,b}(\beta+iv;y)|\,dv
                         &\le \frac C N e^{NE_R},\\
 N\int_0^{h_*}|\mathscr T_{N,b}(\beta+iv;y)|\,dv
                         &\le \frac C N e^{NE_R}.
 \end{split}
 \tag{34}
\]

To include both infinite ends, choose one fixed \(H>\upsilon+1\).
The exact weighted asymptotic slopes are
\(-2\pi(Na+1)\) upward and \(-2\pi(N\xi+1)\) downward, as in
the exact residue calculation for this row. Away from the real
zero line, the midpoint and period factors in (31) have their
explicit nonzero asymptotic factors. Comparing the remaining
reciprocal factorials between height \(H\) and any larger height
costs at most \(8N\varepsilon_H\), with
\(\varepsilon_H\to0\), by the original cyclotomic remainder bounds.
Choose \(H\) so that \(8\varepsilon_H<\pi H/20\).
The loss \(\pi H/10\) from (24), followed by those exact
tail slopes, bounds both complete tails by the same right side
of (34). Thus
\[
 \boxed{\quad
 N\int_{\mathbb R}
 |w_{N,0}(v)\mathscr T_{N,b}(\beta+iv;y)|\,dv
 +N\int_0^{h_*}|\mathscr T_{N,b}(\beta+iv;y)|\,dv
                  \le\frac C N e^{NE_R}.
 \quad}
 \tag{35}
\]
The [endpoint-value gap](research_mixed_three_left_cycle_right_endpoint_gap.md)
proves \(\Re\Phi_1-E_R>1/20\). Consequently every right contribution
in the exact residue decomposition is exponentially smaller than
the raised Gaussian (19). Both current signs and both level
parities are retained; the upper bound does not require cancellation
between the right current and its join.

All comparisons have strict compact reserves. A small fixed complex
neighborhood of the output \(y=x_0\) preserves them. Here the
incoming value is still the physical real number \(b/N\).
No holomorphic continuation of the integer index \(b\), or of its
summation endpoint, is asserted by these estimates.
