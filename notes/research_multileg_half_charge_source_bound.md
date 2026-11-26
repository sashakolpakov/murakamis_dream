# The original multi-leg half-charge coupon

Private written proof, 17 November 2026.

One original middle Newton factor at a traced vertex admits a
whole-outside-period bound at every fixed integer power and every
positive degree. Except for the elementary zero-power one-leg
case, its complete-outside value has a nonzero half-charge
Gaussian. The source is the literal middle factor, not a
continuous-charge replacement or a discarded normal.

The complete-neighbor cone geometry is already in [G]. The new
contour argument uses the coherent low complete-end polynomial
from [E,R], including when the full even-level off-grid kernel
has a larger radical contribution. That contribution is contracted
exactly before it is estimated.

## 1. Source and assertions

Fix integers \(r\ge1\) and \(n\in\mathbb Z\) before letting
the level \(N\ge2\) tend to infinity. Write
\[
 D=N-1,\quad m=\lfloor N/2\rfloor,\quad L=D-m,\quad
 q=e^{\pi i/N},\quad \eta=(-1)^D,\quad \epsilon_N=(-1)^m,
\]
\[
 s_j=2\sin(j\pi/N),\quad S_j=\prod_{a=1}^js_a,\quad
 c_a=2\cos((2a+1)\pi/N),\quad
 e_j(z)=S_j^{-2}\prod_{a<j}(c_a-z).
 \tag{1}
\]
The original algebra, trace, crossing and kernels are
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f,
\]
\[
 R(c_a)=q^{D^2/2}(-1)^a q^{a(a+1)},\qquad
 \chi_N=q^{D^2/4},\qquad A=e_L,\quad B=e_{L+1},
\]
\[
 K_N(z,\zeta)=\sum_{j=0}^De_j(z)e_j(\zeta),\qquad
 K_N^{\rm low}(z,\zeta)=\sum_{j=0}^Le_j(z)e_j(\zeta).
 \tag{2}
\]
All crossing powers use the full physical Hermite algebra.
Only the traced variable is reduced. Define the ordinary
outside polynomial
\[
 \mathcal C_{r,n,N}(\boldsymbol\zeta)
 =\phi_N^{(z)}
   \left[R(z)^n A(z)\prod_{i=1}^rK_N(z,\zeta_i)\right].
 \tag{3}
\]
Let \(\Psi(t)=\psi(t,0)\) have its original complete normalization:
\[
 \Psi(0)=M_\infty=\frac{4G}{\pi},\qquad
 \Psi'(t)=-\frac1\pi\operatorname{asinh}\tan(t/2),\qquad
 \Psi''(t)=-\frac{\sec(t/2)}{2\pi}.
 \tag{4}
\]
Here \(G\) is Catalan's constant. Branches continue from zero in
\(|\Re t|<\pi\). For \(r+|n|>1\), put
\[
 nt_*+2ir\operatorname{asinh}\tan(t_*/2)=\pi,\qquad
 \Im t_*<0,\quad |\Re t_*|<\pi,
\]
\[
 S(t)=r\Psi(t)+\frac{int^2}{4\pi}-\frac{it}{2},\qquad
 \mathcal S_{r,n}=S(t_*),\quad M_{r,n}=\Re\mathcal S_{r,n},\quad
 \mathfrak A=\frac{r\sec(t_*/2)-in}{2\pi}.
 \tag{5}
\]
The construction below fixes this unique complete cone branch;
\(\Re\mathfrak A>0\), and its square root has positive real part.

**Theorem.** The following statements concern the exact source (3).
Assume \(r+|n|>1\) through (10a); the remaining case is (11).

1. Its degree in each separate ordinary outside variable is at
   most \(m\). If \(r+|n|>1\), then for each fixed multi-index
   \(\alpha\), some \(C_\alpha,a_\alpha\) satisfy
   \[
   \left|\partial_{\boldsymbol\zeta}^{\alpha}
       \mathcal C_{r,n,N}(\boldsymbol\zeta)\right|
   \le C_\alpha N^{a_\alpha}
      \exp\left\{NM_{r,n}
                  +m\sum_{i=1}^r|\Im u_i|\right\},
   \qquad \zeta_i=-2\cos u_i,\quad u_i\in\mathbb C.
   \tag{6}
   \]
   In particular this is a bound on the whole real outside cube,
   including its ordinary endpoint normals.
