# The shortened wire kernel at the two-power saddle

Private written proof, 16 November 2026.

The complete-output saddle for power two lies outside the half-plane
used by the physical-row theorem. The original shortened Newton sum
nevertheless has a nonzero local Gaussian coefficient there. A ray in
the tangent coordinate proves this directly. One factorial argument
has crossed into the upper continuation of the negative half-plane;
its exact reciprocal reflection retains the normalization.

This is a local wire and local trace result. It does not bound the
whole decorated two-power trace. In particular it does not discard
the remaining fold currents.

## 1. The source and the selected point

Put \(q=e^{\pi i/N}\), \(D=N-1\), \(\eta=(-1)^D\), and
\[
 c_j=2\cos((2j+1)\pi/N),\qquad
 S_j=\prod_{\ell=1}^j2\sin(\pi\ell/N),\qquad
 e_j(C)=S_j^{-2}\prod_{\ell<j}(c_\ell-C).
 \tag{1}
\]
We use precisely the shortened kernel
\[
 K_N^<(-2\cos t,-2\cos u)
   =\sum_{j<\lfloor N/2\rfloor}
                    e_j(-2\cos t)e_j(-2\cos u).
 \tag{2}
\]
The full original kernel has additional terms. They are not included
in the off-grid assertion below.

Let \(t_2=a-iH\), \(0<a<\pi\), \(H>0\), be the calibrated terminal
saddle for power two. Its equation and selected root are
\[
 \operatorname{asinh}(\tan(t_2/2))=it_2-i\pi,\qquad
 k=\cos(t_2/2)=\frac{1+i}{2},\qquad A=k^2=\frac i2.
 \tag{3}
\]
Indeed taking the hyperbolic sine of the first equation gives
\(\tan(t_2/2)=-i\sin t_2\), hence \(k^2=i/2\).
The first-quadrant root is the original selected branch.
Its color is \(2-2i\); no assertion valid only for \(\Re C<2\)
is applied at this point.

Retain the original factorial phase
\[
 J'(y)=\operatorname{Log}(2\sin\pi y),\qquad J(0)=0,
\]
\[
 b(y,t)=-J(1/2-y+t/(2\pi))-J(1/2-y-t/(2\pi))-2J(y),
 \qquad F(y;t,u)=b(y,t)+b(y,u).
 \tag{4}
\]
Branches are continued from the original positive factorial strip.
In the upper negative half-plane,
\[
 J_+(w)=-J(-w)+i\pi w.
 \tag{5}
\]
Write \(y_*(t,u)\) for the selected wire critical point,
\(\psi(t,u)=F(y_*;t,u)\), and
\[
 a_e(t,u)=
 \frac{\sqrt{2\pi}}
      {4\sin^2(\pi y_*)\sqrt{-F_{yy}(y_*;t,u)}}.
 \tag{6}
\]
The square root follows the oriented ray in the proof. This is the
same absolute phase and amplitude as in the free-boundary wire
source, continued without changing the logarithmic lift.

**Theorem 1.** On a fixed complex neighborhood of \((t_2,0)\),
at both parities,
\[
 K_N^<(-2\cos t,-2\cos u)
  =N^{-3/2}a_e(t,u)e^{N\psi(t,u)}
                         [1+O_{\rm hol}(N^{-1})],
 \qquad a_e(t,u)\ne0.
 \tag{7}
\]
The assertion includes all fixed derivatives on smaller
neighborhoods. It is even in \(u\) and therefore descends to a fixed
ordinary output-color neighborhood of \(-2\).
The conjugate assertion holds at the negative-power saddle
\(\overline{t_2}\).

## 2. A strict ray maximum at \(A=i/2\)

