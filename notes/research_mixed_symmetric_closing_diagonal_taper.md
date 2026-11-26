# A paid diagonal taper on the taller closing rectangle

Private written finite-source deduction, 9 November 2026. A diagonal
first-angle path pays both sectors of the enlarged edge envelope.
It connects the original critical-height right endpoint to the
vertical at \(2\pi/3\), which then reaches height \(1/10\).
The subsequent low and far connectors remain separate.

No mathematical numerical evaluation, saved-value arithmetic, import,
compilation, or frozen-source edit is used.

## 1. Original source and path

Keep the calibrated phase from the
[taller strip theorem](research_mixed_symmetric_closing_strip_phase_and_tail.md):
\[
 u=\beta-iK,\quad0\le\beta\le\pi/2,\quad0\le K\le7/10,\qquad
 t_*(u)=a_*(u)-iH_*(u),\qquad s(u)=\Re S_3(0,u),
\]
\[
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+3it^2/(4\pi)-it,\qquad
 s(u)>321/200.
 \tag{1}
\]
In fact \(2/3<H_*<1\). To verify the new lower height explicitly,
write the original cubic root as \(v=x+ib=2\cos(t_*/2)\).
Its imaginary equation at \(b=1/2\) has right side
\(-x^2/2+7/8<0\), since \(x>3/2\). On this lower outgoing
rectangle \(\Im\cos(u/2)\ge0\), so connected continuation of
the original root gives \(b>1/2\). If \(H_*\le2/3\), then
\[
 b=2\sin(a_*/2)\sinh(H_*/2)
 <\sqrt2\sinh(1/3)
 <(10/7)(18/53)=180/371<1/2,
 \tag{2}
\]
a contradiction. The series bound used here is
\(\sinh x\le x/(1-x^2/6)\) at \(x=1/3\).

Set
\[
 d=\pi/2-\max a_*(u)>0,\qquad
 g_0=\min\{d^2/(8\pi),1/5000\}>0 .
 \tag{3}
\]
All extrema are over the compact rectangle in (1).
The new path, oriented to the right and then upwards, is
\[
 \begin{split}
 \gamma_D(u):\quad
 t(a)&=a-i\{H_*(u)-(a-\pi/2)\},
                  &&\pi/2\le a\le2\pi/3,\\
 \gamma_V(u):\quad
 t&=2\pi/3-ih,
                  &&H_*(u)-\pi/6\ge h\ge1/10 .
 \end{split}
 \tag{4}
\]
Its joining height belongs to \((1/7,1/2)\), by (2) and
\(3<\pi<22/7\). Thus the whole path is in the enlarged
high/vertical finite-edge domain.

Use the exact two-short-edge current
\[
 \begin{gathered}
 U_N=\lfloor N/2\rfloor-1,\qquad
 K_N^<(t,u)=\sum_{j=0}^{U_N}e_j(-2\cos t)e_j(-2\cos u),\\
 g_N^{<<}(t,u)=\sin t\,K_N^<(t,0)K_N^<(t,u)e^{3iNt^2/(4\pi)},\\
 \eta_N=(-1)^{N-1},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2},\qquad
 C_{N,3}=e^{3\pi i(N-1)^2/(4N)} .
 \end{gathered}
 \tag{5}
\]
These are the original double-pole trace factors, with no row or
alias removed.

**Theorem.** Uniformly on (1), at both parities and all sufficiently
large \(N\),
\[
 \left|-\frac{N^2C_{N,3}}{\pi i}
       \int_{\gamma_D(u)\cup\gamma_V(u)}
                    g_N^{<<}(t,u)W_N(t)\,dt\right|
             \le C e^{N(s(u)-g_0/4)} .
 \tag{6}
\]
The same bound holds for the sum of the two absolute integrals.
This theorem stops at \(2\pi/3-i/10\).

## 2. Both relevant Hessian signs