2. At the complete outside assignment, through both parities,
   \[
   \mathcal C_{r,n,N}(-2,\ldots,-2)
   =\chi_N^n
     \frac{\sqrt{2\pi N}}{\pi\sqrt{\mathfrak A}}\,
     b_N(t_*)\,
     \exp\{N\mathcal S_{r,n}+rE_N(t_*)\}(1+o(1)),
   \tag{7}
   \]
   where
   \[
   b_N(t)=
   \begin{cases}
     \cos(t/2),&N\ {\rm odd},\\
     \displaystyle\frac{2i\sin t}{c_*+2\cos t},
        &N\ {\rm even},\qquad c_*=-2\cos(\pi/N),
   \end{cases}
   \tag{8}
   \]
   and \(E_N\) is the exact holomorphic logarithmic error
   \[
   K_N^{\rm low}(-2\cos t,-2)
                    =\exp\{N\Psi(t)+E_N(t)\}.
   \tag{9}
   \]
   On the fixed contour neighborhood used below, every fixed
   derivative of \(E_N\) is \(O(\log N)\). All factors displayed
   in (7) are nonzero, and the factor outside
   \(e^{N\mathcal S_{r,n}}\) has upper and lower polynomial
   bounds. Consequently the complete coupon is nonzero for
   all sufficiently large levels and has rate \(M_{r,n}\).
3. There are \(c,C,a>0\) such that at physical outside colors,
   with \(\tau_b=\arccos(-c_b/2)\in[0,\pi]\),
   \[
   |\mathcal C_{r,n,N}(c_{b_1},\ldots,c_{b_r})|
   \le CN^a
      \exp\left\{N\left[M_{r,n}
             -c\sum_i(1-\cos\tau_{b_i})\right]\right\}.
   \tag{10}
   \]
   This last assertion is a sampled **value** bound. Its
   angular loss is not asserted in differentiated slots.

There is also a mixed-jet consequence with a precise loss
of angular information in every differentiated slot.
After decreasing \(c>0\), for every fixed multi-index
\(\alpha\),
\[
 \left|(\partial^\alpha\mathcal C_{r,n,N})
                 (c_{b_1},\ldots,c_{b_r})\right|
 \le C_\alpha N^{a_\alpha}
   \exp\left\{N\left[M_{r,n}
      -c\sum_{j:\alpha_j=0}(1-\cos\tau_{b_j})\right]\right\}.
 \tag{10a}
\]
Only the undifferentiated physical slots keep the Gaussian
loss. The proof uses finite interpolation, not differentiation
of (10).

The exceptional \(r=1,n=0\) is exactly
\[
 \mathcal C_{1,0,N}(\zeta)=e_m(\zeta),\qquad
 e_m(-2)=
 \begin{cases}1,&N\ {\rm odd},\\1/N,&N\ {\rm even}.\end{cases}
 \tag{11}
\]
It satisfies (6) with \(M_{1,0}\) replaced by zero, but no
half-charge saddle or formula (7) is assigned to it.

## 2. Exact low source, normal adapter and high correction

Write \(\mathcal C^{\rm low}\) for (3) with all kernels low.
The source identities in [C] give
\[
 \mathcal C_{r,n,N}=
 \begin{cases}
  \mathcal C^{\rm low}_{r,n,N},&N\ {\rm odd},\\
  \displaystyle\mathcal C^{\rm low}_{r,n,N}
   +R(c_*)^n\sum_{i=1}^r B(\zeta_i)
       \prod_{j\ne i}F_{J,N}(\zeta_j),&N\ {\rm even},
 \end{cases}
 \quad J=m-1,\quad F_{J,N}(\zeta)=K_N(c_*,\zeta).
 \tag{12}
\]
Indeed products of two high factors vanish in the traced
algebra. At odd levels \(A\) kills each high factor. At even
levels it kills all of them except \(e_m=B\), and
\(\phi_N(R^nABf)=R(c_*)^nf(c_*)\). At a physical selected
value the low and full kernels agree. These facts prove (12)
coefficientwise with arbitrary ordinary outside variables.
Since \(L=m\) odd and \(L=m-1\) even, (12) proves the degree
bound in the theorem.