At \(u=0\), put \(z=\tan(\pi y)\). The exact phase derivative is
\[
 e^{F_y}=\frac{A-(1-A)z^2}{z^4}.
 \tag{8}
\]
On the oriented ray \(z=kr\), \(0<r<\infty\), set \(v=r^2\).
Then
\[
 y=\pi^{-1}\arctan(kr),\qquad
 F_r=\frac{k}{\pi(1+Av)}\operatorname{Log}R,\qquad
 R=\frac1v+\frac{2i(v-1)}{v^2}.
 \tag{9}
\]
The chosen logarithm tends to zero at \(r=1\).
The tangent in (9) has positive real part; the sign of its
imaginary part is the sign of \(2-v\).

For \(0<v<1\), \(\Re R=1/v>1\) and \(\Im R<0\).
The tangent has positive imaginary part, so \(\Re F_r>0\).
For \(v>1\), \(\Im R>0\) and \(|R|<1\), since
\[
 v^4-v^2-4(v-1)^2
 =(v-1)(v^3+v^2-4v+4)>0.
 \tag{10}
\]
The cubic on the right has value \(2\) at \(1\) and positive
derivative for \(v\ge1\). For \(1<v\le2\) both terms in the real
part of (9) are therefore nonpositive, with a strict negative
real-log term.

