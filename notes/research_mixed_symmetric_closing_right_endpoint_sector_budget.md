# A right taper that pays the fixed-depth endpoint sector

Private written source comparison, 9 November 2026. At inner depth
\(7/10\), the endpoint sector of the complete wider-edge bound
has a useful attached budget. A specified right outer hyperbola
pays this sector uniformly. Its geometric sector and the omitted
inner connectors are explicitly not estimated.

No mathematical numerical evaluation, saved-value arithmetic,
import, compilation or frozen-source edit is used.

## 1. The actual closing action and a stronger existing floor

Let \(u_g=\beta_g-iK_g\) be the original geometric closing point,
and retain
\[
 \Xi(u)=2S_3(0,u)+iu^2/\pi-iu,\qquad
                         M_g=\Re\Xi(u_g).
 \tag{1}
\]
The adopted localization gives
\(0<\beta_g<\pi/2\) and \(17/30<K_g<7/10\).
The [horizontal maximum theorem](research_mixed_symmetric_closing_horizontal_concavity.md),
applied at the endpoint of its actual horizontal, gives
\[
 M_g\ge\Re\Xi(\pi/2-iK_g)
       =2\Re S_3(0,\pi/2-iK_g)>321/100.
 \tag{2}
\]
The equality uses the exact cancellation of the real parts of
the outer quadratic crossing and linear trace charge at
\(\Re u=\pi/2\). The last inequality is the original action
floor in the [taller strip theorem](research_mixed_symmetric_closing_strip_phase_and_tail.md).
No value of \(M_g\) has been evaluated.

## 2. A uniform first-edge comparison at depth \(7/10\)

Fix
\[
 h=7/10,\quad t=a-ih,\quad0\le a\le2\pi/3,\qquad
 u=\beta-iK,\quad\pi/2\le\beta\le2\pi/3,\quad1/10\le K\le7/10 .
 \tag{3}
\]
The complete source envelope supplied by the positive and signed
wider-edge theorems has the endpoint rate
\[
 E_h(a,u)=\Re\psi(a-ih,0)+(h+K)/2
                                  +3ah/(2\pi)-h.
 \tag{4}
\]
All constants here are the original ones; in particular
\(\psi(0,0)=2b_2\), \(b_2<7/12\).

We first sharpen the horizontal first-edge curvature:
\[
               \Re\sec((a-ih)/2)>16/17.
 \tag{5}
\]
Indeed put \(x=\cos(a/2)\in[1/2,1]\) and
\(s=\sinh(7/20)<3/8\). The exact real part is
\[
                  \frac{x\cosh(7/20)}{x^2+s^2}.
 \tag{6}
\]
Since \(x^2>s^2\), this decreases in \(x\). Its minimum is
\(\operatorname{sech}(7/20)>16/17\), using the adopted
positive-series bound \(\cosh(7/20)<17/16\).

The original first-edge formulas give
\[
 \frac{d^2}{da^2}\Re\psi(a-ih,0)
                =-\frac{\Re\sec((a-ih)/2)}{2\pi},\qquad
 \frac d{da}\Re\psi(a-ih,0)\big|_{a=0}=0.
 \tag{7}
\]
On the imaginary axis
\[
 \frac d{dh}\psi(-ih,0)
          =\frac{\arcsin(\tanh(h/2))}{\pi}
          \le\frac{h}{2\pi}.
 \tag{8}
\]
For the inequality, the derivative of
\(\arcsin(\tanh(h/2))\) is
\(\tfrac12\operatorname{sech}(h/2)\le1/2\), and both
sides vanish at zero. Integrating (5)--(8) yields
\[
 \Re\psi(a-ih,0)
      \le2b_2+\frac{h^2}{4\pi}-\frac{4a^2}{17\pi}.
 \tag{9}
\]

The quadratic upper bound for (4) increases throughout
\(0\le a\le2\pi/3\). Its vertex is
\(3h/(16/17)=357/160>2\pi/3\), using \(\pi<22/7\).
At the right endpoint it gives
\[
 E_h(a,u)\le C_h+K/2,\qquad
 C_h<\frac76+\frac{49}{400\pi}
                        -\frac{16\pi}{153}+\frac7{20}
                         <\frac{123}{100}.
 \tag{10}
\]
The last comparison uses \(\pi>25/8\):
\[
 \frac76+\frac7{20}+\frac{49}{1250}-\frac{50}{153}
                <\frac{123}{100}
 \quad\Longleftrightarrow\quad
 \frac{50}{153}>\frac{611}{1875},
 \tag{11}
\]
and its integer witness is \(93750>93483\).

## 3. An exact finite inner-current envelope