For either low or full product \(f_N(z;\boldsymbol\zeta)\),
put
\[
 h(z)=e^{inN\arccos(-z/2)^2/(4\pi)}f_N(z;\boldsymbol\zeta).
 \tag{13}
\]
The squared inverse cosine is holomorphic on
\(\mathbb C\setminus[2,\infty)\), including \(-2\).
Let \(I\) be its ordinary interpolant at all distinct physical
nodes. Its degree is at most \(m\) odd and less than \(m\)
even. At even levels set
\[
 Q_{\rm e}(z)=2T_m(z/2),\qquad
 \mathscr D(z)=\frac{h(z)-I(z)}{Q_{\rm e}(z)}.
 \tag{14}
\]
At odd levels put
\[
 Q_{\rm o}(z)=(z+2)\{U_m(z/2)-U_{m-1}(z/2)\}.
 \tag{15}
\]
The exact coupon adapter is
\[
 \phi_N(R^nAf_N)=
 \begin{cases}
  \epsilon_N N\chi_N^n[z^m]I(z),&N\ {\rm odd},\\
  2N\epsilon_N\chi_N^n\mathscr D(c_*),&N\ {\rm even}.
 \end{cases}
 \tag{16}
\]
To verify the carrier, if
\(t_a=\pi-(2a+1)\pi/N\), direct expansion gives
\[
 R(c_a)^n=\chi_N^n e^{inNt_a^2/(4\pi)}.
 \tag{17}
\]
The Frobenius identity \(\phi_N(e_i e_j)=\mathbf1_{i+j=D}\)
makes multiplication by \(A\) select the Newton coefficient
at index \(m\). At odd levels its first \(m+1\) nodes are
distinct and \(e_m\) has leading coefficient
\((-1)^m/N\). At even levels its next node repeats \(c_*\), and
\[
 e_m(z)=\frac{(-1)^m}{2N}Q_{\rm e}(z),\qquad
 \partial_z\log e^{inN\arccos(-z/2)^2/(4\pi)}
                 \big|_{c_*}=\frac{in}{2s_1}.
 \tag{18}
\]
The latter is the original crossing normal. Confluent divided
differences therefore give exactly (16), including negative
powers and \(N=2\). All ordinary outside derivatives commute
with these identities.

At complete outside colors the even correction in (12) is
\[
                 \frac rN R(c_*)^nF_{J,N}(-2)^{r-1},
 \tag{19}
\]
since \(B(-2)=1/N\). On the real outside cube it has size at
most a polynomial times \(e^{N(r-1)M_\infty}\): [C] bounds
the real radical \(B\) polynomially, and [F] gives
\(|F_{J,N}(\zeta)|\le F_{J,N}(-2)\) there; [R] fixes the
latter rate at \(M_\infty\).

## 3. The complete half-charge geometry and its action

It suffices first to take \(n\ge0\). The cone equation is
\[
 nt+2ir\operatorname{asinh}\tan(t/2)=2\pi\lambda,
                   \qquad 0<\lambda\le\tfrac12.
 \tag{20}
\]
Here is the complete-branch construction from [G], with the
charge interval made explicit. For \(n>0\), write
\(t=2a-2ib\), \(0<a<\pi/2\), \(b>0\). The principal return is
\[
 \operatorname{asinh}\tan(a-ib)=A_0-iB_0,\quad
 A_0=\operatorname{artanh}\frac{\sin a}{\cosh b},\quad
 B_0=\arctan\frac{\sinh b}{\cos a}.
 \tag{21}
\]
Thus
\[
 nb=rA_0,\qquad na+rB_0=\pi\lambda.
 \tag{22}
\]
At fixed \(a\), the equation
\(\sin a=\cosh b\tanh(nb/r)\) has exactly one positive
solution \(b(a)\), strictly increasing in \(a\). The second
left side in (22) then increases from zero to
\((n+r)\pi/2\). This proves existence and uniqueness precisely
when \(0<\lambda<(n+r)/2\). For \(n=0\),
\[
 t(\lambda)=-2i\operatorname{asinh}
                       \tan(\pi\lambda/r),\qquad \lambda<r/2.
 \tag{23}
\]
Negative powers use \(t_{r,-n}=-\overline{t_{r,n}}\).
There is no negative-real solution when \(n>0\), since the
first equation in (22) would have \(nb>0\) and \(A_0<0\).
For \(n=0\) it forces \(a=0\).
The original shapes in [G] are
\((iR_0,iw,i/R_0,i/w)\) and
\((i/R_0,iw,iR_0,i/w)\), where
\(w=e^{it/2}\) and \(R_0=\sec(t/2)+\tan(t/2)\).
Both \(w\) and \(R_0\) have positive real part on the branch,
as do their reciprocals. Thus every shape is positive.
The same continued peripheral computation in [G] gives
period \(-2\pi i\lambda\).
At \(\lambda=1/2\) this is the marked cone angle \(\pi\),
not a new assertion about a unit-charge filled manifold.

