# Lower rows and regular currents at the full negative incoming height

Research deduction, 7 November 2026. The lower physical rows, both
horizontal residue remainders, the complete lower vertical remainder,
and the lower unweighted main-path connector are exponentially smaller
than the original conditional critical action throughout the displaced
incoming rectangle. The incoming carrier is included in every estimate.

The upper physical rows and the real upper cut are separate obligations.
This note does not assert a complete conditional asymptotic. No numerical
evaluation is used.

## 1. The original finite source and its critical action

Keep
\[
\begin{gathered}
r=e^{-2\pi i/N},\quad D=N-1,\quad
P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\\
C_{1,N}(X,Y)=\sum_{j=0}^{D}
             \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},\\
a=x+ih_a,\quad \frac12\le x\le\frac7{10},\quad
       -\frac9{125}\le h_a\le0,\\
y=z+iH,\quad \frac{11}{50}\le z\le\frac9{20},\quad
       0\le H\le\frac1{100},\qquad
X=e^{-2\pi ia},\quad Y=e^{-2\pi iy}.
\end{gathered}                                                    \tag{1}
\]
The original phase is
\[
Q(s;a,y)=g(a+s)+g(y+s)-3g(s)-g(a)-g(y)+2\pi ias,
\qquad g'(w)=\Log(1-e^{-2\pi iw}).                                \tag{2}
\]
The logarithm is principal on \(0<\Re w<1\); its primitive
constant is unchanged. The
[negative-height branch theorem](research_mixed_conditional_negative_height_branch.md)
and the
[height-action theorem](research_mixed_conditional_height_action_monotonicity.md)
give a simple original critical point \(s_*=s_*(a,y)\), with
\[
\begin{gathered}
Q_s(s_*;a,y)=0,\qquad
\frac1{16}<\Re s_*<1-x,\qquad
\frac25<|e^{2\pi is_*}|<2,\\
\Theta(a,y)=Q(s_*;a,y),\qquad M(a,y)=\Re\Theta(a,y)>\frac{13}{24}.
\end{gathered}                                                    \tag{3}
\]
All strict critical-point distances have positive uniform minima
on the compact parameter set (1). In addition,
\[
\Re Q_{ss}(t+i\eta;a,y)<0
\quad\left(\frac1{16}\le t<1-x,\quad \eta\in\mathbb R\right).
                                                                    \tag{4}
\]
The same inequality holds a little below \(1/16\), as the cited
cotangent proof applies from \(3/50\). On fixed compact regular
strips with bounded height it has a uniform strict reserve.

For real \(t\), write the zero-safe physical row rate as
\[
\begin{split}
R(a,y;t)={}&-2\pi h_a t-3J(t)\\
 &+\int_0^t\log|1-e^{2\pi h_a-2\pi i(x+u)}|\,du
  +\int_0^t\log|1-e^{2\pi H-2\pi i(z+u)}|\,du .
\end{split}                                                       \tag{5}
\]
The original uniform finite-product upper estimate is
\[
\left|X^{-j}p_j(X)p_j(Y)/P_j^3\right|
 \le C N^B e^{N R(a,y;j/N)}.                                     \tag{6}
\]
It is valid through numerator zeros and at both extreme indices.
The regularized-log proof in
[the joint-source theorem, Section 2](research_mixed_half_face_joint_source_packet.md)
gives the same estimate on bounded parameter neighborhoods, with
uniformly continuous integrated rate. For a continuous real index
strictly inside the regular factorial chart, (5) is exactly
\(\Re Q(t;a,y)\). Thus no interpolation of an integer-degree
estimate is needed at a real cut.

## 2. The complete physical lower end

Put \(T=e^{-2\pi h_a}\). The full allowed height satisfies
\[
\log T\le\frac{18\pi}{125}<\frac6{13}<\log(8/5),
\qquad T<\frac85.                                                \tag{7}
\]
Here \(\pi<22/7\) gives \(18\pi/125<396/875<6/13\),
and \(\log u>2(u-1)/(u+1)\) for \(u>1\) gives the last
comparison. The first integral in (5), together with its carrier,
is therefore, for \(t>0\),
\[
\int_0^t\log|T-e^{-2\pi i(x+u)}|\,du<t.                         \tag{8}
\]
Indeed \(T+1<13/5<8/3<e\), where the last strict inequality
is supplied by the first four terms of the exponential series.
The outgoing factors obey
\[
1+e^{2\pi H}<\frac{339}{164}<\frac{25}{12}
 <\frac{269}{128}<e^{3/4}.                                     \tag{9}
\]
The first inequality uses the original bound
\(e^{\pi/50}<175/164\). The last rational number in (9) is
\(1+3/4+(3/4)^2/2+(3/4)^3/6\).