On \(0<a\le2\pi/3,\ 1/10\le H\le1\), put
\[
 c=\cos((a-iH)/2),\quad C=\cos(u/2),\quad
 A=c^2,\ B=C^2,\ D_0=A+B-AB .
 \tag{7}
\]
The original mixed and high-edge branches give
\[
 \Phi_{tt}=-\frac1{2\pi}
       \left\{\frac1c+\frac C{c\sqrt{D_0}}\right\}
                         +\frac{3i}{2\pi}.
 \tag{8}
\]
No branch is assigned from this derivative formula: both source
theorems identify the same original primitive on their overlap.

First,
\[
 |1-A|<21/20,\quad |1-B|<13/20,\quad
 |1-D_0|<273/400<1/\sqrt2 .
 \tag{9}
\]
The last strict comparison follows from \(149058<160000\).
Hence \(|\arg\sqrt{D_0}|<\pi/8\). Also
\[
 0<\arg c<\pi/4,\qquad0\le\arg C<7/20<\pi/8 .
 \tag{10}
\]
For the first inequality use
\(\tan(a/2)\tanh(H/2)<\sqrt3/2<1\); for the second use
\(\tan(\beta/2)\tanh(K/2)<7/20\).
Thus \(C/(c\sqrt{D_0})\) has positive real part.
The original extended secant bound is
\(\Re(1/c)>7/8\) on this whole first-angle rectangle.
In particular
\[
                         \Re\Phi_{tt}<-1/(4\pi).
 \tag{11}
\]

We also need the sign of its imaginary part. Write
\(A=A_r+iA_i,\ B=B_r+iB_i\), where \(A_i>0,\ B_i\ge0\).
Here
\[
 A_r>1/10,\quad A_r<13/10,\quad
 B_r\ge1/2,\quad B_r<23/20 .
 \tag{12}
\]
If \(A_r\le1\), then
\(\Re D_0\ge(1+A_r)/2>11/20\).
If \(A_r\ge1\), then
\(\Re D_0\ge1-(3/10)(3/20)=191/200>11/20\).
Moreover \(|c|\ge1/2\) and \(|C|<17/16\). Therefore
\[
 \left|\frac C{c\sqrt{D_0}}\right|
       <\frac{17}{8\sqrt{11/20}}<3,
 \qquad 5780<6336 .
 \tag{13}
\]
Since \(\Im(1/c)<0\), (8) and (13) imply
\[
                              \Im\Phi_{tt}>0.
 \tag{14}
\]
The inequalities persist with uniform margins on the compact
parts of these rectangles used below.

## 3. Geometric and endpoint rates on the diagonal

For fixed \(u\), set \(R(a,H)=\Re\Phi(a-iH,u)\), and keep the
literal endpoint sector
\[
 E(a,H)=\Re\psi(a-iH,0)+(H+K)/2+3aH/(2\pi)-H .
 \tag{15}
\]
The original critical point has \(\Phi_t(t_*,u)=0\).
Integrating (11) horizontally at height \(H_*\) gives
\[
 R(\pi/2,H_*)\le s-d^2/(8\pi).
 \tag{16}
\]
The same horizontal integration of (14) shows that
\(\Im\Phi_t(\pi/2-iH_*,u)>0\), whereas its real part is
negative. Thus the derivative of \(R\) in the diagonal
direction \(dt/da=1+i\) is negative at the initial point.
Along the entire diagonal,
\[
 \frac{d^2}{da^2}R(a,H_*-(a-\pi/2))
            =\Re\{2i\Phi_{tt}\}=-2\Im\Phi_{tt}<0 .
 \tag{17}
\]
The geometric rate therefore decreases along \(\gamma_D\).

By the taller mixed-edge endpoint lemma,
\(\Re\psi(\pi/2-iH_*,u)>(H_*+K)/2+1/400\).
Consequently
\[
 E(\pi/2,H_*)<R(\pi/2,H_*)-1/400 .
 \tag{18}
\]
We show that \(E\) also decreases along this diagonal.
Let \(r_0(t)=\operatorname{arsinh}\tan(t/2)\), with its
original branch. At \(a=\pi/2\),
\[
 \frac d{dH}\{\Re r_0-\Im r_0\}
                =\tfrac12\{\Re\sec(t/2)+\Im\sec(t/2)\}>0.
 \tag{19}
\]
Indeed the half-cosine argument is
\(\arctan(\tanh(H/2))<\pi/4\).
At \(H=0\), the expression is \(\operatorname{arsinh}1>3/4\);
the exact series witness is \(\sinh(3/4)\le24/29<1\).
The initial diagonal derivative of (15) is therefore
\[
 E'_D=-\frac14+
       \frac{3H_*/2-(\Re r_0-\Im r_0)}{\pi}<0,
 \tag{20}
\]
using \(H_*<1\) and \(3/4<\pi/4\).