The Hessian is
\[
 S''(t)=\frac{-r\sec(t/2)+in}{2\pi}.
 \tag{24}
\]
Since \(\Re\sec(t/2)>0\) for \(|\Re t|<\pi\), it never
vanishes. Let \(H(\lambda)=-\Im t(\lambda)\) and
\(\Delta_{r,n}=rM_\infty-M_{r,n}\). Differentiating the
stationary value gives
\[
 \Delta_{r,n}=\int_0^{1/2}H(\lambda)\,d\lambda,\qquad
 \partial_n M_{r,n}
       =\frac{(\Re t_*)H(1/2)}{2\pi}>0\quad(n>0).
 \tag{25}
\]
For \(r\ge2\), (22) implies
\[
 H(\lambda)\le2\operatorname{asinh}\tan(\pi\lambda/r)
                            \le2\operatorname{asinh}1.
 \tag{26}
\]
For \(r=1,n\ge2\), \(a<\pi\lambda/n\) and
\(A_0<\operatorname{asinh}\tan a\), giving
\[
 H(\lambda)<\frac2n\operatorname{asinh}
                                    \tan(\pi\lambda/n)
                             \le\operatorname{asinh}1.
 \tag{27}
\]
For \(r=n=1\) the exact solution is
\[
 t(\lambda)=\pi\lambda
              -2i\operatorname{asinh}\sin(\pi\lambda/2).
 \tag{28}
\]
This follows by setting \(a=\pi\lambda/2\),
\(\sinh b=\sin a\), so \(A_0=b\), \(B_0=a\).
It also satisfies the bound in (26). Consequently, at every
integer pair under consideration,
\[
 M_{r,n}-(r-1)M_\infty
       \ge M_\infty-\operatorname{asinh}1>0.
 \tag{29}
\]
For the strict last inequality, \(\sinh1>1\) and
\(M_\infty>112/99>1\); the latter follows from
\(G>8/9\) and \(\pi<22/7\). The bound is independent of the
fixed pair, although subsequent contour constants may depend
on that pair.

## 4. Rectangles with all complementary rates strictly smaller

We construct \(T\in(0,\pi)\) such that, writing \(t_*=a_*-iH_*\),
\[
 |a_*|<T,\qquad r\Psi(T)<M_{r,n},\qquad
 \Re(-2\cos t)<2
   \quad (|\Re t|\le T,\ |\Im t|\le H_*).
 \tag{30}
\]
All inequalities have a fixed margin after slightly enlarging
the rectangle as needed for analytic estimates.

For \(r\ge2\), \(a_*<\pi/2\). To see this for \(n=1\),
at half-angle \(a=\pi/4\) the equation \(b=rA_0\)
has \(b\) at least its \(r=1\) value; hence
\(B_0\ge\pi/4\) and \(a+rB_0>\pi/2\).
For \(n\ge2\), \(na\ge\pi/2\) there already. Monotonicity
in (22) proves the assertion. At \(n=0\), \(a_*=0\).
By (23)--(25),
\[
 \Delta_{r,n}\le\Delta_{r,0}
   =\frac{2r}{\pi}\int_0^{\pi/(2r)}
                         \operatorname{asinh}\tan y\,dy
   \le r\{M_\infty-\Psi(\pi/2)\}.
 \tag{31}
\]
Equality in the last comparison and in the action comparison
occurs only at \(r=2,n=0\). Thus \(T=\pi/2\) works except
there. In that case increase \(T\) slightly:
\(\Psi\) is strictly decreasing on \((0,\pi)\), while the
color rectangle has \(\Re(-2\cos t)\le0\) at \(T=\pi/2\).