It remains to consider \(v>2\), where the tangent has negative
imaginary part. Put \(b=2-2/v\), so \(1<b<2\). The required
inequality is
\[
 f(b):=
 \log\frac{2}{(2-b)\sqrt{1+b^2}}
       -\frac{b-1}{3-b}\arctan b>0.
 \tag{11}
\]
Here the first term is \(-\log|R|\), and the coefficient in
the second is the absolute imaginary-to-real tangent ratio.
We have \(f(1)=\tfrac12\log2>0\).
Concavity of \(\arctan\) on \([1,2]\), and \(\pi<16/5\), give
\[
 \arctan b\le\frac{\pi}{4}+\frac{b-1}{2}
                      <\frac b2+\frac3{10}.
 \tag{12}
\]
Direct differentiation gives
\[
 f'(b)=\frac1{2-b}
 -\frac{4b-b^2-1}{(3-b)(1+b^2)}
 -\frac{2\arctan b}{(3-b)^2}.
 \tag{13}
\]
After (12), a lower bound has denominator
\(5(2-b)(3-b)^2(1+b^2)>0\) and numerator
\[
 15b^4-82b^3+184b^2-182b+69
   =15x^4-22x^3+28x^2+4,\qquad x=b-1.
 \tag{14}
\]
This is positive: \(15x^2-22x+28\) has negative discriminant
and positive leading coefficient, so the right side is
\(x^2(15x^2-22x+28)+4>0\).
Thus \(f'>0\), proving (11) and \(\Re F_r<0\) for all \(r>1\).

The ray has exactly one strict maximum, at \(r=1\). There
\[
 F_{rr}(1)=-\frac2{\pi k},\qquad
 F_{yy}(y_*;t_2,0)=-\frac{2\pi(1+A)^2}{k^3}.
 \tag{15}
\]
The real part of \(2/(\pi k)\) is positive. Hence the oriented
Gaussian is nondegenerate and has the coefficient in (6).

## 3. The reflected ray and factorial branches

Write the ray as \(y=x+i\omega(x)\), \(0<x<1/2\). Since
\(\arg k=\pi/4\),
\[
 \sinh(2\pi\omega(x))=\sin(2\pi x).
 \tag{16}
\]
For \(0\le v\le\omega(x)\), define
\[
 R_v=\cos(2\pi x)\cosh(2\pi v)-1,\qquad
 B_v=\sin(2\pi x)\sinh(2\pi v).
 \tag{17}
\]
We have \(0\le B_v\le1\), with equality only at
\(x=1/4,\ v=\omega(1/4)\). At that point \(R_v=-1\).
In particular neither \(R_v+i(1+B_v)\) nor
\(R_v+i(1-B_v)\) vanishes. The latter can reach the
negative real axis, but its continued argument there is
\(\pi\), not a reset to \(-\pi\).

For the original reflected action difference
\[
 D_x(v)=\Re F(x-iv;t_2,0)-\Re F(x+iv;t_2,0),
\]
the exact derivative formula from the wire source is
\[
 D_x'(v)=
 \arg[R_v+i(1+B_v)]+\arg[R_v+i(1-B_v)]<2\pi.
 \tag{18}
\]
The first argument is strictly between \(0\) and \(\pi\);
the second is in that interval or equals \(\pi\) at the
single boundary point just described. There is no winding.
Since \(D_x(0)=0\), the reflected lower ray with its original
cotangent penalty has a strictly smaller rate than the upper
ray. All nonconstant upper cotangent terms also have the
strict penalty \(2\pi\omega(x)\). These gaps are uniform
on compact subarcs away from the endpoints.

The potentially reflected factorial has argument
\[
 w_-=1/2-y-t_2/(2\pi).
 \tag{19}
\]
It stays strictly in the upper half-plane throughout the
region between the rays. Indeed \(\cos t_2=-1+i\) gives
\[
 \sinh^2 H=\frac{1+\sqrt5}{2}>1,
 \qquad H>\operatorname{asinh}1
                 =2\pi\max_x\omega(x).
 \tag{20}
\]
To check the first identity, use
\(\cos a\cosh H=-1\), \(\sin a\sinh H=1\), and
\(\cos^2a+\sin^2a=1\).
Thus \(\Im w_-=H/(2\pi)-\Im y>0\).
The other shifted argument \(1/2-y+t_2/(2\pi)\)
has positive real part. Both scaled real parts remain in
a compact subinterval of \((-1,1)\) after fixed endpoint
cuts are chosen.

When \(w_-\) has negative real part, use the exact identity
\[
 \frac1{G_N(Nw_--1/2)}
 =\frac{e^{-i\pi Nw_-}}{N}
       (1+e^{2\pi iNw_-})G_N(-Nw_--1/2).
 \tag{21}
\]
Both terms are retained in upper bounds. On a compact
saddle neighborhood \(\Im w_->0\) is bounded away from zero.
The midpoint factorial expansion then gives
\[
 \frac1{G_N(Nw_--1/2)}
  =N^{-1/2}e^{-NJ_+(w_-)}
                        [1+O_{\rm hol}(N^{-1})].
 \tag{22}
\]
Its leading scalar is exactly one: the numerator factorial
in (21) is \(\sqrt N e^{NJ(-w_-)}[1+O(N^{-1})]\),
and the second exponential in its parentheses is smaller.
The same formula on the positive side follows directly
from the midpoint expansion. The two continuations agree.
No additional phase or guessed constant is introduced.

## 4. Recovering the actual finite shortened sum

The exact interpolation of each Newton factor is
\[
 \mathcal E_N(y,t)=
 \frac{N}{
 G_N(N(1/2-y+t/(2\pi))-1/2)
 G_N(N(1/2-y-t/(2\pi))-1/2)G_N(Ny)^2}.
 \tag{23}
\]
It equals \(e_j(-2\cos t)\) at \(y=j/N\) as an ordinary
identity, not merely on physical colors.
The reciprocal factorial zeros introduce no poles in the
region between the truncated rays. Near the saddle, (22)
and the remaining ordinary factorial expansions give
\[
 \mathcal E_N(y,t)\mathcal E_N(y,u)
   =\frac{e^{NF(y;t,u)}}{4N^2\sin^2(\pi y)}
                         [1+O_{\rm hol}(N^{-1})].
 \tag{24}
\]
This proves the same amplitude as on the old ray domain,
including when (19) has negative real part.

The endpoint values of the continued phase are
\[
 F(0;t_2,0)=0,\qquad F(1/2;t_2,0)=it_2/2.
 \tag{25}
\]
The strict increase and decrease in Section 2 imply that
both real endpoint rates are strictly smaller than the
maximum \(\Re\psi(t_2,0)\). No comparison of \(H\) with
the full radical rate is required.
Choose fixed cuts near \(0\) and \(1/2\), shifted by
\(O(N^{-1})\) to sampling midpoints.
The small endpoint arcs, the vertical connectors, and
the omitted real index intervals preserve these gaps.
The exact midpoint factorial bounds apply even when an
argument crosses zero or a reciprocal factorial vanishes.

Enclose precisely the retained integer indices by
\(\pi N\cot(\pi Ny)\). Its constant upper and lower terms
combine to \(+N\) times the oriented wire integral.
Section 3 bounds every nonconstant cotangent term, and
the endpoint gaps bound every connector and omitted
finite sum. Gaussian integration in the real parameter
\(r\) at \(1\) now proves (7) at \(u=0,t=t_2\).

All gaps are strict on fixed compact contour pieces.
The exact upper factorial exponent is continuous on the
remaining faces, and the arguments in Section 3 stay
nonzero. The contour and its local saddle therefore
continue to a fixed complex neighborhood of \((t_2,0)\).
Deforming a small segment through the moving saddle
proves the uniform holomorphic assertion (7).
Buffered Cauchy estimates retain every fixed derivative.

At odd \(N=2m+1\), the more usual low sum through \(m\)
contains the extra term \(e_m(-2\cos t)e_m(-2\cos u)\).
The shortened sum (2) ends at \(m-1\).
This difference belongs to the endpoint interval already
bounded, at both parities. No identification of that term
with zero is made.

The phase \(\psi\) is the original one. One explicit
continuation first follows the positive real \(k\)-axis
to \(1/2\), then the segment \(k=1/2+iy\),
\(0\le y\le1/2\). On the real segment the saddle
factorial argument is positive, since
\(\arctan k<\arcsin k\). On the vertical segment write
\(t/2=A_0-iB_0\). Then
\(\cos A_0\cosh B_0=1/2\),
\(y=\sin A_0\sinh B_0\), and
\[
 \frac{\sinh(2B_0)}{\tan(\arg k)}
       =\frac{\cosh B_0}{\sin A_0}>1
       \quad(y>0).
\]
Thus the potentially reflected saddle factorial stays
in the upper half-plane. The selected root \(\arctan k\)
and the other arguments meet no zero. Formula (21)
supplies the continuation when needed.
Thus the original identity
\(\psi(t,0)=\int_0^{1/2}2\operatorname{asinh}
(\cos(t/2)\cot\pi v)\,dv\) keeps its complete constant.
The selected terminal action is the calibrated
\(\mathcal I_2=2G/\pi\), where
\(G=\int_0^{\pi/4}\log(\cot s)\,ds\) is Catalan's constant.

## 5. Consequence for the actual decorated local trace

Fix \(r\) real microscopic parameters in a bounded interval.
Use the sharp physical representatives of the actual
endpoint kernels, with their original bulk anchors.
Near \(t_2\), put
\[
 \mathcal H_N(t)=\prod_{i=1}^r
 H_{i,N}^+\!\left(\frac{\pi-\pi/N-t}{2\pi},\alpha_i\right).
 \tag{26}
\]
The point lies in a fixed designated nonreal compact with
nonzero imaginary part of \(\operatorname{Log}\sin(\pi x)\).
The actual insertion theorem gives
\[
 |\mathcal H_N(t)|\ge cN^{-r},\qquad
 |\partial_t^j\mathcal H_N(t)|
              \le C_j[(1+\log N)/N]^r
 \tag{27}
\]
on a smaller neighborhood. This is uniform for bounded
real parameters, including level-dependent choices.

For \(n=2\sigma\), \(\sigma=\pm1\), the exact favored local
trace has prefactor \(\sigma iN^2/\pi\), the original carrier
\(\mathfrak c_{N,n}=e^{\pi i nD^2/(4N)}\), and rational factor
\[
 \frac{e^{-i\sigma Nt}}{(1-\eta e^{-i\sigma Nt})^2}.
 \tag{28}
\]
These follow from the original full-normal residue formula,
with its signed horizontal orientation. They are independent
of the half-plane estimate formerly used for the wire.
At the fixed saddle height all nonleading terms in (28)
are exponentially smaller.

Let \(t_n(u)\) solve
\[
 \psi_t(t_n(u),u)+\frac{in}{2\pi}t_n(u)-i\sigma=0
 \tag{29}
\]
near \(t_2\) or its conjugate, and put
\[
 W_n(u)=\psi(t_n(u),u)+\frac{in}{4\pi}t_n(u)^2-i\sigma t_n(u),
 \qquad
 \lambda_n(u)=-\psi_{tt}(t_n(u),u)-\frac{in}{2\pi}.
 \tag{30}
\]
For positive power,
\(\lambda_2(0)=(1-3i)/(2\pi)\), so its real part is positive.
This follows from
\(\psi_{tt}(t,0)=-1/(2\pi\cos(t/2))\).
The negative case is the conjugate.

The paired favored local integrals, with the original mirror
half-normalization, consequently equal
\[
 \mathfrak c_{N,n} e^{NW_n(u)}
 \frac{\sigma i}{\pi}\sin t_n(u)\,
 a_e(t_n(u),u)\sqrt{\frac{2\pi}{\lambda_n(u)}}\,
 \mathcal H_N(t_n(u))
       [1+O((1+\log N)^{r+1}/\sqrt N)].
 \tag{31}
\]
For negative power use the conjugate designated representatives
in (26). This formula is uniform on a fixed complex output
neighborhood and for bounded real microscopic parameters.
To justify the relative error directly, divide the insertion
by its nonzero saddle value. Its variation is
\(O((1+\log N)^r|t-t_n(u)|)\) by (27).
The nondegenerate Gaussian integrates this variation with
relative error \(O((1+\log N)^r/\sqrt N)\).
The wire error in (7) is \(O(N^{-1})\), and all rational
aliases in (28) retain their exponential loss.
The three powers \(N^2,N^{-3/2},N^{-1/2}\) cancel.
Every displayed leading factor is nonzero.

This proves an actual nonzero local coefficient for the
decorated powers \(2\) and \(-2\).
It does not prove that the other pieces of the original
trace cannot cancel it. In particular no fixed positive
gap is available from the older two-power fold estimate.
The actual cap error and all adjacent seams must still
be assembled with their precise prefactors.

## 6. Complete direct sources

The complete sources below were read at the stated matching
pins. The new steps are the ray inequality (11)--(14),
the critical reflected-alias check, and the explicit
normalization (22) across the reflected factorial.

* [Original free-boundary wire contour](research_pair_free_boundary_kernel.md),
  SHA256 e62ae0c2701388a7e9bf3ad171d7005b845098542e48dffb1a36c4bc95ee745f.
* [Uniform midpoint factorial bounds](research_uniform_factorial_and_boundary_decay.md),
  SHA256 4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11.
* [Specified factorial and its bulk expansion](exact_factorial_interpolation_and_complex_contours.md),
  SHA256 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72.
* [Absolute terminal action calibration](research_terminal_characteristic_action_calibration.md),
  SHA256 582c359817b69b0dd1094e49878d15917230e86f6e7831fe448ea4aacee8a1fd.
* [Actual nonreal microscopic insertion](research_endpoint_nonreal_insertion_lower_bound.md),
  SHA256 ab3b4687b53c2168d22342c0e822b243a563f716d2a7a0de18d87c372546d7d0.
* [Signed local trace and relative Gaussian calculation](research_shortened_endpoint_decorated_local_gaussian.md),
  SHA256 8e65d3885c88ea358e6c14fab59d9b1c825cc5e2d6a7a14f9a57e8c0810ab109.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build or
compilation was run. Existing adopted and public notes are unchanged.