The holomorphic function whose real part is \(E\) is
\(\psi(t,0)+3it^2/(4\pi)-it/2+K/2\). Its diagonal
second derivative has real part
\[
 E''_D=-\{3-\Im\sec(t/2)\}/\pi<-3/\pi .
 \tag{21}
\]
Thus \(E\) decreases throughout \(\gamma_D\). Equations
(16)--(21) pay both attached sectors on this full segment.

## 4. A uniform low geometric endpoint

Put \(a_0=2\pi/3,\ h_0=1/10,\ t_0=a_0-ih_0\). We prove
\[
                     \Re\Phi(t_0,u)<321/200-1/5000 .
 \tag{22}
\]
The first edge has
\(\psi(0,0)=2b_2,\ b_2<7/12\), and
\(\psi_{tt}(t,0)=-\sec(t/2)/(2\pi)\).
For \(0\le x<\pi/2\), the differential identity
\(\sec''x=2\sec^3x-\sec x\) gives successively
\[
 \sec x\ge1+x^2/2+5x^4/24+61x^6/720 .
 \tag{23}
\]
For an explicit derivation, \(2y^3-y\) is increasing for \(y\ge1\).
Start with \(\sec x\ge1+x^2/2\), substitute it in that identity
and integrate twice to obtain the \(5x^4/24\) term.
Substituting \(1+x^2/2+5x^4/24\) again gives the
\(61x^4/24\) lower term in \(\sec''x\), and hence the last
term in (23). All omitted coefficients are nonnegative.
Two integrations now give
\[
 2\psi(a_0,0)
 <\frac73-\frac{2\pi}{9}-\frac{\pi^3}{486}
                -\frac{\pi^5}{26244}
                -\frac{61\pi^7}{66134880}.
 \tag{24}
\]
Using \(25/8<\pi\), the four losses in (24) respectively exceed
\[
             \frac{25}{36},\qquad\frac{251}{4000},
             \qquad\frac9{800},\qquad\frac1{400}.
 \tag{25}
\]
The quartic comparison is \(62500000>62456832\).
For the next two use \(\pi^2>39/4\), so
\(\pi^5>38025/128\) and \(\pi^7>177957/64\).
Their cleared comparisons are respectively
\(30420000>30233088\) and \(4342150800>4232632320\).
The sum in (25) is \(13877/18000\).

Raising the first height to \(h_0\) costs at most
\(h_0^2/\pi<2/625\) for two copies of this edge:
at real part \(a_0\),
\[
 \Re\sec((a_0-ih)/2)
       =\frac{\frac12\sqrt{1+\sinh^2(h/2)}}
                    {\frac14+\sinh^2(h/2)}\le2,
 \tag{26}
\]
and the initial height derivative vanishes.