For \(r=1,n\ge2\), integrate (27) at \(n=2\) to obtain
strictly
\(\Delta_{1,2}<M_\infty-\Psi(\pi/2)\).
Monotonicity in \(n\) gives the same strict comparison for
all \(n\ge2\), and \(a_*<\pi/2\). Again take \(T=\pi/2\).

It remains to treat \(r=n=1\). Formula (28) gives
\[
 a_*=\pi/2,\qquad \cosh H_*=2,\qquad
 \Delta_{1,1}
   =\frac4\pi\int_0^{\pi/4}\operatorname{asinh}(\sin y)\,dy
   \le\frac4\pi(1-1/\sqrt2).
 \tag{32}
\]
Since \(\sec y\ge1+y^2/2\) on \([0,\pi/3]\),
\[
 M_\infty-\Psi(2\pi/3)
   =\frac2\pi\int_0^{\pi/3}\operatorname{asinh}\tan y\,dy
   \ge\frac\pi9+\frac{\pi^3}{972}
   >\frac{113}{300}>\frac{5800}{15543}
   >\frac4\pi(1-1/\sqrt2).
 \tag{33}
\]
For the last rational comparisons one may use
\(\pi>157/50\), \(\sqrt2<99/70\);
\(113\cdot15543>5800\cdot300\).
The secant inequality follows by integrating
\(\sec''y=\sec y(1+2\tan^2y)\ge1\) twice.
Choose \(T<2\pi/3\) sufficiently close to \(2\pi/3\).
Then \(\Psi(T)<M_{1,1}\), \(T>a_*\), and
\(-2\cos T\cosh H_*<2\), proving (30).

Finally, on each fixed-height horizontal line and each fixed
real-part vertical line,
\[
 \partial_a^2\Re S(a-ih)
       =-\frac r{2\pi}\Re\sec((a-ih)/2)<0,\qquad
 \partial_h^2\Re S(a-ih)>0.
 \tag{34}
\]
The lower horizontal side has its unique maximum at \(t_*\).
Every vertical side is bounded by the larger of its two
endpoint rates: \(r\Psi(T)\) at height zero, and its strictly
smaller horizontal corner rate at height \(H_*\).
Thus every vertical connector and every horizontal part away
from \(t_*\) has a fixed strict gap. Reflection handles the
upper sides and negative powers. This argument uses convexity
on the vertical sides, not a sign for their first derivatives.

## 5. The actual observation contours and the complete Gaussian