For \(0<t\le1/16\), the sine chord
\(2\sin\pi u\ge6u\) gives
\[
J(t)\ge t\{\log(6t)-1\},\qquad
R(a,y;t)< f(t):=t\{3+7/4-3\log(6t)\}.                          \tag{10}
\]
The derivative \(f'(t)=7/4-3\log(6t)\) is positive on this
interval. Consequently
\[
\begin{split}
R(a,y;t)&<f(1/16)
 =\frac{19/4+9\log2-3\log3}{16}<\frac{161}{320},\\
R(a,y;0)&=0.
\end{split}                                                       \tag{11}
\]
We used \(\log2<7/10\) and \(\log3>1\). In particular
\[
\frac{13}{24}-\frac{161}{320}=\frac{37}{960}>0.                 \tag{12}
\]
Joint continuity of (5) gives a fixed lower collar
\(0\le t\le1/16+\varepsilon_-\) on which
\[
R(a,y;t)<\frac{161}{320}+\frac1{100},\qquad
M(a,y)-R(a,y;t)>\frac{137}{4800}>\frac1{40}.                     \tag{13}
\]
The collar is uniform in (1). It can be made smaller whenever
needed to retain the critical point above its upper endpoint.

Set
\[
L_N=\lfloor N/16\rfloor+1,\qquad
                     \ell_N=(L_N-1/2)/N .                       \tag{14}
\]
The omitted physical rows are exactly \(0\le j<L_N\), including
\(j=0\), and they have (11). For all large \(N\), the real
half-grid cut \(\ell_N\) has (13). Summing the positive bounds
(6) costs only a polynomial factor. Hence the complete lower
physical sum and the real lower cut lie strictly below the original
critical action at every allowed incoming height. This statement
uses all physical rows in the lower range and both parities.

## 3. Exact regular rectangle and all-height argument bounds

Choose any sufficiently small fixed \(\varepsilon>0\) such that
the original critical point is retained below the upper cuts
\[
K_N(x)=\lceil N(1-x-\varepsilon)\rceil,
\qquad u_N=(K_N(x)-1/2)/N.                                      \tag{15}
\]
Such a choice follows from (3) and compactness. It makes
\(\ell_N<\Re s_*<u_N\), with uniform positive distances for
all large \(N\). All factors in the exact interpolation
\[
T_N(s;a,y)=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                    E_N(a)E_N(y)E_N(s)^3                       \tag{16}
\]
are in their original regular strips on
\[
\ell_N\le\Re s\le u_N,\qquad |\Im s|\le2.                     \tag{17}
\]
Here \(\Pi_N\) is the original negative-root factorial and
\(E_N=1/\Pi_N\). At every retained integer \(s=j/N\), (16)
is exactly the summand in (1). The incoming numerator has
real-part distance at least \(3\varepsilon/4\) from its wall.
The new incoming height only enlarges the fixed bounded ranges
of the imaginary factorial arguments; it does not change their
regular real strips or the exact recurrence.

Write \(A(w)=\Arg(1-e^{-2\pi iw})\). For every real height,
\(A(\xi+i\eta)\) lies between \(0\) and \(\pi-2\pi\xi\)
if \(0<\xi<1/2\), and between \(\pi-2\pi\xi\) and zero
if \(1/2<\xi<1\). Thus, with \(s=t+i\eta\),
\[
\partial_\eta\Re Q
 =-A(a+s)-A(y+s)+3A(s)-2\pi x.                                 \tag{18}
\]
The carrier contribution is \(-2\pi\Re a\), not a term in
\(\Im a\). For \(\eta\ge0\), the same argument intervals as in
[the original far-half alias theorem, Section 2](research_mixed_next_far_half_conditional_aliases.md)
give
\[
\partial_\eta\Re Q
\le\max\{2\pi-4\pi t,\ \pi+2\pi z-2\pi t\}
\le\frac{9\pi}{5}.                                             \tag{19}
\]
We use \(t\ge1/20\) and \(z\le9/20\), which hold on (17)
for large \(N\). This calculation is independent of the incoming
height.

For \(\eta\le0\), the outgoing height is at most \(1/100\),
and \(z+t\ge27/100\). If \(z+t\ge1/2\), its argument is
nonpositive. Otherwise put \(\theta=2\pi(z+t)\). The original
guard gives
\[
e^{2\pi(H+\eta)}(\sin\theta+\cos\theta)
\le\frac{175}{164}\frac{23}{25}<1,
\qquad A(y+s)<\frac\pi4.                                      \tag{20}
\]
The incoming and own-denominator terms in (18) have favorable
signs, regardless of the incoming height. Therefore
\[
\partial_\eta\Re Q\ge-\frac\pi4-2\pi x
                         \ge-\frac{33\pi}{20}\quad(\eta\le0).
                                                                    \tag{21}
\]
Equations (19)--(21) yield
\[
\Re Q(t+i\eta)-\Re Q(t)\le
\begin{cases}
(9\pi/5)\eta,&\eta\ge0,\\
(33\pi/20)|\eta|,&\eta\le0.
\end{cases}                                                       \tag{22}
\]

## 4. Paid residue remainders

Keep the exact positively oriented rectangle identity
\[
\begin{split}
\sum_{j=L_N}^{K_N(x)-1}T_N(j/N;a,y)
 &=N\int_{\ell_N}^{u_N}T_N(t;a,y)\,dt+\mathcal R_N(a,y),\\
\mathcal R_N&=\frac{N}{2i}\left\{
\int_{\partial\mathcal R^+}T_N(s)[\cot(\pi Ns)+i]\,ds
+\int_{\partial\mathcal R^-}T_N(s)[\cot(\pi Ns)-i]\,ds
\right\}.
\end{split}                                                       \tag{23}
\]
Each sign-half comprises its two outer vertical portions and its
horizontal side, with no real segment. This is the identity of
the far-half alias theorem, now with complex \(a\); holomorphy on
(17) leaves its residues, signs and original density \(+N\)
unchanged.

At either half-grid vertical cut the appropriate remainder kernel
is at most \(2e^{-2\pi N|\eta|}\). On the horizontal sides
\(|\eta|=2\), the same bound holds with the constant four.
Combining with (22) leaves additional rates
\[
-\frac\pi5\eta\quad(\eta\ge0),\qquad
-\frac{7\pi}{20}|\eta|\quad(\eta\le0)                           \tag{24}
\]
relative to the real value at that index. Thus the entire lower
vertical remainder is paid by (13), at both signs of height.
The upper vertical remainder has the same reduction to its real
upper-cut value, but that value is not bounded by this argument.

Both horizontal remainders have a separate uniform estimate.
On the retained real interval, where \(0<t<1/2\), (8)--(9)
and the original \(-J(t)<1/6\) give
\[
\Re Q(t;a,y)<\frac74t-3J(t)<\frac{11}{8}.                       \tag{25}
\]
At height two, the smaller loss in (24) is \(2\pi/5\).
Therefore each horizontal remainder has rate below
\[
\frac{11}{8}-\frac{2\pi}{5}<\frac7{40}<\frac{13}{24},           \tag{26}
\]
using only \(\pi>3\). No cap estimate or outside Fourier
weight is used in (26). Uniform factorial tolerances and
polynomial factors leave a finite gap, for example \(1/80\),
for the lower physical sum, the lower vertical remainder, and
both horizontal remainders relative to \(M(a,y)\).

## 5. The complete lower main-path connector

Move the real zero mode in (23) to height
\(h_*=\Im s_*(a,y)\). The exact path replacement retains
the lower connector from \(\ell_N\) to \(\ell_N+ih_*\), the
translated horizontal main path, and the upper connector from
\(u_N+ih_*\) to \(u_N\). Neither connector carries a decaying
cotangent kernel.

Let
\[
d_-:=\min_{(a,y)\text{ in }(1)}(\Re s_*(a,y)-1/16)>0.
\]
The radius bounds in (3) keep \(|h_*|\) bounded strictly below
two. Compactness in (4) gives \(\kappa>0\) on the relevant
retained strips and heights. For all large \(N\), horizontal
concavity through the actual saddle implies
\[
\Re Q(\ell_N+ih_*;a,y)
 \le M(a,y)-\frac{\kappa d_-^2}{8}.                             \tag{27}
\]
The real endpoint obeys (13). Along the lower connector,
\(\partial_{\eta\eta}\Re Q=-\Re Q_{ss}>0\), so its phase is
bounded by the larger endpoint value. This pays the whole
unweighted connector, for either sign of \(h_*\), with uniform
phase gap at least
\[
\eta_-:=\min\{1/40,\ \kappa d_-^2/8\}>0.                       \tag{28}
\]
Its length, the residue density \(N\), and the original
factorial symbol change only polynomial prefactors. The upper
connector would follow by the same argument once its real
endpoint has a strict own-action bound. No such upper-end
bound is asserted here.

## 6. Source scope and fixed derivatives

The estimates above retain the literal source (1), the exact
carrier, the true row \(j=0\), both parity choices, and all four
residue sides in (23). Only the explicitly paid sides have been
removed. In particular the outstanding source groups are the
physical rows \(j\ge K_N(x)\), the real upper cut and its
vertical remainders, and the upper unweighted join. The main
Gaussian and its nonzero coefficient cannot be substituted for
the entire sum before these groups are controlled.

The displayed strict gaps also give local holomorphic and fixed
mixed derivative bounds. At each base parameter keep both
integer cuts, all row groups, the alias paths, and the lower
connector fixed. Their strict gaps persist on a small fixed
parameter neighborhood: use the zero-safe physical estimate
(5)--(6), and ordinary phase continuity on the compact regular
paths. Normalize each paid contribution by the original
\(e^{N\Theta(a,y)}\), then apply Cauchy's formula on a smaller
neighborhood. For every fixed mixed derivative the bound has
the form \(C N^B e^{-N\gamma}\), for some common
\(\gamma>0\) smaller than \(\eta_-\) and the other displayed
reserves. No derivative of a moving integer cut is taken.

These conclusions concern only the conditional factor. There
is no ordinary-color variable in (1), no added observation
scalar, and no conclusion about the remaining cap or the
selected next-source affine comparison.