Keep the original two-short-edge Hermite current on the fixed line
\(\gamma_h=[-\pi/2,2\pi/3]-ih\):
\[
 \begin{gathered}
 U_N=\lfloor N/2\rfloor-1,\quad
 \eta_N=(-1)^{N-1},\quad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2},\\
 C_{N,n}=e^{n\pi i(N-1)^2/(4N)},\\
 J_{h,N}(u)=-\frac{N^2C_{N,3}}{\pi i}
 \int_{\gamma_h}
 \sin t\,K_N^<(t,0)K_N^<(t,u)
                     e^{3iNt^2/(4\pi)}W_N(t)\,dt .
 \end{gathered}
 \tag{12}
\]
No term is deleted from either shortened kernel. This is a
specified part of a possible full inner contour, not a new
formula for the whole \(Q_N\).

Define the explicit positive geometric maximum
\[
 G_h(u)=\max_{0\le a\le2\pi/3}
       \Re\{\psi(a-ih,0)+\psi(a-ih,u)
                                +3i(a-ih)^2/(4\pi)-i(a-ih)\}.
 \tag{13}
\]
The first-short slit theorem applies to the whole fixed first
line: its ordinary spectral image has real part less than two.
For the second edge the positive wider source covers
\([0,2\pi/3]-ih\), including zero by the outgoing strictness
argument in the signed source. The swapped opposite-height
theorem covers the negative first-angle part. Its reflected
geometric debit bounds that part by (13), and its endpoint
sector is no larger than its reflected positive counterpart.

It follows, with every factor in (12) retained, that for each
fixed \(\tau>0\)
\[
 |J_{h,N}(u)|\le C_\tau\left[
              e^{N(G_h(u)+\tau)}
             +e^{N(123/100+K/2+\tau)}\right].
 \tag{14}
\]
Polynomial trace factors and the fixed path length are absorbed
in \(\tau\). The two terms in (14) are upper bounds for sectors
of a maximum; they are not asserted to be a decomposition of
the finite source into two separately defined currents.

## 4. The outer endpoint budget on a specified hyperbola

Use the oriented right outer path
\[
 u(\beta)=\beta-iK(\beta),\qquad
 K(\beta)=\frac{\pi K_g}{2\beta},\qquad
                         \pi/2\le\beta\le2\pi/3.
 \tag{15}
\]
Its heights satisfy \(3K_g/4\le K(\beta)\le K_g\);
in particular they are greater than \(17/40>1/10\), so
the entire source statement (14) applies. The original outer
crossing \(e^{iNu^2/\pi}\) and full \(W_N(u)\) have combined
rate
\[
                        (2\beta/\pi-1)K.
 \tag{16}
\]
The doubled endpoint sector from (14) consequently has rate
\[
 \begin{split}
 2(123/100+K/2)+(2\beta/\pi-1)K
       &=123/50+2\beta K/\pi\\
       &=123/50+K_g
        <79/25<M_g-1/20 .
 \end{split}
 \tag{17}
\]
The full sampling denominator is uniformly bounded away from
zero on (15); no alias truncation is made. Fixed \(\sin u\),
length and \(N^2C_{N,4}/(\pi i)\) factors cost only a polynomial.
Thus, if (14) is inserted into the outer absolute integral
formed from \(J_{h,N}(u)^2\), the inequality
\((x+y)^2\le2x^2+2y^2\) leaves its endpoint-sector bound
exponentially below \(M_g\), for example by \(1/40\) after
choosing the fixed tolerances small enough.

The surviving geometric-sector bound is explicitly
\[
                   2G_h(u)+(2\beta/\pi-1)K.
 \tag{18}
\]
No estimate below \(M_g\) for (18) is proved here. Nor does
(12) include the center height join, the first-angle low/far
currents, the exact finite trace corrections, or the two
full-to-short edge restoration errors. Replacing the full
inner \(Q_N\) by \(J_{h,N}\) in the original closing is not
authorized by this note. The useful conclusion is the actual
source inequality (14) and the strict endpoint budget (17)
on a fully specified candidate outer path.

## Frozen source bindings

- Positive wider finite edge:
  f3f9cdca2307f100a5766638ae91e329be5c7f372ac9b303ede0a28c9953e22f.
- Signed central source, original phase and reflected debit:
  dea764c87b923f51be906688369da2fed794d376cb11469522f98983559d63c8.
- First-short slit bound:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Exact first-edge derivatives and cubic current:
  7ba93b34b12765ebdfec7853ffc1e7e77bc370e07770c9088f59e538785af908.
- Complete action floor and height series:
  fa1224123389462fd7e29199f1045d0892c167225b4dd6f79ea5bd967a583795.
- Actual horizontal maximum:
  f7890776761cf7d59e015617b9daf89a240d0b57b1bd51c86ee1e03000782a0b.
- Actual geometric height localization:
  6bf4646f6ec7b48dcbdbacfaacbe14ecb864c9d049114d3bd7c1b95fb66cc6f0.