Use the low product in (13). Let \(Q=Q_{\rm e}\) or \(Q_{\rm o}\)
and define the exact distinct-node observation
\[
 \mathcal O(w)=\sum_a
       \frac{Nh(c_a)}{Q'(c_a)(w-c_a)}=\frac{NI(w)}{Q(w)}.
 \tag{35}
\]
Choose parity-appropriate midpoint cuts \(T_N=T+O(N^{-1})\):
\(T_N=2k\pi/N\) even, \(T_N=(2k+1)\pi/N\) odd.
Let the angular rectangle have heights \(\pm H_*\).
The exact Chebyshev identities are
\[
 Q_{\rm e}(-2\cos t)=2\epsilon_N\cos(Nt/2),\qquad
 Q_{\rm o}(-2\cos t)
       =4\epsilon_N\sin(t/2)\sin(Nt/2).
 \tag{36}
\]
Apply the ordinary Cauchy residue formula and
\(dz=2\sin t\,dt\), counting both angular preimages.
The resulting contour has factor \(N/(4\pi i)\).
Its lower and upper sides add because the angular integrand
is odd. The folded lower integrals are exactly
\[
 \mathcal J_{\rm e}(w)=
 \frac{\epsilon_N N}{\pi i}
 \int_{-T_N-iH_*}^{T_N-iH_*}
 \frac{\sin t\, f_N(-2\cos t)\,
                  e^{inNt^2/(4\pi)-iNt/2}}
      {(w+2\cos t)(1+e^{-iNt})}\,dt
       +\text{the paired vertical sides},
 \tag{37}
\]
\[
 \mathcal J_{\rm o}(w)=
 \frac{\epsilon_N N}{\pi}
 \int_{-T_N-iH_*}^{T_N-iH_*}
 \frac{\cos(t/2)\, f_N(-2\cos t)\,
                  e^{inNt^2/(4\pi)-iNt/2}}
      {(w+2\cos t)(1-e^{-iNt})}\,dt
       +\text{the paired vertical sides}.
 \tag{38}
\]
The vertical sides here are the original unfolded contour
pieces with their full sine or cosine denominators. At a
midpoint their reciprocals are bounded by
\(2e^{-N|h|/2}\). No period-defect side is discarded.
At the odd ramified point \(t=0\),
\(Q_{\rm o}(-2\cos t)=\epsilon_NNt^2+O(t^4)\);
the half-double-cover factor gives exactly the single-node
term \(\epsilon_Nh(-2)/(w+2)\) in (35).

Let \(\mathcal T(w)\) be the omitted physical-node sum.
For \(w>2\), \(\mathcal O=\mathcal J+\mathcal T\).
At even levels, continuation to the inside point \(w=c_*\)
retains the evaluation residue and gives exactly
\[
               \mathscr D(c_*)=
                    -\{\mathcal J_{\rm e}(c_*)+\mathcal T(c_*)\}/N.
 \tag{39}
\]
This is holomorphic pole cancellation, so it retains the
actual central normal. At odd levels use
\(\lim_{w\to+\infty}w\mathcal O(w)=N[z^m]I\).

By [R] at odd levels and [E] at even levels, (9) holds on a
fixed neighborhood of the entire color rectangle in (30),
with every fixed logarithmic derivative \(O(\log N)\).
These theorems estimate the actual coherent low polynomial,
not a chosen recurrence solution. The even theorem proves
its relative comparison with the last physical row.

At complete outside colors, \(f_N(-2\cos t)=
\exp\{rN\Psi(t)+rE_N(t)\}\).
Every omitted physical value has rate at most \(r\Psi(T)\):
the original physical ratios imply that \(F_{a,N}(-2)\)
decreases as \(\tau_a\) increases, and the first omitted
value is covered by (9). The observation weights and all
denominators in the required top or central row cost only
powers of \(N\). Equations (30), (34) therefore pay the
whole omitted sum and all vertical sides. The nonconstant
parts of the lower denominators have a fixed exponential
gap because \(H_*>0\).

Near \(t_*\), retain \(e^{rE_N(t_*)}\) exactly. On a
window of radius \(N^{-2/5}\), its ratio to its central
value is \(1+o(1)\), by the logarithmic derivative bound.
The cubic phase error is \(O(N^{-1/5})\); the remaining
Gaussian tails beat every polynomial amplitude ratio.
Since \(\Re\mathfrak A>0\), the oriented horizontal Gaussian
is \(\sqrt{2\pi/N}/\sqrt{\mathfrak A}\), with its nonzero
principal square root. Substituting in (37)--(39) and (16)
gives exactly (7)--(8) for the low coupon. In particular the
even multiplier is
\(-2/ i=2i\), with no unretained crossing carrier.
At \(n=0\), \(t_*=-iH_*\), both parity factors in (8) are
positive; this also checks the orientation.

Their denominators do not vanish: \(t_*\ne0\),
\(|\Re t_*|<\pi\), and \(\Im t_*<0\); thus
\(\sin t_*\ne0\), \(\cos(t_*/2)\ne0\), and
\(c_*+2\cos t_*\) stays separated from zero.
Equation (29) pays (19), so (7) also holds for the full
coupon. Negative \(n\) follows exactly by conjugating
the values and the one central crossing normal in (16):
\(\mathcal C_{r,-n,N}(\boldsymbol\zeta)=
\overline{\mathcal C_{r,n,N}(\overline{\boldsymbol\zeta})}\).
This agrees with the branches in (5)--(8).

## 6. The whole outside cube and its degree continuation

On every fixed compact \(\mathcal W\Subset\{\Re z<2\}\),
[F, Lemma 1] bounds the actual low kernel, for real
\(\zeta\in[-2,2]\), by
\[
 |K_N^{\rm low}(z,\zeta)|
                   \le CN^a e^{N\Re\Psi(\arccos(-z/2))}.
 \tag{40}
\]
Apply this separately to the \(r\) factors on the contour.
The crossing, the denominator and the action remain exactly
those of Sections 4--5. Hence the horizontal integral is at
most a polynomial times \(e^{NM_{r,n}}\), and all vertical
parts have their strict gap uniformly over the real cube.
At an omitted selected physical node, [F, (11)] gives
\[
 |K_N(c_a,\zeta)|\le CN^aF_{a,N}(-2),\qquad -2\le\zeta\le2.
 \tag{41}
\]
The same complete physical-tail gap therefore applies to
the entire product. Formula (39) retains the even normal
without estimating an off-grid derivative by a value.
Finally (12) and (29) bound the full high correction.
This proves (6) on the real cube with \(\alpha=0\).

By the already proved degree bound, tensor Markov
inequalities give every fixed ordinary derivative on that
cube at a polynomial cost. Applying the one-variable
Bernstein ellipse inequality successively in the outside
variables gives, for degree at most \(m\) in each variable,
\[
 |P(-2\cos u_1,\ldots,-2\cos u_r)|
 \le\|P\|_{[-2,2]^r}
                  e^{m\sum_i|\Im u_i|}.
 \tag{42}
\]
One may first apply it with the other variables real and
then repeat; complex coefficients cause no change in the
one-variable inequality. Applying it to each differentiated
coupon proves (6) for all complex angles. No restriction
to a fixed complex strip is needed.

For (11), the Frobenius identity directly gives
\(\phi_N(AK_N)=e_{D-L}=e_m\). Its odd real interval norm
is polynomial, for example by cardinal interpolation from
the values zero at the double nodes and one at \(-2\);
the derivative denominators are those of [F, (3)].
At even levels (18) gives a real interval norm at most
\(1/N\). Markov and (42) prove the stated zero-rate bound.
If a zero-leg scalar is wanted, [C]'s single-\(A\)
observation rows give \(|\phi_N(R^nA)|\le C_nN^{a_n}\)
for every fixed integer \(n\); no zero-leg geometry is used.

## 7. Additional decay at physical outside values

The lower barrier in [R] for the actual physical row ratios
\(\rho_j=F_{j,N}/F_{j-1,N}\), on the contour color compact,
gives
\[
 |\rho_j|\ge1+c(N/2-j)/N
 \quad(\lfloor N/4\rfloor\le j\le J_N),\qquad
 |\rho_j|>1\quad\hbox{at earlier rows},
 \quad J_N=\lfloor(N-1)/2\rfloor.
 \tag{43}
\]
Summing its logarithm backwards from \(J_N\) proves
\[
 \frac{|F_{b,N}(z)|}{|F_{J_N,N}(z)|}
       \le C e^{-c(J_N-b)^2/N}
       \le C e^{-c' N(1-\cos\tau_b)}.
 \tag{44}
\]
For rows before the displayed tail, its tail product already
gives \(e^{-cN}\), which suffices for the second inequality.
At even levels \(\tau_b=(2(J_N-b)+1)\pi/N\); at odd levels
\(\tau_b=2(J_N-b)\pi/N\). These formulas account for the
harmless constant in (44) at the last even row.

At physical outside colors,
\(K_N^{\rm low}(z,c_b)=F_{b,N}(z)\).
The last row in (44) has the same complete logarithmic
profile, by [R,E]. Thus (44) supplies the angular loss
in the entire selected contour integral. The omitted
physical-node sum keeps its complete gap \(\delta>0\)
from Section 5. Since
\(\sum_i(1-\cos\tau_{b_i})\le2r\), shrink \(c'\) if
necessary so that this loss is at most \(\delta/2\);
the omitted sum then satisfies the same upper exponent.
The even correction in (12) vanishes at physical outside
values because \(B(c_b)=0\). This proves (10).

The argument is a value comparison of exact rows. It gives
no right to differentiate the sampled loss. All ordinary
normals are bounded instead by the separate whole-cube
and polynomial-degree argument in Section 6.

To prove the stronger mixed statement (10a), put
\(H_\alpha=\{j:\alpha_j>0\}\) and hold all other slots at
their displayed physical values. At odd levels the coupon
has degree at most \(m\) in each hit slot and there are
\(m+1\) distinct physical nodes. Their cardinal
interpolation has polynomial Lebesgue norm by [F, (3),(7)].
On their tensor grid (10), with the nonnegative hit-slot
loss dropped, therefore extends to the real hit-variable
cube at polynomial cost. Tensor Markov inequalities give
the required ordinary hit derivatives, retaining every
unhit loss.

At even levels apply that argument to
\(\mathcal C^{\rm low}\), whose degree in each slot is
at most \(m-1\), the number of distinct nodes minus one.
Its full physical grid agrees exactly with the full
coupon by (12). The remaining mixed derivative of (12)
has polynomial size at rate \((r-1)M_\infty\):
each differentiated \(B\) is polynomially bounded, and
every fixed derivative of \(F_{J,N}\) is bounded by a
polynomial times \(F_{J,N}(-2)\), using the real norm
and Markov's inequality. A term whose \(B\) slot is not
hit vanishes at that slot's physical value.
Put \(\delta=M_{r,n}-(r-1)M_\infty>0\). Decrease the
constant in (10a) so that \(2rc\le\delta/2\).
Then the correction's rate is strictly below
\(M_{r,n}-c\sum_{\alpha_j=0}(1-\cos\tau_{b_j})\).
This proves (10a) at both parities. It supplies no angular
loss in a slot on which an ordinary normal is taken.

## 8. Scope, coverage and complete direct sources

The positive cone branch and its complete normalization
were already established in [G]. The previously proved
one-leg observation in [F] has a stronger outside angular
loss on its stated range. The zero-power lower-half
lattice-charge initializer uses a Chebyshev charge coupon,
not \(A\), and the high-degree isolated theorem treats the
unit-charge source without this insertion. Neither is
being replaced by a formal change of charge.

Here the new conclusion is for the full single-\(A\)
multi-leg co-source, at every fixed integer power, with
its central normal and even high correction retained.
It allows arbitrary later joint exterior contractions,
but does not estimate them. Formula (7) is at complete
outside values; no fixed free-color relative packet,
angular decay in differentiated slots, global geometric-cycle
transport or arbitrary-short-filling theorem is asserted.
The literal cutoff forcing \(A\otimes B\) remains a
different insertion from a middle edge \(A\otimes A\).

The complete direct texts and their used implications
were read at the following versions:

* [C: Exact cutoff and middle-factor observations](research_cutoff_cluster_exact_reduction.md),
  SHA256 50d126430f711407c5815d840c401c30fef0c09f018fad1a5dfbef60eca81374.
* [F: Free-boundary half-charge observation](research_free_boundary_half_charge_observation.md),
  SHA256 871e2a286f6c8eb90572badf45d454e9c0042537719ce8b3881d22dc5d7fff5b.
* [E: Even complete low kernel](research_even_complete_low_kernel.md),
  SHA256 ea3a8b7becbed501a28969f9cd6715c2b5e0b660aba7c5eb57229b1977220ed1.
* [R: Last physical row](research_last_physical_row_riccati.md),
  SHA256 a6a79106b81b94f5d163022b056c9c6a51e0cdb4f602f090c9f3401436f87c7d.
* [G: Isolated-vertex cone geometry](research_isolated_internal_vertex_geometry.md),
  SHA256 84719ed6ce670d9e5a91d434ea3007d53abf6d1ef9d5a525e90bed6bd83bce0f.

Only written mathematics, source-text reads and hashes were
used. No mathematical program, numerical experiment, test
or build was run. Frozen notes and public papers were unchanged.