For the outgoing edge at \(t_0\), move first along the real
angle \(0\le b\le\beta\). Its real derivative is nonpositive,
as is its initial downward-height derivative, because
\(\cos(t_0/2)\) is in the first quadrant and the return is
principal. Along the subsequent downward segment, put
\(A=\cos^2(t_0/2),B=\cos^2((\beta-ik)/2)\).
The elementary bound \(\cosh(1/10)<101/100\) gives
\[
 99/400<\Re A<1/4,\quad \Im A>0,\quad
 \Re B\ge1/2,\quad\Im B\ge0,\quad
 \Re D_0>(1+\Re A)/2>499/800>9/16 .
 \tag{27}
\]
Also \(|\cos(t_0/2)|<13/25\) by the original low-height
bound, and \(|\cos((\beta-ik)/2)|\ge1/\sqrt2>7/10\).
The calibrated derivative consequently satisfies
\[
 |\psi_{uu}(t_0,\beta-ik)|
   =\left|\frac{\cos(t_0/2)}
       {2\pi\cos((\beta-ik)/2)\sqrt{D_0}}\right|
                  <\frac1{2\pi}.
 \tag{28}
\]
The explicit ratio bound before \(1/(2\pi)\) is \(104/105<1\).
The whole downward cost is at most
\(K^2/(4\pi)<49/1250\).
At \(a_0\) the real cubic crossing and charge cancel exactly.
Equations (24)--(28) yield
\[
 \Re\Phi(t_0,u)
 <\frac73-\frac{13877}{18000}+\frac{53}{1250}
 =\frac{144431}{90000}
 =\frac{321}{200}-\frac{19}{90000}
 <\frac{321}{200}-\frac1{5000}.
 \tag{29}
\]
This proves (22) with the original action normalization.

## 5. The remaining vertical and complete finite current

At \(a=a_0\), (11) gives \(R_{HH}=-\Re\Phi_{tt}>0\).
Its upper-depth endpoint is the paid end of \(\gamma_D\);
its lower-depth endpoint is paid by (22) and (1).
Convexity therefore bounds the whole vertical by \(s-g_0\).
For the endpoint sector,
\[
 E(a_0,h)=\Re\psi(a_0-ih,0)+h/2+K/2
 \tag{30}
\]
strictly increases in \(h\), since \(\Im r_0<0\).
Its maximum is the already paid diagonal endpoint.
Thus both rates in the full finite-edge envelope are at most
\(s-g_0\) on \(\gamma_D\cup\gamma_V\).

The first shortened factor in (5) has its original slit bound
\(\exp N(\Re\psi(t,0)+\tau)\), up to fixed polynomial costs.
The whole path is a fixed compact of that slit domain.
The second factor has the enlarged full envelope
\(\exp N(\max\{\Re\psi(t,u),(h+K)/2\}+\tau)\).
These estimates retain every original physical row and both parities.
On the path \(h\ge1/10\), so the exact multiplier is
\[
                    |W_N(t)|\le Ce^{-Nh}.
 \tag{31}
\]
It retains all Fourier charges. The sine, path lengths and
\(|C_{N,3}|\) are uniformly bounded. Choose each source allowance
smaller than \(g_0/4\), then absorb the original \(N^2/\pi\)
and remaining polynomial factors into a further allowance
smaller than \(g_0/4\). This proves (6).
The whole replacement path lies strictly below the real sampling
line, and its endpoints agree with those of the previous high
horizontal followed by its vertical. The finite integrand in (5)
is holomorphic between these paths. Cauchy's theorem therefore
preserves that original current without an added residue or cap.

The path ends at the same point as the old low connector,
but that connector's outgoing-height domain has not been enlarged
by this proof. The central signed current and both exact edge
deletions are independent source theorems. No full inner packet
or ordinary closing asymptotic is asserted here.

## Frozen source bindings

- Taller calibrated cubic/action and full outgoing trace:
  fa1224123389462fd7e29199f1045d0892c167225b4dd6f79ea5bd967a583795.
- Taller mixed packet, endpoint gap, and signed central source:
  01630dd45f907e7d116fc8d51fed0ef00e13176f379b5ce1ab0186403cd1a94c.
- Enlarged complete high/vertical finite-edge envelope:
  9451d127c809566902d4b629e949b6c87517b9ffc06ff27776e191573ec88c5f.
- Original secant bound through first real angle \(2\pi/3\):
  492ae47bfcaa02198c0e819ef97cb9e7afb7c066d559a84373031091612b2c53.
- Original low first-height derivative and normalization:
  5813ddfa3f16e81c7907bbf8e11f6be0d07d30e0e71a74f5845d889aa1a4ac85.
- All-row complete-end slit upper bound:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Exact original one-remaining-current assembly:
  2c5be7138aed7dabbb06f04010c602ee095fa8ceb62ec213e75e4d628aa95421.
